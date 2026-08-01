### 5.5A.3 Configurations for inter-band CA

Table 5.5A.3-1: Void

Table 5.5A.3-2: Void

Table 5.5A.3-3: Void

#### 5.5A.3.0 General

For the NR inter-band CA configurations in sub-clause 5.5A.3, when the capability supportedBandPairListNR-r18 is present, three or four bands can be configured in the uplink with simultaneous uplink transmission on up to two bands, and the corresponding inter-band CA requirements with uplink assigned to one or two bands shall apply. For each uplink band pair in the NR inter-band CA configurations, according to the capability uplinkTxSwitchingOptionForBandPair-r18,

– if switchedUL is supported, uplink transmission on any one band of the band pair in the band combination shall be supported according to the scheduling commands, and the corresponding inter-band CA requirements with uplink assigned to one band on band X or band Y apply;

– if dualUL is supported, simultaneous uplink transmission on the two NR UL bands from the band pair for which dualUL is declared in the band combination shall be supported according to the scheduling commands, and the corresponding inter-band CA requirements with uplink CA between the two uplink bands apply.

Low NR band inter-band CA configurations in which the UE is allowed to indicate support of the configuration via switching featureSetCombinationLowBandSwitching-r19 are indicated with the corresponding note in the configuration tables in sub-clause 5.5A.3.1.

#### 5.5A.3.1 Configurations for inter-band CA (two bands)

##### Table 5.5A.3.1-1a ~ Table 5.5A.3.1-1e

Table 5.5A.3.1-1a: NR CA configurations and bandwidth
combinations sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n1A-n3A | n38CA_n1A-n3A8 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n1 | 5, 10, 15, 20 | 2 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3B | CA_n1A-n3A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
| CA_n1B-n3A | CA_n1A-n3A | n1 | CA_n1B_BCS0 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n1 | CA_n1B_BCS0 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1A-n3(2A) | CA_n1A-n3A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n1 | 5, 10, 15, 20 | 2 |
|  |  | n3 | CA_n3(2A)_BCS1 |  |
| CA_n1(2A)-n3A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1(2A)-n3(2A) | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3(2A)_BCS1 |  |
| CA_n1(2A)-n3B | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
| CA_n1A-n5A | CA_n1A-n5A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1(2A)-n5A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
| CA_n1A-n7A | n78CA_n1A-n7A8 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7B | n78CA_n1A-n7ACA_n7B | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
| CA_n1A-n7(2A) | CA_n1A-n7A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
| CA_n1(2A)-n7A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
| CA_n1A-n8A | CA_n1A-n8A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 of 38.101-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 of 38.101-1 |  |
| CA_n1(2A)-n8A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n1A-n18A | CA_n1A-n18A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n18 | 5, 10, 15 |  |
| CA_n1A-n20A | CA_n1A-n20A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n26A | n268CA_n1A-n26A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n26 | 5, 10, 15, 20 |  |
| CA_n1A-n26(2A) | n268CA_n26(2A)CA_n1A-n26A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n1A-n28A | CA_n1A-n28A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1(2A)-n28A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
| CA_n1A-n38A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1(2A)-n38A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1A-n40A | CA_n1A-n40A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n1 | 5, 10, 15, 20 | 1 |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n40B | - | n1 | 5, 10, 15, 20 | 0 |
|  |  | n40 | CA_n40B_BCS0 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | CA_n40B_BCS4 and 5 |  |
| CA_n1A-n41A | n418,9CA_n1A-n41A8 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n46A | CA_n1A-n46A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | 10, 20, 40, 60, 80 |  |
| CA_n1A-n46C | CA_n1A-n46A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46C_BCS0 |  |
| CA_n1A-n46D | CA_n1A-n46A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46D_BCS0 |  |
| CA_n1A-n46(2A) | CA_n1A-n46A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46(2A)_BCS0 |  |
| CA_n1A-n67A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n71A | CA_n1A-n71A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n1A-n74A | CA_n1A-n74A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n74 | 5, 10, 15, 20 |  |
| CA_n1A-n75A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n75 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n77A | n778,9CA_n1A-n77A8 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n77(2A) | n778,9CA_n1A-n77A8CA_n77(2A)8 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n1A-n77(3A) | n778,9CA_n1A-n77A8CA_n77(2A)8 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n1A-n78A | n18n788,9CA_n1A-n78A8,13, 14 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40 | 2 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20 | 3 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n78(2A) | n788,9CA_n1A-n78A8,13, 14 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n78 | CA_n78(2A)_BCS1 |  |
|  | n788,9CA_n78(2A)8CA_n1A-n78A8, 13, 14 | n1 | 5, 10, 15, 20 | 2 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n78C | n788,9CA_n78C8CA_n1A-n78A8,13,14 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78C_BCS0 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n78 | CA_n78C_BCS0 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40 | 2 |
|  |  | n78 | CA_n78C_BCS0 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 3 |
|  |  | n78 | CA_n78C_BCS1 |  |
|  | n788,9CA_n78C8CA_n1A-n78A8,13,14CA_n1A-n78C | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n1A-n78(A-C) | CA_n78CCA_n1A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n1A-n78D | CA_n78CCA_n1A-n78ACA_n1A-n78C | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78D_BCS4 and 5 |  |
| CA_n1(2A)-n78A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n79A | n798,9CA_n1A-n79A8 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n79C | CA_n1A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  |  | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n1(2A)-n79A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n79 | 40, 60, 80, 100 |  |
|  |  | n1 | CA_n1(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1(2A)-n79C | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  |  | n1 | CA_n1(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n1A-n102A | CA_n1A-n102A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n1A-n102(2A) | CA_n1A-n102A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n1A-n102B | CA_n1A-n102ACA_n1A-n102B | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n1A-n102C | CA_n1A-n102ACA_n1A-n102C | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n1A-n102D | CA_n1A-n102A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n1A-n102E | CA_n1A-n102A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n1A-n105A | CA_n1A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |

Table 5.5A.3.1-1b: NR CA configurations and bandwidth combinations
sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n2A-n5A | n28CA_n2A-n5A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  | CA_n2A-n5A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5B | CA_n2A-n5ACA_n5B | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | CA_n5B_BCS0 |  |
|  |  | n2 | See n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
| CA_n2(2A)-n5A | CA_n2A-n5A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5B | CA_n2A-n5ACA_n5B | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
| CA_n2A-n7A | CA_n2A-n7A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
| CA_n2A-n7(2A) | CA_n2A-n7A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
| CA_n2(2A)-n7A | CA_n2A-n7A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
| CA_n2A-n12A | CA_n2A-n12A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
| CA_n2(2A)-n12A | CA_n2A-n12A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n12 | 5, 10, 15 |  |
| CA_n2A-n14A | n28n148CA_n2A-n14A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n2 | See n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | See n14 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n14A | CA_n2A-n14A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n14 | See n14 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n29A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
| CA_n2(2A)-n29A | - | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n29 | 5, 10 |  |
| CA_n2A-n30A | CA_n2A-n30A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n2 | See n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | See n30 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n30A | CA_n2A-n30A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n30 | See n30 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n38A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n38 | 5, 10, 15, 20, 40 |  |
| CA_n2A-n41A | CA_n2A-n41A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
| CA_n2(2A)-n41A | CA_n2A-n41A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n48A | CA_n2A-n48A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 |  |
|  | n28CA_n2A-n48A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48B | CA_n48BCA_n2A-n48A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48B_BCS2 |  |
|  | CA_n48BCA_n2A-n48ACA_n2A-n48B | n2 | See n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
| CA_n2A-n48C | CA_n2A-n48A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
| CA_n2A-n48(2A) | CA_n2A-n48A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n2 | See n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
| CA_n2A-n48(A-B) | CA_n2A-n48A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(A-B)_BCS0 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48(A-B)_BCS1 |  |
|  |  | n2 | See n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(A-B)_BCS 4 and 5 |  |
| CA_n2(2A)-n48A | CA_n2A-n48A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n48 | See n48 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n48B | CA_n48BCA_n2A-n48ACA_n2A-n48B | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
| CA_n2(2A)-n48(2A) | CA_n2A-n48A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
| CA_n2(3A)-n48A | CA_n2A-n48A | n2 | CA_n2(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n48 | See n48 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n66A | n28n668 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  | n28n668CA_n2A-n66A | n2 | 5, 10, 15, 20 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  | CA_n2A-n66A | n2 | See n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | See n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n66A | CA_n2A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | See n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n66(2A) | CA_n2A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n2 | See n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n2(2A)-n66(2A) | CA_n2A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n2(2A)-n66(3A) | CA_n2A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
| CA_n2A-n66(3A) | CA_n2A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(3A)_BCS4 and 5 |  |
| CA_n2A-n66B | CA_n2A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66B_BCS0 |  |
| CA_n2A-n71A | CA_n2A-n71A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | - | n2 | See n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | See n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n71A | CA_n2A-n71A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | - | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | See n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n77A | n28n778,9CA_n2A-n77A8,13,14 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n77(2A) | n778,9CA_n2A-n77A8CA_n77(2A)7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n2A-n77B | CA_n2A-n77A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77B_BCS0 |  |
|  | - | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77B_BCS 4 and 5 |  |
| CA_n2A-n77C | n778, 9CA_n77C8,9CA_n2A-n77A8,13,14 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77C_BCS0 |  |
|  | n778, 9CA_n77CCA_n2A-n77A8CA_n2A-n77C | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2(2A)-n77A | n778, 9CA_n2A-n77A8,13,14 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n77B | CA_n2A-n77A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77B_BCS0 |  |
|  | - | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77B_BCS 4 and 5 |  |
| CA_n2(2A)-n77(2A) | n778,9CA_n2A-n77A8CA_n77(2A)7 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n2A-n77(3A) | CA_n2A-n77A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
| CA_n2(2A)-n77C | n778,9CA_n77C8,9CA_n2A-n77A8,13,14 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n778,9CA_n77C8,9CA_n2A-n77A13,14CA_n2A-n77C | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2(3A)-n77A | CA_n2A-n77A | n2 | CA_n2(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n78A | CA_n2A-n78A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | See n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n78(2A) | CA_n2A-n78A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS1 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n2 | See n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |

Table 5.5A.3.1-1c: NR CA configurations and bandwidth combinations
sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n3A-n5A | CA_n3A-n5A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
| CA_n3(2A)-n5A | - | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
| CA_n3A-n7A | n38n78CA_n3A-n7A8 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7B | n78CA_n3A-n7ACA_n7B | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
| CA_n3A-n7(2A) | CA_n3A-n7A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
| CA_n3(2A)-n7A | CA_n3A-n7A | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  | - | n3 | CA_n3(2A)_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
| CA_n3(2A)-n7(2A) | CA_n3A-n7A | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
| CA_n3B-n7A | n78CA_n3A-n7A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  | n78CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
| CA_n3B-n7B | n78CA_n3A-n7ACA_n7B | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n3 | CA_n3B_BCS 4 and 5 | 4 and 5 |
|  |  | n7 | CA_n7B_BCS 4 and 5 |  |
|  | n78CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
| CA_n3A-n8A | CA_n3A-n8A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | See n8 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3(2A)-n8A | CA_n3A-n8A | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n3A-n18A | CA_n3A-n18A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n20A | n38CA_n3A-n20A8 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n26A | n268CA_n3A-n26A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n26 | 5, 10, 15, 20 |  |
| CA_n3A-n26(2A) | n268CA_n26(2A)CA_n3A-n26A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n3B-n26A | n268CA_n3A-n26A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  | CA_n3Bn268 | n3 | CA_n3B_BCS1 | 1 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
| CA_n3B-n26(2A) | n268CA_n26(2A)CA_n3A-n26A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  | CA_n3Bn268 | n3 | CA_n3B_BCS1 | 1 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n3A-n28A | n38CA_n3A-n28A8 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 2 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40 | 3 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3B-n28A | CA_n3A-n28A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
| CA_n3(2A)-n28A | - | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
| CA_n3A-n34A | CA_n3A-n34A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n34 | 5, 10, 15 |  |
|  |  | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n34 | See n34 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n38A | CA_n3A-n38A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n38 | 5, 10, 15, 20, 40 |  |
| CA_n3B-n38A | - | n3 | CA_n3B_BCS0 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n3(2A)-n38A | - | n3 | CA_n3(2A)_BCS1 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n3A-n39A | n3 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
| CA_n3A-n40A | n408,9CA_n3A-n40A8 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35,40 | 2 |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n41A | n418,9CA_n3A-n41A8 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30 | 1 |
|  |  | n41 | 10, 15, 20, 40, 50, 60 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 | 2 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 3 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n41B | CA_n3A-n41A | n3 | 5, 10, 15, 20 | 0 |
|  |  | n41 | CA_n41B_BCS0 |  |
| CA_n3A-n41C | n418CA_n41C8CA_n3A-n41A8CA_n3A-n41C8 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n41 | CA_n41C_BCS0 |  |
|  |  | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS4 and 5 |  |
| CA_n3A-n41(2A) | CA_n3A-n41A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n41 | CA_n41(2A)_BCS0 |  |
|  |  | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS4 and 5 |  |
| CA_n3(2A)-n41A | CA_n3A-n41A | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n67A | n38 | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n71A | CA_n3A-n71A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n3(2A)-n71A | CA_n3A-n71A | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n3A-n74A | CA_n3A-n74A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n74 | 5, 10, 15, 20 |  |
| CA_n3A-n75A | - | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n75 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n77A | n778,9CA_n3A-n77A8 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35,40 | 1 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n77(2A) | n778,9CA_n77(2A)8CA_n3A-n77A8 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35,40 | 1 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n3A-n77(3A) | n778,9CA_n77(2A)8CA_n3A-n77A8 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n3A-n78A | n38n788,9CA_n3A-n78A8,13, 14 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n78C | n788,9CA_n78C8CA_n3A-n78A8,13,14 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | n788,9CA_n78C8CA_n3A-n78A8,13,14 | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n78 | CA_n78C_BCS0 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 | 2 |
|  |  | n78 | CA_n78C_BCS1 |  |
|  | n788,9CA_n78C8CA_n3A-n78A8,13,14CA_n3A-n78C | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n3A-n78(2A) | n38n788,9CA_n3A-n78A8,13, 14CA_n78(2A)8 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3A-n78(A-C) | CA_n78CCA_n3A-n78A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n3(2A)-n78A | CA_n3A-n78A8,14 | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | CA_n3(2A)_BCS1 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3(2A)-n78C | CA_n78CCA_n3A-n78ACA_n3A-n78C | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n3B-n78A | n788,9CA_n3A-n78A8,13,14 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | CA_n3B_BCS4 and 5 | 4 and 5 |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  | CA_n3BCA_n3A-n78A8,13,14 | n3 | CA_n3B_BCS1 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n78C | n788,9CA_n78C8CA_n3A-n78A8,13,14 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3BCA_n3A-n78A8,13,14 | n3 | CA_n3B_BCS1 | 1 |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3B-n78(2A) | n788,9CA_n3A-n78A8,13,14 | n3 | CA_n3B_BCS0 | 0 |
|  | CA_n78(2A)8 | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n78(2A)CA_n3A-n78A8,13,14 | n3 | CA_n3B_BCS4 and 5 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3B-n78(A-C) | CA_n78CCA_n3A-n78A | n3 | CA_n3B_BCS1 | 0 |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n3A-n79A | n38n798,9CA_n3A-n79A8 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3(2A)-n79A | CA_n3A-n79A | n3 | CA_n3(2A)_BCS1 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n3 | CA_n3(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n79C | n38n798,9CA_n79C8CA_n3A-n79A8 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  | CA_n79CCA_n3A-n79ACA_n3A-n79C | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n3(2A)-n79C | CA_n3A-n79A | n3 | CA_n3(2A)_BCS1 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  |  | n3 | CA_n3(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n3B-n79A | - | n3 | CA_n3B_BCS0 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n3 | CA_n3B_BCS4 and 5 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3B-n79C | - | n3 | CA_n3B_BCS0 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  |  | n3 | CA_n3B_BCS4 and 5 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n3A-n102A | CA_n3A-n102A | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n3A-n102(2A) | CA_n3A-n102A | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n3A-n102B | CA_n3A-n102ACA_n3A-n102B | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n3A-n102C | CA_n3A-n102ACA_n3A-n102C | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n3A-n102D | CA_n3A-n102A | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n3A-n102E | CA_n3A-n102A | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n3A-n104A | CA_n3A-n104A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n104 | 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n104 | n104 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n104C | CA_n104CCA_n3A-n104ACA_n3A-n104C | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n104 | CA_n104C_BCS0 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n104 | CA_n104C_BCS 4 and 5 |  |
| CA_n3A-n105A | CA_n3A-n105A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |

Table 5.5A.3.1-1d: NR CA configurations and bandwidth combinations  
sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n5A-n7A | CA_n5A-n7A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n7B | CA_n5A-n7ACA_n7B | n5 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
| CA_n5A-n8A | n5A15, CA_n5A-n8A19 | n5 | 5, 10 | 0 |
|  |  | n8 | 5, 10 |  |
| CA_n5A-n12A | CA_n5A-n12A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
| CA_n5B-n12A | CA_n5A-n12ACA_n5B | n5 | CA_n5B_BCS0 | 0 |
|  |  | n12 | 5, 10, 15 |  |
| CA_n5A-n13A | CA_n5A-n13A | n5 | 5, 10, 15, 20 | 4 and 5 |
|  |  | n13 | 5, 10 |  |
| CA_n5B-n13A | CA_n5A-n13A | n5 | CA_n5B_BCS0 | 0 |
|  |  | n13 | 5, 10 |  |
| CA_n5A-n14A | CA_n5A-n14A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n14A | CA_n5A-n14ACA_n5B | n5 | CA_n5B_BCS0 | 0 |
|  |  | n14 | 5, 10 |  |
| CA_n5A-n25A | CA_n5A-n25A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n25(2A) | CA_n5A-n25A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
| CA_n5A-n28A | CA_n5A-n28A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
| CA_n5A-n29A17 | - | n5 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n29A | CA_n5B | n5 | CA_n5B_BCS0 | 0 |
|  |  | n29 | 5, 10 |  |
| CA_n5A-n30A | CA_n5A-n30A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n40A | CA_n5A-n40A | n5 | 5, 10, 15, 20, 251 | 0 |
|  |  | n40 | 55, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80,90,100 |  |
| CA_n5A-n41A | CA_n5A-n41A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48A | CA_n5A-n48A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48(2A) | CA_n5A-n48A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
| CA_n5A-n48B | CA_n48BCA_n5A-n48A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48B_BCS2 |  |
|  | CA_n48BCA_n5A-n48ACA_n5A-n48B | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
| CA_n5A-n48C | CA_n5A-n48A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
| CA_n5A-n48(A-B) | CA_n5A-n48A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(A-B)_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48(A-B)_BCS1 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(A-B)_BCS 4 and 5 |  |
| CA_n5B-n48A | CA_n5BCA_n5A-n48ACA_n5B-n48A | n5 | CA_n5B_BCS 4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n48B | CA_n5BCA_n48BCA_n5A-n48ACA_n5A-n48B | n5 | CA_n5B_BCS 4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
| CA_n5B-n48(2A) | CA_n5BCA_n5A-n48A | n5 | CA_n5B_BCS 4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
| CA_n5A-n66A | n668CA_n5A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n66B | CA_n5A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66B_BCS0 |  |
| CA_n5B-n66A | CA_n5A-n66ACA_n5B | n5 | CA_n5B_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | CA_n5B_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n66B | CA_n5A-n66A | n5 | CA_n5B_BCS0 | 0 |
|  |  | n66 | CA_n66B_BCS0 |  |
| CA_n5A-n66(2A) | CA_n5A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n5A-n66(3A) | CA_n5A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
| CA_n5B-n66(2A) | CA_n5A-n66ACA_n5B | n5 | CA_n5B_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n5 | CA_n5B_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n5A-n71A | - | n5 | 5, 10, 15, 20 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n77A | n778,9CA_n5A-n77A8,13,14 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n77B | CA_n5A-n77An778,9 | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77B_BCS 4 and 5 |  |
| CA_n5A-n77(2A) | n778,9CA_n5A-n77A8CA_n77(2A)8 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n5A-n77(3A) | n778,9CA_n77(2A)8CA_n5A-n77A8 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n5(2A)-n77A | n778,9CA_n5A-n77A8 | n5 | CA_n5(2A)_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n77C | n778,9CA_n5A-n77A8,13,14CA_n77C8,9 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n778,9CA_n5A-n77A8,13,14CA_n77C8,9CA_n5A-n77C | n5 | See n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n5(2A)-n77C | n778,9CA_n77CCA_n5A-n77A8 | n5 | CA_n5(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n5 | CA_n5(2A)_BCS0 | 1 |
|  |  | n77 | CA_n77C_BCS1 |  |
| CA_n5B-n77A | n778,9CA_n5A-n77A8,13,14CA_n5B | n5 | CA_n5B_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n778,9CA_n5A-n77A8,13,14CA_n5B | n5 | CA_n5B_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n77C | n778,9CA_n5A-n77A8,13,14CA_n5BCA_n77C8,9 | n5 | CA_n5B_BCS0 | 0 |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n5 | CA_n5B_BCS0 | 1 |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n778,9CA_n5A-n77A8,13,14CA_n5BCA_n77C8,9CA_n5A-n77C | n5 | CA_n5B_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n5A-n78A | n788,9CA_n5A-n78A8 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n78(2A) | n788,9CA_n5A-n78A8CA_n78(2A)8 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n5A-n78C | CA_n5A-n78A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78C_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n78 | CA_n78C_BCS1 |  |
|  | CA_n78CCA_n5A-n78C | n5 | See n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n5A-n78(A-C) | CA_n78CCA_n5A-n78A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n5A-n79A | CA_n5A-n79A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n79C | CA_n5A-n79A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n5A-n105A | CA_n5A-n105A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |

Table 5.5A.3.1-1e: NR CA configurations and bandwidth combinations
sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n7A-n8A | CA_n7A-n8A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n7(2A)-n8A | CA_n7A-n8A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n7A-n12A | CA_n7A-n12A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n7 | See n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n12 | See n12 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n20A | n78CA_n7A-n20A8 | n7 | See n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | See n20 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n25A | CA_n7A-n25A | n7 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n25(2A) | CA_n7A-n25A | n7 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
| CA_n7(2A)-n25A | CA_n7A-n25A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n7(2A)-n25(2A) | CA_n7A-n25A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
| CA_n7A-n26A | n78n268CA_n7A-n26A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n26 | 5, 10, 15, 20 |  |
| CA_n7A-n26(2A) | n78n268CA_n26(2A)CA_n7A-n26A | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n7B-n26A | n78n268CA_n7A-n26ACA_n7B | n7 | CA_n7B_BCS0 | 0 |
|  |  | n26 | 5, 10, 15, 20 |  |
| CA_n7B-n26(2A) | n78n268CA_n7BCA_n26(2A)CA_n7A-n26A | n7 | CA_n7B_BCS0 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n7A-n28A | n78CA_n7A-n28A8 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7B-n28A | n78CA_n7A-n28ACA_n7B | n7 | CA_n7B_BCS0 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
| CA_n7A-n29A | - | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n40A | CA_n7A-n40A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n46A | CA_n7A-n46A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | 20, 40, 60, 80 |  |
| CA_n7A-n46C | CA_n7A-n46A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46C_BCS0 |  |
| CA_n7A-n46D | CA_n7A-n46A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46D_BCS0 |  |
| CA_n7A-n46(2A) | CA_n7A-n46A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46(2A)_BCS0 |  |
| CA_n7A-n66A | CA_n7A-n66A | n7 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 10, 15, 20, 40 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n66(2A) | CA_n7A-n66A | n7 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n7(2A)-n66A | CA_n7A-n66A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n7(2A)-n66(2A) | CA_n7A-n66A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n7A-n67A | - | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n71A | - | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | CA_n7A-n71A | n7 | See n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | See n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n75A | - | n7 | 10, 15, 20 | 0 |
|  |  | n75 | 5, 10, 15, 20 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n77A | n778,9CA_n7A-n77A8,13,14 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7(2A)-n77A | n778,9CA_n7A-n77A8 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n77(2A) | n778,9CA_n77(2A)8CA_n7A-n77A8 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n7(2A)-n77(2A) | n778,9 CA_n77(2A)8CA_n7A-n77A8 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7A-n77(3A) | n778,9CA_n77(2A)8CA_n7A-n77A8 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n7(2A)-n77(3A) | n778,9CA_n77(2A)8CA_n7A-n77A8 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
| CA_n7A-n78A | n78n788,9CA_n7A-n78A8,13, 14 | n7 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n78C | n78n788,9CA_n7A-n78A8,13,14CA_n78C8 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n7A-n78(A-C) | CA_n78CCA_n7A-n78A | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n7B-n78A | n78n788,9CA_n7A-n78A8,13,14CA_n7B | n7 | CA_n7B_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n7 | CA_n7B_BCS4 and 5 | 4 and 5 |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7B-n78(2A) | n78n788,9CA_n7A-n78A8,13,14CA_n7B | n7 | CA_n7B_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | n78CA_n78(2A)8CA_n7A-n78A8,13,14 | n7 | CA_n7B_BCS4 and 5 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n7B-n78C | n78n788,9CA_n7BCA_n7A-n78A8,13,14CA_n78C8 | n7 | CA_n7B_BCS0 | 0 |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n7A-n78(2A) | n78n788,9CA_n7A-n78A8,13, 14CA_n78(2A)8 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n7 | See n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n7(2A)-n78A | n788,9CA_n7A-n78A8 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n7 | CA_n7(2A)_BCS0 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n7 | CA_n7(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7B-n78(A-C) | CA_n7BCA_n7A-n78ACA_n78C | n7 | CA_n7B_BCS0 | 0 |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n7(2A)-n78(2A) | n788,9CA_n7A-n78A8CA_n78(2A) | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  |  | n7 | CA_n7(2A)_BCS0 | 1 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n7 | CA_n7(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n7A-n79A | - | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n79C | - | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n7A-n102A | CA_n7A-n102A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n7A-n102(2A) | CA_n7A-n102A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n7A-n102B | CA_n7A-n102ACA_n7A-n102B | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n7A-n102C | CA_n7A-n102ACA_n7A-n102C | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n7A-n102D | CA_n7A-n102A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n7A-n102E | CA_n7A-n102A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n7A-n105A | CA_n7A-n105A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n8A-n20A | CA_n8A-n20A | n8 | 5, 10, 15, 20 | 0 |
|  |  | n20 | 5, 10, 15, 20 |  |
| CA_n8A-n28A | CA_n8A-n28A | n8 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n8 | 5, 10, 15, 20 | 1 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
| CA_n8A-n34A | n88n348,9CA_n8A-n34A8 | n8 | 5, 10, 15, 20 | 0 |
|  |  | n34 | 5, 10, 15 |  |
| CA_n8A-n38A | - | n8 | 5, 10, 15, 20 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n8A-n39A | n88n398,9CA_n8A-n39A8 | n8 | 5, 10, 15, 20 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n40A | n88n408,9CA_n8A-n40A8 | n8 | 5, 10, 15, 20 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n41A | n88n418,9CA_n8A-n41A8 | n8 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n8 | 5, 10, 15, 20 | 1 |
|  |  | n41 | 10, 15, 20, 40, 50, 60 |  |
|  |  | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n41C | n88n418,9CA_n41CCA_n8A-n41A8CA_n8A-n41C | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS4 and 5 |  |
| CA_n8A-n50A | CA_n8A-n50A | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n50 | n50 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n75A | - | n8 | 5, 10, 15, 20 | 0 |
|  |  | n75 | 5, 10, 15, 20 |  |
|  |  | n8 | 5, 10,15, 20 | 1 |
|  |  | n75 | 5, 10,15, 20, 25, 30, 40, 50 |  |
| CA_n8A-n77A | n778,9CA_n8A-n77A8 | n8 | 5, 10, 15, 20 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n8A-n77(2A) | - | n8 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  | CA_n8A-n77A | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n8A-n78A | n788,9CA_n8A-n78A8,13 | n8 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n8 | 5, 10, 15, 20 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n78C | CA_n8A-n78A | n8 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n8A-n78ACA_n8A-n78CCA_n78C | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n8A-n78(2A) | CA_n8A-n78A | n8 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS1 |  |
|  |  | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n8A-n79A | n88n798,9CA_n8A-n79A8 | n8 | 5, 10, 15, 20 | 0 |
|  |  | n79 | 10, 20, 40, 50, 60, 80, 100 |  |
|  |  | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n79C | CA_n79CCA_n8A-n79A | n8 | 5, 10, 15, 20 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  | CA_n79CCA_n8A-n79ACA_n8A-n79C | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n8A-n104A | CA_n8A-n104A | n8 | 5, 10, 15, 20, 25, 30, 35 | 0 |
|  |  | n104 | 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n104 | n104 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n104C | CA_n104CCA_n8A-n104ACA_n8A-n104C | n8 | 5, 10, 15, 20, 25, 30, 35 | 0 |
|  |  | n104 | CA_n104C_BCS0 |  |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n104 | CA_n104C_BCS 4 and 5 |  |

##### Table 5.5A.3.1-1f ~ Table 5.5A.3.1-1j

Table 5.5A.3.1-1f: NR CA configurations and bandwidth combinations
sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n12A-n25A | CA_n12A-n25A | n12 | 5, 10, 15 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n12 | n12 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
| CA_n12A-n29A18 | - | n12 | n12 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
| CA_n12A-n30A | CA_n12A-n30A | n12 | 5, 10, 15 | 0 |
|  |  | n30 | 5, 10 |  |
| CA_n12A-n41A | - | n12 | 5, 10, 15 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n12 | n12 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n12A-n48A | - | n12 | 5, 10, 15 | 0 |
|  |  | n48 | 10, 15, 20, 30, 40 |  |
| CA_n12A-n66A | CA_n12A-n66A | n12 | 5, 10, 15 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n12 | n12 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n12A-n66(2A) | CA_n12A-n66A | n12 | 5, 10, 15 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n12A-n66(3A) | CA_n12A-n66A | n12 | 5, 10, 15 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
| CA_n12A-n71A | - | n12 | 5, 10, 15 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n12A-n77A | n778, 9CA_n12A-n77A8 | n12 | 5, 10, 15 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n12 | n12 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n12A-n77B | CA_n12A-n77A | n12 | n12 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77B_BCS 4 and 5 |  |
| CA_n12A-n77C | CA_n12A-n77A | n12 | n12 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n12A-n77(2A) | n778, 9CA_n12A-n77A8 | n12 | 5, 10, 15 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n12A-n78A | CA_n12A-n78A | n12 | 5, 10, 15 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n12A-n78(2A) | CA_n12A-n78A | n12 | 5, 10, 15 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n13A-n25A | CA_n13A-n25A | n13 | 5, 10 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n13A-n66A | CA_n13A-n66A | n13 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n13 | 5, 10, | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n13A-n66B | CA_n13A-n66A | n13 | 5, 10 | 0 |
|  |  | n66 | CA_n66B_BCS0 |  |
| CA_n13A-n66(2A) | CA_n13A-n66A | n13 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n13A-n77A | n778, 9CA_n13A-n77A8 | n13 | 5, 10 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n13A-n77(2A) | n778,9CA_n77(2A)8CA_n13A-n77A8 | n13 | 5, 10 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n13A-n77C | n778,9CA_n77CCA_n13A-n77A8 | n13 | 5, 10 | 0 |
|  |  | n77 | CA_n77C_BCS1 |  |
| CA_n14A-n29A18 | - | n14 | n12 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
| CA_n14A-n30A | n148CA_n14A-n30A | n14 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
| CA_n14A-n66A | n148n668CA_n14A-n66A | n14 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n14A-n66(2A) | CA_n14A-n66A | n14 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n14A-n66(3A) | CA_n14A-n66A | n14 | 5, 10 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
| CA_n14A-n77A | n148n778, 9CA_n14A-n77A8 | n14 | 5, 10 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n14A-n77(2A) | n778, 9CA_n14A-n77A8 | n14 | 5, 10 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n18A-n28A23 | CA_n18A-n28A | n18 | 5, 10, 15 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n18A-n40A | n408,9CA_n18A-n40A8,9 | n18 | 5, 10, 15 | 0 |
|  |  | n40 | 10, 15, 20, 30, 40 |  |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n18A-n41A | n418,9CA_n18A-n41A8,9 | n18 | 5, 10, 15 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n18A-n74A | CA_n18A-n74A | n18 | 5, 10, 15 | 0 |
|  |  | n74 | 5, 10, 15, 20 |  |
| CA_n18A-n77A | n778,9CA_n18A-n77A8,9 | n18 | 5, 10, 15 | 0 |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n18 | See n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n18A-n77(2A) | n778,9CA_n18A-n77A8,9CA_n77(2A)8 | n18 | 5, 10, 15 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n18 | See n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n18A-n77(3A) | n778,9CA_n18A-n77A8,9CA_n77(2A)8 | n18 | 5, 10, 15 | 0 |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n18A-n78A | CA_n18A-n78A | n18 | 5, 10, 15 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n18 | See n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n18A-n78(2A) | CA_n18A-n78A | n18 | 5, 10, 15 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n18 | See n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |

Table 5.5A.3.1-1g: NR CA configurations and bandwidth combinations
sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n20A-n28A22 | CA_n20A-n28A | n20 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n20 | 5, 10, 15, 20 | 1 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n20 | 5, 10, 15, 20 | 2 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n20A-n40A | - | n20 | 5, 10, 15, 20 | 0 |
|  |  | n40 | 5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n20A-n41A | CA_n20A-n41A | n20 | 5,10,15,20 | 0 |
|  |  | n41 | 5,10,15,20,25,30,35,40,45,50,60,70,80,90,100 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n20A-n67A | - | n20 | 5, 10, 15, 20 | 0 |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n20A-n71A | CA_n20A-n71A | n20 | 5,10,15,20 | 0 |
|  |  | n71 | 5,10,15,20 |  |
| CA_n20A-n75A | - | n20 | 5, 10, 15, 20 | 0 |
|  |  | n75 | 5, 10, 15, 20 |  |
|  |  | n20 | 5, 10,15, 20 | 1 |
|  |  | n75 | 5, 10,15, 20, 25, 30, 40, 50 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n20A-n77A | CA_n20A-n77A | n20 | 5, 10, 15, 20 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n20A-n77(2A) | CA_n20A-n77A | n20 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n20A-n78A | CA_n20A-n78A | n20 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n20 | See n20 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n20A-n78C | - | n20 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n20A-n78(2A) | CA_n20A-n78ACA_n78(2A) | n20 | See n20 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n24A-n41A | CA_n24A-n41A | n24 | 5, 10 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n24 | See n24 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n24A-n41(2A) | CA_n24A-n41A | n24 | 5, 10 | 0 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n24 | See n24 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS4 and 5 |  |
| CA_n24A-n48A | CA_n24A-n48A | n24 | 5, 10 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 |  |
| CA_n24A-n48B | CA_n24A-n48A | n24 | 5, 10 | 0 |
|  |  | n48 | CA_n48B_BCS1 |  |
| CA_n24A-n48(2A) | CA_n24A-n48A | n24 | 5, 10 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
| CA_n24A-n48(3A) | CA_n24A-n48A | n24 | 5, 10 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
| CA_n24A-n77A | CA_n24A-n77A | n24 | 5, 10 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n24 | See n24 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n24A-n77C | CA_n24A-n77A | n24 | 5, 10 | 0 |
|  |  | n77 | CA_n77C_BCS1 |  |
| CA_n24A-n77(2A) | CA_n24A-n77A | n24 | 5, 10 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n24 | See n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n25A-n29A | - | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n38A | CA_n25A-n38A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n25(2A)-n38A | CA_n25A-n38A | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n25A-n41A | n258n418,9CA_n25A-n41A8,9,13,14 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | See n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A | n258n418,9CA_n25A-n41A8,9,13,14 | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n25 | CA_n25(2A)_BCS1 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41C | n258n418,9CA_n25A-n41A8,9CA_n25A-n41C8,9CA_n41C8,9 | n25 | CA_n25(2A)_BCS1 | 0 |
|  |  | n41 | CA_n41C_BCS2 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
| CA_n25(2A)-n41(2A) | n258n418,9CA_n25A-n41A8,9 | n25 | CA_n25(2A)_BCS1 | 0 |
|  |  | n41 | CA_n41(2A)_BCS3 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
| CA_n25A-n41C | n258n418,9CA_n25A-n41A8,9,13,14CA_n41C8,9CA_n25A-n41C8,9 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | CA_n41C_BCS0 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | CA_n41C_BCS1 |  |
|  | n258n418,9CA_n25A-n41A8,9,13,14CA_n41C8,9CA_n25A-n41C8,9,13,14 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
| CA_n25A-n41(2A) | n258n418,9CA_n25A-n41A8,9,13,14 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | CA_n41(2A)_BCS3 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
| CA_n25A-n41(3A) | n258n418,9CA_n25A-n41A8 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | CA_n41(3A)_BCS0 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
| CA_n25A-n41(A-C) | n258n418,9CA_n25A-n41A8CA_n25A-n41C8CA_n41C8,9 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | CA_n41(A-C)_BCS0 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
| CA_n25(2A)-n41(3A) | n258n418,9CA_n25A-n41A8 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41(A-C) | n258n418,9CA_n41C8CA_n25A-n41A8CA_n25A-n41C | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
| CA_n25A-n46A | - | n25 | 5, 10, 15, 20 | 0 |
|  |  | n46 | 20, 40, 60, 80 |  |
| CA_n25A-n48A | CA_n25A-n48A | n25 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 |  |
| CA_n25A-n48(2A) | CA_n25A-n48A | n25 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
| CA_n25A-n48C | CA_n25A-n48A | n25 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n48 | CA_n48C_BCS0 |  |
| CA_n25A-n66A | n258n668CA_n25A-n66A8,9 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 30, 40 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66(2A) | n258n668CA_n25A-n66A8 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n66A | n258n668CA_n25A-n66A8 | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n66 | 10, 15, 20, 30, 40 |  |
|  |  | n25 | CA_n25(2A)_BCS0 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n25 | CA_n25(2A)_BCS1 | 2 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n66(2A) | n258n668CA_n25A-n66A8 | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n25 | CA_n25(2A)_BCS0 | 1 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n25 | CA_n25(2A)_BCS1 | 2 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n25(3A)-n66A | n258n668CA_n25A-n66A8 | n25 | CA_n25(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(3A)-n66(2A) | n258n668CA_n25A-n66A8 | n25 | CA_n25(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n25A-n71A | n258n718CA_n25A-n71A8,9 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n71B | n258n718CA_n25A-n71A8 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | CA_n71B_BCS0 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n71 | CA_n71B_BCS2 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25A-n71(2A) | n258n718CA_n25A-n71A8 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n71A | n258n718CA_n25A-n71A8 | n25 | CA_n25(2A)_BCS1 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n71(2A) | n258n718CA_n25A-n71A8 | n25 | CA_n25(2A)_BCS1 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n71B | n258n718CA_n25A-n71A8 | n25 | CA_n25(2A)_BCS1 | 0 |
|  |  | n71 | CA_n71B_BCS2 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25(3A)-n71A | n258n718CA_n25A-n71A8 | n25 | CA_n25(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(3A)-n71(2A) | n258n718CA_n25A-n71A8 | n25 | CA_n25(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25(3A)-n71B | n258n718CA_n25A-n71A8 | n25 | CA_n25(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25A-n77A | n258n778,9CA_n25A-n77A8,9,13,14 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n77(2A) | n258n778,9CA_n77(2A)8CA_n25A-n77A8,13,14 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n77(3A) | n778,9CA_n77(2A)8CA_n25A-n77A8 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n25(2A)-n77A | n258n778,9CA_n25A-n77A8,9,13,14 | n25 | CA_n25(2A)_BCS1 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | CA_n25(2A)_BCS0 | 1 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n77(2A) | n258n778,9CA_n25(2A)CA_n77(2A)8CA_n25A-n77A8 | n25 | CA_n25(2A)_BCS1 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n25 | CA_n25(2A)_BCS0 | 1 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n77(3A) | n778,9CA_n25(2A)CA_n77(2A)8CA_n25A-n77A8 | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
| CA_n25A-n78A | n788,9CA_n25A-n78A8 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | See n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n78(2A) | n788,9CA_n25A-n78A8 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n78(2A)8 | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | - | n25 | See n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n25(2A)-n78A | n788,9CA_n25A-n78A8 | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n25 | CA_n25(2A)_BCS0 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | CA_n25(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n78(2A) | n788,9CA_n25A-n78A8 | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS1 |  |
|  |  | n25 | CA_n25(2A)_BCS0 | 1 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n25 | CA_n25(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n25A-n85A | n258CA_n25A-n85A8 | n25 | See n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n85A | CA_n25A-n85A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(3A)-n85A | CA_n25A-n85A | n25 | CA_n25(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |

Table 5.5A.3.1-1h: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n26A-n28A | CA_n26A-n28A16 | n26 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 | 1 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
| CA_n26A-n29A | - | n26 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n29 | 5, 10 |  |
| CA_n26A-n48A | CA_n26A-n48A | n26 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 |  |
| CA_n26A-n48(2A) | CA_n26A-n48A | n26 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
| CA_n26A-n66A | CA_n26A-n66A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n26A-n66(2A) | CA_n26A-n66A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
| CA_n26A-n66(3A) | - | n26 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
| CA_n26A-n70A | CA_n26A-n70A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n26A-n71A | - | n26 | 5, 10, 15, 20 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n26A-n77A | CA_n26A-n77A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n26A-n78A | n268n788,9CA_n26A-n78A8,13,14 | n26 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n26A-n78C | n268n788,9CA_n26A-n78A8,13,14CA_n78C8 | n26 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n26A-n78(A-C) | CA_n78CCA_n26A-n78A | n26 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n26(2A)-n78A | n268n788,9CA_n26(2A)CA_n26A-n78A8,13,14 | n26 | CA_n26(2A)_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n26(2A)-n78C | n268n788,9CA_n26A-n78A8,13,14CA_n26(2A)CA_n78C8 | n26 | CA_n26(2A)_BCS0 | 0 |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n26A-n78(2A) | n268n788,9CA_n26A-n78A8,13,14CA_n78(2A)8 | n26 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n78(2A) | n26 | n26 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n26A-n78A8,13,14 | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n26(2A)-n78(2A) | n268n788,9CA_n26(2A)CA_n78(2A)8CA_n26A-n78A8,13,14 | n26 | CA_n26(2A)_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n26(2A)-n78(A-C) | CA_n26(2A)CA_n26A-n78ACA_n78C | n26 | CA_n26(2A)_BCS0 | 0 |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n28A-n34A | n348,9CA_n28A-n34A8 | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n34 | 5, 10, 15 |  |
| CA_n28A-n38A | - | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n28A-n39A | n398CA_n28A-n39A8 | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n40A | n408,9CA_n28A-n40A8 | n28 | 5, 10, 15, 20 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 | 1 |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n40B | - | n28 | 5, 10, 15, 20 | 0 |
|  |  | n40 | CA_n40B_BCS0 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | CA_n40B_BCS4 and 5 |  |
| CA_n28A-n41A | n418,9CA_n28A-n41A8,13,14 | n28 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n28 | 5, 10, 15, 20, 30 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n41(2A) | CA_n41(2A)CA_n28A-n41A | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS4 and 5 |  |
| CA_n28A-n41B | CA_n28A-n41A | n28 | 5, 10 | 0 |
|  |  | n41 | CA_n41B_BCS0 |  |
| CA_n28A-n41C | n418,9CA_n41C8CA_n28A-n41A8,13,14 | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n41 | CA_n41C_BCS1 |  |
|  | n418,9CA_n41C8CA_n28A-n41A8,13,14CA_n28A-n41C | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS4 and 5 |  |
| CA_n28A-n46A | CA_n28A-n46A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n46 | 20, 40, 60, 80 |  |
| CA_n28A-n46C | CA_n28A-n46A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n46 | CA_n46C_BCS0 |  |
| CA_n28A-n46D | CA_n28A-n46A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n46 | CA_n46D_BCS0 |  |
| CA_n28A-n46(2A) | CA_n28A-n46A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n46 | CA_n46(2A)_BCS0 |  |
| CA_n28A-n50A | CA_n28A-n50A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n50 | 5, 10, 15, 20, 40, 50, 60, 801 |  |
| CA_n28A-n67A18 | - | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n71A | - | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n28A-n74A | CA_n28A-n74A | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n74 | 5, 10, 15, 20 |  |
| CA_n28A-n75A23 | - | n28 | 5, 10, 15, 20 | 0 |
|  |  | n75 | 5, 10, 15, 20 |  |
|  |  | n28 | 5, 10, 15, 20 | 1 |
|  |  | n75 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 | 2 |
|  |  | n75 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | See n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n77A | n778,9CA_n28A-n77A8 | n28 | 5, 10, 15, 20 | 0 |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 | 1 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n77C | CA_n28A-n77A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77C_BCS1 |  |
| CA_n28A-n77(2A) | n778,9CA_n77(2A)8CA_n28A-n77A8 | n28 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 | 1 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n28A-n77(3A) | n778,9CA_n77(2A)8CA_n28A-n77A8 | n28 | 5, 10 | 0 |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n28A-n78A | n788,9CA_n28A-n78A8,13,14 | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n28 | 5, 10, 15, 20, 30 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n78C | n788,9CA_n28A-n78A8,13,14CA_n78C8 | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n28A-n78(2A) | n788,9CA_n78(2A)8CA_n28A-n78A8,13, 14 | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 | 1 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n28A-n78(A-C) | CA_n28A-n78ACA_n78C | n28 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n28A-n79A | n798,9CA_n28A-n79A8,13,14 | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n79C | n798,9CA_n79C8 | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  | n798,9CA_n79C8CA_n28A-n79A8CA_n28A-n79C | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n28A-n94A | - | n28 | 5, 10, 15, 20 | 0 |
|  |  | n94 | 5, 10, 15, 20 |  |
| CA_n28A-n102A | CA_n28A-n102A | n28 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n28A-n102(2A) | CA_n28A-n102A | n28 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n28A-n102B | CA_n28A-n102ACA_n28A-n102B | n28 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n28A-n102C | CA_n28A-n102ACA_n28A-n102C | n28 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n28A-n102D | CA_n28A-n102A | n28 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n28A-n102E | CA_n28A-n102A | n28 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n28A-n105A | - | n28 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n29A-n30A | - | n29 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
| CA_n29A-n48A | - | n29 | 5, 10 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 |  |
| CA_n29A-n66A | n668 | n29 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n29 | 5, 10 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n66B | n668 | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66B_BCS0 |  |
| CA_n29A-n66(2A) | n668 | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n29 | 5, 10 | 1 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  | - | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n29A-n66(3A) | n668 | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  | - | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(3A)_BCS 4 and 5 |  |
| CA_n29A-n70A | n708 | n29 | 5, 10 | 0 |
|  |  | n70 | 5, 10, 15, 201,, 251 |  |
|  | - | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n71A17 | n718 | n29 | 5, 10 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | - | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n71(2A) | - | n29 | 5, 10 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
| CA_n29A-n77A | n778, 9 | n29 | 5, 10 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | - | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n77(2A) | n778, 9 | n29 | 5, 10 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  | CA_n77(2A) | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n29A-n77(3A) | CA_n77(2A) | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |

Table 5.5A.3.1-1i: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n30A-n66A | CA_n30A-n66A | n30 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n30 | See n30 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | See n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n30A-n66(2A) | CA_n30A-n66A | n30 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n30 | See n30 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n30A-n66(3A) | CA_n30A-n66A | n30 | 5, 10 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(3A)_BCS4 and 5 |  |
| CA_n30A-n77A | n778, 9CA_n30A-n77A8 | n30 | 5, 10 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n30 | See n30 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n30A-n77(2A) | n778, 9CA_n77(2A)CA_n30A-n77A8 | n30 | 5, 10 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  | n778, 9CA_n30A-n77A8 | n30 | See n30 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n34A-n39A | n348,9n398CA_n34A-n39A8 | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 |  |
| CA_n34A-n40A | n348,9n408,9CA_n34A-n40A8 | n34 | 5, 10, 15 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n34A-n41A | n348,9n418,9CA_n34A-n41A8 | n34 | 5, 10, 15 | 0 |
|  |  | n41 | 10, 15, 20, 30 ,40 ,50, 60, 70, 80, 90, 100 |  |
|  |  | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n34A-n41C | n348,9n418,9CA_n41CCA_n34A-n41A8CA_n34A-n41C | n34 | 5, 10, 15 | 0 |
|  |  | n41 | CA_n41C_BCS1 |  |
|  |  | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS4 and 5 |  |
| CA_n34A-n79A | n348,9n798,9CA_n34A-n79A8 | n34 | 5, 10, 15 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n34A-n79C | n348,9n798,9CA_n34A-n79A8 | n34 | 5, 10, 15 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  | n348,9n798,9CA_n79CCA_n34A-n79A8CA_n34A-n79C | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n34A-n104A | CA_n34A-n104A | n34 | 5, 10, 15 | 0 |
|  |  | n104 | 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n34 | n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n104 | n104 channel bandwidths in Table 5.3.5-1 |  |
| CA_n34A-n104C | CA_n104CCA_n34A-n104ACA_n34A-n104C | n34 | 5, 10, 15 | 0 |
|  |  | n104 | CA_n104C_BCS0 |  |
|  |  | n34 | n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n104 | CA_n104C_BCS 4 and 5 |  |
| CA_n38A-n40A | - | n38 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n40 | 5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n38A-n66A | CA_n38A-n66A | n38 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 30, 40 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n38A-n66(2A) | CA_n38A-n66A | n38 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n38A-n71A | - | n38 | 5, 10, 15, 20 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n38A-n78A | CA_n38A-n78A | n38 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n38 | See n38 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n38A-n78(2A) | CA_n38A-n78A | n38 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  |  | n38 | 5, 10, 15, 20 | 1 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n38 | See n38 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n38A-n79A | - | n38 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n38 | See n38 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n38A-n79C | - | n38 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  |  | n38 | See n38 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n39A-n40A | n398n408,9CA_n39A-n40A8 | n39 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n39A-n41A | n398n418,9CA_n39A-n41A8 | n39 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n39A-n41C | n398n418,9CA_n41C8CA_n39A-n41A8CA_n39A-n41C8 | n39 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | CA_n41C_BCS0 |  |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS4 and 5 |  |
| CA_n39A-n41(2A) | CA_n39A-n41A | n39 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | CA_n41(2A)_BCS0 |  |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS4 and 5 |  |
| CA_n39A-n79A | n398n798,9CA_n39A-n79A8 | n39 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n39A-n79C | CA_n79CCA_n39A-n79ACA_n39A-n79C | n39 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n40A-n41A | n408,9n418,9CA_n40A-n41A8 | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | 10, 15, 20, 40, 50, 60 |  |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n41B | n418,9CA_n40A-n41A8,9 | n40 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | CA_n41B_BCS0 |  |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41B_BCS4 and 5 |  |
| CA_n40A-n41C | CA_n41CCA_n40A-n41ACA_n40A-n41C | n40 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | CA_n41C_BCS0 |  |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS4 and 5 |  |
| CA_n40A-n50A | CA_n40A-n50A | n40 | n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n50 | n50 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n71A | CA_n40A-n71A | n40 | n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n75A | - | n40 | n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n77A | n408,9n778,9CA_n40A-n77A8,9 | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 704, 80, 904, 100 |  |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n77(2A) | n408,9n778,9CA_n40A-n77A8,9 | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n40A-n77C | CA_n40A-n77A | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n77 | CA_n77C_BCS1 |  |
| CA_n40B-n77A | n778CA_n40A-n77A | n40 | CA_n40B_BCS1 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 704, 80, 904, 100 |  |
| CA_n40B-n77(2A) | CA_n40A-n77A | n40 | CA_n40B_BCS1 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n40B-n77C | CA_n40A-n77A | n40 | CA_n40B_BCS1 | 0 |
|  |  | n77 | CA_n77C_BCS1 |  |
|  |  | n40 | CA_n40B_BCS4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n40A-n78A | n408,9n788,9CA_n40A-n78A8 | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n78(2A) | CA_n40A-n78A | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 | 0 |
|  |  | n78 | CA_n78(2A)_BCS1 |  |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n40A-n78C | CA_n40A-n78A | n40 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n40B-n78A | - | n40 | CA_n40B_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  | CA_n40A-n78A | n40 | CA_n40B_BCS1 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n40B-n78(2A) | CA_n40A-n78A | n40 | CA_n40B_BCS1 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n40 | CA_n40B_BCS 4 and 5 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n40B-n78C | CA_n40A-n78A | n40 | CA_n40B_BCS1 | 0 |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n40A-n79A | n408,9n798,9CA_n40A-n79A8 | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n79C | n408,9n798,9CA_n79C8CA_n40A-n79A8 | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  | CA_n79CCA_n40A-n79ACA_n40A-n79C | n40 | See n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n40A-n105A | CA_n40A-n105A | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |

Table 5.5A.3.1-1j: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n41A-n48A | CA_n41A-n48A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | See n48 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n48B | CA_n41A-n48A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n48 | CA_n48B_BCS2 |  |
| CA_n41A-n48C | CA_n41A-n48A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n48 | CA_n48C_BCS1 |  |
| CA_n41A-n48(2A) | CA_n41A-n48A | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
| CA_n41C-n48A | CA_n41A-n48A | n41 | CA_n41C_BCS2 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 |  |
| CA_n41C-n48B | CA_n41A-n48A | n41 | CA_n41C_BCS2 | 0 |
|  |  | n48 | CA_n48B_BCS2 |  |
| CA_n41C-n48C | CA_n41A-n48A | n41 | CA_n41C_BCS2 | 0 |
|  |  | n48 | CA_n48C_BCS1 |  |
| CA_n41(2A)-n48A | CA_n41A-n48A | n41 | CA_n41(2A)_BCS3 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 |  |
|  |  | n41 | CA_n41(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | See n48 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n48B | CA_n41A-n48A | n41 | CA_n41(2A)_BCS3 | 0 |
|  |  | n48 | CA_n48B_BCS2 |  |
| CA_n41(2A)-n48C | CA_n41A-n48A | n41 | CA_n41(2A)_BCS3 | 0 |
|  |  | n48 | CA_n48C_BCS1 |  |
| CA_n41(2A)-n48(2A) | CA_n41A-n48A | n41 | CA_n41(2A)_BCS1 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n41 | CA_n41(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
| CA_n41A-n50A | CA_n41A-n50A | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n50 | 5, 10, 15, 20, 40, 50, 60, 801 |  |
| CA_n41A-n66A | n418,9n668CA_n41A-n66A8,9,13,14 | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n66A | n418,9 n668CA_n41A-n66A8,9,13,14 | n41 | CA_n41(2A)_BCS1 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n41 | CA_n41(2A)_BCS1 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66(2A) | n418, 9n668CA_n41A-n66A8,9,13,14 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 1 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n41C-n66A | n418, 9n668CA_n41A-n66A8,9,13,14CA_n41C8,9CA_n41C-n66A8,9 | n41 | CA_n41C_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n41 | CA_n41C_BCS1 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  | n418, 9CA_n41A-n66A8,9,13,14CA_n41C8,9CA_n41C-n66A8,9,13,14 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n66(2A) | n418, 9n668CA_n41A-n66A8,9CA_n41C8,9CA_n41C-n66A8,9 | n41 | CA_n41C_BCS2 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n41(2A)-n66(2A) | n418,9n668CA_n41A-n66A8,9 | n41 | CA_n41(2A)_BCS3 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n41(3A)-n66A | n418, 9n668CA_n41A-n66A8 | n41 | CA_n41(3A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40, |  |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(3A)-n66(2A) | n418,9n668CA_n41A-n66A8 | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n41(A-C)-n66A | n418,9n668CA_n41C8,9CA_n41A-n66A8CA_n41C-n66A8 | n41 | CA_n41(A-C)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(A-C)-n66(2A) | n418,9n668CA_n41C8CA_n41A-n66A8CA_n41C-n66A | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n41A-n70A | CA_n41A-n70A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n41A-n71A | n418,9n718CA_n41A-n71A8,9,13,14 | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 1 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n71B | n418,9n718CA_n41A-n71A8,9,13,14 | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n71 | CA_n71B_BCS0 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 1 |
|  |  | n71 | CA_n71B_BCS2 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n41A-n71(2A) | n418,9n718CA_n41A-n71A8,9,13,14 | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 1 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n41C-n71A | n418,9n718CA_n41A-n71A8,9,13,14CA_n41C8,9CA_n41C-n71A8,9 | n41 | CA_n41C_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | CA_n41C_BCS1 | 1 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | n418,9n718CA_n41A-n71A8,9,13,14CA_n41C8,9CA_n41C-n71A8,9,13,14 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n71(2A) | n418,9n718CA_n41A-n71A8,9CA_n41C-n71A8,9CA_n41C8,9 | n41 | CA_n41C_BCS1 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n41(2A)-n71A | n418,9n718CA_n41A-n71A8,9,13,14 | n41 | CA_n41(2A)_BCS1 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | CA_n41(2A)_BCS3 | 1 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n71(2A) | n418,9n718CA_n41A-n71A8,9 | n41 | CA_n41(2A)_BCS1 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n41(2A)-n71B | n418,9n718CA_n41A-n71A8,9 | n41 | CA_n41(2A)_BCS1 | 0 |
|  |  | n71 | CA_n71B_BCS0 |  |
|  |  | n41 | CA_n41(2A)_BCS1 | 1 |
|  |  | n71 | CA_n71B_BCS2 |  |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n41(3A)-n71A | n418,9n718CA_n41A-n71A8 | n41 | CA_n41(3A)_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(3A)-n71B | n418,9n718CA_n41A-n71A8 | n41 | CA_n41(3A)_BCS4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS4 and 5 |  |
| CA_n41(3A)-n71(2A) | n418,9n718CA_n41A-n71A8 | n41 | CA_n41(3A)_BCS4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS4 and 5 |  |
| CA_n41(A-C)-n71A | n418,9n718CA_n41A-n71A8CA_n41C8,9CA_n41C-n71A8 | n41 | CA_n41(A-C)_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(A-C)-n71B | n418,9n718CA_n41A-n71A8CA_n41C8CA_n41C-n71A | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n41(A-C)-n71(2A) | n418,9n718CA_n41A-n71A8CA_n41C8CA_n41C-n71A | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n41C-n71B | n418,9n718CA_n41A-n71A8,9CA_n41C-n71A8,9CA_n41C8,9 | n41 | CA_n41C_BCS0 | 0 |
|  |  | n71 | CA_n71B_BCS0 |  |
|  |  | n41 | CA_n41C_BCS1 | 1 |
|  |  | n71 | CA_n71B_BCS2 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n41A-n74A | n418CA_n41A-n74A8 | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n74 | 5, 10, 15, 20 |  |
| CA_n41A-n75A | - | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n75 | 5,10, 15, 20, 25,30,40,50 |  |
| CA_n41A-n77A | n418,9n778,9CA_n41A-n77A8,9,13,14 | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 1 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41B-n77A | CA_n41A-n77A | n41 | CA_n41B_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n41B-n77(2A) | CA_n41A-n77A | n41 | CA_n41B_BCS0 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n41(2A)-n77A | n418,9n778,9CA_n41A-n77A8,9,13,14 | n41 | CA_n41(2A)_BCS1 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(3A)-n77A | n418,9n778,9CA_n41A-n77A8,9 | n41 | CA_n41(3A)_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(A-C)-n77A | n418,9n778,9CA_n41C8,9CA_n41A-n77A8,9CA_n41C-n77A8,9 | n41 | CA_n41(A-C)_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n77A | n418,9n778,9CA_n41A-n77A8,9,13,14CA_n41C8,9 | n41 | CA_n41C_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n418,9n778,9CA_n41A-n77A8,9,13,14CA_n41C8,9CA_n41C-n77A8,9,13,14 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n77(2A) | n418,9n778,9CA_n77(2A)8CA_n41A-n77A8,13 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  | n418,9n778,9CA_n41A-n77A8,13 | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41C-n77(2A) | n418,9n778,9CA_n41A-n77A8CA_n41C8CA_n41C-n77A | n41 | CA_n41C_BCS0 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41A-n77(3A) | n418,9n778,9CA_n41A-n77A8CA_n77(2A)8 | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS 4 and 5 |  |
| CA_n41(2A)-n77(2A) | - | n41 | CA_n41(2A)_BCS1 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  | n418,9n778,9CA_n41A-n77A8 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41A-n77C | CA_n41A-n77A | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n41A-n78A | CA_n41A-n78A | n41 | 10, 15, 20, 40, 50, 60, 80, 100 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n78(2A) | CA_n78(2A)CA_n41A-n78A | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n41A-n78C | CA_n41A-n78ACA_n41A-n78CCA_n78C | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n78 | CA_n78C_BCS0 |  |
|  |  | n41 | 5,10,15,20,25,30,35,40,45,50,60,70,80,90,100 | 1 |
|  |  | n78 | CA_n78C_BCS1 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n41A-n79A | n418,9n798,9CA_n41A-n79A8,13,14 | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n41 | 10, 15, 20, 40, 50, 60 | 1 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 2 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n79C | n418,9n798,9CA_n41A-n79A8,13,14CA_n79C8 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  | n418,9n798,9CA_n79C8CA_n41A-n79A8,13,14CA_n41A-n79C | n41 | See n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n41C-n79A | n418,9n798,9CA_n41A-n79A8,13,14CA_n41C8 | n41 | CA_n41C_BCS0 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n41 | CA_n41C_BCS4 and 5 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n79A | CA_n41(2A)CA_n41A-n79A | n41 | CA_n41(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n79C | n418,9n798,9CA_n41C8CA_n79C8CA_n41A-n79A8 | n41 | CA_n41C_BCS0 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  |  | n41 | CA_n41C_BCS4 and 5 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n41A-n85A | n418,9CA_n41A-n85A8,13,14 | n41 | See n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n85A | CA_n41A-n85ACA_n41C | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n85A | CA_n41A-n85A | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(3A)-n85A | CA_n41A-n85A | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(A-C)-n85A | CA_n41A-n85ACA_n41C | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n104A | CA_n41A-n104A | n41 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n104 | 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n104 | n104 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n104A | CA_n41CCA_n41A-n104ACA_n41C-n104A | n41 | CA_n41C_BCS0 | 0 |
|  |  | n104 | 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | CA_n41C_BCS0 | 4 and 5 |
|  |  | n104 | n104 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n104C | CA_n104CCA_n41A-n104ACA_n41A-n104C | n41 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n104 | CA_n104C_BCS0 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n104 | CA_n104C_BCS 4 and 5 |  |

##### Table 5.5A.3.1-1k ~ Table 5.5A.3.1-1o

Table 5.5A.3.1-1k: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n46A-n48A | CA_n46A-n48A | n46 | 20, 40, 60, 80 | 0 |
|  |  | n48 | 20 |  |
|  |  | n46 | 20, 40, 60, 80 | 1 |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 |  |
| CA_n46A-n48(2A) | CA_n46A-n48A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
| CA_n46A-n48(3A) | CA_n46A-n48A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
| CA_n46A-n48(4A) | CA_n46A-n48A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
| CA_n46A-n48B | CA_n46A-n48A | n46 | 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
| CA_n46A-n48C | CA_n46A-n48ACA_n46A-n48B | n46 | 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
| CA_n46B-n48A | CA_n46A-n48A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | 20 |  |
|  |  | n46 | CA_n46B_BCS0 | 1 |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 |  |
| CA_n46B-n48(2A) | CA_n46A-n48A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
| CA_n46B-n48(3A) | CA_n46A-n48A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
| CA_n46B-n48(4A) | CA_n46A-n48A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
| CA_n46B-n48B | CA_n46A-n48ACA_n46A-n48B | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
| CA_n46B-n48C | CA_n46A-n48A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
| CA_n46C-n48A | CA_n46A-n48A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | 20 |  |
|  |  | n46 | CA_n46C_BCS0 | 1 |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 |  |
| CA_n46C-n48(2A) | CA_n46A-n48A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
| CA_n46C-n48(3A) | CA_n46A-n48A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
| CA_n46C-n48(4A) | CA_n46A-n48A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
| CA_n46C-n48B | CA_n46A-n48ACA_n46A-n48B | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
| CA_n46C-n48C | CA_n46A-n48A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
| CA_n46D-n48A | CA_n46A-n48A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | 20 |  |
|  |  | n46 | CA_n46D_BCS0 | 1 |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 |  |
| CA_n46D-n48(2A) | CA_n46A-n48A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
| CA_n46D-n48(3A) | CA_n46A-n48A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
| CA_n46D-n48(4A) | CA_n46A-n48A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
| CA_n46D-n48B | CA_n46A-n48ACA_n46A-n48B | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
| CA_n46D-n48C | CA_n46A-n48A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
| CA_n46M-n48A | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | 20 |  |
| CA_n46M-n48(2A) | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
| CA_n46M-n48(3A) | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
| CA_n46M-n48(4A) | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
| CA_n46M-n48B | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
| CA_n46M-n48C | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
| CA_n46N-n48A | CA_n46A-n48A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 |  |
| CA_n46N-n48(2A) | CA_n46A-n48A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
| CA_n46N-n48(3A) | CA_n46A-n48A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
| CA_n46N-n48(4A) | CA_n46A-n48A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
| CA_n46N-n48B | CA_n46A-n48ACA_n46A-n48B | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
| CA_n46N-n48C | CA_n46A-n48A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
| CA_n46A-n66A | - | n46 | 20, 40, 60, 80 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n46A-n77A | CA_n46A-n77A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n46C-n77A | CA_n46A-n77A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n46D-n77A | CA_n46A-n77A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n46A-n77(2A) | CA_n77(2A)CA_n46A-n77A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n46C-n77(2A) | CA_n77(2A)CA_n46A-n77A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n46D-n77(2A) | CA_n77(2A)CA_n46A-n77A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n46(2A)-n77A | CA_n46A-n77A | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n46(2A)-n77(2A) | CA_n77(2A)CA_n46A-n77A | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n46A-n78A | CA_n46A-n78A | n46 | 20, 40, 60, 80 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n46C-n78A | CA_n46A-n78A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n46D-n78A | CA_n46A-n78A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n46A-n78(2A) | CA_n78(2A)CA_n46A-n78A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n46C-n78(2A) | CA_n78(2A)CA_n46A-n78A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n46D-n78(2A) | CA_n78(2A)CA_n46A-n78A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n46(2A)-n78A | CA_n46A-n78A | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n46(2A)-n78(2A) | CA_n78(2A)CA_n46A-n78A | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n46A-n96A | - | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46B-n96A | - | n46 | CA_n46B_BCS0 | 0 |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46C-n96A | - | n46 | CA_n46C_BCS0 | 0 |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46D-n96A | - | n46 | CA_n46D_BCS0 | 0 |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46M-n96A | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46N-n96A | - | n46 | CA_n46N_BCS1 | 0 |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46A-n96B | - | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46B-n96B | - | n46 | CA_n46B_BCS0 | 0 |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46C-n96B | - | n46 | CA_n46C_BCS0 | 0 |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46D-n96B | - | n46 | CA_n46D_BCS0 | 0 |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46M-n96B | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46N-n96B | - | n46 | CA_n46N_BCS1 | 0 |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46A-n96C | - | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46B-n96C | - | n46 | CA_n46B_BCS0 | 0 |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46C-n96C | - | n46 | CA_n46C_BCS0 | 0 |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46D-n96C | - | n46 | CA_n46D_BCS0 | 0 |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46M-n96C | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46N-n96C | - | n46 | CA_n46N_BCS1 | 0 |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46A-n96D | - | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46B-n96D | - | n46 | CA_n46B_BCS0 | 0 |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46C-n96D | - | n46 | CA_n46C_BCS0 | 0 |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46D-n96D | - | n46 | CA_n46D_BCS0 | 0 |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46M-n96D | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46N-n96D | - | n46 | CA_n46N_BCS1 | 0 |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46A-n96E | - | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46B-n96E | - | n46 | CA_n46B_BCS0 | 0 |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46C-n96E | - | n46 | CA_n46C_BCS0 | 0 |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46D-n96E | - | n46 | CA_n46D_BCS0 | 0 |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46M-n96E | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46N-n96E | - | n46 | CA_n46N_BCS1 | 0 |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46A-n102A | - | n46 | 10, 20, 40, 60, 80, 100 | 0 |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n46A-n102(2A) | - | n46 | 10, 20, 40, 60, 80, 100 | 0 |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n46A-n102B | CA_n102B | n46 | 10, 20, 40, 60, 80, 100 | 0 |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n46A-n102C | CA_n102C | n46 | 10, 20, 40, 60, 80, 100 | 0 |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n46A-n102D | - | n46 | 10, 20, 40, 60, 80, 100 | 0 |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n46A-n102E | - | n46 | 10, 20, 40, 60, 80, 100 | 0 |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n46(2A)-n102A | - | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n46(2A)-n102(2A) | - | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n46(2A)-n102B | CA_n102B | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n46(2A)-n102C | CA_n102C | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n46(2A)-n102D | - | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n46(2A)-n102E | - | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n46C-n102A | - | n46 | CA_n46C_BCS0 | 0 |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n46C-n102(2A) | - | n46 | CA_n46C_BCS0 | 0 |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n46C-n102B | CA_n102B | n46 | CA_n46C_BCS0 | 0 |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n46C-n102C | CA_n102C | n46 | CA_n46C_BCS0 | 0 |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n46C-n102D | - | n46 | CA_n46C_BCS0 | 0 |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n46C-n102E | - | n46 | CA_n46C_BCS0 | 0 |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n46D-n102A | - | n46 | CA_n46D_BCS0 | 0 |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n46D-n102(2A) | - | n46 | CA_n46D_BCS0 | 0 |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n46D-n102B | CA_n102B | n46 | CA_n46D_BCS0 | 0 |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n46D-n102C | CA_n102C | n46 | CA_n46D_BCS0 | 0 |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n46D-n102D | - | n46 | CA_n46D_BCS0 | 0 |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n46D-n102E | - | n46 | CA_n46D_BCS0 | 0 |
|  |  | n102 | CA_n102E_BCS0 |  |

Table 5.5A.3.1-1l: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n48A-n53A | - | n48 | 5, 10, 15, 20, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n53 | 5, 10 |  |
| CA_n48(2A)-n53A | - | n48 | CA_n48(2A)_BCS0 | 0 |
|  |  | n53 | 5, 10 |  |
| CA_n48A-n66A | CA_n48A-n66A | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 806, 906, 1006 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 2 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40, |  |
|  | n668 | n48 | See n48 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n48A-n66A | n66 | See n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48A-n66B | CA_n48A-n66A | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 0 |
|  |  | n66 | CA_n66B_BCS0 |  |
| CA_n48A-n66(2A) | CA_n48A-n66A | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n48 | See n48 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n48A-n66(3A) | CA_n48A-n66A | n48 | See n48 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(3A)_BCS 4 and 5 |  |
| CA_n48B-n66A | CA_n48BCA_n48A-n66A | n48 | CA_n48B_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n48 | CA_n48B_BCS1 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n48 | CA_n48B_BCS2 | 2 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  | CA_n48BCA_n48A-n66ACA_n48B-n66A | n48 | CA_n48B_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | See n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48B-n66B | CA_n48A-n66A | n48 | CA_n48B_BCS0 | 0 |
|  |  | n66 | CA_n66B_BCS0 |  |
|  |  | n48 | CA_n48B_BCS2 | 1 |
|  |  | n66 | CA_n66B_BCS0 |  |
| CA_n48B-n66(2A) | CA_n48BCA_n48A-n66A | n48 | CA_n48B_BCS2 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n48 | CA_n48B_BCS2 | 1 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n48 | CA_n48B_BCS2 | 2 |
|  |  | n66 | CA_n66(2A)_BCS2 |  |
|  | CA_n48BCA_n48A-n66ACA_n48B-n66A | n48 | CA_n48B_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n48C-n66A | CA_n48BCA_n48A-n66A | n48 | CA_n48C_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n48 | CA_n48C_BCS0 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n48C-n66B | CA_n48A-n66A | n48 | CA_n48C_BCS1 | 0 |
|  |  | n66 | CA_n66B_BCS0 |  |
| CA_n48(2A)-n66A | CA_n48A-n66A | n48 | CA_n48(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n48 | CA_n48(2A)_BCS0 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n48 | CA_n48(2A)_BCS1 | 2 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | See n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48(2A)-n66B | CA_n48A-n66A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n66 | CA_n66B_BCS0 |  |
| CA_n48(2A)-n66(2A) | CA_n48A-n66A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n48(3A)-n66A | CA_n48A-n66A | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
| CA_n48(A-B)-n66A | CA_n48A-n66A | n48 | CA_n48(A-B)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n48 | CA_n48(A-B)_BCS1 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n48 | CA_n48(A-B)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | See n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48A-n70A | CA_n48A-n70A | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n48(2A)-n70A | CA_n48A-n70A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
| CA_n48(3A)-n70A | CA_n48A-n70A | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
| CA_n48B-n70A | CA_n48A-n70A | n48 | CA_n48B_BCS2 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n48A-n71A | CA_n48A-n71A | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48A-n71(2A) | CA_n48A-n71A | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
| CA_n48(2A)-n71A | CA_n48A-n71A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48(2A)-n71(2A) | CA_n48A-n71A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
| CA_n48(3A)-n71A | CA_n48A-n71A | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48(4A)-n71A | CA_n48A-n71A | n48 | CA_n48(4A)_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48B-n71A | CA_n48A-n71A | n48 | CA_n48B_BCS2 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48B-n71(2A) | CA_n48A-n71A | n48 | CA_n48B_BCS2 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
| CA_n48C-n71A | CA_n48A-n71A | n48 | CA_n48C_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48A-n77A | n778,9 | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n48 | See n48 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48A-n77C | n778,9CA_n77C8,9 | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 0 |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 1 |
|  |  | n77 | CA_n77C_BCS1 |  |
|  |  | n48 | See n48 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n48A-n77(2A) | - | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n48 | See n48 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n48(2A)-n77A | n778,9 | n48 | CA_n48(2A)_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n48 | CA_n48(2A)_BCS1 | 1 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48(2A)-n77C | n778,9CA_n77C8,9 | n48 | CA_n48(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n48 | CA_n48(2A)_BCS0 | 1 |
|  |  | n77 | CA_n77C_BCS1 |  |
|  |  | n48 | CA_n48(2A)_BCS1 | 2 |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n48 | CA_n48(2A)_BCS1 | 3 |
|  |  | n77 | CA_n77C_BCS1 |  |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n48(2A)-n77(2A) | - | n48 | CA_n48(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n48(3A)-n77A | - | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48B-n77A | CA_n48Bn778,9 | n48 | CA_n48B_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n48 | CA_n48B_BCS1 | 1 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n48 | CA_n48B_BCS2 | 2 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n778,9CA_n48B | n48 | CA_n48B_BCS4 and 5 | 4 and 5 |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48B-n77C | n778,9CA_n48BCA_n77C8,9 | n48 | CA_n48B_BCS0 | 0 |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n48 | CA_n48B_BCS0 | 1 |
|  |  | n77 | CA_n77C_BCS1 |  |
|  |  | n48 | CA_n48B_BCS2 | 2 |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n48 | CA_n48B_BCS2 | 3 |
|  |  | n77 | CA_n77C_BCS1 |  |
|  |  | n48 | CA_n48B_BCS4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n48(A-B)-n77A | n778,9 | n48 | CA_n48(A-B)_BCS0 | 0 |
|  | CA_n48B | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n48 | CA_n48(A-B)_BCS1 | 1 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(A-B)-n77C | n778,9CA_n48BCA_n77C | n48 | CA_n48(A-B)_BCS1 | 0 |
|  |  | n77 | CA_n77C_BCS1 |  |
| CA_n48A-n96A | CA_n48A-n96A | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 0 |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n48(2A)-n96A | CA_n48A-n96A | n48 | CA_n48(2A)_BCS0 | 0 |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n48(2A)-n96B | CA_n48A-n96B | n48 | CA_n48(2A)_BCS0 | 0 |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n48(2A)-n96C | CA_n48A-n96A | n48 | CA_n48(2A)_BCS0 | 0 |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n48(2A)-n96D | CA_n48A-n96A | n48 | CA_n48(2A)_BCS0 | 0 |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n48(2A)-n96E | CA_n48A-n96A | n48 | CA_n48(2A)_BCS0 | 0 |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n48(3A)-n96A | CA_n48A-n96A | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n48(3A)-n96B | CA_n48A-n96B | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n48(3A)-n96C | CA_n48A-n96A | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n48(3A)-n96D | CA_n48A-n96A | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n48(3A)-n96E | CA_n48A-n96A | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n48(4A)-n96A | CA_n48A-n96A | n48 | CA_n48(4A)_BCS0 | 0 |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n48(4A)-n96B | CA_n48A-n96A | n48 | CA_n48(4A)_BCS0 | 0 |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n48(4A)-n96C | CA_n48A-n96A | n48 | CA_n48(4A)_BCS0 | 0 |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n48(4A)-n96D | CA_n48A-n96A | n48 | CA_n48(4A)_BCS0 | 0 |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n48(4A)-n96E | CA_n48A-n96A | n48 | CA_n48(4A)_BCS0 | 0 |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n48A-n96B | CA_n48A-n96A | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 0 |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n48A-n96C | CA_n48A-n96A | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 0 |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n48A-n96D | CA_n48A-n96A | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 0 |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n48A-n96E | CA_n48A-n96A | n48 | 5, 10, 15, 20, 30, 40, 506, 606, 706, 806, 906, 1006 | 0 |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n48B-n96A | CA_n48A-n96ACA_n48B-n96A | n48 | CA_n48B_BCS0 | 0 |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n48B-n96B | CA_n48A-n96ACA_n48B-n96A | n48 | CA_n48B_BCS0 | 0 |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n48B-n96C | CA_n48A-n96ACA_n48B-n96A | n48 | CA_n48B_BCS0 | 0 |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n48B-n96D | CA_n48A-n96ACA_n48B-n96A | n48 | CA_n48B_BCS0 | 0 |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n48B-n96E | CA_n48A-n96ACA_n48B-n96A | n48 | CA_n48B_BCS0 | 0 |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n48C-n96A | CA_n48A-n96A | n48 | CA_n48C_BCS0 | 0 |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n48C-n96B | CA_n48A-n96A | n48 | CA_n48C_BCS0 | 0 |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n48C-n96C | CA_n48A-n96A | n48 | CA_n48C_BCS0 | 0 |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n48C-n96D | CA_n48A-n96A | n48 | CA_n48C_BCS0 | 0 |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n48C-n96E | CA_n48A-n96A | n48 | CA_n48C_BCS0 | 0 |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n50A-n77A | CA_n50A-n77A | n50 | n50 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n50A-n78A | CA_n50A-n78A | n50 | 5, 10, 15, 20, 30, 40, 50, 60, 801 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |

Table 5.5A.3.1-1m: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n66A-n70A | n668n708 | n66 | 5, 10, 15, 20, 40 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  | - | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66B-n70A | n668n708 | n66 | CA_n66B_BCS0 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n66(2A)-n70A | n668n708 | n66 | CA_n66(2A)_BCS0 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  | - | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66(3A)-n70A | n668n708 | n66 | CA_n66(3A)_BCS0 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  | - | n66 | CA_n66(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66A-n71A | n668n718CA_n66A-n71A8,9 | n66 | 5, 10, 15, 20, 40 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66A-n71B | n668n718CA_n66A-n71A8 | n66 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | CA_n71B_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n71 | CA_n71B_BCS2 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n66A-n71(2A) | n668n718CA_n66A-n71A8 | n66 | 5, 10, 15, 20, 40 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n66(2A)-n71A | n668n718CA_n66A-n71A8 | n66 | CA_n66(2A)_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n66 | CA_n66(2A)_BCS1 | 1 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66(2A)-n71B | n668n718CA_n66A-n71A8 | n66 | CA_n66(2A)_BCS1 | 0 |
|  |  | n71 | CA_n71B_BCS2 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n66(2A)-n71(2A) | n668n718CA_n66A-n71A8 | n66 | CA_n66(2A)_BCS1 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n66(3A)-n71A | n668n718CA_n66A-n71A | n66 | CA_n66(3A)_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n66 | CA_n66(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66(3A)-n71(2A) | CA_n66A-n71A | n66 | CA_n66(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n66B-n71A | n668n718CA_n66A-n71A | n66 | CA_n66B_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n66A-n77A | n668n778,9CA_n66A-n77A8,9,13,14 | n66 | 5, 10, 15, 20, 40 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66A-n77B | CA_n66A-n77A | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77B_BCS 4 and 5 |  |
| CA_n66(2A)-n77A | n668n778,9CA_n66A-n77A8,9,13,14 | n66 | CA_n66(2A)_BCS1 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | CA_n66(2A)_BCS1 | 1 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66(2A)-n77B | CA_n66A-n77A | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77B_BCS 4 and 5 |  |
| CA_n66A-n77(2A) | n668n778,9CA_n66A-n77A8,13,14CA_n77(2A)8 | n66 | 5, 10, 15, 20, 40 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n66(3A)-n77A | n668n778,9CA_n66A-n77A8 | n66 | CA_n66(3A)_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n66A-n77A | n66 | CA_n66(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66(2A)-n77(2A) | n668n778,9CA_n66A-n77A8CA_n77(2A) | n66 | CA_n66(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 | 1 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n66(3A)-n77(2A) | n778,9CA_n66A-n77A8 | n66 | CA_n66(3A)_BCS0 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n66 | CA_n66(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n66A-n77C | n778,9CA_n77C8,9CA_n66A-n77A8,13,14 | n66 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n77 | CA_n77C_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n778,9CA_n77C8,9CA_n66A-n77A8,13,14CA_n66A-n77C | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n66A-n77(3A) | n778,9CA_n77(2A)8CA_n66A-n77A8 | n66 | 5, 10, 15, 20, 40 | 0 |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n66(2A)-n77(3A) | CA_n77(2A)CA_n66A-n77A | n66 | CA_n66(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
| CA_n66(2A)-n77C | n778,9CA_n77C8,9CA_n66A-n77A8,13,14 | n66 | CA_n66(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77C_BCS1 |  |
|  |  | n66 | CA_n66(2A)_BCS1 | 1 |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n778,9CA_n77C8,9CA_n66A-n77A8,13,14CA_n66A-n77C | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n66(3A)-n77C | n778,9CA_n77CCA_n66A-n77A8 | n66 | CA_n66(3A)_BCS0 | 0 |
|  |  | n77 | CA_n77C_BCS1 |  |
| CA_n66B-n77A | n668n778,9CA_n66A-n77A8 | n66 | CA_n66B_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n66B-n77C | n778,9CA_n77CCA_n66A-n77A8 | n66 | CA_n66B_BCS0 | 0 |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n66 | CA_n66B_BCS0 | 1 |
|  |  | n77 | CA_n77C_BCS1 |  |
| CA_n66A-n78A | n788,9CA_n66A-n78A8 | n66 | 5, 10, 15, 20, 40 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | See n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66A-n78(2A) | n788,9CA_n66A-n78A8 | n66 | 5, 10, 15, 20, 30, 40 | 0 |
|  | CA_n78(2A)8 | n78 | CA_n78(2A)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n66 | See n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n66(2A)-n78A | n788,9CA_n66A-n78A8 | n66 | CA_n66(2A)_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n66 | CA_n66(2A)_BCS1 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66(2A)-n78(2A) | n788,9CA_n66A-n78A8 | n66 | CA_n66(2A)_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS1 |  |
|  |  | n66 | CA_n66(2A)_BCS1 | 1 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n66A-n85A | n668CA_n66A-n85A8 | n66 | See n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66(2A)-n85A | CA_n66A-n85A | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n67A-n78A | - | n67 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n67A-n78(2A) | CA_n78(2A) | n67 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |

Table 5.5A.3.1-1n: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n70A-n71A | n708n718CA_n70A-n71A | n70 | 5, 10, 15, 201, 251 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n70A-n71(2A) | CA_n70A-n71A | n70 | 5, 10, 15, 201, 251 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n70A-n77A | n708CA_n70A-n77A13,14 | n70 | 5, 10, 15, 201, 251 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n70A-n78A | CA_n70A-n78A | n70 | 5, 10, 15, 201, 251 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n71A-n77A | n718n778,9CA_n71A-n77A8,9,13,14 | n71 | 5, 10, 15, 20 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n71A-n77(2A) | n718n778,9CA_n77(2A)8CA_n71A-n77A8,13,14 | n71 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n71A-n77(3A) | n778,9CA_n77(2A)8CA_n71A-n77A8 | n71 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n71A-n77B | CA_n71A-n77A | n71 | n71 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77B_BCS 4 and 5 |  |
| CA_n71A-n77C | CA_n71A-n77A | n71 | n71 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n71B-n77A | n718n778,9CA_n71A-n77A8,9,13,14 | n71 | CA_n71B_BCS2 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n71B-n77(2A) | n718n778,9CA_n71A-n77A8 | n71 | CA_n71B_BCS2 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n71(2A)-n77A | n718n778,9CA_n71A-n77A8,9,13,14 | n71 | CA_n71(2A)_BCS0 | 0 |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n71(2A)-n77(2A) | n718n778, 9CA_n71A-n77A8 | n71 | CA_n71(2A)_BCS0 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n71(2A)-n77B | CA_n71A-n77A | n71 | CA_n71(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77B_BCS 4 and 5 |  |
| CA_n71(2A)-n77C | CA_n71A-n77A | n71 | CA_n71(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n71A-n78A | n788,9CA_n71A-n78A8 | n71 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | See n71 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n71A-n78(2A) | n788,9CA_n71A-n78A8 | n71 | 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n71 | See n71 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n71A-n78C | CA_n71A-n78ACA_n71A-n78CCA_n78C | n71 | See n71 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n71A-n85A | n718 | n71 | See n71 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n71(2A)-n85A | - | n71 | CA_n71(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n71B-n85A | - | n71 | CA_n71B_BCS 4 and 5 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n74A-n77A | n778CA_n74A-n77A8 | n74 | 5, 10, 15, 20 | 0 |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n74 | n74 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n74A-n77(2A) | n778CA_n74A-n77A8CA_n77(2A)8 | n74 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n74 | n74 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n74A-n78A | CA_n74A-n78A | n74 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
| CA_n75A-n78A | - | n75 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n75A-n78(2A) | CA_n78(2A) | n75 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n76A-n78A | - | n76 | 5 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
| CA_n77A-n78A2 | - | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n77A-n78C2 | - | n77 | 10,15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n77A-n78(2A)2 | - | n77 | 10,15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n77A-n79A | n778,9n798,9CA_n77A-n79A8 | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  | CA_n77A-n79A | n77 | See n77 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n77(2A)-n79A | n778,9n798,9CA_n77(2A)8,12CA_n77A-n79A8 | n77 | CA_n77(2A)_BCS1 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  | CA_n77(2A)CA_n77A-n79A | n77 | CA_n77(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n77(3A)-n79A | n778,9n798,9CA_n77(2A) 8,12CA_n77A-n79A8 | n77 | CA_n77(3A)_BCS1 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n77 | CA_n77(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n77A-n85A | n778,9n858CA_n77A-n85A8 ,13,14 | n77 | See n77 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n77(2A)-n85A | CA_n77A-n85A | n77 | CA_n77(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n85 | See n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n77A-n102A | CA_n77A-n102A | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n77A-n102(2A) | CA_n77A-n102A | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n77A-n102B | CA_n77A-n102ACA_n77A-n102B | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n77A-n102C | CA_n77A-n102ACA_n77A-n102C | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n77A-n102D | CA_n77A-n102A | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n77A-n102E | CA_n77A-n102A | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n77(2A)-n102A | CA_n77(2A) CA_n77A-n102A | n77 | CA_n77(2A)_BCS4 and 5 | 0 |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n77(2A)-n102(2A) | CA_n77(2A) CA_n77A-n102A | n77 | CA_n77(2A)_BCS4 and 5 | 0 |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n77(2A)-n102B | CA_n77(2A) CA_n77A-n102ACA_n77A-n102B | n77 | CA_n77(2A)_BCS4 and 5 | 0 |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n77(2A)-n102C | CA_n77(2A) CA_n77A-n102ACA_n77A-n102C | n77 | CA_n77(2A)_BCS4 and 5 | 0 |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n77(2A)-n102D | CA_n77(2A) CA_n77A-n102A | n77 | CA_n77(2A)_BCS4 and 5 | 0 |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n77(2A)-n102E | CA_n77(2A) CA_n77A-n102A | n77 | CA_n77(2A)_BCS4 and 5 | 0 |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n78A-n79A | n788,9n798,9CA_n78A-n79A8 | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 | 1 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n78A-n79C | - | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n79 | CA_n79C_BCS0 |  |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n78(2A)-n79A | n788,9n798,9CA_n78A-n79A | n78 | CA_n78(2A)_BCS1 | 0 |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n78A-n92A | CA_n78A-n92A | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n92 | 5, 10, 15, 20 |  |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n92 | See n92 channel bandwidths in Table 5.3.5-1 |  |
| CA_n78(2A)-n92A | CA_n78A-n92A | n78 | CA_n78(2A)_BCS0 | 0 |
|  |  | n92 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n92 | See n92 channel bandwidths in Table 5.3.5-1 |  |
| CA_n78A-n94A | - | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n94 | 5, 10, 15, 20 |  |
| CA_n78A-n102A | CA_n78A-n102A | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n78A-n102(2A) | CA_n78A-n102A | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n78A-n102B | CA_n78A-n102ACA_n78A-n102B | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n78A-n102C | CA_n78A-n102ACA_n78A-n102C | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n78A-n102D | CA_n78A-n102A | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n78A-n102E | CA_n78A-n102A | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n78(2A)-n102A | CA_n78A-n102ACA_n78(2A) | n78 | CA_n78(2A)_BCS2 | 0 |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n78(2A)-n102B | CA_n78A-n102ACA_n78(2A)CA_n78A-n102B | n78 | CA_n78(2A)_BCS2 | 0 |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n78(2A)-n102C | CA_n78A-n102ACA_n78(2A)CA_n78A-n102C | n78 | CA_n78(2A)_BCS2 | 0 |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n78(2A)-n102D | CA_n78A-n102ACA_n78(2A) | n78 | CA_n78(2A)_BCS2 | 0 |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n78(2A)-n102E | CA_n78A-n102ACA_n78(2A) | n78 | CA_n78(2A)_BCS2 | 0 |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n78(2A)-n102(2A) | CA_n78A-n102ACA_n78(2A) | n78 | CA_n78(2A)_BCS2 | 0 |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n78A-n104A | CA_n78A-n104A | n78 | n78 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n104 | n104 channel bandwidths in Table 5.3.5-1 |  |
| CA_n78A-n105A | CA_n78A-n105A | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |

Table 5.5A.3.1-1o: NR CA configurations and bandwidth combinations sets defined for inter-band CA (two bands)

| NR CA configuration | Uplink CA configuration or single uplink carrier10 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n100A-n101A | CA_n100A-n101A | n100 | 3, 5 | 0 |
|  |  | n101 | 5, 10 |  |

The following notes are applied to the above tables:

NOTE 1: This UE channel bandwidth is applicable only to downlink.

NOTE 2: The minimum requirements for intra-band contiguous or non-contiguous CA apply.

NOTE 3: For each channel bandwidth of each component carrier, refer to Table 5.3.5-1 for the applicable SCSs. For a given band, not all UE channel bandwidths support the same SCSs.

NOTE 4: This UE channel bandwidth is optional in this release of the specification.

NOTE 5: For this bandwidth, the minimum requirements are restricted to operation when carrier is configured as an SCell part of DC or CA configuration.

NOTE 6: For this bandwidth, the minimum requirements are restricted to operation when carrier is configured as an downlink SCell part of CA configuration

NOTE 7: Limited to operation at 3450-3550 MHz and 3700–3980 MHz.

NOTE 8: Minimum requirements for Power Class 2 are applicable for this uplink CA configuration according to clause 6.2A.1.1 or 6.2A.1.2 or 6.2A.1.3 or single uplink carrier configuration according to clauses 6.2.1 or 6.2D.1 or 6.2G.1 in this downlink/uplink combination.

NOTE 9: Minimum requirements for Power Class 1.5 are applicable for this uplink CA configuration according to clause 6.2A.1.3 or single uplink carrier according to clauses 6.2.1 or 6.2D.1 or 6.2G.1 in this downlink/uplink combination.

NOTE 10:  Only single uplink carriers with power class other than PC3 are listed.

NOTE 11: The CA configurations are given in Table 5.5A.1-1 or Table 5.5A.2-1 in this specification

NOTE 12: Void.

NOTE 13: Minimum requirements for Power Class 2 are applicable for this uplink CA configuration according to clause 6.2H.3.1 or 6.2L.3.1.

NOTE 14 Minimum requirements for Power Class 1.5 are applicable for this uplink CA configuration according to clause 6.2H.3.1 or 6.2L.3.1.

NOTE 15: Uplink is only in n5 for CA_n5-n8.

NOTE 16: For UEs only supporting DL CA_n26-n28, uplink support in band n26 is optional, if the UE supports CA_n26-n28 UL configuration, it should also support UL in band n26 and n28.

NOTE 17: The UEs is allowed to indicate support of low NR band inter-band carrier aggregation via switching featureSetCombinationLowBandSwitching-r19 for this NR CA configuration

NOTE 18: Applicable only for UEs which indicate support of low NR band inter-band carrier aggregation via switching featureSetCombinationLowBandSwitching-r19 for this NR CA configuration

NOTE 19: When UL CA_n5A-n8A is supported, some restrictions may be needed to avoid simultaneous n5DL and n8 UL during UL CA_n5A-n8A with DL CA_n5A-n8A configuration. The UE and/or NW behaviors are not specified in the 3GPP specifications when there is a conflict between n5DL and n8UL including dynamic scheduling, semi-static signals and unspecified transitions between n5DL and n8UL.

NOTE 20: For single uplink carrier or TDD band intra-band uplink CA without NOTE 8, minimum requirements for Power Class 2 are applicable provided the said power class has been specified in Table 6.2.1-1, Table 6.2D.1-1, Table 6.2A.1.1-1, Table 6.2A.1.2-1 and Table 6.2H.1.1-1 and the corresponding PC2 MSD is specified in clause 7.3A.2.3.1 or clause 7.3A.2.3.2 or there is no MSD impact for this downlink/uplink combination.

NOTE 21: For single uplink carrier or TDD band intra-band uplink CA without NOTE 9, minimum requirements for Power Class 1.5 are applicable provided the said power class has been specified in Table 6.2.1-1 or Table 6.2D.1-1, Table 6.2A.1.1-1, Table 6.2A.1.2-1 and Table 6.2H.1.1-1 and the corresponding PC1.5 MSD is specified in clause 7.3A.2.3.1 or clause 7.3A.2.3.2 or there is no MSD impact for this downlink/uplink combination.

NOTE 22: The frequency range in band n28 is restricted for this band combination to 703- 733 MHz for the UL and 758-788 MHz for the DL.

NOTE 23: The frequency range in band n28 is restricted for this band combination to 718-748 MHz for the UL and 773-803 MHz for the DL.

#### 5.5A.3.2 Configurations for inter-band CA (three bands)

Table 5.5A.3.2-1: Void

##### Table 5.5A.3.2-1a

Table 5.5A.3.2-1a: NR CA configurations and bandwidth combinations sets defined for inter-band CA (three bands)

| NR CA configuration | Uplink CA configurationor single uplink carrier6 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n1A-n3A-n5A | CA_n1A-n3ACA_n1A-n5ACA_n3A-n5A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n5 | 5, 10, 15, 20 |  |
| CA_n1A-n3A-n7A | n37n77CA_n1A-n3A7CA_n1A-n7A7CA_n3A-n7A7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n1 | 5, 10, 15, 20 | 2 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7B | n77 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  | n77CA_n1A-n3ACA_n1A-n7ACA_n3A-n7ACA_n7B | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
| CA_n1A-n3A-n7(2A) | CA_n1A-n3ACA_n1A-n7ACA_n3A-n7A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
| CA_n1A-n3(2A)-n7A | CA_n1A-n3ACA_n1A-n7ACA_n3A-n7A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3(2A)_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
| CA_n1A-n3(2A)-n7(2A) | CA_n1A-n3ACA_n1A-n7ACA_n3A-n7A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
| CA_n1(2A)-n3A-n7A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
| CA_n1A-n3B-n7A | n77CA_n1A-n3ACA_n1A-n7ACA_n3A-n7A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  | n77CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
| CA_n1(2A)-n3B-n7A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
| CA_n1(2A)-n3(2A)-n7A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3(2A)_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
| CA_n1A-n3B-n7B | n77CA_n1A-n3ACA_n1A-n7ACA_n3A-n7ACA_n7B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  | n77CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
| CA_n1A-n3A-n8A | CA_n1A-n3ACA_n1A-n8ACA_n3A-n8A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3(2A)-n8A | CA_n1A-n3ACA_n1A-n8ACA_n3A-n8A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3(2A)_BCS 4 and 5 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n1A-n3A-n18A | CA_n1A-n3ACA_n1A-n18ACA_n3A-n18A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n18 | 5, 10, 15 |  |
| CA_n1A-n3A-n20A | n37CA_n1A-n3A7CA_n1A-n20ACA_n3A-n20A7 | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n26A | n267CA_n1A-n3ACA_n1A-n26ACA_n3A-n26A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
| CA_n1A-n3A-n26(2A) | n267CA_n26(2A)CA_n1A-n3ACA_n1A-n26ACA_n3A-n26A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n1A-n3B-n26A | n267CA_n1A-n3ACA_n1A-n26ACA_n3A-n26A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  | n267CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
| CA_n1A-n3B-n26(2A) | n267CA_n26(2A)CA_n1A-n3ACA_n1A-n26ACA_n3A-n26A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n1A-n3A-n28A | n37 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n28 | 5, 10, 15, 202 |  |
|  | n37CA_n1A-n3A7CA_n1A-n28ACA_n3A-n28A7 | n1 | 5, 10, 15, 20 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 2 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 201, 301 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3B-n28A | CA_n1A-n3ACA_n1A-n28ACA_n3A-n28A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
| CA_n1A-n3A-n38A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1A-n3B-n38A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1(2A)-n3A-n38A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1(2A)-n3B-n38A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1A-n3(2A)-n38A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3(2A)_BCS1 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1(2A)-n3(2A)-n38A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3(2A)_BCS1 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1A-n3A-n40A | CA_n1A-n3ACA_n1A-n40ACA_n3A-n40A | n1 | 5, 10, 15, 20, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 30, 35, 40, 45, 50 |  |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n41A | n417,9CA_n1A-n3ACA_n1A-n41A7CA_n3A-n41A7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3(2A)-n41A | CA_n1A-n3ACA_n1A-n41ACA_n3A-n41A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
| CA_n1A-n3A-n67A | CA_n1A-n3A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n71A | CA_n1A-n3ACA_n1A-n71ACA_n3A-n71A | n1 | 5,10,15,20,25,30,40,45,50 | 0 |
|  |  | n3 | 5,10,15,20,25,30,35,40,45,50 |  |
|  |  | n71 | 5,10,15,20 |  |
| CA_n1A-n3(2A)-n71A | CA_n1A-n3ACA_n1A-n71ACA_n3A-n71A | n1 | 5,10,15,20,25,30,40,45,50 | 0 |
|  |  | n3 | CA_n3(2A)_BCS 4 and 5 |  |
|  |  | n71 | 5,10,15,20 |  |
| CA_n1A-n3A-n75A | CA_n1A-n3A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n77A | n777,9CA_n1A-n3ACA_n1A-n77A7,9CA_n3A-n77A7,9 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20 | 2 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35,40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n77(2A) | n777,9CA_n1A-n3ACA_n1A-n77A7CA_n3A-n77A7CA_n77(2A)7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n1A-n3A-n77(3A) | n777,9CA_n1A-n3ACA_n1A-n77A7CA_n3A-n77A7CA_n77(2A)7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n1A-n3A-n78A | n37n787,9CA_n1A-n3A7CA_n1A-n78A7,13, 14CA_n3A-n78A7,13, 14 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20 | 2 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n78C | n787,9CA_n1A-n3ACA_n1A-n78A7,13,14CA_n3A-n78A7,13,14CA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
|  | CA_n1A-n3ACA_n1A-n78A7,13,14CA_n1A-n78CCA_n3A-n78A7,13,14CA_n3A-n78CCA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 4 and 5 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n1A-n3(2A)-n78A | n787,9CA_n1A-n3ACA_n1A-n78A7CA_n3A-n78A7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n1A-n3ACA_n1A-n78ACA_n3A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 4 and 5 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3(2A)-n78C | CA_n1A-n3ACA_n1A-n78ACA_n1A-n78CCA_n3A-n78ACA_n3A-n78CCA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 4 and 5 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n1A-n3A-n78(2A) | n37n787,9CA_n1A-n3A7CA_n1A-n78A7,13, 14CA_n3A-n78A7,13, 14CA_n78(2A)7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n3A-n78(A-C) | n787,9CA_n1A-n3ACA_n1A-n78A7CA_n3A-n78A7CA_n78C7 | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n1A-n3B-n78A | CA_n1A-n3ACA_n1A-n78A7,13,14CA_n3A-n78A7,13,14 | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3BCA_n1A-n78A7,13,14CA_n3A-n78A7,13,14 | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3B-n78(2A) | n787,9CA_n1A-n3ACA_n1A-n78A7,13,14CA_n3A-n78A7,13,14 | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n3BCA_n1A-n78A7,13,14CA_n3A-n78A7,13,14 | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n78(2A)CA_n1A-n78A7,13,14CA_n3A-n78A7,13,14 | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | CA_n3B_BCS4 and 5 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n3B-n78C | CA_n78CCA_n1A-n3ACA_n1A-n78A7,13,14CA_n3A-n78A7,13,14 | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3BCA_n1A-n78A7,13,14CA_n3A-n78A7,13,14 | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n3A-n79A | n797,9CA_n1A-n3ACA_n1A-n79A7CA_n3A-n79A7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  | CA_n1A-n3ACA_n1A-n79ACA_n3A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1(2A)-n3A-n79A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n3A-n79C | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1(2A)-n3A-n79C | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1A-n3B-n79A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n3B-n79C | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1(2A)-n3B-n79A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1(2A)-n3B-n79C | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1A-n3(2A)-n79A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3(2A)_BCS1 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n3(2A)-n79C | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3(2A)_BCS1 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1(2A)-n3(2A)-n79A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3(2A)_BCS1 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1(2A)-n3(2A)-n79C | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3(2A)_BCS1 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1A-n3A-n105A | CA_n1A-n3ACA_n1A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  | CA_n3A-n105A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n5A-n7A | CA_n1A-n5ACA_n1A-n7ACA_n5A-n7A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
| CA_n1A-n5A-n7B | CA_n1A-n5ACA_n1A-n7ACA_n5A-n7ACA_n7B | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
| CA_n1A-n5A-n8A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n1A-n5A-n28A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  | CA_n1A-n5ACA_n1A-n28ACA_n5A-n28A | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n5A-n40A | CA_n1A-n5ACA_n1A-n40ACA_n5A-n40A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
| CA_n1A-n5A-n78A | CA_n1A-n5ACA_n1A-n78ACA_n5A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 704, 80, 90, 100 |  |
|  |  | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n5A-n78(2A) | CA_n1A-n5ACA_n1A-n78ACA_n5A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n1A-n5A-n78(A-C) | CA_n78CCA_n1A-n5ACA_n1A-n78ACA_n5A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n1A-n5A-n78C | CA_n78CCA_n1A-n5ACA_n1A-n78ACA_n5A-n78A | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n1A-n5A-n79A | CA_n1A-n5ACA_n1A-n79ACA_n5A-n79A | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n5A-n105A | CA_n1A-n5ACA_n1A-n105ACA_n5A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n7A-n8A | CA_n1A-n7ACA_n1A-n8ACA_n7A-n8A | n1 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n1A-n7(2A)-n8A | CA_n1A-n7ACA_n1A-n8ACA_n7A-n8A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n1A-n7A-n20A | n77CA_n1A-n7A7CA_n1A-n20ACA_n7A-n20A7 | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n26A | n77n267CA_n1A-n26ACA_n1A-n7ACA_n7A-n26A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
| CA_n1A-n7A-n26(2A) | n77n267CA_n26(2A)CA_n1A-n26ACA_n1A-n7ACA_n7A-n26A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n1A-n7B-n26A | n77n267CA_n1A-n26ACA_n1A-n7ACA_n7A-n26ACA_n7B | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
| CA_n1A-n7B-n26(2A) | n77n267CA_n1A-n26ACA_n1A-n7ACA_n7A-n26ACA_n7BCA_n26(2A) | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n1A-n7A-n28A | n77CA_n1A-n7A7CA_n1A-n28ACA_n7A-n28A7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | See n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7B-n28A | n77CA_n1A-n28ACA_n1A-n7ACA_n7A-n28ACA_n7B | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
| CA_n1A-n7A-n38A10 | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1(2A)-n7A-n38A10 | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1A-n7A-n40A | CA_n1A-n7ACA_n1A-n40ACA_n7A-n40A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n67A | CA_n1A-n7A | n1 | 5, 10, 15, 20, 30, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n75A | CA_n1A-n7A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n77A | CA_n1A-n7ACA_n1A-n77ACA_n7A-n77A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n77(2A) | CA_n77(2A)CA_n1A-n7ACA_n1A-n77ACA_n7A-n77A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n1A-n7A-n78A | n77n787,9CA_n1A-n7A7CA_n1A-n78A7,13, 14CA_n7A-n78A7,13, 14 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 901, 100 |  |
|  |  | n1 | 5, 10, 15, 20 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 901, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n78(A-C) | CA_n78CCA_n1A-n7ACA_n1A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n1A-n7B-n78A | n77n787,9CA_n1A-n78A7,13,14CA_n1A-n7ACA_n7A-n78A7,13,14CA_n7B | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 704, 80, 90, 100 |  |
| CA_n1A-n7B-n78(2A) | n77n787,9CA_n1A-n78A7,13,14CA_n1A-n7ACA_n7A-n78A7,13,14CA_n7BCA_n78(2A)7 | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | n77CA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n1A-n78A7,13,14CA_n7A-n78A7,13,14 | n7 | CA_n7B_BCS4 and 5 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n7A-n78(2A) | n77n787,9CA_n1A-n7A7CA_n1A-n78A7,13, 14CA_n7A-n78A7,13, 14 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | n77n787,9CA_n78(2A)7CA_n1A-n7A7CA_n1A-n78A7,13,14CA_n7A-n78A7,13,14 | n1 | 5, 10, 15, 20 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n7A-n78C | n77n787,9CA_n78C7CA_n1A-n7ACA_n1A-n78A7,13,14CA_n7A-n78A7,13,14 | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n7B-n78C | n77n787,9CA_n7BCA_n1A-n7ACA_n1A-n78A7,13,14CA_n7A-n78A7,13,14CA_n78C7 | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n7(2A)-n78A | CA_n1A-n7ACA_n1A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n7A-n79A | CA_n1A-n7ACA_n1A-n79ACA_n7A-n79A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n7A-n79C | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1(2A)-n7A-n79A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1(2A)-n7A-n79C | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1A-n7A-n105A | CA_n1A-n7ACA_n1A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  | CA_n7A-n105A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n8A-n28A | CA_n1A-n8ACA_n1A-n28ACA_n8A-n28A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n28 | 10, 15, 20 |  |
| CA_n1A-n8A-n40A | CA_n1A-n8ACA_n1A-n40ACA_n8A-n40A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n8A-n41A | CA_n1A-n8ACA_n1A-n41ACA_n8A-n41A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n8A-n77A | - | n1 | 5, 10, 15, 20 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
| CA_n1A-n8A-n77(2A) | - | n1 | 5, 10, 15, 20 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n1A-n8A-n78A | CA_n1A-n8ACA_n1A-n78ACA_n8A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  | - | n1 | 5, 10, 15, 20 | 1 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  | CA_n1A-n8ACA_n1A-n78ACA_n8A-n78A | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | See n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n8A-n78C | CA_n78CCA_n1A-n8ACA_n1A-n78ACA_n1A-n78CCA_n8A-n78ACA_n8A-n78C | n1 | See n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | See n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n1A-n8A-n78(2A) | - | n1 | 5, 10, 15, 20 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS1 |  |
|  | CA_n1A-n8ACA_n1A-n78ACA_n8A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n8A-n79A | CA_n1A-n8ACA_n1A-n79ACA_n8A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n18A-n28A | CA_n1A-n18ACA_n1A-n28ACA_n18A-n28A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n28 | 5, 10 |  |
| CA_n1A-n18A-n41A | n417,9CA_n1A-n18ACA_n1A-n41A7CA_n18A-n41A7 | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
| CA_n1A-n18A-n77A | n777,9CA_n1A-n18ACA_n1A-n77A7,9CA_n18A-n77A7,9 | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
| CA_n1A-n18A-n77(2A) | n777,9CA_n1A-n18ACA_n1A-n77A7,9CA_n18A-n77A7,9CA_n77(2A) | n1 | 5, 10, 15, 20 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n1A-n18A-n77(3A) | n777,9CA_n1A-n18ACA_n1A-n77A7CA_n18A-n77A7CA_n77(2A) | n1 | 5, 10, 15, 20 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
| CA_n1A-n20A-n28A17 | CA_n1A-n20ACA_n1A-n28ACA_n20A-n28A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n20A-n41A | CA_n1A-n20ACA_n1A-n41ACA_n20A-n41A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n20A-n67A | CA_n1A-n20A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n20A-n71A | CA_n1A-n20ACA_n1A-n71ACA_n20A-n71A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n1A-n20A-n75A | CA_n1A-n20A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n20A-n77A | CA_n1A-n20ACA_n1A-n77ACA_n20A-n77A | n1 | 5,10,15,20,25,30,40,45,50 | 4 and 5 |
|  |  | n20 | 5,10,15,20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n20A-n77(2A) | CA_n1A-n20ACA_n1A-n77ACA_n20A-n77A | n1 | 5,10,15,20,25,30,40,45,50 | 4 and 5 |
|  |  | n20 | 5,10,15,20 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n1A-n20A-n78A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n1A-n20ACA_n1A-n78ACA_n20A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n20A-n78(2A) | CA_n1A-n20ACA_n1A-n78ACA_n20A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n26A-n78A | n267n787,9CA_n1A-n26ACA_n1A-n78A7,13,14CA_n26A-n78A7,13,14 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n26A-n78C | n267n787,9CA_n78C7CA_n1A-n26ACA_n1A-n78A7,13,14CA_n26A-n78A7,13,14 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n26A-n78(A-C) | CA_n78CCA_n1A-n26ACA_n1A-n78ACA_n26A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n1A-n26(2A)-n78A | n267n787,9CA_n1A-n26ACA_n1A-n78A7,13,14CA_n26A-n78A7,13,14CA_n26(2A) | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n26A-n78(2A) | n267n787,9CA_n1A-n26ACA_n1A-n78A7,13,14CA_n26A-n78A7,13,14CA_n78(2A)7 | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | n267CA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n1A-n78A7,13,14CA_n26A-n78A7,13,14 | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n26(2A)-n78(2A) | n267n787,9CA_n1A-n26ACA_n1A-n78A7,13,14CA_n26A-n78A7,13,14CA_n26(2A)CA_n78(2A)7 | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n1A-n26(2A)-n78C | n267n787,9CA_n26(2A)CA_n78C7CA_n1A-n26ACA_n1A-n78A7,13,14CA_n26A-n78A7,13,14 | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n28A-n38A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1A-n28A-n40A | CA_n1A-n28ACA_n1A-n40ACA_n28A-n40A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n1 | 5, 10, 15, 20 | 1 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n28A-n40B | CA_n1A-n28ACA_n1A-n40ACA_n28A-n40A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n40 | CA_n40B_BCS0 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | CA_n40B_BCS4 and 5 |  |
| CA_n1A-n28A-n41A | n417,9CA_n1A-n28ACA_n1A-n41A7CA_n28A-n41A7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n28A-n46A | CA_n1A-n28ACA_n1A-n46ACA_n28A-n46A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n46 | 10, 20, 40, 60, 80 |  |
| CA_n1A-n28A-n46C | CA_n1A-n28ACA_n1A-n46ACA_n28A-n46A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n46 | CA_n46C_BCS0 |  |
| CA_n1A-n28A-n46D | CA_n1A-n28ACA_n1A-n46ACA_n28A-n46A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n46 | CA_n46D_BCS0 |  |
| CA_n1A-n28A-n46(2A) | CA_n1A-n28ACA_n1A-n46ACA_n28A-n46A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n46 | CA_n46(2A)_BCS0 |  |
| CA_n1A-n28A-n75A | - | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n75 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  | CA_n1A-n28A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n28A-n77A | n777,9CA_n1A-n28ACA_n1A-n77A7,9CA_n28A-n77A7,9 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20 | 1 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n28A-n77(2A) | n777,9CA_n1A-n28ACA_n1A-n77A7,9CA_n28A-n77A7,9CA_n77(2A)7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n1 | 5, 10, 15, 20 | 1 |
|  |  | n28 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n1A-n28A-n77(3A) | n777,9CA_n1A-n28ACA_n1A-n77A7,9CA_n28A-n77A7,9CA_n77(2A)7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n1A-n28A-n78A | n787,9CA_n1A-n28ACA_n1A-n78A7,13, 14CA_n28A-n78A7,13, 14 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 202 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20 | 1 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 2 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n28A-n78(2A) | n787,9CA_n1A-n28ACA_n1A-n78A7,13, 14CA_n28A-n78A7,13, 14CA_n78(2A)7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n28A-n78C | n787,9CA_n1A-n28ACA_n1A-n78A7,13,14CA_n28A-n78A7,13,14 | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  | CA_n78C7 | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n28A-n78(A-C) | CA_n78CCA_n1A-n28ACA_n1A-n78ACA_n28A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n1A-n28A-n79A | n797,9CA_n1A-n28ACA_n1A-n79A7CA_n28A-n79A7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  | CA_n1A-n28ACA_n1A-n79ACA_n28A-n79A | n1 | n1 channel bandwidths in Table 5.3.5.1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5.1 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n28A-n102A | CA_n1A-n28ACA_n1A-n102ACA_n28A-n102A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n1A-n28A-n102B | CA_n1A-n28ACA_n1A-n102ACA_n1A-n102BCA_n28A-n102ACA_n28A-n102B | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n1A-n28A-n102C | CA_n1A-n28ACA_n1A-n102ACA_n1A-n102CCA_n28A-n102ACA_n28A-n102C | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n1A-n28A-n102D | CA_n1A-n28ACA_n1A-n102ACA_n28A-n102A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n1A-n28A-n102E | CA_n1A-n28ACA_n1A-n102ACA_n28A-n102A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n1A-n28A-n102(2A) | CA_n1A-n28ACA_n1A-n102ACA_n28A-n102A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n1A-n38A-n78A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n40A-n41A | CA_n1A-n40ACA_n1A-n41ACA_n40A-n41A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n40A-n75A | - | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n40A-n77A | CA_n1A-n40ACA_n1A-n77ACA_n40A-n77A | n1 | 5, 10, 15, 20, 30, 40, 45, 50 | 0 |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n40A-n77(2A) | CA_n1A-n40ACA_n1A-n77ACA_n40A-n77A | n1 | 5, 10, 15, 20, 30, 40, 45, 50 | 0 |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n1A-n40A-n78A | CA_n1A-n40ACA_n1A-n78ACA_n40A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20 | 1 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20 | 2 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n40B-n78A | CA_n1A-n40ACA_n1A-n78ACA_n40A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n40 | CA_n40B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | CA_n40B_BCS 4 and 5 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n40A-n79A | CA_n1A-n40ACA_n1A-n79ACA_n40A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n40A-n105A | CA_n1A-n40ACA_n1A-n105ACA_n40A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n41A-n71A | CA_n1A-n41ACA_n1A-n71ACA_n41A-n71A | n1 | 5,10,15,20,25,30,40,45,50 | 0 |
|  |  | n41 | 5,10,15,20,25,30,35,40,45,50,60,70,80,90,100 |  |
|  |  | n71 | 5,10,15,20 |  |
| CA_n1A-n41A-n75A | - | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n41A-n77A | n417,9n777,9CA_n1A-n41A7CA_n1A-n77A7CA_n41A-n77A7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
| CA_n1A-n41A-n77(2A) | n417,9n777,9CA_n1A-n41A7CA_n1A-n77A7CA_n41A-n77A7CA_n77(2A) | n1 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n1A-n41A-n77(3A) | CA_n1A-n41ACA_n1A-n77ACA_n41A-n77ACA_n77(2A) | n1 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
| CA_n1A-n41A-n78A | CA_n1A-n41ACA_n1A-n78ACA_n41A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 100 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
| CA_n1A-n41A-n78C | CA_n78CCA_n1A-n41ACA_n1A-n78ACA_n1A-n78CCA_n41A-n78ACA_n41A-n78C | n1 | 5,10,15,20,25,30,40,45,50 | 0 |
|  |  | n41 | 5,10,15,20,25,30,35,40,45,50,60,70,80,90,100 |  |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n1A-n41A-n79A | CA_n1A-n41ACA_n1A-n79ACA_n41A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n46A-n78A | CA_n1A-n46ACA_n1A-n78ACA_n46A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | 10, 20, 40, 60, 80 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n46C-n78A | CA_n1A-n46ACA_n1A-n78ACA_n46A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46C_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n46D-n78A | CA_n1A-n46ACA_n1A-n78ACA_n46A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46D_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n46(2A)-n78A | CA_n1A-n46ACA_n1A-n78ACA_n46A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n46A-n78(2A) | CA_n1A-n46ACA_n1A-n78ACA_n46A-n78ACA_n78(2A) | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | 10, 20, 40, 60, 80 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n1A-n46C-n78(2A) | CA_n1A-n46ACA_n1A-n78ACA_n46A-n78ACA_n78(2A) | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46C_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n1A-n46D-n78(2A) | CA_n1A-n46ACA_n1A-n78ACA_n46A-n78ACA_n78(2A) | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46D_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n1A-n46(2A)-n78(2A) | CA_n1A-n46ACA_n1A-n78ACA_n46A-n78ACA_n78(2A) | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n1A-n67A-n78A | CA_n1A-n78A | n1 | 5, 10, 15, 20, 30, 40, 45, 50 | 0 |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n67A-n78(2A) | CA_n1A-n78ACA_n78(2A) | n1 | 5, 10, 15, 20, 30, 40, 45, 50 | 0 |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n71A-n77A | CA_n1A-n71ACA_n1A-n77ACA_n71A-n77A | n1 | 5,10,15,20,25,30,40,45,50 | 0 |
|  |  | n71 | 5,10,15,20 |  |
|  |  | n77 | 10,15,20,25,30,40,50,60,70,80,90,100 |  |
| CA_n1A-n71A-n77(2A) | CA_n1A-n71ACA_n1A-n77ACA_n71A-n77A | n1 | 5,10,15,20,25,30,40,45,50 | 0 |
|  |  | n71 | 5,10,15,20 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n1A-n71A-n78A | CA_n1A-n71ACA_n1A-n78ACA_n71A-n78A | n1 | 5,10,15,20,25,30,40,45,50 | 0 |
|  |  | n71 | 5,10,15,20 |  |
|  |  | n78 | 10,15,20,25,30,40,50,60,70,80,90,100 |  |
| CA_n1A-n71A-n78C | CA_n78CCA_n1A-n71ACA_n1A-n78ACA_n1A-n78CCA_n71A-n78ACA_n71A-n78C | n1 | 5,10,15,20,25,30,40,45,50 | 0 |
|  |  | n71 | 5,10,15,20 |  |
|  |  | n78 | CA_n78C_BCS 4 and 5 |  |
| CA_n1A-n75A-n78A | CA_n1A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n75A-n78(2A) | CA_n78(2A)CA_n1A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n77A-n79A4 | n777,9n797,9CA_n1A-n77A7CA_n1A-n79A7CA_n77A-n79A7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n77(2A)-n79A4 | n777,9n797,9CA_n1A-n77A7CA_n1A-n79A7CA_n77A-n79A7CA_n77(2A)7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n77(3A)-n79A4 | n777,9n797,9CA_n1A-n77A7CA_n1A-n79A7CA_n77A-n79ACA_n77(2A)7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n78A-n79A5 | n787,9n797,9CA_n1A-n78A7CA_n1A-n79A7CA_n78A-n79A7 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n1 | 5, 10, 15, 20 | 1 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n78(2A)-n79A | n787,9n797,9CA_n1A-n78ACA_n1A-n79ACA_n78A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS1 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n78A-n102A | CA_n1A-n78ACA_n1A-n102ACA_n78A-n102A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n1A-n78A-n102B | CA_n1A-n78ACA_n1A-n102ACA_n1A-n102BCA_n78A-n102ACA_n78A-n102B | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n1A-n78A-n102C | CA_n1A-n78ACA_n1A-n102ACA_n1A-n102CCA_n78A-n102ACA_n78A-n102C | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n1A-n78A-n102D | CA_n1A-n78ACA_n1A-n102ACA_n78A-n102A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n1A-n78A-n102E | CA_n1A-n78ACA_n1A-n102ACA_n78A-n102A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n1A-n78A-n102(2A) | CA_n1A-n78ACA_n1A-n102ACA_n78A-n102A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n1A-n78(2A)-n102A | CA_n1A-n78ACA_n1A-n102ACA_n78A-n102ACA_n78(2A) | n1 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n1A-n78(2A)-n102B | CA_n1A-n78ACA_n1A-n102ACA_n1A-n102BCA_n78A-n102ACA_n78A-n102BCA_n78(2A) | n1 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n1A-n78(2A)-n102C | CA_n1A-n78ACA_n1A-n102ACA_n1A-n102CCA_n78A-n102ACA_n78A-n102CCA_n78(2A) | n1 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n1A-n78(2A)-n102D | CA_n1A-n78ACA_n1A-n102ACA_n78A-n102ACA_n78(2A) | n1 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n1A-n78(2A)-n102E | CA_n1A-n78ACA_n1A-n102ACA_n78A-n102ACA_n78(2A) | n1 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n1A-n78(2A)-n102(2A) | CA_n1A-n78ACA_n1A-n102ACA_n78A-n102ACA_n78(2A) | n1 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n1A-n78A-n105A | CA_n1A-n78ACA_n1A-n105ACA_n78A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n2A-n5A-n30A | CA_n2A-n5ACA_n2A-n30ACA_n5A-n30A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n30A | CA_n2A-n5ACA_n2A-n30ACA_n5A-n30A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n41A | CA_n2A-n5ACA_n2A-n41ACA_n5A-n41A | n2 | 5, 10, 15, 20, 25, 30, 35, 40 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
| CA_n2A-n5A-n48A | CA_n2A-n5ACA_n2A-n48ACA_n5A-n48A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n48A | CA_n2A-n5ACA_n2A-n48ACA_n5A-n48A | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n48B | CA_n2A-n5ACA_n2A-n48ACA_n2A-n48BCA_n5A-n48ACA_n5A-n48BCA_n48B | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
| CA_n2A-n5B-n48A | CA_n2A-n5ACA_n2A-n48ACA_n5A-n48ACA_n5B | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n48B | CA_n2A-n5ACA_n2A-n48ACA_n2A-n48BCA_n5A-n48ACA_n5A-n48BCA_n48B | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | CA_n48B_BCS1 |  |
|  |  | n2 | 5, 10, 15, 20 | 2 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | CA_n48B_BCS2 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
| CA_n2A-n5B-n48B | CA_n2A-n5ACA_n2A-n48ACA_n2A-n48BCA_n5A-n48ACA_n5A-n48BCA_n5BCA_n48B | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
| CA_n2A-n5A-n48(2A) | CA_n2A-n5ACA_n2A-n48ACA_n5A-n48A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
| CA_n2(2A)-n5A-n48(2A) | CA_n2A-n5ACA_n2A-n48ACA_n5A-n48A | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
| CA_n2(2A)-n5B-n48A | CA_n2A-n5ACA_n2A-n48ACA_n5A-n48ACA_n5B | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5B-n48B | CA_n2A-n5ACA_n2A-n48ACA_n2A-n48BCA_n5A-n48ACA_n5A-n48BCA_n5BCA_n48B | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
| CA_n2A-n5B-n48(2A) | CA_n2A-n5ACA_n2A-n48ACA_n5A-n48ACA_n5B | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
| CA_n2(2A)-n5B-n48(2A) | CA_n2A-n5ACA_n2A-n48ACA_n5A-n48ACA_n5B | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
| CA_n2A-n5A-n48(A-B) | CA_n2A-n5ACA_n2A-n48ACA_n5A-n48A | n2 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n5 | 5, 10, 15, 20, 251 |  |
|  |  | n48 | CA_n48(A-B)_BCS0 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n5 | 5, 10, 15, 20, 251 |  |
|  |  | n48 | CA_n48(A-B)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48(A-B)_BCS4 and 5 |  |
| CA_n2A-n5A-n66A | CA_n2A-n5ACA_n2A-n66ACA_n5A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n66A | CA_n2A-n5ACA_n2A-n66ACA_n5A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n66(2A) | CA_n2A-n5ACA_n2A-n66ACA_n5A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n2A-n5A-n66(2A) | CA_n2A-n5ACA_n2A-n66ACA_n5A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n2A-n5A-n66(3A) | CA_n2A-n5ACA_n2A-n66ACA_n5A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
| CA_n2A-n5B-n66A | CA_n2A-n5ACA_n2A-n66ACA_n5A-n66ACA_n5B | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5B-n66(2A) | CA_n2A-n5ACA_n2A-n66ACA_n5A-n66ACA_n5B | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n2(2A)-n5B-n66A | CA_n2A-n5ACA_n2A-n66ACA_n5A-n66ACA_n5B | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5B-n66(2A) | CA_n2A-n5ACA_n2A-n66ACA_n5A-n66ACA_n5B | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n2A-n5A-n77A | n777,9CA_n2A-n5ACA_n2A-n77A7,13,14CA_n5A-n77A7,13,14 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n2A-n5ACA_n2A-n77A7,13,14CA_n5A-n77A7,13,14 | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5B-n77A | n777,9CA_n2A-n5ACA_n2A-n77A7,13,14CA_n5A-n77A7,13,14CA_n5B | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n77C | n777,9CA_n2A-n5ACA_n2A-n77A7,13,14CA_n5A-n77A7,13,14CA_n77C7,9 | n2 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n5 | 5, 10, 15, 20, 251 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n5 | 5, 10, 15, 20, 251 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n777,9CA_n2A-n5ACA_n2A-n77A7,13,14CA_n2A-n77C7,13,14CA_n5A-n77A7,13,14CA_n5A-n77C7,13,14CA_n77C7,9 | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2A-n5B-n77C | n777,9CA_n2A-n5ACA_n2A-n77A7,13,14CA_n2A-n77C7,13,14CA_n5BCA_n5A-n77A7,13,14CA_n5A-n77C7,13,14CA_n77C7,9 | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2A-n5A-n77(2A) | n777,9CA_n2A-n5ACA_n2A-n77A7CA_n5A-n77A7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n2(2A)-n5A-n77A | n777,9CA_n2A-n5ACA_n2A-n77A7,13,14CA_n5A-n77A7,13,14 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n2A-n5ACA_n2A-n77A7,13,14CA_n5A-n77A7,13,14 | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n77C | n777,9CA_n2A-n5ACA_n2A-n77A7,13,14CA_n2A-n77C7,13,14CA_n5A-n77A7,13,14CA_n5A-n77C7,13,14CA_n77C7,9 | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2(2A)-n5A-n77(2A) | n777,9CA_n2A-n5ACA_n2A-n77A7CA_n5A-n77A7 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n2(2A)-n5B-n77A | n777,9CA_n2A-n5ACA_n2A-n77A7,13,14CA_n5A-n77A7,13,14CA_n5B | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5B-n77C | n777,9CA_n2A-n5ACA_n2A-n77A7,13,14CA_n2A-n77C7,13,14CA_n5A-n77A7,13,14CA_n5A-n77C7,13,14CA_n5BCA_n77C7,9 | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2A-n7A-n12A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n12 | 5, 10, 15 |  |
| CA_n2A-n7A-n66A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
| CA_n2A-n7A-n71A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n2A-n7A-n77A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n12A-n30A | CA_n2A-n12ACA_n2A-n30ACA_n12A-n30A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n30 | 5, 10 |  |
| CA_n2(2A)-n12A-n30A | CA_n2A-n12ACA_n2A-n30ACA_n12A-n30A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n30 | 5, 10 |  |
| CA_n2A-n12A-n41A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
| CA_n2A-n12A-n66A | CA_n2A-n12ACA_n2A-n66ACA_n12A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n2(2A)-n12A-n66A | CA_n2A-n12ACA_n2A-n66A CA_n12A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n2A-n12A-n66(2A) | CA_n2A-n12ACA_n2A-n66A CA_n12A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n2(2A)-n12A-n66(2A) | CA_n2A-n12ACA_n2A-n66ACA_n12A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n2A-n12A-n66(3A) | CA_n2A-n12ACA_n2A-n66ACA_n12A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
| CA_n2A-n12A-n71A | CA_n2A-n12ACA_n2A-n71A | n2 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n2A-n12A-n77A | n777,9CA_n2A-n12ACA_n2A-n77A7CA_n12A-n77A7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2(2A)-n12A-n77A | n777,9CA_n2A-n12ACA_n2A-n77A7CA_n12A-n77A7 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n12A-n77(2A) | n777,9CA_n2A-n12ACA_n2A-n77A7CA_n12A-n77A7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2(2A)-n12A-n77(2A) | n777,9CA_n2A-n12ACA_n2A-n77A7CA_n12A-n77A7 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n14A-n30A | CA_n2A-n14ACA_n2A-n30ACA_n14A-n30A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n14A-n30A | CA_n2A-n14ACA_n2A-n30ACA_n14A-n30A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
| CA_n2A-n14A-n66A | CA_n2A-n14ACA_n2A-n66ACA_n14A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n14A-n66A | CA_n2A-n14ACA_n2A-n66ACA_n14A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n14A-n66(2A) | CA_n2A-n14ACA_n2A-n66ACA_n14A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n2A-n14A-n66(2A) | CA_n2A-n14ACA_n2A-n66ACA_n14A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n2A-n14A-n66(3A) | CA_n2A-n14ACA_n2A-n66ACA_n14A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
| CA_n2A-n14A-n77A | n777,9CA_n2A-n14ACA_n2A-n77A7CA_n14A-n77A7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n14A-n77(2A) | n777,9CA_n2A-n14ACA_n2A-n77A7CA_n14A-n77A7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n2(2A)-n14A-n77A | n777,9CA_n2A-n14ACA_n2A-n77A7CA_n14A-n77A7 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n14A-n77(2A) | n777,9CA_n2A-n14ACA_n2A-n77A7CA_n14A-n77A7 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n2A-n29A-n30A | CA_n2A-n30A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
| CA_n2(2A)-n29A-n30A | CA_n2A-n30A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
| CA_n2A-n29A-n66A | CA_n2A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n2(2A)-n29A-n66A | CA_n2A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n2A-n29A-n66(2A) | CA_n2A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n2(2A)-n29A-n66(2A) | CA_n2A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n2A-n29A-n77A | n777,9CA_n2A-n77A7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2(2A)-n29A-n77A | n777,9CA_n2A-n77A7 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n29A-n77(2A) | n777,9CA_n2A-n77A7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2(2A)-n29A-n77(2A) | n777,9CA_n2A-n77A7 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n30A-n66A | CA_n2A-n30ACA_n2A-n66ACA_n30A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n30A-n66A | CA_n2A-n30ACA_n2A-n66ACA_n30A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n30A-n66(2A) | CA_n2A-n30ACA_n2A-n66ACA_n30A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n2(2A)-n30A-n66(2A) | CA_n2A-n30ACA_n2A-n66ACA_n30A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n2A-n30A-n66(3A) | CA_n2A-n30ACA_n2A-n66ACA_n30A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(3A)_BCS4 and 5 |  |
| CA_n2A-n30A-n77A | n777,9CA_n2A-n30ACA_n2A-n77A7CA_n30A-n77A7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n30A-n77(2A) | n777,9CA_n2A-n30ACA_n2A-n77A7CA_n30A-n77A7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n2(2A)-n30A-n77A | n777,9CA_n2A-n30ACA_n2A-n77A7CA_n30A-n77A7 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n30A-n77(2A) | n777,9CA_n2A-n30ACA_n2A-n77A7CA_n30A-n77A7 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n2A-n41A-n66A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
| CA_n2A-n41A-n71A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n2A-n48A-n66A | CA_n2A-n48ACA_n2A-n66ACA_n48A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n48A-n66A | CA_n2A-n48ACA_n2A-n66ACA_n48A-n66A | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n48B-n66A | CA_n2A-n48ACA_n2A-n66ACA_n2A-n48BCA_n48A-n66ACA_n48B-n66ACA_n48B | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48(A-B)-n66A | CA_n2A-n48ACA_n2A-n66ACA_n48A-n66A | n2 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n48 | CA_n48(A-B)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n48 | CA_n48(A-B)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(A-B)_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48B-n66A | CA_n48BCA_n2A-n48ACA_n2A-n66ACA_n2A-n48BCA_n48A-n66ACA_n48B-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48B_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | 5, 10, 15, 20 | 2 |
|  |  | n48 | CA_n48B_BCS2 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48(2A)-n66A | CA_n2A-n48ACA_n2A-n66ACA_n48A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48A-n66(2A) | CA_n2A-n48ACA_n2A-n66ACA_n48A-n66A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n2A-n48B-n66(2A) | CA_n2A-n48ACA_n2A-n66ACA_n2A-n48BCA_n48A-n66ACA_n48B-n66ACA_n48B | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n2(2A)-n48(2A)-n66A | CA_n2A-n48ACA_n2A-n66ACA_n48A-n66A | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n48A-n66(2A) | CA_n2A-n48ACA_n2A-n66ACA_n48A-n66A | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n2A-n48(2A)-n66(2A) | CA_n2A-n48ACA_n2A-n66ACA_n48A-n66A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n2(2A)-n48B-n66(2A) | CA_n2A-n48ACA_n2A-n66ACA_n2A-n48BCA_n48A-n66ACA_n48B-n66ACA_n48B | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n2(2A)-n48(2A)-n66(2A) | CA_n2A-n48ACA_n2A-n66ACA_n48A-n66A | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n2A-n48A-n77A | n777,9CA_n2A-n48ACA_n2A-n77A7,13,14 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n2A-n48ACA_n2A-n77A7,13,14 | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48A-n77C | n777,9CA_n2A-n48ACA_n2A-n77A7,13,14CA_n77C7,9 | n2 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n777,9CA_n2A-n48ACA_n2A-n77A7,13,14CA_n2A-n77C7,13,14CA_n77C7,9 | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2A-n48(2A)-n77C | n777,9CA_n2A-n48ACA_n2A-n77A7,13,14 | n2 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n777,9CA_n77CCA_n2A-n48ACA_n2A-n77A7,13,14CA_n2A-n77C7,9,13,14 | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2A-n48B-n77A | n777,9CA_n48BCA_n2A-n48ACA_n2A-n77A7,13,14 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48B_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | 5, 10, 15, 20 | 2 |
|  |  | n48 | CA_n48B_BCS2 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n48BCA_n2A-n48ACA_n2A-n48BCA_n2A-n77A7,13,14 | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48B-n77C | n777,9CA_n48BCA_n2A-n48ACA_n2A-n77A7,13,14 | n2 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n48 | CA_n48B_BCS2 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n777,9CA_n48BCA_n77C7,9CA_n2A-n48ACA_n2A-n48BCA_n2A-n77A7,13,14CA_n2A-n77C7,13,14 | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2(2A)-n48B-n77A | n777,9CA_n2A-n48ACA_n2A-n48BCA_n2A-n77A7,13,14CA_n48B | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48(2A)-n77A | n777,9CA_n2A-n48ACA_n2A-n77A7,13,14 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n48A-n77A | n777,9CA_n2A-n48ACA_n2A-n77A7,13,14 | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n48(2A)-n77A | n777,9CA_n2A-n48ACA_n2A-n77A7,13,14 | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n48A-n77C | n777,9CA_n2A-n48ACA_n2A-n77A7,13,14CA_n2A-n77C7,13,14CA_n77C7,9 | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2(2A)-n48(2A)-n77C | n777,9CA_n2A-n48ACA_n2A-n77A7,13,14CA_n2A-n77C7,13,14CA_n77C7,9 | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2(2A)-n48B-n77C | n777,9CA_n2A-n48ACA_n2A-n48BCA_n2A-n77A7,13,14CA_n2A-n77C7,13,14CA_n48BCA_n77C | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2A-n66A-n71A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n2A-n66A-n77A | n777,9CA_n2A-n66ACA_n2A-n77A7,13,14CA_n66A-n77A7,13,14 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n2A-n66ACA_n2A-n77A7,13,14CA_n66A-n77A7,13,14 | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n66A-n77A | n777,9CA_n2A-n66ACA_n2A-n77A7,13,14CA_n66A-n77A7,13,14 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n2A-n66ACA_n2A-n77A7,13,14CA_n66A-n77A7,13,14 | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n66A-n77C | n777,9CA_n2A-n66ACA_n2A-n77A7,13,14CA_n2A-n77C7,13,14CA_n66A-n77A7,13,14CA_n66A-n77C7,13,14CA_n77C7,9 | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2A-n66(2A)-n77A | n777,9CA_n2A-n66ACA_n2A-n77A7,13,14CA_n66A-n77A7,13,14 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n2A-n66ACA_n2A-n77A7,13,14CA_n66A-n77A7,13,14 | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n66(2A)-n77C | n777,9CA_n2A-n66ACA_n2A-n77A7,13,14CA_n2A-n77C7,13,14CA_n66A-n77A7,13,14CA_n66A-n77C7,13,14CA_n77C7,9 | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2A-n66A-n77C | n777,9CA_n2A-n66ACA_n2A-n77A7,13,14CA_n66A-n77A7,13,14 | n2 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n777,9CA_n77C7,9CA_n2A-n66ACA_n2A-n77A7,13,14CA_n2A-n77C7,13,14CA_n66A-n77A7,13,14CA_n66A-n77C7,13,14 | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2A-n66A-n77(2A) | n777,9CA_n2A-n66ACA_n2A-n77A7CA_n66A-n77A7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n2(2A)-n66(2A)-n77A | n777,9CA_n2A-n66ACA_n66A-n77A7,13,14CA_n2A-n77A7,13,14 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n2A-n66ACA_n66A-n77A7,13,14CA_n2A-n77A7,13,14 | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n66(2A)-n77C | n777,9CA_n2A-n66ACA_n66A-n77A7,13,14CA_n66A-n77C7,13,14CA_n2A-n77A7,13,14CA_n2A-n77C7,13,14CA_n77C7,9 | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n2(2A)-n66(2A)-n77(2A) | n777,9CA_n2A-n66ACA_n2A-n77A7CA_n66A-n77A7 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2(2A)-n66A-n77(2A) | n777,9CA_n2A-n66ACA_n66A-n77A7CA_n2A-n77A7 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n2A-n66(2A)-n77(2A) | n777,9CA_n2A-n66ACA_n66A-n77A7CA_n2A-n77A7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n2A-n66(3A)-n77A | n777,9CA_n2A-n66ACA_n66A-n77A7CA_n2A-n77A7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n66(3A)-n77(2A) | n777,9CA_n2A-n66ACA_n2A-n77A7CA_n66A-n77A7 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n66A-n78A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n66A-n78(2A) | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n2A-n71A-n77A | CA_n2A-n71ACA_n2A-n77ACA_n71A-n77A | n2 | 5, 10, 15, 20, 25, 30, 35, 40 | 0 |
|  |  | n71 | 5, 10, 15, 20, 25, 30, 35 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n71A-n77(2A) | CA_n2A-n71ACA_n2A-n77ACA_n71A-n77A | n2 | 5, 10, 15, 20, 25, 30, 35, 40 | 0 |
|  |  | n71 | 5, 10, 15, 20, 25, 30, 35 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n71A-n78A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n71A-n78(2A) | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n3A-n5A-n7A | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40 |  |
|  | CA_n3A-n5ACA_n3A-n7ACA_n5A-n7A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
| CA_n3A-n5A-n7B | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  | CA_n3A-n5ACA_n3A-n7ACA_n5A-n7ACA_n7B | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
| CA_n3A-n5A-n8A | - | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n3A-n5A-n28A | - | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  | CA_n3A-n5ACA_n3A-n28ACA_n5A-n28A | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n5A-n78A | CA_n3A-n5ACA_n3A-n78ACA_n5A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n5A-n78(2A) | CA_n3A-n5ACA_n3A-n78ACA_n5A-n78A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n3A-n5A-n78C | CA_n78CCA_n3A-n5ACA_n3A-n78ACA_n5A-n78A | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n3A-n5A-n78(A-C) | CA_n78CCA_n3A-n5ACA_n3A-n78ACA_n5A-n78A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n3A-n5A-n79A | CA_n3A-n5ACA_n3A-n79ACA_n5A-n79A | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n8A | CA_n3A-n7ACA_n3A-n8ACA_n7A-n8A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n8 | 5, 10, 15, 20, 35 |  |
| CA_n3A-n7(2A)-n8A | CA_n3A-n7ACA_n3A-n8ACA_n7A-n8A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n3(2A)-n7A-n8A | CA_n3A-n7ACA_n3A-n8ACA_n7A-n8A | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n3(2A)-n7(2A)-n8A | CA_n3A-n7ACA_n3A-n8ACA_n7A-n8A | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n3A-n7A-n20A | n37n77CA_n3A-n7A7CA_n3A-n20A7CA_n7A-n20A7 | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | See n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | See n20 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n26A | n77n267CA_n3A-n26ACA_n3A-n7ACA_n7A-n26A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
| CA_n3A-n7A-n26(2A) | n77n267CA_n3A-n26ACA_n3A-n7ACA_n7A-n26ACA_n26(2A) | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n3A-n7B-n26A | n77n267CA_n3A-n26ACA_n3A-n7ACA_n7A-n26ACA_n7B | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
| CA_n3A-n7B-n26(2A) | n77n267CA_n3A-n26ACA_n3A-n7ACA_n7A-n26ACA_n7BCA_n26(2A) | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n3B-n7A-n26A | n77n267CA_n3A-n7ACA_n3A-n26ACA_n7A-n26A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  | n77n267CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
| CA_n3B-n7A-n26(2A) | n77n267CA_n3A-n7ACA_n3A-n26ACA_n7A-n26ACA_n26(2A) | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  | n77n267CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n3B-n7B-n26A | n77n267CA_n3A-n7ACA_n3A-n26ACA_n7A-n26ACA_n7B | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  | n77n267CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
| CA_n3B-n7B-n26(2A) | n77n267CA_n3A-n7ACA_n3A-n26ACA_n7A-n26ACA_n7BCA_n26(2A) | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  | n77n267CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n3A-n7A-n28A | n37n77 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  | n37n77CA_n3A-n7A7CA_n3A-n28A7CA_n7A-n28A7 | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 2 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7B-n28A | n77 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  | n77CA_n3A-n7ACA_n3A-n28ACA_n7A-n28ACA_n7B | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
| CA_n3B-n7A-n28A | n77CA_n3A-n7ACA_n3A-n28ACA_n7A-n28A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  | n77CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
| CA_n3B-n7B-n28A | n77CA_n7BCA_n3A-n7ACA_n3A-n28ACA_n7A-n28A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  | n77CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
| CA_n3A-n7A-n38A10 | - | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n3B-n7A-n38A10 | - | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n3(2A)-n7A-n38A10 | - | n3 | CA_n3(2A)_BCS1 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n3A-n7A-n40A | CA_n3A-n7ACA_n3A-n40ACA_n7A-n40A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n67A | CA_n3A-n7A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n75A | CA_n3A-n7A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n77A | CA_n3A-n7A CA_n3A-n77A CA_n7A-n77A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n77(2A) | CA_n77(2A)CA_n3A-n7A CA_n3A-n77A CA_n7A-n77A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n3A-n7A-n78A | n37n77n787,9CA_n3A-n7A7CA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 704, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n78C | n77n787,9CA_n78C7CA_n3A-n7ACA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3A-n7A-n78(A-C) | CA_n78CCA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n3A-n7B-n78A | n77n787,9 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  | CA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  | n77n787,9CA_n3A-n7ACA_n3A-n78A7,13,14CA_n7A-n78A7,13,14CA_n7B | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 704, 80, 90, 100 |  |
| CA_n3A-n7B-n78(2A) | n77n787,9CA_n3A-n7ACA_n3A-n78A7,13,14CA_n7A-n78A7,13,14CA_n7B | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  | CA_n78(2A) 7 | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | n77CA_n78(2A) | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n7 | CA_n7B_BCS4 and 5 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3A-n7B-n78C | n77n787,9CA_n3A-n7ACA_n3A-n78A7,13,14CA_n7A-n78A7,13,14CA_n7BCA_n78C7 | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3A-n7A-n78(2A) | n37n77n787,9CA_n78(2A)7CA_n3A-n7A7CA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3A-n7(2A)-n78A | CA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n7A-n78A | n77n787,9CA_n3A-n7ACA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n77CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  | CA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n7A-n78(2A) | n77n787,9CA_n78(2A)7CA_n3A-n7ACA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | n77CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  | CA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | n77CA_n78(2A) | n3 | CA_n3B_BCS4 and 5 | 4 and 5 |
|  | CA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3B-n7A-n78C | n77n787,9CA_n3A-n7ACA_n3A-n78A7,13,14CA_n7A-n78A7,13,14CA_n78C7 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
|  | n77CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  | CA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3B-n7B-n78A | n77n787,9CA_n3A-n7ACA_n3A-n78A7,13,14CA_n7A-n78A7,13,14CA_n7B | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n77CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  | CA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n7B-n78(2A) | n77n787,9CA_n3A-n7ACA_n3A-n78A7,13,14CA_n7A-n78A7,13,14CA_n7B | n3 | CA_n3B_BCS0 | 0 |
|  | CA_n78(2A) 7 | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | n77CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  | CA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | n77CA_n78(2A) | n3 | CA_n3B_BCS4 and 5 | 4 and 5 |
|  | CA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n7 | CA_n7B_BCS4 and 5 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3B-n7B-n78C | n77n787,9CA_n3A-n7ACA_n3A-n78A7,13,14CA_n7A-n78A7,13,14CA_n7BCA_n78C7 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | n77CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  | CA_n3A-n78A7,13,14CA_n7A-n78A7,13,14 | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3(2A)-n7A-n78A | CA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3(2A)-n7(2A)-n78A | CA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n7A-n79A | CA_n3A-n7ACA_n3A-n79A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n7A-n79C | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n3B-n7A-n79A | - | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3(2A)-n7A-n79A | - | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n7A-n79C | - | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n3(2A)-n7A-n79C | - | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n3A-n7A-n105A | CA_n3A-n7ACA_n3A-n105A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  | CA_n7A-n105A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n3A-n8A-n28A | CA_n3A-n8ACA_n3A-n28ACA_n8A-n28A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20, 35 |  |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
| CA_n3A-n8A-n39A | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
| CA_n3A-n8A-n40A | CA_n3A-n8ACA_n3A-n40ACA_n8A-n40A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n8A-n41A | CA_n3A-n8ACA_n3A-n41ACA_n8A-n41A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n8A-n77A | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
| CA_n3A-n8A-n77(2A) | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n3A-n8A-n78A | CA_n3A-n8ACA_n3A-n78ACA_n8A-n78A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n8A-n78(2A) | CA_n3A-n8ACA_n3A-n78ACA_n8A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n3(2A)-n8A-n78A | CA_n3A-n8ACA_n3A-n78ACA_n8A-n78A | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3(2A)-n8A-n78C | CA_n3A-n8ACA_n3A-n78ACA_n3A-n78CCA_n8A-n78ACA_n8A-n78C | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n3A-n8A-n78C | CA_n78CCA_n3A-n8ACA_n3A-n78ACA_n3A-n78CCA_n8A-n78ACA_n8A-n78C | n3 | 5,10,15,20,25,30,35,40,45,50 | 4 and 5 |
|  |  | n8 | 5,10,15,20 |  |
|  |  | n78 | CA_n78C_BCS 4 and 5 |  |
| CA_n3A-n8A-n79A | CA_n3A-n8ACA_n3A-n79ACA_n8A-n79A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n3A-n18A-n28A | CA_n3A-n18ACA_n3A-n28ACA_n18A-n28A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n28 | 5, 10 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n18A-n41A | n417,9CA_n3A-n41A7,9CA_n3A-n18ACA_n18A-n41A7,9 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  | n417,9CA_n3A-n41A7,9CA_n3A-n18ACA_n18A-n41A7,9 | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n18A-n77A | n777,9CA_n3A-n18ACA_n3A-n77A7,9CA_n18A-n77A7,9 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  | n777,9CA_n3A-n18ACA_n3A-n77A7,9CA_n18A-n77A7,9 | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n18A-n77(2A) | n777,9CA_n3A-n18ACA_n3A-n77A7,9CA_n18A-n77A7,9CA_n77(2A)7 | n3 | 5, 10, 15, 20 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  | n777,9CA_n3A-n18ACA_n3A-n77A7,9CA_n18A-n77A7,9 | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n3A-n18A-n77(3A) | n777,9CA_n3A-n18ACA_n3A-n77A7CA_n18A-n77A7CA_n77(2A) | n3 | 5, 10, 15, 20 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
| CA_n3A-n20A-n67A | n37CA_n3A-n20A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n20A-n28A17 | CA_n3A-n20ACA_n3A-n28ACA_n20A-n28A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n20A-n41A | CA_n3A-n20ACA_n3A-n41ACA_n20A-n41A | n3 | 5, 10, 15, 20, 25, 30, 45, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n20A-n71A | CA_n3A-n20ACA_n3A-n71ACA_n20A-n71A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n3A-n20A-n75A | CA_n3A-n20A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n20A-n77A | CA_n3A-n20ACA_n3A-n77ACA_n20A-n77A | n3 | 5,10,15,20,25,30,35,40,45,50 | 0 |
|  |  | n20 | 5,10,15,20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n20A-n77(2A) | CA_n3A-n20ACA_n3A-n77ACA_n20A-n77A | n3 | 5,10,15,20,25,30,35,40,45,50 | 0 |
|  |  | n20 | 5,10,15,20 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n3A-n20A-n78A | CA_n3A-n20A CA_n3A-n78A CA_n20A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n20A-n78(2A) | CA_n3A-n20A CA_n3A-n78A CA_n20A-n78ACA_n78(2A) | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | See n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3A-n26A-n78A | n267n787,9CA_n3A-n26ACA_n3A-n78A7,13,14CA_n26A-n78A7,13,14 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n26A-n78(2A) | n267n787,9CA_n3A-n26ACA_n3A-n78A7,13,14CA_n26A-n78A7,13,14CA_n78(2A)7 | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n78(2A) | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n3A-n78A7,13,14CA_n26A-n78A7,13,14 | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3A-n26A-n78C | n267n787,9CA_n3A-n26ACA_n3A-n78A7,13,14CA_n26A-n78A7,13,14CA_n78C7 | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n3A-n26A-n78(A-C) | CA_n78CCA_n3A-n26ACA_n3A-n78ACA_n26A-n78A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n3A-n26(2A)-n78A | n267n787,9CA_n3A-n26ACA_n3A-n78A7,13,14CA_n26A-n78A7,13,14CA_n26(2A) | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n26(2A)-n78(2A) | n267n787,9CA_n3A-n26ACA_n3A-n78A7,13,14CA_n26A-n78A7,13,14CA_n26(2A)CA_n78(2A)7 | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n3A-n26(2A)-n78C | n267n787,9CA_n3A-n26ACA_n3A-n78A7,13,14CA_n26A-n78A7,13,14CA_n26(2A)CA_n78C7 | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n3B-n26A-n78A | n267n787,9CA_n3A-n26ACA_n3A-n78A7,13,14CA_n26A-n78A7,13,14 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n267CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  | CA_n26A-n78A7,13,14CA_n3A-n78A7,13,14 | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n26A-n78(2A) | n267n787,9CA_n3A-n26ACA_n3A-n78A7,13,14CA_n26A-n78A7,13,14CA_n78(2A)7 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | n267CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  | CA_n3A-n78A7,13,14CA_n26A-n78A7,13,14 | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | n267CA_n78(2A) | n3 | CA_n3B_BCS4 and 5 | 4 and 5 |
|  |  | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3B-n26A-n78C | n267n787,9CA_n3A-n26ACA_n3A-n78A7,13,14CA_n26A-n78A7,13,14CA_n78C7 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | n267CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  | CA_n3A-n78A7,13,14CA_n26A-n78A7,13,14 | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3B-n26(2A)-n78A | n267n787,9CA_n3A-n26ACA_n3A-n78A7,13,14CA_n26A-n78A7,13,14CA_n26(2A) | n3 | CA_n3B_BCS0 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n267CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  | CA_n3A-n78A7,13,14CA_n26A-n78A7,13,14 | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n26(2A)-n78(2A) | n267n787,9CA_n3A-n26ACA_n3A-n78A7,13,14CA_n26A-n78A7,13,14CA_n26(2A)CA_n78(2A)7 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | n267CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  | CA_n3A-n78A7,13,14CA_n26A-n78A7,13,14 | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n3B-n26(2A)-n78C | n267n787,9CA_n3A-n26ACA_n3A-n78A7,13,14CA_n26A-n78A7,13,14CA_n26(2A)CA_n78C7 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | n267CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  | CA_n3A-n78A7,13,14CA_n26A-n78A7,13,14 | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3A-n28A-n38A | - | n3 | 5, 10, 15, 20, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n38 | 5, 10, 15, 20, 30, 40 |  |
| CA_n3A-n28A-n40A | CA_n3A-n28ACA_n3A-n40ACA_n28A-n40A | n3 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n40 | 20, 40 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35,40 | 1 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n28A-n41A | n417,9CA_n3A-n28ACA_n3A-n41A7,9CA_n28A-n41A7,9 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n28A-n41B | CA_n3A-n28ACA_n3A-n41ACA_n28A-n41A | n3 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | CA_n41B_BCS0 |  |
| CA_n3A-n28A-n75A | CA_n3A-n28A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n28A-n77A | n777,9CA_n3A-n28ACA_n3A-n77A7,9CA_n28A-n77A7,9 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35,40 | 2 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n28A-n77(2A) | n777,9CA_n3A-n28ACA_n3A-n77A7,9CA_n28A-n77A7,9CA_n77(2A)7,9 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n3A-n28A-n77(3A) | n777,9CA_n3A-n28ACA_n3A-n77A7,9CA_n28A-n77A7,9CA_n77(2A)7,9 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n3A-n28A-n78A | n37n787,9CA_n3A-n28A7CA_n3A-n78A7,13, 14CA_n28A-n78A7,13, 14 | n3 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 202 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n28 | 5, 10, 15, 202 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 | 2 |
|  |  | n28 | 5, 10 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n28A-n78C | n787,9CA_n78C7CA_n3A-n28ACA_n3A-n78A7,13,14CA_n28A-n78A7,13,14 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3A-n28A-n78(2A) | n37n787,9CA_n3A-n28A7CA_n3A-n78A7,13, 14CA_n28A-n78A7,13, 14 | n3 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 202 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n28 | 5, 10 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | n37n787,9CA_n78(2A)7CA_n3A-n28A7CA_n3A-n78A7,13, 14CA_n28A-n78A7,13, 14 | n3 | 5, 10, 15, 20, 25, 30, 40 | 2 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3A-n28A-n78(A-C) | CA_n78CCA_n3A-n28ACA_n3A-n78ACA_n28A-n78A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n3B-n28A-n78A | n787,9CA_n3A-n28ACA_n3A-n78A7,13,14CA_n28A-n78A7,13,14 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3BCA_n3A-n78A7,13,14CA_n28A-n78A7,13,14 | n3 | CA_n3B_BCS1 | 1 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n28A-n78(2A) | n787,9CA_n78(2A)7CA_n3A-n28ACA_n3A-n78A7,13,14CA_n28A-n78A7,13,14 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n3BCA_n3A-n78A7,13,14CA_n28A-n78A7,13,14 | n3 | CA_n3B_BCS1 | 1 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n3B-n28A-n78C | n787,9CA_n78C7CA_n3A-n28ACA_n3A-n78A7,13,14CA_n28A-n78A7,13,14 | n3 | CA_n3B_BCS0 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3BCA_n3A-n78A7,13,14CA_n28A-n78A7,13,14 | n3 | CA_n3B_BCS1 | 1 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3A-n28A-n79A | n797,9CA_n3A-n28ACA_n3A-n79A7CA_n28A-n79A7 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n79 | 40, 50, 80, 100 |  |
|  | CA_n3A-n28ACA_n3A-n79ACA_n28A-n79A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n3A-n34A-n41A | CA_n3A-n34ACA_n3A-n41ACA_n34A-n41A | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n34 | See n34 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n34A-n41C | CA_n3A-n34ACA_n3A-n41ACA_n34A-n41A | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n34 | See n34 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
| CA_n3A-n34A-n79A | CA_n3A-n34ACA_n3A-n79ACA_n34A-n79A | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n34 | See n34 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n38A-n40A | - | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n38A-n78A | - | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n39A-n41A | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n41 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n39A-n79A | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n79 | 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n40A-n78A | CA_n3A-n40ACA_n3A-n78ACA_n40A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n40A-n105A | CA_n3A-n40ACA_n3A-n105ACA_n40A-n105A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n3A-n41A-n71A | CA_n3A-n41ACA_n3A-n71ACA_n41A-n71A | n3 | 5,10,15,20,25,30,35,40,45,50 | 0 |
|  |  | n41 | 5,10,15,20,25,30,35,40,45,50,60,70,80,90,100 |  |
|  |  | n71 | 5,10,15,20 |  |
| CA_n3A-n41A-n78C | CA_n78CCA_n3A-n41ACA_n3A-n78ACA_n3A-n78CCA_n41A-n78ACA_n41A-n78C | n3 | 5,10,15,20,25,30,35,40,45,50 | 4 and 5 |
|  |  | n41 | 5,10,15,20,25,30,35,40,45,50,60,70,80,90,100 |  |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n3(2A)-n41A-n78A | CA_n3A-n41ACA_n3A-n78ACA_n41A-n78A | n3 | CA_n3(2A)_BCS0 | 4 and 5 |
|  |  | n41 | 5,10,15,20,25,30,35,40,45,50,60,70,80,90,100 |  |
|  |  | n78 | 10,15,20,25,30,40,50,60,70,80,90,100 |  |
| CA_n3(2A)-n41A-n78C | CA_n3A-n41ACA_n3A-n78ACA_n41A-n78ACA_n41A-n78C | n3 | CA_n3(2A)_BCS0 | 4 and 5 |
|  |  | n41 | 5,10,15,20,25,30,35,40,45,50,60,70,80,90,100 |  |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n3A-n71A-n78A | CA_n3A-n71ACA_n3A-n78ACA_n71A-n78A | n3 | 5,10,15,20,25,30,35,40,45,50 | 4 and 5 |
|  |  | n71 | 5,10,15,20 |  |
|  |  | n78 | 10,15,20,25,30,40,50,60,70,80,90,100 |  |
| CA_n3(2A)-n71A-n78A | CA_n3A-n71ACA_n3A-n78ACA_n71A-n78A | n3 | CA_n3(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | 5,10,15,20 |  |
|  |  | n78 | 10,15,20,25,30,40,50,60,70,80,90,100 |  |
| CA_n3(2A)-n71A-n78C | CA_n78CCA_n3A-n71ACA_n3A-n78ACA_n3A-n78CCA_n71A-n78ACA_n71A-n78C | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n71 | 5,10,15,20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n3A-n71A-n78C | CA_n78CCA_n3A-n71ACA_n3A-n78ACA_n3A-n78CCA_n71A-n78ACA_n71A-n78C | n3 | 5,10,15,20,25,30,35,40,45,50 | 4 and 5 |
|  |  | n71 | 5,10,15,20 |  |
|  |  | n78 | CA_n78C_BCS 4 and 5 |  |
| CA_n3A-n77A-n79A4 | n777,9n797,9CA_n3A-n77A7CA_n3A-n79A7CA_n77A-n79A7 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n77(2A)-n79A4 | n777,9n797,9CA_n77(2A)7CA_n3A-n77A7CA_n3A-n79A7CA_n77A-n79A7 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n77(3A)-n79A4 | n777,9n797,9CA_n77(2A)7CA_n3A-n77A7CA_n3A-n79A7CA_n77A-n79A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n40A-n41A | CA_n3A-n40ACA_n3A-n41ACA_n40A-n41A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n40A-n41C | CA_n3A-n40ACA_n3A-n41ACA_n40A-n41A | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | CA_n41C_BCS4 and 5 |  |
| CA_n3A-n40A-n77A | CA_n3A-n40ACA_n3A-n77ACA_n40A-n77A | n3 | 5, 10, 15, 20, 30, 35, 40, 45, 50 | 0 |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n40A-n77(2A) | CA_n3A-n40ACA_n3A-n77ACA_n40A-n77A | n3 | 5, 10, 15, 20, 30, 35, 40, 45, 50 | 0 |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n3A-n40A-n79A | CA_n3A-n40ACA_n3A-n79ACA_n40A-n79A | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n41A-n77A | n417,9n777,9CA_n3A-n41A7,9CA_n3A-n77A7,9CA_n41A-n77A7,9 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | - | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n41B-n77A | CA_n3A-n41ACA_n3A-n77ACA_n41A-n77A | n3 | 5, 10, 15, 20 | 0 |
|  |  | n41 | CA_n41B_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n41B-n77(2A) | CA_n3A-n41ACA_n3A-n77ACA_n41A-n77A | n3 | 5, 10, 15, 20 | 0 |
|  |  | n41 | CA_n41B_BCS0 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n3A-n41A-n77(2A) | n417,9n777,9CA_n3A-n41A7,9CA_n3A-n77A7,9CA_n41A-n77A7,9CA_n77(2A)7 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  | - | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n3A-n41A-n77(3A) | n417,9n777,9CA_n3A-n41A7,9CA_n3A-n77A7,9CA_n41A-n77A7,9CA_n77(2A)7 | n3 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
| CA_n3A-n41A-n78A | - | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3A-n41ACA_n3A-n78ACA_n41A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
| CA_n3A-n41A-n78(2A) | CA_n3A-n41ACA_n3A-n78ACA_n41A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n3A-n41A-n79A | n3n417, 9n797, 9CA_n3A-n41A7CA_n3A-n79A7CA_n41A-n79A7 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30 | 1 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n3 | 5, 10, 15, 20, 25, 30 | 2 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n41A-n79C | CA_n3A-n41ACA_n3A-n79ACA_n41A-n79A | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n3A-n41C-n79A | CA_n41CCA_n3A-n41ACA_n3A-n79ACA_n41A-n79A | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS4 and 5 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n41C-n79C | CA_n3A-n41ACA_n3A-n79ACA_n41A-n79A | n3 | See n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS4 and 5 |  |
|  |  | n79 | CA_n79C_BCS4 and 5 |  |
| CA_n3A-n67A-n78A | CA_n3A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n67A-n78(2A) | CA_n78(2A)CA_n3A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3A-n71A-n77A | CA_n3A-n71ACA_n3A-n77ACA_n71A-n77A | n3 | 5,10,15,20,25,30,35,40,45,50 | 0 |
|  |  | n71 | 5,10,15,20 |  |
|  |  | n77 | 10,15,20,25,30,40,50,60,70,80,90,100 |  |
| CA_n3A-n71A-n77(2A) | CA_n3A-n71ACA_n3A-n77ACA_n71A-n77A | n3 | 5,10,15,20,25,30,35,40,45,50 | 0 |
|  |  | n71 | 5,10,15,20 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n3A-n75A-n78A | CA_n3A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n75A-n78(2A) | CA_n78(2A) CA_n3A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n3A-n78A-n79A5 | n787,9 | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  | n797CA_n3A-n78A7CA_n3A-n79A7CA_n78A-n79A5,7 | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  | CA_n3A-n78A CA_n3A-n79ACA_n78A-n79A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n78A-n79C | - | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n3B-n78A-n79A | - | n3 | CA_n3B_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n3B-n78A-n79C | - | n3 | CA_n3B_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n3(2A)-n78A-n79A | - | n3 | CA_n3(2A)_BCS1 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n3(2A)-n78A-n79C | - | n3 | CA_n3(2A)_BCS1 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n3A-n78A-n105A | CA_n3A-n78ACA_n3A-n105ACA_n78A-n105A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n5A-n7A-n25A | CA_n5A-n7ACA_n5A-n25ACA_n7A-n25A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 35, 40, 45 |  |
| CA_n5A-n7A-n25(2A) | CA_n5A-n7ACA_n5A-n25ACA_n7A-n25A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
| CA_n5A-n7A-n28A | - | n5 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
| CA_n5A-n7A-n40A | CA_n5A-n7ACA_n5A-n40ACA_n7A-n40A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n7A-n66A | CA_n5A-n7ACA_n5A-n66ACA_n7A-n66A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 35, 40, 45 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n7A-n77A | n777,9CA_n5A-n7ACA_n5A-n77A7CA_n7A-n77A7 | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | See n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n7A-n77(2A) | n777,9CA_n77(2A)7CA_n5A-n7ACA_n5A-n77A7CA_n7A-n77A7 | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n5 | See n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | See n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n5A-n7A-n77(3A) | n777,9CA_n77(2A)7CA_n5A-n7ACA_n5A-n77A7CA_n7A-n77A7 | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
| CA_n5A-n7A-n78A | n787,9CA_n5A-n78A7CA_n7A-n78A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n5A-n7ACA_n5A-n78ACA_n7A-n78A | n5 | 5, 10, 15, 20 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n7A-n78(2A) | CA_n5A-n7ACA_n5A-n78ACA_n7A-n78A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n5A-n7A-n78C | CA_n78CCA_n5A-n7ACA_n5A-n78ACA_n7A-n78A | n5 | See n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | See n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78C_BCS4 and 5 |  |
| CA_n5A-n7A-n78(A-C) | CA_n78CCA_n5A-n7ACA_n5A-n78ACA_n7A-n78A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n5A-n7B-n78A | n787,9CA_n5A-n78A7CA_n7A-n78A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n5A-n7ACA_n5A-n78ACA_n7A-n78ACA_n7B | n5 | 5, 10, 15, 20 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 704, 80, 90, 100 |  |
| CA_n5A-n7A-n105A | CA_n5A-n7ACA_n5A-n105ACA_n7A-n105A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n5A-n12A-n77A | n777CA_n5A-n12ACA_n5A-n77A7CA_n12A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n12A-n77(2A) | n777CA_n5A-n12A CA_n5A-n77A7 CA_n12A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n5A-n14A-n30A | CA_n5A-n14ACA_n5A-n30ACA_n14A-n30A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n14A-n66A | CA_n5A-n14ACA_n5A-n66ACA_n14A-n66A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n14A-n66(2A) | CA_n5A-n14ACA_n5A-n66ACA_n14A-n66A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n5A-n14A-n77A | n777CA_n5A-n14ACA_n5A-n77A7CA_n14A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n14A-n77(2A) | n777CA_n5A-n14A CA_n5A-n77A7 CA_n14A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n5A-n25A-n29A | CA_n5A-n25A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n29 | 5, 10 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n25A-n41A | CA_n5A-n25ACA_n5A-n41ACA_n25A-n41A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 35, 40, 45 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
| CA_n5A-n25(2A)-n41A | CA_n5A-n25ACA_n5A-n41ACA_n25A-n41A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n25 | CA_n25(2A) |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
| CA_n5A-n25A-n66A | CA_n5A-n25ACA_n5A-n66ACA_n25A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n25(2A)-n66A | CA_n5A-n25ACA_n5A-n66ACA_n25A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n5A-n25A-n66(2A) | CA_n5A-n25ACA_n5A-n66ACA_n25A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n5A-n25(2A)-n66(2A) | CA_n5A-n25ACA_n5A-n66ACA_n25A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n5A-n25A-n77A | n777,9CA_n5A-n25A | n5 | 5, 10, 15, 20 | 0 |
|  | CA_n5A-n77A7 | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  | CA_n25A-n77A7 | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n25(2A)-n77A | n777,9CA_n5A-n25ACA_n5A-n77A7CA_n25A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n25A-n77(2A) | n777,9CA_n77(2A)7CA_n5A-n25ACA_n5A-n77A7CA_n25A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n5A-n25A-n77(3A) | n777,9CA_n77(2A)7CA_n5A-n25ACA_n5A-n77A7CA_n25A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
| CA_n5A-n25(2A)-n77(2A) | n777,9CA_n5A-n25ACA_n5A-n77A7CA_n25A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n5A-n25A-n78A | n787,9CA_n5A-n25ACA_n5A-n78A7CA_n25A-n78A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n25(2A)-n78A | n787,9CA_n5A-n25ACA_n5A-n78A7CA_n25A-n78A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n25A-n78(2A) | n787,9CA_n5A-n25ACA_n5A-n78A7CA_n25A-n78A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n5A-n25(2A)-n78(2A) | n787,9CA_n5A-n25ACA_n5A-n78A7CA_n25A-n78A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n5A-n28A-n78A | CA_n5A-n28ACA_n5A-n78ACA_n28A-n78A | n5 | See n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n28A-n79A | CA_n5A-n28ACA_n5A-n79ACA_n28A-n79A | n5 | See n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n28A-n105A | CA_n5A-n28ACA_n5A-n105A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n5A-n29A-n66A | CA_n5A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n29A-n77A | n777CA_n5A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n29A-n77(2A) | n777CA_n5A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n5A-n30A-n66A | CA_n5A-n30ACA_n5A-n66ACA_n30A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n30A-n66(2A) | CA_n5A-n30ACA_n5A-n66ACA_n30A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n5A-n30A-n66(3A) | CA_n5A-n30ACA_n5A-n66ACA_n30A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
| CA_n5A-n30A-n77A | n777,9CA_n5A-n30ACA_n5A-n77A7CA_n30A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n30A-n77(2A) | n777,9CA_n5A-n30A CA_n5A-n77A7 CA_n30A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n5A-n40A-n78A | CA_n5A-n40ACA_n5A-n78ACA_n40A-n78A | n5 | 5, 10, 15, 20, 251 | 0 |
|  |  | n40 | 58, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90,100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90,100 |  |
| CA_n5A-n40A-n105A | CA_n5A-n40A CA_n5A-n105A CA_n40A-n105A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n5A-n41A-n66A | CA_n5A-n41A CA_n5A-n66A CA_n41A-n66A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 35, 40, 45 |  |
| CA_n5A-n41A-n77A | CA_n5A-n41ACA_n5A-n77ACA_n41A-n77A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n41A-n77(2A) | CA_n5A-n41ACA_n5A-n77ACA_n41A-n77A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n5A-n48A-n66A | CA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n48A-n66A | CA_n5A-n48ACA_n5A-n66ACA_n48A-n66ACA_n5B | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48(A-B)-n66A | CA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n5 | 5, 10, 15, 20, 251 | 0 |
|  |  | n48 | CA_n48(A-B)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | 5, 10, 15, 20, 251 | 1 |
|  |  | n48 | CA_n48(A-B)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(A-B)_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48B-n66A | CA_n48BCA_n5A-n48ACA_n5A-n48BCA_n5A-n66ACA_n48A-n66ACA_n48B-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48B_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | 5, 10, 15, 20 | 2 |
|  |  | n48 | CA_n48B_BCS2 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n48B-n66A | CA_n48BCA_n5A-n48ACA_n5A-n48BCA_n5A-n66ACA_n5BCA_n48A-n66ACA_n48B-n66A | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48(2A)-n66A | CA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n48(2A)-n66A | CA_n5A-n48ACA_n5A-n66ACA_n5BCA_n48A-n66A | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48A-n66(2A) | CA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n5A-n48B-n66(2A) | CA_n5A-n48ACA_n5A-n66ACA_n5A-n48BCA_n48A-n66ACA_n48B-n66ACA_n48B | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n5A-n48(2A)-n66(2A) | CA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n5B-n48A-n66(2A) | CA_n5A-n48ACA_n5A-n66ACA_n5BCA_n48A-n66A | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n5B-n48(2A)-n66(2A) | CA_n5A-n48ACA_n5A-n66ACA_n5BCA_n48A-n66A | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n5B-n48B-n66(2A) | CA_n5A-n48ACA_n5A-n48BCA_n5A-n66ACA_n5BCA_n48A-n66ACA_n48B-n66ACA_n48B | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n5A-n48A-n77A | n777,9CA_n5A-n48ACA_n5A-n77A7,13,14 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n5A-n48ACA_n5A-n77A7,13,14 | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n48A-n77A | n777,9CA_n5A-n48ACA_n5A-n77A7,13,14CA_n5B | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48A-n77C | n777,9CA_n5A-n48ACA_n5A-n77A7,13,14CA_n77C7,9 | n5 | 5, 10, 15, 20, 251 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20, 251 | 1 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n777,9CA_n5A-n48ACA_n5A-n77A7,13,14CA_n5A-n77CCA_n77C7,9 | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n5A-n48B-n77A | n777,9CA_n5A-n48ACA_n5A-n77A7,13,14 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48B_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | 5, 10, 15, 20 | 2 |
|  |  | n48 | CA_n48B_BCS2 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n5A-n48ACA_n5A-n48BCA_n5A-n77A7,13,14CA_n48B | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48B-n77C | n777,9CA_n5A-n48ACA_n5A-n77A7,13,14CA_n77C | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  |  | n5 | 5, 10, 15, 20 | 2 |
|  |  | n48 | CA_n48B_BCS1 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20 | 3 |
|  |  | n48 | CA_n48B_BCS1 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n777,9CA_n5A-n48ACA_n5A-n48BCA_n5A-n77A7,13,14CA_n5A-n77CCA_n48BCA_n77C | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n5A-n48(2A)-n77A | n777,9CA_n5A-n48ACA_n5A-n77A7,13,14 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48(2A)-n77C | n777,9CA_n5A-n48ACA_n5A-n77A7,13,14CA_n77C | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  |  | n5 | 5, 10, 15, 20 | 2 |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20 | 3 |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n777,9CA_n5A-n48ACA_n5A-n77A7,13,14CA_n5A-n77CCA_n77C | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n5B-n48A-n77C | n777,9CA_n5A-n48ACA_n5A-n77A7,13,14CA_n5A-n77CCA_n5BCA_n77C7,9 | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n5B-n48(2A)-n77A | n777,9CA_n5A-n48ACA_n5A-n77A7,13,14CA_n5B | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n48(2A)-n77C | n777,9CA_n5A-n48ACA_n5A-n77A7,13,14CA_n5A-n77CCA_n5BCA_n77C | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n5B-n48B-n77A | n777,9CA_n5A-n48ACA_n5A-n48BCA_n5A-n77A7,13,14CA_n5BCA_n48B | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n48B-n77C | n777,9CA_n5A-n48ACA_n5A-n48BCA_n5A-n77A7,13,14CA_n5A-n77CCA_n5BCA_n48BCA_n77C | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n5A-n66A-n77A | n777,9CA_n5A-n66ACA_n5A-n77A7,13,14CA_n66A-n77A7,13,14 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n66A-n77A | n777,9CA_n5A-n66ACA_n5A-n77A7,13,14CA_n66A-n77A7,13,14CA_n5B | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n66(2A)-n77A | n777,9CA_n5A-n66ACA_n5A-n77A7,13,14CA_n66A-n77A7,13,14 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n5A-n66ACA_n5A-n77A7,13,14CA_n66A-n77A7,13,14 | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n66(2A)-n77C | n777,9CA_n5A-n66ACA_n5A-n77A7,13,14CA_n5A-n77CCA_n66A-n77A7,13,14CA_n66A-n77CCA_n77C7,9 | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n5B-n66(2A)-n77A | n777,9CA_n5A-n66ACA_n5A-n77A7,13,14CA_n66A-n77A7,13,14CA_n5B | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n66(2A)-n77C | n777,9CA_n5A-n66ACA_n5A-n77A7,13,14CA_n5A-n77CCA_n5BCA_n66A-n77A7,13,14CA_n66A-n77CCA_n77C7,9 | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n5A-n66(2A)-n77(2A) | n777,9CA_n5A-n66ACA_n5A-n77A7CA_n66A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n5A-n66(3A)-n77A | n777,9CA_n5A-n66ACA_n66A-n77A7CA_n5A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n66(3A)-n77(2A) | n777,9CA_n5A-n66ACA_n66A-n77A7CA_n5A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n5A-n66A-n77C | n777,9CA_n5A-n66ACA_n5A-n77A7,13,14CA_n66A-n77A7,13,14CA_n77C7,9 | n5 | 5, 10, 15, 20, 251 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n5 | 5, 10, 15, 20, 251 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n777,9CA_n5A-n66ACA_n5A-n77A7,13,14CA_n5A-n77CCA_n66A-n77ACA_n66A-n77CCA_n77C7,9 | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n5B-n66A-n77C | n777,9CA_n5A-n66ACA_n5A-n77A7,13,14CA_n5A-n77CCA_n5BCA_n66A-n77ACA_n66A-n77CCA_n77C7,9 | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n5A-n66A-n77(2A) | n777,9CA_n5A-n66ACA_n5A-n77A7CA_n66A-n77A7CA_n77(2A)7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n66 | 5, 10, 15, 20, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n5A-n66A-n77(3A) | CA_n77(2A)CA_n5A-n66ACA_n5A-n77A7CA_n66A-n77A7 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n5A-n66A-n78A | CA_n5A-n66ACA_n5A-n78ACA_n66A-n78A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n5 | 5, 10, 15, 20 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n66(2A)-n78A | CA_n5A-n66A CA_n5A-n78A CA_n66A-n78A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n66A-n78(2A) | CA_n5A-n66A CA_n5A-n78A CA_n66A-n78A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n5A-n66(2A)-n78(2A) | CA_n5A-n66A CA_n5A-n78A CA_n66A-n78A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n5A-n78A-n79A | CA_n5A-n78ACA_n5A-n79ACA_n78A-n79A | n5 | See n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n78A-n105A | CA_n5A-n78A CA_n5A-n105A CA_n78A-n105A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n7A-n8A-n28A | CA_n7A-n8ACA_n7A-n28ACA_n8A-n28A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
| CA_n7A-n8A-n40A | CA_n7A-n8ACA_n7A-n40ACA_n8A-n40A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n8A-n78A | CA_n7A-n8ACA_n7A-n78ACA_n8A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n8A-n79A | CA_n7A-n8ACA_n7A-n79ACA_n8A-n79A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7(2A)-n8A-n78A | CA_n7A-n8ACA_n7A-n78ACA_n8A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n12A-n25A | - | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n12 | n12 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n12A-n66A | - | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 35, 40, 45 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n12 | n12 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n12A-n71A | CA_n7A-n12ACA_n7A-n71A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n7A-n12A-n77A | - | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n12 | n12 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n20A-n28A17 | CA_n7A-n20ACA_n7A-n28ACA_n20A-n28A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n20A-n67A | CA_n7A-n20A | n7 | See n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | See n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | See n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n20A-n75A | CA_n7A-n20A | n7 | See n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | See n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | See n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n20A-n78A | CA_n7A-n20A CA_n7A-n78A CA_n20A-n78A | n7 | See n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | See n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n20A-n78(2A) | CA_n7A-n20A CA_n7A-n78A CA_n20A-n78ACA_n78(2A) | n7 | See n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | See n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n7A-n25A-n29A | CA_n7A-n25A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n25A-n66A | CA_n7A-n25ACA_n7A-n66ACA_n25A-n66A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n25(2A)-n66A | CA_n7A-n25ACA_n7A-n66ACA_n25A-n66A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n7A-n25(2A)-n66(2A) | CA_n7A-n25ACA_n7A-n66ACA_n25A-n66A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n7A-n25A-n66(2A) | CA_n7A-n25ACA_n7A-n66ACA_n25A-n66A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n7(2A)-n25A-n66A | CA_n7A-n25ACA_n7A-n66ACA_n25A-n66A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n7(2A)-n25(2A)-n66A | CA_n7A-n25ACA_n7A-n66ACA_n25A-n66A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n7(2A)-n25A-n66(2A) | CA_n7A-n25ACA_n7A-n66ACA_n25A-n66A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n7(2A)-n25(2A)-n66(2A) | CA_n7A-n25ACA_n7A-n66ACA_n25A-n66A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n7A-n25A-n71A | CA_n7A-n25ACA_n7A-n71ACA_n25A-n71A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n25A-n77A | n777,9CA_n7A-n25ACA_n7A-n77A7CA_n25A-n77A7 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n7A-n25ACA_n7A-n77ACA_n25A-n77A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n25(2A)-n77A | n777,9CA_n7A-n25ACA_n7A-n77A7CA_n25A-n77A7 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n25A-n77(2A) | n777,9CA_n77(2A)7CA_n7A-n25ACA_n7A-n77A7CA_n25A-n77A7 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  | CA_n77(2A)CA_n7A-n25ACA_n7A-n77ACA_n25A-n77A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n7A-n25A-n77(3A) | n777,9CA_n77(2A)7CA_n7A-n25ACA_n7A-n77A7CA_n25A-n77A7 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  | CA_n77(2A)CA_n7A-n25ACA_n7A-n77ACA_n25A-n77A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n7A-n25(2A)-n77(2A) | n777,9CA_n7A-n25ACA_n7A-n77A7CA_n25A-n77A7 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7(2A)-n25A-n77A | n777,9CA_n7A-n25ACA_n7A-n77A7CA_n25A-n77A7 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7(2A)-n25(2A)-n77A | n777,9CA_n7A-n25ACA_n7A-n77A7CA_n25A-n77A7 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7(2A)-n25A-n77(2A) | n777,9CA_n7A-n25ACA_n7A-n77A7CA_n25A-n77A7 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7(2A)-n25(2A)-n77(2A) | n777,9CA_n7A-n25ACA_n7A-n77A7CA_n25A-n77A7 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7A-n25A-n78A | CA_n7A-n25ACA_n7A-n78ACA_n25A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 704, 80, 904, 100 |  |
| CA_n7(2A)-n25A-n78A | CA_n7A-n25ACA_n7A-n78ACA_n25A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 704, 80, 904, 100 |  |
| CA_n7A-n25(2A)-n78A | CA_n7A-n25ACA_n7A-n78ACA_n25A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 704, 80, 904, 100 |  |
| CA_n7(2A)-n25(2A)-n78A | CA_n7A-n25ACA_n7A-n78ACA_n25A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 704, 80, 904, 100 |  |
| CA_n7A-n25A-n78(2A) | CA_n7A-n25ACA_n7A-n78ACA_n25A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7(2A)-n25A-n78(2A) | CA_n7A-n25ACA_n7A-n78ACA_n25A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n7A-n25(2A)-n78(2A) | CA_n7A-n25ACA_n7A-n78ACA_n25A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n7(2A)-n25(2A)-n78(2A) | CA_n7A-n25ACA_n7A-n78ACA_n25A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n7A-n26A-n78A | n77n267n787,9CA_n7A-n26ACA_n7A-n78A7,13,14CA_n26A-n78A7,13,14 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n26A-n78(2A) | n77n267n787,9CA_n78(2A)7CA_n7A-n26ACA_n7A-n78A7,13,14CA_n26A-n78A7,13,14 | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | n77n267CA_n78(2A) | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n7A-n78A7,13,14CA_n26A-n78A7,13,14 | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n7A-n26A-n78C | n77n267n787,9CA_n7A-n26ACA_n7A-n78A7,13,14CA_n26A-n78A7,13,14CA_n78C7 | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n7A-n26A-n78(A-C) | CA_n78CCA_n7A-n26ACA_n7A-n78A7,13,14CA_n26A-n78A7,13,14 | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n7A-n26(2A)-n78A | n77n267n787,9CA_n7A-n26ACA_n7A-n78A7,13,14CA_n26A-n78A7,13,14CA_n26(2A) | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n26(2A)-n78(2A) | n77n267n787,9CA_n78(2A) 7CA_n7A-n26ACA_n7A-n78A7,13,14CA_n26A-n78A7,13,14CA_n26(2A) | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n7A-n26(2A)-n78C | n77n267n787,9CA_n7A-n26ACA_n7A-n78A7,13,14CA_n26A-n78A7,13,14CA_n26(2A)CA_n78C7 | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n7B-n26A-n78A | n77n267n787,9CA_n7A-n26ACA_n7A-n78A7,13,14CA_n26A-n78A7,13,14CA_n7B | n7 | CA_n7B_BCS0 | 0 |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7B-n26A-n78(2A) | n77n267n787,9CA_n78(2A)7CA_n7A-n26ACA_n7A-n78A7,13,14CA_n7BCA_n26A-n78A7,13,14 | n7 | CA_n7B_BCS0 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | n77n267CA_n78(2A) | n7 | CA_n7B_BCS4 and 5 | 4 and 5 |
|  | CA_n7A-n78A7,13,14CA_n26A-n78A7,13,14 | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n7B-n26A-n78C | n77n267n787,9CA_n7A-n26ACA_n7A-n78A7,13,14CA_n7BCA_n26A-n78A7,13,14CA_n78C7 | n7 | CA_n7B_BCS0 | 0 |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n7B-n26(2A)-n78A | n77n267n787,9CA_n7A-n26ACA_n7A-n78A7,13,14CA_n26A-n78A7,13,14CA_n7BCA_n26(2A) | n7 | CA_n7B_BCS0 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7B-n26(2A)-n78(2A) | n77n267n787,9CA_n78(2A) 7CA_n7A-n26ACA_n7A-n78A7,13,14CA_n26A-n78A7,13,14CA_n7BCA_n26(2A) | n7 | CA_n7B_BCS0 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n7B-n26(2A)-n78C | n77n267n787,9CA_n7A-n26ACA_n7A-n78A7,13,14CA_n26A-n78A7,13,14CA_n7BCA_n26(2A)CA_n78C7 | n7 | CA_n7B_BCS0 | 0 |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n7A-n28A-n38A11 | - | n7 | 5, 10, 15, 20, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n38 | 5, 10, 15, 20, 30, 40 |  |
| CA_n7A-n28A-n40A | CA_n7A-n28ACA_n7A-n40ACA_n28A-n40A | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n28A-n75A | CA_n7A-n28A | n7 | See n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | See n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | See n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n28A-n78A | n77n787,9CA_n7A-n78A7,13,14CA_n28A-n78A7,13,14 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  | n77n787,9CA_n7A-n28A7CA_n7A-n78A7,13,14CA_n28A-n78A7,13,14 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 704, 80, 90, 100 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n28A-n78(2A) | n77n787,9CA_n7A-n28A7CA_n7A-n78A7,13,14CA_n28A-n78A7,13,14CA_n78(2A)7 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n7A-n28A-n78C | n77n787,9CA_n78C7CA_n7A-n28ACA_n7A-n78A7,13,14CA_n28A-n78A7,13,14 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n7A-n28A-n78(A-C) | CA_n78CCA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(A-C)_BCS1 |  |
| CA_n7B-n28A-n78A | n77n787,9CA_n7A-n78A7,13,14CA_n28A-n78A7,13,14 | n7 | CA_n7B_BCS0 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  | n77CA_n7A-n28ACA_n7A-n78A7,13,14CA_n28A-n78A7,13,14CA_n7B | n7 | CA_n7B_BCS0 | 1 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 704, 80, 90, 100 |  |
| CA_n7B-n28A-n78(2A) | n77n787,9CA_n7BCA_n7A-n28ACA_n7A-n78A7,13,14CA_n28A-n78A7,13,14CA_n78(2A)7 | n7 | CA_n7B_BCS0 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7B-n28A-n78C | n77n787CA_n7BCA_n78C7CA_n7A-n28ACA_n7A-n78A7,13,14CA_n28A-n78A7,13,14 | n7 | CA_n7B_BCS0 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n7A-n28A-n79A | CA_n7A-n28ACA_n7A-n79ACA_n28A-n79A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n29A-n66A | CA_n7A-n66A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n29A-n77A | CA_n7A-n77A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n29A-n77(2A) | CA_n7A-n77ACA_n77(2A) | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n7A-n29A-n77(3A) | CA_n7A-n77ACA_n77(2A) | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n7A-n38A-n78A10 | - | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n40A-n78A | CA_n7A-n40ACA_n7A-n78ACA_n40A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n40 | 5, 10, 15, 20, 30, 40, 50, 60, 80 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n40A-n79A | CA_n7A-n40ACA_n7A-n79ACA_n40A-n79A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n40A-n105A | CA_n7A-n40ACA_n7A-n105ACA_n40A-n105A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n40 | 5,10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n7A-n46A-n78A | CA_n7A-n46A CA_n7A-n78A CA_n46A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | 20, 40, 60, 80 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n46C-n78A | CA_n7A-n46A CA_n7A-n78A CA_n46A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46C_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n46D-n78A | CA_n7A-n46A CA_n7A-n78A CA_n46A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46D_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n46(2A)-n78A | CA_n7A-n46A CA_n7A-n78A CA_n46A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n46(2A)-n78(2A) | CA_n7A-n46A CA_n7A-n78A CA_n46A-n78ACA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7A-n46A-n78(2A) | CA_n7A-n46A CA_n7A-n78A CA_n46A-n78ACA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | 20, 40, 60, 80 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7A-n46C-n78(2A) | CA_n7A-n46A CA_n7A-n78A CA_n46A-n78ACA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46C_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7A-n46D-n78(2A) | CA_n7A-n46A CA_n7A-n78A CA_n46A-n78ACA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n46 | CA_n46D_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7A-n66A-n71A | CA_n7A-n66ACA_n7A-n71ACA_n66A-n71A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n66A-n77A | n777,9CA_n7A-n66ACA_n7A-n77A7CA_n66A-n77A7 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n66(2A)-n77A | n777,9CA_n7A-n66ACA_n7A-n77A7CA_n66A-n77A7 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n66A-n77(2A) | n777,9CA_n77(2A)CA_n7A-n66A CA_n7A-n77A7 CA_n66A-n77A7 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n7A-n66A-n77(3A) | n777,9CA_n77(2A)7CA_n77(2A) 7CA_n7A-n66ACA_n7A-n77A7CA_n66A-n77A7 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n7A-n66(2A)-n77(2A) | n777,9CA_n7A-n66A CA_n7A-n77A7 CA_n66A-n77A7 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7(2A)-n66A-n77A | n777,9CA_n7A-n66A CA_n7A-n77A7 CA_n66A-n77A7 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7(2A)-n66(2A)-n77A | n777,9CA_n7A-n66A CA_n7A-n77A7 CA_n66A-n77A7 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7(2A)-n66A-n77(2A) | n777,9CA_n7A-n66A CA_n7A-n77A7 CA_n66A-n77A7 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7(2A)-n66(2A)-n77(2A) | n777,9CA_n7A-n66A CA_n7A-n77A7 CA_n66A-n77A7 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7A-n66A-n78A | n787,9CA_n7A-n66ACA_n7A-n78A7CA_n66A-n78A7 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n66A-n78(2A) | CA_n7A-n66ACA_n7A-n78ACA_n66A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7(2A)-n66A-n78A | CA_n7A-n66ACA_n7A-n78ACA_n66A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n66(2A)-n78A | CA_n7A-n66ACA_n7A-n78ACA_n66A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7(2A)-n66(2A)-n78A | CA_n7A-n66ACA_n7A-n78ACA_n66A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n66(2A)-n78(2A) | CA_n7A-n66ACA_n7A-n78ACA_n66A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7(2A)-n66A-n78(2A) | CA_n7A-n66ACA_n7A-n78ACA_n66A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7(2A)-n66(2A)-n78(2A) | CA_n7A-n66ACA_n7A-n78ACA_n66A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7A-n67A-n78A | CA_n7A-n78A | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n67A-n78(2A) | CA_n7A-n78A CA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n7A-n71A-n77A | n777,9CA_n7A-n71ACA_n7A-n77A7CA_n71A-n77A7 | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n71 | 5, 10, 15, 20, 25, 30, 35 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n7 | See n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | See n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n71A-n77(2A) | n777,9CA_n77(2A)7CA_n7A-n71ACA_n7A-n77A7CA_n71A-n77A7 | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n71 | 5, 10, 15, 20, 25, 30, 35 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n7 | See n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | See n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n7A-n71A-n77(3A) | n777,9CA_n77(2A)7CA_n7A-n71ACA_n7A-n77A7CA_n71A-n77A7 | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 | 0 |
|  |  | n71 | 5, 10, 15, 20, 25, 30, 35 |  |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
| CA_n7A-n75A-n78A | CA_n7A-n78A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n75A-n78(2A) | CA_n78(2A)CA_n7A-n78A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n7A-n78A-n79A | CA_n7A-n78ACA_n7A-n79ACA_n78A-n79A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n78A-n102A | CA_n7A-n78ACA_n7A-n102ACA_n78A-n102A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n7A-n78A-n102B | CA_n7A-n78ACA_n7A-n102ACA_n7A-n102BCA_n78A-n102ACA_n78A-n102B | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n7A-n78A-n102C | CA_n7A-n78ACA_n7A-n102ACA_n7A-n102CCA_n78A-n102ACA_n78A-n102C | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n7A-n78A-n102D | CA_n7A-n78ACA_n7A-n102ACA_n78A-n102A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n7A-n78A-n102E | CA_n7A-n78ACA_n7A-n102ACA_n78A-n102A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n7A-n78A-n102(2A) | CA_n7A-n78ACA_n7A-n102ACA_n78A-n102A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n7A-n78(2A)-n102A | CA_n7A-n78ACA_n7A-n102ACA_n78A-n102ACA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n7A-n78(2A)-n102B | CA_n7A-n78ACA_n7A-n102ACA_n7A-n102BCA_n78A-n102ACA_n78A-n102BCA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n7A-n78(2A)-n102C | CA_n7A-n78ACA_n7A-n102ACA_n7A-n102CCA_n78A-n102ACA_n78A-n102CCA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n7A-n78(2A)-n102D | CA_n7A-n78ACA_n7A-n102ACA_n78A-n102ACA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n7A-n78(2A)-n102E | CA_n7A-n78ACA_n7A-n102ACA_n78A-n102ACA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n7A-n78(2A)-n102(2A) | CA_n7A-n78ACA_n7A-n102ACA_n78A-n102ACA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n7A-n78A-n105A | CA_n7A-n78ACA_n7A-n105ACA_n78A-n105A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |

##### Table 5.5A.3.2-1b

Table 5.5A.3.2-1b: NR CA configurations and bandwidth combinations sets defined for inter-band CA (three bands)

| NR CA configuration | Uplink CA configurationor single uplink carrier6 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n8A-n20A-n28A | CA_n8A-n20A | n8 | 5, 10, 15, 20 | 0 |
|  | CA_n8A-n28A | n20 | 5, 10, 15, 20 |  |
|  | CA_n20A-n28A | n28 | 5, 10, 15, 20, 25, 30 |  |
| CA_n8A-n20A-n75A | CA_n8A-n20A | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n28A-n40A | CA_n8A-n28ACA_n8A-n40ACA_n28A-n40A | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40  channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n28A-n75A | CA_n8A-n28A | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n28A-n77A | CA_n8A-n28ACA_n8A-n77ACA_n28A-n77A | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n28A-n77(2A) | CA_n8A-n28ACA_n8A-n77ACA_n28A-n77A | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n8A-n28A-n78A | CA_n8A-n28ACA_n8A-n78ACA_n28A-n78A | n8 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n8A-n28A-n79A | CA_n8A-n28ACA_n8A-n79ACA_n28A-n79A | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n38A-n40A | - | n8 | 5, 10, 15, 20 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n8A-n39A-n40A | CA_n8A-n39ACA_n8A-n40ACA_n39A-n40A | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n39A-n41A | CA_n8A-n39ACA_n8A-n41ACA_n39A-n41A | n8 | 5, 10, 15, 20 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 100 |  |
|  | - | n8 | 5, 10, 15, 20 | 1 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n41 | 10, 15, 20, 40, 50, 60 |  |
|  | CA_n8A-n39ACA_n8A-n41ACA_n39A-n41A | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n39A-n41C | CA_n8A-n39ACA_n8A-n41ACA_n39A-n41A | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
| CA_n8A-n39A-n79A | CA_n8A-n39ACA_n8A-n79ACA_n39A-n79A | n8 | 5, 10, 15, 20 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n40A-n41A | CA_n8A-n40ACA_n8A-n41ACA_n40A-n41A | n8 | 5, 10, 15, 20 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n40A-n41C | CA_n41CCA_n8A-n40ACA_n8A-n41ACA_n40A-n41A | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | CA_n41C_BCS4 and 5 |  |
| CA_n8A-n40A-n78A | CA_n8A-n40ACA_n8A-n78ACA_n40A-n78A | n8 | 5, 10, 15, 20 | 0 |
|  |  | n40 | 5, 10, 15, 20, 30, 40, 50, 60, 80 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n40A-n77A | CA_n8A-n40ACA_n8A-n77ACA_n40A-n77A | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n40A-n77(2A) | CA_n8A-n40ACA_n8A-n77ACA_n40A-n77A | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n8A-n40A-n79A | CA_n8A-n40ACA_n8A-n79ACA_n40A-n79A | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n41A-n78A | CA_n8A-n41ACA_n8A-n78ACA_n41A-n78A | n8 | 5, 10, 15, 20 | 4 and 5 |
|  |  | n41 | 5,10,15,20,25,30,35,40,45,50,60,70,80,90,100 |  |
|  |  | n78 | 10,15,20,25,30,40,50,60,70,80,90,100 |  |
| CA_n8A-n41A-n78C | CA_n78CCA_n8A-n41ACA_n8A-n78ACA_n8A-n78CCA_n41A-n78ACA_n41A-n78C | n8 | 5, 10, 15, 20 | 4 and 5 |
|  |  | n41 | 5,10,15,20,25,30,35,40,45,50,60,70,80,90,100 |  |
|  |  | n78 | CA_n78C_BCS 4 and 5 |  |
| CA_n8A-n41A-n79A | CA_n8A-n41ACA_n8A-n79ACA_n41A-n79A | n8 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n8 | 5, 10, 15, 20 | 1 |
|  |  | n41 | 10, 15, 20, 40, 50, 60 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n41C-n79A | CA_n41CCA_n8A-n41ACA_n8A-n79ACA_n41A-n79A | n8 | See n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n78A-n79A | - | n8 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  | CA_n8A-n78A CA_n8A-n79ACA_n78A-n79A | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n78(2A)-n79A | - | n8 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS1 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n12A-n25A-n41A | - | n12 | 5, 10, 15 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n12 | See n12 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | See n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n12A-n25A-n66A | - | n12 | 5, 10, 15 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n12 | See n12 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | See n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | See n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n12A-n30A-n66A | CA_n12A-n30ACA_n12A-n66ACA_n30A-n66A | n12 | 5, 10, 15 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n12A-n30A-n66(2A) | CA_n12A-n30ACA_n12A-n66ACA_n30A-n66A | n12 | 5, 10, 15 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n12A-n30A-n66(3A) | CA_n12A-n30ACA_n12A-n66ACA_n30A-n66A | n12 | 5, 10, 15 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
| CA_n12A-n30A-n77A | n777,9CA_n12A-n30A,CA_n12A-n77A7CA_n30A-n77A7 | n12 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n12A-n30A-n77(2A) | n777,9CA_n12A-n30ACA_n12A-n77A7CA_n30A-n77A7 | n12 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n12A-n41A-n66A | - | n12 | 5, 10, 15 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n12 | See n12 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | See n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n12A-n41A-n77A | - | n12 | 5, 10, 15 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n12 | See n12 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n12A-n66A-n77A | n777,9CA_n12A-n66ACA_n12A-n77A7CA_n66A-n77A7 | n12 | 5, 10, 15 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n12A-n66(2A)-n77A | n777,9CA_n12A-n66ACA_n12A-n77A7CA_n66A-n77A7 | n12 | 5, 10, 15 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n12A-n66A-n77(2A) | n777,9CA_n12A-n66ACA_n12A-n77A7CA_n66A-n77A7 | n12 | 5, 10, 15 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n12A-n66(2A)-n77(2A) | n777,9CA_n12A-n66ACA_n12A-n77A7CA_n66A-n77A7 | n12 | 5, 10, 15 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n12A-n66(3A)-n77A | n777,9CA_n12A-n66ACA_n12A-n77A7CA_n66A-n77A7 | n12 | 5, 10, 15 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n12A-n66(3A)-n77(2A) | n777,9CA_n12A-n66ACA_n12A-n77A7CA_n66A-n77A7 | n12 | 5, 10, 15 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n12A-n71A-n77A | CA_n12A-n77ACA_n71A-n77A | n12 | 5, 10, 15 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n13A-n25A-n66A | CA_n13A-n25ACA_n13A-n66ACA_n25A-n66A | n13 | 5, 10 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n13A-n25A-n77A | n777,9CA_n13A-n25ACA_n13A-n77A7CA_n25A-n77A7 | n13 | 5, 10 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n13A-n25A-n77(2A) | n777,9CA_n77(2A)7CA_n13A-n25ACA_n13A-n77A7CA_n25A-n77A7 | n13 | 5, 10 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n13A-n66A-n77A | n777, 9CA_n13A-n66ACA_n13A-n77A7CA_n66A-n77A7 | n13 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n13A-n66A-n77(2A) | n777,9CA_n77(2A)7CA_n13A-n66ACA_n13A-n77A7CA_n66A-n77A7 | n13 | 5, 10 | 0 |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n14A-n30A-n66A | CA_n14A-n30ACA_n14A-n66ACA_n30A-n66A | n14 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n14A-n30A-n66(2A) | CA_n14A-n30ACA_n14A-n66ACA_n30A-n66A | n14 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n14A-n30A-n66(3A) | CA_n14A-n30ACA_n14A-n66ACA_n30A-n66A | n14 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
| CA_n14A-n30A-n77A | n777,9CA_n14A-n30ACA_n14A-n77A7CA_n30A-n77A7 | n14 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n14A-n30A-n77(2A) | n777,9CA_n14A-n30ACA_n14A-n77A7CA_n30A-n77A7 | n14 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n14A-n66A-n77A | n777,9CA_n14A-n66ACA_n14A-n77A7CA_n66A-n77A7 | n14 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n14A-n66(2A)-n77A | n777,9CA_n14A-n66ACA_n14A-n77A7CA_n66A-n77A7 | n14 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n14A-n66A-n77(2A) | n777,9CA_n14A-n66ACA_n14A-n77A7CA_n66A-n77A7 | n14 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n14A-n66(2A)-n77(2A) | n777,9CA_n14A-n66ACA_n14A-n77A7CA_n66A-n77A7 | n14 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n14A-n66(3A)-n77A | n777,9CA_n14A-n66ACA_n14A-n77A7CA_n66A-n77A7 | n14 | 5, 10 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n14A-n66(3A)-n77(2A) | n777,9CA_n14A-n66ACA_n14A-n77A7CA_n66A-n77A7 | n14 | 5, 10 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n18A-n28A-n41A | n417,9CA_n18A-n28ACA_n18A-n41A7,9CA_n28A-n41A7,9 | n18 | 5, 10, 15 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  | n417,9CA_n18A-n28ACA_n18A-n41A7,9CA_n28A-n41A7,9 | n18 | n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n18A-n28A-n77A | n777,9CA_n18A-n28ACA_n18A-n77A7,9CA_n28A-n77A7,9 | n18 | 5, 10, 15 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n18A-n28A-n77(2A) | n777,9CA_n18A-n28ACA_n18A-n77A7CA_n28A-n77A7 | n18 | 5, 10, 15 | 0 |
|  | CA_n77(2A) | n28 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n18A-n28A-n77(3A) | n777,9CA_n18A-n28ACA_n18A-n77A7CA_n28A-n77A7 | n18 | 5, 10, 15 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
| CA_n18A-n40A-n77A | n407,9n777,9CA_n18A-n40A7,9CA_n18A-n77A7,9CA_n40A-n77A7,9 | n18 | n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n18A-n41A-n77A | n417,9n777,9CA_n18A-n41A7CA_n18A-n77A7,9CA_n41A-n77A7,9 | n18 | 5, 10, 15 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n18A-n41A-n77(2A) | n417,9n777,9CA_n18A-n41A7,9CA_n18A-n77A7,9CA_n41A-n77A7,9CA_n77(2A)7 | n18 | 5, 10, 15 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n18A-n41A-n77(3A) | n417,9n777,9CA_n18A-n41A7CA_n18A-n77A7CA_n41A-n77A7 | n18 | 5, 10, 15 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
| CA_n20A-n28A-n75A | CA_n20A-n28A | n20 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n75 | 5, 10, 15, 20 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n20A-n28A-n78A17 | - | n20 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  | CA_n20A-n28ACA_n20A-n78ACA_n28A-n78A | n20 | n20 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n20A-n28A-n78C | - | n20 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n20A-n41A-n71A | CA_n20A-n41ACA_n20A-n71ACA_n41A-n71A | n20 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n20A-n41A-n77A | CA_n20A-n41ACA_n20A-n77ACA_n41A-n77A | n20 | 5,10,15,20 | 0 |
|  |  | n41 | 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n20A-n41A-n77(2A) | CA_n20A-n41ACA_n20A-n77ACA_n41A-n77A | n20 | 5,10,15,20 | 0 |
|  |  | n41 | 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n20A-n41A-n78A | CA_n20A-n41ACA_n20A-n78ACA_n41A-n78A | n20 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n20A-n67A-n78A | CA_n20A-n78A | n20 | See n20 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n67 | See n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | See n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n20A-n71A-n78A | CA_n20A-n71ACA_n20A-n78ACA_n71A-n78A | n20 | 5, 10, 15, 20 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n20A-n67A-n78(2A) | CA_n20A-n78ACA_n78(2A) | n20 | See n20 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n67 | See n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n20A-n75A-n78A | CA_n20A-n78A | n20 | n20 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n20A-n75A-n78(2A) | CA_n78(2A)CA_n20A-n78A | n20 | n20 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n24A-n41A-n48A | CA_n24A-n41ACA_n24A-n48ACA_n41A-n48A | n24 | 5, 10 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n48 | 5, 10, 15, 20, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
| CA_n24A-n41(2A)-n48A | CA_n24A-n41ACA_n24A-n48ACA_n41A-n48A | n24 | 5, 10 | 0 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n48 | 5, 10, 15, 20, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
| CA_n24A-n41A-n48(2A) | CA_n24A-n41ACA_n24A-n48ACA_n41A-n48A | n24 | 5, 10 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
| CA_n24A-n41(2A)-n48(2A) | CA_n24A-n41ACA_n24A-n48ACA_n41A-n48A | n24 | 5, 10 | 0 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
| CA_n24A-n41A-n77A | CA_n24A-n41ACA_n24A-n77ACA_n41A-n77A | n24 | 5, 10 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n24 | See n24 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n24A-n41(2A)-n77A | CA_n24A-n41ACA_n24A-n77ACA_n41A-n77A | n24 | 5, 10 | 0 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n24 | 5, 10 | 1 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n24 | See n24 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS4 and 5 |  |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n24A-n41A-n77(2A) | CA_n24A-n41ACA_n24A-n77ACA_n41A-n77A | n24 | 5, 10 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n24 | 5, 10 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n24 | See n24 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n24A-n41(2A)-n77(2A) | CA_n24A-n41ACA_n24A-n77ACA_n41A-n77A | n24 | 5, 10 | 0 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n24 | 5, 10 | 1 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n24 | See n24 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n24A-n48A-n77A | - | n24 | 5, 10 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 5012, 6012, 8012, 9012, 10012 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n24A-n48(2A)-n77A | - | n24 | 5, 10 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n24A-n48A-n77(2A) | - | n24 | 5, 10 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n24A-n48(2A)-n77(2A) | - | n24 | 5, 10 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n25A-n29A-n66A | CA_n25A-n66A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n29A-n77A | CA_n25A-n77A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n29A-n77(2A) | CA_n25A-n77ACA_n77(2A) | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n25A-n29A-n77(3A) | CA_n25A-n77ACA_n77(2A) | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n25A-n38A-n66A | CA_n25A-n38ACA_n25A-n66ACA_n38A-n66A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n25(2A)-n38A-n66A | CA_n25A-n38ACA_n25A-n66ACA_n38A-n66A | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n25(2A)-n38A-n66(2A) | CA_n25A-n38ACA_n25A-n66ACA_n38A-n66A | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n25A-n38A-n66(2A) | CA_n25A-n38ACA_n25A-n66ACA_n38A-n66A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n38 | 5, 10, 15, 20 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n25A-n38A-n78A | CA_n25A-n38ACA_n25A-n78ACA_n38A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25A-n38A-n78(2A) | CA_n25A-n38ACA_n25A-n78ACA_n38A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25(2A)-n38A-n78A | CA_n25A-n38ACA_n25A-n78ACA_n38A-n78A | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25(2A)-n38A-n78(2A) | CA_n25A-n38ACA_n25A-n78ACA_n38A-n78A | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25A-n41A-n66A | n257n417,9n667CA_n25A-n41A7,9,13,14CA_n25A-n66A7,13CA_n41A-n66A7,9,13,14 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n66(2A) | n257n417,9n667CA_n25A-n41A7,13,14CA_n25A-n66A7CA_n41A-n66A7,13,14 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n25A-n41C-n66A | n257n417,9n667CA_n25A-n41A7,9CA_n25A-n66A7CA_n41A-n66A7,9CA_n41C7,9CA_n25A-n41C7,9CA_n41C-n66A7,9 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | CA_n41C_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | CA_n41C_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(2A)-n66A | n257n417,9n667CA_n25A-n41A7,9CA_n25A-n66A7CA_n41A-n66A7,9 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(2A)-n66(2A) | n257n417,9n667CA_n25A-n41A7CA_n25A-n66A7CA_n41A-n66A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n25A-n41(3A)-n66(2A) | n257n417,9n667CA_n25A-n41A7CA_n25A-n66A7CA_n41A-n66A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n25A-n41(3A)-n66A | n257n417,9n667CA_n25A-n41A7CA_n25A-n66A7CA_n41A-n66A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41C-n66(2A) | n257n417,9n667CA_n25A-n41A7CA_n25A-n41CCA_n25A-n66A7CA_n41A-n66A7CA_n41C-n66ACA_n41C7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n25A-n41(A-C)-n66A | n257n417,9n667CA_n25A-n41A7CA_n25A-n41CCA_n25A-n66A7CA_n41A-n66A7CA_n41C7CA_n41C-n66A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(A-C)-n66(2A) | n257n417,9n667CA_n25A-n41A7CA_n25A-n41CCA_n25A-n66A7CA_n41A-n66A7CA_n41C7CA_n41C-n66A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41A-n66A | n257n417,9n667CA_n25A-n41A7,13,14CA_n25A-n66A7CA_n41A-n66A7,13,14 | n25 | CA_n25(2A)_BCS1 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n25 | CA_n25(2A)_BCS1 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 30, 40 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A-n66(2A) | n257n417,9n667CA_n25A-n41A7CA_n25A-n66A7CA_n41A-n66A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41(2A)-n66A | n257n417,9n667CA_n25A-n41A7CA_n25A-n66A7CA_n41A-n66A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41(3A)-n66A | n257n417,9n667CA_n25A-n41A7CA_n25A-n66A7CA_n41A-n66A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41(2A)-n66(2A) | n257n417,9n667CA_n25A-n41A7CA_n25A-n66A7CA_n41A-n66A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41C-n66A | n257n417,9n667CA_n25A-n41A7CA_n25A-n41CCA_n25A-n66A7CA_n41A-n66A7CA_n41C-n66ACA_n41C7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41C-n66(2A) | n257n417,9n667CA_n25A-n41A7CA_n25A-n41CCA_n25A-n66A7CA_n41A-n66A7CA_n41C7CA_n41C-n66A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41(A-C)-n66A | n257n417,9n667CA_n25A-n41A7CA_n25A-n41CCA_n25A-n66A7CA_n41A-n66A7CA_n41C7CA_n41C-n66A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n71A | n257n417,9n717CA_n25A-n41A7,9,13,14CA_n25A-n71A7,13CA_n41A-n71A7,9,13,14 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n71B | n257n417,9n717CA_n25A-n41A7,13,14CA_n25A-n71A7CA_n41A-n71A7,13,14 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | CA_n71B_BCS2 |  |
|  |  | n25 | 5, 10, 15, 20, 30, 40 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | CA_n71B_BCS2 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25A-n41A-n71(2A) | n257n417,9n717CA_n25A-n41A7,13,14CA_n25A-n71A7CA_n41A-n71A7,13,14 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n25 | 5, 10, 15, 20, 30, 40 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25A-n41(2A)-n71A | n257n417,9n717CA_n25A-n41A7,9CA_n25A-n71A7CA_n41A-n71A7,9 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(2A)-n71B | n257n417,9n717CA_n25A-n41A7CA_n25A-n71A7CA_n41A-n71A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25A-n41(2A)-n71(2A) | n257n417,9n717CA_n25A-n41A7CA_n25A-n71A7CA_n41A-n71A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25A-n41(3A)-n71A | n257n417,9n717CA_n25A-n41A7CA_n25A-n71A7CA_n41A-n71A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(3A)-n71B | n257n417,9n717CA_n25A-n41A7CA_n25A-n71A7CA_n41A-n71A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25A-n41(3A)-n71(2A) | n257n417,9n717CA_n25A-n41A7CA_n25A-n71A7CA_n41A-n71A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25A-n41C-n71A | n257n417,9n717CA_n25A-n41A7,9CA_n25A-n71A7CA_n41A-n71A7,9CA_n41C7,9CA_n25A-n41C7,9CA_n41C-n71A7,9 | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | CA_n41C_BCS0 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | CA_n41C_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41C-n71B | n257n417,9n717CA_n25A-n41A7CA_n25A-n41CCA_n25A-n71A7CA_n41A-n71A7CA_n41C-n71ACA_n41C7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25A-n41C-n71(2A) | n257n417,9n717CA_n25A-n41A7CA_n25A-n41CCA_n25A-n71A7CA_n41A-n71A7CA_n41C-n71ACA_n41C7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25A-n41(A-C)-n71A | n257n417,9n717CA_n25A-n41A7CA_n25A-n41CCA_n25A-n71A7CA_n41A-n71A7CA_n41C7CA_n41C-n71A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(A-C)-n71B | n257n417,9n717CA_n25A-n41A7CA_n25A-n41CCA_n25A-n71A7CA_n41A-n71A7CA_n41C7CA_n41C-n71A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25A-n41(A-C)-n71(2A) | n257n417,9n717CA_n25A-n41A7CA_n25A-n71A7CA_n25A-n41CCA_n41A-n71A7CA_n41C7CA_n41C-n71A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41A-n71A | n257n417,9n717CA_n25A-n41A7,13,14CA_n25A-n71A7CA_n41A-n71A7,13,14 | n25 | CA_n25(2A)_BCS1 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | CA_n25(2A)_BCS1 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A-n71B | n257n417,9n717CA_n25A-n41A7CA_n25A-n71A7CA_n41A-n71A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25(2A)-n41A-n71(2A) | n257n417,9n717CA_n25A-n41A7CA_n25A-n71A7CA_n41A-n71A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41(2A)-n71A | n257n417,9n717CA_n25A-n41A7CA_n25A-n71A7CA_n41A-n71A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41(2A)-n71(2A) | n257n417,9n717CA_n25A-n41A7CA_n25A-n71A7CA_n41A-n71A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41(2A)-n71B | n257n417,9n717CA_n25A-n41A7CA_n25A-n71A7CA_n41A-n71A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25(2A)-n41(3A)-n71A | n257n417,9n717CA_n25A-n41A7CA_n25A-n71A7CA_n41A-n71A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41C-n71A | n257n417,9n717CA_n25A-n41A7CA_n25A-n41CCA_n25A-n71A7CA_n41A-n71A7CA_n41C-n71ACA_n41C7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41C-n71(2A) | n257n417,9n717CA_n25A-n41A7CA_n25A-n41CCA_n25A-n71A7CA_n41A-n71A7CA_n41C7CA_n41C-n71A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41C-n71B | n257n417,9n717CA_n25A-n41A7CA_n25A-n41CCA_n25A-n71A7CA_n41A-n71A7CA_n41C7CA_n41C-n71A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25(2A)-n41(A-C)-n71A | n257n417,9n717CA_n25A-n41A7CA_n25A-n41CCA_n25A-n71A7CA_n41A-n71A7CA_n41C7CA_n41C-n71A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n77A | n257n417,9n777,9CA_n25A-n41A7,9,13,14CA_n25A-n77A7,9,13,14CA_n41A-n77A7,9,13,14 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(2A)-n77A | n257n417,9n777,9CA_n25A-n41A7CA_n25A-n77A7CA_n41A-n77A7,9 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(3A)-n77A | n257n417,9n777,9CA_n25A-n41A7CA_n25A-n77A7CA_n41A-n77A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n77(2A) | n257n417,9n777,9CA_n25A-n41A7CA_n25A-n77A7CA_n41A-n77A7 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n41(2A)-n77(2A) | n417,9n777,9CA_n25A-n41A7CA_n25A-n77A7CA_n41A-n77A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41A-n77A | n257n417,9n777,9CA_n25A-n41A7,9CA_n25A-n77A7,9CA_n41A-n77A7,9 | n25 | CA_n25(2A)_BCS1 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A-n77(2A) | n417,9n777,9CA_n25A-n41A7CA_n25A-n77A7CA_n41A-n77A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41C-n77A | n257n417,9n777,9CA_n25A-n41A7CA_n25A-n41CCA_n25A-n77A7CA_n41A-n77A7CA_n41C7CA_n41C-n77A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41(2A)-n77A | n257n417,9n777,9CA_n25A-n41A7CA_n25A-n77A7CA_n41A-n77A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41C-n77A | n257n417,9n777,9CA_n25A-n41A7CA_n25A-n77A7CA_n41A-n77A7,9CA_n41C7,9CA_n25A-n41C7CA_n41C-n77A7,9 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | CA_n41C_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | CA_n41C_BCS2 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(A-C)-n77A | n257n417,9n777,9CA_n25A-n41A7CA_n25A-n41CCA_n25A-n77A7CA_n41A-n77A7CA_n41C-n77ACA_n41C7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41C-n77(2A) | n417,9n777.9CA_n25A-n41A7CA_n25A-n77A7CA_n41A-n77A7CA_n41C7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41C-n77(2A) | CA_n25A-n41A CA_n25A-n77ACA_n41A-n77A CA_n41C | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41(2A)-n77(2A) | CA_n25A-n41A CA_n25A-n77A CA_n41A-n77A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41(3A)-n77A | n417,9n777,9CA_n25A-n41A7CA_n25A-n77A7CA_n41A-n77A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41(A-C)-n77A | n417,9n777,9CA_n25A-n41A7CA_n25A-n41CCA_n25A-n77A7CA_n41A-n77A7CA_n41C7CA_n41C-n77A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n78A | CA_n25A-n41ACA_n25A-n78ACA_n41A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25A-n41A-n78(2A) | CA_n25A-n41ACA_n25A-n78ACA_n41A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25A-n41A-n85A | CA_n25A-n41ACA_n25A-n85ACA_n41A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41C-n85A | CA_n25A-n41ACA_n25A-n85ACA_n41A-n85ACA_n41C | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(2A)-n85A | CA_n25A-n41ACA_n25A-n85ACA_n41A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A-n85A | CA_n25A-n41ACA_n25A-n85ACA_n41A-n85A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n48A-n66A | CA_n25A-n48ACA_n25A-n66ACA_n48A-n66A | n25 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 5012 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n48 | 5, 10, 15, 20, 40, 5012, 6012, 8012, 9012, 10012 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n25A-n48(2A)-n66A | CA_n25A-n48ACA_n25A-n66ACA_n48A-n66A | n25 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n25A-n48C-n66A | CA_n25A-n48ACA_n25A-n66ACA_n48A-n66A | n25 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n25A-n66A-n71A | - | n25 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | n257n667n717CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66A-n71B | n257n667n717CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | CA_n71B_BCS2 |  |
|  | n257n667n717CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25A-n66A-n71(2A) | n257n667n717CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  | n257n667n717CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25A-n66(2A)-n71A | n257n667n717CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | n257n667n717CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66(2A)-n71B | n257n667n717CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25A-n66(2A)-n71(2A) | n257n667n717CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n66A-n71A | n257n667n717CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | CA_n25(2A)_BCS1 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n66(2A)-n71A | n257n667n717CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n66A-n71B | n257n667n717CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25(2A)-n66(2A)-n71B | CA_n25A-n66A CA_n25A-n71A CA_n66A-n71A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25(2A)-n66A-n71(2A) | n257n667n717CA_n25A-n66A7CA_n25A-n71A7CA_n66A-n71A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n66(2A)-n71(2A) | CA_n25A-n66A CA_n25A-n71A CA_n66A-n71A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25(3A)-n66A-n71A | n257n667n717CA_n25A-n66A7 CA_n25A-n71A7 CA_n66A-n71A7 | n25 | CA_n25(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(3A)-n66(2A)-n71A | CA_n25A-n66ACA_n25A-n71ACA_n66A-n71A | n25 | CA_n25(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(3A)-n66A-n71B | CA_n25A-n66ACA_n25A-n71ACA_n66A-n71A | n25 | CA_n25(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25(3A)-n66A-n71(2A) | CA_n25A-n66ACA_n25A-n71ACA_n66A-n71A | n25 | CA_n25(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25A-n66A-n77A | n257n667n777,9CA_n25A-n66A7,13CA_n25A-n77A7,9,13,14CA_n66A-n77A7,9,13,14 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66(2A)-n77A | n257n667n777,9CA_n25A-n66A7CA_n25A-n77A7,13,14CA_n66A-n77A7,13,14 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66A-n77(2A) | n257n667n777,9CA_n77(2A)7CA_n25A-n66A7CA_n25A-n77A7CA_n66A-n77A7 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n66A-n77(3A) | n777,9CA_n77(2A)7CA_n25A-n66ACA_n25A-n77A7CA_n66A-n77A7 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS 4 and 5 |  |
| CA_n25A-n66(2A)-n77(2A) | n777,9CA_n25A-n66ACA_n25A-n77A7CA_n66A-n77A7 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n66A-n77A | n257n667n777,9CA_n25A-n66A7CA_n25A-n77A7,13,14CA_n66A-n77A7,13,14 | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n66(2A)-n77A | n257n667n777,9CA_n25A-n66A7CA_n25A-n77A7CA_n66A-n77A7 | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n66A-n77(2A) | n777,9CA_n25A-n66ACA_n25A-n77A7CA_n66A-n77A7 | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n66(2A)-n77(2A) | n777,9CA_n25A-n66ACA_n25A-n77A7CA_n66A-n77A7 | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n66A-n78A | n787,9CA_n25A-n66ACA_n25A-n78A7CA_n66A-n78A7 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25(2A)-n66A-n78A | n787,9CA_n25A-n66A CA_n25A-n78A7 CA_n66A-n78A7 | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25A-n66(2A)-n78A | CA_n25A-n66A CA_n25A-n78A CA_n66A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25A-n66A-n78(2A) | n787CA_n25A-n66A CA_n25A-n78A7 CA_n66A-n78A7CA_n78(2A)7 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25(2A)-n66(2A)-n78A | CA_n25A-n66A CA_n25A-n78A CA_n66A-n78A | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25(2A)-n66A-n78(2A) | CA_n25A-n66A CA_n25A-n78A CA_n66A-n78A | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25A-n66(2A)-n78(2A) | CA_n25A-n66A CA_n25A-n78A CA_n66A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25(2A)-n66(2A)-n78(2A) | CA_n25A-n66A CA_n25A-n78A CA_n66A-n78A | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25A-n66A-n85A | CA_n25A-n66ACA_n25A-n85ACA_n66A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66(2A)-n85A | CA_n25A-n66A CA_n25A-n85A CA_n66A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n66A-n85A | CA_n25A-n66A CA_n25A-n85A CA_n66A-n85A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n71A-n77A | n257n717n777,9CA_n25A-n71A7,13CA_n25A-n77A7,9,13,14CA_n71A-n77A7,9,13,14 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n71A-n77(2A) | n257n717n777,9CA_n77(2A)7CA_n25A-n71A7CA_n25A-n77A7CA_n71A-n77A7 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n71A-n77(3A) | n777,9CA_n77(2A)7CA_n25A-n71ACA_n25A-n77A7CA_n71A-n77A7 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  | CA_n77(2A)CA_n25A-n71ACA_n25A-n77ACA_n71A-n77A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n25A-n71B-n77A | n257n717n777,9CA_n25A-n71A7CA_n25A-n77A7,13,14CA_n71A-n77A7,13,14 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | CA_n71B_BCS2 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n71B-n77(2A) | n777,9CA_n25A-n71ACA_n25A-n77A7CA_n71A-n77A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n71(2A)-n77A | n257n717n777,9CA_n25A-n71A7CA_n25A-n77A7,13,14CA_n71A-n77A7,13,14 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n71(2A)-n77(2A) | n777,9CA_n25A-n71ACA_n25A-n77A7CA_n71A-n77A7 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n71A-n77A | n257n717n777,9CA_n25A-n71A7CA_n25A-n77A7,13,14CA_n71A-n77A7,13,14 | n25 | CA_n25(2A)_BCS1 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n71A-n77(2A) | n777,9CA_n25A-n71ACA_n25A-n77A7CA_n71A-n77A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n71B-n77A | n257n717n777,9CA_n25A-n71A7CA_n25A-n77A7CA_n71A-n77A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n71B-n77(2A) | n777,9CA_n25A-n71ACA_n25A-n77A7CA_n71A-n77A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n71(2A)-n77A | n257n717n777,9CA_n25A-n71A7CA_n25A-n77A7CA_n71A-n77A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n71(2A)-n77(2A) | n777,9CA_n25A-n71ACA_n25A-n77A7CA_n71A-n77A7 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n71A-n78A | CA_n25A-n71ACA_n25A-n78ACA_n71A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25A-n71A-n78(2A) | CA_n25A-n71ACA_n25A-n78ACA_n71A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25A-n71A-n85A | CA_n25A-n71ACA_n25A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n71B-n85A | CA_n25A-n71A CA_n25A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n71(2A)-n85A | CA_n25A-n71A CA_n25A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n71A-n85A | CA_n25A-n71A CA_n25A-n85A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n77A-n85A | CA_n25A-n77ACA_n25A-n85ACA_n77A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n77(2A)-n85A | CA_n25A-n77ACA_n25A-n85ACA_n77A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n77A-n85A | CA_n25A-n77ACA_n25A-n85ACA_n77A-n85A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n26A-n29A-n66A | CA_n26A-n66A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n26A-n29A-n66(2A) | CA_n26A-n66A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n26A-n29A-n66(3A) | - | n26 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
| CA_n26A-n29A-n70A | CA_n26A-n70A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
| CA_n26A-n48A-n66A | CA_n26A-n48ACA_n26A-n66ACA_n48A-n66A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 5012, 6012, 8012, 9012, 10012 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n26A-n48(2A)-n66A | CA_n26A-n48ACA_n26A-n66ACA_n48A-n66A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n26A-n48A-n66(2A) | CA_n26A-n48ACA_n26A-n66ACA_n48A-n66A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 5012, 6012, 8012, 9012, 10012 |  |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
| CA_n26A-n48(2A)-n66(2A) | CA_n26A-n48ACA_n26A-n66ACA_n48A-n66A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
| CA_n26A-n48A-n70A | CA_n26A-n48ACA_n26A-n70ACA_n48A-n70A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 40, 5012, 6012, 8012, 9012, 10012 |  |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
| CA_n26A-n66A-n70A | CA_n26A-n66ACA_n26A-n70A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n26A-n66(2A)-n70A | CA_n26A-n66ACA_n26A-n70A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n26A-n66(3A)-n70A | - | n26 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n26A-n66A-n71A | CA_n26A-n66ACA_n66A-n71A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n26A-n66(2A)-n71A | CA_n26A-n66ACA_n66A-n71A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n26A-n66(3A)-n71A | CA_n66A-n71A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n26A-n66A-n77A | CA_n26A-n66ACA_n26A-n77ACA_n66A-n77A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40 |  |
| CA_n26A-n70A-n71A | CA_n26A-n70ACA_n70A-n71A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n26A-n70A-n77A | CA_n26A-n70ACA_n26A-n77ACA_n70A-n77A | n26 | 5, 10, 15, 20 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40 |  |
| CA_n28A-n38A-n78A | - | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n28A-n39A-n40A | CA_n28A-n39ACA_n28A-n40ACA_n39A-n40A | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 100 |  |
| CA_n28A-n39A-n41A | CA_n28A-n39ACA_n28A-n41ACA_n39A-n41A | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n39 | n39 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n39A-n41C | CA_n28A-n39ACA_n28A-n41ACA_n39A-n41A | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n41 | CA_n41C_BCS1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n39 | n39 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
| CA_n28A-n39A-n79A | CA_n28A-n39ACA_n28A-n79ACA_n39A-n79A | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n28A-n40A-n41A | CA_n28A-n40ACA_n28A-n41ACA_n40A-n41A | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n40A-n41C | CA_n28A-n40ACA_n28A-n41ACA_n40A-n41A | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n41 | CA_n41C_BCS0 |  |
| CA_n28A-n40A-n71A | CA_n40A-n71ACA_n28A-n40A | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n40A-n75A | - | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n40A-n78A | CA_n28A-n40ACA_n28A-n78ACA_n40A-n78A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  | CA_n28A-n40ACA_n28A-n78ACA_n40A-n78A | n28 | 5, 10, 15, 20 | 1 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 100 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n40A-n77A | CA_n28A-n40ACA_n28A-n77ACA_n40A-n77A | n28 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n28A-n40A-n77(2A) | CA_n28A-n40ACA_n28A-n77ACA_n40A-n77A | n28 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n28A-n40B-n78A | CA_n28A-n40ACA_n28A-n78ACA_n40A-n78A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n40 | CA_n40B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | CA_n40B_BCS4 and 5 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n40A-n79A | CA_n28A-n40ACA_n28A-n79ACA_n40A-n79A | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n41A-n74A | n417CA_n28A-n41A7CA_n28A-n74ACA_n41A-n74A7 | n28 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n74 | 5, 10, 15, 20 |  |
|  | - | n28 | 5, 10, 15, 20, 30 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n74 | 5, 10, 15, 20 |  |
| CA_n28A-n41A-n75A | - | n28 | 5,10, 15, 20, 25,30 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n75 | 5,10, 15, 20, 25,30,40,50 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n41A-n77A | n417,9n777,9CA_n28A-n41A7,9 | n28 | 5, 10, 15, 20, 30 | 0 |
|  | CA_n28A-n77A7,9 | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  | CA_n41A-n77A7,9 | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n41B-n77A | CA_n28A-n41ACA_n28A-n77ACA_n41A-n77A | n28 | 5, 10 | 0 |
|  |  | n41 | CA_n41B_BCS0 |  |
|  |  | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n28A-n41B-n77(2A) | CA_n28A-n41ACA_n28A-n77ACA_n41A-n77A | n28 | 5, 10 | 0 |
|  |  | n41 | CA_n41B_BCS0 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n28A-n41A-n77(2A) | n417,9n777,9CA_n28A-n41A7 | n28 | 5, 10, 15, 20, 30 | 0 |
|  | CA_n28A-n77A7 | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  | CA_n41A-n77A7CA_n77(2A)7 | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n28A-n41A-n77(3A) | n417,9n777,9CA_n28A-n41A7,9CA_n28A-n77A7,9CA_n41A-n77A7,9CA_n77(2A)7,9 | n28 | 5, 10 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
| CA_n28A-n41A-n78A | CA_n28A-n41ACA_n41A-n78ACA_n28A-n78A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  | - | n28 | 5,10, 15, 20, 25,30 | 1 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
| CA_n28A-n41A-n78(2A) | CA_n78(2A)CA_n28A-n41ACA_n28A-n78ACA_n41A-n78A | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n28A-n41A-n79A | n28n417, 9n797, 9CA_n28A-n41A7CA_n28A-n79A7CA_n41A-n79A7 | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n41A-n79C | CA_n79CCA_n28A-n41ACA_n28A-n79ACA_n28A-n79CCA_n41A-n79ACA_n41A-n79C | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | CA_n79C_BCS 4 and 5 |  |
| CA_n28A-n41C-n79A | CA_n41CCA_n28A-n41ACA_n28A-n79ACA_n41A-n79A | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n41 | CA_n41C_BCS1 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n41C-n79C | CA_n41CCA_n79CCA_n28A-n41ACA_n28A-n79ACA_n28A-n79CCA_n41A-n79A | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n41 | CA_n41C_BCS1 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n79 | CA_n79C_BCS 4 and 5 |  |
| CA_n28A-n46A-n78A | CA_n28A-n46ACA_n28A-n78ACA_n46A-n78A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n46 | 20, 40, 60, 80 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n28A-n46C-n78A | CA_n28A-n46ACA_n28A-n78ACA_n46A-n78A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n46 | CA_n46C_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n28A-n46D-n78A | CA_n28A-n46ACA_n28A-n78ACA_n46A-n78A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n46 | CA_n46D_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n28A-n46(2A)-n78A | CA_n28A-n46ACA_n28A-n78ACA_n46A-n78A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n46 | CA_n46(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n28A-n46(2A)-n78(2A) | CA_n28A-n46ACA_n28A-n78ACA_n46A-n78ACA_n78(2A) | n28 | 5, 10, 15, 20 | 0 |
|  |  | n46 | CA_n46(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n28A-n46A-n78(2A) | CA_n28A-n46ACA_n28A-n78ACA_n46A-n78ACA_n78(2A) | n28 | 5, 10, 15, 20 | 0 |
|  |  | n46 | 20, 40, 60, 80 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n28A-n46C-n78(2A) | CA_n28A-n46ACA_n28A-n78ACA_n46A-n78ACA_n78(2A) | n28 | 5, 10, 15, 20 | 0 |
|  |  | n46 | CA_n46C_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n28A-n46D-n78(2A) | CA_n28A-n46ACA_n28A-n78ACA_n46A-n78ACA_n78(2A) | n28 | 5, 10, 15, 20 | 0 |
|  |  | n46 | CA_n46D_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n28A-n71A-n77A | CA_n28A-n77A7CA_n71A-n77A7 | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n71A-n77(2A) | CA_n28A-n77ACA_n71A-n77A | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n28A-n74A-n77A | n777CA_n28A-n74ACA_n28A-n77A7CA_n74A-n77A7 | n28 | 5, 10, 15, 20, 30 | 0 |
|  |  | n74 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  | - | n28 | 5, 10, 15, 20, 30 | 1 |
|  |  | n74 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n28A-n75A-n78A | - | n28 | 5, 10, 15, 20 | 0 |
|  |  | n75 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n28 | 5,10, 15, 20, 25,30 | 1 |
|  |  | n75 | 5,10, 15, 20, 25,30,40,50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n28A-n78A | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n75A-n78(2A) | CA_n78(2A)CA_n28A-n78A | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A) BCS 4 and 5 |  |
| CA_n28A-n77A-n79A4 | n777,9n797,9CA_n28A-n77A7CA_n28A-n79A7CA_n77A-n79A7 | n28 | 5, 10, 15, 20 | 0 |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  | CA_n28A-n77ACA_n28A-n79ACA_n77A-n79A | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n28A-n77(2A)-n79A4 | n777,9n797,9CA_n77(2A)7CA_n28A-n77A7CA_n28A-n79A7CA_n77A-n79A7 | n28 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  | n777,9n797,9CA_n28A-n77A7CA_n28A-n79A7CA_n77A-n79ACA_n77(2A)7 | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n77(3A)-n79A4 | n777,9n797,9CA_n77(2A)7CA_n28A-n77A7CA_n28A-n79A7CA_n77A-n79A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n78A-n79A | n787,9n797,9CA_n28A-n78A7CA_n28A-n79A7CA_n78A-n79A7 | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  | CA_n28A-n78A7CA_n28A-n79A7CA_n78A-n79A7 | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n78(2A)-n79A | CA_n28A-n78ACA_n28A-n79ACA_n78A-n79A | n28 | See n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n78A-n102A | CA_n28A-n78ACA_n28A-n102ACA_n78A-n102A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n28A-n78A-n102B | CA_n28A-n78ACA_n28A-n102ACA_n28A-n102BCA_n78A-n102ACA_n78A-n102B | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n28A-n78A-n102C | CA_n28A-n78ACA_n28A-n102ACA_n28A-n102CCA_n78A-n102ACA_n78A-n102C | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n28A-n78A-n102D | CA_n28A-n78ACA_n28A-n102ACA_n78A-n102A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n28A-n78A-n102E | CA_n28A-n78ACA_n28A-n102ACA_n78A-n102A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n28A-n78A-n102(2A) | CA_n28A-n78ACA_n28A-n102ACA_n78A-n102A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n28A-n78(2A)-n102A | CA_n28A-n78ACA_n28A-n102ACA_n78A-n102ACA_n78(2A) | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n28A-n78(2A)-n102B | CA_n28A-n78ACA_n28A-n102ACA_n28A-n102BCA_n78A-n102ACA_n78A-n102BCA_n78(2A) | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n28A-n78(2A)-n102C | CA_n28A-n78ACA_n28A-n102ACA_n28A-n102CCA_n78A-n102ACA_n78A-n102CCA_n78(2A) | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n28A-n78(2A)-n102D | CA_n28A-n78ACA_n28A-n102ACA_n78A-n102ACA_n78(2A) | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n28A-n78(2A)-n102E | CA_n28A-n78ACA_n28A-n102ACA_n78A-n102ACA_n78(2A) | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n28A-n78(2A)-n102(2A) | CA_n28A-n78ACA_n28A-n102ACA_n78A-n102ACA_n78(2A) | n28 | 5, 10, 15, 20 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n29A-n30A-n66A | CA_n30A-n66A | n29 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n29A-n30A-n66(2A) | CA_n30A-n66A | n29 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n29A-n30A-n77A | n777,9CA_n30A-n77A7 | n29 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n29A-n30A-n77(2A) | n777,9CA_n30A-n77A7 | n29 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n29A-n66A-n70A | n667n707 | n29 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  | - | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n66B-n70A | n667n707 | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66B_BCS0 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n29A-n66(2A)-n70A | n667n707 | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  | - | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n66(3A)-n70A | n667n707 | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  | - | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(3A)_BCS4 and 5 |  |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n66A-n71A | n667n707CA_n66A-n71A | n29 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | CA_n66A-n71A | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n66(2A)-n71A | n667n717CA_n66A-n71A | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | CA_n66A-n71A | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n66A-n71(2A) | CA_n66A-n71A | n29 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
| CA_n29A-n66(2A)-n71(2A) | CA_n66A-n71A | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
| CA_n29A-n66(3A)-n71A | n667n717CA_n66A-n71A | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | CA_n66A-n71A | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(3A)_BCS4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n66A-n77A | n667n777,9CA_n66A-n77A7 | n29 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n66A-n77A | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n66(2A)-n77A | n667n777,9CA_n66A-n77A7 | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n29A-n66A-n77(2A) | n777,9CA_n66A-n77A7 | n29 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  | CA_n66A-n77ACA_n77(2A) | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n29A-n66A-n77(3A) | CA_n66A-n77ACA_n77(2A) | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n29A-n66(3A)-n77A | n667n777,9CA_n66A-n77A7 | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n29A-n66(2A)-n77(2A) | n777,9CA_n66A-n77A7 | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n29A-n66(3A)-n77(2A) | n777,9CA_n66A-n77A7 | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n29A-n70A-n71A | n707n717CA_n70A-n71A | n29 | 5, 10 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | CA_n70A-n71A | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n70A-n71(2A) | CA_n70A-n71A | n29 | 5, 10 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
| CA_n30A-n66A-n77A | n777,9CA_n30A-n66ACA_n30A-n77A7CA_n66A-n77A7 | n30 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n30 | See n30 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | See n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n30A-n66(2A)-n77A | n777,9CA_n30A-n66A CA_n30A-n77A7 CA_n66A-n77A7 | n30 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n30 | See n30 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | See n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n30A-n66A-n77(2A) | n777,9CA_n30A-n66A CA_n30A-n77A7 CA_n66A-n77A7 | n30 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n30 | See n30 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | See n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n30A-n66(2A)-n77(2A) | n777,9CA_n30A-n66A CA_n30A-n77A7 CA_n66A-n77A7 | n30 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n30 | See n30 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n30A-n66(3A)-n77A | n777,9CA_n30A-n66A CA_n30A-n77A7 CA_n66A-n77A7 | n30 | 5, 10 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n30A-n66(3A)-n77(2A) | n777,9CA_n30A-n66ACA_n30A-n77A7CA_n66A-n77A7 | n30 | 5, 10 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n34A-n39A-n40A | CA_n34A-n39ACA_n34A-n40ACA_n39A-n40A | n34 | 5, 10, 15 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 100 |  |
|  |  | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n34A-n39A-n41A | CA_n34A-n39ACA_n34A-n41ACA_n39A-n41A | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n34A-n39A-n41C | CA_n34A-n39ACA_n34A-n41ACA_n39A-n41A | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
| CA_n34A-n40A-n41A | CA_n34A-n40ACA_n34A-n41ACA_n40A-n41A | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n34A-n40A-n41C | CA_n34A-n40ACA_n34A-n41ACA_n40A-n41A | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
| CA_n34A-n41A-n79A | CA_n34A-n41ACA_n34A-n79ACA_n41A-n79A | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n34A-n41A-n79C | CA_n34A-n41ACA_n34A-n79ACA_n41A-n79A | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | CA_n79C_BCS 4 and 5 |  |
| CA_n34A-n41C-n79A | CA_n34A-n41ACA_n34A-n79ACA_n41A-n79A | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n34A-n41C-n79C | CA_n34A-n41ACA_n34A-n79ACA_n41A-n79A | n34 | See n34 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n79 | CA_n79C_BCS 4 and 5 |  |
| CA_n38A-n66A-n78A | CA_n38A-n66ACA_n38A-n78ACA_n66A-n78A | n38 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n38A-n66A-n78(2A) | CA_n38A-n66ACA_n38A-n78ACA_n66A-n78A | n38 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n38A-n66(2A)-n78A | CA_n38A-n66ACA_n38A-n78ACA_n66A-n78A | n38 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n38A-n66(2A)-n78(2A) | CA_n38A-n66ACA_n38A-n78ACA_n66A-n78A | n38 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n39A-n40A-n41A | CA_n39A-n40ACA_n39A-n41ACA_n40A-n41A | n39 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n39A-n40A-n41C | CA_n39A-n40ACA_n39A-n41ACA_n40A-n41A | n39 | See n39 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
| CA_n39A-n40A-n79A | CA_n39A-n40ACA_n40A-n79ACA_n39A-n79A | n39 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | See n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n39A-n41A-n79A | CA_n39A-n41ACA_n39A-n79ACA_n41A-n79A | n39 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | 10, 15, 20, 40, 50, 60 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n39 | See n39 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n39A-n41A-n79C | CA_n39A-n41ACA_n39A-n79ACA_n41A-n79A | n39 | See n39 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | CA_n79C_BCS 4 and 5 |  |
| CA_n39A-n41C-n79A | CA_n39A-n41ACA_n39A-n79ACA_n41A-n79A | n39 | See n39 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n41A-n75A | - | n40 | See n40  channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | See n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n41A-n77A18 | - | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n407,9n417,9n777,9CA_n40A-n41A7,9CA_n40A-n77A7,9CA_n41A-n77A7,9 | n40 | n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n41B-n77A | - | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 | 0 |
|  |  | n41 | CA_n41B_BCS0 |  |
|  |  | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n417,9n777,9CA_n40A-n41A7,9CA_n40A-n77A7,9CA_n41A-n77A7,9 | n40 | n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41B_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n41A-n79A | CA_n40A-n41ACA_n40A-n79ACA_n41A-n79A | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 100 |  |
|  |  | n79 | , 40, 50, 60, 80, 100 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | 10, 15, 20, 40, 50, 60 |  |
|  |  | n79 | , 40, 50, 60, 80, 100 |  |
|  |  | n40 | See n40  channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | See n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n41C-n79A | CA_n41CCA_n41A-n79ACA_n40A-n41ACA_n40A-n79A | n40 | See n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS4 and 5 |  |
|  |  | n79 | See n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n71A-n77A | CA_n40A-n71ACA_n40A-n77ACA_n71A-n77A | n40 | n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n71A-n77(2A) | CA_n40A-n71ACA_n40A-n77ACA_n71A-n77A | n40 | n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n40A-n78A-n79A | CA_n40A-n78ACA_n40A-n79ACA_n78A-n79A | n40 | n40 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n40A-n78A-n105A | CA_n40A-n78ACA_n40A-n105ACA_n78A-n105A | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n41A-n66A-n70A | CA_n41A-n66ACA_n41A-n70A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n41A-n66A-n71A | n417,9n667n717CA_n41A-n71A7,9,13,14CA_n41A-n66A7,9,13,14CA_n66A-n71A7,13 | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66A-n71B | n417,9n667n717CA_n41A-n66A7,13,14CA_n41A-n71A7,13,14CA_n66A-n71A7 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | CA_n71B_BCS2 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n41A-n66A-n71(2A) | n417,9n667n717CA_n41A-n66A7,13,14CA_n41A-n71A7,13,14CA_n66A-n71A7 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n41A-n66(2A)-n71A | n417,9n667n717CA_n41A-n66A7,13,14CA_n66A-n71A7CA_n41A-n71A7,13,14 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66(2A)-n71B | n417,9n667n717CA_n41A-n66A7CA_n66A-n71A7CA_n41A-n71A7 | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n41A-n66(2A)-n71(2A) | n417,9n667n717CA_n41A-n66A7CA_n66A-n71A7CA_n41A-n71A7 | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n41(2A)-n66A-n71A | n417,9n667n717CA_n41A-n71A7,9CA_n41A-n66A7,9CA_n66A-n71A7 | n41 | CA_n41(2A)_BCS1 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | CA_n41(2A)_BCS1 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n66A-n71B | n417,9n667n717CA_n41A-n66A7CA_n41A-n71A7CA_n66A-n71A7 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n41(2A)-n66A-n71(2A) | n417,9n667n717CA_n41A-n66A7CA_n41A-n71A7CA_n66A-n71A7 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n41(2A)-n66(2A)-n71A | n417,9n667n717CA_n41A-n71A7CA_n41A-n66A7CA_n66A-n71A7 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n66(2A)-n71(2A) | n417,9n667n717CA_n41A-n71A7CA_n41A-n66A7CA_n66A-n71A7 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n41(2A)-n66(2A)-n71B | n417,9n667n717CA_n41A-n71A7CA_n41A-n66A7CA_n66A-n71A7 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n41(3A)-n66A-n71A | n667n717CA_n41A-n71A7CA_n41A-n66A7CA_n66A-n71A7 | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(3A)-n66(2A)-n71A | n417,9n667n717CA_n41A-n71A7CA_n41A-n66A7CA_n66A-n71A7 | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(3A)-n66A-n71B | n417,9n667n717CA_n41A-n71A7CA_n41A-n66A7CA_n66A-n71A7 | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n41(3A)-n66A-n71(2A) | n417,9n667n717CA_n41A-n71A7CA_n41A-n66A7CA_n66A-n71A7 | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n41C-n66A-n71A | n417,9n667n717CA_n41A-n66A7,9CA_n41C-n66A7,9CA_n41A-n71A7,9CA_n41C-n71A7,9CA_n41C7,9CA_n66A-n71A7 | n41 | CA_n41C_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | CA_n41C_BCS1 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n66A-n71B | n417,9n667n717CA_n41A-n66A7CA_n41C-n66ACA_n41A-n71A7CA_n41C-n71ACA_n41C7CA_n66A-n71A7 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n41C-n66A-n71(2A) | n417,9n667n717CA_n41A-n66A7CA_n41C-n66ACA_n41A-n71A7CA_n41C-n71ACA_n41C7CA_n66A-n71A7 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n41C-n66(2A)-n71A | n417,9n667n717CA_n41A-n66A7CA_n41C-n66ACA_n41A-n71A7CA_n41C-n71ACA_n41C7CA_n66A-n71A7 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n66(2A)-n71(2A) | n417,9n667n717CA_n41A-n71A7CA_n41A-n66A7CA_n41C7CA_n41C-n66ACA_n41C-n71ACA_n66A-n71A7 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n41C-n66(2A)-n71B | n417,9n667n717CA_n41A-n71A7CA_n41A-n66A7CA_n41C7CA_n41C-n66ACA_n41C-n71ACA_n66A-n71A7 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n41(A-C)-n66A-n71A | n417,9n667n717CA_n41C7CA_n41A-n71A7CA_n41A-n66A7CA_n41C-n66ACA_n41C-n71ACA_n66A-n71A7 | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(A-C)-n66A-n71B | n417,9n667n717CA_n41A-n66A7 CA_n41A-n71A7 CA_n41C7 CA_n41C-n66ACA_n41C-n71ACA_n66A-n71A7 | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n41(A-C)-n66A-n71(2A) | n417,9n667n717CA_n41A-n71A7CA_n41A-n66A7CA_n41C7CA_n41C-n66ACA_n41C-n71ACA_n66A-n71A7 | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n41(A-C)-n66(2A)-n71A | n417,9n667n717CA_n41A-n71A7CA_n41A-n66A7CA_n41C7CA_n41C-n66ACA_n41C-n71ACA_n66A-n71A7 | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66A-n77A | n417,9n667n777,9CA_n41A-n66A7,9,13,14CA_n41A-n77A7,9,13.14CA_n66A-n77A7,9,13,14 | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66A-n77(2A) | n417,9n667n777,9CA_n41A-n77A7CA_n41A-n66A7CA_n66A-n77A7 | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41A-n66(2A)-n77A | n417,9n667n777,9CA_n41A-n66A7,9CA_n41A-n77A7,9CA_n66A-n77A7,9 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66(2A)-n77(2A) | n417,9n777,9CA_n41A-n66A7CA_n41A-n77A7CA_n66A-n77A7 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41(2A)-n66A-n77A | n417,9n667n777,9CA_n41A-n66A7CA_n41A-n77A7,9CA_n66A-n77A7 | n41 | CA_n41(2A)_BCS1 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n66A-n77(2A) | n417,9n777,9CA_n41A-n66A7CA_n41A-n77A7CA_n66A-n77A7 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41(2A)-n66(2A)-n77A | n417,9n667n777,9CA_n41A-n66A7CA_n41A-n77A7CA_n66A-n77A7 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n66(2A)-n77(2A) | CA_n41A-n66ACA_n41A-n77ACA_n66A-n77A | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41(3A)-n66A-n77A | n417,9n667n777,9CA_n41A-n66A7CA_n41A-n77A7CA_n66A-n77A7 | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(3A)-n66(2A)-n77A | n417,9n777,9CA_n41A-n66A7CA_n41A-n77A7CA_n66A-n77A7 | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n66A-n77A | n417,9n667n777,9CA_n41A-n66A7CA_n41A-n77A7,9CA_n41C7,9CA_n66A-n77A7CA_n41C-n66A7CA_n41C-n77A7,9 | n41 | CA_n41C_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n66A-n77(2A) | n417,9n777,9CA_n41A-n66A7CA_n41A-n77A7CA_n41C7CA_n66A-n77A7 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41C-n66(2A)-n77A | n417,9n667n777,9CA_n41A-n66A7CA_n41A-n77A7CA_n41C7CA_n41C-n66ACA_n41C-n77ACA_n66A-n77A7 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n66(2A)-n77(2A) | CA_n41A-n66ACA_n41A-n77ACA_n41C CA_n66A-n77A | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41(A-C)-n66A-n77A | n417,9n667n777,9CA_n41A-n66A7CA_n41C-n66ACA_n41A-n77A7CA_n41C-n77ACA_n41C7CA_n66A-n77A7 | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(A-C)-n66(2A)-n77A | n417,9n777,9CA_n41A-n66A7CA_n41C-n66ACA_n41A-n77A7CA_n41C-n77ACA_n41C7CA_n66A-n77A7 | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66A-n78A | CA_n41A-n66ACA_n41A-n78ACA_n66A-n78A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n41A-n66A-n78(2A) | CA_n41A-n66ACA_n41A-n78ACA_n66A-n78A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n41A-n66(2A)-n78A | CA_n41A-n66ACA_n41A-n78ACA_n66A-n78A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n41A-n66(2A)-n78(2A) | CA_n41A-n66ACA_n41A-n78ACA_n66A-n78A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n41A-n66A-n85A | CA_n41A-n66ACA_n41A-n85ACA_n66A-n85A | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66(2A)-n85A | CA_n41A-n66ACA_n41A-n85ACA_n66A-n85A | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n66A-n85A | CA_n41A-n66A CA_n41A-n85A CA_n66A-n85A | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n66A-n85A | CA_n41A-n66A CA_n41A-n85A CA_n41C CA_n66A-n85A | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n70A-n78A | CA_n41A-n70ACA_n41A-n78ACA_n70A-n78A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n41A-n71A-n77A | n417,9n717n777,9CA_n41A-n71A7,9,13,14CA_n41A-n77A7,9,13,14CA_n71A-n77A7,9,13,14 | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 1 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n71B-n77A | n417,9n717n777,9CA_n41A-n71A7,9CA_n41A-n77A7,9CA_n71A-n77A7,9 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n71 | CA_n71B_BCS2 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n71B-n77(2A) | n417,9n777,9CA_n41A-n71A7CA_n41A-n77A7CA_n71A-n77A7 | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41A-n71(2A)-n77A | n417,9n717n777,9CA_n41A-n71A7,9CA_n41A-n77A7,9CA_n71A-n77A7,9 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n71A-n77(2A) | n417,9n717n777,9CA_n41A-n71A7CA_n41A-n77A7CA_n71A-n77A7 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41(2A)-n71A-n77A | n417,9n717n777,9CA_n41A-n71A7CA_n41A-n77A7,9CA_n71A-n77A7 | n41 | CA_n41(2A)_BCS1 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n71B-n77A | n417,9n717n777,9CA_n41A-n71A7CA_n41A-n77A7CA_n71A-n77A7 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n71(2A)-n77A | n417,9n717n777,9CA_n41A-n71A7CA_n41A-n77A7CA_n71A-n77A7 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n71A-n77(2A) | n417,9n777,9CA_n41A-n71A7CA_n41A-n77A7CA_n71A-n77A7 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41(3A)-n71A-n77A | n417,9n717n777,9CA_n41A-n71A7CA_n41A-n77A7CA_n71A-n77A7 | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n71(2A)-n77(2A) | n417,9n777,9CA_n41A-n71A7CA_n41A-n77A7CA_n71A-n77A7 | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41(2A)-n71B-n77(2A) | CA_n41A-n71ACA_n41A-n77ACA_n71A-n77A | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41(2A)-n71(2A)-n77(2A) | CA_n41A-n71ACA_n41A-n77ACA_n71A-n77A | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41(3A)-n71B-n77A | n417,9n777,9CA_n41A-n71A7CA_n41A-n77A7CA_n71A-n77A7 | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(3A)-n71(2A)-n77A | n417,9n777,9CA_n41A-n71A7CA_n41A-n77A7CA_n71A-n77A7 | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n71A-n77A | n417,9n717n777,9CA_n41A-n71A7CA_n41A-n77A7,9CA_n41C7,9CA_n71A-n77A7CA_n41C-n71A7CA_n41C-n77A7,9 | n41 | CA_n41C_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n71B-n77A | n417,9n717n777,9CA_n41A-n71A7CA_n41A-n77A7CA_n41C7CA_n41C-n71ACA_n41C-n77ACA_n71A-n77A7 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n71(2A)-n77A | n417,9n717n777,9CA_n41A-n71A7CA_n41A-n77A7CA_n41C7CA_n41C-n71ACA_n41C-n77ACA_n71A-n77A7 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n71A-n77(2A) | n417,9n777,9CA_n41A-n71A7CA_n41A-n77A7CA_n41C7CA_n71A-n77A7 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41C-n71B-n77(2A) | CA_n41A-n71ACA_n41A-n77ACA_n41CCA_n71A-n77A | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41C-n71(2A)-n77(2A) | CA_n41A-n71ACA_n41A-n77ACA_n41CCA_n71A-n77A | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41(A-C)-n71A-n77A | n417,9n717n777,9CA_n41A-n71A7CA_n41C-n71ACA_n41A-n77A7CA_n41C-n77ACA_n41C7CA_n71A-n77A7 | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(A-C)-n71B-n77A | n417,9n777,9CA_n41A-n71A7CA_n41C-n71ACA_n41A-n77A7CA_n41C-n77ACA_n41C7CA_n71A-n77A7 | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(A-C)-n71(2A)-n77A | n417,9n777,9CA_n41A-n71A7CA_n41C-n71ACA_n41A-n77A7CA_n41C-n77ACA_n41C7CA_n71A-n77A7 | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n71A-n78A | CA_n41A-n71ACA_n41A-n78ACA_n71A-n78A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n41A-n71A-n78(2A) | CA_n41A-n71ACA_n41A-n78ACA_n71A-n78A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n41A-n71A-n78C | CA_n78CCA_n41A-n71ACA_n41A-n78ACA_n41A-n78CCA_n71A-n78ACA_n71A-n78C | n41 | 5,10,15,20,25,30,35,40,45,50,60,70,80,90,100 | 4 and 5 |
|  |  | n71 | 5,10,15,20 |  |
|  |  | n78 | CA_n78C_BCS 4 and 5 |  |
| CA_n41A-n71A-n85A | CA_n41A-n71ACA_n41A-n85A | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n71B-n85A | CA_n41A-n71ACA_n41A-n85A | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n71(2A)-n85A | CA_n41A-n71ACA_n41A-n85A | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n74A-n77A | n417n777CA_n41A-n74A7CA_n41A-n77A7CA_n74A-n77A7 | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n74 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n41A-n75A-n78A | - | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n75 | 5,10, 15, 20, 25,30,40,50 |  |
|  |  | n78 | 10, 15, 20, 25,30,40, 50, 60,70, 80, 90, 100 |  |
| CA_n41A-n77A-n79A | n417,9n777,9n797,9CA_n41A-n77A7CA_n41A-n79A7CA_n77A-n79A7 | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n41A-n77(2A)-n79A | n417,9n777,9n797,9CA_n41A-n77A7CA_n41A-n79A7CA_n77A-n79A7 | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  | CA_n77(2A)7 | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n41A-n77(3A)-n79A | CA_n41A-n77ACA_n41A-n79ACA_n77A-n79A | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 | 0 |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n41A-n77A-n85A | CA_n41A-n77ACA_n41A-n85ACA_n77A-n85A | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n77A-n85A | CA_n41A-n77A CA_n41A-n85A CA_n77A-n85A | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n77(2A)-n85A | CA_n41A-n77A CA_n41A-n85A CA_n77A-n85A | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n77A-n85A | CA_n41A-n77A CA_n41A-n85A CA_n41C CA_n77A-n85A | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |

##### Table 5.5A.3.2-1c

Table 5.5A.3.2-1c: NR CA configurations and bandwidth combinations sets defined for inter-band CA (three bands)

| NR CA configuration | Uplink CA configurationor single uplink carrier6 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n46A-n48A-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46B-n48A-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46C-n48A-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46D-n48A-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46M-n48A-n96A | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46N-n48A-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46A-n48B-n96A | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46B-n48B-n96A | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46C-n48B-n96A | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46D-n48B-n96A | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46M-n48B-n96A | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46N-n48B-n96A | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46A-n48C-n96A | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46B-n48C-n96A | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46C-n48C-n96A | CA_n46A-n48ACA_n46A-n48B CA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46D-n48C-n96A | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46M-n48C-n96A | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46N-n48C-n96A | CA_n46A-n48ACA_n46A-n48B CA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46A-n48A-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46B-n48A-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46C-n48A-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46D-n48A-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 1001 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46M-n48A-n96B | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46N-n48A-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46A-n48A-n96C | - | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46B-n48A-n96C | - | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46C-n48A-n96C | - | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46D-n48A-n96C | - | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46M-n48A-n96C | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46N-n48A-n96C | - | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46A-n48B-n96C | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46B-n48B-n96C | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46C-n48B-n96C | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46D-n48B-n96C | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46M-n48B-n96C | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46N-n48B-n96C | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46A-n48C-n96C | - | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46B-n48C-n96C | - | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46C-n48C-n96C | - | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46D-n48C-n96C | - | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46M-n48C-n96C | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46N-n48C-n96C | - | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46A-n48A-n96D | - | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46B-n48A-n96D | - | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46C-n48A-n96D | - | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46D-n48A-n96D | - | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46M-n48A-n96D | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46N-n48A-n96D | - | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46A-n48C-n96D | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46B-n48C-n96D | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46C-n48C-n96D | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46D-n48C-n96D | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46M-n48C-n96D | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46N-n48C-n96D | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46A-n48A-n96E | - | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46B-n48A-n96E | - | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46C-n48A-n96E | - | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46D-n48A-n96E | - | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46M-n48A-n96E | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46N-n48A-n96E | - | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46A-n48C-n96E | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46B-n48C-n96E | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46C-n48C-n96E | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46D-n48C-n96E | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46M-n48C-n96E | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46N-n48C-n96E | CA_n46A-n48ACA_n46A-n48BCA_n48A-n96ACA_n48BCA_n48B-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48C_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46A-n48(2A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46B-n48(2A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46C-n48(2A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46D-n48(2A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46M-n48(2A)-n96A | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46N-n48(2A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46A-n48(2A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46B-n48(2A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46C-n48(2A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46D-n48(2A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46M-n48(2A)-n96B | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46N-n48(2A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46A-n48(2A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46B-n48(2A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46C-n48(2A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46D-n48(2A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46M-n48(2A)-n96C | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46N-n48(2A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46A-n48(2A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46B-n48(2A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46C-n48(2A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46D-n48(2A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46M-n48(2A)-n96D | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46N-n48(2A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46A-n48(2A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46B-n48(2A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46C-n48(2A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46D-n48(2A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46M-n48(2A)-n96E | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46N-n48(2A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46A-n48(3A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46B-n48(3A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46C-n48(3A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46D-n48(3A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46M-n48(3A)-n96A | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46N-n48(3A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46A-n48(3A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46B-n48(3A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46C-n48(3A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46D-n48(3A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46M-n48(3A)-n96B | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46N-n48(3A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46A-n48(3A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46B-n48(3A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46C-n48(3A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46D-n48(3A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46M-n48(3A)-n96C | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46N-n48(3A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46A-n48(3A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46B-n48(3A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46C-n48(3A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46D-n48(3A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46M-n48(3A)-n96D | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46N-n48(3A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46A-n48(3A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46B-n48(3A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46C-n48(3A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46D-n48(3A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46M-n48(3A)-n96E | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46N-n48(3A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(3A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46A-n48(4A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46B-n48(4A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46C-n48(4A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46D-n48(4A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46M-n48(4A)-n96A | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46N-n48(4A)-n96A | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | 20, 40, 60, 80 |  |
| CA_n46A-n48(4A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46B-n48(4A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46C-n48(4A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46D-n48(4A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46M-n48(4A)-n96B | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46N-n48(4A)-n96B | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96B_BCS0 |  |
| CA_n46A-n48(4A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46B-n48(4A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46C-n48(4A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46D-n48(4A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46M-n48(4A)-n96C | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46N-n48(4A)-n96C | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96C_BCS0 |  |
| CA_n46A-n48(4A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46B-n48(4A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46C-n48(4A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46D-n48(4A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46M-n48(4A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46N-n48(4A)-n96D | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96D_BCS0 |  |
| CA_n46A-n48(4A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | 10, 20, 40, 60, 80 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46B-n48(4A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46B_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46C-n48(4A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46D-n48(4A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46M-n48(4A)-n96E | - | n46 | CA_n46M_BCS0 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46N-n48(4A)-n96E | CA_n46A-n48ACA_n48A-n96A | n46 | CA_n46N_BCS1 | 0 |
|  |  | n48 | CA_n48(4A)_BCS0 |  |
|  |  | n96 | CA_n96E_BCS0 |  |
| CA_n46A-n78A-n102A | CA_n46A-n78ACA_n78A-n102A | n46 | 10,20, 40, 60, 80, 100 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n46A-n78A-n102B | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102B | n46 | 10,20, 40, 60, 80, 100 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n46A-n78A-n102C | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102C | n46 | 10,20, 40, 60, 80, 100 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n46A-n78A-n102D | CA_n46A-n78ACA_n78A-n102A | n46 | 10,20, 40, 60, 80, 100 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n46A-n78A-n102E | CA_n46A-n78ACA_n78A-n102A | n46 | 10,20, 40, 60, 80, 100 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n46A-n78A-n102(2A) | CA_n46A-n78ACA_n78A-n102A | n46 | 10,20, 40, 60, 80, 100 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n46(2A)-n78A-n102A | CA_n46A-n78ACA_n78A-n102A | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n46(2A)-n78A-n102B | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102B | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n46(2A)-n78A-n102C | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102C | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n46(2A)-n78A-n102D | CA_n46A-n78ACA_n78A-n102A | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n46(2A)-n78A-n102E | CA_n46A-n78ACA_n78A-n102A | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n46(2A)-n78A-n102(2A) | CA_n46A-n78ACA_n78A-n102A | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n46C-n78A-n102A | CA_n46A-n78ACA_n78A-n102A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n46C-n78A-n102B | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102B | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n46C-n78A-n102C | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102C | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n46C-n78A-n102D | CA_n46A-n78ACA_n78A-n102A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n46C-n78A-n102E | CA_n46A-n78ACA_n78A-n102A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n46C-n78A-n102(2A) | CA_n46A-n78ACA_n78A-n102A | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n46D-n78A-n102A | CA_n46A-n78ACA_n78A-n102A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n46D-n78A-n102B | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102B | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n46D-n78A-n102C | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102C | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n46D-n78A-n102D | CA_n46A-n78ACA_n78A-n102A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n46D-n78A-n102E | CA_n46A-n78ACA_n78A-n102A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n46D-n78A-n102(2A) | CA_n46A-n78ACA_n78A-n102A | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n46A-n78(2A)-n102A | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | 10,20, 40, 60, 80, 100 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n46A-n78(2A)-n102B | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102BCA_n78(2A) | n46 | 10,20, 40, 60, 80, 100 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n46A-n78(2A)-n102C | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102CCA_n78(2A) | n46 | 10,20, 40, 60, 80, 100 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n46A-n78(2A)-n102D | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | 10,20, 40, 60, 80, 100 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n46A-n78(2A)-n102E | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | 10,20, 40, 60, 80, 100 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n46A-n78(2A)-n102(2A) | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | 10,20, 40, 60, 80, 100 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n46(2A)-n78(2A)-n102A | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n46(2A)-n78(2A)-n102B | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102BCA_n78(2A) | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n46(2A)-n78(2A)-n102C | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102CCA_n78(2A) | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n46(2A)-n78(2A)-n102D | CA_n46A-n78ACA_n78A-n102A | n46 | CA_n46(2A)_BCS0 | 0 |
|  | CA_n78(2A) | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n46(2A)-n78(2A)-n102E | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n46(2A)-n78(2A)-n102(2A) | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | CA_n46(2A)_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n46C-n78(2A)-n102A | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n46C-n78(2A)-n102B | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102BCA_n78(2A) | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n46C-n78(2A)-n102C | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102CCA_n78(2A) | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n46C-n78(2A)-n102D | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n46C-n78(2A)-n102E | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n46C-n78(2A)-n102(2A) | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | CA_n46C_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n46D-n78(2A)-n102A | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | 20, 40, 60, 80, 100 |  |
| CA_n46D-n78(2A)-n102B | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102BCA_n78(2A) | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102B_BCS0 |  |
| CA_n46D-n78(2A)-n102C | CA_n46A-n78ACA_n78A-n102ACA_n78A-n102CCA_n78(2A) | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102C_BCS0 |  |
| CA_n46D-n78(2A)-n102D | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102D_BCS0 |  |
| CA_n46D-n78(2A)-n102E | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102E_BCS0 |  |
| CA_n46D-n78(2A)-n102(2A) | CA_n46A-n78ACA_n78A-n102ACA_n78(2A) | n46 | CA_n46D_BCS0 | 0 |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n102 | CA_n102(2A)_BCS0 |  |
| CA_n48A-n66A-n70A | CA_n48A-n66ACA_n48A-n70A | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n48A-n66(2A)-n70A | CA_n48A-n66ACA_n48A-n70A | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n48(2A)-n66A-n70A | CA_n48A-n66ACA_n48A-n70A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n48(2A)-n66(2A)-n70A | CA_n48A-n66ACA_n48A-n70A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n48(3A)-n66A-n70A | CA_n48A-n66ACA_n48A-n70A | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n48A-n66(3A)-n70A | CA_n48A-n66ACA_n48A-n70A | n48 | 5, 10, 15, 20, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n48B-n66A-n70A | CA_n48A-n66ACA_n48A-n70A | n48 | CA_n48B_BCS2 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
| CA_n48A-n66A-n71A | CA_n48A-n66ACA_n48A-n71ACA_n66A-n71A | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48A-n66(2A)-n71A | CA_n48A-n66ACA_n48A-n71ACA_n66A-n71A | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48(2A)-n66A-n71A | CA_n48A-n66ACA_n48A-n71ACA_n66A-n71A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48(2A)-n66A-n71(2A) | CA_n48A-n66ACA_n48A-n71ACA_n66A-n71A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
| CA_n48A-n66(3A)-n71A | CA_n48A-n66ACA_n48A-n71ACA_n66A-n71A | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48B-n66A-n71A | CA_n48A-n66ACA_n48A-n71ACA_n66A-n71A | n48 | CA_n48B_BCS2 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48A-n66A-n71(2A) | CA_n48A-n66ACA_n48A-n71ACA_n66A-n71A | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
| CA_n48A-n66A-n77A | n777,9CA_n48A-n66ACA_n66A-n77A7,13,14 | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n48A-n66ACA_n66A-n77A7,13,14 | n48 | n48 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48A-n66(2A)-n77A | n777,9CA_n48A-n66ACA_n66A-n77A7,13,14 | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n48A-n66ACA_n66A-n77A7,13,14 | n48 | n48 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48A-n66(3A)-n77A | CA_n48A-n66ACA_n66A-n77A | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48A-n66A-n77C | n777,9CA_n48A-n66ACA_n66A-n77A7,13,14CA_n77C7,9 | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n777,9CA_n48A-n66ACA_n66A-n77A7,13,14CA_n66A-n77CCA_n77C7,9 | n48 | n48 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n48B-n66A-n77C | n777,9CA_n48A-n66ACA_n66A-n77A7,13,14CA_n77C | n48 | CA_n48B_BCS2 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n777,9CA_n48A-n66ACA_n48B-n66ACA_n66A-n77A7,13,14CA_n66A-n77CCA_n48BCA_n77C | n48 | CA_n48B_BCS4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n48B-n66A-n77A | n777,9CA_n48A-n66ACA_n66A-n77A7,13,14 | n48 | CA_n48B_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n48 | CA_n48B_BCS1 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n48 | CA_n48B_BCS2 | 2 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n48A-n66ACA_n48B-n66ACA_n66A-n77A7,13,14CA_n48B | n48 | CA_n48B_BCS4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48(2A)-n66A-n77A | n777,9CA_n48A-n66ACA_n66A-n77A7,13,14 | n48 | CA_n48(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n48 | CA_n48(2A)_BCS1 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n777,9CA_n48A-n66ACA_n66A-n77A7,13,14 | n48 | CA_n48(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48(3A)-n66A-n77A | CA_n48A-n66ACA_n66A-n77A | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(2A)-n66A-n77C | n777,9CA_n77CCA_n48A-n66ACA_n66A-n77A7,13,14 | n48 | CA_n48(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n48 | CA_n48(2A)_BCS0 | 1 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  |  | n48 | CA_n48(2A)_BCS1 | 2 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  |  | n48 | CA_n48(2A)_BCS1 | 3 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | n777,9CA_n77CCA_n48A-n66ACA_n66A-n77A7,13,14CA_n66A-n77C | n48 | CA_n48(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n48B-n66(2A)-n77A | n777,9CA_n48BCA_n48A-n66ACA_n48B-n66ACA_n66A-n77A7,13,14 | n48 | CA_n48B_BCS4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48A-n66(2A)-n77C | n777,9CA_n77C7,9CA_n48A-n66ACA_n66A-n77A7,13,14CA_n66A-n77C | n48 | n48 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n48(2A)-n66(2A)-n77A | n777,9CA_n48A-n66ACA_n66A-n77A7,13,14 | n48 | CA_n48(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48(2A)-n66(2A)-n77C | n777,9CA_n77CCA_n48A-n66ACA_n66A-n77A7,13,14CA_n66A-n77C | n48 | CA_n48(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n48B-n66(2A)-n77C | n777,9CA_n48BCA_n77CCA_n48A-n66ACA_n48B-n66ACA_n66A-n77A7,13,14CA_n66A-n77C | n48 | CA_n48B_BCS4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS4 and 5 |  |
| CA_n48A-n70A-n71A | CA_n48A-n70ACA_n48A-n71ACA_n70A-n71A | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48(2A)-n70A-n71A | CA_n48A-n70ACA_n48A-n71ACA_n70A-n71A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48B-n70A-n71A | CA_n48A-n70ACA_n48A-n71ACA_n70A-n71A | n48 | CA_n48B_BCS2 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48A-n70A-n71(2A) | CA_n48A-n70ACA_n48A-n71ACA_n70A-n71A | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
| CA_n48(2A)-n70A-n71(2A) | CA_n48A-n70ACA_n48A-n71ACA_n70A-n71A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
| CA_n48A-n70A-n77A | CA_n48A-n70ACA_n70A-n77A | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(2A)-n70A-n77A | CA_n48A-n70ACA_n70A-n77A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(3A)-n70A-n77A | CA_n48A-n70ACA_n70A-n77A | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(2A)-n71A-n77A | CA_n48A-n71ACA_n71A-n77A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48A-n71A-n77A | CA_n48A-n71ACA_n71A-n77A | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48A-n71(2A)-n77A | CA_n48A-n71ACA_n71A-n77A | n48 | 5, 10, 15, 20, 30, 40, 5012, 6012, 7012, 8012, 9012, 10012 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(2A)-n71(2A)-n77A | CA_n48A-n71ACA_n71A-n77A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(3A)-n71A-n77A | CA_n48A-n71ACA_n71A-n77A | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n66A-n70A-n71A | n667n707n717CA_n66A-n71ACA_n70A-n71A | n66 | 5, 10, 15, 20, 40 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66A-n70A-n78A | CA_n66A-n78A CA_n70A-n78A | n66 | 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n66A-n70A-n71(2A) | CA_n66A-n71ACA_n70A-n71A | n66 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n66B-n70A-n71A | n667n707n717CA_n66A-n71ACA_n70A-n71A | n66 | CA_n66B_BCS0 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n66(2A)-n70A-n71A | n667n707n717CA_n66A-n71ACA_n70A-n71A | n66 | CA_n66(2A)_BCS0 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66(2A)-n70A-n71(2A) | CA_n66A-n71ACA_n70A-n71A | n66 | CA_n66(2A)_BCS0 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n66(3A)-n70A-n71A | n667n707n717CA_n66A-n71ACA_n70A-n71A | n66 | CA_n66(3A)_BCS0 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | CA_n66A-n71ACA_n70A-n71A | n66 | CA_n66(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66A-n70A-n77A | n667n707CA_n66A-n77ACA_n70A-n77A | n66 | 5, 10, 15, 20, 25, 30, 35, 40 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n66(2A)-n70A-n77A | n667n707CA_n66A-n77ACA_n70A-n77A | n66 | CA_n66(2A)_BCS0 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n66(3A)-n70A-n77A | CA_n66A-n77ACA_n70A-n77A | n66 | CA_n66(3A)_BCS0 | 0 |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n66A-n71A-n77A | n667n717n777,9CA_n66A-n71A7,13CA_n66A-n77A7,9,13,14CA_n71A-n77A7,9,13,14 | n66 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66A-n71B-n77A | n667n717n777,9CA_n66A-n71A7CA_n66A-n77A7,13,14CA_n71A-n77A7,13,14 | n66 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | CA_n71B_BCS2 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66A-n71B-n77(2A) | n777,9CA_n66A-n71ACA_n66A-n77A7CA_n71A-n77A7 | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n66A-n71(2A)-n77A | n667n717n777,9CA_n66A-n71A7CA_n66A-n77A7,13,14CA_n71A-n77A7,13,14 | n66 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66A-n71(2A)-n77(2A) | n777,9CA_n66A-n71ACA_n66A-n77A7CA_n71A-n77A7 | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n66(2A)-n71A-n77A | n667n717n777,9CA_n66A-n71A7CA_n66A-n77A7,13,14CA_n71A-n77A7,13,14 | n66 | CA_n66(2A)_BCS1 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n66A-n71ACA_n66A-n77ACA_n71A-n77A | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66(3A)-n71A-n77A | CA_n66A-n71ACA_n66A-n77ACA_n71A-n77A | n66 | CA_n66(3A)_BCS0 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n66A-n71A-n77(2A) | n667n717n777,9CA_n77(2A)7CA_n66A-n71A7CA_n66A-n77A7CA_n71A-n77A7 | n66 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n66A-n71A-n77(3A) | n777,9CA_n77(2A)7CA_n66A-n71ACA_n66A-n77A7CA_n71A-n77A7 | n66 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  | CA_n77(2A)CA_n66A-n71ACA_n66A-n77ACA_n71A-n77A | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n66(2A)-n71B-n77A | n667n717n777,9CA_n66A-n71A7CA_n66A-n77A7CA_n71A-n77A7 | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66(2A)-n71B-n77(2A) | n777,9CA_n66A-n71ACA_n66A-n77A7CA_n71A-n77A7 | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n66(2A)-n71(2A)-n77A | n667n717n777,9CA_n66A-n71A7CA_n66A-n77A7CA_n71A-n77A7 | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66(2A)-n71A-n77(2A) | n777,9CA_n66A-n71ACA_n66A-n77A7CA_n71A-n77A7 | n66 | CA_n66(2A)_BCS1 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n66(2A)-n71(2A)-n77(2A) | n777,9CA_n66A-n71ACA_n66A-n77A7CA_n71A-n77A7 | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n66A-n71A-n78A | CA_n66A-n71ACA_n66A-n78ACA_n71A-n78A | n66 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n66A-n71A-n78(2A) | CA_n66A-n71ACA_n66A-n78ACA_n71A-n78A | n66 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n66(2A)-n71A-n78A | CA_n66A-n71ACA_n66A-n78ACA_n71A-n78A | n66 | CA_n66(2A)_BCS1 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n66(2A)-n71A-n78(2A) | CA_n66A-n71ACA_n66A-n78ACA_n71A-n78A | n66 | CA_n66(2A)_BCS1 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n66A-n71A-n85A | CA_n66A-n71ACA_n66A-n85A | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66A-n71B-n85A | CA_n66A-n71A CA_n66A-n85A | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66A-n71(2A)-n85A | CA_n66A-n71A CA_n66A-n85A | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66(2A)-n71A-n85A | CA_n66A-n71A CA_n66A-n85A | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66A-n77A-n85A | CA_n66A-n77ACA_n66A-n85ACA_n77A-n85A | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66A-n77(2A)-n85A | CA_n66A-n77A CA_n66A-n85A CA_n77A-n85A | n66 | n66 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n66(2A)-n77A-n85A | CA_n66A-n77ACA_n66A-n85ACA_n77A-n85A | n66 | CA_n66(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n70A-n71A-n77A | CA_n70A-n71ACA_n70A-n77ACA_n71A-n77A | n70 | 5, 10, 15, 20, 25 | 0 |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n70A-n71(2A)-n77A | CA_n70A-n71ACA_n70A-n77ACA_n71A-n77A | n70 | 5, 10, 15, 20, 25 | 0 |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |

The following notes are applied to the above tables.

NOTE 1: This UE channel bandwidth is applicable only to downlink

NOTE 2: For the 20 MHz bandwidth, the minimum requirements are specified for NR UL carrier frequencies confined to either 713-723 MHz or 728-738 MHz.

NOTE 3:  For each channel bandwidth of each component carrier, refer to Table 5.3.5-1 for the applicable SCSs. For a given band, not all UE channel bandwidths support the same SCSs.

NOTE 4: The minimum requirements only apply for non-simultaneous Rx/Tx between all carriers for TDD combinations.

NOTE 5: Simultaneous Rx/Tx capability for TDD combinations does not apply for UEs supporting band n78 with an n77 implementation.

NOTE 6: Only single uplink carriers with power class other than PC3 are listed.

NOTE 7: Minimum requirements for Power Class 2 are applicable for this uplink combination or single uplink carrier in this downlink/uplink combination

NOTE 8: For this bandwidth, the minimum requirements are restricted to operation when carrier is configured as an SCell part of DC or CA configuration.

NOTE 9: Minimum requirements for Power Class 1.5 are applicable for this uplink combination or single uplink carrier in this downlink/uplink combination

NOTE 10: For a band combination which include band n7 and n38 simultaneously, carriers in band n7 and n38 can only be configured as downlink carriers. Power imbalance between downlink carriers on Band n7 and Band n38 is assumed to be within 6dB.

NOTE 11: UL carrier shall be supported in Band n28 only. Power imbalance between downlink carriers on Band 7 and Band 38 is assumed to be within 6dB.

NOTE 12: For this bandwidth, the minimum requirements are restricted to operation when carrier is configured as a downlink SCell part of CA configuration.

NOTE 13: Minimum requirements for Power Class 2 are applicable for this uplink CA configuration according to clause 6.2H.3.1 or 6.2L.3.1.

NOTE 14: Minimum requirements for Power Class 1.5 are applicable for this uplink CA configuration according to clause 6.2H.3.1 or 6.2L.3.1.

NOTE 15: For a two-band UL configuration without NOTE 7 or NOTE 13, minimum requirements for Power Class 2 are applicable provided the said power class has been specified in Table 6.2A.1.3-1 or Table 6.2H.3.1-1 respectively and the corresponding PC2 MSD is specified in clause 7.3A.2.3.2 or there is no MSD impact for this downlink/uplink combination.

NOTE 16: For a two-band UL configuration without NOTE 9 or NOTE 14, minimum requirements for Power Class 1.5 are applicable provided the said power class has been specified in Table 6.2A.1.3-1 or Table 6.2H.3.1-1 respectively and the corresponding PC1.5 MSD is specified in clause 7.3A.2.3.2 or there is no MSD impact for this downlink/uplink combination.

NOTE 17: The frequency range in band n28 is restricted for this band combination to 703-733MHz for the UL and 758-788MHz for the DL.

NOTE 18: This combination only works for non-simultaneous RX/TX. In the case that there is no simultaneous RX/TX also no RX sensitivity section is needed.

#### 5.5A.3.3 Configurations for inter-band CA (four bands)

Table 5.5A.3.3-1: Void

##### Table 5.5A.3.3-1a

Table 5.5A.3.3-1a: NR CA configurations and bandwidth combinations sets defined for inter-band CA (four bands)

| NR CA configuration | Uplink CA configurationor single uplink carrier 4 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n1A-n3A-n5A-n7A | CA_n1A-n3ACA_n1A-n5ACA_n1A-n7ACA_n3A-n5ACA_n3A-n7ACA_n5A-n7A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
| CA_n1A-n3A-n5A-n7B | CA_n1A-n3ACA_n1A-n5ACA_n1A-n7ACA_n3A-n5ACA_n3A-n7ACA_n5A-n7ACA_n7B | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
| CA_n1A-n3A-n5A-n28A | CA_n1A-n3ACA_n1A-n5ACA_n1A-n28ACA_n3A-n5ACA_n3A-n28ACA_n5A-n28A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n5A-n78A | CA_n1A-n3ACA_n1A-n5ACA_n1A-n78ACA_n3A-n5ACA_n3A-n78ACA_n5A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7A-n8A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n8ACA_n3A-n7ACA_n3A-n8ACA_n7A-n8A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n1A-n3(2A)-n7A-n8A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n8ACA_n3A-n7ACA_n3A-n8ACA_n7A-n8A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n1A-n3A-n7(2A)-n8A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n8ACA_n3A-n7ACA_n3A-n8ACA_n7A-n8A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n1A-n3(2A)-n7(2A)-n8A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n8ACA_n3A-n7ACA_n3A-n8ACA_n7A-n8A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
| CA_n1A-n3A-n7A-n20A | n35n75CA_n1A-n3A5CA_n1A-n7A5CA_n1A-n20ACA_n3A-n7A5CA_n3A-n20A5CA_n7A-n20A5 | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7A-n26A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n26ACA_n3A-n7ACA_n3A-n26ACA_n7A-n26A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
| CA_n1A-n3B-n7A-n26A | CA_n3BCA_n1A-n3ACA_n1A-n7ACA_n1A-n26ACA_n3A-n7ACA_n3A-n26ACA_n7A-n26A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
| CA_n1A-n3A-n7B-n26A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n26ACA_n3A-n7ACA_n3A-n26ACA_n7A-n26ACA_n7B | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
| CA_n1A-n3B-n7B-n26A | CA_n7BCA_n1A-n3ACA_n1A-n7ACA_n1A-n26ACA_n3A-n7ACA_n3A-n26ACA_n7A-n26A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
| CA_n1A-n3A-n7A-n26(2A) | CA_n1A-n3ACA_n1A-n7ACA_n1A-n26ACA_n3A-n7ACA_n3A-n26ACA_n7A-n26A | n1 | 5, 10, 15, 20 | 0 |
|  | CA_n26(2A) | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n1A-n3B-n7A-n26(2A) | CA_n1A-n3ACA_n1A-n7ACA_n1A-n26ACA_n3A-n7ACA_n3A-n26ACA_n7A-n26A | n1 | 5, 10, 15, 20 | 0 |
|  | CA_n26(2A) | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n1A-n3A-n7B-n26(2A) | CA_n7BCA_n26(2A)CA_n1A-n3ACA_n1A-n7ACA_n1A-n26ACA_n3A-n7ACA_n3A-n26ACA_n7A-n26A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n1A-n3B-n7B-n26(2A) | CA_n7BCA_n26(2A)CA_n1A-n3ACA_n1A-n7ACA_n1A-n26ACA_n3A-n7ACA_n3A-n26ACA_n7A-n26A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
| CA_n1A-n3A-n7A-n28A | n35n75 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  | n35n75CA_n1A-n3A5CA_n1A-n7A5CA_n1A-n28ACA_n3A-n7A5CA_n3A-n28A5CA_n7A-n28A5 | n1 | 5, 10, 15, 20 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 202 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7B-n28A | - | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  | CA_n1A-n3ACA_n1A-n7ACA_n1A-n28ACA_n3A-n7ACA_n3A-n28ACA_n7A-n28ACA_n7B | n1 | 5, 10, 15, 20 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
| CA_n1A-n3B-n7A-n28A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n28ACA_n3A-n7ACA_n3A-n28ACA_n7A-n28A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
| CA_n1A-n3B-n7B-n28A | CA_n7BCA_n1A-n3ACA_n1A-n7ACA_n1A-n28ACA_n3A-n7ACA_n3A-n28ACA_n7A-n28A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
| CA_n1A-n3A-n7A-n38A7 | - | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1(2A)-n3A-n7A-n38A7 | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1A-n3B-n7A-n38A7 | - | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1(2A)-n3B-n7A-n38A7 | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1A-n3(2A)-n7A-n38A7 | - | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3(2A)_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1(2A)-n3(2A)-n7A-n38A7 | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3(2A)_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1A-n3A-n7A-n40A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n40ACA_n3A-n7ACA_n3A-n40ACA_n7A-n40A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7A-n67A | CA_n1A-n3ACA_n1A-n7ACA_n3A-n7A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7A-n75A | CA_n1A-n3ACA_n1A-n7ACA_n3A-n7A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7A-n77A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n77ACA_n3A-n7ACA_n3A-n77ACA_n7A-n77A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7A-n77(2A) | CA_n1A-n3ACA_n1A-n7ACA_n1A-n77ACA_n3A-n7ACA_n3A-n77ACA_n7A-n77ACA_n77(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n1A-n3A-n7A-n78A | n35n75n785,6CA_n1A-n3A5CA_n1A-n7A5CA_n1A-n78A5CA_n3A-n7A5CA_n3A-n78A5CA_n7A-n78A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 2 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3B-n7A-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3B-n7B-n78A | CA_n7BCA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7A-n78(2A) | n35n75n785,6CA_n78(2A)5CA_n1A-n3A5CA_n1A-n7A5CA_n1A-n78A5CA_n3A-n7A5CA_n3A-n78A5CA_n7A-n78A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3A-n7A-n78C | CA_n78CCA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3A-n7B-n78A | - | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78ACA_n7B | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3B-n7A-n78(2A) | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | CA_n3B_BCS 4 and 5 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3B-n7A-n78C | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78ACA_n78C | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n3A-n7B-n78(2A) | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78ACA_n7B | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n7B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78A CA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | CA_n7B_BCS 4 and 5 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3A-n7B-n78C | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78ACA_n7BCA_n78C | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n7B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
|  | CA_n3A-n7ACA_n78CCA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n78ACA_n7A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | CA_n7B_BCS 4 and 5 |  |
|  |  | n78 | CA_n78C_BCS 4 and 5 |  |
| CA_n1A-n3B-n7B-n78(2A) | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78ACA_n7B | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n3BCA_n7B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | CA_n3B_BCS 4 and 5 |  |
|  |  | n7 | CA_n7B_BCS 4 and 5 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3B-n7B-n78C | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78ACA_n7BCA_n78C | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n3(2A)-n7A-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7(2A)-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3(2A)-n7(2A)-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7A-n79A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n3A-n7A-n79C | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1(2A)-n3A-n7A-n79A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1(2A)-n3A-n7A-n79C | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1A-n3B-n7A-n79A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n3B-n7A-n79C | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1(2A)-n3B-n7A-n79A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1(2A)-n3B-n7A-n79C | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1A-n3(2A)-n7A-n79A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n3(2A)-n7A-n79C | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1(2A)-n3(2A)-n7A-n79A | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1(2A)-n3(2A)-n7A-n79C | - | n1 | CA_n1(2A)_BCS0 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n79 | CA_n79C_BCS0 |  |
| CA_n1A-n3A-n7A-n105A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n105ACA_n3A-n7ACA_n3A-n105ACA_n7A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n105 | 5, 10,15, 20, 25, 30, 35 |  |
| CA_n1A-n3A-n8A-n40A | CA_n1A-n3ACA_n1A-n8ACA_n1A-n40ACA_n3A-n8ACA_n3A-n40ACA_n8A-n40A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n8A-n41A | CA_n1A-n3ACA_n1A-n8ACA_n1A-n41ACA_n3A-n8ACA_n3A-n41ACA_n8A-n41A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n8A-n77A | - | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
| CA_n1A-n3A-n8A-n77(2A) | - | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n1A-n3A-n8A-n78A | CA_n1A-n3ACA_n1A-n8ACA_n1A-n78ACA_n3A-n8ACA_n3A-n78ACA_n8A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 901, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3(2A)-n8A-n78A | CA_n1A-n3ACA_n1A-n8ACA_n1A-n78ACA_n3A-n8ACA_n3A-n78ACA_n8A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n8A-n78C | CA_n1A-n3ACA_n1A-n8ACA_n1A-n78ACA_n1A-n78CCA_n3A-n8ACA_n3A-n78ACA_n3A-n78CCA_n8A-n78ACA_n8A-n78C | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3(2A)-n8A-n78C | CA_n1A-n3ACA_n1A-n8ACA_n1A-n78ACA_n1A-n78CCA_n3A-n8ACA_n3A-n78ACA_n3A-n78CCA_n8A-n78ACA_n8A-n78C | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3A-n18A-n28A | CA_n1A-n3ACA_n1A-n18ACA_n1A-n28ACA_n3A-n18ACA_n3A-n28A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n28 | 5, 10 |  |
| CA_n1A-n3A-n18A-n41A | n415,6CA_n1A-n3ACA_n1A-n18ACA_n1A-n41A5,6CA_n3A-n18ACA_n3A-n41A5,6CA_n18A-n41A5,6 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
| CA_n1A-n3A-n18A-n77A | n775CA_n1A-n3ACA_n1A-n18ACA_n1A-n77A5CA_n3A-n18ACA_n3A-n77A5CA_n18A-n77A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n18A-n77(2A) | n775CA_n1A-n3ACA_n1A-n18ACA_n1A-n77A5CA_n3A-n18ACA_n3A-n77A5CA_n18A-n77A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n1A-n3A-n20A-n41A | CA_n1A-n3ACA_n1A-n20ACA_n1A-n41ACA_n3A-n20ACA_n3A-n41ACA_n20A-n41A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n20A-n67A | CA_n1A-n3ACA_n1A-n20ACA_n3A-n20A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n20A-n71A | CA_n1A-n3ACA_n1A-n20ACA_n1A-n71ACA_n3A-n20ACA_n3A-n71ACA_n20A-n71A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
| CA_n1A-n3A-n20A-n75A | CA_n1A-n3ACA_n1A-n20ACA_n3A-n20A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n20A-n77A | CA_n1A-n3ACA_n1A-n20ACA_n1A-n77ACA_n3A-n20ACA_n3A-n77ACA_n20A-n77A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n20A-n77(2A) | CA_n1A-n3ACA_n1A-n20ACA_n1A-n77ACA_n3A-n20ACA_n3A-n77ACA_n20A-n77A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n1A-n3A-n20A-n78A | CA_n1A-n3ACA_n1A-n20ACA_n1A-n78ACA_n3A-n20ACA_n3A-n78ACA_n20A-n78A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n1A-n3ACA_n1A-n20ACA_n1A-n78ACA_n3A-n20ACA_n3A-n78ACA_n20A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n20A-n78(2A) | CA_n1A-n3ACA_n1A-n20ACA_n1A-n78ACA_n3A-n20ACA_n3A-n78ACA_n20A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3A-n26A-n78A | CA_n1A-n3ACA_n1A-n26ACA_n1A-n78ACA_n3A-n26ACA_n3A-n78ACA_n26A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n26(2A)-n78A | CA_n1A-n3ACA_n1A-n26ACA_n1A-n78ACA_n3A-n26ACA_n3A-n78ACA_n26A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n26(2A) | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n26A-n78(2A) | CA_n1A-n3ACA_n1A-n26ACA_n1A-n78ACA_n3A-n26ACA_n3A-n78ACA_n26A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n1A-n3A-n26A-n78C | CA_n1A-n3ACA_n1A-n26ACA_n1A-n78ACA_n3A-n26ACA_n3A-n78ACA_n26A-n78ACA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3A-n26(2A)-n78(2A) | CA_n1A-n3ACA_n1A-n26ACA_n1A-n78ACA_n3A-n26ACA_n3A-n78ACA_n26A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n26(2A)CA_n78(2A) | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n1A-n3A-n26(2A)-n78C | CA_n1A-n3ACA_n1A-n26ACA_n1A-n78ACA_n3A-n26ACA_n3A-n78ACA_n26A-n78ACA_n26(2A)CA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3B-n26A-n78A | CA_n1A-n3ACA_n1A-n26ACA_n1A-n78ACA_n3A-n26ACA_n3A-n78ACA_n26A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3B-n26(2A)-n78A | CA_n1A-n3ACA_n1A-n26ACA_n1A-n78ACA_n3A-n26ACA_n3A-n78ACA_n26A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n26(2A) | n3 | CA_n3B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3B-n26A-n78(2A) | CA_n1A-n3ACA_n1A-n26ACA_n1A-n78ACA_n3A-n26ACA_n3A-n78ACA_n26A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | CA_n3B_BCS 4 and 5 |  |
|  |  | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3B-n26A-n78C | CA_n1A-n3ACA_n1A-n26ACA_n1A-n78ACA_n3A-n26ACA_n3A-n78ACA_n26A-n78ACA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n3B-n26(2A)-n78(2A) | CA_n1A-n3ACA_n1A-n26ACA_n1A-n78ACA_n3A-n26ACA_n3A-n78ACA_n26A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n26(2A)CA_n78(2A) | n3 | CA_n3B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n1A-n3B-n26(2A)-n78C | CA_n1A-n3ACA_n1A-n26ACA_n1A-n78ACA_n3A-n26ACA_n3A-n78ACA_n26A-n78ACA_n26(2A)CA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n3A-n28A-n38A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1A-n3A-n28A-n40A | CA_n1A-n3ACA_n1A-n28ACA_n1A-n40ACA_n3A-n28ACA_n3A-n40ACA_n28A-n40A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n28A-n41A | n415,6CA_n1A-n3ACA_n1A-n28ACA_n1A-n41A5,6CA_n3A-n28ACA_n3A-n41A5,6CA_n28A-n41A5,6 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n28A-n75A | CA_n1A-n3ACA_n1A-n28ACA_n3A-n28A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n28A-n77A | n775,6CA_n1A-n3ACA_n1A-n28ACA_n1A-n77A5CA_n3A-n28ACA_n3A-n77A5CA_n28A-n77A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20 | 1 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n28 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n28A-n77(2A) | n775,6CA_n1A-n3ACA_n1A-n28ACA_n1A-n77A5CA_n3A-n28ACA_n3A-n77A5CA_n28A-n77A5CA_n77(2A)5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n1A-n3A-n28A-n77(3A) | n775,6CA_n1A-n3ACA_n1A-n28ACA_n1A-n77A5CA_n3A-n28ACA_n3A-n77A5CA_n28A-n77A5CA_n77(2A)5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS 4 and 5 |  |
| CA_n1A-n3A-n28A-n78A | n35n785,6 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n28 | 5, 10, 15, 202 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 901, 100 |  |
|  | n35n785,6CA_n1A-n3A5CA_n1A-n28ACA_n1A-n78A5CA_n3A-n28A5CA_n3A-n78A5CA_n28A-n78A5 | n1 | 5, 10, 15, 20 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n28 | 5, 10, 15, 202 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 2 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 202,302 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n28A-n78(2A) | n35n785,6 CA_n78(2A)5CA_n1A-n3A5CA_n1A-n28ACA_n1A-n78A5CA_n3A-n28A5CA_n3A-n78A5CA_n28A-n78A5 | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 202, 302 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3A-n28A-n78C | CA_n78CCA_n1A-n3ACA_n1A-n28ACA_n1A-n78ACA_n3A-n28ACA_n3A-n78ACA_n28A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 202, 302 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n3B-n28A-n78A | CA_n1A-n3ACA_n1A-n28ACA_n1A-n78ACA_n3A-n28ACA_n3A-n78ACA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3B-n28A-n78(2A) | CA_n78(2A)CA_n1A-n3ACA_n1A-n28ACA_n1A-n78ACA_n3A-n28ACA_n3A-n78ACA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n1A-n3B-n28A-n78C | CA_n1A-n3ACA_n1A-n28ACA_n1A-n78ACA_n3A-n28ACA_n3A-n78ACA_n28A-n78ACA_n78C | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n3A-n28A-n79A | n795,6CA_n1A-n3ACA_n1A-n28ACA_n1A-n79A5CA_n3A-n28ACA_n3A-n79A5CA_n28A-n79A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25,30 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  | CA_n1A-n3ACA_n1A-n28ACA_n1A-n79ACA_n3A-n28ACA_n3A-n79ACA_n28A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n38A-n78A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n40A-n41A | CA_n1A-n3ACA_n1A-n40ACA_n1A-n41ACA_n3A-n40ACA_n3A-n41ACA_n40A-n41A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n40A-n77A | CA_n1A-n3ACA_n1A-n40ACA_n1A-n77ACA_n3A-n40ACA_n3A-n77ACA_n40A-n77A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n40A-n77(2A) | CA_n1A-n3ACA_n1A-n40ACA_n1A-n77ACA_n3A-n40ACA_n3A-n77ACA_n40A-n77A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n1A-n3A-n40A-n78A | CA_n1A-n3ACA_n1A-n40ACA_n1A-n78ACA_n3A-n40ACA_n3A-n78ACA_n40A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n40A-n79A | CA_n1A-n3ACA_n1A-n79ACA_n1A-n40ACA_n3A-n79ACA_n3A-n40ACA_n40A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n40A-n105A | CA_n1A-n3ACA_n1A-n40ACA_n1A-n105ACA_n3A-n40ACA_n3A-n105ACA_n40A-n105A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n3A-n41A-n71A | CA_n1A-n3ACA_n1A-n41ACA_n1A-n71ACA_n3A-n41ACA_n3A-n71ACA_n41A-n71A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n1A-n3A-n41A-n77A | n415,6n775,6CA_n1A-n3ACA_n1A-n41A5CA_n1A-n77A5CA_n3A-n41A5CA_n3A-n77A5CA_n41A-n77A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n41A-n77(2A) | n415,6n775,6CA_n1A-n3ACA_n1A-n41A5CA_n1A-n77A5CA_n3A-n41A5CA_n3A-n77A5CA_n41A-n77A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n1A-n3A-n41A-n78A | CA_n1A-n3ACA_n1A-n41ACA_n1A-n78ACA_n3A-n41ACA_n3A-n78ACA_n41A-n78A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n41A-n78C | CA_n1A-n3ACA_n1A-n41ACA_n1A-n78ACA_n1A-n78CCA_n3A-n41ACA_n3A-n78ACA_n3A-n78CCA_n41A-n78ACA_n41A-n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3(2A)-n41A-n78A | CA_n1A-n3ACA_n1A-n41ACA_n1A-n78ACA_n3A-n41ACA_n3A-n78ACA_n41A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3(2A)-n41A-n78C | CA_n1A-n3ACA_n1A-n41ACA_n1A-n78ACA_n1A-n78CCA_n3A-n41ACA_n3A-n78ACA_n3A-n78CCA_n41A-n78ACA_n41A-n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3A-n41A-n79A | CA_n1A-n3ACA_n1A-n41ACA_n1A-n79ACA_n3A-n41ACA_n3A-n79ACA_n41A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n3A-n67A-n78A | CA_n1A-n3ACA_n1A-n78ACA_n3A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n67A-n78(2A) | CA_n1A-n3ACA_n1A-n78ACA_n3A-n78ACA_n78(2A) | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n3A-n71A-n77A | CA_n1A-n3ACA_n1A-n71ACA_n1A-n77A CA_n3A-n71ACA_n3A-n77ACA_n71A-n77A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n71A-n77(2A) | CA_n1A-n3ACA_n1A-n71ACA_n1A-n77A CA_n3A-n71ACA_n3A-n77ACA_n71A-n77A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n1A-n3A-n71A-n78A | CA_n1A-n3ACA_n1A-n71ACA_n1A-n78ACA_n3A-n71ACA_n3A-n78ACA_n71A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n71A-n78C | CA_n1A-n3ACA_n1A-n71ACA_n1A-n78ACA_n1A-n78CCA_n3A-n71ACA_n3A-n78ACA_n3A-n78CCA_n71A-n78ACA_n71A-n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3(2A)-n71A-n78A | CA_n1A-n3ACA_n1A-n71ACA_n1A-n78ACA_n3A-n71ACA_n3A-n78ACA_n71A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3(2A)-n71A-n78C | CA_n1A-n3ACA_n1A-n71ACA_n1A-n78ACA_n3A-n71ACA_n3A-n78ACA_n71A-n78ACA_n71A-n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3A-n75A-n78A | CA_n1A-n3ACA_n1A-n78ACA_n3A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n75A-n78(2A) | CA_n1A-n3ACA_n1A-n78ACA_n3A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3A-n77A-n79A | n775,6n795,6CA_n1A-n3ACA_n1A-n77A5CA_n1A-n79A5CA_n3A-n77A5CA_n3A-n79A5CA_n77A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25,30 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  | CA_n1A-n3ACA_n1A-n77ACA_n1A-n79ACA_n3A-n77ACA_n3A-n79ACA_n77A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n77(2A)-n79A | n775,6n795,6CA_n1A-n3ACA_n1A-n77A5CA_n1A-n79A5CA_n3A-n77A5CA_n3A-n79A5CA_n77A-n79ACA_n77(2A)5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25,30 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n77(3A)-n79A | CA_n1A-n3ACA_n1A-n77ACA_n1A-n79ACA_n3A-n77ACA_n3A-n79ACA_n77A-n79ACA_n77(2A) | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25,30 |  |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS 4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n78A-n79A | CA_n1A-n3ACA_n1A-n78ACA_n1A-n79ACA_n3A-n78ACA_n3A-n79ACA_n78A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n78A-n105A | CA_n1A-n3ACA_n1A-n78ACA_n1A-n105ACA_n3A-n78ACA_n3A-n105ACA_n78A-n105A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25,30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25,30, 35 |  |
| CA_n1A-n5A-n7A-n40A | CA_n1A-n5A CA_n1A-n7A CA_n1A-n40A CA_n5A-n7A CA_n5A-n40A CA_n7A-n40A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n5A-n7A-n78A | CA_n1A-n5ACA_n1A-n7ACA_n1A-n78ACA_n5A-n7ACA_n5A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n5A-n7B-n78A | CA_n1A-n5ACA_n1A-n7ACA_n1A-n78ACA_n5A-n7ACA_n5A-n78ACA_n7A-n78ACA_n7B | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n5A-n7A-n105A | CA_n1A-n5A CA_n1A-n7A CA_n1A-n105A CA_n5A-n7A CA_n5A-n105A CA_n7A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n5A-n28A-n78A | CA_n1A-n5ACA_n1A-n28ACA_n1A-n78ACA_n5A-n28ACA_n5A-n78ACA_n28A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n5A-n28A-n79A | CA_n1A-n5ACA_n1A-n28ACA_n1A-n79ACA_n5A-n28ACA_n5A-n79ACA_n28A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n5A-n40A-n78A | CA_n1A-n5ACA_n1A-n40ACA_n1A-n78ACA_n5A-n40ACA_n5A-n78ACA_n40A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n5A-n40A-n105A | CA_n1A-n5A CA_n1A-n40A CA_n1A-n105A CA_n5A-n40A CA_n5A-n105A CA_n40A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n5A-n78A-n79A | CA_n1A-n5ACA_n1A-n78ACA_n1A-n79ACA_n5A-n78ACA_n5A-n79ACA_n78A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n5A-n78A-n105A | CA_n1A-n5A CA_n1A-n78A CA_n1A-n105A CA_n5A-n78A CA_n5A-n105A CA_n78A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40 , 50 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n7A-n8A-n40A | CA_n1A-n7A CA_n1A-n8ACA_n1A-n40ACA_n7A-n8A CA_n7A-n40ACA_n8A-n40A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n8A-n78A | CA_n1A-n7A CA_n1A-n8A CA_n1A-n78ACA_n7A-n8A CA_n7A-n78ACA_n8A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n7(2A)-n8A-n78A | CA_n1A-n7ACA_n1A-n8ACA_n1A-n78ACA_n7A-n8ACA_n7A-n78ACA_n8A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n7A-n20A-n28A11 | CA_n1A-n7ACA_n1A-n20ACA_n1A-n28ACA_n7A-n20ACA_n7A-n28ACA_n20A-n28A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n20A-n67A | CA_n1A-n7ACA_n1A-n20ACA_n7A-n20A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n20A-n75A | CA_n1A-n7ACA_n1A-n20ACA_n7A-n20A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n20A-n78A | CA_n1A-n7ACA_n1A-n20ACA_n1A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n20A-n78(2A) | CA_n1A-n7ACA_n1A-n20ACA_n1A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n7A-n26A-n78A | CA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n7B-n26A-n78A | CA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n7A-n26(2A)-n78A | CA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  | CA_n26(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n7A-n26A-n78(2A) | CA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n7A-n26A-n78C | CA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n7A-n26(2A)-n78(2A) | CA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  | CA_n26(2A)CA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n1A-n7A-n26(2A)-n78C | CA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n26(2A)CA_n78C | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n7B-n26(2A)-n78A | CA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n1 | 5, 10, 15, 20 | 0 |
|  | CA_n26(2A) | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n7B-n26A-n78(2A) | CA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | CA_n7B_BCS 4 and 5 |  |
|  |  | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n7B-n26A-n78C | CA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7BCA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n7B-n26(2A)-n78(2A) | CA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n1 | 5, 10, 15, 20 | 0 |
|  | CA_n26(2A) | n7 | CA_n7B_BCS0 |  |
|  | CA_n78(2A) | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n1A-n7B-n26(2A)-n78C | CA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7BCA_n26(2A)CA_n78C | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n7A-n28A-n38A7 | - | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1A-n7A-n28A-n75A | CA_n1A-n7ACA_n1A-n28ACA_n7A-n28A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n28A-n78A | n75n785,6CA_n1A-n7A5CA_n1A-n28ACA_n1A-n78A5CA_n7A-n28A5CA_n7A-n78A5CA_n28A-n78A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7B-n28A-n78A | CA_n1A-n7ACA_n1A-n28ACA_n1A-n78ACA_n7A-n28ACA_n7A-n78ACA_n7BCA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n7B-n28A-n78(2A) | CA_n7BCA_n78(2A)CA_n1A-n7ACA_n1A-n28ACA_n1A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n1A-n7B-n28A-n78C | CA_n7BCA_n78CCA_n1A-n7ACA_n1A-n28ACA_n1A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n7A-n28A-n78(2A) | n75n785,6CA_n78(2A)5CA_n1A-n7A5CA_n1A-n28ACA_n1A-n78A5CA_n7A-n28A5CA_n7A-n78A5CA_n28A-n78A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 202 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n7A-n28A-n78C | CA_n78CCA_n1A-n7ACA_n1A-n28ACA_n1A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 202 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n7A-n38A-n78A7 | - | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n7A-n40A-n78A | CA_n1A-n7ACA_n1A-n40A CA_n1A-n78ACA_n7A-n40ACA_n7A-n78A CA_n40A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n40A-n79A | CA_n1A-n7ACA_n1A-n79ACA_n1A-n40ACA_n7A-n40ACA_n7A-n79ACA_n40A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n40A-n105A | CA_n1A-n7ACA_n1A-n40ACA_n1A-n105ACA_n7A-n40ACA_n7A-n105A CA_n40A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n7A-n67A-n78A | CA_n1A-n7ACA_n1A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n67A-n78(2A) | CA_n1A-n7ACA_n1A-n78ACA_n7A-n78ACA_n78(2A) | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n7A-n75A-n78A | CA_n1A-n7ACA_n1A-n78ACA_n7A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n75A-n78(2A) | CA_n1A-n7ACA_n1A-n78ACA_n7A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n7A-n78A-n79A | CA_n1A-n7ACA_n1A-n78ACA_n1A-n79ACA_n7A-n78ACA_n7A-n79ACA_n78A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n78A-n105A | CA_n1A-n7ACA_n1A-n78ACA_n1A-n105ACA_n7A-n78ACA_n7A-n105A CA_n78A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n8A-n28A-n40A | CA_n1A-n8ACA_n1A-n28ACA_n1A-n40ACA_n8A-n28ACA_n8A-n40ACA_n28A-n40A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n8A-n40A-n78A | CA_n1A-n8ACA_n1A-n40ACA_n1A-n78ACA_n8A-n40ACA_n8A-n78ACA_n40A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n8A-n40A-n79A | CA_n1A-n8ACA_n1A-n40ACA_n1A-n79ACA_n8A-n40ACA_n8A-n79ACA_n40A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n8A-n41A-n78A | CA_n1A-n8ACA_n1A-n41ACA_n1A-n78ACA_n8A-n41ACA_n8A-n78ACA_n41A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n8A-n41A-n78C | CA_n1A-n8ACA_n1A-n41ACA_n1A-n78ACA_n1A-n78CCA_n8A-n41ACA_n8A-n78ACA_n8A-n78CCA_n41A-n78ACA_n41A-n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n8A-n78A-n79A | CA_n1A-n8ACA_n1A-n78ACA_n1A-n79ACA_n8A-n78ACA_n8A-n79ACA_n78A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n8A-n78(2A)-n79A | - | n1 | 5, 10, 15, 20 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS1 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n18A-n28A-n41A | n415,6CA_n1A-n18ACA_n1A-n28ACA_n1A-n41A5CA_n18A-n28ACA_n18A-n41A5CA_n28A-n41A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
| CA_n1A-n18A-n28A-n77A | n775,6CA_n1A-n18ACA_n1A-n28ACA_n1A-n77A5CA_n18A-n28ACA_n18A-n77A5CA_n28A-n77A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n28 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n18A-n41A-n77A | n415n775CA_n1A-n18ACA_n1A-n41A5CA_n1A-n77A5CA_n18A-n41A5CA_n18A-n77A5CA_n41A-n77A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n20A-n28A-n78A9 | CA_n1A-n20ACA_n1A-n28ACA_n1A-n78ACA_n20A-n28ACA_n20A-n78ACA_n28A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n20A-n41A-n71A | CA_n1A-n20ACA_n1A-n41ACA_n1A-n71ACA_n20A-n41ACA_n20A-n71ACA_n41A-n71A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
| CA_n1A-n20A-n41A-n77A | CA_n1A-n20ACA_n1A-n41ACA_n1A-n77ACA_n20A-n41ACA_n20A-n77ACA_n41A-n77A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n20A-n41A-n77(2A) | CA_n1A-n20ACA_n1A-n41ACA_n1A-n77ACA_n20A-n41ACA_n20A-n77ACA_n41A-n77A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n1A-n20A-n41A-n78A | CA_n1A-n20ACA_n1A-n41ACA_n1A-n78ACA_n20A-n41ACA_n20A-n78ACA_n41A-n78A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n20A-n67A-n78A | CA_n1A-n20ACA_n1A-n78ACA_n20A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n20A-n67A-n78(2A) | CA_n1A-n20ACA_n1A-n78ACA_n20A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n20A-n71A-n78A | CA_n1A-n20ACA_n1A-n71ACA_n1A-n78ACA_n20A-n71ACA_n20A-n78ACA_n71A-n78A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n20A-n75A-n78A | CA_n1A-n20ACA_n1A-n78ACA_n20A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n20A-n75A-n78(2A) | CA_n1A-n20ACA_n1A-n78ACA_n20A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n28A-n38A-n78A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n28A-n40A-n41A | CA_n1A-n28ACA_n1A-n40ACA_n1A-n41ACA_n28A-n40ACA_n28A-n41ACA_n40A-n41A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n28A-n40A-n77A | CA_n1A-n28ACA_n1A-n40ACA_n1A-n77ACA_n28A-n40ACA_n28A-n77ACA_n40A-n77A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n28A-n40A-n77(2A) | CA_n1A-n28ACA_n1A-n40ACA_n1A-n77ACA_n28A-n40ACA_n28A-n77ACA_n40A-n77A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n1A-n28A-n40A-n78A | CA_n1A-n28ACA_n1A-n40ACA_n1A-n78ACA_n28A-n40ACA_n28A-n78ACA_n40A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n28A-n40B-n78A | CA_n1A-n28ACA_n1A-n40ACA_n1A-n78ACA_n28A-n40ACA_n28A-n78ACA_n40A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n40 | CA_n40B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n28A-n40A-n79A | CA_n1A-n28ACA_n1A-n40ACA_n1A-n79ACA_n28A-n40ACA_n28A-n79ACA_n40A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n28A-n41A-n77A | n415,6n775,6CA_n1A-n28ACA_n1A-n41A5CA_n1A-n77A5CA_n28A-n41A5CA_n28A-n77A5CA_n41A-n77A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n28A-n41A-n77(2A) | n415,6n775,6CA_n1A-n28ACA_n1A-n41A5CA_n1A-n77A5CA_n28A-n41A5CA_n28A-n77A5CA_n41A-n77A5 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n1A-n28A-n41A-n79A | CA_n1A-n28ACA_n1A-n41ACA_n1A-n79ACA_n28A-n41ACA_n28A-n79ACA_n41A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n28A-n75A-n78A | - | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n75 | 5, 10, 15, 20, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n1A-n28ACA_n1A-n78ACA_n28A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n28A-n75A-n78(2A) | CA_n1A-n28ACA_n1A-n78ACA_n28A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n28A-n77A-n79A | n775,6n795,6CA_n1A-n28ACA_n1A-n77A5CA_n1A-n79A5CA_n28A-n77A5CA_n28A-n79A5CA_n77A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  | CA_n1A-n28ACA_n1A-n77ACA_n1A-n79ACA_n28A-n77ACA_n28A-n79ACA_n77A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n28A-n78A-n79A | n785,6n795,6CA_n1A-n28ACA_n1A-n78ACA_n1A-n79ACA_n28A-n78ACA_n28A-n79ACA_n78A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n28A-n77(2A)-n79A | CA_n1A-n28ACA_n1A-n77ACA_n1A-n79ACA_n28A-n77ACA_n28A-n79ACA_n77A-n79ACA_n77(2A) | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n28A-n77(3A)-n79A | CA_n1A-n28ACA_n1A-n77ACA_n1A-n79ACA_n28A-n77ACA_n28A-n79ACA_n77A-n79ACA_n77(2A) | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS 4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n40A-n78A-n79A | CA_n1A-n40ACA_n1A-n78ACA_n1A-n79ACA_n40A-n78ACA_n40A-n79ACA_n78A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n40A-n78A-n105A | CA_n1A-n40ACA_n1A-n78ACA_n1A-n105ACA_n40A-n78ACA_n40A-n105ACA_n78A-n105A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n41A-n71A-n77A | CA_n1A-n41ACA_n1A-n71A CA_n1A-n77A CA_n41A-n71ACA_n41A-n77ACA_n71A-n77A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n41A-n71A-n77(2A) | CA_n1A-n41ACA_n1A-n71A CA_n1A-n77A CA_n41A-n71ACA_n41A-n77ACA_n71A-n77A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n1A-n41A-n71A-n78A | CA_n1A-n41ACA_n1A-n71ACA_n1A-n78ACA_n41A-n71ACA_n41A-n78ACA_n71A-n78A | n1 | 5, 10, 15, 20, 30, 40, 50 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n41A-n71A-n78C | CA_n1A-n41ACA_n1A-n71ACA_n1A-n78ACA_n1A-n78CCA_n41A-n71ACA_n41A-n78ACA_n41A-n78CCA_n71A-n78ACA_n71A-n78C | n1 | 5, 10, 15, 20, 30, 40, 50 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n41A-n77A-n79A | CA_n1A-n41ACA_n1A-n77ACA_n1A-n79ACA_n41A-n77ACA_n41A-n79ACA_n77A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n41A-n77(2A)-n79A | CA_n1A-n41ACA_n1A-n77ACA_n1A-n79ACA_n41A-n77ACA_n41A-n79ACA_n77A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n2A-n5A-n30A-n66A | CA_n2A-n5ACA_n2A-n30ACA_n2A-n66ACA_n5A-n30ACA_n5A-n66ACA_n30A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n30A-n66A | CA_n2A-n5ACA_n2A-n30ACA_n2A-n66ACA_n5A-n30ACA_n5A-n66ACA_n30A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
| CA_n2A-n5A-n30A-n66(2A) | CA_n2A-n5ACA_n2A-n30ACA_n2A-n66ACA_n5A-n30ACA_n5A-n66ACA_n30A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n2A-n5A-n30A-n77A | n775,6CA_n2A-n5ACA_n2A-n30ACA_n2A-n77A5CA_n5A-n30ACA_n5A-n77A5CA_n30A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n30A-n77A | n775,6CA_n2A-n5ACA_n2A-n30ACA_n2A-n77A5CA_n5A-n30ACA_n5A-n77A5CA_n30A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2(2A)-n5A-n30A-n77(2A) | n775,6CA_n2A-n5ACA_n2A-n30ACA_n2A-n77A5CA_n5A-n30ACA_n5A-n77A5CA_n30A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n5A-n30A-n77(2A) | n775,6CA_n2A-n5ACA_n2A-n30ACA_n2A-n77A5CA_n5A-n30ACA_n5A-n77A5CA_n30A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n2A-n5A-n48A-n66A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 |  |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
|  | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n48A-n66A | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n48A-n66(2A) | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n2(2A)-n5A-n48A-n66(2A) | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n2A-n5A-n48(2A)-n66(2A) | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n2A-n5A-n48B-n66(2A) | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n2A-n48BCA_n5A-n48ACA_n5A-n48BCA_n5A-n66ACA_n48A-n66ACA_n48B-n66ACA_n48B | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n2A-n5A-n48B-n66A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | CA_n48B_BCS2 |  |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
|  | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 2 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | CA_n48B_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 3 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | CA_n48B_BCS2 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  | CA_n48BCA_n2A-n5ACA_n2A-n48ACA_n2A-n48BCA_n2A-n66ACA_n5A-n48ACA_n5A-n48BCA_n5A-n66ACA_n48A-n66A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n48B-n66A | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5B-n48B-n66A | CA_n2A-n5ACA_n2A-n48ACA_n2A-n48BCA_n2A-n66ACA_n5A-n48ACA_n5A-n48BCA_n5A-n66ACA_n48A-n66ACA_n48B-n66ACA_n48B | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n5B | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n48(2A)-n66A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
|  | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 2 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5B-n48A-n66A | CA_n5BCA_n2A-n5ACA_n2A-n66ACA_n2A-n48ACA_n5A-n66ACA_n5A-n48ACA_n48A-n66A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5B-n48A-n66A | CA_n5BCA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5B-n48(2A)-n66A | CA_n5BCA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5B-n48A-n66(2A) | CA_n5BCA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
| CA_n2(2A)-n5A-n48(2A)-n66A | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n48B-n66A | CA_n2A-n5ACA_n2A-n48ACA_n2A-n48BCA_n2A-n66ACA_n5A-n48ACA_n5A-n48BCA_n5A-n66ACA_n48A-n66ACA_n48B-n66ACA_n48B | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n48(A-B)-n66A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | CA_n48(A-B)_BCS1 |  |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
|  | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n5A-n48ACA_n5A-n66ACA_n48A-n66A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48(A-B)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n48A-n77A | n775,6 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n775,6CA_n2A-n5ACA_n2A-n48ACA_n2A-n77A5CA_n5A-n48ACA_n5A-n77A5 | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n2A-n5ACA_n2A-n48ACA_n2A-n77ACA_n5A-n48ACA_n5A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n48A-n77A | CA_n2A-n5ACA_n2A-n48ACA_n2A-n77ACA_n5A-n48ACA_n5A-n77A | n2 | CccA_n2(2A)_BCS 4 and 5 _BCS 4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n48(2A)-n77A | CA_n2A-n5ACA_n2A-n48ACA_n2A-n77ACA_n5A-n48ACA_n5A-n77A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5B-n48A-n77A | CA_n5BCA_n2A-n5ACA_n2A-n48ACA_n2A-n77ACA_n5A-n48ACA_n5A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5B-n48A-n77A | CA_n5BCA_n2A-n5ACA_n2A-n48ACA_n2A-n77ACA_n5A-n48ACA_n5A-n77A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5B-n48(2A)-n77A | CA_n5BCA_n2A-n5ACA_n2A-n48ACA_n2A-n77ACA_n5A-n48ACA_n5A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n48A-n77C | n775,6CA_n77CCA_n2A-n5ACA_n2A-n48ACA_n2A-n77A5CA_n5A-n48ACA_n5A-n77A5 | n2 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  | n775,6 | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | CA_n77CCA_n2A-n5ACA_n2A-n48ACA_n2A-n77ACA_n2A-n77CCA_n5A-n48ACA_n5A-n77ACA_n5A-n77C | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2(2A)-n5A-n48A-n77C | CA_n77CCA_n2A-n5ACA_n2A-n48ACA_n2A-n77ACA_n2A-n77CCA_n5A-n48ACA_n5A-n77ACA_n5A-n77C | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2A-n5B-n48A-n77C | CA_n5BCA_n77CCA_n2A-n5ACA_n2A-n48ACA_n2A-n77ACA_n2A-n77CCA_n5A-n48ACA_n5A-n77ACA_n5A-n77C | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2A-n5A-n48B-n77A | n775,6 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | CA_n48B_BCS2 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n775,6CA_n2A-n5ACA_n2A-n48ACA_n2A-n77A5CA_n5A-n48ACA_n5A-n77A5 | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 2 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | CA_n48B_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 3 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | CA_n48B_BCS2 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n48BCA_n2A-n5ACA_n2A-n48ACA_n2A-n48BCA_n2A-n77ACA_n5A-n48ACA_n5A-n48BCA_n5A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n48B-n77A | CA_n48BCA_n2A-n5ACA_n2A-n48ACA_n2A-n48BCA_n2A-n77ACA_n5A-n48ACA_n5A-n48BCA_n5A-n77A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5B-n48B-n77A | CA_n5BCA_n48BCA_n2A-n5ACA_n2A-n48ACA_n2A-n48BCA_n2A-n77ACA_n5A-n48ACA_n5A-n48BCA_n5A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n48B-n77C | CA_n48BCA_n77CCA_n2A-n5ACA_n2A-n48ACA_n2A-n48BCA_n2A-n77ACA_n2A-n77CCA_n5A-n48ACA_n5A-n48BCA_n5A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n5A-n77C | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2A-n5A-n48(2A)-n77A | n775,6 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n775,6CA_n2A-n5ACA_n2A-n48ACA_n2A-n77A5CA_n5A-n48ACA_n5A-n77A5 | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 2 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n2A-n5ACA_n2A-n48ACA_n2A-n77ACA_n5A-n48ACA_n5A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n48(2A)-n77C | CA_n77CCA_n2A-n5ACA_n2A-n48ACA_n2A-n77ACA_n2A-n77CCA_n5A-n48ACA_n5A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n5A-n77C | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2A-n5A-n66A-n77A | n775,6CA_n2A-n5ACA_n2A-n66ACA_n2A-n77A5CA_n5A-n66ACA_n5A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n2A-n5ACA_n2A-n66ACA_n2A-n77ACA_n5A-n66ACA_n5A-n77ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5B-n66A-n77A | CA_n5BCA_n2A-n5ACA_n2A-n66ACA_n2A-n77ACA_n5A-n66ACA_n5A-n77ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5B-n66(2A)-n77A | CA_n5BCA_n2A-n5ACA_n2A-n66ACA_n2A-n77ACA_n5A-n66ACA_n5A-n77ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n66A-n77A | n775,6CA_n2A-n5ACA_n2A-n66ACA_n2A-n77A5CA_n5A-n66ACA_n5A-n77A5CA_n66A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30,40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n2A-n5ACA_n2A-n66ACA_n2A-n77ACA_n5A-n66ACA_n5A-n77ACA_n66A-n77A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n66(2A)-n77A | CA_n2A-n5ACA_n2A-n66ACA_n2A-n77ACA_n5A-n66ACA_n5A-n77ACA_n66A-n77A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5B-n66A-n77A | CA_n5BCA_n2A-n5ACA_n2A-n66ACA_n2A-n77ACA_n5A-n66ACA_n5A-n77ACA_n66A-n77A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n66A-n77C | CA_n77CCA_n2A-n5ACA_n2A-n66ACA_n2A-n77ACA_n2A-n77CCA_n5A-n66ACA_n5A-n77ACA_n5A-n77CCA_n66A-n77ACA_n66A-n77C | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2A-n5A-n66(2A)-n77A | n775,6CA_n2A-n5ACA_n2A-n66ACA_n2A-n77A5CA_n5A-n66ACA_n5A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n2A-n5ACA_n2A-n66ACA_n2A-n77ACA_n5A-n66ACA_n5A-n77ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n66A-n77(2A) | n775,6CA_n2A-n5ACA_n2A-n66ACA_n2A-n77A5CA_n5A-n66ACA_n5A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n2A-n5A-n66(2A)-n77(2A) | n775,6CA_n2A-n5ACA_n2A-n66ACA_n2A-n77A5CA_n5A-n66ACA_n5A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2(2A)-n5A-n66A-n77(2A) | n775,6CA_n2A-n5ACA_n2A-n66ACA_n2A-n77A5CA_n5A-n66ACA_n5A-n77A5CA_n66A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n5A-n66A-n77C | n775,6CA_n77CCA_n2A-n5ACA_n2A-n66ACA_n2A-n77A5CA_n5A-n77A5CA_n5A-n66ACA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | CA_n77CCA_n2A-n5ACA_n2A-n66ACA_n2A-n77ACA_n2A-n77CCA_n5A-n77ACA_n5A-n77CCA_n5A-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n66A-n77C | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2A-n5A-n66(2A)-n77C | CA_n77CCA_n2A-n5ACA_n2A-n66ACA_n2A-n77ACA_n2A-n77CCA_n5A-n77ACA_n5A-n66ACA_n5A-n77CCA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n66A-n77C | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2A-n5B-n66A-n77C | CA_n5BCA_n77CCA_n2A-n5ACA_n2A-n66ACA_n2A-n77ACA_n2A-n77CCA_n5A-n66ACA_n5A-n77ACA_n5A-n77CCA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n66A-n77C | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2A-n12A-n30A-n66A | CA_n2A-n12ACA_n2A-n30ACA_n2A-n66ACA_n12A-n30ACA_n12A-n66ACA_n30A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n2(2A)-n12A-n30A-n66A | CA_n2A-n12ACA_n2A-n30ACA_n2A-n66ACA_n12A-n30ACA_n12A-n66ACA_n30A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n2A-n12A-n30A-n66(2A) | CA_n2A-n12ACA_n2A-n30ACA_n2A-n66ACA_n12A-n30ACA_n12A-n66ACA_n30A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n2A-n12A-n30A-n77A | n775,6CA_n2A-n12ACA_n2A-n30ACA_n2A-n77A5CA_n12A-n30ACA_n12A-n77A5CA_n30A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2(2A)-n12A-n30A-n77A | n775,6CA_n2A-n12ACA_n2A-n30ACA_n2A-n77A5CA_n12A-n30ACA_n12A-n77A5CA_n30A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n12A-n30A-n77(2A) | n775,6CA_n2A-n12ACA_n2A-n30ACA_n2A-n77A5CA_n12A-n30ACA_n12A-n77A5CA_n30A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2(2A)-n12A-n30A-n77(2A) | n775,6CA_n2A-n12ACA_n2A-n30ACA_n2A-n77A5CA_n12A-n30ACA_n12A-n77A5CA_n30A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n12A-n66A-n77A | n775,6CA_n2A-n12ACA_n2A-n66ACA_n2A-n77A5CA_n12A-n66ACA_n12A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2(2A)-n12A-n66A-n77A | n775,6CA_n2A-n12ACA_n2A-n66ACA_n2A-n77A5CA_n12A-n66ACA_n12A-n77A5CA_n66A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n12A-n66(2A)-n77A | n775,6CA_n2A-n12ACA_n2A-n66ACA_n2A-n77A5CA_n12A-n66ACA_n12A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n12A-n66A-n77(2A) | n775,6CA_n2A-n12ACA_n2A-n66ACA_n2A-n77A5CA_n12A-n66ACA_n12A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n12A-n66(2A)-n77(2A) | n775,6CA_n2A-n12ACA_n2A-n66ACA_n2A-n77A5CA_n12A-n66ACA_n12A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2(2A)-n12A-n66A-n77(2A) | n775,6CA_n2A-n12ACA_n2A-n66ACA_n2A-n77A5CA_n12A-n66ACA_n12A-n77A5CA_n66A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n14A-n30A-n66A | CA_n2A-n14ACA_n2A-n30ACA_n2A-n66ACA_n14A-n30ACA_n14A-n66ACA_n30A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n14A-n30A-n66A | CA_n2A-n14ACA_n2A-n30ACA_n2A-n66ACA_n14A-n30ACA_n14A-n66ACA_n30A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n2A-n14A-n30A-n66(2A) | CA_n2A-n14ACA_n2A-n30ACA_n2A-n66ACA_n14A-n30ACA_n14A-n66ACA_n30A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n2A-n14A-n30A-n77A | n775,6CA_n2A-n14ACA_n2A-n30ACA_n2A-n77A5CA_n14A-n30ACA_n14A-n77A5CA_n30A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n14A-n30A-n77A | n775,6CA_n2A-n14ACA_n2A-n30ACA_n2A-n77A5CA_n14A-n30ACA_n14A-n77A5CA_n30A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n14A-n30A-n77(2A) | n775,6CA_n2A-n14ACA_n2A-n30ACA_n2A-n77A5CA_n14A-n30ACA_n14A-n77A5CA_n30A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n2(2A)-n14A-n30A-n77(2A) | n775,6CA_n2A-n14ACA_n2A-n30ACA_n2A-n77A5CA_n14A-n30ACA_n14A-n77A5CA_n30A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n14A-n66A-n77A | n775,6CA_n2A-n14ACA_n2A-n66ACA_n2A-n77A5CA_n14A-n66ACA_n14A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n14A-n66A-n77A | n775,6CA_n2A-n14ACA_n2A-n66ACA_n2A-n77A5CA_n14A-n66ACA_n14A-n77A5CA_n66A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n14A-n66(2A)-n77A | n775,6CA_n2A-n14ACA_n2A-n66ACA_n2A-n77A5CA_n14A-n66ACA_n14A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n14A-n66A-n77(2A) | n775,6CA_n2A-n14ACA_n2A-n66ACA_n2A-n77A5CA_n14A-n66ACA_n14A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n2A-n14A-n66(2A)-n77(2A) | n775,6CA_n2A-n14ACA_n2A-n66ACA_n2A-n77A5CA_n14A-n66ACA_n14A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2(2A)-n14A-n66A-n77(2A) | n775,6CA_n2A-n14ACA_n2A-n66ACA_n2A-n77A5CA_n14A-n66ACA_n14A-n77A5CA_n66A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n29A-n30A-n66A | CA_n2A-n30ACA_n2A-n66ACA_n30A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n2(2A)-n29A-n30A-n66A | CA_n2A-n30ACA_n2A-n66ACA_n30A-n66A | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n2A-n29A-n30A-n66(2A) | CA_n2A-n30ACA_n2A-n66ACA_n30A-n66A | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
| CA_n2A-n29A-n30A-n77A | n775,6CA_n2A-n30ACA_n2A-n77A5CA_n30A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2(2A)-n29A-n30A-n77A | n775,6CA_n2A-n30ACA_n2A-n77A5CA_n30A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n29A-n30A-n77(2A) | n775,6CA_n2A-n30ACA_n2A-n77A5CA_n30A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2(2A)-n29A-n30A-n77(2A) | n775,6CA_n2A-n30ACA_n2A-n77A5CA_n30A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n29A-n66A-n77A | n775,6CA_n2A-n66ACA_n2A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2(2A)-n29A-n66A-n77A | n775,6CA_n2A-n66ACA_n2A-n77A5CA_n66A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n29A-n66(2A)-n77A | n775,6CA_n2A-n66ACA_n2A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n29A-n66A-n77(2A) | n775,6CA_n2A-n66ACA_n2A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2(2A)-n29A-n66A-n77(2A) | n775,6CA_n2A-n66ACA_n2A-n77A5CA_n66A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n29A-n66(2A)-n77(2A) | n775,6CA_n2A-n66ACA_n2A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n30A-n66A-n77A | n775,6CA_n2A-n30ACA_n2A-n66ACA_n2A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n30A-n66A-n77A | n775,6CA_n2A-n30ACA_n2A-n66ACA_n2A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n30A-n66(2A)-n77A | n775,6CA_n2A-n30ACA_n2A-n66ACA_n2A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n30A-n66A-n77(2A) | n775,6CA_n2A-n30ACA_n2A-n66ACA_n2A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n2A-n30A-n66(2A)-n77(2A) | n775,6CA_n2A-n30ACA_n2A-n66ACA_n2A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2(2A)-n30A-n66A-n77(2A) | n775,6CA_n2A-n30ACA_n2A-n66ACA_n2A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n2 | CA_n2(2A)_BCS0 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n41A-n66A-n71A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n2A-n48A-n66A-n77A | n775,6 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n775,6CA_n2A-n48ACA_n2A-n66ACA_n2A-n77A5CA_n48A-n66ACA_n66A-n77A5 | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n48A-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n48A-n66A-n77A | CA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n48A-n66ACA_n66A-n77A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48B-n66A-n77A | n775,6 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48B_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n775,6CA_n2A-n48ACA_n2A-n66ACA_n2A-n77A5CA_n48A-n66ACA_n66A-n77A5 | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 2 |
|  |  | n48 | CA_n48B_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 3 |
|  |  | n48 | CA_n48B_BCS2 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n48BCA_n2A-n48ACA_n2A-n48BCA_n2A-n66ACA_n2A-n77ACA_n48A-n66ACA_n48B-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n48B-n66A-n77A | CA_n48BCA_n2A-n48ACA_n2A-n48BCA_n2A-n66ACA_n2A-n77ACA_n48A-n66ACA_n48B-n66ACA_n66A-n77A | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48(2A)-n66A-n77A | n775,6 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n775,6CA_n2A-n48ACA_n2A-n66ACA_n2A-n77A5CA_n48A-n66ACA_n66A-n77A5 | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 2 |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n48A-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48A-n66(2A)-n77A | CA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n48A-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n48(2A)-n66A-n77A | CA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n48A-n66ACA_n66A-n77A | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n48A-n66(2A)-n77A | CA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n48A-n66ACA_n66A-n77A | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48B-n66(2A)-n77A | CA_n48BCA_n2A-n48ACA_n2A-n48BCA_n2A-n66ACA_n2A-n77ACA_n48A-n66ACA_n48B-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48(2A)-n66(2A)-n77A | CA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n48A-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n48A-n66A-n77C | n775,6 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS0 |  |
|  | n775,6CA_n77CCA_n2A-n48ACA_n2A-n66ACA_n2A-n77A5CA_n48A-n66ACA_n66A-n77A5 | n2 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  |  | n2 | 5, 10, 15, 20, 25, 30, 40 | 2 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | CA_n77CCA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n2A-n77CCA_n48A-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n66A-n77C | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2(2A)-n48A-n66A-n77C | CA_n77CCA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n2A-n77CCA_n48A-n66ACA_n66A-n77ACA_n66A-n77C | n2 | CA_n2(2A)_BCS4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2A-n48B-n66A-n77C | CA_n48BCA_n77CCA_n2A-n48ACA_n2A-n48BCA_n2A-n66ACA_n2A-n77ACA_n2A-n77CCA_n48A-n66ACA_n48B-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n66A-n77C | n48 | CA_n48B_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2A-n48(2A)-n66A-n77C | CA_n77CCA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n2A-n77CCA_n48A-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n66A-n77C | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2A-n48A-n66(2A)-n77C | CA_n77CCA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n2A-n77CCA_n48A-n66ACA_n66A-n77ACA_n66A-n77C | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2A-n66A-n71A-n77A | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n66A-n71A-n77(2A) | - | n2 | 5, 10, 15, 20 | 0 |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n66A-n71A-n78A | - | n2 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n66A-n71A-n78(2A) | - | n2 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n3A-n5A-n7A-n78A | - | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3A-n5ACA_n3A-n7ACA_n3A-n78ACA_n5A-n7ACA_n5A-n78ACA_n7A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n5A-n7B-n78A | - | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3A-n5ACA_n3A-n7ACA_n3A-n78ACA_n5A-n7ACA_n5A-n78ACA_n7A-n78ACA_n7B | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 1 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n5A-n28A-n78A | CA_n3A-n5ACA_n3A-n28ACA_n3A-n79ACA_n5A-n28ACA_n5A-n79ACA_n28A-n79A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n5A-n28A-n79A | CA_n3A-n5ACA_n3A-n28ACA_n3A-n79ACA_n5A-n28ACA_n5A-n79ACA_n28A-n79A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n8A-n40A | CA_n3A-n7ACA_n3A-n8ACA_n3A-n40ACA_n7A-n8ACA_n7A-n40ACA_n8A-n40A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n8A-n78A | CA_n3A-n7ACA_n3A-n8ACA_n3A-n78ACA_n7A-n8ACA_n7A-n78ACA_n8A-n78A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
| CA_n3(2A)-n7A-n8A-n78A | CA_n3A-n7ACA_n3A-n8ACA_n3A-n78ACA_n7A-n8ACA_n7A-n78ACA_n8A-n78A | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n7(2A)-n8A-n78A | CA_n3A-n7ACA_n3A-n8ACA_n3A-n78ACA_n7A-n8ACA_n7A-n78ACA_n8A-n78A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3(2A)-n7(2A)-n8A-n78A | CA_n3A-n7ACA_n3A-n8ACA_n3A-n78ACA_n7A-n8ACA_n7A-n78ACA_n8A-n78A | n3 | CA_n3(2A)_BCS0 | 0 |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n7A-n20A-n28A11 | CA_n3A-n7ACA_n3A-n20ACA_n3A-n28ACA_n7A-n20ACA_n7A-n28ACA_n20A-n28A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n20A-n67A | CA_n3A-n7ACA_n3A-n20ACA_n7A-n20A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n20A-n75A | CA_n3A-n7ACA_n3A-n20ACA_n7A-n20A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n20A-n78A | CA_n3A-n7ACA_n3A-n20ACA_n3A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n20A-n78(2A) | CA_n3A-n7ACA_n3A-n20ACA_n3A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78ACA_n78(2A) | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n3A-n7A-n26A-n78A | CA_n3A-n7ACA_n3A-n26ACA_n3A-n78ACA_n7A-n26ACA_n7A-n78ACA_n26A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n7B-n26A-n78A | CA_n3A-n7ACA_n3A-n26ACA_n3A-n78ACA_n7A-n26ACA_n7A-n78ACA_n26A-n78ACA_n7B | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n7A-n26(2A)-n78A | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  | CA_n26(2A) | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n7A-n26A-n78(2A) | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n78(2A) | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n3A-n7A-n26A-n78C | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n78C | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n3A-n7A-n26(2A)-n78(2A) | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  | CA_n26(2A) | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  | CA_n78(2A) | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n3A-n7A-n26(2A)-n78C | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n26(2A)CA_n78C | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n3A-n7B-n26(2A)-n78A | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  | CA_n26(2A) | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n7B-n26A-n78(2A) | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n78(2A) | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | CA_n7B_BCS 4 and 5 |  |
|  |  | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n3A-n7B-n26A-n78C | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7BCA_n78C | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n3A-n7B-n26(2A)-n78(2A) | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  | CA_n26(2A)CA_n78(2A) | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n3A-n7B-n26(2A)-n78C | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7BCA_n26(2A)CA_n78C | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n3B-n7A-n26A-n78A | CA_n3A-n7ACA_n3A-n26ACA_n3A-n78ACA_n7A-n26ACA_n7A-n78ACA_n26A-n78A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n7A-n26(2A)-n78A | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n3 | CA_n3B_BCS0 | 0 |
|  | CA_n26(2A) | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n7A-n26A-n78(2A) | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n78(2A) | n3 | CA_n3B_BCS 4 and 5 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n3B-n7A-n26A-n78C | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n78C | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3B-n7A-n26(2A)-n78(2A) | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n26(2A)CA_n78(2A) | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n3B-n7A-n26(2A)-n78C | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n26(2A)CA_n78C | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3B-n7B-n26A-n78A | CA_n3A-n7ACA_n3A-n26ACA_n3A-n78ACA_n7A-n26ACA_n7A-n78ACA_n26A-n78ACA_n7B | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n7B-n26(2A)-n78A | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n3 | CA_n3B_BCS0 | 0 |
|  | CA_n26(2A) | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n7B-n26A-n78(2A) | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n78(2A) | n3 | CA_n3B_BCS 4 and 5 | 4 and 5 |
|  |  | n7 | CA_n7B_BCS 4 and 5 |  |
|  |  | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n3B-n7B-n26A-n78C | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7BCA_n78C | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3B-n7B-n26(2A)-n78(2A) | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n3 | CA_n3B_BCS0 | 0 |
|  | CA_n26(2A) | n7 | CA_n7B_BCS0 |  |
|  | CA_n78(2A) | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n3B-n7B-n26(2A)-n78C | CA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7BCA_n26(2A)CA_n78C | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3A-n7A-n28A-n38A7 | - | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n3A-n7A-n28A-n75A | CA_n3A-n7ACA_n3A-n28ACA_n7A-n28A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n28A-n78A | n35n75n785,6 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n35n75n785,6CA_n3A-n7A5CA_n3A-n28A5CA_n3A-n78A5CA_n7A-n28A5CA_n7A-n78A5CA_n28A-n78A5 | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 202 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n28A-n78(2A) | n35n75n785,6CA_n78(2A)5CA_n3A-n7A5CA_n3A-n28A5CA_n3A-n78A5CA_n7A-n28A5CA_n7A-n78A5CA_n28A-n78A5 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 202 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n3A-n7A-n28A-n78C | CA_n78CCA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 202 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n3A-n7B-n28A-n78A | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n7BCA_n28A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n7B-n28A-n78(2A) | CA_n7BCA_n78(2A)CA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n3A-n7B-n28A-n78C | CA_n7BCA_n78CCA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n3B-n7A-n28A-n78A | CA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n7A-n28A-n78(2A) | CA_n78(2A)CA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n3B-n7B-n28A-n78A | CA_n7BCA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3B-n7B-n28A-n78(2A) | CA_n7BCA_n78(2A)CA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n3B-n7B-n28A-n78C | CA_n7BCA_n78CCA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3B-n7A-n28A-n78C | CA_n78CCA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n3 | CA_n3B_BCS0 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n3 | CA_n3B_BCS1 | 1 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n3A-n7A-n38A-n78A7 | - | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n7A-n40A-n78A | CA_n3A-n7ACA_n3A-n40ACA_n3A-n78ACA_n7A-n40ACA_n7A-n78ACA_n40A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n40A-n79A | CA_n3A-n7ACA_n3A-n79ACA_n3A-n40ACA_n7A-n40ACA_n40A-n79A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n40A-n105A | CA_n3A-n7ACA_n3A-n40ACA_n3A-n105ACA_n7A-n40ACA_n7A-n105ACA_n40A-n105A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n3A-n7A-n67A-n78A | CA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n67A-n78(2A) | CA_n3A-n7ACA_n3A-n78ACA_n7A-n78ACA_n78(2A) | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3A-n7A-n75A-n78A | CA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n75A-n78(2A) | CA_n3A-n7ACA_n3A-n78ACA_n7A-n78ACA_n78(2A) | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3A-n7A-n78A-n105A | CA_n3A-n7ACA_n3A-n78ACA_n3A-n105ACA_n7A-n78ACA_n7A-n105ACA_n78A-n105A | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n3A-n8A-n28A-n40A | CA_n3A-n8ACA_n3A-n28ACA_n3A-n40ACA_n8A-n28ACA_n8A-n40ACA_n28A-n40A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n8A-n39A-n41A | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
| CA_n3A-n8A-n39A-n79A | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n3A-n8A-n40A-n78A | CA_n3A-n8ACA_n3A-n40ACA_n3A-n78ACA_n8A-n40ACA_n8A-n78ACA_n40A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n8A-n40A-n79A | CA_n3A-n8ACA_n3A-n40ACA_n3A-n79ACA_n8A-n40ACA_n8A-n79ACA_n40A-n79A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n8A-n41A-n78A | CA_n3A-n8ACA_n3A-n41ACA_n3A-n78ACA_n8A-n41ACA_n8A-n78ACA_n41A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n8A-n41A-n78C | CA_n3A-n8ACA_n3A-n41ACA_n3A-n78ACA_n3A-n78CCA_n8A-n41ACA_n8A-n78ACA_n8A-n78CCA_n41A-n78ACA_n41A-n78C | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n3A-n8A-n41A-n79A | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n3A-n18A-n28A-n41A | n415,6CA_n3A-n18ACA_n3A-n28ACA_n3A-n41A5,6CA_n18A-n28ACA_n18A-n41A5,6CA_n28A-n41A5,6 | n3 | 5, 10, 15, 20 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n18A-n28A-n77A | n775CA_n3A-n18ACA_n3A-n28ACA_n3A-n77A5CA_n18A-n28ACA_n18A-n77A5CA_n28A-n77A5 | n3 | 5, 10, 15, 20 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n28 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n18A-n41A-n77A | n415n775CA_n3A-n18ACA_n3A-n41A5CA_n3A-n77A5CA_n18A-n41A5CA_n18A-n77A5CA_n41A-n77A5 | n3 | 5, 10, 15, 20 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n18 | n18 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n20A-n28A-n78A11 | CA_n3A-n20ACA_n3A-n28ACA_n3A-n78ACA_n20A-n28ACA_n20A-n78ACA_n28A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n20A-n41A-n71A | CA_n3A-n20ACA_n3A-n41ACA_n3A-n71ACA_n20A-n41ACA_n20A-n71ACA_n41A-n71A | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
| CA_n3A-n20A-n41A-n77A | CA_n3A-n20ACA_n3A-n41ACA_n3A-n77ACA_n20A-n41ACA_n20A-n77ACA_n41A-n77A | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n20A-n41A-n77(2A) | CA_n3A-n20ACA_n3A-n41ACA_n3A-n77ACA_n20A-n41ACA_n20A-n77ACA_n41A-n77A | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n3A-n20A-n41A-n78A | CA_n3A-n20ACA_n3A-n41ACA_n3A-n78ACA_n20A-n41ACA_n20A-n78ACA_n41A-n78A | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n20A-n67A-n78A | CA_n3A-n20ACA_n3A-n78ACA_n20A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n20A-n67A-n78(2A) | CA_n3A-n20ACA_n3A-n78ACA_n20A-n78ACA_n78(2A) | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n3A-n20A-n71A-n78A | CA_n3A-n20ACA_n3A-n71ACA_n3A-n78ACA_n20A-n71ACA_n20A-n78ACA_n71A-n78A | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n20A-n75A-n78A | CA_n3A-n20ACA_n3A-n78ACA_n20A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n20A-n75A-n78(2A) | CA_n3A-n20ACA_n3A-n78ACA_n20A-n78ACA_n78(2A) | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3A-n28A-n38A-n78A | - | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n28A-n40A-n41A | CA_n3A-n28ACA_n3A-n40ACA_n3A-n41ACA_n28A-n40ACA_n28A-n41ACA_n40A-n41A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n28A-n40A-n77A | CA_n3A-n28ACA_n3A-n40ACA_n3A-n77ACA_n28A-n40ACA_n28A-n77ACA_n40A-n77A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n40 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n28A-n40A-n77(2A) | CA_n3A-n28ACA_n3A-n40ACA_n3A-n77ACA_n28A-n40ACA_n28A-n77ACA_n40A-n77A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n40 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n3A-n28A-n40A-n78A | CA_n3A-n28ACA_n3A-n40ACA_n3A-n78ACA_n28A-n40ACA_n28A-n78ACA_n40A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n28A-n40A-n79A | CA_n3A-n28ACA_n3A-n40ACA_n3A-n79ACA_n28A-n40ACA_n28A-n79ACA_n40A-n79A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n28A-n41A-n77A | n415,6n775,6CA_n3A-n28ACA_n3A-n41A5CA_n3A-n77A5CA_n28A-n41A5CA_n28A-n77A5CA_n41A-n77A5 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n28A-n41B-n77A | CA_n3A-n28ACA_n3A-n41ACA_n3A-n77ACA_n28A-n41ACA_n28A-n77ACA_n41A-n77A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n41 | CA_n41B_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n28A-n41A-n77(2A) | n415,6n775,6CA_n3A-n28ACA_n3A-n41A5,6CA_n3A-n77A5,6CA_n28A-n41A5,6CA_n28A-n77A5,6CA_n41A-n77A5,6 | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n3 | 5, 10, 15, 20 | 1 |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n3A-n28A-n41B-n77(2A) | CA_n3A-n28ACA_n3A-n41ACA_n3A-n77ACA_n28A-n41ACA_n28A-n77ACA_n41A-n77A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | CA_n41B_BCS0 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
| CA_n3A-n28A-n41A-n78A | CA_n3A-n28ACA_n3A-n41ACA_n3A-n78ACA_n28A-n41ACA_n28A-n78ACA_n41A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n28A-n41A-n78(2A) | CA_n3A-n28ACA_n3A-n41ACA_n3A-n78ACA_n28A-n41ACA_n28A-n78ACA_n41A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n3A-n28A-n41A-n79A | n415,6n795,6CA_n3A-n28ACA_n3A-n41A5CA_n3A-n79A5CA_n28A-n41A5CA_n28A-n79A5CA_n41A-n79A5 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n3A-n28A-n75A-n78A | CA_n3A-n28ACA_n3A-n78ACA_n28A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n28A-n75A-n78(2A) | CA_n3A-n28ACA_n3A-n78ACA_n28A-n78ACA_n78(2A) | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n3A-n28A-n77A-n79A | n775,6n795,6CA_n3A-n28ACA_n3A-n77A5CA_n3A-n79A5CA_n28A-n77A5CA_n28A-n79A5CA_n77A-n79A5 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 80, 100 |  |
|  | CA_n3A-n28ACA_n3A-n77ACA_n3A-n79ACA_n28A-n77ACA_n28A-n79ACA_n77A-n79A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n28A-n77(2A)-n79A | CA_n3A-n28ACA_n3A-n77ACA_n3A-n79ACA_n28A-n77ACA_n28A-n79ACA_n77A-n79ACA_n77(2A) | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n79 | 40, 50, 80, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n28A-n77(3A)-n79A | CA_n3A-n28ACA_n3A-n77ACA_n3A-n79ACA_n28A-n77ACA_n28A-n79ACA_n77A-n79ACA_n77(2A) | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(3A)_BCS0 |  |
|  |  | n79 | 40, 50, 80, 100 |  |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS 4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n39A-n41A-n79A | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n3A-n40A-n78A-n79A | CA_n3A-n40ACA_n3A-n78ACA_n3A-n79ACA_n40A-n78ACA_n40A-n79ACA_n78A-n79A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n40A-n78A-n105A | CA_n3A-n40ACA_n3A-n78ACA_n3A-n105ACA_n40A-n78ACA_n40A-n105ACA_n78A-n105A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25,30, 35 |  |
| CA_n3A-n41A-n71A-n77A | CA_n3A-n41A CA_n3A-n71ACA_n3A-n77ACA_n41A-n71ACA_n41A-n77ACA_n71A-n77A | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n41A-n71A-n77(2A) | CA_n3A-n41A CA_n3A-n71ACA_n3A-n77ACA_n41A-n71ACA_n41A-n77ACA_n71A-n77A | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n3A-n41A-n71A-n78A | CA_n3A-n41ACA_n3A-n71ACA_n3A-n78ACA_n41A-n71ACA_n41A-n78ACA_n71A-n78A | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20, |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n41A-n71A-n78C | CA_n3A-n41ACA_n3A-n71ACA_n3A-n78ACA_n3A-n78CCA_n41A-n71ACA_n41A-n78ACA_n41A-n78CCA_n71A-n78ACA_n71A-n78C | n3 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20, |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n3A-n41A-n77A-n79A | n415,6n775,6n795,6CA_n3A-n41A5CA_n3A-n77A5CA_n3A-n79A5CA_n41A-n77A5CA_n41A-n79A5CA_n77A-n79A5 | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n3A-n41A-n77(2A)-n79A | CA_n3A-n41A CA_n3A-n77A CA_n3A-n79A CA_n41A-n77ACA_n41A-n79ACA_n77A-n79A | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |

##### Table 5.5A.3.3-1b

Table 5.5A.3.3-1b: NR CA configurations and bandwidth combinations sets defined for inter-band CA (four bands)

| NR CA configuration | Uplink CA configurationor single uplink carrier 4 | NR Band | Channel bandwidth (MHz) (NOTE 3) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n5A-n7A-n40A-n78A | CA_n5A-n7A CA_n5A-n40A CA_n5A-n78A CA_n7A-n40A CA_n7A-n78A CA_n40A-n78A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n7A-n40A-n105A | CA_n5A-n7A CA_n5A-n40A CA_n5A-n105A CA_n7A-n40A CA_n7A-n105A CA_n40A-n105A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n5A-n7A-n66A-n77A | CA_n5A-n7ACA_n5A-n66ACA_n5A-n77ACA_n7A-n66ACA_n7A-n77ACA_n66A-n77A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n7A-n66A-n77(2A) | CA_n77(2A)CA_n5A-n7ACA_n5A-n66ACA_n5A-n77ACA_n7A-n66ACA_n7A-n77ACA_n66A-n77A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n5A-n7A-n66A-n77(3A) | CA_n5A-n7ACA_n5A-n66ACA_n5A-n77ACA_n7A-n66ACA_n7A-n77ACA_n66A-n77A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n66 | 5, 10, 15, 20, 30, 40 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n5A-n7A-n78A-n105A | CA_n5A-n7A CA_n5A-n78A CA_n5A-n105A CA_n7A-n78A CA_n7A-n105A CA_n78A-n105A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n5A-n14A-n30A-n66A | CA_n5A-n14ACA_n5A-n30ACA_n5A-n66ACA_n14A-n30ACA_n14A-n66ACA_n30A-n66A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n14A-n30A-n66(2A) | CA_n5A-n14A CA_n5A-n30A CA_n5A-n66A CA_n14A-n30A CA_n14A-n66A CA_n30A-n66A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
| CA_n5A-n25A-n29A-n66A | CA_n5A-n25ACA_n5A-n66ACA_n25A-n66A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n29 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 30, 40 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n25A-n66A-n77A | n775,6CA_n5A-n25ACA_n5A-n66ACA_n5A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n25(2A)-n66A-n77A | n775,6CA_n5A-n25ACA_n5A-n66ACA_n5A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n25A-n66(2A)-n77A | n775,6CA_n5A-n25ACA_n5A-n66ACA_n5A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n25A-n66A-n77(2A) | n775,6CA_n5A-n25ACA_n5A-n66ACA_n5A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n5A-n25A-n66A-n77(3A) | CA_n5A-n25ACA_n5A-n66ACA_n5A-n77ACA_n25A-n66ACA_n25A-n77ACA_n66A-n77A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 30, 40 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n5A-n25(2A)-n66(2A)-n77A | n775,6CA_n5A-n25ACA_n5A-n66ACA_n5A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n25(2A)-n66A-n77(2A) | n775,6CA_n5A-n25ACA_n5A-n66ACA_n5A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n5A-n25A-n66(2A)-n77(2A) | n775,6CA_n5A-n25ACA_n5A-n66ACA_n5A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n5A-n25(2A)-n66(2A)-n77(2A) | n775,6CA_n5A-n25ACA_n5A-n66ACA_n5A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n5A-n25A-n66A-n78A | n785CA_n5A-n25ACA_n5A-n66ACA_n5A-n78A5CA_n25A-n66ACA_n25A-n78A5CA_n66A-n78A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n25(2A)-n66A-n78A | CA_n5A-n25ACA_n5A-n66ACA_n5A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n25A-n66(2A)-n78A | CA_n5A-n25ACA_n5A-n66ACA_n5A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n25A-n66A-n78(2A) | n785CA_n5A-n25ACA_n5A-n66ACA_n5A-n78A5CA_n25A-n66ACA_n25A-n78A5CA_n66A-n78A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n5A-n25(2A)-n66(2A)-n78A | CA_n5A-n25ACA_n5A-n66ACA_n5A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n25(2A)-n66A-n78(2A) | CA_n5A-n25ACA_n5A-n66ACA_n5A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n5A-n25A-n66(2A)-n78(2A) | CA_n5A-n25ACA_n5A-n66ACA_n5A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n5A-n25(2A)-n66(2A)-n78(2A) | CA_n5A-n25ACA_n5A-n66ACA_n5A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n5 | 5, 10, 15, 20 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n5A-n28A-n78A-n79A | CA_n5A-n28ACA_n5A-n78ACA_n5A-n79ACA_n28A-n78ACA_n28A-n79ACA_n78A-n79A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n30A-n66A-n77A | n775,6CA_n5A-n30ACA_n5A-n66ACA_n5A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n30A-n66(2A)-n77A | n775,6CA_n5A-n30ACA_n5A-n66ACA_n5A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n5A-n30A-n66(2A)-n77(2A) | n775,6CA_n5A-n30ACA_n5A-n66ACA_n5A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n5A-n30A-n66A-n77(2A) | n775,6CA_n5A-n30ACA_n5A-n66ACA_n5A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n5A-n40A-n78A-n105A | CA_n5A-n40A CA_n5A-n78A CA_n5A-n105A CA_n40A-n78A CA_n40A-n105A CA_n78A-n105A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n5A-n48A-n66A-n77A | n775,6 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n775,6CA_n5A-n48ACA_n5A-n66ACA_n5A-n77A5CA_n48A-n66ACA_n66A-n77A5 | n5 | 5, 10, 15, 20, 25 | 1 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n66A-n77A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48(2A)-n66(2A)-n77A | CA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n66A-n77A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48A-n66A-n77C | n775,6CA_n5A-n48ACA_n5A-n66ACA_n5A-n77A5CA_n48A-n66ACA_n66A-n77A5 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | CA_n77CCA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n5A-n77CCA_n48A-n66ACA_n66A-n77A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n66A-n77C | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n5A-n48A-n66(2A)-n77C | CA_n77CCA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n5A-n77CCA_n48A-n66ACA_n66A-n77ACA_n66A-n77C | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n5B-n48A-n66A-n77A | CA_n5BCA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n66A-n77A | n5 | CA_n5B_BCS 4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n48(2A)-n66A-n77A | CA_n5BCA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n66A-n77A | n5 | CA_n5B_BCS 4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n48A-n66(2A)-n77A | CA_n5BCA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n66A-n77A | n5 | CA_n5B_BCS 4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n48A-n66A-n77C | CA_n5BCA_n77CCA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n5A-n77CCA_n48A-n66ACA_n66A-n77ACA_n66A-n77C | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n5A-n48B-n66A-n77A | n775,6 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48B_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n775,6CA_n5A-n48ACA_n5A-n66ACA_n5A-n77A5CA_n48A-n66ACA_n66A-n77A5 | n5 | 5, 10, 15, 20, 25 | 1 |
|  |  | n48 | CA_n48B_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | 5, 10, 15, 20, 25 | 2 |
|  |  | n48 | CA_n48B_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | 5, 10, 15, 20, 25 | 3 |
|  |  | n48 | CA_n48B_BCS2 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n48BCA_n5A-n48ACA_n5A-n48BCA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n48B-n66ACA_n66A-n77A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5B-n48B-n66A-n77A | CA_n5BCA_n48BCA_n5A-n48ACA_n5A-n48BCA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n48B-n66ACA_n66A-n77A | n5 | CA_n5B_BCS4 and 5 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48B-n66(2A)-n77A | CA_n48BCA_n5A-n48ACA_n5A-n48BCA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n48B-n66ACA_n66A-n77A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48B_BCS4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48B-n66A-n77C | CA_n48BCA_n77CCA_n5A-n48ACA_n5A-n48BCA_n5A-n66ACA_n5A-n77ACA_n5A-n77CCA_n48A-n66ACA_n48B-n66ACA_n66A-n77A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n66A-n77C | n48 | CA_n48B_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n5A-n48(2A)-n66A-n77A | n775,6 | n5 | 5, 10, 15, 20 | 0 |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n775,6CA_n5A-n48ACA_n5A-n66ACA_n5A-n77A5CA_n48A-n66ACA_n66A-n77A5 | n5 | 5, 10, 15, 20, 25 | 1 |
|  |  | n48 | CA_n48(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n5 | 5, 10, 15, 20, 25 | 2 |
|  |  | n48 | CA_n48(2A)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n66A-n77A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48A-n66(2A)-n77A | CA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n66A-n77A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n5A-n48(2A)-n66A-n77C | CA_n77CCA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n5A-n77CCA_n48A-n66ACA_n66A-n77A | n5 | n5 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  | CA_n66A-n77C | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n7A-n8A-n28A-n40A | CA_n7A-n8ACA_n7A-n28ACA_n7A-n40ACA_n8A-n28ACA_n8A-n40ACA_n28A-n40A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n8A-n40A-n78A | CA_n7A-n8ACA_n7A-n40A CA_n7A-n78ACA_n8A-n40A CA_n8A-n78A CA_n40A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n8A-n40A-n79A | CA_n7A-n8ACA_n7A-n40ACA_n7A-n79ACA_n8A-n40ACA_n8A-n79ACA_n40A-n79A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n12A-n25A-n66A | - | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n12 | n12 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n20A-n28A-n78A11 | CA_n7A-n20ACA_n7A-n28ACA_n7A-n78ACA_n20A-n28ACA_n20A-n78ACA_n28A-n78A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n20A-n67A-n78A | CA_n7A-n20ACA_n7A-n78ACA_n20A-n78A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n20A-n67A-n78(2A) | CA_n7A-n20ACA_n7A-n78ACA_n20A-n78ACA_n78(2A) | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n7A-n20A-n75A-n78A | CA_n7A-n20ACA_n7A-n78ACA_n20A-n78A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n20A-n75A-n78(2A) | CA_n7A-n20ACA_n7A-n78ACA_n20A-n78ACA_n78(2A) | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n7A-n25A-n29A-n77A | CA_n7A-n25ACA_n7A-n77ACA_n25A-n77A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n25A-n29A-n77(2A) | CA_n7A-n25ACA_n7A-n77ACA_n25A-n77ACA_n77(2A) | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n29 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n7A-n25A-n29A-n77(3A) | CA_n7A-n25ACA_n7A-n77ACA_n25A-n77ACA_n77(2A) | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n29 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n7A-n25A-n66A-n71A | - | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | CA_n7A-n25ACA_n7A-n66ACA_n7A-n71ACA_n25A-n66ACA_n25A-n71ACA_n66A-n71A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n25A-n66A-n77A | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7(2A)-n25A-n66A-n77A | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n25(2A)-n66A-n77A | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n25A-n66(2A)-n77A | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n25A-n66A-n77(2A) | n775,6CA_n77(2A)5CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n7A-n25A-n66A-n77(3A) | CA_n7A-n25ACA_n7A-n66ACA_n7A-n77ACA_n25A-n66ACA_n25A-n77ACA_n66A-n77A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 30, 40 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n7(2A)-n25(2A)-n66A-n77A | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7(2A)-n25A-n66(2A)-n77A | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7(2A)-n25A-n66A-n77(2A) | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7A-n25(2A)-n66(2A)-n77A | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n25(2A)-n66A-n77(2A) | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7A-n25A-n66(2A)-n77(2A) | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7(2A)-n25(2A)-n66(2A)-n77A | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7(2A)-n25A-n66(2A)-n77(2A) | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7(2A)-n25(2A)-n66A-n77(2A) | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7A-n25(2A)-n66(2A)-n77(2A) | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7(2A)-n25(2A)-n66(2A)-n77(2A) | n775,6CA_n7A-n25ACA_n7A-n66ACA_n7A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n7A-n25A-n66A-n78A | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n25(2A)-n66A-n78A | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n25A-n66(2A)-n78A | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n25A-n66A-n78(2A) | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7(2A)-n25A-n66A-n78A | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n25(2A)-n66A-n78(2A) | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7A-n25(2A)-n66(2A)-n78A | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n25A-n66(2A)-n78(2A) | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7(2A)-n25(2A)-n66A-n78A | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7(2A)-n25A-n66(2A)-n78A | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7(2A)-n25A-n66A-n78(2A) | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7A-n25(2A)-n66(2A)-n78(2A) | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7(2A)-n25(2A)-n66A-n78(2A) | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7(2A)-n25(2A)-n66(2A)-n78A | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7(2A)-n25A-n66(2A)-n78(2A) | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7(2A)-n25(2A)-n66(2A)-n78(2A) | CA_n7A-n25ACA_n7A-n66ACA_n7A-n78ACA_n25A-n66ACA_n25A-n78ACA_n66A-n78A | n7 | CA_n7(2A)_BCS0 | 0 |
|  |  | n25 | CA_n25(2A)_BCS0 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n7A-n25A-n71A-n77A | CA_n7A-n25ACA_n7A-n71ACA_n7A-n77ACA_n25A-n71ACA_n25A-n77ACA_n71A-n77A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n25A-n71A-n77(2A) | CA_n7A-n25ACA_n7A-n71ACA_n7A-n77ACA_n25A-n71ACA_n25A-n77ACA_n71A-n77A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n7A-n28A-n38A-n78A7 | - | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n7A-n28A-n40A-n78A | CA_n7A-n28ACA_n7A-n40ACA_n7A-n78ACA_n28A-n40ACA_n28A-n78ACA_n40A-n78A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n28A-n40A-n79A | CA_n7A-n28ACA_n7A-n40ACA_n7A-n79ACA_n28A-n40ACA_n28A-n79ACA_n40A-n79A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n28A-n75A-n78A | CA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n28A-n75A-n78(2A) | CA_n7A-n28ACA_n7A-n78ACA_n28A-n78ACA_n78(2A) | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n7A-n29A-n66A-n77A | CA_n7A-n66ACA_n7A-n77ACA_n66A-n77A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n29A-n66A-n77(2A) | CA_n7A-n66ACA_n7A-n77ACA_n66A-n77ACA_n77(2A) | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n7A-n29A-n66A-n77(3A) | CA_n7A-n66ACA_n7A-n77ACA_n66A-n77ACA_n77(2A) | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n7A-n40A-n78A-n79A | CA_n7A-n40ACA_n7A-n78ACA_n7A-n79ACA_n40A-n78ACA_n40A-n79ACA_n78A-n79A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n40A-n78A-n105A | CA_n7A-n40ACA_n7A-n78ACA_n7A-n105ACA_n40A-n78ACA_n40A-n105ACA_n78A-n105A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 80 |  |
|  |  | n78 | 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n7A-n66A-n71A-n77A | CA_n7A-n66ACA_n7A-n71ACA_n7A-n77ACA_n66A-n71ACA_n66A-n77ACA_n71A-n77A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n66A-n71A-n77(2A) | CA_n7A-n66ACA_n7A-n71ACA_n7A-n77ACA_n66A-n71ACA_n66A-n77ACA_n71A-n77A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n7A-n66A-n71A-n77(3A) | CA_n7A-n66ACA_n7A-n71ACA_n7A-n77ACA_n66A-n71ACA_n66A-n77ACA_n71A-n77A | n7 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n66 | 5, 10, 15, 20, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20, 25, 30, 35 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n8A-n20A-n28A-n75A | CA_n8A-n20ACA_n8A-n28ACA_n20A-n28A | n8 | 5, 10, 15, 20 | 0 |
|  |  | n20 | 5, 10, 15, 20 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n75 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
| CA_n8A-n28A-n40A-n78A | CA_n8A-n28ACA_n8A-n40ACA_n8A-n78ACA_n28A-n40ACA_n28A-n78ACA_n40A-n78A | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n28A-n40A-n79A | CA_n8A-n28ACA_n8A-n40ACA_n8A-n79ACA_n28A-n40ACA_n28A-n79ACA_n40A-n79A | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n8A-n39A-n41A-n79A | - | n8 | 5, 10, 15, 20 | 0 |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n8A-n40A-n78A-n79A | CA_n8A-n40ACA_n8A-n78ACA_n8A-n79ACA_n40A-n78ACA_n40A-n79ACA_n78A-n79A | n8 | n8 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n12A-n30A-n66A-n77A | n775,6CA_n12A-n30ACA_n12A-n66ACA_n12A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n12 | 5, 10,15 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n12A-n30A-n66(2A)-n77A | n775,6CA_n12A-n30ACA_n12A-n66ACA_n12A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n12 | 5, 10,15 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n12A-n30A-n66A-n77(2A) | n775,6CA_n12A-n30ACA_n12A-n66ACA_n12A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n12 | 5, 10,15 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n12A-n30A-n66(2A)-n77(2A) | n775,6CA_n12A-n30ACA_n12A-n66ACA_n12A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n12 | 5, 10,15 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n13A-n25A-n66A-n77A | n775,6CA_n13A-n25ACA_n13A-n66ACA_n13A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n13 | 5, 10 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n13A-n25A-n66A-n77(2A) | n775,6CA_n77(2A)CA_n13A-n25ACA_n13A-n66ACA_n13A-n77A5CA_n25A-n66ACA_n25A-n77A5CA_n66A-n77A5 | n13 | 5, 10 | 0 |
|  |  | n25 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n14A-n30A-n66A-n77A | n775,6CA_n14A-n30ACA_n14A-n66ACA_n14A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n14 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n14A-n30A-n66(2A)-n77A | n775,6CA_n14A-n30ACA_n14A-n66ACA_n14A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n14 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n14A-n30A-n66A-n77(2A) | n775,6CA_n14A-n30ACA_n14A-n66ACA_n14A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n14 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n14 | n14 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n30 | n30 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n14A-n30A-n66(2A)-n77(2A) | n775,6CA_n14A-n30ACA_n14A-n66ACA_n14A-n77A5CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n14 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n18A-n28A-n41A-n77A | n415,6n775,6CA_n18A-n28ACA_n18A-n41A5,6CA_n18A-n77A5,6CA_n28A-n41A5,6CA_n28A-n77A5,6CA_n41A-n77A5,6 | n18 | 5, 10, 15 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n415,6n775,6CA_n18A-n28ACA_n18A-n41A5,6CA_n18A-n77A5,6CA_n28A-n41A5,6CA_n28A-n77A5,6CA_n41A-n77A5,6 | n18 | n18 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n20A-n41A-n71A-n78A | CA_n20A-n41ACA_n20A-n71ACA_n20A-n78ACA_n41A-n71ACA_n41A-n78ACA_n71A-n78A | n20 | 5, 10,15, 20 | 0 |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n78 | 10,15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25A-n29A-n66A-n77A | CA_n25A-n66ACA_n25A-n77ACA_n66A-n77A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n29A-n66A-n77(2A) | CA_n25A-n66ACA_n25A-n77ACA_n66A-n77ACA_n77(2A) | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n25A-n29A-n66A-n77(3A) | CA_n25A-n66ACA_n25A-n77ACA_n66A-n77ACA_n77(2A) | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n29 | n29 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS4 and 5 |  |
| CA_n25A-n38A-n66A-n78A | CA_n25A-n38ACA_n25A-n66ACA_n25A-n78ACA_n38A-n66ACA_n38A-n78ACA_n66A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25(2A)-n38A-n66A-n78A | CA_n25A-n38ACA_n25A-n66ACA_n25A-n78ACA_n38A-n66ACA_n38A-n78ACA_n66A-n78A | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25A-n38A-n66(2A)-n78A | CA_n25A-n38ACA_n25A-n66ACA_n25A-n78ACA_n38A-n66ACA_n38A-n78ACA_n66A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25A-n38A-n66A-n78(2A) | CA_n25A-n38ACA_n25A-n66ACA_n25A-n78ACA_n38A-n66ACA_n38A-n78ACA_n66A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25(2A)-n38A-n66(2A)-n78A | CA_n25A-n38ACA_n25A-n66ACA_n25A-n78ACA_n38A-n66ACA_n38A-n78ACA_n66A-n78A | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25(2A)-n38A-n66A-n78(2A) | CA_n25A-n38ACA_n25A-n66ACA_n25A-n78ACA_n38A-n66ACA_n38A-n78ACA_n66A-n78A | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25A-n38A-n66(2A)-n78(2A) | CA_n25A-n38ACA_n25A-n66ACA_n25A-n78ACA_n38A-n66ACA_n38A-n78ACA_n66A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25(2A)-n38A-n66(2A)-n78(2A) | CA_n25A-n38ACA_n25A-n66ACA_n25A-n78ACA_n38A-n66ACA_n38A-n78ACA_n66A-n78A | n25 | CA_n25(2A)_BCS0 | 0 |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25A-n41A-n66A-n71A | - | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | n255n415,6n665n715CA_n25A-n41A5,9,10CA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5,9,10CA_n41A-n71A5,9,10CA_n66A-n71A5 | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(A-C)-n66A-n71A | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n41CCA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41C-n66ACA_n41A-n71A5CA_n41C-n71ACA_n41C5CA_n66A-n71A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n66(2A)-n71A | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41A-n71A5CA_n66A-n71A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n66(2A)-n71(2A) | n415,6CA_n25A-n41A5 CA_n25A-n66A CA_n25A-n71A CA_n41A-n66A5 CA_n41A-n71A5 CA_n66A-n71A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25A-n41A-n66(2A)-n71B | n415,6CA_n25A-n41A5 CA_n25A-n66A CA_n25A-n71A CA_n41A-n66A5 CA_n41A-n71A5 CA_n66A-n71A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25A-n41A-n66A-n71(2A) | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41A-n71A5CA_n66A-n71A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25A-n41A-n66A-n71B | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41A-n71A5CA_n66A-n71A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25A-n41(2A)-n66A-n71A | - | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | CA_n41(2A)_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41A-n71A5CA_n66A-n71A5 | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(2A)-n66A-n71(2A) | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41A-n71A5CA_n66A-n71A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25A-n41(2A)-n66A-n71B | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41A-n71A5CA_n66A-n71A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25A-n41(2A)-n66(2A)-n71A | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41A-n71A5CA_n66A-n71A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41C-n66A-n71A | - | n25 | 5, 10, 15, 20 | 0 |
|  |  | n41 | CA_n41C_BCS0 |  |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n41CCA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41C-n66ACA_n41A-n71A5CA_n41C-n71ACA_n41C5CA_n66A-n71A5 | n25 | 5, 10, 15, 20, 25, 30, 40 | 1 |
|  |  | n41 | CA_n41C_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41C-n66A-n71(2A) | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n41CCA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41C-n66ACA_n41A-n71A5CA_n41C-n71ACA_n41C5CA_n66A-n71A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25A-n41C-n66A-n71B | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n41CCA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41C-n66ACA_n41A-n71A5CA_n41C-n71ACA_n41C5CA_n66A-n71A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25A-n41C-n66(2A)-n71A | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n41CCA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41C-n66ACA_n41A-n71A5CA_n41C-n71ACA_n41C5CA_n66A-n71A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A-n66A-n71A | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41A-n71A5CA_n66A-n71A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A-n66A-n71(2A) | n415,6CA_n25A-n41A5 CA_n25A-n66A CA_n25A-n71A CA_n41A-n66A5 CA_n41A-n71A5 CA_n66A-n71A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41A-n66A-n71B | n415,6CA_n25A-n41A5 CA_n25A-n66A CA_n25A-n71A CA_n41A-n66A5 CA_n41A-n71A5 CA_n66A-n71A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
| CA_n25(2A)-n41A-n66(2A)-n71A | n415,6CA_n25A-n41A5 CA_n25A-n66A CA_n25A-n71A CA_n41A-n66A5 CA_n41A-n71A5 CA_n66A-n71A | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41(2A)-n66A-n71A | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41A-n71A5CA_n66A-n71A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41C-n66A-n71A | n255n415,6n665n715CA_n25A-n41A5CA_n25A-n41CCA_n25A-n66A5CA_n25A-n71A5CA_n41A-n66A5CA_n41C-n66ACA_n41A-n71A5CA_n41C-n71ACA_n41C5CA_n66A-n71A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(3A)-n66A-n71A | n255n415,6n665n715CA_n25A-n41A5 CA_n25A-n66A5 CA_n25A-n71A5 CA_n41A-n66A5 CA_n41A-n71A5 CA_n66A-n71A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n66A-n77A | n255n415,6n665n775,6CA_n25A-n41A5,6CA_n25A-n66A5CA_n25A-n77A5,6CA_n41A-n66A5,6CA_n41A-n77A5,6CA_n66A-n77A5,6 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(A-C)-n66A-n77A | n415,6n775,6CA_n25A-n41A5CA_n25A-n41CCA_n25A-n66ACA_n25A-n77A5CA_n41C5CA_n41A-n66A5CA_n41C-n66ACA_n41A-n77A5CA_n41C-n77ACA_n66A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41C-n66A-n77A | n255n415,6n665n775,6CA_n25A-n41A5CA_n25A-n41CCA_n25A-n66A5CA_n25A-n77A5CA_n41A-n66A5CA_n41A-n77A5CA_n41C5CA_n41C-n66ACA_n41C-n77ACA_n66A-n77A5 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | CA_n41C_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41C-n66A-n77(2A) | CA_n25A-n41ACA_n25A-n66ACA_n25A-n77ACA_n41CCA_n41A-n66ACA_n41A-n77ACA_n66A-n77A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n41C-n66(2A)-n77A | n255n415,6n665n775,6CA_n25A-n41A5 CA_n25A-n41CCA_n25A-n66A5 CA_n25A-n77A5 CA_n41A-n66A5 CA_n41C-n66ACA_n41A-n77A5 CA_n41C-n77ACA_n41C5 CA_n66A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(2A)-n66A-n77A | n255n415,6n665n775,6CA_n25A-n41A5CA_n25A-n66A5CA_n25A-n77A5CA_n41A-n66A5CA_n41A-n77A5CA_n66A-n77A5 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(2A)-n66A-n77(2A) | CA_n25A-n41ACA_n25A-n66ACA_n25A-n77ACA_n41A-n66ACA_n41A-n77ACA_n66A-n77A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n41(3A)-n66A-n77A | n415,6n775,6CA_n25A-n41A5CA_n25A-n66ACA_n25A-n77A5CA_n41A-n66A5CA_n41A-n77A5CA_n66A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n66(2A)-n77A | n255n415,6n665n775,6CA_n25A-n41A5CA_n25A-n66A5CA_n25A-n77A5CA_n41A-n66A5CA_n41A-n77A5CA_n66A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n66A-n77(2A) | n415,6n775,6CA_n25A-n41A5CA_n25A-n66ACA_n25A-n77A5CA_n41A-n66A5CA_n41A-n77A5CA_n66A-n77A5 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n41A-n66(2A)-n77(2A) | n415,6n775,6CA_n25A-n41A5 CA_n25A-n66A CA_n25A-n77A5 CA_n41A-n66A5 CA_n41A-n77A5 CA_n66A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n41(2A)-n66(2A)-n77A | n255n415,6n665n775,6CA_n25A-n41A5 CA_n25A-n66A5 CA_n25A-n77A5 CA_n41A-n66A5 CA_n41A-n77A5 CA_n66A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A-n66A-n77A | n255n415,6n665n775,6CA_n25A-n41A5CA_n25A-n66A5CA_n25A-n77A5CA_n41A-n66A5CA_n41A-n77A5CA_n66A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A-n66A-n77(2A) | n415,6n775,6CA_n25A-n41A5 CA_n25A-n66A CA_n25A-n77A5 CA_n41A-n66A5 CA_n41A-n77A5 CA_n66A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41A-n66(2A)-n77A | n255n415,6n665n775,6CA_n25A-n41A5CA_n25A-n66A5CA_n25A-n77A5CA_n41A-n66A5CA_n41A-n77A5CA_n66A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41C-n66A-n77A | n255n415,6n665n775,6CA_n25A-n41A5 CA_n25A-n41CCA_n25A-n66A5 CA_n25A-n77A5 CA_n41A-n66A5 CA_n41C-n66ACA_n41A-n77A5 CA_n41C-n77ACA_n66A-n77A5CA_n41C5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41(2A)-n66A-n77A | n255n415,6n665n775,6CA_n25A-n41A5 CA_n25A-n66A5 CA_n25A-n77A5 CA_n41A-n66A5 CA_n41A-n77A5 CA_n66A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n66A-n78A | CA_n25A-n41ACA_n25A-n66ACA_n25A-n78ACA_n41A-n66ACA_n41A-n78ACA_n66A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25A-n41A-n66A-n78(2A) | CA_n25A-n41ACA_n25A-n66ACA_n25A-n78ACA_n41A-n66ACA_n41A-n78ACA_n66A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25A-n41A-n66A-n85A | CA_n25A-n41ACA_n25A-n66ACA_n25A-n85ACA_n41A-n66ACA_n41A-n85ACA_n66A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n71A-n77A | n255n415,6n715n775,6CA_n25A-n41A5,6CA_n25A-n71A5CA_n25A-n77A5,6CA_n41A-n71A5,6CA_n41A-n77A5,6CA_n71A-n77A5,6 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n71A-n77(2A) | n415,6n775,6CA_n25A-n41A5CA_n25A-n71ACA_n25A-n77A5CA_n41A-n71A5CA_n41A-n77A5CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n41A-n71B-n77A | n255n415,6n715n775,6CA_n25A-n41A5CA_n25A-n71A5CA_n25A-n77A5CA_n41A-n71A5CA_n41A-n77A5CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n71B-n77(2A) | n415,6n775,6CA_n25A-n41A5 CA_n25A-n71A CA_n25A-n77A5 CA_n41A-n71A5 CA_n41A-n77A5 CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n41A-n71(2A)-n77A | n255n415,6n715n775,6CA_n25A-n41A5CA_n25A-n71A5CA_n25A-n77A5CA_n41A-n71A5CA_n41A-n77A5CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n71(2A)-n77(2A) | n415,6n775,6CA_n25A-n41A5 CA_n25A-n71A CA_n25A-n77A5 CA_n41A-n71A5 CA_n41A-n77A5 CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n41(A-C)-n71A-n77A | n415,6n775,6CA_n25A-n41A5CA_n25A-n41CCA_n25A-n71ACA_n25A-n77A5CA_n41C5CA_n41A-n71A5CA_n41C-n71ACA_n41A-n77A5CA_n41C-n77ACA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(A-C)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41C-n71A-n77A | n255n415,6n715n775,6CA_n25A-n41A5CA_n25A-n41CCA_n25A-n71A5CA_n25A-n77A5CA_n41A-n71A5CA_n41A-n77A5CA_n41C5CA_n41C-n71ACA_n41C-n77ACA_n71A-n77A5 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | CA_n41C_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41C-n71A-n77(2A) | CA_n25A-n41ACA_n25A-n71ACA_n25A-n77ACA_n41CCA_n41A-n71ACA_n41A-n77ACA_n71A-n77A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n41C-n71B-n77A | n255n415,6n715n775,6CA_n25A-n41A5 CA_n25A-n41CCA_n25A-n71A5 CA_n25A-n77A5 CA_n41A-n71A5 CA_n41C-n71ACA_n41A-n77A5 CA_n41C-n77ACA_n41C5 CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41C-n71(2A)-n77A | n255n415,6n715n775,6CA_n25A-n41A5 CA_n25A-n41CCA_n25A-n71A5 CA_n25A-n77A5 CA_n41A-n71A5 CA_n41C-n71ACA_n41A-n77A5 CA_n41C-n77ACA_n41C5 CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(2A)-n71A-n77A | n255n415,6n715n775,6CA_n25A-n41A5CA_n25A-n71A5CA_n25A-n77A5CA_n41A-n71A5CA_n41A-n77A5CA_n71A-n77A5 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | CA_n41(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(2A)-n71A-n77(2A) | CA_n25A-n41ACA_n25A-n71ACA_n25A-n77ACA_n41A-n71ACA_n41A-n77ACA_n71A-n77A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n41(3A)-n71A-n77A | n415,6n775,6CA_n25A-n41A5CA_n25A-n71ACA_n25A-n77A5CA_n41A-n71A5CA_n41A-n77A5CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(3A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(2A)-n71B-n77A | n255n415,6n715n775,6CA_n25A-n41A5 CA_n25A-n71A5 CA_n25A-n77A5 CA_n41A-n71A5 CA_n41A-n77A5 CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(2A)-n71(2A)-n77A | n255n415,6n715n775,6CA_n25A-n41A5 CA_n25A-n71A5 CA_n25A-n77A5 CA_n41A-n71A5 CA_n41A-n77A5 CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A-n71A-n77A | n255n415,6n715n775,6CA_n25A-n41A5CA_n25A-n71A5CA_n25A-n77A5CA_n41A-n71A5CA_n41A-n77A5CA_n71A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A-n71(2A)-n77A | n255n415,6n715n775,6CA_n25A-n41A5CA_n25A-n71A5CA_n25A-n77A5CA_n41A-n71A5CA_n41A-n77A5CA_n71A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A-n71B-n77A | n255n415,6n715n775,6CA_n25A-n41A5CA_n25A-n71A5CA_n25A-n77A5CA_n41A-n71A5CA_n41A-n77A5CA_n71A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A-n71A-n77(2A) | n415,6n775,6CA_n25A-n41A5 CA_n25A-n71A CA_n25A-n77A5 CA_n41A-n71A5 CA_n41A-n77A5 CA_n71A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n41C-n71A-n77A | n255n415,6n715n775,6CA_n25A-n41A5 CA_n25A-n41CCA_n25A-n71A5 CA_n25A-n77A5 CA_n41A-n71A5 CA_n41C-n71ACA_n41A-n77A5 CA_n41C-n77ACA_n71A-n77A5CA_n41C5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41(2A)-n71A-n77A | n255n415,6n715n775,6CA_n25A-n41A5 CA_n25A-n71A5 CA_n25A-n77A5 CA_n41A-n71A5 CA_n41A-n77A5 CA_n71A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n71A-n78A | CA_n25A-n41ACA_n25A-n71ACA_n25A-n78ACA_n41A-n71ACA_n41A-n78ACA_n71A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25A-n41A-n71A-n85A | CA_n25A-n41ACA_n25A-n71ACA_n25A-n85ACA_n41A-n71ACA_n41A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n77A-n85A | CA_n25A-n41A CA_n25A-n77A CA_n25A-n85A CA_n41A-n77A CA_n41A-n85A CA_n77A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66A-n71A-n77A | n255n665n715n775,6CA_n25A-n66A5CA_n25A-n71A5CA_n25A-n77A5,9,10CA_n66A-n71A5CA_n66A-n77A5,9,10CA_n71A-n77A5,9,10 | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66(2A)-n71A-n77A | n255n665n715n775,6CA_n25A-n66A5CA_n25A-n71A5CA_n25A-n77A5CA_n66A-n71A5CA_n66A-n77A5CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66(2A)-n71A-n77(2A) | n775,6CA_n25A-n66ACA_n25A-n71ACA_n25A-n77A5CA_n66A-n71ACA_n66A-n77A5CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n66A-n71B-n77A | n255n665n715n775,6CA_n25A-n66A5CA_n25A-n71A5CA_n25A-n77A5CA_n66A-n71A5CA_n66A-n77A5CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66A-n71(2A)-n77A | n255n665n715n775,6CA_n25A-n66A5CA_n25A-n71A5CA_n25A-n77A5CA_n66A-n71A5CA_n66A-n77A5CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66A-n71A-n77(2A) | n775,6CA_n25A-n66ACA_n25A-n71ACA_n25A-n77A5CA_n66A-n71ACA_n66A-n77A5CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n66A-n71A-n77(3A) | CA_n25A-n66ACA_n25A-n71ACA_n25A-n77ACA_n66A-n71ACA_n66A-n77ACA_n71A-n77A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20, 25, 30, 35 |  |
|  |  | n77 | CA_n77(3A)_BCS1 |  |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS 4 and 5 |  |
| CA_n25A-n66A-n71(2A)-n77(2A) | n775,6CA_n25A-n66ACA_n25A-n71ACA_n25A-n77A5CA_n66A-n71ACA_n66A-n77A5CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n66A-n71B-n77(2A) | n775,6CA_n25A-n66ACA_n25A-n71ACA_n25A-n77A5CA_n66A-n71ACA_n66A-n77A5CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n66(2A)-n71(2A)-n77A | n775,6CA_n25A-n66A CA_n25A-n71A CA_n25A-n77A5 CA_n66A-n71A CA_n66A-n77A5 CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66(2A)-n71B-n77A | n775,6CA_n25A-n66A CA_n25A-n71A CA_n25A-n77A5 CA_n66A-n71A CA_n66A-n77A5 CA_n71A-n77A5 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n66A-n71A-n77A | n255n665n715n775,6CA_n25A-n66A5CA_n25A-n71A5CA_n25A-n77A5CA_n66A-n71A5CA_n66A-n77A5CA_n71A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n66A-n71A-n77(2A) | n775,6CA_n25A-n66ACA_n25A-n71ACA_n25A-n77A5CA_n66A-n71ACA_n66A-n77A5CA_n71A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25(2A)-n66A-n71(2A)-n77A | n775,6CA_n25A-n66A CA_n25A-n71A CA_n25A-n77A5 CA_n66A-n71A CA_n66A-n77A5 CA_n71A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n66A-n71B-n77A | n775,6CA_n25A-n66A CA_n25A-n71A CA_n25A-n77A5 CA_n66A-n71A CA_n66A-n77A5 CA_n71A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n66(2A)-n71A-n77A | n775,6CA_n25A-n66A CA_n25A-n71A CA_n25A-n77A5 CA_n66A-n71A CA_n66A-n77A5 CA_n71A-n77A5 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66A-n71A-n78A | CA_n25A-n66ACA_n25A-n71ACA_n25A-n78ACA_n66A-n71ACA_n66A-n78ACA_n71A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25A-n66(2A)-n71A-n78A | CA_n25A-n66ACA_n25A-n71ACA_n25A-n78ACA_n66A-n71ACA_n66A-n78ACA_n71A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n25A-n66A-n71A-n78(2A) | CA_n25A-n66ACA_n25A-n71ACA_n25A-n78ACA_n66A-n71ACA_n66A-n78ACA_n71A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25A-n66(2A)-n71A-n78(2A) | CA_n25A-n66ACA_n25A-n71ACA_n25A-n78ACA_n66A-n71ACA_n66A-n78ACA_n71A-n78A | n25 | 5, 10, 15, 20, 25, 30, 40 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n25A-n66A-n71A-n85A | CA_n25A-n66A CA_n25A-n71A CA_n25A-n85A CA_n66A-n71A CA_n66A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n66A-n77A-n85A | CA_n25A-n66ACA_n25A-n77ACA_n25A-n85ACA_n66A-n77ACA_n66A-n85ACA_n77A-n85A | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n40A-n71A-n77A | CA_n28A-n40ACA_n28A-n77ACA_n40A-n71ACA_n40A-n77ACA_n71A-n77A | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n40A-n78A-n79A | CA_n28A-n40ACA_n28A-n78ACA_n28A-n79ACA_n40A-n78ACA_n40A-n79ACA_n78A-n79A | n28 | n28 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n28A-n41A-n75A-n78A | - | n28 | 5,10, 15, 20, 25,30 | 0 |
|  |  | n41 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n75 | 5,10, 15, 20, 25,30,40,50 |  |
|  |  | n78 | 10, 15, 20, 25,30,40, 50, 60,70, 80, 90, 100 |  |
| CA_n28A-n41A-n77A-n79A | n415,6n775,6n795,6CA_n28A-n41A5CA_n28A-n77A5CA_n28A-n79A5CA_n41A-n77A5CA_n41A-n79A5CA_n77A-n79A5 | n28 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n28A-n41A-n77(2A)-n79A | CA_n28A-n41ACA_n28A-n77ACA_n28A-n79ACA_n41A-n77ACA_n41A-n79ACA_n77A-n79A | n28 | 5, 10, 15, 20 | 0 |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS0 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n29A-n30A-n66A-n77A | n775,6CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n29 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n29A-n30A-n66(2A)-n77A | n775,6CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n29 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n29A-n30A-n66A-n77(2A) | n775,6CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n29 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n29A-n30A-n66(2A)-n77(2A) | n775,6CA_n30A-n66ACA_n30A-n77A5CA_n66A-n77A5 | n29 | 5, 10 | 0 |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n29A-n66A-n70A-n71A | n665n705n715CA_n66A-n71ACA_n70A-n71A | n29 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 40 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | CA_n66A-n71ACA_n70A-n71A | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n66(2A)-n70A-n71A | n665n705n715CA_n66A-n71ACA_n70A-n71A | n29 | 5, 10 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n70 | 5, 10, 15, 201, 251 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  | CA_n66A-n71ACA_n70A-n71A | n29 | n29 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n70 | n70 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
| CA_n29A-n66A-n70A-n71(2A) | CA_n66A-n71A CA_n70A-n71A | n29 | 5, 10 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
| CA_n41A-n66A-n70A-n78A | CA_n41A-n66ACA_n41A-n70ACA_n41A-n78ACA_n66A-n78ACA_n70A-n78A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | 10, 15, 20, 25, 30, 40 |  |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n41A-n66A-n71A-n77A | n415,6n665n715n775,6CA_n41A-n66A5,6CA_n41A-n71A5,6CA_n41A-n77A5,6CA_n66A-n71A5CA_n66A-n77A5,6CA_n71A-n77A5,6 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66A-n71B-n77A | n415,6n665n715n775,6CA_n41A-n66A5CA_n41A-n71A5CA_n41A-n77A5CA_n66A-n71A5CA_n66A-n77A5CA_n71A-n77A5 | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66A-n71B-n77(2A) | n415,6n775,6CA_n41A-n66A5CA_n41A-n71A5CA_n41A-n77A5CA_n66A-n71ACA_n66A-n77A5CA_n71A-n77A5 | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41A-n66A-n71(2A)-n77A | n415,6n665n715n775,6CA_n41A-n66A5CA_n41A-n71A5CA_n41A-n77A5CA_n66A-n71A5CA_n66A-n77A5CA_n71A-n77A5 | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66A-n71(2A)-n77(2A) | n415,6n775,6CA_n41A-n66A5 CA_n41A-n71A5 CA_n41A-n77A5 CA_n66A-n71A CA_n66A-n77A5 CA_n71A-n77A5 | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41A-n66(2A)-n71A-n77(2A) | n415,6n775,6CA_n41A-n66A5 CA_n41A-n71A5 CA_n41A-n77A5 CA_n66A-n71A CA_n66A-n77A5 CA_n71A-n77A5 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41(A-C)-n66A-n71A-n77A | n415,6n775,6CA_n41C5CA_n41A-n66A5CA_n41C-n66ACA_n41A-n71A5CA_n41C-n71ACA_n41A-n77A5CA_n41C-n77ACA_n66A-n71ACA_n66A-n77A5CA_n71A-n77A5 | n41 | CA_n41(A-C)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n66A-n71A-n77A | n415,6n665n715n775,6CA_n41A-n66A5CA_n41A-n71A5CA_n41A-n77A5CA_n41C5CA_n41C-n66ACA_n41C-n71ACA_n41C-n77ACA_n66A-n71A5CA_n66A-n77A5CA_n71A-n77A5 | n41 | CA_n41C_BCS1 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n66A-n71A-n77(2A) | CA_n41C CA_n41A-n66ACA_n41A-n71ACA_n41A-n77ACA_n66A-n71ACA_n66A-n77ACA_n71A-n77A | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41C-n66A-n71B-n77A | n415,6n665n715n775,6CA_n41C5CA_n41A-n66A5 CA_n41C-n66ACA_n41A-n71A5 CA_n41C-n71ACA_n41A-n77A5 CA_n41C-n77ACA_n66A-n71A5 CA_n66A-n77A5 CA_n71A-n77A5 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n66A-n71(2A)-n77A | n415,6n665n715n775,6CA_n41C5CA_n41A-n66A5 CA_n41C-n66ACA_n41A-n71A5 CA_n41C-n71ACA_n41A-n77A5 CA_n41C-n77ACA_n66A-n71A5 CA_n66A-n77A5 CA_n71A-n77A5 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41C-n66(2A)-n71A-n77A | n415,6n665n715n775,6CA_n41C5CA_n41A-n66A5 CA_n41C-n66ACA_n41A-n71A5 CA_n41C-n71ACA_n41A-n77A5 CA_n41C-n77ACA_n66A-n71A5 CA_n66A-n77A5 CA_n71A-n77A5 | n41 | CA_n41C_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n66A-n71A-n77(2A) | CA_n41A-n66ACA_n41A-n71ACA_n41A-n77ACA_n66A-n71ACA_n66A-n77ACA_n71A-n77A | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41(3A)-n66A-n71A-n77A | n415,6n775,6CA_n41A-n66A5CA_n41A-n71A5CA_n41A-n77A5CA_n66A-n71ACA_n66A-n77A5CA_n71A-n77A5 | n41 | CA_n41(3A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n66A-n71A-n77A | n415,6n665n715n775,6CA_n41A-n66A5CA_n41A-n71A5CA_n41A-n77A5CA_n66A-n71A5CA_n66A-n77A5CA_n71A-n77A5 | n41 | CA_n41(2A)_BCS1 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n66A-n71B-n77A | n415,6n66A5n71A5n775,6CA_n41A-n66A5 CA_n41A-n71A5 CA_n41A-n77A5 CA_n66A-n71A5 CA_n66A-n77A5 CA_n71A-n77A5 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n66A-n71(2A)-n77A | n415,6n665n715n775,6CA_n41A-n66A5 CA_n41A-n71A5 CA_n41A-n77A5 CA_n66A-n71A5 CA_n66A-n77A5 CA_n71A-n77A5 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41(2A)-n66(2A)-n71A-n77A | n415,6n665n715n775,6CA_n41A-n66A5 CA_n41A-n71A5 CA_n41A-n77A5 CA_n66A-n71A5 CA_n66A-n77A5 CA_n71A-n77A5 | n41 | CA_n41(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66(2A)-n71A-n77A | n415,6n665n715n775,6CA_n41A-n66A5CA_n41A-n71A5CA_n41A-n77A5CA_n66A-n71A5CA_n66A-n77A5CA_n71A-n77A5 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66(2A)-n71(2A)-n77A | n415,6n66A5n71A5n775,6CA_n41A-n66A5CA_n41A-n71A5CA_n41A-n77A5CA_n66A-n71A5CA_n66A-n77A5CA_n71A-n77A5 | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66(2A)-n71B-n77A | n415,6n665n715n775,6CA_n41A-n66A5CA_n41A-n71A5CA_n41A-n77A5CA_n66A-n71A5CA_n66A-n77A5CA_n71A-n77A5 | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66A-n71A-n77(2A) | n415,6n775,6CA_n41A-n66A5CA_n41A-n77A5CA_n41A-n71A5CA_n66A-n71ACA_n66A-n77A5CA_n71A-n77A5 | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n41A-n66A-n71A-n78A | CA_n41A-n66ACA_n41A-n71ACA_n41A-n78ACA_n66A-n71ACA_n66A-n78ACA_n71A-n78A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n41A-n66(2A)-n71A-n78A | CA_n41A-n66ACA_n41A-n71ACA_n41A-n78ACA_n66A-n71ACA_n66A-n78ACA_n71A-n78A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n41A-n66A-n71A-n78(2A) | CA_n41A-n66ACA_n41A-n71ACA_n41A-n78ACA_n66A-n71ACA_n66A-n78ACA_n71A-n78A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n41A-n66(2A)-n71A-n78(2A) | CA_n41A-n66ACA_n41A-n71ACA_n41A-n78ACA_n66A-n71ACA_n66A-n78ACA_n71A-n78A | n41 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n41A-n66A-n71A-n85A | CA_n41A-n66ACA_n41A-n71ACA_n41A-n85ACA_n66A-n71ACA_n66A-n85A | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n41A-n66A-n77A-n85A | CA_n41A-n66A CA_n41A-n77A CA_n41A-n85A CA_n66A-n77A CA_n66A-n85A CA_n77A-n85A | n41 | n41 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n85 | n85 channel bandwidths in Table 5.3.5-1 |  |
| CA_n48A-n66A-n70A-n71A | CA_n48A-n66A CA_n48A-n70A CA_n48A-n71A CA_n66A-n71A CA_n70A-n71A | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
| CA_n48A-n66A-n70A-n77A | CA_n48A-n66A CA_n48A-n70A CA_n66A-n77A CA_n70A-n77A | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48A-n66(2A)-n70A-n77A | CA_n48A-n66ACA_n48A-n70ACA_n66A-n77ACA_n70A-n77A | n48 | 5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(2A)-n66(2A)-n70A-n77A | CA_n48A-n66A CA_n48A-n70A CA_n66A-n77A CA_n70A-n77A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48A-n66(3A)-n70A-n77A | CA_n48A-n66A CA_n48A-n70A CA_n66A-n77A CA_n70A-n77A | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(2A)-n66A-n70A-n77A | CA_n48A-n66ACA_n48A-n70ACA_n66A-n77ACA_n70A-n77A | n48 | CA_n48(2A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(3A)-n66A-n70A-n77A | CA_n48A-n66A CA_n48A-n70A CA_n66A-n77A CA_n70A-n77A | n48 | CA_n48(3A)_BCS0 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48A-n66A-n71A-n77A | CA_n48A-n66A CA_n48A-n71A CA_n66A-n71A CA_n66A-n77A CA_n71A-n77A | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(2A)-n66A-n71A-n77A | CA_n48A-n66A CA_n48A-n71A CA_n66A-n71A CA_n66A-n77A CA_n71A-n77A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(2A)-n66A-n71(2A)-n77A | CA_n48A-n66A CA_n48A-n71A CA_n66A-n71A CA_n66A-n77A CA_n71A-n77A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48A-n66(2A)-n71A-n77A | CA_n48A-n66A CA_n48A-n71A CA_n66A-n71A CA_n66A-n77A CA_n71A-n77A | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 | 0 |
|  |  | n66 | CA_n66(2A)_BCS0 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 | 1 |
|  |  | n66 | CA_n66(2A)_BCS1 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48A-n66(3A)-n71A-n77A | CA_n48A-n66A CA_n48A-n71A CA_n66A-n71A CA_n66A-n77A CA_n71A-n77A | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 | 0 |
|  |  | n66 | CA_n66(3A)_BCS0 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48A-n66A-n71(2A)-n77A | CA_n48A-n66A CA_n48A-n71A CA_n66A-n71A CA_n66A-n77A CA_n71A-n77A | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 | 0 |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48A-n70A-n71A-n77A | CA_n48A-n70A CA_n48A-n71A CA_n70A-n71A CA_n70A-n77A CA_n71A-n77A | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(2A)-n70A-n71A-n77A | CA_n48A-n70A CA_n48A-n71A CA_n70A-n71A CA_n70A-n77A CA_n71A-n77A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48A-n70A-n71(2A)-n77A | CA_n48A-n70A CA_n48A-n71A CA_n70A-n71A CA_n70A-n77A CA_n71A-n77A | n48 | 5, 10, 15, 20, 30, 40, 508, 608, 708, 808, 908, 1008 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n48(2A)-n70A-n71(2A)-n77A | CA_n48A-n70A CA_n48A-n71A CA_n70A-n71A CA_n70A-n77A CA_n71A-n77A | n48 | CA_n48(2A)_BCS1 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n71 | CA_n71(2A)_BCS0 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n66A-n70A-n71A-n77A | CA_n66A-n71A CA_n66A-n77A CA_n70A-n71A CA_n70A-n77A CA_n71A-n77A | n66 | 5, 10, 15, 20, 25, 30, 35, 40 | 0 |
|  |  | n70 | 5, 10, 15, 20, 25 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |

The following notes are applied to the above tables.

NOTE 1: This UE channel bandwidth is optional in this release of the specification.

NOTE 2: For the 20 MHz bandwidth, the minimum requirements are specified for NR UL carrier frequencies confined to either 713-723 MHz or 728-738 MHz. For the 30MHz bandwidth, the minimum requirements are specified for NR UL transmission bandwidth configuration confined to either 703-733 or 718-748 MHz.

NOTE 3: For each channel bandwidth of each component carrier, refer to Table 5.3.5-1 for the applicable SCSs. For a given band, not all UE channel bandwidths support the same SCSs.

NOTE 4:  Only single uplink carriers with power class other than PC3 are listed.

NOTE 5: Minimum requirements for Power Class 2 are applicable for this uplink combination or single uplink carrier in this downlink/uplink combination.

NOTE 6: Minimum requirements for Power Class 1.5 are applicable for this uplink combination or single uplink carrier in this downlink/uplink combination.

NOTE 7: For a band combination which includes band n7 and n38 simultaneously, carriers in band n7 and n38 can only be configured as downlink carriers. Power imbalance between downlink carriers on Band n7 and Band n38 is assumed to be within 6dB.

NOTE 8: For this bandwidth, the minimum requirements are restricted to operation when carrier is configured as a downlink SCell part of CA configuration

NOTE 9: Minimum requirements for Power Class 2 are applicable for this uplink configuration with 1Tx antenna connector in one band and 2Tx antenna connectors in the other band.

NOTE 10: Minimum requirements for Power Class 1.5 are applicable for this uplink configuration with 1Tx antenna connector in one band and 2Tx antenna connectors in the other band.

NOTE 11: The frequency range in band n28 is restricted for this band combination to 703- 733 MHz for the UL and 758-788 MHz for the DL.

#### 5.5A.3.4 Configurations for inter-band CA (five bands)

Table 5.5A.3.4-1: NR CA configurations and bandwidth combinations sets defined for inter-band CA (five bands)

| NR CA configuration | Uplink configurationor single uplink carrier 2 | NR Band | Channel bandwidth (MHz) (NOTE 1) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n1A-n3A-n5A-n7A-n78A | CA_n1A-n3ACA_n1A-n5ACA_n1A-n7ACA_n1A-n78ACA_n3A-n5ACA_n3A-n7ACA_n3A-n78ACA_n5A-n7ACA_n5A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n5A-n7B-n78A | CA_n1A-n3ACA_n1A-n5ACA_n1A-n7ACA_n1A-n78ACA_n3A-n5ACA_n3A-n7ACA_n3A-n78ACA_n5A-n7ACA_n5A-n78ACA_n7A-n78ACA_n7B | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n5A-n28A-n78A | CA_n1A-n3ACA_n1A-n5ACA_n1A-n28ACA_n1A-n79ACA_n3A-n5ACA_n3A-n28ACA_n3A-n79ACA_n5A-n28ACA_n5A-n79ACA_n28A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7A-n8A-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n8ACA_n1A-n78ACA_n3A-n7ACA_n3A-n8ACA_n3A-n78ACA_n7A-n8ACA_n7A-n78ACA_n8A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 40, 50, 60, 80, 90, 100 |  |
| CA_n1A-n3(2A)-n7A-n8A-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n8ACA_n1A-n78ACA_n3A-n7ACA_n3A-n8ACA_n3A-n78ACA_n7A-n8ACA_n7A-n78ACA_n8A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7(2A)-n8A-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n8ACA_n1A-n78ACA_n3A-n7ACA_n3A-n8ACA_n3A-n78ACA_n7A-n8ACA_n7A-n78ACA_n8A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3(2A)-n7(2A)-n8A-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n8ACA_n1A-n78ACA_n3A-n7ACA_n3A-n8ACA_n3A-n78ACA_n7A-n8ACA_n7A-n78ACA_n8A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3(2A)_BCS0 |  |
|  |  | n7 | CA_n7(2A)_BCS0 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7A-n20A-n67A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n20ACA_n3A-n7ACA_n3A-n20ACA_n7A-n20A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7A-n20A-n75A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n20ACA_n3A-n7ACA_n3A-n20ACA_n7A-n20A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7A-n20A-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n20ACA_n1A-n78ACA_n3A-n7ACA_n3A-n20ACA_n3A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7A-n20A-n78(2A) | CA_n1A-n3ACA_n1A-n7ACA_n1A-n20ACA_n1A-n78ACA_n3A-n7ACA_n3A-n20ACA_n3A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3A-n7A-n26A-n78A | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7A-n26(2A)-n78A | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n26(2A) | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7A-n26A-n78(2A) | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3A-n7A-n26A-n78C | CA_n78CCA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3A-n7A-n26(2A)-n78(2A) | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n26(2A) | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  | CA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n1A-n3A-n7A-n26(2A)-n78C | CA_n26(2A)CA_n78CCA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3B-n7A-n26A-n78A | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3B-n7A-n26(2A)-n78A | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n26(2A) | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3B-n7A-n26A-n78(2A) | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | CA_n3B_BCS 4 and 5 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3B-n7A-n26A-n78C | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n3B-n7A-n26(2A)-n78(2A) | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n26(2A) | n3 | CA_n3B_BCS0 |  |
|  | CA_n78(2A) | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n1A-n3B-n7A-n26(2A)-n78C | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n26(2A)CA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n3B-n7B-n26A-n78A | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n7B | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3B-n7B-n26(2A)-n78A | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n7BCA_n26(2A) | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3B-n7B-n26A-n78(2A) | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n7B | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | CA_n3B_BCS 4 and 5 |  |
|  |  | n7 | CA_n7B_BCS 4 and 5 |  |
|  |  | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3B-n7B-n26A-n78C | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7BCA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n3B-n7B-n26(2A)-n78(2A) | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n7BCA_n26(2A) | n3 | CA_n3B_BCS0 |  |
|  | CA_n78(2A) | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n1A-n3B-n7B-n26(2A)-n78C | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7BCA_n26(2A)CA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n3A-n7B-n26A-n78A | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7B-n26(2A)-n78A | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n26(2A) | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7B-n26A-n78(2A) | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
|  | CA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | CA_n7B_BCS 4 and 5 |  |
|  |  | n26 | n26 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3A-n7B-n26A-n78C | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7BCA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3A-n7B-n26(2A)-n78(2A) | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  | CA_n26(2A) | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  | CA_n78(2A) | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78(2A)_BCS0 |  |
| CA_n1A-n3A-n7B-n26(2A)-n78C | CA_n1A-n3ACA_n1A-n26ACA_n1A-n7ACA_n1A-n78ACA_n3A-n26ACA_n3A-n7ACA_n3A-n78ACA_n7A-n26ACA_n26A-n78ACA_n7A-n78ACA_n7BCA_n26(2A)CA_n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n26 | CA_n26(2A)_BCS0 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3A-n7A-n28A-n38A4 | - | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
| CA_n1A-n3A-n7A-n28A-n75A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n28ACA_n3A-n7ACA_n3A-n28ACA_n7A-n28A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7A-n28A-n78A | n33n73n783,5 | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | n33n73n783,5CA_n1A-n3A3CA_n1A-n7A3CA_n1A-n28ACA_n1A-n78A3CA_n3A-n7A3CA_n3A-n28A3CA_n3A-n78A3CA_n7A-n28A3CA_n7A-n78A3CA_n28A-n78A3 | n1 | 5, 10, 15, 20 | 1 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7B-n28A-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n28ACA_n1A-n78ACA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n7BCA_n28A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7A-n28A-n78(2A) | n33n73n783,5CA_n78(2A)3CA_n1A-n3A3CA_n1A-n7A3CA_n1A-n28ACA_n1A-n78A3CA_n3A-n7A3CA_n3A-n28A3CA_n3A-n78A3CA_n7A-n28A3CA_n7A-n78A3CA_n28A-n78A3 | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n1A-n3A-n7A-n28A-n78C | CA_n78CCA_n1A-n3ACA_n1A-n7ACA_n1A-n28ACA_n1A-n78ACA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 30 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3A-n7B-n28A-n78(2A) | CA_n7BCA_n78(2A)CA_n1A-n3ACA_n1A-n7ACA_n1A-n28ACA_n1A-n78ACA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n1A-n3A-n7B-n28A-n78C | CA_n7BCA_n78CCA_n1A-n3ACA_n1A-n7ACA_n1A-n28ACA_n1A-n78ACA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3B-n7A-n28A-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n28ACA_n1A-n78ACA_n3A-n7ACA_n3A-n28ACA_n3A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3B-n7A-n28A-n78(2A) | CA_n78(2A) CA_n1A-n3A CA_n1A-n7A CA_n1A-n28A CA_n1A-n78A CA_n3A-n7A CA_n3A-n28A CA_n3A-n78A CA_n7A-n28A CA_n7A-n78A CA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n1A-n3B-n7A-n28A-n78C | CA_n78C CA_n1A-n3A CA_n1A-n7A CA_n1A-n28A CA_n1A-n78A CA_n3A-n7A CA_n3A-n28A CA_n3A-n78A CA_n7A-n28A CA_n7A-n78A CA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n3B-n7B-n28A-n78A | CA_n7B CA_n1A-n3A CA_n1A-n7A CA_n1A-n28A CA_n1A-n78A CA_n3A-n7A CA_n3A-n28A CA_n3A-n78A CA_n7A-n28A CA_n7A-n78A CA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3B-n7B-n28A-n78(2A) | CA_n7B CA_n78(2A) CA_n1A-n3A CA_n1A-n7A CA_n1A-n28A CA_n1A-n78A CA_n3A-n7A CA_n3A-n28A CA_n3A-n78A CA_n7A-n28A CA_n7A-n78A CA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
| CA_n1A-n3B-n7B-n28A-n78C | CA_n7BCA_n78C CA_n1A-n3A CA_n1A-n7A CA_n1A-n28A CA_n1A-n78A CA_n3A-n7A CA_n3A-n28A CA_n3A-n78A CA_n7A-n28A CA_n7A-n78A CA_n28A-n78A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | CA_n3B_BCS0 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
|  | CA_n3B | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 1 |
|  |  | n3 | CA_n3B_BCS1 |  |
|  |  | n7 | CA_n7B_BCS0 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n78 | CA_n78C_BCS1 |  |
| CA_n1A-n3A-n7A-n38A-n78A4 | - | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7A-n40A-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n40ACA_n1A-n78ACA_n3A-n7ACA_n3A-n40ACA_n3A-n78ACA_n7A-n40ACA_n7A-n78ACA_n40A-n78A | n1 | 5, 10,15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10,15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7A-n40A-n105A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n40ACA_n1A-n105ACA_n3A-n7ACA_n3A-n40ACA_n3A-n105ACA_n7A-n40ACA_n7A-n105ACA_n40A-n105A | n1 | 5, 10,15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10,15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10,15, 20, 25, 30, 35 |  |
| CA_n1A-n3A-n7A-n67A-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7A-n67A-n78(2A) | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78ACA_n78(2A) | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n67 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78(2A)_BCS2 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n3A-n7A-n75A-n78A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n7A-n75A-n78(2A) | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n3A-n7ACA_n3A-n78ACA_n7A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n3A-n7A-n78A-n105A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n78ACA_n1A-n105ACA_n3A-n7ACA_n3A-n78ACA_n3A-n105ACA_n7A-n78ACA_n7A-n105ACA_n78A-n105A | n1 | 5, 10,15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10,15, 20, 25, 30, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10,15, 20, 25, 30, 35 |  |
| CA_n1A-n3A-n8A-n41A-n78A | CA_n1A-n3ACA_n1A-n8ACA_n1A-n41ACA_n1A-n78ACA_n3A-n8ACA_n3A-n41ACA_n3A-n78ACA_n8A-n41ACA_n8A-n78ACA_n41A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n8A-n41A-n78C | CA_n1A-n3ACA_n1A-n8ACA_n1A-n41ACA_n1A-n78ACA_n1A-n78CCA_n3A-n8ACA_n3A-n41ACA_n3A-n78ACA_n3A-n78CCA_n8A-n41ACA_n8A-n78ACA_n8A-n78CCA_n41A-n78ACA_n41A-n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3A-n20A-n41A-n71A | CA_n1A-n3ACA_n1A-n20ACA_n1A-n41ACA_n1A-n71ACA_n3A-n20ACA_n3A-n41ACA_n3A-n71ACA_n20A-n41ACA_n20A-n71ACA_n41A-n71A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
| CA_n1A-n3A-n20A-n41A-n77A | CA_n1A-n3ACA_n1A-n20ACA_n1A-n41ACA_n1A-n77ACA_n3A-n20ACA_n3A-n41ACA_n3A-n77ACA_n20A-n41ACA_n20A-n77ACA_n41A-n77A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n20A-n41A-n77(2A) | CA_n1A-n3ACA_n1A-n20ACA_n1A-n41ACA_n1A-n77ACA_n3A-n20ACA_n3A-n41ACA_n3A-n77ACA_n20A-n41ACA_n20A-n77ACA_n41A-n77A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n1A-n3A-n20A-n41A-n78A | CA_n1A-n3ACA_n1A-n20ACA_n1A-n41ACA_n1A-n78ACA_n3A-n20ACA_n3A-n41ACA_n3A-n78ACA_n20A-n41ACA_n20A-n78ACA_n41A-n78A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n20A-n71A-n78A | CA_n1A-n3ACA_n1A-n20ACA_n1A-n71ACA_n1A-n78ACA_n3A-n20ACA_n3A-n71ACA_n3A-n78ACA_n20A-n71ACA_n20A-n78ACA_n71A-n78A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n20A-n75A-n78A | CA_n1A-n3ACA_n1A-n20ACA_n1A-n78ACA_n3A-n20ACA_n3A-n78ACA_n20A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n20A-n75A-n78(2A) | CA_n1A-n3ACA_n1A-n20ACA_n1A-n78ACA_n3A-n20ACA_n3A-n78ACA_n20A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n3A-n28A-n38A-n78A | - | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n28A-n40A-n41A | CA_n1A-n3ACA_n1A-n28ACA_n1A-n40ACA_n1A-n41ACA_n3A-n28ACA_n3A-n40ACA_n3A-n41ACA_n28A-n40ACA_n28A-n41ACA_n40A-n41A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n28A-n40A-n77A | CA_n1A-n3ACA_n1A-n28ACA_n1A-n40ACA_n1A-n77ACA_n3A-n28ACA_n3A-n40ACA_n3A-n77ACA_n28A-n40ACA_n28A-n77ACA_n40A-n77A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n28A-n40A-n77(2A) | CA_n1A-n3ACA_n1A-n28ACA_n1A-n40ACA_n1A-n77ACA_n3A-n28ACA_n3A-n40ACA_n3A-n77ACA_n28A-n40ACA_n28A-n77ACA_n40A-n77A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n1A-n3A-n28A-n41A-n77A | CA_n1A-n3ACA_n1A-n28ACA_n1A-n41ACA_n1A-n77ACA_n3A-n28ACA_n3A-n41ACA_n3A-n77ACA_n28A-n41ACA_n28A-n77ACA_n41A-n77A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n28A-n41A-n79A | CA_n1A-n3ACA_n1A-n28ACA_n1A-n41ACA_n1A-n79ACA_n3A-n28ACA_n3A-n41ACA_n3A-n79ACA_n28A-n41ACA_n28A-n79ACA_n41A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n3A-n28A-n75A-n78A | CA_n1A-n3ACA_n1A-n28ACA_n1A-n78ACA_n3A-n28ACA_n3A-n78ACA_n28A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n28A-n75A-n78(2A) | CA_n1A-n3ACA_n1A-n28ACA_n1A-n78ACA_n3A-n28ACA_n3A-n78ACA_n28A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n3A-n28A-n77A-n79A | CA_n1A-n3ACA_n1A-n28ACA_n1A-n77ACA_n1A-n79ACA_n3A-n28ACA_n3A-n77ACA_n3A-n79ACA_n28A-n77ACA_n28A-n79ACA_n77A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n28 | 5, 10 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n28A-n77(2A)-n79A | CA_n1A-n3ACA_n1A-n28ACA_n1A-n77ACA_n1A-n79ACA_n3A-n28ACA_n3A-n77ACA_n3A-n79ACA_n28A-n77ACA_n28A-n79ACA_n77A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n28 | 5, 10 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
|  |  | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n28A-n77(3A)-n79A | CA_n1A-n3ACA_n1A-n28ACA_n1A-n77ACA_n1A-n79ACA_n3A-n28ACA_n3A-n77ACA_n3A-n79ACA_n28A-n77ACA_n28A-n79ACA_n77A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(3A)_BCS 4 and 5 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n40A-n78A-n79A | CA_n1A-n3ACA_n1A-n40ACA_n1A-n78ACA_n1A-n79ACA_n3A-n40ACA_n3A-n78ACA_n3A-n79ACA_n40A-n78ACA_n40A-n79ACA_n78A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n3 | n3 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n3A-n40A-n78A-n105A | CA_n1A-n3ACA_n1A-n40ACA_n1A-n78ACA_n1A-n105ACA_n3A-n40ACA_n3A-n78ACA_n3A-n105ACA_n40A-n78ACA_n40A-n105ACA_n78A-n105A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n40 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n3A-n41A-n71A-n77A | CA_n1A-n3ACA_n1A-n41ACA_n1A-n71A CA_n1A-n77A CA_n3A-n41A CA_n3A-n71ACA_n3A-n77ACA_n41A-n71ACA_n41A-n77ACA_n71A-n77A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n77 | 10,15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n41A-n71A-n77(2A) | CA_n1A-n3ACA_n1A-n41ACA_n1A-n71A CA_n1A-n77A CA_n3A-n41A CA_n3A-n71ACA_n3A-n77ACA_n41A-n71ACA_n41A-n77ACA_n71A-n77A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n1A-n3A-n41A-n71A-n78A | CA_n1A-n3ACA_n1A-n41ACA_n1A-n71ACA_n1A-n78ACA_n3A-n41ACA_n3A-n71ACA_n3A-n78ACA_n41A-n71ACA_n41A-n78ACA_n71A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n41A-n71A-n78C | CA_n1A-n3ACA_n1A-n41ACA_n1A-n71A CA_n1A-n78A CA_n1A-n78C CA_n3A-n41A CA_n3A-n71ACA_n3A-n78ACA_n3A-n78CCA_n41A-n71ACA_n41A-n78ACA_n41A-n78CCA_n71A-n78ACA_n71A-n78C | n1 | 5, 10, 15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n71 | 5, 10, 15, 20 |  |
|  |  | n78 | CA_n78C_BCS0 |  |
| CA_n1A-n3A-n41A-n77A-n79A | CA_n1A-n3ACA_n1A-n41ACA_n1A-n77ACA_n1A-n79ACA_n3A-n41ACA_n3A-n77ACA_n3A-n79ACA_n41A-n77ACA_n41A-n79ACA_n77A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n3 | 5, 10, 15, 20 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n1A-n5A-n7A-n40A-n78A | CA_n1A-n5A CA_n1A-n7A CA_n1A-n40A CA_n1A-n78A CA_n5A-n7A CA_n5A-n40A CA_n5A-n78A CA_n7A-n40A CA_n7A-n78A CA_n40A-n78A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n7 | 5, 10,15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n5A-n7A-n40A-n105A | CA_n1A-n5A CA_n1A-n7A CA_n1A-n40A CA_n1A-n105A CA_n5A-n7A CA_n5A-n40A CA_n5A-n105A CA_n7A-n40A CA_n7A-n105A CA_n40A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n7 | 5, 10,15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n5A-n7A-n78A-n105A | CA_n1A-n5A CA_n1A-n7A CA_n1A-n78A CA_n1A-n105A CA_n5A-n7A CA_n5A-n78A CA_n5A-n105A CA_n7A-n78A CA_n7A-n105A CA_n78A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n7 | 5, 10,15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n5A-n28A-n78A-n79A | CA_n1A-n5ACA_n1A-n28ACA_n1A-n78ACA_n1A-n79ACA_n5A-n28ACA_n5A-n78ACA_n5A-n79ACA_n28A-n78ACA_n28A-n79ACA_n78A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n5A-n40A-n78A-n105A | CA_n1A-n5A CA_n1A-n40A CA_n1A-n78A CA_n1A-n105A CA_n5A-n40A CA_n5A-n78A CA_n5A-n105A CA_n40A-n78A CA_n40A-n105A CA_n78A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n7A-n20A-n28A-n78A 7 | CA_n1A-n7ACA_n1A-n20ACA_n1A-n28ACA_n1A-n78ACA_n7A-n20ACA_n7A-n28ACA_n7A-n78ACA_n20A-n28ACA_n20A-n78ACA_n28A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n20A-n67A-n78A | CA_n1A-n7ACA_n1A-n20ACA_n1A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n20A-n67A-n78(2A) | CA_n1A-n7ACA_n1A-n20ACA_n1A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n7A-n20A-n75A-n78A | CA_n1A-n7ACA_n1A-n20ACA_n1A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n20A-n75A-n78(2A) | CA_n1A-n7ACA_n1A-n20ACA_n1A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n7A-n28A-n75A-n78A | CA_n1A-n7ACA_n1A-n28ACA_n1A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n28A-n75A-n78(2A) | CA_n1A-n7ACA_n1A-n28ACA_n1A-n78ACA_n7A-n28ACA_n7A-n78ACA_n28A-n78ACA_n78(2A) | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS4 and 5 |  |
| CA_n1A-n7A-n28A-n38A-n78A4 | - | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n7A-n40A-n78A-n79A | CA_n1A-n7ACA_n1A-n40ACA_n1A-n78ACA_n1A-n79ACA_n7A-n40ACA_n7A-n78ACA_n7A-n79ACA_n40A-n78ACA_n40A-n79ACA_n78A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n7A-n40A-n78A-n105A | CA_n1A-n7ACA_n1A-n40ACA_n1A-n78ACA_n1A-n105ACA_n7A-n40ACA_n7A-n78ACA_n7A-n105ACA_n40A-n78ACA_n40A-n105ACA_n78A-n105A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n1A-n8A-n40A-n78A-n79A | CA_n1A-n8ACA_n1A-n40ACA_n1A-n78ACA_n1A-n79ACA_n8A-n40ACA_n8A-n78ACA_n8A-n79ACA_n40A-n78ACA_n40A-n79ACA_n78A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n8 | n8 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n18A-n28A-n41A-n77A | n413,5n773,5CA_n1A-n18ACA_n1A-n28ACA_n1A-n41A3CA_n1A-n77A3CA_n18A-n28A3CA_n18A-n41A3CA_n18A-n77A3CA_n28A-n41A3CA_n28A-n77A3CA_n41A-ns77A3 | n1 | 5, 10, 15, 20 | 0 |
|  |  | n18 | 5, 10, 15 |  |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n20A-n41A-n71A-n78A | CA_n1A-n20ACA_n1A-n41ACA_n1A-n71ACA_n1A-n78ACA_n20A-n41ACA_n20A-n71ACA_n20A-n78ACA_n41A-n71ACA_n41A-n78ACA_n71A-n78A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n78 | 10,15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n28A-n40A-n78A-n79A | CA_n1A-n28ACA_n1A-n40ACA_n1A-n78ACA_n1A-n79ACA_n28A-n40ACA_n28A-n78ACA_n28A-n79ACA_n40A-n78ACA_n40A-n79A CA_n78A-n79A | n1 | n1 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n40 | n40 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n79 | n79 channel bandwidths in Table 5.3.5-1 |  |
| CA_n1A-n28A-n41A-n77A-n79A | CA_n1A-n28ACA_n1A-n41ACA_n1A-n77ACA_n1A-n79ACA_n28A-n41ACA_n28A-n77ACA_n28A-n79ACA_n41A-n77ACA_n41A-n79ACA_n77A-n79A | n1 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n2A-n5A-n30A-n66A-n77A | n773,5CA_n2A-n5ACA_n2A-n30ACA_n2A-n66ACA_n2A-n77A3CA_n5A-n30ACA_n5A-n66ACA_n5A-n77A3CA_n30A-n66ACA_n30A-n77A3CA_n66A-n77A3 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n5A-n30A-n66A-n77(2A) | n773,5CA_n2A-n5ACA_n2A-n30ACA_n2A-n66ACA_n2A-n77A3CA_n5A-n30ACA_n5A-n66ACA_n5A-n77A3CA_n30A-n66ACA_n30A-n77A3CA_n66A-n77A3 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n5A-n48A-n66A-n77A | n773,5CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n2A-n77A3CA_n5A-n48ACA_n5A-n66ACA_n5A-n77A3CA_n48A-n66ACA_n66A-n77A3 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 706, 806, 906, 1006 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2(2A)-n5A-n48A-n66A-n77A | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n66A-n77A | n2 | CA_n2(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5B-n48A-n66A-n77A | CA_n5BCA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | CA_n5B_BCS 4 and 5 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n48A-n66(2A)-n77A | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n48B-n66A-n77A | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n2A-n77A3CA_n5A-n48ACA_n5A-n66ACA_n5A-n77A3CA_n48A-n66ACA_n48BCA_n66A-n77A3 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | CA_n48B_BCS2 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  | CA_n48BCA_n2A-n5ACA_n2A-n48ACA_n2A-n48BCA_n2A-n66ACA_n2A-n77ACA_n5A-n48ACA_n5A-n48BCA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n48B-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48B_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n48(2A)-n66A-n77A | CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n48A-n66ACA_n66A-n77A | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | CA_n48(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n2A-n5A-n48A-n66A-n77C | n773,5CA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n2A-n77A3CA_n5A-n48ACA_n5A-n66ACA_n5A-n77A3CA_n48A-n66ACA_n66A-n77A3CA_n77C | n2 | 5, 10, 15, 20 | 0 |
|  |  | n5 | 5, 10, 15, 20 |  |
|  |  | n48 | 5, 10, 15, 20, 40, 506, 606, 706, 806, 906, 1006 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77C_BCS1 |  |
|  | CA_n77CCA_n2A-n5ACA_n2A-n48ACA_n2A-n66ACA_n2A-n77ACA_n2A-n77CCA_n5A-n48ACA_n5A-n66ACA_n5A-n77ACA_n5A-n77CCA_n48A-n66ACA_n66A-n77ACA_n66A-n77C | n2 | n2 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n5 | n5 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n48 | n48 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77C_BCS 4 and 5 |  |
| CA_n2A-n12A-n30A-n66A-n77A | n773,5CA_n2A-n12ACA_n2A-n30ACA_n2A-n66ACA_n2A-n77A3CA_n12A-n30ACA_n12A-n66ACA_n12A-n77A3CA_n30A-n66ACA_n30A-n77A3CA_n66A-n77A3 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n12A-n30A-n66A-n77(2A) | n773,5CA_n2A-n12ACA_n2A-n30ACA_n2A-n66ACA_n2A-n77A3CA_n12A-n30ACA_n12A-n66ACA_n12A-n77A3CA_n30A-n66ACA_n30A-n77A3CA_n66A-n77A3 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n12 | 5, 10, 15 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n14A-n30A-n66A-n77A | n773,5CA_n2A-n14ACA_n2A-n30ACA_n2A-n66ACA_n2A-n77A3CA_n14A-n30ACA_n14A-n66ACA_n14A-n77A3CA_n30A-n66ACA_n30A-n77A3CA_n66A-n77A3 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n14A-n30A-n66A-n77(2A) | n773,5CA_n2A-n14ACA_n2A-n30ACA_n2A-n66ACA_n2A-n77A3CA_n14A-n30ACA_n14A-n66ACA_n14A-n77A3CA_n30A-n66ACA_n30A-n77A3CA_n66A-n77A3 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n14 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n2A-n29A-n30A-n66A-n77A | n773,5CA_n2A-n30ACA_n2A-n66ACA_n2A-n77A3CA_n30A-n66ACA_n30A-n77A3CA_n66A-n77A3 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n2A-n29A-n30A-n66A-n77(2A) | n773,5CA_n2A-n30ACA_n2A-n66ACA_n2A-n77A3CA_n30A-n66ACA_n30A-n77A3CA_n66A-n77A3 | n2 | 5, 10, 15, 20 | 0 |
|  |  | n29 | 5, 10 |  |
|  |  | n30 | 5, 10 |  |
|  |  | n66 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n77 | CA_n77(2A)_BCS1 |  |
| CA_n3A-n7A-n20A-n28A-n78A 7 | CA_n3A-n7ACA_n3A-n20ACA_n3A-n28ACA_n3A-n78ACA_n7A-n20ACA_n7A-n28ACA_n7A-n78ACA_n20A-n28ACA_n20A-n78ACA_n28A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n28 | n28 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n20A-n67A-n78A | CA_n3A-n7ACA_n3A-n20ACA_n3A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n20A-n67A-n78(2A) | CA_n3A-n7ACA_n3A-n20ACA_n3A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78ACA_n78(2A) | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n67 | n67 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n3A-n7A-n20A-n75A-n78A | CA_n3A-n7ACA_n3A-n20ACA_n3A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78A | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | n78 channel bandwidths in Table 5.3.5-1 |  |
| CA_n3A-n7A-n20A-n75A-n78(2A) | CA_n3A-n7ACA_n3A-n20ACA_n3A-n78ACA_n7A-n20ACA_n7A-n78ACA_n20A-n78ACA_n78(2A) | n3 | n3 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n7 | n7 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n20 | n20 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n75 | n75 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n78 | CA_n78(2A)_BCS 4 and 5 |  |
| CA_n3A-n7A-n28A-n38A-n78A4 | - | n3 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n7A-n40A-n78A-n105A | CA_n3A-n7ACA_n3A-n40ACA_n3A-n78ACA_n3A-n105ACA_n7A-n40ACA_n7A-n78ACA_n7A-n105ACA_n40A-n78ACA_n40A-n105ACA_n78A-n105A | n3 | 5, 10, 15, 20 | 0 |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n3A-n8A-n39A-n41A-n79A | - | n3 | 5, 10, 15, 20, 25, 30 | 0 |
|  |  | n8 | 5, 10, 15, 20 |  |
|  |  | n39 | 5, 10, 15, 20, 25, 30, 35, 40 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n3A-n20A-n41A-n71A-n78A | CA_n3A-n20ACA_n3A-n41ACA_n3A-n71ACA_n3A-n78ACA_n20A-n41ACA_n20A-n71ACA_n20A-n78ACA_n41A-n71ACA_n41A-n78ACA_n71A-n78A | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 | 0 |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n78 | 10,15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n3A-n28A-n41A-n77A-n79A | CA_n3A-n28ACA_n3A-n41ACA_n3A-n77ACA_n3A-n79ACA_n28A-n41ACA_n28A-n77ACA_n28A-n79ACA_n41A-n77ACA_n41A-n79ACA_n77A-n79A | n3 | 5, 10, 15, 20 | 0 |
|  |  | n28 | 5, 10 |  |
|  |  | n41 | 10, 15, 20, 30, 40, 50, 60, 80, 90, 100 |  |
|  |  | n77 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n79 | 40, 50, 60, 80, 100 |  |
| CA_n5A-n7A-n40A-n78A-n105A | CA_n5A-n7A CA_n5A-n40A CA_n5A-n78A CA_n5A-n105A CA_n7A-n40A CA_n7A-n78A CA_n7A-n105A CA_n40A-n78A CA_n40A-n105A CA_n78A-n105A | n5 | 5, 10, 15, 20, 25 | 0 |
|  |  | n7 | 5, 10,15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| CA_n7A-n25A-n66A-n71A-n77A | CA_n7A-n25ACA_n7A-n66ACA_n7A-n71ACA_n7A-n77ACA_n25A-n66ACA_n25A-n71ACA_n25A-n77ACA_n66A-n71ACA_n66A-n77ACA_n71A-n77A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n7A-n25A-n66A-n71A-n77(2A) | CA_n7A-n25ACA_n7A-n66ACA_n7A-n71ACA_n7A-n77ACA_n25A-n66ACA_n25A-n71ACA_n25A-n77ACA_n66A-n71ACA_n66A-n77ACA_n71A-n77A | n7 | n7 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n25 | n25 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS4 and 5 |  |
| CA_n25A-n41A-n66A-n71A-n77A | n253n413,5n663n713n773,5CA_n25A-n41A3CA_n25A-n66A3CA_n25A-n71A3CA_n25A-n77A3CA_n41A-n66A3CA_n41A-n71A3CA_n41A-n77A3CA_n66A-n71A3CA_n66A-n77A3CA_n71A-n77A3 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n66A-n71A-n77(2A) | n413,5n773,5CA_n25A-n41A3 CA_n25A-n66A CA_n25A-n71A CA_n25A-n77A3 CA_n41A-n66A3 CA_n41A-n71A3 CA_n41A-n77A3 CA_n66A-n71A CA_n66A-n77A3 CA_n71A-n77A3 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | CA_n77(2A)_BCS 4 and 5 |  |
| CA_n25A-n41A-n66(2A)-n71A-n77A | n253n413,5n663n713n773,5CA_n25A-n41A3CA_n25A-n66A3CA_n25A-n71A3CA_n25A-n77A3CA_n41A-n66A3CA_n41A-n71A3CA_n41A-n77A3CA_n66A-n71A3CA_n66A-n77A3CA_n71A-n77A3 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | CA_n66(2A)_BCS 4 and 5 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n66A-n71(2A)-n77A | n253n413,5n663n713n773,5CA_n25A-n41A3CA_n25A-n66A3CA_n25A-n71A3CA_n25A-n77A3CA_n41A-n66A3CA_n41A-n71A3CA_n41A-n77A3CA_n66A-n71A3CA_n66A-n77A3CA_n71A-n77A3 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71(2A)_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41A-n66A-n71B-n77A | n253n413,5n663n713n773,5CA_n25A-n41A3CA_n25A-n66A3CA_n25A-n71A3CA_n25A-n77A3CA_n41A-n66A3CA_n41A-n71A3CA_n41A-n77A3CA_n66A-n71A3CA_n66A-n77A3CA_n71A-n77A3 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | CA_n71B_BCS 4 and 5 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41C-n66A-n71A-n77A | n253n413,5n663n713n773,5CA_n25A-n41A3CA_n25A-n41CCA_n25A-n66A3 CA_n25A-n71A3 CA_n25A-n77A3 CA_n41A-n66A3CA_n41C-n66ACA_n41A-n71A3CA_n41C-n71ACA_n41A-n77A3CA_n41C-n77ACA_n41C3CA_n66A-n71A3 CA_n66A-n77A3 CA_n71A-n77A3 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41C_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25A-n41(2A)-n66A-n71A-n77A | n253n413,5n663n713n773,5CA_n25A-n41A3 CA_n25A-n66A3 CA_n25A-n71A3 CA_n25A-n77A3 CA_n41A-n66A3 CA_n41A-n71A3 CA_n41A-n77A3 CA_n66A-n71A3 CA_n66A-n77A3 CA_n71A-n77A3 | n25 | n25 channel bandwidths in Table 5.3.5-1 | 4 and 5 |
|  |  | n41 | CA_n41(2A)_BCS 4 and 5 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| CA_n25(2A)-n41A-n66A-n71A-n77A | n253n413,5n663n713n773,5CA_n25A-n41A3 CA_n25A-n66A3 CA_n25A-n71A3 CA_n25A-n77A3 CA_n41A-n66A3 CA_n41A-n71A3 CA_n41A-n77A3 CA_n66A-n71A3 CA_n66A-n77A3 CA_n71A-n77A3 | n25 | CA_n25(2A)_BCS 4 and 5 | 4 and 5 |
|  |  | n41 | n41 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n66 | n66 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n71 | n71 channel bandwidths in Table 5.3.5-1 |  |
|  |  | n77 | n77 channel bandwidths in Table 5.3.5-1 |  |
| NOTE 1:  For each channel bandwidth of each component carrier, refer to Table 5.3.5-1 of TS 38.101-1 and TS 38.101-2 for the applicable SCSs for NR FR1 and NR FR2 bands respectively. For a given band, not all UE channel bandwidths support the same SCSs.NOTE 2: Only single uplink carriers with power class other than PC3 are listed.NOTE 3: Minimum requirements for Power Class 2 are applicable for this uplink combination or single uplink carrier in this downlink/uplink combination.NOTE 4:  For a band combination which includes band n7 and n38 simultaneously, carriers in band n7 and n38 can only be configured as downlink carriers. Power imbalance between downlink carriers on Band n7 and Band n38 is assumed to be within 6dB.NOTE 5: Power Class 1.5 is allowed for this single uplink carrier in this downlink/uplink combination.NOTE 6: For this bandwidth, the minimum requirements are restricted to operation when carrier is configured as a downlink SCell part of CA configurationNOTE 7: The frequency range in band n28 is restricted for this band combination to 703- 733 MHz for the UL and 758-788 MHz for the DL. |  |  |  |  |

#### 5.5A.3.5 Configurations for inter-band CA (six bands)


Table 5.5A.3.5-1: NR CA configurations and bandwidth combinations sets defined for inter-band CA (six bands)

| NR CA configuration | Uplink configuration | NR Band | Channel bandwidth (MHz) (NOTE 1) | Bandwidth combination set |
| --- | --- | --- | --- | --- |
| CA_n1A-n3A-n7A-n28A-n38A-n78A2 | - | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n7 | 5, 10, 15, 20, 25, 30, 40, 50 |  |
|  |  | n28 | 5, 10, 15, 20, 25, 30 |  |
|  |  | n38 | 5, 10, 15, 20, 25, 30, 40 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n3A-n7A-n40A-n78A-n105A | CA_n1A-n3ACA_n1A-n7ACA_n1A-n40ACA_n1A-n78ACA_n1A-n105ACA_n3A-n7ACA_n3A-n40ACA_n3A-n78ACA_n3A-n105ACA_n7A-n40ACA_n7A-n78ACA_n7A-n105ACA_n40A-n78ACA_n40A-n105ACA_n78A-n105A | n1 | 5, 10,15, 20, 25, 30, 40, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 40, 50 |  |
|  |  | n7 | 5, 10,15, 20, 25, 30, 40, 50 |  |
|  |  | n40 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10,15, 20, 25, 30, 35 |  |
| CA_n1A-n3A-n20A-n41A-n71A-n78A | CA_n1A-n3ACA_n1A-n20ACA_n1A-n41ACA_n1A-n71ACA_n1A-n78ACA_n3A-n20ACA_n3A-n41ACA_n3A-n71ACA_n3A-n78ACA_n20A-n41ACA_n20A-n71ACA_n20A-n78ACA_n41A-n71ACA_n41A-n78ACA_n71A-n78A | n1 | 5, 10,15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n3 | 5, 10,15, 20, 25, 30, 35, 40, 45, 50 |  |
|  |  | n20 | 5, 10,15, 20 |  |
|  |  | n41 | 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 |  |
|  |  | n71 | 5, 10,15, 20, 25, 30, 35 |  |
|  |  | n78 | 10,15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
| CA_n1A-n5A-n7A-n40A-n78A-n105A | CA_n1A-n5A CA_n1A-n7A CA_n1A-n40A CA_n1A-n78A CA_n1A-n105A CA_n5A-n7A CA_n5A-n40A CA_n5A-n78A CA_n5A-n105A CA_n7A-n40A CA_n7A-n78A CA_n7A-n105A CA_n40A-n78A CA_n40A-n105A CA_n78A-n105A | n1 | 5, 10, 15, 20, 25, 30, 40, 45, 50 | 0 |
|  |  | n5 | 5, 10, 15, 20, 25 |  |
|  |  | n7 | 5, 10,15, 20, 25, 30, 35, 40, 50 |  |
|  |  | n40 | 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n78 | 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 |  |
|  |  | n105 | 5, 10, 15, 20, 25, 30, 35 |  |
| NOTE 1:  For each channel bandwidth of each component carrier, refer to Table 5.3.5-1 of TS 38.101-1 and TS 38.101-2 for the applicable SCSs for NR FR1 and NR FR2 bands respectively. For a given band, not all UE channel bandwidths support the same SCSs.NOTE 2: For a band combination which includes band n7 and n38 simultaneously, carriers in band n7 and n38 can only be configured as downlink carriers. Power imbalance between downlink carriers on Band n7 and Band n38 is assumed to be within 6dB. |  |  |  |  |
