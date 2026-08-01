# TS 38.101 38101-1-j60_s07-XX

## 7Receiver characteristics

## 7.1General

Unless otherwise stated the receiver characteristics are specified at the antenna connector(s) of the UE. For UE(s) with an integral antenna only, a reference antenna(s) with a gain of 0 dBi is assumed for each antenna port(s). UE with an integral antenna(s) may be taken into account by converting these power levels into field strength requirements, assuming a 0 dBi gain antenna. For UEs with more than one receiver antenna connector, identical interfering signals shall be applied to each receiver antenna port if more than one of these is used (diversity).

The levels of the test signal applied to each of the antenna connectors shall be as defined in the respective clauses below.

The applicability of receiver requirements for Band n90 is in accordance with that for Band n41; a UE supporting Band n90 shall meet the minimum requirements for Band n41.

With the exception of clause 7.3, the requirements shall be verified with the network signalling value NS_01 configured (Table 6.2.3-1).

All the parameters in clause 7 are defined using the UL reference measurement channels specified in Annex A.2.2, the DL reference measurement channels specified in Annex A.3.2 and using the set-up specified in Annex C.3.1.

The minimum requirements specified in clauses 7.5, 7.6, 7.7 and 7.8 for NR band n48 refer to the minimum requirements for NR bands < 2.7 GHz.

For the additional requirements for intra-band non-contiguous carrier aggregation of two or more sub-blocks, an in-gap test refers to the case when the interfering signal is located at a negative offset with respect to the assigned lowest channel frequency of the highest sub-block and located at a positive offset with respect to the assigned highest channel frequency of the lowest sub-block.

For the additional requirements for intra-band non-contiguous carrier aggregation of two or more sub-blocks, an out-of-gap test refers to the case when the interfering signal(s) is (are) located at a positive offset with respect to the assigned channel frequency of the highest carrier frequency, or located at a negative offset with respect to the assigned channel frequency of the lowest carrier frequency.

For the additional requirements for intra-band non-contiguous carrier aggregation of two or more sub-blocks with channel bandwidth larger than or equal to 5 MHz, the existing adjacent channel selectivity requirements, in-band blocking requirements (for each case), and narrow band blocking requirements apply for in-gap tests only if the corresponding interferer frequency offsets with respect to the two measured carriers satisfy the following condition in relation to the sub-block gap size Wgap for at least one of these carriers j = 1,2, so that the interferer frequency position does not change the nature of the core requirement tested:

Wgap ≥ 2∙|FInterferer (offset),j|  – BWChannel(j)

where FInterferer (offset),j for a sub-block with a single component carrier is the interferer frequency offset with respect to carrier j as specified in clause 7.5, clause 7.6.2 and clause 7.6.4 for the respective requirement and BWChannel(j) the channel bandwidth of carrier j. FInterferer (offset),j for a sub-block with two or more contiguous component carriers is the interference frequency offset with respect to the carrier adjacent to the gap is specified in clause 7.5A, 7.6A.2 and 7.6A.3. The interferer frequency offsets for adjacent channel selectivity, each in-band blocking case and narrow- band blocking shall be tested separately with a single in-gap interferer at a time.

For the additional requirements for operation with shared spectrum channel access, the receiver requirements apply under the assumption that all 20 MHz sub-bands and all RB’s of each sub-band within the downlink channel are allocated with intra-cell guard bands configured to zero.

Unless otherwise stated, the receiver requirements of inter-band UL CA are applicable to UE with one Tx antenna connector in each of the two bands, or UE with one Tx antenna connector in one band and two Tx antenna connectors in the other band.

Unless otherwise stated, the receiver requirements of single carrier or CA operation are applicable to UE with one Tx antenna connector or multiple Tx antenna connectors with UL MIMO or Tx diversity operation in the UL band(s).

## 7.1AGeneral

The minimum requirements for band combinations including Band n41 also apply for the corresponding band combinations with Band n90 replacing Band n41 but with otherwise identical parameters. For brevity the said band combinations with Band n90 are not listed in the tables below but are covered by this specification.

The minium requirements specified in clauses 7.5A, 7.6A, 7.7A and 7.8A for NR band n48 refer to the minimum requirements for NR bands < 2.7 GHz.

## 7.1FGeneral

For wideband operations, the minimum requirements for the receiver characteristics are specified when zero width intra-cell guardbands are configured and with all RB set(s) within the channel scheduled and with all RB sets available for DL transmissions according to the channel access procedures in [14].

Unless stated otherwise, when a clause is not present for shared spectrum channel access, the general requirements and the additional clause requirements (suffices A,B,D) in clause 7 apply.

## 7.1G(Reserved)

## 7.1H(Reserved)

## 7.1IGeneral

For a (e)Redcap UE the requirements in Section 7 shall be verified with the channel bandwidth up to 20MHz and REFSENS specified in clause 7.3I.

## 7.1JGeneral for ATG

Unless otherwise stated, the receiver characteristics are specified at the antenna connector(s) of the ATG UE with one or multiple omni-directional antenna(s) or at the transceiver array boundary (TAB) connectors of the ATG UE with the antenna array. The definition about transceiver array boundary (TAB) is specified in clause 4.3.2 of TS 38.104 [16].

For ATG UE with multiple omni-directional antennas not indicating the capability antennaArrayType-r18, the receiver RF requirements are defined on top of each antenna connector.

For ATG UE with antenna array indicating the capability antennaArrayType-r18, the receiver RF requirements are defined on top of each TAB connector.

## 7.1K(Reserved)

## 7.1L(Reserved)

## 7.1MGeneral for LP-WUS/WUR

The minimum requirements are specified assuming only one receiver for the wake-up signal. The criterion for verifying all receiver core RF requirements shall be MDR of the LP-WUS, which shall not exceed 1% with the LP-WUS parameters given in Annex A.3M.

## 7.2Diversity characteristics

The UE is required to be equipped with a minimum of two Rx antenna ports in all operating bands except for the bands n7, n38, n41, n48, n77, n78, n79, n104 where the UE is required to be equipped with a minimum of four Rx antenna ports. This requirement applies when the band is used as a standalone band or as part of a band combination.

Unless otherwise stated, the following applicability rules apply,

-For the single carrier REFSENS requirements in Clause 7:

-the UE shall be verified with two Rx antenna ports in all supported frequency bands,

-additional requirements for four Rx ports shall be verified in operating bands where the UE is equipped with four Rx antenna ports, and

-additional requirements for four and six Rx ports shall be verified in operating bands where the UE is equipped with six Rx antenna ports, and

-additional requirements for four, six and eight Rx ports shall be verified in operating bands where the UE is equipped with eight Rx antenna ports.

-For Rx requirements other than single carrier REFSENS in Clause 7:

-the UE shall be verified with four Rx antenna ports and skip two Rx antenna ports requirements in operating bands where the UE is equipped with four Rx antenna ports,

-the UE shall be verified with six Rx antenna ports and skip both two and four Rx antenna ports requirements in operating bands where the UE is equipped with six Rx antenna ports,

-the UE shall be verified with eight Rx antenna ports and skip two, four and six Rx antenna ports requirements in operating bands where the UE is equipped with eight Rx antenna ports unless the UE does not support eight Rx ports for band(s) in a band combination in which case those band(s) shall be verified with four Rx antenna ports,

-otherwise, the UE shall be verified with two Rx antenna ports.

-The above rules apply for all clauses except for clause 7.9.

A (e)Redcap UE is required to be equipped with a minimum of single Rx antenna port and maximum of two Rx antenna ports. Clause 7 requirements for four Rx antenna ports do not apply to a (e)RedCap UE.

If a UE indicates intraBandNR-CA-non-collocated-r18 or intraBandNR-CA-non-collocated-r19, both Rx power imbalance requirements as specified in clause 7.10A and Rx requirements in clauses 7.3 – 7.9 shall be verified.

## 7.2JDiversity characteristics for ATG

The ATG UE is required to be equipped with a minimum of two Rx antenna ports in all operating bands. ATG UE is required optionally to be equipped with four Rx antenna ports.

## 7.2MDiversity characteristics for WUS/WUR

There is no diversity gain for LP-WUS/WUR.

## 7.3Reference sensitivity

## 7.3.1General

The reference sensitivity power level REFSENS is the minimum mean power applied to each one of the UE antenna ports for all UE categories, at which the throughput shall meet or exceed the requirements for the specified reference measurement channel.

In later clauses of Clause 7 where the value of REFSENS is used as a reference to set the corresponding requirement:

-when the UE is verified with 2 Rx antenna ports, it shall be verified against those requirements by applying the REFSENS value in Table 7.3.2-1a, Table 7.3.2-1b and Table 7.3.2-1c or Table 7.3.2-1d with 2 Rx antenna ports tested;

-when the UE is verified with 4 Rx antenna ports, it shall be verified against those requirements by applying the resulting REFSENS value derived from the requirement in Table 7.3.2-2 with 4 Rx antenna ports tested.

-when the UE is verified with 6 Rx antenna ports, it shall be verified against those requirements by applying the resulting REFSENS value derived from the requirement in Table 7.3.2-2aa with 6 Rx antenna ports tested.

-when the UE is verified with 8 Rx antenna ports, it shall be verified against those requirements by applying the resulting REFSENS value derived from the requirement in Table 7.3.2-2a with 8 Rx antenna ports tested.

## 7.3.2Reference sensitivity power level

The throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2.2, A3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.3.2-1a, Table 7.3.2-1b, Table 7.3.2-1c, Table 7.3.2-1d , Table 7.3.2-2, and Table 7.3.2-2a and Table 7.3.2-2aa.

Table 7.3.2-1a: Two antenna port reference sensitivity QPSK PREFSENS for FDD bands

Table 7.3.2-1b: Two antenna port reference sensitivity QPSK PREFSENS for TDD, SDL and FDD with variable duplex operation bands

For power class 2 UEs, certain degradation of the reference sensitivity in Table 7.3.2-1a is allowed. The maximum amount of degradation is specified in Table 7.3.2-1c, and in Table 7.3.2-1d for a UE that indicates txDiversity-r16 or txDiversity2Tx-r18 [15].

Table 7.3.2-1c: Reference Sensitivity Degradation from PC3 to PC2 for FDD bands for UE not supporting Tx Diversity

Table 7.3.2-1d: Reference Sensitivity Degradation from PC3 to PC2 forFDD bands for UE supporting Tx Diversity

For UE(s) equipped with 4 Rx antenna ports, reference sensitivity for 2Rx antenna ports in Table 7.3.2-1a and in Table 7.3.2-1b shall be modified by the amount given in ΔRIB,4R in Table 7.3.2-2 for the applicable operating bands. For operating band frequency range ≤ 1 GHz, the 4Rx operation is primarily for FWA form factor, and when 4Rx operation is supported by handheld UE, ∆RIB,4R as indicated in Table 7.3.2-2 NOTE 2 is applied.

Table 7.3.2-2: Four antenna port reference sensitivity allowance ΔRIB,4R

For UE(s) equipped with 8 Rx antenna ports, reference sensitivity for 2Rx antenna ports in Table 7.3.2-1a and in Table 7.3.2-1b shall be modified by the amount given in ΔRIB,8R in Table 7.3.2-2a for the applicable operating bands.

Table 7.3.2-2a: Eight antenna port reference sensitivity allowance ΔRIB,8R

For UE(s) equipped with 6 Rx antenna ports, reference sensitivity for 2Rx antenna ports in Table 7.3.2-1a and in Table 7.3.2-1b shall be modified by the amount given in ΔRIB,6R in Table 7.3.2-2aa for the applicable operating bands.

Table 7.3.2-2aa: Six antenna port reference sensitivity allowance ΔRIB,6R

For two Rx antenna port XR UE(s) indicating UE capability supportOf2RxXR-r18, reference sensitivity for two Rx antenna ports in Table 7.3.2-1a and in Table 7.3.2-1b shall be modified by the amount given in ΔRXR,2R in Table 7.3.2-2b for the applicable operating bands.

Table 7.3.2-2b: Two antenna port XR UE reference sensitivity allowance ΔRXR,2R

The reference receive sensitivity (REFSENS) requirement specified in Table 7.3.2-1a, Table 7.3.2-1b, Table 7.3.2-1c, Table 7.3.2-1d, Table 7.3.2-2, Table 7.3.2-2a, Table 7.3.2-2aa and Table 7.3.2-2b shall be met with uplink transmission bandwidth less than or equal to that specified in Table 7.3.2-3 except for the channel bandwidths indicated with NOTE 11 in Table 7.3.2-1a, NOTE 4 in Table 7.3.2-1c, and NOTE 4 in Table 7.3.2-1d.

Table 7.3.2-3: Uplink configuration for reference sensitivity

Unless given by Table 7.3.2-4, the minimum requirements specified in Tables 7.3.2-1a, Tables 7.3.2-1b, Tables 7.3.2-1c, Tables 7.3.2-1d and 7.3.2-2 shall be verified with the network signalling value NS_01 (Table 6.2.3-1) configured.

Table 7.3.2-4: Network signaling value for reference sensitivity

## 7.3.3ΔRIB,c

For a UE supporting CA, SUL or DC band combination, the minimum requirement for reference sensitivity in Table 7.3.2-1a and Table 7.3.2-1b shall be increased by the amount given by ΔRIB,c defined in clause 7.3A, 7.3B, 7.3C in this specification and 7.3A, 7.3B in TS 38.101-3 [3] for the applicable operating bands.

In case the UE supports more than one of band combinations for CA, SUL or DC, and an operating band belongs to more than one band combinations then

-When the operating band frequency range is ≤ 1 GHz, the applicable additional ΔRIB,c shall be the average value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in this specification and 7.3A, 7.3B in TS 38.101-3 [3], truncated to one decimal place that apply for that operating band among the supported band combinations. In case there is a harmonic relation between low band UL and high band DL, then the maximum ΔRIB,c among the different supported band combinations involving such band shall be applied

-When the operating band frequency range is > 1 GHz, the applicable additional ΔRIB,c shall be the maximum value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in this specification and 7.3A, 7.3B in TS 38.101-3 [3] for the applicable operating bands.

## 7.3AReference sensitivity for CA

## 7.3A.1General

The reference sensitivity power level REFSENS is the minimum mean power applied to each one of the UE antenna ports for all UE categories, at which the throughput shall meet or exceed the requirements for the specified reference measurement channel. For operations with 4 Rx or 8 Rx antenna ports, the MSD in the applicable bands shall be increased by the absolute value of ΔRIB,4R in Table 7.3.2-2 or ΔRIB,8R in Table 7.3.2-2a when MSD > 0.

For reference sensitivity exception test points where the specified carrier frequency does not correspond to a valid NR-ARFCN, the closest NR-ARFCN as specified in clause 5.4.2 applies.

For reference sensitivity level tests or reference sensitivity exception tests specified in clause 7.3A, SCS=15kHz based UL test configuration can be replaced by SCS=30kHz based UL test configuration. The equivalent substitution relationship between different SCS UL test configuration is shown in Table 7.3A.1-1 for the operating bands above 2.2GHz.

Table 7.3A.1-1: Equivalent substitution relationship between different SCS UL test configuration

## 7.3A.2Reference sensitivity power level for CA

## 7.3A.2.1Reference sensitivity power level for Intra-band contiguous CA

For intra-band contiguous carrier aggregation, the throughput of each component carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.3.2-1a, Table 7.3.2-1b, Table 7.3.2-2, Table 7.3.2-2a, and Table 7.3.2-3.

For UE(s) supporting one uplink carrier, the uplink configuration of the PCC shall be in accordance with Table 7.3.2-3 and the downlink PCC carrier center frequency shall be configured closer to uplink operating band than any of the downlink SCC center frequency. For power class 3, the reference sensitivity power level is increased by ΔRIBC for specific uplink and downlink test points which are specified in Table 7.3A.2.1-1a.

For aggregation of two or more downlink FDD carriers with two uplink carriers, the reference sensitivity is defined only for the specific uplink and downlink test points which are specified in Table 7.3A.2.1-1 and the power class 3 reference sensitivity power level increased by ΔRIBC. The requirements apply with all downlink carriers active. Unless given by Table 7.3.2-4, the reference sensitivity requirements shall be verified with the network signaling value NS_01 (Table 6.2.3.1-1) configured.

Table 7.3A.2.1-1: Power class 3 intra-band contiguous CA  reference sensitivity with two uplink carriers

Table 7.3A.2.1-1a: Power class 3 intra-band contiguous CA reference sensitivitywith one uplink carrier

Table 7.3A.2.1-2: Void

For power class 2, the reference sensitivity power level is increased by ΔRIBC for specific uplink and downlink test points which are specified in Table 7.3A.2.1-3. The requirements apply with all downlink carriers active. Unless given by Table 7.3.2-4, the reference sensitivity requirements shall be verified with the network signalling value NS_01 (Table 6.2.3.1-1) configured.

Table 7.3A.2.1-3: Power class 2 intra-band contiguous CA reference sensitivitywith one uplink carrier

## 7.3A.2.1.1PC2 and PC1.5 MSD requirements with look-up tables for Intra-band CA

7.3A.2.1.1.1General

The PC2 and PC1.5 MSD requirements with look-up tables for Intra-band CA do not apply when band is n46, n96 or n102.

7.3A.2.1.1.2Intra-band CA with 1UL CC

The PC2 and the PC1.5 MSD requirements with look-up tables for Intra-band CA reference sensitivity exceptions (MSD) due to 1UL CC interference shall apply when the following criteria are met:

-A PC3 reference sensitivity exception requirement is specified either in Table 7.3A.2.1-1a, or in Table 7.3A.2.2-1, and, the corresponding PC2 or PC1.5 reference sensitivity exception requirement is not specified in Table 7.3A.2.1-3, or in Table 7.3A.2.2-1a, and

-PC2 output power achieved with one Tx antenna connector “PC21Tx”, or achieved with two Tx antenna connectors “PC22Tx”, or PC1.5 output power achieved with two Tx antenna connectors “PC1.52Tx” is specified in Table 6.2.1-1 or Table 6.2D.1-1, and,

