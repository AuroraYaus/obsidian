---
type: spec
aliases:
  - content
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_36.213_36213-j30_s14-xx/content.md"
---
# TS 36.213 36213-j30_s14-xx

## 14UE procedures related to Sidelink

A UE can be configured by higher layers with one or more PSSCH resource configuration(s). A PSSCH resource configuration can be for reception of PSSCH, or for transmission of PSSCH. The physical sidelink shared channel related procedures are described in Clause 14.1.

A UE can be configured by higher layers with one or more PSCCH resource configuration(s). A PSCCH resource configuration can be for reception of PSCCH, or for transmission of PSCCH and the PSCCH resource configuration is associated with either sidelink transmission mode 1,2,3 or sidelink transmission mode 4. The physical sidelink control channel related procedures are described in Clause 14.2.

A UE can be configured by higher layers with one or more PSDCH resource configuration(s). A PSDCH resource configuration can be for reception of PSDCH, or for transmission of PSDCH. The transmissions of PSDCH according to a PSDCH resource configuration are associated with either sidelink discovery type 1 or sidelink discovery type 2B. The physical sidelink discovery channel related procedures are described in Clause 14.3.

The physical sidelink synchronization related procedures are described in Clause 14.4.

Except in the case of secondary sidelink synchronization signal transmission, sidelink transmission power shall not change during a sidelink subframe. For a UE transmitting PSBCH, the transmit power of PSBCH () is same as the transmit power of primary sidelink synchronisation signal .

A UE is not expected to be configured with PSCCH resource configuration(s) such that, in a given subframe, the total number of resource blocks across the resource block pools (as described in Clause 14.2.3) indicated by the PSCCH resource configuration(s) exceeds 50 in sidelink transmission mode 1 or 2.

In sidelink transmission mode 3 or 4, a UE is

-not expected to attempt to decode more than 10 or 20 PSCCHs in a subframe depending on the configuration of v2x-HighReception-r14.

-not expected to attempt to decode more than 100 or 136 RBs in a subframe depending on the configuration of v2x-HighReception-r14.

-not expected to attempt to decode more than 10 or 20 PSCCHs in a subframe depending on the configuration of v2x-HighReception-r15 and v2x-BandwidthClassRxSL-r15.

-not expected to attempt to decode more than 100 or 136 RBs in a subframe depending on the configuration of v2x-HighReception-r15 and v2x-BandwidthClassRxSL-r15.

-not expected to attempt to decode more than 15 or 30 PSCCHs in a subframe depending on the configuration of v2x-HighReception-r15 and v2x-BandwidthClassRxSL-r15.

-not expected to attempt to decode more than 150 or 204 RBs in a subframe depending on the configuration of v2x-HighReception-r15 and v2x-BandwidthClassRxSL-r15.

-not expected to combine PSCCH transmitted in different subframes.

-not required to perform PSSCH-RSRP measurement in a subframe that occurs before the reception of a successfully decoded associated SCI format 1.

If the UE does not indicate capability v2x-HighReception-r14 or v2x-HighReception-r15, it shall implement a mechanism to avoid systematic dropping of PSCCH when the number of PSCCH candidates exceeds the UE's capability. UE applies the PSSCH-RSRP measured in a subframe that occurs at the reception of a successfully decoded associated SCI format 1 to a subframe that is indicated by the SCI format 1 but occurs before the reception of the SCI format 1. UE applies the PSSCH-RSRP measured in a subframe that occurs at the reception of a successfully decoded associated SCI format 1 to a subframe that is indicated by the SCI format 1 if SCI format 1 scheduling the same transport block is successfully decoded in only one subframe. UE is not expected to decode PSSCH that occurs before the reception of a successfully decoded associated SCI format 1.

If a UE uplink transmission that is not a PRACH transmission in subframe n+1 of a serving cell overlaps in time domain with a PSDCH transmission or a SLSS transmission for PSDCH by the UE in subframe n and subframe n+1 is included in discTxGapConfig [11], then the UE shall drop the uplink transmission in subframe n+1. Else, if a UE uplink transmission in subframe n+1 of a serving cell overlaps in time domain with sidelink transmission/reception for sidelink transmission mode 1 or 2 by the UE in subframe n of the serving cell, then the UE shall drop the sidelink transmission/reception in subframe n.

If a UE uplink transmission of a serving cell overlaps in time domain with a sidelink transmission for sidelink transmission mode 3 or 4 of the same serving cell and the value in "Priority" field of the corresponding SCI is smaller than the high layer parameter thresSL-TxPrioritization, then the UE shall drop the uplink transmission. Else, if a UE uplink transmission of a serving cell overlaps in time domain with sidelink transmission for sidelink transmission mode 3 or 4 of the same serving cell, then the UE shall drop the sidelink transmission.

For a given carrier frequency, a UE is not expected to receive sidelink physical channels/signals with different cyclic prefix lengths in the same sidelink subframe.

For a given carrier frequency, in a sidelink subframe, if a UE has a sidelink transmission, the sidelink transmission shall occur only in contiguous physical resource blocks in sidelink transmission mode 1 or 2.

In sidelink transmission mode 1 or 2, if a UE's sidelink transmission does not occur on a serving cell with its uplink transmission(s), and if the UE's sidelink transmission in a subframe overlaps in time with its uplink transmission(s), the UE shall adjust the sidelink transmission power such that its total transmission power does not exceed defined in [6] on any overlapped portion. In this case, calculation of the adjustment to the sidelink transmission power is not specified.

In sidelink transmission mode 3 or 4, if a UE's sidelink transmission has SCI whose "Priority" field is set to a value smaller than the high layer parameter thresSL-TxPrioritization, and if the UE's sidelink transmission in a subframe overlaps in time with its uplink transmission(s) occurring on serving cell(s) where the sidelink transmission does not occur, the UE shall adjust the uplink transmission power such that its total transmission power does not exceed defined in [6] on any overlapped portion. In this case, calculation of the adjustment to the uplink transmission power is not specified.

In sidelink transmission mode 3 or 4, if a UE's sidelink transmission has SCI whose "Priority" field is set to a value greater than or equal to the high layer parameter thresSL-TxPrioritization, and if the UE's sidelink transmission in a subframe overlaps in time with its uplink transmission(s) occurring on serving cell(s) where the sidelink transmission does not occur, the UE shall adjust the sidelink transmission power such that its total transmission power does not exceed defined in [6] on any overlapped portion. In this case, calculation of the adjustment to the sidelink transmission power is not specified.

In sidelink transmission mode 3 or 4, if a UE's sidelink transmission on a carrier overlaps in time with sidelink transmission on other carrier(s) and its total transmission power exceeds defined in [6], the UE shall adjust the transmission power of the sidelink transmission which has SCI whose "Priority" field is set to the largest value among all the "Priority" values of the overlapped sidelink transmissions such that its total transmission power does not exceed defined in [6]. In this case, calculation of the adjustment to the sidelink transmission power is not specified. If the transmission power still exceeds  defined in [6] after this power adjustment, the UE shall drop the sidelink transmission with the largest "Priority" field in its SCI and repeat this procedure over the non-dropped carriers. It is not specified which sidelink transmission the UE adjusts when sidelink transmissions overlapping in time on two or more carriers have the same value for the "Priority" field.

## 14.1Physical Sidelink Shared Channel related procedures

## 14.1.1UE procedure for transmitting the PSSCH

If the UE transmits SCI format 0 on PSCCH according to a PSCCH resource configuration in subframe n belonging to a PSCCH period (described in Clause 14.2.3), then for the corresponding PSSCH transmissions

-the transmissions occur in a set of subframes in the PSCCH period and in a set of resource blocks within the set of subframes. The first PSSCH transport block is transmitted in the first four subframes in the set, the second transport block is transmitted in the next four subframes in the set, and so on.

-for sidelink transmission mode 1,

-the set of subframes is determined using the subframe pool indicated by the PSSCH resource configuration (described in Clause 14.1.4) and using time resource pattern () in the SCI format 0 as described in Clause 14.1.1.1.

-the set of resource blocks is determined using Resource block assignment and hopping allocation in the SCI format 0 as described in Clause 14.1.1.2.

-for sidelink transmission mode 2,

-the set of subframes is determined using the subframe pool indicated by the PSSCH resource configuration (described in Clause 14.1.3) and using time resource pattern () in the SCI format 0 as described in Clause 14.1.1.3.

-the set of resource blocks is determined using the resource block pool indicated by the PSSCH resource configuration (described in Clause 14.1.3) and using Resource block assignment and hopping allocation in the SCI format 0 as described in Clause 14.1.1.4.

-the modulation order is determined using the "modulation and coding scheme " field () in SCI format 0. For, the modulation order is set to , where is determined from Table 8.6.1-1.

-the TBS index () is determined based onand Table 8.6.1-1, and the transport block size is determined using  and the number of allocated resource blocks () using the procedure in Clause 7.1.7.2.1.

If the UE transmits SCI format 1 on PSCCH according to a PSCCH resource configuration in subframe n, then for the corresponding PSSCH transmissions of one TB

-for sidelink transmission mode 3,

-the set of subframes and the set of resource blocks are determined using the subframe pool indicated by the PSSCH resource configuration (described in Clause 14.1.5) and using "Retransmission index and Time gap between initial transmission and retransmission" field and "Frequency resource location of the initial transmission and retransmission" field in the SCI format 1 as described in Clause 14.1.1.4A.

-for sidelink transmission mode 4,

-the set of subframes and the set of resource blocks are determined using the subframe pool indicated by the PSSCH resource configuration (described in Clause 14.1.5) and using "Retransmission index and Time gap between initial transmission and retransmission" field and "Frequency resource location of the initial transmission and retransmission" field in the SCI format 1 as described in Clause 14.1.1.4B.

-if higher layer indicates that rate matching for the last symbol in the subframe is used for the given PSSCH

-Transmission Format of corresponding SCI format 1 is set to 1,

-the modulation order is determined using the "modulation and coding scheme " field () in SCI format 1.

-for , the TBS index () is determined based onand Table 8.6.1-1,

-for , the TBS index () is determined based onand Table 14.1.1-2,

-the transport block size is determined by using  and setting the Table 7.1.7.2.1-1 column indicator to , where  to the total number of allocated PRBs based on the procedure defined in Clause 14.1.1.4A and 14.1.1.4B.

-otherwise

-Transmission Format of SCI format 1 is set to 0 if present,

-the modulation order is determined using the "modulation and coding scheme " field () in SCI format 1. For, the modulation order is set to , where is determined from Table 8.6.1-1.

-the TBS index () is determined based onand Table 8.6.1-1, and the transport block size is determined using  and the number of allocated resource blocks () using the procedure in Clause 7.1.7.2.1.

For sidelink transmission mode 3 and 4, the parameter  is given by table 14.1.1-1.

Table 14.1.1-1: Determination offor sidelink transmission mode 3 and 4

Table 14.1.1-2: Modulation and TBS index table for

## 14.1.1.1UE procedure for determining subframes for transmitting PSSCH for sidelink transmission mode 1

Within the PSCCH period (described in Clause 14.2.3), the subframes used for PSSCH are determined as follows:

-a subframe indicator bitmap  and are determined using the procedure described in Clause 14.1.1.1.1.

-a bitmap  is determined using and a subframe  in the subframe pool is used for PSSCH if , otherwise the subframe is not used for PSSCH, where  and are described in Clause 14.1.4. The subframes used for PSSCH are denoted by arranged in increasing order of subframe index and where is the number of subframes that can be used for PSSCH transmission in a PSCCH period and is a multiple of 4.

## 14.1.1.1.1Determination of subframe indicator bitmap

For FDD and TDD with UL/DL configuration belonging to {1,2,4,5}, is 8, and the mapping between Time Resource pattern Index () and subframe indicator bitmap is given by table 14.1.1.1.1-1.

For TDD with UL/DL configuration 0, is 7, and the mapping between Time Resource pattern Index () and subframe indicator bitmap is given by table 14.1.1.1.1-2.

For TDD with UL/DL configuration belonging to {3,6}, is 6, and the mapping between Time Resource pattern Index () and subframe indicator bitmap is given by table 14.1.1.1.1-3.

Table 14.1.1.1.1-1: Time Resource pattern Index mapping for

Table 14.1.1.1.1-2: Time Resource pattern Index mapping for

Table 14.1.1.1.1-3: Time Resource pattern Index mapping for

## 14.1.1.2UE procedure for determining resource blocks for transmitting PSSCH for sidelink transmission mode 1

The set of resource blocks is determined using the procedure described in Clause 14.1.1.2.1 and 14.1.1.2.2.

## 14.1.1.2.1PSSCH resource allocation for sidelink transmission mode 1

The resource allocation and hopping field of the SCI format 0 is used to determine a set of indices denoted by (0 ≤ < ), a starting index , and a number of allocated PRBs  and using the procedure in Clause 8.1.1, and 8.4 (for sidelink frequency hopping with type 1 or type 2 hopping) with the following exceptions:

-the term 'PUSCH' in Clauses 8.1.1 and 8.4 is replaced with 'PSSCH'.

-the quantity  in Clause 8.1.1 is replaced with  .

-the quantity  in Clauses 8.1.1 and 8.4 is replaced with .

-the quantity in Clauses 8.1.1and 8.4 is replaced with .

-the quantityin Clauses 8.1.1 and 8.4 is replaced with.

-the quantity  in Clause 8.4 is replaced with .

-the quantity  is given by higher layer parameter rb-Offset-r12 associated with the corresponding PSSCH resource configuration.

-the quantity  is given by higher layer parameter numSubbands-r12 associated with the corresponding PSSCH resource configuration.

## 14.1.1.2.2PSSCH frequency hopping for sidelink transmission mode 1

If sidelink frequency hopping with type 1 hopping is enabled, the set of physical resource blocks for PSSCH transmission is determined using Clause 8.4 with the following exceptions:

-the term 'PUSCH' is replaced with 'PSSCH'.

-only inter-subframe hopping shall be used.

-the quantity  is replaced with .

-the quantity is replaced with .

-the quantity  is replaced with .

-the quantity  is given by higher layer parameter rb-Offset-r12 associated with the PSSCH resource configuration.

-the frequency hopping field in the SCI format 0 is used instead of DCI format 0.

-the quantity is replaced with .

-the quantity  is replaced with .

-for odd  (described in Clause 9.2.4 of [3]), the set of physical resource blocks for PSSCH transmission are contiguous resource blocks starting from PRB with index.

-for even  (described in Clause 9.2.4 of [3]), the set of physical resource blocks for PSSCH transmission are contiguous resource blocks starting from PRB with index.

## 14.1.1.3UE procedure for determining subframes for transmitting PSSCH for sidelink transmission mode 2

For FDD or for TDD, and the UE not configured with the higher layer parameter trpt-Subset-r12

-The allowed values of correspond to the values of satisfying  , for a value of in , where  and  are determined from table 14.1.1.3-1.

For FDD or for TDD with UL/DL configuration belonging to {0,1,2,3,4,6}, and the UE configured with the higher layer parameter trpt-Subset-r12

-The allowed values of correspond to the values of satisfying  , for values of  in satisfying ,  and where  and  are determined from table 14.1.1.3-1, and is the bitmap indicated by trpt-Subset-r12.

Table 14.1.1.3-1: Determination of and  for sidelink transmission mode 2

Within a PSCCH period, the subframes used for PSSCH are determined as follows:

-a subframe indicator bitmap  and are determined using the procedure described in Clause 14.1.1.1.1 from the allowed values of described in this Clause.

-a bitmap  is determined using and a subframe  in the subframe pool is used for PSSCH if , otherwise the subframe is not used for PSSCH, where  and are described in Clause 14.1.3. The subframes used for PSSCH are denoted by arranged in increasing order of subframe index and where is the number of subframes that can be used for PSSCH transmission in a PSCCH period and is a multiple of 4.

## 14.1.1.4UE procedure for determining resource blocks for transmitting PSSCH for sidelink transmission mode 2

The set of resource blocks within the resource block pool (defined in 14.1.3) is determined using the Clause 14.1.1.2.1 .

If sidelink frequency hopping with type 1 hopping is enabled, the set of physical resource blocks for PSSCH transmission is determined using Clause 14.1.1.2.2 with the following exceptions

-the quantity is replaced with  (defined in 14.1.3).

-for odd , the set of physical resource blocks for PSSCH transmission are given by contiguous resource blocksbelonging to the resource block pool, where .

-for even , the set of physical resource blocks for PSSCH transmission are given by contiguous resource blocksbelonging to the resource block pool, where .

## 14.1.1.4AUE procedure for determining subframes and resource blocks for transmitting PSSCH for sidelink transmission mode 3

If the UE has a configured sidelink grant (described in [8]) in subframe  with the corresponding PSCCH resource m (described in Clause 14.2.4), the resource blocks and subframes of the corresponding PSSCH transmissions are determined according to 14.1.1.4C.

If the UE has a configured sidelink grant (described in [8]) for an SL SPS configuration activated by Clause 14.2.1 and if a set of sub-channels in subframe  is determined as the time and frequency resource for PSSCH transmission corresponding to the configured sidelink grant (described in [8]) of the SL SPS configuration, the same set of sub-channels in subframes  are also determined for PSSCH transmissions corresponding to the same sidelink grant where j=1, 2,…, , and  is determined by Clause 14.1.5. Here,  is the sidelink SPS interval of the corresponding SL SPS configuration.

