# TS 38.101 38101-1-j60_s0505A03-0505A03

## 5.5A.3Configurations for inter-band CA

Table 5.5A.3-1: Void

Table 5.5A.3-2: Void

Table 5.5A.3-3: Void

## 5.5A.3.0General

For the NR inter-band CA configurations in sub-clause 5.5A.3, when the capability supportedBandPairListNR-r18 is present, three or four bands can be configured in the uplink with simultaneous uplink transmission on up to two bands, and the corresponding inter-band CA requirements with uplink assigned to one or two bands shall apply. For each uplink band pair in the NR inter-band CA configurations, according to the capability uplinkTxSwitchingOptionForBandPair-r18,

–if switchedUL is supported, uplink transmission on any one band of the band pair in the band combination shall be supported according to the scheduling commands, and the corresponding inter-band CA requirements with uplink assigned to one band on band X or band Y apply;

–if dualUL is supported, simultaneous uplink transmission on the two NR UL bands from the band pair for which dualUL is declared in the band combination shall be supported according to the scheduling commands, and the corresponding inter-band CA requirements with uplink CA between the two uplink bands apply.

Low NR band inter-band CA configurations in which the UE is allowed to indicate support of the configuration via switching featureSetCombinationLowBandSwitching-r19 are indicated with the corresponding note in the configuration tables in sub-clause 5.5A.3.1.

## 5.5A.3.1Configurations for inter-band CA (two bands)

## Table 5.5A.3.1-1a ~ Table 5.5A.3.1-1e

Table 5.5A.3.1-1a: NR CA configurations and bandwidthcombinations sets defined for inter-band CA (two bands)

Table 5.5A.3.1-1b: NR CA configurations and bandwidth combinationssets defined for inter-band CA (two bands)

Table 5.5A.3.1-1c: NR CA configurations and bandwidth combinationssets defined for inter-band CA (two bands)

Table 5.5A.3.1-1d: NR CA configurations and bandwidth combinations  sets defined for inter-band CA (two bands)

Table 5.5A.3.1-1e: NR CA configurations and bandwidth combinationssets defined for inter-band CA (two bands)

## Table 5.5A.3.1-1f ~ Table 5.5A.3.1-1j

Table 5.5A.3.1-1f: NR CA configurations and bandwidth combinationssets defined for inter-band CA (two bands)

Table 5.5A.3.1-1g: NR CA configurations and bandwidth combinationssets defined for inter-band CA (two bands)

Table 5.5A.3.1-1h: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

Table 5.5A.3.1-1i: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

Table 5.5A.3.1-1j: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

## Table 5.5A.3.1-1k ~ Table 5.5A.3.1-1o

Table 5.5A.3.1-1k: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

Table 5.5A.3.1-1l: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

Table 5.5A.3.1-1m: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

Table 5.5A.3.1-1n: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

Table 5.5A.3.1-1o: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

The following notes are applied to the above tables:

NOTE 1:This UE channel bandwidth is applicable only to downlink.

NOTE 2:The minimum requirements for intra-band contiguous or non-contiguous CA apply.

NOTE 3:For each channel bandwidth of each component carrier, refer to Table 5.3.5-1 for the applicable SCSs. For a given band, not all UE channel bandwidths support the same SCSs.

NOTE 4:This UE channel bandwidth is optional in this release of the specification.

NOTE 5:For this bandwidth, the minimum requirements are restricted to operation when carrier is configured as an SCell part of DC or CA configuration.

NOTE 6:For this bandwidth, the minimum requirements are restricted to operation when carrier is configured as an downlink SCell part of CA configuration

NOTE 7:Limited to operation at 3450-3550 MHz and 3700–3980 MHz.

NOTE 8:Minimum requirements for Power Class 2 are applicable for this uplink CA configuration according to clause 6.2A.1.1 or 6.2A.1.2 or 6.2A.1.3 or single uplink carrier configuration according to clauses 6.2.1 or 6.2D.1 or 6.2G.1 in this downlink/uplink combination.

NOTE 9:Minimum requirements for Power Class 1.5 are applicable for this uplink CA configuration according to clause 6.2A.1.3 or single uplink carrier according to clauses 6.2.1 or 6.2D.1 or 6.2G.1 in this downlink/uplink combination.

NOTE 10: Only single uplink carriers with power class other than PC3 are listed.

NOTE 11: The CA configurations are given in Table 5.5A.1-1 or Table 5.5A.2-1 in this specification