For these cases, and where in the following PCx denotes either PC21Tx, PC22Tx or PC1.52Tx, the PCx MSD is specified as:

PCx MSD = PC3 MSD + MSD

where,

-PCx MSD is the reference sensitivity exception specified for PC21Tx, PC22Tx, or PC1.52Tx,

-PC3 MSD is the reference sensitivity exception specified for PC3 in Table 7.3A.2.1-1a, or in Table 7.3A.2.2-1,

-MSD values are specified in Table 7.3A.2.1.1.2-1 output columns denoted “MSDmax 3, 6, 9”. These apply to the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in Table Table 7.3A.2.1-1a, or in Table 7.3A.2.2-1,

-The correspondence between the MSDmax specified in Table 7.3A.2.1.1.2-1, the source of interference and PCx MSD is specified in Table 7.3A.2.1.1.2-2,

Table 7.3A.2.1.1.2-1: MSD per MSDmax look-up table for MSD

Table 7.3A.2.1.1.2-2: MSDmax correspondence look-up table for source of interference and PCx MSD

As an exception, for cases where:

-The PC21Tx MSD is specified in 7.3A.2.1-3, or in Table 7.3A.2.2-1a, and

-The PC3 MSD is not specified in Table 7.3A.2.1-1a, or in Table 7.3A.2.2-1, and

-PC1.5 output power achieved with two Tx antenna connectors “PC1.52Tx” is specified in Table 6.2.1-1 or in Table 6.2D.1-1,

then the PC1.52Tx MSD is specified as:

PC1.52Tx MSD = PC21Tx MSD + MSD,

where in the Table 7.3A.2.1.1.2-1,

-MSD is specified output column denoted “MSDmax 6”,

-The input column uses the specified “PC21Tx MSD” instead of “PC3 MSD”. These apply to the same uplink/downlink configurations as those specified for the minimum PC2 MSD requirements in Table Table 7.3A.2.1-1a, or in Table 7.3A.2.2-1.

## 7.3A.2.2Reference sensitivity power level for Intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, throughput of each downlink component carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) and parameters specified in Table 7.3.2-1a, Table 7.3.2-1b, Table 7.3.2-2, Table 7.3.2-2a and Table 7.3A.2.2-1.

For aggregation of two or more downlink FDD carriers with one uplink carrier and unless otherwise noted, the downlink SCC carrier center frequency shall be configured closer to the uplink operating band than the downlink PCC center frequency. For power class 3, the reference sensitivity is increased by ΔRIBNC only for the specific uplink and downlink test points which are specified in Table 7.3A.2.2-1. For power class 2, the reference sensitivity power level is increased by ΔRIBNC for specific uplink and downlink test points which are specified in Table 7.3A.2.2-1a. The requirements apply with all downlink carriers active. Unless given by Table 7.3.2-4, the reference sensitivity requirements shall be verified with the network signaling value NS_01 (Table 6.2.3.1-1) configured.

Table 7.3A.2.2-1: Power class 3 intra-band non-contiguous CA reference sensitivity with one uplink carrier.

Table 7.3A.2.2-1a: Power class 2 intra-band non-contiguous CA reference sensitivitywith one uplink carrier

For intra-band non-contiguous carrier aggregation with two uplink carriers and two or more downlink sub-blocks, throughput of each downlink component carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) and parameters specified in Table 7.3.2-1a, Table 7.3.2-1b, Table 7.3.2-2, Table 7.3.2-2a and Table 7.3A.2.2-2 with the power class 3 reference sensitivity power level increased by ΔRIBNC  only for the specific uplink and downlink test points which are specified in Table 7.3A.2.2-2.The requirements apply with all downlink carriers and two uplink carriers active. The reference sensitivity requirements shall be verified with the network signaling value NS_01 (Table 6.2.3.1-1) configured.

Table 7.3A.2.2-2: Power class 3 intra-band non-contiguous CA reference sensitivitywith two uplink carriers

## 7.3A.2.3Reference sensitivity power level for Inter-band CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one NR band the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1 with parameters specified in  Table 7.3.2-1a, Table 7.3.2-1b, Table 7.3.2-2, Table 7.3.2-2a, Table 7.3.2-3, and in Table 7.3F.2-1, Table 7.3F.2-2, Table 7.3F.2-3 for inter-band CA with one shared spectrum channel access band, modified in accordance with clause 7.3A.3.2. The reference sensitivity is defined to be met with all downlink component carriers active and one of the uplink carriers active. Exceptions to reference sensitivity are allowed in accordance with clause 7.3A.4, 7.3A.5 and 7.3A.6.

For the combination of intra-band and inter-band carrier aggregation, the intra-band CA relaxation, ΔRIBC and ΔRIBNC, are also applied according to the clause 7.3A.2.1 and 7.3A.2.2.

## 7.3A.2.3.1PC2 and PC1.5 MSD requirements with look-up tables for two-band DL CA with 1UL band

7.3A.2.3.1.0General

The PC2 and PC1.5 MSD requirements with look-up tables for two or three DL band CA with 1UL band do not apply when the UL band is either band n46, band n96 or band n102.

7.3A.2.3.1.11UL band with 1UL CC for 2DL band CA

The PC2 and the PC1.5 MSD requirements with look-up tables for two-band DL CA reference sensitivity exceptions (MSD) due to 1UL band 1UL CC harmonic, harmonic mixing, and cross band isolation interference shall apply when the following criteria are met:

-A PC3 reference sensitivity exception requirement is specified either in Table 7.3A.4-1, or in Table 7.3A.4-4 or in Table 7.3A.6-1, and, the corresponding PC2 or PC1.5 reference sensitivity exception requirement is not specified in Table 7.3A.4-2a, or in Table 7.3A.4-4a-1, or in Table 7.3A.4-4b, or in Table 7.3A.6-1a-1, or in Table 7.3A.6-1b, and

-PC2 output power achieved with one Tx antenna connector “PC21Tx”, or achieved with two Tx antenna connectors “PC22Tx”, or PC1.5 output power achieved with two Tx antenna connectors “PC1.52Tx” is specified in Table 6.2.1-1 or Table 6.2D.1-1, and,

-The PCx aggressor NR UL band is the same aggressor UL band as in case of PC3 MSD.

For these cases, and where in the following PCx denotes either PC21Tx, PC22Tx or PC1.52Tx, the PCx MSD due to harmonic, harmonic mixing, and cross band isolation is specified as:

PCx MSD = PC3 MSD + MSD

where,

-PCx MSD is the reference sensitivity exception specified for PC21Tx, PC22Tx, or PC1.52Tx,

-PC3 MSD is the reference sensitivity exception specified for PC3 in Table 7.3A.4-1, or in Table 7.3A.4-4 or in Table 7.3A.6-1,

-MSD values are specified in Table 7.3A.2.3.1.1-1 output columns denoted “MSDmax 3, 6, 9”. These apply to the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in Table 7.3A.4-1, or in Table 7.3A.4-4 or in Table 7.3A.6-1,

-The correspondence between the MSDmax specified in Table 7.3A.2.3.1.1-1, the source of interference and PCx MSD is specified in Table 7.3A.2.3.1.1-2,

Table 7.3A.2.3.1.1-1: MSD per MSDmax look-up table for MSD due to harmonic, harmonic mixing, cross band isolation

Table 7.3A.2.3.1.1-2: MSDmax correspondence look-up table for source of interference and PCx MSD

As an exception, for cases where:

-The PC21Tx MSD is specified in Table 7.3A.4-2a or in Table 7.3A.4-4a-1 or in Table 7.3A.6-1a-1, and

-The PC3 MSD is not specified in Table 7.3A.4-1, or in Table 7.3A.4-4 or in Table 7.3A.6-1, and

-The PC1.5 MSD is not specified in Table 7.3A.4-4b or in Table 7.3A.6-1b, and

-PC1.5 output power achieved with two Tx antenna connectors “PC1.52Tx” is specified in Table 6.2.1-1 or in Table 6.2D.1-1,

then the PC1.52Tx MSD is specified as:

PC1.52Tx MSD = PC21Tx MSD + MSD,

where in the Table 7.3A.2.3.1.1-1,

-MSD is specified output column denoted “MSDmax 6”,

-The input column uses the specified “PC21Tx MSD” instead of “PC3 MSD”. These apply to the same uplink/downlink configurations as those specified for the minimum PC2 MSD requirements in Table 7.3A.4-2a, or in Table 7.3A.4-4a-1 or in Table 7.3A.6-1a-1.

7.3A.2.3.1.21UL TDD band with 2UL CCs for 2DL band CA

The PC2 and the PC1.5 MSD requirements with look-up tables for two-band DL CA reference sensitivity exceptions (MSD) due to 1UL band with 2UL CC intermodulation interference shall apply when the following criteria are met:

-The UL band is a TDD band configured with intra-band contiguous or intra-band non-contiguous UL CA, and,

-A PC3 reference sensitivity exception requirement is specified in Table 7.3A.5-1, and the corresponding PC2 or PC1.5 reference sensitivity exception requirement is not specified in Table 7.3A.5-1a or in Table 7.3A.5-1b,

-PC2 or PC1.5 power class is specified in Table 6.2A.1.1-1, Table 6.2A.1.2-1 or Table 6.2H.1.1-1

-The PCx aggressor NR UL band is the same aggressor UL band as in case of PC3 MSD.

For these cases, and where in the following PCx denotes either PC2 or PC1.5, the PCx MSD due to 1UL band with two contiguous or two non-contiguous UL CC intermodulation interference is specified as:

PCx MSD = PC3 MSD + MSD

where,

-PC3 MSD is the reference sensitivity exception specified in Table 7.3A.5-1,

-For IMD3 and IMD5 MSD values are specified in Table 7.3A.2.3.1.1-1 output column denoted “MSDmax 3” for PC2 and “MSDmax 6” for PC1.5,

-For IMD4 and ≥ IMD6 MSD values are specified in Table 7.3A.2.3.2.1-1 output columns denoted “MSDmax  9” for PC2 and “MSDmax 15” for PC1.5,

-These apply for the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in Table 7.3A.5-1,

-The correspondence between the MSDmax specified in Table 7.3A.2.3.2.1-1, the IMD order and PCx MSD is specified in Table 7.3A.2.3.1.2-1,

Table 7.3A.2.3.1.2-1: MSDmax correspondence look-up table for 1UL band 2UL CC IMD order and PCx MSD

As an exception, for cases where:

-The PC2 MSD is specified in Table 7.3A.5-1a, and,

-The PC3 MSD is not specified in Table 7.3A.5-1, and,

-The PC1.5 MSD is not specified in Table 7.3A.5-1b, and,

-PC1.5 power class is specified in Table 6.2A.1.1-1, Table 6.2A.1.2-1 or Table 6.2H.1.1-1,

then the PC1.5 MSD is specified as:

PC1.5 MSD = PC2 MSD + MSD,

where,

-MSD is specified output column denoted “MSDmax 3” in the Table 7.3A.2.3.1.1-1 for IMD3 and IMD5, and,

-MSD is specified output column denoted “MSDmax 6” in the Table 7.3A.2.3.2.1-1 for IMD4 and ≥ IMD6,

-The input column uses the specified “PC2 MSD” instead of “PC3 MSD”. These apply to the same uplink/downlink configurations as those specified for the minimum PC2 MSD requirements in Table 7.3A.5-1a.

## 7.3A.2.3.2PC2 and PC1.5 MSD requirements with look-up tables for two-band or three-band DL CA with two-band UL CA

7.3A.2.3.2.0General

The PC2 and PC1.5 MSD requirements with look-up tables for two or three DL band CA with 2UL band CA do not apply when the UL band is either band n46, band n96 or band n102.

7.3A.2.3.2.12UL band CA with 1UL CC in each band

The PC2 and the PC1.5 MSD requirements with look-up tables for two-band and three-band DL CA reference sensitivity exceptions (MSD) due to 2UL CA intermodulation interference shall apply when the following criteria are met:

-A PC3 reference sensitivity exception requirement is specified either in Table 7.3A.5-1, or in Table 7.3A.5-2, and, the corresponding PC2 or PC1.5 reference sensitivity exception requirement is not specified in Table 7.3A.5-1a, or in Table 7.3A.5-1b, or in Table 7.3A.5-2a, or in Table 7.3A.5-2b, and

-PC2 or PC1.5 two-band UL CA is specified in Table 6.2A.1.3-1, or Table 6.2H.3.1-1, or in clause 6.2L.3.1, and,

-The PC2 or PC1.5 MSD is caused by the same uplink/downlink configurations as in case of PC3 MSD.

For these cases, and where in the following PCx denotes either PC2 or PC1.5, the PCx MSD due to 2UL CA intermodulation interference is specified as:

PCx MSD = PC3 MSD + MSD

where,

-PCx MSD is the reference sensitivity exception specified for PC2 or PC1.5 with 2UL band CA 1Tx or 2Tx in each UL band and with 1UL CC in each UL band,

-PC3 MSD is the reference sensitivity exception specified for PC3 in Table 7.3A.5-1, or in Table 7.3A.5-2,

-MSD values are specified in Table 7.3A.2.3.2.1-1 output columns denoted “MSDmax 6, 9, 12, 15, 18, 24, 30”. These apply for the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in Table 7.3A.5-1, or in Table 7.3A.5-2, and,

-The correspondence between the MSDmax specified in Table 7.3A.2.3.2.1-1, the IMD order and PCx MSD is specified in Table 7.3A.2.3.2.1-2,

Table 7.3A.2.3.2.1-1: MSD per MSDmax look-up table for MSD due to 2UL CA intermodulation interference

Table 7.3A.2.3.2.1-2: MSDmax correspondence look-up table for IMD order and PCx MSD

As an exception, for cases where:

-The PC2 MSD is specified in Table 7.3A.5-1a or in Table 7.3A.5-2a, and,

-The PC3 MSD is not specified in Table 7.3A.5-1 or in Table 7.3A.5-2, and,

-The PC1.5 MSD is not specified in Table 7.3A.5-1b or in Table 7.3A.5-2b, and,

-PC2 or PC1.5 two-band UL CA is specified in Table 6.2A.1.3-1 or Table 6.2H.3.1-1 or in clause 6.2L.3.1,

then the PC1.5 MSD is specified as:

PC1.5 MSD = PC2 MSD + MSD,

where,

-In the Table 7.3A.2.3.2.1-1, MSD is specified with output columns denoted “MSDmax 6, 9, 12, 15” and where the input column uses the specified PC2 MSD specified in Table 7.3A.5-1a or in Table 7.3A.5-2a instead of the PC3 MSD, and

-In the Table 7.3A.2.3.2.1-2, the correspondence between the MSDmax and the IMD order is specified using the column specified for “PC2 MSD”, and

-These PC1.5 MSD requirements apply for the same uplink/downlink configurations as those specified in the PC2 MSD requirements of Table 7.3A.5-1a or Table 7.3A.5-2a.

7.3A.2.3.2.22UL band CA with 2UL contiguous CCs in one TDD band and 1UL CC in the other band

The PC2 and the PC1.5 MSD requirements with look-up tables for two-band and three-band DL CA reference sensitivity exceptions (MSD) due to 2UL band CA IMD3 interference from 2UL CC in one TDD band and 1UL CC in the other band, (also known as 1st order triple-beat MSD) shall apply when the following criteria are met:

-The UL band is configured with intra-band contiguous UL CA is a TDD band, and,

-The other UL band is configured with 1UL CC, and

-A PC3 reference sensitivity exception requirement is specified in Table 7.3A.5-1 or in Table 7.3A.5-2, and the corresponding PC2 or PC1.5 reference sensitivity exception requirement is not specified in Tables 7.3A.5-1a or 7.3A.5-2a or Tables 7.3A.5-1b or 7.3A.5-2b,

-PC2 or PC1.5 power class is specified in Table 6.2A.1.3-1 or Table 6.2H.3.1-1 or in clause 6.2L.3.1,

-The PCx aggressor NR UL band is the same aggressor UL band as in case of PC3 MSD.

For these cases, and where in the following PCx denotes either PC2 or PC1.5, the PCx MSD due to 2UL band CA IMD3 interference with two contiguous UL CC in one band and 1UL CC in the other band is specified as:

PCx MSD = PC3 MSD + MSD

where,

-PC3 MSD is the reference sensitivity exception specified for PC3 in Table 7.3A.5-1, or in Table 7.3A.5-2,

-MSD values are specified in Table 7.3A.2.3.2.1-1output column denoted “MSDmax 6” for PC2 and “MSDmax 12” for PC1.5. These apply for the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in Table 7.3A.5-1, or in Table 7.3A.5-2, and,

As an exception, for cases where:

-The PC2 MSD is specified in Table 7.3A.5-1a or in Table 7.3A.5-2a, and,

-The PC3 MSD is not specified in Table 7.3A.5-1 or in Table 7.3A.5-2, and,

-The PC1.5 MSD is not specified in Table 7.3A.5-1b or in Table 7.3A.5-2b, and,

-PC1.5 two-band UL CA for a total of 2Tx or 3Tx or 4Tx and with 1CC in one UL band and two CCs in the other UL band is specified in Table 6.2A.1.3-1 or Table 6.2H.3.1-1 or in clause 6.2L.3.1,

then the PC1.5 MSD is specified as:

PC1.5 MSD = PC2 MSD + MSD

where in the Table 7.3A.2.3.2.1-1,

-MSD is specified with output column denoted “MSDmax 6”,

-The input column uses the specified “PC2 MSD” instead of “PC3 MSD”.

## 7.3A.2.4Void

## 7.3A.2.5Reference sensitivity power level for low NR band carrier aggregation via switching