## 14.1.1.4BUE procedure for determining subframes and resource blocks for transmitting PSSCH and reserving resources for sidelink transmission mode 4

If the UE has a configured sidelink grant (described in [8]) in subframe with the corresponding PSCCH resource m (described in Clause 14.2.4), the resource blocks and subframes of the corresponding PSSCH transmissions are determined according to 14.1.1.4C.

The number of subframes in one set of the time and frequency resources for transmission opportunities of PSSCH is given by  where = 10*SL_RESOURCE_RESELECTION_COUNTER [8] if configured else is set to 1.

If a set of sub-channels in subframe  is determined as the time and frequency resource for PSSCH transmission corresponding to the configured sidelink grant (described in [8]), the same set of sub-channels in subframes  are also determined for PSSCH transmissions corresponding to the same sidelink grant where j=1, 2,…, ,  , and  is determined by Clause 14.1.5. Here,  is the resource reservation interval indicated by higher layers.

If a UE is configured with high layer parameter cr-Limit and transmits PSSCH in subframe n, the UE shall ensure the following limits for any priority value k;

where  is the CR evaluated in subframe n-4 for the PSSCH transmissions with "Priority" field in the SCI set to i, and  corresponds to the high layer parameter cr-Limit that is associated with the priority value k and the CBR range which includes the CBR measured in subframe n-4. It is up to UE implementation how to meet the above limits, including dropping the transmissions in subframe n.

## 14.1.1.4CUE procedure for determining subframes and resource blocks for PSSCH transmission associated with an SCI format 1

The set of subframes and resource blocks for PSSCH transmission is determined by the resource used for the PSCCH transmission containing the associated SCI format 1, and "Frequency resource location of the initial transmission and retransmission" field, "Retransmission index" field, "Time gap between initial transmission and retransmission" field of the associated SCI format 1 as described below.

"Frequency resource location of the initial transmission and retransmission" field in the SCI format 1 is equal to resource indication value (RIV) corresponding to a starting sub-channel index () and a length in terms of contiguously allocated sub-channels ( 1). The resource indication value is defined by

if  then

else

where  is the total number of sub-channels in the pool determined by higher layer parameter numSubchannel.

For the SCI format 1 transmitted on the PSCCH resource m (described in subcaluse 14.2.4) in subframe , the set of subframes and sub-channels for the corresponding PSSCH are determined as follows:

-if  is zero,

-the time and frequency resources for the corresponding PSSCH is given by

-sub-channel(s)  in subframe .

-else if"Retransmission index" in the SCI format 1 is zero,

-the time and frequency resources for the corresponding PSSCH is given by

-sub-channel(s)  in subframe , and

-sub-channels  in subframe .

-else if"Retransmission index" in the SCI format 1 is one,

-the time and frequency resources for the corresponding PSSCH is given by

-sub-channels  in subframe , and

-sub-channels  in subframe .

where  is the value indicated by "Time gap between initial transmission and retransmission" field the SCI format 1 and  is determined by Clause 14.1.5.

When sub-channel(s)  are determined in a subframe for the transmission of PSSCH, the set of resource blocks determined for the PSSCH transmission is given by  contiguous resource blocks with the physical resource block number  for . Here,  and  are given by higher layer parameters startRBSubchannel and sizeSubchannel, respectively. The parameters  and  are given as follows:

-if a pool is (pre)configured such that a UE always transmits PSCCH and the corresponding PSSCH in adjacent resource blocks in a subframe,  and  is the largest integer that fulfils

where  is a set of non-negative integers

-if a pool is (pre)configured such that a UE may transmit PSCCH and the corresponding PSSCH in non-adjacent resource blocks in a subframe,  and  is the largest integer that fulfils

where  is a set of non-negative integers.

## 14.1.1.5UE procedure for PSSCH power control

For sidelink transmission mode 1 and PSCCH period i, the UE transmit power  for PSSCH transmission is given by the following

-if the TPC command field in configured sidelink grant (described in [8]) for PSCCH period i is set to 0

-

-if the TPC command field in configured sidelink grant (described in [8]) for PSCCH period i is set to 1

- [dBm]

where  is defined in [6], and is the bandwidth of the PSSCH resource assignment expressed in number of resource block and  whereis defined in Clause 5.1.1.1.  and  are provided by higher layer parameters p0-r12 and alpha-r12, respectively and that are associated with the corresponding PSSCH resource configuration.

For sidelink transmission mode 2, the UE transmit power  for PSSCH transmission is given by

[dBm] ,

where  is defined in [6], and is the bandwidth of the PSSCH resource assignment expressed in number of resource blocks and  where is defined in Clause 5.1.1.1.  and  are provided by higher layer parameters p0-r12 and alpha-r12, respectively and that are associated with the corresponding PSSCH resource configuration.

For sidelink transmission mode 3, the UE transmit power  for PSSCH transmission is given by

[dBm] ,

where  is defined in [6], and is the bandwidth of the PSSCH resource assignment expressed in number of resource blocks and  where is defined in Clause 5.1.1.1.  and  are provided by higher layer parameters p0SL-V2V and alphaSL-V2V, respectively and that are associated with the corresponding PSSCH resource configuration.

For sidelink transmission mode 4, the UE transmit power  for PSSCH transmission in subframe n is given by

[dBm] ,

where  is defined in [6],  is the bandwidth of the PSSCH resource assignment expressed in number of resource blocks, , and  where is defined in Clause 5.1.1.1.  and  are provided by higher layer parameters p0SL-V2V and alphaSL-V2V, respectively and that are associated with the corresponding PSSCH resource configuration. If higher layer parameter maxTxpower is configured then

else

where is set to a maxTxpower value based on the priority level of the PSSCH and the CBR range which includes the CBR measured in subframe n-4.

## 14.1.1.6UE procedure for determining the subset of resources to be reported to higher layers in PSSCH resource selection in sidelink transmission mode 4 and in sensing measurement in sidelink transmission mode 3

In sidelink transmission mode 4, when requested by higher layers in subframe n for a carrier, the UE shall determine the set of resources to be reported to higher layers for PSSCH transmission according to the steps described in this Clause. Parameters  the number of sub-channels to be used for the PSSCH transmission in a subframe,  the resource reservation interval, and  the priority to be transmitted in the associated SCI format 1 by the UE are all provided by higher layers (described in [8]).  is determined according to Clause 14.1.1.4B.

In sidelink transmission mode 3, when requested by higher layers in subframe n for a carrier, the UE shall determine the set of resources to be reported to higher layers in sensing measurement according to the steps described in this Clause. Parameters ,  and are all provided by higher layers (described in [11]).  is determined by=10*SL_RESOURCE_RESELECTION_COUNTER, where SL_RESOURCE_RESELECTION_COUNTER is provided by higher layers [11].

If partial sensing is not configured by higher layers then the following steps are used:

1)A candidate single-subframe resource for PSSCH transmission  is defined as a set of  contiguous sub-channels with sub-channel x+j in subframe  where . The UE shall assume that any set of  contiguous sub-channels included in the corresponding PSSCH resource pool (described in 14.1.5) within the time interval  corresponds to one candidate single-subframe resource, where selections of  and  are up to UE implementations under  and , if  is provided by higher layers for , otherwise . UE selection of  shall fulfil the latency requirement. The total number of the candidate single-subframe resources is denoted by.

2)The UE shall monitor subframes ,, …,  except for those in which its transmissions occur, where  if subframe n belongs to the set , otherwise subframe is the first subframe after subframe n belonging to the set . The UE shall perform the behaviour in the following steps based on PSCCH decoded and S-RSSI measured in these subframes.

3)The parameter  is set to the value indicated by the i-th SL-ThresPSSCH-RSRP field in SL-ThresPSSCH-RSRP-List where .i=(a-1)*8+b

4)The set  is initialized to the union of all the candidate single-subframe resources. The set  is initialized to an empty set.

5)The UE shall exclude any candidate single-subframe resource  from the set  if it meets all the following conditions:

-the UE has not monitored subframe  in Step 2.

-there is an integer j which meets  where j=0, 1, …, , , k is any value allowed by the higher layer parameter restrictResourceReservationPeriod and q=1,2,…,Q. Here,  if  and , where  if subframe n belongs to the set , otherwise subframe  is the first subframe belonging to the set  after subframe n; and  otherwise.

6)The UE shall exclude any candidate single-subframe resource  from the set  if it meets all the following conditions:

-the UE receives an SCI format 1 in subframe , and "Resource reservation" field and "Priority" field in the received SCI format 1 indicate the values  and , respectively according to Clause 14.2.1.

-PSSCH-RSRP measurement according to the received SCI format 1 is higher than .

-the SCI format received in subframe or the same SCI format 1 which is assumed to be received in subframe(s)  determines according to 14.1.1.4C the set of resource blocks and subframes which overlaps with  for q=1, 2, …, Q and j=0, 1, …, . Here, if  and , where  if subframe n belongs to the set , otherwise subframe is the first subframe after subframe n belonging to the set ; otherwise .

7)If the number of candidate single-subframe resources remaining in the set  is smaller than , then Step 4 is repeated with  increased by 3 dB.

8)For a candidate single-subframe resource  remaining in the set, the metric  is defined as the linear average of S-RSSI measured in sub-channels x+k for  in the monitored subframes in Step 2 that can be expressed by  for a non-negative integer j if , and  for a non-negative integer j otherwise.

9)The UE moves the candidate single-subframe resource  with the smallest metric  from the set  to . This step is repeated until the number of candidate single-subframe resources in the set  becomes greater than or equal to ,

10)When the UE is configured by upper layers to transmit using resource pools on multiple carriers, it shall exclude a candidate single-subframe resource  from  if the UE does not support transmission in the candidate single-subframe resource in the carrier under the assumption that transmissions take place in other carrier(s) using the already selected resources due to its limitation in the number of simultaneous transmission carriers, its limitation in the supported carrier combinations, or interruption for RF retuning time [10].

The UE shall report set  to higher layers.

If partial sensing is configured by higher layers then the following steps are used:

1)A candidate single-subframe resource for PSSCH transmission  is defined as a set of  contiguous sub-channels with sub-channel x+j in subframe  where . The UE shall determine by its implementation a set of subframes which consists of at least  subframes within the time interval  where selections of  and  are up to UE implementations under  and , if  is provided by higher layers for , otherwise . UE selection of  shall fulfil the latency requirement and  shall be greater than or equal to the high layer parameter minNumCandidateSF. The UE shall assume that any set of  contiguous sub-channels included in the corresponding PSSCH resource pool (described in 14.1.5) within the determined set of subframes correspond to one candidate single-subframe resource. The total number of the candidate single-subframe resources is denoted by.

2)If a subframe  is included in the set of subframes in Step 1, the UE shall monitor any subframe  if k-th bit of the high layer parameter gapCandidateSensing is set to 1. The UE shall perform the behaviour in the following steps based on PSCCH decoded and S-RSSI measured in these subframes.

3)The parameter  is set to the value indicated by the i-th SL-ThresPSSCH-RSRP field in SL-ThresPSSCH-RSRP-List where . i=(a-1)*8+b

4)The set  is initialized to the union of all the candidate single-subframe resources. The set  is initialized to an empty set.

5)The UE shall exclude any candidate single-subframe resource  from the set  if it meets all the following conditions:

-the UE receives an SCI format 1 in subframe , and "Resource reservation" field and "Priority" field in the received SCI format 1 indicate the values  and , respectively according to Clause 14.2.1.

-PSSCH-RSRP measurement according to the received SCI format 1 is higher than .

-the SCI format received in subframe or the same SCI format 1 which is assumed to be received in subframe(s)  determines according to 14.1.1.4C the set of resource blocks and subframes which overlaps with  for q=1, 2, …, Q and j=0, 1, …, . Here, if  and , where  is the last subframe of the  subframes , and  otherwise.

6)If the number of candidate single-subframe resources remaining in the set  is smaller than , then Step 4 is repeated with  increased by 3 dB.

7)For a candidate single-subframe resource  remaining in the set, the metric  is defined as the linear average of S-RSSI measured in sub-channels x+k for  in the monitored subframes in Step 2 that can be expressed by  for a non-negative integer j.

8)The UE moves the candidate single-subframe resource  with the smallest metric  from the set  to . This step is repeated until the number of candidate single-subframe resources in the set  becomes greater than or equal to .

9)When the UE is configured by upper layers to transmit using resource pools on multiple carriers, it shall exclude a candidate single-subframe resource  from  if the UE does not support transmission in the candidate single-subframe resource in the carrier under the assumption that transmissions take place in other carrier(s) using the already selected resources due to its limitation in the number of simultaneous transmission carriers, its limitation in the supported carrier combinations, or interruption for RF retuning time [10].

The UE shall report set  to higher layers.

If transmission based on random selection is configured by upper layers and when the UE is configured by upper layers to transmit using resource pools on multiple carriers, the following steps are used:

1)A candidate single-subframe resource for PSSCH transmission  is defined as a set of  contiguous sub-channels with sub-channel x+j in subframe  where . The UE shall assume that any set of  contiguous sub-channels included in the corresponding PSSCH resource pool (described in 14.1.5) within the time interval  corresponds to one candidate single-subframe resource, where selections of  and  are up to UE implementations under  and , if  is provided by higher layers for , otherwise . UE selection of  shall fulfil the latency requirement. The total number of the candidate single-subframe resources is denoted by.

2)The set  is initialized to the union of all the candidate single-subframe resources. The set  is initialized to an empty set.

3)The UE moves the candidate single-subframe resource  from the set  to .

4)The UE shall exclude a candidate single-subframe resource  from  if the UE does not support transmission in the candidate single-subframe resource in the carrier under the assumption that transmissions take place in other carrier(s) using the already selected resources due to its limitation in the number of simultaneous transmission carriers, its limitation in the supported carrier combinations, or interruption for RF retuning time [10].

The UE shall report set  to higher layers.

## 14.1.1.7Conditions for selecting resources when the number of HARQ transmissions is two in sidelink transmission mode 4

When a set of subframes  for  have been selected for a set of transmission opportunities of PSSCH, a set of subframes  for  for another set of transmission opportunities of PSSCH shall meet the conditions ,  and  mod  where  and  is the maximum number of transmission opportunities of PSSCH in a selected subframe set. Here,  is the resource reservation interval provided by higher layers.kPrsvp_TX'≠0

## 14.1.2UE procedure for receiving the PSSCH

For sidelink transmission mode 1, a UE upon detection of SCI format 0 on PSCCH can decode PSSCH according to the detected SCI format 0.

For sidelink transmission mode 2, a UE upon detection of SCI format 0 on PSCCH can decode PSSCH according to the detected SCI format 0, and associated PSSCH resource configuration configured by higher layers.

For sidelink transmission mode 3, a UE upon detection of SCI format 1 on PSCCH can decode PSSCH according to the detected SCI format 1, and associated PSSCH resource configuration configured by higher layers.

For sidelink transmission mode 4, a UE upon detection of SCI format 1 on PSCCH can decode PSSCH according to the detected SCI format 1, and associated PSSCH resource configuration configured by higher layers.

## 14.1.3UE procedure for determining resource block pool and subframe pool for sidelink transmission mode 2

For a PSCCH period associated with the PSCCH resource configuration (determined in Clause 14.2.3) which is also associated with the PSSCH resource configuration, the UE determines a PSSCH pool consisting of a subframe pool and resource block pool as follows.

-For TDD, if the parameter tdd-Config-r12 is indicated by the PSCCH resource configuration, the TDD UL/DL configuration used for determining the subframe pool is given by the parameter tdd-Config-r12, otherwise, the TDD UL/DL configuration used for determining the subframe pool is given by the UL/DL configuration (i.e. parameter subframeAssignment) for the serving cell.

-Within the PSCCH period, the uplink subframes with subframe index greater than or equal to  are denoted by arranged in increasing order of subframe index, where  is described in Clause 14.2.3 and  is the offsetIndicator-r12 indicated by the PSSCH resource configuration, where denotes the number of uplink subframes within the PSCCH period with subframe index greater than or equal to .

-A bitmap  is determined using, for , where  and  are the bitmap and the length of the bitmap indicated by subframeBitmap-r12, respectively.

-A subframe  () belongs to the subframe pool if . The subframes in the subframe pool are denoted by arranged in increasing order of subframe index and denotes the number of subframes in the subframe pool.

-A PRB with index  () belongs to the resource block pool if  or if , where S1, S2, and M denote the prb-Start-r12, prb-End-r12 and prb-Num-r12 indicated by the PSSCH resource configuration respectively.

-The resource blocks in the resource block pool are denoted by arranged in increasing order of resource block indices and  is the number of resource blocks in the resource block pool.

14.1.4UE procedure for determining subframe pool for sidelink transmission mode 1

For a PSCCH period associated with the PSCCH resource configuration (described in Clause 14.2.3) which is also associated with the PSSCH resource configuration, the UE determines a PSSCH pool consisting of a subframe pool as follows.

-For TDD, if the parameter tdd-Config-r12 is indicated by the PSCCH resource configuration, the TDD UL/DL configuration used for determining the subframe pool is given by the parameter tdd-Config-r12, otherwise, the TDD UL/DL configuration used for determining the subframe pool is given by the UL/DL configuration (i.e. parameter subframeAssignment) for the serving cell.

-Each uplink subframe with subframe index greater than or equal to belongs to the subframe pool for PSSCH, where  and  are described in Clause 14.2.3.

