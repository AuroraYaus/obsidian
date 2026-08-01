# 6 Random access procedure

If the UE is configured with a SCG, the UE shall apply the procedures described in this clause for both MCG and SCG

- When the procedures are applied for MCG, the terms 'secondary cell', 'secondary cells', 'serving cell', 'serving cells' in this clause refer to secondary cell, secondary cells, serving cell, serving cells belonging to the MCG respectively.

- When the procedures are applied for SCG, the terms 'secondary cell', 'secondary cells', 'serving cell', 'serving cells' in this clause refer to secondary cell, secondary cells (not including PSCell), serving cell, serving cells belonging to the SCG respectively. The term 'primary cell' in this clause refers to the PSCell of the SCG

For a UE configured with EN-DC/NE-DC and serving cell frame structure type 1, if the UE is configured with tdm-PatternConfig/tdm-PatternConfigNE-DC for the serving cell, the UE is not expected to transmit any uplink physical channel or signal in the serving cell on subframes other than offset-UL subframes, where the offset-UL subframes are determined by applying an offset value given by harq-Offset-r15 to the subframes denoted as uplink in the UL/DL configuration tdm-PatternConfig/tdm-PatternConfigNE-DC.

Prior to initiation of the non-synchronized physical random access procedure, Layer 1 shall receive the following information from the higher layers:

- Random access channel parameters (PRACH configuration and frequency position)

- Parameters for determining the root sequences and their cyclic shifts in the preamble sequence set for the primary cell (index to logical root sequence table, cyclic shift (), and set type (unrestricted or restricted set))

## 6.1 Physical non-synchronized random access procedure

From the physical layer perspective, the L1 random access procedure encompasses the transmission of random access preamble and random access response. The remaining messages are scheduled for transmission by the higher layer on the shared data channel and are not considered part of the L1 random access procedure. A random access channel occupies 6 resource blocks in a subframe or set of consecutive subframes reserved for random access preamble transmissions. The eNodeB is not prohibited from scheduling data in the resource blocks reserved for random access channel preamble transmission.

A UE is not expected to be configured with PRACH on a LAA SCell.

The following steps are required for the L1 random access procedure:

- Layer 1 procedure is triggered upon request of a preamble transmission by higher layers.

- A preamble index, a target preamble received power (PREAMBLE_RECEIVED_TARGET_POWER), a corresponding RA-RNTI and a PRACH resource are indicated by higher layers as part of the request.

- For a BL/CE UE, a number of PRACH repetitions for preamble transmission attempt is also indicated by higher layers as part of the request. For a non-BL/CE UE or for a BL/CE UE with the PRACH coverage enhancement level 0/1/2, a preamble transmission power PPRACH is determined as 
PPRACH = min{, PREAMBLE_RECEIVED_TARGET_POWER +  }_[dBm], where  is the configured UE transmit power defined in [6] for subframe i of serving cell  and  is the downlink path loss estimate calculated in the UE for serving cell . For a BL/CE UE, PPRACH is set to  for the highest PRACH coverage enhancement level 3.

- A preamble sequence is selected from the preamble sequence set using the preamble index.

- A single preamble is transmitted using the selected preamble sequence with transmission power PPRACH on the indicated PRACH resource. For a BL/CE UE, the single preamble is transmitted for the number of PRACH repetitions for the associated PRACH coverage enhancement level as indicated by higher layers.

- For non-BL/CE UEs, detection of a PDCCH with the indicated RA-RNTI is attempted during a window controlled by higher layers (see [8], Clause 5.1.4). If detected, the corresponding DL-SCH transport block is passed to higher layers. The higher layers parse the transport block and indicate the 20-bit uplink grant to the physical layer, which is processed according to Clause 6.2.

- For BL/CE UEs, detection of a MPDCCH with DCI scrambled by RA-RNTI is attempted during a window controlled by higher layers (see [8], Clause 5.1.4). If detected, the corresponding DL-SCH transport block is passed to higher layers. The higher layers parse the transport block and indicate the Nr-bit uplink grant to the physical layer, which is processed according to Clause 6.2.

### 6.1.1 Timing

Throughout this clause, for a BL/CE UE, if the UE is configured with the higher layer parameter k-Offset,

- $ K_{offset}=K_{cell\_offset}-K_{UE\_offset}$ where

$ K_{cell\_offset}$ is the parameter k-Offset provided by higher layers, and

$ K_{UE\_offset}$ is the parameter Differential Koffset provided by higher layers, otherwise $ K_{UE\_offset}=0 $

otherwise,

- $ K_{offset}=0 $, $ K_{cell\_offset}=0 $.

If the UE is configured with higher layer parameter k-Offset, for a PUSCH (re)transmission associated with the TC-RNTI, $ K_{offset}=$ k-Offset.

For the L1 random access procedure, a non-BL/CE UE's uplink transmission timing after a random access preamble transmission is as follows.

a) If a PDCCH with associated RA-RNTI is detected in subframe n, and the corresponding DL-SCH transport block contains a response to the transmitted preamble sequence, the UE shall, according to the information in the response, transmit an UL-SCH transport block in the first subframe . If the UE supports reduced control plane latency and reducedControlPlaneLatency is enabled, ![](media_svg/image7.svg) [公式: k_{1}÷5], otherwise, ![](media_svg/image8.svg) [公式: k_{1}÷6]. If the UL delay field in Clause 6.2 is set to zero,  is the first available UL subframe for PUSCH transmission, where for TDD serving cell, the first UL subframe for PUSCH transmission is determined based on the UL/DL configuration (i.e., the parameter subframeAssignment) indicated by higher layers. The UE shall postpone the PUSCH transmission to the next available UL subframe after  if the field is set to 1.

b) If a random access response is received in subframe n, and the corresponding DL-SCH transport block does not contain a response to the transmitted preamble sequence, the UE shall, if requested by higher layers, be ready to transmit a new preamble sequence no later than in subframe .

c) If no random access response is received in subframe n, where subframe n is the last subframe of the random access response window, the UE shall, if requested by higher layers, be ready to transmit a new preamble sequence no later than in subframe , except if the transmitted preamble sequence is on a TDD serving cell not configured for PUSCH/PUCCH transmission.

For the L1 random access procedure, a BL/CE UE's uplink transmission after a random access preamble transmission is as follows.

a) If a MPDCCH with associated RA-RNTI is detected and the corresponding DL-SCH transport block reception ending in subframe n contains a response to the transmitted preamble sequence, the UE shall, according to the information in the response, transmit an UL-SCH transport block in the first subframe $ n+k_{1}+K_{offset}$, , if the UL delay field in Clause 6.2 is set to zero where the subframe $ n+k_{1}+K_{offset}$ is the first available UL subframe for PUSCH transmission, where for TDD serving cell, the first UL subframe for PUSCH transmission is determined based on the UL/DL configuration (i.e., the parameter subframeAssignment) indicated by higher layers.

When the number of Msg3 PUSCH repetitions, , as indicated in the random access response, is greater than 1, the subframe $ n+k_{1}+K_{offset}$ is the first available UL subframe in the set of BL/CE UL subframes. The UE shall postpone the PUSCH transmission to the next available UL subframe after $ n+k_{1}+K_{offset}+∆$, if the UL delay field is set to 1.

When the number of Msg3 PUSCH repetitions,, as indicated in the random access response, is equal to 1, the subframe $ n+k_{1}+K_{offset}$ is the first available UL subframe for PUSCH transmission determined by for FDD and the parameter subframeAssignment for TDD. The UE shall postpone the PUSCH transmission to the next available UL subframe after $ n+k_{1}+K_{offset}+∆$, if the UL delay field is set to 1.

b) If a random access response is received and its reception ends in subframe n, and the corresponding DL-SCH transport block does not contain a response to the transmitted preamble sequence, the UE shall, if requested by higher layers, be ready to transmit a new preamble sequence no later than in subframe $ n+5+K_{offset}$.

c) If the most recent PRACH coverage enhancement level for the UE is 0 or 1,

- if no random access response is received in subframe n, where subframe n is the last subframe of the random access response window, the UE shall, if requested by higher layers, be ready to transmit a new preamble sequence no later than in subframe $ n+4+K_{offset}$.

If the most recent PRACH coverage enhancement level for the UE is 2 or 3,

- if no MPDCCH scheduling random access response is received in subframe n, where subframe n is the last subframe of the random access response window, the UE shall, if requested by higher layers, be ready to transmit a new preamble sequence no later than in subframe $ n+4+K_{offset}$;

- if an MPDCCH with associated RA-RNTI is detected and the corresponding DL-SCH transport block reception ending in subframe n cannot be successfully decoded, the UE shall, if requested by higher layers, be ready to transmit a new preamble sequence no later than in subframe $ n+4+K_{offset}$.

In case a random access procedure is initiated by a "PDCCH order" in subframe n for non-BL/CE UEs, the UE shall, if requested by higher layers, transmit random access preamble in the first subframe , , where a PRACH resource is available.

In case a random access procedure is initiated by a "PDCCH order" reception ending in subframe n for BL/CE UEs, the UE shall, if requested by higher layers, transmit random access preamble in the first subframe $ n+k_{2}+K_{cell\_offset}$,, where a PRACH resource is available.

If a UE is configured with multiple TAGs, and if the UE is configured with the carrier indicator field for a given serving cell, the UE shall use the carrier indicator field value from the detected "PDCCH order" to determine the serving cell for the corresponding random access preamble transmission.

## 6.2 Random Access Response Grant

The higher layers indicate the Nr-bit UL Grant to the physical layer, as defined in 3GPP TS36.321 [8]. 
This is referred to the Random Access Response Grant in the physical layer.

If BL/CE UE then

- If the most recent PRACH coverage enhancement level for the UE is 0 or 1, the contents of the Random Access Response Grant are interpreted according to CEModeA.

- If the most recent PRACH coverage enhancement level for the UE is 2 or 3, the contents of the Random Access Response Grant are interpreted according to CEModeB.

- The content of these Nr bits starting with the MSB and ending with the LSB are given in Table 6-2 for CEmodeA and CEmodeB if the higher layers do not indicate EDT to the physical layer as defined in [8], and in Table 6.2-F if the higher layers indicate EDT.:

- where  =  and

Table 6-2: Random Access Response Grant Content field size

| DCI contents | CEmodeA | CEmodeB |
| --- | --- | --- |
| Msg3 PUSCH narrowband index |  | 2 |
| Msg3 PUSCH Resource allocation | 4 | 3 |
| Number of Repetitions for Msg3 PUSCH | 2 | 3 |
| MCS | 3 | 0 |
| TBS | 0 | 2 |
| TPC | 3 | 0 |
| CSI request | 1 | 0 |
| UL delay | 1 | 0 |
| Msg3/4 MPDCCH narrowband index | 2 | 2 |
| Zero padding | 4 - | 0 |
| Total Nr-bits | 20 | 12 |

Table 6.2-F: Random Access Response Grant Content field size for EDT

| DCI contents | CEmodeA | CEmodeB |
| --- | --- | --- |
| Msg3 PUSCH narrowband index | ![](media_svg/image20.svg) [公式≈: _{N}_{NB}index] | 3 |
| Msg3 PUSCH Resource allocation | 5 | 3 |
| Number of Repetitions for Msg3 PUSCH | 2 | 3 |
| TPC | 3 | 0 |
| CSI request | 1 | 0 |
| UL delay | 1 | 0 |
| Msg3/4 MPDCCH narrowband index | ![](media_svg/image20.svg) [公式≈: _{N}_{NB}index] | 3 |
| Zero padding | 8 - ![](media_svg/image21.svg) [公式≈: _{2}_{∪}_{N}_{NB}index] | 0 |
| Total Nr-bits | 20 | 12 |

- For CEmodeB, the Msg3 PUSCH narrowband index indicates the narrowband to be used for first subframe of Msg3 PUSCH transmission as given in Table 6.2-A if the higher layers do not indicate EDT to the physical layer as defined in [8], Table 6.2-G otherwise.

- given in Table 6.2-A, Table 6.2-B and Table 6.2-G is the narrow band used for first subframe of MPDCCH for Random Access Response and is determined by higher layer parameter mpdcch-NarrowbandsToMonitor-r13 if only one narrowband is configured, otherwise, it is determined by Table 6-2-E.

Table 6.2-A: Msg3 PUSCH Narrowband Value for CEmodeB.

| Value of 'Msg3 narrowband index' | Msg3 PUSCH Narrowband |
| --- | --- |
| '00' |  |
| '01' |  |
| '10' |  |
| '11' |  |

Table 6.2-G: Msg3 PUSCH Narrowband Value for CEmodeB and EDT.

| Value of 'Msg3 narrowband index' | Msg3 PUSCH Narrowband |
| --- | --- |
| '000' | ![](media_svg/image23.svg) [公式≈: NB_{RAR}modN_{NB}] |
| '001' | ![](media_svg/image24.svg) [公式≈: (NB_{RAR}+1)modN_{NB}] |
| '010' | ![](media_svg/image25.svg) [公式≈: (NB_{RAR}+2)modN_{NB}] |
| '011' | ![](media_svg/image26.svg) [公式≈: (NB_{RAR}+3)modN_{NB}] |
| '100' | ![](media_svg/image27.svg) [公式≈: (NBN_{RARNB}+4mod)] |
| '101' | ![](media_svg/image28.svg) [公式≈: (NBN_{RARNB}+5mod)] |
| '110' | ![](media_svg/image29.svg) [公式≈: (NBN_{RARNB}+6mod)] |
| '111' | ![](media_svg/image30.svg) [公式≈: (NBN_{RARNB}+7mod)] |

- The Msg3/4 MPDCCH narrowband index indicates the narrowband used for first subframe of MPDCCH configured by Temporary C-RNTI and/or C-RNTI during random access procedure as given in Table 6.2-B if the higher layers do not indicate EDT to the physical layer as defined in [8], value of ![](media_svg/image20.svg) [公式≈: _{N}_{NB}index] for CEModeA and Table 6.2-H for CEModeB otherwise. The number of downlink narrowbands is given by  = .

Table 6.2-B: Msg3/4 MPDCCH Narrowband Value for CEmodeA and CEmodeB.

| Value of 'Msg3/4 MPDCCH narrowband index' | Msg3/4 MPDCCH Narrowband |
| --- | --- |
| '00' |  |
| '01' |  |
| '10' |  |
| '11' |  |

Table 6.2-H: Msg3/4 MPDCCH Narrowband Value for CEmodeB and EDT.

| Value of 'Msg3/4 MPDCCH narrowband index' | Msg3/4 MPDCCH Narrowband |
| --- | --- |
| '000' | ![](media_svg/image33.svg) [公式≈: ^{NBN}RARNB^{mod}2] |
| '001' | ![](media_svg/image34.svg) [公式≈: (NBN_{RARNB}+1mod)_{2}] |
| '010' | ![](media_svg/image35.svg) [公式≈: (NBN_{RARNB}+2mod)_{2}] |
| '011' | ![](media_svg/image36.svg) [公式≈: (NBN_{RARNB}+3mod)_{2}] |
| '100' | ![](media_svg/image37.svg) [公式≈: (NBN_{RARNB}+4mod)_{2}] |
| '101' | ![](media_svg/image38.svg) [公式≈: (NBN_{RARNB}+5mod)_{2}] |
| '110' | ![](media_svg/image39.svg) [公式≈: (NBN_{RARNB}+6mod)_{2}] |
| '111' | ![](media_svg/image40.svg) [公式≈: (NBN_{RARNB}+7mod)_{2}] |

- The repetition number field in the random access response grant configured by higher layers indicates the repetition level (![](media_svg/image41.svg) [公式≈: ^{N}Msg3]) for the initial transmission of Msg3 PUSCH as given in Table 6.2-C for CEmodeA and Table 6.2-D for CEmodeB, where

-  is determined by higher layer parameter pusch-maxNumRepetitionCEmodeA-r13 if it is signaled, otherwise  = 8,

-  is determined by higher layer parameter pusch-maxNumRepetitionCEmodeB-r13 if it is signaled, otherwise  = 512.

If the higher layers indicate EDT to the physical layer as defined in [8] and if the UE is configured with higher layer parameter edt-SmallTBS-Enabled-r15, the repetition number for the initial transmission of Msg3 PUSCH is the smallest integer multiple of M  that is equal to or larger than![](media_svg/image44.svg) [公式≈: ^{TBSTBSN}MsgMsgMsg33,max3^{∪}] where ![](media_svg/image45.svg) [公式≈: ^{TBS}Msg3] is the TBS of Msg3 PUSCH as determined in clause 8.6.2, and ![](media_svg/image46.svg) [公式≈: ^{TBS}Msg3,max] is the value of the higher layer parameter edt-TBS-r15. M=4 if ![](media_svg/image41.svg) [公式≈: ^{N}Msg3]> 4, M = 1 otherwise.

Table 6.2-C: Msg3 PUSCH Repetition Level Value for CEmodeA.

| Value of 'Repetition number' | Msg3 PUSCH Repetition level |
| --- | --- |
| '00' |  |
| '01' |  |
| '10' |  |
| '11' |  |

Table 6.2-D: Msg3 PUSCH Repetition Level Value for CEmodeB.

| Value of 'Repetition number' | Msg3 PUSCH Repetition level |
| --- | --- |
| '000' |  |
| '001' |  |
| '010' |  |
| '011' |  |
| '100' |  |
| '101' |  |
| '110' |  |
| '111' |  |

Table 6.2-E: Narrowband () for MPDCCH RAR.

| Mapped Preamble Index |  |
| --- | --- |
| mod( Preamble Index, 2 )=0 | First narrowband configured by high layer parameter mpdcch-NarrowbandsToMonitor-r13 |
| mod( Preamble Index, 2 )=1 | Second narrowband configured by high layer parameter mpdcch-NarrowbandsToMonitor-r13 |

- The resource allocation field is interpreted as follows:

- For CEmodeA,

- if the higher layers indicate EDT to the physical layer as defined in [8], then

- interpret the resource allocation using UL resource allocation type 0 within the indicated narrowband

- else,

- insert one most significant bit with value set to '0', and interpret the expanded resource allocation using UL resource allocation type 0 within the indicated narrowband.

- For CEmodeB, interpret the resource allocation using UL resource allocation type 2 within the indicated narrowband.

- The truncated modulation and coding scheme field is interpreted such that the modulation and coding scheme corresponding to the Random Access Response grant is determined from MCS indices 0 through 7 for CEmodeA in Table 8.6.1-1

The truncated TBS field is interpreted such that the TBS value corresponding to the Random Access Response grant is determined from TBS indices 0 through 3 for CEmodeB in Table 7.1.7.2.1-1

else,

- Nr=20, and the content of these 20 bits starting with the MSB and ending with the LSB are as follows:

- Hopping flag – 1 bit

- Fixed size resource block assignment – 10 bits

- Truncated modulation and coding scheme – 4 bits

If a UE is performing non-contention based random access procedure and is configured with higher layer parameter pusch-EnhancementsConfig, then

- Repetition number of Msg3 – 3 bits

else

- TPC command for scheduled PUSCH – 3 bits

- UL delay – 1 bit

- CSI request – 1 bit

- The UE shall use the single-antenna port uplink transmission scheme for the PUSCH transmission corresponding to the Random Access Response Grant and the PUSCH retransmission for the same transport block.

- The UE shall perform PUSCH frequency hopping if the single bit frequency hopping (FH) field in a corresponding Random Access Response Grant is set as 1 and the uplink resource block assignment is type 0, otherwise no PUSCH frequency hopping is performed. When the hopping flag is set, the UE shall perform PUSCH hopping as indicated via the fixed size resource block assignment detailed below.

- The fixed size resource block assignment field is interpreted as follows:

- if

- Truncate the fixed size resource block assignment to its b least significant bits, where , and interpret the truncated resource block assignment according to the rules for a regular DCI format 0

- else

- Insert b most significant bits with value set to '0' after the NUL_hop hopping bits in the fixed size resource block assignment, where the number of hopping bits NUL_hop is zero when the hopping flag bit is not set to 1, and is defined in Table 8.4-1 when the hopping flag bit is set to 1, and , and interpret the expanded resource block assignment according to the rules for a regular DCI format 0

- end if

- The truncated modulation and coding scheme field is interpreted such that the modulation and coding scheme corresponding to the Random Access Response grant is determined from MCS indices 0 through 15 in Table 8.6.1-1.

- The TPC command  shall be used for setting the power of the PUSCH, and is interpreted according to Table 6.2-1.

end if

Table 6.2-1: TPC Command  for Scheduled PUSCH

| TPC Command | Value (in dB) |
| --- | --- |
| 0 | -6 |
| 1 | -4 |
| 2 | -2 |
| 3 | 0 |
| 4 | 2 |
| 5 | 4 |
| 6 | 6 |
| 7 | 8 |

In non-contention based random access procedure, the CSI request field is interpreted to determine whether an aperiodic CQI, PMI, RI, and CRI report is included in the corresponding PUSCH transmission according to Clause 7.2.1. In contention based random access procedure, the CSI request field is reserved.

The UL delay applies for TDD, FDD and FDD-TDD and this field can be set to 0 or 1 to indicate whether the delay of PUSCH is introduced as shown in Clause 6.1.1. A BL/CE UE interpreting the contents of the random access response according to CEModeB shall follow the description of UL delay field set to 0.

# 7 Physical downlink shared channel related procedures

If the UE is configured with a SCG, the UE shall apply the procedures described in this clause for both MCG and SCG unless stated otherwise

- When the procedures are applied for MCG, the terms 'secondary cell', 'secondary cells', 'serving cell', and 'serving cells' in this clause refer to secondary cell, secondary cells, serving cell or serving cells belonging to the MCG respectively unless stated otherwise. The terms 'subframe' and 'subframes' refer to subframe or subframes belonging to MCG.

- When the procedures are applied for SCG, the terms 'secondary cell', 'secondary cells', 'serving cell' and 'serving cells' in this clause refer to secondary cell, secondary cells (not including the PSCell), serving cell, serving cells belonging to the SCG respectively unless stated otherwise. The term 'primary cell' in this clause refers to the PSCell of the SCG. The terms 'subframe' and 'subframes' refer to subframe or subframes belonging to SCG

If a UE is configured with dl-TTI-Length, and PDSCH is received in a slot, the term 'slot/subslot' refers to a slot in this clause.

If the UE is configured with dl-TTI-Length, and PDSCH is received in a subslot, the term 'slot/subslot' refers to a subslot in this clause.

If a UE is configured with a LAA Scell, the UE shall apply the procedures described in this clause assuming frame structure type 1 for the LAA Scell unless stated otherwise.

For FDD,

- if the UE supports ce-pdsch-tenProcesses and is configured with CEModeA and higher layer parameter ce-pdsch-tenProcesses-config set to 'On' there shall be a maximum of 10 downlink HARQ processes per serving cell;

- if the BL/CE UE is configured with higher layer parameter ce-PDSCH-14HARQ-Config, and configured with CEModeA, there shall be a maximum of 14 downlink HARQ processes per serving cell.

- 16 downlink HARQ processes per serving cell configured with higher layer parameter dl-TTI-Length

- otherwise, there shall be a maximum of 8 downlink HARQ processes per serving cell.

For FDD-TDD and primary cell frame structure type 1, there shall be a maximum of

- 16 downlink HARQ processes per serving cell configured with higher layer parameter dl-TTI-Length

- 8 downlink HARQ processes per serving cell, otherwise.

For TDD and a UE not configured with the parameter EIMTA-MainConfigServCell-r12 for any serving cell,, if the UE is configured with one serving cell, or if the UE is configured with more than one serving cell and the TDD UL/DL configuration of all the configured serving cells is the same, the maximum number of downlink HARQ processes per serving cell configured with higher layer parameter dl-TTI-Length shall be 16, otherwise determined by the UL/DL configuration (Table 4.2-2 of [3]), as indicated in Table 7-1.

For TDD, if a UE is configured with more than one serving cell and if the TDD UL/DL configuration of at least two configured serving cells is not the same, or if the UE is configured with the parameter EIMTA-MainConfigServCell-r12 for at least one serving cell, or for FDD-TDD and primary cell frame structure type 2 and serving cell frame structure type 2, the maximum number of downlink HARQ processes for a serving cell configured with higher layer parameter dl-TTI-Length shall be 16, otherwise determined as indicated in Table 7-1, wherein the "TDD UL/DL configuration" in Table 7-1 refers to the DL-reference UL/DL configuration for the serving cell (as defined in Clause 10.2).

For FDD-TDD and primary cell frame structure type 2 and serving cell frame structure type 1, the maximum number of downlink HARQ processes for the serving cell configured with higher layer parameter dl-TTI-Length shall be 16, otherwise determined by the DL-reference UL/DL configuration for the serving cell (as defined in Clause 10.2), as indicated in Table 7-2.

A BL/CE UE configured with CEModeB is not expected to support more than 4 downlink HARQ processes if the UE is configured with higher layer parameter ce-PDSCH-MultiTB-Config, 2 downlink HARQ processes otherwise.

For TDD and a BL/CE configured with CEModeA, the maximum number of downlink HARQ processes for a serving cell shall be determined as indicated in Table 7-3.

For a UE configured with EN-DC/NE-DC, if serving cell frame structure type 1 and if the UE is configured with tdm-PatternConfig/tdm-PatternConfigNE-DC for the serving cell, or if the UE is configured with tdm-PatternConfig2 for a serving cell with EN-DC, the maximum number of downlink HARQ processes for the serving cell shall be determined by DL-reference UL/DL configuration given by tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 for the serving cell, as indicated in Table 7-2.

For a UE configured with EN-DC/NE-DC and more than one serving cells, if primary cell frame structure type 1 and if the UE is configured with tdm-PatternConfig/tdm-PatternConfigNE-DC for the primary cell, or if the UE is configured with tdm-PatternConfig2 for a primary cell with EN-DC, the maximum number of downlink HARQ processes for each secondary cell is equal to the maximum number of downlink HARQ processes for the primary cell.

The dedicated broadcast HARQ process defined in [8] is not counted as part of the maximum number of HARQ processes for FDD, TDD and FDD-TDD.

Table 7-1: Maximum number of DL HARQ processes for TDD

| TDD UL/DL configuration | Maximum number of HARQ processes |
| --- | --- |
| 0 | 4 |
| 1 | 7 |
| 2 | 10 |
| 3 | 9 |
| 4 | 12 |
| 5 | 15 |
| 6 | 6 |

Table 7-2: Maximum number of DL HARQ processes for FDD-TDD, primary cell frame structure type 2, and serving cell frame structure type 1

| DL-reference UL/DLConfiguration | Maximum number of HARQ processes |
| --- | --- |
| 0 | 10 |
| 1 | 11 |
| 2 | 12 |
| 3 | 15 |
| 4 | 16 |
| 5 | 16 |
| 6 | 12 |

Table 7-3: Maximum number of DL HARQ processes for TDD
(UE configured with CEModeA)

| TDD UL/DL configuration | Maximum number of HARQ processes |
| --- | --- |
| 0 | 6 |
| 1 | 9 |
| 2 | 12 |
| 3 | 11 |
| 4 | 14 |
| 5 | 16 |
| 6 | 8 |

## 7.1 UE procedure for receiving the physical downlink shared channel

Except the subframes indicated by the higher layer parameter mbsfn-SubframeConfigList or by mbsfn-SubframeConfigList-v1250 or by mbsfn-SubframeConfigList-v14xy or by laa-SCellSubframeConfig of serving cell , a UE shall

- upon detection of a PDCCH of the serving cell with DCI format 1, 1A, 1B, 1C, 1D, 2, 2A, 2B, 2C, or 2D intended for the UE in a subframe, or

- upon detection of an EPDCCH of the serving cell with DCI format 1, 1A, 1B, 1D, 2, 2A, 2B, 2C, or 2D intended for the UE in a subframe, or

- upon detection of a PDCCH of the serving cell with DCI format 7-1A, 7-1B, 7-1C, 7-1D, 7-1E, 7-1F, 7-1G intended for the UE in the first slot/subslot of a subframe

- upon detection of a SPDCCH of the serving cell with DCI format 7-1A, 7-1B, 7-1C, 7-1D, 7-1E, 7-1F, 7-1G intended for the UE in a slot/subslot

decode the corresponding PDSCH in the same subframe/slot/subslot with the restriction of the number of transport blocks defined in the higher layers, unless specified otherwise.

For a given serving cell, if the UE is configured with higher layer parameter blindSubframePDSCH-Repetitions, the UE shall upon detection of a PDCCH/EPDCCH with DCI format 1A with CRC scrambled by C-RNTI in UE-specific search space of subframe n, intended for the UE, decode, starting from subframe n, the corresponding PDSCH transmission in k consecutive DL subframe(s) according to the PDCCH information, where the value of k is determined by the repetition number field in the corresponding DCI. For k>1,

- if the UE is configured with transmission mode 1, 2, 3, 4, 5, 6, 7 or 8 for the serving cell, the k consecutive DL subframes do not include MBSFN subframe(s).

- the UE shall assume the truncated modulation and coding scheme field is interpreted such that the modulation and coding scheme corresponding to DCI format 1A is determined from MCS indices 0 through 15 if the higher layer parameter MCS-restrictionSubframePDSCH-Repetitions is set to '1'.

- The UE shall assume all the k PDSCH data transmissions are received in the same resource blocks.

- For TDD cell, the k consecutive DL subframes include the k DL subframes or special subframes according to the UL/DL configuration indicated by higher layer parameter subframeAssignment for the serving cell.

- If the UE is configured with higher layer parameter EIMTA-MainConfigServCell-r12, the UE shall discard any PDCCH/EPDCCH for PDSCH data transmission with k>1 in a subframe which has been indicated as an UL subframe or a special subframe by higher layer parameter subframeAssignment but indicated as a DL subframe by a PDCCH with CRC scrambled by eIMTA-RNTI containing an UL/DL configuration for the serving cell.

For a given serving cell, if the UE is configured with higher layer parameter blindSlotSubslotPDSCH-Repetitions, the UE shall upon detection of a PDCCH/SPDCCH with DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G with CRC scrambled by C-RNTI in slot/sublot n, intended for the UE, decode, starting from slot/subslot n, the corresponding PDSCH transmission in k consecutive DL slot(s)/subslot(s) according to the PDCCH/SPDCCH information, where the value of k is determined by the repetition number field in the corresponding DCI. For k>1,

- the UE is not expected to receive the PDSCH data transmissions with more than two transmission layers.

- if the k consecutive DL slots/subslots cross two consecutive subframes with different downlink transmission modes, the UE is not expected to receive the PDSCH data transmissions after the former subframe.

- for DCI format 7-1F/7-1G, the UE shall assume the value of the DMRS position indicator field (defined in 3GPP TS 36.212 [4]) is set to '0'.

- the UE shall assume the modulation and coding scheme corresponding to DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G is determined from MCS indices 0 through 15 if the higher layer parameter MCS-restrictionSlotSubslotPDSCH-Repetitions is set to '1'.

- the UE shall assume the "PDSCH RE Mapping and Quasi-Co-Location Indicator" field is applied to all the k PDSCH data transmissions signaled via PDCCH/SPDCCH with DCI format 7-1G.

- the UE shall assume the "precoding information" field is applied to all the k PDSCH data transmissions signaled via PDCCH/SPDCCH with DCI format 7-1C.

- the UE shall assume the "TPMI information for precoding" field is applied to all the k PDSCH data transmissions signaled via PDCCH/SPDCCH with DCI format 7-1D.

- the UE shall assume all the k PDSCH data transmissions are received in the same resource blocks.

- For FDD cell,

- the UE may assume that the same precoder applies to all scheduled k PDSCH transmissions.

- subslot 0 of a subframe is not counted as a DL subslot for k PDSCH transmissions if the CFI value is 2 or 3.

- For TDD cell,

- the UE may assume that the same precoder applies to those of the k scheduled PDSCH transmissions occur between guard periods of two adjacent special subframes.

- the k consecutive DL slots include the k DL slots of DL subframe or DwPTS according to the UL/DL configuration indicated by higher layer parameter subframeAssignment for the serving cell.

For BL/CE UEs, the set of BL/CE DL subframes is indicated as follows

- If DL resource reservation is enabled for the UE as specified in [11],

- for PDSCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PDSCH transmission without a corresponding MPDCCH,

- if the Resource reservation field in the DCI is set to 0, then the set of BL/CE DL subframes corresponds to all downlink subframes and special subframes during the PDSCH transmission;

- if the Resource reservation field in the DCI is set to 1, then the set of BL/CE DL subframes corresponds to all downlink subframes and special subframes that are not fully reserved according to higher layer parameters (a subframe is considered fully reserved if and only if all OFDM symbols of all PRBs of the PDSCH transmission are reserved in the subframe);

- for MPDCCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space,

- the set of BL/CE DL subframes corresponds to all downlink subframes and available special subframes that are not fully reserved according to higher layer parameters (a subframe is considered fully reserved if and only if all OFDM symbols of all PRBs of the MPDCCH transmission are reserved in the subframe).

- In all other cases, the set of BL/CE DL subframes is indicated by the higher layers according to fdd-DownlinkOrTddSubframeBitmapBR [11].

A BL/CE UE shall upon detection of a MPDCCH with DCI format 6-1A, 6-1B, 6-2 intended for the UE, decode the corresponding PDSCH in one more BL/CE DL subframes as described in Clause 7.1.11, with the restriction of the number of transport blocks defined in the higher layers.

For a BL/CE UE in a NTN FDD serving cell with a PDSCH ending in subframe n, and the UE configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap or higher layer parameter downlinkHARQ-FeedbackDisabledDCI, if the UE shall not provide HARQ-ACK for a HARQ process associated with a transport block in the PDSCH, the UE is not expected to receive a MPDCCH or a PDSCH without a corresponding MPDCCH for the same HARQ process as the PDSCH ending in subframe n in any BL/CE DL subframe starting from subframe n+1 to subframe n+3.

For the purpose of decoding PDSCH containing SystemInformationBlockType2, a BL/CE UE shall assume that subframes in which SystemInformationBlockType2 is scheduled are non-MBSFN subframes.

If a UE is configured with more than one serving cell and if the frame structure type of any two configured serving cells is different, then the UE is considered to be configured for FDD-TDD carrier aggregation.

Except for MBMS reception, the UE is not required to monitor PDCCH with CRC scrambled by the SI-RNTI on the PSCell.

A UE may assume that positioning reference signals are not present in resource blocks in which it shall decode PDSCH according to a detected PDCCH with CRC scrambled by the SI-RNTI or P-RNTI with DCI format 1A or 1C intended for the UE.

A UE configured with the carrier indicator field for a given serving cell shall assume that the carrier indicator field is not present in any PDCCH of the serving cell in the common search space that is described in Clause 9.1. Otherwise, the configured UE shall assume that for the given serving cell the carrier indicator field is present in PDCCH/EPDCCH located in the UE specific search space described in Clause 9.1 when the PDCCH/EPDCCH CRC is scrambled by C-RNTI or SPS C-RNTI.

If a UE is configured by higher layers to decode PDCCH with CRC scrambled by the SI-RNTI, the UE shall decode the PDCCH and the corresponding PDSCH according to any of the combinations defined in Table 7.1-1. The scrambling initialization of PDSCH corresponding to these PDCCHs is by SI-RNTI.

A UE operating in an MBMS-dedicated carrier may be configured with two SI-RNTI values, in which case the UE shall apply the procedure described in this clause for each of the SI-RNTIs.

Table 7.1-1: PDCCH and PDSCH configured by SI-RNTI

| DCI format | Search Space | Transmission scheme of PDSCH corresponding to PDCCH |
| --- | --- | --- |
| DCI format 1C | Common | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2). |
| DCI format 1A | Common | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2). |

For BL/CE UE, for PDSCH carrying SystemInformationBlockType1-BR and SI-messages, the UE shall decode PDSCH according to Table 7.1-1A. The scrambling initialization of PDSCH is by SI-RNTI.

Table 7.1-1A: PDSCH configured by SI-RNTI

| Transmission scheme of PDSCH |
| --- |
| If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2). |

If a UE is configured with higher layer parameter ce-ETWS-CMAS-RxInConn and configured by higher layers to decode MPDCCH with CRC scrambled by the SI-RNTI, the UE shall decode the MPDCCH according to any of the combinations defined in Table 7.1-1B.

Table 7.1-1B: MPDCCH configured by SI-RNTI

| DCI format | Search Space |
| --- | --- |
| 6-1A or 6-1B | Type0-common |

If a UE is configured by higher layers to decode PDCCH with CRC scrambled by the P-RNTI, the UE shall decode the PDCCH and the corresponding PDSCH according to any of the combinations defined in Table 7.1-2. 
The scrambling initialization of PDSCH corresponding to these PDCCHs is by P-RNTI.

If a UE is configured by higher layers to decode MPDCCH with CRC scrambled by the P-RNTI, the UE shall decode the MPDCCH and any corresponding PDSCH according to any of the combinations defined in Table 7.1-2A. 
The scrambling initialization of PDSCH corresponding to these MPDCCHs is by P-RNTI.

The UE is not required to monitor PDCCH with CRC scrambled by the P-RNTI on the PSCell.

Table 7.1-2: PDCCH and PDSCH configured by P-RNTI

| DCI format | Search Space | Transmission scheme of PDSCH corresponding to PDCCH |
| --- | --- | --- |
| DCI format 1C | Common | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |
| DCI format 1A | Common | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |

Table 7.1-2A: MPDCCH and PDSCH configured by P-RNTI

| DCI format | Search Space | Transmission scheme of PDSCH corresponding to MPDCCH |
| --- | --- | --- |
| 6-2 | Type1-common | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |

If a UE is configured by higher layers to decode PDCCH with CRC scrambled by the RA-RNTI, the UE shall decode the PDCCH and the corresponding PDSCH according to any of the combinations defined in Table 7.1-3. The scrambling initialization of PDSCH corresponding to these PDCCHs is by RA-RNTI.

If a UE is configured by higher layers to decode MPDCCH with CRC scrambled by the RA-RNTI, the UE shall decode the MPDCCH and the corresponding PDSCH according to any of the combinations defined in Table 7.1-3A. The scrambling initialization of PDSCH corresponding to these MPDCCHs is by RA-RNTI.

When RA-RNTI and either C-RNTI or SPS C-RNTI are assigned in the same subframe, the UE is not required to decode a PDSCH on the primary cell indicated by a PDCCH/EPDCCH/SPDCCH with a CRC scrambled by C-RNTI or SPS C-RNTI.

Table 7.1-3: PDCCH and PDSCH configured by RA-RNTI

| DCI format | Search Space | Transmission scheme of PDSCH corresponding to PDCCH |
| --- | --- | --- |
| DCI format 1C | Common | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |
| DCI format 1A | Common | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |

Table 7.1-3A: MPDCCH and PDSCH configured by RA-RNTI

| DCI format | Search Space | Transmission scheme of PDSCH corresponding to MPDCCH |
| --- | --- | --- |
| 6-1A or 6-1B | Type2-common | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |

If a UE is configured by higher layers to decode PDCCH with CRC scrambled by the G-RNTI or SC-RNTI, the UE shall decode the PDCCH and the corresponding PDSCH according to any of the combinations defined in Table 7.1-4. The scrambling initialization of PDSCH corresponding to these PDCCHs is by G-RNTI or SC-RNTI.

Table 7.1-4: PDCCH and PDSCH configured by G-RNTI or SC-RNTI

| DCI format | Search Space | Transmission scheme of PDSCH corresponding to PDCCH |
| --- | --- | --- |
| DCI format 1C | Common | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2). |
| DCI format 1A | Common | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2). |

If a UE is configured by higher layers to decode PDCCH with CRC scrambled by the SC-N-RNTI, the UE shall decode the PDCCH according to the combination defined in table 7.1-4A.

Table 7.1-4A: PDCCH configured by SC-N-RNTI

| DCI format | Search Space |
| --- | --- |
| DCI format 1C | Common |

If a UE is configured by higher layers to decode MPDCCH with CRC scrambled by the SC-RNTI, the UE shall decode the MPDCCH according to the combination defined in table 7.1-4B.

Table 7.1-4B: MPDCCH and PDSCH configured by SC-RNTI

| DCI format | Search Space | Transmission scheme of PDSCH corresponding to MPDCCH |
| --- | --- | --- |
| 6-2 | Type1A-common | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |

If a UE is configured by higher layers to decode MPDCCH with CRC scrambled by the G-RNTI, the UE shall decode the MPDCCH according to the combination defined in table 7.1-4C.

Table 7.1-4C: MPDCCH and PDSCH configured by G-RNTI

| DCI format | Search Space | Transmission scheme of PDSCH corresponding to MPDCCH |
| --- | --- | --- |
| 6-1A or 6-1B | Type2A-common | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |

The UE is semi-statically configured via higher layer signalling to receive PDSCH data transmissions signalled via PDCCH/EPDCCH with DCI formats other than 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G according to one of the transmission modes, denoted mode 1 to mode 10. If the UE is configured with higher layer parameter dl-TTI-Length, the UE is semi-statically configured via higher layer signalling to receive PDSCH transmissions signalled via PDCCH/SPDCCH with DCI formats 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G according to

- one of the transmission modes, denoted mode 1, 2, 3, 4, 6, 9, 10 for frame structure type 1, and mode 1,2,3,4,6,8,9,10 for frame structure type 2 in non-MBSFN subframes.

- one of the transmission modes, denoted mode 9, 10 for frame structure type 1 and frame structure type 2 in MBSFN subframes

For a BL/CE UE, the UE is semi-statically configured via higher layer signalling to receive PDSCH data transmissions signalled via MPDCCH according to one of the transmission modes: mode 1, mode 2, mode 6, and mode 9.

For LAA Scells, the UE is not expected to receive PDSCH data transmissions signalled via PDCCH/EPDCCH according to transmission modes 5, 6, 7.

For a serving cell, if the UE is configured with higher layer parameter shortTTI, and if the UE does not support pdsch-SlotSubslotPDSCH-Decoding (3GPP TS 36.331 [11]), the UE is not expected to receive PDSCH data transmissions signalled via PDCCH with CRC scrambled by the C-RNTI/SPS C-RNTI and DCI Formats other than DCI Format 7-1 A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G in a subframe, if also PDSCHs assigned by PDCCH/SPDCCH associated with DCI Format 7-1 A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G is received in the same subframe of the same serving cell. Additionally, the UE shall transmit HARQ-ACK associated with both the subframe-PDSCH and slot/subslot-PDSCH, regardless of the support of pdsch-SlotSubslotPDSCH-Decoding.

For a UE configured with higher layer parameter shortTTI, the UE may skip decoding any transport block(s) received in PDSCH transmissions signalled via PDCCH/EPDCCH with CRC scrambled by the C-RNTI/SPS C-RNTI and DCI Formats other than DCI Format 7-1 A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G in the last WDL subframes if the UE has detected PDCCH/SPDCCH associated with DCI Format 7-1 A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G, and if ![](media_svg/image64.svg) [公式: W_{DL}>0] is indicated by skipSubframeProcessing capability [12]. If the UE skips decoding, the physical layer indicates to higher layer that the transport block(s) are not successfully decoded.

For a UE configured with higher layer parameter shortTTI, and for PDSCH data transmissions in subslot n signalled via PDCCH/SPDCCH of a serving cell

- with DCI format 7-1F/7-1G, the UE is not expected to receive UE-specific reference signals corresponding to a transport block mapped to more than two-layer spatial multiplexing in subslot n of subframe N,

- if the UE has received UE-specific reference signals corresponding to a transport block mapped to more than two-layer spatial multiplexing in subslot n-1 of subframe N or

- if n=0 and if the UE has received UE-specific reference signals corresponding to a transport block mapped to more than two-layer spatial multiplexing in subslot 5 of subframe N-1, and if the UE does not support dmrs-RepetitionSubslotPDSCH (3GPP TS 36.331 [11])

- with DCI format 7-1F/7-1G, the UE may assume that UE-specific reference signals were present in those PRGs of subslot n-1, where PDSCH is mapped to

if the DCI associated with the subslot-PDSCH indicates the absence of the UE-specific reference signal in subslot n (See DMRS position indicator field in 3GPP TS 36.212 [4]).

For a serving cell, if the UE is configured with higher layer parameter shortTTI, the UE is not expected to receive

- PDSCH data transmissions signalled via PDCCH/SPDCCH of the serving cell with CRC scrambled by the C-RNTI/SPS C-RNTI and DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G for a transport block corresponding to a HARQ process with NDI not toggled if the previous PDSCH transmission of the transport block was signalled via PDCCH with CRC scrambled by the C-RNTI/SPS C-RNTI with DCI format other than DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G when the number of codewords for the previous PDSCH transmissions is two or the transport block size is more than the maximum transport block size supported for slot/subslot-PDSCH transmission.

- PDSCH data transmissions signalled via PDCCH/SPDCCH of the serving cell with CRC scrambled by the C-RNTI/SPS C-RNTI and DCI format 7-1F/7-1G in subslot n, if the PDCCH/SPDCCH indicates the absence of the UE-specific reference signal in subslot n and

- if n=0 and if the UE does not support dmrs-SharingSubslotPDSCH (3GPP TS 36.331 [11]) or

- if the UE has not received a PDCCH/SPDCCH with CRC scrambled by the C-RNTI/SPS C-RNTI and DCI format 7-1F/7-1G in one subslot before subslot n or

- if the UE has received a PDCCH/SPDCCH with CRC scrambled by the C-RNTI/SPS C-RNTI DCI format 7-1F/7-1G in one subslot before subslot n indicating

- the absence of the UE-specific reference signal in one subslot before subslot n or

- the presence of the UE-specific reference signal in one subslot before subslot n

- if the PDSCH PRGs of one subslot before subslot n do not include all the PDSCH PRGs of subslot n or

- if the number of antenna ports associated with the PDSCH of one subslot before subslot n is less than the number of antenna ports associated with the PDSCH of subslot n or

- if the number of antenna ports associated with the PDSCH of both subslot n and one subslot before subslot n is 1 but different antenna port is indicated between subslot n and one subslot before the subslot n

The UE shall provide the HARQ-ACK response associated with the PDCCH/SPDCCH received in subslot n if the UE has not received a PDCCH/SPDCCH with CRC scrambled by the C-RNTI/SPS C-RNTI and DCI format 7-1F/7-1G in one subslot before the subslot n.

For a UE configured with higher layer parameter shortProcessingTime,

- the UE is not expected to receive PDCCH in common search space for which HARQ-ACK response shall be provided in a subframe n, and PDCCH in UE specific search space for which HARQ-ACK response shall be provided in the same subframe n.

- the UE is not expected to receive PDCCH in common search space in subframe n, and PDCCH in UE specific search space in the same subframe n.

For frame structure type 1,

- the UE is not expected to receive PDSCH resource blocks transmitted on antenna port 5 in any subframe in which the number of OFDM symbols for PDCCH with normal CP is equal to four;

- a non-BL/CE UE is not expected to receive PDSCH resource blocks transmitted on antenna port 5, 7, 8, 9, 10, 11, 12, 13 or 14 in the two PRBs to which a pair of VRBs is mapped if either one of the two PRBs overlaps in frequency with a transmission of either PBCH or primary or secondary synchronization signals in the same subframe;

- the UE is not expected to receive PDSCH resource blocks transmitted on antenna port 7 for which distributed VRB resource allocation is assigned.

- The UE may skip decoding the transport block(s) if it does not receive all assigned PDSCH resource blocks except if it is capable of receiving the non-colliding PDSCH resource blocks in an assignment which partly collides in frequency with a transmission of PBCH or primary synchronization signal or secondary synchronization signal in the same subframes and that capability is indicated by pdsch-CollisionHandling [12]. If the UE skips decoding, the physical layer indicates to higher layer that the transport block(s) are not successfully decoded.

For frame structure type 2,

- the UE is not expected to receive PDSCH resource blocks transmitted on antenna port 5 in any subframe in which the number of OFDM symbols for PDCCH with normal CP is equal to four;

- the UE is not expected to receive PDSCH resource blocks transmitted on antenna port 5 in the two PRBs to which a pair of VRBs is mapped if either one of the two PRBs overlaps in frequency with a transmission of PBCH in the same subframe;

- a non-BL/CE UE is not expected to receive PDSCH resource blocks transmitted on antenna port 7, 8, 9, 10, 11, 12, 13 or 14 in the two PRBs to which a pair of VRBs is mapped if either one of the two PRBs overlaps in frequency with a transmission of primary or secondary synchronization signals in the same subframe;

- with normal CP configuration, the UE is not expected to receive PDSCH on antenna port 5 for which distributed VRB resource allocation is assigned in the special subframe with configuration #1 or #6;

- the UE is not expected to receive PDSCH on antenna port 7 for which distributed VRB resource allocation is assigned;

- with normal cyclic prefix, the UE is not expected to receive PDSCH resource blocks transmitted on antenna port 5 in DwPTS when the UE is configured with special subframe configuration 9 or 10.

- The UE may skip decoding the transport block(s) if it does not receive all assigned PDSCH resource blocks except if it is capable of receiving the non-colliding PDSCH resource blocks in an assignment which partly collides in frequency with a transmission of PBCH or primary synchronization signal or secondary synchronization signal in the same subframe and that capability is indicated by pdsch-CollisionHandling [12]. If the UE skips decoding, the physical layer indicates to higher layer that the transport block(s) are not successfully decoded.

- If the UE is not configured for PUSCH/PUCCH transmission for at least one TDD serving cell, the UE is not expected to receive PDSCH on serving cell  if the PDSCH overlaps in time with SRS transmission (including any interruption due to uplink or downlink RF retuning time [10]) on TDD serving cell  not configured for PUSCH/PUCCH transmission, and if the UE is not capable of simultaneous reception and transmission on serving cell and serving cell .

- if a UE is configured with higher layer parameter shortTTI for a serving cell, the UE is not expected to

- receive PDSCH data transmissions signalled via PDCCH/SPDCCH with DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G in

- DwPTS when the UE is configured with special subframe configuration 0 and 5;

- the second slot of DwPTS when the UE is configured with special subframe configuration 1, 2, 6 and 7.

- be configured with EIMTA-MainConfigServCell-r12 for the serving cell.

For a UE configured with EN-DC/NE-DC and serving cell frame structure type 1, if the UE is configured with tdm-PatternConfig/tdm-PatternConfigNE-DC for the serving cell, or if the UE is configured with tdm-PatternConfig2 for the serving cell with EN-DC, the UE is not expected to receive PDSCH data transmissions signalled via PDCCH in common search space for which HARQ-ACK response shall be provided in a subframe n, and PDSCH data transmissions signalled via PDCCH/EPDCCH in UE specific search space for which HARQ-ACK response shall be provided in the same subframe n.

If a UE is configured by higher layers to decode PDCCH with CRC scrambled by the C-RNTI, the UE shall decode the PDCCH and any corresponding PDSCH according to the respective combinations defined in Table 7.1-5. The scrambling initialization of PDSCH corresponding to these PDCCHs is by C-RNTI. The UE shall decode the PDCCH DCI Format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G only if the UE is configured with higher layer parameter shortTTI.

If a UE is configured by higher layers to decode EPDCCH with CRC scrambled by the C-RNTI, the UE shall decode the EPDCCH and any corresponding PDSCH according to the respective combinations defined in Table 7.1-5A. The scrambling initialization of PDSCH corresponding to these EPDCCHs is by C-RNTI.

If a BL/CE UE is configured by higher layers to decode MPDCCH with CRC scrambled by the C-RNTI except for random access procedure, the UE shall decode the MPDCCH and any corresponding PDSCH according to the respective combinations defined in Table 7.1-5B. The scrambling initialization of PDSCH corresponding to these MPDCCHs is by C-RNTI.

If a UE is configured with CEModeA, the UE shall decode MPDCCH DCI Format 6-1A. If the UE is configured with CEModeB, the UE shall decode MPDCCH DCI Format 6-1B.

If a UE is configured with higher layer parameter shortTTI and the UE is configured by higher layers to decode SPDCCH with CRC scrambled by the C-RNTI, the UE shall decode the SPDCCH and any corresponding PDSCH according to the respective combinations defined in Table 7.1-5C. The scrambling initialization of PDSCH corresponding to these SPDCCHs is by C-RNTI.

If the UE is configured with the carrier indicator field for a given serving cell and, if the UE is configured by higher layers to decode PDCCH/EPDCCH with CRC scrambled by the C-RNTI, then the UE shall decode PDSCH of the serving cell indicated by the carrier indicator field value in the decoded PDCCH/EPDCCH.

When a UE configured in transmission mode 3, 4, 8, 9 or 10 receives a DCI Format 1A assignment, it shall assume that the PDSCH transmission is associated with transport block 1 and that transport block 2 is disabled.

When a UE is configured in transmission mode 7, scrambling initialization of UE-specific reference signals corresponding to these PDCCHs/EPDCCHs is by C-RNTI.

The UE does not support transmission mode 8 if extended cyclic prefix is used in the downlink.

When a UE is configured in transmission mode 9 or 10, in the downlink subframes indicated by the higher layer parameter mbsfn-SubframeConfigList or by mbsfn-SubframeConfigList-v1250 or by mbsfn-SubframeConfigList-v14xy or by laa-SCellSubframeConfig of serving cell  except in subframes for the serving cell

- indicated by higher layers to decode PMCH or,

- configured by higher layers to be part of a positioning reference signal occasion and the positioning reference signal occasion is only configured within MBSFN subframes and the cyclic prefix length used in subframe #0 is normal cyclic prefix,

the UE shall upon detection of a PDCCH with CRC scrambled by the C-RNTI with DCI format 1A/2C/2D intended for the UE or, upon detection of an EPDCCH with CRC scrambled by the C-RNTI with DCI format 1A/2C/2D intended for the UE, decode the corresponding PDSCH in the same subframe.

A UE configured in transmission mode 10 can be configured with scrambling identities, ,  by higher layers for UE-specific reference signal generation as defined in Clause 6.10.3.1 of [3] to decode PDSCH according to a detected PDCCH/EPDCCH with CRC scrambled by the C-RNTI with DCI format 2D intended for the UE.

Table 7.1-5: PDCCH and PDSCH configured by C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PDSCH corresponding to PDCCH |  |
| --- | --- | --- | --- | --- |
| Mode 1 | DCI format 1A | Common andUE specific by C-RNTI | Single-antenna port, port 0 (see Clause 7.1.1) |  |
|  | DCI format 1 and 7-1A | UE specific by C-RNTI | Single-antenna port, port 0 (see Clause 7.1.1) |  |
| Mode 2 | DCI format 1A | Common andUE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |  |
|  | DCI format 1 and 7-1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |  |
| Mode 3 | DCI format 1A | Common andUE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |  |
|  | DCI format 2A and 7-1B | UE specific by C-RNTI | Large delay CDD (see Clause 7.1.3) or Transmit diversity (see Clause 7.1.2) |  |
| Mode 4 | DCI format 1A | Common andUE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |  |
|  | DCI format 2 and 7-1C | UE specific by C-RNTI | Closed-loop spatial multiplexing (see Clause 7.1.4)or Transmit diversity (see Clause 7.1.2) |  |
| Mode 5 | DCI format 1A | Common andUE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |  |
|  | DCI format 1D | UE specific by C-RNTI | Multi-user MIMO (see Clause 7.1.5) |  |
| Mode 6 | DCI format 1A | Common andUE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |  |
|  | DCI format 1B | UE specific by C-RNTI | Closed-loop spatial multiplexing (see Clause 7.1.4) using a single transmission layer |  |
|  | DCI format 7-1D | UE specific by C-RNTI | Closed-loop spatial multiplexing (see Clause 7.1.4) using a single transmission layer or transmit diversity (see Clause 7.1.2) |  |
| Mode 7 | DCI format 1A | Common andUE specific by C-RNTI | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |  |
|  | DCI format 1 | UE specific by C-RNTI | Single-antenna port, port 5 (see Clause 7.1.1) |  |
| Mode 8 | DCI format 1A | Common and UE specific by C-RNTI | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |  |
|  | DCI format 2B | UE specific by C-RNTI | Dual layer transmission, port 7 and 8 (see Clause 7.1.5A) or single-antenna port, port 7 or 8 (see Clause 7.1.1) |  |
|  | DCI format 7-1E | UE specific by C-RNTI | Dual layer transmission, port 7 and 8 (see Clause 7.1.5A) or single-antenna port, port 7 or 8 (see Clause 7.1.1) or Transmit Diversity, port 7 and 8 (see Clause 7.1.2) |  |
| Mode 9 | DCI format 1A | Common and UE specific by C-RNTI | Non-MBSFN subframe: If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2)MBSFN subframe: Single-antenna port, port 7 (see Clause 7.1.1) |  |
|  | DCI format 2C | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2) or dual layer transmission port 7-8 (see Clause 7.1.5A), if UE is configured with higher layer parameter semiOpenLoop, up to 8 layer transmission, ports 7-14 (see Clause 7.1.5B) otherwise; or single-antenna port, port 7, 8, 11, or 13 (see Clause 7.1.1) if UE is configured with higher layer parameter dmrs-tableAlt, single-antenna port, port 7 or 8 (see Clause 7.1.1) otherwise |  |
|  | DCI format 7-1F | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2), if UE is configured with higher layer parameter semiOpenLoopSTTI Up to 2 layer transmission, ports 7-8 (see Clause 7.1.5B) or single-antenna port, port 7 or 8 (see Clause 7.1.1) or transmit diversity, port 7-8, (see Clause 7.1.2) if the UE is configured with slotSubslotPDSCH-TXDiv-2layer-TM9/10 (3GPP TS 36.331 [11]).Up to 4 layer transmission, ports 7-10 (see Clause 7.1.5B) or single-antenna port, port 7 or 8 (see Clause 7.1.1) or transmit diversity, port 7-8, (see Clause 7.1.2) if the UE is configured with slotSubslotPDSCH-TXDiv-4layer-TM9/10 (3GPP TS 36.331 [11]).Up to 4 layer transmission, ports 7-10 (see Clause 7.1.5B) otherwise; or single-antenna port, port 7 or 8 (see Clause 7.1.1). |  |
| Mode 10 | DCI format 1A | Common and UE specific by C-RNTI | Non-MBSFN subframe: If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2)MBSFN subframe: Single-antenna port, port 7 (see Clause 7.1.1) |  |
|  | DCI format 2D | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2) or dual layer transmission port 7-8 (see Clause 7.1.5A), if UE is configured with higher layer parameter semiOpenLoop, up to 8 layer transmission, ports 7-14 (see Clause 7.1.5B) otherwise; or single-antenna port, port 7, 8, 11, or 13 (see Clause 7.1.1) if UE is configured with higher layer parameter dmrs-tableAlt, single-antenna port, port 7 or 8 (see Clause 7.1.1) otherwise |  |
|  | DCI format 7-1G | US specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2), if UE is configured with higher layer parameter semiOpenLoopSTTI.Up to 2 layer transmission, ports 7-8 (see Clause 7.1.5B) or single-antenna port, port 7 or 8 (see Clause 7.1.1) or transmit diversity, port 7-8, (see Clause 7.1.2) if the UE is configured with slotSubslotPDSCH-TXDiv-2layer-TM9/10 (3GPP TS 36.331 [11]).Up to 4 layer transmission, ports 7-10 (see Clause 7.1.5B) or single-antenna port, port 7 or 8 (see Clause 7.1.1) or transmit diversity, port 7-8 (see Clause 7.1.2) if the UE is configured with slotSubslotPDSCH-TxDiv-4layer-TM9/10 (3GPP TS 36.331 Up to 4 layer transmission, ports 7-10 (see Clause 7.1.5B) otherwise, or single-antenna port, port 7 or 8 (see Clause 7.1.1) |  |

Table 7.1-5A: EPDCCH and PDSCH configured by C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PDSCH corresponding to EPDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 1A | UE specific by C-RNTI | Single-antenna port, port 0 (see Clause 7.1.1) |
|  | DCI format 1 | UE specific by C-RNTI | Single-antenna port, port 0 (see Clause 7.1.1) |
| Mode 2 | DCI format 1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
|  | DCI format 1 | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 3 | DCI format 1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
|  | DCI format 2A | UE specific by C-RNTI | Large delay CDD (see Clause 7.1.3) or Transmit diversity (see Clause 7.1.2) |
| Mode 4 | DCI format 1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
|  | DCI format 2 | UE specific by C-RNTI | Closed-loop spatial multiplexing (see Clause 7.1.4)or Transmit diversity (see Clause 7.1.2) |
| Mode 5 | DCI format 1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
|  | DCI format 1D | UE specific by C-RNTI | Multi-user MIMO (see Clause 7.1.5) |
| Mode 6 | DCI format 1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
|  | DCI format 1B | UE specific by C-RNTI | Closed-loop spatial multiplexing (see Clause 7.1.4) using a single transmission layer |
| Mode 7 | DCI format 1A | UE specific by C-RNTI | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |
|  | DCI format 1 | UE specific by C-RNTI | Single-antenna port, port 5 (see Clause 7.1.1) |
| Mode 8 | DCI format 1A | UE specific by C-RNTI | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |
|  | DCI format 2B | UE specific by C-RNTI | Dual layer transmission, port 7 and 8 (see Clause 7.1.5A) or single-antenna port, port 7 or 8 (see Clause 7.1.1) |
| Mode 9 | DCI format 1A | UE specific by C-RNTI | Non-MBSFN subframe: If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2)MBSFN subframe: Single-antenna port, port 7 (see Clause 7.1.1) |
|  | DCI format 2C | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2) or dual layer transmission port 7-8 (see Clause 7.1.5A), if UE is configured with higher layer parameter semiOpenLoop, up to 8 layer transmission, ports 7-14 (see Clause 7.1.5B) otherwise; or single-antenna port, port 7, 8, 11, or 13 (see Clause 7.1.1) if UE is configured with higher layer parameter dmrs-tableAlt, single-antenna port, port 7 or 8 (see Clause 7.1.1) otherwise |
| Mode 10 | DCI format 1A | UE specific by C-RNTI | Non-MBSFN subframe: If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2)MBSFN subframe: Single-antenna port, port 7 (see Clause 7.1.1) |
|  | DCI format 2D | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2) or dual layer transmission port 7-8 (see Clause 7.1.5A), if UE is configured with higher layer parameter semiOpenLoop, up to 8 layer transmission, ports 7-14 (see Clause 7.1.5B) otherwise; or single-antenna port, port 7, 8, 11, or 13 (see Clause 7.1.1) if UE is configured with higher layer parameter dmrs-tableAlt, single-antenna port, port 7 or 8 (see Clause 7.1.1) otherwise |

Table 7.1-5B: MPDCCH and PDSCH configured by C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PDSCH corresponding to MPDCCH |
| --- | --- | --- | --- |
| Mode 1 | 6-1A | Type0-Common | Single-antenna port, port 0 (see Clause 7.1.1) |
|  | 6-1A or 6-1B | UE specific by C-RNTI |  |
| Mode 2 | 6-1A | Type0-Common | Transmit diversity (see Clause 7.1.2) |
|  | 6-1A or 6-1B | UE specific by C-RNTI |  |
| Mode 6 | 6-1A | Type0-Common | Transmit diversity (see Clause 7.1.2) |
|  | 6-1A | UE specific by C-RNTI | Closed-loop spatial multiplexing (see Clause 7.1.4) using a single transmission layer |
| Mode 9 | 6-1A | Type0-Common | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |
|  | 6-1A | UE specific by C-RNTI | Single-antenna port, port 7 or 8 (see Clause 7.1.1) |
|  | 6-1B | UE specific by C-RNTI | Single-antenna port, port 7 (see Clause 7.1.1) |

Table 7.1-5C: SPDCCH and PDSCH configured by C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PDSCH corresponding to SPDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 7-1A | UE specific by C-RNTI | Single-antenna port, port 0 (see Clause 7.1.1) |
| Mode 2 | DCI format 7-1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 3 | DCI format 7-1B | UE specific by C-RNTI | Large delay CDD (see Clause 7.1.3) |
| Mode 4 | DCI format 7-1C | UE specific by C-RNTI | Closed-loop spatial multiplexing (see Clause 7.1.4) or Transmit diversity (see Clause 7.1.2) |
| Mode 6 | DCI format 7-1D | UE specific by C-RNTI | Closed-loop spatial multiplexing (see Clause 7.1.4) using a single transmission layer or Transmit diversity (see Clause 7.1.2) |
| Mode 8 | DCI format 7-1E | UE specific by C-RNTI | Dual layer transmission, port 7 and 8 (see Clause 7.1.5A) or single-antenna port, port 7 or 8 (see Clause 7.1.1) or Transmit Diversity, port 7 and port 8 (see Clause 7.1.2) |
| Mode 9 | DCI format 7-1F | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2), if UE is configured with higher layer parameter semiOpenLoopSTTI.Up to 2 layer transmission, ports 7-8 (see Clause 7.1.5B) or single-antenna port, port 7 or 8 (see Clause 7.1.1) or transmit diversity, port 7-8, (see Sublause 7.1.2) if the UE is configured with slotSubslotPDSCH-TXDiv-2layer-TM9/10 (3GPP TS 36.331 [11]).Up to 4 layer transmission, ports 7-10 (see Clause 7.1.5B) or single-antenna port, port 7 or 8 (see Clause 7.1.1) or transmit diversity, port 7-8 (see Clause 7.1.2) if the UE is configured with slotSubslotPDSCH-TXDiv-4layer-TM9/10 (3GPP TS 36.331 [11]).Up to 4 layer transmission, ports 7-10 (see Clause 7.1.5B) otherwise; or single-antenna port, port 7 or 8 (see Clause 7.1.1). |
| Mode 10 | DCI format 7-1G | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2), if UE is configured with higher layer parameter semiOpenLoopSTTI.Up to 2 layer transmission, port 7-8 (see Clause 7.1.5B) or single-antenna port, port 7 or 8 (see Clause 7.1.1) or transmit diversity, port 7-8 (see Clause 7.1.2) if the UE is configured with slotSubslotPDSCH-TXDiv-2layer-TM9/10 (3GPP TS 36.331 [11]).Up to 4 layer transmission, ports 7-10 (see Clause 7.1.5B) or single-antenna port, port 7 or 8 (See Clause 7.1.1) or transmit diversity, port 7-8 (see Clause 7.1.2) if the UE is configured with slotSubslot PDSCH-TXDiv-4layer-TM9/10 (3GPP TS 36.331 [11]).Up to 4 layer transmission, ports 7-10 (see Clause 7.1.5B) otherwise; or single-antenna port, port 7 or 8 (see Clause 7.1.1). |

If a UE is configured by higher layers to decode PDCCH with CRC scrambled by the SPS C-RNTI, the UE shall decode the PDCCH on the primary cell and any corresponding PDSCH on the primary cell according to the respective combinations defined in Table 7.1-6 unless the UE is configured with higher layer parameter shortProcessingTime and for DCI formats 1/1A/2/2A/2B/2C/2D mapped onto the UE-specific search space. The same PDSCH related configuration applies in the case that a PDSCH is transmitted without a corresponding PDCCH. The scrambling initialization of PDSCH corresponding to these PDCCHs and PDSCH without a corresponding PDCCH is by SPS C-RNTI.

If a UE is configured by higher layers to decode EPDCCH with CRC scrambled by the SPS C-RNTI, the UE shall decode the EPDCCH on the primary cell and any corresponding PDSCH on the primary cell according to the respective combinations defined in Table 7.1-6A. The same PDSCH related configuration applies in the case that a PDSCH is transmitted without a corresponding EPDCCH. The scrambling initialization of PDSCH corresponding to these EPDCCHs and PDSCH without a corresponding EPDCCH is by SPS C-RNTI.

If a UE configured with CEModeA is configured by higher layers to decode MPDCCH with CRC scrambled by the SPS C-RNTI, the UE shall decode the MPDCCH on the primary cell and any corresponding PDSCH on the primary cell according to the respective combinations defined in Table 7.1-6B. The same PDSCH related configuration applies in the case that a PDSCH is transmitted without a corresponding MPDCCH. The scrambling initialization of PDSCH corresponding to these MPDCCHs and PDSCH without a corresponding MPDCCH is by SPS C-RNTI.

When a UE is configured in transmission mode 7, scrambling initialization of UE-specific reference signals for PDSCH corresponding to these PDCCHs/EPDCCHs and for PDSCH without a corresponding PDCCH/EPDCCH is by SPS C-RNTI.

When a UE is configured in transmission mode 9 or 10, in the downlink subframes indicated by the higher layer parameter mbsfn-SubframeConfigList or by mbsfn-SubframeConfigList-v1250 or by mbsfn-SubframeConfigList-v14xy of serving cell  except in subframes for the serving cell

- indicated by higher layers to decode PMCH or,

- configured by higher layers to be part of a positioning reference signal occasion and the positioning reference signal occasion is only configured within MBSFN subframes and the cyclic prefix length used in subframe #0 is normal cyclic prefix,

the UE shall upon detection of a PDCCH with CRC scrambled by the SPS C-RNTI with DCI format 1A/2C/2D/7-1F/7-1G except when the UE is configured with higher layer parameter shortProcessingTime and with DCI format 1A/2C/2D mapped onto the UE-specific search space, or upon detection of a EPDCCH with CRC scrambled by the SPS C-RNTI with DCI format 1A/2C/2D, or upon detection of a SPDCCH with CRC scrambled by the SPS C-RNTI with DCI format 7-1F/7-1G, or for a configured PDSCH without PDCCH intended for the UE, decode the corresponding PDSCH in the same subframe/slot/subslot.

A UE configured in transmission mode 10 can be configured with scrambling identities, ,  by higher layers for UE-specific reference signal generation as defined in Clause 6.10.3.1 of [3] to decode PDSCH according to a detected

- PDCCH/EPDCCH with CRC scrambled by the SPS C-RNTI with DCI format 2D

- PDCCH/SPDCCH with CRC scrambled by the SPS C-RNTI with DCI format 7-1G

intended for the UE.

For PDSCH without a corresponding PDCCH/EPDCCH, the UE shall use the value of and the scrambling identity of  (as defined in Clause 6.10.3.1 of [3]) derived from the DCI format 2D/7-1G corresponding to the associated SPS activation for UE-specific reference signal generation.

Table 7.1-6: PDCCH and PDSCH configured by SPS C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PDSCH corresponding to PDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 1A | Common andUE specific by C-RNTI | Single-antenna port, port 0 (see Clause 7.1.1) |
|  | DCI format 1 and 7-1A | UE specific by C-RNTI | Single-antenna port, port 0 (see Clause 7.1.1) |
| Mode 2 | DCI format 1A | Common andUE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
|  | DCI format 1 and 7-1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 3 | DCI format 1A | Common andUE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
|  | DCI format 2A and 7-1B | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 4 | DCI format 1A | Common andUE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
|  | DCI format 2 and 7-1C | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 5 | DCI format 1A | Common andUE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 6 | DCI format 1A | Common andUE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
|  | DCI format 7-1D | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 7 | DCI format 1A | Common andUE specific by C-RNTI | Single-antenna port, port 5 (see Clause 7.1.1) |
|  | DCI format 1 | UE specific by C-RNTI | Single-antenna port, port 5 (see Clause 7.1.1) |
| Mode 8 | DCI format 1A | Common and UE specific by C-RNTI | Single-antenna port, port 7(see Clause 7.1.1) |
|  | DCI format 2B and 7-1E | UE specific by C-RNTI | Single-antenna port, port 7 or 8 (see Clause 7.1.1) |
| Mode 9 | DCI format 1A | Common and UE specific by C-RNTI | Single-antenna port, port 7 (see Clause 7.1.1) |
|  | DCI format 2C | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2) if UE is configured with higher layer parameter semiOpenLoop, or single-antenna port, port 7, 8, 11, or 13 (see Clause 7.1.1) if UE is configured with higher layer parameter dmrs-tableAlt, Single-antenna port, port 7 or 8, (see Clause 7.1.1) otherwise |
|  | DCI format 7-1F | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2) if UE is configured with higher layer parameter semiOpenLoopSTTI, Transmit diversity, port 7-8, (see Clause 7.1.2) or single antenna port, port 7 or 8, (see Clause 7.1.1) if UE is configured with higher layer parameter slotSubslotPDSCH-TXDiv-2layer-TM9/10 or subSlotslotPDSCH TS 36.331 [11]).Single-antenna port, port 7 or 8, (see Clause 7.1.1) otherwise. |
| Mode 10 | DCI format 1A | Common and UE specific by C-RNTI | Single-antenna port, port 7 (see Clause 7.1.1) |
|  | DCI format 2D | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2) if UE is configured with higher layer parameter semiOpenLoop, or single-antenna port, port 7, 8, 11, or 13 (see Clause 7.1.1) if UE is configured with higher layer parameter dmrs-tableAlt, Single-antenna port, port 7 or 8, (see Clause 7.1.1) otherwise |
|  | DCI format 7-1G | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2) if UE is configured with higher layer parameter semiOpenLoop, Transmit diversity, port 7,8 (see Clause 7.1.2) or single antenna port, port 7 or 8, (see Clause 7.1.1) if UE is configured with higher layer parameter slotSubslotPDSCH-TXDiv-2layer-TM9/10 or slotSubslotPDSCH-TXDiv-4layer-TM9/10 (3GPP TS 36.331[11]).Single-antenna port, port 7 or 8, (see Clause 7.1.1) otherwise. |

Table 7.1-6A: EPDCCH and PDSCH configured by SPS C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PDSCH corresponding to EPDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 1A | UE specific by C-RNTI | Single-antenna port, port 0 (see Clause 7.1.1) |
|  | DCI format 1 | UE specific by C-RNTI | Single-antenna port, port 0 (see Clause 7.1.1) |
| Mode 2 | DCI format 1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
|  | DCI format 1 | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 3 | DCI format 1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
|  | DCI format 2A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 4 | DCI format 1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
|  | DCI format 2 | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 5 | DCI format 1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 6 | DCI format 1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 7 | DCI format 1A | UE specific by C-RNTI | Single-antenna port, port 5 (see Clause 7.1.1) |
|  | DCI format 1 | UE specific by C-RNTI | Single-antenna port, port 5 (see Clause 7.1.1) |
| Mode 8 | DCI format 1A | UE specific by C-RNTI | Single-antenna port, port 7(see Clause 7.1.1) |
|  | DCI format 2B | UE specific by C-RNTI | Single-antenna port, port 7 or 8 (see Clause 7.1.1) |
| Mode 9 | DCI format 1A | UE specific by C-RNTI | Single-antenna port, port 7 (see Clause 7.1.1) |
|  | DCI format 2C | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2) if UE is configured with higher layer parameter semiOpenLoop, or single-antenna port, port 7, 8, 11, or 13 (see Clause 7.1.1) if UE is configured with higher layer parameter dmrs-tableAlt, Single-antenna port, port 7 or 8, (see Clause 7.1.1) otherwise |
| Mode 10 | DCI format 1A | UE specific by C-RNTI | Single-antenna port, port 7 (see Clause 7.1.1) |
|  | DCI format 2D | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2) if UE is configured with higher layer parameter semiOpenLoop, or single-antenna port, port 7, 8, 11, or 13 (see Clause 7.1.1) if UE is configured with higher layer parameter dmrs-tableAlt, Single-antenna port, port 7 or 8, (see Clause 7.1.1) otherwise |

Table 7.1-6B: MPDCCH and PDSCH configured by SPS C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PDSCH corresponding to MPDCCH |
| --- | --- | --- | --- |
| Mode 1 | 6-1A | UE specific by C-RNTI | Single-antenna port, port 0 (see Clause 7.1.1) |
| Mode 2 | 6-1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 6 | 6-1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 9 | 6-1A | UE specific by C-RNTI | Single-antenna port, port 7 or 8 (see Clause 7.1.1) |

NOTE: For BL/CE UEs configured with transmission mode 6, and for DCI 6-1A mapped onto the UE specific search space and with CRC scrambled by the SPS C-RNTI, the bits corresponding to TPMI information for precoding and PMI information for precoding are set to zero.

Table 7.1-6C: SPDCCH and PDSCH configured by SPS C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PDSCH corresponding to SPDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 7-1A | UE specific by C-RNTI | Single-antenna port, port 0 (see Clause 7.1.1) |
| Mode 2 | DCI format 7-1A | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 3 | DCI format 7-1B | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 4 | DCI format 7-1C | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 6 | DCI format 7-1D | UE specific by C-RNTI | Transmit diversity (see Clause 7.1.2) |
| Mode 8 | DCI format 7-1E | UE specific by C-RNTI | Single-antenna port, port 7 or 8 (see Clause 7.1.1) |
| Mode 9 | DCI format 7-1F | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2) if UE is configured with higher layer parameter semiOpenLoopSTTI.Transmit diversity, port 7-8, (see Clause 7.1.2) or single antenna port, port 7 or 8, (see Clause 7.1.1) if UE is configured with higher layer parameter slotSubslotPDSCH-TXDiv-2layer-TM9/10 or slotSubslotPDSCH-TXDiv-4layer-TM9/10 (3GPP TS 36.331 [11]).Single-antenna port, port 7 or 8, (see Clause 7.1.1) otherwise. |
| Mode 10 | DCI format 7-1G | UE specific by C-RNTI | Transmit diversity, port 7-8, (see Clause 7.1.2) if UE is configured with higher layer parameter semiOpenLoopSTTI.Transmit diversity, port 7-8, (see Clause 7.1.2) or single antenna port, port 7 or 8, (see Clause 7.1.1) if UE is configured with higher layer parameter slotSubslotPDSCH-TXDiv-2layer-TM9/10 or slotSubslotPDSCH-TXDiv-4layer-TM9/10 (3GPP TS 36.331 [11]).Single-antenna port, port 7 or 8, (see Clause 7.1.1) otherwise. |

If a UE is configured by higher layers to decode PDCCH with CRC scrambled by the Temporary C-RNTI and is not configured to decode PDCCH with CRC scrambled by the C-RNTI, the UE shall decode the PDCCH and the corresponding PDSCH according to the combination defined in Table 7.1-7. The scrambling initialization of PDSCH corresponding to these PDCCHs is by Temporary C-RNTI.

If a UE is configured by higher layers to decode MPDCCH with CRC scrambled by the Temporary C-RNTI and is not configured to decode MPDCCH with CRC scrambled by the C-RNTI during random access procedure, the UE shall decode the MPDCCH and the corresponding PDSCH according to the combination defined in Table 7.1-8. The scrambling initialization of PDSCH corresponding to these MPDCCHs is by Temporary C-RNTI.

If a UE is also configured by higher layers to decode MPDCCH with CRC scrambled by the C-RNTI during random access procedure, the UE shall decode the MPDCCH and the corresponding PDSCH according to the combination defined in Table 7.1-8. The scrambling initialization of PDSCH corresponding to these MPDCCHs is by C-RNTI.

If a UE is configured by higher layers to decode MPDCCH with CRC scrambled by the CB-RNTI during the CB-Msg3-EDT procedure, the UE shall decode the MPDCCH and the corresponding PDSCH according to the combination defined in Table 7.1-8. The scrambling initialization of PDSCH corresponding to these MPDCCHs is by CB-RNTI.

Table 7.1-7: PDCCH and PDSCH configured by Temporary C-RNTI

| DCI format | Search Space | Transmission scheme of PDSCH corresponding to PDCCH |
| --- | --- | --- |
| DCI format 1A | Common and  UE specific  by Temporary C-RNTI | If the number of PBCH antenna port is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |
| DCI format 1 | UE specific  by Temporary C-RNTI | If the number of PBCH antenna port is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |

Table 7.1-8: MPDCCH and PDSCH configured by Temporary C-RNTI and/or C-RNTI during random access procedure, or CB-RNTI during CB-Msg3-EDT procedure

| DCI format | Search Space | Transmission scheme of PDSCH corresponding to MPDCCH |
| --- | --- | --- |
| DCI format 6-1A | Type2-Common | If the number of PBCH antenna port is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |
| DCI format 6-1B | Type2-Common | If the number of PBCH antenna port is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2) |
| Note 1: Only DCI format 6-1A is applicable for CB-RNTI during CB-Msg3-EDT procedure |  |  |

If a BL/CE UE is configured by higher layers to decode MPDCCH with CRC scrambled by the PUR-RNTI, the UE shall decode the MPDCCH and any corresponding PDSCH according to the respective combinations defined in Table 7.1-9. The scrambling initialization of PDSCH corresponding to these MPDCCHs is by PUR-RNTI.

Table 7.1-9: MPDCCH and PDSCH configured by PUR-RNTI

| DCI format | Search Space | Transmission scheme of PDSCH corresponding to MPDCCH |
| --- | --- | --- |
| 6-1A or 6-1B | UE specific by PUR-RNTI | If the number of PBCH antenna ports is one, Single-antenna port, port 0 is used (see Clause 7.1.1), otherwise Transmit diversity (see Clause 7.1.2). |

If the UE is configured with higher layer parameter must-Config-r14, and if the PDCCH/EPDCCH DCI of the corresponding PDSCH transmission indicates MUST interference is present [4],

- the UE may assume that the starting OFDM symbol of MUST interference is same as the starting OFDM symbol of the corresponding PDSCH transmission,

- for transmission modes 8-10, the UE may assume ,  of MUST interference are same as that of the corresponding PDSCH transmission.

A UE is not required to receive PDSCH assigned by MPDCCH with DCI CRC scrambled by SC-RNTI or G-RNTI if the set of subframes carrying the PDSCH includes any subframes in which the UE monitors Type1-MPDCCH common search space or PDSCH assigned by MPDCCH sent in Type1-MPDCCH common search space.

A UE is not required to receive PDSCH assigned by MPDCCH with DCI CRC scrambled by G-RNTI if the set of subframes carrying the PDSCH includes any subframes in which the UE monitors Type1A-MPDCCH common search space, or includes any subframes in which the UE receives PDSCH assigned by MPDCCH with DCI CRC scrambled by SC-RNTI.

The transmission schemes of the PDSCH are described in the following clauses.

### 7.1.1 Single-antenna port scheme

For the single-antenna port transmission schemes (port 0/5/7/8/11/13) of the PDSCH, the UE may assume that an eNB transmission on the PDSCH would be performed according to Clause 6.3.4.1 of [3].

If the UE is not configured with higher layer parameter dmrs-tableAlt and in case an antenna port  is used, or if the higher layer parameter dmrs-tableAlt is set to 1 and in case an antenna port  corresponding to one codeword values 0-3 in Table 5.3.3.1.5C-2 [4] is used, the UE cannot assume that the other antenna port in the set  is not associated with transmission of PDSCH to another UE.

If the UE is configured with higher layer parameter dmrs-tableAlt, and in case of single layer transmission scheme on antenna port  corresponding to one codeword values 4-11 in Table 5.3.3.1.5C-2 [4] is used, the UE cannot assume that the other antenna ports in the set  is not associated with transmission of PDSCH to another UE.

### 7.1.2 Transmit diversity scheme

For the transmit diversity transmission scheme of the PDSCH, the UE may assume that an eNB transmission on the PDSCH would be performed according to Clause 6.3.4.3 of [3]

### 7.1.3 Large delay CDD scheme

For the large delay CDD transmission scheme of the PDSCH, the UE may assume that an eNB transmission on the PDSCH would be performed according to large delay CDD as defined in Clause 6.3.4.2.2 of [3].

### 7.1.4 Closed-loop spatial multiplexing scheme

For the closed-loop spatial multiplexing transmission scheme of the PDSCH, the UE may assume that an eNB transmission on the PDSCH would be performed according to the applicable number of transmission layers as defined in Clause 6.3.4.2.1 of [3].

### 7.1.5 Multi-user MIMO scheme

For the multi-user MIMO transmission scheme of the PDSCH, the UE may assume that an eNB transmission on the PDSCH would be performed on one layer and according to Clause 6.3.4.2.1 of [3]. The dB value signalled on PDCCH/EPDCCH with DCI format 1D using the downlink power offset field is given in Table 7.1.5-1.

Table 7.1.5-1: Mapping of downlink power offset field in DCI format 1D to the value.

| Downlink power offset field | [dB] |
| --- | --- |
| 0 | -10log10(2) |
| 1 | 0 |

### 7.1.5A Dual layer scheme

For the dual layer transmission scheme of the PDSCH, the UE may assume that an eNB transmission on the PDSCH would be performed with two transmission layers on antenna ports 7 and 8 as defined in Clause 6.3.4.4 of [3].

### 7.1.5B Up to 8 layer transmission scheme

For the up to 8 layer transmission scheme of the PDSCH, the UE may assume that an eNB transmission on the PDSCH would be performed with up to 8 transmission layers on antenna ports 7 - 14 as defined in Clause 6.3.4.4 of [3].

If the UE is configured with higher layer parameter dmrs-tableAlt, and in case of dual layer transmission scheme on antenna portsor corresponding to two codewords values 2-5 in Table 5.3.3.1.5C-2 [4] is used, the UE cannot assume that the other antenna ports in the set  is not associated with transmission of PDSCH to another UE.

### 7.1.6 Resource allocation

The UE shall interpret the resource allocation field depending on the PDCCH/EPDCCH DCI format detected. A resource allocation field in each PDCCH/EPDCCH includes two parts, a resource allocation header field and information consisting of the actual resource block assignment.

PDCCH DCI formats 1, 2, 2A, 2B, 2C and 2D with type 0 and PDCCH DCI formats 1, 2, 2A, 2B, 2C and 2D with type 1 resource allocation have the same format and are distinguished from each other via the single bit resource allocation header field which exists depending on the downlink system bandwidth (Clause 5.3.3.1 of [4]), where type 0 is indicated by 0 value and type 1 is indicated otherwise. PDCCH with DCI format 1A, 1B, 1C and 1D have a type 2 resource allocation while PDCCH with DCI format 1, 2, 2A, 2B, 2C and 2D have type 0 or type 1 resource allocation. PDCCH DCI formats with a type 2 resource allocation do not have a resource allocation header field.

EPDCCH DCI formats 1, 2, 2A, 2B, 2C and 2D with type 0 and EPDCCH DCI formats 1, 2, 2A, 2B, 2C and 2D with type 1 resource allocation have the same format and are distinguished from each other via the single bit resource allocation header field which exists depending on the downlink system bandwidth (Clause 5.3.3.1 of [4]), where type 0 is indicated by 0 value and type 1 is indicated otherwise. EPDCCH with DCI format 1A, 1B, and 1D have a type 2 resource allocation while EPDCCH with DCI format 1, 2, 2A, 2B, 2C and 2D have type 0 or type 1 resource allocation. EPDCCH DCI formats with a type 2 resource allocation do not have a resource allocation header field.

If the UE is configured with higher layer parameter shortTTI, PDCCH/SPDCCH with DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G utilizes a higher layer configured resource allocation type 0 or resource allocation type 2.

If the UE is configured with higher layer parameter ce-pdsch-maxBandwidth-config with value 20MHz and the resource block assignment flag is set to 0

- MPDCCH with DCI format 6-1A utilizes a type 0 resource allocation.

else if the UE is configured with higher layer parameter ce-pdsch-maxBandwidth-config with value 20MHz and the resource block assignment flag is set to 1, or the UE is configured with higher layer parameter ce-pdsch-maxBandwidth-config with value 5 MHz, or mpdcch-PDSCH-MaxBandwidth-SC-MTCH is set to 24 PRBs,

For system bandwidth larger than 1.4 MHz,

MPDCCH with DCI format 6-1A utilizes same type 2 resource allocation within each allocated narrowband.

otherwise,

MPDCCH with DCI format 6-1A utilizes a type 2 resource allocation.

otherwise

- MPDCCH with DCI format 6-1A utilizes a type 2 resource allocation.

Resource allocation for MPDCCH with DCI format 6-1B is given by the Resource block assignment field as described in [4]. For a UE configured with higher layer parameter ce-pdsch-maxBandwidth-config with value 20MHz and CEModeB, the allocated widebands (WBs) are based on the wideband combination index according to Table 7.1.6-2.

MPDCCH with DCI format 6-2 assigns a set of six contiguously allocated localized virtual resource blocks within a narrowband. Localized virtual resource blocks are always used in case of MPDCCH with DCI format 6-1A, 6-1B, or 6-2.

A UE may assume, for any PDSCH transmission scheduled by a cell with physical cell identity given in NAICS-AssistanceInfo-r12 and the PDSCH transmission mode belonging to transmissionModeList-r12 associated with the cell except spatial multiplexing using up to 8 transmission layers in transmission mode 10, that the resource allocation granularity and precoding granularity in terms of PRB pairs in the frequency domain are both given by N, where N is given by the higher layer parameter resAllocGranularity-r12 associated with the cell. The first set of N consecutive PRB pairs of the resource allocation starts from the lowest frequency of the system bandwidth and the UE may assume the same precoding applies to all PRB pairs within a set.

For a BL/CE UE, the resource allocation for PDSCH carrying SystemInformationBlockType1-BR and SI messages is a set of six contiguously allocated localized virtual resource blocks within a narrowband. The number of repetitions for the PDSCH carrying SystemInformationBlockType1-BR is determined based on the parameter schedulingInfoSIB1-BR configured by higher-layers and according to Table 7.1.6-1. If the value of the parameter schedulingInfoSIB1-BR configured by higher-layers is set to 0, UE assumes that SystemInformationBlockType1-BR is not transmitted.

Table 7.1.6-1: Number of repetitions for PDSCH carrying SystemInformationBlockType1-BR for BL/CE UE.

| Value of schedulingInfoSIB1-BR | Number of PDSCH repetitions |
| --- | --- |
| 0 | N/A |
| 1 | 4 |
| 2 | 8 |
| 3 | 16 |
| 4 | 4 |
| 5 | 8 |
| 6 | 16 |
| 7 | 4 |
| 8 | 8 |
| 9 | 16 |
| 10 | 4 |
| 11 | 8 |
| 12 | 16 |
| 13 | 4 |
| 14 | 8 |
| 15 | 16 |
| 16 | 4 |
| 17 | 8 |
| 18 | 16 |
| 19-31 | Reserved |

Table 7.1.6-2: Wideband combination index for a UE configured with higher layer parameter ce-pdsch-maxBandwidth-config with value 20MHz and CEModeB

| Wideband combination index | Indices of allocated WBs |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
| 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 |
| 2 | 0,1 | 2 | 2 |
| 3 | Reserved | 0,1 | 3 |
| 4 | NA | 1,2 | 0,1 |
| 5 | NA | 0,2 | 2,3 |
| 6 | NA | 0,1,2 | 0,1,2 |
| 7 | NA | Reserved | 0,1,2,3 |

#### 7.1.6.1 Resource allocation type 0

In resource allocations of type 0, resource block assignment information includes a bitmap indicating the Resource Block Groups (RBGs) that are allocated to the scheduled UE where a RBG is a set of consecutive virtual resource blocks (VRBs) of localized type as defined in Clause 6.2.3.1 of [3].

For a UE configured with higher layer parameter ce-pdsch-maxBandwidth-config with value 20MHz and the resource block assignment flag is set to 0

- Resource block group size (P) is given by the value S described in sub clause 5.3.3.1.12 of [4].

-  and  is used in place of  for the rest of this clause, unless explicitly mentioned.

otherwise

- Resource block group size (P) is a function of the system bandwidth as shown in Table 7.1.6.1-1A if a UE is configured with higher layer parameter shortTTI and for DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G, Table 7.1.6.1-1 otherwise.

For DCI formats other than DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G, the total number of RBGs () for downlink system bandwidth of is given by where of the RBGs are of size P and if  then one of the RBGs is of size. If a UE is configured with higher layer parameter shortTTI and for DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G, the total number of RBGs () for downlink system bandwidth of is given by where  of the RBGs are of size P and if  then the last RBGs is of size . The bitmap is of size bits with one bitmap bit per RBG such that each RBG is addressable.

For a UE configured with higher layer parameter ce-pdsch-maxBandwidth-config with value 20MHz and the resource block assignment flag is set to 0

- The RBGs shall be indexed according to RBG indexing described in Clause 8.1.5.1 by replacing with , 'uplink' with 'downlink' , and  with  (but not ![](media_svg/image86.svg) [公式: N&apos;^{DL}_{RB}]).

otherwise

- For DCI formats other than DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G, the RBGs shall be indexed in the order of increasing frequency and non-increasing RBG sizes starting at the lowest frequency.

- For DCI formats 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G, the RBGs shall be indexed in the order of increasing frequency and non-decreasing RBG sizes starting at the lowest frequency.

The order of RBG to bitmap bit mapping is such that RBG 0 to RBG are mapped to MSB to LSB of the bitmap. The RBG is allocated to the UE if the corresponding bit value in the bitmap is 1, the RBG is not allocated to the UE otherwise.

Table 7.1.6.1-1: Type 0 resource allocation RBG size vs. Downlink System Bandwidth

| System Bandwidth | RBG Size |
| --- | --- |
|  | (P) |
| ≤10 | 1 |
| 11 – 26 | 2 |
| 27 – 63 | 3 |
| 64 – 110 | 4 |

Table 7.1.6.1-1A: Type 0 resource allocation RBG size vs. Downlink System Bandwidth for DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G

| System Bandwidth | RBG Size |
| --- | --- |
|  | (P) |
| ≤10 | 1 |
| 11 – 24 | 2 |
| 25 – 63 | 6 |
| 64 – 110 | 12 |

#### 7.1.6.2 Resource allocation type 1

In resource allocations of type 1, a resource block assignment information of size  indicates to a scheduled UE the VRBs from the set of VRBs from one of P RBG subsets. The virtual resource blocks used are of localized type as defined in Clause 6.2.3.1 of [3]. Also P is the RBG size associated with the system bandwidth as shown in Table 7.1.6.1-1. A RBG subset , where , consists of every th RBG starting from RBG . The resource block assignment information consists of three fields [4].

The first field with bits is used to indicate the selected RBG subset among  RBG subsets.

The second field with one bit is used to indicate a shift of the resource allocation span within a subset. A bit value of 1 indicates shift is triggered. Shift is not triggered otherwise.

The third field includes a bitmap, where each bit of the bitmap addresses a single VRB in the selected RBG subset in such a way that MSB to LSB of the bitmap are mapped to the VRBs in the increasing frequency order. The VRB is allocated to the UE if the corresponding bit value in the bit field is 1, the VRB is not allocated to the UE otherwise. The portion of the bitmap used to address VRBs in a selected RBG subset has size  and is defined as

The addressable VRB numbers of a selected RBG subset start from an offset,  to the smallest VRB number within the selected RBG subset, which is mapped to the MSB of the bitmap. The offset is in terms of the number of VRBs and is done within the selected RBG subset. If the value of the bit in the second field for shift of the resource allocation span is set to 0, the offset for RBG subset  is given by . Otherwise, the offset for RBG subset  is given by , where the LSB of the bitmap is justified with the highest VRB number within the selected RBG subset. is the number of VRBs in RBG subset and can be calculated by the following equation,

Consequently, when RBG subset  is indicated, bit  for  in the bitmap field indicates VRB number,

.

#### 7.1.6.3 Resource allocation type 2

For BL/CE UEs with resource allocation type 2 resource assignment,  and  is used in the rest of this Clause.

In resource allocations of type 2, the resource block assignment information indicates to a scheduled UE a set of contiguously allocated localized virtual resource blocks or distributed virtual resource blocks. In case of resource allocation signalled with PDCCH DCI format 1A, 1B or 1D, or for resource allocation signalled with EPDCCH DCI format 1A, 1B, or 1D, one bit flag indicates whether localized virtual resource blocks or distributed virtual resource blocks are assigned (value 0 indicates Localized and value 1 indicates Distributed VRB assignment) while distributed virtual resource blocks are always assigned in case of resource allocation signalled with PDCCH DCI format 1C and localized virtual resource blocks are always assigned in case of resource allocation signalled with PDCCH/SPDCCH DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G. Localized VRB allocations for a UE vary from a single VRB up to a maximum number of VRBs spanning the system bandwidth. For DCI format 1A the distributed VRB allocations for a UE vary from a single VRB up to  VRBs, where  is defined in [3], if the DCI CRC is scrambled by P-RNTI, RA-RNTI, or SI-RNTI. With PDCCH DCI format 1B, 1D with a CRC scrambled by C-RNTI, or with DCI format 1A with a CRC scrambled with C-RNTI, SPS C-RNTI or Temporary C-RNTI distributed VRB allocations for a UE vary from a single VRB up to  VRBs if  is 6-49 and vary from a single VRB up to 16 if  is 50-110. With EPDCCH DCI format 1B, 1D with a CRC scrambled by C-RNTI, or with DCI format 1A with a CRC scrambled with C-RNTI, SPS C-RNTI distributed VRB allocations for a UE vary from a single VRB up to  VRBs if  is 6-49 and vary from a single VRB up to 16 if  is 50-110. With PDCCH DCI format 1C and 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G, VRB allocations for a UE vary from  VRB(s) up to  VRBs with an increment step of , where  value is determined depending on the downlink system bandwidth as shown in Table 7.1.6.3-1 for DCI format 1C and Table 7.1.6.3-1A for DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G.

Table 7.1.6.3-1:  values vs. Downlink System Bandwidth

| System BW () |  |
| --- | --- |
|  | DCI format 1C |
| 6-49 | 2 |
| 50-110 | 4 |

Table 7.1.6.3-1A:  values vs. Downlink System Bandwidth

| System BW () |  |
| --- | --- |
|  | DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G |
| 20 – 26 | 4 |
| 27 – 63 | 6 |
| 64 – 110 | 4 |

For PDCCH DCI format 1A, 1B, or 1D or for PDCCH DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G and <20, or for EPDCCH DCI format 1A, 1B, or 1D, or for MPDCCH DCI format 6-1A, or for SPDCCH DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G and <20, a type 2 resource allocation field consists of a resource indication value (RIV) corresponding to a starting resource block () and a length in terms of virtually contiguously allocated resource blocks .

The resource indication value is defined by

if  then

else

where 1 and shall not exceed .

For a BL/CE UE configured with CEModeA, and configured with higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig-r15, and ![](media_svg/image135.svg) [公式≈: 0(1)/210≥−+<RIVNN_{RBRB}^{DLDL}], the ![](media_svg/image128.svg) [公式≈: ^{RB}start] and ![](media_svg/image129.svg) [公式≈: ^{L}CRBs] is determined according to Table 7.1.6.3-2 where,

- ![](media_svg/image136.svg) [公式≈: ^{nn}NBNB,0,5^{,}] is the smallest and the largest physical resource-block number, respectively, of the allocated narrowband as defined in Clause 6.2.7 of [3]

- ![](media_svg/image137.svg) [公式≈: _{N}_{RB}DL] is the value of the downlink system bandwidth

- P is the RBG size associated with the downlink system bandwidth,![](media_svg/image137.svg) [公式≈: _{N}_{RB}DL], according to Table 7.1.6.1-1

- ![](media_svg/image138.svg) [公式≈: nPPNnRBNB=+−−min,1^{⊇⇒}⊕⇐_{⊕⇐}_{⊗⇔}^{⋅∂}⋅∂_{√∃}^{n}^{NB}_{P}^{,5}RB,5^{DL}]

- Physical resource-blocks with indices ![](media_svg/image139.svg) [公式≈: RBl_{start}+<0] or ![](media_svg/image140.svg) [公式≈: ^{RBlN}start^{+÷}RB^{DL}], ![](media_svg/image141.svg) [公式≈: lL=−0,1,...1_{CRBs}] correspond to physical resource-blocks outside the allocated narrowband relative to physical resource-block ![](media_svg/image142.svg) [公式≈: ^{n}NB,0]

- $ L_{CRBs}$ shall not exceed (![](media_svg/image143.svg) [公式≈: ^{NnRB}RB,0^{DL}^{−−}NBstart])

Table 7.1.6.3-2: ![](media_svg/image128.svg) [公式≈: ^{RB}start] and ![](media_svg/image129.svg) [公式≈: ^{L}CRBs]for ![](media_svg/image135.svg) [公式≈: 0(1)/210≥−+<RIVNN_{RBRB}^{DLDL}] and CEModeA

| ![](media_svg/image144.svg) [公式≈: RIVNN−+_{RBRB}^{DLDL}(1)/2] | ![](media_svg/image128.svg) [公式≈: ^{RB}start] | ![](media_svg/image129.svg) [公式≈: ^{L}CRBs] |
| --- | --- | --- |
|  |  |  |
| 0 | ![](media_svg/image145.svg) [公式≈: ^{Pn}^{⋅∂}⋅∂_{√∃}^{n}^{NB}_{P}^{,0}^{−}NB,0] | 2 |
| 1 |  | 3 |
| 2 |  | 4 |
| 3 |  | 5 |
| 4 |  | 6 |
| 5 | ![](media_svg/image146.svg) [公式≈: ^{n}RB] | 6 |
| 6 | ![](media_svg/image147.svg) [公式: n_{RB}+1] | 5 |
| 7 | ![](media_svg/image148.svg) [公式: n_{RB}+2] | 4 |
| 8 | ![](media_svg/image149.svg) [公式: n_{RB}+3] | 3 |
| 9 | ![](media_svg/image150.svg) [公式: n_{RB}+4] | 2 |

For PDCCH DCI format 1C or for PDCCH/SPDCCH DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G and , a type 2 resource block assignment field consists of a resource indication value (RIV) corresponding to a virtual starting resource block (=, , ,…, ) and a length in terms of virtually contiguously allocated resource blocks (=, ,…, ).

The resource indication value is defined by:

if  then

else

where ,  and , and where

## 1 and shall not exceed .

For PDCCH DCI format 1C or for PDCCH/SPDCCH DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G and , the starting resource block index is the same as the virtual starting resource block index (). For PDCCH/SPDCCH DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G and , the LSB of RIV indicates whether the starting resource block index is  or (value 0 indicates  and value 1 indicates ). In case of resource allocation signalled with

- PDCCH/SPDCCH DCI format 7-1A/7-1B/7-1C/7-1D, and , if the resource allocation indicates the corresponding PDSCH is mapped to RB index 23, the UE shall assume the PDSCH is also mapped to RB index 24.

- PDCCH/SPDCCH DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G, and , if the resource allocation indicates the corresponding PDSCH is mapped to RB index 47, the UE shall assume the PDSCH is also mapped to RB index 48 and 49.

- PDCCH/SPDCCH DCI format 7-1A/7-1B/7-1C/7-1D, and , if the resource allocation indicates the corresponding PDSCH is mapped to RB index 71, the UE shall assume the PDSCH is also mapped to RB index 72, 73 and 74.

- PDCCH/SPDCCH DCI format 7-1E/7-1F/7-1G, and , if the resource allocation indicates the corresponding PDSCH is mapped to RB index 71, the UE shall assume the PDSCH is also mapped to RB index 72, and 73.

#### 7.1.6.4 PDSCH starting position

This Clause describes PDSCH starting position for UEs that are not BL/CE UEs.

PDSCH starting position for BL/CE UEs is described in Clause 7.1.6.4A.

The starting OFDM symbol for the PDSCH of each activated serving cell is given by index  .

For a UE configured in transmission mode 1-9, for a given activated serving cell

- if the PDSCH is assigned by EPDCCH received in the same serving cell, or if the UE is configured to monitor EPDCCH in the subframe and the PDSCH is not assigned by a PDCCH/EPDCCH, and if the UE is configured with the higher layer parameter epdcch-StartSymbol-r11

-  is given by the higher-layer parameter epdcch-StartSymbol-r11.

- else if PDSCH and the corresponding PDCCH/EPDCCH are received on different serving cells

-  is given by the higher-layer parameter pdsch-Start-r10 for the serving cell on which PDSCH is received,

- Otherwise

-  is given by the CFI value in the subframe of the given serving cell when , and  is given by the CFI value + 1 in the subframe of the given serving cell when .

For a UE configured in transmission mode 10, for a given activated serving cell

- if the PDSCH is assigned by a PDCCH with DCI format 1C or by a PDCCH with DCI format 1A and with CRC scrambled with P-RNTI/RA-RNTI/SI-RNTI/Temporary C-RNTI

-  is given by the span of the DCI given by the CFI value in the subframe of the given serving cell according to Clause 5.3.4 of [4].

- if the PDSCH is assigned by a PDCCH/EPDCCH with DCI format 1A and with CRC scrambled with C-RNTI and if the PDSCH transmission is on antenna ports 0 - 3

- if the PDSCH is assigned by EPDCCH received in the same serving cell

-  is given by  for the EPDCCH-PRB-set where EPDCCH with the DCI format 1A was received ( as defined in Clause 9.1.4.1),

- else if PDSCH and the corresponding PDCCH/EPDCCH are received on different serving cells

-  is given by the higher-layer parameter pdsch-Start-r10for the serving cell on which PDSCH is received.

- otherwise

-  is given by the CFI value in the subframe of the given serving cell when , and  is given by the CFI value+1 in the subframe of the given serving cell when .

- if the PDSCH is assigned by or semi-statically scheduled by a PDCCH/EPDCCH with DCI format 1A and if the PDSCH transmission is on antenna port 7

- if the value of the higher layer parameter pdsch-Start-r11 determined from parameter set 1 in table 7.1.9-1 for the serving cell on which PDSCH is received belongs to {1,2,3,4},

- is given by the higher layer parameter pdsch-Start-r11 determined from parameter set 1 in table 7.1.9-1 for the serving cell on which PDSCH is received.

- else,

- if PDSCH and the corresponding PDCCH/EPDCCH are received on different serving cells,

-  is given by the higher-layer parameter pdsch-Start-r10for the serving cell on which PDSCH is received

- otherwise

-  is given by the CFI value in the subframe of the given serving cell when , and  is given by the CFI value + 1 in the subframe of the given serving cell when .

- if the subframe on which PDSCH is received is indicated by the higher layer parameter mbsfn-SubframeConfigList-r11 determined from parameter set 1 in table 7.1.9-1 for the serving cell on which PDSCH is received, or if the PDSCH is received on subframe 1 or 6 for the frame structure type 2,

- ,

- otherwise

- .

- if the PDSCH is assigned by or semi-persistently scheduled by a PDCCH/EPDCCH with DCI format 2D,

- if the value of the higher layer parameter pdsch-Start-r11 determined from the DCI (according to Clause 7.1.9) for the serving cell on which PDSCH is received belongs to {1,2,3,4},

-  is given by parameter pdsch-Start-r11 determined from the DCI (according to Clause 7.1.9) for the serving cell on which PDSCH is received except if UE is configured with Type C quasi co-location and when two codewords are transmitted then  is given by the maximum of the pdsch-Start-r11and pdsch-Start2-r15 parameters,

- else,

- if PDSCH and the corresponding PDCCH/EPDCCH are received on different serving cells,

-  is given by the higher-layer parameter pdsch-Start-r10for the serving cell on which PDSCH is received

- Otherwise

-  is given by the CFI value in the subframe of the given serving cell when , and  is given by the CFI value+1 in the subframe of the given serving cell when .

- if the subframe on which PDSCH is received is indicated by the higher layer parameter mbsfn-SubframeConfigList-r11 determined from the DCI (according to Clause 7.1.9) for the serving cell on which PDSCH is received, or if the PDSCH is received on subframe 1 or 6 for frame structure type 2,

- ,

- otherwise

- .

#### 7.1.6.4A PDSCH starting position for BL/CE UEs

The starting OFDM symbol for PDSCH is given by index  in the first slot in a subframe  and is determined as follows

- for reception of SIB1-BR

- if for the cell on which PDSCH is received

- if for the cell on which PDSCH is received

- else

- is given by the higher layer parameter startSymbolBR

- if subframe  is a special subframe or configured as an MBSFN subframe, and if the BL/CE UE is configured in CEModeA

-

- else

- .

#### 7.1.6.5 Physical Resource Block (PRB) bundling

A UE configured for transmission mode 9 for a given serving cell c may assume that precoding granularity is multiple resource blocks in the frequency domain when PMI/RI reporting is configured.

For a given serving cell c, if a UE is configured for transmission mode 10

- if PMI/RI reporting is configured for all configured CSI processes for the serving cell c, the UE may assume that precoding granularity is multiple resource blocks in the frequency domain,

- otherwise, the UE shall assume the precoding granularity is one resource block in the frequency domain.

If the UE is non-BL/CE UE,

- if the UE is configured for transmission mode 9, 10 with PMI/RI reporting and with higher layer parameter widebandPRG-Subframe and the scheduled PRBs are consecutive PRBs, the UE may assume that the same precoder applies on all the scheduled PRBs,

- otherwise, fixed system bandwidth dependent Precoding Resource block Groups (PRGs) of size  partition the system bandwidth and each PRG consists of consecutive PRBs. The PRG size a UE may assume for a given system bandwidth is given by Table 7.1.6.5-1. If  then one of the PRGs is of size . The PRG size is non-increasing starting at the lowest frequency. The UE may assume that the same precoder applies on all scheduled PRBs within a PRG.

If the UE is a BL/CE UE not configured with higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig-r15, PRGs of size ![](media_svg/image190.svg) [公式: P^{±}]=3 partition a narrowband with RB indices 0-2 in the narrowband in one PRG and RB indices 3-5 in the narrowband in another PRG.

If the UE is a BL/CE UE configured with CEModeA and configured with higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig-r15,

- if $ 0\leq  RIV-N_{RB}^{DL}(N_{RB}^{DL}+1)/2<5 $ in Table 7.1.6.3-2, then the set of two PRGs is starting from $ RB_{start}$;

- if $ 5\leq  RIV-N_{RB}^{DL}(N_{RB}^{DL}+1)/2<10 $, then the set of two PRGs is ending ending at $(RB_{start}+L_{CRBs}-1)$.

If the UE is a BL/CE UE configured with CEModeB and configured with higher layer parameter ce-PDSCH-FlexibleStartPRB-AllocConfig-r15, the set of PRGs is starting from the lowest RB of the narrowband $ n_{NB}$ shifted by $ n_{NB}^{shift}$, according to Table 6.2.7-1 [3].

Table 7.1.6.5-1

| System Bandwidth () | PRG Size () (PRBs) |
| --- | --- |
| ≤10 | 1 |
| 11 – 26 | 2 |
| 27 – 63 | 3 |
| 64 – 110 | 2 |

For a given serving cell c and for slot/subslot-PDSCH transmissions,

- if the UE is configured for transmission mode 9, 10 with PMI/RI reporting and with higher layer parameter widebandPRG- SlotSubslot and the scheduled PRBs are consecutive PRBs, the UE may assume that the same precoder applies on all the scheduled PRBs,

- otherwise, for a UE configured for transmission mode 9, 10 using frame structure type 1 or transmission modes 8, 9, 10 using frame structure type 2, precoding granularity is 2 resource blocks in frequency domain. Precoding Resource block Groups (PRGs) of size 2 partition the system bandwidth and each PRG consists of consecutive PRBs. The UE is expected to receive UE-specific reference signal corresponding to a PDSCH over both resource blocks of a PRG. If  then, PDSCH is not mapped to the last resource block. The UE may assume that the same precoder applies on the two PRBs within a PRG.

### 7.1.7 Modulation order and transport block size determination

To determine the modulation order and transport block size(s) in the physical downlink shared channel, the UE shall first

- if the UE is a BL/CE UE

- if PDSCH is assigned by MPDCCH DCI format 6-1A

- if the UE is configured with higher layer parameter ce-PDSCH-64QAM-Config-r15 and the DCI is mapped onto the UE specific search space and the repetition number field in the DCI indicates PDSCH repetition level 1

- if "Scheduling TBs for Unicast" field in DCI format 6-1A is present and either 4 or 6 TBs are scheduled by the corresponding DCI,

- read the 4-bit "modulation and coding scheme (![](media_svg/image194.svg) [公式≈: ^{I}MCS^{1}])" field in the DCI

- the UE is not expected to receive a DCI format 6-1A indicating

- otherwise,

- read the 5-bit extended "modulation and coding scheme (![](media_svg/image194.svg) [公式≈: ^{I}MCS^{1}])" field in the DCI

- otherwise

- read the 4-bit "modulation and coding scheme ()" field in the DCI

- The UE is not expected to receive a DCI format 6-1A indicating

- else if PDSCH is assigned by MPDCCH DCI format 6-2

- read the 3-bit "modulation and coding scheme ()" field in the DCI

- The UE is not expected to receive a DCI format 6-2 indicating

- else if PDSCH is assigned by MPDCCH DCI format 6-1B

- read the 4-bit "modulation and coding scheme ()" field in the DCI and set =.

- else if PDSCH carriers SystemInformationBlockType1-BR

- set  to the value of the parameter schedulingInfoSIB1-BR configured by higher-layers

- otherwise

- read the 5 or 6-bit "modulation and coding scheme" field () in the DCI

and second if the PDCCH DCI CRC is scrambled by P-RNTI, RA-RNTI, or SI-RNTI then

- for DCI format 1A:

- set the Table 7.1.7.2.1-1 column indicator to from Clause 5.3.3.1.3 in [4]

- for DCI format 1C:

- use Table 7.1.7.2.3-1 for determining its transport block size.

else

- if the UE is a BL/CE UE

- if MPDCCH DCI CRC is scrambled by RA-RNTI for DCI format 6-1A

- set the Table 7.1.7.2.1-1 column indicator to from Clause 5.3.3.1.12 in [4]

- else if PDSCH is assigned by MPDCCH DCI format 6-2

- use Table 7.1.7.2.3-1 for determining its transport block size.

- else if PDSCH carriers SystemInformationBlockType1-BR

- use Clause 7.1.7.2.7 for determining its transport block size.

- else if PDSCH is assigned by MPDCCH DCI format 6-1B

- use Clause 7.1.7.2.6 for determining its transport block size if the UE is not configured with higher layer parameter ce-pdsch-maxBandwidth-config with value ≥5MHz and not configured with higher layer parameter mpdcch-PDSCH-MaxBandwidth-SC-MTCH with value 24 PRBs.

- otherwise,

- set  to the total number of allocated PRBs based on the procedure defined in Clause 7.1.6.

- if PDSCH is assigned by MPDCCH DCI format 6-1A, the repetition number field in the DCI indicates PDSCH repetition level 1, and the transport block is transmitted in DwPTS of the special subframe in frame structure type 2, then

- for special subframe configuration 9 with normal cyclic prefix:

- set the Table 7.1.7.2.1-1 column indicator

- for other special subframe configurations:

- set the Table 7.1.7.2.1-1 column indicator ,

- else set the Table 7.1.7.2.1-1 column indicator .

- otherwise

- set  to the total number of allocated PRBs based on the procedure defined in Clause 7.1.6.

- if the higher layer parameter altMCS-Table is not configured, or for PDSCH assigned by DCI other than DCI format 1/1B/1D/2/2A/2B/2C/2D with CRC scrambled by C-RNTI; if the transport block is transmitted in DwPTS of the special subframe in frame structure type 2, or is transmitted in the subframes with the same duration as the DwPTS duration of a special subframe configuration in frame structure type 3, then

- for special subframe configuration 9 and 10 with normal cyclic prefix or special subframe configuration 7 with extended cyclic prefix:

- set the Table 7.1.7.2.1-1 column indicator

- for other special subframe configurations:

- set the Table 7.1.7.2.1-1 column indicator ,

- else if the higher layer parameter altMCS-Table is configured, and for PDSCH assigned by DCI format 1/1B/1D/2/2A/2B/2C/2D with CRC scrambled by C-RNTI; if the the transport block transmitted in DwPTS of the special subframe in frame structure type 2, or is transmitted in the subframes with the same duration as the DwPTS duration of a special subframe configuration in frame structure type 3, then

- if $ 44\leq   I_{MCS}\leq  58 $, set $\alpha  $ to higher layer parameter altMCS-Table-scaling, otherwise $\alpha  =1 $

- for special subframe configuration 9 and 10 with normal cyclic prefix or special subframe configuration 7 with extended cyclic prefix:

- set the Table 7.1.7.2.1-1 column indicator $ N_{PRB}=max\left \{ \lfloor  N_{PRB}^{'}\times   0.375\times  \alpha  \rfloor  ,1\right \} $

- for other special subframe configurations:

- set the Table 7.1.7.2.1-1 column indicator $ N_{PRB}=max\left \{ \lfloor  N_{PRB}^{'}\times  0.75\times  \alpha  \rfloor  ,1\right \} $

- else if the higher layer parameter altMCS-Table is configured, and for PDSCH assigned by DCI format 1/1B/1D/2/2A/2B/2C/2D with CRC scrambled by C-RNTI; then

- if $ 44\leq   I_{MCS}\leq  58 $, set $\alpha  $ to higher layer parameter altMCS-Table-scaling, otherwise $\alpha  =1 $

- set the Table 7.1.7.2.1-1 column indicator $ N_{PRB}=max\left \{ \lfloor  N_{PRB}^{'}\times  \alpha  \rfloor  ,1\right \} $

- else, set the Table 7.1.7.2.1-1 column indicator .

- for DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G, the derived transport block size (after TBS translation as described in clauses 7.1.7.2.2, 7.1.7.2.4, 7.1.7.2.5 when the transport block is mapped to more than one spatial layer) is scaled by α (for slot-PDSCH, and for subslot-PDSCH), then rounded to the closest (NOTE 1) valid transport block size in

- Table 7.1.7.2.1-1 when the transport block is mapped to one spatial layer,

- The union of Table 7.1.7.2.1-1 and Table 7.1.7.2.2-1 when the transport block is mapped to two spatial layers,

- The union of Table 7.1.7.2.1-1 and Table 7.1.7.2.4-1 when the transport block is mapped to three spatial layers,

- The union of Table 7.1.7.2.1-1 and Table 7.1.7.2.5-1 when the transport block is mapped to four spatial layers.

If the scaled TBS is closest to two valid transport block sizes, it is rounded to the larger transport block size.

NOTE 1: In the rounding procedure, and for a given serving cell:

- For UEs configured with neither altCQI-Table1024QAM-STTI nor altCQI-TableSTTI, the UE shall only include in the rounding procedure the TBS entries present in Table 7.1.7.2.1-1 with $ I_{TBS}\leq  26A $, and the entries in 7.1.7.2.2-1, 7.1.7.2.4-1, 7.1.7.2.5-1 for which the TBS_L1 is present in Table 7.1.7.2.1-1 with $ I_{TBS}\leq  26A $.

- For UEs configured with altCQI-TableSTTI, the UE shall only include in the rounding procedure the TBS entries present in Table 7.1.7.2.1-1 with $ I_{TBS}\leq  33B $, and the entries in 7.1.7.2.2-1, 7.1.7.2.4-1, 7.1.7.2.5-1 for which the TBS_L1 is present in Table 7.1.7.2.1-1 with $ I_{TBS}\leq  33B $.

The UE may skip decoding a transport block in an initial transmission if the effective channel code rate is higher than 0.932, where the effective channel code rate is defined as the number of downlink information bits (including CRC bits) divided by the number of physical channel bits on PDSCH. If the UE skips decoding, the physical layer indicates to higher layer that the transport block is not successfully decoded. For the special subframe configurations 0 and 5 with normal downlink CP or configurations 0 and 4 with extended downlink CP in frame structure type 2, or for subframes with the same duration as the DwPTS duration of the special subframe configuration 0 and 5 in frame structure type 3, with the special subframe configurations shown in Table 4.2-1 of [3], or for the special subframe configuration 10 configured by the higher layer signalling ssp10-CRS-LessDwPTS, a non-BL/CE UE shall assume there is no PDSCH transmission in DwPTS of the special subframe.

For frame structure type 2, a BL/CE UE shall assume PDSCH is dropped in a special subframe considered as BL/CE DL subframe according to Clause 6.8B.1 of [3] in the following cases

- for PDSCH scheduled from UE-specific search space, Type0-MPDCCH common search space, Type1-MPDCCH common search space, Type1A-MPDCCH common search space, Type2-MPDCCH common search space or Type2A-MPDCCH common search space, if an MPDCCH belonging to the corresponding search space is dropped in the special subframe according to clause 9.1.5.

- if PDSCH carries SI messages.

#### 7.1.7.1 Modulation order and redundancy version determination

For BL/CE UEs configured with CEModeA, is used in place of in the rest of this Clause.

The UE shall use = 2 if the DCI CRC is scrambled by P-RNTI, RA-RNTI, SI-RNTI, or SC-RNTI, or if PDSCH is assigned by MPDCCH DCI Format 6-1B, or if PDSCH carriers SystemInformationBlockType1-BR, or if PDSCH carries BL/CE SI messages, or if the UE is configured with CEModeA and higher layer parameter ce-pdsch-puschEnhancement-config with value 'On' and repetition number field in the corresponding DCI indicates a value greater than 1, otherwise,

- if the higher layer parameter altMCS-Table is configured, and if the PDSCH is assigned by a PDCCH/EPDCCH with DCI format 1/1B/1D/2/2A/2B/2C/2D with CRC scrambled by C-RNTI,

- if the assigned PDSCH is transmitted only in the second slot of a subframe, the UE shall use![](media_svg/image200.svg) [公式≈: ^{I}MCS]and Table 7.1.7.1-1C to determine the modulation order (![](media_svg/image210.svg) [公式≈: _{Q}_{m}&apos;]). The modulation order (![](media_svg/image209.svg) [公式≈: ^{Q}m]) used in the physical downlink shared channel is set to ![](media_svg/image211.svg) [公式≈: _{Q}_{m}_{=}_{Q}_{m}&apos;];

- otherwise, the UE shall use![](media_svg/image200.svg) [公式≈: ^{I}MCS]and Table 7.1.7.1-1C to determine the modulation order (![](media_svg/image209.svg) [公式≈: ^{Q}m]) used in the physical downlink shared channel.

- else if the higher layer parameter altCQI-Table-1024QAM-r15 is configured, and if the PDSCH is assigned by a PDCCH/EPDCCH with DCI format 1/1B/1D/2/2A/2B/2C/2D with CRC scrambled by C-RNTI,

- if the assigned PDSCH is transmitted only in the second slot of a subframe, the UE shall useand Table 7.1.7.1-1B to determine the modulation order (). The modulation order () used in the physical downlink shared channel is set to ;

- otherwise, the UE shall useand Table 7.1.7.1-1B to determine the modulation order () used in the physical downlink shared channel.

- else if the higher layer parameter altCQI-Table-1024QAM-STTI_r15 is configured, and if the PDSCH is assigned by a PDCCH/SPDCCH with DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G with CRC scrambled by C-RNTI or SPS-C-RNTI,

- the UE shall useand Table 7.1.7.1-1B to determine the modulation order () used in the physical downlink shared channel.

- else if the higher layer parameter altCQI-Table-r12 is configured, and if the PDSCH is assigned by a PDCCH/EPDCCH with DCI format 1/1B/1D/2/2A/2B/2C/2D with CRC scrambled by C-RNTI,

- if the assigned PDSCH is transmitted only in the second slot of a subframe, the UE shall useand Table 7.1.7.1-1A to determine the modulation order (). The modulation order () used in the physical downlink shared channel is set to ;

- otherwise, the UE shall useand Table 7.1.7.1-1A to determine the modulation order () used in the physical downlink shared channel.

- else

- if the higher layer parameter altCQI-Table-STTI-r15 is configured, and if the PDSCH is assigned by a    PDCCH/SPDCCH with DCI format 7-1A/7-1B/7-1C/7-1E/7-1F/7-1G with CRC scrambled by C-RNTI,

- the UE shall useand Table 7.1.7.1-1A to determine the modulation order () used in the physical downlink shared channel.

- if the assigned PDSCH is transmitted only in the second slot of a subframe, the UE shall useand Table 7.1.7.1-1 to determine the modulation order (). The modulation order () used in the physical downlink shared channel is set to ;

- otherwise, the UE shall useand Table 7.1.7.1-1 to determine the modulation order () used in the physical downlink shared channel.

Table 7.1.7.1-1: Modulation and TBS index table for PDSCH

| MCS Index | Modulation Order | Modulation Order | TBS Index |
| --- | --- | --- | --- |
| 0 | 2 | 2 | 0 |
| 1 | 2 | 2 | 1 |
| 2 | 2 | 2 | 2 |
| 3 | 2 | 2 | 3 |
| 4 | 2 | 2 | 4 |
| 5 | 2 | 4 | 5 |
| 6 | 2 | 4 | 6 |
| 7 | 2 | 4 | 7 |
| 8 | 2 | 4 | 8 |
| 9 | 2 | 4 | 9 |
| 10 | 4 | 6 | 9 |
| 11 | 4 | 6 | 10 |
| 12 | 4 | 6 | 11 |
| 13 | 4 | 6 | 12 |
| 14 | 4 | 6 | 13 |
| 15 | 4 | 6 | 14 |
| 16 | 4 | 6 | 15 |
| 17 | 6 | 6 | 15 |
| 18 | 6 | 6 | 16 |
| 19 | 6 | 6 | 17 |
| 20 | 6 | 6 | 18 |
| 21 | 6 | 6 | 19 |
| 22 | 6 | 6 | 20 |
| 23 | 6 | 6 | 21 |
| 24 | 6 | 6 | 22 |
| 25 | 6 | 6 | 23 |
| 26 | 6 | 6 | 24 |
| 27 | 6 | 6 | 25 |
| 28 | 6 | 6 | 26/26A |
| 29 | 2 | 2 | reserved |
| 30 | 4 | 4 |  |
| 31 | 6 | 6 |  |

Table 7.1.7.1-1A. Modulation and TBS index table 2 for PDSCH

| MCS Index | Modulation Order | Modulation Order | TBS Index |
| --- | --- | --- | --- |
| 0 | 2 | 2 | 0 |
| 1 | 2 | 2 | 2 |
| 2 | 2 | 2 | 4 |
| 3 | 2 | 4 | 6 |
| 4 | 2 | 4 | 8 |
| 5 | 4 | 6 | 10 |
| 6 | 4 | 6 | 11 |
| 7 | 4 | 6 | 12 |
| 8 | 4 | 6 | 13 |
| 9 | 4 | 6 | 14 |
| 10 | 4 | 8 | 15 |
| 11 | 6 | 8 | 16 |
| 12 | 6 | 8 | 17 |
| 13 | 6 | 8 | 18 |
| 14 | 6 | 8 | 19 |
| 15 | 6 | 8 | 20 |
| 16 | 6 | 8 | 21 |
| 17 | 6 | 8 | 22 |
| 18 | 6 | 8 | 23 |
| 19 | 6 | 8 | 24 |
| 20 | 8 | 8 | 25 |
| 21 | 8 | 8 | 27 |
| 22 | 8 | 8 | 28 |
| 23 | 8 | 8 | 29 |
| 24 | 8 | 8 | 30 |
| 25 | 8 | 8 | 31 |
| 26 | 8 | 8 | 32 |
| 27 | 8 | 8 | 33/33A/33B |
| 28 | 2 | 2 | reserved |
| 29 | 4 | 4 |  |
| 30 | 6 | 6 |  |
| 31 | 8 | 8 |  |

Table 7.1.7.1-1B. Modulation and TBS index table 3 for PDSCH

| MCS Index | Modulation Order | Modulation Order | TBS Index |
| --- | --- | --- | --- |
| 0 | 2 | 2 | 0 |
| 1 | 2 | 2 | 2 |
| 2 | 2 | 2 | 4 |
| 3 | 2 | 4 | 6 |
| 4 | 2 | 4 | 8 |
| 5 | 4 | 6 | 11 |
| 6 | 4 | 6 | 13 |
| 7 | 4 | 8 | 15 |
| 8 | 6 | 8 | 16 |
| 9 | 6 | 8 | 18 |
| 10 | 6 | 8 | 20 |
| 11 | 6 | 8 | 21 |
| 12 | 6 | 8 | 22 |
| 13 | 6 | 8 | 23 |
| 14 | 6 | 8 | 24 |
| 15 | 8 | 8 | 25 |
| 16 | 8 | 8 | 27 |
| 17 | 8 | 8 | 28 |
| 18 | 8 | 8 | 29 |
| 19 | 8 | 8 | 30 |
| 20 | 8 | 8 | 31 |
| 21 | 8 | 8 | 32 |
| 22 | 8 | 8 | 33/33A/33B |
| 23 | 10 | 10 | 34A |
| 24 | 10 | 10 | 35 |
| 25 | 10 | 10 | 36 |
| 26 | 10 | 10 | 37A/37 |
| 27 | 2 | 2 | reserved |
| 28 | 4 | 4 |  |
| 29 | 6 | 6 |  |
| 30 | 8 | 8 |  |
| 31 | 10 | 10 |  |

Table 7.1.7.1-1C. Modulation and TBS index table 4 for PDSCH

| MCS Index ![](media_svg/image200.svg) [公式≈: ^{I}MCS] | Modulation Order ![](media_svg/image209.svg) [公式≈: ^{Q}m] | Modulation Order ![](media_svg/image214.svg) [公式≈: _{Q}_{m}&apos;] | TBS Index ![](media_svg/image215.svg) [公式≈: ^{I}TBS] |
| --- | --- | --- | --- |
| 0 | 2 | 2 | 0 |
| 1 | 2 | 2 | 1 |
| 2 | 2 | 2 | 2 |
| 3 | 2 | 2 | 3 |
| 4 | 2 | 2 | 4 |
| 5 | 2 | 4 | 5 |
| 6 | 2 | 4 | 6 |
| 7 | 2 | 4 | 7 |
| 8 | 2 | 4 | 8 |
| 9 | 2 | 4 | 9 |
| 10 | 4 | 6 | 9 |
| 11 | 4 | 6 | 10 |
| 12 | 4 | 6 | 11 |
| 13 | 4 | 6 | 12 |
| 14 | 4 | 6 | 13 |
| 15 | 4 | 6 | 14 |
| 16 | 4 | 6 | 15 |
| 17 | 6 | 6 | 15 |
| 18 | 6 | 6 | 16 |
| 19 | 6 | 6 | 17 |
| 20 | 6 | 6 | 18 |
| 21 | 6 | 6 | 19 |
| 22 | 6 | 6 | 20 |
| 23 | 6 | 6 | 21 |
| 24 | 6 | 6 | 22 |
| 25 | 6 | 6 | 23 |
| 26 | 6 | 6 | 24 |
| 27 | 6 | 6 | 25 |
| 28 | 6 | 6 | 27 |
| 29 | 6 | 6 | 28 |
| 30 | 8 | 8 | 25 |
| 31 | 8 | 8 | 27 |
| 32 | 8 | 8 | 28 |
| 33 | 8 | 8 | 29 |
| 34 | 8 | 8 | 30 |
| 35 | 8 | 8 | 31 |
| 36 | 8 | 8 | 32 |
| 37 | 8 | 8 | 33A |
| 38 | 8 | 8 | 33/33B |
| 39 | 10 | 10 | 34A |
| 40 | 10 | 10 | 35 |
| 41 | 10 | 10 | 36 |
| 42 | 10 | 10 | 37A |
| 43 | 10 | 10 | 37 |
| 44 | 2 | 2 | 0 |
| 45 | 2 | 2 | 2 |
| 46 | 4 | 6 | 9 |
| 47 | 4 | 6 | 11 |
| 48 | 4 | 6 | 13 |
| 49 | 6 | 6 | 15 |
| 50 | 6 | 6 | 17 |
| 51 | 6 | 6 | 19 |
| 52 | 6 | 6 | 21 |
| 53 | 8 | 8 | 25 |
| 54 | 8 | 8 | 28 |
| 55 | 8 | 8 | 30 |
| 56 | 8 | 8 | 32 |
| 57 | 10 | 10 | 34A |
| 58 | 10 | 10 | 36 |
| 59 | 2 | 2 | Reserved |
| 60 | 4 | 4 |  |
| 61 | 6 | 6 |  |
| 62 | 8 | 8 |  |
| 63 | 10 | 10 |  |

For a given serving cell, if the UE is configured with higher layer parameter blindSubframePDSCH-Repetitions, for PDSCH transmitted in a given block of k subframes corresponding to DCI format 1A with CRC scrambled by C-RNTI in UE-specific search space, the redundancy version (rvidx) for the  subframe is determined according to

- Table 7.1.7.1-2 using ![](media_svg/image217.svg) [公式: rvjrv=+()mod4_{DCI}], where ![](media_svg/image218.svg) [公式: jk=−0,1,...,1] if the configured higher layer parameter RV-cyclingSequenceSubframePDSCH-Repetitions parameter is set to '{0,2,3,1}';

- Otherwise, ![](media_svg/image219.svg) [公式: rv=0]for all of the k PDSCH transmissions.

where the value of ![](media_svg/image220.svg) [公式≈: ^{rv}DCI] and k are determined by the 'Redundancy version' and 'Repetition number' fields in the corresponding DCI, respectively.

For a given serving cell, if the UE is configured with higher layer parameter blindSlotSubslotPDSCH-Repetitions, for PDSCH transmitted in a given block of k slots/subslots corresponding to DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G, the redundancy version (rvidx) for the  slot/subslot is determined according to

- Table 7.1.7.1-2 using ![](media_svg/image217.svg) [公式: rvjrv=+()mod4_{DCI}], where ![](media_svg/image218.svg) [公式: jk=−0,1,...,1] if the configured higher layer parameter RV-cyclingSequenceSlotsublotPDSCH-Repetitions parameter is set to '{0,2,3,1}';

- Otherwise, ![](media_svg/image219.svg) [公式: rv=0]for all of the k PDSCH transmissions.

where the value of ![](media_svg/image220.svg) [公式≈: ^{rv}DCI] and k are determined by the 'Redundancy version' and 'Repetition number' fields in the corresponding DCI, respectively.

For a UE configured with altMCS-Table, the UE is not expected to receive a PDSCH with a modulation order of 1024QAM unless configured with altCQI-Table-1024QAM-r15, and the UE is not expected to receive a PDSCH with a modulation order of 256QAM unless configured with altCQI-Table-r12 or altCQI-Table-1024QAM-r15.

For BL/CE UEs, for a PDSCH not carrying SystemInformationBlockType1-BR or SI message, the same redundancy version is applied to PDSCH associated with a TB that is transmitted in a given block of  consecutive subframes associated with the TB, including subframes that are not BL/CE DL subframes. The subframe number of the first subframe in each block of consecutive subframes, denoted as , satisfies , where  for FDD and  for TDD. Denote  as the subframe number of the first downlink subframe intended for PDSCH associated with a TB, as defined in Clause 7.1.11. The PDSCH transmission associated with the TB spans $ N_{abs,TB}^{PDSCH}$ consecutive subframes associated with the TB, including subframes that are not BL/CE DL subframes where the PDSCH transmission is postponed and excluding subframes associated with other TBs scheduled by the DCI, if any. For the  block of consecutive subframes within the set of $ N_{abs,TB}^{PDSCH}$ subframes associated with the TB as described above, the redundancy version (rvidx) associated with the TB is determined according to Table 7.1.7.1-2 using , where , and $ J^{PDSCH}=\lceil  \frac {N_{abs,TB}^{PDSCH}+\left ( \left ( i_{0}-\delta  \right ) modN_{acc}\right ) }{N_{acc}}\rceil  $. The  blocks of subframes are sequential in time, starting with  to which subframe belongs. For a BL/CE UE configured with CEModeB, or a BL/CE UE receiving PDSCH associated with P-RNTI,  for FDD and  for TDD, and . For a BL/CE UE configured in CEModeA, . For a BL/CE UE configured in CEModeA and not configured with the higher layer parameter ce-PDSCH-MultiTB-Config,  for the TB is determined by the 'Redundancy version' field in DCI format 6-1A. For a BL/CE UE configured in CEModeA and configured with higher layer parameter ce-PDSCH-MultiTB-Config,

- if $ N_{TB}=1 $, for the TB is determined by the 'Redundancy version' in the 'Scheduling TBs for Unicast' field in DCI format 6-1A

- else if $ N_{TB}=2 $ and the HARQ process IDs for each of the scheduled TBs are h1 and h2 (h1<h2),  of the scheduled TB with HARQ process ID h1 is determined by the 'Redundancy version for TB 1' in the 'Scheduling TBs for Unicast' field in DCI format 6-1A, and  of the scheduled TB with HARQ process ID h2 is determined as follows:

- If the UE is configured with higher layer parameter ce-PDSCH-64QAM-Config and the repetition number field in the DCI indicates no PDSCH repetition, it is given by the'Redundancy version for TB 1' in the 'Scheduling TBs for Unicast' field in DCI format 6-1A

- else if the UE is configured with higher layer parameter mpdcch-pdsch-HoppingConfig set to 'on' and the repetition number field in the DCI indicates PDSCH repetition, it is given by the 'Redundancy version for TB 1' in the 'Scheduling TBs for Unicast' field in DCI format 6-1A

- else it is given by the 'Redundancy version for TB 2' in the 'Scheduling TBs for Unicast' field in DCI format 6-1A

- else if $ N_{TB}$ = 4 or 6 is indicated by the corresponding DCI,  for all scheduled TBs

- else

- if the UE is configured with higher layer parameter ce-PDSCH-64QAM-Config and the repetition number field in the DCI indicates no PDSCH repetition,  for all TBs

- else if the UE is configured with higher layer parameter mpdcch-pdsch-HoppingConfig set to 'on' and the repetition number field in the DCI indicates PDSCH repetition,  for all TBs

- else  of all TBs is determined by the 'Redundancy version for all TBs' in the 'Scheduling TBs for Unicast' field in DCI format 6-1A

where $ N_{TB}$ is the number of scheduled TB determined in the corresponding DCI.

Table 7.1.7.1-2: Redundancy version

| Redundancy version Index | rvidx |
| --- | --- |
| 0 | 0 |
| 1 | 2 |
| 2 | 3 |
| 3 | 1 |

#### 7.1.7.2 Transport block size determination

For BL/CE UEs configured with CEModeA,  is used in place of in the rest of this Clause

If the DCI CRC is scrambled by P-RNTI, RA-RNTI, or SI-RNTI then

- for DCI format 1A or DCI format 6-1A:

- the UE shall set the TBS index () equal to  and determine its TBS by the procedure in Clause 7.1.7.2.1 for .

- for DCI format 1C and DCI format 6-2:

- the UE shall set the TBS index () equal to  and determine its TBS from Table 7.1.7.2.3-1.

else if the DCI CRC is scrambled by SC-RNTI then

- the UE shall set the TBS index () equal to  and determine its TBS from Table 7.1.7.2.3-1.

else if the higher layer parameter altMCS-Table is configured, and for DCI format 1/1B/1D/2/2A/2B/2C/2D with CRC scrambled by C-RNTI

- for $ 0\leq   I_{MCS}\leq   58 $, the UE shall first determine the TBS index (![](media_svg/image215.svg) [公式≈: ^{I}TBS]) using![](media_svg/image200.svg) [公式≈: ^{I}MCS]and Table 7.1.7.1-1C except if the transport block is disabled in DCI formats 2, 2A, 2B, 2C and 2D as specified below. When $ I_{MCS}=38 $, if the UE is scheduled by DCI formats 1/1B/2/2A and is configured with b33 in tbsIndexAlt2, ![](media_svg/image215.svg) [公式≈: ^{I}TBS] is 33B; otherwise ![](media_svg/image215.svg) [公式≈: ^{I}TBS] is 33. For a transport block that is not mapped to more than single-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.1. For a transport block that is mapped to two-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.2. For a transport block that is mapped to three-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.4. For a transport block that is mapped to four-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.5.

- for $ 59\leq   I_{MCS}\leq   63 $, the TBS is assumed to be as determined from DCI transported in the latest PDCCH/EPDCCH for the same transport block using $ 0\leq   I_{MCS}\leq   58 $.

- In DCI formats 2, 2A, 2B, 2C and 2D a transport block is disabled if ![](media_svg/image239.svg) [公式: I_{MCS}=0] and if rvidx = 1 otherwise the transport block is enabled.

else if the higher layer parameter altCQI-Table-r12 is configured, then

- for DCI format 1A with CRC scrambled by C-RNTI and for DCI format 1/1A/2/2A/2B/2C/2D with CRC scrambled by SPS C-RNTI:

- for , the UE shall first determine the TBS index () usingand Table 7.1.7.1-1 except if the transport block is disabled in DCI formats 2, 2A, 2B, 2C and 2D as specified below. For a transport block that is not mapped to more than single-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.1.

- for, the TBS is assumed to be as determined from DCI transported in the latest PDCCH/EPDCCH for the same transport block using . If there is no PDCCH/EPDCCH for the same transport block using, and if the initial PDSCH for the same transport block is semi-persistently scheduled, the TBS shall be determined from the most recent semi-persistent scheduling assignment PDCCH/EPDCCH.

- In DCI formats 2, 2A, 2B, 2C and 2D a transport block is disabled if  and if rvidx = 1 otherwise the transport block is enabled.

- for DCI format 1/1B/1D/2/2A/2B/2C/2D with CRC scrambled by C-RNTI

- for , the UE shall first determine the TBS index () usingand Table 7.1.7.1-1A except if the transport block is disabled in DCI formats 2, 2A, 2B, 2C and 2D as specified below. When , if the UE is scheduled by DCI formats 2C/2D and is configured with a33 in tbsIndexAlt,  is 33A, or if the UE is scheduled by DCI formats 1/1B/2/2A and is configured with b33 in tbsIndexAlt2,  is 33B; otherwise  is 33. For a transport block that is not mapped to more than single-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.1. For a transport block that is mapped to two-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.2. For a transport block that is mapped to three-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.4. For a transport block that is mapped to four-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.5.

- for , the TBS is assumed to be as determined from DCI transported in the latest PDCCH/EPDCCH for the same transport block using .

- In DCI formats 2, 2A, 2B, 2C and 2D a transport block is disabled if  and if rvidx = 1 otherwise the transport block is enabled.

else if the higher layer parameter altCQI-Table-STTI-r15 is configured, then

- for DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G with CRC scrambled by SPS C-RNTI:

- for , the UE shall determine the TBS index () using by the procedure in Clause 7.1.7.

- for, the TBS is assumed to be as determined from DCI transported in the latest PDCCH/SPDCCH for the same transport block using . If there is no PDCCH/SPDCCH for the same transport block using, and if the initial PDSCH for the same transport block is semi-persistently scheduled, the TBS shall be determined from the most recent semi-persistent scheduling assignment PDCCH/SPDCCH.

- for DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G with CRC scrambled by C-RNTI

- for , the UE shall first determine the TBS index () usingand Table 7.1.7.1-1A. When , if the UE is scheduled by DCI formats 7-1F/7-1G and is configured with a33 in tbsIndexAlt-STTI,  is 33A, or if the UE is scheduled by DCI formats 7-1D/7-1C/7-1B and is configured with b33 in tbsIndexAlt2-STTI,  is 33B; otherwise  is 33.When ,  is 33. The TBS is determined by the procedure in Clause 7.1.7.

- for , the TBS is assumed to be as determined from DCI transported in the latest PDCCH/SPDCCH for the same transport block using .

else if the higher layer parameter altCQI-Table-1024QAM-r15 is configured, then

- for DCI format 1A with CRC scrambled by C-RNTI and for DCI format 1/1A/2/2A/2B/2C/2D with CRC scrambled by SPS C-RNTI:

- for , the UE shall first determine the TBS index () usingand Table 7.1.7.1-1. For a transport block, the TBS is determined by the procedure in Clause 7.1.7.2.1.

- for , the TBS is assumed to be as determined from DCI transported in the latest PDCCH/EPDCCH for the same transport block using . If there is no PDCCH/EPDCCH for the same transport block using , and if the initial PDSCH for the same transport block is semi-persistently scheduled, the TBS shall be determined from the most recent semi-persistent scheduling assignment PDCCH/EPDCCH.

- for DCI format 1/1B/1D/2/2A/2B/2C/2D with CRC scrambled by C-RNTI;

- for , the UE shall first determine the TBS index () usingand Table 7.1.7.1-1B except if the transport block is disabled in DCI formats 2, 2A, 2B, 2C and 2D as specified below. When , if the UE is scheduled by DCI formats 2C/2D and is configured with a33 in tbsIndexAlt,  is 33A, or if the UE is scheduled by DCI formats 1/1B/2/2A and is configured with b33 in tbsIndexAlt2,  is 33B; otherwise  is 33. When , if the UE is configured with a37 in tbsIndexAlt3,  is 37A, otherwise  is 37. For a transport block that is not mapped to more than single-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.1. For a transport block that is mapped to two-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.2. For a transport block that is mapped to three-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.4. For a transport block that is mapped to four-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.5.

- for , the TBS is assumed to be as determined from DCI transported in the latest PDCCH/EPDCCH for the same transport block using . If there is no PDCCH/EPDCCH for the same transport block using , and if the initial PDSCH for the same transport block is semi-persistently scheduled, the TBS shall be determined from the most recent semi-persistent scheduling assignment PDCCH/EPDCCH.

- In DCI formats 2, 2A, 2B, 2C and 2D a transport block is disabled if  and if rvidx = 1 otherwise the transport block is enabled.

else if the higher layer parameter altCQI-Table-1024QAM-STTI_r15 is configured, then

- for DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G with CRC scrambled by C-RNTI or SPS C-RNTI;

- for , the UE shall first determine the TBS index () usingand Table 7.1.7.1-1B. When , if the UE is scheduled by DCI formats 7-1F/7-1G and is configured with a33 in tbsIndexAlt-STTI,  is 33A, or if the UE is scheduled by DCI formats 7-1B/7-1C/7-1D and is configured with b33 in tbsIndexAlt2-STTI,  is 33B; otherwise  is 33. When , if the UE is scheduled by DCI formats 7-1F/7-1G and is configured with a37 in tbsIndexAlt3-STTI,  is 37A, otherwise  is 37. For a transport block that is not mapped to more than single-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7 and 7.1.7.2.1. For a transport block that is mapped to two-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7 and 7.1.7.2.2. For a transport block that is mapped to three-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7 and 7.1.7.2.4. For a transport block that is mapped to four-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7 and 7.1.7.2.5.

- for , the TBS is assumed to be as determined from DCI transported in the latest PDCCH/SPDCCH for the same transport block using . If there is no PDCCH/SPDCCH for the same transport block using , and if the initial PDSCH for the same transport block is semi-persistently scheduled, the TBS shall be determined from the most recent semi-persistent scheduling assignment PDCCH/SPDCCH.

else if the UE supports ce-pdsch-pusch-maxBandwidth with value ≥5MHz, or if the UE is configured with higher layer parameter ce-PDSCH-64QAM-Config-r15 and the MPDCCH DCI format 6-1A is mapped onto the UE specific search space and the repetition number field in the DCI indicates PDSCH repetition level 1,

- for, the TBS is assumed to be as determined from DCI transported in the latest MPDCCH for the same transport block using . If there is no MPDCCH for the same transport block using, and if the initial PDSCH for the same transport block is semi-persistently scheduled, the TBS shall be determined from the most recent semi-persistent scheduling assignment MPDCCH.

- forthe UE shall first determine the TBS index () usingand Table 7.1.7.1-1

- if the UE is configured with higher layer parameter ce-pdsch-maxBandwidth-config with value 5MHz or if the UE is configured with higher layer parameter pdsch-MaxBandwidth-SC-MTCH with value 24 PRBs

- For CEModeA,

- if the UE is configured with higher layer parameter ce-PDSCH-64QAM-Config-r15 and the MPDCCH DCI format 6-1A is mapped onto the UE specific search space and the repetition number field in the DCI indicates PDSCH repetition level 1,

- set ![](media_svg/image267.svg) [公式: TBS^{±}] to the TBS determined by the procedure in Clause 7.1.7.2.1,

- ![](media_svg/image268.svg) [公式: TBSTBS=min,4008{±}]

- otherwise, TBS is determined by the procedure in Clause 7.1.7.2.8 for

- For CEModeB, TBS is determined by the procedure in Clause 7.1.7.2.8 for

- if the UE is configured with higher layer parameter ce-pdsch-maxBandwidth-config with value > 5MHz

- For CEModeA,

- if the UE is configured with higher layer parameter ce-PDSCH-64QAM-Config-r15 and the MPDCCH DCI format 6-1A is mapped onto the UE specific search space and the repetition number field in the DCI indicates PDSCH repetition level 1,

- set ![](media_svg/image267.svg) [公式: TBS^{±}] to the TBS determined by the procedure in Clause 7.1.7.2.1,

- ![](media_svg/image271.svg) [公式: TBSTBS=min,{±27376}]

- otherwise, TBS is determined by the procedure in Clause 7.1.7.2.1 for

- For CEModeB, TBS is determined by the procedure in Clause 7.1.7.2.1 for

- otherwise,

- if the UE is configured with higher layer parameter ce-PDSCH-64QAM-Config-r15 and the MPDCCH DCI format 6-1A is mapped onto the UE specific search space and the repetition number field in the DCI indicates PDSCH repetition level 1,

- set ![](media_svg/image267.svg) [公式: TBS^{±}] to the TBS determined by the procedure in Clause 7.1.7.2.1,

- $ TBS=\operatorname {min}\left (\left \{ \begin {matrix}TBS^{'}, & 1736\end {matrix}\right \} \right )$ if UE is configured with higher layer parameter ce-PDSCH-maxTBS, $ TBS=\operatorname {min}\left (\left \{ \begin {matrix}TBS^{'}, & 1000\end {matrix}\right \} \right )$ otherwise

- otherwise

- TBS is determined by the procedure in Clause 7.1.7.2.1

else

- for, the UE shall first determine the TBS index () usingand Table 7.1.7.1-1 except if the transport block is disabled in DCI formats 2, 2A, 2B, 2C and 2D as specified below. When , if the UE is scheduled by DCI formats 2C/2D and is configured with a26 in tbsIndexAlt,  is 26A; otherwise  is 26. For a transport block that is not mapped to more than single-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.1. For a transport block that is mapped to two-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.2. For a transport block that is mapped to three-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.4. For a transport block that is mapped to four-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.5.

- for, the TBS is assumed to be as determined from DCI transported in the latest PDCCH/EPDCCH for the same transport block using . If there is no PDCCH/EPDCCH for the same transport block using, and if the initial PDSCH for the same transport block is semi-persistently scheduled, the TBS shall be determined from the most recent semi-persistent scheduling assignment PDCCH/EPDCCH.

- In DCI formats 2, 2A, 2B, 2C and 2D a transport block is disabled if  and if rvidx = 1 otherwise the transport block is enabled.

For a BL/CE UE, if the UE is configured with higher layer parameter ce-PDSCH-MultiTB-Config and multiple TB, ![](media_svg/image277.svg) [公式≈: ^{1}^{<<}^{NN}TBTB,max], are scheduled in the corresponding DCI with CRC scrambled by C-RNTI, the HARQ process ID ![](media_svg/image278.svg) [公式≈: hskNiN_{ii}=+=−_{TB,maxTB},0,1,,1,κ]for each of the scheduled ![](media_svg/image279.svg) [公式≈: ^{N}TB] TBs are determined from the value of the 'HARQ index with offset' in the 'Scheduling TBs for Unicast' field for CEmodeA or the HARQ index in the 'Scheduling TBs for Unicast' field for CEmodeB in the corresponding DCI which is a combinatorial index r defined as ![](media_svg/image280.svg) [公式≈: ^{r}^{=}^{N}^{⊆}i^{TB}=0^{−}^{1}^{Ns}^{TB,max}NiTB−^{−}^{i}]$+r_{offset}$, where

- the set ![](media_svg/image281.svg) [公式≈: {s_{i}}_{i}^{N}_{=}^{TB}_{0}^{−}^{1}], (![](media_svg/image282.svg) [公式≈: ^{1,}^{≥≥<}^{sNss}iiiTB,max1+]) contains the ![](media_svg/image279.svg) [公式≈: ^{N}TB] sorted HARQ process IDs and ![](media_svg/image283.svg) [公式≈: x_{y}_{=}^{√}⌡_{⌠}_{⌡}_{∞}^{⊇}⊕_{⊕}_{⊗}_{0}^{x}_{y}^{⇒}⇐_{⇐}_{⇔}x_{x}÷_{<}y_{y}] is the extended binomial coefficient, resulting in unique label ![](media_svg/image284.svg) [公式≈: r⎰−^{√∅}^{⌡⌡}⌠∇_{⌡⌡}_{∞∈}0,,1λ^{⊇⇒}⊕⇐_{⊕⇐}_{⊗⇔}^{N}^{TB,max}_{N}_{TB}]$+r_{offset}$,

- $ r_{offset}$ is the offset value as defined in 5.3.3.1.12 of [4] for CE mode A, and $ r_{offset}=0 $ for CEmodeB,

- ![](media_svg/image279.svg) [公式≈: ^{N}TB] is the number of scheduled TB, and

- ![](media_svg/image285.svg) [公式≈: ^{N}TB,max^{=}^{8}] if UE is configured with CEModeA, and ![](media_svg/image286.svg) [公式≈: ^{N}TB,max^{=}^{4}] if UE is configured with CEModeB,

- ![](media_svg/image287.svg) [公式: k=1] if UE is configured with CEModeA, and 'Multi-TB HARQ processes group' field is present and set to '1' in the corresponding DCI, ![](media_svg/image288.svg) [公式: k=0] otherwise.

For a BL/CE UE, if the UE is configured with higher layer parameter ce-PDSCH-MultiTB-Config and $ N_{TB,max}$ TBs are scheduled in the corresponding DCI with CRC scrambled by C-RNTI, the HARQ process IDs for each scheduled TB are $ h_{i}=i+kN_{TB,max}$  , $ i=0,1,\ldots  ,N_{TB,max}-1 $, where

- ![](media_svg/image285.svg) [公式≈: ^{N}TB,max^{=}^{8}] if UE is configured with CEModeA, and ![](media_svg/image286.svg) [公式≈: ^{N}TB,max^{=}^{4}] if UE is configured with CEModeB,

- if UE is configured with CEModeA, and 'Multi-TB HARQ processes group' field is present and set to '1' in the corresponding DCI, ![](media_svg/image288.svg) [公式: k=0] otherwise.

The NDI and HARQ process ID, as signalled on PDCCH/EPDCCH/MPDCCH/SPDCCH, and the TBS, as determined above, shall be delivered to higher layers.

##### 7.1.7.2.1 Transport blocks not mapped to two or more layer spatial multiplexing

For, the TBS is given by the (,) entry of Table 7.1.7.2.1-1.

Table 7.1.7.2.1-1: Transport block size table (dimension 44×110)

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| 0 | 16 | 32 | 56 | 88 | 120 | 152 | 176 | 208 | 224 | 256 |
| 1 | 24 | 56 | 88 | 144 | 176 | 208 | 224 | 256 | 328 | 344 |
| 2 | 32 | 72 | 144 | 176 | 208 | 256 | 296 | 328 | 376 | 424 |
| 3 | 40 | 104 | 176 | 208 | 256 | 328 | 392 | 440 | 504 | 568 |
| 4 | 56 | 120 | 208 | 256 | 328 | 408 | 488 | 552 | 632 | 696 |
| 5 | 72 | 144 | 224 | 328 | 424 | 504 | 600 | 680 | 776 | 872 |
| 6 | 328 | 176 | 256 | 392 | 504 | 600 | 712 | 808 | 936 | 1032 |
| 7 | 104 | 224 | 328 | 472 | 584 | 712 | 840 | 968 | 1096 | 1224 |
| 8 | 120 | 256 | 392 | 536 | 680 | 808 | 968 | 1096 | 1256 | 1384 |
| 9 | 136 | 296 | 456 | 616 | 776 | 936 | 1096 | 1256 | 1416 | 1544 |
| 10 | 144 | 328 | 504 | 680 | 872 | 1032 | 1224 | 1384 | 1544 | 1736 |
| 11 | 176 | 376 | 584 | 776 | 1000 | 1192 | 1384 | 1608 | 1800 | 2024 |
| 12 | 208 | 440 | 680 | 904 | 1128 | 1352 | 1608 | 1800 | 2024 | 2280 |
| 13 | 224 | 488 | 744 | 1000 | 1256 | 1544 | 1800 | 2024 | 2280 | 2536 |
| 14 | 256 | 552 | 840 | 1128 | 1416 | 1736 | 1992 | 2280 | 2600 | 2856 |
| 15 | 280 | 600 | 904 | 1224 | 1544 | 1800 | 2152 | 2472 | 2728 | 3112 |
| 16 | 328 | 632 | 968 | 1288 | 1608 | 1928 | 2280 | 2600 | 2984 | 3240 |
| 17 | 336 | 696 | 1064 | 1416 | 1800 | 2152 | 2536 | 2856 | 3240 | 3624 |
| 18 | 376 | 776 | 1160 | 1544 | 1992 | 2344 | 2792 | 3112 | 3624 | 4008 |
| 19 | 408 | 840 | 1288 | 1736 | 2152 | 2600 | 2984 | 3496 | 3880 | 4264 |
| 20 | 440 | 904 | 1384 | 1864 | 2344 | 2792 | 3240 | 3752 | 4136 | 4584 |
| 21 | 488 | 1000 | 1480 | 1992 | 2472 | 2984 | 3496 | 4008 | 4584 | 4968 |
| 22 | 520 | 1064 | 1608 | 2152 | 2664 | 3240 | 3752 | 4264 | 4776 | 5352 |
| 23 | 552 | 1128 | 1736 | 2280 | 2856 | 3496 | 4008 | 4584 | 5160 | 5736 |
| 24 | 584 | 1192 | 1800 | 2408 | 2984 | 3624 | 4264 | 4968 | 5544 | 5992 |
| 25 | 616 | 1256 | 1864 | 2536 | 3112 | 3752 | 4392 | 5160 | 5736 | 6200 |
| 26 | 712 | 1480 | 2216 | 2984 | 3752 | 4392 | 5160 | 5992 | 6712 | 7480 |
| 26A | 632 | 1288 | 1928 | 2600 | 3240 | 3880 | 4584 | 5160 | 5992 | 6456 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| 0 | 288 | 328 | 344 | 376 | 392 | 424 | 456 | 488 | 504 | 536 |
| 1 | 376 | 424 | 456 | 488 | 520 | 568 | 600 | 632 | 680 | 712 |
| 2 | 472 | 520 | 568 | 616 | 648 | 696 | 744 | 776 | 840 | 872 |
| 3 | 616 | 680 | 744 | 808 | 872 | 904 | 968 | 1032 | 1096 | 1160 |
| 4 | 776 | 840 | 904 | 1000 | 1064 | 1128 | 1192 | 1288 | 1352 | 1416 |
| 5 | 968 | 1032 | 1128 | 1224 | 1320 | 1384 | 1480 | 1544 | 1672 | 1736 |
| 6 | 1128 | 1224 | 1352 | 1480 | 1544 | 1672 | 1736 | 1864 | 1992 | 2088 |
| 7 | 1320 | 1480 | 1608 | 1672 | 1800 | 1928 | 2088 | 2216 | 2344 | 2472 |
| 8 | 1544 | 1672 | 1800 | 1928 | 2088 | 2216 | 2344 | 2536 | 2664 | 2792 |
| 9 | 1736 | 1864 | 2024 | 2216 | 2344 | 2536 | 2664 | 2856 | 2984 | 3112 |
| 10 | 1928 | 2088 | 2280 | 2472 | 2664 | 2792 | 2984 | 3112 | 3368 | 3496 |
| 11 | 2216 | 2408 | 2600 | 2792 | 2984 | 3240 | 3496 | 3624 | 3880 | 4008 |
| 12 | 2472 | 2728 | 2984 | 3240 | 3368 | 3624 | 3880 | 4136 | 4392 | 4584 |
| 13 | 2856 | 3112 | 3368 | 3624 | 3880 | 4136 | 4392 | 4584 | 4968 | 5160 |
| 14 | 3112 | 3496 | 3752 | 4008 | 4264 | 4584 | 4968 | 5160 | 5544 | 5736 |
| 15 | 3368 | 3624 | 4008 | 4264 | 4584 | 4968 | 5160 | 5544 | 5736 | 6200 |
| 16 | 3624 | 3880 | 4264 | 4584 | 4968 | 5160 | 5544 | 5992 | 6200 | 6456 |
| 17 | 4008 | 4392 | 4776 | 5160 | 5352 | 5736 | 6200 | 6456 | 6712 | 7224 |
| 18 | 4392 | 4776 | 5160 | 5544 | 5992 | 6200 | 6712 | 7224 | 7480 | 7992 |
| 19 | 4776 | 5160 | 5544 | 5992 | 6456 | 6968 | 7224 | 7736 | 8248 | 8504 |
| 20 | 5160 | 5544 | 5992 | 6456 | 6968 | 7480 | 7992 | 8248 | 8760 | 9144 |
| 21 | 5544 | 5992 | 6456 | 6968 | 7480 | 7992 | 8504 | 9144 | 9528 | 9912 |
| 22 | 5992 | 6456 | 6968 | 7480 | 7992 | 8504 | 9144 | 9528 | 10296 | 10680 |
| 23 | 6200 | 6968 | 7480 | 7992 | 8504 | 9144 | 9912 | 10296 | 11064 | 11448 |
| 24 | 6712 | 7224 | 7992 | 8504 | 9144 | 9912 | 10296 | 11064 | 11448 | 12216 |
| 25 | 6968 | 7480 | 8248 | 8760 | 9528 | 10296 | 10680 | 11448 | 12216 | 12576 |
| 26 | 8248 | 8760 | 9528 | 10296 | 11064 | 11832 | 12576 | 13536 | 14112 | 14688 |
| 26A | 7224 | 7736 | 8504 | 9144 | 9912 | 10296 | 11064 | 11832 | 12576 | 12960 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
| 0 | 568 | 600 | 616 | 648 | 680 | 712 | 744 | 776 | 776 | 808 |
| 1 | 744 | 776 | 808 | 872 | 904 | 936 | 968 | 1000 | 1032 | 1064 |
| 2 | 936 | 968 | 1000 | 1064 | 1096 | 1160 | 1192 | 1256 | 1288 | 1320 |
| 3 | 1224 | 1256 | 1320 | 1384 | 1416 | 1480 | 1544 | 1608 | 1672 | 1736 |
| 4 | 1480 | 1544 | 1608 | 1736 | 1800 | 1864 | 1928 | 1992 | 2088 | 2152 |
| 5 | 1864 | 1928 | 2024 | 2088 | 2216 | 2280 | 2344 | 2472 | 2536 | 2664 |
| 6 | 2216 | 2280 | 2408 | 2472 | 2600 | 2728 | 2792 | 2984 | 2984 | 3112 |
| 7 | 2536 | 2664 | 2792 | 2984 | 3112 | 3240 | 3368 | 3368 | 3496 | 3624 |
| 8 | 2984 | 3112 | 3240 | 3368 | 3496 | 3624 | 3752 | 3880 | 4008 | 4264 |
| 9 | 3368 | 3496 | 3624 | 3752 | 4008 | 4136 | 4264 | 4392 | 4584 | 4776 |
| 10 | 3752 | 3880 | 4008 | 4264 | 4392 | 4584 | 4776 | 4968 | 5160 | 5352 |
| 11 | 4264 | 4392 | 4584 | 4776 | 4968 | 5352 | 5544 | 5736 | 5992 | 5992 |
| 12 | 4776 | 4968 | 5352 | 5544 | 5736 | 5992 | 6200 | 6456 | 6712 | 6712 |
| 13 | 5352 | 5736 | 5992 | 6200 | 6456 | 6712 | 6968 | 7224 | 7480 | 7736 |
| 14 | 5992 | 6200 | 6456 | 6968 | 7224 | 7480 | 7736 | 7992 | 8248 | 8504 |
| 15 | 6456 | 6712 | 6968 | 7224 | 7736 | 7992 | 8248 | 8504 | 8760 | 9144 |
| 16 | 6712 | 7224 | 7480 | 7736 | 7992 | 8504 | 8760 | 9144 | 9528 | 9912 |
| 17 | 7480 | 7992 | 8248 | 8760 | 9144 | 9528 | 9912 | 10296 | 10296 | 10680 |
| 18 | 8248 | 8760 | 9144 | 9528 | 9912 | 10296 | 10680 | 11064 | 11448 | 11832 |
| 19 | 9144 | 9528 | 9912 | 10296 | 10680 | 11064 | 11448 | 12216 | 12576 | 12960 |
| 20 | 9912 | 10296 | 10680 | 11064 | 11448 | 12216 | 12576 | 12960 | 13536 | 14112 |
| 21 | 10680 | 11064 | 11448 | 12216 | 12576 | 12960 | 13536 | 14112 | 14688 | 15264 |
| 22 | 11448 | 11832 | 12576 | 12960 | 13536 | 14112 | 14688 | 15264 | 15840 | 16416 |
| 23 | 12216 | 12576 | 12960 | 13536 | 14112 | 14688 | 15264 | 15840 | 16416 | 16992 |
| 24 | 12960 | 13536 | 14112 | 14688 | 15264 | 15840 | 16416 | 16992 | 17568 | 18336 |
| 25 | 13536 | 14112 | 14688 | 15264 | 15840 | 16416 | 16992 | 17568 | 18336 | 19080 |
| 26 | 15264 | 16416 | 16992 | 17568 | 18336 | 19080 | 19848 | 20616 | 21384 | 22152 |
| 26A | 13536 | 14112 | 15264 | 15840 | 16416 | 16992 | 17568 | 18336 | 19080 | 19848 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
| 0 | 840 | 872 | 904 | 936 | 968 | 1000 | 1032 | 1032 | 1064 | 1096 |
| 1 | 1128 | 1160 | 1192 | 1224 | 1256 | 1288 | 1352 | 1384 | 1416 | 1416 |
| 2 | 1384 | 1416 | 1480 | 1544 | 1544 | 1608 | 1672 | 1672 | 1736 | 1800 |
| 3 | 1800 | 1864 | 1928 | 1992 | 2024 | 2088 | 2152 | 2216 | 2280 | 2344 |
| 4 | 2216 | 2280 | 2344 | 2408 | 2472 | 2600 | 2664 | 2728 | 2792 | 2856 |
| 5 | 2728 | 2792 | 2856 | 2984 | 3112 | 3112 | 3240 | 3368 | 3496 | 3496 |
| 6 | 3240 | 3368 | 3496 | 3496 | 3624 | 3752 | 3880 | 4008 | 4136 | 4136 |
| 7 | 3752 | 3880 | 4008 | 4136 | 4264 | 4392 | 4584 | 4584 | 4776 | 4968 |
| 8 | 4392 | 4584 | 4584 | 4776 | 4968 | 4968 | 5160 | 5352 | 5544 | 5544 |
| 9 | 4968 | 5160 | 5160 | 5352 | 5544 | 5736 | 5736 | 5992 | 6200 | 6200 |
| 10 | 5544 | 5736 | 5736 | 5992 | 6200 | 6200 | 6456 | 6712 | 6712 | 6968 |
| 11 | 6200 | 6456 | 6712 | 6968 | 6968 | 7224 | 7480 | 7736 | 7736 | 7992 |
| 12 | 6968 | 7224 | 7480 | 7736 | 7992 | 8248 | 8504 | 8760 | 8760 | 9144 |
| 13 | 7992 | 8248 | 8504 | 8760 | 9144 | 9144 | 9528 | 9912 | 9912 | 10296 |
| 14 | 8760 | 9144 | 9528 | 9912 | 9912 | 10296 | 10680 | 11064 | 11064 | 11448 |
| 15 | 9528 | 9912 | 10296 | 10296 | 10680 | 11064 | 11448 | 11832 | 11832 | 12216 |
| 16 | 9912 | 10296 | 10680 | 11064 | 11448 | 11832 | 12216 | 12216 | 12576 | 12960 |
| 17 | 11064 | 11448 | 11832 | 12216 | 12576 | 12960 | 13536 | 13536 | 14112 | 14688 |
| 18 | 12216 | 12576 | 12960 | 13536 | 14112 | 14112 | 14688 | 15264 | 15264 | 15840 |
| 19 | 13536 | 13536 | 14112 | 14688 | 15264 | 15264 | 15840 | 16416 | 16992 | 16992 |
| 20 | 14688 | 14688 | 15264 | 15840 | 16416 | 16992 | 16992 | 17568 | 18336 | 18336 |
| 21 | 15840 | 15840 | 16416 | 16992 | 17568 | 18336 | 18336 | 19080 | 19848 | 19848 |
| 22 | 16992 | 16992 | 17568 | 18336 | 19080 | 19080 | 19848 | 20616 | 21384 | 21384 |
| 23 | 17568 | 18336 | 19080 | 19848 | 19848 | 20616 | 21384 | 22152 | 22152 | 22920 |
| 24 | 19080 | 19848 | 19848 | 20616 | 21384 | 22152 | 22920 | 22920 | 23688 | 24496 |
| 25 | 19848 | 20616 | 20616 | 21384 | 22152 | 22920 | 23688 | 24496 | 24496 | 25456 |
| 26 | 22920 | 23688 | 24496 | 25456 | 25456 | 26416 | 27376 | 28336 | 29296 | 29296 |
| 26A | 20616 | 20616 | 21384 | 22152 | 22920 | 23688 | 24496 | 24496 | 25456 | 26416 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
| 0 | 1128 | 1160 | 1192 | 1224 | 1256 | 1256 | 1288 | 1320 | 1352 | 1384 |
| 1 | 1480 | 1544 | 1544 | 1608 | 1608 | 1672 | 1736 | 1736 | 1800 | 1800 |
| 2 | 1800 | 1864 | 1928 | 1992 | 2024 | 2088 | 2088 | 2152 | 2216 | 2216 |
| 3 | 2408 | 2472 | 2536 | 2536 | 2600 | 2664 | 2728 | 2792 | 2856 | 2856 |
| 4 | 2984 | 2984 | 3112 | 3112 | 3240 | 3240 | 3368 | 3496 | 3496 | 3624 |
| 5 | 3624 | 3752 | 3752 | 3880 | 4008 | 4008 | 4136 | 4264 | 4392 | 4392 |
| 6 | 4264 | 4392 | 4584 | 4584 | 4776 | 4776 | 4968 | 4968 | 5160 | 5160 |
| 7 | 4968 | 5160 | 5352 | 5352 | 5544 | 5736 | 5736 | 5992 | 5992 | 6200 |
| 8 | 5736 | 5992 | 5992 | 6200 | 6200 | 6456 | 6456 | 6712 | 6968 | 6968 |
| 9 | 6456 | 6712 | 6712 | 6968 | 6968 | 7224 | 7480 | 7480 | 7736 | 7992 |
| 10 | 7224 | 7480 | 7480 | 7736 | 7992 | 7992 | 8248 | 8504 | 8504 | 8760 |
| 11 | 8248 | 8504 | 8760 | 8760 | 9144 | 9144 | 9528 | 9528 | 9912 | 9912 |
| 12 | 9528 | 9528 | 9912 | 9912 | 10296 | 10680 | 10680 | 11064 | 11064 | 11448 |
| 13 | 10680 | 10680 | 11064 | 11448 | 11448 | 11832 | 12216 | 12216 | 12576 | 12960 |
| 14 | 11832 | 12216 | 12216 | 12576 | 12960 | 12960 | 13536 | 13536 | 14112 | 14112 |
| 15 | 12576 | 12960 | 12960 | 13536 | 13536 | 14112 | 14688 | 14688 | 15264 | 15264 |
| 16 | 13536 | 13536 | 14112 | 14112 | 14688 | 14688 | 15264 | 15840 | 15840 | 16416 |
| 17 | 14688 | 15264 | 15264 | 15840 | 16416 | 16416 | 16992 | 17568 | 17568 | 18336 |
| 18 | 16416 | 16416 | 16992 | 17568 | 17568 | 18336 | 18336 | 19080 | 19080 | 19848 |
| 19 | 17568 | 18336 | 18336 | 19080 | 19080 | 19848 | 20616 | 20616 | 21384 | 21384 |
| 20 | 19080 | 19848 | 19848 | 20616 | 20616 | 21384 | 22152 | 22152 | 22920 | 22920 |
| 21 | 20616 | 21384 | 21384 | 22152 | 22920 | 22920 | 23688 | 24496 | 24496 | 25456 |
| 22 | 22152 | 22920 | 22920 | 23688 | 24496 | 24496 | 25456 | 25456 | 26416 | 27376 |
| 23 | 23688 | 24496 | 24496 | 25456 | 25456 | 26416 | 27376 | 27376 | 28336 | 28336 |
| 24 | 25456 | 25456 | 26416 | 26416 | 27376 | 28336 | 28336 | 29296 | 29296 | 30576 |
| 25 | 26416 | 26416 | 27376 | 28336 | 28336 | 29296 | 29296 | 30576 | 31704 | 31704 |
| 26 | 30576 | 30576 | 31704 | 32856 | 32856 | 34008 | 35160 | 35160 | 36696 | 36696 |
| 26A | 26416 | 27376 | 27376 | 29296 | 29296 | 29296 | 30576 | 30576 | 31704 | 32856 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 |
| 0 | 1416 | 1416 | 1480 | 1480 | 1544 | 1544 | 1608 | 1608 | 1608 | 1672 |
| 1 | 1864 | 1864 | 1928 | 1992 | 1992 | 2024 | 2088 | 2088 | 2152 | 2152 |
| 2 | 2280 | 2344 | 2344 | 2408 | 2472 | 2536 | 2536 | 2600 | 2664 | 2664 |
| 3 | 2984 | 2984 | 3112 | 3112 | 3240 | 3240 | 3368 | 3368 | 3496 | 3496 |
| 4 | 3624 | 3752 | 3752 | 3880 | 4008 | 4008 | 4136 | 4136 | 4264 | 4264 |
| 5 | 4584 | 4584 | 4776 | 4776 | 4776 | 4968 | 4968 | 5160 | 5160 | 5352 |
| 6 | 5352 | 5352 | 5544 | 5736 | 5736 | 5992 | 5992 | 5992 | 6200 | 6200 |
| 7 | 6200 | 6456 | 6456 | 6712 | 6712 | 6712 | 6968 | 6968 | 7224 | 7224 |
| 8 | 7224 | 7224 | 7480 | 7480 | 7736 | 7736 | 7992 | 7992 | 8248 | 8504 |
| 9 | 7992 | 8248 | 8248 | 8504 | 8760 | 8760 | 9144 | 9144 | 9144 | 9528 |
| 10 | 9144 | 9144 | 9144 | 9528 | 9528 | 9912 | 9912 | 10296 | 10296 | 10680 |
| 11 | 10296 | 10680 | 10680 | 11064 | 11064 | 11448 | 11448 | 11832 | 11832 | 12216 |
| 12 | 11832 | 11832 | 12216 | 12216 | 12576 | 12576 | 12960 | 12960 | 13536 | 13536 |
| 13 | 12960 | 13536 | 13536 | 14112 | 14112 | 14688 | 14688 | 14688 | 15264 | 15264 |
| 14 | 14688 | 14688 | 15264 | 15264 | 15840 | 15840 | 16416 | 16416 | 16992 | 16992 |
| 15 | 15840 | 15840 | 16416 | 16416 | 16992 | 16992 | 17568 | 17568 | 18336 | 18336 |
| 16 | 16416 | 16992 | 16992 | 17568 | 17568 | 18336 | 18336 | 19080 | 19080 | 19848 |
| 17 | 18336 | 19080 | 19080 | 19848 | 19848 | 20616 | 20616 | 20616 | 21384 | 21384 |
| 18 | 19848 | 20616 | 21384 | 21384 | 22152 | 22152 | 22920 | 22920 | 23688 | 23688 |
| 19 | 22152 | 22152 | 22920 | 22920 | 23688 | 24496 | 24496 | 25456 | 25456 | 25456 |
| 20 | 23688 | 24496 | 24496 | 25456 | 25456 | 26416 | 26416 | 27376 | 27376 | 28336 |
| 21 | 25456 | 26416 | 26416 | 27376 | 27376 | 28336 | 28336 | 29296 | 29296 | 30576 |
| 22 | 27376 | 28336 | 28336 | 29296 | 29296 | 30576 | 30576 | 31704 | 31704 | 32856 |
| 23 | 29296 | 29296 | 30576 | 30576 | 31704 | 31704 | 32856 | 32856 | 34008 | 34008 |
| 24 | 31704 | 31704 | 32856 | 32856 | 34008 | 34008 | 35160 | 35160 | 36696 | 36696 |
| 25 | 32856 | 32856 | 34008 | 34008 | 35160 | 35160 | 36696 | 36696 | 37888 | 37888 |
| 26 | 37888 | 37888 | 39232 | 40576 | 40576 | 40576 | 42368 | 42368 | 43816 | 43816 |
| 26A | 32856 | 34008 | 34008 | 35160 | 36696 | 36696 | 36696 | 37888 | 37888 | 39232 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 |
| 0 | 1672 | 1736 | 1736 | 1800 | 1800 | 1800 | 1864 | 1864 | 1928 | 1928 |
| 1 | 2216 | 2280 | 2280 | 2344 | 2344 | 2408 | 2472 | 2472 | 2536 | 2536 |
| 2 | 2728 | 2792 | 2856 | 2856 | 2856 | 2984 | 2984 | 3112 | 3112 | 3112 |
| 3 | 3624 | 3624 | 3624 | 3752 | 3752 | 3880 | 3880 | 4008 | 4008 | 4136 |
| 4 | 4392 | 4392 | 4584 | 4584 | 4584 | 4776 | 4776 | 4968 | 4968 | 4968 |
| 5 | 5352 | 5544 | 5544 | 5736 | 5736 | 5736 | 5992 | 5992 | 5992 | 6200 |
| 6 | 6456 | 6456 | 6456 | 6712 | 6712 | 6968 | 6968 | 6968 | 7224 | 7224 |
| 7 | 7480 | 7480 | 7736 | 7736 | 7992 | 7992 | 8248 | 8248 | 8504 | 8504 |
| 8 | 8504 | 8760 | 8760 | 9144 | 9144 | 9144 | 9528 | 9528 | 9528 | 9912 |
| 9 | 9528 | 9912 | 9912 | 10296 | 10296 | 10296 | 10680 | 10680 | 11064 | 11064 |
| 10 | 10680 | 11064 | 11064 | 11448 | 11448 | 11448 | 11832 | 11832 | 12216 | 12216 |
| 11 | 12216 | 12576 | 12576 | 12960 | 12960 | 13536 | 13536 | 13536 | 14112 | 14112 |
| 12 | 14112 | 14112 | 14112 | 14688 | 14688 | 15264 | 15264 | 15264 | 15840 | 15840 |
| 13 | 15840 | 15840 | 16416 | 16416 | 16992 | 16992 | 16992 | 17568 | 17568 | 18336 |
| 14 | 17568 | 17568 | 18336 | 18336 | 18336 | 19080 | 19080 | 19848 | 19848 | 19848 |
| 15 | 18336 | 19080 | 19080 | 19848 | 19848 | 20616 | 20616 | 20616 | 21384 | 21384 |
| 16 | 19848 | 19848 | 20616 | 20616 | 21384 | 21384 | 22152 | 22152 | 22152 | 22920 |
| 17 | 22152 | 22152 | 22920 | 22920 | 23688 | 23688 | 24496 | 24496 | 24496 | 25456 |
| 18 | 24496 | 24496 | 24496 | 25456 | 25456 | 26416 | 26416 | 27376 | 27376 | 27376 |
| 19 | 26416 | 26416 | 27376 | 27376 | 28336 | 28336 | 29296 | 29296 | 29296 | 30576 |
| 20 | 28336 | 29296 | 29296 | 29296 | 30576 | 30576 | 31704 | 31704 | 31704 | 32856 |
| 21 | 30576 | 31704 | 31704 | 31704 | 32856 | 32856 | 34008 | 34008 | 35160 | 35160 |
| 22 | 32856 | 34008 | 34008 | 34008 | 35160 | 35160 | 36696 | 36696 | 36696 | 37888 |
| 23 | 35160 | 35160 | 36696 | 36696 | 37888 | 37888 | 37888 | 39232 | 39232 | 40576 |
| 24 | 36696 | 37888 | 37888 | 39232 | 39232 | 40576 | 40576 | 42368 | 42368 | 42368 |
| 25 | 39232 | 39232 | 40576 | 40576 | 40576 | 42368 | 42368 | 43816 | 43816 | 43816 |
| 26 | 45352 | 45352 | 46888 | 46888 | 48936 | 48936 | 48936 | 51024 | 51024 | 52752 |
| 26A | 40576 | 40576 | 40576 | 40576 | 42368 | 42368 | 43816 | 43816 | 45352 | 45352 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 |
| 0 | 1992 | 1992 | 2024 | 2088 | 2088 | 2088 | 2152 | 2152 | 2216 | 2216 |
| 1 | 2600 | 2600 | 2664 | 2728 | 2728 | 2792 | 2792 | 2856 | 2856 | 2856 |
| 2 | 3240 | 3240 | 3240 | 3368 | 3368 | 3368 | 3496 | 3496 | 3496 | 3624 |
| 3 | 4136 | 4264 | 4264 | 4392 | 4392 | 4392 | 4584 | 4584 | 4584 | 4776 |
| 4 | 5160 | 5160 | 5160 | 5352 | 5352 | 5544 | 5544 | 5544 | 5736 | 5736 |
| 5 | 6200 | 6200 | 6456 | 6456 | 6712 | 6712 | 6712 | 6968 | 6968 | 6968 |
| 6 | 7480 | 7480 | 7736 | 7736 | 7736 | 7992 | 7992 | 8248 | 8248 | 8248 |
| 7 | 8760 | 8760 | 8760 | 9144 | 9144 | 9144 | 9528 | 9528 | 9528 | 9912 |
| 8 | 9912 | 9912 | 10296 | 10296 | 10680 | 10680 | 10680 | 11064 | 11064 | 11064 |
| 9 | 11064 | 11448 | 11448 | 11832 | 11832 | 11832 | 12216 | 12216 | 12576 | 12576 |
| 10 | 12576 | 12576 | 12960 | 12960 | 12960 | 13536 | 13536 | 13536 | 14112 | 14112 |
| 11 | 14112 | 14688 | 14688 | 14688 | 15264 | 15264 | 15840 | 15840 | 15840 | 16416 |
| 12 | 16416 | 16416 | 16416 | 16992 | 16992 | 17568 | 17568 | 17568 | 18336 | 18336 |
| 13 | 18336 | 18336 | 19080 | 19080 | 19080 | 19848 | 19848 | 19848 | 20616 | 20616 |
| 14 | 20616 | 20616 | 20616 | 21384 | 21384 | 22152 | 22152 | 22152 | 22920 | 22920 |
| 15 | 22152 | 22152 | 22152 | 22920 | 22920 | 23688 | 23688 | 23688 | 24496 | 24496 |
| 16 | 22920 | 23688 | 23688 | 24496 | 24496 | 24496 | 25456 | 25456 | 25456 | 26416 |
| 17 | 25456 | 26416 | 26416 | 26416 | 27376 | 27376 | 27376 | 28336 | 28336 | 29296 |
| 18 | 28336 | 28336 | 29296 | 29296 | 29296 | 30576 | 30576 | 30576 | 31704 | 31704 |
| 19 | 30576 | 30576 | 31704 | 31704 | 32856 | 32856 | 32856 | 34008 | 34008 | 34008 |
| 20 | 32856 | 34008 | 34008 | 34008 | 35160 | 35160 | 35160 | 36696 | 36696 | 36696 |
| 21 | 35160 | 36696 | 36696 | 36696 | 37888 | 37888 | 39232 | 39232 | 39232 | 40576 |
| 22 | 37888 | 39232 | 39232 | 40576 | 40576 | 40576 | 42368 | 42368 | 42368 | 43816 |
| 23 | 40576 | 40576 | 42368 | 42368 | 43816 | 43816 | 43816 | 45352 | 45352 | 45352 |
| 24 | 43816 | 43816 | 45352 | 45352 | 45352 | 46888 | 46888 | 46888 | 48936 | 48936 |
| 25 | 45352 | 45352 | 46888 | 46888 | 46888 | 48936 | 48936 | 48936 | 51024 | 51024 |
| 26 | 52752 | 52752 | 55056 | 55056 | 55056 | 55056 | 57336 | 57336 | 57336 | 59256 |
| 26A | 45352 | 46888 | 46888 | 48936 | 48936 | 48936 | 51024 | 51024 | 51024 | 52752 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 |
| 0 | 2280 | 2280 | 2280 | 2344 | 2344 | 2408 | 2408 | 2472 | 2472 | 2536 |
| 1 | 2984 | 2984 | 2984 | 3112 | 3112 | 3112 | 3240 | 3240 | 3240 | 3240 |
| 2 | 3624 | 3624 | 3752 | 3752 | 3880 | 3880 | 3880 | 4008 | 4008 | 4008 |
| 3 | 4776 | 4776 | 4776 | 4968 | 4968 | 4968 | 5160 | 5160 | 5160 | 5352 |
| 4 | 5736 | 5992 | 5992 | 5992 | 5992 | 6200 | 6200 | 6200 | 6456 | 6456 |
| 5 | 7224 | 7224 | 7224 | 7480 | 7480 | 7480 | 7736 | 7736 | 7736 | 7992 |
| 6 | 8504 | 8504 | 8760 | 8760 | 8760 | 9144 | 9144 | 9144 | 9144 | 9528 |
| 7 | 9912 | 9912 | 10296 | 10296 | 10296 | 10680 | 10680 | 10680 | 11064 | 11064 |
| 8 | 11448 | 11448 | 11448 | 11832 | 11832 | 12216 | 12216 | 12216 | 12576 | 12576 |
| 9 | 12960 | 12960 | 12960 | 13536 | 13536 | 13536 | 13536 | 14112 | 14112 | 14112 |
| 10 | 14112 | 14688 | 14688 | 14688 | 14688 | 15264 | 15264 | 15264 | 15840 | 15840 |
| 11 | 16416 | 16416 | 16992 | 16992 | 16992 | 17568 | 17568 | 17568 | 18336 | 18336 |
| 12 | 18336 | 19080 | 19080 | 19080 | 19080 | 19848 | 19848 | 19848 | 20616 | 20616 |
| 13 | 20616 | 21384 | 21384 | 21384 | 22152 | 22152 | 22152 | 22920 | 22920 | 22920 |
| 14 | 22920 | 23688 | 23688 | 24496 | 24496 | 24496 | 25456 | 25456 | 25456 | 25456 |
| 15 | 24496 | 25456 | 25456 | 25456 | 26416 | 26416 | 26416 | 27376 | 27376 | 27376 |
| 16 | 26416 | 26416 | 27376 | 27376 | 27376 | 28336 | 28336 | 28336 | 29296 | 29296 |
| 17 | 29296 | 29296 | 30576 | 30576 | 30576 | 30576 | 31704 | 31704 | 31704 | 32856 |
| 18 | 31704 | 32856 | 32856 | 32856 | 34008 | 34008 | 34008 | 35160 | 35160 | 35160 |
| 19 | 35160 | 35160 | 35160 | 36696 | 36696 | 36696 | 37888 | 37888 | 37888 | 39232 |
| 20 | 37888 | 37888 | 39232 | 39232 | 39232 | 40576 | 40576 | 40576 | 42368 | 42368 |
| 21 | 40576 | 40576 | 42368 | 42368 | 42368 | 43816 | 43816 | 43816 | 45352 | 45352 |
| 22 | 43816 | 43816 | 45352 | 45352 | 45352 | 46888 | 46888 | 46888 | 48936 | 48936 |
| 23 | 46888 | 46888 | 46888 | 48936 | 48936 | 48936 | 51024 | 51024 | 51024 | 51024 |
| 24 | 48936 | 51024 | 51024 | 51024 | 52752 | 52752 | 52752 | 52752 | 55056 | 55056 |
| 25 | 51024 | 52752 | 52752 | 52752 | 55056 | 55056 | 55056 | 55056 | 57336 | 57336 |
| 26 | 59256 | 59256 | 61664 | 61664 | 61664 | 63776 | 63776 | 63776 | 66592 | 66592 |
| 26A | 52752 | 52752 | 55056 | 55056 | 55056 | 55056 | 57336 | 57336 | 57336 | 59256 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100 |
| 0 | 2536 | 2536 | 2600 | 2600 | 2664 | 2664 | 2728 | 2728 | 2728 | 2792 |
| 1 | 3368 | 3368 | 3368 | 3496 | 3496 | 3496 | 3496 | 3624 | 3624 | 3624 |
| 2 | 4136 | 4136 | 4136 | 4264 | 4264 | 4264 | 4392 | 4392 | 4392 | 4584 |
| 3 | 5352 | 5352 | 5352 | 5544 | 5544 | 5544 | 5736 | 5736 | 5736 | 5736 |
| 4 | 6456 | 6456 | 6712 | 6712 | 6712 | 6968 | 6968 | 6968 | 6968 | 7224 |
| 5 | 7992 | 7992 | 8248 | 8248 | 8248 | 8504 | 8504 | 8760 | 8760 | 8760 |
| 6 | 9528 | 9528 | 9528 | 9912 | 9912 | 9912 | 10296 | 10296 | 10296 | 10296 |
| 7 | 11064 | 11448 | 11448 | 11448 | 11448 | 11832 | 11832 | 11832 | 12216 | 12216 |
| 8 | 12576 | 12960 | 12960 | 12960 | 13536 | 13536 | 13536 | 13536 | 14112 | 14112 |
| 9 | 14112 | 14688 | 14688 | 14688 | 15264 | 15264 | 15264 | 15264 | 15840 | 15840 |
| 10 | 15840 | 16416 | 16416 | 16416 | 16992 | 16992 | 16992 | 16992 | 17568 | 17568 |
| 11 | 18336 | 18336 | 19080 | 19080 | 19080 | 19080 | 19848 | 19848 | 19848 | 19848 |
| 12 | 20616 | 21384 | 21384 | 21384 | 21384 | 22152 | 22152 | 22152 | 22920 | 22920 |
| 13 | 23688 | 23688 | 23688 | 24496 | 24496 | 24496 | 25456 | 25456 | 25456 | 25456 |
| 14 | 26416 | 26416 | 26416 | 27376 | 27376 | 27376 | 28336 | 28336 | 28336 | 28336 |
| 15 | 28336 | 28336 | 28336 | 29296 | 29296 | 29296 | 29296 | 30576 | 30576 | 30576 |
| 16 | 29296 | 30576 | 30576 | 30576 | 30576 | 31704 | 31704 | 31704 | 31704 | 32856 |
| 17 | 32856 | 32856 | 34008 | 34008 | 34008 | 35160 | 35160 | 35160 | 35160 | 36696 |
| 18 | 36696 | 36696 | 36696 | 37888 | 37888 | 37888 | 37888 | 39232 | 39232 | 39232 |
| 19 | 39232 | 39232 | 40576 | 40576 | 40576 | 40576 | 42368 | 42368 | 42368 | 43816 |
| 20 | 42368 | 42368 | 43816 | 43816 | 43816 | 45352 | 45352 | 45352 | 46888 | 46888 |
| 21 | 45352 | 46888 | 46888 | 46888 | 46888 | 48936 | 48936 | 48936 | 48936 | 51024 |
| 22 | 48936 | 48936 | 51024 | 51024 | 51024 | 51024 | 52752 | 52752 | 52752 | 55056 |
| 23 | 52752 | 52752 | 52752 | 55056 | 55056 | 55056 | 55056 | 57336 | 57336 | 57336 |
| 24 | 55056 | 57336 | 57336 | 57336 | 57336 | 59256 | 59256 | 59256 | 61664 | 61664 |
| 25 | 57336 | 59256 | 59256 | 59256 | 61664 | 61664 | 61664 | 61664 | 63776 | 63776 |
| 26 | 66592 | 68808 | 68808 | 68808 | 71112 | 71112 | 71112 | 73712 | 73712 | 75376 |
| 26A | 59256 | 59256 | 59256 | 61664 | 61664 | 61664 | 63776 | 63776 | 63776 | 66592 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 101 | 102 | 103 | 104 | 105 | 106 | 107 | 108 | 109 | 110 |
| 0 | 2792 | 2856 | 2856 | 2856 | 2984 | 2984 | 2984 | 2984 | 2984 | 3112 |
| 1 | 3752 | 3752 | 3752 | 3752 | 3880 | 3880 | 3880 | 4008 | 4008 | 4008 |
| 2 | 4584 | 4584 | 4584 | 4584 | 4776 | 4776 | 4776 | 4776 | 4968 | 4968 |
| 3 | 5992 | 5992 | 5992 | 5992 | 6200 | 6200 | 6200 | 6200 | 6456 | 6456 |
| 4 | 7224 | 7224 | 7480 | 7480 | 7480 | 7480 | 7736 | 7736 | 7736 | 7992 |
| 5 | 8760 | 9144 | 9144 | 9144 | 9144 | 9528 | 9528 | 9528 | 9528 | 9528 |
| 6 | 10680 | 10680 | 10680 | 10680 | 11064 | 11064 | 11064 | 11448 | 11448 | 11448 |
| 7 | 12216 | 12576 | 12576 | 12576 | 12960 | 12960 | 12960 | 12960 | 13536 | 13536 |
| 8 | 14112 | 14112 | 14688 | 14688 | 14688 | 14688 | 15264 | 15264 | 15264 | 15264 |
| 9 | 15840 | 16416 | 16416 | 16416 | 16416 | 16992 | 16992 | 16992 | 16992 | 17568 |
| 10 | 17568 | 18336 | 18336 | 18336 | 18336 | 18336 | 19080 | 19080 | 19080 | 19080 |
| 11 | 20616 | 20616 | 20616 | 21384 | 21384 | 21384 | 21384 | 22152 | 22152 | 22152 |
| 12 | 22920 | 23688 | 23688 | 23688 | 23688 | 24496 | 24496 | 24496 | 24496 | 25456 |
| 13 | 26416 | 26416 | 26416 | 26416 | 27376 | 27376 | 27376 | 27376 | 28336 | 28336 |
| 14 | 29296 | 29296 | 29296 | 29296 | 30576 | 30576 | 30576 | 30576 | 31704 | 31704 |
| 15 | 30576 | 31704 | 31704 | 31704 | 31704 | 32856 | 32856 | 32856 | 34008 | 34008 |
| 16 | 32856 | 32856 | 34008 | 34008 | 34008 | 34008 | 35160 | 35160 | 35160 | 35160 |
| 17 | 36696 | 36696 | 36696 | 37888 | 37888 | 37888 | 39232 | 39232 | 39232 | 39232 |
| 18 | 40576 | 40576 | 40576 | 40576 | 42368 | 42368 | 42368 | 42368 | 43816 | 43816 |
| 19 | 43816 | 43816 | 43816 | 45352 | 45352 | 45352 | 46888 | 46888 | 46888 | 46888 |
| 20 | 46888 | 46888 | 48936 | 48936 | 48936 | 48936 | 48936 | 51024 | 51024 | 51024 |
| 21 | 51024 | 51024 | 51024 | 52752 | 52752 | 52752 | 52752 | 55056 | 55056 | 55056 |
| 22 | 55056 | 55056 | 55056 | 57336 | 57336 | 57336 | 57336 | 59256 | 59256 | 59256 |
| 23 | 57336 | 59256 | 59256 | 59256 | 59256 | 61664 | 61664 | 61664 | 61664 | 63776 |
| 24 | 61664 | 61664 | 63776 | 63776 | 63776 | 63776 | 66592 | 66592 | 66592 | 66592 |
| 25 | 63776 | 63776 | 66592 | 66592 | 66592 | 66592 | 68808 | 68808 | 68808 | 71112 |
| 26 | 75376 | 75376 | 75376 | 75376 | 75376 | 75376 | 75376 | 75376 | 75376 | 75376 |
| 26A | 66592 | 66592 | 66592 | 68808 | 68808 | 68808 | 71112 | 71112 | 71112 | 71112 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| 27 | 648 | 1320 | 1992 | 2664 | 3368 | 4008 | 4584 | 5352 | 5992 | 6712 |
| 28 | 680 | 1384 | 2088 | 2792 | 3496 | 4264 | 4968 | 5544 | 6200 | 6968 |
| 29 | 712 | 1480 | 2216 | 2984 | 3752 | 4392 | 5160 | 5992 | 6712 | 7480 |
| 30 | 776 | 1544 | 2344 | 3112 | 3880 | 4776 | 5544 | 6200 | 6968 | 7736 |
| 31 | 808 | 1608 | 2472 | 3240 | 4136 | 4968 | 5736 | 6456 | 7480 | 8248 |
| 32 | 840 | 1672 | 2536 | 3368 | 4264 | 5160 | 5992 | 6712 | 7736 | 8504 |
| 32A | 904 | 1864 | 2792 | 3752 | 4584 | 5544 | 6456 | 7480 | 8248 | 9144 |
| 33 | 968 | 1992 | 2984 | 4008 | 4968 | 5992 | 6968 | 7992 | 8760 | 9912 |
| 33A | 840 | 1736 | 2600 | 3496 | 4392 | 5160 | 5992 | 6968 | 7736 | 8760 |
| 33B | 968 | 1992 | 2984 | 4008 | 4968 | 5992 | 6968 | 7992 | 8760 | 9912 |
| 34 | 1032 | 2088 | 3112 | 4264 | 5160 | 6200 | 7224 | 8504 | 9528 | 10296 |
| 34A | 1064 | 2088 | 3112 | 4264 | 5352 | 6456 | 7480 | 8504 | 9528 | 10680 |
| 35 | 1096 | 2216 | 3240 | 4392 | 5544 | 6712 | 7736 | 8760 | 9912 | 11064 |
| 36 | 1160 | 2280 | 3496 | 4584 | 5736 | 6968 | 7992 | 9144 | 10296 | 11448 |
| 37A | 1192 | 2408 | 3624 | 4776 | 5992 | 7224 | 8504 | 9528 | 10680 | 11832 |
| 37 | 1224 | 2472 | 3752 | 4968 | 6200 | 7480 | 8760 | 9912 | 11064 | 12384 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| 27 | 7224 | 7992 | 8504 | 9144 | 9912 | 10680 | 11448 | 11832 | 12576 | 12960 |
| 28 | 7736 | 8504 | 9144 | 9912 | 10680 | 11064 | 11832 | 12576 | 13536 | 14112 |
| 29 | 8248 | 8760 | 9528 | 10296 | 11064 | 11832 | 12576 | 13536 | 14112 | 14688 |
| 30 | 8504 | 9528 | 10296 | 11064 | 11832 | 12576 | 13536 | 14112 | 14688 | 15840 |
| 31 | 9144 | 9912 | 10680 | 11448 | 12216 | 12960 | 14112 | 14688 | 15840 | 16416 |
| 32 | 9528 | 10296 | 11064 | 11832 | 12960 | 13536 | 14688 | 15264 | 16416 | 16992 |
| 32A | 10296 | 11064 | 12216 | 12960 | 14112 | 14688 | 15840 | 16416 | 17568 | 18336 |
| 33 | 10680 | 11832 | 12960 | 13536 | 14688 | 15840 | 16992 | 17568 | 19080 | 19848 |
| 33A | 9528 | 10296 | 11448 | 12216 | 12960 | 14112 | 14688 | 15840 | 16416 | 17568 |
| 33B | 10680 | 11832 | 12960 | 13536 | 14688 | 15840 | 16992 | 17568 | 19080 | 19848 |
| 34 | 11448 | 12576 | 13536 | 14688 | 15840 | 16992 | 17568 | 19080 | 19848 | 20616 |
| 34A | 11448 | 12576 | 13536 | 14688 | 15840 | 16992 | 17568 | 19080 | 19848 | 21384 |
| 35 | 12216 | 12960 | 14112 | 15264 | 16416 | 17568 | 18336 | 19848 | 20616 | 22152 |
| 36 | 12576 | 13536 | 14688 | 15840 | 16992 | 18336 | 19848 | 20616 | 22152 | 22920 |
| 37A | 12960 | 14112 | 15840 | 16992 | 18336 | 19080 | 20616 | 21384 | 22920 | 23688 |
| 37 | 13536 | 14688 | 15840 | 17568 | 18336 | 19848 | 21384 | 22152 | 23688 | 24496 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
| 27 | 14112 | 14688 | 15264 | 15840 | 16416 | 16992 | 17568 | 18336 | 19080 | 19848 |
| 28 | 14688 | 15264 | 16416 | 16992 | 17568 | 18336 | 19080 | 19848 | 20616 | 21384 |
| 29 | 15840 | 16416 | 16992 | 17568 | 18336 | 19080 | 19848 | 20616 | 21384 | 22152 |
| 30 | 16416 | 16992 | 18336 | 19080 | 19848 | 20616 | 21384 | 22152 | 22920 | 23688 |
| 31 | 17568 | 18336 | 19080 | 19848 | 20616 | 21384 | 22152 | 22920 | 23688 | 24496 |
| 32 | 17568 | 19080 | 19848 | 20616 | 21384 | 22152 | 22920 | 23688 | 24496 | 25456 |
| 32A | 19848 | 20616 | 21384 | 22152 | 22920 | 24496 | 25456 | 26416 | 27376 | 27376 |
| 33 | 20616 | 21384 | 22920 | 23688 | 24496 | 25456 | 26416 | 27376 | 28336 | 29296 |
| 33A | 18336 | 19080 | 19848 | 20616 | 22152 | 22920 | 23688 | 24496 | 25456 | 26416 |
| 33B | 20616 | 21384 | 22920 | 23688 | 24496 | 25456 | 26416 | 27376 | 28336 | 29296 |
| 34 | 22152 | 22920 | 24496 | 25456 | 26416 | 27376 | 28336 | 29296 | 30576 | 31704 |
| 34A | 22152 | 22920 | 24496 | 25456 | 26416 | 27376 | 28336 | 29296 | 30576 | 31704 |
| 35 | 22920 | 24496 | 25456 | 26416 | 27376 | 28336 | 29296 | 30576 | 31704 | 32856 |
| 36 | 24496 | 25456 | 26416 | 27376 | 28336 | 29296 | 30576 | 31704 | 32856 | 34008 |
| 37A | 25456 | 26416 | 27376 | 28336 | 30576 | 31704 | 32856 | 34008 | 35160 | 36696 |
| 37 | 26416 | 27376 | 28336 | 29296 | 30576 | 31704 | 32856 | 35160 | 35160 | 36696 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
| 27 | 20616 | 21384 | 22152 | 22920 | 22920 | 23688 | 24496 | 25456 | 25456 | 26416 |
| 28 | 22152 | 22152 | 22920 | 23688 | 24496 | 25456 | 26416 | 26416 | 27376 | 28336 |
| 29 | 22920 | 23688 | 24496 | 25456 | 26416 | 26416 | 27376 | 28336 | 29296 | 29296 |
| 30 | 24496 | 25456 | 25456 | 26416 | 27376 | 28336 | 29296 | 29296 | 30576 | 31704 |
| 31 | 25456 | 26416 | 27376 | 28336 | 29296 | 29296 | 30576 | 31704 | 31704 | 32856 |
| 32 | 26416 | 27376 | 28336 | 29296 | 29296 | 30576 | 31704 | 32856 | 32856 | 34008 |
| 32A | 28336 | 29296 | 30576 | 31704 | 32856 | 32856 | 34008 | 35160 | 36696 | 36696 |
| 33 | 30576 | 31704 | 32856 | 34008 | 35160 | 35160 | 36696 | 37888 | 39232 | 39232 |
| 33A | 27376 | 27376 | 29296 | 29296 | 30576 | 30576 | 31704 | 32856 | 34008 | 35160 |
| 33B | 30576 | 31704 | 32856 | 34008 | 35160 | 35160 | 36696 | 37888 | 39232 | 39232 |
| 34 | 32856 | 34008 | 35160 | 35160 | 36696 | 37888 | 39232 | 39232 | 40576 | 42368 |
| 34A | 32856 | 34008 | 35160 | 35160 | 36696 | 37888 | 39232 | 40576 | 40576 | 42368 |
| 35 | 34008 | 35160 | 36696 | 37888 | 37888 | 39232 | 40576 | 42368 | 42368 | 43816 |
| 36 | 35160 | 36696 | 37888 | 39232 | 40576 | 40576 | 42368 | 43816 | 45352 | 45352 |
| 37A | 36696 | 37888 | 39232 | 40576 | 42368 | 43816 | 43816 | 45352 | 46888 | 48936 |
| 37 | 37888 | 39232 | 40576 | 42368 | 43816 | 43816 | 45352 | 46888 | 48936 | 48936 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
| 27 | 27376 | 27376 | 28336 | 29296 | 29296 | 30576 | 31704 | 31704 | 32856 | 32856 |
| 28 | 29296 | 29296 | 30576 | 30576 | 31704 | 32856 | 32856 | 34008 | 34008 | 35160 |
| 29 | 30576 | 31704 | 31704 | 32856 | 34008 | 34008 | 35160 | 35160 | 36696 | 36696 |
| 30 | 31704 | 32856 | 34008 | 34008 | 35160 | 36696 | 36696 | 37888 | 37888 | 39232 |
| 31 | 34008 | 35160 | 35160 | 36696 | 36696 | 37888 | 39232 | 39232 | 40576 | 40576 |
| 32 | 35160 | 35160 | 36696 | 37888 | 37888 | 39232 | 40576 | 40576 | 42368 | 42368 |
| 32A | 37888 | 39232 | 40576 | 40576 | 42368 | 42368 | 43816 | 43816 | 45352 | 46888 |
| 33 | 40576 | 40576 | 42368 | 43816 | 43816 | 45352 | 46888 | 46888 | 48936 | 48936 |
| 33A | 35160 | 36696 | 36696 | 37888 | 39232 | 40576 | 40576 | 40576 | 42368 | 43816 |
| 33B | 40576 | 40576 | 42368 | 43816 | 43816 | 45352 | 46888 | 46888 | 48936 | 48936 |
| 34 | 42368 | 43816 | 45352 | 46888 | 46888 | 48936 | 48936 | 51024 | 51024 | 52752 |
| 34A | 43816 | 43816 | 45352 | 46888 | 46888 | 48936 | 48936 | 51024 | 51024 | 52752 |
| 35 | 45352 | 46888 | 46888 | 48936 | 48936 | 51024 | 51024 | 52752 | 52752 | 55056 |
| 36 | 46888 | 48936 | 48936 | 51024 | 51024 | 52752 | 55056 | 55056 | 57336 | 57336 |
| 37A | 48936 | 51024 | 51024 | 52752 | 55056 | 55056 | 57336 | 57336 | 59256 | 59256 |
| 37 | 51024 | 52752 | 52752 | 55056 | 55056 | 57336 | 57336 | 59256 | 61664 | 61664 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 |
| 27 | 34008 | 34008 | 35160 | 35160 | 36696 | 36696 | 37888 | 37888 | 39232 | 39232 |
| 28 | 35160 | 36696 | 36696 | 37888 | 39232 | 39232 | 40576 | 40576 | 42368 | 42368 |
| 29 | 37888 | 39232 | 39232 | 40576 | 40576 | 42368 | 42368 | 43816 | 43816 | 45352 |
| 30 | 40576 | 40576 | 42368 | 42368 | 43816 | 43816 | 45352 | 45352 | 46888 | 46888 |
| 31 | 42368 | 42368 | 43816 | 45352 | 45352 | 46888 | 46888 | 46888 | 48936 | 48936 |
| 32 | 43816 | 43816 | 45352 | 46888 | 46888 | 46888 | 48936 | 48936 | 51024 | 51024 |
| 32A | 46888 | 48936 | 48936 | 51024 | 51024 | 52752 | 52752 | 52752 | 55056 | 55056 |
| 33 | 51024 | 51024 | 52752 | 52752 | 55056 | 55056 | 57336 | 57336 | 59256 | 59256 |
| 33A | 43816 | 45352 | 45352 | 46888 | 48936 | 48936 | 48936 | 51024 | 51024 | 52752 |
| 33B | 51024 | 51024 | 52752 | 52752 | 55056 | 55056 | 57336 | 57336 | 59256 | 59256 |
| 34 | 52752 | 55056 | 55056 | 57336 | 57336 | 59256 | 59256 | 61664 | 61664 | 63776 |
| 34A | 52752 | 55056 | 55056 | 57336 | 57336 | 59256 | 59256 | 61664 | 61664 | 63776 |
| 35 | 55056 | 57336 | 57336 | 59256 | 59256 | 61664 | 61664 | 63776 | 63776 | 66592 |
| 36 | 59256 | 59256 | 61664 | 61664 | 63776 | 63776 | 66592 | 66592 | 68808 | 68808 |
| 37A | 61664 | 61664 | 63776 | 63776 | 66592 | 66592 | 68808 | 68808 | 71112 | 71112 |
| 37 | 63776 | 63776 | 66592 | 66592 | 68808 | 68808 | 71112 | 71112 | 73712 | 75376 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 |
| 27 | 40576 | 40576 | 42368 | 42368 | 43816 | 43816 | 43816 | 45352 | 45352 | 46888 |
| 28 | 42368 | 43816 | 43816 | 45352 | 45352 | 46888 | 46888 | 46888 | 48936 | 48936 |
| 29 | 45352 | 45352 | 46888 | 46888 | 48936 | 48936 | 48936 | 51024 | 51024 | 52752 |
| 30 | 46888 | 48936 | 48936 | 51024 | 51024 | 51024 | 52752 | 52752 | 55056 | 55056 |
| 31 | 51024 | 51024 | 52752 | 52752 | 52752 | 55056 | 55056 | 55056 | 57336 | 57336 |
| 32 | 52752 | 52752 | 52752 | 55056 | 55056 | 57336 | 57336 | 57336 | 59256 | 59256 |
| 32A | 57336 | 57336 | 59256 | 59256 | 59256 | 61664 | 61664 | 63776 | 63776 | 63776 |
| 33 | 59256 | 61664 | 61664 | 63776 | 63776 | 63776 | 66592 | 66592 | 68808 | 68808 |
| 33A | 52752 | 55056 | 55056 | 55056 | 57336 | 57336 | 57336 | 59256 | 59256 | 61664 |
| 33B | 59256 | 61664 | 61664 | 63776 | 63776 | 63776 | 66592 | 66592 | 68808 | 68808 |
| 34 | 63776 | 63776 | 66592 | 66592 | 68808 | 68808 | 71112 | 71112 | 71112 | 73712 |
| 34A | 63776 | 66592 | 66592 | 66592 | 68808 | 68808 | 71112 | 71112 | 73712 | 73712 |
| 35 | 66592 | 68808 | 68808 | 71112 | 71112 | 73712 | 73712 | 75376 | 76208 | 76208 |
| 36 | 71112 | 71112 | 73712 | 73712 | 75376 | 76208 | 76208 | 78704 | 78704 | 81176 |
| 37A | 73712 | 73712 | 75376 | 76208 | 78704 | 78704 | 81176 | 81176 | 81176 | 84760 |
| 37 | 76208 | 76208 | 78704 | 78704 | 81176 | 81176 | 81176 | 84760 | 84760 | 87936 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 |
| 27 | 46888 | 46888 | 48936 | 48936 | 48936 | 51024 | 51024 | 51024 | 52752 | 52752 |
| 28 | 48936 | 51024 | 51024 | 52752 | 52752 | 52752 | 55056 | 55056 | 55056 | 57336 |
| 29 | 52752 | 52752 | 55056 | 55056 | 55056 | 57336 | 57336 | 57336 | 59256 | 59256 |
| 30 | 55056 | 57336 | 57336 | 57336 | 59256 | 59256 | 59256 | 61664 | 61664 | 63776 |
| 31 | 59256 | 59256 | 59256 | 61664 | 61664 | 63776 | 63776 | 63776 | 66592 | 66592 |
| 32 | 61664 | 61664 | 61664 | 63776 | 63776 | 63776 | 66592 | 66592 | 66592 | 68808 |
| 32A | 66592 | 66592 | 68808 | 68808 | 68808 | 71112 | 71112 | 73712 | 73712 | 73712 |
| 33 | 71112 | 71112 | 71112 | 73712 | 75376 | 76208 | 76208 | 76208 | 78704 | 78704 |
| 33A | 61664 | 61664 | 63776 | 63776 | 66592 | 66592 | 66592 | 68808 | 68808 | 68808 |
| 33B | 71112 | 71112 | 71112 | 73712 | 75376 | 76208 | 76208 | 76208 | 78704 | 78704 |
| 34 | 75376 | 76208 | 76208 | 78704 | 78704 | 78704 | 81176 | 81176 | 81176 | 84760 |
| 34A | 75376 | 76208 | 76208 | 78704 | 78704 | 81176 | 81176 | 81176 | 84760 | 84760 |
| 35 | 78704 | 78704 | 81176 | 81176 | 81176 | 84760 | 84760 | 84760 | 87936 | 87936 |
| 36 | 81176 | 81176 | 84760 | 84760 | 84760 | 87936 | 87936 | 90816 | 90816 | 90816 |
| 37A | 84760 | 84760 | 87936 | 87936 | 90816 | 90816 | 90816 | 93800 | 93800 | 97896 |
| 37 | 87936 | 87936 | 90816 | 90816 | 93800 | 93800 | 93800 | 97896 | 97896 | 97896 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 |
| 27 | 52752 | 55056 | 55056 | 55056 | 57336 | 57336 | 57336 | 59256 | 59256 | 59256 |
| 28 | 57336 | 57336 | 59256 | 59256 | 59256 | 61664 | 61664 | 61664 | 61664 | 63776 |
| 29 | 59256 | 61664 | 61664 | 61664 | 63776 | 63776 | 63776 | 66592 | 66592 | 66592 |
| 30 | 63776 | 63776 | 63776 | 66592 | 66592 | 66592 | 68808 | 68808 | 68808 | 71112 |
| 31 | 66592 | 68808 | 68808 | 68808 | 71112 | 71112 | 71112 | 73712 | 73712 | 73712 |
| 32 | 68808 | 71112 | 71112 | 71112 | 73712 | 73712 | 73712 | 75376 | 76208 | 76208 |
| 32A | 75376 | 76208 | 76208 | 78704 | 78704 | 78704 | 81176 | 81176 | 81176 | 84760 |
| 33 | 81176 | 81176 | 81176 | 81176 | 84760 | 84760 | 84760 | 87936 | 87936 | 87936 |
| 33A | 71112 | 71112 | 71112 | 73712 | 75376 | 75376 | 76208 | 76208 | 78704 | 78704 |
| 33B | 81176 | 81176 | 81176 | 81176 | 84760 | 84760 | 84760 | 87936 | 87936 | 87936 |
| 34 | 84760 | 84760 | 87936 | 87936 | 87936 | 90816 | 90816 | 93800 | 93800 | 93800 |
| 34A | 84760 | 87936 | 87936 | 87936 | 90816 | 90816 | 90816 | 93800 | 93800 | 93800 |
| 35 | 87936 | 90816 | 90816 | 93800 | 93800 | 93800 | 93800 | 97896 | 97896 | 97896 |
| 36 | 93800 | 93800 | 93800 | 97896 | 97896 | 97896 | 101840 | 101840 | 101840 | 101840 |
| 37A | 97896 | 97896 | 97896 | 101840 | 101840 | 101840 | 105528 | 105528 | 105528 | 107832 |
| 37 | 101840 | 101840 | 101840 | 105528 | 105528 | 107832 | 107832 | 110136 | 110136 | 112608 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100 |
| 27 | 59256 | 61664 | 61664 | 61664 | 63776 | 63776 | 63776 | 63776 | 66592 | 66592 |
| 28 | 63776 | 63776 | 66592 | 66592 | 66592 | 66592 | 68808 | 68808 | 68808 | 71112 |
| 29 | 66592 | 68808 | 68808 | 68808 | 71112 | 71112 | 71112 | 73712 | 73712 | 73712 |
| 30 | 71112 | 71112 | 73712 | 73712 | 75376 | 75376 | 76208 | 76208 | 78704 | 78704 |
| 31 | 75376 | 76208 | 76208 | 78704 | 78704 | 78704 | 81176 | 81176 | 81176 | 81176 |
| 32 | 78704 | 78704 | 78704 | 81176 | 81176 | 81176 | 84760 | 84760 | 84760 | 84760 |
| 32A | 84760 | 84760 | 87936 | 87936 | 87936 | 87936 | 90816 | 90816 | 90816 | 93800 |
| 33 | 90816 | 90816 | 90816 | 93800 | 93800 | 93800 | 93800 | 97896 | 97896 | 97896 |
| 33A | 78704 | 81176 | 81176 | 81176 | 81176 | 84760 | 84760 | 84760 | 84760 | 87936 |
| 33B | 90816 | 90816 | 90816 | 93800 | 93800 | 93800 | 93800 | 97896 | 97896 | 100752 |
| 34 | 93800 | 97896 | 97896 | 97896 | 97896 | 101840 | 101840 | 101840 | 105528 | 105528 |
| 34A | 93800 | 97896 | 97896 | 97896 | 101840 | 101840 | 101840 | 101840 | 105528 | 105528 |
| 35 | 97896 | 101840 | 101840 | 101840 | 105528 | 105528 | 105528 | 107832 | 110136 | 110136 |
| 36 | 105528 | 105528 | 107832 | 107832 | 110136 | 110136 | 112608 | 112608 | 115040 | 115040 |
| 37A | 110136 | 110136 | 112608 | 112608 | 115040 | 115040 | 117256 | 117256 | 119816 | 119816 |
| 37 | 112608 | 115040 | 115040 | 115040 | 117256 | 119816 | 119816 | 119816 | 124464 | 125808 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 101 | 102 | 103 | 104 | 105 | 106 | 107 | 108 | 109 | 110 |
| 27 | 66592 | 66592 | 68808 | 68808 | 68808 | 71112 | 71112 | 71112 | 71112 | 73712 |
| 28 | 71112 | 71112 | 73712 | 73712 | 73712 | 75376 | 75376 | 76208 | 76208 | 76208 |
| 29 | 75376 | 76208 | 76208 | 76208 | 78704 | 78704 | 78704 | 81176 | 81176 | 81176 |
| 30 | 78704 | 81176 | 81176 | 81176 | 81176 | 84760 | 84760 | 84760 | 84760 | 87936 |
| 31 | 84760 | 84760 | 84760 | 84760 | 87936 | 87936 | 87936 | 87936 | 90816 | 90816 |
| 32 | 87936 | 87936 | 87936 | 87936 | 90816 | 90816 | 90816 | 93800 | 93800 | 93800 |
| 32A | 93800 | 93800 | 93800 | 97896 | 97896 | 97896 | 97896 | 101840 | 101840 | 101840 |
| 33 | 97896 | 97896 | 97896 | 97896 | 97896 | 97896 | 97896 | 97896 | 97896 | 97896 |
| 33A | 87936 | 87936 | 87936 | 90816 | 90816 | 90816 | 93800 | 93800 | 93800 | 97896 |
| 33B | 100752 | 100752 | 100752 | 100752 | 100752 | 100752 | 100752 | 100752 | 100752 | 100752 |
| 34 | 105528 | 105528 | 105528 | 105528 | 105528 | 105528 | 105528 | 105528 | 105528 | 105528 |
| 34A | 105528 | 107832 | 107832 | 110136 | 110136 | 112608 | 112608 | 115040 | 115040 | 115040 |
| 35 | 110136 | 110136 | 112608 | 115040 | 115040 | 115040 | 117256 | 119816 | 119816 | 119816 |
| 36 | 117256 | 117256 | 117256 | 119816 | 119816 | 119816 | 124464 | 124464 | 125808 | 125808 |
| 37A | 119816 | 124464 | 124464 | 124464 | 125808 | 125808 | 128496 | 128496 | 130392 | 130392 |
| 37 | 125808 | 125808 | 128496 | 128496 | 128496 | 133208 | 133208 | 133208 | 133208 | 137792 |

##### 7.1.7.2.2 Transport blocks mapped to two-layer spatial multiplexing

For, the TBS is given by the (,) entry of Table 7.1.7.2.1-1.

For, a baseline TBS_L1 is taken from the (,) entry of Table 7.1.7.2.1-1, which is then translated into TBS_L2 using the mapping rule shown in Table 7.1.7.2.2-1. The TBS is given by TBS_L2.

Table 7.1.7.2.2-1: One-layer to two-layer TBS translation table

| TBS_L1 | TBS_L2 | TBS_L1 | TBS_L2 | TBS_L1 | TBS_L2 | TBS_L1 | TBS_L2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1544 | 3112 | 3752 | 7480 | 10296 | 20616 | 28336 | 57336 |
| 1608 | 3240 | 3880 | 7736 | 10680 | 21384 | 29296 | 59256 |
| 1672 | 3368 | 4008 | 7992 | 11064 | 22152 | 30576 | 61664 |
| 1736 | 3496 | 4136 | 8248 | 11448 | 22920 | 31704 | 63776 |
| 1800 | 3624 | 4264 | 8504 | 11832 | 23688 | 32856 | 66592 |
| 1864 | 3752 | 4392 | 8760 | 12216 | 24496 | 34008 | 68808 |
| 1928 | 3880 | 4584 | 9144 | 12576 | 25456 | 35160 | 71112 |
| 1992 | 4008 | 4776 | 9528 | 12960 | 25456 | 36696 | 73712 |
| 2024 | 4008 | 4968 | 9912 | 13536 | 27376 | 37888 | 76208 |
| 2088 | 4136 | 5160 | 10296 | 14112 | 28336 | 39232 | 78704 |
| 2152 | 4264 | 5352 | 10680 | 14688 | 29296 | 40576 | 81176 |
| 2216 | 4392 | 5544 | 11064 | 15264 | 30576 | 42368 | 84760 |
| 2280 | 4584 | 5736 | 11448 | 15840 | 31704 | 43816 | 87936 |
| 2344 | 4776 | 5992 | 11832 | 16416 | 32856 | 45352 | 90816 |
| 2408 | 4776 | 6200 | 12576 | 16992 | 34008 | 46888 | 93800 |
| 2472 | 4968 | 6456 | 12960 | 17568 | 35160 | 48936 | 97896 |
| 2536 | 5160 | 6712 | 13536 | 18336 | 36696 | 51024 | 101840 |
| 2600 | 5160 | 6968 | 14112 | 19080 | 37888 | 52752 | 105528 |
| 2664 | 5352 | 7224 | 14688 | 19848 | 39232 | 55056 | 110136 |
| 2728 | 5544 | 7480 | 14688 | 20616 | 40576 | 57336 | 115040 |
| 2792 | 5544 | 7736 | 15264 | 21384 | 42368 | 59256 | 119816 |
| 2856 | 5736 | 7992 | 15840 | 22152 | 43816 | 61664 | 124464 |
| 2984 | 5992 | 8248 | 16416 | 22920 | 45352 | 63776 | 128496 |
| 3112 | 6200 | 8504 | 16992 | 23688 | 46888 | 66592 | 133208 |
| 3240 | 6456 | 8760 | 17568 | 24496 | 48936 | 68808 | 137792 |
| 3368 | 6712 | 9144 | 18336 | 25456 | 51024 | 71112 | 142248 |
| 3496 | 6968 | 9528 | 19080 | 26416 | 52752 | 73712 | 146856 |
| 3624 | 7224 | 9912 | 19848 | 27376 | 55056 | 75376 | 149776 |
| 76208 | 152976 | 81176 | 161760 | 87936 | 175600 | 93800 | 187712 |
| 78704 | 157432 | 84760 | 169544 | 90816 | 181656 | 97896 | 195816 |
| 100752 | 201936 | 101840 | 203704 | 105528 | 211936 |  |  |
| 107832 | 214176 | 110136 | 220296 | 112608 | 226416 | 115040 | 230104 |
| 117256 | 236160 | 119816 | 239656 | 124464 | 248272 | 125808 | 251640 |

##### 7.1.7.2.3 Transport blocks mapped for DCI Format 1C and DCI Format 6-2

The TBS is given by theentry of Table 7.1.7.2.3-1. For DCI Format 6-2, .

Table 7.1.7.2.3-1: Transport Block Size (TBS) table for DCI format 1C and DCI Format 6-2

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TBS | 40 | 56 | 72 | 120 | 136 | 144 | 176 | 208 | 224 | 256 | 280 | 296 | 328 | 336 | 392 | 488 |
|  | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
| TBS | 552 | 600 | 632 | 696 | 776 | 840 | 904 | 1000 | 1064 | 1128 | 1224 | 1288 | 1384 | 1480 | 1608 | 1736 |

##### 7.1.7.2.4 Transport blocks mapped to three-layer spatial multiplexing

For , the TBS is given by the (,) entry of Table 7.1.7.2.1-1.

For , a baseline TBS_L1 is taken from the (,) entry of Table 7.1.7.2.1-1, which is then translated into TBS_L3 using the mapping rule shown in Table 7.1.7.2.4-1. The TBS is given by TBS_L3.

Table 7.1.7.2.4-1: One-layer to three-layer TBS translation table

| TBS_L1 | TBS_L3 | TBS_L1 | TBS_L3 | TBS_L1 | TBS_L3 | TBS_L1 | TBS_L3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1032 | 3112 | 2664 | 7992 | 8248 | 24496 | 26416 | 78704 |
| 1064 | 3240 | 2728 | 8248 | 8504 | 25456 | 27376 | 81176 |
| 1096 | 3240 | 2792 | 8248 | 8760 | 26416 | 28336 | 84760 |
| 1128 | 3368 | 2856 | 8504 | 9144 | 27376 | 29296 | 87936 |
| 1160 | 3496 | 2984 | 8760 | 9528 | 28336 | 30576 | 90816 |
| 1192 | 3624 | 3112 | 9144 | 9912 | 29296 | 31704 | 93800 |
| 1224 | 3624 | 3240 | 9528 | 10296 | 30576 | 32856 | 97896 |
| 1256 | 3752 | 3368 | 9912 | 10680 | 31704 | 34008 | 101840 |
| 1288 | 3880 | 3496 | 10296 | 11064 | 32856 | 35160 | 105528 |
| 1320 | 4008 | 3624 | 10680 | 11448 | 34008 | 36696 | 110136 |
| 1352 | 4008 | 3752 | 11064 | 11832 | 35160 | 37888 | 115040 |
| 1384 | 4136 | 3880 | 11448 | 12216 | 36696 | 39232 | 119816 |
| 1416 | 4264 | 4008 | 11832 | 12576 | 37888 | 40576 | 119816 |
| 1480 | 4392 | 4136 | 12576 | 12960 | 39232 | 42368 | 128496 |
| 1544 | 4584 | 4264 | 12960 | 13536 | 40576 | 43816 | 133208 |
| 1608 | 4776 | 4392 | 12960 | 14112 | 42368 | 45352 | 137792 |
| 1672 | 4968 | 4584 | 13536 | 14688 | 43816 | 46888 | 142248 |
| 1736 | 5160 | 4776 | 14112 | 15264 | 45352 | 48936 | 146856 |
| 1800 | 5352 | 4968 | 14688 | 15840 | 46888 | 51024 | 152976 |
| 1864 | 5544 | 5160 | 15264 | 16416 | 48936 | 52752 | 157432 |
| 1928 | 5736 | 5352 | 15840 | 16992 | 51024 | 55056 | 165216 |
| 1992 | 5992 | 5544 | 16416 | 17568 | 52752 | 57336 | 171888 |
| 2024 | 5992 | 5736 | 16992 | 18336 | 55056 | 59256 | 177816 |
| 2088 | 6200 | 5992 | 18336 | 19080 | 57336 | 61664 | 185728 |
| 2152 | 6456 | 6200 | 18336 | 19848 | 59256 | 63776 | 191720 |
| 2216 | 6712 | 6456 | 19080 | 20616 | 61664 | 66592 | 199824 |
| 2280 | 6712 | 6712 | 19848 | 21384 | 63776 | 68808 | 205880 |
| 2344 | 6968 | 6968 | 20616 | 22152 | 66592 | 71112 | 214176 |
| 2408 | 7224 | 7224 | 21384 | 22920 | 68808 | 73712 | 221680 |
| 2472 | 7480 | 7480 | 22152 | 23688 | 71112 | 75376 | 226416 |
| 2536 | 7480 | 7736 | 22920 | 24496 | 73712 |  |  |
| 2600 | 7736 | 7992 | 23688 | 25456 | 76208 |  |  |
| 76208 | 230104 | 81176 | 245648 | 87936 | 266440 | 93800 | 284608 |
| 78704 | 236160 | 84760 | 254328 | 90816 | 275376 | 97896 | 293736 |
| 105528 | 314888 | 107832 | 324336 | 110136 | 324336 | 112608 | 336576 |
| 115040 | 339112 | 117256 | 351224 | 119816 | 363336 | 124464 | 373296 |
| 125808 | 375448 |  |  |  |  |  |  |

##### 7.1.7.2.5 Transport blocks mapped to four-layer spatial multiplexing

For , the TBS is given by the (,) entry of Table 7.1.7.2.1-1.

For , a baseline TBS_L1 is taken from the (,) entry of Table 7.1.7.2.1-1, which is then translated into TBS_L4 using the mapping rule shown in Table 7.1.7.2.5-1. The TBS is given by TBS_L4.

Table 7.1.7.2.5-1: One-layer to four-layer TBS translation table

| TBS_L1 | TBS_L4 | TBS_L1 | TBS_L4 | TBS_L1 | TBS_L4 | TBS_L1 | TBS_L4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 776 | 3112 | 2280 | 9144 | 7224 | 29296 | 24496 | 97896 |
| 808 | 3240 | 2344 | 9528 | 7480 | 29296 | 25456 | 101840 |
| 840 | 3368 | 2408 | 9528 | 7736 | 30576 | 26416 | 105528 |
| 872 | 3496 | 2472 | 9912 | 7992 | 31704 | 27376 | 110136 |
| 904 | 3624 | 2536 | 10296 | 8248 | 32856 | 28336 | 115040 |
| 936 | 3752 | 2600 | 10296 | 8504 | 34008 | 29296 | 115040 |
| 968 | 3880 | 2664 | 10680 | 8760 | 35160 | 30576 | 124464 |
| 1000 | 4008 | 2728 | 11064 | 9144 | 36696 | 31704 | 128496 |
| 1032 | 4136 | 2792 | 11064 | 9528 | 37888 | 32856 | 133208 |
| 1064 | 4264 | 2856 | 11448 | 9912 | 39232 | 34008 | 137792 |
| 1096 | 4392 | 2984 | 11832 | 10296 | 40576 | 35160 | 142248 |
| 1128 | 4584 | 3112 | 12576 | 10680 | 42368 | 36696 | 146856 |
| 1160 | 4584 | 3240 | 12960 | 11064 | 43816 | 37888 | 151376 |
| 1192 | 4776 | 3368 | 13536 | 11448 | 45352 | 39232 | 157432 |
| 1224 | 4968 | 3496 | 14112 | 11832 | 46888 | 40576 | 161760 |
| 1256 | 4968 | 3624 | 14688 | 12216 | 48936 | 42368 | 169544 |
| 1288 | 5160 | 3752 | 15264 | 12576 | 51024 | 43816 | 175600 |
| 1320 | 5352 | 3880 | 15264 | 12960 | 51024 | 45352 | 181656 |
| 1352 | 5352 | 4008 | 15840 | 13536 | 55056 | 46888 | 187712 |
| 1384 | 5544 | 4136 | 16416 | 14112 | 57336 | 48936 | 195816 |
| 1416 | 5736 | 4264 | 16992 | 14688 | 59256 | 51024 | 203704 |
| 1480 | 5992 | 4392 | 17568 | 15264 | 61664 | 52752 | 211936 |
| 1544 | 6200 | 4584 | 18336 | 15840 | 63776 | 55056 | 220296 |
| 1608 | 6456 | 4776 | 19080 | 16416 | 66592 | 57336 | 230104 |
| 1672 | 6712 | 4968 | 19848 | 16992 | 68808 | 59256 | 236160 |
| 1736 | 6968 | 5160 | 20616 | 17568 | 71112 | 61664 | 245648 |
| 1800 | 7224 | 5352 | 21384 | 18336 | 73712 | 63776 | 254328 |
| 1864 | 7480 | 5544 | 22152 | 19080 | 76208 | 66592 | 266440 |
| 1928 | 7736 | 5736 | 22920 | 19848 | 78704 | 68808 | 275376 |
| 1992 | 7992 | 5992 | 23688 | 20616 | 81176 | 71112 | 284608 |
| 2024 | 7992 | 6200 | 24496 | 21384 | 84760 | 73712 | 293736 |
| 2088 | 8248 | 6456 | 25456 | 22152 | 87936 | 75376 | 299856 |
| 2152 | 8504 | 6712 | 26416 | 22920 | 90816 |  |  |
| 2216 | 8760 | 6968 | 28336 | 23688 | 93800 |  |  |
| 76208 | 305976 | 81176 | 324336 | 87936 | 351224 | 93800 | 375448 |
| 78704 | 314888 | 84760 | 339112 | 90816 | 363336 | 97896 | 391656 |
| 105528 | 422232 | 107832 | 422232 | 110136 | 440616 | 112608 | 452832 |
| 115040 | 460232 | 117256 | 471192 | 119816 | 478400 | 124464 | 501792 |
| 125808 | 502624 |  |  |  |  |  |  |

##### 7.1.7.2.6 Transport blocks mapped for BL/CE UEs configured with CEModeB and PDSCH bandwidth up to 1.4MHz

BL/CE UEs configured with CEModeB and not configured with higher layer parameter ce-pdsch-maxBandwidth-config with value ≥5MHz and not configured with higher layer parameter mpdcch-PDSCH-MaxBandwidth-SC-MTCH with value 24 PRBs shall set  and determine its TBS by the procedure in Clause 7.1.7.2.1 for , and  = 4 or= 6.

##### 7.1.7.2.7 Transport blocks mapped for BL/CE UEs SystemInformationBlockType1-BR

The TBS is given by theentry of Table 7.1.7.2.7-1.

Table 7.1.7.2.7-1: Transport block size (TBS) table for PDSCH carrying SystemInformationBlockType1-BR

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TBS | N/A | 208 | 208 | 208 | 256 | 256 | 256 | 328 | 328 | 328 | 504 | 504 | 504 | 712 | 712 | 712 |
|  | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
| TBS | 936 | 936 | 936 | Reserved |  |  |  |  |  |  |  |  |  |  |  |  |

##### 7.1.7.2.8 Transport blocks mapped for UEs configured with ce-pdsch-maxBandwidth-config value of 5 MHz or with pdsch-MaxBandwidth-SC-MTCH value of 24 PRBs

For, and the TBS is given by the (,) entry of Table 7.1.7.2.1-1.

For, and the TBS is given by the (,) entry of Table 7.1.7.2.8-1.

Table 7.1.7.2.8-1: Transport block size (TBS) table for UEs configured with ce-pdsch-maxBandwidth-config value of 5 MHz or with pdsch-MaxBandwidth-SC-MTCH value of 24 PRBs

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
| 0 | 392 | 424 | 456 | 488 | 504 | 536 | 568 | 600 | 616 | 648 |
| 1 | 520 | 568 | 600 | 632 | 680 | 712 | 744 | 776 | 808 | 872 |
| 2 | 648 | 696 | 744 | 776 | 840 | 872 | 936 | 968 | 1000 | 1064 |
| 3 | 872 | 904 | 968 | 1032 | 1096 | 1160 | 1224 | 1256 | 1320 | 1384 |
| 4 | 1064 | 1128 | 1192 | 1288 | 1352 | 1416 | 1480 | 1544 | 1608 | 1736 |
| 5 | 1320 | 1384 | 1480 | 1544 | 1672 | 1736 | 1864 | 1928 | 2024 | 2088 |
| 6 | 1544 | 1672 | 1736 | 1864 | 1992 | 2088 | 2216 | 2280 | 2408 | 2472 |
| 7 | 1800 | 1928 | 2088 | 2216 | 2344 | 2472 | 2536 | 2664 | 2792 | 2984 |
| 8 | 2088 | 2216 | 2344 | 2536 | 2664 | 2792 | 2984 | 3112 | 3240 | 3368 |
| 9 | 2344 | 2536 | 2664 | 2856 | 2984 | 3112 | 3368 | 3496 | 3624 | 3752 |
| 10 | 2664 | 2792 | 2984 | 3112 | 3368 | 3496 | 3752 | 3880 | 4008 | 4008 |
| 11 | 2984 | 3240 | 3496 | 3624 | 3880 | 4008 | 4008 | 4008 |  |  |
| 12 | 3368 | 3624 | 3880 | 4008 | 4008 |  |  |  |  |  |
| 13 | 3880 | 4008 | 4008 |  |  |  |  |  |  |  |
| 14 | 4008 |  |  |  |  |  |  |  |  |  |

#### 7.1.7.3 Redundancy Version determination for Format 1C

If the DCI Format 1C CRC is scrambled by P-RNTI or RA-RNTI, then

- the UE shall set the Redundancy Version to 0

Else if the DCI Format 1C CRC is scrambled by SI-RNTI, then

- the UE shall set the Redundancy Version as defined in [8].

### 7.1.8 Storing soft channel bits

For FDD, TDD and FDD-TDD, if the UE is configured with more than one serving cell or if the UE is configured with a SCG, then for each serving cell, for at least  transport blocks, upon decoding failure of a code block of a transport block, the UE shall store received soft channel bits corresponding to a range of at least ,…,, where:

,

,  , , , ,and  are defined in Clause 5.1.4.1.2 of [4].

MDL_HARQ is the maximum number of DL HARQ processes.

If the UE is configured with a SCG

- is the number of configured serving cells across both MCG and SCG.

else

- is the number of configured serving cells.

is the maximum "Total number of soft channel bits" [12] among all the indicated UE categories [11] of this UE.

In determining k, the UE should give priority to storing soft channel bits corresponding to lower values of k.  shall correspond to a received soft channel bit. The range ,…,may include subsets not containing received soft channel bits.

### 7.1.9 PDSCH resource mapping parameters

A UE configured in transmission mode 10 for a given serving cell can be configured with up to 8 parameter sets by higher layer signaling to decode PDSCH according to a detected PDCCH/EPDCCH with DCI format 2D intended for the UE and the given serving cell. The UE shall use the parameter set according to the value of the 'PDSCH RE Mapping and Quasi-Co-Location indicator' field (mapping defined in Table 7.1.9-1 for Type B and defined in Table 7.9.1-1A for Type C quasi co-location) in the detected PDCCH/EPDCCH with DCI format 2D for determining the RE mapping (defined in Clause 6.4 of [3]), and for determining antenna port quasi co-location (defined in Clause 7.1.10) for PDSCH if the UE is configured with Type B quasi co-location type (defined in Clause 7.1.10) or for each PDSCH codeword if the UE is configured with Type C quasi co-location (defined in Clause 7.1.10). If the UE is configured with Type C quasi co-location and not configured with parameter set for codeword 1, the UE shall assume the parameter set for codeword 1 is the same as the parameter set for codeword 0.

For PDSCH without a corresponding PDCCH/EPDCCH, the UE shall use the parameter set indicated in the PDCCH/EPDCCH with DCI format 2D corresponding to the associated SPS activation for determining the RE mapping (defined in Clause 6.4 of [3]) and antenna port quasi co-location (defined in Clause 7.1.10) for PDSCH if the UE is configured with Type B quasi co-location and for each PDSCH codeword if the UE is configured with Type C quasi co-location.

Table 7.1.9-1: PDSCH RE Mapping and Quasi-Co-Location Indicator field in DCI format 2D for Type B quasi co-location

| Value of 'PDSCH RE Mapping and Quasi-Co-Location Indicator' field | Description |
| --- | --- |
| '00' | Parameter set 1 configured by higher layers |
| '01' | Parameter set 2 configured by higher layers |
| '10' | Parameter set 3 configured by higher layers |
| '11' | Parameter set 4 configured by higher layers |

Table 7.1.9-1A: PDSCH RE Mapping and Quasi-Co-Location Indicator field in DCI format 2D for Type C quasi co-location

| Value of 'PDSCH RE Mapping and Quasi-Co-Location Indicator' field | Description |
| --- | --- |
| '00' | Parameter set 1 configured by higher layers for codeword 0 and Parameter set 2 configured by higher layers for codeword 1 (if any) |
| '01' | Parameter set 3 configured by higher layers for codeword 0 and Parameter set 4 configured by higher layers for codeword 1 (if any) |
| '10' | Parameter set 5 configured by higher layers for codeword 0 and Parameter set 6 configured by higher layers for codeword 1 (if any) |
| '11' | Parameter set 7 configured by higher layers for codeword 0 and Parameter set 8 configured by higher layers for codeword 1 (if any) |

The following parameters for determining PDSCH RE mapping and PDSCH antenna port quasi co-location are configured via higher layer signaling for each parameter set for Type B quasi co-location and parameter set 1,3,5,7 for Type C quasi co-location:

- crs-PortsCount-r11.

- crs-FreqShift-r11.

- mbsfn-SubframeConfigList-r11.

- csi-RS-ConfigZPId-r11.

- pdsch-Start-r11.

- qcl-CSI-RS-ConfigNZPId-r11.

The following parameters for determining PDSCH RE mapping and PDSCH antenna port quasi co-location are configured via higher layer signaling for parameter set 2,4,6,8 for Type C quasi co-location

- crs-PortsCount-v15xy.

- crs-FreqShift-v15xy.

- mbsfn-SubframeConfigList-v15xy.

- csi-RS-ConfigZPId-v15xy.

- pdsch-Start-v15xy.

- qcl-CSI-RS-ConfigNZPId-v15xy.

To decode PDSCH according to a detected PDCCH/EPDCCH with DCI format 1A with CRC scrambled with C-RNTI intended for the UE and the given serving cell and for PDSCH transmission on antenna port 7, a UE configured in transmission mode 10 for a given serving cell shall use the parameter set 1 in table 7.1.9-1 or table 7.1.9-1A for determining the PDSCH RE mapping (defined in Clause 6.4 of [3]), and for determining PDSCH antenna port quasi co-location (defined in Clause 7.1.10) if the UE is configured with Type B or Type C quasi co-location type (defined in Clause 7.1.10).

To decode PDSCH corresponding to detected PDCCH/EPDCCH with DCI format 1A with CRC scrambled with SPS C-RNTI and PDSCH without a corresponding PDCCH/EPDCCH associated with SPS activation indicated in PDCCH/EPDCCH with DCI format 1A, a UE configured in transmission mode 10 for a given serving cell shall use the parameter set 1 in table 7.1.9-1 or table 7.1.9-1A for determining the PDSCH RE mapping (defined in Clause 6.4 of [3]), and for determining PDSCH antenna port quasi co-location (defined in Clause 7.1.10) if the UE is configured with Type B or Type C quasi co-location type (defined in Clause 7.1.10).

If the UE is configured in transmission mode 10 and configured with Type B or Type C quasi co-location and configured with higher layer parameter csi-RS-NZP-mode set to 'multiShot' for a CSI process, the UE is not expected to receive a 'PDSCH RE Mapping and Quasi-Co-Location indicator' selecting a parameter set with CSI-RS resource configuration for the CSI process identified by the higher layer parameter qcl-CSI-RS-ConfigNZPId-r11 corresponding to a deactivated CSI-RS resource (defined in Clause 7.2.8) or an activated CSI-RS resource (defined in Clause 7.2.8) with no CSI-RS transmission since the activation of the CSI-RS resource.

If the UE is configured in transmission mode 10 and configured with Type B or Type C quasi co-location and configured with higher layer parameter csi-RS-ConfigNZP-ApList and configured with higher layer parameter csi-RS-NZP-mode set to 'aperiodic' for a CSI process, the UE is not expected to receive a 'PDSCH RE Mapping and Quasi-Co-Location indicator' selecting a parameter set with CSI-RS resource configuration for the CSI process identified by the higher layer parameter qcl-CSI-RS-ConfigNZPId-r11.

To decode PDSCH according to a detected PDCCH/EPDCCH with DCI format 1A intended for the UE on a given serving cell and for PDSCH transmission on antenna port 0 – 3, a UE configured in transmission mode 10 for the given serving cell shall determine the PDSCH RE mapping (as described in Clause 6.4 of [3]) using the lowest indexed zero-power CSI-RS resource.

To decode PDSCH according to a detected SPDCCH with DCI format 7-1 A, 7-1B, 7-1C, 7-1D, 7-1E, 7-1F, 7-1G with CRC scrambled with C-RNTI or retransmission of PDSCH according to a detected SPDCCH with DCI format 7-1 A, 7-1B, 7-1C, 7-1D, 7-1E, 7-1F, 7-1G with CRC scrambled with SPS C-RNTI intended for the UE and the given serving cell, a UE shall use the value of the higher layer parameter rateMatchingMode (for each SPDCCH-PRB set), and the 'Used/Unused SPDCCH resource indication' field (if present) in the SPDCCH for determining the PDSCH RE mapping (defined in Clause 6.4 of [3]).

A UE configured with higher layer parameter csi-RS-ConfigZP-ApList for a given serving cell is configured with 4 aperiodic zero-power CSI-RS resources by higher layer signaling to decode PDSCH according to a detected PDCCH/EPDCCH with DCI format 1/1B/1D//2/2A/2B/2C/2D intended for the UE and the given serving cell. The UE shall use the aperiodic zero-power CSI-RS resource according to the value of the ' Aperiodic zero-power CSI-RS resource indicator for PDSCH RE Mapping' field (mapping defined in Table 7.1.9-2) in the detected PDCCH/EPDCCH with DCI format 1/1B/1D/2/2A/2B/2C/2D for determining the PDSCH RE mapping (defined in Clause 6.4 of [3]).

Table 7.1.9-2: Aperiodic zero-power CSI-RS resource indicator for PDSCH RE Mapping field in DCI format 1/1B/1D/2/2A/2B/2C/2D

| Value of Aperiodic zero-power CSI-RS resource indicator for PDSCH RE Mapping ' field | Description |
| --- | --- |
| '00' | Aperiodic zero-power CSI-RS resources 1 configured by higher layers |
| '01' | Aperiodic zero-power CSI-RS resources 2 configured by higher layers |
| '10' | Aperiodic zero-power CSI-RS resources 3 configured by higher layers |
| '11' | Aperiodic zero-power CSI-RS resources 4 configured by higher layers |

### 7.1.10 Antenna ports quasi co-location for PDSCH

A UE configured in transmission mode 8-10 for a serving cell may assume the antenna ports 7 – 14 of the serving cell are quasi co-located (as defined in [3]) for a given subframe with respect to delay spread, Doppler spread, Doppler shift, average gain, and average delay.

A UE configured in transmission mode 1-9 for a serving cell may assume the antenna ports 0 – 3, 5, 7 – 46 of the serving cell are quasi co-located (as defined in [3]) with respect to Doppler shift, Doppler spread, average delay, and delay spread.

A UE configured in transmission mode 10 for a serving cell is configured with one of three quasi co-location types for the serving cell by higher layer parameter qcl-Operation to decode PDSCH according to transmission scheme associated with antenna ports 7-14:

- Type A: The UE may assume the antenna ports 0 – 3, 7 – 46 of a serving cell are quasi co-located (as defined in [3]) with respect to delay spread, Doppler spread, Doppler shift, and average delay.

- Type B: The UE may assume the antenna ports 15 – 46 corresponding to the CSI-RS resource configuration identified by the higher layer parameter qcl-CSI-RS-ConfigNZPId-r11 (defined in Clause 7.1.9) and the antenna ports 7 – 14 associated with the PDSCH are quasi co-located (as defined in [3]) with respect to Doppler shift, Doppler spread, average delay, and delay spread.

- Type C: The UE may assume the antenna ports 15 – 46 corresponding to the CSI-RS resource configuration identified by the higher layer parameter qcl-CSI-RS-ConfigNZPId-r11 or qcl-CSI-RS-ConfigNZPId2-r15 (defined in Clause 7.1.9) and the antenna ports 7 – 14 associated with each PDSCH codeword are quasi co-located (as defined in [3]) with respect to Doppler shift, Doppler spread, average delay, and delay spread.

For a LAA Scell, the UE is not expected to be configured with quasi co-location type B or type C.

### 7.1.11 PDSCH subframe assignment for BL/CE UE

A BL/CE UE shall upon detection of a MPDCCH with DCI format 6-1A/6-1B/6-2 intended for the UE, decode the corresponding PDSCH in subframe(s) n+ki with i = 0, 1, …, NTBN-1 according to the MPDCCH, where

- subframe n is the last subframe in which the MPDCCH is transmitted and is determined from the starting subframe of MPDCCH transmission and the DCI subframe repetition number field in the corresponding DCI;

- the value of ![](media_svg/image319.svg) [公式≈: ^{N}TB]is the number of scheduled TB determined in the corresponding DCI if present,![](media_svg/image320.svg) [公式: N_{TB}=1] otherwise;

- the value of  is determined by the repetition number field in the corresponding DCI, where  are given in Table 7.1.11-1, Table 7.1.11-2 and Table 7.1.11-3, respectively

- if the UE is configured with higher layer parameter multiTB-Gap and the PDSCH corresponds to an MPDCCH with DCI CRC scrambled by G-RNTI,

- subframe(s) ni = n+ki with i=0,1,…, NTBN-1 are NTBN BL/CE DL subframe(s), where![](media_svg/image323.svg) [公式≈: xkkk=<<<_{011}κ_{NN}_{TB}_{−}], subframe n+x is the second BL/CE DL subframe after subframe n, and for $ i=1,\ldots  ,N\times  N_{TB}-1 $, subframe $ n_{i}$ is the first BL/CE DL subframe after subframe $ n_{i-1}+N_{gap}\times  \delta  (imodN)$, where $ N_{gap}$ is given by higher layer parameter multiTB-Gap, and $\delta  \left ( d\right ) ={\begin {matrix}1, d=0 \\ 0,d\neq  0\end {matrix}$.

- otherwise,

- subframe(s) ni = n+ki with i=0,1,…, NTBN-1 are NTBN consecutive BL/CE DL subframe(s), where ![](media_svg/image323.svg) [公式≈: xkkk=<<<_{011}κ_{NN}_{TB}_{−}], and subframe n+x is the jth BL/CE DL subframe after subframe n, and j is given by the value of the PDSCH scheduling delay option as defined in [4] if the UE is configured with CEModeA and 'PDSCH scheduling delay and HARQ-ACK delay for 14 HARQ' field is present in the corresponding DCI, j=2 otherwise.

- for ![](media_svg/image324.svg) [公式: N_{TB}>1],

- if the UE is configured with higher layer parameter interleaving in ce-PDSCH-MultiTB-Config, and PDSCH corresponding to a MPDCCH with DCI CRC scrambled by C-RNTI and ![](media_svg/image325.svg) [公式: NC>] where ![](media_svg/image326.svg) [公式: C=1] for BL/CE UE configured with CEModeA, ![](media_svg/image327.svg) [公式: C=4] for BL/CE UE configured with CEModeB,

- BL/CE DL subframes ![](media_svg/image328.svg) [公式≈: ^{n}gcNrl∪∪++(TB)] with ![](media_svg/image329.svg) [公式: lgcNCgC=−=−=0,1,1,0,1,/1,κκ] are associated with TBr+1 , ![](media_svg/image330.svg) [公式: rN=−0,1,1κ_{TB}]

- otherwise,

- BL/CE DL subframes ![](media_svg/image331.svg) [公式≈: ^{n}rNl∪+] with ![](media_svg/image332.svg) [公式: lN=−0,1,1κ] are associated with TBr+1 , ![](media_svg/image330.svg) [公式: rN=−0,1,1κ_{TB}].

For BL/CE UEs, and for a PDSCH transmission starting in subframe n+k0 without a corresponding MPDCCH, the UE shall decode the PDSCH transmission in subframe(s) n+ki with i = 0, 1, …, N-1, where

- subframe(s) n+ki with i=0,1,…,N-1 are N consecutive BL/CE DL subframe(s), where 0≤k0<k1<…,kN-1 and the value of  is determined by the repetition number field in the activation DCI, where  are given in Table 7.1.11-1, Table 7.1.11-2 and Table 7.1.11-3, respectively.

If PDSCH carrying SystemInformationBlockType1-BR is transmitted in one narrowband in subframe n+ki, a BL/CE UE shall assume any other PDSCH in the same narrowband in the subframe n+ki is dropped. If PDSCH carrying SI message is transmitted in one narrowband in subframe n+ki, a BL/CE UE shall assume any other PDSCH not carrying SystemInformationBlockType1-BR in the same narrowband in the subframe n+ki is dropped.

For single antenna port (port 0), transmit diversity and closed-loop spatial multiplexing transmission schemes, if a PDSCH is transmitted in BL/CE DL subframe n+ki and BL/CE DL subframe n+ki is configured as an MBSFN subframe, a BL/CE UE shall assume that the PDSCH in subframe n+ki is dropped.

For PDSCH assigned by MPDCCH with DCI CRC scrambled by G-RNTI and DCI Format 6-1A, the UE shall use the higher layer parameter pdsch-maxNumRepetitionCEmodeA-SC-MTCH instead of pdsch-maxNumRepetitionCEmodeA in Table 7.1.11-1.

For PDSCH assigned by MPDCCH with DCI CRC scrambled by G-RNTI and DCI Format 6-1B, the UE shall use the higher layer parameter pdsch-maxNumRepetitionCEmodeB-SC-MTCH instead of pdsch-maxNumRepetitionCEmodeB in Table 7.1.11-2.

For a BL/CE UE in half-duplex FDD operation, if the UE is configured with CEModeA, and configured with higher layer parameter ce-HARQ-AckBundling, and 'HARQ-ACK bundling flag' in the corresponding DCI is set to 1, the UE shall assume .

Table 7.1.11-1: PDSCH repetition levels (DCI Format 6-1A)

| Higher layer parameter'pdsch-maxNumRepetitionCEmodeA' |  |
| --- | --- |
| Not configured | {1,2,4,8} |
| 16 | {1,4,8,16} |
| 32 | {1,4,16,32} |

Table 7.1.11-2: PDSCH repetition levels (DCI Format 6-1B)

| Higher layer parameter'pdsch-maxNumRepetitionCEmodeB' |  |
| --- | --- |
| Not configured | {4,8,16,32,64,128,256,512} |
| 192 | {1,4,8,16,32,64,128,192} |
| 256 | {4,8,16,32,64,128,192,256} |
| 384 | {4,16,32,64,128,192,256,384} |
| 512 | {4,16,64,128,192,256,384,512} |
| 768 | {8,32,128,192,256,384,512,768} |
| 1024 | {4,8,16,64,128,256,512,1024} |
| 1536 | {4,16,64,256,512,768,1024,1536} |
| 2048 | {4,16,64,128,256,512,1024,2048} |

Table 7.1.11-3: PDSCH repetition levels (DCI Format 6-2)

| 2-bit "DCI subframe repetition number" field in DCI Format 6-2 |  |
| --- | --- |
| 00 | {1,2,4,8,16,32,64,128} |
| 01 | {4,8,16,32,64,128,192,256} |
| 10 | {32,64,128,192,256,384,512,768} |
| 11 | {192,256,384,512,768,1024,1536,2048} |

## 7.2 UE procedure for reporting Channel State Information (CSI)

If the UE is configured with a PUCCH-SCell, the UE shall apply the procedures described in this clause for both primary PUCCH group and secondary PUCCH group unless stated otherwise

When the procedures are applied for the primary PUCCH group, the terms 'secondary cell', 'secondary cells', 'serving cell', and 'serving cells' in this clause refer to secondary cell, secondary cells, serving cell or serving cells belonging to the primary PUCCH group respectively unless stated otherwise.

When the procedures are applied for secondary PUCCH group, the terms 'secondary cell', 'secondary cells', 'serving cell' and 'serving cells' in this clause refer to secondary cell, secondary cells (not including the PUCCH-SCell), serving cell, serving cells belonging to the secondary PUCCH group respectively unless stated otherwise. The term 'primary cell' in this clause refers to the PUCCH-SCell of the secondary PUCCH group.

If a UE is configured with a LAA SCell for UL transmissions, the UE shall apply the procedures described in this clause assuming frame structure type 1 for the LAA SCell unless stated otherwise.

The time and frequency resources that can be used by the UE to report CSI which consists of Channel Quality Indicator (CQI), precoding matrix indicator (PMI), precoding type indicator (PTI), CSI-RS resource indicator (CRI), and/or rank indication (RI) are controlled by the eNB. For spatial multiplexing, as given in [3], the UE shall determine a RI corresponding to the number of useful transmission layers. For transmit diversity as given in [3], RI is equal to one.

A non-BL/CE UE in transmission mode 8 or 9 is configured with or without PMI/RI reporting by the higher layer parameter pmi-RI-Report.

A UE in transmission mode 10 can be configured with one or more CSI processes per serving cell by higher layers.

For a UE in transmission mode 10,

- If a UE is not configured with higher layer parameter eMIMO-Type, each CSI process is associated with a CSI-RS resource (defined in Clause 7.2.5) and a CSI-interference measurement (CSI-IM) resource (defined in Clause 7.2.6). A UE can be configured with up to two CSI-IM resources for a CSI process if the UE is configured with CSI subframe sets  and  by the higher layer parameter csi-SubFramePatternConfig-r12 for the CSI process.

- If the UE is configured with higher layer parameter eMIMO-Type and not configured with higher layer parameter eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', each CSI process is associated with a CSI-RS resource (defined in Clause 7.2.5) and a CSI-interference measurement (CSI-IM) resource (defined in Clause 7.2.6). A UE can be configured with up to two CSI-IM resources for a CSI process if the UE is configured with CSI subframe sets  and  by the higher layer parameter csi-SubFramePatternConfig-r12 for the CSI process.

- If the UE is configured with higher layer parameter eMIMO-Type and not configured with higher layer parameter eMIMO-Type2, and eMIMO-Type is set to 'CLASS B', each CSI process is associated with one or more CSI-RS resource (defined in Clause 7.2.5) and one or more CSI-interference measurement (CSI-IM) resource (defined in Clause 7.2.6). Each CSI-RS resource is associated with a CSI-IM resource by higher layers. For a CSI process with one CSI-RS resource, a UE can be configured with CSI-IM resource for each CSI subframe sets if the UE is configured with CSI subframe sets  and  by the higher layer parameter csi-SubFramePatternConfig-r12 for the CSI process. If a UE is configured with higher layer parameter FeCoMPCSIEnabled for a CSI process, the CSI process is associated with two CSI-RS resource and one CSI-IM resource.

- If the UE is configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B', each CSI process is associated with a CSI-RS resource (defined in Clause 7.2.5) and a CSI-interference measurement (CSI-IM) resource (defined in Clause 7.2.6) for eMIMO-Type, and one CSI-RS resource (defined in Clause 7.2.5) and one CSI-interference measurement (CSI-IM) resource (defined in Clause 7.2.6) for eMIMO-Type2. A UE can be configured with up to two CSI-IM resources for each eMIMO-Type and eMIMO-Type2 of a CSI process if the UE is configured with CSI subframe sets  and  by the higher layer parameter csi-SubFramePatternConfig-r12 for the CSI process.

- If the UE is configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B', and eMIMO-Type2 is set to 'CLASS B', each CSI process is associated with more than one CSI-RS resource (defined in Clause 7.2.5) and more than one CSI-interference measurement (CSI-IM) resource (defined in Clause 7.2.6) with association of each CSI-RS resource with a CSI-IM resource by higher layers for eMIMO-Type, and one CSI-RS resource (defined in Clause 7.2.5) and one CSI-interference measurement (CSI-IM) resource (defined in Clause 7.2.6) for eMIMO-Type2.

For a UE in transmission mode 10, a CSI reported by the UE corresponds to a CSI process configured by higher layers. Each CSI process can be configured with or without PMI/RI reporting by higher layer signalling.

If a UE is configured with a serving cell with frame structure 3, the UE is not required to update measurements for more than 5 CSI processes in a subframe, in case the total number of serving cells is no more than 5. If a UE is configured with more than 5 serving cells, the UE is not required to update measurements for more than  CSI processes in a subframe, where the value of  is given by

- maxNumberUpdatedCSI-Proc-r13 if the UE is configured with a serving cell with frame structure 3

- maxNumberUpdatedCSI-Proc-SPT-r15if the UE is configured with higher layer parameter shortProcessingTime

If a UE is configured with the higher layer parameter shortTTI, the UE is not required to update measurements for more than  CSI processes in a DL

- slot, where the value of  is given by maxNumberUpdatedCSI-Proc-STTI-Comb77-r15 if the higher layer parameter dl-TTI-Length is set to 'slot' and if the higher layer parameter ul-TTI-Length is set to 'slot'.

- subslot, where the value of  is given by maxNumberUpdatedCSI-Proc-STTI-Comb27-r15 if the higher layer parameter dl-TTI-Length is set to 'subslot' and if the higher layer parameter ul-TTI-Length is set to 'slot'.

- subslot, where the value of  is given by maxNumberUpdatedCSI-Proc-STTI-Comb22-Set1-r15 if the higher layer parameter dl-TTI-Length is set to 'subslot' and if the higher layer parameter ul-TTI-Length is set to 'subslot' and if proc-Timeline-r15 is set to 'nplus4set1' or 'nplus6set1'.

- subslot, where the value of  is given by maxNumberUpdatedCSI-Proc-STTI-Comb22-Set2-r15 if the higher layer parameter dl-TTI-Length is set to 'subslot' and if the higher layer parameter ul-TTI-Length is set to 'subslot' and if proc-Timeline-r15 is set to 'nplus6set2' or 'nplus8set2'.

For UE in transmission mode 9 and the UE configured with higher layer parameter eMIMO-Type, the term 'CSI process' in this Clause refers to the CSI configured for the UE.

For a UE in transmission mode 9, and if the UE is configured with higher layer parameter eMIMO-Type, and,

- UE is not configured with higher layer parameter eMIMO-Type2 and eMIMO-Type is set to 'CLASS A', each CSI process is associated with a CSI-RS resource (defined in Clause 7.2.5).

- UE is not configured with higher layer parameter eMIMO-Type2 and eMIMO-Type is set to 'CLASS B', each CSI process is associated with one or more CSI-RS resource (defined in Clause 7.2.5).

- UE is configured with higher layer parameter eMIMO-Type2 and eMIMO-Type is set to 'CLASS A' and eMIMO-Type2 is set to 'CLASS B', each CSI process is associated with a CSI-RS resource (defined in Clause 7.2.5) for eMIMO-Type, and a CSI-RS resource (defined in Clause 7.2.5) for eMIMO-Type2.

- UE is configured with higher layer parameter eMIMO-Type2 and eMIMO-Type is set to 'CLASS B' and eMIMO-Type2 is set to 'CLASS B', each CSI process is associated with more than one CSI-RS resource (defined in Clause 7.2.5) for eMIMO-Type, and a CSI-RS resource (defined in Clause 7.2.5) for eMIMO-Type2.

For a CSI process, and if a UE is configured in transmission mode 9 or 10, and UE is not configured with higher layer parameter pmi-RI-Report, and UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and the number of CSI-RS antenna ports in at least one of the one or more configured CSI-RS resource is more than one, the UE is considered to be configured without PMI reporting.

For a UE configured in transmission mode 9 or 10, UE is not expected to be configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and more than one CSI-RS resource configured, and the number of CSI-RS resource configured with one antenna port is not equal to total number number of CSI-RS resources associated with the CSI process.

A UE is configured with resource-restricted CSI measurements if the subframe sets  and  are configured by higher layers. A UE can also be configured with resource restricted CSI measurements for dormant serving cells with subframe sets CCSI,0-dormant and CCSI,1-dormant. If the UE is configured with resource restricted CSI measurements for dormant serving cells, ![](media_svg/image337.svg) [公式≈: ^{C}CSI,0] and ![](media_svg/image338.svg) [公式≈: ^{C}CSI,1] in this clause refer to ![](media_svg/image337.svg) [公式≈: ^{C}CSI,0] and ![](media_svg/image338.svg) [公式≈: ^{C}CSI,1] for activated serving cells, and to CCSI,0-dormant and CCSI,1-dormant for dormant serving cells.

For a serving cell with frame structure type 1, a UE is not expected to be configured with csi-SubframePatternConfig-r12.

CSI reporting is periodic or aperiodic.

A BL/CE UE configured with CEModeB is not expected to be configured with either aperiodic CSI or periodic CSI reporting.

If the UE is configured with more than one serving cell, it transmits aperiodic CSI for activated serving cell(s) only, and periodic CSI for activated and/or dormant serving cell(s) only.

If a UE is not configured for simultaneous PUSCH and PUCCH transmission, it shall transmit periodic CSI reporting on PUCCH as defined hereafter in subframes with no PUSCH allocation.

If a UE is not configured for simultaneous PUSCH and PUCCH transmission, it shall transmit periodic CSI reporting on PUSCH of the serving cell with smallest ServCellIndex as defined hereafter in subframes with a PUSCH allocation, where the UE shall use the same PUCCH-based periodic CSI reporting format on PUSCH.

A UE shall transmit aperiodic CSI reporting on PUSCH if the conditions specified hereafter are met. For aperiodic CQI/PMI reporting, RI reporting is transmitted only if the configured CSI feedback type supports RI reporting.

Table 7.2-1: Void

In case both periodic and aperiodic CSI reporting would occur in the same subframe, the UE shall only transmit the aperiodic CSI report in that subframe. If the aperiodic CSI reporting occurs on an LAA SCell, the UE shall assume that the UL channel access procedure, as described in clause 4.2 of [13], is successful to determine whether periodic and aperiodic CSI reporting would occur in the same subframe.

If the higher layer parameter altCQI-TableSTTI-r15 is configured and is set to allSubframes and aperiodic CSI is triggered through DCI format 7-0A or 7-0B,

- the UE shall report CQI according to Table 7.2.3-2.

Else if the higher layer parameter altCQI-Table1024QAM-STTI-r15 is configured and is set to allSubframes and aperiodic CSI is triggered through DCI format 7-0A or 7-0B,

- the UE shall report CQI according to Table 7.2.3-4.

Else if the higher layer parameter altCQI-TableSTTI-r15 is configured and is set to csi-SubframeSet1 or csi-SubframeSet2 and aperiodic CSI is triggered through DCI format 7-0A or 7-0B,

- the UE shall report CQI according to Table 7.2.3-2 for the corresponding CSI subframe set configured by altCQI-TableSTTI-r15

- the UE shall report CQI for the other CSI subframe set according to Table 7.2.3-1.

Else if the higher layer parameter altCQI-Table1024QAM-STTI-r15 is configured and is set to csi-SubframeSet1 or csi-SubframeSet2 and aperiodic CSI is triggered through DCI format 7-0A or 7-0B,

- the UE shall report CQI according to Table 7.2.3-4 for the corresponding CSI subframe set configured by altCQI-Table1024QAM-STTI-r15

- the UE shall report CQI for the other CSI subframe set according to Table 7.2.3-1.

Else if aperiodic CSI is triggered through DCI format 7-0A or 7-0B,

the UE shall report CQI according to Table 7.2.3-1.

Else if the higher layer parameter altCQI-Table-r12 is configured and is set to allSubframes,

- the UE shall report CQI according to Table 7.2.3-2.

Else if the higher layer parameter altCQI-Table-1024QAM-r15 is configured and is set to allSubframes

- the UE shall report CQI according to Table 7.2.3-4.

Else if the higher layer parameter altCQI-Table-r12 is configured and is set to csi-SubframeSet1 or csi-SubframeSet2,

- the UE shall report CQI according to Table 7.2.3-2 for the corresponding CSI subframe set configured by altCQI-Table-r12

- the UE shall report CQI for the other CSI subframe set according to Table 7.2.3-1.

Else if the higher layer parameter altCQI-Table-1024QAM-r15 is configured and is set to csi-SubframeSet1 or csi-SubframeSet2,

- the UE shall report CQI according to Table 7.2.3-4 for the corresponding CSI subframe set configured by altCQI-Table-1024QAM-r15

- the UE shall report CQI for the other CSI subframe set according to Table 7.2.3-1.

Else

- the UE shall report CQI according to Table 7.2.3-1.

For a BL/CE UE, if the UE is configured with higher layer parameter ce-PDSCH-64QAM-Config-r15 and the higher layer parameter csi-NumRepetitionCE-r13 indicates more than one subframe, or if the UE is configured with higher layer parameter ce-CQI-AlternativeTableConfig-r15,

- the UE shall report CQI according to Table 7.2.3-6.

- if the UE is not capable of supporting 64QAM in PDSCH, or the UE is configured with higher layer parameter mpdcch-pdsch-HoppingConfig-r13 set to 'on' and the UE is calculating CQI for a wideband CSI report, the reported CQI < 13.

Else if the higher layer parameter ce-PDSCH-64QAM-Config-r15 is configured,

- the UE shall report CQI according to Table 7.2.3-5.

- if the UE is configured with higher layer parameter mpdcch-pdsch-HoppingConfig-r13 set to 'on' and the UE is calculating CQI for a wideband CSI report, the reported CQI < 11.

Else

- the UE shall report CQI according to Table 7.2.3-3 with CQI index between 1 and 10.

For a non-BL/CE UE, when reporting RI the UE reports a single instance of the number of useful transmission layers. For each RI reporting interval when the UE is configured in transmission modes 4 or when the UE is configured in transmission mode 8, 9 or 10 with PMI/RI reporting, a UE shall determine a RI from the supported set of RI values as defined in Clause 5.2.2.6 of [4] and report the number in each RI report. For each RI reporting interval when the UE is configured in transmission mode 3, a UE shall determine RI as defined in Clause 5.2.2.6 of [4] in each reporting interval and report the detected number in each RI report to support selection between transmit diversity and large delay CDD.

For a UE configured in transmission mode 9 or 10, when reporting CRI the UE reports a single instance of one or more selected CSI-RS resource(s). For each CRI reporting interval, when a UE is configured in transmission mode 10 with higher layer parameter FeCoMPCSIEnabled and determines CRI=2 from the supported set of CRI values as defined in Clause 5.2.2.6 of [4], the UE reports the CRI=2 in each CRI report, where CRI value 2 corresponds to the configured two CSI-RS resources and one CSI-IM resource. Otherwise, when a UE is configured with higher layer parameter eMIMO-Type, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one for a CSI process, the UE shall determine a CRI from the supported set of CRI values as defined in Clause 5.2.2.6 of [4] and report the number in each CRI report, where CRI value 0 corresponds to the configured csi-RS-ConfigNZPId, first entry of csi-IM-ConfigIdList, first entry of p-C-AndCBSR-PerResourceConfigList, and alternativeCodebookEnabledFor4TXProc, and CRI value k (k>0) corresponds to the configured k-th entry of csi-RS-ConfigNZPIdListExt, (k+1)-th entry of csi-IM-ConfigIdList, (k+1)-th entry of p-C-AndCBSR-PerResourceConfigList, and k-th entry of ace-For4Tx-PerResourceConfigList.

For a UE configured in transmission mode 9 or 10, when reporting CRI the UE reports a single instance of one or more selected CSI-RS resource(s). For each CRI reporting interval, when a UE is configured in transmission mode 10 with higher layer parameter FeCoMPCSIEnabled and determines CRI=2 from the supported set of CRI values as defined in Clause 5.2.2.6 of [4], the UE reports the CRI=2 in each CRI report, where CRI value 2 corresponds to the configured two CSI-RS resources and one CSI-IM resource. Otherwise, when a UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and high layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one for a CSI process, the UE shall determine a CRI from the supported set of CRI values as defined in clause 5.2.2.6 of [4] and report the number in each CRI report, where, if csi-RS-ConfigNZPId is activated, CRI value 0 corresponds to the activated csi-RS-ConfigNZPId, first entry of csi-IM-ConfigIdList, p-C-AndCBSR-PerResourceConfigList, and alternativeCodebookEnabledFor4TXProc, and CRI value k (k>0) corresponds to the (k+1)-th activated CSI-RS resource, which is associated with l-th entry of csi-RS-ConfigNZPIdListExt, (l+1)-th entry of csi-IM-ConfigIdList, (l+1)-th entry of p-C-AndCBSR-PerResourceConfigList, and l-th entry of ace-For4Tx-PerResourceConfigList; If csi-RS-ConfigNZPId is not activated, CRI value k corresponds to the (k+1)-th activated CSI-RS resource, which is associated with l-th entry of csi-RS-ConfigNZPIdListExt, (l+1)-th entry of csi-IM-ConfigIdList, (l+1)-th entry of p-C-AndCBSR-PerResourceConfigList, and l-th entry of ace-For4Tx-PerResourceConfigList.

For a non-BL/CE UE, when reporting PMI the UE reports either a single or a multiple PMI report. The number of RBs represented by a single UE PMI report can be  or a smaller subset of RBs. The number of RBs represented by a single PMI report is semi-statically configured by higher layer signalling. A UE is restricted to report PMI, RI and PTI on a subframe-PUCCH/PUSCH within a precoder codebook subset specified by one or more bitmap parameter(s) codebookSubsetRestriction, codebookSubsetRestriction-1, codebookSubsetRestriction-2, codebookSubsetRestriction-3, codebookSubsetRestriction-4 configured by higher layer signalling. If a UE is configured by higher-layer parameter shortTTI, the UE is restricted to report PMI, RI and PTI on subslot/slot-based PUSCH within a precoder codebook subset specified by a bitmap parameter codebookSubsetRestriction, configured by higher layer signalling for the subslot/slot-based transmission.

For a UE configured in transmission mode 10 and the UE not configured with higher layer parameter eMIMO-Type for a CSI process, or for a UE configured in transmission mode 9 or 10 and the UE configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured for a CSI process, the bitmap parameter codebookSubsetRestriction is configured for each CSI process and each subframe sets (if subframe sets  and  are configured by higher layers) by higher layer signaling.

For a UE configured in transmission mode 9 or 10 and for a CSI process and the UE configured with higher layer parameter eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B', and one CSI-RS resource configured and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured for eMIMO-Type2 of the CSI process, the bitmap parameter codebookSubsetRestriction is configured for eMIMO-Type2 of each CSI process and each subframe sets (if subframe sets  and  are configured by higher layers) by higher layer signaling.

For a UE configured in transmission mode 9 or 10, and for a CSI process and UE configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', except when the UE is configured with higher layer parameter advancedCodebookEnabled and advancedCodebookEnabled is set to 'TRUE', the bitmap parameters codebookSubsetRestriction-1, codebookSubsetRestriction-2 is configured for the CSI process and each subframe sets (if subframe sets  and  are configured by higher layers) by higher layer signaling.

For a UE configured in transmission mode 9 or 10, and for a CSI process and UE configured with higher layer parameter advancedCodebookEnabled and advancedCodebookEnabled is set to 'TRUE', and the UE is configured   with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', and the UE is configured with 8, 12, 16, 20, 24, 28, and 32 antenna ports, the UE is either configured with bitmap parameter codebookSubsetRestriction-1, or, the UE is configured with bitmap parameter  codebookSubsetRestriction-4 for the CSI process and each subframe sets (if subframe sets ![](media_svg/image337.svg) [公式≈: ^{C}CSI,0] and ![](media_svg/image338.svg) [公式≈: ^{C}CSI,1] are configured by higher layers) by higher layer signaling.

For a UE configured in transmission mode 9 or 10, and for a CSI process and UE configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE, the bitmap parameter codebookSubsetRestriction-3 is configured for the CSI process and each subframe sets (if subframe sets  and  are configured by higher layers) by higher layer signaling.

For a UE configured in transmission mode 9 or 10, and for a CSI process and the UE configured with higher layer parameter eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE for eMIMO-Type2 of the CSI process, the bitmap parameter codebookSubsetRestriction-3 is configured for eMIMO-Type2 of the CSI process and each subframe sets (if subframe sets  and  are configured by higher layers) by higher layer signaling.

For a UE configured in transmission mode 9 or 10, and for a CSI process and UE configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and more than one CSI-RS resource configured, the bitmap parameter codebookSubsetRestriction is configured for each CSI-RS resource of the CSI process and each subframe sets (if subframe sets  and  are configured by higher layers) by higher layer signaling.

For a specific precoder codebook and associated transmission mode, the bitmap can specify all possible precoder codebook subsets from which the UE can assume the eNB may be using when the UE is configured in the relevant transmission mode. Codebook subset restriction is supported for transmission modes 3, 4, 5, 6 and for transmission modes 8, 9 and 10 with PMI/RI reporting, and transmission mode 9 and 10 without PMI reporting. The resulting number of bits for each transmission mode are given in Table 7.2-1b, Table 7.2-1d, Table 7.2-1e, and Table 7.2-1f. The bitmap parameter codebookSubsetRestriction, codebookSubsetRestriction-1 or codebookSubsetRestriction-3 forms the bit sequence where  is the LSB and is the MSB and where a bit value of zero indicates that the PMI and RI reporting is not allowed to correspond to precoder(s) associated with the bit. The bitmap parameter codebookSubsetRestriction-2 forms the bit sequence where  is the LSB and is the MSB and where a bit value of zero indicates that the PMI and RI reporting is not allowed to correspond to precoder(s) associated with the bit. The association of bits to precoders for the relevant transmission modes are given as follows:

1. Transmission mode 3

a. 2 antenna ports: bit is associated with the precoder in Table 6.3.4.2.3-1 of [3] corresponding to  layers and codebook index 0 while bit  is associated with the precoder for 2 antenna ports in Clause 6.3.4.3 of [3].

b. 4 antenna ports: bit is associated with the precoders in Table 6.3.4.2.3-2 of [3] corresponding to  layers and codebook indices 12, 13, 14, and 15 while bit  is associated with the precoder for 4 antenna ports in Clause 6.3.4.3 of [3].

2. Transmission mode 4

a. 2 antenna ports: see Table 7.2-1c

b. 4 antenna ports: bit  is associated with the precoder for  layers and with codebook index in Table 6.3.4.2.3-2 of [3].

3. Transmission modes 5 and 6

a. 2 antenna ports: bit  is associated with the precoder for  layer with codebook index in Table 6.3.4.2.3-1 of [3].

b. 4 antenna ports: bit  is associated with the precoder for  layer with codebook index in Table 6.3.4.2.3-2 of [3].

4. Transmission mode 8

a. 2 antenna ports: see Table 7.2-1c

b. 4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE configured: bit  is associated with the precoder for  layers and with codebook index in Table 6.3.4.2.3-2 of [3], .

c. 4 antenna ports with alternativeCodeBookEnabledFor4TX-r12=TRUE configured: bit  is associated with the precoder for  layers () and codebook index  and bit  is associated with the precoder for  layers () and codebook index. Codebook indices  and  are given in Table 7.2.4-0A or 7.2.4-0B, for =1 or 2 respectively.

5. Transmission modes 9 and 10

a. 2 antenna ports except when a UE configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE for a CSI process, or when a UE configured with higher layer parameter eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE for eMIMO-Type2 of a CSI process: see Table 7.2-1c

b. 4 antenna ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE configured or for a CSI process the UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE or for a CSI process the UE is configured with higher layer parameter eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE for eMIMO-Type2 of a CSI process: bit  is associated with the precoder for  layers and with codebook index in Table 6.3.4.2.3-2 of [3].

c. 4 antenna ports with alternativeCodeBookEnabledFor4TX-r12=TRUE configured except when a UE configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE for a CSI process, or when a UE configured with higher layer parameter eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE for eMIMO-Type2 of a CSI process: bit is associated with the precoder for  layers () and codebook index  and bit is associated with the precoder for  layers () and codebook index. Codebook indices  and  are given in Table 7.2.4-0A, 7.2.4-0B, 7.2.4-0C or 7.2.4-0D, for =1,2,3 or 4 respectively.

d. 8 antenna ports except when a UE configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', or for when a UE configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE for a CSI process, or for when a UE configured with higher layer parameter eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE for eMIMO-Type2 of a CSI process: bit is associated with the precoder for  layers () and codebook index  where and bit is associated with the precoder for  layers () and codebook index  where . Codebook indices  and  are given in Table 7.2.4-1, 7.2.4-2, 7.2.4-3, 7.2.4-4, 7.2.4-5, 7.2.4-6, 7.2.4-7, or 7.2.4-8, for =1,2,3,4,5,6,7, or 8 respectively.

e. 8, 12, 16, 20, 24, 28, and 32 antenna ports and for a CSI process the UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A': bit  is associated with the precoder based on the quantity ,  and bit  is associated with the precoder for  layers (). The quantity  is defined in Clause 7.2.4. Bit  is associated with the precoder for  layers () and codebook index  where  is given in Table 7.2-1g. Codebook index  is given in Table 7.2.4-10, 7.2.4-11, 7.2.4-12, 7.2.4-13, 7.2.4-14, 7.2.4-15, 7.2.4-16, or 7.2.4-17, for =1,2,3,4,5,6,7, or 8 respectively.

f. 2, 4, or 8 antenna ports and for a CSI process the UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE, or the UE is configured with higher layer parameter eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE for eMIMO-Type2 of the CSI process: bit  is associated with the precoder for  layers and codebook index where  and  for 2 antenna ports,  and  for 4 antenna ports, and  and  for 8 antenna ports. Codebook index  is given in Table 7.2.4-18, 7.2.4-19, or 7.2.4-20, for 2, 4, or 8 antenna ports respectively.

g. 8, 12, 16, 20, 24, 28, and 32 antenna ports and for a CSI process the UE is configured with higher layer parameter advancedCodebookEnabled and advancedCodebookEnabled is set to 'TRUE', and the UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', and the UE is configured with bitmap parameter codebookSubsetRestriction-1: bit  is associated with the precoder based on the quantity ,  and bit  is associated with the precoder for  layers (). The quantity  is defined in Clause 7.2.4.

h. 8, 12, 16, 20, 24, 28, and 32 antenna ports and for a CSI process the UE is configured with higher layer parameter advancedCodebookEnabled and advancedCodebookEnabled is set to 'TRUE', and the UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', and the UE is configured with bitmap parameter codebookSubsetRestriction-4:  The bitmap parameter codebookSubsetRestriction-4 forms the bit sequence , consisting of  bits, where  is the LSB and is the MSB. The bit pair is associated with the group of quantities  for  if  and  for  if  and the bit  is associated with the precoder for  layers (). The quantity  is defined in Clause 7.2.4.

i For =1,2 layer reporting, PMI reporting is not allowed to correspond to a precoder where any quantity  from the group of quantities  is selected by the codebook indices  , unless the corresponding bit pair

ii For =1,2 layer reporting, PMI reporting is not allowed to correspond to a precoder where any quantity  from the group of quantities  is selected by the codebook index  , if the relative power indicator (RPI),  is larger than the maxmimum allowed value according to Table 7.2-1h.

iii For =3,4,5,6,7,8 layer reporting, PMI reporting is not allowed to correspond to a precoder where any quantity  from the group of quantities   is associated with the precoder, unless the corresponding bit pair .

For a BL/CE UE, when reporting PMI the UE reports a single PMI report. A UE is restricted to report PMI within a precoder codebook subset specified by a bitmap parameter codebookSubsetRestriction configured by higher layer signalling. For a specific precoder codebook and associated transmission mode, the bitmap can specify all possible precoder codebook subsets from which the UE can assume the eNB may be using when the UE is configured in the relevant transmission mode. Codebook subset restriction is supported for transmission modes 6 and 9. The resulting number of bits for each transmission mode is given in Table 7.2-1b. The bitmap forms the bit sequence  where  is the LSB and  is the MSB and where a bit value of zero indicates that the PMI reporting is not allowed to correspond to precoder(s) associated with the bit. The association of bits to precoders for the relevant transmission modes are given as follows:

- Transmission mode 6

- 2 antenna ports: bit  is associated with the precoder for  layer with codebook index in Table 6.3.4.2.3-1 of [3].

- 4 antenna ports: bit  is associated with the precoder for  layer with codebook index in Table 6.3.4.2.3-2 of [3].

- Transmission mode 9

- 2 antenna ports: bit  is associated with the precoder for  layer with codebook index in Table 6.3.4.2.3-1 of [3].

- 4 antenna ports: bit  is associated with the precoder for  layer and with codebook index in Table 6.3.4.2.3-2 of [3].

- 8 antenna ports: bit $ a_{i_{1}}$ is associated with the precoder for  layer and codebook index , and bit $ a_{53+i_{2}}$ is associated with the precoder for  layer and codebook index . Codebook indices  and  are given in Table 7.2.4-1. The 8 antenna ports case for Transmission mode 9 is only applicable when the UE is configured with the higher layer parameter ce-CSI-RS-Feedback.

Table 7.2-1b: Number of bits in codebook subset restriction codebookSubsetRestriction bitmap for applicable transmission modes

|  | Number of bits |  |  |
| --- | --- | --- | --- |
|  | 2 antenna ports | 4 antenna ports | 8 antenna ports |
| Transmission mode 3 | 2 | 4 |  |
| Transmission mode 4 | 6 | 64 |  |
| Transmission mode 5 | 4 | 16 |  |
| Transmission mode 6 | 4 | 16 |  |
| Transmission mode 8 | 6 | 64 with alternativeCodeBookEnabledFor4TX-r12=TRUE configured, otherwise 32 |  |
| Transmission modes 9 and 10 | 6 | 96 with alternativeCodeBookEnabledFor4TX-r12=TRUE configured, otherwise 64 | 109 |

Table 7.2-1c: Association of bits in codebookSubSetRestriction bitmap to precoders in the 2 antenna port codebook of Table 6.3.4.2.3-1 in [3]

| Codebook index | Number of layers |  |
| --- | --- | --- |
|  | 1 | 2 |
| 0 | a0 | - |
| 1 | a1 | a4 |
| 2 | a2 | a5 |
| 3 | a3 | - |

Table 7.2-1d: Number of bits in codebook subset restriction codebookSubsetRestriction1 bitmap for applicable transmission modes

|  | Number of bits |
| --- | --- |
| Transmission modes 9 and 10 |  |
|  |  |

Table 7.2-1e: Number of bits in codebook subset restriction codebookSubsetRestriction2 bitmap for applicable transmission modes

|  | Value of codebookConfig | Number of bits |
| --- | --- | --- |
| Transmission modes 9 and 10 | 1 | 12 |
|  | 2 | 56 |
|  | 3 | 56 |
|  | 4 | 56 |

Table 7.2-1f: Number of bits in codebook subset restriction codebookSubsetRestriction3 bitmap for applicable transmission modes

|  | Number of bits |  |  |
| --- | --- | --- | --- |
|  | 2 antenna ports | 4 antenna ports | 8 antenna ports |
| Transmission modes 9 and 10 | 6 | 22 | 60 |

Table 7.2-1g:  for a CSI process with eMIMO-Type set to 'CLASS A'

| Value of codebookConfig |  |
| --- | --- |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 |  |

Table 7.2-1h: Maximum value of relative power indicator for restricted ![](media_svg/image387.svg) [公式≈: ^{v}l,m] quantities

| Value of bit pair ![](media_svg/image404.svg) [公式≈: ^{{,}}^{aa}2()2()1NnnNnn_{212212}+++] | Maximum value of Relative Power Indicator ![](media_svg/image416.svg) [公式≈: ^{I}p] |
| --- | --- |
|  |  |
| '00' | 0 |
| '01' | 1 |
| '10' | 2 |
| '11' | 3 |

For a non-BL/CE UE, the set of subbands (S) a UE shall evaluate for CQI reporting spans the entire downlink system bandwidth. A subband is a set of k contiguous PRBs where k is a function of system bandwidth. Note the last subband in set S may have fewer than k contiguous PRBs depending on . The number of subbands for system bandwidth given by is defined by. The subbands shall be indexed in the order of increasing frequency and non-increasing sizes starting at the lowest frequency.

- For transmission modes 1, 2, 3 and 5, as well as transmission modes 8, 9 and 10 without PMI/RI reporting, transmission mode 4 with RI=1, transmission modes 8, 9 and 10 with PMI/RI reporting and RI=1, and transmission modes 9 and 10 without PMI reporting and RI=1, a single 4-bit wideband CQI is reported.

- For transmission modes 3 and 4, as well as transmission modes 8, 9 and 10 with PMI/RI reporting, and transmission modes 9 and 10 without PMI reporting, CQI is calculated assuming transmission of

- one codeword for slot/subslot-PUSCH based triggered reporting,

- one codeword for RI=1 and two codewords for RI > 1.

- For RI > 1 with transmission mode 4, as well as transmission modes 8, 9 and 10 with PMI/RI reporting, and transmission modes 9 and 10 without PMI reporting, PUSCH based triggered reporting includes reporting a wideband CQI which comprises:

- A 4-bit wideband CQI for codeword 0

- A 4-bit wideband CQI for codeword 1 for subframe-PUSCH based triggered reporting

- For RI > 1 with transmission mode 4, as well as transmission modes 8, 9 and 10 with PMI/RI reporting, and transmission modes 9 and 10 without PMI reporting, PUCCH based reporting includes reporting a 4-bit wideband CQI for codeword 0 and a wideband spatial differential CQI. The wideband spatial differential CQI value comprises:

- A 3-bit wideband spatial differential CQI value for codeword 1 offset level

- Codeword 1 offset level = wideband CQI index for codeword 0 – wideband CQI index for codeword 1.

- The mapping from the 3-bit wideband spatial differential CQI value to the offset level is shown in Table 7.2-2.

Table 7.2-2 Mapping spatial differential CQI value to offset level

| Spatial differential CQI value | Offset level |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | -4 |
| 5 | -3 |
| 6 | -2 |
| 7 | -1 |

### 7.2.1 Aperiodic CSI Reporting using PUSCH

The term "UL/DL configuration" in this Clause refers to the higher layer parameter subframeAssignment unless specified otherwise.

A non-BL/CE UE shall perform aperiodic CSI reporting using the PUSCH in subframe/slot/subslot n+k on serving cell , upon decoding in subframe/slot/subslot n either:

- an uplink DCI format [4], or

- a Random Access Response Grant,

for serving cell  if the respective CSI request field is set to trigger a report and is not reserved. If the CSI request field from an uplink DCI format 7-0A/7-0B is set to trigger a report, the reported CSI shall be according to the transmission mode configured by higher layers for the subframe where the trigger was received. The UE is not expected to receive a CSI request field set to trigger a report in a DCI indicating a PUSCH transmission in UpPTS.

For a serving cell that is a LAA SCell, aperiodic CSI reporting using the PUSCH in subframe n+k is conditioned on if the UE is allowed to transmit in the subframe according to the channel access procedures described in clause 4.2.1 of [13].

For a serving cell ![](media_svg/image429.svg) [公式: c] that is a LAA SCell, a UE configured with Partial PUSCH mode 1 is not expected to receive an aperiodic CSI report request triggering a CSI report without UL-SCH.

A BL/CE UE shall perform aperiodic CSI reporting using the PUSCH upon decoding either:

- an uplink DCI format [4], or

- a Random Access Response Grant,

for serving cell  if the respective CSI request field is set to trigger a report and is not reserved. The subframe(s) in which the PUSCH carrying the corresponding aperiodic CSI reporting triggered by an UL DCI format is transmitted is determined according to Clause 8.0.

If the CSI request field is 1 bit and the UE is configured in transmission mode 1-9 and the UE is not configured with csi-SubframePatternConfig-r12 for any serving cell, a report is triggered for serving cell , if the CSI request field is set to '1'. If the UE is configured with higher layer parameter eMIMO-Type2 for the aperiodic CSI on the serving cell , the report is for a higher layer configured eMIMO type of the aperiodic CSI configured for the UE on the serving cell . If the UE is configured with higher layer parameter csi-RS-ConfigNZP-ApList and the number of activated CSI-RS resources given by the higher layer parameter numberActivatedAperiodicCSI-RS-Resources is set to '1' for the serving cell , the report is for the activated CSI-RS resource for the serving cell .

If the CSI request field is 1 bit and the UE is configured in transmission mode 10 and the UE is not configured with csi-SubframePatternConfig-r12 for any serving cell, a report is triggered for a set of CSI process(es) for serving cell  corresponding to the higher layer configured set of CSI process(es) associated with the value of CSI request field of '01' in Table 7.2.1-1B, if the CSI request field is set to '1'. If the UE is configured with higher layer parameter eMIMO-Type2 for a CSI process of the triggered set of CSI process(es), the report is for a higher layer configured eMIMO type associated with the value of CSI request field of '01' for the CSI process. If the UE is configured with higher layer parameter csi-RS-ConfigNZP-ApList and the number of activated CSI-RS resources given by the higher layer parameter numberActivatedAperiodicCSI-RS-Resources is set to '1' for a CSI process of the triggered set of CSI process(es), the report is for the activated CSI-RS resource for the CSI process.

If the CSI request field size is 2 bits and the UE is configured in transmission mode 1-9 for all serving cells and the UE is not configured with csi-SubframePatternConfig-r12 for any serving cell, a report is triggered according to the value in Table 7.2.1-1A corresponding to aperiodic CSI reporting. If the UE is configured with higher layer parameter eMIMO-Type2 for the aperiodic CSI on a serving cell of the triggered set of serving cells, the report is for a higher layer configured eMIMO type associated with the value of CSI request field of the aperiodic CSI configured for the UE on the serving cell. If the UE is configured with higher layer parameter csi-RS-ConfigNZP-ApList and the number of activated CSI-RS resources given by the higher layer parameter numberActivatedAperiodicCSI-RS-Resources is set to '1' for a serving cell of the triggered set of serving cells, the report is for the activated CSI-RS resource for the serving cell.

If the CSI request field size is 2 bits and the UE is configured in transmission mode 10 for at least one serving cell and the UE is not configured with csi-SubframePatternConfig-r12 for any serving cell, a report is triggered according to the value in Table 7.2.1-1B corresponding to aperiodic CSI reporting. If the UE is configured with higher layer parameter eMIMO-Type2 a CSI process of the triggered set of CSI process(es), the report is for a higher layer configured eMIMO type associated with the value of CSI request field for the CSI process. If the UE is configured with higher layer parameter csi-RS-ConfigNZP-ApList and the number of activated CSI-RS resources given by the higher layer parameter numberActivatedAperiodicCSI-RS-Resources is set to '1' for a serving cell of the triggered set of serving cells, the report is for the activated CSI-RS resource for the serving cell.

If the CSI request field is 1 bit and the UE is configured with the higher layer parameter csi-SubframePatternConfig-r12 for at least one serving cell, a report is triggered for a set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) for serving cell  corresponding to the higher layer configured set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) associated with the value of CSI request field of '01' in Table 7.2.1-1C, if the CSI request field is set to '1'. If the UE is configured with higher layer parameter eMIMO-Type2 for a CSI process of the triggered set of CSI process(es) for serving cell , the report is for a higher layer configured eMIMO type associated with the value of CSI request field of '01' for the CSI process for serving cell . If the UE is configured with higher layer parameter csi-RS-ConfigNZP-ApList and the number of activated CSI-RS resources given by the higher layer parameter numberActivatedAperiodicCSI-RS-Resources is set to '1' for a CSI process of the triggered set of CSI process(es), the report is for the activated CSI-RS resource for the CSI process for the serving cell .

If the CSI request field size is 2 bits and the UE is configured with the higher layer parameter csi-SubframePatternConfig-r12 for at least one serving cell, a report is triggered according to the value in Table 7.2.1-1C corresponding to aperiodic CSI reporting. If the UE is configured with higher layer parameter eMIMO-Type2 for a CSI process of the triggered set of CSI process(es), the report is for a higher layer configured eMIMO type associated with the value of CSI request field for the CSI process. If the UE is configured with higher layer parameter csi-RS-ConfigNZP-ApList and the number of activated CSI-RS resources given by the higher layer parameter numberActivatedAperiodicCSI-RS-Resources is set to '1' for a CSI process of the triggered set of CSI process(es), the report is for the activated CSI-RS resource for the CSI process.

If the CSI request field size is 3 bits and the UE is not configured with the higher layer parameter csi-SubframePatternConfig-r12 for any serving cell, and UE is not configured with higher layer parameter csi-RS-ConfigNZP-ApList or UE is configured with higher layer parameter csi-RS-ConfigNZP-ApList and the number of activated CSI-RS resources given by the higher layer parameter numberActivatedAperiodicCSI-RS-Resources is set to '1' for each CSI process, a report is triggered according to the value in Table 7.2.1-1D corresponding to aperiodic CSI reporting. If the UE is configured with higher layer parameter eMIMO-Type2 for a CSI process of the triggered set of CSI process(es), the report is for a higher layer configured eMIMO type associated with the value of CSI request field for the CSI process. If the UE is configured with higher layer parameter csi-RS-ConfigNZP-ApList and the number of activated CSI-RS resources given by the higher layer parameter numberActivatedAperiodicCSI-RS-Resources is set to '1' for a CSI process of the triggered set of CSI process(es), the report is for the activated CSI-RS resource for the CSI process.

If the CSI request field size is 3 bits and the UE is configured with the higher layer parameter csi-SubframePatternConfig-r12 for at least one serving cell, and UE is not configured with higher layer parameter csi-RS-ConfigNZP-ApList or UE is configured with higher layer parameter csi-RS-ConfigNZP-ApList and the number of activated CSI-RS resources given by the higher layer parameter numberActivatedAperiodicCSI-RS-Resources is set to '1' for each CSI process, a report is triggered according to the value in Table 7.2.1-1E corresponding to aperiodic CSI reporting. If the UE is configured with higher layer parameter eMIMO-Type2 for a CSI process of the triggered set of CSI process(es), the report is for a higher layer configured eMIMO type associated with the value of CSI request field for the CSI process. If the UE is configured with higher layer parameter csi-RS-ConfigNZP-ApList and the number of activated CSI-RS resources given by the higher layer parameter numberActivatedAperiodicCSI-RS-Resources is set to '1' for a CSI process of the triggered set of CSI process(es), the report is for the activated CSI-RS resource for the CSI process.

If the CSI request field size is 3 bits and the UE is not configured with the higher layer parameter csi-SubframePatternConfig-r12 for any serving cell, and UE is configured with higher layer parameter csi-RS-ConfigNZP-ApList and the number of activated CSI-RS resources given by the higher layer parameter numberActivatedAperiodicCSI-RS-Resources is set to more than '1' for at least one CSI process, a report is triggered for serving cell  according to the value in Table 7.2.1-1F corresponding to aperiodic CSI reporting. If the UE is configured with higher layer parameter eMIMO-Type2 for a CSI process of the triggered set of CSI process(es), the report is for a higher layer configured eMIMO type associated with the value of CSI request field for the CSI process for serving cell .

If the CSI request field size is 3 bits and the UE is configured with the higher layer parameter csi-SubframePatternConfig-r12 for at least one serving cell, and UE is configured with csi-RS-ConfigNZP-ApList and the number of activated CSI-RS resources given by the higher layer parameter numberActivatedAperiodicCSI-RS-Resources is set to more than '1' for at least one CSI process, a report is triggered for serving cell  according to the value in Table 7.2.1-1G corresponding to aperiodic CSI reporting. If the UE is configured with higher layer parameter eMIMO-Type2 for a CSI process of the triggered set of CSI process(es), the report is for a higher layer configured eMIMO type associated with the value of CSI request field for the CSI process for serving cell .

If the CSI request field size is 4 bits and the UE is not configured with the higher layer parameter csi-SubframePatternConfig-r12 for any serving cell, a report is triggered according to the value in Table 7.2.1-1H corresponding to aperiodic CSI reporting. If the UE is configured with higher layer parameter eMIMO-Type2 for a CSI process of the triggered set of CSI process(es), the report is for a higher layer configured eMIMO type associated with the value of CSI request field for the CSI process.

If the CSI request field size is 4 bits and the UE is configured with the higher layer parameter csi-SubframePatternConfig-r12 for at least one serving cell, a report is triggered according to the value in Table 7.2.1-1I corresponding to aperiodic CSI reporting. If the UE is configured with higher layer parameter eMIMO-Type2 for a CSI process of the triggered set of CSI process(es), the report is for a higher layer configured eMIMO type associated with the value of CSI request field for the CSI process.

If the CSI request field size is 5 bits and the UE is not configured with the higher layer parameter csi-SubframePatternConfig-r12 for any serving cell, a report is triggered according to the value in Table 7.2.1-1J corresponding to aperiodic CSI reporting. If the UE is configured with higher layer parameter eMIMO-Type2 for a CSI process of the triggered set of CSI process(es), the report is for a higher layer configured eMIMO type associated with the value of CSI request field for the CSI process.

If the CSI request field size is 5 bits and the UE is configured with the higher layer parameter csi-SubframePatternConfig-r12 for at least one serving cell, a report is triggered according to the value in Table 7.2.1-1K corresponding to aperiodic CSI reporting. If the UE is configured with higher layer parameter eMIMO-Type2 for a CSI process of the triggered set of CSI process(es), the report is for a higher layer configured eMIMO type associated with the value of CSI request field for the CSI process.

If the UE is configured with higher layer parameter csi-RS-ConfigNZP-ApList for a CSI process of the triggered set of CSI process(es), the UE shall assume the CSI-RS resource associated with the value of CSI request field for the CSI process is present in subframe n.

For a given serving cell, if the UE is configured in transmission modes 1-9, the "CSI process" in Table 7.2.1-1B, Table 7.2.1-1C, Table 7.2.1-1D, and Table 7.2.1-1E refers to the aperiodic CSI configured for the UE on the given serving cell. A UE is not expected to be configured by higher layers with more than 5 CSI processes in each of the 1st and 2nd set of CSI process(es) in Table 7.2.1-1B. A UE is not expected to be configured by higher layers with more than 5 CSI processes and/or {CSI process, CSI subframe set}-pair(s) in each of the 1st and 2nd set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) in Table 7.2.1-1C. A UE is not expected to be configured by higher layers with more than one instance of the same CSI process in each of the higher layer configured sets associated with the value of CSI request field of '01', '10', and '11' in Table 7.2.1-1B and Table 7.2.1-1C respectively. A UE is not expected to be configured by higher layers with more than 32 CSI processes in each of the 1st to 6th set of CSI process(es) in Table 7.2.1-1D. A UE is not expected to be configured by higher layers with more than 32 CSI processes and/or {CSI process, CSI subframe set}-pair(s) in each of the 1st to 6th set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) in Table 7.2.1-1E. A UE is not expected to be configured by higher layers with more than one instance of the same CSI process in each of the higher layer configured sets associated with the value of CSI request field of '001', '010', '011', '100', '101', '110' and '111' in Table 7.2.1-1D, Table 7.2.1-1E, Table 7.2.1-1F, and Table 7.2.1-1G respectively. A UE is not expected to be configured by higher layers with more than 32 of {CSI process, CSI-RS resource} in each of the 1st to 7th set of {CSI process, CSI-RS resource} in Table 7.2.1-1F. A UE is not expected to be configured by higher layers with more than 32 {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} in each of the 1st to 7th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} in Table 7.2.1-1G. A UE is not expected to be configured by higher layers with more than 32 of {CSI process, CSI-RS resource} in each of the 1st to 14th set of {CSI process, CSI-RS resource} in Table 7.2.1-1H. A UE is not expected to be configured by higher layers with more than 32 {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} in each of the 1st to 14th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} in Table 7.2.1-1I. A UE is not expected to be configured by higher layers with more than one instance of the same CSI process in each of the higher layer configured sets associated with the value of CSI request field of '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111' in Table 7.2.1-1H, and Table 7.2.1-1I respectively. A UE is not expected to be configured by higher layers with more than 32 of {CSI process, CSI-RS resource} in each of the 1st to 30th set of {CSI process, CSI-RS resource} in Table 7.2.1-1J. A UE is not expected to be configured by higher layers with more than 32 {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} in each of the 1st to 30th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} in Table 7.2.1-1K. A UE is not expected to be configured by higher layers with more than one instance of the same CSI process in each of the higher layer configured sets associated with the value of CSI request field of '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111' , '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111' in Table 7.2.1-1J, and Table 7.2.1-1K respectively.

A UE is not expected to receive more than one aperiodic CSI report request for a given subframe triggered by uplink DCI formats other than 7-0A/7-0B.

A UE is not expected to update CSI corresponding to the CSI reference resource (defined in Clause 7.2.3) for all CSI report requests triggered by uplink DCI format 7-0A/7-0B except  CSI report requests when the UE has  unreported aperiodic CSI requests, where a CSI request shall only be counted as unreported in a slot/subslot before the slot/subslot where the PUSCH carrying the corresponding CSI is transmitted, and  is the maximum number of CSI requests triggered by uplink DCI format 7-0A/7-0B supported by the UE.

If a UE is configured with higher layer parameter eMIMO-Type for a CSI process, the UE is not expected to receive an aperiodic CSI report request for a given slot/subslot triggering a CSI report for the CSI process.

If a UE is configured with higher layer parameter eMIMO-Type and eMIMO-Type2 for a CSI process, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, the UE on reception of an aperiodic CSI report request triggering a CSI report for eMIMO-Type2 of the CSI process is not expected to update CSI for eMIMO-Type2 (nCQI_ref -1) (defined in Clause 7.2.3) subframes before or (nCQI_ref -1) subframes after the subframe comprising the non-zero power CSI-RS (defined in [3]) within the CSI-RS resource associated with eMIMO-Type of the CSI process.

If a UE is configured with more than one CSI process for a serving cell, the UE on reception of an aperiodic CSI report request triggering a CSI report according to Table 7.2.1-1B is not expected to update CSI corresponding to the CSI reference resource (defined in Clause 7.2.3) for all CSI processes except the  lowest-indexed CSI processes for the serving cell associated with the request when the UE has  unreported CSI processes associated with other aperiodic CSI requests for the serving cell, where a CSI process associated with a CSI request shall only be counted as unreported in a subframe/slot/subslot before the subframe/slot/subslot where the PUSCH carrying the corresponding CSI is transmitted, and  is the maximum number of CSI processes supported by the UE for the serving cell corresponding to subframe/slot/subslot-PUSCH, and:

- for FDD serving cell ;

- for TDD serving cell

- if the UE is configured with four CSI processes for the serving cell ,

- if the UE is configured with two or three CSI processes for the serving cell, .

If more than one value of  is included in the UE-EUTRA-Capability, the UE assumes a value of  that is consistent with its CSI process configuration. If more than one consistent value of  exists, the UE may assume any one of the consistent values.

If a UE is configured with multiple cell groups, and if the UE receives multiple aperiodic CSI report requests in a subframe for different cell groups triggering more than one CSI report, the UE is not required to update CSI for more than 5 CSI processes from the CSI processes corresponding to all the triggered CSI reports.

If a UE is configured with a PUCCH-SCell, and if the UE receives multiple aperiodic CSI report requests in a subframe for both the primary PUCCH group and the secondary PUCCH group triggering more than one CSI report, the UE is not required to update CSI for more than 5 CSI processes from the CSI processes corresponding to all the triggered CSI reports, in case the total number of serving cells in the primary and secondary PUCCH group is no more than 5. If a UE is configured with more than 5 serving cells, and if the UE receives aperiodic CSI report request in a subframe triggering more than CSI reports, the UE is not required to update CSI for more than  CSI processes from the CSI processes corresponding to all the triggered CSI reports, where the value of is given by nMaxProc-r14 if csi-RS-ConfigNZP-ApList is configured for at least one CSI process for which aperiodic CSI report is requested, otherwise, by maxNumberUpdatedCSI-Proc-r13.

Table 7.2.1-1A: CSI Request field for PDCCH/EPDCCH/SPDCCH with uplink DCI format in UE specific search space

| Value of CSI request field | Description |
| --- | --- |
| '00' | No aperiodic CSI report is triggered |
| '01' | Aperiodic CSI report is triggered for serving cell |
| '10' | Aperiodic CSI report is triggered for a 1st set of serving cells configured by higher layers |
| '11' | Aperiodic CSI report is triggered for a 2nd set of serving cells configured by higher layers |

Table 7.2.1-1B: CSI Request field for PDCCH/EPDCCH/SPDCCH with uplink DCI format in UE specific search space

| Value of CSI request field | Description |
| --- | --- |
| '00' | No aperiodic CSI report is triggered |
| '01' | Aperiodic CSI report is triggered for a set of CSI process(es) configured by higher layers for serving cell |
| '10' | Aperiodic CSI report is triggered for a 1st set of CSI process(es) configured by higher layers |
| '11' | Aperiodic CSI report is triggered for a 2nd set of CSI process(es) configured by higher layers |

Table 7.2.1-1C: CSI Request field for PDCCH/EPDCCH/MPDCCH/SPDCCH with uplink DCI format in UE specific search space

| Value of CSI request field | Description |
| --- | --- |
| '00' | No aperiodic CSI report is triggered |
| '01' | Aperiodic CSI report is triggered for a set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) configured by higher layers for serving cell |
| '10' | Aperiodic CSI report is triggered for a 1st set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) configured by higher layers |
| '11' | Aperiodic CSI report is triggered for a 2nd set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) configured by higher layers |

Table 7.2.1-1D: CSI Request field for PDCCH/EPDCCH/SPDCCH with uplink DCI format in UE specific search space

| Value of CSI request field | Description |
| --- | --- |
| '000' | No aperiodic CSI report is triggered |
| '001' | Aperiodic CSI report is triggered for a set of CSI process(es) configured by higher layers for serving cell |
| '010' | Aperiodic CSI report is triggered for a 1st set of CSI process(es) configured by higher layers |
| '011' | Aperiodic CSI report is triggered for a 2nd set of CSI process(es) configured by higher layers |
| '100' | Aperiodic CSI report is triggered for a 3rd set of CSI process(es) configured by higher layers |
| '101' | Aperiodic CSI report is triggered for a 4th set of CSI process(es) configured by higher layers |
| '110' | Aperiodic CSI report is triggered for a 5th set of CSI process(es) configured by higher layers |
| '111' | Aperiodic CSI report is triggered for a 6th set of CSI process(es) configured by higher layers |

Table 7.2.1-1E: CSI Request field for PDCCH/EPDCCH/SPDCCH with uplink DCI format in UE specific search space

| Value of CSI request field | Description |
| --- | --- |
| '000' | No aperiodic CSI report is triggered |
| '001' | Aperiodic CSI report is triggered for a set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) configured by higher layers for serving cell |
| '010' | Aperiodic CSI report is triggered for a 1st set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) configured by higher layers |
| '011' | Aperiodic CSI report is triggered for a 2nd set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) configured by higher layers |
| '100' | Aperiodic CSI report is triggered for a 3rd set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) configured by higher layers |
| '101' | Aperiodic CSI report is triggered for a 4th set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) configured by higher layers |
| '110' | Aperiodic CSI report is triggered for a 5th set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) configured by higher layers |
| '111' | Aperiodic CSI report is triggered for a 6th set of CSI process(es) and/or {CSI process, CSI subframe set}-pair(s) configured by higher layers |

Table 7.2.1-1F: CSI Request field for PDCCH/EPDCCH/SPDCCH with uplink DCI format in UE specific search space

| Value of CSI request field | Description |
| --- | --- |
| '000' | No aperiodic CSI report is triggered |
| '001' | Aperiodic CSI report is triggered for a 1st set of {CSI process, CSI-RS resource} configured by higher layers for serving cell |
| '010' | Aperiodic CSI report is triggered for a 2nd set of {CSI process, CSI-RS resource} configured by higher layers for serving cell |
| '011' | Aperiodic CSI report is triggered for a 3rd set of {CSI process, CSI-RS resource} configured by higher layers for serving cell |
| '100' | Aperiodic CSI report is triggered for a 4th set of {CSI process, CSI-RS resource} configured by higher layers for serving cell |
| '101' | Aperiodic CSI report is triggered for a 5th set of {CSI process, CSI-RS resource} configured by higher layers for serving cell |
| '110' | Aperiodic CSI report is triggered for a 6th set of {CSI process, CSI-RS resource} configured by higher layers for serving cell |
| '111' | Aperiodic CSI report is triggered for a 7th set of {CSI process, CSI-RS resource} configured by higher layers for serving cell |

Table 7.2.1-1G: CSI Request field for PDCCH/EPDCCH/SPDCCH with uplink DCI format in UE specific search space

| Value of CSI request field | Description |
| --- | --- |
| '000' | No aperiodic CSI report is triggered |
| '001' | Aperiodic CSI report is triggered for a 1st set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers for serving cell |
| '010' | Aperiodic CSI report is triggered for a 2nd set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers for serving cell |
| '011' | Aperiodic CSI report is triggered for a 3rd set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers for serving cell |
| '100' | Aperiodic CSI report is triggered for a 4th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers for serving cell |
| '101' | Aperiodic CSI report is triggered for a 5th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers for serving cell |
| '110' | Aperiodic CSI report is triggered for a 6th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers for serving cell |
| '111' | Aperiodic CSI report is triggered for a 7th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers for serving cell |

Table 7.2.1-1H: CSI Request field for PDCCH/EPDCCH with uplink DCI format in UE specific search space

| Value of CSI request field | Description |
| --- | --- |
| '0000' | No aperiodic CSI report is triggered |
| '0001' | Aperiodic CSI report is triggered for a set of {CSI process, CSI-RS resource} configured by higher layers for serving cell |
| '0010' | Aperiodic CSI report is triggered for a 1st set of {CSI process, CSI-RS resource} configured by higher layers |
| '0011' | Aperiodic CSI report is triggered for a 2nd set of {CSI process, CSI-RS resource} configured by higher layers |
| '0100' | Aperiodic CSI report is triggered for a 3rd set of {CSI process, CSI-RS resource} configured by higher layers |
| '0101' | Aperiodic CSI report is triggered for a 4th set of {CSI process, CSI-RS resource} configured by higher layers |
| '0110' | Aperiodic CSI report is triggered for a 5th set of {CSI process, CSI-RS resource} configured by higher layers |
| '0111' | Aperiodic CSI report is triggered for a 6th set of {CSI process, CSI-RS resource} configured by higher layers |
| '1000' | Aperiodic CSI report is triggered for a 7th set of {CSI process, CSI-RS resource} configured by higher layers |
| '1001' | Aperiodic CSI report is triggered for a 8th set of {CSI process, CSI-RS resource} configured by higher layers |
| '1010' | Aperiodic CSI report is triggered for a 9th set of {CSI process, CSI-RS resource} configured by higher layers |
| '1011' | Aperiodic CSI report is triggered for a 10th set of {CSI process, CSI-RS resource} configured by higher layers |
| '1100' | Aperiodic CSI report is triggered for a 11th set of {CSI process, CSI-RS resource} configured by higher layers |
| '1101' | Aperiodic CSI report is triggered for a 12th set of {CSI process, CSI-RS resource} configured by higher layers |
| '1110' | Aperiodic CSI report is triggered for a 13th set of {CSI process, CSI-RS resource} configured by higher layers |
| '1111' | Aperiodic CSI report is triggered for a 14th set of {CSI process, CSI-RS resource} configured by higher layers |

Table 7.2.1-1I: CSI Request field for PDCCH/EPDCCH with uplink DCI format in UE specific search space

| Value of CSI request field | Description |
| --- | --- |
| '0000' | No aperiodic CSI report is triggered |
| '0001' | Aperiodic CSI report is triggered for a set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers for serving cell |
| '0010' | Aperiodic CSI report is triggered for a 1st set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '0011' | Aperiodic CSI report is triggered for a 2nd set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '0100' | Aperiodic CSI report is triggered for a 3rd set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '0101' | Aperiodic CSI report is triggered for a 4th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '0110' | Aperiodic CSI report is triggered for a 5th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '0111' | Aperiodic CSI report is triggered for a 6th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '1000' | Aperiodic CSI report is triggered for a 7th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '1001' | Aperiodic CSI report is triggered for a 8th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '1010' | Aperiodic CSI report is triggered for a 9th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '1011' | Aperiodic CSI report is triggered for a 10th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '1100' | Aperiodic CSI report is triggered for a 11th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '1101' | Aperiodic CSI report is triggered for a 12th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '1110' | Aperiodic CSI report is triggered for a 13th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '1111' | Aperiodic CSI report is triggered for a 14th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |

Table 7.2.1-1J: CSI Request field for PDCCH/EPDCCH with uplink DCI format in UE specific search space

| Value of CSI request field | Description |
| --- | --- |
| '00000' | No aperiodic CSI report is triggered |
| '00001' | Aperiodic CSI report is triggered for a set of {CSI process, CSI-RS resource} configured by higher layers for serving cell |
| '00010' | Aperiodic CSI report is triggered for a 1st set of {CSI process, CSI-RS resource} configured by higher layers |
| '00011' | Aperiodic CSI report is triggered for a 2nd set of {CSI process, CSI-RS resource} configured by higher layers |
| '00100' | Aperiodic CSI report is triggered for a 3rd set of {CSI process, CSI-RS resource} configured by higher layers |
| '00101' | Aperiodic CSI report is triggered for a 4th set of {CSI process, CSI-RS resource} configured by higher layers |
| '00110' | Aperiodic CSI report is triggered for a 5th set of {CSI process, CSI-RS resource} configured by higher layers |
| '00111' | Aperiodic CSI report is triggered for a 6th set of {CSI process, CSI-RS resource} configured by higher layers |
| '01000' | Aperiodic CSI report is triggered for a 7th set of {CSI process, CSI-RS resource} configured by higher layers |
| '01001' | Aperiodic CSI report is triggered for a 8th set of {CSI process, CSI-RS resource} configured by higher layers |
| '01010' | Aperiodic CSI report is triggered for a 9th set of {CSI process, CSI-RS resource} configured by higher layers |
| '01011' | Aperiodic CSI report is triggered for a 10th set of {CSI process, CSI-RS resource} configured by higher layers |
| '01100' | Aperiodic CSI report is triggered for a 11th set of {CSI process, CSI-RS resource} configured by higher layers |
| '01101' | Aperiodic CSI report is triggered for a 12th set of {CSI process, CSI-RS resource} configured by higher layers |
| '01110' | Aperiodic CSI report is triggered for a 13th set of {CSI process, CSI-RS resource} configured by higher layers |
| '01111' | Aperiodic CSI report is triggered for a 14th set of {CSI process, CSI-RS resource} configured by higher layers |
| '10000' | Aperiodic CSI report is triggered for a 15th set of {CSI process, CSI-RS resource} configured by higher layers |
| '10001' | Aperiodic CSI report is triggered for a 16th set of {CSI process, CSI-RS resource} configured by higher layers |
| '10010' | Aperiodic CSI report is triggered for a 17th set of {CSI process, CSI-RS resource} configured by higher layers |
| '10011' | Aperiodic CSI report is triggered for a 18th set of {CSI process, CSI-RS resource} configured by higher layers |
| '10100' | Aperiodic CSI report is triggered for a 19th set of {CSI process, CSI-RS resource} configured by higher layers |
| '10101' | Aperiodic CSI report is triggered for a 20th set of {CSI process, CSI-RS resource} configured by higher layers |
| '10110' | Aperiodic CSI report is triggered for a 21st set of {CSI process, CSI-RS resource} configured by higher layers |
| '10111' | Aperiodic CSI report is triggered for a 22nd set of {CSI process, CSI-RS resource} configured by higher layers |
| '11000' | Aperiodic CSI report is triggered for a 23rd set of {CSI process, CSI-RS resource} configured by higher layers |
| '11001' | Aperiodic CSI report is triggered for a 24th set of {CSI process, CSI-RS resource} configured by higher layers |
| '11010' | Aperiodic CSI report is triggered for a 25th set of {CSI process, CSI-RS resource} configured by higher layers |
| '11011' | Aperiodic CSI report is triggered for a 26th set of {CSI process, CSI-RS resource} configured by higher layers |
| '11100' | Aperiodic CSI report is triggered for a 27th set of {CSI process, CSI-RS resource} configured by higher layers |
| '11101' | Aperiodic CSI report is triggered for a 28th set of {CSI process, CSI-RS resource} configured by higher layers |
| '11110' | Aperiodic CSI report is triggered for a 29th set of {CSI process, CSI-RS resource} configured by higher layers |
| '11111' | Aperiodic CSI report is triggered for a 30th set of {CSI process, CSI-RS resource} configured by higher layers |

Table 7.2.1-1K: CSI Request field for PDCCH/EPDCCH with uplink DCI format in UE specific search space

| Value of CSI request field | Description |
| --- | --- |
| '00000' | No aperiodic CSI report is triggered |
| '00001' | Aperiodic CSI report is triggered for a set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers for serving cell |
| '00010' | Aperiodic CSI report is triggered for a 1st set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '00011' | Aperiodic CSI report is triggered for a 2nd set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '00100' | Aperiodic CSI report is triggered for a 3rd set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '00101' | Aperiodic CSI report is triggered for a 4th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '00110' | Aperiodic CSI report is triggered for a 5th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '00111' | Aperiodic CSI report is triggered for a 6th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '01000' | Aperiodic CSI report is triggered for a 7th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '01001' | Aperiodic CSI report is triggered for a 8th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '01010' | Aperiodic CSI report is triggered for a 9th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '01011' | Aperiodic CSI report is triggered for a 10th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '01100' | Aperiodic CSI report is triggered for a 11th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '01101' | Aperiodic CSI report is triggered for a 12th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '01110' | Aperiodic CSI report is triggered for a 13th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '01111' | Aperiodic CSI report is triggered for a 14th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '10000' | Aperiodic CSI report is triggered for a 15th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '10001' | Aperiodic CSI report is triggered for a 16th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '10010' | Aperiodic CSI report is triggered for a 17th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '10011' | Aperiodic CSI report is triggered for a 18th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '10100' | Aperiodic CSI report is triggered for a 19th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '10101' | Aperiodic CSI report is triggered for a 20th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '10110' | Aperiodic CSI report is triggered for a 21st set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '10111' | Aperiodic CSI report is triggered for a 22nd set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '11000' | Aperiodic CSI report is triggered for a 23rd set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '11001' | Aperiodic CSI report is triggered for a 24th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '11010' | Aperiodic CSI report is triggered for a 25th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '11011' | Aperiodic CSI report is triggered for a 26th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '11100' | Aperiodic CSI report is triggered for a 27th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '11101' | Aperiodic CSI report is triggered for a 28th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '11110' | Aperiodic CSI report is triggered for a 29th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |
| '11111' | Aperiodic CSI report is triggered for a 30th set of {CSI process, CSI-RS resource} and/or {CSI process, CSI subframe set, CSI-RS resource} configured by higher layers |

NOTE: PDCCH/EPDCCH/MPDCCH/SPDCCH with DCI formats used to grant PUSCH transmissions as given by DCI format 0, DCI format 4, DCI format 6-0A and DCI format 7-0A/7-0B are herein referred to as uplink DCI format when common behaviour is addressed.

For a serving cell that is not a LAA SCell, and a non-BL/CE UE, when the CSI request field from an uplink DCI format other than 7-0A/7-0B is set to trigger a report,

- for FDD k=3 if the UE is configured with higher layer parameter shortProcessingTime, and the corresponding DCI format is mapped onto the UE-specific search space and k=4 otherwise,

- for TDD UL/DL configuration 1-6, k is given in Table 8-2,

- for TDD UL/DL configuration 0,

- if the MSB of the UL index is set to 1 and LSB of the UL index is set to 0, k is given in Table 8-2i if the UE is configured with higher layer parameter shortProcessingTime, and the corresponding DCI format is mapped onto the UE-specific search space, in Table 8-2 otherwise; or

- if MSB of the UL index is set to 0 and LSB of the UL index is set to 1, k is equal to 6 if the UE is configured with higher layer parameter shortProcessingTime, and the corresponding DCI format is mapped onto the UE-specific search, 7 otherwise; or

- if both MSB and LSB of the UL index is set to 1, k is given in Table 8-2i if the UE is configured with higher layer parameter shortProcessingTime, and the corresponding DCI format is mapped onto the UE-specific search space, in Table 8-2 otherwise.

For a serving cell , when the CSI request field from an uplink DCI format 7-0A/7-0B is set to trigger a report, for

- FDD, if the UE is configured for subslot uplink transmissions, k is determined based on higher layer configuration from , otherwise k=4.

- TDD, k is given by table 8-2m, 8-2n, 8-2p according to the corresponding special subframe configuration.

For TDD, if a UE is configured with more than one serving cell and if the UL/DL configurations of at least two serving cells are different, or if the UE is configured with the parameter EIMTA-MainConfigServCell-r12 for at least one serving cell, or for FDD-TDD and serving cell frame structure type 2, the "TDD UL/DL Configuration" given in Table 8-2 refers to the UL-reference UL/DL configuration (defined in Clause 8.0).

For a serving cell that is a LAA SCell, when the CSI request field from an uplink DCI format is set to trigger a report,

corresponds to the scheduled PUSCH subframe determined in Clause 8.0 if the uplink DCI format is 0A/4A,

corresponds to the N-th scheduled PUSCH subframe determined in Clause 8.0 if the uplink DCI format is 0B/4B and ,

corresponds to the (N-1)-th scheduled PUSCH subframe determined in Clause 8.0 if the uplink DCI format is 0B/4B and ,

value of N is determined by the number of scheduled subframes field in the corresponding DCI format 0B/4B

For a non-BL/CE UE, when the CSI request field from a Random Access Response Grant is set to trigger a report and is not reserved, k is equal to  if the UL delay field in Clause 6.2 is set to zero, where  is given in Clause 6.1.1. The UE shall postpone aperiodic CSI reporting to the next available UL subframe if the UL delay field is set to 1.

For a BL/CE UE, when the CSI request field from a Random Access Response Grant is set to trigger a report and is not reserved, the subframe(s) in which the corresponding aperiodic CSI reporting is transmitted is determined according to Clause 6.1.1.

The minimum reporting interval for aperiodic reporting of CQI and PMI and RI and CRI is 1 subframe. The subband size for CQI shall be the same for transmitter-receiver configurations with and without precoding.

If a UE is not configured for simultaneous PUSCH and PUCCH transmission, when aperiodic CSI report with no transport block associated as defined in Clause 8.6.2 and positive SR is transmitted in the same subframe/slot/subslot, the UE shall transmit SR, and, if applicable, HARQ-ACK, on PUCCH resources as described in Clause 10.1

A UE is semi-statically configured by higher layers to feed back CQI and PMI and corresponding RI and CRI on the same PUSCH using one of the following CSI reporting modes given in Table 7.2.1-1 and described below. For a BL/CE UE the UE shall not transmit the RI for any CSI reporting mode in Table 7.2.1-1.

If a UE is configured with higher layer parameter FeCoMPCSIEnabled for a CSI process the reported CRI value can take on values 0, 1, 2. For CRI value of 2, then 2 sets of PMI/CQI/RI are reported, one set for each of the configured CSI-RS resources.  The combinations of the reported RIs are restricted to the following sets {1,1}, {1,2}, {2,1}, {2,2}, {2,3}, {3,2}, {3,3}, {3,4}, {4,3}, {4,4} where {x,y} indicates RI value of x corresponding to the first CSI-RS resource and RI value of y corresponding to the second CSI-RS resource.

If a UE is configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, one of the following CSI reporting modes given in Table 7.2.1-1 is configured only for eMIMO-Type2 and for any CSI reporting mode in Table 7.2.1-1,

- the UE shall not transmit CQI and second precoding matrix indicator  for eMIMO-Type;

- the UE shall not transmit RI for eMIMO-Type except if the maximum number of supported layers for spatial multiplexing in DL by the UE is more than 2, then UE feeds back a 1-bit RI according to Table 7.2.1-1L;

- the UE shall transmit wideband first PMI for eMIMO-Type.

If a UE is configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with more than one CSI-RS resource configured, and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, one of the following CSI reporting modes given in Table 7.2.1-1 is configured only for eMIMO-Type2 and the UE shall not transmit CQI, PMI, RI for eMIMO-Type and the UE shall transmit CRI for eMIMO-Type for any CSI reporting mode in Table 7.2.1-1.

Table 7.2.1-1: CQI and PMI Feedback Types for PUSCH CSI reporting Modes

|  |  | PMI Feedback Type |  |  |
| --- | --- | --- | --- | --- |
|  |  | No PMI | Single PMI | Multiple PMI |
| PUSCH CQIFeedback Type | Wideband(wideband CQI) | Mode 1-0 | Mode 1-1 | Mode 1-2 |
|  | UE Selected(subband CQI) | Mode 2-0 |  | Mode 2-2 |
|  | Higher Layer-configured(subband CQI) | Mode 3-0 | Mode 3-1 | Mode 3-2 |

Table 7.2.1-1L: Mapping of RI field to RI

| Value of RI field | RI |
| --- | --- |
| 0 | 1 |
| 1 | 3 |

For non-BL/CE UE and for each of the transmission modes defined in Clause 7.1, the following reporting modes are supported on PUSCH:

Transmission mode 1 : Modes 2-0, 3-0, 1-0

Transmission mode 2 : Modes 2-0, 3-0, 1-0

Transmission mode 3 : Modes 2-0, 3-0, 1-0

Transmission mode 4 : Modes 1-2, 2-2, 3-1, 3-2, 1-1

Transmission mode 5 : Mode 3-1, 1-1

Transmission mode 6 : Modes 1-2, 2-2, 3-1, 3-2, 1-1

Transmission mode 7 : Modes 2-0, 3-0, 1-0

Transmission mode 8 : Modes 1-2, 2-2, 3-1, 3-2, 1-1 if the UE is configured with PMI/RI reporting; modes 2-0, 3-0, 1-0 if the UE is configured without PMI/RI reporting

Transmission mode 9 : Modes 1-2, 2-2, 3-1, 3-2, 1-1 if the UE is configured with PMI/RI reporting and number of CSI-RS ports > 1 and the UE is not configured with higher layer parameter advancedCodebookEnabled; modes 1-2, 2-2, 3-1, 3-2 if the UE is configured with PMI/RI reporting and number of CSI-RS ports > 1 and the UE is configured with higher layer parameter advancedCodebookEnabled; modes 2-0, 3-0, 1-0 if the UE is configured without PMI/RI reporting or without PMI reporting or number of CSI-RS ports=1 or the number of CSI-RS ports in each of one or more CSI-RS resources in a CSI process is one when eMIMO-Type or eMIMO-Type2 is set to 'CLASS B'; modes 1-1, 3-1 if the UE is configured with higher layer parameter semiOpenLoop.

Transmission mode 10 : Modes 1-2, 2-2, 3-1, 3-2, 1-1 if the UE is configured with PMI/RI reporting and number of CSI-RS ports > 1 and the UE is not configured with higher layer parameter advancedCodebookEnabled; modes 1-2, 2-2, 3-1, 3-2 if the UE is configured with PMI/RI reporting and number of CSI-RS ports > 1 and the UE is configured with higher layer parameter advancedCodebookEnabled; modes 2-0, 3-0, 1-0 if the UE is configured without PMI/RI reporting or without PMI reporting or number of CSI-RS ports=1 or the number of CSI-RS ports in each of one or more CSI-RS resources in a CSI process is one when eMIMO-Type or eMIMO-Type2 is set to 'CLASS B'; modes 1-1, 3-1 if the UE configured with higher layer parameter semiOpenLoop.

For a BL/CE UE configured with CEModeA, the following reporting modes are supported on PUSCH:

Transmission mode 1 : Mode 2-0

Transmission mode 2 : Mode 2-0

Transmission mode 6 : Mode 2-0

Transmission mode 9 : Mode 2-0

For Transmission mode 6 and a BL/CE UE configured with a C-RNTI, the BL/CE UE reports CQI for the closed-loop with spatial multiplexing PDSCH transmission scheme.

The aperiodic CSI reporting mode is given by the parameter cqi-ReportModeAperiodic which is configured by higher-layer signalling.

For a non-BL/CE UE, a serving cell with , PUSCH reporting modes are not supported for that serving cell.

For a non-BL/CE UE, RI is only reported for transmission modes 3 and 4, as well as transmission modes 8, 9 and 10 with PMI/RI reporting, and transmission modes 9 and 10 without PMI reporting.

For a BL/CE UE, RI is not reported.

If the UE is configured with higher layer parameter eMIMO-Type2 for a CSI process, the higher layer parameter eMIMO-Type in the rest of this Clause refers to higher layer configured eMIMO type associated with the value of CSI request field triggering aperiodic CSI reporting for the CSI process.

For serving cell , a UE configured in transmission mode 10 with PMI/RI reporting or without PMI reporting for a CSI process can be configured with a 'RI-reference CSI process' for the CSI process. If the UE is configured with a 'RI-reference CSI process' for the CSI process, the reported RI for the CSI process shall be the same as the reported RI for the configured 'RI-reference CSI process'. The RI for the 'RI-reference CSI process' is not based on any other configured CSI process other than the 'RI-reference CSI process'. The UE is not expected to receive an aperiodic CSI report request for a given subframe/slot/subslot triggering a CSI report including CSI associated with the CSI process and not including CSI associated with the configured 'RI-reference CSI process'. If the UE is configured with a 'RI-reference CSI process' for a CSI process and if subframe sets  and  are configured by higher layers for only one of the CSI processes then the UE is not expected to receive configuration for the CSI process configured with the subframe subsets that have a different set of restricted RIs with precoder codebook subset restriction between the two subframe sets. The UE is not expected to receive configurations for the CSI process and the 'RI-reference CSI process' that have a different:

- Aperiodic CSI reporting mode, and/or

- number of CSI-RS antenna ports, and/or

- set of restricted RIs with precoder codebook subset restriction if subframe sets  and  are not configured by higher layers for both CSI processes, and/or

- set of restricted RIs with precoder codebook subset restriction for each subframe set if subframe sets  and  are configured by higher layers for both CSI processes, and/or

- set of restricted RIs with precoder codebook subset restriction if subframe sets  and  are configured by higher layers for only one of the CSI processes, and the set of restricted RIs for the two subframe sets are the same, and/or

- number of CSI-RS antenna ports for any two CSI-RS resources for the two CSI processes, if a UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one for at least one of the two CSI processes, and/or

- set of restricted RIs with precoder codebook subset restriction for any two CSI-RS resources for the two CSI processes, if a UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one for at least one of the two CSI processes and if subframe sets  and  are not configured by higher layers for both CSI processes, and/or

- set of restricted RIs with precoder codebook subset restriction for each subframe set and for any two CSI-RS resources for the two CSI processes, if a UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one for at least one of the two CSI processes and if subframe sets  and  are configured by higher layers for both CSI processes, and/or

- set of restricted RIs with precoder codebook subset restriction for any two CSI-RS resources for the two CSI processes, if a UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one for at least one of the two CSI processes and if subframe sets  and  are configured by higher layers for only one of the CSI processes, and the set of restricted RIs for the two subframe sets are the same.

For a non-BL/CE UE, a RI report for a serving cell on an aperiodic reporting mode is valid only for CQI/PMI report or CQI report without PMI reporting for that serving cell on that aperiodic reporting mode.

For a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with parameter eMIMO-Type configured by higher layers, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B' and the number of configured CSI-RS resources is more than one, and for a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, and the total number of antenna ports across all configured CSI-RS resources is more than 15, the UE on reception of an aperiodic CSI report request triggering a CSI report in uplink subframe  is not expected to update CRI corresponding to the CSI process if CRI for the CSI process has been reported and updated on or after subframe .

Wideband feedback

Mode 1-2 description:

For a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one, and for a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, the UE shall report one wideband CRI which is calculated assuming transmission on set S subbands.

For each subband a preferred precoding matrix is selected from the codebook subset assuming transmission only in the subband

A UE shall report one wideband CQI value per codeword which is calculated assuming the use of the corresponding selected precoding matrix in each subband and transmission on set S subbands. The UE shall report the selected precoding matrix indicator for each set S subband except with

## 8 CSI-RS ports configured for transmission modes 9 and 10 or with alternativeCodeBookEnabledFor4TX-r12=TRUE configured for transmission modes 8, 9 and 10, in which case a first precoding matrix indicator is reported for the set S subbands and a second precoding matrix indicator  is reported for each set S subband, if the UE is not configured with higher layer parameter eMIMO-Type or advancedCodebookEnabled, or UE is configured in transmission mode 9 or 10 and advancedCodebookEnabled=TRUE, and reported , or UE reports CRI, or UE is configured in transmission mode 9 or 10, and with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured.

UE is configured in transmission mode 9 or 10, and with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', in which case a first precoding matrix indicator  is reported for the set S subbands and a second precoding matrix indicator  is reported for each set S subband, if the UE is not configured with higher layer parameter advancedCodebookEnabled, or UE is configured with higher layer parameter advancedCodebookEnabled=TRUE, and reported .

UE is configured in transmission mode 9 or 10, and with higher layer parameter advancedCodebookEnabled=TRUE, and reported , in which case a first precoding matrix indicator  is reported for the set S subbands, a relative power indicator  is reported for the set S subbands and a second precoding matrix indicator  is reported for each set S subband.

Subband size is given by Table 7.2.1-3A when the CSI request field from an uplink DCI format 7-0A/7-0B is set to trigger a report, Table 7.2.1-3 otherwise.

For transmission modes 4, 8, 9 and 10, the reported PMI and CQI values and RPI value (if reported) are calculated conditioned on the reported RI. For other transmission modes they are reported conditioned on rank 1. If CRI is reported, the reported PMI, CQI, and RI values are calculated conditioned on the reported CRI.

Mode 1-1 description:

For a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one, and for a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, the UE shall report one wideband CRI which is calculated assuming transmission on set S subbands.

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands

A UE shall report a wideband CQI value per codeword which is calculated assuming the use of the single precoding matrix in all subbands and transmission on set S subbands

The UE shall report the selected single precoding matrix indicator except with

## 8 CSI-RS ports configured for transmission modes 9 and 10 or with alternativeCodeBookEnabledFor4TX-r12=TRUE configured for transmission modes 8, 9 and 10, in which case a first and second precoding matrix indicator are reported corresponding to the selected single precoding matrix, if the UE is not configured with higher layer parameter eMIMO-Type, or UE reports CRI, or UE is configured in transmission mode 9 or 10, and with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured or when higher layer parameter semiOpenLoop is configured and RI<3, in which case a first precoding matrix indicator is reported corresponding to the selected single precoding matrix.

UE is configured in transmission mode 9 or 10, and with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', in which case a first and second precoding matrix indicator are reported corresponding to the selected single precoding matrix, except when higher layer parameter semiOpenLoop is configured and RI<3, in which case a first precoding matrix indicator is reported corresponding to the selected single precoding matrix.

For transmission modes 4, 8, 9 and 10, the reported PMI and CQI values are calculated conditioned on the reported RI. For other transmission modes they are reported conditioned on rank 1. If CRI is reported, the reported PMI, CQI, and RI values are calculated conditioned on the reported CRI.

Mode 1-0 description:

If a UE is configured in transmission mode 9 or 10, and UE is configured with higher layer parameter eMIMO-Type for a CSI process, and eMIMO-Type is set to 'CLASS B', and the number of CSI-RS antenna ports in at least one of the one or more configured CSI-RS resource is more than one,

If the UE is not configured with higher layer parameter csi-RS-NZP-mode, and the number of configured CSI-RS resources is more than one, or the UE is configured with higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, the UE shall report one wideband CRI which is calculated assuming transmission on set S subbands.

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands

A UE shall report a wideband CQI value per codeword which is calculated assuming the use of the single precoding matrix in all subbands and transmission on set S subbands

The selected precoding matrix, and reported CQI values are calculated conditioned on the reported RI. If CRI is reported, the selected precoding matrix, reported CQI, and RI values are calculated conditioned on the reported CRI

otherwise,

For a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one, and for a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, the UE shall report one wideband CRI which is calculated assuming transmission on set S subbands.

A UE shall report a wideband CQI value which is calculated assuming transmission on set S subbands

The wideband CQI represents channel quality for the first codeword, even when RI>1.

For transmission mode 3 the reported CQI value is calculated conditioned on the reported RI. For other transmission modes they are reported conditioned on rank 1. If CRI is reported, the reported CQI values are calculated conditioned on the reported CRI.

Higher Layer-configured subband feedback

Mode 3-0 description:

If a UE is configured in transmission mode 9 or 10, and UE is configured with higher layer parameter eMIMO-Type for a CSI process, and eMIMO-Type is set to 'CLASS B', and the number of CSI-RS antenna ports in at least one of the one or more configured CSI-RS resource is more than one,

If the UE is not configured with higher layer parameter csi-RS-NZP-mode, and the number of configured CSI-RS resources is more than one, or the UE is configured with higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, the UE shall report one wideband CRI which is calculated assuming transmission on set S subbands.

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands

A UE shall report one subband CQI value per codeword for each set S subband which are calculated assuming the use of the single precoding matrix in all subbands and assuming transmission in the corresponding subband.

A UE shall report a wideband CQI value per codeword which is calculated assuming the use of the single precoding matrix in all subbands and transmission on set S subbands

The selected precoding matrix, and reported CQI values are calculated conditioned on the reported RI. If CRI is reported, the selected precoding matrix, reported CQI, and RI values are calculated conditioned on the reported CRI

otherwise,

For a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one, and for a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, the UE shall report one wideband CRI which is calculated assuming transmission on set S subbands.

A UE shall report a wideband CQI value which is calculated assuming transmission on set S subbands

The UE shall also report one subband CQI value for each set S subband. The subband CQI value is calculated assuming transmission only in the subband

Both the wideband and subband CQI represent channel quality for the first codeword, even when RI>1.

For transmission mode 3 the reported CQI values are calculated conditioned on the reported RI. For other transmission modes they are reported conditioned on rank 1. If CRI is reported, the reported CQI values are calculated conditioned on the reported CRI.

Mode 3-1 description:

For a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one, and for a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, the UE shall report one wideband CRI which is calculated assuming transmission on set S subbands.

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands

A UE shall report one subband CQI value per codeword for each set S subband which are calculated assuming the use of the single precoding matrix in all subbands and assuming transmission in the corresponding subband.

A UE shall report a wideband CQI value per codeword which is calculated assuming the use of the single precoding matrix in all subbands and transmission on set S subbands

The UE shall report the selected single precoding matrix indicator except with,

## 8 CSI-RS ports configured for transmission modes 9 and 10 or with alternativeCodeBookEnabledFor4TX-r12=TRUE configured for transmission modes 8, 9 and 10, in which case a first and second precoding matrix indicator are reported corresponding to the selected single precoding matrix, if the UE is not configured with higher layer parameter eMIMO-Type or advancedCodebookEnabled, or UE is configured in transmission mode 9 or 10 and advancedCodebookEnabled=TRUE, and reported , or UE reports CRI, or UE is configured in transmission mode 9 or 10, and with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, or when higher layer parameter semiOpenLoop is configured and RI<3, in which case a first precoding matrix indicator is reported corresponding to the selected single precoding matrix.

UE is configured in transmission mode 9 or 10, and with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', in which case a first and second precoding matrix indicator are reported corresponding to the selected single precoding matrix if the UE is not configured with higher layer parameter advancedCodebookEnabled, or UE is configured with higher layer parameter advancedCodebookEnabled=TRUE, and reported , except when higher layer parameter semiOpenLoop is configured and RI<3, in which case a first precoding matrix indicator is reported corresponding to the selected single precoding matrix.

UE is configured in transmission mode 9 or 10, and with higher layer parameter advancedCodebookEnabled=TRUE, and reported , in which case a first and second precoding matrix indicator and relative power indicator are reported corresponding to the selected single precoding matrix.

For transmission modes 4, 8, 9 and 10, the reported PMI and CQI values and RPI value (if reported) are calculated conditioned on the reported RI. For other transmission modes they are reported conditioned on rank 1. If CRI is reported, the reported PMI, CQI, and RI values are calculated conditioned on the reported CRI.

Mode 3-2 description:

For a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one, and for a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, the UE shall report one wideband CRI which is calculated assuming transmission on set S subbands.

For each subband a preferred precoding matrix is selected from the codebook subset assuming transmission only in the subband

A UE shall report one wideband CQI value per codeword which is calculated assuming the use of the corresponding selected precoding matrix in each subband and transmission on set S subbands.

A UE shall report the selected single precoding matrix indicator for each set S subband except with,

## 8 CSI-RS ports configured for transmission mode 9 and 10, or with alternativeCodeBookEnabledFor4TX-r12=TRUE configured for transmission modes 8, 9 and 10, in which case the UE shall report a first precoding matrix indicator for all set S subbands and also report a second precoding matrix indicator for each set S subband, if the UE is not configured with higher layer parameter eMIMO-Type or advancedCodebookEnabled, or UE is configured in transmission mode 9 or 10 and advancedCodebookEnabled=TRUE, and reported , or UE reports CRI, or UE is configured in transmission mode 9 or 10, and with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured.

UE is configured in transmission mode 9 or 10, and with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', in which case a first precoding matrix indicator  is reported for the set S subbands and a second precoding matrix indicator  is reported for each set S subband if the UE is not configured with higher layer parameter advancedCodebookEnabled, or UE is configured with higher layer parameter advancedCodebookEnabled=TRUE, and reported .

UE is configured in transmission mode 9 or 10, and with higher layer parameter advancedCodebookEnabled=TRUE, and reported , in which case a first precoding matrix indicator  is reported for the set S subbands, a relative power indicator  is reported for the set S subbands, and a second precoding matrix indicator  is reported for each set S subband.

A UE shall report one subband CQI value per codeword for each set S subband reflecting transmission over the single subband and using the selected precoding matrix in the corresponding subband.

For transmission modes 4, 8, 9 and 10, the reported PMI and CQI values and RPI value (if reported) are calculated conditioned on the reported RI. For transmission mode 6 they are reported conditioned on rank 1. If CRI is reported, the reported PMI, CQI, and RI values are calculated conditioned on the reported CRI.

Subband CQI value for each codeword are encoded differentially with respect to their respective wideband CQI using 2-bits as defined by

Subband differential CQI offset level = subband CQI index – wideband CQI index. The mapping from the 2-bit subband differential CQI value to the offset level is shown in Table 7.2.1-2.

Table 7.2.1-2: Mapping subband differential CQI value to offset level

| Subband differential CQI value | Offset level |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | -1 |

Supported subband size (k) is given in Table 7.2.1-3A when the CSI request field from an uplink DCI format 7-0A/7-0B is set to trigger a report, in Table 7.2.1-3 otherwise.

Table 7.2.1-3: Subband Size (k) vs. System Bandwidth

| System Bandwidth | Subband Size |
| --- | --- |
|  | (k) |
| 6 - 7 | NA |
| 8 - 10 | 4 |
| 11 - 26 | 4 |
| 27 - 63 | 6 |
| 64 - 110 | 8 |

Table 7.2.1-3A: Subband Size (k) vs. System Bandwidth when the CSI request field from an uplink DCI format 7-0A/7-0B is set to trigger a report

| System Bandwidth | Subband Size |
| --- | --- |
|  | (k) |
| 6 - 7 | NA |
| 8 - 10 | 4 |
| 11 - 26 | 12 |
| 27 - 63 | 12 |
| 64 - 110 | 12 |

UE-selected subband feedback

Mode 2-0 description:

If a UE is configured in transmission mode 9 or 10, and UE is configured with higher layer parameter eMIMO-Type for a CSI process, and eMIMO-Type is set to 'CLASS B', and the number of CSI-RS antenna ports in at least one of the one or more configured CSI-RS resource is more than one,

If the UE is not configured with higher layer parameter csi-RS-NZP-mode, and the number of configured CSI-RS resources is more than one, or the UE is configured with higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, the UE shall report one wideband CRI which is calculated assuming transmission on set S subbands.

The UE shall perform joint selection of the set of M preferred subbands of size k within the set of subbands S and a preferred single precoding matrix selected from the codebook subset that is preferred to be used for transmission over the M selected subbands.

The UE shall report one CQI value per codeword reflecting transmission only over the selected M preferred subbands and using the same selected single precoding matrix in each of the M subbands.

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands

A UE shall report a wideband CQI value per codeword which is calculated assuming the use of the single precoding matrix in all subbands and transmission on set S subbands

The selected precoding matrix, and reported CQI values are calculated conditioned on the reported RI. If CRI is reported, the selected precoding matrix, reported CQI, and RI values are calculated conditioned on the reported CRI.

otherwise,

For a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one, and for a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, the UE shall report one wideband CRI which is calculated assuming transmission on set S subbands.

The UE shall select a set of M preferred subbands of size k (where k and M are given in Table 7.2.1-5 for each system bandwidth range) within the set of subbands S.

The UE shall also report one CQI value reflecting transmission only over the M selected subbands determined in the previous step. The CQI represents channel quality for the first codeword, even when RI>1.

Additionally, the UE shall also report one wideband CQI value which is calculated assuming transmission on set S subbands. The wideband CQI represents channel quality for the first codeword, even when RI>1.

For transmission mode 3 the reported CQI values are calculated conditioned on the reported RI. For other transmission modes they are reported conditioned on rank 1. If CRI is reported, the reported CQI values are calculated conditioned on the reported CRI.

Mode 2-2 description:

For a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one, and for a UE configured in transmission mode 9 or 10, and for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, the UE shall report one wideband CRI which is calculated assuming transmission on set S subbands.

The UE shall perform joint selection of the set of M preferred subbands of size k within the set of subbands S and a preferred single precoding matrix selected from the codebook subset that is preferred to be used for transmission over the M selected subbands.

The UE shall report one CQI value per codeword reflecting transmission only over the selected M preferred subbands and using the same selected single precoding matrix in each of the M subbands.

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands

A UE shall report a wideband CQI value per codeword which is calculated assuming the use of the single precoding matrix in all subbands and transmission on set S subbands

The UE shall report the selected single precoding matrix indicator preferred for the M selected subbands and the selected single precoding matrix indicator for all set S subbands except with,

## 8 CSI-RS ports configured for transmission modes 9 and 10 or with alternativeCodeBookEnabledFor4TX-r12=TRUE configured for transmission modes 8, 9 and 10, in which case the UE shall report a first precoding matrix indicator for all set S subbands, a second precoding matrix indicator for all set S subbands and another second precoding matrix indicator for the M selected subbands, if the UE is not configured with higher layer parameter eMIMO-Type or advancedCodebookEnabled, or UE is configured in transmission mode 9 or 10 and advancedCodebookEnabled=TRUE, and reported , or UE reports CRI, or UE is configured in transmission mode 9 or 10, and with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured.

UE is configured in transmission mode 9 or 10, and with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', in which case the UE shall report a first precoding matrix indicator  for all set S subbands, a second precoding matrix indicator  for all set S subbands and another second precoding matrix indicator  for or the M selected subbands if the UE is not configured with higher layer parameter advancedCodebookEnabled, or UE is configured with higher layer parameter advancedCodebookEnabled=TRUE, and reported .

UE is configured in transmission mode 9 or 10, and with higher layer parameter advancedCodebookEnabled=TRUE, and reported , in which case the UE shall report a first precoding matrix indicator  for all set S subbands, a relative power indicator  is reported for all set S subbands, a second precoding matrix indicator  for all set S subbands and another second precoding matrix indicator  for or the M selected subbands.

For transmission modes 4, 8, 9 and 10, the reported PMI and CQI values and RPI value (if reported) are calculated conditioned on the reported RI. For other transmission modes they are reported conditioned on rank 1. If CRI is reported, the reported PMI, CQI, and RI values are calculated conditioned on the reported CRI.

For all UE-selected subband feedback modes the UE shall report the positions of the M selected subbands using a combinatorial index r defined as

where the set , () contains the M sorted subband indices and  is the extended binomial coefficient, resulting in unique label .

The CQI value for the M selected subbands for each codeword is encoded differentially using 2-bits relative to its respective wideband CQI as defined by

Differential CQI offset level = M selected subbands CQI index – wideband CQI index

The mapping from the 2-bit differential CQI value to the offset level is shown in Table 7.2.1-4.

Table 7.2.1-4: Mapping differential CQI value to offset level

| Differential CQI value | Offset level |
| --- | --- |
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |

Supported subband size k and M values include those shown in Table 7.2.1-5A when the CSI request field from an uplink DCI format 7-0A/7-0B is set to trigger a report, in Table 7.2.1-5 otherwise. In Table 7.2.1-5 the k and M values are a function of system bandwidth.

The number of bits to denote the position of the M selected subbands is .

For a BL/CE UE, the reported CQI values are calculated conditioned on rank 1.

- UE-selected subband feedback

- Mode 2-0 description:

- The UE shall report one wideband CQI value which is calculated assuming transmission on all narrowband(s) in the CSI reference resource.

- If frequency hopping is configured for MPDCCH,

- the UE shall select M=1 preferred narrowband defined in Clause 6.2.7 of [3] within the set of narrowband(s) in which MPDCCH is monitored.

- the UE shall also report one CQI value reflecting transmission only over the selected narrowband determined in the previous step.

- The CQI value for the M=1 selected narrowband is encoded differentially using 2-bits relative to its respective wideband CQI as defined by

- Differential CQI offset level = selected narrowband CQI index – wideband CQI index

- The mapping from the 2-bit differential CQI value to the offset level is shown in Table 7.2.1-4.

- the UE shall report the positions of the M=1 selected narrowband according to Table 7.2.1-6.

- otherwise,

- the UE shall report a Differential CQI value = 0 and a position of the M=1 selected narrowband according to Table 7.2.1-6.

Table 7.2.1-5: Subband Size (k) and Number of Subbands (M) in S vs. Downlink System Bandwidth

| System Bandwidth | Subband Size k (RBs) | M |
| --- | --- | --- |
|  |  |  |
| 6 – 7 | NA | NA |
| 8 – 10 | 2 | 1 |
| 11 – 26 | 2 | 3 |
| 27 – 63 | 3 | 5 |
| 64 – 110 | 4 | 6 |

Table 7.2.1-5A: Subband Size (k) and Number of Subbands (M) in S vs. Downlink System Bandwidth when the CSI request field from an uplink DCI format 7-0A/7-0B is set to trigger a report

| System Bandwidth | Subband Size k (RBs) | M |
| --- | --- | --- |
|  |  |  |
| 6 – 7 | NA | NA |
| 8 – 11 | 4 | 1 |
| 12 – 26 | 12 | 1 |
| 27 – 63 | 12 | 2 |
| 64 – 110 | 12 | 4 |

Table 7.2.1-6: Reporting UE selected narrowband position for BL/CE UEs

| Number of narrowbands for MPDCCH monitoring | UE reported bit(s) for narrowband position (MSB, LSB) | MPDCCH Narrowband Reported |
| --- | --- | --- |
| 1 | 0 | The narrowband used for MPDCCH monitoring |
| 2 | 0 | Narrowband with lowest narrowband index |
|  | 1 | Narrowband with highest narrowband index |
| 4 | 00 | Narrowband with lowest narrowband index |
|  | 01 | Narrowband with second lowest narrowband index |
|  | 10 | Narrowband with third lowest narrowband index |
|  | 11 | Narrowband with highest narrowband index |

### 7.2.2 Periodic CSI Reporting using PUCCH

A UE is semi-statically configured by higher layers to periodically feed back different CSI components (CQI, PMI, PTI, CRI, and/or RI) on the PUCCH using the reporting modes given in Table 7.2.2-1 and described below. A UE in transmission mode 10 can be configured by higher layers for multiple periodic CSI reports corresponding to one or more CSI processes per serving cell on PUCCH.

A BL/CE UE configured with CEModeB is not expected to be configured with periodic CSI report.

If a UE is configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured,

- one of the following CSI reporting modes given in Table 7.2.2-1 is configured only for eMIMO-Type2

- the UE shall not transmit CQI, PTI, and second precoding matrix indicator  for eMIMO-Type for any CSI reporting mode in Table 7.2.2-1

- the UE shall not transmit RI for eMIMO-Type and for any CSI reporting mode in Table 7.2.2-1 except if the maximum number of supported layers for spatial multiplexing in DL supported by the UE is more than 2, then UE feeds back a 1-bit RI according to Table 7.2.1-1L

- the UE shall report a type 2a report consisting of wideband first PMI if RI is not transmitted, otherwise type 5 report consisting of jointly coded RI and a wideband first PMI for eMIMO-Type for any CSI reporting mode in Table 7.2.2-1, as described below.

If a UE is configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with more than one CSI-RS resource configured, and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, one of the following CSI reporting modes given in Table 7.2.2-1 is configured only for eMIMO-Type2 and the UE shall not transmit CQI, PMI, PTI, RI for eMIMO-Type for any CSI reporting mode in Table 7.2.2-1 and the UE shall report a type10 report consisting of CRI as described below.

If a UE is configured with higher layer configured parameter semiOpenLoop, except with 2 CSI-RS ports or with 4 CSI-RS ports and alternativeCodeBookEnabledFor4TX-r12=FALSE, the UE shall report a type 2a report consisting of wideband first PMI for CSI reporting modes 1-1 and 2-1 in Table 7.2.2-1, as described below.

Table 7.2.2-1: CQI and PMI Feedback Types for PUCCH CSI reporting Modes

|  |  | PMI Feedback Type |  |
| --- | --- | --- | --- |
|  |  | No PMI | Single PMI |
| PUCCH CQIFeedback Type | Wideband(wideband CQI) | Mode 1-0 | Mode 1-1 |
|  | UE Selected(subband CQI) | Mode 2-0 | Mode 2-1 |

For a non-BL/CE UE and for each of the transmission modes defined in Clause 7.1, the following periodic CSI reporting modes are supported on PUCCH:

Transmission mode 1 : Modes 1-0, 2-0

Transmission mode 2 : Modes 1-0, 2-0

Transmission mode 3 : Modes 1-0, 2-0

Transmission mode 4 : Modes 1-1, 2-1

Transmission mode 5 : Modes 1-1, 2-1

Transmission mode 6 : Modes 1-1, 2-1

Transmission mode 7 : Modes 1-0, 2-0

Transmission mode 8 : Modes 1-1, 2-1 if the UE is configured with PMI/RI reporting; modes 1-0, 2-0 if the UE is configured without PMI/RI reporting

Transmission mode 9 : Modes 1-1, 2-1 if the UE is configured with PMI/RI reporting and number of CSI-RS ports>1 and the UE is not configured with higher layer parameter advancedCodebookEnabled, or the UE is configured with higher layer parameter semiOpenLoop; mode 1-1 if the UE is configured with PMI/RI reporting and number of CSI-RS ports>1 and the UE is configured with higher layer parameter advancedCodebookEnabled; modes 1-0, 2-0 if the UE is configured without PMI/RI reporting or without PMI reporting or number of CSI-RS ports=1 or the number of CSI-RS ports in each of one or more CSI-RS resources in a CSI process is one when eMIMO-Type or eMIMO-Type2 is set to be 'CLASS B'.

Transmission mode 10 : Modes 1-1, 2-1 if the UE is configured with PMI/RI reporting and number of CSI-RS ports>1 and the UE is not configured with higher layer parameter advancedCodebookEnabled, or the UE is configured with higher layer parameter semiOpenLoop; mode 1-1 if the UE is configured with PMI/RI reporting and number of CSI-RS ports>1 and the UE is configured with higher layer parameter advancedCodebookEnabled; modes 1-0, 2-0 if the UE is configured without PMI/RI reporting or without PMI reporting or number of CSI-RS ports=1 or the number of CSI-RS ports in each of one or more CSI-RS resources in a CSI process is one when eMIMO-Type or eMIMO-Type2 is set to be 'CLASS B'.

For a BL/CE UE configured with CEModeA, the following periodic CSI reporting modes are supported on PUCCH:

Transmission mode 1 : Mode 1-0

Transmission mode 2 : Mode 1-0

Transmission mode 6 : Mode 1-1

Transmission mode 9 : Modes 1-1, 1-0 if the UE is not configured with higher layer parameter ce-CSI-RS-Feedback; mode 1-1 if the UE is configured with PMI/RI reporting and number of CSI-RS ports=8 and the UE is configured with higher layer parameter ce-CSI-RS-Feedback.

For a UE configured in transmission mode 1-9, one periodic CSI reporting mode for each activated serving cell is configured by higher-layer signalling. Additionally, one periodic CSI reporting mode can be configured by higher-layer signalling for each dormant serving cell.

For a UE configured in transmission mode 10, one or more periodic CSI reporting modes for each serving cell are configured by higher-layer signalling. Additionally, one periodic CSI reporting mode can be configured by higher-layer signalling for each dormant serving cell.

For UE in transmission mode 9 and the UE configured with higher layer parameter eMIMO-Type, the term 'CSI process' in this Clause refers to the CSI configured for the UE.

For a UE configured with transmission mode 9 or 10, and with 8 CSI-RS ports, if the UE is not configured with parameter eMIMO-Type by higher layers , or the UE is configured with parameter eMIMO-Type by higher layers, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, or the UE is configured with parameter eMIMO-Type2 by higher layers, and eMIMO-Type2 is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured,or the UE is configured with parameter eMIMO-Type by higher layers, and eMIMO-Type is set to 'CLASS B', and more than one CSI-RS resource configured, and at least one CSI-RS resource with 8 CSI-RS ports, mode 1-1 is configured to be either submode 1 or submode 2 via higher-layer signaling using the parameter PUCCH_format1-1_CSI_reporting_mode.

For a UE configured with transmission mode 8, 9 or 10, and with alternativeCodeBookEnabledFor4TX-r12=TRUE configured, if the UE is not configured with higher layer parameter eMIMO-Type, or the UE is configured with parameter eMIMO-Type by higher layers, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, or the UE is configured with parameter eMIMO-Type2 by higher layers, and eMIMO-Type2 is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, or the UE is configured with parameter eMIMO-Type by higher layers, and eMIMO-Type is set to 'CLASS B', and more than one CSI-RS resource configured, and at least one CSI-RS resource with 4 CSI-RS ports, mode 1-1 is configured to be either submode 1 or submode 2 via higher-layer signaling using the parameter PUCCH_format1-1_CSI_reporting_mode.

For the UE-selected subband CQI, a CQI report in a certain subframe of a certain serving cell describes the channel quality in a particular part or in particular parts of the bandwidth of that serving cell described subsequently as bandwidth part (BP) or parts. The bandwidth parts shall be indexed in the order of increasing frequency and non-increasing sizes starting at the lowest frequency.

For each serving cell

- There are a total of N subbands for a serving cell system bandwidth given by wheresubbands are of size k. If  then one of the subbands is of size.

- A bandwidth part j is frequency-consecutive and consists of subbands where J bandwidth parts span S or  as given in Table 7.2.2-2. If  then  is. If J>1 then  is either  or , depending on, k and J.

- Each bandwidth part j, where 0 ≤ j ≤ J-1, is scanned in sequential order according to increasing frequency.

- For UE selected subband feedback a single subband out of  subbands of a bandwidth part is selected along with a corresponding L-bit label indexed in the order of increasing frequency, where.

The CQI and PMI payload sizes of each PUCCH CSI reporting mode are given in Table 7.2.2-3.

The following CQI/PMI and RI reporting types with distinct periods and offsets are supported for the PUCCH CSI reporting modes given in Table 7.2.2-3:

- Type 1 report supports CQI feedback for the UE selected sub-bands

- Type 1a report supports subband CQI and second PMI feedback

- Type 2, Type 2b, and Type 2c report supports wideband CQI and PMI feedback

- Type 2a report supports wideband PMI feedback

- Type 3 report supports RI feedback

- Type 4 report supports wideband CQI

- Type 5 report supports RI and wideband PMI feedback

- Type 6 report supports RI and PTI feedback

- Type 7 report support CRI and RI feedback

- Type 8 report supports CRI, RI and wideband PMI feedback

- Type 9 report supports CRI, RI and PTI feedback

- Type 10 report supports CRI feedback

- Type 11 report supports RI and RPI feedback

For a UE configured in transmission mode 1-9 and for each serving cell, or for a UE configured in transmission mode 10 and for each CSI process in each serving cell, the periodicity  (in subframes) and offset  (in subframes) for CQI/PMI reporting are determined based on the parameter cqi-pmi-ConfigIndex () for the activated serving cells, given in Table 7.2.2-1A for FDD or for FDD-TDD with primary cell frame structure 1 and Table 7.2.2-1C for TDD or for FDD-TDD and primary cell frame structure type 2. For the dormant serving cells, ![](media_svg/image470.svg) [公式≈: ^{I}CQIPMI/] is given by the parameter cqi-pmi-ConfigIndexDormant. The periodicity  and relative offset  for RI reporting are determined based on the parameter ri-ConfigIndex () for the activated serving cells, given in Table 7.2.2-1B. For the serving cells in the dormant state, ![](media_svg/image473.svg) [公式≈: ^{I}RI] is given by the parameter ri-ConfigIndexDormant. For a UE configured in transmission mode 9 and for each serving cell, or for a UE configured in transmission mode 10 and for each CSI process in each serving cell, if the UE is configured with parameter eMIMO-Type by higher layers, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one, or the UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, when RI reporting is configured, the periodicity  for CRI reporting is determined based on the parameter cri-ConfigIndex () given in Table 7.2.2-1J. When the number of antenna ports in each configured CSI-RS resource is one, the periodicity  and relative offset for CRI reporting are determined based on the parameter cri-ConfigIndex () given in Table 7.2.2-1K. If a UE is configured with parameter eMIMO-Type and eMIMO-Type2, the parameters cqi-pmi-ConfigIndex, ri-ConfigIndex are for eMIMO-Type2. If a UE is configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with more than one CSI-RS resource configured, and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, the parameter cri-ConfigIndex is for eMIMO-Type. If a UE is configured with parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, the periodicity  and relative offset  for wideband first PMI/RI reporting for eMIMO-Type are determined based on the parameter periodicityOffsetIndex () given in Table 7.2.2-1L. The parameters cqi-pmi-ConfigIndex, cqi-pmi-ConfigIndexDormant, ri-ConfigIndex, ri-ConfigIndexDormant, periodicityOffsetIndex, and cri-ConfigIndex are configured by higher layer signalling. The relative reporting offset for RI  takes values from the set . If a UE is configured to report for more than one CSI subframe set then parameter cqi-pmi-ConfigIndex, ri-ConfigIndex, periodicityOffsetIndex, and cri-ConfigIndex respectively correspond to the CQI/PMI, RI, PMI/RI, and CRI periodicity and relative reporting offset for subframe set 1 and cqi-pmi-ConfigIndex2, cqi-pmi-ConfigIndex2Dormant, ri-ConfigIndex2, ri-ConfigIndex2Dormant, periodicityOffsetIndex2, and cri-ConfigIndex2 respectively correspond to the CQI/PMI, RI, PMI/RI, and CRI periodicity and relative reporting offset for subframe set 2. For a UE configured with transmission mode 10, the parameters cqi-pmi-ConfigIndex , ri-ConfigIndex, periodicityOffsetIndex, cri-ConfigIndex, cqi-pmi-ConfigIndex2, ri-ConfigIndex2, periodicityOffsetIndex2, and cri-ConfigIndex2 can be configured for each CSI process. A BL/CE UE is not expected to be configured with the parameter ri-ConfigIndex.

In the case where wideband CQI/PMI reporting is configured:

- The reporting instances for wideband CQI/PMI are subframes satisfying .

- For a UE configured in transmission mode 9 or 10, and UE configured with the parameter eMIMO-Type by higher layers, and eMIMO-Type set to 'CLASS A', and UE not configured with the parameter eMIMO-Type2, the reporting interval of wideband first PMI reporting is an integer multiple  of period  (in subframes).

- The reporting instances for wideband first PMI are subframes satisfying .

- For a UE configured in transmission mode 9 or 10, if UE is configured with parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, and RI reporting for eMIMO-Type2 is not configured, the reporting interval of wideband first PMI and RI reporting for eMIMO-Type is an integer multiple  of period  (in subframes).

- The reporting instances for wideband first PMI and RI for eMIMO-Type are subframes satisfying .

- For a UE configured in transmission mode 9 or 10, if UE is configured with parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with more than one CSI-RS resource configured, and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, and RI reporting for eMIMO-Type2 is not configured, the reporting interval of CRI reporting for eMIMO-Type is an integer multiple  of period  (in subframes)

- The reporting instances for CRI are subframes satisfying .

- In case RI reporting is configured, the reporting interval of the RI reporting, or RI and RPI reporting if UE is configured in transmission mode 9 or 10, and with higher layer parameter advancedCodebookEnabled=TRUE, is an integer multiple  of period  (in subframes).

- The reporting instances for RI or RI and RPI are subframes satisfying .

- For a UE configured in transmission mode 9 or 10, and UE configured with parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, the reporting interval of wideband first PMI and RI reporting for eMIMO-Type is an integer multiple  of period  (in subframes).

- The reporting instances for wideband first PMI and RI for eMIMO-Type are subframes satisfying .

- In case CRI reporting is configured,

- if the number of antenna ports in each configured CSI-RS resource is one,

- the reporting interval of the CRI reporting is an integer multiple  of period  (in subframes)

- The reporting instances for CRI are subframes satisfying .

- otherwise

- the reporting interval of the CRI reporting is an integer multiple  of period  (in subframes).

- The reporting instances for CRI are subframes satisfying .

In the case where both wideband CQI/PMI and subband CQI (or subband CQI/second PMI for transmission modes 9 and 10) reporting are configured:

- The reporting instances for wideband CQI/PMI and subband CQI (or subband CQI/second PMI for transmission modes 9 and 10) are subframes satisfying .

- For a UE configured in transmission mode 9 or 10, if UE is configured with parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, and RI reporting for eMIMO-Type2 is not configured, the reporting interval of wideband first PMI and RI reporting for eMIMO-Type is an integer multiple  of period  (in subframes).

- The reporting instances for wideband first PMI and RI for eMIMO-Type are subframes satisfying .

- For a UE configured in transmission mode 9 or 10, if UE is configured with parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS B' with more than one CSI-RS resource configured, and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, and RI reporting for eMIMO-Type2 is not configured, the reporting interval of CRI reporting for eMIMO-Type is an integer multiple  of period  (in subframes)

- The reporting instances for CRI are subframes satisfying .

- When PTI is not transmitted (due to not being configured) or the most recently transmitted PTI is equal to 1 for a UE configured in transmission modes 8 and 9, or for a UE configured in transmission mode 10 without a 'RI-reference CSI process' for a CSI process, or the transmitted PTI is equal to 1 reported in the most recent RI reporting instance for a CSI process when a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for the CSI process, or the transmitted PTI is equal to 1 for a 'RI-reference CSI process' reported in the most recent RI reporting instance for a CSI process when a UE is configured in transmission mode 10 with the 'RI-reference CSI process' for the CSI process, and the most recent type 6 report for the CSI process is dropped:

- The wideband CQI/ wideband PMI (or wideband CQI/wideband second PMI for transmission modes 8, 9 and 10) report has period , and is reported on the subframes satisfying . The integer  is defined as , where  is the number of bandwidth parts.

- Between every two consecutive wideband CQI/ wideband PMI (or wideband CQI/wideband second PMI for transmission modes 8, 9 and 10) reports, the remaining  reporting instances are used in sequence for subband CQI (or subband CQI/second PMI for transmission modes 9 and 10) reports on  full cycles of bandwidth parts except when the gap between two consecutive wideband CQI/PMI reports contains less than  reporting instances due to a system frame number transition to 0, in which case the UE shall not transmit the remainder of the subband CQI (or subband CQI/second PMI for transmission modes 9 and 10) reports which have not been transmitted before the second of the two wideband CQI/ wideband PMI (or wideband CQI/wideband second PMI for transmission modes 8, 9 and 10) reports. Each full cycle of bandwidth parts shall be in increasing order starting from bandwidth part 0 to bandwidth part . The parameter is configured by higher-layer signalling.

- When the most recently transmitted PTI is 0 for a UE configured in transmission modes 8 and 9 or for a UE configured in transmission mode 10 without a 'RI-reference CSI process' for a CSI process, or the transmitted PTI is 0 reported in the most recent RI reporting instance for a CSI process when a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for the CSI process, or the transmitted PTI is 0 for a 'RI-reference CSI process' reported in the most recent RI reporting instance for a CSI process when a UE is configured in transmission mode 10 with the 'RI-reference CSI process' for the CSI process, and the most recent type 6 report for the CSI process is dropped:

- The wideband first precoding matrix indicator report has period , and is reported on the subframes satisfying , where is signalled by higher layers.

- Between every two consecutive wideband first precoding matrix indicator reports, the remaining reporting instances are used for a wideband second precoding matrix indicator with wideband CQI as described below

- In case RI reporting is configured, the reporting interval of RI is  times the wideband CQI/PMI period , and RI is reported on the same PUCCH cyclic shift resource as both the wideband CQI/PMI and subband CQI reports.

- The reporting instances for RI are subframes satisfying .

- For a UE configured in transmission mode 9 or 10, and UE configured with parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, the reporting interval of wideband first PMI and RI reporting for eMIMO-Type is an integer multiple  of period  (in subframes).

- The reporting instances for wideband first PMI and RI for eMIMO-Type are subframes satisfying .

- In case CRI reporting is configured,

- if the number of antenna ports in each configured CSI-RS resource is one,

- the reporting interval of the CRI reporting is  times the wideband CQI/PMI period ,

- The reporting instances for CRI are subframes satisfying .

- otherwise

- the reporting interval of the CRI reporting is  times the RI period  (in subframes).

- The reporting instances for CRI are subframes satisfying .

If the UE is configured with higher layer parameter eMIMO-Type2 for a CSI process, at the CQI, PMI, RI, PTI reporting instances for eMIMO-Type2 of the CSI process, the parameter eMIMO-Type in the rest of this Clause refers to the parameter eMIMO-Type2 for the CSI process.

If a UE is not configured with higher layer parameter eMIMO-Type, or for a CSI process a UE is configured with higher layer parameter eMIMO-Type and not configured with higher layer parameter eMIMO-Type2 and eMIMO-Type is set to 'CLASS A', or for a CSI process a UE is configured with higher layer parameter eMIMO-Type and eMIMO-Type is set to 'CLASS B', except with higher layer parameter csi-RS-NZP-mode configured, and one configured CSI-RS resource, or for a CSI process a UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and one activated CSI-RS resource, in case of collision of a CSI report with PUCCH reporting type 3, 5, 6 or 11 of one serving cell with a CSI report with PUCCH reporting type 1, 1a, 2, 2a, 2b, 2c, or 4 of the same serving cell the latter CSI report with PUCCH reporting type (1, 1a, 2, 2a, 2b, 2c, or 4), except a CSI report with PUCCH reporting type 2a for eMIMO-Type of a CSI process of the same serving cell with configured higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, has lower priority and is dropped.

If a UE is configured with higher layer parameter eMIMO-Type and not configured with higher layer parameter eMIMO-Type2 and eMIMO-Type is set to 'CLASS A' for a CSI process, in case of collision of a CSI report with PUCCH reporting type 2a of one serving cell with a CSI report with PUCCH reporting type 1, 1a, 2, 2b, 2c, or 4 of the same serving cell, the latter CSI report with PUCCH reporting type (1, 1a, 2, 2b, 2c, or 4) has lower priority and is dropped.

If a UE is not configured with higher layer parameter format4-MultiCSI-resourceConfiguration or format5-MultiCSI-resourceConfiguration, for a CSI process, if a UE is configured with higher layer parameter eMIMO-Type except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B', and more than one configured CSI-RS resources, or a UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and more than one activated CSI-RS resources, in case of collision of a CSI report with PUCCH reporting type 7, 8, 9, or 10 of one serving cell with a CSI report with PUCCH reporting type 1, 1a, 2, 2a, 2b, 2c, 3, 4, 5, 6, or 11 of the same serving cell the latter CSI report with PUCCH reporting type (1, 1a, 2, 2a, 2b, 2c, 3, 4, 5, 6, or 11), except CSI report with PUCCH reporting type 2a or 5 for eMIMO-Type of a CSI process of the same serving cell with configured higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, has lower priority and is dropped.

For a CSI process, if a UE is configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, PUCCH reporting type 2a, or 5 for eMIMO-Type of the CSI process of one serving cell has the same priority with PUCCH reporting type (7, 8, 9, or 10) of the same serving cell.

For a serving cell and UE configured in transmission mode 10, in case of collision between CSI reports of same serving cell with PUCCH reporting type of the same priority, and the CSI reports corresponding to different CSI processes, the CSI reports corresponding to all CSI processes except the CSI process with the lowest csi-ProcessId-r11 are dropped.

For a serving cell and UE configured in transmission mode 1-9 and configured with CSI subframe sets  and  by the higher layer parameter csi-SubframePatternConfig-r12 for the serving cell, in case of collision between CSI reports of same serving cell with PUCCH reporting type of the same priority, the CSI report corresponding to CSI subframe set  is dropped.

For a serving cell and UE configured in transmission mode 10 and configured with CSI subframe sets  and  by the higher layer parameter csi-SubframePatternConfig-r12 for the serving cell, in case of collision between CSI reports of same serving cell with PUCCH reporting type of the same priority and the CSI reports corresponding to CSI processes with same csi-ProcessId-r11, the CSI report corresponding to CSI subframe set  is dropped.

If a UE is not configured with higher layer parameter format4-MultiCSI-resourceConfiguration or format5-MultiCSI-resourceConfiguration, and if a PUCCH format 4 or format 5 resource for HARQ-ACK according to Table 10.1.2.2.3-1 cannot be determined, and if the UE is configured with more than one serving cell, the UE transmits a CSI report of only one serving cell in any given subframe. For a given subframe, in case of collision of a CSI report with PUCCH reporting type 7, 8, 9, or 10 of one serving cell with a CSI report with PUCCH reporting type 1, 1a, 2, 2a, 2b, 2c, 3, 4, 5, 6, or 11 of another serving cell, the latter CSI with PUCCH reporting type (1, 1a, 2, 2a, 2b, 2c, 3, 4, 5, 6, or 11), except CSI report with PUCCH reporting type 2a or 5 for eMIMO-Type of a CSI process of the another serving cell with configured higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, has lower priority and is dropped. For a given subframe, in case of collision of a CSI report with PUCCH reporting type 3, 5, 6, 11, or 2a of one serving cell with a CSI report with PUCCH reporting type 1, 1a, 2, 2b, 2c, or 4 of another serving cell, the latter CSI with PUCCH reporting type (1, 1a, 2, 2b, 2c, or 4) has lower priority and is dropped. For a given subframe, in case of collision of CSI report with PUCCH reporting type 2, 2b, 2c, or 4 of one serving cell with CSI report with PUCCH reporting type 1 or 1a of another serving cell, the latter CSI report with PUCCH reporting type 1, or 1a has lower priority and is dropped. For a given subframe, if a UE is configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and eMIMO-Type is set to 'CLASS A', and eMIMO-Type2 is set to 'CLASS B' with one CSI-RS resource configured, PUCCH reporting type 2a, or 5 for eMIMO-Type of the CSI process of one serving cell has the same priority with PUCCH reporting type (7, 8, 9, or 10) of the same serving cell in case of collision of type 2a, or 5 for eMIMO-Type of the CSI process of the serving cell with PUCCH reporting types of another serving cell.

For a given subframe and serving cells with UE configured in transmission mode 1-9, in case of collision between CSI reports of these different serving cells with PUCCH reporting type of the same priority, the CSI reports for all these serving cells except the serving cell with lowest ServCellIndex are dropped.

If a UE is not configured with higher layer parameter format4-MultiCSI-resourceConfiguration or format5-MultiCSI-resourceConfiguration, and if a PUCCH format 4 or format 5 resource for HARQ-ACK according to Table 10.1.2.2.3-1 cannot be determined, for a given subframe and serving cells with UE configured in transmission mode 10, in case of collision between CSI reports of different serving cells with PUCCH reporting type of the same priority and the CSI reports corresponding to CSI processes with same csi-ProcessId-r11, the CSI reports of all serving cells except the serving cell with lowest ServCellIndex are dropped.

If a UE is not configured with higher layer parameter format4-MultiCSI-resourceConfiguration or format5-MultiCSI-resourceConfiguration, and if a PUCCH format 4 or format 5 resource for HARQ-ACK according to Table 10.1.2.2.3-1 cannot be determined, for a given subframe and serving cells with UE configured in transmission mode 10, in case of collision between CSI reports of different serving cells with PUCCH reporting type of the same priority and the CSI reports corresponding to CSI processes with different csi-ProcessId-r11, the CSI reports of all serving cells except the serving cell with CSI reports corresponding to CSI process with the lowest csi-ProcessId-r11 are dropped.

If a UE is not configured with higher layer parameter format4-MultiCSI-resourceConfiguration or format5-MultiCSI-resourceConfiguration, and if a PUCCH format 4 or format 5 resource for HARQ-ACK according to Table 10.1.2.2.3-1 cannot be determined, for a given subframe, in case of collision between CSI report of a given serving cell with UE configured in transmission mode 1-9, and CSI report(s) corresponding to CSI process(es) of a different serving cell with the UE configured in transmission mode 10, and the CSI reports of the serving cells with PUCCH reporting type of the same priority, the CSI report(s) corresponding to CSI process(es) with csi-ProcessId-r11 > 1 of the different serving cell are dropped.

If a UE is not configured with higher layer parameter format4-MultiCSI-resourceConfiguration or format5-MultiCSI-resourceConfiguration, and if a PUCCH format 4 or format 5 resource for HARQ-ACK according to Table 10.1.2.2.3-1 cannot be determined, for a given subframe, in case of collision between CSI report of a given serving cell with UE configured in transmission mode 1-9, and CSI report corresponding to CSI process with csi-ProcessId-r11 = 1 of a different serving cell with the UE configured in transmission mode 10, and the CSI reports of the serving cells with PUCCH reporting type of the same priority, the CSI report of the serving cell with highest ServCellIndex is dropped.

See Clause 10.1 for UE behaviour regarding collision between CSI and HARQ-ACK and the corresponding PUCCH format assignment.

If a UE is not configured with higher layer parameter format4-MultiCSI-resourceConfiguration or format5-MultiCSI-resourceConfiguration, and if a PUCCH format 4 or format 5 resource for HARQ-ACK according to Table 10.1.2.2.3-1 cannot be determined, the CSI report of a given PUCCH reporting type shall be transmitted on the PUCCH resource  as defined in [3], where  is UE specific and configured by higher layers for each serving cell.

If a UE is not configured with higher layer parameter format4-MultiCSI-resourceConfiguration or format5-MultiCSI-resourceConfiguration, and

- if the UE is not configured for simultaneous PUSCH and PUCCH transmission or,

- if the UE is configured for simultaneous PUSCH and PUCCH transmission and not transmitting PUSCH,

in case of collision between CSI and positive SR in a same subframe, CSI is dropped.

If a UE is configured with format4-MultiCSI-resourceConfiguration or format5-MultiCSI-resourceConfiguration, for a subframe in which only periodic CSI and SR (if any) is transmitted,

if there is only one CSI report in the subframe,

the CSI report of a given PUCCH reporting type shall be transmitted on the PUCCH resource  as defined in [3], where  is UE specific and configured by higher layers for each serving cell;

In case of collision between CSI and positive SR in a same subframe, if the UE is not configured for simultaneous PUSCH and PUCCH transmission, or if the UE is configured for simultaneous PUSCH and PUCCH transmission and not transmitting PUSCH, CSI is dropped.

if there are more than one CSI reports in the subframe,

if the parameter simultaneousAckNackAndCQI-Format4-Format5-r13 provided by higher layers is set TRUE, when a PUCCH format 4/5 transmission of CSI reports coincides with a sub-frame configured to the UE by higher layers for transmission of a scheduling request, the UE shall transmit the CSI and SR on the PUCCH; Otherwise, CSI is dropped;

if the UE is configured with a single PUCCH format 4 resource  according to higher layer parameter format4-MultiCSI-resourceConfiguration, the PUCCH format 4 resource  is used for transmission of the CSI reports and SR (if any);

if the UE is configured with a PUCCH format 5 resource according to higher layer parameter format5-MultiCSI-resourceConfiguration, the PUCCH format 5 resource is used for transmission of the CSI reports and SR (if any);

if the UE is configured with two PUCCH format 4 resources  and according to higher layer parameter format4-MultiCSI-resourceConfiguration, if , the PUCCH format 4 resource with the smaller  between  and  is used for transmission of the CSI reports; otherwise, the PUCCH format 4 resource with the larger  between  and  is used for transmission of the CSI reports, where

is the total number of CSI report bits in the subframe;

is the number of CRC bits;

if there is no scheduling request bit in the subframe and  otherwise;

, , is the number of PRBs for  and  respectively, according to higher layer parameter numberOfPRB-format4-r13 according to Table 10.1.1-2;

if shortened PUCCH format 4 is used in the subframe and  otherwise; and

is the code rate given by higher layer parameter maximumPayloadCoderate-r13 according to Table 10.1.1-1.

If a UE transmits only periodic CSI and SR (if any) using either a PUCCH format 4  or PUCCH format 5 in a subframe and if , the UE shall select the SR (if any) and  CSI report(s) for transmission in ascending order of , where:

-  is the total number of CSI report bits in the subframe;

-  is the number of CRC bits

-  if there is no scheduling request bit in the subframe and  otherwise;

-  for PUCCH format 4 and  for PUCCH format 5, where  if shortened PUCCH format 4 or shortened PUCCH format 5 is used in the subframe and  otherwise;

-  is the code rate given by higher layer parameter maximumPayloadCoderate-r13 according to Table 10.1.1-1;

- for a CSI report of a serving cell,  for the CSI report is defined as, where

-  for CSI report type 7/8/9/10,  for CSI report type 3/5/6/2a/11,  for CSI report type 2/2b/2c/4, and  for CSI report type 1/1a;

- is the CSI process ID according to csi-ProcessId-r11 if the serving cell is configured with transmission mode 10, and  if the serving cell configured with transmission mode 1-9;

- is the serving cell index;

-  and  for CSI subframe sets  and  respectively if CSI subframe sets are configured for the serving cell, and  otherwise.

- The value of  satisfies  and , where  if there no scheduling request bit in the subframe and  otherwise.  is the number of CSI report bits for the nth CSI report in ascending order of .

If a UE is configured with format4-MultiCSI-resourceConfiguration or format5-MultiCSI-resourceConfiguratio and if the UE is configured with more than  periodic CSI reports in a subframe, the UE is not required to update CSI for more than  CSI processes from the CSI processes corresponding to all the configured CSI reports, where the value of is given by maxNumberUpdatedCSI-Proc-r13.

If a UE configured with PUCCH format 4 or PUCCH format 5 transmits UCI over PUSCH, that would have been transmitted over PUCCH format 4 or PUCCH format 5 if the UE did not have a PUSCH grant, then the UE shall select the CSI report(s) (if any) for transmission following the same procedure as for transmission over PUCCH.

Table 7.2.2-1A: Mapping of  to  and  for FDD or for FDD-TDD and primary cell frame structure type 1

|  | Value of | Value of |
| --- | --- | --- |
| 0    1 | 2 |  |
| 2    6 | 5 | – 2 |
| 7    16 | 10 | – 7 |
| 17    36 | 20 | – 17 |
| 37    76 | 40 | – 37 |
| 77    156 | 80 | – 77 |
| 157    316 | 160 | – 157 |
| = 317 | Reserved |  |
| 318    349 | 32 | – 318 |
| 350    413 | 64 | – 350 |
| 414    541 | 128 | – 414 |
| 542    601 | 60 | – 542 |
| 602    1023 | Reserved |  |

Table 7.2.2-1B: Mapping of  to  and .

|  | Value of | Value of |
| --- | --- | --- |
| 0    160 | 1 | − |
| 161    321 | 2 | − ( – 161) |
| 322    482 | 4 | − ( – 322) |
| 483    643 | 8 | − ( – 483) |
| 644    804 | 16 | − ( – 644) |
| 805    965 | 32 | − ( – 805) |
| 966    1023 | Reserved |  |

Table 7.2.2-1C: Mapping of  to  and  for TDD or for FDD-TDD and primary cell frame structure type 2

|  | Value of | Value of |
| --- | --- | --- |
| = 0 | 1 |  |
| 1    5 | 5 | – 1 |
| 6    15 | 10 | – 6 |
| 16    35 | 20 | – 16 |
| 36    75 | 40 | – 36 |
| 76    155 | 80 | – 76 |
| 156    315 | 160 | – 156 |
| 316    375 | 60 | – 316 |
| 376    1023 | Reserved |  |

Table 7.2.2-1J: Mapping of ![](media_svg/image475.svg) [公式≈: ^{I}CRI] $ I_{CRI}$ to ![](media_svg/image474.svg) [公式≈: ^{M}CRI] $ I_{CRI}$ $ M_{CRI}$ when RI reporting is configured

|  | Value of $ M_{CRI}$![](media_svg/image474.svg) [公式≈: ^{M}CRI] |
| --- | --- |
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |
| 6 | 64 |
| 7 | 128 |
| 7<1023 | Reserved |

Table 7.2.2-1K: Mapping of ![](media_svg/image475.svg) [公式≈: ^{I}CRI]$ M_{CRI}$ to ![](media_svg/image474.svg) [公式≈: ^{M}CRI] $ M_{CRI}$ $ M_{CRI}$ and $ N_{OFFSET,CRI}$ when the number of antenna ports in each configured CSI-RS resource is one

| ![](media_svg/image475.svg) [公式≈: ^{I}CRI] | Value of ![](media_svg/image474.svg) [公式≈: ^{M}CRI]$ M_{CRI}$ | Value of |
| --- | --- | --- |
| 0  ![](media_svg/image475.svg) [公式≈: ^{I}CRI]$ I_{CRI}$  160 | 1 | −![](media_svg/image475.svg) [公式≈: ^{I}CRI]$ I_{CRI}$ |
| 161  ![](media_svg/image475.svg) [公式≈: ^{I}CRI]$ I_{CRI}$  321 | 2 | − ($ I_{CRI}$![](media_svg/image475.svg) [公式≈: ^{I}CRI] – 161) |
| 322  ![](media_svg/image475.svg) [公式≈: ^{I}CRI]$ I_{CRI}$  482 | 4 | − ($ I_{CRI}$![](media_svg/image475.svg) [公式≈: ^{I}CRI]– 322) |
| 483  ![](media_svg/image475.svg) [公式≈: ^{I}CRI]$ I_{CRI}$  643 | 8 | − ($ I_{CRI}$![](media_svg/image475.svg) [公式≈: ^{I}CRI] – 483) |
| 644  ![](media_svg/image475.svg) [公式≈: ^{I}CRI]$ I_{CRI}$  804 | 16 | − ($ I_{CRI}$![](media_svg/image475.svg) [公式≈: ^{I}CRI] – 644) |
| 805  ![](media_svg/image475.svg) [公式≈: ^{I}CRI]$ I_{CRI}$  965 | 32 | − ($ I_{CRI}$![](media_svg/image475.svg) [公式≈: ^{I}CRI]– 805) |
| 966  ![](media_svg/image475.svg) [公式≈: ^{I}CRI]$ I_{CRI}$  1023 | Reserved |  |

Table 7.2.2-1L: Mapping of ![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI]$ M_{CRI}$ to ![](media_svg/image555.svg) [公式≈: ^{M}PMI/RI] $ M_{CRI}$ and ![](media_svg/image556.svg) [公式≈: ^{N}OFFSET,PMI/RI]$ M_{CRI}$ $ M_{CRI}$ $ N_{OFFSET,CRI}$

| ![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI] | Value of ![](media_svg/image557.svg) [公式≈: ^{M}PMI/RI]$ M_{CRI}$ | Value of ![](media_svg/image558.svg) [公式≈: ^{N}OFFSET,PMI/RI] |
| --- | --- | --- |
| 0  ![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI]$ I_{CRI}$  160 | 1 | −![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI]$ I_{CRI}$ |
| 161  ![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI]$ I_{CRI}$  321 | 2 | − ($ I_{CRI}$![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI] – 161) |
| 322  ![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI]$ I_{CRI}$  482 | 4 | − ($ I_{CRI}$![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI]– 322) |
| 483  ![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI]$ I_{CRI}$  643 | 8 | − ($ I_{CRI}$![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI] – 483) |
| 644  ![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI]$ I_{CRI}$  804 | 16 | − ($ I_{CRI}$![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI] – 644) |
| 805  ![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI]$ I_{CRI}$  965 | 32 | − ($ I_{CRI}$![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI]– 805) |
| 966  ![](media_svg/image554.svg) [公式≈: ^{I}PMI/RI]$ I_{CRI}$  1023 | Reserved |  |

For TDD or FDD-TDD and primary cell frame structure type 2 periodic CQI/PMI reporting, the following periodicity values apply for a serving cell c depending on the TDD UL/DL configuration of the primary cell [3], where the UL/DL configuration corresponds to the eimta-HARQ-ReferenceConfig-r12 for the primary cell if the UE is configured with the parameter EIMTA-MainConfigServCell-r12 for the primary cell, or to the harq-ReferenceConfig-r14 for the primary cell when the UE is configured with the parameter harq-ReferenceConfig-r14:

- The reporting period of  is applicable for the serving cell c only if TDD UL/DL configuration of the primary cell belongs to {0, 1, 3, 4, 6}, and where all UL subframes of the primary cell in a radio frame are used for CQI/PMI reporting.

- The reporting period of  is applicable for the serving cell c only if TDD UL/DL configuration of the primary cell belongs to {0, 1, 2, 6}.

- The reporting periods of  are applicable for the serving cell c for any TDD UL/DL configuration of the primary cell.

For a serving cell with , Mode 2-0 and Mode 2-1 are not supported for that serving cell.

The sub-sampled codebook for PUCCH mode 1-1 submode 2 for 8 CSI-RS ports is defined in Table 7.2.2-1D for first and second precoding matrix indicator  and . Joint encoding of rank and first precoding matrix indicator  for PUCCH mode 1-1 submode 1 for 8 CSI-RS ports is defined in Table 7.2.2-1E. The sub-sampled codebook for PUCCH mode 2-1 for 8 CSI-RS ports is defined in Table 7.2.2-1F for PUCCH Reporting Type 1a. For a BL/CE UE configured with CEModeA and PUCCH mode 1-1 for 8 CSI-RS ports, the entries in Table 7.2.2-1D and Table 7.2.2-1E corresponding to rank 1 are used, and the codebook indices  and  are given in Table 7.2.4-1.

For a UE configured with transmission mode 9 or 10, and the UE configured with parameter eMIMO-Type by higher layers, and eMIMO-Type is set to 'CLASS A', and PUCCH Reporting Type 1a, the sub-sampled codebook for PUCCH mode 2-1 for value of parameter codebookConfig set to 2, 3, or 4 is defined in Table 7.2.2-1F, for value of parameter codebookConfig set to 1, the value of the second PMI, , is set to .

Table 7.2.2-1D: PUCCH mode 1-1 submode 2 codebook subsampling

| RI | Relationship between the first PMI value and codebook index |  | Relationship between the second PMI value and codebook index |  | total |
| --- | --- | --- | --- | --- | --- |
|  | Value of the first PMI | Codebook index | Value of the second PMI | Codebook index | #bits |
| 1 | 0-7 |  | 0-1 |  | 4 |
| 2 | 0-7 |  | 0-1 |  | 4 |
| 3 | 0-1 |  | 0-7 |  | 4 |
| 4 | 0-1 |  | 0-7 |  | 4 |
| 5 | 0-3 |  | 0 | 0 | 2 |
| 6 | 0-3 |  | 0 | 0 | 2 |
| 7 | 0-3 |  | 0 | 0 | 2 |
| 8 | 0 | 0 | 0 | 0 | 0 |

Table 7.2.2-1E: Joint encoding of RI and  for PUCCH mode 1-1 submode 1

| Value of joint encoding of RI and the first PMI | RI | Codebook index |
| --- | --- | --- |
| 0-7 | 1 |  |
| 8-15 | 2 |  |
| 16-17 | 3 |  |
| 18-19 | 4 |  |
| 20-21 | 5 |  |
| 22-23 | 6 |  |
| 24-25 | 7 |  |
| 26 | 8 | 0 |
| 27-31 | reserved | NA |

Table 7.2.2-1F: PUCCH mode 2-1 codebook subsampling

| RI | Relationship between the second PMI value and codebook index |  |
| --- | --- | --- |
|  | Value of the second PMI | Codebook index |
| 1 | 0-15 |  |
| 2 | 0-3 |  |
| 3 | 0-3 |  |
| 4 | 0-3 |  |
| 5 | 0 | 0 |
| 6 | 0 | 0 |
| 7 | 0 | 0 |
| 8 | 0 | 0 |

The sub-sampled codebook for PUCCH mode 1-1 submode 2 for transmission modes 8, 9 and 10 configured with alternativeCodeBookEnabledFor4TX-r12=TRUE is defined in Table 7.2.2-1G for first and second precoding matrix indicator  and. Joint encoding of rank and first precoding matrix indicator  for PUCCH mode 1-1 submode 1 for transmission modes 8, 9 and 10 configured with alternativeCodeBookEnabledFor4TX-r12=TRUE is defined in Table 7.2.2-1H. The sub-sampled codebook for PUCCH mode 2-1 for transmission modes 8, 9 and 10 configured with alternativeCodeBookEnabledFor4TX-r12=TRUE is defined in Table 7.2.2-1I for PUCCH Reporting Type 1a.

Table 7.2.2-1G: PUCCH mode 1-1 submode 2 codebook subsampling with 4 antenna ports

| RI | Relationship between the first PMI value and codebook index |  | Relationship between the second PMI value and codebook index |  | total |
| --- | --- | --- | --- | --- | --- |
|  | Value of the first PMI | Codebook index | Value of the second PMI | Codebook index | #bits |
| 1 | 0-3 |  | 0-3 |  | 4 |
| 2 | 0-3 |  | 0-3 |  | 4 |
| 3 | 0 | 0 | 0-15 |  | 4 |
| 4 | 0 | 0 | 0-15 |  | 4 |

Table 7.2.2-1 H: Joint encoding of RI and for PUCCH mode 1-1 submode 1 with 4 antenna ports

| Value of joint encoding of RI and the first PMI | RI | Codebook index |
| --- | --- | --- |
|  |  |  |
| 0-7 | 1 |  |
| 8-15 | 2 |  |
| 16 | 3 | 0 |
| 17 | 4 | 0 |
| 18-31 | reserved | NA |

Table 7.2.2-1 I: PUCCH mode 2-1 codebook subsampling with 4 antenna ports

| RI | Relationship between the second PMI value and codebook index |  |
| --- | --- | --- |
|  | Value of the second PMI | Codebook index |
| 1 | 0-15 |  |
| 2 | 0-3 |  |
| 3 | 0-3 |  |
| 4 | 0-3 |  |

For a UE configured with transmission mode 9 or 10, and the UE configured with parameter advancedCodebookEnabled=TRUE and and PUCCH Reporting Type 2b, the sub-sampled codebook for PUCCH mode 1-1 for value of  is defined in Table 7.2.2-1H, and for value of , the value of the second PMI, , is set to .

Table 7.2.2-1H: PUCCH mode 1-1 codebook subsampling, with parameter advancedCodebookEnabled=TRUE,

| Relationship between the second PMI value and codebook index |  |
| --- | --- |
| Value of the second PMI | Codebook index |
| 0 | 2048 |
| 1 | 2113 |
| 2 | 2178 |
| 3 | 2243 |
| 4 | 2568 |
| 5 | 2633 |
| 6 | 2698 |
| 7 | 2763 |
| 8 | 3348 |
| 9 | 3413 |
| 10 | 3478 |
| 11 | 3543 |
| 12 | 3868 |
| 13 | 3933 |
| 14 | 3998 |
| 15 | 4063 |

An CRI or RI or PTI or any precoding matrix indicator reported for a serving cell in a periodic reporting mode is valid only for CSI reports for that serving cell on that periodic CSI reporting mode.

For serving cell , a UE configured in transmission mode 10 with PMI/RI reporting or without PMI reporting for a CSI process can be configured with a 'RI-reference CSI process'. The RI for the 'RI-reference CSI process' is not based on any other configured CSI process other than the 'RI-reference CSI process'. If the UE is configured with a 'RI-reference CSI process' for a CSI process and if subframe sets  and  are configured by higher layers for only one of the CSI processes then the UE is not expected to receive configuration for the CSI process configured with the subframe subsets that have a different set of restricted RIs with precoder codebook subset restriction between the two subframe sets.The UE is not expected to receive configurations for the CSI process and the 'RI-reference CSI process' that have a different:

- periodic CSI reporting mode (including sub-mode if configured), and/or

- number of CSI-RS antenna ports, and/or

- set of restricted RIs with precoder codebook subset restriction if subframe sets  and  are not configured by higher layers for both CSI processes, and/or

- set of restricted RIs with precoder codebook subset restriction for each subframe set if subframe sets  and  are configured by higher layers for both CSI processes, and/or

- set of restricted RIs with precoder codebook subset restriction if subframe sets  and  are configured by higher layers for only one of the CSI processes, and the set of restricted RIs for the two subframe sets are the same, and/or

- number of CSI-RS antenna ports for any two CSI-RS resources for the two CSI processes, if a UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one for at least one of the two CSI processes, and/or

- set of restricted RIs with precoder codebook subset restriction for any two CSI-RS resources for the two CSI processes, if a UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one for at least one of the two CSI processes and if subframe sets  and  are not configured by higher layers for both CSI processes, and/or

- set of restricted RIs with precoder codebook subset restriction for each subframe set and for any two CSI-RS resources for the two CSI processes, if a UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one for at least one of the two CSI processes and if subframe sets  and  are configured by higher layers for both CSI processes, and/or

- set of restricted RIs with precoder codebook subset restriction for any two CSI-RS resources for the two CSI processes, if a UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one for at least one of the two CSI processes and if subframe sets  and  are configured by higher layers for only one of the CSI processes, and the set of restricted RIs for the two subframe sets are the same.

If a UE is configured for CRI reporting,

- For the calculation of CQI/PMI/RI conditioned on the last reported CRI, in the absence of a last reported CRI the UE shall conduct the CQI/PMI/RI calculation conditioned on the lowest possible CRI. If reporting for more than one CSI subframe set is configured, CQI/PMI/RI is conditioned on the last reported CRI linked to the same subframe set as the CSI report.

- For the calculation of CQI/PMI conditioned on the last reported RI and CRI, in the absence of a last reported RI and CRI, the UE shall conduct the CQI/PMI calculation conditioned on the lowest possible RI associated with the lowest possible CRI and as given by the bitmap parameter codebookSubsetRestriction and the parameter alternativeCodeBookEnabledFor4TX-r12 if configured. If reporting for more than one CSI subframe set is configured, CQI/PMI is conditioned on the last reported RI associated with the last reported CRI and linked to the same subframe set as the CSI report

otherwise,

- For the calculation of CQI/PMI conditioned on the last reported RI, in the absence of a last reported RI the UE shall conduct the CQI/PMI calculation conditioned on the lowest possible RI as given by the bitmap parameter codebookSubsetRestriction and the parameter alternativeCodeBookEnabledFor4TX-r12 if configured. If reporting for more than one CSI subframe set is configured, CQI/PMI is conditioned on the last reported RI linked to the same subframe set as the CSI report.

For a non-BL/CE UE, the periodic CSI reporting modes are described as following:

Wideband feedback

Mode 1-0 description:

In the subframe where RI is reported (only for transmission mode 3, and transmission mode 9 or 10 without PMI reporting with one configured CSI-RS resource or with more than one configured CSI-RS resource and the number of CSI-RS ports of the selected CSI-RS resource is more than one):

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, for transmission mode 3 the UE shall determine a RI assuming transmission on set S subbands, and for transmission mode 9 or 10 without PMI reporting, the UE shall determine a RI assuming transmission on set S subbands, and conditioned on the last reported periodic CRI if the UE is configured with CRI reporting.

The UE shall report a type 3 report consisting of one RI.

In the subframe where RI and CRI is reported (for transmission mode 9 or 10 without PMI reporting and without higher layer parameter csi-RS-NZP-mode configured, and number of configured CSI-RS resources more than one, and for transmission mode 9 or 10 without PMI reporting and with higher layer parameter csi-RS-NZP-mode set to 'multiShot', and number of activated CSI-RS resources more than one):

A UE shall determine a CRI assuming transmission on set S subbands.

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands conditioned on the reported CRI.

The UE shall report a type 7 report consisting of one RI and one CRI.

In the subframe where CRI is reported (only for transmission mode 9 or 10 with CRI reporting and the number of antenna ports in each of configured CSI-RS resources is one):

A UE shall determine a CRI assuming transmission on set S subbands.

The UE shall report a type10 report consisting of one CRI.

In the subframe where CQI is reported:

If the UE is configured without PMI reporting (only for transmission mode 9 or 10):

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands.

A UE shall report a type 4 report consisting of

A single wideband CQI value which is calculated assuming the use of a single precoding matrix in all subbands and transmission on set S subbands.

When RI>1, an additional 3-bit wideband spatial differential CQI, which is shown in Table 7.2-2.

If the UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a ''RI-reference CSI process'' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the ''RI-reference CSI process'' is reported in the most recent RI reporting instance for the CSI process, the selected precoding matrix and CQI for the CSI process are calculated conditioned on the reported periodic RI for the configured ''RI-reference CSI process'' in the most recent RI reporting instance for the CSI process and last reported periodic CRI for the CSI process; otherwise the selected precoding matrix and CQI are calculated conditioned on the last reported periodic RI and the last reported periodic CRI.

otherwise,

If a UE is configured in transmission mode 10 with a ''RI-reference CSI process'' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the ''RI-reference CSI process'' is reported in the most recent RI reporting instance for the CSI process, the selected precoding matrix and CQI for the CSI process are calculated conditioned on the reported periodic RI for the configured ''RI-reference CSI process'' in the most recent RI reporting instance for the CSI process; otherwise the selected precoding matrix and CQI are calculated conditioned on the last reported periodic RI.

otherwise,

A UE shall report a type 4 report consisting of one wideband CQI value which is calculated assuming transmission on set S subbands. The wideband CQI represents channel quality for the first codeword, even when RI>1.

For transmission mode 3 the CQI is calculated conditioned on the last reported periodic RI. For other transmission modes it is calculated conditioned on transmission rank 1. If the UE is configured with CRI reporting, the CQI is calculated conditioned on the last reported periodic CRI.

Mode 1-1 description:

In the subframe where RI is reported (only for transmission modes 4, 8, 9 and 10):

If the UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands conditioned on the last reported periodic CRI.

otherwise,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands.

The UE shall report a type 3 report consisting of one RI.

In the subframe where RI and CRI is reported for transmission modes 9 and 10:

A UE shall determine a CRI assuming transmission on set S subbands.

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands conditioned on the reported CRI for the CSI process.

The UE shall report a type 7 report consisting of one RI and one CRI.

In the subframe where RI and RPI is reported for transmission modes 9 and 10:

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands.

If the determined , RPI is set to 0; otherwise UE shall determine a RPI assuming transmission on set S subbands.

The UE shall report a type 11 report consisting of one RI and one RPI.

In the subframe where RI and a first PMI are reported for transmission modes 9 and 10 configured with submode 1 and 8 CSI-RS ports without CRI reporting and not configured with advancedCodebookEnabled or 8 CSI-RS ports or 4 CSI-RS ports with alternativeCodeBookEnabledFor4TX-r12=TRUE in the selected CSI-RS resource and UE is configured with CRI reporting, and for transmission modes 8, 9 and 10 configured with submode 1 and alternativeCodeBookEnabledFor4TX-r12=TRUE without CRI reporting and not configured with advancedCodebookEnabled:

If the UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands conditioned on the last reported periodic CRI.

otherwise,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands.

The UE shall report a type 5 report consisting of jointly coded RI and a first PMI corresponding to a set of precoding matrices selected from the codebook subset assuming transmission on set S subbands.

If the UE is configured with CRI reporting,

If the UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process and in case of collision of type 5 report for the CSI process with type 5 report for the 'RI-reference CSI process', the wideband first PMI for the CSI process shall be the same as the wideband first PMI in the most recent type 5 report for the configured 'RI-reference CSI process'; otherwise, the wideband first PMI value is calculated conditioned on the reported periodic RI and last reported periodic CRI.

otherwise,

If the UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process and in case of collision of type 5 report for the CSI process with type 5 report for the 'RI-reference CSI process', the wideband first PMI for the CSI process shall be the same as the wideband first PMI in the most recent type 5 report for the configured 'RI-reference CSI process'; otherwise, the wideband first PMI value is calculated conditioned on the reported periodic RI.

In the subframe where CRI, RI and a first PMI are reported for transmission modes 9, and 10 configured with submode 1 and 8 CSI-RS ports in at least one of the configured CSI-RS resources, or for transmission modes 8, 9 and 10 configured with submode 1 and alternativeCodeBookEnabledFor4TX-r12=TRUE and 4 CSI-RS ports in at least one of configured CSI-RS resources:

A UE shall determine a CRI assuming transmission on set S subbands.

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands conditioned on the reported CRI.

If the configured CSI-RS resource corresponding to the determined CRI comprises 8 CSI-RS ports or 4 CSI-RS ports with alternativeCodeBookEnabledFor4TX-r12=TRUE, the UE shall report a type 8 report consisting of jointly coded CRI, RI and a first PMI corresponding to a set of precoding matrices selected from the codebook subset assuming transmission on set S subbands. Otherwise, the UE shall report a type 8 report consisting of jointly coded CRI, RI and a first PMI fixed to zero.

If the UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process and in case of collision of type 5 report for the CSI process with type 5 report for the 'RI-reference CSI process', the wideband first PMI for the CSI process shall be the same as the wideband first PMI in the most recent type 5 report for the configured 'RI-reference CSI process'; otherwise, the wideband first PMI value is calculated conditioned on the reported periodic RI and last reported periodic CRI conditioned on the reported CRI.

In the subframe where the wideband first PMI is reported, for transmission modes 9 and 10 with higher layer parameter eMIMO-Type configured, and eMIMO-Type set to 'CLASS A', or for transmission modes 9 and 10 with higher layer parameter advancedCodebookEnabled =TRUE configured, and last reported periodic ,

A set of precoding matrices corresponding to the wideband first PMI is selected from the codebook assuming transmission on set S subbands.

A UE shall report a type 2a report consisting of the wideband first PMI corresponding to the selected set of precoding matrices.

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the 'RI-reference CSI process' is reported in the most recent RI reporting instance for the CSI process, the wideband first PMI value for the CSI process is calculated conditioned on the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process; otherwise the wideband first PMI value is calculated conditioned on the last reported periodic RI.

In the subframe where CQI/PMI is reported for all transmission modes except with,

UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', or

UE configured with higher layer parameter advancedCodebookEnabled=TRUE, and last reported periodic , or

## 8 CSI-RS ports configured for transmission modes 9 and 10, or with alternativeCodeBookEnabledFor4TX-r12=TRUE configured for transmission modes 8, 9 and 10, if the UE is not configured with higher layer parameter eMIMO-Type, or UE configured with CRI reporting, or UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured:

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands.

A UE shall report a type 2 report consisting of

A single wideband CQI value which is calculated assuming the use of a single precoding matrix in all subbands and transmission on set S subbands.

The selected single PMI (wideband PMI).

When RI>1, an additional 3-bit wideband spatial differential CQI, which is shown in Table 7.2-2.

If the UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a ''RI-reference CSI process'' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the ''RI-reference CSI process'' is reported in the most recent RI reporting instance for the CSI process, the PMI and CQI for the CSI process are calculated conditioned on the reported periodic RI for the configured ''RI-reference CSI process'' in the most recent RI reporting instance for the CSI process; otherwise the PMI and CQI are calculated conditioned on the last reported periodic RI and the last reported periodic CRI.

otherwise,

For transmission modes 4, 8, 9 and 10,

If a UE is configured in transmission mode 10 with a ''RI-reference CSI process'' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the ''RI-reference CSI process'' is reported in the most recent RI reporting instance for the CSI process, the PMI and CQI for the CSI process are calculated conditioned on the reported periodic RI for the configured ''RI-reference CSI process'' in the most recent RI reporting instance for the CSI process; otherwise the PMI and CQI are calculated conditioned on the last reported periodic RI.

For other transmission modes the PMI and CQI are calculated conditioned on transmission rank 1.

In the subframe where wideband CQI/second PMI is reported for transmission modes 9 and 10 with 8 CSI-RS ports and submode 1 without CRI reporting, or for 8 CSI-RS ports or 4 CSI-RS ports with alternativeCodeBookEnabledFor4TX-r12=TRUE in the selected CSI-RS resource and UE is configured with CRI reporting, or for transmission modes 8, 9 and 10 with submode 1 and alternativeCodeBookEnabledFor4TX-r12=TRUE without CRI reporting, or for transmission modes 9 and 10 with higher layer parameter eMIMO-Type configured, and eMIMO-Type set to 'CLASS A', or for transmission modes 9 and 10 with higher layer parameter advancedCodebookEnabled =TRUE configured, and last reported periodic :

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands.

A UE shall report a type 2b report consisting of

A single wideband CQI value which is calculated assuming the use of the single precoding matrix in all subbands and transmission on set S subbands.

The wideband second PMI corresponding to the selected single precoding matrix.

When RI>1, an additional 3-bit wideband spatial differential CQI, which is shown in Table 7.2-2.

If the UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 5 report for the CSI process is dropped, and a type 5 report for the 'RI-reference CSI process' is reported in the most recent RI reporting instance for the CSI process,

The wideband second PMI value for the CSI process is calculated conditioned on the reported periodic RI and the wideband first PMI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported periodic CRI for the CSI process.

The wideband CQI value is calculated conditioned on the selected precoding matrix for the CSI process and the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported periodic CRI for the CSI process.

Otherwise,

The wideband second PMI value is calculated conditioned on the last reported periodic RI and the wideband first PMI and the last reported periodic CRI.

The wideband CQI value is calculated conditioned on the selected precoding matrix and the last reported periodic RI and the last reported periodic CRI.

otherwise,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 5 report for the CSI process is dropped, and a type 5 report for the 'RI-reference CSI process' is reported in the most recent RI reporting instance for the CSI process,

The wideband second PMI value for the CSI process is calculated conditioned on the reported periodic RI and the wideband first PMI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process.

The wideband CQI value is calculated conditioned on the selected precoding matrix for the CSI process and the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process.

Otherwise,

The wideband second PMI value is calculated conditioned on the last reported periodic RI and the wideband first PMI.

The wideband CQI value is calculated conditioned on the selected precoding matrix and the last reported periodic RI.

In the subframe where wideband CQI/first PMI/second PMI is reported for transmission modes 9 and 10 with submode 2 and 8 CSI-RS ports configured without CRI reporting and not configured with advancedCodebookEnabled, or 8 CSI-RS ports or 4 CSI-RS ports with alternativeCodeBookEnabledFor4TX-r12=TRUE in the selected CSI-RS resource and UE is configured with CRI reporting, and for transmission modes 8, 9 and 10 with submode 2 and alternativeCodeBookEnabledFor4TX-r12=TRUE configured without CRI reporting and not configured with advancedCodebookEnabled:

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands.

A UE shall report a type 2c report consisting of

A single wideband CQI value which is calculated assuming the use of a single precoding matrix in all subbands and transmission on set S subbands.

The wideband first PMI and the wideband second PMI corresponding to the selected single precoding matrix as defined in Clause 7.2.4.

When RI>1, an additional 3-bit wideband spatial differential CQI, which is shown in Table 7.2-2.

If the UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the 'RI-reference CSI process' is reported in the most recent RI reporting instance for the CSI process, the wideband first PMI, the wideband second PMI and the wideband CQI for the CSI process are calculated conditioned on the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported periodic CRI for the CSI process; otherwise the wideband first PMI, the wideband second PMI and the wideband CQI are calculated conditioned on the last reported periodic RI and the last reported periodic CRI.

otherwise

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the 'RI-reference CSI process' is reported in the most recent RI reporting instance for the CSI process, the wideband first PMI, the wideband second PMI and the wideband CQI for the CSI process are calculated conditioned on the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process; otherwise the wideband first PMI, the wideband second PMI and the wideband CQI are calculated conditioned on the last reported periodic RI.

UE Selected subband feedback

Mode 2-0 description:

In the subframe where RI is reported (only for transmission mode 3, and transmission mode 9 or 10 without PMI reporting with one configured CSI-RS resource or with more than one configured CSI-RS resource and the number of CSI-RS ports of the selected CSI-RS is more than one):

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, for transmission mode 3 the UE shall determine a RI assuming transmission on set S subbands, and for transmission mode 9 or 10 without PMI reporting, the UE shall determine a RI assuming transmission on set S subbands, and conditioned on the last reported periodic CRI if the UE is configured with CRI reporting.

The UE shall report a type 3 report consisting of one RI.

In the subframe where RI and CRI is reported (for transmission mode 9 or 10 without PMI reporting and without higher layer parameter csi-RS-NZP-mode configured, and number of configured CSI-RS resources more than one and the number of antenna ports in at least one of the configured CSI-RS resources is more than one, and for transmission mode 9 or 10 without PMI reporting and with higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources more than one and the number of antenna ports in at least one of the activated CSI-RS resources is more than one):

A UE shall determine a CRI assuming transmission on set S subbands.

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands conditioned on the reported CRI.

The UE shall report a type 7 report consisting of one RI and one CRI.

In the subframe where CRI is reported (only for transmission mode 9 or 10 with CRI reporting and the number of antenna ports in each of configured CSI-RS resources is one):

A UE shall determine a CRI assuming transmission on set S subbands.

The UE shall report a type10 report consisting of one CRI.

In the subframe where wideband CQI is reported:

If the UE is configured without PMI reporting (only for transmission mode 9 or 10):

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands.

A UE shall report a type 4 report on each respective successive reporting opportunity consisting of

A single wideband CQI value which is calculated assuming the use of a single precoding matrix in all subbands and transmission on set S subbands.

When RI>1, an additional 3-bit wideband spatial differential CQI, which is shown in Table 7.2-2.

If the UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a ''RI-reference CSI process'' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the ''RI-reference CSI process'' is reported in the most recent RI reporting instance for the CSI process, the subband selection, selected precoding matrix and CQI for the CSI process are calculated conditioned on the reported periodic RI for the configured ''RI-reference CSI process'' in the most recent RI reporting instance for the CSI process and the last reported periodic CRI for the CSI process; otherwise the subband selection, selected precoding matrix and CQI are calculated conditioned on the last reported periodic RI and the last reported periodic CRI.

otherwise

If a UE is configured in transmission mode 10 with a ''RI-reference CSI process'' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the ''RI-reference CSI process'' is reported in the most recent RI reporting instance for the CSI process, the subband selection, selected precoding matrix and CQI for the CSI process are calculated conditioned on the reported periodic RI for the configured ''RI-reference CSI process'' in the most recent RI reporting instance for the CSI process; otherwise the subband selection, selected precoding matrix and CQI are calculated conditioned on the last reported periodic RI.

otherwise,

The UE shall report a type 4 report on each respective successive reporting opportunity consisting of one wideband CQI value which is calculated assuming transmission on set S subbands. The wideband CQI represents channel quality for the first codeword, even when RI>1.

For transmission mode 3 the CQI is calculated conditioned on the last reported periodic RI. For other transmission modes it is calculated conditioned on transmission rank 1. If the UE is configured with CRI reporting, the CQI is calculated conditioned on the last reported periodic CRI.

In the subframe where CQI for the selected subbands is reported:

If the UE is configured without PMI reporting (only for transmission mode 9 or 10):

The UE shall select the preferred subband within the set of Nj subbands in each of the J bandwidth parts where J is given in Table 7.2.2-2.

A single precoding matrix is selected from the codebook subset assuming transmission on on the selected subband within the applicable bandwidth part.

The UE shall report a type 1 report per bandwidth part on each respective successive reporting opportunity consisting of:

CQI value for codeword 0 reflecting transmission only over the selected subband of a bandwidth part determined in the previous step along with the corresponding preferred subband L-bit label.

When RI>1, an additional 3-bit subband spatial differential CQI value for codeword 1 offset level

Codeword 1 offset level = subband CQI index for codeword 0 – subband CQI index for codeword 1.

The mapping from the 3-bit subband spatial differential CQI value to the offset level is shown in Table 7.2-2.

If the UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a ''RI-reference CSI process'' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the ''RI-reference CSI process'' is reported in the most recent RI reporting instance for the CSI process, the selected precoding matrix and CQI for the CSI process are calculated conditioned on the reported periodic RI for the configured ''RI-reference CSI process'' in the most recent RI reporting instance for the CSI process and the last reported periodic CRI for the CSI process; otherwise the selected precoding matrix and CQI are calculated conditioned on the last reported periodic RI and the last reported periodic CRI.

otherwise,

If a UE is configured in transmission mode 10 with a ''RI-reference CSI process'' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the ''RI-reference CSI process'' is reported in the most recent RI reporting instance for the CSI process, the selected precoding matrix and CQI for the CSI process are calculated conditioned on the reported periodic RI for the configured ''RI-reference CSI process'' in the most recent RI reporting instance for the CSI process; otherwise the selected precoding matrix and CQI are calculated conditioned on the last reported periodic RI.

otherwise,

The UE shall select the preferred subband within the set of  subbands in each of the J bandwidth parts where J is given in Table 7.2.2-2.

The UE shall report a type 1 report consisting of one CQI value reflecting transmission only over the selected subband of a bandwidth part determined in the previous step along with the corresponding preferred subband L-bit label. A type 1 report for each bandwidth part will in turn be reported in respective successive reporting opportunities. The CQI represents channel quality for the first codeword, even when RI>1.

For transmission mode 3 the preferred subband selection and CQI values are calculated conditioned on the last reported periodic RI. For other transmission modes they are calculated conditioned on transmission rank 1. If the UE is configured with CRI reporting, the preferred subband selection and CQI values are calculated conditioned on the last reported periodic CRI.

Mode 2-1 description:

In the subframe where RI is reported for transmission mode 4, transmission mode 8 except with alternativeCodeBookEnabledFor4TX-r12=TRUE configured, transmission modes 9 and 10 with 2 CSI-RS ports, and transmission modes 9 and 10 with 4 CSI-RS ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE configured, and for transmission modes 9 and 10 with higher layer parameter eMIMO-Type configured, eMIMO-Type set to 'CLASS B', one CSI-RS resource configured, with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE:

If a UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands conditioned on the last reported periodic CRI.

otherwise,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands.

The UE shall report a type 3 report consisting of one RI.

In the subframe where RI and PTI are reported, for transmission modes 9 and 10 with 8 CSI-RS ports configured and higher layer parameter eMIMO-Type not configured, or for transmission modes 9 and 10 with 8 CSI-RS ports or 4 CSI-RS ports with alternativeCodeBookEnabledFor4TX-r12=TRUE in the selected CSI-RS resource and UE is configured with CRI reporting, or for transmission modes 9 and 10 with 8 CSI-RS ports configured and UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, or for transmission modes 9 and 10 with higher layer parameter eMIMO-Type configured, and eMIMO-Type set to 'CLASS A',or for transmission modes 8, 9 and 10 with alternativeCodeBookEnabledFor4TX-r12=TRUE configured without CRI reporting then:

If a UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands conditioned on the last reported periodic CRI.

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the PTI for the CSI process shall be the same as the PTI in the most recent type 6 report for the configured 'RI-reference CSI process'; otherwise, the UE shall determine a precoder type indication (PTI) conditioned on the last reported periodic CRI.

otherwise,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands.

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the PTI for the CSI process shall be the same as the PTI in the most recent type 6 report for the configured 'RI-reference CSI process'; otherwise, the UE shall determine a precoder type indication (PTI).

The PTI for the CSI process shall be equal to 1 if the RI reported jointly with the PTI is greater than 2 for transmission modes 8, 9, 10 with alternativeCodeBookEnabledFor4TX-r12=TRUE configured.

The UE shall report a type 6 report consisting of one RI and the PTI.

In the subframe where RI and CRI are reported for transmission modes 9 and 10 with parameter eMIMO-Type configured by higher layers, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one and RI and CRI is reported for transmission modes 9 and 10 with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one:

A UE shall determine a CRI assuming transmission on set S subbands.

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the RI for the CSI process shall be the same as the RI in the most recent CSI report comprising RI for the configured 'RI-reference CSI process' irrespective of subframe sets if configured; otherwise, the UE shall determine a RI assuming transmission on set S subbands conditioned on the reported CRI for the CSI process.

If each of the maximum number of ports in the configured CSI-RS resources is 2, or 4 except with alternativeCodeBookEnabledFor4TX-r12=TRUE configured,

The UE shall report a type 7 report consisting of one RI and one CRI.

otherwise,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, the PTI for the CSI process shall be the same as the PTI in the most recent type 6 report for the configured 'RI-reference CSI process'; otherwise, the UE shall determine a precoder type indication (PTI) conditioned on the reported CRI for the CSI process.

If the configured CSI-RS resource corresponding to the determined CRI comprises 2 CSI-RS ports or 4 CSI-RS ports except with alternativeCodeBookEnabledFor4TX-r12=TRUE configured, PTI is fixed to zero.

The PTI for the CSI process shall be equal to 1 if the RI reported jointly with the PTI is greater than 2 for transmission modes 9, 10 with alternativeCodeBookEnabledFor4TX-r12=TRUE configured.

The UE shall report a type 9 report consisting of one CRI, RI, and the PTI.

In the subframe where wideband CQI/PMI is reported for all transmission modes except with

UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', or

## 8 CSI-RS ports configured for transmission modes 9 and 10, or with alternativeCodeBookEnabledFor4TX-r12=TRUE configured for transmission modes 8, 9 and 10, if the UE is not configured with higher layer parameter eMIMO-Type, or UE is configured with CRI reporting, or UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured:

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands.

A UE shall report a type 2 report on each respective successive reporting opportunity consisting of:

A wideband CQI value which is calculated assuming the use of a single precoding matrix in all subbands and transmission on set S subbands.

The selected single PMI (wideband PMI).

When RI>1, an additional 3-bit wideband spatial differential CQI, which is shown in Table 7.2-2.

If the UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the 'RI-reference CSI process' is reported in the most recent RI reporting instance for the CSI process, the PMI and CQI values for the CSI process are calculated conditioned on the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported periodic CRI for the CSI process; otherwise the PMI and CQI values are calculated conditioned on the last reported periodic RI and the last reported periodic CRI.

otherwise,

For transmission modes 4, 8, 9 and 10,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the 'RI-reference CSI process' is reported in the most recent RI reporting instance for the CSI process, the PMI and CQI values for the CSI process are calculated conditioned on the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process; otherwise the PMI and CQI values are calculated conditioned on the last reported periodic RI.

For other transmission modes the PMI and CQI values are calculated conditioned on transmission rank 1.

In the subframe where the wideband first PMI is reported for transmission modes 9 and 10 with 8 CSI-RS ports configured and higher layer parameter eMIMO-Type not configured, or for transmission modes 9 and 10 with 8 CSI-RS ports or 4 CSI-RS ports with alternativeCodeBookEnabledFor4TX-r12=TRUE in the selected CSI-RS resource and UE is configured with CRI reporting, or for transmission modes 9 and 10 with 8 CSI-RS ports configured and UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, or for transmission modes 9 and 10 with higher layer parameter eMIMO-Type configured, and eMIMO-Type set to 'CLASS A', or for transmission modes 8, 9 and 10 with alternativeCodeBookEnabledFor4TX-r12=TRUE configured without CRI reporting:

A set of precoding matrices corresponding to the wideband first PMI is selected from the codebook subset assuming transmission on set S subbands.

A UE shall report a type 2a report on each respective successive reporting opportunity consisting of the wideband first PMI corresponding to the selected set of precoding matrices.

If the UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 6 report for the CSI process is dropped, and a type 6 report for the 'RI-reference CSI process' with PTI=0 is reported in the most recent RI reporting instance for the CSI process, the wideband first PMI value for the CSI process is calculated conditioned on the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported periodic CRI for the CSI process; otherwise with the last reported PTI=0, the wideband first PMI value is calculated conditioned on the last reported periodic RI and the last reported periodic CRI.

otherwise,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 6 report for the CSI process is dropped, and a type 6 report for the 'RI-reference CSI process' with PTI=0 is reported in the most recent RI reporting instance for the CSI process, the wideband first PMI value for the CSI process is calculated conditioned on the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process; otherwise with the last reported PTI=0, the wideband first PMI value is calculated conditioned on the last reported periodic RI.

In the subframe where wideband CQI/second PMI is reported, for transmission modes 9 and 10 with 8 CSI-RS ports configured and higher layer parameter eMIMO-Type not configured, or for transmission modes 9 and 10 with 8 CSI-RS ports or 4 CSI-RS ports with alternativeCodeBookEnabledFor4TX-r12=TRUE in the selected CSI-RS resource and UE is configured with CRI reporting, or for transmission modes 9 and 10 with 8 CSI-RS ports configured and UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, or for transmission modes 9 and 10 with higher layer parameter eMIMO-Type configured, and eMIMO-Type set to 'CLASS A',or for transmission modes 8,9, and 10 with alternativeCodeBookEnabledFor4TX-r12=TRUE configured without CRI reporting:

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands.

A UE shall report a type 2b report on each respective successive reporting opportunity consisting of:

A wideband CQI value which is calculated assuming the use of the selected single precoding matrix in all subbands and transmission on set S subbands.

The wideband second PMI corresponding to the selected single precoding matrix.

When RI>1, an additional 3-bit wideband spatial differential CQI, which is shown in Table 7.2-2.

If the UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 6 report for the CSI process is dropped, and a type 6 report for the 'RI-reference CSI process' with PTI=1 is reported in the most recent RI reporting instance for the CSI process,

The wideband second PMI value for the CSI process is calculated conditioned on the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported wideband first PMI for the CSI process and the last reported periodic CRI for the CSI process,

The wideband CQI value is calculated conditioned on the selected precoding matrix for the CSI process and the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported periodic CRI for the CSI process.

Otherwise, with the last reported PTI=1,

The wideband second PMI value is calculated conditioned on the last reported periodic RI and the wideband first PMI and the last reported periodic CRI.

The wideband CQI value is calculated conditioned on the selected precoding matrix and the last reported periodic RI and the last reported periodic CRI.

otherwise,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 6 report for the CSI process is dropped, and a type 6 report for the 'RI-reference CSI process' with PTI=1 is reported in the most recent RI reporting instance for the CSI process,

The wideband second PMI value for the CSI process is calculated conditioned on the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported wideband first PMI for the CSI process,

The wideband CQI value is calculated conditioned on the selected precoding matrix for the CSI process and the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process.

Otherwise, with the last reported PTI=1,

The wideband second PMI value is calculated conditioned on the last reported periodic RI and the wideband first PMI.

The wideband CQI value is calculated conditioned on the selected precoding matrix and the last reported periodic RI.

If the last reported first PMI was computed under an RI assumption that differs from the last reported periodic RI, or in the absence of a last reported first PMI, the conditioning of the second PMI value is not specified.

In the subframe where CQI for the selected subband is reported for all transmission modes except with

UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', or

## 8 CSI-RS ports configured for transmission modes 9 and 10, or with alternativeCodeBookEnabledFor4TX-r12=TRUE configured for transmission modes 8, 9 and 10, if the UE is not configured with higher layer parameter eMIMO-Type, or UE is configured with CRI reporting, or UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured:

The UE shall select the preferred subband within the set of Nj subbands in each of the J bandwidth parts where J is given in Table 7.2.2-2.

The UE shall report a type 1 report per bandwidth part on each respective successive reporting opportunity consisting of:

CQI value for codeword 0 reflecting transmission only over the selected subband of a bandwidth part determined in the previous step along with the corresponding preferred subband L-bit label.

When RI>1, an additional 3-bit subband spatial differential CQI value for codeword 1 offset level

Codeword 1 offset level = subband CQI index for codeword 0 – subband CQI index for codeword 1.

Assuming the use of the most recently reported single precoding matrix in all subbands and transmission on the selected subband within the applicable bandwidth part.

The mapping from the 3-bit subband spatial differential CQI value to the offset level is shown in Table 7.2-2.

If the UE is configured with CRI reporting,

F If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the 'RI-reference CSI process' is reported in the most recent RI reporting instance for the CSI process, the subband selection and CQI values for the CSI process are calculated conditioned on the last reported periodic wideband PMI for the CSI process and the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported periodic CRI for the CSI process; otherwise the subband selection and CQI values are calculated conditioned on the last reported periodic wideband PMI, RI and CRI.

otherwise,

For transmission modes 4, 8, 9 and 10,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 3 report for the CSI process is dropped, and a type 3 report for the 'RI-reference CSI process' is reported in the most recent RI reporting instance for the CSI process, the subband selection and CQI values for the CSI process are calculated conditioned on the last reported periodic wideband PMI for the CSI process and the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process; otherwise the subband selection and CQI values are calculated conditioned on the last reported periodic wideband PMI and RI.

For other transmission modes the subband selection and CQI values are calculated conditioned on the last reported PMI and transmission rank 1.

In the subframe where wideband CQI/second PMI is reported, for transmission modes 9 and 10 with 8 CSI-RS ports configured and higher layer parameter eMIMO-Type not configured, or for transmission modes 9 and 10 with 8 CSI-RS ports or 4 CSI-RS ports with alternativeCodeBookEnabledFor4TX-r12=TRUE in the selected CSI-RS resource and UE is configured with CRI reporting, or for transmission modes 9 and 10 with 8 CSI-RS ports configured and UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, or for transmission modes 9 and 10 with higher layer parameter eMIMO-Type configured, and eMIMO-Type set to 'CLASS A',or for transmission modes 8, 9 and 10 with alternativeCodeBookEnabledFor4TX-r12=TRUE configured without CRI reporting:

A single precoding matrix is selected from the codebook subset assuming transmission on set S subbands.

The UE shall report a type 2b report on each respective successive reporting opportunity consisting of:

A wideband CQI value which is calculated assuming the use of the selected single precoding matrix in all subbands and transmission on set S subbands.

The wideband second PMI corresponding to the selected single precoding matrix.

When RI>1, an additional 3-bit wideband spatial differential CQI, which is shown in Table 7.2-2.

If the UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 6 report for the CSI process is dropped, and a type 6 report for the 'RI-reference CSI process' with PTI=0 is reported in the most recent RI reporting instance for the CSI process,

The wideband second PMI value for the CSI process is calculated conditioned on the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported wideband first PMI for the CSI process and the last reported periodic CRI for the CSI process.

The wideband CQI value is calculated conditioned on the selected precoding matrix for the CSI process and the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported periodic CRI for the CSI process.

otherwise, with the last reported PTI=0,

The wideband second PMI value is calculated conditioned on the last reported periodic RI and the wideband first PMI and the last reported periodic CRI.

The wideband CQI value is calculated conditioned on the selected precoding matrix and the last reported periodic RI process and the last reported periodic CRI.

otherwise,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 6 report for the CSI process is dropped, and a type 6 report for the 'RI-reference CSI process' with PTI=0 is reported in the most recent RI reporting instance for the CSI process,

The wideband second PMI value for the CSI process is calculated conditioned on the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported wideband first PMI for the CSI process.

The wideband CQI value is calculated conditioned on the selected precoding matrix for the CSI process and the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process.

Otherwise, with the last reported PTI=0,

The wideband second PMI value is calculated conditioned on the last reported periodic RI and the wideband first PMI.

The wideband CQI value is calculated conditioned on the selected precoding matrix and the last reported periodic RI.

If the last reported first PMI was computed under an RI assumption that differs from the last reported periodic RI, or in the absence of a last reported first PMI, the conditioning of the second PMI value is not specified.

In the subframe where subband CQI/second PMI for the selected subband is reported, for transmission modes 9 and 10 with 8 CSI-RS ports configured and higher layer parameter eMIMO-Type not configured, or for transmission modes 9 and 10 with 8 CSI-RS ports or 4 CSI-RS ports with alternativeCodeBookEnabledFor4TX-r12=TRUE in the selected CSI-RS resource and UE is configured with CRI reporting, or for transmission modes 9 and 10 with 8 CSI-RS ports configured and UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and except with higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, or for transmission modes 9 and 10 with higher layer parameter eMIMO-Type configured, and eMIMO-Type set to 'CLASS A',or for transmission modes 8, 9 and 10 with alternativeCodeBookEnabledFor4TX-r12=TRUE configured without CRI reporting:

The UE shall select the preferred subband within the set of Nj subbands in each of the J bandwidth parts where J is given in Table 7.2.2-2.

The UE shall report a type 1a report per bandwidth part on each respective successive reporting opportunity consisting of:

CQI value for codeword 0 reflecting transmission only over the selected subband of a bandwidth part determined in the previous step along with the corresponding preferred subband L-bit label.

When RI>1, an additional 3-bit subband spatial differential CQI value for codeword 1 offset level

Codeword 1 offset level = subband CQI index for codeword 0 – subband CQI index for codeword 1.

Assuming the use of the precoding matrix corresponding to the selected second PMI and the most recently reported first PMI and transmission on the selected subband within the applicable bandwidth part.

The mapping from the 3-bit subband spatial differential CQI value to the offset level is shown in Table 7.2-2.

A second PMI of the preferred precoding matrix selected from the codebook subset assuming transmission only over the selected subband within the applicable bandwidth part determined in the previous step.

If the UE is configured with CRI reporting,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 6 report for the CSI process is dropped, and a type 6 report for the 'RI-reference CSI process' with PTI=1 is reported in the most recent RI reporting instance for the CSI process,

The subband second PMI values for the CSI process are calculated conditioned on the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported wideband first PMI for the CSI process and the last reported periodic CRI for the CSI process.

The subband selection and CQI values are calculated conditioned on the selected precoding matrix for the CSI process and the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported periodic CRI for the CSI process.

Otherwise, with the last reported PTI=1

The subband second PMI values are calculated conditioned on the last reported periodic RI and the wideband first PMI and the last reported periodic CRI.

The subband selection and CQI values are calculated conditioned on the selected precoding matrix and the last reported periodic RI and the last reported periodic CRI.

otherwise,

If a UE is configured in transmission mode 10 with a 'RI-reference CSI process' for a CSI process, and the most recent type 6 report for the CSI process is dropped, and a type 6 report for the 'RI-reference CSI process' with PTI=1 is reported in the most recent RI reporting instance for the CSI process,

The subband second PMI values for the CSI process are calculated conditioned on the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process and the last reported wideband first PMI for the CSI process.

The subband selection and CQI values are calculated conditioned on the selected precoding matrix for the CSI process and the reported periodic RI for the configured 'RI-reference CSI process' in the most recent RI reporting instance for the CSI process.

Otherwise, with the last reported PTI=1

The subband second PMI values are calculated conditioned on the last reported periodic RI and the wideband first PMI.

The subband selection and CQI values are calculated conditioned on the selected precoding matrix and the last reported periodic RI.

If the last reported first PMI was computed under an RI assumption that differs from the last reported periodic RI, or in the absence of a last reported first PMI, the conditioning of the second PMI value is not specified.

Table 7.2.2-2: Subband Size (k) and Bandwidth Parts (J) vs. Downlink System Bandwidth

| System Bandwidth | Subband Size k (RBs) | Bandwidth Parts (J) |
| --- | --- | --- |
|  |  |  |
| 6 – 7 | NA | NA |
| 8 – 10 | 4 | 1 |
| 11 – 26 | 4 | 2 |
| 27 – 63 | 6 | 3 |
| 64 – 110 | 8 | 4 |

For a BL/CE UE, the periodic CSI reporting modes are described as following:

Wideband feedback

Mode 1-0 description:

In the subframe where CQI is reported:

A UE shall report a type 4 report consisting of one wideband CQI value which is calculated assuming transmission on all narrowband(s) in the CSI reference resource. The wideband CQI is calculated conditioned on transmission rank 1.

Mode 1-1 description:

In the subframe where a first PMI is reported for transmission modes 9 configured with submode 1 and 8 CSI-RS ports, the UE shall report a type 2a report consisting of a first PMI corresponding to a set of precoding matrices selected from the codebook subset assuming transmission on all narrowband(s) in the CSI reference resource. The wideband first PMI value is calculated conditioned on transmission rank 1.

In the subframe where wideband CQI/second PMI is reported for transmission modes 9 with 8 CSI-RS ports and submode 1:

A single precoding matrix is selected from the codebook subset assuming transmission on all narrowband(s) in the CSI reference resource.

A UE shall report a type 2b report consisting of

A single wideband CQI value which is calculated assuming the use of the single precoding matrix in all narrowband(s) in the CSI reference resource and transmission on all narrowband(s) in the CSI reference resource.

The wideband second PMI corresponding to the selected single precoding matrix.

The wideband second PMI is calculated conditioned on transmission rank 1 and the last reported wideband first PMI. The wideband CQI is calculated conditioned on the selected precoding matrix and transmission rank 1.

In the subframe where wideband CQI/first PMI/second PMI is reported for transmission modes 9 with submode 2 and 8 CSI-RS ports configured:

A single precoding matrix is selected from the codebook subset assuming transmission on all narrowband(s) in the CSI reference resource.

A UE shall report a type 2c report consisting of

A single wideband CQI value which is calculated assuming the use of the single precoding matrix in all narrowband(s) in the CSI reference resource and transmission on all narrowband(s) in the CSI reference resource.

The wideband first PMI and the wideband second PMI corresponding to the selected single precoding matrix as defined in Clause 7.2.4.

The wideband first PMI, the wideband second PMI and the wideband CQI are calculated conditioned on transmission rank 1.

In the subframe where CQI/PMI is reported:

A single precoding matrix is selected from the codebook subset assuming transmission on all narrowband(s) in the CSI reference resource. The PMI is calculated conditioned on transmission rank 1.

A UE shall report a type 2 report consisting of

A single wideband CQI value which is calculated assuming the use of a single precoding matrix in all narrowband(s) in the CSI reference resource and transmission on all narrowband(s) in the CSI reference resource. The wideband CQI is calculated conditioned on transmission rank 1.

The selected single PMI (wideband PMI).

If parameter ttiBundling provided by higher layers is set to TRUE and if an UL-SCH in subframe bundling operation collides with a periodic CSI reporting instance, then the UE shall drop the periodic CSI report of a given PUCCH reporting type in that subframe and shall not multiplex the periodic CSI report payload in the PUSCH transmission in that subframe. A UE is not expected to be configured with simultaneous PUCCH and PUSCH transmission when UL-SCH subframe bundling is configured.

If the UE is configured with higher layer paramter pusch-EnhancementsConfig, and if a PUSCH transmission spans more than one subframe as indicated by the repetition number field in DCI 0C, the UE shall drop the periodic CSI report of a given PUCCH reporting type in that subframe and shall not multiplex the periodic CSI report payload in the PUSCH transmission in that subframe. A UE is not expected to be configured with simultaneous PUCCH and PUSCH transmission when pusch-EnhancementsConfig is configured.

Table 7.2.2-3: PUCCH Reporting Type Payload size per PUCCH Reporting Mode and Mode State

| PUCCH Reporting Type | Reported | Mode State | PUCCH Reporting Modes |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Mode 1-1 | Mode 2-1 | Mode 1-0 | Mode 2-0 |
|  |  |  | (bits/BP*) | (bits/BP*) | (bits/BP*) | (bits/BP*) |
| 1 | Sub-bandCQI | RI = 1 | NA | 4+L | NA | 4+L |
|  |  | RI > 1 | NA | 7+L | NA | 4+L17+L2 |
| 1a | Sub-band CQI / second PMI | 8 antenna ports or 8/12/16/20/24/28/32 antenna ports with codebookConfig={2,3,4}, RI = 1 | NA | 8+L | NA | NA |
|  |  | 8 antenna ports or 8/12/16/20/24/28/32 antenna ports with codebookConfig={2,3,4}, 1 < RI < 5 | NA | 9+L | NA | NA |
|  |  | 8 antenna ports or 8/12/16/20/24/28/32 antenna ports with codebookConfig={1,2,3,4} RI > 4 | NA | 7+L | NA | NA |
|  |  | 8/12/16/20/24/28/32 antenna ports with codebookConfig=1, RI = 1 | NA | 6+L | NA | NA |
|  |  | 8/12/16/20/24/28/32 antenna ports with codebookConfig=1, RI = 2 | NA | 9+L | NA | NA |
|  |  | 8/12/16/20/24/28/32 antenna ports with codebookConfig=1, 2<RI<5 | NA | 8+L | NA | NA |
|  |  | 4 antenna ports RI=1 | NA | 8+L | NA | NA |
|  |  | 4 antenna ports 1<RI4 | NA | 9+L | NA | NA |
| 2 | Wideband CQI/PMI | 2 antenna ports RI = 1 | 6 | 6 | NA | NA |
|  |  | 4 antenna ports RI = 1, Note5 | 8 | 8 | NA | NA |
|  |  | 2 antenna ports RI > 1 | 8 | 8 | NA | NA |
|  |  | 4 antenna ports RI > 1, Note5 | 11 | 11 | NA | NA |
|  |  | 4 antenna ports RI = 1, Note6 | 7 | 7 | NA | NA |
|  |  | 4 antenna ports RI = 2, Note6 | 10 | 10 | NA | NA |
|  |  | 4 antenna ports RI = 3, Note6 | 9 | 9 | NA | NA |
|  |  | 4 antenna ports RI = 4, Note6 | 8 | 8 | NA | NA |
|  |  | 8 antenna ports RI = 1 | 8 | 8 | NA | NA |
|  |  | 8 antenna ports 1<RI<4 | 11 | 11 | NA | NA |
|  |  | 8 antenna ports RI = 4 | 10 | 10 | NA | NA |
|  |  | 8 antenna ports RI > 4 | 7 | 7 | NA | NA |
| 2a | Wideband first PMI | 8 antenna ports RI < 3 | NA | 4 | NA | NA |
|  |  | 8 antenna ports 2 < RI < 8 | NA | 2 | NA | NA |
|  |  | 8 antenna ports RI = 8 | NA | 0 | NA | NA |
|  |  | 4 antenna ports 1RI2 | NA | 4 | NA | NA |
|  |  | 4 antenna ports 2RI4 | NA | NA | NA | NA |
|  |  | 8/12/16/20/24/28/32 antenna ports with codebookConfig=1, 1RI8 | Note3 | Note3 | NA | NA |
|  |  | 8/12/16/20/24/28/32 antenna ports with codebookConfig={2,3,4} | Note4 | Note4 | NA | NA |
|  |  | 4 antenna ports with advancedCodebookEnabled =True, 1RI2 | 3 | NA | NA | NA |
|  |  | 4 antenna ports with advancedCodebookEnabled =True, 3RI4 | 0 | NA | NA | NA |
|  |  | 8 antenna ports with advancedCodebookEnabled =True, 1RI2 | 6 | NA | NA | NA |
|  |  | 8 antenna ports with advancedCodebookEnabled =True, 3RI7 | 2 | NA | NA | NA |
|  |  | 8 antenna ports with advancedCodebookEnabled =True, RI=8 | 0 | NA | NA | NA |
|  |  | 8/12/16/20/24/28/32 antenna ports with advancedCodebookEnabled =True and eMIMO-Type is set to 'CLASS A', 1RI8 | Note7 | NA | NA | NA |
|  |  | 8/12/16/20/24/28/32 antenna ports, eMIMO-Type and eMIMO-Type2 configured by higher layers, eMIMO-Type is set to 'CLASS A', eMIMO-Type2 is set to 'CLASS B', and maximum 1 or 2 layers are supported by the UE | Note8 | Note8 | Note8 | Note8 |
| 2b | Wideband CQI / second PMI | 8 antenna ports or 8/12/16/20/24/28/32 antenna ports with codebookConfig = {2,3,4}, RI = 1 | 8 | 8 | NA | NA |
|  |  | 8 antenna ports or 8/12/16/20/24/28/32 antenna ports with codebookConfig = {2,3,4}, 1 < RI < 4 | 11 | 11 | NA | NA |
|  |  | 8 antenna ports or 8/12/16/20/24/28/32 antenna ports with codebookConfig = {2,3,4}, RI = 4 | 10 | 10 | NA | NA |
|  |  | 8 antenna ports or 8/12/16/20/24/28/32 antenna ports with codebookConfig = {1,2,3,4}, RI > 4 | 7 | 7 | NA | NA |
|  |  | 4 antenna ports RI=1 | 8 | 8 | NA | NA |
|  |  | 4 antenna port 1<RI4 | 11 | 11 | NA | NA |
|  |  | 8/12/16/20/24/28/32 antenna ports with codebookConfig=1, RI = 1 | 6 | 6 | NA | NA |
|  |  | 8/12/16/20/24/28/32 antenna ports with codebookConfig=1, RI = 2 | 9 | 9 | NA | NA |
|  |  | 8/12/16/20/24/28/32 antenna ports with codebookConfig=1, 2<RI<5 | 8 | 8 | NA | NA |
|  |  | 4/8 antenna ports with advancedCodebookEnabled =True or 8/12/16/20/24/28/32 antenna ports with advancedCodebookEnabled =True and eMIMO-Type is set to 'CLASS A', RI = 1 | 10 | NA | NA | NA |
|  |  | 4/8 antenna ports with advancedCodebookEnabled =True or 8/12/16/20/24/28/32 antenna ports with advancedCodebookEnabled =True and eMIMO-Type is set to 'CLASS A', RI = 2 | 11 | NA | NA | NA |
| 2c | Wideband CQI / first PMI / second PMI | 8 antenna ports RI = 1 | 8 | NA | NA | NA |
|  |  | 8 antenna ports 1 < RI  4 | 11 | NA | NA | NA |
|  |  | 8 antenna ports 4 < RI  7 | 9 | NA | NA | NA |
|  |  | 8 antenna ports RI = 8 | 7 | NA | NA | NA |
|  |  | 4 antenna ports RI=1 | 8 | NA | NA | NA |
|  |  | 4 antenna port 1<RI4 | 11 | NA | NA | NA |
| 3 | RI | 2/4 antenna ports, 2-layer spatial multiplexing | 1 | 1 | 1 | 1 |
|  |  | 8 antenna ports, 2-layer spatial multiplexing | 1 | NA | NA112 | NA112 |
|  |  | 4 antenna ports, 4-layer spatial multiplexing | 2 | 2 | 2 | 2 |
|  |  | 8 antenna ports, 4-layer spatial multiplexing | 2 | NA | NA122 | NA122 |
|  |  | 8-layer spatial multiplexing | 3 | NA | NA132 | NA132 |
|  |  | 12/16/20/24/28/32 antenna ports, 2-layer spatial multiplexing | 1 | NA | NA | NA |
|  |  | 12/16/20/24/28/32 antenna ports, 4-layer spatial multiplexing | 2 | NA | NA | NA |
|  |  | 12/16/20/24/28/32 antenna ports, 8-layer spatial multiplexing | 3 | NA | NA | NA |
| 4 | Wideband CQI | RI = 1 or RI>1, without PMI/RI reporting | NA | NA | 4 | 4 |
|  |  | RI = 1 without PMI reporting | NA | NA | 4 | 4 |
|  |  | RI>1 without PMI reporting | NA | NA | 7 | 7 |
| 5 | RI/ first PMI | 8 antenna ports, 2-layer spatial multiplexing | 4 | NA | NA | NA |
|  |  | 8 antenna ports, 4 and 8-layer spatial multiplexing | 5 |  |  |  |
|  |  | 4 antenna ports, 2-layer spatial multiplexing | 4 |  |  |  |
|  |  | 4 antenna ports, 4-layer spatial multiplexing | 5 |  |  |  |
|  |  | 8/12/16/20/24/28/32 antenna ports, eMIMO-Type and eMIMO-Type2 configured by higher layers, eMIMO-Type is set to 'CLASS A', eMIMO-Type2 is set to 'CLASS B', and maximum 4 or 8 layers are supported by the UE | Note9 | Note9 | Note9 | Note9 |
| 6 | RI/PTI | 8 antenna ports, 2-layer spatial multiplexing | NA | 2 | NA | NA |
|  |  | 8 antenna ports, 4-layer spatial multiplexing | NA | 3 | NA | NA |
|  |  | 8 antenna ports, 8-layer spatial multiplexing | NA | 4 | NA | NA |
|  |  | 4 antenna ports, 2-layer spatial multiplexing | NA | 2 | NA | NA |
|  |  | 4 antenna ports, 4-layer spatial multiplexing | NA | 3 | NA | NA |
|  |  | 12/16/20/24/28/32 antenna ports, 2-layer spatial multiplexing | NA | 2 | NA | NA |
|  |  | 12/16/20/24/28/32 antenna ports, 4-layer spatial multiplexing | NA | 3 | NA | NA |
|  |  | 12/16/20/24/28/32 antenna ports, 8-layer spatial multiplexing | NA | 4 | NA | NA |
| 7 | CRI/RI | 2-layer spatial multiplexing | k+1 | k+1 | k+1 | k+1 |
|  |  | 4-layer spatial multiplexing | k+2 | k+2 | k+2 | k+2 |
|  |  | 8-layer spatial multiplexing | k+3 | k+3 | k+3 | k+3 |
| 8 | CRI/RI/first PMI | 2-layer spatial multiplexing | k+4 | NA | NA | NA |
|  |  | 4 and 8-layer spatial multiplexing | k+5 | NA | NA | NA |
| 9 | CRI/RI/PTI | 2-layer spatial multiplexing | NA | k+2 | NA | NA |
|  |  | 4-layer spatial multiplexing | NA | k+3 | NA | NA |
|  |  | 8-layer spatial multiplexing | NA | k+4 | NA | NA |
| 10 | CRI | Without PMI/RI reporting | NA | NA | k | k |
| 11 | RI/RPI | 2-layer spatial multiplexing | 3 | NA | NA | NA |
|  |  | 4-layer spatial multiplexing | 4 | NA | NA | NA |
|  |  | 8-layer spatial multiplexing | 5 | NA | NA | NA |
| NOTE *: For wideband CQI reporting types, the stated payload size applies to the full bandwidth.NOTE 1: Without PMI/RI reportingNOTE 2: Without PMI reporting and without csi-RS-NZP-mode,  where is the number of configured CSI-RS resources or without PMI reporting and with higher layer parameter csi-RS-NZP-mode set to 'multiShot' and activatedResources>1,  where N is the number of activated CSI-RS resources.NOTE 3: Sum of Wideband first PMI i1,1 bit width and Wideband first PMI i1,2 bit width in Table 5.2.3.3.2-3B-1 of [4] with PTI=0NOTE 4: Sum of Wideband first PMI i1,1 bit width and Wideband first PMI i1,2 bit width in Table 5.2.3.3.2-3B-2 of [4] with PTI=0NOTE 5: Not configured with parameter eMIMO-Type by higher-layersNOTE 6: Configured with parameter eMIMO-Type by higher-layers Note 7: Sum of Wideband first PMI i1,1 bit width, Wideband first PMI i1,2 bit width, Wideband first PMI i1,3 bit width in Table 5.2.3.3.1-4C of [4]NOTE 8: Sum of Wideband first PMI i1,1 bit width and Wideband first PMI i1,2 bit width in Table 5.2.3.3.1-4D of [4] with Max 1 or 2 layers.NOTE 9: Sum of Wideband first PMI i1,1 bit width, Wideband first PMI i1,2 bit width and RI bit width in Table 5.2.3.3.1-4D of [4] with Max 4 or 8 layers. |  |  |  |  |  |  |

### 7.2.3 Channel Quality Indicator (CQI) definition

The CQI indices and their interpretations are given in Table 7.2.3-1, Table 7.2.3-5, Table 7.2.3-6 for reporting CQI based on QPSK, 16QAM and 64QAM. The CQI indices and their interpretations are given in Table 7.2.3-2 for reporting CQI based on QPSK, 16QAM, 64QAM and 256QAM. The CQI indices and their interpretations are given in Table 7.2.3-3 for reporting CQI based on QPSK and 16QAM. The CQI indices and their interpretations are given in Table 7.2.3-4 for reporting CQI based on QPSK, 16QAM, 64QAM, 256QAM, and 1024QAM.

For a non-BL/CE UE, based on an unrestricted observation interval in time unless specified otherwise in this Clause, and an unrestricted observation interval in frequency, the UE shall derive for each CQI value reported in uplink subframe/slot/subslot n the highest CQI index between 1 and 15 in Table 7.2.3-1, Table 7.2.3-2 or Table 7.2.3-4 which satisfies the following condition, or CQI index 0 if CQI index 1 does not satisfy the condition:

- A single PDSCH transport block with a combination of modulation scheme and transport block size corresponding to the CQI index, and occupying a group of downlink physical resource blocks termed the CSI reference resource, could be received with a transport block error probability not exceeding 0.1.

For a BL/CE UE, based on an unrestricted observation interval in time and frequency, the UE shall derive for each CQI value the highest CQI index in Table 7.2.3-3, Table 7.2.3-5 or Table 7.2.3-6 which satisfies the following condition, or CQI index 0 if CQI index 1 does not satisfy the condition:

- A single PDSCH transport block with a combination of modulation scheme and transport block size corresponding to the CQI index, and occupying a group of downlink physical resource blocks termed the CSI reference resource, could be received with a transport block error probability not exceeding 0.1.

If CSI subframe sets  and  are configured by higher layers, each CSI reference resource belongs to either  or  but not to both. When CSI subframe sets  and  are configured by higher layers a UE is not expected to receive a trigger for which the CSI reference resource is in subframe that does not belong to either subframe set. For a UE in transmission mode 10 and periodic CSI reporting, the CSI subframe set for the CSI reference resource is configured by higher layers for each CSI process.

If the UE is configured with parameter eMIMO-Type2 by higher layers for a CSI process, for computing the CQI value for eMIMO-Type2 of the CSI process, the parameter eMIMO-Type in the rest of this Clause refers to the parameter eMIMO-Type2 for the CSI process.

For a UE in transmission mode 9 when parameter pmi-RI-Report is configured by higher layers and parameter eMIMO-Type is not configured by higher layers, the UE shall derive the channel measurements for computing the CQI value reported in uplink subframe/slot/subslot n based on only the Channel-State Information (CSI) reference signals (CSI-RS) defined in [3] for which the UE is configured to assume non-zero power for the CSI-RS. For a non-BL/CE UE in transmission mode 9 when the parameter pmi-RI-Report is not configured by higher layers or in transmission modes 1-8 the UE shall derive the channel measurements for computing CQI based on CRS. For a BL/CE UE, the UE shall derive the channel measurements for computing CQI based on CSI-RS if configured with the higher layer parameter ce-CSI-RS-Feedback for transmission mode 9 and the number of CSI-RS ports=8, otherwise based on CRS.

For a UE in transmission mode 10, when parameter eMIMO-Type is not configured by higher layers, the UE shall derive the channel measurements for computing the CQI value reported in uplink subframe/slot/subslot n and corresponding to a CSI process, based on only the non-zero power CSI-RS (defined in [3]) within a configured CSI-RS resource associated with the CSI process.

For a UE in transmission mode 9 and the UE configured with parameter eMIMO-Type by higher layers, the term 'CSI process' in this clause refers to the CSI configured for the UE.

For a UE in transmission mode 9 or 10 and for a CSI process, if the UE is configured with parameter eMIMO-Type by higher layers, and eMIMO-Type is set to 'CLASS A', and one CSI-RS resource configured, or the UE is configured with parameter eMIMO-Type by higher layers, and eMIMO-Type is set to 'CLASS B', and parameter channelMeasRestriction is not configured by higher layers, the UE shall derive the channel measurements for computing the CQI value reported in uplink subframe n and corresponding to the CSI process, based on only the non-zero power CSI-RS (defined in [3]) within a configured CSI-RS resource associated with the CSI process. If the UE is configured with parameter eMIMO-Type by higher layers, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B' and the number of configured CSI-RS resources is K>1, and parameter channelMeasRestriction is not configured by higher layers, the UE shall derive the channel measurements for computing the CQI value using only the configured CSI-RS resource indicated by the CRI. If the UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, and parameter channelMeasRestriction is not configured by higher layers, the UE shall derive the channel measurements for computing the CQI value using only the activated CSI-RS resource indicated by CRI.

For a UE in transmission mode 9 or 10 and for a CSI process, if the UE is configured with parameter eMIMO-Type by higher layers, and eMIMO-Type is set to 'CLASS B', and parameter channelMeasRestriction is configured by higher layers, the UE shall derive the channel measurements for computing the CQI value reported in uplink subframe n and corresponding to the CSI process, based on only the most recent, no later than the CSI reference resource, non-zero power CSI-RS (defined in [3]) within a configured CSI-RS resource associated with the CSI process. If the UE is configured with parameter eMIMO-Type by higher layers, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B' and the number of configured CSI-RS resources is K>1, and parameter channelMeasRestriction is configured by higher layers, the UE shall derive the channel measurements for computing the CQI value using only the most recent, no later than the CSI reference resource, non-zero power CSI-RS within the configured CSI-RS resource indicated by the CRI. If the UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is more than one, and parameter channelMeasRestriction is configured by higher layers, the UE shall derive the channel measurements for computing the CQI value using only the most recent, no later than the CSI reference resource, non-zero power CSI-RS within the activated CSI-RS resource indicated by the CRI.

For a UE in transmission mode 10, when parameter eMIMO-Type is not configured by higher layers, the UE shall derive the interference measurements for computing the CQI value reported in uplink subframe/slot/subslot n and corresponding to a CSI process, based on only the configured CSI-IM resource associated with the CSI process.

For a UE in transmission mode 10 and for a CSI process, when parameters eMIMO-Type and interferenceMeasRestriction is configured by higher layers, the UE shall derive the interference measurements for computing the CQI value reported in uplink subframe n and corresponding to the CSI process, based on only the most recent, no later than the CSI reference resource, configured CSI-IM resource associated with the CSI process. If the UE is configured with parameter eMIMO-Type by higher layers, except with higher layer parameter csi-RS-NZP-mode configured, and eMIMO-Type is set to 'CLASS B' and the number of configured CSI-RS resources is K>1, and interferenceMeasRestriction is configured, the UE shall derive interference measurement for computing the CQI value based on only the most recent, no later than the CSI reference resource, the configured CSI-IM resource associated with the CSI-RS resource indicated by the CRI. If the UE is configured with higher layer parameter eMIMO-Type set to 'CLASS B' and higher layer parameter csi-RS-NZP-mode set to 'multiShot', and the number of activated CSI-RS resources is K>1, and interferenceMeasRestriction is configured, the UE shall derive interference measurement for computing the CQI value based on only the most recent, no later than the CSI reference resource, the configured CSI-IM resource associated with the activated CSI-RS resource indicated by the CRI. If interferenceMeasRestriction is not configured, the UE shall derive the interference measurement for computing the CQI value based on the CSI-IM associated with the CSI-RS resource indicated by the CRI.

If the UE in transmission mode 10 is configured by higher layers for CSI subframe sets  and  for the CSI process, the configured CSI-IM resource within the subframe subset belonging to the CSI reference resource is used to derive the interference measurement.

For a UE configured with the parameter EIMTA-MainConfigServCell-r12 for a serving cell, configured CSI-IM resource(s) within only downlink subframe(s) of a radio frame that are indicated by UL/DL configuration of the serving cell can be used to derive the interference measurement for the serving cell.

For a LAA Scell,

- for channel measurements, if the UE averages CRS/CSI-RS measurements from multiple subframes

- the UE should not average CSI-RS measurement in subframe n1 with CSI-RS measurement in a later subframe n2, if any OFDM symbol of subframe n1 or any subframe from subframe n1+1 to subframe n2, is not occupied.

- the UE should not average CRS measurement in subframe n1 with CRS measurement in a later subframe n2, if any OFDM symbol of the second slot of subframe n1 or any OFDM symbol of any subframe from subframe n1+1 to subframe n2-1, or any of the first 3 OFDM symbols in subframe n2, is not occupied.

- for interference measurements, the UE shall derive the interference measurements for computing the CQI value based on only measurements in subframes with occupied OFDM symbols.

A combination of modulation scheme and transport block size corresponds to a CQI index if:

- the combination could be signalled for transmission on the PDSCH in the CSI reference resource according to the relevant Transport Block Size table, and

- the modulation scheme is indicated by the CQI index, and

- the combination of transport block size and modulation scheme when applied to the reference resource results in the effective channel code rate which is the closest possible to the code rate indicated by the CQI index. If more than one combination of transport block size and modulation scheme results in an effective channel code rate equally close to the code rate indicated by the CQI index, only the combination with the smallest of such transport block sizes is relevant.

The CSI reference resource for a serving cell is defined as follows:

- For a non-BL/CE UE, in the frequency domain, the CSI reference resource is defined by the group of downlink physical resource blocks corresponding to the band to which the derived CQI value relates. For a BL/CE UE, in the frequency domain, the CSI reference resource includes all downlink physical resource blocks for any of the narrowband to which the derived CQI value relates.

- In the time domain and for a non-BL/CE UE,

- for a UE configured in transmission mode 1-9 or transmission mode 10 with a single configured CSI process for the serving cell, the CSI reference resource is defined by a single downlink subframe/slot/subslot or special subframe or a slot in a special subframe n-nCQI_ref,

- where for periodic CSI reporting nCQI_ref is the smallest value greater than or equal to , such that it corresponds to a valid downlink or valid special subframe,

- where for aperiodic CSI reporting, if the UE is not configured with the higher layer parameter csi-SubframePatternConfig-r12, and

- where for LAA serving cell,

- if aperiodic CSI reporting is triggered by DCI format 0A/0B/4A/4B with 'PUSCH trigger A' set to 1,

- nCQI_ref is the smallest value greater than or equal to , such that subframe n-nCQI_ref corresponds to a valid downlink subframe no later than the subframe in which DCI format 0A/0B/4A/4B with 'PUSCH trigger A' set to 1 is received.

- if aperiodic CSI reporting is triggered by DCI format 0A/0B/4A/4B with 'PUSCH trigger A' set to 0,

- nCQI_ref is the smallest value greater than or equal to , such that subframe n-nCQI_ref corresponds to a valid downlink subframe.

- otherwise,

- nCQI_ref is the smallest value greater than or equal to , such that subframe n-nCQI_ref corresponds to a valid downlink subframe.

- where for FDD serving cell or TDD serving cell,

- nCQI_ref is such that the reference resource is in the same valid downlink subframe/slot/subslot or valid special subframe or a valid slot in a special subframe as the corresponding CSI request in an uplink DCI format.

- nCQI_ref is equal to 4 and subframe n-nCQI_ref corresponds to a valid downlink or valid special subframe, where subframe n-nCQI_ref is received after the subframe with the corresponding CSI request in a Random Access Response Grant.

- where for aperiodic CSI reporting, and the UE configured with the higher layer parameter csi-SubframePatternConfig-r12,

- for the UE configured in transmission mode 1-9,

- nCQI_ref is the smallest value greater than or equal to

for aperiodic CSI reporting on subframe-PUSCH

## 4 for aperiodic CSI reporting on slot-PUSCH if the higher layer parameter dl-TTI-Length is set to slot

for aperiodic CSI reporting on subslot-PUSCH

Subslot nCQI_ref is not later than

subslot 0 of subframe n-2 for aperiodic CSI reporting on slot 0 of subframe n

subslot 3 of subframe n-2 for aperiodic CSI reporting on slot 1 of subframe n

if the higher layer parameter dl-TTI-Length is set to 'subslot', and the higher layer parameter ul-TTI-Length is set to 'slot'

and subframe/slot/subslot n-nCQI_ref corresponds to a valid downlink subframe/slot/subslot or valid special subframe or a valid slot in a special subframe, where subframe/slot/subslot n-nCQI_ref is received on or after the subframe/slot/subslot with the corresponding CSI request in an uplink DCI format;

- nCQI_ref is the smallest value greater than or equal to 4, and subframe n-nCQI_ref corresponds to a valid downlink or valid special subframe, where subframe n-nCQI_ref is received after the subframe with the corresponding CSI request in a Random Access Response Grant;

- if there is no valid value for nCQI_ref based on the above conditions, then nCQI_ref is the smallest value such that the reference resource is in a valid downlink subframe/slot/subslot or valid special subframe or a valid slot in a special subframe n-nCQI_ref prior to the subframe/slot/subslot with the corresponding CSI request, where subframe/slot/subslot n-nCQI_ref is the lowest indexed valid downlink subframe/slot/subslot or valid special subframe or a valid slot in a special subframe within a radio frame;

- for the UE configured in transmission mode 10,

- nCQI_ref is the smallest value greater than or equal to

for aperiodic CSI reporting on subframe-PUSCH,

## 4 for aperiodic CSI reporting on slot-PUSCH if the higher layer parameter dl-TTI-Length is set to slot

for aperiodic CSI reporting on subslot-PUSCH

Subslot nCQI_ref is not later than

subslot 0 of subframe n-2 for aperiodic CSI reporting on slot 0 of subframe n

subslot 3 of subframe n-2 for aperiodic CSI reporting on slot 1 of subframe n

if the higher layer parameter dl-TTI-Length is set to 'subslot', and the higher layer parameter ul-TTI-Length is set to 'slot'such that it corresponds to a valid downlink subframe/slot/subslot or valid special subframe or a valid slot in a special subframe, and the corresponding CSI request is in an uplink DCI format;

- nCQI_ref is the smallest value greater than or equal to 4, and subframe n-nCQI_ref corresponds to a valid downlink or valid special subframe, where subframe n-nCQI_ref is received after the subframe with the corresponding CSI request in a Random Access Response Grant;

- for a UE configured in transmission mode 10 with multiple configured CSI processes for the serving cell, the CSI reference resource for a given CSI process is defined by a single downlink subframe/slot/subslot or special subframe or a valid slot in a special subframe n-nCQI_ref,

- where for FDD serving cellsubslot nCQI_ref is not later than

- subslot 5 of subframe n-3 for aperiodic CSI reporting on slot 0 of subframe n

- subslot 2 of subframe n-2 for aperiodic CSI reporting on slot 1 of subframe n

if the higher layer parameter dl-TTI-Length is set to subslot, and the higher layer parameter ul-TTI-Length is set to slot

- nCQI_ref is the smallest value greater than or equal to

- 5 for aperiodic CSI reporting on slot-PUSCH if the higher layer parameter dl-TTI-Length is set to 'slot'

-  for aperiodic CSI reporting on subslot-PUSCH,

- +1, otherwise

such that it corresponds to a valid downlink subframe/slot/subslot or valid special subframe or a valid slot in a special subframe, and for aperiodic CSI reporting the corresponding CSI request is in an uplink DCI format;

- where for FDD serving cell and aperiodic CSI reporting nCQI_ref is equal to 5 and subframe n-nCQI_ref corresponds to a valid downlink or valid special subframe, where subframe n-nCQI_ref is received after the subframe with the corresponding CSI request in a Random Access Response Grant.

- where for TDD serving cell, and 2 or 3 configured CSI processes, and periodic or aperiodic CSI reporting, nCQI_ref is the smallest value greater than or equal to 4 for aperiodic CSI reporting on slot-based PUSCH, and  otherwise, such that it corresponds to a valid downlink or valid special subframe or a valid slot in a special subframe, and for aperiodic CSI reporting the corresponding CSI request is in an uplink DCI format;

- where for TDD serving cell, and 2 or 3 configured CSI processes, and aperiodic CSI reporting, nCQI_ref is equal to 4 and subframe n-nCQI_ref corresponds to a valid downlink or valid special subframe, where subframe n-nCQI_ref is received after the subframe with the corresponding CSI request in a Random Access Response Grant;

- where for TDD serving cell, and 4 configured CSI processes, and periodic or aperiodic CSI reporting, nCQI_ref is the smallest value greater than or equal to 5 for aperiodic CSI reporting on slot-based PUSCH, and  otherwise, such that it corresponds to a valid downlink or valid special subframe or a valid slot in a special subframe, and for aperiodic CSI reporting the corresponding CSI request is in an uplink DCI format;

- where for TDD serving cell, and 4 configured CSI processes, and aperiodic CSI reporting, nCQI_ref is equal to 5 and subframe n-nCQI_ref corresponds to a valid downlink or valid special subframe, where subframe n-nCQI_ref is received after the subframe with the corresponding CSI request in a Random Access Response Grant.

- where for LAA serving cell and periodic CSI reporting, nCQI_ref is the smallest value greater than or equal to , such that it corresponds to a valid downlink subframe.

- where for LAA serving cell and aperiodic CSI reporting, and

- if aperiodic CSI reporting is triggered by DCI format 0A/0B/4A/4B with 'PUSCH trigger A' set to 1,

- nCQI_ref is the smallest value greater than or equal to +1, such that subframe n-nCQI_ref corresponds to a valid downlink subframe no later than the subframe in which DCI format 0A/0B/4A/4B with 'PUSCH trigger A' set to 1 is received.

- if aperiodic CSI reporting is triggered by DCI format 0A/0B/4A/4B with 'PUSCH trigger A' set to 0,

- nCQI_ref is the smallest value greater than or equal to +1, such that subframe n-nCQI_ref corresponds to a valid downlink subframe.

- otherwise,

- nCQI_ref is the smallest value greater than or equal to 5, such that subframe n-nCQI_ref corresponds to a valid downlink subframe.

- In the time domain and for a BL/CE UE, the CSI reference resource is defined by a set of BL/CE downlink or special subframes where the last subframe is subframe n-nCQI_ref -Koffset,

- where $ K_{offset}$ is given by,

- if the UE is configured with the higher layer parameter k-Offset,

- $ K_{offset}=K_{cell\_offset}-K_{UE\_offset}$ where

$ K_{cell\_offset}$ is the parameter k-Offset provided by higher layers, and

$ K_{UE\_offset}$ is the parameter Differential Koffset provided by higher layers, otherwise $ K_{UE\_offset}=0 $

- otherwise,

- $ K_{offset}=0 $;

If the UE is configured with higher layer parameter k-Offset, for a PUSCH (re)transmission associated with the TC-RNTI, $ K_{offset}=$ k-Offset.

- where for periodic CSI reporting nCQI_ref is ≥ 4;

- where for aperiodic CSI reporting nCQI_ref is ≥ 4;

where each subframe in the CSI reference resource is a valid downlink or valid special subframe;

- where for wideband CSI reports:

- The set of BL/CE downlink or special subframes is the set of the last  subframes before n-nCQI_ref -Koffset used for MPDCCH monitoring by the BL/CE UE in each of the narrowbands where the BL/CE UE monitors MPDCCH, where  is the number of narrowbands where the BL/CE UE monitors MPDCCH.

- where for subband CSI reports:

- The set of BL/CE downlink or special subframes is the set of the last subframes used for MPDCCH monitoring by the BL/CE UE in the corresponding narrowband before n-nCQI_ref -Koffset;

- where is given by the "repetition" column when UE is configured to report the CQI according to Table 7.2.3-6, otherwise by the higher layer parameter csi-NumRepetitionCE.

A subframe/slot/subslot in a serving cell shall be considered to be a valid downlink subframe/slot/subslot or a valid special subframe or a valid slot in a special subframe if:

- it is configured as a downlink subframe/slot/subslot or a special subframe or a slot in a special subframe for that UE, and

- in case multiple cells with different uplink-downlink configurations are aggregated and the UE is not capable of simultaneous reception and transmission in the aggregated cells, the subframe/slot/subslot in the primary cell is a downlink subframe or a special subframe with the length of DwPTS more than  for subframe-based transmissions, or the slot is a first slot of DwPTS for special subframe configurations 1,2,3,4,6,7,8,9,10, or the second slot of DwPTS for special subframe configurations 3,4,8 for slot-based transmissions, and

- except for a non-BL/CE UE in transmission mode 9 or 10, the subframe/slot/subslot is not in an MBSFN subframe, and

- in case of TDD

- and subframe-based transmissions, the subframe does not contain a DwPTS field in case the length of DwPTS is  and less,

- and slot-based transmission,

- the slot is not a slot of DwPTS for special subframe configurations 0, 5,

- the slot is not the second slot of DwPTS for special subframe configurations 1, 2, 6, 7.

- it is not a special subframe with special subframe configuration 10 configured by ssp10-CRS-LessDwPTS, and

- it does not fall within a configured measurement gap for that UE, and

- for periodic CSI reporting, it is an element of the CSI subframe set linked to the periodic CSI report when that UE is configured with CSI subframe sets, and

- for a UE configured in transmission mode 10 with multiple configured CSI processes, and aperiodic CSI reporting for a CSI process, it is an element of the CSI subframe set linked to the downlink or special subframe containing the subframe/slot/subslot with the corresponding CSI request in an uplink DCI format, when that UE is configured with CSI subframe sets for the CSI process and UE is not configured with the higher layer parameter csi-SubframePatternConfig-r12, and

- for a UE configured in transmission mode 1-9, and aperiodic CSI reporting, it is an element of the CSI subframe set associated with the corresponding CSI request in an uplink DCI format, when that UE is configured with CSI subframe sets by the higher layer parameter csi-SubframePatternConfig-r12, and

- for a UE configured in transmission mode 10, and aperiodic CSI reporting for a CSI process, it is an element of the CSI subframe set associated with the corresponding CSI request in an uplink DCI format, when that UE is configured with CSI subframe sets by the higher layer parameter csi-SubframePatternConfig-r12 for the CSI process.

- except if the serving cell is a LAA Scell, and at least one OFDM symbol in the subframe is not occupied.

- except if the serving cell is a LAA Scell, and as described in sub clause 6.10.1.1 in [3].

- except if the serving cell is a LAA Scell, and for a UE configured in transmission mode 9 or 10, the configured CSI-RS resource associated with the CSI process is not in the subframe.

For a non-BL/CE UE, if there is no valid downlink subframe/slot/subslot or no valid special subframe or no valid slot in a special subframe for the CSI reference resource in a serving cell, CSI reporting is omitted for the serving cell in uplink subframe/slot/subslot n.

- In the layer domain, the CSI reference resource is defined by any RI and PMI on which the CQI is conditioned.

In the CSI reference resource, the UE shall assume the following for the purpose of deriving the CQI index, and if also configured, PMI and RI except when the CSI request field from an uplink DCI format 7-0A/7-0B is set to trigger a report:

- The first 3 OFDM symbols are occupied by control signalling

- No resource elements used by primary or secondary synchronization signals or PBCH or EPDCCH

- CP length of the non-MBSFN subframes

- Redundancy Version 0

- If CSI-RS is used for channel measurements, the ratio of PDSCH EPRE to CSI-RS EPRE is as given in Clause 7.2.5

- For transmission mode 9 CSI reporting of a non-BL/CE UE:

- CRS REs are as in non-MBSFN subframes;

- If the UE is configured for PMI/RI reporting or without PMI reporting, the UE-specific reference signal overhead is consistent with the most recent reported rank if more than one CSI-RS port is configured, and is consistent with rank 1 transmission if only one CSI-RS port is configured; and PDSCH signals on antenna ports  for layers would result in signals equivalent to corresponding symbols transmitted on antenna ports , as given by,

if the UE is configured with higher layer parameter semiOpenLoop,

for

for

where  is a vector of symbols from the layer mapping in clause 6.3.3.2 of [3], is the number of CSI-RS ports configured, and if UE reports a PMI,  where  associated with PMI codebook Table 7.2.4-0A and Table 7.2.4-0B for 4 antenna ports when alternativeCodeBookEnabledFor4TX-r12=TRUE is configured,  associated with PMI codebook Table 7.2.4-1 and Table 7.2.4-2 for 8 antenna ports when higher layer parameter eMIMO-Type is not configured,  associated with PMI codebook Table 7.2.4-10 and Table 7.2.4-11 for 8/12/16/20/24/28/32 antenna ports when higher layer parameter eMIMO-Type is configured, and where  is the column vector associated with the reported first PMI i1 and the second PMI i2 configured according to codebook subset restriction, and otherwise  is the selected precoding matrix corresponding to the reported CQI applicable to . The corresponding PDSCH signals transmitted on antenna ports  would have a ratio of EPRE to CSI-RS EPRE equal to the ratio given in clause 7.2.5,

otherwise,

,

where  is a vector of symbols from the layer mapping in Clause 6.3.3.2 of [3],  is the number of CSI-RS ports configured, and if only one CSI-RS port is configured, is 1, otherwise for UE configured for PMI/RI reporting is the precoding matrix corresponding to the reported PMI applicable to  and for UE configured without PMI reporting is the selected precoding matrix corresponding to the reported CQI applicable to . The corresponding PDSCH signals transmitted on antenna ports  would have a ratio of EPRE to CSI-RS EPRE equal to the ratio given in Clause 7.2.5.

- For transmission mode 10 CSI reporting, if a CSI process is configured without PMI/RI reporting:

- If the number of antenna ports of the associated CSI-RS resource is one, a PDSCH transmission is on single-antenna port, port 7. The channel on antenna port {7} is inferred from the channel on antenna port {15} of the associated CSI-RS resource.

- CRS REs are as in non-MBSFN subframes. The CRS overhead is assumed to be the same as the CRS overhead corresponding to the number of CRS antenna ports of the serving cell;

- The UE-specific reference signal overhead is 12 REs per PRB pair.

- Otherwise,

- If the number of antenna ports of the associated CSI-RS resource is 2, the PDSCH transmission scheme assumes the transmit diversity scheme defined in Clause 7.1.2 on antenna ports {0,1} except that the channels on antenna ports {0,1} are inferred from the channels on antenna port {15, 16} of the associated CSI resource respectively.

- If the number of antenna ports of the associated CSI-RS resource is 4, the PDSCH transmission scheme assumes the transmit diversity scheme defined in Clause 7.1.2 on antenna ports {0,1,2,3} except that the channels on antenna ports {0,1,2,3} are inferred from the channels on antenna ports {15, 16, 17, 18} of the associated CSI-RS resource respectively.

- The UE is not expected to be configured with more than 4 antenna ports for the CSI-RS resource associated with the CSI process configured without PMI/RI reporting.

- The overhead of CRS REs is assuming the same number of antenna ports as that of the associated CSI-RS resource.

- UE-specific reference signal overhead is zero.

- For transmission mode 10 CSI reporting, if a CSI process is configured with PMI/RI reporting or without PMI reporting:

- CRS REs are as in non-MBSFN subframes. The CRS overhead is assumed to be the same as the CRS overhead corresponding to the number of CRS antenna ports of the serving cell;

- The UE-specific reference signal overhead is consistent with the most recent reported rank for the CSI process if more than one CSI-RS port is configured, and is consistent with rank 1 transmission if only one CSI-RS port is configured; and PDSCH signals on antenna ports for layers would result in signals equivalent to corresponding symbols transmitted on antenna ports , as given by,

if the UE is configured with higher layer parameter semiOpenLoop and not configured with higher layer parameter FeCoMPCSIEnabled,

for

for

where  is a vector of symbols from the layer mapping in clause 6.3.3.2 of [3], is the number of CSI-RS ports configured, and if UE reports a PMI,  where  associated with PMI codebook Table 7.2.4-0A and Table 7.2.4-0B for 4 antenna ports when alternativeCodeBookEnabledFor4TX-r12=TRUE is configured,  associated with PMI codebook Table 7.2.4-1 and Table 7.2.4-2 for 8 antenna ports when higher layer parameter eMIMO-Type is not configured,  associated with PMI codebook Table 7.2.4-10 and Table 7.2.4-11 for 8/12/16/20/24/28/32 antenna ports when higher layer parameter eMIMO-Type is configured, and where  is the column vector associated with the reported first PMI i1 and the second PMI i2 configured according to codebook subset restriction, and otherwise  is the selected precoding matrix corresponding to the reported CQI applicable to . The corresponding PDSCH signals transmitted on antenna ports  would have a ratio of EPRE to CSI-RS EPRE equal to the ratio given in clause 7.2.5,

otherwise if the UE is not configured with higher layer parameter FeCoMPCSIEnabled or the UE is configured with higher layer parameter FeCoMPCSIEnabled and UE reports CRI with value of 0 or 1,

,

where  is a vector of symbols from the layer mapping in Clause 6.3.3.2 of [3],  is the number of antenna ports of the associated CSI-RS resource, and if P=1,is 1, otherwise for UE configured for PMI/RI reporting is the precoding matrix corresponding to the reported PMI applicable to  and for UE configured without PMI reporting is the selected precoding matrix corresponding to the reported CQI applicable to . The corresponding PDSCH signals transmitted on antenna ports  would have a ratio of EPRE to CSI-RS EPRE equal to the ratio given in Clause 7.2.5,

otherwise if the UE is configured with higher layer parameter FeCoMPCSIEnabled and UE reports CRI=2 then the PDSCH signals on antenna ports corresponding to layers of codeword k would result in signals equivalent to corresponding symbols transmitted on antenna ports  corresponding to the (k+1)th CSI-RS resource, where  are the number of antenna ports for the (k+1)th CSI-RS resource, as given by

$\left [ \begin {matrix}y_{k}^{(15)}(i) \\ ⋮ \\ y_{k}^{(14+P_{k})}(i)\end {matrix}\right ] =W_{k}\left ( i\right ) \left [ \begin {matrix}x_{k}^{\left ( 0\right ) }\left ( i\right )  \\ ⋮ \\ x_{k}^{\left ( \upsilon  _{k}-1\right ) }\left ( i\right ) \end {matrix}\right ] ,k=0,1 $

where  is a vector of symbols from the layer mapping in Clause 6.3.3.2 of [3] for codeword k=0, 1 and where the CSI corresponding to a codeword is calculated based on the assumption that inter-codeword interference is derived from channel measurement obtained from the NZP CSI-RS resource and the precoding matrix corresponding to the other codeword. The corresponding PDSCH signals transmitted on antenna ports  would have a ratio of EPRE to CSI-RS EPRE equal to the ratio given in Clause 7.2.5 for the (k+1)th CSI-RS resource.  If =1, then  is 1 otherwise for UE configured for PMI/RI reporting  is the precoding matrix corresponding to the reported PMI applicable to  and for UE configured without PMI reporting is the selected precoding matrix corresponding to the reported CQI applicable to .

- Assume no REs allocated for CSI-RS and zero-power CSI-RS

- Assume no REs allocated for PRS

- The PDSCH transmission scheme given by Table 7.2.3-0 depending on the transmission mode currently configured for the UE (which may be the default mode).

- If CRS is used for channel measurements, the ratio of PDSCH EPRE to cell-specific RS EPRE is as given in Clause 5.2 with the exception of which shall be assumed to be

- [dB] for any modulation scheme, if the UE is configured with transmission mode 2 with 4 cell-specific antenna ports, or transmission mode 3 with 4 cell-specific antenna ports and the associated RI is equal to one;

- [dB] for any modulation scheme and any number of layers, otherwise.

The shift is given by the parameter nomPDSCH-RS-EPRE-Offset which is configured by higher-layer signalling.

When the CSI request field from an uplink DCI format 7-0A/7-0B is set to trigger a report, the UE shall assume the number of available REs assumed for the reference resource for the purpose of deriving the CQI index, and if also configured, PMI and RI is:

- half of the number of available REs assumed for the reference resource when the CSI request field from an uplink DCI format other than 7-0A/7-0B is set to trigger a report if the UE is configured for slot-based uplink transmissions,

- one sixth of the number of available REs assumed for the reference resource when the CSI request field from an uplink DCI format other than 7-0A/7-0B is set to trigger a report if the UE is configured for subslot-based uplink transmissions

Table 7.2.3-0: PDSCH transmission scheme assumed for CSI reference resource

| Transmissionmode | Transmission scheme of PDSCH |
| --- | --- |
| 1 | Single-antenna port, port 0 |
| 2 | Transmit diversity |
| 3 | Transmit diversity if the associated rank indicator is 1, otherwise large delay CDD |
| 4 | Closed-loop spatial multiplexing |
| 5 | Multi-user MIMO |
| 6 | Closed-loop spatial multiplexing with a single transmission layer |
| 7 | If the number of PBCH antenna ports is one, Single-antenna port, port 0; otherwise Transmit diversity |
| 8 | If the UE is configured without PMI/RI reporting: if the number of PBCH antenna ports is one, single-antenna port, port 0; otherwise transmit diversity.If the UE is configured with PMI/RI reporting: closed-loop spatial multiplexing. |
| 9 | For activated serving cells, and a non-BL/CE UE, if the UE is configured without PMI/RI reporting: if the number of PBCH antenna ports is one, single-antenna port, port 0; otherwise transmit diversity. For activated serving cells, and a non-BL/CE UE, if the UE is configured with PMI/RI reporting or without PMI reporting: if the number of CSI-RS ports is one, single-antenna port, port 7; otherwise up to 8 layer transmission, ports 7-14 (see Clause 7.1.5B). For activated serving cells, and a BL/CE UE, if the UE is not configured with periodic CSI reporting mode 1-1: if the number of PBCH antenna ports is one, single-antenna port, port 0; otherwise transmit diversity.For activated serving cells, and a BL/CE UE, if the UE is configured with periodic CSI reporting mode 1-1: if the number of PBCH antenna ports is one, single-antenna port, port 0; otherwise closed-loop spatial multiplexing with a single transmission layer.For dormant serving cells: if the number of PBCH antenna ports is one, single-antenna port, port 0; otherwise transmit diversity. |
| 10 | For activated serving cells, if a CSI process of the UE is configured without PMI/RI reporting: if the number of CSI-RS ports is one, single-antenna port, port7; otherwise transmit diversity.For activated serving cells, and if a CSI process of the UE is configured with PMI/RI reporting or without PMI reporting: if the number of CSI-RS ports is one, single-antenna port, port 7; otherwise up to 8 layer transmission, ports 7-14 (see Clause 7.1.5B). For dormant serving cells: if the number of PBCH antenna ports is one, single-antenna port, port 0; otherwise transmit diversity. |

Table 7.2.3-1: 4-bit CQI Table

| CQI index | modulation | code rate x 1024 | efficiency |
| --- | --- | --- | --- |
| 0 | out of range |  |  |
| 1 | QPSK | 78 | 0.1523 |
| 2 | QPSK | 120 | 0.2344 |
| 3 | QPSK | 193 | 0.3770 |
| 4 | QPSK | 308 | 0.6016 |
| 5 | QPSK | 449 | 0.8770 |
| 6 | QPSK | 602 | 1.1758 |
| 7 | 16QAM | 378 | 1.4766 |
| 8 | 16QAM | 490 | 1.9141 |
| 9 | 16QAM | 616 | 2.4063 |
| 10 | 64QAM | 466 | 2.7305 |
| 11 | 64QAM | 567 | 3.3223 |
| 12 | 64QAM | 666 | 3.9023 |
| 13 | 64QAM | 772 | 4.5234 |
| 14 | 64QAM | 873 | 5.1152 |
| 15 | 64QAM | 948 | 5.5547 |

Table 7.2.3-2: 4-bit CQI Table 2

| CQI index | modulation | code rate x 1024 | efficiency |
| --- | --- | --- | --- |
| 0 | out of range |  |  |
| 1 | QPSK | 78 | 0.1523 |
| 2 | QPSK | 193 | 0.3770 |
| 3 | QPSK | 449 | 0.8770 |
| 4 | 16QAM | 378 | 1.4766 |
| 5 | 16QAM | 490 | 1.9141 |
| 6 | 16QAM | 616 | 2.4063 |
| 7 | 64QAM | 466 | 2.7305 |
| 8 | 64QAM | 567 | 3.3223 |
| 9 | 64QAM | 666 | 3.9023 |
| 10 | 64QAM | 772 | 4.5234 |
| 11 | 64QAM | 873 | 5.1152 |
| 12 | 256QAM | 711 | 5.5547 |
| 13 | 256QAM | 797 | 6.2266 |
| 14 | 256QAM | 885 | 6.9141 |
| 15 | 256QAM | 948 | 7.4063 |

Table 7.2.3-3: 4-bit CQI Table 3

| CQI index | modulation | code rate x 1024 x | efficiency x |
| --- | --- | --- | --- |
| 0 | out of range |  |  |
| 1 | QPSK | 40 | 0.0781 |
| 2 | QPSK | 78 | 0.1523 |
| 3 | QPSK | 120 | 0.2344 |
| 4 | QPSK | 193 | 0.3770 |
| 5 | QPSK | 308 | 0.6016 |
| 6 | QPSK | 449 | 0.8770 |
| 7 | QPSK | 602 | 1.1758 |
| 8 | 16QAM | 378 | 1.4766 |
| 9 | 16QAM | 490 | 1.9141 |
| 10 | 16QAM | 616 | 2.4063 |
| 11 | Reserved | Reserved | Reserved |
| 12 | Reserved | Reserved | Reserved |
| 13 | Reserved | Reserved | Reserved |
| 14 | Reserved | Reserved | Reserved |
| 15 | Reserved | Reserved | Reserved |

Table 7.2.3-4: 4-bit CQI Table 4

| CQI index | modulation | code rate x 1024 | Efficiency |
| --- | --- | --- | --- |
| 0 | out of range |  |  |
| 1 | QPSK | 78 | 0.1523 |
| 2 | QPSK | 193 | 0.3770 |
| 3 | QPSK | 449 | 0.8770 |
| 4 | 16QAM | 378 | 1.4766 |
| 5 | 16QAM | 616 | 2.4063 |
| 6 | 64QAM | 567 | 3.3223 |
| 7 | 64QAM | 666 | 3.9023 |
| 8 | 64QAM | 772 | 4.5234 |
| 9 | 64QAM | 873 | 5.1152 |
| 10 | 256QAM | 711 | 5.5547 |
| 11 | 256QAM | 797 | 6.2266 |
| 12 | 256QAM | 885 | 6.9141 |
| 13 | 256QAM | 948 | 7.4063 |
| 14 | 1024QAM | 853 | 8.3301 |
| 15 | 1024QAM | 948 | 9.2578 |

Table 7.2.3-5: 4-bit CQI Table 5

| CQI index | modulation | code rate x 1024 | efficiency |
| --- | --- | --- | --- |
| 0 | out of range |  |  |
| 1 | QPSK | 40 | 0.0781 |
| 2 | QPSK | 78 | 0.1523 |
| 3 | QPSK | 120 | 0.2344 |
| 4 | QPSK | 193 | 0.3770 |
| 5 | QPSK | 308 | 0.6016 |
| 6 | QPSK | 449 | 0.8770 |
| 7 | QPSK | 602 | 1.1758 |
| 8 | 16QAM | 378 | 1.4766 |
| 9 | 16QAM | 490 | 1.9141 |
| 10 | 16QAM | 616 | 2.4063 |
| 11 | 64QAM | 466 | 2.7305 |
| 12 | 64QAM | 567 | 3.3223 |
| 13 | 64QAM | 666 | 3.9023 |
| 14 | 64QAM | 772 | 4.5234 |
| 15 | 64QAM | 873 | 5.1152 |

Table 7.2.3-6: 4-bit CQI Table 6

| CQI index | modulation | code rate x 1024 | repetition |
| --- | --- | --- | --- |
| 0 | out of range |  |  |
| 1 | QPSK | 56 | 32 |
| 2 | QPSK | 207 | 16 |
| 3 | QPSK | 266 | 4 |
| 4 | QPSK | 195 | 2 |
| 5 | QPSK | 142 | 1 |
| 6 | QPSK | 266 | 1 |
| 7 | QPSK | 453 | 1 |
| 8 | QPSK | 637 | 1 |
| 9 | 16QAM | 423 | 1 |
| 10 | 16QAM | 557 | 1 |
| 11 | 16QAM | 696 | 1 |
| 12 | 16QAM | 845 | 1 |
| 13 | 64QAM | 651 | 1 |
| 14 | 64QAM | 780 | 1 |
| 15 | 64QAM | 888 | 1 |

### 7.2.4 Precoding Matrix Indicator (PMI) definition

For transmission modes 4, 5 and 6, precoding feedback is used for channel dependent codebook based precoding and relies on UEs reporting precoding matrix indicator (PMI). For transmission mode 8, the UE shall report PMI if configured with PMI/RI reporting. For transmission modes 9 and 10, the non-BL/CE UE shall report PMI if configured with PMI/RI reporting and the number of CSI-RS ports is larger than 1. For transmission modes 9, the BL/CE UE shall report PMI based on CSI-RS if configured with the higher layer parameter ce-CSI-RS-Feedback and the number of CSI-RS ports=8, otherwise based on CRS. A UE shall report PMI based on the feedback modes described in 7.2.1 and 7.2.2. For other transmission modes, PMI reporting is not supported.

For 2 antenna ports, except with,

UE configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE, or

UE configured with higher layer parameter eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE,

each PMI value corresponds to a codebook index given in Table 6.3.4.2.3-1 of [3] as follows:

- For 2 antenna ports  or {15,16} and an associated RI value of 1, a PMI value of  corresponds to the codebook index  given in Table 6.3.4.2.3-1 of [3] with .

- For 2 antenna ports  or {15,16} and an associated RI value of 2, a PMI value of  corresponds to the codebook index given in Table 6.3.4.2.3-1 of [3] with .

- For 2 antenna ports {15,16}, UE shall only use the precoding matrix corresponding to codebook index 0 in Table 6.3.4.2.3-1 of [3] with  and shall not report a PMI value if the UE is configured with higher layer parameter semiOpenLoop=TRUE.

For 4 antenna ports  or {15,16,17,18}, except with,

UE configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, or

UE configured with higher layer parameter eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE, or

UE configured with higher layer parameter advancedCodebookEnabled=TRUE, and  with  equal to the associated RI value,

each PMI value corresponds to a codebook index given in Table 6.3.4.2.3-2 of [3] or a pair of codebook indices given in Table 7.2.4-0A, 7.2.4-0B, 7.2.4-0C, or 7.2.4-0D as follows:

- A PMI value of  corresponds to the codebook index  given in Table 6.3.4.2.3-2 of [3] with  equal to the associated RI value except with alternativeCodeBookEnabledFor4TX-r12=TRUE configured.

- If higher layer parameter semiOpenLoop=TRUE configured except with alternativeCodeBookEnabledFor4TX-r12=TRUE configured, UE shall not report a PMI value and shall use the precoding matrix for REs of jth PRB-pair according to , where  is the precoder index given by  and denote precoder matrices corresponding to precoder indices 12,13,14 and 15, respectively, in Table 6.3.4.2.3-2 of [3] with .

- If alternativeCodeBookEnabledFor4TX-r12=TRUE is configured, each PMI value corresponds to a pair of codebook indices given in Table 7.2.4-0A, 7.2.4-0B, 7.2.4-0C, or 7.2.4-0D, where the quantities ,  and  in Table 7.2.4-0A and Table 7.2.4-0B are given by

- A first PMI value of  and a second PMI value of  correspond to the codebook indices  and  respectively given in Table 7.2.4-0j with  equal to the associated RI value and where j ={A,B,C,D} respectively when ,  and.

- The quantity  in Table 7.2.4-0C and Table 7.2.4-0D denotes the matrix defined by the columns given by the set  from the expression  where  is the  identity matrix and the vector  is given by Table 6.3.4.2.3-2 in [3] and .

- In some cases codebook subsampling is supported. The sub-sampled codebook for PUCCH mode 1-1 submode 2 is defined in Table 7.2.2-1G for first and second precoding matrix indicators  and . Joint encoding of rank and first precoding matrix indicator  for PUCCH mode 1-1 submode 1 is defined in Table 7.2.2-1H. The sub-sampled codebook for PUCCH mode 2-1 is defined in Table 7.2.2-1I for PUCCH Reporting Type 1a.

- UE shall only use the value of  according to the configured codebook subset restriction, where the UE is expected to be configured with a single value of  in {0,1,2,…,15} for 1 layer and in {0,1,2…,7} for 2 layers, and shall not report  if the UE is configured with higher layer parameter semiOpenLoop=TRUE.

Table 7.2.4-0A: Codebook for 1-layer CSI reporting using antenna ports 0 to 3 or 15 to 18

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 0 – 15 |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| 0 - 15 |  |  |  |  |  |  |  |  |
| where |  |  |  |  |  |  |  |  |

Table 7.2.4-0B: Codebook for 2-layer CSI reporting using antenna ports 0 to 3 or 15 to 18

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 |
| 0 – 15 |  |  |  |  |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
| 0 – 15 |  |  |  |  |
|  |  |  |  |  |
|  | 8 | 9 | 10 | 11 |
| 0 – 15 |  |  |  |  |
|  |  |  |  |  |
|  | 12 | 13 | 14 | 15 |
| 0 – 15 |  |  |  |  |
| where |  |  |  |  |

Table 7.2.4-0C: Codebook for 3-layer CSI reporting using antenna ports 15 to 18

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| 0 |  |  |  |  |  |  |  |  |

Table 7.2.4-0D: Codebook for 4-layer CSI reporting using antenna ports 15 to 18

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| 0 |  |  |  |  |  |  |  |  |

For a non-BL/CE UE, the UE is not expected to receive the configuration of alternativeCodeBookEnabledFor4TX-r12 except for transmission mode 8 configured with 4 CRS ports, and transmission modes 9 and 10 configured with 4 CSI-RS ports. For a UE configured in transmission mode 10, the parameter alternativeCodeBookEnabledFor4TX-r12 may be configured for each CSI process.

For a BL/CE UE, the UE is not expected to receive the configuration of alternativeCodeBookEnabledFor4TX-r12.

For 8 antenna ports, except with,

- UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', or

- UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, or

- UE is configured with higher layer parameter eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, or

- UE configured with higher layer parameter advancedCodebookEnabled=TRUE, and  with  equal to the associated RI value,

each PMI value corresponds to a pair of codebook indices given in Table 7.2.4-1, 7.2.4-2, 7.2.4-3, 7.2.4-4, 7.2.4-5, 7.2.4-6, 7.2.4-7, or 7.2.4-8, where the quantities  and  are given by

- as follows:For 8 antenna ports, a first PMI value of  and a second PMI value of  corresponds to the codebook indices  and  given in Table 7.2.4-j with  equal to the associated RI value and where j = ,  and .

- In some cases codebook subsampling is supported. The sub-sampled codebook for PUCCH mode 1-1 submode 2 is defined in Table 7.2.2-1D for first and second precoding matrix indicator  and . Joint encoding of rank and first precoding matrix indicator  for PUCCH mode 1-1 submode 1 is defined in Table 7.2.2-1E. The sub-sampled codebook for PUCCH mode 2-1 is defined in Table 7.2.2-1F for PUCCH Reporting Type 1a. For a BL/CE UE configured with CEModeA and PUCCH mode 1-1 for 8 CSI-RS ports, the entries in Table 7.2.2-1D and Table 7.2.2-1E corresponding to rank 1 are used.

- UE shall only use the value of  according to the configured codebook subset restriction, where the UE is expected to be configured with a single value of  in {0,1,2,…,15} for 1 layer and in {0,1,2…,7} for 2 layers, and shall not report  if the UE is configured with higher layer parameter semiOpenLoop=TRUE.

Table 7.2.4-1: Codebook for 1-layer CSI reporting using antenna ports 15 to 22

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 0 – 15 |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| 0 - 15 |  |  |  |  |  |  |  |  |
| where |  |  |  |  |  |  |  |  |

Table 7.2.4-2: Codebook for 2-layer CSI reporting using antenna ports 15 to 22

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 |
| 0 – 15 |  |  |  |  |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
| 0 – 15 |  |  |  |  |
|  |  |  |  |  |
|  | 8 | 9 | 10 | 11 |
| 0 – 15 |  |  |  |  |
|  |  |  |  |  |
|  | 12 | 13 | 14 | 15 |
| 0 – 15 |  |  |  |  |
| where |  |  |  |  |

Table 7.2.4-3: Codebook for 3-layer CSI reporting using antenna ports 15 to 22

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 |
| 0 - 3 |  |  |  |  |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
| 0 - 3 |  |  |  |  |
|  |  |  |  |  |
|  | 8 | 9 | 10 | 11 |
| 0 - 3 |  |  |  |  |
|  |  |  |  |  |
|  | 12 | 13 | 14 | 15 |
| 0 - 3 |  |  |  |  |
| where |  |  |  |  |

Table 7.2.4-4: Codebook for 4-layer CSI reporting using antenna ports 15 to 22

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 |
| 0 - 3 |  |  |  |  |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
| 0 - 3 |  |  |  |  |
| where |  |  |  |  |

Table 7.2.4-5: Codebook for 5-layer CSI reporting using antenna ports 15 to 22.

|  |  |
| --- | --- |
|  | 0 |
| 0 - 3 |  |

Table 7.2.4-6: Codebook for 6-layer CSI reporting using antenna ports 15 to 22.

|  |  |
| --- | --- |
|  | 0 |
| 0 - 3 |  |

Table 7.2.4-7: Codebook for 7-layer CSI reporting using antenna ports 15 to 22.

|  |  |
| --- | --- |
|  | 0 |
| 0 - 3 |  |

Table 7.2.4-8: Codebook for 8-layer CSI reporting using antenna ports 15 to 22.

|  |  |
| --- | --- |
|  | 0 |
| 0 |  |

For 8 antenna ports, 12 antenna ports, 16 antenna ports, 20 antenna ports, 24 antenna ports, 28 antenna ports, 32 antenna ports, and UE configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', except with UE configured with higher layer parameter advancedCodebookEnabled=TRUE, and  with  equal to the associated RI value, each PMI value corresponds to three codebook indices given in Table 7.2.4-10, 7.2.4-11, 7.2.4-12, 7.2.4-13, 7.2.4-14, 7.2.4-15, 7.2.4-16, or 7.2.4-17, where the quantities , and  are given by

- The values of , , , and  are configured with the higher-layer parameter codebookConfig-N1, codebookConfig-N2, codebook-Over-Sampling-RateConfig-O1, and codebook-Over-Sampling-RateConfig-O2, respectively. The supported configurations of and  for a given number of CSI-RS ports are given in Table 7.2.4-9. The number of CSI-RS ports, P, is .

- UE is not expected to be configured with value of codebookConfig set to 2 or 3, if the value of codebookConfigN2 is set to 1.

- UE shall only use and shall not report if the value of codebookConfig-N2 is set to 1.

- A first PMI value  corresponds to the codebook indices pair , and a second PMI value corresponds to the codebook index given in Table 7.2.4-j with  equal to the associated RI value and where j = .

- In some cases codebook subsampling is supported. The sub-sampled codebook for PUCCH mode 2-1 for value of parameter codebookConfig set to 2, 3, or 4 is defined in Table 7.2.2-1F for PUCCH Reporting Type 1a.

- UE shall only use the value of  according to the configured codebook subset restriction, where the UE is expected to be configured with a single value of  in {0,1,2,…,15} for 1 layer and in {0,1,2…,7} for 2 layers, and shall not report if the UE is configured with higher layer parameter semiOpenLoop=TRUE

Table 7.2.4-9: Supported configurations of and

| Number of  CSI-RS antenna ports, P |  |  |
| --- | --- | --- |
|  |  |  |
| 8 | (2,2) | (4,4), (8,8) |
| 12 | (2,3) | (8,4), (8,8) |
|  | (3,2) | (8,4), (4,4) |
| 16 | (2,4) | (8,4), (8,8) |
|  | (4,2) | (8,4), (4,4) |
|  | (8,1) | (4,-), (8,-) |
| 20 | (2,5) | (8,4) |
|  | (5,2) | (4,4) |
|  | (10,1) | (4,-) |
| 24 | (2,6) | (8,4) |
|  | (3,4) | (8,4) |
|  | (4,3) | (4,4) |
|  | (6,2) | (4,4) |
|  | (12,1) | (4,-) |
| 28 | (2,7) | (8,4) |
|  | (7,2) | (4,4) |
|  | (14,1) | (4,-) |
| 32 | (2,8) | (8,4) |
|  | (4,4) | (8,4) |
|  | (8,2) | (4,4) |
|  | (16,1) | (4,-) |

Table 7.2.4-10: Codebook for 1-layer CSI reporting using antenna ports 15 to 14+P

| Value of Codebook-Config |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 0 | 1 | 2 | 3 |
| 1 |  |  |  |  |  |  |
| where |  |  |  |  |  |  |

| Value of Codebook-Config |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 0 | 1 | 2 | 3 |
| 2 |  |  |  |  |  |  |
| Value of Codebook-Config |  |  |  |  |  |  |
|  |  |  | 4 | 5 | 6 | 7 |
| 2 |  |  |  |  |  |  |
| Value of Codebook-Config |  |  |  |  |  |  |
|  |  |  | 8 | 9 | 10 | 11 |
| 2 |  |  |  |  |  |  |
| Value of Codebook-Config |  |  |  |  |  |  |
|  |  |  | 12 | 13 | 14 | 15 |
| 2 |  |  |  |  |  |  |
| where |  |  |  |  |  |  |

| Value of Codebook-Config |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 0 | 1 | 2 | 3 |
| 3 |  |  |  |  |  |  |
| Value of Codebook-Config |  |  |  |  |  |  |
|  |  |  | 4 | 5 | 6 | 7 |
| 3 |  |  |  |  |  |  |
| Value of Codebook-Config |  |  |  |  |  |  |
|  |  |  | 8 | 9 | 10 | 11 |
| 3 |  |  |  |  |  |  |
| Value of Codebook-Config |  |  |  |  |  |  |
|  |  |  | 12 | 13 | 14 | 15 |
| 3 |  |  |  |  |  |  |
| where , if , if |  |  |  |  |  |  |

| Value of Codebook-Config |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 0 | 1 | 2 | 3 |
| 4 |  |  |  |  |  |  |
| Value of Codebook-Config |  |  |  |  |  |  |
|  |  |  | 4 | 5 | 6 | 7 |
| 4 |  |  |  |  |  |  |
| Value of Codebook-Config |  |  |  |  |  |  |
|  |  |  | 8 | 9 | 10 | 11 |
| 4 |  |  |  |  |  |  |
| Value of Codebook-Config |  |  |  |  |  |  |
|  |  |  | 12 | 13 | 14 | 15 |
| 4 |  |  |  |  |  |  |
| where , if , if |  |  |  |  |  |  |

Table 7.2.4-11: Codebook for 2-layer CSI reporting using antenna ports 15 to 14+P

| 2 Layers, Codebook-Config = 1 |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 0 | 1 | 2 | 3 |
|  |  |  |  |  |
| where . |  |  |  |  |

| 2 Layers, Codebook-Config = 2 |  |  |  |  |
| --- | --- | --- | --- | --- |
| If |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 0 | 1 | 2 | 3 |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 8 | 9 | 10 | 11 |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 12 | 13 | 14 | 15 |
|  |  |  |  | . |
| where . |  |  |  |  |

| 2 Layers, Codebook-Config = 3 |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 0 | 1 | 2 | 3 |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 8 | 9 | 10 | 11 |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 12 | 13 | 14 | 15 |
|  |  |  |  |  |
| where  if  and, if |  |  |  |  |

| 2 Layers, Codebook-Config = 4 |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 0 | 1 | 2 | 3 |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 8 | 9 | 10 | 11 |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 12 | 13 | 14 | 15 |
|  |  |  |  |  |
| where  if  and, if |  |  |  |  |

Table 7.2.4-12: Codebook for 3-layer CSI reporting using antenna ports 15 to 14+P

| 3 Layers, Codebook-Config = 1, |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  | 0 | 1 |
|  |  |  |
|  |  |  |
| where  , |  |  |

| 3 Layers, Codebook-Config = 1, |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  | 0 | 1 |
|  |  |  |
|  |  |  |
|  |  |  |
| where  , |  |  |

| 3 Layers, Codebook-Config = 2 |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 0 | 1 | 2 | 3 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 8 | 9 | 10 | 11 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 12 | 13 | 14 | 15 |
|  |  |  |  |  |
|  |  |  |  |  |
| where  , |  |  |  |  |

| 3 Layers, Codebook-Config =3 |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 0 | 1 | 2 | 3 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 8 | 9 | 10 | 11 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 12 | 13 | 14 | 15 |
|  |  |  |  |  |
|  |  |  |  |  |
| where  , |  |  |  |  |

| 3 Layers, Codebook-Config =4, |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | 0 | 1 | 2 | 3 |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | 8 | 9 | 10 | 11 |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | 12 | 13 | 14 | 15 |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
| where  , |  |  |  |  |  |

| 3 Layers, Codebook-Config =4, |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | 0 | 1 | 2 | 3 |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | 8 | 9 | 10 | 11 |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | 12 | 13 | 14 | 15 |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
| where  , |  |  |  |  |  |

Table 7.2.4-13: Codebook for 4-layer CSI reporting using antenna ports 15 to 14+P

| 4 Layers, Codebook-Config = 1, |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  | 0 | 1 |
|  |  |  |
|  |  |  |
| where |  |  |

| 4 Layers, Codebook-Config = 1, |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  | 0 | 1 |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

| 4 Layers, Codebook-Config = 2 |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 0 | 1 | 2 | 3 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

| 4 Layers, Codebook-Config =3 |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 0 | 1 | 2 | 3 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

| 4 Layers, Codebook-Config =4, |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 0 | 1 | 2 | 3 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

| 4 Layers, Codebook-Config =4, |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 0 | 1 | 2 | 3 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

Table 7.2.4-14: Codebook for 5-layer CSI reporting using antenna ports 15 to 14+P

| 5 Layers, P=8, N1=N2 |  |  |  |
| --- | --- | --- | --- |
| Value of Codebook-Config |  |  |  |
| 1 |  |  |  |
| 2-4 |  |  |  |
| for Codebook-Config = 2-4 for Codebook-Config = 1 |  |  |  |

| 5 Layers, P=12 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Value of Codebook-Config | Configuration |  |  |  |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
|  |  |  |  |  |
| 4 |  |  |  |  |
|  |  |  |  |  |
| where for Codebook-Config = 2-4 for Codebook-Config = 1 |  |  |  |  |

| 5 Layers, |  |  |  |  |
| --- | --- | --- | --- | --- |
| Value of Codebook-Config | Configuration |  |  |  |
| 1 |  |  |  |  |
|  |  |  | 0 |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
|  |  |  |  |  |
| 4 | , |  |  |  |
|  |  |  | 0 |  |
|  |  |  |  |  |
| where  for Codebook-Config = 2-4  for Codebook-Config = 1 |  |  |  |  |

Table 7.2.4-15: Codebook for 6-layer CSI reporting using antenna ports 15 to 14+P

| 6 Layers, P=8, N1=N2 |  |  |  |
| --- | --- | --- | --- |
| Value of Codebook-Config |  |  |  |
| 1 |  |  |  |
| 2-4 |  |  |  |
| where  for Codebook-Config = 2-4 for Codebook-Config = 1 |  |  |  |

| 6 Layers, P=12 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Value of Codebook-Config | Configuration |  |  |  |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
|  |  |  |  |  |
| 4 |  |  |  |  |
|  |  |  |  |  |
| where  for Codebook-Config = 2-4  for Codebook-Config = 1 |  |  |  |  |

| 6 Layers, |  |  |  |  |
| --- | --- | --- | --- | --- |
| Value of Codebook-Config | Configuration |  |  |  |
| 1 |  |  |  |  |
|  |  |  | 0 |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
|  |  |  |  |  |
| 4 | , |  |  |  |
|  |  |  | 0 |  |
|  |  |  |  |  |
| where  for Codebook-Config = 2-4  and for Codebook-Config = 1 |  |  |  |  |

Table 7.2.4-16: Codebook for 7-layer CSI reporting using antenna ports 15 to 14+P

| 7 Layers P=8, N1=N2 |  |  |  |
| --- | --- | --- | --- |
| Value of Codebook-Config |  |  |  |
| 1 |  |  |  |
| 2-4 |  |  |  |
| where for Codebook-Config = 2-4 for Codebook-Config = 1 |  |  |  |

| 7 Layers, P=12 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Value of Codebook-Config | Configuration |  |  |  |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
|  |  |  |  |  |
| 4 |  |  |  |  |
|  |  |  |  |  |
| where for Codebook-Config = 2-4  for Codebook-Config = 1 |  |  |  |  |

| 7 Layers, |  |  |  |  |
| --- | --- | --- | --- | --- |
| Value of Codebook-Config | Configuration |  |  |  |
| 1 |  |  |  |  |
|  |  |  | 0 |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
|  |  |  |  |  |
| 4 | , |  |  |  |
|  |  |  | 0 |  |
|  |  |  |  |  |
| where  for Codebook-Config = 2-4 and for Codebook-Config = 1 |  |  |  |  |

Table 7.2.4-17: Codebook for 8-layer CSI reporting using antenna ports 15 to 14+P

| 8 Layers, P=8, N1=N2 |  |  |  |
| --- | --- | --- | --- |
| Value of Codebook-Config |  |  |  |
| 1 |  |  |  |
| 2-4 |  |  |  |
| where for Codebook-Config = 2-4for Codebook-Config = 1 |  |  |  |

| 8 Layers, P=12 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Value of Codebook-Config | Configuration |  |  |  |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
|  |  |  |  |  |
| 4 |  |  |  |  |
|  |  |  |  |  |
| where  for Codebook-Config = 2-4  for Codebook-Config = 1 |  |  |  |  |

| 8 Layers, |  |  |  |  |
| --- | --- | --- | --- | --- |
| Value of Codebook-Config | Configuration |  |  |  |
| 1 |  |  |  |  |
|  |  |  | 0 |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
|  |  |  |  |  |
| 4 | , |  |  |  |
|  |  |  | 0 |  |
|  |  |  |  |  |
| where  for Codebook-Config = 2-4  Codebook-Config = 1 |  |  |  |  |

For 4 antenna ports , 8 antenna ports , 12 antenna ports , 16 antenna ports , 20 antenna ports , 24 antenna ports , 28 antenna ports , 32 antenna ports , and UE configured with higher layer parameter advancedCodebookEnabled=TRUE, and  with  equal to the associated RI value, each PMI value corresponds to four codebook indices given in Table 7.2.4-17C, where the quantities , and  are given by

The values of ,  are configured with the higher-layer parameter codebookConfig-N1, and codebookConfig-N2 respectively. The supported configurations of  for a given number of CSI-RS ports are given in Table 7.2.4-9. In addition,  and  are also supported configurations. The number of CSI-RS ports, P, is . ;  if, otherwise.

UE shall only use and shall not report if the value of codebookConfigN2 is set to 1.

A first PMI value  corresponds to the codebook indices combination , and a second PMI value corresponds to the codebook index  given in Table 7.2.4-17C for 1-layer and 2-layers.  for 1-layer, and  for 2-layers where  is the index for the layer. The mapping of  to  and  is given in Table 7.2.4-17A and relative power indicator (RPI), , to  is given in Table 7.2.4-17B.

In some cases codebook subsampling is supported. The sub-sampled codebook for PUCCH mode 1-1 for value of  is defined in Table 7.2.2-1H for PUCCH Reporting Type 2b.

Table 7.2.4-17A: Mapping of  field to  and

| Value of |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| 1 | 2 | 0 | 2 | 0 | 0 | 1 | 0 | 2 | 0 | 2 | 2 | 0 |  |  | 2 | 0 |
| 2 | 3 | 0 | 0 | 1 | 1 | 1 | 0 | 3 | 1 | 0 | 3 | 0 |  |  | 3 | 0 |
| 3 | 0 | 1 | 1 | 1 |  |  | 1 | 0 | 1 | 1 | 4 | 0 |  |  |  |  |
| 4 | 1 | 1 | 2 | 1 |  |  | 1 | 1 | 1 | 2 | 5 | 0 |  |  |  |  |
| 5 | 2 | 1 |  |  |  |  | 1 | 2 |  |  | 6 | 0 |  |  |  |  |
| 6 | 3 | 1 |  |  |  |  | 1 | 3 |  |  | 7 | 0 |  |  |  |  |

Table 7.2.1-17B: Mapping of  field to

| Value of  field |  |
| --- | --- |
| 0 |  |
| 1 |  |
| 2 |  |
| 3 |  |

Table 7.2.4-17C: Codebook for 1-layer and 2-layer CSI reporting using antenna ports 15 to 14+P

| 1 and 2 Layers |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| ,, | 0 | 1 | 2 | 3 |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
|  |  |  |  |  |
|  | 8 | 9 | 10 | 11 |
|  |  |  |  |  |
|  | 12 | 13 | 14 | 15 |
|  |  |  |  |  |
|  |  |  |  |  |
| ,, | 0 | 1 | 2 | 3 |
|  |  |  |  |  |
|  | 4 | 5 | 6 | 7 |
|  |  |  |  |  |
|  | 8 | 9 | 10 | 11 |
|  |  |  |  |  |
|  | 12 | 13 | 14 | 15 |
|  |  |  |  |  |
|  | For one layer: ,and for two layers: $ W_{k_{1},k_{2},m_{1},m_{2},p,q_{1,1},q_{2,1},q_{3,1},q_{1,2},q_{2,2},q_{3,2}}^{(2)}=\frac {1}{\sqrt {2}}\left [ \begin {matrix}W_{k_{1},k_{2},m_{1},m_{2},p,q_{1,1},q_{2,1},q_{3,1}}^{1} & W_{k_{1},k_{2},m_{1},m_{2},p,q_{1,2},q_{2,2},q_{3,2}}^{2}\end {matrix}\right ] $ |  |  |  |
|  |  |  |  |  |

For a UE configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured, or a UE configured with higher layer parameter eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B', and one CSI-RS resource configured, and higher layer parameter alternativeCodebookEnabledCLASSB_K1=TRUE configured,

- For 2 antenna ports, a PMI value corresponds to the codebook index  given in Table 7.2.4-18 with  equal to the associated RI value.

- For 2 antenna ports {15,16}, UE shall only use the precoding matrix corresponding to codebook index 0 in Table 6.3.4.2.3-1 of [3] with  and shall not report PMI value if the UE is configured with higher layer parameter semiOpenLoop=TRUE.

- For 4 antenna ports , a PMI corresponds to the codebook index  given in Table 7.2.4-19 with  equal to the associated RI value.

- For 4 antenna ports , UE shall not report PMI value and shall use the precoding matrix for REs of jth PRB-pair according to , where  is the precoder index given by and denote precoder matrices corresponding to precoder indices 12,13,14 and 15, respectively, in Table 6.3.4.2.3-2 of [3] with  if the UE is configured with higher layer parameter semiOpenLoop=TRUE.

- For 8 antenna ports, a PMI value corresponds to the codebook index  given in Table 7.2.4-20 with  equal to the associated RI value.

where is a length-N column-vector where its l-th element is 1 for k=l (), and 0 otherwise.

Table 7.2.4-18: Codebook for -layer CSI reporting using antenna ports

| Codebook index, n | Number of layers |  |
| --- | --- | --- |
|  | 1 | 2 |
| 0 |  |  |
| 1 |  |  |
| 2 |  | - |
| 3 |  | - |

Table 7.2.4-19: Codebook for -layer CSI reporting using antenna ports

| Codebook index, n | Number of layers |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 | 4 |
| 0 |  |  |  |  |
| 1 |  |  |  |  |
| 2 |  |  |  | - |
| 3 |  |  |  | - |
| 4 |  |  | - | - |
| 5 |  |  | - | - |
| 6 |  |  | - | - |
| 7 |  |  | - | - |

Table 7.2.4-20: Codebook for -layer CSI reporting using antenna ports

| Codebook index, n | Number of layers |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 | 4 |
| 0 |  |  |  |  |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |
| 6 |  |  |  |  |
| 7 |  |  |  |  |
| 8 |  |  |  | - |
| 9 |  |  |  | - |
| 10 |  |  |  | - |
| 11 |  |  |  | - |
| 12 |  |  |  | - |
| 13 |  |  |  | - |
| 14 |  |  |  | - |
| 15 |  |  |  | - |

| Codebook index, n | Number of layers |  |
| --- | --- | --- |
|  | 5 | 6 |
| 0 |  |  |
| 1-15 | - | - |

| Codebook index, n | Number of layers |  |
| --- | --- | --- |
|  | 7 | 8 |
| 0 |  |  |
| 1-15 | - | - |

### 7.2.5 Channel-State Information – Reference Signal (CSI-RS) definition

For a serving cell and UE configured in transmission mode 9 and not configured with higher layer parameter eMIMO-Type and eMIMO-Type2, the UE can be configured with one CSI-RS resource configuration.

For a serving cell and UE configured in transmission mode 9 and configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', the UE can be configured with one CSI-RS resource configuration.

For a serving cell and UE configured in transmission mode 9 and configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', the UE can be configured with one or more CSI-RS resource configuration(s).

For a serving cell and UE configured in transmission mode 9 and configured with higher layer parameter eMIMO-Type2, and eMIMO-Type2 is set to 'CLASS B', the UE can be configured with one CSI-RS resource configuration.

For a serving cell and UE configured in transmission mode 10, the UE can be configured with one or more CSI-RS resource configuration(s).

The following parameters for which the UE shall assume non-zero transmission power for CSI-RS are configured via higher layer signaling for each CSI-RS resource configuration:

- CSI-RS resource configuration identity, if the UE is configured in transmission mode 9 and configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and the UE is configured with more than one CSI-RS resource configurations, or if the UE is configured in transmission mode 10,

- Number of CSI-RS ports. The allowable values and port mapping are given in Clause 6.10.5 of [3].

- CSI RS Configuration (see Table 6.10.5.2-1 and Table 6.10.5.2-2 in [3])

- CSI RS subframe configuration  except for aperiodic CSI-RS resource configuration. The allowable values are given in Clause 6.10.5.3 of [3].

- UE assumption on reference PDSCH transmitted power for CSI feedback , if the UE is configured in transmission mode 9.

- UE assumption on reference PDSCH transmitted power for CSI feedback  for each CSI process, if the UE is configured in transmission mode 10. If CSI subframe sets  and  are configured by higher layers for a CSI process, is configured for each CSI subframe set of the CSI process.

- Pseudo-random sequence generator parameter, . The allowable values are given in [11].

- CDM type parameter, if the UE is configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A' for a CSI process. The allowable values are given in Clause 6.10.5.2 of [3].

- frequencyDensity, if the UE is configured with higher layer parameter eMIMO-Type or eMIMO-Type2 for a CSI process. The allowable values are given in Clause 6.10.5.2 of [3].

- transmissionComb, if the UE is configured with higher layer parameter eMIMO-Type or eMIMO-Type2 for a CSI process. The allowable values are given in Clause 6.10.5.2 of [3].

- Higher layer parameter qcl-CRS-Info-r11 for quasi co-location type B or type C UE assumption of CRS antenna ports and CSI-RS antenna ports with the following parameters, if the UE is configured in transmission mode 10:

- qcl-ScramblingIdentity-r11.

- crs-PortsCount-r11.

- mbsfn-SubframeConfigList-r11.

is the assumed ratio of PDSCH EPRE to CSI-RS EPRE when UE derives CSI feedback and takes values in the range of [-8, 15] dB with 1 dB step size, where the PDSCH EPRE corresponds to the symbols for which the ratio of the PDSCH EPRE to the cell-specific RS EPRE is denoted by , as specified in Table 5.2-2 and Table 5.2-3.

A UE should not expect the configuration of CSI-RS and PMCH in the same subframe of a serving cell.

A BL/CE UE configured with CEModeA and higher layer parameter ce-CSI-RS-Feedback is not expected to be configured with aperiodic CSI-RS resource configuration.

For frame structure type 2 serving cell and 4 CRS ports, the UE is not expected to receive a CSI RS Configuration index (see Table 6.10.5.2-1 and Table 6.10.5.2-2 in [3]) belonging to the set [20-31] for the normal CP case or the set [16-27] for the extended CP case.

A UE may assume the CSI-RS antenna ports of a CSI-RS resource configuration are quasi co-located (as defined in [3]) with respect to delay spread, Doppler spread, Doppler shift, average gain, and average delay.

A UE configured in transmission mode 10 and with quasi co-location type B or type C, may assume the antenna ports 0 – 3 associated with qcl-CRS-Info-r11 corresponding to a CSI-RS resource configuration and antenna ports 15 – 46 corresponding to the CSI-RS resource configuration are quasi co-located (as defined in [3]) with respect to Doppler shift, and Doppler spread.

A UE configured in transmission mode 10, and configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS B', and the number of configured CSI-RS resources is more than one for a CSI process, and with quasi co-location type B, is not expected to receive CSI-RS resource configurations for the CSI process that have different values of the higher layer parameter qcl-CRS-Info-r11.

A UE configured in transmission mode 10, and configured with higher layer parameter eMIMO-Type and eMIMO-Type2, and with quasi co-location type B, is not expected to receive CSI-RS resource configurations for eMIMO-Type and eMIMO-Type2 of the CSI process that have different values of the higher layer parameter qcl-CRS-Info-r11.

A BL/CE UE configured with CEModeA or CEModeB is not expected to be configured with non-zero transmission power CSI-RS, except when the BL/CE UE is configured with the higher layer parameter ce-CSI-RS-Feedback.

A UE configured in transmission mode 9 or 10, and configured with higher layer parameter eMIMO-Type, and eMIMO-Type is set to 'CLASS A', and more than one CSI-RS configurations for a CSI-RS resource, is not expected to receive CSI-RS configurations for the CSI-RS resource that have different values of frequencyDensity.

### 7.2.6 Channel-State Information – Interference Measurement (CSI-IM) Resource definition

For a serving cell and UE configured in transmission mode 10, the UE can be configured with one or more CSI-IM resource configuration(s). The following parameters are configured via higher layer signaling for each CSI-IM resource configuration:

- Zero-power CSI RS Configuration (see Table 6.10.5.2-1 and Table 6.10.5.2-2 in [3])

- Zero-power CSI RS subframe configuration . The allowable values are given in Clause 6.10.5.3 of [3].

For a serving cell, if a UE is not configured with the higher layer parameter csi-SubframePatternConfig-r12, the UE is not expected to receive CSI-IM resource configuration(s) that are not all completely overlapping with one zero-power CSI-RS resource configuration which can be configured for the UE.

A UE is not expected to receive a CSI-IM resource configuration that is not completely overlapping with one of the zero-power CSI-RS resource configurations defined in Clause 7.2.7.

For a serving cell, if a UE is not configured with CSI subframe sets  and  for any CSI process, and the UE is configured with four CSI-IM resources, then the UE is not expected to be configured with CSI processes that are associated with all of the four CSI-IM resources.

A UE should not expect the configuration of CSI-IM resource and PMCH in the same subframe of a serving cell.

### 7.2.7 Zero Power CSI-RS Resource definition

For a serving cell and UE configured in transmission mode 1-9 and UE not configured with csi-SubframePatternConfig-r12 for the serving cell, the UE can be configured with one zero-power CSI-RS resource configuration. For a serving cell and UE configured in transmission mode 1-9 and UE configured with csi-SubframePatternConfig-r12 for the serving cell, the UE can be configured with up to two zero-power CSI-RS resource configurations. For a serving cell and UE configured in transmission mode 10, the UE can be configured with one or more zero-power CSI-RS resource configuration(s).

For a serving cell, the UE can be configured with up to 5 additional zero-power CSI-RS resource configurations according to the higher layer parameter ds-ZeroTxPowerCSI-RS-r12.

The following parameters are configured via higher layer signaling for each zero-power CSI-RS resource configuration:

- Zero-power CSI RS Configuration list (16-bit bitmap ZeroPowerCSI-RS in [3])

- Zero-power CSI RS subframe configuration  except for aperiodic zero-power CSI-RS resource configuration. The allowable values are given in Clause 6.10.5.3 of [3].

A UE should not expect the configuration of zero-power CSI-RS and PMCH in the same subframe of a serving cell.

For frame structure type 1 serving cell, the UE is not expected to receive the 16-bit bitmap ZeroPowerCSI-RS with any one of the 6 LSB bits set to 1 for the normal CP case, or with any one of the 8 LSB bits set to 1 for the extended CP case.

For frame structure type 2 serving cell and 4 CRS ports, the UE is not expected to receive the 16-bit bitmap ZeroPowerCSI-RS with any one of the 6 LSB bits set to 1 for the normal CP case, or with any one of the 8 LSB bits set to 1 for the extended CP case.

A BL/CE UE configured with CEModeA or CEModeB is not expected to be configured with zero-power CSI-RS.

### 7.2.8 CSI-RS Activation / Deactivation

For a serving cell and UE configured in transmission mode 9 or 10 and for a CSI process the UE configured with higher layer parameter eMIMO-Type and eMIMO-Type is set to 'CLASS B',

- if the UE is configured with higher layer parameter csi-RS-ConfigNZP-ApList, the higher layer parameter csi-RS-NZP-mode is set to aperiodic, and number of configured CSI-RS resources in csi-RS-ConfigNZP-ApList is more than 2 and more than the number of activated CSI-RS resources N given by the higher layer parameter activatedResources for the CSI process, or

- if the higher layer parameter csi-RS-NZP-mode is set to multiShot,

- when a UE receives an activation command [8] for CSI-RS resource(s) associated with the CSI process in subframe n, the corresponding actions in [8] and UE assumption on CSI-RS transmission corresponding to the  activated CSI-RS resource(s) shall be applied no later than the minimum requirement defined in [10] and no earlier than subframe n+8, where is the number of activated CSI-RS resources for the CSI process, and is the maximum number of CSI-RS resources supported by the UE for a CSI process of the serving cell given by the higher layer parameter nMaxResource-r14 included in the MIMO-UE-ParametersPerTM-r14xy,

- when a UE receives a deactivation command [8] for activated CSI-RS resource(s) associated with the CSI process in subframe n, the corresponding actions in [8] and UE assumption on cessation of CSI-RS transmission corresponding to the deactivated CSI-RS resource(s) shall apply no later than the minimum requirement defined in [10] and no later than subframe n+8.

## 7.3 UE procedure for reporting HARQ-ACK

If the UE is not configured with shortTTI, the term 'subframe/slot' refers to a subframe in this clause.

If the UE is configured with shortTTI, and UCI is to be transmitted in a slot, the term 'subframe/slot' refers to a slot, subframe otherwise, in this clause.

If the UE is configured withshortTTI, and UCI is to be transmitted in a subslot, the term 'slot/subslot' refers to a subslot, slot otherwise, in this clause.

If the UE is configured with a PUCCH-SCell, the UE shall apply the procedures described in this clause for both primary PUCCH group and secondary PUCCH group unless stated otherwise

When the procedures are applied for the primary PUCCH group, the terms 'secondary cell', 'secondary cells', 'serving cell', and 'serving cells' in this clause refer to secondary cell, secondary cells, serving cell or serving cells belonging to the primary PUCCH group respectively unless stated otherwise.

When the procedures are applied for secondary PUCCH group, the terms 'secondary cell', 'secondary cells', 'serving cell' and 'serving cells' in this clause refer to secondary cell, secondary cells (not including the PUCCH-SCell), serving cell, serving cells belonging to the secondary PUCCH group respectively unless stated otherwise. The term 'primary cell' in this clause refers to the PUCCH-SCell of the secondary PUCCH group.

If each of the serving cell(s) configured for the UE has frame structure type 1, the UE procedure for HARQ-ACK reporting for frame structure type 1 is given in Clause 7.3.1.

If each of the serving cell(s) configured for the UE has frame structure type 2, the UE procedure for HARQ-ACK reporting for frame structure type 2 is given in Clause 7.3.2.

If the UE is configured with more than one serving cell, and if the frame structure type of any two configured serving cells is different, and if the primary cell is frame structure type 1, UE procedure for HARQ-ACK reporting is given in Clause 7.3.3.

If the UE is configured for more than one serving cell, and if the frame structure type of any two configured serving cells is different, and if the primary cell is frame structure type 2, UE procedure for HARQ-ACK reporting is given in Clause 7.3.4.

For a UE configured with EN-DC/NE-DC

- if serving cell frame structure type 1, and if the UE is configured with tdm-PatternConfig/tdm-PatternConfigNE-DC for the serving cell, or

- if the UE configured with EN-DC, and if serving cell frame structure type 1, and if the UE is configured with tdm-PatternConfig2 for the serving cell, or

- if the UE configured with EN-DC, and if primary cell frame structure type 2, and if the UE is configured with tdm-PatternConfig2 for the primary cell, and if the UE configured with more than one serving cells, and if secondary serving cell frame structure type 2 with different UL/DL configuration than the primary cell, or if secondary serving cell is frame structure type 1,

- UE procedure for HARQ-ACK reporting for the serving cell is given in Clause 7.3.4 assuming primary cell frame structure type 2 with "UL/DL configuration" given by tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2 and serving cell frame structure type 1. The UE shall apply an offset value given by harq-Offset-r15/harq-Offset-r16 to the subframe index in the UL/DL configuration for determining the HARQ-ACK reporting for the serving cell.

- if the UE configured with EN-DC, and if primary cell frame structure type 2, and if the UE is configured with tdm-PatternConfig2 for the primary cell,

- UE procedure for HARQ-ACK reporting for the primary cell is given in Clause 7.3.2.1 assuming the UE is configured with one serving cell with "UL/DL configuration" given by tdm-PatternConfig2 and serving cell frame structure type 2. The UE shall apply an offset value given by harq-Offset-r16 to the subframe index in the UL/DL configuration for determining the HARQ-ACK reporting for the serving cell.

- if serving cell frame structure type 1, and if the UE is configured with tdm-PatternConfig/tdm-PatternConfigNE-DC for the serving cell, or if the UE configured with EN-DC, and if the UE does not indicate a capability for dynamic power sharing (as specified in [17]), and if the UE is configured with tdm-PatternConfig2 for the serving cell, the UE is not expected to transmit any uplink physical channel or signal in the serving cell on subframes other than the offset-UL subframes, where the offset-UL subframes are determined by applying the offset value to the subframes denoted as uplink in the UL/DL configuration.

- if serving cell frame structure type 1, and if the UE is configured with tdm-PatternConfig/tdm-PatternConfigNE-DC for the serving cell, or if the UE configured with EN-DC, and if serving cell frame structure type 1, and if the UE is configured with tdm-PatternConfig2 for the serving cell,

- For a PDSCH data transmissions signalled via PDCCH in common search space for which HARQ-ACK response shall be provided, the UE shall assume the value of the DAI field in the corresponding DCI format is equal to '1'. If the UE transmits HARQ-ACK on PUSCH scheduled via PDCCH in common search space, the UE shall assume the value of the DAI field in the DCI format for scheduling the PUSCH is equal to '1' and the UE is not expected to receive PDSCH scheduled via PDCCH/EPDDCH in UE-specific search space for which the HARQ-ACK response is multiplexed onto the PUSCH.

For a UE configured with EN-DC/NE-DC and more than one serving cells,

- if primary cell frame structure type 1 and if the UE is configured with tdm-PatternConfig/tdm-PatternConfigNE-DC for the primary cell, or

- if the UE configured with EN-DC, and if primary cell frame structure type 1 and if the UE is configured with tdm-PatternConfig2 for the primary cell, or

- if the UE configured with EN-DC, and if primary cell frame structure type 2 and if the UE is configured with tdm-PatternConfig2 for the primary cell and if secondary serving cell has the same UL/DL configuration as the primary cell,

- UE procedure for HARQ-ACK reporting of each secondary cell follows the procedure of the primary cell.

Throughout this clause,

- if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space, and otherwise.

- if the UE is configured with higher layer parameter shortTTI and for PDSCH transmissions in a subslot,  is determined based on higher layer parameter proc-Timeline-r15, where

- = 4 if proc-Timeline-r15 is set to 'nplus4set1'

- = 6 if proc-Timeline-r15 is set to 'nplus6set1' or 'nplus6set2'

- = 8 if proc-Timeline-r15 is set to 'nplus8set2'

- for a BL/CE UE, the value of $ K_{offset}$ is given by,

- if the UE is configured with the higher layer parameter k-Offset,

- $ K_{offset}=K_{cell\_offset}-K_{UE\_offset}$ where

$ K_{cell\_offset}$ is the parameter k-Offset provided by higher layers, and

$ K_{UE\_offset}$ is the parameter Differential Koffset provided by higher layers, otherwise $ K_{UE\_offset}=0 $

- otherwise,

- $ K_{offset}=0 $.

If the UE is configured with higher layer parameter k-Offset, for a PUSCH (re)transmission associated with the TC-RNTI, $ K_{offset}=$ k-Offset.

If the UE is configured with higher layer parameter shortTTI, and the UE has received slot/subslot-PDSCH without an associated PDCCH/SPDCCH or with an associated PDCCH/SPDCCH with DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G for which slot/subslot-PUCCH including HARQ-ACK and SR (if any) is to be transmitted on slot/subslot s of subframe n,

- If the UE is configured with higher layer parameter codebooksizeDetermination-r13 = dai, the UE shall transmit the HARQ-ACK corresponding to subframe-PDSCH on the slot/subslot-PUCCH if the UE has received subframe-PDSCH without an associated PDCCH/SPDCCH or with an associated PDCCH/EPDCCH with DCI format 1/1A/1B/1D/2/2A/2B/2C/2D on subframe of a serving cell and if the slot/subslot-PUCCH is the first occurrence of the slot/subslot-PUCCH/PUSCH in the subframe;

- If the UE is configured with no more than five serving cells or if the UE is configured with higher layer parameter codebooksizeDetermination-r13 = cc, the UE shall transmit the HARQ-ACK corresponding to subframe-PDSCH for all serving cells on the slot/subslot-PUCCH regardless whether the UE has received subframe-PDSCH without an associated PDCCH/SPDCCH or with an associated PDCCH/EPDCCH with DCI format 1/1A/1B/1D/2/2A/2B/2C/2D associated with subframe-PDSCH for any of the serving cell(s) on subframe . If the UE has not received subframe-PDSCH for a serving cell on subframe, the corresponding HARQ-ACK bit(s) is NACK;

and

-  for FDD, and  for TDD where  is defined in Table 10.1.3.1-1B if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space for subframe-PDSCH, and in Table 10.1.3.1-1 otherwise.

- spatial bundling of the HARQ-ACK corresponding to subframe-PDSCH is applied if the HARQ-ACK is to be transmitted on

- subslot s or

- slot s and spatialBundlingPUCCH is set TRUE.

- the sequence of HARQ-ACK bit(s) corresponding to subframe-PDSCH  is determined in Clause 5.2.3.1A of [4]

If the UE is configured with higher layer parameter shortTTI, and the UE transmits slot/subslot-PUSCH on slot/subslot s of subframe n without associated PDCCH/SPDCCH or with associated PDCCH/SPDCCH with DCI format 7-0A/7-0B and if the UE is not configured with simultaneous PUSCH and PUCCH transmission,

- the UE shall transmit the HARQ-ACK corresponding to subframe-PDSCH on the slot/subslot-PUSCH if the UE has received subframe-PDSCH on subframe of a serving cell and if the slot/subslot-PUSCH is the first occurrence of the slot/subslot-PUCCH/PUSCH in the subframe;

- if the UE is configured with no more than five serving cells or if the UE is configured with higher layer parameter codebooksizeDetermination-r13 = cc, the UE shall transmit the HARQ-ACK corresponding to subframe-PDSCH for all serving cells on the slot/subslot-PUSCH if the UE has received slot/subslot-PDSCH without an associated PDCCH/SPDCCH or with an associated PDCCH/SPDCCH with DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G for which HARQ-ACK response shall be provided on slot/subslot s of subframe n, and

- if the UE has received subframe-PDSCH without an associated PDCCH/EPDCCH or with an associated PDCCH/EPDCCH with DCI format 1/1A/1B/1D/2/2A/2B/2C/2D for at least one of the serving cell(s) on subframe , or

- if the UE has not received subframe-PDSCH without an associated PDCCH/EPDCCH or with an associated PDCCH/EPDCCH with DCI format 1/1A/1B/1D/2/2A/2B/2C/2D for any of the serving cell(s) on subframe , and if the slot/subslot-PUSCH is the first occurrence of the slot/subslot-PUCCH/PUSCH in the subframe;

- the corresponding HARQ-ACK bit(s) is NACK, if the UE has not received subframe-PDSCH without an associated PDCCH/SPDCCH or with an associated PDCCH/EPDCCH with DCI format 1/1A/1B/1D/2/2A/2B/2C/2D for a serving cell(s) on subframe ;

and

-  for FDD, and  for TDD where  is defined in Table 10.1.3.1-1B if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space for subframe-PDSCH, and in Table 10.1.3.1-1 otherwise.

- spatial bundling of the HARQ-ACK corresponding to subframe-PDSCH is applied if the HARQ-ACK is to be transmitted on

- subslot s or

- slot s and spatialBundlingPUCCH is set TRUE

- the sequence of HARQ-ACK bit(s) corresponding to subframe-PDSCH  is determined in Clause 5.2.2.6 of [4].

If the UE is configured with higher layer parameter blindSubframePDSCH-Repetitions for a given serving cell, UE procedure for HARQ-ACK reporting for the serving cell corresponding to a PDCCH/EPDCCH with DCI format 1A with CRC scrambled by C-RNTI in UE-specific search space is given in this clause assuming the subframe-PDSCH is received in the last subframe of the set of received k DL subframes according to the PDCCH/EPDCCH information as described in clause 7.1.

If the UE is configured with higher layer parameter blindSlotSubslotPDSCH-Repetitions for a given serving cell, UE procedure for HARQ-ACK reporting for the serving cell corresponding to a PDCCH/SPDCCH with DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G with CRC scrambled by C-RNTI is given in this clause assuming the slot/subslot-PDSCH is received in the last slot/subslot of the set of received k DL slots/subslots according to the PDCCH/SPDCCH information as described in clause 7.1.

For a BL/CE UE in a NTN FDD serving cell, and the UE not configured with higher layer parameter downlinkHARQ-FeedbackDisabledDCI and configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap indicating enabled HARQ-ACK information for a HARQ process associated with a transport block in the PDSCH, the UE shall provide HARQ-ACK for the HARQ process associated with the transport block.

For a BL/CE UE in a NTN FDD serving cell, and the UE configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap indicating disabled HARQ-ACK information for a HARQ process associated with a transport block in the PDSCH, the UE shall provide HARQ-ACK for a HARQ process associated with a transport block in a detected PDSCH

- if the UE is configured with CEModeA, and configured with higher layer parameter harq-FeedbackEnablingforSPSactive = 'enabled', and the detected PDSCH is the first SPS PDSCH after SPS activation.

For a BL/CE UE in a NTN FDD serving cell, and the UE configured with CEModeB and higher layer parameter downlinkHARQ-FeedbackDisabledDCI, the UE shall provide HARQ-ACK for a HARQ process associated with a transport block in a detected PDSCH

- if the HARQ-ACK Resource offset field does not function as HARQ feedback disabled indicator as specified in [4] in DCI format 6-1B in the MPDCCH corresponding to the PDSCH.

For a BL/CE UE in half-duplex FDD operation in a NTN serving cell, if the UE is configured with CEModeA, and configured with higher layer parameter ce-HARQ-AckBundling, and configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap indicating disabled HARQ-ACK information for a HARQ process associated with a transport block in the PDSCH, the UE is not expected to receive the corresponding DCI with HARQ-ACK bundling flag set to 1.

For a BL/CE UE, if the UE is configured with CEModeA, and if the UE is configured with higher layer parameter harq-AckBundling in ce-PDSCH-MultiTB-Config and multiple TB are scheduled in the corresponding DCI format 6-1A with CRC scrambled by C-RNTI,

- for the UE in a NTN FDD serving cell, if the UE is configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap indicating disabled HARQ-ACK information for a HARQ process associated with a transport block of the multiple TB, and if the UE shall provide HARQ-ACK for at least one TB of the multiple TB, the UE shall generate an ACK for HARQ-ACK corresponding to the transport block associated with the HARQ process with disabled HARQ-ACK information;

- for HARQ-ACK transmission associated with the corresponding DCI, the UE shall generate M HARQ-ACK bits by performing a logical AND operation of HARQ-ACKs across all TBs in each TB bundle $ A_{b}$ where b = 1, …, M;

- the set of TBs that belong to TB bundle $ A_{b}$ and the number of TB bundles M are given by Table 7.3-1;

- the value of ![](media_svg/image319.svg) [公式≈: ^{N}TB]is the number of scheduled TB determined in the corresponding DCI.

Table 7.3-1: Value of $ A_{b}$ and M for different values of DCI field 'Multi-TB HARQ-ACK bundling size' and for different values of number of scheduled transport blocks $ N_{TB}$

| DCI field 'Multi-TB HARQ-ACK  bundling size' | $ N_{TB}=1 $ | $ N_{TB}=2 $ | $ N_{TB}=4 $ | $ N_{TB}=6 $ | $ N_{TB}=8 $ |
| --- | --- | --- | --- | --- | --- |
| 00 | $ A_{1}=\{TB_{0}\}$ | $ A_{1}=\left \{ TB_{0}\right \} $ $ A_{2}=\left \{ TB_{1}\right \} $ | $ A_{1}=\left \{ TB_{0}\right \} $ $ A_{2}=\left \{ TB_{1}\right \} $ $ A_{3}=\left \{ TB_{2}\right \} $ $ A_{4}=\left \{ TB_{3}\right \} $ | $ A_{1}=\left \{ TB_{0}\right \} $ $ A_{2}=\left \{ TB_{1}\right \} $ $ A_{3}=\left \{ TB_{2}\right \} $ $ A_{4}=\left \{ TB_{3}\right \} $ $ A_{5}=\left \{ TB_{4}\right \} $ $ A_{6}=\left \{ TB_{5}\right \} $ | $ A_{1}=\left \{ TB_{0}\right \} $ $ A_{2}=\left \{ TB_{1}\right \} $ $ A_{3}=\left \{ TB_{2}\right \} $ $ A_{4}=\left \{ TB_{3}\right \} $ $ A_{5}=\left \{ TB_{4}\right \} $ $ A_{6}=\left \{ TB_{5}\right \} $ $ A_{7}=\left \{ TB_{6}\right \} $ $ A_{8}=\left \{ TB_{7}\right \} $ |
| 01 | - | $ A_{1}=\left \{ TB_{0}, TB_{1}\right \} $ | $ A_{1}=\left \{ TB_{0}, TB_{1}\right \} $ $ A_{2}=\left \{ TB_{2}, TB_{3}\right \} $ | $ A_{1}=\left \{ TB_{0}, TB_{1}\right \} $ $ A_{2}=\left \{ TB_{2}, TB_{3}\right \} $ $ A_{3}=\left \{ TB_{4}, TB_{5}\right \} $ | $ A_{1}=\left \{ TB_{0}, TB_{1}\right \} $ $ A_{2}=\left \{ TB_{2}, TB_{3}\right \} $ $ A_{3}=\left \{ TB_{4}, TB_{5}\right \} $ $ A_{4}=\left \{ TB_{6}, TB_{7}\right \} $ |
| 10 | - | - | $ A_{1}=\left \{ TB_{0}, TB_{1}\right \} $ $ A_{2}=\left \{ TB_{2}\right \} $ $ A_{3}=\left \{ TB_{3}\right \} $ | $ A_{1}=\left \{ TB_{0}, TB_{1},TB_{2}\right \} $ $ A_{2}=\left \{ TB_{3}, TB_{4},TB_{5}\right \} $ | $ A_{1}=\left \{ TB_{0}, TB_{1},TB_{2}\right \} $ $ A_{2}=\left \{ TB_{3}, TB_{4},TB_{5}\right \} $ $ A_{3}=\left \{ TB_{6}, TB_{7}\right \} $ |
| 11 | - | - | $ A_{1}=\left \{ TB_{0}, TB_{1},TB_{2}, TB_{3}\right \} $ | $ A_{1}=\left \{ TB_{0}, TB_{1},TB_{2},TB_{3}\right \} $ $ A_{2}=\left \{ TB_{4}, TB_{5}\right \} $ | $ A_{1}=\left \{ TB_{0}, TB_{1},TB_{2},TB_{3}\right \} $ $ A_{2}=\left \{ TB_{4}, TB_{5},TB_{6},TB_{7}\right \} $ |

### 7.3.1 FDD HARQ-ACK reporting procedure

For FDD with PUCCH format 1a/1b transmission, when both HARQ-ACK and SR are transmitted in the same sub-frame/slot, a UE shall transmit the HARQ-ACK on its assigned HARQ-ACK PUCCH format 1a/1b resource for a negative SR transmission and transmit the HARQ-ACK on its assigned SR PUCCH resource for a positive SR transmission.

For FDD with PUCCH format 1a transmission, when both HARQ-ACK and SR are transmitted in the same subslot, a UE shall transmit the HARQ-ACK bit according to Table 7.3.1-0A;

Table 7.3.1-0A: PUCCH format 1a resource for transmission of HARQ-ACK bit and SR

| HARQ-ACK | SR transmission | Resource for HARQ-ACK bits transmission |
| --- | --- | --- |
| ACK/NACK | negative | HARQ-ACK PUCCH format 1a resource |
| NACK | positive | The first SR PUCCH resource value configured by the higher layers |
| ACK | positive | The second SR PUCCH resource value configured by the higher layers |

for FDD with PUCCH format 1b transmission, when both HARQ-ACK and SR are transmitted in the same subslot, a UE shall transmit the HARQ-ACK bits according to Table 7.3.1-0B;

Table 7.3.1-0B: PUCCH format 1b resource for transmission of HARQ-ACK bits

| HARQ-ACK(0) | HARQ-ACK(1) | SR transmission | Resource for HARQ-ACK bits transmission |
| --- | --- | --- | --- |
| ACK/NACK | ACK/NACK | negative | HARQ-ACK PUCCH format 1b resource |
| NACK | NACK | positive | The first SR PUCCH resource value configured by the higher layers |
| ACK | NACK | positive | The second SR PUCCH resource value configured by the higher layers |
| NACK | ACK | positive | The third SR PUCCH resource value configured by the higher layers |
| ACK | ACK | positive | The fourth SR PUCCH resource value configured by the higher layers |

where SR PUCCH resources are configured by higher layer parameter sr-SubslotSPUCCH-Resource, and HARQ-ACK(j), j=0, 1 denotes the ACK/NACK response for a transport block or SPS release PDCCH/EPDCCH/SPDCCH associated with serving cell c.

For FDD with PUCCH format 1b with channel selection, when both HARQ-ACK and SR are transmitted in the same sub-frame a UE shall transmit the HARQ-ACK on its assigned HARQ-ACK PUCCH resource with channel selection as defined in Clause 10.1.2.2.1 for a negative SR transmission and transmit one HARQ-ACK bit per serving cell on its assigned SR PUCCH resource for a positive SR transmission according to the following:

if only one transport block or a PDCCH/EPDCCH indicating downlink SPS release is detected on a serving cell, the HARQ-ACK bit for the serving cell is the HARQ-ACK bit corresponding to the transport block or the PDCCH/EPDCCH indicating downlink SPS release;

if two transport blocks are received on a serving cell, the HARQ-ACK bit for the serving cell is generated by spatially bundling the HARQ-ACK bits corresponding to the transport blocks;

if neither PDSCH transmission for which HARQ-ACK response shall be provided nor PDCCH/EPDCCH indicating downlink SPS release is detected for a serving cell, the HARQ-ACK bit for the serving cell is set to NACK;

and the HARQ-ACK bits for the primary cell and the secondary cell are mapped to  and , respectively, where  and  are specified in Clause 5.4.1 in [3].

For FDD, when a PUCCH format 3/4/5 transmission of HARQ-ACK coincides with a subframe/slot/subslot configured to the UE by higher layers for transmission of a scheduling request, the UE shall multiplex HARQ-ACK and SR bits on HARQ-ACK PUCCH resource as defined in Clause 5.2.3.1 in [4], unless the HARQ-ACK corresponds to a subframe-PDSCH transmission on the primary cell only or a PDCCH/EPDCCH indicating downlink SPS release on the primary cell only, in which case the SR shall be transmitted as for FDD with PUCCH format 1a/1b.

For a non-BL/CE UE for FDD and for a PUSCH transmission, a UE shall not transmit HARQ-ACK on PUSCH in subframe/slot/subslot n if the UE does not receive PDSCH or PDCCH/SPDCCH indicating downlink SPS release in

- subframe n- for subframe-PDSCH or in subframe  for PDCCH indicating downlink SPS release

- slot n-4 for slot-PDSCH

- subslot for subslot-SPDSCH if the higher layer parameter ul-TTI-Length is set to 'subslot'

- any of the subslot numbers listed in Table 10.1-1 if the higher layer parameter ul-TTI-Length is set to 'slot' and slot-PUSCH is transmitted in subframe

For a BL/CE UE, for FDD and for a PUSCH transmission scheduled by an MPDCCH where the last transmission of the MPDCCH is in subframe n-4-Koffset, a UE shall not transmit HARQ-ACK on PUSCH in subframe n if there is no PDSCH or MPDCCH indicating downlink SPS release transmitted to the UE in subframe n-4-Koffset where the last transmission of the PDSCH or MPDCCH indicating downlink SPS release is in subframe n-4-Koffset.

When only a positive SR is transmitted using subframe-PUCCH, a UE shall use PUCCH Format 1 for the SR resource as defined in Clause 5.4.1 in [3].

When only a positive SR is transmitted using slot/subslot-PUCCH, a UE shall use PUCCH Format 1 for the first SR resource configured by higher layers as defined in Clause 5.4A.2 in [3].

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = dai and PDSCH is associated with DCI format 1/1A/1B/1D/2/2A/2B/2C/2D, the following HARQ-ACK reporting procedure applies to subframe-PDSCH operation. If a UE is configured with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai and PDSCH is associated with DCI format 7-1A/7-1B/7-1C/7-1D/7-1F/7-1G, the following HARQ-ACK reporting procedure applies to slot/subslot-PDSCH operation.

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = dai or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai, for FDD and a subframe/subslot n, the value of the counter Downlink Assignment Indicator (DAI) in DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1F/7-1G denotes the accumulative number of {serving cell, subframe/slot/subslot}-pair(s) with PDSCH transmission(s) associated with PDCCH/EPDCCH/SPDCCH and serving cell with PDCCH/EPDCCH/SPDCCH indicating downlink SPS release, up to the present serving cell and present subframe/slot/subslot, first in increasing order of serving cell index and then in increasing order of subframe/slot/subslot index; the value of the total DAI in DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G denotes the total number of {serving cell, subframe/slot/subslot}-pair(s) with PDSCH transmission(s) associated with PDCCH/EPDCCH/SPDCCH (s) and serving cell with PDCCH/EPDCCH/SPDCCH indicating downlink SPS release. Denote  as the value of the counter DAI in DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1F/7-1G scheduling PDSCH transmission or indicating downlink SPS release for serving cell c in subframe/slot/subslot s within the set of subframe(s)/slot(s)/subslot(s) for which HARQ-ACK response shall be provided in subframe/slot/subslot n, according to table 7.3.1-1. Denote  as the value of the total DAI, according to Table 7.3.1-1. The UE shall assume a same value of total DAI in all PDCCH/EPDCCH/SPDCCH scheduling PDSCH transmission(s) and PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in a subframe/slot/subslot.

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = dai or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai and if the UE transmits HARQ-ACK using PUCCH format 3 or PUCCH format 4 or PUCCH format 5 in subframe/slot/subslot n, the UE shall determine the  according to the following pseudo-code:

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell

Set s = 0

Set j = 0

Set

Set

Set  to the number of cells configured by higher layers for the UE

Set S = 3 for subslot PDSCH operation with higher layer parameter dl-TTI-Length='subslot' and ul-TTI-Length='slot'; S = 2 for subframe-PDSCH operation with the higher layer parameter shortProcessingTime configured; 1 otherwise

while s < S

while c <

if there is a PDSCH on serving cell c associated with PDCCH/EPDCCH/SPDCCH or there is a PDCCH/EPDCCH/SPDCCH indicating downlink SPS release on serving cell c for which HARQ-ACK is transmitted in subframe/slot/subslot n, or

if

end if

if

j = j+1

end if

if the higher layer parameter spatialBundlingPUCCH is set FALSE and the UE is configured with a transmission mode supporting two transport blocks in at least one configured serving cell and HARQ-ACK is not to be transmitted on subslot-PUCCH,

= HARQ-ACK bit corresponding to the first codeword of this cell

= HARQ-ACK bit corresponding to the second codeword of this cell

elseif the higher layer parameter spatialBundlingPUCCH is set TRUE and the UE is configured with a transmission mode supporting two transport blocks in at least one configured serving cell or HARQ-ACK is to be transmitted on subslot-PUCCH,

= binary AND operation of the HARQ-ACK bits corresponding to the first and second codewords of this cell

else

= HARQ-ACK bit for subframe/slot/subslot s of this cell.

end if

end if

c = c + 1

end while

s = s + 1

end while

if

j = j+1

end if

if the higher layer parameter spatialBundlingPUCCH is set FALSE and the UE is configured with a transmission mode supporting two transport blocks in at least one configured serving cell and HARQ-ACK is not to be transmitted on subslot-PUCCH,

else

end if

for any

if SPS PDSCH transmission is activated for a UE and the UE is configured to receive SPS PDSCH in subframe/slot  or in subslot

= HARQ-ACK bit associated with the SPS PDSCH transmission

end if

For a UE configured with higher layer parameter codebooksizeDetermination-r13 = dai or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai, if the UE transmits HARQ-ACK on PUSCH in a subframe/slot/subslot, the UE shall determine the  according to the above procedure as if the UE transmits HARQ-ACK using PUCCH format 3 or PUCCH format 4 or PUCCH format 5, except that the higher layer parameter spatialBundlingPUCCH is replaced by spatialBundlingPUSCH.

Table 7.3.1-1: Value of counter DAI and total DAI

| DAI MSB, LSB | or | Number of serving cells with PDSCH transmission associated with PDCCH/EPDCCH/SPDCCH and serving cell with PDCCH/EPDCCH/SPDCCH indicating DL SPS release |
| --- | --- | --- |
| 0,0 | 1 | 1 or 5 or 9 or 13 or 17 or 21 or 25 or 29 |
| 0,1 | 2 | 2 or 6 or 10 or 14 or 18 or 22 or 26 or 30 |
| 1,0 | 3 | 3 or 7 or 11 or 15 or 19 or 23 or 27 or 31 |
| 1,1 | 4 | 0 or 4 or 8 or 12 or 16 or 20 or 24 or 28 or 32 |

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = cc or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = cc and if the UE transmits HARQ-ACK using PUCCH format 4 or PUCCH format 5 in subframe/slot/subslot n, the UE shall determine the  according to the pseudo-code in Clause 5.2.3.1 for subframe-PUCCH transmission and Clause 5.2.3.1A for slot/subslot-PUCCH transmission in [4].

For a UE configured with higher layer parameter codebooksizeDetermination-r13 = cc or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = cc, if the UE transmits HARQ-ACK on PUSCH in a subframe/slot/subslot, the UE shall determine the  according to the pseudo-code in Clause 5.2.2.6 in [4].

For a BL/CE UE with higher layer parameter ce-PDSCH-14HARQ-Config not configured, for PDSCH transmission in subframe n-k-Koffset, if the UE is in half-duplex FDD operation and is configured with CEModeA and higher layer parameter ce-HARQ-AckBundling and the 'HARQ-ACK bundling flag' in the corresponding DCI is set to 1, or if the UE is configured with higher layer parameter ce-SchedulingEnhancement,

- if the 'HARQ-ACK delay' field in the corresponding DCI indicates value k, the UE shall determine the subframe n as the HARQ-ACK transmission subframe.

- the HARQ-ACK delay value k is determined from the corresponding DCI based on the higher layer parameters according to Table 7.3.1-2.

For a BL/CE UE with higher layer parameter ce-PDSCH-14HARQ-Config configured, for PDSCH transmission in subframe n-k-Koffset, if the UE is in half-duplex FDD operation and is configured with CEModeA, and 'PDSCH scheduling delay and HARQ-ACK delay for 14 HARQ' field is present in the corresponding DCI,

- if the HARQ-ACK delay value as defined in [4], in the corresponding DCI indicates value k, the UE shall determine the subframe n as the HARQ-ACK transmission subframe.

For a BL/CE UE in half-duplex FDD operation, if the UE is configured with CEModeA, and if the UE is configured with higher layer parameter ce-HARQ-AckBundling and the 'HARQ-ACK bundling flag' in the corresponding DCI is set to 1,

- for HARQ-ACK transmission in subframe n, the UE shall generate one HARQ-ACK bit by performing a logical AND operation of HARQ-ACKs across all  BL/CE DL subframes for which subframe n is the 'HARQ-ACK transmission subframe'.

- if subframe n-k1-Koffset is the most recent subframe for which subframe n is the 'HARQ-ACK transmission subframe', and if the 'Transport blocks in a bundle' field in the corresponding DCI for PDSCH transmission in subframe n-k1-Koffset indicates a number of transport blocks in a bundle other than , the UE shall generate a NACK for HARQ-ACK transmission in subframe n.

- if the UE has received W PDSCH transmissions before subframe n, and if the UE is expected to transmit HARQ-ACK for the W PDSCH transmissions in subframes , the UE is not expected to receive a new PDSCH transmission in subframe n for which the corresponding HARQ-ACK shall be provided, where W is minimum number of W’ and the total HARQ processes number with enabled HARQ-ACK information, and W’=10 if higher layer parameter ce-pdsch-tenProcesses-config is set to 'On', W’=12 if higher layer parameter ce-PDSCH-14HARQ-Config is configured, and W’=8 otherwise.

- if the UE is expected to transmit HARQ-ACK for the PDSCH transmissions received before subframe n in subframes , the UE is not expected to receive a new PDSCH transmission in subframe n for which the HARQ-ACK is to be transmitted in subframe

Table 7.3.1-2: HARQ-ACK delay for BL/CE UE in CEModeA

| 'HARQ-ACK delay' field in DCI | HARQ-ACK delay value when 'ce-SchedulingEnhancement' set to 'range1' | HARQ-ACK delay value when 'ce-SchedulingEnhancement' set to 'range2', or 'ce-SchedulingEnhancement' is not configured and 'ce-HARQ-AckBundling' is set |
| --- | --- | --- |
| 000 | 4 | 4 |
| 001 | 5 | 5 |
| 010 | 7 | 6 |
| 011 | 9 | 7 |
| 100 | 11 | 8 |
| 101 | 13 | 9 |
| 110 | 15 | 10 |
| 111 | 17 | 11 |

### 7.3.2 TDD HARQ-ACK reporting procedure

For TDD and a UE not configured with the parameter EIMTA-MainConfigServCell-r12 for any serving cell, if the UE is configured with one serving cell, or if the UE is configured with more than one serving cell and the TDD UL/DL configuration of all the configured serving cells is the same, UE procedure for reporting HARQ-ACK is given in Clause 7.3.2.1.

For TDD, if a UE is configured with more than one serving cell and the TDD UL/DL configuration of at least two configured serving cells is not the same, or if the UE is configured with the parameter EIMTA-MainConfigServCell-r12 for at least one serving cell, UE procedure for reporting HARQ-ACK is given in Clause 7.3.2.2.

When only a positive SR is transmitted, a UE shall use subframe-PUCCH Format 1 for the SR resource as defined in Clause 5.4.1 in [3].

When only a positive SR is transmitted using slot-PUCCH, a UE shall use PUCCH Format 1 for the first SR resource configured by higher layers as defined in Clause 5.4A.2 in [3].

#### 7.3.2.1 TDD HARQ-ACK reporting procedure for same UL/DL configuration

Unless otherwise stated, the procedure in this clause applies to non-BL/CE UEs.

For TDD, the UE shall upon detection of a PDSCH transmission or a PDCCH/EPDCCH/SPDCCH indicating downlink SPS release (defined in Clause 9.2) within subframe/slot(s) , where , intended for the UE and for which HARQ-ACK response shall be provided, transmit the HARQ-ACK response in UL subframe/slot n and  is defined in

- Table 10.1.3.1-1E if the UE is configured with higher layer parameter shortTTI for slot-PDSCH and special subframe configuration 0, 5, 9, and 10,

- Table 10.1.3.1-1D if the UE is configured with higher layer parameter shortTTI for special subframe configuration 3, 4, and 8,

- Table 10.1.3.1-1C if the UE is configured with higher layer parameter shortTTI for slot-PDSCH and special subframe configuration 1, 2, 6, 7,

- Table 10.1.3.1-1B if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space for subframe-based PDSCH and

- Table 10.1.3.1-1 otherwise.

For TDD, when PUCCH format 3/4/5 is configured for transmission of HARQ-ACK,

- for special subframe configurations 0, 5 and 10 if configured by ssp10-CRS-LessDwPTS with normal downlink CP or configurations 0 and 4 with extended downlink CP in a serving cell, shown in table 4.2-1 [3], the special subframe of the serving cell is excluded from the HARQ-ACK codebook size determination. In this case, if the serving cell is the primary cell, there is no PDCCH/EPDCCH indicating downlink SPS release in the special subframe.

- for special subframe configurations 1, 2, 6, and 7 and slot-PDSCH, the second slot of DwPTS of the serving cell is excluded from the HARQ-ACK codebook size determination. In this case, if the serving cell is the primary cell, there is no PDCCH/SPDCCH indicating downlink SPS release in the second slot of DwPTS.

For TDD UL/DL configurations 1-6 and one configured serving cell, if the UE is not configured with PUCCH format 3, the value of the Downlink Assignment Index (DAI) in DCI format 0/4/7-0A/7-0B, , detected by the UE according to Table 7.3-X in subframe/slot , where  is defined in

- Table 7.3-Y4 if the UE is configured with higher layer parameter shortTTI and for special subframe configuration 3, 4, 8 for slot-PDSCH,

- Table 7.3-Y3 if the UE is configured with higher layer parameter shortTTI and for special subframe configuration 0, 5, 9, 10 for slot-PDSCH,

- Table 7.3-Y2 if the UE is configured with higher layer parameter shortTTI and for special subframe configuration 1,2,6,7 for slot-PDSCH,

- Table 7.3-Y1 if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space for subframe-PDSCH,

- Table 7.3-Y otherwise,

represents the total number of subframes/slots with PDSCH transmissions and with PDCCH/EPDCCH/SPDCCH indicating downlink SPS release to the corresponding UE within all the subframe(s)/slot(s) , where. The value  includes all PDSCH transmission with and without corresponding PDCCH/EPDCCH/SPDCCH within all the subframe(s)/slot(s) . In case neither PDSCH transmission, nor PDCCH/EPDCCH/SPDCCH indicating the downlink SPS resource release is intended to the UE, the UE can expect that the value of the DAI in DCI format 0/4/7-0A/7-0B, , if transmitted, is set to 4.

For TDD UL/DL configuration 1-6 and a UE configured with more than one serving cell, or for TDD UL/DL configuration 1and a UE configured with one serving cell and PUCCH format 3, a value is determined by the Downlink Assignment Index (DAI) in DCI format 0/4/7-0A/7-0B according to Table 7.3-Z in subframe/slot , where  is defined in

- Table 7.3-Y4 if the UE is configured with higher layer parameter shortTTI and for special subframe configuration 3, 4, 8 for slot-PDSCH,

- Table 7.3-Y3 if the UE is configured with higher layer parameter shortTTI and for special subframe configuration 0, 5, 9, 10 for slot-PDSCH,

- Table 7.3-Y2 if the UE is configured with higher layer parameter shortTTI and for special subframe configuration 1, 2, 6, 7 for slot-PDSCH,

- Table 7.3-Y1 if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space for subframe-PDSCH,

- Table 7.3-Y otherwise.

In case neither PDSCH transmission, nor PDCCH/EPDCCH/SPDCCH indicating the downlink SPS resource release is intended to the UE, the UE can expect that the value of  is set to 4 by the DAI in DCI format 0/4/7-0A/7-0B if transmitted.

If a UE is not configured with higher layer parameter shortTTI and not configured with higher layer parameter codebooksizeDetermination-r13 = dai or is configured with higher layer parameter shortTTI and not configured with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai, for TDD UL/DL configurations 1-6, the value of the DAI in DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G denotes the accumulative number of PDCCH/EPDCCH/SPDCCH (s) with assigned PDSCH transmission(s) and PDCCH/EPDCCH/SPDCCH indicating downlink SPS release up to the present subframe/slot within subframe(s)/slot(s)  of each configured serving cell, where , and shall be updated from subframe/slot to subframe/slot. Denote  as the value of the DAI in PDCCH/EPDCCH/SPDCCH with DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G detected by the UE according to Table 7.3-X in subframe/slot  in serving cell , where  is the smallest value in the set  (defined in Table10.1.3.1-1D if the UE is configured with higher layer parameter shortTTI and special subframe configuration 3, 4, 8 for slot-PDSCH, in Table 10.1.3.1-1C if the UE is configured with higher layer parameter shortTTI and special subframe configuration 0, 1, 2, 5, 6, 7, 9, 10 for slot-PDSCH, in Table 10.1.3.1-1B if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space for subframe-PDSCH and in Table 10.1.3.1-1 otherwise) such that the UE detects a DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G. When configured with one serving cell, the subscript of  in  can be omitted.

For all TDD UL/DL configurations, denote  as the total number of PDCCH/EPDCCH/SPDCCH (s) with assigned PDSCH transmission(s) and PDCCH/EPDCCH/SPDCCH indicating downlink SPS release detected by the UE within the subframe(s)/slot(s)  in serving cell , where . When configured with one serving cell, the subscript of  in  can be omitted. Denote , which can be zero or one, as the number of PDSCH transmissions without a corresponding PDCCH/EPDCCH/SPDCCH within the subframe(s)/slot(s) , where .

For TDD HARQ-ACK bundling or HARQ-ACK multiplexing and a subframe/slot  with , the UE shall generate one or two HARQ-ACK bits by performing a logical AND operation per codeword across  subframe(s)/slot(s) downlink and special subframes associated with a single UL subframe/slot, of all the corresponding  individual PDSCH transmission HARQ-ACKs and individual ACK in response to received PDCCH/EPDCCH/SPDCCH indicating downlink SPS release, where  is the number of elements in the set  defined in Table10.1.3.1-1D if the UE is configured with higher layer parameter shortTTI and special subframe configuration 3, 4, 8 for slot-PDSCH, in Table 10.1.3.1-1C if the UE is configured with higher layer parameter shortTTI and special subframe configuration 0, 1, 2, 5, 6, 7, 9, 10 for slot-PDSCH, in Table 10.1.3.1-1B if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space for subframe-PDSCH and in Table 10.1.3.1-1 otherwise. The UE shall detect if at least one downlink assignment has been missed, and for the case that the UE is transmitting on PUSCH the UE shall also determine the parameter.

For TDD UL/DL configuration 0,  shall be 1 if the UE detects the PDSCH transmission with or without corresponding PDCCH/EPDCCH/SPDCCH, or detects PDCCH/SPDCCH indicating downlink SPS release within the subframe/slot , where . The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/SPDCCH indicating downlink SPS release within the subframe(s)/slot (s) , where .

For the case that the UE is not transmitting on PUSCH in subframe/slot n and TDD UL/DL configurations 1-6, if  and , the UE detects that at least one downlink assignment has been missed.

For the case that the UE is transmitting on PUSCH and the PUSCH transmission is performed based on a detected PDCCH/EPDCCH/SPDCCH with DCI format 0/4/7-0A/7-0B intended for the UE and TDD UL/DL configurations 1-6, if  the UE detects that at least one downlink assignment has been missed and the UE shall generate NACK for all codewords where  is determined by the UE as . If the UE does not detect any downlink assignment missing,  is determined by the UE as . UE shall not transmit HARQ-ACK if and .

For the case that the UE is transmitting on PUSCH, and the PUSCH transmission is not based on a detected PDCCH/EPDCCH/SPDCCH with DCI format 0/4/7-0A/7-0B intended for the UE and TDD UL/DL configurations 1-6, if  and , the UE detects that at least one downlink assignment has been missed and the UE shall generate NACK for all codewords. The UE determines  as the number of assigned subframes/slots. The UE shall not transmit HARQ-ACK if .

For TDD, when PUCCH format 3 is configured for transmission of HARQ-ACK without PUCCH format 4 or PUCCH format 5 configured for transmission of HARQ-ACK, the HARQ-ACK feedback bits  for the c-th serving cell configured by RRC are constructed as follows, where c≥0,  if transmission mode configured in the c-th serving cell supports one transport block or spatial HARQ-ACK bundling is applied and otherwise, where is the number of subframes/slots in downlink and special subframes for which the UE needs to feedback HARQ-ACK bits for the c-th serving cell.

- For subframe-PDSCH and the case that the UE is transmitting on PUCCH,  where  is the number of elements in the set  defined in Table 10.1.3.1-1B if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space for subframe-PDSCH and in Table .1-1 otherwise; associated with subframe/slot n and the set  does not include a special subframe of configurations 0,5 and 10 if configured by ssp10-CRS-LessDwPTS with normal downlink CP or of configurations 0 and 4 with extended downlink CP; otherwise .

- For slot-PDSCH, special subframe configuration 0, 1, 2, 5, 6, 7, 9, 10, and the case that the UE is transmitting on PUCCH,  where  is the number of elements in the set  defined in Table 10.1.3.1-1C; associated with slot n and the set  does not include a slot in a special subframe of configurations 0 and 5 with normal downlink CP or of configurations 0 and 4 with extended downlink CP; otherwise .

- For slot-PDSCH, special subframe configuration 3, 4, 8, and the case that the UE is transmitting on PUCCH,  where  is the number of elements in the set  defined in Table 10.1.3.1-1D; associated with slot n and the set  does not include a slot in a special subframe of configurations 0 and 5 with normal downlink CP or of configurations 0 and 4 with extended downlink CP; otherwise .

- For subframe-PDSCH, and TDD UL/DL configuration 0 or for a PUSCH transmission not performed based on a detected PDCCH/EPDCCH with DCI format 0/4, the UE shall assume  where  is the number of elements in the set  defined in Table 10.1.3.1-1B if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space for subframe-PDSCH and in Table 10.1.3.1-1 otherwise; associated with subframe n and the set  does not include a special subframe of configurations 0, 5 and 10 if configured by ssp10-CRS-LessDwPTS with normal downlink CP or of configurations 0 and 4 with extended downlink CP; otherwise . The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH indicating downlink SPS release in subframe(s) , where .

- For slot-PDSCH, special subframe configuration 0, 1, 2, 5, 6, 7, 9, 10, and TDD UL/DL configuration 0 or for a PUSCH transmission not performed based on a detected PDCCH/SPDCCH with DCI format 7-0A/7-0B, the UE shall assume  where  is the number of elements in the set  defined in Table 10.1.3.1-1C associated with slot n and the set  does not include a slot in a special subframe of configurations 0 and 5 with normal downlink CP; otherwise . The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/SPDSCH indicating downlink SPS release in slot(s), where .

- For slot-PDSCH, special subframe configuration 3, 4, 8, and TDD UL/DL configuration 0 or for a PUSCH transmission not performed based on a detected PDCCH/SPDCCH with DCI format 7-0A/7-0B, the UE shall assume  where  is the number of elements in the set  defined in Table 10.1.3.1-1D associated with slot n. The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/ SPDSCH indicating downlink SPS release in slot(s), where .

- For TDD UL/DL configurations {1, 2, 3, 4, 6} and a PUSCH transmission performed based on a detected PDCCH/EPDCCH with DCI format 0/4/7-0A/7-0B, the UE shall assume . The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in subframe(s)/slot(s)  where  and .

- For TDD UL/DL configurations 5 and a PUSCH transmission performed based on a detected PDCCH/EPDCCH/SPDCCH with DCI format 0/4/7-0A/7-0B, the UE shall assume , where denotes the maximum value of  among all the configured serving cells, is the total number of received PDSCHs and PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in subframe(s)/slot(s)   on the c-th serving cell,. The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in subframe(s)/slot(s)  where  and .

For TDD, when PUCCH format 4/5 is configured for transmission of HARQ-ACK and if the UE is configured with higher layer parameter codebooksizeDetermination-r13 = cc or codebooksizeDeterminationsSTTI-r15 = cc, the HARQ-ACK feedback bits  for the c-th serving cell configured by RRC are constructed as follows, where c≥0,  if transmission mode configured in the c-th serving cell supports one transport block or spatial HARQ-ACK bundling is applied or for slot-PDSCH and otherwise, where is the number of subframs/slots in downlink and special subframes for which the UE needs to feedback HARQ-ACK bits for the c-th serving cell.

- For subframe-PDSCH and the case that the UE is transmitting on PUCCH,  where  is the number of elements in the set  defined in Table 10.1.3.1-1B if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space for subframe-PDSCH and in Table .1-1 otherwise; associated with subframe n and the set  does not include a special subframe of configurations 0, 5 and 10 if configured by ssp10-CRS-LessDwPTS with normal downlink CP or of configurations 0 and 4 with extended downlink CP; otherwise .

- For slot-PDSCH, special subframe configuration 0, 1, 2, 5, 6, 7, 9, 10 and the case that the UE is transmitting on PUCCH,  where  is the number of elements in the set  defined in Table .1-1C associated with slot n and the set  does not include a slot in a special subframe of configurations 0 and 5 with normal downlink CP; otherwise .

- For slot-PDSCH, special subframe configuration 3, 4, 8, and the case that the UE is transmitting on PUCCH,  where  is the number of elements in the set  defined in Table .1-1D associated with slot n.

- For subframe-PDSCH and the case that UE is transmitting on PUSCH not performed based on a detected PDCCH/EPDCCH with DCI format 0/4 or on PUSCH adjusted based on an associated detected DCI format 0/4, the UE shall assume  where  is the number of elements in the set  defined in Table 10.1.3.1-1 associated with subframe n and the set  does not include a special subframe of configurations 0, 5 and 10 if configured by ssp10-CRS-LessDwPTS with normal downlink CP or of configurations 0 and 4 with extended downlink CP; otherwise . The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH indicating downlink SPS release in subframe(s), where .

- For slot-PDSCH, special subframe configuration 0, 1, 2, 5, 6, 7, 9, 10, and the case that UE is transmitting on PUSCH not performed based on a detected PDCCH/SPDCCH with DCI format 7-0A/7-0B, the UE shall assume  where  is the number of elements in the set  defined in Table 10.1.3.1-1C associated with slot n and the set  does not include a slot in a special subframe of configurations 0 and 5 with normal downlink CP; otherwise . The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/ SPDCCH indicating downlink SPS release in slot(s), where .

- For slot-PDSCH, special subframe configuration 3, 4, 8, and the case that UE is transmitting on PUSCH not performed based on a detected PDCCH/SPDCCH with DCI format 7-0A/7-0B, the UE shall assume  where  is the number of elements in the set  defined in Table 10.1.3.1-1D associated with slot n. The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/SPDCCH indicating downlink SPS release in slot(s), where .

For TDD, when PUCCH format 3/4/5 is configured for transmission of HARQ-ACK and if the UE is not configured with higher layer parameter codebooksizeDetermination-r13 = dai for subframe-PDSCH or codebooksizeDeterminationsSTTI-r15 = dai for slot-PDSCH,

for TDD UL/DL configurations 1-6, the HARQ-ACK for a PDSCH transmission with a corresponding PDCCH/EPDCCH/SPDCCH or for a PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in subframe/slot  is associated with  if transmission mode configured in the c-th serving cell supports one transport block or spatial HARQ-ACK bundling is applied or for slot-PDSCH, or associated with  and  otherwise, where DAI(k) is the value of DAI in DCI format /1B/1D/A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G detected in subframe/slot ,  and  are the HARQ-ACK feedback for codeword 0 and codeword 1, respectively. For the case with , the HARQ-ACK associated with a PDSCH transmission without a corresponding PDCCH/EPDCCH/SPDCCH is mapped to  The HARQ-ACK feedback bits without any detected PDSCH transmission or without detected PDCCH/EPDCCH/SPDCCH indicating downlink SPS release are set to NACK;

- for TDD UL/DL configuration 0, the HARQ-ACK for a PDSCH transmission or for a PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in subframe/slot  is associated with  if transmission mode configured in the c-th serving cell supports one transport block or associated with  and  otherwise, where  and  are the HARQ-ACK feedback for codeword 0 and codeword 1, respectively. The HARQ-ACK feedback bits without any detected PDSCH transmission or without detected PDCCH/EPDCCH/SPDCCH indicating downlink SPS release are set to NACK.

For TDD when format 1b with channel selection is configured for transmission of HARQ-ACK and for 2 configured serving cells, the HARQ-ACK feedback bits on PUSCH are constructed as follows.

- For TDD UL/DL configuration 0, = HARQ-ACK(j),  as defined in Clause .2.1. The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH indicating downlink SPS release in subframe(s) where .

- For TDD UL/DL configurations {1, 2, 3, 4, 6} and a PUSCH transmission performed based on a detected PDCCH/EPDCCH with DCI format 0/4 with =1 or 2,  is determined as if PUCCH format 3 is configured for transmission of HARQ-ACK, except that spatial HARQ-ACK bundling across multiple codewords within a downlink or special subframe is performed for all serving cells configured with a downlink transmission mode that supports up to two transport blocks in case =2.

- For TDD UL/DL configurations {1, 2, 3, 4, 6} and a PUSCH transmission performed based on a detected PDCCH/EPDCCH with DCI format 0/4 with =3 or 4, , as defined in Table .2-5 or in Table 10.1.3.2-6 respectively, where the value of is replaced by . The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH indicating downlink SPS release in subframe(s) where  and .

- For TDD UL/DL configurations {1, 2, 3, 4, 6} and a PUSCH transmission not performed based on a detected PDCCH/EPDCCH with DCI format 0/4 and a subframe  with =1 or 2, = HARQ-ACK(j),  as defined in Clause .2.1. The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH indicating downlink SPS release in subframe(s) where .

- For TDD UL/DL configurations {1, 2, 3, 4, 6} and a PUSCH transmission not performed based on a detected PDCCH/EPDCCH with DCI format 0/4 and a subframe  with =3 or 4, , as defined in Table .2-5 or in Table 10.1.3.2-6 respectively. The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH indicating downlink SPS release in subframe(s) where .

For TDD HARQ-ACK bundling, when the UE is configured by transmission mode 3, 4, 8, 9 or 10 defined in Clause 7.1 and HARQ-ACK bits corresponding to a subframe-PDSCH are transmitted on PUSCH, the UE shall always generate 2 HARQ-ACK bits assuming both codeword 0 and 1 are enabled. For the case that the UE detects only the PDSCH transmission associated with codeword 0 within the bundled subframes, the UE shall generate NACK for codeword 1.

For TDD HARQ-ACK bundling, when HARQ-ACK response corresponds to a slot-PDSCH, the UE shall always generate 1 HARQ-ACK bit.

Table 7.3-X: Value of Downlink Assignment Index

| DAI MSB, LSB | or | Number of subframes/slots with PDSCH transmission and with PDCCH/EPDC/SPDCCH CH indicating DL SPS release |
| --- | --- | --- |
| 0,0 | 1 | 1 or 5 or 9 |
| 0,1 | 2 | 2 or 6 or 10 |
| 1,0 | 3 | 3 or 7 |
| 1,1 | 4 | 0 or 4 or 8 |

Table 7.3-Y: Uplink association index k' for TDD

| TDD UL/DL Configuration | subframe number n |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 1 |  |  | 6 | 4 |  |  |  | 6 | 4 |  |
| 2 |  |  | 4 |  |  |  |  | 4 |  |  |
| 3 |  |  | 4 | 4 | 4 |  |  |  |  |  |
| 4 |  |  | 4 | 4 |  |  |  |  |  |  |
| 5 |  |  | 4 |  |  |  |  |  |  |  |
| 6 |  |  | 7 | 7 | 5 |  |  | 7 | 7 |  |

Table 7.3-Y1: Uplink association index k' for TDD and UE configured with shortProcessingTime

| TDD UL/DL Configuration | subframe number n |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 1 |  |  | 3 | 3 |  |  |  | 3 | 3 |  |
| 2 |  |  | 3 |  |  |  |  | 3 |  |  |
| 3 |  |  | 3 | 3 | 3 |  |  |  |  |  |
| 4 |  |  | 3 | 3 |  |  |  |  |  |  |
| 5 |  |  | 3 |  |  |  |  |  |  |  |
| 6 |  |  | 6 | 4 | 4 |  |  | 6 | 3 |  |

Table 7.3-Y2: Uplink association index k' for TDD with special subframe configuration 1, 2, 6, 7 and UE configured with ul-TTI-Length

| TDD UL/DL Configuration | slot number n |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| 1 |  |  |  |  | 4 | 4 | 4 |  |  |  |  |  |  |  | 4 | 4 | 4 |  |  |  |
| 2 |  |  |  |  | 4 | 4 |  |  |  |  |  |  |  |  | 4 | 4 |  |  |  |  |
| 3 |  |  |  |  | 6 | 6 | 6 | 6 | 6 | 6 |  |  |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  | 4 | 4 | 4 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 |  |  |  |  | 4 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 |  |  |  |  | 6 | 6 | 6 | 6 | 6 |  |  |  |  |  | 4 | 4 | 4 |  |  |  |

Table 7.3-Y3: Uplink association index k' for TDD with special subframe configuration 0, 5, 9, 10 and UE configured with ul-TTI-Length

| TDD UL/DL Configuration | slot number n |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| 1 |  |  |  |  | 5 | 5 | 5 | 5 |  |  |  |  |  |  | 5 | 5 | 5 | 5 |  |  |
| 2 |  |  |  |  | 4 | 4 |  |  |  |  |  |  |  |  | 4 | 4 |  |  |  |  |
| 3 |  |  |  |  | 7 | 7 | 7 | 7 | 7 | 7 |  |  |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  | 5 | 5 | 5 | 5 |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 |  |  |  |  | 4 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 |  |  |  |  | 4 |  | 5 |  | 6 |  |  |  |  |  | 4 | 4 | 4 |  |  |  |

Table 7.3-Y4: Uplink association index k' for TDD with special subframe configuration 3, 4, 8 and UE configured with ul-TTI-Length

| TDD UL/DL Configuration | slot number n |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| 1 |  |  |  |  | 4 | 4 | 4 | 4 |  |  |  |  |  |  | 4 | 4 | 4 | 4 |  |  |
| 2 |  |  |  |  | 4 | 4 |  |  |  |  |  |  |  |  | 4 | 4 |  |  |  |  |
| 3 |  |  |  |  | 6 | 6 | 6 | 6 | 6 | 6 |  |  |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  | 4 | 4 | 4 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 |  |  |  |  | 4 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 |  |  |  |  | 6 | 6 | 6 | 6 | 6 | 6 |  |  |  |  | 4 | 4 | 4 | 4 |  |  |

Table 7.3-Z: Value of  determined by the DAI field in DCI format 0/4/7-0A/7-0B

| DAI MSB, LSB |  |
| --- | --- |
| 0,0 | 1 |
| 0,1 | 2 |
| 1,0 | 3 |
| 1,1 | 4 |

For subframe-PUSCH and TDD HARQ-ACK multiplexing and a subframe  with , spatial HARQ-ACK bundling across multiple codewords within a downlink or special subframe is performed by a logical AND operation of all the corresponding individual HARQ-ACKs. In case the UE is transmitting on PUSCH, the UE shall determine the number of HARQ-ACK feedback bits  and the HARQ-ACK feedback bits  ,  to be transmitted in subframe n.

If the PUSCH transmission is performed based on a detected PDCCH/EPDCCH with DCI format 0/4 intended for the UE, then  unless  and  in which case the UE shall not transmit HARQ-ACK. The spatially bundled HARQ-ACK for a PDSCH transmission with a corresponding PDCCH/EPDCCH or for a PDCCH/EPDCCH indicating downlink SPS release in subframe  is associated with  where DAI(k) is the value of DAI in DCI format 1A/1B/1D/1/2/2A/2B/2C/2D detected in subframe . For the case with , the HARQ-ACK associated with a PDSCH transmission without a corresponding PDCCH/EPDCCH is mapped to . The HARQ-ACK feedback bits without any detected PDSCH transmission or without detected PDCCH/EPDCCH indicating downlink SPS release are set to NACK.

If the PUSCH transmission is not performed based on a detected PDCCH/EPDCCH with DCI format 0/4 intended for the UE, , and  is associated with the spatially bundled HARQ-ACK for downlink or special subframe , where. The HARQ-ACK feedback bits without any detected PDSCH transmission or without detected PDCCH/EPDCCH indicating downlink SPS release are set to NACK. The UE shall not transmit HARQ-ACK if .

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = dai and PDSCH is associated with DCI format 1/1A/1B/1D/2/2A/2B/2C/2D, the following HARQ-ACK reporting procedure applies to subframe-PDSCH operation. If a UE is configured with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai and PDSCH is associated with DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G, the following HARQ-ACK reporting procedure applies to slot-PDSCH operation.

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = dai or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai, the value of the counter Downlink Assignment Indicator (DAI) in DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G denotes the accumulative number of {serving cell, subframe/slot}-pair(s) in which PDSCH transmission(s) associated with PDCCH/EPDCCH/SPDCCH or PDCCH/EPDCCH/SPDCCH indicating downlink SPS release is present, up to the present serving cell and present subframe/slot, first in increasing order of serving cell index and then in increasing order of subframe/slot index within subframe(s)/slot(s)  where ; the value of the total DAI in DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G denotes the total number of {serving cell, subframe/slot }-pair(s) in which PDSCH transmission(s) associated with PDCCH/EPDCCH/SPDCCH(s) or PDCCH/EPDCCH/SPDCCH indicating downlink SPS release is present, up to the present subframe/slot within subframe/slot (s)  where , and shall be updated from subframe/slot to subframe/slot. Denote  as the value of the counter DAI in DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G scheduling PDSCH transmission or indicating downlink SPS release for serving cell c in subframe/slot  where  according to table 7.3.2.1-1. Denote as the value of the total DAI in subframe/slot  where , according to Table 7.3.2.1-1. The UE shall assume a same value of total DAI in all PDCCH/EPDCCH/SPDCCH scheduling PDSCH transmission(s) and PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in a subframe/slot.

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = dai or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai and if the UE transmits HARQ-ACK using PUCCH format 3 or PUCCH format 4 or PUCCH format 5 in subframe/slot n, the UE shall determine the  according to the following pseudo-code:

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell

Set m = 0 – subframe/slot index: lower index corresponds to earlier subframe within subframe(s)/slot(s)  where

Set j = 0

Set

Set

Set

Set  to the number of cells configured by higher layers for the UE

Set M to the number of subframes/slots within subframe(s)/slot(s)  where

while m < M

while c <

if there is a PDSCH on serving cell c in subframe/slot m associated with PDCCH/EPDCCH/SPDCCH or there is a PDCCH/EPDCCH/SPDCCH indicating downlink SPS release on serving cell c in subframe/slot m for which HARQ-ACK is transmitted in subframe/slot n,

if

j = j+1

end if

if

else

end if

if the higher layer parameter spatialBundlingPUCCH is set FALSE and the UE is configured with a transmission mode supporting two transport blocks in at least one configured serving cell,

= HARQ-ACK bit corresponding to the first codeword of this cell

= HARQ-ACK bit corresponding to the second codeword of this cell

elseif the higher layer parameter spatialBundlingPUCCH is set TRUE and the UE is configured with a transmission mode supporting two transport blocks in at least one configured serving cell,

= binary AND operation of the HARQ-ACK bits corresponding to the first and second codewords of this cell

else

= HARQ-ACK bit of this cell

end if

c = c + 1

end while

m = m + 1

end while

if

j = j+1

end if

if the higher layer parameter spatialBundlingPUCCH is set FALSE and the UE is configured with a transmission mode supporting two transport blocks in at least one configured serving cell,

else

for any

if SPS PDSCH transmission is activated for a UE and the UE is configured to receive SPS PDSCH in a subframe/slot  where

= HARQ-ACK bit associated with the SPS PDSCH transmission

end if

For a UE configured with higher layer parameter codebooksizeDetermination-r13 = dai or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai, if the UE transmits HARQ-ACK on PUSCH in a subframe/slot, the UE shall determine the  according to the above procedure as if the UE transmits HARQ-ACK using PUCCH format 3 or PUCCH format 4 or PUCCH format 5, except that the higher layer parameter spatialBundlingPUCCH is replaced by spatialBundlingPUSCH.

Table 7.3.2.1-1: Value of counter DAI and total DAI

| DAI MSB, LSB | or | Number of {serving cell, subframe/slot }-pair(s) in which PDSCH transmission(s) associated with PDCCH/EPDCCH/SPDCCH or PDCCH/EPDCCH/SPDCCH indicating downlink SPS release is present, denoted as and |
| --- | --- | --- |
| 0,0 | 1 |  |
| 0,1 | 2 |  |
| 1,0 | 3 |  |
| 1,1 | 4 |  |

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = cc or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = cc and if the UE transmits HARQ-ACK using slot-PUCCH format 3 or PUCCH format 4 or PUCCH format 5 in subframe/slot n, the UE shall determine the  according to the pseudo-code in Clause 5.2.3.1 for subframe-PUCCH transmission and Clause 5.2.3.1A for slot-PUCCH transmission in [4].

For a UE configured with higher layer parameter codebooksizeDetermination-r13 = cc or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = cc, if the UE transmits HARQ-ACK on PUSCH in a subframe/slot, the UE shall determine the  according to the pseudo-code in Clause 5.2.2.6 in [4].

For TDD when a PUCCH format 3 or a PUCCH format 4/5 configured with higher layer parameter codebooksizeDetermination-r13 =cc or codebooksizeDeterminationsSTTI-r15 = cc transmission of HARQ-ACK coincides with a subframe/slot configured to the UE by higher layers for transmission of a scheduling request, the UE shall multiplex HARQ-ACK and SR bits on HARQ-ACK PUCCH resource as defined in Clause 5.2.3.1 for subframe-PUCCH transmission and Clause 5.2.3.1A for slot-PUCCH transmission in [4], unless the HARQ-ACK corresponds to one of the following cases except for the UE configured with EN-DC and tdm-PatternConfig2,

- for subframe-PDSCH, a single PDSCH transmission only on the primary cell indicated by the detection of a corresponding PDCCH/EPDCCH in subframe , where , and for TDD UL/DL configurations 1-6 the DAI value in the PDCCH/EPDCCH is equal to '1' (defined in Table 7.3-X), or a PDCCH/EPDCCH indicating downlink SPS release (defined in Clause 9.2) in subframe , where , and for TDD UL/DL configurations 1-6 the DAI value in the PDCCH/EPDCCH is equal to '1', or

- for subframe-PDSCH, a single PDSCH transmission only on the primary cell where there is not a corresponding PDCCH/EPDCCH detected within subframe(s) , where  and no PDCCH/EPDCCH indicating downlink SPS release (defined in Clause 9.2) within subframe(s) , where , or

- for subframe-PDSCH, a PDSCH transmission only on the primary cell where there is not a corresponding PDCCH/EPDCCH detected within subframe(s) , where and an additional PDSCH transmission only on the primary cell indicated by the detection of a corresponding PDCCH/EPDCCH in subframe , where  with the DAI value in the PDCCH/EPDCCH equal to '1' (defined in Table 7.3-X) or a PDCCH/EPDCCH indicating downlink SPS release (defined in Clause 9.2) in the subframe , where  with the DAI value in the PDCCH/EPDCCH equal to '1',

in which case the UE shall transmit the HARQ-ACK and scheduling request according to the procedure for PUCCH format 1b with channel selection in TDD.

For TDD when a PUCCH format 4/5 configured with higher layer parameter codebooksizeDetermination-r13 = dai or codebooksizeDeterminationsSTTI-r15 = dai transmission of HARQ-ACK coincides with a subframe/slot configured to the UE by higher layers for transmission of a scheduling request, the UE shall multiplex HARQ-ACK and SR bits on HARQ-ACK PUCCH resource as defined in Clause 5.2.3.1 and Clause 5.2.3.1A for slot-PUCCH transmission in [4], unless the HARQ-ACK corresponds to one of the following cases

- for subframe-PDSCH, a single PDSCH transmission only on the primary cell indicated by the detection of a corresponding PDCCH/EPDCCH in subframe , where , and both the counter DAI value and the total DAI value in the PDCCH/EPDCCH is equal to '1' (defined in Table 7.3.2.1-1), or a single PDCCH/EPDCCH indicating downlink SPS release (defined in Clause 9.2) in subframe , where , and both the counter DAI value and the total DAI value in the PDCCH/EPDCCH is equal to '1' (defined in Table 7.3.2.1-1), or

- for subframe-PDSCH, a single PDSCH transmission only on the primary cell where there is not a corresponding PDCCH/EPDCCH detected within subframe(s) , where  and no PDCCH/EPDCCH indicating downlink SPS release (defined in Clause 9.2) within subframe(s) , where , or

- for subframe-PDSCH, a PDSCH transmission only on the primary cell where there is not a corresponding PDCCH/EPDCCH detected within subframe(s) , where and an additional PDSCH transmission only on the primary cell indicated by the detection of a corresponding PDCCH/EPDCCH in subframe , where  with both the counter DAI value and the total DAI value in the PDCCH/EPDCCH is equal to '1' (defined in Table 7.3.2.1-1) or an additional PDCCH/EPDCCH indicating downlink SPS release (defined in Clause 9.2) in the subframe , where  with both the counter DAI value and the total DAI value in the PDCCH/EPDCCH is equal to '1' (defined in Table 7.3.2.1-1),

in which case the UE shall transmit the HARQ-ACK and scheduling request according to the procedure for PUCCH format 1b with channel selection in TDD.

For TDD when the UE is configured with HARQ-ACK bundling, HARQ-ACK multiplexing or PUCCH format 1b with channel selection, and when both HARQ-ACK and SR are transmitted in the same subframe/slot, a UE shall transmit the bundled HARQ-ACK or the multiple HARQ-ACK responses (according to Clause 10.1) on its assigned HARQ-ACK PUCCH resources for a negative SR transmission. For a positive SR, the UE shall transmit  on its assigned SR PUCCH resource using PUCCH format 1b according to Clause 5.4.1 for subframe-PDSCH and Clause 5.4A.2 for slot-PDSCH in [3]. For subframe-PDSCH, the value of  are generated according to Table 7.3-1 from the  HARQ-ACK responses including ACK in response to PDCCH/EPDCCH indicating downlink SPS release by spatial HARQ-ACK bundling across multiple codewords within each PDSCH transmission for all serving cells . For slot-PDSCH, the value of  are generated according to Table 7.3-1 from the  HARQ-ACK responses including ACK in response to SPDCCH indicating downlink SPS release. For TDD UL/DL configurations 1-6, if  and  for a serving cell c, the UE detects that at least one downlink assignment has been missed.

Table 7.3-1: Mapping between multiple HARQ-ACK responses and

| Number of ACK among multiple () HARQ-ACK responses |  |
| --- | --- |
| 0 or None (UE detect at least one DL assignment is missed) | 0, 0 |
| 1 | 1, 1 |
| 2 | 1, 0 |
| 3 | 0, 1 |
| 4 | 1, 1 |
| 5 | 1, 0 |
| 6 | 0, 1 |
| 7 | 1, 1 |
| 8 | 1, 0 |
| 9 | 0, 1 |

For TDD if the parameter simultaneousAckNackAndCQI provided by higher layers is set TRUE, and if the UE is configured with HARQ-ACK bundling, HARQ-ACK multiplexing or PUCCH format 1b with channel selection, and if the UE receives PDSCH and/or PDCCH/EPDCCH indicating downlink SPS release only on the primary cell within subframe(s) , where , a UE shall transmit the CSI and  using PUCCH format 2b for normal CP or PUCCH format 2 for extended CP, according to Clause 5.2.3.4 in [4] with  replaced by . The value of  are generated according to Table 7.3-1 from the  HARQ-ACK responses including ACK in response to PDCCH/EPDCCH indicating downlink SPS release by spatial HARQ-ACK bundling across multiple codewords within each PDSCH transmission for all serving cells . For TDD UL/DL configurations 1-6, if  and  for a serving cell c, the UE detects that at least one downlink assignment has been missed.

For TDD if the parameter simultaneousAckNackAndCQI provided by higher layers is set TRUE, and if the UE is configured with PUCCH format 1b with channel selection and receives at least one PDSCH on the secondary cell within subframe(s) , where , the UE shall drop the CSI and transmit HARQ-ACK according to Clause .

For TDD and a UE is configured with PUCCH format 3, except for the UE configured with EN-DC and tdm-PatternConfig2,

if the parameter simultaneousAckNackAndCQI is set TRUE and if the UE receives,

- a single PDSCH transmission only on the primary cell indicated by the detection of a corresponding PDCCH/EPDCCH in subframe , where , and for TDD UL/DL configurations 1-6 the DAI value in the PDCCH/EPDCCH is equal to '1' (defined in Table 7.3-X), or a PDCCH/EPDCCH indicating downlink SPS release (defined in Clause 9.2) in subframe , where , and for TDD UL/DL configurations 1-6 the DAI value in the PDCCH/EPDCCH is equal to '1', or

- a single PDSCH transmission only on the primary cell where there is not a corresponding PDCCH/EPDCCH detected within subframe(s) , where  and no PDCCH/EPDCCH indicating downlink SPS release (defined in Clause 9.2) within subframe(s) , where ,

then the UE shall transmit the CSI and HARQ-ACK using PUCCH format 2//2b according to Clause .4 in [4];

else if

- the parameter simultaneousAckNackAndCQI-Format3-r11 is set TRUE and if PUCCH format 3 resource is determined according to Clause 10.1.3.1 or Clause 10.1.3.2.2 and

- if the total number of bits in the subframe corresponding to HARQ-ACKs, SR (if any), and the CSI is not larger than 22, or

- if the total number of bits in the subframe corresponding to spatially bundled HARQ-ACKs, SR (if any), and the CSI is not larger than 22

then the UE shall transmit the HARQ-ACKs, SR (if any) and the CSI using the determined PUCCH format 3 resource according to [4];

else,

- the UE shall drop the CSI and transmit the HARQ-ACK according to Clause .

For TDD and a UE configured with PUCCH format 4 or PUCCH format 5, and if the UE has HARQ-ACK/SR and periodic CSI reports to transmit in a subframe,

if a PUCCH format 3 is determined to transmit the HARQ-ACK/SR according to Clause 10.1.3.2.3 or 10.1.3.2.4, the UE shall use the determined PUCCH format 3 for transmission of the HARQ-ACK/SR and periodic CSI report(s) if the parameter simultaneousAckNackAndCQI-Format3-r11 provided by higher layers is set TRUE; otherwise, the UE shall drop the periodic CSI report(s) and transmit only HARQ-ACK/SR;

if a PUCCH format 4 is determined to transmit the HARQ-ACK/SR according to Clause 10.1.3.2.3 or a PUCCH format 5 is determined to transmit the HARQ-ACK/SR according to 10.1.3.2.4, the UE shall use the determined PUCCH format 4 or PUCCH format 5 for transmission of the HARQ-ACK/SR and periodic CSI report(s) if the parameter simultaneousAckNackAndCQI-Format4-Format5-r13 provided by higher layers is set TRUE; otherwise, the UE shall drop the periodic CSI report(s) and transmit only HARQ-ACK/SR;

if there is no PUCCH format 3 or 4 determined to transmit the HARQ-ACK/SR according to Clause 10.1.3.2.3 and there is no PUCCH format 3 or 5 determined to transmit the HARQ-ACK/SR according to Clause 10.1.3.2.4 and there are more than one periodic CSI report(s) in the subframe,

if the parameter simultaneousAckNackAndCQI-Format4-Format5-r13 provided by higher layers is set TRUE and if the UE is configured with a single PUCCH format 4 resource  according to higher layer parameter format4-MultiCSI-resourceConfiguration, the PUCCH format 4 resource  is used for transmission of the HARQ-ACK/SR and periodic CSI report(s);

if the parameter simultaneousAckNackAndCQI-Format4-Format5-r13 provided by higher layers is set TRUE and if the UE is configured with a PUCCH format 5 resource according to higher layer parameter format5-MultiCSI-resourceConfiguration, the PUCCH format 5 resource is used for transmission of the HARQ-ACK/SR and periodic CSI report(s);

if the parameter simultaneousAckNackAndCQI-Format4-Format5-r13 provided by higher layers is set TRUE and if the UE is configured with two PUCCH format 4 resources  and according to higher layer parameter format4-MultiCSI-resourceConfiguration, if , the PUCCH format 4 resource with the smaller  between  and  is used for transmission of the HARQ-ACK/SR and periodic CSI report(s); otherwise, the PUCCH format 4 resource with the larger  between  and  is used for transmission of the HARQ-ACK/SR periodic CSI report(s), where

is the total number of HARQ-ACK bits in the subframe;

if there is no scheduling request bit in the subframe and  otherwise

is the total number of CSI report bits in the subframe;

is the number of CRC bits;

, , is the number of PRBs for  and  respectively, according to higher layer parameter numberOfPRB-format4-r13 according to Table 10.1.1-2;

if shortened PUCCH format 4 is used in the subframe and  otherwise; and

is the code rate given by higher layer parameter maximumPayloadCoderate-r13 according to Table 10.1.1-1.

otherwise, the UE shall drop the periodic CSI reports and transmit only HARQ-ACK/SR.

if there is no PUCCH format 3 or 4 determined to transmit the HARQ-ACK/SR according to Clause 10.1.3.2.3 and there is no PUCCH format 3 or 5 determined to transmit the HARQ-ACK/SR according to Clause 10.1.3.2.4 and there is only one periodic CSI report in the subframe,

if there is no positive SR and the parameter simultaneousAckNackAndCQI is set TRUE and if the UE receives,

a single PDSCH transmission only on the primary cell indicated by the detection of a corresponding PDCCH/EPDCCH in subframe , where , and the counter DAI value in the PDCCH/EPDCCH is equal to '1' (defined in Table 7.3-X), or a PDCCH/EPDCCH indicating downlink SPS release (defined in Clause 9.2) in subframe , where , and the counter DAI value in the PDCCH/EPDCCH is equal to '1', or

a single PDSCH transmission only on the primary cell where there is not a corresponding PDCCH/EPDCCH detected within subframe(s) , where  and no PDCCH/EPDCCH indicating downlink SPS release (defined in Clause 9.2) within subframe(s) , where ,

then the UE shall transmit the CSI and HARQ-ACK using PUCCH format 2//2b according to Clause .4 in [4];

else,

the UE shall drop the CSI and transmit the HARQ-ACK according to Clause 10.1.3.2.3 or 10.1.3.2.4 when UE shall transmit HARQ-ACK only or UE shall drop the CSI and transmit the HARQ-ACK and SR according to the procedure for PUCCH format 1b with channel selection in TDD when there is positive SR.

If a UE transmits HARQ-ACK/SR and periodic CSI report(s) using either a PUCCH format 4  or PUCCH format 5 in a subframe

if , the UE shall transmit the HARQ-ACK/SR and periodic CSI bits using the PUCCH format 4  or the PUCCH format 5  ;

if , the UE shall select  CSI report(s) for transmission together with HARQ-ACK/SR in ascending order of , where ,  and are determined according to Clause 7.2.2; the value of  satisfies  and , and  is the number of CSI report bits for the nth CSI report in ascending order of .

For TDD and a BL/CE UE,

- if the UE is configured with ce-PDSCH-MultiTB-Config, and multiple TBs are scheduled by a single DCI

- the UE is not expected to receive any other PDSCH transmission(s) or MPDCCH indicating downlink SPS release, corresponding to which the UE shall report HARQ-ACK in any subframe(s) in which HARQ-ACKs are reported for the multiple TBs scheduled by the single DCI, according to clause 10.2

- the UE behaviour for HARQ-ACK reporting is the same as that of a BL/CE UE with FDD, except:

- PUCCH resource(s) is (are) determined according to Clause 10.1.3.1; and

- PUCCH(s) is (are) transmitted in a set of BL/CE UL subframe(s) according to Clause 10.2 for TDD and BL/CE UEs;

- else if the UE is configured with csi-NumRepetitionCE equal to 1 and mPDCCH-NumRepetition equal to 1,

- the UE behaviour for HARQ-ACK reporting is the same as that of a non-BL/CE UE with TDD, except:

- PDCCH/EPDCCH is replaced by MPDCCH; and

- DCI format 1/1A/1B/1D/2/2A/2B/2C/2D is replaced by DCI format 6-1A; and

- DCI format 0/4 is replaced by DCI format 6-0A; and

- PUCCH is transmitted in a set of BL/CE UL subframe(s) according to Clause 10.2 for TDD and BL/CE UEs;

- else

- the UE is not expected to receive more than one PDSCH transmission, or more than one of PDSCH and MPDCCH indicating downlink SPS releases, with transmission ending within subframe(s) $ n-k $, where  and  is defined in Table 10.1.3.1-1 intended for the UE;

- The UE behavior for HARQ-ACK reporting is the same as that of a BL/CE UE with FDD, except:

- PUCCH resource is determined according to Clause 10.1.3.1; and

- PUCCH is transmitted in a set of BL/CE UL subframe(s) according to Clause 10.2 for TDD and BL/CE UEs.

If the BL/CE UE is configured in CEModeA, and if the PDSCH is assigned by or semi-statically scheduled by a MPDCCH with DCI format 6-1A, the UE shall assume no PDSCH repetition if the higher layer parameter csi-NumRepetitionCE-r13 indicates one subframe.

#### 7.3.2.2 TDD HARQ-ACK reporting procedure for different UL/DL configurations

For a configured serving cell, the DL-reference UL/DL configuration as defined in Clause 10.2 is referred to as the "DL-reference UL/DL configuration" in the rest of this Clause.

For a configured serving cell, if a UE is not configured with higher layer parameter codebooksizeDetermination-r13 = dai or codebooksizeDeterminationsSTTI-r15 = dai and if the DL-reference UL/DL configuration is 0, then the DAI in DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G is not used.

The UE shall upon detection of a PDSCH transmission or a PDCCH/EPDCCH/SPDCCH indicating downlink SPS release (defined in Clause 9.2) within subframe(s)/slot(s)  for serving cell c, where  intended for the UE and for which HARQ-ACK response shall be provided, transmit the HARQ-ACK response in UL subframe/slot n, wherein set contains values of such that subframe/slot n-k corresponds to a downlink subframe/slot or a special subframe or a slot in a special subframe for serving cell c, where DL subframe or special subframe of serving cell c is according to the higher layer parameter eimta-HARQ-ReferenceConfig-r12 if the UE is configured with the higher layer parameter EIMTA-MainConfigServCell-r12 for serving cell c, or to harq-ReferenceConfig-r14 when the UE is configured with the parameter harq-ReferenceConfig-r14;  is defined in Table 10.1.3.1-1C if the UE is configured with higher layer parameter shortTTI for slot-PDSCH, in Table 10.1.3.1-1B if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space for subframe-PDSCH and in Table 10.1.3.1-1 otherwise (where "UL/DL configuration" in Table 10.1.3.1-1, Table 10.1.3.1-1B, Table 10.1.3.1-1C refers to the DL-reference UL/DL configuration) is associated with subframe/slot n.  is the number of elements in set associated with subframe/slot n for serving cell c.

For the remainder of this Clause .

If the UE is configured with the parameter EIMTA-MainConfigServCell-r12 for the primary cell, "UL/DL configuration of the primary cell" in the rest of this Clause refers to "DL-reference UL/DL configuration of the primary cell".

When PUCCH format 3/4/5 is configured for transmission of HARQ-ACK,

- for special subframe configurations 0 and 5 with normal downlink CP or configurations 0 and 4 with extended downlink CP in a serving cell, shown in table 4.2-1 [3], the special subframe of the serving cell is excluded from the HARQ-ACK codebook size determination. In this case, if the serving cell is the primary cell, there is no PDCCH/EPDCCH indicating downlink SPS release in the special subframe.

- for special subframe configurations 1, 2, 6, and 7 and slot-PDSCH, the second slot of DwPTS of the serving cell is excluded from the HARQ-ACK codebook size determination. In this case, if the serving cell is the primary cell, there is no PDCCH/SPDCCH indicating downlink SPS release in the second slot of DwPTS.

If the UL-reference UL/DL configuration (defined in Sec 8.0) belongs to {1,2,3,4,5,6} for a serving cell, a value is determined by the Downlink Assignment Index (DAI) in DCI format 0/4/7-0A/7-0B corresponding to a PUSCH on the serving cell according to Table 7.3-Z in subframe , where  is defined in Table 7.3-Y2 if the UE is configured with higher layer parameter shortTTI for slot-PDSCH, Table 7.3-Y1 if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space for subframe-PDSCH, Table 7.3-Y otherwise and the "TDD UL/DL Configuration" in Table 7.3-Y/7.3-Y1/7.3-Y2 refers to the UL-reference UL/DL configuration (defined in Clause 8.0) for the serving cell. In case neither PDSCH transmission, nor PDCCH/EPDCCH/SPDCCH indicating the downlink SPS resource release is intended to the UE, the UE can expect that the value of  is set to 4 by the DAI in DCI format 0/4/7-0A/7-0B if transmitted.

If a UE is not configured with higher layer parameter codebooksizeDetermination-r13 = dai or codebooksizeDeterminationsSTTI-r15 = dai and if the DL-reference UL/DL configuration belongs to {1,2,3,4,5,6}, the value of the DAI in DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G denotes the accumulative number of PDCCH/EPDCCH/SPDCCH (s) with assigned PDSCH transmission(s) and PDCCH/EPDCCH/SPDCCH indicating downlink SPS release up to the present subframe/slot within subframe(s)/slot(s)  of each configured serving cell, where , and shall be updated from subframe/slot to subframe/slot. Denote  as the value of the DAI in PDCCH/EPDCCH/SPDCCH with DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G detected by the UE according to Table 7.3-X in subframe/slot in serving cell , where  is the smallest value in the set  such that the UE detects a DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G.

For all TDD UL/DL configurations, denote  as the total number of PDCCH/EPDCCH/SPDCCH (s) with assigned PDSCH transmission(s) and PDCCH/EPDCCH/SPDCCH indicating downlink SPS release detected by the UE within the subframe(s)/slot(s)  in serving cell , where . Denote , which can be zero or one, as the number of PDSCH transmissions without a corresponding PDCCH/EPDCCH/SPDCCH within the subframe(s)/slot(s) , where .

If PUCCH format 3 is configured for transmission of HARQ-ACK without PUCCH format 4/5 configured for transmission of HARQ-ACK, the HARQ-ACK feedback bits  for the c-th serving cell configured by RRC are constructed as follows, where c≥0,  if transmission mode configured in the c-th serving cell supports one transport block or spatial HARQ-ACK bundling is applied and otherwise, where is the number of subframes/slots in downlink and special subframes for which the UE needs to feedback HARQ-ACK bits for the c-th serving cell.

- For the case that the UE is transmitting in subframe/slot n on PUCCH or a PUSCH transmission not performed based on a detected DCI format 0/4/7-0A/7-0B or a PUSCH transmission performed based on an associated detected DCI format 0/4/7-0A/7-0B with UL-reference UL/DL configuration 0 (defined in Sec 8.0), then. The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in subframe(s)/slot(s) , where .

- If DL-reference UL/DL configuration of each of the configured serving cells belongs to {0, 1, 2, 3, 4, 6} and for a PUSCH transmission in a subframe/slot n performed based on a detected PDCCH/EPDCCH/SPDCCH with DCI format 0/4/7-0A/7-0B using UL-reference UL/DL configuration belonging to {1,2,3,4,5,6} (defined in Sec 8.0), the UE shall assume . The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in subframe(s)/slot(s)  where  and .

- If DL-reference UL/DL configuration of at least one configured serving cell belongs to {5} and for a PUSCH transmission performed based on an associated detected PDCCH/EPDCCH/SPDCCH with DCI format 0/4/7-0A/7-0B using UL-reference UL/DL configuration belonging to {1,2,3,4,5,6} (defined in Sec 8.0), the UE shall assume , where denotes the maximum value of  among all the configured serving cells, is the total number of received PDSCHs and PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in subframe(s)/slot(s)  for the c-th serving cell,. The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in subframe(s)/slot(s)  where  and .

If PUCCH format 4/5 is configured for transmission of HARQ-ACK and higher layer parameter codebooksizeDetermination-r13 = dai or codebooksizeDeterminationsSTTI-r15 = dai is not configured, the HARQ-ACK feedback bits  for the c-th serving cell configured by RRC are constructed as follows, where c≥0,  if transmission mode configured in the c-th serving cell supports one transport block or spatial HARQ-ACK bundling is applied and otherwise, where is the number of subframes/slots in downlink and special subframes for which the UE needs to feedback HARQ-ACK bits for the c-th serving cell.

- For the case that the UE is transmitting in subframe/slot n on PUCCH or a PUSCH transmission not performed based on a detected DCI format 0/4/7-0A/7-0B or a PUSCH transmission performed based on an associated detected DCI format 0/4/7-0A/7-0B, then. The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in subframe(s)/slot(s) , where .

When PUCCH format 3/4/5 is configured for transmission of HARQ-ACK and if the UE is not configured with higher layer parameter codebooksizeDetermination-r13 = dai or codebooksizeDeterminationsSTTI-r15 = dai,

if DL-reference UL/DL configuration belongs to {1,2,3,4,5,6}, the HARQ-ACK for a PDSCH transmission with a corresponding PDCCH/EPDCCH/SPDCCH or for a PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in subframe/slot  is associated with  if transmission mode configured in the c-th serving cell supports one transport block or spatial HARQ-ACK bundling is applied, or associated with  and  otherwise, where DAI(k) is the value of DAI in DCI format /1B/1D/A/2B/2C/2D detected in subframe ,  and  are the HARQ-ACK feedback for codeword 0 and codeword 1, respectively. For the case with , the HARQ-ACK associated with a PDSCH transmission without a corresponding PDCCH/EPDCCH/SPDCCH is mapped to  The HARQ-ACK feedback bits without any detected PDSCH transmission or without detected PDCCH/EPDCCH/SPDCCH indicating downlink SPS release are set to NACK;

- if DL-reference UL/DL configuration is 0, the HARQ-ACK for a PDSCH transmission or for a PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in subframe/slot  is associated with  if transmission mode configured in the c-th serving cell supports one transport block or spatial HARQ-ACK bundling is applied, or associated with  and  otherwise, where  and  are the HARQ-ACK feedback for codeword 0 and codeword 1, respectively. The HARQ-ACK feedback bits without any detected PDSCH transmission or without detected PDCCH/EPDCCH/SPDCCH indicating downlink SPS release are set to NACK.

If DL-reference UL/DL configuration of each of the serving cells belongs to {0,1,2,3,4,6} and if PUCCH format 1b with channel selection is configured for transmission of HARQ-ACK and for two configured serving cells, the HARQ-ACK feedback bits on PUSCH are constructed as follows

- if UL-reference UL/DL configuration (defined in Sec 8.0) belongs to {1, 2, 3, 4, 6}, for a PUSCH transmission performed based on a detected PDCCH/EPDCCH with DCI format 0/4 with =1 or 2,  is determined as if PUCCH format 3 is configured for transmission of HARQ-ACK, except that spatial HARQ-ACK bundling across multiple codewords within a downlink or special subframe is performed for all serving cells configured with a downlink transmission mode that supports up to two transport blocks in case =2, where the UL-reference UL/DL configuration is the UL-reference UL/DL configuration of the serving cell corresponding to the PUSCH transmission.

- if UL-reference UL/DL configuration (defined in Sec 8.0) belongs to {1, 2, 3, 4, 6}, for a PUSCH transmission performed based on a detected PDCCH/EPDCCH with DCI format 0/4 with =3 or 4, , as defined in Table .2-5 or in Table 10.1.3.2-6 respectively, where the value of is replaced by  where the UL-reference UL/DL configuration is the UL-reference UL/DL configuration of the serving cell corresponding to the PUSCH transmission. The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH indicating downlink SPS release in subframe(s) where  and .

- if UL-reference UL/DL configuration (defined in Sec 8.0) is 0, or if UL-reference UL/DL configuration (defined in Sec 8.0) belongs to {1, 2, 3, 4, 6}, for a PUSCH transmission not performed based on a detected PDCCH/EPDCCH with DCI format 0/4, for a subframe  with =1 or 2 ( defined in Sec 10.1.3.2.1), = HARQ-ACK(j),  as defined in Clause .2.1, where the UL-reference UL/DL configuration is the UL-reference UL/DL configuration of the serving cell corresponding to the PUSCH transmission. The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH indicating downlink SPS release in subframe(s) where .

- if UL-reference UL/DL configuration (defined in Sec 8.0) is 0, or if UL-reference UL/DL configuration (defined in Sec 8.0) belongs to {1, 2, 3, 4, 6} and, for a PUSCH transmission not performed based on a detected PDCCH/EPDCCH with DCI format 0/4, for a subframe  with =3 or 4 ( defined in Sec 10.1.3.2.1), , as defined in Table .2-5 or in Table 10.1.3.2-6 respectively, where the UL-reference UL/DL configuration is the UL-reference UL/DL configuration of the serving cell corresponding to the PUSCH transmission. The UE shall not transmit HARQ-ACK on PUSCH if the UE does not receive PDSCH or PDCCH/EPDCCH indicating downlink SPS release in subframe(s) where .

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = dai and PDSCH is associated with DCI format 1/1A/1B/1D/2/2A/2B/2C/2D, the following HARQ-ACK reporting procedure applies to subframe-PDSCH operation. If a UE is configured with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai and PDSCH is associated with DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G, the following HARQ-ACK reporting procedure applies to slot-PDSCH operation.

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = dai or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai, the value of the counter Downlink Assignment Indicator (DAI) in DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G denotes the accumulative number of {serving cell, subframe/slot}-pair(s) in which PDSCH transmission(s) associated with PDCCH/EPDCCH/SPDCCH or PDCCH/EPDCCH/SPDCCH indicating downlink SPS release is present, up to the present serving cell and present subframe/slot, first in increasing order of serving cell index and then in increasing order of subframe/slot index within subframe(s)/slot(s)  where  and C is the set of configured serving cells; the value of the total DAI in DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G denotes the total number of {serving cell, subframe/slot}-pair(s) in which PDSCH transmission(s) associated with PDCCH/EPDCCH/SPDCCH (s) or PDCCH/EPDCCH/SPDCCH indicating downlink SPS release is present, up to the present subframe/slot within subframe(s)/slot(s)  where  and C is the set of configured serving cells, and shall be updated from subframe/slot to subframe/slot. Denote  as the value of the counter DAI in DCI format 1/1A/1B/1D/2/2A/2B/2C/2D/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G scheduling PDSCH transmission or indicating downlink SPS release for serving cell c in subframe/slot  where  according to table 7.3.2.1-1. Denote as the value of the total DAI in subframe/slot  where , according to Table 7.3.2.1-1. The UE shall assume a same value of total DAI in all PDCCH/EPDCCH/SPDCCH scheduling PDSCH transmission(s) and PDCCH/EPDCCH/SPDCCH indicating downlink SPS release in a subframe/slot. For a serving cell c and a value  but , the {serving cell, subframe/slot}-pair {c, } is excluded when determining the values of counter DAI and total DAI for HARQ-ACK transmission in subframe/slot n.

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = dai or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai and if the UE transmits HARQ-ACK using PUCCH format 3 or PUCCH format 4 or PUCCH format 5 in subframe/slot n, the UE shall determine the  according to the following pseudo-code:

Set c = 0 – cell index: lower indices correspond to lower RRC indices of corresponding cell

Set m = 0 – subframe/slot index: lower index corresponds to earlier subframe/slot within subframe(s)/slot(s)  where

Set j = 0

Set

Set

Set

Set  to the number of cells configured by higher layers for the UE

Set M to the number of subframes/slots within subframe(s)/slot(s)  where

while m < M

while c <

if there is a PDSCH on serving cell c in subframe/slot m associated with PDCCH/EPDCCH/SPDCCH or there is a PDCCH/EPDCCH/SPDCCH indicating downlink SPS release on serving cell c in subframe/slot m, and if subframe/slot m belongs to the set of subframe(s)/slot(s)  where ,

if

j = j+1

end if

if

else

end if

if the higher layer parameter spatialBundlingPUCCH is set FALSE and the UE is configured with a transmission mode supporting two transport blocks in at least one configured serving cell,

= HARQ-ACK bit corresponding to the first codeword of this cell

= HARQ-ACK bit corresponding to the second codeword of this cell

elseif the higher layer parameter spatialBundlingPUCCH is set TRUE and the UE is configured with a transmission mode supporting two transport blocks in at least one configured serving cell,

= binary AND operation of the HARQ-ACK bits corresponding to the first and second codewords of this cell

else

= HARQ-ACK bit of this cell

end if

end if

c = c + 1

end while

m = m + 1

end while

if

j = j+1

end if

if the higher layer parameter spatialBundlingPUCCH is set FALSE and the UE is configured with a transmission mode supporting two transport blocks in at least one configured serving cell,

else

end if

for any

if SPS PDSCH transmission is activated for a UE and the UE is configured to receive SPS PDSCH in a subframe/slot  where

= HARQ-ACK bit associated with the SPS PDSCH transmission

end if

For a UE configured with higher layer parameter codebooksizeDetermination-r13 = dai or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai, if the UE transmits HARQ-ACK on PUSCH in a subframe/slot, the UE shall determine the  according to the above procedure as if the UE transmits HARQ-ACK using PUCCH format 3 or PUCCH format 4 or PUCCH format 5, except that the higher layer parameter spatialBundlingPUCCH is replaced by spatialBundlingPUSCH.

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = cc or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = cc, if the UE transmits HARQ-ACK using PUCCH format 4 or PUCCH format 5 in subframe/slot n, the UE shall determine the  according to the pseudo-code in Clause 5.2.3.1 in [4].

For a UE configured with higher layer parameter codebooksizeDetermination-r13 = cc or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = cc, if the UE transmits HARQ-ACK on PUSCH in a subframe/slot, the UE shall determine the  according to the pseudo-code in Clause 5.2.2.6 in [4].

When a PUCCH format 3 transmission of HARQ-ACK coincides with a subframe/slot configured to the UE by higher layers for transmission of a scheduling request, the UE shall multiplex HARQ-ACK and SR bits on HARQ-ACK PUCCH resource as defined in Clause 5.2.3.1 for subframe-PUCCH transmission and Clause 5.2.3.1A for slot-PUCCH transmission in [4], unless the HARQ-ACK corresponds to one of the following cases except for the UE configured with EN-DC and tdm-PatternConfig2,

a single PDSCH transmission only on the primary cell indicated by the detection of a corresponding PDCCH/EPDCCH/SPDCCH in subframe/slot , where , and for UL/DL configuration of the primary cell belonging to {1,2,3,4,5,6}, the DAI value in the PDCCH/EPDCCH/SPDCCH is equal to '1' (defined in Table 7.3-X), or a PDCCH/EPDCCH/SPDCCH indicating downlink SPS release (defined in Clause 9.2) in subframe/slot , where , and for UL/DL configuration of the primary cell belonging to {1,2,3,4,5,6} the DAI value in the PDCCH/EPDCCH/SPDCCH is equal to '1', or

a single PDSCH transmission only on the primary cell where there is not a corresponding PDCCH/EPDCCH/SPDCCH detected within subframe(s)/slot(s) , where  and no PDCCH/EPDCCH/SPDCCH indicating downlink SPS release (defined in Clause 9.2) within subframe(s)/slot(s) , where , or

a PDSCH transmission only on the primary cell where there is not a corresponding PDCCH/EPDCCH/SPDCCH detected within subframe(s)/slot(s) , where and an additional PDSCH transmission only on the primary cell indicated by the detection of a corresponding PDCCH/EPDCCH/SPDCCH in subframe/slot , where  with the DAI value in the PDCCH/EPDCCH/SPDCCH equal to '1' (defined in Table 7.3-X) or a PDCCH/EPDCCH/SPDCCH indicating downlink SPS release (defined in Clause 9.2) in the subframe/slot , where  with the DAI value in the PDCCH/EPDCCH/SPDCCH equal to '1',

in which case the UE shall transmit the HARQ-ACK and scheduling request according to the procedure for PUCCH format 1b with channel selection in TDD for subframe-PDSCH and PUCCH format 1b for slot-PDSCH.

When a PUCCH format 4/5 transmission of HARQ-ACK coincides with a subframe/slot configured to the UE by higher layers for transmission of a scheduling request, the UE shall follow the same procedure described in Clause 7.3.2.1.

If the parameter simultaneousAckNackAndCQI provided by higher layers is set TRUE, and if the UE is configured with PUCCH format 1b with channel selection, and if the UE receives PDSCH and/or PDCCH/EPDCCH indicating downlink SPS release only on the primary cell within subframe(s) , where , a UE shall transmit the CSI and  using PUCCH format 2b for normal CP or PUCCH format 2 for extended CP, according to Clause 5.2.3.4 in [4] with  replaced by . The value of  are generated according to Table 7.3-1 from the  HARQ-ACK responses including ACK in response to PDCCH/EPDCCH indicating downlink SPS release by spatial HARQ-ACK bundling across multiple codewords within each PDSCH transmission for all serving cells . If DL-reference UL/DL configuration belongs to {1,2,3,4,5,6} and, if  and  for a serving cell c, the UE detects that at least one downlink assignment has been missed.

If the parameter simultaneousAckNackAndCQI provided by higher layers is set TRUE, and if the UE is configured with PUCCH format 1b with channel selection and receives at least one PDSCH on the secondary cell within subframe(s) , where , the UE shall drop the CSI and transmit HARQ-ACK according to Clause .

When both HARQ-ACK and CSI are configured to be transmitted in the same sub-frame and if a UE is configured with PUCCH format 3 and not configured with PUCCH format 4/5, except for the UE configured with EN-DC and tdm-PatternConfig2,

if the parameter simultaneousAckNackAndCQI is set TRUE and if the UE receives

- a single PDSCH transmission only on the primary cell indicated by the detection of a corresponding PDCCH/EPDCCH in subframe , where , and for UL/DL configuration of the primary cell belonging to {1,2,3,4,5,6} the DAI value in the PDCCH/EPDCCH is equal to '1' (defined in Table 7.3-X), or a PDCCH/EPDCCH indicating downlink SPS release (defined in Clause 9.2) in subframe , where , and for UL/DL configuration of the primary cell belonging to {1,2,3,4,5,6} the DAI value in the PDCCH/EPDCCH is equal to '1', or

- a single PDSCH transmission only on the primary cell where there is not a corresponding PDCCH detected within subframe(s) , where  and no PDCCH/EPDCCH indicating downlink SPS release (defined in Clause 9.2) within subframe(s) , where ,

then the UE shall transmit the CSI and HARQ-ACK using PUCCH format 2//2b according to Clause .4 in [4];

else if

- the parameter simultaneousAckNackAndCQI-Format3-r11 is set TRUE and if PUCCH format 3 resource is determined according to Clause 10.1.3.1 or Clause 10.1.3.2.2 and

- if the total number of bits in the subframe corresponding to HARQ-ACKs, SR (if any), and the CSI is not larger than 22, or

- if the total number of bits in the subframe corresponding to spatially bundled HARQ-ACKs, SR (if any), and the CSI is not larger than 22

then the UE shall transmit the HARQ-ACKs, SR (if any) and the CSI using the determined PUCCH format 3 resource according to [4];

else,

- the UE shall drop the CSI and transmit the HARQ-ACK according to Clause .

For TDD and a UE configured with PUCCH format 4 or PUCCH format 5, if the parameter simultaneousAckNackAndCQI-Format4-Format5-r13 provided by higher layers is set TRUE, and if the UE has HARQ-ACK/SR and periodic CSI reports to transmit in a subframe, the UE HARQ-ACK/SR and periodic CSI reporting procedure follow the procedure described in Clause 7.3.2.1 with the parameter simultaneousAckNackAndCQI-Format4-Format5-r13 provided by higher layers is set TRUE.

### 7.3.3 FDD-TDD HARQ-ACK reporting procedure for primary cell frame structure type 1

For FDD-TDD and the primary cell is frame structure type 1, with PUCCH format 1b with channel selection,

- for a negative SR transmission,

- UE shall transmit the HARQ-ACK on its assigned HARQ-ACK PUCCH resource with channel selection as defined in Clause 10.1.2A.

- for a positive SR transmission,

- if one transport block or two transport blocks or a PDCCH/EPDCCH indicating downlink SPS release is detected on the primary cell in subframe , and if subframe j is an uplink or a special subframe of configurations 0, 5 and 10 if configured by ssp10-CRS-LessDwPTS with normal downlink CP or of configurations 0 and 4 with extended downlink CP for the secondary cell according to the higher layer parameter subframeAssignment for UE not configured with either higher layer parameter EIMTA-MainConfigServCell-r12 or harq-ReferenceConfig-r14 and according to the higher layer parameter eimta-HARQ-ReferenceConfig-r12 for UE configured with the higher layer parameter EIMTA-MainConfigServCell-r12, and to harq-ReferenceConfig-r14 for the primary cell when the UE is configured with the parameter harq-ReferenceConfig-r14

- UE shall transmit the HARQ-ACK and SR as for FDD with PUCCH format 1a/1b as described in Clause 7.3.1.

- otherwise

- UE shall transmit the HARQ-ACK and SR as for FDD with PUCCH format 1b with channel selection as described in Clause 7.3.1.

where the value of j is

- i-1 if UE is configured with higher layer parameter shortProcessingTime for primary cell and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space on primary cell, and UE is not configured with higher layer parameter shortProcessingTime for secondary cell,

- i+1 if UE is configured with higher layer parameter shortProcessingTime for both primary and secondary cells except when the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space on primary cell,

- i, otherwise.

For FDD-TDD and the primary cell is frame structure type 1, when PUCCH format 3/4/5 is configured for transmission of HARQ-ACK,

- for special subframe configurations 0, 5 and 10 if configured by ssp10-CRS-LessDwPTS with normal downlink CP or configurations 0 and 4 with extended downlink CP in a serving cell, shown in table 4.2-1 [3], the special subframe of the serving cell is excluded from the HARQ-ACK codebook size determination.

- for special subframe configurations 1, 2, 6, and 7 and slot-PDSCH, the second slot of DwPTS of the serving cell is excluded from the HARQ-ACK codebook size determination.

For FDD-TDD and the primary cell is frame structure type 1, when a PUCCH format 3/4/5 transmission of HARQ-ACK coincides with a subframe/slot/subslot configured to the UE by higher layers for transmission of a scheduling request, the UE shall multiplex HARQ-ACK and SR bits on HARQ-ACK PUCCH resource as defined in Clause 5.2.3.1 in [4], unless the HARQ-ACK corresponds to a subframe-PDSCH transmission on the primary cell only or a PDCCH/EPDCCH indicating downlink SPS release on the primary cell only, in which case the SR shall be transmitted as for FDD with PUCCH format 1a/1b as described in Clause 7.3.1.

For FDD-TDD and for a PUSCH transmission, a UE shall not transmit HARQ-ACK on PUSCH in subframe/slot/subslot n if the UE does not receive PDSCH or PDCCH indicating downlink SPS release in

- subframe n- for subframe-PDSCH or in subframe  for PDCCH indicating downlink SPS release,

- slot for slot-PDSCH,

- subslot for subslot- PDSCH if the higher layer parameter ul-TTI-Length is set to 'subslot',

- any of the subslot numbers listed in Table 10.1-1 if the higher layer parameter ul-TTI-Length is set to 'slot' and slot-PUSCH is transmitted in subframe m.

When only a positive SR is transmitted, a UE shall use PUCCH Format 1 for the SR resource as defined in Clause 5.4.1 in [3].

When only a positive SR is transmitted using slot/subslot-PUCCH, a UE shall use PUCCH Format 1 for the first SR resource configured by higher layers as defined in Clause 5.4A.2 in [3].

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = dai or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai, the FDD-TDD HARQ-ACK reporting procedure follows the HARQ-ACK procedure described in Clause 7.3.1 for a UE configured with higher layer parameter codebooksizeDetermination-r13 = dai or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = dai.

If a UE is configured with higher layer parameter codebooksizeDetermination-r13 = cc or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = cc, the FDD-TDD HARQ-ACK reporting procedure follows the HARQ-ACK procedure described in Clause 7.3.1 for a UE configured with higher layer parameter codebooksizeDetermination-r13 = cc or with higher layer parameter codebooksizeDeterminationsSTTI-r15 = cc.

### 7.3.4 FDD-TDD HARQ-ACK reporting procedure for primary cell frame structure type 2

When only a positive SR is transmitted, a UE shall use PUCCH Format 1 for the SR resource as defined in Clause 5.4.1 in [3].

When only a positive SR is transmitted using slot-PUCCH, a UE shall use PUCCH Format 1 for the first SR resource configured by higher layers as defined in Clause 5.4A.2 in [3].

The FDD-TDD HARQ-ACK reporting procedure follows the HARQ-ACK procedure described in Clause 7.3.2.2 with the following exceptions:

- for a serving cell with frame structure type 1, and a UE not configured to monitor PDCCH/EPDCCH in another serving cell for scheduling the serving cell, is defined in Table 10.1.3A-1, else is defined in Table 10.1.3.1-1C if the UE is configured with higher layer parameter shortTTI for slot-PDSCH, in Table 10.1.3.1-1B if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space for subframe-PDSCH and in Table 10.1.3.1-1 otherwise.

- for a serving cell with frame structure type 1 and a UE not configured to monitor PDCCH/EPDCCH/SPDCCH in another serving cell for scheduling the serving cell, if the DL-reference UL/DL configuration of the serving cell in Table 10.1.3A-1 belongs to {2,3,4},is determined as in Clause 7.3.2.2 for a serving cell with DL-reference UL/DL configuration {5}.

- for a serving cell with frame structure type 1, and if PUCCH format 3 is configured for transmission of HARQ-ACK, and for a PUSCH transmission in a subframe/slot n performed based on a detected PDCCH/EPDCCH/SPDCCH with DCI format 0/4/7-0A/7-0B, the UE shall assume the UL-reference UL/DL configuration of the serving cell belongs to {1,2,3,4,5,6}.

- for a serving cell with frame structure type 1, and if DL-reference UL/DL configuration of each of the serving cells belongs to {0,1,2,3,4,6}, and if PUCCH format 1b with channel selection is configured for transmission of HARQ-ACK and for two configured serving cells, the UE shall assume the UL-reference UL/DL configuration of the serving cell belongs to {1,2,3,4,6}.

- for a serving cell with frame structure type 1, a value is determined by the Downlink Assignment Index (DAI) in DCI format 0/4/7-0A/7-0B corresponding to a PUSCH on the serving cell according to Table 7.3-Z in subframe/slot , where =4.

- for a serving cell with frame structure type 1, when PUCCH format 3 is configured for transmission of HARQ-ACK, if the DL-reference UL/DL configuration of the serving cell is 0, the HARQ-ACK for a PDSCH transmission with a corresponding PDCCH/EPDCCH/SPDCCH in subframe/slot  is associated with  if transmission mode configured in the c-th serving cell supports one transport block or spatial HARQ-ACK bundling is applied, or associated with  and  otherwise, where DAI(k) is the value of DAI in DCI format /1B/1D/A/2B/2C/2D detected in subframe ,  and  are the HARQ-ACK feedback for codeword 0 and codeword 1, respectively. For the case with , the HARQ-ACK associated with a PDSCH transmission without a corresponding PDCCH/EPDCCH/SPDCCH is mapped to . The HARQ-ACK feedback bits without any detected PDSCH transmission are set to NACK.