The reference sensitivity power level REFSENS for low NR band inter-band carrier aggregation supported via switching featureSetCombinationLowBandSwitching-r19  in a band pair is the minimum mean power applied to each band respectively at each one of the UE antenna ports for all UE categories, at which the throughput in the DL scheduling before and/or after the Switching Gap shall meet or exceed the requirements for the specified reference measurement channel. It’s noted that the DL scheduling in the RMC for Inter-band CA via switching as specified in Annexes A.8 is closest to the Switching Gap (gapDurationPCelltoSCell-r19 and gapDurationSCelltoPCell-r19) configured by network.

For a UE indicating the capability switchingPeriodForFDD-SDL-r19 for the band pair of NR inter-band CA combinations defined in Table 5.2A.2.1-1, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2.2/A8.1 (with one sided dynamic OCNG Pattern OP.1 FDD for the DL-signal as described in Annex A.5.1.1) with the REFSENS specified in Table 7.3.2-1a for PCell FDD band, the REFSENS specified in Table 7.3.2-1b for SCell SDL band and uplink transmission bandwidth less than or equal to that specified in Table 7.3.2-3 for PCell FDD band.

## 7.3A.3ΔRIB,c for CA

## 7.3A.3.1General

For a UE supporting a CA configuration, the ΔRIB,c applies for both SC and CA operation.

## 7.3A.3.2ΔRIB,c for Inter-band CA

For the UE which supports inter-band carrier aggregation, the minimum requirement for reference sensitivity in clause 7.3A.2 shall be increased by the amount given by ΔRIB,c defined in clause 7.3A.3.2 for the applicable operating bands. Unless otherwise stated, ΔRIB,c is set to zero.

In case the UE supports more than one of band combinations for CA, SUL or DC, and an operating band belongs to more than one band combinations then

-When the operating band frequency range is ≤ 1 GHz, the applicable additional ΔRIB,c shall be the average value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in this specification and 7.3A, 7.3B in TS 38.101-3 [3], truncated to one decimal place that apply for that operating band among the supported band combinations. In case there is a harmonic relation between low band UL and high band DL, then the maximum ΔRIB,c among the different supported band combinations involving such band shall be applied

-When the operating band frequency range is > 1 GHz, the applicable additional ΔRIB,c shall be the maximum value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in this specification and 7.3A, 7.3B in TS 38.101-3 [3] for the applicable operating bands.

## 7.3A.3.2.1ΔRIB,c for two bands

Table 7.3A.3.2.1-1: ΔRIB,c due to CA (two bands)

Table 7.3A.3.2.1-2: void

## 7.3A.3.2.2Void

## 7.3A.3.2.3ΔRIB,c for three bands

Table 7.3A.3.2.3-1: ΔRIB,c due to CA (three bands)

## 7.3A.3.2.4ΔRIB,c for four bands

Table 7.3A.3.2.4-1: ΔRIB,c due to CA (four bands)

## 7.3A.3.2.5ΔRIB,c for five bands

Table 7.3A.3.2.5-1: ΔRIB,c due to CA (five bands)

## 7.3A.3.2.6ΔRIB,c for six bands

Table 7.3A.3.2.6-1: ΔRIB,c due to CA (six bands)

## 7.3A.3.3ΔRIB,c for Intra-band CA

Table 7.3A.3.3-1: ΔRIB,c due to Intra-band contiguous CA

Table 7.3A.3.3-2: ΔRIB,c due to Intra-band non-contiguous CA

## 7.3A.4Reference sensitivity exceptions due to harmonic interference for CA

Sensitivity degradation is allowed for different combinations of UL configurations and DL channel bandwidths if a band in frequency range 1 is impacted by UL harmonic interference from another band which belongs to NR band in frequency range 1 of the same downlink CA configuration. Reference sensitivity exceptions and uplink/downlink configurations due to UL harmonic from a PC3 aggressor NR UL band for either single band uplink or PC3 or PC2 CA are specified in Table 7.3A.4-1. For these exceptions, only the listed test points in Table 7.3A.4-1 are needed to be tested.

Table 7.3A.4-1: Reference sensitivity exceptions and uplink/downlink configurations due to UL harmonic from a PC3 aggressor NR UL band for NR DL CA FR1

The reference sensitivity for the shared access band does not apply when there is at least one individual RE within the shared access downlink transmission bandwidth which falls into the reference sensitivity exclusion region as specified in Table 7.3A.4-1a.

Table 7.3A.4-1a: NR-U reference sensitivity measurement exclusion region in MHz.

Table 7.3A.4-2: Void

For a PC2 aggressor NR UL band for NR DL CA FR1, the maximum amount of REFSENS degradation is specified in Table 7.3A.4-2a.

Table 7.3A.4-2a: Reference sensitivity exceptions and uplink/downlink configurations due to UL harmonic from a PC2 aggressor NR UL band for NR DL CA FR1

Table 7.3A.4-2b: Void

Table 7.3A.4-3: Void

Table 7.3A.4-3a: Void

Sensitivity degradation is allowed for different combinations of UL configurations and DL channel bandwidths if a band is impacted by receiver harmonic mixing due to another band part which belongs to PC3 NR band or PC2 NR band of the same CA configuration. Reference sensitivity exceptions and uplink/downlink configurations due to harmonic mixing from a PC3 aggressor NR UL band for either PC3 or PC2 CA are specified in Table 7.3A.4-4 and from a PC2 aggressor NR UL band for PC2 CA are specified in Table 7.3A.4-4a.For these exceptions, only the listed test points in Table 7.3A.4-4, Table 7.3A.4-4a and Table 7.3A.4-4b are needed to be tested. Sensitivity degradation is not required for receiver even order harmonic mixing with aggressor 3rd order and above harmonic interference.

Table 7.3A.4-4: Reference sensitivity exceptions and uplink/downlink configurations due to harmonic mixing from a PC3 aggressor NR UL band for DL NR CA FR1

Table 7.3A.4-4a-1: Reference sensitivity exceptions and uplink/downlink configurations due to harmonic mixing from a PC2 aggressor NR UL band for NR DL CA FR1

Table 7.3A.4-4a-2: Void

Table 7.3A.4-4b: Reference sensitivity exceptions and uplink/downlink configurations due to harmonic mixing from a PC1.5 aggressor NR UL band for NR DL CA FR1

The reference sensitivity for the shared access band does not apply when there is at least one individual RE within the shared access downlink transmission bandwidth which falls into the reference sensitivity exclusion region as specified in Table 7.3A.4-1c.

Table 7.3A.4-4c: NR-U reference sensitivity measurement exclusion region in MHz.

Table 7.3A.4-4d: Reference sensitivity exceptions and uplink/downlink configurations due to harmonic mixing from a power class 5 aggressor NR UL band for NR DL CA FR1

Table 7.3A.4-5: Void

## 7.3A.5Reference sensitivity exceptions due to intermodulation interference due to 2UL CA

For inter-band carrier aggregation with uplink assigned to two CCs from up to two UL NR bands and three CCs from two UL NR bands given in Table 7.3A.5-1, Table 7.3A.5-1a, Table 7.3A.5-1b, Table 7.3A.5-2, Table 7.3A.5-2a and Table 7.3A.5-2b the reference sensitivity is defined only for the specific uplink and downlink test points specified in Table 7.3A.5-1, Table 7.3A.5-1a, Table 7.3A.5-1b, Table 7.3A.5-, Table 7.3A.5-2a and Table 7.3A.5-2b. For these test points the reference sensitivity requirement specified in Table 7.3.2-1a, Table 7.3.2-1b, Table 7.3.2-2 and Table 7.3.2-2a  are relaxed by the amount of the corresponding parameter MSD given in Table 7.3A.5-1, Table 7.3A.5-1a, Table 7.3A.5-1b, Table 7.3A.5-2, Table 7.3A.5-2a and Table 7.3A.5-2b.

Table 7.3A.5-1: 2DL/2UL inter-band Reference sensitivity QPSK PREFSENS and uplink/downlink configurations for PC3 CA

Table 7.3A.5-1a: 2DL/2UL inter-band Reference sensitivity QPSK PREFSENS and uplink/downlink configurations for PC2 CA

Table 7.3A.5-1b: 2DL/2UL inter-band Reference sensitivity QPSK PREFSENS and uplink/downlink configurations for PC1.5 CA

Table 7.3A.5-2: 3DL/2UL interband Reference sensitivity QPSK PREFSENS and uplink/downlink configurations for PC3 CA

Table 7.3A.5-2a: 3DL/2UL interband Reference sensitivity QPSK PREFSENS and uplink/downlink configurations for PC2 CA

Table 7.3A.5-2b: 3DL/2UL inter-band Reference sensitivity QPSK PREFSENS and uplink/downlink configurations for PC1.5 CA

## 7.3A.6Reference sensitivity exceptions due to cross band isolation for CA

Sensitivity degradation is allowed for a band if it is impacted by UL of another band part which belongs to NR band of the same NR CA configuration due to cross band isolation issues. The reference sensitivity degradation for the victim band due to cross band isolation is specified only for the specific uplink and downlink test points specified in Table 7.3A.6-1 for either PC3 and PC2 NR CA from a PC3 aggressor NR UL band, and for PC2 NR CA, in Table 7.3A.6-1afrom a PC2 aggressor NR UL band, and in Table 7.3A.6-1b from a PC1.5 aggressor NR single band uplink, and in Table 7.3A.6-3 when a DL band < 1 GHz  is victim of two simultaneous PC3 aggressor NR UL bands.

In Tables 7.3A.6-1, 7.3A.6-1a and 7.3A.6-1b the following terminology is used to define the source of cross-band isolation interference:

-“ACLR1” indicates that the first adjacent channel of the aggressor UL band falls into the Rx channel of victim band.

-“ACLR2” indicates that the second adjacent channel of the aggressor UL band falls into the Rx channel of victim band.

-“>ACLR2” indicates that neither the first, nor the second adjacent channel of the aggressor UL band falls into the Rx channel of victim band.

In Table 7.3A.6-3 only two DL / two UL < 1 GHz bands cases where one DL is simultaneously victim of UL channel ACLR1 of one band and UL channel ACLR1 or 2 of the other band are specified.

Table 7.3A.6-1: Reference sensitivity exceptions (MSD) and uplink/downlink configurations due to cross band isolation from a PC3 aggressor NR UL band for NR CA FR1

Table 7.3A.6-1a-1: Reference sensitivity exceptions (MSD) and uplink/downlink configurations due to cross band isolation from a PC2 aggressor NR UL band for NR CA FR1

Table 7.3A.6-1a-2: Void

Table 7.3A.6-1b: Reference sensitivity exceptions (MSD) and uplink/downlink configurations due to cross band isolation from a PC1.5 aggressor NR single UL band for DL NR CA FR1

Table 7.3A.6-1c: Reference sensitivity exceptions (MSD) and uplink/downlink configurations due to cross band isolation from a power class 5 aggressor NR single UL band for DL NR CA FR1

Table 7.3A.6-2: Void

Table 7.3A.6-3: Reference sensitivity exceptions (MSD) and uplink/downlink configurations due to cross band isolation from two simulataneous PC3 aggressor NR UL bands for NR CA FR1

## 7.3A.7Lower-MSD requirements for inter-band CA

A UE can report better MSD performance than the minimum requirements as specified in clause 7.3A.4, 7.3A.5, 7.3A.6, 7.3A.2.3.1 and in clause 7.3A.2.3.2 by lowerMSD-r18 capability, except that the reporting for MSD caused by IMD with order higher than 5, IMD of UL intra-band CA or triple-beat is not supported in this release of the specification. The MSD performance after improvement is categorized into different lower-MSD capability classes, which are defined in Table 7.3A.7-1.

Table 7.3A.7-1: Lower-MSD capability classes

The reported lower-MSD capability classes are subject to the same uplink/downlink configurations as defined for the minimum MSD requirements in clause 7.3A.4, 7.3A.5, 7.3A.6, 7.3A.2.3.1 and 7.3A.2.3.2. If a UE can support more than one test points for a given REFSENS exception case, the reported lower-MSD capability class is applicable for the test point having the largest specified MSD value. Otherwise, it’s only applicable for the test point which can be supported by the UE. If one or multiple power classes are requested by the network, the UE can, if supported, report lowerMSD-r18 capability for the requested power classes; otherwise, the UE shall report lowerMSD-r18 capability for the highest supported power class for the given CA configuration.

The UE shall meet one of the following conditions in order to report lowerMSD-r18 capability for a given REFSENS exception case:

-If the specified minimum requirement is tightly bounded by the range of a lower-MSD capability class (i.e, Thresholdi-1 < MSD ≤ Thresholdi, where i and (i-1) are two adjacent lower-MSD capability classes), the actual MSD shall be at least one-level lower (i.e., actual MSD ≤ Thresholdi-1); or

-If the specified minimum requirement is larger than the maximum threshold (corresponding to lower-MSD capability class VIII), the actual MSD shall be no more than the maximum threshold.

Otherwise, the UE shall not report lowerMSD-r18 capability for this REFSENS exception case.

If the special MSD type “ALL” is indicated in the lowerMSD-r18 capability, the reporting conditions as specified above shall be met for each MSD type that has been specified in this release for the given CA configuration.

NOTE 1: The lowerMSD-r18 capability is verified by reusing the MSD test point parameters and only replacing the minimum MSD requirement value by the threshold of the reported lower-MSD capability class. UE supporting lower MSD shall indicate the lower MSD capability for the requested power class if supported. If no power class is explicitly requested, the UE supporting lower MSD shall indicate the lower MSD capability for the highest supported power class of the band combination including victim band and aggressor band(s). And, similar to the specified MSD minimum requirements, only the highest supported power class or the power class required by the certification/regulation body per UL configuration is verified.

NOTE 2:If the UE is equipped with four or eight Rx antenna ports for the victim band of the BC, the lowerMSD-r18 capability is verified with four or eight Rx antenna ports according to clause 7.2 under the condition mentioned above, but with the increased MSD values by the absolute value of ΔRIB,4R or ΔRIB,8R applied for the requirement based on the description in clause 7.3A.1.

## 7.3BReference sensitivity for NR-DC

For inter-band NR-DC configurations, the reference sensitivity for the corresponding inter-band CA configuration as specified in clause 7.3A applies.

## 7.3CReference sensitivity for SUL

## 7.3C.1General

The reference sensitivity power level REFSENS is the minimum mean power applied to each one of the UE antenna ports for all UE categories, at which the throughput shall meet or exceed the requirements for the specified reference measurement channel. For operations with 4 Rx or 8 Rx antenna ports, the MSD in the applicable bands shall be increased by the absolute value of ΔRIB,4R in Table 7.3.2-2 or ΔRIB,8R in Table 7.3.2-2a when MSD > 0.

For reference sensitivity exception test points where the specified carrier frequency does not correspond to a valid NR-ARFCN, the closest NR-ARFCN as specified in clause 5.4.2 applies.

For reference sensitivity level tests or reference sensitivity exception tests specified in clause 7.3C, SCS=15kHz based UL test configuration can be replaced by SCS=30kHz based UL test configuration. The equivalent substitution relationship between different SCS UL test configuration is shown in Table 7.3A.1-1 for the operating bands above 2.2GHz.

## 7.3C.2Reference sensitivity power level for SUL

For SUL operation, the reference receive sensitivity (REFSENS) requirement for downlink bands specified in Table 7.3.2-1a, Table 7.3.2-1b, Table 7.3.2-2 and Table 7.3.2-2a  shall be met for an uplink transmission bandwidth less than or equal to that specified in Table 7.3.2-3 or supplementary uplink transmission bandwidth less than or equal to that specified in Table 7.3C.2-1 with reference measurement channels as specified in Annexes A.2.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1), unless sensitivity degradation is allowed in this clause of this specification. These exceptions also apply to any higher order CA or DC combination containing one of the exception combinations in this clause as subset.

For SUL operation with downlink CA, the reference receive sensitivity (REFSENS) requirement for downlink bands specified in clause 7.3A.2 shall be met for an uplink transmission bandwidth less than or equal to that specified in Table 7.3.2-3 or supplementary uplink transmission bandwidth less than or equal to that specified in Table 7.3C.2-1 with reference measurement channels as specified in Annexes A.2.2.2,  A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1), unless sensitivity degradation is allowed in this clause of this specification. These exceptions also apply to any higher order CA or DC combination containing one of the exception combinations in this clause as subset.

Table 7.3C.2-1: Supplementary uplink configuration for reference sensitivity

For the UE that supports any of the SUL operation given in Table 7.3C.2-2, exceptions to the requirements specified in Table 7.3.2-1a and Table 7.3.2-1b are allowed for different combinations of UL configurations and DL channel bandwidths when the uplink is active in a lower frequency band and is within a specified frequency range such that transmitter harmonics fall within the downlink transmission bandwidth assigned in a higher band as noted in Table 7.3C.2-2 and Table 7.3C.2-2a. For these exceptions, only the listed test points in Table 7.3C.2-2 are needed to be tested for PC3, and only the listed test points in Table 7.3C.2-2a are needed to be tested for PC2.

Table 7.3C.2-2: PC3 Reference sensitivity and uplink/downlink configurations for SUL operation (exceptions due to uplink harmonic issue)

Table 7.3C.2-2a: PC2 Reference sensitivity and uplink/downlink configurations for SUL operation (exceptions due to uplink harmonic issue)

Table 7.3C.2-3: Void

For the UE that supports any of the SUL operation given in Table 7.3C.2-4 and Table 7.3C.2-4a, reference sensitivity degradation is allowed for different combinations of UL configurations and DL channel bandwidths when a DL band is impacted by UL band due to cross band isolation issues. For these exceptions, only the listed test points in Table 7.3C.2-4 are needed to be tested for PC3, and only the listed test points in Table 7.3C.2-4a are needed to be tested for PC2.

Table 7.3C.2-4: PC3 Reference sensitivity and uplink/downlink configurations for SUL operation (exceptions due to cross band isolation)

Table 7.3C.2-4a: PC2 Reference sensitivity and uplink/downlink configurations for SUL operation (exceptions due to cross band isolation)

Table 7.3C.2-5: Void