-The subframes in the subframe pool for PSSCH are denoted by arranged in increasing order of subframe index and denotes the number of subframes in the subframe pool.

## 14.1.5UE procedure for determining resource block pool and subframe pool for sidelink transmission mode 3 and 4

The set of subframes that may belong to a PSSCH resource pool for sidelink transmission mode 3 or 4 is denoted by  where

-,

-the subframe index is relative to subframe#0 of the radio frame corresponding to SFN 0 of the serving cell or DFN 0 (described in [11]),

-the set includes all the subframes except the following subframes,

-subframes in which SLSS resource is configured,

-downlink subframes and special subframes if the sidelink transmission occurs in a TDD cell,

-reserved subframes which are determined by the following steps:

1)the remaining subframes excluding  and  subframes from the set of all the subframes are denoted by  arranged in increasing order of subframe index, where  is the number of subframes in which SLSS resource is configured within 10240 subframes and  is the number of downlink subframes and special subframes within 10240 subframes if the sidelink transmission occurs in a TDD cell.

2)a subframe  belongs to the reserved subframes if  where  and . Here,  the length of the bitmap is configured by higher layers.

-the subframes are arranged in increasing order of subframe index.

The UE determines the set of subframes assigned to a PSSCH resource pool as follows:

-A bitmap  associated with the resource pool is used where  the length of the bitmap is configured by higher layers.b0,b1,…,bLbitmap-1

-A subframe  belongs to the subframe pool if  where  .

The UE determines the set of resource blocks assigned to a PSSCH resource pool as follows:

-The resource block pool consists of  sub-channels where  is given by higher layer parameter numSubchannel.

-The sub-channel m for  consists of a set of  contiguous resource blocks with the physical resource block number  for  where  and  are given by higher layer parameters startRBSubchannel and sizeSubchannel, respectively

## 14.2Physical Sidelink Control Channel related procedures

For sidelink transmission mode 1, if a UE is configured by higher layers to receive DCI format 5 with the CRC scrambled by the SL-RNTI, the UE shall decode the PDCCH/EPDCCH according to the combination defined in Table 14.2-1.

Table 14.2-1: PDCCH/EPDCCH configured by SL-RNTI

For sidelink transmission mode 3, if a UE is configured by higher layers to receive DCI format 5A with the CRC scrambled by the SL-V-RNTI or SL-SPS-V-RNTI , the UE shall decode the PDCCH/EPDCCH according to the combination defined in Table 14.2-2. A UE is not expected to receive DCI format 5A with size larger than DCI format 0 in the same search space that DCI format 0 is defined on.

Table 14.2-2: PDCCH/EPDCCH configured by SL-V-RNTI or SL-SPS-V-RNTI

The carrier indicator field value in DCI format 5A corresponds to v2x-InterFreqInfo.

## 14.2.1UE procedure for transmitting the PSCCH

For sidelink transmission mode 1and PSCCH period i,

the UE shall determine the subframes and resource blocks for transmitting SCI format 0 as follows.

-SCI format 0 is transmitted in two subframes in the subframe pool and one physical resource block per slot in each of the two subframes, wherein the physical resource blocks belong to the resource block pool, where the subframe pool and the resource block pool are indicated by the PSCCH resource configuration (as defined in Clause 14.2.3)

-the two subframes and the resource blocks are determined using "Resource for PSCCH" field () in the configured sidelink grant (described in [8]) as described in Clause 14.2.1.1.

the UE shall set the contents of the SCI format 0 as follows:

-the UE shall set the Modulation and coding scheme field according to the Modulation and coding scheme indicated by the higher layer parameter mcs-r12 if the parameter is configured by higher layers.

-the UE shall set the Frequency hopping flag according to the "Frequency hopping flag" field in the configured sidelink grant.

-the UE shall set the Resource block assignment and hopping resource allocation according to the "Resource block assignment and hopping resource allocation" field in the configured sidelink grant.

-the UE shall set the Time resource pattern according to the "Time resource pattern" field in the configured sidelink grant .

-the UE shall set the eleven-bit Timing advance indication to  to indicate sidelink reception timing adjustment value using the NTA (defined in [3]) value for the UE in the subframe that is no earlier than subframe  (described in Clause 14.2.1.1).

For sidelink transmission mode 2,

-SCI format 0 is transmitted in two subframes in the subframe pool and one physical resource block per slot in each of the two subframes, wherein the physical resource blocks belongs to the resource block pool, where the subframe pool and the resource block pool are indicated by the PSCCH resource configuration (as defined in Clause 14.2.3)

-the two subframes and the resource blocks are determined using the procedure described in Clause 14.2.1.2

-the UE shall set the eleven-bit Timing advance indication  in the SCI format 0 to zero.

For sidelink transmission mode 3,

-The UE shall determine the subframes and resource blocks for transmitting SCI format 1 as follows:

-SCI format 1 is transmitted in two physical resource blocks per slot in each subframe where the corresponding PSSCH is transmitted.

-If the UE receives in subframe n DCI format 5A with the CRC scrambled by the SL-V-RNTI, one transmission of PSCCH is in the PSCCH resource  (described in Clause 14.2.4) in the first subframe that is included in  and that starts not earlier than .  is the value indicated by "Lowest index of the sub-channel allocation to the initial transmission" associated with the configured sidelink grant (described in [8]) if the field "Lowest index of the sub-channel allocation to the initial transmission" in the corresponding DCI format 5A is present and  otherwise,  is determined by Clause 14.1.5, the value m is indicated by 'SL index' field in the corresponding DCI format 5A according to Table 14.2.1-1 if this field is present and m=0 otherwise,  is the start of the downlink subframe carrying the DCI, and  and  are described in [3].tqSL TDL-NTA2×TS+4+m×10-3LInit=0TDLNTATS

-If "Time gap between initial transmission and retransmission" in the configured sidelink grant (described in [8]) is not equal to zero, another transmission of PSCCH is in the PSCCH resource  in subframe , where  is the value indicated by "Time gap between initial transmission and retransmission" field in the configured sidelink grant.  corresponds to the value  determined by the procedure in Clause 14.1.1.4C with the RIV set to the value indicated by "Frequency resource location of the initial transmission and retransmission" field in the configured sidelink grant.

-If the UE receives in subframe n DCI format 5A with the CRC scrambled by the SL-SPS-V-RNTI , the UE shall consider the received DCI information as a valid sidelink semi-persistent activation or release only for the SPS configuration indicated by the SL SPS configuration index field. If the received DCI activates an SL SPS configuration, one transmission of PSCCH is in the PSCCH resource  (described in Clause 14.2.4) in the first subframe  that is included in  and that starts not earlier than .  is the value indicated by "Lowest index of the sub-channel allocation to the initial transmission" associated with the configured sidelink grant (described in [8]) if the field "Lowest index of the sub-channel allocation to the initial transmission" in the corresponding DCI format 5A is present and  otherwise,  is determined by Clause 14.1.5, the value m is indicated by 'SL index' field in the corresponding DCI format 5A according to Table 14.2.1-1 if this field is present and m=0 otherwise,  is the start of the downlink subframe carrying the DCI, and  and  are described in [3]..tqSL TDL-NTA2×TS+4+m×10-3LInit=0TDLNTATS

-If "Time gap between initial transmission and retransmission" in the configured sidelink grant (described in [8]) is not equal to zero, another transmission of PSCCH is in the PSCCH resource  in subframe , where  is the value indicated by "Time gap between initial transmission and retransmission" field in the configured sidelink grant.  corresponds to the value  determined by the procedure in Clause 14.1.1.4C with the RIV set to the value indicated by "Frequency resource location of the initial transmission and retransmission" field in the configured sidelink grant.

-The UE shall set the contents of the SCI format 1 as follows:

-the UE shall set the Modulation and coding scheme as indicated by higher layers.

-the UE shall set the "Priority" field according to the highest priority among those priority(s) indicated by higher layers corresponding to the transport block. Priority field '000' corresponds to priority '1', priority field '001' corresponds to priority '2', and so on.

-the UE shall set the Time gap between initial transmission and retransmission field, the Frequency resource location of the initial transmission and retransmission field, and the Retransmission index field such that the set of time and frequency resources determined for PSSCH according to Clause 14.1.1.4C is in accordance with the PSSCH resource allocation indicated by the configured sidelink grant.

-the UE shall set the Resource reservation according to table 14.2.1-2 based on indicated value X, where X is equal to the Resource reservation interval provided by higher layers divided by 100.

-Each transmission of SCI format 1 is transmitted in one subframe and two physical resource blocks per slot of the subframe.

-The UE shall randomly select the cyclic shift  among {0, 3, 6, 9} in each PSCCH transmission.

For sidelink transmission mode 4,

-The UE shall determine the subframes and resource blocks for transmitting SCI format 1 as follows:

-SCI format 1 is transmitted in two physical resource blocks per slot in each subframe where the corresponding PSSCH is transmitted.

-If the configured sidelink grant from higher layer indicates the PSCCH resource in subframe , one transmission of PSCCH is in the indicated PSCCH resource m (described in Clause 14.2.4) in subframe .

-If "Time gap between initial transmission and retransmission" in the configured sidelink grant (described in [8]) is not equal to zero, another transmission of PSCCH is in the PSCCH resource  in subframe  where  is the value indicated by "Time gap between initial transmission and retransmission" field in the configured sidelink grant,  corresponds to the value  determined by the procedure in Clause 14.1.1.4C with the RIV set to the value indicated by "Frequency resource location of the initial transmission and retransmission" field in the configured sidelink grant.

-the UE shall set the contents of the SCI format 1 as follows:

-the UE shall set the Modulation and coding scheme as indicated by higher layers.

-the UE shall set the "Priority" field according to the highest priority among those priority(s) indicated by higher layers corresponding to the transport block. Priority field '000' corresponds to priority '1', priority field '001' corresponds to priority '2', and so on.

-the UE shall set the Time gap between initial transmission and retransmission field, the Frequency resource location of the initial transmission and retransmission field, and the Retransmission index field such that the set of time and frequency resources determined for PSSCH according to Clause 14.1.1.4C is in accordance with the PSSCH resource allocation indicated by the configured sidelink grant.

-the UE shall set the Resource reservation field according to table 14.2.1-2 based on indicated value X, where X is equal to the Resource reservation interval provided by higher layers divided by 100.

-Each transmission of SCI format 1 is transmitted in one subframe and two physical resource blocks per slot of the subframe.

-The UE shall randomly select the cyclic shift  among {0, 3, 6, 9} in each PSCCH transmission.

Table 14.2.1-1: Mapping of DCI format 5A offset field to indicated value m

Table 14.2.1-2: Determination of the Resource reservation field in SCI format 1

## 14.2.1.1UE procedure for determining subframes and resource blocks for transmitting PSCCH for sidelink transmission mode 1

For ,

-one transmission of the PSCCH is in resource block of subframe  of the PSCCH period, where  and .

-the other transmission of the PSCCH is in resource block  of subframe  of the PSCCH period, where  and .

where,, and are described in Clause 14.2.3.

## 14.2.1.2UE procedure for determining subframes and resource blocks for transmitting PSCCH for sidelink transmission mode 2

The allowed values for PSCCH resource selection are given by 0,1…  where and  described in Clause 14.2.3. The two subframes and the resource blocks are determined using selected resource value  (described in [8]) and the procedure described in Clause 14.2.1.1.

## 14.2.1.3UE procedure for PSCCH power control

For sidelink transmission mode 1 and PSCCH period i, the UE transmit power  for PSCCH transmission is given by the following

-if the TPC command field in the configured sidelink grant (described in [8]) for PSCCH period i is set to 0

-

-if the TPC command field in the configured sidelink grant (described in [8]) for PSCCH period i is set to 1

- [dBm]

where  is defined in [6], and =1 and  where is defined in Clause 5.1.1.1.  and  are provided by higher layer parameters p0-r12 and alpha-r12, respectively and are associated with the corresponding PSCCH resource configuration.

For sidelink transmission mode 2, the UE transmit power  for PSCCH transmission is given by

[dBm] ,

where  is the configured by higher layers and =1 and  whereis defined in Clause 5.1.1.1.  and  are provided by higher layer parameters p0-r12 and alpha-r12, respectively and are associated with the corresponding PSCCH resource configuration.

For sidelink transmission mode 3, the UE transmit power  for PSCCH transmission is given by

[dBm],

where  is defined in [6], is the bandwidth of the PSSCH resource assignment expressed in number of resource block, , and  where is defined in Clause 5.1.1.1.  and  are provided by higher layer parameters p0SL-V2V and alphaSL-V2V, respectively and that are associated with the corresponding PSSCH resource configuration.

For sidelink transmission mode 4, the UE transmit power  for PSCCH transmission in subframe n is given by

[dBm],

where is defined in [6], is the bandwidth of the PSSCH resource assignment expressed in number of resource block, , and  where is defined in Clause 5.1.1.1.  and  are provided by higher layer parameters p0SL-V2V and alphaSL-V2V, respectively and that are associated with the corresponding PSSCH resource configuration. If higher layer parameter maxTxpower is configured then

else

where is set to a maxTxpower value based on the priority level of the PSSCH and the CBR range which includes the CBR measured in subframe n-4.

## 14.2.2UE procedure for receiving the PSCCH

For each PSCCH resource configuration associated with sidelink transmission mode 1, a UE configured by higher layers to detect SCI format 0 on PSCCH shall attempt to decode the PSCCH according to the PSCCH resource configuration, and using the Group destination IDs indicated by higher layers.

For each PSCCH resource configuration associated with sidelink transmission mode 2, a UE configured by higher layers to detect SCI format 0 on PSCCH shall attempt to decode the PSCCH according to the PSCCH resource configuration, and using the Group destination IDs indicated by higher layers.

For each PSCCH resource configuration associated with sidelink transmission mode 3, a UE configured by higher layers to detect SCI format 1 on PSCCH shall attempt to decode the PSCCH according to the PSCCH resource configuration. The UE is not required to decode more than one PSCCH at each PSCCH resource candidate. The UE shall not assume any value for the "Reserved bits" before decoding a SCI format 1.

For each PSCCH resource configuration associated with sidelink transmission mode 4, a UE configured by higher layers to detect SCI format 1 on PSCCH shall attempt to decode the PSCCH according to the PSCCH resource configuration. The UE is not required to decode more than one PSCCH at each PSCCH resource candidate. The UE shall not assume any value for the "Reserved bits" before decoding a SCI format 1.

## 14.2.3UE procedure for determining resource block pool and subframe pool for PSCCH

The following procedure is used for sidelink transmission mode 1 and 2.

A PSCCH resource configuration for transmission/reception is associated with a set of periodically occurring time-domain periods (known as PSCCH periods). The i-th PSCCH period begins at subframe with subframe index and ends in subframe with subframe index , where

-,

-the subframe index is relative to subframe#0 of the radio frame corresponding to SFN 0 of the serving cell or DFN 0 (described in [11]),

- is the offsetIndicator-r12 indicated by the PSCCH resource configuration,

-is the sc-Period-r12 indicated by the PSCCH resource configuration.

For a PSCCH period, the UE determines a PSCCH pool consisting of a subframe pool and a resource block pool as follows.

-For TDD, if the parameter tdd-Config-r12 is indicated by the PSCCH resource configuration, the TDD UL/DL configuration used for determining the subframe pool is given by the parameter tdd-Config-r12, otherwise, the TDD UL/DL configuration used for determining the subframe pool is given by the UL/DL configuration (i.e. parameter subframeAssignment) for the serving cell.

-The first uplink subframes are denoted by arranged in increasing order of subframe index, where is the length of the bitmap subframeBitmap-r12 indicated by the PSCCH resource configuration.

-A subframe  () belongs to the subframe pool if, where is the bitmap subframeBitmap-r12 indicated by the PSCCH resource configuration. The subframes in the subframe pool are denoted by arranged in increasing order of subframe index and  is the number of subframes in the subframe pool. A PRB with index  () belongs to the resource block pool if or if , where S1, S2, and M denote the prb-Start-r12, prb-End-r12 and prb-Num-r12 indicated by the PSCCH resource configuration respectively.

-The resource blocks in the resource block pool are denoted by arranged in increasing order of resource block indices and  is the number of resource blocks in the resource block pool.

## 14.2.4UE procedure for determining resource block pool for PSCCH in sidelink transmission mode 3 and 4

The following procedure is used for sidelink transmission mode 3 and 4.

If a pool is (pre)configured such that a UE always transmits PSCCH and the corresponding PSSCH in adjacent resource blocks in a subframe, the PSCCH resource m is the set of two contiguous resource blocks with the physical resource block number  for j=0 and 1 where  and  are given by higher layer parameters startRBSubchannel and sizeSubchannel, respectively.

If a pool is (pre)configured such that a UE may transmit PSCCH and the corresponding PSSCH in non-adjacent resource blocks in a subframe, the PSCCH resource m is the set of two contiguous resource blocks with the physical resource block number  for j=0 and 1 where  is given by higher layer parameter startRBPSCCHPool.

14.3Physical Sidelink Discovery Channel related procedures

14.3.1UE procedure for transmitting the PSDCH

If a UE is configured by higher layers to transmit PSDCH according to a PSDCH resource configuration, in a PSDCH period ,

