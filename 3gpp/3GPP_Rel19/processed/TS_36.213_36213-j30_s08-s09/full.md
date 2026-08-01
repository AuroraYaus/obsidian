# 8 Physical uplink shared channel related procedures

If the UE is configured with a SCG, the UE shall apply the procedures described in this clause for both MCG and SCG

- When the procedures are applied for MCG, the terms 'secondary cell', 'secondary cells' , 'serving cell', 'serving cells' in this clause refer to secondary cell, secondary cells, serving cell, serving cells belonging to the MCG respectively.

- When the procedures are applied for SCG, the terms 'secondary cell', 'secondary cells', 'serving cell', 'serving cells' in this clause refer to secondary cell, secondary cells (not including PSCell), serving cell, serving cells belonging to the SCG respectively. The term 'primary cell' in this clause refers to the PSCell of the SCG.

If a UE is configured with a LAA SCell for UL transmissions, the UE shall apply the procedures described in this clause assuming frame structure type 1 for the LAA SCell unless stated otherwise.

For a UE configured with EN-DC/NE-DC and serving cell frame structure type 1, if the UE is configured with tdm-PatternConfig/tdm-PatternConfigNE-DC for the serving cell, the UE is not expected to transmit any uplink physical channel or signal in the serving cell on subframes other than offset-UL subframes, where the offset-UL subframes are determined by applying an offset value given by harq-Offset-r15 to the subframes denoted as uplink in the UL/DL configuration tdm-PatternConfig/tdm-PatternConfigNE-DC.

For a UE configured with EN-DC with primary cell frame structure type 1, if the UE is configured with tdm-PatternConfig2 for a serving cell, and if the UE indicates a capability fdd-PCellUL-TX-AllUL-Subframe-r16 (as specified in [11]), the UE transmits any uplink physical channel or signal without associated DCI if configured, in the serving cell on any uplink subframes. Otherwise, if the UE is configured with tdm-PatternConfig2 for the serving cell and if the UE does not indicate a capability fdd-PCellUL-TX-AllUL-Subframe-r16, the UE is not expected to transmit any uplink physical channel or signal without associated DCI except for PRACH in the serving cell on subframes other than offset-UL subframes, where the offset-UL subframes are determined by applying an offset value given byharq-Offset-r16to the subframes denoted as uplink in the UL/DL configuration tdm-PatternConfig2.

For a UE configured with EN-DC with primary cell frame structure type 2, if the UE is configured with tdm-PatternConfig2 for a serving cell, and if the UE indicates a capabilitytdd-PCellUL-TX-AllUL-Subframe-r16(as specified in [11]), the UE transmits any uplink physical channel or signal without associated DCI if configured, in the serving cell on any uplink subframes. Otherwise, if the UE is configured with tdm-PatternConfig2 for the serving cell and if the UE does not indicate a capabilitytdd-PCellUL-TX-AllUL-Subframe-r16, the UE is not expected to transmit any uplink physical channel or signal without associated DCI except for PRACH in the serving cell on subframes other than offset-UL subframes, where the offset-UL subframes are determined by applying an offset value given byharq-Offset-r16to the subframes denoted as uplink in the UL/DL configuration tdm-PatternConfig2.

For a UE configured with EN-DC/NE-DC, if serving cell frame structure type 1 and if the UE is configured with tdm-PatternConfig/tdm-PatternConfigNE-DC for the serving cell, or if the UE is configured with tdm-PatternConfig2 for a serving cell with EN-DC, the UE is not expected to be configured with more than one serving cell in the uplink.

For a non-BL/CE UE, and for FDD and transmission mode 1 and a cell that is not a LAA SCell, there shall be 16 uplink HARQ processes per serving cell configured with higher layer parameter ul-STTI-Length, otherwise 8 uplink HARQ processes per serving cell for non-subframe bundling operation, i.e. normal HARQ operation, and 3 uplink HARQ processes for subframe bundling operation when parameter e-HARQ-Pattern-r12 is set to TRUE and 4 uplink HARQ processes for subframe bundling operation otherwise. For a non-BL/CE UE, and for FDD and transmission mode 2 configured for subframe-PUSCH and a cell that is not a LAA SCell, there shall be 32 uplink HARQ processes per serving cell configured with higher layer parameters ul-STTI-Length and shortProcessingTime, otherwise 16 uplink HARQ processes per serving cell for non-subframe bundling operation and there are two HARQ processes associated with a given subframe for subframe-PUSCH as described in [8]. The subframe bundling operation is configured by the parameter ttiBundling provided by higher layers.

For FDD and a BL/CE UE configured with CEModeA, there shall be at most 8 uplink HARQ processes per serving cell.

For FDD and a BL/CE UE configured with CEModeB, there shall be at most 4 uplink HARQ processes per serving cell if the UE is configured with higher layer parameter ce-PUSCH-MultiTB-Config, 2 uplink HARQ processes per serving cell otherwise.

For a BL/CE UE and PUSCH transmission using preconfigured uplink resource, there shall be 1 uplink HARQ process per serving cell.

For a LAA SCell, and transmission mode 1, there shall be 16 uplink HARQ processes. For a LAA SCell, and transmission mode 2, there shall be 32 uplink HARQ processes.

There shall be 16 uplink HARQ processes per TDD serving cell configured with higher layer parameter ul-STTI-Length.

In case higher layers configure the use of subframe bundling for FDD and TDD, the subframe bundling operation is only applied to UL-SCH, such that four consecutive uplink subframes are used.

A BL/CE UE is not expected to be configured with simultaneous PUSCH and PUCCH transmission.

Throughout this clause, for a BL/CE UE, the value of $ K_{offset}$ is given by,

- if the UE is configured with the higher layer parameter k-Offset,

- $ K_{offset}=K_{cell\_offset}-K_{UE\_offset}$ where

$ K_{cell\_offset}$ is the parameter k-Offset provided by higher layers, and

$ K_{UE\_offset}$ is the parameter Differential Koffset provided by higher layers, otherwise $ K_{UE\_offset}=0 $

- otherwise,

- $ K_{offset}=0 $.

If the UE is configured with higher layer parameter k-Offset, for a PUSCH (re)transmission associated with the TC-RNTI, $ K_{offset}=$ k-Offset.

## 8.0 UE procedure for transmitting the physical uplink shared channel

The term "UL/DL configuration" in this Clause refers to the higher layer parameter subframeAssignment unless specified otherwise.

Throughout this clause, if the UE is configured with higher layer parameter shortTTI and the corresponding PDCCH/SPDCCH with DCI format 7-0A/7-0B is detected in a subslot, if the UE is configured for subslot uplink transmissions, ![](media_svg/image1.svg) [公式≈: ^{X}p]is determined based on higher layer configuration from ![](media_svg/image2.svg) [公式: {4,6,8}], otherwise![](media_svg/image3.svg) [公式: X_{p}=4]. If subslot number n is in subframe N, subslot ![](media_svg/image4.svg) [公式: n+X_{p}]refers to subslot number ![](media_svg/image5.svg) [公式: (n+X_{p})mod6]in subframe ![](media_svg/image6.svg) [公式≈: _{N}_{+}⋅_{⋅}_{√}n+_{6}X_{p}∂_{∂}_{∃}].

For a given serving cell, if a UE is configured with higher layer parameter shortProcessingTime, the UE is not expected to receive

- more than one uplink scheduling grants for an uplink subframe.

- PDCCH in common search space with DCI format 0 in subframe n and PDCCH in User-specific search space with DCI format 0/4 in the same subframe n.

For a serving cell, and a UE configured with higher layer parameter ul-STTI-Length, the UE is not expected to transmit subframe-PUSCH

- in a given subframe corresponding to PDCCH with uplink DCI format other than 7-0A/7-0B or without a corresponding PDCCH if the UE detects PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B corresponding to a PUSCH transmission in the same subframe or if the UE transmits a slot/subslot-PUSCH without a corresponding PDCCH/SPDCCH. The UE shall transmit the HARQ-ACK response corresponding to the subframe-PUSCH using the slot/subslot-PUSCH (as defined in Clause 7.3). The UE shall apply spatial HARQ-ACK bundling on the HARQ-ACK response

- in case subslot-PUSCH is used

- in case slot-PUSCH is used if the bundling is configured for the cell.

- in a given subframe corresponding to PDCCH/EPDCCH with uplink DCI format other than 7-0A/7-0B received in subframe n if the UE detects PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B in any subframe from subframe n+1 to subframe n+WUL corresponding to a PUSCH transmission, and if ![](media_svg/image7.svg) [公式: W_{UL}>0] is indicated by skipSubframeProcessing capability [12],

- in case of a collision between the subframe-PUSCH and slot/subslot-PUCCH. The UE shall transmit the HARQ-ACK response corresponding to the subframe-PUSCH using the slot/subslot-PUCCH (as defined in Clause 7.3). The UE shall apply spatial HARQ-ACK bundling on the HARQ-ACK response

- in case subslot-PUCCH is used

- in case slot-PUCCH is used if the bundling is configured for the cell.

- in case of a collision between the subframe-PUSCH, subframe-PUCCH, and slot/subslot-PUSCH when simultaneous PUSCH and PUCCH transmission is configured for the UE. The UE is also not expected to transmit subframe-PUCCH. The UE shall transmit the HARQ-ACK response corresponding to the subframe-PUCCH using the slot/subslot-PUSCH.

For a serving cell, and a UE configured with higher layer parameter shortTTI, the UE is not expected to transmit PUSCH corresponding to PDCCH/SPDCCH with CRC scrambled by the C-RNTI/SPS C-RNTI and with uplink DCI format 7-0A/7-0B

- in UpPTS of the special subframe in frame structure type 2 with special subframe configuration 0-9 or,

- for a transport block corresponding to a HARQ process with NDI not toggled if the previous PUSCH transmission of the transport block was signalled via PDCCH in UE specific search space with CRC scrambled by the C-RNTI/SPS C-RNTI with DCI format other than DCI format 7-0A/7-0B when the number of codewords for the previous PUSCH transmission is two or the transport block size is larger than the maximum transport block size supported for slot/subslot-PUSCH transmission.

For a UE configured with more than one serving cell and not capable of simultaneous transmission of different uplink signal durations to different serving cells as indicated by UE capability simultaneousTx-differentTx-duration, in case of a collision between

- a slot-PUSCH of first serving cell and a subframe-PUSCH/PUCCH/SRS/PRACH of second serving cell or

- a subslot-PUSCH of first serving cell and a subframe/slot-PUSCH/PUCCH/SRS/PRACH of second serving cell

the uplink transmission(s) of the second serving cell are dropped.

For a serving cell, and a UE configured with higher layer parameter shortTTI, the UE shall discard PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B for subslot n if PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B for subslot n-1 indicates the DMRS transmission in the first symbol of subslot n

- if the PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B for subslot n does not indicate DMRS transmission in the first symbol of subslot n, or

- if the PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B for subslot n indicates the DMRS transmission in the first symbol of subslot n,

- if the cyclic shift and/or IFDMA comb of subslot n-1 is not identical to that of subslot n, or

- if the PUSCH RBs of subslot n-1 is not identical to those of subslot n, or

- if precoding information and number of layers of subslot n-1 are not identical to those of subslot n, or

- if TPC field for subslot n is not '1' and if the UE is configured with higher layer parameter accumulationEnabledsTTI, or

- if TPC field for subslot n-1 is not identical to that of subslot n and if the UE is not configured with higher layer parameter accumulationEnabledsTTI.

For a serving cell, and a UE configured with higher layer parameter totalNumberPUSCH-SPS-STTI-UL-Repetitions or totalNumberPUSCH-SPS-UL-Repetitions,

- the UE is not expected to transmit PUSCH with a subframe/slot/subslot duration associated with a DCI scrambled by SPS C-RNTI colliding with ongoing PUSCH repetitions of the same subframe/slot/subslot duration associated with another DCI scrambled by SPS C-RNTI.

- for a FDD cell, the UE shall upon detection of a PDCCH/EPDCCH/SPDCCH with DCI format 0/7-0A/7-0B with CRC scrambled by SPS C-RNTI with NDI set to 0, intended for the UE, transmit the corresponding PUSCH inkconsecutive UL subframes/slots/subslots.

- for a TDD cell not configured with higher layer parameter symPUSCH-UpPts-r14, the UE shall upon detection of a PDCCH/EPDCCH/SPDCCH with DCI format 0/7-0A/7-0B with CRC scrambled by SPS C-RNTI with NDI set to 0, intended for the UE, transmit the corresponding PUSCH inkconsecutive UL subframes/slots according to the UL/DL configuration indicated by higher layer parametersubframeAssignmentfor the serving cell.

- for a TDD cell configured with higher layer parameter symPUSCH-UpPts-r14, the UE shall upon detection of a PDCCH/EPDCCH/SPDCCH with DCI format 0/7-0A/7-0B with CRC scrambled by SPS C-RNTI with NDI set to 0, intended for the UE, transmit the corresponding PUSCH ink consecutive UL subframes/slots or UpPTSaccording to the UL/DL configuration indicated by higher layer parametersubframeAssignmentfor the serving cell.

- for a TDD cell configured with UL/DL configuration 0 indicated by higher layer parameter subframeAssignment, the UE is not expected to receive a DCIof format 0 with CRC scrambled by SPS C-RNTI scheduling more than one PUSCH with a subframe duration by UL index.

- for a TDD cell configured with UL/DL configuration 6 indicated by higher layer parameter subframeAssignment and configured with higher layer parameters symPUSCH-UpPts-r14, the UE is not expected to receive a DCI of format 0 with CRC scrambled by SPS C-RNTI scheduling more than one PUSCH with a subframe duration by UL index.

- for a TDD cell configured with UL/DL configurations 0/6 indicated by higher layer parameter subframeAssignment, the UE is not expected to receive a DCIof format 7-0A/7-0B with CRC scrambled by SPS C-RNTI scheduling more than one PUSCH with a slot duration by UL index.

For a serving cell that is not a LAA SCell, and for FDD and normal HARQ operation, the UE shall upon detection on a given serving cell of a

- PDCCH/EPDCCH with DCI format 0/4 and/or a PHICH transmission in subframe n intended for the UE, perform a corresponding PUSCH transmission in subframe n+ kp according to the PDCCH/EPDCCH and PHICH information where ![](media_svg/image8.svg) [公式: k_{p}=3] if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space, ![](media_svg/image9.svg) [公式: k_{p}=4]otherwise.

- PDCCH/SPDCCH with DCI format 7-0A/7-0B intended for the UE in

- slot n, perform a corresponding PUSCH transmission in slot ![](media_svg/image4.svg) [公式: n+X_{p}]

- subslot n, perform a corresponding PUSCH transmission

- in subslot ![](media_svg/image4.svg) [公式: n+X_{p}]if the UE is configured with subslot-based uplink transmissions, or

- in slot 0 of subframe N if the UE is configured with slot-based uplink transmissions, and subslot n (with n being subslot numbered from 0 to 5 within a subframe) is only one of

- subframe N-3, and subslot number n=4 or 5, or

- subframe N-2, and subslot number n=0

- in slot 1 of subframe N if the UE is configured with slot-based uplink transmissions, and subslot n belongs to subframe N-2, and n is only one of subslot number {1, 2, 3}

if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8].

For FDD-TDD and normal HARQ operation and a PUSCH for serving cell  with frame structure type 1, the UE shall upon detection of a PDCCH/EPDCCH with DCI format 0/4 and/or a PHICH transmission in subframe n intended for the UE, perform a corresponding PUSCH transmission for serving cell c in subframe n+![](media_svg/image11.svg) [公式≈: ^{k}p] according to the PDCCH/EPDCCH and PHICH information if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8], where ![](media_svg/image8.svg) [公式: k_{p}=3] if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space, ![](media_svg/image9.svg) [公式: k_{p}=4]otherwise.

For normal HARQ operation, if the UE detects a PHICH transmission and if the most recent PUSCH transmission for the same transport block was using spatial multiplexing according to Clause 8.0.2 and the UE does not detect a PDCCH/EPDCCH with DCI format 4 in subframe n intended for the UE, the UE shall perform the corresponding PUSCH retransmission in the associated subframe according to the PHICH information, and using the number of transmission layers and precoding matrix according to the most recent PDCCH/EPDCCH, if the number of negatively acknowledged transport blocks is equal to the number of transport blocks indicated in the most recent PDCCH/EPDCCH associated with the corresponding PUSCH.

For normal HARQ operation, if the UE detects a PHICH transmission and if the most recent PUSCH transmission for the same transport block was using spatial multiplexing according to Clause 8.0.2 and the UE does not detect a PDCCH/EPDCCH with DCI format 4 in subframe n intended for the UE, and if the number of negatively acknowledged transport blocks is not equal to the number of transport blocks indicated in the most recent PDCCH/EPDCCH associated with the corresponding PUSCH then the UE shall perform the corresponding PUSCH retransmission in the associated subframe according to the PHICH information, using the precoding matrix with codebook index 0 and the number of transmission layers equal to number of layers corresponding to the negatively acknowledged transport block from the most recent PDCCH/EPDCCH. In this case, the UL DMRS resources are calculated according to the cyclic shift field for DMRS [3] in the most recent PDCCH/EPDCCH with DCI format 4 associated with the corresponding PUSCH transmission and number of layers corresponding to the negatively acknowledged transport block.

If a UE is configured with the carrier indicator field for a given serving cell, the UE shall use the carrier indicator field value from the detected PDCCH/EPDCCH with uplink DCI format to determine the serving cell for the corresponding PUSCH transmission.

For FDD and normal HARQ operation, if a PDCCH/EPDCCH/SPDCCH with CSI request field set to trigger an aperiodic CSI report, as described in Clause 7.2.1, is detected by a UE on subframe/slot/subslot n, and simultaneous PUSCH and PUCCH transmission is not configured for the UE or is detected on slot/subslot n, then UCI is mapped on the corresponding PUSCH transmission on,

- slot n+4 for slot-PUSCH transmissions when the higher layer parameter dl-STTI-Length is set to 'slot'

- slot 0 of subframe N+2 for slot-PUSCH transmissions in case of subslot number n=4 or 5 in subframe N-1, or subslot number n=0 in subframe N when the higher layer parameter dl-STTI-Length is set to 'subslot'

- slot 1 of subframe N+2 for slot-PUSCH transmissions in case of subslot number n=1 or 2 or 3 in subframe N when the higher layer parameter dl-STTI-Length is set to 'subslot'

- subslot ![](media_svg/image4.svg) [公式: n+X_{p}]for subslot-PUSCH transmissions

- subframe n+ kp where ![](media_svg/image8.svg) [公式: k_{p}=3] if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space, ![](media_svg/image9.svg) [公式: k_{p}=4]otherwise for subframe-PUSCH transmissions.

For FDD and a BL/CE UE configured with CEModeA, if an MPDCCH with CSI request field set to trigger an aperiodic CSI report, as described in Clause 7.2.1, is detected by a UE on subframe n, then on subframe n+4+Koffset UCI is mapped on the corresponding PUSCH transmission, including all subframe repetitions of the PUSCH transmission.

For FDD-TDD and normal HARQ operation, for a serving cell with frame structure type 1, if a PDCCH/EPDCCH/SPDCCH with CSI request field set to trigger an aperiodic CSI report, as described in Clause 7.2.1, is detected by a UE on subframe n, and simultaneous PUSCH and PUCCH transmission is not configured for the UE or is detected on slot/sublost n, UCI is mapped on the corresponding PUSCH transmission on

- slot n+4 for slot-PUSCH transmissions when the higher layer parameter dl-STTI-Length is set to 'slot';

- slot 0 of subframe N+2 for slot-PUSCH transmissions in case of subslot number n=4 or 5 in subframe N-1, or subslot n=0 corresponding to subframe N when the higher layer parameter dl-STTI-Length is set to 'subslot';

- slot 1 of subframe N+2 for slot-PUSCH transmissions in case of subslot number n=1 or 2 or 3 in subframe N when the higher layer parameter dl-STTI-Length is set to 'subslot';

- subslot ![](media_svg/image4.svg) [公式: n+X_{p}]for subslot-PUSCH transmissions;

- subframe n+ kp where  if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space, otherwise for subframe-PUSCH transmissions.

For TDD, if a UE is configured with the parameter EIMTA-MainConfigServCell-r12 for at least one serving cell, if the UE is configured with one serving cell or if the UE is configured with more than one serving cell and the TDD UL/DL configuration of all the configured serving cells is the same, then for a given serving cell, the serving cell UL/DL configuration is the UL-reference UL/DL configuration.

For TDD, if a UE is configured with more than one serving cell and if the UL/DL configurations of at least two serving cells are different, if the serving cell is a primary cell or if the UE is not configured to monitor PDCCH/EPDCCH in another serving cell for scheduling the serving cell, the serving cell UL/DL configuration is the UL-reference UL/DL configuration.

For TDD, if a UE is configured with more than one serving cell and if the UL/DL configurations of at least two serving cells are different and if the serving cell is a secondary cell and if the UE is configured to monitor PDCCH/EPDCCH in another serving cell for scheduling the serving cell, then for the serving cell, the UL reference UL/DL configuration is given in Table 8-0A corresponding to the pair formed by (other serving cell UL/DL configuration, serving cell UL/DL configuration).

For FDD-TDD and primary cell frame structure type 2, if a serving cell is a primary cell, the serving cell UL/DL configuration is the UL-reference UL/DL configuration for the serving cell.

For FDD-TDD if the UE is not configured to monitor PDCCH/EPDCCH in another serving cell for scheduling a secondary serving cell with frame structure type 2, the serving cell UL/DL configuration is the UL-reference UL/DL configuration for the serving cell.

For FDD-TDD, and for secondary serving cell c with frame structure type 2, if the UE is configured to monitor PDCCH/EPDCCH in another serving cell with frame structure type 1 for scheduling the serving cell, the serving cell UL/DL configuration is the UL-reference UL/DL configuration for the serving cell.

For FDD-TDD, if a UE is configured with more than one serving cell with frame structure type 2, and if the serving cell is a secondary cell with frame structure type 2 and if the UE is configured to monitor PDCCH/EPDCCH in another serving cell with frame structure type 2 for scheduling the serving cell, then for the serving cell, the UL reference UL/DL configuration is given in Table 8-0A corresponding to the pair formed by (other serving cell UL/DL configuration, serving cell UL/DL configuration).

Table 8-0A: UL-reference UL/DL Configuration for serving cell based on the pair formed by (other serving cell UL/DL configuration, serving cell UL/DL configuration)

| Set # | (other serving cell UL/DL configuration, serving cell UL/DL configuration) | UL-reference UL/DL configuration |
| --- | --- | --- |
| Set 1 | (1,1),(1,2),(1,4),(1,5) | 1 |
|  | (2,2),(2,5) | 2 |
|  | (3,3),(3,4),(3,5) | 3 |
|  | (4,4),(4,5) | 4 |
|  | (5,5) | 5 |
| Set 2 | (1,0),(2,0),(3,0),(4,0),(5,0) | 0 |
|  | (2,1),(4,1),(5,1) | 1 |
|  | (5,2) | 2 |
|  | (4,3),(5,3) | 3 |
|  | (5,4) | 4 |
|  | (1,6),(2,6),(3,6),(4,6),(5,6) | 6 |
| Set 3 | (3,1) | 1 |
|  | (3,2),(4,2) | 2 |
|  | (1,3),(2,3) | 3 |
|  | (2,4) | 4 |
| Set 4 | (0,0),(6,0) | 0 |
|  | (0,1),(0,2),(0,4),(0,5),(6,1),(6,2),(6,5) | 1 |
|  | (0,3),(6,3) | 3 |
|  | (6,4) | 4 |
|  | (0,6),(6,6) | 6 |

If a UE is configured with the parameter EIMTA-MainConfigServCell-r12 for a serving cell, for a radio frame of the serving cell, PUSCH transmissions can occur only in subframes that are indicated by eIMTA-UL/DL-configuration as uplink subframe(s) for the serving cell unless specified otherwise.

For TDD and normal HARQ operation, if a PDCCH/EPDCCH/SPDCCH with CSI request field set to trigger an aperiodic CSI report, as described in Clause 7.2.1, is detected by a UE on subframe n and simultaneous PUSCH and PUCCH transmission is not configured for the UE or is detected by a UE on slot n, then on subframe/slot n+k UCI is mapped on the corresponding PUSCH transmission where k is given by

Table 8-2m for special subframe configuration 1,2,3,4,6,7,8 if the UE is configured with higher layer parameter ul-STTI-Length, and the corresponding uplink DCI format is 7-0A/7-0B;

Table 8-2n for special subframe configuration 0,5,9 if the UE is configured with higher layer parameter ul-STTI-Length, and the corresponding uplink DCI format is 7-0A/7-0B;

Table 8-2p if the UE is configured with higher layer parameters ul-STTI-Length and symPUSCH-UpPts-r14, and the corresponding uplink DCI format is 7-0A/7-0B;

Table 8-2i if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space;

Table 8-2 otherwise.

For TDD and a BL/CE UE configured with CEModeA, if an MPDCCH with CSI request field set to trigger an aperiodic CSI report, as described in Clause 7.2.1, is detected by a UE on subframe n, then on subframe n+k UCI is mapped on the corresponding PUSCH transmission, including all subframe repetitions of the PUSCH transmission, where k is given by Table 8-2.

For FDD-TDD normal HARQ operation, for a serving cell with frame structure type 2, if a PDCCH/EPDCCH with CSI request field set to trigger an aperiodic CSI report on the serving cell, as described in Clause 7.2.1, is detected by a UE on subframe n, then on subframe n+k UCI is mapped on the corresponding PUSCH transmission where k is given by Table 8-2 and the "TDD UL/DL configuration" refers to the UL-reference UL/DL configuration for the serving cell, when simultaneous PUSCH and PUCCH transmission is not configured for the UE.

When a UE is configured with higher layer parameter ttiBundling and configured with higher layer parameter e-HARQ-Pattern-r12 set to FALSE or not configured, for FDD and subframe bundling operation, the UE shall upon detection of a PDCCH/EPDCCH with DCI format 0 in subframe n intended for the UE, and/or a PHICH transmission in subframe n-5 intended for the UE, perform a corresponding first PUSCH transmission in the bundle in subframe n+4 according to the PDCCH/EPDCCH and PHICH information if a transport block corresponding to the HARQ process of the first PUSCH transmission is generated as described in [8].

When a UE is configured with higher layer parameter ttiBundling and configured with higher layer parameter e-HARQ-Pattern-r12 set to TRUE, for FDD and subframe bundling operation, the UE shall upon detection of a PDCCH/EPDCCH with DCI format 0 in subframe n intended for the UE, and/or a PHICH transmission in subframe n-1 intended for the UE, perform a corresponding first PUSCH transmission in the bundle in subframe n+4 according to the PDCCH/EPDCCH and PHICH information if a transport block corresponding to the HARQ process of the first PUSCH transmission is generated as described in [8].

For both FDD and TDD serving cells, the NDI as signalled on PDCCH/EPDCCH/MPDCCH/SPDCCH, the RV as determined in Clause 8.6.1, and the TBS as determined in Clause 8.6.2, shall be delivered to higher layers.

If the UE is not configured with higher layer parameter ul-STTI-Length, for a non-BL/CE UE, for TDD and transmission mode 1, the number of HARQ processes per serving cell shall be determined by the UL/DL configuration (Table 4.2-2 of [3]), as indicated in Table 8-1 if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, otherwise the number of HARQ processes per serving cell shall be determined as

- ![](media_svg/image14.svg) [公式: min{8,}Z], where![](media_svg/image15.svg) [公式: Z]is indicated in Table 8-1a, if the UE is configured with shortProcessingTime and the corresponding PDCCH is in the UE-specific search space,

- indicated in Table 8-1a.

For a non-BL/CE UE, for TDD and transmission mode 2 if the UE is not configured with higher layer parameter ul-STTI-Length, the number of HARQ processes per serving cell for non-subframe bundling operation shall be twice the number determined by the UL/DL configuration (Table 4.2-2 of [3]) for TDD and transmission mode 1 there are two HARQ processes associated with a given subframe as described in [8]. For TDD and both transmission mode 1 and transmission mode 2, the "TDD UL/DL configuration" in Table 8-1 and Table 8-1a refers to the UL-reference UL/DL configuration for the serving cell if UL-reference UL/DL configuration is defined for the serving cell and refers to the serving cell UL/DL configuration otherwise.

For a non-BL/CE UE configured higher layer parameter ul-STTI-Length, if the UE is configured with shortProcessingTime and transmission mode 2 for subframe-PUSCH the number of HARQ processes per TDD serving cell for non-subframe bundling operation is 32, and 16 otherwise. There are two HARQ processes for transmission mode 2 of subframe-PUSCH associated with a given subframe as described in [8].

For a BL/CE UE configured with CEModeA and for TDD, the maximum number of HARQ processes per serving cell shall be determined by the UL/DL configuration (Table 4.2-2 of [3]) according to the normal HARQ operation in Table 8-1. For TDD a BL/CE UE configured with CEModeB is not expected to support more than 4 uplink HARQ processes per serving cell if the UE is configured with higher layer parameter ce-PUSCH-MultiTB-Config, 2 uplink HARQ processes per serving cell otherwise.

Table 8-1: Number of synchronous UL HARQ processes for TDD

| TDD UL/DL configuration | Number of HARQ processes for normal HARQ operation | Number of HARQ processes for subframe bundling operation |
| --- | --- | --- |
| 0 | 7 | 3 |
| 1 | 4 | 2 |
| 2 | 2 | N/A |
| 3 | 3 | N/A |
| 4 | 2 | N/A |
| 5 | 1 | N/A |
| 6 | 6 | 3 |

Table 8-1a: Number of synchronous UL HARQ processes for TDD and UE configured with symPUSCH-UpPts-r14

| TDD UL/DL configuration | Number of HARQ processes for normal HARQ operation | Number of HARQ processes for subframe bundling operation |
| --- | --- | --- |
| 0 | 9 | N/A |
| 1 | 6 | N/A |
| 2 | 4 | 2 |
| 3 | 4 | 2 |
| 4 | 3 | N/A |
| 5 | 2 | N/A |
| 6 | 8 | N/A |

For TDD, if the UE is not configured with EIMTA-MainConfigServCell-r12 for any serving cell, and if a UE is configured with one serving cell, or if the UE is configured with more than one serving cell and the TDD UL/DL configuration of all the configured serving cells is the same,

- For TDD UL/DL configurations 1-6 and normal HARQ operation and UE not configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, the UE shall upon detection of a PDCCH/EPDCCH/SPDCCH with uplink DCI format in subframe/slot n and/or a PHICH transmission in subframe n intended for the UE, perform a corresponding PUSCH transmission in subframe/slot n+k, with k given in

- Table 8-2m for special subframe configuration 1, 2, 3, 4, 6, 7, 8 if the UE is configured with higher layer parameter ul-STTI-Length, and the corresponding uplink DCI format is 7-0A/7-0B

- Table 8-2n for special subframe configuration 0, 5, 9 if the UE is configured with higher layer parameter ul-STTI-Length, and the corresponding uplink DCI format is 7-0A/7-0B

- For TDD UL/DL configuration 6 and for n=0, 1, 2, 10, 11, 12

- If only the MSB of the UL index in the uplink DCI is set in slot n, the UE shall perform a corresponding PUSCH transmission in slot n+ k

- If only the LSB of the UL index in the uplink DCI is set in slot n, the UE shall perform a corresponding PUSCH transmission in slot n+ k+1

- If both the MSB and LSB of the UL index in the uplink DCI are set in slot n, the UE shall perform a corresponding PUSCH transmission in both slot n+ k and n+ k+1, where the HARQ process number of the PUSCH in slot n+k is  and the HARQ process number of the PUSCH in n+k+1 is  with  from the HARQ process number field in the corresponding DCI format.

- Table 8-2i if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with DCI format 0/4 and with CRC scrambled by C-RNTI is in the UE-specific search space,

- Table 8-2 otherwise,

according to the PDCCH/EPDCCH/SPDCCH and PHICH information if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8].

- For TDD UL/DL configuration 0 and normal HARQ operation the UE shall upon detection of a PDCCH/EPDCCH with uplink DCI format 0/4 and/or a PHICH transmission in subframe n intended for the UE, perform a corresponding PUSCH transmission in subframe n+k if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8] and if the MSB of the UL index in the PDCCH/EPDCCH with uplink DCI format 0/4 is set to 1 or PHICH is received in subframe n=0 or 5 in the resource corresponding to , as defined in Clause 9.1.2, or PHICH is received in subframe n=1 or 6 corresponding to PUSCH transmission in subframe n-5 for UE configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell. If, for TDD UL/DL configuration 0 and normal HARQ operation, the LSB of the UL index in the DCI format 0/4 is set to 1 in subframe n or a PHICH is received in subframe n=0 or 5 in the resource corresponding to , as defined in Clause 9.1.2, or PHICH is received in subframe n=1 or 6 corresponding to PUSCH transmission in subframe n-4, the UE shall perform a corresponding PUSCH transmission in subframe n+ kp if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8]. If, for TDD UL/DL configuration 0, both the MSB and LSB of the UL index in the PDCCH/EPDCCH with uplink DCI format 0/4 are set in subframe n, the UE shall perform a corresponding PUSCH transmission in both subframes n+ k and n+ kp if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8], with k given in

- Table 8-2g if the UE is configured with higher layer parameter symPUSCH-UpPts-r14 and the UE is either not configured with higher layer parameter shortProcessingTime for the serving cell or is configured with higher layer parameter shortProcessingTime for the serving cell and the corresponding PDCCH is in the common search space,

- Table 8-2i if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 and the UE is configured with higher layer parameter shortProcessingTime for the serving cell and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space,

- Table 8-2j if the UE is configured with higher layer parameters symPUSCH-UpPts-r14 and shortProcessingTime for the serving cell and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space,

- Table 8-2 otherwise.

if the UE is configured with higher layer parameters symPUSCH-UpPts-r14 and shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space, or if n=1 or 6 and the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 but is configured with shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space, otherwise.

In case the UE is configured with higher layer parameter shortProcessingTime for the serving cell and both the MSB and LSB of the UL index in the PDCCH with uplink DCI format 0/4 with the UE's C-RNTI in the UE-specific search space are set to 1, the HARQ process number of the PUSCH in subframe n+k is  and the HARQ process number of the PUSCH in subframe n+kp is , where  is determined according to the HARQ process number field in the corresponding DCI format and MUL_HARQ is the number of UL HARQ processes per cell for transmission mode 1 and half the number of UL HARQ processes per cell for transmission mode 2.

- For TDD UL/DL configuration 0 and normal HARQ operation the UE shall upon detection of a PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B in slot n intended for the UE, perform a corresponding PUSCH transmission in slot n+k if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8], with k given in

- Table 8-2m for special subframe configuration 1, 2, 3, 4, 6, 7, 8, and in Table 8-2n for special subframe configuration 0, 5, 9

- If only the MSB of the UL index in the PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B is set in slot n, the UE shall perform a corresponding PUSCH transmission in slot n+ k

- If only the LSB of the UL index in the PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B is set in slot n, the UE shall perform a corresponding PUSCH transmission in slot n+ k+1

- If both the MSB and LSB of the UL index in the PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B are set in slot n, the UE shall perform a corresponding PUSCH transmission in both slot n+ k and n+ k+1, where the HARQ process number of the PUSCH in slot n+k is  and the HARQ process number of the PUSCH in n+k+1 is  with  from the HARQ process number field in the corresponding DCI format.

- The UE is not expected to receive LSB of the UL index in PDCCH/SPDCCH with uplink DCI format set to 1 in slot n=0, 1, 10 and 11 for special subframe configuration 1, 2, 3, 4, 6, 7, 8

- Table 8-2p if the UE is configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell

- If UL index in the PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B in slot n=2 or n=12 is set to

- '10', the UE shall perform a corresponding PUSCH transmission in slot n+k

- '01', the UE shall perform a corresponding PUSCH transmission in slot n+ k+1

- '11', the UE shall perform a corresponding PUSCH transmission in slot n+ k+5

- '00', the UE shall perform a corresponding PUSCH transmission in slot n+ k, n+k+1, and n+k+5, where the HARQ process number of the PUSCH in slot n+k is , the HARQ process number of the PUSCH in n+k+1 is , and the HARQ process number of the PUSCH in n+k+5 is  with  from the HARQ process number field in the corresponding DCI format.

- If UL index in the PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B in slot n=0, 1, 10 or 11 is set to

- '10', the UE shall perform a corresponding PUSCH transmission in slot n+ k

- '01', the UE shall perform a corresponding PUSCH transmission in slot n+ k+1

- '11', the UE shall perform a corresponding PUSCH transmission in slot n+ k and n+k+1, where the HARQ process number of the PUSCH in slot n+k is ![](media_svg/image25.svg) [公式≈: ^{n}HARQ_ID] and the HARQ process number of the PUSCH in n+k+1 is ![](media_svg/image26.svg) [公式≈: (n_{HARQ_ID}+1)mod16]with ![](media_svg/image25.svg) [公式≈: ^{n}HARQ_ID] from the HARQ process number field in the corresponding DCI format.

- For TDD UL/DL configurations 1-5 and normal HARQ operation and UE configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, the UE shall upon detection of a PDCCH/EPDCCH/SPDCCH with uplink DCI format in subframe/slot n intended for the UE, and/or a PHICH transmission intended for the UE in subframe n+l with l given in Table 8-2h, perform a corresponding PUSCH transmission in subframe/slot n+k, with k given in Table 8-2j if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI has DCI Format 0/4 and is in the UE-specific search space, Table 8-2p if the corresponding PDCCH/SPDCCH has DCI format 7-0A/7-0B, in Table 8-2g otherwise, according to the PDCCH/EPDCCH and/or PHICH information if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8].

- For TDD UL/DL configuration 6 and normal HARQ operation and UE configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, the UE shall upon detection of a PDCCH/EPDCCH with uplink DCI format 0/4 and/or a PHICH transmission in subframe n intended for the UE, perform a corresponding PUSCH transmission in subframe n+k if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8] and if the MSB of the UL index in the PDCCH/EPDCCH with uplink DCI format 0/4 is set to 1 or PHICH is received in subframe n=1 or 6 or 9, or PHICH is received in subframe n=0 corresponding to PUSCH transmission in subframe n-6, or PHICH is received in subframe n=5 corresponding to PUSCH transmission in subframe n-7, with k given in Table 8-2j if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI has DCI format 0/4 and is in the UE-specific search space, in Table 8-2g otherwise. If, for TDD UL/DL configuration 6 and normal HARQ operation, the LSB of the UL index in the DCI format 0/4 is set to 1 in subframe n, or PHICH is received in subframe n=0 or 5 corresponding to PUSCH transmission in subframe n-4, the UE shall perform a corresponding PUSCH transmission in subframe n+ kp if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8]. If, for TDD UL/DL configuration 6, both the MSB and LSB of the UL index in the PDCCH/EPDCCH with uplink DCI format 0/4 are set in subframe n, the UE shall perform a corresponding PUSCH transmission in both subframes n+ k and n+ kp if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8], with k given in Table 8-2j if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI has DCI format 0/4 and is in the UE-specific search space, in Table 8-2g otherwise. In case the UE is configured with higher layer parameter shortProcessingTime for the serving cell and both the MSB and LSB of the UL index in the PDCCH with CRC scrambled by C-RNTI has DCI format 0/4 in the UE-specific search space are set to 1, the HARQ process number of the PUSCH in subframe n+k is  and the HARQ process number of the PUSCH in subframe n+kp is , where  is determined according to the HARQ process number field in the corresponding DCI format and MUL_HARQ is the number of UL HARQ processes per cell for transmission mode 1 and half the number of UL HARQ processes per cell for transmission mode 2. Note that ![](media_svg/image27.svg) [公式≈: ^{k}p]is given as,

- ![](media_svg/image28.svg) [公式: k_{p}=4] if ![](media_svg/image29.svg) [公式: n=0] or 9 and the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space,

- ![](media_svg/image30.svg) [公式: k_{p}=6] if n=1, 5, or 6 and the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space,

- ![](media_svg/image31.svg) [公式: k_{p}=6]otherwise.

The UE is not expected to receive LSB of the UL index in PDCCH/EPDCCH with uplink DCI format 0/4 set to 1 in subframe n=9 unless the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI has DCI format 0/4 in the UE-specific search space.

- For TDD UL/DL configuration 6 and normal HARQ operation and the UE is configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, the UE shall upon detection of a PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B in slot n intended for the UE, perform a corresponding PUSCH transmission in slot n+k if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8], with k given in Table 8-2p

- If UL index in the PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B in slot n=2 is set to

- '10', the UE shall perform a corresponding PUSCH transmission in slot n+k

- '01', the UE shall perform a corresponding PUSCH transmission in slot n+ k+1

- '11', the UE shall perform a corresponding PUSCH transmission in slot n+ k+5

- '00', the UE shall perform a corresponding PUSCH transmission in slot n+ k, n+k+1, and n+k+5, where the HARQ process number of the PUSCH in slot n+k is , the HARQ process number of the PUSCH in n+k+1 is , and the HARQ process number of the PUSCH in n+k+5 is  with  from the HARQ process number field in the corresponding DCI format.

- If UL index in the PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B in slot n=0, 1, 10, 11, 12, 19 is set to

- '10', the UE shall perform a corresponding PUSCH transmission in slot n+ k

- '01', the UE shall perform a corresponding PUSCH transmission in slot n+ k+1

- '11', the UE shall perform a corresponding PUSCH transmission in slot n+ k and n+k+1, where the HARQ process number of the PUSCH in slot n+k is ![](media_svg/image25.svg) [公式≈: ^{n}HARQ_ID] and the HARQ process number of the PUSCH in n+k+1 is ![](media_svg/image26.svg) [公式≈: (n_{HARQ_ID}+1)mod16] with ![](media_svg/image25.svg) [公式≈: ^{n}HARQ_ID] from the HARQ process number field in the corresponding DCI format.

For TDD, if a UE is configured with more than one serving cell and the TDD UL/DL configuration of at least two configured serving cells is not the same or if the UE is configured with EIMTA-MainConfigServCell-r12 for at least one serving cell, or FDD-TDD,

- For a serving cell with an UL-reference UL/DL configurations belonging to {1,2,3,4,5,6} and normal HARQ operation and UE not configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, the UE shall upon detection of a PDCCH/EPDCCH with uplink DCI format 0/4 and/or a PHICH transmission in subframe n intended for the UE, perform a corresponding PUSCH transmission in subframe n+k for the serving cell according to the PDCCH/EPDCCH and/or PHICH information if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8], with k given in Table 8-2i if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI has DCI format 0/4 in the UE-specific search space, in Table 8-2 otherwise, where the "TDD UL/DL Configuration" given in Table 8-2 refers to the UL-reference UL/DL configuration.

- For a serving cell with UL-reference UL/DL configuration 0 and normal HARQ operation the UE shall upon detection of a PDCCH/EPDCCH with uplink DCI format 0/4 and/or a PHICH transmission in subframe n intended for the UE, perform a corresponding PUSCH transmission in subframe n+k for the serving cell if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8] and if the MSB of the UL index in the PDCCH/EPDCCH with uplink DCI format 0/4 is set to 1 or PHICH is received in subframe n=0 or 5 in the resource corresponding to , as defined in Clause 9.1.2, or PHICH is received in subframe n=1 or 6 corresponding to PUSCH transmission in subframe n-5 for UE configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell. If, for a serving cell with UL-reference UL/DL configuration 0 and normal HARQ operation, the LSB of the UL index in the DCI format 0/4 is set to 1 in subframe n or a PHICH is received in subframe n=0 or 5 in the resource corresponding to , as defined in Clause 9.1.2, or PHICH is received in subframe n=1 or 6 corresponding to PUSCH transmission in subframe n-4, the UE shall perform a corresponding PUSCH transmission in subframe n+ kp for the serving cell if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8]. If, for a serving cell with UL-reference UL/DL configuration 0, both the MSB and LSB of the UL index in the PDCCH/EPDCCH with uplink DCI format 0/4 are set in subframe n, the UE shall perform a corresponding PUSCH transmission in both subframes n+ k and n+ kp for the serving cell if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8]. In case the UE is configured with higher layer parameter shortProcessingTime for the serving cell and both the MSB and LSB of the UL index in the PDCCH with uplink DCI format 0/4 with the UE's C-RNTI in the UE-specific search space are set to 1, the HARQ process number of the PUSCH in subframe n+k is  and the HARQ process number of the PUSCH in subframe n+kp is , where  is determined according to the HARQ process number field in the corresponding DCI format and MUL_HARQ is the number of UL HARQ processes per cell for transmission mode 1 and half the number of UL HARQ processes per cell for transmission mode 2. Note that k is given in

- Table 8-2gif the UE is configured with higher layer parameter symPUSCH-UpPts-r14 and the UE is either not configured with higher layer parameter shortProcessingTime for the serving cell or is configured with higher layer parameter shortProcessingTime for the serving cell and the corresponding PDCCH with CRC scrambled by C-RNTI is in the common search space,

- Table 8-2i if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 and the UE is configured with higher layer parameter shortProcessingTime for the serving cell and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space,

- Table 8-2j if the UE is configured with higher layer parameters symPUSCH-UpPts-r14 and shortProcessingTime for the serving cell and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space,

- Table 8-2 otherwise,

where the "TDD UL/DL Configuration" given in Table 8-2, Table 8-2g, Table 8-2i, Table 8-2j refers to the UL-reference UL/DL configuration. Note that if the UE is configured with higher layer parameters symPUSCH-UpPts-r14 and shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space, or if n =1 or 6 and the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 but is configured with shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space, ![](media_svg/image34.svg) [公式: k_{p}=7]otherwise.

- For a serving cell with an UL-reference UL/DL configurations belonging to {1,2,3,4,5} and normal HARQ operation and UE configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, the UE shall upon detection of a PDCCH/EPDCCH with uplink DCI format 0/4 in subframe n intended for the UE, and/or a PHICH transmission intended for the UE in subframe n+l with l given in Table 8-2h, perform a corresponding PUSCH transmission in subframe n+k for the serving cell according to the PDCCH/EPDCCH and/or PHICH information if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8], with k given in Table 8-2j if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI has DCI format 0/4 in the UE-specific search space, in Table 8-2g otherwise, where the "TDD UL/DL Configuration" given in Table 8-2g, Table 8-2h and Table 8-2j refers to the UL-reference UL/DL configuration.

- For a serving cell with UL-reference UL/DL configuration configuration 6 and normal HARQ operation and UE configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, the UE shall upon detection of a PDCCH/EPDCCH with uplink DCI format 0/4 and/or a PHICH transmission in subframe n intended for the UE, perform a corresponding PUSCH transmission in subframe n+k if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8] and if the MSB of the UL index in the PDCCH/EPDCCH with uplink DCI format 0/4 is set to 1 or PHICH is received in subframe n=1 or 6 or 9, or PHICH is received in subframe n=0 corresponding to PUSCH transmission in subframe n-6, or PHICH is received in subframe n=5 corresponding to PUSCH transmission in subframe n-7, with k given in Table 8-2j if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI has DCI format 0/4 in the UE-specific search space, in Table 8-2g otherwise. If, for a serving cell with UL-reference UL/DL configuration 6 and normal HARQ operation, the LSB of the UL index in the DCI format 0/4 is set to 1 in subframe n, or PHICH is received in subframe n=0 or 5 corresponding to PUSCH transmission in subframe n-4, the UE shall perform a corresponding PUSCH transmission in subframe n+ kp if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8]. If, for a serving cell with UL-reference UL/DL configuration 6, both the MSB and LSB of the UL index in the PDCCH/EPDCCH with uplink DCI format 0/4 are set in subframe n, the UE shall perform a corresponding PUSCH transmission in both subframes n+ k and n+ kp if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8], with k given in Table 8-2j if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI has DCI format 0/4 in the UE-specific search space, in Table 8-2g otherwise, where the "TDD UL/DL Configuration" given in Table 8-2g and Table 8-2j refers to the UL-reference UL/DL configuration. In case the UE is configured with higher layer parameter shortProcessingTime for the serving cell and both the MSB and LSB of the UL index in the PDCCH with uplink DCI format 0/4 with the UE's C-RNTI in the UE-specific search space are set to 1, the HARQ process number of the PUSCH in subframe n+k is  and the HARQ process number of the PUSCH in subframe n+kp is , where  is determined according to the HARQ process number field in the corresponding DCI format and MUL_HARQ is the number of UL HARQ processes per cell for transmission mode 1 and half the number of UL HARQ processes per cell for transmission mode 2. Note that kp is given as,

- ![](media_svg/image28.svg) [公式: k_{p}=4] if n = 0 or 9 and the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space,

- ![](media_svg/image30.svg) [公式: k_{p}=6] if n=1, 5, or 6 and the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space,

- ![](media_svg/image31.svg) [公式: k_{p}=6]otherwise.

The UE is not expected to receive LSB of the UL index in PDCCH/EPDCCH with uplink DCI format set to 1 in subframe n=9 unless the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI is in the UE-specific search space.

For TDD UL/DL configurations 1, 2, 3 and 6 and subframe bundling operation, the UE shall upon detection of a PDCCH/EPDCCH with DCI format 0 in subframe n intended for the UE, and/or a PHICH transmission intended for the UE in subframe n-l with l given in Table 8-2a, perform a corresponding first PUSCH transmission in the bundle in subframe n+k according to the PDCCH/EPDCCH and/or PHICH information if a transport block corresponding to the HARQ process of the first PUSCH transmission is generated as described in [8], with k given in Table 8-2 if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, otherwise k given in Table 8-2g.

For TDD UL/DL configuration 0 and subframe bundling operation, the UE shall upon detection of a PDCCH/EPDCCH with DCI format 0 in subframe n intended for the UE, and/or a PHICH transmission intended for the UE in subframe n-l with l given in Table 8-2a, perform a corresponding first PUSCH transmission in the bundle in subframe n+k according to the PDCCH/EPDCCH and PHICH information if a transport block corresponding to the HARQ process of the first PUSCH transmission is generated as described in [8] and if the MSB of the UL index in the DCI format 0 is set to 1 or if , as defined in Clause 9.1.2, with k given in Table 8-2. If, for TDD UL/DL configuration 0 and subframe bundling operation, the LSB of the UL index in the PDCCH/EPDCCH with DCI format 0 is set to 1 in subframe n or if , as defined in Clause 9.1.2, the UE shall perform a corresponding first PUSCH transmission in the bundle in subframe n+7, according to the PDCCH/EPDCCH and PHICH information if a transport block corresponding to the HARQ process of the first PUSCH transmission is generated as described in [8].

Table 8-2: k for TDD configurations 0-6

| TDD UL/DL Configuration | subframe number n |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 0 | 4 | 6 |  |  |  | 4 | 6 |  |  |  |
| 1 |  | 6 |  |  | 4 |  | 6 |  |  | 4 |
| 2 |  |  |  | 4 |  |  |  |  | 4 |  |
| 3 | 4 |  |  |  |  |  |  |  | 4 | 4 |
| 4 |  |  |  |  |  |  |  |  | 4 | 4 |
| 5 |  |  |  |  |  |  |  |  | 4 |  |
| 6 | 7 | 7 |  |  |  | 7 | 7 |  |  | 5 |

Table 8-2a: l for TDD configurations 0, 1, 2, 3 and 6

| TDD UL/DL Configuration | subframe number n |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 0 | 9 | 6 |  |  |  | 9 | 6 |  |  |  |
| 1 |  | 2 |  |  | 3 |  | 2 |  |  | 3 |
| 2 |  | 3 |  | 0 |  |  | 3 |  | 0 |  |
| 3 | 1 |  |  |  |  |  |  | 7 | 0 | 1 |
| 6 | 5 | 5 |  |  |  | 6 | 6 |  |  | 8 |

Table 8-2g: k for TDD configurations 0-6 and UE configured with symPUSCH-UpPts-r14

| TDD UL/DL Configuration | subframe number n |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 0 | 4 | 5 |  |  |  | 4 | 5 |  |  |  |
| 1 | 6 | 6 |  |  | 4 | 6 | 6 |  |  | 4 |
| 2 |  | 5 |  | 4 |  |  | 5 |  | 4 |  |
| 3 | 4 |  |  |  |  |  |  | 4 | 4 | 4 |
| 4 |  |  |  |  |  |  |  | 4 | 4 | 4 |
| 5 |  |  |  |  |  |  |  | 4 | 4 |  |
| 6 | 7 | 7 |  |  |  | 7 | 7 |  |  | 5 |

Table 8-2h: l for TDD configurations 1-5 and UE configured with symPUSCH-UpPts-r14

| TDD UL/DL Configuration | subframe number n |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 1 | 1 | 0 |  |  | 0 | 1 | 0 |  |  | 0 |
| 2 |  | 2 |  | 0 |  |  | 2 |  | 0 |  |
| 3 | 0 |  |  |  |  |  |  | 1 | 0 | 0 |
| 4 |  |  |  |  |  |  |  | 1 | 0 | 0 |
| 5 |  |  |  |  |  |  |  | 1 | 0 |  |

Table 8-2i: k for TDD configurations 0-6 and UE configured with shortProcessingTime

| TDD UL/DL Configuration | subframe number n |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 0 | 3 | 3 |  |  |  | 3 | 3 |  |  |  |
| 1 | 3 |  |  |  | 3 | 3 |  |  |  | 3 |
| 2 |  |  |  |  | 3 |  |  |  |  | 3 |
| 3 | 3 | 3 |  |  |  |  |  |  |  | 3 |
| 4 | 3 |  |  |  |  |  |  |  |  | 3 |
| 5 |  |  |  |  |  |  |  |  |  | 3 |
| 6 | 4 | 6 |  |  |  | 3 | 6 |  |  | 4 |

Table 8-2j: k for TDD configurations 0-6 UE configured with shortProcessingTime and with symPUSCH-UpPts-r14

| TDD UL/DL Configuration | subframe number n |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 0 | 3 | 3 |  |  |  | 3 | 3 |  |  |  |
| 1 | 3 | 5 |  |  | 3 | 3 | 5 |  |  | 3 |
| 2 |  |  |  | 3 | 3 |  |  |  | 3 | 3 |
| 3 | 3 | 3 |  |  |  |  |  |  | 3 | 3 |
| 4 | 3 |  |  |  |  |  |  |  | 3 | 3 |
| 5 |  |  |  |  |  |  |  |  | 3 | 3 |
| 6 | 3 | 5 |  |  |  | 3 | 5 |  |  | 3 |

Table 8-2m: k for TDD configurations 0-6, special subframe configuration 1,2,3,4,6,7,8 and UE configured with ul-STTI-Length

| TDD UL/DL Configuration | slot number n |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| 0 | 4 | 4 | 4 | 5 |  |  |  |  |  |  | 4 | 4 | 4 | 5 |  |  |  |  |  |  |
| 1 | 4 | 4 | 4 | 4 |  |  |  |  |  |  | 4 | 4 | 4 | 4 |  |  |  |  |  |  |
| 2 | 4 | 4 |  |  |  |  |  |  |  |  | 4 | 4 |  |  |  |  |  |  |  |  |
| 3 | 6 | 6 | 6 | 6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 6 | 6 |
| 4 | 4 | 4 | 4 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | 4 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | 6 | 6 | 6 | 6 |  |  |  |  |  |  | 4 | 4 | 4 | 4 |  |  |  |  | 6 | 6 |

Table 8-2n: k for TDD configurations 0-6, special subframe configuration 0,5,9 and UE configured with ul-STTI-Length

| TDD UL/DL Configuration | slot number n |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| 0 | 4 | 5 | 6 |  |  |  |  |  |  |  | 4 | 5 | 6 |  |  |  |  |  |  |  |
| 1 | 5 | 5 | 5 |  |  |  |  |  |  | 5 | 5 | 5 | 5 |  |  |  |  |  |  | 5 |
| 2 | 4 | 4 |  |  |  |  |  |  |  |  | 4 | 4 |  |  |  |  |  |  |  |  |
| 3 | 7 | 7 | 7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 7 | 7 | 7 |
| 4 | 5 | 5 | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 5 |
| 5 | 4 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | 4 | 5 | 6 |  |  |  |  |  |  |  | 4 | 4 | 4 |  |  |  |  |  |  |  |

Table 8-2p: k for TDD configurations 0-6, UE configured with symPUSCH-UpPts-r14, and ul-STTI-Length

| TDD UL/DL Configuration | slot number n |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| 0 | 4 | 5 | 6 |  |  |  |  |  |  |  | 4 | 5 | 6 |  |  |  |  |  |  |  |
| 1 | 5 | 5 | 5 |  |  |  |  |  | 5 | 5 | 5 | 5 | 5 |  |  |  |  |  | 5 | 5 |
| 2 | 4 | 4 |  |  |  |  |  |  |  | 4 | 4 | 4 |  |  |  |  |  |  |  | 4 |
| 3 | 7 | 7 | 7 |  |  |  |  |  |  |  |  |  |  |  |  |  | 7 | 7 | 7 | 7 |
| 4 | 5 | 5 | 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 5 | 5 |
| 5 | 4 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 4 |
| 6 | 4 | 5 | 6 |  |  |  |  |  |  |  | 4 | 4 | 4 |  |  |  |  |  |  | 4 |

For BL/CE UEs, the set of BL/CE UL subframes is indicated as follows

- If UL resource reservation is enabled for the UE as specified in [11],

- for PUSCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PUSCH transmission without a corresponding MPDCCH,

- if the Resource reservation field in the DCI is set to 0, then the set of BL/CE UL subframes corresponds to all uplink subframes during the PUSCH transmission;

- if the Resource reservation field in the DCI is set to 1, then the set of BL/CE UL subframes corresponds to all uplink subframes that are not fully reserved according to higher layer parameters (a subframe is considered fully reserved if and only if all SC-FDMA symbols of the PUSCH transmission are reserved in the subframe);

- for PUCCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PUSCH transmission without a corresponding MPDCCH,

- the set of BL/CE UL subframes corresponds to all uplink subframes that are not fully reserved according to higher layer parameters (a subframe is considered fully reserved if and only if all SC-FDMA symbols of the PUCCH transmission are reserved in the subframe).

- In all other cases, the set of BL/CE UL subframes is indicated by the higher layers according to fdd-DownlinkOrTddSubframeBitmapBR and fdd-UplinkSubframeBitmapBR [11].

For BL/CE UEs, PUSCH transmission can be scheduled by a MPDCCH with DCI format 6-0A/6-0B, or the transmission can correspond to using preconfigured uplink resource configured by higher layers. Transmission using preconfigured uplink resource is initiated by higher layers as specified in [14], while retransmission of transport blocks transmitted using preconfigured uplink resource are scheduled by a MPDCCH with DCI format 6-0A/6-0B.

For a PUSCH transmission using preconfigured uplink resource, the UE shall use the repetition number configured by higher layers.

A BL/CE UE shall upon detection on a given serving cell of an MPDCCH with DCI format 6-0A/6-0B scheduling PUSCH intended for the UE, perform a corresponding PUSCH transmission in subframe(s) ni = n+ki+Koffset if a transport block(s) corresponding to the HARQ process(es) of the PUSCH transmission is generated as described in [8] with i = 0, 1, …, NTBN-1 according to the MPDCCH, where

- subframe n is the last subframe in which the MPDCCH is transmitted;

- the value of ![](media_svg/image35.svg) [公式≈: ^{N}TB]is the number of scheduled TB determined by the corresponding DCI if present, ![](media_svg/image36.svg) [公式: N_{TB}=1] otherwise;

- ![](media_svg/image37.svg) [公式≈: xkkk=<<<_{011}κ_{NN}_{TB}_{−}] and the value of ![](media_svg/image38.svg) [公式: Nnnn±⎰{1,2,κ_{max}}] is determined by the repetition number field in the corresponding DCI, where

- if the UE is configured with higher layer parameter ce-pdsch-puschEnhancement-config with value 'On' ![](media_svg/image39.svg) [公式: n1,n2,κn_{max}]are given by {1,2,4,8,12,16,24,32}

- otherwise, are given in Table 8-2b and Table 8-2c; and

- if the UE is configured with higher layer parameter ce-PUSCH-SubPRB-Config-r15, and the PUSCH resource assignment in the corresponding DCI is using uplink resource allocation type 5, ![](media_svg/image41.svg) [公式≈: ^{NM}^{=∪∪}^{⊥∀}^{⋅∂}⋅∂⋅∂MMslotsRU^{UL}^{2}^{N}∪^{±}^{M}2^{slots}^{UL}^{RU}] where N ≤ 32 for CE Mode A and N ≤ 2048 for CE Mode B, ![](media_svg/image42.svg) [公式≈: ^{M}slots^{UL}] is defined in [3] and ![](media_svg/image43.svg) [公式≈: ^{M}RU] is determined according to procedure in clause 8.1.6, ![](media_svg/image44.svg) [公式: NN=±] otherwise

- in case N>1, subframe(s) n+ki+Koffset with i=0,1,…, NTBN-1 are NTBN consecutive BL/CE UL subframe(s) starting with subframe n+x+Koffset, and in case N=1, k0=x;

- for ![](media_svg/image45.svg) [公式: N_{TB}>1],

- if the UE is configured with higher layer parameter interleaving in ce-PUSCH-MultiTB-Config, and PUSCH corresponding to a MPDCCH with DCI CRC scrambled by C-RNTI and ![](media_svg/image46.svg) [公式: NC>]

- where $ C=\frac {M_{slots}^{UL}}{2}\cdot  M_{RU}$ if the UE is configured with higher layer parameter ce-PUSCH-SubPRB-Config-r15 and the PUSCH resource assignment is using uplink resource allocation type 5, otherwise ![](media_svg/image47.svg) [公式: C=1] for UE configured with CEModeA, and ![](media_svg/image48.svg) [公式: C=4] for UE configured with CEModeB,

- BL/CE UL subframes ![](media_svg/image49.svg) [公式≈: ^{n}gcNrl∪∪++(TB)] with ![](media_svg/image50.svg) [公式: lgcNCgC=−=−=0,1,1,0,1,/1,κκ] are associated with TBr+1 , ![](media_svg/image51.svg) [公式: rN=−0,1,1κ_{TB}]

- otherwise,

- BL/CE UL subframes ![](media_svg/image52.svg) [公式≈: ^{n}rNl∪+] with ![](media_svg/image53.svg) [公式: lN=−0,1,1κ] are associated with TBr+1 , ![](media_svg/image51.svg) [公式: rN=−0,1,1κ_{TB}]

- the HARQ process ID ![](media_svg/image54.svg) [公式: siN_{i},0,1,,1,=−κ_{TB}]for each of the scheduled ![](media_svg/image55.svg) [公式≈: ^{N}TB] ![](media_svg/image56.svg) [公式≈: (^{1}^{<<}^{NN}TBTB,max)]TBs are determined from the value of the 'HARQ index with offset' in the 'Scheduling TBs for Unicast' field for CEmodeA or the 'HARQ index' in the 'Scheduling TBs for Unicast' field for CEmodeB in the corresponding DCI which is a combinatorial index r defined as ![](media_svg/image57.svg) [公式≈: ^{r}^{=}^{N}^{⊆}i^{TB}=0^{−}^{1}^{Ns}^{TB,max}NiTB−^{−}^{i}]$+r_{offset}$, where

- the set ![](media_svg/image58.svg) [公式≈: {s_{i}}_{i}^{N}_{=}^{TB}_{0}^{−}^{1}], (![](media_svg/image59.svg) [公式≈: ^{1,}^{≥≥<}^{sNss}iiiTB,max1+]) contains the ![](media_svg/image55.svg) [公式≈: ^{N}TB]sorted HARQ process IDs and ![](media_svg/image60.svg) [公式≈: x_{y}_{=}^{√}⌡_{⌠}_{⌡}_{∞}^{⊇}⊕_{⊕}_{⊗}_{0}^{x}_{y}^{⇒}⇐_{⇐}_{⇔}x_{x}÷_{<}y_{y}] is the extended binomial coefficient, resulting in unique label ![](media_svg/image61.svg) [公式≈: r⎰−^{√∅}^{⌡⌡}⌠∇_{⌡⌡}_{∞∈}0,,1λ^{⊇⇒}⊕⇐_{⊕⇐}_{⊗⇔}^{N}^{TB,max}_{N}_{TB}]$+r_{offset}$,

- $ r_{offset}$ is the offset value as defined in 5.3.3.1.10 of [4] for CE mode A, and $ r_{offset}=0 $ for CE mode B,

- ![](media_svg/image62.svg) [公式≈: ^{N}TB,max^{=}^{8}] if UE is configured with CEModeA, and ![](media_svg/image63.svg) [公式≈: ^{N}TB,max^{=}^{4}] if UE is configured with CEModeB.

- for FDD, x = 4;

- for TDD UL/DL configurations 1-6, or for TDD UL/DL configuration 0 and a BL/CE UE in CEModeB, the value of x is given as the value of k in Table 8-2 for the corresponding TDD UL/DL configuration; If the value x is not given in Table 8-2 for subframe n, denote subframe n' as the first downlink/special subframe which has a value in Table 8-2 after subframe n, and substitute n with n' in the above procedure for performing the PUSCH transmission.

- for TDD UL/DL configuration 0 and a BL/CE UE in CEModeA, if the MSB of the UL index in the MPDCCH with DCI format 6-0A is set to 1, the value of x is given as the value of k in Table 8-2 for the corresponding TDD UL/DL configuration; if the LSB of the UL index in the MPDCCH with DCI format 6-0A is set to 1, x = 7. The UE is not expected to receive DCI format 6-0A with both the MSB and LSB of the UL index set to 1 when N>1 or ce-PUSCH-MultiTB-Config is configured. In case both the MSB and LSB of the UL index are set to 1, the HARQ process number of the PUSCH corresponding the MSB of the UL index is ![](media_svg/image25.svg) [公式≈: ^{n}HARQ_ID] and the HARQ process number of the PUSCH corresponding the LSB of the UL index is ![](media_svg/image64.svg) [公式≈: (n_{HARQ_ID}+1)mod7], where ![](media_svg/image25.svg) [公式≈: ^{n}HARQ_ID] is determined according to the HARQ process number field in DCI format 6-0A

- The higher layer parameter ttiBundling is not applicable to BL/CE UEs.

- For a BL/CE UE, in case a PUSCH transmission with a corresponding MPDCCH collides with a PUSCH transmission without a corresponding MPDCCH in a subframe n, the PUSCH transmission without a corresponding MPDCCH is dropped from subframe n.

- For a BL/CE UE, in case of collision between at least one physical resource block to be used for PUSCH transmission and physical resource blocks corresponding to configured PRACH resources for BL/CE UEs or non-BL/CE UEs (defined in [3]) in a same subframe, the PUSCH transmission is dropped in that subframe.

- For a BL/CE UE in half-duplex FDD operation, in case a PUSCH transmission including half-duplex guard subframe without a corresponding MPDCCH collides partially or fully with a PDSCH transmission with a corresponding MPDCCH, the PUSCH transmission without a corresponding MPDCCH is dropped.

- For a BL/CE UE in half-duplex FDD operation and configured with ce-pdsch-puschEnhancement-config, in case a PUSCH transmission including half-duplex guard subframe collides partially or fully with a PDSCH transmission without a corresponding MPDCCH, the PUSCH transmission is dropped.

For BL/CE UEs, and for a PUSCH transmission starting in subframe n+ k0 without a corresponding MPDCCH, the UE shall adjust the PUSCH transmission in subframe(s) n+ki with i = 0, 1, …, N-1, where

- 0≤k0<k1<…,kN-1 and the value of ![](media_svg/image38.svg) [公式: Nnnn±⎰{1,2,κ_{max}}] is determined by the repetition number field in the activation DCI, where are given in Table 8-2b and Table 8-2c; and

- if the UE is configured with higher layer parameter ce-PUSCH-SubPRB-Config-r15, and the PUSCH resource assignment in the activation DCI is using uplink resource allocation type 5, ![](media_svg/image65.svg) [公式≈: ^{NM}^{=∪∪}^{⊥∀}^{⋅∂}⋅∂⋅∂MMslotsRU^{UL}^{2}^{N}∪^{±}^{M}2^{slots}^{UL}^{RU}] where ![](media_svg/image66.svg) [公式≈: ^{M}slots^{UL}] is defined in [3] and ![](media_svg/image67.svg) [公式≈: ^{M}RU] is determined according to procedure in clause 8.1.6, ![](media_svg/image44.svg) [公式: NN=±] otherwise

- in case N>1, subframe(s) n+ki with i=0,1,…,N-1 are N consecutive BL/CE UL subframe(s), and in case N=1, k0=0;

A BL/CE UE configured with mpdcch-UL-HARQ-ACK-FeedbackConfig shall upon detection on a given serving cell of an MPDCCH with DCI format 6-0A/6-0B intended for the UE in the UE-specific search space indicating HARQ-ACK(s) corresponding to transport block(s) associated to HARQ process(es) in the most recent PUSCH transmission with N>1, drop the remaining PUSCH transmission(s) (if any) corresponding to the transport block(s) no later than subframe n+k+Koffset, where

subframe n is the last subframe in which the MPDCCH is transmitted; and

for FDD, k = 4;

for TDD the value of k is given in Table 8-2 for the corresponding TDD UL/DL configuration; If the value of k is not given in Table 8-2 for subframe n, denote subframe n' as the first downlink/special subframe which has a value in Table 8-2 after subframe n, and substitute n with n' in the above procedure;

value of ![](media_svg/image68.svg) [公式: N^{±}]is determined by the repetition number field in the corresponding DCI associated with the most recent PUSCH transmission;

if the UE is configured with higher layer parameter ce-PUSCH-SubPRB-Config-r15, and the PUSCH resource assignment in the corresponding DCI associated with the most recent PUSCH transmission is using uplink resource allocation type 5, ![](media_svg/image69.svg) [公式≈: ^{NM}^{=∪∪}^{⊥∀}^{⋅∂}⋅∂⋅∂MMslotsRU^{UL}^{2}^{N}∪^{±}^{M}2^{slots}^{UL}^{RU}] where ![](media_svg/image66.svg) [公式≈: ^{M}slots^{UL}] is defined in [3] and ![](media_svg/image67.svg) [公式≈: ^{M}RU] is determined according to procedure in clause 8.1.6, ![](media_svg/image44.svg) [公式: NN=±] otherwise.

For a BL/CE UE configured with mpdcch-UL-HARQ-ACK-FeedbackConfig, if the UE detects a first MPDCCH with DCI format 6-0A/6-0B intended for the UE scheduling PUSCH in subframes $\{s_{0},\ldots  ,s_{N-1}\}$, and if the UE detects a second MPDCCH with DCI format 6-0A/6-0B intended for the UE scheduling PUSCH in subframes $\{q_{0},\ldots  ,q_{L-1}\}$ with $ M\leq  q_{0}\leq  s_{N-1}$, where

- for any HARQ ID that is indicated in both the first MPDCCH and the second MPDCCH, the NDI indicated in the second MPDCCH is toggled with respect to the NDI indicated in the first MPDCCH

- for each HARQ ID i indicated in the first MPDCCH, the first subframe $ M $ in which the second MPDCCH is transmitted meets $ M\geq  s_{0,i}+k $, where  $ s_{0,i}$ is the first subframe in which the HARQ ID i is transmitted

- for FDD, k = 4,

- for TDD the value of k is given in Table 8-2 for the corresponding TDD UL/DL configuration; If the value of k is not given in Table 8-2 for subframe n, denote subframe n' as the first downlink/special subframe which has a value in Table 8-2 after subframe n, and substitute n with n' in the above procedure

the UE shall

- drop the remaining PUSCH transmission(s) of the transport block(s) scheduled by the first MPDCCH starting from subframe $ K $, where $ M<K\leq  q_{0}$, and

- deliver HARQ-ACK feedback corresponding to the transport block(s) scheduled by the first MPDCCH to higher layers, and

- transmit the PUSCH scheduled by the second MPDCCH in subframes $\{q_{0},\ldots  ,q_{L-1}\}$

Table 8-2b: PUSCH repetition levels (DCI Format 6-0A)

| Higher layer parameter'pusch-maxNumRepetitionCEmodeA' |  |
| --- | --- |
| Not configured | {1,2,4,8} |
| 16 | {1,4,8,16} |
| 32 | {1,4,16,32 } |

Table 8-2c: PUSCH repetition levels (DCI Format 6-0B)

| Higher layer parameter'pusch-maxNumRepetitionCEmodeB' |  |
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

A UE configured with parameter pusch-EnhancementsConfig shall upon detection on a given serving cell of an PDCCH/EPDCCH with DCI Format 0C intended for the UE, perform a corresponding PUSCH transmission in subframe(s) n+ki if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8] with i = 0, 1, …, N-1 according to the PDCCH/EPDCCH, where

- subframe n is the subframe in which the PDCCH/EPDCCH is transmitted; and

- x≤k0<k1<…,kN-1 and the value of N is given by Table 8-2k based on the repetition number field in the corresponding DCI Format 0C; and

- in case N>1, subframe(s) n+ki with i=0,1,…,N-1 are N consecutive UL subframe(s) starting with subframe n+x, and in case N=1, k0=x;

- for FDD, x = 4;

- for TDD UL/DL configurations 1-5 or for TDD UL/DL configuration 6 and a UE not configured with higher layer parameter symPUSCH-UpPts-r14, the value of x is given as the value of k in Table 8-2 for the corresponding TDD UL/DL configuration; If the value x is not given in Table 8-2 for subframe n, denote subframe n' as the first downlink/special subframe which has a value in Table 8-2 after subframe n, and substitute n with n' in the above procedure for performing the PUSCH transmission.

- for TDD UL/DL configuration 0, if the MSB of the UL index in the PDCCH with DCI format 0C is set to 1, the value of x is given as the value of k in Table 8-2 for the corresponding TDD UL/DL configuration; if the LSB of the UL index in the PDCCH with DCI format 0C is set to 1, x = 7. The UE is not expected to receive DCI format 0C with both the MSB and LSB of the UL index set to 1 when N>1. In case both the MSB and LSB of the UL index are set to 1, the HARQ process number of the PUSCH corresponding the MSB of the UL index is ![](media_svg/image25.svg) [公式≈: ^{n}HARQ_ID] and the HARQ process number of the PUSCH corresponding the LSB of the UL index is ![](media_svg/image64.svg) [公式≈: (n_{HARQ_ID}+1)mod7], where ![](media_svg/image25.svg) [公式≈: ^{n}HARQ_ID] is determined according to the HARQ process number field in DCI format 0C

- for TDD UL/DL configuration 6 and a UE configured with higher layer parameter symPUSCH-UpPTS-r14, if the MSB of the UL index in the PDCCH with DCI format 0C is set to 1, the value of x is given as the value of k in Table 8-2 for the corresponding TDD UL/DL configuration; if the LSB of the UL index in the PDCCH with DCI format 0C is set to 1, x = 6. The UE is not expected to receive DCI format 0C with both the MSB and LSB of the UL index set to 1 when N>1. In case both the MSB and LSB of the UL index are set to 1, the HARQ process number of the PUSCH corresponding the MSB of the UL index is ![](media_svg/image25.svg) [公式≈: ^{n}HARQ_ID] and the HARQ process number of the PUSCH corresponding the LSB of the UL index is ![](media_svg/image64.svg) [公式≈: (n_{HARQ_ID}+1)mod7], where ![](media_svg/image25.svg) [公式≈: ^{n}HARQ_ID] is determined according to the HARQ process number field in DCI format 0C

Table 8-2k: PUSCH repetition levels (DCI Format 0C)

| Repetition Number field in DCI Format 0C | Number of repetitions N |
| --- | --- |
| 000 | 1 |
| 001 | 2 |
| 010 | 4 |
| 011 | 8 |
| 100 | 12 |
| 101 | 16 |
| 110 | 24 |
| 111 | 32 |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

For a serving cell that is a LAA SCell, a UE shall

- upon detection of an PDCCH/ EPDCCH with DCI format 0A/0B/4A/4B and with 'PUSCH trigger A' field set to '0' in subframe n intended for the UE, or

- upon detection of PDCCH/ EPDCCH with DCI format 0A/0B/4A/4B in subframe n-p with 'PUSCH trigger A' field set to '1' intended for the UE for the serving cell and that has not been triggered by a 'PUSCH trigger B' field set to '1' received prior to subframe n on the serving cell, with p>=1 and p<=v, and upon detection of PDCCH with DCI CRC scrambled by CC-RNTI and with 'PUSCH trigger B' field set to '1' in subframe n on the serving cell

perform a corresponding PUSCH transmission, conditioned on the channel access procedures described in clause 4.2.1 of [13], in subframe(s) n+l+k+i with i = 0, 1, …, N-1 according to the PDCCH/EPDCCH and HARQ process ID ![](media_svg/image72.svg) [公式≈: ^{mod}^{(}^{n}HARQ_ID^{+}^{i}^{,}^{N}HARQ^{)}], where

- N =1 for DCI format 0A/4A, and value of N is determined by the 'number of scheduled subframes' field in the corresponding DCI format 0B/4B.

- The UE is configured the maximum value of N by higher layer parameter maxNumberOfSchedSubframes-Format0B for DCI format 0B and higher layer parameter maxNumberOfSchedSubframes-Format4B for DCI format 4B;

- value of timing offset k is determined by the 'Timing offset' field in the corresponding DCI 0A/0B/4A/4B according to Table 8-2d if 'PUSCH trigger A' field set to '0' or Table 8-2e otherwise;

- value of ![](media_svg/image73.svg) [公式≈: ^{n}HARQ_ID]is determined by the HARQ process number field in the corresponding DCI format 0A/0B/4A/4B and ![](media_svg/image74.svg) [公式≈: N_{HARQ}=16];

- for 'PUSCH trigger A' field set to '0' in the corresponding DCI format 0A/0B/4A/4B,

- l = 3 if the UE is configured with higher layer parameter shortProcessingTime, and 4 otherwise

- otherwise

- value of l is the UL offset as determined by the 'UL duration and offset' field in the corresponding DCI with CRC scrambled by CC-RNTI according to the procedure in Clause 13A, if 'PUSCH trigger B' field set to '1',

- value of validation duration v is determined by the 'Timing offset' field in the corresponding PDCCH/ EPDCCH with DCI format 0A/0B/4A/4B according to Table 8-2f

- the smallest value of l+k supported by the UE is included in the UE-EUTRA-Capability

- the value of p+l+k is at least 3 if the UE is configured with higher layer parameter shortProcessingTime, and 4 otherwise.

Table 8-2d: Timing offset ![](media_svg/image75.svg) [公式: k]for DCI format 0A/0B/4A/4B with 'PUSCH trigger A' field set to '0'.

| Value of  'Timing offset' field | ![](media_svg/image76.svg) [公式: k] |
| --- | --- |
| 0000 | 0 |
| 0001 | 1 |
| 0010 | 2 |
| 0011 | 3 |
| 0100 | 4 |
| 0101 | 5 |
| 0110 | 6 |
| 0111 | 7 |
| 1000 | 8 |
| 1001 | 9 |
| 1010 | 10 |
| 1011 | 11 |
| 1100 | 12 |
| 1101 | 13 |
| 1110 | 14 |
| 1111 | 15 |

Table 8-2e: Timing offset ![](media_svg/image77.svg) [公式: k]for DCI format 0A/0B/4A/4B with 'PUSCH trigger A' field set to '1'.

| Value of the first two bits of 'Timing offset' field | ![](media_svg/image76.svg) [公式: k] |
| --- | --- |
| 00 | 0 |
| 01 | 1 |
| 10 | 2 |
| 11 | 3 |

Table 8-2f: Validation duration ![](media_svg/image78.svg) [公式: v] for DCI format 0A/0B/4A/4B with 'PUSCH trigger A' field set to '1'.

| Value of the last two bits of 'Timing offset' field | ![](media_svg/image79.svg) [公式: v] |
| --- | --- |
| 00 | 8 |
| 01 | 12 |
| 10 | 16 |
| 11 | 20 |

For a serving cell that is an LAA SCell, a UE that is configured with autonomous uplink transmissions on the serving cell may perform a corresponding PUSCH transmission in subframe n, if the following conditions are met:

- subframe n is configured as usable for autonomous uplink transmission; and

- the UE has not received a grant according to DCI Format 0A/0B/4A/4B for transmission in subframe n; and

- autonomous uplink transmissions on the serving cell have been activated and not released according to the procedure described in clause 9.2A; and

- subframe n is not in the DMTC window of the serving cell; and

- channel access procedures described in clause 4.2.1 of [13] are followed to obtain channel access on the serving cell for subframe n.

- Additionally, if subframe n is a subframe in which the UE is not required to receive any downlink physical channels and/or physical signals according to clause 13A, then in order to perform a corresponding PUSCH transmission the UE shall have detected a PDCCH with DCI CRC scrambled by CC-RNTI indicating that subframe n is shared with the UE.

For an LAA serving cell where a UE is performing an autonomous uplink transmission in one or more contiguous subframe(s) on all ![](media_svg/image80.svg) [公式≈: _{N}_{RB}UL] resource blocks, for the first such subframe the UE randomly determines a timing offset ![](media_svg/image81.svg) [公式≈: ^{N}start^{FS3}] to be applied for transmission according to [3] from a set of values configured by higher layers according to the following rule:

- If the first such subframe is a subframe in which the UE is not required to receive any downlink physical channels and/or physical signals, the set of values is determined by 30.72 * aul-startingFullBW-insideCOT;

- otherwise, the set of values is determined by 30.72 * aul-startingFullBW-outsideCOT.

- ![](media_svg/image81.svg) [公式≈: ^{N}start^{FS3}] is common for all carriers if more than one carrier is activated for autonomous uplink transmission.

For an LAA serving cell where a UE is performing an autonomous uplink transmission in one or more contiguous subframe(s) on fewer than ![](media_svg/image80.svg) [公式≈: _{N}_{RB}UL] resource blocks, for the first such subframe the UE determines a timing offset ![](media_svg/image81.svg) [公式≈: ^{N}start^{FS3}] to be applied for transmission according to [3] according to the following rule:

- If the first such subframe is a subframe in which the UE is not required to receive any downlink physical channels and/or physical signals, ![](media_svg/image81.svg) [公式≈: ^{N}start^{FS3}] is equal to 30.72 * aul-startingPartialBW-insideCOT;

- otherwise, ![](media_svg/image81.svg) [公式≈: ^{N}start^{FS3}] is equal to 30.72 * aul-startingPartialBW-outsideCOT.

For a LAA SCell, a UE is not expected to receive more than one uplink scheduling grant for a subframe.

For a LAA SCell, the HARQ process ID shall be delivered to higher layers.

For a BL/CE UE, the HARQ process ID shall be delivered to higher layers.

If a UE is configured with higher layer parameter shortTTI or shortProcessingTime, the HARQ process ID shall be delivered to higher layers.

A UE is semi-statically configured via higher layer signalling to transmit PUSCH transmissions signalled via PDCCH/EPDCCH with DCI formats other than 7-0A/7-0B according to one of two uplink transmission modes, denoted mode 1 - 2. If a UE is configured with higher layer parameter ul-STTI-Length, the UE is semi-statically configured via higher layer signalling to transmit PUSCH transmissions signalled via PDCCH/SPDCCH with DCI formats 7-0A/7-0B according to one of two uplink transmission modes, denoted mode 1 - 2.

For a LAA SCell, the uplink transmission mode for autonomous uplink transmissions is configured independently from the uplink transmission mode for grant-based uplink transmissions. A UE is not expected to be configured with uplink transmission mode 2 for autonomous transmissions and uplink transmission mode 1 for grant-based uplink transmissions on the same LAA Scell.

If a UE is configured by higher layers to decode PDCCHs with the CRC scrambled by the C-RNTI, the UE shall decode the PDCCH according to the combination defined in Table 8-3 and transmit the corresponding PUSCH if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8]. The scrambling initialization of this PUSCH corresponding to these PDCCHs and the PUSCH retransmission for the same transport block is by C-RNTI.

If a UE is configured by higher layers to decode EPDCCHs with the CRC scrambled by the C-RNTI, the UE shall decode the EPDCCH according to the combination defined in Table 8-3A and transmit the corresponding PUSCH if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8]. The scrambling initialization of this PUSCH corresponding to these EPDCCHs and the PUSCH retransmission for the same transport block is by C-RNTI.

If a UE is configured with higher layer parameter shortTTI and the UE is configured by higher layers to decode SPDCCH with the CRC scrambled by the C-RNTI, the UE shall decode the SPDCCH according to the combination defined in Table 8-3C and transmit the corresponding PUSCH if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8]. The scrambling initialization of this PUSCH corresponding to these SPDCCHs and the PUSCH retransmission for the same transport block is by C-RNTI.

If a UE is configured with a higher layer parameter pusch-EnhancementsConfig, the UE shall decode PDCCH/EPDCCH DCI format 0C in UE specific search space. In this case the UE is not required to decode/monitor DCI format 0 in the UE specific search space.

If a UE is configured with a higher layer parameter shortTTI, the UE shall decode PDCCH DCI format 7-0A/7-0B in UE specific search space.

If a UE is configured with a higher layer parameter pusch-EnhancementsConfig, the UE may assume that PDCCH/EPDCCH for a PUSCH retransmission of a transport block will occur in the UE specific search space if the PDCCH/EPDCCH for the corresponding initial PUSCH transmission for the same transport block was decoded in the UE specific search space.

If a UE is configured with a higher layer parameter pusch-EnhancementsConfig, the UE may assume that PDCCH/EPDCCH for a PUSCH retransmission of a transport block will occur in the common search space if the PDCCH/EPDCCH for the corresponding initial PUSCH transmission for the same transport block was decoded in the common search space.

If a UE is configured with higher layer parameter pusch-EnhancementsConfig, and the UE decodes a DCI format 0 in the common search space, the UE shall calculate the HARQ ID $ n_{HARQ}$ for the corresponding PUSCH transmission in subframe $\lfloor  \frac {n_{s}}{2}\rfloor  $ and radio frame $ n_{f}$ as:

For a transmission in a normal uplink subframe, $ n_{HARQ}=\left ( x_{HARQ}\left ( \lfloor  \frac {n_{s}}{2}\rfloor  \right ) +(x_{MAX}+1)\times  n_{f}\right ) modM_{HARQ}$, where

For FDD, $ x_{HARQ}\left ( n\right ) =n $, and $ x_{max}=9 $

For TDD, $ x_{HARQ}\left ( n\right ) $ is given by Table 8-2q, and $ x_{MAX}=max\left \{ x_{HARQ}\left ( n\right ) \right \} $.

$ M_{HARQ}$ is the number of HARQ processes, which is $ M_{HARQ}=8 $ for FDD, and given by the "Normal HARQ operation" column in table 8-1, in the case of TDD.

For a transmission in a special subframe, $ n_{HARQ}=M_{HARQ}$ if the transmission happens in the first special subframe of the radio frame, and $ n_{HARQ}=M_{HARQ}+1 $ otherwise.

Table 8-2q: $ x_{HARQ}$ for TDD

| TDD UL/DL Configuration | subframe number n |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 0 |  |  | 0 | 1 | 2 |  |  | 3 | 4 | 5 |
| 1 |  |  | 0 | 1 |  |  |  | 2 | 3 |  |
| 2 |  |  | 0 |  |  |  |  | 1 |  |  |
| 3 |  |  | 0 | 1 | 2 |  |  |  |  |  |
| 4 |  |  | 0 | 1 |  |  |  |  |  |  |
| 5 |  |  | 0 |  |  |  |  |  |  |  |
| 6 |  |  | 0 | 1 | 2 |  |  | 3 | 4 |  |

The UE may for handover purposes, and before acquiring the SFN at the target cell, assume an absolute value of the relative time difference between radio frame ![](media_svg/image82.svg) [公式: i] in the current cell and the target cell of less than ![](media_svg/image83.svg) [公式: 153600∪T_{s}] when determining $ n_{HARQ}$.

If a UE is configured by higher layers to decode MPDCCHs with the CRC scrambled by the C-RNTI, the UE shall decode the MPDCCH according to the combination defined in Table 8-3B and transmit the corresponding PUSCH if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8]. The scrambling initialization of this PUSCH corresponding to these MPDCCHs and the PUSCH retransmission for the same transport block is by C-RNTI.

Transmission mode 1 is the default uplink transmission mode for a UE until the UE is assigned an uplink transmission mode by higher layer signalling.

When a UE configured in transmission mode 2 receives a DCI Format 0/0A/0B/0C uplink scheduling grant, it shall assume that the PUSCH transmission is associated with transport block 1 and that transport block 2 is disabled.

Table 8-3: PDCCH and PUSCH configured by C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PUSCH corresponding to PDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 0 | Common andUE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |
|  | DCI format 0A or 0B or 0C or 7-0A | UE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |
| Mode 2 | DCI format 0 | Common andUE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |
|  | DCI format 0A or 0B or 0C | UE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |
|  | DCI format 4 or 4A or 4B or 7-0B | UE specific by C-RNTI | Closed-loop spatial multiplexing (see Clause 8.0.2) |

Table 8-3A: EPDCCH and PUSCH configured by C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PUSCH corresponding to EPDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 0 or 0A or 0B or 0C | UE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |
| Mode 2 | DCI format 0 or 0A or 0B or 0C | UE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |
|  | DCI format 4 or 4A or 4B | UE specific by C-RNTI | Closed-loop spatial multiplexing (see Clause 8.0.2) |

Table 8-3B: MPDCCH and PUSCH configured by C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PUSCH corresponding to MPDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 6-0A or 6-0B | Type0-common (only for 6-0A) and UE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |

Table 8-3C: SPDCCH and PUSCH configured by C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PUSCH corresponding to SPDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 7-0A | UE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |
| Mode 2 | DCI format 7-0B | UE specific by C-RNTI | Closed-loop spatial multiplexing (see Clause 8.0.2) |

If a UE is configured by higher layers to decode PDCCHs with the CRC scrambled by the C-RNTI and is also configured to receive random access procedures initiated by "PDCCH orders", the UE shall decode the PDCCH according to the combination defined in Table 8-4.

If a UE is configured by higher layers to decode EPDCCHs with the CRC scrambled by the C-RNTI and is also configured to receive random access procedures initiated by "PDCCH orders", the UE shall decode the EPDCCH according to the combination defined in Table 8-4A.

If a UE is configured by higher layers to decode MPDCCHs with the CRC scrambled by the C-RNTI and is also configured to receive random access procedures initiated by "PDCCH orders", the UE shall decode the MPDCCH according to the combination defined in Table 8-4B.

Table 8-4: PDCCH configured as "PDCCH order" to initiate random access procedure

| DCI format | Search Space |
| --- | --- |
| DCI format 1A | Common andUE specific by C-RNTI |

Table 8-4A: EPDCCH configured as "PDCCH order" to initiate random access procedure

| DCI format | Search Space |
| --- | --- |
| DCI format 1A | UE specific by C-RNTI |

Table 8-4B: MPDCCH configured as "PDCCH order" to initiate random access procedure

| DCI format | Search Space |
| --- | --- |
| DCI format 6-1A or 6-1B | Type0-common (only for 6-1A) and UE specific by C-RNTI |

If a UE is configured by higher layers to decode PDCCHs with the CRC scrambled by the SPS C-RNTI or UL-SPS-V-RNTI, the UE shall decode the PDCCH according to the combination defined in Table 8-5 and transmit the corresponding PUSCH if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8] except when the UE is configured with higher layer parameter shortProcessingTime and with DCI format 0 mapped onto the UE-specific search space. 
The scrambling initialization of this PUSCH corresponding to these PDCCHs and PUSCH retransmission for the same transport block is by SPS C-RNTI or UL-SPS-V-RNTI. The scrambling initialization of initial transmission of this PUSCH without a corresponding PDCCH and the PUSCH retransmission for the same transport block is by SPS C-RNTI or UL-SPS-V-RNTI.

If a UE is configured by higher layers to decode EPDCCHs with the CRC scrambled by the SPS C-RNTI or UL-SPS-V-RNTI, the UE shall decode the EPDCCH according to the combination defined in Table 8-5A and transmit the corresponding PUSCH if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8]. 
The scrambling initialization of this PUSCH corresponding to these EPDCCHs and PUSCH retransmission for the same transport block is by SPS C-RNTI or UL-SPS-V-RNTI. The scrambling initialization of initial transmission of this PUSCH without a corresponding EPDCCH and the PUSCH retransmission for the same transport block is by SPS C-RNTI or UL-SPS-V-RNTI.

If a UE is configured by higher layers to decode MPDCCHs with the CRC scrambled by the SPS C-RNTI, the UE shall decode the MPDCCH according to the combination defined in Table 8-5B and transmit the corresponding PUSCH if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8]. 
The scrambling initialization of this PUSCH corresponding to these MPDCCHs and PUSCH retransmission for the same transport block is by SPS C-RNTI. The scrambling initialization of initial transmission of this PUSCH without a corresponding MPDCCH and the PUSCH retransmission for the same transport block is by SPS C-RNTI.

If a UE is configured by higher layers to decode SPDCCHs with the CRC scrambled by the SPS C-RNTI, the UE shall decode the SPDCCH according to the combination defined in Table 8-5C and transmit the corresponding PUSCH if a transport block corresponding to the HARQ process of the PUSCH transmission is generated as described in [8]. 
The scrambling initialization of this PUSCH corresponding to these SPDCCHs and PUSCH retransmission for the same transport block is by SPS C-RNTI. The scrambling initialization of initial transmission of this PUSCH without a corresponding SPDCCH and the PUSCH retransmission for the same transport block is by SPS C-RNTI.

Table 8-5: PDCCH and PUSCH configured by SPS C-RNTI or UL-SPS-V-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PUSCH corresponding to PDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 0 | Common andUE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |
|  | DCI format 7-0A | UE specific by C-RNTI |  |
| Mode 2 | DCI format 0 | Common andUE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |
|  | DCI format 7-0B | UE specific by C-RNTI |  |

Table 8-5A: EPDCCH and PUSCH configured by SPS C-RNTI or UL-SPS-V-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PUSCH corresponding to PDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 0 | UE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |
| Mode 2 | DCI format 0 | UE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |

Table 8-5B: MPDCCH and PUSCH configured by SPS C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PUSCH corresponding to PDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 6-0A | Type0-common (only for 6-0A) and UE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |

Table 8-5C: SPDCCH and PUSCH configured by SPS C-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PUSCH corresponding to SPDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 7-0A | UE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |
| Mode 2 | DCI format 7-0B | UE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |

If a UE is configured by higher layers to decode PDCCHs with the CRC scrambled by the Temporary C-RNTI regardless of whether UE is configured or not configured to decode PDCCHs with the CRC scrambled by the C-RNTI, the UE shall decode the PDCCH according to the combination defined in Table 8-6 and transmit the corresponding PUSCH. The scrambling initialization of PUSCH corresponding to these PDCCH is by Temporary C-RNTI.

If a UE is configured by higher layers to decode MPDCCHs with the CRC scrambled by the Temporary C-RNTI regardless of whether UE is configured or not configured to decode MPDCCHs with the CRC scrambled by the C-RNTI during random access procedure, the UE shall decode the MPDCCH according to the combination defined in Table 8-6A and transmit the corresponding PUSCH. The scrambling initialization of PUSCH corresponding to these MPDCCH is by Temporary C-RNTI.

If a Temporary C-RNTI is set by higher layers, the scrambling of PUSCH corresponding to the Random Access Response Grant in Clause 6.2 and the PUSCH retransmission for the same transport block is by Temporary C-RNTI. Else, the scrambling of PUSCH corresponding to the Random Access Response Grant in Clause 6.2 and the PUSCH retransmission for the same transport block is by C-RNTI.

If a UE is also configured by higher layers to decode MPDCCH with CRC scrambled by the C-RNTI during random access procedure, the UE shall decode the MPDCCH according to the combination defined in Table 8-6A and transmit the corresponding PUSCH. The scrambling initialization of PUSCH corresponding to these MPDCCH is by C-RNTI.

The scrambling initialization of PUSCH corresponding to the CB-Msg3 is by CB-RNTI.

Table 8-6: PDCCH configured by Temporary C-RNTI

| DCI format | Search Space |
| --- | --- |
| DCI format 0 | Common |

Table 8-6A: MPDCCH configured by Temporary C-RNTI and/or C-RNTI during random access procedure

| DCI format | Search Space |
| --- | --- |
| DCI format 6-0A, 6-0B | Type2-Common |

If a UE is configured by higher layers to decode PDCCHs with the CRC scrambled by the TPC-PUCCH-RNTI, the UE shall decode the PDCCH according to the combination defined in table 8-7. The notation 3/3A implies that the UE shall receive either DCI format 3 or DCI format 3A depending on the configuration.

If a UE is configured by higher layers to decode MPDCCHs with the CRC scrambled by the TPC-PUCCH-RNTI, the UE shall decode the MPDCCH according to the combination defined in table 8-7A. The notation 3/3A implies that the UE shall receive either DCI format 3 or DCI format 3A depending on the configuration.

Table 8-7: PDCCH configured by TPC-PUCCH-RNTI

| DCI format | Search Space |
| --- | --- |
| DCI format 3/3A | Common |

Table 8-7A: MPDCCH configured by TPC-PUCCH-RNTI

| DCI format | Search Space |
| --- | --- |
| DCI format 3/3A | Type0-Common (for CEModeA only) |

If a UE is configured by higher layers to decode PDCCHs with the CRC scrambled by the TPC-PUSCH-RNTI, the UE shall decode the PDCCH according to the combination defined in table 8.8. The notation 3/3A implies that the UE shall receive either DCI format 3 or DCI format 3A depending on the configuration.

If a UE is configured by higher layers to decode MPDCCHs with the CRC scrambled by the TPC-PUSCH-RNTI, the UE shall decode the MPDCCH according to the combination defined in table 8.8A. The notation 3/3A implies that the UE shall receive either DCI format 3 or DCI format 3A depending on the configuration.

Table 8-8: PDCCH configured by TPC-PUSCH-RNTI

| DCI format | Search Space |
| --- | --- |
| DCI format 3/3A | Common |

Table 8-8A: MPDCCH configured by TPC-PUSCH-RNTI

| DCI format | Search Space |
| --- | --- |
| DCI format 3/3A | Type0-Common (for CEModeA only) |

If the UE is configured by higher layers to decode PDCCHs with the CRC scrambled by higher layer parameter srs-TPC-RNTI-r14, the UE shall decode the PDCCH according to the combination defined in Table 8-8B.

Table 8-8B: PDCCH configured by higher layer parameter srs-TPC-RNTI-r14

| DCI format | Search Space |
| --- | --- |
| DCI format 3B | Common |

If a UE is configured by higher layers to decode PDCCHs/EPDCCHs with the CRC scrambled by the AUL C-RNTI, the UE shall decode the PDCCH/EPDCCH according to the combination defined in Table 8-9.

Table 8-9: PDCCH/EPDCCH configured by AUL C-RNTI

| Autonomous uplinkTransmission mode | DCI format | Search Space | Transmission scheme of correspondingautonomous PUSCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 0A | UE specific by C-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |
| Mode 2 | DCI format 4A | UE specific by C-RNTI | Closed-loop spatial multiplexing (see Clause 8.0.2) |

A UE may transmit PUSCH on preconfigured uplink resources as configured by higher layers. The scrambling initialization of PUSCH transmission using preconfigured uplink resource is by PUR-RNTI.

If a UE is configured by higher layers to decode MPDCCHs with the CRC scrambled by the PUR-RNTI, the UE shall decode the MPDCCH according to the combination defined in Table 8-10 and in case the indication in the DCI corresponds to the retransmission of a transport block transmitted using preconfigured uplink resource, transmit a corresponding PUSCH. The scrambling initialization of this PUSCH corresponding to these MPDCCHs and the PUSCH retransmission for the same transport block is by PUR-RNTI.

Table 8-10: MPDCCH and PUSCH configured by PUR-RNTI

| Transmission mode | DCI format | Search Space | Transmission scheme of PUSCH corresponding to MPDCCH |
| --- | --- | --- | --- |
| Mode 1 | DCI format 6-0A or 6-0B | UE specific by PUR-RNTI | Single-antenna port, port 10 (see Clause 8.0.1) |

### 8.0.1 Single-antenna port scheme

For the single-antenna port transmission schemes (port 10) of the PUSCH, the UE transmission on the PUSCH is performed according to Clause 5.3.2A.1 of [3].

### 8.0.2 Closed-loop spatial multiplexing scheme

For the closed-loop spatial multiplexing transmission scheme of the PUSCH, the UE transmission on the PUSCH is performed according to the applicable number of transmission layers as defined in Clause 5.3.2A.2 of [3].

## 8.1 Resource allocation for PDCCH/EPDCCH/SPDCCH with uplink DCI format

Two resource allocation schemes Type 0 and Type 1 are supported for PDCCH/EPDCCH with uplink DCI format 0/4.

Resource allocation scheme Type 0 or Type 2 or Type 4 or Type 5 are supported for MPDCCH with uplink DCI format or configured by higher layers for PUSCH transmission using preconfigured uplink resource.

Resource allocation scheme Type 0 is supported for PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B.

Resource allocation scheme Type 3 is supported for a LAA SCell and PDCCH/EPDCCH with uplink DCI format 0A/0B/4A/4B.

If the resource allocation type bit is not present in the uplink DCI format, only resource allocation type 0 is supported.

If the resource allocation type bit is present in the uplink DCI format, the selected resource allocation type for a decoded PDCCH/EPDCCH is indicated by a resource allocation type bit where type 0 is indicated by 0 value and type 1 is indicated otherwise. The UE shall interpret the resource allocation field depending on the resource allocation type bit in the PDCCH/EPDCCH with uplink DCI format detected.

### 8.1.1 Uplink resource allocation type 0

The resource allocation information for uplink resource allocation type 0 indicates to a scheduled UE a set of contiguously allocated virtual resource block indices denoted by . A resource allocation field in the scheduling grant consists of a resource indication value (RIV) corresponding to a starting resource block () and a length in terms of contiguously allocated resource blocks ( 1).

For a BL/CE UE,

- uplink resource allocation type 0 is only applicable for UE configured with CEModeA, and

- ![](media_svg/image87.svg) [公式≈: 26≥≥L_{CRBs}], if the UE in TDD is configured with higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocConfig; otherwise ![](media_svg/image88.svg) [公式≈: ^{L}CRBs^{≥}^{6}] and,

- if the UE is configured with higher layer parameters ce-PUSCH-FlexibleStartPRB-AllocConfig, ![](media_svg/image89.svg) [公式≈: ^{L}CRBs]shall not exceed $ N_{RB}^{UL}-RB_{START}-l_{e}$ with $ RB_{START}$={$ l_{e},\ldots  , (N_{RB}^{UL}-l_{e}-1)\}$, where $ l_{e}=\lfloor  \frac {N_{RB}^{UL}}{2}\rfloor  -\frac {6N_{NB}^{UL}}{2}$ is the number of edge RB(s) not belonging to any narrowband in one side of system bandwidth $ N_{RB}^{UL}$, and $ N_{NB}^{UL}$ is the number of narrowbands. PUSCH resource allocations shall not contain PRB(s) not belonging to any narrowband unless it is the center PRB in the uplink system bandwidth, and,

- if the UE is not configured with higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocConfig, ![](media_svg/image80.svg) [公式≈: _{N}_{RB}UL] is always set to 6 in this clause regardless of the system bandwidth.

For PDCCH/SPDCCH DCI format 7-0A/7-0B and $ N_{RB}^{UL}>15 $, VRB allocations for a UE vary from 4 VRB(s) up to ![](media_svg/image90.svg) [公式≈: _{√}N_{RB}^{UL}/4_{∃}≠4] VRBs with an increment step of 4 VRBs. A type 0 resource block assignment field consists of a resource indication value (RIV) corresponding to a starting resource block ![](media_svg/image91.svg) [公式≈: ^{RBRBOffset}STARTSTARTSTART^{=∪+}^{±}^{4}] using ![](media_svg/image92.svg) [公式≈: RB_{START}±=−0,1,2,...,(1))⋅∂_{√∃}N_{RB}^{UL}/4] and a length in terms of virtually contiguously allocated resource blocks ![](media_svg/image93.svg) [公式≈: (4, 8,..., 4)L_{CRBs}=∪⋅∂_{√∃}N_{RB}^{UL}/4], where ![](media_svg/image94.svg) [公式≈: Offset_{START}] is defined if configured by higher layer parameter resourceAllocationOffset; otherwise set to 0. The resource indication value is defined by:

if ![](media_svg/image95.svg) [公式≈: (L_{CRBs}±−1)≥_{√}N_{RB}±^{UL}/2_{∃}] then

![](media_svg/image96.svg) [公式≈: RIV=N_{RB}±^{UL}(L_{CRBs}±−1)+RB_{START}±]

else

![](media_svg/image97.svg) [公式≈: RIV=N_{RB}±^{UL}(N_{RB}±^{UL}−L_{CRBs}±+1)+(N_{RB}±^{UL}−1−RB_{START}±)]

where ![](media_svg/image98.svg) [公式≈: ^{L}CRBs^{±}^{=}^{L}CRBs^{/}^{4}], and ![](media_svg/image99.svg) [公式≈: ^{N}RB^{±}^{UL}^{=}√^{N}RB^{UL}^{/}^{4}∃], and where,

![](media_svg/image100.svg) [公式≈: ^{L}CRBs^{±}] 1 and shall not exceed ![](media_svg/image101.svg) [公式≈: ^{N}RB^{±}^{UL}^{−}^{R}^{B}START^{±}].

Otherwise, the resource indication value is defined by

if  then

if a BL/CE UE in TDD is configured with higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocConfig, then

![](media_svg/image103.svg) [公式≈: RIVNLRB=−+_{RBCRBsSTART}^{UL}(2)]

else

![](media_svg/image104.svg) [公式≈: RIVNLRB=−+_{RBCRBsSTART}^{UL}(1)]

else

### 8.1.2 Uplink resource allocation type 1

The resource allocation information for uplink resource allocation type 1 indicates to a scheduled UE two sets of resource blocks with each set including one or more consecutive resource block groups of size P as given in table 7.1.6.1-1 assuming  as the system bandwidth. A combinatorial index r consists of  bits. The bits from the resource allocation field in the scheduling grant represent r unless the number of bits in the resource allocation field in the scheduling grant is

- smaller than required to fully represent r, in which case the bits in the resource allocation field in the scheduling grant occupy the LSBs of r and the value of the remaining bits of r shall be assumed to be 0; or

- larger than required to fully represent r, in which case r occupies the LSBs of the resource allocation field in the scheduling grant.

The combinatorial index r corresponds to a starting and ending RBG index of resource block set 1, and , and resource block set 2, and  respectively, where r is given by equation  defined in Clause 7.2.1 with M=4 and . Clause 7.2.1 also defines ordering properties and range of values that  (RBG indices) map to. Only a single RBG is allocated for a set at the starting RBG index if the corresponding ending RBG index equals the starting RBG index.

### 8.1.3 Uplink resource allocation type 2

Uplink resource allocation type 2 is only applicable for BL/CE UE configured with CEModeB. The resource allocation information for uplink resource allocation type 2 indicates to a scheduled UE a set of contiguously allocated resource blocks within a narrowband as given in Table 8.1.3-1. If the UE is not configured with higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocOffset, ![](media_svg/image115.svg) [公式: n_{RB}=0] else value of ![](media_svg/image116.svg) [公式≈: ^{n}RB]is given by the higher layer parameter, offsetCeModeB.

If the UE is configured with higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocOffset and the value of the resource allocation field is '110' or '111', the allocated resource blocks with indices less than 0 and greater than 5 correspond to resource-blocks outside the allocated narrowband relative to resource block 0. The physical resource-block numbers are $\{\operatorname {max}\left (\left ( l_{e},n_{RB}+n_{NB,0}+2i\right ) \right ),\operatorname {min}\left (\left ( N_{RB}^{UL}-l_{e}-1,n_{RB}+n_{NB,0}+2i\right ) \right )\}$ with $ i=0 $ or $ i=1 $ for the resource allocation field of '110' or '111', respectively, where $ l_{e}=\lfloor  \frac {N_{RB}^{UL}}{2}\rfloor  -\frac {6N_{NB}^{UL}}{2}$ is the number of edge RB(s) not belonging to any narrowband in one side of system bandwidth $ N_{RB}^{UL}$, and $ N_{NB}^{UL}$ is the number of narrowbands, and $ n_{NB,0}$ is the smallest physical resource-block number of the narrowband as defined in Clause 6.2.7 of [3]. PUSCH resource allocations shall not contain PRB(s) not belonging to any narrowband unless it is the center PRB in the uplink system bandwidth.

Table 8.1.3-1: Resource block(s) allocation for BL/CE UE configured with CEModeB.

| Value of resource allocation field | Allocated resource blocks |
| --- | --- |
| '000' | 0 |
| '001' | 1 |
| '010' | 2 |
| '011' | 3 |
| '100' | 4 |
| '101' | 5 |
| '110' | ![](media_svg/image117.svg) [公式≈: ^{n}RB] and ![](media_svg/image118.svg) [公式: n_{RB}+1] |
| '111' | ![](media_svg/image119.svg) [公式: n_{RB}+2] and ![](media_svg/image120.svg) [公式: n_{RB}+3] |

### 8.1.4 Uplink resource allocation type 3

Uplink resource allocation type 3 is only applicable for a LAA SCell. The resource allocation information for uplink resource allocation type 3 indicates to a scheduled UE a set of allocated resource blocks, ![](media_svg/image121.svg) [公式≈: RB_{START}+l+i∪N] where, ![](media_svg/image122.svg) [公式≈: N=_{√}N_{RB}^{UL}/10_{∃}], ![](media_svg/image123.svg) [公式: i=0,1,λ9].

For ![](media_svg/image124.svg) [公式: N_{RB}^{UL}=100], a resource allocation field in the scheduling grant consists of a resource indication value (RIV). For ![](media_svg/image124.svg) [公式: N_{RB}^{UL}=100] and ![](media_svg/image125.svg) [公式: 0≥RIV<N(N+1)/2] , ![](media_svg/image126.svg) [公式: l=0,1,λL−1] and the resource indication value corresponds to the starting resource block (![](media_svg/image127.svg) [公式≈: ^{RB}START]) and the value of ![](media_svg/image128.svg) [公式: L](![](media_svg/image129.svg) [公式: L÷1]). The resource indication value is defined by,

if ![](media_svg/image130.svg) [公式: (L−1)≥_{√}N/2_{∃}] then

![](media_svg/image131.svg) [公式≈: RIV=N(L−1)+RB_{START}]

else

![](media_svg/image132.svg) [公式≈: RIV=N(N−L+1)+(N−1−RB_{START})]

For ![](media_svg/image133.svg) [公式: N_{RB}^{UL}=100] and ![](media_svg/image134.svg) [公式: RIV÷N(N+1)/2] , the resource indication value corresponds to the starting resource block (![](media_svg/image127.svg) [公式≈: ^{RB}START]) and the set of values ![](media_svg/image135.svg) [公式: l] according to Table 8.1.4-1.

Table 8.1.4-1: ![](media_svg/image127.svg) [公式≈: ^{RB}START] and ![](media_svg/image135.svg) [公式: l] for ![](media_svg/image134.svg) [公式: RIV÷N(N+1)/2].

| ![](media_svg/image136.svg) [公式: RIV−N(N+1)/2] | ![](media_svg/image127.svg) [公式≈: ^{RB}START] | ![](media_svg/image135.svg) [公式: l] |
| --- | --- | --- |
| 0 | 0 | {0, 5} |
| 1 | 0 | {0, 1, 5, 6} |
| 2 | 1 | {0, 5} |
| 3 | 1 | {0, 1, 2, 3, 5, 6, 7, 8} |
| 4 | 2 | {0, 5} |
| 5 | 2 | {0, 1, 2, 5, 6, 7} |
| 6 | 3 | {0, 5} |
| 7 | 4 | {0, 5} |

For ![](media_svg/image137.svg) [公式: N_{RB}^{UL}=50], the resource allocation field indicates a bitmap of the allocated values of l where l = 0,1,2,3,4. The order of set of resource blocks to bitmap bit mapping is in such way that l = 0 to l = 4 are mapped to MSB to LSB of the bitmap respectively. The set of resource blocks is allocated to the UE if the corresponding bit value in the bitmap is 1, and the set of resource blocks are not allocated otherwise.

### 8.1.5 Uplink resource allocation type 4

Uplink resource allocation type 4 is only applicable for BL/CE UEs configured with CEModeA and configured with higher layer parameter ce-pusch-maxBandwidth-config with value 5MHz. The resource allocation information for uplink resource allocation type 4 indicates to a scheduled UE a set of contiguously allocated resource blocks as follows.

- the set of contiguously allocated resource blocks are indicated using resource block groups where each resource block group is a set of ![](media_svg/image138.svg) [公式: P=3]consecutive resource blocks and resource block group indices are determined as described clause 8.1.5.1 where ![](media_svg/image139.svg) [公式≈: _{N}_{RBG}_{UL}_{=}⋅_{⋅}_{√}N_{P}&apos;^{UL}_{RB}∂_{∂}_{∃}] and ![](media_svg/image140.svg) [公式≈: N&apos;^{UL}_{RB}=6∪^{⋅}_{⋅}_{√}^{N}_{6}^{RB}^{UL}^{∂}_{∂}_{∃}].

- the resource allocation field in the scheduling grant consists of a resource block group indication value (![](media_svg/image141.svg) [公式: RBGIV]) corresponding to a starting resource block group index (![](media_svg/image142.svg) [公式≈: ^{RBG}start]) and a length in terms of contiguously allocated resource block groups (![](media_svg/image143.svg) [公式≈: ^{L}CRBGs^{>}^{2}]). The resource block group indication value is determined from ![](media_svg/image144.svg) [公式: RBGIV&apos;] by ![](media_svg/image145.svg) [公式: RBGIV=_{√}RBGIV&apos;/11_{∃}∪32+RBGIV&apos;mod11+21] and ![](media_svg/image144.svg) [公式: RBGIV&apos;] is defined by

if ![](media_svg/image146.svg) [公式≈: (L_{CRBGs}−1)≥(M/2)]

![](media_svg/image147.svg) [公式≈: RBGIV&apos;=(2N_{RBG}^{UL}−K)(L_{CRBGs}−3)+RBG_{start}]

Else

![](media_svg/image148.svg) [公式≈: RBGIV&apos;=(2N_{RBG}^{UL}−K)(M−L_{CRBGs}+1)−RBG_{start}−1]

where, for ![](media_svg/image149.svg) [公式: N_{RB}^{UL}>15], ![](media_svg/image150.svg) [公式: K=9], ![](media_svg/image151.svg) [公式: M=8], and for ![](media_svg/image152.svg) [公式: N_{RB}^{UL}=15], ![](media_svg/image153.svg) [公式: K=5], ![](media_svg/image154.svg) [公式: M=4].

- For odd![](media_svg/image155.svg) [公式≈: _{N}_{RB}UL], if the resource allocation computed using the ![](media_svg/image141.svg) [公式: RBGIV] includes PRBs on both sides of the centre PRB, the resource allocation is updated by removing the PRB with the largest PRB index and including the centre PRB.

#### 8.1.5.1 UL Resource Block Groups

The uplink resource block groups of size ![](media_svg/image156.svg) [公式: P]are numbered ![](media_svg/image157.svg) [公式≈: n_{RBG}=0,...,N_{RBG}^{UL}−1] in order of increasing physical resource-block number where uplink resource block group ![](media_svg/image158.svg) [公式≈: ^{n}RBG]is composed of physical resource-block indices

![](media_svg/image159.svg) [公式≈: ^{√}^{⌡}^{⌠}^{⌡}_{∞}^{P}^{P}P^{∪}^{∪}∪^{n}^{n}n^{RBG}^{RBG}_{RBG}^{+}^{+}+^{i}^{i}i^{0}^{0}_{0}^{+}^{+}+^{i}^{i}i+1^{if}^{if}if^{N}^{N}N^{RB}^{RB}_{RB}^{UL}^{UL}^{UL}^{mod}^{mod}mod^{2}^{2}2^{=}^{=}=^{1}1^{0}^{and}and^{n}n^{RBG}_{RBG}^{<}÷^{N}N^{RBG}_{RBG}^{UL}^{UL}^{2}2]

where

![](media_svg/image160.svg) [公式≈: _{i}_{0}i=_{=}0_{⋅}_{⋅}_{√},_{N}1,...,_{2}_{RB}_{UL}_{∂}_{∂}_{∃}P_{−}−_{6}1_{∪}_{√}_{N}_{2}_{RB}_{UL}_{6}_{∃}]

### 8.1.6 Uplink resource allocation type 5

Uplink resource allocation type 5 is applicable for BL/CE UEs configured with higher layer parameter ce-PUSCH-SubPRB-Config-r15 or PUR-Config or CB-Msg3-ConfigSIB.

The resource allocation information for uplink resource allocation type 5 indicates to a scheduled UE

- a set of contiguously allocated subcarriers within an allocated resource block of a narrowband,

- a number of resource units (![](media_svg/image161.svg) [公式≈: ^{M}RU]) determined by the 'number of resource units' field in the corresponding DCI or higher layer parameter numRUs in PUR-Config according to Table 8.1.6-2 for UE configured with CEModeA, and Table 8.1.6-3 for UE configured with CEModeB, or higher layer parameter numRUs in CB-Msg3-ConfigSIB.

For a UE configured with CEModeA and the value of the 'number of resource units' field in the scheduling grant set to other than '00', the allocated resource block within a narrowband is given by ![](media_svg/image162.svg) [公式≈: _{⋅∂}_{⋅∂}_{⋅∂}_{√∃}_{n}_{10}_{RA}UL] where ![](media_svg/image163.svg) [公式≈: _{n}_{RA}UL] is the value of the 'resource allocation' field in the scheduling grant, and the allocated subcarriers within the allocated resource block is given in Table 8.1.6-1. For a UE configured with CEModeA and the value of higher layer parameter numRUs in PUR-Config or higher layer parameter numRUs in CB-Msg3-ConfigSIB set to other than '00', the allocated resource block within a narrowband is given by ![](media_svg/image162.svg) [公式≈: _{⋅∂}_{⋅∂}_{⋅∂}_{√∃}_{n}_{10}_{RA}UL] where ![](media_svg/image163.svg) [公式≈: _{n}_{RA}UL] is indicated by higher layer parameter prb-AllocationInfo in PUR-Config or each entry of higher layer parameter prb-AllocationInfoset in CB-Msg3-ConfigSIB, and the allocated subcarriers within the allocated resource block is given in Table 8.1.6-1. For PUSCH sub-PRB allocation in CE Mode A, the UE shall consider the DCI valid even if the number of transmitted subframes is greater than pusch-maxNumRepetitionCEmodeA.

For a UE configured with CEModeB and the value of the 'sub-PRB allocation flag' field in the scheduling grant set to '1', the allocated resource block within a narrowband is given by the higher layer parameter locationCE-ModeB, and the allocated subcarriers within the allocated resource block is given in Table 8.1.6-1 where ![](media_svg/image163.svg) [公式≈: _{n}_{RA}UL] is the value of the 'resource allocation' field in the scheduling grant.

For a UE configured with CEModeB and the value of higher layer parameter subPRB-Allocation in PUR-Config set to '1', the allocated resource block within a narrowband is given by higher layer parameter locationCE-ModeB in PUR-Config, and the allocated subcarriers within the allocated resource block are indicated by the higher layer parameter prb-AllocationInfo in PUR-Config according to Table 8.1.6-1.

In Table 8.1.6-1, ![](media_svg/image164.svg) [公式≈: _{N}_{ID}cell] is the physical-layer cell identity as given in clause 6.11 of [3].

Table 8.1.6-1: Subcarriers allocation for BL/CE UE.

| ![](media_svg/image165.svg) [公式: n_{RA}^{UL}mod10]![](media_svg/image163.svg) [公式≈: _{n}_{RA}UL]= value of resource allocation field or indicated by higher layer parameter prb-AllocationInfo in PUR-Config | Modulation | Set of Allocated subcarriers |
| --- | --- | --- |
| 0 | π/2-BPSK | ![](media_svg/image166.svg) [公式≈: N_{ID}^{cell}mod2(0,1)+] |
| 1 | π/2-BPSK | ![](media_svg/image167.svg) [公式≈: N_{ID}^{cell}mod2(3,4)+] |
| 2 | π/2-BPSK | ![](media_svg/image168.svg) [公式≈: N_{ID}^{cell}mod2(6,7)+] |
| 3 | π/2-BPSK | ![](media_svg/image169.svg) [公式≈: N_{ID}^{cell}mod2(9,10)+] |
| 4 | QPSK | 0,1,2 |
| 5 | QPSK | 3,4,5 |
| 6 | QPSK | 6,7,8 |
| 7 | QPSK | 9,10,11 |
| 8 | QPSK | 0,1,2,3,4,5 |
| 9 | QPSK | 6,7,8,9,10,11 |

Table 8.1.6-2: Number of resource units for CEModeA.

| Value of 'number of resource units' field or value of higher layer parameter numRUs in PUR-Config | Number of resource units![](media_svg/image170.svg) [公式≈: ^{M}RU] |
| --- | --- |
| '01' | 1 |
| '10' | 2 |
| '11' | 4 |

Table 8.1.6-3: Number of resource units for CEModeB.

| Value of 'number of resource units' field or value of higher layer parameter numRUs in PUR-Config | Number of resource units![](media_svg/image170.svg) [公式≈: ^{M}RU] |
| --- | --- |
| '0' | 2 |
| '1' | 4 |

## 8.2 UE sounding procedure

If the UE is configured with a PUCCH-SCell, the UE shall apply the procedures described in this clause for both primary PUCCH group and secondary PUCCH group unless stated otherwise

When the procedures are applied for the primary PUCCH group, the terms 'secondary cell', 'secondary cells', 'serving cell', and 'serving cells' in this clause refer to secondary cell, secondary cells, serving cell or serving cells belonging to the primary PUCCH group respectively unless stated otherwise.

When the procedures are applied for secondary PUCCH group, the terms 'secondary cell', 'secondary cells', 'serving cell' and 'serving cells' in this clause refer to secondary cell, secondary cells (not including the PUCCH-SCell), serving cell, serving cells belonging to the secondary PUCCH group respectively unless stated otherwise. The term 'primary cell' in this clause refers to the PUCCH-SCell of the secondary PUCCH group.

A UE shall transmit Sounding Reference Symbol (SRS) on per serving cell SRS resources based on three trigger types:

- trigger type 0: higher layer signalling

- trigger type 1: DCI formats 0/0A/0B/4/4A/4B/1A/6-0A/6-1A for FDD, TDD, and frame structure type 3 and DCI formats 2B/2C/2D/3B for TDD, and frame structure type 3, and DCI format 7-0A/7-0B/7-1E/7-1F/7-1G for TDD if the UE is configured by higher layers for SRS triggering via DCI format 7-0A and has indicated the capability srs-DCI7-Triggering-FS2-r15/ srs-DCI7-Triggering-FS2-r16 and the UE is configured for SRS triggering with srs-DCI7-TriggeringConfig-r15/ srs-DCI7-Triggering-FS2-r16.

trigger type 2: DCI formats 0/4/1A for FDD and TDD, and DCI formats 2B/2C/2D/3B for TDD, and DCI format 7-0A/7-0B/7-1E/7-1F/7-1G for TDD if the UE is configured by higher layers for SRS triggering via DCI format 7-0A and has indicated the capability srs-DCI7-Triggering-FS2-r16 and the UE is configured for SRS triggering with srs-DCI7-TriggeringConfig-r16.

A UE is not expected to be configured with SRS trigger type 0 and trigger type 2 on a LAA SCell.

In case both trigger type 0 and trigger type 1 SRS transmissions would occur in the same subframe in the same serving cell, the UE shall only transmit the trigger type 1 SRS transmission. This prioritization rule shall be applied before other prioritization rules defined in this clause.

In case both trigger type 1 and trigger type 2 SRS transmissions would occur in the same subframe, the UE shall transmit both the trigger type1 and type 2 SRS transmissions.

In case both trigger type 0 and trigger type 2 SRS transmissions would occur in the same subframe, the UE shall transmit both the trigger type 0 and type 2 SRS transmissions.

If higher layer parameter specialSubframePatterns-v1430 indicates ssp10, or if higher layer parameter specialSubframePatterns-v1450 indicates ssp10-CRS-LessDwPTS, the UE shall assume for the purpose of determining $ k_{SRS}$ that the special subframe configuration is that signalled by specialSubframePatterns (without suffix).

A UE may be configured with SRS parameters for trigger type 0 and trigger type 1/2 on each serving cell. A BL/CE UE configured with CEModeB is not expected to be configured with SRS parameters for trigger type 0 and trigger type 1. A BL/CE UE is not expected to be configured with SRS parameters for trigger type 2.The following SRS parameters are serving cell specific and semi-statically configurable by higher layers for trigger type 0 and for trigger type 1/2.

- Number of combs ![](media_svg/image171.svg) [公式≈: ^{K}TC] as defined in Clause 5.5.3.2 of [3] for trigger type 0 and each configuration of trigger type 1/2, if configured

- srs-UpPtsAdd: two or four additional SC-FDMA symbols in UpPTS as defined in [11] for trigger type 0 and trigger type 1, if configured

- Transmission comb , as defined in Clause 5.5.3.2 of [3] for trigger type 0 and each configuration of trigger type 1/2

- Starting physical resource block assignment , as defined in Clause 5.5.3.2 of [3] for trigger type 0 and each configuration of trigger type 1/2 for a serving cell that is not a LAA SCell. For a serving cell that is a LAA SCell, ![](media_svg/image174.svg) [公式: n_{RRC}=0].

- duration: single or indefinite (until disabled), as defined in [11] for trigger type 0

- srs-ConfigIndex ISRS for SRS periodicity  and SRS subframe offset , as defined in Table 8.2-1 and Table 8.2-2 for trigger type 0 and SRS periodicity  and SRS subframe offset , as defined in Table 8.2-4 for trigger type 1 and Table 8.2-5 trigger for type 1/2 for a serving cell that is not a LAA SCell

- SRS bandwidth , as defined in Clause 5.5.3.2 of [3] for trigger type 0 and each configuration of trigger type 1/2 for a serving cell that is not a LAA SCell. For a serving cell that is a LAA SCell, ![](media_svg/image180.svg) [公式: B_{SRS}=0].

- Frequency hopping bandwidth, , as defined in Clause 5.5.3.2 of [3] for trigger type 0 and each configuration of type 2

- Cyclic shift , as defined in Clause 5.5.3.1 of [3] for trigger type 0 and each configuration of trigger type 1/2

- Number of antenna ports  for trigger type 0 and each configuration of trigger type 1/2

- SRS subframe for each configuration of trigger type 1 for a serving cell that is a LAA SCell and DCI format 4B

Starting SC-FDMA symbol $ l_{0}$ and duration $ N $ and repetition number $ R $ as defined in Clause 5.5.3.2.2 of [3] for each configuration of SRS trigger type 2.

For a TDD serving cell,

- If the serving cell not configured for PUSCH/PUCCH transmission, or if the UE supports ce-srsEnhancement-r14

- For trigger type 0, the UE can be configured with more than one configuration of SoundingRS-UL-ConfigDedicatedUpPTsExt and/or SoundingRS-UL-ConfigDedicated, and the SRS parameters in each of the configurations shall be used. The UE is not expected to receive more than one SRS configuration indicating SRS transmission on multiple symbols in different subframes within a half frame.

- For trigger type 1, the UE can be configured with more than one configuration of SoundingRS-UL- ConfigDedicatedAperiodicUpPTsExt and/or SoundingRS-UL- ConfigDedicatedAperiodic, and the SRS parameters in each of the configurations shall be used. The UE is not expected to receive more than one SRS configuration indicating SRS transmission on multiple symbols in different subframes within a half frame.

- For trigger type 2, the parameters in SoundingRS-UL-ConfigDedicatedAdd shall be used.

- Otherwise

- For trigger type 0, if SoundingRS-UL-ConfigDedicatedUpPTsExt is configured, the SRS parameters in SoundingRS-UL-ConfigDedicatedUpPTsExt shall be used; otherwise, SoundingRS-UL-ConfigDedicated shall be used.

- For trigger type 1, if SoundingRS-UL-ConfigDedicatedAperiodicUpPTsExt is configured, the SRS parameters in SoundingRS-UL-ConfigDedicatedAperiodicUpPTsExt shall be used; otherwise, SoundingRS-UL-ConfigDedicatedAperiodic shall be used.

- For trigger type 2, the parameters in SoundingRS-UL-ConfigDedicatedAdd shall be used.

For trigger type 1 and DCI format 4/4A/4B/7-0B, and trigger type 2 and DCI format 4/7-0B, three sets of SRS parameters, srs-ConfigApDCI-Format4, are configured by higher layer signalling. The 2-bit SRS request field [4] in DCI format 4/4A/4B/7-0B indicates the SRS parameter set given in Table 8.1-1. For trigger type 1 and DCI format 0/0A/0B /6-0A/7-0A, and trigger type 2 and DCI format 0/6-0A/7-0A, a single set of SRS parameters, srs-ConfigApDCI-Format0, is configured by higher layer signalling. For trigger type 1/2 and DCI formats 1A/2B/2C/2D/6-1A/7-1E/7-1F/7-1G, a single common set of SRS parameters, srs-ConfigApDCI-Format2b, is configured by higher layer signalling. For a serving cell that is not a LAA SCell, the SRS request field is 1 bit [4] for DCI formats 0/1A/2B/2C/2D/6-0A/6-1A/7-0A/7-1E/7-1F/7-1G, with type 1/2 SRS triggered if the value of the SRS request field is set to '1'. For a serving cell that is a LAA SCell, the SRS timing offset field is 3 bits [4] for DCI formats 1A/2B/2C/2D, with a type 1 SRS triggered if the value of the SRS timing offset field is not set to '000'. The SRS request field is 1 bit [4] for DCI formats 0A, with type 1/2 SRS triggered if the value of the SRS request field is set to '1'. The 2-bit SRS request field [4] in DCI format 0B indicates the type 1 SRS triggering and PUSCH subframe (as determined in Clause 8.0) with SRS as given in Table 8.2-0A.

For a serving cell that is not a LAA SCell, a 1-bit SRS request field shall be included in DCI formats 0/1A for frame structure type 1 and 0/1A/2B/2C/2D for frame structure type 2 if the UE is configured with SRS parameters for DCI formats 0/1A/2B/2C/2D by higher-layer signalling. A 1-bit SRS request field shall be included in DCI format 7-0A for frame structure type 2 if the UE is configured with SRS parameters srs-ConfigApDCI-Format0 and srs-DCI7-TriggeringConfig-r15 by higher-layer signalling. A 1-bit SRS request field shall be included in DCI formats 7-1E/7-1F/7-1G for frame structure type 2 if the UE is configured with SRS parameters srs-ConfigApDCI-Format2b and srs-DCI7-TriggeringConfig-r15 by higher-layer signalling. A 1-bit SRS request field shall be included in DCI formats 6-0A/6-1A, the value of which is reserved if the UE is not configured with SRS parameters for DCI formats 6-0A/6-1A by higher layer signalling.

For a TDD serving cell not configured for PUSCH/PUCCH transmission, and trigger type 1/2, a SRS request field [4] shall be included in DCI format 3B if the value of the higher layer parameter fieldTypeFormat3B is set to 3 or 4. If the UE is configured with more than 5 TDD serving cells without PUSCH/PUCCH transmission, a single SRS request field is included in DCI format 3B for a set of the TDD serving cells without PUSCH/PUCCH transmission as given in Table 8.2-0C; otherwise one or more SRS request fields is included in DCI format 3B each corresponding to a TDD serving cell without PUSCH/PUCCH transmission as configured by higher layers. If the UE is configured with no more than 5 TDD serving cells without PUSCH/PUCCH transmission, and the UE is not configured with srs-ConfigApDCI-Format4, the SRS request field [4] in DCI format 3B is 1-bit, 2-bits otherwise. For the 1-bit SRS request field [4] in DCI format 3B, type 1/2 SRS is triggered if the value of the SRS request field is set to '1' with SRS parameters, srs-ConfigApDCI-Format2b, configured by higher layer signalling. For the 2-bit SRS request field [4] in DCI format 3B, and UE configured with no more than 5 TDD serving cells without PUSCH/PUCCH transmission, the SRS request field indicates the SRS parameter set given in Table 8.1-1 with the three sets of SRS parameters, srs-ConfigApDCI-Format4, configured by higher layer signalling. For the 2-bit SRS request field [4] in Table 8.2-0C and DCI format 3B, and UE configured with more than 5 TDD serving cells without PUSCH/PUCCH transmission, SRS parameters, srs-ConfigApDCI-Format1a2b2c, configured by higher layer signalling for the associated serving cell, is used if type 1/2 SRS is triggered. For the 2-bit SRS request field [4] in Table 8.2-0C and DCI format 3B, and UE configured with more than 5 TDD serving cells without PUSCH/PUCCH transmission, if the UE receives an SRS request field with value '00', the DCI does not indicate type 1/2 SRS trigger, but the UE shall apply the power control commands received in the DCI format 3B according to Clause 5.1.3.1.

Table 8.1-1: SRS request value for trigger type 1/2 in DCI format 4/7-0B, or trigger type 1 in DCI format 4A/4B

| Value of SRS request field | Description |
| --- | --- |
| '00' | No type 1/2 SRS trigger |
| '01' | The 1st SRS parameter set configured by higher layers |
| '10' | The 2nd SRS parameter set configured by higher layers |
| '11' | The 3rd SRS parameter set configured by higher layers |

Table 8.2-0A: SRS request value for trigger type 1 in DCI format 0B

| Value of SRS request field | Description |
| --- | --- |
| '00' | No type 1 SRS trigger |
| '01' | Type 1 SRS trigger and first scheduled PUSCH subframe |
| '10' | Type 1 SRS trigger and second scheduled PUSCH subframe |
| '11' | Type 1 SRS trigger and last scheduled PUSCH subframe |

Table 8.2-0C: SRS request value for trigger type 1/2 in DCI format 3B and for UE configured with more than 5 TDD serving cells without PUSCH/PUCCH transmission

| Value of SRS request field | Description |
| --- | --- |
| '00' | No type 1/2 SRS trigger for a 1st set of serving cells configured by higher layers |
| '01' | Type 1/2 SRS trigger for a 2nd set of serving cells configured by higher layers |
| '10' | Type 1/2 SRS trigger for a 3rd set of serving cells configured by higher layers |
| '11' | Type 1/2 SRS trigger for a 4th set of serving cells configured by higher layers |

For all DCI formats with type 1/2 SRS trigger, each SRS parameter set contains one trigger type 1 and/or one trigger type 2 SRS configuration. When a SRS parameter set is triggered with the 1-bit SRS request set to 1 (for DCI formats with 1-bit SRS request field) or with the corresponding SRS request field value signalled (for DCI formats with 2-bits SRS request field), the configured trigger type 1 and/or trigger type 2 SRS is transmitted according to their respective configurations.

For a serving cell that is not a LAA SCell, the serving cell specific SRS transmission bandwidths  are configured by higher layers. The allowable values are given in Clause 5.5.3.2 of [3].

For a serving cell that is not a LAA SCell, the serving cell specific SRS transmission sub-frames are configured by higher layers. The allowable values are given in Clause 5.5.3.3 of [3].

For a TDD serving cell, trigger type 0 and 1 SRS transmissions can occur in UpPTS and uplink subframes of the UL/DL configuration indicated by the higher layer parameter subframeAssignment for the serving cell. Trigger type 2 SRS transmissions can occur in uplink subframes of the UL/DL configuration indicated by the higher layer parameter subframeAssignment for the serving cell except the last symbol of a subframe.

For trigger type 0 and type 1 SRS transmission, when closed-loop or open-loop UE transmit antenna selection is enabled for a given serving cell for a UE that supports transmit antenna selection, or for a UE that can be configured with ue-TxAntennaSelection-SRS-1T4R-Config or ue-TxAntennaSelection-SRS-2T4R-NrOfPairs,

when higher layer parameter 'ue-TxAntennaSelection-SRS-1T4R-Config' is configured for a given serving cell, the index $ a\left ( n_{SRS}\right ) $, of the UE antenna that transmits the SRS at time nSRS is given by

$ a\left ( n_{SRS}\right ) =n_{SRS}mod4 $, for both partial and full sounding bandwidth, and when frequency hopping is disabled (i.e., $ b_{hop}\geq  B_{SRS}$),

$$ a\left ( n_{SRS}\right ) ={\begin {matrix}\left ( n_{SRS}+\lfloor  \frac {n_{SRS}}{max\left ( 4,K\right ) }\rfloor  +\beta  \left ( \lfloor  \frac {n_{SRS}}{4}\rfloor  mod\lfloor  \frac {max\left ( 4,K\right ) }{4}\rfloor  \right ) \right ) mod 4, & whenKis even \\ n_{SRS}mod 4, & otherwise\end {matrix}$$

with $\beta  ={\begin {matrix}1, & ifN_{1}=2,N_{2}=2 \\ 0, & otherwise\end {matrix}$, when frequency hopping is enabled (i.e., $ b_{hop}<B_{SRS}$).

when higher layer parameter 'ue-TxAntennaSelection-SRS-2T4R-NrOfPairs' is configured for a given serving cell for a UE configured with $\Lambda  $ UE antenna pairs, where $\Lambda  =\{2 or 3\}$ is given by higher layer parameter 'ue-TxAntennaSelection-SRS-2T4R-NrOfPairs', the index $ a\left ( n_{SRS}\right ) $ for the UE antenna pair as $\left \{ 2a\left ( n_{SRS}\right ) , 2a\left ( n_{SRS}\right ) +1\right \} $ when $\Lambda  $ =2, or $\left \{ 0, a\left ( n_{SRS}\right ) +1\right \} $ when $\Lambda  $ =3 that transmits the SRS at time nSRS is given by

$ a\left ( n_{SRS}\right ) =n_{SRS}mod\Lambda  $ for both partial and full sounding bandwidth, and when frequency hopping is disabled (i.e., $ b_{hop}\geq  B_{SRS}$),

with $\beta  ={\begin {matrix}1, & ifKmod\Lambda  ^{2}=0 \\ 0, & otherwise\end {matrix}$ , when frequency hopping is enabled (i.e., $ b_{hop}<B_{SRS}$).

- otherwise, the index , of the UE antenna that transmits the SRS at time nSRS is given by

, for both partial and full sounding bandwidth, and when frequency hopping is disabled (i.e., ),

,

when frequency hopping is enabled (i.e., ),

where values BSRS, bhop, Nb, and nSRS are given in Clause 5.5.3.2 of [3], and (where  regardless of the  value), except when a single SRS transmission is configured for the UE. If a UE is configured with more than one serving cell, and for a group of cells belonging to bands that are signalled to be switched together in txAntennaSwitchUL the UE is not expected to transmit SRS on different antenna ports simultaneously. If a UE is configured with more than one serving cell, and for a group of cells belonging to bands that are signalled to be switched together in txAntennaSwitchUL the UE is not expected to transmit SRS and PUSCH on different antenna ports simultaneously.

For trigger type 2 SRS transmission, when closed-loop or open-loop UE transmit antenna selection is enabled for a given serving cell for a UE that supports antenna selection, or for UE that can be configured with ue-TxAntennaSelection-SRS-1T4R-Config or ue-TxAntennaSelection-SRS-2T4R-NrOfPairs, the index $ a\left ( n_{SRS}\right ) $ of the UE antenna that transmits the SRS at time nSRS is given by $ a\left ( n_{SRS}\right ) =n_{SRS}$ when frequency hopping is disabled, and $ a\left ( n_{SRS}\right ) =\lfloor  \frac {n_{SRS}}{N_{FH}}\rfloor  $ when frequency hopping is enabled, where $ N_{FH}$ is the number of frequency hops defined in Clause 5.5.3.2.2 of [3]. The UE is not expected to be configured with $ a\left ( n_{SRS}\right ) \geq  N_{AS}$ and

- when higher layer parameter 'ue-TXAntennaSelection-SRS-1T4R-Config' is configured for a given serving cell, the number of antenna switches $ N_{AS}$ = 4.

- when higher layer parameter 'ue-TXAntennaSelection-SRS-2T4R-NrOfPairs' is configured for a given serving cell for a UE configured with $\Lambda  $ UE antenna pairs, where $\Lambda  =\{2 or 3\}$ is given by higher layer parameter 'ue-TXAntennaSelection-SRS-2T4R-NrOfPairs', the number of antenna switches $ N_{AS}$ = $\Lambda  $, and the index for the UE antenna pair that transmits the SRS at time $ n_{SRS}$ is $\left \{ 2a\left ( n_{SRS}\right ) , 2a\left ( n_{SRS}\right ) +1\right \} $ when $\Lambda  $ =2, or $\left \{ 0, a\left ( n_{SRS}\right ) +1\right \} $ when $\Lambda  $ =3.

- otherwise, the number of antenna switches $ N_{AS}$ = 2.

When higher layer parameter 'ue-TxAntennaSelection-SRS-1T4R-Config' is configured or 'ue-TxAntennaSelection-SRS-2T4R-NrOfPairs' is configured for a serving cell, a UE is not expected to be configured with more than two antenna ports for any uplink physical channel or signal on that serving cell.

A UE may be configured to transmit SRS on  antenna ports of a serving cell where may be configured by higher layer signalling. For PUSCH transmission mode 1 and for PUSCH transmission mode 2  with two antenna ports configured for PUSCH and  with 4 antenna ports configured for PUSCH. A UE configured for SRS transmission on multiple antenna ports of a serving cell shall transmit SRS for all the configured transmit antenna ports within one SC-FDMA symbol of the same subframe of the serving cell. 
The SRS transmission bandwidth and starting physical resource block assignment are the same for all the configured antenna ports of a given serving cell. The UE does not support a value of ![](media_svg/image171.svg) [公式≈: ^{K}TC] set to '4', if the UE is configured for SRS transmission on 4 antenna ports of a serving cell.

If a UE is not configured with multiple TAGs and the UE is not configured with the parameter srs-UpPtsAdd for trigger type 1 and the UE is not configured with trigger type 2 SRS transmission, or if a UE is not configured with multiple TAGs and the UE is not configured with more than one serving cell of different CPs and the UE is not configured with trigger type 2 SRS transmission, or if a UE is configured for PUSCH transmission in UpPTS and a SRS transmission overlaps with a PUSCH transmission on the same symbol in UpPTS within a TDD serving cell, the UE shall not transmit trigger type 0/1 SRS in a symbol whenever SRS and PUSCH transmissions happen to overlap in the same symbol, except when the SRS is on a TDD serving cell not configured for PUSCH/PUCCH transmission.

For the case when a trigger type 0/1 SRS transmission in a first serving cell happens to overlap in the same symbol as a PUSCH transmission in a second serving cell, and the first and second serving cells are in the same TAG, same band, and use the same cyclic prefix, the UE may drop the trigger type 0/1 SRS transmission.

For the case when a trigger type 2 SRS transmission in a first serving cell happens to overlap in the same symbol as the PUSCH/PUCCH transmission in a second serving cell, and the first and second serving cells are in the same TAG, same band, and use the same cyclic prefix, the UE may drop the trigger type 2 SRS transmission in the overlapped symbol.

For TDD serving cell, and UE not configured with additional SC-FDMA symbols in UpPTS, when one SC-FDMA symbol exists in UpPTS of the given serving cell, it can be used for SRS transmission, when two SC-FDMA symbols exist in UpPTS of the given serving cell, both can be used for SRS transmission and for trigger type 0 SRS both can be assigned to the same UE. For TDD serving cell, and if the UE is configured with two or four additional SC-FDMA symbols in UpPTS of the given serving cell, all can be used for SRS transmission and for trigger type 0 SRS at most two SC-FDMA symbols out of the configured additional SC-FDMA symbols in UpPTS can be assigned to the same UE, except for UE not configured for PUSCH/PUCCH transmission or for UE supporting ce-srsEnhancement-r14, where all can be assigned to the same UE. A UE is not expected to be configured with trigger type 2 SRS in UpPTS.

If a UE is not configured with multiple TAGs and the UE is not configured with the parameter srs-UpPtsAdd for trigger type 1 and the UE is not configured with trigger type 2 SRS transmission, or if a UE is not configured with multiple TAGs and the UE is not configured with more than one serving cell of different CPs and the UE is not configured with trigger type 2 SRS transmission, or if a UE is configured with multiple TAGs and trigger type 0/1 SRS and PUCCH format 2/2a/2b happen to coincide in the same subframe in the same serving cell, except when the SRS is on a TDD serving cell not configured for PUSCH/PUCCH transmission,

- The UE shall not transmit type 0 triggered SRS whenever type 0 triggered SRS and PUCCH format 2/2a/2b transmissions happen to coincide in the same subframe;

- The UE shall not transmit type 1 triggered SRS whenever type 1 triggered SRS and PUCCH format 2a/2b or format 2 with HARQ-ACK transmissions happen to coincide in the same subframe;

- The UE shall not transmit PUCCH format 2 without HARQ-ACK whenever type 1 triggered SRS and PUCCH format 2 without HARQ-ACK transmissions happen to coincide in the same subframe.

If a UE is not configured with multiple TAGs and the UE is not configured with the parameter srs-UpPtsAdd for trigger type 1 and the UE is not configured with trigger type 2 SRS transmission, or if a UE is not configured with multiple TAGs and the UE is not configured with more than one serving cell of different CPs and the UE is not configured with trigger type 2 SRS transmission, or if a UE is configured with multiple TAGs and trigger type 0/1 SRS and PUCCH happen to coincide in the same subframe/slot/subslot in the same serving cell, except when the SRS is on a TDD serving cell not configured for PUSCH/PUCCH transmission,

- The UE shall not transmit trigger type 0/1 SRS whenever SRS transmission and PUCCH transmission carrying HARQ-ACK and/or positive SR happen to coincide in the same subframe/slot/subslot if the parameter ackNackSRS-SimultaneousTransmission is FALSE;

- For FDD-TDD and primary cell frame structure 1, the UE shall not transmit trigger type 0/1 SRS in a symbol whenever SRS transmission and PUCCH transmission carrying HARQ-ACK and/or positive SR using shortened format as defined in Clauses 5.4.1, 5.4.2A, 5.4.2B, 5.4.2C, and 5.4A of [3] happen to overlap in the same symbol if the parameter ackNackSRS-SimultaneousTransmission is TRUE.

- Unless otherwise prohibited, the UE shall transmit trigger type 0/1 SRS whenever SRS transmission and PUCCH transmission carrying HARQ-ACK and/or positive SR using shortened format as defined in Clauses 5.4.1, 5.4.2A, and 5.4A of [3] happen to coincide in the same subframe/slot/subslot if the parameter ackNackSRS-SimultaneousTransmission is TRUE.

If a UE is not configured with multiple TAGs and the UE is not configured with the parameter srs-UpPtsAdd for trigger type 1 and the UE is not configured with trigger type 2 SRS transmission, or if a UE is not configured with multiple TAGs and the UE is not configured with more than one serving cell of different CPs and the UE is not configured with trigger type 2 SRS transmission, the UE shall not transmit SRS whenever SRS transmission on any serving cells and PUCCH transmission carrying HARQ-ACK and/or positive SR using normal PUCCH format as defined in Clauses 5.4.1, 5.4.2A, and 5.4A of [3] happen to coincide in the same subframe/slot/subslot.

In UpPTS, whenever SRS transmission instance overlaps with the PRACH region for preamble format 4 or exceeds the range of uplink system bandwidth configured in the serving cell, the UE shall not transmit SRS.

For a TDD serving cell d not configured for PUSCH/PUCCH transmission, denote as s0(d) the corresponding serving cell whose UL transmissions may be interrupted as signalled by srs-SwitchFromServCellIndex. Define the set S(d)= {s0(d)… sN-1(d)} as the set of serving cells that meet the all the following conditions:

- {s0(d)… sN-1(d)} are in the same band as s0(d).

- {s0(d)… sN-1(d)} have the same CP as s0(d).

- {s0(d)… sN-1(d)} are in the same TAG as s0(d).

The following prioritization rules shall be applied in case of collision between a transmission of SRS over serving cell d and transmission of a physical signal/channel over a serving cell in set S(d):

- If PUSCH/PUCCH transmission carrying HARQ-ACK/positive SR/RI/PTI/CRI/wideband PMI only (PUCCH reporting type 2a in Clause 7.2.2) and/or PRACH on a serving cell in set S(d) overlaps in the same symbol with the SRS transmission (including any interruption due to uplink or downlink RF retuning time [10]) on serving cell d, then the UE shall not transmit trigger type 0/1 SRS or drop the overlapped symbol(s) of type 2 SRS (including any interruption due to uplink or downlink RF retuning time [10]). Otherwise,

- if PUSCH transmission carrying aperiodic CSI on a serving cell in set S(d) overlaps in the same symbol with the SRS transmission (including any interruption due to uplink or downlink RF retuning time [10]) in serving cell d, and if the SRS transmission is a type 0 SRS transmission, then the UE shall not transmit the type 0 SRS. Otherwise,

- if PUSCH transmission on a serving cell in set S(d) overlaps in more than one symbol with the SRS transmission (including any interruption due to uplink or downlink RF retuning time [10]) in serving cell d, then the UE shall drop the PUSCH transmission. If PUCCH/trigger type 0/1 SRS transmission on a serving cell in set S(d) overlaps in the same symbol with the SRS transmission (including any interruption due to uplink or downlink RF retuning time [10]) on serving cell d, the UE shall drop the PUCCH/trigger type 0/1 SRS transmission. If a subset of symbol(s) for type 2 SRS transmission on a serving cell in set S(d) overlaps with the SRS transmission (including any interruption due to uplink or downlink RF retuning time [10]) on serving cell d, the UE shall drop the subset of the symbol(s) for type 2 SRS on a serving cell in set S(d).

In case an SRS transmission in subframe N on serving cell d is dropped due to a collision with a higher priority transmission (as defined above) in subframe N+1, and there is a lower priority transmission (as defined above) in subframe N that would have been dropped had the transmission in subframe N+1 not occurred, the UE is not required to transmit the lower priority transmission in subframe N.

The UE is not expected to be triggered to transmit type 2 SRS on serving cell d in subframe N that overlaps (including any interruption due to uplink or downlink RF retuning time [10]) with uplink subframe N-1 on a serving cell in set S(d).

The parameter ackNackSRS-SimultaneousTransmission provided by higher layers determines if a UE is configured to support the transmission of HARQ-ACK on PUCCH and SRS in one subframe/slot/subslot. If it is configured to support the transmission of HARQ-ACK on PUCCH and SRS in one subframe/slot/subslot, then in the cell specific SRS subframes of the primary cell in case of subframe-PUCCH or in the last slot/subslot of the cell specific SRS subframes of the primary cell in case of slot/subslot-PUCCH,

- if the UE transmits PUCCH format 1/1a/1b/3, the UE shall transmit HARQ-ACK and SR using the shortened PUCCH format as defined in Clauses 5.4.1, 5.4.2A, and 5.4A.3 of [3], where the HARQ-ACK or the SR symbol corresponding to the SRS location in the last symbol of the subframe is punctured.

- If the UE transmits PUCCH format 4/5 partly or fully overlapping with the cell specific SRS bandwidth in the cell specific SRS subframes of the primary cell, then UE shall transmit UCI using the shortened PUCCH format as defined in Clauses 5.4.2B, 5.4.2C, and 5.4A.4 of [3].

For PUCCH format 1/1a/1b/3, this shortened PUCCH format shall be used in a cell specific SRS subframe or the last slot/subslot of the cell specific SRS subframe of the primary cell even if the UE does not transmit SRS in that subframe. For PUCCH format 4/5, this shortened PUCCH format shall be used if the PUCCH transmission partly or fully overlaps with the cell-specific SRS bandwidth in the cell specific SRS subframes or the last slot/subslot of the cell specific SRS subframes of the primary cell even if the UE does not transmit SRS in that subframe, or if the UE transmits SRS in the last symbol of that subframe even if the PUCCH format 4/5 does not partly or fully overlap with the cell-specific SRS. The cell specific SRS subframes are defined in Clause 5.5.3.3 of [3]. Otherwise, the UE shall use the normal PUCCH format 1/1a/1b as defined in Clause 5.4.1, and 5.4A.2 of [3] or normal PUCCH format 3 as defined in Clause 5.4.2A, and 5.4A.3 or normal PUCCH format 4 as defined in Clause 5.4.2B, and 5.4A.4 or normal PUCCH format 5 as defined in Clause 5.4.2C of [3].

For a BL/CE UE not configured with the higher layer parameter srs-UpPtsAdd, for a SRS transmission in subframe n and if the UE transmits PUSCH/PUCCH in subframe n and/or n+1, the UE shall not transmit the SRS in subframe n if the SRS transmission bandwidth in subframe n is not completely within the narrowband of PUSCH/PUCCH in subframe n and/or n+1

A BL/CE UE not configured with the higher layer parameter srs-UpPtsAdd shall not transmit SRS in UpPTS if SRS frequency location is different from DwPTS reception narrowband in the same special subframe.

For a BL/CE UE, the SRS transmission that falls into the reserved symbol of a BL/CE UL subframe is dropped.

For a TDD serving cell, ![](media_svg/image198.svg) [公式≈: ^{c}1], not configured for PUSCH/PUCCH transmission, the UE is not expected to be configured with SRS resource(s) such that the SRS transmission (including any interruption due to uplink or downlink RF retuning time [10]) may overlap in time with PDCCH monitoring in subframes 0 or 5 on serving cell ![](media_svg/image199.svg) [公式≈: ^{c}2], if the UE is not capable of simultaneous transmission and reception on serving cell ![](media_svg/image198.svg) [公式≈: ^{c}1] and serving cell ![](media_svg/image200.svg) [公式≈: ^{c}2].

Trigger type 0 SRS configuration of a UE in a serving cell for SRS periodicity,, and SRS subframe offset,, is defined in Table 8.2-1 and Table 8.2-2, for FDD and TDD serving cell, respectively. The periodicity  of the SRS transmission is serving cell specific and is selected from the set {2, 5, 10, 20, 40, 80, 160, 320} ms or subframes. 
For the SRS periodicity  of 2 ms in TDD serving cell configured for PUSCH and/or PUCCH transmission, two SRS resources are configured in a half frame containing UL subframe(s) of the given serving cell. For the SRS periodicity  of 2 ms in TDD serving cell not configured for PUSCH/PUCCH transmission, two or more SRS resources are configured in a half frame containing UL subframe(s) of the given serving cell.

Type 0 triggered SRS transmission instances in a given serving cell for TDD serving cell with  and for FDD serving cell are the subframes satisfying , where for FDD  is the subframe index within the frame, for TDD serving cell, if the UE is configured with the parameter srs-UpPtsAdd for trigger type 0,  is defined in Table 8.2-6; otherwise  is defined in Table 8.2-3. The SRS transmission instances for TDD serving cell with  are the subframes satisfying .

For TDD serving cell, and a UE configured for type 0 triggered SRS transmission in serving cell c, and the UE configured with the parameter EIMTA-MainConfigServCell-r12 for serving cell c, if the UE does not detect an UL/DL configuration indication for radio frame m (as described in Clause 13.1), the UE shall not transmit trigger type 0 SRS in a subframe of radio frame m that is indicated by the parameter eimta-HARQ-ReferenceConfig-r12 as a downlink subframe unless the UE transmits PUSCH in the same subframe.

For a serving cell that is not a LAA SCell, trigger type 1 SRS configuration of a UE in a serving cell for SRS periodicity,, and SRS subframe offset,, is defined in Table 8.2-4 and Table 8.2-5, for FDD and TDD serving cell, respectively; and trigger type 2 SRS configuration of a UE in a serving cell for SRS periodicity, , and SRS subframe offset,, is defined in Table 8.2-5, for TDD serving cell. The periodicity  of the SRS transmission is serving cell specific and is selected from the set {2, 5, 10} ms or subframes. 
For the SRS periodicity  of 2 ms in TDD serving cell configured for PUSCH and/or PUCCH transmission, two SRS resources are configured in a half frame containing UL subframe(s) of the given serving cell. For the SRS periodicity  of 2 ms in TDD serving cell not configured for PUSCH/PUCCH transmission, two or more SRS resources are configured in a half frame containing UL subframe(s) of the given serving cell.

For TDD serving cell configured for PUSCH and/or PUCCH transmission, and a UE configured for type 1/2 triggered SRS transmission in serving cell c and configured with the parameter srs-UpPtsAdd, the UE is not expected to receive trigger type 1/2 SRS configurations with SRS periodicity  of 2 ms.

A UE configured for type 1/2 triggered SRS transmission in serving cell c and not configured with a carrier indicator field shall transmit SRS on serving cell c upon detection of a positive SRS request in PDCCH/EPDCCH/MPDCCH/SPDCCH scheduling PUSCH/PDSCH on serving cell c.

A UE configured for type 1/2 triggered SRS transmission in serving cell c and configured with a carrier indicator field shall transmit SRS on serving cell c upon detection of a positive SRS request in PDCCH/EPDCCH/SPDCCH scheduling PUSCH/PDSCH with the value of carrier indicator field corresponding to serving cell c.

For a serving cell that is not a LAA SCell, a non-BL/CE UE configured for type 1/2 triggered SRS transmission on serving cell c upon detection of a positive SRS request in subframe n, slot 2n or slot 2n+1 of serving cell c shall commence SRS transmission in the first subframe satisfying ![](media_svg/image212.svg) [公式: n+k,k÷k_{p}], and

- ![](media_svg/image213.svg) [公式: k_{p}=2] if the positive SRS request in PDCCH/SPDCCH with DCI format 7-0A/7-1A is detected in slot 2n or slot 2n+1, for TDD

- ![](media_svg/image214.svg) [公式: k_{p}=3] if the UE is configured with higher layer parameter shortProcessingTime and the corresponding PDCCH with CRC scrambled by C-RNTI with DCI format other than DCI format 7-0A/7-0B/7-1E/7-1F/7-1G is in the UE-specific search space,

- ![](media_svg/image215.svg) [公式: k_{p}=4]otherwise, and

for TDD serving cell c with  and for FDD serving cell c,

for TDD serving cell c with

where for FDD serving cell c  is the subframe index within the frame , for TDD serving cell c, if the UE is configured with the parameter srs-UpPtsAdd for trigger type 1,  is defined in Table 8.2-6; otherwise  is defined in Table 8.2-3. For a TDD serving cell not configured for PUSCH/PUCCH transmission and the positive SRS request detected in PDCCH/EPDCCH scheduling PDSCH and the UE configured with soundingRS-FlexibleTiming-r14 by higher layer signalling, if the trigger type 1 SRS transmission (including any interruption due to uplink or downlink RF retuning time [10]) in the first subframe  happens to overlap with a HARQ-ACK transmission for any serving cell, the UE shall commence trigger type 1 SRS transmission in subframe n + k + l, where l = max( 5, ). The soundingRS-FlexibleTiming-r14 if configured by higher layer signaling is not applied to trigger type 2 SRS.

For a type 1/2 SRS triggered for more than one TDD serving cell in DCI format 3B and UE configured with more than 5 TDD serving cells without PUSCH/PUCCH transmission, the order of the triggered SRS transmission on the serving cells follow the order of the serving cells in the indicated set of serving cells configured by higher layers. For a type 1/2 SRS triggered for more than one TDD serving cell in DCI format 3B and UE configured with no more than 5 TDD serving cells without PUSCH/PUCCH transmission, the order of the triggered SRS transmission on the serving cells follow the order of the serving cells with type 1/2 SRS triggered in the DCI. The SRS resource for the n-th (n>=2) SRS transmission is determined such that it is the first SRS resource on or after the SRS resource for the (n-1)-th SRS transmission provided it does not collide with any previous SRS transmission triggered in the DCI format 3B, or interruption due to UL or DL RF retuning time [10].

For a serving cell c that is a LAA SCell, a UE configured for type 1 triggered SRS transmission on serving cell c upon detection of a positive SRS request in subframe n of serving cell c shall commence SRS transmission, conditioned on the channel access procedures described in clause 4.2.1 of [13], in subframe ![](media_svg/image222.svg) [公式: n+k], where

![](media_svg/image223.svg) [公式: k]corresponds to the scheduled PUSCH subframe determined in Clause 8.0 if SRS is triggered in DCI format 0A/4A,

![](media_svg/image223.svg) [公式: k]is determined from Table 8.2-0A and the corresponding scheduled PUSCH subframe determined in Clause 8.0 if SRS is triggered in DCI format 0B,

![](media_svg/image224.svg) [公式: k=m+mod(l,N)] where the value of l is determined from SRS subframe parameter for the indicated SRS parameter set in Table 8.1, ![](media_svg/image225.svg) [公式: m]is determined from the first scheduled PUSCH subframe determined in Clause 8.0 and N is determined by the procedure in Clause 8.0 if SRS is triggered in DCI format 4B,

![](media_svg/image226.svg) [公式: k=3+l]where the value of l is determined by the SRS timing offset field in the corresponding DCI if SRS is triggered in DCI format 1A/2B/2C/2D according to Table 8.2-0B.

Table 8.2-0B: ![](media_svg/image227.svg) [公式: l] for SRS trigger type 1/2 in DCI format 1A/2B/2C/2D

| Value of SRS timing offset field | ![](media_svg/image227.svg) [公式: l] |
| --- | --- |
| '000' | No type 1/2 SRS trigger |
| '001' | 1 |
| '010' | 2 |
| '011' | 3 |
| '100' | 4 |
| '101' | 5 |
| '110' | 6 |
| '111' | 7 |

A BL/CE UE configured for type 1 triggered SRS transmission on serving cell c upon detection of a positive SRS request of serving cell c shall commence SRS transmission in the first subframe satisfying $ n+k+K_{offset}$, $ k\geq  4 $, where subframe n is the last subframe in which the DCI format 6-0A/6-1A with the positive SRS request is transmitted, and

for TDD serving cell c with  and for FDD serving cell c,

for TDD serving cell c with  where for FDD serving cell c  is the subframe index within the frame , for TDD serving cell c , if the UE is configured with the parameter srs-UpPtsAdd for trigger type 1,  is defined in Table 8.2-6; otherwise  is defined in Table 8.2-3.

A UE configured for type 1/2 triggered SRS transmission is not expected to receive type 1/2 SRS triggering events associated with different values of trigger type 1/2 SRS transmission parameters, as configured by higher layer signalling, for the same subframe and the same serving cell.

For a serving cell that is a LAA SCell, a UE configured for type 1 triggered SRS transmission is not expected to receive type 1 SRS triggering event in DCI format 0B associated with a subframe that is not scheduled for PUSCH transmission for the same serving cell.

For a serving cell that is an LAA SCell, if the uplink transmission in a subframe is ending in the end of symbol #3 or in the end of symbol #6, the UE shall not transmit SRS in that subframe.

A UE configured for type 2, type 1, or type 0 triggered SRS transmission and more than one TDD serving cell without PUSCH/PUCCH transmission is not expected to receive type 2, type 1, or type 0 SRS triggering events that can result in uplink transmissions beyond the UE's indicated uplink carrier aggregation capability included in the UE-EUTRA-Capability [12].

For TDD serving cell c, and a UE configured with EIMTA-MainConfigServCell-r12 for a serving cell c, the UE shall not transmit SRS in a subframe of a radio frame that is indicated by the corresponding eIMTA-UL/DL-configuration as a downlink subframe.

A UE shall not transmit SRS whenever SRS and a PUSCH transmission corresponding to a Random Access Response Grant or a retransmission of the same transport block as part of the contention based random access procedure coincide in the same subframe.

A UE not configured with higher layer parameter ul-STTI-Length is not expected to be triggered with trigger type 2 SRS transmission in the same subframe as a PUSCH/PUCCH transmission in the same serving cell.

A UE configured with higher layer parameter ul-STTI-Length shall drop the trigger type 2 SRS transmission in the overlapped symbol when the trigger type 2 SRS transmission and slot PUSCH/PUCCH transmission happens to overlap in the same symbol and same serving cell.

A UE shall not transmit trigger type 2 SRS when trigger type 2 SRS transmission and PRACH happen to overlap in the same subframe and same serving cell.

Table 8.2-1: UE Specific SRS Periodicity  and Subframe Offset Configuration 
 for trigger type 0, FDD

| SRS Configuration Index ISRS | SRS Periodicity  (ms) | SRS Subframe Offset |
| --- | --- | --- |
| 0 – 1 | 2 | ISRS |
| 2 – 6 | 5 | ISRS – 2 |
| 7 – 16 | 10 | ISRS – 7 |
| 17 – 36 | 20 | ISRS – 17 |
| 37 – 76 | 40 | ISRS – 37 |
| 77 – 156 | 80 | ISRS – 77 |
| 157 – 316 | 160 | ISRS – 157 |
| 317 – 636 | 320 | ISRS – 317 |
| 637 – 1023 | reserved | reserved |

Table 8.2-2: UE Specific SRS Periodicity  and Subframe Offset Configuration 
 for trigger type 0, TDD

| SRS Configuration Index ISRS | SRS Periodicity  (ms) | SRS Subframe Offset |
| --- | --- | --- |
| 0 | 2 | 0, 1 |
| 1 | 2 | 0, 2 |
| 2 | 2 | 1, 2 |
| 3 | 2 | 0, 3 |
| 4 | 2 | 1, 3 |
| 5 | 2 | 0, 4 |
| 6 | 2 | 1, 4 |
| 7 | 2 | 2, 3 |
| 8 | 2 | 2, 4 |
| 9 | 2 | 3, 4 |
| 10 – 14 | 5 | ISRS – 10 |
| 15 – 24 | 10 | ISRS – 15 |
| 25 – 44 | 20 | ISRS – 25 |
| 45 – 84 | 40 | ISRS – 45 |
| 85 – 164 | 80 | ISRS – 85 |
| 165 – 324 | 160 | ISRS – 165 |
| 325 – 644 | 320 | ISRS – 325 |
| 645 – 1023 | reserved | reserved |

Table 8.2-3:  for TDD

|  | subframe index n |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 |  | 2 | 3 | 4 | 5 | 6 |  | 7 | 8 | 9 |
|  |  | 1st symbol of UpPTS | 2nd symbol of UpPTS |  |  |  |  | 1st symbol of UpPTS | 2nd symbol of UpPTS |  |  |  |
| in case UpPTS length of 2 symbols |  | 0 | 1 | 2 | 3 | 4 |  | 5 | 6 | 7 | 8 | 9 |
| in case UpPTS length of 1 symbol |  | 1 |  | 2 | 3 | 4 |  | 6 |  | 7 | 8 | 9 |

Table 8.2-4: UE Specific SRS Periodicity  and Subframe Offset Configuration 
 for trigger type 1, FDD

| SRS Configuration Index  ISRS | SRS Periodicity   (ms) | SRS Subframe Offset |
| --- | --- | --- |
| 0 – 1 | 2 | ISRS |
| 2 – 6 | 5 | ISRS – 2 |
| 7 – 16 | 10 | ISRS – 7 |
| 17 – 31 | reserved | reserved |

Table 8.2-5: UE Specific SRS Periodicity  and Subframe Offset Configuration 
 for trigger type 1/2, TDD

| SRS Configuration Index  ISRS | SRS Periodicity   (ms) | SRS Subframe Offset |
| --- | --- | --- |
| 0 | reserved | reserved |
| 1 | 2 | 0, 2 |
| 2 | 2 | 1, 2 |
| 3 | 2 | 0, 3 |
| 4 | 2 | 1, 3 |
| 5 | 2 | 0, 4 |
| 6 | 2 | 1, 4 |
| 7 | 2 | 2, 3 |
| 8 | 2 | 2, 4 |
| 9 | 2 | 3, 4 |
| 10 – 14 | 5 | ISRS – 10 |
| 15 – 24 | 10 | ISRS – 15 |
| 25 – 31 | reserved | reserved |

Table 8.2-6:  for TDD and UE configured with two or four additional SC-FDMA symbols in UpPTS

|  | subframe index n |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 |  |  |  | 2 | 3 | 4 | 5 | 6 |  |  |  | 7 | 8 | 9 |
|  |  | 1st symbol of UpPTS | 2nd symbol of UpPTS | 3rd symbol of UpPTS | 4th symbol of UpPTS |  |  |  |  | 1st symbol of UpPTS | 2nd symbol of UpPTS | 3rd symbol of UpPTS | 4th symbol of UpPTS |  |  |  |
| in case UpPTS length of 4 symbols |  | 0 | 1 | 2 | 3 |  |  |  |  | 5 | 6 | 7 | 8 |  |  |  |
| in case UpPTS length of 2 symbols |  | 2 | 3 |  |  |  |  |  |  | 7 | 8 |  |  |  |  |  |

## 8.3 UE HARQ-ACK procedure

For FDD, and serving cell with frame structure type 1, an HARQ-ACK received on the PHICH assigned to a UE in subframe i is associated with the PUSCH transmission in subframe i-4.

For FDD-TDD, and serving cell with frame structure type 1, and UE not configured to monitor PDCCH/EPDCCH in another serving cell with frame structure type 2 for scheduling the serving cell, an HARQ-ACK received on the PHICH assigned to a UE in subframe i is associated with the PUSCH transmission in subframe i-4.

For FDD-TDD, if a serving cell is a secondary cell with frame structure type 1 and if the UE is configured to monitor PDCCH/EPDCCH in another serving cell with frame structure type 2 for scheduling the serving cell, then an HARQ-ACK received on the PHICH assigned to a UE in subframe i is associated with PUSCH transmission on the serving cell in subframe i-6.

For TDD, if the UE is not configured with EIMTA-MainConfigServCell-r12 for any serving cell and, if a UE is configured with one serving cell, or if the UE is configured with more than one serving cell and the TDD UL/DL configuration of all the configured serving cells is the same,

- For frame structure type 2 UL/DL configuration 1-6, an HARQ-ACK received on the PHICH assigned to a UE in subframe i is associated with the PUSCH transmission in the subframe i-k as indicated by the following Table 8.3-1 if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, otherwise as indicated by the following Table 8.3-2.

- For frame structure type 2 UL/DL configuration 0, an HARQ-ACK received on the PHICH in the resource corresponding to , as defined in Clause 9.1.2, assigned to a UE in subframe i is associated with the PUSCH transmission in the subframe i-k as indicated by the following Table 8.3-1 if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, otherwise as indicated by the following Table 8.3-2. For frame structure type 2 UL/DL configuration 0, an HARQ-ACK received on the PHICH in the resource corresponding to , as defined in Clause 9.1.2, assigned to a UE in subframe i is associated with the PUSCH transmission in the subframe i-6.

For TDD, if a UE is configured with more than one serving cell and the TDD UL/DL configuration of at least two configured serving cells is not the same, or if the UE is configured with EIMTA-MainConfigServCell-r12 for at least one serving cell, or FDD-TDD and serving cell is frame structure type 2,

- For serving cell with an UL-reference UL/DL configuration (defined in Clause 8.0) belonging to {1,2,3,4,5,6}, an HARQ-ACK received on the PHICH assigned to a UE in subframe i is associated with the PUSCH transmission in the subframe i-k for the serving cell as indicated by the following Table 8.3-1 if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, otherwise as indicated by the following Table 8.3-2, where "TDD UL/DL Configuration" in Table 8.3-1 and Table 8.3-2 refers to the UL-reference UL/DL Configuration.

- For a serving cell with UL-reference UL/DL configuration 0 (defined in Clause 8.0), an HARQ-ACK received on the PHICH in the resource corresponding to , as defined in Clause 9.1.2, assigned to a UE in subframe i is associated with the PUSCH transmission in the subframe i-k for the serving cell as indicated by the following Table 8.3-1 if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, otherwise as indicated by the following Table 8.3-2, where "TDD UL/DL Configuration" in Table 8.3-1 and Table 8.3-2 refers to the UL-reference UL/DL configuration. For a serving cell with UL-reference UL/DL configuration 0, an HARQ-ACK received on the PHICH in the resource corresponding to , as defined in Clause 9.1.2, assigned to a UE in subframe i is associated with the PUSCH transmission in the subframe i-6 for the serving cell.

- For FDD-TDD, if a serving cell is a secondary cell with UL-reference UL/DL configuration 0 and if the UE is configured to monitor PDCCH/EPDCCH in another serving cell with frame structure type 1 for scheduling the serving cell, for downlink subframe i, if a transport block was transmitted in the associated PUSCH subframe i-6 for the serving cell then PHICH resource corresponding to that transport block is not present in subframe i.

For a BL/CE UE, the UE is not expected to receive PHICH corresponding to a transport block.

If a UE is configured with a LAA SCell for UL transmissions, the UE is not expected to receive PHICH corresponding to a transport block on the LAA SCell.

For a serving cell, if a UE is configured with a higher layer parameter shortProcessingTime, the UE is not expected to receive PHICH corresponding to a transport block scheduled by an uplink scheduling grant via PDCCH in the UE-specific search space on the serving cell.

For a serving cell, if a UE is configured with a higher layer parameter shortTTI, the UE is not expected to receive PHICH corresponding to a transport block scheduled by an uplink scheduling grant via PDCCH/SPDCCH with uplink DCI format 7-0A/7-0B on the serving cell.

For a UE configured with EN-DC/NE-DC and serving cell frame structure type 1, if the UE is configured with tdm-PatternConfig/tdm-PatternConfigNE-DC or if the UE is configured with tdm-PatternConfig2 with EN-DC, for the serving cell, the UE is not expected to receive PHICH corresponding to a transport block on the serving cell and ACK for that transport block shall be delivered to the higher layers.

For a UE configured with EN-DC/NE-DC and serving cell frame structure type 1, if the UE is configured with tdm-PatternConfig/tdm-PatternConfigNE-DC or if the UE is configured with tdm-PatternConfig2 with EN-DC for the serving cell, UL grant in subframe n schedules the same UL HARQ process as that in subframe n-6.

Table 8.3-1: k for TDD configurations 0-6

| TDD UL/DL Configuration | subframe number i |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 0 | 7 | 4 |  |  |  | 7 | 4 |  |  |  |
| 1 |  | 4 |  |  | 6 |  | 4 |  |  | 6 |
| 2 |  |  |  | 6 |  |  |  |  | 6 |  |
| 3 | 6 |  |  |  |  |  |  |  | 6 | 6 |
| 4 |  |  |  |  |  |  |  |  | 6 | 6 |
| 5 |  |  |  |  |  |  |  |  | 6 |  |
| 6 | 6 | 4 |  |  |  | 7 | 4 |  |  | 6 |

Table 8.3-2: k for TDD configurations 0-6 and UE configured with symPUSCH-UpPts-r14

| TDD UL/DL Configuration | subframe number i |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 0 | 7 | 5,4 |  |  |  | 7 | 5,4 |  |  |  |
| 1 |  | 5,4 |  |  | 6 |  | 5,4 |  |  | 6 |
| 2 |  |  |  | 7,6 |  |  |  |  | 7,6 |  |
| 3 | 6 |  |  |  |  |  |  |  | 7,6 | 6 |
| 4 |  |  |  |  |  |  |  |  | 7,6 | 6 |
| 5 |  |  |  |  |  |  |  |  | 7,6 |  |
| 6 | 6,4 | 4 |  |  |  | 7,4 | 4 |  |  | 6 |

For a non-BL/CE UE, the physical layer in the UE shall deliver indications to the higher layers as follows:

For FDD with a UE not configured with tdm-PatternConfig/tdm-PatternConfigNE-DC/tdm-PatternConfig2, and for TDD with a UE configured with one serving cell, and for TDD with a UE configured with more than one serving cell and with TDD UL/DL configuration of all configured serving cells the same, and UE is not configured with EIMTA-MainConfigServCell-r12 for any serving cell, for downlink or special subframe i, if a transport block was transmitted in the associated PUSCH subframe then:

if ACK is decoded on the PHICH corresponding to that transport block in subframe i, or if that transport block is disabled by PDCCH/EPDCCH received in downlink or special subframe i, ACK for that transport block shall be delivered to the higher layers; else NACK for that transport block shall be delivered to the higher layers.

For TDD, if the UE is configured with more than one serving cell, and if at least two serving cells have different UL/DL configurations, or the UE is configured with EIMTA-MainConfigServCell-r12 for at least one serving cell, or for FDD-TDD, for downlink or special subframe i, if a transport block was transmitted in the associated PUSCH subframe then:

if ACK is decoded on the PHICH corresponding to that transport block in subframe i, or if that transport block is disabled by PDCCH/EPDCCH received in downlink or special subframe i, ACK for that transport block shall be delivered to the higher layers; or

if a PHICH resource corresponding to that transport block is not present in subframe i or if UE is not expected to receive PHICH corresponding to that transport block in subframe i, ACK for that transport block shall be delivered to the higher layers.

else NACK for that transport block shall be delivered to the higher layers.

## 8.3A Autonomous uplink feedback procedure

If the UE detects on the scheduling cell for an UL transmissions on an LAA SCell a transmission of DCI Format 0A/4A with the CRC scrambled by AUL C-RNTI carrying AUL-DFI, the UE shall use the autonomous uplink feedback information according to the following procedures:

- For each HARQ process configured for autonomous uplink transmission, the corresponding HARQ-ACK feedback is delivered to higher layers. For the HARQ processes not configured for autonomous uplink transmission, the corresponding HARQ-ACK feedback is not delivered to higher layers;

- For an uplink transmission in subframe n, the UE expects HARQ-ACK feedback in the AUL-DFI at earliest in subframe n+4;

- If the UE receives AUL-DFI in a subframe indicating ACK for a HARQ process, the UE is not expected to receive AUL-DFI indicating ACK for the same HARQ process prior to 4ms after the UE transmits another uplink transmission associated with that HARQ process;

- The "TPC for PUSCH' information is applied according to the procedures in clause 5.1;

- If present, the UE applies the TPMI field received in subframe n for autonomous uplink transmissions starting from subframe n+4. The UE is not expected to receive a TPMI that changes the number of transmission layers.

## 8.4 UE PUSCH hopping procedure

The UE shall perform PUSCH frequency hopping if the single bitFrequency Hopping (FH) field in a corresponding PDCCH/EPDCCH with DCI format 0 is set to 1 and the uplink resource block assignment is type 0 otherwise no PUSCH frequency hopping is performed.

A UE performing PUSCH frequency hopping shall determine its PUSCH Resource Allocation (RA) for the first slot of a subframe (S1) including the lowest index PRB () in subframe n from the resource allocation field in the latest PDCCH/EPDCCH with DCI format 0 for the same transport block.If there is no PDCCH/EPDCCH for the same transport block,the UE shall determine its hopping type based on

the hopping information in the most recent semi-persistent scheduling assignment PDCCH/EPDCCH, when the initial PUSCH for the same transport block is semi-persistently scheduled or

the random access response grant for the same transport block, when the PUSCH is initiated by the random access response grant.

The resource allocation field in DCI format 0 excludes either 1 or 2 bits used for hopping information as indicated by Table 8.4-1 below where the number of PUSCH resource blocks is defined as

For type 1 and type 2 PUSCH hopping,  if  is an odd number where  defined in [3].  in other cases. The size of the resource allocation field in DCI format 0 after excluding either 1 or 2 bits shall be , where NUL_hop = 1 or 2 bits. The number of contiguous RBs that can be assigned to a type-1 hopping user is limited to . The number of contiguous RBs that can be assigned to a type-2 hopping user is limited to min(,), where the number of sub-bands  is given by higher layers.

A UE performing PUSCH frequency hopping shall use one of two possible PUSCH frequency hopping types based on the hopping information. PUSCH hopping type 1 is described in Clause 8.4.1 and type 2 is described in Clause 8.4.2.

Table 8.4-1: Number of Hopping Bits NUL_hop vs. System Bandwidth

| System BW | #Hopping bits for 2nd slot RA (NUL_hop) |
| --- | --- |
| 6-49 | 1 |
| 50-110 | 2 |

The parameter Hopping-mode provided by higher layers determines if PUSCH frequency hopping is "inter-subframe" or "intra and inter-subframe".

### 8.4.1 Type 1 PUSCH hopping

For PUSCH hopping type 1 the hopping bit or bits indicated in Table 8.4-1 determine as defined in Table 8.4-2. The lowest index PRB () of the 1st slot RA in subframe i is defined as , where , and is obtained from the uplink scheduling grant as in Clause 8.4 and Clause 8.1.

The lowest index PRB () of the 2nd slot RA in subframe i is defined as .

The set of physical resource blocks to be used for PUSCH transmission are contiguously allocated resource blocks from PRB index  for the 1st slot, and from PRB index  for the 2nd slot, respectively, where is obtained from the uplink scheduling grant as in Clause 8.4 and Clause 8.1.

If the Hopping-mode is "inter-subframe", the 1st slot RA is applied to even CURRENT_TX_NB, and the 2nd slot RA is applied to odd CURRENT_TX_NB, where CURRENT_TX_NB is defined in [8].

### 8.4.2 Type 2 PUSCH hopping

In PUSCH hopping type 2 the set of physical resource blocks to be used for transmission in slot  is given by the scheduling grant together with a predefined pattern according to [3] Clause 5.3.4. 
If the system frame number is not acquired by the UE yet, the UE shall not transmit PUSCH with type-2 hopping and  for TDD, where  is defined in [3].

Table 8.4-2: PDCCH/EPDCCH DCI format 0 hopping bit definition

| System BW | Number of  Hopping bits | Information in  hopping bits |  |
| --- | --- | --- | --- |
| 6 – 49 | 1 | 0 | , |
|  |  | 1 | Type 2 PUSCH Hopping |
| 50 – 110 | 2 | 00 |  |
|  |  | 01 |  |
|  |  | 10 |  |
|  |  | 11 | Type 2 PUSCH Hopping |

## 8.5 UE Reference Symbol (RS) procedure

If UL sequence-group hopping or sequence hopping is configured in a serving cell, it applies to all Reference Symbols (SRS, PUSCH and PUCCH RS). If disabling of the sequence-group hopping and sequence hopping is configured for the UE in the serving cell through the higher-layer parameter Disable-sequence-group-hopping, the sequence-group hopping and sequence hopping for PUSCH RS are disabled.

## 8.6 Modulation order, redundancy version and transport block size determination

To determine the modulation order, redundancy version and transport block size for the physical uplink shared channel, the UE shall first

- for a cell that is

- a LAA SCell or,

- configured with higher layer parameter shortProcessingTime and the PDCCH with CRC scrambled by C-RNTI corresponding to the PUSCH is in the UE-specific search space, or

- configured with higher layer parameter shortTTI and the associated DCI is of format 7-0A/7-0B,

- read the "modulation and coding scheme" field () and "redundancy version" field (),

- otherwise

- if the UE is a non-BL/CE UE,

- read the "modulation and coding scheme and redundancy version" field ()

- elseif the UE is a BL/CE UE,

- for transmission using preconfigured uplink resources,

- read the higher layer parameter mcs-r16 in PUR-Config

- otherwise

- read the "modulation and coding scheme" field ()

and

- check the "CSI request" bit field, and

- compute the total number of allocated PRBs () based on the procedure defined in Clause 8.1, and

- compute the number of coded symbols for control information.

### 8.6.1 Modulation order and redundancy version determination

For a non-BL/CE UE and for , the modulation order () is determined as follows, where =  unless specified otherwise:

- If the UE is capable of supporting 64QAM in PUSCH and is not capable of supporting 256QAM in PUSCH and has not been configured by higher layers to transmit only QPSK and 16QAM, the modulation order is given by in Table 8.6.1-1.

- If the UE is capable of supporting 256QAM in PUSCH, and has not been configured by higher layers to transmit only QPSK and 16QAM and has not been configured with higher layer parameter Enable256QAM, the modulation order is given by in Table 8.6.1-1.

- If the UE is capable of supporting 256QAM in subframe-PUSCH and configured with higher layer parameter Enable256QAM, the modulation order is given by in Table 8.6.1-3 for subframe-PUSCH ,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet1-DCI-Format0=TRUE, the associated DCI is of format 0/0A/0B mapped onto the UE specific search space and with CRC scrambled by the C-RNTI, and the subframe of the PUSCH belongs to uplink power control subframe set 1, or,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet1-DCI-Format4=TRUE, the associated DCI is of format 4/4A/4B mapped onto the UE specific search space and with CRC scrambled by the C-RNTI, and the subframe of the PUSCH belongs to uplink power control subframe set 1, or,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet2-DCI-Format0=TRUE, the associated DCI is of format 0/0A/0B mapped onto the UE specific search space and with CRC scrambled by the C-RNTI, and the subframe of the PUSCH belongs to uplink power control subframe set 2, or,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet2-DCI-Format4=TRUE, the associated DCI is of format 4/4A/4B mapped onto the UE specific search space and with CRC scrambled by the C-RNTI, and the subframe/slot/subslot of the PUSCH belongs to uplink power control subframe set 2, or,

- if higher layer parameter tpc-SubframeSet is not configured, higher layer parameter dci-Format0=TRUE, and the associated DCI is of format 0/0A/0B mapped onto the UE specific search space and with CRC scrambled by the C-RNTI, or,

- if higher layer parameter tpc-SubframeSet is not configured, higher layer parameter dci-Format4=TRUE, and the associated DCI is of format 4/4A/4B mapped onto the UE specific search space and with CRC scrambled by the C-RNTI,

- otherwise, the modulation order is given by in Table 8.6.1-1 for subframe-PUSCH.

- If the UE is capable of supporting 256QAM in slot/subslot PUSCH and configured with higher layer parameter Enable256QAMSTTI, the modulation order is given by in Table 8.6.1-3 for slot/subslot-PUSCH,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet1-256QAM-STTI=TRUE, the associated DCI is of format 7-0A/7-0B mapped onto the UE specific search space and with CRC scrambled by the C-RNTI, and the subframe of the slot/subslot-PUSCH belongs to uplink power control subframe set 1, or,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet2-256QAM-STTI=TRUE, the associated DCI is of format 7-0A/7-0B mapped onto the UE specific search space and with CRC scrambled by the C-RNTI, and the subframe of the slot/subslot PUSCH belongs to uplink power control subframe set 2, or,

- if higher layer parameter tpc-SubframeSet is not configured, the associated DCI is of format 7-0A/7-0B mapped onto the UE specific search space and with CRC scrambled by the C-RNTI,;

- otherwise, the modulation order is given by in Table 8.6.1-1 for slot/subslot PUSCH.

- If the UE is not capable of supporting 64QAM in PUSCH or has been configured by higher layers to transmit only QPSK and 16QAM, is first read from Table 8.6.1-1. The modulation order is set to  = min(4,).

- If the parameter ttiBundling provided by higher layers is set to TRUE, then the modulation order is set to . Resource allocation size is restricted to  applies in this case if the UE does not indicate support by higher layers to operate without it.

- If the UE is configured with higher layer parameter pusch-EnhancementsConfig, and if the PDCCH corresponding to the PUSCH transmission is located in UE specific search space, then is first obtained according to the procedure above. The modulation order () is determined as follows.

- If the uplink DCI modulation override bit is set to zero, or if =2

- then =

- otherwise

- if =8 then = 6,

- if =6 then = 4,

- if =4 then = 2.

For a non-BL/CE UE and for  the modulation order () is determined as follows:

- if DCI format 0/0A/0B/7-0A is used and  and N =1 (determined by the procedure in Clause 8.0) or, if DCI format 4/7-0B is used and only 1 TB is enabled and for the enabled TB and the signalled number of transmission layers is 1 or if DCI format 4A/4B is used and  for both TBs and N =1 (determined by the procedure in Clause 8.0), and if

- the "CSI request" bit field is 1 bit and the bit is set to trigger an aperiodic report and,  or,

- the "CSI request" bit field is 2 bits and is triggering an aperiodic CSI report for one serving cell according to Table 7.2.1-1A, and,  or,

- the "CSI request" bit field is 2 bits and is triggering an aperiodic CSI report for more than one serving cell according to Table 7.2.1-1A and,  or,

- the "CSI request" bit field is 2 bits and is triggering an aperiodic CSI report for one CSI process according to Table 7.2.1-1B and  or,

- the "CSI request" bit field is 2 bits and is triggering an aperiodic CSI report for more than one CSI process according to Table 7.2.1-1B and  or,

- the "CSI request" bit field is 2 bits and is triggering an aperiodic CSI report for one CSI process or {CSI process, CSI subframe set}-pair according to Table 7.2.1-1C and  or,

- the "CSI request" bit field is 2 bits and is triggering an aperiodic CSI report for more than one CSI process and/or {CSI process, CSI subframe set}-pair according to Table 7.2.1-1C and , or

- the "CSI request" bit field is 3 bits and is triggering an aperiodic CSI report for one CSI process according to Table 7.2.1-1D or Table 7.2.1-1E or Table 7.2.1-1F or Table 7.2.1-1G and , or

- the "CSI request" bit field is 3 bits and is triggering an aperiodic CSI report for 2 to 5 CSI processes according to Table 7.2.1-1D or Table 7.2.1-1E or Table 7.2.1-1F or Table 7.2.1-1G and , or

- the "CSI request" bit field is 3 bits and is triggering an aperiodic CSI report for more than 5 CSI processes according to Table 7.2.1-1D or Table 7.2.1-1E or Table 7.2.1-1F or Table 7.2.1-1G, or

- the "CSI request" bit field in DCI format 0A/0B/4A/4B/7-0A/7-0B is set to trigger an aperiodic CSI report, or

- the "CSI request" bit field is 4 bits and is triggering an aperiodic CSI report for one CSI process according to Table 7.2.1-1H or Table 7.2.1-1I and , or

- the "CSI request" bit field is 4 bits and is triggering an aperiodic CSI report for 2 to 5 CSI processes according to Table 7.2.1-1H or Table 7.2.1-1I and , or

- the "CSI request" bit field is 4 bits and is triggering an aperiodic CSI report for more than 5 CSI processes according to Table 7.2.1-1H or Table 7.2.1-1I, or

- the "CSI request" bit field is 5 bits and is triggering an aperiodic CSI report for one CSI process according to Table 7.2.1-1J or Table 7.2.1-1K and , or

- the "CSI request" bit field is 5 bits and is triggering an aperiodic CSI report for 2 to 5 CSI processes according to Table 7.2.1-1J or Table 7.2.1-1K and , or

- the "CSI request" bit field is 5 bits and is triggering an aperiodic CSI report for more than 5 CSI processes according to Table 7.2.1-1J or Table 7.2.1-1K, or

- the "CSI request" bit field in DCI is set to trigger an aperiodic CSI report and UE is configured with higher layer parameter advancedCodebookEnabled,

- the "CSI request" bit field in DCI is set to trigger an aperiodic CSI report and UE is configured with higher layer parameter FeCoMPCSIEnabled,

then the modulation order is set to .

- Otherwise,

- For a cell that is not a LAA SCell, the modulation order shall be determined from the DCI transported in the latest PDCCH/EPDCCH/SPDCCH with DCI format 0/4/7-0A/7-0B for the same transport block using . If there is no PDCCH/EPDCCH/SPDCCH with DCI format 0/4/7-0A/7-0B for the same transport block using , the modulation order shall be determined from

- the most recent semi-persistent scheduling assignment PDCCH/EPDCCH/SPDCCH, when the initial PUSCH for the same transport block is semi-persistently scheduled, or,

- the random access response grant for the same transport block, when the PUSCH is initiated by the random access response grant.

- For a cell that is an LAA SCell and a UE that is configured with Partial PUSCH Mode 2 or 3, if ![](media_svg/image277.svg) [公式: I_{MCS}=30], the modulation order shall be determined from the DCI transported in the latest PDCCH/EPDCCH with DCI format 0A/0B/4A/4B for the same transport block using ![](media_svg/image278.svg) [公式: 0≥I_{MCS}≥28].

For a cell that is not a LAA SCell, and a non-BL/CE UE,

- for subframe-PUSCH, if the UE is configured with higher layer parameter enable256QAM-r14, and if the PDCCH corresponding to the PUSCH transmission is located in UE specific search space with CRC scrambled by the C-RNTI, the UE shall useand Table 8.6.1-3 to determine the redundancy version (rvidx) to use in the physical uplink shared channel,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet1-DCI-Format0=TRUE, the associated DCI is of format 0/0A/0B, and the subframe of the PUSCH belongs to uplink power control subframe set 1, or,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet1-DCI-Format4=TRUE, the associated DCI is of format 4/4A/4B, and the subframe of the PUSCH belongs to uplink power control subframe set 1, or,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet2-DCI-Format0=TRUE, the associated DCI is of format 0/0A/0B, and the subframe of the PUSCH belongs to uplink power control subframe set 2, or,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet2-DCI-Format4=TRUE, the associated DCI is of format 4/4A/4B, and the subframe of the PUSCH belongs to uplink power control subframe set 2, or,

- if higher layer parameter tpc-SubframeSet is not configured, higher layer parameter dci-Format0=TRUE, and the associated DCI is of format 0/0A/0B, or,

- if higher layer parameter tpc-SubframeSet is not configured, higher layer parameter dci-Format4=TRUE, and the associated DCI is of format 4/4A/4B;

- otherwise, the UE shall useand Table 8.6.1-1 to determine the redundancy version (rvidx) to use in the physical uplink shared channel.

For a LAA SCell and DCI format 0A/4A, the redundancy version (rvidx) to use in the physical uplink shared channel is given by ![](media_svg/image279.svg) [公式: rv_{idx}=rv].

For a LAA SCell and DCI format 0B/4B, the redundancy version (rvidx) to use in the physical uplink shared channel is given by ![](media_svg/image280.svg) [公式: rv_{idx}=2∪rv].

For a serving cell, if the UE is configured with higher layer parameter

- shortProcessingTime if the PDCCH with CRC scrambled by C-RNTI corresponding to the PUSCH transmission is located in UE specific search space or

- shortTTI and if the associated DCI is of format 7-0A/7-0B,

the redundancy version (rvidx) to use in the physical uplink shared channel is given by ![](media_svg/image279.svg) [公式: rv_{idx}=rv].

For a serving cell, for semi-persistently scheduled slot/subslot-PUSCH transmissions of a transport block spanning K consecutive PUSCH transmissions corresponding to an SPS configuration with higher layer parameters rv-SPS-STTI-UL-Repetitions and totalNumberPUSCH-SPS-STTI-UL-Repetitions, the redundancy version (rvidx) is determined according to Table 8.6.1-0 for the kth PUSCH transmission, using ![](media_svg/image281.svg) [公式: rvk=−(1)mod4] where k=1,…, K,, and K=totalNumberPUSCH-SPS-STTI-UL-Repetitions.

For a serving cell, for semi-persistently scheduled subframe-PUSCH transmissions of a transport block spanning K consecutive PUSCH transmissions corresponding to an SPS configuration with higher layer parameters rv-SPS-UL-Repetitions and totalNumberPUSCH-SPS-UL-Repetitions, the redundancy version (rvidx) is determined according to Table 8.6.1-0 for the kth PUSCH transmission, using ![](media_svg/image282.svg) [公式: rvk=−(1)mod4] where k=1,…, K, and K=totalNumberPUSCH-SPS-UL-Repetitions.

Table 8.6.1-0: Redundancy Version corresponding to different values of higher layer parameter rv-SPS-STTI-UL-Repetitions or rv-SPS-UL-Repetitions

| Redundancy version Index rv | rvidx for rv-SPS-STTI-UL-Repetitions or rv-SPS-UL-Repetitions ={0,0,0,0,0,0} | rvidx for rv-SPS-STTI-UL-Repetitions or rv-SPS-UL-Repetitions ={0,2,3,1,0,2} | rvidx for rv-SPS-STTI-UL-Repetitions or rv-SPS-UL-Repetitions ={0,3,0,3,0,3} |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 1 | 0 | 2 | 3 |
| 2 | 0 | 3 | 0 |
| 3 | 0 | 1 | 3 |

Table 8.6.1-1: Modulation, TBS index and redundancy version table for PUSCH

| MCS Index | Modulation Order | TBS Index | Redundancy Version rvidx |
| --- | --- | --- | --- |
| 0 | 2 | 0 | 0 |
| 1 | 2 | 1 | 0 |
| 2 | 2 | 2 | 0 |
| 3 | 2 | 3 | 0 |
| 4 | 2 | 4 | 0 |
| 5 | 2 | 5 | 0 |
| 6 | 2 | 6 | 0 |
| 7 | 2 | 7 | 0 |
| 8 | 2 | 8 | 0 |
| 9 | 2 | 9 | 0 |
| 10 | 2 | 10 | 0 |
| 11 | 4 | 10 | 0 |
| 12 | 4 | 11 | 0 |
| 13 | 4 | 12 | 0 |
| 14 | 4 | 13 | 0 |
| 15 | 4 | 14 | 0 |
| 16 | 4 | 15 | 0 |
| 17 | 4 | 16 | 0 |
| 18 | 4 | 17 | 0 |
| 19 | 4 | 18 | 0 |
| 20 | 4 | 19 | 0 |
| 21 | 6 | 19 | 0 |
| 22 | 6 | 20 | 0 |
| 23 | 6 | 21 | 0 |
| 24 | 6 | 22 | 0 |
| 25 | 6 | 23 | 0 |
| 26 | 6 | 24 | 0 |
| 27 | 6 | 25 | 0 |
| 28 | 6 | 26 | 0 |
| 29 | reserved |  | 1 |
| 30 |  |  | 2 |
| 31 |  |  | 3 |

For a BL/CE UE

- if the UE is configured with CEModeA, and higher layer parameter ce-pusch-nb-maxTbs-config configured with value 'On', and if the MPDCCH corresponding to the PUSCH transmission is located in UE-specific search space, the modulation order is determined according to table 8.6.1-2A.

- if the UE is configured with higher layer parameter ce-pdsch-puschEnhancement-config with value 'On', and if the Modulation order override field in the DCI is set to 1, the modulation order is set to

- if the UE is configured with higher layer parameter edt-Parameters-r15, and if the PUSCH transmission is scheduled by the Random Access Response Grant, and the higher layers indicate EDT to the physical layer as defined in [8], or the PUSCH retransmission of the same transport block including EDT as part of the contention based random access procedure with ![](media_svg/image284.svg) [公式: I_{MCS}=15] in the uplink scheduling grant, the modulation order is set to .

- if the UE is configured with higher layer parameter ce-PUSCH-SubPRB-Config-r15, and the PUSCH resource assignment is using uplink resource allocation type 5, the modulation order is set to ![](media_svg/image285.svg) [公式: Q_{m}=1] for π/2-BPSK, otherwise.

- otherwise, the modulation order is determined according to table 8.6.1-2.

A BL/CE UE configured with CEModeB is not expected to receive a DCI format 6-0B indicating ![](media_svg/image286.svg) [公式: I_{MCS}>10].

For a BL/CE UE or for UEs configured with higher layer parameter PUSCH-EnhancementsConfig,

- if the UE is configured with higher layer parameter ce-PUSCH-SubPRB-Config-r15, and the PUSCH resource assignment is using uplink resource allocation type 5, the redundancy version (rvidx) to use for the i-th BL/CE UL subframe associated with a TB in the physical uplink shared channel is determined according to Table 7.1.7.1-2 using ![](media_svg/image287.svg) [公式≈: rvrv=+()mod4^{⋅∂}_{⋅∂}_{√∃}_{MM}_{RUslots}_{∪}^{i}_{UL}_{/2}_{DCI}] where $ i=0, 1, \ldots  ,N-1 $, and N is the number of BL/CE UL subframes associated with the TB for the PUSCH transmission as determined in clause 8.0. For a BL/CE UE configured in CEModeA,![](media_svg/image288.svg) [公式≈: ^{rv}DCI] is determined by the 'Redundancy version' field in DCI format 6-0A, if present. For a BL/CE UE configured in CEModeA, if the UE is configured with higher layer parameter ce-PUSCH-MultiTB-Config and multiple TB are scheduled in the corresponding DCI, and the 'Redundancy version' field for a scheduled TB is not present in the corresponding DCI,  for all TBs scheduled by the DCI. For a BL/CE UE configured with CEModeB, . For a BL/CE UE,  for a PUSCH transmission using preconfigured uplink resource.

- otherwise, the same redundancy version is applied to PUSCH associated with a TB that is transmitted in a given block of ![](media_svg/image290.svg) [公式≈: ^{N}acc] consecutive subframes associated with a TB, including subframes that are not BL/CE UL subframes. The subframe number of the first subframe in each block of ![](media_svg/image290.svg) [公式≈: ^{N}acc] such consecutive subframes, denoted as ![](media_svg/image291.svg) [公式≈: ^{n}abs,1], satisfies ![](media_svg/image292.svg) [公式≈: ^{n}abs,1^{mod}^{N}acc^{=}^{0}]. Denote  as the subframe number of the first uplink subframe intended for PUSCH associated with a TB. For BL/CE UEs, the PUSCH transmission associated with a TB spans $ N_{abs,TB}^{PUSCH}$ consecutive subframes associated with the TB, including subframes that are not BL/CE UL subframes where the PUSCH transmission is postponed and excluding subframes associated with other TBs scheduled by the DCI, if any. For the  block of consecutive subframes within the set of $ N_{abs,TB}^{PUSCH}$ subframes associated with the TB as described above, the redundancy version (rvidx) associated with the TB is determined according to Table 7.1.7.1-2 using ![](media_svg/image296.svg) [公式: rvjrv=+(_{DCI})mod4], where ![](media_svg/image297.svg) [公式≈: jJ=−0,1,...,1^{PUSCH}], and $ J^{PUSCH}=\lceil  \frac {N_{abs,TB}^{PUSCH}+\left ( i_{0}modN_{acc}\right ) }{N_{acc}}\rceil  $. The ![](media_svg/image298.svg) [公式≈: _{J}PUSCH] blocks of subframes are sequential in time, starting with ![](media_svg/image299.svg) [公式: j=0] to which subframe belongs. For a BL/CE UE configured with CEModeB,  for FDD and  for TDD, and ![](media_svg/image302.svg) [公式: rv_{DCI}=0]. For a UE configured with higher layer parameter PUSCH-EnhancementsConfig,  and ![](media_svg/image288.svg) [公式≈: ^{rv}DCI] is determined by the 'Redundancy version' field in DCI format 0C. For UEs configured with higher layer parameter PUSCH-EnhancementsConfig,.$ N_{abs,TB}^{PUSCH}=N_{rep}^{PUSCH}$. For a BL/CE UE configured in CEModeA, . For a BL/CE UE configured in CEModeA, and not configured with the higher layer parameter ce-PUSCH-MultiTB-Config, ![](media_svg/image288.svg) [公式≈: ^{rv}DCI] for a TB is determined by the 'Redundancy version' field in DCI format 6-0A.

- if $ N_{TB}=1 $ is indicated by the corresponding DCI,  for the TB is determined by the 'Redundancy version' in the 'Scheduling TBs for Unicast' field in DCI format 6-0A

- else if $ N_{TB}=2 $ is indicated by the corresponding DCI, and the HARQ process IDs for each of the scheduled TBs are h1 and h2 (h1<h2),  of the scheduled TB with HARQ process ID h1 is determined by the 'Redundancy version for TB 1' in the 'Scheduling TBs for Unicast' field in DCI format 6-0A, and  of the scheduled TB with HARQ process ID h2 is determined by

- if the UE is configured with higher layer parameter pusch-HoppingConfig set to'on' and the repetition number field in the DCI indicates PUSCH repetition, the 'Redundancy version for TB 1' in the 'Scheduling TBs for Unicast' field in DCI format 6-0A

- otherwise the 'Redundancy version for TB 2' in the 'Scheduling TBs for Unicast' field in DCI format 6-0A

- else if $ N_{TB}$ = 4 or 6,  for all scheduled TBs

- else

- if the UE is configured with higher layer parameter pusch-HoppingConfig set to 'on' and the repetition number field in the DCI indicates PUSCH repetition,  for all TBs

- otherwise  of all TBs is determined by the 'Redundancy version for all TBs' in the 'Scheduling TBs for Unicast' field in DCI format 6-0A.

Table 8.6.1-2: Modulation and TBS index table for PUSCH

| MCS Index ![](media_svg/image305.svg) [公式≈: ^{I}MCS] | Modulation Order ![](media_svg/image306.svg) [公式≈: ^{Q}m] | TBS Index ![](media_svg/image307.svg) [公式≈: ^{I}TBS] |
| --- | --- | --- |
| 0 | 2 | 0 |
| 1 | 2 | 1 |
| 2 | 2 | 2 |
| 3 | 2 | 3 |
| 4 | 2 | 4 |
| 5 | 2 | 5 |
| 6 | 2 | 6 |
| 7 | 2 | 7 |
| 8 | 2 | 8 |
| 9 | 2 | 9 |
| 10 | 2 | 10 |
| 11 | 4 | 10 |
| 12 | 4 | 11 |
| 13 | 4 | 12 |
| 14 | 4 | 13 |
| 15 | 4 | 14 |

Table 8.6.1-2A: Modulation and TBS index table for PUSCH

| MCS Index ![](media_svg/image305.svg) [公式≈: ^{I}MCS] | Modulation Order ![](media_svg/image306.svg) [公式≈: ^{Q}m] | TBS Index ![](media_svg/image307.svg) [公式≈: ^{I}TBS] |
| --- | --- | --- |
| 0 | 2 | 0 |
| 1 | 2 | 2 |
| 2 | 2 | 4 |
| 3 | 2 | 5 |
| 4 | 2 | 6 |
| 5 | 2 | 8 |
| 6 | 2 | 10 |
| 7 | 4 | 10 |
| 8 | 4 | 12 |
| 9 | 4 | 14 |
| 10 | 4 | 16 |
| 11 | 4 | 17 |
| 12 | 4 | 18 |
| 13 | 4 | 19 |
| 14 | 4 | 20 |
| 15 | 4 | 21 |

Table 8.6.1-3: Modulation, TBS index and redundancy version table for PUSCH

| MCS Index | Modulation Order | TBS Index | Redundancy Version rvidx |
| --- | --- | --- | --- |
| 0 | 2 | 0 | 0 |
| 1 | 2 | 2 | 0 |
| 2 | 2 | 4 | 0 |
| 3 | 2 | 6 | 0 |
| 4 | 2 | 8 | 0 |
| 5 | 2 | 10 | 0 |
| 6 | 4 | 11 | 0 |
| 7 | 4 | 12 | 0 |
| 8 | 4 | 13 | 0 |
| 9 | 4 | 14 | 0 |
| 10 | 4 | 16 | 0 |
| 11 | 4 | 17 | 0 |
| 12 | 4 | 18 | 0 |
| 13 | 4 | 19 | 0 |
| 14 | 6 | 20 | 0 |
| 15 | 6 | 21 | 0 |
| 16 | 6 | 22 | 0 |
| 17 | 6 | 23 | 0 |
| 18 | 6 | 24 | 0 |
| 19 | 6 | 25 | 0 |
| 20 | 6 | 27 | 0 |
| 21 | 6 | 28 | 0 |
| 22 | 6 | 29 | 0 |
| 23 | 8 | 30 | 0 |
| 24 | 8 | 31 | 0 |
| 25 | 8 | 32 | 0 |
| 26 | 8 | 32A | 0 |
| 27 | 8 | 33 | 0 |
| 28 | 8 | 34 | 0 |
| 29 | reserved |  | 1 |
| 30 |  |  | 2 |
| 31 |  |  | 3 |

Table 8.6.1-4: Void

### 8.6.2 Transport block size determination

For a non-BL/CE UE and for , the UE shall first determine the TBS index () using  except if the transport block is disabled in DCI format 4/4A/4B as specified below. For a transport block that is not mapped to two-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.1. For a transport block that is mapped to two-layer spatial multiplexing, the TBS is determined by the procedure in Clause 7.1.7.2.2.

For, DCI format 7-0A/7-0B, the derived transport block size as described in clause 7.1.7.2.1 when the transport block is mapped to one spatial layer and the derived transport block size after TBS translation as described in clauses 7.1.7.2.2, 7.1.7.2.4, 7.1.7.2.5 when the transport block is mapped to more than one spatial layer is scaled by ![](media_svg/image308.svg) [公式: Α], then rounded to the closest valid transport block size

- in Table 7.1.7.2.1-1 when the transport block is mapped to one spatial layer,

- the union of Table 7.1.7.2.1-1 and Table 7.1.7.2.2-1 when the transport block is mapped to two spatial layers,

- the union of Table 7.1.7.2.1-1 and Table 7.1.7.2.4-1when the transport block is mapped to three spatial layers,

- the union of Table 7.1.7.2.1-1 and Table 7.1.7.2.5-1when the transport block is mapped to four spatial layers,

where

- ![](media_svg/image308.svg) [公式: Α] is given by higher layer parameter tbs-scalingFactorSubslotSPS-UL-Repetitions for subslot-PUSCH if the UE is configured with higher layer parameter totalNumberPUSCH-SPS-STTI-UL-Repetitions when the PDCCH/SPDCCH CRC is scrambled by SPS C-RNTI.

- for slot-PUSCH except if the UE is configured with a higher layer parameter symPUSCH-UpPts-r14 and the TB is transmitted in UpPTS of the special subframe in frame structure type 2, $\alpha  =0.125 $ for slot-PUSCH in special subframe configuration with up to 3 UpPTS SC-FDMA data symbols, $\alpha  =0.375 $ for slot-PUSCH in special subframe configuration with more than 3 UpPTS SC-FDMA data symbols,  for subslot-PUSCH with one data symbol in the subslot, and  for subslot-PUSCH with two or three data symbols in the subslot.

If the scaled TBS is closest to two valid transport block sizes, it is rounded to the larger transport block size.

For subframe-PUSCH, the UE shall determine the TBS index () using and Table 8.6.1-3, if the UE is configured with higher layer parameter enable256QAM, and if the PDCCH corresponding to the PUSCH transmission is located in UE specific search space with CRC scrambled by the C-RNTI, and

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet1-DCI-Format0=TRUE, the associated DCI is of format 0/0A/0B, and the subframe of the PUSCH belongs to uplink power control subframe set 1, or,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet1-DCI-Format4=TRUE, the associated DCI is of format 4/4A/4B, and the subframe of the PUSCH belongs to uplink power control subframe set 1, or,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet2-DCI-Format0=TRUE, the associated DCI is of format 0/0A/0B, and the subframe of the PUSCH belongs to uplink power control subframe set 2, or,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet2-DCI-Format4=TRUE, the associated DCI is of format 4/4A/4B, and the subframe of the PUSCH belongs to uplink power control subframe set 2, or,

- if higher layer parameter tpc-SubframeSet is not configured, higher layer parameter dci-Format0=TRUE, and the associated DCI is of format 0/0A/0B, or,

- if higher layer parameter tpc-SubframeSet is not configured, higher layer parameter dci-Format4=TRUE, and the associated DCI is of format 4/4A/4B;

otherwise, the UE shall determine the TBS index () using and Table 8.6.1-1.

For subslot/slot-PUSCH, the UE shall determine the TBS index () using and Table 8.6.1-3, if the UE is configured with higher layer parameter Enable256QAMSTTI, and if the PDCCH/SPDCCH corresponding to the PUSCH transmission is located in UE specific search space with CRC scrambled by the C-RNTI, and

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet1-256QAM-STTI=TRUE, the associated DCI is of format 7-0A/7-0B, and the subframe of the slot/subslot-PUSCH belongs to uplink power control subframe set 1, or,

- if higher layer parameter tpc-SubframeSet is configured, higher layer parameter subframeSet2-256QAM-STTI=TRUE, the associated DCI is of format 7-0A/7-0B, and the subframe of the slot/subslot-PUSCH belongs to uplink power control subframe set 2, or,

- if higher layer parameter tpc-SubframeSet is not configured, and the associated DCI is of format 7-0A/7-0B;

otherwise, the UE shall determine the TBS index () using and Table 8.6.1-1.

If the UE is configured with higher layer parameter symPUSCH-UpPts-r14, ttiBundling=FALSE, and the transport block is transmitted in UpPTS of the special subframe in frame structure type 2, then

- for special subframe configuration with up to 3 UpPTS SC-FDMA data symbols:

- set the Table 7.1.7.2.1-1 column indicator to ![](media_svg/image312.svg) [公式≈: max{_{√}N_{PRB}≠0.125_{∃},1}] instead of ![](media_svg/image313.svg) [公式≈: ^{N}PRB]

- otherwise:

- set the Table 7.1.7.2.1-1 column indicator to ![](media_svg/image314.svg) [公式≈: max{_{√}N_{PRB}≠0.375_{∃},1}] instead of ![](media_svg/image315.svg) [公式≈: ^{N}PRB].

If the transport block is transmitted on an LAA SCell,

- If ![](media_svg/image316.svg) [公式: 0≥I_{MCS}≥28], then

- if the UE is transmitting a Partial PUSCH Mode 2, or if the UE is transmitting a Partial PUSCH Mode 3 ending at symbol #6

- set the Table 7.1.7.2.1-1 column indicator to ![](media_svg/image317.svg) [公式≈: max{_{√}N_{PRB}≠0.5_{∃},1}] instead of ![](media_svg/image318.svg) [公式≈: ^{N}PRB]

- if the UE is transmitting a Partial PUSCH Mode 3 ending at symbol #3

- set the Table 7.1.7.2.1-1 column indicator to ![](media_svg/image319.svg) [公式≈: max{_{√}N_{PRB}≠0.125_{∃},1}] instead of ![](media_svg/image318.svg) [公式≈: ^{N}PRB]

- If the UE is configured with Partial PUSCH Mode 2 or 3 on the LAA SCell and ![](media_svg/image277.svg) [公式: I_{MCS}=30], the transport block size shall be determined from the latest PDCCH/EPDCCH with DCI format 0A/0B/4A/4B for the same transport block using ![](media_svg/image316.svg) [公式: 0≥I_{MCS}≥28].

For a non-BL/CE UE and for ,

- if DCI format 0/0A/0B/7-0A/7-0B is used and  and N =1 (determined by the procedure in Clause 8.0) or, if DCI format 4 is used and only 1 TB is enabled and  for the enabled TB and the number of transmission layers is 1 or if DCI format 4A/4B is used and  for both TBs and N =1 (determined by the procedure in Clause 8.0), and if

- the "CSI request" bit field is 1 bit and is set to trigger an aperiodic CSI report and  or,

- the "CSI request" bit field is 2 bits and is triggering an aperiodic CSI report for one serving cell according to Table 7.2.1-1A, and ,  or,

- the "CSI request" bit field is 2 bits and is triggering aperiodic CSI report for more than one serving cell according to Table 7.2.1-1A and,  or,

- the "CSI request" bit field is 2 bits and is triggering an aperiodic CSI report for one CSI process according to Table 7.2.1-1B and  or,

- the "CSI request" bit field is 2 bits and is triggering an aperiodic CSI report for more than one CSI process according to Table 7.2.1-1B and,  or,

- the "CSI request" bit field is 2 bits and is triggering an aperiodic CSI report for one CSI process or {CSI process, CSI subframe set}-pair according to Table 7.2.1-1C and  or,

- the "CSI request" bit field is 2 bits and is triggering an aperiodic CSI report for more than one CSI process and/or {CSI process, CSI subframe set}-pair according to Table 7.2.1-1C and , or

- the "CSI request" bit field is 3 bits and is triggering an aperiodic CSI report for one CSI process according to Table 7.2.1-1D or Table 7.2.1-1E or Table 7.2.1-1F or Table 7.2.1-1G and , or

- the "CSI request" bit field is 3 bits and is triggering an aperiodic CSI report for 2 to 5 CSI processes according to Table 7.2.1-1D or Table 7.2.1-1E or Table 7.2.1-1F or Table 7.2.1-1G and , or

- the "CSI request" bit field is 3 bits and is triggering an aperiodic CSI report for more than 5 CSI processes according to Table 7.2.1-1D or Table 7.2.1-1E or Table 7.2.1-1F or Table 7.2.1-1G, or

- the "CSI request" bit field in DCI format 0A/0B/4A/4B/7-0A/7-0B is set to trigger an aperiodic CSI report, or

- the "CSI request" bit field is 4 bits and is triggering an aperiodic CSI report for one CSI process according to Table 7.2.1-1H or Table 7.2.1-1I and , or

- the "CSI request" bit field is 4 bits and is triggering an aperiodic CSI report for 2 to 5 CSI processes according to Table 7.2.1-1H or Table 7.2.1-1I and , or

- the "CSI request" bit field is 4 bits and is triggering an aperiodic CSI report for more than 5 CSI processes according to Table 7.2.1-1H or Table 7.2.1-1I, or

- the "CSI request" bit field is 5 bits and is triggering an aperiodic CSI report for one CSI process according to Table 7.2.1-1J or Table 7.2.1-1K and , or

- the "CSI request" bit field is 5 bits and is triggering an aperiodic CSI report for 2 to 5 CSI processes according to Table 7.2.1-1J or Table 7.2.1-1K and , or

- the "CSI request" bit field is 5 bits and is triggering an aperiodic CSI report for more than 5 CSI processes according to Table 7.2.1-1J or Table 7.2.1-1K, or

- the "CSI request" bit field in DCI is set to trigger an aperiodic CSI report and UE is configured with higher layer parameter advancedCodebookEnabled,

- the "CSI request" bit field in DCI is set to trigger an aperiodic CSI report and UE is configured with higher layer parameter FeCoMPCSIEnabled,

then there is no transport block for the UL-SCH and only the control information feedback for the current PUSCH reporting mode is transmitted by the UE.

- Otherwise, the transport block size shall be determined from the initial PDCCH/EPDCCH/SPDCCH for the same transport block using . If there is no initial PDCCH/EPDCCH/SPDCCH with an uplink DCI format for the same transport block using , the transport block size shall be determined from

- the most recent semi-persistent scheduling assignment PDCCH/EPDCCH/SPDCCH, when the initial PUSCH for the same transport block is semi-persistently scheduled, or,

- the random access response grant for the same transport block, when the PUSCH is initiated by the random access response grant.

In DCI format 4 a transport block is disabled if either the combination of  and  or the combination of  and  is signalled, otherwise the transport block is enabled.

In DCI formats 4A/4B a transport block is disabled if ![](media_svg/image330.svg) [公式: I_{MCS}=29] and otherwise the transport block is enabled.

If DCI format 4B is used and  for both TBs, UE is not expected to receive the value of N >1 as determined by the procedure in Clause 8.0.

If DCI format 0B is used and , UE is not expected to receive the value of N >1 as determined by the procedure in Clause 8.0.

For a BL/CE UE configured with CEModeA and a PUSCH transmission not scheduled by the Random Access Response Grant,

- if the UE is configured with higher layer parameter ce-PUSCH-SubPRB-Config-r15,

- if the value of the 'number of resource units' field in the scheduling grant is set to '01', the TBS is determined according to the procedure in Clause 7.1.7.2.1 with ![](media_svg/image331.svg) [公式≈: ^{II}TBS^{=}MCS] and ![](media_svg/image332.svg) [公式≈: ^{N}PRB^{=}^{2}] for ![](media_svg/image333.svg) [公式: 07≥≥I_{TBS}],

- elseif the value of the 'number of resource units' field in the scheduling grant is set to '10', the TBS is determined according to the procedure in Clause 7.1.7.2.1 with ![](media_svg/image334.svg) [公式≈: ^{II}TBS^{=+}MCS^{1}] and ![](media_svg/image335.svg) [公式≈: ^{N}PRB^{=}^{3}]for ![](media_svg/image336.svg) [公式: 18≥≥I_{TBS}],

- elseif the value of the 'number of resource units' field in the scheduling grant is set to '11', ![](media_svg/image337.svg) [公式: TBSTBS=min,1000{±}] where ![](media_svg/image338.svg) [公式: TBS^{±}] is the TBS determined according to the procedure in Clause 7.1.7.2.1 with ![](media_svg/image339.svg) [公式≈: ^{II}TBS^{=+}MCS^{3}] and ![](media_svg/image340.svg) [公式≈: ^{N}PRB^{=}^{6}] for ![](media_svg/image341.svg) [公式: 310≥≥I_{TBS}],

- elseif the UE is configured with higher layer parameter ce-pusch-nb-maxTbs-config with value 'On', and if the MPDCCH corresponding to the PUSCH transmission is located in UE-specific search space, the UE shall first determine the TBS index () usingand Table 8.6.1-2A;

- otherwise, the UE shall first determine the TBS index () usingand Table 8.6.1-2.

For a BL/CE UE configured with CEModeA and a PUSCH transmission not scheduled by the Random Access Response Grant,

- if the UE is configured with higher layer parameter edt-Parameters-r15, and if the uplink scheduling grant corresponding to the PUSCH transmission indicates a retransmission as part of the contention based random access procedure with ![](media_svg/image342.svg) [公式: 07≥≥I_{MCS}] and the most recent PUSCH transmission including a transport block with EDT, the TBS is determined by the procedure in Clause 7.1.7.2.1, for ![](media_svg/image343.svg) [公式: 07≥≥I_{TBS}] and the transport block does not include EDT;

- elseif the UE is configured with higher layer parameter edt-Parameters-r15, and if the uplink scheduling grant corresponding to the PUSCH transmission indicates a retransmission of the same transport block including EDT as part of the contention based random access procedure with ![](media_svg/image344.svg) [公式: I_{MCS}=15],

- if the UE is configured with higher layer parameter edt-SmallTBS-Enabled-r15, the repetition number for the transmission of Msg3 PUSCH is the smallest integer multiple of M  that is equal to or larger than![](media_svg/image345.svg) [公式≈: ^{TBSTBSN}MsgMsgMsg33,max3^{∪}] where ![](media_svg/image346.svg) [公式≈: ^{TBS}Msg3] is the TBS corresponding to the PUSCH transmission scheduled by the Random Access Response Grant, and ![](media_svg/image347.svg) [公式≈: ^{TBS}Msg3,max] is the value of the higher layer parameter edt-TBS-r15. M = 4 if ![](media_svg/image348.svg) [公式≈: ^{N}Msg3]> 4, M = 1 otherwise.

- otherwise, the TBS is given by higher layer parameter edt-TBS-r15.

- elseif the UE is not configured with higher layer parameter ce-PUSCH-SubPRB-Config-r15, or if the UE is configured with higher layer parameter ce-PUSCH-SubPRB-Config-r15 and the value of the 'number of resource units' field in the scheduling grant is set to '00'

- if the UE is configured with higher layer parameter ce-pusch-maxBandwidth-config with value 5MHz, the TBS is determined by the procedure in Clause 7.1.7.2.1, for ![](media_svg/image349.svg) [公式: 0≥I_{TBS}≥14]

- otherwise, the TBS is determined by the procedure in Clause 7.1.7.2.1.

For a BL/CE UE configured with CEModeA and a PUSCH transmission scheduled by the Random Access Response Grant,

- if the UE is configured with higher layer parameter edt-Parameters-r15, and the higher layers indicate EDT to the physical layer as defined in [8],

- if the UE is not configured with higher layer parameter edt-SmallTBS-Enabled-r15, the TBS is given by higher layer parameter edt-TBS-r15, the UE selects a TBS from the allowed TBS values in Table 8.6.2-1 otherwise.

- otherwise, the UE shall determine the TBS index by the procedure in Clause 6.2.

Table 8.6.2-1: EDT TBS for CEModeA with edt-SmallTBS-Enabled-r15 set to "true".

| edt-TBS-r15 | edt-SmallTBS-Subset-r15 | Allowable TBS values |
| --- | --- | --- |
| 408 | not configured | 328, 408 |
| 504 | not configured | 328, 408, 456, 504 |
| 504 | enabled | 408, 504 |
| 600 | not configured | 328, 408, 504, 600 |
| 600 | enabled | 408, 600 |
| 712 | not configured | 328, 456, 600, 712 |
| 712 | enabled | 456, 712 |
| 808 | not configured | 328, 504, 712, 808 |
| 808 | enabled | 504, 808 |
| 936 | not configured | 328, 504, 712, 936 |
| 936 | enabled | 504, 936 |
| 1000 | not configured | 328, 536, 776, 1000 |
| 1000 | enabled | 536, 1000 |

For a BL/CE UE configured with CEModeB,

- if the UE is configured with higher layer parameter edt-Parameters-r15, and if the PUSCH transmission is scheduled by the Random Access Response Grant, and the higher layers indicate EDT to the physical layer as defined in [8],

- if the UE is not configured with higher layer parameter edt-SmallTBS-Enabled-r15, the TBS is given by higher layer parameter edt-TBS-r15, the UE selects a TBS from the allowed TBS values in Table 8.6.2-2 otherwise.

- elseif the UE is configured with higher layer parameter edt-Parameters-r15, and if the uplink scheduling grant corresponding to the PUSCH transmission indicates a retransmission as part of the contention based random access procedure with ![](media_svg/image350.svg) [公式: 03≥≥I_{MCS}] and the most recent PUSCH transmission including a transport block with EDT, the UE shall determine the TBS index () using  and Table 8.6.1-2, and the TBS is determined by the procedure in Clause 7.1.7.2.1, for ![](media_svg/image351.svg) [公式: 03≥≥I_{TBS}] and the transport block does not include EDT

- elseif the UE is configured with higher layer parameter edt-Parameters-r15, and if the uplink scheduling grant corresponding to the PUSCH transmission indicates a retransmission of the same transport block including EDT as part of the contention based random access procedure with ![](media_svg/image344.svg) [公式: I_{MCS}=15],

- if the UE is configured with higher layer parameter edt-SmallTBS-Enabled-r15, the repetition number for the transmission of Msg3 PUSCH is the smallest integer multiple of M  that is equal to or larger than ![](media_svg/image345.svg) [公式≈: ^{TBSTBSN}MsgMsgMsg33,max3^{∪}] where ![](media_svg/image346.svg) [公式≈: ^{TBS}Msg3] is the TBS corresponding to the PUSCH transmission scheduled by the Random Access Response Grant, and ![](media_svg/image347.svg) [公式≈: ^{TBS}Msg3,max] is the value of the higher layer parameter edt-TBS-r15. M = 4 if ![](media_svg/image348.svg) [公式≈: ^{N}Msg3]> 4, M = 1 otherwise.

- otherwise, the TBS is given by higher layer parameter edt-TBS-r15.

- elseif the UE is configured with higher layer parameter ce-PUSCH-SubPRB-Config-r15, and the value of the 'sub-PRB allocation flag' field in the scheduling grant is set to '1',

- if the value of the 'number of resource units' field in the scheduling grant is set to '0', the TBS is determined according to the procedure in Clause 7.1.7.2.1 with ![](media_svg/image334.svg) [公式≈: ^{II}TBS^{=+}MCS^{1}] and ![](media_svg/image335.svg) [公式≈: ^{N}PRB^{=}^{3}]for ![](media_svg/image336.svg) [公式: 18≥≥I_{TBS}],

- elseif the value of the 'number of resource units' field in the scheduling grant is set to '1', the TBS is determined according to the procedure in Clause 7.1.7.2.1 with ![](media_svg/image339.svg) [公式≈: ^{II}TBS^{=+}MCS^{3}] and ![](media_svg/image340.svg) [公式≈: ^{N}PRB^{=}^{6}] for ![](media_svg/image352.svg) [公式: 39≥≥I_{TBS}],

- otherwise, the UE shall determine the TBS index () using  and Table 8.6.1-2, and the TBS is determined according to the procedure in Clause 7.1.7.2.1 for ![](media_svg/image353.svg) [公式: 0≥I_{TBS}≥10], and ![](media_svg/image354.svg) [公式≈: ^{N}PRB]=6 when resource allocation field is '110' or '111' otherwise![](media_svg/image354.svg) [公式≈: ^{N}PRB]= 3.

Table 8.6.2-2: EDT TBS for CEModeB with edt-SmallTBS-Enabled-r15 set to "true".

| edt-TBS-r15 | edt-SmallTBS-Subset-r15 | Allowable TBS values |
| --- | --- | --- |
| 408 | not configured | 328, 408 |
| 456 | not configured | 328, 408, 456 |
| 456 | enabled | 408, 456 |
| 504 | not configured | 328, 408, 456, 504 |
| 504 | enabled | 408, 504 |
| 600 | not configured | 328, 408, 504, 600 |
| 600 | enabled | 408, 600 |
| 712 | not configured | 328, 456, 600, 712 |
| 712 | enabled | 456, 712 |
| 808 | not configured | 328, 504, 712, 808 |
| 808 | enabled | 504, 808 |
| 936 | not configured | 328, 504, 712, 936 |
| 936 | enabled | 504, 936 |

### 8.6.3 Control information MCS offset determination

Offset values are defined for single codeword PUSCH transmission and multiple codeword PUSCH transmission. Single codeword subframe-PUSCH transmission offsets ,  and  shall be configured to values according to Table 8.6.3-1,2,3 with the higher layer signalled indexes  if the UE transmits no more than 22 HARQ-ACK bits on a PUSCH or if ![](media_svg/image359.svg) [公式≈: _{I}_{offset}HARQ_{,}_{X}−ACK] is not configured, , and , respectively. Single codeword PUSCH transmission offset shall be configured to values according to [Table 8.6.3-1] with the higher layer signalled index ![](media_svg/image359.svg) [公式≈: _{I}_{offset}HARQ_{,}_{X}−ACK] if the UE transmits more than 22 HARQ-ACK bits on a PUSCH and ![](media_svg/image359.svg) [公式≈: _{I}_{offset}HARQ_{,}_{X}−ACK] is configured.

AUL PUSCH transmission offset for AUL-UCI $\beta  _{offset}^{AUL-UCI}$ shall be configured to values according to Table 8.6.3-1 with the higher layer signalled index $ I_{offset}^{AUL-UCI}$.

If the UE is configured with higher layer parameter ul-STTI-Length,

- slot-PUSCH transmission offsets, ![](media_svg/image362.svg) [公式≈: _{Β}_{offset}HARQ−ACK], ![](media_svg/image363.svg) [公式≈: ^{Β}offset^{RI}]and ![](media_svg/image364.svg) [公式≈: ^{Β}offset^{CQI}] shall be configured via higher layer parameters betaOffsetSlot-ACK-Index, betaOffsetSlot-RI-Index, and betaOffsetSlot-CQI-Index to values according to Table 8.6.3-1, Table 8.6.3-2, and Table 8.6.3-3 with the higher layer signalled indexes  if the UE transmits no more than 22 HARQ-ACK bits on a PUSCH, and , and respectively. Slot-PUSCH transmission offset ![](media_svg/image365.svg) [公式≈: _{Β}_{offset}HARQ−ACK]shall be configured to values according to Table 8.6.3-1 with the higher layer signalled index ![](media_svg/image366.svg) [公式≈: _{I}_{offset}HARQ_{,}_{X}−ACK] if the UE transmits more than 22 HARQ-ACK bits on a slot-PUSCH.

- subslot-PUSCH transmission offsets, ![](media_svg/image367.svg) [公式≈: _{Β}_{offset}HARQ_{,}_{1}−ACK], ![](media_svg/image368.svg) [公式≈: _{Β}_{offset}HARQ_{,}_{2}−ACK], ![](media_svg/image369.svg) [公式≈: ^{Β}offset^{RI},1], ![](media_svg/image370.svg) [公式≈: ^{Β}offset^{RI},2]and ![](media_svg/image371.svg) [公式≈: ^{Β}offset^{CQI}] shall be configured via higher layer parameters betaOffsetSubslot-ACK-Index, betaOffset2Subslot-ACK-Index, betaOffsetSubslot-RI-Index, betaOffset2Subslot-RI-Index, and betaOffsetSubslot-CQI-Index to values according to Table 8.6.3-1, Table 8.6.3-2, and Table 8.6.3-3 with the higher layer signalled indexes ![](media_svg/image372.svg) [公式≈: _{I}_{offset}HARQ_{,}_{1}−ACK], ![](media_svg/image373.svg) [公式≈: _{I}_{offset}HARQ_{,}_{2}−ACK] if the UE transmits no more than 22 HARQ-ACK bits on a PUSCH, and ![](media_svg/image374.svg) [公式≈: ^{I}offset^{RI},1], ![](media_svg/image375.svg) [公式≈: ^{I}offset^{RI},2] and respectively. Subslot-PUSCH transmission offset ![](media_svg/image376.svg) [公式≈: _{Β}_{offset}HARQ_{,}_{1}−ACK]and ![](media_svg/image377.svg) [公式≈: _{Β}_{offset}HARQ_{,}_{2}−ACK]shall be configured to values according to Table 8.6.3-1 with the higher layer signalled index ![](media_svg/image378.svg) [公式≈: ^{I}offset^{HARQ},1,^{−}X^{ACK}], and ![](media_svg/image379.svg) [公式≈: ^{I}offset^{HARQ},2^{−},X^{ACK}] if the UE transmits more than 22 HARQ-ACK bits on a subslot-PUSCH. If the Beta offset indicator field in PDCCH/SPDCCH with DCI format 7-0A/7-0B is set to 0, ![](media_svg/image380.svg) [公式≈: _{Β}_{offset}HARQ−ACK_{=}_{Β}_{offset}HARQ_{,}_{1}−ACK], and ![](media_svg/image381.svg) [公式≈: ^{Β}offset^{RI}^{=}^{Β}offset^{RI},1], otherwise ![](media_svg/image382.svg) [公式≈: _{Β}_{offset}HARQ−ACK_{=}_{Β}_{offset}HARQ_{,}_{2}−ACK], and ![](media_svg/image383.svg) [公式≈: ^{Β}offset^{RI}^{=}^{Β}offset^{RI},2].

Multiple codeword PUSCH transmission offsets ,  and  shall be configured to values according to Table -1,2,3 with the higher layer signalled indexes  if the UE transmits no more than 22 HARQ-ACK bits on a PUSCH or if ![](media_svg/image387.svg) [公式≈: ^{I}offset^{HARQ},MC^{−}^{ACK},X] is not configured,  and , respectively. Multiple codeword PUSCH transmission offset shall be configured to values according to [Table 8.6.3-1] with the higher layer signalled index ![](media_svg/image387.svg) [公式≈: ^{I}offset^{HARQ},MC^{−}^{ACK},X] if the UE transmits more than 22 HARQ-ACK bits on a PUSCH and ![](media_svg/image387.svg) [公式≈: ^{I}offset^{HARQ},MC^{−}^{ACK},X] is configured.

If the UE is configured with higher layer parameter UplinkPowerControlDedicated-v12x0 for serving cell , and if a subframe belongs to uplink power control subframe set 2 as indicated by the higher layer parameter tpc-SubframeSet-r12, then for that subframe, the UE shall use

- the higher layer indexes , ![](media_svg/image391.svg) [公式≈: ^{I}offset^{HARQ},set^{−}^{ACK}2,X], and  in place of , ![](media_svg/image359.svg) [公式≈: _{I}_{offset}HARQ_{,}_{X}−ACK], , and  respectively in Tables 8.6.3-1,2,3, to determine ,  and  respectively for single codeword PUSCH transmissions, and

- the higher layer indexes , ![](media_svg/image395.svg) [公式≈: ^{I}offset^{HARQ},MC^{−}^{ACK},set2,X],  and  in place of , ![](media_svg/image387.svg) [公式≈: ^{I}offset^{HARQ},MC^{−}^{ACK},X],  and  respectively in Tables 8.6.3-1,2,3, to determine ,  and  respectively for multiple codeword PUSCH transmissions.

Table 8.6.3-1: Mapping of HARQ-ACK offset or AUL-UCI offset values and the index signalled by higher layers

| or  or $ I_{offset}^{AUL-UCI}$ | or $\beta  _{offset}^{AUL-UCI}$ |
| --- | --- |
| 0 | 2.000 |
| 1 | 2.500 |
| 2 | 3.125 |
| 3 | 4.000 |
| 4 | 5.000 |
| 5 | 6.250 |
| 6 | 8.000 |
| 7 | 10.000 |
| 8 | 12.625 |
| 9 | 15.875 |
| 10 | 20.000 |
| 11 | 31.000 |
| 12 | 50.000 |
| 13 | 80.000 |
| 14 | 126.000 |
| 15 | 1.0 |

Table 8.6.3-2: Mapping of RI offset values and the index signalled by higher layers

| or |  |
| --- | --- |
| 0 | 1.250 |
| 1 | 1.625 |
| 2 | 2.000 |
| 3 | 2.500 |
| 4 | 3.125 |
| 5 | 4.000 |
| 6 | 5.000 |
| 7 | 6.250 |
| 8 | 8.000 |
| 9 | 10.000 |
| 10 | 12.625 |
| 11 | 15.875 |
| 12 | 20.000 |
| 13 | reserved |
| 14 | reserved |
| 15 | reserved |

Table 8.6.3-3: Mapping of CQI offset values and the index signalled by higher layers

| or |  |
| --- | --- |
| 0 | reserved |
| 1 | reserved |
| 2 | 1.125 |
| 3 | 1.250 |
| 4 | 1.375 |
| 5 | 1.625 |
| 6 | 1.750 |
| 7 | 2.000 |
| 8 | 2.250 |
| 9 | 2.500 |
| 10 | 2.875 |
| 11 | 3.125 |
| 12 | 3.500 |
| 13 | 4.000 |
| 14 | 5.000 |
| 15 | 6.250 |

## 8.7 UE transmit antenna selection

UE transmit antenna selection is configured by higher layers via parameter ue-TransmitAntennaSelection. The UE is not expected to be simultaneously configured with SRS-Antenna-Switching-2T4R and ue-TransmitAntennaSelection.

A UE configured with transmit antenna selection for a serving cell is not expected to

- be configured with more than one antenna port for any uplink physical channel or signal for any configured serving cell, or

- be configured with trigger type 1 SRS transmission on any configured serving cell, or

- be configured with simultaneous PUCCH and PUSCH transmission, or

- receive DCI Format 0 indicating uplink resource allocation type 1 for any serving cell, or

- be configured with a SCG.

If UE transmit antenna selection is disabled or not supported by the UE, the UE shall transmit from UE port 0.

If closed-loop UE transmit antenna selection is enabled by higher layers the UE shall perform transmit antenna selection for PUSCH in subframe n in response to the most recent command received via DCI Format 0 in subframe n-4 or earlier (see Clause 5.3.3.2 of [4]).

If a UE is configured with more than one serving cell, and for a group of cells belonging to bands that are signalled to be switched together in txAntennaSwitchUL the UE may assume the same transmit antenna port value is indicated in each PDCCH/EPDCCH with DCI format 0 in a given subframe.

If open-loop UE transmit antenna selection is enabled by higher layers, the transmit antenna for PUSCH to be selected by the UE is not specified.

## 8.8 Transmission timing adjustments

The higher layers indicate the 16-bit UL Grant to the physical layer, as defined in [11]. This is referred to the UL Grant in the physical layer. The content of these 16 bits starting with the MSB and ending with the LSB are as follows:

- Hopping flag – 1 bit, as described in Clause 6.2

- Fixed size resource block assignment – 10 bits, as described in Clause 6.2

- Truncated modulation and coding scheme – 4 bits, as described in Clause 6.2

- CQI request – 1 bit, as described in Clause 6.2

# 9 Physical downlink control channel procedures

If the UE is configured with a SCG, the UE shall apply the procedures described in this clause for both MCG and SCG

- When the procedures are applied for MCG, the terms 'secondary cell', 'secondary cells' , 'serving cell', 'serving cells' in this clause refer to secondary cell, secondary cells, serving cell, serving cells belonging to the MCG respectively.

- When the procedures are applied for SCG, the terms 'secondary cell', 'secondary cells', 'serving cell', 'serving cells' in this clause refer to secondary cell, secondary cells (not including PSCell), serving cell, serving cells belonging to the SCG respectively. The term 'primary cell' in this clause refers to the PSCell of the SCG.

If a UE is configured with a LAA Scell, the UE shall apply the procedures described in this clause assuming frame structure type 1 for the LAA Scell unless stated otherwise.

For a UE configured with EN-DC/NE-DC and more than one serving cell, if primary cell frame structure type 1 and if the UE is configured with tdm-PatternConfig/tdm-PatternConfigNE-DC for the primary cell, or if the UE is configured with tdm-PatternConfig2 for a primary cell with EN-DC, the UE is not expected to be configured with carrier indicator field in any of the serving cells.

## 9.1 UE procedure for determining physical downlink control channel assignment

### 9.1.1 PDCCH assignment procedure

The control region of each serving cell consists of a set of CCEs, numbered from 0 to  according to Clause 6.8.1 in [3], where  is the total number of CCEs in the control region of subframe . 
The UE shall monitor a set of PDCCH candidates on one or more activated serving cells as configured by higher layer signalling for control information, where monitoring implies attempting to decode each of the PDCCHs in the set according to all the monitored DCI formats.

A BL/CE UE is not required to monitor PDCCH.

A UE is not required to monitor PDCCH in an MBSFN subframe with zero-size non-MBSFN region.

The set of PDCCH candidates to monitor are defined in terms of search spaces, where a search space  at aggregation level  is defined by a set of PDCCH candidates. For each serving cell on which PDCCH is monitored, the CCEs corresponding to PDCCH candidate m of the search space  are given by

where is defined below, . For the common search space . For the PDCCH UE specific search space, for the serving cell on which PDCCH is monitored, if the monitoring UE is configured with carrier indicator field then  for =0 and ![](media_svg/image411.svg) [公式≈: m&apos;=m+^{n}_{⊆}_{x}^{CI}_{=}^{−}_{0}^{1}M_{x}^{(}^{L}^{)}] for >0 where  is the carrier indicator field value and ![](media_svg/image412.svg) [公式≈: _{M}_{x}(L)] is the reference number of PDCCH candidates for a carrier indicator field value "x", else if the monitoring UE is not configured with carrier indicator field then , where .  is the number of PDCCH candidates to monitor in the given search space for the scheduled serving cell. If the monitoring UE is configured with higher layer parameter shortTTI, for monitoring DCI format 7-0A/7-0B/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G, is replaced by the corresponding element of higher layer parameter dci7-CandidatesPerAL-PDCCH. If a carrier indicator field value "x" corresponds to a LAA SCell and the monitoring UE is configured with uplink transmission on the LAA SCell,![](media_svg/image415.svg) [公式≈: _{M}_{x}(L)] is the maximum number of  over all configured DCI formats for the LAA SCell. Otherwise, ![](media_svg/image415.svg) [公式≈: _{M}_{x}(L)] is determined according to Table 9.1.1-1 by replacing  with ![](media_svg/image415.svg) [公式≈: _{M}_{x}(L)].

If a UE is configured with higher layer parameter cif-InSchedulingCell-r13, the carrier indicator field value corresponds to cif-InSchedulingCell-r13, otherwise, the carrier indicator field value is the same as ServCellIndex given in [11].

If a UE is configured with a LAA SCell for UL transmissions, and if the UE is configured with higher layer parameter cif-InSchedulingCell-r14 for the LAA SCell, the carrier indicator field value in PDCCH scheduling PUSCH corresponds to cif-InSchedulingCell-r14, otherwise, the carrier indicator field value is the same as ServCellIndex given in [11].

The UE shall monitor one common search space in every non-DRX subframe at each of the aggregation levels 4 and 8 on the primary cell.

A UE shall monitor common search space on a cell to decode the PDCCHs necessary to receive MBMS on that cell when configured by higher layers. In addition to applying the procedures described in this Clause for determining PDCCH assignment for non-MBSFN subframes on a MBMS-dedicated cell to receive MBMS on that cell when configured by higher layers, the UE shall also monitor a common search space ![](media_svg/image416.svg) [公式≈: _{S}_{k}(L)] at aggregation level ![](media_svg/image417.svg) [公式: L=16] with a single PDCCH candidate ![](media_svg/image418.svg) [公式≈: _{M}()L_{=}_{1}] and ![](media_svg/image419.svg) [公式≈: ^{Y}k] set to 0.

If a UE is not configured for EPDCCH monitoring, and if the UE is not configured with a carrier indicator field, then the UE shall monitor one PDCCH UE-specific search space at each of the aggregation levels 1, 2, 4, 8 on each activated serving cell in every non-DRX subframe.

If a UE is not configured for EPDCCH monitoring, and if the UE is configured with a carrier indicator field, then the UE shall monitor one or more UE-specific search spaces at each of the aggregation levels 1, 2, 4, 8 on one or more activated serving cells as configured by higher layer signalling in every non-DRX subframe.

If a UE is configured for EPDCCH monitoring on a serving cell, and if that serving cell is activated, and if the UE is not configured with a carrier indicator field, then the UE shall monitor one PDCCH UE-specific search space at each of the aggregation levels 1, 2, 4, 8 on that serving cell in all non-DRX subframes where EPDCCH is not monitored on that serving cell.

If a UE is configured for EPDCCH monitoring on a serving cell, and if that serving cell is activated, and if the UE is configured with a carrier indicator field, then the UE shall monitor one or more PDCCH UE-specific search spaces at each of the aggregation levels 1, 2, 4, 8 on that serving cell as configured by higher layer signalling in all non-DRX subframes where EPDCCH is not monitored on that serving cell.

A UE is not expected to monitor PDCCH candidates with DCI format 0/1/1A/2/2A/2B/2C/2D mapped onto the UE-specific search space, and with the CRC scrambled by the SPS C-RNTI, when the UE is configured with higher layer parameter shortProcessingTime.

A UE is not expected to monitor PDCCH candidates with DCI format 7-0A/7-0B/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G over more than

- 28 CCEs on a serving cell if the higher layer parameter dl-STTI-Length is set to 'subslot'.

- 32 CCEs on a serving cell if the higher layer parameter dl-STTI-Length is set to 'slot'.

A UE is not expected to be configured to monitor more than

- 6 PDCCH candidates with DCI format 7-0A/7-0B/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G on a service cell in a subslot if the higher layer parameter dl-STTI-Length is set to 'subslot'

- 12 PDCCH candidates with DCI format 7-0A/7-0B/7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G on a serving cell in a slot if the higher layer parameter dl-STTI-Length is set to 'slot'.

The UE is not expected to be configured to monitor PDCCH corresponding to DCI format 7-0A/7-0B /7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G with carrier indicator field in a given serving cell.

A UE configured with higher layer parameter shortTTI for a serving cell is not required to monitor PDCCH for the serving cell on any other serving cell.

The UE is not expected to be configured to monitor PDCCH corresponding to DCI format 7-0A/7-0B /7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G when CFI value is 3 and ![](media_svg/image420.svg) [公式: N_{RB}^{DL}≥10].

The common and PDCCH UE-specific search spaces on the primary cell may overlap. If the UE is configured with higher layer parameter shortProcessingTime, a PDCCH with DCI format 0/1A detected in the overlap shall be considered by the UE as having been received in the PDCCH common search space.

A UE configured with the carrier indicator field associated with monitoring PDCCH on serving cell c shall monitor PDCCH configured with carrier indicator field and with CRC scrambled by C-RNTI in the PDCCH UE specific search space of serving cell c.

A UE configured with the carrier indicator field associated with monitoring PDCCH on the primary cell shall monitor PDCCH configured with carrier indicator field and with CRC scrambled by SPS C-RNTI or UL-SPS-V-RNTI in the PDCCH UE specific search space of the primary cell.

The UE shall monitor the common search space for PDCCH without carrier indicator field.

For the serving cell on which PDCCH is monitored, if the UE is not configured with a carrier indicator field, it shall monitor the PDCCH UE specific search space for PDCCH without carrier indicator field, if the UE is configured with a carrier indicator field it shall monitor the PDCCH UE specific search space for PDCCH with carrier indicator field.

If the UE is not configured with a LAA Scell, the UE is not expected to monitor the PDCCH of a secondary cell if it is configured to monitor PDCCH with carrier indicator field corresponding to that secondary cell in another serving cell.

If the UE is configured with a LAA Scell, the UE is not expected to monitor the PDCCH UE specific space of the LAA SCell if it is configured to monitor PDCCH with carrier indicator field corresponding to that LAA Scell in another serving cell,

- where the UE is not expected to be configured to monitor PDCCH with carrier indicator field in an LAA Scell;

- where the UE is not expected to be scheduled with PDSCH starting in the second slot in a subframe in an LAA Scell if the UE is configured to monitor PDCCH with carrier indicator field corresponding to that LAA Scell in another serving cell.

For the serving cell on which PDCCH is monitored, the UE shall monitor PDCCH candidates at least for the same serving cell.

A UE configured to monitor PDCCH candidates with CRC scrambled by C-RNTI, SPS C-RNTI or UL-SPS-V-RNTI with a common payload size and with the same first CCE index  (as described in Clause 10.1) but with different sets of DCI information fields as defined in [4] in the

- common search space

- PDCCH UE specific search space

on the primary cell shall assume that for the PDCCH candidates with CRC scrambled by C-RNTI, SPS C-RNTI or UL-SPS-V-RNTI,

if the UE is configured with the carrier indicator field associated with monitoring the PDCCH on the primary cell, only the PDCCH in the common search space is transmitted by the primary cell;

otherwise, only the PDCCH in the UE specific search space is transmitted by the primary cell.

A UE configured to monitor PDCCH candidates in a given serving cell with a given DCI format size with CIF, and CRC scrambled by C- RNTI, where the PDCCH candidates may have one or more possible values of CIF for the given DCI format size, shall assume that a PDCCH candidate with the given DCI format size may be transmitted in the given serving cell in any PDCCH UE specific search space corresponding to any of the possible values of CIF for the given DCI format size.

If a serving cell is a LAA Scell, and if the higher layer parameter subframeStartPosition for the Scell indicates 's07',

- The UE monitors PDCCH UE-specific search space candidates on the Scell in both the first and second slots of a subframe, and the aggregation levels defining the search spaces are listed in Table 9.1.1-1A;

otherwise,

- The aggregation levels defining the search spaces are listed in Table 9.1.1-1.

If a serving cell is a LAA Scell, the UE may receive PDCCH with DCI CRC scrambled by CC-RNTI as described in Clause 13A on the LAA Scell.

The DCI formats that the UE shall monitor depend on the configured transmission mode per each serving cell as defined in Clause 7.1.

If a UE is configured with higher layer parameter skipMonitoringDCI-format0-1A for a serving cell, the UE is not required to monitor the PDCCH with DCI Format 0/1A in the UE specific search space for that serving cell.

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured with higher layer parameter skipMonitoringDCI-format0A for the LAA SCell, the UE is not required to monitor the PDCCH with DCI Format 0A in the UE specific search space for the LAA SCell.

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured in transmission mode 2 and if the UE is configured with higher layer parameter skipMonitoringDCI-format4A for the LAA SCell, the UE is not required to monitor the PDCCH with DCI Format 4A in the UE specific search space for the LAA SCell.

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured with higher layer parameter enableMonitoringDCI-format0B for the LAA SCell, the UE is required to monitor the PDCCH with DCI Format 0B in the UE specific search space for the LAA SCell.

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured in transmission mode 2 and if the UE is configured with higher layer parameter enableMonitoringDCI-format4B for the LAA SCell, the UE is required to monitor the PDCCH with DCI Format 4B in the UE specific search space for the LAA SCell.

If a UE is not configured for PUSCH/PUCCH transmission for at least one TDD serving cell, the UE is not expected to monitor PDCCH on serving cell ![](media_svg/image198.svg) [公式≈: ^{c}1] if the PDCCH overlaps in time with SRS transmission (including any interruption due to uplink or downlink RF retuning time [10]) on TDD serving cell ![](media_svg/image199.svg) [公式≈: ^{c}2] not configured for PUSCH/PUCCH transmission, and if the UE is not capable of simultaneous reception and transmission on serving cell ![](media_svg/image198.svg) [公式≈: ^{c}1]and serving cell ![](media_svg/image200.svg) [公式≈: ^{c}2].

If a UE is configured with higher layer parameter pdcch-candidateReductions for a UE specific search space at aggregation level L for a serving cell, the corresponding number of PDCCH candidates is given by ![](media_svg/image422.svg) [公式≈: M^{(}^{L}^{)}=round(a≠M^{(}_{full}^{L}^{)})], where the value of ![](media_svg/image423.svg) [公式: a] is determined according to Table 9.1.1-2 and ![](media_svg/image424.svg) [公式≈: ^{M}^{(}full^{L}^{)}] is determined according to Table 9.1.1-1 by replacing ![](media_svg/image425.svg) [公式≈: _{M}(L)]with ![](media_svg/image426.svg) [公式≈: ^{M}^{(}full^{L}^{)}].

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured with higher layer parameter pdcch-candidateReductions-Format0A for a UE specific search space at aggregation level L for the LAA SCell, the corresponding number of PDCCH candidates for DCI format 0A is given by ![](media_svg/image422.svg) [公式≈: M^{(}^{L}^{)}=round(a≠M^{(}_{full}^{L}^{)})], where the value of ![](media_svg/image423.svg) [公式: a] is determined according to Table 9.1.1-2 and ![](media_svg/image424.svg) [公式≈: ^{M}^{(}full^{L}^{)}] is determined according to Table 9.1.1-1 by replacing ![](media_svg/image425.svg) [公式≈: _{M}(L)]with ![](media_svg/image426.svg) [公式≈: ^{M}^{(}full^{L}^{)}].

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured with higher layer parameter pdcch-candidateReductions-Format0B-4A-4B-AL1-2 for a UE specific search space of the first and second aggregation level for the LAA SCell, the corresponding number of PDCCH candidates for DCI format 0B/4A/4B is given by ![](media_svg/image422.svg) [公式≈: M^{(}^{L}^{)}=round(a≠M^{(}_{full}^{L}^{)})], where the value of ![](media_svg/image423.svg) [公式: a] is determined according to Table 9.1.1-2 and ![](media_svg/image424.svg) [公式≈: ^{M}^{(}full^{L}^{)}] is determined according to Table 9.1.1-1 by replacing ![](media_svg/image425.svg) [公式≈: _{M}(L)]with ![](media_svg/image426.svg) [公式≈: ^{M}^{(}full^{L}^{)}].

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured with higher layer parameter pdcch-candidateReductions-Format0B-4A-4B-AL3-4 for a UE specific search space of the third and fourth aggregation level for the LAA SCell, the corresponding number of PDCCH candidates for DCI format 0B/4A/4B is given by ![](media_svg/image422.svg) [公式≈: M^{(}^{L}^{)}=round(a≠M^{(}_{full}^{L}^{)})], where the value of ![](media_svg/image423.svg) [公式: a] is determined according to Table 9.1.1-3 and ![](media_svg/image424.svg) [公式≈: ^{M}^{(}full^{L}^{)}] is determined according to Table 9.1.1-1 by replacing ![](media_svg/image425.svg) [公式≈: _{M}(L)]with ![](media_svg/image426.svg) [公式≈: ^{M}^{(}full^{L}^{)}].

Table 9.1.1-1: PDCCH candidates monitored by a UE

| Search space |  |  | Number of PDCCH  candidates |
| --- | --- | --- | --- |
| Type | Aggregation level | Size [in CCEs] |  |
| UE-specific | 1 | 6 | 6 |
|  | 2 | 12 | 6 |
|  | 4 | 8 | 2 |
|  | 8 | 16 | 2 |
| Common | 4 | 16 | 4 |
|  | 8 | 16 | 2 |

Note: the Size [in CCEs] is given assuming ![](media_svg/image423.svg) [公式: a] =1

Table 9.1.1-1A: PDCCH UE-specific search space candidates monitored by a UE on LAA Scell

| Search space |  |  | Number of PDCCH  candidates  in first slot | Number of PDCCH  candidates  in second slot |
| --- | --- | --- | --- | --- |
| Type | Aggregation level | Size [in CCEs] |  |  |
| UE-specific | 1 | 6 | 6 | 6 |
|  | 2 | 12 | 6 | 6 |
|  | 4 | 8 | 2 | 2 |
|  | 8 | 16 | 2 | 2 |

Note: the Size [in CCEs] is given assuming ![](media_svg/image423.svg) [公式: a] =1

Table 9.1.1-2: Scaling factor for PDCCH candidates reduction

| pdcch-candidateReductions | Value of ![](media_svg/image428.svg) [公式: a] |
| --- | --- |
| 0 | 0 |
| 1 | 0.33 |
| 2 | 0.66 |
| 3 | 1 |

Table 9.1.1-3: Scaling factor for PDCCH candidates reduction

| pdcch-candidateReductions | Value of ![](media_svg/image428.svg) [公式: a] |
| --- | --- |
| 0 | 0 |
| 1 | 0.5 |
| 2 | 1 |
| 3 | 1.5 |

For the common search spaces, is set to 0 for the two aggregation levels  and .

For the UE-specific search space  at aggregation level, the variable is defined by

where , ,  and ,  is the slot number within a radio frame. 
The RNTI value used for  is defined in Clause 7.1 in downlink and Clause 8 in uplink.

### 9.1.2 PHICH assignment procedure

If a UE is not configured with multiple TAGs, or if a UE is configured with multiple TAGs and PUSCH transmissions scheduled from serving cell in subframe n are not scheduled by a Random Access Response Grant corresponding to a random access preamble transmission for a secondary cell

- For PUSCH transmissions scheduled from serving cell in subframe n, the UE shall determine the corresponding PHICH resource of serving cell  in subframe , where

-  is always 4 for FDD.

- is 6 for FDD-TDD and serving cell c frame structure type 2 and the PUSCH transmission is for another serving cell with frame structure type 1.

- is 4 for FDD-TDD and serving cell c frame structure type 1and the PUSCH transmission is for a serving cell with frame structure type 1.

- is given in table 9.1.2-1 for FDD-TDD and serving cell c frame structure type 1 and the PUSCH transmission is for another serving cell with frame structure type 2.

- For TDD, if the UE is not configured with EIMTA-MainConfigServCell-r12 for any serving cell and, if the UE is configured with one serving cell, or if the UE is configured with more than one serving cell and the TDD UL/DL configuration of all the configured serving cells is the same, for PUSCH transmissions scheduled from serving cell in subframe n, the UE shall determine the corresponding PHICH resource of serving cell  in subframe , where  is given in table 9.1.2-1 if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, otherwise  is given in Table 9.1.2-3.

- For TDD, if the UE is configured with more than one serving cell and the TDD UL/DL configuration of at least two configured serving cells is not the same, or if the UE is configured with EIMTA-MainConfigServCell-r12 for at least one serving cell , or for FDD-TDD and serving cell frame structure type 2, for PUSCH transmissions scheduled from serving cell in subframe n, the UE shall determine the corresponding PHICH resource of serving cell  in subframe , where is given in table 9.1.2-1 if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 for the serving cell, otherwise  is given in Table 9.1.2-3, where the "TDD UL/DL Configuration" in the rest of this Clause refers to the UL-reference UL/DL configuration (defined in Clause 8.0) of the serving cell corresponding to the PUSCH transmission.

If a UE is configured with multiple TAGs, for PUSCH transmissions on subframe n for a secondary cell  scheduled by a Random Access Response grant corresponding to a random access preamble transmission for the secondary cell ,

- For TDD, if the UE is configured with more than one serving cell and the TDD UL/DL configuration of at least two configured serving cells is not the same, or if the UE is configured with EIMTA-MainConfigServCell-r12 for at least one serving cell, or for FDD-TDD and serving cell  frame structure type 2, the "TDD UL/DL Configuration" in the rest of this Clause refers to the UL-reference UL/DL configuration (defined in Clause 8.0) of secondary cell .

- If the UE is not configured to monitor PDCCH/EPDCCH with carrier indicator field corresponding to secondary cell  in another serving cell, the UE shall determine the corresponding PHICH resource on the secondary cell  in subframe , where

- is always 4 for FDD and where  is given in table 9.1.2-1 if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 for the secondary cell , otherwise  is given in Table 9.1.2-3 for TDD.

- is 4 for FDD-TDD and secondary cell  frame structure type 1.

-  is given in table 9.1.2-1 if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 for the secondary cell , otherwise  is given in Table 9.1.2-3 for FDD-TDD and secondary cell  frame structure type 2

- If the UE is configured to monitor PDCCH/EPDCCH with carrier indicator field corresponding to secondary cell  in another serving cell , the UE configured with multiple TAGs shall determine the corresponding PHICH resource on the serving cell  in subframe , where

- is always 4 for FDD and where  is given in table 9.1.2-1 if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 for the secondary cell , otherwise  is given in Table 9.1.2-3 for TDD.

- is 4 for FDD-TDD and primary cell frame structure type 1 and frame structure type 1 for secondary cell  and serving cell

-  is given in table 9.1.2-1 if the UE is not configured with higher layer parameter symPUSCH-UpPts-r14 for the secondary cell , otherwise  is given in Table 9.1.2-3 for FDD-TDD and serving cell c frame structure type 2

-  is 6 for FDD-TDD and serving cell c frame structure type 1 and serving cell frame structure type 2

For subframe bundling operation, the corresponding PHICH resource is associated with the last subframe in the bundle.

Table 9.1.2-1:  for TDD

| TDD UL/DL Configuration | subframe index n |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 0 |  |  | 4 | 7 | 6 |  |  | 4 | 7 | 6 |
| 1 |  |  | 4 | 6 |  |  |  | 4 | 6 |  |
| 2 |  |  | 6 |  |  |  |  | 6 |  |  |
| 3 |  |  | 6 | 6 | 6 |  |  |  |  |  |
| 4 |  |  | 6 | 6 |  |  |  |  |  |  |
| 5 |  |  | 6 |  |  |  |  |  |  |  |
| 6 |  |  | 4 | 6 | 6 |  |  | 4 | 7 |  |

Table 9.1.2-3:  for TDD and UE configured with symPUSCH-UpPts-r14

| TDD UL/DL Configuration | subframe index n |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 0 |  | 5 | 4 | 7 | 6 |  | 5 | 4 | 7 | 6 |
| 1 |  | 5 | 4 | 6 |  |  | 5 | 4 | 6 |  |
| 2 |  | 7 | 6 |  |  |  | 7 | 6 |  |  |
| 3 |  | 7 | 6 | 6 | 6 |  |  |  |  |  |
| 4 |  | 7 | 6 | 6 |  |  |  |  |  |  |
| 5 |  | 7 | 6 |  |  |  |  |  |  |  |
| 6 |  | 4 | 4 | 6 | 6 |  | 4 | 4 | 7 |  |

The PHICH resource is identified by the index pairwhere is the PHICH group number and is the orthogonal sequence index within the group as defined by:

where

is mapped from the cyclic shift for DMRS field (according to Table 9.1.2-2) in the most recent PDCCH/EPDCCH with uplink DCI format [4] for the transport block(s) associated with the corresponding PUSCH transmission. shall be set to zero, if there is no PDCCH/EPDCCH with uplink DCI format for the same transport block, and

if the initial PUSCH for the same transport block is semi-persistently scheduled, or

if the initial PUSCH for the same transport block is scheduled by the random access response grant .

is the spreading factor size used for PHICH modulation as described in Clause 6.9.1 in [3].

![](media_svg/image451.svg) [公式≈: _{I}_{PRB}_{_}_{RA}_{=}√_{⌡}_{⌡}_{⌡}_{⌡}_{⌠}_{⌡}_{⌡}_{⌡}_{⌡}_{∞}_{I}_{I}_{PRB}_{PRB}_{lowest}_{lowest}_{_}_{_}_{RA}_{RA}_{_}_{_}_{index}_{index}_{+}_{1}for the_{TBs}_{for }_{no}_{PDCCH/EPDC}_{associated}_{a}_{is}_{second}_{not }first _{equal}TB_{TB}_{PDCCH/EPDC}of_{CH}_{ to}_{of}a_{ the}_{a}_{associated}PUSCH_{PUSCH}_{number } with _{ with }_{CH}_{ with the}_{of}_{when the}associated_{TBs}_{associated}_{indicated}_{correspond}_{number }PDCCH/EPDC_{PDCCH/EPDC}_{in the}_{ing}_{of}_{PUSCH}_{most }_{negatively}_{recent }CH_{CH}or _{acknowledg}for thecase_{ed}of] where  is the lowest PRB index in the first slot of the corresponding PUSCH transmission

is the number of PHICH groups configured by higher layers as described in Clause 6.9 of [3],

Table 9.1.2-2: Mapping between  and the cyclic shift for DMRS field
 in PDCCH/EPDCCH with uplink DCI format in [4]

| Cyclic Shift for DMRS Field in PDCCH/EPDCCH  with uplink DCI format in [4] |  |
| --- | --- |
| 000 | 0 |
| 001 | 1 |
| 010 | 2 |
| 011 | 3 |
| 100 | 4 |
| 101 | 5 |
| 110 | 6 |
| 111 | 7 |

### 9.1.3 Control Format Indicator (CFI) assignment procedure

For a serving cell, if a UE is configured with higher layer parameter cfi-SlotSubslotNonMBSFN, the UE shall assume the CFI is equal to the value of the higher layer parameter cfi-SlotSubslotNonMBSFN for non-MBSFN subframes for receiving physical downlink shared channel with slot/subslot duration.

For a serving cell, if a UE is configured with higher layer parameter cfi-SlotSubslotMBSFN, the UE shall assume the CFI is equal to the value of the higher layer parameter cfi-SlotSubslotMBSFN for MBSFN subframes for receiving physical downlink shared channel with slot/subslot duration.

For a serving cell using frame structure 2, if a UE is configured with higher layer parameter cfi-PatternSlotSubslot, the UE shall assume the CFI is equal to the value of the higher layer parameter cfi-PatternSlotSubslot for the subframes for receiving physical downlink shared channel with slot duration.

For a serving cell, if a UE is configured with higher layer parameter cfi-SubframeNonMBSFN, the UE shall assume the CFI is equal to the value of the higher layer parameter cfi-SubframeNonMBSFN for non-MBSFN subframes for receiving physical downlink shared channel with subframe duration.

For a serving cell, if a UE is configured with higher layer parameter cfi-SubframeMBSFN, the UE shall assume the CFI is equal to the value of the higher layer parameter cfi-SubframeMBSFN for MBSFN subframes for receiving physical downlink shared channel with subframe duration.

For a serving cell using frame structure 2, if a UE is configured with higher layer parameter cfi-PatternSubframe, the UE shall assume the CFI is equal to the value of the higher layer parameter cfi-PatternSubframe for the subframes for receiving physical downlink shared channel with subframe duration.

For a serving cell, if a UE is configured with higher layer parameters cfi-SubframeNonMBSFN and cfi-SlotSubslotNonMBSFN, the UE is not expected to be configured with different values of cfi-SlotSubslotNonMBSFN and cfi-SubframeNonMBSFN.

For a serving cell, if a UE is configured with higher layer parameters cfi-SubframeMBSFN and cfi-SlotSubslotMBSFN, the UE is not expected to be configured with different values of cfi-SlotSubslotMBSFN and cfi-SubframeMBSFN.

For a serving cell using frame structure 2, if a UE is configured with higher layer parameters cfi-PatternSlotSubslot and cfi-PatternSubframe, the UE is not expected to be configured with different values of cfi-PatternSlotSubslot and cfi-PatternSubframe.

PHICH duration is signalled by higher layers according to Table 6.9.3-1 in [3]. The duration signalled puts a lower limit on the size of the control region determined from the control format indicator (CFI). When , if extended PHICH duration is indicated by higher layers then the UE shall assume that CFI is equal to PHICH duration.

In subframes indicated by higher layers to decode PMCH, when , a UE may assume that CFI is equal to the value of the higher layer parameter non-MBSFNregionLength [11].

For a MBMS-dedicated cell, if a UE is configured with higher layer parameter semiStaticCFI-MBMS included in MasterInformationBlock-MBMS, the UE shall assume the CFI is equal to the value of the higher layer parameter semiStaticCFI-MBMS for non-MBSFN subframes if a non-zero value is indicated by semiStaticCFI-MBMS.

### 9.1.4 EPDCCH assignment procedure

For each serving cell, higher layer signalling can configure a UE with one or two EPDCCH-PRB-sets for EPDCCH monitoring. The PRB-pairs corresponding to an EPDCCH-PRB-set are indicated by higher layers as described in Clause 9.1.4.4. Each EPDCCH-PRB-set consists of set of ECCEs numbered from 0 to where is the number of ECCEs in EPDCCH-PRB-set  of subframe . Each EPDCCH-PRB-set can be configured for either localized EPDCCH transmission or distributed EPDCCH transmission.

The UE shall monitor a set of EPDCCH candidates on one or more activated serving cells as configured by higher layer signalling for control information, where monitoring implies attempting to decode each of the EPDCCHs in the set according to the monitored DCI formats.

A BL/CE UE is not required to monitor EPDCCH.

A UE configured with higher layer parameter shortProcessingTime or shortTTI for a serving cell is not required to monitor EPDCCH for the serving cell or on that serving cell.

If a UE is configured with higher layer parameter shortTTI for a serving cell, and if the UE does not support epdcch-STTI-differentCells-r15 (3GPP TS 36.331 [11]), the UE is not expected to monitor EPDCCH for any serving cell.

If a UE is configured with higher layer parameter shortProcessingTime for a serving cell, and if the UE does not support epdcch-SPT-differentCells-r15 (3GPP TS 36.331 [11]), the UE is not expected to monitor EPDCCH for any serving cell.

A UE is not required to monitor EPDCCH in an MBSFN subframe with zero-size non-MBSFN region.

The set of EPDCCH candidates to monitor are defined in terms of EPDCCH UE-specific search spaces.

For each serving cell, the subframes in which the UE monitors EPDCCH UE-specific search spaces are configured by higher layers.

The UE shall not monitor EPDCCH

- For TDD and normal downlink CP, in special subframes for the special subframe configurations 0 and 5, or for frame structure type 3, in the subframe with the same duration as the DwPTS duration of the special subframe configurations 0 and 5, shown in Table 4.2-1 of [3], or for the special subframe configuration 10 configured by the higher layer signalling ssp10-CRS-LessDwPTS.

- For TDD and extended downlink CP, in special subframes for the special subframe configurations 0, 4 and 7 shown in Table 4.2-1 of [3].

- In subframes indicated by higher layers to decode PMCH.

- For TDD and if the UE is configured with different UL/DL configurations for the primary and a secondary cell, in a downlink subframe on the secondary cell when the same subframe on the primary cell is a special subframe and the UE is not capable of simultaneous reception and transmission on the primary and secondary cells.

An EPDCCH UE-specific search space at aggregation level  is defined by a set of EPDCCH candidates.

For an EPDCCH-PRB-set , the ECCEs corresponding to EPDCCH candidate m of the search space  are given by

![](media_svg/image462.svg) [公式≈: L^{√}^{⌡}⌠_{⌡}_{∞}^{⊇}^{⊕}_{⊕}_{⊗}Yp,k+^{⋅}⋅_{⋅}_{√}^{m}_{L}^{∪}_{∪}^{N}_{M}^{ECCE}_{p}(L_{,}_{full})^{,}^{p}^{,}^{k}^{∂}∂_{∂}_{∃}+b^{⇒}^{⇐}_{⇐}_{⇔}mod√NECCE,p,k/L∃^{∅}^{⌡}∇_{⌡}_{∈}+i]

where

is defined below,

if the UE is configured with a carrier indicator field for the serving cell on which EPDCCH is monitored, otherwise

is the carrier indicator field value,

![](media_svg/image466.svg) [公式≈: ^{M}p^{(}^{L},full^{)}] is the maximum number of EPDCCH candidates among all the configured DCI formats over all the configured carrier indicator field values for an aggregation level L in EPDCCH-PRB-set p if the UE is configured with uplink transmission on a LAA SCell, otherwise, ![](media_svg/image467.svg) [公式≈: ^{M}p^{(}^{L},full^{)}] is the nominal number of EPDCCH candidates at aggregation level L in EPDCCH-PRB-set p determined according to Tables 9.1.4-1a to 9.1.4-5b by replacing ![](media_svg/image468.svg) [公式≈: _{M}_{p}(L)] with ![](media_svg/image467.svg) [公式≈: ^{M}p^{(}^{L},full^{)}],

.

If the UE is not configured with a carrier indicator field for the serving cell on which EPDCCH is monitored,  is the number of EPDCCH candidates to monitor at aggregation level  in EPDCCH-PRB-set  for the serving cell on which EPDCCH is monitored, as given in Tables 9.1.4-1a, 9.1.4-1b, 9.1.4-2a, 9.1.4-2b, 9.1.4-3a, 9.1.4-3b, 9.1.4-4a, 9.4.4-4b, 9.1.4-5a, 9.1.4-5b below; otherwise,  is the number of EPDCCH candidates to monitor at aggregation level  in EPDCCH-PRB-set  for the serving cellindicated by .

If a UE is configured with higher layer parameter pdcch-candidateReductions for a specific search space at aggregation level L in EPDCCH-PRB-set  for a serving cell, the corresponding number of EPDCCH candidates is given by ![](media_svg/image472.svg) [公式≈: M_{p}^{(}^{L}^{)}=round(a≠M_{p}^{(}^{L}_{,}^{)}_{full})], where the value of ![](media_svg/image423.svg) [公式: a] is determined according to Table 9.1.1-2 and ![](media_svg/image473.svg) [公式≈: ^{M}p^{(}^{L},^{)}full] is determined according to Tables 9.1.4-1a to 9.1.4-5b by replacing ![](media_svg/image468.svg) [公式≈: _{M}_{p}(L)]with ![](media_svg/image474.svg) [公式≈: ^{M}p^{(}^{L},^{)}full].

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured with higher layer parameter pdcch-candidateReductions-Format0A for a UE specific search space at aggregation level L in EPDCCH-PRB-set  for the LAA SCell, the corresponding number of EPDCCH candidates for DCI format 0A is given by ![](media_svg/image472.svg) [公式≈: M_{p}^{(}^{L}^{)}=round(a≠M_{p}^{(}^{L}_{,}^{)}_{full})], where the value of ![](media_svg/image423.svg) [公式: a] is determined according to Table 9.1.1-2 and ![](media_svg/image473.svg) [公式≈: ^{M}p^{(}^{L},^{)}full] is determined according to Tables 9.1.4-1a to 9.1.4-5b by replacing ![](media_svg/image468.svg) [公式≈: _{M}_{p}(L)]with ![](media_svg/image474.svg) [公式≈: ^{M}p^{(}^{L},^{)}full].

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured with higher layer parameter pdcch-candidateReductions-Format0B-4A-4B-AL1-2 for a UE specific search space of the first and second aggregation level in EPDCCH-PRB-set  for the LAA SCell, the corresponding number of EPDCCH candidates for DCI format 0B/4A/4B is given by ![](media_svg/image472.svg) [公式≈: M_{p}^{(}^{L}^{)}=round(a≠M_{p}^{(}^{L}_{,}^{)}_{full})], where the value of ![](media_svg/image423.svg) [公式: a] is determined according to Table 9.1.1-2 and ![](media_svg/image473.svg) [公式≈: ^{M}p^{(}^{L},^{)}full] is determined according to Tables 9.1.4-1a to 9.1.4-5b by replacing ![](media_svg/image468.svg) [公式≈: _{M}_{p}(L)]with ![](media_svg/image474.svg) [公式≈: ^{M}p^{(}^{L},^{)}full].

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured with higher layer parameter pdcch-candidateReductions-Format0B-4A-4B-AL3-5 for a UE specific search space of the third, fourth, and fifth aggregation level in EPDCCH-PRB-set  for the LAA SCell, the corresponding number of EPDCCH candidates for DCI format 0B/4A/4B is given by ![](media_svg/image472.svg) [公式≈: M_{p}^{(}^{L}^{)}=round(a≠M_{p}^{(}^{L}_{,}^{)}_{full})], where the value of ![](media_svg/image423.svg) [公式: a] is determined according to Table 9.1.1-3 and ![](media_svg/image473.svg) [公式≈: ^{M}p^{(}^{L},^{)}full] is determined according to Tables 9.1.4-1a to 9.1.4-5b by replacing ![](media_svg/image468.svg) [公式≈: _{M}_{p}(L)]with ![](media_svg/image474.svg) [公式≈: ^{M}p^{(}^{L},^{)}full].

If a UE is configured with higher layer parameter cif-InSchedulingCell-r13, the carrier indicator field value corresponds to cif-InSchedulingCell-r13, otherwise the carrier indicator field value is the same as ServCellIndex given in [11].

If a UE is configured with a LAA SCell for UL transmissions, and if the UE is configured with higher layer parameter cif-InSchedulingCell-r14 for the LAS SCell, the carrier indicator field value in EPDCCH scheduling PUSCH corresponds to cif-InSchedulingCell-r14, otherwise, the carrier indicator field value is the same as ServCellIndex given in [11].

A UE is not expected to monitor an EPDCCH candidate, if an ECCE corresponding to that EPDCCH candidate is mapped to a PRB pair that overlaps in frequency with a transmission of either PBCH or primary or secondary synchronization signals in the same subframe.

If a UE is configured with two EPDCCH-PRB-sets with the same value (where is defined in Clause 6.10.3A.1 in [3]), if the UE receives an EPDCCH candidate with a given DCI payload size corresponding to one of the EPDCCH-PRB-sets and mapped only to a given set of REs (as described in Clause 6.8A.5 in [3]), and if the UE is also configured to monitor an EPDCCH candidate with the same DCI payload size and corresponding to the other EPDCCH-PRB-set and which is mapped only to the same set of REs, and if the number of the first ECCE of the received EPDCCH candidate is used for determining PUCCH resource for HARQ-ACK transmission (as described in Clause 10.1.2 and Clause 10.1.3), the number of the first ECCE shall be determined based on EPDCCH-PRB-set .

The variable is defined by

where , , ,  and ,  is the slot number within a radio frame. The RNTI value used for  is defined in Clause 7.1 in downlink and Clause 8 in uplink. The DCI formats that the UE shall monitor depend on the configured transmission mode per each serving cell as defined in Clause 7.1.

If a UE is configured with higher layer parameter skipMonitoringDCI-format0-1A for a serving cell, the UE is not required to monitor the EPDCCH with DCI Format 0/1A in the UE specific search space for that serving cell.

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured with higher layer parameter skipMonitoringDCI-format0A for the LAA SCell, the UE is not required to monitor the EPDCCH with DCI Format 0A in the UE specific search space for the LAA SCell.

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured in transmission mode 2 and if the UE is configured with higher layer parameter skipMonitoringDCI-format4A for the LAA SCell, the UE is not required to monitor the EPDCCH with DCI Format 4A in the UE specific search space for the LAA SCell.

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured with higher layer parameter enableMonitoringDCI-format0B for the LAA SCell, the UE is required to monitor the EPDCCH with DCI Format 0B in the UE specific search space for the LAA SCell.

If a UE is configured with a LAA SCell for UL transmissions and if the UE is configured in transmission mode 2 and if the UE is configured with higher layer parameter enableMonitoringDCI-format4B for the LAA SCell, the UE is required to monitor the EPDCCH with DCI Format 4B in the UE specific search space for the LAA SCell.

If a serving cell is a LAA Scell, and if the higher layer parameter subframeStartPosition for the Scell indicates 's07'

- the UE monitors EPDCCH UE-specific search space candidates on the Scell assuming they start in both the first slot and the second slot of a subframe.

The aggregation levels defining the search spaces and the number of monitored EPDCCH candidates is given as follows

- For a UE configured with only one EPDCCH-PRB-set for distributed transmission, the aggregation levels defining the search spaces and the number of monitored EPDCCH candidates are listed in Table 9.1.4-1a, Table 9.1.4-1b.

- For a UE configured with only one EPDCCH-PRB-set for localized transmission, the aggregation levels defining the search spaces and the number of monitored EPDCCH candidates are listed in Table 9.1.4-2a, Table 9.1.4-2b.

- For a UE configured with two EPDCCH-PRB-sets for distributed transmission, the aggregation levels defining the search spaces and the number of monitored EPDCCH candidates are listed in Table 9.1.4-3a, 9.1.4-3b.

- For a UE configured with two EPDCCH-PRB-sets for localized transmission, the aggregation levels defining the search spaces and the number of monitored EPDCCH candidates are listed in Table 9.1.4-4a, 9.4.4-4b.

- For a UE configured with one EPDCCH-PRB-set for distributed transmission, and one EPDCCH-PRB-set for localized transmission, the aggregation levels defining the search spaces and the number of monitored EPDCCH candidates are listed in Table 9.1.4-5a, 9.1.4-5b.

If the UE is not configured with a carrier indicator field for the serving cell on which EPDCCH is monitored,  of the serving cell on which EPDCCH is monitored. If the UE is configured with a carrier indicator field for the serving cell on which EPDCCH is monitored,  of the serving cell indicated by .

For Tables 9.1.4-1a, 9.1.4-1b, 9.1.4-2a, 9.1.4-2b, 9.1.4-3a, 9.1.4-3b, 9.1.4-4a, 9.4.4-4b, 9.1.4-5a, 9.1.4-5b

- Case 1 applies

- for normal subframes and normal downlink CP when DCI formats 2/2A/2B/2C/2D are monitored and  , or

- for frame structure type 3, for downlink subframes with PDSCH transmissions starting in the second slot,

- for special subframes with special subframe configuration 3,4,8 for frame structure type 2 or the subframes with the same duration as the DwPTS duration of a special subframe configuration 3,4,8 for frame structure type 3, and normal downlink CP when DCI formats 2/2A/2B/2C/2D are monitored and  , or

- for normal subframes and normal downlink CP when DCI formats 1A/1B/1D/1/2/2A/2B/2C/2D/0/0A/0B/4/4A/4B/5/6-0A/6-0B/6-1A/6-1B are monitored, and when  ( defined in Clause 6.8A.1 in [3]), or

- for special subframes with special subframe configuration 3, 4, 8 for frame structure type 2 or the subframes with the same duration as the DwPTS duration of a special subframe configuration 3,4,8 for frame structure type 3, and normal downlink CP when DCI formats 1A/1B/1D/1/2A/2/2B/2C/2D/0/0A/0B/4/4A/4B/5/6-0A/6-0B/6-1A/6-1B are monitored, and when  (defined in Clause 6.8A.1 in [3]);

- Case 2 applies

- for normal subframes and extended downlink CP when DCI formats 1A/1B/1D/1/2A/2/2B/2C/2D/0/0A/0B/4/4A/4B/5/6-0A/6-0B/6-1A/6-1B are monitored or,

- for special subframes with special subframe configuration 1, 2, 6, 7, 9, 10 for frame structure type 2 or the subframes with the same duration as the DwPTS duration of a special subframe configuration 1, 2, 6, 7, 9, 10 for frame structure type 3, and normal downlink CP when DCI formats 1A/1B/1D/1/2A/2/2B/2C/2D/0/0A/0B/4/4A/4B/5/6-0A/6-0B/6-1A/6-1B are monitored, or

- for special subframes with special subframe configuration 1,2,3,5,6 and extended downlink CP when DCI formats 1A/1B/1D/1/2A/2/2B/2C/2D/0/0A/0B/4/4A/4B/5/6-0A/6-0B/6-1A/6-1B are monitored;

- otherwise

- Case 3 is applied.

is the number of PRB-pairs constituting EPDCCH-PRB-set .

Table 9.1.4-1a: EPDCCH candidates monitored by a UE 
(One Distributed EPDCCH-PRB-set - Case1, Case 2)

|  | Number of EPDCCH candidates   for Case 1 |  |  |  |  | Number of EPDCCH candidates   for Case 2 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | L=2 | L=4 | L=8 | L=16 | L=32 | L=1 | L=2 | L=4 | L=8 | L=16 |
| 2 | 4 | 2 | 1 | 0 | 0 | 4 | 2 | 1 | 0 | 0 |
| 4 | 8 | 4 | 2 | 1 | 0 | 8 | 4 | 2 | 1 | 0 |
| 8 | 6 | 4 | 3 | 2 | 1 | 6 | 4 | 3 | 2 | 1 |

Table 9.1.4-1b: EPDCCH candidates monitored by a UE 
(One Distributed EPDCCH-PRB-set – Case 3)

|  | Number of EPDCCH candidates   for Case 3 |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | L=1 | L=2 | L=4 | L=8 | L=16 |
| 2 | 8 | 4 | 2 | 1 | 0 |
| 4 | 4 | 5 | 4 | 2 | 1 |
| 8 | 4 | 4 | 4 | 2 | 2 |

Table 9.1.4-2a: EPDCCH candidates monitored by a UE 
(One Localized EPDCCH-PRB-set - Case1, Case 2)

|  | Number of EPDCCH candidates   for Case 1 |  |  |  | Number of EPDCCH candidates   for Case 2 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | L=2 | L=4 | L=8 | L=16 | L=1 | L=2 | L=4 | L=8 |
| 2 | 4 | 2 | 1 | 0 | 4 | 2 | 1 | 0 |
| 4 | 8 | 4 | 2 | 1 | 8 | 4 | 2 | 1 |
| 8 | 6 | 6 | 2 | 2 | 6 | 6 | 2 | 2 |

Table 9.1.4-2b: EPDCCH candidates monitored by a UE 
(One Localized EPDCCH-PRB-set – Case 3)

|  | Number of EPDCCH candidates   for Case 3 |  |  |  |
| --- | --- | --- | --- | --- |
|  | L=1 | L=2 | L=4 | L=8 |
| 2 | 8 | 4 | 2 | 1 |
| 4 | 6 | 6 | 2 | 2 |
| 8 | 6 | 6 | 2 | 2 |

.

Table 9.1.4-3a: EPDCCH candidates monitored by a UE 
(Two Distributed EPDCCH-PRB-sets - Case1, Case 2)

|  |  | Number of EPDCCH candidates   for Case 1 |  |  |  |  | Number of EPDCCH candidates   for Case 2 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | L=2 | L=4 | L=8 | L=16 | L=32 | L=1 | L=2 | L=4 | L=8 | L=16 |
| 2 | 2 | 4,4 | 2,2 | 1,1 | 0,0 | 0,0 | 4,4 | 2,2 | 1,1 | 0,0 | 0,0 |
| 4 | 4 | 3,3 | 3,3 | 1,1 | 1,1 | 0,0 | 3,3 | 3,3 | 1,1 | 1,1 | 0,0 |
| 8 | 8 | 3,3 | 2,2 | 1,1 | 1,1 | 1,1 | 3,3 | 2,2 | 1,1 | 1,1 | 1,1 |
| 4 | 2 | 5,3 | 3,2 | 1,1 | 1,0 | 0,0 | 5,3 | 3,2 | 1,1 | 1,0 | 0,0 |
| 8 | 2 | 4,2 | 4,2 | 1,1 | 1,0 | 1,0 | 4,2 | 4,2 | 1,1 | 1,0 | 1,0 |
| 8 | 4 | 3,3 | 2,2 | 2,1 | 1,1 | 1,0 | 3,3 | 2,2 | 2,1 | 1,1 | 1,0 |

Table 9.1.4-3b: EPDCCH candidates monitored by a UE 
(Two Distributed EPDCCH-PRB-sets – Case 3)

|  |  | Number of EPDCCH candidates   for Case 3 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | L=1 | L=2 | L=4 | L=8 | L=16 |
| 2 | 2 | 2,2 | 3,3 | 2,2 | 1,1 | 0,0 |
| 4 | 4 | 2,2 | 2,2 | 2,2 | 1,1 | 1,1 |
| 8 | 8 | 2,2 | 2,2 | 2,2 | 1,1 | 1,1 |
| 4 | 2 | 3,1 | 3,2 | 3,1 | 1,1 | 1,0 |
| 8 | 2 | 3,1 | 4,1 | 3,1 | 1,1 | 1,0 |
| 8 | 4 | 2,2 | 2,2 | 2,2 | 1,1 | 1,1 |

Table 9.1.4-4a: EPDCCH candidates monitored by a UE 
(Two Localized EPDCCH-PRB-sets - Case1, Case 2)

|  |  | Number of EPDCCH candidates  for Case 1 |  |  |  | Number of EPDCCH candidates   for Case 2 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | L=2 | L=4 | L=8 | L=16 | L=1 | L=2 | L=4 | L=8 |
| 2 | 2 | 4,4 | 2,2 | 1,1 | 0,0 | 4,4 | 2,2 | 1,1 | 0,0 |
| 4 | 4 | 3,3 | 3,3 | 1,1 | 1,1 | 3,3 | 3,3 | 1,1 | 1,1 |
| 8 | 8 | 3,3 | 3,3 | 1,1 | 1,1 | 3,3 | 3,3 | 1,1 | 1,1 |
| 4 | 2 | 4,3 | 4,2 | 1,1 | 1,0 | 4,3 | 4,2 | 1,1 | 1,0 |
| 8 | 2 | 5,2 | 4,2 | 1,1 | 1,0 | 5,2 | 4,2 | 1,1 | 1,0 |
| 8 | 4 | 3,3 | 3,3 | 1,1 | 1,1 | 3,3 | 3,3 | 1,1 | 1,1 |

Table 9.1.4-4b: EPDCCH candidates monitored by a UE 
(Two Localized EPDCCH-PRB-sets – Case 3)

|  |  | Number of EPDCCH candidates   for Case 3 |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | L=1 | L=2 | L=4 | L=8 |
| 2 | 2 | 3,3 | 3,3 | 1,1 | 1,1 |
| 4 | 4 | 3,3 | 3,3 | 1,1 | 1,1 |
| 8 | 8 | 3,3 | 3,3 | 1,1 | 1,1 |
| 4 | 2 | 4,2 | 4,2 | 1,1 | 1,1 |
| 8 | 2 | 4,2 | 4,2 | 1,1 | 1,1 |
| 8 | 4 | 3,3 | 3,3 | 1,1 | 1,1 |

Table 9.1.4-5a: EPDCCH candidates monitored by a UE (NOTE)

|  |  | Number of EPDCCH candidates   for Case 1 |  |  |  |  | Number of EPDCCH candidates   for Case 2 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | L=2 | L=4 | L=8 | L=16 | L=32 | L=1 | L=2 | L=4 | L=8 | L=16 |
| 2 | 2 | 4,4 | 2,2 | 1,1 | 0,0 | 0,0 | 4,4 | 2,2 | 1,1 | 0,0 | 0,0 |
| 4 | 4 | 4,2 | 4,3 | 0,2 | 0,1 | 0,0 | 4,2 | 4,3 | 0,2 | 0,1 | 0,0 |
| 8 | 8 | 4,1 | 4,2 | 0,2 | 0,2 | 0,1 | 4,1 | 4,2 | 0,2 | 0,2 | 0,1 |
| 2 | 4 | 4,3 | 2,4 | 0,2 | 0,1 | 0,0 | 4,3 | 2,4 | 0,2 | 0,1 | 0,0 |
| 2 | 8 | 4,1 | 2,2 | 0,4 | 0,2 | 0,1 | 4,1 | 2,2 | 0,4 | 0,2 | 0,1 |
| 4 | 2 | 5,2 | 4,2 | 1,1 | 1,0 | 0,0 | 5,2 | 4,2 | 1,1 | 1,0 | 0,0 |
| 4 | 8 | 4,1 | 4,2 | 0,2 | 0,2 | 0,1 | 4,1 | 4,2 | 0,2 | 0,2 | 0,1 |
| 8 | 2 | 5,1 | 4,2 | 2,1 | 1,0 | 0,0 | 5,1 | 4,2 | 2,1 | 1,0 | 0,0 |
| 8 | 4 | 6,1 | 4,2 | 0,2 | 0,1 | 0,0 | 6,1 | 4,2 | 0,2 | 0,1 | 0,0 |
| NOTE: One localized EPDCCH-PRB-set and one distributed EPDCCH-PRB-set, - Case1, Case 2;   is the identity of the localized EPDCCH-PRB-set,   is the identity of the distributed EPDCCH-PRB-set |  |  |  |  |  |  |  |  |  |  |  |

Table 9.1.4-5b: EPDCCH candidates monitored by a UE (NOTE)

|  |  | Number of EPDCCH candidates   for Case 3 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | L=1 | L=2 | L=4 | L=8 | L=16 |
| 2 | 2 | 4,1 | 4,2 | 2,2 | 0,1 | 0,0 |
| 4 | 4 | 4,1 | 4,1 | 2,2 | 0,1 | 0,1 |
| 8 | 8 | 4,1 | 4,1 | 2,2 | 0,1 | 0,1 |
| 2 | 4 | 4,1 | 4,1 | 2,2 | 0,1 | 0,1 |
| 2 | 8 | 4,1 | 4,1 | 2,2 | 0,1 | 0,1 |
| 4 | 2 | 4,1 | 4,1 | 2,2 | 1,1 | 0,0 |
| 4 | 8 | 4,1 | 4,1 | 2,2 | 0,1 | 0,1 |
| 8 | 2 | 4,1 | 4,1 | 4,1 | 0,1 | 0,0 |
| 8 | 4 | 4,1 | 4,1 | 2,2 | 0,1 | 0,1 |
| NOTE: One localized EPDCCH-PRB-set and one distributed EPDCCH-PRB-set - Case 3);  is the identity of the localized EPDCCH-PRB-set,   is the identity of the distributed EPDCCH-PRB-set) |  |  |  |  |  |  |

If the UE is not configured with a carrier indicator field, then the UE shall monitor one EPDCCH UE-specific search space at each of the aggregation levels given by Tables 9.1.4-1a to 9.1.4-5b on each activated serving cell for which it is configured to monitor EPDCCH.

If a UE is configured for EPDCCH monitoring, and if the UE is configured with a carrier indicator field, then the UE shall monitor one or more EPDCCH UE-specific search spaces at each of the aggregation levels given by Tables 9.1.4-1a to 9.1.4-5b on one or more activated serving cells as configured by higher layer signalling.

A UE configured with the carrier indicator field associated with monitoring EPDCCH on serving cell c shall monitor EPDCCH configured with carrier indicator field and with CRC scrambled by C-RNTI in the EPDCCH UE specific search space of serving cell c.

A UE configured with the carrier indicator field associated with monitoring EPDCCH on the primary cell shall monitor EPDCCH configured with carrier indicator field and with CRC scrambled by SPS C-RNTI or UL-SPS-V-RNTI in the EPDCCH UE specific search space of the primary cell.

A UE is not expected to be configured to monitor EPDCCH with carrier indicator field in an LAA Scell

A UE is not expected to be scheduled with PDSCH starting in the second slot in a subframe in an LAA Scell if the UE is configured to monitor EPDCCH with carrier indicator field corresponding to that LAA Scell in another serving cell

For the serving cell on which EPDCCH is monitored, if the UE is not configured with a carrier indicator field, it shall monitor the EPDCCH UE specific search space for EPDCCH without carrier indicator field, if the UE is configured with a carrier indicator field it shall monitor the EPDCCH UE specific search space for EPDCCH with carrier indicator field.

A UE is not expected to monitor the EPDCCH of a secondary cell if it is configured to monitor EPDCCH with carrier indicator field corresponding to that secondary cell in another serving cell. For the serving cell on which EPDCCH is monitored, the UE shall monitor EPDCCH candidates at least for the same serving cell.

A UE configured to monitor EPDCCH candidates in a given serving cell with a given DCI format size with CIF, and CRC scrambled by C- RNTI, where the EPDCCH candidates may have one or more possible values of CIF for the given DCI format size, shall assume that an EPDCCH candidate with the given DCI format size may be transmitted in the given serving cell in any EPDCCH UE specific search space corresponding to any of the possible values of CIF for the given DCI format size.

For the serving cell on which EPDCCH is monitored, a UE is not required to monitor the EPDCCH in a subframe which is configured by higher layers to be part of a positioning reference signal occasion if the positioning reference signal occasion is only configured within MBSFN subframes and the cyclic prefix length used in subframe #0 is normal cyclic prefix.

A UE may assume the same  value (described in Clause 6.10.3A.1 of [3]) is used for antenna ports 107,108 while monitoring an EPDCCH candidate associated with either antenna port 107 or antenna port 108. 
A UE may assume the same  value (described in Clause 6.10.3A.1 of [3]) is used for antenna ports 109,110 while monitoring an EPDCCH candidate associated with either antenna port 109 or antenna port 110.

#### 9.1.4.1 EPDCCH starting position

For a given serving cell, if the UE is configured via higher layer signalling to receive PDSCH data transmissions according to transmission modes 1-9,

if the UE is configured with a higher layer parameter epdcch-StartSymbol-r11,

the starting OFDM symbol for EPDCCH given by index  is determined from the higher layer parameter,

otherwise

the starting OFDM symbol for EPDCCH given by index  is given by the CFI value in the subframe of the given serving cell when , and  is given by the CFI value+1 in the subframe of the given serving cell when

For a given serving cell, if the UE is configured via higher layer signalling to receive PDSCH data transmissions according to transmission mode 10, for each EPDCCH-PRB-set, the starting OFDM symbol for monitoring EPDCCH in subframe  is determined from the higher layer parameter pdsch-Start-r11 (defined in Clause 9.1.4.3) as follows

if the value of the parameter pdsch-Start-r11 belongs to {1,2,3,4},

is given by the higher layer parameter pdsch-Start-r11

otherwise

is given by the CFI value in subframe  of the given serving cell when , and  is given by the CFI value+1 in subframe of the given serving cell when

if subframe  is indicated by the higher layer parameter mbsfn-SubframeConfigList-r11 (defined in Clause 9.1.4.3), or if subframe  is subframe 1 or 6 for frame structure type 2,

,

otherwise

.

If a serving cell is a LAA Scell, and if the higher layer parameter subframeStartPosition for the Scell indicates 's07'

for monitoring EPDCCH candidates starting in the first slot of the subframe, the starting OFDM symbol for EPDCCH is given by index  in the first slot in a subframe;

for monitoring EPDCCH candidates starting in the second slot of the subframe, the starting OFDM symbol for EPDCCH is given by index  in the second slot in a subframe;

otherwise

the starting OFDM symbol for EPDCCH is given by index  in the first slot in a subframe.

#### 9.1.4.2 Antenna ports quasi co-location for EPDCCH

For a given serving cell, if the UE is configured via higher layer signalling to receive PDSCH data transmissions according to transmission modes 1-9, and if the UE is configured to monitor EPDCCH,

- the UE may assume the antenna ports 0 – 3, 107 – 110 of the serving cell are quasi co-located (as defined in [3]) with respect to Doppler shift, Doppler spread, average delay, and delay spread.

For a given serving cell, if the UE is configured via higher layer signalling to receive PDSCH data transmissions according to transmission mode 10, and if the UE is configured to monitor EPDCCH, for each EPDCCH-PRB-set,

- if the UE is configured by higher layers to decode PDSCH according to quasi co-location Type-A as described in Clause 7.1.10

- the UE may assume the antenna ports 0 – 3, 107 – 110 of the serving cell are quasi co-located (as defined in [3]) with respect to Doppler shift, Doppler spread, average delay, and delay spread.

- if the UE is configured by higher layers to decode PDSCH according to quasi co-location Type-B or type C as described in Clause 7.1.10

- the UE may assume antenna ports 15 – 22 corresponding to the higher layer parameter qcl-CSI-RS-ConfigNZPId-r11 (defined in Clause 9.1.4.3) and antenna ports 107-110 are quasi co-located (as defined in [3]) with respect to Doppler shift, Doppler spread, average delay, and delay spread.

#### 9.1.4.3 Resource mapping parameters for EPDCCH

For a given serving cell, if the UE is configured via higher layer signalling to receive PDSCH data transmissions according to transmission mode 10, and if the UE is configured to monitor EPDCCH, for each EPDCCH-PRB-set, the UE shall use the parameter set indicated by the higher layer parameter re-MappingQCL-ConfigId-r11 for determining the EPDCCH RE mapping (defined in Clause 6.8A.5 of [3]) and EPDCCH antenna port quasi co-location. The following parameters for determining EPDCCH RE mapping (as described in Clause 6.8A.5 of [3]) and EPDCCH antenna port quasi co-location are included in the parameter set:

- crs-PortsCount-r11.

- crs-FreqShift-r11.

- mbsfn-SubframeConfigList-r11.

- csi-RS-ConfigZPId-r11.

- pdsch-Start-r11.

- qcl-CSI-RS-ConfigNZPId-r11.

- csi-RS-ConfigZPId2-r12 if the UE is configured with CSI subframe sets  and  by the higher layer parameter csi-SubframePatternConfig-r12 for the serving cell or the UE is configured with higher layer parameter eMIMO-Type for TDD serving cell.

#### 9.1.4.4 PRB-pair indication for EPDCCH

For BL/CE UEs and USS, following is applied in the rest of this Clause.

- ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}] is used in place of ![](media_svg/image507.svg) [公式≈: ^{N}RB^{X}^{p}].

- If ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=2+4, PRB-pairs of the 2 PRB set is obtained using resourceBlockAssignment-r11 and the procedure described in the rest of this Clause. PRB-pairs of the 4 PRB set is the remaining 4 PRB-pairs in PRB-pairs in MPDCCH-PRB-set . If ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=2, PRB-pairs of the 2 PRB set is obtained using resourceBlockAssignment-r11 and the procedure described in the rest of this Clause. If ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=4, PRB-pairs of the 4 PRB set is obtained using resourceBlockAssignment-r11 and the procedure described in the rest of this Clause.

- ![](media_svg/image508.svg) [公式≈: _{N}_{RB}DL] is set to 6.

For a given serving cell, for each EPDCCH-PRB-pair set/MPDCCH-PRB-pair set , the UE is configured with a higher layer parameter resourceBlockAssignment-r11 indicating a combinatorial index  corresponding to the PRB index , () and given by equation , where  is the number of PRB pairs associated with the downlink bandwidth,  is the number of PRB-pairs constituting EPDCCH-PRB-set/MPDCCH-PRB-pair set , and is configured by the higher layer parameter numberPRBPairs-r11, and  is the extended binomial coefficient, resulting in unique label .

### 9.1.5 MPDCCH assignment procedure

A BL/CE UE shall monitor a set of MPDCCH candidates on one or more Narrowbands (described in Clause 6.2.7 of [3]) as configured by higher layer signalling for control information, where monitoring implies attempting to decode each of the MPDCCHs in the set according to all the monitored DCI formats. The Narrowband in a subframe used for MPDCCH monitoring is determined as described in [3].

A UE that is not a BL/CE UE is not required to monitor MPDCCH.

A BL/CE UE can derive the configuration of one or two MPDCCH-PRB-sets for MPDCCH monitoring from higher layer signalling. The PRB-pairs corresponding to MPDCCH-PRB-set ![](media_svg/image516.svg) [公式: p=0] are indicated by higher layers. Each MPDCCH-PRB-set consists of set of ECCEs numbered from 0 to ![](media_svg/image517.svg) [公式≈: N&apos;_{ECCE}_{,}_{p}_{,}_{k}−1]where ![](media_svg/image518.svg) [公式≈: ^{N}^{&apos;}ECCE,p,k]is the number of ECCEs in MPDCCH-PRB-set  of subframe .

The MPDCCH-PRB-set(s) can be configured by higher layers for either localized MPDCCH transmission or distributed MPDCCH transmission.

The set of MPDCCH candidates to monitor are defined in terms of MPDCCH search spaces.

The BL/CE UE shall monitor one or more of the following search spaces

- a Type0-MPDCCH common search space if configured with CEmodeA, or if configured with CEmodeB and higher layer parameter ce-ETWS-CMAS-RxInConn,

- a Type1-MPDCCH common search space,

- a Type1A-MPDCCH common search space,

- a Type2-MPDCCH common search space,

- a Type2A-MPDCCH common search space, and

- a MPDCCH UE-specific search space.

A BL/CE UE configured with CEModeB is not required to monitor Type0-MPDCCH common search space unless the UE is configured with higher layer parameter ce-ETWS-CMAS-RxInConn.

The BL/CE UE is not required to simultaneously monitor MPDCCH UE-specific search space and Type1-MPDCCH common search space.

The BL/CE UE is not required to simultaneously monitor MPDCCH UE-specific search space and Type2-MPDCCH common search space.

The BL/CE UE is not required to monitor Type1A-MPDCCH common search space or Type2A-MPDCCH common search space if the set of subframes comprising the search space include any subframes in which it monitors Type1-MPDCCH common search space or any subframes in which the UE receives PDSCH assigned by PDCCH with DCI CRC scrambled by P-RNTI.

The BL/CE UE is not required to monitor Type2A-MPDCCH common search space if the set of subframes comprising the search space include any subframes in which it monitors Type1A-MPDCCH common search space or any subframes in which the UE receives PDSCH assigned by MPDCCH with DCI CRC scrambled by SC-RNTI.

A BL/CE UE is not required to monitor Type1-MPDCCH common search space or in case of half-duplex FDD operation MWUS if the set of subframes comprising the search space or the set of subframes where MWUS may be received include any subframes in which the UE has initiated a PUSCH transmission using preconfigured uplink resource on a given serving cell.

A BL/CE UE is not required to monitor Type1-MPDCCH common search space or MWUS in subframes in which the UE monitors a UE-specific MPDCCH search space given by PUR-RNTI.

A BL/CE UE is not expected to monitor an MPDCCH candidate, if an ECCE corresponding to that MPDCCH candidate is mapped to a PRB pair that overlaps with a transmission of PDSCH scheduled previously in the same subframe.

For aggregation level ![](media_svg/image519.svg) [公式: L&apos;24=] or ![](media_svg/image520.svg) [公式: L&apos;12=] ECCEs, the number of ECCEs refers to the MPDCCH mapping to the REs of the 2+4 PRB set as defined in [3]. An MPDCCH search space ![](media_svg/image521.svg) [公式≈: _{MS}_{k}(&apos;,)LR]at aggregation level ![](media_svg/image522.svg) [公式: L&apos;1,2,4,8,16,12,24⎰{}] and repetition level ![](media_svg/image523.svg) [公式: R⎰{1,2,4,8,16,32,64,128,256}]is defined by a set of MPDCCH candidates where each candidate is repeated in a set of ![](media_svg/image524.svg) [公式: R] consecutive BL/CE downlink subframes starting with subframe ![](media_svg/image525.svg) [公式: k]. For an MPDCCH-PRB-set , the ECCEs corresponding to MPDCCH candidate m of the search space ![](media_svg/image526.svg) [公式≈: _{MS}_{k}(L&apos;,R)] are given by

![](media_svg/image527.svg) [公式≈: L&apos;^{√}^{⌡}⌠_{⌡}_{∞}(Yp,k+^{⋅}⋅_{⋅}_{√}^{m}^{∪}_{L}^{N}_{&apos;}_{∪}_{M}^{&apos;}^{ECCE}_{&apos;}(_{p}L&apos;)^{,}^{p}^{,}^{k}^{∂}∂_{∂}_{∃})mod√N&apos;ECCE,p,k/L&apos;∃^{∅}^{⌡}∇_{⌡}_{∈}+i]

where

![](media_svg/image528.svg) [公式: i=0,κ,L&apos;−1]

![](media_svg/image529.svg) [公式≈: m=0,1,κM&apos;^{(}_{p}^{L}^{&apos;}^{)}−1],

![](media_svg/image530.svg) [公式≈: _{M}_{&apos;}(_{p}L&apos;)]is the number of MPDCCH candidates to monitor at aggregation level![](media_svg/image531.svg) [公式: L&apos;] in MPDCCH-PRB-set  in each subframe in the set of ![](media_svg/image524.svg) [公式: R] consecutive subframes.

![](media_svg/image532.svg) [公式≈: ^{Y}p,k]for MPDCCH UE-specific search space is determined as described in Clause 9.1.4, and ![](media_svg/image533.svg) [公式: Y_{p}_{,}_{k}=0] for Type0-MPDCCH common search space, Type1-MPDCCH common search space, Type1A-MPDCCH common search space, Type2-MPDCCH common search space and Type2A-MPDCCH common search space.

For ![](media_svg/image534.svg) [公式: R>1], if subframe ![](media_svg/image525.svg) [公式: k]is a special subframe that does not support MPDCCH according to table 6.8B.1-1 in [3], the UE shall calculate ![](media_svg/image535.svg) [公式≈: ^{N}^{&apos;}ECCE,p,k] by assuming ![](media_svg/image536.svg) [公式≈: _{N}_{EREG}ECCE_{=}_{4}]for normal cyclic prefix and ![](media_svg/image537.svg) [公式≈: _{N}_{EREG}ECCE_{=}_{8}]for extended cyclic prefix.

A BL/CE UE is not expected to monitor MPDCCH in subframes that are not BL/CE DL subframes as defined in clause 7.1.

Until BL/CE UE receives higher layer configuration of MPDCCH UE-specific search space, the BL/CE UE monitors MPDCCH according to the same configuration of MPDCCH search space and Narrowband as that for MPDCCH scheduling Msg4.

The aggregation and repetition levels defining the MPDCCH search spaces and the number of monitored MPDCCH candidates are given as follows:

For MPDCCH UE-specific search space

- if the BL/CE UE is configured with ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=2 or ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=4 PRB-pairs, and mPDCCH-NumRepetition=1, and

- if the MPDCCH-PRB-set is configured for distributed transmission, the aggregation levels defining the search spaces and the number of monitored MPDCCH candidates are listed in Table 9.1.4-1a and Table 9.1.4-1b, where ![](media_svg/image538.svg) [公式: L] is substituted with ![](media_svg/image531.svg) [公式: L&apos;] for ![](media_svg/image538.svg) [公式: L]≤24, and ![](media_svg/image539.svg) [公式≈: ^{N}RB^{X}^{p}] is substituted with ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}].

- if the MPDCCH-PRB-set is configured for localized transmission, the aggregation levels defining the search spaces and the number of monitored MPDCCH candidates are listed in Table 9.1.4-2a and Table 9.1.4-2b, where ![](media_svg/image538.svg) [公式: L] is substituted with ![](media_svg/image531.svg) [公式: L&apos;] and ![](media_svg/image539.svg) [公式≈: ^{N}RB^{X}^{p}] is substituted with ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}].

- otherwise

- if the UE is configured with CEModeA, and ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=2 or ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=4, the aggregation and repetition levels defining the search spaces and the number of monitored MPDCCH candidates are listed in Table 9.1.5-1a

- if the UE is configured with CEModeA, and ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=2+4 , the aggregation and repetition levels defining the search spaces and the number of monitored MPDCCH candidates are listed in Table 9.1.5-1b

- if the UE is configured with CEModeB, and ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=2 or ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=4, the aggregation and repetition levels defining the search spaces and the number of monitored MPDCCH candidates are listed in Table 9.1.5-2a

- if the UE is configured with CEModeB, and ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=2+4 , the aggregation and repetition levels defining the search spaces and the number of monitored MPDCCH candidates are listed in Table 9.1.5-2b

![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]is the number of PRB-pairs configured for MPDCCH UE-specific search space. When ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=2+4, it is given by the higher layer parameter numberPRB-Pairs-r13, and when ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=2 or ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=4, it is given by the higher layer parameter numberPRB-Pairs-r11, except for MPDCCH candidates associated with PUR-RNTI in which case it is given by the higher layer parameter mpdcch-PRB-Pairs-r16 in PUR-Config.

![](media_svg/image540.svg) [公式: r1], ![](media_svg/image541.svg) [公式: r2], ![](media_svg/image542.svg) [公式: r3], ![](media_svg/image543.svg) [公式: r4] are determined from Table 9.1.5-3 by substituting the value of ![](media_svg/image544.svg) [公式≈: ^{r}max] with the value of higher layer parameter mPDCCH-NumRepetition, except for MPDCCH candidates associated with PUR-RNTI in which case it is given by the value of the higher layer parameter mpdcch-NumRepetition-r16 in PUR-Config.

The PRB-pairs within a Narrowband corresponding to an MPDCCH-PRB-set are indicated by higher layers and are determined using the description given in Clause 9.1.4.4.

If higher layer configuration numberPRB-Pairs-r13 or numberPRB-Pairs in PUR-MPDCCH-Config for MPDCCH-PRB-set is 6, ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=2+4, and the number of PRB-pairs in an MPDCCH-PRB-set = 2+4.

If Type2-MPDCCH common search space or Type2A-MPDCCH common search space,

- PRB-pairs of the 2 PRB set in the 2+4 PRB set correspond to PRB-pairs with the largest two PRB indices in MPDCCH-PRB-set .

- PRB-pairs of the4 PRB set in the 2+4 PRB set correspond to PRB-pairs with the smallest 4 PRB indices in MPDCCH-PRB-set .

- PRB-pairs of the 2+4 PRB set in the 2+4 PRB set correspond to all PRB-pairs in MPDCCH-PRB-set

Table 9.1.5-1a: MPDCCH candidates monitored by a BL/CE UE 
(CEModeA, MPDCCH-PRB-set size – 2PRBs or 4PRBs)

| ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}] | R | ![](media_svg/image530.svg) [公式≈: _{M}_{&apos;}(_{p}L&apos;)] |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | L'=2 | L'=4 | L'=8 | L'=16 | L'=24 |
| 2 | r1 | 2 | 1 | 1 | 0 | 0 |
| 4 |  | 1 | 1 | 1 | 1 | 0 |
| 2 | r2 | 2 | 1 | 1 | 0 | 0 |
| 4 |  | 1 | 1 | 1 | 1 | 0 |
| 2 | r3 | 2 | 1 | 1 | 0 | 0 |
| 4 |  | 1 | 1 | 1 | 1 | 0 |
| 2 | r4 | 2 | 1 | 1 | 0 | 0 |
| 4 |  | 1 | 1 | 1 | 1 | 0 |

Table 9.1.5-1b: MPDCCH candidates monitored by a BL/CE UE 
(CEModeA, MPDCCH-PRB-set size – 2+4PRBs)

| MPDCCH PRB set | R | ![](media_svg/image530.svg) [公式≈: _{M}_{&apos;}(_{p}L&apos;)] |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | L'=2 | L'=4 | L'=8 | L'=16 | L'=24 |
| 2 PRB set in 2+4 PRB set | r1 | 1 | 1 | 0 | 0 | 0 |
| 4 PRB set in 2+4 PRB set |  | 0 | 0 | 2 | 1 | 0 |
| Both PRB sets in 2+4 PRB set |  | 0 | 0 | 0 | 0 | 1 |
| 2 PRB set in 2+4 PRB set | r2 | 0 | 1 | 1 | 0 | 0 |
| 4 PRB set in 2+4 PRB set |  | 0 | 0 | 2 | 1 | 0 |
| Both PRB sets in 2+4 PRB set |  | 0 | 0 | 0 | 0 | 1 |
| 2 PRB set in 2+4 PRB set | r3 | 0 | 0 | 0 | 0 | 0 |
| 4 PRB set in 2+4 PRB set |  | 0 | 0 | 1 | 1 | 0 |
| Both PRB sets in 2+4 PRB set |  | 0 | 0 | 0 | 0 | 1 |
| 2 PRB set in 2+4 PRB set | r4 | 0 | 0 | 0 | 0 | 0 |
| 4 PRB set in 2+4 PRB set |  | 0 | 0 | 0 | 0 | 0 |
| Both PRB sets in 2+4 PRB set |  | 0 | 0 | 0 | 0 | 1 |

Table 9.1.5-2a: MPDCCH candidates monitored by a BL/CE UE 
(CEModeB, MPDCCH-PRB-set size – 2PRBs or 4PRBs)

| ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}] | R | ![](media_svg/image530.svg) [公式≈: _{M}_{&apos;}(_{p}L&apos;)] |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | L'=2 | L'=4 | L'=8 | L'=16 | L'=24 |
| 2 | r1 | 0 | 0 | 1 | 0 | 0 |
| 4 |  | 0 | 0 | 1 | 1 | 0 |
| 2 | r2 | 0 | 0 | 1 | 0 | 0 |
| 4 |  | 0 | 0 | 1 | 1 | 0 |
| 2 | r3 | 0 | 0 | 1 | 0 | 0 |
| 4 |  | 0 | 0 | 1 | 1 | 0 |
| 2 | r4 | 0 | 0 | 1 | 0 | 0 |
| 4 |  | 0 | 0 | 1 | 1 | 0 |

Table 9.1.5-2b: MPDCCH candidates monitored by a BL/CE UE 
(CEModeB, MPDCCH-PRB-set size – 2+4PRBs)

| MPDCCH PRB set | R | ![](media_svg/image530.svg) [公式≈: _{M}_{&apos;}(_{p}L&apos;)] |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | L'=2 | L'=4 | L'=8 | L'=16 | L'=24 |
| 2 PRB set in 2+4 PRB set | r1 | 0 | 0 | 1 | 0 | 0 |
| 4 PRB set in 2+4 PRB set |  | 0 | 0 | 0 | 1 | 0 |
| Both PRB sets in 2+4 PRB set |  | 0 | 0 | 0 | 0 | 1 |
| 2 PRB set in 2+4 PRB set | r2 | 0 | 0 | 1 | 0 | 0 |
| 4 PRB set in 2+4 PRB set |  | 0 | 0 | 0 | 1 | 0 |
| Both PRB sets in 2+4 PRB set |  | 0 | 0 | 0 | 0 | 1 |
| 2 PRB set in 2+4 PRB set | r3 | 0 | 0 | 1 | 0 | 0 |
| 4 PRB set in 2+4 PRB set |  | 0 | 0 | 0 | 1 | 0 |
| Both PRB sets in 2+4 PRB set |  | 0 | 0 | 0 | 0 | 1 |
| 2 PRB set in 2+4 PRB set | r4 | 0 | 0 | 1 | 0 | 0 |
| 4 PRB set in 2+4 PRB set |  | 0 | 0 | 0 | 1 | 0 |
| Both PRB sets in 2+4 PRB set |  | 0 | 0 | 0 | 0 | 1 |

Table 9.1.5-3: Determination of repetition levels

| ![](media_svg/image545.svg) [公式≈: ^{r}max] | ![](media_svg/image540.svg) [公式: r1] | ![](media_svg/image541.svg) [公式: r2] | ![](media_svg/image542.svg) [公式: r3] | ![](media_svg/image543.svg) [公式: r4] |
| --- | --- | --- | --- | --- |
| 1 | 1 | - | - | - |
| 2 | 1 | 2 | - | - |
| 4 | 1 | 2 | 4 | - |
| >=8 | ![](media_svg/image546.svg) [公式: r_{max}/8] | ![](media_svg/image547.svg) [公式: r_{max}/4] | ![](media_svg/image548.svg) [公式: r_{max}/2] | ![](media_svg/image545.svg) [公式≈: ^{r}max] |

Table 9.1.5-4: Repetition levels for Type1/1A-MPDCCH common search space

| ![](media_svg/image545.svg) [公式≈: ^{r}max] | ![](media_svg/image540.svg) [公式: r1] | ![](media_svg/image541.svg) [公式: r2] | ![](media_svg/image542.svg) [公式: r3] | ![](media_svg/image543.svg) [公式: r4] |
| --- | --- | --- | --- | --- |
| 256 | 2 | 16 | 64 | 256 |
| 128 | 2 | 16 | 64 | 128 |
| 64 | 2 | 8 | 32 | 64 |
| 32 | 1 | 4 | 16 | 32 |
| 16 | 1 | 4 | 8 | 16 |
| 8 | 1 | 2 | 4 | 8 |
| 4 | 1 | 2 | 4 | - |
| 2 | 1 | 2 | - | - |
| 1 | 1 | - | - | - |

For Type0-MPDCCH common search space, the narrowband location and the MPDCCH-PRB-set  are the same as for MPDCCH UE-specific search space, and

- if ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=2,

- ![](media_svg/image530.svg) [公式≈: _{M}_{&apos;}(_{p}L&apos;)]=1 for ![](media_svg/image531.svg) [公式: L&apos;]=8 and repetition levels ![](media_svg/image540.svg) [公式: r1],![](media_svg/image541.svg) [公式: r2], ![](media_svg/image542.svg) [公式: r3], ![](media_svg/image543.svg) [公式: r4] given in Table 9.1.5.-3. For all other cases, ![](media_svg/image530.svg) [公式≈: _{M}_{&apos;}(_{p}L&apos;)]=0

- if ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=4,

- ![](media_svg/image530.svg) [公式≈: _{M}_{&apos;}(_{p}L&apos;)]=1 for ![](media_svg/image531.svg) [公式: L&apos;]=16 and repetition levels ![](media_svg/image540.svg) [公式: r1],![](media_svg/image541.svg) [公式: r2], ![](media_svg/image542.svg) [公式: r3], ![](media_svg/image543.svg) [公式: r4] given in Table 9.1.5.-3. For all other cases, ![](media_svg/image530.svg) [公式≈: _{M}_{&apos;}(_{p}L&apos;)]=0

- if ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=2+4,

- ![](media_svg/image530.svg) [公式≈: _{M}_{&apos;}(_{p}L&apos;)]=1 for ![](media_svg/image531.svg) [公式: L&apos;]=24 and repetition levels ![](media_svg/image540.svg) [公式: r1],![](media_svg/image541.svg) [公式: r2], ![](media_svg/image542.svg) [公式: r3], ![](media_svg/image543.svg) [公式: r4] given in Table 9.1.5.-3. For all other cases, ![](media_svg/image530.svg) [公式≈: _{M}_{&apos;}(_{p}L&apos;)]=0

where ![](media_svg/image540.svg) [公式: r1], ![](media_svg/image541.svg) [公式: r2], ![](media_svg/image542.svg) [公式: r3], ![](media_svg/image543.svg) [公式: r4] are determined from Table 9.1.5-3 by substituting the value of ![](media_svg/image544.svg) [公式≈: ^{r}max] with the value of higher layer parameter mPDCCH-NumRepetition.

For Type1-MPDCCH common search space and Type1A-MPDCCH common search space, the number of PRB-pairs in MPDCCH-PRB-set is 2+4 PRB-pairs, and

- ![](media_svg/image530.svg) [公式≈: _{M}_{&apos;}(_{p}L&apos;)]=1 for ![](media_svg/image531.svg) [公式: L&apos;]=24 and repetition levels ![](media_svg/image540.svg) [公式: r1],![](media_svg/image541.svg) [公式: r2], ![](media_svg/image542.svg) [公式: r3], ![](media_svg/image543.svg) [公式: r4] where the repetition levels are determined from Table 9.1.5-4 by substituting the value of ![](media_svg/image544.svg) [公式≈: ^{r}max]

- with higher layer parameter mPDCCH-NumRepetition-Paging for Type1-MPDCCH common search space, and

- with higher layer parameter mpdcch-NumRepetitions-SC-MCCH for Type1A-MPDCCH common search space.

- For all other cases, ![](media_svg/image530.svg) [公式≈: _{M}_{&apos;}(_{p}L&apos;)]=0

For Type2-MPDCCH common search space, the number of PRB-pairs in MPDCCH-PRB-set is 2+4 PRB-pairs, and

- If the most recent coverage enhancement level used for PRACH is coverage enhancement level 0 and 1, the aggregation and repetition levels defining the search spaces and the number of monitored MPDCCH candidates are determined from Table 9.1.5-1b, by assuming that the number of candidates for ![](media_svg/image531.svg) [公式: L&apos;]<8 as zero.

- If the most recent coverage enhancement level used for PRACH is coverage enhancement level 2 and 3, the aggregation and repetition levels defining the search spaces and the number of monitored MPDCCH candidates are determined from Table 9.1.5-2b.

where ![](media_svg/image540.svg) [公式: r1], ![](media_svg/image541.svg) [公式: r2], ![](media_svg/image542.svg) [公式: r3], ![](media_svg/image543.svg) [公式: r4]are determined from Table 9.1.5-3 by substituting the value of ![](media_svg/image544.svg) [公式≈: ^{r}max] with the value of higher layer parameter mPDCCH-NumRepetition-RA.

For Type2A-MPDCCH common search space, the number of PRB-pairs in MPDCCH-PRB-set is 2+4 PRB-pairs, and

- for CEModeA, the aggregation and repetition levels defining the search spaces and the number of monitored MPDCCH candidates are determined from Table 9.1.5-1b, by assuming that the number of candidates for ![](media_svg/image531.svg) [公式: L&apos;]<8 as zero,

- for CEModeB, the aggregation and repetition levels defining the search spaces and the number of monitored MPDCCH candidates are determined from Table 9.1.5-2b,

where ![](media_svg/image540.svg) [公式: r1], ![](media_svg/image541.svg) [公式: r2], ![](media_svg/image542.svg) [公式: r3], ![](media_svg/image543.svg) [公式: r4]are determined from Table 9.1.5-3 by substituting the value of ![](media_svg/image544.svg) [公式≈: ^{r}max] with the value of higher layer parameter mpdcch-NumRepetitions-SC-MTCH.

In tables 9.1.5-1a, 9.1.5-1b, 9.1.5-2a, 9.1.5-2b, and for MPDCCH UE-specific search space when BL/CE UE is configured with ![](media_svg/image506.svg) [公式: N&apos;_{RB}^{X}^{p}]=2+4 or mPDCCH-NumRepetition > 1 or mpdcch-NumRepetition > 1 in PUR-MPDCCH-Config, Type0, Type1, Type1A, Type2, Type2A MPDCCH common search space, ![](media_svg/image531.svg) [公式: L&apos;] is applied for ![](media_svg/image549.svg) [公式≈: _{N}_{EREG}ECCE]=4, and ![](media_svg/image550.svg) [公式: L&apos;&apos;] is applied for ![](media_svg/image549.svg) [公式≈: _{N}_{EREG}ECCE]=8 wherein ![](media_svg/image551.svg) [公式: LL&apos;&apos;&apos;/2=] substituting the values of ![](media_svg/image531.svg) [公式: L&apos;].

If a BL/CE UE is configured with higher layer parameter localizedMappingType in CRS-ChEstMPDCCH-ConfigDedicated set to 'CSI-based' or 'Reciprocity-based', and the MPDCCH-PRB-set  is configured for localized transmission, and for MPDCCH UE-specific search space or Type0-MPDCCH common search space, the UE may assume the relation between the DMRS and the CRS ports follows the predefined mapping type (as defined in [3]), for the following MPDCCH candidates

- if ![](media_svg/image552.svg) [公式: N&apos;2_{RB}^{X}^{p}=], MPDCCH candidates with aggregation level ![](media_svg/image553.svg) [公式: L&apos;8=] and repetition levels ![](media_svg/image540.svg) [公式: r1],![](media_svg/image541.svg) [公式: r2], ![](media_svg/image542.svg) [公式: r3], ![](media_svg/image543.svg) [公式: r4]

- if ![](media_svg/image554.svg) [公式: N&apos;4_{RB}^{X}^{p}=], MPDCCH candidates with aggregation level ![](media_svg/image555.svg) [公式: L&apos;16=] and repetition levels ![](media_svg/image540.svg) [公式: r1],![](media_svg/image541.svg) [公式: r2], ![](media_svg/image542.svg) [公式: r3], ![](media_svg/image543.svg) [公式: r4]

- if ![](media_svg/image556.svg) [公式: N&apos;24_{RB}^{X}^{p}=+], MPDCCH candidates with aggregation level ![](media_svg/image557.svg) [公式: L&apos;24=] and repetition levels ![](media_svg/image540.svg) [公式: r1],![](media_svg/image541.svg) [公式: r2], ![](media_svg/image542.svg) [公式: r3], ![](media_svg/image543.svg) [公式: r4]

and for other MPDCCH candidates,

- if higher layer parameter localizedMappingType in CRS-ChEstMPDCCH-ConfigDedicated is set to 'CSI-based' the UE may assume the relation between DMRS and CRS ports, as defined in [3], is based on a most recent reported PMI ending no later than subframe $ k0-4 $.

- if higher layer parameter localizedMappingType in CRS-ChEstMPDCCH-ConfigDedicated is set to 'Reciprocity-based', the UE shall not assume any relation between the DMRS and CRS ports.

If a BL/CE UE is configured with higher layer parameter localizedMappingType in CRS-ChEstMPDCCH-ConfigDedicated set to 'CSI-based' or 'Reciprocity-based', and the MPDCCH-PRB-set  is configured for localized transmission, and ![](media_svg/image552.svg) [公式: N&apos;2_{RB}^{X}^{p}=] or ![](media_svg/image554.svg) [公式: N&apos;4_{RB}^{X}^{p}=], and $ r_{max}>2 $, for MPDCCH UE-specific search space or Type0-MPDCCH common search space, the antenna port for MPDCCH candidates with aggregation level $ L^{'}=2 $ shall be changed as specified in [3].

For Type1-MPDCCH common search space, Type1A-MPDCCH common search space, Type2-MPDCCH common search space and Type2A-MPDCCH common search space, distributed MPDCCH transmission is used.

For MPDCCH UE-specific search space given by PUR-RNTI, distributed MPDCCH transmission is used.

For MPDCCH UE-specific search space, Type0-MPDCCH common search space, Type1A-MPDCCH common search space, Type2-MPDCCH common search space and Type2A-MPDCCH common search space locations of starting subframe ![](media_svg/image525.svg) [公式: k] are given by ![](media_svg/image558.svg) [公式: k=k_{b}]where ![](media_svg/image559.svg) [公式≈: ^{k}b]is the ![](media_svg/image560.svg) [公式: b]th consecutive BL/CE DL subframe from subframe ![](media_svg/image561.svg) [公式: k0], and ![](media_svg/image562.svg) [公式: b=u∪rj], and ![](media_svg/image563.svg) [公式: u=0,1,κ^{r}^{max}_{rj}−1], and ![](media_svg/image564.svg) [公式: j⎰{1,2,3,4}], where

- subframe ![](media_svg/image561.svg) [公式: k0] is a subframe satisfying the condition ![](media_svg/image565.svg) [公式≈: (10n_{f}+_{√}n_{s}2_{∃})modT=_{√}Α_{offset}∪T_{∃}], where ![](media_svg/image566.svg) [公式: T=r_{max}∪G]

- For MPDCCH UE-specific search space and Type0-MPDCCH common search space, ![](media_svg/image567.svg) [公式: G] is given by the higher layer parameter mPDCCH-startSF-UESS, except for MPDCCH candidates associated with PUR-RNTI in which case it is given by the higher layer parameter mpdcch-startSF-UESS-r16 in PUR-Config,

- For Type1A-MPDCCH common search space, ![](media_svg/image567.svg) [公式: G] is given by the higher layer parameter mpdcch-startSF-SC-MCCH

- For Type2-MPDCCH common search space, ![](media_svg/image567.svg) [公式: G] is given by the higher layer parameter mPDCCH-startSF-CSS-RA-r13

- For Type2A-MPDCCH common search space, ![](media_svg/image567.svg) [公式: G] is given by the higher layer parameter mpdcch-startSF-SC-MTCH

- ![](media_svg/image568.svg) [公式≈: ^{Α}offset]is given by the higher layer parameter mpdcch-Offset-SC-MTCH for Type2A-MPDCCH common search space, and by the higher layer parameter mpdcch-Offset-PUR-SS-r16 in PUR-Config for MPDCCH candidates associated with PUR-RNTI, and ![](media_svg/image569.svg) [公式≈: ^{Α}offset^{=}^{0}]otherwise; and

- ![](media_svg/image544.svg) [公式≈: ^{r}max]is given by the higher layer parameter mPDCCH-NumRepetition for MPDCCH UE-specific search space and Type0-MPDCCH common search space, except for MPDCCH candidates associated with PUR-RNTI in which case it is given by the higher layer parameter mpdcch-NumRepetition-r16 in PUR-Config, and mPDCCH-NumRepetition-RA for Type2-MPDCCH common search space, and mpdcch-NumRepetitions-SC-MCCH for Type1A-MPDCCH common search space, and mpdcch-NumRepetitions-SC-MTCH for Type2A-MPDCCH common search space and

- ![](media_svg/image540.svg) [公式: r1], ![](media_svg/image541.svg) [公式: r2], ![](media_svg/image542.svg) [公式: r3], ![](media_svg/image543.svg) [公式: r4]are given in Table 9.1.5-3.

A BL/CE UE is not expected to be configured with values of ![](media_svg/image570.svg) [公式≈: ^{r}max]and ![](media_svg/image571.svg) [公式: G]that result in non-integer values of ![](media_svg/image572.svg) [公式: T].

For Type1-MPDCCH common search space, ![](media_svg/image525.svg) [公式: k]=![](media_svg/image561.svg) [公式: k0] and is determined from locations of paging opportunity subframes,

If SystemInformationBlockType1-BR or SI message is transmitted in one narrowband in subframe ![](media_svg/image573.svg) [公式: k], a BL/CE UE shall assume MPDCCH in the same narrowband in the subframe ![](media_svg/image574.svg) [公式: k] is dropped.

The BL/CE UE is not required to monitor an MPDCCH search space if any ECCEs corresponding to any of its MPDCCH candidates occur within a frame before ![](media_svg/image575.svg) [公式: n_{f}=0]and also occur within frame![](media_svg/image576.svg) [公式: n_{f}÷0].

The BL/CE UE is not required to monitor an MPDCCH search space during the PUSCH transmission gap as defined in clause 5.3.4 of [3].

The BL/CE UE is not expected to be configured with overlapping MPDCCH search spaces of the same type.

A BL/CE UE configured to monitor MPDCCH candidates with CRC scrambled by C-RNTI or SPS C-RNTI with the same payload size and with the same aggregation level in the Type0-MPDCCH common search space and the MPDCCH UE-specific search space shall assume that for the MPDCCH candidates with CRC scrambled by C-RNTI or SPS C-RNTI, only the MPDCCH in the UE specific search space is transmitted.

For MPDCCH UE-specific search space or for Type0-MPDCCH common search space if the higher layer parameter mPDCCH-NumRepetition is set to 1 or the higher layer parameter mpdcch-NumRepetition in PUR-MPDCCH-Config is set to 1; or for Type2-MPDCCH common search space if the higher layer parameter mPDCCH-NumRepetition-RA is set to 1; or for Type2A-MPDCCH common search space if the higher layer parameter mpdcch-NumRepetitions-SC-MTCH is set to 1;

- The BL/CE UE is not required to monitor MPDCCH

- For TDD and normal downlink CP, in special subframes for the special subframe configurations 0 and 5 shown in Table 4.2-1 of [3], or for the special subframe configuration 10 configured by the higher layer signalling ssp10-CRS-LessDwPTS

- For TDD and extended downlink CP, in special subframes for the special subframe configurations 0, 4 and 7 shown in Table 4.2-1 of [3];

otherwise

- The BL/CE UE is not required to monitor MPDCCH

- For TDD, in special subframes, if the BL/CE UE is configured with CEModeB

- For TDD and normal downlink CP, in special subframes for the special subframe configurations 0, 1, 2, 5, 6, 7, 9, and 10 shown in Table 4.2-1 of [3], if the BL/CE UE is configured with CEModeA

- For TDD and extended downlink CP, in special subframes for the special subframe configurations 0, 4 and 7 shown in Table 4.2-1 of [3], if the BL/CE UE is configured with CEModeA.

- For TDD, in special subframes, for MPDCCH in Type1/1A-MPDCCH common search space.

If the UE has initiated a PUSCH transmission using preconfigured uplink resource ending in subframe n, the UE shall monitor the MPDCCH UE-specific search space in a search space window starting in subframe n+4+Kmac with duration given by higher layer parameter pur-ResponseWindowTimer where $ K_{mac}$ is provided by higher layer parameter K-mac, otherwise $ K_{mac}=0 $. Upon detection of a MPDCCH with DCI format 6-0A/6-0B with CRC scrambled by PUR-RNTI intended for the UE within the search space window and the corresponding DCI is for PUR ACK/fallback indication (as defined in [4]), the UE is not required to monitor the MPDCCH UE-specific search space for the remaining search space window duration.

The number of MPDCCH repetitions is indicated in the 'DCI subframe repetition number' field in the DCI according to the mapping in Table 9.1.5-5. For a BL/CE UE in half-duplex FDD operation, if the UE is configured with CEModeA, and configured with higher layer parameter ce-HARQ-AckBundling, and 'HARQ-ACK bundling flag' in the corresponding DCI is set to 1, the UE shall assume the number of MPDCCH repetitions as 1.

Table 9.1.5-5: Mapping for DCI subframe repetition number

| R | DCI subframe repetition number |
| --- | --- |
|  |  |
| ![](media_svg/image540.svg) [公式: r1] | 00 |
| ![](media_svg/image577.svg) [公式: r2] | 01 |
| ![](media_svg/image578.svg) [公式: r3] | 10 |
| ![](media_svg/image579.svg) [公式: r4] | 11 |

#### 9.1.5.1 MPDCCH starting position

The starting OFDM symbol for MPDCCH given by index ![](media_svg/image580.svg) [公式≈: ^{l}MPDCCHStart] in the first slot in a subframe ![](media_svg/image581.svg) [公式: k] and is determined as follows

- ![](media_svg/image582.svg) [公式≈: ^{l}MPDCCHStart^{±}]is given by the higher layer parameter startSymbolBR

- if subframe ![](media_svg/image583.svg) [公式: k] is a special subframe or configured as an MBSFN subframe, and if the BL/CE UE is configured in CEModeA

- ![](media_svg/image584.svg) [公式≈: ^{ll}MPDCCHStartMPDCCHStart^{=}^{min2,}^{(}^{±}^{)}]

- else

- ![](media_svg/image585.svg) [公式≈: ^{ll}MPDCCHStartMPDCCHStart^{=}^{±}].

#### 9.1.5.2 Antenna ports quasi co-location for MPDCCH

Regardless of transmission modes configuration of PDSCH data transmissions, the BL/CE UE may assume the antenna ports 0 – 3, 107 – 110 of the serving cell are quasi co-located (as defined in [3]) with respect to Doppler shift, Doppler spread, average delay, and delay spread.

#### 9.1.5.3 Preconfigured Uplink Resource ACK/fallback procedure

If a UE has initiated a PUSCH transmission using preconfigured uplink resource on a given serving cell, and upon detection of a MPDCCH with DCI format 6-0A/6-0B with CRC scrambled by PUR-RNTI intended for the UE within the PUR search space window as defined in Clause 9.1.5, and the corresponding DCI is for PUR ACK/fallback indication (as defined in [4]),

- the UE shall deliver the PUR ACK/fallback indication, as signalled on the MPDCCH, to the higher layers, and

- the UE shall deliver to higher layers a 3-bit PUSCH repetition adjustment as signalled on the MPDCCH, where a bit with a value of 0 shall be prepended to the DCI field if the DCI field has a size of 2 bits.

### 9.1.6 SPDCCH assignment procedure

If the UE is configured with shortTTI, and SPDCCH is monitored in a slot, the term 'slot/subslot' refers to a slot in this clause.

If the UE is configured with shortTTI, and SPDCCH is monitored in a subslot, the term 'slot/subslot' refers to a subslot in this clause.

A UE configured with shortTTI is not expected to be configured with MBSFN subframe with zero-size non-MBSFN region.

For each serving cell, higher layer signalling can configure a UE with

- one or two SPDCCH-PRB-sets for SPDCCH monitoring in a slot/subslot of a non-MBSFN subframe, and

- one or two SPDCCH-PRB-sets for SPDCCH monitoring in a slot/subslot of an MBSFN subframe.

The PRBs corresponding to a SPDCCH-PRB-set are indicated by higher layers as described in Clause 9.1.6.2. Each SPDCCH-PRB-set consists of a set of SCCEs numbered from 0 to ![](media_svg/image586.svg) [公式≈: ^{N}SCCE,p^{−}^{1}]where ![](media_svg/image587.svg) [公式≈: ^{N}SCCE,p]is the number of SCCEs in SPDCCH-PRB-set  in a subframe. Each SPDCCH-PRB-set can be configured for either localized SPDCCH transmission or distributed SPDCCH transmission.

The UE shall monitor a set of SPDCCH candidates on one or more activated serving cells as configured by higher layer signalling for control information, where monitoring implies attempting to decode each of the SPDCCHs in the set according to the monitored DCI formats.

A UE is not required to monitor CRS-based SPDCCH in an MBSFN subframe.

A UE is not required to monitor CRS-based SPDCCH and DMRS-based SPDCCH in a slot/subslot if the UE does not support differentRSType.

A UE is not expected to receive DMRS-based SPDCCH scheduling PDSCH in slots/subslots where the UE is configured with DL transmission modes 1-4, 6.

The UE is not expected to be configured to monitor SPDCCH with carrier indicator field in a given serving cell.

The UE is not expected to monitor

- SPDCCH in the first subslot of a subframe

- SPDCCH in the first slot of a subframe if higher layer parameters dl-STTI-Length is set to 'slot'.

For 4 port CRS-based SPDCCH, a UE is not required to receive an SREG belonging to multiple PDCCH candidates if any resource element in that SREG corresponds to different antenna ports for those multiple PDCCH candidates, where the precoding sub-matrix is described in the precoding operation from clause 6.3.4.3 of 3GPP TS 36.211 [3].

The set of SPDCCH candidates to monitor are defined in terms of SPDCCH UE-specific search spaces. An SPDCCH UE-specific search space ![](media_svg/image588.svg) [公式≈: _{sS}_{k}(L)] or slot/subslot number k at aggregation level ![](media_svg/image589.svg) [公式: L⎰{1,2,4,8}] is defined by a set of SPDCCH candidates.

For a CRS-based SPDCCH-PRB-set ![](media_svg/image590.svg) [公式: p]or a DMRS-based SPDCCH-PRB-set ![](media_svg/image590.svg) [公式: p]configured with localized SPDCCH transmission in slot/subslot number ![](media_svg/image591.svg) [公式: k], the SCCEs corresponding to SPDCCH candidate ![](media_svg/image592.svg) [公式: m]of the search space ![](media_svg/image593.svg) [公式≈: _{sS}_{k}(L)] at aggregation level ![](media_svg/image594.svg) [公式: L]are given by

![](media_svg/image595.svg) [公式≈: ^{√}^{⌡}⌠_{⌡}_{∞}^{⊇}^{⊕}_{⊕}_{⊗}^{Y}p^{L}^{+}^{L}^{∪}^{√}^{⌡}⌠_{⌡}_{∞}^{⋅}⋅_{⋅}_{√}^{m}_{L}^{∪}_{∪}^{N}_{M}^{sCCE,}_{p,}(L_{k})^{p}^{∂}∂_{∂}_{∃}^{mod}√^{N}sCCE,p^{/}^{L}∃^{∅}^{⌡}∇_{⌡}_{∈}^{+}^{i}^{⇒}^{⇐}_{⇐}_{⇔}^{mod}^{N}sCCE,p^{∅}^{⌡}∇_{⌡}_{∈}]

For a DMRS-based SPDCCH-PRB-set ![](media_svg/image590.svg) [公式: p]configured with distributed SPDCCH transmission in slot/subslot number k, the SCCEs corresponding to SPDCCH candidate ![](media_svg/image592.svg) [公式: m]of the search space ![](media_svg/image596.svg) [公式≈: _{sS}_{k}(_{,}L_{l})]are given by

![](media_svg/image597.svg) [公式≈: ^{⊇}_{⊕}_{⊕}_{⊗}_{Y}_{p}L_{+}^{⋅}_{⋅}_{⋅}_{√}^{m}_{L}^{∪}_{∪}^{N}_{M}SCCE_{p}_{(}_{L}_{,}_{k}_{)},p^{∂}_{∂}_{∂}_{∃}^{⇒}_{⇐}_{⇐}_{⇔}_{mod}^{⋅}_{⋅}_{√}^{N}SCCE_{L},p^{∂}_{∂}_{∃}_{+}_{i}_{∪}^{⋅}_{⋅}_{√}^{N}SCCE_{L},p^{∂}_{∂}_{∃}]

where

![](media_svg/image598.svg) [公式≈: _{Y}_{p}L] is determined by higher layer parameter al- StartingPointSPDCCH,

![](media_svg/image599.svg) [公式≈: _{M}_{p}(L_{,}_{k})]is the number of SPDCCH candidates, determined by higher layer parameter dci7-CandidateSetsPerAL-SPDCCH-r15, to monitor among all the configured DCI formats for an aggregation level ![](media_svg/image594.svg) [公式: L]in SPDCCH-PRB-set ![](media_svg/image590.svg) [公式: p]in slot/subslot number ![](media_svg/image591.svg) [公式: k],![](media_svg/image600.svg) [公式≈: m=0,...,M_{p}^{(}^{L}_{,}_{k}^{)}−1].

For SPDCCH-PRB-set , and k belonging to the set of subslots indicated by higher layer parameter subslotApplicability-r15, ![](media_svg/image599.svg) [公式≈: _{M}_{p}(L_{,}_{k})]is given by the first value of higher layer parameter dci7-CandidateSetsPerAL-SPDCCH-r15 corresponding to aggregation level ![](media_svg/image594.svg) [公式: L], otherwise, ![](media_svg/image599.svg) [公式≈: _{M}_{p}(L_{,}_{k})] is given by the second value of higher layer parameter dci7-CandidateSetsPerAL-SPDCCH-r15 corresponding to aggregation level ![](media_svg/image594.svg) [公式: L].

The UE is not required to receive DMRS-based SPDCCH on resource blocks of a PRG overlapping with PBCH or primary or secondary synchronization signals in a slot/subslot.

A UE is not expected to be configured to monitor more than

- 6 SPDCCH candidates on a service cell in a subslot if the higher layer parameter dl-STTI-Length is set to 'subslot'

- 12 SPDCCH candidates on a serving cell in a slot if the higher layer parameter dl-STTI-Length is set to 'slot'.

A UE is not expected to monitor SPDCCH candidates over more than

- 16 SCCEs on a serving cell in a subslot if the higher layer parameter dl-STTI-Length is set to 'subslot'

- 32 SCCEs on a serving cell in a slot if the higher layer parameter dl-STTI-Length is set to 'slot'

A UE is not expected to monitor more than ![](media_svg/image602.svg) [公式: 68≠] numberOfBlindeDecodesUSS DCI blind decodes on PDCCH/EPDCCH and SPDCCH UE-specific search space(s) in a subframe if the UE indicated capability numberOfBlindeDecodesUSS .

#### 9.1.6.1 Resource mapping parameters for SPDCCH

For a given serving cell, if the UE is configured via higher layer signalling to monitor SPDCCH, for each SPDCCH-PRB-set, for

- CRS-based SPDCCH, the UE shall use the parameter set indicated by the higher layer parameter sPDCCH-NoOfSymbols to determine the SPDCCH symbols starting from the first OFDM symbol of the slot/subslot.

#### 9.1.6.2 PRB-pair indication for SPDCCH

For a given serving cell, for each CRS-based SPDCCH-PRB set , the UE is configured with a higher layer parameter resourceBlockAssignment indicating a combinatorial index  corresponding to the PRB index , () and given by equation , where  is the number of PRB-pairs associated with the downlink bandwidth,  is the number of PRB-pairs constituting SPDCCH-PRB-set, and is configured by the higher layer parameter numberRB-InFreq-domain and  is the extended binomial coefficient, resulting in unique label .

For a given serving cell, for each DMRS-based SPDCCH-PRB set , the UE is configured with a higher layer parameter resourceBlockAssignment indicating a combinatorial index  corresponding to the PRB indices ![](media_svg/image603.svg) [公式≈: 2≠{k_{i}}_{i}^{N}_{=}^{RB}^{2}_{0}^{X}^{p}^{−}^{1}−1], and ![](media_svg/image604.svg) [公式≈: 2≠{k_{i}}_{i}^{N}_{=}^{2}^{RB}_{0}^{X}^{p}^{−}^{1}], (![](media_svg/image605.svg) [公式≈: 1≥k_{i}≥_{√}N_{RB}^{DL}/2_{∃},k_{i}<k_{i}_{+}_{1}]) and given by equation ![](media_svg/image606.svg) [公式≈: ^{r}^{=}^{N}^{⊆}i=^{RB}^{2}^{X}0^{p}^{√}N^{N}_{RB}^{X}^{RB}^{DL}^{p}/^{/}2^{2}−^{∃}^{−}i^{k}^{i}], where  is the number of PRB-pairs associated with the downlink bandwidth,  is the number of PRB-pairs constituting SPDCCH-PRB-set, and is configured by the higher layer parameter numberRB-InFreq-domain and  is the extended binomial coefficient, resulting in unique label ![](media_svg/image607.svg) [公式≈: r⎰^{√}^{⌡}_{⌠}_{⌡}_{∞}0,...,^{⊇}^{⊕}_{⊕}_{⊗}^{√}_{N}^{N}_{RB}_{X}^{RB}^{DL}_{p}_{/}^{/}_{2}^{2}^{∃}^{⇒}^{⇐}_{⇐}_{⇔}−1^{∅}^{⌡}_{∇}_{⌡}_{∈}].

#### 9.1.6.3 Physical Resource Block (PRB) bundling for DMRS-based SPDCCH

For an SPDCCH-PRB-set with DMRS-based SPDCCH candidates, precoding granularity is 2 resource blocks in frequency domain. Precoding Resource block Groups (PRGs) of size 2 partition the system bandwidth and each PRG consists of consecutive PRBs. The UE is expected to receive UE-specific reference signal corresponding to a DMRS-based SPDCCH candidate over both resource blocks of a PRG. If ![](media_svg/image608.svg) [公式: N_{RB}^{DL}mod2>0] then, no DMRS-based SPDCCH candidate is mapped to the last resource block. The UE may assume that the same precoder applies on the two PRBs within a PRG.

#### 9.1.6.4 Antenna ports quasi co-location for DMRS-based SPDCCH

For a given serving cell, if the UE is configured to monitor DMRS-based SPDCCH in slots/subslots where the UE is configured via higher layer signalling to receive slot/subslot-PDSCH data transmissions according to transmission modes 8 and 9,

- the UE may assume the antenna ports 0 – 3, 107 of the serving cell are quasi co-located (as defined in [3]) with respect to Doppler shift, Doppler spread, average delay, and delay spread.

For a given serving cell, if the UE is configured to monitor DMRS-based SPDCCH in slots/subslots where the UE is configured via higher layer signalling to receive slot/subslot-PDSCH data transmissions according to transmission modes 10, for each DMRS-based SPDCCH-PRB-set,

- if the UE is configured by higher layers to decode slot/subslot-PDSCH according to quasi co-location Type-A as described in Clause 7.1.10

- the UE may assume the antenna ports 0 – 3, 107 of the serving cell are quasi co-located (as defined in [3]) with respect to Doppler shift, Doppler spread, average delay, and delay spread.

- if the UE is configured by higher layers to decode slot/subslot-PDSCH according to quasi co-location Type-B as described in Clause 7.1.10

- the UE may assume antenna ports 15 – 22 corresponding to the higher layer parameter qcl-CSI-RS-ConfigNZPId-r11 (defined in Clause 9.1.4.3) and antenna port 107 are quasi co-located (as defined in [3]) with respect to Doppler shift, Doppler spread, average delay, and delay spread.

## 9.2 PDCCH/EPDCCH/MPDCCH/SPDCCH validation for semi-persistent scheduling

A UE shall validate a Semi-Persistent Scheduling assignment PDCCH only if all the following conditions are met:

- the CRC parity bits obtained for the PDCCH payload are scrambled with the Semi-Persistent Scheduling C-RNTI or UL-SPS-V-RNTI

- the new data indicator field is set to '0'. In case of DCI formats 2, 2A, 2B, 2C and 2D, the new data indicator field refers to the one for the enabled transport block.

A UE shall validate a Semi-Persistent Scheduling assignment EPDCCH only if all the following conditions are met:

- the CRC parity bits obtained for the EPDCCH payload are scrambled with the Semi-Persistent Scheduling C-RNTI or UL-SPS-V-RNTI

- the new data indicator field is set to '0'. In case of DCI formats 2, 2A, 2B, 2C and 2D, the new data indicator field refers to the one for the enabled transport block.

A UE shall validate a Semi-Persistent Scheduling assignment MPDCCH only if all the following conditions are met:

- the CRC parity bits obtained for the MPDCCH payload are scrambled with the Semi-Persistent Scheduling C-RNTI

- the new data indicator field is set to '0'.

A UE shall validate a Semi-Persistent Scheduling assignment SPDCCH/PDCCH with DCI format 7-0A/7-0B /7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G only if all the following conditions are met:

- the CRC parity bits obtained for the SPDCCH/PDCCH payload are scrambled with the Semi-Persistent Scheduling C-RNTI

- the new data indicator field is set to '0'.

- the DMRS position indicator field for DCI formats 7-1F/7-1G is set to 0 in case of subslot-PDSCH.

- in case of subslot-PUSCH, the DMRS pattern field for DCI formats 7-0A/7-0B is set to,

- '0' for the LSB if the higher layer parameter semiPersistSchedIntervalUL is set to 1 subslot or if the UE is configured with higher layer parameter totalNumberPUSCH-SPS-STTI-UL-Repetitions, '00' otherwise for semi-persistent scheduling activation PDCCH /SPDCCH validation,

- '11' for semi-persistent scheduling release PDCCH /SPDCCH validation,

If the UE is not configured with more than one uplink SPS configuration on a given serving cell, validation is achieved if all the fields for the respective used DCI format are set according to Table 9.2-1 or Table 9.2-1A, 9.2-1B, 9.2-1C; otherwise, if the UE is configured with more than one uplink SPS configurations on a given serving cell, validation is achieved if all the fields excluding the 3 least significant bits of HARQ process number field for the respective used DCI format are set according to Table 9.2-1 or Table 9.2-1A.

If validation is achieved, the UE shall consider the received DCI information accordingly as a valid semi-persistent activation or release.

- If the valid DCI format 0 is scrambled with UL-SPS-V-RNTI, the UE shall consider the received DCI information as a valid semi-persistent activation or release only for the SPS configuration indicated by the UL SPS configuration index field.

- On a given serving cell, if the UE is configured with more than one uplink SPS configurations, and if the valid DCI format 0/7-0A/7-0B is scrambled with SPS C-RNTI, the UE shall consider the received DCI information as a valid semi-persistent activation or release only for the SPS configuration indicated by the 3 least significant bits of the HARQ process number field in the DCI.

If validation is not achieved, the received DCI format shall be considered by the UE as having been received with a non-matching CRC.

Table 9.2-1: Special fields for Semi-Persistent Scheduling Activation PDCCH/EPDCCH/SPDCCH Validation

|  | DCI format 0 | DCI format 1/1A | DCI format  2/2A/2B/2C/2D | DCI format  7-0A/7-0B | DCI format 7-1A/1B/1C/1D/1E/1F/1G |
| --- | --- | --- | --- | --- | --- |
| TPC command for scheduled PUSCH | set to '00' | N/A | N/A | set to '00' | N/A |
| Cyclic shift DM RS | set to '000' if present | N/A | N/A | set to '0' | N/A |
| Modulation and coding scheme  and redundancy version | MSB is set to '0' | N/A | N/A | N/A | N/A |
| HARQ process number | N/A | FDD: set to '000'TDD: set to '0000' | FDD: set to '000'TDD: set to '0000' | set to '0000' | set to '0000' |
| Modulation and coding scheme | N/A | MSB is set to '0' for 5-bit MCS field, otherwise two MSBs are set to '0' | For the enabled transport block: MSB is set to '0' for 5-bit MCS field, otherwise two MSBs are set to '0' | - | - |
| Redundancy version | N/A | set to '00' | For the enabled transport block: set to '00' | set to '00' | set to '00' |
| TPC command for slot/subslot-PUCCH | N/A | N/A | N/A | N/A | set to '00' |
| Cyclic Shift Field mapping table for DMRS | - | N/A | N/A | set to '0' | N/A |

Table 9.2-1A: Special fields for Semi-Persistent Scheduling Release PDCCH/EPDCCH/SPDCCH Validation

|  | DCI format 0 | DCI format 1A | DCI format 7-0A/7-0B | DCI format 7-1A/1B/1C/1D/1E/1F/1G |
| --- | --- | --- | --- | --- |
| TPC command for scheduled PUSCH | set to '00' | N/A | set to '00' | N/A |
| Cyclic shift DM RS | set to '000' if present | N/A | set to '0' | N/A |
| Modulation and coding scheme  and redundancy version | set to '11111' | N/A | N/A | N/A |
| Resource block assignment and  hopping resource allocation | Set to all '1's | N/A | N/A | N/A |
| HARQ process number | N/A | FDD: set to '000' TDD: set to '0000' | set to '0000' | set to '0000' |
| Modulation and coding scheme | N/A | set to '11111' for 5-bit MCS field, otherwise set to '111111' | set to '11111' | set to '11111' |
| Redundancy version | N/A | set to '00' | set to '00' | set to '00' |
| Resource block assignment | N/A | Set to all '1's | set to all '1's | set to all '1's |
| TPC command for slot/subslot-PUCCH | N/A | N/A | N/A | set to '00' |
| Cyclic Shift Field mapping table for DMRS | - | N/A | set to '0' | N/A |

Table 9.2-1B: Special fields for Semi-Persistent Scheduling Activation MPDCCH Validation

|  | DCI format 6-0A | DCI format 6-1A |
| --- | --- | --- |
| HARQ process number | set to '000' | Set to all '0's |
| Redundancy version | set to '00' | set to '00' |
| TPC command for scheduled PUSCH | set to '00' | N/A |
| TPC command for scheduled PUCCH | N/A | set to '00' |

Table 9.2-1C: Special fields for Semi-Persistent Scheduling Release MPDCCH Validation

|  | DCI format 6-0A | DCI format 6-1A |
| --- | --- | --- |
| HARQ process number | set to '000' | Set to all '0's |
| Redundancy version | set to '00' | set to '00' |
| Repetition number | set to '00' | set to '00' |
| Modulation and coding scheme | set to '1111' | set to '1111' |
| TPC command for scheduled PUSCH | set to '00' | N/A |
| Resource block assignment | Set to all '1's | Set to all '1's |

For the case that the DCI format indicates a semi-persistent downlink scheduling activation, the TPC command for PUCCH field shall be used as an index to one of the four PUCCH resource values configured by higher layers, with the mapping defined in Table 9.2-2

Table 9.2-2: PUCCH resource value for downlink semi-persistent scheduling

| Value of 'TPC command  for PUCCH' |  |
| --- | --- |
| '00' | The first PUCCH resource value configured by the higher layers |
| '01' | The second PUCCH resource value configured by the higher layers |
| '10' | The third PUCCH resource value configured by the higher layers |
| '11' | The fourth PUCCH resource value configured by the higher layers |

## 9.2A PDCCH/EPDCCH validation for autonomous uplink transmissions

A UE shall validate a autonomous uplink assignment PDCCH/EPDCCH only if all the following conditions are met:

- the CRC parity bits obtained for the PDCCH/EPDCCH payload are scrambled with the AUL C-RNTI; and

- the 'Flag for AUL differentiation' indicates activating/releasing AUL transmission.

Validation is achieved if all the fields for the respective used DCI format are set according to Table 9.2A-1 or Table 9.2A-2.

If validation is achieved, the UE shall consider the received DCI information accordingly as a valid autonomous uplink transmission activation or release.

If validation is not achieved, the received DCI format shall be considered by the UE as having been received with a non-matching CRC.

Table 9.2A-1: Special fields for Autonomous Uplink Activation PDCCH/EPDCCH Validation

|  | DCI Format 0A | DCI Format 4A |
| --- | --- | --- |
| PUSCH trigger A | Set to '0' | N/A |
| Timing offset | Set to '0000' | Set to '0000' |
| HARQ process number | Set to '0000' | Set to '0000' |
| New data indicator | Set to '0' | Set to '0' for both CWs |
| Redundancy version | Set to '00' | Set to '00' |
| TPC for scheduled PUSCH | Set to '00' | Set to '00' |
| CSI request | All bits set to '0' | All bits set to '0' |
| SRS request | Set to '0' | Set to '00' |
| PUSCH starting position | Set to '00' | Set to '00' |
| PUSCH ending position | Set to '0' | Set to '0' |
| Channel Access type | Set to '0' | Set to '0' |
| Channel Access Priority Class | Set to '00' | Set to '00' |

Table 9.2A-2: Special fields for Autonomous Uplink Release PDCCH/EPDCCH Validation

|  | DCI Format 0A | DCI Format 4A |
| --- | --- | --- |
| PUSCH trigger A | Set to '0' | N/A |
| Timing offset | Set to '1111' | Set to '1111' |
| Resource block assignment | All bits set to '1' | All bits set to '1' |
| Modulation and coding scheme | Set to '11111' | Set to '11111' for both CWs |
| HARQ process number | Set to '0000' | Set to '0000' |
| New data indicator | Set to '0' | Set to '0' for both CWs |
| Redundancy version | Set to '00' | Set to '00' |
| TPC for scheduled PUSCH | Set to '00' | Set to '00' |
| Cyclic shift for DM RS and OCC index | Set to '000' | Set to '000' |
| CSI request | All bits set to '0' | All bits set to '0' |
| SRS request | Set to '0' | Set to '00' |
| PUSCH starting position | Set to '00' | Set to '00' |
| PUSCH ending position | Set to '0' | Set to '0' |
| Channel Access type | Set to '0' | Set to '0' |
| Channel Access Priority Class | Set to '00' | Set to '00' |

## 9.3 PDCCH/EPDCCH/MPDCCH/SPDCCH control information procedure

A UE shall discard the PDCCH/EPDCCH/MPDCCH/SPDCCH if consistent control information is not detected.

For a serving cell, if the UE is configured with higher layer parameter blindSubframePDSCH-Repetitions, the UE shall discard any PDCCH/EPDCCH for PDSCH data transmissions in subframes in which the UE is receiving PDSCH assigned by PDCCH/EPDCCH with DCI format 1A with CRC scrambled by C-RNTI in UE-specific search space.

For a serving cell, if the UE is configured with higher layer parameter blindSlotSubslotPDSCH-Repetitions, the UE shall discard any PDCCH/SPDCCH for PDSCH data transmissions in slots/subslots in which the UE is receiving PDSCH assigned by PDCCH/SPDCCH with DCI format 7-1A/7-1B/7-1C/7-1D/7-1E/7-1F/7-1G with CRC scrambled by C-RNTI.