For the UE that supports any of the SUL operation given in Table 7.3C.2-6 and Table 7.3C.2-6a, reference sensitivity degradation is allowed for different combinations of UL configurations and DL channel bandwidths when a DL band is impacted by UL band due to harmonic mixing issues. For these exceptions, only the listed test points in Table 7.3C.2-6 are needed to be tested for PC3, and only the listed test points in Table 7.3C.2-6a are needed to be tested for PC2.

Table 7.3C.2-6: PC3 reference sensitivity and uplink/downlink configurations for SUL operation (exceptions due to harmonic mixing)

Table 7.3C.2-6a: PC2 reference sensitivity and uplink/downlink configurations for SUL operation (exceptions due to harmonic mixing)

## 7.3C.2.1PC2 and PC1.5 MSD requirements with look-up tables for SUL with downlink CA

The PC2 and the PC1.5 MSD requirements with look-up tables for SUL with downlink CA due to SUL band 1UL CC harmonic, harmonic mixing, and cross band isolation interference shall apply when the following criterias are met:

-A PC3 reference sensitivity exception requirement is specified either in Table 7.3C.2-2, or in Table 7.3C.2-4 or in Table 7.3C.2-6, and,

-PC2 output power achieved with one Tx antenna connector, denoted here “PC21Tx”, or achieved with two Tx antenna connectors, denoted here “PC22Tx”, or PC1.5 output power achieved with two Tx antenna connectors, denoted here “PC1.52Tx”, is specified as a valid power class in Table 6.2.1-1, and,

-The PCx aggressor SUL band is the same aggressor SUL band as in case of PC3 MSD.

For these cases, and where in the following PCx denotes either PC21Tx, PC22Tx or PC1.52Tx, the PCx MSD due to harmonic, harmonic mixing, and cross band isolation is specified as:

PCx MSD = PC3 MSD + MSD

where,

-PCx MSD is the reference sensitivity exception specified for PC21Tx, PC22Tx, or PC1.52Tx,

-PC3 MSD is the reference sensitivity exception specified for PC3 in Table 7.3C.2-2, or in Table 7.3C.2-4 or in Table 7.3C.2-6,

-MSD values are specified in Table 7.3C.2.1-1 output columns denoted “MSDmax 3, 6, 9”. These apply to the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in Table 7.3C.2-2, or in Table 7.3C.2-4 or in Table 7.3C.2-6,

-The correspondence between the MSDmax specified in Table 7.3C.2.1-1, the source of interference and PCx MSD is specified in Table 7.3C.2.1-2,

Table 7.3C.2.1-1: MSD per MSDmax look-up table for MSD due to harmonic, harmonic mixing, cross band isolation

Table 7.3C.2.1-2: MSDmax correspondence look-up table for source of interference and PCx MSD

As an exception, for cases where:

-The PC21Tx MSD is specified in Table 7.3C.2-2a or in Table 7.3C.2-4a or in Table 7.3C.2-6a, and

-The PC3 MSD is not specified in Table 7.3C.2-2, or in Table 7.3C.2-4 or in Table 7.3C.2-6, and

-The PC1.5 MSD is not specified, and

-PC1.5 output power achieved with two Tx antenna connectors “PC1.52Tx” is specified as a valid power class in Table 6.2.1-1,

then the PC1.52Tx MSD is specified as:

PC1.52Tx MSD = PC21Tx MSD + MSD,

where in the Table 7.3C.2.1-1,

-MSD is specified output column denoted “MSDmax 6”,

-The input column uses the specified “PC21Tx MSD” instead of “PC3 MSD”. These apply to the same uplink/downlink configurations as those specified for the minimum PC2 MSD requirements in Table 7.3C.2-2a or in Table 7.3C.2-4a or in Table 7.3C.2-6a.

## 7.3C.3ΔRIB,c for SUL

## 7.3C.3.1General

For a UE supporting a SUL configuration, the ΔRIB,c applies for both SC and SUL operation.

## 7.3C.3.2SUL band combination

For the UE which supports SUL band combiantion, the minimum requirement for reference sensitivity in clause 7.3C.2 shall be increased by the amount given in ΔRIB,c defined in clause 7.3C.3.2 for the applicable operating bands. Unless otherwise stated, ΔRIB,c is set to zero.

In case the UE supports more than one of band combinations for CA, SUL or DC, and an operating band belongs to more than one band combinations then

-When the operating band frequency range is ≤ 1 GHz, the applicable additional ΔRIB,c shall be the average value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in this specification and 7.3A, 7.3B in TS 38.101-3 [3], truncated to one decimal place that apply for that operating band among the supported band combinations. In case there is a harmonic relation between low band UL and high band DL, then the maximum ΔRIB,c among the different supported band combinations involving such band shall be applied

-When the operating band frequency range is > 1 GHz, the applicable additional ΔRIB,c shall be the maximum value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in this specification and 7.3A, 7.3B in TS 38.101-3 [3] for the applicable operating bands.

## 7.3C.3.2.1ΔRIB,c  for two bands

Table 7.3C.3.2.1-1: ΔRIB,c due to SUL (two bands)

## 7.3C.3.2.2ΔRIB,c  for three bands

Table 7.3C.3.2.2-1: ΔRIB,c due to SUL (three bands)

## 7.3C.3.2.3ΔRIB,c  for four bands

Table 7.3C.3.2.3-1: ΔRIB,c due to SUL (four bands)

## 7.3DReference sensitivity for UL MIMO

For UE with multiple transmitter antenna connectors up to a maximum of four in closed-loop spatial multiplexing scheme, the minimum requirements specified in clause 7.3 shall be met with the UL MIMO configurations described in clause 6.2D.1 and clause 6.2F.1D for shared spectrum access operation, and the reference measurement channels as specified in Annex A.2.2 for CP-OFDM waveforms shall apply. For UL MIMO, the parameter PUMAX is the total transmitter power over all transmit antenna connectors.

## 7.3EReference sensitivity for V2X

## 7.3E.1General

The reference sensitivity power level PREFSENS_V2X is the minimum mean power applied to each one of the UE antenna ports for V2X UE, at which the throughput shall meet or exceed the requirements for the specified reference measurement channel.

## 7.3E.2Minimum requirements

When UE is configured for NR V2X reception non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.7.2 with parameters specified in Table 7.3E.2-1.

Table 7.3E.2-1: Reference sensitivity of NR V2X Bands (PC5)

Table 7.3E.2-2: Sidelink TX configuration for reference sensitivity of NR V2X Bands (PC5)

## 7.3E.2AMinimum requirements for Sidelink CA

The reference sensitivity power level REFSENS is the minimum mean power applied to each one of the UE antenna ports, at which the throughput shall meet or exceed the requirements for the specified reference measurement channel.

## 7.3E.2A.1Reference sensitivity power level for Sidelink CA

For intra-band contiguous NR SL CA operation, the reference sensitivity requirement specified in Table 7.3E.2-1 shall apply for each component carrier with all carriers active. The requirement is applied for each carrier reception when 2 carrier transmissions are activated at the same time.

For intra-band non-contiguous NR SL CA UE, the reference sensitivity requirement specified in Table 7.3E.2-1 shall apply for each sub-block with all carriers active. The requirement is applied for each sub-block reception when 2 sub-block transmissions are activated at the same time.

## 7.3E.2FMinimum requirements for Sidelink Unlicensed

## 7.3E.2F.1General

The reference sensitivity power level REFSENS is the minimum mean power applied to each one of the UE antenna ports, at which the throughput shall meet or exceed the requirements for the specified reference measurement channel.

In later clauses of Clause 7 where the value of REFSENS is used as a reference to set the corresponding requirement, the UE shall be verified against those requirements by applying the REFSENS value in Table 7.3E.2F.2-1 with 2 Rx antenna ports tested.

## 7.3E.2F.2Reference sensitivity power level

The throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.7.2 with parameters specified in Table 7.3E.2F.2-1, Table 7.3E.2F.2-2, and Table 7.3E.2F.2-3.

Table 7.3E.2F.2-1: Two antenna port reference sensitivity QPSK PREFSENS

For UE(s) equipped with 4 Rx antenna ports, reference sensitivity for 2Rx antenna ports in Table 7.3E.2F.2-1 shall be modified by the amount given in ΔRIB,4R in Table 7.3E.2F.2-2 for the applicable operating bands.

Table 7.3E.2F.2-2: Four antenna port reference sensitivity allowance ΔRIB,4R

The reference receive sensitivity (REFSENS) requirement specified in Table 7.3E.2F.2-1 and Table 7.3E.2F.2-2 shall be met with sidelink transmission bandwidth less than or equal to that specified in Table 7.3E.2F.2-3.

Table 7.3E.2F.2-3: Transmitted sidelink  configuration for reference sensitivity

Unless given by Table 7.3E.2F.2-4, the minimum requirements specified in Tables 7.3E.2F.2-1 and 7.3E.2F.2-2 shall be verified with the network signalling value NS_01 (Table 6.2F.3.1-1) configured.

Table 7.3F.2-4: Network signaling value for reference sensitivity

## 7.3E.3Reference sensitivity power level for V2X concurrent operation

## 7.3E.3.1General

When UE is configured for NR V2X reception on V2X carrier concurrent with NR uplink and downlink, NR V2X sidelink throughput for the carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.7.2 with parameters specified in Table 7.3E.2-1 and 7.3E.2-2. Also, the NR downlink throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.3 with parameters specified in Tables 7.3.2-1a, 7.3.2-1b, 7.3.2-2 and 7.3.2-3. The reference sensitivity is defined to be met with all downlink component carriers active. The REFSENS of Uu downlink and PC5 sidelink will be tested at the same time. Exceptions to reference sensitivity with different transmission and reception configurations are allowed for the combinations of aggressor and victim bands specified in Tables 7.3E.3-3 and 7.3E.3-4. The limited test configurations are specified in Tables 7.3E.3-3 and 7.3E.3-4 to verify MSD requirements.

For the intra-band concurrent NR V2X operation, the reference sensitivity power level shall be applied per carrier. The requirements in clause 7.3.2 shall be applied for NR downlink carrier and the requirements in clause 7.3E.2 shall be applied for NR sidelink carrier. NR V2X sidelink throughput for the carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.7.2. Also, the NR downlink throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.3.2 in TS38.101-1.

For reference sensitivity exception test points where the specified carrier frequency does not correspond to a valid NR-ARFCN, the closest NR-ARFCN as specified in clause 5.4.2 applies.

Table 7.3E.3-1: Void

Table 7.3E.3-2: ΔRIB,V2X (two bands)

Table 7.3E.3-3: Reference sensitivity exceptions (MSD) due to cross band isolation for inter-band concurrent operation

Table 7.3E.3-4: Reference sensitivity exceptions (MSD) due to harmonic interference for inter-band concurrent operation

## 7.3E.3FMinimum requirements for SL-U concurrent operation

## 7.3E.3F.1Reference sensitivity power level for SL-U concurrent operation

For the inter-band concurrent NR SL-U operation, the requirements specified in clause 7.3E.2F.2 shall apply for the NR sidelink reception in the operating bands in Table 5.2E.2F-1 and the requirements specified in clause 7.3.2 shall apply for the NR downlink reception in licensed band while all downlink carriers are active.

For the REFSENS exception of SL_n78-n46 inter-band concurrent NR SL-U operation, the existing CA_n46-n78 MSD requirements in Table 7.3A.5-1 are applied. Also, the existing ΔRIB of CA_n46-n78 in Table 7.3A.3.2.1-1 is applied for SL_n78-n46 inter-band concurrent NR SL-U operation UE.

## 7.3FReference sensitivity for shared spectrum channel access

## 7.3F.1General

The reference sensitivity power level REFSENS is the minimum mean power applied to each one of the UE antenna ports, at which the throughput shall meet or exceed the requirements for the specified reference measurement channel.

In later clauses of Clause 7 where the value of REFSENS is used as a reference to set the corresponding requirement, the UE shall be verified against those requirements by applying the REFSENS value in Table 7.3G.2-1 with 2 Rx antenna ports tested.

## 7.3F.2Reference sensitivity power level

The throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2.2, A3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.3F.2-1, Table 7.3F.2-2, and Table 7.3F.2-3.

Table 7.3F.2-1: Two antenna port reference sensitivity QPSK PREFSENS

For UE(s) equipped with 4 Rx antenna ports, reference sensitivity for 2Rx antenna ports in Table 7.3F.2-1 shall be modified by the amount given in ΔRIB,4R in Table 7.3F.2-2 for the applicable operating bands.

Table 7.3F.2-2: Four antenna port reference sensitivity allowance ΔRIB,4R

The reference receive sensitivity (REFSENS) requirement specified in Table 7.3F.2-1 and Table 7.3F.2-2 shall be met with uplink transmission bandwidth less than or equal to that specified in Table 7.3F.2-3.

Table 7.3F.2-3: Uplink configuration for reference sensitivity

Unless given by Table 7.3F.2-4, the minimum requirements specified in Tables 7.3F.2-1 and 7.3F.2-2 shall be verified with the network signalling value NS_01 (Table 6.2F.3.1-1) configured.

Table 7.3F.2-4: Network signaling value for reference sensitivity

## 7.3F.3Void

## 7.3F.4Void

## 7.3F.4AShared spectrum channel access CA

## 7.3F.4A.1Intra-band contiguous shared spectrum channel access CA

For intra-band contiguous carrier aggregation, the throughput of each component carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.3F.2-1, Table 7.3F.2-2, and Table 7.3F.2-3.

## 7.3F.5Void

## 7.3F.5.1Void

## 7.3F.5.2Void

## 7.3F.5.3Void

## 7.3GReference sensitivity for Tx Diversity

For UE supporting Tx diversity, the minimum requirements specified in Table 7.3.2-1a, Table 7.3.2-1b, Table 7.3.2-1d, Table 7.3.2-2, Table 7.3.2-2aa and Table 7.3.2-2a shall be met with Tx diversity configuration described in clause 6.2G.1. For Tx diversity, the parameter PUMAX is defined in clause 6.2G.4 with the sum of the output power from all UE antenna connectors.

## 7.3G.5Void

## 7.3G.5.0Void

## 7.3H(Reserved)

## 7.3IReference sensitivity for (e)RedCap

## 7.3I.1General

The reference sensitivity power level REFSENS is the minimum mean power applied to each one of the UE antenna ports for all UE categories, at which the throughput shall meet or exceed the requirements for the specified reference measurement channel.

## 7.3I.2Reference sensitivity power level for RedCap

For a RedCap UE equipped with 2 Rx antenna ports, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2.2, A3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.3.2-1a and Table 7.3.2-1b for the applicable operating bands. The reference sensitivity (REFSENS) requirement specified for a RedCap UE equipped with 2 Rx antenna ports shall be met with uplink transmission bandwidth less than or equal to that specified in Table 7.3.2-3 and, for FDD bands, with the Tx-Rx separation as defined in clause 5.4.4 for the applicable band and UE channel bandwidth.

For a power class 2 RedCap UE equipped with 2 Rx antenna ports operating in FD-FDD mode, certain degradation of the reference sensitivity in Table 7.3.2-1a is allowed. The maximum amount of degradation is specified in Table 7.3.2-1c.

For a RedCap UE equipped with 1 Rx antenna ports, reference sensitivity for 2Rx antenna ports in Table 7.3.2-1a and in Table 7.3.2-1b shall be modified by the amount given in ΔR1R in Table 7.3I.2-1 for the applicable operating bands. The reference sensitivity (REFSENS) requirement specified for a RedCap UE equipped with 1 Rx antenna ports shall be met with uplink transmission bandwidth less than or equal to that specified in Table 7.3.2-3 and, for FDD bands, with the Tx-Rx separation as defined in clause 5.4.4 for the applicable band and UE channel bandwidth.

For a power class 2 RedCap UE equipped with 2 Rx or 1 Rx antenna port(s) operating in HD-FDD mode or with TDD band, the reference sensitivity is specified in Table 7.3I.2-2 and Table 7.3I.2-3 respectively.

For a power class 2 RedCap UE equipped with 1 Rx antenna ports operating in FD-FDD mode, the reference sensitivity in Table 7.3I.2-1b shall be met with uplink transmission bandwidth less than or equal to that specified in Table 7.3.2-3.

Table 7.3I.2-1: Single antenna port reference sensitivity allowance ΔR1R

Table 7.3I.2-1b: The reference sensitivity for PC2 RedCap UE with 1 Rx antenna port operating in FD-FDD mode

For a RedCap UE equipped with 2 Rx antenna ports operating in HD-FDD mode, reference sensitivity for 2Rx antenna ports in Table 7.3I.2-2 shall be met with uplink transmission bandwidth less than or equal to that specified in Table 7.3I.2-4.

Table 7.3I.2-2: HD-FDD RedCap UE with 2 Rx antenna port reference sensitivity

For a RedCap UE equipped with 1 Rx antenna ports and operating in HD-FDD mode, reference sensitivity for 1Rx antenna ports in Table 7.3I.2-3 shall be met with uplink transmission bandwidth less than or equal to that specified in Table 7.3I.2-4.

Table 7.3I.2-3: HD-FDD RedCap UE with 1 Rx antenna port reference sensitivity

Table 7.3I.2-4: Uplink configuration for HD-FDD reference sensitivity

## 7.3I.3Reference sensitivity power level for eRedCap

For UE supporting IE supportOfERedCap-r18 and IE eRedCapNotReducedBB-BW-r18, the REFSENS requirements for RedCap UE in clause 7.3I.2 apply.