-the number of transmissions for a transport block on PSDCH is  where is given by the higher layer parameter numRetx-r12, and each transmission corresponds to one subframe belonging to a set of subframes, and in each subframe, the PSDCH is transmitted on two physical resource blocks per slot.

-for sidelink discovery type 1,

-the allowed values for PSDCH resource selection are given by 0,1… , where and , and

-the j-th transmission () for the transport block occurs in contiguous resource blocks and of subframe  of the PSDCH period, where

- and  and using selected resource value  (described in [8]).

-,,andare described in Clause 14.3.3.

-for sidelink discovery type 2B,

-The j-th transmission () for the transport block occurs in contiguous resource blocks and of subframe  of the PSDCH period, where

-

-

- for

- and , and,,andare described in Clause 14.3.3.

- and  are given by higher layer parameters discPRB-Index and discSF-Index, respectively and that associated with the PSDCH resource configuration.

-, andare given by higher layer parameters a-r12, b-r12, and c-r12, repectively and that are associated with the PSDCH resource configuration.

- is the number of PSDCH periods since  was received.

-the transport block size is 232

For sidelink discovery, the UE transmit power  for PSDCH transmission is given by the following

[dBm]

where  is defined in [6], and =2 and  where is defined in Clause 5.1.1.1 where

is the serving cell if the sidelink discovery transmission occurs on the uplink carrier frequency of a serving cell, or

is the cell indicated by higher layers on downlink carrier frequency indicated by discCarrierRef-r13[11] if sidelink discovery transmission does not occur on the uplink carrier frequency of a serving cell.

and  are provided by higher layer parameters p0-r12 and alpha-r12, respectively and are associated with the corresponding PSDCH resource configuration.

A UE shall drop any PSDCH transmissions that are associated with sidelink discovery type 1 in a sidelink subframe if the UE has a PSDCH transmission associated with sidelink discovery type 2B in that subframe.

14.3.2UE procedure for receiving the PSDCH

For sidelink discovery type 1, for each PSDCH resource configuration associated with reception of PSDCH, a UE configured by higher layers to detect a transport block on PSDCH can decode the PSDCH according to the PSDCH resource configuration.

For sidelink discovery type 2B, for each PSDCH resource configuration associated with reception of PSDCH, a UE configured by higher layers to detect a transport block on PSDCH can decode the PSDCH according to the PSDCH resource configuration.

14.3.3UE procedure for determining resource block pool and subframe pool for sidelink discovery

A PSDCH resource configuration for transmission/reception is associated with a set of periodically occurring time-domain periods (known as PSDCH periods). The i-th PSDCH period begins at subframe with subframe index and ends in subframe with subframe index , where

-,

-the subframe index is relative to subframe#0 of a radio frame corresponding to SFN 0 of the serving cell or DFN 0 (described in [11]),

- is the offsetIndicator-r12 indicated by the PSDCH resource configuration

-is the discPeriod-r12 indicated by the PSDCH resource configuration.

For a PSDCH period, the UE determines a discovery pool consisting of a subframe pool and a resource block pool for PSDCH as follows.

-For TDD, if the parameter tdd-Config-r12 is indicated by the PSDCH resource configuration, the TDD UL/DL configuration used for determining the subframe pool is given by the parameter tdd-Config-r12, otherwise, the TDD UL/DL configuration used for determining the subframe pool is given by the UL/DL configuration (i.e. parameter subframeAssignment) for the serving cell.

-A bitmap  is obtained using, for , where and are the bitmap and the length of the bitmap indicated by subframeBitmap-r12, respectively, and , where is the numRepetition-r12 indicated by the PSDCH resource configuration.

-The first uplink subframes are denoted by  arranged in increasing order of subframe index.

-A subframe  () belongs to the subframe pool if . The subframes in the subframe pool are denoted by arranged in increasing order of subframe index and  denotes the number of subframes in the subframe pool.

-A PRB with index  () belongs to the resource block pool if or if , where S1, S2, and M denote the prb-Start-r12, prb-End-r12 and prb-Num-r12 indicated by the PSDCH resource configuration respectively.

-The resource blocks in the resource block pool are denoted by arranged in increasing order of resource block indices and  is the number of resource blocks in the resource block pool.

14.4Physical Sidelink Synchronization related procedures

The synchronization resource configuration(s) for the UE are given by the higher layer parameter SL-SyncConfig-r12 or v2x-SyncConfig.

A UE shall transmit sidelink synchronisation signals according to Clause 5.10.7 in [11].

A UE may assume that sidelink synchronization signals are signals transmitted by an eNB as described in Clause 6.11 of [3] or are signals transmitted by a UE as described in [11].

A UE is not expected to blindly detect the cyclic prefix length of sidelink synchronization signals transmitted by another UE.

For a sidelink synchronization resource configuration associated with PSDCH reception, if cell c is indicated by the parameter physCellId-r12 and if the parameter discSyncWindow-r12 is configured with value w1 for cell c, the UE may assume that sidelink synchronization signals are transmitted in cell c and that they are received within a reference synchronization window of size +/-w1 ms with respect to the sidelink synchronization resource of cell c indicated by higher layers. The sidelink synchronization identity associated with the sidelink synchronization resource is indicated by higher layers.

For PSDCH reception, if cell c is indicated by the parameter physCellId-r12 and if the parameter discSyncWindow-r12 is configured with value w2 for cell c, the UE may assume that PSDCH of UE in cell c is received within a reference synchronization window of size +/-w2 ms with respect to the discovery resource of cell c indicated by higher layers.

The UE transmit power of primary sidelink synchronization signal  and the UE transmit power of secondary synchronization signal  are given by

-If the UE is configured with sidelink transmission mode 1, and if the UE transmits sidelink synchronization signals in PSCCH period i, and if the TPC command field in the configured sidelink grant (described in [8]) for the PSCCH period i is set to 0

-

-

-otherwise

- [dBm] ,

- [dBm] ,

where  and  are defined in [6]. and  where is defined in Clause 5.1.1.1.  and  are provided by higher layer parameters associated with the corresponding sidelink synchronization signal resource configuration.

If sidelink synchronization signals are transmitted for PSDCH, and if the PSDCH transmission does not occur on any serving cell configured for the UE,  is the cell indicated by higher layers on downlink carrier frequency indicated by discCarrierRef [11]. Otherwise,  is the serving cell on which the sidelink synchronization signals are transmitted. If sidelink synchronization signals are transmitted for PSDCH, then PSDCH and sidelink synchronization signal transmission occur on the same carrier frequency.

## 15Void

## 16UE Procedures related to narrowband IoT

Throughout this clause,

-for a NB-IoT UE in a IoT NTN TDD serving cell,

-the UE shall not assume any downlink physical signal or physical channel is present in any subframe other than within the D consecutive downlink subframes according to the frame structure type 1 for IoT NTN TDD and the value of D defined in [3],

-the UE shall not transmit any uplink physical signal or physical channel in any subframe other than within the U consecutive uplink subframes according to the frame structure type 1 for IoT NTN TDD and the value of U defined in [3].

-the term “DL subframe” includes the 𝐷 consecutive downlink subframes, the 𝑈 consecutive uplink subframes and guard period subframes as defined in [3].

-for a NB-IoT UE, the value of  is given by,Koffset

-if the UE is configured with the higher layer parameter k-Offset,

- whereKoffset= Kcell_offset-KUE_offset

is the parameter k-Offset provided by higher layers, andKcell_offset

is the parameter Differential Koffset provided by higher layers, otherwise KUE_offsetKUE_offset=0

-otherwise,

-.Koffset=0

If the UE is configured with higher layer parameter k-Offset, for an NPUSCH (re)transmission associated with the TC-RNTI,  k-Offset.Koffset=

## 16.1Synchronization procedures

## 16.1.1Cell search

Cell search is the procedure by which a UE acquires time and frequency synchronization with a cell and detects the narrowband physical layer Cell ID.

If the higher layer parameter operationModeInfo indicates 'inband-SamePCI' or samePCI-Indicator indicates 'samePCI'' for a cell, the UE may assume that the physical layer cell ID is same as the narrowband physical layer cell ID for the cell.

The following signals are transmitted in the downlink to facilitate cell search for Narrowband IoT: the narrowband primary and narrowband secondary synchronization signals.

A UE may assume the antenna ports 2000 – 2001 and the antenna port for the narrowband primary/secondary synchronization signals of a serving cell are quasi co-located (as defined in [3]) with respect to Doppler shift and average delay.

## 16.1.2Timing synchronization

Upon reception of a timing advance command, the UE shall adjust uplink transmission timing for NPUSCH, and SR if configured with higher layer parameter sr-WithoutHARQ-ACK-Config, based on the received timing advance command.

The timing advance command indicates the change of the uplink timing relative to the current uplink timing as multiples of 16. The start timing of the random access preamble is specified in [3].

In case of random access response, an 11-bit timing advance command [8], TA, indicates NTA values by index values of TA = 0, 1, 2, ..., 1536, where an amount of the time alignment is given by NTA = TA 16. NTA is defined in [3].

In other cases, a 6-bit timing advance command [8] or the Timing advance adjustment field in DCI format N0 if present [4], TA, indicates adjustment of the current NTA value, NTA,old, to the new NTA value, NTA,new, by index values of TA = 0, 1, 2,..., 63, where NTA,new = NTA,old + (TA 31)16. Here, adjustment of NTA value by a positive or a negative amount indicates advancing or delaying the uplink transmission timing by a given amount respectively.

For a timing advance command reception ending in DL subframe n, the corresponding adjustment of the uplink transmission timing shall apply for the uplink NPUSCH transmissions starting from subframe n+12 +Koffset+1. When the UE's uplink NPUSCH transmissions in NB-IoT uplink slot n and NB-IoT uplink slot n+1 are overlapped due to the timing adjustment, the UE shall complete transmission of NB-IoT uplink slot n and not transmit the overlapped part of NB-IoT uplink slot n+1.

If the received downlink timing changes and is not compensated or is only partly compensated by the uplink timing adjustment without timing advance command as specified in [10], the UE changes NTA accordingly.

For a UE in a NTN serving cell, using serving satellite higher-layer ephemeris parameters, if configured, the UE determines  (defined in [3]) using the serving satellite position and its own position to pre-compensate the two-way transmission delay on the service link. To pre-compensate the two-way transmission delay between the uplink time synchronization reference point and the serving satellite, the UE determines (defined in [3]) based on one-way propagation delay  which can be obtained as:NTA,adjUENTA,adjcommon Delaycommont

Delaycommont=12NTAcommon+NTAcommonDrift×t-tepoch+NTAcommonDriftVariation×t-tepoch2

where , , and  are given by the higher layer parameters nta-Common, nta-CommonDrift, and nta-CommonDriftVariation respectively, and  is the epoch time given by the higher layer parameter epochTime.  provides a distance at time  between the serving satellite and the uplink time synchronization reference point divided by the speed of light. The uplink time synchronization reference point is the point where DL and UL are frame aligned with an offset given by .NTAcommonNTAcommonDriftNTAcommonDriftVariationtepochDelaycommon(t)tNTA,offset

For a NB-IoT UE communicating over NTN FDD, time and frequency pre-compensation is adjusted per uplink segment with a transmission duration of  time units, where the quantity  is provided by higher layers, as specified in 3GPP TS 36.331 [11].NsegmentprecompensationNsegmentprecompensation

In case of CB-Msg3 EDT procedure for a UE communicating over NTN, the start timing of a NPUSCH transmission using CB-Msg3 resource shall be aligned with the start of the corresponding uplink subframe at the UE by assuming .NTA=0

## 16.2Power control

## 16.2.1Uplink power control

Uplink power control controls the transmit power of the different uplink physical channels.

## 16.2.1.1Narrowband physical uplink shared channel

## 16.2.1.1.1UE behaviour

The setting of the UE Transmit power for a Narrowband Physical Uplink Shared Channel (NPUSCH) transmission is defined as follows. For FDD or IoT NTN TDD, if the UE is capable of enhanced random access power control [12], and it is configured by higher layers, and for TN TDD, enhanced random access power control shall be applied for a UE which started the random access procedure in the first or second configured NPRACH repetition level.

The UE transmit power  for NPUSCH transmission in NB-IoT UL slot i for the serving cell is given by:

For NPUSCH (re)transmissions corresponding to the random access response grant if enhanced random access power control is not applied, and for all other NPUSCH transmissions except for NPUSCH (re)transmission corresponding to preconfigured uplink resource, when the number of repetitions of the allocated NPUSCH RUs is greater than 2:

[dBm]

otherwise

[dBm]PPUSCH,c(i)=min&PCMAX,c(i),&10log10(MNPUSCH,c(i))+PO_NPUSCH,c(j)+αc(j)⋅PLc+ΔTF,c(i))

where,

-is the configured UE transmit power defined in [6] in NB-IoT UL slot i for serving cell .

- is the NPUSCH transmission resource bandwidth normalized by 15 kHz, where {1/4} is used for 3.75 kHz subcarrier spacing and {1, 3, 6, 12} are used for 15kHz subcarrier spacingMNPUSCH,c(i)

- is a parameter composed of the sum of a component  provided from higher layers and a component  provided by higher layers for j=1, 3 and for serving cell where . For NPUSCH (re)transmissions corresponding to a dynamic scheduled grant or a semi-persistent grant then j=1, for NPUSCH (re)transmissions corresponding to the random access response grant then j=2 and for NPUSCH transmission using preconfigured uplink resource then j=3. . If enhanced random access power control is not applied, , where the parameter preambleInitialReceivedTargetPower [8] () and  are signalled from higher layers for serving cell . If enhanced random access power control is applied, PO_NPUSCH,cjPO_UE_NPUSCH,c2=0PO_NOMINAL_NPUSCH,c(2)=PO_PRE+∆PREAMBLE_Msg3∆PREAMBLE_Msg3

PO_NOMINAL_NPUSCH,c2=MSG3_RECEIVED_TARGET_POWER +ΔPREAMBLE_Msg3

-For CB-Msg3 transmissions, then j=4, and  is the parameter CB-MSG3_RECEIVED_TARGET_POWER provided by higher layers for serving cell .PO_PUSCH,c(4)

-For j=1, for NPUSCH format 2, =1; for NPUSCH format 1, is provided by higher layers for serving cell . For j=2,  For j=3,  is the parameter alpha in PUR-Config-NB provided by higher layers for serving cell . For j=4, is the parameter alpha in CB-Msg3-ConfigSIB-NB provided by higher layers for serving cell .

- is the downlink path loss estimate calculated in the UE for serving cell  in dB and  = nrs-Power + nrs-PowerOffsetNonAnchor – NRSRP, where nrs-Power is provided by higher layers and Clause 16.2.2, and nrs-PowerOffsetNonAnchor is set to zero if it is not provided by higher layers and NRSRP is defined in [5] for serving cell .

-If a NB-IoT UE is configured with npusch-16QAM-Config or pur-UL-16QAM-Config, then for NPUSCH (re)transmissions with QPSK and 16QAM,

- for and  for where  is given by the parameter deltaMCS-Enabled provided by higher layers for serving cell , andΔTF,ci=10log102BPRE⋅Ks-1∆TF,c(i)=0

- where  is the code block size and  is the number of resource elements determined as  where , ,  are defined in [3], and  is defined in section 16.5.1.1BPRE=K/NREKNRENRE=(NsymbUL-1)NslotsULNscRUNRUNsymbULNslotsULNscRUNRU

-otherwise .∆TF,c(i)=0

## 16.2.1.1.2Power headroom

If the UE transmits NPUSCH in NB-IoT UL slot  for serving cell , power headroom is computed using

[dB]

where, , , , and, are defined in Clause 16.2.1.1.1.

The power headroom shall be rounded down to the closest value in the set [PH1, PH2, PH3, PH4] dB if enhanced PHR is not configured and [PH1, PH2, …, PH15, PH16] dB if enhanced PHR is configured as defined in [10]. The power headroom is delivered by the physical layer to higher layers.

## 16.2.1.2SR

## 16.2.1.2.1UE behaviour

If the UE is configured with higher layer parameter sr-WithoutHARQ-ACK-Config, the setting of the UE transmit power for SR transmission without HARQ-ACK is defined as follows.

The UE transmit power  for SR transmission in NB-IoT UL slot i for the serving cell is given by:

[dBm]

where,

-is the configured UE transmit power defined in [6] in NB-IoT UL slot i for serving cell .

-is {1/3} for NPRACH format 2 and {1}for NPRACH format 0/1.

-is signaled from higher layers for serving cell .

- is signaled from higher layers for serving cell .

- is defined in Clause 16.2.1.1.1.

## 16.2.2Downlink power allocation

The eNodeB determines the downlink transmit energy per resource element.

For an NB-IoT cell, the UE may assume NRS EPRE is constant across the downlink NB-IoT system bandwidth and constant across all subframes that contain NRS, until different NRS power information is received.

The downlink NRS EPRE can be derived from the downlink narrowband reference-signal transmit power given by nrs-Power + nrs-PowerOffsetNonAnchor, where the parameter nrs-Power is provided by higher layers and nrs-PowerOffsetNonAnchor is zero if it is not provided by higher layers. The downlink narrowband reference-signal transmit power is defined as the linear average over the power contributions (in [W]) of all resource elements that carry narrowband reference signals within the operating NB-IoT system bandwidth.

A UE may assume that the ratio of NWUS EPRE to NRS EPRE is 0 dB.

