# TS 38.101 38101-1-j60_s0505B-0505J

## 5.5BConfigurations for DC

For an NR DC configuration specified in Table 5.5B-1, the bandwidth combination sets for the corresponding NR CA configuration in 5.5A.3, i.e., dual uplink inter-band carrier aggregation with uplink assigned to two NR bands, are applicable to Dual Connectivity.

Table 5.5B-1: Inter-band NR DC configurations (two bands)

Table 5.5B-2: Inter-band NR DC configurations (three bands)

Table 5.5B-3: Inter-band NR DC configurations (four bands)

Table 5.5B-4: Inter-band NR DC configurations (five bands)

## 5.5CConfigurations for SUL

The configuration tables for SUL describe Bandwidth Combination Sets. Bandwidth Combination Set 4 and 5 contains all possible defined channel bandwidths for each band in the combination. The fact that BCS4 and BCS5 contains all channel bandwidths for each band does not alter if a bandwidth is mandatory or optional for a given band. Bandwidths that are identified as optional in Table 5.3.5-1 for a given release are still optional for UEs that support BCS4 or BCS5. , where the bandwidths the UE supports for each band, the maximum bandwidth and/or minimum bandwidth for the band in the band combination are indicated in the UE capabilities. The minimum bandwidth per CC and aggregated FDD, TDD and total bandwidth per band combination may be indicated only for BCS5 as described in 38.306 [15] and BCS5 shall not be indicated together with BCS4 for a SUL configuration. For SUL band combinations including FR1 intra-band CA and with BCS4 or BCS5, the Bandwidth Combination Sets for the FR1 intra-band CA are BCS4 or BCS5.

For the NR SUL band configurations with inter-band CA in sub-clause 5.5C, when the capability supportedBandPairListNR-r18 is present, three or four bands can be configured in the uplink with simultaneous uplink transmission on up to two bands, and the corresponding requirements for SUL band configurations with inter-band CA and with uplink assigned to one or two bands shall apply. For each uplink band pair in the NR SUL band configurations with inter-band CA, according to the capability uplinkTxSwitchingOptionForBandPair,

–if switchedUL is supported, uplink transmission on any one band of the band pair in the band combination shall be supported according to the scheduling commands, and the corresponding requirements for SUL band configuration with inter-band CA and with uplink assigned to one band on band X or band Y apply;

–if dualUL is supported, simultaneous uplink transmission on the two NR UL bands from the band pair for which dualUL is declared in the band combination shall be supported according to the scheduling commands, and the corresponding requirements for SUL band configuration with inter-band CA and with uplink CA between the two uplink bands apply.

For SUL band configuration with inter-band CA, band pair(s) of two non-SUL bands with switchedUL or dualUL by the parameter uplinkTxSwitchingOption is supported, and any other band pair(s) including SUL with switchedUL is supported, in release 18.

Table 5.5C-1: Supported channel bandwidths per SUL band combination

Table 5.5C-2: Supported channel bandwidths per SUL band combination with intra-band non-contiguous CA

Table 5.5C-3: Supported channel bandwidths per SUL band combinationwith intra-band contiguous CA

Table 5.5C-4: Supported channel bandwidths per SUL band combination with inter-band CA

Table 5.5C-5: Supported channel bandwidths per SUL band combinationwith inter-band CA (two SUL cells)

## 5.5DReserved

## 5.5EConfigurations for Sidelink

## 5.5E.1AConfigurations for Sidelink CA

For NR SL CA operation, the SL CA channel bandwidths for intra-band contiguous are specified in clause 5.5E.1A.1. The same (symmetrical) channel bandwidth is specified for both the transmission and reception path.

## 5.5E.1A.1Configurations for Sidelink intra-band contiguous CA

Table 5.5E.1A.1-1 NR SL CA configurations and bandwidth combination set for SL intra-band contiguous CA in FR1

## 5.5E.1A.2Configurations for Sidelink intra-band non-contiguous CA

Table 5.5E.1A.1-2 NR SL CA configurations and bandwidth combination set for SL intra-band non-contiguous CA in FR1

## 5.5JConfigurations for ATG

## 5.5J.1AConfigurations for ATG CA

The ATG intra-band contiguous CA configurations and channel bandwidths are specified in clause 5.5J.1A.1. The ATG inter-band CA configurations and channel bandwidths are specified in clause 5.5J.1A.2.

## 5.5J.1A.1Configurations for ATG intra-band contiguous CA

Table 5.5J.1A.1-1 Configurations and bandwidth combination set for ATG intra-band contiguous CA in FR1

## 5.5J.1A.2Configurations for ATG inter-band CA

Table 5.5J.1A.2-1 Configurations and bandwidth combination set for ATG inter-band CA in FR1