For UE supporting IE supportOfERedCap-r18 but not supporting eRedCapNotReducedBB-BW-r18, the reference sensitivity requirements for 5 MHz channel bandwidth with 15 kHz SCS defined in clause 7.3I.2 apply. These reference sensitivity requirements for 5 MHz channel bandwidth apply also for 10, 15 and 20 MHz channel bandwidths with 15 kHz SCS. In case the reference sensitivity requirements for 5 MHz channel bandwidth are not defined, the reference sensitivity requirements for 10 MHz channel bandwidth apply with the reference sensitivity level reduced by 3.2 dB, and the UL configuration shall be less than or equal to minimum between RB number specified in Table 7.3I.2-4  and 25 RBs for HD-FDD operation, and minimum between RB number specified in Table 7.3.2-3 and 25RBs otherwise. These reference sensitivity requirements for 10 MHz channel bandwidth apply also for 15 and 20 MHz channel bandwidths. Both Tx RBs in UL configuration and Rx RBs in FRC, when applicable, shall be allocated within the range from RBlow = ceil(NRB/2 - NRB_PR3/2) to RBhigh = RBlow + NRB_PR3 -1, where RBlow and RBhigh are the lowest and highest available RB position and NRB_PR3 is 25 RBs for 15 kHz SCS.

For UE supporting IE supportOfERedCap-r18 but not supporting eRedCapNotReducedBB-BW-r18, for 30 kHz SCS, the reference sensitivity requirements defined for 10 MHz channel bandwidth in clause 7.3I.2 apply with reference sensitivity level reduced by 3.0 dB and the UL configuration shall be less than or equal to minimum between RB number specified in Table 7.3I.2-4 and 12 RBs for HD-FDD operation, and minimum between RB number specified in Table 7.3.2-3 and 12RBs otherwise. These reference sensitivity requirements for 10 MHz channel bandwidth apply also for 15 and 20 MHz channel bandwidths with 30 kHz SCS. Both Tx RBs in UL configuration and Rx RBs in FRC, when applicable, shall be allocated within the range from RBlow = ceil(NRB/2 - NRB_PR3/2) to RBhigh = RBlow + NRB_PR3 -1, where RBlow and RBhigh are the lowest and highest available RB position and NRB_PR3 is 12 RBs for 30 kHz SCS.

NOTE:It is not necessary to repeat verification when same requirement applies for multiple channel bandwidths.

## 7.3JReference sensitivity for ATG

## 7.3J.1General

For ATG UE with multiple omni-directional antennas not indicating the capability antennaArrayType-r18, the reference sensitivity power level REFSENS is the minimum mean power per polarization at antenna connector, at which the throughput shall meet or exceed the requirements for the specified reference measurement channel.

For ATG UE with antenna array indicating the capability antennaArrayType-r18,the reference sensitivity power level REFSENS is the minimum mean power per polarization at TAB antenna connector, at which the throughput shall meet or exceed the requirements for the specified reference measurement channel.

## 7.3J.2Reference sensitivity power level

For a ATG UE(s) equipped with 2 Rx antenna ports, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2.2 and A.3.2 (with one sided dynamic OCNG Pattern OP.1 FDD for the DL-signal as described in Annex A.5.1.1) with parameters specified in Table 7.3.2-1a and Table 7.3.2-1b for the applicable operating bands.

For ATG UE(s) equipped with 4 Rx antenna ports, reference sensitivity for 2Rx antenna ports shall be modified by the amount given in ΔRIB,4R in Table 7.3.2-2 for the applicable operating bands.

The reference sensitivity (REFSENS) requirement for a ATG UE shall be met with uplink transmission bandwidth less than or equal to that specified in Table 7.3.2-3.

## 7.3J.2AReference sensitivity power level for ATG CA

## 7.3J.2A.1Reference sensitivity power level for ATG intra-band contiguous CA

For ATG UE intra-band contiguous carrier aggregation, the throughput of each component carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.3.2-1a, Table 7.3.2-1b, Table 7.3.2-2, Table 7.3.2-2a, and Table 7.3.2-3.

For UE(s) supporting one uplink carrier, the uplink configuration of the PCC shall be in accordance with Table 7.3.2-3 and the downlink PCC carrier center frequency shall be configured closer to uplink operating band than any of the downlink SCC center frequency.

## 7.3J.2A.2Reference sensitivity power level for ATG inter-band CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one NR band the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2.2 and A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1 with parameters specified in Table 7.3.2-1a, Table 7.3.2-1b, Table 7.3.2-2, Table 7.3.2-2a and Table 7.3.2-3. The reference sensitivity is defined to be met with all downlink component carriers active and one of the uplink carriers active. Exceptions to reference sensitivity are allowed in accordance with clause 7.3J.2A.3.

The reference sensitivity exceptions due to cross band isolation is applicable to the UL aggressor band configured with either one Tx antenna connector or two Tx antenna connectors with UL MIMO.

## 7.3J.3AΔRIB,c for ATG CA

For ATG UE supporting inter-band carrier aggregation, the minimum requirement for reference sensitivity in clause 7.3A.2 shall be increased by the amount given by ΔRIB,c defined in clause 7.3A.3.2 for the applicable operating bands. Unless otherwise stated, ΔRIB,c is set to zero.

## 7.3J.4AReference sensitivity exceptions due to cross band isolation for ATG CA

Sensitivity degradation is allowed for a band if it is impacted by UL of another band part which belongs to NR band of the same NR CA configuration due to cross band isolation issues. The reference sensitivity degradation for the victim band due to cross band isolation is specified only for the specific uplink and downlink test points specified in Table 7.3J.4A-1, and the reference sensitivity degradation values according to UL output power are specified in Table 7.3J.4A-1a.

Table 7.3J.4A-1: Reference sensitivity exceptions (MSD) and uplink/downlink configurations due to cross band isolation from an ATG UE aggressor NR UL band for NR CA in FR1

Table 7.3J.4A-1a: Reference sensitivity exceptions (MSD) and uplink/downlink configurations due to cross band isolation from an ATG UE aggressor for different NR UL output powers

## 7.3K(Reserved)

## 7.3L(Reserved)

## 7.3MReference sensitivity for LP-WUS/WUR

## 7.3M.1General

The reference sensitivity power level REFSENS is the minimum mean power applied to the UE antenna port, at which the MDR criterion with the side conditions specified in 7.1M shall be met.

## 7.3M.2Reference sensitivity power level for LP-WUS/WUR

The REFSENS for the LP-WUS/WUR shall be specified in Table 7.3M.2-1. The reference sensitivity in Table 7.3M.2-1 shall be modified by the amount given in ΔRLP-WUS in Table 7.3M.2-2 for the applicable operating bands.

Table 7.3M.2-1: Reference sensitivity for LP-WUR

Table 7.3M.2-2: Reference sensitivity allowance ΔRLP-WUS

## 7.4Maximum input level

Maximum input level is defined as the maximum mean power received at the UE antenna port, at which the specified relative throughput shall meet or exceed the minimum requirements for the specified reference measurement channel. The throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexs A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.4-1.

Table 7.4-1: Maximum input level

## 7.4AMaximum input level for CA

## 7.4A.1Maximum input level for Intra-band contiguous CA

For intra-band contiguous carrier aggregation maximum input level is defined as the maximum mean power received at the UE antenna port, over the Transmission bandwidth configuration of each CC.

The throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.4A.1-1 for each component carrier.

Table 7.4A.1-1: Maximum input level for Intra-band contiguous CA

## 7.4A.2Maximum input level for Intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, each larger than or equal to 5 MHz, the maximum input level requirements are defined with the uplink configuration in accordance with 7.3A.2.2-1. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in Table 7.4-1 and Table 7.4A.1-1 for one component carrier and two component carriers per sub-block, respectively. The throughput of each downlink component carrier shall be ≥ 95% of the maximum throughput of the specified reference measurement channel as specified in Annex A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD as described in Annex A.5.1.1 and A.5.2.1. The requirements apply with all downlink carriers active.

## 7.4A.3Maximum input level for Inter-band CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one NR band, the maximum input level is defined with the uplink active on the band(s) other than the band whose downlink is being tested. For NR CA configurations including an operating band without uplink band or an operating band with an unpaired DL part (as noted in Table 5.2-1), the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. The UE shall meet the requirements specified in clause 7.4 for each component carrier while all downlink carriers are active.

The throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexs A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD as described in Annex A.5.1.1/A.5.2.1) for each component carrier.

## 7.4BMaximum input level for NR-DC

For inter-band NR-DC configurations, the maximum input level for the corresponding inter-band CA configuration as specified in clause 7.4A applies.

## 7.4DMaximum input level for UL MIMO

For UE with multiple transmitter antenna connectors up to a maximum of four in closed-loop spatial multiplexing, the minimum requirements specified in clause 7.4 shall be met with the UL MIMO configurations described in clause 6.2D.1 and clause 6.2F.1D for shared spectrum access operation. For UL MIMO, the parameter PCMAX_L is defined as the total transmitter power over all transmit antenna connectors.

## 7.4EMaximum input level for V2X

## 7.4E.1General

Maximum input level is defined as the maximum mean power received at the UE antenna port, at which the specified relative throughput shall meet or exceed the minimum requirements for the specified reference measurement channel. When UE is configured for NR V2X reception non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.7.3 and A.7.4 with parameters specified in Table 7.4E.1-1.

Table 7.4E.1-1: Maximum input level of NR V2X

## 7.4E.1AMaximum input level for Sidelink CA

For intra-band contiguous NR SL CA operation, the following maximum input level requirement shall be applied to the SL CA bandwidth class B.

Table 7.4E.1A-1 Maximum input levels for intra-band contiguous CA UE

The throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annex A.7.3 and A.7.4. The requirements apply with all downlink carriers active.

For intra-band non-contiguous NR SL CA, the maximum input level requirements in Section 7.4E.1 will be applied to each sub-block. The throughput (>= 95% T-put) of each CC shall meet or exceed the minimum requirements for the specified reference measurement channel in A.7.3 and A.7.4. The requirements apply with all downlink carriers active.

## 7.4E.1FGeneral requirement for Sidelink Unlicensed

The maximum input level requirement of SL-U operation in clause 7.4 apply.

The throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.7.3 and A.7.4.

## 7.4E.2Maximum input level for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 7.4E.1 shall apply for the NR sidelink reception in the operating bands in Table 5.2E.2-1 and the requirements specified in clause 7.4 shall apply for the NR downlink reception in licensed band while all downlink carriers are active.

## 7.4E.2FMaximum input level for SL-U concurrent operation

For the inter-band concurrent NR SL-U operation, the requirements specified in clause 7.4E.1F shall apply for the NR sidelink reception in the operating bands in Table 5.2E.2F-1 and the requirements specified in clause 7.4 shall apply for the NR downlink reception in licensed band while all downlink carriers are active.

## 7.4F(Reserved)

## 7.4G(Reserved)

## 7.4H(Reserved)

## 7.4I(Reserved)

## 7.4JMaximum input level for ATG

## 7.4J.1General

Maximum input level is defined as the maximum mean power received at the UE antenna port, at which the specified relative throughput shall meet or exceed the minimum requirements for the specified reference measurement channel. The throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexs A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.4J.1-1.

Table 7.4J.1-1: Maximum input level for ATG

## 7.4J.2AMaximum input level for ATG CA

## 7.4J.2A.1Minimum requirement for ATG intra-band contiguous CA

For intra-band contiguous carrier aggregation maximum input level is defined as the maximum mean power received at the UE antenna port, over the Transmission bandwidth configuration of each CC.

The throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.4J.2A-1 for each component carrier.

Table 7.4J.2A-1: Maximum input level for ATG intra-band contiguous CA

## 7.4J.2A.1Minimum requirement for ATG inter-band CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one NR band, the maximum input level is defined with the uplink active on the band(s) other than the band whose downlink is being tested. For NR CA configurations including an operating band without uplink band or an operating band with an unpaired DL part (as noted in Table 5.2-1), the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. The UE shall meet the requirements specified in clause 7.4A.1 for each component carrier while all downlink carriers are active.

The throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD as described in Annex A.5.1.1/A.5.2.1) for each component carrier.

## 7.4K(Reserved)

## 7.4L(Reserved)

## 7.4MMaximum input level for LP-WUS/WUR

Maximum input level is defined as the maximum mean power received at the UE antenna connector, at which the MDR criterion shall be met with the side conditions in clause 7.1M and with parameters specified in Table 7.4M-1, and in Tables 7.4M-2a and 7.4M-2b respectively.

The UE supporting LP-WUS shall fulfil the minimum requirements specified in Table 7.4M-1 for type 1 and type 2 LP-WUR. For this requirement, a non-LP-WUS DL RB is defined as any RB in the DL transmission bandwidth configuration of the UE channel that is not occupied by the LP-WUS carrier as defined in sub-clause 5.3M.

Table 7.4M-1: Maximum input level for Type1 LR and Type2 LR

Table 7.4M-2a: Test parameters for Maximum input level for Type1 LR and Type 2 LR, case1

Table 7.4M-2b: Test parameters for Maximum input level for Type1 LR and Type 2 LR, case 2

## 7.5Adjacent channel selectivity

Adjacent channel selectivity (ACS) is a measure of a receiver's ability to receive an NR signal at its assigned channel frequency in the presence of an adjacent channel signal at a given frequency offset from the centre frequency of the assigned channel. ACS is the ratio of the receive filter attenuation on the assigned channel frequency to the receive filter attenuation on the adjacent channel(s).

The UE shall fulfil the minimum requirements specified in Table 7.5-1 for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz and the minimum requirements specified in Table 7.5-2 for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz. These requirements apply for all values of an adjacent channel interferer up to -25 dBm and for any SCS specified for the channel bandwidth of the wanted signal. However, it is not possible to directly measure the ACS; instead the lower and upper range of test parameters are chosen as in Table 7.5-3 and Table 7.5-4 for verification of the requirements specified in Table 7.5-1, and as in Table 7.5-5 and Table 7.5-6 for verification of the requirements specified in Table 7.5-2. For these test parameters, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1). For operating bands with an unpaired DL part (as noted in Table 5.2-1), the requirements only apply for carriers assigned in the paired part.

Table 7.5-1: ACS for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz

Table 7.5-2: ACS for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz

Table 7.5-3: Test parameters for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz, case 1

Table 7.5-4: Test parameters for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz, case 2

Table 7.5-5: Test parameters for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz, case 1

Table 7.5-6: Test parameters for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz, case 2

## 7.5AAdjacent channel selectivity for CA

## 7.5A.1Adjacent channel selectivity for Intra-band contiguous CA

For intra-band contiguous carrier aggregation the downlink SCC(s) shall be configured at nominal channel spacing to the PCC. The UE shall fulfil the minimum requirement specified in Table 7.5A.1-1 and 7.5A.1-1a for an adjacent channel interferer on either side of the aggregated downlink signal at a specified frequency offset and for an interferer power up to -25 dBm.

The throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Tables 7.5A.1-2, 7.5A.1-2a, 7.5A.1-3 and 7.5A.1-3a.

Table 7.5A.1-1: ACS for intra-band contiguous CA with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz

Table 7.5A.1-1a: ACS for intra-band contiguous CA with FDL_high < 2700 MHz and FUL_high < 2700 MHz

Table 7.5A.1-2: Test parameters for intra-band contiguous CA with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz, case 1

Table 7.5A.1-2a: Test parameters for intra-band contiguous CA with FDL_high<2700 MHz and FUL_high<2700 MHz, case 1

Table 7.5A.1-3: Test parameters for intra-band contiguous CA with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz, case 2

Table 7.5A.1-3a: Test parameters for intra-band contiguous CA with FDL_high <2700 MHz and FUL_high<2700 MHz, case 2

## 7.5A.2Adjacent channel selectivity Intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation with FDL_high < 2700 MHz and FUL_high < 2700 MHz with one uplink carrier and two or more downlink sub-blocks, each larger than or equal to 5 MHz, the adjacent channel selectivity requirements are defined with the uplink configuration in accordance with Table 7.3A.2.2-1. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in clauses 7.5 and 7.5A.1 for one component carrier and two component carriers per sub-block, respectively. The UE shall fulfil the minimum requirements all values of a single adjacent channel interferer in-gap and out-of-gap up to a –25 dBm interferer power while all downlink carriers are active. For the lower range of test parameters (Case 1), the interferer power Pinterferer  shall be set to the maximum of the levels given by the carriers of the respective sub-blocks as specified in Table 7.5-3 and Table 7.5A.1-2a for one component carrier and two component carriers per sub-block, respectively. The wanted signal power levels for the carriers of each sub-block shall then be adjusted relative to Pinterferer  in accordance with the ACS requirement for each sub-block (Table 7.5-1 and Table 7.5A.1-1a). For the upper range of test parameters (Case 2) for which the interferer power Pinterferer  is -25 dBm (Table 7.5-4 and Table 7.5A.1-3a) the wanted signal power levels for the carriers of each sub-block shall be adjusted relative to Pinterferer  like for Case 1.

For intra-band non-contiguous carrier aggregation with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz with one uplink carrier and two or more downlink sub-blocks, each larger than or equal to 5 MHz, the adjacent channel selectivity requirements are defined with the uplink configuration in accordance with Table 7.3A.2.2-1. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in clauses 7.5 and 7.5A.1 for one component carrier and two component carriers per sub-block, respectively. The UE shall fulfil the minimum requirements all values of a single adjacent channel interferer in-gap and out-of-gap up to a –25 dBm interferer power while all downlink carriers are active. For the lower range of test parameters (Case 1), the interferer power Pinterferer  shall be set to the maximum of the levels given by the carriers of the respective sub-blocks as specified in Table 7.5-5 and Table 7.5A.1-2 for one component carrier and two component carriers per sub-block, respectively. The wanted signal power levels for the carriers of each sub-block shall then be adjusted relative to Pinterferer  in accordance with the ACS requirement for each sub-block (Table 7.5-2 and Table 7.5A.1-1). For the upper range of test parameters (Case 2) for which the interferer power Pinterferer  is -25 dBm (Table 7.5-6 and Table 7.5A.1-3) the wanted signal power levels for the carriers of each sub-block shall be adjusted relative to Pinterferer  like for Case 1.

The throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