A UE may assume the ratio of NPDSCH EPRE to NRS EPRE among NPDSCH REs (not applicable to NPDSCH REs with zero EPRE) is 0 dB for an NB-IoT cell with one NRS antenna port and -3 dB for an NB-IoT cell with two NRS antenna ports if higher layer parameter nrs-PowerRatio is not configured.

If a UE is configured with the higher layer parameter nrs-PowerRatio in npdsch-16QAM-Config or pur-DL-16QAM-Config,

-the ratio of NPDSCH EPRE to NRS EPRE among NPDSCH REs in symbols with NRS is given by  for a cell with one NRS antenna port and  for a cell with two NRS antenna ports, where  is given by the parameter nrs-PowerRatio.15×(6ρ-1)14×(6ρ-1)ρ

-if higher layer parameter operationModeInfo indicates '10' or '11',

-the ratio of NPDSCH EPRE to NRS EPRE among NPDSCH REs (not applicable to NPDSCH REs with zero EPRE) is given by the parameter nrs-PowerRatio in symbols without NRS

-otherwise,

-the ratio of NPDSCH EPRE to NRS EPRE among NPDSCH REs (not applicable to NPDSCH REs with zero EPRE) is given by the parameter nrs-PowerRatio in symbols without NRS and CRS, and

-the ratio of NPDSCH EPRE to NRS EPRE among NPDSCH REs (not applicable to NPDSCH REs with zero EPRE) is given by the parameter nrs-PowerRatioWithCRS in symbols with CRS.

A UE may assume the ratio of NPBCH EPRE to NRS EPRE among NPBCH REs (not applicable to NPBCH REs with zero EPRE) is 0 dB for an NB-IoT cell with one NRS antenna port and -3 dB for an NB-IoT cell with two NRS antenna ports.

A UE may assume the ratio of NPDCCH EPRE to NRS EPRE among NPDCCH REs (not applicable to NPDCCH REs with zero EPRE) is 0 dB for an NB-IoT cell with one NRS antenna port and -3 dB for an NB-IoT cell with two NRS antenna ports.

If higher layer parameter operationModeInfo indicates '00' or samePCI-Indicator indicates 'samePCI' for a cell, the ratio of NRS EPRE to CRS EPRE is given by the parameter nrs-CRS-PowerOffset if the parameter nrs-CRS-PowerOffset is provided by higher layers, and the ratio of NRS EPRE to CRS EPRE may be assumed to be 0 dB if the parameter nrs-CRS-PowerOffset is not provided by higher layers. If nrs-CRS-PowerOffset is provided by higher layers and is a non-integer value, the value of nrs-Power is 0.23 dBm higher than indicated.

## 16.3Random access procedure

Prior to initiation of the non-synchronized physical random access procedure, Layer 1 shall receive the following information from the higher layers:

-Narrowband Random access channel parameters (NPRACH configuration)

## 16.3.1Physical non-synchronized random access procedure

From the physical layer perspective, the L1 random access procedure encompasses the transmission of narrowband random access preamble and narrowband random access response. The remaining messages are scheduled for transmission by the higher layer on the shared data channel and are not considered part of the L1 random access procedure. A random access channel occupies one subcarrier per set of consecutive symbols reserved for narrowband random access preamble transmissions.

The following steps are required for the L1 random access procedure:

-Layer 1 procedure is triggered upon request of a narrowband preamble transmission by higher layers.

-A target narrowband preamble received power (NARROWBAND_PREAMBLE_RECEIVED_TARGET_POWER), a corresponding RA-RNTI and a NPRACH resource are indicated by higher layers as part of the request.

-If enhanced random access power control is not applied, for the lowest configured repetition level; and if enhanced random access power control is applied then for all configured repetition levels, a narrowband preamble transmission power PNPRACH is determined as PNPRACH = min{, NARROWBAND_PREAMBLE_RECEIVED_TARGET_POWER +  }_[dBm], where  is the configured UE transmit power for narrowband IoT transmission defined in [6] for subframe i of serving cell  and  is the downlink path loss estimate calculated in the UE for serving cell . If enhanced random access power control is not applied, for a repetition level other than the lowest configured repetition level, PNPRACH is set to .

-The narrowband preamble is transmitted with transmission power PNPRACH commencing on the indicated NPRACH resource. The narrowband preamble is transmitted for the number of NPRACH repetitions for the associated NPRACH repetition level as indicated by higher layers.

Detection of a NPDCCH with DCI scrambled by RA-RNTI is attempted during a window controlled by higher layers (see [8], Clause 5.1.4). If detected, the corresponding DL-SCH transport block is passed to higher layers. The higher layers parse the transport block and indicate the Nr-bit uplink grant to the physical layer, which is processed according to Clause 16.3.3

## 16.3.2Timing

For the L1 random access procedure, UE's uplink transmission timing after a random access preamble transmission is as follows.

a)If a NPDCCH with associated RA-RNTI is detected and the corresponding DL-SCH transport block ending in subframe n contains a response to the transmitted preamble sequence, the UE shall, according to the information in the response, transmit an UL-SCH transport block according to Clause 16.3.3.

b)If a random access response is received and the corresponding DL-SCH transport block ending in subframe n does not contain a response to the transmitted preamble sequence, the UE shall, if requested by higher layers, be ready to transmit a new preamble sequence no later than the NB-IoT UL slot starting 12 milliseconds after the end of subframe n.

c)If no NPDCCH scheduling random access response is received in subframe n, where subframe n is the last subframe of the random access response window, the UE shall, if requested by higher layers, be ready to transmit a new preamble sequence no later than the NB-IoT UL slot starting 12 milliseconds after the end of subframe n.

d)If an NPDCCH scheduling random access response with associated RA-RNTI is detected and the corresponding DL-SCH transport block reception ending in subframe n cannot be successfully decoded, the UE shall, if requested by higher layers, be ready to transmit a new preamble sequence no later than the NB-IoT UL slot starting 12 milliseconds after the end of subframe n.

In case a random access procedure is initiated by a "PDCCH order" ending in subframe n, the UE shall, if requested by higher layers, start transmission of random access preamble at the end of the first subframe , , where a NPRACH resource is available. n+k2+Kcell_offset

The "PDCCH order" in DCI format N1 indicates to the UE,

-allocated subcarrier for NPRACH, where  is the subcarrier indication field in the corresponding DCI, is reserved for preamble format 0/1, is reserved for preamble format 2 if nprach-ParametersListFmt2 is configured and the UE indicates the nprach-Format2 capability and Preamble format indicator is set to 1.

-a repetition number () for NPRACH determined by the repetition number field () in the corresponding DCI according to Table 16.3.2-1 where R1, R2 (if any) and R3 (if any) are given by the higher layer parameter numRepetitionsPerPreambleAttempt for each NPRACH resource, respectively. R1 < R2 <R3.

Table 16.3.2-1: Number of repetitions () for NPRACH following a "PDCCH order"

The UE shall transmit random access preamble on the NB-IoT carrier indicated by "Carrier indication of NPRACH" field, if the field is present in the "PDCCH order". If the value of "Carrier indication of NPRACH" is non-zero, it indicates a NPRACH carrier derived from SystemInformationBlockType22-NB [11] for which the index in the list is equal to the carrier indication. If the value of "Carrier indication of NPRACH" is zero, the uplink carrier used for NPRACH is derived from SystemInformationBlockType2-NB [11].

If nprach-ParametersListFmt2 is configured and the UE indicates the nprach-Format2 capability, the UE shall transmit the preamble format indicated by "Preamble format indicator" field, otherwise the UE shall transmit preamble format 0/1.

## 16.3.3Narrowband random access response grant

The higher layers indicate the Nr-bit UL Grant to the physical layer, as defined in 3GPP TS 36.321 [8]. This is referred to as the Narrowband Random Access Response Grant in the physical layer.

Nr-bit =15, and the content of these 15 bits starting with the MSB and ending with the LSB are as follows:

-Uplink subcarrier spacing  is '0'=3.75 kHz or '1'=15 kHz – 1 bit

-Subcarrier indication field  as determined in Clause 16.5.1.1 – 6 bits

-Scheduling delay field () as determined in Clause 16.5.1 with k0 = 12 for IDelay = 0 , where NB-IoT DL subframe n is the last subframe in which the NPDSCH associated with the Narrowband Random Access Response Grant is transmitted – 2 bits

-Msg3 repetition number  as determined in Clause 16.5.1.1 – 3 bits

-MCS index indicating TBS, modulation, and number of RUs for Msg3 – 3 bits

The redundancy version for the first transmission of Msg3 is 0.

If the UE is not using higher layer parameter edt-Parameters, or the UE is using higher layer parameter edt-parameters and ,

-the TBS, modulation, and number of RUs for Msg3 are determined according to Table 16.3.3-1

otherwise,

-if the UE is configured with higher layer parameter edt-SmallTBS-Enabled set to 'false',

-the TBS is given by higher layer parameter edt-TBS

-otherwise,

the UE selects a TBS from the allowed TBS values according to Table 16.3.3-2

the repetition number for Msg3 is the smallest integer multiple of L value that is equal to or larger than where  is the selected TBS for Msg3, and  is given by higher layer parameter edt-TBS

-if  and  and , then is used in clause 16.5.1.2, otherwise is used

-the number of RUs for Msg3 are determined according to Table 16.3.3-3

π/4 QPSK modulation is used for  and for  with ; QPSK modulation is used for with

Table 16.3.3-1: MCS index for Msg3 NPUSCH

Table 16.3.3-2: EDT TBS for Msg3 NPUSCH with edt-SmallTBS-Enabled set to 'true'

Table 16.3.3-3: MCS index for Msg3 NPUSCH and EDT

## 16.4Narrowband physical downlink shared channel related procedures

A NB-IoT UE shall determine whether a downlink subframe or a TDD special subframe configured for NB-IoT DL transmission is a NB-IoT DL subframe as follows

-If the UE determines that the subframe contains NPSS/NSSS/NPBCH/ SystemInformationBlockType1-NB transmission, then the subframe is not assumed as a NB-IoT subframe.

-Else if the UE is in a IoT NTN TDD serving cell and the UE determines the subframe is not one of the D consecutive downlink subframes according to the frame structure type 1 for IoT NTN TDD and the value of D defined in [3], then the subframe is not assumed as a NB-IoT DL subframe.

-Else if higher layer parameter resourceReservationConfigDL is configured

-for NPDSCH transmission associated with C-RNTI using UE-specific NPDCCH search space

-if the Resource reservation field in the DCI is set to 0, then the subframe is assumed as a NB-IoT DL subframe

-else if the Resource reservation field in the DCI is set to 1, then the subframe is assumed as a NB-IoT DL subframe if it is not fully reserved according to the higher layer parameters (a subframe is considered fully reserved if and only if all OFDM symbols are reserved in the subframe).

-for NPDCCH transmission associated with C-RNTI or SPS C-RNTI using UE-specific NPDCCH search space

-the subframe is assumed as a NB-IoT DL subframe if it is not fully reserved according to the higher layer parameters (a subframe is considered fully reserved if and only if all OFDM symbols are reserved in the subframe).

-In all other cases, a NB-IoT UE shall assume a subframe as a NB-IoT DL subframe if

-for a NB-IoT carrier that a UE receives higher layer parameter operationModeInfo, the subframe is configured as NB-IoT DL subframe or the subframe is a TDD special subframe configured for NB-IoT DL transmission after the UE has obtained SystemInformationBlockType1-NB.

-the subframe is configured as NB-IoT DL subframe by the higher layer parameter downlinkBitmapNonAnchor.

-except when the UE is configured with higher layer parameter additionalTxSIB1-Config set to TRUE, subframe #3 not containing additional SystemInformationBlockType1-NB transmission is assumed as a NB-IoT DL subframe if the UE monitors a NPDCCH UE-specific search space or decodes NPDSCH transmission scheduled by NPDCCH in the UE-specific search space.

For a NB-IoT UE that supports twoHARQ-Processes-r14 or the UE is configured with higher layer parameter npdsch-MultiTB-Config, there shall be a maximum of 2 downlink HARQ processes.

## 16.4.1UE procedure for receiving the narrowband physical downlink shared channel

A UE shall upon detection on a given serving cell of a NPDCCH with DCI format N1, N2 ending in subframe n intended for the UE, decode, starting in

-n+5 DL subframe for FDD or IoT NTN TDD,

-n+5 subframe for TN TDD,

the corresponding NPDSCH transmission in N consecutive NB-IoT DL subframe(s) ni with i = 0, 1, …, N-1 according to the NPDCCH information, where

-subframe n is the last subframe in which the NPDCCH is transmitted and is determined from the starting subframe of NPDCCH transmission and the DCI subframe repetition number field in the corresponding DCI;

-subframe(s) ni with i=0,1,…,N-1 are N consecutive NB-IoT DL subframe(s) excluding subframes used for SI messages or scheduling gap (if any) or processing gap (if any) where, n0<n1<…,nN-1 ,

-, where the value of  is determined as specified in Clause 16.4.1.3, the value of is determined by the resource assignment field in the corresponding DCI (see Clause 16.4.1.3), and the value of is determined by the Number of scheduled TB for Unicast field or Number of scheduled TB for SC-MTCH field, if present, in the corresponding DCI,  otherwise,

-k0 is the number of NB-IoT DL subframe(s) starting in DL subframe n+5 for FDD or IoT NTN TDD or subframe n+5 for TN TDD, until DL subframe n0, where k0 is determined by the scheduling delay field () for DCI format N1, and k0 = 0 for DCI format N2. For DCI CRC scrambled by G-RNTI, k0 is determined by the scheduling delay field () according to Table 16.4.1-1a, otherwise k0 is determined by the scheduling delay field () according to Table 16.4.1-1. The value of is according to Clause 16.6 for the corresponding DCI format N1,

-for ,

-if the UE is configured with higher layer parameter multiTB-Config in npdsch-MultiTB-Config set to 'interleaved', and NPDSCH corresponding to a NPDCCH with DCI CRC scrambled by C-RNTI, and

-NB-IoT DL subframes  with  are associated with TBr+1 ,

-otherwise,

-NB-IoT DL subframes  with  are associated with TBr+1 ,

-for  and NPDSCH corresponding to an NPDCCH with DCI CRC scrambled by G-RNTI,

-if multiTB-Gap is not configured and , a processing gap of 20ms is inserted after every 2 TBs

-otherwise, a scheduling gap with a length equal to the indicated value of multiTB-Gap is inserted between TBr and TBr+1, .

-If the scheduling gap or the processing gap overlaps with the NPDSCH transmission gap defined in [3], the overlapped part of the scheduling gap or processing gap is also counted as the part of NPDSCH transmission gap.

Table 16.4.1-1: for DCI format N1.

Table 16.4.1-1a: for DCI format N1 with DCI CRC scrambled by G-RNTI.

If a UE is configured with higher layer parameter twoHARQ-ProcessesConfig

-for FDD, the UE is not expected to receive transmissions in the Type B half duplex guard periods as specified in [3]

otherwise

-for FDD, the UE is not expected to receive transmissions in 3 DL subframes following the end of a NPUSCH transmission by the UE.

-for TDD, the UE is not expected to receive transmissions in 3 subframes following the end of a NPUSCH transmission by the UE.

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the P-RNTI, the UE shall decode the NPDCCH and the corresponding NPDSCH according to any of the combinations defined in Table 16.4.1-2. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by P-RNTI.

Table 16.4.1-2: NPDCCH and NPDSCH configured by P-RNTI

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the RA-RNTI, the UE shall decode the NPDCCH and the corresponding NPDSCH according to any of the combinations defined in Table 16.4.1-3. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by RA-RNTI.

Table 16.4.1-3: NPDCCH and NPDSCH configured by RA-RNTI

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the C-RNTI except during random access procedure, the UE shall decode the NPDCCH and the corresponding NPDSCH according to any of the combinations defined in Table 16.4.1-4. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by C-RNTI.

Table 16.4.1-4: NPDCCH and NPDSCH configured by C-RNTI

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the Temporary C-RNTI and is not configured to decode NPDCCH with CRC scrambled by the C-RNTI during random access procedure, the UE shall decode the NPDCCH and the corresponding NPDSCH according to the combination defined in Table 16.4.1-5. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by Temporary C-RNTI.

If a UE is also configured by higher layers to decode NPDCCH with CRC scrambled by the C-RNTI during random access procedure, the UE shall decode the NPDCCH and the corresponding NPDSCH according to the combination defined in Table 16.4.1-5. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by C-RNTI.

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the CB-RNTI during the CB-Msg3-EDT procedure, the UE shall decode the NPDCCH and the corresponding NPDSCH according to the combination defined in Table 16.4.1-5. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by CB-RNTI.

Table 16.4.1-5: NPDCCH and NPDSCH configured by Temporary C-RNTI and/or C-RNTI during random access procedure, or CB-RNTI during CB-Msg3-EDT procedure

For NPDSCH carrying SystemInformationBlockType1-NB and SI-messages, the UE shall decode NPDSCH according to the transmission scheme defined in Table 16.4.1-6. The scrambling initialization of NPDSCH is by SI-RNTI.

Table 16.4.1-6: NPDSCH configured by SI-RNTI

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the SC-RNTI, the UE shall decode the NPDCCH and the corresponding NPDSCH according to any of the combinations defined in Table 16.4.1-7. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by SC-RNTI.

