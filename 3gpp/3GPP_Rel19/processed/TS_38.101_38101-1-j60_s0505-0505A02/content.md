# TS 38.101 38101-1-j60_s0505-0505A02

## 5.5Void

## 5.5AConfigurations for CA

## 5.5A.0General

The configurations for CA operating band including Band n41 also apply for the corresponding CA operating bands with Band n90 replacing Band n41 but with otherwise identical parameters. For brevity the said configuration for CA operating bands with Band n90 are not listed in the tables below but are covered by this specification.

Noncontiguous resource allocation and almost contiguous allocation are not applicable for each NR carrier of intraband contiguous and non-contiguous CA configurations.

For a CA configuration with one or more operating band supporting asymmetric channel bandwidths as specified in sub-clause 5.3.6, requirements are defined for an asymmetric UL and DL channel bandwidth combination of a supported asymmetric channel bandwidth combination set for an operating band of the CA configuration when the said UL and DL channel bandwidths are also contained in a supported bandwidth combination set of the CA configuration.

For a higher order band combination of which CA_n20-n28 is a subset, the frequency range in band n28 is restricted for the higher order band combination to 703-733 MHz for the UL and 758-788 MHz for the DL.

The configuration tables for CA describe Bandwidth Combination Sets. Bandwidth Combination Set 4 and 5 contain all possible defined channel bandwidths for each band in the combination. The fact that BCS4 and BCS5 contain all channel bandwidths for each band does not alter if a bandwidth is mandatory or optional for a given band. Bandwidths that are identified as optional in Table 5.3.5-1 for a given release are still optional for UEs that support BCS4 or BCS5, where the bandwidths the UE supports for each band, the maximum bandwidth and/or minimum bandwidth for the band in the band combination are indicated in the UE capabilities. The minimum bandwidth per CC and maximum aggregated FDD, TDD and total bandwidth per band combination may be indicated only for BCS5 as described in 38.306 [15] and BCS5 shall not be indicated together with BCS4 for a CA configuration. For inter-band CA combinations including FR1 intra-band CA and with BCS4 or BCS5 in the following configuration tables, the Bandwidth Combination Sets for the FR1 intra-band CA are BCS4 or BCS5, respectively.

By default, unless otherwise noted/stated and except for NR band restricted to operation with share spectrum access channel, power class 3 applies to:

-all valid NR FR1 band single uplink configurations,

-all specified NR FR1 band intra-band uplink CA configurations,

-all specified inter-band CA configurations.

For NR bands with operation restricted to shared spectrum channel access, by default power class 5 applies to all valid single uplink configurations and to all specified intra-band uplink CA configuration. The applicability of higher power class(es) is described in the CA configuration tables in clauses 5.5A.1, 5.5A.2 and 5.5A.3. For inter-band CA combinations in clause 5.5A.3, the applicability of higher power class(es) for higher order band combinations is extended based on the following conditions:

-For a combination of intra-band and inter-band CA, the same higher power class(es) may be supported, which are specified for the inter-band UL CA configuration(s) in the combination composed of the same bands without intra-band CA.

-For a combination of intra-band and inter-band CA, the higher power class(es) may be supported for single-carrier UL when the same higher power class(es) are specified for all its fallback combinations.

-For a combination with 3 or more DL bands without intra-band CA, the higher power class(es) may be supported for single-carrier UL when the same higher power class(es) are specified for all its 2-band fallback combinations.

-For a combination with 4 or more DL bands without intra-band CA, the higher power class(es) may be supported for inter-band UL CA configuration(s) when the same higher power class(es) are specified for all its 3-band fallback combinations.

A UE supporting a given power class for a CA configuration shall meet the corresponding transmitter and receiver requirements in Clause 6 and Clause 7, respectively.

In the CA configuration tables of clause 5.5A.1 and clause 5.5A.2:

-Unless otherwise noted/stated, Uplink CA configuration entries with "-" mean single uplink carrier is valid for downlink intra-band CA,

In the CA configuration tables of clause 5.5A.3:

-Uplink CA configuration entries with "-" mean that any valid constituent band of the downlink inter-band CA combination can be configured as a single uplink carrier,

-Unless otherwise noted, all of the valid downlink constituent bands can be configured as a single uplink carrier,

-If an uplink CA configuration is supported, its fallback single uplink is also supported.

## 5.5A.1Configurations for intra-band contiguous CA

Table 5.5A.1-1: NR CA configurations and bandwidth combination sets defined forintra-band contiguous CA

Table 5.5A.1-2: Void

## 5.5A.2Configurations for intra-band non-contiguous CA

Table 5.5A.2-1: NR CA configurations and bandwidth combination sets defined forintra-band non-contiguous CA

Table 5.5A.2-2: NR CA configurations and bandwidth combination sets defined formixed intra-band contiguous and non-contiguous CA