## 7.5A.3Adjacent channel selectivity Inter-band CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one NR band, the adjacent channel requirements are defined with the uplink active on the band(s) other than the band whose downlink is being tested. For NR CA configurations including an operating band without uplink operation or an operating band with an unpaired DL part (as noted in Table 5.2-1), the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. The UE shall meet the requirements specified in clause 7.5 and clause 7.5F when the downlink belongs to a spectrum sharing defined band, for each component carrier while all downlink carriers are active.

The throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

## 7.5BAdjacent channel selectivity for NR-DC

For inter-band NR-DC configurations, the adjacent channel selectivity for the corresponding inter-band CA configuration as specified in clause 7.5A applies.

## 7.5DAdjacent channel selectivity for UL MIMO

For UE(s) with multiple transmitter antenna connectors up to a maximum of four in closed-loop spatial multiplexing scheme, the minimum requirements specified in clause 7.5 shall be met with the UL MIMO configurations described in clause 6.2D.1 and clause 6.2F.1D for shared spectrum access operation. For UL MIMO, the parameter PCMAX_L is defined as the total transmitter power over all transmit antenna connectors.

## 7.5EAdjacent channel selectivity for V2X

## 7.5E.1General

Adjacent channel selectivity (ACS) is a measure of a receiver's ability to receive an NR signal at its assigned channel frequency in the presence of an adjacent channel signal at a given frequency offset from the centre frequency of the assigned channel. ACS is the ratio of the receive filter attenuation on the assigned channel frequency to the receive filter attenuation on the adjacent channel(s).

The UE shall fulfil the minimum requirements specified in Table 7.5E.1-1 for NR V2X UE. These requirements apply for all values of an adjacent channel interferer up to -25 dBm and for any SCS specified for the channel bandwidth of the wanted signal. However, it is not possible to directly measure the ACS; instead the lower and upper range of test parameters are chosen as in Table 7.5E.1-2 and Table 7.5E.1-3 for verification of the requirements specified in Table 7.5E.1-1. For these test parameters, when UE is configured for NR V2X reception non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.7.2.

In licensed band, the minimum requirements shall reuse the same ACS values with NR UE.

Table 7.5E.1-1: Adjacent channel selectivity for NR V2X

Table 7.5E.1-2: Test parameters for Adjacent channel selectivity for V2X, Case 1

Table 7.5E.1-2a: Test parameters for Adjacent channel selectivity in n14, Case 1

Table 7.5E.1-3: Test parameters for Adjacent channel selectivity for V2X, Case 2

Table 7.5E.1-3a: Test parameters for Adjacent channel selectivity in n14, Case 2

## 7.5E.1AAdjacent channel selectivity requirement for Sidelink CA

For intra-band contiguous NR SL CA operation, the UE shall fulfil the minimum requirement specified in Table 7.5E.1A-1 to Table 7.5E.1A-3 where the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.7.2.

Table 7.5E.1A-1 ACS for intra-band contiguous NR SL CA UE

Table 7.5E.1A-2 Test parameters for intra-band contiguous SL CA UE, case 1

Table 7.5E.1A-3 Test parameters for intra-band contiguous SL CA UE, case 2

For intra-band non-contiguous NR SL CA, the UE shall fulfil the minimum requirement specified in Table 7.5E.1-1 to Table 7.5E.1-3 per sub-block where the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.7.2.

For the ACS requirement, the UE shall meet the requirements for each sub-block as specified in clauses 7.5E for one component carrier per sub-block. The UE shall fulfil the minimum requirements all values of a single adjacent channel interferer in-gap and out-of-gap up to a –25 dBm interferer power while all sidelink carriers are active. For the lower range of test parameters (Case 1), the interferer power Pinterferer shall be set to the maximum of the levels given by the carriers of the respective sub-blocks as specified in Table 7.5E-2 for one component carrier per sub-block. The wanted signal power levels for the carriers of each sub-block shall then be adjusted relative to Pinterferer in accordance with the ACS requirement for each sub-block (Table 7.5E-1). For the upper range of test parameters (Case 2) for which the interferer power Pinterferer is -25 dBm (Table 7.5E-3) the wanted signal power levels for the carriers of each sub-block shall be adjusted relative to Pinterferer like for Case 1.

## 7.5E.1FGeneral requirement for Sidelink Unlicensed

The ACS requirement of SL-U operation in clause 7.5F.1 apply.

The throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.7.2.

## 7.5E.2Adjacent channel selectivity for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 7.5E.1 shall apply for the NR sidelink reception in the operating bands in Table 5.2E.2-1 and the requirements specified in clause 7.5 shall apply for the NR downlink reception in licensed band while all downlink carriers are active.

## 7.5E.2FAdjacent channel selectivity for SL-U concurrent operation

For the inter-band concurrent NR SL-U operation, the requirements specified in clause 7.5E.1F shall apply for the NR sidelink reception in the operating bands in Table 5.2E.2F-1 and the requirements specified in clause 7.5 shall apply for the NR downlink reception in licensed band while all downlink carriers are active.

## 7.5FAdjacent channel selectivity for shared spectrum channel access

## 7.5F.1General

Adjacent channel selectivity (ACS) is a measure of a receiver's ability to receive an NR signal at its assigned channel frequency in the presence of an adjacent channel signal at a given frequency offset from the centre frequency of the assigned channel. ACS is the ratio of the receive filter attenuation on the assigned channel frequency to the receive filter attenuation on the adjacent channel(s).

Instead of the general ACS requirements specified in clause 7.5, the UE shall fulfil the minimum requirements specified in Table 7.5F.1-1. These requirements apply for any SCS specified for the channel bandwidth of the wanted signal.  For the test parameters specified in Table 7.5F.1-2, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

Table 7.5F.1-1: ACS for shared spectrum channel access bands

Table 7.5F.1-2: Test parameters for shared spectrum channel access bands

## 7.5F.1AAdjacent channel selectivity for shared spectrum channel access CA

## 7.5F.1A.1Intra-band contiguous shared spectrum channel access CA

ACS for intra-band contiguous shared access CA requirements are specified in Table 7.5F.1A.1-1.  These requirements apply for any SCS specified for the channel bandwidth of the wanted signal.  For the test parameters specified in Table 7.5F.1A.1-2, the throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

Table 7.5F.1A.1-1: ACS for intra-band contiguous shared access CA

Table 7.5F.1A.1-2: Test parameters for intra-band contiguous NR-U CA

## 7.5F.2Void

## 7.5G(Reserved)

## 7.5H(Reserved)

## 7.5I(Reserved)

## 7.5JAdjacent channel selectivity for ATG

## 7.5J.1General

Adjacent channel selectivity (ACS) is a measure of a receiver's ability to receive an NR signal at its assigned channel frequency in the presence of an adjacent channel signal at a given frequency offset from the centre frequency of the assigned channel. ACS is the ratio of the receive filter attenuation on the assigned channel frequency to the receive filter attenuation on the adjacent channel(s).

The UE shall fulfil the minimum requirements specified in Table 7.5J.1-1 for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz and the minimum requirements specified in Table 7.5J.1-2 for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz. These requirements apply for all values of an adjacent channel interferer up to -42 dBm with omni-directional antenna and -30dBm with antenna array for any SCS specified for the channel bandwidth of the wanted signal. However, it is not possible to directly measure the ACS; instead the lower and upper range of test parameters are chosen as in Table 7.5J.1-3 and Table 7.5J.1-4 for verification of the requirements specified in Table 7.5J.1-1, and as in Table 7.5J.1-5 and Table 7.5J,1-6 for verification of the requirements specified in Table 7.5J.1-2. For these test parameters, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

Table 7.5J.1-1: ACS for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz

Table 7.5J.1-2: ACS for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz

Table 7.5J.1-3: Test parameters for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz, case 1

Table 7.5J.1-4: Test parameters for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz, case 2

Table 7.5J.1-5: Test parameters for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz, case 1

Table 7.5J.1-6: Test parameters for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz, case 2

## 7.5J.2AAdjacent channel selectivity for ATG CA

## 7.5J.2A.1Minimum requirement for ATG intra-band contiguous CA

For intra-band contiguous carrier aggregation the downlink SCC(s) shall be configured at nominal channel spacing to the PCC. The UE shall fulfil the minimum requirement specified in Table 7.5J.2A.1-1 for an adjacent channel interferer on either side of the aggregated downlink signal at a specified frequency offset and for an interferer power up to -42 dBm for omni-directional antenna or -30dBm for antenna array.

The throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Tables 7.5J.2A.1-2 and 7.5J.2A.1-3.

Table 7.5J.2A.1-1: ACS for ATG intra-band contiguous CA with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz

Table 7.5J.2A.1-2: Test parameters for ATG intra-band contiguous CA with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz, case 1

Table 7.5J.2A.1-3: Test parameters for ATG intra-band contiguous CA with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz, case 2

## 7.5J.2A.2Minimum requirement for ATG inter-band contiguous CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one NR band, the adjacent channel requirements are defined with the uplink active on the band(s) other than the band whose downlink is being tested. For NR CA configurations including an operating band without uplink operation or an operating band with an unpaired DL part (as noted in Table 5.2-1), the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. The UE shall meet the requirements specified in clause 7.5J.1 for each component carrier while all downlink carriers are active.

The throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

## 7.5K(Reserved)

## 7.5L(Reserved)

## 7.5MAdjacent channel and subcarrier selectivity for LP-WUS/WUR

## 7.5M.1General

This clause specifies the requirements for Adjacent channel selectivity (ACS) and Adjacent subcarrier selectivity (ASCS) for LP-WUS/WUR.

## 7.5M.2Adjacent channel selectivity for LP-WUS/WUR

The adjacent channel selectivity (ACS) is a measure of a receiver’s ability to receive an LP-WUS signal at its configured RBs inside the configured channel, in the presence of an adjacent channel signal at a given frequency offset from the centre frequency of the configured channel. ACS is the ratio of the receive filter attenuation on the LP-WUS frequency to the receive filter attenuation on the adjacent channel(s).

The UE shall fulfil the minimum requirements specified in Table 7.5M.2-1 for Type 1 LR and Type 2 LR respectively.

These requirements apply for any SCS specified in table 5.3M.2-1. The requirement in table 7.5M.2-1 shall be verified for each set of test parameters in Table 7.5M.2-2 and Table 7.5M.2-3, respectively. For these parameters, the MDR criterion in clause 7.1M shall be met with the side conditions in clause 7.1M. In this requirement, guard RBs for ACS are adjacent to the LP-WUS and located between the LPWUS and the interferer.

Table 7.5M.2-1: ACS requirement

Table 7.5M.2-2: Test parameters, case 1

Table 7.5M.2-3: Test parameters for case 2

## 7.5M.3Adjacent subcarrier selectivity for LP-WUS/WUR

Adjacent subcarrier selectivity (ASCS) is a measure of a receiver’s ability to receive the LP-WUS on the assigned subcarriers in the presence of fully populated NR signal at all adjacent subcarriers. ASCS is the ratio of the receiver filter attenuation on the LP-WUS RBs to the receiver filter attenuation on the adjacent subcarriers.

The UE shall fulfil the minimum requirements specified in Table 7.5M.3-1 and 7.5M.3-2.

Table 7.5M.3-1: ASCS test parameters for Type-1 LR

Table 7.5M.3-2: ASCS test parameters for Type-2 LR

## 7.6Blocking characteristics

## 7.6.1General

The blocking characteristic is a measure of the receiver's ability to receive a wanted signal at its assigned channel frequency in the presence of an unwanted interferer on frequencies other than those of the spurious response or the adjacent channels, without this unwanted input signal causing a degradation of the performance of the receiver beyond a specified limit. The blocking performance shall apply at all frequencies except those at which a spurious response occurs.

For shared spectrum channel access and band combinations with operating bands intended for shared spectrum channel access, the blocking characteristics is specified in clause 7.6F.

## 7.6.2In-band blocking

For NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz in-band blocking (IBB) is defined for an unwanted interfering signal falling into the UE receive band or into the first 15 MHz below or above the UE receive band.  The throughput of the wanted signal shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.6.2-1 and Table 7.6.2-2. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal. For operating bands with an unpaired DL part (as noted in Table 5.2-1), the requirements only apply for carriers assigned in the paired part.

Table 7.6.2-1: In-band blocking parameters for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz

Table 7.6.2-2: In-band blocking for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz

NOTE:For bands n100 and n101, additional requirements for wideband cab-radio receiver are specified by ETSI TC RT based on ECC Decision (20)02 [19].

For NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz in-band blocking (IBB) is defined for an unwanted interfering signal falling into the UE receive band or into an immediately adjacent frequency range up to 3*BWChannel below or above the UE receive band where BWChannel is the bandwidth of the wanted signal. The throughput of the wanted signal shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1)] with parameters specified in Table 7.6.2-3 and Table 7.6.2-4. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal.

Table 7.6.2-3: In-band blocking parameters for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz

Table 7.6.2-4: In-band blocking for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz

## 7.6.3Out-of-band blocking

For NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz out-of-band band blocking is defined for an unwanted CW interfering signal falling outside a frequency range 15 MHz below or above the UE receive band. The throughput of the wanted signal shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.6.3-1 and Table 7.6.3-2. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal. For operating bands with an unpaired DL part (as noted in Table 5.2-1), the requirements only apply for carriers assigned in the paired part.

Table 7.6.3-1: Out-of-band blocking parameters for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz

Table 7.6.3-2: Out of-band blocking for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz

NOTE:For bands n100 and n101, additional requirements for wideband cab-radio receiver are specified by ETSI TC RT based on ECC Decision (20)02 [19].

For interferer frequencies across ranges 1, 2 and 3 in Table 7.6.3-2, a maximum of

exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a step size of  MHz withthe number of resource blocks in the downlink transmission bandwidth configuration, BWChannel the bandwidth of the frequency channel in MHz and n = 1, 2, 3 for SCS = 15, 30, 60 kHz, respectively. For these exceptions, the requirements in clause 7.7 apply.

For NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz out-of-band band blocking is defined for an unwanted CW interfering signal falling outside a frequency range up to 3*BWChannel below or from 3*BWChannel above the UE receive band, where BWChannel is the channel bandwidth. The throughput of the wanted signal shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.6.3-3 and Table 7.6.3-4. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal.

Table 7.6.3-3: Out-of-band blocking parameters for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz

Table 7.6.3-4: Out of-band blocking for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz

For interferer frequencies across ranges 1, 2 and 3 in Table 7.6.3-4, a maximum of

exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a step size of  MHz withthe number of resource blocks in the downlink transmission bandwidth configuration, BWChannel the bandwidth of the frequency channel in MHz and n = 1, 2, 3 for SCS = 15, 30, 60 kHz, respectively. For these exceptions, the requirements in clause 7.7 apply.

## 7.6.4Narrow band blocking

This requirement is measure of a receiver's ability to receive a NR signal at its assigned channel frequency in the presence of an unwanted narrow band CW interferer at a frequency, which is less than the nominal channel spacing.

The relative throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.6.4-1. For operating bands with an unpaired DL part (as noted in Table 5.2-1), the requirements only apply for carriers assigned in the paired part.

Table 7.6.4-1: Narrow Band Blocking

NOTE:For bands n100 and n101, additional requirements for wideband cab-radio receiver are specified by ETSI TC RT based on ECC Decision (20)02 [19].

## 7.6ABlocking characteristics for CA

## 7.6A.1General

## 7.6A.2In-band blocking for CA

## 7.6A.2.1In-band blocking for Intra-band contiguous CA

For intra-band contiguous carrier aggregation the downlink SCC(s) shall be configured at nominal channel spacing to the PCC. The UE shall fulfil the minimum requirement specified in Table 7.6A.2.1-1 and 7.6A.2.1-1a for an adjacent channel interferer on either side of the aggregated downlink signal at a specified frequency offset and for an interferer power up to -25 dBm. The throughput of each carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

Table 7.6A.2.1-1: In-band blocking parameters for intra-band contiguous CA with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz

Table 7.6A.2.1-1a: In-band blocking parameters for intra-band contiguous CA with FDL_low < 2700 MHz and FUL_low < 2700 MHz

Table 7.6A.2.1-2: In-band blocking for intra-band contiguous CA  with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz

Table 7.6A.2.1-2a: In-band blocking for intra-band contiguous CA with FDL_low  < 2700 MHz and FUL_low  < 2700 MHz

## 7.6A.2.2In-band blocking for Intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, each larger than or equal to 5 MHz, the in-band blocking requirements are defined with the uplink configuration in accordance with Table 7.3A.2.2-1. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in clause 7.6.2 and 7.6A.2.1 for one component carrier and two component carriers per sub-block, respectively. The requirements apply for in-gap and out-of-gap interferers while all downlink carriers are active.

The throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

## 7.6A.2.3In-band blocking for Inter-band CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one NR band, the in-band blocking requirements are defined with the uplink active on the band(s) other than the band whose downlink is being tested. The UE shall meet the requirements specified in clause 7.6.2 and clause 7.6F.2 when the downlink belongs to a spectrum sharing defined band, for each component carrier while all downlink carriers are active.

For the UE which supports inter-band CA configuration in Table 7.3A.3.2.1-1, Pinterferer power defined in Table 7.6.2-2 and 7.6.2-4, and Table 7.6F.2.1-2 for shared spectrum channel access, is increased by the amount given by ΔRIB,c in Table 7.3A.3.2.1-1 and in Table 7.3F.3-1 for shared spectrum channel access.

For NR CA configurations including an operating band without uplink operation or an operating band with an unpaired DL part (as noted in Table 5.2-1), the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. The requirements for the component carrier configured in the operating band without uplink operation are specified in clause 7.6.2 while all downlink carriers are active.

Table 7.6A.2.3-1: Void

The throughput of each carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

## 7.6A.3Out-of-band blocking for CA

## 7.6A.3.1Out-of-band blocking for Intra-band contiguous CA

For intra-band contiguous carrier aggregation the downlink SCC(s) shall be configured at nominal channel spacing to the PCC. For FDD, the PCC shall be configured closest to the uplink band. All downlink carriers shall be active throughout the test.