Table 16.4.1-7: NPDCCH and NPDSCH configured by SC-RNTI

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the G-RNTI, the UE shall decode the NPDCCH and the corresponding NPDSCH according to any of the combinations defined in Table 16.4.1-8. The scrambling initialization of NPDSCH corresponding to these NPDCCHs is by G-RNTI.

Table 16.4.1-8: NPDCCH and NPDSCH configured by G-RNTI

If a UE is configured by higher layers to decode NPDCCH with CRC scrambled by the PUR-RNTI, the UE shall decode the NPDCCH and the corresponding NPDSCH according to any of the combination defined in Table 16.4.1-9. The scrambling initialization of the NPDSCH corresponding to these NPDCCHs is by PUR-RNTI.

Table 16.4.1-9: NPDCCH and NPDSCH configured by PUR-RNTI

A UE is not required to receive NPDSCH assigned by NPDCCH with DCI CRC scrambled by G-RNTI in subframes in which the UE monitors a Type1A-NPDCCH common search space or in subframes in which the UE receives NPDSCH assigned by NPDCCH with DCI CRC scrambled by SC-RNTI

A UE is not required to receive NPDSCH assigned by NPDCCH with DCI CRC scrambled by SC-RNTI or G-RNTI in subframes in which the UE monitors a Type1-NPDCCH common search space or in subframes in which the UE receives NPDSCH assigned by NPDCCH with DCI CRC scrambled by P-RNTI

A UE is not required to receive NPDSCH assigned by NPDCCH with DCI CRC scrambled by SC-RNTI or G-RNTI in subframes in which the UE monitors a Type2-NPDCCH common search space or in subframes in which the UE receives NPDSCH assigned by NPDCCH with DCI CRC scrambled by C-RNTI, CB-RNTI, or Temporary C-RNTI.

The transmission schemes for NPDSCH are defined in the following Clauses.

## 16.4.1.1Single-antenna port scheme

For the single-antenna port transmission schemes (port 2000) of the NPDSCH, the UE may assume that an eNB transmission on the NPDSCH would be performed according to Clause 6.3.4.1 of [3].

## 16.4.1.2Transmit diversity scheme

For the transmit diversity transmission scheme of the NPDSCH, the UE may assume that an eNB transmission on the NPDSCH would be performed according to Clause 6.3.4.3 of [3]

## 16.4.1.3Resource allocation

The resource allocation information in DCI format N1, N2 (paging) for NPDSCH indicates to a scheduled UE

-a number of subframes () determined by the resource assignment field () in the corresponding DCI according to Table 16.4.1.3-1.

-a repetition number () determined by the repetition number field () in the corresponding DCI according to Table 16.4.1.3-2, except for NPDSCH with 16QAM where . NRep=1

Table 16.4.1.3-1: Number of subframes () for NPDSCH.

Table 16.4.1.3-2: Number of repetitions () for NPDSCH.

For FDD or IoT NTN TDD, the number of repetitions for the NPDSCH carrying SystemInformationBlockType1-NB is determined based on the parameter schedulingInfoSIB1 configured by higher-layers and according to Table 16.4.1.3-3.

Table 16.4.1.3-3: Number of repetitions for NPDSCH carrying SystemInformationBlockType1-NB, FDD or IoT NTN TDD.

For FDD or IoT NTN TDD, the starting radio frame for the first transmission of the NPDSCH carrying SystemInformationBlockType1-NB is determined according to Table 16.4.1.3-4.

Table 16.4.1.3-4: Starting radio frame for the first transmission of the NPDSCH carrying SystemInformationBlockType1-NB, FDD or IoT NTN TDD.

For the TN TDD NB-IoT carrier on which NPSS/NSSS/NPBCH are detected, the number of repetitions and subframe index for the NPDSCH carrying SystemInformationBlockType1-NB is determined based on the parameter schedulingInfoSIB1 configured by higher-layers and according to Table 16.4.1.3-5.

Table 16.4.1.3-5: Number of repetitions and subframe index for NPDSCH carrying SystemInformationBlockType1-NB, TN TDD.

For the TN TDD NB-IoT carrier on which NPSS/NSSS/NPBCH are detected, the starting radio frame for the first transmission of the NPDSCH carrying SystemInformationBlockType1-NB is determined according to Table 16.4.1.3-6.

Table 16.4.1.3-6: Starting radio frame for the first transmission of the NPDSCH carrying SystemInformationBlockType1-NB, TN TDD.

For a higher layer configured TN TDD NB-IoT carrier, the number of repetitions and subframe index for the NPDSCH carrying SystemInformationBlockType1-NB is determined based on the parameter schedulingInfoSIB1 configured by higher-layers and according to Table 16.4.1.3-7.

Table 16.4.1.3-7: Number of repetitions and subframe index for NPDSCH carrying SystemInformationBlockType1-NB, TN TDD.

For a higher layer configured TN TDD NB-IoT carrier, the starting radio frame for the first transmission of the NPDSCH carrying SystemInformationBlockType1-NB is determined according to Table 16.4.1.3-8.

Table 16.4.1.3-8: Starting radio frame for the first transmission of the NPDSCH carrying SystemInformationBlockType1-NB, TN TDD.

## 16.4.1.4NPDSCH starting position

The starting OFDM symbol for NPDSCH is given by index  in the first slot in a subframe  and is determined as follows

-if subframe  is a subframe used for receiving SIB1-NB

-if the value of the higher layer parameter operationModeInfo is set to '00' or '01'

- if the value of the higher layer parameter operationModeInfo is set to '10' and the value of the higher layer parameter sib-GuardbandInfo is set to '10' or '11' for TN TDD

-otherwise

-elseif subframe  is a special subframe for NPDSCH without repetition

- where is given by the higher layer parameter eutraControlRegionSize if the value of the higher layer parameter eutraControlRegionSize is present

-otherwise

-else

-is given by the higher layer parameter eutraControlRegionSize if the value of the higher layer parameter eutraControlRegionSize is present

-otherwise

## 16.4.1.5Modulation order and transport block size determination

To determine the modulation order in the NPDSCH, the UE shall

-if the UE is configured with higher layer parameter npdsch-16QAM-Config and the DCI is mapped onto the UE specific search space given by C-RNTI, or the UE is configured with higher layer parameter pur-DL-16QAM-Config and the DCI is mapped onto the UE specific search space given by PUR-RNTI,

-If the 4-bit "modulation and coding scheme" field () in the DCI is set to ‘1111’,

-use modulation order, = 4

-otherwise

-use modulation order, = 2

-otherwise

-use modulation order, = 2.

To determine the transport block size in the NPDSCH, the UE shall first,

-if NPDSCH carries SystemInformationBlockType1-NB

-set  to the value of the parameter schedulingInfoSIB1 configured by higher-layers

-else if NPDSCH with 16QAM

-read the 4-bit "modulation and coding scheme for 16QAM" () in the DCIIMCS'

-If for the carrier on which NPSS/NSSS/NPBCH are detected the value of the higher layer parameter operationModeInfo is set to '00' or '01', or if the value of the higher layer parameter inbandCarrierInfo-r13 is configured for a higher layer configured carrier if any, set , otherwise set ITBS=IMCS'+11ITBS=IMCS'+14

-otherwise

-read the 4-bit "modulation and coding scheme" field () in the DCI and set .

and second,

-if NPDSCH carries SystemInformationBlockType1-NB

-use Clause 16.4.1.5.2 for determining its transport block size.

-otherwise,

-read the 3-bit "resource assignment" field () in the DCI and determine its TBS by the procedure in Clause 16.4.1.5.1.

For a NPDCCH UE-specific search space, if the UE is configured with higher layer parameter twoHARQ-ProcessesConfig, or the UE is configured with higher layer parameter npdsch-MultiTB-Config and single TB is scheduled in the corresponding DCI

-the NDI and HARQ process ID as signalled on NPDCCH, and the TBS, as determined above, shall be delivered to higher layers,

otherwise

-the NDI as signalled on NPDCCH, and the TBS, as determined above, shall be delivered to higher layers. If the UE is configured with higher layer parameter npdsch-MultiTB-Config and multiple TB are scheduled in the corresponding DCI, the HARQ process ID of 0 is for the first TB and HARQ process ID of 1 shall be assumed for the second TB, otherwise, HARQ process ID of 0 shall be assumed.

## 16.4.1.5.1Transport blocks not mapped for SystemInformationBlockType1-NB

The TBS is given by the (,) entry of Table 16.4.1.5.1-1.

If for the carrier on which NPSS/NSSS/NPBCH are detected the value of the higher layer parameter operationModeInfo is set to '00' or '01', or if the value of the higher layer parameter inbandCarrierInfo-r13 is configured for a higher layer configured carrier if any,

-if NPDSCH with 16QAM , otherwise ;11≤ITBS≤17

otherwise,

-if NPDSCH with 16QAM , otherwise .14≤ITBS≤210≤ITBS≤13

Table 16.4.1.5.1-1: Transport block size (TBS) table.

## 16.4.1.5.2Transport blocks mapped for SystemInformationBlockType1-NB

The TBS is given by theentry of Table 16.4.1.5.2-1 for FDD or IoT NTN TDD, and Table 16.4.1.5.2-2 for TN TDD NB-IoT carrier on which NPSS/NSSS/NPBCH are detected and Table 16.4.1.5.2-3 for a higher layer configured TN TDD NB-IoT carrier.

Table 16.4.1.5.2-1: Transport block size (TBS) table for NPDSCH carrying SystemInformationBlockType1-NB, FDD or IoT NTN TDD

Table 16.4.1.5.2-2: Transport block size (TBS) table for NPDSCH carrying SystemInformationBlockType1-NB, TN TDD

Table 16.4.1.5.2-3: Transport block size (TBS) table for NPDSCH carrying SystemInformationBlockType1-NB, TN TDD

## 16.4.2UE procedure for reporting ACK/NACK

The UE shall upon detection of a NPDSCH transmission ending in NB-IoT subframe n intended for the UE and for which an ACK/NACK shall be provided, start, after the end of

- DL subframe for FDD or IoT NTN TDD,

- NB-IoT UL subframes following the end of n+12 subframe for TN TDD,

transmission of the NPUSCH carrying ACK/NACK response, and SR (if any) if the serving cell is FDD or IoT NTN TDD and the UE is configured with higher layer parameter sr-with-HARQ-ACK-Config, using NPUSCH format 2 in N consecutive NB-IoT UL slots, where

-, where

-the value of is given by the higher layer parameter ack-NACK-NumRepetitions-Msg4 configured for the associated NPRACH resource for Msg4 NPDSCH transmission, and higher layer parameter ack-NACK-NumRepetitions otherwise,

-the value of  is the number of slots of the resource unit (defined in clause 10.1.2.3 of [3]), and

-if the UE is configured with higher layer parameter harq-ACK-Bundling in npdsch-MultiTB-Config, or if the UE is in a NTN serving cell and multiple TB are scheduled in the NPDCCH corresponding to the NPDSCH and the UE is not configured with higher layer parameter downlinkHARQ-FeedbackDisabledDCI-NB and configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap-NB indicating disabled HARQ-ACK information for a HARQ process associated with a transport block in the NPDSCH, then , otherwise , where the value of is determined by the Number of scheduled TB for Unicast field if present in the NPDCCH corresponding to the NPDSCH, otherwise ,

-allocated subcarrier for ACK/NACK and value of k0 is determined by the ACK/NACK resource field in the DCI format of the corresponding NPDCCH or the HARQ ACK resource field in the MAC CMR of CB-Msg4 [8] according to Table 16.4.2-1, and Table 16.4.2-2,

-for FDD or IoT NTN TDD, .

-for TN TDD, .

-For

-if the UE is configured with higher layer parameter harq-AckBundling in npdsch-MultiTB-Config, and the NPDSCH corresponding to a NPDCCH with DCI CRC scrambled by C-RNTI,

-if the UE is in a NTN serving cell and if the UE is not configured with higher layer parameter downlinkHARQ-FeedbackDisabledDCI-NB and configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap-NB indicating disabled HARQ-ACK information for a HARQ process associated with a transport block in the NPDSCH, the UE shall generate an ACK for HARQ-ACK corresponding to the transport block

-the ACK/NACK response is generated by performing a logical AND operation of HARQ-ACKs corresponding to the TBr+1 ,

-otherwise,

-if

-the ACK/NACK response is the HARQ-ACK corresponding to the transport block associated with the HARQ process with enabled HARQ-ACK information

-otherwise

-NB-IoT UL slots  with  of the NPUSCH carry ACK/NACK response for TBr+1 ,

except if the UE is in a NTN serving cell, and the UE is not configured with higher layer parameter downlinkHARQ-FeedbackDisabledDCI-NB and configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap-NB indicating disabled HARQ-ACK information for all HARQ process(es) associated with transport block(s) in the NPDSCH, or the HARQ-ACK Resource field functions as HARQ feedback disabled indicator in DCI format N1 as specified in [4] in the NPDCCH corresponding to the NPDSCH.

Table 16.4.2-1: ACK/NACK subcarrier and for NPUSCH with subcarrier spacing .

Table 16.4.2-2: ACK/NACK subcarrier and for NPUSCH with subcarrier spacing .

## 16.5Narrowband physical uplink shared channel related procedures

For a NB-IoT UE that supports twoHARQ-Processes-r14 or the UE is configured with higher layer parameter npusch-MultiTB-Config, there shall be a maximum of 2 uplink HARQ processes.

For a NB-IoT UE and NPUSCH transmission using preconfigured uplink resource, there shall be 1 uplink HARQ process.

A NB-IoT UE shall determine whether a subframe is a NB-IoT UL subframe as follows

-If higher layer parameter resourceReservationConfigUL is configured

-for NPUSCH format 1 transmission associated with C-RNTI or SPS C-RNTI using UE-specific NPDCCH search space including NPUSCH format 1 transmission without a corresponding NPDCCH

-if the Resource reservation field in the DCI is set to 0, then the subframe is assumed as a NB-IoT UL subframe

-else if the Resource reservation field in the DCI is set to 1, then the subframe is assumed as a NB-IoT UL subframe if it is not fully reserved according to the higher layer parameters (a subframe is considered fully reserved if and only if all SC-FDMA symbols are reserved in the subframe).

-for NPUSCH format 2 transmission

-the subframe is assumed as a NB-IoT UL subframe if it is not fully reserved according to the higher layer parameters (a subframe is considered fully reserved if and only if all SC-FDMA symbols are reserved in the subframe).

-In all other cases,

-for TN TDD, a NB-IoT UE shall assume a subframe as a NB-IoT UL subframe if, for a NB-IoT carrier, it is configured as NB-IoT UL subframe by higher layers

-for FDD, a NB-IoT UE shall always assume a subframe as a NB-IoT UL subframe

-for IoT NTN TDD, a NB-IoT UE shall assume a subframe as a NB-IoT UL subframe if it is one of the U consecutive uplink subframes according to the frame structure type 1 for IoT NTN TDD and the value of U defined in [3].

## 16.5.1UE procedure for transmitting format 1 narrowband physical uplink shared channel

NPUSCH format 1 transmission can be scheduled by a NPDCCH with DCI format N0, or the transmission can correspond to using preconfigured uplink resource configured by higher layers. Transmission using preconfigured uplink resource is initiated by higher layers as specified in [14] , while retransmission of transport blocks transmitted using preconfigured uplink resource are scheduled by a NPDCCH with DCI format N0.

A UE shall upon detection on a given serving cell of a NPDCCH with DCI format N0 ending in NB-IoT DL subframe n scheduling NPUSCH intended for the UE, perform, at the end of

-n+k0+Koffset DL subframe for FDD or IoT NTN TDD,

-k0 NB-IoT UL subframes following the end of n+8 subframe for TN TDD,

a corresponding NPUSCH transmission using NPUSCH format 1 in N consecutive NB-IoT UL slots ni with i = 0, 1, …, N-1 according to the NPDCCH information where

-subframe n is the last subframe in which the NPDCCH is transmitted and is determined from the starting subframe of NPDCCH transmission and the DCI subframe repetition number field in the corresponding DCI; and

-, where the value of  is determined as specified in Clause 16.5.1.1, the value of is determined by the resource assignment field in the corresponding DCI (see Clause 16.5.1.1), the value of  is the number of NB-IoT UL slots of the resource unit (defined in clause 10.1.2.3 of [3]) corresponding to the  allocated number of subcarriers (as determined in Clause 16.5.1.1) in the corresponding DCI, and the value of is determined by the Number of scheduled TB for Unicast field, if present, in the corresponding DCI,  otherwise

-for FDD or IoT NTN TDD,

-if NPUSCH transmission with subcarrier spacing and the UE configured with higher layer parameter npusch-OCC-Enabled and  and OCC enabled in the corresponding DCI,NRep>1

-n0 is the first NB-IoT UL slot, , starting after the end of subframe n+k0+Koffset that fulfills ns(5nf+ns) mod 4=0

-otherwise,

-n0 is the first NB-IoT UL slot starting after the end of subframe n+k0+Koffset

-for TN TDD, n0 is the first NB-IoT UL slot starting after k0 NB-IoT UL subframes following the end of n+8 subframe

-value of k0 is determined by the scheduling delay field () in the corresponding DCI according to Table 16.5.1-1 for FDD or IoT NTN TDD and Table 16.5.1-1A for TN TDD

-For ,