NOTE 12: Void.

NOTE 13: Minimum requirements for Power Class 2 are applicable for this uplink CA configuration according to clause 6.2H.3.1 or 6.2L.3.1.

NOTE 14 Minimum requirements for Power Class 1.5 are applicable for this uplink CA configuration according to clause 6.2H.3.1 or 6.2L.3.1.

NOTE 15: Uplink is only in n5 for CA_n5-n8.

NOTE 16: For UEs only supporting DL CA_n26-n28, uplink support in band n26 is optional, if the UE supports CA_n26-n28 UL configuration, it should also support UL in band n26 and n28.

NOTE 17:The UEs is allowed to indicate support of low NR band inter-band carrier aggregation via switching featureSetCombinationLowBandSwitching-r19 for this NR CA configuration

NOTE 18:Applicable only for UEs which indicate support of low NR band inter-band carrier aggregation via switching featureSetCombinationLowBandSwitching-r19 for this NR CA configuration

NOTE 19:When UL CA_n5A-n8A is supported, some restrictions may be needed to avoid simultaneous n5DL and n8 UL during UL CA_n5A-n8A with DL CA_n5A-n8A configuration. The UE and/or NW behaviors are not specified in the 3GPP specifications when there is a conflict between n5DL and n8UL including dynamic scheduling, semi-static signals and unspecified transitions between n5DL and n8UL.

NOTE 20:For single uplink carrier or TDD band intra-band uplink CA without NOTE 8, minimum requirements for Power Class 2 are applicable provided the said power class has been specified in Table 6.2.1-1, Table 6.2D.1-1, Table 6.2A.1.1-1, Table 6.2A.1.2-1 and Table 6.2H.1.1-1 and the corresponding PC2 MSD is specified in clause 7.3A.2.3.1 or clause 7.3A.2.3.2 or there is no MSD impact for this downlink/uplink combination.

NOTE 21:For single uplink carrier or TDD band intra-band uplink CA without NOTE 9, minimum requirements for Power Class 1.5 are applicable provided the said power class has been specified in Table 6.2.1-1 or Table 6.2D.1-1, Table 6.2A.1.1-1, Table 6.2A.1.2-1 and Table 6.2H.1.1-1 and the corresponding PC1.5 MSD is specified in clause 7.3A.2.3.1 or clause 7.3A.2.3.2 or there is no MSD impact for this downlink/uplink combination.

NOTE 22:The frequency range in band n28 is restricted for this band combination to 703- 733 MHz for the UL and 758-788 MHz for the DL.

NOTE 23: The frequency range in band n28 is restricted for this band combination to 718-748 MHz for the UL and 773-803 MHz for the DL.

## 5.5A.3.2Configurations for inter-band CA (three bands)

Table 5.5A.3.2-1: Void

## Table 5.5A.3.2-1a

Table 5.5A.3.2-1a: NR CA configurations and bandwidth combinations sets defined for inter-band CA (three bands)

## Table 5.5A.3.2-1b

Table 5.5A.3.2-1b: NR CA configurations and bandwidth combinations sets defined for inter-band CA (three bands)

## Table 5.5A.3.2-1c

Table 5.5A.3.2-1c: NR CA configurations and bandwidth combinations sets defined for inter-band CA (three bands)

The following notes are applied to the above tables.

NOTE 1:This UE channel bandwidth is applicable only to downlink

NOTE 2:For the 20 MHz bandwidth, the minimum requirements are specified for NR UL carrier frequencies confined to either 713-723 MHz or 728-738 MHz.

NOTE 3: For each channel bandwidth of each component carrier, refer to Table 5.3.5-1 for the applicable SCSs. For a given band, not all UE channel bandwidths support the same SCSs.

NOTE 4:The minimum requirements only apply for non-simultaneous Rx/Tx between all carriers for TDD combinations.

NOTE 5:Simultaneous Rx/Tx capability for TDD combinations does not apply for UEs supporting band n78 with an n77 implementation.

NOTE 6:Only single uplink carriers with power class other than PC3 are listed.

NOTE 7:Minimum requirements for Power Class 2 are applicable for this uplink combination or single uplink carrier in this downlink/uplink combination

NOTE 8:For this bandwidth, the minimum requirements are restricted to operation when carrier is configured as an SCell part of DC or CA configuration.

NOTE 9:Minimum requirements for Power Class 1.5 are applicable for this uplink combination or single uplink carrier in this downlink/uplink combination