The UE shall fulfil the minimum requirement in presence of an interfering signal specified in Table 7.6A.3-1 and Table 7.6A.3-2 being on either side of the aggregated signal. The throughput of each carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

Table 7.6A.3-1: Out-of-band blocking parameters for intra-band contiguous CA

Table 7.6A.3-1a: Void

Table 7.6A.3-2: Out of-band blocking for intra-band contiguous CA

Table 7.6A.3-2a: Void

For interferer frequencies across ranges 1, 2 and 3 in Table 7.6A.3-2, a maximum of

exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a step size of  MHz with  the number of resource blocks in the downlink transmission bandwidth configuration,  BWChannel is the bandwidth of the frequency channel in MHz and n = 1, 2, 3 for SCS = 15, 30, 60 kHz, respectively. For these exceptions, the requirements in subclause 7.7A.1 apply.

## 7.6A.3.2Out-of-band blocking for Intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, the out-of-band blocking requirements are defined with the uplink configuration in accordance with Table 7.3A.2.2-1. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in clauses 7.6.3 and 7.6A.3.1 for one component carrier and two component carriers per sub-block, respectively. The requirements apply with all downlink carriers active.

The throughput of each carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

## 7.6A.3.3Out-of-band blocking for Inter-band CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one NR band, the out-of-band blocking requirements are defined with the uplink active on the band(s) other than the band whose downlink is being tested. For NR CA configurations including an operating band without uplink band or an operating band with an unpaired DL part (as noted in Table 5.2-1), the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. The UE shall meet the requirements specified in clause 7.6.3 for each component carrier while all downlink carriers are active.

For inter-band carrier aggregation with component carriers in operating bands < 2.7GHz including n48, and for FDL_Low(j) – 15 MHz ≤ f ≤ FDL_High(j) + 15 MHz, the appropriate adjacent channel selectivity and in-band blocking requirements in the respective clauses 7.5 and 7.6.2 shall be applied for carrier j. For inter-band carrier aggregation with component carriers in operating bands > 2.7GHz excluding n48, and for FDL_Low(j) – 3* BWchannel ≤ f ≤ FDL_High(j) + 3* BWchannel, the appropriate adjacent channel selectivity and in-band blocking requirements in the respective clauses 7.5 and 7.6.2 shall be applied for carrier j. FDL_Low(j) and FDL_High(j) denote the respective lower and upper frequency limits of the operating band containing carrier j, j = 1,…,X, with carriers numbered in increasing order of carrier frequency and X the number of component carriers in the band combination. BWchannel denotes the channel bandwidth of the wanted signal component carrier j. If CW interferer falls in a gap between FDL_High(j) and FDL_Low(j+1) where the corresponding OOB ranges 1 and 2 overlap, then the lower level interferer limit of the overlapping OOB ranges applies.

If FDL_high of the lower NR band is greater than or equal to the FDL_low of the another upper NR band as in overlapping RX frequency ranges, then the OOB range shall start from the FDL_low of the lower NR band, and from the FDL_high of the upper NR band.

For inter-band carrier aggregation with uplink assigned to two NR bands, the out-of-band blocking requirements specified in clause 7.6.3 shall be met with the transmitter power for the uplink set to 7 dB below PCMAX_L,f,c  for each serving cell c.

For the UE which supports inter-band CA configuration in Table 7.3A.3.2.1-1, Pinterferer power defined in Table 7.6.3-2 and 7.6.3-4 and Table 7.6F.3.2-2 for shared spectrum channel access, is increased by the amount given by ΔRIB,c in Table 7.3A.3.2.1-1 and in Table 7.3F.3-1 for shared spectrum channel access.

For inter-band CA combination listed in Table 7.6A.3.3-1, exceptions to the requirement specified in Table 7.6A.3.3-2 are allowed when the second order intermodulation product of the lower frequency band UL carrier and the CW interfering signal fully or partially overlaps with the higher frequency band DL carrier. Unless otherwise stated, the exceptions apply to any power classes for the listed inter-band CA combinations.

Table 7.6A.3.3-1: CA band combination with exceptions allowed

Table 7.6A.3.3-1a: Void

Table 7.6A.3.3-2: Requirement for out-of-band blocking exceptions

For all interferer frequency ranges specified in clause 7.6.3 a maximum of

exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a step size of   MHz with NRB the number of resource blocks in the downlink transmission bandwidth configuration, BWChannel the bandwidth of the frequency channel in MHz and n = 1, 2, 3 for SCS = 15, 30, 60 kHz, respectively. For these exceptions, the requirements in clause 7.7 apply.

The throughput of each carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

## 7.6A.4Narrow band blocking for CA

## 7.6A.4.1Narrow band blocking for Intra-band contiguous CA

For intra-band contiguous carrier aggregation, the downlink SCC(s) shall be configured at nominal channel spacing to the PCC. For FDD, the PCC shall be configured closest to the uplink band. All downlink carriers shall be active throughout the test. The uplink output power shall be set as specified in Table 7.6A.4.1-1 with the uplink configuration. For UE(s) supporting one uplink, the uplink configuration of the PCC shall be in accordance with Table 7.3.2-3. The UE shall fulfil the minimum requirement in presence of an interfering signal specified in Table 7.6A.4.1-1 being on either side of the aggregated signal. The throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.6A.4.1-1.

Table 7.6A.4.1-1: Narrow-band blocking for intra-band contiguous CA

## 7.6A.4.2Narrow band blocking for Intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation with FDL_low < 2700 MHz and FUL_low < 2700 MHz with one uplink carrier and two or more downlink sub-blocks, the narrow band blocking requirements are defined with the uplink configuration in accordance with Table 7.3A.2.2-1. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in clauses 7.6.4 and 7.6A.4.1 for one component carrier and two component carriers per sub-block, respectively. The requirements apply for in-gap and out-of-gap interferers while all downlink carriers are active.

The throughput of each carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

## 7.6A.4.3Narrow band blocking for Inter-band CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one NR band, the narrow band blocking requirements are defined with the uplink active on the band(s) other than the band whose downlink is being tested. For NR CA configurations including an operating band without uplink band or an operating band with an unpaired DL part (as noted in Table 5.2-1), the requirements for all downlinks shall be met with the single uplink carrier active in each band capable of UL operation. The UE shall meet the requirements specified in clause 7.6.4 for each component carrier while all downlink carriers are active.

For the UE which supports inter-band CA configuration in Table 7.3A.3.2.1-1, PUW power defined in Table 7.6.4-1 is increased by the amount given by ΔRIB,c in Table 7.3A.3.2.1-1.

The throughput of each carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

## 7.6BBlocking characteristics for NR-DC

For inter-band NR-DC configurations, the blocking characteristics for the corresponding inter-band CA configuration as specified in clause 7.6A applies.

## 7.6CBlocking characteristics for SUL

## 7.6C.1General

## 7.6C.2In-band blocking for SUL

For SUL operation, the in-band blocking requirement for downlink bands specified in clause 7.6.2 shall be met.

For SUL operation with downlink CA, the in-band blocking requirement for downlink bands specified in clause 7.6A.2 shall be met.

## 7.6C.3Out-of-band blocking for SUL

For SUL operation, the out-of-band blocking requirement for downlink bands specified in clause 7.6.3 shall be met. For SUL operation with downlink CA, the out-of-band blocking requirement for downlink bands specified in clause 7.6A.3 shall be met. For operation band combination listed in Table 7.6C.3-1, exceptions to the requirement specified in Table 7.6C.3-2 are allowed when the second order intermodulation product of the SUL carrier and the CW interfering signal fully or partially overlaps with the DL carrier.

Table 7.6C.3-1: SUL operating band combination with exceptions allowed

Table 7.6C.3-2: Requirement for out-of-band blocking exceptions

For all interferer frequency ranges specified in clause 7.6.3 a maximum of

exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a step size of MHz with NRB the number of resource blocks in the downlink transmission bandwidth configuration, BWChannel the bandwidth of the frequency channel in MHz and n = 1, 2, 3 for SCS = 15, 30, 60 kHz, respectively. For these exceptions, the requirements in clause 7.7 apply.

## 7.6C.4Narrow band blocking for SUL

Narrow band blocking is not specified for SUL band combination.

## 7.6DBlocking characteristics for UL MIMO

For UE with multiple transmitter antenna connectors up to a maximum of four in closed-loop spatial multiplexing scheme, the minimum requirements specified in clause 7.6 shall be met with the UL MIMO configurations described in clause 6.2D.1 and in clause 6.2F.1D for shared spectrum access operation. For UL MIMO, the parameter PCMAX_L is defined as the total transmitter power over all transmit antenna connectors.

## 7.6EBlocking characteristics for V2X

## 7.6E.1General

The blocking characteristic is a measure of the receiver's ability to receive a wanted signal at its assigned channel frequency in the presence of an unwanted interferer on frequencies other than those of the spurious response or the adjacent channels, without this unwanted input signal causing a degradation of the performance of the receiver beyond a specified limit. The blocking performance shall apply at all frequencies except those at which a spurious response occurs.

## 7.6E.2In-band blocking

## 7.6E.2.1General

When UE is configured for NR V2X reception non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, the throughput of the wanted signal shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annex A.7.2 with parameters specified in Table 7.6E.2.1-1 and Table 7.6E.2.1-2. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal.

Table 7.6E.2.1-1: In-band blocking parameters for NR V2X

Table 7.6E.2.1-1a: In-band blocking parameters in n14

Table 7.6E.2.1-2: In-band blocking for NR V2X

## 7.6E.2.1AIn-band blocking for Sidelink CA

For intra-band contiguous SL CA operation, the UE shall fulfil the minimum requirement specified in Table 7.6E.2.1A-1 to Table 7.6E.2.1A-2 where the throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.7.2.

Table 7.6E.2.1A-1 In-band blocking parameters for intra-band contiguous SL CA UE

Table 7.6E.2.1A-2 In-band blocking for intra-band contiguous SL CA UE

For intra-band non-contiguous SL CA operation, the UE shall meet the requirements for each sub -block as specified in clause 7.6E.2 for one component carrier per sub-block. The requirements apply for in-gap and out-of-gap interferers while all sidelink carriers are active. The UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.7.2 with the test parameters defined in clause 7.6E.2.1 per sub-block while all downlink carriers are active.

## 7.6E.2.2In-band blocking for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 7.6E.2.1 shall apply for the NR sidelink reception in the operating bands in Table 5.2E.2-1 and the requirements specified in clause 7.6.2 shall apply for the NR downlink reception in licensed band while all downlink carriers are active.

## 7.6E.2.2FIn-band blocking for SL-U concurrent operation

For the inter-band concurrent NR SL-U operation, the requirements specified in clause 7.6E.2F shall apply for the NR sidelink reception in the operating bands in Table 5.2E.2F-1 and the requirements specified in clause 7.6.2 shall apply for the NR downlink reception in licensed band while all downlink carriers are active.

## 7.6E.3Out-of-band blocking

## 7.6E.3.1General

For NR V2X bands out-of-band band blocking is defined for an unwanted CW interfering signal falling outside a frequency range 30 MHz below or above the UE receive band. When UE is configured for NR V2X reception non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, the throughput of the wanted signal shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.7.2 with parameters specified in Table 7.6E.3.1-1 and Table 7.6E.3.1-2. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal.

For interferer frequencies across ranges 1, 2 and 3 in Table 7.6E.3.1-2, a maximum of

exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a step size of MHz with NRB the number of resource blocks in the transmission bandwidth configuration, BWChannel the bandwidth of the frequency channel in MHz and n = 1, 2, 3 for SCS = 15, 30, 60 kHz, respectively. For these exceptions, the requirements in clause 7.7E.1 apply.

Table 7.6E.3.1-1: Out-of-band blocking parameters for NR V2X

Table 7.6E.3.1-2: Out of-band blocking for NR V2X

## 7.6E.3.1AOut-of-band blocking for Sidelink CA

For intra-band contiguous SL CA operation, the UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.7.2 with parameters specified in Tables 7.6E.3.1A-1 and 7.6E.3.1A-2.

For interferer frequencies across ranges 1, 2 and 3 in Table 7.6E.3.1A-2, a maximum of

exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a step size of MHz with NRB the number of resource blocks in the transmission bandwidth configuration, BWChannel the bandwidth of the frequency channel in MHz and n = 1, 2, 3 for SCS = 15, 30, 60 kHz, respectively. For these exceptions, the requirements in clause 7.7E.1A apply.

Table 7.6E.3.1A-1: Out-of-band blocking parameters for intra-band contiguous SL CA UE

Table 7.6E.3.1A-2: Out of band blocking for intra-band contiguous SL CA UE

For intra-band non-contiguous SL CA operation, the UE shall meet the requirements for each sub-block as specified in clauses 7.6E.3 for one component carrier per sub-block, respectively. The requirements apply with all sidelink carriers active. The UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.7.2 with test parameters defined in clause 7.6E.3.1 per sub-block while all downlink carriers are active.

## 7.6E.3.2Out-of-band blocking for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 7.6E.3.1 shall apply for the NR sidelink reception in Band n47 and the requirements specified in clause 7.6.3 shall apply for the NR downlink reception in licensed band while all downlink carriers are active.

## 7.6E.3.2FOut-of-band blocking for SL-U concurrent operation

For the inter-band concurrent NR SL-U operation, the requirements specified in clause 7.6E.3F shall apply for the NR sidelink reception in the operating bands in Table 5.2E.2F-1 and the requirements specified in clause 7.6.3 shall apply for the NR downlink reception in licensed band while all downlink carriers are active.

## 7.6E.3FOut-of-band blocking for Sidelink Unlicensed

Out-of-band band blocking is defined for an unwanted CW interfering signal falling outside a frequency range 60 MHz or greater below or above the UE receive band. The throughput of the wanted signal shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex 7.2 with parameters specified in Table 7.6F.3.1-1 and Table 7.6F.3.1-2. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal.

## 7.6FBlocking characteristics for shared spectrum channel access

## 7.6F.1General

The blocking characteristic is a measure of the receiver's ability to receive a wanted signal at its assigned channel frequency in the presence of an unwanted interferer on frequencies other than those of the spurious response or the adjacent channels, without this unwanted input signal causing a degradation of the performance of the receiver beyond a specified limit. The blocking performance shall apply at all frequencies except those at which a spurious response occurs.

## 7.6F.2In-band blocking

## 7.6F.2.1General

In-band blocking (IBB) is defined for an unwanted interfering signal falling into the UE receive band or into the first 60 MHz below or above the UE receive band.  The throughput of the wanted signal shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.6F.2.1-1 and Table 7.6F.2.1-2. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal.

Table 7.6F.2.1-1: In-band blocking parameters for shared access bands

Table 7.6F.2.1-2: In-band blocking for shared access bands

## 7.6F.2.2Void

## 7.6F.2AIn-band blocking for shared spectrum CA

## 7.6F.2A.1Intra-band contiguous shared spectrum channel access CA

In-band blocking for intra-band contiguous shared access CA requirements are specified in Table 7.6F.2A.1-1.  These requirements apply for any SCS specified for the channel bandwidth of the wanted signal.  For the test parameters specified in Table 7.6F.2A.1-2, the throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

Table 7.6F.2A.1-1: In-band blocking parameters for intra-band contiguous shared access CA

Table 7.6F.2A.1-2: In-band blocking for intra-band contiguous shared access CA

## 7.6F.3Out-of-band blocking

## 7.6F.3.1General

Out-of-band band blocking is defined for an unwanted CW interfering signal falling outside a frequency range 60 MHz or greater below or above the UE receive band. The throughput of the wanted signal shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.6F.3.1-1 and Table 7.6F.3.1-2. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal.

Table 7.6F.3.1-1: Out-of-band blocking parameters for shared access bands

Table 7.6F.3.1-2: Out of-band blocking for shared access bands

For interferer frequencies across ranges 1, 2 and 3 in Table 7.6F.3.1-2, a maximum of

exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a step size of  MHz withthe number of resource blocks in the downlink transmission bandwidth configuration, CBW the bandwidth of the frequency channel in MHz and n = 1, 2, 3 for SCS = 15, 30, 60 kHz, respectively. For these exceptions, the requirements in clause 7.7F apply.

## 7.6F.3.2Void

## 7.6F.3AOut-of-band blocking for shared spectrum CA

## 7.6F.3A.1Intra-band contiguous shared spectrum channel access CA

Out-of-band blocking for intra-band contiguous shared access CA requirements are specified in Table 7.6F.3A.1-1.  These requirements apply for any SCS specified for the channel bandwidth of the wanted signal.  For the test parameters specified in Table 7.6F.3A.1-2, the throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

Table 7.6F.3A.1-1: Out-of-band blocking parameters for intra-band contiguous shared access CA

Table 7.6F.3A.1-2: Out of-band blocking for intra-band contiguous CA

## 7.6G(Reserved)

## 7.6H(Reserved)

## 7.6IBlocking characteristics for RedCap

Requirements in clauses 7.6.1 to 7.6.4 apply for a RedCap UE, except for a RedCap UE supporting both Band n20 and Band n28 the out-of-band blocking requirements for Band n20 and Band n28 specified in clause 7.6.3 apply with FDL_low given by Band n28 and FDL_high by Band n20.

## 7.6JBlocking characteristics for ATG

## 7.6J.1General

The blocking characteristic is a measure of the receiver's ability to receive a wanted signal at its assigned channel frequency in the presence of an unwanted interferer on frequencies other than those of the spurious response or the adjacent channels, without this unwanted input signal causing a degradation of the performance of the receiver beyond a specified limit. The blocking performance shall apply at all frequencies except those at which a spurious response occurs.

## 7.6J.2In-band blocking for ATG

For ATG UE, the in-band blocking requirement defined in clause 7.6.2 applies.

## 7.6J.2AIn-band blocking for ATG CA

## 7.6J.2A.1In-band blocking for ATG Intra-band contiguous CA