-if the UE is configured with higher layer parameter npusch-MultiTB-Config set to 'interleaved', and NPUSCH corresponding to a NPDCCH with DCI CRC scrambled by C-RNTI, and  where  for ,  otherwise.

-NB-IoT UL slots  with  are associated with TBr+1 , .  if  and the UE is configured with higher layer parameter npusch-OCC-Enabled and  and OCC enabled in the corresponding DCI,  otherwise.l=0,1,…g-1,  c=0,1,…NRep/(CMOCC)-1, g=CMOCCNRUNslotsULMOCC=2NscRU=1NRep>1MOCC=1

-otherwise,

-NB-IoT UL slots  with  are associated with TBr+1 ,

Table 16.5.1-1: for DCI format N0 for FDD or IoT NTN TDD.

Table 16.5.1-1A: for DCI format N0 for TN TDD.

If a NPUSCH transmission without a corresponding NPDCCH collides partially or fully with a NPDSCH transmission, the NPUSCH transmission is dropped.

If a UE is configured by higher layers to decode NPDCCHs with the CRC scrambled by the C-RNTI, the UE shall decode the NPDCCH according to the combination defined in Table 16.5.1-2 and transmit a corresponding NPUSCH. The scrambling initialization of this NPUSCH corresponding to these NPDCCHs and the NPUSCH retransmission for the same transport block is by C-RNTI.

Table 16.5.1-2: NPDCCH and NPUSCH configured by C-RNTI

If a UE is configured to receive random access procedures initiated by "PDCCH orders", the UE shall decode the NPDCCH according to the combination defined in Table 16.5.1-3.

Table 16.5.1-3: NPDCCH configured as "PDCCH order" to initiate random access procedure

If a UE is configured by higher layers to decode NPDCCHs with the CRC scrambled by the Temporary C-RNTI regardless of whether UE is configured or not configured to decode NPDCCH with the CRC scrambled by the C-RNTI during random access procedure, the UE shall decode the NPDCCH according to the combination defined in Table 16.5.1-4 and transmit the corresponding NPUSCH. The scrambling initialization of NPUSCH corresponding to these NPDCCHs is by Temporary C-RNTI.

If a Temporary C-RNTI is set by higher layers, the scrambling initialization of NPUSCH corresponding to the Narrowband Random Access Response Grant in Clause 16.3.3 and any NPUSCH retransmission(s) for the same transport block is by Temporary C-RNTI. Otherwise, the scrambling initialization of NPUSCH corresponding to the Narrowband Random Access Response Grant in Clause 16.3.3 and any NPUSCH retransmission(s) for the same transport block is by C-RNTI.

If a UE is also configured by higher layers to decode NPDCCH with CRC scrambled by the C-RNTI during random access procedure, the UE shall decode the NPDCCH according to the combination defined in Table 16.5.1-4 and transmit the corresponding NPUSCH. The scrambling initialization of NPUSCH corresponding to these NPDCCH is by C-RNTI.

The scrambling initialization of NPUSCH corresponding to the CB-Msg3 is by CB-RNTI.

Table 16.5.1-4: NPDCCH and NPUSCH configured by Temporary C-RNTI and/or C-RNTI during random access procedure

If a UE is configured by higher layers to decode NPDCCHs with the CRC scrambled by the SPS C-RNTI, the UE shall decode the NPDCCH according to the combination defined in Table 16.5.1-5 and transmit a corresponding NPUSCH if a transport block corresponding to the HARQ process of the NPUSCH transmission is generated as described in [8]. The scrambling initialization of this NPUSCH corresponding to these NPDCCHs and NPUSCH retransmission for the same transport block is by SPS C-RNTI. The scrambling initialization of initial transmission of this NPUSCH without a corresponding NPDCCH and the NPUSCH retransmission for the same transport block is by SPS C-RNTI.

Table 16.5.1-5: NPDCCH and NPUSCH configured by SPS C-RNTI

A UE may transmit NPUSCH on preconfigured uplink resources as configured by higher layers. The scrambling initialization of NPUSCH transmission using preconfigured uplink resource is by PUR-RNTI.

If a UE is configured by higher layers to decode NPDCCHs with the CRC scrambled by the PUR-RNTI, the UE shall decode the NPDCCH according to the combination defined in Table 16.5.1-6 and in case the indication in the DCI corresponds to the retransmission of a transport block transmitted using preconfigured uplink resource, transmit a corresponding NPUSCH. The scrambling initialization of this NPUSCH corresponding to these NPDCCHs and the NPUSCH retransmission for the same transport block is by PUR-RNTI.

Table 16.5.1-6: NPDCCH and NPUSCH configured by PUR-RNTI

## 16.5.1.1Resource allocation

The resource allocation information in uplink DCI format N0 for NPUSCH transmission or configured by higher layers for NPUSCH transmission using preconfigured uplink resource indicates to a scheduled UE, or configured by higher layers for CB-Msg3-EDT

-a set of contiguously allocated subcarriers () of a resource unit determined by the Subcarrier indication field, or by the Modulation and coding scheme and Subcarrier indication field, or by the higher layer parameter npusch-SubCarrierSetIndex in PUR-Config-NB, or by the higher layer parameter npusch-SubCarrierSetList in CB-Msg3-ConfigSIB-NB

-a number of resource units () determined by the resource assignment field according to Table 16.5.1.1-2, or by the higher layer parameter npusch-NumRUsIndex in PUR-Config-NB, or by the higher layer parameter npusch-NumRUsIndex in CB-Msg3-ConfigSIB-NB

-a repetition number () determined by the repetition number field according to Table 16.5.1.1-3, and for a NPUSCH transmission using preconfigured uplink resource or for a NPUSCH transmission using CB-Msg3 resource, the UE shall use the repetition number configured by higher layers; except for NPUSCH with 16QAM where NRep=1

-OCC enabled/disabled if the UE is configured with higher layer parameter npusch-OCC-Enabled and .NRep>1

The subcarrier spacing  of NPUSCH transmission is determined by

-the higher layer parameter npusch-SubCarrierSetIndex, in the case of NPUSCH transmission using preconfigured uplink resources and subsequent NPUSCH transmissions until a Narrowband Random Access Response Grant is received,

-the higher layer parameter npusch-SubCarrierSetList, in the case of NPUSCH transmission using CB-Msg3 resources and subsequent NPUSCH transmissions, or

-the uplink subcarrier spacing field in the Narrowband Random Access Response Grant according to Clause 16.3.3 otherwise.

For NPUSCH transmission with subcarrier spacing, where  is the subcarrier indication field and is reserved if the UE is not configured with higher layer parameter npusch-OCC-Enabled or the UE is configured with higher layer parameter npusch-OCC-Enabled and  or the UE is configured with higher layer parameter npusch-OCC-Enabled and  and OCC disabled, or  where  is the Modulation and coding scheme and Subcarrier indication field and  is reserved if the UE is configured with higher layer parameter npusch-OCC-Enabled and  and OCC enabled,, or nsc is configured by higher layers parameter npusch-SubCarrierSetIndex in PUR-Config-NB for NPUSCH transmissions using preconfigured uplink resources, or nsc is configured by higher layers parameter npusch-SubCarrierSetList in CB-Msg3-ConfigSIB-NB for CB-Msg3-EDT.NRep=1NRep>1nsc=Isc-MCS10Isc-MCSIsc-MCS=480,481,...,511NRep>1

For NPUSCH transmission with subcarrier spacing, the subcarrier indication field () in the DCI or npusch-SubCarrierSetIndex in PUR-Config-NB for NPUSCH transmissions using preconfigured uplink resources or npusch-SubCarrierSetList in CB-Msg3-ConfigSIB-NB for CB-Msg3-EDT determines the set of contiguously allocated subcarriers () according to

-Table 16.5.1.1-1 if the UE is not configured with higher layer parameter npusch-OCC-Enabled or the UE is configured with higher layer parameter npusch-OCC-Enabled and ,NRep=1

-Table 16.5.1.1-4 if the UE is configured with higher layer parameter npusch-OCC-Enabled and , and OCC disabled,NRep>1

-Table 16.5.1.1-5 otherwise.

Table 16.5.1.1-1: Allocated subcarriers for NPUSCH with .

Table 16.5.1.1-2: Number of resource units () for NPUSCH.

Table 16.5.1.1-3: Number of repetitions () for NPUSCH.

Table 16.5.1.1-4: Allocated subcarriers for NPUSCH with  when UE is configured with higher layer parameter npusch-OCC-Enabled and , and OCC disabled.NRep>1

Table 16.5.1.1-5: Allocated subcarriers for NPUSCH with  when UE is configured with higher layer parameter npusch-OCC-Enabled and  and OCC enabled.NRep>1

## 16.5.1.2Modulation order, redundancy version and transport block size determination

To determine the modulation order, redundancy version and transport block size for the NPUSCH, the UE shall first

-read the "modulation and coding scheme" field () in the DCI or configured by higher layers for NPUSCH transmission using preconfigured uplink resource or NPUSCH transmission using CB-Msg3-EDT, or read the "Modulation and coding scheme and Subcarrier indication" field  in the DCI and set  if the UE is configured with higher layer parameter npusch-OCC-Enabled and  and OCC enabled and , andIsc-MCSIMCS=Isc-MCS mod 10NRep>1

-read the "redundancy version" field () in the DCI, or initiate with  for NPUSCH transmission using preconfigured uplink resource or NPUSCH transmission using CB-Msg3-EDT, or when the UE is configured with higher layer parameter npusch-OCC-Enabled and  and , andrvDCI=0NRep>1

-read the "resource assignment" field () in the DCI or configured by higher layers for NPUSCH transmission using preconfigured uplink resource or configured in higher layer parameter npusch-NumRUsIndex in CB-Msg3-Config-NB for NPUSCH transmission using CB-Msg3-EDT, and

-compute the total number of allocated subcarriers (), number of resource units (), and repetition number () according to Clause 16.5.1.1.

If the UE is configured with higher layer parameter edt-Parameters and the most recent NPUSCH transmission including a transport block with EDT, the UE is not expected to receive a DCI indicating a NPUSCH retransmission as part of the contention based random access procedure with 3 ≤ IMCS ≤ 14.

If the UE is configured with higher layer parameter edt-Parameters, and for a NPUSCH retransmission of the same transport block including EDT as part of the contention based random access procedure with  in the DCI,

-the modulation order is set to .

-if the UE is configured with higher layer parameter edt-SmallTBS-Enabled set to 'true', the repetition number for the NPUSCH retransmission is the smallest integer multiple of  value that is equal to or larger than where  is the TBS corresponding to the NPUSCH transmission scheduled by the Narrowband Random Access Response Grant, and  is given by the higher layer parameter edt-TBS.

elseif the UE is configured with higher layer parameter edt-Parameters, and if the DCI indicates a retransmission as part of the contention based random access procedure with  and the most recent NPUSCH transmission including a transport block with EDT,

-the TBS and modulation are determined according to Table 16.3.3-1 in Clause 16.3.3, for  and the transport block does not include EDT

elseif the UE is configured with higher layer parameter npusch-16QAM-Config, and the DCI is mapped onto the UE specific search space and  set to ‘1111’, or for NPUSCH transmission using preconfigured uplink resource and higher layer parameter pur-UL-16QAM-Config configured, = 4

otherwise, the UE shall use modulation order, = 2 if . The UE shall useand Table 16.5.1.2-1 to determine the modulation order to use for NPUSCH if .

Table 16.5.1.2-1: Modulation and TBS index table for NPUSCH with .

If the UE is configured with higher layer parameter npusch-MultiTB-Config and multiple TB are scheduled in the corresponding DCI,  is used for each TB.

The NPUSCH associated with a TB is transmitted in N NB-IoT UL slots associated with the TB, ni , i=0,1,…,N-1. For the NPUSCH transmission in jth block of B consecutive NB-IoT UL slots associated with the TB ni ,, the redundancy version  associated with the TB is determined by, , where

-if

-if the UE is configured with higher layer parameter npusch-OCC-Enabled and  and OCC enabled is indicated in corresponding DCINRep>1

-L=2

-otherwise

-L=1

-otherwise

-.

Portion of NPUSCH codeword with  associated with a TB as defined in clause 6.3.2 in [4] mapped to slot  of allocated  resource unit(s) is transmitted in NB-IoT UL slots associated with the TB ni for and  for

The UE shall use (,) and Table 16.5.1.2-2 to determine the TBS to use for the NPUSCH. is given in Table 16.5.1.2-1 if , or  if NPUSCH with 16QAM except for NPUSCH transmission using preconfigured uplink resource in which case  is given by higher layers in PUR-Config-NB, or except for NPUSCH transmission using CB-Msg3-EDT resource in which case  is given by higher layer parameter npusch-MCS-r19 in CB-Msg3-Config-NB,  otherwise.  is the value of the "modulation and coding scheme for 16QAM" in the DCI.ITBS=IMCS'+14ITBSITBSIMCS'

-If NPUSCH with 16QAM , otherwise .14≤ITBS≤210≤ITBS≤13

Table 16.5.1.2-2: Transport block size (TBS) table for NPUSCH.

For a NPDCCH UE-specific search space, if the UE is configured with higher layer parameter twoHARQ-ProcessesConfig, or the UE is configured with higher layer parameter npusch-MultiTB-Config and single TB is scheduled in the corresponding DCI

-the NDI and HARQ process ID as signalled on NPDCCH, and the RV and TBS, as determined above, shall be delivered to higher layers,

otherwise

-the NDI as signalled on NPDCCH, and the RV and TBS, as determined above, shall be delivered to higher layers. If the UE is configured with higher layer parameter npusch-MultiTB-Config and multiple TB are scheduled in the corresponding DCI, HARQ process ID of 0 shall be assumed for the first TB and HARQ process ID of 1 shall be assumed for the second TB.

## 16.5.2UE procedure for NPUSCH retransmission

For a NPUSCH retransmission, the UE shall follow the HARQ information in DCI as specified in [8].

## 16.5.3UE procedure for transmitting SR

If the UE is configured with higher layer parameter sr-WithoutHARQ-ACK-Config, the UE is configured with Narrowband Random access channel parameters (NPRACH configuration) for SR transmission by higher layers.

The UE shall, if requested by higher layers for transmitting SR, start transmission of a narrowband random access preamble on the NB-IoT carrier configured in sr-NPRACH-Resource at the next available NPRACH resource, unless the transmission would overlap with any subframe(s) of NPDSCH reception. The narrowband preamble is transmitted on the allocated subcarrier and a number of NPRACH repetitions for the associated NPRACH repetition level as indicated by higher layers. The narrowband random access preamble is transmitted with transmission power as determined in clause 16.2.1.2, commencing on the indicated NPRACH resource.

## 16.6Narrowband physical downlink control channel related procedures

Throughout this clause, if a NB-IoT UE is configured with higher layer parameter k-Mac, Kmac = k-Mac otherwise, Kmac = 0.

A UE shall monitor a set of NPDCCH candidates (described in Clause 10.2.5.1 of [3]) as configured by higher layer signalling for control information, where monitoring implies attempting to decode each of the NPDCCHs in the set according to all the monitored DCI formats.

The set of NPDCCH candidates to monitor are defined in terms of NPDCCH search spaces.

The UE shall monitor one or more of the following search spaces

-a Type1-NPDCCH common search space,

-a Type1A-NPDCCH common search space,

-a Type2-NPDCCH common search space,

-a Type2A-NPDCCH common search space, and

-a NPDCCH UE-specific search space.

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

An NPDCCH search space  at aggregation level  ( for TDD special subframe,  otherwise), and repetition level  is defined by a set of NPDCCH candidates where each candidate is repeated in a set of consecutive NB-IoT downlink subframes excluding subframes used for transmission of SI messages starting with subframe .

For NPDCCH UE-specific search space, the aggregation and repetition levels defining the search spaces and the corresponding NPDCCH candidates are listed in Table 16.6-1 by substituting the value of with the higher layer configured parameter npdcch-NumRepetitions, except for NPDCCH candidates associated with PUR-RNTI in which case it is given by higher layer parameter npdcch-NumRepetitions in PUR-Config-NB.

For Type1-NPDCCH common search space and Type1A-NPDCCH common search space, the aggregation and repetition levels defining the search spaces are listed in Table 16.6-2 by substituting the value of

-with the higher layer configured parameter npdcch-NumRepetitionPaging for Type1-NPDCCH common search space;

-with the higher layer configured parameter npdcch-NumRepetitions-SC-MCCH for Type1A-NPDCCH common search space.

For Type2-NPDCCH common search space and Type2A-NPDCCH common search space, the aggregation and repetition levels defining the search spaces and the corresponding monitored NPDCCH candidates are listed in Table 16.6-3 by substituting the value of

-with the higher layer configured parameter npdcch-NumRepetitions-RA for Type2-NPDCCH common search space;

-with the higher layer configured parameter npdcch-NumRepetitions-SC-MTCH for Type2A-NPDCCH common search space.

The locations of starting subframe  are given by where is the th consecutive NB-IoT DL subframe from subframe , excluding subframes used for transmission of SI messages, and , and , and where

-subframe  is a subframe satisfying the condition , where , T≥4.

-for NPDCCH UE-specific search space,

-is given by the higher layer parameter npdcch-StartSF-USS, except for NPDCCH candidates associated with PUR-RNTI in which case it is given by higher layer parameter npdcch-StartSF-USS in PUR-Config-NB,