NOTE 10:For a band combination which include band n7 and n38 simultaneously, carriers in band n7 and n38 can only be configured as downlink carriers. Power imbalance between downlink carriers on Band n7 and Band n38 is assumed to be within 6dB.

NOTE 11: UL carrier shall be supported in Band n28 only. Power imbalance between downlink carriers on Band 7 and Band 38 is assumed to be within 6dB.

NOTE 12:For this bandwidth, the minimum requirements are restricted to operation when carrier is configured as a downlink SCell part of CA configuration.

NOTE 13: Minimum requirements for Power Class 2 are applicable for this uplink CA configuration according to clause 6.2H.3.1 or 6.2L.3.1.

NOTE 14: Minimum requirements for Power Class 1.5 are applicable for this uplink CA configuration according to clause 6.2H.3.1 or 6.2L.3.1.

NOTE 15:For a two-band UL configuration without NOTE 7 or NOTE 13, minimum requirements for Power Class 2 are applicable provided the said power class has been specified in Table 6.2A.1.3-1 or Table 6.2H.3.1-1 respectively and the corresponding PC2 MSD is specified in clause 7.3A.2.3.2 or there is no MSD impact for this downlink/uplink combination.

NOTE 16:For a two-band UL configuration without NOTE 9 or NOTE 14, minimum requirements for Power Class 1.5 are applicable provided the said power class has been specified in Table 6.2A.1.3-1 or Table 6.2H.3.1-1 respectively and the corresponding PC1.5 MSD is specified in clause 7.3A.2.3.2 or there is no MSD impact for this downlink/uplink combination.

NOTE 17:The frequency range in band n28 is restricted for this band combination to 703-733MHz for the UL and 758-788MHz for the DL.

NOTE 18:This combination only works for non-simultaneous RX/TX. In the case that there is no simultaneous RX/TX also no RX sensitivity section is needed.

## 5.5A.3.3Configurations for inter-band CA (four bands)

Table 5.5A.3.3-1: Void

## Table 5.5A.3.3-1a

Table 5.5A.3.3-1a: NR CA configurations and bandwidth combinations sets defined for inter-band CA (four bands)

## Table 5.5A.3.3-1b

Table 5.5A.3.3-1b: NR CA configurations and bandwidth combinations sets defined for inter-band CA (four bands)

The following notes are applied to the above tables.

NOTE 1:This UE channel bandwidth is optional in this release of the specification.

NOTE 2:For the 20 MHz bandwidth, the minimum requirements are specified for NR UL carrier frequencies confined to either 713-723 MHz or 728-738 MHz. For the 30MHz bandwidth, the minimum requirements are specified for NR UL transmission bandwidth configuration confined to either 703-733 or 718-748 MHz.

NOTE 3:For each channel bandwidth of each component carrier, refer to Table 5.3.5-1 for the applicable SCSs. For a given band, not all UE channel bandwidths support the same SCSs.

NOTE 4: Only single uplink carriers with power class other than PC3 are listed.

NOTE 5:Minimum requirements for Power Class 2 are applicable for this uplink combination or single uplink carrier in this downlink/uplink combination.

NOTE 6:Minimum requirements for Power Class 1.5 are applicable for this uplink combination or single uplink carrier in this downlink/uplink combination.

NOTE 7:For a band combination which includes band n7 and n38 simultaneously, carriers in band n7 and n38 can only be configured as downlink carriers. Power imbalance between downlink carriers on Band n7 and Band n38 is assumed to be within 6dB.

NOTE 8:For this bandwidth, the minimum requirements are restricted to operation when carrier is configured as a downlink SCell part of CA configuration

NOTE 9:Minimum requirements for Power Class 2 are applicable for this uplink configuration with 1Tx antenna connector in one band and 2Tx antenna connectors in the other band.

NOTE 10:Minimum requirements for Power Class 1.5 are applicable for this uplink configuration with 1Tx antenna connector in one band and 2Tx antenna connectors in the other band.

NOTE 11:The frequency range in band n28 is restricted for this band combination to 703- 733 MHz for the UL and 758-788 MHz for the DL.

## 5.5A.3.4Configurations for inter-band CA (five bands)

Table 5.5A.3.4-1: NR CA configurations and bandwidth combinations sets defined for inter-band CA (five bands)

## 5.5A.3.5Configurations for inter-band CA (six bands)

Table 5.5A.3.5-1: NR CA configurations and bandwidth combinations sets defined for inter-band CA (six bands)