For ATG UE supporting intra-band contiguous CA operation, the in-band blocking requirement defined in clause 7.6A.2.1 applies.

## 7.6J.2A.2In-band blocking for ATG Inter-band CA

For ATG UE supporting inter-band CA operation, the in-band blocking requirement defined in clause 7.6A.2.3 applies.

## 7.6J.3Out-of-band blocking for ATG

For ATG UE, the out-of-band blocking requirement defined in clause 7.6.3 applies.

NOTE:In 3GPP, the ATG UE out-of-band blocking specification is defined to ensure the telecommunication link and there may be other sources of interference and regulatory issues that need to be considered when designing ATG UE, i.e. avionic equipment.

## 7.6J.3AOut-of-band blocking for ATG CA

NOTE:In 3GPP, the ATG UE out-of-band blocking specification is defined to ensure the telecommunication link and there may be other sources of interference and regulatory issues that need to be considered when designing ATG UE, i.e. avionic equipment.

## 7.6J.3A.1Out-of-band blocking for ATG Intra-band contiguous CA

For ATG UE supporting intra-band contiguous CA operation, the out-of-band blocking requirement defined in clause 7.6A.3.1 applies.

## 7.6J.3A.2Out-band blocking for ATG Inter-band CA

For ATG UE supporting inter-band CA operation, the out-of-band blocking requirement defined in clause 7.6A.3.3 applies.

## 7.6K(Reserved)

## 7.6L(Reserved)

## 7.7Spurious response

Spurious response is a measure of the ability of the receiver to receive a wanted signal on its assigned channel frequency without exceeding a given degradation due to the presence of an unwanted CW interfering signal at any other frequency for which a response is obtained, i.e. for which the out-of-band blocking limit as specified in clause 7.6.3 is not met.

The throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2  and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters for the wanted signal as specified in Table 7.7-1 for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz and in Table 7.7-1a for NR bands with FDL_high ≥ 3300 MHz and FUL_high ≥ 3300 MHz and for the interferer as specified in Table 7.7-2. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal. For operating bands with an unpaired DL part (as noted in Table 5.2-1), the requirements only apply for carriers assigned in the paired part.

Table 7.7-1: Spurious response parameters for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz

Table 7.7.1-1a: Spurious response parameters for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz

Table 7.7-2: Spurious response

## 7.7ASpurious response for CA

## 7.7A.1Spurious response for Intra-band contiguous CA

Table 7.7A-1: Spurious response parameters for intra-band contiguous CA

Table 7.7A-2: Spurious response for CA

Table 7.7A-3: Void

Table 7.7A-4: Void

## 7.7A.2Spurious response for Intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, the spurious response requirements are defined with the uplink configuration in accordance with Table 7.3A.2.2-1. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in clauses 7.7 and 7.7A.1 for one component carrier and two component carriers per sub-block, respectively. The requirements apply with all downlink carriers active.

The throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

## 7.7A.3Spurious response for Inter-band CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one NR band, the spurious response are defined with the uplink active on the band(s) other than the band whose downlink is being tested. The UE shall meet the requirements specified in clause 7.7 for each component carrier while all downlink carriers are active.

For the UE which supports inter-band CA configuration in Table 7.3A.3.2.1-1, Pinterferer power defined in Table 7.7-2 and Table 7.7F.1-2 for shared spectrum channel access is increased by the amount given by ΔRIB,c in Table 7.3A.3.2.1-1 and in Table 7.3F.3-1 for shared spectrum channel access .

The throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

## 7.7BSpurious response for NR-DC

For inter-band NR-DC configurations, the spurious response for the corresponding inter-band CA configuration as specified in clause 7.7A applies.

## 7.7DSpurious response for UL MIMO

For UE with multiple transmitter antenna connectors up to a maximum of four in closed-loop spatial multiplexing scheme, the minimum requirements specified in clause 7.7 shall be met with the UL MIMO configurations described in clause 6.2D.1 and in clause 6.2F.1D for shared spectrum access operation. For UL MIMO, the parameter PCMAX_L is defined as the total transmitter power over all transmit antenna connectors.

## 7.7ESpurious response for V2X

## 7.7E.1General

Spurious response is a measure of the receiver’s ability to receive a wanted signal on its assigned channel frequency without exceeding a given degradation due to the presence of an unwanted CW interfering signal at any other frequency for which a response is obtained, i.e. for which the out-of-band blocking limit as specified in clause 7.6E.3.1 is not met.

When UE is configured for NR V2X reception non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.7.2 with parameters for the wanted signal as specified in Table 7.7E.1-1 and Table 7.7E.1-2 for NR V2X bands. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal.

Table 7.7E.1-1: Spurious response parameters for NR V2X

Table 7.7E.1-2: Spurious response for NR V2X

## 7.7E.1ASpurious response requirements for Sidelink CA

For intra-band contiguous SL CA operation, the UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.7.2 with parameters specified in Table 7.7E.1A-1 and Table 7.7E.1A-2.

Table 7.7E.1A-1: Spurious response parameters for intra-band contiguous SL CA UE

Tables 7.7E.1A-2: Spurious response for intra-band contiguous SL CA UE

For intra-band non-contiguous SL CA operation, the UE shall meet the requirements for each sub-block as specified in clauses 7.7E for one component carrier per sub-block, respectively. The requirements apply with all sidelink carriers active. The UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.7.2 with test parameters defined in clause 7.7E.1 per sub-block while all downlink carriers are active.

## 7.7E.1FGeneral requirement for Sidelink Unlicensed

The spurious response requirement in clause 7.7F.1 apply.

For spurious responses, the throughput of the wanted signal shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex 7.2

## 7.7E.2Spurious response for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 7.7E.1 shall apply for the NR sidelink reception in the operating bands in Table 5.2E.2-1 and the requirements specified in clause 7.7 shall apply for the NR downlink reception in licensed band while all downlink carriers are active.

## 7.7E.2FSpurious response for SL-U concurrent operation

For the inter-band concurrent NR SL-U operation, the requirements specified in clause 7.7E.1F shall apply for the NR sidelink reception in the operating bands in Table 5.2E.2F-1 and the requirements specified in clause 7.7 shall apply for the NR downlink reception in licensed band while all downlink carriers are active.

## 7.7FSpurious response for shared spectrum channel access

## 7.7F.1General

For spurious responses, the throughput of the wanted signal shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.7F.1-1 and Table 7.7F.1-2. The relative throughput requirement shall be met for any SCS at any other frequency at which a response is obtained i.e. for which the limit as specified in clause 7.6F.3.1 is not met.

Table 7.7F.1-1: Spurious response parameters for shared access bands

Table 7.7F.1-2: Spurious response for shared spectrum channel access

## 7.7F.1ASpurious response for shared spectrum channel access CA

## 7.7F.1A.1Intra-band contiguous shared spectrum channel access CA

For spurious responses, the throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.7F.1A.1-1 and Table 7.7F.1A.1-2. The relative throughput requirement shall be met for any SCS at any other frequency at which a response is obtained i.e. for which the limit as specified in clause 7.6F.3.2 is not met.

Table 7.7F.1A.1-1: Spurious response parameters for intra-band contiguous shared access CA

Table 7.7F.1A.1-2: Spurious response for intra-band contiguous shared access CA

## 7.7F.2Void

## 7.7G(Reserved)

## 7.7H(Reserved)

## 7.7I(Reserved)

## 7.7JSpurious response for ATG

## 7.7J.1General

For ATG UE, the spurious response defined in clause 7.7 applies.

## 7.7J.1ASpurious response for ATG CA

## 7.7J.1A.1Spurious response for ATG intra-band contiguous CA

For ATG UE supporting intra-band contiguous CA operation, the spurious response defined in clause 7.7A.1 applies.

## 7.7J.1A.2Spurious response for ATG inter-band CA

For ATG UE supporting inter-band CA operation, the spurious response defined in clause 7.7A.3 applies.

## 7.7K(Reserved)

## 7.7L(Reserved)

## 7.8Intermodulation characteristics

## 7.8.1General

Intermodulation response rejection is a measure of the capability of the receiver to receive a wanted signal on its assigned channel frequency in the presence of two or more interfering signals which have a specific frequency relationship to the wanted signal

## 7.8.2Wide band Intermodulation

The wide band intermodulation requirement is defined using a CW carrier and modulated NR signal as interferer 1 and interferer 2 respectively.

The throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.8.2-1 for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz and Table 7.8.2-2 for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal. For operating bands with an unpaired DL part (as noted in Table 5.2-1), the requirements only apply for carriers assigned in the paired part.

Table 7.8.2-1: Wide band intermodulation parameters for NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz

Table 7.8.2-2: Wide band intermodulation parameters for NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz

## 7.8AIntermodulation characteristics for CA

## 7.8A.1General

## 7.8A.2Wide band intermodulation for CA

## 7.8A.2.1Wide band intermodulation for Intra-band contiguous CA

Table 7.8A.2.1-1: Wide band intermodulation parameters for intra-band contiguous CA with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz

Table 7.8A.2.1-2: Wide band intermodulation parameters for intra-band contiguous CA with FDL_low  < 2700 MHz and FUL_low  < 2700 MHz

## 7.8A.2.2Wide band intermodulation for Intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation with one uplink carrier and two or more downlink sub-blocks, the wide band intermodulation requirements are defined with the uplink configuration in accordance with Table 7.3A.2.2-1. For this uplink configuration, the UE shall meet the requirements for each sub-block as specified in clause 7.8.2 and 7.8A.2.1 for one component carrier and two component carriers per sub-block, respectively. The requirements apply for out-of-gap interferers while all downlink carriers are active.

The throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

## 7.8A.2.3Wide band intermodulation for Inter-band CA

For inter-band carrier aggregation with one component carrier per operating band and the uplink assigned to one NR band, the wide band intermodulation requirements are defined with the uplink active on the band(s) other than the band whose downlink is being tested. The UE shall meet the requirements specified in clause 7.8 for each component carrier while all downlink carriers are active.

For the UE which supports inter-band CA configuration in Table 7.3A.3.2.1-1, Pinterferer power defined in Table 7.8.2-1 and 7.8.2-2 and Table 7.8F.2-1 for shared spectrum channel access is increased by the amount given by ΔRIB,c in Table 7.3A.3.2.1-1 in Table 7.3F.3-1 for shared spectrum channel access .

The throughput of each carrier shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1).

## 7.8BIntermodulation characteristics for NR-DC

For inter-band NR-DC configurations, the intermodulation characteristics for the corresponding inter-band CA configuration as specified in clause 7.8A applies.

## 7.8DIntermodulation characteristics for UL MIMO

For UE(s) with multiple transmitter antenna connectors up to a maximum of four in closed-loop spatial multiplexing scheme, the minimum requirements in clause 7.8 shall be met with the UL MIMO configurations described in clause 6.2D.1 and in clause 6.2F.1D for shared spectrum access operation. For UL MIMO, the parameter PCMAX_L is defined as the total transmitter power over all transmit antenna connectors.

## 7.8EIntermodulation characteristics for V2X

## 7.8E.1General

Intermodulation response rejection is a measure of the capability of the receiver to receive a wanted signal on its assigned channel frequency in the presence of two or more interfering signals which have a specific frequency relationship to the wanted signal.

## 7.8E.2Wide band Intermodulation

## 7.8E.2.1General

The wide band intermodulation requirement is defined using modulated NR carrier and a CW signal as interferer 1 and interferer 2 respectively. When UE is configured for NR V2X reception non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.7.2 with parameters specified in Table 7.8E.2-1 for NR V2X bands. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal.

Table 7.8E.2-1: Wide band intermodulation parameters for NR V2X

Table 7.8E.2-1a: Wide band intermodulation parameters in n14

## 7.8E.2.2Wide band Intermodulation for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 7.8E.2.1 shall apply for the NR sidelink reception in the operating bands in Table 5.2E.2-1 and the requirements specified in clause 7.8 shall apply for the NR downlink reception in licensed band while all downlink carriers are active.

## 7.8E.2.2AWide band intermodulation for Sidelink CA

For intra-band contiguous SL CA operation, the UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.7.2 with parameters specified in Table 7.8E.2.1A-1 for the specified wanted signal mean power in the presence of two interfering signals.

Table 7.8E.2.2A-1: Wide band intermodulation for intra-band contiguous SL CA UE

For intra-band non-contiguous SL CA operation, the UE shall meet the requirements for each sub-block as specified in clauses 7.8E.2 for one component carrier per sub-block, respectively. The requirements apply with all sidelink carriers active. The UE throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annex A.7.2 with test parameters defined in clause 7.8E.2.1 per sub-block while all downlink carriers are active.

## 7.8E.2.2FWide band Intermodulation for SL-U concurrent operation

For the inter-band concurrent NR SL-U operation, the requirements specified in clause 7.8E.2F shall apply for the NR sidelink reception in the operating bands in Table [5.2E.2F-1] and the requirements specified in clause 7.8 shall apply for the NR downlink reception in licensed band while all downlink carriers are active.

## 7.8E.2FWide band Intermodulation for Sidelink Unlicensed

The spurious response requirement in clause 7.8F.2 apply.

Instead of the general wideband intermodulation requirements specified in clause 7.8.2, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annex 7.2 with parameters specified in Table 7.8F.2-1. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal.

## 7.8FIntermodulation characteristics for shared spectrum channel access

## 7.8F.1General

Intermodulation response rejection is a measure of the capability of the receiver to receive a wanted signal on its assigned channel frequency in the presence of two or more interfering signals which have a specific frequency relationship to the wanted signal

## 7.8F.2Wide band Intermodulation

The wide band intermodulation requirement is defined using a CW carrier and modulated NR signal as interferer 1 and interferer 2 respectively.

Instead of the general wideband intermodulation requirements specified in clause 7.8.2, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2 and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table 7.8F.2-1. The relative throughput requirement shall be met for any SCS specified for the channel bandwidth of the wanted signal.

Table 7.8F.2-1: Wide band intermodulation parameters for shared spectrum channel access

## 7.8G(Reserved)

## 7.8H(Reserved)

## 7.8I(Reserved)

## 7.8JIntermodulation characteristics for ATG

## 7.8J.1General

Intermodulation response rejection is a measure of the capability of the receiver to receive a wanted signal on its

assigned channel frequency in the presence of two or more interfering signals which have a specific frequency relationship to the wanted signal.

## 7.8J.2Wide band intermodulation for ATG

For ATG UE, the wide band intermodulation requirement defined in clause 7.8.2 applies.

## 7.8J.2AWide band intermodulation for ATG CA

## 7.8J.2A.1Wide band intermodulation for ATG intra-band contiguous CA

For ATG UE supporting intra-band contiguous carrier aggregation, the wide band intermodulation requirement defined in clause 7.8A.2.1 applies.

## 7.8J.2A.2Wide band intermodulation for ATG inter-band CA

For ATG UE supporting inter-band carrier aggregation, the wide band intermodulation requirement defined in clause 7.8A.2.3 applies.

## 7.8K(Reserved)

## 7.8L(Reserved)

## 7.9Spurious emissions

The spurious emissions power is the power of emissions generated or amplified in a receiver that appear at the UE antenna connector.

The power of any narrow band CW spurious emission shall not exceed the maximum level specified in Table 7.9-1

Table 7.9-1: General receiver spurious emission requirements

## 7.9ASpurious emissions for CA

## 7.9A.1Void

## 7.9A.2Void

## 7.9A.3Spurious emissions for Inter-band CA

For inter-band carrier aggregation including an operating band without uplink band, the UE shall meet the Rx spurious emissions requirements specified in clause 7.9 for each component carrier while all downlink carriers are active.

## 7.9BSpurious emissions for NR-DC

For inter-band NR-DC configurations, the spurious emissions for the corresponding inter-band CA configuration as specified in clause 7.9A applies.

## 7.9JSpurious emissions for ATG

## 7.9J.1General

For ATG UE, the spurious emissions as specified in clause 7.9 applies.

## 7.9J.1ASpurious emissions for ATG CA

## 7.9J.1A.1Spurious emissions for ATG inter-band CA

For ATG UE supporting inter-band carrier aggregation including an operating band without uplink band, the UE shall meet the Rx spurious emissions requirements specified in clause 7.9 for each component carrier while all downlink carriers are active.

## 7.9MSpurious emissions for LP-WUS/WUR

The spurious emissions as specified in clause 7.9 applies.

## 7.10Power imbalance

## 7.10APower imbalance for CA

## 7.10A.1General

Power imbalance requirement is a measure of the receiver’s ability to receive a wanted signal in the presence of another signal with a power imbalance and a specific frequency offset from the wanted signal.

Power imbalance requirement in this subclause is applicable for:

-A UE capable of intraBandNR-CA-non-collocated-r18 and is not provided with nonCollocatedTypeNR-CA-r18 and is configured with maxMIMO-Layers with value less than or equal to 2; or,

-A UE capable of intraBandNR-CA-non-collocated-r19 and nonCollocatedTypeNR-CA-r1900 is provided with value type4 and is configured with maxMIMO-Layer equal to 4.

## 7.10A.2Minimum requirement

For the test parameters in Table 7.10A.2-1, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 TDD for the DL-signal as described in Annex A.5.2.1).

Table 7.10A.2-1: Power imbalance parameters for intra-band non-contiguous CA

For a UE capable of intraBandNR-CA-non-collocated-r18 for the following CA band combinations in Table 7.10A.2-2, the Power imbalance requirements are applicable with 2Rx antenna ports for each component carrier if it is not provided with nonCollocatedTypeNR-CA-r18 and is configured with maxMIMO-Layers with value less than or equal to 2.

For a UE capable of intraBandNR-CA-non-collocated-r19 with the CA band combinations in Table 7.10A.2-2, the Rx requirements for four Rx ports are applicable for each component carrier, if nonCollocatedTypeNR-CA-r1900 is provided with value type4 and the UE is configured with maxMIMO-Layers equal to 4.

Table 7.10A.2-2: NR CA combinations