-is given by the higher layer parameter npdcch-Offset-USS, except for NPDCCH candidates associated with PUR-RNTI in which case it is given by higher layer parameter npdcch-Offset-USS in PUR-Config-NB,

-for NPDCCH Type2-NPDCCH common search space,

-is given by the higher layer parameter npdcch-StartSF-CSS-RA,

-is given by the higher layer parameter npdcch-Offset-RA,

-for NPDCCH Type2A-NPDCCH common search space,

-is given by the higher layer parameter npdcch-startSF-SC-MTCH,

-is given by the higher layer parameter npdcch-Offset-SC-MTCH,

For Type1-NPDCCH common search space,and is determined from locations of NB-IoT paging opportunity subframes.

For Type1A-NPDCCH common search space, and subframe  is a subframe satisfying the condition , where , T≥4 and

-is given by the higher layer parameter npdcch-StartSF-SC-MCCH,

-is given by the higher layer parameter npdcch-Offset-SC-MCCH.

For UE-specific search space by C-RNTI,

if the UE is configured by higher layers with a NB-IoT carrier for monitoring of NPDCCH UE-specific search space,

-the UE shall monitor the NPDCCH UE-specific search space on the higher layer configured NB-IoT carrier,

-the UE is not expected to receive NPSS, NSSS, NPBCH on the higher layer configured NB-IoT carrier.

otherwise,

-the UE shall monitor the NPDCCH UE-specific search space on the same NB-IoT carrier on which NPSS/NSSS/NPBCH are detected.

For UE-specific search space by PUR-RNTI, the UE is configured by the higher layer parameter carrierConfig in PUR-Config-NB with a NB-IoT carrier for monitoring of NPDCCH UE-specific search space,

-the UE shall monitor the NPDCCH UE-specific search space on the higher layer configured NB-IoT carrier,

-the UE is not expected to receive NPSS, NSSS, NPBCH on the higher layer configured NB-IoT carrier if the NB-IoT carrier is not the same as the NB-IoT carrier on which NPSS/NSSS/NPBCH are detected.

If the UE has initiated a NPUSCH transmission using preconfigured uplink resource ending in subframe n, the UE shall monitor the NPDCCH UE-specific search space in a search space window starting in subframe n+4+Kmac with duration given by higher layer parameter pur-ResponseWindowTimer. Upon detection of a NPDCCH with DCI format N0 with CRC scrambled by PUR-RNTI intended for the UE within the search space window and the value of "modulation and coding scheme" field () in the corresponding DCI is set to '14', the UE is not required to monitor the NPDCCH UE-specific search space for the remaining search space window duration.

Table 16.6-1: NPDCCH UE- specific search space candidates

Table 16.6-2: Type 1/Type 1A - NPDCCH common search space candidates

Table 16.6-3: Type 2/Type 2A - NPDCCH common search space candidates

For a NPDCCH UE-specific search space, if a NB-IoT UE is configured with higher layer parameter twoHARQ-ProcessesConfig or npusch-MultiTB-Config and if the NB-IoT UE detects NPDCCH with DCI Format N0 ending in subframe n, and if the corresponding NPUSCH format 1 transmission starts from n+k or in a NTN serving cell, from an uplink subframe which, after accounting for uplink transmission timing, overlaps with downlink subframe n+k,

-if the corresponding NPDCCH with DCI format N0 with CRC scrambled by C-RNTI schedules two transport blocks as determined by the Number of scheduled TB for Unicast field if present, the UE is not required to monitor an NPDCCH candidate in any subframe starting from subframe n+1 to subframe n+k-1, otherwise the UE is not required to monitor an NPDCCH candidate in any subframe starting from subframe n+k-2 to subframe n+k-1; and

the UE does not expect to receive a DCI Format N0 before subframe n+k-2 for which the corresponding NPUSCH format 1 transmission ends later than subframe n+k+255 if the corresponding NPDCCH with DCI format N0 schedules one transport block.

-for TN TDD, and if the corresponding NPUSCH format1 transmission ends in subframe n+m, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+ k to subframe n+m-1.

otherwise

-if the NB-IoT UE detects NPDCCH with DCI Format N0 ending in subframe n or receives a NPDSCH carrying a random access response grant ending in subframe n, and if the corresponding NPUSCH format 1 transmission starts from n+k or in a NTN serving cell, from an uplink subframe which, after accounting for uplink transmission timing, overlaps with downlink subframe n+k, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+k-1.

-for TN TDD, if the NB-IoT UE detects NPDCCH with DCI Format N0 ending in subframe n or receives a NPDSCH carrying a random access response grant ending in subframe n, and if the corresponding NPUSCH format 1 transmission ends in n+k, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+k.

For a NPDCCH UE-specific search space, if a NB-IoT UE is configured with higher layer parameter twoHARQ-ProcessesConfig or npdsch-MultiTB-Config

-and if the NB-IoT UE detects NPDCCH with DCI Format N1 ending in subframe n, and if a NPDSCH transmission starts from n+k,

-if the corresponding NPDCCH with DCI format N1 with CRC scrambled by C-RNTI schedules two transport blocks as determined by the Number of scheduled TB for Unicast field if present, the UE is not required to monitor an NPDCCH candidate in any subframe starting from subframe n+1 to subframe n+k-1;

-otherwise, the UE is not required to monitor an NPDCCH candidate in any subframe starting from subframe n+k-2 to subframe n+k-1;

otherwise

-if the NB-IoT UE detects NPDCCH with DCI Format N1 or N2 ending in subframe n, and if the corresponding NPDSCH transmission starts from n+k, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+k-1.

If a NB-IoT UE detects NPDCCH with DCI Format N1 ending in subframe n, and if the corresponding NPDSCH transmission starts from n+k, and

-for FDD or IoT NTN TDD, if the corresponding NPUSCH format 2 transmission starts from subframe n+m or in a NTN serving cell, from an uplink subframe which, after accounting for uplink transmission timing, overlaps with downlink subframe n+m, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+ k to subframe n+m-1.

-for TN TDD, if the corresponding NPUSCH format 2 transmission ends in subframe n+m the UE is not required to monitor NPDCCH in any subframe starting from subframe n+ k to subframe n+m-1.

If a NB-IoT UE detects NPDCCH with DCI Format N1 for "PDCCH order" ending in subframe n, and

-for FDD or IoT NTN TDD, if the corresponding NPRACH transmission starts from subframe n+k or in a NTN serving cell, from an uplink subframe which, after accounting for uplink transmission timing, overlaps with downlink subframe n+k, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+k-1.

-for TN TDD, if the corresponding NPRACH transmission ends in subframe n+k, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+k-1.

If a NB-IoT UE is configured with higher layer parameter twoHARQ-ProcessesConfig

-and if the UE has a NPUSCH transmission ending in subframe n,

-the UE is not required to receive transmissions in the Type B half-duplex guard periods as specified in [3]for FDD ; and

-the UE is not expected to receive an NPDCCH with DCI format N0/N1 for the same HARQ process ID as the NPUSCH transmission in any subframe starting from subframe n+1 to subframe n+3, or in a NTN serving cell, in any downlink subframe that overlaps with uplink subframe n+1 to subframe n+Kmac+3 except if the UE is configured with higher layer parameter uplinkHARQ-mode set to ‘HARQModeB’ for the same HARQ process ID, or if the NPUSCH transmission carries ACK/NACK response, as determined in clause 16.4.2, for the same HARQ process ID associated with a transport block scheduled in a NPDCCH scheduling a single transport block, and the UE is configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap-NB indicating disabled HARQ-ACK information for the same HARQ process ID and configured with higher layer parameter downlinkHARQ-FeedbackDisabledDCI-NB;

else if the UE is not using higher layer parameter edt-Parameters or if the UE is using higher layer parameter edt-Parameters and

-if the NB-IoT UE has a NPUSCH transmission ending in subframe n,

-the UE is not required to receive transmissions in the Type B half-duplex guard periods as specified in [3] for FDD; and

-the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+3 or in a NTN serving cell, in any downlink subframe that overlaps with uplink subframe n+1 to subframe n+Kmac+3 except if the UE is configured with higher layer parameter uplinkHARQ-mode set to ‘HARQModeB’, or if the NPUSCH transmission carries ACK/NACK response as determined in clause 16.4.2 and the UE is configured with higher layer parameter downlinkHARQ-FeedbackDisabledBitmap-NB indicating disabled HARQ-ACK information and configured with higher layer parameter downlinkHARQ-FeedbackDisabledDCI-NB.

otherwise,

-If the NB-IoT UE has a NPUSCH transmission for Msg3 ending in subframe with transport block size , whereas if would have been selected the NPUSCH transmission would have ended in subframe n, the UE is not required to monitor NPDCCH in any subframe starting from subframe n'+1 to subframe n+3 or in a NTN serving cell, in any downlink subframe that overlaps with uplink subframe n'+1 to subframe n+Kmac+3. n'

If a NB-IoT UE receives a NPDSCH transmission ending in subframe n, and if the UE is not required to transmit a corresponding NPUSCH format 2, the UE is not required to monitor NPDCCH in any subframe starting from subframe n+1 to subframe n+12.

If a NB-IoT UE is configured with higher layer parameter twoHARQ-ProcessesConfig

-the UE is not required to monitor an NPDCCH candidate of an NPDCCH search space if the candidate ends in subframe n, and if the UE is configured to monitor NPDCCH candidates of another NPDCCH search space having starting subframe k0 before subframe n+5

otherwise

-the UE is not required to monitor NPDCCH candidates of an NPDCCH search space if an NPDCCH candidate of the NPDCCH search space ends in subframe n, and if the UE is configured to monitor NPDCCH candidates of another NPDCCH search space having starting subframe k0 before subframe n+5.

An NB-IoT UE is not required to monitor NPDCCH candidates of an NPDCCH search space during an NPUSCH UL gap.

An NB-IoT UE is not required to monitor NPDCCH candidates of a Type2A-NPDCCH common search space during the scheduling gap or the processing gap.

For an NB-IoT UE configured with higher layer parameter sr-WithoutHARQ-ACK-Config, if the transmission of a narrowband random access preamble for SR ends on subframe n,

-in case of frame structure type 1 with NPRACH format 0 and 1 when the number of NPRACH repetitions is greater than or equal to 64, or NPRACH format 2 when the number of NPRACH repetitions is greater than or equal to 16, the UE is not required to monitor NPDCCH UE-specific search space from subframe n to subframe n+40 or in a NTN serving cell, in any downlink subframes that overlap with uplink subframe n to subframe n+Kmac+40,

-otherwise, the UE is not required to monitor NPDCCH UE-specific search space from subframe n to subframe n+3 or in a NTN serving cell, in any downlink subframes that overlap with uplink subframe n to subframe n+Kmac+3.

## 16.6.1NPDCCH starting position

The starting OFDM symbol for NPDCCH given by index  in the first slot in a subframe  and is determined as follows

-if higher layer parameter eutraControlRegionSize is present

-if subframe  is a special subframe for NPDCCH without repetition

- where is given by the higher layer parameter eutraControlRegionSize

-else  is given by the higher layer parameter eutraControlRegionSize

otherwise

-

## 16.6.2NPDCCH control information procedure

A UE shall discard the NPDCCH if consistent control information is not detected.

## 16.6.3NPDCCH validation for semi-persistent scheduling

A UE shall validate a Semi-Persistent Scheduling assignment NPDCCH only if all the following conditions are met:

-the CRC parity bits obtained for the NPDCCH payload are scrambled with the Semi-Persistent Scheduling C-RNTI

-the new data indicator field is set to '0'.

Validation is achieved if all the fields for the used DCI format N0 are set according to Table 16.6.3-1 or Table 16.6.3-2.

If validation is achieved, the UE shall consider the received DCI information accordingly as a valid semi-persistent activation or release.

If validation is not achieved, the received DCI format shall be considered by the UE as having been received with a non-matching CRC.

Table 16.6.3-1: Special fields for Semi-Persistent Scheduling Activation NPDCCH Validation

Table 16.6.3-2: Special fields for Semi-Persistent Scheduling Release NPDCCH Validation

## 16.6.4Preconfigured uplink resource ACK/fallback procedure

If a UE has initiated a NPUSCH transmission using preconfigured uplink resource on a given serving cell, and upon detection of a NPDCCH with DCI format N0 with CRC scrambled by PUR-RNTI intended for the UE within the PUR search space window as defined in Clause 16.6, and the value of "modulation and coding scheme" field () in the corresponding DCI set to '14', the UE shall deliver the PUR ACK/fallback indication and the NPUSCH repetition adjustment, as signaled on the NPDCCH, to the higher layers.

## 16.7Assumptions independent of physical channel related to narrowband IoT

A UE may assume the antenna ports 2000 – 2001 of a serving cell are quasi co-located (as defined in [3]) with respect to delay spread, Doppler spread, Doppler shift, average gain, and average delay.

## 16.8UE procedure for acquiring cell-specific reference signal sequence and raster offset

If the higher layer parameter operationModeInfo indicates inband-SamePCI for a cell, the UE may derive cell-specific reference signal sequence and raster offset from the higher layer parameter eutra-CRS-SequenceInfo according to Table 16.8-1, where E-UTRA PRB index  is defined as .

Table 16.8-1: Definition of eutra-CRS-SequenceInfo

## 16.9UE procedure for receiving narrowband wake up signal

A NB-IoT UE can be configured with up to two NWUS [14]. A UE may assume that no more than one NWUS sequence is transmitted per NWUS resource at a given time.

A NB-IoT UE using NWUS can assume the actual duration of NWUS is one of the values in the set listed in Table 16.9-1 corresponding to the maximum duration of NWUS, , configured by higher layers. There is a total of  NB-IoT DL subframes and subframes #4 carrying SystemInformationBlockType1-NB in the maximum duration of NWUS. The NWUS starts in subframe w0, where w0 is the latest subframe such that there is a total of  NB-IoT DL subframes and subframes #4 carrying SystemInformationBlockType1-NB in the duration that ends in subframe (g0-1), where g0 is defined by [14] and  is the NWUS resource that the UE is associated to as defined in [3]. The UE may assume that NWUS and its associated NB-IoT paging occasion subframes are on the same NB-IoT carrier.LNWUS_maxLNWUS_maxNIDresource

Table 16.9-1: Actual NWUS durations in NB-IoT DL subframes or subframes containing SystemInformationBlockType1-NB.

A NB-IoT UE using NWUS can assume there are at least 10 NB-IoT DL subframes between the end of the maximum duration of NWUS and the first associated NB-IoT paging occasion subframe.

## 16.10GNSS measurement gap related procedures

For a NB-IoT UE in a NTN serving cell, when the UE receives a GNSS Measurement Command MAC CE in a NPDSCH ending in DL subframe n,

-if the UE shall not provide HARQ-ACK information for the HARQ process associated with the transport block in the NPDSCH carrying GNSS Measurement Command MAC CE,

-the UE shall assume the start of the measurement gap in subframe n+13

-otherwise,

-the UE shall assume the start of the measurement gap in subframe k+2, where k is the first DL subframe after the end of the transmission of the NPUSCH carrying ACK/NACK response for the HARQ process associated with the transport block in the NPDSCH.

For a NB-IoT UE in a NTN serving cell, the UE is not required to monitor NPDCCH within the GNSS measurement gap duration, until it reacquires GNSS position and a contention based Random Access is performed as specified in TS 36.321 [8].

## 17Wake-up signal related procedures for BL/CE UE

A BL/CE UE can be configured with up to two MWUS [14]. A UE may assume that no more than one MWUS sequence is transmitted per MWUS resource at a given time.

A BL/CE UE using MWUS can assume the actual duration of MWUS is one of the values in the set listed in Table 17-1 corresponding to the maximum duration of MWUS, , configured by higher layers. There is a total of BL/CE DL subframes in the maximum duration of MWUS. The MWUS starts in subframe w0, where w0 is the latest subframe such that there is a total of  BL/CE DL subframes in the duration that ends in subframe (g0-1), where g0 is defined by [14],  if FDM-only MWUS resource configuration [14],  otherwise, and  is the MWUS resource that the UE is associated to as defined in [3]. The UE may assume that MWUS and its first associated paging occasion subframes are in the same narrowband. In frame structure type 2, those special subframes, indicated as BL/CE DL subframes by higher layer fdd-DownlinkOrTddSubframeBitmapBR, are not counted in maximum duration and actual duration of MWUS. LMWUS_max LMWUS_maxk∙LMWUS_maxk=1k=NIDresource+12NIDresource

Table 17-1: Actual MWUS durations in BL/CE DL subframes.

## 18GNSS measurement gap related procedures for BL/CE UE

For a BL/CE UE in a NTN FDD serving cell, when the UE receives a GNSS Measurement Command MAC CE in a PDSCH ending in DL subframe n,

-if the UE shall not provide HARQ-ACK information for the HARQ process associated with the transport block in the PDSCH carrying GNSS Measurement Command MAC CE,

-the UE shall assume the start of the measurement gap in subframe n+6

-otherwise,

-the UE shall assume the start of the measurement gap in subframe k+2, where k is the first DL subframe after the end of the HARQ-ACK transmission for the HARQ process associated with the transport block in the PDSCH.

For a BL/CE UE in a NTN FDD serving cell, the UE is not required to monitor MPDCCH within the GNSS measurement gap duration, until it reacquires GNSS position and a contention based Random Access is performed as specified in TS 36.321 [8].
