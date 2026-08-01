# 6 Transmitter characteristics

## 6.1 General

Unless otherwise stated the transmitter characteristics are specified at the antenna connector(s) of the UE for the bands operating on frequency range 1 and over the air of the UE for the bands operating on frequency range 2. The requirements for frequency range 1 and frequency range 2 can be verified separately. For the carrier in frequency range 1, requirements can be verified with NR FR2 link disabled. For the carrier in frequency range 2, requirements can be verified in OTA mode with E-UTRA or NR FR1 connecting to the network by OTA without calibration.

Unless otherwise stated, requirements for NR transmitter written in TS 38.101-1 [2] and TS 38.101-2 [3] apply and are assumed anchor agnostic. Requirements are verified under conditions where anchor resources do not interfere NR operation. If UE indicates IE powerClassNRPart-r16 as defined in TS 38.331 [9] in EN-DC, UE shall meet NR requirements according to this power class.

For sub-clauses with suffix A or B: the minimum requirements for band combinations including Band n41 also apply for the corresponding band combinations with Band n90 replacing Band n41 but with otherwise identical parameters. For brevity the said band combinations with Band n90 are not listed in the tables below but are covered by this specification.

## 6.2 Void

## 6.2A Transmitter power for CA

### 6.2A.1 UE maximum output power for CA

#### 6.2A.1.1 Inter-band CA between FR1 and FR2

Table 6.2A.1.1-1: Void

For inter-band NR CA in FR1 and FR2 combined, the UE shall meet each transmitter power requirement specified in TS 38.101-1 [2] and TS 38.101-2 [3] for each frequency range independently.

### 6.2A.2 UE maximum output power reduction for CA

#### 6.2A.2.1 Inter-band CA between FR1 and FR2

For inter-band NR CA between FR1 and FR2, UE maximum output power reduction specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for each frequency range respectively.

### 6.2A.3 UE additional maximum output power reduction for CA

For inter-band NR CA between FR1 and FR2, UE additional maximum output power reduction specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for each frequency range respectively.

### 6.2A.4 Configured output power for CA

#### 6.2A.4.1 Configured output power level

For inter-band NR CA between FR1 and FR2, UE configured output power specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for each frequency range respectively.

For inter-band NR CA between FR1 and FR2 with a single uplink component carrier configured in FR1, when the powerBoostPi2BPSK-r18 or powerBoostQPSK-r18 is set to 1 for a UE supporting the capability of powerBoosting-pi2BPSK-QPSK-Modified-r18 or powerBoosting-pi2BPSK-QPSK-r18, the configured maximum output power PCMAX,c  on serving cell c shall be set as specified for PCMAX,f,c in clause 6.2.4.

#### 6.2A.4.2 ΔTIB,c for CA

##### 6.2A.4.2.1 ΔTIB,c for Inter-band CA between FR1 and FR2

Unless otherwise stated, ΔTIB,c for NR FR1 band and FR2 band of inter-band CA defined in table 5.5A.1-1 is set to zero.

Table 6.2A.4.2.1-1: Void

Table 6.2A.4.2.1-2: Void

Table 6.2A.4.2.1-3: Void

## 6.2B Transmitter power for DC

### 6.2B.1 UE maximum output power for DC

#### 6.2B.1.1 Intra-band contiguous EN-DC

The following UE Power Classes define the total maximum output power for any transmission bandwidth(s) of the CG(s) configured.

The maximum output power is measured as the total maximum output power across the UE antenna connector(s). The period of measurement shall be at least one sub frame.

Table 6.2B.1.1-1: Maximum output power for EN-DC (continuous sub-blocks)

| EN-DC configuration | Power class 1.5(dBm) | Tolerance(dB) | Power class 2(dBm) | Tolerance(dB) | Power class 3(dBm) | Tolerance(dB) |
| --- | --- | --- | --- | --- | --- | --- |
| DC_(n)3AA3 |  |  |  |  | 23 | +2/-3 |
| DC_(n)5AA3 |  |  |  |  | 23 | +2/-3 |
| DC_(n)7AA3 |  |  |  |  | 23 | +2/-3 |
| DC_(n)8AA3 |  |  |  |  | 23 | +2/-3 |
| DC_(n)12AA3 |  |  |  |  | 23 | +2/-3 |
| DC_(n)40AA3 |  |  | 26 | +2/-3 | 23 | +2/-3 |
| DC_(n)71AA |  |  |  |  | 23 | +2/-3 |
| DC_(n)38AA3 |  |  |  |  | 23 | +2/-3 |
| DC_(n)41AA | 29 | +2/-3 | 26 | +2/-3 | 23 | +2/-3 |
| DC_(n)48AA3 |  |  |  |  | 23 | +2/-3 |
| DC_(n)66AA3 |  |  |  |  | 23 | +2/-3 |
| NOTE 1:  An uplink DC configuration in which the band has NOTE 3 in Table 6.2.1-1 in TS 38.101-1 or NOTE 2 in Table 6.2.2-1 in TS 36.101 is allowed to reduce the lower tolerance limit by 1.5 dB when the transmission bandwidths of at least one of the bands are confined within FUL_low and FUL_low + 4 MHz or FUL_high - 4 MHz and FUL_high.NOTE 2: Power Class 3 is the default power class unless otherwise stated.NOTE 3: Only single switched UL is supported. |  |  |  |  |  |  |

If UE supports a different power class than the default UE power class for EN-DC band combination, and the supported power class enables higher maximum output power than that of the default power class:

- if the E-UTRA UL/DL configuration is 0 or 6; or

- if the E-UTRA UL/DL configuration is 1 and special subframe configuration is 0 or 5; or

- if the IE p-maxUE-FR1-r15 as defined in TS 36.331 [8] is provided and set to the maximum output power of the default power class or lower;

- apply all requirements for the default power class, and set the configured transmitted power as specified in clause 6.2B.4;

- else

- if the UE does not support a power class with higher maximum output power than power class 2; or

- if the E-UTRA UL/DL configuration is not 2 or 4 or 5; or

- if the field of UE IE maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.331 is absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than 25% (The exact evaluation period is no less than one radio frame); or

- if the field of UE IE maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-PC2-FR1 (The exact evaluation period is no less than one radio frame); or

- if the IE P-Max as defined in TS 38.331 [9] is provided and set to the maximum output power of the power class 2 or lower;

- apply all requirements for the power class 2 and set the configured transmitted power as specified in clause 6.2B.4;

- else

- apply all requirements for the supported power class, and set the configured transmitted power class as specified in clause 6.2B.4;

#### 6.2B.1.1a Intra-band contiguous NE-DC

The following UE Power Classes define the total maximum output power for any transmission bandwidth(s) of the CG(s) configured.

The maximum output power is measured as the total maximum output power across the UE antenna connector(s). The period of measurement shall be at least one sub frame.

Table 6.2B.1.1a-1: Maximum output power for NE-DC (continuous sub-blocks)

| NE-DC configuration | Power class 1.5(dBm) | Tolerance(dB) | Power class 2(dBm) | Tolerance(dB) | Power class 3(dBm) | Tolerance(dB) |
| --- | --- | --- | --- | --- | --- | --- |
| DC_3 (n) AA3 |  |  |  |  | 23 | +2/-3 |
| NOTE 1: If all transmitted resource blocks over all component carriers are confined within FUL_low and FUL_low + 4 MHz or/and FUL_high – 4 MHz and FUL_high, the maximum output power requirement is relaxed by reducing the lower tolerance limit by 1.5 dBNOTE 2: Power Class 3 is the default power class unless otherwise stated.NOTE 3: Only single switched UL is supported. |  |  |  |  |  |  |

#### 6.2B.1.2 Intra-band non-contiguous EN-DC

Table 6.2B.1.2-1: Maximum output power for EN-DC (non-continuous sub-blocks)

| EN-DC configuration | Power class 1.5(dBm) | Tolerance(dB) | Power class 2(dBm) | Tolerance(dB) | Power class 3(dBm) | Tolerance(dB) |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DC_1A_n1A4 |  |  |  |  | 23 | +2/-3 |  |
| DC_2A_n2A4 |  |  |  |  | 23 | +2/-3 |  |
| DC_3A_n3A |  |  |  |  | 23 | +2/-3 |  |
| DC_5A_n5A4 |  |  |  |  | 23 | +2/-3 |  |
| DC_7A_n7A4 |  |  |  |  | 23 | +2/-3 |  |
| DC_40A_n40A4 |  |  |  |  | 23 | +2/-3 |  |
| DC_48A_n48A4 |  |  |  |  | 23 | +2/-3 |  |
| DC_41A_n41A | 29 | +2/-3 | 26 | +2/-3 | 23 | +2/-3 |  |
| DC_66A_n66A4 |  |  |  |  | 23 | +2/-3 |  |
| DC_71A_n71A4 |  |  |  |  | 23 | +2/-3 |  |
| NOTE 1: An uplink DC configuration in which the band has NOTE 3 in Table 6.2.1-1 in TS 38.101-1 or NOTE 2 in Table 6.2.2-1 in TS 36.101 is allowed to reduce the lower tolerance limit by 1.5 dB when the transmission bandwidths of at least one of the bands are confined within FUL_low and FUL_low + 4 MHz or FUL_high - 4 MHz and FUL_high.NOTE 2: Void.NOTE 3: Power Class 3 is the default power class unless otherwise stated.NOTE 4: Only single switched UL is supported. |  |  |  |  |  |  |  |

If UE supports a different power class than the default UE power class for EN-DC band combination, and the supported power class enables higher maximum output power than that of the default power class:

- if the E-UTRA UL/DL configuration is 0 or 6; or

- if the E-UTRA UL/DL configuration is 1 and special subframe configuration is 0 or 5; or

- if the IE p-maxUE-FR1-r15 as defined in TS 36.331 [8] is provided and set to the maximum output power of the default power class or lower;

- apply all requirements for the default power class, and set the configured transmitted power as specified in clause 6.2B.4;

- else

- if the UE does not support a power class with higher maximum output power than power class 2; or

- if the E-UTRA UL/DL configuration is not 2 or 4 or 5; or

- if the field of UE IE maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.331 is absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than 25% (The exact evaluation period is no less than one radio frame); or

- if the field of UE IE maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-PC2-FR1 (The exact evaluation period is no less than one radio frame); or

- if the IE P-Max as defined in TS 38.331 [9] is provided and set to the maximum output power of the power class 2 or lower;

- apply all requirements for the power class 2 and set the configured transmitted power as specified in clause 6.2B.4;

- else

- apply all requirements for the supported power class, and set the configured transmitted power class as specified in clause 6.2B.4;

#### 6.2B.1.3 Inter-band EN-DC within FR1

For inter-band EN-DC of E-UTRA and NR in FR1, the following UE Power Classes define the maximum output power for any transmission bandwidth within the aggregated channel bandwidth. The maximum output power is measured as the sum of the maximum output power at each UE antenna connector. The period of measurement shall be at least one sub frame (1ms). UE maximum output power shall be measured over all component carriers from different bands. If each band has separate antenna connectors, maximum output power is measured as the sum of maximum output power at each UE antenna connector.

The maximum output power for inter-band EN-DC with one Tx per band is specified in Table 6.2B.1.3-1. The per band power class for each band applicable to REFSENS exceptions for a given inter-band UL EN-DC power class are specified in Table 6.2B.3.1-1a. These configurations are subject to the applicable power class of each E-UTRA band and NR band specified in Table 6.2.2-1 of TS 36.101 and Table 6.2.1-1 of TS 38.101-1 respectively. The power classes referenced are according to the reported ue-PowerClass-N-r13 for the E-UTRA band or ue-CA-PowerClass-N for the E-UTRA intra-band UL CA of the EN-DC combination, and reported powerClassNRPart-r16 for the NR band and for NR intra-band UL CA of the EN-DC combination if indicated or ue-PowerClass otherwise.

If higherPowerLimitMRDC-r17 is indicated for an UL inter-band EN-DC configuration as specified in Table 6.2B.1.3-1  and with uplink bands of different power class capabilities, the UE maximum output power specified in Table 6.2B.1.3-1 for this UL EN-DC configuration is modified in accordance with sub-clause 6.2B.4.1.3.

Table 6.2B.1.3-1: Maximum output power for inter-band EN-DC (two bands)

| EN-DC configuration | Power class 1.5(dBm) | Tolerance(dB) | Power class 2(dBm) | Tolerance(dB) | Power class 3(dBm) | Tolerance(dB) |
| --- | --- | --- | --- | --- | --- | --- |
| DC_1A_n3A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n5A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n8A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n20A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n26A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n38A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n40A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_1A_n50A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n51A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n71A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_1A_n84A_ULSUP-TDM_n77A |  |  | [266] | [+2/-3] | 23 | +2/-3 |
| DC_1A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_1A_n84A_ULSUP-TDM_n78A |  |  | [266] | [+2/-3] | 23 | +2/-3 |
| DC_1A_n79A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_1A_n84A_ULSUP-TDM_n79A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n80A |  |  |  |  | 23 | +2/-3 |
| DC_1A_n105A |  |  |  |  | 23 | +2/-3 |
| DC_2A_n5A |  |  |  |  | 23 | +2/-3 |
| DC_2A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_2A_n12A |  |  |  |  | 23 | +2/-3 |
| DC_2A_n14A |  |  |  |  | 23 | +2/-3 |
| DC_2A_n25A |  |  |  |  | N/A | N/A |
| DC_2A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_2A_n30A |  |  |  |  | 23 | +2/-3 |
| DC_2A_n38A |  |  |  |  | 23 | +2/-3 |
| DC_2A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_2A_n46A |  |  |  |  | 23 | +2/-3 |
| DC_2A_n48A |  |  |  |  | 23 | +2/-3 |
| DC_2A_n66A |  |  |  |  | 23 | +2/-3 |
| DC_2A_n71A |  |  |  |  | 23 | +2/-3 |
| DC_2A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_2A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_3A_n1A |  |  |  |  | 23 | +2/-3 |
| DC_3C_n1A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n7B |  |  |  |  | 23 | +2/-3 |
| DC_3C_n7A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n8A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n20A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n26A |  |  |  |  | 23 | +2/-3 |
| DC_3C_n28A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_3C_n26A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n38A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n40A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_3C_n41A, |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_3A_n50A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n51A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n71A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_3C_n77A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_3C_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_3A_n79A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_3C_n79A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n80A_ULSUP-TDM_n41A |  |  |  |  | 23 | +2/-3 |
| DC_3C_n80A_ULSUP-TDM_n41A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n80A_ULSUP-TDM_n77AA |  |  |  |  | 23 | +2/-3 |
| DC_3A_n80A_ULSUP-TDM_n78A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n80A_ULSUP-TDM_n79A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n82A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n84A |  |  |  |  | 23 | +2/-3 |
| DC_3A_n105A |  |  |  |  | 23 | +2/-3 |
| DC_4A_n2A |  |  |  |  | 23 | +2/-3 |
| DC_4A_n5A |  |  |  |  | 23 | +2/-3 |
| DC_4A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_4A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_4A_n38A |  |  |  |  | 23 | +2/-3 |
| DC_4A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_4A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_5A_n2A |  |  |  |  | 23 | +2/-3 |
| DC_5A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_5A_n12A |  |  |  |  | 23 | +2/-3 |
| DC_5A_n25A |  |  |  |  | 23 | +2/-3 |
| DC_5A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_5A_n30A |  |  |  |  | 23 | +2/-3 |
| DC_5A_n38A |  |  |  |  | 23 | +2/-3 |
| DC_5A_n40A |  |  |  |  | 23 | +2/-3 |
| DC_5A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_5A_n48A |  |  |  |  | 23 | +2/-3 |
| DC_5A_n66A |  |  |  |  | 23 | +2/-3 |
| DC_5A_n71A |  |  |  |  | 23 | +2/-3 |
| DC_5A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_5A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_5A_n79A |  |  |  |  | 23 | +2/-3 |
| DC_5A_n89A_ULSUP-TDM_n78A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n1A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n2A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n3A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n5A |  |  |  |  | 23 | +2/-3 |
| DC_7C_n5A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n8A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n12A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n20A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n25A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n26A |  |  |  |  | 23 | +2/-3 |
| DC_7C_n26A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n40A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n51A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n66A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n71A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n77A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_7C_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_7A_n79A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n80A |  |  |  |  | 23 | +2/-3 |
| DC_7A_n105A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n1A |  |  |  |  | 23 | +2/-3 |
| DC_8B_n1A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n2A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n3A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n20A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n34A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n38A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n39A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n40A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n41A, |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_8A_n71A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_8A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_8B_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_8A_n79A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_8A_n79C |  |  |  |  | 23 | +2/-3 |
| DC_8A_n80A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n81A_ULSUP-TDM_n41A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n81A_ULSUP-TDM_n78A |  |  |  |  | 23 | +2/-3 |
| DC_8A_n81A_ULSUP-TDM_n79A |  |  |  |  | 23 | +2/-3 |
| DC_11A_n1A |  |  |  |  | 23 | +2/-3 |
| DC_11A_n3A |  |  |  |  | 23 | +2/-3 |
| DC_11A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_11A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_11A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_11A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_11A_n79A |  |  |  |  | 23 | +2/-3 |
| DC_12A_n2A |  |  |  |  | 23 | +2/-3 |
| DC_12A_n5A |  |  |  |  | 23 | +2/-3 |
| DC_12A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_12A_n25A |  |  |  |  | 23 | +2/-3 |
| DC_12A_n30A |  |  |  |  | 23 | +2/-3 |
| DC_12A_n38A |  |  |  |  | 23 | +2/-3 |
| DC_12A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_12A_n66A |  |  |  |  | 23 | +2/-3 |
| DC_12A_n71A7 |  |  |  |  | 23 | +2/-3 |
| DC_12A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_12A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_13A_n2A |  |  |  |  | 23 | +2/-3 |
| DC_13A_n5A |  |  |  |  | 23 | +2/-3 |
| DC_13A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_13A_n25A |  |  |  |  | 23 | +2/-3 |
| DC_13A_n48A |  |  |  |  | 23 | +2/-3 |
| DC_13A_n66A |  |  |  |  | 23 | +2/-3 |
| DC_13A_n71A |  |  |  |  | 23 | +2/-3 |
| DC_13A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_13A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_14A_n2A |  |  |  |  | 23 | +2/-3 |
| DC_14A_n5A |  |  |  |  | 23 | +2/-3 |
| DC_14A_n30A |  |  |  |  | 23 | +2/-3 |
| DC_14A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_14A_n66A |  |  |  |  | 23 | +2/-3 |
| DC_14A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_18A_n3A |  |  |  |  | 23 | +2/-3 |
| DC_18A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_18A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_18A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_18A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_18A_n79A |  |  |  |  | 23 | +2/-3 |
| DC_19A_n1A |  |  |  |  | 23 | +2/-3 |
| DC_19A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_19A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_19A_n79A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_20A_n1A |  |  |  |  | 23 | +2/-3 |
| DC_20A_n3A |  |  |  |  | 23 | +2/-3 |
| DC_20A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_20A_n8A |  |  |  |  | 23 | +2/-3 |
| DC_20A_n38A |  |  |  |  | 23 | +2/-3 |
| DC_20A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_20A_n40A |  |  |  |  | 23 | +2/-3 |
| DC_20A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_20A_n50A |  |  |  |  | 23 | +2/-3 |
| DC_20A_n51A |  |  |  |  | 23 | +2/-3 |
| DC_20A_n77A |  |  |  |  | 23 | +2/-3 |
| DC_20A_n80A |  |  |  |  | 23 | +2/-3 |
| DC_20A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_20A_n82A_ULSUP-TDM_n78A |  |  |  |  | 23 | +2/-3 |
| DC_20A_n83A |  |  |  |  | 23 | +2/-3 |
| DC_21A_n1A |  |  |  |  | 23 | +2/-3 |
| DC_21A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_21A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_21A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_21A_n79A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_25A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_25A_n77A |  |  |  |  | 23 | +2/-3 |
| DC_25A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_26A_n25A |  |  |  |  | 23 | +2/-3 |
| DC_26A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_26A_n77A |  |  |  |  | 23 | +2/-3 |
| DC_26A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_26A_n79A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n1A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n2A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n3A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n5A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n7B |  |  |  |  | 23 | +2/-3 |
| DC_28A_n8A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n20A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n38A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n40A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_28A_n50A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n51A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n66A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n71A7 |  |  |  |  | 23 | +2/-3 |
| DC_28A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_28A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_28A_n79A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n105A7 |  |  |  |  | 23 | +2/-3 |
| DC_28A_n83A_ULSUP-TDM_n41A |  |  |  |  | 23 | +2/-3 |
| DC_28A_n83A_ULSUP-TDM_n78A |  |  |  |  | 23 | +2/-3 |
| DC_30A_n2A |  |  |  |  | 23 | +2/-3 |
| DC_30A_n5A |  |  |  |  | 23 | +2/-3 |
| DC_30A_n12A |  |  |  |  | 23 | +2/-3 |
| DC_30A_n14A |  |  |  |  | 23 | +2/-3 |
| DC_30A_n66A |  |  |  |  | 23 | +2/-3 |
| DC_30A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_38A_n1A |  |  |  |  | 23 | +2/-3 |
| DC_38A_n3A |  |  |  |  | 23 | +2/-3 |
| DC_38A_n8A |  |  |  |  | 23 | +2/-3 |
| DC_38A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_38A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_38A_n79A |  |  |  |  | 23 | +2/-3 |
| DC_39A_n40A |  |  |  |  | 23 | +2/-3 |
| DC_39A_n41A |  |  | 265 | +2/-3 | 23 | +2/-3 |
| DC_39C_n41A |  |  | 265 | +2/-3 | 23 | +2/-3 |
| DC_39A_n78A |  |  |  |  | 23 | +2/-3 |
| DC_39A_n79A |  |  | 265 | +2/-3 | 23 | +2/-3 |
| DC_40A_n1A |  |  |  |  | 23 | +2/-3 |
| DC_40A_n3A |  |  |  |  | 23 | +2/-3 |
| DC_40A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_40A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_40A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_40A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_40C_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_40A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_40C_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_40A_n79A |  |  |  |  | 23 | +2/-3 |
| DC_41A_n1A |  |  |  |  | 23 | +2/-3 |
| DC_41C_n1A |  |  |  |  | 23 | +2/-3 |
| DC_41A_n3A |  |  |  |  | 23 | +2/-3 |
| DC_41C_n3A |  |  |  |  | 23 | +2/-3 |
| DC_41A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_41C_n28A |  |  |  |  | 23 | +2/-3 |
| DC_41A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_41C_n77A |  |  | [266] | [+2/-3] | 23 | +2/-3 |
| DC_41A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_41C_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_41A_n79A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_41A_n79C |  |  |  |  | 23 | +2/-3 |
| DC_41C_n79A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_42A_n1A |  |  |  |  | 23 | +2/-3 |
| DC_42C_n1A |  |  |  |  | 23 | +2/-3 |
| DC_42A_n3A |  |  |  |  | 23 | +2/-3 |
| DC_42C_n3A |  |  |  |  | 23 | +2/-3 |
| DC_42A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_42C_n28A |  |  |  |  | 23 | +2/-3 |
| DC_42A_n51A |  |  |  |  | 23 | +2/-3 |
| DC_42A_n77A |  |  |  |  | N/A | N/A |
| DC_42A_n78A |  |  |  |  | N/A | N/A |
| DC_42A_n79A |  |  |  |  | N/A | N/A |
| DC_48A_n2A |  |  |  |  | 23 | +2/-3 |
| DC_48A_n5A |  |  |  |  | 23 | +2/-3 |
| DC_48A_n12A |  |  |  |  | 23 | +2/-3 |
| DC_48A_n25A |  |  |  |  | 23 | +2/-3 |
| DC_48A_n46A |  |  |  |  | 23 | +2/-3 |
| DC_48A_n66A |  |  |  |  | 23 | +2/-3 |
| DC_48A_n71A |  |  |  |  | 23 | +2/-3 |
| DC_66A_n2A |  |  |  |  | 23 | +2/-3 |
| DC_66A_n5A |  |  |  |  | 23 | +2/-3 |
| DC_66A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_66A_n12A |  |  |  |  | 23 | +2/-3 |
| DC_66A_n14A |  |  |  |  | 23 | +2/-3 |
| DC_66A_n25A |  |  |  |  | 23 | +2/-3 |
| DC_66A_n28A |  |  |  |  | 23 | +2/-3 |
| DC_66A_n30A |  |  |  |  | 23 | +2/-3 |
| DC_66A_n38A |  |  |  |  | 23 | +2/-3 |
| DC_66A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_66A_n46A |  |  |  |  | 23 | +2/-3 |
| DC_66A_n48A |  |  |  |  | 23 | +2/-3 |
| DC_66A_n71A |  |  |  |  | 23 | +2/-3 |
| DC_66A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_66A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_66A_n86A_ULSUP-TDM_n78A |  |  |  |  | 23 | +2/-3 |
| DC_68A_n1A |  |  |  |  | 23 | +2/-3 |
| DC_68A_n3A |  |  |  |  | 23 | +2/-3 |
| DC_68A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_68A_n8A |  |  |  |  | 23 | +2/-3 |
| DC_68A_n20A |  |  |  |  | 23 | +2/-3 |
| DC_68A_n38A |  |  |  |  | 23 | +2/-3 |
| DC_68A_n40A |  |  |  |  | 23 | +2/-3 |
| DC_68A_n41A |  |  |  |  | 23 | +2/-3 |
| DC_68A_n77A |  |  |  |  | 23 | +2/-3 |
| DC_68A_n78A |  |  |  |  | 23 | +2/-3 |
| DC_68A_n79A |  |  |  |  | 23 | +2/-3 |
| DC_71A_n2A |  |  |  |  | 23 | +2/-3 |
| DC_71A_n5A |  |  |  |  | 23 | +2/-3 |
| DC_71A_n7A |  |  |  |  | 23 | +2/-3 |
| DC_71A_n12A7 |  |  |  |  | 23 | +2/-3 |
| DC_71A_n25A |  |  |  |  | 23 | +2/-3 |
| DC_71A_n38A |  |  |  |  | 23 | +2/-3 |
| DC_71A_n41A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_71A_n48A |  |  |  |  | 23 | +2/-3 |
| DC_71A_n66A |  |  |  |  | 23 | +2/-3 |
| DC_71A_n77A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_71A_n78A |  |  | 266 | +2/-3 | 23 | +2/-3 |
| DC_106A_n41A |  |  |  |  | 23 | +2/-3 |
| DC_106A_n48A |  |  |  |  | 23 | +2/-3 |
| NOTE 1: An uplink DC configuration in which at least one of the bands has NOTE 3 in Table 6.2.1-1 in TS 38.101-1 or NOTE 2 in Table 6.2.2-1 in TS 36.101 is allowed to reduce the lower tolerance limit by 1.5 dB when the transmission bandwidths of at least one of the bands is confined within FUL_low and FUL_low + 4 MHz or FUL_high - 4 MHz and FUL_high.NOTE 2: PPowerClass, EN-DC is the maximum UE power specified without taking into account the toleranceNOTE 3: For inter-band EN-DC the maximum power requirement should apply to the total transmitted power over all component carriers (per UE).NOTE 4: Power Class 3 is the default power class unless otherwise stated.NOTE 5: The UE is not required to support PC2 within each individual cell group. Power class support within each individual cell group is signaled separately by the UE.NOTE 6:  The UE supports PC3 within E-UTRA cell group, and supports either PC3 or PC2 within NR cell group. Power class support within each individual cell group is signaled separately by the UE.NOTE 7: Only single switched UL is supported.NOTE 8: Void.NOTE 9: Void. |  |  |  |  |  |  |

Table 6.2B.1.3-1a: Per band power class applicable to REFSENS exceptions (two band UL EN-DC)

| Inter-band ULpower class(NOTE 1) | Uplink bands of same power class |  | Uplink bands of different power class |  |
| --- | --- | --- | --- | --- |
|  | E-UTRA band2 | NR band | E-UTRA band2 | NR band |
| Class 3 | Class 3 | Class 3 | Class 3 | Class 5 |
| Class 2 | Class 3 | Class 3 | Class 3 | Class 2 |
|  | Class 2 | Class 2 | Class 2 | Class 3 |
| Class 1.5 | Class 2 | Class 2 |  |  |
| NOTE 1: Indicated by powerClass/powerClass-v1610.NOTE 2: For the FDD E-UTRA band, only Class 3 is applicable. |  |  |  |  |

If a UE supports a different power class than the default UE power class for an E-UTRA TDD and NR TDD Inter-band EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

– if the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 30% (The exact evaluation period is no less than one radio frame); or

– if the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is not absent and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS38.331 (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power of the default power class or lower;

– shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified sub-clause 6.2B.4;

– Else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 and larger than or equal to 0.5*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS 38.331; or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 30% and larger than or equal to 15% when maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent. (The exact evaluation period is no less than one radio frame):

– shall apply all requirements for power class 2 and set the configured transmitted power class as specified in sub-clause 6.2B.4.

Else shall apply all requirements for the supported power class and set the configured transmitted power class as specified in sub-clause 6.2B.4.

If a UE supports a different power class than the default UE power class for an E-UTRA FDD and NR TDD EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

If UE indicating the two capabilities maxUplinkDutyCycle-FDD-TDD-EN-DC1 and maxUplinkDutyCycle-FDD-TDD-EN-DC2:

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal tomaxUplinkDutyCycle-FDD-TDD-EN-DC1as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

– shall apply all requirements for the supported power class and set the configured transmitted power class as specified in sub-clause 6.2B.4.

– else

– shall apply all requirements for the default power class and set the configured transmitted power as specified sub-clause 6.2B.4;

else

– shall apply all requirements for the supported power class and set the configured transmitted power as specified sub-clause 6.2B.4;

#### 6.2B.1.3a Inter-band NE-DC within FR1

For inter-band NE-DC of E-UTRA and NR in FR1, the following UE power classes define the maximum output power for any transmission bandwidth within the aggregated channel bandwidth. The maximum output power is measured as the sum of the maximum output power at each UE antenna connector. The period of measurement shall be at least one sub frame (1 ms). UE maximum output power shall be measured over all component carriers from different bands. If each band has separate antenna connectors, maximum output power is measured as the sum of maximum output power at each UE antenna connector.

Table 6.2B.1.3a-1: Maximum output power for inter-band NE-DC (two bands)

| NE-DC configuration | Power class 3(dBm) | Tolerance(dB) |
| --- | --- | --- |
| DC_n1A_28A | 23 | +2/-3 |
| DC_n3A_1A | 23 | +2/-3 |
| DC_n3A_8A | 23 | +2/-3 |
| DC_n8A_1A | 23 | +2/-3 |
| DC_n8A_3A | 23 | +2/-3 |
| DC_n28A_3A | 23 | +2/-3 |
| DC_n28A_3C | 23 | +2/-3 |
| DC_n28A_8A | 23 | +2/-3 |
| DC_n28A_20A | 23 | +2/-3 |
| DC_n28A_34A | 23 | +2/-3 |
| DC_n28A_39A | 23 | +2/-3 |
| DC_n28A_40A | 23 | +2/-3 |
| DC_n28A_40C | 23 | +2/-3 |
| DC_n40A_42A | 23 | +2/-3 |
| DC_n41A_3A | 23 | +2/-3 |
| DC_n41A_8A | 23 | +2/-3 |
| DC_n41A_34A | 23 | +2/-3 |
| DC_n41A_39A | 23 | +2/-3 |
| DC_n41A_40A | 23 | +2/-3 |
| DC_n77A_1A | 23 | +2/-3 |
| DC_n77A_3A | 23 | +2/-3 |
| DC_n77A_8A | 23 | +2/-3 |
| DC_n78A_1A | 23 | +2/-3 |
| DC_n78A_3A | 23 | +2/-3 |
| DC_n78A_5A | 23 | +2/-3 |
| DC_n78A_7A | 23 | +2/-3 |
| DC_n78A_8A | 23 | +2/-3 |
| DC_n78A_26A | 23 | +2/-3 |

#### 6.2B.1.4 Inter-band EN-DC including FR2

UE maximum output power requirement for E-UTRA single carrier and CA operation specified in clauses 6.2.2 and 6.2.2A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.2.1, 6.2A.1, and 6.2D.1 of TS 38.101-2 [3] apply.

#### 6.2B.1.4a (Void)

#### 6.2B.1.5 Inter-band EN-DC including both FR1 and FR2

UE maximum output power requirement for E-UTRA single carrier and CA operation specified in clauses 6.2.2 and 6.2.2A of TS 36.101 [4] and for NR single carrier specified in clause 6.2.1 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.2.1, 6.2A.1, and 6.2D.1 of TS 38.101-2 [3] apply. When uplink is EN-DC mode within FR1 only then UE maximum output power requirement is specified in clause 6.2B.1.3 of this specification.

### 6.2B.2 UE maximum output power reduction for DC

#### 6.2B.2.0 General

The UE maximum output power reduction (MPR) specified in this clause is applicable for UEs configured with EN-DC when NS_01 is indicated in the MCG and the SCG. The MPR applies subject to indication in the field modifiedMPRbehavior for the SCG [2].

#### 6.2B.2.1 Intra-band contiguous EN-DC

##### 6.2B.2.1.1 General

When the UE is configured for intra-band contiguous EN-DC, the UE determines the total allowed maximum output power reduction as specified in this clause.

For UE supporting dynamic power sharing the following:

- for the MCG, MPRc in accordance with TS 36.101 [4]

- for the SCG,

MPR'c = MPRNR = MAX( MPRsingle,NR, MPRENDC)

- for the total configured transmission power,

MPRtot = PPowerClass,EN-DC – min(PPowerClass,EN-DC ,10*log10(10^((PPowerClass,E-UTRA - MPRE-UTRA)/10) + 10^((PPowerClass,NR - MPRNR)/10))

where

MPRE-UTRA = MAX(MPRsingle,E-UTRA, MPRENDC )

with

- MPRsingle, E-UTRAis the MPR defined for the E-UTRA transmission in TS 36.101 [4]

- MPRsingle,NR is the MPR defined for the NR transmission in TS 38.101-1 [2]

For UEs not supporting dynamic power sharing the following:

- for the MCG,

MPRc = MAX(MPRsingle,E-UTRA, MPRENDC )

- for the SCG,

MPR'c = MAX( MPRsingle,NR, MPRENDC )

where

- MPRsingle,NR is the MPR defined for the NR transmission in TS 38.101-1 [2]

- MPRsingle,E-UTRA is the MPR defined for the E-UTRA transmission in TS 36.101 [4]

MPRENDC is defined in Clause 6.2B.2.1.2

##### 6.2B.2.1a (Void)

##### 6.2B.2.1.2 MPR for power class 3 and power class 2

MPR in this clause is applicable for power class 3 and power class 2 UEs indicating IE dualPA-Architecture supported with EN-DC power class being the same as the E-UTRA and NR power class, otherwise the UE can use as much MPR as needed to fulfil emissions requirements when scheduled with dual uplink transmission. For UEs scheduled with single uplink transmission, MPR in clause 6.2.4 of TS 36.101 [4] and 6.2.2 of TS 38.101-1 [2] apply. For a UE supporting dynamic power sharing for DC_(n)71AA for which dual simultaneous uplink transmissions are mandatory and A-MPR defined in clause 6.2B.3.1.1 is applied as MPR. The allowed maximum output power reduction applied to transmission on the MCG and the SCG is defined as follows:

MPRENDC = MA

Where MA is defined as follows

MA =  15 ;  0 ≤ B < 0.5

## 10 ;  0.5 ≤ B < 1.0

## 8 ;  1.0 ≤ B < 2.0

## 6 ;  2.0 ≤ B

Where:

For UEs supporting dynamic power sharing,

B = (LCRB_alloc, E-UTRA * 12* SCSE-UTRA + LCRB_alloc,NR * 12 * SCSNR)/1,000,000

For UEs not supporting dynamic power sharing,

For E-UTRA

B = (LCRB_alloc, E-UTRA * 12* SCSE-UTRA + 12 * SCSNR)/1,000,000

Where SCSNR = 15,000 Hz is assumed in calculation of B.

For NR

B = (12* SCSE-UTRA + LCRB_alloc,NR * 12 * SCSNR)/1,000,000

Where SCSE-UTRA = 15,000 Hz is assumed in calculation of B.

and MA is reduced by 1 dB for B < 2.

#### 6.2B.2.2 Intra-band non-contiguous EN-DC

##### 6.2B.2.2.1 General

When the UE is configured for intra-band non-contiguous EN-DC, the UE determines the total allowed maximum output power reduction as specified in this clause.

For UE supporting dynamic power sharing the following:

- for the MCG, MPRc in accordance with TS 36.101 [4]

- for the SCG,

MPR'c = MPRNR = MAX( MPRsingle,NR, MPRENDC)

- for the total configured transmission power,

MPRtot = PPowerClass,EN-DC – min(PPowerClass,EN-DC ,10*log10(10^((PPowerClass,E-UTRA - MPRE-UTRA)/10) + 10^((PPowerClass,NR - MPRNR)/10))

where

MPRE-UTRA = MAX(MPRsingle,E-UTRA, MPRENDC )

with

- MPRsingle, E-UTRAis the MPR defined for the E-UTRA transmission in TS 36.101 [4]

- MPRsingle,NR is the MPR defined for the NR transmission in TS 38.101-1 [2]

For UEs not supporting dynamic power sharing the following

- for the MCG,

MPRc = MAX(MPRsingle,E-UTRA, MPRENDC )

- for the SCG,

MPR'c = MAX( MPRsingle,NR, MPRENDC )

where

- MPRsingle,NR is the MPR defined for the NR transmission in TS 38.101-1 [2]

- MPRsingle,E-UTRA is the MPR defined for the E-UTRA transmission in TS 36.101 [4]

MPRENDC is defined in Clause 6.2B.2.2.2

##### 6.2B.2.2.2 MPR for power class 3 and power class 2

MPR in this clause is applicable for power class 3 and power class 2 UEs indicating IE dualPA-Architecture supported with EN-DC power class being the same as the E-UTRA and NR power class, otherwise the UE can use as much MPR as needed to fulfil emissions requirements when scheduled with dual uplink transmission. For UEs scheduled with single uplink transmission, MPR in clause 6.2.4 of TS 36.101 [4] and 6.2.2 of TS 38.101-1 [2] apply.  The allowed maximum output power reduction for IM3 related emissions applied to transmission on the MCG and the SCG is defined as follows:

MPRENDC = MA

Where MA is defined as follows

MA =  18 ;  0 ≤ B < 1.0

## 17 ;  1.0 ≤ B < 2.0

## 16 ;  2.0 ≤ B < 5.0

## 15 ;  5.0 ≤ B

Where:

For UEs supporting dynamic power sharing,

B = (LCRB_alloc, E-UTRA * 12* SCSE-UTRA + LCRB_alloc,NR * 12 * SCSNR)/ 1,000,000

For UEs not supporting dynamic power sharing,

For E-UTRA

B= (LCRB_alloc, E-UTRA * 12* SCSE-UTRA + 12 * SCSNR)/ 1,000,000

Where SCSNR = 15,000 Hz is assumed in calculation of B.

For NR

B = (12 * SCSE-UTRA + LCRB_alloc,NR * 12 * SCSNR)/ 1,000,000

Where SCSE-UTRA = 15,000 Hz is assumed in calculation of B.

and MA is reduced by 1 dB for B < 2.

#### 6.2B.2.3 Inter-band EN-DC within FR1

For inter-band EN-DC between E-UTRA and FR1 NR, UE maximum output power reduction specified in TS 36.101 [4] and TS 38.101-1 [2] apply for E-UTRA and NR respectively.

#### 6.2B.2.3a Inter-band NE-DC within FR1

For inter-band NE-DC between E-UTRA and FR1 NR, UE maximum output power reduction specified in TS 36.101 [4] and TS 38.101-1 [2] apply for E-UTRA and NR respectively.

#### 6.2B.2.4 Inter-band EN-DC including FR2

UE maximum output power reduction requirement for E-UTRA single carrier and CA operation specified in clauses 6.2.3 and 6.2.3A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.2.2, 6.2A.2 , and 6.2D.2 of TS 38.101-2 [3] apply.

#### 6.2B.2.4a (Void)

#### 6.2B.2.5 Inter-band EN-DC including both FR1 and FR2

UE maximum output power reduction requirement for E-UTRA single carrier and CA operation specified in clauses 6.2.3 and 6.2.3A of TS 36.101 [4] and for NR single carrier specified in clause 6.2.2 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.2.2, 6.2A.2 , and 6.2D.2 of TS 38.101-2 [3] apply.

### 6.2B.3 UE additional maximum output power reduction for EN-DC

#### 6.2B.3.1 Intra-band contiguous EN-DC

##### 6.2B.3.1.0 General

For intra-band contiguous EN-DC band combinations with additional requirements the allowed A-MPR is specified in Table 6.2B.3.1.0-1 for UEs configured with EN-DC and combinations of network signalling values indicated in the E-UTRA and NR cell groups.

Unless otherwise stated the A-MPR specified in clause 6.2B.3.1 for intra-band contiguous EN-DC configurations is the total power reduction allowed including MPR.

Table 6.2B.3.1.0-1: Additional maximum power reduction for Intra-band contiguous EN-DC

| DC configuration | Requirement (clause) | E-UTRA network signalling value | NR network signalling value | A-MPR(clause) |
| --- | --- | --- | --- | --- |
| DC_(n)71AA | 6.5B.2.1.2.1 | NS_35 | NS_35 | 6.2B.3.1.13 |
| DC_(n)41AA1 | 6.5B.2.1.2.26.5B.4.1.1 | NS_01 or NS_04 | NS_04 | 6.2B.3.1.24 |
| NOTE 1: Only applies to UEs that support dual UL transmission for this EN-DC combination.NOTE 2: The additional emission requirement is indicated when the combination of network signalling values in the two CGs is set (only for UEs configured with EN-DC).NOTE 3: The A-MPR is applied as MPR if NS_35 is not signalled.NOTE 4: Void |  |  |  |  |

##### 6.2B.3.1.1 A-MPR for DC_(n)71AA

For UE supporting dynamic power sharing the following:

- for the MCG, A-MPRc in accordance with TS 36.101 [4]

- for the SCG, A-MPR'c = A-MPRDC

- for the total configured transmission power, A-MPRtot = A-MPRDC

with A-MPRDC as defined in this clause.

For UEs not supporting dynamic power sharing the following

- for the MCG,

A-MPRc = A-MPRE-UTRA

- for the SCG,

A-MPR'c = A-MPRNR

with A-MPRE-UTRA and A-MPRNR as defined in this clause.

For DC_(n)71AA with configured with network signaling values as per Table 6.2B.3.1.0-1 the allowed A-MPR is defined by

- for UE indicating support of dynamicPowerSharing in the UE-MRDC-Capability IE

A-MPRDC = CEIL{ MA,DC (A), 0.5}

where A-MPRDC is the total power reduction allowed (dB),

- for OFDM:

MA,DC = 11.00 - 11.67*A;  0.00 < A ≤ 0.30

## 8.10 - 2.00*A;     0.30 < A ≤ 0.80

6.50;        0.80 < A ≤ 1.00

- for DFT-S-OFDM:

MA,DC = 11.00 - 13.33*A;   0.00 < A ≤ 0.30

## 8.00 - 3.33*A;        0.30 < A ≤ 0.60

6.00;        0.60 < A ≤ 1.00

where

$$ A=\frac {L_{CRB,E-UTRA}+L_{CRB,NR}}{N_{RB,E-UTRA}+N_{RB,NR}}$$

with LCRB, E-UTRA and NRB, E-UTRA the number of allocated PRB and transmission bandwidth for MCG, LCRB,NR and NRB,NR the number of allocated PRB and transmission bandwidth for SCG with SCS = 15 kHz.

- for UE not indicating support of dynamicPowerSharing

A-MPRE-UTRA = CEIL{ MA,E-UTRA , 0.5}

A-MPRNR = CEIL{ MA,NR, 0.5}

where A-MPR is the total power reduction allowed per CG with

$$ M_{A,E-UTRA}=M_{A,DC}(A_{E-UTRA,wc})-1-_{E-UTRA}$$

$$ M_{A,NR}=M_{A,DC}(A_{NR,wc})-1-_{NR}$$

$$ A_{E-UTRA,wc}=\frac {L_{CRB,E-UTRA}+1}{N_{RB,E-UTRA}+N_{RB,NR}}$$

$$ A_{NR,wc}=\frac {1+L_{CRB,NR}}{N_{RB,E-UTRA}+N_{RB,NR}}$$

$$∆_{E-UTRA}=10log_{10}\frac {N_{RB,E-UTRA}}{N_{RB,E-UTRA}+N_{RB,NR}}$$

$$∆_{NR}=10log_{10}\frac {N_{RB,NR}}{N_{RB,E-UTRA}+N_{RB,NR}}$$

Where LCRB,NR and NRB,NR the number of allocated PRB and transmission bandwidth for SCG with SCS = 15 kHz.

##### 6.2B.3.1.2 A-MPR for NS_04

6.2B.3.1.2.0 General

When the UE is configured for B41/n41 intra-band contiguous EN-DC and it receives IE NS_04, the UE determines the total allowed maximum output power reduction as specified in this clause. The A-MPR for EN-DC defined in this clause is used instead of MPR defined in 6.2B.2.1, not additively, so EN-DC MPR = 0 when NS_04 is signaled. For UEs scheduled with single uplink transmission, AMPR in clause 6.2.4 of [4] and 6.2.3 of [2] apply.

For UE supporting dynamic power sharing the following:

- for the MCG, A-MPRc in accordance with TS 36.101 [4]

- for the SCG,

A-MPR'c = A-MPRNR = MAX( A-MPRsingle,NR, A-MPRIM3)

- for the total configured transmission power,

A-MPRtot = PPowerClass,EN-DC – min(PPowerClass,EN-DC ,10*log10(10^((PPowerClass,E-UTRA - A-MPRE-UTRA)/10) + 10^((PPowerClass,NR - A-MPRNR)/10))

where

A-MPRE-UTRA = MAX( A-MPRsingle,E-UTRA + MPRsingle,E-UTRA, A-MPRIM3 )

with

- A-MPRsingle, E-UTRA is the A-MPR defined for the E-UTRA transmission in TS 36.101 [4]

- A-MPRsingle,NR is the A-MPR defined for the NR transmission in TS 38.101-1 [2]

- MPRsingle,E-UTRA is the MPR defined for the E-UTRA transmission in TS 36.101 [4]

For UEs not supporting dynamic power sharing the following

- for the MCG,

A-MPRc = MAX( A-MPRsingle, E-UTRA + MPRsingle,E-UTRA, A-MPRIM3 )

- for the SCG,

A-MPR'c = MAX( A-MPRsingle,NR, A-MPRIM3 )

where

- A-MPRsingle, E-UTRAis the A-MPR defined for the E-UTRA transmission in TS 36.101 [4]

- A-MPRsingle,NR is the A-MPR defined for the NR transmission in TS 38.101-1 [2]

- MPRsingle,E-UTRA is the MPR defined for the E-UTRA transmission in TS 36.101 [4]

The UE determines the Allocation Configuration Case and the value of A-MPRIM3 as follows:

If FIM3,low_block,low < 2490.5 MHz

Allocation Configuration Case B. A-MPRIM3 defined in Clause 6.2B.3.1.2.2

Else

Allocation Configuration Case A. A-MPRIM3 defined in Clause 6.2B.3.1.2.1

where

- FIM3,low_block,low = (2 * Flow_alloc,low_edge) – Fhigh_alloc,high_edge

- Flow_alloc,low_edge is the lowermost frequency of lower transmission bandwidth configuration.

- Fhigh_alloc,high_edge is the uppermost frequency of upper transmission bandwidth configuration.

Where the transmission bandwidth configuration for NR is the maximum frequency span covering all the configured SCSSpecificCarrier for scenarios that carrier bandwidths with different SCS can be fully overlapped.

NOTE: For non-dynamic power sharing capable UEs, since the allocation is unknown for one RAT, the edges of the channel transmission bandwidth are used instead of the edges of the RB allocations for that RAT.

6.2B.3.1.2.1 A-MPRIM3 for NS_04 to meet -13 dBm / 1MHz

A-MPR is relative to 26 dBm for a power class 2 Cell Group to support PC1.5 and PC2 EN-DC UE. The same A-MPR is used relative to 23 dBm for a power class 3 Cell Group to support PC2 and PC3 EN-DC UE. The detail A-MPR values are decided based on the modified MPR behaviour in in Annex H.1. For the UE is configured with allocation configurations Case A or Case C (defined in Clause 6.2B.3.2.1), the allowed maximum output power reduction for IM3s applied to transmission on the MCG and the SCG with non-contiguous resource allocation is defined as follows:

A-MPRIM3 = MA

Where MA is defined as follows

MA =  12 ; 0 ≤ B < 0.54

## 10 ; 0.54 ≤ B < 1.08

## 9 ; 1.08 ≤ B < 2.16

## 8.5 ; 2.16 ≤ B < 3.24

## 8 ; 3.24 ≤ B < 5.4

## 6 ; 5.4 ≤ B

Where:

For UEs supporting dynamic power sharing,

B = (LCRB_alloc, E-UTRA * 12* SCSE-UTRA + LCRB_alloc,NR * 12 * SCSNR)/1,000,000

For UEs not supporting dynamic power sharing,

For E-UTRA

B = (LCRB_alloc, E-UTRA * 12* SCSE-UTRA + 12 * SCSNR)/1,000,000

Where SCSNR =15,000 Hz is assumed in calculation of B.

For NR

B = (12* SCSE-UTRA + LCRB_alloc,NR * 12 * SCSNR)/1,000,000

Where SCSE-UTRA = 15,000 Hz is assumed in calculation of B.

and MA is reduced by 1 dB for B < 2.0.

6.2B.3.1.2.2 A-MPR for NS_04 to meet -25 dBm / 1MHz

A-MPR is relative to 26 dBm for a power class 2 Cell Group to support PC1.5 and PC2 EN-DC UE. The same A-MPR is used relative to 23 dBm for a power class 3 Cell Group to support PC2 and PC3 EN-DC UE. The detail A-MPR values are decided based on the modified MPR behaviour in Annex H.1.  For the UE is configured with allocation configurations Case B or Case D (defined in Clause 6.2B.3.2.1), the allowed maximum output power reduction for IM3s applied to transmission on the MCG and the SCG with non-contiguous resource allocation is defined as follows:

A-MPRIM3 = MA

Where MA is defined as follows

MA =  15 ;  0 ≤ B < 1.08

## 14 ;  1.08 ≤ B < 5.4

## 13 ;  5.4 ≤ B < 8.1

## 12 ;  8.1 ≤ B < 25.2

## 10 ;  25.2 ≤ B

Where:

For UEs supporting dynamic power sharing,

B = (LCRB_alloc, E-UTRA * 12* SCSE-UTRA + LCRB_alloc,NR * 12 * SCSNR)/ 1,000,000

For UEs not supporting dynamic power sharing,

For E-UTRA

B = (LCRB_alloc,E-UTRA * 12* SCSE-UTRA + 12 * SCSNR)/1,000,000

Where SCSNR =15,000 Hz is assumed in calculation of B.

For NR

B = (12* SCSE-UTRA + LCRB_alloc,NR * 12 * SCSNR)/1,000,000

Where SCSE-UTRA = 15,000 Hz is assumed in calculation of B.

and MA is reduced by 1 dB.

#### 6.2B.3.2 Intra-band non-contiguous EN-DC

##### 6.2B.3.2.0 General

For intra-band non-contiguous EN-DC band combinations with additional requirements the A-MPR allowed are specified in Table 6.2B.3.2.0-1 for UEs configured with EN-DC and combinations of network signalling values indicated in the E-UTRA and NR cell group(s). Unless otherwise stated the A-MPR specified in clause 6.2B.3.2 for intra-band non-contiguous EN-DC configurations is the total power reduction allowed including MPR. For UEs scheduled with single uplink transmission, AMPR in clause 6.2.4 of [4] and 6.2.3 of [2] apply.

Table 6.2B.3.2.0-1: Allowed power reduction for intra-band non-contiguous EN-DC

| DC configuration | Requirement (clause) | E-UTRA network signalling value | NR network signalling value | A-MPR (clause) |  |
| --- | --- | --- | --- | --- | --- |
| DC_41A_n41A1 | 6.6.3.3.19 and 6.6.2.2.2 of TS 36.101 [4] and 6.5.2.3.2 and 6.5.3.3.1 of TS 38.101-1 [2] | NS_01 or NS_04 | NS_04 | 6.2B.3.2.1 |  |
| NOTE 1: Only applies to UEs that support dual UL transmission for this EN-DC combination.NOTE 2: The requirement applies when the combination of network signalling values in the two CGs is set (only for UEs configured with EN-DC). |  |  |  |  |  |

##### 6.2B.3.2.1 A-MPR for NS_04

When the UE is configured for B41/n41 intra-band non-contiguous EN-DC and it receives IE NS_04, the UE determines the total allowed maximum output power reduction as specified in this clause. The A-MPR for EN-DC defined in this clause is used instead of MPR defined in 6.2B.2.2, not additively, so EN-DC MPR=0 when NS_04 is signaled.

For UE supporting dynamic power sharing the following:

- for the MCG, A-MPRc in accordance with TS 36.101 [4]

- for the SCG,

A-MPR'c = A-MPRNR = MAX( A-MPRsingle,NR, A-MPREN-DC)

- for the total configured transmission power,

A-MPRtot = PPowerClass,EN-DC – min(PPowerClass,EN-DC ,10*log10(10^((PPowerClass,E-UTRA - A-MPRE-UTRA)/10) + 10^((PPowerClass,NR - A-MPRNR)/10))

where

A-MPRE-UTRA = MAX( A-MPRsingle,E-UTRA + MPRsingle,E-UTRA, A-MPREN-DC )

A-MPREN-DC = MAX(A-MPRIM3, A-MPRACLRoverlap )

with

- A-MPRsingle, E-UTRA is the A-MPR defined for the E-UTRA transmission in TS 36.101 [4]

- A-MPRsingle,NR is the A-MPR defined for the NR transmission in TS 38.101-1 [2]

- MPRsingle,E-UTRA is the MPR defined for the E-UTRA transmission in TS 36.101 [4]

For UEs not supporting dynamic power sharing the following

- for the MCG,

A-MPRc = MAX( A-MPRsingle, E-UTRA + MPRsingle,E-UTRA, A-MPRIM3, A-MPRACLRoverlap)

- for the SCG,

A-MPR'c = MAX( A-MPRsingle,NR, A-MPRIM3, A-MPRACLRoverlap)

where

- A-MPRsingle, E-UTRAis the A-MPR defined for the E-UTRA transmission in TS 36.101 [4]

- A-MPRsingle,NR is the A-MPR defined for the NR transmission in TS 38.101-1 [2]

- MPRsingle,E-UTRA is the MPR defined for the E-UTRA transmission in TS 36.101 [4]

The UE determines the Allocation Configuration Case and the value of A-MPRIM3 as follows:

If AND( FIM3,low_block,high < Ffilter,low ,  MAX( SEM-13,high, FIM3,high_block,low ) > Ffilter,high )

Allocation Configuration Case C. A-MPRIM3 defined in Clause 6.2B.3.1.2.1

Else

Allocation Configuration Case D. A-MPRIM3 defined in Clause 6.2B.3.1.2.2

where

- FIM3,low_block,high = (2 * Flow_alloc,high_edge ) – Fhigh_alloc,low_edge

- FIM3,high_block,low = (2 * Fhigh_alloc,low_edge) – Flow_alloc,high_edge

- Flow_alloc,low_edge is the lowermost frequency of lower transmission bandwidth allocation.

- Flow_alloc,high_edge is the uppermost frequency of lower transmission bandwidth allocation.

- Fhigh_alloc,low_edge is the lowermost frequency of upper transmission bandwidth allocation.

- Fhigh_alloc,high_edge is the uppermost frequency of upper transmission bandwidth allocation.

- Ffilter,low = 2480 MHz

- Ffilter,high = 2745 MHz

- SEM-13,high = Threshold frequency where upper spectral emission mask for upper channel drops from -13 dBm / 1MHz to -25 dBm / 1MHz, as specified in Clause6.6.2.2.2 in [4] and Clause 6.5.2.3.2 in [2] respectively.

Where the transmission bandwidth configuration for NR is the maximum frequency span covering all the configured SCSSpecificCarrier for scenarios that carrier bandwidths with different SCS can be fully overlapped

The UE determines the value of A-MPRACLRoverlap as specified in Table 6.2B.3.2.1-1:

Table 6.2B.3.2.1-1: A-MPRACLRoverlap

| Wgap | A-MPRACLRoverlap |
| --- | --- |
| < BWchannel,E-UTRA + BWchannel,NR | 4 dB |
| ≥ BWchannel,E-UTRA + BWchannel,NR | 0 dB |
| NOTE 1: Wgap = Fhigh_channel,low_edge - Flow_channel,high_edge |  |

#### 6.2B.3.3 Inter-band EN-DC within FR1

For inter-band EN-DC between E-UTRA and FR1 NR, UE additional maximum output power reduction specified in TS 36.101 [4] and TS 38.101-1 [2] apply for E-UTRA and NR respectively.

Unless specified in Table 6.2B.3.3-1, for inter-band carrier aggregation with uplink assigned to LTE and NR bands, the requirements in [2] clause 6.2.3 apply for NR uplink component carrier and the requirements in [4] clause 6.2.4 apply for LTE uplink component carrier.

Unless otherwise stated, for inter-band EN-DC with uplink assigned to LTE and NR bands and specified in Table 6.2B.3.3-1, the combined requirements and allowed A-MPR are applibale on both LTE and NR bands when LTE and NR component carriers are active. The requirements in Table 6.2B.3.3-1 are specified in terms of an additional spectrum emission requirement. The emission requirements specified in Table 6.2B.3.3-1 also apply for the frequency ranges that are less than FOOB (MHz) from the edge of the channel bandwidth specified in TS 36.101 [4] and TS 38.101-1 [2], respectively.

Table 6.2B.3.3-1: Additional Requirements for inter-band EN-DC (two-bands)

| NR CA combination | Band | AppliedNS | Requirements (clause)(TS 36.101 [4]) | Requirements (clause)(TS 38.101-1 [2]) | A-MPR(table/clause)(TS 36.101 [4]) | A-MPR(table/clause)(TS 38.101-1 [2]) | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DC_1_n3 | 1 | 05 | 6.6.3.3.1 | 6.6.3.3.1 | Table 6.2.4-1 (NS_05) | N/A | 1 |
|  | n3 | 100 | N/A | 6.5.2.4.2 | N/A | Table 6.2.3.1-2 |  |
| DC_1_n5 | 1 | 05 | 6.6.3.3.1 | N/A | Table 6.2.4-1 (NS_05) | N/A | 1 |
|  | n5 | 100 | N/A | 6.5.2.4.2 | N/A | Table 6.2.3.1-2 |  |
| DC_1_n8 | 1 | 05 | 6.6.3.3.1 | N/A | Table 6.2.4-1 (NS_05) | N/A | 1 |
|  | n8 | 43 | N/A | 6.5.3.3.5 | N/A | Clause 6.2.3.6 |  |
|  |  | 43U | N/A | 6.5.3.3.5, 6.5.2.4.2 | N/A | Clause 6.2.3.6 |  |
| DC_1_n28 | 1 | 05 | 6.6.3.3.1 | N/A | Table 6.2.4-1 (NS_05) | N/A | 2 |
|  | n28 | 17 | N/A | 6.5.3.3.2 | N/A | N/A |  |
| DC_1_n40 | 1 | 05 | 6.6.3.3.1 | N/A | Table 6.2.4-1 (NS_05) | N/A |  |
| DC_1_n41 | 1 | 05 | 6.6.3.3.1 | N/A | Table 6.2.4-1 (NS_05) | N/A |  |
|  | n41 | 47 | N/A | 6.5.3.3.15 | N/A | Table 6.2.3.18-2 |  |
| DC_1_n77 DC_1_n84_ULSUP-TDM_n77 | 1 | 05 | 6.6.3.3.1 | N/A | Table 6.2.4-1 (NS_05) | N/A | 1 |
|  | n84 | 05 | N/A | 6.5.3.3.4 | N/A | Clause 6.2.3.4 |  |
|  |  | 05U | N/A | 6.5.3.3.4 | N/A | Clause 6.2.3.4 |  |
| DC_1_n78DC_1_n84_ULSUP-TDM_n78 | 1 | 05 | 6.6.3.3.1 | N/A | Table 6.2.4-1 (NS_05) | N/A | 1 |
|  | n84 | 05 | N/A | 6.5.3.3.4 | N/A | Clause 6.2.3.4 |  |
|  |  | 05U | N/A | 6.5.3.3.4, 6.5.2.4.2 | N/A | Clause 6.2.3.4 |  |
| DC_1_n79DC_1_n84_ULSUP-TDM_n79 | 1 | 05 | 6.6.3.3.1 | N/A | Table 6.2.4-1 (NS_05) | N/A | 1 |
|  | n84 | 05 | N/A | 6.5.3.3.4 | N/A | Clause 6.2.3.4 |  |
|  |  | 05U | N/A | 6.5.3.3.4, 6.5.2.4.2 | N/A | Clause 6.2.3.4 |  |
| DC_3_n1 | n1 | 05 | N/A | 6.5.3.3.4 | N/A | Clause 6.2.3.4 | 1 |
|  |  | 05U | N/A | 6.5.3.3.4, 6.5.2.4.2 | N/A | Clause 6.2.3.4 |  |
| DC_3_n5 | n5 | 100 | N/A | 6.5.2.4.2 | N/A | Table 6.2.3.1-2 | 1 |
| DC_3_n8 | n8 | 43 | N/A | 6.5.3.3.5 | N/A | Clause 6.2.3.6 | 1 |
|  |  | 43U | N/A | 6.5.3.3.5 | N/A | Clause 6.2.3.6 |  |
| DC_3_n28 | n28 | 17 | N/A | 6.5.3.3.2 | N/A | N/A | 2 |
| DC_3_n41,DC_3_n80_ULSUP-TDM_n41 | n41 | 47 | N/A | 6.5.3.3.15 | N/A | Table 6.2.3.18-2 | 1 |
|  | n80 | 100 | N/A | 6.5.2.4.2 | N/A | Table 6.2.3.1-2 |  |
| DC_8_n1 | n1 | 05 | N/A | 6.5.3.3.4 | N/A | Clause 6.2.3.4 | 1, 3 |
|  |  | 05U | N/A | 6.5.3.3.4, 6.5.2.4.2 | N/A | Clause 6.2.3.4 |  |
| DC_8_n3 | n3 | 100 | N/A | 6.5.2.4.2 | N/A | Table 6.2.3.1-2 | 1, 3 |
| DC_8_n28 | n28 | 17 | N/A | 6.5.3.3.2 | N/A | N/A | 2, 3 |
| DC_8_n41,DC_8_n81_ULSUP-TDM_n41 | n41 | 47 | N/A | 6.5.3.3.15 | N/A | Table 6.2.3.18-2 | 3 |
|  | n81 | 43 | N/A | 6.5.3.3.5 | N/A | Clause 6.2.3.6 |  |
|  |  | 43U | N/A | 6.5.3.3.5 | N/A | Clause 6.2.3.6 |  |
| DC_11_n3 | n3 | 100 | N/A | 6.5.2.4.2 | N/A | Table 6.2.3.1-2 | 1 |
| DC_11_n28 | n28 | 17 | N/A | 6.5.3.3.2 | N/A | N/A | 2 |
| DC_11_n41 | n41 | 47 | N/A | 6.5.3.3.15 | N/A | Table 6.2.3.18-2 |  |
| DC_18_n3 | n3 | 100 | N/A | 6.5.2.4.2 | N/A | Table 6.2.3.1-2 | 1 |
| DC_18_n28 | n28 | 17 | N/A | 6.5.3.3.2 | N/A | N/A | 2 |
| DC_19_n1 | 19 | 08 | 6.6.3.3.3 | N/A | Table 6.2.4-1 (NS_08) | N/A | 1 |
|  | n1 | 05 | N/A | 6.5.3.3.4 | N/A | Clause 6.2.3.4 |  |
|  |  | 05U | N/A | 6.5.3.3.4, 6.5.2.4.2 | N/A | Clause 6.2.3.4 |  |
| DC_19_n77 | 19 | 08 | 6.6.3.3.3 | N/A | Table 6.2.4-1 (NS_08) | N/A |  |
| DC_19_n78 | 19 | 08 | 6.6.3.3.3 | N/A | Table 6.2.4-1 (NS_08) | N/A |  |
| DC_19_n79 | 19 | 08 | 6.6.3.3.3 | N/A | Table 6.2.4-1 (NS_08) | N/A |  |
| DC_21_n1 | 21 | 09 | 6.6.3.3.4 | N/A | Table 6.2.4-1 (NS_08) | N/A | 1 |
|  | n1 | 05 | N/A | 6.5.3.3.4 | N/A | Clause 6.2.3.4 |  |
|  |  | 05U | N/A | 6.5.3.3.4, 6.5.2.4.2 | N/A | Clause 6.2.3.4 |  |
| DC_21_n28 | 21 | 09 | 6.6.3.3.4 | N/A | Table 6.2.4-1 (NS_09) |  | 2 |
|  | n28 | 17 | N/A | 6.5.3.3.2 | N/A | N/A |  |
| DC_21_n77 | 21 | 09 | 6.6.3.3.4 | N/A | Table 6.2.4-1 (NS_09) | N/A |  |
| DC_21_n78 | 21 | 09 | 6.6.3.3.4 | N/A | Table 6.2.4-1 (NS_09) | N/A |  |
| DC_21_n79 | 21 | 09 | 6.6.3.3.4 | N/A | Table 6.2.4-1 (NS_09) | N/A |  |
| DC_28_n1 | 28 | 17 | 6.6.3.3.10 | N/A | Table 6.2.4-1 (NS_17) | N/A | 1, 2 |
|  | n1 | 05 | N/A | 6.5.3.3.4 | N/A | Clause 6.2.3.4 |  |
|  |  | 05U | N/A | 6.5.3.3.4, 6.5.2.4.2 | N/A | Clause 6.2.3.4 |  |
| DC_28_n3 | 28 | 17 | 6.6.3.3.10 | N/A | Table 6.2.4-1 (NS_17) | N/A | 2 |
|  | n3 | 100 | N/A | 6.5.2.4.2 | N/A | Table 6.2.3.1-2 |  |
| DC_28_n5 | 28 | 17 | 6.6.3.3.10 | N/A | Table 6.2.4-1 (NS_17) | N/A | 1, 2 |
|  | n5 | 100 | N/A | 6.5.2.4.2 | N/A | Table 6.2.3.1-2 |  |
| DC_28_n8 | 28 | 17 | 6.6.3.3.10 | N/A | Table 6.2.4-1 (NS_17) | Table 6.2.4-1 (NS_17) | 1, 2 |
|  | n8 | 43 | N/A | 6.5.3.3.5 | N/A | Clause 6.2.3.6 |  |
|  |  | 43U | N/A | 6.5.3.3.5 | N/A | Clause 6.2.3.6 |  |
| DC_28_n40 | 28 | 17 | 6.6.3.3.10 | N/A | Table 6.2.4-1 (NS_17) | N/A | 2 |
| DC_28_n41 | 28 | 17 | 6.6.3.3.10 | N/A | Table 6.2.4-1 (NS_17) | N/A | 2 |
|  | n41 | 47 | N/A | 6.5.3.3.15 | N/A | Table 6.2.3.18-2 |  |
| DC_28_n77 | 28 | 17 | 6.6.3.3.10 | N/A | Table 6.2.4-1 (NS_17) | N/A | 2 |
| DC_28_n78 | 28 | 17 | 6.6.3.3.10 | N/A | Table 6.2.4-1 (NS_17) | N/A | 2 |
| DC_28_n79 | 28 | 17 | 6.6.3.3.10 | N/A | Table 6.2.4-1 (NS_17) | N/A | 2 |
| DC_40_n1 | n1 | 05 | N/A | 6.5.3.3.4 | N/A | Clause 6.2.3.4 | 1 |
|  |  | 05U | N/A | 6.5.3.3.4, 6.5.2.4.2 | N/A | Clause 6.2.3.4 |  |
| DC_40_n41 | n41 | 47 | N/A | 6.5.3.3.15 | N/A | Table 6.2.3.18-2 |  |
| DC_41_n3 | n3 | 100 | N/A | 6.5.2.4.2 | N/A | Table 6.2.3.1-2 | 1 |
| DC_41_n28 | n28 | 17 | N/A | 6.5.3.3.2 | N/A | N/A | 2 |
| DC_42_n1 | n1 | 05 | N/A | 6.5.3.3.4 | N/A | Clause 6.2.3.4 | 1 |
|  |  | 05U | N/A | 6.5.3.3.4, 6.5.2.4.2 | N/A | Clause 6.2.3.4 |  |
| DC_42_n3 | n3 | 100 | N/A | 6.5.2.4.2 | N/A | Table 6.2.3.1-2 | 1 |
| DC_42_n28 | n28 | 17 | N/A | 6.5.3.3.2 | N/A | N/A | 2 |
| NOTE 1: NS_05U, NS_43U and NS_100 can be signalled for NR bands that have UTRA services deployed and protected range is specified in clause 6.5.2.4.2 of TS38.101-1[2] and the requirements in clause 6.5.2.4.2 are only appliable to the signalling band.NOTE 2: Applicable when the assigned NR carrier is confined within 718 MHz and 748 MHz and when the channel bandwidth used is 5 or 10 MHz.NOTE 3: This requirement is applicable only for the following cases: A: for carriers of 5 MHz channel bandwidth when carrier centre frequency (Fc) is within the range 902.5 MHz ≤ Fc < 907.5 MHz with an uplink transmission bandwidth less than or equal to 20 RB; B: for carriers of 5 MHz channel bandwidth when carrier centre frequency (Fc) is within the range 907.5 MHz ≤ Fc ≤ 912.5 MHz without any restriction on uplink transmission bandwidth; C: for carriers of 10 MHz channel bandwidth when carrier centre frequency (Fc) is Fc = 910 MHz with an uplink transmission bandwidth less than or equal to 32 RB with RBstart > 3. |  |  |  |  |  |  |  |

#### 6.2B.3.3A Inter-band NE-DC within FR1

For inter-band NE-DC between E-UTRA and FR1 NR, UE additional maximum output power reduction specified in TS 36.101 [4] and TS 38.101-1 [2] apply for E-UTRA and NR respectively.

Unless specified in Table 6.2B.3.3A-1, for inter-band carrier aggregation with uplink assigned to LTE and NR bands, the requirements in [2] clause 6.2.3 apply for NR uplink component carrier and the requirements in [4] clause 6.2.4 apply for LTE uplink component carrier.

Unless otherwise stated, for inter-band NE-DC with uplink assigned to NR and LTE bands and specified in Table 6.2B.3.3A-1, the combined requirements and allowed A-MPR are applicable on both LTE and NR bands when LTE and NR component carriers are active. The requirements in Table 6.2B.3.3A-1 are specified in terms of an additional spectrum emission requirement. The emission requirements specified in Table 6.2B.3.3A-1 also apply for the frequency ranges that are less than FOOB (MHz) from the edge of the channel bandwidth specified in TS 36.101 [4] and TS 38.101-1 [2], respectively.

Table 6.2B.3.3A-1: Additional Requirements for inter-band NE-DC (two-bands)

| NR CA combination | Band | AppliedNS | Requirements (clause)(TS 36.101 [4]) | Requirements (clause)(TS 38.101-1 [2]) | A-MPR(table/clause)(TS 36.101 [4]) | A-MPR(table/clause)(TS 38.101-1 [2]) | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DC_n1_28 | n1 | 05 | N/A | 6.5.3.3.4 | N/A | Clause 6.2.3.4 | 1, 2 |
|  |  | 05U | N/A | 6.5.3.3.4, 6.5.2.4.2 | N/A | Clause 6.2.3.4 |  |
|  | 28 | 17 | 6.6.3.3.10 | N/A | Table 6.2.4-1 (NS_17) | N/A |  |
| DC_n78_1 | 1 | 05 | 6.6.3.3.1 | N/A | Table 6.2.4-1 (NS_05) | N/A |  |
| NOTE 1: NS_05U can be signalled for NR bands that have UTRA services deployed and protected range is specified in clause 6.5.2.4.2 of TS38.101-1[2] and the requirements in clause 6.5.2.4.2 are only appliable to the signalling band.NOTE 2: Applicable when the assigned NR carrier is confined within 718 MHz and 748 MHz and when the channel bandwidth used is 5 or 10 MHz. |  |  |  |  |  |  |  |

#### 6.2B.3.4 Inter-band EN-DC including FR2

UE additional maximum output power reduction requirement for E-UTRA single carrier and CA operation specified in clauses 6.2.4 and 6.2.4A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.2.3, 6.2A.3 and 6.2D.3 of TS 38.101-2 [3] apply.

#### 6.2B.3.4A (Void)

#### 6.2B.3.5 Inter-band EN-DC including both FR1 and FR2

UE additional maximum output power reduction requirement for E-UTRA single carrier and CA operation specified in clauses 6.2.4 and 6.2.4A of TS 36.101 [4] and for NR single carrier specified in clause 6.2.3 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.2.3, 6.2A.3 and 6.2D.3 of TS 38.101-2 [3] apply.

### 6.2B.4 Configured output power for DC

#### 6.2B.4.1 Configured output power level

##### 6.2B.4.1.1 Intra-band contiguous EN-DC

The following requirements apply for one component carrier per CG configured for synchronous DC.

For intra-band dual connectivity with one uplink serving cell per CG on E-UTRA and NR respectively, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of CG i, i = 1,2, and its total configured maximum transmission power for EN-DC operation $ P_{Total}^{EN-DC}$= 10log10($\hat  {P}_{total}^{EN-DC}$) with $\hat  {P}_{total}^{EN-DC}$ as specified in clause 7.6 of TS 38.213 [10].

The configured maximum output power PCMAX_ E-UTRA,c (p) in sub-frame p for the configured E-UTRA uplink carrier shall be set within the bounds:

PCMAX_L_ E-UTRA,c (p) ≤ PCMAX_ E-UTRA,c (p) ≤  PCMAX H _ E-UTRA,c (p)

where PCMAX_L_ E-UTRA,c and PCMAX H _ E-UTRA,c are the limits for a serving cell c as specified in TS 36.101 [4] clause 6.2.5 modified by PLTE as follows:

PCMAX_L_ E-UTRA,c = MIN {MIN(PEMAX,c , PEMAX, EN-DC, PLTE) – tC_ E-UTRA, c,  (PPowerClass, EN-DC – ΔPPowerClass,EN-DC ), (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA) – MAX(MPRc + A-MPRc + ΔTIB,c  + TC_ E-UTRA, c + TProSe, P-MPRc)}

PCMAX H _ E-UTRA,c = MIN {PEMAX,c, PEMAX, EN-DC , PLTE, PPowerClass, EN-DC, PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA}

where

- PEMAX,EN-DC is the value given by the field p-maxUE-FR1 of the RRCConnectionReconfiguration-v1530 IE as defined in TS 36.331 [8];

- PLTE is the value given by the field p-maxEUTRA-r15 of the RRCConnectionReconfiguration-v1510 IE as defined in TS 36.331 [8] which is the same as PLTE in TS 38.213 [10];

- ∆tC_EUTRA, c = 1.5 dB when NOTE 2 in Table 6.2.2-1 of TS 36.101 [4] applies; ∆tC_EUTRA, c = 0 dB otherwise;

and whenever NS_01 is not indicated within CG 1:

- for a UE indicating support of dynamicPowerSharing, the MPRc and the A-MPRc are determined in accordance with the DCI of serving cell c of the CG 1 and the specification in clause 6.2.4 of TS 36.101 [4];

- for a UE not indicating support of dynamicPowerSharing, the A-MPRc is determined in accordance with clause 6.2B.3.1 with parameters applicable for UEs not indicating support of dynamicPowerSharing and MPRc = 0 dB;

and whenever NS_01 is indicated in CG 1:

- for a UE indicating support of dynamicPowerSharing, the MPRc is determined in accordance with the DCI of serving cell c of the CG 1 and the specification in clause 6.2.4 of TS 36.101 [4];

- for a UE not indicating support of dynamicPowerSharing, the MPRc is determined in accordance with clause 6.2B.2.1 with parameters applicable for UEs not indicating support of dynamicPowerSharing and A-MPRc = 0 dB;

The configured maximum output power PCMAX,f,c,NR (q) in physical channel q for the configured NR carrier shall be set within the bounds:

PCMAX_L,f,c,,NR (q) ≤  PCMAX,f,c,NR (q) ≤  PCMAX_H,f,c,NR (q)

where PCMAX_L,f,c,NR and PCMAX_H,f,c,NR are the limits for a serving cell c as specified in clause 6.2.4 of TS38.101-1 [2] modified  as follows:

PCMAX_L,f,c,,NR = MIN {MIN(PEMAX,c , PEMAX, EN-DC, PNR) - TC_NR, c, (PPowerClass, EN-DC – ΔPPowerClass,EN-DC ),  (PPowerClass,NR – ΔPPowerClass,NR) – MAX(MAX(MPRc,A-MPRc)+ ΔTIB,c + TC_NR, c + ∆TRxSRS,  P-MPRc) }

PCMAX_H,f,c,NR = MIN {PEMAX,c, PEMAX, EN-DC, PNR, PPowerClass, EN-DC, PPowerClass,NR – ΔPPowerClass,NR }

where

- PEMAX,EN-DC is the value given by the field p-maxUE-FR1 of the RRCConnectionReconfiguration-v1530 IE as defined in TS 36.331 [8];

- PLTE signalled by RRC as p-MaxEUTRA-r15 in TS 36.331 [8]

- PNR is the value given by the field  p-NR-FR1 of the PhysicalCellGroupConfig IE as defined in  [9] and signalled by RRC;

- ΔTc_E-UTRA, c = 1.5dB when NOTE 2 in Table 6.2.2-1 in TS 36.101 [4] applies for a serving cell c, otherwise TC_ E-UTRA,c = 0dB;

- TC_NR,c = 1.5dB when NOTE 3 in Table 6.2.1-1 in TS 38.101-1 [2] applies for a serving cell c, otherwise TC_NR,c = 0dB;

- ΔTIB,c specified in clause 6.2B.4.2.1 for EN-DC, the individual Power Class defined in table 6.2B.1.1 and any other additional power reductions parameters specified in clauses 6.2B.2 and 6.2B.3 for EN-DC are applicable to PCMAX_ E-UTRA,c and PCMAX,f,c,NR evaluations.

- PPowerClass, EN-DC is defined in clause 6.2B.1.1 for intra-band contiguous EN-DC;

- PPowerClass,NR is the nominal UE power of the power class that the UE supports for the NR band of the EN-DC combination as defined in clause 6.2.1 of 38.101-1 [2]; in case IE powerClassNRPart-r16 as defined in TS 38.331 [9] is indicated, PPowerClass,NR should use that value instead;

- ΔPPowerClass,NR is 3 dB, 6 dB, or 0 dB according to clause 6.2.4 of TS 38.101-1 [2] for a UE that supports power class 2 or power class 1.5 in the NR band of the EN-DC combination as defined in clause 6.2.1 of TS 38.101-1 [2];

- PPowerClass,E-UTRA is the nominal UE power of the power class that the UE supports for the E-UTRA band of the EN-DC combination as defined in clause 6.2.2 of 36.101 [4];

- ΔPPowerClass,E-UTRA is 3 dB or 0 dB according to clause 6.2.5 of TS 36.101 [4] for a UE that supports power class 2 in the E-UTRA band of the EN-DC combination as defined in clause 6.2.2 of TS 36.101 [4];

- ΔPPowerClass,EN-DC is 3 dB for a power class 2 capable EN-DC UE when  LTE UL/DL configuration is 0 or 6; or LTE UL/DL configuration is 1 and special subframe configuration is 0 or 5; ΔPPowerClass,EN-DC = 3 dB when the IE p-maxUE-FR1 as defined in TS 36.331 [4] is provided and set to the maximum output power of the default power class or lower; ΔPPowerClass,EN-DC is 6 dB for a power class 1.5 capable EN-DC UE when the LTE UL duty cycle is greater than max(50%, maxUplinkDutyCycle-PC2-FR1); ΔPPowerClass,EN-DC is 3 dB for a power class 1.5 capable EN-DC UE when the LTE UL duty cycle is between max(50%,maxUplinkDutyCycle-PC2-FR1) and max(25%,0.5*maxUplinkDutyCycle-PC2-FR1); otherwise ΔPPowerClass,EN-DC = 0 dB; The IE maxUplinkDutyCycle-PC2-FR1 is defined in TS 38.331 [9].

- NOTE: UE reports  ∆PPowerClass,EN-DC when deltaPowerClassReporting-r18 is present, dpc-Reporting-FR1 [7] is configuredand the reporting is triggered only by uplink duty cycle exceedance or by return to the powerClass after the duty cycle exceedance.

and whenever an NS signalling other than NS_01 is indicated within CG 2:

- for a UE indicating support of dynamicPowerSharing, A-MPRc = A-MPR'c with A-MPR'c determined in accordance with clause 6.2B.3.1 and MPRc = 0 dB if transmission(s) in subframe p on CG 1 overlap in time with physical channel q on CG 2;

- for a UE indicating support of dynamicPowerSharing, A-MPRc is determined in accordance with TS 38.101-1 [2] if transmission(s) in subframe p on CG 1 does not overlap in time with physical channel q on CG 2;

- for a UE not indicating support of dynamicPowerSharing, the A-MPRc is determined in accordance with clause 6.2B.3.1 with parameters applicable for UEs not indicating support of dynamicPowerSharing and MPRc = 0 dB;

and whenever NS_01 is indicated in CG 2.

- for a UE indicating support of dynamicPowerSharing, MPRc = MPR'c with MPR'c determined in accordance with clause 6.2B.2.1 and A-MPRc = 0 dB if transmission(s) in subframe p on CG 1 overlap in time with physical channel q on CG 2;

- for a UE indicating support of dynamicPowerSharing, MPRc is determined in accordance with TS 38.101-1 [2] if transmission(s) in subframe p on CG 1 does not overlap in time with physical channel q on CG 2;

- for a UE not indicating support of dynamicPowerSharing, the MPRc is determined in accordance with clause 6.2B.2.1 with parameters applicable for UEs not indicating support of dynamicPowerSharing and A-MPRc = 0 dB;

If the transmissions from NR and E-UTRA do not overlap, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications apply with the modifications specified above. The lower value between PPowerClass, EN-DC or PEMAX, EN-DC shall not be exceeded at any time by UE.

If the EN-DC UE is not supporting dynamic power sharing, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications TS 36.101 [4] and TS 38.101-1 [2] respectively apply with the modifications specified above.

If the UE does not support dynamic power sharing,

$ P_{Total}^{EN-DC}$ = MIN { PEMAX, EN-DC , PPowerClass, EN-DC - ΔPPowerClass,EN-DC } + 0.3 dB

For UEs indicating support of dynamicPowerSharing in the UE-MRDC-Capability IE the UE can configure the total maximum transmission power $ P_{Total}^{EN-DC}$ within the range

PEN-DC,tot_L ≤ $ P_{Total}^{EN-DC}$ ≤  PEN-DC,tot_H

where

PEN-DC,tot_L (p,q) = MIN{ PPowerClass,EN-DC - ΔPPowerClass,EN-DC – MAX{MPRtot, A-MPRtot}, PEMAX,EN-DC}

PEN-DC,tot_H (p,q) = MIN{PPowerClass,EN-DC, PEMAX,EN-DC }

for sub-frame p on CG 1 overlapping with physical channel q on CG 2 and with MPRtot and A-MPRtot in accordance with 6.2B.2.1 and clause 6.2B.3.1, respectively.

The measured total maximum output power PUMAX over both CGs/RATs, measured over the transmission reference time duration is

PUMAX = 10 log10 [pUMAX,c,E-UTRA + pUMAX,f,c,NR],

where pUMAX,c,E-UTRA and pUMAX,c,NR denotes the measured output power of serving cell c for E-UTRA and NR respectively, expressed in linear scale.

For UEs indicating support of dynamicPowerSharing, the measured total configured maximum output power PUMAX shall be within the following bounds:

PCMAX_L -TLOW (PCMAX_L)  ≤  PUMAX  ≤  PCMAX_H + THIGH (PCMAX_H)

with the tolerances TLOW(PCMAX_L) and THIGH(PCMAX_H) for applicable values of PCMAX_L and PCMAX_L specified in Table 6.2B.4.1.1-2.

When an UL subframe transmission p from E-UTRA overlap with a physical channel q from the NR, then for PUMAX evaluation, the E-UTRA subframe p is taken as reference period TREF and always considered as the reference measurement duration and the following rules are applicable.

TREF and Teval are specified in Table 6.2B.4.1.1-1 when same or different subframes and physical channel durations are used in aggregated carriers. The lesser of PPowerClass ,EN-DC and PEMAX,EN-DC shall not be exceeded by the UE during any evaluation period of time.

Table 6.2B.4.1.1-1: PCMAX evaluation window

| transmission duration | TREF | Teval |
| --- | --- | --- |
| Different transmission duration in different RAT carriers | E-UTRA Subframe | Min(Tno_hopping, Physical Channel Length) |

For each TREF, the PCMAX_H is evaluated per Teval and given by the maximum value over the transmission(s) within the Teval as follows:

PCMAX_H  = MAX { PCMAX_ EN-DC _H (p,q) , PCMAX_ EN-DC _H (p,q+1), … , PCMAX_ EN-DC _H (p,q+n) }

where PCMAX_ EN-DC _H are the applicable upper limits for each overlapping scheduling unit pairs (p,q) , (p, q+1) , up to (p, q+n) for each applicable Teval duration, where q+n is the last NR UL physical channel overlapping with E-UTRA subframe p.

While PCMAX_L is computed as follows:

PCMAX_L = MIN { PCMAX_ EN-DC _L (p,q) , PCMAX_ EN-DC _L (p,q+1), … , PCMAX_ EN-DC _L (p,q+n)}

where PCMAX_EN-DC_L are the applicable lower limits for each overlapping scheduling unit pairs (p,q) , (p, q+1) , up to (p, q+n) for each applicable Teval duration, where q+n is the last NR UL physical channel overlapping with E-UTRA subframe p,

With

PCMAX_ EN-DC _H(p,q) = MIN {10 log10 [pCMAX H _ E-UTRA,c (p) + pCMAX H,f,c,NR (q)], PEMAX, EN-DC ,PPowerClass, EN-DC}

And:

a= 10 log10 [pCMAX_ E-UTRA,c (p) +pCMAX,f,c,NR (q) ] > PEN-DC,tot_L

b= 10 log10 [pCMAX_ E-UTRA,c (p) +pCMAX,f,c,NR (q) /X_scale] > PEN-DC,tot_L

If a= FALSE and the configured transmission power spectral density between the MCG and SCG differs by less than 6 dB

PCMAX_ EN-DC _L(p,q) = MIN {10 log10 [pCMAX L _ E-UTRA,c (p) + pCMAX L,f,c,,NR (q)], PEMAX, EN-DC ,PPowerClass, EN-DC - ΔPPowerClass,EN-DC }

ELSE If (a=TRUE) AND (b=FALSE) and the configured transmission power spectral density between the MCG and SCG differs by less than 6 dB

PCMAX_ EN-DC _L(p,q) = MIN {10 log10 [pCMAX L _ E-UTRA,c (p) + pCMAX L,f,c,,NR (q) /X_scale ], PEMAX, EN-DC ,PPowerClass, EN-DC - ΔPPowerClass,EN-DC }

ELSE If b= TRUE or the transmission power after power scaling spectral density between the MCG and SCG differs by more than 6 dB

PCMAX_ EN-DC _L(p,q) = MIN {10 log10 [pCMAX L _ E-UTRA,c (p) ], PEMAX, EN-DC ,PPowerClass, EN-DC- ΔPPowerClass,EN-DC }

where

- pCMAX H _ E-UTRA,c (p) is the E-UTRA higher limit of the maximum configured power expressed in linear scale;

- pCMAX H,f,c,NR (q) is the NR higher limit of the maximum configured power expressed in linear scale;

- pCMAX L _ E-UTRA,c (p) is the E-UTRA lower limit of the maximum configured power expressed in linear scale;

- pCMAX L,f,c,NR (q) is the NR lower limit of the maximum configured power expressed in linear scale;

- PPowerClass, EN-DC is defined in clause 6.2B.1.1 for intra-band EN-DC;

- X_scale is the linear value of X dB which is configured by RRC and can only take values [0 , 6] dB

- pCMAX  E-UTRA,c (p) is the linear value of PCMAX  E-UTRA,c (p), the real configured max power for E-UTRA

- pCMAX,f,c  NR (q) is the linear value of PCMAX,f,c,NR (q), the real configured max power of NR

Table 6.2B.4.1.1-2: PCMAX tolerance for Dual Connectivity E-UTRA-NR

| PCMAX(dBm) | ToleranceTLOW (PCMAX_L) (dB) | ToleranceTHIGH (PCMAX_H) (dB) |
| --- | --- | --- |
| 23 ≤ PCMAX ≤ 33 | 3.0 | 2.0 |
| 22 ≤ PCMAX < 23 | 5.0 | 2.0 |
| 21 ≤ PCMAX< 22 | 5.0 | 3.0 |
| 20 ≤ PCMAX < 21 | 6.0 | 4.0 |
| 16 ≤ PCMAX < 20 | 5.0 |  |
| 11 ≤ PCMAX < 16 | 6.0 |  |
| -40 ≤ PCMAX < 11 | 7.0 |  |

If the UE supports dynamic power sharing, and when E-UTRA and NR transmissions overlap and the condition (If (a=TRUE) AND (b=FALSE)) is met, SCG shall be transmitted and the following supplementary minimum requirement apply for the measured SCG power, PUMAX,f,c,NR (q), under nominal conditions and unless otherwise stated

10log(pCMAX L,f,c,NR(q)/X_scale)  –  TLOW (10log(pCMAX L,f,c,NR(q)/X_scale) )}  ≤  PUMAX,f,c,NR (q) ≤  10log(pCMAX H, f,c,NR (q)) + THIGH (10log(pCMAX H, f,c,NR (q))).

with the tolerances TLOW and THIGH for applicable values of PCMAX specified in Table 6.2B.4.1.1-2.

If the UE supports dynamic power sharing, the measured maximum output power in subframe p on CG 1, pUMAX,c,E-UTRA,  shall meet the requirements in clause 6.2.5 in TS 36.101 [4] with the limits PCMAX_L,c and PCMAX_H,c replaced by PCMAX_L_ E-UTRA,c and PCMAX_H_ E- UTRA,c as specified above, respectively.

If the configured transmission power spectral density between the MCG and SCG differs by more than 6 dB, then

PUMAX,f,c,NR (q) ≤ 10log(pCMAX H, f,c,NR (q)) + THIGH (10log(pCMAX H, f,c,NR (q))).

##### 6.2B.4.1.1a Intra-band contiguous NE-DC

The following requirements apply for one component carrier per CG configured for synchronous DC.

For intra-band dual connectivity with one uplink serving cell per CG on E-UTRA and NR respectively, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of CG i, i = 1,2, and its total configured maximum transmission power for NE-DC operation $ P_{Total}^{NE-DC}$= 10log10($\hat  {P}_{total}^{NE-DC}$) with $\hat  {P}_{total}^{NE-DC}$ as specified in clause 7.6.1A of TS 38.213 [10].

The configured maximum output power PCMAX_ E-UTRA,c (p) in sub-frame p for the configured E-UTRA uplink carrier shall be set within the bounds:

PCMAX_L_ E-UTRA,c (p) ≤ PCMAX_ E-UTRA,c (p) ≤  PCMAX H _ E-UTRA,c (p)

where PCMAX_L_ E-UTRA,c and PCMAX H _ E-UTRA,c are the limits for a serving cell c as specified in TS 36.101 [4] clause 6.2.5 modified by PLTE as follows:

PCMAX_L_ E-UTRA,c = MIN { MIN(PEMAX, NE-DC , PEMAX,c , PLTE) – tC_E-UTRA, c, (PPowerClass, NE-DC – ΔPPowerClass, NE-DC), (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA) – MAX(MPRc + A-MPRc + ΔTIB,c  + TC_ E-UTRA, c + TProSe, P-MPRc)}

PCMAX H _ E-UTRA,c = MIN {PEMAX,c,  PEMAX, NE-DC , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC), PLTE, (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA)}

with exception that

- if no symbol of slot  of the NR that is indicated as uplink or flexible by TDD-UL-DL-ConfigurationCommon or TDD-UL-DL-ConfigDedicated overlaps with subframe  of the E-UTRA; or

- if NR slot(s) that is indicated as downlink by TDD-UL-DL-ConfigurationCommon or TDD-UL-DL-ConfigDedicated does not overlap with subframe  of the E-UTRA; then

PCMAX_L_ E-UTRA,c = MIN { MIN(PEMAX, NE-DC , PEMAX,c) – tC_E-UTRA, c, (PPowerClass, NE-DC – ΔPPowerClass, NE-DC), (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA) – MAX(MPRc + A-MPRc + ΔTIB,c  + TC_ E-UTRA, c + TProSe, P-MPRc)}

PCMAX H _ E-UTRA,c = MIN {PEMAX,c,  PEMAX, NE-DC , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC), (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA)}

The configured maximum output power PCMAX,f,c,NR (q) in physical-channel q for the configured NR carrier shall be set within the bounds:

PCMAX_L,f,c,NR (q) ≤  PCMAX,f,c,NR (q) ≤  PCMAX_H,f,c,NR (q)

where PCMAX_L,f,c,NR and PCMAX_H,f,c,NR are the limits for a serving cell c as specified in clause 6.2.4 of TS 38.101-1 [2] modified by PNR as follows:

PCMAX_L,f,c,NR = MIN { MIN(PEMAX, NE-DC , PEMAX,c , PNR) – tC_NR, c, (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), (PPowerClass,NR – ΔPPowerClass,NR) – MAX(MPRc + A-MPRc+ ΔTIB,c + TC_NR, c + ∆TRxSRS,  P-MPRc) }

PCMAX_H,f,c,NR = MIN {PEMAX,c, PEMAX, NE-DC, PNR, (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), PPowerClass,NR – ΔPPowerClass,NR}

- PEMAX,NE-DC signalled by RRC as p-UE-FR1 in TS 38.331 [9];

- PLTE signalled by RRC as p-MaxEUTRA in TS 36.331 [8];

- PNR signalled by RRC as p-NR-FR1 defined in TS 38.331 [9];

- ΔTc_E-UTRA,c = 1.5dB when NOTE 2 in Table 6.2.2-1 in TS 36.101 [4] applies for a serving cell c, otherwise TC_ E-UTRA,c = 0dB;

- TC_NR,c = 1.5dB when NOTE 3 in Table 6.2.1-1 in TS 38.101-1 [2] applies for a serving cell c, otherwise TC_NR,c = 0dB;

- ΔTIB,c is specified in clause 6.2B.4.2;

- PPowerClass, NE-DC is defined in clause 6.2B.1.1a for intra-band contiguous NE-DC;

- ΔPPowerClass,NE-DC = 3 dB for a power class 2 capable NE-DC UE when requirements of default power class had been applied as specified in sub-clause 6.2B.1; otherwise ΔPPowerClass,NE-DC = 0 dB;

- PPowerClass,NR is the nominal UE power of the power class that the UE supports for the NR band of the NE-DC combination as defined in clause 6.2.1 of 38.101-1 [2]; in case powerClassNRPart as defined in TS 38.331 [9] is indicated, PPowerClass,NR should use that value instead.

- ΔPPowerClass,NR is 3 dB or 0 dB according to clause 6.2.4 of TS 38.101-1 [2] for a UE that supports power class 2 in the NR band of the EN-DC combination as defined in clause 6.2.1 of TS 38.101-1 [2];

- PPowerClass,E-UTRA is the nominal UE power of the power class that the UE supports for the E-UTRA band of the NE-DC combination as defined in clause 6.2.2 of 36.101 [4];

- ΔPPowerClass,E-UTRA is 3 dB or 0 dB according to clause 6.2.5 of TS 36.101 [4] for a UE that supports power class 2 in the E-UTRA band of the EN-DC combination as defined in clause 6.2.2 of TS 36.101 [4];

If the transmissions from NR and E-UTRA do not overlap, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications apply with the modifications specified above. The lower value between PPowerClass, NE-DC or PEMAX, NE-DC shall not be exceeded at any time by UE.

$ P_{Total}^{NE-DC}$ = 10log10($\hat  {P}_{total}^{NE-DC}$) with $ P_{Total}^{NE-DC}$ the configured maximum transmission power for NE-DC operation as specified in clause 7.6 of TS 38.213 [10].

The total configured maximum transmission power is

$ P_{Total}^{NE-DC}$= MIN { PEMAX, NE-DC ,PPowerClass, NE-DC – ΔPPowerClass, NE-DC }

If the UE does not support dynamic power sharing,

$ P_{Total}^{NE-DC}$ = MIN { PEMAX, NE-DC , PPowerClass, NE-DC - ΔPPowerClass,EN-DC } + 0.3 dB

If the NE-DC UE is not supporting dynamic power sharing, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications TS 36.101 [4] and TS 38.101-1 [2] respectively apply with the modifications specified above and $ P_{Total}^{NE-DC}$ applies.

##### 6.2B.4.1.2 Intra-band non-contiguous EN-DC

The following requirements apply for one component carrier per CG configured for synchronous DC. The CG(s) are indexed by j = 1 for MCG and j = 2 for SCG.

The configured maximum output power PCMAX_ E-UTRA,c (p) in sub-frame p for the configured E-UTRA uplink carrier shall be set in accordance with clause 6.2B.4.1.1 but where

- for a UE not indicating support of dynamicPowerSharing, the A-MPRc determined in accordance with clause 6.2B.3.2 with parameters applicable for UEs not indicating support of dynamicPowerSharing and MPRc = 0 dB;

whenever NS_01 is not indicated within CG 1 while

- for a UE not indicating support of dynamicPowerSharing, the MPRc determined in accordance with clause 6.2B.2.2 with parameters applicable for UEs not indicating support of dynamicPowerSharing and A-MPRc = 0 dB;

whenever NS_01 is indicated in CG 1.

The configured maximum output power PCMAX,f,c,NR (q) in physical channel q for the configured NR carrier shall be set in accordance with clause 6.2B.4.1.1 but where

- for a UE indicating support of dynamicPowerSharing, A-MPRc = A-MPR'c with A-MPR'c determined in accordance with clause 6.2B.3.2 and MPRc = 0 dB if transmission(s) in subframe p on CG 1 overlap in time with physical channel q on CG 2;

- for a UE indicating support of dynamicPowerSharing, A-MPRc is determined in accordance with TS 38.101-1 [2] if transmission(s) in subframe p on CG 1 does not overlap in time with physical channel q on CG 2;

- for a UE not indicating support of dynamicPowerSharing, the A-MPRc is determined in accordance with clause 6.2B.3.2 with parameters applicable for UEs not indicating support of dynamicPowerSharing and MPRc = 0 dB;

whenever NS_01 is not indicated in CG 2 while

- for a UE indicating support of dynamicPowerSharing, MPRc = MPR'c with MPR'c determined in accordance with clause 6.2B.2.2 and A-MPRc = 0 dB if transmission(s) in subframe p on CG 1 overlap in time with physical channel q on CG 2;

- for a UE indicating support of dynamicPowerSharing, MPRc is determined in accordance with TS 38.101-1 [2] if transmission(s) in subframe p on CG 1 does not overlap in time with physical channel q on CG 2;

- for a UE not indicating support of dynamicPowerSharing, the MPRc is determined in accordance with clause 6.2B.2.2 with parameters applicable for UEs not indicating support of dynamicPowerSharing and A-MPRc = 0 dB;

whenever NS_01 is indicated in CG 2.

For UEs indicating support of dynamicPowerSharing in the UE-MRDC-Capability IE, the UE can configure the total transmission power in accordance with clause 6.2B.4.1.1 but with Ppowerclass,EN-DC the EN-DC power class of the intra-band non-contiguous band combination configured and A-MPR determined in accordance with clause 6.2B.3.2.

The total maximum output power PUMAX over both CGs is measured in accordance with clause 6.2B.4.1.1 and shall be within the limits specified in clause 6.2B.4.1.1 but with parameters applicable for the non-contiguous band combination configured.

The maximum output power levels pUMAX,c,E-UTRA and pUMAX,f,c,NR for the CGs are measured in accordance with clause 6.2B.4.1.1 and shall be within the limits specified in clause 6.2B.4.1.1 but with parameters applicable for the non-contiguous band combination configured.

6.2B.4.1.3 Inter-band EN-DC within FR1

For inter-band dual connectivity with one uplink serving cell or more than one uplink serving cells configured for intra-band UL CA on the E-UTRA CG and one uplink serving cell on the NR CG or more than one uplink serving cells configured for intra-band UL CA, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of CG i, i = 1,2, and its total configured maximum transmission power for EN-DC operation, $ P_{Total}^{EN-DC}$= 10log10($\hat  {P}_{total}^{EN-DC}$) with $\hat  {P}_{total}^{EN-DC}$ as specified in clause 7.6 of TS 38.213 [10]. For EN-DC with more than one uplink serving cells configured for intra-band UL CA on the E-UTRA CG, the PCMAX applies to the entire E-UTRA CG. For EN-DC with more than one uplink serving cells configured for intra-band UL CA on the NR CG, the PCMAX applies to the entire NR CG.

For a UE configured with EN-DC and serving cell frame structure type 1, if the UE is configured with subframeAssignment-r15 for the serving cell and E-UTRA Pcell is FDD, the UE is not expected to be configured with more than one serving cells in the uplink.

The configured maximum output power PCMAX_ E-UTRA,c (p) in sub-frame p for the configured E-UTRA uplink carrier(s) shall be set within the bounds:

PCMAX_L_ E-UTRA,c (p) ≤  PCMAX_ E-UTRA,c (p) ≤  PCMAX H _ E-UTRA,c (p)

where PCMAX_L_ E-UTRA,c and PCMAX H _ E-UTRA,c are the limits for a serving cell c as specified in TS 36.101 [4] clause 6.2.5 modified by PLTE as follows:

PCMAX_L_ E-UTRA,c = MIN { PEMAX, EN-DC , (PPowerClass, EN-DC – ΔPPowerClass,EN-DC ), MIN(PEMAX,c , PLTE) – tC_ E-UTRA, c,  (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA) – MAX(MPRc + A-MPRc + ΔTIB,c  + tC_ E-UTRA, c + TProSe, P-MPRc)}

PCMAX H _ E-UTRA,c = MIN {PEMAX,c,  PEMAX, EN-DC  , (PPowerClass, EN-DC – ΔPPowerClass,EN-DC ), PLTE, PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA}

For EN-DC with more than one uplink serving cells configured for intra-band UL CA on the E-UTRA CG, PCMAX_L_ E-UTRA,c and PCMAX H _ E-UTRA,c are the limits for the E-UTRA CG as specified in TS 36.101 [4] clause6.2.5A modified by PLTE as follows:

PCMAX_L_ E-UTRA,c  = MIN{10 log10 ∑ pEMAX,c  - TC , (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA) – MAX(MPR + A-MPR + ΔTIB,c + TC + TProSe, P-MPR ), PLTE, PPowerClass,EN-DC }

PCMAX H _ E-UTRA,c  = MIN{10 log10 ∑ pEMAX,c , PPowerClass,E-UTRA, PLTE, PPowerClass,EN-DC}

The configured maximum output power PCMAX,f,c,NR (q) in physical-channel q for the configured NR carrier shall be set within the bounds:

PCMAX_L,f,c,NR (q) ≤  PCMAX,f,c,NR (q) ≤  PCMAX_H,f,c,NR (q)

where PCMAX_L,f,c,NR and PCMAX_H,f,c,NR are the limits for a serving cell c as specified in clause 6.2.4 of TS 38.101-1 [2] modified as follows:

PCMAX_L,f,c,NR = MIN { PEMAX, EN-DC  , (PPowerClass, EN-DC – ΔPPowerClass,EN-DC ), MIN(PEMAX,c , PNR ) - TC_NR, c,  (PPowerClass,NR – ΔPPowerClass,NR) – MAX(MAX(MPRc, A-MPRc)+ ΔTIB,c + TC_NR, c + ∆TRxSRS,  P-MPRc) }

PCMAX_H,f,c,NR = MIN {PEMAX,c, PEMAX, EN-DC  , (PPowerClass, EN-DC – ΔPPowerClass,EN-DC ), PNR , PPowerClass,NR – ΔPPowerClass,NR }

For EN-DC with more than one uplink serving cells configured for intra-band UL CA on the NR CG, PCMAX_L,f,c, NR and PCMAX_H,f,c, NR are the limits for the NR CG as specified in [2] subclause 6.2A.4 modified by PNR as follows:

PCMAX_L,f,c,NR  = MIN{10 log10 ∑ pEMAX,c  - TC , PEMAX,CA, PPowerClass,NR – MAX(MPR + A-MPR + ΔTIB,c + T_NR ,C + TRxSRS, P-MPR ), PNR, PPowerClass,EN-DC }

PCMAX_H,f,c,NR  = MIN{10 log10 ∑ pEMAX,c , PEMAX,CA, PPowerClass,NR, PNR, PPowerClass,EN-DC}

where

- PEMAX,EN-DC is the value given by the field p-maxUE-FR1 of the RRCConnectionReconfiguration-v1530 IE as defined in TS 36.331 [8];

- If more than one E-UTRA uplink serving cell is configured as intra-band UL CA in the E-UTRA CG, PPowerClass refers to the maximum output power of the E-UTRA intra-band CA power class given in Table 6.2.2A-1 of TS 36.101 [4],

- If more than one NR uplink serving cell is configured as intra-band UL CA in the NR CG, PPowerClass refers to the maximum output power of the NR intra-band CA power class given in sub clause 6.2A.1 of [2],

- PLTE is the value given by the field p-maxEUTRA-r15 of the RRCConnectionReconfiguration-v1510 IE as defined in TS 36.331 [8];

- If more than one E-UTRA uplink serving cell is configured as intra-band UL CA in the E-UTRA CG, MPRc = MPR and A-MPRc = A-MPR with MPR and A-MPR specified in clause 6.2.3A and clause 6.2.4A of TS 36.101 [4] respectively. There is one power management term for the UE, denoted P-MPR, and P-MPR c = P-MPR. PCMAX_ E-UTRA,c is calculated under the assumption that the transmit power is increased by the same amount in dB on all component carriers within the E-UTRA CG.

- If more than one NR uplink serving cell is configured as intra-band UL CA in the NR CG, MPRc and A-MPRc are determined by subclause 6.2.2 of [2]. There is one power management term for the UE, denoted P-MPR, and P-MPR c = P-MPR.

- PNR is the value given by the field p-NR-FR1 of the PhysicalCellGroupConfig IE as defined in TS 38.331 [9];

- Δtc_E-UTRA, c = 1.5 dB when NOTE 2 in Table 6.2.2-1 in TS 36.101 [4] applies for a serving cell c, otherwise TC_ E-UTRA,c = 0 dB;

- TC_NR,c = 1.5dB when NOTE 3 in Table 6.2.1-1 in TS 38.101-1 [2] applies for a serving cell c, otherwise TC_NR,c = 0 dB;TC_NR,C is the highest value TC_NR,C among all serving cells c if more than one NR uplink serving cell is configured as intra-band UL CA in the NR CG;

- PPowerClass, EN-DC is the nominal UE power class indicated by PowerClass defined in clause 6.2B.1.3 for inter-band EN-DC;

- If the UE indicates higherPowerLimitMRDC-r17 and ΔPPowerClass,EN-DC = 0, PPowerClass,EN-DC is replaced by the sum of the linear powers of PPowerClass,NR and PPowerClass,E-UTRA converted to dB;

- If the UE further indicates powerBoosting-pi2BPSK-QPSK-Modified-r18 or powerBoosting-pi2BPSK-QPSK-r18, and if IE powerBoostPi2BPSK-r18 and/or powerBoostQPSK-r18 is set to 1 as defined in TS 38.101-1 [2] for any of the NR bands that comprise the band combination, PPowerClass,NR is replaced by PPowerClass,NR + ΔPPowerBoost and PPowerClass,EN-DC is replaced by the sum of the linear powers of PPowerClass,NR + ΔPPowerBoost and PPowerClass,E-UTRA converted to dB;

- ∆PPowerClass,EN-DC = 3 dB for a power class 2 capable EN-DC UE when requirements of default power class had been applied as specified in sub-clause 6.2B.1; otherwise ∆PPowerClass,EN-DC = 0 dB;

NOTE: UE reports ∆PPowerClass,EN-DC when deltaPowerClassReporting-r18 is present, dpc-Reporting-FR1 [7] is configured and the reporting is triggered only by uplink duty cycle exceedance or by return to the powerClass after the duty cycle exceedance.

- PPowerClass,NR is the nominal UE power of the power class indicated by ue-PowerClass that the UE supports for the NR band and for NR intra-band UL CA of the EN-DC combination as defined in clause 6.2.1 or 6.2A1.1 of 38.101-1 [2]; in case IE powerClassNRPart-r16 as defined in TS 38.331 [9] is indicated, PPowerClass,NR should use that value instead;

- ΔPPowerClass,NR is 3 dB or 0 dB according to clause 6.2.4 of TS 38.101-1 [2] for a UE that supports power class 2 in the NR band of the EN-DC combination as defined in clause 6.2.1 of TS 38.101-1 [2];

- PPowerClass,E-UTRA is the nominal UE power of the power class indicated by ue-PowerClass-N-r13 that the UE supports for the E-UTRA band or indicated by ue-CA-PowerClass-N E-UTRA intra-band UL CA of the EN-DC combination as defined in clause 6.2.2 or 6.2.2A of 36.101 [4];

- ΔPPowerClass,E-UTRA is 3 dB or 0 dB according to clause 6.2.5 of TS 36.101 [4] for a UE that supports power class 2 in the E-UTRA band of the EN-DC combination as defined in clause 6.2.2 of TS 36.101 [4];

- ΔTIB,c specified in clause 6.2B.4.2.3 for EN-DC, the individual Power Class defined in table 6.2B.1.3 and any other additional power reductions parameters specified in clauses 6.2B.2 and 6.2B.3for EN-DC are applicable to PCMAX_ E-UTRA,c and PCMAX,f,c,NR evaluations.

- ∆TRxSRS is the highest value among all serving cells c.

If the transmissions from NR and E-UTRA do not overlap, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications apply with the modifications specified above. The lower value between PPowerClass, EN-DC or PEMAX, EN-DC shall not be exceeded at any time by UE.

$ P_{Total}^{EN-DC}$ = 10log10($\hat  {P}_{total}^{EN-DC}$) with $ P_{Total}^{EN-DC}$ the configured maximum transmission power for EN-DC operation as specified in clause 7.6 of TS 38.213 [10].

The total configured maximum transmission power for both synchronous and non-synchronous operation is

$ P_{Total}^{EN-DC}$= MIN { PEMAX, EN-DC ,PPowerClass, EN-DC – ΔPPowerClass, EN-DC }

If the UE does not support dynamic power sharing,

$ P_{Total}^{EN-DC}$= MIN { PEMAX, EN-DC ,PPowerClass, EN-DC  – ΔPPowerClass, EN-DC } + 0.3 dB

If the EN-DC UE does not support dynamic power sharing, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications TS 36.101 [4] and TS 38.101-1 [2] respectively apply with the modifications specified above and $ P_{Total}^{EN-DC}$ applies.

When a UE supporting dynamic sharing is configured for overlapping E-UTRA uplink and NR uplink transmissions, the UE can set its configured maximum output power PCMAX_ E-UTRA,c and PCMAX,f,c,NR for the configured E-UTRA and NR uplink carriers, respectively, and its configured maximum transmission power for EN-DC operation, $\hat  {P}_{Total}^{EN-DC}$, as specified above.

The measured total maximum output power PUMAX over both CGs/RATs, measured over the transmission reference time duration is

PUMAX = 10 log10 [pUMAX,c,E-UTRA + pUMAX,c,NR],

where pUMAX,c,E-UTRA and pUMAX,c,NR denotes the measured output power of serving cell c for E-UTRA and NR respectively, expressed in linear scale.

The measured total configured maximum output power PUMAX shall be within the following bounds:

PCMAX_L -TLOW (PCMAX_L)  ≤  PUMAX  ≤  PCMAX_H + THIGH (PCMAX_H)

with the tolerances TLOW(PCMAX_H) and THIGH(PCMAX_H) for applicable values of PCMAX specified in Table 6.2B.4.1.3-2.

When an UL subframe transmission p from E-UTRA overlap with a physical-channel q from the NR, then for PUMAX evaluation, the E-UTRA subframe p is taken as reference period TREF and always considered as the reference measurement duration and the following rules are applicable.

TREF and Teval are specified in Table 6.2B.4.1.3-1 when same or different subframe and physical-channel durations are used in aggregated carriers. The lesser of PPowerClass ,EN-DC and PEMAX,EN-DC shall not be exceeded by the UE during any evaluation period of time where PPowerClass ,EN-DC is replaced by the sum of the linear powers of PPowerClass,NR and PPowerClass,E-UTRA converted to dB if the UE indicates higherPowerLimitMRDC-r17.

Table 6.2B.4.1.3-1: PCMAX evaluation window

| transmission duration | TREF | Teval |
| --- | --- | --- |
| Different transmission duration in different RAT carriers | E-UTRA Subframe on all aggregated cells of E-UTRA | Min(Tno_hopping, Physical Channel Length) on all aggregated cells of NR |

For each TREF, the PCMAX_H is evaluated per Teval and given by the maximum value over the transmission(s) within the Teval as follows:

PCMAX_H  = MAX { PCMAX_ EN-DC _H (p,q) , PCMAX_ EN-DC _H (p,q+1), … , PCMAX_ EN-DC _H (p,q+n) }

where PCMAX_ EN-DC _H are the applicable upper limits for each overlapping scheduling unit pairs (p,q) , (p, q+1) , up to (p, q+n) for each applicable Teval duration, where q+n is the last NR UL physical-channel overlapping with E-UTRA subframe p.

While PCMAX_L is computed as follows:

PCMAX_L = MIN { PCMAX_ EN-DC _L (p,q) , PCMAX_ EN-DC _L (p,q+1), … , PCMAX_ EN-DC _L (p,q+n)}

where PCMAX_EN-DC_L are the applicable lower limits for each overlapping scheduling unit pairs (p,q) , (p, q+1) , up to (p, q+n) for each applicable Teval duration, where q+n is the last NR UL physical-channel overlapping with E-UTRA subframe p,

With

PCMAX_ EN-DC _H(p,q) = MIN {10 log10 [pCMAX H _ E-UTRA,c (p) + pCMAX H,f,c,NR (q)], PEMAX, EN-DC ,PPowerClass, EN-DC}

And:

a= 10 log10 [pCMAX_ E-UTRA,c (p) +pCMAX,f,c,NR (q) ] > $ P_{Total}^{EN-DC}$

b= 10 log10 [pCMAX_ E-UTRA,c (p) +pCMAX,f,c,NR (q) /X_scale] > $ P_{Total}^{EN-DC}$

If a= FALSE

PCMAX_ EN-DC _L(p,q) = MIN {10 log10 [pCMAX L _ E-UTRA,c (p) + pCMAX L,f,c,NR (q)], PEMAX, EN-DC ,PPowerClass, EN-DC}

ELSE If (a=TRUE) AND (b=FALSE)

PCMAX_ EN-DC _L(p,q) = MIN {10 log10 [pCMAX L _ E-UTRA,c (p) + pCMAX L,f,c,NR (q) /X_scale ], PEMAX, EN-DC ,PPowerClass, EN-DC}

ELSE If b= TRUE

PCMAX_ EN-DC _L(p,q) = MIN {10 log10 [pCMAX L _ E-UTRA,c (p) ], PEMAX, EN-DC ,PPowerClass, EN-DC}

where

- pCMAX H _ E-UTRA,c (p) is the E-UTRA higher limit of the maximum configured power expressed in linear scale;

- pCMAX L,f,c,NR (q) is the NR higher limit of the maximum configured power expressed in linear scale;

- pCMAX L _ E-UTRA,c (p) is the E-UTRA lower limit of the maximum configured power expressed in linear scale;

- pCMAX L,f,c,NR (q) is the NR lower limit of the maximum configured power expressed in linear scale;

- PPowerClass, EN-DC is defined in clause 6.2B.1.3-1 for inter-band EN-DC; if the UE indicates higherPowerLimitMRDC-r17, PPowerClass,EN-DC is replaced by the sum of the linear powers of PPowerClass,NR and PPowerClass,E-UTRA converted to dB;

- X_scale is the linear value of X dB which is configured by RRC and can only take values [0 , 6]

- pCMAX_ E-UTRA,c (p) is the linear value of PCMAX_ E-UTRA,c (p), the configured max power for E-UTRA. If more than one E-UTRA uplink serving cell is configured as intra-band UL CA in the E-UTRA CG, PCMAX_ E-UTRA,c (p) will be replaced by PCMAX(p) which is the configured maximum power for the entire E-UTRA CG.

- pCMAX,f,c,NR (q) is the linear value of PCMAX,f,c,NR (q), the configured max power of NR, If more than one NR uplink serving cell is configured as intra-band UL CA in the NR CG,  PCMAX_ NR,c (q) will be replaced by PCMAX(q) which is the configured maximum power for the entire NR CG.

Table 6.2B.4.1.3-2: PCMAX tolerance for Dual Connectivity E-UTRA-NR

| PCMAX(dBm) | ToleranceTLOW (PCMAX_L) (dB) | ToleranceTHIGH (PCMAX_H) (dB) |
| --- | --- | --- |
| 23 ≤ PCMAX ≤ 33 | 3.0 | 2.0 |
| 22 ≤ PCMAX < 23 | 5.0 | 2.0 |
| 21 ≤ PCMAX< 22 | 5.0 | 3.0 |
| 20 ≤ PCMAX < 21 | 6.0 | 4.0 |
| 16 ≤ PCMAX < 20 | 5.0 |  |
| 11 ≤ PCMAX < 16 | 6.0 |  |
| -40 ≤ PCMAX < 11 | 7.0 |  |
| NOTE 1: For UEs not indicating support of dynamic power sharing, the upper tolerance Thigh shall be reduced by 0.3 dB for P ≥ 20 dBm. |  |  |

When E-UTRA and NR transmissions overlap and the condition (If (a=TRUE) AND (b=FALSE)) is met, SCG shall be transmitted and the following supplementary minimum requirement apply for the measured SCG power, PUMAX,f,c,NR (q), under nominal conditions.

10log(pCMAX L,f,c,NR (q)/X_scale)  –  TLOW (10log(pCMAX L,f,c,NR (q)/X_scale) )}  ≤  PUMAX,f,c,NR (q) ≤  10log(pCMAX H, f,c,NR (q)) + THIGH (10log(pCMAX H, f,c,NR (q))).

with the tolerances TLOW and THIGH for applicable values of PCMAX specified in Table 6.2B.4.1.3-2.

##### 6.2B.4.1.3a Inter-band NE-DC within FR1

For inter-band dual connectivity with one uplink serving cell per CG on E-UTRA and NR respectively, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of CG i, i = 1,2, and its total configured maximum transmission  power for NE-DC operation, $ P_{Total}^{NE-DC}$= 10log10($\hat  {P}_{total}^{NE-DC}$) with $\hat  {P}_{total}^{NE-DC}$ as specified in clause 7.6.1A of TS 38.213 [10].

The configured maximum output power PCMAX_ E-UTRA,c (p) in sub-frame p for the configured E-UTRA uplink carrier shall be set within the bounds:

PCMAX_L_ E-UTRA,c (p) ≤  PCMAX_ E-UTRA,c (p) ≤  PCMAX H _ E-UTRA,c (p)

where PCMAX_L_ E-UTRA,c and PCMAX H _ E-UTRA,c are the limits for a serving cell c as specified in TS 36.101 [4] clause 6.2.5 modified by PLTE as follows:

PCMAX_L_ E-UTRA,c = MIN { PEMAX, NE-DC , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), MIN(PEMAX,c , PLTE) – tC_ E-UTRA, c,  (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA) – MAX(MPRc + A-MPRc + ΔTIB,c  + TC_ E-UTRA, c + TProSe, P-MPRc)}

PCMAX H _ E-UTRA,c = MIN {PEMAX,c,  PEMAX, NE-DC  , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), PLTE, PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA}

with exception that

- if no symbol of slot  of the NR that is indicated as uplink or flexible by TDD-UL-DL-ConfigurationCommon or TDD-UL-DL-ConfigDedicated overlaps with subframe  of the E-UTRA; or

- if NR slot(s) that is indicated as downlink by TDD-UL-DL-ConfigurationCommon or TDD-UL-DL-ConfigDedicated does not overlap with subframe  of the E-UTRA; then

PCMAX_L_ E-UTRA,c = MIN { PEMAX, NE-DC , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), PEMAX,c  – tC_ E-UTRA, c,  (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA) – MAX(MPRc + A-MPRc + ΔTIB,c  + TC_ E-UTRA, c + TProSe, P-MPRc)}

PCMAX H _ E-UTRA,c = MIN {PEMAX,c,  PEMAX, NE-DC  , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA}

The configured maximum output power PCMAX,f,c,NR (q) in physical-channel q for the configured NR carrier shall be set within the bounds:

PCMAX_L,f,c,NR (q) ≤  PCMAX,f,c,NR (q) ≤  PCMAX_H,f,c,NR (q)

where PCMAX_L,f,c,NR and PCMAX_H,f,c,NR are the limits for a serving cell c as specified in clause 6.2.4 of TS 38.101-1 [2] modified by PNR as follows:

PCMAX_L,f,c,NR = MIN { PEMAX, NE-DC  , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), MIN(PEMAX,c , PNR ) - TC_NR, c,  (PPowerClass,NR – ΔPPowerClass,NR) – MAX(MPRc + A-MPRc+ ΔTIB,c + TC_NR, c + ∆TRxSRS,  P-MPRc) }

PCMAX_H,f,c,NR = MIN {PEMAX,c, PEMAX, NE-DC  , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), PNR , PPowerClass,NR – ΔPPowerClass,NR }

- PEMAX,NE-DC signalled by RRC as p-UE-FR1 in TS 38.331 [9];

- PLTE signalled by RRC as p-MaxEUTRA in TS 36.331 [8];

- PNR signalled by RRC as p-NR-FR1 defined in TS 38.331 [9];

- ΔTc_E-UTRA, c = 1.5dB when NOTE 2 in Table 6.2.2-1 in TS 36.101 [4] applies for a serving cell c, otherwise TC_ E-UTRA,c = 0dB;

- TC_NR,c = 1.5dB when NOTE 3 in Table 6.2.1-1 in TS 38.101-1 [2] applies for a serving cell c, otherwise TC_NR,c = 0dB;

- ΔTIB,c specified in clause  6.2B.4.2.3 for NE-DC, the individual Power Class defined in table 6.2B.1.3a and any other additional power reductions parameters specified in clauses  6.2B.2.3a for NE-DC are applicable to PCMAX_ E-UTRA,c and PCMAX,f,c,NR evaluations.

- PPowerClass, NE-DC is defined in clause 6.2B.1.3a for inter-band NE-DC;

- PPowerClass,NR is the nominal UE power of the power class that the UE supports for the NR band of the NE-DC combination as defined in clause 6.2.1 of 38.101-1 [2]; in case powerClassNRPart as defined in TS 38.331 [9] is indicated, PPowerClass,NR should use that value instead.

- PPowerClass,E-UTRA is the nominal UE power of the power class that the UE supports for the E-UTRA band of the NE-DC combination as defined in clause 6.2.2 of 36.101 [4];

- ΔPPowerClass,NE-DC = 3 dB for a power class 2 capable NE-DC UE when requirements of default power class had been applied as specified in sub-clause 6.2B.1; otherwise ΔPPowerClass,NE-DC = 0 dB;

If the transmissions from NR and E-UTRA do not overlap, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications apply with the modifications specified above. The lower value between PPowerClass, NE-DC or PEMAX, NE-DC shall not be exceeded at any time by UE.

$ P_{Total}^{NE-DC}$ = 10log10($\hat  {P}_{total}^{NE-DC}$) with $ P_{Total}^{NE-DC}$ the configured maximum transmission power for NE-DC operation as specified in clause 7.6 of TS 38.213 [10].

The total configured maximum transmission power for both synchronous and non-synchronous operation is

$ P_{Total}^{NE-DC}$= MIN { PEMAX, NE-DC ,PPowerClass, NE-DC – ΔPPowerClass, NE-DC }

If the UE does not support dynamic power sharing,

$ P_{Total}^{NE-DC}$= MIN { PEMAX, NE-DC ,PPowerClass, NE-DC  – ΔPPowerClass, NE-DC } + 0.3 dB

If the NE-DC UE does not support dynamic power sharing, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications TS 36.101 [4] and TS 38.101-1 [2] respectively apply with the modifications specified above and $ P_{Total}^{NE-DC}$ applies.

When a UE supporting dynamic  sharing is configured for overlapping E-UTRA uplink and NR uplink transmissions, the UE can set its configured maximum output power PCMAX_ E-UTRA,c and PCMAX,f,c,NR for the configured E-UTRA and NR uplink carriers, respectively, and its configured maximum transmission power for NE-DC operation, $\hat  {P}_{Total}^{NE-DC}$, as specified above.

The measured total maximum output power PUMAX over both CGs/RATs, measured over the transmission reference time duration is

PUMAX = 10 log10 [pUMAX,c,E-UTRA + pUMAX,c,NR],

where pUMAX,c,E-UTRA and pUMAX,c,NR denotes the measured output power of serving cell c for E-UTRA and NR respectively, expressed in linear scale.

The measured total configured maximum output power PUMAX shall be within the following bounds:

PCMAX_L -TLOW (PCMAX_L)  ≤  PUMAX  ≤  PCMAX_H + THIGH (PCMAX_H)

with the tolerances TLOW(PCMAX_L) and THIGH(PCMAX_H) for applicable values of PCMAX specified in Table 6.2B.4.1.3a-2.

When an UL subframe transmission p from E-UTRA overlap with a physical-channel q from the NR, then for PUMAX evaluation, the E-UTRA subframe p is taken as reference period TREF and always considered as the reference measurement duration and the following rules are applicable.

TREF and Teval are specified in Table 6.2B.4.1.3a-1 when same or different subframe and physical-channel durations are used in aggregated carriers. PPowerClass ,NE-DC shall not be exceeded by the UE during any evaluation period of time.

Table 6.2B.4.1.3a-1: PCMAX evaluation window

| transmission duration | TREF | Teval |
| --- | --- | --- |
| Different transmission duration in different RAT carriers | LTE Subframe | Min(Tno_hopping, Physical Channel Length) |

For each TREF, the PCMAX_H is evaluated per Teval and given by the maximum value over the transmission(s) within the Teval as follows:

PCMAX_H  = MAX { PCMAX_ NE-DC _H (p,q) , PCMAX_ NE-DC _H (p,q+1), … , PCMAX_ NE-DC _H (p,q+n) }

where PCMAX_ NE-DC _H are the applicable upper limits for each overlapping scheduling unit pairs (p,q) , (p, q+1) , up to (p, q+n) for each applicable Teval duration, where q+n is the last NR UL physical-channel overlapping with LTE subframe p.

While PCMAX_L is computed as follows:

PCMAX_L = MIN { PCMAX_ NE-DC _L (p,q) , PCMAX_ NE-DC _L (p,q+1), … , PCMAX_ NE-DC _L (p,q+n)}

where PCMAX_NE-DC_L are the applicable lower limits for each overlapping scheduling unit pairs (p,q) , (p, q+1) , up to (p, q+n) for each applicable Teval duration, where q+n is the last NR UL physical-channel overlapping with LTE subframe p,

With

PCMAX_ NE-DC _H(p,q) = MIN {10 log10 [pCMAX H _ E-UTRA,c (p) + pCMAX H,f,c,NR (q)], PEMAX, NE-DC ,PPowerClass, NE-DC}

And:

a = 10 log10 [pCMAX_ E-UTRA,c (p) +pCMAX,f,c,NR (q) ] > $ P_{Total}^{NE-DC}$

If a = TRUE

PCMAX_ NE-DC _L(p,q) = MIN {10 log10 [pCMAX L _ E-UTRA,c (p) ], PEMAX, NE-DC ,PPowerClass, NE-DC}

Else

PCMAX_ NE-DC _L(p,q) = MIN {10 log10 [pCMAX L _ E-UTRA,c (p) + pCMAX L,f,c,NR (q)], PEMAX, NE-DC ,PPowerClass, NE-DC}

where

- pCMAX H _ E-UTRA,c (p) is the E-UTRA higher limit of the maximum configured power expressed in linear scale;

- pCMAX H,f,c,NR (q) is the NR higher limit of the maximum configured power expressed in linear scale;

- pCMAX L _ E-UTRA,c (p) is the E-UTRA lower limit of the maximum configured power expressed in linear scale;

- pCMAX L,f,c,NR (q) is the NR lower limit of the maximum configured power expressed in linear scale;

- PPowerClass, NE-DC is defined in clause 6.2B.1.3a for inter-band NE-DC;

- pCMAX_ E-UTRA,c (p) is the linear value of PCMAX_ E-UTRA,c (p), the real configured max power for E-UTRA

- pCMAX,f,c,NR (q) is the linear value of PCMAX,f,c,NR (q), the real configured max power of NR

Table 6.2B.4.1.3a-2: PCMAX tolerance for Dual Connectivity E-UTRA-NR

| PCMAX(dBm) | ToleranceTLOW (PCMAX_L) (dB) | ToleranceTHIGH (PCMAX_H) (dB) |
| --- | --- | --- |
| 23 ≤ PCMAX ≤ 33 | 3.0 | 2.0 |
| 22 ≤ PCMAX < 23 | 5.0 | 2.0 |
| 21 ≤ PCMAX< 22 | 5.0 | 3.0 |
| 20 ≤ PCMAX < 21 | 6.0 | 4.0 |
| 16 ≤ PCMAX < 20 | 5.0 |  |
| 11 ≤ PCMAX < 16 | 6.0 |  |
| -40 ≤ PCMAX < 11 | 7.0 |  |
| NOTE 1: For UEs not indicating support of dynamic power sharing, the upper tolerance Thigh shall be reduced by 0.3 dB for P ≥ 20 dBm. |  |  |

When E-UTRA and NR transmissions overlap and the condition a = TRUE, PUMAX,f,c,NR (q) for MCG, under nominal conditions, shall meet

PUMAX,f,c,NR (q) ≤  10log(pCMAX H, f,c,,NR c (q)) + THIGH (10log(pCMAX H, f,c,,NR c (q))).

with the tolerances TLOW and THIGH for applicable values of PCMAX specified in Table 6.2B.4a.1.3-2.

When LTE and NR transmissions overlap and the condition a = FALSE), then PUMAX, under nominal conditions, shall be within the following bounds:

PCMAX_L -TLOW (PCMAX_L)  ≤  PUMAX  ≤  PCMAX_H + THIGH (PCMAX_H)

where PCMAX_L, PCMAX_H, and PUMAX are specified above with the tolerances TLOW and THIGH specified in Table 6.2B.4a.1.3-2 for applicable values of PCMAX_L and PCMAX_H.

##### 6.2B.4.1.4 Inter-band EN-DC including FR2

For inter-band dual connectivity with one uplink serving cell per CG on E-UTRA and NR respectively, with NR configured in FR2, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of CG i, i = 1,2.

The UE maximum configured power PCMAX,c(i), on E-UTRA for the subframe i shall be set according to clause 6.2.5 from TS 36.101 [4]. Applicable inter-band ΔTIB,c parameters shall be used according to the clauses 6.2B.4.2.4 or 6.2B.4.2.5.

The UE maximum configured power PCMAX,c(j), on NR for the slot j shall be set according to subclase 6.2.4 from TS 38.101-2 [3].

For the configured power measurements TS 36.101 [4] clause 6.2.5 and TS 38.101-2 [3] clause 6.2.4 are applicable.

##### 6.2B.4.1.4a (Void)

##### 6.2B.4.1.5 Inter-band EN-DC including both FR1 and FR2

For inter-band dual connectivity with one uplink serving cell per CG on E-UTRA and NR respectively, with both CGs configured in FR1, the requirements specified in clause 6.2B.4.1.3 apply.

For inter-band dual connectivity with one uplink serving cell per CG on E-UTRA and NR respectively, with NR configured in FR2, the requirements specified in clause 6.2B.4.1.4 apply.

For inter-band dual connectivity with one uplink serving cell in first CG on E-UTRA and two uplink serving cells in second CG on NR FR1 and NR FR2 respectively, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) , i = 1,2,3 with i=1 for E-UTRA, i=2 for NR FR1 and i=3 for NR FR2.

– For serving cell on FR2, the requirements specified in clause 6.2.4 in TS 38.101-2 [3] apply to the UE maximum configured power PCMAX,c(3),3 and the measured maximum configured power.

– For remaining inter-band dual connectivity involving CG1 and CG2, the requirements specified in clause 6.2B.4.1.3 apply.

#### 6.2B.4.2 ΔTIB,c for DC

##### 6.2B.4.2.0 General

For the UE which supports inter-band EN-DC or NE-DC configuration, ΔTIB,c in Tables below applies where unless otherwise stated, the same ΔTIB,c is applicable to NR band(s) part for DC configurations which have the same NR operating band combination. Unless otherwise stated, ΔTIB,c is set to zero.

Unless ΔTIB,c  is specified for the NE-DC configuration, the specified ΔTIB,c  for the EN-DC configuration including same bands as the corresponding NE-DC configuration is applicable for the NE-DC configuration.

##### 6.2B.4.2.1 Intra-band contiguous EN-DC

ΔTIB,c is not applicable for intra-band contiguous EN-DC.

##### 6.2B.4.2.1a (Void)

##### 6.2B.4.2.2 Intra-band non-contiguous EN-DC

ΔTIB,c is not applicable for intra-band non-contiguous EN-DC.

##### 6.2B.4.2.3 Inter-band EN-DC within FR1

###### 6.2B.4.2.3.1 ΔTIB,c for EN-DC two bands

Table 6.2B.4.2.3.1-1: ΔTIB,c due to EN-DC(two bands)

| Inter-band EN-DC configuration | ΔTIB,c for E-UTRA band / NR band (dB)7 |  |  |
| --- | --- | --- | --- |
|  | Component band in order of bands in configuration8 |  |  |
| DC_1_n3 | 0.3 | 0.3 |  |
| DC_1_n5 | 0.3 | 0.3 |  |
| DC_1_n7DC_1-1_n7 | 0.5 | 0.6 |  |
| DC_1_n8 | 0.3 | 0.3 |  |
| DC_1_n20 | 0.3 | 0.3 |  |
| DC_1_n26 | 0.3 | 0.3 |  |
| DC_1_n28 | 0.3 | 0.6 |  |
| DC_1_n38 | 0.5 | 0.5 |  |
| DC_1_n40 | 0.5 | 0.5 |  |
| DC_1_n41 | 0.5 | 0.5 |  |
| DC_1_n50 | 0.5 | 0.5 |  |
| DC_1_n51 | 0.6 | 0.6 |  |
| DC_1_n71 | 0.3 | 0.3 |  |
| DC_1_n77 | 0.6 | 0.8 |  |
| DC_1_n78 | 0.3 | 0.8 |  |
| DC_1_n105 | 0.3 | 0.6 |  |
| DC_2_n5DC_2-2_n5 | 0.3 | 0.3 |  |
| DC_2_n7DC_2-2_n7 | 0.5 | 0.5 |  |
| DC_2_n12 | 0.3 | 0.3 |  |
| DC_2_n14 | 0.3 | 0.3 |  |
| DC_2_n28 | 0.3 | 0.3 |  |
| DC_2_n30 DC_2-2_n30 | 0.5 | 0.3 |  |
| DC_2_n38DC_2-2_n38 | 0.5 | 0.9 |  |
| DC_2_n41DC_2-2_n41 | 0.5 | 0.41 / 0.92 |  |
| DC_2_n48 | 0.6 | 0.8 |  |
| DC_2_n66DC_2-2_n66 | 0.5 | 0.5 |  |
| DC_2_n71DC_2-2_n71 | 0.3 | 0.3 |  |
| DC_2_n77DC_2-2_n77 | 0.6 | 0.8 |  |
| DC_2_n78DC_2-2_n78 | 0.6 | 0.8 |  |
| DC_3_n1 | 0.3 | 0.3 |  |
| DC_3_n5 | 0.3 | 0.3 |  |
| DC_3_n8DC_3-3_n8 | 0.3 | 0.3 |  |
| DC_3_n7DC_3-3_n7 | 0.5 | 0.5 |  |
| DC_3_n105 | 0.3 | 0.6 |  |
| DC_3_n20DC_3-3_n20 | 0.3 | 0.3 |  |
| DC_3_n26 | 0.3 | 0.3 |  |
| DC_3_n28 | 0.3 | 0.3 |  |
| DC_3_n34 | 0.5 | 0.5 |  |
| DC_3_n38 | 0.5 | 0.5 |  |
| DC_3_n40 | 0.5 | 0.5 |  |
| DC_3-n41DC_3-3_n41 | 0.5 | 0.33 / 0.84 |  |
| DC_3_n50 | 0.5 | 0.5 |  |
| DC_3_n51 | 0.3 | 0.3 |  |
| DC_3_n71 | 0.3 | 0.3 |  |
| DC_3_n77DC_3-3_n77 | 0.6 | 0.8 |  |
| DC_3_n78DC_3-3_n78 | 0.6 | 0.8 |  |
| DC_4_n2 | 0.5 | 0.5 |  |
| DC_4_n5 | 0.3 | 0.3 |  |
| DC_4_n7 | 0.5 | 0.5 |  |
| DC_4_n28 | 0.3 | 0.6 |  |
| DC_4_n38 | 0.5 | 0.8 |  |
| DC_4_n41 | 0.5 | 0.81 / 1.32 |  |
| DC_4_n78 | 0.6 | 0.8 |  |
| DC_5_n1 | 0.3 | 0.3 |  |
| DC_5_n2DC_5-5_n2 | 0.3 | 0.3 |  |
| DC_5_n3 | 0.3 | 0.3 |  |
| DC_5_n7 | 0.3 | 0.3 |  |
| DC_5_n12 | 0.8 | 0.4 |  |
| DC_5_n25 | 0.3 | 0.3 |  |
| DC_5_n28 | 0.5 | 0.5 |  |
| DC_5_n30 | 0.3 | 0.3 |  |
| DC_5_n38 | 0.3 | 0.3 |  |
| DC_5_n40 | 0.3 | 0.3 |  |
| DC_5_n41 | 0.6 | 0.3 |  |
| DC_5_n48 | 0.3 | 0.3 |  |
| DC_5_n66DC_5-5_n66 | 0.3 | 0.3 |  |
| DC_5_n71 | 0.5 | 0.5 |  |
| DC_5_n77 | 0.6 | 0.8 |  |
| DC_5_n78 | 0.6 | 0.8 |  |
| DC_7_n1DC_7-7_n1 | 0.6 | 0.5 |  |
| DC_7_n2 | 0.5 | 0.5 |  |
| DC_7_n3DC_7-7_n3 | 0.5 | 0.5 |  |
| DC_7_n5DC_7-7_n5 | 0.3 | 0.3 |  |
| DC_7_n8DC_7-7_n8 | 0.3 | 0.6 |  |
| DC_7_n12 | 0.3 | 0.3 |  |
| DC_7_n20 | 0.3 | 0.3 |  |
| DC_7_n25 | 0.5 | 0.5 |  |
| DC_7_n26 | 0.3 | 0.3 |  |
| DC_7_n28, DC_7-7_n28 | 0.3 | 0.3 |  |
| DC_7_n40 DC_7-7_n40 | 0.5 | 0.6 |  |
| DC_7_n51 | 0.3 | 0.3 |  |
| DC_7_n71 | 0.3 | 0.6 |  |
| DC_7_n66DC_7-7_n66 | 0.5 | 0.5 |  |
| DC_7_n77DC_7-7_n77 | 0.5 | 0.8 |  |
| DC_7_n78DC_7-7_n78 | 0.5 | 0.8 |  |
| DC_7_n79DC_7-7_n79 | 0.5 | 0.8 |  |
| DC_7_n105 | 0.3 | 0.6 |  |
| DC_8_n1 | 0.3 | 0.3 |  |
| DC_8_n2 | 0.3 | 0.3 |  |
| DC_8_n3 | 0.3 | 0.3 |  |
| DC_8_n7 | 0.6 | 0.3 |  |
| DC_8_n20 | 0.4 | 0.4 |  |
| DC_8_n28 | 0.6 | 0.5 |  |
| DC_8_n34 | 0.3 | 0.3 |  |
| DC_8_n38 | 0.6 | 0.3 |  |
| DC_8_n39 | 0.3 | 0.3 |  |
| DC_8_n40 | 0.3 | 0.3 |  |
| DC_8_n41 | 0.3 | 0.3 |  |
| DC_8_n71 | 0.5 | 0.5 |  |
| DC_8_n77 | 0.6 | 0.8 |  |
| DC_8_n78 | 0.6 | 0.8 |  |
| DC_11_n1 | 0.3 | 0.3 |  |
| DC_11_n3 | 0.8 | 0.9 |  |
| DC_11_n28 | 0.4 | 0.6 |  |
| DC_11_n41 | 0.3 | 0.3 |  |
| DC_11_n77 | 0.4 | 0.8 |  |
| DC_11_n78 | 0.4 | 0.8 |  |
| DC_12_n2 | 0.3 | 0.3 |  |
| DC_12_n5 | 0.4 | 0.8 |  |
| DC_12_n7 | 0.3 | 0.3 |  |
| DC_12_n25 | 0.3 | 0.3 |  |
| DC_12_n30 | 0.3 | 0.3 |  |
| DC_12_n38 | 0.3 | 0.3 |  |
| DC_12_n41 | 0.3 | 0.3 |  |
| DC_12_n66 | 0.8 | 0.3 |  |
| DC_12_n71 | 1 | 1 |  |
| DC_12_n77 | 0.5 | 0.8 |  |
| DC_12_n78 | 0.5 | 0.8 |  |
| DC_13_n2 | 0.3 | 0.3 |  |
| DC_13_n5 | 0.5 | 0.5 |  |
| DC_13_n7 | 0.5 | 0.5 |  |
| DC_13_n25 | 0.3 | 0.3 |  |
| DC_13_n48 | 0.3 | 0.3 |  |
| DC_13_n66 | 0.3 | 0.3 |  |
| DC_13_n71 | 0.5 | 0.5 |  |
| DC_13_n77 | 0.5 | 0.8 |  |
| DC_13_n78 | 0.5 | 0.8 |  |
| DC_14_n2 | 0.3 | 0.3 |  |
| DC_14_n5 | 0.5 | 0.5 |  |
| DC_14_n30 | 0.3 | 0.3 |  |
| DC_14_n41 | 0.3 | 0.3 |  |
| DC_14_n66 | 0.3 | 0.3 |  |
| DC_14_n77 | 0.5 | 0.8 |  |
| DC_18_n3 | 0.3 | 0.3 |  |
| DC_18_n28 | 0.5 | 0.5 |  |
| DC_18_n41 | 0.3 | 0.33 |  |
| DC_18_n77 | 0.3 | 0.8 |  |
| DC_18_n78 | 0.3 | 0.8 |  |
| DC_19_n1 | 0.3 | 0.3 |  |
| DC_19_n77 | 0.3 | 0.8 |  |
| DC_19_n78 | 0.3 | 0.8 |  |
| DC_20_n1 | 0.3 | 0.3 |  |
| DC_20_n3 | 0.3 | 0.3 |  |
| DC_20_n7 | 0.3 | 0.3 |  |
| DC_20_n8 | 0.4 | 0.4 |  |
| DC_20_n28 | 0.5 | 0.5 |  |
| DC_20_n38 | 0.5 | 0.3 |  |
| DC_20_n40 | 0.3 | 0.3 |  |
| DC_20_n41 | 0.3 | 0.3 |  |
| DC_20_n50 | 0.3 | 0.4 |  |
| DC_20_n51 | 0.5 | 0.5 |  |
| DC_20_n77 | 0.6 | 0.8 |  |
| DC_20_n78 | 0.6 | 0.8 |  |
| DC_21_n1 | 0.3 | 0.3 |  |
| DC_21_n28 | 0.4 | 0.3 |  |
| DC_21_n77 | 0.4 | 0.8 |  |
| DC_21_n78 | 0.4 | 0.8 |  |
| DC_25_n41,DC_25-25_n41 | 0.5 | 0.41 / 0.92 |  |
| DC_25_n77DC_25-25_n77 | 0.6 | 0.8 |  |
| DC_25_n78DC_25-25_n78 | 0.6 | 0.8 |  |
| DC_26_n25 | 0.3 | 0.3 |  |
| DC_26_n41 | 0.3 | 0.3 |  |
| DC_26_n77 | 0.3 | 0.8 |  |
| DC_26_n78 | 0.3 | 0.8 |  |
| DC_28_n1 | 0.6 | 0.3 |  |
| DC_28_n2 | 0.3 | 0.3 |  |
| DC_28_n3 | 0.3 | 0.3 |  |
| DC_28_n5 | 0.5 | 0.5 |  |
| DC_28_n7 | 0.3 | 0.3 |  |
| DC_28_n8 | 0.5 | 0.6 |  |
| DC_28_n20 | 0.5 | 0.5 |  |
| DC_28_n38 | 0.3 | 0.3 |  |
| DC_28_n40 | 0.3 | 0.3 |  |
| DC_28_n41 | 0.3 | 0.3 |  |
| DC_28_n50 | 0.3 | 0.4 |  |
| DC_28_n51 | 0.5 | 0.5 |  |
| DC_28_n66 | 0.6 | 0.3 |  |
| DC_28_n71 | 1.1 | 1.1 |  |
| DC_28_n77 | 0.5 | 0.8 |  |
| DC_28_n78 | 0.5 | 0.8 |  |
| DC_28_n105 | 1.0 | 1.0 |  |
| DC_30_n2 | 0.3 | 0.5 |  |
| DC_30_n5 | 0.3 | 0.3 |  |
| DC_30_n12 | 0.3 | 0.3 |  |
| DC_30_n14 | 0.3 | 0.3 |  |
| DC_30_n66 | 0.5 | 0.8 |  |
| DC_30_n77 | 0.5 | 0.8 |  |
| DC_38_n1 | 0.5 | 0.5 |  |
| DC_38_n3 | 0.5 | 0.5 |  |
| DC_38_n8 | 0.6 | 0.3 |  |
| DC_38_n28 | 0.3 | 0.3 |  |
| DC_38_n78 | - | 0.5 |  |
| DC_38_n79 | 0.3 | 0.8 |  |
| DC_39-n41 | 0.5 | 0.5 |  |
| DC_39_n78 | 0.3 | 0.8 |  |
| DC_39_n79 | 0.3 | 0.8 |  |
| DC_40_n1 | 0.5 | 0.5 |  |
| DC_40_n3 | 0.5 | 0.5 |  |
| DC_40_n7 | 0.6 | 0.5 |  |
| DC_40_n28 | 0.3 | 0.3 |  |
| DC_40_n41 | 0.5 | 0.5 |  |
| DC_40_n77 | - | 0.5 |  |
| DC_40_n78 | - | 0.56 |  |
| DC_40_n79 | 0.3 | 0.8 |  |
| DC_41_n1 | 0.5 | 0.5 |  |
| DC_41_n3 | 0.33 / 0.84 | 0.5 |  |
| DC_41_n28 | 0.3 | 0.3 |  |
| DC_41_n77 | 0.3 | 0.8 |  |
| DC_41_n78 | 0.3 | 0.8 |  |
| DC_41_n79 | 0.3 | 0.8 |  |
| DC_42_n1 | 0.8 | 0.3 |  |
| DC_42_n3 | 0.8 | 0.6 |  |
| DC_42_n28 | 0.5 | 0.8 |  |
| DC_42_n51 | 0.6 | 0.8 |  |
| DC_48_n2 | 0.8 | 0.6 |  |
| DC_48_n5 | 0.3 | 0.3 |  |
| DC_48_n12 | 0.3 | 0.3 |  |
| DC_48_n25 | 0.8 | 0.6 |  |
| DC_48_n46 | 0.8 | - |  |
| DC_48_n66 | 0.8 | 0.6 |  |
| DC_48_n71DC_48-48_n71DC_48-48-48_n71 | 0.3 | 0.3 |  |
| DC_66_n2DC_66-66_n2DC_66-66-66_n2 | 0.5 | 0.5 |  |
| DC_66_n5,DC_66-66_n5,DC_66-66-66_n5 | 0.3 | 0.3 |  |
| DC_66_n7DC_66-66_n7 | 0.5 | 0.5 |  |
| DC_66_n12 | 0.8 | 0.3 |  |
| DC_66_n14 | 0.3 | 0.3 |  |
| DC_66_n25 | 0.5 | 0.5 |  |
| DC_66_n28 | 0.3 | 0.6 |  |
| DC_66_n30DC_66-66_n30 | 0.5 | 0.8 |  |
| DC_66_n38DC_66-66_n38 | 0.5 | 0.5 |  |
| DC_66_n41 | 0.5 | 0.81 / 1.32 |  |
| DC_66_n48DC_66-66_n48 | 0.6 | 0.8 |  |
| DC_66_n71DC_66-66_n71 | 0.3 | 0.3 |  |
| DC_66_n77DC_66-66_n77DC_66-66-66_n77 | 0.6 | 0.8 |  |
| DC_66_n78DC_66-66_n78 | 0.6 | 0.8 |  |
| DC_68_n1 | 0.6 | 0.3 |  |
| DC_68_n3 | 0.3 | 0.3 |  |
| DC_68_n7 | 0.3 | 0.3 |  |
| DC_68_n8 | 0.5 | 0.6 |  |
| DC_68_n20 | 0.5 | 0.5 |  |
| DC_68_n38 | 0.3 | 0.3 |  |
| DC_68_n40 | 0.3 | 0.3 |  |
| DC_68_n41 | 0.3 | 0.3 |  |
| DC_68_n77 | 0.5 | 0.8 |  |
| DC_68_n78 | 0.5 | 0.8 |  |
| DC_71_n2 | 0.3 | 0.3 |  |
| DC_71_n5 | 0.5 | 0.5 |  |
| DC_71_n7 | 0.6 | 0.3 |  |
| DC_71_n12 | 1 | 1 |  |
| DC_71_n25 | 0.3 | 0.3 |  |
| DC_71_n38 | 0.6 | 0.3 |  |
| DC_71_n41 | 0.6 | 0.3 |  |
| DC_71_n48 | 0.3 | 0.3 |  |
| DC_71_n66 | 0.3 | 0.3 |  |
| DC_71_n77 | 0.5 | 0.8 |  |
| DC_71_n78 | 0.5 | 0.8 |  |
| DC_106_n41 | 0.6 | 0.3 |  |
| DC_106_n48 | 0.6 | 0.8 |  |
| NOTE 1: The requirement is applied for UE transmitting on the frequency range of 2545-2690 MHz.NOTE 2: The requirement is applied for UE transmitting on the frequency range of 2496-2545 MHz.NOTE 3: Applicable for the frequency range of 2515 – 2690 MHz.NOTE 4: Applicable for the frequency range of 2496 - 2515 MHz.NOTE 5: Applicable for UE supporting inter-band EN-DC without simultaneous Rx/Tx.NOTE 6: Only applicable for UE supporting inter-band carrier aggregation with uplink in one E-UTRA band and without simultaneous Rx/Tx.NOTE 7: “-” denotes ΔTIB,c = 0.NOTE 8: The component band order in the configuration should be listed by the order of E-UTRA band and NR band respectively. |  |  |  |

###### 6.2B.4.2.3.2 ΔTIB,c for EN-DC three bands

Table 6.2B.4.2.3.2-1: ΔTIB,c due to EN-DC (three bands)

| Inter-band EN-DC configuration | ΔTIB,c for E-UTRA band / NR band (dB)6 |  |  |
| --- | --- | --- | --- |
|  | Component band in order of bands in configuration7 |  |  |
| DC_1_n1-n41 | 0.5 | 0.5 | 0.5 |
| DC_1_n1-n78 | 0.3 | 0.3 | 0.8 |
| DC_1-3_n1DC_1-3-3_n1 | 0.3 | 0.3 | 0.3 |
| DC_1-3_n3 DC_1_(n)3 | 0.3 | 0.3 | 0.3 |
| DC_1-3_n5 | 0.3 | 0.3 | 0.3 |
| DC_1-3_n7 | 0.6 | 0.6 | 0.6 |
| DC_1-3_n8DC_1-3-3_n8 | 0.3 | 0.3 | 0.3 |
| DC_1_n3-n8 | 0.3 | 0.3 | 0.3 |
| DC_1-3_n28 | 0.3 | 0.3 | 0.6 |
| DC_1-3_n26 | 0.3 | 0.3 | 0.3 |
| DC_1_n3-n28 | 0.3 | 0.3 | 0.6 |
| DC_1-3_n38 | 0.5 | 0.5 | 0.5 |
| DC_1-3_n40 | 0.5 | 0.5 | 0.5 |
| DC_1-3_n41DC_1-3-3_n41 | 0.5 | 0.5 | 0.33 / 0.84 |
| DC_1_n3-n41 | 0.5 | 0.5 | 0.33 / 0.84 |
| DC_1-41_n3 | 0.5 | 0.33 / 0.84 | 0.5 |
| DC_1_n3-n75 | 0.5 | 0.5 | N/A |
| DC_1-3_n77 | 0.6 | 0.6 | 0.8 |
| DC_1_n3-n77 | 0.6 | 0.6 | 0.8 |
| DC_1-3_n71 | 0.3 | 0.3 | 0.3 |
| DC_1-3_n78DC_1-3-3_n78DC_1-1-3-3_n78 | 0.6 | 0.6 | 0.8 |
| DC_1-3_n79 | 0.3 | 0.3 | - |
| DC_1_n3-n78 | 0.6 | 0.6 | 0.8 |
| DC_1_n3-n79 | 0.3 | 0.3 | 0.8 |
| DC_1-3_n105 | 0.3 | 0.3 | 0.6 |
| DC_1-5_n3 | 0.3 | 0.3 | 0.3 |
| DC_1-5_n28 | 0.3 | 0.5 | 0.6 |
| DC_1-5_n40 | 0.6 | 0.3 | 0.5 |
| DC_1_n5-n40 | 0.6 | 0.6 | 0.9 |
| DC_1-5_n77 | 0.3 | 0.6 | 0.8 |
| DC_1-5_n78 | 0.3 | 0.6 | 0.8 |
| DC_1-5_n79 | 0.3 | 0.3 | - |
| DC_1-7_n1 | 0.5 | 0.6 | 0.5 |
| DC_1-7_n3 | 0.6 | 0.6 | 0.6 |
| DC_1-7_n5 | 0.5 | 0.6 | 0.3 |
| DC_1-7_n7DC_1-(n)7 | 0.5 | 0.6 | 0.6 |
| DC_1-7_n8DC_1-7-7_n8 | 0.5 | 0.6 | 0.6 |
| DC_1-7_n20 | 0.5 | 0.6 | 0.3 |
| DC_1-7_n26 | 0.5 | 0.6 | 0.3 |
| DC_1-7_n28 | 0.5 | 0.6 | 0.6 |
| DC_1-7_n38 | 0.5 | N/A | N/A |
| DC_1-7_n40DC_1-7-7_n40 | 0.6 | 0.8 | 0.9 |
| DC_1-7_n77 | 0.6 | 0.6 | 0.8 |
| DC_1-7_n78DC_1-7-7_n78 | 0.6 | 0.6 | 0.8 |
| DC_1-7_n105 | 0.5 | 0.6 | 0.6 |
| DC_1_n7-n78 | 0.6 | 0.6 | 0.8 |
| DC_1-8_n1 | 0.3 | 0.3 | 0.3 |
| DC_1-8_n3 | 0.3 | 0.3 | 0.3 |
| DC_1-8_n3DC_1-8_n28 | 0.3 | 0.6 | 0.6 |
| DC_1_n8-n40 | 0.3 | 0.3 | 0.5 |
| DC_1-8_n41 | 0.5 | 0.6 | 0.6 |
| DC_1-8_n71 | 0.3 | 0.6 | 0.6 |
| DC_1-8_n77 | 0.3 | 0.6 | 0.8 |
| DC_1_n8-n77 | 0.3 | 0.6 | 0.8 |
| DC_1-8_n78 | 0.3 | 0.6 | 0.8 |
| DC_1_n8-n78 | 0.3 | 0.6 | 0.8 |
| DC_1-8_n79 | 0.3 | 0.3 | - |
| DC_1-11_n3 | 0.3 | 0.8 | 0.9 |
| DC_1-11_n28 | 0.3 | 0.4 | 0.6 |
| DC_1-11_n41 | 0.5 | 0.3 | 0.5 |
| DC_1-11_n77 | 0.6 | 0.4 | 0.8 |
| DC_1-11_n78 | 0.3 | 0.4 | 0.8 |
| DC_1-11_n79 | 0.3 | 0.3 | - |
| DC_1-18_n3 | 0.3 | 0.3 | 0.3 |
| DC_1-18_n28 | 0.3 | 0.5 | 0.5 |
| DC_1-18_n41 | 0.5 | 0.3 | 0.5 |
| DC_1-18_n77 | 0.3 | 0.3 | 0.8 |
| DC_1-18_n78 | 0.3 | 0.3 | 0.8 |
| DC_1-19_n77 | 0.3 | 0.3 | 0.8 |
| DC_1-19_n78 | 0.3 | 0.3 | 0.8 |
| DC_1-19_n79 | 0.3 | 0.3 | - |
| DC_1-20_n1 | 0.3 | 0.3 | 0.3 |
| DC_1-20_n3 | 0.3 | 0.3 | 0.3 |
| DC_1-20_n7 | 0.5 | 0.3 | 0.6 |
| DC_1-20_n8 | 0.3 | 0.4 | 0.4 |
| DC_1-20_n28 | 0.5 | 0.6 | 0.6 |
| DC_1-20_n38 | 0.5 | 0.3 | 0.5 |
| DC_1-20_n41 | 0.5 | 0.3 | 0.51 / 1.22 |
| DC_1-20_n78DC_1-1-20_n78 | 0.3 | 0.3 | 0.8 |
| DC_1-21_n28 | 0.3 | 0.4 | 0.6 |
| DC_1-21_n77 | 0.3 | 0.3 | 0.8 |
| DC_1-21_n78 | 0.6 | 0.4 | 0.8 |
| DC_1-21_n79 | 0.3 | 0.3 | - |
| DC_1-26_n78DC_1-1-20_n78 | 0.3 | 0.6 | 0.8 |
| DC_1_n26-n78 | 0.3 | 0.6 | 0.8 |
| DC_1-28_n3 | 0.3 | 0.6 | 0.3 |
| DC_1-28_n5 | 0.3 | 0.5 | 0.5 |
| DC_1-28_n7 | 0.5 | 0.6 | 0.6 |
| DC_1-28_n20 | 0.3 | 0.6 | 0.6 |
| DC_1-28_n38 | 0.5 | 0.6 | 0.6 |
| DC_1-28_n71 | 0.3 | 1.1 | 1.1 |
| DC_1-28_n77 | 0.3 | 0.6 | 0.8 |
| DC_1-28_n78 | 0.3 | 0.6 | 0.8 |
| DC_1_n28-n75 | 0.3 | 0.7 | N/A |
| DC_1_n28-n78 | 0.3 | 0.6 | 0.8 |
| DC_1_n28-n79 | 0.3 | 0.6 | - |
| DC_1_n28-n40 | 0.6 | 0.3 | 0.5 |
| DC_1_n28-n77 | 0.6 | 0.6 | 0.8 |
| DC_1-28_n40 | 0.6 | 0.3 | 0.5 |
| DC_1-32_n3 | 0.5 | N/A | 0.5 |
| DC_1-32_n8 | 0.5 | N/A | 0.3 |
| DC_1-32_n28 | 0.3 | N/A | 0.7 |
| DC_1-32_n41 | 0.5 | N/A | 0.6 |
| DC_1-32_n78 | 0.5 | N/A | 0.8 |
| DC_1-38_n3 | 0.5 | 0.5 | 0.5 |
| DC_1-38_n7 | 0.5 | N/A | N/A |
| DC_1-38_n8 | 0.5 | 0.5 | 0.3 |
| DC_1-38_n28 | 0.5 | 0.5 | 0.6 |
| DC_1-(n)38 | 0.5 | 0.5 | 0.5 |
| DC_1-38_n78 | 0.5 | 0.5 | 0.8 |
| DC_1_n38-n78 | 0.5 | 0.5 | 0.8 |
| DC_1A-40A_n28A | 0.5 | 0.6 | 0.6 |
| DC_1_n40-n41 | 0.6 | 0.9 | 0.8 |
| DC_1_n40-n71 | 0.5 | 0.5 | 0.6 |
| DC_1_n40-n77 | 0.3 | 0.5 | 0.8 |
| DC_1-40_n78 | 0.6 | 0.35 | 0.85 |
| DC_1_n40-n78 | 0.3 | 0.5 | 0.8 |
| DC_1_n40-n105 | 0.5 | 0.5 | 0.6 |
| DC_1-41_n1 | 0.5 | 0.5 | 0.5 |
| DC_1-41_n3 | 0.5 | 0.33 / 0.84 | 0.5 |
| DC_1-41_n28 | 0.5 | 0.5 | 0.5 |
| DC_1-(n)41 | 0.5 | 0.5 | 0.5 |
| DC_1-41_n41 | 0.5 | 0.5 | 0.5 |
| DC_1-41_n77 | 0.5 | 0.5 | 0.8 |
| DC_1_n41-n77 | 0.5 | 0.5 | 0.8 |
| DC_1-41_n78 | 0.5 | 0.5 | 0.8 |
| DC_1_n41-n78 | 0.5 | 0.5 | 0.8 |
| DC_1-41_n79 | 0.5 | 0.5 | - |
| DC_1-42_n3 | 0.3 | 0.8 | 0.6 |
| DC_1-42_n28 | 0.3 | 0.8 | 0.8 |
| DC_1-42_n77 | 0.6 | N/A | 0.8 |
| DC_1-42_n78 | 0.3 | N/A | 0.8 |
| DC_1-42_n79 | 0.3 | N/A | - |
| DC_1_n71-n77 | 0.6 | 0.6 | 0.8 |
| DC_1_n75-n78 | 0.5 | N/A | 0.8 |
| DC_1_n77-n79 | 0.6 | 0.8 | - |
| DC_1_SUL_n77-n80 | 0.6 | 0.8 | 0.6 |
| DC_1_SUL_n77-n84 | 0.6 | 0.8 | 0.6 |
| DC_1_SUL_n78-n84 | 0.3 | 0.8 | 0.3 |
| DC_1_n78-n79 | 0.3 | 0.8 | 0.5 |
| DC_1_SUL_n78-n80 | 0.6 | 0.8 | 0.6 |
| DC_1_n78-n105 | 0.3 | 0.8 | 0.6 |
| DC_2_n2-n7 | 0.5 | 0.5 | 0.5 |
| DC_2_n2-n38 | 0.5 | 0.5 | 0.9 |
| DC_2_n2-n41 | 0.5 | 0.5 | 0.5 |
| DC_2_n2-n66 | 0.5 | 0.5 | 0.5 |
| DC_2_n2-n71 | 0.3 | 0.3 | 0.3 |
| DC_2_n2-n77 | 0.6 | 0.6 | 0.8 |
| DC_2_n2-n78 | 0.6 | 0.6 | 0.8 |
| DC_2-4_n28 | 0.5 | 0.5 | 0.8 |
| DC_2-4_n38 | 0.5 | 0.5 | 0.5 |
| DC_2-4_n41 | 0.5 | 0.5 | 0.5 |
| DC_2-4_n78 | 0.6 | 0.6 | 0.8 |
| DC_2-5_n2DC_2-5-5_n2 | 0.3 | 0.3 | 0.3 |
| DC_2-5_n5DC_2-2-5_n5 DC_2-(n)5DC_2-2-(n)5 | 0.3 | 0.3 | 0.3 |
| DC_2-5_n7DC_2-2-5_n7 | 0.5 | 0.3 | 0.5 |
| DC_2_n5-n7 | 0.5 | 0.6 | 0.4 |
| DC_2-5_n12 | 0.3 | 0.8 | 0.4 |
| DC_2-5_n30DC_2-2-5_n30 | 0.5 | 0.3 | 0.3 |
| DC_2-5_n41 | 0.5 | 0.6 | 0.41 / 0.92 |
| DC_2-5_n48 | 0.6 | 0.3 | 0.8 |
| DC_2-5_n66DC_2-5-5_n66 | 0.5 | 0.3 | 0.5 |
| DC_2-5_n71 | 0.3 | 0.5 | 0.5 |
| DC_2-5_n77 DC_2-2-5_n77 | 0.6 | 0.6 | 0.8 |
| DC_2-5_n78DC_2-2-5_n78 | 0.6 | 0.6 | 0.8 |
| DC_2-7_n5DC_2-7-7_n5 | 0.3 | 0.3 | 0.3 |
| DC_2-7_n7 | 0.5 | 0.5 | 0.5 |
| DC_2-7_n12DC_2-2-7_n12 | 0.5 | 0.5 | 0.3 |
| DC_2_n7-n12 | 0.5 | 0.5 | 0.3 |
| DC_2-7_n25DC_2-7-7_n25 | 0.5 | 0.5 | 0.5 |
| DC_2-7_n28 | 0.5 | 0.5 | 0.3 |
| DC_2_n5-n77 | 0.6 | 0.3 | 0.8 |
| DC_2-7_n38DC_2-2-7_n38 | 0.5 | N/A | N/A |
| DC_2-7_n71 | 0.5 | 0.5 | 0.6 |
| DC_2_n7-n71 | 0.5 | 0.5 | 0.3 |
| DC_2-7_n66DC_2-7-7_n66DC_2_n7-n66 | 0.5 | 0.5 | 0.5 |
| DC_2-7_n77DC_2-2-7_n77DC_2-7-7_n77 | 0.6 | 0.5 | 0.8 |
| DC_2_n7-n77 | 0.6 | 0.5 | 0.8 |
| DC_2-7_n78DC_2-2-7_n78 | 0.5 | 0.5 | - |
| DC_2_n7-n78 | 0.6 | 0.5 | 0.8 |
| DC_2-8_n2 | 0.3 | 0.3 | 0.3 |
| DC_2-12_n2 | 0.3 | 0.3 | - |
| DC_2-12_n5DC_2-2-12_n5 | 0.3 | 0.4 | 0.8 |
| DC_2-12_n7DC_2-2-12_n7 | 0.5 | 0.3 | 0.5 |
| DC_2_(n)12 | 0.3 | 0.3 | 0.3 |
| DC_2-12_n30DC_2-2-12_n30 | 0.5 | 0.3 | 0.3 |
| DC_2-12_n41 DC_2-2-12_n41 | 0.5 | 0.3 | 0.5 |
| DC_2-12_n66, DC_2-2-12_n66 | 0.5 | 0.8 | 0.5 |
| DC_2-12_n77DC_2-2-12_n77 | 0.6 | 0.3 | 0.8 |
| DC_2_n12-n77DC_2-2_n12-n77 | 0.6 | 0.3 | 0.8 |
| DC_2-12_n78 | 0.6 | 0.6 | 0.8 |
| DC_2_n12-n78 | 0.6 | 0.3 | 0.8 |
| DC_2_n38-n66 | 0.5 | 0.9 | 0.5 |
| DC_2-13_n2 | 0.3 | 0.3 | 0.3 |
| DC_2-13_n5DC_2-2-13_n5 | 0.3 | 0.5 | 0.3 |
| DC_2-13_n25 | 0.3 | 0.3 | 0.3 |
| DC_2-13_n48 | 0.6 | 0.3 | 0.8 |
| DC_2-13_n66DC_2-2-13_n66 | 0.5 | 0.3 | 0.5 |
| DC_2-13_n77 DC_2-2-13_n77 | 0.6 | 0.5 | 0.8 |
| DC_2-14_n2 | 0.3 | 0.3 | 0.3 |
| DC_2-14_n5DC_2-2-14_n5 | 0.3 | 0.4 | 0.8 |
| DC_2-14_n30DC_2-2-14_n30 | 0.5 | 0.3 | 0.5 |
| DC_2-14_n66DC_2-2-14_n66 | 0.5 | 0.3 | 0.5 |
| DC_2-14_n77DC_2-2-14_n77 | 0.5 | 0.3 | 0.8 |
| DC_2_n25-n66 | 0.5 | 0.5 | 0.5 |
| DC_2-28_n7 | 0.5 | 0.3 | 0.5 |
| DC_2-28_n66 | 0.5 | 0.6 | 0.5 |
| DC_2-28_n78 | 0.6 | 0.5 | 0.8 |
| DC_2-29_n30DC_2-2-29_n30 | 0.5 | N/A | 0.3 |
| DC_2-29_n66DC_2-2-29_n66 | 0.5 | N/A | 0.5 |
| DC_2-29_n77 DC_2-2-29_n77 | 0.6 | N/A | 0.8 |
| DC_2-29-n78 | 0.6 | N/A | 0.8 |
| DC_2-30_n2 | 0.5 | 0.3 | 0.5 |
| DC_2-30_n5, DC_2-2-30_n5 | 0.5 | 0.3 | 0.3 |
| DC_2-30_n66, DC_2-2-30_n66 | 0.5 | 0.3 | 0.5 |
| DC_2-30_n77 DC_2-2-30_n77 | 0.6 | 0.3 | 0.8 |
| DC_2_n38-n71 | 0.5 | 0.5 | 0.3 |
| DC_2-38_n78 | 0.6 | 0.9 | 0.8 |
| DC_2_n38-n78 | 0.6 | 0.9 | 0.8 |
| DC_2_n41-n66DC_2-2_n41-n66 | 0.5 | 0.5 | 0.5 |
| DC_2_n41-n71DC_2-2_n41-n71 | 0.5 | 0.5 | 0.3 |
| DC_2_n41-n77 | 0.6 | 0.41 / 0.92 | 0.8 |
| DC_2_n41-n78 | 0.6 | 0.41 / 0.92 | 0.8 |
| DC_2-46_n5DC_2-2-46_n5 | 0.3 | NA | 0.3 |
| DC_2-46_n41 | 0.5 | NA | 0.41 / 0.92 |
| DC_2-46_n66 | 0.5 | NA | 0.5 |
| DC_2-46_n77DC_2-46-46_n77 | 0.6 | NA | 0.8 |
| DC_2-48_n2 | 0.6 | 0.8 | 0.6 |
| DC_2-48_n5 | 0.6 | 0.8 | 0.3 |
| DC_2-48_n12 | 0.6 | 0.3 | 0.8 |
| DC_2-48_n48 | 0.6 | 0.8 | 0.8 |
| DC_2-48_n66 | 0.6 | 0.8 | 0.6 |
| DC_2-48_n71 | 0.6 | 0.8 | 0.3 |
| DC_2-48_n77DC_2-48-48_n77DC_2-48-48-48_n77 | 0.3 | N/A | 0.5 |
| DC_2-66_n2DC_2-66-66_n2 | 0.5 | 0.5 | 0.5 |
| DC_2-66_n5,DC_2-2-66_n5,DC_2-66-66_n5,DC_2-2-66-66_n5,DC_2-66-66-66_n5 | 0.5 | 0.5 | 0.3 |
| DC_2-66_n7DC_2-2-66_n7 | 0.5 | 0.5 | 0.5 |
| DC_2-66_n12 | 0.5 | 0.5 | 0.8 |
| DC_2-66_n25 | 0.5 | 0.5 | 0.5 |
| DC_2-66-n28 | 0.5 | 0.5 | 0.6 |
| DC_2-66_n30 DC_2-2-66_n30DC_2-66-66_n30DC_2-2-66-66_n30 | 0.5 | 0.5 | 0.3 |
| DC_2-66_n38DC_2-2-66_n38DC_2-66-66_n38 | 0.5 | 0.5 | 0.9 |
| DC_2-66_n41 | 0.5 | 0.5 | 0.81 / 1.32 |
| DC_2-66_n48DC_2-66-66_n48 | 0.6 | 0.6 | 0.8 |
| DC_2-66_n66 DC_2-2-66-66_n66 | 0.5 | 0.5 | 0.5 |
| DC_2_(n)66 | 0.5 | 0.5 | 0.5 |
| DC_2-66_n71DC_2_n66-n71DC_2-2_n66-n71 | 0.5 | 0.5 | 0.3 |
| DC_2-66_n77DC_2-2-66_n77DC_2-66-66_n77DC_2-2-66-66_n77 | 0.6 | 0.6 | 0.8 |
| DC_2_n66-n77DC_2-2_n66-n77 | 0.6 | 0.6 | 0.8 |
| DC_2-66_n78DC_2-66-66_n78DC_2_n66-n78 | 0.6 | 0.6 | 0.8 |
| DC_2-71_n7 DC_2-2-71_n7 | 0.5 | 0.6 | 0.5 |
| DC_2-71_n38DC_2-2-71_n38 | 0.5 | 0.3 | 0.5 |
| DC_2-71_n41 DC_2-2-71_n41 | 0.5 | 0.3 | 0.5 |
| DC_2-71_n66DC_2-2-71_n66 | 0.5 | 0.3 | 0.5 |
| DC_2-71_n71 | 0.3 | 0.3 | 0.3 |
| DC_2-(n)71 | 0.3 | 0.3 | 0.3 |
| DC_2_n71-n77DC_2-2_n71-n77 | 0.6 | 0.6 | 0.8 |
| DC_2-71_n77DC_2-2-71_n77 | 0.6 | 0.6 | 0.8 |
| DC_2-71_n78 DC_2-2-71_n78 | 0.6 | 0.6 | 0.8 |
| DC_2_n71-n78DC_2-2_n71-n78 | 0.6 | 0.6 | 0.8 |
| DC_3_n1-n5 | 0.3 | 0.3 | 0.3 |
| DC_3_n1-n7 | 0.6 | 0.6 | 0.6 |
| DC_3_n1-n8 DC_3-3_n1-n8 | 0.3 | 0.3 | 0.3 |
| DC_3_n1-n20DC_3-3_n1-n20 | 0.3 | 0.3 | 0.3 |
| DC_3_n1-n28 | 0.3 | 0.3 | 0.6 |
| DC_3_n1-n38 | 0.5 | 0.5 | 0.5 |
| DC_3_n1-n40 | 0.5 | 0.5 | 0.5 |
| DC_3_n1-n41DC_3-3_n1-n41 | 0.5 | 0.5 | 0.5 |
| DC_3_n1-n75 | 0.5 | 0.5 | N/A |
| DC_3_n1-n77 | 0.6 | 0.6 | 0.8 |
| DC_3_n1-n78 | 0.6 | 0.6 | 0.8 |
| DC_3_n1-n105 | 0.3 | 0.3 | 0.6 |
| DC_(n)3-n7 | 0.5 | 0.5 | 0.5 |
| DC_3_n3-n7 | 0.5 | 0.5 | 0.5 |
| DC_(n)3-n8 | 0.3 | - | 0.3 |
| DC_(n)3-n28 | 0.3 | 0.3 | 0.3 |
| DC_3_n3-n28 | 0.3 | 0.3 | 0.3 |
| DC_(n)3-n77 | - | 0.6 | 0.8 |
| DC_(n)3-n78 | - | 0.6 | 0.8 |
| DC_3_n1-n79 | 0.3 | 0.3 | - |
| DC_3_n3-n41 | 0.5 | 0.5 | 0.33 / 0.84 |
| DC_3_n3-n77 | 0.6 | 0.6 | 0.8 |
| DC_3_n3-n78 | 0.6 | 0.6 | 0.8 |
| DC_3-5_n1 | 0.3 | 0.3 | 0.3 |
| DC_3-5_n3 | 0.3 | 0.3 | 0.3 |
| DC_3-5_n28 | 0.3 | 0.7 | 0.7 |
| DC_3_n5-n40DC_3-5_n40 | 0.5 | 0.3 | 0.5 |
| DC_3-5_n77 | 0.6 | 0.6 | 0.8 |
| DC_3-5_n78 | 0.6 | 0.6 | 0.8 |
| DC_3-5_n79 | 0.3 | 0.3 | - |
| DC_3_n5-n105 | 0.3 | 0.3 | 0.6 |
| DC_3-7_n1DC_3-3-7_n1DC_3-7-7_n1DC_3-3-7-7_n1 | 0.3 | 0.6 | 0.5 |
| DC_3-7_n3 | 0.5 | 0.5 | 0.5 |
| DC_3-7_n5 | 0.5 | 0.5 | 0.3 |
| DC_3-7_n7DC_3-(n)7 | 0.5 | 0.5 | 0.5 |
| DC_3-7_n8DC_3-3-7_n8DC_3-7-7_n8DC_3-3-7-7_n8 | 0.5 | 0.5 | 0.6 |
| DC_3-7_n26 | 0.5 | 0.5 | 0.3 |
| DC_3-7_n28 | 0.5 | 0.5 | 0.3 |
| DC_3_n7-n28 | 0.5 | 0.5 | 0.3 |
| DC_3-7_n38 | 0.5 | N/A | N/A |
| DC_3-7_n40DC_3-7-7_n40 | 0.6 | 0.8 | 0.9 |
| DC_3-7_n77DC_3-3-7_n77DC_3-7-7_n77DC_3-3-7-7_n77 | 0.6 | 0.6 | 0.8 |
| DC_3-7_n78DC_3-7-7_n78DC_3-3-7_n78DC_3-3-7-7_n78 | 0.6 | 0.6 | 0.8 |
| DC_3_n7-n78 | 0.6 | 0.6 | 0.8 |
| DC_3-7_n79DC_3-3-7_n79DC_3-7-7_n79DC_3-3-7-7_n79 | 0.5 | 0.5 | 0.8 |
| DC_3-7_n105 | 0.5 | 0.5 | 0.6 |
| DC_3-8_n1DC_3-3-8_n1 | 0.3 | 0.3 | 0.3 |
| DC_3-8_n7 | 0.5 | 0.6 | 0.5 |
| DC_3-8_n40 | 0.5 | 0.3 | 0.5 |
| DC_3_n8-n40 | 0.5 | 0.3 | 0.5 |
| DC_3_n8-n41 | 0.5 | 0.3 | 0.33/0.84 |
| DC_3-8_n41DC_3-3-8_n41 | 0.5 | 0.3 | 0.33/0.84 |
| DC_3-8_n28 | 0.3 | 0.6 | 0.5 |
| DC_3-8_n71 | 0.3 | 0.6 | 0.5 |
| DC_3-8_n77 | 0.6 | 0.6 | 0.8 |
| DC_3_n8-n77 | 0.6 | 0.6 | 0.8 |
| DC_3-8_n78 DC_3-3-8_n78 | 0.6 | 0.6 | 0.8 |
| DC_3_n8-n78 DC_3-3_n8-n78 | 0.6 | 0.6 | 0.8 |
| DC_3-8_n79 | 0.3 | 0.3 | - |
| DC_3-11_n28 | 0.8 | 0.9 | 0.6 |
| DC_3-11_n77 | 0.8 | 0.9 | 0.8 |
| DC_3-11_n79 | 0.8 | 0.9 | - |
| DC_3-18_n3 | 0.3 | 0.3 | 0.3 |
| DC_3-18_n28 | 0.3 | 0.5 | 0.3 |
| DC_3-18_n41 | 0.6 | 0.3 | 0.33 / 0.84 |
| DC_3-18_n77 | 0.6 | 0.3 | 0.8 |
| DC_3-18_n78 | 0.6 | 0.3 | 0.8 |
| DC_3-18_n79 | 0.3 | 0.3 | - |
| DC_3-19_n1 | 0.3 | 0.3 | 0.3 |
| DC_3-19_n77 | 0.6 | 0.3 | 0.8 |
| DC_3-19_n78 | 0.6 | 0.3 | 0.8 |
| DC_3-19_n79 | 0.3 | 0.3 | - |
| DC_3-20_n1 | 0.3 | 0.3 | 0.3 |
| DC_3-20_n3 | 0.3 | 0.3 | 0.3 |
| DC_3-20_n7 | 0.5 | 0.3 | 0.5 |
| DC_3-20_n8 | 0.3 | 0.4 | 0.4 |
| DC_3-20_n28 | 0.3 | 0.5 | 0.5 |
| DC_3-20_n38 | 0.5 | 0.3 | 0.5 |
| DC_3-20_n41DC_3-3-20_n41 | 0.5 | 0.3 | 0.53 / 1.24 |
| DC_3_n20-n67 | 0.3 | 0.5 | N/A |
| DC_3-20_n78 | 0.5 | 0.3 | 0.8 |
| DC_3_n20-n78DC_3-3_n20-n78 | 0.5 | 0.3 | 0.8 |
| DC_3-21_n1 | 0.8 | 0.9 | 0.3 |
| DC_3-21_n28 | 0.8 | 0.9 | 0.3 |
| DC_3-21_n77 | 0.8 | 0.9 | 0.8 |
| DC_3-21_n78 | 0.8 | 0.9 | 0.8 |
| DC_3-21_n79 | 0.8 | 0.9 | - |
| DC_3-26_n78 | 0.6 | 0.6 | 0.8 |
| DC_3_n26-n78 | 0.6 | 0.6 | 0.8 |
| DC_3-28_n1 | 0.3 | 0.6 | 0.3 |
| DC_3-28_n3 | 0.3 | 0.3 | 0.3 |
| DC_3-28_n5 | 0.3 | 0.5 | 0.5 |
| DC_3-28_n7 | 0.5 | 0.3 | 0.5 |
| DC_3-28_n38 | 0.5 | 0.3 | 0.5 |
| DC_3_n28-n40 | 0.5 | 0.3 | 0.5 |
| DC_3-28_n40 | 0.5 | 0.3 | 0.5 |
| DC_3-28_n41 | 0.5 | 0.5 | 0.33 / 0.84 |
| DC_3-28_n71 | 0.3 | 1.1 | 1.1 |
| DC_3_n28-n75 | 0.3 | 0.3 | N/A |
| DC_3-28_n77 | 0.6 | 0.5 | 0.8 |
| DC_3_n28-n77 | 0.6 | 0.5 | 0.8 |
| DC_3-28_n78 | 0.5 | 0.3 | 0.8 |
| DC_3_n28-n78 | 0.5 | 0.3 | 0.8 |
| DC_3_n28-n79 | 0.3 | 0.3 | - |
| DC_3-32_n1 | 0.5 | NA | 0.5 |
| DC_3-32_n7 | 0.7 | NA | 0.7 |
| DC_3-32_n28 | 0.3 | NA | 0.3 |
| DC_3-32_n41 | 0.7 | N/A | 0.7 |
| DC_3-32_n78 | 0.6 | NA | 0.8 |
| DC_3-38_n7 | 0.5 | NA | NA |
| DC_3A-38A_n1A | 0.5 | 0.5 | 0.5 |
| DC_3-38_n28 | 0.5 | 0.5 | 0.6 |
| DC_3_n38-n40 | 0.5 | 0.53 | 0.5 |
| DC_3-38_n78 | 0.6 | 0.5 | 0.8 |
| DC_8A-38A_n78A | 0.6 | 0.3 | 0.8 |
| DC_3_n38-n78 | 0.6 | 0.5 | 0.8 |
| DC_3-40_n1 | 0.5 | 0.5 | 0.5 |
| DC_3A-40A_n28A | 0.5 | 0.5 | 0.3 |
| DC_3_n40-n41 | 0.5 | 0.5 | 0.53 / 0.84 |
| DC_3_n40-n71 | 0.5 | 0.5 | 0.6 |
| DC_3-40_n77 | 0.6 | 0.5 | 0.8 |
| DC_3_n40-n77 | 0.6 | 0.5 | 0.8 |
| DC_3-40_n78 | 0.6 | 0.35 | 0.85 |
| DC_3_n40-n78 | 0.6 | 0.5 | 0.8 |
| DC_3_n40-n79 | 0.5 | 0.5 | - |
| DC_3_n40-n105 | 0.5 | 0.5 | 0.6 |
| DC_3-41_n1 | 0.5 | 0.33 / 0.84 | 0.5 |
| DC_3-41_n3 | 0.5 | 0.33 / 0.84 | 0.5 |
| DC_3-41_n28 | 0.5 | 0.33 / 0.84 | 0.3 |
| DC_3-(n)41 | 0.5 | 0.33 / 0.84 | 0.33 / 0.84 |
| DC_3-41_n41DC_3-3-41_n41 | 0.5 | 0.33 / 0.84 | 0.33 / 0.84 |
| DC_3_n41-n71 | 0.5 | 0.33 / 0.84 | 0.6 |
| DC_3-41_n77DC_3_n41-n77 | 0.6 | 0.33 / 0.84 | 0.8 |
| DC_3-41_n78 | 0.6 | 0.33 / 0.84 | 0.8 |
| DC_3_n41-n78 | 0.6 | 0.33 / 0.84 | 0.8 |
| DC_3-41_n79 | 0.6 | 0.33 / 0.84 | - |
| DC_3_n41-n79 | 0.6 | 0.33 / 0.84 | - |
| DC_3_SUL_n41-n80 | 0.5 | 0.33 / 0.84 | 0.5 |
| DC_3-42_n1 | 0.6 | 0.8 | 0.6 |
| DC_3-42_n28 | 0.6 | 0.8 | 0.8 |
| DC_3-42_n77 | 0.6 | N/A | 0.8 |
| DC_3-42_n78 | 0.6 | N/A | 0.8 |
| DC_3-42_n79 | 0.6 | N/A | - |
| DC_3_n71-n77 | 0.6 | 0.6 | 0.8 |
| DC_3_n71-n78 | 0.3 | 0.6 | 0.8 |
| DC_3_n75-n78 | 0.6 | N/A | 0.8 |
| DC_3_n77-n79 | 0.6 | 0.8 | - |
| DC_3_SUL_n77-n80 | 0.6 | 0.8 | 0.6 |
| DC_3_SUL_n77-n84 | 0.6 | 0.8 | 0.6 |
| DC_3_n78-n79DC_3-3_n78-n79 | 0.6 | 0.8 | 0.5 |
| DC_3_SUL_n78-n80 | 0.6 | 0.8 | 0.6 |
| DC_3_SUL_n78-n82 | 0.5 | 0.8 | 0.3 |
| DC_3_SUL_n78-n84 | 0.6 | 0.8 | 0.6 |
| DC_3_n78-n105 | 0.3 | 0.8 | 0.6 |
| DC_4-5_n78 | 0.6 | 0.6 | 0.8 |
| DC_4-7_n28 | 0.5 | 0.5 | 0.6 |
| DC_4-7_n78 | 0.6 | 0.5 | 0.8 |
| DC_5_n1-n28 | 0.5 | 0.3 | 0.6 |
| DC_5_n1-n78 | 0.6 | 0.6 | 0.8 |
| DC_5_n2-n41 | 0.6 | 0.5 | 0.41 / 0.92 |
| DC_5_n2-n66 | 0.3 | 0.5 | 0.5 |
| DC_5_n2-n77 | 0.6 | 0.6 | 0.8 |
| DC_5_n2-n78 | 0.6 | 0.6 | 0.8 |
| DC_5_n2-n7 | 0.3 | 0.5 | 0.5 |
| DC_5_n3-n28 | 0.5 | 0.3 | 0.5 |
| DC_5_n3-n78 | 0.6 | 0.6 | 0.8 |
| DC_5_n5-n77 | 0.6 | 0.6 | 0.8 |
| DC_5-7_n1DC_5-7-7_n1 | 0.3 | 0.6 | 0.5 |
| DC_5-7_n3 | 0.3 | 0.5 | 0.5 |
| DC_5-7_n7 | 0.5 | 0.3 | 0.3 |
| DC_5-7_n25 | 0.6 | 0.4 | 0.5 |
| DC_5_n7-n25 | 0.6 | 0.4 | 0.5 |
| DC_5-7_n28DC_5-7-7_n28 | 0.7 | 0.3 | 0.7 |
| DC_5-7_n40DC_5-7-7_n40 | 0.3 | 0.5 | 0.6 |
| DC_5-7_n66 | 0.3 | 0.5 | 0.5 |
| DC_5_n7-n66 | 0.3 | 0.5 | 0.5 |
| DC_5-7_n71 | 0.5 | 0.3 | 0.6 |
| DC_5-7_n77 | 0.6 | 0.6 | 0.8 |
| DC_5_n7-n77 | 0.6 | 0.6 | 0.8 |
| DC_5-7_n78DC_5-7-7_n78 | 0.6 | 0.6 | 0.8 |
| DC_5_n7-n78 | 0.6 | 0.6 | 0.8 |
| DC_5_(n)12 | 0.8 | 0.4 | 0.4 |
| DC_5-13_n2 | 0.5 | 0.5 | 0.3 |
| DC_5-13_n66 | 0.3 | 0.3 | 0.3 |
| DC_5-13_n77 | 0.6 | 0.5 | 0.8 |
| DC_5_n28-n77 | 0.6 | 0.5 | 0.9 |
| DC_5_n28-n78 | 0.6 | 0.5 | 0.9 |
| DC_5_n28-n79 | 0.7 | 0.7 | 0.8 |
| DC_5-30_n2 | 0.3 | 0.3 | 0.5 |
| DC_5-30_n66 | 0.3 | 0.3 | 0.5 |
| DC_5-30_n77 | 0.6 | 0.3 | 0.8 |
| DC_5_n38-n66 | 0.5 | 0.8 | 0.5 |
| DC_5-40_n77 | 0.6 | 0.3 | 0.8 |
| DC_5_n40-n77 | 0.6 | 0.3 | 0.8 |
| DC_5-40_n78 | 0.6 | 0.5 | 0.8 |
| DC_5_n40-n78 | 0.6 | 0.5 | 0.8 |
| DC_5_n41-n66 | 0.6 | 0.81 / 1.32 | 0.5 |
| DC_5_n41-n77 | 0.6 | 0.3 | 0.8 |
| DC_5_n41-n78 | 0.6 | 0.3 | 0.8 |
| DC_5-41_n79 | 0.3 | 0.3 | - |
| DC_5-46_n66 | 0.3 | N/A | 0.3 |
| DC_5-48_n12 | 0.8 | 0.3 | 0.4 |
| DC_5-48_n71 | 0.5 | 0.3 | 0.5 |
| DC_5-48_n77 | 0.6 | N/A | 0.8 |
| DC_5-66_n2DC_5-5-66_n2DC_5-66-66_n2DC_5-5-66-66_n2 | 0.3 | 0.5 | 0.5 |
| DC_5-66_n5DC_5-66-66_n5 | 0.3 | 0.3 | 0.3 |
| DC_5-66-n7 | 0.3 | 0.5 | 0.5 |
| DC_5-66_n12 | 0.3 | 0.8 | 0.8 |
| DC_5-66_n25 | 0.3 | 0.5 | 0.5 |
| DC_5-66_n30DC_5-66-66_n30 | 0.3 | 0.5 | 0.3 |
| DC_5-66_n41 | 0.6 | 0.5 | 0.81 / 1.32 |
| DC_5-66_n48DC_5-66-66_n48 | 0.3 | 0.6 | 0.8 |
| DC_5-(n)66DC_5-66_n66DC_5-5-66_n66DC_5-66-(n)66DC_5-66-66_n66DC_5-5-66-66_n66 | 0.3 | 0.3 | 0.3 |
| DC_5-66_n71 | 0.5 | 0.3 | 0.5 |
| DC_5-66_n77 DC_5-66-66_n77 | 0.6 | 0.6 | 0.8 |
| DC_5_n66-n77 | 0.6 | 0.6 | 0.8 |
| DC_5-66_n78 | 0.6 | 0.6 | 0.8 |
| DC_5_n66-n78 | 0.6 | 0.6 | 0.8 |
| DC_5_SUL_n78-n89 | 0.6 | 0.8 | 0.6 |
| DC_7_n1-n8DC_7-7_n1-n8 | 0.6 | 0.5 | 0.5 |
| DC_7_n1-n28 | 0.6 | 0.5 | 0.6 |
| DC_7_n1-n40 | 0.8 | 0.6 | 0.9 |
| DC_7_n1-n75 | 0.6 | 0.5 | N/A |
| DC_7_n1-n78 | 0.6 | 0.6 | 0.8 |
| DC_7_n2-n66 | 0.5 | 0.5 | 0.5 |
| DC_7_n2-n71 | 0.5 | 0.5 | 0.3 |
| DC_7_n2-n77 | 0.5 | 0.6 | 0.8 |
| DC_7_n2-n78 | 0.5 | 0.6 | 0.8 |
| DC_7_n3-n78 | 0.6 | 0.6 | 0.8 |
| DC_7_n5-n40 | 0.8 | 0.6 | 0.9 |
| DC_7_n7-n78 | 0.5 | 0.5 | 0.8 |
| DC_7-8_n1DC_7-7-8_n1 | 0.6 | 0.6 | 0.5 |
| DC_7-8_n3 | 0.5 | 0.6 | 0.5 |
| DC_7-8_n7 | 0.3 | 0.6 | 0.3 |
| DC_7-8_n20 | 0.3 | 0.6 | 0.6 |
| DC_7-8_n28 | 0.3 | 0.6 | 0.5 |
| DC_7-8_n40 | 0.5 | 0.6 | 0.6 |
| DC_7_n8-n40 | 0.5 | 0.6 | 0.6 |
| DC_7-8_n77 | 0.5 | 0.6 | 0.8 |
| DC_7-8_n78DC_7-7-8_n78 | 0.5 | 0.6 | 0.8 |
| DC_7_n8-n78 DC_7-7_n8-n78 | 0.5 | 0.6 | 0.8 |
| DC_7-12_n25 | 0.5 | 0.3 | 0.5 |
| DC_7-12_n66 | 0.5 | 0.5 | 0.5 |
| DC_7_n12-n77 | 0.5 | 0.5 | 0.8 |
| DC_7-12_n77 | 0.5 | 0.5 | 0.8 |
| DC_7-12_n78 | 0.5 | 0.5 | 0.8 |
| DC_7_n12-n78 | 0.5 | 0.5 | 0.8 |
| DC_7-13_n25DC_7-7-13_n25 | 0.5 | 0.3 | 0.5 |
| DC_7-13_n66 | 0.5 | 0.3 | 0.5 |
| DC_7-20_n1 | 0.6 | 0.3 | 0.5 |
| DC_7-20_n3 | 0.5 | 0.3 | 0.5 |
| DC_7-20_n7 | 0.3 | 0.3 | 0.3 |
| DC_7-20_n8 | 0.3 | 0.4 | 0.4 |
| DC_7-20_n28 | 0.3 | 0.6 | 0.6 |
| DC_7-20_n38 | N/A | 0.3 | N/A |
| DC_7-20_n78DC_7-7-20_n78 | 0.3 | 0.3 | 0.8 |
| DC_7-25_n77DC_7-7-25_n77DC_7-25-25_n77DC_7-7-25-25_n77 | 0.5 | 0.6 | 0.8 |
| DC_7_n25-n71 | 0.5 | 0.5 | 0.6 |
| DC_7-25_n78DC_7-7-25_n78DC_7-25-25_n78DC_7-7-25-25_n78 | 0.5 | 0.6 | 0.8 |
| DC_7_n25-n66 DC_7-7_n25-n66 | 0.5 | 0.5 | 0.5 |
| DC_7-26_n78 | 0.6 | 0.6 | 0.8 |
| DC_7_n26-n78 | 0.6 | 0.6 | 0.8 |
| DC_7-28_n1 DC_7-7-28_n1 | 0.6 | 0.6 | 0.5 |
| DC_7-28_n2 | 0.5 | 0.3 | 0.5 |
| DC_7-28_n3 | 0.5 | 0.3 | 0.5 |
| DC_7-28_n5 | 0.3 | 0.5 | 0.5 |
| DC_7-28_n7 | 0.3 | 0.3 | 0.3 |
| DC_7-28_n20 | 0.3 | 0.6 | 0.6 |
| DC_7_n28-n40 | 0.5 | 0.3 | 0.6 |
| DC_7-28_n40 | 0.5 | 0.3 | 0.6 |
| DC_7-28_n66 | 0.5 | 0.6 | 0.5 |
| DC_7-28_n78 | 0.3 | 0.3 | 0.8 |
| DC_7_n28-n78DC_7-7_n28-n78 | 0.3 | 0.3 | 0.8 |
| DC_7-29_n78 | 0.5 | N/A | 0.8 |
| DC_7-32_n1 | 0.6 | N/A | 0.5 |
| DC_7-32_n3 | 0.7 | N/A | 0.7 |
| DC_7-32_n8 | 0.7 | N/A | 0.6 |
| DC_7-32_n28 | 0.3 | N/A | 0.7 |
| DC_7-32_n78 | 0.5 | N/A | 0.8 |
| DC_7-38_n3 | 0.5 | 0.5 | 0.5 |
| DC_7_n38-n78 | N/A | N/A | 0.8 |
| DC_7_n78-n79DC_7-7_n78-n79 | 0.5 | 0.8 | 0.8 |
| DC_7-40_n1 | 0.8 | 0.9 | 0.6 |
| DC_7_n40-n77DC_7-7_n40-n77 | 0.5 | 0.6 | 0.8 |
| DC_7-40-n78 | 0.5 | 0.35 | 0.85 |
| DC_7_n40-n78DC_7-7_n40-n78 | 0.5 | 0.6 | 0.8 |
| DC_7_n40-n105 | 0.5 | 0.6 | 0.6 |
| DC_7-46_n78 | 0.5 | N/A | 0.8 |
| DC_7-66_n2 | 0.5 | 0.5 | 0.5 |
| DC_7-66_n5DC_7-66-66_n5DC_7-7-66_n5DC_7-7-66-66_n5 | 0.3 | 0.3 | 0.3 |
| DC_7-66_n7DC_7-66-66_n7 | 0.5 | 0.5 | 0.5 |
| DC_7-66_n12 | 0.5 | 0.5 | 0.8 |
| DC_7-66_n25DC_7-7-66_n25 | 0.5 | 0.5 | 0.5 |
| DC_7-66_n28 | 0.5 | 0.5 | 0.6 |
| DC_7-66_n38 | N/A | 0.5 | N/A |
| DC_7-(n)66DC_7-66_n66DC_7-7-(n)66DC_7-7-66_n66DC_7-7-66-(n)66DC_7-66-(n)66 | 0.5 | 0.5 | 0.5 |
| DC_7-66_n71 DC_7-66-66_n71 | 0.5 | 0.5 | 0.5 |
| DC_7_n66-n71 | 0.5 | 0.5 | 0.5 |
| DC_7-66_n77DC_7-7-66_n77 | 0.5 | 0.6 | 0.8 |
| DC_7_n66-n77 | 0.5 | 0.6 | 0.8 |
| DC_7-66_n78DC_7-7-66_n78DC_7-66-66_n78DC_7-7-66-66_n78 | 0.5 | 0.5 | - |
| DC_7_n66-n78DC_7-7_n66-n78 | 0.5 | 0.6 | 0.8 |
| DC_7-71_n12 | 0.5 | 0.5 | 0.3 |
| DC_7-71_n25 | 0.5 | 0.3 | 0.5 |
| DC_7-71_n66 | 0.5 | 0.5 | 0.5 |
| DC_7-71_n77 | 0.5 | 0.5 | 0.8 |
| DC_7_n71-n77 | 0.5 | 0.6 | 0.8 |
| DC_7-71_n78 | 0.5 | 0.5 | 0.8 |
| DC_7_n71-n78 | 0.3 | 0.5 | 0.8 |
| DC_7_n75-n78 | 0.5 | N/A | 0.8 |
| DC_7_SUL_n78-n80 | 0.6 | 0.8 | 0.6 |
| DC_7_n78-n105 | 0.5 | 0.8 | 0.6 |
| DC_8_n1-n3 | 0.3 | 0.3 | 0.3 |
| DC_8_n1-n28 | 0.6 | 0.3 | 0.6 |
| DC_8_n1-n40 | 0.3 | 0.3 | 0.5 |
| DC_8_n1-n41 | 0.6 | 0.5 | 0.6 |
| DC_8_n1-n77 | 0.6 | 0.6 | 0.8 |
| DC_8_n1-n78 | 0.6 | 0.3 | 0.8 |
| DC_8_n1-n79 | 0.3 | 0.3 | 0 |
| DC_8_(n)3 | 0.3 | 0.3 | 0.3 |
| DC_8_n3-n28 | 0.6 | 0.3 | 0.5 |
| DC_8_n3-n77 | 0.6 | 0.6 | 0.8 |
| DC_8_n3-n78 | 0.6 | 0.6 | 0.8 |
| DC_8_n3-n79 | 0.3 | 0.3 | 0.8 |
| DC_8_n7-n78 | 0.6 | 0.5 | 0.8 |
| DC_8-11_n3 | 0.3 | 0.8 | 0.9 |
| DC_8-11_n28 | 0.6 | 0.4 | 0.6 |
| DC_8-11_n77 | 0.6 | 0.4 | 0.8 |
| DC_8-11_n78 | 0.6 | 0.4 | 0.8 |
| DC_8-20_n1 | 0.4 | 0.4 | 0.3 |
| DC_8-20_n3 | 0.4 | 0.4 | 0.3 |
| DC_8-20_n28 | 0.6 | 0.5 | 0.5 |
| DC_8-20_n78 | 0.6 | 0.6 | 0.8 |
| DC_8A-28A_n1A | 0.6 | 0.5 | 0.3 |
| DC_8-28_n3 | 0.6 | 0.5 | 0.3 |
| DC_8-28_n40 | 0.6 | 0.5 | 0.3 |
| DC_8-28_n71 | 0.7 | 1.1 | 1.1 |
| DC_8_n28-n77DC_8-28_n77 | 0.6 | 0.5 | 0.8 |
| DC_8_n28-n78 | 0.6 | 0.5 | 0.8 |
| DC_8-32_n1 | 0.3 | N/A | 0.5 |
| DC_8-32_n3 | 0.3 | N/A | 0.8 |
| DC_8-32_n28 | 0.5 | N/A | 0.5 |
| DC_8-38_n1 | 0.3 | 0.5 | 0.5 |
| DC_8A-38A_n28A | 0.6 | 0.3 | 0.5 |
| DC_8_n38-n40 | 0.3 | 0.3 | 0.3 |
| DC_8-39_n40 | 0.3 | 0.3 | 0.3 |
| DC_8_n39-n40 | 0.3 | 0.3 | 0.3 |
| DC_8-39_n41 | 0.3 | 0.3 | 0.3 |
| DC_8-39_n79 | 0.3 | 0.3 | 0.8 |
| DC_8_n39-n79 | 0.3 | 0.3 | - |
| DC_8-40_n1 | 0.3 | 0.5 | 0.3 |
| DC_8A-40A_n28A | 0.6 | 0.3 | 0.5 |
| DC_8_n40-n71 | 0.6 | 0.9 | 0.6 |
| DC_8_n40-n77 | 0.6 | 0.5 | 0.8 |
| DC_8-40-n78 | 0.6 | 0.35 | 0.85 |
| DC_8_n40-n41 | 0.3 | 0.3 | 0.3 |
| DC_8_n40-n79 | 0.3 | 0.3 | - |
| DC_8-41_n1 | 0.3 | 0.3 | 0.3 |
| DC_8-41_n3 | 0.3 | 0.33 / 0.84 | 0.5 |
| DC_8-41_n41 | 0.6 | 0.3 | 0.3 |
| DC_8-41_n77 | 0.6 | 0.3 | 0.8 |
| DC_8-41_n78 | 0.6 | 0.3 | 0.8 |
| DC_8_n41-n78 | 0.6 | 0.5 | 0.8 |
| DC_8_n41-n79 | 0.3 | 0.3 | - |
| DC_8_SUL_n41-n81 | 0.3 | 0.3 | 0.3 |
| DC_8-42_n1 | 0.6 | 0.8 | 0.3 |
| DC_8-42_n3 | 0.6 | 0.8 | 0.6 |
| DC_8-42_n28 | 0.6 | 0.8 | 0.8 |
| DC_8-42_n77 | 0.6 | N/A | 0.8 |
| DC_8-42_n79 | 0.6 | 0.8 | - |
| DC_8_n71-n77 | 0.67 | 0.57 | 0.8 |
| DC_8_n77-n79 | 0.6 | 0.8 | 0.5 |
| DC_8_SUL_n78-n80 | 0.6 | 0.8 | 0.6 |
| DC_8_SUL_n78- n81 | 0.6 | 0.8 | 0.6 |
| DC_11_n1-n3 | 0.8 | 0.3 | 0.9 |
| DC_11_n1-n77 | 0.4 | 0.6 | 0.8 |
| DC_11_n3-n28 | 0.8 | 0.9 | 0.6 |
| DC_11_n3-n77 | 0.8 | 0.9 | 0.8 |
| DC_11_n3-n79 | 0.8 | 0.9 | 0.8 |
| DC_11-18_n77 | 0.4 | 0.3 | 0.8 |
| DC_11-18_n78 | 0.4 | 0.3 | 0.8 |
| DC_11_n28-n77 | 0.4 | 0.6 | 0.8 |
| DC_11_n77-n79 | - | 0.5 | - |
| DC_12_n2-n7 | 0.3 | 0.5 | 0.5 |
| DC_12_n2-n38 | 0.3 | 0.5 | 0.5 |
| DC_12_n2-n41 | 0.3 | 0.5 | 0.5 |
| DC_12_n2-n66 | 0.8 | 0.5 | 0.5 |
| DC_12_n2-n77 | 0.3 | 0.6 | 0.8 |
| DC_12_n2-n78 | 0.3 | 0.6 | 0.8 |
| DC_12_(n)5 | 0.8 | 0.4 | 0.8 |
| DC_12_n7-n25 | 0.3 | 0.5 | 0.5 |
| DC_12_n7-n66 | 0.8 | 0.5 | 0.5 |
| DC_12_n7-n77 | 0.5 | 0.5 | 0.8 |
| DC_12_n7-n78 | 0.5 | 0.5 | 0.8 |
| DC_12_n25-n41 | 0.3 | 0.5 | 0.41/0.92 |
| DC_12_n25-n66 | 0.8 | 0.5 | 0.5 |
| DC_12_n25-n77 | 0.5 | 0.3 | 0.8 |
| DC_12-30_n2 | 0.3 | 0.3 | 0.5 |
| DC_12-30_n5 | 0.8 | 0.8 | 0.3 |
| DC_12-30_n66 | 0.8 | 0.3 | 0.5 |
| DC_12-30_n77 | 0.5 | 0.3 | 0.5 |
| DC_12_n41-n66 | 0.6 | 0.81 / 1.32 | 0.5 |
| DC_12-48_n5 | 0.4 | 0.3 | 0.8 |
| DC_12-66_n2 | 0.8 | 0.5 | 0.5 |
| DC_12-66_n5DC_12-66-66_n5 | 0.8 | 0.8 | 0.3 |
| DC_12-66_n7 | 0.6 | 0.5 | 0.8 |
| DC_12-66_n25 | 0.8 | 0.5 | 0.5 |
| DC_12-66_n30 DC_12-66-66_n30 | 0.8 | 0.5 | 0.3 |
| DC_12-66_n41 | 0.6 | 0.5 | 0.81 / 1.32 |
| DC_12_n66-n77 | 0.8 | 0.6 | 0.8 |
| DC_12-66_n77 DC_12-66-66_n77 | 0.8 | 0.6 | 0.8 |
| DC_12-66_n78 | 0.6 | 0.6 | 0.8 |
| DC_12-(n)66DC_12-66_n66 | 0.8 | 0.3 | 0.3 |
| DC_12_n66-n78 | 0.6 | 0.6 | 0.8 |
| DC_12-71_n2 | 0.5 | 0.5 | 0.3 |
| DC_12-71_n77 | 0.4 | 0.8 | 0.5 |
| DC_13_n2-n77 | 0.3 | 0.6 | 0.8 |
| DC_13_n5-n48 | 0.4 | 0.8 | 0.3 |
| DC_13_n5-n77 | 0.5 | 0.6 | 0.8 |
| DC_13_n7-n78 | 0.5 | 0.5 | 0.8 |
| DC_13_n25-n66 | 0.3 | 0.5 | 0.5 |
| DC_13-46_n2 | 0.3 | N/A | 0.3 |
| DC_13-46_n5 | 0.5 | N/A | 0.5 |
| DC_13-46_n66 | 0.3 | N/A | 0.3 |
| DC_13-46_n77 DC_13-46-46_n7 | 0.5 | N/A | 0.8 |
| DC_13-48_n2 | 0.3 | 0.8 | 0.6 |
| DC_13-48_n66 | 0.3 | 0.8 | 0.6 |
| DC_13_n48-n66 | 0.3 | 0.8 | 0.6 |
| DC_13-48_n77 | 0.5 | N/A | 0.8 |
| DC_13-66_n2DC_13-66-66_n2 | 0.3 | 0.5 | 0.5 |
| DC_13-66_n5 | 0.5 | 0.3 | 0.5 |
| DC_13-66_n48DC_13-66-66_n48 | 0.3 | 0.6 | 0.8 |
| DC_13-(n)66DC_13-66_n66DC_13-66-(n)66DC_13-66-66_n66 | 0.3 | 0.3 | 0.3 |
| DC_13-66_n77DC_13-66-66_n77 | 0.5 | 0.6 | 0.8 |
| DC_13_n66-n77 | 0.3 | 0.6 | 0.8 |
| DC_14-30_n2 | 0.3 | 0.3 | 0.5 |
| DC_14-30_n5 | 0.8 | 0.8 | 0.3 |
| DC_14-30_n66 | 0.3 | 0.3 | 0.5 |
| DC_14-30_n77 | 0.5 | 0.3 | 0.8 |
| DC_14-66_n2 DC_14-66-66_n2 | 0.3 | 0.5 | 0.5 |
| DC_14-66_n5DC_14-66-66_n5 | 0.8 | 0.8 | 0.3 |
| DC_14-66_n30DC_14-66-66_n30 | 0.3 | 0.5 | 0.3 |
| DC_14-66_n66 | 0.3 | 0.3 | 0.3 |
| DC_14-66_n77DC_14-66-66_n77 | 0.6 | 0.6 | 0.8 |
| DC_18_n3-n41 | 0.3 | 0.5 | 0.3 |
| DC_18_n3-n77 | 0.3 | 0.6 | 0.8 |
| DC_18_n3-n78 | 0.3 | 0.6 | 0.8 |
| DC_18_n28-n41 | 0.5 | 0.5 | 0.3 |
| DC_18-28_n77 | 0.5 | 0.5 | 0.8 |
| DC_18_n28-n77 | 0.5 | 0.5 | 0.8 |
| DC_18-28_n78 | 0.5 | 0.5 | 0.8 |
| DC_18_n28-n78 | 0.5 | 0.5 | 0.8 |
| DC_18-28_n79 | 0.5 | 0.5 | - |
| DC_18-41_n3 | 0.3 | 0.33 / 0.84 | 0.5 |
| DC_18-41_n77 | 0.3 | 0.3 | 0.8 |
| DC_18_n41-n77 | 0.3 | 0.3 | 0.8 |
| DC_18-41_n78 | 0.3 | 0.3 | 0.8 |
| DC_18_n41-n78 | 0.3 | 0.3 | 0.8 |
| DC_18-42_n77 | 0.3 | N/A | 0.8 |
| DC_18-42_n78 | 0.3 | N/A | 0.8 |
| DC_18-42_n79 | 0.3 | N/A | - |
| DC_19_n1-n77 | 0.3 | 0.3 | 0.8 |
| DC_19_n1-n78 | 0.3 | 0.3 | 0.8 |
| DC_19_n1-n79 | 0.3 | 0.3 | - |
| DC_19-21_n1 | 0.3 | 0.4 | 0.3 |
| DC_19-21_n77 | 0.3 | 0.4 | 0.8 |
| DC_19-21_n78 | 0.3 | 0.4 | 0.8 |
| DC_19-21_n79 | 0.3 | 0.4 | - |
| DC_19-42_n1 | 0.3 | 0.8 | 0.3 |
| DC_19-42_n77 | 0.3 | N/A | 0.8 |
| DC_19-42_n78 | 0.3 | N/A | 0.8 |
| DC_19-42_n79 | 0.3 | N/A | - |
| DC_19_n77-n79 | 0.3 | 0.8 | - |
| DC_19_n78-n79 | 0.3 | 0.8 | 0.5 |
| DC_20_n1-n7 | 0.3 | 0.5 | 0.6 |
| DC_20_n1-n28 | 0.3 | 0.6 | 0.6 |
| DC_20_n1-n41 | 0.6 | 0.5 | 0.6 |
| DC_20_n1-n67 | 0.6 | 0.5 | N/A |
| DC_20_n1-n75 | 0.3 | 0.5 | N/A |
| DC_20_n1-n78 | 0.3 | 0.3 | 0.8 |
| DC_20-(n)3 | 0.3 | 0.3 | 0.3 |
| DC_20_n3-n67 | 0.5 | 0.3 | N/A |
| DC_20_n3-n78 | 0.3 | 0.5 | 0.8 |
| DC_20_n7-n28 | 0.5 | 0.3 | 0.5 |
| DC_20_n8-n75 | 0.4 | 0.4 | N/A |
| DC_20_n7-n78 | 0.3 | 0.3 | 0.8 |
| DC_20_n8-n78 | 0.6 | 0.6 | 0.8 |
| DC_20-28_n1 | 0.6 | 0.6 | 0.5 |
| DC_20-28_n3 | 0.5 | 0.6 | 0.5 |
| DC_20-28_n7 | 0.6 | 0.6 | 0.3 |
| DC_20_n28-n75 | 0.5 | 0.7 | N/A |
| DC_20-28_n78 | 0.6 | 0.5 | 0.8 |
| DC_20_n28-n78 | 0.6 | 0.6 | 0.8 |
| DC_20-32_n1 | 0.3 | N/A | 0.5 |
| DC_20-32_n3 | 0.3 | N/A | 0.5 |
| DC_20-32_n7 | 0.3 | N/A | 0.7 |
| DC_20-32_n8 | 0.4 | N/A | 0.4 |
| DC_20-32_n28 | 0.5 | N/A | 0.7 |
| DC_20-32_n78 | 0.5 | N/A | 0.8 |
| DC_20-38_n1 | 0.5 | 0.3 | 0.5 |
| DC_20-38_n1 | 0.5 | 0.3 | 0.5 |
| DC_20-38_n3 | 0.3 | 0.5 | 0.5 |
| DC_20A-38A_n28A | 0.6 | 0.3 | 0.6 |
| DC_20-(n)38 | 0.3 | 0.3 | 0.3 |
| DC_20-38_n78 | 0.6 | - | 0.8 |
| DC_20_n38-n78 | 0.6 | 0.3 | 0.8 |
| DC_20-40-n1 | 0.3 | 0.5 | 0.3 |
| DC_20A-40A_n28A | 0.5 | 0.3 | 0.5 |
| DC_20-40_n78 | 0.6 | 0.35 | 0.85 |
| DC_20-41_n1 | 0.3 | 0.51 / 1.22 | 0.5 |
| DC_20-41_n78 | 0.5 | 0.3 | 0.8 |
| DC_20_n41-n78 | 0.5 | 0.3 | 0.8 |
| DC_20-67_n3 | 0.5 | N/A | 0.3 |
| DC_20_n75-n78 | 0.5 | N/A | 0.8 |
| DC_20_n76-n78 | 0.5 | N/A | 0.8 |
| DC_20_SUL_n78-n80 | 0.3 | 0.8 | 0.5 |
| DC_20_SUL_n78-n82 | 0.6 | 0.8 | 0.6 |
| DC_20_SUL_n78-n83 | 0.8 | 0.8 | 0.8 |
| DC_20_n78-n92 | 0.6 | - | 0.8 |
| DC_21_n1-n77 | 0.3 | 0.3 | 0.8 |
| DC_21_n1-n78 | 0.4 | 0.6 | 0.8 |
| DC_21_n1-n79 | 0.3 | 0.3 | - |
| DC_21_n28-n77 | 0.4 | 0.5 | 0.8 |
| DC_21_n28-n78 | 0.4 | 0.5 | 0.8 |
| DC_21_n28-n79 | 0.4 | - | 0.3 |
| DC_21-42_n1 | 0.4 | 0.8 | 0.3 |
| DC_21-42_n77 | 0.4 | N/A | 0.8 |
| DC_21-42_n78 | 0.4 | N/A | 0.8 |
| DC_21-42_n79 | 0.4 | N/A | - |
| DC_21_n77-n79 | 0.4 | 0.8 | - |
| DC_21_n78-n79 | 0.4 | 0.8 | 0.5 |
| DC_25-41_n41DC_25_(n)41DC_25-25-41_n41DC_25-25_(n)41 | 0.5 | 0.41 / 0.92 | 0.41 / 0.92 |
| DC_25-66_n77DC_25-25-66_n77 | 0.6 | 0.6 | 0.8 |
| DC_25-66_n78DC_25-25-66_n78 | 0.6 | 0.6 | 0.8 |
| DC_28_n1-n5 | 0.6 | 0.3 | 0.5 |
| DC_28_n1-n40 | 0.6 | 0.3 | 0.5 |
| DC_28_n1-n78 | 0.6 | 0.3 | 0.8 |
| DC_28_n1-n105 | 1 | 0.3 | 1 |
| DC_28_n3-n77 | 0.5 | 0.6 | 0.8 |
| DC_28_n3-n78 | 0.3 | 0.6 | 0.8 |
| DC_28_n5-n40 | 0.6 | 0.6 | 0.9 |
| DC_28_n5-n78 | 0.7 | 0.7 | 0.8 |
| DC_28_n5-n105 | 1.0 | 0.7 | 1.0 |
| DC_28_n7-n78 | 0.3 | 0.3 | 0.8 |
| DC_28_n8-n78 | 0.5 | 0.6 | 0.3 |
| DC_28_n40-n71 | 1.1 | 0.6 | 1.1 |
| DC_28_n40-n77 | 0.5 | 0.3 | 0.8 |
| DC_28_n40-n78 | 0.5 | 0.35 | 0.85 |
| DC_28-32_n1 | 0.6 | N/A | 0.5 |
| DC_28-32_n3 | 0.3 | N/A | 0.3 |
| DC_28-32_n41 | 0.6 | N/A | 0.3 |
| DC_28-38_n1 | 0.6 | 0.5 | 0.5 |
| DC_28-38_n78 | 0.5 | 0.3 | 0.8 |
| DC_28A-40A_n1A | 0.6 | 0.6 | 0.5 |
| DC_28_n40-n41 | 0.3 | 0.5 | 0.5 |
| DC_28-41_n77 | 0.5 | 0.3 | 0.8 |
| DC_28-41_n78 | 0.5 | 0.3 | 0.8 |
| DC_28-41_n79 | 0.3 | 0.3 | 0.8 |
| DC_28_SUL_n41-n83 | 0.3 | 0.3 | 0.3 |
| DC_28-42_n77 | 0.5 | N/A | 0.8 |
| DC_28-42_n78 | 0.5 | N/A | 0.8 |
| DC_28-42_n79 | 0.5 | N/A | - |
| DC_28-66_n7 | 0.6 | 0.5 | 0.5 |
| DC_28-66_n66 | 0.6 | 0.3 | 0.3 |
| DC_28_n71-n77 | 1.1 | 1.1 | 0.8 |
| DC_28_n78-n105 | 1 | 0.8 | 1 |
| DC_28_SUL_n78-n83 | 0.5 | 0.8 | 0.5 |
| DC_29-30_n2 | N/A | 0.3 | 0.5 |
| DC_29-30_n66 | N/A | 0.3 | 0.5 |
| DC_29-30_n77 | N/A | 0.3 | 0.5 |
| DC_29-66_n2DC_29-66-66_n2 | N/A | 0.5 | 0.5 |
| DC_29-66_n30DC_29-66-66_n30 | N/A | 0.5 | 0.3 |
| DC_29-(n)66 | N/A | 0.5 | 0.5 |
| DC_29-66_n77 | N/A | 0.6 | 0.8 |
| DC_29-66-66_n77 | N/A | 0.6 | 0.8 |
| DC_29-66_n78 | N/A | 0.6 | 0.8 |
| DC_30-(n)5 | 0.3 | 0.3 | 0.3 |
| DC_30-66_n2 | 0.3 | 0.5 | 0.5 |
| DC_30-66_n5, DC_30-66-66_n5, DC_30-66-66-66_n5 | 0.3 | 0.5 | 0.3 |
| DC_30-66_n66 | 0.3 | 0.5 | 0.5 |
| DC_30-66_n77 DC_30-66-66_n77 | 0.3 | 0.6 | 0.8 |
| DC_32-38_n1 | N/A | 0.5 | 0.5 |
| DC_32-38_n28 | N/A | 0.7 | 0.6 |
| DC_38_n3-n78 | 0.5 | 0.6 | 0.8 |
| DC_38_n28-n78 | 0.3 | 0.5 | 0.8 |
| DC_38A-40A_n1A | 0.5 | 0.5 | 0.5 |
| DC_38A-40A_n28A | 0.5 | 0.5 | 0.3 |
| DC_39_n40-n41 | 0.3 | 0.3/0.68 | 0.3/0.68 |
| DC_39_n40-n79 | 0.3 | - | 0.8 |
| DC_39_n41-n79 | 0.5 | 0.5 | 0.8 |
| DC_40_n1-n78 | 0.5 | 0.3 | 0.8 |
| DC_40-42_n77 | 0.45 | N/A | 0.55 |
| DC_40-42_n78 | 0.45 | N/A 5 | 0.55 |
| DC_41_n1-n3 | 0.53 | 0.5 | 0.84 |
| DC_41_n1-n41 | 0.5 | 0.5 | 0.5 |
| DC_41_n1-n77 | 0.5 | 0.5 | 0.8 |
| DC_41_n1-n78 | 0.5 | 0.5 | 0.8 |
| DC_41_n3-n41 | 0.33 / 084 | 0.5 | 0.33 / 084 |
| DC_41_n3-n77 | 0.33 / 084 | 0.6 | 0.8 |
| DC_41_n3-n78 | 0.33 / 084 | 0.6 | 0.8 |
| DC_41_n28-n41 | 0.33 / 084 | 0.3 | 0.33 / 084 |
| DC_41_n28-n77 | 0.3 | 0.5 | 0.8 |
| DC_41_n28-n78 | 0.3 | 0.5 | 0.8 |
| DC_41_n41-n77 | 0.3 | 0.3 | 0.8 |
| DC_41_n41-n78 | 0.3 | 0.3 | 0.8 |
| DC_(n)41-n78 | 0.3 | 0.3 | 0.8 |
| DC_41-42_n77 | 0.5 | N/A | 0.8 |
| DC_41-42_n78 | 0.5 | N/A | 0.8 |
| DC_41-42_n79 | 0.3 | N/A | - |
| DC_42_n1-n3 | 0.8 | 0.3 | 0.6 |
| DC_42_n1-n77 | 0.8 | 0.6 | 0.8 |
| DC_42_n1-n78 | 0.8 | 0.3 | 0.8 |
| DC_42_n1-n79 | 0.8 | 0.3 | - |
| DC_42_n3-n28 | 0.8 | 0.6 | 0.8 |
| DC_42_n3-n77 | 0.8 | 0.6 | 0.8 |
| DC_42_n28-n77 | 0.5 | 0.8 | 0.8 |
| DC_46-48_n5 | N/A | 0.8 | 0.3 |
| DC_46-48_n66 | N/A | 0.8 | 0.6 |
| DC_46-66_n5DC_46-66-66_n5 | N/A | 0.3 | 0.3 |
| DC_46-66_n25 | N/A | 0.5 | 0.5 |
| DC_46-66_n77 DC_46-46-66_n77 | N/A | 0.6 | 0.8 |
| DC_48_(n)5 | 0.3 | 0.3 | 0.3 |
| DC_48_(n)12 | 0.3 | 0.3 | 0.3 |
| DC_48_n25-n48 | 0.8 | 0.6 | 0.8 |
| DC_48_n48-n66 | 0.8 | 0.8 | 0.6 |
| DC_48-66_n2 | 0.8 | 0.6 | 0.6 |
| DC_48-66_n12 | 0.8 | 0.6 | 0.3 |
| DC_48-66_n25 | 0.8 | 0.6 | 0.6 |
| DC_48-66_n48 | 0.8 | 0.6 | 0.6 |
| DC_48-66_n71 | 0.8 | 0.6 | 0.3 |
| DC_48-66_n5 | 0.8 | 0.6 | 0.3 |
| DC_48-66_n66 | 0.8 | 0.6 | 0.6 |
| DC_48-66_n77 | N/A | 0.6 | 0.8 |
| DC_66_n2-n7 | 0.5 | 0.5 | 0.5 |
| DC_66_n2-n38 | 0.5 | 0.5 | 0.9 |
| DC_66_n2-n41 | 0.5 | 0.5 | 0.81 / 1.32 |
| DC_66_n2-n66 | 0.5 | 0.5 | 0.5 |
| DC_66_n2-n71 | 0.5 | 0.5 | 0.3 |
| DC_66_n2-n77 | 0.6 | 0.6 | 0.8 |
| DC_66_n2-n78 | 0.6 | 0.6 | 0.8 |
| DC_66-(n)5DC_66-66-(n)5 | 0.3 | 0.3 | 0.3 |
| DC_66_n5-n48 | 0.6 | 0.3 | 0.8 |
| DC_66_n5-n77 | 0.6 | 0.3 | 0.8 |
| DC_66_n7-n12 | 0.5 | 0.5 | 0.5 |
| DC_66_n7-n25 | 0.5 | 0.5 | 0.5 |
| DC_66_n7-n66 | 0.5 | 0.5 | 0.5 |
| DC_66_n7-n71 | 0.5 | 0.5 | 0.5 |
| DC_66_n7-n77 | 0.6 | 0.5 | 0.8 |
| DC_66_n7-n78 | 0.6 | 0.5 | 0.8 |
| DC_66_(n)12 | 0.8 | 0.5 | 0.8 |
| DC_66_n12-n77 | 0.6 | 0.8 | 0.8 |
| DC_66_n12-n78 | 0.6 | 0.6 | 0.8 |
| DC_66_n25-n41 | 0.5 | 0.5 | 0.81 / 1.32 |
| DC_66_n25-n48 | 0.6 | 0.6 | 0.8 |
| DC_66_n25-n66 | 0.5 | 0.5 | 0.5 |
| DC_66_n25-n71 | 0.5 | 0.5 | 0.3 |
| DC_66_n38-n66 | 0.5 | 0.5 | 0.5 |
| DC_66_n38-n71 | 0.5 | 0.8 | 0.5 |
| DC_66_n38-n78 | 0.6 | 0.5 | 0.8 |
| DC_66_n41-n66 | 0.5 | 0.5 | 0.5 |
| DC_66_n41-n71 | 0.5 | 0.81 / 1.32 | 0.6 |
| DC_66_n41-n77 | 0.6 | 0.81 / 1.32 | 0.8 |
| DC_66_n41-n78 | 0.6 | 0.81 / 1.32 | 0.8 |
| DC_(n)66-n71DC_66_n66-n71 | 0.3 | 0.3 | 0.3 |
| DC_66_n66-n77 | 0.6 | 0.6 | 0.8 |
| DC_(n)66-n78DC_66_n66-n78 | 0.6 | 0.6 | 0.8 |
| DC_66-71_n2 | 0.5 | 0.3 | 0.5 |
| DC_66-71_n7 | 0.5 | 0.6 | 0.8 |
| DC_66-71_n12 | 0.3 | 0.5 | 0.5 |
| DC_66-71_n25 | 0.5 | 0.6 | 0.5 |
| DC_66_(n)71 | 0.3 | 0.3 | 0.3 |
| DC_66-71_n38 | 0.5 | 0.5 | 0.8 |
| DC_66-71_n41 | 0.5 | 0.6 | 0.81 / 1.32 |
| DC_66-71_n66 | 0.3 | 0.3 | 0.3 |
| DC_66-71_n77 | 0.6 | 0.6 | 0.8 |
| DC_66_n71-n77 | 0.6 | 0.6 | 0.8 |
| DC_66-71_n78 | 0.6 | 0.6 | 0.8 |
| DC_66_n71-n78 | 0.6 | 0.6 | 0.8 |
| DC_66_SUL_n78-n86 | 0.6 | 0.8 | 0.6 |
| DC_71_n2-n7 | 0.6 | 0.5 | 0.5 |
| DC_71_n2-n41 | 0.3 | 0.5 | 0.5 |
| DC_71_n2-n66 | 0.3 | 0.5 | 0.5 |
| DC_71_n2-n77 | 0.6 | 0.6 | 0.8 |
| DC_71_n2-n78 | 0.6 | 0.6 | 0.8 |
| DC_71_n7-n25 | 0.3 | 0.5 | 0.5 |
| DC_71_n7-n66 | 0.5 | 0.5 | 0.5 |
| DC_71_n7-n77 | 0.5 | 0.5 | 0.8 |
| DC_71_n25-n41 | 0.5 | 0.5 | 0.6 |
| DC_71_n25-n66 | 0.6 | 0.5 | 0.5 |
| DC_71_n25-n77 | 0.5 | 0.6 | 0.8 |
| DC_71_n38-n66 | 0.5 | 0.8 | 0.5 |
| DC_71_n38-n78 | 0.5 | 0.3 | 0.8 |
| DC_71_n41-n66 | 0.5 | 0.81 / 1.32 | 0.6 |
| DC_71_n66-n77 | 0.6 | 0.6 | 0.8 |
| DC_71_n66-n78 | 0.6 | 0.6 | 0.8 |
| NOTE 1: The requirement is applied for UE transmitting on the frequency range of 2545 - 2690 MHz.NOTE 2: The requirement is applied for UE transmitting on the frequency range of 2496 - 2545 MHz.NOTE 3: The requirement is applied for UE transmitting on the frequency range of 2515 – 2690 MHz.NOTE 4: The requirement is applied for UE transmitting on the frequency range of 2496 – 2515 MHz.NOTE 5: Only applicable for UE supporting inter-band carrier aggregation with uplink in one NR band and without simultaneous Rx/Tx.NOTE 6: “-” denotes ΔTIB,c = 0.NOTE 7: The component band order in the configuration should be listed by the order of E-UTRA band and NR band respectively, such as for DC_66_(n)12 the band order from left to right is 12, 66 and n12.NOTE 8:   The requirements only apply for UE supporting inter-band carrier aggregation with simultaneous Rx/Tx capability. |  |  |  |

###### 6.2B.4.2.3.3 ΔTIB,c for EN-DC four bands

Table 6.2B.4.2.3.3-1: ΔTIB,c due to EN-DC(four bands)

| Inter-band EN-DC configuration | ΔTIB,c for E-UTRA band / NR band (dB)12 |  |  |  |
| --- | --- | --- | --- | --- |
|  | Component band in order of bands in configuration13 |  |  |  |
| DC_1-(n)3-n8 | 0.3 | 0.3 | 0.3 | 0.3 |
| DC_1-3_n1-n41DC_1-3-3_n1-n41 | 0.5 | 0.5 | 0.5 | 0.34/0.85 |
| DC_1-3_n1-n78DC_1-3-3_n1-n78 | 0.5 | 0.5 | 0.5 | 0.8 |
| DC_1-3_n3-n41 | 0.5 | 0.5 | 0.5 | 0.34/0.85 |
| DC_1-3_n3-n77DC_1-(n)3-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3_n3-n78DC_1-(n)3-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3_n5-n40 | 0.6 | 0.6 | 0.6 | 0.9 |
| DC_1-3-5_n28 | 0.3 | 0.3 | 0.7 | 0.7 |
| DC_1-3-5_n40 | 0.6 | 0.6 | 0.6 | 0.9 |
| DC_1-3-5_n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-5_n78 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_1-3-5_n79 | 0.3 | 0.3 | 0.3 | - |
| DC_1-3-7_n3 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7_n1 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7_n5 | 0.6 | 0.6 | 0.6 | 0.3 |
| DC_1-3-7_n7DC_1-3-(n)7 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7_n8DC_1-3-3-7_n8DC_1-3-7-7_n8DC_1-3-3-7-7_n8 | 0.6 | 0.6 | 0.6 | 0.3 |
| DC_1-3-7_n26 | 0.6 | 0.6 | 0.6 | 0.3 |
| DC_1-3-7_n28DC_1-3-7-7_n28 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7_n38 | 0.6 | 0.6 | N/A | N/A |
| DC_1-3-7_n40DC_1-3-7-7_n40 | 0.6 | 0.6 | 0.8 | 0.9 |
| DC_1-3-7_n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-7_n78DC_1-3-3-7_n78DC_1-3-3-7-7_n78DC_1-3-7-7_n78DC_1-1-3-3-7_n78 | 0.7 | 0.7 | 0.7 | 0.8 |
| DC_1-3_n7-n78 | 0.7 | 0.7 | 0.7 | 0.8 |
| DC_1-3-7_n105 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-8_n1DC_1-3-3-8_n1 | 0.3 | 0.3 | 0.3 | 0.3 |
| DC_1-3-8_n7 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-8_n28 | 0.3 | 0.3 | 0.6 | 0.6 |
| DC_1-3-8_n40 | 0.6 | 0.6 | 0.6 | 0.9 |
| DC_1-3-8_n41DC_1-3-3-8_n41 | 0.5 | 0.5 | 0.3 | 0.34 / 0.85 |
| DC_1-3-8_n71 | 0.3 | 0.3 | 0.6 | 0.6 |
| DC_1-3-8_n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1_n3-n8-n77DC_1-3-3-8_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-8_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3_n8-n78DC_1-3-3_n8-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-8_n79 | 0.3 | 0.3 | 0.3 | - |
| DC_1-3-11_n28 | 0.3 | 0.8 | 0.9 | 0.6 |
| DC_1-3-11_n77 | 0.6 | 0.8 | 0.9 | 0.8 |
| DC_1-3-18_n3 | 0.3 | 0.3 | 0.3 | 0.3 |
| DC_1-3-18_n28 | 0.3 | 0.3 | 0.3 | 0.6 |
| DC_1-3-18_n41 | 0.3 | 0.3 | 0.3 | 0.34 |
| DC_1-3-28_n3 | 0.3 | 0.3 | 0.6 | 0.3 |
| DC_1-3-18_n77 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_1-3-18_n78 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_1-3-18_n79 | 0.3 | 0.3 | 0.3 | - |
| DC_1-3-19_n78 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_1-3-19_n79 | 0.3 | 0.3 | 0.3 | - |
| DC_1-3-20_n1DC_1-3-3-20_n1 | 0.3 | 0.3 | 0.3 | 0.3 |
| DC_1-3-20_n3 | 0.3 | 0.3 | 0.3 | 0.3 |
| DC_1-3-20_n7 | 0.3 | 0.5 | 0.3 | 0.5 |
| DC_1-3-20_n8 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-20_n28 | 0.3 | 0.3 | 0.6 | 0.6 |
| DC_1-3-20_n38 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_1-3-20_n41DC_1-3-3-20_n41 | 0.5 | 0.5 | 0.3 | 0.84 / 1.35 |
| DC_1-3-20_n78DC_1-1-3-20_n78DC_1-3-3-20_n78 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_1-3-21_n77 | 0.6 | 0.8 | 0.9 | 0.8 |
| DC_1-3-21_n78 | 0.6 | 0.8 | 0.9 | 0.8 |
| DC_1-3-21_n79 | 0.3 | 0.8 | 0.9 | - |
| DC_1-3-26_n78 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_1-3_n26-n78 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_1-3-28_n5 | 0.3 | 0.3 | 0.6 | 0.6 |
| DC_1-3-28_n7 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-28_n38 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-28_n40 | 0.5 | 0.5 | 0.6 | 0.5 |
| DC_1-3-28_n71 | 0.3 | 0.3 | 1.1 | 1.1 |
| DC_1-3_n28-n75 | 0.3 | 0.3 | 0.6 | N/A |
| DC_1-3-28_n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1_n3-n28-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-28_n78DC_1-3-3-28_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3_n28-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-28_n79 | 0.6 | 0.6 | 0.6 | - |
| DC_1_n3-n28-n79 | 0.6 | 0.6 | 0.6 | - |
| DC_1-3_n28-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3_n28-n79 | 0.3 | 0.3 | 0.6 | - |
| DC_1-3-32_n28 | 0.3 | 0.3 | N/A | 0.6 |
| DC_1-3-38_n28 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_1-3-32_n78 | 0.6 | 0.6 | - | 0.8 |
| DC_1-3-38_n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_1-3_n38-n78 | 0.5 | 0.6 | 0.6 | 0.8 |
| DC_1-3-40_n28 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_1-3_n40-n71 | 0.6 | 0.6 | 0.6 | 0.5 |
| DC_1-3_n40-n77 | 0.5 | 0.6 | 0.36 | 0.86 |
| DC_1-3_n40-n78 | 0.5 | 0.6 | 0.36 | 0.86 |
| DC_1-3-40_n78 | 0.6 | 0.6 | 0.39 | 0.89 |
| DC_1-3_n40-n105 | 0.6 | 0.6 | 0.6 | 0.5 |
| DC_1-3-41_n1DC_1-3-3-41_n1 | 0.5 | 0.5 | 0.34 / 0.85 | 0.5 |
| DC_1-3-41_n3 | 0.5 | 0.5 | 0.34 / 0.85 | 0.5 |
| DC_1-3-41_n28 | 0.5 | 0.5 | 0.34 / 0.85 | 0.6 |
| DC_1-3-41_n41DC_1-3-3-41_n41 | 0.5 | 0.5 | 0.34 / 0.85 | 0.34 / 0.85 |
| DC_1-3_(n)41 | 0.5 | 0.5 | 0.34 / 0.85 | 0.34 / 0.85 |
| DC_1-3-41_n77 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_1-3_n41-n77 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_1-3-41_n78DC_1-3-3-41_n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_1-3_n41-n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_1-3-41_n79 | 0.5 | 0.5 | 0.34 / 0.85 | - |
| DC_1-3-42_n28 | 0.6 | 0.6 | 0.8 | 0.8 |
| DC_1-3-42_n77 | 0.6 | 0.6 | N/A | 0.8 |
| DC_1-3-42_n78 | 0.6 | 0.6 | N/A | 0.8 |
| DC_1-3-42_n79 | 0.6 | 0.6 | N/A | - |
| DC_1-3_n71-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3_n75-n78 | 0.6 | 0.6 | N/A | 0.8 |
| DC_1-3_n77-n79 | 0.6 | 0.6 | 0.8 | - |
| DC_1_n3-n77-n79 | 0.6 | 0.6 | 0.8 | - |
| DC_1-3_n78-n79 | 0.6 | 0.6 | 0.8 | - |
| DC_1-3_n78-n105 | 0.6 | 0.6 | 0.8 | 0.6 |
| DC_1-3_SUL_n78-n80 | 0.6 | 0.6 | 0.8 | 0.6 |
| DC_1-5-7_n28DC_1-5-7-7_n28 | 0.5 | 0.7 | 0.6 | 0.7 |
| DC_1-5-7_n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-5-7_n78DC_1-5-7-7_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-5_n28-n78 | 0.3 | 0.6 | 0.6 | 0.9 |
| DC_1-5_n40-n77 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_1-5_n40-n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_1-5-41_n79 | 0.5 | 0.3 | 0.5 | - |
| DC_1-7_n3-n38 | 0.6 | 0.6 | 0.6 | 0.5 |
| DC_1-7_n3-n78 | 0.5 | 0.2 | 0.6 | 0.8 |
| DC_1-7_n5-n40 | 0.6 | 0.8 | 0.6 | 0.9 |
| DC_1-7_n7-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-7-8_n3 | 0.6 | 0.6 | 0.3 | 0.6 |
| DC_1-7-8_n7 | 0.5 | 0.6 | 0.6 | 0.6 |
| DC_1-7-8_n20 | 0.5 | 0.6 | 0.6 | 0.6 |
| DC_1-7-8_n28DC_1-7-7-8_n28 | 0.5 | 0.6 | 0.6 | 0.6 |
| DC_1-7-8_n78DC_1-7-7-8_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-7_n8-n78DC_1-7-7_n8-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-7-20_n3 | 0.3 | 0.5 | 0.3 | 0.5 |
| DC_1-7-20_n8 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-7-20_n28 | 0.5 | 0.6 | 0.6 | 0.6 |
| DC_1-7-20_n38 | 0.5 | N/A | 0.3 | N/A |
| DC_1-7-20_n78DC_1-1-7-20_n78DC_1-7-7-20_n78 | 0.6 | 0.7 | 0.4 | 0.8 |
| DC_1-7-26_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-7_n26-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-7-28_n3 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-7-28_n5 | 0.3 | 0.3 | 0.6 | 0.6 |
| DC_1-7-28_n7 | 0.5 | 0.6 | 0.6 | 0.6 |
| DC_1-7-28_n20 | 0.5 | 0.6 | 0.6 | 0.6 |
| DC_1-7-28_n38 | 0.5 | N/A | 0.6 | N/A |
| DC_1-7-28_n40 | 0.6 | 0.8 | 0.6 | 0.9 |
| DC_1-7-28_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-7_n28-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-7-32_n3 | 0.6 | 0.6 | N/A | 0.6 |
| DC_1-7-32_n8 | 0.7 | 0.7 | N/A | 0.6 |
| DC_1-7-32_n28 | 0.5 | 0.6 | N/A | 0.7 |
| DC_1-7_n40-n77DC_1-7-7_n40-n77 | 0.6 | 0.5 | 0.5 | 0.8 |
| DC_1-7_n40-n105 | 0.6 | 0.5 | 0.5 | 0.5 |
| DC_1-7-38_n3 | 0.6 | N/A | N/A | 0.6 |
| DC_1-7-38_n78 | 0.3 | N/A | N/A | 0.8 |
| DC_1-7-32_n78 | 0.6 | 0.6 | - | 0.8 |
| DC_1-7-38_n8 | 0.5 | N/A | N/A | 0.5 |
| DC_1-7-38_n28 | 0.3 | N/A | N/A | 0.6 |
| DC_1-7-40_n78 | 0.6 | 0.5 | 0.39 | 0.89 |
| DC_1-7_n40-n78DC_1-7-7_n40-n78 | 0.6 | 0.5 | 0.5 | 0.8 |
| DC_1-7_n75-n78 | 0.2 | 0.2 | N/A | 0.5 |
| DC_1-7_n78-n105 | 0.6 | 0.6 | 0.8 | 0.6 |
| DC_1-8_n1-n41 | 0.5 | 0.6 | 0.5 | 0.6 |
| DC_1-8_n1-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-8-(n)3 | 0.3 | 0.3 | 0.3 | 0.3 |
| DC_1-8_n3-n28 | 0.3 | 0.6 | 0.3 | 0.6 |
| DC_1-8_n3-n77 | 0.6 | 0.6 | 0.8 | 0.8 |
| DC_1-8_n3-n78 | 0.6 | 0.6 | 0.8 | 0.8 |
| DC_1-8_n3-n79 | 0.3 | 0.3 | 0.3 | 0.8 |
| DC_1-8_n7-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-8-11_n3 | 0.3 | 0.3 | 0.8 | 0.9 |
| DC_1-8-11_n28 | 0.3 | 0.6 | 0.4 | 0.6 |
| DC_1-8-11_n77 | 0.6 | 0.6 | 0.4 | 0.8 |
| DC_1-8-11_n78 | 0.3 | 0.6 | 0.4 | 0.8 |
| DC_1-8-11_n79 | 0.3 | 0.3 | 0.4 | - |
| DC_1-8-20_n3 | 0.3 | 0.4 | 0.4 | 0.3 |
| DC_1-8-20_n28 | 0.3 | 0.6 | 0.6 | 0.6 |
| DC_1-8-20_n78 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_1-8-28_n3 | 0.3 | 0.6 | 0.6 | 0.3 |
| DC_1-8-28_n40 | 0.3 | 0.6 | 0.6 | 0.5 |
| DC_1-8-28_n71 | 0.3 | 0.7 | 1.1 | 1.1 |
| DC_1-8-28_n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-8_n28-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-8-28_n78 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_1-8_n28-n78 | 0.3 | 0.6 | 0.5 | 0.8 |
| DC_1-8_n28-n79 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_1-8-32_n3 | 0.5 | 0.3 | N/A | 0.8 |
| DC_1-8-32_n78 | 0.5 | 0.6 | N/A | 0.8 |
| DC_1-8_n40-n77 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_1-8-38_n28 | 0.5 | 0.6 | 0.6 | 0.6 |
| DC_1-8-38_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-8-40_n28 | 0.5 | 0.6 | 0.6 | 0.6 |
| DC_1-8_n40-n71 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_1-8-40_n78 | 0.6 | 0.6 | 0.39 | 0.89 |
| DC_1-8-41_n1 | 0.6 | 0.3 | 0.6 | 0.6 |
| DC_1-8-41_n41 | 0.5 | 0.6 | 0.6 | 0.6 |
| DC_1-8-41_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-8_n41-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-8-42_n3 | 0.3 | 0.6 | 0.8 | 0.6 |
| DC_1-8-42_n28 | 0.3 | 0.6 | 0.8 | 0.8 |
| DC_1-8_n40-n78 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_1-8-42_n77 | 0.6 | 0.6 | N/A | 0.8 |
| DC_1-8_n71-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-8_n77-n79 | 0.6 | 0.6 | 0.8 | 0.5 |
| DC_1-11_n3-n28 | 0.3 | 0.8 | 0.9 | 0.6 |
| DC_1-11_n3-n77 | 0.6 | 0.8 | 0.9 | 0.8 |
| DC_1-11_n3-n79 | 0.3 | 0.8 | 0.9 | 0.8 |
| DC_1-11-18_n3 | 0.3 | 0.9 | 0.3 | 0.8 |
| DC_1-11-18_n28 | 0.3 | 0.4 | 0.4 | 0.6 |
| DC_1-11-18_n41 | 0.5 | 0.4 | 0.3 | 0.5 |
| DC_1-11-18_n77 | 0.6 | 0.4 | 0.3 | 0.8 |
| DC_1-11-18_n78 | 0.3 | 0.4 | 0.3 | 0.8 |
| DC_1-11_n77-n79 | 0.6 | 0.4 | 0.8 | - |
| DC_1-18_n3-n41 | 0.3 | 0.3 | 0.3 | 0.34 |
| DC_1-18_n3-n77 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_1-18_n3-n78 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_1-18_n28-n41 | 0.3 | 0.3 | 0.5 | 0.34 |
| DC_1-18-28_n77 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_1-18_n28-n77 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_1-18-28_n78 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_1-18_n28-n78 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_1-18-28_n79 | 0.3 | 0.5 | 0.5 | - |
| DC_1-18-41_n77 | 0.6 | 0.3 | 0.5 | 0.8 |
| DC_1-18_n41-n77 | 0.6 | 0.3 | 0.5 | 0.8 |
| DC_1-18-41_n78 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_1-18_n41-n78 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_1-18-42_n77 | 0.3 | 0.3 | N/A | 0.8 |
| DC_1-18-42_n78 | 0.3 | 0.3 | N/A | 0.8 |
| DC_1-18-42_n79 | 0.3 | 0.3 | N/A | - |
| DC_1-19-42_n77 | 0.6 | 0.3 | N/A | 0.8 |
| DC_1-19-42_n78 | 0.3 | 0.3 | N/A | 0.8 |
| DC_1-19-42_n79 | 0.3 | 0.3 | N/A | - |
| DC_1-19_n77-n79 | 0.3 | 0.3 | 0.8 | - |
| DC_1-19_n78-n79 | 0.3 | 0.3 | 0.8 | - |
| DC_1-20_n1-n41 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_1-20_n1-n78 | 0.3 | 0.3 | 0.3 | 0.8 |
| DC_1-20_n3-n38 | 0.5 | 0.3 | 0.3 | 0.5 |
| DC_1-20_n3-n78 | 0.3 | 0.6 | 0.3 | 0.8 |
| DC_1-20_n7-n78 | 0.5 | 0.3 | 0.3 | 0.8 |
| DC_1-20_n8-n78 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_1-20-28_n3 | 0.3 | 0.6 | 0.6 | 0.3 |
| DC_1-20_n28-n75 | 0.3 | 0.6 | 0.7 | N/A |
| DC_1-20-28_n78 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_1-20_n28-n78 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_1-20-32_n3 | 0.5 | 0.3 | N/A | 0.5 |
| DC_1-20-32_n28 | 0.3 | 0.6 | N/A | 0.7 |
| DC_1-20-32_n78 | 0.3 | 0.3 | N/A | 0.8 |
| DC_1-20-38_n3 | 0.3 | 0.3 | 0.3 | 0.3 |
| DC_1-20-38_n28 | 0.5 | 0.6 | 0.6 | 0.6 |
| DC_1-20-40_n28 | 0.5 | 0.6 | 0.6 | 0.6 |
| DC_1-20_(n)38 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_1-20-38_n8 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_1-20-38_n78 | 0.3 | 0.6 | - | 0.8 |
| DC_1-20-40_n78 | 0.5 | 0.3 | 0.59 | 0.89 |
| DC_1-20-41_n1 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_1-20-41_n41 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_1-20-41_n78 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_1-20_n41-n78 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_1-21-28_n77 | 0.6 | 0.4 | 0.6 | 0.8 |
| DC_1-21-28_n78 | 0.3 | 0.4 | 0.6 | 0.8 |
| DC_1-21-28_n79 | 0.3 | 0.4 | 0.6 | - |
| DC_1-21_n28-n77 | 0.3 | 0.4 | 0.6 | 0.8 |
| DC_1-21_n28-n78 | 0.6 | 0.4 | 0.6 | 0.8 |
| DC_1-21_n28-n79 | 0.3 | 0.4 | 0.6 | - |
| DC_1-21-42_n77 | 0.6 | 0.4 | N/A | 0.8 |
| DC_1-21-42_n78 | 0.3 | 0.4 | N/A | 0.8 |
| DC_1-21-42_n79 | 0.3 | 0.4 | N/A | - |
| DC_1-21_n77-n79 | 0.3 | 0.3 | 0.8 |  |
| DC_1-21_n78-n79 | 0.3 | 0.3 | 0.8 |  |
| DC_1-28_n3-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-28_n3-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-28_n5-n40 | 0.6 | 0.6 | 0.6 | 0.9 |
| DC_1-28-(n)7 | 0.5 | 0.6 | 0.6 | 0.6 |
| DC_1-28_n7-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-28-32_n3 | 0.5 | 0.6 | N/A | 0.5 |
| DC_1-28-32_n41 | 0.6 | 0.6 | N/A | 0.8 |
| DC_1-28_n40-n41 | 0.6 | 0.6 | 0.9 | 0.8 |
| DC_1-28_n40-n71 | 0.5 | 1.1 | 0.6 | 1.1 |
| DC_1-28_n40-n77 | 0.5 | 0.5 | 0.3 | 0.8 |
| DC_1-28-40_n78 | 0.5 | 0.5 | 0.36 | 0.86 |
| DC_1-28_n40-n78 | 0.5 | 0.5 | 0.36 | 0.86 |
| DC_1-28_n41-n77 | 0.5 | 0.5 | 0.3 | 0.8 |
| DC_1-28-42_n77 | 0.6 | 0.6 | N/A | 0.8 |
| DC_1-28-42_n78 | 0.3 | 0.6 | N/A | 0.8 |
| DC_1-28-42_n79 | 0.3 | 0.6 | N/A |  |
| DC_1-28_n71-n77 | 0.6 | 0.61.1 | 0.61.1 | 0.8 |
| DC_1_n28-n77-n79 | 0.6 | 0.6 | 0.8 | 0.5 |
| DC_1_n28-n78-n79 | 0.3 | 0.6 | 0.8 | 0.5 |
| DC_1-32_n28-n78 | 0.3 | N/A | 0.7 | 0.8 |
| DC_1-32_n40-n41 | 0.6 | N/A | 0.9 | 0.8 |
| DC_1-38_n3-n78 | 0.5 | 0.6 | 0.6 | 0.8 |
| DC_1-38_n7-n78 | 0.6 | 0.5 | 0.6 | 0.8 |
| DC_1-38_n28-n78 | 0.5 | 0.5 | 0.5 | 0.8 |
| DC_1_n40-n78-n105 | 0.5 | 0.5 | 0.8 | 0.5 |
| DC_1-41_n1-n41 | 0.5 | 0.34 / 0.85 | 0.5 | 0.34 / 0.85 |
| DC_1-41_n1-n78 | 0.5 | 0.34 / 0.85 | 0.5 | 0.8 |
| DC_1-41_n3-n41 | 0.5 | 0.34 / 0.85 | 0.5 | 0.34 / 0.85 |
| DC_1-41_n3-n77 | 0.6 | 0.34 / 0.85 | 0.6 | 0.8 |
| DC_1-41_n3-n78 | 0.6 | 0.34 / 0.85 | 0.6 | 0.8 |
| DC_1-41_n28-n41 | 0.5 | 0.34 / 0.85 | 0.5 | 0.34 / 0.85 |
| DC_1-41_n28-n77 | 0.6 | 0.5 | 0.5 | 0.8 |
| DC_1-41_n28-n78 | 0.5 | 0.5 | 0.5 | 0.8 |
| DC_1-41_n41-n77 | 0.5 | 0.5 | 0.5 | 0.8 |
| DC_1-41_n41-n78 | 0.5 | 0.5 | 0.5 | 0.8 |
| DC_1-41-42_n77 | 0.5 | 0.5 | N/A | 0.8 |
| DC_1-41-42_n78 | 0.5 | 0.5 | N/A | 0.8 |
| DC_1-41-42_n79 | 0.5 | 0.5 | N/A | - |
| DC_1-42_n3-n28 | 0.3 | 0.8 | 0.6 | 0.8 |
| DC_1-42_n3-n77 | 0.6 | N/A | 0.6 | 0.8 |
| DC_1-42_n77-n79 | 0.6 | N/A | 0.8 | - |
| DC_1-42_n28-n77 | 0.6 | N/A | 0.8 | 0.8 |
| DC_1-42_n78-n79 | 0.3 | N/A | 0.8 | - |
| DC_2-4-7_n28 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_2-4-7_n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_2-5_n2-n41 | 0.5 | 0.6 | 0.5 | 0.41 / 0.92 |
| DC_2-5_n2-n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-5_n2-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-5_n2-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-5_n5-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-5-7_n2 | 0.5 | 0.3 | 0.5 | 0.3 |
| DC_2-5-7_n7 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-5-7_n66  DC_2-2-5-7_n66DC_2-5-7-7_n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-5-7_n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-5-7_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-5_(n)12 | 0.3 | 0.8 | 0.4 | 0.4 |
| DC_2-12_(n)5 | - | 0.5 | 0.3 | 0.5 |
| DC_2-5-30_n2 | 0.5 | 0.3 | 0.3 | 0.5 |
| DC_2-5-30_n66 | 0.5 | 0.3 | 0.3 | 0.5 |
| DC_2-5-30_n77DC_2-2-5-30_n77 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_2-5_n41-n66 | 0.5 | 0.6 | 0.51 / 12 | 0.5 |
| DC_2-5_n41-n77 | 0.6 | 0.6 | 0.41 / 0.92 | 0.8 |
| DC_2-5_n41-n78 | 0.6 | 0.6 | 0.41 / 0.92 | 0.8 |
| DC_2-5-48_n12 | 0.6 | 0.8 | 0.8 | 0.4 |
| DC_2-5-48_n71 | 0.6 | 0.5 | 0.8 | 0.5 |
| DC_2-5-48_n77 | 0.6 | 0.6 | N/A | 0.8 |
| DC_2-5-66_n2 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-5-66_n5 | 0.5 | 0.3 | 0.5 | 0.3 |
| DC_2-5-66_n7 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-5-66_n12 | 0.3 | 0.5 | 0.5 | 0.3 |
| DC_2-5-66_n30DC_2-2-5-66_n30DC_2-5-66-66_n30 | 0.5 | 0.3 | 0.5 | 0.3 |
| DC_2-5-66_n41DC_2-2-5-66_n41 | 0.5 | 0.6 | 0.5 | 0.81 / 1.32 |
| DC_2-5-66_n48DC_2-5-66-66_n48 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_2-2-5-(n)66DC_2-5-66-(n)66DC_2-5-(n)66DC_2-5-66_n66DC_2-5-5-66_n66DC_2-5-66-66_n66DC_2-2-5-66-(n)66DC_2-2-5-66-66_n66DC_2-5-5-66-66_n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-5-66_n71 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-5-66_n77DC_2-2-5-66_n77DC_2-5-66-66_n77 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_2-5-66_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-5_n66-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-5_n66-n78 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_2-7_n2-n66 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-7_n2-n71 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_2-7_n2-n77 | 0.6 | 0.5 | 0.6 | 0.8 |
| DC_2-7_n2-n78 | 0.6 | 0.5 | 0.6 | 0.8 |
| DC_2-7-12_n2 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-7-12_n66 DC_2-2-7-12_n66 | 0.5 | 0.5 | 0.8 | 0.5 |
| DC_2-7-12_n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-7_n12-n77 | 0.6 | 0.5 | 0.3 | 0.8 |
| DC_2-7-12_n78 DC_2-2-7-12_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-7-13_n25 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-7-13_n66DC_2-7-7-13_n66DC_2-2-7-7-13_n66 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-7_n25-n66 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-7-28_n7 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-7-28_n66 | 0.5 | 0.5 | 0.6 | 0.5 |
| DC_2-7-28_n78 | 0.5 | 0.5 | 0.3 | 0.8 |
| DC_2-7-29_n78DC_2-7-7-29_n78 | 0.6 | 0.5 | N/A | 0.8 |
| DC_2-7_n38-n66DC_2-7-7_n38-n66 | 0.5 | N/A | N/A | 0.5 |
| DC_2-7-38_n78 | 0.6 | N/A | N/A | 0.8 |
| DC_2-7_n38-n78DC_2-7-7_n38-n78 | 0.6 | N/A | N/A | 0.8 |
| DC_2-7-66_n2 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-7-66_n7DC_2-7-66-66_n7 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-7-66_n12 | 0.5 | 0.5 | 0.5 | 0.8 |
| DC_2-7-66_n25 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-7-66_n28 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_2-7-66_n38DC_2-2-7-66_n38 | 0.5 | N/A | 0.5 | N/A |
| DC_2-7-(n)66DC_2-7-66_n66 DC_2-7-7-(n)66DC_2-7-7-66_n66DC_2-7-7-66-(n)66DC_2-7-66-(n)66 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-7-66_n71 DC_2-2-7-66_n71 | 0.5 | 0.5 | 0.5 | 0.3 |
| DC_2-7_n66-n71 | 0.5 | 0.5 | 0.5 | 0.3 |
| DC_2-7-66_n77 | 0.6 | 0.5 | 0.6 | 0.8 |
| DC_2-7-66_n78DC_2-7-7-66_n78DC_2-7-66-66_n78DC_2-7-7-66-66_n78DC_2-7_n66-n78DC_2-7-7_n66-n78 | 0.6 | 0.5 | 0.6 | 0.8 |
| DC_2-7_n66-n77 | 0.6 | 0.5 | 0.6 | 0.8 |
| DC_2-7-71_n2 | 0.5 | 0.5 | 0.6 | 0.5 |
| DC_2-7-71_n66 DC_2-2-7-71_n66 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-7-71_n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-7_n71-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-7-71_n78 DC_2-2-7 -71_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-7_n71-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-12_n2-n41 | 0.5 | 0.3 | 0.5 | 0.41 / 0.92 |
| DC_2-12_n2-n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-12_n2-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-12_n2-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-12-30_n2 | 0.5 | 0.3 | 0.3 | 0.5 |
| DC_2-12-30_n66 | 0.5 | 0.8 | 0.3 | 0.5 |
| DC_2-12-30_n77DC_2-2-12-30_n77 | 0.6 | 0.5 | 0.3 | 0.8 |
| DC_2-12_n41-n66 | 0.5 | 0.8 | 0.51 / 12 | 0.5 |
| DC_2-12-48_n5 | 0.6 | 0.4 | 0.8 | 0.8 |
| DC_2-12-66_n2 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-12-66_n5 | 0.5 | 0.8 | 0.5 | 0.8 |
| DC_2-12-66_n7 | 0.5 | 0.6 | 0.5 | 0.8 |
| DC_2-12-66_n30DC_2-2-12-66_n30DC_2-12-66-66_n30 | 0.5 | 0.8 | 0.5 | 0.3 |
| DC_2-2-12-(n)66DC_2-12-(n)66DC_2-12-66_n66 | 0.5 | 0.8 | 0.5 | 0.5 |
| DC_2-12-66_n77DC_2-2-12-66_n77DC_2-12-66-66_n77 | 0.6 | 0.8 | 0.6 | 0.8 |
| DC_2-12_n66-n77 | 0.6 | 0.8 | 0.6 | 0.8 |
| DC_2-12-66_n78 DC_2-2-12-66_n78 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_2-12_n66-n78 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_2-13_n25-n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-13-48_n77 | 0.6 | 0.5 | N/A | 0.8 |
| DC_2-13-66_n2 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-13-66_n5 | 0.5 | 0.3 | 0.5 | 0.3 |
| DC_2-13-66_n48 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_2-13-(n)66DC_2-2-13-(n)66DC_2-13-66_n66DC_2-13-66-(n)66DC_2-2-13-66-(n)66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-13-66_n77DC_2-2-13-66_n77DC_2-2-13-66-66_n77DC_2-13-66-66_n77 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_2-13_n66-n77 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_2-14-30_n2 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-14-30_n66 | 0.5 | 0.3 | 0.3 | 0.5 |
| DC_2-14-30_n77DC_2-2-14-30_n77 | 0.6 | 0.5 | 0.3 | 0.8 |
| DC_2-14-66_n2DC_2-14-66-66_n2 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-14-66_n30DC_2-2-14-66_n30DC_2-14-66-66_n30 | 0.5 | 0.3 | 0.5 | 0.3 |
| DC_2-14-66_n66DC_2-2-14-66_n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-14-66_n77DC_2-2-14-66_n77DC_2-14-66-66_n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-28-66_n7 | 0.5 | 0.6 | 0.5 | 0.5 |
| DC_2-28-66_n66 | 0.5 | 0.6 | 0.5 | 0.5 |
| DC_2-29-30_n2 | 0.5 | N/A | 0.3 | 0.5 |
| DC_2-29-30_n66 | 0.5 | N/A | 0.3 | 0.5 |
| DC_2-29-30_n77DC_2-2-29-30_n77 | 0.6 | N/A | 0.3 | 0.8 |
| DC_2-29-66_n2DC_2-29-66-66_n2 | 0.5 | N/A | 0.5 | 0.5 |
| DC_2-29-66_n30DC_2-2-29-66_n30DC_2-29-66-66_n30 | 0.5 | N/A | 0.5 | 0.3 |
| DC_2-29-(n)66DC_2-2-29-(n)66DC_2-29-66_n66 | 0.5 | N/A | 0.5 | 0.5 |
| DC_2-29-66_n77 | 0.6 | N/A | 0.6 | 0.8 |
| DC_2-29-66_n78 | 0.6 | N/A | 0.6 | 0.8 |
| DC_2-30-(n)5DC_2-2-30-(n)5 | 0.5 | 0.3 | 0.3 | 0.3 |
| DC_2-30-66_n2DC_2-30-66-66_n2 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-30-66_n5 | 0.5 | 0.3 | 0.5 | 0.3 |
| DC_2-30-66_n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-30-66_n77DC_2-2-30-66_n77DC_2-30-66-66_n77 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_2-46_n41-n66 | 0.5 | N/A | 0.5 | 0.5 |
| DC_2-46_n41-n71 | 0.5 | N/A | 0.5 | 0.6 |
| DC_2-46-48_n2 | 0.6 | N/A | 0.8 | 0.6 |
| DC_2-46-48_n5 | 0.6 | N/A | 0.8 | 0.3 |
| DC_2-46-48_n66 | 0.6 | N/A | 0.8 | 0.6 |
| DC_2-46-66_n5 | 0.5 | N/A | 0.5 | 0.3 |
| DC_2-46-66_n41 | 0.5 | N/A | 0.5 | 0.81 / 1.32 |
| DC_2-46-66_n71 | - | N/A | 0.3 | 0.3 |
| DC_2-48-66_n77 | 0.6 | N/A | 0.6 | 0.8 |
| DC_2-48_n48-n66 | 0.6 | 0.8 | 0.8 | 0.6 |
| DC_2-48_(n)5 | 0.6 | 0.3 | 0.8 | 0.3 |
| DC_2-46_n66_n71 | 0.5 | N/A | 0.5 | 0.3 |
| DC_2-48-66_n2 | 0.6 | 0.8 | 0.6 | 0.6 |
| DC_2-48-66_n5 | 0.6 | 0.8 | 0.6 | - |
| DC_2-48-66_n12 | 0.6 | 0.8 | 0.6 | 0.3 |
| DC_2-48-66_n66 | 0.6 | 0.8 | 0.6 | 0.6 |
| DC_2-48-66_n71 | 0.6 | 0.8 | 0.6 | 0.3 |
| DC_2-66_n2-n41 | 0.5 | 0.5 | 0.5 | 0.51 / 12 |
| DC_2-66_n2-n66 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-66_n2-n71 | 0.5 | 0.5 | 0.5 | 0.3 |
| DC_2-66_n2-n77DC_2-66-66_n2-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-66_n2-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-66_(n)5DC_2-2-66_(n)5DC_2-66-66_(n)5 | 0.5 | 0.3 | 0.5 | 0.3 |
| DC_2-66_n5-n77 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_2-66_n12-n77 | 0.6 | 0.6 | 0.8 | 0.8 |
| DC_2-66_n12-n78 | 0.6 | 0.6 | 0.8 | 0.8 |
| DC_2-66_n25-n66 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-66_n38-n78 | 0.6 | 0.6 | 0.9 | 0.8 |
| DC_2-66_n41-n66 | 0.5 | 0.5 | 0.81 / 1.32 | 0.5 |
| DC_2-66_n41-n71 | 0.5 | 0.5 | 0.81 / 1.32 | 0.8 |
| DC_2-66_n41-n77 | 0.6 | 0.6 | 0.81 / 1.32 | 0.8 |
| DC_2-66_n41-n78 | 0.5 | 0.5 | 0.81 / 1.32 | 0.8 |
| DC_2-66_n66-n71 | 0.5 | 0.5 | 0.5 | 0.3 |
| DC_2-66_n66-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-(n)66-n78DC_2-66_n66-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-66-71_n2 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-66-71_n38DC_2-2-66-71_n38 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-66-71_n41 DC_2-2-66-71_n41 | 0.5 | 0.5 | 0.8 | 0.81 / 1.32 |
| DC_2-66-71_n66 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-66-(n)71 | 0.5 | 0.5 | 0.3 | 0.3 |
| DC_2-66-71_n71 | 0.5 | 0.5 | 0.3 | 0.3 |
| DC_2-66-71_n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-66_n71-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-66-71_n78DC_2-2-66-71_n78 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-66_n71-n78 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-71_n2-n41 | 0.5 | 0.6 | 0.5 | 0.41 / 0.92 |
| DC_2-71_n2-n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-71_n2-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-71_n2-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-71_n41-n66 | 0.5 | 0.8 | 0.81 / 1.32 | 0.8 |
| DC_2-71_n66-n77 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_2-71_n66-n78 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_3_n1-n20-n78DC_3-3_n1-n20-n78 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_3_n1-n28-n75 | 0.3 | 0.3 | 0.7 | N/A |
| DC_3_n1-n75-n78 | 0.6 | 0.6 | N/A | 0.8 |
| DC_3_n1-n40-n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_3_n1-n77-n79 | 0.6 | 0.6 | 0.8 | 0.5 |
| DC_3_n1-n78-n79 | 0.6 | 0.3 | 0.8 | 0.5 |
| DC_3-5_n1-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-5-7_n1DC_3-5-7-7_n1 | 0.6 | 0.3 | 0.6 | 0.6 |
| DC_3-5-7_n28DC_3-5-7-7_n28 | 0.5 | 0.7 | 0.5 | 0.7 |
| DC_3-5-7_n40DC_3-5-7-7_n40 | 0.6 | 0.6 | 0.8 | 0.9 |
| DC_3-5-7_n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-5-7_n78DC_3-5-7-7_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-5_n28-n78 | 0.5 | 0.6 | 0.5 | 0.9 |
| DC_3-5_n40-n77 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_3-5_n40-n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_3_n5-n40-n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_3-5-41_n79 | 0.5 | 0.33 | 0.34 / 0.85 | - |
| DC_3-7_n1-n8 DC_3-3-7_n1-n8 DC_3-3-7-7_n1-n8 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_3-7_n1-n28 | 0.6 | 0.6 | 0.6 | 0.5 |
| DC_3-7_n1-n40 | 0.6 | 0.8 | 0.6 | 0.9 |
| DC_3-7_n1-n75 | 0.6 | 0.6 | 0.6 | N/A |
| DC_3-7_n1-n78 | 0.7 | 0.7 | 0.7 | 0.8 |
| DC_3-7_n3-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7_n5-n40 | 0.6 | 0.8 | 0.6 | 0.9 |
| DC_3-7_n7-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-8_n1DC_3-3-7-8_n1DC_3-7-7-8_n1DC_3-3-7-7-8_n1 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_3-7-8_n7 | 0.5 | 0.5 | 0.6 | 0.5 |
| DC_3-7-8_n28DC_3-7-7-8_n28 | 0.5 | 0.5 | 0.6 | 0.5 |
| DC_3-7-8_n40 | 0.5 | 0.5 | 0.6 | 0.6 |
| DC_3-7-8_n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-8_n78DC_3-3-7-8_n78DC_3-7-7-8_n78DC_3-3-7-7-8_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7_n8-n78DC_3-3-7_n8-n78 DC_3-7-7_n8-n78 DC_3-3-7-7_n8-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-20_n1 | 0.6 | 0.6 | 0.3 | 0.6 |
| DC_3-7-20_n3 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_3-7-20_n7 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_3-7-20_n8 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_3-7-20_n28 | 0.5 | 0.5 | 0.6 | 0.5 |
| DC_3-7-20_n38 | 0.5 | N/A | 0.3 | N/A |
| DC_3-7-20_n78DC_3-3-7-20_n78DC_3-7-7-20_n78 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_3-7-26_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7_n26-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-28_n1DC_3-7-7-28_n1 | 0.6 | 0.6 | 0.5 | 0.6 |
| DC_3-7-28_n3 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_3-7-28_n5 | 0.5 | 0.5 | 0.4 | 0.4 |
| DC_3-7-28_n7 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_3-7-28_n38 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_3-7-28_n40 | 0.6 | 0.8 | 0.3 | 0.9 |
| DC_3-7-28_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7_n28-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-32_n1 | 0.6 | 0.6 | N/A | 0.6 |
| DC_3-7-32_n28 | 0.5 | 0.5 | N/A | 0.3 |
| DC_3-7-32_n78 | 0.6 | 0.6 | N/A | 0.8 |
| DC_3-7-38_n28 | 0.3 | N/A | N/A | 0.3 |
| DC_3-7-38_n78 | 0.6 | N/A | N/A | 0.8 |
| DC_3-7-40_n1 | 0.6 | 0.8 | 0.9 | 0.6 |
| DC_3-7_n40-n77DC_3-7-7_n40-n77 | 0.6 | 0.5 | 0.5 | 0.8 |
| DC_3-7-40_n78 | 0.6 | 0.5 | 0.39 | 0.89 |
| DC_3-7_n40-n78DC_3-7-7_n40-n78 | 0.6 | 0.5 | 0.5 | 0.8 |
| DC_3-7_n40-n105 | 0.6 | 0.5 | 0.5 | 0.5 |
| DC_3-7_n75-n78 | 0.6 | 0.6 | N/A | 0.8 |
| DC_3-7_n78-n79DC_3-3-7_n78-n79DC_3-7-7_n78-n79DC_3-3-7-7_n78-n79 | 0.6 | 0.6 | 0.8 | 0.5 |
| DC_3-7_n78-n105 | 0.6 | 0.6 | 0.8 | 0.6 |
| DC_3-7_SUL_n78-n80 | 0.6 | 0.6 | 0.8 | 0.6 |
| DC_3-8_n1-n28 | 0.3 | 0.6 | 0.3 | 0.6 |
| DC_3-3-8_n1-n78 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_3-8_n7-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3_n1-n8-n78 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_3-8_n1-n41DC_3-3-8_n1-n41 | 0.6 | 0.3 | 0.5 | 0.34 / 0.85 |
| DC_3-8_n1-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-8_n1-n78DC_3-3-8_n1-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-8-11_n28 | 0.8 | 0.6 | 0.9 | 0.6 |
| DC_3-8-11_n77 | 0.8 | 0.6 | 0.9 | 0.8 |
| DC_3-8-20_n1 | 0.3 | 0.4 | 0.4 | 0.3 |
| DC_3-8-20_n28 | 0.3 | 0.6 | 0.5 | 0.5 |
| DC_3-8-20_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-8-28_n40 | 0.3 | 0.6 | 0.6 | 0.5 |
| DC_3-8-28_n71 | 0.3 | 0.7 | 1.1 | 1.1 |
| DC_3-8-28_n77 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_3-8_n28-n77 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_3-8-28_n1 | 0.3 | 0.6 | 0.6 | 0.3 |
| DC_3-8-28_n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_3-8_n28-n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_3-8-32_n1 | 0.5 | 0.3 | N/A | 0.8 |
| DC_3-8-32_n28 | 0.3 | 0.3 | N/A | 0.6 |
| DC_3-8-32_n78 | 0.8 | 0.6 | N/A | 0.8 |
| DC_3-8-38_n1 | 0.6 | 03 | 0.6 | 0.6 |
| DC_3-8-38_n28 | 0.5 | 0.6 | 0.5 | 0.5 |
| DC_3-8-38_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-8-40_n28 | 0.5 | 0.6 | 0.6 | 0.5 |
| DC_3-8-40_n1 | 0.5 | 0.5 | 0.6 | 0.5 |
| DC_3-8_n40-n71 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_3-8-40_n78 | 0.6 | 0.6 | 0.39 | 0.89 |
| DC_3-8_n40-n41 | 0.5 | 0.3 | 0.5 | 0.54/0.85 |
| DC_3-8_n40-n77 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_3-8_n40-n78 | 0.6 | 0.3 | 0.5 | 0.8 |
| DC_3-8_n40-n79 | 0.5 | 0.3 | 0.5 | - |
| DC_3-8-41_n1DC_3-3-8-41_n1 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_3-8-41_n41DC_3-3-8-41_n41 | 0.5 | 0.3 | 0.34 / 0.85 | 0.34 / 0.85 |
| DC_3-8-41_n78DC_3-3-8-41_n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-8_n41-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-8_n41-n79 | 0.6 | 0.3 | 0.34/0.85 | - |
| DC_3-8-42_n77 | 0.6 | 0.6 | N/A | 0.8 |
| DC_(n)3-n8-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-8_n71-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-8_n77-n79 | 0.6 | 0.6 | 0.8 | 0.5 |
| DC_3-8_SUL_n78-n80 | 0.6 | 0.6 | 0.8 | 0.6 |
| DC_3-11_n28-n77 | 0.8 | 0.9 | 0.6 | 0.8 |
| DC_3-18_n3-n41 | 0.6 | 0.3 | 0.6 | 0.34 / 0.85 |
| DC_3-18_n3-n77 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_3-18_n3-n78 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_3-18_n28-n41 | 0.6 | 0.3 | 0.5 | 0.34 / 0.85 |
| DC_3-18_n28-n77 | 0.6 | 0.3 | 0.5 | 0.8 |
| DC_3-18_n28-n78 | 0.6 | 0.3 | 0.5 | 0.8 |
| DC_3-18_n41-n77 | 0.6 | 0.3 | 0.5 | 0.8 |
| DC_3-18_n41-n78 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_3-18-42_n77 | 0.3 | 0.3 | N/A | 0.8 |
| DC_3-18-42_n78 | 0.3 | 0.3 | N/A | 0.8 |
| DC_3-18-42_n79 | 0.6 | 0.3 | N/A | - |
| DC_3-19_n1-n77 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_3-19_n1-n78 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_3-19_n1-n79 | 0.3 | 0.3 | 0.3 | - |
| DC_3-19-21_n77 | 0.8 | 0.3 | 0.9 | 0.8 |
| DC_3-19-21_n78 | 0.8 | 0.3 | 0.9 | 0.8 |
| DC_3-19-21_n79 | 0.8 | 0.3 | 0.9 | - |
| DC_3-19-42_n1 | 0.6 | 0.3 | 0.8 | - |
| DC_3-19-42_n77 | 0.6 | 0.3 | N/A | 0.8 |
| DC_3-19-42_n78 | 0.6 | 0.3 | N/A | 0.8 |
| DC_3-19-42_n79 | 0.6 | 0.3 | N/A | - |
| DC_3-19_n77-n79 | 0.6 | 0.3 | 0.8 | - |
| DC_3-19_n78-n79 | 0.6 | 0.3 | 0.8 | - |
| DC_3-20_n1-n7 | 0.6 | 0.3 | 0.6 | 0.6 |
| DC_3-20_n1-n28 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_3-20_n1-n41DC_3-3-20_n1-n41 | 0.6 | 0.3 | 0.6 | 0.34 / 0.85 |
| DC_3-20_n1-n75 | 0.5 | 0.3 | 0.5 | N/A |
| DC_3-20_n1-n78 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_3-20_n3-n67 | 0.3 | 0.5 | 0.3 | N/A |
| DC_3-20_n7-n28 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_3-20_n8-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-20-28_n1 | 0.3 | 0.6 | 0.6 | 0.3 |
| DC_3-20-28_n7 | 0.5 | 0.6 | 0.6 | 0.5 |
| DC_3-20_n28-n75 | 0.3 | 0.5 | 0.5 | N/A |
| DC_3-20-28_n78DC_3-3-20-28_n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_3-20_n28-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-20-32_n1 | 0.5 | 0.3 | N/A | 0.5 |
| DC_3-20-32_n7 | 0.7 | 0.3 | N/A | 0.7 |
| DC_3-20-32_n28 | 0.3 | 0.5 | N/A | 0.5 |
| DC_3-20-32_n78 | 0.5 | 0.3 | N/A | 0.8 |
| DC_3-20-38_n1 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_3-20-38_n28 | 0.5 | 0.6 | 0.5 | 0.5 |
| DC_3-20-38_n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_3-20_n38-n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_3-20-40_n78 | 0.6 | 0.5 | 0.36 | 0.86 |
| DC_3-20-40_n1 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_3-20-40_n28 | 0.5 | 0.6 | 0.5 | 0.5 |
| DC_3-20-41_n1DC_3-3-20-41_n1 | 0.6 | 0.3 | 0.6 | 0.6 |
| DC_3-20-41_n41DC_3-3-20-41_n41 | 0.5 | 0.3 | 0.34 / 0.85 | 0.34 / 0.85 |
| DC_3-20-41_n78DC_3-3-20-41_n78DC_3-20_n41-n78 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_3-20-67_n3 | 0.3 | 0.5 | N/A | 0.3 |
| DC_3_20_SUL_n78-n80 | 0.5 | 0.3 | 0.8 | 0.5 |
| DC_3-21_n1-n77 | 0.8 | 0.9 | 0.6 | 0.8 |
| DC_3-21_n1-n78 | 0.8 | 0.9 | 0.6 | 0.8 |
| DC_3-21_n1-n79 | 0.8 | 0.9 | 0.3 | - |
| DC_3-21_n28-n77 | 0.8 | 0.9 | 0.5 | 0.8 |
| DC_3-21_n28-n78 | 0.8 | 0.9 | 0.5 | 0.8 |
| DC_3-21_n28-n79 | 0.8 | 0.9 | 0.3 | - |
| DC_3-21-42_n1 | 0.8 | 0.9 | 0.8 | 0.6 |
| DC_3-21-42_n77 | 0.8 | 0.9 | N/A | 0.8 |
| DC_3-21-42_n78 | 0.8 | 0.9 | N/A | 0.8 |
| DC_3-21-42_n79 | 0.8 | 0.9 | N/A | - |
| DC_3-21_n77-n79 | 0.8 | 0.9 | 0.8 | - |
| DC_3-21_n78-n79 | 0.8 | 0.9 | 0.8 | - |
| DC_3-28_n1-n40 | 0.5 | 0.6 | 0.5 | 0.5 |
| DC_3-28_n1-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-28_n3-n78 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_3-28_n5-n40 | 0.6 | 0.6 | 0.6 | 0.9 |
| DC_3-28-(n)7 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_3-28_n7-n78DC_3-3-28_n7-n78 | 1.0 | 0.5 | 0.8 | 0.8 |
| DC_3-28-32_n1 | 0.3 | 0.6 | N/A | 0.3 |
| DC_3-28-38_n1 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_3-28-40_n1 | 0.5 | 0.6 | 0.5 | 0.5 |
| DC_3-28_n40-n71 | 0.5 | 1.1 | 0.6 | 1.1 |
| DC_3-28_n40-n77 | 0.6 | 0.5 | 0.3 | 0.8 |
| DC_3-28-40_n78 | 0.6 | 0.5 | 0.36 | 0.86 |
| DC_3-28_n40-n78 | 0.6 | 0.5 | 0.36 | 0.86 |
| DC_3-28_n41-n77 | 1.0 | 0.5 | 0.34 / 0.85 | 0.8 |
| DC_3-28-41_n78 | 1.0 | 0.5 | 0.34 / 0.85 | 0.8 |
| DC_3-28-42_n77 | 0.6 | 0.5 | N/A | 0.8 |
| DC_3-28-42_n78 | 0.6 | 0.5 | N/A | 0.8 |
| DC_3-28-42_n79 | 0.6 | 0.5 | N/A | - |
| DC_3-28_n71-n77 | 0.6 | 1.1 | 1.1 | 0.8 |
| DC_3_n28-n77-n79 | 0.6 | 0.5 | 0.8 | 0.5 |
| DC_3_n28-n78-n79 | 0.6 | 0.5 | 0.8 | 0.5 |
| DC_3-28_n78-n105 | 0.6 | 1 | 0.8 | 1 |
| DC_3-32_n1-n28 | 0.3 | N/A | 0.3 | 0.6 |
| DC_3-32_n1-n78 | 0.6 | N/A | 0.6 | 0.8 |
| DC_3-32_n28-n78 | 0.6 | NA | 0.3 | 0.8 |
| DC_3-32-38_n28 | 0.7 | N/A | 0.7 | 0.6 |
| DC_3-38_n7-n78 | 0.6 | N/A | N/A | 0.8 |
| DC_3-38_n28-n78 | 1.0 | 0.3 | 0.5 | 0.8 |
| DC_3-38-40_n1 | 0.6 | 0.8 | 0.9 | 0.6 |
| DC_3-38-40_n28 | 0.6 | 0.8 | 0.9 | 0.3 |
| DC_3-40_n1-n78 | 0.6 | 0.36 | 0.5 | 0.86 |
| DC_3_n40-n41-n79 | 0.5 | 0.5 | 0.54/0.85 | 0.8 |
| DC_3_n40-n78-n105 | 0.5 | 0.5 | 0.8 | 0.5 |
| DC_3-41_n1-n41DC_3-3-41_n1-n41 | 0.5 | 0.34 / 0.85 | 0.5 | 0.34 / 0.85 |
| DC_3-41_n1-n78DC_3-3-41_n1-n78 | 0.6 | 0.5 | 0.6 | 0.8 |
| DC_3-41_n3-n41 | 0.5 | 0.34 / 0.85 | 0.5 | 0.34 / 0.85 |
| DC_3-41_n3-n77 | 0.6 | 0.34 / 0.85 | 0.6 | 0.8 |
| DC_3-41_n3-n78 | 0.6 | 0.34 / 0.85 | 0.6 | 0.8 |
| DC_3-41_n28-n41 | 0.6 | 0.34 / 0.85 | 0.5 | 0.34 / 0.85 |
| DC_3-41_n28-n77 | 0.6 | 0.34 / 0.85 | 0.5 | 0.8 |
| DC_3-41_n28-n78 | 1.0 | 0.34 / 0.85 | 0.5 | 0.8 |
| DC_3-41_n41-n77 | 0.6 | 0.34 / 0.85 | 0.34 / 0.85 | 0.8 |
| DC_3-41_n41-n78 | 0.6 | 0.34 / 0.85 | 0.34 / 0.85 | 0.8 |
| DC_3-41-42_n77 | 1.0 | 0.34 / 0.85 | N/A | 0.8 |
| DC_3-41-42_n78 | 1.0 | 0.34 / 0.85 | N/A | 0.8 |
| DC_3-41-42_n79 | 1.0 | 0.34 / 0.85 | N/A | - |
| DC_3-42_n1-n77 | 0.6 | N/A | 0.6 | 0.8 |
| DC_3-42_n1-n78 | 0.6 | N/A | 0.6 | 0.8 |
| DC_3-42_n1-n79 | 0.6 | 0.8 | 0.6 | - |
| DC_3-42_n28-n77 | 0.6 | N/A | 0.8 | 0.8 |
| DC_3-42_n77-n79 | 0.6 | N/A | 0.8 | - |
| DC_3-42_n78-n79 | 0.6 | N/A | 0.8 | - |
| DC_5-7_n1-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_5-7_n2-n66 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_5-7_n2-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_5-7_n2-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_5-7_n28-n78 | 0.6 | 0.6 | 0.5 | 0.9 |
| DC_5-7_n40-n77DC_5-7-7_n40-n77 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_5-7_n40-n78DC_5-7-7_n40-n78 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_5-7-66_n2 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_5-7-66_n7DC_5-7-66-66_n7 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_5-7-(n)66DC_5-7-7-(n)66DC_5-7-66_n66 DC_5-7-7-66_n66 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_5-7-66_n77 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_5-7_n66-n77 | 0.5 | 0.8 | 1.0 | 0.8 |
| DC_5-7_n66-n78 | 0.5 | 0.8 | 1.0 | 0.8 |
| DC_5-7-66_n78 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_5-30-66_n2 | 0.3 | 0.3 | 0.5 | 0.5 |
| DC_5-30-66_n66 | 0.3 | 0.3 | 0.5 | 0.5 |
| DC_5-30-66_n77DC_5-30-66-66_n77 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_5-48_(n)12 | 0.8 | 0.4 | 0.3 | 0.8 |
| DC_5-48-66_n12 | 0.8 | 0.8 | 0.6 | 0.4 |
| DC_5-48-66_n71 | 0.5 | 0.8 | 0.6 | 0.5 |
| DC_5-48-66_n77 | 0.6 | N/A | 0.6 | 0.8 |
| DC_5-66_n2-n41 | 0.6 | 0.5 | 0.5 | 0.81 / 1.32 |
| DC_5-66_n2-n66 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_5-66_n2-n77DC_5-66-66_n2-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_5-66_n2-n78 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_5-66_n5-n77DC_5-66-66_n5-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_5-66_(n)12 | 0.3 | 0.8 | 0.8 | 0.8 |
| DC_5-66_n41-n66 | 0.6 | 0.5 | 0.81 / 1.32 | 0.5 |
| DC_5-66_n41-n77 | 0.6 | 0.6 | 0.81 / 1.32 | 0.8 |
| DC_5-66_n41-n78 | 0.6 | 0.6 | 0.81 / 1.32 | 0.8 |
| DC_5-66_n66-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_7_n1-n40-n78 | 0.3 | 0.2 | 0.8 | 0.5 |
| DC_7_n1-n40-n78 | 0.8 | 0.6 | 0.9 | 0.8 |
| DC_7_n1-n75-n78 | 0.6 | 0.6 | - | 0.8 |
| DC_7-8_n1-n40 | 0.8 | 0.6 | 0.6 | 0.9 |
| DC_7-8_n1-n78DC_7-7-8_n1-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_7-8_n7-n78 | 0.5 | 0.6 | 0.5 | 0.8 |
| DC_7-8-20_n1 | 0.6 | 0.6 | 0.6 | 0.5 |
| DC_7-8-20_n3 | 0.5 | 0.6 | 0.4 | 0.5 |
| DC_7-8_n28-n78 | 0.5 | 0.6 | 0.5 | 0.8 |
| DC_7-8-32_n1 | 0.7 | 0.6 | N/A | 0.7 |
| DC_7-8-32_n78 | 0.7 | 0.6 | N/A | 0.8 |
| DC_7-8-38_n1 | N/A | 0.5 | N/A | 0.5 |
| DC_7-8-40_n1 | 0.8 | 0.6 | 0.9 | 0.6 |
| DC_7-8-40_n78 | 0.5 | 0.6 | 0.39 | 0.89 |
| DC_7-8_n40-n78 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_7-12_n2-n66 | 0.5 | 0.8 | 0.5 | 0.5 |
| DC_7-12_n2-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_7-12_n2-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_7-12-66_n2 | 0.5 | 0.8 | 0.5 | 0.5 |
| DC_7-12-66_n25 | 0.5 | 0.8 | 0.5 | 0.5 |
| DC_7-12-66_n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_7-12-66_n77 | 0.8 | 0.5 | 1.0 | 0.8 |
| DC_7-12_n66-n77 | 0.8 | 0.5 | 1.0 | 0.8 |
| DC_7-12-66_n78 | 0.8 | 0.5 | 1.0 | 0.8 |
| DC_7-12_n66-n78 | 0.8 | 0.5 | 1.0 | 0.8 |
| DC_7-12-71_n77 | 0.5 | 0.5 | 0.8 | 0.8 |
| DC_7-13_n25-n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_7-7-13-(n)66DC_7-13-(n)66DC_7-13-66_n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_7-20_n1-n75 | 0.7 | 0.3 | 0.7 | N/A |
| DC_7-20_n1-n78 | 0.7 | 0.4 | 0.6 | 0.8 |
| DC_7-20_n3-n38 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_7-20_n3-n78 | 0.5 | 0.6 | 0.5 | 0.8 |
| DC_7-20_n8-n78 | 0.5 | 0.6 | 0.6 | 0.8 |
| DC_7-20-28_n1 | 0.6 | 0.6 | 0.6 | 0.5 |
| DC_7-20-28_n3 | 0.5 | 0.6 | 0.5 | 0.5 |
| DC_7-20-28_n78 | 0.3 | 0.6 | 0.5 | 0.8 |
| DC_7-20_n28-n78 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_7-20-32_n1 | 0.6 | 0.3 | N/A | 0.5 |
| DC_7-20-32_n3 | 0.7 | 0.3 | N/A | 0.3 |
| DC_7-20-32_n8 | 0.7 | 0.6 | N/A | 0.6 |
| DC_7-20-32_n28 | 0.3 | 0.5 | N/A | 0.7 |
| DC_7-20-32_n78 | 0.7 | 0.5 | N/A | 0.8 |
| DC_7-20-38_n1 | N/A | 0.3 | N/A | 0.5 |
| DC_7-20-38_n3 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_7-20-38_n8 | N/A | 0.6 | N/A | 0.6 |
| DC_7-20-38_n78 | N/A | 0.6 | N/A | 0.8 |
| DC_7-28_n1-n40 | 0.3 | 0.2 | - | 0.8 |
| DC_7-28_n1-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_7-28_n3-n78 | 0.8 | 0.5 | 1.0 | 0.8 |
| DC_7-28_n5-n40 | 0.8 | 0.6 | 0.6 | 0.9 |
| DC_7-28_n7-n78 | 0.3 | 0.3 | 0.3 | 0.8 |
| DC_7-28-66_n7 | 0.5 | 0.6 | 0.5 | 0.5 |
| DC_7-28-66_n66 | 0.5 | 0.6 | 0.5 | 0.5 |
| DC_7-28-32_n1 | 0.7 | 0.6 | N/A | 0.7 |
| DC_7-28-32_n3 | 0.7 | 0.3 | N/A | 0.7 |
| DC_7-28-38_n1 | N/A | 0.6 | N/A | 0.5 |
| DC_7-28-38_n78 | N/A | 0.3 | N/A | 0.8 |
| DC_7-28_n38-n78 | N/A | 0.3 | N/A | 0.8 |
| DC_7-28_n40-n78 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_7-29-66_n78 | 0.5 | N/A | 0.6 | 0.8 |
| DC_7-32_n1-n28 | 0.6 | N/A | 0.5 | 0.6 |
| DC_7-32_n1-n78 | 0.2 | - | 0.2 | 0.5 |
| DC_7-32_n28-n78 | 0.3 | N/A | 0.7 | 0.8 |
| DC_7-38_n3-n78 | N/A | N/A | 0.6 | 0.8 |
| DC_7-40_n1-n78 | 0.5 | 0.56 | 0.6 | 0.86 |
| DC_7_n40-n78-n105 | 0.5 | 0.5 | 0.8 | 0.5 |
| DC_7-66_n2-n66 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_7-66_n2-n71 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_7-66_n2-n77 | 0.5 | 0.6 | 0.6 | 0.8 |
| DC_7-66_n2-n78 | 0.5 | 0.6 | 0.6 | 0.8 |
| DC_7-66_n12-n77 | 0.8 | 1.0 | 0.5 | 0.8 |
| DC_7-66_n12-n78 | 0.8 | 1.0 | 0.5 | 0.8 |
| DC_7-66_n25-n66 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_7-66_n38-n78DC_7-7-66_n38-n78 | N/A | 0.6 | N/A | 0.8 |
| DC_7-66_n66-n71 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_7-66-71_n25 | 0.5 | 0.5 | 0.6 | 0.5 |
| DC_7-66_n66-n77 | 0.5 | 0.6 | 0.6 | 0.8 |
| DC_7-(n)66-n78DC_7-7-(n)66-n78DC_7-66_n66-n78DC_7-7-66_n66-n78 | 0.5 | 0.6 | 0.6 | 0.8 |
| DC_7-66-71_n2 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_7-66-71_n77 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_7-66_n71-n77 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_7-66-71_n78 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_7-66_n71-n78 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_7-71_n2-n66 | 0.6 | 0.6 | 0.6 | 0.5 |
| DC_7-71_n2-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_7-71_n2-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_7-71_n66-n77 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_7-71_n66-n78 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_8_n1-n3-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_8-(n)3-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_8-(n)3-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_8_n3-n28-n77 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_8_n3-n28-n79 | 0.6 | 0.5 | 0.3 | 0.8 |
| DC_8_n3-n77-n79 | 0.6 | 0.6 | 0.8 | 0.8 |
| DC_8-11_n1-n3 | 0.3 | 0.8 | 0.3 | 0.9 |
| DC_8-11_n1-n77 | 0.6 | 0.4 | 0.6 | 0.8 |
| DC_8-11_n3-n28 | 0.6 | 0.8 | 0.9 | 0.6 |
| DC_8-11_n3-n77 | 0.6 | 0.8 | 0.9 | 0.8 |
| DC_8-11_n3-n79 | 0.3 | 0.8 | 0.9 | 0.8 |
| DC_8-11_n28-n77 | 0.6 | 0.4 | 0.6 | 0.8 |
| DC_8-11_n77-n79 | 0.6 | 0.4 | 0.8 | 0.5 |
| DC_8-20_n1-n78 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_8-20-28_n1 | 0.6 | 0.6 | 0.6 | 0.3 |
| DC_8-20-28_n3 | 0.6 | 0.5 | 0.5 | 0.3 |
| DC_8-20-28_n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_8-20-32_n1 | 0.4 | 0.4 | N/A | 0.5 |
| DC_8-20-32_n3 | 0.4 | 0.5 | N/A | 0.3 |
| DC_8-20-38_n1 | 0.6 | 0.5 | 0.5 | 0.5 |
| DC_8-20-38_n28 | 0.6 | 0.5 | 0.3 | 0.5 |
| DC_8-20-38_n78 | 0.6 | 0.5 | 0.3 | 0.8 |
| DC_8-20-40_n1 | 0.6 | 0.5 | 0.5 | 0.5 |
| DC_8-20-40_n28 | 0.6 | 0.5 | 0.3 | 0.5 |
| DC_8-20-40_n78 | 0.6 | 0.5 | 0.3 | 0.8 |
| DC_8-28-38_n1 | 0.6 | 0.5 | 0.5 | 0.5 |
| DC_8-28-40_n1 | 0.6 | 0.5 | 0.5 | 0.5 |
| DC_8-28_n40-n71 | 0.7 | 1.1 | 0.3 | 1.1 |
| DC_8-28_n40-n77 | 0.6 | 0.5 | 0.3 | 0.8 |
| DC_8-28_n71-n77 | 0.6 | 1.1 | 1.1 | 0.8 |
| DC_8_n28-n77-n79 | 0.6 | 0.5 | 0.8 | 0.8 |
| DC_8-32_n1-n78 | 0.6 | N/A | 0.5 | 0.8 |
| DC_8-32-38_n1 | 0.3 | N/A | 0.5 | 0.5 |
| DC_8-38-40_n28 | 0.6 | 0.5 | 0.3 | 0.5 |
| DC_8_n39-n40-n41 | 0.3 | 0.3 | 0.3 | 0.3 |
| DC_8_n39-n40-n79 | 0.3 | 0.3 | 0.3 | 0.8 |
| DC_8_n40-n41-n79 | 0.3 | 0.3 | 0.3 | - |
| DC_8-39_n40-n41 | 0.3 | 0.3 | 0.3 | 0.3 |
| DC_8-39_n40-n79 | 0.3 | 0.3 | 0.3 | 0.8 |
| DC_8-40_n1-n78 | 0.3 | 0.56 | 0.5 | 0.86 |
| DC_8-41_n1-n3 | 0.3 | 0.54 / 0.85 | 0.5 | 0.5 |
| DC_8-41_n1-n41 | 0.3 | 0.3 | 0.3 | 0.3 |
| DC_8-41_n1-n77 | 0.6 | 0.5 | 0.6 | 0.8 |
| DC_8-41_n1-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_8-41_n3-n77 | 0.6 | 0.310 / 0.811 | 0.6 | 0.8 |
| DC_8-42_n1-n3 | 0.6 | 0.8 | 0.3 | 0.6 |
| DC_8-42_n1-n77 | 0.6 | N/A | 0.6 | 0.8 |
| DC_8-42_n3-n28 | 0.6 | 0.8 | 0.6 | 0.8 |
| DC_8-42_n3-n77 | 0.6 | 0.8 | 0.6 | 0.8 |
| DC_8-42_n28-n77 | 0.6 | 0.8 | 0.8 | 0.8 |
| DC_11_n3-n28-n77 | 0.8 | 0.9 | 0.6 | 0.8 |
| DC_11_n3-n77-n79 | 0.8 | 0.9 | 0.8 | 0.8 |
| DC_12-30-66_n2 | 0.8 | 0.3 | 0.5 | 0.5 |
| DC_12-30-66_n66 | 0.8 | 0.3 | 0.5 | 0.5 |
| DC_12-30-66_n77DC_12-30-66-66_n77 | 0.8 | 0.3 | 0.6 | 0.8 |
| DC_12-48_(n)5 | 0.8 | 0.4 | 0.3 | 0.8 |
| DC_12-48-66_n5 | 0.8 | 0.8 | 0.8 | 0.3 |
| DC_12-66_(n)5 | 0.3 | 0.8 | 0.8 | 0.3 |
| DC_12-66_n2-n41 | 0.8 | 0.5 | 0.5 | 0.51 / 12 |
| DC_12-66_n2-n66 | 0.8 | 0.5 | 0.5 | 0.5 |
| DC_12-66_n2-n77 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_12-66_n2-n78 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_12-66_n66-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_13-48-66_n77 | 0.3 | N/A | 0.6 | 0.8 |
| DC_13-66_n2-n77 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_13-66_n5-n48 | 0.4 | 0.6 | 0.8 | 0.8 |
| DC_13-66_n5-n77DC_13-66-66_n5-n77 | 0.5 | 0.6 | 0.6 | 0.8 |
| DC_13-66_n66-n77 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_14-30-66-n2 | 0.3 | 0.3 | 0.5 | 0.5 |
| DC_14-30-66_n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_14-30-66_n77DC_14-30-66-66_n77 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_18-41_n3-n77 | 0.3 | 0.34 / 0.85 | 0.6 | 0.8 |
| DC_18-41_n3-n78 | 0.3 | 0.34 / 0.85 | 0.6 | 0.8 |
| DC_19_n1-n77-n79 | 0.3 | 0.6 | 0.8 | 0.5 |
| DC_19_n1-n78-n79 | 0.3 | 0.3 | 0.8 | 0.5 |
| DC_19-21_n1-n77 | 0.3 | 0.4 | 0.3 | 0.8 |
| DC_19-21_n1-n78 | 0.3 | 0.4 | 0.6 | 0.8 |
| DC_19-21_n1-n79 | 0.3 | 0.4 | 0.3 | - |
| DC_19-21-42_n1 | 0.3 | 0.4 | 0.8 | 0.3 |
| DC_19-21-42_n77 | 0.3 | 0.4 | N/A | 0.8 |
| DC_19-21-42_n78 | 0.3 | 0.4 | N/A | 0.8 |
| DC_19-21-42_n79 | 0.3 | 0.4 | N/A | - |
| DC_19-21_n77-n79 | 0.3 | 0.4 | 0.8 | - |
| DC_19-21_n78-n79 | 0.3 | 0.4 | 0.8 | - |
| DC_19-42_n1-n77 | 0.3 | N/A | 0.6 | 0.8 |
| DC_19-42_n1-n78 | 0.3 | N/A | 0.3 | 0.8 |
| DC_19-42_n1-n79 | 0.3 | 0.8 | 0.3 | - |
| DC_19-42_n77-n79 | 0.3 | N/A | 0.8 | - |
| DC_19-42_n78-n79 | 0.3 | N/A | 0.8 | - |
| DC_20-(n)3-n67 | 0.5 | 0.3 | 0.3 | N/A |
| DC_20-28-32_n1 | 0.6 | 0.6 | N/A | 0.5 |
| DC_20-28-32_n3 | 0.5 | 0.6 | N/A | 0.5 |
| DC_20-28-38_n1 | 0.6 | 0.6 | 0.5 | 0.5 |
| DC_20-28-40_n1 | 0.6 | 0.6 | 0.5 | 0.5 |
| DC_20-28-40_n78 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_20-32_n1-n28 | 0.6 | N/A | 0.3 | 0.7 |
| DC_20-32_n1-n78 | 0.6 | N/A | 0.3 | 0.8 |
| DC_20-32-38_n1 | 0.3 | N/A | 0.5 | 0.5 |
| DC_20-38_n3-n78 | 0.6 | 0.5 | 0.6 | 0.8 |
| DC_20-38-40_n1 | 0.6 | 0.5 | 0.5 | 0.5 |
| DC_20-38-40_n28 | 0.6 | 0.5 | 0.5 | 0.5 |
| DC_20-41_n1-n41 | 0.3 | 0.3 | 0.5 | 0.5 |
| DC_20-41_n1-n78 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_20-67-(n)3 | 0.5 | 0.3 | N/A | 0.3 |
| DC_21_n1-n77-n79 | 0.4 | 0.6 | 0.8 | 0.5 |
| DC_21_n1-n78-n79 | 0.4 | 0.6 | 0.8 | 0.5 |
| DC_21-28-42_n77 | 0.4 | 0.5 | N/A | 0.8 |
| DC_21-28-42_n78 | 0.4 | 0.5 | N/A | 0.8 |
| DC_21-28-42_n79 | 0.4 | 0.5 | N/A | - |
| DC_21_n28-n77-n79 | 0.4 | 0.5 | 0.8 | 0.5 |
| DC_21_n28-n78-n79 | 0.4 | 0.5 | 0.8 | - |
| DC_21-42_n1-n77 | 0.4 | N/A | 0.6 | 0.8 |
| DC_21-42_n1-n78 | 0.4 | N/A | 0.3 | 0.8 |
| DC_21-42_n1-n79 | 0.4 | 0.8 | 0.3 | - |
| DC_21-42_n77-n79 | 0.4 | N/A | 0.8 | - |
| DC_21-42_n78-n79 | 0.4 | N/A | 0.8 | - |
| DC_28_n1-n40-n78 | 0.2 | 0.2 | 0.8 | 0.5 |
| DC_28_n5-n40-n78 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_28-32-38_n1 | 0.7 | N/A | 0.5 | 0.5 |
| DC_28-32_n40-n41 | 0.6 | N/A | 0.9 | 0.8 |
| DC_28-41-42_n78 | 0.5 | 0.3 | N/A | 0.8 |
| DC_29-30-66_n2DC_29-30-66-66_n2 | N/A | 0.3 | 0.5 | 0.5 |
| DC_29-30-66_n66 | N/A | 0.3 | 0.5 | 0.5 |
| DC_29-30-66_n77 | N/A | 0.3 | 0.6 | 0.8 |
| DC_30-66-(n)5 | 0.3 | 0.3 | 0.5 | 0.3 |
| DC_42_n1-n77-n79 | 0.8 | 0.6 | 0.8 | - |
| DC_42_n1-n78-n79 | 0.8 | 0.3 | 0.8 | - |
| DC_42_n3-n28-n77 | 0.8 | 0.6 | 0.8 | 0.8 |
| DC_46-66_n25-n41 | N/A | 0.5 | 0.5 | 0.41 / 0.92 |
| DC_46-66_n25-n71 | N/A | 0.5 | 0.5 | 0.3 |
| DC_46-66_n41-n71 | N/A | 0.5 | 0.41 / 0.92 | 0.6 |
| DC_48-66_n25-n48 | 0.8 | 0.6 | 0.6 | 0.8 |
| DC_66-71_n2-n41 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_66-71_n2-n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_66-71_n2-n77 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_66-71_n2-n78 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_66-71_n66-n77 | 0.6 | 0.6 | 0.6 | 0.8 |
| NOTE 1: The requirement is applied for UE transmitting on the frequency range of 2545 - 2690 MHz.NOTE 2: The requirement is applied for UE transmitting on the frequency range of 2496 - 2545 MHz.NOTE 3: The values in the table reflect what can be achieved with the present state of the art technology. They shall be reconsidered when the state of the art technology progresses.NOTE 4: The requirement is applied for UE transmitting on the frequency range of 2515 – 2690 MHz.NOTE 5: The requirement is applied for UE transmitting on the frequency range of 2496 – 2515 MHz.NOTE 6: Only applicable for UE supporting inter-band carrier aggregation with uplink in one E-UTRA band and without simultaneous Rx/Tx.NOTE 7: Void.NOTE 8: Void.NOTE 9: Only applicable for UE supporting inter-band carrier aggregation with uplink in one NR band and without simultaneous Rx/TxNOTE 10: The requirement is applied for UE transmitting on the frequency range of 2515 - 2690 MHz.NOTE 11: The requirement is applied for UE transmitting on the frequency range of 2496 – 2515 MHz.NOTE 12: “-” denotes ΔTIB,c = 0.NOTE 13: The component band order in the configuration should be listed by the order of E-UTRA band and NR band respectively, such as for DC_30-66-(n)5 the band order from left to right is 5, 30, 66 and n5. |  |  |  |  |

###### 6.2B.4.2.3.4 ΔTIB,c for EN-DC five bands

Table 6.2B.4.2.3.4-1: ΔTIB,c due to EN-DC (five bands)

| Inter-band EN-DC configuration | ΔTIB,c for E-UTRA band / NR band (dB)6 |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Component band in order of bands in configuration7 |  |  |  |  |
| DC_1-3-5-7_n28DC_1-3-5-7-7_n28 | 0.5 | 0.5 | 0.7 | 0.6 | 0.7 |
| DC_1-3-5-7_n40DC_1-3-5-7-7_n40 | 0.6 | 0.6 | 0.6 | 0.8 | 0.9 |
| DC_1-3-5-7_n77 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-5-7_n78DC_1-3-5-7-7_n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-5_n28-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.9 |
| DC_1-3-5_n40-n77 | 0.6 | 0.6 | 0.6 | 0.35 | 0.85 |
| DC_1-3-5_n40-n78 | 0.6 | 0.6 | 0.6 | 0.35 | 0.85 |
| DC_1-3-5-41_n79 | 0.5 | 0.5 | 0.3 | 0.53 / 0.84 | - |
| DC_1-3-7_n3-n78 | 0.7 | 0.7 | 0.7 | 0.7 | 0.8 |
| DC_1-3-7_n5-n40 | 0.6 | 0.6 | 0.8 | 0.6 | 0.9 |
| DC_1-3-7_n7-n78 | 0.7 | 0.7 | 0.7 | 0.7 | 0.8 |
| DC_1-3-7-8_n7 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7-8_n28DC_1-3-3-7-8_n78DC_1-3-7-7-8_n78DC_1-3-3-7-7-8_n78 | 0.5 | 0.5 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7-8_n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-7_n8-n78DC_1-3-3-7_n8-n78DC_1-3-7-7_n8-n78DC_1-3-3-7-7_n8-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-7-20_n8 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7-20_n28 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7-20_n38 | 0.3 | 0.3 | N/A | 0.3 | N/A |
| DC_1-3-7-20_n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7-26_n78DC_1-1-3-7-20_n78DC_1-3-3-7-20_n78DC_1-3-7-7-20_n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-7_n26-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-7-28_n3 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7-28_n5 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7-28_n7DC_1-3-28-(n)7 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7-28_n38 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7_n28-n38 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-7-28_n40 | 0.6 | 0.6 | 0.8 | 0.6 | 0.9 |
| DC_1-3-7-28_n78DC_1-3-7-7-28_n78 | 0.7 | 0.7 | 0.7 | 0.6 | 0.8 |
| DC_1-3-7_n28-n78 | 0.7 | 0.7 | 0.7 | 0.6 | 0.8 |
| DC_1-3-7-32_n28 | 0.6 | 0.6 | 0.6 | N/A | 0.6 |
| DC_1-3-7-32_n78 | 0.7 | 0.7 | 0.7 | N/A | 0.8 |
| DC_1-3-7-38_n28 | 0.6 | 0.6 | N/A | N/A | 0.5 |
| DC_1-3-7-38_n78 | 0.7 | 0.7 | N/A | N/A | 0.8 |
| DC_1-3-7-40_n78 | 0.6 | 0.6 | 0.5 | 0.35 | 0.85 |
| DC_1-3-7_n40-n77DC_1-3-7-7_n40-n77 | 0.6 | 0.6 | 0.8 | 0.9 | 0.8 |
| DC_1-3-7_n40-n78DC_1-3-7-7_n40-n78 | 0.6 | 0.6 | 0.8 | 0.9 | 0.8 |
| DC_1-3-7_n40-n105 | 0.7 | 0.7 | 0.7 | 0.8 | 0.7 |
| DC_1-3-7_n75-n78 | 0.7 | 0.7 | 0.7 | N/A | 0.8 |
| DC_1-3-7_n78-n105 | 0.7 | 0.7 | 0.7 | 0.8 | 0.7 |
| DC_1-3-8_n1-n41DC_1-3-3-8_n1-n41 | 0.5 | 0.5 | 0.3 | 0.5 | 0.33 / 0.84 |
| DC_1-3-8_n1-n78DC_1-3-3-8_n1-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-8_n7-n78 | 0.7 | 0.7 | 0.6 | 0.7 | 0.8 |
| DC_1-3-8-11_n28 | 0.3 | 0.8 | 0.6 | 0.9 | 0.6 |
| DC_1-3-8-11_n77 | 0.6 | 0.8 | 0.6 | 0.9 | 0.8 |
| DC_1-3-8-20_n28 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-3-8-20_n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-8-28_n40 | 0.6 | 0.6 | 0.6 | 0.6 | 0.5 |
| DC_1-3-8-28_n71 | 0.3 | 0.3 | 0.7 | 1.1 | 1.1 |
| DC_1-3-8-28_n77 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-8_n28-n77 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-8-28_n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-8_n28-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-8_n40-n71 | 0.5 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_1-3-8_n40-n77 | 0.6 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_1-3-8-41_n1DC_1-3-3-8-41_n1 | 0.5 | 0.5 | 0.3 | 0.33 / 0.84 | 0.5 |
| DC_1-3-8-41_n41DC_1-3-3-8-41_n41 | 0.5 | 0.5 | 0.3 | 0.33 / 0.84 | 0.33 / 0.84 |
| DC_1-3-8-41_n78 | 0.7 | 0.7 | 0.6 | 0.7 | 0.8 |
| DC_1-3-8-32_n78 | 0.6 | 0.6 | 0.6 | N/A | 0.8 |
| DC_1-3-8-40_n78 | 0.6 | 0.6 | 0.6 | 0.35 | 0.85 |
| DC_1-3-8-38_n28 | 0.6 | 0.6 | 0.6 | - | 0.6 |
| DC_1-3-8-38_n78 | 0.6 | 0.6 | 0.6 | - | 0.8 |
| DC_1-3-8-40_n28 | 0.6 | 0.6 | 0.6 | - | 0.6 |
| DC_1-3-8_n41-n78 | 0.7 | 0.7 | 0.6 | 0.7 | 0.8 |
| DC_1-3-8-42_n77 | 0.6 | 0.6 | 0.6 | N/A | 0.8 |
| DC_1-(n)3-8_n77 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-8_n71-n77 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-8_n77-n79 | 0.6 | 0.6 | 0.6 | 0.8 | 0.5 |
| DC_1-3-11_n28-n77 | 0.6 | 0.8 | 0.9 | 0.6 | 0.8 |
| DC_1-3-18_n3-n41 | 0.5 | 0.5 | 0.3 | 0.5 | 0.33 / 0.84 |
| DC_1-3-18_n3-n77 | 0.6 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_1-3-18_n3-n78 | 0.6 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_1-3-18_n28-n41 | 0.5 | 0.5 | 0.3 | 0.6 | 0.33 / 0.84 |
| DC_1-3-18_n28-n77 | 0.3 | 0.3 | 0.3 | 0.6 | 0.8 |
| DC_1-3-18_n28-n77 | 0.3 | 0.3 | 0.3 | 0.6 | 0.8 |
| DC_1-3-18_n41-n77 | 0.5 | 0.5 | 0.3 | 0.33 / 0.84 | 0.8 |
| DC_1-3-18_n41-n78 | 0.5 | 0.5 | 0.3 | 0.33 / 0.84 | 0.8 |
| DC_1-3-18-42_n77 | 0.6 | 0.6 | 0.3 | N/A | 0.8 |
| DC_1-3-18-42_n78 | 0.6 | 0.6 | 0.3 | N/A | 0.8 |
| DC_1-3-18-42_n79 | 0.6 | 0.6 | 0.3 | N/A | - |
| DC_1-3-19-21_n77 | 0.6 | 0.8 | 0.3 | 0.9 | 0.8 |
| DC_1-3-19-21_n78 | 0.6 | 0.8 | 0.3 | 0.9 | 0.8 |
| DC_1-3-19-21_n79 | 0.3 | 0.8 | 0.3 | 0.9 | - |
| DC_1-3-19-42_n77 | 0.6 | 0.6 | 0.3 | N/A | 0.8 |
| DC_1-3-19-42_n78 | 0.6 | 0.6 | 0.3 | N/A | 0.8 |
| DC_1-3-19-42_n79 | 0.6 | 0.6 | 0.3 | N/A | - |
| DC_1-3-20_n1-n78 | 0.6 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_1-3-20_n7-n78 | 0.6 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_1-3-20_n8-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-20_n28-n75 | 0.3 | 0.3 | 0.6 | 0.6 | N/A |
| DC_1-3-20-28_n78DC_1-3-3-20-28_n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-20_n28-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-20-32_n28 | 0.3 | 0.3 | 0.6 | N/A | 0.6 |
| DC_1-3-20-32_n78 | 0.6 | 0.6 | 0.6 | N/A | 0.8 |
| DC_1-3-20-38_n28 | 0.3 | 0.6 | 0.6 | 0.5 | 0.6 |
| DC_1-3-20-38_n78 | 0.3 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_1-3-20_n38-n78 | 0.3 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_1-3-20-40_n28 | 0.3 | 0.6 | 0.6 | 0.5 | 0.6 |
| DC_1-3-20-40_n78 | 0.5 | 0.5 | 0.3 | 0.55 | 0.85 |
| DC_1-3-20-41_n1DC_1-3-3-20-41_n1 | 0.5 | 0.5 | 0.3 | 0.33 / 0.84 | 0.5 |
| DC_1-3-20-41_n78 | 0.5 | 0.5 | 0.3 | 0.33 / 0.84 | 0.8 |
| DC_1-3-20_n41-n78 | 0.5 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_1-3-21-42_n77 | 0.6 | 0.8 | 0.9 | N/A | 0.6 |
| DC_1-3-21-42_n78 | 0.6 | 0.8 | 0.9 | N/A | 0.6 |
| DC_1-3-21-42_n79 | 0.6 | 0.8 | 0.9 | N/A | - |
| DC_1-3-21_n77-n79 | 0.6 | 0.8 | 0.9 | 0.8 | - |
| DC_1-3-21_n78-n79 | 0.6 | 0.8 | 0.9 | 0.8 | - |
| DC_1-3-28_n3-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-28_n7-n78 | 0.7 | 0.7 | 0.6 | 0.7 | 0.8 |
| DC_1-3-28-40_n78 | 0.5 | 0.5 | 0.6 | 0.5 | 0.8 |
| DC_1-3-28_n40-n71 | 0.5 | 0.5 | 1.1 | 0.6 | 1.1 |
| DC_1-3-28_n40-n77 | 0.5 | 0.5 | 0.5 | 0.3 | 0.8 |
| DC_1-3-28_n40-n78 | 0.5 | 0.6 | 0.5 | 0.35 | 0.85 |
| DC_1-3-28-42_n77 | 0.6 | 0.6 | 0.6 | N/A | 0.8 |
| DC_1-3-28-42_n78 | 0.6 | 0.6 | 0.6 | N/A | 0.8 |
| DC_1-3-28-42_n79 | 0.6 | 0.6 | 0.6 | N/A | - |
| DC_1-3-28_n71-n77 | 0.6 | 0.6 | 1.1 | 1.1 | 0.8 |
| DC_1-3_n28-n77-n79 | 0.6 | 0.6 | 0.6 | 0.8 | 0.5 |
| DC_1_n3-n28-n77-n79 | 0.6 | 0.6 | 0.6 | 0.8 | 0.8 |
| DC_1-3_n28-n78-n79 | 0.3 | 0.6 | 0.6 | 0.8 | 0.5 |
| DC_1-3-32_n28-n78 | 0.3 | 0.6 | N/A | 0.6 | 0.8 |
| DC_1-3-38_n7-n78 | 0.7 | 0.7 | N/A | N/A | 0.8 |
| DC_1-3-38_n28-n78 | 0.5 | 0.6 | 0.3 | 0.5 | 0.8 |
| DC_1-3_n40-n78-n105 | 0.5 | 0.6 | 0.5 | 0.8 | 0.5 |
| DC_1-3-41_n1-n41DC_1-3-3-41_n1-n41 | 0.5 | 0.5 | 0.33 / 0.84 | 0.5 | 0.33 / 0.84 |
| DC_1-3-41_n1-n78DC_1-3-3-41_n1-n78 | 0.5 | 0.5 | 0.33 / 0.84 | 0.5 | 0.8 |
| DC_1-3-41_n3-n41 | 0.5 | 0.5 | 0.33 / 0.84 | 0.5 | 0.33 / 0.84 |
| DC_1-3-41_n3-n77 | 0.6 | 0.6 | 0.5 | 0.6 | 0.8 |
| DC_1-3-41_n3-n78 | 0.6 | 0.6 | 0.5 | 0.6 | 0.8 |
| DC_1-3-41_n28-n41 | 0.3 | 0.3 | 0.33 / 0.84 | 0.6 | 0.33 / 0.84 |
| DC_1-3-41_n28-n77 | 0.6 | 0.6 | 0.33 / 0.84 | 0.5 | 0.8 |
| DC_1-3-41_n28-n78 | 0.5 | 0.6 | 0.33 / 0.84 | 0.5 | 0.8 |
| DC_1-3-41_n41-n77 | 0.6 | 0.6 | 0.5 | 0.5 | 0.8 |
| DC_1-3-41_n41-n78 | 0.6 | 0.6 | 0.5 | 0.5 | 0.8 |
| DC_1-3-41-42_n77 | 0.6 | 0.6 | 0.5 | N/A | 0.8 |
| DC_1-3-41-42_n78 | 0.6 | 0.6 | 0.5 | N/A | 0.8 |
| DC_1-3-41-42_n79 | 0.6 | 0.6 | 0.5 | N/A | - |
| DC_1-3-42_n28-n77 | 0.6 | 0.6 | 0.8 | 0.8 | 0.8 |
| DC_1-5-7_n28-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.9 |
| DC_1-5-7_n40-n77DC_1-5-7-7_n40-n77 | 0.6 | 0.6 | 0.5 | 0.35 | 0.85 |
| DC_1-5-7_n40-n78DC_1-5-7-7_n40-n78 | 0.6 | 0.6 | 0.5 | 0.35 | 0.85 |
| DC_1-7-8_n7-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-7-8-20 _n28 | 0.5 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-7-8-20_n78 | 0.6 | 0.7 | 0.6 | 0.6 | 0.8 |
| DC_1-7-8_n28-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-7-8-32_n78 | 0.7 | 0.7 | 0.6 | N/A | - |
| DC_1-7-8-40_n78 | 0.6 | 0.5 | 0.6 | 0.35 | 0.85 |
| DC_1-7-20_n3-n38 | 0.6 | 0.6 | 0.6 | 0.6 | 0.5 |
| DC_1-7-20_n3-n78 | 0.6 | 0.7 | 0.4 | 0.5 | 0.8 |
| DC_1-7-20_n8-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-7-20-28 _n3 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_1-7-20_n28-n78 | 0.6 | 0.7 | 0.6 | 0.6 | 0.8 |
| DC_1-7-20-32_n3 | 0.7 | 0.7 | 0.3 | N/A | 0.7 |
| DC_1-7-20-32_n8 | 0.7 | 0.7 | 0.6 | N/A | 0.6 |
| DC_1-7-20-32_n28 | 0.5 | 0.6 | 0.6 | N/A | 0.7 |
| DC_1-7-20-32_n78 | 0.6 | 0.7 | 0.4 | N/A | 0.8 |
| DC_1-7-20-38_n3 | 0.6 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_1-7-20-38_n8 | 0.5 | N/A | 0.6 | N/A | 0.6 |
| DC_1-7-20-38_n78 | 0.6 | 0.7 | 0.6 | - | 0.8 |
| DC_1-7-28_n3-n78 | 0.7 | 0.7 | 0.6 | 0.7 | 0.6 |
| DC_1-7-28_n5-n40 | 0.6 | 0.8 | 0.6 | 0.6 | 0.9 |
| DC_1-7-28_n7-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-7-28-32_n3 | 0.6 | 0.6 | 0.6 | N/A | 0.6 |
| DC_1-7-32_n28-n78 | 0.5 | 0.6 | N/A | 0.7 | 0.8 |
| DC_1-7-28_n40-n78 | 0.6 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_1-7-38_n3-n78 | 0.6 | N/A | N/A | 0.6 | 0.8 |
| DC_1-7_n40-n78-n105 | 0.5 | 0.6 | 0.5 | 0.8 | 0.5 |
| DC_1-8-(n)3-n77 | 0.6 | 0.6 | 0.8 | 0.8 | 0.8 |
| DC_1-8-(n)3-n78 | 0.6 | 0.6 | 0.8 | 0.8 | 0.8 |
| DC_1-8_n3-n28-n77 | 0.6 | 0.6 | 0.8 | 0.6 | 0.8 |
| DC_1-8_n3-n28-n79 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-8_n3-n77-n79 | 0.6 | 0.6 | 0.8 | 0.8 | 0.8 |
| DC_1-8-11_n3-n28 | 0.3 | 0.6 | 0.8 | 0.9 | 0.6 |
| DC_1-8-11_n3-n77 | 0.6 | 0.6 | 0.8 | 0.9 | 0.8 |
| DC_1-8-11_n3-n79 | 0.3 | 0.3 | 0.8 | 0.9 | 0.8 |
| DC_1-8-11_n28-n77 | 0.6 | 0.6 | 0.4 | 0.6 | 0.8 |
| DC_1-8-11_n77-n79 | 0.6 | 0.6 | 0.4 | 0.8 | 0.5 |
| DC_1-8-20-28_n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-8-20-38_n28 | 0.6 | 0.6 | 0.6 | 0.5 | 0.6 |
| DC_1-8-20-38_n78 | 0.6 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_1-8-20-40_n28 | 0.6 | 0.6 | 0.6 | 0.5 | 0.6 |
| DC_1-8-28_n40-n71 | 0.3 | 0.7 | 1.1 | 0.3 | 1.1 |
| DC_1-8-28_n40-n77 | 0.6 | 0.6 | 0.5 | 0.3 | 0.8 |
| DC_1-8-28_n71-n77 | 0.6 | 0.6 | 1.1 | 1.1 | 0.8 |
| DC_1-8_n28-n77-n79 | 0.6 | 0.6 | 0.6 | 0.8 | 0.8 |
| DC_1-8-41_n1-n41 | 0.6 | 0.3 | 0.6 | 0.6 | 0.6 |
| DC_1-8-41_n1-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-8-42_n3-n28 | 0.3 | 0.6 | 0.8 | 0.6 | 0.8 |
| DC_1-8-42_n3-n77 | 0.6 | 0.6 | 0.8 | 0.8 | 0.8 |
| DC_1-8-42_n28-n77 | 0.6 | 0.6 | 0.8 | 0.8 | 0.8 |
| DC_1-11_n3-n28-n77 | 0.6 | 0.8 | 0.9 | 0.6 | 0.8 |
| DC_1-11_n3-n77-n79 | 0.6 | 0.8 | 0.9 | 0.8 | 0.8 |
| DC_1-18-41_n3-n77 | 0.6 | 0.3 | 0.33 / 0.84 | 0.6 | 0.8 |
| DC_1-18-41_n3-n78 | 0.6 | 0.3 | 0.33 / 0.84 | 0.6 | 0.8 |
| DC_1-19-21-42_n77 | 0.3 | 0.3 | 0.4 | 0.8 | 0.8 |
| DC_1-19-21-42_n78 | 0.3 | 0.3 | 0.4 | N/A | 0.8 |
| DC_1-19-21-42_n79 | 0.3 | 0.3 | 0.4 | N/A | - |
| DC_1-19-42_n77-n79 | 0.6 | 0.3 | N/A | 0.8 | - |
| DC_1-19-42_n78-n79 | 0.3 | 0.3 | N/A | 0.8 | - |
| DC_1-20-28-32_n3 | 0.5 | 0.6 | 0.6 | N/A | 0.5 |
| DC_1-20-38_n3-n78 | 0.5 | 0.6 | 0.5 | 0.6 | 0.8 |
| DC_1-20-41_n1-n78 | 0.5 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_1-21-28-42_n77 | 0.6 | 0.4 | 0.6 | N/A | 0.8 |
| DC_1-21-28-42_n78 | 0.3 | 0.4 | 0.6 | N/A | 0.8 |
| DC_1-21-28-42_n79 | 0.3 | 0.4 | 0.6 | N/A | - |
| DC_1-21_n28-n77-n79 | 0.6 | 0.4 | 0.6 | 0.8 | 0.5 |
| DC_1-21_n28-n78-n79 | 0.6 | 0.4 | 0.6 | 0.8 | 0.5 |
| DC_1-21-42_n77-n79 | 0.6 | 0.4 | N/A | 0.8 | - |
| DC_1-28-32_n40-n41 | 0.6 | 0.6 | N/A | 0.9 | 0.8 |
| DC_1-42_n3-n28-n77 | 0.6 | 0.8 | 0.8 | 0.8 | 0.8 |
| DC_1-21-42_n78-n79 | 0.3 | 0.4 | N/A | 0.8 | - |
| DC_2-5-7_n2-n66 | 0.5 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_2-5-7_n2-n77 | 0.6 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_2-5-7_n2-n78 | 0.6 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_2-5-7-66_n2 | 0.5 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_2-5-7-66_n7DC_2-5-7-66-66_n7 | 0.5 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_2-5-7-(n)66DC_2-5-7-7-(n)66DC_2-5-7-66_n66 | 0.5 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_2-5-7-66_n77DC_2-5-7_n66-n77 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-5-7-66_n78DC_2-5-7_n66-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_2-5-66_n2-n41 | 0.5 | 0.6 | 0.5 | 0.5 | 0.81 / 1.32 |
| DC_2-5-66_n2-n77DC_2-5-66-66_n2-n77 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-5-66_n2-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-5-66_n5-n77DC_2-5-66-66_n5-n77 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-5-66_n41-n66 | 0.6 | 0.6 | 0.81 / 1.32 | 0.41 / 0.92 | 0.81 / 1.32 |
| DC_2-5-66_n41-n77 | 0.6 | 0.6 | 0.81 / 1.32 | 0.81 / 1.32 | 0.8 |
| DC_2-5-66_n41-n78 | 0.6 | 0.5 | 0.81 / 1.32 | 0.41 / 0.92 | 0.8 |
| DC_2-5-30-66_n2 | 0.5 | 0.3 | 0.3 | 0.5 | 0.5 |
| DC_2-5-30-66_n66 | 0.5 | 0.3 | 0.3 | 0.5 | 0.5 |
| DC_2-5-30-66_n77 | 0.6 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_2-5-66_n66-n77 | 0.5 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_2-7-12_n2-n77 | 0.6 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_2-7-12_n2-n66 | 0.5 | 0.5 | 0.8 | 0.5 | 0.5 |
| DC_2-7-12_n2-n78 | 0.6 | 0.6 | 0.6 | 0.5 | 0.6 |
| DC_2-7-12-66_n2 | 0.5 | 0.5 | 0.8 | 0.5 | 0.5 |
| DC_2-7-12-66_n66 | 0.6 | 0.8 | 0.5 | 0.8 | 0.8 |
| DC_2-7-12-66_n77DC_2-7-12_n66-n77 | 0.6 | 0.8 | 0.5 | 1 | 0.8 |
| DC_2-7-12-66_n78DC_2-7-12_n66-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_2-7-13_n25-n66 | 0.5 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-7-13-(n)66DC_2-7-7-13-(n)66DC_2-7-13-66_n66 | 0.5 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-7-28-66_n7 | 0.5 | 0.5 | 0.6 | 0.5 | 0.5 |
| DC_2-7-28-66_n66 | 0.5 | 0.5 | 0.6 | 0.5 | 0.5 |
| DC_2-7-29-66_n78DC_2-7-7-29-66_n78 | 0.6 | 0.5 | N/A | 0.6 | 0.8 |
| DC_2-7-66_n2-n66 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-7-66_n2-n71 | 0.5 | 0.5 | 0.5 | 0.5 | 0.3 |
| DC_2-7-66_n2-n77 | 0.6 | 0.5 | 0.6 | 0.5 | 0.8 |
| DC_2-7-66_n2-n78 | 0.6 | 0.5 | 0.6 | 0.5 | 0.8 |
| DC_2-7-66_n25-n66 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-7-66_n66-n71 | 0.5 | 0.5 | 0.5 | 0.5 | 0.6 |
| DC_2-7-66_n66-n77 | 0.6 | 0.5 | 0.6 | 0.6 | 0.8 |
| DC_2-7-(n)66-n78DC_2-7-66_n66-n78DC_2-7-7-(n)66-n78DC_2-7-7-66_n66-n78 | 0.6 | 0.5 | 0.6 | 0.6 | 0.8 |
| DC_2-7-66-71_n2 | 0.5 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-7-66-71_n66 | 0.5 | 0.5 | 0.5 | 0.6 | 0.5 |
| DC_2-7-66-71_n77DC_2-7-66_n71-n77 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_2-7-66-71_n78DC_2-7-66_n71-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_2-7-71_n2-n66 | 0.5 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-7-71_n2-n77 | 0.6 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_2-7-71_n2-n78 | 0.6 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_2-7-71_n66-n77 | 0.6 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_2-7-71_n66-n78 | 0.6 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_2-12-30-66_n2 | 0.5 | 0.8 | 0.3 | 0.5 | 0.5 |
| DC_2-12-30-66_n66 | 0.5 | 0.8 | 0.3 | 0.5 | 0.5 |
| DC_2-12-30-66_n77 | 0.6 | 0.8 | 0.3 | 0.6 | 0.8 |
| DC_2-12-66_n2-n41 | 0.5 | 0.8 | 0.5 | 0.5 | 0.51 / 12 |
| DC_2-12-66_n2-n66 | 0.5 | 0.8 | 0.5 | 0.5 | 0.5 |
| DC_2-12-66_n2-n77 | 0.6 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_2-12-66_n2-n78 | 0.6 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_2-12-66_n66-n77 | 0.6 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_2-13-66_n2-n77DC_2-13-66-66_n2-n77 | 0.6 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_2-13-66_n5-n77DC_2-2-13-66_n5-n77DC_2-13-66-66_n5-n77 | 0.6 | 0.5 | 0.6 | 0.6 | 0.8 |
| DC_2-13-66_n66-n77DC_2-2-13-66_n66-n77 | 0.6 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_2-14-30-66_n2 | 0.5 | 0.3 | 0.3 | 0.5 | 0.5 |
| DC_2-14-30-66_n66 | 0.5 | 0.3 | 0.3 | 0.5 | 0.5 |
| DC_2-14-30-66_n77 | 0.6 | 0.6 | 0.3 | 0.6 | 0.8 |
| DC_2-29-30-66_n2 | 0.5 | N/A | 0.3 | 0.5 | 0.5 |
| DC_2-29-30-66_n66 | 0.5 | N/A | 0.3 | 0.5 | 0.5 |
| DC_2-29-30-66_n77 | 0.6 | N/A | 0.3 | 0.6 | 0.8 |
| DC_2-30-66-(n)5 | 0.5 | 0.3 | 0.3 | 0.5 | 0.3 |
| DC_2-46-66_n41-n71 | 0.5 | N/A | 0.5 | 0.41 / 0.92 | 0.6 |
| DC_2-66-71_n2-n41 | 0.5 | 0.5 | 0.6 | 0.5 | 0.41 / 0.92 |
| DC_2-66-71_n2-n66 | 0.5 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-66-71_n2-n77 | 0.5 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_2-66-71_n2-n78 | 0.5 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_2-66-71_n66-n77 | 0.5 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_3-5-7_n28-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.9 |
| DC_3-5-7_n40-n77DC_3-5-7-7_n40-n77 | 0.6 | 0.6 | 0.5 | 0.55 | 0.85 |
| DC_3-5-7_n40-n78DC_3-5-7-7_n40-n78 | 0.6 | 0.6 | 0.5 | 0.55 | 0.85 |
| DC_3-7_n1-n40-n78 | 0.2 | 0.3 | 0.2 | 0.8 | 0.5 |
| DC_3-7_n1-n75-n78 | 0.7 | 0.7 | 0.7 | - | 0.8 |
| DC_3-7-8_n1-n40 | 0.5 | 0.8 | 0.6 | 0.6 | 0.9 |
| DC_3-7-8_n1-n78DC_3-3-7-8_n1-n78DC_3-7-7-8_n1-n78DC_3-3-7-7-8_n1-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7_n1-n8-n78DC_3-3-7_n1-n8-n78DC_3-7-7_n1-n8-n78DC_3-3-7-7_n1-n8-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-8_n7-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-8-20_n1 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_3-7-8-20_n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-8_n28-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-8-32_n1 | 0.6 | 0.7 | 0.6 | N/A | 0.7 |
| DC_3-7-8-32_n78 | 0.6 | 0.6 | 0.6 | N/A | 0.8 |
| DC_3-7-8-40_n78 | 0.6 | 0.5 | 0.6 | 0.55 | 0.85 |
| DC_3-7-8_n40-n78 | 0.6 | 0.5 | 0.6 | 0.55 | 0.85 |
| DC_3-7-20_n1-n75 | 0.7 | 0.7 | 0.3 | 0.7 | N/A |
| DC_3-7-20_n1-n78 | 0.6 | 0.7 | 0.6 | 0.6 | 0.8 |
| DC_3-7-20_n8-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-20-28_n1 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| DC_3-7-20_n28-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-20-28_n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-20-32_n1 | 0.7 | 0.7 | 0.3 | N/A | 0.7 |
| DC_3-7-20-32_n78 | 0.6 | 0.6 | 0.3 | N/A | 0.8 |
| DC_3-7-20-38_n78 | 0.6 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_3-7-28_n1-n40 | 0.6 | 0.8 | 0.6 | 0.6 | 0.9 |
| DC_3-7-28_n1-n78 | 0.7 | 0.7 | 0.6 | 0.7 | 0.6 |
| DC_3-7-28_n3-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-28_n5-n40 | 0.6 | 0.8 | 0.6 | 0.6 | 0.9 |
| DC_3-7-28_n7-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-28_n40-n78 | 0.6 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_3-7-32_n1-n28 | 0.6 | 0.6 | N/A | 0.6 | 0.7 |
| DC_3-7-32_n1-n78 | 0.3 | 0.3 | N/A | 0.3 | 0.5 |
| DC_3-7-32_n28-n78 | 0.6 | 0.5 | N/A | 0.3 | 0.8 |
| DC_3-7-40_n1-n78 | 0.6 | 0.5 | 0.35 | 0.6 | 0.85 |
| DC_3-8-11_n28-n77 | 0.8 | 0.6 | 0.9 | 0.6 | 0.8 |
| DC_3-8-20-28_n1 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 |
| DC_3-8-20_n1-n78 | 0.6 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_3-8-20-38_n1 | 0.2 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_3-8-20-38_n28 | 0.2 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_3-8-20-40_n1 | 0.2 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_3-8-20-40_n28 | 0.2 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_3-8-20-40_n78 | 0.2 | 0.2 | 0.2 | 0.5 | 0.8 |
| DC_3-8-28-38_n1 | 0.2 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_3-8-28-40_n1 | 0.2 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_3-8-20-28_n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-8-28_n40-n71 | 0.3 | 0.7 | 1.1 | 0.3 | 1.1 |
| DC_3-8-28_n40-n77 | 0.6 | 0.6 | 0.5 | 0.3 | 0.8 |
| DC_3-8-28_n71-n77 | 0.6 | 0.6 | 1.1 | 1.1 | 0.8 |
| DC_3-8-32_n1-n78 | 0.6 | 0.6 | N/A | 0.8 | 0.8 |
| DC_3-8-40_n1-n78 | 0.6 | 0.6 | 0.35 | 0.6 | 0.85 |
| DC_3-8-41_n1-n41DC_3-3-8-41_n1-n41 | 0.5 | 0.3 | 0.33 / 0.84 | 0.5 | 0.33 / 0.84 |
| DC_3-8-41_n1-n78DC_3-3-8-41_n1-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-19-21-42_n77 | 0.8 | 0.3 | 0.9 | N/A | 0.8 |
| DC_3-19-21-42_n78 | 0.8 | 0.3 | 0.9 | N/A | 0.8 |
| DC_3-19-21-42_n79 | 0.8 | 0.3 | 0.9 | N/A | - |
| DC_3-19-42_n1-n77 | 0.6 | 0.3 | N/A | 0.6 | 0.8 |
| DC_3-19-42_n1-n78 | 0.6 | 0.3 | N/A | 0.6 | 0.8 |
| DC_3-19-42_n1-n79 | 0.6 | 0.3 | 0.8 | 0.6 | - |
| DC_3-20_n1-n28-n75 | 0.3 | 0.6 | 0.3 | 0.6 | - |
| DC_3-20-28-38_n1 | 0.2 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_3-20-28-40_n1 | 0.2 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_3-20-28-40_n78 | 0.2 | 0.2 | 0.2 | 0.5 | 0.8 |
| DC_3-20-32_n1-n28 | 0.3 | 0.6 | N/A | 0.3 | 0.6 |
| DC_3-20-38-40_n1 | 0.2 | 0.2 | 0.5 | 0.5 | 0.2 |
| DC_3-20-38-40_n28 | 0.2 | 0.2 | 0.5 | 0.5 | 0.2 |
| DC_3-20-32_n1-n78 | 0.6 | 0.6 | N/A | 0.3 | 0.8 |
| DC_3-20-41_n1-n78DC_3-3-20-41_n1-n78 | 0.5 | 0.3 | 0.5 | 0.5 | 0.8 |
| DC_3-21_n1-n77-n79 | 0.8 | 0.9 | 0.6 | 0.8 | 0.5 |
| DC_3-21_n1-n78-n79 | 0.8 | 0.9 | 0.6 | 0.8 | 0.5 |
| DC_3-21_n28-n77-n79 | 0.8 | 0.9 | 0.5 | 0.8 | 0.5 |
| DC_3-21_n28-n78-n79 | 0.8 | 0.9 | 0.5 | 0.8 | 0.5 |
| DC_3-21-42_n1-n77 | 0.8 | 0.9 | N/A | 0.6 | 0.6 |
| DC_3-21-42_n1-n78 | 0.8 | 0.9 | N/A | 0.6 | 0.6 |
| DC_3-21-42_n1-n79 | 0.8 | 0.9 | 0.8 | 0.6 | - |
| DC_3-28_n1-n40-n78 | 0.6 | 0.8 | 0.6 | 0.9 | 0.8 |
| DC_3-28-41-42_n78 | 1.0 | 0.5 | 0.33 / 0.84 | N/A | 0.8 |
| DC_5-7-66_n2-n66 | 0.3 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_5-7-66_n2-n77 | 0.3 | 0.5 | 0.5 | 0.5 | 0.8 |
| DC_5-7-66_n2-n78 | 0.3 | 0.5 | 0.5 | 0.5 | 0.8 |
| DC_5-7-66_n66-n77 | 0.3 | 0.5 | 0.5 | 0.5 | 0.8 |
| DC_7-8-20-32_n1 | 0.7 | 0.6 | 0.7 | N/A | 0.5 |
| DC_7-8-20_n1-n78 | 0.6 | 0.6 | 0.6 | 0.5 | 0.8 |
| DC_7-8-32_n1-n78 | 0.7 | 0.6 | N/A | 0.7 | 0.8 |
| DC_7-8-40_n1-n78 | 0.5 | 0.6 | 0.35 | 0.6 | 0.85 |
| DC_7-12-66_n2-n66 | 0.5 | 0.8 | 0.5 | 0.5 | 0.5 |
| DC_7-12-66_n2-n77 | 0.8 | 0.8 | 1.0 | 0.5 | 0.8 |
| DC_7-12-66_n2-n78 | 0.8 | 0.8 | 1.0 | 0.5 | 0.8 |
| DC_7-12-66_n66-n77 | 0.8 | 0.8 | 1.0 | 0.5 | 0.8 |
| DC_7-20-28-32_n1 | 0.7 | 0.6 | 0.6 | N/A | 0.7 |
| DC_7-20-28-32_n3 | 0.7 | 0.6 | 0.5 | N/A | 0.7 |
| DC_7-20-32_n1-n78 | 0.7 | 0.6 | N/A | 0.7 | 0.8 |
| DC_7-20-32-38_n1 | N/A | 0.3 | - | N/A | 0.7 |
| DC_7-20-38_n3-n78 | 0.5 | 0.6 | 0.5 | 0.5 | 0.8 |
| DC_7-28_n1-n40-n78 | 0.8 | 0.8 | 0.6 | 0.9 | 0.8 |
| DC_7-66-71_n2-n66 | 0.5 | 0.6 | 0.6 | 0.6 | 0.5 |
| DC_7-66-71_n2-n77 | 0.6 | 0.6 | 0.3 | 0.5 | 0.8 |
| DC_7-66-71_n2-n78 | 0.6 | 0.6 | 0.3 | 0.5 | 0.8 |
| DC_7-66-71_n66-n77 | 0.5 | 0.5 | 0.5 | 0.5 | 0.8 |
| DC_8_n3-n28-n77-n79 | 0.2 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_8-11_n3-n28-n77 | 0.6 | 0.8 | 0.9 | 0.6 | 0.8 |
| DC_8-11_n3-n77-n79 | 0.6 | 0.8 | 0.9 | 0.8 | 0.8 |
| DC_8-20-28-38_n1 | 0.2 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_8-20-28-40_n1 | 0.2 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_8-20-38-40_n28 | 0.2 | 0.2 | 0.4 | 0.5 | 0.2 |
| DC_8-42_n3-n28-n77 | 0.6 | 0.8 | 0.6 | 0.8 | 0.8 |
| DC_19-21-42_n1-n77 | 0.3 | 0.4 | N/A | 0.3 | 0.8 |
| DC_19-21-42_n1-n78 | 0.3 | 0.4 | N/A | 0.3 | 0.8 |
| DC_19-21-42_n1-n79 | 0.3 | 0.4 | 0.8 | 0.3 | - |
| DC_19-21-42_n77-n79 | 0.3 | 0.4 | N/A | 0.8 | - |
| DC_19-21-42_n78-n79 | 0.3 | 0.4 | N/A | 0.8 | - |
| DC_19-42_n1-n77-n79 | 0.3 | N/A | 0.6 | 0.8 | 0.5 |
| DC_19-42_n1-n78-n79 | 0.3 | N/A | 0.3 | 0.8 | 0.5 |
| NOTE 1: The requirement is applied for UE transmitting on the frequency range of 2545 – 2690 MHz.NOTE 2: The requirement is applied for UE transmitting on the frequency range of 2496 – 2545 MHz. NOTE 3: The requirement is applied for UE transmitting on the frequency range of 2515 – 2690 MHz.NOTE 4: The requirement is applied for UE transmitting on the frequency range of 2496 – 2515 MHz.NOTE 5: Only applicable for UE supporting inter-band carrier aggregation with uplink in one E-UTRA band and without simultaneous Rx/TxNOTE 6: “-” denotes ΔTIB,c = 0.NOTE 7: The component band order in the configuration should be listed by the order of E-UTRA band and NR band respectively, such as for DC_2-30-66-(n)5 the band order from left to right is 2, 5, 30, 66 and n5. |  |  |  |  |  |

###### 6.2B.4.2.3.5 ΔTIB,c for EN-DC six bands

Table 6.2B.4.2.3.5-1: ΔTIB,c due to EN-DC (six bands)

| Inter-band EN-DC configuration | ΔTIB,c for E-UTRA band / NR band (dB)3 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Component band in order of bands in configuration4 |  |  |  |  |  |
| DC_1-3-5-7_n28-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 | 0.9 |
| DC_1-3-5-7_n40-n77DC_1-3-5-7-7_n40-n77 | 0.6 | 0.6 | 0.6 | 0.5 | 0.31 | 0.81 |
| DC_1-3-5-7_n40-n78DC_1-3-5-7-7_n40-n78 | 0.6 | 0.6 | 0.6 | 0.5 | 0.31 | 0.81 |
| DC_1-3-7-8_n7-n78 | 0.7 | 0.7 | 0.7 | 0.6 | 0.7 | 0.8 |
| DC_1-3-7-8_n28-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-7-8-32_n78 | 0.6 | 0.6 | 0.6 | 0.6 | N/A | 0.8 |
| DC_1-3-7-8-40_n78 | 0.6 | 0.6 | 0.5 | 0.6 | 0.31 | 0.81 |
| DC_1-3-7-20_n8-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-7-20-28_n78 | 0.7 | 0.7 | 0.7 | 0.6 | 0.6 | 0.8 |
| DC_1-3-7-20_n28-n78 | 0.7 | 0.7 | 0.7 | 0.6 | 0.6 | 0.8 |
| DC_1-3-7-20-32_n78 | 0.7 | 0.7 | 0.7 | 0.4 | N/A | 0.8 |
| DC_1-3-7-20-38_n78 | 0.7 | 0.7 | N/A | 0.6 | N/A | 0.8 |
| DC_1-3-7-20_n38-n78 | 0.6 | 0.6 | N/A | 0.6 | N/A | 0.8 |
| DC_1-3-7-28_n3-n78 | 0.7 | 0.7 | 0.7 | 0.6 | 0.7 | 0.8 |
| DC_1-3-7-28_n5-n40 | 0.6 | 0.6 | 0.8 | 0.6 | 0.6 | 0.9 |
| DC_1-3-7-28_n7-n78 | 0.7 | 0.7 | 0.7 | 0.6 | 0.7 | 0.8 |
| DC_1-3-7-28_n40-n78 | 0.6 | 0.6 | 0.8 | 0.3 | 0.9 | 0.8 |
| DC_1-3-7-28_n38-n78 | 0.7 | 0.7 | 0.7 | 0.6 | 0.7 | 0.8 |
| DC_1-3-7-32_n28-n78 | 0.6 | 0.6 | 0.6 | N/A | 0.6 | 0.8 |
| DC_1-3-7_n40-n78-n105 | 0.7 | 0.7 | 0.7 | 0.6 | 0.8 | 0.6 |
| DC_1-3-8-11_n28-n77 | 0.6 | 0.8 | 0.6 | 0.9 | 0.6 | 0.8 |
| DC_1-3-8-20-28_n78 | 0.3 | 0.3 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-8-20_n28-n78 | 0.3 | 0.3 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_1-3-8-20-38_n28 | 0.3 | 0.3 | 0.6 | 0.6 | - | 0.6 |
| DC_1-3-8-20-40_n28 | 0.3 | 0.3 | 0.6 | 0.6 | 0.9 | 0.6 |
| DC_1-3-8-28_n40-n71 | 0.3 | 0.3 | 0.7 | 1.1 | 0.3 | 1.1 |
| DC_1-3-8-28_n40-n77 | 0.6 | 0.6 | 0.6 | 0.5 | 0.3 | 0.8 |
| DC_1-3-8-28_n71_n77 | 0.6 | 0.8 | 0.6 | 1.1 | 1.1 | 0.8 |
| DC_1-3-8-38_n28-n78 | 0.3 | 0.3 | 0.6 | - | 0.6 | 0.8 |
| DC_1-3-8-41_n1-n41DC_1-3-3-8-41_n1-n41 | 0.5 | 0.5 | 0.3 | 0.35 / 0.86 | 0.5 | 0.35 / 0.86 |
| DC_1-3-8-41_n1-n78 | 0.7 | 0.7 | 0.6 | 0.7 | 0.7 | 0.8 |
| DC_1-3-20-38_n28-n78 | 0.3 | 0.3 | 0.6 | - | 0.6 | 0.8 |
| DC_1-3-20-40_n28-n78 | 0.3 | 0.3 | 0.6 | - | 0.6 | 0.8 |
| DC_1-7-20-28-32_n3 | 0.6 | 0.6 | 0.6 | 0.6 | N/A | 0.6 |
| DC_1-7-20-38_n3-n78 | 0.6 | 0.7 | 0.6 | 0.5 | 0.6 | 0.8 |
| DC_1-8_n3-n28-n77-n79 | 0.6 | 0.6 | 0.8 | 0.6 | 0.8 | 0.8 |
| DC_1-8-11_n3-n28-n77 | 0.6 | 0.6 | 0.8 | 0.9 | 0.6 | - |
| DC_1-8-20-38_n28-n78 | 0.3 | 0.6 | 0.6 | - | 0.6 | 0.8 |
| DC_1-8-42_n3-n28-n77 | 0.6 | 0.6 | 0.8 | 0.8 | - | 0.8 |
| DC_2-5-7-66_n2-n66 | 0.5 | 0.3 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-5-7-66_n2-n77 | 0.5 | 0.3 | 0.5 | 0.5 | 0.5 | 0.8 |
| DC_2-5-7-66_n2-n78 | 0.5 | 0.3 | 0.5 | 0.5 | 0.5 | 0.8 |
| DC_2-7-12-66_n2-n66 | 0.5 | 0.5 | 0.8 | 0.5 | 0.5 | 0.5 |
| DC_2-7-12-66_n2-n77 | 0.6 | 0.6 | 0.8 | 0.5 | 0.5 | 0.8 |
| DC_2-5-7-66_n66-n77 | 0.5 | 0.3 | 0.5 | 0.5 | 0.5 | 0.8 |
| DC_2-7-12-66_n2-n78 | 0.6 | 0.6 | 0.8 | 0.5 | 0.5 | 0.8 |
| DC_2-7-66-71_n2-n66 | 0.5 | 0.5 | 0.6 | 0.6 | 0.6 | 0.5 |
| DC_2-7-66-71_n2-n77 | 0.5 | 0.5 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_2-7-12-66_n66-n77 | 0.6 | 0.6 | 0.8 | 0.5 | 0.5 | 0.8 |
| DC_2-7-66-71_n2-n78 | 0.5 | 0.5 | 0.5 | 0.3 | 0.5 | 0.8 |
| DC_2-7-66-71_n66-n77 | 0.5 | 0.5 | 0.5 | 0.6 | 0.5 | 0.8 |
| DC_3-7-8-20_n1-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 | 0.8 |
| DC_3-7-8-32_n1-n78 | 0.6 | 0.6 | 0.6 | N/A | 0.6 | 0.8 |
| DC_3-7-8-40_n1-n78 | 0.6 | 0.5 | 0.6 | 0.32 | 0.6 | 0.82 |
| DC_3-7-20-32_n1-n78 | 0.6 | 0.6 | 0.6 | N/A | 0.6 | 0.8 |
| DC_3-7-28_n1-n40-n78 | 0.6 | 0.8 | 0.8 | 0.6 | 0.9 | 0.8 |
| DC_3-8-20-28_n1-n78 | 0.6 | 0.6 | 0.6 | 0.6 | 0.7 | 0.8 |
| DC_3-8-20-28-38_n1 | 0.6 | 0.6 | 0.6 | 0.6 | - | 0.7 |
| DC_3-8-20-28-40_n1 | 0.6 | 0.6 | 0.6 | 0.6 | - | 0.7 |
| DC_3-8-20-38_n1-n28 | 0.6 | 0.6 | 0.6 | - | 0.7 | 0.6 |
| DC_3-8-20-40_n1-n28 | 0.6 | 0.6 | 0.6 | 0.9 | 0.7 | 0.6 |
| DC_3-8-20-40_n1-n78 | 0.6 | 0.6 | 0.6 | 0.9 | 0.7 | 0.8 |
| DC_3-20-28-40_n1-n78 | 0.6 | 0.6 | 0.6 | 0.9 | 0.7 | 0.8 |
| DC_3-20-38-40_n1-n28 | 0.6 | 0.6 | - | 0.9 | 0.7 | 0.6 |
| DC_7-8-20-32-38_n1 | N/A | 0.6 | 0.6 | N/A | N/A | 0.7 |
| DC_7-20-28-32-38_n1 | N/A | 0.6 | 0.6 | N/A | N/A | 0.7 |
| NOTE 1: Only applicable for UE supporting inter-band carrier aggregation with uplink in one NR band and without simultaneous Rx/Tx.NOTE 2: Only applicable for UE supporting inter-band carrier aggregation with uplink in one E-UTRA band and without simultaneous Rx/Tx.NOTE 3: “-” denotes ΔTIB,c = 0.NOTE 4: The component band order in the configuration should be listed by the order of E-UTRA band and NR band respectively.NOTE 5: The requirement is applied for UE transmitting on the frequency range of 2515 – 2690 MHz.NOTE 6: The requirement is applied for UE transmitting on the frequency range of 2496 – 2515 MHz. |  |  |  |  |  |  |

##### 6.2B.4.2.3a Inter-band NE-DC within FR1

Unless ΔTIB,c  is specified in this clause, the value of ΔTIB,c  for the correspondingly specified EN-DC configuration in clause 6.2B.4.2.3 is applicable.

Table 6.2B.4.2.3a-1: ΔTIB,c due to NE-DC (two bands)

| Inter-band NE-DC configuration | ΔTIB,c for NR band / E-UTRA band (dB)1 |  |
| --- | --- | --- |
|  | Component band in order of bands in configuration2 |  |
| DC_n28_34 | 0.3 | 0.3 |
| DC_n28_39 | 0.3 | 0.3 |
| DC_n40_42 | 0 | 0.5 |
| DC_n41_34 | 0.3 | 0.3 |
| NOTE *: “-” denotes ΔTIB,c = 0.NOTE **: The component band order in the configuration should be listed by the order of NR band and E-UTRA band respectively. |  |  |

##### 6.2B.4.2.4 Inter-band EN-DC including FR2

###### 6.2B.4.2.4.1 ΔTIB,c for EN-DC two bands

Unless otherwise stated, ΔTIB,c for E-UTRA and FR2 NR bands of inter-band EN-DC combinations defined in table 5.5B.5.1-1 is set to zero.

Table 6.2B.4.2.4.1-1: Void

###### 6.2B.4.2.4.2 ΔTIB,c for EN-DC three bands

Unless otherwise stated, ΔTIB,c for FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA bands for inter-band EN-DC defined in table 5.5B.5.2-1 is the same as those for the corresponding E-UTRA CA configuration specified in TS 36.101 [4], without the FR2 NR bands.

Table 6.2B.4.2.4.2-1: Void

###### 6.2B.4.2.4.3 ΔTIB,c for EN-DC four bands

Unless otherwise stated, ΔTIB,c for FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA bands for inter-band EN-DC defined in table 5.5B.5.3-1 is the same as those for the corresponding E-UTRA CA configuration specified in TS 36.101 [4], without the FR2 NR bands.

Table 6.2B.4.2.4.3-1: Void

###### 6.2B.4.2.4.4 ΔTIB,c for EN-DC five bands

Unless otherwise stated, ΔTIB,c for FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA bands for inter-band EN-DC defined in table 5.5B.5.4-1 is the same as those for the corresponding E-UTRA CA configuration specified in TS 36.101 [4], without the FR2 NR bands.

Table 6.2B.4.2.4.4-1: Void

###### 6.2B.4.2.4.5 Void

##### 6.2B.4.2.4a (Void)

##### 6.2B.4.2.5 Inter-band EN-DC including both FR1 and FR2

###### 6.2B.4.2.5.1 ΔTIB,c for EN-DC three bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.2-1, ΔTIB,c for constituent FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 6.2B.4.2.3.

Table 6.2B.4.2.5.1-1: Void

###### 6.2B.4.2.5.2 ΔTIB,c for EN-DC four bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.3-1, ΔTIB,c for constituent FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 6.2B.4.2.3.

###### 6.2B.4.2.5.3 ΔTIB,c for EN-DC five bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.4-1, ΔTIB,c for constituent FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA and FR1 NR bands   is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 6.2B.4.2.3.

###### 6.2B.4.2.5.4 ΔTIB,c for EN-DC six bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.5-1, ΔTIB,c for constituent FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 6.2B.4.2.3.

### 6.2B.5 Configured output power for NR-DC

#### 6.2B.5.1 Configured output power level

##### 6.2B.5.1.1 Inter-band NR-DC between FR1 and FR2

For both synchronous and non-synchronous inter-band NR-DC [12] with MCG in FR1 and SCG in FR2 combined with one uplink serving cell per CG, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of CG i, i = 1,2 as specified in clause 6.2.4 of TS 38.101-1 [2] and clause 6.2.4 TS 38.101-2 [3] independently.

For inter-band NR-DC between FR1 and FR2 with a single uplink component carrier configured in FR1, when the powerBoostPi2BPSK-r18 or powerBoostQPSK-r18 is set to 1 for a UE supporting the capability of powerBoosting-pi2BPSK-QPSK-Modified-r18 or powerBoosting-pi2BPSK-QPSK-r18, the configured maximum output power PCMAX,c  on serving cell c shall be set as specified for PCMAX,f,c in clause 6.2.4.

## 6.2E Transmitter power for V2X in FR1

### 6.2E.1 UE maximum output power for V2X

#### 6.2E.1.1 UE maximum output power for Intra-band contiguous V2X

For intra-band contiguous V2X operating UE, the allowed UE maximum output power shall be applied in Table 6.2.2-1 [4] for E-UTRA SL transmission or applied in Table 6.2.1-1 [2] for NR SL transmission, respectively.

Table 6.2E.1.1-1: Maximum output power for V2X combination (continuous sub-blocks)

| V2X configuration | Power class 2(dBm) | Tolerance(dB) | Power class 3(dBm) | Tolerance(dB) |
| --- | --- | --- | --- | --- |
| V2X_(n)47AA |  |  | 23 | +2/-31 |
| NOTE 1: If all transmitted resource blocks over all component carriers are confined within FUL_low and FUL_low + 4 MHz or/and FUL_high – 4 MHz and FUL_high, the maximum output power requirement is relaxed by reducing the lower tolerance limit by 1.5 dBNOTE 2: Power Class 3 is the default power class unless otherwise stated.NOTE 3: Only single switched UL is supported |  |  |  |  |

#### 6.2E.1.2 UE maximum output power for Intra-band non-contiguous V2X

For intra-band non-contiguous V2X operating UE, the allowed UE maximum output power shall be applied in Table 6.2.2-1 [4] for E-UTRA SL transmission or applied in Table 6.2.1-1 [2] for NR SL transmission, respectively.

Table 6.2E.1.2-1: Maximum output power for V2X combination (non-contiguous sub-blocks)

| V2X configuration | Power class 2(dBm) | Tolerance(dB) | Power class 3(dBm) | Tolerance(dB) |
| --- | --- | --- | --- | --- |
| V2X_47A_n47A |  |  | 23 | +2/-31 |
| NOTE 1: If all transmitted resource blocks over all component carriers are confined within FUL_low and FUL_low + 4 MHz or/and FUL_high – 4 MHz and FUL_high, the maximum output power requirement is relaxed by reducing the lower tolerance limit by 1.5 dBNOTE 2: Power Class 3 is the default power class unless otherwise stated.NOTE 3: Only single switched UL is supported |  |  |  |  |

#### 6.2E.1.3 UE maximum output power for Inter-band V2X

For the NR V2X inter-band con-current operation, the maximum output power is specified in Table 6.2E.1.3-1 for each operating band. The period of measurement shall be at least one sub frame (1ms).

Table 6.2E.1.3-1: Con-current V2X UE Power Class

| V2X con-current operating band Configuration | NR or E-UTRA band | Class 1 (dBm) | Tolerance (dB) | Class 2 (dBm) | Tolerance(dB) | Class 3 (dBm) | Tolerance (dB) | Class 4 (dBm) | Tolerance (dB) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2X_3A_n47A | 3 |  |  |  |  | 23 | ±2 |  |  |
|  | n47 |  |  | 26 | +2/-3 | 23 | +2/-3 |  |  |
| V2X_20A_n38A | 20 |  |  |  |  | 23 | ±24 |  |  |
|  | n38 |  |  |  |  | 23 | +2/-3 |  |  |
| V2X_n39A_47A | n39 |  |  |  |  | 23 | ±2 |  |  |
|  | 47 |  |  | 26 | ±2 | 23 | ±2 |  |  |
| V2X_39A_n47A | 39 |  |  |  |  | 23 | ±2 |  |  |
|  | n47 |  |  | 26 | +2/-3 | 23 | +2/-3 |  |  |
| V2X_n40A_47A | n40 |  |  |  |  | 23 | ±2 |  |  |
|  | 47 |  |  | 26 | ±2 | 23 | ±2 |  |  |
| V2X_40A_n47A | 40 |  |  |  |  | 23 | +2/-34 |  |  |
|  | n47 |  |  | 26 | +2/-3 | 23 | +2/-3 |  |  |
| V2X_n71A_47A | n71 |  |  |  |  | 23 | +2/-2.5 |  |  |
|  | 47 |  |  | 26 | ±2 | 23 | ±2 |  |  |
| V2X_n78A_47A | n78 |  |  |  |  | 23 | +2/-34 |  |  |
|  | 47 |  |  | 26 | ±2 | 23 | ±2 |  |  |
| V2X_n79A_47A | n79 |  |  |  |  | 23 | +2/-3 |  |  |
|  | 47 |  |  | 26 | ±2 | 23 | ±2 |  |  |
| NOTE 1: For the con-current band combinations, the simultaneous transmission and reception of sidelink and Uu interfaces can be supported while operation is agnostic of the service used on each interface.NOTE 2: PPowerClass is the maximum output power specified without taking into account the tolerance for each operation band.NOTE 3: For inter-band con-current operation, the aggregation power apply to the total transmitted power over all component carriers (per UE).NOTE 4: 4 refers to the transmission bandwidths (Figure 5.6-1) confined within FUL_low and FUL_low + 4 MHz or FUL_high – 4 MHz and FUL_high, the maximum output power requirement is relaxed by reducing the lower tolerance limit by 1.5 dB |  |  |  |  |  |  |  |  |  |

### 6.2E.2 UE maximum output power reduction for V2X

#### 6.2E.2.1 UE maximum output power reduction for Intra-band V2X

For intra-band V2X operating UE, maximum output power reduction specified in clause 6.2.3G [4] and in clause 6.2E.2 [2] apply, respectively.

#### 6.2E.2.2 UE maximum output power reduction for Inter-band V2X

For the inter-band con-current NR V2X operation, the allowed maximum power reduction (MPR) for the maximum output power shall be applied per each component carrier. The MPR requirements in subclause 6.2.3 of TS 36.101 [4] apply for E-UTRA Uu operation in licensed band, and the MPR requirements in subclause 6.2E.2 of TS 38.101-1 [2] apply for NR sidelink operation. The MPR requirements in subclause 6.2.3G of TS 36.101 [4] apply for E-UTRA V2X operation, and the MPR requirements in subclause 6.2.2 of TS 38.101-1 [2] apply for NR Uu operation.

### 6.2E.3 UE additional maximum output power reduction for V2X

#### 6.2E.3.1 UE additional maximum output power reduction for Intra-band V2X

For intra-band V2X operating UE, additional maximum output power reduction specified in clause 6.2.4G [4] and in clause 6.2C.3 [2] apply, respectively.

#### 6.2E.3.2 UE additional maximum output power reduction for Inter-band V2X

For the inter-band con-current NR V2X operation, the allowed additional maximum power reduction (A-MPR) for the maximum output power shall be applied per each component carrier. The A-MPR requirements in subclause 6.2.3 of TS 36.101 [4] apply for E-UTRA Uu operation in licensed band, and the A-MPR requirements in in subclause 6.2C.3 of TS 38.101-1 [2] apply for NR sidelink operation in Band n47.

### 6.2E.4 Configured output power for V2X

#### 6.2E.4.1 UE configured output power for Intra-band V2X

For intra-band V2X operating UE, each UE configured output power specified in clause 6.2.5G [4] and in clause 6.2E.4 [2] apply, respectively.

#### 6.2E.4.2 UE configured output power for Inter-band V2X

When a UE is configured for simultaneous NR V2X sidelink and NR uplink transmissions for inter-band con-current operation, the UE is allowed to set its configured maximum output power PCMAX,c,Uu and PCMAX,c,V2X for the configured E-UTRA or NR uplink carrier and the configured NR V2X SL or E-UTRA V2X SL carrier, respectively, and its total configured maximum output power PCMAX,c. The TIB,V2X of PCMAX,c,Uu is specified in Table 6.2E.4.2-1.

The configured maximum output power PCMAX c,Uu(p) in subframe p for the configured E-UTRA or NR uplink carrier shall be set within the bounds:

PCMAX_L,c, Uu (p) ≤  PCMAX,c, Uu (p) ≤  PCMAX_H,c, Uu (p)

where PCMAX_L,c,Uu and PCMAX_H,c, Uu are the limits for a serving cell c as specified in subclause 6.2.5 TS 36.101 [4] or 6.2.4 TS 38.101-1 [2].

The configured maximum output power PCMAX c,V2X (q) in slot q for the configured NR or E-UTRA V2X SL carrier shall be set within the bounds:

PCMAX,c,V2X (q) ≤  PCMAX_H,c,V2X (q)

where PCMAX_H,c,V2X is the limit as specified in subclause 6.2E.4 of TS 38.101-1 [2] or 6.2.5G of TS 36.101 [5].

The total UE configured maximum output power PCMAX (p,q) in a subframe p of E-UTRA uplink carrier and a slot q of NR V2X sidelink that overlap in time shall be set within the following bounds for synchronous and asynchronous operation unless stated otherwise:

PCMAX_L (p,q) ≤  PCMAX (p,q)  ≤  PCMAX_H (p,q)

with

PCMAX_L (p,q) =  PCMAX_L,c,Uu (p)

PCMAX_H (p,q) = 10 log10 [pCMAX_H,c, Uu (p) + pCMAX_H,c,V2X (q)]

where pCMAX_H,c,V2X and pCMAX_H,c,Uu are the limits PCMAX_H,c,V2X (q) and PCMAX_H,c,Uu (p) expressed in linear scale.

The measured total maximum output power PUMAX over both the E-UTRA uplink and NR V2X carriers is

PUMAX = 10 log10 [pUMAX,c,Uu + pUMAX,c,V2X],

where pUMAX,c,Uu  denotes the measured output power of serving cell c for the configured E-UTRA uplink carrier or NR uplink carrier, and pUMAX,c,V2X  denotes the measured output power for the configured NR V2X SL carrier or E-UTRA V2X SLcarrier expressed in linear scale.

When a UE is configured for synchronous V2X sidelink and uplink transmissions,

PCMAX_L(p, q)   –  TLOW (PCMAX_L(p, q))  ≤  PUMAX  ≤  PCMAX_H(p, q)  + THIGH (PCMAX_H(p, q))

where PCMAX_L (p,q) and PCMAX_H (p,q) are the limits for the pair (p,q) and with the tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX specified in Table 6.2E.4-1. PCMAX_L may be modified for any overlapping portion of slots (p, q) and (p +1, q+1).

Table 6.2E.4.2-1: ΔTIB,V2X for inter-band con-current V2X operation (two bands)

| V2X con-current operating band Configuration | Operating Band | ΔTIB,V2X [dB] |
| --- | --- | --- |
| V2X_20A_n38A | 20 | 0.01 |
| Note 1: The ΔTIB,V2X is applied on top of ΔTIB,c of DC_20A_n38A UE that is considered harmonic trap filter to reduce 3rd harmonic impact from Band 20. |  |  |

## 6.2H Transmitter power for DC with UL MIMO

### 6.2H.1 UE maximum output power for DC with UL MIMO

#### 6.2H.1.1 void

#### 6.2H.1.2 void

#### 6.2H.1.3 Inter-band EN-DC with UL MIMO within FR1

For inter-band EN-DC of E-UTRA and NR in FR1, the following UE Power Classes define the maximum output power for any transmission bandwidth within the aggregated channel bandwidth. The maximum output power is measured as the sum of the maximum output power at each UE antenna connector. The period of measurement shall be at least one sub frame (1ms). UE maximum output power shall be measured over all component carriers from different bands. If each band has separate antenna connectors, maximum output power is measured as the sum of maximum output power at each UE antenna connector.

The maximum output power for inter-band EN-DC with one Tx in E-UTRA band and 2Tx in NR band is specified in Table 6.2H.1.3-1. The per band power class for each band applicable to REFSENS exceptions for a given inter-band UL EN-DC power class are specified in Table 6.2H.3.1-1a. These configurations are subject to the applicable power class of each E-UTRA band and NR band specified in Table 6.2.2-1 of TS 36.101 and Table 6.2D.1-1 of TS 38.101-1 respectively.The power classes referenced are according to the reported ue-PowerClass-N-r13 for the E-UTRA band or ue-CA-PowerClass-N for the E-UTRA intra-band UL CA of the EN-DC combination, and reported powerClassNRPart-r16 for the NR band and for NR intra-band UL CA of the EN-DC combination if indicated or ue-PowerClass otherwise.

If higherPowerLimitMRDC-r17 is indicated for an UL inter-band EN-DC configuration as specified in Table 6.2H.1.3-1 and with uplink bands of different power class capabilities, the UE maximum output power specified in Table 6.2H.1.3-1 for this UL EN-DC configuration is modified in accordance with sub-clause 6.2H.4.1.3.

Table 6.2H.1.3-1: Maximum output power for inter-band EN-DC with UL MIMO and/or TxD (two bands)

| EN-DC configuration | Power class 1.5(dBm) | Tolerance(dB) | Power class 2(dBm) | Tolerance(dB) | Power class 3(dBm) | Tolerance(dB) |
| --- | --- | --- | --- | --- | --- | --- |
| DC_1A_n78A |  |  | 265 | +2/-3 | 23 | +2/-3 |
| DC_3A_n78A |  |  | 265 | +2/-3 | 23 | +2/-3 |
| DC_5A_n78A |  |  | 265 | +2/-3 | 23 | +2/-3 |
| DC_7A_n78A |  |  | 265 | +2/-3 | 23 | +2/-3 |
| DC_8A_n78A |  |  | 265 | +2/-3 | 23 | +2/-3 |
| DC_20A_n78A |  |  | 265 | +2/-3 | 23 | +2/-3 |
| DC_28A_n78A |  |  | 265 | +2/-3 | 23 | +2/-3 |
| DC_40A_n78A |  |  | 265 | +2/-3 | 23 | +2/-3 |
| DC_41A_n78A |  |  | 265 | +2/-3 | 23 | +2/-3 |
| NOTE 1: An uplink DC configuration in which at least one of the bands has NOTE 3 in Table 6.2.1-1 in TS 38.101-1 or NOTE 2 in Table 6.2.2-1 in TS 36.101 is allowed to reduce the lower tolerance limit by 1.5 dB when the transmission bandwidths of at least one of the bands is confined within FUL_low and FUL_low + 4 MHz or FUL_high - 4 MHz and FUL_high.NOTE 2: PPowerClass, EN-DC is the maximum UE power specified without taking into account the toleranceNOTE 3: For inter-band EN-DC the maximum power requirement should apply to the total transmitted power over all component carriers (per UE).NOTE 4: Power Class 3 is the default power class unless otherwise stated.NOTE 5:  The UE supports PC3 in E-UTRA band, and supports PC3 or PC2 with UL MIMO and/or TxD in NR bandNOTE 6:  VoidNOTE 7:   Void |  |  |  |  |  |  |

Table 6.2H.1.3-1a: Per band power class applicable to REFSENS exceptions (two band UL EN-DC)

| Inter-band Power class(NOTE 1) | Uplink bands of same power class |  | Uplink bands of different power class |  |
| --- | --- | --- | --- | --- |
|  | E-UTRA band2 | NR band | E-UTRA band2 | NR band |
| Class 3 | Class 3 | Class 3 |  |  |
| Class 2 | Class 3 | Class 3 | Class 3 | Class 2 |
|  | Class 2 | Class 2 | Class 2 | Class 3 |
| Class 1.5 | Class 2 | Class 2 | Class 3 | Class 1.5 |
|  |  |  | Class 2 | Class 1.5 |
| NOTE 1: Indicated by powerClass/powerClass-v1610.NOTE 2: For the FDD E-UTRA band, only Class 3 is applicable. |  |  |  |  |

If a UE supports power class 2 for an E-UTRA TDD and NR TDD Inter-band EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 30% when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power of the default power class or lower;

– shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified sub-clause 6.2H.4;

– Else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS 38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present; or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 30% when maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent. (The exact evaluation period is no less than one radio frame):

– shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2H.4.

If a UE supports power class 1.5 for an E-UTRA TDD and NR TDD Inter-band EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 15% when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power of the default power class or lower;

– shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified sub-clause 6.2H.4;

– Else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.25*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 but less than or equal to 0.5*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS 38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present; or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 7.5% but less than or equal to 15% when maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent. (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power between 23dBm and 26dBm;

– shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2H.4.

– Else

– shall apply all requirements for the power class 1.5 and set the configured transmitted power class as specified in sub-clause 6.2H.4.

If a UE supports power class 2 for an E-UTRA FDD and NR TDD EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

If UE indicating the two capabilities maxUplinkDutyCycle-FDD-TDD-EN-DC1 and maxUplinkDutyCycle-FDD-TDD-EN-DC2:

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal tomaxUplinkDutyCycle-FDD-TDD-EN-DC1as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

– shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2H.4.

– else

– shall apply all requirements for the default power class and set the configured transmitted power as specified sub-clause 6.2H.4;

else

– shall apply all requirements for the power class 2 and set the configured transmitted power as specified sub-clause 6.2H.4;

If a UE supports power class 1.5 for an E-UTRA FDD and NR TDD EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

If UE indicating the two capabilities maxUplinkDutyCycle-FDD-TDD-EN-DC1 and maxUplinkDutyCycle-FDD-TDD-EN-DC2:

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC1as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

– shall apply all requirements for the power class 1.5 and set the configured transmitted power class as specified in sub-clause 6.2H.4.

– else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC1 but less than or equal to 1.0*maxUplinkDutyCycle-FDD-TDD-EN-DC1 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC2 but less than or equal to 1.0*maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

– shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2H.4.

– else

– shall apply all requirements for the default power class and set the configured transmitted power as specified sub-clause 6.2H.4;

else

– shall apply all requirements for the power class 1.5 and set the configured transmitted power as specified sub-clause 6.2H.4;

### 6.2H.2 UE maximum output power reduction for DC with UL MIMO

#### 6.2H.2.1 void

#### 6.2H.2.2 void

#### 6.2H.2.3 Inter-band EN-DC with UL MIMO within FR1

For inter-band EN-DC between E-UTRA and FR1 NR, UE maximum output power reduction specified in TS 36.101 [4] and TS 38.101-1 [2] apply for E-UTRA and NR respectively.

### 6.2H.3 UE additional maximum output power reduction for EN-DC with UL MIMO

#### 6.2H.3.1 void

#### 6.2H.3.2 void

#### 6.2H.3.3 Inter-band EN-DC with UL MIMO within FR1

For inter-band EN-DC with UL MIMO in NR band, unless specified in Table 6.2B.3.3-1, the requirements in [2] clause 6.2.3 apply for NR uplink component carrier and the requirements in [4] clause 6.2.4 apply for LTE uplink component carrier.

### 6.2H.4 Configured output power for DC with UL MIMO

#### 6.2H.4.1 Configured output power level

##### 6.2H.4.1.1 void

##### 6.2H.4.1.2 void

6.2H.4.1.3 Inter-band EN-DC with UL MIMO within FR1

For inter-band EN-DC with UL MIMO in one NR band, the requirements in clause 6.2B.4.1.3 apply except that:

- PPowerClass,EN-DC is the maximum UE power specified in Table 6.2H.1.3-1 without taking into account the tolerance; if the UE indicates higherPowerLimitMRDC-r17 for an UL inter-band EN-DC configuration with uplink bands of different power class capabilities specified in Table 6.2H.1.3-1 and ΔPPowerClass,EN-DC = 0, PPowerClass,EN-DC is replaced by the sum of the linear powers of PPowerClass,NR and PPowerClass,E-UTRA converted to dBm;

- If the NR component carrier is configured with UL MIMO, the MPRc and A-MPRc are specified in clause 6.2D.2 and clause 6.2D.3 of [2] respectively.

- ∆PPowerClass,EN-DC:

– For a power class 2 capable UE, it is 3dB when the requirements of default power class are applied as specified in sub-clause 6.2H.1.3, otherwise ΔPPowerClass,EN-DC = 0 dB;

## 6.2L Transmitter power for DC with Tx Diversity

### 6.2L.1 UE maximum output power for DC with Tx Diversity

#### 6.2L.1.1 void

#### 6.2L.1.2 void

#### 6.2L.1.3 Inter-band EN-DC with Tx Diversity within FR1

For inter-band EN-DC of E-UTRA and NR in FR1, the UE Power Classes in table 6.2H.1.3 define the maximum output power for any transmission bandwidth within the aggregated channel bandwidth. The maximum output power is measured as the sum of the maximum output power at each UE antenna connector. The period of measurement shall be at least one sub frame (1ms). UE maximum output power shall be measured over all component carriers from different bands. If each band has separate antenna connectors, maximum output power is measured as the sum of maximum output power at each UE antenna connector. The per band power class for each band applicable to REFSENS exceptions for a given inter-band UL EN-DC power class are specified in Table 6.2H.3.1-1a. These configurations are subject to the applicable power class of each E-UTRA band and NR band specified in Table 6.2.2-1 of TS 36.101 and Table 6.2.1-1 of TS 38.101-1 respectively. The power classes referenced are according to the reported ue-PowerClass-N-r13 for the E-UTRA band or ue-CA-PowerClass-N for the E-UTRA intra-band UL CA of the EN-DC combination, and reported powerClassNRPart-r16 for the NR band and for NR intra-band UL CA of the EN-DC combination if indicated or ue-PowerClass otherwise.

If higherPowerLimitMRDC-r17 is indicated for an UL inter-band EN-DC configuration with Tx Diversity as specified in Table 6.2H.1.3-1 and with uplink bands of different power class capabilities, the UE maximum output power specified in Table 6.2H.1.3-1 for EN-DC configuration is increased in accordance with sub-clause 6.2L.4.1.3.

If a UE supports power class 2 for an E-UTRA TDD and NR TDD Inter-band EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 30% when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power of the default power class or lower;

– shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified sub-clause 6.2L.4;

– Else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS 38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present; or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 30% when maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent. (The exact evaluation period is no less than one radio frame):

– shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2L.4.

If a UE supports power class 1.5 for an E-UTRA TDD and NR TDD Inter-band EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 15% when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power of the default power class or lower;

– shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified sub-clause 6.2L.4;

– Else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.25*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 but less than or equal to 0.5*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS 38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present; or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 7.5% but less than or equal to 15% when maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent. (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power between 23dBm and 26dBm;

– shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2L.4.

– Else

– shall apply all requirements for the power class 1.5 and set the configured transmitted power class as specified in sub-clause 6.2L.4.

If a UE supports power class 2 for an E-UTRA FDD and NR TDD EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

If UE indicating the two capabilities maxUplinkDutyCycle-FDD-TDD-EN-DC1 and maxUplinkDutyCycle-FDD-TDD-EN-DC2:

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal tomaxUplinkDutyCycle-FDD-TDD-EN-DC1as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

– shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2L.4.

– else

– shall apply all requirements for the default power class and set the configured transmitted power as specified sub-clause 6.2L.4;

else

– shall apply all requirements for the power class2  and set the configured transmitted power as specified sub-clause 6.2L.4;

If a UE supports power class 1.5 for an E-UTRA FDD and NR TDD EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

If UE indicating the two capabilities maxUplinkDutyCycle-FDD-TDD-EN-DC1 and maxUplinkDutyCycle-FDD-TDD-EN-DC2:

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC1as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

– shall apply all requirements for the power class 1.5 and set the configured transmitted power class as specified in sub-clause 6.2L.4.

– else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC1 but less than or equal to 1.0*maxUplinkDutyCycle-FDD-TDD-EN-DC1 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

– if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC2 but less than or equal to 1.0*maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

– shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2L.4.

– else

– shall apply all requirements for the default power class and set the configured transmitted power as specified sub-clause 6.2L.4;

else

– shall apply all requirements for the power class 1.5 and set the configured transmitted power as specified sub-clause 6.2L.4;

### 6.2L.2 UE maximum output power reduction for DC with Tx Diversity

#### 6.2L.2.1 void

#### 6.2L.2.2 void

#### 6.2L.2.3 Inter-band EN-DC with Tx Diversity within FR1

For inter-band EN-DC between E-UTRA and FR1 NR, UE maximum output power reduction specified in TS 36.101 [4] and TS 38.101-1 [2] apply for E-UTRA and NR respectively.

### 6.2L.3 UE additional maximum output power reduction for EN-DC with Tx Diversity

#### 6.2L.3.1 void

#### 6.2L.3.2 void

#### 6.2L.3.3 Inter-band EN-DC with Tx Diversity within FR1

For inter-band EN-DC with Tx Diversity in one NR band, unless specified in Table 6.2B.3.3-1, the requirements in [2] clause 6.2.3 apply for NR uplink component carrier and the requirements in [4] clause 6.2.4 apply for LTE uplink component carrier.

### 6.2L.4 Configured output power for DC with Tx Diversity

#### 6.2L.4.1 Configured output power level

##### 6.2L.4.1.1 void

##### 6.2L.4.1.2 void

6.2L.4.1.3 Inter-band EN-DC with Tx Diversity within FR1

For inter-band EN-DC with Tx Diversity in one NR band, the requirements in clause 6.2B.4.1.3 apply except that:

- PPowerClass,EN-DC is the maximum UE power specified in Table 6.2H.1.3-1 without taking into account the tolerance; if the UE indicates higherPowerLimitMRDC-r17 for an UL inter-band EN-DC configuration with uplink bands of different power class capabilities specified in Table 6.2H.1.3-1 and ΔPPowerClass,EN-DC = 0, PPowerClass,EN-DC is replaced by the sum of the linear powers of PPowerClass,NR and PPowerClass,E-UTRA converted to dBm;

- If the NR component carrier is configured with Tx Diversity, the MPRc and A-MPRc are specified in clause 6.2G.2 and clause 6.2G.3 of [2] respectively.

- ∆PPowerClass,EN-DC:

– For a power class 2 capable UE, it is 3dB when the requirements of default power class are applied as specified in sub-clause 6.2L.1.3, otherwise ΔPPowerClass,EN-DC = 0 dB;

## 6.3 Output power dynamics

Output power dynamics for EN-DC operations in FR1 and FR2 as specified in TS 38.101-1 [2] and TS 38.101-2 [3], respectively. E-UTRA as specified in TS 36.101 [4]. For intra-band contiguous EN-DC operation in FR1, minimum output power requirements specified in clause 6.3.1 of TS 38.101-1 [2] and clause 6.3.2 of TS 36.101 [4] shall only apply when the power of all NR and E-UTRA carriers are set to minimum value. Similarly, OFF power requirements specified in clause 6.3.2 of TS 38.101-1 [2] and clause 6.3.3 of TS 36.101 [4] shall only apply when the power of all NR and E-UTRA carriers are OFF. The OFF power condition in transmit ON/OFF time mask requirements specified in clause 6.3.3 of TS 38.101-1 [2] and clause 6.3.4 of TS 36.101 [4] is applicable only when all NR and E-UTRA carriers are OFF. If both E-UTRA and NR transition between ON and OFF states simultaneously, the longer transient time shall apply to both. If either E-UTRA or NR is OFF and the other carrier transitions from OFF to ON, then the transiet time associated with that carrier applies.

## 6.3A Output power dynamics for CA

For inter-band NR CA between FR1 and FR2, output power dynamics as specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for FR1 and FR2 respectively.

6.3B Output power dynamics for DC

### 6.3B.0 General

The E-UTRA and NR switching time mask defines the observation period between E-UTRA subframe and NR slot/mini-slot boundary. Both E-UTRA subframe and NR slot/mini-slot have ON power transmissions. The ON power is defined as the mean power over the symbol duration excluding any transient period. For E-UTRA subframe or NR slot/mini-slot having OFF power transmission, the general time mask for E-UTRA or NR shall apply.

For inter-band EN-DC or NE-DC, output power dynamics requirement for E-UTRA single carrier and CA operation specified in clauses 6.3 and 6.3A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.3 and 6.3A of TS 38.101-1 [2] and  for NR single carrier, CA operation and UL-MIMO specified in clause 6.3, 6.3A and 6.3D of TS 38.101-2 [3] apply.

### 6.3B.1 Output power dynamics for EN-DC with UL sharing from UE perspective

#### 6.3B.1.1 E-UTRA and NR switching time mask for TDM based UL sharing from UE perspective

The E-UTRA and NR switching time mask is applicable for non-simultaneous transmissions between E-UTRA and NR in TDM based UL sharing from the UE perspective in the same channel, which is shared by E-UTRA and NR. The requirement applies on the condition that UE is capable of handling the uplink transmission timing difference between E-UTRA and NR which is less than or equal to [2.21]μs.

For UEs reporting E-UTRA and NR switching time capability of type 1 with switching time < 0.5 us for TDM based UL sharing from UE perspective within FR1 time masks in Figure 6.3B.1.1-1 and Figure 6.3B.1.1-2 shall apply. For UEs reporting E-UTRA and NR switching time capability of type 2 with switching time < 20 us for TDM based UL sharing from UE perspective within FR1, time masks in Figure 6.3B.1.1-3 and Figure 6.3B.1.1-4 shall apply. The additional time for the transient period on the succeeding E-UTRA subframe or NR slot is caused by the uplink transmission timing difference, for which the maximum value is [2.21]μs.

Figure 6.3B.1.1-1: E-UTRA to NR switching time mask for type 1 for TDM based UL sharing from UE perspective within FR1

Figure 6.3B.1.1-2: NR to E-UTRA switching time mask for type 1 for TDM based UL sharing from UE perspective within FR1

Figure 6.3B.1.1-3: E-UTRA to NR switching time mask for type 2 for TDM based UL sharing from UE perspective within FR1

Figure 6.3B.1.1-4: NR to E-UTRA switching time mask for type 2 for TDM based UL sharing from UE perspective within FR1

### 6.3B.1a (Void)

### 6.3B.2 Output power dynamics for intra-band EN-DC without dual PA capability

For intra-band contiguous and intra-band non-contiguous EN-DC configurations without dual PA capability, maximum UL switching time is defined as 120 us and DL reception interruption is allowed during UL switching. Time masks in Figure 6.3B.2-1 and Figure 6.3B.2-2 shall apply.

Figure 6.3B.2-1: E-UTRA to NR switching time mask for intra-band EN-DC without dual PA capabilitywhen single UL is allowed

Figure 6.3B.2-2: NR to E-UTRA switching time mask for intra-band EN-DC without dual PA capabilitywhen single UL is allowed

### 6.3B.2a (Void)

### 6.3B.3 Output power dynamics for intra-band EN-DC with dual PA capability

For both intra-band contiguous and non-contiguous EN-DC with dual PA capability, time masks in Figure 6.3B.3-1 and Figure 6.3B.3-2 shall apply.

Figure 6.3B.3-1: E-UTRA to NR switching time mask for intra-band EN-DC with dual PA capability

Figure 6.3B.3-2: NR to E-UTRA switching time mask for intra-band EN-DC with dual PA capability

### 6.3B.3a (Void)

### 6.3B.4 Output power dynamics for switching between two uplink carriers

#### 6.3B.4.1 E-UTRA and NR switching time mask between two uplink carriers

In addition to the requirements in 6.3B.0 and the maximum output power requirement specified in Table 6.2B.1.3-1 with inter-band EN-DC (two bands), the switching time mask specified in this sub-clause is applicable for an uplink band pair of a inter-band EN-DC configuration without SUL band when the capability uplinkTxSwitchingPeriod is present, and is only applicable for uplink switching mechanisms specified in sub-clause 6.1.6 of TS 38.214 [14], where E-UTRA UL carrier 1 is capable of one transmit antenna connector and NR UL carrier 2 is capable of two transmit antenna connectors, and the two uplink carriers are in different bands with different carrier frequencies. The UE shall support the switch between single layer transmission with one antenna port and two-layer transmission with two antenna ports on the two uplink carriers following the scheduling commands and rank adaptation, i.e., both single layer and two-layer transmission with 2 antenna ports, and single layer transmission with 1 antenna port shall be supported on NR UL carrier 2 as specified in [38.306].

The switching periods described in Figure 6.3B.4.1-1 are only located in NR carrier, and the length of uplink switching period X is less than the value indicated by UE capability uplinkTxSwitchingPeriod.

When switching from one carrier to another, if there is no uplink transmission scheduled or configured on the switch-from carrier for at least the duration of the switching period (X µs) before the point in time the UE is scheduled or configured to start the transmission on the switch-to carrier, the switching period is fully contained in the time period between the end of the transmission on the switch-from carrier and the start of the transmission on the switch-to carrier. In addition, the RRC signalling uplinkTxSwitchingPeriodLocation is ignored by the UE.

Figure 6.3B.4.1-1: Time mask for switching between E-UTRA UL carrier and NR UL carrier, where the switching period is located in NR carrier

The following applies for the uplink switching cases specified in clause 6.1.6.1 of [14] with uplinkTxSwitchingOption set to either switchedUL or dualUL when the configuration of the location of the switching period by uplinkTxSwitchingPeriodLocation is ignored by the UE:

- if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [14] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the uplink switching gap indicated by uplinkTxSwitchingPeriod on any of the carriers before T0, transient periods of 10 s are located at the end of the last symbol(s) configured or scheduled on the carriers before T0 and at the start of the first symbol(s) configured or scheduled or configured at T0.

The requirements apply for the case of co-located and synchronized network deployment with the max receiving timing difference of 3us between the two carriers.

The time mask is applicable to uplink transmissions when configured with switchedUL or dualUL.

### 6.3B.5 Output power dynamics for inter-band EN-DC

The switching time mask defined in this clause is applicable for a UE indicating support of IE singleUL-Transmission for the specific inter-band EN-DC combination for which only single switched UL is supported . The maximum UL switching time is defined as 120 us. Time masks in Figure 6.3B.5-1 and Figure 6.3B.5-2 shall apply.

Figure 6.3B.5-1: E-UTRA to NR switching time mask for inter-band EN-DC when only single switched UL is supported

Figure 6.3B.5-2: NR to E-UTRA switching time mask for inter-band EN-DC when only single switched UL is supported

## 6.3E Output power dynamics for V2X

### 6.3E.1 General

The E-UTRA SL and NR SL switching time mask defines the observation period between E-UTRA subframe and NR slot/mini-slot boundary. Both E-UTRA subframe and NR slot/mini-slot have ON power transmissions. The ON power is defined as the mean power over the symbol duration excluding any transient period. For E-UTRA subframe or NR slot/mini-slot having OFF power transmission, the general time mask for E-UTRA or NR shall apply.

### 6.3E.2 Output power dynamics for intra-band V2X operation

For intra-band V2X operation bands specified in subclause 5.3E.1 and 5.3E.2, the SL switching time masks in Figure 6.3E.2-1 shall apply.

The switching time shall be located on the RAT of lower priority when NR SL and LTE SL have different priorities based on priority information specified in TS 38.213. It is up to UE implementation when NR SL and LTE SL have the same priority based on priority information specified in TS 38.213.

![](media/捕获123.PNG)

Figure 6.3E.2-1: Time mask for switching between NR SL and E-UTRA SL

### 6.3E.3 Output power dynamics for inter-band V2X con-current operation

For inter-band con-current NR V2X operation, the output power dynamics requirement shall be applied per each component carrier. The output dynamic requirements specified in clause 6.3 of TS 36.101 [4] apply for E-UTRA UL transmission and the requirements specified in clause 6.3E of TS 38.101-1 [2] apply for NR SL transmission. The output dynamic requirements specified in clause 6.3.2G, 6.3.3G, 6.3.4G of TS 36.101 [4] apply for E-UTRA SL transmission and the requirements specified in clause 6.3 of TS 38.101-1 [2] apply for NR UL transmission.

6.3H Output power dynamics for DC with UL MIMO


### 6.3H.0 General

The E-UTRA and NR switching time mask defines the observation period between E-UTRA subframe and NR slot/mini-slot boundary. Both E-UTRA subframe and NR slot/mini-slot have ON power transmissions. The ON power is defined as the mean power over the symbol duration excluding any transient period. For E-UTRA subframe or NR slot/mini-slot having OFF power transmission, the general time mask for E-UTRA or NR shall apply.

For inter-band EN-DC with UL MIMO, output power dynamics requirement for E-UTRA single carrier operation specified in clauses 6.3 of TS 36.101 [4] and for NR single carrier with UL MIMO operation specified in clause 6.3D of TS 38.101-1 [2] apply.

### 6.3H.1 void

### 6.3H.2 void

### 6.3H.3 Output power dynamics for inter-band EN-DC with UL MIMO

For a UE indicating support of IE singleUL-Transmission for the specific inter-band EN-DC combination with UL MIMO for which only single switched UL is supported, the requirements defined in 6.3B.5 apply.

6.3L Output power dynamics for DC with Tx Diversity

### 6.3L.0 General

The E-UTRA and NR switching time mask defines the observation period between E-UTRA subframe and NR slot/mini-slot boundary. Both E-UTRA subframe and NR slot/mini-slot have ON power transmissions. The ON power is defined as the mean power over the symbol duration excluding any transient period. For E-UTRA subframe or NR slot/mini-slot having OFF power transmission, the general time mask for E-UTRA or NR shall apply.

For inter-band EN-DC with Tx Diversity, output power dynamics requirement for E-UTRA single carrier operation specified in clauses 6.3 of TS 36.101 [4] and for NR single carrier with Tx Diversity operation specified in clause 6.3D of TS 38.101-1 [2] apply.

### 6.3L.1 void

### 6.3L.2 void

### 6.3L.3 Output power dynamics for inter-band EN-DC with Tx Diversity

For a UE indicating support of IE singleUL-Transmission for the specific inter-band EN-DC combination with Tx Diversity for which only single switched UL is supported, the requirements defined in 6.3B.5 apply.

## 6.4 Void

## 6.4A Transmit signal quality for CA

### 6.4A.1 Frequency error for CA

For inter-band NR CA between FR1 and FR2, frequency error as specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for FR1 and FR2 respectively.

### 6.4A.2 Transmit modulation quality for CA

For inter-band NR CA between FR1 and FR2, transmit modulation quality as specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for FR1 and FR2 respectively.

DMRS bundling requirements, as specified in clause 6.4.2.5 in TS 38.101-1 [2] and clause 6.4.2.6 in TS 38.101-2 [3], apply when one uplink band and CC is configured for DMRS bundling at a time. If UE needs to apply P-MPR as described in 6.2.4 of TS 38.101-1 or TS 38.101-2 during a granted DMRS bundle on any uplink CC, phase continuity is not expected to be maintained in the bundle.

## 6.4B Transmit signal quality for DC

### 6.4B.1 Frequency error for DC

#### 6.4B.1.1 Frequency error for Intra-band contiguous EN-DC

For intra-band contiguous EN-DC, the requirement shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4.1 in TS 38.101-1 [2], respectively.

#### 6.4B.1.1a Frequency error for Intra-band contiguous NE-DC

For intra-band contiguous NE-DC, the requirement shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4.1 in TS 38.101-1 [2], respectively.

#### 6.4B.1.2 Frequency error for Intra-band non-contiguous EN-DC

For intra-band non-contiguous EN-DC, the requirement shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4.1 in TS 38.101-1 [2], respectively.

#### 6.4B.1.3 Frequency error for inter-band EN-DC within FR1

For inter-band EN-DC with uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4.1 in TS 38.101-1 [2], respectively, with all component carriers active. If multiple component carriers are assigned to one E-UTRA band, the requirements in clauses 6.5.1A in TS 36.101 [4] apply for those component carriers.

#### 6.4B.1.3a Frequency error for inter-band NE-DC within FR1

For inter-band NE-DC with uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4.1 in TS 38.101-1 [2], respectively, with all component carriers active. If multiple component carriers are assigned to one E-UTRA band, the requirements in clauses 6.5.1A in TS 36.101 [4] apply for those component carriers, and if multiple component carriers are assigned to one NR band, the requirements in clauses 6.4A.1 in TS 38.101-1 [2] apply for those component carriers.

#### 6.4B.1.4 Frequency error for inter-band EN-DC including FR2

Frequency error requirement for E-UTRA single carrier and CA operation specified in clauses 6.5.1 and 6.5.1A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.4.1, 6.4A.1 and 6.4D.1 of TS 38.101-2 [3] apply.

#### 6.4B.1.4a (Void)

#### 6.4B.1.5 Frequency error for inter-band EN-DC including both FR1 and FR2

Frequency error requirement for E-UTRA single carrier and CA operation specified in clauses 6.5.1 and 6.5.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.4.1 and 6.4A.1 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.4.1, 6.4A.1 and 6.4D.1 of TS 38.101-2 [3] apply.

### 6.4B.2 Transmit modulation quality for DC

#### 6.4B.2.1 Transmit modulation quality for Intra-band contiguous EN-DC

##### 6.4B.2.1.1 Error Vector Magnitude

For the intra-band contiguous EN-DC with one component carrier per CG the EVM requirement applies with PRB allocation in one of the CG and the other CG unallocated.

The EVM requirements for each CG are according to clause 6.5.2 of TS 36.101 [4] for the MCG and 6.4.2 of TS38.101-1 [2] for the SCG with EN-DC configured.

##### 6.4B.2.1.2 Carrier leakage

The carrier leakage requirements for each CG are according to clause 6.5.2 of TS 36.101 [4] for the MCG and 6.4.2 of TS 38.101-1 [2] for the SCG with EN-DC configured.

##### 6.4B.2.1.3 In-band emissions

For the MCG the in-band emission requirments in Table 6.5.2A.3.1-1 and 6.5.2A.3.1-2 in TS 36.101 [4] apply within the aggregated transmission bandwidth configuration of the EN-DC bandwidth with the carriers of both CGs active and one single contiguous PRB allocation of bandwidth LCRB within the MCG at the edge of the said aggregated transmission bandwidth configuration.

For the SCG the in-band emission requirements in Table 6.4.2.3-1 in TS 38.101-1 [2] apply within the aggregated transmission bandwidth configuration of the EN-DC bandwidth with the carriers of both CGs active and one single contiguous PRB allocation of bandwidth LCRB within the SCG at the edge of the aggregated transmission bandwidth configuration.

#### 6.4B.2.1a Transmit modulation quality for Intra-band contiguous NE-DC

##### 6.4B.2.1a.1 Error Vector Magnitude

For the intra-band contiguous NE-DC with one component carrier per CG the EVM requirement applies with PRB allocation in one of the CG and the other CG unallocated.

The EVM requirements for each CG are according to clause 6.4.2 of TS 38.101-1 [2] for the MCG and 6.5.2 of TS 36.101 [4] for the SCG with NE-DC configured.

##### 6.4B.2.1a.2 Carrier leakage

The carrier leakage requirements for each CG are according to clause 6.4.2 of TS 38.101-1 [2] for the MCG and 6.5.2 of TS 36.101 [4] for the SCG with NE-DC configured.

##### 6.4B.2.1a.3 In-band emissions

For the MCG the in-band emission requirements in Table 6.4.2.3-1 in TS 38.101-1 [2] are applied within the aggregated transmission bandwidth configuration of the NE-DC bandwidth with the carriers of both CGs active and one single contiguous PRB allocation of bandwidth LCRB within the MCG at the edge of the aggregated transmission bandwidth configuration.

For the SCG the in-band emission requirements in Table 6.5.2A.3.1-1 and 6.5.2A.3.1-2 in TS 36.101 [4] are applied, within the aggregated transmission bandwidth configuration of the NE-DC bandwidth with the carriers of both CGs active and one single contiguous PRB allocation of bandwidth LCRB within the SCG at the edge of the said aggregated transmission bandwidth configuration.

#### 6.4B.2.2 Transmit modulation quality for Intra-band non-contiguous EN-DC

##### 6.4B.2.2.1 Error Vector Magnitude

For the intra-band non-contiguous EN-DC with one component carrier per CG the EVM requirement applies with PRB allocation in one of the CG and the other CG unallocated.

The EVM requirements for each CG are according to clause 6.5.2 of TS 36.101 [4] for the MCG and 6.4.2 of TS38.101-1 [2] for the SCG with EN-DC configured.

##### 6.4B.2.2.2 Carrier leakage

The carrier leakage requirements for each CG are according to clause 6.5.2 of TS 36.101 [4] for the MCG and 6.4.2 of TS 38.101-1 [2] for the SCG with EN-DC configured and PRB allocation only in the CG being measured.

##### 6.4B.2.2.3 In-band emissions

For the MCG the in-band emission requirements in Table 6.5.2A.3.1-1 and 6.5.2A.3.1-2 in TS 36.101 [4] apply within the transmission bandwidth configuration of the MCG with the carriers of both CGs active and one single contiguous PRB allocation of bandwidth LCRB within the MCG at the edge of the transmission bandwidth configuration.

For the SCG the in-band emission requirements in Table 6.4.2.3-1 in TS 38.101-1 [2] apply within the transmission bandwidth configuration of the SCG with the carriers of both CGs active and one single contiguous PRB allocation of bandwidth LCRB within the SCG at the edge of the transmission bandwidth configuration.

6.4B.2.3 Transmit modulation quality for Inter-band EN-DC within FR1

For inter-band EN-DC with uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.2 in TS 36.101 [4] and in clause 6.4.2 in TS 38.101-1 [2], respectively, with all component carriers active, applies with PRB allocation in one of the CG and the other CG unallocated. If multiple component carriers are assigned to one E-UTRA band, the requirements in subclauses 6.5.2A in TS 36.101 [4] apply for those component carriers.

#### 6.4B.2.3a Transmit modulation quality for Inter-band NE-DC within FR1

For inter-band NE-DC with uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.2 in TS 36.101 [4] and in clause 6.4.2 in TS 38.101-1 [2], respectively, with all component carriers active, applies with PRB allocation in one of the CG and the other CG unallocated. If multiple component carriers are assigned to one E-UTRA band, the requirements in clauses 6.5.2A in TS 36.101 [4] apply for those component carriers, and if multiple component carriers are assigned to one NR band, the requirements in clauses 6.4A.2 in TS 38.101-1 [2] apply for those component carriers.

#### 6.4B.2.4 Transmit modulation quality for Inter-band EN-DC including FR2

Transmit modulation quality requirement for E-UTRA single carrier and CA operation specified in clauses 6.5.2 and 6.5.2A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.4.2, 6.4A.2 and 6.4D.2 of TS 38.101-2 [3] apply.

DMRS bundling requirements, as specified in clause 6.4.2.6 in TS 38.101-2 [3], apply when one uplink band and CC is configured for DMRS bundling at a time. If UE is needs to apply P-MPR as described in 6.2.5of TS 36.101-1 or 6.2.4 of TS 38.101-2, during a granted DMRS bundle on the uplink CC of FR2, phase continuity is not expected to be maintained in the bundle.

#### 6.4B.2.4a (Void)

#### 6.4B.2.5 Transmit modulation quality for inter-band EN-DC including both FR1 and FR2

Transmit modulation quality requirement for E-UTRA single carrier and CA operation specified in clauses 6.5.2 and 6.5.2A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.4.2 and 6.4A.2  of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.4.2, 6.4A.2 and 6.4D.2 of TS 38.101-2 [3] apply.

## 6.4E Transmit signal quality for V2X operation in FR1

### 6.4E.1 Frequency error for V2X

For intra-band V2X operating UE, the requirement shall apply on each component carrier as defined in clause 6.5.1G in TS 36.101 [4] and in clause 6.4E.1 in TS 38.101-1 [2], respectively.

For the inter-band con-current NR V2X operation, the requirements specified in subclause 6.4.1 of TS 36.101 [4] shall apply for the E-UTRA uplink in licensed band and the requirements specified in subclause 6.4E.1 of TS 38.101-1 [2] shall apply for the sidelink in NR Band n47.

#### 6.4E.2 Transmit modulation quality for V2X

#### 6.4E.2.1 Transmit modulation quality for Intra-band V2X

##### 6.4E.2.2.1 Error Vector Magnitude

For intra-band V2X operating UE, the requirement shall apply on each SL transmission as defined in clause 6.5.2G.1 in TS 36.101 [4] and in clause 6.4E.2.1 in TS 38.101-1 [2], respectively.

For the inter-band con-current NR V2X operation, the requirements specified in subclause 6.5.2 of TS 36.101 [4] shall apply for the E-UTRA uplink in licensed band and the requirements specified in subclause 6.4E.2.1 of TS 38.101-1 [2] shall apply for the sidelink in NR Band n47.

##### 6.4E.2.2.2 Carrier leakage

For intra-band V2X operating UE, the requirement shall apply on each SL transmission as defined in clause 6.5.2G.2 in TS 36.101 [4] and in clause 6.4E.2.2 in TS 38.101-1 [2], respectively.

##### 6.4E.2.2.3 In-band emissions

For intra-band V2X operating UE, the requirement shall apply on each SL transmission as defined in clause 6.5.2G.3 in TS 36.101 [4] and in clause 6.4E.2.3 in TS 38.101-1 [2], respectively.

#### 6.4E.2.2 Transmit modulation quality for Inter-band V2X

For inter-band V2X with transmission assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.2 in TS 36.101 [4] and in clause 6.4.2 in TS 38.101-1 [2], respectively, with all component carriers active. If multiple component carriers are assigned to one E-UTRA band, the requirements in clauses 6.5.2A in TS 36.101 [4] apply for those component carriers.

## 6.4H Transmit signal quality for DC with UL MIMO

### 6.4H.1 Frequency error for DC with UL MIMO

#### 6.4H.1.1 void

#### 6.4H.1.2 void

#### 6.4H.1.3 Frequency error for inter-band EN-DC with UL MIMO within FR1

For inter-band EN-DC with UL MIMO and uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4D.1 in TS 38.101-1 [2], respectively, with all component carriers active.

### 6.4H.2 Transmit modulation quality for DC with UL MIMO

#### 6.4H.2.1 void

#### 6.4H.2.2 void

#### 6.4H.2.3 Transmit modulation quality for inter-band EN-DC with UL MIMO within FR1

For inter-band EN-DC with UL MIMO and uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.2 in TS 36.101 [4] and in clause 6.4D.2 in TS 38.101-1 [2], respectively, with all component carriers active.

## 6.4L Transmit signal quality for DC with Tx Diversity

### 6.4L.1 Frequency error for DC with Tx Diversity

#### 6.4L.1.1 void

#### 6.4L.1.2 void

#### 6.4L.1.3 Frequency error for inter-band EN-DC with Tx Diversity within FR1

For inter-band EN-DC with Tx Diversity and uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4G.1 in TS 38.101-1 [2], respectively, with all component carriers active.

### 6.4L.2 Transmit modulation quality for DC with Tx Diversity

#### 6.4L.2.1 void

#### 6.4L.2.2 void

#### 6.4L.2.3 Transmit modulation quality for inter-band EN-DC with Tx Diversity within FR1

For inter-band EN-DC with Tx Diversity and uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.2 in TS 36.101 [4] and in clause 6.4G.2 in TS 38.101-1 [2], respectively, with all component carriers active.

## 6.5 Void

## 6.5A Output RF spectrum emissions for CA

### 6.5A.1 Occupied bandwidth for CA

For inter-band NR CA between FR1 and FR2, occupied bandwidth specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for each frequency range respectively.

### 6.5A.2 Out-of-band emissions for CA

For inter-band NR CA between FR1 and FR2, out-of-band emissions specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for each frequency range respectively.

### 6.5A.3 Spurious emissions for CA

#### 6.5A.3.1 Inter-band CA between FR1 and FR2

Unless otherwise stated, for inter-band CA between FR1 and FR2, spurious emission and UE co-existence requirements specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for each component carrier respectively.

Table 6.5A.3.1-1: Void

### 6.5A.4 Transmit intermodulation for CA

For inter-band NR CA between FR1 and FR2, transmit intermodulation specified in TS 38.101-1 [2] apply for each component carrier for NR FR1.

## 6.5B Output RF spectrum emissions for DC

### 6.5B.1 Occupied bandwidth for EN-DC

#### 6.5B.1.1 Intra-band contiguous EN-DC

For intra-band contiguous EN-DC the occupied bandwidth is a measure of the bandwidth containing 99% of the total integrated power of the transmitted spectrum. The OBW shall be less than the aggregated channel bandwidth for EN-DC, denoted as ENBW in clause 5.3B.

#### 6.5B.1.2 Intra-band non-contiguous EN-DC

For intra-band non-contiguous EN-DC, occupied bandwidth requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.1 and 6.6.1A of TS 36.101 [4] and for NR single carrier specified in clause 6.5.1 of TS 38.101-1 [2] apply.

#### 6.5B.1.3 Inter-band EN-DC within FR1

Occupied bandwidth requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.1 and 6.6.1A of TS 36.101 [4] and for NR single carrier specified in clause 6.5.1 of TS 38.101-1 [2] apply.

#### 6.5B.1.3a (Void)

#### 6.5B.1.4 Inter-band EN-DC including FR2

Occupied bandwidth requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.1 and 6.6.1A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.1, 6.5A.1 and 6.5D.1 of TS 38.101-2 [3] apply.

#### 6.5B.1.4a (Void)

#### 6.5B.1.5 Inter-band EN-DC including both FR1 and FR2

Occupied bandwidth requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.1 and 6.6.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.5.1 and 6.5A.1 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.1, 6.5A.1 and 6.5D.1 of TS 38.101-2 [3] apply.

### 6.5B.2 Out-of-band emissions for DC

#### 6.5B.2.1 Intra-band contiguous EN-DC

The out of band emissions are unwanted emissions immediately outside the EN-DC aggregated channel bandwidth resulting from the modulation process and non-linearity in the transmitter but excluding spurious emissions. This out of band emission limit is specified in terms of a spectrum emission mask and an adjacent channel leakage power ratio.

Unless otherwise stated, the OOBE limits specified for the DC combination in this clause supercede any OOBE requirements specified for each sub-block in the respective TS [4] and TS 38.101-1 [2].

The requirements apply to the sum of transmissions across all antenna connectors.

##### 6.5B.2.1.1 Spectrum emissions mask

The spectrum emission mask of the UE applies to frequencies (ΔfOOB) starting from the ± edge of the EN-DC aggregated channel bandwidth. For frequencies offset greater than ΔfOOB as specified in Table 6.5B.2.1.1-1 the spurious requirements in clause 6.5B.3 are applicable.

The general spectrum emission for intra-band contiguous EN-DC is specified in Table 6.5B.2.1.1-1.

The power of any UE emission shall not exceed the levels specified in Table 6.5B.2.1.1-1 for the specified EN-DC aggregated channel bandwidth.

Table 6.5B.2.1.1-1: General spectrum emission mask for intra-band contiguous EN-DC

| ΔfOOB(MHz) | Spectrum emission limit (dBm) | Measurement bandwidth |
| --- | --- | --- |
| ± 0 - 1 | Max(Round(10*log(0.15/ENBW)),-24) | 30 kHz |
| ± 1 - 5 | -10 | 1 MHz |
| ± 5 - ENBW | -13 | 1 MHz |
| ± ENBW – (ENBW+5) | -25 | 1 MHz |
| NOTE: ENBW refers to the aggregated channel bandwidth in MHz as defined in clause 5.3B. |  |  |

##### 6.5B.2.1.2 Additional spectrum emissions mask

###### 6.5B.2.1.2.1 Requirements for network signalled value "NS_35"

When NS_35 is indicated in the MCG and NS_35 is indicated in the SCG, the requirements in Table 6.5B.2.1.2.1-1 apply in the frequency ranges immediately adjacent and outside the aggregated sub-blocks of the EN-DC configuration for DC_(n)71AA.

Table 6.5B.2.1.2.1-1: Additional requirements

| ΔfOOB(MHz) | Frequency offset of measurement filter centre frequency, f_offset | Minimum requirement(dBm) | Measurement bandwidth |
| --- | --- | --- | --- |
| 0 MHz  f < 0.1 MHz | 0.015 MHz  f_offset < 0.085 MHz | -13 | 30 kHz |
| 0.1 MHz  f < ENBW | 0.15 MHz  f_offset < ENBW – 0.05 MHz | -13 | 100 kHz |
| ENBW  f < ENBW + 5 MHz | ENBW+0.5 MHz  f_offset < ENBW + 4.5 MHz | -25 | 1 MHz |
| NOTE 1: ENBW is the aggregated bandwidth of an E-UTRA sub-block and an adjacent NR sub-block; there is no frequency separation between the said sub-blocks. The sub-block bandwidths include any internal guard bands. |  |  |  |

###### 6.5B.2.1.2.2 Requirements for network signalled value "NS_04"

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

The Band 41/n41 SEM transition point from -13 dBm/MHz to -25 dBm/MHz is based on the emission bandwidth. The emission bandwidth is defined as the width of the signal between two points, one below the carrier center frequency and one above the carrier center frequency, outside of which all emissions are attenuated at least 26 dB below the transmitter power. Since the 26 dB emission bandwidth is implementation dependent, the transmission bandwidths occupied by RBs is used for the SEM. The emission bandwidth for E-UTRA carriers is document in TS 36.101 [4], and the emission bandwidth for NR carriers is documented in TS 38.101-1 [2]. The total emission bandwidth for contiguous intra-band EN-DC is the sum of the emission bandwidth for each CC plus the guard band between contiguous CCs.

When "NS_04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5B.2.1.2.2-1.

Table 6.5B.2.1.2.2-1: DC_(n)41 SEM with NS_04

|  | Spectrum emission limit (dBm) / measurement bandwidthfor each ENBW |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ΔfOOB MHz | 15  MHz | 20  MHz | 40  MHz | 50  MHz | > 50  MHz | Measurement bandwidth |
| ± 0 - 1 | -10 | -10 | -10 |  |  | 2 % ENBW |
|  |  |  |  | -10 |  | 1 MHz |
| ± 1 - 5 | -10 |  |  |  |  | 1 MHz |
| ± 5 - X | -13 |  |  |  |  |  |
| ± X - (ENBW + 5 MHz) | -25 |  |  |  |  |  |
| NOTE: X is defined as the sum of the emission bandwidth of the component carriers plus the guard band between contiguous CCs. |  |  |  |  |  |  |

##### 6.5B.2.1.3 Adjacent channel leakage ratio

For EN-DC operation with an E-UTRA sub-block immediately adjacent to an NR sub-block, the ACLR is defined as the ratio of the filtered mean power centred on the aggregated sub-block bandwidth ENBW to the filtered mean power centred on an adjacent bandwidth of the same size ENBW at nominal channel spacing. The UE shall meet the ACLR minimum requirement EN-DCACLR specified in Table 6.5B.2.1.3-1 with ENBW the sum of the sub-block bandwidths.

The assigned channel power and adjacent channel power are measured with rectangular filters with measurement bandwidths specified in 6.5B.2.1.3-1.

Table 6.5B.2.1.3-1: ACLR for intra-band EN-DC (contiguous sub-blocks)

| Parameter | Unit | Value |
| --- | --- | --- |
| EN-DCACLR for PC3 | dBc | 30 |
| EN-DCACLR for PC2 | dBc | 31 |
| EN-DCACLR for PC1.5 | dBc | 31 |
| Measurement bandwidth of EN-DC channel |  | 1.00*ENBW |
| Measurement bandwidth of adjacent channel |  | 0.95*ENBW |
| Frequency offset of adjacent channel |  | ENBW/-ENBW |
| NOTE 1: ENBW is the aggregated bandwidth in MHz as defined in clause 5.3B.NOTE 2: The frequency offset is that in between the centre frequencies of the measurement filters |  |  |

#### 6.5B.2.2 Intra-band non-contiguous EN-DC

##### 6.5B.2.2.1 Spectrum emissions mask

The spectral emission mask for intra-band non-contiguous EN-DC is a composite of the emission mask for each CC with the level set to the maximum value from each mask for each frequency outside of the transmission bandwidth of either carrier. A composite spectrum emission mask is a combination of individual CC spectrum emissions masks. Where two masks overlap the most relaxed limit is used. Composite spectrum emission mask applies to frequencies up to  ΔfOOB starting from the edges of the sub-blocks. If for some frequency an individual CC spectrum emission mask overlaps with the bandwidth of another CC then the emission mask does not apply for that frequency.

##### 6.5B.2.2.2 Additional spectrum emissions mask

When additional spectrum emission mask or masks apply, the additional SEM(s) shall be used to calculate the composite SEM described in 6.5B.2.2.1.

##### 6.5B.2.2.3 Adjacent channel leakage ratio

For intra-band non-contiguous EN-DC, the EN-DC Adjacent Channel Leakage power Ratio (EN-DCACLR) is the ratio of the sum of the filtered mean powers centred on the assigned E-UTRA and NR sub-block frequencies to the filtered mean power centred on an adjacent channel frequency at nominal channel spacing. In case the sub-block gap bandwidth Wgap is smaller than a E-UTRA or NR sub-block bandwidth, no EN-DCACLR requirement is set for the corresponding sub-block for the gap. The assigned EN-DC sub-block power and adjacent channel power are measured with rectangular filters with measurement bandwidths specified in TS 36.101 [4] for the E-UTRA sub-block, and TS 38.101-1 [2] for the NR sub-block. If the measured adjacent channel power is greater than –50dBm then the EN-DCACLR shall be higher than the value specified in for E-UTRAACLR and NRACLR.

#### 6.5B.2.3 Inter-band EN-DC within FR1

Unless otherewise stated, the OOBE requirements specified in clause 6.6.2.1 of TS 36.101 [4], sub- clause 6.6.2 of TS 36.101 [4] and clause 6.5.2 of TS 38.101-1 [2] apply for each component carrier.

#### 6.5B.2.3a (Void)

#### 6.5B.2.4 Inter-band EN-DC including FR2

Unless otherewise stated, out-of-band emissions requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.2 of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.2, 6.5A.2 and 6.5D.2 of TS 38.101-2 [3] apply.

#### 6.5B.2.4a Inter-band NE-DC including FR2

Unless otherewise stated, out-of-band emissions requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.2 of TS 36.101 [4] and for NR single carrier, CA operation, and UL-MIMO specified in clause 6.5.2, 6.5A.2 and 6.5D.2 of TS 38.101-2 [3] apply.

#### 6.5B.2.5 Inter-band EN-DC including both FR1 and FR2

Unless otherewise stated, out-of-band emissions requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.2 of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.5.2 and 6.5A.2 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.2, 6.5A.2 and 6.5D.2 of TS 38.101-2 [3] apply.

### 6.5B.3 Spurious emissions for DC

#### 6.5B.3.1 Intra-band contiguous EN-DC

##### 6.5B.3.1.1 General spurious emissions

The general spurious emissions requirements specified in clause 6.6.3.1 of TS 36.101 [4] and clause 6.5.3.1 of TS 38.101-1 [2] apply beyond any frequencies for which the out-of-band emissions requirements in clause 6.5B.2.1apply.

##### 6.5B.3.1.2 Spurious emission band UE co-existence

The requirements in Table 6.5B.3.1.2-1 apply on each component carrier with all component carriers are active. Unless otherwise stated, the spurious emission for UE co-existence requirements are not applicabe to the frequency ranges where out-of-band emissions requirements in clause 6.5B.2 are defined.

Table 6.5B.3.1.2-1: Requirements for intra-band contiguous EN-DC

| EN-DC Configuration | Spurious emission |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Protected band | Frequency range (MHz) |  |  | Maximum Level (dBm) | MBW (MHz) | NOTE |
| DC_(n)71 | E-UTRA Band 4, 5, 12, 13, 14, 17, 24, 26, 30, 48, 54, 66 | FDL_low | - | FDL_high | -50 | 1 |  |
|  | E-UTRA Band 2, 25, 41, 70,NR Band n77 | FDL_low | - | FDL_high | -50 | 1 | 2 |
|  | E-UTRA Band 29 | FDL_low | -- | FDL_high | -38 | 1 | 3 |
|  | E-UTRA Band 71 | FDL_low | - | FDL_high | -50 | 1 | 3 |
| DC_(n)41 | E-UTRA Band 1, 2, 3, 4, 5, 8, 10, 11, 12, 13 , 14, 17, 18, 19, 21, 24, 25, 26, 27, 28, 29, 30, 34, 39, 42, 44, 45, 48, 50, 51, 54, 66, 70, 71, 73, 74NR Band n77, n78 | FDL_low | - | FDL_high | -50 | 1 |  |
|  |  |  |  |  |  |  |  |
|  | NR Band n79 | FDL_low | - | FDL_high | -50 | 1 | 2 |
|  | E-UTRA Band 40 | FDL_low | - | FDL_high | -40 | 1 |  |
| NOTE 1: FDL_low and FDL_high refer to each frequency band specified in Table 5.5-1 in TS 36.101 [4] or in Table 5.2-1 in TS 38.101-1 [2].NOTE 2: As exceptions, measurements with a level up to the applicable requirements defined in Table 6.6.3.1-2 in TS 36.101 [4] and Table 6.5.3.1-2 in TS 38.101-1 [2] are permitted for each assigned carrier used in the measurement due to 2nd, 3rd, 4th or 5th harmonic spurious emissions. Due to spreading of the harmonic emission the exception is also allowed for the first 1 MHz frequency range immediately outside the harmonic emission on both sides of the harmonic emission. This results in an overall exception interval centred at the harmonic emission of (2 MHz + N x LCRB x 180 kHz), where N is 2, 3, 4, 5 for the 2nd, 3rd, 4th or 5th harmonic respectively. The exception is allowed if the measurement bandwidth (MBW) totally or partially overlaps the overall exception intervalNOTE 3: These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1, Table 6.6.3.1A-1 in TS 36.101 [4] or in Table 6.5.3.1-1 in TS 38.101-1 [2] from the edge of the channel bandwidth.NOTE4: Void. |  |  |  |  |  |  |  |

NOTE: To simplify the above Table, E-UTRA band numbers are listed for bands which are specified only for E-UTRA operation or both E-UTRA and NR operation. NR band numbers are listed for bands which are specified only for NR operation.

#### 6.5B.3.2 Intra-band non-contiguous EN-DC

##### 6.5B.3.2.1 General spurious emissions

The general spurious emissions requirements specified in clause 6.6.3.1 of TS 36.101 [4] and clause 6.5.3.1 of TS 38.101-1 [2] apply beyond any frequencies for which the out-of-band emissions requirements in clause 6.5B.2.2 apply. If for some frequency an individual CC spurious emission requirement overlaps with the general spectrum emission mask or the bandwidth of another CC then it does not apply.

##### 6.5B.3.2.2 Spurious emission band UE co-existence

The requirements in Table 6.5B.3.2.2-1 apply with all component carriers are active. Unless otherwise stated, the spurious emission for UE co-existence requirements are not applicabe to the frequency ranges where out-of-band emissions requirements in clause 6.5B.2 are defined.

Table 6.5B.3.2.2-1: Requirements for intra-band non-contiguous EN-DC

| EN-DC Configuration | Spurious emission |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Protected band | Frequency range (MHz) |  |  | Maximum Level (dBm) | MBW (MHz) | NOTE |
| DC_3_n3 | E-UTRA Band 1, 5, 7, 8, 11, 18, 19, 20, 21, 26, 27, 28, 31, 32, 33, 34, 38, 39, 40, 41, 43, 44, 45, 50, 51, 65, 67, 68, 69, 72, 73,74, 75, 76.NR Band n79, n109 | FDL_low | - | FDL_high | -50 | 1 |  |
|  | E-UTRA Band 3 | FDL_low | - | FDL_high | -50 | 1 | 3 |
|  | E-UTRA Band 22, 42, 52, NR Band n77, n78 | FDL_low | - | FDL_high | -50 | 1 | 2 |
|  |  |  |  |  |  |  |  |
| DC_41_n41 | E-UTRA Band 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 17, 18, 19, 21, 24, 25, 26, 27, 28, 29, 34, 39, 42, 44, 45, 48, 50, 51, 54, 66, 70, 71, 73, 74NR Band n77, n78 | FDL_low | - | FDL_high | -50 | 1 |  |
|  |  |  |  |  |  |  |  |
|  | E-UTRA Band 30 | FDL_low | - | FDL_high | -40 | 1 |  |
|  | E-UTRA Band 40 | FDL_low | - | FDL_high | -40 | 1 |  |
|  | NR band n79 | FDL_low | - | FDL_high | -50 | 1 | 2 |
| NOTE 1: FDL_low and FDL_high refer to each frequency band specified in Table 5.5-1 in TS 36.101 [4] or in Table 5.2-1 in TS 38.101-1 [2].NOTE 2: As exceptions, measurements with a level up to the applicable requirements defined in Table 6.6.3.1-2 in TS 36.101 [4] and Table 6.5.3.1-2 in TS 38.101-1 [2] are permitted for each assigned carrier used in the measurement due to 2nd, 3rd, 4th or 5th harmonic spurious emissions. Due to spreading of the harmonic emission the exception is also allowed for the first 1 MHz frequency range immediately outside the harmonic emission on both sides of the harmonic emission. This results in an overall exception interval centred at the harmonic emission of (2MHz + N x LCRB x 180kHz), where N is 2, 3, 4, 5 for the 2nd, 3rd, 4th or 5th harmonic respectively. The exception is allowed if the measurement bandwidth (MBW) totally or partially overlaps the overall exception intervalNOTE 3: These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 and Table 6.6.3.1A-1 from the edge of the channel bandwidth.NOTE 4: Void.NOTE 5: Void. |  |  |  |  |  |  |  |

NOTE: To simplify the above Table, E-UTRA band numbers are listed for bands which are specified only for E-UTRA operation or both E-UTRA and NR operation. NR band numbers are listed for bands which are specified only for NR operation.

#### 6.5B.3.3 Inter-band EN-DC within FR1

6.5B.3.3.1 General spurious emissions

The general spurious emissions requirements specified in clause 6.6.3.1 of TS 36.101 [4], clause 6.5.3.1 of TS38.101-1 [2] and TS 38.101-2 [3] apply for each component carrier. For the case of inter-band EN-DC with a single carrier per cell group, the general spurious emissions requirements also apply with both downlink carrier and both uplink carriers active. Limits on configured maximum output power for the uplink according to clause 6.2B.4 apply. If for some frequency a spurious emission requirement of an individual component carrier overlaps with the spectrum emission mask or channel bandwidth of another component carrier then it does not apply.

NOTE: The general spurious emission requirements with both uplink carriers active are allowed to be verified for only a single inter-band EN-DC configuration per NR band. Furthermore, the requirements are allowed to be verified by measuring spurious emissions at the specific frequencies where second and third order intermodulation products generated by the two transmitted carriers can occur.

Table 6.5B.3.3.1-1: (Void)

##### 6.5B.3.3.2 Spurious emission band UE co-existence

This clause specifies additional the requirements for uplink EN-DC coexistence with protected bands with the single CC uplink assigned to E-UTRA and NR bands for the specified uplink carrier aggregation configurations in Table 6.5B.3.3.2-1. The intersection of the requirements for the individual bands specified in clause 6.5.3.2 of [2] and clause 6.6.3.2 of [4] shall also apply for the specified uplink EN-DC configurations. Intersection of a requirement means that both UL constituent bands have the same protected band requirement specified and if one or both protected bands have note(s) associated those note(s) also apply.

The requirements in Table 6.5B.3.3.2-1 and the intersection of the requirements for the individual bands specified in clause 6.5.3.2 of [2] and clause 6.6.3.2 of [4] apply on each component carrier with all component carriers are active. Unless otherwise stated, the spurious emission for UE co-existence requirements are not applicable to the frequency ranges where out-of-band emissions requirements in clause 6.5B.2 are defined.

NOTE: For inter-band EN-DC with uplink assigned to one LTE band and one NR band the requirements in Table 6.5B.3.3.2-1 could be verified by measuring spurious emissions at the specific frequencies where second and third order intermodulation products generated by the two transmitted carriers can occur; in that case, the requirements for remaining applicable frequencies in Table 6.5B.3.3.2-1 and in 6.5.3.2 of [2] and clause 6.6.3.2 of [4] would be considered to be verified by the measurements verifying the uplink single carrier UE to UE co-existence requirements.

Table 6.5B.3.3.2-1: Requirements

| EN-DC Configuration | Spurious emission |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Protected band | Frequency range (MHz) |  |  | Maximum Level (dBm) | MBW (MHz) | NOTE |
| DC_1_n26 | Frequency range | 738 |  | 799 | -50 | 1 |  |
|  | Frequency range | 799 |  | 803 | -40 | 1 | 5 |
| DC_1_n28 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
| DC_2_n14 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_2_n28 | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_3_n20 | Frequency range | 758 | - | 788 | -50 | 1 |  |
| DC_3_n28 | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_3_n34 | Frequency range | 1884.5 | - | 1915.7 | -41 | 0.3 | 3 |
| DC_4_n5 | Frequency range | 859 | - | 869 | -27 | 1 |  |
| DC_4_n28 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_5_n7 | Frequency range | 859 | - | 869 | -27 | 1 |  |
| DC_5_n28 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_5_n40 | Frequency range | 859 | - | 869 | -27 | 1 |  |
| DC_5_n48 | Frequency range | 859 | - | 869 | -27 | 1 |  |
| DC_5_n66 | Frequency range | 859 | - | 869 | -27 | 1 |  |
| DC_5_n78DC_5_n89_ULSUP-TDM_n78 | Frequency range | 859 | - | 869 | -27 | 1 |  |
| DC_5_n79 | Frequency range | 859 | - | 869 | -27 | 1 |  |
| DC_7_n28 | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_8_n1 | Frequency range | 860 | - | 890 | -40 | 1 | 5, 12 |
| DC_8_n3 | Frequency range | 860 | - | 890 | -40 | 1 | 5. 12 |
| DC_8_n7 | Frequency range | 860 | - | 890 | -40 | 1 | 5, 12 |
| DC_8_n20 | Frequency range | 758 | - | 788 | -50 | 1 |  |
| DC_8_n28 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
|  | Frequency range | 860 | - | 890 | -40 | 1 | 5, 12 |
| DC_8_n34 | Frequency range | 860 | - | 890 | -40 | 1 | 5, 12 |
| DC_8_n41,DC_8_n81_ULSUP-TDM_n41 | Frequency range | 860 | - | 890 | -40 | 1 | 5, 12 |
| DC_8_n77 | Frequency range | 860 | - | 890 | -40 | 1 | 5, 12 |
| DC_8_n78DC_8_n81_ULSUP-TDM_n78 | Frequency range | 860 | - | 890 | -40 | 1 | 5, 12 |
| DC_8_n79DC_8_n81_ULSUP-TDM_n79 | Frequency range | 860 | - | 890 | -40 | 1 | 5, 12 |
| DC_11_n1 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_11_n3 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_11_n28 | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
|  | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_11_n41 | Frequency range | 945 | - | 960 | -50 | 1 |  |
| DC_11_n77 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_11_n78 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_11_n79 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_13_n2 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_13_n5 | Frequency range | 859 | - | 869 | -27 | 1 |  |
|  | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_13_n7 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_13_n25 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_13_n48 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_13_n66 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 803 | -35 | 0.00625 | 5 |
| DC_13_n71 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_13_n77 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_14_n2 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_14_n30 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_14_n77 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_14_n66 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_18_n28 | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 799 | -50 | 1 |  |
|  | Frequency range | 799 | - | 803 | -40 | 1 | 5 |
|  | Frequency range | 860 | - | 890 | -40 | 1 |  |
|  | Frequency range | 945 | - | 960 | -50 | 1 | 5 |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_18_n41 | Frequency range | 945 | - | 960 | -50 | 1 |  |
| DC_13_n78 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_18_n3 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_18_n77 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_18_n78 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_18_n79 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_19_n1 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_19_n77 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_19_n78 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_19_n79 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_20_n1 | Frequency range | 758 | - | 788 | -50 | 1 |  |
| DC_20_n3 | Frequency range | 758 | - | 788 | -50 | 1 |  |
| DC_20_n41 | Frequency range | 758 | - | 788 | -50 | 1 |  |
| DC_20_n50 | Frequency range | 758 | - | 788 | -50 | 1 |  |
| DC_20_n51 | Frequency range | 758 | - | 788 | -50 | 1 |  |
| DC_20A_91A_ULSUP-TDM,DC_20A_92A_ULSUP-TDM | Frequency range | 758 | - | 788 | -50 | 1 |  |
| DC_21_n1 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_21_n28 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
|  | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
| DC_21_n77 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_21_n78 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_21_n79 | Frequency range | 945 | - | 960 | -50 | 1 |  |
|  | Frequency range | 2545 | - | 2575 | -50 | 1 |  |
|  | Frequency range | 2595 | - | 2645 | -50 | 1 |  |
| DC_26_n41 | Frequency range | 703 | - | 799 | -50 | 1 |  |
|  | Frequency range | 799 | - | 803 | -40 | 1 | 5 |
|  | Frequency range | 945 | - | 960 | -50 | 1 |  |
| DC_26_n77 | Frequency range | 703 | - | 799 | -50 | 1 |  |
|  | Frequency range | 799 | - | 803 | -40 | 1 | 5 |
|  | Frequency range | 945 | - | 960 | -50 | 1 |  |
| DC_26_n78 | Frequency range | 703 | - | 799 | -50 | 1 |  |
|  | Frequency range | 799 | - | 803 | -40 | 1 | 5 |
|  | Frequency range | 945 | - | 960 | -50 | 1 |  |
| DC_26_n79 | Frequency range | 703 | - | 799 | -50 | 1 |  |
|  | Frequency range | 799 | - | 803 | -40 | 1 | 5 |
|  | Frequency range | 945 | - | 960 | -50 | 1 |  |
| DC_28_n1 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n2 | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n3 | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n5 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n7 | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n8 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n38 | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n40 | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n41DC_28_n83_ULSUP-TDM_n41 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n50 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n51 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n66 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n77 | Frequency range | 758 | - | 773 | -32 | 1 |  |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n78DC_28_n83_ULSUP-TDM_n78 | Frequency range | 758 | - | 773 | -32 | 1 |  |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_28_n79 | Frequency range | 758 | - | 773 | -32 | 1 |  |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_30_n14 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_38_n8 | Frequency range | 860 | - | 890 | -40 | 1 | 5, 12 |
| DC_38_n28 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_38_n78 | N/A |  |  |  |  |  |  |
| DC_40_n77 | N/A |  |  |  |  |  |  |
| DC_41_n28 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_42_n77 | N/A |  |  |  |  |  |  |
| DC_42_n78 | N/A |  |  |  |  |  |  |
| DC_42_n79 | N/A |  |  |  |  |  |  |
| DC_48_n77 | N/A |  |  |  |  |  |  |
| DC_66_n14 | Frequency range | 769 | - | 775 | -35 | 0.00625 | 5 |
|  | Frequency range | 799 | - | 805 | -35 | 0.00625 | 5 |
| DC_66_n28 | Frequency range | 470 | - | 694 | -42 | 8 | 5, 17 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 14 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 5 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 5 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_68_n20 | Frequency range | 758 | - | 788 | -50 | 1 |  |
| DC_68_n38 | Frequency range | 2620 | - | 2645 | -15.5 | 5 | 5, 22, 26 |
|  | Frequency range | 2645 | - | 2690 | -40 | 1 | 5, 22 |
| DC_68_n41 | Frequency range | 2530 | - | 2535 | -25 | 1 | 23 |
|  | Frequency range | 2505 | - | 2530 | -30 | 1 | 23 |
| NOTE 1: VoidNOTE 2: VoidNOTE 3: VoidNOTE 4: VoidNOTE 5: These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1, Table 6.6.3.1A-1 in TS 36.101 [4] or in Table 6.5.3.1-1 in TS 38.101-1 [2] from the edge of the channel bandwidth.NOTE 6: VoidNOTE 7: VoidNOTE 8: VoidNOTE 9: Applicable when the assigned E-UTRA or NR carrier is confined within 718 MHz and 748 MHz and when the channel bandwidth used is 5 or 10 MHz.NOTE 10: VoidNOTE 11: VoidNOTE 12: This requirement is applicable only for the following cases: A: for carriers of 5 MHz channel bandwidth when carrier centre frequency (Fc) is within the range 902.5 MHz ≤ Fc < 907.5 MHz with an uplink transmission bandwidth less than or equal to 20 RB; B: for carriers of 5 MHz channel bandwidth when carrier centre frequency (Fc) is within the range 907.5 MHz ≤ Fc ≤ 912.5 MHz without any restriction on uplink transmission bandwidth; C: for carriers of 10 MHz channel bandwidth when carrier centre frequency (Fc) is Fc = 910 MHz with an uplink transmission bandwidth less than or equal to 32 RB with RBstart > 3.NOTE 13: VoidNOTE 14: This requirement is applicable for 5 and 10 MHz E-UTRA or NR channel bandwidth allocated within 718-728MHz. For carriers of 10 MHz bandwidth, this requirement applies for an uplink transmission bandwidth less than or equal to 30 RB with RBstart > 1 and RBstart < 48.NOTE 15: VoidNOTE 16: VoidNOTE 17: This requirement is applicable in the case of a 10 MHz E-UTRA or NR carrier confined within 703 MHz and 733 MHz, otherwise the requirement of -25 dBm with a measurement bandwidth of 8 MHz applies.NOTE 18: VoidNOTE 19: VoidNOTE 20: Void.NOTE 21: VoidNOTE 22: Void |  |  |  |  |  |  |  |

#### 6.5B.3.3a Inter-band NE-DC within FR1

##### 6.5B.3.3a.1 Void

##### 6.5B.3.3a.2 Spurious emission band UE co-existence

This clause specifies the requirements for the specified NE-DC configurations that do not have a corresponding defined EN-DC, for coexistence with protected bands. For the NE-DC configurations that have a corresponding specified EN-DC configuration, the requirements in Table 6.5B.3.3.2-1 apply on each component carrier with all component carriers are active. Unless otherwise stated, the spurious emission for UE co-existence requirements are not applicabe to the frequency ranges where out-of-band emissions requirements in clause 6.5B.2 are defined.

Table 6.5B.3.3a.2-1: Requirements

| E-UTRA and NR DC Configuration | Spurious emission |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Protected band | Frequency range (MHz) |  |  | Maximum Level (dBm) | MBW (MHz) | NOTE |
| DC_n28_34 | E-UTRA Band 3, 7, 8, 18, 19 ,20, 26, 31, 38, 40, 41, 72NR band n77, n79, n100, n101 | FDL_low | - | FDL_high | -50 | 1 |  |
|  | E-UTRA Band 22, 32, 42, 43, 50, 51, 52, 65, 73, 74, 75 NR band n78, n109 | FDL_low | - | FDL_high | -50 | 1 | 2 |
|  | E-UTRA Band 11, 21 | FDL_low | - | FDL_high | -50 | 1 | 5, 6 |
|  | E-UTRA Band 1 | FDL_low | - | FDL_high | -50 | 1 | 5, 7 |
|  | Frequency range | 470 | - | 694 | -42 | 8 | 4, 9 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 8 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 4 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 4 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_n28_39 | E-UTRA Band 8, 26, 34, 40, 41NR band n79 | FDL_low | - | FDL_high | -50 | 1 |  |
|  | E-UTRA Band 22, 42, 50, 51, 52, 73, 74NR band n77, n78 | FDL_low | - | FDL_high | -50 | 1 | 2 |
|  | E-UTRA Band 1 | FDL_low | - | FDL_high | -50 | 1 | 5, 7 |
|  | Frequency range | 470 | - | 694 | -42 | 8 | 4, 9 |
|  | Frequency range | 470 | - | 710 | -26.2 | 6 | 8 |
|  | Frequency range | 662 | - | 694 | -26.2 | 6 | 4 |
|  | Frequency range | 758 | - | 773 | -32 | 1 | 4 |
|  | Frequency range | 773 | - | 803 | -50 | 1 |  |
| DC_n41_34 | UTRA Band 1, 3, 8, 26, 28, 39, 42, 44, 45, 50, 51, 52, 65, 73, 74NR band n78 | FDL_low | - | FDL_high | -50 | 1 |  |
|  | NR band n79 | FDL_low | - | FDL_high | -50 | 1 | 2 |
|  | E-UTRA Band 11, 18, 19, 21 | FDL_low | - | FDL_high | -50 | 1 |  |
|  | E-UTRA 40 | FDL_low | - | FDL_high | -40 | 1 |  |
| NOTE 1: FDL_low and FDL_high refer to each frequency band specified in Table 5.5-1 in TS 36.101 [4] or in Table 5.2-1 in TS 38.101-1 [2].NOTE 2: As exceptions, measurements with a level up to the applicable requirements defined in Table 6.6.3.1-2 are permitted for each assigned E-UTRA carrier used in the measurement due to 2nd, 3rd, 4th or 5th harmonic spurious emissions. Due to spreading of the harmonic emission the exception is also allowed for the first 1 MHz frequency range immediately outside the harmonic emission on both sides of the harmonic emission. This results in an overall exception interval centred at the harmonic emission of (2 MHz + N x LCRB x 180 kHz), where N is 2, 3, 4, 5 for the 2nd, 3rd, 4th or 5th harmonic respectively. The exception is allowed if the measurement bandwidth (MBW) totally or partially overlaps the overall exception interval.NOTE 3: VoidNOTE 4: These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1, Table 6.6.3.1A-1 in TS 36.101 [4] or in Table 6.5.3.1-1 in TS 38.101-1 [2] from the edge of the channel bandwidth.NOTE 5: Applicable when the assigned E-UTRA carrier is confined within 718 MHz and 748 MHz and when the channel bandwidth used is 5 or 10 MHz.NOTE 6: As exceptions, measurements with a level up to the applicable requirement of -38 dBm/MHz is permitted for each assigned E-UTRA carrier used in the measurement due to 2nd harmonic spurious emissions. An exception is allowed if there is at least one individual RB within the transmission bandwidth (see Figure 5.6-1) for which the 2nd harmonic totally or partially overlaps the measurement bandwidth (MBW).NOTE 7: As exceptions, measurements with a level up to the applicable requirement of -36 dBm/MHz is permitted for each assigned E-UTRA carrier used in the measurement due to 3rd harmonic spurious emissions. An exception is allowed if there is at least one individual RB within the transmission bandwidth (see Figure 5.6-1) for which the 3rd harmonic totally or partially overlaps the measurement bandwidth (MBW).NOTE 8: This requirement is applicable for 5 and 10 MHz E-UTRA channel bandwidth allocated within 718-728MHz. For carriers of 10 MHz bandwidth, this requirement applies for an uplink transmission bandwidth less than or equal to 30 RB with RBstart > 1 and RBstart < 48.NOTE 9: This requirement is applicable in the case of a 10 MHz E-UTRA carrier confined within 703 MHz and 733 MHz, otherwise the requirement of -25 dBm with a measurement bandwidth of 8 MHz applies. |  |  |  |  |  |  |  |

#### 6.5B.3.4 Inter-band EN-DC including FR2

##### 6.5B.3.4.0 General spurious emission

General spurious requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.3.1 and 6.6.3.1A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.3, 6.5A.3 and 6.5D.3 of TS 38.101-2 [3] apply.

##### 6.5B.3.4.1 Spurious emission band UE co-existence

This clause specifies the requirements for the specified EN-DC, for coexistence with protected bands. Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.5.1-1, no requirements for FR2 NR bands to protect E-UTRA and FR1 NR bands are applied to the constituent FR2 NR bands. Spurious emission band UE co-existence requirements specified in TS 36.101 [4] are applied to the constituent E-UTRA bands for the EN-DC configuration.

Spurious emission band UE co-existence requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.3.2 and 6.6.3.2A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.3.1, 6.5A.3.1 and 6.5D.3.1 of TS 38.101-2 [3] apply.

Table 6.5B.3.4.1-1: Void

#### 6.5B.3.4a (Void)

##### 6.5B.3.4a.1 (Void)

#### 6.5B.3.5 Inter-band EN-DC including both FR1 and FR2

##### 6.5B.3.5.0 General spurious emission

General spurious requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.3.1 and 6.6.3.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.5.3.1 and 6.5A.3.1 of TS 38.101-1 [2] and clause 6.5.3, 6.5A.3 and 6.5D.3 of TS 3801-2 [3] apply.

##### 6.5B.3.5.1 Spurious emission band UE co-existence

This clause specifies the requirements for the specified EN-DC, for coexistence with protected bands. Unless otherwise stated, for inter-band EN-DC configurations defined in clause 5.5B.6, no requirements for FR2 NR bands to protect E-UTRA and FR1 NR bands are applied to the constituent FR2 NR bands. Spurious emission band UE co-existence requirements for constituent E-UTRA and FR1 NR bands for the inter-band EN-DC are the same as those for the corresponding EN-DC configuration without the FR2 bands specified in 6.5B.3.2.2.

Spurious emission band UE co-existence requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.3.2 and 6.6.3.2A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.5.3.2 and 6.5A.3.2 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.3.1, 6.5A.3.1 and 6.5D.3.1 of TS 38.101-2 [3] apply.

Table 6.5B.3.5.1-1: Void

### 6.5B.4 Additional spurious emissions

#### 6.5B.4.1 General

These requirements are specified in terms of an additional spectrum emission requirement. Additional spurious emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

NOTE: For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

##### 6.5B.4.1.1 Void

#### 6.5B.4.2 Intra-band contiguous EN-DC

##### 6.5B.4.2.1 Minimum requirement (network signalled value "NS_04")

When "NS 04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5B.4.1.1-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.5B.4.1.1-1: Additional requirements

| Frequency band(MHz) | Channel bandwidth / Spectrum emission limit (dBm) | Measurement bandwidth |
| --- | --- | --- |
| 2495 ≤ f < 2496 | -13 | 1 % of Channel BW for contiguous BW up to 100 MHz,1 MHz for contiguous BW  > 100 MHz |
| 2490.5 ≤ f < 2495 | -13 | 1 MHz |
| 0 < f < 2490.5 | -25 | 1 MHz |

#### 6.5B.4.3 Intra-band non-contiguous EN-DC

##### 6.5B.4.3.1 Minimum requirement (network signalled value "NS_04")

When "NS 04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5B.4.1.1-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.5B.4.1.1-1: Additional requirements

| Frequency band(MHz) | Channel bandwidth / Spectrum emission limit (dBm) | Measurement bandwidth |
| --- | --- | --- |
| 2495 ≤ f < 2496 | -13 | 1 % of Channel BW for contiguous BW up to 100 MHz,1 MHz for contiguous BW  > 100 MHz |
| 2490.5 ≤ f < 2495 | -13 | 1 MHz |
| 0 < f < 2490.5 | -25 | 1 MHz |

#### 6.5B.4.4 Inter-band EN-DC within FR1

The additional spurious emissions requirements specified for E-UTRA in clause 6.6.3.3 and 6.6.3.3A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.3.3, 6.5A.3.3 and 6.5D.3 of TS 38.101-1 [2] apply for each component carrier.

#### 6.5B.4.4a (Void)

#### 6.5B.4.5 Inter-band EN-DC including FR2

The additional spurious emissions requirements specified for E-UTRA in clause 6.6.3.3 and 6.6.3.3A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.3.3, 6.5A.3.3 and 6.5D.3 of TS 38.101-2 [3] apply for each component carrier.

#### 6.5B.4.6 Inter-band EN-DC including both FR1 and FR2

The additional spurious emissions requirements specified for E-UTRA in clause 6.6.3.3 and 6.6.3.3A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.3.3, 6.5A.3.3 and 6.5D.3 of TS 38.101-1 [2] and in clause 6.5.3.3, 6.5A.3.3 and 6.5D.3 of TS 38.101-2 [3] apply for each component carrier.

### 6.5B.5 Transmit intermodulation for DC

#### 6.5B.5.1 Intra-band contiguous EN-DC

Unless otherwise stated, no transmit intermodulation requirements are applied for intra band contiguous EN DC.

#### 6.5B.5.1a (Void)

#### 6.5B.5.2 Intra-band non-contiguous EN-DC

Unless otherwise stated, no transmit intermodulation requirements are applied for intra band non contiguous EN DC.

#### 6.5B.5.3 Inter-band EN-DC within FR1

The transmit intermodulation requirement specified in clauses 6.7.1 of TS 36.101 [4] and clauses 6.5.4 and 6.5A.4 of TS 38.101-1 [2] apply for each component carrier in E-UTRA bands and NR bands, respectively.

#### 6.5B.5.3a (Void)

#### 6.5B.5.4 Inter-band EN-DC including FR2

Transmit intermodulation requirements specified in clause 6.7.1 and 6.7.1A of TS 36.101 [4] apply for each component carrier in E-UTRA bands.

#### 6.5B.5.4a (Void)

#### 6.5B.5.5 Inter-band EN-DC including both FR1 and FR2

Transmit intermodulation requirement specified in clauses 6.7.1 and 6.7.1A of TS 36.101 [4] and clauses 6.5.4 and 6.5A.4 of TS 38.101-1 [2] apply for each component carrier in E-UTRA bands and NR bands, respectively.

## 6.5E Output RF spectrum emissions for V2X operation in FR1

### 6.5E.1 Occupied bandwidth

#### 6.5E.1.1 Intra-band V2X

For intra-band V2X, the occupied bandwidth specified in clause 6.6.1G in TS 36.101 [4] and specified in clause 6.5E.1 in TS 38.101-1 [2] apply for each frequency range respectively.

#### 6.5E.1.2 inter-band V2X con-current operation

For the inter-band con-current NR V2X operation, the requirements specified in subclause 6.6.1 of TS 36.101 [4] shall apply for the E-UTRA uplink in licensed band and the requirements specified in subclause 6.5E.1 of TS 38.101-1 [2] shall apply for the sidelink in NR Band n47.

### 6.5E.2 Out-of-band emissions

#### 6.5E.2.1 Intra-band V2X

For intra-band V2X, out-of-band emissions specified in clause 6.6.2G in TS 36.101 [4] and specified in clause 6.5E.2 in TS 38.101-1 [2] apply for each frequency range respectively.

#### 6.5E.2.2 Inter-band V2X con-current operation

For the inter-band con-current NR V2X operation, the general SEM/additional SEM requirements and ACLR specified in subclause 6.6.2 of TS 36.101 [4] shall apply for the E-UTRA uplink in licensed band and the general SEM/additional SEM and ACLR requirements specified in subclause 6.5E.2 of TS 38.101-1 [2] shall apply for the sidelink in NR Band n47.

### 6.5E.3 Spurious emissions

#### 6.5E.3.1 Intra-band V2X

##### 6.5E.3.1.1 General spurious emissions

For intra-band V2X, the general spurious emissions requirements specified in clause 6.6.3.1 of TS 36.101 [4] and clause 6.5E.3.1 of TS 38.101-1 [2] apply for each frequency range respectively.

##### 6.5E.3.1.2 Spurious emission band UE co-existence

For intra-band V2X, the spurious emissions band UE co-existence requirements specified in clause 6.6.3.2 of TS 36.101 [4] and clause 6.5E.3.2 of TS 38.101-1 [2] apply for each frequency range respectively.

#### 6.5E.3.2  Inter-band V2X con-current operation

##### 6.5E.3.2.1 General spurious emissions

For inter-band V2X, the general spurious emissions requirements specified in clause 6.6.3.1 of TS 36.101 [4] and clause 6.5E.3.1 of TS 38.101-1 [2] apply for each frequency range respectively.

##### 6.5E.3.2.2 Spurious emission band UE co-existence

This clause specifies the additional requirements for inter-band con-current V2X operation with the single CC uplink assigned to E-UTRA or NR bands for coexistence with protected bands for the specified simultaneous transmission of the inter-band con-current V2X configurations in Table 6.5E.3.2.2-1. The intersection of the requirements for the individual bands specified in clause 6.5.3.2 shall also apply for the specified simultaneous transmission of the inter-band con-current V2X. Intersection of a requirement means that both UL or sidelink transmission constituent bands have the same protected band requirement specified and if one or both protected bands have note(s) associated those note(s) also apply.

For the inter-band con-current NR V2X operation, the UE-coexistence requirements in Table 6.5E.3.2.2-1 apply for the corresponding inter-band con-current operation with transmission assigned to both E-UTRA/NR uplink in licensed band and sidelink in E-UTRA/NR Bands. Unless otherwise stated, the spurious emission for UE co-existence requirements are not applicabe to the frequency ranges where out-of-band emissions requirements in clause 6.5E.2 are defined.

NOTE: For inter-band con-current V2X operation with uplink assigned to E-UTRA/NR band and slidelink transmission assigned to E-UTRA/NR V2X operating bands, the requirements in Table 6.5E.3.2.2-1 could be verified by measuring spurious emissions at the specific frequencies where second and third order intermodulation products generated by the two transmitted carriers can occur; in that case, the requirements for remaining applicable frequencies in Table 6.5E.3.2.2-1 and in clause 6.5.3.2 would be considered to be verified by the measurements verifying the one uplink inter-band con-current UE to UE co-existence requirements.

Table 6.5E.3.2.2-1: Requirements for inter-band con-current V2X operation

| V2X con-current operating band cofiguration | Spurious emission |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Protected band | Frequency range (MHz) |  |  | Maximum Level (dBm) | MBW (MHz) | NOTE |
| V2X_1A_n47A |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| V2X_n1A_47A |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| V2X_8A_n47A |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| V2X_n8A_47A |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| V2X_3_n47 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| V2X_20_n38 |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| V2X_n3_47 |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| V2X_n34_47 |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| V2X_34_n47 |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| V2X_n39_47 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| V2X_39_n47 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| V2X_n40_47 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| V2X_40_n47 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| V2X_n71_47 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| V2X_n78_47 |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| V2X_n79_47 |  |  |  |  |  |  |  |
|  | Frequency range | 5925 | - | 5950 | -30 | 1 | 3, 4 |
|  | Frequency range | 5815 | - | 5855 | -30 | 1 | 3 |
| NOTE 1: Void.NOTE 2: Void.NOTE 3: Applicable when NS_33 is configured by the pre-configured radio parameters for power class 3 V2X UE.NOTE 4: In the frequency range x-5950MHz, SE requirement of -30dBm/MHz should be applied; where x = max (5925, fc + 15), where fc is the channel centre frequency. |  |  |  |  |  |  |  |

### 6.5E.4 Transmit intermodulation

#### 6.5E.4.1 Intra-band V2X

For intra-band V2X, transmit intermodulation requirements specified in clause 6.7.1G of TS 36.101 [4] and clause 6.5E.4 of TS 38.101-1 [2] apply for each frequency range respectively.

#### 6.5E.4.2 Inter-band V2X con-current operation

For the inter-band con-current NR V2X operation, the requirements specified in subclause 6.7.1 of TS 36.101 [4] shall apply for the E-UTRA uplink in licensed band and the requirements specified in subclause 6.5E.4 of TS 38.101-1 [2] shall apply for the sidelink in NR Band n47.

## 6.5H Output RF spectrum emissions for DC with UL MIMO

### 6.5H.1 Occupied bandwidth for EN-DC with UL MIMO

#### 6.5H.1.1 void

#### 6.5H.1.2 void

#### 6.5H.1.3 Inter-band EN-DC with UL MIMO within FR1

Occupied bandwidth requirement for E-UTRA single carrier specified in clauses 6.6.1 of TS 36.101 [4] and for NR single carrier specified in clause 6.5D.1 of TS 38.101-1 [2] apply.

### 6.5H.2 Out-of-band emissions for DC with UL MIMO

#### 6.5H.2.1 void

#### 6.5H.2.2 void

#### 6.5H.2.3 Inter-band EN-DC with UL MIMO within FR1

Unless otherewise stated, the OOBE requirements specified in clause 6.6.2.1 of TS 36.101 [4], sub- clause 6.6.2 of TS 36.101 [4] and clause 6.5D.2 of TS 38.101-1 [2] apply for each component carrier.

### 6.5H.3 Spurious emissions for DC with UL MIMO

#### 6.5H.3.1 void

#### 6.5H.3.2 void

6.5H.3.3 Inter-band EN-DC with UL MIMO within FR1

The requirements in 6.5B.3.3 apply and for the NR component carrier configured with UL MIMO, the configurations of UL MIMO are according to clause 6.5D.3 of TS 38.101-1 [2].

### 6.5H.4 Additional spurious emissions for DC with UL MIMO

#### 6.5H.4.1 void

#### 6.5H.4.2 void

#### 6.5H.4.3 Inter-band EN-DC with UL MIMO within FR1

The additional spurious emissions requirements specified for E-UTRA in clause 6.6.3.3 of TS 36.101 [4] and for NR UL MIMO specified in clause 6.5D.3 of TS 38.101-1 [2] apply for each component carrier.

### 6.5H.5 Transmit intermodulation for DC with UL MIMO

#### 6.5H.5.1 void

#### 6.5H.5.2 void

#### 6.5H.5.3 Inter-band EN-DC with UL MIMO within FR1

The transmit intermodulation requirement specified in clauses 6.7.1 of TS 36.101 [4] and clauses 6.5D.4 of TS 38.101-1 [2] apply for each component carrier in E-UTRA bands and NR bands, respectively.

## 6.5L Output RF spectrum emissions for DC with Tx Diversity

### 6.5L.1 Occupied bandwidth for EN-DC with Tx Diversity

#### 6.5L.1.1 void

#### 6.5L.1.2 void

#### 6.5L.1.3 Inter-band EN-DC with Tx Diversity within FR1

Occupied bandwidth requirement for E-UTRA single carrier specified in clauses 6.6.1 of TS 36.101 [4] and for NR single carrier specified in clause 6.5G.1 of TS 38.101-1 [2] apply.

### 6.5L.2 Out-of-band emissions for DC with Tx Diversity

#### 6.5L.2.1 void

#### 6.5L.2.2 void

#### 6.5L.2.3 Inter-band EN-DC with Tx Diversity within FR1

Unless otherewise stated, the OOBE requirements specified in clause 6.6.2.1 of TS 36.101 [4], sub- clause 6.6.2 of TS 36.101 [4] and clause 6.5D.2 of TS 38.101-1 [2] apply for each component carrier.

### 6.5L.3 Spurious emissions for DC with Tx Diversity

#### 6.5L.3.1 void

#### 6.5L.3.2 void

#### 6.5L.3.3 Inter-band EN-DC with Tx Diversity within FR1

The requirements in 6.5B.3.3 apply except that:

- For the NR component carrier configured with Tx Diversity, the general spurious emissions specified in clause 6.5G.3.1 of TS 38.101-1 [2] are applied, and the coexistence band protection requirements specified in clause 6.5G.3.2 of [2] are applied.

### 6.5L.4 Additional spurious emissions for DC with Tx Diversity

#### 6.5L.4.1 void

#### 6.5L.4.2 void

#### 6.5L.4.3 Inter-band EN-DC with Tx Diversity within FR1

The additional spurious emissions requirements specified for E-UTRA in clause 6.6.3.3 of TS 36.101 [4] and for NR Tx Diversity specified in clause 6.5G.3 of TS 38.101-1 [2] apply for each component carrier.

### 6.5L.5 Transmit intermodulation for DC with Tx Diversity

#### 6.5L.5.1 void

#### 6.5L.5.2 void

#### 6.5L.5.3 Inter-band EN-DC with Tx Diversity within FR1

The transmit intermodulation requirement specified in clauses 6.7.1 of TS 36.101 [4] and clauses 6.5G.4 of TS 38.101-1 [2] apply for each component carrier in E-UTRA bands and NR bands, respectively.

## 6.6B Beam correspondence for DC

6.6B.1 Void

6.6B.2 Void

6.6B.3 Void

6.6B.4 Inter-band EN-DC including FR2

Beam correspondence requirement for RRC_CONNECTED state as specified in clause 6.6 and 6.6A of TS 38.101-2 [3] apply for NR FR2 bands.

### 6.6B.4a (Void)

### 6.6B.5 Inter-band EN-DC including both FR1 and FR2

Beam correspondence requirement for RRC CONNECTED state as specified in clause 6.6 and 6.6A of TS 38.101-2 [3] apply for NR FR2 bands.

# 7 Receiver characteristics

## 7.1 General

Unless otherwise stated the receiver characteristics are specified at the antenna connector(s) of the UE for the bands operating on frequency range 1 and over the air of the UE for the bands operating on frequency range 2. The requirements for frequency range 1 and frequency range 2 can be verified separately. For the carrier in frequency range 1, requirements can be verified with NR FR2 link disabled. For the carrier in frequency range 2, requirements can be verified in OTA mode with E-UTRA or NR FR1 connecting to the network by OTA without calibration.

The requirements defined in this clause are the extra requirements compared with the single carrier requirements defined in TS 38.101-1 [2] and TS 38.101-2 [3].

Unless otherwise stated, the UL and DL reference measurement channels are the same with the configurations specified in TS 38.101-1 [2] and TS 38.101-2 [3].

Unless otherwise stated, requirements for NR receiver written in TS 38.101-1 [2] and TS 38.101-2 [3] apply and are assumed anchor agnostic. Requirements are verified under conditions where anchor resources do not interfere NR operation.

For intra-band EN-DC, the output power is configured as follows:

- One E-UTRA uplink carrier with the output power set to 29 dB below PCMAX_L and the NR band whose downlink is being tested has its uplink carrier output power set to 4 dB below PCMAX_L,f,c.

- One NR uplink carrier with the output power set to 29 dB below PCMAX_L,f,c and the E-UTRA band whose downlink is being tested has its uplink carrier output power set to 4 dB below PCMAX_L,c.

For the additional requirements for intra-band non-contiguous EN-DC of two sub-blocks, an in-gap test refers to the case when the interfering signal is located at a negative offset with respect to the assigned lowest channel frequency of the highest sub-block and located at a positive offset with respect to the assigned highest channel frequency of the lowest sub-block.

For the additional requirements for intra-band non-contiguous EN-DC of two sub-blocks, an out-of-gap test refers to the case when the interfering signal(s) is (are) located at a positive offset with respect to the assigned channel frequency of the highest carrier frequency or located at a negative offset with respect to the assigned channel frequency of the lowest carrier frequency.

For the additional requirements for intra-band non-contiguous EN-DC of two sub-blocks with channel bandwidth larger than or equal to 5 MHz, the existing adjacent channel selectivity requirements, in-band blocking requirements (for each case), and narrow band blocking requirements apply for in-gap tests only if the corresponding interferer frequency offsets with respect to the two measured carriers satisfy the following condition in relation to the sub-block gap size Wgap for at least one of the E-UTRA or NR sub-blocks, so that the interferer frequency position does not change the nature of the core requirement tested:

Wgap ≥ 2∙|FInterferer (offset)| – BWChannel

For the E-UTRA sub-block, the FInterferer (offset), for a sub-block with a single component carrier is the interferer frequency offset with respect to carrier as specified in clause 7.5.1, clause 7.6.1 and clause 7.6.3 for the respective requirement in TS 36.101 [4] and BWChannel. FInterferer (offset) for the E-UTRA sub-block with two or more contiguous component carriers is the interference frequency offset with respect to the carrier adjacent to the gap is specified in clause 7.5.1A, 7.6.1A and 7.6.3A in TS 36.101 [4].

For the NR sub-block, the FInterferer (offset), for a sub-block with a single component carrier is the interferer frequency offset with respect to carrier as specified in clause 7.5.1, clause 7.6.1 and clause 7.6.3 for the respective requirement in TS 38.101-1 [2] and BWChannel.

The interferer frequency offsets for adjacent channel selectivity, each in-band blocking case and narrow-band blocking shall be tested separately with a single in-gap interferer at a time.

For sub-clauses with suffix A or B: the minimum requirements for band combinations including Band n41 also apply for the corresponding band combinations with Band n90 replacing Band n41 but with otherwise identical parameters. For brevity the said band combinations with Band n90 are not listed in the tables below but are covered by this specification.

Unless otherwise stated, for the FR1 requirements in this clause,

- The UE shall be verified with four Rx antenna ports and skip two Rx antenna ports requirements in operating bands where the UE is equipped with four Rx antenna ports,

- the UE shall be verified with eight antenna ports and skip both two and four Rx antenna ports requirements in operating bands where the UE is equipped with eight Rx antenna ports unless UE is not supporting 8Rx ports for band(s) in band combination in which case those band(s) shall be verified with four Rx antenna ports in that band combination, otherwise, the UE shall be verified with two Rx antenna ports.

If a UE indicates both interBandMRDC-WithOverlapDL-Bands-r16 and requirementTypeIndication-r18 , it shall be verified with bothfour Rx antenna ports and two Rx antenna ports requirements.

If a UE indicates interBandMRDC-WithOverlapDL-Bands-r16 but does not indicate requirementTypeIndication-r18, it shall be verified with two Rx antenna ports requirements.Unless otherwise stated, the receiver requirements of inter-band EN-DC are applicable to UE with one or two Tx antenna connectors in NR band.

If a UE indicates interBandMRDC-WithOverlapDL-Bands-r19, it shall be verified with four Rx antenna ports requirements.  Moreover, it shall be verified with six or eight Rx antenna ports requirements when the maxMIMO-Layersis equal to six or eight, respectively.

## 7.2 Void

## 7.3 Void

## 7.3A Reference sensitivity for CA

### 7.3A.1 General

For NR CA operation, NR single carrier and CA operation of  REFSENS requirements defined in TS 38.101-1 [2] and TS 38.101-2 [3] apply to all downlink bands part of NR CA configurations listed in Table 5.2A.1-1unless sensitivity degradation is allowed as defined in clause 7.3A.

A UE which supports inter-band NR CA configuration is allowed to apply each sensitivity degradation for FR1 specified in clause 7.3A.2 TS 38.101-1 [2] and for FR2 specified in clause 7.3A.2 of TS 38.101-2 [3] independently.

### 7.3A.2 Reference sensitivity power level for CA

### 7.3A.3 ΔRIB,c for CA

For the UE which supports inter-band NR CA configuration, the minimum requirement for reference sensitivity in clause 7.3.2, 7.3A2  in TS 38.101-1 [2] and clause 7.3.2, 7.3A.2in TS 38.101-2 [3] shall be increased by the amount given in ΔRIB,c in Tables below. Unless otherwise stated, ΔRIB,c is set to zero.

In case the UE supports more than one of band combinations for CA, SUL or DC, and an operating band belongs to more than one band combinations then

- When the operating band frequency range is ≤ 1GHz, the applicable additional ∆RIB,c shall be the average value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in TS 38.101-1 [2] and 7.3A, 7.3B in this specification, truncated to one decimal place that apply for that operating band among the supported band combinations. In case there is a harmonic relation between low band UL and high band DL, then the maximum ΔRIB,c among the different supported band combinations involving such band shall be applied

- When the operating band frequency range is > 1 GHz, the applicable additional ΔRIB,c shall be the maximum value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in TS 38.101-1 [2] and 7.3A, 7.3B in this specification for the applicable operating bands.

#### 7.3A.3.1 ΔRIB,c for Inter-band CA between FR1 and FR2

ΔRIB,c is independent between FR1 and FR2. For inter-band CA between FR1 and FR2, ΔRIB,c for the FR1 band(s) from TS 38.101-1 [2] applies and ΔRIB,c for the FR2 NR band(s) is set to zero. Otherwise ΔRIB,c is set to zero.

Table 7.3A.3.1-1: Void

Table 7.3A.3.1-2: Void

Table 7.3A.3.1-3: Void

### 7.3A.4 Void

## 7.3B Reference sensitivity level for DC

### 7.3B.1 General

For EN-DC, E-UTRA and NR single carrier, CA, and MIMO operation of REFSENS requirements defined in TS38.101-1 [2], TS 38.101-2[3] and TS 36.101 [4] apply to all downlink bands of EN-DC configurations listed in clause 5.5B, unless sensitivity degradation exception is allowed in this clause of this specification, clause 7.3 in TS38.101-1 [2], clause 7.3 in TS 38.101-2 [3] or clause 7.3 in TS 36.101 [4]. Allowed exceptions specified in this clause of the specification, clause 7.3 in TS 38.101-1 [2], clause 7.3 in TS 38.101-2 [3] or clause 7.3 in TS 36.101 [4] also apply to any higher order EN-DC configuration combination containing one of the band combinations that exception is allowed for. Reference sensitivity exceptions are specified by applying maximum sensitivity degradation (MSD) into applicable REFSENS requirement. EN-DC REFSENS requirements shall be met for NR uplink transmissions using QPSK DFT-s-OFDM waveforms as defined in clause 7.3.2 [2]. Unless otherwise specified UL allocation uses the lowest SCS allowable for a given channel BW. Limits on configured maximum output power for the uplink according to clause 6.2B.4 shall apply.

In case of interband EN-DC the receiver REFSENS requirements in this clause do not apply for 1.4 and 3 MHz E-UTRA carriers. For the case of inter-band EN-DC with a single carrier per cell group and multi carrier per cell group, in addition to the E-UTRA and NR single carrier, CA, and MIMO operation of REFSENS requirements defined in TS 38.101-1 [2], TS 38.101-2[3], and TS 36.101 [4], the REFSENS requirements specified therein also apply with both downlink carriers and both uplink carriers active unless sensitivity exceptions are allowed in this clause of this specification, clause 7.3 in TS 38.101-1 [2] or clause 7.3 in TS 36.101 [4].

For reference sensitivity exception test points where the specified carrier frequency does not correspond to a valid NR-ARFCN, the closest NR-ARFCN as specified in clause 5.4.2 applies.

For operations with 4or 8 Rx antenna ports in an E-UTRA band or an NR band, the MSD in the applicable bands shall be increased by the absolute value of ΔRIB,4Rin Table 7.3.1-1aor ΔRIB,8R in Table 7.3.1-1aa of TS 36.101[4] for the E-UTRA band or ΔRIB,4R in Table 7.3.2-2or ΔRIB,8R in Table 7.3.2-2a of TS 38.101-1 for the NR band when MSD > 0.

NOTE: For inter-band EN-DC, the reference sensitivity requirement with both uplink carriers active is allowed to be verified for only a single inter-band EN-DC configuration per NR band.

For reference sensitivity level tests or reference sensitivity exception tests specified in clause 7.3B, SCS=15kHz based UL test configuration for NR bands can be replaced by SCS=30kHz based UL test configuration. The equivalent substitution relationship for NR bands between different SCS UL test configuration is shown in table 7.3B.1-1 for the NR operating bands above 2.2GHz.

Table 7.3B.1-1: Equivalent substitution relationship between different SCS UL test configurations for NR bands

| SCS (kHz) | (BW[MHz], LCRB) |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | (10, 50) | (15, 75) | (20, 100) | (25, 128) | (30, 160) | (35, 180) | (40, 216) | (45, 240) | (50, 270) |
| 30 | (10, 24) | (15, 36) | (20, 50) | (25, 64) | (30, 75) | (35, 90) | (40, 100) | (45, 108) | (50, 128) |
| NOTE 1: A Lcrb value for 30kHz SCS that is not defined in this table can be determined as the closest integer number that is lower or equal to half the corresponding Lcrb value for 15kHz SCS and satisfies the following equation: $ Number of RBs=2^{X}\times  3^{Y}\times  5^{Z}$ (where X, Y and Z are non-negative integers), except for 1 RB LCRB for 15 kHz SCS which is kept to 1 RB LCRB for 30 kHz SCS.NOTE 2: A value of RBstart for 30kHz SCS is determined as the closest integer number that is lower or equal to half the corresponding RBstart for 15 kHz SCS. If RBstart + LCRB would exceed NRB, RBstart is adjusted so that UL RB allocation fits inside NRB. |  |  |  |  |  |  |  |  |  |

### 7.3B.2 Reference sensitivity for DC

#### 7.3B.2.1 Intra-band contiguous EN-DC

For intra-band contiguous EN-DC configurations, the reference sensitivity power level REFSENS is the minimum mean power applied to each one of the UE antenna ports at which the throughput for the carrier(s) of the E-UTRA and NR CGs shall meet or exceed the requirements for the specified E-UTRA and NR reference measurement channels. The reference sensitivity requirements apply with all uplink carriers and all downlink carriers active for EN-DC configuration and Uplink EN-DC configuration listed in Table 5.5B.2-1 and Table 5.5B.3-1, as supported by the UE. For EN-DC configurations where uplink is not available in either the MCG or the SCG or for EN-DC configurations where the UE only supports single uplink operation, reference sensitivity requirements are verified with the downlink carrier(s) from the cell group without uplink shall be configured closer to the uplink operating band than any of the downlink carriers from the cell group with uplink.

Sensitivity degradation is allowed for Intra-band contiguous EN-DC configurations listed in Table 7.3B.2.1-1 the reference sensitivity is defined only for the specific uplink and downlink test points which are specified in Table 7.3B.2.1-1 and E-UTRA and NR single carrier requriements do not apply.

Table 7.3B.2.1-1: Reference sensitivity (MSD) for intra-band contiguous EN-DC

| EN-DC configuration / channel allocations /MSD |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EN-DC configuration | E-UTRA/NR band | FC (UL)(MHz) | Channel bandwidth(MHz) | ULallocation (LCRB) | FC (DL)(MHz) | MSD(dB) | Duplex mode |
| DC_(n)3AA | 3 | N/A | 15 | N/A | 1842.5 | 6.2 | FDD |
|  | n3 | 1770.0 | 30 | 10 (RBstart = 150) | 1865.0 | N/A |  |
| DC_(n)5AA | 5 | N/A | 5 | N/A | 871.5 | 5.2 | FDD |
|  | n5 | 839 | 20 | 20 (RBend = 105) | 884 | N/A |  |
| DC_(n)8AA | 8 | N/A | 10 | N/A | 935 | [20.4] | FDD |
|  | n8 | 905 | 20 | 20 (RBstart = 86) | 950 | N/A |  |
| DC_(n)12AA | 12 | N/A | 5 | N/A | 733.5 | 4.5 | FDD |
|  | n12 | 711 | 10 | 20 (RBend = 51) | 741 | N/A |  |
| DC_(n)71AA | 71 | 668 | 10 | 10 (RBstart = 0) | 622 | 17.2 | FDD |
|  | n71 | 678 | 10 | 10 (RBend = 51) | 632 | 29.4 |  |
| DC_(n)71AA4 | 71 | 668 | 10 | 10 (RBstart = 0) | 622 | 17.2 |  |
|  | n71 | 678 | 101 | 10 (RBend = 51) | 634.5 | 29.1 |  |
| DC_(n)71AA3 | 71 | N/A | 10 | N/A | 642.0 | 21.3 |  |
|  | n71 | 673.0 | 20 | 5 (RBstart = 0) | 627.0 | N/A |  |
| DC_(n)71AA4 | 71 | N/A | 5 | N/A | 639.5 | 6.8 |  |
|  | n71 | 670.5 | 151 | 5 (RBstart = 2) | 627.0 | N/A |  |
| DC_(n)71AA5 | 71 | N/A | 5 | N/A | 634.5 | 6.4 |  |
|  | n71 | 670.5 | 15 | 5 (RBstart = 0) | 624.5 | N/A |  |
| NOTE 1: In accordance to BCS1, the NR uplink bandwidth is specified as in this table, but the corresponding NR downlink bandwidth is 5 MHz larger.NOTE 2: The transmitters powers shall be set to PUMAX, as defined in TS 38.101-1 [2], TS 38.101-2 [3], and TS 36.101 [4], with additional limits on configured maximum output power for the uplink according to clause 6.2B.4.NOTE 3: Applicable only to BCS 2.NOTE 4: Applicable only to BCS 1.NOTE 5: Applicable only to BCS 0. |  |  |  |  |  |  |  |

#### 7.3B.2.1a (Void)

#### 7.3B.2.2 Intra-band non-contiguous EN-DC

For intra-band non-contiguous EN-DC configurations, the reference sensitivity power level REFSENS is the minimum mean power applied to each one of the UE antenna ports at which the throughput for the carrier(s) of the E-UTRA and NR CGs shall meet or exceed the requirements for the specified E-UTRA and NR reference measurement channels.

Sensitivity degradation is allowed for Intra-band non-contiguous EN-DC configurations listed in Table 7.3B.2.2-1, the reference sensitivity is defined only for the specific uplink and downlink test points which are specified in Table 7.3B.2.2-1 and E-UTRA and NR single carrier requriements do not apply.

For UE supporting Intra-band non-contiguous EN-DC configurations with single switched UL, no MSD is specified and E-UTRA and NR single carrier requriements apply.

Table 7.3B.2.2-1: Reference sensitivity (MSD) for intra-band non-contiguous EN-DC

| MSD / DC bandwidth class A + A |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DC configuration | E-UTRA/NR band | FC (UL)(MHz) | Channel bandwidth(MHz) | ULallocation (LCRB) | FC (DL)(MHz) | MSD(dB) | Duplex mode |
| DC_3A_n3A | 3 | 1782.5 | 5 | 12 (RBstart =0) | 1877.5 | 0112 | FDD |
|  | n3 | 1772.5 | 5 | 12 (RBend = 24) | 1867.5 | 011.52 |  |
| DC_3A_n3A | 3 | 1782.5 | 5 | 12 (RBstart = 9) | 1877.5 | 31292 |  |
|  | n3 | 1752.5 | 5 | 12 (RBstart = 0) | 1847.5 | 151312 |  |
| DC_3A_n3A | 3 | 1782.5 | 5 | 12 (RBstart = 12) | 1877.5 | 161,3 |  |
|  | n3 | 1737.5 | 5 | 12 (RBstart = 0) | 1832.5 | 331,3 |  |
| DC_3A_n3A | 3 | 1737.5 | 5 | 12 (RBstart = 0) | 1832.5 | 331,3,4 |  |
|  | n3 | 1782.5 | 5 | 12 (RBstart = 12) | 1877.5 | 161,3,4 |  |
| NOTE 1: Applicable for UE signaling with dual PA capability.NOTE 2: Applicable for UE signaling without dual PA capability.NOTE 3: The IMD also impacts Rx received blocks for UE signaling without dual PA capability but the requirements are not specified.NOTE 4: The test point is not applicable for BCS0 of DC_3A_n3A in Table 5.3B.1.3-1. |  |  |  |  |  |  |  |

#### 7.3B.2.3 Inter-band EN-DC within FR1

##### 7.3B.2.3.0 General

7.3B.2.3.0.0 MSD requirements with Look-Up tables

Reference sensitivity exceptions are specified for the condition when there is uplink transmission only in the aggressor band.

The PC2 and PC1.5 MSD requirements with look-up tables for two or three DL band EN-DC with 1UL or 2UL DC band do not apply when the UL band is either band 46/n46, band n96 or band n102.

7.3B.2.3.0.1 PC2 and PC1.5 MSD requirements with look-up tables for two-band DL EN-DC with 1UL band single CC

The PC2 and the PC1.5 MSD requirements with look-up tables for two-band EN-DC reference sensitivity exceptions (MSD) due to 1UL band 1UL CC harmonic, harmonic mixing, and cross band isolation interference shall apply when the following criterias are met:

- A PC3 reference sensitivity exception requirement is specified either in Table 7.3B.2.3.1-1, or in Table 7.3B.2.3.2-1 or in Table 7.3B.2.3.4-1, and

- A PC2 reference sensitivity exception requirement is not specified respectively in Table 7.3B.2.3.2-1a, or in Table 7.3B.2.3.4-1a, and PC1.5 reference sensitivity exception requirement is not specified, and

- PC2 is specified in Table 6.2B.1.3-1 and PC2 output power is specified as a valid per band power class in Table 6.2B.1.3-1a, denoted here “PC21Tx”, or PC2 is specified in Table 6.2H.1.3-1 and PC2 is specified as a valid per band power class in Table 6.2H.1.3-1a, denoted here “PC22Tx”, or PC1.5 is specified in Table 6.2H.1.3-1 and PC1.5 output power is specified as a valid per band power class in Table 6.2H.1.3-1a, denoted here “PC1.52Tx”, and,

-  The PCx aggressor UL band is the same aggressor UL band as in case of PC3 MSD.

For these cases, and where in the following PCx denotes either PC21Tx, PC22Tx or PC1.52Tx, the PCx MSD due to harmonic, harmonic mixing, and cross band isolation is specified as:

PCx MSD = PC3 MSD + MSD


where,

- PCx MSD is the reference sensitivity exception specified for PC21Tx, PC22Tx, or PC1.52Tx,

- PC3 MSD is the reference sensitivity exception specified for PC3 in Table 7.3B.2.3.1-1, or in Table 7.3B.2.3.2-1 or in Table 7.3B.2.3.4-1

- MSD values are specified in Table 7.3B.2.3.0.1-1 output columns denoted “MSDmax 3, 6, 9”. These apply to the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in Table 7.3B.2.3.1-1, or in Table 7.3B.2.3.2-1 or in Table 7.3B.2.3.4-1,

- The correspondence between the MSDmax specified in Table 7.3B.2.3.0.1-1, the source of interference and PCx MSD is specified in Table 7.3B.2.3.0.1-2,

Table 7.3B.2.3.0.1-1: MSD per MSDmax look-up table for MSD due to harmonic, harmonic mixing, cross band isolation

| PC3 MSD (dB) | MSDmax / MSD(dB) |  |  |
| --- | --- | --- | --- |
|  | 3 | 6 | 9 |
| 0.1≤ PC3 MSD <1.0 | 0.7 | 1.1 | 2.5 |
| 1.0≤ PC3 MSD <3.0 | 1.6 | 2.7 | 5.1 |
| 3.0≤ PC3 MSD <5.0 | 2.0 | 3.8 | 6.5 |
| 5.0≤ PC3 MSD <7.0 | 2.3 | 4.5 | 7.3 |
| 7.0≤ PC3 MSD <9.0 | 2.5 | 5.0 | 7.9 |
| PC3 MSD ≥9.0 | 3 | 6 | 9 |

Table 7.3B.2.3.0.1-2: MSDmax correspondence look-up table for source of interference and PCx MSD

| Source of interference | MSDmax |  |  |
| --- | --- | --- | --- |
|  | PC21Tx MSD | PC22Tx MSD | PC1.52Tx MSD |
| UL harmonic | 3 | 6 | 9 |
| Harmonic mixing | 3 | 6 | 9 |
| Cross band isolation | 3 | 6 | 9 |

As an exception, for cases where:

- The PC21Tx MSD is specified in Table 7.3B.2.3.2-1a or in Table 7.3B.2.3.4-1a, and

- The PC3 MSD is not specified in Table 7.3B.2.3.2-1, or in Table 7.3B.2.3.4-1, and

- The PC1.5 MSD is not specified, and

- PC1.5 is specified in Table 6.2H.1.3-1 and PC1.5 output power is specified as a valid per band power class in Table 6.2H.1.3-1a, denoted here as “PC1.52Tx”, and,

then the PC1.52Tx MSD is specified as:

PC1.52Tx MSD = PC21Tx MSD + MSD,

where in the Table 7.3B.2.3.0.1-1,

- MSD is specified output column denoted “MSDmax 6”,

- The input column uses the specified “PC21Tx MSD” instead of “PC3 MSD”. These apply to the same uplink/downlink configurations as those specified for the minimum PC2 MSD requirements in Table 7.3B.2.3.2-1a or in Table 7.3B.2.3.4-1a.


7.3B.2.3.0.2 PC2 and PC1.5 MSD requirements with look-up tables for two-band or three-band DL EN-DC with two-band UL EN-DC and a single CC per UL band.

The PC2 and the PC1.5 MSD requirements with look-up tables for two-band and three-band DL EN-DC reference sensitivity exceptions (MSD) due to 2UL EN-DC intermodulation interference shall apply when the following criterias are met:

- A PC3 reference sensitivity exception requirement is specified either in Table 7.3B.2.3.5.1-1, or in Table 7.3B.2.3.5.2-1, and,

- A PC2 reference sensitivity exception requirement is not specified respectively in Table 7.3B.2.3.5.1-1a or in Table 7.3B.2.3.5.2-1a and PC1.5 reference sensitivity exception requirement is not specified, and,

- PC2 or PC1.5 two-band UL EN-DC for a total of 2Tx or 3Tx and 1CC in each UL band is specified as a valid two-band UL EN-DC configuration in Table 6.2B.1.3-1, or in Table 6.2H.1.3-1, and,

- The PC2 or PC1.5 MSD is caused by the same uplink/downlink configurations as in case of PC3 MSD.

For these cases, and where in the following PCx denotes either PC2 or PC1.5, the PCx MSD due to 2UL EN-DC intermodulation interference is specified as:

PCx MSD = PC3 MSD + MSD

where,

- PCx MSD is the reference sensitivity exception specified for PC2 or PC1.5 with 2UL band EN-DC for a total of 2Tx or 3Tx and with 1UL CC in each UL band,

- PC3 MSD is the reference sensitivity exception specified for PC3 in Table 7.3B.2.3.5.1-1, or in Table 7.3B.2.3.5.2-1,

- MSD values are specified in Table 7.3B.2.3.0.2-1 output columns denoted “MSDmax 6, 9, 12, 15, 18, 24, 30”. These apply for the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in Table 7.3B.2.3.5.1-1, or in Table 7.3B.2.3.5.2-1, and,

- The correspondence between the MSDmax specified in Table 7.3B.2.3.0.2-1, the IMD order and PCx MSD is specified in Table 7.3B.2.3.0.2-2,

Table 7.3B.2.3.0.2-1: MSD per MSDmax look-up table for MSD due to 2UL EN-DC intermodulation interference

| PC3 MSD (dB) | MSDmax / MSD(dB) |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 6 | 9 | 12 | 15 | 18 | 24 | 30 |
| 0.1≤ PC3 MSD <0.5 | 1.2 | 2.4 | 3.9 | 5.8 | 7.9 | 13.2 | 18.8 |
| 0.5≤ PC3 MSD <1.0 | 1.7 | 3.5 | 5.4 | 7.5 | 10.0 | 15.6 | 21.4 |
| 1.0≤ PC3 MSD <2.0 | 2.8 | 4.8 | 7.1 | 9.6 | 12.4 | 18.0 | 24.1 |
| 2.0≤ PC3 MSD <3.0 | 3.5 | 5.7 | 8.2 | 10.9 | 13.7 | 19.5 | 25.5 |
| 3.0≤ PC3 MSD <4.0 | 3.9 | 6.3 | 8.9 | 11.7 | 14.5 | 20.5 | 26.5 |
| 4.0≤ PC3 MSD <5.0 | 4.3 | 6.8 | 9.4 | 12.4 | 15.2 | 21.2 | 27.2 |
| 5.0≤ PC3 MSD <6.0 | 4.5 | 7.1 | 9.9 | 12.8 | 15.8 | 21.7 | 27.7 |
| 6.0≤ PC3 MSD <7.0 | 4.8 | 7.6 | 10.4 | 13.3 | 16.2 | 22.3 | 28.2 |
| 7.0≤ PC3 MSD <8.0 | 5.0 | 7.8 | 10.7 | 13.6 | 16.6 | 22.5 | 28.5 |
| 8.0≤ PC3 MSD <9.0 | 5.2 | 8.1 | 11.0 | 14.0 | 16.9 | 22.8 | 28.8 |
| PC3 MSD ≥9.0 | 6 | 9 | 12 | 15 | 18 | 24 | 30 |

Table 7.3B.2.3.0.2-2: MSDmax correspondence look-up table for IMD order and PCx MSD

| IMD order | MSDmax |  |
| --- | --- | --- |
|  | PC2 MSD | PC1.5 MSD |
| IMD2 | 6 | 12 |
| IMD3 | 9 | 18 |
| IMD4 | 12 | 24 |
| IMD5 | 15 | 30 |

As an exception, for cases where:

- The PC2 MSD is specified in Table 7.3B.2.3.5.1-1a or in Table 7.3B.2.3.5.2-1a, and,

- The PC3 MSD is not specified in Table 7.3B.2.3.5.1-1or in Table 7.3B.2.3.5.2-1, and,

- The PC1.5 MSD is not specified, and,

- PC1.5 two-band UL EN-DC for a total of 2Tx or 3Tx and 1CC in each UL band is specified as a valid two-band UL EN-DC configuration in Table 6.2B.1.3-1, or in Table 6.2H.1.3-1.

then the PC1.5 MSD is specified as:

PC1.5 MSD = PC2 MSD + MSD,

where,

- In the Table 7.3B.2.3.0.2-1, MSD is specified with output columns denoted “MSDmax 6, 9, 12, 15” and where the input column uses the specified PC2 MSD specified in Table 7.3B.2.3.5.1-1a or in Table 7.3B.2.3.5.2-1a instead of the PC3 MSD, and

- In the Table 7.3B.2.3.0.2-2, the correspondence between the MSDmax and the IMD order is specified using the column specified for “PC2 MSD”, and

- These PC1.5 MSD requirements apply for the same uplink/downlink configurations as those specified in the PC2 MSD requirements of Table 7.3B.2.3.5.1-1a or in Table 7.3B.2.3.5.2-1a.

In all cases, the MSD requirements specified in Table 7.3B.2.3.0.2-1 and in Table 7.3B.2.3.0.2-2 do not apply to 2UL band EN-DC configurations with 3UL CCs, e.g. a combination of intra-band and inter-band dual connectivity.

7.3B.2.3.0.3 PC2 and PC1.5 MSD requirements with look-up tables for two-band DL EN-DC with 2UL CC in NR TDD band.

The PC2 and the PC1.5 MSD requirements with look-up tables for two-band DL EN-DC reference sensitivity exceptions (MSD) due to 1UL NR TDD band with 2UL CC intermodulation interference shall apply when the following criteria are met:

- The UL band is a NR TDD band configured with intra-band contiguous UL CA, and,

- A PC3 reference sensitivity exception requirement is specified in Table 7.3B.2.3.5.1-1, and the corresponding PC2 reference sensitivity exception requirement is not specified in Table 7.3B.2.3.5.1-1a,

- PC2 or PC1.5 power class is specified in Table 6.2B.1.3-1 or Table 6.2H.1.3-1

- The PCx aggressor NR UL band is the same aggressor UL band as in case of PC3 MSD.

For these cases, and where in the following PCx denotes either PC2 or PC1.5, the PCx MSD due to 1UL NR TDD band with two contiguous UL CC intermodulation interference is specified as:

PCx MSD = PC3 MSD + MSD

where,

- PC3 MSD is the reference sensitivity exception specified in Table 7.3B.2.3.5.1-1,

- For IMD3 and IMD5 MSD values are specified in Table 7.3B.2.3.0.1-1 output column denoted “MSDmax 3” for PC2 and “MSDmax 6” for PC1.5,

- For IMD4 and ≥ IMD6 MSD values are specified in Table 7.3B.2.3.0.2-1 output columns denoted “MSDmax  9” for PC2 and “MSDmax 15” for PC1.5,

- These apply for the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in Table 7.3B.2.3.5.1-1,

- The correspondence between the MSDmax specified in Table 7.3A.2.3.2.1-1, the IMD order and PCx MSD is specified in Table 7.3B.2.3.0.3-1,

Table 7.3B.2.3.0.3-1: MSDmax correspondence look-up table for 1UL band 2UL CC IMD order and PCx MSD

| IMD order | MSDmax |  |
| --- | --- | --- |
|  | PC2 MSD | PC1.5 MSD |
| IMD3 | 3 | 6 |
| IMD4 | 9 | 15 |
| IMD5 | 3 | 6 |
| ≥ IMD6 | 9 | 15 |

In all cases, the MSD requirements specified in Table 7.3B.2.3.0.3-1 do not apply to 1UL FDD band CA configurations with two UL CCs, and in this case, MSD shall be specified in Table 7.3B.2.3.5.1-1a for PC2, or in a new table for PC1.5.

7.3B.2.3.0.4 PC2 and PC1.5 MSD requirements with look-up tables for two-band or three-band DL EN-DC with two-band UL EN-DC with 2UL CC in NR TDD band.

The PC2 and the PC1.5 MSD requirements with look-up tables for two-band and three-band DL EN-DC reference sensitivity exceptions (MSD) due to 2UL band EN-DC IMD3 interference from 2UL CC in the NR TDD band and 1UL CC in the LTE FDD band, (also known as 1st order triple-beat MSD) shall apply when the following criteria are met:

- The NR UL band is configured with intra-band contiguous UL CA is a TDD band, and,

- The LTE UL band is configured with 1UL CC is a FDD band, and

- A PC3 reference sensitivity exception requirement is specified in Table 7.3B.2.3.5.1-1 or in Table 7.3B.2.3.5.2-1, and the corresponding PC2 reference sensitivity exception requirement is not specified in Table Table 7.3B.2.3.5.1-1a or Table 7.3B.2.3.5.2-1a,

- PC2 or PC1.5 power class is specified in Table 6.2B.1.2-1 or Table 6.2H.1.3-1,

- The PCx aggressor NR UL band is the same aggressor UL band as in case of PC3 MSD.

For these cases, and where in the following PCx denotes either PC2 or PC1.5, the PCx MSD due to 2UL band EN-DC IMD3 interference with two contiguous UL CC in the NR band and 1UL CC in the LTE band is specified as:

PCx MSD = PC3 MSD + MSD

where,

- PC3 MSD is the reference sensitivity exception specified for PC3 in 7.3B.2.3.5.1-1, or in 7.3B.2.3.5.2-1,

- MSD values are specified in Table 7.3B.2.3.0.2-1 column denoted “MSDmax 6” for PC2 and “MSDmax 12” for PC1.5. These apply for the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in 7.3B.2.3.5.1-1, or in Table 7.3B.2.3.5.2-1,

##### 7.3B.2.3.1 Reference sensitivity exceptions due to UL harmonic interference for EN-DC in NR FR1

Sensitivity degradation is allowed for different combinations of UL configurations and DL channel bandwidths if a band if it is impacted by UL harmonic interference from another band part of the same EN-DC configuration. Reference sensitivity exceptions for the victim band (high) and uplink/downlink configurations due to UL harmonic from a PC3 aggressor UL band (low) for either single band uplink or PC3 or PC2 EN-DC are specified in Table 7.3B.2.3.1-1 For these exceptions, only the listed test points in Table 7.3B.2.3.1-1 need to be tested.

Table 7.3B.2.3.1-1: Reference sensitivity exceptions (MSD) due to UL harmonic for EN-DC in NR FR1

| UL band | DL band | UL BW | SCS of UL band | UL RB Allocation | DL BW | MSD | UL/DL fc condition | UL/DL harmonic order |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | (MHz) | (kHz) | LCRB | (MHz) | (dB) |  |  |
| 1 | n77 | 5 | 15 | 12 | 10 | 23.9 | NOTE 2 | UL2/DL1direct-hit |
| 1 | n77 | 5 | 15 | 12 | 100 | 13.8 | NOTE 2 | UL2/DL1direct-hit |
| 2 | n48 | 5 | 15 | 25 | 10 | 8.1 | NOTE 6 | UL2/DL1near-miss |
| n2 | 48 | 5 | 15 | 25 | 5 | 8.1 | NOTE 6 | UL2/DL1near-miss |
| 2 | n77 | 5 | 15 | 12 | 10 | 23.9 | NOTE 2 | UL2/DL1direct-hit |
| 2 | n77 | 5 | 15 | 12 | 100 | 13.8 | NOTE 2 | UL2/DL1direct-hit |
| 2 | n78 | 5 | 15 | 12 | 10 | 23.9 | NOTE 2 | UL2/DL1direct-hit |
| 2 | n78 | 5 | 15 | 12 | 100 | 13.8 | NOTE 2 | UL2/DL1direct-hit |
| 3 | n77 | 5 | 15 | 12 | 10 | 23.9 | NOTE 2 | UL2/DL1direct-hit |
| 3 | n77 | 5 | 15 | 12 | 100 | 13.8 | NOTE 2 | UL2/DL1direct-hit |
| 3 | n78 | 5 | 15 | 12 | 10 | 23.9 | NOTE 2 | UL2/DL1direct-hit |
| 3 | n78 | 5 | 15 | 12 | 100 | 13.8 | NOTE 2 | UL2/DL1direct-hit |
| n3 | 42 | 5 | 15 | 12 | 5 | 27.3 | NOTE 2 | UL2/DL1direct-hit |
| n3 | 42 | 5 | 15 | 12 | 20 | 21.3 | NOTE 2 | UL2/DL1direct-hit |
| 4 | n78 | 5 | 15 | 12 | 10 | 23.9 | NOTE 2 | UL2/DL1direct-hit |
| 4 | n78 | 5 | 15 | 12 | 100 | 13.8 | NOTE 2 | UL2/DL1direct-hit |
| 5 | n778 | 5 | 15 | 6 | 10 | 10.5 | NOTE 4 | UL4/DL1direct-hit |
| 5 | n778 | 5 | 15 | 6 | 100 | 2.9 | NOTE 4 | UL4/DL1direct-hit |
| 5 | n778 | 5 | 15 | 5 | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 5 | n778 | 5 | 15 | 5 | 100 | 2.9 | NOTE 5 | UL5/DL1direct-hit |
| 5 | n78 | 5 | 15 | 6 | 10 | 10.5 | NOTE 4 | UL4/DL1direct-hit |
| 5 | n78 | 5 | 15 | 6 | 100 | 2.9 | NOTE 4 | UL4/DL1direct-hit |
| 7 | n79 | 5 | 15 | 25 | 10 | 9.3 | NOTE 6 | UL2/DL1near-miss |
| 8 | n311 | NA | NA |  | NA | NA | NOTE 2 | UL2/DL1direct-hit |
| 8 | n7 | 5 | 15 | 8 | 5 | 10 | NOTE 3 | UL3/DL1direct-hit |
| 8 | n7 | 5 | 15 | 8 | 50 | 1.1 | NOTE 3 | UL3/DL1direct-hit |
| 8 | n41 | 5 | 15 | 8 | 10 | 13 | NOTE 3 | UL3/DL1direct-hit |
| 8 | n41 | 5 | 15 | 8 | 100 | 4.5 | NOTE 3 | UL3/DL1direct-hit |
| 8 | n77 | 5 | 15 | 6 | 10 | 10.8 | NOTE 4 | UL4/DL1direct-hit |
| 8 | n77 | 5 | 15 | 6 | 100 | 3.1 | NOTE 4 | UL4/DL1direct-hit |
| 8 | n78 | 5 | 15 | 6 | 10 | 10.8 | NOTE 4 | UL4/DL1direct-hit |
| 8 | n78 | 5 | 15 | 6 | 100 | 3.1 | NOTE 4 | UL4/DL1direct-hit |
| 8 | n79 | 5 | 15 | 5 | 10 | 12.0 | NOTE 5 | UL5/DL1direct-hit |
| 8 | n79 | 5 | 15 | 5 | 100 | 4.4 | NOTE 5 | UL5/DL1direct-hit |
| n8 | 311 | NA | NA | NA | NA | NA | NOTE 2 | UL2/DL1direct-hit |
| n8 | 7 | 5 | 15 | 8 | 5 | 10 | NOTE 3 | UL3/DL1direct-hit |
| n8 | 7 | 5 | 15 | 8 | 20 | 5.3 | NOTE 3 | UL3/DL1direct-hit |
| n12 | 48 | 5 | 15 | 5 | 5 | 13 | NOTE 5 | UL5/DL1direct-hit |
| n12 | 48 | 5 | 15 | 5 | 20 | 7.8 | NOTE 5 | UL5/DL1direct-hit |
| 12 | n66 | 5 | 15 | 8 | 5 | 10 | NOTE 3 | UL3/DL1direct-hit |
| 12 | n66 | 5 | 15 | 8 | 40 | 3.1 | NOTE 3 | UL3/DL1direct-hit |
| n12 | 66 | 5 | 15 | 8 | 5 | 10 | NOTE 3 | UL3/DL1direct-hit |
| n12 | 66 | 5 | 15 | 8 | 20 | 5.5 | NOTE 3 | UL3/DL1direct-hit |
| 12 | n77 | 5 | 15 | 5 | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 12 | n77 | 5 | 15 | 5 | 100 | 2.9 | NOTE 5 | UL5/DL1direct-hit |
| 12 | n78 | 5 | 15 | 5 | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 12 | n78 | 5 | 15 | 5 | 100 | 2.9 | NOTE 5 | UL5/DL1direct-hit |
| 13 | n77 | 5 | 15 |  | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 13 | n77 | 5 | 15 | 5 | 100 | 2.9 | NOTE 5 | UL5/DL1direct-hit |
| 14 | n77 | 5 | 15 | 5 | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 14 | n77 | 5 | 15 | 5 | 100 | 2.9 | NOTE 5 | UL5/DL1direct-hit |
| 18 | n77 | 5 | 15 | 5 | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 18 | n77 | 5 | 15 | 5 | 100 | 2.9 | NOTE 5 | UL5/DL1direct-hit |
| 18 | n78 | 5 | 15 | 5 | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 18 | n78 | 5 | 15 | 5 | 100 | 2.9 | NOTE 5 | UL5/DL1direct-hit |
| 19 | n77 | 5 | 15 | 5 | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 19 | n77 | 5 | 15 | 5 | 100 | 2.9 | NOTE 5 | UL5/DL1direct-hit |
| 19 | n77 | 5 | 15 | 6 | 10 | 10.5 | NOTE 4 | UL4/DL1direct-hit |
| 19 | n77 | 5 | 15 | 6 | 100 | 2.9 | NOTE 4 | UL4/DL1direct-hit |
| 19 | n78 | 5 | 15 | 6 | 10 | 10.5 | NOTE 4 | UL4/DL1direct-hit |
| 19 | n78 | 5 | 15 | 6 | 100 | 2.9 | NOTE 4 | UL4/DL1direct-hit |
| 20 | n38 | 5 | 15 | 8 | 5 | 12.9 | NOTE 3 | UL3/DL1direct-hit |
| 20 | n38 | 5 | 15 | 8 | 50 | 4.3 | NOTE 3 | UL3/DL1direct-hit |
| 20 | n41 | 5 | 15 | 8 | 10 | 10.3 | NOTE 3 | UL3/DL1direct-hit |
| 20 | n41 | 5 | 15 | 8 | 100 | 1.5 | NOTE 3 | UL3/DL1direct-hit |
| 20 | n77 | 5 | 15 | 6 | 10 | 10.8 | NOTE 4 | UL4/DL1direct-hit |
| 20 | n77 | 5 | 15 | 6 | 100 | 3.1 | NOTE 4 | UL4/DL1direct-hit |
| 20 | n78 | 5 | 15 | 6 | 10 | 10.8 | NOTE 4 | UL4/DL1direct-hit |
| 20 | n78 | 5 | 15 | 6 | 100 | 3.1 | NOTE 4 | UL4/DL1direct-hit |
| 25 | n77 | 5 | 15 | 12 | 10 | 23.9 | NOTE 2 | UL2/DL1direct-hit |
| 25 | n77 | 5 | 15 | 12 | 100 | 13.8 | NOTE 2 | UL2/DL1direct-hit |
| 25 | n78 | 5 | 15 | 12 | 10 | 23.9 | NOTE 2 | UL2/DL1direct-hit |
| 25 | n78 | 5 | 15 | 12 | 100 | 13.8 | NOTE 2 | UL2/DL1direct-hit |
| n25 | 48 | 5 | 15 | 25 | 5 | 8.1 | NOTE 6 | UL2/DL1near-miss |
| 26 | n41 | 5 | 15 | 8 | 10 | 10.3 | NOTE 3 | UL3/DL1direct-hit |
| 26 | n41 | 5 | 15 | 8 | 100 | 2.7 | NOTE 3 | UL3/DL1direct-hit |
| 26 | n77 | 5 | 15 | 6 | 10 | 10.8 | NOTE 4 | UL4/DL1direct-hit |
| 26 | n77 | 5 | 15 | 6 | 100 | 3.1 | NOTE 4 | UL4/DL1direct-hit |
| 26 | n78 | 5 | 15 | 6 | 10 | 10.8 | NOTE 4 | UL4/DL1direct-hit |
| 26 | n78 | 5 | 15 | 6 | 100 | 3 | NOTE 4 | UL4/DL1direct-hit |
| 28 | n1 | 5 | 15 | 8 | 5 | 10.2 | NOTE 3 | UL3/DL1direct-hit |
| 28 | n1 | 5 | 15 | 8 | 50 | 2.6 | NOTE 3 | UL3/DL1direct-hit |
| n28 | 1 | 5 | 15 | 8 | 5 | 10.2 | NOTE 3 | UL3/DL1direct-hit |
| n28 | 1 | 5 | 15 | 8 | 20 | 5.3 | NOTE 3 | UL3/DL1direct-hit |
| n28 | 4 | 5 | 15 | 8 | 5 | 10.2 | NOTE 3 | UL3/DL1direct-hit |
| n28 | 4 | 5 | 15 | 8 | 20 | 5.3 | NOTE 3 | UL3/DL1direct-hit |
| n28 | 11 | 5 | 15 | 12 | 5 | 24.8 | NOTE 2 | UL2/DL1direct-hit |
| n28 | 11 | 5 | 15 | 12 | 10 | 21.8 | NOTE 2 | UL2/DL1direct-hit |
| n28 | 2112 | NA | NA | NA | NA | NA | NOTE 2 | UL2/DL1direct-hit |
| n28 | 2112 | NA | NA | NA | NA | NA | NOTE 2 | UL2/DL1direct-hit |
| n28 | 32 | 5 | 15 | 12 | 5 | 28.1 | NOTE 2 | UL2/DL1direct-hit |
| n28 | 32 | 5 | 15 | 12 | 20 | 21.9 | NOTE 2 | UL2/DL1direct-hit |
| n28 | 42 | 5 | 15 | 5 | 5 | 14.1 | NOTE 5 | UL5/DL1direct-hit |
| n28 | 42 | 5 | 15 | 5 | 20 | 8.6 | NOTE 5 | UL5/DL1direct-hit |
| 28 | n50 | 5 | 15 | 5 | 10 | 24.6 | NOTE 2 | UL2/DL1direct-hit |
| 28 | n50 | 5 | 15 | 12 | 80 | 15.8 | NOTE 2 | UL2/DL1direct-hit |
| 28 | n51 | 5 | 15 | 12 | 5 | 28.1 | NOTE 2 | UL2/DL1direct-hit |
| n28 | 66 | 5 | 15 | 8 | 5 | 10.2 | NOTE 3 | UL3/DL1direct-hit |
| n28 | 66 | 5 | 15 | 8 | 20 | 5.3 | NOTE 3 | UL3/DL1direct-hit |
| 28 | n66 | 5 | 15 | 8 | 5 | 10.2 | NOTE 3 | UL3/DL1direct-hit |
| 28 | n66 | 5 | 15 | 8 | 40 | 3.2 | NOTE 3 | UL3/DL1direct-hit |
| 28 | n75 | 5 | 15 | 12 | 5 | 28.1 | NOTE 2 | UL2/DL1direct-hit |
| 28 | n75 | 5 | 15 | 12 | 50 | 17.9 | NOTE 2 | UL2/DL1direct-hit |
| 28 | n77 | 5 | 15 | 5 | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 28 | n77 | 5 | 15 | 5 | 100 | 2.9 | NOTE 5 | UL5/DL1direct-hit |
| 28 | n78 | 5 | 15 | 5 | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 28 | n78 | 5 | 15 | 5 | 100 | 2.9 | NOTE 5 | UL5/DL1direct-hit |
| 66 | n48 | 5 | 15 | 12 | 10 | 24.4 | NOTE 2 | UL2/DL1direct-hit |
| n66 | 48 | 5 | 15 | 12 | 5 | 27.1 | NOTE 2 | UL2/DL1direct-hit |
| 66 | n77 | 5 | 15 | 12 | 10 | 23.9 | NOTE 2 | UL2/DL1direct-hit |
| 66 | n77 | 5 | 15 | 12 | 100 | 13.8 | NOTE 2 | UL2/DL1direct-hit |
| 66 | n78 | 5 | 15 | 12 | 10 | 23.9 | NOTE 2 | UL2/DL1direct-hit |
| 66 | n78 | 5 | 15 | 12 | 100 | 13.8 | NOTE 2 | UL2/DL1direct-hit |
| 68 | n1 | 5 | 15 | 8 | 5 | 10.2 | NOTE 3 | UL3/DL1direct-hit |
| 68 | n77 | 5 | 15 | 5 | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 68 | n78 | 5 | 15 | 5 | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 71 | n7 | 5 | 15 | 6 | 5 | 14.6 | NOTE 4 | UL4/DL1direct-hit |
| 71 | n7 | 5 | 15 | 6 | 50 | 2.1 | NOTE 4 | UL4/DL1direct-hit |
| n71 | 7 | 5 | 15 | 6 | 5 | 14.6 | NOTE 4 | UL4/DL1direct-hit |
| n71 | 7 | 5 | 15 | 6 | 20 | 9 | NOTE 4 | UL4/DL1direct-hit |
| 71 | n2510 | 5 | 15 | 8 | 5 | 6.9 | NOTE 3 | UL3/DL1direct-hit |
| 71 | n2510 | 5 | 15 | 8 | 20 | 2.9 | NOTE 3 | UL3/DL1direct-hit |
| 71 | n41 | 5 | 15 | 6 | 10 | 10.8 | NOTE 4 | UL4/DL1direct-hit |
| 71 | n41 | 5 | 15 | 6 | 100 | 3.1 | NOTE 4 | UL4/DL1direct-hit |
| 71 | n77 | 5 | 15 | 5 | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 71 | n77 | 5 | 15 | 5 | 100 | 2.9 | NOTE 5 | UL5/DL1direct-hit |
| 71 | n78 | 5 | 15 | 5 | 10 | 10.4 | NOTE 5 | UL5/DL1direct-hit |
| 71 | n78 | 5 | 15 | 5 | 100 | 2.9 | NOTE 5 | UL5/DL1direct-hit |
| n105 | 7 | 5 | 15 | 6 | 5 | 18 | NOTE 4 | UL4/DL1direct-hit |
| n105 | 7 | 5 | 15 | 6 | 20 | 12 | NOTE 4 | UL4/DL1direct-hit |
| 106 | n41 | 3 | 15 | 8 | 10 | 13 | NOTE 3 | UL3/DL1direct-hit |
| 106 | n41 | 3 | 15 | 8 | 100 | 4.5 | NOTE 3 | UL3/DL1direct-hit |
| 106 | n48 | 3 | 15 | 6 | 10 | 10.5 | NOTE 4 | UL4/DL1direct-hit |
| 106 | n48 | 3 | 15 | 6 | 100 | 2.9 | NOTE 4 | UL4/DL1direct-hit |
| NOTE 1: The direct-hit requirements apply when there is at least one individual RE within the uplink transmission bandwidth of the aggressor (lower) band for which the 2nd / 3rd / 4th / 5th transmitter harmonic is within the downlink transmission bandwidth of a victim (higher) band. The requirements should be verified using RBstart = floor((NRB-LCRB)/2), where floor(x) is the greatest integer less than or equal to x, and where the UL parameters NRB and LCRB are respectively, the transmission bandwidth configuration and the number of RB’s for the specified UL band channel bandwidth and the UL band subcarrier spacing.NOTE 2: The requirements should be verified for UL EARFCN or NR ARFCN of the aggressor (lower) band (superscript LB) such that ![](media_svg/image9.svg) [公式≈: f_{UL}^{LB}=_{√}f_{DL}^{HB}/0.2_{∃}0.1]in MHz and ![](media_svg/image10.svg) [公式≈: ^{FBWfFBW}ULlowChannelULULhighChannel^{LBLBLBLBLB}__^{+≥≥−}^{/2/2}] with carrier frequency in the victim (higher) band in MHz and  the channel bandwidth configured in the lower band.This DL band may be affected by near-miss interference for which the MSD is not specified. NOTE 3: The requirements should be verified for UL EARFCN or NR ARFCN of the aggressor (lower) band (superscript LB) such that ![](media_svg/image11.svg) [公式≈: ff_{ULDL}^{LBHB}=⋅∂_{√∃}/0.30.1] in MHz and ![](media_svg/image10.svg) [公式≈: ^{FBWfFBW}ULlowChannelULULhighChannel^{LBLBLBLBLB}__^{+≥≥−}^{/2/2}] with the carrier frequency in the victim (higher) band in MHz and  the channel bandwidth configured in the low band.NOTE 4: The requirements should be verified for UL EARFCN or NR ARFCN of the aggressor (lower) band (superscript LB) such that ![](media_svg/image12.svg) [公式≈: f_{UL}^{LB}=_{√}f_{DL}^{HB}/0.4_{∃}0.1]in MHz and ![](media_svg/image10.svg) [公式≈: ^{FBWfFBW}ULlowChannelULULhighChannel^{LBLBLBLBLB}__^{+≥≥−}^{/2/2}] with carrier frequency in the victim (higher) band in MHz and  the channel bandwidth configured in the lower band.NOTE 5: The requirements should be verified for UL EARFCN or NR-ARFCN of the aggressor (lower) band (superscript LB) such that ![](media_svg/image15.svg) [公式≈: f_{UL}^{LB}=_{√}f_{DL}^{HB}/0.5_{∃}0.1]in MHz and ![](media_svg/image10.svg) [公式≈: ^{FBWfFBW}ULlowChannelULULhighChannel^{LBLBLBLBLB}__^{+≥≥−}^{/2/2}] with carrier frequency in the victim (higher) band in MHz and  the channel bandwidth configured in the lower band.NOTE 6: The near-miss requirements are only applicable when direct-hit requirements do not apply.   These requirements should be verified for downlink channel bandwidths no larger than 10 MHz and with a carrier frequency at $\pm  \left ( 10+BW_{Channel}^{HB}/2\right ) $ MHz offset from ![](media_svg/image16.svg) [公式≈: _{2}_{f}_{UL}LB] in the victim (higher band) with ![](media_svg/image10.svg) [公式≈: ^{FBWfFBW}ULlowChannelULULhighChannel^{LBLBLBLBLB}__^{+≥≥−}^{/2/2}], whereand![](media_svg/image17.svg) [公式≈: ^{BW}Channel^{HB}]are the channel bandwidths configured in the aggressor (lower) and victim (higher) bands in MHz, respectively.NOTE 7: For these bandwidths, the minimum requirements are restricted to operation when carrier is configured as a downlink carrier part of CA configuration.NOTE 8: For a UE which supports this band combination only when the Band n77 frequency range restriction defined in NOTE 12 of Table 5.2-1 from TS 38.101-1 applies, the MSD test point(s) cannot be verified for the band combination and the test point(s) can be skipped.NOTE 9: Void.NOTE 10: These requirements apply when the upper edge frequency of the 5 MHz uplink channel in Band 71 is located at or below 668 MHz and the downlink channel in Band n25 is located with its upper edge at 1995 MHz.NOTE 11: No requirements apply when there is at least one individual RE within the uplink transmission bandwidth of the low band for which the 2nd transmitter harmonic is within the downlink transmission bandwidth of the high band. The reference sensitivity for all active downlink component carriers is only verified when this is not the case (the requirements specified in clause 7.3.1 from TS 36.101-1 apply unless otherwise specified).NOTE 12: The frequency range in band n28 is restricted for this band combination to 728 - 738 MHz for the UL. This band is subject to 2nd harmonic fall in B21 also which MSD is not specified.NOTE 13: Void. |  |  |  |  |  |  |  |  |

Table 7.3B.2.3.1-2: Void

Table 7.3B.2.3.1-3: Reference sensitivity QPSK PREFSENS (EN-DC with n46)

| E-UTRA or NR Band / Channel bandwidth of the affected DL band / MSD |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UL band | DL band | 5MHz(dB) | 10 MHz(dB) | 15 MHz(dB) | 20 MHz(dB) | 25 MHz(dB) | 40 MHz(dB) | 50 MHz(dB) | 60 MHz(dB) | 80 MHz(dB) | 90 MHz(dB) | 100 MHz(dB) |
| 2 | n461 |  |  |  | N/A |  | N/A |  | N/A | N/A |  |  |
| n46 | 22,3 | 28 | 28 | 28 | 28 |  |  |  |  |  |  |  |
| n46 | 482,4 | 22.6 | 19.5 | 17.8 | 16.6 |  |  |  |  |  |  |  |
| 66 | n46 |  |  |  | N/A |  | N/A |  | N/A | N/A |  |  |
| NOTE 1: These requirements apply when there is at least one individual RE within the downlink (victim) transmission bandwidth which falls into the reference sensitivity exclusion region as specified in Table 6.x.1.7-2 and Table 6.x.1.7-3.NOTE 2:  These requirements apply when there is at least one individual RE within the uplink transmission bandwidth of the aggressor (higher) band and when the frequency range of relative higher band’s uplink channel bandwidth or uplink 1st adjacent channel bandwidth is fully or partially overlapped with the downlink transmission bandwidth of a victim (lower) band.NOTE 3:   The requirements for a victim (lower) band apply for UL EARFCN of the aggressor (higher) band (superscript HB) such that ![](media/cid:image004.png@01D629D8.2A3DDB60)  in MHz and $ F_{UL\_low}^{HB}+BW_{Channel}^{HB}/2\leq  f_{UL}^{HB}\leq  F_{UL\_high}^{HB}-BW_{Channel}^{HB}/2 $ with ![](media/cid:image005.png@01D629D8.2A3DDB60)  the DL carrier frequency in the lower band and  the channel bandwidth configured in the higher band, both in MHz.NOTE 4:  The requirements should be verified for UL NR-ARFCN of the aggressor (high) band (superscript HB) such that  $ f_{UL}^{HB}=\lfloor  15*f_{DL}^{LB}\rfloor  0.1 $  in MHz and  $ F_{UL\_low}^{HB}+BW_{Channel}^{HB}/2\leq  f_{UL}^{HB}\leq  F_{UL\_high}^{HB}-BW_{Channel}^{HB}/2 $ with  with ![](media_svg/image21.svg) [公式≈: _{f}_{DL}LB] carrier frequency in the victim (lower) band in MHz and the channel bandwidth configured in the higher band. |  |  |  |  |  |  |  |  |  |  |  |  |

Table 7.3B.2.3.1-4: Void

Table 7.3B.2.3.1-5: Uplink configuration for reference sensitivity exceptions due to receiver harmonic mixing for EN-DC paring with n46

| E-UTRA or NR Band / SCS / Channel bandwidth of the affected DL band / UL RB allocation of the agressor band |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UL band | DL band | SCS of UL band(kHz) | 5 MHz(LCRB) | 10 MHz(LCRB) | 15 MHz(LCRB) | 20 MHz(LCRB) | 25 MHz(LCRB) | 40 MHz(LCRB) | 50 MHz(LCRB) | 60 MHz(LCRB) | 80 MHz(LCRB) | 90 MHz(LCRB) | 100 MHz(LCRB) |
| n46 | 2 | 15 | 25 | 50 | 75 | 100 |  |  |  |  |  |  |  |
| n46 | 48 | 15 | 12 | 25 | 36 | 50 |  |  |  |  |  |  |  |

##### 7.3B.2.3.2 Reference sensitivity exceptions due to receiver harmonic mixing for EN-DC in NR FR1

Sensitivity degradation is allowed for different combinations of UL configurations and DL channel bandwidths if a band is impacted by receiver harmonic mixing due to another band part of the same EN-DC configuration. Reference sensitivity exceptions for the victim band (low) and uplink/downlink configurations due to UL harmonic from a PC3 aggressor UL band (high) for either single band uplink or PC3 or PC2 EN-DC are specified in Table 7.3B.2.3.2-1.

Reference sensitivity exceptions and uplink/downlink configurations due to harmonic mixing from a PC2 aggressor UL for PC2 EN-DC are specified in Table 7.3B.2.3.2-1a.

For these exceptions, only the listed test points in Table 7.3B.2.3.2-1 and Table 7.3B.2.3.2-1a need to be tested.

Table 7.3B.2.3.2-1: Reference sensitivity exceptions (MSD) due to receiver harmonic mixing for EN-DC in NR FR1

| UL band | DL band | UL BW | SCS of UL band | UL RB Allocation | DL BW | MSD | UL/DL fc condition | UL/DL harmonic order |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | (MHz) | (kHz) | LCRB | (MHz) | (dB) |  |  |
| 1 | n71 | 5 | 15 | 25 | 5 | 26.8 | NOTE 4 | UL1/DL3 |
| 1 | n71 | 5 | 15 | 25 | 20 | 15.6 | NOTE 4 | UL1/DL3 |
| 1 | n105 | 5 | 15 | 25 | 5 | 26.8 | NOTE 4 | UL1/DL3 |
| 1 | n105 | 5 | 15 | 25 | 20 | 16.5 | NOTE 4 | UL1/DL3 |
| 2 | n71 | 5 | 15 | 25 | 5 | 26.8 | NOTE 4 | UL1/DL3 |
| 2 | n71 | 5 | 15 | 25 | 20 | 15.6 | NOTE 4 | UL1/DL3 |
| n2 | 71 | 5 | 15 | 25 | 5 | 26.8 | NOTE 4 | UL1/DL3 |
| n2 | 71 | 5 | 15 | 25 | 20 | 17.1 | NOTE 4 | UL1/DL3 |
| 7 | n2612 | 5 | 15 | 25 | 5 | [2.0] | NOTE 4 | UL1/DL3 |
| 7 | n105 | 5 | 15 | 25 | 5 | 5.7 | NOTE 14 | UL1/DL4 |
| 7 | n105 | 5 | 15 | 25 | 20 | 1 | NOTE 14 | UL1/DL4 |
| n25 | 71 | 5 | 15 | 25 | 5 | 26.8 | NOTE 4 | UL1/DL3 |
| n25 | 71 | 5 | 15 | 25 | 20 | 17.1 | NOTE 4 | UL1/DL3 |
| 30 | n14 | 10 | 15 | 50 | 5 | 1.6 | NOTE 16 | UL1/DL3Near miss |
| n38 | 59 | NA | NA | NA | NA | NA | NOTE 4 | UL1/DL3 |
| n40 | 20 | 10 | 15 | 25 | 5 | 27.8 | NOTE 4 | UL1/DL3 |
| n40 | 20 | 10 | 15 | 25 | 20 | 20.8 | NOTE 4 | UL1/DL3 |
| n40 | 28 | 10 | 15 | 25 | 5 | 37.8 | NOTE 4 | UL1/DL3 |
| n40 | 28 | 10 | 15 | 25 | 20 | 30.3 | NOTE 4 | UL1/DL3 |
| n40 | 68 | 10 | 15 | 25 | 5 | 37.8 | NOTE 4 | UL1/DL3 |
| n41 | 5 | 10 | 15 | 25 | 5 | 24.3 | NOTE 4 | UL1/DL3 |
| n41 | 5 | 10 | 15 | 25 | 10 | 21.3 | NOTE 4 | UL1/DL3 |
| n41 | 18 | 10 | 15 | 25 | 5 | 26.3 | NOTE 4 | UL1/DL3 |
| n41 | 18 | 10 | 15 | 25 | 15 | 21.5 | NOTE 4 | UL1/DL3 |
| n41 | 26 | 10 | 15 | 25 | 5 | 23.8 | NOTE 4 | UL1/DL3 |
| n41 | 26 | 10 | 15 | 25 | 15 | 19 | NOTE 4 | UL1/DL3 |
| n46 | 2 | 20 | 15 | 25 | 5 | 28 | NOTE 4 | UL1/DL3 |
| n46 | 48 | 20 | 15 | 12 | 5 | 26.8 | NOTE 2 | UL2/DL3 |
| n46 | 48 | 20 | 15 | 12 | 20 | 20.8 | NOTE 2 | UL2/DL3 |
| 48 | n12 | 5 | 15 | 25 | 5 | 31 | NOTE 2 | UL1/DL5 |
| 48 | n12 | 5 | 15 | 25 | 10 | 27.8 | NOTE 2 | UL1/DL5 |
| n77 | 2 | 10 | 15 | 25 | 5 | 6.7 | NOTE 13 | UL1/DL2 |
| n77 | 2 | 10 | 15 | 25 | 20 | 2.9 | NOTE 13 | UL1/DL2 |
| n77 | 3 | 10 | 15 | 25 | 5 | 5.7 | NOTE 13 | UL1/DL2 |
| n77 | 3 | 10 | 15 | 25 | 20 | 2.3 | NOTE 13 | UL1/DL2 |
| n77 | 5 | 10 | 15 | 25 | 5 | 5.7 | NOTE 14 | UL1/DL4 |
| n77 | 7 | 10 | 15 | 12 | 5 | 13.4 | NOTE 8 | UL2/DL3 |
| n77 | 7 | 10 | 15 | 12 | 20 | 7.9 | NOTE 8 | UL2/DL3 |
| n77 | 12 | 10 | 15 | 25 | 5 | 31 | NOTE 2 | UL1/DL5 |
| n77 | 12 | 10 | 15 | 25 | 10 | 28 | NOTE 2 | UL1/DL5 |
| n77 | 13 | 10 | 15 | 25 | 5 | 31 | NOTE 2 | UL1/DL5 |
| n77 | 13 | 10 | 15 | 25 | 10 | 28 | NOTE 2 | UL1/DL5 |
| n77 | 14 | 10 | 15 | 25 | 5 | 31 | NOTE 2 | UL1/DL5 |
| n77 | 14 | 10 | 15 | 25 | 10 | 28 | NOTE 2 | UL1/DL5 |
| n77 | 19 | 10 | 15 | 25 | 5 | 7.3 | NOTE 14 | UL1/DL4 |
| n77 | 19 | 10 | 15 | 25 | 15 | 3.9 | NOTE 14 | UL1/DL4 |
| n77 | 25 | 10 | 15 | 25 | 5 | 5.6 | NOTE 13 | UL1/DL2 |
| n77 | 25 | 10 | 15 | 25 | 20 | 2.2 | NOTE 13 | UL1/DL2 |
| n77 | 28 | 10 | 15 | 25 | 5 | 31 | NOTE 2 | UL1/DL5 |
| n77 | 28 | 10 | 15 | 25 | 20 | 23.5 | NOTE 2 | UL1/DL5 |
| n77 | 29 | 10 | 15 | 25 | 5 | 31 | NOTE 2 | UL1/DL5 |
| n77 | 29 | 10 | 15 | 25 | 10 | 28 | NOTE 2 | UL1/DL5 |
| n77 | 40 | 10 | 15 | 12 | 5 | 14.7 | NOTE 4 | UL2/DL3 |
| n77 | 40 | 10 | 15 | 12 | 20 | 9.1 | NOTE 4 | UL2/DL3 |
| n77 | 41 | 10 | 15 | 12 | 5 | 14.7 | NOTE 8 | UL2/DL3 |
| n77 | 41 | 10 | 15 | 12 | 20 | 9.1 | NOTE 8 | UL2/DL3 |
| n77 | 68 | 10 | 15 | 25 | 5 | 31 | NOTE 2 | UL1/DL5 |
| n78 | 2 | 10 | 15 | 25 | 5 | 6.7 | NOTE 13 | UL1/DL2 |
| n78 | 2 | 10 | 15 | 25 | 20 | 2.9 | NOTE 13 | UL1/DL2 |
| n78 | 3 | 10 | 15 | 25 | 5 | 5.7 | NOTE 13 | UL1/DL2 |
| n78 | 3 | 10 | 15 | 25 | 20 | 2.3 | NOTE 13 | UL1/DL2 |
| n78 | 5 | 10 | 15 | 25 | 5 | 5.7 | NOTE 14 | UL1/DL4 |
| n78 | 8 | 10 | 15 | 25 | 5 | 5.7 | NOTE 14 | UL1/DL4 |
| n78 | 8 | 10 | 15 | 25 | 20 | 3.8 | NOTE 14 | UL1/DL4 |
| n78 | 12 | 10 | 15 | 25 | 5 | 31 | NOTE 2 | UL1/DL5 |
| n78 | 12 | 10 | 15 | 25 | 10 | 28 | NOTE 2 | UL1/DL5 |
| n78 | 12 | 10 | 15 | 25 | 5 | 34 | NOTE 2 | UL1/DL5 |
| n78 | 12 | 10 | 15 | 25 | 15 | 31 | NOTE 2 | UL1/DL5 |
| n78 | 13 | 10 | 15 | 25 | 5 | 31 | NOTE 2 | UL1/DL5 |
| n78 | 13 | 10 | 15 | 25 | 10 | 28 | NOTE 2 | UL1/DL5 |
| n78 | 19 | 10 | 15 | 25 | 5 | 7.3 | NOTE 14 | UL1/DL4 |
| n78 | 19 | 10 | 15 | 25 | 15 | 3.9 | NOTE 14 | UL1/DL4 |
| n78 | 26 | 10 | 15 | 25 | 5 | 8.1 | NOTE 14 | UL1/DL4 |
| n78 | 40 | 10 | 15 | 12 | 5 | 14.7 | NOTE 8 | UL2/DL3 |
| n78 | 40 | 10 | 15 | 12 | 20 | 9.1 | NOTE 8 | UL2/DL3 |
| n78 | 41 | 10 | 15 | 12 | 5 | 14.7 | NOTE 8 | UL2/DL3 |
| n78 | 41 | 10 | 15 | 12 | 20 | 9.1 | NOTE 8 | UL2/DL3 |
| n78 | 68 | 10 | 15 | 25 | 5 | 31 | NOTE 2 | UL1/DL5 |
| n79 | 5 | 10 | 15 | 25 | 5 | 27.5 | NOTE 2 | UL1/DL5 |
| n79 | 8 | 10 | 15 | 25 | 5 | 25 | NOTE 2 | UL1/DL5 |
| n79 | 8 | 10 | 15 | 25 | 10 | 22 | NOTE 2 | UL1/DL5 |
| n79 | 11 | 10 | 15 | 25 | 5 | 39.3 | NOTE 4 | UL1/DL3 |
| n79 | 11 | 10 | 15 | 25 | 10 | 36.3 | NOTE 4 | UL1/DL3 |
| n79 | 19 | 10 | 15 | 25 | 5 | 29.5 | NOTE 2 | UL1/DL5 |
| n79 | 19 | 10 | 15 | 25 | 15 | 24.7 | NOTE 2 | UL1/DL5 |
| n79 | 21 | 10 | 15 | 25 | 5 | 39.3 | NOTE 4 | UL1/DL3 |
| n79 | 21 | 10 | 15 | 25 | 15 | 34.5 | NOTE 4 | UL1/DL3 |
| n79 | 26 | 10 | 15 | 25 | 5 | 27 | NOTE 2 | UL1/DL5 |
| n79 | 26 | 10 | 15 | 25 | 15 | 22.2 | NOTE 2 | UL1/DL5 |
| NOTE 1: These requirements apply when there is at least one individual RE within the uplink transmission bandwidth of the aggressor (higher) band for which the mixing product due to harmonic of victim (lower) band LO with leakage of aggressor (higher) band is within the downlink transmission bandwidth of a victim (lower) band.NOTE 2: The requirements should be verified for DL EARFCN of the victim (lower) band (superscript LB) such that ![](media_svg/image22.svg) [公式≈: f_{DL}^{LB}=_{√}f_{UL}^{HB}/0.5_{∃}0.1]  and $ F_{UL\_low}^{HB}+BW_{Channel}^{HB}/2\leq  f_{UL}^{HB}\leq  F_{UL\_high}^{HB}-BW_{Channel}^{HB}/2 $ with ![](media_svg/image23.svg) [公式≈: _{f}_{DL}LB] the DL carrier frequency in the lower band and $ f_{UL}^{HB}$ the UL carrier frequency and $ BW_{Channel}^{HB}$ the channel bandwidth configured in the higher band, both in MHz.NOTE 3: Void.NOTE 4: The requirements should be verified for DL EARFCN or NR ARFCN of the victim (lower) band (superscript LB) such that ![](media_svg/image24.svg) [公式≈: ff_{DLUL}^{LBHB}=⋅∂_{√∃}/0.30.1]  and $ F_{UL\_low}^{HB}+BW_{Channel}^{HB}/2\leq  f_{UL}^{HB}\leq  F_{UL\_high}^{HB}-BW_{Channel}^{HB}/2 $ with ![](media_svg/image23.svg) [公式≈: _{f}_{DL}LB]  the DL carrier frequency in the lower band and $ f_{UL}^{HB}$ the UL carrier frequency and $ BW_{Channel}^{HB}$ the channel bandwidth configured in the higher band, both in MHz. NOTE 5: VoidNOTE 6: VoidNOTE 7: VoidNOTE 8: The requirements should be verified for DL EARFCN of the  victim (lower) band (superscript LB) such that $ f_{DL}^{LB}=\lfloor  f_{UL}^{HB}/0.15\rfloor  0.1 $   and $ BW_{Channel}^{HB}$ the channel bandwidth configured with![](media_svg/image21.svg) [公式≈: _{f}_{DL}LB] the DL carrier frequency in the lower band and $ f_{UL}^{HB}$ the UL carrier frequency and $ BW_{Channel}^{HB}$ the channel bandwidth configured in the higher band, both in MHz. NOTE 9: No requirements apply for the case that there is at least one individual RE within the uplink transmission bandwidth of the relative higher band and when the frequency range of relative higher band’s uplink channel bandwidth or uplink 1st adjacent channel bandwidth is fully or partially overlapped with the 3 times of the frequency range of the relative lower band’s downlink channel bandwidth. The reference sensitivity is only verified when this is not the case.NOTE 10: MSD test point can be chosen according to supported BW and lowest SCS supported by the UE.NOTE 11: The MSD test points cannot be verified for the band combination in US due to the Band n77 frequency range restriction.NOTE 12: The requirements should be verified for the lowest NR ARFCN of the affected DL (lower) band and for the highest NR ARFCN of the UL (higher) bandNOTE 13: The requirements should be verified for DL EARFCN or NR ARFCN of the victim (lower) band (superscript LB) such that $ f_{DL}^{LB}=\lfloor  f_{UL}^{HB}/0.2\rfloor  0.1 $  and $ F_{UL\_low}^{HB}+BW_{Channel}^{HB}/2\leq  f_{UL}^{HB}\leq  F_{UL\_high}^{HB}-BW_{Channel}^{HB}/2 $ with ![](media_svg/image23.svg) [公式≈: _{f}_{DL}LB]  the DL carrier frequency in the lower band and $ f_{UL}^{HB}$ the UL carrier frequency in the higher band, both in MHz. NOTE 14: The requirements should be verified for DL EARFCN or NR ARFCN of the victim (lower) band (superscript LB) such that $ f_{DL}^{LB}=\lfloor  f_{UL}^{HB}/0.4\rfloor  0.1 $  and $ F_{UL\_low}^{HB}+BW_{Channel}^{HB}/2\leq  f_{UL}^{HB}\leq  F_{UL\_high}^{HB}-BW_{Channel}^{HB}/2 $ with ![](media_svg/image23.svg) [公式≈: _{f}_{DL}LB]  the DL carrier frequency in the lower band and $ f_{UL}^{HB}$ the UL carrier frequency in the higher band, both in MHz. NOTE 15: The requirements should be verified using RBstart = floor((NRB-LCRB)/2), where floor(x) is the greatest integer less than or equal to x, and where the UL parameters NRB and LCRB are respectively, the transmission bandwidth configuration and the number of RB’s for the specified UL band channel bandwidth and the UL band subcarrier spacing.NOTE 16: The requirements should be verified for the highest NR ARFCN of the affected DL (lower) band and for the lowest NR ARFCN of the UL (higher) band. |  |  |  |  |  |  |  |  |

Table 7.3B.2.3.2-1a: Reference sensitivity exceptions (MSD) due to receiver harmonic mixing for PC2 EN-DC in NR FR1

| UL band | DL band | UL BW | SCS of UL band | UL RB Allocation | DL BW | MSD | UL/DL fc condition | UL/DL harmonic order |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | (MHz) | (kHz) | LCRB | (MHz) | (dB) |  |  |
| n41 | 5 | 10 | 15 | 25 | 5 | 27.3 | NOTE 4 | UL1/DL3 |
| n41 | 26 | 10 | 15 | 25 | 5 | 26.8 | NOTE 4 | UL1/DL3 |
| n41 | 18 | 10 | 15 | 25 | 5 | 29.3 | NOTE 4 | UL1/DL3 |
| n77 | 2 | 10 | 15 | 25 | 5 | 9.2 | NOTE 6 | UL1/DL2 |
| n77 | 2 | 10 | 15 | 25 | 20 | 4.5 | NOTE 6 | UL1/DL2 |
| n77 | 3 | 10 | 15 | 25 | 5 | 8.1 | NOTE 6 | UL1/DL2 |
| n77 | 3 | 10 | 15 | 25 | 20 | 3.8 | NOTE 6 | UL1/DL2 |
| n77 | 12 | 10 | 15 | 25 | 5 | 34 | NOTE 1 | UL1/DL5 |
| n77 | 12 | 10 | 15 | 25 | 10 | 31 | NOTE 1 | UL1/DL5 |
| n77 | 13 | 10 | 15 | 25 | 5 | 34 | NOTE 1 | UL1/DL5 |
| n77 | 13 | 10 | 15 | 25 | 10 | 31 | NOTE 1 | UL1/DL5 |
| n77 | 14 | 10 | 15 | 25 | 5 | 34 | NOTE 1 | UL1/DL5 |
| n77 | 14 | 10 | 15 | 25 | 10 | 31 | NOTE 1 | UL1/DL5 |
| n77 | 19 | 10 | 15 | 25 | 5 | 9.8 | NOTE 6 | UL1/DL2 |
| n77 | 19 | 10 | 15 | 25 | 15 | 5.9 | NOTE 6 | UL1/DL2 |
| n77 | 28 | 10 | 15 | 25 | 5 | 34 | NOTE 1 | UL1/DL5 |
| n77 | 28 | 10 | 15 | 25 | 20 | 26.5 | NOTE 1 | UL1/DL5 |
| n772 | 29 | 10 | 15 | 25 | 5 | 34 | NOTE 1 | UL1/DL5 |
| n772 | 29 | 10 | 15 | 25 | 10 | 31 | NOTE 1 | UL1/DL5 |
| n77 | 40 | 10 | 15 | 12 | 5 | 17.7 | NOTE 4 | UL2/DL3 |
| n77 | 40 | 10 | 15 | 12 | 20 | 11.9 | NOTE 4 | UL2/DL3 |
| n77 | 41 | 10 | 15 | 12 | 5 | 17.7 | NOTE 4 | UL2/DL3 |
| n77 | 41 | 10 | 15 | 12 | 20 | 11.9 | NOTE 4 | UL2/DL3 |
| n78 | 3 | 10 | 15 | 25 | 5 | 8.1 | NOTE 6 | UL1/DL2 |
| n78 | 3 | 10 | 15 | 25 | 20 | 3.8 | NOTE 6 | UL1/DL2 |
| n78 | 8 | 10 | 15 | 25 | 5 | 8.1 | NOTE 5 | UL1/DL4 |
| n78 | 8 | 10 | 15 | 25 | 10 | 5.7 | NOTE 5 | UL1/DL4 |
| n78 | 5 | 10 | 15 | 25 | 5 | 8.1 | NOTE 5 | UL1/DL4 |
| n78 | 13 | 10 | 15 | 25 | 5 | 34 | NOTE 1 | UL1/DL5 |
| n78 | 19 | 10 | 15 | 25 | 5 | 9.8 | NOTE 5 | UL1/DL4 |
| n78 | 19 | 10 | 15 | 25 | 15 | 5.9 | NOTE 5 | UL1/DL4 |
| n78 | 28 | 10 | 15 | 25 | 5 | 34 | NOTE 1 | UL1/DL5 |
| n78 | 28 | 10 | 15 | 25 | 20 | 26.5 | NOTE 1 | UL1/DL5 |
| n78 | 40 | 10 | 15 | 12 | 5 | 17.7 | NOTE 4 | UL2/DL3 |
| n78 | 40 | 10 | 15 | 12 | 20 | 11.9 | NOTE 4 | UL2/DL3 |
| n78 | 41 | 10 | 15 | 12 | 5 | 17.7 | NOTE 4 | UL2/DL3 |
| n78 | 41 | 10 | 15 | 12 | 20 | 11.9 | NOTE 4 | UL2/DL3 |
| n79 | 19 | 10 | 15 | 25 | 5 | 32.5 | NOTE 1 | UL1/DL5 |
| n79 | 19 | 10 | 15 | 25 | 15 | 27.7 | NOTE 1 | UL1/DL5 |
| n79 | 21 | 10 | 15 | 25 | 5 | 42.3 | NOTE 3 | UL1/DL3 |
| n79 | 21 | 10 | 15 | 25 | 15 | 37.5 | NOTE 3 | UL1/DL3 |
| NOTE 1: The requirements should be verified for DL EARFCN of the victim (lower) band (superscript LB) such that ![](media_svg/image22.svg) [公式≈: f_{DL}^{LB}=_{√}f_{UL}^{HB}/0.5_{∃}0.1] and $ F_{UL\_low}^{HB}+BW_{Channel}^{HB}/2\leq  f_{UL}^{HB}\leq  F_{UL\_high}^{HB}-BW_{Channel}^{HB}/2 $  with ![](media_svg/image23.svg) [公式≈: _{f}_{DL}LB] the DL carrier frequency in the lower band and $ f_{UL}^{HB}$ the UL carrier frequency and $ BW_{Channel}^{HB}$ the channel bandwidth configured in the higher band, both in MHz.NOTE 2: For a UE which supports this band combination only when the Band n77 frequency range restriction defined in NOTE 12 of Table 5.2-1 from TS 38.101-1 applies, the MSD test point(s) cannot be verified for the band combination and the test point(s) can be skipped.NOTE 3: The requirements should be verified for DL EARFCN or NR ARFCN of the victim (lower) band (superscript LB) such that ![](media_svg/image24.svg) [公式≈: ff_{DLUL}^{LBHB}=⋅∂_{√∃}/0.30.1]  and $ F_{UL\_low}^{HB}+BW_{Channel}^{HB}/2\leq  f_{UL}^{HB}\leq  F_{UL\_high}^{HB}-BW_{Channel}^{HB}/2 $  with ![](media_svg/image23.svg) [公式≈: _{f}_{DL}LB] the DL carrier frequency in the lower band and $ f_{UL}^{HB}$ the UL carrier frequency and $ BW_{Channel}^{HB}$ the channel bandwidth in the higher band, both in MHz.NOTE 4: The requirements should be verified for DL EARFCN of the  victim (lower) band (superscript LB) such that $ f_{DL}^{LB}=\lfloor  f_{UL}^{HB}/0.15\rfloor  0.1 $  and $ F_{UL\_low}^{HB}+BW_{Channel}^{HB}/2\leq  f_{UL}^{HB}\leq  F_{UL\_high}^{HB}-BW_{Channel}^{HB}/2 $ with the DL carrier frequency in the lower band and $ f_{UL}^{HB}$ the UL carrier frequency  and $ BW_{Channel}^{HB}$ the channel bandwidth in the higher band, both in MHz.NOTE 5: The requirements should be verified for UL NR-ARFCN of the aggressor (higher) band (superscript HB) such that ![](media_svg/image26.svg) [公式≈: f_{DL}^{LB}=_{√}f_{UL}^{HB}/0.4_{∃}0.1]  in MHz and $ F_{UL\_low}^{HB}+BW_{Channel}^{HB}/2\leq  f_{UL}^{HB}\leq  F_{UL\_high}^{HB}-BW_{Channel}^{HB}/2 $ with  the carrier frequency in the victim (lower) band and  the channel bandwidth configured in the higher bandNOTE 6: The requirements should be verified for DL EARFCN or NR ARFCN of the victim (lower) band (superscript LB) such that $ f_{DL}^{LB}=\lfloor  f_{UL}^{HB}/0.2\rfloor  0.1 $ and $ F_{UL\_low}^{HB}+BW_{Channel}^{HB}/2\leq  f_{UL}^{HB}\leq  F_{UL\_high}^{HB}-BW_{Channel}^{HB}/2 $   with ![](media_svg/image23.svg) [公式≈: _{f}_{DL}LB]  the DL carrier frequency in the lower band and $ f_{UL}^{HB}$ the UL carrier frequency in the higher band, both in MHz. NOTE 7: The requirements should be verified using RBstart = floor((NRB-LCRB)/2), where floor(x) is the greatest integer less than or equal to x, and where the UL parameters NRB and LCRB are respectively, the transmission bandwidth configuration and the number of RB’s for the specified UL band channel bandwidth and the UL band subcarrier spacing. |  |  |  |  |  |  |  |  |

Table 7.3B.2.3.2-2: Void

##### 7.3B.2.3.3 Void

##### 7.3B.2.3.4 Reference sensitivity exceptions due to cross band isolation for EN-DC in NR FR1

Sensitivity degradation is allowed for a band if it is impacted by UL of another band part of the same EN-DC configuration due to cross band isolation issues. Reference sensitivity exceptions for the victim band are specified only for the specific uplink and downlink test points specified in Table 7.3B.2.3.4-1 and Table 7.3B.2.3.4-1a.

In Tables 7.3B.2.3.4-1 and 7.3B.2.3.4-1a the following terminology is used to define the source of cross-band isolation interference:

- “ACLR1” indicates that the first adjacent channel of the aggressor UL band falls into the Rx channel of victim band.

- “ACLR2” indicates that the second adjacent channel of the aggressor UL band falls into the Rx channel of victim band.

- “>ACLR2” indicates that neither the first, nor the second adjacent channel of the aggressor UL band falls into the Rx channel of victim band.

Table 7.3B.2.3.4-1: Reference sensitivity exceptions (MSD) due to cross band isolation and uplink/downlink configurations for PC3 EN-DC in NR FR1

| UL band | DL band | UL Fc | UL BW | SCS of UL band | UL RB Allocation | DL Fc | DL BW | MSD | Cross-bandInterferencesource |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | (MHz) | (MHz) | (kHz) | LCRB | (MHz) | (MHz) | (dB) |  |
| n1 | 3 | 1922.5 | 5 | 15 | 25 (RBstart=0) | 1877.5 | 5 | 3 | >ACLR2 |
| n1 | 3 | 1945 | 50 | 15 | 128 (RBstart=0) | 1877.5 | 5 | 19.7 | ACLR1 |
| n1 | 38 | 1955 | 50 | 15 | 128 (RBstart=142) | 2572.5 | 5 | 2.9 | >ACLR2 |
| n1 | 40 | 1955 | 50 | 15 | 128 (RBstart=142) | 2302.5 | 5 | 6.6 | >ACLR2 |
| n1 | 41 | 1955 | 50 | 15 | 128 (RBstart=142) | 2498.5 | 5 | 6.1 | >ACLR2 |
| 1 | n3 | 1930 | 20 | 15 | 100 (RBstart=0) | 1877.5 | 5 | [7.9] | >ACLR2 |
| 1 | n3 | 1922.5 | 5 | 15 | 25 (RBstart=0) | 1877.5 | 5 | 3 | >ACLR2 |
| 1 | n40 | 1970 | 20 | 15 | 100 (RBstart=0) | 2305 | 10 | 6.6 | >ACLR2 |
| 1 | n41 | 1970 | 20 | 15 | 100 (RBstart=0) | 2501 | 10 | 6.1 | >ACLR2 |
| n3 | 11 | 1735 | 50 | 15 | 50 (RBstart=0) | 1493.4 | 5 | 6.4 | >ACLR2 |
| n3 | 11 | 1712.5 | 5 | 15 | 25 (RBstart=0) | 1493.4 | 5 | 6.4 | >ACLR2 |
| n3 | 41 | 1760 | 50 | 15 | 50 (RBstart=220) | 2498.5 | 5 | 0.7 | >ACLR2 |
| 3 | n41 | 1775 | 20 | 15 | 50 (RBstart=50) | 2501 | 10 | 0.7 | >ACLR2 |
| 3 | n51 | 1720 | 20 | 15 | 50 (RBstart=0) | 1429.5 | 5 | 6.4 | >ACLR2 |
| 3 | n51 | 1712.5 | 5 | 15 | 25 (RBstart=0) | 1429.5 | 5 | 6.4 | >ACLR2 |
| n5 | 28 | 834 | 20 | 15 | 20 (RBstart=0) | 800.5 | 5 | 17.5 | ACLR2 |
| 5 | n28 | 829 | 10 | 15 | 25 (RBstart=0) | 800.5 | 5 | 11.4 | >ACLR2 |
| 7 | n40 | 2510 | 20 | 15 | 75 (RBstart=0) | 2395 | 10 | 3.7 | >ACLR2 |
| n12 | 71 | 706.5 | 15 | 15 | 20 (RBstart=0) | 649.5 | 5 | 3.8 | >ACLR2 |
| 12 | n71 | 704 | 10 | 15 | 20 (RBstart=0) | 649.5 | 5 | 3.8 | >ACLR2 |
| 18 | n287 | 822.5 | 15 | 15 | 25 (RBstart=0) | 800.5 | 5 | 31.3 | ACLR1 |
| 18 | n28 | 822.5 | 15 | 15 | 25 (RBstart=0) | 785.5 | 5 | 12.7 | ACLR2 |
| n25 | 2 | 1895 | 40 | 15 | 40 (RBstart=176) | 1932.5 | 5 | 33 | ACLR1 |
| 28 | n71 | 713 | 20 | 15 | 25 (RBstart=0) | 649.5 | 5 | 5.7 | >ACLR2 |
| 28 | n105 | 713 | 20 | 15 | 25 (RBstart=0) | 649.5 | 5 | 5.7 | >ACLR2 |
| 30 | n66 | 2310 | 10 | 15 | 25 (RBstart=0) | 2177.5 | 5 | 8.3 | >ACLR2 |
| n34 | 3 | 2017.5 | 15 | 15 | 75 (RBstart=0) | 1877.5 | 5 | 3 | >ACLR2 |
| n38 | 1 | 2590 | 40 | 15 | 216 (RBstart=0) | 2167.5 | 5 | 1.9 | >ACLR2 |
| n38 | 2 | 2590 | 40 | 15 | 216 (RBstart=0) | 1987.5 | 5 | 0.6 | >ACLR2 |
| n38 | 4 | 2590 | 40 | 15 | 216 (RBstart=0) | 2152.5 | 5 | 1.9 | >ACLR2 |
| n38 | 66 | 2590 | 40 | 15 | 216 (RBstart=0) | 2177.5 | 5 | 1.9 | >ACLR2 |
| 38 | n1 | 2580 | 20 | 15 | 100 (RBstart=0) | 2167.5 | 5 | 1.9 | >ACLR2 |
| 39 | n41 | 1910 | 20 | 15 | 100 (RBstart=0) | 2501 | 10 | [3.3] | >ACLR2 |
| n40 | 1 | 2350 | 100 | 30 | 270 (RBstart=0) | 2167.5 | 5 | [21.9] | ACLR2 |
| n40 | 7 | 2350 | 100 | 30 | 270 (RBstart=3) | 2622.5 | 5 | 22.3 | >ACLR2 |
| 40 | n1 | 2310 | 20 | 15 | 100 (RBstart=0) | 2167.5 | 5 | 8.3 | >ACLR2 |
| 40 | n7 | 2390 | 20 | 15 | 100 (RBstart=0) | 2622.5 | 5 | [22.3] | >ACLR2 |
| n41 | 1 | 2546 | 100 | 30 | 270 (RBstart=0) | 2167.5 | 5 | 9.1 | >ACLR2 |
| n41 | 2 | 2546 | 100 | 30 | 270 (RBstart=0) | 1987.5 | 5 | 0.6 | >ACLR2 |
| n41 | 3 | 2546 | 100 | 30 | 270 (RBstart=0) | 1877.5 | 5 | 0.6 | >ACLR2 |
| n41 | 4 | 2546 | 100 | 30 | 270 (RBstart=0) | 2152.5 | 5 | 3.5 | >ACLR2 |
| n41 | 25 | 2546 | 100 | 30 | 270 (RBstart=0) | 1992.5 | 5 | 0.6 | >ACLR2 |
| n41 | 39 | 2546 | 100 | 30 | 270 (RBstart=3) | 1917.5 | 5 | 1.6 | >ACLR2 |
| n41 | 40 | 2546 | 100 | 30 | 270 (RBstart=0) | 2397.5 | 5 | 31.4 | ACLR2 |
| n41 | 661 | 2546 | 100 | 30 | 270 (RBstart=0) | 2177.5 | 5 | 3.5 | >ACLR2 |
| 41 | n1 | 2506 | 20 | 15 | 100 (RBstart=0) | 2167.5 | 5 | 9.1 | >ACLR2 |
| 41 | n3 | 2506 | 20 | 15 | 100 (RBstart=0) | 1877.5 | 5 | 0.6 | >ACLR2 |
| 41 | n77 | 2680 | 20 | 15 | 100 (RBstart=0) | 3305 | 10 | 8.3 | >ACLR2 |
| 41 | n78 | 2680 | 20 | 15 | 100 (RBstart=0) | 3305 | 10 | 8.3 | >ACLR2 |
| n46 | 48 | 5190 | 80 | 30 | 216 (RBstart=0) | 3697.5 | 5 | 13.3 | >ACLR2 |
| 48 | n46 | 3690 | 20 | 15 | 100 (RBstart=0) | 5160 | 20 | 7 | >ACLR2 |
| n50 | 3 | 1487 | 60 | 30 | 162 (RBstart=0) | 1807.5 | 5 | 2.5 | >ACLR2 |
| 68 | n20 | 720.5 | 15 | 15 | 25 (RBstart=50) | 793.5 | 5 | 5.7 | >ACLR2 |
| n71 | 12 | 688 | 20 | 15 | 20 (RBstart=86) | 731.5 | 5 | 8.2 | >ACLR2 |
| n71 | 28 | 688 | 20 | 15 | 20 (RBstart=86) | 760.5 | 5 | 6.5 | >ACLR2 |
| 71 | n12 | 688 | 20 | 15 | 20 (RBstart=80) | 731.5 | 5 | 8.2 | ACLR2 |
| n77 | 71 | 3350 | 100 | 30 | 270 (RBstart=0) | 2687.5 | 5 | 4.5 | >ACLR2 |
| n77 | 411 | 3350 | 100 | 30 | 270 (RBstart=0) | 2687.5 | 5 | 4.5 | >ACLR2 |
| n78 | 71 | 3350 | 100 | 30 | 270 (RBstart=0) | 2687.5 | 5 | 4.5 | >ACLR2 |
| n78 | 38 | 3350 | 100 | 30 | 270 (RBstart=0) | 2617.5 | 5 | 3.3 | >ACLR2 |
| n78 | 401 | 3350 | 100 | 30 | 270 (RBstart=0) | 2397.5 | 5 | 4.5 | >ACLR2 |
| n78 | 411 | 3350 | 100 | 30 | 270 (RBstart=0) | 2687.5 | 5 | 4.5 | >ACLR2 |
| n78 | 46 | 3750 | 100 | 30 | 270 (RBstart=3) | 5160 | 20 | 13.5 | >ACLR2 |
| n79 | 426 | 4550 | 100 | 30 | 270 (RBstart=0) | 3597.5 | 5 | 2.6 | >ACLR2 |
| n84 | 3 | 1945 | 50 | 15 | 128 (RBstart=0) | 1877.5 | 5 | 19.7 | ACLR1 |
| n105 | 28 | 693 | 20 | 15 | 20 (RBstart=86) | 760.5 | 5 | 6.9 | >ACLR2 |
| NOTE 1: Applicable only when harmonic mixing MSD for this combination is not applied.NOTE 2: The B41 requirements are modified by -0.5dB when carrier frequency of the assigned E-UTRA channel bandwidth is within 2515 – 2690 MHz.NOTE 3: Void.NOTE 4: The NR DL band should be configured using the lowest SCS that is compatible with the specified DL CBW.NOTE 5: Void.NOTE 6: The requirements only apply for UEs supporting inter-band DC_42_n79 ENDC with simultaneous Rx/Tx capability. Simultaneous Rx/Tx capability does not apply for UEs supporting band 42 with a n77 implementation only. These restrictions are applicable to related higher order configurations.NOTE 7:  The MSD exceptions are applicable to the case that interference of UL band 3rd order IMD product falls into the affected DL channels. |  |  |  |  |  |  |  |  |  |

Table 7.3B.2.3.4-1a: Reference sensitivity exceptions (MSD) due to cross band isolation and uplink/downlink configurations for PC2 EN-DC in NR FR1

| UL band | DL band | UL Fc | UL BW | SCS of UL band | UL RB Allocation | DL Fc | DL BW | MSD | Cross-bandInterferencesource |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | (MHz) | (MHz) | (kHz) | LCRB | (MHz) | (MHz) | (dB) |  |
| 3 | n41 | 1775 | 20 | 15 | 50 (RBstart=50) | 2501 | 10 | 0.7 | >ACLR2 |
| n41 | 1 | 2546 | 100 | 30 | 270 (RBstart=0) | 2167.5 | 5 | 12.4 | >ACLR2 |
| n41 | 2 | 2546 | 100 | 30 | 270 (RBstart=0) | 1987.5 | 5 | 1.6 | >ACLR2 |
| n41 | 3 | 2546 | 100 | 30 | 270 (RBstart=0) | 1877.5 | 5 | 2.3 | >ACLR2 |
| n41 | 4 | 2546 | 100 | 30 | 270 (RBstart=0) | 2152.5 | 5 | 12.4 | >ACLR2 |
| n41 | 25 | 2546 | 100 | 30 | 270 (RBstart=0) | 1992.5 | 5 | 1.6 | >ACLR2 |
| n41 | 40 | 2546 | 100 | 30 | 270 (RBstart=0) | 2397.5 | 5 | 34.4 | ACLR2 |
| n41 | 66 | 2546 | 100 | 30 | 270 (RBstart=0) | 2177.5 | 5 | 12.4 | >ACLR2 |
| n77 | 2 | 3350 | 100 | 30 | 270 (RBstart=0) | 1987.5 | 5 | 1.0 | >ACLR2 |
| n77 | 30 | 3350 | 100 | 30 | 270 (RBstart=0) | 2357.5 | 5 | 1.0 | >ACLR2 |
| n77 | 401 | 3350 | 100 | 30 | 270 (RBstart=0) | 2395 | 10 | 6.5 | >ACLR2 |
| n77 | 411 | 3350 | 100 | 30 | 270 (RBstart=0) | 2687.5 | 5 | 6.5 | >ACLR2 |
| n77 | 66 | 3350 | 100 | 30 | 270 (RBstart=0) | 2177.5 | 5 | 1.0 | >ACLR2 |
| n78 | 7 | 3350 | 100 | 30 | 270 (RBstart=0) | 2687.5 | 5 | 6.5 | >ACLR2 |
| n78 | 25 | 3350 | 100 | 30 | 270 (RBstart=0) | 1992.5 | 5 | 1.0 | >ACLR2 |
| n78 | 38 | 3350 | 100 | 30 | 270 (RBstart=0) | 2617.5 | 5 | 5.3 | >ACLR2 |
| n78 | 401 | 3350 | 100 | 30 | 270 (RBstart=0) | 2397.5 | 5 | 6.7 | >ACLR2 |
| n78 | 411 | 3350 | 100 | 30 | 270 (RBstart=0) | 2687.5 | 5 | 6.5 | >ACLR2 |
| NOTE 1: Applicable only when harmonic mixing MSD for this combination is not applied. |  |  |  |  |  |  |  |  |  |

Table 7.3B.2.3.4-2: Void

##### 7.3B.2.3.5 MSD for intermodulation interference due to dual uplink operation for EN-DC in NR FR1

7.3B.2.3.5.0 General

For EN-DC configurations in NR FR1 the UE may indicate capability of not supporting simultaneous dual uplink operation due to possible intermodulation interference overlapping in frequency to its own primary downlink channel bandwidth if

- the intermodulation order is 2;

- the intermodulation order is 3 when both operating bands are between 450 MHz – 960 MHz or between 1427 MHz – 2690 MHz

In the case for EN-DC configurations in NR FR1 for which the intermodulation products caused by dual uplink operation do not interfere with its own primary downlink channel bandwidth as defined in Annex I the UE is mandated to operate in dual and triple uplink mode.

For EN-DC configurations in NR FR1 with uplink and downlink assigned to E-UTRA and NR FR1 bands given in Table 7.3B.2.3.5.1-1, Table 7.3B.2.3.5.1-1a, Table 7.3B.2.3.5.2-0 and Table 7.3B.2.3.5.2-1 the reference sensitivity is defined only for the specific uplink and downlink test points specified in Table 7.3B.2.3.5.1-1, Table 7.3B.2.3.5.1-1a, Table 7.3B.2.3.5.2-0 and Table 7.3B.2.3.5.2-1. For these test points the reference sensitivity levels specified in clause 7.3.1 in TS 36.101 [4] and 7.3.2 of TS 38.101-1 [2] for the corresponding channel bandwidths or in clause 7.3.1 of TS 36.101 [4] are relaxed by the amount of the parameter MSD given in Table 7.3B.2.3.5.1-1, Table 7.3B.2.3.5.1-1a, Table 7.3B.2.3.5.2-0 and Table 7.3B.2.3.5.2-1.

The throughput on each of the CGs shall be ≥ 95% of the maximum throughput of the respective reference measurement channels as specified in Annex A of TS 38.101-1 [2] and Annex A of TS 36.101 [4], with parameters specified in Table 7.3B.2.3.5.1-1, Table 7.3B.2.3.5.1-1a, Table 7.3B.2.3.5.2-0 and Table 7.3B.2.3.5.2-1 with dual UL transmissions overlapping in time unless otherwise stated.

###### 7.3B.2.3.5.1 MSD test points for intermodulation interference due to dual uplink operation for PC3 EN-DC in NR FR1 involving two bands

Table 7.3B.2.3.5.1-1: MSD test points for PCell due to dual uplink operation for PC3 EN-DC in NR FR1 (two bands)

| NR or E-UTRA Band / Channel bandwidth / NRB / MSD |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EN-DCConfiguration | EUTRA or NR band | UL Fc  (MHz) | UL/DL BW  (MHz) | UL  LCRB | DL Fc (MHz) | MSD  (dB) | IMD order |
| DC_1_n3 | 1 | 1950 | 5 | 25 | 2140 | 23 | IMD3 |
|  | n3 | 1760 | 5 | 25 | 1855 | N/A | N/A |
| DC_1C_n3 | 1C | 19501970 | 2020 | 1 (RBstart=0)1 (RBstart=67) | 21402160 | N/A | N/A |
|  | n3 | N/A | 5 | N/A | 1877.5 | 36 | IMD5 |
| DC_1A_n8A | 1 | 1965 | 5 | 25 | 2155 | 6.0 | IMD4 |
|  | n8 | 887.5 | 5 | 25 | 932.5 | N/A | N/A |
| DC_1A_n71ADC_1A_n71B | 1 | 1958 | 5 | 25 | 2148 | N/A | N/A |
|  | n71 | 668 | 5 | 25 | 622 | 15.1 | IMD3 |
| DC_1A_n77ADC_1A_SUL_n77A-n84ADC_1A_n77(2A)DC_1A_n77(3A) | 1 | 1950 | 5 | 25 | 2140 | 29.8 | IMD212 |
|  | n77 | 4090 | 10 | 50 | 4090 | N/A | N/A |
| DC_1A_n78ADC_1A_SUL_n78A-n84ADC_1A_n78(2A)DC_1A_n78(A-C) | 1 | 1950 | 5 | 25 | 2140 | 8.0 | IMD43 |
|  | n78 | 3710 | 10 | 50 | 3710 | N/A | N/A |
| DC_2A_n46A | 2 | 1880 | 5 | 25 | 1960 | 12.0 | IMD3 |
|  | n46 | 5720 | 20 | 100 | 5720 | N/A | N/A |
| DC_2A_n48A | 2 | 1852.5 | 5 | 25 | 1932.5 | 12 | IMD4 |
|  | n48 | 3625 | 20 | 100 | 3625 | N/A | N/A |
| DC_2A_n66ADC_2A-2A_n66ADC_2A_n66(2A) | 2 | 1855 | 5 | 25 | 1935 | 20 | IMD3 |
|  | n66 | 1775 | 5 | 25 | 2175 | N/A | N/A |
|  | 2 | 1883.3 | 5 | 25 | 1963.3 | N/A | N/A |
|  | n66 | 1750 | 5 | 25 | 2150 | 4 | IMD5 |
| DC_2A_n77ADC_2A_n77(2A)DC_2A-2A_n77ADC_2A_n77(2A)DC_2A-2A_n77(2A) | 2 | 1855 | 5 | 25 | 1935 | 26 | IMD212 |
|  | n77 | 3790 | 10 | 50 | 3790 | N/A | N/A |
|  | 2 | 1885 | 5 | 25 | 1965 | 5 | IMD5 |
|  | n77 | 3810 | 10 | 50 | 3810 | N/A | N/A |
| DC_2A_n78ADC_2A_n78(2A)DC_2A-2A_n78(2A) | 2 | 1855 | 5 | 25 | 1935 | 26 | IMD212 |
|  | n78 | 3790 | 10 | 50 | 3790 | N/A | N/A |
| DC_3_n1 | 3 | 1760 | 5 | 25 | 1855 | N/A | N/A |
|  | n1 | 1950 | 5 | 25 | 2140 | 23 | IMD3 |
| DC_3_n5 | 3 | 1771 | 10 | 50 | 1866 | 4 | IMD4 |
|  | n5 | 838 | 5 | 25 | 883 | N/A | N/A |
|  | 3 | 1721 | 10 | 50 | 1816 | N/A | N/A |
|  | n5 | 838 | 5 | 25 | 883 | 24 | IMD23 |
| DC_3A_n7ADC_3C_n7A | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |
|  | n7 | 2535 | 10 | 50 | 2655 | 10.2 | IMD4 |
| DC_3_n8 | n8 | 900 | 5 | 25 | 945 | 8 | IMD43 |
|  | 3 | 1755 | 10 | 50 | 1850 | N/A | N/A |
|  | n8 | 897.5 | 5 | 25 | 942.5 | N/A | N/A |
|  | 3 | 1747.5 | 10 | 50 | 1842.5 | 6.4 | IMD5 |
| DC_3A_n20ADC_3C_n20ADC_3A-3A_n20A | 3 | 1775 | 5 | 25 | 1870 | 4 | IMD4 |
|  | n20 | 840 | 5 | 25 | 799 | N/A | N/A |
|  | 3 | 1735 | 5 | 25 | 1830 | N/A | N/A |
|  | n20 | 847 | 5 | 25 | 806 | 9 | IMD4 |
| DC_3A_n26A | 3 | 1771 | 10 | 50 | 1866 | 4 | IMD4 |
|  | n26 | 838 | 5 | 25 | 883 | N/A | N/A |
|  | 3 | 1721 | 10 | 50 | 1816 | N/A | N/A |
|  | n26 | 838 | 5 | 25 | 883 | 24 | IMD23 |
| DC_3C_n26A | 3 | 1720 | 20 | 1 (RBSTART=0) | 1815 | N/A | N/A |
|  |  | 1739.8 | 20 | 1 (RBSTART=99) | 1834.8 | N/A |  |
|  | n26 | 841.5 | 15 | 25(RBSTART=54) | 886.5 | 18.9 | IMD3 |
| DC_3C_n28A | n28 | 715.5 | 25 | 25(RBSTART=108) | 770.5 | 11 | IMD39 |
|  | 3 | 1720 | 20 | 1 (RBSTART=0) | 1815 | N/A | N/A |
|  |  | 1739.8 | 20 | 1 (RBSTART=99) | 1834.8 |  |  |
| DC_3A_n38A | 3 | 1712.8 | 5 | 25 | 1807.8 | 8.2 | IMD4 |
|  | n38 | 2616.7 | 10 | 50 | 2616.7 | N/A | N/A |
| DC_3A_n41ADC_3C_n41ADC_3A_SUL_n41A-n80ADC_3C_SUL_n41A-n80ADC_3A-3A_n41A | 3 | 1740 | 5 | 25 | 1835 | 8.2 | IMD4 |
|  | n41 | 2657.5 | 10 | 50 | 2657.5 | N/A | N/A |
| DC_3A_n77ADC_3A_n77(2A)DC_3A_n77(3A)DC_3A_SUL_n77A-n80ADC_3A_n78ADC_3A_SUL_n78A-n80ADC_3A_n78(2A)DC_3A_n78(A-C)DC_3C_n78ADC_3C_n78(2A) | 3 | 1740 | 5 | 25 | 1835 | 26 | IMD212 |
|  | n77, n78 | 3575 | 10 | 50 | 3575 | N/A | N/A |
| DC_4A_n2A | n2 | 1860 | 20 | 502 | 1940 | 5 | IMD3 |
|  | 4 | 1752.5 | 5 | 25 | 2152.5 | N/A | N/A |
|  | n2 | 1868.3 | 5 | 25 | 1948.3 | N/A | N/A |
|  | 4 | 1735 | 5 | 25 | 2135 | 5 | IMD5 |
| DC_4A_n5A | n5 | 838 | 5 | 25 | 883 | 30 | IMD23 |
|  | 4 | 1721 | 5 | 25 | 2121 | N/A | N/A |
| DC_4A_n7A | 4 | 1730 | 5 | 25 | 2130 | N/A | N/A |
|  | n7 | 2535 | 10 | 50 | 2655 | 15 | IMD4 |
| DC_5A_n3A | 5 | 838 | 5 | 25 | 883 | N/A | N/A |
|  | n3 | 1771 | 10 | 50 | 1866 | 4 | IMD4 |
|  | 5 | 838 | 5 | 25 | 883 | 24 | IMD23 |
|  | n3 | 1721 | 10 | 50 | 1816 | N/A | N/A |
| DC_5_n7 | n7 | 2547 | 10 | 50 | 2667 | N/A | N/A |
|  | 5 | 834 | 5 | 25 | 879 | 12 | IMD33 |
| DC_5_n38 | 5 | 844 | 5 | 25 | 889 | 12 | IMD33 |
|  | n38 | 2577 | 10 | 50 | 2577 | N/A | N/A |
| DC_5A_n41A | 5 | 839 | 5 | 25 | 884 | 15.6 | IMD33 |
|  | n41 | 2562 | 10 | 50 | 2562 | N/A | N/A |
| DC_5A_n66A | 5 | 838 | 5 | 25 | 883 | 30 | IMD23 |
|  | n66 | 1721 | 5 | 25 | 2121 | N/A | N/A |
| DC_5A_n77A8DC_5A_n77(2A)8DC_5A_n77(3A)8 | 5 | 844 | 5 | 25 | 889 | 8.3 | IMD4 |
|  | n77 | 3421 | 10 | 50 | 3421 | N/A | N/A |
|  | 5 | 826.5 | 5 | 25 | 871.5 | 5.5 | IMD5 |
|  | n77 | 4177.5 | 10 | 50 | 4177.5 | N/A | N/A |
| DC_5A_n78ADC_5A_n78(2A)DC_5A_n78(A-C)DC_5A_n78CDC_5A_SUL_n78A-n89A | 5 | 844 | 5 | 25 | 889 | 8.3 | IMD4 |
|  | n78 | 3421 | 10 | 50 | 3421 | N/A | N/A |
| DC_7_n3DC_7-7_n3 | 7 | 2535 | 10 | 50 | 2655 | 13 | IMD4 |
|  | n3 | 1730 | 5 | 25 | 1825 | N/A | N/A |
| DC_7_n5 | 7 | 2547 | 10 | 50 | 2667 | N/A | N/A |
|  | n5 | 834 | 5 | 25 | 879 | 12 | IMD33 |
| DC_7A_n20A | 7 | 2512 | 10 | 50 | 2632 | N/A | N/A |
|  | n20 | 851 | 5 | 25 | 810 | 12 | IMD33 |
| DC_7A_n26ADC_7C_n26A | 7 | 2547 | 10 | 50 | 2667 | N/A | N/A |
|  | n26 | 834 | 5 | 25 | 879 | 12 | IMD33 |
|  | 7 | 2567.5 | 5 | 25 | 2687.5 | 2.5 | IMD5 |
|  | n26 | 816.5 | 5 | 25 | 861.5 | N/A | N/A |
| DC_7A_n40ADC_7A-7A_n40A | 7 | 2510 | 5 | 25 | 2630 | 23 | IMD3 |
|  | n40 | 2390 | 10 | 50 | 2390 | N/A | N/A |
| DC_7A_n66ADC_7A-7A_n66ADC_7C_n66A | 7 | 2535 | 10 | 50 | 2655 | 15 | IMD4 |
|  | n66 | 1730 | 5 | 25 | 2130 | N/A | N/A |
| DC_7A_n77ADC_7A-7A_n77(2A)DC_7A-7A_n77(3A)DC_7A_n77(2A)DC_7A_n77(3A)DC_7C_n77ADC_7C_n77(2A) | 7 | 2540 | 5 | 25 | 2660 | 7.1 | IMD4 |
|  | n77 | 3870 | 10 | 50 | 3870 | N/A | N/A |
| DC_7_n79DC_7-7_n79 | 7 | 2510 | 5 | 25 | 2630 | [8] | IMD4 |
|  | n79 | 4900 | 40 | 216 | 4900 | N/A | N/A |
| DC_8A_n1ADC_8B_n1A | 8 | 887.5 | 5 | 25 | 932.5 | N/A | N/A |
|  | n1 | 1965 | 5 | 25 | 2155 | 6 | IMD4 |
| DC_8A_n3ADC_8B_n3A | 8 | 900 | 5 | 25 | 945 | 8 | IMD43 |
|  | n3 | 1755 | 10 | 50 | 1850 | N/A | N/A |
|  | 8 | 897.5 | 5 | 25 | 942.5 | N/A | N/A |
|  | n3 | 1747.5 | 10 | 50 | 1842.5 | 6.4 | IMD5 |
| DC_8A_n20A | n20 | 849.5 | 5 | 25 | 808.5 | 25 | IMD33 |
|  | 8 | 890.5 | 5 | 25 | 935.5 | N/A | N/A |
|  | n20 | 847.5 | 5 | 25 | 806.5 | N/A | N/A |
|  | 8 | 892.5 | 5 | 25 | 937.5 | 25 | IMD33 |
| DC_8A_n38A | 8 | 887.5 | 5 | 25 | 932.5 | 8.1 | IMD5 |
|  | n38 | 2617.5 | 5 | 25 | 2617.5 | N/A | N/A |
| DC_8A_n41ADC_8A_SUL_n41A-n81A | 8 | 882.5 | 5 | 25 | 927.5 | 12.1 | IMD33 |
|  | n41 | 2685 | 10 | 50 | 2685 | N/A | N/A |
| DC_8A_n77ADC_8B_n77ADC_8B_n77(2A)DC_8A_n78ADC_8B_n78ADC_8A_n78(2A)DC_8A_n77(3A)DC_8A_SUL_n78A-n81A | 8 | 897.5 | 5 | 25 | 942.5 | 8.3 | IMD4 |
|  | n77, n78 | 3635 | 10 | 50 | 3635 | N/A | N/A |
| DC_8A_n79A,DC_8A_n79C,DC_8A_SUL_n79A-n81A | 8 | 897.5 | 5 | 25 | 942.5 | 4.8 | IMD5 |
|  | n79 | 4532.5 | 40 | 216 | 4532.5 | N/A | N/A |
| DC_11A_n28A | 11 | 1430.5 | 5 | 25 | 1478.5 | N/A | N/A |
|  | n28 | 743 | 5 | 25 | 798 | 10.4 | IMD4 |
| DC_12A_n77ADC_12A_n77(2A) | 12 | 702 | 5 | 20 | 732 | 5.5 | IMD5 |
|  | n77 | 3540 | 10 | 50 | 3540 | N/A | N/A |
| DC_12A_n78A | 12 | 710 | 5 | 25 | 740 | 5.5 | IMD5 |
|  | n78 | 3580 | 10 | 50 | 3580 | N/A | N/A |
| DC_13A_n5A | 13 | 783 | 5 | 25 | 752 | N/A | N/A |
|  | n5 | 828 | 5 | 25 | 873 | 25 | IMD3 |
| DC_13A_n7ADC_13A_n7(2A) | 13 | 784.5 | 5 | 25 | 753.5 | N/A | N/A |
|  | n7 | 2520 | 40 | 216 | 2640 | 2.5 | IMD5 |
| DC_13A_n77A | 13 | 784.5 | 5 | 20 | 753.5 | 5.5 | IMD5 |
|  | n77 | 3891.5 | 10 | 50 | 3891.5 | N/A | N/A |
| DC_14A_n5A | 14 | 791 | 5 | 25 | 761 | N/A | N/A |
|  | n5 | 836 | 5 | 25 | 881 | 25 | IMD3 |
|  | 14 | 795.5 | 5 | 25 | 765.5 | 25 | IMD3 |
|  | n5 | 826.5 | 5 | 25 | 871.5 | N/A | N/A |
| DC_14A_n77ADC 14A_n77(2A) | 14 | 795.5 | 5 | 15 | 765.5 | 5.5 | IMD5 |
|  | n77 | 3947.5 | 10 | 50 | 3947.5 | N/A | N/A |
| DC_18A_n3A | 18 | 823 | 5 | 25 | 868 | N/A | N/A |
|  | n3 | 1721 | 5 | 25 | 1816 | 4 | IMD4 |
| DC_18A_n77A10 | 18 | 827.5 | 5 | 25 | 872.5 | 8.4 | IMD410 |
|  | n77 | 3355 | 10 | 50 | 3355 | N/A | N/A |
|  | 18 | 817.5 | 5 | 25 | 862.5 | 4.5 | IMD510 |
|  | n77 | 4130 | 10 | 50 | 4130 | N/A | N/A |
| DC_18A_n78A | 18 | 827.5 | 5 | 25 | 872.5 | 8.4 | IMD411 |
|  | n78 | 3355 | 10 | 50 | 3355 | N/A | N/A |
| DC_19A_n77A | 19 | 836.5 | 5 | 25 | 881.5 | 13.6 | IMD43 |
|  | n77 | 3391 | 10 | 50 | 3391 | N/A | N/A |
| DC_19A_n78A | 19 | 836.5 | 5 | 25 | 881.5 | 13.6 | IMD4 |
|  | n78 | 3391 | 10 | 50 | 3391 | N/A | N/A |
| DC_20A_n3A | 20 | 840 | 5 | 25 | 799 | N/A | N/A |
|  | n3 | 1775 | 5 | 25 | 1870 | 4 | IMD4 |
|  | 20 | 847 | 5 | 25 | 806 | 9 | IMD4 |
|  | n3 | 1735 | 5 | 25 | 1830 | N/A | N/A |
| DC_20_n7 | 20 | 851 | 5 | 25 | 810 | 12 | IMD33 |
|  | n7 | 2512 | 10 | 50 | 2632 | N/A | N/A |
| DC_20A_n8A | 20 | 849.5 | 5 | 25 | 808.5 | 25 | IMD33 |
|  | n8 | 890.5 | 5 | 25 | 935.5 | N/A | N/A |
|  | 20 | 847.5 | 5 | 25 | 806.5 | N/A | N/A |
|  | n8 | 892.5 | 5 | 25 | 937.5 | 25 | IMD33 |
| DC_20A_n38A | 20 | N/A | N/A | N/A | N/A | N/A | IMD5 |
|  | n38 | N/A | N/A | N/A | N/A | N/A | N/A |
| DC_20_n41 | 20 | 851 | 5 | 25 | 810 | 12.1 | IMD33 |
|  | n41 | 2512 | 10 | 50 | 2512 | N/A | N/A |
| DC_20A_n77A | 20 | 850 | 5 | 25 | 809 | 11 | IMD4 |
|  | n77 | 3359 | 10 | 50 | 3359 | N/A | N/A |
|  | 20 | 840 | 5 | 25 | 799 | 6.5 | IMD5 |
|  | n77 | 4159 | 10 | 50 | 4159 | N/A | N/A |
| DC_20A_n78ADC_20A_n78C7DC_20A_n78(2A)DC_20A_SUL_n78A-n82A | 20 | 850 | 5 | 25 | 809 | 11 | IMD4 |
|  | n78 | 3359 | 10 | 50 | 3359 | N/A | N/A |
| DC_21A_n28A7 | 21 | 1450.4 | 5 | 25 | 1498.4 | 2.5 | IMD5 |
|  | n28 | 735.5 | 5 | 25 | 790.5 | N/A | N/A |
| DC_21A_n79A | 21 | 1457.5 | 5 | 25 | 1505.5 | 18.4 | IMD3 |
|  | n79 | 4420.5 | 40 | 216 | 4420.5 | N/A | N/A |
| DC_25A_n77ADC_25A-25A_n77A | 25 | 1855 | 5 | 25 | 1935 | 26 | IMD212 |
|  | n77 | 3790 | 10 | 50 | 3790 | N/A | N/A |
|  | 25 | 1885 | 5 | 25 | 1965 | 5 | IMD5 |
|  | n77 | 3810 | 10 | 50 | 3810 | N/A | N/A |
| DC_25A_n78A | 25 | 1855 | 5 | 25 | 1935 | 26 | IMD212 |
| DC_25A-25A_n78A | n78 | 3790 | 10 | 50 | 3790 | N/A | N/A |
|  | 25 | 1875 | 5 | 25 | 1955 | 5 | IMD5 |
|  | n78 | 3790 | 10 | 50 | 3790 | N/A | N/A |
| DC_26A_n41A | 26 | 839 | 5 | 25 | 884 | 15.6 | IMD33 |
|  | n41 | 2562 | 10 | 50 | 2562 | N/A | N/A |
| DC_26A_n77ADC_26A_n78ADC_26A_n78(2A) | 26 | 836.5 | 5 | 25 | 881.5 | 11.1 | IMD4 |
|  | n77, n78 | 3391 | 10 | 50 | 3391 | N/A | N/A |
| DC_28_n50 | 28 | 730 | 10 | 50 | 775 | 15.3 | IMD212 |
|  | n50 | 1500 | 10 | 50 | 1500 | N/A | N/A |
|  | 28 | 740 | 10 | 50 | 785 | 0.5 | IMD5 |
|  | n50 | 1500 | 10 | 50 | 1500 | N/A | N/A |
| DC_28A_n51A | 28 | 742.3 | 5 | 25 | 797.3 | 5 | IMD4 |
|  | n51 | 1429.5 | 5 | 25 | 1429.5 | N/A | N/A |
| DC_28A_n77ADC_28C_n77ADC_28C_n77(2A)DC_28A_n78ADC_28A_n78(2A)DC_28A_SUL_n78A-n83A | 28 | 705.5 | 5 | 25 | 760.5 | 5.5 | IMD5 |
|  | n77, n78 | 3582.5 | 10 | 50 | 3582.5 | N/A | N/A |
| DC_30A_n77ADC_30A_n77(2A) | 30 | 2310 | 5 | 25 | 2355 | 8.0 | IMD4 |
|  | n77 | 3487.5 | 10 | 50 | 3487.5 | N/A | N/A |
| DC_38A_n3A | n3 | 1713 | 5 | 25 | 1808 | 8.2 | IMD4 |
|  | 38 | 2617 | 5 | 25 | 2617 | N/A | N/A |
| DC_38A_n8A | 38 | 2617.5 | 5 | 25 | 2617.5 | N/A | N/A |
|  | n8 | 887.5 | 5 | 25 | 932.5 | 8.1 | IMD5 |
| DC_40A_n7A | n7 | 2510 | 5 | 25 | 2630 | 23 | IMD3 |
|  | 40 | 2390 | 5 | 25 | 2390 | N/A | N/A |
| DC_41A_n3ADC_41C_n3A | n3 | 1740 | 5 | 25 | 1835 | 8.2 | IMD4 |
|  | 41 | 2657.5 | 5 | 25 | 2657.5 | N/A | N/A |
| DC_42_n3 | 42 | 3575 | 10 | 50 | 3575 | N/A | N/A |
|  | n3 | 1740 | 5 | 25 | 1835 | 26 | IMD212 |
| DC_42_n28 | 42 | 3582.5 | 10 | 50 | 3582.5 | N/A | N/A |
|  | n28 | 705.5 | 5 | 25 | 760.5 | 5.5 | IMD5 |
| DC_48A_n2ADC_48C_n2ADC_48D_n2ADC_48E_n2A | 48 | 3625 | 20 | 100 | 3625 | N/A | N/A |
|  | n2 | 1852.5 | 5 | 25 | 1932.5 | 12 | IMD4 |
| DC_48A_n12A | 48 | 3557.5 | 10 | 50 | 3557.5 | N/A | N/A |
|  | n12 | 705.5 | 5 | 25 | 735.5 | 5.5 | IMD5 |
| DC_48A_n25ADC_48C_n25ADC_48D_n25A | 48 | 3625 | 20 | 100 | 3625 | N/A | N/A |
|  | n25 | 1852.5 | 5 | 25 | 1932.5 | 12 | IMD4 |
| DC_48A_n66ADC_48C_n66ADC_48D_n66A | 48 | 3630 | 20 | 100 | 3630 | N/A | N/A |
|  | n66 | 1715 | 5 | 25 | 2115 | 4 | IMD5 |
| DC_66A_n2A,DC_66A_n2(2A)DC_66A-66A_n2A | 66 | 1775 | 5 | 25 | 2175 | N/A | N/A |
|  | n2 | 1855 | 5 | 25 | 1935 | 20 | IMD3 |
|  | 66 | 1750 | 5 | 25 | 2150 | 4 | IMD5 |
|  | n2 | 1883.3 | 5 | 25 | 1963.3 | N/A | N/A |
| DC_66A_n5A | n5 | 838 | 5 | 25 | 883 | 30 | IMD23 |
|  | 66 | 1721 | 5 | 25 | 2121 | N/A | N/A |
| DC_66A_n7ADC_66A-66A_n7ADC_66A_n7(2A)DC_66A-66A_n7(2A) | 66 | 1730 | 5 | 25 | 2130 | N/A | N/A |
|  | n7 | 2535 | 10 | 50 | 2655 | 15 | IMD4 |
| DC_66A_n25A | 66 | 1775 | 5 | 25 | 2175 | N/A | N/A |
|  | n25 | 1855 | 5 | 25 | 1935 | 20 | IMD3 |
|  | 66 | 1712.5 | 5 | 25 | 2112.5 | 23 | IMD3 |
|  | n25 | 1912.5 | 5 | 25 | 1992.5 | N/A | N/A |
| DC_66A_n46A | 66 | 1735 | 5 | 25 | 2135 | 12.0 | IMD3 |
|  | n46 | 5605 | 20 | 100 | 5605 | N/A | N/A |
| DC_66A_n48A | 66 | 1715 | 5 | 25 | 2115 | 4 | IMD5 |
|  | n48 | 3630 | 20 | 100 | 3630 | N/A | N/A |
| DC_66A_n71A | 66 | 1750 | 5 | 25 | 2150 | 5 | IMD4 |
|  | n71 | 675 | 5 | 25 | 629 | N/A | N/A |
| DC_66A_n77ADC_66A_n77(2A)DC_66A-66A_n77ADC_66A-66A_n77(2A)DC_66A-66A-66A_n77ADC_66A-66A-66A_n77(2A) | 66 | 1775 | 5 | 25 | 2175 | 31.0 | IMD2 |
|  | n77 | 3950 | 10 | 50 | 3950 | N/A | N/A |
|  | 66 | 1760 | 5 | 25 | 2160 | 5.0 | IMD5 |
|  | n77 | 3720 | 10 | 50 | 3720 | N/A | N/A |
| DC_66A_n78A | 66 | 1730 | 5 | 25 | 2150 | 5.0 | IMD5 |
|  | n78 | 3660 | 10 | 50 | 3660 | N/A | N/A |
| DC_68A_n77A | 68 | 705.5 | 5 | 25 | 760.5 | 5.5 | IMD5 |
|  | n77 | 3582.5 | 10 | 50 | 3582.5 | N/A | N/A |
| DC_68A_n78A | 68 | 705.5 | 5 | 25 | 760.5 | 5.5 | IMD5 |
|  | n78 | 3582.5 | 10 | 50 | 3582.5 | N/A | N/A |
| DC_71A_n38A | 71 | 665 | 5 | 25 | 619 | 11 | IMD4 |
|  | n38 | 2614 | 10 | 50 | 2614 | N/A | N/A |
| DC_71A_n41A | 71 | 666 | 5 | 25 | 620 | 9.5 | IMD4 |
|  | n41 | 2618 | 10 | 50 | 2618 | N/A | N/A |
| DC_71A_n66A | 71 | 675 | 5 | 25 | 629 | N/A | N/A |
|  | n66 | 1750 | 5 | 25 | 2150 | 5 | IMD4 |
| DC_71A_n77A8DC_71A_n77(2A)8 | 71 | 671 | 5 | 25 | 625 | 5.5 | IMD5 |
|  | n77 | 3309 | 10 | 50 | 3309 | N/A | N/A |
| DC_71A_n78A | 71 | 681.5 | 5 | 25 | 635.5 | 5.5 | IMD5 |
| DC_71A_n78(2A) | n78 | 3361.5 | 10 | 50 | 3361.5 | N/A | N/A |
| DC_106A_n41ADC_106A_n41C DC_106A_n41(2A) | 106 | 898.5 | 3 | 25 | 937.5 | [10] | IMD5 |
|  | n41 | 2656.5 | 10 | 50 | N/A | N/A | N/A |
| DC_106A_n48ADC_106A_n48C DC_106A_n48(2A) | 106 | 898.5 | 3 | 25 | 937.5 | [10] | IMD4 |
|  | n48 | 3633 | 10 | 50 | N/A | N/A | N/A |
| NOTE 1: E-UTRA carrier shall be set to min(+20 dBm, PCMAX_L_E-UTRA,c) and NR carrier shall be set to min(+20 dBm, PCMAX_L,f,c,NR) as defined in clause 6.2B.4.1.3.NOTE 2: RBstart = 0NOTE 3: This band is subject to IMD5 also which MSD is not specified.NOTE 4: VoidNOTE 5: VoidNOTE 6:  VoidNOTE 7: The frequency range in band n28 is restricted for this band combination to 728 – 738 MHz for the UL and 783 – 793 MHz for the DL. This band is subject to IMD2, IMD4 and IMD5 fall in n28 also which MSD is not specified. In addition, this band is subject to IMD4 fall in B21 also which MSD is not specified.NOTE 8: For a UE which supports this band combination only when the Band n77 frequency range restriction defined in NOTE 12 of Table 5.2-1 from TS 38.101-1 applies, the MSD test point(s) cannot be verified for the band combination and the test point(s) can be skipped.NOTE 9:  This test configuration ensures the B3 self-interference would not interrupt the testing.NOTE 10: For a UE which supports this band combination only when the Band n77 frequency range restriction of 3400 - 4100 MHz in Japan applies, the MSD test point(s) cannot be verified for the band combination and the test point(s) can be skipped.NOTE 11: For a UE which supports this band combination only when the Band n78 frequency range restriction of 3400 - 3800 MHz in Japan applies, the MSD test point(s) cannot be verified for the band combination and the test point(s) can be skipped.NOTE 12: This band is subject to IMD4 also which MSD is not specified. |  |  |  |  |  |  |  |

Table 7.3B.2.3.5.1-1a: MSD test points for PCell due to dual uplink operation for PC2 EN-DC in NR FR1 (two bands)

| NR or E-UTRA Band / Channel bandwidth / NRB / MSD |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EN-DCConfiguration | EUTRA or NR band | UL Fc  (MHz) | UL/DL BW  (MHz) | UL  LCRB | DL Fc (MHz) | MSD  (dB) | IMD order |
| DC_1A_n77A | 1 | 1950 | 5 | 25 | 2140 | 35.8 | IMD26 |
| DC_1A_n77(2A)DC_1A_n77(3A) | n77 | 4090 | 10 | 50 | 4090 | N/A | N/A |
| DC_3A_n41A | 3 | 1740 | 5 | 25 | 1835 | 18.4 | IMD4 |
|  | n41 | 2657.5 | 10 | 50 | 2657.5 | N/A | N/A |
| DC_3A_n78A | 3 | 1740 | 5 | 25 | 1835 | 31.9 | IMD2 |
| DC_3A-3A_n78A | n78 | 3575 | 10 | 50 | 3575 | N/A | N/A |
| DC_3A_n78A | 3 | 1765 | 5 | 25 | 1860 | 18.5 | IMD4 |
| DC_3A-3A_n78ADC_3A_n78(2A)DC_3C_n78ADC_3C_n78(2A) | n78 | 3435 | 10 | 50 | 3435 | N/A | N/A |
| DC_1A_n78A | 1 | 1950 | 5 | 25 | 2140 | 17.8 | IMD4 |
|  | n78 | 3710 | 10 | 50 | 3710 | N/A | N/A |
| DC_2A_n77ADC_2A-2A_n77ADC_2A_n77CDC_2A-2A_n77CDC_2A_n77(2A)DC_2A-2A_n77(2A) | 2 | 1855 | 5 | 25 | 1935 | 32.10 | IMD26 |
|  | n77 | 3790 | 10 | 50 | 3790 | N/A | N/A |
| DC_2A_n78A | 2 | 1855 | 5 | 25 | 1935 | 32.10 | IMD26 |
| DC_2A_n78(2A) | n78 | 3790 | 10 | 50 | 3790 | N/A | N/A |
| DC_3A_n77A | 3 | 1740 | 5 | 25 | 1835 | 31.9 | IMD26 |
| DC_3A_n77(2A)DC_3A_n77(3A) | n77 | 3575 | 10 | 50 | 3575 | N/A | N/A |
| DC_5_n41A | 5 | 839 | 5 | 25 | 884 | 24.6 | IMD33 |
|  | n41 | 2562 | 10 | 50 | 2562 | N/A | N/A |
| DC_5A_n77A3DC_5A_n77C3DC_5A_n77(2A)3 | 5 | 844 | 5 | 25 | 889 | 18.60 | IMD41 |
|  | n77 | 3421 | 10 | 50 | 3421 | N/A | N/A |
| DC_5A_n78A | 5 | 844 | 5 | 25 | 889 | 17.5 | IMD4 |
|  | n78 | 3421 | 10 | 52 | 3421 | N/A | N/A |
| DC_8A_n78ADC_8B_n78ADC_8A_n78(2A) | 8 | 897.5 | 5 | 25 | 942.5 | 15.5 | IMD4 |
|  | n78 | 3635 | 10 | 50 | 3635 | N/A | N/A |
| DC_8A_n79A | 8 | 897.5 | 5 | 25 | 942.5 | 21.5 | IMD5 |
|  | n79 | 4532.5 | 40 | 216 | 4532.5 | N/A | N/A |
| DC_13A_n77ADC_13A_n77C | 13 | 782 | 5 | 20 | 751 | 15.37 | IMD5 |
|  | n77 | 3879 | 10 | 50 | 3879 | N/A | N/A |
| DC_66A_n77ADC_66A-66A_n77ADC_66A-66A-66A_n77ADC_66A_n77CDC_66A-66A_n77CDC_66A-66A-66A_n77CDC_66A_n77(2A)DC_66A-66A_n77(2A)DC_66A-66A-66A_n77(2A) | 66 | 1775 | 5 | 25 | 2175 | 34.33 | IMD2 |
|  | n77 | 3950 | 10 | 50 | 3950 | N/A | N/A |
|  | 66 | 1760 | 5 | 25 | 2160 | 11.27 | IMD5 |
|  | n77 | 3720 | 10 | 50 | 3720 | N/A | N/A |
| DC_8A_n41A | 8 | 882.5 | 5 | 25 | 927.5 | 18.2 | IMD31 |
|  | n41 | 2685 | 10 | 50 | 2685 | N/A | N/A |
| DC_8A_n77ADC_8A_n77(2A)DC_8A_n77(3A) | 8 | 897.5 | 5 | 25 | 942.5 | 15.5 | IMD4 |
|  | n77 | 3635 | 10 | 50 | 3635 | N/A | N/A |
| DC_12A_n77ADC_12A_n77(2A) | 12 | 702 | 5 | 20 | 732 | 11.7 | IMD5 |
|  | n77 | 3540 | 10 | 50 | 3540 | N/A | N/A |
| DC_12A_n78A | n12 | 702 | 5 | 20 | 732 | 11.7 | IMD5 |
|  | n78 | 3540 | 10 | 20 | 3540 | N/A |  |
| DC_14A_n77ADC_14A_n77(2A) | 14 | 795.5 | 5 | 15 | 765.5 | 11.7 | IMD5 |
|  | n77 | 3947.5 | 10 | 50 | 3947.5 | N/A | N/A |
| DC_18A_n77A | 18 | 827.5 | 5 | 25 | 872.5 | 17.5 | IMD45 |
|  | n77 | 3355 | 10 | 50 | 3355 | N/A | N/A |
|  | 18 | 817.5 | 5 | 25 | 862.5 | 10.5 | IMD55 |
|  | n77 | 4130 | 10 | 50 | 4130 | N/A | N/A |
| DC_18A_n78A | 18 | 827.5 | 5 | 25 | 872.5 | 18.4 | IMD411 |
|  | n78 | 3355 | 10 | 50 | 3355 | N/A | N/A |
| DC_19A_n77ADC_19A_n77(2A) | 19 | 836.5 | 5 | 25 | 881.5 | 25.3 | IMD4 |
|  | n77 | 3391 | 10 | 50 | 3391 | N/A | N/A |
|  | 19 | 832.5 | 5 | 25 | 877.5 | 8.1 | IMD5 |
|  | n77 | 4195 | 10 | 50 | 4195 | N/A | N/A |
| DC_19A_n78ADC_19A_n78(2A) | 19 | 836.5 | 5 | 25 | 881.5 | 25.3 | IMD4 |
|  | n78 | 3391 | 10 | 50 | 3391 | N/A | N/A |
| DC_20A_n41 | 20 | 851 | 5 | 25 | 810 | 19.1 | IMD31 |
|  | n41 | 2512 | 10 | 50 | 2512 | N/A | N/A |
| DC_20A_n78A | 20 | 850 | 5 | 25 | 809 | 18.8 | IMD4 |
|  | n78 | 3359 | 10 | 50 | 3359 | N/A | N/A |
| DC_25A_n78A | 25 | 1855 | 5 | 25 | 1935 | 32.1 | IMD26 |
|  | n78 | 3790 | 10 | 50 | 3790 | N/A | N/A |
|  | 25 | 1875 | 5 | 25 | 1955 | 20 | IMD5 |
|  | n78 | 3790 | 10 | 50 | 3790 | N/A | N/A |
| DC_26A_n41A | 26 | 839 | 5 | 25 | 884 | 24.6 | IMD33 |
|  | n41 | 2562 | 10 | 50 | 2562 | N/A | N/A |
| DC_26A_n78A | 26 | 836.5 | 5 | 25 | 881.5 | 23.8 | IMD4 |
|  | n78 | 3391 | 10 | 50 | 3391 | N/A | N/A |
| DC_28A_n77A | 28 | 705.5 | 5 | 25 | 760.5 | 19.2 | IMD5 |
|  | n77 | 3582.5 | 10 | 50 | 3582.5 | N/A | N/A |
| DC_30A_n77ADC_30A_n77(2A) | 30 | 2310 | 5 | 25 | 2355 | 17.6 | IMD4 |
|  | n77 | 3487.5 | 10 | 50 | 3487.5 | N/A | N/A |
| DC_28A_n78A | 28 | 705.5 | 5 | 25 | 760.5 | 11.7 | IMD5 |
|  | n78 | 3582.5 | 10 | 50 | 3582.5 | N/A | N/A |
| DC_21A_n79A | 21 | 1457.5 | 5 | 25 | 1505.5 | 33.4 | IMD3 |
|  | n79 | 4420.5 | 10 | 50 | 4420.5 | N/A | N/A |
| DC_66A_n78A | 66 | 1760 | 5 | 25 | 2160 | 11.27 | IMD5 |
|  | n77 | 3720 | 10 | 50 | 3720 | N/A | N/A |
| DC_71A_n41A | 71 | 666 | 5 | 25 | 620 | 21.5 | IMD4 |
|  | n41 | 2618 | 10 | 50 | 2618 | N/A | N/A |
| DC_71A_n77A3 | 71 | 681.5 | 5 | 25 | 635.5 | 11.4 | IMD5 |
|  | n77 | 3361.5 | 10 | 50 | 3361.5 | N/A | N/A |
| DC_71A_n78A | 71 | 681.5 | 5 | 25 | 635.5 | 11.4 | IMD5 |
| DC_71A_n78(2A) | n78 | 3361.5 | 10 | 50 | 3361.5 | N/A | N/A |
| NOTE 1: This band is subject to IMD5 also which MSD is not specified.NOTE 2: VoidNOTE 3: For a UE which supports this band combination only when the Band n77 frequency range restriction defined in NOTE 12 of Table 5.2-1 from TS 38.101-1 applies, the MSD test point(s) cannot be verified for the band combination and the test point(s) can be skipped.NOTE 4: E-UTRA carrier shall be set to min(+23 dBm, PCMAX_L_E-UTRA,c) and NR carrier shall be set to min(+23 dBm, PCMAX_L,f,c,NR) as defined in clause 6.2B.4.1.3.NOTE 5: For a UE which supports this band combination only when the Band n77 frequency range restriction of 3400 - 4100 MHz in Japan applies, the MSD test point(s) cannot be verified for the band combination and the test point(s) can be skipped.NOTE 6: This band is subject to IMD4 also which MSD is not specified. |  |  |  |  |  |  |  |

###### 7.3B.2.3.5.2 MSD test points for intermodulation interference due to dual uplink operation for EN-DC in NR FR1 involving three bands

Table 7.3B.2.3.5.2-0: MSD test points for Pcell due to dual uplink operation for EN-DC in NR FR1 (three bands)

| NR or E-UTRA Band / Channel bandwidth / NRB / MSD |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EN-DC Configuration | EUTRA/NR band | UL Fc  (MHz) | UL/DL BW  (MHz) | ULLCRB | DL Fc (MHz) | MSD  (dB) | IMD order |
| DC_66A-(n)71AA | 66 | 1750 | 5 | 25 | 2150 | 5 | IMD4 |
|  | n71 | 678 | 10 | 10 (RBstart =0) | 632 | N/A | N/A |
| NOTE 1:  VoidNOTE 2: E-UTRA carrier shall be set to min(+20 dBm, PCMAX_L_E-UTRA,c) and NR carrier shall be set to min(+20 dBm, PCMAX_L,f,c,NR) as defined in clause 6.2B.4.1.3. |  |  |  |  |  |  |  |

Table 7.3B.2.3.5.2-1: MSD test points for Scell due to dual uplink operation for EN-DC in NR FR1 (three bands)

| NR or E-UTRA Band / Channel bandwidth / NRB / MSD |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EN-DC Configuration | EUTRA / NR band | UL Fc  (MHz) | UL/DL BW  (MHz) | ULLCRB | DL Fc (MHz) | MSD  (dB) | IMD order |  |
| DC_1A_n1A-n78A | 1 | 1945 | 5 | 25 | 2135 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2125 | 12.0 | IMD4 |  |
|  | n78 | 3710 | 10 | 50 | 3710 | N/A | N/A |  |
| DC_1A-3A_n1A | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
| DC_1A-3A-3A_n1A | 3 | 1750 | 5 | 25 | 1845 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2150 | 23 | IMD3 |  |
| DC_1A-3A_n28ADC_1A-3C_n28A | 1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1818.5 | 4.0 | IMD5 |  |
|  | n28 | 710.5 | 5 | 25 | 765.5 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2139 | 11.0 | IMD4 |  |
|  | 3 | 1780 | 5 | 25 | 1875 | N/A | N/A |  |
|  | n28 | 710.5 | 5 | 25 | 765.5 | N/A | N/A |  |
| DC_1A-3A_n71ADC_1A-3A_n71B | 1 | N/A | 5 | N/A | 2150 | 5 | IMD4 |  |
| DC_1A-3C_n71A | 3 | 1750 | 5 | 25 | 1845 | N/A | N/A |  |
|  | n71 | 675 | 5 | 25 | 629 | N/A | N/A |  |
| DC_1A_n3A-n28A | 1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1818.5 | 4.0 | IMD5 |  |
|  | n28 | 710.5 | 5 | 25 | 765.5 | N/A | N/A |  |
| DC_1A_n3A-n41A | 1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | n3 | 1712.5 | 5 | 25 | 1807.5 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2507.5 | 4 | IMD5 |  |
| DC_1A_n3A-n75A | n75 | N/A | 5 | N/A | 1480 | 15.2 | IMD34 |  |
|  | n3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | 1 | 1960 | 5 | 25 | 2150 | N/A | N/A |  |
| DC_1A_n3A-n79A | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4950 | 4.7 | IMD5 |  |
| DC_1A_n5A-n40A | 1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | n5 | 826.5 | 5 | 25 | 871.5 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2305 | 9.0 | IMD4 |  |
|  | 1 | 1945 | 5 | 25 | 2135 | N/A | N/A |  |
|  | n5 | N/A | 5 | N/A | 880 | 8.5 | IMD4 |  |
|  | n40 | 2385 | 10 | 50 | 2385 | N/A | N/A |  |
| DC_1A-7A_n28ADC_1A-7C_n28A DC_1A-7A-7A_n28A | 1 | 1935 | 5 | 25 | 2125 | N/A | N/A |  |
|  | n28 | 718 | 5 | 25 | 773 | N/A | N/A |  |
|  | 7 | N/A | 10 | N/A | 2653 | 30.0 | IMD2 |  |
| DC_1A-7A_n40A | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
| DC_1A-7A-7A_n40A | 7 | N/A | 5 | N/A | 2630 | 23 | IMD3 |  |
|  | n40 | 2390 | 10 | 50 | 2390 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2120 | 16.4 | IMD3 |  |
|  | 7 | 2530 | 5 | 25 | 2650 | N/A | N/A |  |
|  | n40 | 2310 | 10 | 50 | 2310 | N/A | N/A |  |
| DC_1A-8A_n41A | 1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 927.5 | 0.5 | IMD5 |  |
|  | n41 | 2502.5 | 10 | 50 | 2502.5 | N/A | N/A |  |
| DC_1A_n8A-n77A | 1 | 1955 | 5 | 25 | 2145 | N/A | N/A |  |
| DC_1A_n8A-n77(2A) | n8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3410 | 1.5 | IMD5 |  |
|  | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3960 | 8.8 | IMD3 |  |
|  | 1 | 1955 | 5 | 25 | 2145 | N/A | N/A |  |
|  | n8 | N/A | 5 | N/A | 955 | 3.3 | IMD5 |  |
|  | n77 | 3410 | 10 | 50 | 3410 | N/A | N/A |  |
| DC_1A-8A_n78A | 1 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_1A_n8A-n78(2A) | 8 | N/A | N/A | N/A | N/A | N/A | IMD5 |  |
|  | n78 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_1A-3A_n77ADC_1A-3A_n77(2A)DC_1A-3A_n77(3A)DC_1A-3C_n77ADC_1A-3A_n77CDC_1A-3C_n77(2A) | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1807.5 | 31.5 | IMD29 |  |
|  | n77 | 3757.5 | 10 | 50 | 3757.5 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2140 | 31.0 | IMD2 |  |
|  | 3 | 1775 | 5 | 25 | 1870 | N/A | N/A |  |
|  | n77 | 3915 | 10 | 50 | 3915 | N/A | N/A |  |
| DC_1A-3A_n78ADC_1A-3A-3A_n78ADC_1A-3C_n78ADC_1A-3A_n78CDC_1A-3A_n78(2A)DC_1A-3C_n78(2A) DC_1A-3A_n78(A-C) | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1807.5 | 31.2 | IMD2 |  |
|  | n78 | 3757.5 | 10 | 50 | 3757.5 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2125 | 2.8 | IMD5 |  |
|  | 3 | 1775 | 5 | 25 | 1870 | N/A | N/A |  |
|  | n78 | 3725 | 10 | 50 | 3725 | N/A | N/A |  |
| DC_1A_n3A-n77ADC_1A_n3A-n77(2A) | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n3 | 1750 | 5 | 25 | 1845 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3700 | 28.4 | IMD29 |  |
|  | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1807.5 | 31.5 | IMD29 |  |
|  | n77 | 3757.5 | 10 | 50 | 3757.5 | N/A | N/A |  |
| DC_1A_n3A-n78A | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n3 | 1750 | 5 | 25 | 1845 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3700 | 28.4 | IMD2 |  |
|  | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1830 | 27.9 | IMD2 |  |
|  | n78 | 3780 | 10 | 50 | 3780 | N/A | N/A |  |
| DC_1A-3A_n105A | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1855 | 4 | IMD5 |  |
|  | n105 | 695 | 5 | 25 | 644 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2160 | 5 | IMD4 |  |
|  | 3 | 1775 | 5 | 25 | 1870 | N/A | N/A |  |
|  | n105 | 695 | 5 | 25 | 644 | N/A | N/A |  |
| DC_1A-5A_n77ADC_1A-5A_n77(2A)DC_1A-5A_n77(3A) | 1 | N/A | 5 | N/A | 2122 | 18.1 | IMD3 |  |
|  | 5 | 829 | 5 | 25 | 874 | N/A | N/A |  |
|  | n77 | 3780 | 10 | 50 | 3780 | N/A | N/A |  |
|  | 1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 885 | 3.1 | IMD5 |  |
|  | n77 | 3405 | 10 | 50 | 3405 | N/A | N/A |  |
| DC_1A-5A_n78ADC_1A-5A_n78CDC_1A-5A_n78(A-C) | 1 | N/A | 5 | N/A | 2122 | 18.1 | IMD3 |  |
|  | 5 | 829 | 5 | 25 | 874 | N/A | N/A |  |
|  | n78 | 3780 | 10 | 50 | 3780 | N/A | N/A |  |
|  | 1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 885 | 3.1 | IMD5 |  |
|  | n78 | 3405 | 10 | 50 | 3405 | N/A | N/A |  |
| DC_1A_n5A-n78A | 1 | 1932 | 5 | 25 | 2122 | N/A | N/A |  |
|  | n5 | 829 | 5 | 25 | 874 | N/A | N/A |  |
|  | n78 | 3583 | 10 | 50 | 3583 | 18.1 | IMD3 |  |
|  | 1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | n5 | 840 | 5 | 25 | 885 | 3.1 | IMD5 |  |
|  | n78 | 3405 | 10 | 50 | 3405 | N/A | N/A |  |
| DC_1A-7A_n77ADC_1A-7A_n77(2A)DC_1A-7A_n77(3A)DC_1A-7A-7A_n77ADC_1A-7A-7A_n77(2A)DC_1A-7A-7A_n77(3A) | 1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2627.5 | 9.1 | IMD44 |  |
|  | n77 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2140 | 8.7 | IMD4 |  |
|  | 7 | 2510 | 10 | 50 | 2630 | N/A | N/A |  |
|  | n77 | 3580 | 10 | 50 | 3580 | N/A | N/A |  |
| DC_1A-7A_n78ADC_1A-7C_n78ADC_1A-7A_n78(2A)DC_1A-7C_n78(2A)DC_1A-7A_n78CDC_1A-7A_n78(A-C)DC_1A-1A-7A_n78ADC_1A-7A-7A_n78CDC_1A-7A-7A_n78(A-C) | 1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2627.5 | 9.1 | IMD4 |  |
|  | n78 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2140 | 8.7 | IMD4 |  |
|  | 7 | 2510 | 10 | 50 | 2630 | N/A | N/A |  |
|  | n78 | 3580 | 10 | 50 | 3580 | N/A | N/A |  |
| DC_1A_n7A-n78ADC_1A_n7B-n78ADC_1A_n7A-n78(2A) | 1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2627.5 | 9.1 | IMD4 |  |
|  | n78 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n7 | 2520 | 5 | 25 | 2640 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3390 | 10.1 | IMD4 |  |
| DC_1A-3A_n79A | 1 | N/A | 5 | N/A | 2140 | 3.6 | IMD5 |  |
|  | 3 | 1750 | 5 | 25 | 1845 | N/A | N/A |  |
|  | n79 | 4860 | 40 | 216 | 4860 | N/A | N/A |  |
| DC_1A-5A_n28A | 1 | N/A | 5 | N/A | 2123 | 4 | IMD5 |  |
|  | 5 | 829 | 5 | 25 | 874 | N/A | N/A |  |
|  | n28 | 738 | 5 | 25 | 793 | N/A | N/A |  |
|  | 1 | 1965 | 5 | 25 | 2155 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 875 | 4.6 | IMD5 |  |
|  | n28 | 710 | 5 | 25 | 765 | N/A | N/A |  |
| DC_1A-5A_n40A | 1 | N/A | 5 | N/A | 2144 | 4.0 | IMD5 |  |
|  | 5 | 832 | 5 | 25 | 877 | N/A | N/A |  |
|  | n40 | 2320 | 10 | 50 | 2320 | N/A | N/A |  |
|  | 1 | 1945 | 5 | 25 | 2135 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 880 | 8.0 | IMD4 |  |
|  | n40 | 2385 | 10 | 50 | 2385 | N/A | N/A |  |
| DC_1A-5A_n79A | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 882.5 | 18.3 | IMD3 |  |
|  | n79 | 4782.5 | 40 | 216 | 4782.5 | N/A | N/A |  |
|  | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 882.5 | 8.9 | IMD4 |  |
|  | n79 | 4907.5 | 40 | 216 | 4907.5 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2140 | 8.1 | IMD4 |  |
|  | 5 | 837.5 | 5 | 25 | 882.5 | N/A | N/A |  |
|  | n79 | 4652.5 | 40 | 216 | 4652.5 | N/A | N/A |  |
| DC_1A-7A_n105A | 1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2673 | 30 | IMD2 |  |
|  | n105 | 698 | 5 | 25 | 647 | N/A | N/A |  |
| DC_1A-8A_n7A | 1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | n7 | 2502.5 | 5 | 25 | 2622.5 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 927.5 | 1.0 | IMD5 |  |
| DC_1A-8A_n28A | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n28 | 730 | 5 | 25 | 785 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 950 | 3.3 | IMD5 |  |
| DC_1A-8A_n40A | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 930 | 8.0 | IMD4 |  |
|  | n40 | 2395 | 10 | 50 | 2395 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2135 | 5.3 | IMD5 |  |
|  | 8 | 885 | 5 | 25 | 930 | N/A | N/A |  |
|  | n40 | 2395 | 10 | 50 | 2395 | N/A | N/A |  |
| DC_1A-8A_n77A | 1 | 1955 | 5 | 25 | 2145 | N/A | N/A |  |
| DC_1A-8A_n77(2A)DC_1A-8A_n77(3A)DC_1A-8B_n77ADC_1A-8B_n77(2A) | n77 | 3410 | 10 | 50 | 3410 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 955 | 3.3 | IMD5 |  |
|  | 1 | N/A | 5 | N/A | 2140 | 14.4 | IMD3 |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n77 | 3960 | 10 | 50 | 3960 | N/A | N/A |  |
| DC_1A-8A_n79A | 1 | 1935 | 5 | 25 | 2125 | N/A | N/A |  |
|  | n79 | 4815 | 40 | 216 | 4815 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 945 | 15.8 | IMD3 |  |
|  | 1 | N/A | 5 | N/A | 2145 | 8.2 | IMD4 |  |
|  | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n79 | 4845 | 40 | 216 | 4845 | N/A | N/A |  |
| DC_1A_n8A-n40A | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n8 | N/A | 5 | N/A | 930 | 8.0 | IMD4 |  |
|  | n40 | 2395 | 10 | 50 | 2395 | N/A | N/A |  |
| DC_1A_n8A-n78A | 1 | 1945 | 5 | 25 | 2135 | N/A | N/A |  |
|  | n8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3745 | 14.9 | IMD3 |  |
|  | 1 | 1940 | 5 | 25 | 2130 | N/A | N/A |  |
|  | n8 | N/A | 5 | N/A | 940 | 3.3 | IMD5 |  |
|  | n78 | 3380 | 10 | 50 | 3330 | N/A | N/A |  |
| DC_1A-11A_n3A | 1 | 1960 | 5 | 25 | 2150 | N/A | N/A |  |
|  | n3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | 11 | N/A | 5 | N/A | 1480 | 15.2 | IMD3 |  |
| DC_1A-11A_n28A | 11 | 1440 | 5 | 25 | 1488 | N/A | N/A |  |
|  | n28 | 710 | 5 | 25 | 765 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2150 | 28.3 | IMD21 |  |
| DC_1A-11A_n41A | 11 | 1442 | 5 | 25 | 1490 | N/A | N/A |  |
|  | n41 | 2520 | 10 | 50 | 2520 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2156 | 10.2 | IMD4 |  |
|  | 1 | 1940 | 5 | 25 | 2130 | N/A | N/A |  |
|  | n41 | 2685 | 10 | 50 | 2685 | N/A | N/A |  |
|  | 11 | N/A | 5 | N/A | 1490 | 10.6 | IMD4 |  |
| DC_1A-11A_n77ADC_1A-11A_n77(2A)DC_1A-11A_n77(3A) | 1 | 1955 | 5 | 25 | 2145 | N/A | N/A |  |
|  | 11 | N/A | 5 | N/A | 1486 | 31.4 | IMD2 |  |
|  | n77 | 3441 | 10 | 50 | 3441 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2140 | 30.8 | IMD2 |  |
|  | 11 | 1438 | 5 | 25 | 1486 | N/A | N/A |  |
|  | n77 | 3578 | 10 | 50 | 3578 | N/A | N/A |  |
| DC_1A-11A_n78ADC_1A-11A_n78(2A) | 1 | 1955 | 5 | 25 | 2145 | N/A | N/A |  |
|  | 11 | N/A | 5 | N/A | 1486 | 31.4 | IMD2 |  |
|  | n78 | 3441 | 10 | 50 | 3441 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2140 | 30.8 | IMD2 |  |
|  | 11 | 1438 | 5 | 25 | 1486 | N/A | N/A |  |
|  | n78 | 3578 | 10 | 50 | 3578 | N/A | N/A |  |
| DC_1A-11A_n79A | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | 11 | N/A | 5 | N/A | 1483 | 10.2 | IMD4 |  |
|  | n79 | 4427 | 40 | 216 | 4427 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2118 | 15.6 | IMD3 |  |
|  | 11 | 1431 | 5 | 25 | 1479 | N/A | N/A |  |
|  | n79 | 4980 | 40 | 216 | 4980 | N/A | N/A |  |
| DC_1A-18A_n77ADC_1A-18A_n77(2A) | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | 18 | N/A | 5 | N/A | 870 | 3.5 | IMD5 |  |
|  | n77 | 3390 | 10 | 50 | 3390 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2120 | 16.4 | IMD3 |  |
|  | 18 | 825 | 5 | 25 | 870 | N/A | N/A |  |
|  | n77 | 3770 | 10 | 50 | 3770 | N/A | N/A |  |
| DC_1A-18A_n78ADC_1A-18A_n78(2A) | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | 18 | N/A | 5 | N/A | 870 | 3.5 | IMD5 |  |
|  | n78 | 3390 | 10 | 50 | 3390 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2120 | 16.4 | IMD3 |  |
|  | 18 | 819 | 5 | 25 | 864 | N/A | N/A |  |
|  | n78 | 3758 | 10 | 50 | 3758 | N/A | N/A |  |
| DC_1A-18A_n79A | 1 | 1935 | 5 | 25 | 2125 | N/A | N/A |  |
|  | 18 | N/A | 5 | N/A | 867.5 | 18.3 | IMD3 |  |
|  | n79 | 4737.5 | 40 | 216 | 4737.5 | N/A | N/A |  |
|  | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 18 | N/A | 5 | N/A | 865 | 8.9 | IMD4 |  |
|  | n79 | 4925 | 40 | 216 | 4925 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2125 | 8.1 | IMD4 |  |
|  | 18 | 822.5 | 5 | 25 | 867.5 | N/A | N/A |  |
|  | n79 | 4592.5 | 40 | 216 | 4592.5 | N/A | N/A |  |
| DC_1A-19A_n77ADC_1A-19A_n78A | 1 | N/A | 5 | N/A | 2130 | 17.8 | IMD3 |  |
|  | 19 | 832.5 | 5 | 25 | 877.5 | N/A | N/A |  |
|  | n77, n78 | 3795 | 10 | 50 | 3795 | N/A | N/A |  |
|  | 1 | 1940 | 5 | 25 | 2130 | N/A | N/A |  |
|  | 19 | N/A | 5 | N/A | 880 | 5.1 | IMD5 |  |
|  | n77, n78 | 3350 | 10 | 50 | 3350 | N/A | N/A |  |
| DC_1A-19A_n79A | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 19 | N/A | 5 | N/A | 882.5 | 18.3 | IMD3 |  |
|  | n79 | 4782.5 | 40 | 216 | 4782.5 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2140 | 8.1 | IMD4 |  |
|  | 19 | 837.5 | 5 | 25 | 882.5 | N/A | N/A |  |
|  | n79 | 4652.5 | 40 | 216 | 4652.5 | N/A | N/A |  |
| DC_1A-20A_n1A | n1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 20 | 850 | 5 | 25 | 809 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2160 | 6 | IMD4 |  |
| DC_1A_n28A-n41A | 1 | 1935 | 5 | 25 | 2125 | N/A | N/A |  |
|  | n28 | 718 | 5 | 25 | 773 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2653 | 30.1 | IMD2 |  |
|  | 1 | 1923 | 5 | 25 | 2113 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 762 | 29.3 | IMD2 |  |
|  | n41 | 2685 | 10 | 50 | 2685 | N/A | N/A |  |
|  | 1 | 1935 | 5 | 25 | 2125 | N/A | N/A |  |
|  | n28 | N/A | 10 | N/A | 785 | 4.5 | IMD5 |  |
|  | n41 | 2510 | 10 | 50 | 2510 | N/A | N/A |  |
| DC_1A-20A_n7A | 1 | 1940 | 5 | 25 | 2130 | N/A | N/A |  |
|  | 20 | N/A | 10 | N/A | 800 | 4.5 | IMD5 |  |
|  | n7 | 2510 | 10 | 50 | 2630 | N/A | N/A |  |
| DC_1A-20A_n8A | 1 | 1925 | 5 | 25 | 2115 | N/A | N/A |  |
|  | 20 | N/A | 5 | N/A | 805 | 11.5 | IMD4 |  |
|  | n8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
| DC_1A-20A_n38A | 1 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 20 | N/A | N/A | N/A | N/A | N/A | IMD5 |  |
|  | n38 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_1A-20A_n78ADC_1A-1A-20A_n78A | 1 | N/A | 5 | N/A | 2120 | 20.3 | IMD3 |  |
| DC_1A-20A_n78(2A) | 20 | 835 | 5 | 25 | 794 | N/A | N/A |  |
| DC_1A-20A_n78C | n78 | 3790 | 10 | 50 | 3790 | N/A | N/A |  |
|  | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 20 | N/A | 5 | N/A | 810 | 3.0 | IMD5 |  |
|  | n78 | 3330 | 10 | 50 | 3330 | N/A | N/A |  |
| DC_1A-21A_n28A10 | 1 | N/A | 5 | N/A | 2165.3 | 16.1 | IMD3 |  |
|  | 21 | 1450.4 | 5 | 25 | 1498.4 | N/A | N/A |  |
|  | n28 | 735.5 | 5 | 25 | 790.5 | N/A | N/A |  |
| DC_1A-21A_n77ADC_1A-21A_n78A | 1 | N/A | 5 | N/A | 2154.6 | 30.6 | IMD2 |  |
|  | 21 | 1450.4 | 5 | 25 | 1498.4 | N/A | N/A |  |
|  | n77, n78 | 3605 | 10 | 50 | 3605 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2154.6 | 3.6 |  | IMD5 |
|  | 21 | 1450.4 | 5 | 25 | 1498.4 | N/A |  | N/A |
|  | n77, n78 | 3647 | 10 | 50 | 3647 | N/A |  | N/A |
|  | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 21 | N/A | 5 | N/A | 1500 | 31.5 | IMD2 |  |
|  | n77, n78 | 3450 | 10 | 50 | 3450 | N/A | N/A |  |
|  | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 21 | N/A | 5 | N/A | 1500 | 2.9 | IMD5 |  |
|  | n77, n78 | 3675 | 10 | 50 | 3675 | N/A | N/A |  |
| DC_1A-21A_n79A | 1 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 21 | N/A | N/A | N/A | N/A | N/A | IMD4 |  |
|  | n79 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_1A-26A_n78A | 1 | N/A | 5 | N/A | 2122 | 18.1 | IMD3 |  |
|  | 26 | 829 | 5 | 25 | 874 | N/A | N/A |  |
|  | n78 | 3780 | 10 | 50 | 3780 | N/A | N/A |  |
|  | 1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | 26 | N/A | 5 | N/A | 885 | 3.1 | IMD5 |  |
|  | n78 | 3405 | 10 | 50 | 3405 | N/A | N/A |  |
| DC_1A_n26A-n78A | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n26 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3610 | 15.7 | IMD3 |  |
|  | 1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | n26 | N/A | 5 | N/A | 885 | 3.1 | IMD5 |  |
|  | n78 | 3405 | 10 | 50 | 3405 | N/A | N/A |  |
| DC_1A-28A_n3A | 1 | N/A | 5 | N/A | 2139 | 11.0 | IMD4 |  |
|  | 28 | 710.5 | 5 | 25 | 765.5 | N/A | N/A |  |
|  | n3 | 1780 | 5 | 25 | 1875 | N/A | N/A |  |
| DC_1A-28A_n7ADC_1A-1A-28A_n7ADC_1A-28A_n7BDC_1A-1A-28A_n7B | 1 | 1935 | 5 | 25 | 2125 | N/A | N/A |  |
|  | 28 | N/A | 10 | N/A | 785 | 4.5 | IMD5 |  |
|  | n7 | 2510 | 10 | 50 | 2630 | N/A | N/A |  |
| DC_1A-28A_n40A | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
| DC_1A-28C_n40A | 28 | N/A | 5 | N/A | 780 | 8.9 | IMD4 |  |
|  | n40 | 2340 | 10 | 50 | 2340 | N/A | N/A |  |
| DC_1A-28A_n38A | 1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 765 | 4.5 | IMD5 |  |
|  | n38 | 2580 | 5 | 25 | 2580 | N/A | N/A |  |
| DC_1A-28A_n71A | 1 | 1922.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 779.5 | 7.5 | IMD5 |  |
|  | n71 | 675.5 | 5 | 25 | 629.5 | N/A | N/A |  |
| DC_1A-28A_n77A | 1 | N/A | 5 | N/A | 2150 | 15.7 | IMD3 |  |
|  | 28 | 740 | 5 | 25 | 795 | N/A | N/A |  |
|  | n77 | 3630 | 10 | 50 | 3630 | N/A | N/A |  |
|  | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 794 | 4.2 | IMD5 |  |
|  | n77 | 3352 | 10 | 50 | 3352 | N/A | N/A |  |
| DC_1A-28A_n78A | 1 | N/A | 5 | N/A | 2150 | 15.7 | IMD3 |  |
|  | 28 | 740 | 5 | 25 | 795 | N/A | N/A |  |
|  | n78 | 3630 | 10 | 50 | 3630 | N/A | N/A |  |
|  | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 794 | 4.2 | IMD5 |  |
|  | n78 | 3352 | 10 | 50 | 3352 | N/A | N/A |  |
| DC_1A-28A_n79A | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 788 | 15.2 | IMD3 |  |
|  | n79 | 4648 | 40 | 216 | 4648 | N/A | N/A |  |
|  | 1 | 1925 | 5 | 25 | 2115 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 795 | 10.0 | IMD4 |  |
|  | n79 | 4980 | 40 | 216 | 4980 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2167.5 | 1.2 | IMD4 |  |
|  | 28 | 745.5 | 5 | 25 | 800.5 | N/A | N/A |  |
|  | n79 | 4420 | 40 | 216 | 4420 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2125 | 4.5 | IMD5 |  |
|  | 28 | 718 | 5 | 25 | 773 | N/A | N/A |  |
|  | n79 | 4807 | 40 | 216 | 4807 | N/A | N/A |  |
| DC_1A_n28A-n40A | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2374 | 10.1 | IMD4 |  |
|  | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 768 | 8.6 | IMD4 |  |
|  | n40 | 2314 | 10 | 50 | 2314 | N/A | N/A |  |
| DC_1A_n28A-n77ADC_1A_n28A-n78A | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n28 | 733 | 5 | 25 | 788 | N/A | N/A |  |
|  | n77/n78 | N/A | 10 | N/A | 3416 | 15.7 | IMD3 |  |
|  | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n77/n78 | 3320 | 10 | 50 | 3320 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 790 | 4.2 | IMD5 |  |
| DC_1A_n28A-n79A | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 788 | 15.2 | IMD39 |  |
|  | n79 | 4648 | 40 | 216 | 4648 | N/A | N/A |  |
|  | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n28 | 730 | 5 | 25 | 785 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4630 | 14.9 | IMD34 |  |
| DC_1A-32A_n3A | n3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1480 | 15.2 | IMD34 |  |
|  | 1 | 1960 | 5 | 25 | 2150 | N/A | N/A |  |
| DC_1-32_n41 | 1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1454.5 | 13.2 | IMD3 |  |
|  | n41 | 2501 | 10 | 50 | 2501 | N/A | N/A |  |
|  | 1 | 1925 | 5 | 25 | 2115 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1490 | 6.2 | IMD4 |  |
|  | n41 | 2670 | 10 | 50 | 2670 | N/A | N/A |  |
| DC_1A-32A_n78ADC_1A-32A_n78CDC_1A-32A_n78(2A) | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1470 | 31.8 | IMD2 |  |
|  | n78 | 3400 | 10 | 50 | 3400 | N/A | N/A |  |
|  | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1470 | 0 | IMD5 |  |
|  | n78 | 3630 | 10 | 50 | 3630 | N/A | N/A |  |
| DC_1A-38A_n78ADC_1A-38A_n78(2A) | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | 38 | N/A | 5 | N/A | 2590 | 12.7 | IMD4 |  |
|  | n78 | 3320 | 10 | 50 | 3320 | N/A | N/A |  |
| DC_1A_n38A-n78A | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n38 | N/A | 10 | N/A | 2590 | 12.7 | IMD4 |  |
|  | n78 | 3320 | 10 | 50 | 3320 | N/A | N/A |  |
| DC_1A-40A_n28A | 1 | 1920 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 40 | N/A | 5 | N/A | 2374 | 10.1 | IMD4 |  |
|  | n28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
| DC_1A_n40A-n41A | 1 | 1922.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
|  | n40 | 2302.5 | 5 | 25 | 2302.5 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2682.5 | 20 | IMD3 |  |
| DC_1A_n40A-n71A | 1 | 1977 | 5 | 25 | 2167 | N/A | N/A |  |
|  | n40 | 2305 | 10 | 50 | 2305 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 649 | 1 | IMD4 |  |
| DC_1A_n40A-n77A | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
| DC_1A_n40A-n77(2A) | n40 | 2340 | 10 | 50 | 2340 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3450 | 9.8 | IMD4 |  |
|  | 1 | 1960 | 5 | 25 | 2150 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2360 | 10.6 | IMD4 |  |
|  | n77 | 3520 | 10 | 50 | 3520 | N/A | N/A |  |
| DC_1A-40A_n78ADC_1A-40C_n78A | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 40 | N/A | 5 | N/A | 2340 | 10.6 | IMD4 |  |
|  | n78 | 3450 | 10 | 50 | 3450 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2140 | 9.1 | IMD4 |  |
|  | 40 | 2360 | 5 | 25 | 2360 | N/A | N/A |  |
|  | n78 | 3430 | 10 | 50 | 3430 | N/A | N/A |  |
| DC_1A_n40A-n78ADC_1A_n40A-n78(2A) | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
| DC_1A_n40A-n78C | n40 | 2340 | 10 | 50 | 2340 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3450 | 9.8 | IMD4 |  |
|  | 1 | 1960 | 5 | 25 | 2150 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2360 | 10.6 | IMD4 |  |
|  | n78 | 3520 | 10 | 50 | 3520 | N/A | N/A |  |
| DC_1_n40-n105 | 1 | 1977 | 5 | 25 | 2167 | N/A | N/A |  |
|  | n40 | 2305 | 10 | 50 | 2305 | N/A | N/A |  |
|  | n105 | 700 | 5 | 25 | 649 | 1 | IMD4 |  |
| DC_1A-41A_n3ADC_1A-41C_n3A | 1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2507.5 | 5.0 | IMD5 |  |
|  | n3 | 1712.5 | 5 | 25 | 1807.5 | N/A | N/A |  |
| DC_1A-41A_n28A | 1 | 1935 | 5 | 25 | 2125 | N/A | N/A |  |
|  | 41 | N/A | 10 | N/A | 2653 | 30 | IMD2 |  |
|  | n28 | 718 | 5 | 25 | 773 | N/A | N/A |  |
| DC_1A-41A_n77ADC_1A-41C_n77ADC_1A-41A_n77(2A)DC_1A-41C_n77(2A) | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | 41 | 2510 | 5 | 25 | 2510 | 11.0 | IMD4 |  |
|  | n77 | 3400 | 10 | 50 | 3400 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2140 | 9.3 | IMD4 |  |
|  | 41 | 2640 | 5 | 25 | 2640 | N/A | N/A |  |
|  | n77 | 3710 | 10 | 50 | 3710 | N/A | N/A |  |
|  | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 41 | 2510 | 5 | 25 | 2510 | 3.6 | IMD5 |  |
|  | n77 | 4150 | 10 | 50 | 4150 | N/A | N/A |  |
| DC_1A_n41A-n77ADC_1A_n41A-n77(2A) | 1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2515 | 11.5 | IMD44 |  |
|  | n77 | 3410 | 10 | 50 | 3410 | N/A | N/A |  |
|  | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n41 | 2650 | 10 | 25 | 2650 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3330 | 19.6 | IMD34,9 |  |
| DC_1A-41A_n78ADC_1A-41C_n78ADC_1A-41A_n78(2A)DC_1A-41C_n78(2A) | 1 | N/A | 5 | N/A | 2140 | 9.3 | IMD4 |  |
|  | 41 | 2640 | 5 | 25 | 2640 | N/A | N/A |  |
|  | n78 | 3710 | 10 | 50 | 3710 | N/A | N/A |  |
|  | 1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2515 | 12 | IMD4 |  |
|  | n78 | 3410 | 10 | 50 | 3410 | N/A | N/A |  |
| DC_1A_n41A-n78ADC_1A_n41A-n78(2A) | 1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2515 | 11.5 | IMD44 |  |
|  | n78 | 3410 | 10 | 50 | 3410 | N/A | N/A |  |
|  | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n41 | 2650 | 10 | 25 | 2650 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3330 | 19.6 | IMD34,9 |  |
| DC_1A-41A_n79A | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2530 | 29.4 | IMD2 |  |
|  | n79 | 4500 | 40 | 216 | 4500 | N/A | N/A |  |
| DC_1A-42A_n3A | 1 | 1922.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
|  | n3 | 1782.5 | 5 | 25 | 1877.5 | N/A | N/A |  |
|  | 42 | N/A | 5 | N/A | 3425 | 13.0 | IMD4 |  |
| DC_1A-42A_n28A | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n28 | 733 | 5 | 25 | 788 | N/A | N/A |  |
|  | 42 | N/A | 5 | N/A | 3416 | 15.7 | IMD3 |  |
|  | 1 | N/A | 5 | N/A | 2134 | 15.7 | IMD3 |  |
|  | 42 | 3580 | 5 | 25 | 3580 | N/A | N/A |  |
|  | n28 | 723 | 5 | 25 | 778 | N/A | N/A |  |
| DC_1A-42A_n79A | 1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | n79 | 4420 | 40 | 216 | 4420 | N/A | N/A |  |
|  | 42 | N/A | 5 | N/A | 3490 | 4.8 | IMD5 |  |
|  | 42 | 3402.5 | 5 | 25 | 3402.5 | N/A | N/A |  |
|  | n79 | 4640 | 40 | 216 | 4640 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2165 | 15.5 | IMD3 |  |
|  | 42 | 3450 | 5 | 25 | 3450 | N/A | N/A |  |
|  | n79 | 4520 | 40 | 216 | 4520 | N/A | N/A |  |
|  | 1 | N/A | 5 | N/A | 2140 | 9.3 | IMD4 |  |
| DC_1A_n71A-n77A | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 635 | 15.2 | IMD3 |  |
|  | n77 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n71 | 686 | 5 | 25 | 640 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3342 | 15.7 | IMD3 |  |
|  | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n71 | 680 | 5 | 25 | 634 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3990 | 9.4 | IMD4 |  |
| DC_1A_SUL_n77A-n80A | 1 | N/A | 5 | N/A | 2140 | 23 | IMD3 |  |
|  | n80 | 1760 | 5 | 25 | N/A | N/A | N/A |  |
|  | 1 | 1922.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3425 | 13.0 | IMD4 |  |
|  | n80 | 1782.5 | 5 | 25 |  | N/A | N/A |  |
| DC_1A_n75A-n78ADC_1A_n75A-n78(2A) | 1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n75 | N/A | 5 | N/A | 1470 | 30.4 | IMD2 |  |
|  | n78 | 3400 | 10 | 50 | 3400 | N/A | N/A |  |
| DC_1A_n78A-n79A | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n78 | 3410 | 10 | 50 | 3410 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4870 | 15.9 | IMD3 |  |
|  | 1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n79 | 4670 | 40 | 216 | 4670 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3490 | 4.6 | IMD5 |  |
| DC_1A_SUL_n78A-n80ADC_1A_SUL_n78C-n80A | 1 | 1950 | 5 | 25 | 2140 | 23 | IMD3 |  |
|  | n80 | 1760 | 5 | 25 | N/A | N/A | N/A |  |
|  | 1 | 1922.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
|  | n80 | 1782.5 | 5 | 25 |  | N/A | N/A |  |
|  | n78 | 3425 | 10 | 50 | 3425 | 13.0 | IMD4 |  |
| DC_1_n78-n105 | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n78 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | n105 | 686 | 5 | 25 | 635 | 15.2 | IMD3 |  |
|  | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3342 | 15.7 | IMD3 |  |
|  | n105 | 686 | 5 | 25 | 635 | N/A | N/A |  |
| DC_2A-(n)66AA | 2 | 1883.3 | 5 | 25 | 1963.3 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2145 | 2.8 | IMD5 |  |
|  | n66 | 1750 | 5 | 25 | 2150 | 4 | IMD5 |  |
| DC_2A_n2A-n66A | 2 | 1875 | 5 | 25 | 1955 | N/A | N/A |  |
|  | n2 | N/A | 5 | N/A | 1975 | 20 | IMD3 |  |
|  | n66 | 1775 | 5 | 25 | 2175 | N/A | N/A |  |
| DC_2A_n2A-n77A | 2 | 1875 | 5 | 25 | 1955 | N/A | N/A |  |
|  | n2 | N/A | 5 | N/A | 1935 | 26 | IMD29 |  |
|  | n77 | 3810 | 10 | 50 | 3810 | N/A | N/A |  |
| DC_2A_n2A-n78A | 2 | 1852.5 | 5 | 25 | 1932.5 | N/A | N/A |  |
|  | n2 | N/A | 5 | N/A | 1942.5 | 26 | IMD24 |  |
|  | n78 | 3795 | 10 | 50 | 3795 | N/A | N/A |  |
| DC_2A-4A_n28A | 2 | N/A | 5 | N/A | 1960 | 11.0 | IMD4 |  |
|  | 4 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n28 | 740 | 5 | 25 | 795 | N/A | N/A |  |
| DC_2A-4A_n41A | 2 | N/A | 5 | N/A | 1940 | 11.0 | IMD4 |  |
|  | 4 | 1715 | 5 | 25 | 2115 | N/A | N/A |  |
|  | n41 | 2685 | 10 | 50 | 2685 | N/A | N/A |  |
| DC_2A-4A_n78A | 2 | 1875 | 5 | 25 | 1955 | N/A | N/A |  |
|  | 4 | N/A | 5 | N/A | 2145 | 10.3 | IMD4 |  |
|  | n78 | 3480 | 10 | 50 | 3480 | N/A | N/A |  |
|  | 2 | N/A | 5 | N/A | 1960 | 32.1 | IMD29 |  |
|  | 4 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n78 | 3700 | 10 | 50 | 3700 | N/A | N/A |  |
|  | 2 | N/A | 5 | N/A | 1950 | 2.1 | IMD5 |  |
|  | 4 | 1750 | 5 | 25 | 2150 | N/A | N/A |  |
|  | n78 | 3600 | 10 | 50 | 3600 | N/A | N/A |  |
| DC_2A_n5A-n7A | 2 | 1855 | 5 | 25 | 1935 | N/A | N/A |  |
|  | n5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2685 | 30.0 | IMD2 |  |
| DC_2A-5A_n12A8 | 2 | N/A | 5 | N/A | 1980 | 5.9 | IMD5 |  |
|  | 5 | 840 | 5 | 25 | 885 | N/A | N/A |  |
|  | n12 | 705 | 5 | 25 | 735 | N/A | N/A |  |
| DC_2A-5A_n30A | 2 | 1870 | 5 | 25 | 1950 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 880 | 9.7 | IMD4 |  |
|  | n30 | 2310 | 10 | 50 | 2355 | N/A | N/A |  |
| DC_2A-5A_n48ADC_2A-5A_n48B | 2 | N/A | 5 | N/A | 1962 | 15.6 | IMD3 |  |
|  | 5 | 839 | 5 | 25 | 884 | N/A | N/A |  |
|  | n48 | 3640 | 10 | 50 | 3640 | N/A | N/A |  |
| DC_2A-5A_n71A | 2 | 1855 | 5 | 25 | 1935 | N/A | N/A |  |
|  | n71 | 686.5 | 5 | 25 | 640.5 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 891.5 | 4.2 | IMD5 |  |
| DC_2A_n5A-n77A | 2 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
|  | n5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3540 | 16.0 | IMD3 |  |
| DC_2A_n5A-n77A11 | 2 | 1907 | 5 | 25 | 1987 | N/A | N/A |  |
|  | n5 | N/A | 5 | N/A | 889 | 3.8 | IMD5 |  |
|  | n77 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
| DC_2A-5A_n77A11 | 2 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
| DC_2A-5A_n77C11DC_2A-5A_n77(2A)11DC_2A-2A-5A_n77A11 | 5 | N/A | 5 | N/A | 887.5 | 3.8 | IMD5 |  |
| DC_2A-2A-5A_n77C11DC_2A-2A-5A_n77(2A)11 | n77 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | 2 | N/A | 5 | N/A | 1987 | 16.5 | IMD3 |  |
|  | 5 | 846.5 | 5 | 25 | 891.5 | N/A | N/A |  |
|  | n77 | 3680 | 10 | 50 | 3680 | N/A | N/A |  |
| DC_2A-5A_n78ADC_2A-2A-5A_n78ADC_2A-5A_n78(2A) | 2 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 887.5 | 3.8 | IMD5 |  |
|  | n78 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | 2 | N/A | 5 | N/A | 1987 | 16.5 | IMD3 |  |
|  | 5 | 846.5 | 5 | 25 | 891.5 | N/A | N/A |  |
|  | n78 | 3680 | 10 | 50 | 3680 | N/A | N/A |  |
| DC_2A-7A_n5ADC_2A-7C_n5ADC_2A-7A-7A_n5A | 2 | 1855 | 10 | 50 | 1935 | N/A | N/A |  |
|  | 7 | N/A | 10 | N/A | 2685 | 30.0 | IMD2 |  |
|  | n5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
| DC_2A-7A_n12ADC_2A-2A-7A_n12A | 2 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2622.5 | 30.8 | IMD2 |  |
|  | n12 | 713.5 | 5 | 25 | 743.5 | N/A | N/A |  |
| DC_2A_n7A-n12A | 2 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | N/A | 30.8 | IMD2 |  |
|  | n12 | 713.5 | 5 | 25 | 743.5 | N/A | N/A |  |
|  | 2 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
|  | n7 | 2502.5 | 5 | 25 | 2622.5 | N/A | N/A |  |
|  | n12 | N/A | 5 | N/A | 731.5 | 4.5 | IMD5 |  |
| DC_2A-7A_n28ADC_2A-7C_n28A | 2 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2120 | 29.0 | IMD2 |  |
|  | n28 | 740 | 5 | 25 | 795 | N/A | N/A |  |
| DC_2A_n7A-n71A | 2 | 1865 | 5 | 25 | 1945 | N/A | N/A |  |
|  | n7 | 2510 | 10 | 50 | 2630 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 645 | 28.7 | IMD2 |  |
|  | 2 | 1890 | 5 | 25 | 1970 | N/A | N/A |  |
|  | n7 | 2520 | 10 | 50 | 2640 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 630 | 1 | IMD5 |  |
| DC_2A-7A_n77ADC_2A-2A-7A_n77ADC_2A-7C_n77ADC_2A-7A-7A_n77ADC_2A-7A_n77(2A)DC_2A-7C_n77(2A)DC_2A-7A-7A_n77(2A) | 2 | N/A | 5 | N/A | 1950 | 8.6 | IMD4 |  |
|  | 7 | 2550 | 5 | 25 | 2670 | N/A | N/A |  |
|  | n77 | 3525 | 10 | 50 | 3525 | N/A | N/A |  |
|  | 2 | 1860 | 5 | 25 | 1940 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2660 | 3.4 | IMD5 |  |
|  | n77 | 4120 | 10 | 50 | 4120 | N/A | N/A |  |
| DC_2A_n7A-n77A | 2 | 1860 | 5 | 25 | 1940 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2660 | 3.4 | IMD5 |  |
|  | n77 | 4120 | 10 | 50 | 4120 | N/A | N/A |  |
|  | 2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n7 | 2525 | 5 | 25 | 2645 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3775 | 4.2 | IMD5 |  |
| DC_2A-7A_n78ADC_2A-2A-7A_n78ADC_2A-7C_n78ADC_2A-7A-7A_n78ADC_2A-7A_n78(2A)DC_2A-7C_n78(2A)DC_2A-7A-7A_n78(2A) | 2 | N/A | 5 | N/A | 1950 | 8.6 | IMD4 |  |
|  | 7 | 2550 | 5 | 25 | 2670 | N/A | N/A |  |
|  | n78 | 3525 | 10 | 50 | 3475 | N/A | N/A |  |
| DC_2A_n7A-n78ADC_2A_n7(2A)-n78ADC_2A_n7A-n78(2A)DC_2A_n7(2A)-n78(2A) | 2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n7 | 2525 | 5 | 25 | 2645 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3775 | 4.2 | IMD5 |  |
| DC_2-8_n2 | 2 | N/A | 5 | N/A | 1940 | 4 | IMD4 |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n2 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
| DC_2A-12A_n5ADC_2A-2A-12A_n5A | 2 | N/A | 5 | N/A | 1980 | 5.9 | IMD5 |  |
|  | 12 | 705 | 5 | 25 | 735 | N/A | N/A |  |
|  | n5 | 840 | 5 | 25 | 885 | N/A | N/A |  |
| DC_2A-12A_n7ADC_2A-12A_n7(2A) | 2 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
| DC_2A-2A-12A_n7A | 12 | N/A | 5 | N/A | 731.5 | 4.5 | IMD5 |  |
|  | n7 | 2502.5 | 5 | 25 | 2622.5 | N/A | N/A |  |
| DC_2A-12A_n41ADC_2A-2A-12A_n41A | 2 | N/A | 5 | N/A | 1952 | 26 | IMD2 |  |
|  | 12 | 708 | 5 | 50 | 738 | N/A | N/A |  |
|  | n41 | 2660 | 10 | 50 | 2660 | N/A | N/A |  |
|  | 2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | 12 | N/A | 5 | N/A | 738 | 28.7 | IMD24 |  |
|  | n41 | 2638 | 10 | 50 | 2638 | N/A | N/A |  |
| DC_2A-12A_n66A | 2 | N/A | N/A | N/A | N/A | N/A | IMD4 |  |
|  | 12 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | n66 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_2A-12A_n77ADC_2A-12A_n77(2A) | 2 | N/A | 5 | N/A | 1960 | 16.5 | IMD39,11 |  |
| DC_2A-2A-12A_n77ADC_2A-2A-12A_n77(2A) | 12 | 707.5 | 5 | 25 | 737.5 | N/A | N/A |  |
|  | n77 | 3375 | 10 | 50 | 3375 | N/A | N/A |  |
| DC_2A_n12A-n77ADC_2A-2A_n12A-n77A | 2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n12 | 707.5 | 5 | 25 | 737.5 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3315 | 16.0 | IMD34,9,11 |  |
| DC_2A-12A_n78ADC_2A-2A-12A_n78ADC_2A-12A_n78(2A) | 2 | N/A | 5 | N/A | 1954 | 16.5 | IMD3 |  |
|  | 12 | 708 | 5 | 25 | 738 | N/A | N/A |  |
|  | n78 | 3370 | 10 | 50 | 3370 | N/A | N/A |  |
| DC_2A_n12A-n78A | 2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n12 | 707.5 | 5 | 25 | 737.5 | N/A | N/A |  |
|  | n78 | 3315 | 10 | 50 | 3315 | 16.0 | IMD3 |  |
| DC_2A-13A_n48ADC_2A-13A_n48B | 2 | N/A | 5 | N/A | 1983.5 | 15.6 | IMD3 |  |
|  | 13 | 784.5 | 5 | 25 | 753.5 | N/A | N/A |  |
|  | n48 | 3555 | 10 | 50 | 3555 | N/A | N/A |  |
| DC_2A-13A_n66ADC_2A-2A-13A_n66A | 2 | N/A | 5 | N/A | 1940 | 6.2 | IMD4 |  |
|  | 13 | 780 | 10 | 50 | 749 | N/A | N/A |  |
|  | n66 | 1750 | 5 | 25 | 2150 | N/A | N/A |  |
| DC_2A-13A_n77A | 2 | N/A | 5 | N/A | 1944 | 16.0 | IMD3 |  |
| DC_2A-13A_n77C | 13 | 783 | 5 | 25 | 752 | N/A | N/A |  |
| DC_2A-2A-13A_n77ADC_2A-2A-13A_n77C | n77 | 3510 | 10 | 50 | 3510 | N/A | N/A |  |
| DC_2A-14A_n77ADC_2A-14A_n77(2A) | 2 | N/A | 5 | N/A | 1954 | 16.5 | IMD3 |  |
| DC_2A-2A-14A_n77ADC_2A-2A-14A_n77(2A) | 14 | 793 | 5 | 25 | 763 | N/A | N/A |  |
|  | n77 | 3540 | 10 | 50 | 3540 | N/A | N/A |  |
| DC_2A_n25A-n66A | 2 | 1855 | 5 | 25 | 1935 | N/A | N/A |  |
|  | n25 | N/A | 5 | N/A | 1935 | 20 | IMD34 |  |
|  | n66 | 1775 | 5 | 25 | 2175 | N/A | N/A |  |
| DC_2A_n38A-n71A | 2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n38 | N/A | 10 | N/A | 2586 | 29.2 | IMD2 |  |
|  | n71 | 686 | 5 | 25 | 640 | N/A | N/A |  |
| DC_2A_n38A-n78A | 2 | 1870 | 5 | 25 | 1950 | N/A | N/A |  |
|  | n38 | 2610 | 10 | 50 | 2610 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3350 | 14.8 | IMD3 |  |
| DC_2A-14A_n66A | 2 | N/A | 5 | N/A | 1954 | 7.2 | IMD4 |  |
|  | 14 | 793 | 5 | 25 | 763 | N/A | N/A |  |
|  | n66 | 1770 | 5 | 25 | 2170 | N/A | N/A |  |
| DC_2A-28A_n66A | 2 | N/A | 5 | N/A | 1980 | 11 | IMD4 |  |
|  | 28 | 730 | 5 | 25 | 785 | N/A | N/A |  |
|  | n66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
| DC_2A-28A_n78A | 2 | 1904 | 5 | 25 | 1984 | 16.5 | IMD3 |  |
|  | 28 | 708 | 5 | 25 | 763 | N/A | N/A |  |
|  | n78 | 3400 | 10 | 50 | 3400 | N/A | N/A |  |
| DC_2A-30A_n77ADC_2A-30A_n77(2A) | 2 | N/A | 5 | N/A | 1986 | 8.6 | IMD411 |  |
| DC_2A-2A-30A_n77A DC_2A-2A-30A_n77(2A) | 30 | 2312 | 5 | 25 | 2357 | N/A | N/A |  |
|  | n77 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | 2 | 1905 | 5 | 25 | 1985 | N/A | N/A |  |
|  | 30 | N/A | 5 | N/A | 2354 | 10.6 | IMD411 |  |
|  | n77 | 3361 | 10 | 50 | 3361 | N/A | N/A |  |
|  | 2 | 1860 | 5 | 25 | 1940 | N/A | N/A |  |
|  | 30 | N/A | 5 | N/A | 2354 | 3.4 | IMD5 |  |
|  | n77 | 3967 | 10 | 50 | 3967 | N/A | N/A |  |
| DC_2A-38A_n78A | 2 | N/A | 5 | N/A | 1932.5 | 16 | IMD39 |  |
|  | 38 | 2617.5 | 5 | 25 | 2617.5 | N/A | N/A |  |
|  | n78 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
| DC_2A_n41A-n71ADC_2A-2A_n41A-n71A | 2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n41 | 2530 | 10 | 50 | 2530 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 630 | 28.7 | IMD2 |  |
|  | 2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2586 | 29.2 | IMD2 |  |
|  | n71 | 686 | 5 | 50 | 640 | N/A | N/A |  |
| DC_2A_n41A-n77A | 2 | 1870 | 5 | 25 | 1950 | N/A | N/A |  |
|  | n41 | 2670 | 10 | 50 | 2670 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3470 | 13.3 | IMD34 |  |
|  | 2 | 1870 | 5 | 25 | 1950 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2640 | 4.3 | IMD55 |  |
|  | n77 | 4125 | 10 | 50 | 4125 | N/A | N/A |  |
| DC_2A_n41A-n78A | 2 | 1870 | 5 | 25 | 1950 | N/A | N/A |  |
|  | n41 | 2610 | 5 | 25 | 2610 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3350 | 14.8 | IMD34 |  |
| DC_2A-46A_n5A5DC_2A-46C_n5A5DC_2A-46D_n5A5DC_2A-46E_n5A5 | 2 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_2A-2A-46A_n5A5DC_2A-2A-46C_n5A5DC_2A-2A-46D_n5A5 | 46 | N/A | N/A | N/A | N/A | N/A | IMD4,IMD5 |  |
|  | n5 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_2A-46A_n66A5DC_2A-46C_n66A5DC_2A-46D_n66A5DC_2A-46E_n66A5 | 2 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 46 | N/A | N/A | N/A | N/A | N/A | IMD3,IMD5 |  |
|  | n66 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_2A-46A_n77A5DC_2A-46A-46A_n77A5 | 2 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 46 | N/A | N/A | N/A | N/A | N/A | IMD2,IMD3 |  |
|  | n77 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_2A-48A_n2ADC_2A-48C_n2ADC_2A-48D_n2ADC_2A-48E_n2A | n2 | 1853 | 5 | 25 | 1933 | N/A | N/A |  |
|  | 48 | 3590 | 20 | 100 | 3590 | N/A | N/A |  |
|  | 2 | N/A | 5 | N/A | 1969 | 12 | IMD4 |  |
| DC_2A-48A_n5A | 2 | N/A | 5 | N/A | 1950 | 16.9 | IMD3 |  |
| DC_2A-48C_n5A | 48 | 3610 | 10 | 50 | 3610 | N/A | N/A |  |
| DC_2A-48D_n5A | n5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
| DC_2A-48E_n5A | 2 | 1890 | 5 | 25 | 1970 | N/A | N/A |  |
|  | 48 | N/A | 5 | N/A | 3570 | 16.2 | IMD3 |  |
|  | n5 | 840 | 5 | 25 | 885 | N/A | N/A |  |
| DC_2A-48A_n66ADC_2A-48C_n66ADC_2A-48D_n66ADC_2A-48E_n66A | 2 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
|  | 48 | N/A | 10 | N/A | 3620 | 29.4 | IMD2 |  |
|  | n66 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 2 | N/A | 5 | N/A | 1960 | 28.3 | IMD2 |  |
|  | 48 | 3695 | 5 | 25 | 3695 | N/A | N/A |  |
|  | n66 | 1735 | 5 | 25 | 2135 | N/A | N/A |  |
| DC_2A_n48A-n66A | 2 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
|  | n48 | N/A | 10 | N/A | 3620 | 29.4 | IMD2 |  |
|  | n66 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 2 | N/A | 5 | N/A | 1980 | 20 | IMD3 |  |
| DC_2A-66A_n2A | 66 | 1730 | 5 | 25 | 2130 | N/A | N/A |  |
| DC_2A-66A-66A_n2A | n2 | 1855 | 5 | 25 | 1935 | N/A | N/A |  |
| DC_2A-66A_n5A | 2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2140 | 7.2 | IMD4 |  |
|  | n5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
| DC_2A-66A_n25A | 2 | N/A | 5 | N/A | 1980 | 20 | IMD3 |  |
|  | 66 | 1730 | 5 | 25 | 2130 | N/A | N/A |  |
|  | n25 | 1855 | 5 | N/A | 1935 | N/A | N/A |  |
| DC_2A-66A_n28A | 2 | N/A | 5 | N/A | 1960 | 11.0 | IMD4 |  |
|  | 66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n28 | 740 | 5 | 25 | 795 | N/A | N/A |  |
| DC_2A-66A_n41ADC_2A-66A_n41CDC_2A-66A_n41(2A) | 2 | N/A | 5 | N/A | 1940 | 9.5 | IMD4 |  |
|  | 66 | 1715 | 5 | 25 | 2115 | N/A | N/A |  |
|  | n41 | 2685 | 10 | 50 | 2685 | N/A | N/A |  |
| DC_2A-66A_n48ADC_2A-66A_n48BDC_2A-66A-66A_n48ADC_2A-66A-66A_n48B | 2 | 1905 | 5 | 25 | 1985 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2155 | 12.1 | IMD4 |  |
|  | n48 | 3560 | 10 | 50 | 3560 | N/A | N/A |  |
|  | 2 | N/A | 5 | N/A | 1960 | 28.3 | IMD5 |  |
|  | 66 | 1735 | 5 | 25 | 2135 | N/A | N/A |  |
|  | n48 | 3695 | 10 | 50 | 3695 | N/A | N/A |  |
| DC_2A-66A_n77A11 | 2 | 1855 | 5 | 25 | 1935 | N/A | N/A |  |
| DC_2A-66A_n77C11DC_2A-66A_n77(2A)11DC_2A-2A-66A_n77A11DC_2A-2A-66A_n77C11DC_2A-2A-66A_n77(2A)DC_2A-66A-66A_n77A11DC_2A-66A-66A_n77C11DC_2A-66A-66A_n77(2A)DC_2A-2A-66A-66A_n77A11DC_2A-2A-66A-66A_n77C11 | 66 | N/A | 5 | N/A | 2115 | 29.2 | IMD29 |  |
|  | n77 | 3970 | 10 | 50 | 3970 | N/A | N/A |  |
|  | 2 | 1885 | 5 | 25 | 1965 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2175 | 4.0 | IMD5 |  |
|  | n77 | 3915 | 10 | 50 | 3915 | N/A | N/A |  |
|  | 2 | N/A | 5 | N/A | 1960 | 32.1 | IMD2 |  |
|  | 66 | 1760 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n77 | 3720 | 10 | 50 | 3720 | N/A | N/A |  |
| DC_2A_n66A-n77A11DC_2A-2A_n66A-n77A11 | 2 | 1855 | 5 | 25 | 1935 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2115 | 29.2 | IMD2 |  |
|  | n77 | 3970 | 10 | 50 | 3970 | N/A | N/A |  |
|  | 2 | 1853 | 5 | 25 | 1933 | N/A | N/A |  |
|  | n66 | 1713 | 5 | 25 | 2113 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3566 | 29.4 | IMD2 |  |
| DC_2A-66A_n78ADC_2A-66A_n78(2A)DC_2A-66A-66A_n78ADC_2A-66A-66A_n78(2A) | 2 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
| DC_2A-2A-66A_n78A | 66 | N/A | 5 | N/A | 2160 | 10.3 | IMD4 |  |
|  | n78 | 3480 | 10 | 50 | 3480 | N/A | N/A |  |
|  | 2 | N/A | 5 | N/A | 1960 | 32.1 | IMD29 |  |
|  | 66 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n78 | 3700 | 10 | 50 | 3700 | N/A | N/A |  |
|  | 2 | N/A | 5 | N/A | 1960 | 2.1 | IMD5 |  |
|  | 66 | 1760 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n78 | 3620 | 10 | 50 | 3620 | N/A | N/A |  |
| DC_2A_n66A-n78ADC_2A_n66(2A)-n78ADC_2A_n66(2A)-n78(2A) | 2 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
|  | n66 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3620 | 29.4 | IMD29 |  |
|  | 2 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2140 | 10.3 | IMD4 |  |
|  | n78 | 3500 | 10 | 50 | 3500 | N/A | N/A |  |
| DC_2A-71A_n7A | 2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
| DC_2A-2A-71A_n7A | 71 | N/A | 5 | N/A | 630 | 28.7 | IMD24 |  |
|  | n7 | 2530 | 10 | 50 | 2650 | N/A | N/A |  |
| DC_2A-71A_n38ADC_2A-2A-71A_n38A | 2 | N/A | 5 | N/A | 1942 | 26 | IMD2 |  |
|  | 71 | 668 | 5 | 25 | 622 | N/A | N/A |  |
|  | n38 | 2610 | 10 | 50 | 2610 | N/A | N/A |  |
| DC_2A-71A_n41ADC_2A-2A-71A_n41A | 2 | N/A | 5 | N/A | 1942 | 26 | IMD2 |  |
|  | 71 | 668 | 5 | 25 | 622 | N/A | N/A |  |
|  | n41 | 2610 | 10 | 50 | 2610 | N/A | N/A |  |
|  | 2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | 71 | N/A | 5 | N/A | 630 | 28.7 | IMD24 |  |
|  | n41 | 2530 | 10 | 50 | 2530 | N/A | N/A |  |
| DC_2A-71A_n77ADC_2A-2A-71A_n77ADC_2A-71A_n77(2A) | 2 | N/A | 5 | N/A | 1954 | 16.5 | IMD39 |  |
|  | 71 | 693 | 5 | 25 | 647 | N/A | N/A |  |
|  | n77 | 3340 | 10 | 50 | 3340 | N/A | N/A |  |
| DC_2A_n71A-n77ADC_2A-2A_n71A-n77ADC_2A_n71A-n77(2A) | 2 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
|  | n71 | 695.5 | 5 | 25 | 649.5 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3305 | 8 | IMD3 |  |
| DC_2A-71A_n78ADC_2A-2A-71A_n78A | 2 | N/A | 5 | N/A | 1954 | 16.5 | IMD3 |  |
|  | 71 | 693 | 5 | 25 | 647 | N/A | N/A |  |
|  | n78 | 3340 | 10 | 50 | 3340 | N/A | N/A |  |
| DC_2A_n71A-n78ADC_2A-2A_n71A-n78A | 2 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
|  | n71 | 695.5 | 5 | 25 | 649.5 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3305 | 8 | IMD3 |  |
| DC_3A_n1A-n28ADC_3C_n1A-n28A | 3 | 1780 | 5 | 25 | 1875 | N/A | N/A |  |
|  | n28 | 710.5 | 5 | 25 | 765.5 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2139 | 11.0 | IMD4 |  |
| DC_3A_n1A-n40A | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 3 | 1735 | 5 | 25 | 1830 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2380 | 8.0 | IMD5 |  |
| DC_3A_n1A-n41A | 3 | 1712.5 | 5 | 25 | 1807.5 | N/A | N/A |  |
|  | n1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2507.5 | 4 | IMD5 |  |
| DC_3A_n1A-n75A | n75 | N/A | 5 | N/A | 1480 | 15.2 | IMD34,19 |  |
| DC_3C_n1A-n75A | n1 | 1960 | 5 | 25 | 2150 | N/A | N/A |  |
|  | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
| DC_3A_n1A-n77A | 3 | 1750 | 5 | 25 | 1845 | N/A | N/A |  |
|  | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3700 | 28.4 | IMD2 |  |
|  | 3 | 1775 | 5 | 25 | 1870 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2140 | 31.0 | IMD2 |  |
|  | n77 | 3915 | 10 | 50 | 3915 | N/A | N/A |  |
| DC_3A_n1A-n78ADC_3C_n1A-n78ADC_3A-3A_n1A-n78A | 3 | 1750 | 5 | 25 | 1845 | N/A | N/A |  |
|  | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3700 | 28.4 | IMD2 |  |
|  | 3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2130 | 3.5 | IMD5 |  |
|  | n78 | 3720 | 10 | 50 | 3720 | N/A | N/A |  |
| DC_3A_n1A-n79A | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n79 | 4950 | 40 | 216 | 4950 | 4.7 | IMD5 |  |
|  | 3 | 1750 | 5 | 25 | 1845 | N/A | N/A |  |
|  | n1 | 1950 | 40 | 216 | 2140 | 3.6 | IMD5 |  |
|  | n79 | 4860 | 5 | 25 | 4860 | N/A | N/A |  |
| DC_(n)3AA-n8A | n8 | 897.5 | 5 | 25 | 942.5 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1837.5 | 4.5 | IMD5 |  |
|  | n3 | 1747.5 | 5 | 25 | 1842.5 | 6.4 | IMD5 |  |
| DC_3A_n3A-n41A | 3 | 1725 | 5 | 25 | 1820 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1865 | 7.2 | IMD4 |  |
|  | n41 | 2657.5 | 10 | 50 | 2657.5 | N/A | N/A |  |
| DC_(n)3AA-n77ADC_(n)3CA-n77ADC_(n)3AA-n77(2A)DC_(n)3CA-n77(2A) | 3 | 1740 | 5 | 25 | 1835 | 31.9 | IMD24 |  |
|  | n3 | N/A | 5 | N/A | 1840 | [28.9] | IMD24 |  |
|  | n77 | 3575 | 10 | 50 | 3575 | N/A | N/A |  |
| DC_(n)3AA-n78ADC_(n)3CA-n78A | 3 | 1740 | 5 | 25 | 1835 | 31.9 | IMD24 |  |
| DC_(n)3AA-n78(2A)DC_(n)3CA-n78(2A) | n3 | N/A | 5 | N/A | 1840 | [28.9] | IMD24 |  |
|  | n78 | 3575 | 10 | 50 | 3575 | N/A | N/A |  |
| DC_3A-5A_n3A | 3 | N/A | 5 | N/A | 1875 | 4 | IMD4 |  |
|  | 5 | 832.5 | 5 | 25 | 877.5 | N/A | N/A |  |
|  | n3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
| DC_3A-5A_n28A | 3 | N/A | 5 | N/A | 1829.5 | 8.7 | IMD4 |  |
|  | 5 | 845 | 5 | 25 | 890 | N/A | N/A |  |
|  | n28 | 705.5 | 5 | 25 | 760.5 | N/A | N/A |  |
| DC_3A-5A_n77ADC_3A-5A_n77(2A)DC_3A-5A_n77(3A) | 3 | N/A | 5 | N/A | 1820 | 17.3 | IMD3 |  |
|  | 5 | 845 | 5 | 25 | 890 | N/A | N/A |  |
|  | n77 | 3510 | 10 | 50 | 3510 | N/A | N/A |  |
| DC_3A-5A_n78ADC_3A-5A_n78(A-C) | 3 | N/A | N/A | N/A | N/A | N/A | IMD3 |  |
|  | 5 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | n78 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_3A_n5A-n78ADC_3C_n5A-n78A | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
|  | n5 | 845 | 5 | 25 | 890 | N/A | N/A |  |
|  | n78 | 3420 | 10 | 52 | 3420 | 16.1 | IMD3 |  |
| DC_3A-5A_n79A | 3 | 1775 | 5 | 25 | 1870 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 885 | 18.5 | IMD3 |  |
|  | n79 | 4435 | 40 | 216 | 4435 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1877.5 | 0.2 | IMD4 |  |
|  | 5 | 842.5 | 5 | 25 | 887.5 | N/A | N/A |  |
|  | n79 | 4420 | 40 | 216 | 4420 | N/A | N/A |  |
| DC_3A-7A_n5A | 3 | 1780 | 10 | 50 | 1875 | N/A | N/A |  |
|  | 7 | N/A | 10 | N/A | 2625 | 30.0 | IMD21 |  |
|  | n5 | 845 | 5 | 25 | 890 | N/A | N/A |  |
| DC_3A-(n)7AADC_3C-(n)7AA | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2647.5 | 6.9 | IMD4 |  |
|  | n7 | 2535 | 10 | 50 | 2655 | 10.2 | IMD4 |  |
| DC_3A-7A_n8A | 3 | 1780 | 5 | 25 | 1875 | N/A | N/A |  |
|  | n8 | 890 | 5 | 25 | 935 | N/A | N/A |  |
|  | 7 | N/A | 10 | N/A | 2670 | 29.0 | IMD2IMD33 |  |
| DC_3A-7A_n26A | 3 | 1780 | 10 | 50 | 1875 | N/A | N/A |  |
| DC_3A-7C_n26A | 7 | N/A | 10 | N/A | 2625 | 30.0 | IMD2 |  |
| DC_3C-7A_n26ADC_3C-7C_n26A | n26 | 845 | 5 | 25 | 890 | N/A | N/A |  |
|  | 3 | 1760 | 5 | 25 | 1855 | N/A | N/A |  |
|  | 7 | 2555 | 10 | N/A | 2675 | 16.9 | IMD319 |  |
|  | n26 | 845 | 5 | 25 | 890 | N/A | N/A |  |
| DC_3A-7A_n28ADC_3A-7C_n28ADC_3C-7A_n28ADC_3C-7C_n28A | 3 | 1712.5 | 5 | 25 | 1807.5 | N/A | N/A |  |
| DC_3A-7A-7A_n28A | n28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | 7 | N/A | 10 | N/A | 2682 | 16.9 | IMD3 |  |
|  | 7 | 2543 | 10 | 50 | 2663 | N/A | N/A |  |
|  | n28 | 710.5 | 5 | 25 | 765.5 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1832.5 | 26.0 | IMD2 |  |
| DC_3A_n8A-n77A | 3 | 1740 | 5 | 25 | 1835 | N/A | N/A |  |
|  | n8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3540 | 16.3 | IMD34 |  |
|  | 3 | 1715 | 5 | 25 | 1810 | N/A | N/A |  |
|  | n77 | 4190 | 10 | 50 | 4190 | N/A | N/A |  |
|  | n8 | N/A | 5 | N/A | 955 | 9.7 | IMD4 |  |
| DC_3A-18A_n3A | 3 | N/A | 5 | N/A | 1814 | 4 | IMD4\|2*fn3-2*fB18\| |  |
|  | 18 | 823 | 5 | 25 | 868 | N/A | N/A |  |
|  | n3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
| DC_3A-18A_n41A | 18 | N/A | 5 | N/A | 865 | 28.9 | IMD2 |  |
|  | 3 | 1765 | 5 | 25 | 1860 | N/A | N/A |  |
|  | n41 | 2630 | 10 | 50 | 2630 | N/A | N/A |  |
|  | 18 | N/A | 5 | N/A | 865 | 17.5 | IMD3 |  |
|  | 3 | 1725 | 5 | 25 | 1820 | N/A | N/A |  |
|  | n41 | 2585 | 10 | 50 | 2585 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1850 | 28.8 | IMD2 |  |
|  | n41 | 2670 | 10 | 50 | 2670 | N/A | N/A |  |
|  | 18 | 820 | 5 | 25 | 865 | MSD | N/A |  |
| DC_3A-18A_n77ADC_3A-18A_n77(2A)DC_3A-18A_n78ADC_3A-18A_n78(2A) | 3 | N/A | 5 | N/A | 1865 | 15.7 | IMD3 |  |
|  | 18 | 820 | 5 | 25 | 865 | N/A | N/A |  |
|  | n77, n78 | 3505 | 10 | 50 | 3505 | N/A | N/A |  |
| DC_3A-19A_n77ADC_3A-19A_n78A | 3 | N/A | 5 | N/A | 1850 | 17.3 | IMD3 |  |
|  | 19 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | n77, n78 | 3520 | 10 | 50 | 3520 | N/A | N/A |  |
| DC_3A_n7A-n28A | 3 | 1747 | 5 | 25 | 1842 | N/A | N/A |  |
| DC_3C_n7A-n28A | n7 | 2543 | 5 | 25 | 2663 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 796.0 | 20.0 | IMD2 |  |
|  | 3 | 1712.5 | 5 | 25 | 1807.5 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2682 | 17.0 | IMD3 |  |
|  | n28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
| DC_3A-7A_n40A | 3 | N/A | 5 | N/A | 1866.6 | 3.4 | IMD5 |  |
| DC_3A-7A-7A_n40A | 7 | 2530 | 5 | 25 | 2650 | N/A | N/A |  |
|  | n40 | 2310 | 10 | 50 | 2310 | N/A | N/A |  |
| DC_3A-7A_n77A | 3 | N/A | 5 | N/A | 1820 | 17.6 | IMD3 |  |
| DC_3A-7A_n77(2A)DC_3A-7A_n77(3A) | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
| DC_3A-7A-7A_n77(2A) | n77 | 3310 | 10 | 50 | 3310 | N/A | N/A |  |
| DC_3A-7A-7A_n77(3A) | 3 | N/A | 5 | N/A | 1820 | 8.6 | IMD4 |  |
|  | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n77 | 3475 | 10 | 50 | 3475 | N/A | N/A |  |
|  | 3 | 1715 | 5 | 25 | 1810 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2670 | 5.2 | IMD5 |  |
|  | n77 | 4190 | 10 | 50 | 4190 | N/A | N/A |  |
| DC_3A-7A_n78ADC_3C-7A_n78A DC_3C-7C_n78ADC_3A-3A-7A_n78ADC_3A-3A-7A-7A_n78ADC_3A-7A_SUL_n78A-n80ADC_3C-7A_SUL_n78A-n80ADC_3A-7A_n78(2A)DC_3C-7A_n78(2A)DC_3A-7C_n78(2A)DC_3C-7C_n78(2A)DC_3A-7A_n78CDC_3A-7A_n78(A-C)DC_3A-7A-7A_n78C | 3 | N/A | 5 | N/A | 1820 | 17.6 | IMD3 |  |
| DC_3A-7A-7A_n78(A-C) | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n78 | 3310 | 10 | 50 | 3310 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1820 | 8.6 | IMD4 |  |
|  | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n78 | 3475 | 10 | 50 | 3475 | N/A | N/A |  |
| DC_3A-7A_n79A | 3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
| DC_3A-3A-7A_n79A | n79 | 4440 | 10 | 50 | 4440 | N/A | N/A |  |
| DC_3A-7A-7A_n79A | 7 | N/A | 5 | N/A | 2670 | 30.2 | IMD2 |  |
| DC_3A-3A-7A-7A_n79A | 3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
|  | n79 | 4440 | 10 | 50 | 4440 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2640 | 5.0 | IMD5 |  |
|  | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n79 | 4420 | 10 | 50 | 4420 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1855 | 29.4 | IMD2 |  |
|  | 7 | 2550 | 5 | 25 | 2670 | N/A | N/A |  |
|  | n79 | 4745 | 10 | 50 | 4745 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1840 | 4.8 | IMD5 |  |
| DC_3A-7A_n105A | 3 | N/A | 5 | N/A | 1875 | 16.5 | IMD2 |  |
|  | 7 | 2550 | 5 | 25 | 2670 | N/A | N/A |  |
|  | n105 | 675 | 5 | 25 | 624 | N/A | N/A |  |
| DC_3A-8A_n7A | 3 | 1735 | 5 | 25 | 1830 | N/A | N/A |  |
|  | n7 | 2530 | 10 | 50 | 2650 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 940 | 18.0 | IMD3 |  |
| DC_3A-8A_n40A | 3 | N/A | 5 | N/A | 1874 | 4 | IMD5 |  |
| DC_3C-8A_n40A | 8 | 912 | 5 | 25 | 957 | N/A | N/A |  |
|  | n40 | 2305 | 10 | 50 | 2305 | N/A | N/A |  |
| DC_3A-8A_n41A | 3 | 1725 | 5 | 25 | 1820 | N/A | N/A |  |
| DC_3A-3A-8A_n41A | 8 | N/A | 5 | N/A | 945 | 26.0 | IMD215 |  |
|  | n41 | 2670 | 10 | 50 | 2670 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1807.5 | 25 | IMD2x |  |
|  | 8 | 882.5 | 5 | 25 | 927.5 | N/A | N/A |  |
|  | n41 | 2685 | 10 | 50 | 2685 | N/A | N/A |  |
| DC_3A_n8A-n41A | 3 | 1722.5 | 5 | 25 | 1817.5 | N/A | N/A |  |
|  | n8 | 887.5 | 5 | 25 | 932.5 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2610 | 28.0 | IMD216 |  |
|  | 3 | 1725 | 5 | 25 | 1820 | N/A | N/A |  |
|  | n8 | N/A | 5 | N/A | 945 | 26.0 | IMD216 |  |
|  | n41 | 2516 | 10 | 50 | 2516 | N/A | N/A |  |
| DC_3A-8A_n71A | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
| DC_3C-8A_n71A | 8 | N/A | 5 | N/A | 932 | 5 | IMD5 |  |
|  | n71 | 665.5 | 5 | 25 | 619.5 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1870 | 5 | IMD5 |  |
|  | 8 | 890 | 5 | 25 | 935 | N/A | N/A |  |
|  | n71 | 690 | 5 | 25 | 644 | N/A | N/A |  |
| DC_3A-8A_n77ADC_3A-8A_n77(2A)DC_3A-8A_n77(3A)DC_3C-8A_n77ADC_3C-8A_n77(2A) | 3 | 1715 | 5 | 25 | 1810 | N/A | N/A |  |
| DC_3A-8B_n77A | n77 | 4190 | 10 | 50 | 4190 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 955 | 9.7 | IMD4 |  |
|  | 3 | N/A | 5 | N/A | 1820 | 16.5 | IMD3 |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n77 | 3640 | 10 | 50 | 3640 | N/A | N/A |  |
| DC_3A-8A_n78ADC_3A-3A-8A_n78A | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
| DC_3A-8B_n78ADC_3A-3A-8B_n78A DC_3A-8A_n78(2A)DC_3C-8A_n78(2A) | n78 | 3640 | 10 | 50 | 3640 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1820 | 16.5 | IMD319 |  |
| DC_3A_n8A-n78A | 3 | 1740 | 5 | 25 | 1835 | N/A | N/A |  |
|  | n8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3540 | 16.3 | IMD3 |  |
| DC_3A-8A_n79A | 3 | 1755 | 5 | 25 | 1850 | N/A | N/A |  |
|  | n79 | 4465 | 40 | 216 | 4465 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 955 | 15.3 | IMD3 |  |
|  | 3 | N/A | 5 | N/A | 1850 | 8.8 | IMD4 |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n79 | 4580 | 40 | 216 | 4580 | N/A | N/A |  |
| DC_3A_n7A-n78ADC_3A_n7B-n78ADC_3C_n7A-n78ADC_3C_n7B-n78A | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
| DC_3A_n7A-n78(2A) | n7 | 2560 | 5 | 25 | 2680 | N/A | N/A |  |
| DC_3C_n7A-n78(2A) | n78 | N/A | 10 | N/A | 3390 | 16.1 | IMD3 |  |
| DC_3A-11A_n77ADC_3A-11A_n77(2A) | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n77 | 3675 | 10 | 50 | 3675 | N/A | N/A |  |
|  | 11 | N/A | 5 | N/A | 1491 | 8.8 | IMD4 |  |
|  | 11 | 1435.4 | 5 | 25 | 1483.4 | N/A | N/A |  |
|  | n77 | 3905 | 10 | 50 | 3905 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1848 | 3.4 | IMD57 |  |
| DC_3A-11A_n79A | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | 11 | N/A | 5 | 25 | N/A | 25.1 | IMD3 |  |
|  | n79 | 4920 | 40 | 216 | 4920 | N/A | N/A |  |
| DC_3A-19A_n79A | 3 | 1775 | 5 | 25 | 1870 | N/A | N/A |  |
|  | 19 | N/A | 5 | N/A | 885 | 18.5 | IMD3 |  |
|  | n79 | 4435 | 40 | 216 | 4435 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1877.5 | 5.5 | IMD4 |  |
|  | 19 | 842.5 | 5 | 25 | 887.5 | N/A | N/A |  |
|  | n79 | 4420 | 40 | 216 | 4420 | N/A | N/A |  |
| DC_3A-20A_n3A | 3 | N/A | 5 | N/A | 1870 | 4 | IMD4 |  |
|  | 20 | 835 | 5 | 25 | 794 | N/A | N/A |  |
|  | n3 | 1765 | 5 | 25 | 1860 | N/A | N/A |  |
| DC_3A-20A_n7ADC_3C-20A_n7A | 3 | 1737 | 5 | 25 | 1832 | N/A | N/A |  |
|  | 20 | N/A | 10 | N/A | 806 | 10.5 | IMD2 |  |
|  | n7 | 2543 | 10 | 50 | 2663 | N/A | N/A |  |
| DC_3A-20A_n8A | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | 20 | N/A | 5 | N/A | 810 | 27 | IMD2 |  |
|  | 3 | N/A | 5 | N/A | 1860 | 14.5 | IMD4 |  |
|  | n8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | 20 | 840 | 5 | 25 | 799 | N/A | N/A |  |
| DC_3A-20A_n28ADC_3C-20A_n28A | 20 | 852 | 5 | 25 | 811 | N/A | N/A |  |
|  | n28 | 728 | 5 | 25 | 783 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1828 | 9.4 | IMD4 |  |
| DC_3A-20A_n38A | 3 | 1779 | 5 | 25 | 1874 | N/A | N/A |  |
|  | 20 | N/A | 10 | N/A | 811 | 26.0 | IMD21 |  |
|  | n38 | 2590 | 10 | 50 | 2590 | N/A | N/A |  |
| DC_3A-20A_n41ADC_3C-20A_n41ADC_3A-3A-20A-n41A | 3 | N/A | 5 | N/A | 1839 | 26.0 | IMD2 |  |
|  | n41 | 2680 | 10 | 50 | 2680 | N/A | N/A |  |
|  | 20 | 841 | 10 | 50 | 800 | N/A | N/A |  |
|  | 3 | 1779 | 5 | 25 | 1874 | N/A | N/A |  |
|  | n41 | 2590 | 10 | 50 | 2590 | N/A | N/A |  |
|  | 20 | N/A | 10 | N/A | 811 | 26.0 | IMD2 |  |
|  | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
|  | n41 | 2660 | 10 | 50 | 2660 | N/A | N/A |  |
|  | 20 | N/A | 5 | N/A | 800 | 12.5 | IMD3 |  |
| DC_3_n20-n67 | 3 | 1765 | 5 | 25 | 1860 | N/A | N/A |  |
|  | n20 | 837 | 5 | 25 | 796 | N/A | N/A |  |
|  | n67 | N/A | 5 | N/A | 746 | 10.1 | IMD4 |  |
| DC_3A_20A_SUL_n78A-n80ADC_3C_20A_SUL_n78A-n80A | 3 | N/A | 5 | N/A | 1820 | 17.3 | IMD3 |  |
|  | 20 | 845 | 5 | 25 | 804 | N/A | N/A |  |
|  | n78 | 3510 | 10 | 50 | 3510 | N/A | N/A |  |
| DC_3A_n20A-n78ADC_3A-3A_n20A-n78A | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
|  | n20 | 845 | 5 | 25 | 804 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3420 | 16.1 | IMD3 |  |
| DC_3A-20A_n78ADC_3C-20A_n78ADC_3A-20A_n78(2A) | 3 | N/A | 5 | N/A | 1820 | 17.3 | IMD3 |  |
|  | 20 | 845 | 5 | 25 | 804 | N/A | N/A |  |
|  | n78 | 3510 | 10 | 50 | 3510 | N/A | N/A |  |
| DC_3A-21A_n77ADC_3A-21A_n78A | 3 | 1767.5 | 5 | 25 | 1862.5 | N/A | N/A |  |
|  | 21 | N/A | 5 | N/A | 1507.5 | 8.8 | IMD4 |  |
|  | n77, n78 | 3795 | 10 | 50 | 3795 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1862.5 | 30.8 | IMD2 |  |
|  | 21 | 1459.5 | 5 | 25 | 1507.5 | N/A | N/A |  |
|  | n77, n78 | 3322 | 10 | 50 | 3322 | N/A | N/A |  |
| DC_3A-21A_n77A | 3 | N/A | 5 | N/A | 1866.6 | 3.4 | IMD5 |  |
|  | 21 | 1450.4 | 5 | 25 | 1498.4 | N/A | N/A |  |
|  | n77 | 3935 | 10 | 50 | 3935 | N/A | N/A |  |
| DC_3A-21A_n79A | 3 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 21 | N/A | N/A | N/A | N/A | N/A | IMD3 |  |
|  | n79 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1869.2 | 17.8 | IMD3 |  |
|  | 21 | 1450.4 | 5 | 25 | 1498.4 | N/A | N/A |  |
|  | n79 | 4770 | 40 | 216 | 4770 | N/A | N/A |  |
| DC_3A-26A_n78ADC_3C-26A_n78A | 3 | N/A | 5 | N/A | 1862 | 15.7 | IMD3 |  |
|  | 26 | 839 | 5 | 25 | 884 | N/A | N/A |  |
|  | n78 | 3540 | 10 | 50 | 3540 | N/A | N/A |  |
| DC_3A-28A_n1ADC_3C-28A_n1A | 3 | N/A | 5 | N/A | 1820 | 4 | IMD5 |  |
|  | 28 | 710 | 5 | 25 | 765 | N/A | N/A |  |
|  | n1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
| DC_3A-28A_n5ADC_3C-28A_n5A | 3 | N/A | 5 | N/A | 1830 | 8.7 | IMD4 |  |
|  | 28 | 705 | 5 | 25 | 760 | N/A | N/A |  |
|  | n5 | 845 | 5 | 25 | 890 | N/A | N/A |  |
|  | 3 | 1750 | 5 | 25 | 1845 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 785 | 9.4 | IMD4 |  |
|  | n5 | 845 | 5 | 25 | 890 | N/A | N/A |  |
| DC_3A-28A_n7ADC_3C-28A_n7ADC_3A-3A-28A_n7ADC_3A-28A_n7BDC_3C-28A_n7BDC_3A-3A-28A_n7B | 3 | N/A | 5 | N/A | 1832.5 | 26.0 | IMD2 |  |
|  | 28 | 710.5 | 5 | 25 | 765.5 | N/A | N/A |  |
|  | n7 | 2543 | 10 | 50 | 2663 | N/A | N/A |  |
|  | 3 | 1747 | 5 | 25 | 1842 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 796.0 | 20.0 | IMD2 |  |
|  | n7 | 2543 | 5 | 25 | 2663 | N/A | N/A |  |
| DC_3A-28A_n77ADC_3C-28A_n77(2A)DC_3A-28C_n77(2A)DC_3C-28C_n77(2A) | 3 | 1712.5 | 5 | 25 | 1807.5 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 770 | 15.3 | IMD3 |  |
|  | n77 | 4195 | 10 | 50 | 4195 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1850 | 17.0 | IMD3 |  |
|  | 28 | 735 | 5 | 25 | 790 | N/A | N/A |  |
|  | n77 | 3320 | 10 | 50 | 3320 | N/A | N/A |  |
| DC_3A_n28A-n75ADC_3C_n28A-n75A | 3 | 1780 | 5 | 25 | 1875 | N/A | N/A |  |
|  | n28 | 708 | 5 | 25 | 763 | N/A | N/A |  |
|  | n75 | N/A | - | N/A | 1436 | 3.3 | IMD5 |  |
| DC_3A_n28A-n77ADC_3C_n28A-n77ADC_3C_n28A-n77(2A) | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n28 | 733 | 5 | 25 | 788 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 4173 | 15.9 | IMD3 |  |
|  | 3 | 1712.5 | 5 | 25 | 1807.5 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 770 | 15.3 | IMD3 |  |
|  | n77 | 4195 | 10 | 50 | 4195 | N/A | N/A |  |
| DC_3A-28A_n38A | 3 | N/A | 5 | N/A | 1870 | 26.0 | IMD2 |  |
|  | 28 | 710 | 5 | 25 | 765 | N/A | N/A |  |
|  | n38 | 2580 | 5 | 25 | 2580 | N/A | N/A |  |
|  | 3 | 1780 | 5 | 25 | 1875 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 800 | 20.0 | IMD21 |  |
|  | n38 | 2580 | 5 | 25 | 2580 | N/A | N/A |  |
| DC_3A-28A_n41A | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n41 | 2510 | 10 | 50 | 2510 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 790 | 24.5 | IMD21 |  |
|  | 3 | N/A | 5 | N/A | 1832.5 | 26.0 | IMD2 |  |
|  | n41 | 2543 | 10 | 50 | 2543 | N/A | N/A |  |
|  | 28 | 710.5 | 5 | 25 | 765.5 | N/A | N/A |  |
| DC_3A_n28A-n41A | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 790 | 24.61 | IMD2 |  |
|  | n41 | 2510 | 10 | 50 | 2510 | N/A | N/A |  |
|  | 3 | 1780 | 5 | 25 | 1875 | N/A | N/A |  |
|  | n28 | 738 | 5 | 25 | 793 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2518 | 25.4 | IMD2 |  |
|  | 3 | 1715 | 5 | 25 | 1810 | N/A | N/A |  |
|  | n28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2687 | 13.9 | IMD3 |  |
| DC_3A_n26A-n78A | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
| DC_3C_n26A-n78A | n26 | 839 | 5 | 25 | 884 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3408 | 16.1 | IMD34 |  |
| DC_3A-28A_n78ADC_3C-28A_n78ADC_3A-3A-28A_n78A | 3 | N/A | 5 | N/A | 1870 | 17.3 | IMD3 |  |
|  | 28 | 740 | 5 | 25 | 760 | N/A | N/A |  |
|  | n78 | 3350 | 10 | 25 | 3350 | N/A | N/A |  |
| DC_3A-28A_n79A | 3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 780 | 10.3 | IMD4 |  |
|  | n79 | 4530 | 40 | 216 | 4530 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1870 | 5.7 | IMD5 |  |
|  | 28 | 725 | 5 | 25 | 780 | N/A | N/A |  |
|  | n79 | 4770 | 40 | 216 | 4770 | N/A | N/A |  |
| DC_3A_n28A-n78ADC_3C_n28A-n78A | 3 | 1750 | 5 | 25 | 1845 | N/A | N/A |  |
|  | n28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3764 | 4.5 | IMD5 |  |
| DC_3A_n28A-n79A | 3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 780 | 10.3 | IMD4 |  |
|  | n79 | 4530 | 40 | 216 | 4530 | N/A | N/A |  |
|  | 3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
|  | n28 | 725 | 5 | 25 | 780 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4585 | 9.4 | IMD44 |  |
| DC_3A-32A_n41A | 3 | 1780 | 5 | 25 | 1875 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1480 | 10.4 | IMD4 |  |
|  | n41 | 2520 | 10 | 50 | 2520 | N/A | N/A |  |
| DC_3A_n40A-n71A | 3 | 1745 | 5 | 25 | 1840 | N/A | N/A |  |
| DC_3C_n40A-n71A | n40 | 2380 | 10 | 50 | 2380 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 635 | 26.0 | IMD2 |  |
|  | 3 | 1777.5 | 5 | 25 | 1872.5 | N/A | N/A |  |
|  | n40 | 2350 | 10 | 50 | 2350 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 632.5 | 4.5 | IMD5 |  |
|  | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2388 | 26.0 | IMD2 |  |
|  | n71 | 668 | 5 | 25 | 622 | N/A | N/A |  |
| DC_3A_n40A-n77A | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
| DC_3A_n40A-n77(2A) | n40 | 2350 | 10 | 50 | 2350 | N/A | N/A |  |
| DC_3C_n40A-n77A | n77 | N/A | 10 | N/A | 4070 | 30.3 | IMD2 |  |
|  | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
|  | n40 | 2360 | 10 | 50 | 2360 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3620 | 4.8 | IMD5 |  |
|  | 3 | 1745 | 5 | 25 | 1840 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2355 | 29,2 | IMD2 |  |
|  | n77 | 4100 | 10 | 50 | 4100 | N/A | N/A |  |
|  | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2360 | 4.4 | IMD5 |  |
|  | n77 | 3760 | 10 | 50 | 3760 | N/A | N/A |  |
| DC_3A_SUL_n77A-n84A | 3 | 1782.5 | 5 | 25 | 1877.5 | N/A | N/A |  |
|  | n84 | 1922.5 | 5 | 25 | N/A | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3425 | 13.0 | IMD4 |  |
| DC_3A_n40A-n78A | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
| DC_3A_n40A-n78C | n40 | 2360 | 10 | 50 | 2360 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3620 | 4.8 | IMD5 |  |
|  | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2360 | 4.4 | IMD5 |  |
|  | n78 | 3760 | 10 | 50 | 3760 | N/A | N/A |  |
| DC_3A_n40A-n79A | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n40 | 2330 | 10 | 50 | 2330 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4550 | 4.7 | IMD5 |  |
|  | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2330 | 3.2 | IMD5 |  |
|  | n79 | 4550 | 40 | 216 | 4550 | N/A | N/A |  |
| DC_3_n40-n105 | 3 | 1745 | 5 | 25 | 1840 | N/A | N/A |  |
|  | n40 | 2380 | 10 | 50 | 2380 | N/A | N/A |  |
|  | n105 | N/A | 5 | N/A | 635 | 26.0 | IMD2 |  |
|  | 3 | 1777.5 | 5 | 25 | 1872.5 | N/A | N/A |  |
|  | n40 | 2350 | 10 | 50 | 2350 | N/A | N/A |  |
|  | n105 | N/A | 5 | N/A | 632.5 | 4.5 | IMD5 |  |
|  | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2388 | 26.0 | IMD2 |  |
|  | n105 | 668 | 5 | 25 | 617 | N/A | N/A |  |
| DC_3A_n41A-n79A | 3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
|  | n41 | 2670 | 10 | 50 | 2670 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4440 | 30.8 | IMD24 |  |
| DC_3A-42A_n1ADC_3A-42C_n1A | 3 | 1782.5 | 5 | 25 | 1877.5 | N/A | N/A |  |
|  | 42 | N/A | 5 | N/A | 3425 | 13.0 | IMD4 |  |
|  | n1 | 1922.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
| DC_3A_n71A-n77A | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
| DC_3C_n71A-n77A | n71 | 680 | 5 | 25 | 634 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 4140 | 15.9 | IMD31 |  |
|  | 3 | 1747 | 5 | 25 | 1842 | N/A | N/A |  |
|  | n71 | 680 | 5 | 25 | 634 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3787 | 10.1 | IMD4 |  |
|  | 3 | 1748 | 5 | 25 | 1843 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 632 | 15.3 | IMD3 |  |
|  | n77 | 4128 | 10 | 50 | 4128 | N/A | N/A |  |
| DC_3A_n75A-n78ADC_3C_n75A-n78ADC_3A_n75A-n78(2A) | 3 | 1782.5 | 5 | 25 | 1877.5 | N/A | N/A |  |
|  | n78 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | n75 | N/A | - | N/A | 1514.5 | 10.0 | IMD2 |  |
| DC_3A_n78A-n79A | 3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
| DC_3A-3A_n78A-n79A | n78 | 3340 | 10 | 50 | 3340 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4910 | 16.3 | IMD3 |  |
|  | 3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
|  | n79 | 4510 | 40 | 216 | 4510 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3710 | 4.2 | IMD5 |  |
| DC_3A_SUL_n78A-n82A | 3 | N/A | 5 | N/A | 1870 | 4 | IMD4 |  |
|  | n82 | 840 | 5 | 25 | N/A | N/A | N/A |  |
| DC_3A_SUL_n78A-n84A | 3 | 1782.5 | 5 | 25 | 1877.5 | N/A | N/A |  |
|  | n84 | 1922.5 | 5 | 25 | N/A | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3425 | 13.0 | IMD4 |  |
| DC_3A-32A_n1A | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
| DC_3C-32A_n1A | 32 | N/A | 5 | N/A | 1480 | 15.2 | IMD34, 19 |  |
|  | n1 | 1960 | 5 | 25 | 2150 | N/A | N/A |  |
| DC_3A-32A_n7A | 3 | 1775 | 5 | 25 | 1870 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1470 | 10.5 | IMD4 |  |
|  | n7 | 2510 | 10 | 50 | 2630 | N/A | N/A |  |
| DC_3A-32A_n78ADC_3C-32A_n78ADC_3A-32A_n78CDC_3A-32A_n78(2A) | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1470 | 4.9 | IMD4 |  |
|  | n78 | 3720 | 10 | 50 | 3720 | N/A | N/A |  |
|  | 3 | 1775 | 5 | 25 | 1870 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1475 | 0 | IMD5 |  |
|  | n78 | 3400 | 10 | 50 | 3400 | N/A | N/A |  |
| DC_3A-38A_n28ADC_3C-38A_n28A | 38 | 2575 | 5 | 25 | 2575 | N/A | N/A |  |
|  | n28 | 725 | 5 | 25 | 780 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1850 | 26 | IMD2 |  |
| DC_3A-38A_n78ADC_3C-38A_n78A | 3 | N/A | 5 | N/A | 1830 | 16.4 | IMD35 |  |
|  | 38 | 2615 | 5 | 25 | 2615 | N/A | N/A |  |
|  | n78 | 3400 | 10 | 50 | 3400 | N/A | N/A |  |
| DC_3A-40A_n1ADC_3A-40C_n1A | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 3 | 1735 | 5 | 25 | 1830 | N/A | N/A |  |
|  | 40 | N/A | 5 | N/A | 2380 | 8.0 | IMD5 |  |
| DC_3A-40A_n77ADC_3A-40C_n77A | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | 40 | 2310 | 5 | 25 | 2310 | 29.4 | IMD2 |  |
|  | n77 | 4030 | 10 | 50 | 4030 | N/A | N/A |  |
|  | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | 40 | 2350 | 5 | 25 | 2350 | 5.3 | IMD5 |  |
|  | n77 | 3755 | 10 | 50 | 3755 | N/A | N/A |  |
|  | 3 | 1725 | 5 | 25 | 1820 | 29.9 | IMD29 |  |
|  | 40 | 2310 | 5 | 25 | 2310 | N/A | N/A |  |
|  | n77 | 4130 | 10 | 50 | 4130 | N/A | N/A |  |
| DC_3A-40A_n78ADC_3A-40C_n78A | 3 | N/A | 5 | N/A | 1870 | 9.1 | IMD4 |  |
|  | 40 | 2390 | 5 | 25 | 2390 | N/A | N/A |  |
|  | n78 | 3325 | 10 | 50 | 3325 | N/A | N/A |  |
|  | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | 40 | N/A | 5 | N/A | 2360 | 4.4 | IMD5 |  |
|  | n78 | 3760 | 10 | 50 | 3760 | N/A | N/A |  |
| DC_3A-41A_n1ADC_3A-41C_n1ADC_3A-3A-41A_n1ADC_3A-3A-41C_n1A | n1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | 3 | 1712.5 | 5 | 25 | 1807.5 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2507.5 | 5.0 | IMD5 |  |
| DC_3A-41A_n3ADC_3A-41C_n3A | 3 | N/A | 5 | N/A | 1865 | 8.2 | IMD4\|2*fB41-2*fn3\| |  |
|  | 41 | 2657.5 | 5 | 25 | 2657.5 | N/A | N/A |  |
|  | n3 | 1725 | 5 | 25 | 1820 | N/A | N/A |  |
| DC_3A-41A_n28ADC_3A-41C_n28A | 41 | 2543 | 10 | 50 | 2543 | N/A | N/A |  |
|  | n28 | 710.5 | 5 | 25 | 765.5 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1832.5 | 26 | IMD2 |  |
|  | 3 | 1780 | 5 | 25 | 1875 | N/A | N/A |  |
|  | n28 | 738 | 5 | 25 | 793 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2518 | 27.4 | IMD2 |  |
|  | 3 | 1715 | 5 | 25 | 1810 | N/A | N/A |  |
|  | n28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2687 | 15.9 | IMD3 |  |
| DC_3A-41A_n77ADC_3A-41C_n77ADC_3A-41A_n77(2A)DC_3A-41C_n77(2A)DC_3A_n41A-n77ADC_3A_n41A-n77(2A) | 3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n77 | 3900 | 10 | 50 | 3900 | N/A | N/A |  |
|  | 41/n41 | N/A | 10 | N/A | 2640 | 4.8 | IMD5 |  |
|  | 41/n41 | 2620 | 10 | 50 | 2620 | N/A | N/A |  |
|  | n77 | 3400 | 10 | 50 | 3400 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1840 | 14.9 | IMD3 |  |
| DC_3A-41A_n78ADC_3A-41C_n78ADC_3A-41A_n78(2A)DC_3A-41C_n78(2A) | 41 | 2620 | 5 | 25 | 2620 | N/A | N/A |  |
|  | n78 | 3400 | 10 | 50 | 3400 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1840 | 16.4 | IMD3 |  |
| DC_3A_n41A-n78ADC_3A_n41A-n78(2A) | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
|  | n41 | 2560 | 10 | 50 | 2560 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3390 | 16.4 | IMD3 |  |
| DC_3A-41A_n79A | 3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
|  | n79 | 4440 | 40 | 216 | 4440 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2670 | 30.2 | IMD2 |  |
|  | 41 | 2570 | 5 | 25 | 2570 | N/A | N/A |  |
|  | n79 | 4420 | 40 | 216 | 4420 | N/A | N/A |  |
|  | 3 | N/A | 5 | N/A | 1850 | 29.4 | IMD2 |  |
| DC_3A_n71A-n78A | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
|  | n71 | 666 | 5 | 25 | 620 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3728 | 13.0 | IMD4 |  |
|  | 3 | 1715 | 5 | 25 | 1810 | N/A | N/A |  |
|  | n71 | 685 | 5 | 25 | 639 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3775 | 3.8 | IMD5 |  |
| DC_3_n78-n105 | 3 | 1715 | 5 | 25 | 1810 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3725 | 13 | IMD44 |  |
|  | n105 | 670 | 5 | 25 | 619 | N/A | N/A |  |
| DC_4A-5A_n78A | 4 | N/A | 5 | N/A | 2122 | 18.1 | IMD3 |  |
|  | 5 | 829 | 5 | 25 | 874 | N/A | N/A |  |
|  | n78 | 3780 | 10 | 50 | 3780 | N/A | N/A |  |
| DC_4A-7A_n28A | 4 | 1715 | 5 | 25 | 2115 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2685 | 18.0 | IMD3 |  |
|  | n28 | 745 | 5 | 25 | 800 | N/A | N/A |  |
| DC_4A-7A_n78A | 4 | N/A | 5 | N/A | 2150 | 8.7 | IMD4 |  |
|  | 7 | 2550 | 5 | 25 | 2670 | N/A | N/A |  |
|  | n78 | 3625 | 10 | 50 | 3625 | N/A | N/A |  |
| DC_5A_n1A-n78A | 5 | 829 | 5 | 25 | 874 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2122 | 18.1 | IMD3 |  |
|  | n78 | 3780 | 10 | 50 | 3780 | N/A | N/A |  |
|  | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3610 | 15.7 | IMD3 |  |
| DC_5A_n1A-n28A | 5 | 829 | 5 | 25 | 874 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2123 | 4 | IMD5 |  |
|  | n28 | 738 | 5 | 25 | 793 | N/A | N/A |  |
| DC_5A_n2A-n7A | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n2 | 1855 | 5 | 25 | 1935 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2685 | 30.0 | IMD2 |  |
| DC_5A_n2A-n41A | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n2 | 1855 | 10 | 50 | 1935 | N/A | N/A |  |
|  | n41 | 2685 | 10 | 50 | 2685 | 30.0 | IMD2 |  |
| DC_5A_n2A-n66A | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n66 | 1740 | 5 | 25 | 2140 | 7.2 | IMD4 |  |
| DC_5A_n2A-n77A11 | n2 | N/A | 5 | N/A | 1987 | 16.5 | IMD3 |  |
|  | 5 | 846.5 | 5 | 25 | 891.5 | N/A | N/A |  |
|  | n77 | 3680 | 10 | 50 | 3680 | N/A | N/A |  |
| DC_5A_n3A-n28A | 5 | 845 | 5 | 25 | 890 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1829.5 | 8.7 | IMD4 |  |
|  | n28 | 705.5 | 5 | 25 | 760.5 | N/A | N/A |  |
|  | 5 | 827 | 5 | 25 | 872 | N/A | N/A |  |
|  | n3 | 1713 | 5 | 25 | 1808 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 768 | 9.4 | IMD4 |  |
| DC_5A_n5A-n77A11 | 5 | 834 | 5 | 25 | 879 | N/A | N/A |  |
|  | n5 | N/A | 5 | N/A | 889 | 8.3 | IMD4 |  |
|  | n77 | 3391 | 10 | 50 | 3391 | N/A | N/A |  |
|  | 5 | 826.5 | 5 | 25 | 871.5 | N/A | N/A |  |
|  | n5 | N/A | 5 | N/A | 882 | 5.5 | IMD5 |  |
|  | n77 | 4188 | 10 | 50 | 4188 | N/A | N/A |  |
| DC_5A-7A_n7A | 5 | N/A | 5 | N/A | 879 | 12 | IMD34 |  |
|  | 7 | 2527 | 10 | 50 | 2647 | N/A | N/A |  |
|  | n7 | 2547 | 10 | 50 | 2667 | N/A | N/A |  |
| DC_5A_n2A-n78A | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n2 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3540 | 16.0 | IMD3 |  |
|  | 5 | 846.5 | 5 | 25 | 891.5 | N/A | N/A |  |
|  | n2 | N/A | 5 | N/A | 1987 | 16.5 | IMD3 |  |
|  | n78 | 3680 | 10 | 25 | 3680 | N/A | N/A |  |
| DC_5A_n3A-n78A | 5 | 839 | 5 | 25 | 884 | N/A | N/A |  |
|  | n3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3408 | 16.1 | IMD34 |  |
|  | 5 | 839 | 5 | 25 | 884 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1862 | 15.7 | IMD3 |  |
|  | n78 | 3540 | 10 | 50 | 3540 | N/A | N/A |  |
| DC_5A-7A_n1ADC_5A-7A-7A_n1A | 5 | N/A | 5 | N/A | 880 | 1.0 | IMD5 |  |
|  | 7 | 2512 | 10 | 50 | 2632 | N/A | N/A |  |
|  | n1 | 1968 | 5 | 25 | 2158 | N/A | N/A |  |
| DC_5A-7A_n3A | 5 | 845 | 5 | 25 | 890 | N/A | N/A |  |
|  | 7 | N/A | 10 | N/A | 2625 | 30.0 | IMD2 |  |
|  | n3 | 1780 | 5 | 25 | 1875 | N/A | N/A |  |
|  | 5 | 826.5 | 5 | 25 | 871.5 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2687.5 | 17.0 | IMD3 |  |
|  | n3 | 1757 | 5 | 25 | 1852 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 880 | 19.0 | IMD3 |  |
|  | 7 | 2560 | 10 | 50 | 2680 | N/A | N/A |  |
|  | n3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
| DC_5A-7A_n25A | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | 7 | 2565 | 5 | 25 | 2685 | 30.0 | IMD2 |  |
|  | n25 | 1855 | 5 | 25 | 1935 | N/A | N/A |  |
| DC_5A_n7A-n25A | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2685 | 30.0 | IMD2 |  |
|  | n25 | 1855 | 5 | 25 | 1935 | N/A | N/A |  |
| DC_5A-7A_n28A | 5 | 842 | 5 | 25 | 887 | N/A | N/A |  |
| DC_5A-7A-7A_n28A | 7 | N/A | 5 | N/A | 2640 | 5.9 | IMD5 |  |
|  | n28 | 728 | 5 | 25 | 783 | N/A | N/A |  |
| DC_5A-7A_n66ADC_5A-7C_n66ADC_5A-7A-7A_n66A | 5 | N/A | 5 | N/A | 880 | 17.8 | IMD3 |  |
|  | 7 | 2560 | 5 | 25 | 2680 | N/A | N/A |  |
|  | n66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 5 | 846.5 | 5 | 25 | 891.5 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2624 | 29.0 | IMD21 |  |
|  | n66 | 1777.5 | 5 | 25 | 2177.5 | N/A | N/A |  |
| DC_5A_n7A-n66A | 5 | 846.5 | 5 | 25 | 891.5 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2624 | 29.0 | IMD2 |  |
|  | n66 | 1777.5 | 5 | 25 | 2177.5 | N/A | N/A |  |
|  | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2670 | 13 | IMD3 |  |
|  | n66 | 1750 | 5 | 25 | 2150 | N/A | N/A |  |
| DC_5A-7A_n71A | 5 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2660 | 6.5 | IMD5 |  |
|  | n71 | 680 | 5 | 25 | 634 | N/A | N/A |  |
|  | 5 | 844 | 5 | 25 | 889 | N/A | N/A |  |
| DC_5A-7A_n77A | 7 | N/A | 5 | N/A | 2645 | 30.1 | IMD2 |  |
| DC_5A-7A_n77(2A)DC_5A-7A_n77(3A) | n77 | 3489 | 10 | 50 | 3489 | N/A | N/A |  |
| DC_5A-7A-7A_n77A | 5 | N/A | 5 | N/A | 879 | 30.2 | IMD21 |  |
| DC_5A-7A-7A_n77(2A)DC_5A-7A-7A_n77(3A) | 7 | 2550 | 5 | 25 | 2670 | N/A | N/A |  |
|  | n77 | 3429 | 10 | 50 | 3429 | N/A | N/A |  |
| DC_5A_n7A-n77A | 5 | 844 | 5 | 25 | 889 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2645 | 30.1 | IMD2 |  |
|  | n77 | 3489 | 10 | 50 | 3489 | N/A | N/A |  |
|  | 5 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | n7 | 2540 | 5 | 25 | 2660 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3375 | 29.7 | IMD2 |  |
|  | 5 | 829 | 5 | 25 | 885 | N/A | N/A |  |
|  | n7 | 2505 | 5 | 25 | 2625 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 4163 | 16.1 | IMD3 |  |
| DC_5A-7A_n78ADC_5A-7A_n78CDC_5A-7A_n78(A-C)DC_5A-7A-7A_n78C | 5 | 844 | 5 | 25 | 889 | N/A | N/A |  |
| DC_5A-7A-7A_n78(A-C) | 7 | N/A | 10 | N/A | 2645 | 30.1 | IMD2 |  |
|  | n78 | 3489 | 10 | 50 | 3489 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 879 | 30.2 | IMD2 |  |
|  | 7 | 2550 | 10 | 50 | 2670 | N/A | N/A |  |
|  | n78 | 3429 | 10 | 50 | 3429 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 875 | 3.3 | IMD5 |  |
|  | 7 | 2525 | 10 | 50 | 2645 | N/A | N/A |  |
|  | n78 | 3350 | 10 | 50 | 3350 | N/A | N/A |  |
| DC_5A_n7A-n78ADC_5A_n7(2A)-n78ADC_5A_n7A-n78(2A)DC_5A_n7(2A)-n78(2A) | 5 | 844 | 5 | 25 | 889 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2645 | 30.1 | IMD2 |  |
|  | n78 | 3489 | 10 | 50 | 3489 | N/A | N/A |  |
|  | 5 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | n7 | 2540 | 5 | 25 | 2660 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3375 | 29.7 | IMD2 |  |
| DC_5A-13A_n66A | 5 | 840 | 5 | 25 | 885 | N/A | N/A |  |
|  | 13 | N/A | 5 | N/A | 750 | 9.4 | IMD4 |  |
|  | n66 | 1770 | 5 | 25 | 2170 | N/A | N/A |  |
| DC_5A-13A_n77A11 | 5 | 840 | 5 | 25 | 885 | N/A | N/A |  |
| DC_5A-13A_n77C11 | n77 | 4110 | 10 | 50 | 4110 | N/A | N/A |  |
|  | 13 | N/A | 5 | N/A | 750 | 4.4 | IMD5 |  |
|  | 13 | 782 | 5 | 20 | 751 | N/A | N/A |  |
|  | n77 | 4013 | 10 | 50 | 4013 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 885 | 4.5 | IMD5 |  |
| DC_5A_n28A-n77ADC_5A_n28A-n77C | 5 | 846.5 | 5 | 25 | 891.5 | N/A | N/A |  |
|  | n28 | 710.5 | 5 | 25 | 765.5 | 11.6 | IMD4 |  |
|  | n77 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | 5 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | n28 | 710 | 5 | 25 | 765 | 4.4 | IMD5 |  |
|  | n77 | 4105 | 10 | 50 | 4105 | N/A | N/A |  |
| DC_5A_n28A-n78ADC_5A_n28A-n78C | 5 | 846.5 | 5 | 25 | 891.5 | N/A | N/A |  |
|  | n28 | 715.5 | 5 | 25 | 765.5 | 11.6 | IMD4 |  |
|  | n78 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n28 | 707 | 5 | 25 | 762 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3658 | 4.0 | IMD5 |  |
| DC_5A-30A_n2A | 5 | N/A | 5 | N/A | 880 | 8 | IMD4 |  |
|  | 30 | 2310 | 5 | 25 | 2355 | N/A | N/A |  |
|  | n2 | 1870 | 5 | 25 | 1950 | N/A | N/A |  |
| DC_5A-30A_n77ADC_5A-30A_n77(2A) | 5 | 835 | 5 | 25 | 880 | 15.2 | IMD34 |  |
|  | 30 | N/A | 5 | N/A | 2355 | N/A | N/A |  |
|  | n77 | 3740 | 10 | 50 | 3740 | N/A | N/A |  |
|  | 5 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | 30 | N/A | 5 | N/A | 2355 | 13.2 | IMD311 |  |
|  | n77 | 4025 | 10 | 50 | 4025 | N/A | N/A |  |
| DC_5A_n38A-n66A | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n66 | 1760 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n38 | N/A | 10 | N/A | 2590 | 28.9 | IMD2 |  |
| DC_5A-40A_n77ADC_5A-40C_n77ADC_5A-40A_n77CDC_5A-40C_n77C | 5 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | 40 | 2355 | 5 | 25 | 2355 | 13.2 | IMD3 |  |
|  | n77 | 4025 | 10 | 50 | 4025 | N/A | N/A |  |
|  | 5 | 835 | 5 | 25 | 880 | 15.2 | IMD34 |  |
|  | 40 | 2310 | 5 | 25 | 2310 | N/A | N/A |  |
|  | n77 | 3740 | 10 | 50 | 3740 | N/A | N/A |  |
| DC_5A_n41A-n66A | 5 | 846.5 | 5 | 25 | 891.5 | N/A | N/A |  |
|  | n41 | 2624 | 10 | 50 | 2624 | 29.0 | IMD2 |  |
|  | n66 | 1777.5 | 5 | 25 | 2177.5 | N/A | N/A |  |
|  | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n41 | 2600 | 10 | 50 | 2600 | 18 | IMD3 |  |
|  | n66 | 1715 | 5 | 25 | 2115 | N/A | N/A |  |
| DC_5A_n40A-n77A | 5 | 840 | 5 | 25 | 885 | N/A | N/A |  |
| DC_5A_n40A-n77(2A) | n40 | 2310 | 10 | 50 | 2310 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3780 | 16.1 | IMD3 |  |
|  | 5 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2355 | 13.2 | IMD3 |  |
|  | n77 | 4025 | 10 | 50 | 4025 | N/A | N/A |  |
| DC_5A-40A_n78ADC_5A-40C_n78ADC_5A-40A_n78CDC_5A-40C_n78C | 5 | 835 | 5 | 25 | 880 | 15.2 | IMD3 |  |
|  | 40 | 2310 | 5 | 25 | 2310 | N/A | N/A |  |
|  | n78 | 3740 | 10 | 50 | 3740 | N/A | N/A |  |
| DC_5A_n40A-n78A | 5 | 840 | 5 | 25 | 885 | N/A | N/A |  |
| DC_5A_n40A-n78C | n40 | 2310 | 10 | 50 | 2310 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3780 | 16.1 | IMD3 |  |
| DC_5A_n41A-n77A | 5 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | n41 | 2540 | 10 | 50 | 2540 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3375 | 28.2 | IMD22 |  |
|  | 5 | 840 | 5 | 25 | 885 | N/A | N/A |  |
|  | n41 | 2503 | 10 | 50 | 2503 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 4183 | 14.6 | IMD3 |  |
|  | 5 | 844 | 5 | 25 | 889 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2645 | 28.1 | IMD2 |  |
|  | n77 | 3489 | 10 | 50 | 3489 | N/A | N/A |  |
|  | 5 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2510 | 11.2 | IMD3 |  |
|  | n77 | 4180 | 10 | 50 | 4180 | N/A | N/A |  |
| DC_5A_41A_n78A | 5 | N/A | 5 | N/A | 885 | 30.2 | IMD2 |  |
|  | 41 | 2615 | 5 | 25 | 2615 | N/A | N/A |  |
|  | n78 | 3500 | 10 | 50 | 3500 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 881.5 | 3.1 | IMD5 |  |
|  | 41 | 2620.5 | 5 | 25 | 2620.5 | N/A | N/A |  |
|  | n78 | 3490 | 10 | 50 | 3490 | N/A | N/A |  |
| DC_5A_n41A-n78A | 5 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | n41 | 2540 | 10 | 50 | 2540 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3375 | 28.2 | IMD22 |  |
|  | 5 | 844 | 5 | 25 | 889 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2645 | 28.1 | IMD2 |  |
|  | n78 | 3489 | 10 | 50 | 3489 | N/A | N/A |  |
| DC_5A-41A_n79A | 5 | N/A | 5 | N/A | 880 | 23.9 | IMD3 |  |
|  | 41 | 2665 | 20 | 100 | 2665 | N/A | N/A |  |
|  | n79 | 4450 | 40 | 216 | 4450 | N/A | N/A |  |
|  | 5 | 826.5 | 5 | 25 | 871.5 | N/A | N/A |  |
|  | 41 | N/A | 20 | N/A | 2517.5 | 1.8 | IMD4 |  |
|  | n79 | 4980 | 40 | 216 | 4980 | N/A | N/A |  |
| DC_5A-46A_n66A | 5 | 847 | 5 | 25 | 892 | N/A | N/A |  |
|  | 46 | N/A | 10 | N/A | 5163 | 9.04 | IMD4\|2*fB5+2*fn66\| |  |
|  | n66 | 1775 | 5 | 25 | 2175 | N/A | N/A |  |
| DC_5A-48A_n12A | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | 48 | N/A | 5 | N/A | 3650 | 4.4 | IMD5 |  |
|  | n12 | 705 | 5 | 25 | 735 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 875 | 5.9 | IMD5 |  |
|  | 48 | 3695 | 5 | 25 | 3695 | N/A | N/A |  |
|  | n12 | 705 | 5 | 25 | 735 | N/A | N/A |  |
| DC_5A-48A_n71A | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | 48 | N/A | 5 | N/A | 3590 | 4.4 | IMD5 |  |
|  | n71 | 690 | 5 | 25 | 644 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 880 | 5.9 | IMD5 |  |
|  | 48 | 3600 | 5 | 25 | 3600 | N/A | N/A |  |
|  | n71 | 680 | 5 | 25 | 634 | N/A | N/A |  |
| DC_5A-66A_n2ADC_5B-66A_n2ADC_5A-5A-66A_n2ADC_5A-66A-66A_n2ADC_5B-66A-66A_n2ADC_5A-5A-66A-66A_n2A | 5 | 834 | 5 | 25 | 879 | N/A | N/A |  |
| DC_5A-66B_n2ADC_5A-66A_n2(2A) | 66 | N/A | 5 | N/A | 2132 | 7.2 | IMD4 |  |
|  | n2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
| DC_5A-66A_n7ADC_5A-66A-66A_n7A | 5 | N/A | 5 | N/A | 880 | 18.0 | IMD3 |  |
|  | 66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n7 | 2560 | 5 | 25 | 2680 | N/A | N/A |  |
| DC_5A-66A_n25A | 5 | 834 | 5 | 25 | 879 | N/A | N/A |  |
|  | 66 | 1732 | 5 | 25 | 2132 | 7.2 | IMD4 |  |
|  | n25 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
| DC_5A-66A_n30A | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2125 | 4 | IMD5 |  |
|  | n30 | 2307.5 | 5 | 50 | 2352.5 | N/A | N/A |  |
| DC_5A-66A_n41A | 5 | 830 | 5 | 25 | 875 | 28.9 | IMD2 |  |
|  | 66 | 1765 | 5 | 25 | 2165 | N/A | N/A |  |
|  | n41 | 2640 | 10 | 50 | 2640 | N/A | N/A |  |
|  | 5 | 835 | 5 | 25 | 880 | 18.0 | IMD3 |  |
|  | 66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n41 | 2560 | 10 | 50 | 2560 | N/A | N/A |  |
| DC_5A-66A_n71A | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2161 | 13 | IMD3 |  |
|  | n71 | 665.5 | 5 | 25 | 619.5 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 891.5 | 4.2 | IMD5 |  |
|  | 66 | 1770 | 5 | 25 | 2170 | N/A | N/A |  |
|  | n71 | 665.5 | 5 | 25 | 619.5 | N/A | N/A |  |
| DC_5A-66A_n77A | 5 | 826.5 | 5 | 25 | 871.5 | N/A | N/A |  |
| DC_5A-66A_n77CDC_5A-66A_n77(2A)DC_5A-66A-66A_n77ADC_5A-66A-66A_n77C | 66 | N/A | 5 | N/A | 2142 | 13.2 | IMD3 |  |
| DC_5A-66A-66A_n77(2A) | n77 | 3795 | 10 | 50 | 3795 | N/A | N/A |  |
| DC_5A-66A_n78ADC_5A-66A_n78(2A) | 5 | 826.5 | 5 | 25 | 871.5 | N/A | N/A |  |
| DC_5A-66A-66A_n78A | 66 | N/A | 5 | N/A | 2142 | 13.2 | IMD3 |  |
|  | n78 | 3795 | 10 | 50 | 3795 | N/A | N/A |  |
| DC_5A_n66A-n77A | 5 | 826.5 | 5 | 25 | 871.5 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2142 | 13.2 | IMD3 |  |
|  | n77 | 3795 | 10 | 50 | 3795 | N/A | N/A |  |
|  | 5 | 845 | 5 | 25 | 890 | N/A | N/A |  |
|  | n66 | 1785 | 5 | 25 | 2185 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3475 | 16.1 | IMD3 |  |
| DC_5A_n66A-n78A | 5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n66 | 1760 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3420 | 16.6 | IMD3 |  |
|  | 5 | 826.5 | 5 | 25 | 871.5 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2142 | 13.2 | IMD3 |  |
|  | n78 | 3795 | 10 | 50 | 3795 | N/A | N/A |  |
| DC_7A_n1A-n28A | 7 | 2535 | 5 | 25 | 2655 | N/A | N/A |  |
| DC_7C-n1A-n28A | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 780 | 4.3 | IMD5 |  |
| DC_7A_n1A-n40A | 7 | 2540 | 5 | 25 | 2660 | N/A | N/A |  |
|  | n40 | 2335 | 10 | 50 | 2335 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2130 | 15.2 | IMD3 |  |
| DC_7A_n1A-n75A | n1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | 7 | 2502.5 | 5 | 25 | 2622.5 | N/A | N/A |  |
|  | 75 | N/A | 5 | N/A | 1454.5 | 15.2 | IMD3 |  |
| DC_7A_n1A-n78A | 7 | 2520 | 5 | 25 | 2640 | N/A | N/A |  |
| DC_7C_n1A-n78A | n1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
| DC_7A_n1A-n78(2A) | n78 | N/A | 10 | N/A | 3390 | 10.1 | IMD4 |  |
| DC_7C_n1A-n78(2A) | 7 | 2530 | 5 | 25 | 2650 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2160 | 9.0 | IMD4 |  |
|  | n78 | 3610 | 10 | 50 | 3610 | N/A | N/A |  |
| DC_7A_n2A-n71A | 7 | 2530 | 5 | 25 | 2650 | N/A | N/A |  |
|  | n2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 630 | 28.7 | IMD2 |  |
| DC_7A_n2A-n77A | 7 | 2550 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n2 | 1870 | 5 | 25 | 1950 | 8.6 | IMD4 |  |
|  | n77 | 3525 | 10 | 50 | 3525 | N/A | N/A |  |
|  | 7 | 2525 | 5 | 25 | 2645 | N/A | N/A |  |
|  | n2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n77 | 3775 | 10 | 50 | 3775 | 4.2 | IMD5 |  |
| DC_7A_n2A-n78A | 7 | 2550 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n2 | N/A | 5 | N/A | 1950 | 8.6 | IMD4 |  |
|  | n78 | 3525 | 10 | 50 | 3525 | N/A | N/A |  |
|  | 7 | 2525 | 5 | 25 | 2645 | N/A | N/A |  |
|  | n2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3775 | 4.2 | IMD5 |  |
| DC_7A_n3A-n78A | 7 | 2560 | 5 | 25 | 2680 | N/A | N/A |  |
| DC_7C_n3A-n78A | n3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
| DC_7A_n3A-n78(2A) | n78 | N/A | 10 | N/A | 3390 | 16.1 | IMD3 |  |
| DC_7C_n3A-n78(2A) | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1820 | 15.6 | IMD3 |  |
|  | n78 | 3310 | 10 | 50 | 3310 | N/A | N/A |  |
| DC_7A_n8A-n40A | 7 | 2530 | 5 | 25 | 2650 | N/A | N/A |  |
|  | n8 | 905 | 5 | 25 | 950 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2345 | 3.0 | IMD5 |  |
| DC_7A-8A_n3A | n3 | 1735 | 5 | 25 | 1830 | N/A | N/A |  |
|  | 7 | 2530 | 10 | 50 | 2650 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 940 | 18.0 | IMD3 |  |
|  | 7 | N/A | 10 | N/A | 2670 | 29.0 | IMD2+IMD33 |  |
|  | 8 | 890 | 5 | 25 | 935 | N/A | N/A |  |
|  | n3 | 1780 | 5 | 25 | 1875 | N/A | N/A |  |
| DC_7A-8A_n20A | 7 | N/A | 5 | N/A | 2640 | 21.1 | IMD34,15 |  |
|  | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n20 | 840 | 5 | 25 | 799 | N/A | N/A |  |
|  | 7 | 2503 | 5 | 25 | 2623 | N/A | N/A |  |
|  | n20 | 859 | 5 | 25 | 818 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 933 | 4.4 | IMD5 |  |
| DC_7A-8A_n77A | 7 | 2520 | 5 | 25 | 2640 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 940 | 3.1 | IMD5 |  |
|  | n77 | 3310 | 10 | 50 | 3310 | N/A | N/A |  |
|  | 7 | 2530 | 5 | 25 | 2650 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 940 | 30.5 | IMD2 |  |
|  | n77 | 3470 | 10 | 50 | 3470 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2650 | 28 | IMD2 |  |
|  | 8 | 895 | 5 | 25 | 940 | N/A | N/A |  |
|  | n77 | 3545 | 10 | 50 | 3545 | N/A | N/A |  |
| DC_7A-8A_n78A | 7 | 2530 | 5 | 25 | 2650 | N/A | N/A |  |
| DC_7A-8B_n78A | 8 | N/A | 5 | N/A | 940 | 30.5 | IMD2 |  |
| DC_7A-7A-8B_n78A | n78 | 3470 | 10 | 50 | 3470 | N/A | N/A |  |
|  | 7 | 2520 | 5 | 25 | 2640 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 940 | 3.1 | IMD5 |  |
|  | n78 | 3310 | 10 | 50 | 3310 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2650 | 28 | IMD2 |  |
|  | 8 | 895 | 5 | 25 | 940 | N/A | N/A |  |
|  | n78 | 3545 | 10 | 50 | 3545 | N/A | N/A |  |
| DC_7A_n8A-n78A | 7 | 2555 | 5 | 25 | 2675 | N/A | N/A |  |
|  | n8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3455 | 28.5 | IMD2 |  |
|  | 7 | 2555 | 5 | 25 | 2675 | N/A | N/A |  |
|  | n8 | N/A | 5 | N/A | 945 | 29.7 | IMD2 |  |
|  | n78 | 3500 | 10 | 50 | 3500 | N/A | N/A |  |
| DC_7A-12A_n2A | 7 | 2502.5 | 5 | 25 | 2622.5 | N/A | N/A |  |
| DC_7A-12A_n2(2A) | 12 | N/A | 5 | N/A | 731.5 | 5.3 | IMD5 |  |
|  | n2 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2621 | 30.8 | IMD2 |  |
|  | 12 | 713.5 | 5 | 25 | 743.5 | N/A | N/A |  |
|  | n2 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
| DC_7A-12A_n25A | 7 | 2502.5 | 5 | 25 | 2622.5 | N/A | N/A |  |
|  | 12 | N/A | 5 | N/A | 731.5 | 5.3 | IMD5 |  |
|  | n25 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2622.5 | 30.8 | IMD2 |  |
|  | 12 | 713.5 | 5 | 25 | 743.5 | N/A | N/A |  |
|  | n25 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
| DC_7A-12A_n66A | 7 | 2515 | 5 | 25 | 2635 | N/A | N/A |  |
|  | 12 | N/A | 5 | N/A | 742 | 31 | IMD2 |  |
|  | n66 | 1773 | 5 | 25 | 2173 | N/A | N/A |  |
| DC_7A_n12A-n77A | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n12 | N/A | 5 | N/A | 740 | 30.8 | IMD2 |  |
|  | n77 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | 7 | 2505 | 5 | 25 | 2625 | N/A | N/A |  |
|  | n12 | 702 | 5 | 25 | 732 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3909 | 16.0 | IMD3 |  |
| DC_7A-12A_n77ADC_7A-12A_n77(2A) | 7 | N/A | 5 | N/A | 2662 | 29.6 | IMD21 |  |
|  | 12 | 708 | 5 | 25 | 738 | N/A | N/A |  |
|  | n77 | 3370 | 10 | 50 | 3370 | N/A | N/A |  |
|  | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | 12 | N/A | 5 | N/A | 740 | 30.8 | IMD2 |  |
|  | n77 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
| DC_7A-12A_n78ADC_7A-12A_n78(2A) | 7 | N/A | 5 | N/A | 2662 | 29.6 | IMD2 |  |
|  | 12 | 708 | 5 | 25 | 738 | N/A | N/A |  |
|  | n78 | 3370 | 10 | 50 | 3370 | N/A | N/A |  |
|  | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | 12 | N/A | 5 | N/A | 740 | 30.8 | IMD24 |  |
|  | n78 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
| DC_7A_n12A-n78A | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n12 | 710 | 5 | 25 | 740 | 30.8 | IMD24 |  |
|  | n78 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | 7 | 2505 | 5 | 25 | 2625 | N/A | N/A |  |
|  | n12 | 702 | 5 | 25 | 732 | N/A | N/A |  |
|  | n78 | N/A | 10 | 50 | 3606 | 10.3 | IMD4 |  |
| DC_7A-13A_n66A | 7 | 2520 | 5 | 25 | 2640 | N/A | N/A |  |
|  | 13 | N/A | 5 | N/A | 750 | 31 | IMD2 |  |
|  | n66 | 1770 | 5 | 25 | 2170 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2660 | 18 | IMD3 |  |
|  | 13 | 780 | 5 | 25 | 749 | N/A | N/A |  |
|  | n66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
| DC_7A-13A_n25ADC_7A-7A-13A_n25ADC_7C-13A_n25A | 7 | N/A | 10 | N/A | 2662 | 27.6 | IMD2 |  |
|  | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
|  | n25 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
| DC_7A-20A_n1ADC_7C-20A_n1A | 7 | 2510 | 10 | 50 | 2630 | N/A | N/A |  |
|  | 20 | N/A | 10 | N/A | 800 | 4.5 | IMD5 |  |
|  | n1 | 1940 | 5 | 25 | 2130 | N/A | N/A |  |
| DC_7A-20A_n3A | 7 | 2543 | 10 | 50 | 2663 | N/A | N/A |  |
|  | 20 | N/A | 10 | N/A | 806 | 10.5 | IMD2 |  |
|  | n3 | 1737 | 5 | 25 | 1832 | N/A | N/A |  |
|  | 7 | N/A | 10 | N/A | 2630 | 26.0 | IMD21 |  |
|  | 20 | 855 | 5 | 25 | 814 | N/A | N/A |  |
|  | n3 | 1775 | 10 | 50 | 1870 | N/A | N/A |  |
| DC_7A-20A_n7A | 7 | N/A | 5 | N/A | 2631.5 | 2.5 | IMD5 |  |
|  | 20 | 834.5 | 5 | 25 | 793.5 | N/A | N/A |  |
|  | n7 | 2567.5 | 5 | 25 | 2687.5 | N/A | N/A |  |
| DC_7A-20A_n8A | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n8 | 885 | 5 | 25 | 930 | N/A | N/A |  |
|  | 20 | N/A | 5 | N/A | 795 | 17.4 | IMD3 |  |
|  | 7 | N/A | 5 | N/A | 2640 | 21.1 | IMD3 |  |
|  | n8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | 20 | 840 | 5 | 25 | 799 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2624 | 18.8 | IMD3 |  |
|  | n8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | 20 | 857 | 5 | 25 | 816 | N/A | N/A |  |
| DC_7A-20A_n28ADC_7C-20A_n28A | 20 | 842 | 5 | 25 | 801 | N/A | N/A |  |
|  | n28 | 728 | 5 | 25 | 783 | N/A | N/A |  |
|  | 7 | N/A | 10 | N/A | 2640 | 5.9 | IMD5 |  |
| DC_7A-20A_n78ADC_7A-7A-20A_n78A | 7 | 2560 | 5 | 25 | 2680 | N/A | N/A |  |
| DC_7A-20A_n78(2A) | 20 | N/A | 5 | N/A | 810 | 30.5 | IMD2 |  |
| DC_7A-20A_n78C | n78 | 3370 | 10 | 50 | 3370 | N/A | N/A |  |
|  | 7 | 2560 | 5 | 25 | 2680 | N/A | N/A |  |
|  | 20 | N/A | 5 | N/A | 810 | 3.0 | IMD5 |  |
|  | n78 | 3435 | 10 | 50 | 3435 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2675 | 30.8 | IMD2 |  |
|  | 20 | 845 | 5 | 25 | 804 | N/A | N/A |  |
|  | n78 | 3520 | 10 | 50 | 3520 | N/A | N/A |  |
| DC_7A_n25A-n71A | 7 | 2530 | 5 | 25 | 2650 | N/A | N/A |  |
|  | n25 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 630 | 28.7 | IMD2 |  |
|  | 7 | 2550 | 5 | 25 | 2670 | N/A | N/A |  |
|  | n25 | 1910 | 5 | 25 | 1990 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 630 | 5 | IMD5 |  |
| DC_7A-25A_n77ADC_7A-7A-25A_n77ADC_7C-25A_n77ADC_7C-25A-25A_n77ADC_7A-25A-25A_n77ADC_7A-7A-25A-25A_n77A | 7 | 2550 | 5 | 25 | 2670 | N/A | N/A |  |
|  | 25 | N/A | 5 | N/A | 1950 | 8.6 | IMD4 |  |
|  | n77 | 3525 | 10 | 50 | 3525 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2660 | 3.4 | IMD5 |  |
|  | 25 | 1860 | 5 | 25 | 1940 | N/A | N/A |  |
|  | n77 | 4120 | 10 | 50 | 4120 | N/A | N/A |  |
| DC_7A-25A_n78ADC_7A-7A-25A_n78ADC_7C-25A_n78ADC_7A-25A-25A_n78ADC_7A-7A-25A-25A_n78ADC_7C-25A-25A_n78A | 7 | 2550 | 5 | 25 | 2670 | N/A | N/A |  |
|  | 25 | N/A | 5 | N/A | 1950 | 8.6 | IMD4 |  |
|  | n78 | 3525 | 10 | 50 | 3525 | N/A | N/A |  |
| DC_7A-26A_n78A | 7 | 2525 | 5 | 25 | 2645 | 30.1 | IMD2 |  |
| DC_7C-26A_n78A | 26 | 844 | 5 | 25 | 889 | N/A | N/A |  |
|  | n78 | 3489 | 10 | 50 | 3489 | N/A | N/A |  |
|  | 7 | 2550 | 5 | 25 | 2670 | N/A | N/A |  |
|  | 26 | 834 | 5 | 25 | 879 | 30.2 | IMD2 |  |
|  | n78 | 3429 | 10 | 50 | 3429 | N/A | N/A |  |
|  | 7 | 2525 | 5 | 25 | 2645 | N/A | N/A |  |
|  | 26 | 830 | 5 | 25 | 875 | 3.3 | IMD5 |  |
|  | n78 | 3350 | 10 | 50 | 3350 | N/A | N/A |  |
| DC_7A_n26A-n78A | 7 | 2550 | 5 | 25 | 2670 | N/A | N/A |  |
| DC_7C_n26A-n78A | n26 | N/A | 5 | N/A | 879 | 30.2 | IMD2 |  |
|  | n78 | 3429 | 10 | 50 | 3429 | N/A | N/A |  |
|  | 7 | 2525 | 5 | 25 | 2645 | N/A | N/A |  |
|  | n26 | N/A | 5 | N/A | 875 | 3.3 | IMD5 |  |
|  | n78 | 3350 | 10 | 50 | 3350 | N/A | N/A |  |
|  | 7 | 2540 | 5 | 25 | 2660 | N/A | N/A |  |
|  | n26 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3375 | 29.7 | IMD29 |  |
| DC_7A-28A_n1A | 7 | 2535 | 5 | 25 | 2655 | N/A | N/A |  |
| DC_7A-7A-28A_n1A | 28 | N/A | 5 | N/A | 780 | 4.3 | IMD5 |  |
|  | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2665 | 29.0 | IMD2 |  |
|  | 28 | 730 | 5 | 25 | 785 | N/A | N/A |  |
|  | n1 | 1935 | 5 | 25 | 2125 | N/A | N/A |  |
| DC_7A-28A_n2A | 7 | N/A | 10 | N/A | 2630 | 27.6 | IMD2 |  |
|  | 28 | 730 | 5 | 25 | 785 | N/A | N/A |  |
|  | n2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
| DC_7A-28A_n3ADC_7C-28A_n3A | 7 | 2543 | 5 | 25 | 2663 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 796.0 | 20.0 | IMD2 |  |
|  | n3 | 1747 | 5 | 25 | 1842 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2685 | 18 | IMD3 |  |
|  | 28 | 745 | 5 | 25 | 800 | N/A | N/A |  |
|  | n3 | 1715 | 5 | 25 | 1810 | N/A | N/A |  |
| DC_7A-28A_n5A DC_7C-28A_n5A | 7 | 2540 | 5 | 25 | 2660 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 776 | 4.4 | IMD5 |  |
|  | n5 | 829 | 5 | 25 | 874 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2630 | 5.9 | IMD5 |  |
|  | 28 | 730 | 5 | 25 | 785 | N/A | N/A |  |
|  | n5 | 840 | 5 | 25 | 885 | N/A | N/A |  |
| DC_7A-28A_n20A | 7 | N/A | 5 | N/A | 2640 | 5.9 | IMD5 |  |
|  | 28 | 728 | 5 | 25 | 783 | N/A | N/A |  |
|  | n20 | 842 | 5 | 25 | 801 | N/A | N/A |  |
|  | 7 | 2505 | 5 | 25 | 2625 | N/A | N/A |  |
|  | n20 | 859 | 5 | 25 | 818 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 787 | 17.4 | IMD3 |  |
| DC_7A-28A_n40A | 7 | N/A | 5 | N/A | 2630 | 5.9 | IMD5 |  |
|  | 28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | n40 | 2310 | 10 | 50 | 2310 | N/A | N/A |  |
| DC_7A-28A_n66ADC_7C-28A_n66A | 7 | N/A | 10 | N/A | 2682 | 16.9 | IMD3 |  |
|  | 28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | n66 | 1712.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
|  | 7 | 2543 | 5 | 25 | 2663 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 796 | 20.0 | IMD2 |  |
|  | n66 | 1747 | 5 | 25 | 2147 | N/A | N/A |  |
| DC_7A-28A_n78A | 7 | 2567.5 | 5 | 25 | 2687.5 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 782.5 | 28.8 | IMD2 |  |
|  | n78 | 3350 | 10 | 50 | 3350 | N/A | N/A |  |
|  | 7 | 2567.5 | 5 | 25 | 2687.5 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 782.5 | 3.0 | IMD5 |  |
|  | n78 | 3460 | 10 | 50 | 3460 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2650 | 30.5 | IMD2 |  |
|  | 28 | 740 | 5 | 25 | 795 | N/A | N/A |  |
|  | n78 | 3390 | 10 | 50 | 3390 | N/A | N/A |  |
| DC_7A_n28A-n78ADC_7C_n28A-n78A | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
| DC_7A-7A_n28A-n78A | n28 | 745 | 5 | 25 | 800 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3310 | 29.7 | IMD2 |  |
|  | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n78 | 3365 | 10 | 50 | 3365 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 800 | 28.8 | IMD2 |  |
| DC_7A-29A_n78ADC_7C-29A_n78ADC_7A-7A-29A_n78A | 7 | 2540 | 5 | 25 | 2660 | N/A | N/A |  |
|  | 29 | N/A | N/A | N/A | 720 | 3.0 | IMD5 |  |
|  | n78 | 3450 | 10 | 50 | 3450 | N/A | N/A |  |
| DC_7A-32A_n1A | n1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |  |
|  | 7 | 2502.5 | 5 | 25 | 2622.5 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1454.5 | 15.2 | IMD3 |  |
| DC_7A-32A_n3A | 7 | 1775 | 5 | 25 | 1870 | N/A | N/A |  |
|  | n3 | 2510 | 10 | 50 | 2630 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1470 | 10.5 | IMD4 |  |
| DC_7A-32A_n78A | n78 | 3560.5 | 10 | 50 | 3560.5 | N/A | N/A |  |
|  | 7 | 2517.5 | 5 | 25 | 2637.5 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1474.5 | 17.6 | IMD3 |  |
|  | n78 | 3311 | 10 | 50 | 3311 | N/A | N/A |  |
|  | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1492 | 4.9 | IMD4 |  |
| DC_7A-40A_n1ADC_7A-40C_n1A | n1 | 1970 | 5 | 25 | 2160 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2650 | 32.1 | IMD3 |  |
|  | 40 | 2310 | 5 | 25 | 2310 | N/A | N/A |  |
| DC_7A_n40A-n77A | 7 | 2520 | 5 | 25 | 2640 | N/A | N/A |  |
| DC_7A_n40A-n77(2A) | n40 | N/A | 10 | N/A | 2360 | 9.2 | IMD4 |  |
| DC_7A-7A_n40A-n77ADC_7A-7A_n40A-n77(2A) | n77 | 3700 | 10 | 50 | 3700 | N/A | N/A |  |
| DC_7A-40A_n78ADC_7A-40C_n78A | 7 | N/A | 5 | N/A | 2630 | 10.1 | IMD4 |  |
|  | 40 | 2310 | 5 | 25 | 2310 | N/A | N/A |  |
|  | n78 | 3625 | 10 | 50 | 3625 | N/A | N/A |  |
|  | 7 | 2510 | 5 | 25 | 2630 | N/A | N/A |  |
|  | 40 | N/A | 5 | N/A | 2310 | 8.7 | IMD4 |  |
|  | n78 | 3785 | 10 | 50 | 3785 | N/A | N/A |  |
| DC_7A_n40A-n78A | 7 | 2520 | 10 | 50 | 2640 | N/A | N/A |  |
| DC_7A_n40A-n78C | n40 | N/A | 10 | N/A | 2360 | 8.7 | IMD4 |  |
| DC_7A-7A_n40A-n78ADC_7A-7A_n40A-n78C | n78 | 3700 | 10 | 50 | 3700 | N/A | N/A |  |
| DC_7A-46A_n78A6 | 7 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 46 | N/A | N/A | N/A | N/A | N/A | IMD2, IMD5 |  |
|  | n78 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_7A-66A_n5ADC_7C-66A_n5ADC_7A-66A-66A_n5ADC_7C-66A-66A_n5ADC_7A-7A-66A_n5ADC_7A-7A-66A-66A_n5A | 7 | N/A | 10 | N/A | 2625 | 30.0 | IMD26 |  |
|  | 66 | 1775 | 10 | 50 | 2175 | N/A | N/A |  |
|  | n5 | 846.5 | 5 | 25 | 891.5 | N/A | N/A |  |
| DC_7A-66A_n7ADC_7A-66A-66A_n7A | 7 | N/A | 10 | N/A | 2675 | 15 | IMD4 |  |
|  | 66 | 1730 | 5 | 25 | 2130 | N/A | N/A |  |
|  | n7 | 2515 | 10 | 50 | 2635 | N/A | N/A |  |
| DC_7A-66A_n28A | 7 | N/A | 5 | N/A | 2685 | 18.0 | IMD3 |  |
|  | 66 | 1715 | 5 | 25 | 2115 | N/A | N/A |  |
|  | n28 | 745 | 5 | 25 | 800 | N/A | N/A |  |
| DC_7A-66A_n77ADC_7A-7A-66A_n77ADC_7A-7A-66A_n77(2A)DC_7A-66A_n77(2A)DC_7C-66A_n77ADC_7C-66A_n77(2A) | 7 | 2550 | 5 | 25 | 2685 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2150 | 8.7 | IMD4\|2*fB7-2*fn77\| |  |
|  | n77 | 3625 | 10 | 50 | 3475 | N/A | N/A |  |
|  | 66 | 1715 | 5 | 25 | 2115 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2670 | 5.2 | IMD5 |  |
|  | n77 | 4190 | 10 | 50 | 4190 | N/A | N/A |  |
|  | 66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 7 | N/A | 5 | N/A | 2640 | 3.4 | IMD5 |  |
|  | n77 | 3900 | 10 | 50 | 3900 | N/A | N/A |  |
| DC_7A_n66A-n77ADC_7A-7A_n66A-n77ADC_7C_n66A-n77A | 7 | 2550 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2150 | 8.7 | IMD4 |  |
|  | n77 | 3625 | 10 | 50 | 3625 | N/A | N/A |  |
|  | 7 | 2542 | 5 | 25 | 2662 | N/A | N/A |  |
|  | n66 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3344 | 16.0 | IMD34 |  |
| DC_7A-66A_n78ADC_7C-66A_n78ADC_7A-7A-66A_n78ADC_7A-66A-66A_n78ADC_7A-7A-66A-66A_n78ADC_7C-66A-66A_n78ADC_7A_n66A-n78ADC_7A-7A_n66A-n78ADC_7C_n66A-n78ADC_7A-66A_n78(2A)DC_7C-66A_n78(2A)DC_7A-7A-66A_n78(2A)DC_7A-66A-66A_n78(2A)DC_7A-7A-66A-66A_n78(2A)DC_7C-66A-66A_n78(2A) | 7 | 2550 | 5 | 25 | 2685 | N/A | N/A |  |
|  | 66/n66 | N/A | 5 | N/A | 2150 | 8.7 | IMD4 |  |
|  | n78 | 3625 | 10 | 50 | 3475 | N/A | N/A |  |
| DC_7A_n66A-n78ADC_7A-7A_n66A-n78ADC_7C_n66A-n78A | 7 | 2542 | 5 | 25 | 2662 | N/A | N/A |  |
|  | n66 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3344 | 16.0 | IMD3 |  |
| DC_7A-71A_n2A | n2 | 1859 | 5 | 25 | 1939 | N/A | N/A |  |
| DC_7A-71A_n2(2A) | 7 | 2505 | 5 | 25 | 2625 | N/A | N/A |  |
|  | 71 | N/A | 5 | N/A | 646 | 30.8 | IMD2 |  |
| DC_7A-71A_n25A | 7 | 2530 | 5 | 25 | 2530 | N/A | N/A |  |
|  | 71 | N/A | 5 | N/A | 630 | 28.7 | IMD24 |  |
|  | n25 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
| DC_7A-71A_n77ADC_7A-71A_n77(2A) | 7 | N/A | 5 | N/A | 2670 | 29.6 | IMD21 |  |
|  | 71 | 680 | 5 | 25 | 634 | N/A | N/A |  |
|  | n77 | 3350 | 10 | 50 | 3350 | N/A | N/A |  |
| DC_7A_n71A-n77A | 7 | 2505 | 5 | 25 | 2625 | N/A | N/A |  |
|  | n71 | 666 | 5 | 25 | 620 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3837 | 16.0 | IMD3 |  |
| DC_7A-71A_n78ADC_7A-71A_n78(2A) | 7 | N/A | 5 | N/A | 2670 | 29.6 | IMD2 |  |
|  | 71 | 680 | 5 | 25 | 634 | N/A | N/A |  |
|  | n78 | 3350 | 10 | 50 | 3350 | N/A | N/A |  |
|  | 7 | 2540 | 5 | 25 | 2660 | N/A | N/A |  |
|  | 71 | N/A | 5 | N/A | 640 | 3.0 | IMD5 |  |
|  | n78 | 3490 | 10 | 50 | 3490 | N/A | N/A |  |
| DC_7A_n71A-n78A | 7 | 2550 | 5 | 25 | 2670 | N/A | N/A |  |
|  | n71 | 693 | 5 | 25 | 647 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3714 | 9.7 | IMD4 |  |
|  | 7 | 2555 | 5 | 25 | 2675 | N/A | N/A |  |
|  | n78 | 3520 | 10 | 50 | 3520 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 625 | 3.9 | IMD5 |  |
| DC_7A_n75A-n78A | n78 | 3560.5 | 10 | 50 | 3560.5 | N/A | N/A |  |
|  | 7 | 2517.5 | 5 | 25 | 2637.5 | N/A | N/A |  |
|  | n75 | N/A | 5 | N/A | 1474.5 | 17.6 | IMD3 |  |
|  | n78 | 3311 | 10 | 50 | 3311 | N/A | N/A |  |
|  | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n75 | N/A | 5 | N/A | 1492 | 4.9 | IMD4 |  |
| DC_7A_n78A-n79ADC_7A_n78A-n79CDC_7A-7A_n78A-n79A | 7 | 2520 | 5 | 25 | 2640 | N/A | N/A |  |
|  | n78 | 3600 | 10 | 50 | 3600 | N/A | N/A |  |
|  | n79 | N/A | 10 | N/A | 4680 | 20.6 | IMD34,9,13 |  |
|  | 7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3770 | 6.4 | IMD413 |  |
|  | n79 | 4450 | 10 | 50 | 4450 | N/A | N/A |  |
| DC_7A_SUL_n78A-n80A | n80 | 1730 | 5 | 25 |  | N/A | N/A |  |
|  | 7 | N/A | 10 | N/A | 2655 | 13 | IMD4 |  |
| DC_7_n78-n105 | 7 | 2520 | 5 | 25 | 2640 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3700 | 9.7 | IMD4 |  |
|  | n105 | 670 | 5 | 25 | 619 | N/A | N/A |  |
|  | 7 | 2555 | 5 | 25 | 2675 | N/A | N/A |  |
|  | n78 | 3520 | 10 | 50 | 3520 | N/A | N/A |  |
|  | n105 | N/A | 5 | N/A | 625 | 3.9 | IMD5 |  |
| DC_8A_n1A-n28A | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n1 | 1965 | 5 | 25 | 2155 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 765 | 11.6 | IMD4 |  |
| DC_8A_n1A-n40A | 8 | 885 | 5 | 25 | 930 | N/A | N/A |  |
|  | n40 | 2395 | 10 | 50 | 2395 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2135 | 3.3 | IMD5 |  |
| DC_8A_n1A-n77ADC_8B_n1A-n77A | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n1 | 1945 | 5 | 25 | 2135 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3745 | 14.9 | IMD31 |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n77 | 3960 | 10 | 50 | 3960 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2140 | 14.4 | IMD3 |  |
| DC_8A_n1A-n78ADC_8B_n1A-n78A | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n1 | 1945 | 5 | 25 | 2135 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3745 | 14.9 | IMD3 |  |
| DC_8A_n1A-n79A | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n1 | 1955 | 5 | 25 | 2145 | 8.2 | IMD4 |  |
|  | n79 | 4845 | 40 | 216 | 4845 | N/A | N/A |  |
| DC_8A-(n)3AA | 8 | 897.5 | 5 | 25 | 942.5 | N/A | N/A |  |
| DC_8A-(n)3CA | 3 | N/A | 5 | N/A | 1835 | 4.5 | IMD5 |  |
|  | n3 | 1747.5 | 10 | 50 | 1842.5 | 6.4 | IMD5 |  |
| DC_8A_n3A-n28A | 8 | 912.5 | 5 | 25 | 957.5 | N/A | N/A |  |
|  | n3 | 1712.5 | 5 | 25 | 1807.5 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 800 | 30.4 | IMD2 |  |
| DC_8A_n3A-n77ADC_8A_n3A-n77(2A) | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
| DC_8B_n3A-n77A | n3 | 1740 | 5 | 25 | 1835 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3540 | 16.3 | IMD3 |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n77 | 3640 | 10 | 50 | 3640 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1820 | 16.5 | IMD3 |  |
| DC_8A_n3A-n78A | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
| DC_8A_n3A-n78(2A) | n3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3550 | 16.1 | IMD34 |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1820 | 15.7 | IMD3 |  |
|  | n78 | 3640 | 10 | 50 | 3640 | N/A | N/A |  |
| DC_8A_n3A-n79A | 8 | 885 | 5 | 25 | 930 | N/A | N/A |  |
|  | n3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4425 | 15.7 | IMD39 |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n79 | 4580 | 40 | 216 | 4580 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1850 | 8.8 | IMD4 |  |
| DC_8A_n7A-n78A | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n7 | 2555 | 5 | 25 | 2675 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3455 | 28.5 | IMD21 |  |
|  | 8 | 895 | 5 | 25 | 940 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2650 | 28 | IMD2 |  |
|  | n78 | 3545 | 10 | 50 | 3545 | N/A | N/A |  |
| DC_8A-11A_n1A | 11 | 1435 | 5 | 25 | 1483 | N/A | N/A |  |
| DC_8B-11A_n1A | n1 | 1940 | 5 | 25 | 2130 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 930 | 16.6 | IMD35 |  |
| DC_8A-11A_n77A | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
| DC_8A-11A_n77(2A)DC_8B-11A_n77ADC_8B-11A_n77(2A) | n77 | 3311 | 10 | 50 | 3311 | N/A | N/A |  |
|  | 11 | N/A | 5 | N/A | 1491 | 18.8 | IMD3 |  |
|  | 11 | 1430.5 | 5 | 25 | 1478.5 | N/A | N/A |  |
|  | n77 | 3791 | 10 | 50 | 3791 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 930 | 18.2 | IMD3 |  |
| DC_8A-11A_n78A | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n78 | 3311 | 10 | 50 | 3311 | N/A | N/A |  |
|  | 11 | N/A | 5 | N/A | 1491 | 18.8 | IMD3 |  |
|  | 11 | 1430.5 | 5 | 25 | 1478.5 | N/A | N/A |  |
|  | n78 | 3791 | 10 | 50 | 3791 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 930 | 18.2 | IMD3 |  |
| DC_8A-11A_n79A | 8 | 882.5 | 5 | 25 | 927.5 | N/A | N/A |  |
|  | n79 | 4980 | 40 | 216 | 4980 | N/A | N/A |  |
|  | 11 | N/A | 5 | N/A | 1478.4 | 1.2 | IMD5 |  |
|  | 11 | 1435 | 5 | 25 | 1483 | N/A | N/A |  |
|  | n79 | 4810 | 40 | 216 | 4810 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 930 | 2.8 | IMD5 |  |
| DC_8-20_n1 | n1 | 1925 | 5 | 25 | 2115 | N/A | N/A |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | 20 | N/A | 5 | N/A | 805 | 11.5 | IMD4 |  |
| DC_8-20_n3 | n3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | 20 | N/A | 5 | N/A | 810 | 27 | IMD24 |  |
|  | n3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
|  | 8 | 890 | 5 | 25 | 930 | 27 | IMD24 |  |
|  | 20 | 840 | 5 | 25 | 799 | N/A | N/A |  |
| DC_8A-20A_n28A | 8 | N/A | 5 | N/A | 946 | [23.5] | IMD3 |  |
|  | 20 | 837 | 5 | 25 | 796 | N/A | N/A |  |
|  | n28 | 728 | 5 | 25 | 773 | N/A | N/A |  |
| DC_8A-20A_n78A | 8 | 890 | 5 | 25 | 935 | N/A | N/A |  |
|  | n78 | 3470 | 10 | 50 | 3470 | N/A | N/A |  |
|  | 20 | N/A | 5 | N/A | 800 | 12.1 | IMD4 |  |
|  | 8 | N/A | 5 | N/A | 940 | 12.1 | IMD4 |  |
|  | n78 | 3481 | 10 | 50 | 3481 | N/A | N/A |  |
|  | 20 | 847 | 5 | 25 | 806 | N/A | N/A |  |
| DC_8A-28A_n1A | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 780 | 9.4 | IMD4 |  |
|  | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 942 | 3.3 | IMD5 |  |
|  | 28 | 723 | 5 | 25 | 778 | N/A | N/A |  |
|  | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
| DC_8A-28A_n3A | 8 | 912.5 | 5 | 25 | 957.5 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 800 | 30.4 | IMD24 |  |
|  | n3 | 1712.5 | 5 | 25 | 1807.5 | N/A | N/A |  |
| DC_8A-28A_n40A | 8 | N/A | 5 | N/A | 928 | 17.0 | IMD3 |  |
| DC_8A-28C_n40A | 28 | 706 | 5 | 25 | 761 | N/A | N/A |  |
|  | n40 | 2340 | 10 | 50 | 2340 | N/A | N/A |  |
| DC_8A-28A_n77ADC_8A-28A_n77(2A)DC_8A-28C_n77ADC_8A-28C_n77(2A) | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 765 | 11.6 | IMD4 |  |
|  | n77 | 3495 | 10 | 50 | 3495 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 935 | 4.3 | IMD5 |  |
|  | 28 | 713 | 5 | 25 | 768 | N/A | N/A |  |
|  | n77 | 3787 | 10 | 50 | 3787 | N/A | N/A |  |
| DC_8A_n28A-n77A | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3473 | 10.3 | IMD4 |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 765 | 11.6 | IMD4 |  |
|  | n77 | 3495 | 10 | 50 | 3495 | N/A | N/A |  |
| DC_8A_n28A-n78A | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
| DC_8A_n28A-n78(2A) | n28 | 725 | 5 | 25 | 780 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3455 | 10.3 | IMD4 |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 765 | 11.6 | IMD4 |  |
|  | n78 | 3495 | 10 | 50 | 3495 | N/A | N/A |  |
| DC_8A_n28A-n79A | 8 | 912.5 | 5 | 25 | 957.5 | N/A | N/A |  |
|  | n28 | 745.5 | 5 | 25 | 800.5 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4420 | 0.0 | IMD5 |  |
|  | 8 | 905 | 5 | 25 | 950 | N/A | N/A |  |
|  | n79 | 4420 | 40 | 216 | 4420 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 800 | 3.9 | IMD5 |  |
| DC_8A-32A_n78A | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n78 | 3311 | 10 | 50 | 3311 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1491 | 18.8 | IMD3 |  |
| DC_8A-38A_n28A | 8 | 912.5 | 5 | 25 | 957.5 | N/A | N/A |  |
|  | 38 | N/A | 10 | N/A | 2575 | 14.4 | IMD3 |  |
|  | n28 | 745.5 | 5 | 25 | 800.5 | N/A | N/A |  |
| DC_8A-38A_n78A | 8 | 897.5 | 5 | 25 | 942.5 | N/A | N/A |  |
|  | 38 | N/A | 5 | N/A | 2602.5 | 28 | IMD2 |  |
|  | n78 | 3500 | 10 | 50 | 3500 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 927.5 | 29 | IMD2 |  |
|  | 38 | 2572.5 | 5 | 25 | 2572.5 | N/A | N/A |  |
|  | n78 | 3500 | 10 | 50 | 3500 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 937.5 | 3.1 | IMD5 |  |
|  | 38 | 2572.5 | 5 | 25 | N/A | N/A | N/A |  |
|  | n78 | 3390 | 10 | 50 | N/A | N/A | N/A |  |
| DC_8A-39A_n40A | 8 | 895 | 5 | 25 | 940 | 8.6 | IMD4 |  |
|  | 39 | 1900 | 5 | 25 | 1900 | N/A | N/A |  |
|  | n40 | 2370 | 10 | 50 | 2370 | N/A | N/A |  |
|  | 8 | 885 | 5 | 25 | 930 | 4.9 | IMD5 |  |
|  | 39 | 1890 | 5 | 25 | 1890 | N/A | N/A |  |
|  | n40 | 2370 | 10 | 50 | 2370 | N/A | N/A |  |
| DC_8-39_n79 | 8 | 897.5 | 5 | 25 | 942.5 | N/A | N/A |  |
|  | 39 | N/A | 5 | N/A | 1907.5 | 13.8 | IMD4 |  |
|  | n79 | 4600 | 40 | 216 | 4600 | N/A | N/A |  |
|  | 8 | 895 | 5 | 25 | 940 | 15.1 | IMD3 |  |
|  | 39 | 1900 | 10 | 50 | 1900 | N/A | N/A |  |
|  | n79 | 4740 | 40 | 216 | 4740 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 940 | 7.1 | IMD4 |  |
|  | 39 | 1900 | 5 | 25 | 1900 | N/A | N/A |  |
|  | n79 | 4760 | 40 | 216 | 4760 | N/A | N/A |  |
| DC_8A_n39A-n79A | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n39 | 1890 | 10 | 50 | 1890 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4680 | 15.9 | IMD3 |  |
|  | 8 | 890 | 5 | 25 | 935 | N/A | N/A |  |
|  | n39 | 1890 | 10 | 50 | 1890 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4560 | 12.1 | IMD4 |  |
|  | 8 | 897.5 | 5 | 25 | 942.5 | N/A | N/A |  |
|  | n39 | N/A | 10 | N/A | 1907.5 | 13.8 | IMD4 |  |
|  | n79 | 4600 | 40 | 216 | 4600 | N/A | N/A |  |
| DC_8A-40A_n1ADC_8A-40C_n1A | 8 | N/A | 5 | N/A | 930 | 8.0 | IMD4 |  |
|  | 40 | 2395 | 5 | 25 | 2395 | N/A | N/A |  |
|  | n1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
| DC_8A-40A_n28A | 8 | 895 | 5 | 25 | 940 | N/A | N/A |  |
|  | 40 | N/A | 5 | N/A | 2335 | 18.8 | IMD3 |  |
|  | n28 | 720 | 5 | 25 | 775 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 928 | 17.0 | IMD3 |  |
|  | 40 | 2340 | 5 | 25 | 2340 | N/A | N/A |  |
|  | n28 | 706 | 5 | 25 | 761 | N/A | N/A |  |
| DC_8A_n40A-n41ADC_8A_n40A-n41C | 8 | 895 | 5 | 25 | 940 | N/A | N/A |  |
|  | n40 | 2355 | 10 | 50 | 2355 | 4.9 | IMD5 |  |
|  | n41 | N/A | 10 | N/A | 2520 | N/A | N/A |  |
| DC_8_n40-n71 | 8 | 882.5 | 5 | 25 | 927.5 | N/A | N/A |  |
|  | n40 | 2395 | 10 | 50 | 2395 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 632.5 | 17 | IMD3 |  |
|  | 8 | 912.5 | 5 | 25 | 957.5 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2305 | 18 | IMD3 |  |
|  | n71 | 695 | 5 | 25 | 649 | N/A | NA |  |
| DC_28A_n40A-n77A | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
| DC_28C_n40A-n77A | n40 | N/A | 10 | N/A | 2395 | 28 | IMD21 |  |
|  | n77 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n40 | 2395 | 10 | 50 | 2395 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3305 | 28.8 | IMD21 |  |
| DC_8A-40A_n78ADC_8A-40C_n78A | 8 | N/A | 5 | N/A | 950 | 30.5 | IMD2 |  |
|  | 40 | 2380 | 5 | 25 | 2380 | N/A | N/A |  |
|  | n78 | 3330 | 10 | 50 | 3330 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 935 | 19.8 | IMD3 |  |
|  | 40 | 2320 | 5 | 25 | 2320 | N/A | N/A |  |
|  | n78 | 3705 | 10 | 50 | 3705 | N/A | N/A |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | 40 | N/A | 5 | N/A | 2395 | 28 | IMD2 |  |
|  | n78 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
| DC_8A_n40A-n78A | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n40 | 2395 | 10 | 50 | 2395 | N/A | N/A |  |
|  | n78 | 3305 | 10 | 50 | 3307.5 | 28.7 | IMD21 |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n40 | 2395 | 10 | 50 | 2395 | 27.3 | IMD2 |  |
|  | n78 | 3305 | 10 | 50 | 3305 | N/A | N/A |  |
| DC_8A_n40A-n79A | 8 | 885 | 5 | 25 | 930 | N/A | N/A |  |
|  | n40 | 2305 | 10 | 50 | 2305 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4960 | 10.7 | IMD4 |  |
|  | 8 | 885 | 5 | 25 | 930 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2305 | 9.2 | IMD4 |  |
|  | n79 | 4960 | 40 | 216 | 4960 | N/A | N/A |  |
| DC_8A-41A_n1A | 41 | 2500 | 5 | 25 | 2500 | N/A | N/A |  |
| DC_8A-41C_n1A | n1 | 1977 | 5 | 25 | 2167 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 931 | 4.5 | IMD5 |  |
| DC_8A-41A_n3A | n3 | 1780 | 5 | 25 | 1875 | N/A | N/A |  |
| DC_8A-41C_n3A | 8 | 885 | 5 | 25 | 930 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2665 | 27.4 | IMD21 |  |
|  | n3 | 1715 | 5 | 25 | 1810 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 950 | 28.9 | IMD21 |  |
|  | 41 | 2665 | 5 | 25 | 2665 | N/A | N/A |  |
| DC_8A-41A_n77A | 8 | N/A | 5 | N/A | 950 | 29.1 | IMD21, 4 |  |
| DC_8A-41C_n77A | 41 | 2630 | 10 | 50 | 2630 | N/A | N/A |  |
|  | n77 | 3580 | 10 | 50 | 3580 | N/A | N/A |  |
|  | 8 | 895 | 5 | 25 | 940 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2650 | 28.0 | IMD2 |  |
|  | n77 | 3545 | 10 | 50 | 3545 | N/A | N/A |  |
| DC_8A-41A_n78A | 8 | N/A | 5 | N/A | 950 | 29.1 | IMD24 |  |
| DC_8A-41C_n78A | 41 | 2630 | 5 | 25 | 2630 | N/A | N/A |  |
|  | n78 | 3580 | 10 | 50 | 3580 | N/A | N/A |  |
|  | 8 | 895 | 5 | 25 | 940 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2650 | 28.0 | IMD2 |  |
|  | n78 | 3545 | 10 | 50 | 3545 | N/A | N/A |  |
| DC_8A_n41A-n78A | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n41 | 2555 | 10 | 50 | 2555 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3455 | 27 | IMD21 |  |
|  | 8 | 895 | 5 | 25 | 940 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2650 | 26 | IMD2 |  |
|  | n78 | 3545 | 10 | 50 | 3545 | N/A | N/A |  |
| DC_8A_n41A-n79A | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n41 | 2650 | 10 | 50 | 2650 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4470 | 16.3 | IMD3 |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2650 | 15.5 | IMD3 |  |
|  | n79 | 4470 | 40 | 216 | 4470 | N/A | N/A |  |
| DC_8A-42A_n1A | 42 | 3405 | 10 | 50 | 3405 | N/A | N/A |  |
| DC_8A-42C_n1A | n1 | 1955 | 5 | 25 | 2145 | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 945 | 3.3 | IMD5 |  |
| DC_8A-42A_n3A | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n3 | 1740 | 5 | 25 | 1835 | N/A | N/A |  |
|  | 42 | N/A | 5 | N/A | 3540 | 16.3 | IMD3 |  |
| DC_8A-42A_n28A | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | 42 | N/A | 5 | N/A | 3443 | 8.7 | IMD4 |  |
| DC_8A-42A_n79A | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n79 | 4470 | 40 | 216 | 4470 | N/A | N/A |  |
|  | 42 | N/A | 5 | N/A | 3570 | 34.8 | IMD2 |  |
| DC_8A_n71A-n77A | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n71 | 674 | 5 | 25 | 628 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3404 | 10.3 | IMD4 |  |
|  | 8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n71 | 674 | 5 | 25 | 628 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3606 | 4 | IMD5 |  |
|  | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 634.5 | 11.6 | IMD4 |  |
|  | n77 | 3334.5 | 10 | 50 | 3334.5 | N/A | N/A |  |
|  | 8 | 882.5 | 5 | 25 | 927.5 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 640 | 14.49 | IMD5 |  |
|  | n77 | 4170 | 10 | 50 | 4170 | N/A | N/A |  |
| DC_8A_SUL_n78A-n80A | n80 | 1755 | 10 | 50 | N/A | N/A | N/A |  |
|  | 8 | N/A | 5 | N/A | 945 | 8 | IMD4 |  |
|  | n80 | 1750 | 10 | 50 | N/A | N/A | N/A |  |
|  | 8 | 900 | 5 | 25 | 945 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3550 | 8 | IMD33 |  |
| DC_11A_n1A-n3A | 11 | 1430 | 5 | 25 | 1478 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2130 | 17.7 | IMD3 |  |
|  | n3 | 1780 | 5 | 25 | 1875 | N/A | N/A |  |
| DC_11A_n1A-n77ADC_11A_n1A-n77(2A) | 11 | 1435 | 5 | 25 | 1483 | N/A | N/A |  |
|  | n1 | 1940 | 5 | 25 | 2130 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3375 | 29.6 | IMD21 |  |
|  | 11 | 1438 | 5 | 25 | 1486 | N/A | N/A |  |
|  | n77 | 3578 | 10 | 50 | 3578 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2140 | 30.8 | IMD21 |  |
| DC_11A_n3A-n28A | 11 | 1435 | 5 | 25 | 1483 | N/A | N/A |  |
|  | n3 | 1753 | 5 | 25 | 1848 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 800 | 3.0 | IMD5 |  |
| DC_11A_n3A-n77ADC_11A_n3A-n77(2A) | 11 | 1440 | 5 | 25 | 1488 | N/A | N/A |  |
|  | n3 | 1740 | 5 | 25 | 1835 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3780 | 10.8 | IMD4 |  |
|  | 11 | 1440 | 5 | 25 | 1488 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1870 | 29.0 | IMD2 |  |
|  | n77 | 3310 | 10 | 50 | 3310 | N/A | N/A |  |
| DC_11A_n3A-n79A | 11 | 1435 | 5 | 25 | 1483 | N/A | N/A |  |
|  | n3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4640 | 16.2 | IMD3 |  |
|  | 11 | 1435 | 5 | 25 | 1483 | N/A | N/A |  |
|  | n79 | 4735 | 40 | 216 | 4735 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1865 | 17.8 | IMD3 |  |
| DC_11A-18A_n77A | 11 | 1443 | 5 | 25 | 1491 | N/A | N/A |  |
| DC_11A-18A_n77(2A) | n77 | 3706 | 10 | 50 | 3706 | N/A | N/A |  |
|  | 18 | N/A | 5 | N/A | 865 | 18.7 | IMD3 |  |
| DC_11A-18A_n78A | 11 | 1443 | 5 | 25 | 1491 | N/A | N/A |  |
| DC_11A-18A_n78(2A) | n78 | 3706 | 10 | 50 | 3706 | N/A | N/A |  |
|  | 18 | N/A | 5 | N/A | 865 | 18.7 | IMD3 |  |
| DC_11A_n28A-n77ADC_11A_n28A-n77(2A) | 11 | 1443 | 5 | 25 | 1491 | N/A | N/A |  |
|  | n28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3629 | 17.5 | IMD3 |  |
|  | 11 | 1443 | 5 | 25 | 1491 | N/A | N/A |  |
|  | n77 | 3684 | 10 | 50 | 3684 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 798 | 15.8 | IMD3 |  |
| DC_12A_n2A-n7A | 12 | 713.5 | 5 | 25 | 743.5 | N/A | N/A |  |
|  | n2 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2622.5 | 30.8 | IMD2 |  |
| DC_12A_n2A-n38A | 12 | 708 | 5 | 25 | 738 | N/A | N/A |  |
|  | n2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n38 | N/A | 10 | N/A | 2608 | 28.7 | IMD2 |  |
| DC_12A_n2A-n41A | 12 | 708 | 5 | 25 | 738 | N/A | N/A |  |
|  | n2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2608 | 26.7 | IMD2 |  |
| DC_12A_n2A-n66A | 12 | 713.5 | 5 | 25 | 743.5 | N/A | N/A |  |
|  | n2 | 1907.5 | 5 | 25 | 1987.5 | 2 | IMD4 |  |
|  | n66 | 1712.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
| DC_12A_n2A-n77A | 12 | 707.5 | 5 | 25 | 737.5 | N/A | N/A |  |
|  | n2 | 1880 | 5 | 25 | 1960 | 16.5 | IMD3 |  |
|  | n77 | 3375 | 10 | 50 | 3375 | N/A | N/A |  |
|  | 12 | 710 | 5 | 25 | 740 | N/A | N/A |  |
|  | n2 | 1890 | 5 | 25 | 1970 | 12 | IMD4 |  |
|  | n77 | 4100 | 10 | 50 | 4100 | N/A | N/A |  |
|  | 12 | 707.5 | 5 | 25 | 737.5 | N/A | N/A |  |
|  | n2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n77 | 3315 | 10 | 50 | 3315 | 16.0 | IMD34, |  |
|  | 12 | 710 | 5 | 25 | 740 | N/A | N/A |  |
|  | n2 | 1870 | 5 | 25 | 1950 | N/A | N/A |  |
|  | n77 | 4000 | 10 | 50 | 4000 | 12 | IMD4 |  |
| DC_12_n2-n78 | 12 | 707.5 | 5 | 25 | 737.5 | N/A | N/A |  |
|  | n2 | N/A | 5 | N/A | 1960 | 16.5 | IMD3 |  |
|  | n78 | 3375 | 10 | 50 | 3375 | N/A | N/A |  |
|  | 12 | 707.5 | 5 | 25 | 737.5 | N/A | N/A |  |
|  | n2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3315 | 16.0 | IMD3 |  |
| DC_12A_n7A-n25A | 12 | 713.5 | 5 | 25 | 743.5 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2626 | 30.8 | IMD2 |  |
|  | n25 | 1912.5 | 5 | 25 | 1992.5 | N/A | N/A |  |
| DC_12A_n7A-n77A | 12 | 708 | 5 | 25 | 738 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2662 | 29.6 | IMD2 |  |
|  | n77 | 3370 | 10 | 50 | 3370 | N/A | N/A |  |
|  | 12 | 708 | 5 | 25 | 738 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2670 | 13.2 | IMD3 |  |
|  | n77 | 4086 | 10 | 50 | 4086 | N/A | N/A |  |
|  | 12 | 702 | 5 | 25 | 732 | N/A | N/A |  |
|  | n7 | 2505 | 5 | 25 | 2625 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3909 | 16.0 | IMD3 |  |
|  | 12 | 673 | 5 | 25 | 732 | N/A | N/A |  |
|  | n7 | 2505 | 5 | 25 | 2625 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3664 | 10.3 | IMD4 |  |
| DC_12A_n7A-n78ADC_12A_n7(2A)-n78ADC_12A_n7A-n78(2A)DC_12A_n7(2A)-n78(2A) | 12 | 708 | 5 | 25 | 738 | N/A | N/A |  |
|  | n7 | 2520 | 5 | 25 | 2640 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3624 | 9 | IMD4 |  |
|  | 12 | 708 | 5 | 25 | 738 | N/A | N/A |  |
|  | n78 | 3370 | 10 | 50 | 3370 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2662 | 29.6 | IMD2 |  |
| DC_12A_n25A-n41A | 12 | 708 | 5 | 25 | 738 | N/A | N/A |  |
|  | n25 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2608 | 26.7 | IMD2 |  |
|  | 12 | 710 | 5 | 25 | 740 | N/A | N/A |  |
|  | n25 | N/A | 5 | N/A | 1970 | 26 | IMD2 |  |
|  | n41 | 2680 | 10 | 50 | 2680 | N/A | N/A |  |
| DC_12A_n25A-n77A | 12 | 707.5 | 5 | 25 | 737.5 | N/A | N/A |  |
|  | n25 | N/A | 5 | N/A | 1960 | 16.5 | IMD3 |  |
|  | n77 | 3375 | 10 | 50 | 3375 | N/A | N/A |  |
|  | 12 | 710 | 5 | 25 | 740 | N/A | N/A |  |
|  | n25 | N/A | 5 | N/A | 1970 | 12.5 | IMD4 |  |
|  | n77 | 4100 | 10 | 50 | 4100 | N/A | N/A |  |
|  | 12 | 707.5 | 5 | 25 | 737.5 | N/A | N/A |  |
|  | n25 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3315 | 16.0 | IMD3 |  |
|  | 12 | 710 | 5 | 25 | 740 | N/A | N/A |  |
|  | n25 | 1870 | 5 | 25 | 1950 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 4000 | 12 | IMD4 |  |
| DC_12A-30A_n2A | 12 | 708.5 | 5 | 25 | 738.5 | N/A | N/A |  |
|  | 30 | N/A | 5 | N/A | 2353 | 12.0 | IMD4 |  |
|  | n2 | 1885 | 5 | 25 | 1965 | N/A | N/A |  |
| DC_12A-30A_n5A | 12 | 702 | 5 | 25 | 732 | N/A | N/A |  |
|  | 30 | N/A | 5 | N/A | 2355 | 18.8 | IMD3 |  |
|  | n5 | 826.5 | 5 | 25 | 871.5 | N/A | N/A |  |
| DC_12A-30A_n77ADC_12A-30A_n77(2A) | 12 | N/A | 5 | N/A | 740 | 15.2 | IMD34 |  |
|  | 30 | 2310 | 5 | 25 | 2355 | N/A | N/A |  |
|  | n77 | 3880 | 10 | 50 | 3880 | N/A | N/A |  |
|  | 12 | 707.5 | 5 | 25 | 737.5 | N/A | N/A |  |
|  | 30 | N/A | 5 | N/A | 2355 | 13.2 | IMD3 |  |
|  | n77 | 3770 | 10 | 50 | 3770 | N/A | N/A |  |
| DC_12A_n41A-n66A | 12 | 713.5 | 5 | 25 | 743.5 | N/A | N/A |  |
|  | n41 | 2501 | 10 | 50 | 2501 | 20.0 | IMD218 |  |
|  | n66 | 1777.5 | 5 | 25 | 2177.5 | N/A | N/A |  |
| DC_12A-66A_n5ADC_12A-66A-66A_n5A | 12 | N/A | 5 | N/A | 742 | 9.4 | IMD4 |  |
|  | 66 | 1745 | 5 | 25 | 2145 | N/A | N/A |  |
|  | n5 | 829 | 5 | 25 | 874 | N/A | N/A |  |
| DC_12A-66A_n7A | 12 | N/A | 5 | N/A | 742 | 31 | IMD2 |  |
|  | 66 | 1773 | 5 | 25 | 2173 | N/A | N/A |  |
|  | n7 | 2515 | 5 | 25 | 2635 | N/A | N/A |  |
| DC_12A-66A_n25A | 12 | 708.5 | 5 | 25 | 738.5 | N/A | N/A |  |
|  | 66 | 1775 | 5 | 25 | 2175 | N/A | N/A |  |
|  | n25 | N/A | 5 | N/A | 1935 | 20 | IMD3 |  |
|  | 12 | 708.5 | 5 | 25 | 738.5 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2112.5 | 23 | IMD34 |  |
|  | n25 | 1912.5 | 5 | 25 | 1992.5 | N/A | N/A |  |
| DC_12A-66A_n41A | 12 | N/A | 5 | N/A | 742 | 29.5 | IMD2 |  |
|  | 66 | 1773 | 5 | 25 | 2173 | N/A | N/A |  |
|  | n41 | 2515 | 10 | 50 | 2515 | N/A | N/A |  |
| DC_12A-66A_n77ADC_12A-66A_n77(2A) | 12 | N/A | 5 | N/A | 740 | 15.2 | IMD311 |  |
| DC_12A-66A-66A_n77A | 66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
| DC_12A-66A-66A_n77(2A) | n77 | 4180 | 10 | 50 | 4180 | N/A | N/A |  |
|  | 12 | 707 | 5 | 25 | 737 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2126 | 13.2 | IMD3 |  |
|  | n77 | 3540 | 10 | 50 | 3540 | N/A | N/A |  |
| DC_12A_n66A-n77A | 12 | 707 | 5 | 25 | 737 | N/A | N/A |  |
|  | n66 | 1726 | 5 | 25 | 2126 | 13.2 | IMD3 |  |
|  | n77 | 3540 | 10 | 50 | 3540 | N/A | N/A |  |
|  | 12 | 704 | 5 | 25 | 734 | N/A | N/A |  |
|  | n66 | 1723 | 5 | 25 | 2123 | N/A | N/A |  |
|  | n77 | 4150 | 10 | 50 | 4150 | 16.0 | IMD32,4 |  |
|  | 12 | 709 | 5 | 25 | 739 | N/A | N/A |  |
|  | n66 | 1715 | 5 | 25 | 2115 | N/A | N/A |  |
|  | n77 | 3842 | 10 | 50 | 3842 | 9 | IMD4 |  |
| DC_12A-66A_n78A | 12 | 710 | 5 | 25 | 740 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2160 | 17.1 | IMD3 |  |
|  | n78 | 3580 | 5 | 25 | 3580 | N/A | N/A |  |
| DC_12A_n66A-n78ADC_12A_n66(2A)-n78ADC_12A_n66A-n78(2A)DC_12A_n66(2A)-n78(2A) | 12 | 703 | 5 | 25 | 733 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2140 | 16.5 | IMD3 |  |
|  | n78 | 3546 | 10 | 50 | 3546 | N/A | N/A |  |
|  | 12 | 703 | 5 | 25 | 733 | N/A | N/A |  |
|  | n66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3754 | 4.1 | IMD5 |  |
| DC_13A_n2A-n77A | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
|  | n2 | 1896 | 5 | 25 | 1976 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3460 | 17.3 | IMD3 |  |
|  | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
|  | n2 | N/A | 5 | N/A | 1960 | 16.0 | IMD3 |  |
|  | n77 | 3524 | 10 | 50 | 3524 | N/A | N/A |  |
| DC_13A_n5A-n77A11 | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
|  | n77 | 4013 | 10 | 50 | 4013 | N/A | N/A |  |
|  | n5 | N/A | 5 | N/A | 885 | 4.5 | IMD5 |  |
| DC_13A_n7A-n78A | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
|  | n78 | 3432 | 10 | 50 | 3432 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2650 | 27.9 | IMD2 |  |
|  | 13 | 749 | 5 | 25 | 780 | N/A | N/A |  |
|  | n7 | 2560 | 5 | 25 | 2680 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3622 | 9 | IMD4 |  |
|  | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
|  | n7 | 2530 | 5 | 25 | 2650 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3312 | 29.0 | IMD2 |  |
| DC_13A_n25A-n66A | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
|  | n25 | 1860 | 5 | 25 | 1940 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2156 | 7.2 | IMD4 |  |
|  | 13 | 780 | 5 | 25 | 749 | N/A | N/A |  |
|  | n25 | N/A | 5 | N/A | 1940 | 6.2 | IMD4 |  |
|  | n66 | 1750 | 5 | 25 | 2150 | N/A | N/A |  |
| DC_13A-46A_n2A5 | 13 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 46 | N/A | N/A | N/A | N/A | N/A | IMD4 |  |
|  | n2 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_13A-46A_n66A5 | 13 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 46 | N/A | N/A | N/A | N/A | N/A | IMD4,IMD5 |  |
|  | n66 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_13A-46A_n77A5DC_13A-46A-46A_n77A5 | 13 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 46 | N/A | N/A | N/A | N/A | N/A | IMD3,IMD4,IMD5 |  |
|  | n77 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_13A_n48A-n66A | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
|  | n48 | N/A | 5 | N/A | 3584 | 2.8 | IMD5 |  |
|  | n66 | 1716 | 5 | 25 | 2116 | N/A | N/A |  |
|  | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
|  | n48 | 3695 | 5 | 25 | 3695 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2131 | 17.1 | IMD3 |  |
| DC_13A-66A_n2ADC_13A-66A-66A_n2A | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
| DC_13A-66B_n2A | 66 | N/A | 5 | N/A | 2156 | 7..2 | IMD4 |  |
| DC_13A-66C_n2A | n2 | 1860 | 5 | 25 | 1940 | N/A | N/A |  |
| DC_13A-66A_n5A | 13 | N/A | 5 | N/A | 750 | 9.4 | IMD4 |  |
| DC_13A-66A-66A_n5A | 66 | 1770 | 5 | 25 | 2170 | N/A | N/A |  |
|  | n5 | 840 | 5 | 25 | 885 | N/A | N/A |  |
| DC_13A-66A_n48ADC_13A-66A_n48BDC_13A-66A-66A_n48ADC_13A-66A-66A_n48B | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2131 | 17.1 | IMD3 |  |
|  | n48 | 3695 | 10 | 50 | 3695 | N/A | N/A |  |
| DC_13A-66A_n77A | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
| DC_13A-66A_n77CDC_13A-66A-66A_n77ADC_13A-66A-66A_n77C | 66 | N/A | 5 | N/A | 2156 | 17.1 | IMD3 |  |
|  | n77 | 3720 | 10 | 50 | 3720 | N/A | N/A |  |
| DC_13A-66A_n77A11 | 13 | N/A | 5 | N/A | 750 | 15.2 | IMD3 |  |
| DC_13A-66A_n77C11DC_13A-66A-66A_n77A11DC_13A-66A-66A_n77C11 | 66 | 1710 | 5 | 25 | 2110 | N/A | N/A |  |
|  | n77 | 4170 | 10 | 50 | 4170 | N/A | N/A |  |
| DC_13A_n66A-n77A | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
|  | n66 | 1731 | 5 | 25 | 2131 | 17.1 | IMD3 |  |
|  | n77 | 3695 | 10 | 50 | 3695 | N/A | N/A |  |
|  | 13 | 782 | 5 | 25 | 751 | N/A | N/A |  |
|  | n66 | 1760 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n77 | 3324 | 10 | 50 | 3324 | 16.4 | IMD34,9 |  |
| DC_14A-30A_n5A | 14 | 795 | 5 | 25 | 765 | N/A | N/A |  |
|  | 30 | N/A | 5 | N/A | 2353 | 5.9 | IMD5 |  |
|  | n5 | 827 | 5 | 25 | 872 | N/A | N/A |  |
| DC_14A-30A_n77ADC_14A-30A_n77(2A) | 14 | N/A | 5 | N/A | 763 | 15.2 | IMD34 |  |
|  | 30 | 2310 | 5 | 25 | 2355 | N/A | N/A |  |
|  | n77 | 3857 | 10 | 50 | 3857 | N/A | N/A |  |
|  | 14 | 793 | 5 | 25 | 763 | N/A | N/A |  |
|  | 30 | N/A | 5 | N/A | 2355 | 13.2 | IMD3 |  |
|  | n77 | 3941 | 10 | 50 | 3941 | N/A | N/A |  |
| DC_14A-66A_n2ADC_14A-66A-66A_n2A | 14 | 793 | 5 | 25 | 763 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2162 | 7.6 | IMD4 |  |
|  | n2 | 1874 | 5 | 25 | 1954 | N/A | N/A |  |
| DC_14A-66A_n5A | 14 | N/A | 5 | N/A | 762 | 9.4 | IMD4 |  |
|  | 66 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n5 | 834 | 5 | 25 | 879 | N/A | N/A |  |
| DC_14A-66A_n77ADC_14A-66A_n77(2A) | 14 | N/A | 5 | N/A | 763 | 15.2 | IMD311 |  |
| DC_14A-66A-66A_n77A | 66 | 1712.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
| DC_14A-66A-66A_n77(2A) | n77 | 4188 | 10 | 50 | 4188 | N/A | N/A |  |
|  | 14 | 793 | 5 | 25 | 763 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2155 | 13.2 | IMD3 |  |
|  | n77 | 3741 | 10 | 50 | 3741 | N/A | N/A |  |
| DC_18A_n3A-n41A | 18 | 820 | 5 | 25 | 865 | N/A | N/A |  |
|  | n3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2540 | 29.4 | IMD2 |  |
|  | 18 | 820 | 5 | 25 | 865 | N/A | N/A |  |
|  | n41 | 2670 | 10 | 50 | 2670 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1850 | 28.2 | IMD2 |  |
| DC_18A_n3A-n77A | 18 | 820 | 5 | 25 | 865 | N/A | N/A |  |
|  | n3 | 1770 | 5 | 25 | 1865 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3410 | 16.3 | IMD3 |  |
|  | 18 | 820 | 5 | 25 | 865 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1865 | 15.7 | IMD3 |  |
|  | n77 | 3505 | 10 | 50 | 3505 | N/A | N/A |  |
| DC_18A_n3A-n78A | 18 | 820 | 5 | 25 | 865 | N/A | N/A |  |
|  | n3 | 1750 | 5 | 25 | 1845 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3390 | 15.2 | IMD33 |  |
| DC_18A-28A_n77ADC_18A_n28A-n77A | 18 | 820 | 5 | 25 | 865 | N/A | N/A |  |
|  | 28/n28 | N/A | 5 | N/A | 778 | 4.4 | IMD5 |  |
|  | n77 | 4058 | 10 | 50 | 4058 | N/A | N/A |  |
| DC_18A-28A_n77A | 18 | N/A | 5 | N/A | 865 | 3.9 | IMD5 |  |
|  | 28 | 723 | 5 | 25 | 778 | N/A | N/A |  |
|  | n77 | 3757 | 10 | 50 | 3757 | N/A | N/A |  |
| DC_18A-28A_n78A | 18 | N/A | 5 | N/A | 864 | 3.8 | IMD5 |  |
|  | 28 | 723 | 5 | 25 | 778 | N/A | N/A |  |
|  | n78 | 3756 | 10 | 50 | 3756 | N/A | N/A |  |
| DC_18A_n28A-n77ADC_18A_n28A-n78A | 18 | 820 | 5 | 25 | 865 | N/A | N/A |  |
|  | n28 | 710 | 5 | 25 | 765 | N/A | N/A |  |
|  | n77/n78 | N/A | 10 | N/A | 3770 | 4.0 | IMD5 |  |
| DC_18A-41A_n3ADC_18A-41C_n3A | 18 | 820 | 5 | 25 | 865 | N/A | N/A |  |
|  | n3 | 1725 | 5 | 25 | 1820 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2630 | 16.0 | IMD3 |  |
|  | 18 | N/A | 5 | N/A | 865 | 28.9 | IMD21 |  |
|  | n3 | 1765 | 5 | 25 | 1860 | N/A | N/A |  |
|  | 41 | 2630 | 5 | 25 | 2630 | N/A | N/A |  |
| DC_18A-41A_n77ADC_18A-41C_n77A | 18 | N/A | 5 | N/A | 865 | 3.4 | IMD5 |  |
|  | n77 | 3527.5 | 10 | 50 | 3527.5 | N/A | N/A |  |
|  | 41 | 2640 | 5 | 25 | 2640 | N/A | N/A |  |
| DC_18A_n41A-n77ADC_18A_n41A-n77(2A)DC_18A_n41A-n78A | 18 | 820 | 5 | 25 | 865 | N/A | N/A |  |
| DC_18A_n41A-n78(2A) | n41 | 2570 | 10 | 50 | 2570 | N/A | N/A |  |
|  | n77/n78 | N/A | 10 | N/A | 3390 | 28.6 | IMD2 |  |
|  | 18 | 820 | 5 | 25 | 865 | N/A | N/A |  |
|  | n77/n78 | 3450 | 10 | 50 | 3450 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2630 | 26.5 | IMD2 |  |
| DC_18A-41A_n78ADC_18A-41C_n78A | 18 | N/A | 5 | N/A | 865 | 3.4 | IMD5 |  |
|  | n78 | 3527.5 | 10 | 50 | 3527.5 | N/A | N/A |  |
|  | 41 | 2640 | 5 | 25 | 2640 | N/A | N/A |  |
| DC_19A_n1A-n77ADC_19A_n1A-n78A | 19 | 840 | 5 | 25 | 885 | N/A | N/A |  |
|  | n1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | n77/n78 | N/A | 10 | N/A | 3655 | [21.4] | IMD3 |  |
|  | 19 | 832.5 | 5 | 25 | 877.5 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2130 | 17.8 | IMD3 |  |
|  | n77/n78 | 3795 | 10 | 50 | 3795 | N/A | N/A |  |
| DC_19A_n1A-n79A20 |  |  |  | N/A |  |  |  |  |
| DC_19A-21A_n77ADC_19A-21A_n78A | 19 | N/A | 5 | N/A | 882.5 | 18.7 | IMD3 |  |
|  | 21 | 1450.4 | 5 | 25 | 1498.4 | N/A | N/A |  |
|  | n77, n78 | 3783.3 | 10 | 50 | 3783.3 | N/A | N/A |  |
|  | 19 | N/A | 5 | N/A | 882.5 | 13.2 | IMD4 |  |
|  | 21 | 1450.4 | 5 | 25 | 1498.4 | N/A | N/A |  |
|  | n77, n78 | 3468.7 | 10 | 50 | 3468.7 | N/A | N/A |  |
| DC_19A-21A_n77A | 19 | 837.5 | 5 | 25 | 882.5 | N/A | N/A |  |
|  | 21 | N/A | 5 | N/A | 1502.5 | 9.0 | IMD4 |  |
|  | n77 | 4015 | 10 | 50 | 4015 | N/A | N/A |  |
| DC_19A-21A_n79A | 19 | N/A | N/A | N/A | N/A | N/A | IMD5 |  |
|  | 21 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | n79 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 19 | 837.5 | 5 | 25 | 882.5 | N/A | N/A |  |
|  | 21 | N/A | 5 | N/A | 1500 | 3.8 | IMD5 |  |
|  | n79 | 4850 | 40 | 216 | 4850 | N/A | N/A |  |
| DC_19A_n78A-n79A | 19 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | n78 | 3680 | 10 | 50 | 3680 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4515 | 29.3 | IMD2 |  |
|  | 19 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | n79 | 4550 | 40 | 216 | 4550 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3715 | 28.8 | IMD2 |  |
| DC_20A-n1A_n75A | n1 | 1950.5 | 5 | 50 | 2140.5 | N/A | N/A |  |
|  | 20 | 852.5 | 5 | 25 | 811.5 | N/A | N/A |  |
|  | n75 | N/A | 5 | N/A | 1459.5 | 4.0 | IMD5 |  |
| DC_20A_n1A-n78A | 20 | 845 | 5 | 25 | 804 | N/A | N/A |  |
|  | n1 | 1940 | 5 | 25 | 2130 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3630 | 16.0 | IMD3 |  |
|  | 20 | 835 | 5 | 25 | 794 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2120 | 15.3 | IMD3 |  |
|  | n78 | 3790 | 10 | 50 | 3790 | N/A | N/A |  |
| DC_20A-(n)3AA | 3 | N/A | 5 | N/A | 1865 | 3 | IMD4 |  |
|  | n3 | 1775 | 5 | 25 | 1870 | 4 | IMD4 |  |
|  | 20 | 840 | 5 | 25 | 799 | N/A | N/A |  |
| DC_20_n3-n67 | 20 | 837 | 5 | 25 | 796 | N/A | N/A |  |
|  | n3 | 1765 | 5 | 25 | 1860 | N/A | N/A |  |
|  | n67 | N/A | 5 | N/A | 746 | 9.4 | IMD4 |  |
| DC_20A_n3A-n78A | 20 | 845 | 5 | 25 | 804 | N/A | N/A |  |
|  | n3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3420 | 16.1 | IMD3 |  |
|  | 20 | 845 | 5 | 25 | 804 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1860 | 15.7 | IMD3 |  |
|  | n78 | 3550 | 10 | 50 | 3550 | N/A | N/A |  |
| DC_20A_n7A-n28A | 20 | 857 | 5 | 25 | 816 | N/A | N/A |  |
|  | n7 | 2512 | 5 | 25 | 2632 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 798 | 13.9 | IMD3 |  |
|  | 20 | 852 | 5 | 25 | 811 | N/A | N/A |  |
|  | n7 | N/A | 10 | N/A | 2670 | 5.9 | IMD5 |  |
|  | n28 | 738 | 5 | 25 | 793 | N/A | N/A |  |
| DC_20A_n7A-n78A | 20 | 845 | 5 | 25 | 804 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2675 | 30.8 | IMD2 |  |
|  | n78 | 3520 | 10 | 50 | 3520 | N/A | N/A |  |
|  | 20 | 850 | 5 | 25 | 809 | N/A | N/A |  |
|  | n7 | 2550 | 10 | 50 | 2675 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3400 | 28.8 | IMD21 |  |
| DC_20A_n8A-n78A | n8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | 20 | 837 | 5 | 25 | 796 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3567 | 10.3 | IMD4 |  |
|  | n8 | N/A | 5 | N/A | 940 | 12.1 | IMD4 |  |
|  | n78 | 3481 | 10 | 50 | 3481 | N/A | N/A |  |
|  | 20 | 847 | 5 | 25 | 806 | N/A | N/A |  |
| DC_20A-28A_n3A | 20 | 845 | 5 | 25 | 804 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 785 | 9.4 | IMD4 |  |
|  | n3 | 1750 | 5 | 25 | 1845 | N/A | N/A |  |
| DC_20A-28A_n7A | n7 | 2505 | 5 | 25 | 2625 | N/A | N/A |  |
|  | 20 | 859 | 5 | 25 | 818 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 787 | 17.4 | IMD34 |  |
| DC_20A-28A_n78A | 20 | 837 | 5 | 25 | 796 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 799 | 9.4 | IMD4 |  |
|  | n78 | 3310 | 10 | 50 | 3310 | N/A | N/A |  |
|  | 20 | N/A | 5 | N/A | 808 | 3.8 | IMD5 |  |
|  | 28 | 705.5 | 5 | 25 | 760.5 | N/A | N/A |  |
|  | n78 | 3630 | 10 | 50 | 3630 | N/A | N/A |  |
| DC_20A_n28A-n78A, DC_20A_SUL_n78A-n83A | 20 | 857 | 5 | 25 | 816 | N/A | N/A |  |
|  | n28, n83 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3314 | 8.7 | IMD4 |  |
|  | 20 | 837 | 5 | 25 | 796 | N/A | N/A |  |
|  | n78 | 3310 | 10 | 50 | 3310 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 799 | 9.4 | IMD4 |  |
| DC_20A-32A_n1A | n1 | 1950.5 | 5 | 50 | 2140.5 | N/A | N/A |  |
|  | 20 | 852.5 | 5 | 25 | 811.5 | N/A | N/A |  |
|  | 32 | N/A | 5 | N/A | 1459.5 | 4.0 | IMD5 |  |
| DC_20A-38A_n1A | n1 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 20 | N/A | N/A | N/A | N/A | N/A | IMD5 |  |
|  | 38 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_20A-38A_n3A | 20 | 850 | 5 | 25 | 809 | N/A | N/A |  |
|  | 38 | N/A | 5 | N/A | 2610 | 28.4 | IMD21 |  |
|  | n3 | 1760 | 5 | 25 | 1855 | N/A | N/A |  |
| DC_20A-38A_n28A | 20 | 835.5 | 5 | 25 | 793.5 | N/A | N/A |  |
|  | 38 | N/A | 5 | N/A | 2612 | 5.9 | IMD5 |  |
|  | n28 | 730 | 5 | 25 | 785 | N/A | N/A |  |
| DC_20A-38A_n78ADC_20A-38A_n78(2A | 20 | N/A | N/A | N/A | N/A | N/A | IMD2 |  |
|  | 38 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | n78 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 20 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | 38 | N/A | N/A | N/A | N/A | N/A | IMD2 |  |
|  | n78 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_20A_n38A-n78A | 20 | 850 | 5 | 25 | 809 | N/A | N/A |  |
|  | n38 | N/A | 10 | N/A | 2600 | 30.9 | IMD2 |  |
|  | n78 | 3450 | 10 | 50 | 3450 | N/A | N/A |  |
| DC_20A-40A_n1ADC_20A-40C_n1A | 20 | N/A | 5 | N/A | 800 | 8.0 | IMD4 |  |
|  | 40 | 2330 | 5 | 25 | 2330 | N/A | N/A |  |
|  | n1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
| DC_20A-40A_n28A | 20 | 835 | 5 | 25 | 794 | N/A | N/A |  |
|  | 40 | N/A | 5 | N/A | 2385 | 18.8 | IMD3 |  |
|  | n28 | 715 | 5 | 25 | 770 | N/A | N/A |  |
|  | 20 | N/A | 5 | N/A | 815 | 17.0 | IMD3 |  |
|  | 40 | 2305 | 5 | 25 | 2305 | N/A | N/A |  |
|  | n28 | 745 | 5 | 25 | 800 | N/A | N/A |  |
| DC_20A-40A_n78ADC_20A-40C_n78ADC_20A-40A_n78(2A)DC_20A-40C_n78(2A) | 20 | N/A | 5 | N/A | 815 | 19.8 | IMD3 |  |
|  | 40 | 2302.5 | 5 | 25 | 2302.5 | N/A | N/A |  |
|  | n78 | 3790 | 10 | 50 | 3790 | N/A | N/A |  |
| DC_20A-41A_n1A | 20 | N/A | 5 | N/A | 800 | 4.5 | IMD5 |  |
| DC_20A-41C_n1A | 41 | 2510 | 10 | 50 | 2510 | N/A | N/A |  |
|  | n1 | 1940 | 5 | 25 | 2130 | N/A | N/A |  |
| DC_20A-41A_n78A | 20 | 845 | 5 | 25 | 804 | N/A | N/A |  |
| DC_20A-41C_n78A | 41 | N/A | 10 | N/A | 2675 | 29.8 | IMD2 |  |
|  | n78 | 3520 | 10 | 50 | 3520 | N/A | N/A |  |
|  | 20 | N/A | 5 | N/A | 798 | 30.8 | IMD24 |  |
|  | 41 | 2642 | 10 | 50 | 2642 | N/A | N/A |  |
|  | n78 | 3440 | 10 | 50 | 3440 | N/A | N/A |  |
| DC_20A_n41A-n78A | 20 | 845 | 5 | 25 | 804 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2675 | 29.8 | IMD2 |  |
|  | n78 | 3520 | 10 | 50 | 3520 | N/A | N/A |  |
|  | 20 | 850 | 5 | 25 | 809 | N/A | N/A |  |
|  | n41 | 2550 | 10 | 50 | 2550 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3400 | 28.8 | IMD2 |  |
| DC_20A-67A_n3A | 20 | 837 | 5 | 25 | 796 | N/A | N/A |  |
|  | 67 | N/A | 5 | N/A | 746 | 9.4 | IMD4 |  |
|  | n3 | 1765 | 5 | 25 | 1860 | N/A | N/A |  |
| DC_20A_SUL_n78A-n80A | 20 | N/A | 5 | N/A | 806 | 9 | IMD4 |  |
|  | n80 | 1735 | 5 | 25 |  | N/A | N/A |  |
| DC_21A_n1A-n77ADC_21A_n1A-n78A | 21 | 1450.4 | 5 | 25 | 1498.4 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2154.6 | 30.6 | IMD24 |  |
|  | n77/n78 | 3605 | 10 | 50 | 3605 | N/A | N/A |  |
| DC_21A_n1A-n79A20 |  |  |  | N/A |  |  |  |  |
| DC_21A-28A_n77ADC_21A-28A_n78A | 21 | 1452 | 5 | 25 | 1500 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 785.5 | 16.9 | IMD3 |  |
|  | n77/n78 | 3689.5 | 10 | 50 | 3689.5 | N/A | N/A |  |
|  | 21 | N/A | 5 | N/A | 1498.5 | 9.9 | IMD4 |  |
|  | 28 | 730.5 | 5 | 25 | 785.5 | N/A | N/A |  |
|  | n77/n78 | 3690 | 10 | 50 | 3690 | N/A | N/A |  |
| DC_21A-28A_n79A | 21 | N/A | 5 | N/A | 1498 | 5.2 | IMD5 |  |
|  | 28 | 730.5 | 5 | 25 | 785.5 | N/A | N/A |  |
|  | n79 | 4420 | 40 | 216 | 4420 | N/A | N/A |  |
| DC_21A_n28A-n77A | 21 | 1452 | 5 | 25 | 1500 | N/A | N/A |  |
| DC_21A_n28A-n78A | n28 | N/A | 5 | N/A | 785.5 | 16.9 | IMD39 |  |
|  | n77/n78 | 3689.5 | 10 | 50 | 3689.5 | N/A | N/A |  |
|  | 21 | 1452 | 5 | 25 | 1500 | N/A | N/A |  |
|  | n28 | 730.5 | 5 | 25 | 785.5 | N/A | N/A |  |
|  | n77/n78 | N/A | 10 | N/A | 3634.5 | 17.3 | IMD39 |  |
| DC_21A_n28A-n79A 17 | 21 | 1450.4 | 5 | 25 | 1498.4 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 790.5 | 2.8 | IMD5 |  |
|  | n79 | 4980 | 40 | 216 | 4980 | N/A | N/A |  |
|  | 21 | 1460.4 | 5 | 25 | 1508.4 | N/A | N/A |  |
|  | n28 | 735.5 | 5 | 25 | 790.5 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4420 | [6.3] | IMD44 |  |
| DC_21A-42A_n1A | 21 | N/A | 5 | N/A | 1500 | 31.4 | IMD2 |  |
|  | 42 | 3450 | 10 | 50 | 3450 | N/A | N/A |  |
|  | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
| DC_21A_n78A-n79A | 21 | 1453 | 5 | 25 | 1501 | N/A | N/A |  |
|  | n78 | 3420 | 10 | 50 | 3420 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4873 | 30.1 | IMD2 |  |
|  | 21 | 1453 | 5 | 25 | 1501 | N/A | N/A |  |
|  | n79 | 4940 | 40 | 216 | 4940 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3487 | 29.8 | IMD2 |  |
| DC_25A-41A_n41ADC_25A-41C_n41ADC_25A-41D_n41A | 25 | N/A | 5 | N/A | 1992.5 | 8.5 | IMD7 |  |
| DC_25A-25A-41A_n41ADC_25A-25A-41C_n41ADC_25A-25A-41D_n41A | 41 | 2502.5 | 5 | 1 (RBstart=0) | 2502.5 | N/A | N/A |  |
| DC_25A-(n)41CADC_25A-(n)41DADC_25A-25A-(n)41CADC_25A-25A-(n)41DA | n41 | 2670 | 10 | 1 (RBstart=22) | 2670 | N/A | N/A |  |
| DC_25A-66A_n77ADC_25A-25A-66A_n77A | 25 | 1855 | 5 | 25 | 1935 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2115 | 29.2 | IMD29 |  |
|  | n77 | 3970 | 10 | 25 | 3970 | N/A | N/A |  |
|  | 25 | 1885 | 5 | 25 | 1965 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2175 | 4.0 | IMD5 |  |
|  | n77 | 3915 | 10 | 25 | 3915 | N/A | N/A |  |
|  | 25 | N/A | 5 | N/A | 1960 | 32.1 | IMD2 |  |
|  | 66 | 1760 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n77 | 3720 | 10 | 25 | 3720 | N/A | N/A |  |
|  | 25 | N/A | 5 | N/A | 1940 | 9.1 | IMD411 |  |
|  | 66 | 1775 | 5 | 25 | 2175 | N/A | N/A |  |
|  | n77 | 3385 | 10 | 25 | 3385 | N/A | N/A |  |
|  | 25 | N/A | 5 | N/A | 1935 | 4.2 | IMD5 |  |
|  | 66 | 1715 | 5 | 25 | 2115 | N/A | N/A |  |
|  | n77 | 3540 | 10 | 25 | 3540 | N/A | N/A |  |
| DC_25A-66A_n78ADC_25A-25A-66A_n78A | 25 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2160 | 10.4 | IMD4 |  |
|  | n78 | 3480 | 10 | 50 | 3480 | N/A | N/A |  |
|  | 25 | N/A | 5 | N/A | 1960 | 32.1 | IMD29 |  |
|  | 66 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n78 | 3700 | 10 | 50 | 3700 | N/A | N/A |  |
|  | 25 | N/A | 5 | N/A | 1980 | 4.2 | IMD5 |  |
|  | 66 | 1770 | 5 | 25 | 2170 | N/A | N/A |  |
|  | n78 | 3645 | 10 | 25 | 3645 | N/A | N/A |  |
| DC_28A_n1A-n5A | 28 | 708 | 5 | 25 | 763 | N/A | N/A |  |
|  | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n5 | N/A | 5 | N/A | 882 | 4.6 | IMD5 |  |
|  | 28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2136 | 4 | IMD5 |  |
|  | n5 | 836 | 5 | 25 | 881 | N/A | N/A |  |
| DC_28A_n1A-n40A | 28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | n1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2374 | 10.1 | IMD4 |  |
| DC_28A_n1A-n78A | 28 | 733 | 5 | 25 | 788 | N/A | N/A |  |
|  | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3416 | 15.7 | IMD3 |  |
|  | 28 | 740 | 5 | 25 | 795 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2150 | 15.7 | IMD3 |  |
|  | n78 | 3630 | 10 | 50 | 3630 | N/A | N/A |  |
| DC_28A_n3A-n77A | 28 | 735 | 5 | 25 | 790 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1850 | 17.0 | IMD3 |  |
|  | n77 | 3320 | 10 | 50 | 3320 | N/A | N/A |  |
|  | 28 | 733 | 5 | 25 | 788 | N/A | N/A |  |
|  | n3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 4173 | 15.9 | IMD3 |  |
| DC_28A_n3A-n78A | 28 | 735 | 5 | 25 | 790 | N/A | N/A |  |
|  | n3 | 1755 | 5 | 25 | 1850 | 17.0 | IMD3 |  |
|  | n78 | 3320 | 10 | 50 | 3320 | N/A | N/A |  |
|  | n3 | 1750 | 5 | 25 | 1845 | N/A | N/A |  |
|  | 28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | n78 | 3764 | 10 | 50 | 3764 | 4.5 | IMD5 |  |
| DC_28A_n5A-n40A | 28 | 712 | 5 | 25 | 767 | N/A | N/A |  |
|  | n5 | 826.5 | 5 | 25 | 871.5 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2365 | 18.8 | IMD3 |  |
|  | 28 | 720 | 5 | 25 | 775 | N/A | N/A |  |
|  | n5 | N/A | 5 | N/A | 880 | 17.0 | IMD3 |  |
|  | n40 | 2320 | 10 | 50 | 2320 | N/A | N/A |  |
| DC_28A_n5A-n78A | 28 | 707 | 5 | 25 | 762 | N/A | N/A |  |
|  | n5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3781 | 4.0 | IMD5 |  |
|  | 28 | 723 | 5 | 25 | 778 | N/A | N/A |  |
|  | n5 | N/A | 5 | N/A | 874 | 3.8 | IMD5 |  |
|  | n78 | 3766 | 10 | 50 | 3756 | N/A | N/A |  |
| DC_28A_n5A-n105A | 28 | 735 | 5 | 25 | 790 | N/A | N/A |  |
|  | n5 | 835 | 5 | 25 | 880 | N/A | N/A |  |
|  | n105 | N/A | 5 | N/A | 635 | 25 | IMD3 |  |
| DC_28A_n7A-n78ADC_28A_n7B-n78A | 28 | 745 | 5 | 25 | 800 | N/A | N/A |  |
|  | n7 | 2565 | 5 | 25 | 2685 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3310 | 29.7 | IMD2 |  |
|  | 28 | 740 | 5 | 25 | 795 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2650 | 30.5 | IMD2 |  |
|  | n78 | 3390 | 10 | 50 | 3390 | N/A | N/A |  |
| DC_28A_n8A-n78A | 28 | 728 | 5 | 25 | 783 | N/A | N/A |  |
|  | n8 | 910 | 5 | 25 | 955 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3458 | 9.1 | IMD4 |  |
|  | 28 | 713 | 5 | 25 | 768 | N/A | N/A |  |
|  | n8 | N/A | 5 | N/A | 935 | 4.3 | IMD5 |  |
|  | n78 | 3787 | 10 | 50 | 3787 | N/A | N/A |  |
| DC_28A-38A_n1A | n1 | 1975 | 5 | 25 | 2165 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 775 | 4.5 | IMD5 |  |
|  | 38 | 2575 | 5 | 25 | 2575 | N/A | N/A |  |
| DC_28A-40A_n1A | 28 | 740 | 5 | 25 | 795 | N/A | N/A |  |
|  | 40 | N/A | 5 | N/A | 2365 | 10.1 | IMD4 |  |
|  | n1 | 1922.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 780 | 8 | IMD4 |  |
|  | 40 | 2340 | 5 | 25 | 2340 | N/A | N/A |  |
|  | n1 | 1950 | 5 | 25 | 2140 | N/A | N/A |  |
| DC_28_n40-n41 | 28 | 740 | 5 | 25 | 795 | N/A | N/A |  |
|  | n40 | 2380 | 5 | 25 | 2380 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2540 | 11.4 | IMD5 |  |
| DC_28_n40-n71 | 28 | 745.5 | 5 | 25 | 800.5 | N/A | N/A |  |
|  | n40 | 2362.5 | 10 | 50 | 2362.5 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 619.5 | [3.3] | IMD5 |  |
| DC_28A-38A_n78A | 28 | 738 | 5 | 25 | 793 | N/A | N/A |  |
|  | 38 | N/A | 5 | N/A | 2582 | 29.5 | IMD2 |  |
|  | n78 | 3320 | 10 | 50 | 3320 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 793 | 30.8 | IMD24 |  |
|  | 38 | 2582 | 5 | 25 | 2582 | N/A | N/A |  |
|  | n78 | 3375 | 10 | 50 | 3375 | N/A | N/A |  |
| DC_28A_n40A-n77A | 28 | 708 | 5 | 25 | 763 | N/A | N/A |  |
|  | n40 | 2310 | 10 | 50 | 2310 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3726 | [28.6] | IMD31 |  |
|  | 28 | 708 | 5 | 25 | 763 | N/A | N/A |  |
|  | n40 | N/A | 10 | N/A | 2390 | [12.3] | IMD3 |  |
|  | n77 | 3806 | 10 | 50 | 3806 | N/A | N/A |  |
| DC_28A-40A_n78A DC_28A-40C_n78A | 28 | N/A | 5 | N/A | 800.5 | 11 | IMD3 |  |
|  | 40 | 2302.5 | 5 | 25 | 2302.5 | N/A | N/A |  |
|  | n78 | 3795 | 10 | 50 | 3795 | N/A | N/A |  |
|  | 28 | 715 | 5 | 25 | 770 | N/A | N/A |  |
|  | 40 | N/A | 5 | N/A | 2320 | 15.7 | IMD3 |  |
|  | n78 | 3750 | 10 | 50 | 3750 | N/A | N/A |  |
| DC_28A-41A_n77A | 28 | 738 | 5 | 25 | 793 | N/A | N/A |  |
|  | n77 | 3380 | 10 | 50 | 3380 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2642 | 29.5 | IMD2 |  |
|  | 41 | 2642 | 5 | 25 | 2642 | N/A | N/A |  |
|  | n77 | 3440 | 10 | 50 | 3440 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 798 | 30.8 | IMD2 |  |
|  | 41 | 2567.5 | 10 | 50 | 2567.5 | N/A | N/A |  |
|  | n77 | 3460 | 10 | 50 | 3460 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 782.5 | 3.0 | IMD5 |  |
| DC_28A-41A_n78A | 28 | 738 | 5 | 25 | 793 | N/A | N/A |  |
|  | n78 | 3380 | 10 | 50 | 3380 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2642 | 29.5 | IMD2 |  |
|  | 41 | 2642 | 5 | 25 | 2642 | N/A | N/A |  |
|  | n78 | 3440 | 10 | 50 | 3440 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 798 | 30.8 | IMD2 |  |
| DC_28A-41A_n79A | 28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | n79 | 4739 | 40 | 216 | 4739 | N/A | N/A |  |
|  | 41 | N/A | 5 | N/A | 2510 | 8.6 | IMD4 |  |
|  | 41 | 2650 | 5 | 25 | 2650 | N/A | N/A |  |
|  | n79 | 4502 | 40 | 216 | 4502 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 798 | 15.9 | IMD3 |  |
| DC_28A-42A_n79ADC_28A-42A_n79CDC_28A-42C_n79ADC_28A-42C_n79C | 28 | 730 | 5 | 25 | 785 | N/A | N/A |  |
|  | 42 | N/A | 5 | N/A | 3420 | 15.3 | IMD3 |  |
|  | n79 | 4880 | 40 | 216 | 4880 | N/A | N/A |  |
|  | 28 | N/A | 5 | N/A | 800 | 16.2 | IMD2 |  |
|  | 42 | 3597.5 | 5 | 25 | 3597.5 | N/A | N/A |  |
|  | n79 | 4420 | 40 | 216 | 4420 | N/A | N/A |  |
| DC_28A-66A_n7A | 28 | N/A | 5 | N/A | 790 | 27.6 | IMD2 |  |
|  | 66 | 1715 | 5 | 25 | 2115 | N/A | N/A |  |
|  | n7 | 2505 | 5 | 50 | 2625 | N/A | N/A |  |
| DC_28A-66A_n66A | 28 | 710.5 | 5 | 25 | 765.5 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2129 | 11.0 | IMD4 |  |
|  | n66 | 1775 | 5 | 25 | 2175 | N/A | N/A |  |
| DC_28A_n71A-n77A | 28 | 705.5 | 5 | 25 | 760.5 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 628 | 3.8 | IMD5 |  |
|  | n77 | 3450 | 10 | 50 | 3450 | N/A | N/A |  |
| DC_28A_n78A-n105A | 28 | 705.5 | 5 | 25 | 760.5 | N/A | N/A |  |
|  | n78 | 3450 | 10 | 50 | 3450 | N/A | N/A |  |
|  | n105 | N/A | 5 | N/A | 628 | 3.9 | IMD5 |  |
| DC_29A-30A_n66A | 29 | N/A | 5 | 25 | 719.5 | 4.5 | IMD5 |  |
|  | 30 | 2307.5 | 5 | 25 | 2352.5 | N/A | N/A |  |
|  | n66 | 1777.5 | 5 | 25 | 2177.5 | N/A | N/A |  |
| DC_29A-30A_n77A | 29 | N/A | 5 | N/A | 722 | 15.2 | IMD34 |  |
|  | 30 | 2310 | 5 | 25 | 2355 | N/A | N/A |  |
|  | n77 | 3898 | 10 | 50 | 3898 | N/A | N/A |  |
| DC_29A-66A_n77A | 29 | N/A | 5 | N/A | 722 | 15.2 | IMD311 |  |
| DC_29A-66A-66A_n77A | 66 | 1734 | 5 | 25 | 2134 | N/A | N/A |  |
|  | n77 | 4190 | 10 | 50 | 4190 | N/A | N/A |  |
| DC_30A-66A_n5A,DC_30A-66A-66A_n5A,DC_30A-66A-66A-66A_n5A | 30 | 2310 | 5 | 25 | 2355 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2130 | 2.5 | IMD5 |  |
|  | n5 | 830 | 5 | 25 | 875 | N/A | N/A |  |
| DC_30A-66A_n77ADC_30A-66A_n77(2A) | 30 | N/A | 5 | N/A | 2355 | 29.2 | IMD211 |  |
| DC_30A-66A-66A_n77A | 66 | 1745 | 5 | 25 | 2145 | N/A | N/A |  |
| DC_30A-66A-66A_n77(2A) | n77 | 4100 | 10 | 50 | 4100 | N/A | N/A |  |
|  | 30 | N/A | 5 | N/A | 2355 | 3.4 | IMD5 |  |
|  | 66 | 1735 | 5 | 25 | 2135 | N/A | N/A |  |
|  | n77 | 3780 | 10 | 50 | 3780 | N/A | N/A |  |
|  | 30 | 2310 | 5 | 25 | 2355 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2160 | 8.7 | IMD411 |  |
|  | n77 | 3390 | 10 | 50 | 3390 | N/A | N/A |  |
| DC_38A_n3A-n78A | 38 | 2560 | 10 | 50 | 2560 | N/A | N/A |  |
|  | n3 | 1730 | 5 | 25 | 1825 | N/A | N/A |  |
|  | n78 | 3390 | 10 | 50 | 3390 | 16.1 | IMD3 |  |
|  | 38 | 2620 | 5 | 25 | 2620 | N/A | N/A |  |
|  | n3 | 1745 | 5 | 25 | 1840 | 17.6 | IMD39 |  |
|  | n78 | 3400 | 10 | 52 | 3400 | N/A | N/A |  |
| DC_38A_n28A-n78A | 38 | 2615 | 5 | 25 | 2615 | N/A | N/A |  |
|  | n28 | 745 | 5 | 25 | 798 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3360 | 28.2 | IMD29 |  |
|  | 38 | 2615 | 5 | 25 | 2615 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 785 | 30.8 | IMD24 |  |
|  | n78 | 3400 | 10 | 25 | 3400 | N/A | N/A |  |
| DC_38A-40A_n28A | 38 | N/A | 5 | N/A | 2576 | 5.3 | IMD5 |  |
|  | 40 | 2350 | 5 | 25 | 2350 | N/A | N/A |  |
|  | n28 | 708 | 5 | 25 | 763 | N/A | N/A |  |
| DC_39A_n40A-n41ADC_39A_n40A-n41C | 39 | 1917.5 | 5 | 25 | 1917.5 | N/A | N/A |  |
|  | n40 | 2305 | 10 | 50 | 2305 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2685 | 30.3 | IMD3 |  |
| DC_39A_n40A-n79A | 39 | 1917.5 | 5 | 25 | 1917.5 | N/A | N/A |  |
|  | n40 | 2305 | 10 | 50 | 2305 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4980 | 5.8 | IMD4 |  |
| DC_39A_n41A-n79A | 39 | 1900 | 5 | 25 | 1900 | N/A | N/A |  |
|  | n41 | 2620 | 10 | 50 | 2620 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4520 | 29.8 | IMD24 |  |
|  | 39 | 1900 | 5 | 25 | 1900 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2620 | 30.2 | IMD24 |  |
|  | n79 | 4520 | 40 | 216 | 4520 | N/A | N/A |  |
| DC_40A_n1A-n78A | 40 | 2340 | 5 | 25 | 2340 | N/A | N/A |  |
|  | n1 | 1930 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3450 | 9.8 | IMD4 |  |
|  | 40 | 2360 | 5 | 25 | 2360 | N/A | N/A |  |
|  | n1 | N/A | 5 | N/A | 2140 | 9.1 | IMD4 |  |
|  | n78 | 3430 | 10 | 50 | 3430 | N/A | N/A |  |
| DC_40A_n41A-n79A | 40 | 2340 | 5 | 25 | 2340 | N/A | N/A |  |
|  | n41 | 2600 | 10 | 50 | 2600 | N/A | N/A |  |
|  | n79 | N/A | 40 | N/A | 4940 | 30.5 | IMD2 |  |
|  | 40 | 2340 | 5 | 25 | 2340 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2600 | 29.4 | IMD24 |  |
|  | n79 | 4880 | 40 | 216 | 4940 | N/A | N/A |  |
| DC_41A_n1A-n77A | 41 | 2650 | 5 | 25 | 2650 | N/A | TDD |  |
| DC_41C_n1A-n77A | n1 | 1970 | 5 | 25 | 2160 | N/A | FDD |  |
|  | n77 | N/A | 10 | N/A | 3330 | 19.6 | TDD |  |
|  | 41 | 2510 | 5 | 25 | 2510 | N/A | TDD |  |
|  | n77 | 4150 | 10 | 50 | 4150 | N/A | TDD |  |
|  | n1 | N/A | 5 | N/A | 2120 | 11.0 | FDD |  |
| DC_41A_n3A-n77ADC_41C_n3A-n77ADC_41A_n3A-n78ADC_41C_n3A-n78A | 41 | 2620 | 5 | 25 | 2620 | N/A | N/A |  |
|  | n3 | N/A | 5 | N/A | 1840 | 16.4 | IMD3 |  |
|  | n77/n78 | 3400 | 10 | 50 | 3400 | N/A | N/A |  |
|  | 41 | 2580 | 5 | 25 | 2580 | N/A | N/A |  |
|  | n3 | 1720 | 5 | 25 | 1815 | N/A | N/A |  |
|  | n77/n78 | N/A | 10 | N/A | 3440 | 16.8 | IMD34 |  |
| DC_41A_n28A-n77ADC_41C_n28A-n77ADC_41A_n28A-n78ADC_41C_n28A-n78A | 41 | 2580 | 5 | 25 | 2580 | N/A | N/A |  |
|  | n28 | 743 | 5 | 25 | 798 | N/A | N/A |  |
|  | n77/n78 | N/A | 10 | N/A | 3323 | 28.2 | IMD21 |  |
|  | 41 | 2642 | 5 | 25 | 2642 | N/A | N/A |  |
|  | n28 | N/A | 5 | N/A | 798 | 30.8 | IMD21 |  |
|  | n77/n78 | 3440 | 10 | 50 | 3440 | N/A | N/A |  |
| DC_46A-48A_n5A5DC_46C-48A_n5A5DC_46D-48A_n5A5DC_46E-48A_n5A5 | 46 | N/A | N/A | N/A | N/A | N/A | IMD2,IMD3 |  |
|  | 48 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | n5 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_46A-48A_n66A5DC_46C-48A_n66A5DC_46D-48A_n66A5DC_46E-48A_n66A5 | 46 | N/A | N/A | N/A | N/A | N/A | IMD2,IMD3 |  |
|  | 48 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | n66 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_46A-66A_n5A | 46 | N/A | 10 | N/A | 5163 | 9.0 | IMD4 |  |
| DC_46C-66A_n5ADC_46D-66A_n5ADC_46E-66A_n5ADC_46A-66A-66A_n5ADC_46C-66A-66A_n5ADC_46D-66A-66A_n5A | 66 | 1775 | 5 | 25 | 2175 | N/A | N/A |  |
|  | n5 | 847 | 5 | 25 | 892 | N/A | N/A |  |
| DC_46A-66A_n25A4DC_46C-66A_n25A4DC_46D-66A_n25A4 | 46 | N/A | 10 | N/A | 5485 | 16.1 | IMD3 |  |
|  | 66 | 1775 | 5 | 25 | 2175 | N/A | N/A |  |
|  | n25 | 1855 | 5 | 25 | 1935 | N/A | N/A |  |
| DC_46A-66A_n77A5DC_46A-46A-66A_n77A5 | 46 | N/A | N/A | N/A | N/A | N/A | IMD2,IMD3 |  |
|  | 66 | N/A | N/A | N/A | N/A | N/A | N/A |  |
|  | n77 | N/A | N/A | N/A | N/A | N/A | N/A |  |
| DC_48A-(n)12AA | 48 | 3557.5 | 10 | 50 | 3557.5 | N/A | N/A |  |
|  | 12 | N/A | 5 | N/A | 740.5 | 5.5 | IMD5 |  |
|  | n12 | 705.5 | 5 | 25 | 735.5 | 5.5 | IMD5 |  |
| DC_48A-66A_n2ADC_48C-66A_n2ADC_48D-66A_n2ADC_48E-66A_n2A | n2 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
|  | 48 | N/A | 10 | N/A | 3620 | 29.4 | IMD2 |  |
|  | 66 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | 48 | 3560 | 5 | 25 | 3560 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2155 | 12.1 | IMD4 |  |
|  | n2 | 1905 | 5 | 25 | 1985 | N/A | N/A |  |
| DC_48A-66A_n12A | 48 | 3580 | 5 | 25 | 3580 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2160 | 17.1 | IMD3 |  |
|  | n12 | 710 | 5 | 25 | 740 | N/A | N/A |  |
| DC_48A-66A_n25ADC_48C-66A_n25ADC_48D-66A_n25A | 48 | 3630 | 20 | 100 | 3630 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2130 | 8.3 | IMD4 |  |
|  | n25 | 1883.3 | 5 | 25 | 1963.3 | N/A | N/A |  |
|  | 48 | N/A | 10 | N/A | 3620 | 29.4 | IMD2 |  |
|  | 66 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n25 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
| DC_48A-66A_n66ADC_48C-66A_n66A | 48 | 3660 | 20 | 100 | 3660 | N/A | N/A |  |
| DC_48D-66A_n66A | 66 | N/A | 5 | N/A | 2175 | 4.0 | IMD5 |  |
| DC_48E-66A_n66A | n66 | 1715 | 5 | 25 | 2115 | N/A | N/A |  |
| DC_48A-66A_n71A | 48 | 3560 | 5 | 25 | 3560 | N/A | N/A |  |
|  | 66 | N/A | 5 | N/A | 2174 | 15.8 | IMD3 |  |
|  | n71 | 693 | 5 | 25 | 647 | N/A | N/A |  |
|  | 48 | N/A | 5 | N/A | 3697.5 | 13.0 | IMD4 |  |
|  | 66 | 1712.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
|  | n71 | 665.5 | 5 | 25 | 619.5 | N/A | N/A |  |
| DC_66A_n2A-n41A | 66 | 1715 | 5 | 25 | 2115 | N/A | N/A |  |
|  | n2 | 1860 | 5 | 25 | 1940 | 9.5 | IMD4 |  |
|  | n41 | 2685 | 10 | 50 | 2685 | N/A | N/A |  |
| DC_66A_n2A-n66A | 66 | 1775 | 5 | 25 | 2175 | N/A | N/A |  |
|  | n2 | N/A | 5 | N/A | 1935 | 20 | IMD3 |  |
|  | n66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n2 | 1870 | 5 | 25 | 1950 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2170 | 4.0 | IMD5 |  |
| DC_66A_n2A-n77A | n2 | N/A | 5 | N/A | 1960 | 32.1 | IMD2 |  |
|  | 66 | 1760 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n77 | 3720 | 10 | 50 | 3720 | N/A | N/A |  |
|  | n2 | 1853 | 5 | 25 | 1933 | N/A | N/A |  |
|  | 66 | 1713 | 5 | 25 | 2113 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3566 | 29.4 | IMD24 |  |
| DC_66A_n2A-n78A | 66 | 1760 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n2 | N/A | 5 | N/A | 1960 | 32.1 | IMD29 |  |
|  | n78 | 3720 | 10 | 50 | 3720 | N/A | N/A |  |
|  | 66 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n2 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3620 | 34.9 | IMD29 |  |
|  | 66 | 1760 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n2 | N/A | 5 | N/A | 1960 | 2.1 | IMD5 |  |
|  | n78 | 3620 | 10 | 50 | 3620 | N/A | N/A |  |
| DC_66A-(n)5AA | 66 | 1721 | 5 | 25 | 2121 | N/A | N/A |  |
|  | 5 | N/A | 5 | N/A | 878 | 25 | IMD2 |  |
|  | n5 | 838 | 5 | 25 | 883 | 30 | IMD2 |  |
| DC_66A_n5A-n48A | 66 | 1750 | 5 | 25 | 2150 | N/A | N/A |  |
|  | n5 | 834 | 5 | 25 | 879 | N/A | N/A |  |
|  | n48 | N/A | 10 | N/A | 3582 | 3.3 | IMD5 |  |
| DC_66A_n5A-n77A | 66 | 1770 | 5 | 25 | 2170 | N/A | N/A |  |
|  | n5 | 845 | 5 | 25 | 890 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3460 | 16.6 | IMD39 |  |
| DC_66A_n7A-n12A | 66 | 1773 | 5 | 25 | 2173 | N/A | N/A |  |
|  | n7 | 2515 | 5 | 25 | 2635 | N/A | N/A |  |
|  | n12 | N/A | 5 | N/A | 742 | 31 | IMD2 |  |
| DC_66A_n7A-n77A | 66 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n7 | 2542 | 5 | 25 | 2662 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3344 | 16.0 | IMD34 |  |
|  | 66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2640 | 3.4 | IMD5 |  |
|  | n77 | 3900 | 10 | 50 | 3900 | N/A | N/A |  |
| DC_66A_n7A-n78A,DC_66A-66A_n7A-n78DC_66A_n7(2A)-n78ADC_66A-66A_n7(2A)-n78ADC_66A_n7A-n78(2A)DC_66A-66A_n7A-n78(2A)DC_66A-66A_n7(2A)-n78(2A) | 66 | 1730 | 5 | 25 | 2130 | N/A | N/A |  |
|  | n7 | 2560 | 5 | 25 | 2680 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3390 | 16.1 | IMD3 |  |
| DC_66A_n12A-n77A | 66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n12 | N/A | 5 | N/A | 740 | 15.2 | IMD311 |  |
|  | n77 | 4180 | 10 | 50 | 4180 | N/A | N/A |  |
|  | 66 | 1723 | 5 | 25 | 2123 | N/A | N/A |  |
|  | n12 | 704 | 5 | 25 | 734 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 4150 | 16.0 | IMD34,9,11 |  |
| DC_66A_n25A-n41A | 66 | 1715 | 5 | 25 | 2115 | N/A | N/A |  |
|  | n41 | 2685 | 10 | 50 | 2685 | N/A | N/A |  |
|  | n25 | 1860 | 5 | 25 | 1940 | 5 | 11.0 |  |
| DC_66A_n25A-n48A | 66 | 1740 | 5 | 25 | 2140 | N/A | N/A |  |
|  | n25 | 1880 | 5 | 25 | 1960 | N/A | N/A |  |
|  | n48 | N/A | 10 | N/A | 3620 | 29.4 | IMD2 |  |
|  | 66 | 1735 | 5 | 25 | 2135 | N/A | N/A |  |
|  | n25 | N/A | 5 | N/A | 1960 | 28.3 | IMD2 |  |
|  | n48 | 3695 | 10 | 50 | 3695 | N/A | N/A |  |
| DC_66A_n25A-n66A | 66 | 1712.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
|  | n25 | 1912.5 | 5 | 25 | 1992.5 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2117.5 | 23 | IMD34 |  |
| DC_66A_n38A-n78A | 66 | 1760 | 5 | 25 | 2160 | N/A | N/A |  |
|  | n38 | 2610 | 10 | 50 | 2610 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3460 | 15.0 | IMD3 |  |
| DC_66A_n41A-n77A | 66 | 1730 | 5 | 25 | 2130 | N/A | N/A |  |
|  | n41 | 2600 | 10 | 50 | 2600 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3470 | 14.6 | IMD31 |  |
|  | 66 | 1715 | 5 | 25 | 2115 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2670 | 4.2 | IMD55 |  |
|  | n77 | 4190 | 10 | 50 | 4190 | N/A | N/A |  |
| DC_66A_n41A-n78A | 66 | 1730 | 5 | 25 | 2130 | N/A | N/A |  |
|  | n41 | 2560 | 10 | 50 | 2560 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3390 | 14.6 | IMD3 |  |
| DC_66A_n66A-n71A | 66 | 1752 | 5 | 25 | 2152 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2118 | 5.0 | IMD4 |  |
|  | n71 | 693 | 5 | 25 | 647 | N/A | N/A |  |
| DC_66A_n66A-n77A | 66 | 1730 | 5 | 25 | 2130 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2170 | 31 | IMD2 |  |
|  | n77 | 3900 | 10 | 50 | 3900 | N/A | N/A |  |
| DC_66A_n66A-n78A | 66 | 1775 | 5 | 25 | 2175 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2125 | 2.8 | IMD5 |  |
|  | n78 | 3725 | 10 | 50 | 3725 | N/A | N/A |  |
| DC_66A-71A_n77ADC_66A-71A_n77(2A) | 66 | N/A | 5 | N/A | 2160 | 15.5 | IMD39 |  |
|  | 71 | 693 | 5 | 25 | 647 | N/A | N/A |  |
|  | n77 | 3546 | 10 | 50 | 3546 | N/A | N/A |  |
|  | 66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | 71 | N/A | 5 | N/A | 640 | 15.3 | IMD311 |  |
|  | n77 | 4080 | 10 | 50 | 4080 | N/A | N/A |  |
| DC_66A_n71A-n77A | 66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n71 | 668 | 5 | 25 | 622 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 4108 | 15.9 | IMD34,9,11 |  |
|  | 66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n71 | N/A | 5 | N/A | 640 | 15.3 | IMD311 |  |
|  | n77 | 4080 | 10 | 50 | 4080 | N/A | N/A |  |
| DC_66A_n71A-n78A | 66 | 1712.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
|  | n71 | 665.5 | 5 | 25 | 619.5 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3709 | 13.0 | IMD4 |  |
| DC_71A_n2A-n41A | n2 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2586 | 27.2 | IMD2 |  |
|  | 71 | 686 | 5 | 50 | 640 | N/A | N/A |  |
|  | n2 | N/A | 5 | N/A | 1942 | 24.5 | IMD2 |  |
|  | n41 | 2610 | 10 | 50 | 2610 | N/A | N/A |  |
|  | 71 | 668 | 5 | 25 | 622 | N/A | N/A |  |
| DC_71A_n2A-n78A | n2 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
|  | 71 | 695.5 | 5 | 25 | 649.5 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3305 | 8.0 | IMD3 |  |
|  | n2 | N/A | 5 | N/A | 1954 | 16.5 | IMD3 |  |
|  | 71 | 693 | 5 | 25 | 647 | N/A | N/A |  |
|  | n78 | 3340 | 10 | 50 | 3340 | N/A | N/A |  |
| DC_71A_n2A-n77A | 71 | 695.5 | 5 | 25 | 649.5 | N/A | N/A |  |
|  | n2 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3305 | 8.0 | IMD34,9,11 |  |
|  | 71 | 693 | 5 | 25 | 647 | N/A | N/A |  |
|  | n2 | N/A | 5 | N/A | 1954 | 16.5 | IMD39,11 |  |
|  | n77 | 3340 | 10 | 50 | 3340 | N/A | N/A |  |
| DC_71A_n7A-n77A | 71 | 680 | 5 | 25 | 634 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2670 | 29.6 | IMD2 |  |
|  | n77 | 3350 | 10 | 50 | 3350 | N/A | N/A |  |
|  | 71 | 680 | 5 | 25 | 634 | N/A | N/A |  |
|  | n7 | N/A | 5 | N/A | 2640 | 13.2 | IMD3 |  |
|  | n77 | 4000 | 10 | 50 | 4000 | N/A | N/A |  |
|  | 71 | 666 | 5 | 25 | 620 | N/A | N/A |  |
|  | n7 | 2505 | 5 | 25 | 2625 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3837 | 16.0 | IMD3 |  |
|  | 71 | 693 | 5 | 25 | 647 | N/A | N/A |  |
|  | n7 | 2550 | 5 | 25 | 2670 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3714 | 9.7 | IMD4 |  |
| DC_71A_n25A-n41A | n25 | 1900 | 5 | 25 | 1980 | N/A | N/A |  |
|  | n41 | N/A | 10 | N/A | 2586 | 27.2 | IMD29 |  |
|  | 71 | 686 | 5 | 50 | 640 | N/A | N/A |  |
|  | n25 | N/A | 5 | N/A | 1942 | 24.5 | IMD2 |  |
|  | n41 | 2610 | 10 | 50 | 2610 | N/A | N/A |  |
|  | 71 | 668 | 5 | 25 | 622 | N/A | N/A |  |
| DC_71A_n25A-n77A | 71 | 693 | 5 | 25 | 647 | N/A | N/A |  |
|  | n25 | N/A | 5 | N/A | 1954 | 16.5 | IMD3 |  |
|  | n77 | 3340 | 10 | 50 | 3340 | N/A | N/A |  |
|  | 71 | 666 | 5 | 25 | 620 | N/A | N/A |  |
|  | n25 | N/A | 5 | N/A | 1982 | 12.5 | IMD4 |  |
|  | n77 | 3980 | 10 | 50 | 3980 | N/A | N/A |  |
|  | 71 | 695.5 | 5 | 25 | 649.5 | N/A | N/A |  |
|  | n25 | 1907.5 | 5 | 25 | 1987.5 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3298.5 | 16 | IMD34 |  |
|  | 71 | 666 | 5 | 25 | 620 | N/A | N/A |  |
|  | n25 | 1890 | 5 | 25 | 1970 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 3888 | 12 | IMD4 |  |
| DC_71A_n38A-n78A | 71 | 693 | 5 | 25 | 647 | N/A | N/A |  |
|  | n38 | 2615 | 10 | 50 | 2615 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3308 | 29.1 | IMD2 |  |
|  | 71 | 693 | 5 | 25 | 647 | N/A | N/A |  |
|  | n78 | 3308 | 10 | 50 | 3308 | N/A | N/A |  |
|  | n38 | N/A | 10 | N/A | 2615 | 28.7 | IMD2 |  |
| DC_71A_n66A-n77A | 71 | 668 | 5 | 25 | 622 | N/A | N/A |  |
|  | n66 | 1720 | 5 | 25 | 2120 | N/A | N/A |  |
|  | n77 | N/A | 10 | N/A | 4108 | 15.9 | IMD34,9,11 |  |
|  | 71 | 690 | 5 | 25 | 644 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2150 | 15.5 | IMD39,11 |  |
|  | n77 | 3530 | 10 | 50 | 3530 | N/A | N/A |  |
| DC_71A_n66A-n78A | 71 | 693 | 5 | 25 | 647 | N/A | N/A |  |
|  | n78 | 3546 | 10 | 50 | 3546 | N/A | N/A |  |
|  | n66 | N/A | 5 | N/A | 2160 | 15.5 | IMD3 |  |
|  | 71 | 665.5 | 5 | 25 | 619.5 | N/A | N/A |  |
|  | n78 | N/A | 10 | N/A | 3697.5 | 13.0 | IMD4 |  |
|  | n66 | 1712.5 | 5 | 25 | 2112.5 | N/A | N/A |  |
| NOTE 1: This band is subject to IMD3 also which MSD is not specified.NOTE 2: For DC_3A_n3A-n77A, DC_3A_n3A-n78A paired with UL_DC_3A_n3A, the 3rd DL bands n77/n78 are subject to IMD2 which MSD is not specifiedNOTE 3: This MSD requirement apply with both IMD2 and IMD3 products should be generated.NOTE 4: This band is subject to IMD5 also which MSD is not specified.NOTE 5: When Band 46 have self-interference problems by dual uplink CA/EN-DC, then the requirements do not apply in exclusion zone which is frequency range within (harmonics frequency region +  FHD) and IMD frequency region as follow. IMD frequency rangeNOTE 6:  VoidNOTE 7: This band is also subject to IMD2 which is not specified. The frequency range below 3400MHz in n77 is not used for this combination.NOTE 8: Band 5 is also affected by IMD5 from UL DC_2A_n12A, but MSD value is not specified as there is only partial overlap of IMD5 with DL carrier.NOTE 9: This band is subject to IMD4 also which MSD is not specified.NOTE 10: The frequency range in band n28 is restricted for this band combination to 728 – 738 MHz for the UL and 783 – 793 MHz for the DL. This band is subject to IMD2 fall in B1 also which MSD is not specified.NOTE 11: For a UE which supports this band combination only when the Band n77 frequency range restriction defined in NOTE 12 of Table 5.2-1 from TS 38.101-1 applies, the MSD test point(s) cannot be verified for the band combination and the test point(s) can be skipped.NOTE 12: Applicable only if operation with 4 antenna ports is supported in the band with carrier aggregation configured.NOTE 13: VoidNOTE 14: E-UTRA carrier shall be set to min(+20 dBm, PCMAX_L_E-UTRA,c) and NR carrier shall be set to min(+20 dBm, PCMAX_L,f,c,NR) as defined in clause 6.2B.4.1.3.NOTE 15: This band is subject to additional IMD3 for which MSD is not specified.NOTE 16: This band is subject to IMD3 also which MSD is not specified.NOTE 17: The frequency range in band n28 is restricted for this band combination to 728 – 738 MHz for the UL and 783 – 793 MHz for the DL.NOTE 18: In the MSD test configuration, the IMD center does not fall into the DL victim Fc.NOTE 19: This band is subject to 1st order triple-beat IMD3 where MSD is not specified when the UL configuration includes intra-band uplink CCs. NOTE 20: No MSD test points are specified for this combination and verification of IMD impact is not required. |  |  |  |  |  |  |  |  |

Table 7.3B.2.3.5.2-1a: MSD test points for SCell due to dual uplink operation for PC2 EN-DC in NR FR1 (three bands)

| NR or E-UTRA Band / Channel bandwidth / NRB / MSD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EN-DC Configuration |  | EUTRA / NR band |  | UL Fc  (MHz) |  | UL/DL BW  (MHz) |  | ULLCRB |  | DL Fc (MHz) |  | MSD  (dB) |  | IMD order |  |
| DC_1A-3A_n77A |  | 1 |  | 1950 |  | 5 |  | 25 |  | 2140 |  | N/A |  | N/A |  |
| DC_1A-3A_n77(2A) |  | 3 |  | N/A |  | 5 |  | N/A |  | 1807.5 |  | 37.5 |  | IMD25 |  |
| DC_1A-3A_n77(3A) |  | n77 |  | 3757.5 |  | 10 |  | 50 |  | 3757.5 |  | N/A |  | N/A |  |
| DC_1A-3C_n77A |  | 1 |  | N/A |  | 5 |  | N/A |  | 2140 |  | 37.0 |  | IMD21 |  |
| DC_1A-3C_n77(2A) |  | 3 |  | 1775 |  | 5 |  | 25 |  | 1870 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3915 |  | 10 |  | 50 |  | 3915 |  | N/A |  | N/A |  |
| DC_1A-3A_n78ADC_1A-3A_n78(2A) DC_1A-3C_n78ADC_1A-3C_n78(2A) |  | 1 |  | 1950 |  | 5 |  | 25 |  | 2140 |  | N/A |  | N/A |  |
|  |  | 3 |  | N/A |  | 5 |  | N/A |  | 1807.5 |  | 37.2 |  | IMD21 |  |
|  |  | n78 |  | 3757.5 |  | 10 |  | 50 |  | 3757.5 |  | N/A |  | N/A |  |
|  |  | 1 |  | N/A |  | 5 |  | N/A |  | 2125 |  | 17.8 |  | IMD5 |  |
|  |  | 3 |  | 1775 |  | 5 |  | 25 |  | 1870 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3725 |  | 10 |  | 50 |  | 3725 |  | N/A |  | N/A |  |
| DC_1A-3A_n79A |  | 1 |  | N/A |  | 5 |  | N/A |  | 2140 |  | 24.6 |  | IMD5 |  |
|  |  | 3 |  | 1750 |  | 5 |  | 25 |  | 1845 |  | N/A |  | N/A |  |
|  |  | n79 |  | 4860 |  | 10 |  | 50 |  | 4860 |  | N/A |  | N/A |  |
| DC_1A-5A_n78A |  | 1 |  | N/A |  | 5 |  | N/A |  | 2120 |  | 19.2 |  | IMD4 |  |
|  |  | 5 |  | 844 |  | 5 |  | 25 |  | 889 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3670 |  | 10 |  | 52 |  | 3670 |  | N/A |  | N/A |  |
|  |  | 1 |  | 1950 |  | 5 |  | 25 |  | 2140 |  | N/A |  | N/A |  |
|  |  | 5 |  | N/A |  | 5 |  | N/A |  | 889 |  | 19.2 |  | IMD4 |  |
|  |  | n78 |  | 3421 |  | 10 |  | 52 |  | 3421 |  | N/A |  | N/A |  |
|  |  | 1 |  | N/A |  | 5 |  | N/A |  | 2122 |  | 27.0 |  | IMD3 |  |
|  |  | 5 |  | 829 |  | 5 |  | 25 |  | 874 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3780 |  | 10 |  | 52 |  | 3780 |  | N/A |  | N/A |  |
|  |  | 1 |  | 1975 |  | 5 |  | 25 |  | 2165 |  | N/A |  | N/A |  |
|  |  | 5 |  | N/A |  | 5 |  | N/A |  | 885 |  | 13.2 |  | IMD5 |  |
|  |  | n78 |  | 3405 |  | 10 |  | 52 |  | 3405 |  | N/A |  | N/A |  |
| DC_1A-7A_n78A |  | 1 |  | N/A |  | 5 |  | N/A |  | 2120 |  | 19.2 |  | IMD4 |  |
|  |  | 7 |  | 2550 |  | 5 |  | 25 |  | 2670 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3670 |  | 10 |  | 52 |  | 3670 |  | N/A |  | N/A |  |
|  |  | 1 |  | 1977.5 |  | 5 |  | 25 |  | 2167.5 |  | N/A |  | N/A |  |
|  |  | 7 |  | N/A |  | 5 |  | N/A |  | 2627.5 |  | 20.2 |  | IMD4 |  |
|  |  | n78 |  | 3305 |  | 10 |  | 50 |  | 3305 |  | N/A |  | N/A |  |
|  |  | 1 |  | N/A |  | 5 |  | N/A |  | 2140 |  | 19.7 |  | IMD4 |  |
|  |  | 7 |  | 2510 |  | 10 |  | 50 |  | 2630 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3580 |  | 10 |  | 50 |  | 3580 |  | N/A |  | N/A |  |
| DC_1A-8A_n77A |  | 1 |  | 1955 |  | 5 |  | 25 |  | 2145 |  | N/A |  | N/A |  |
| DC_1A-8A_n77(2A)DC_1A-8A_n77(3A) |  | 8 |  | 910 |  | 5 |  | 25 |  | 955 |  | 15.7 |  | IMD5 |  |
|  |  | n77 |  | 3410 |  | 10 |  | 50 |  | 3410 |  | N/A |  | N/A |  |
|  |  | 1 |  | 1950 |  | 5 |  | 25 |  | 2140 |  | 23.4 |  | IMD3 |  |
|  |  | 8 |  | 910 |  | 5 |  | 25 |  | 955 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3960 |  | 10 |  | 50 |  | 3960 |  | N/A |  | N/A |  |
| DC_1A-8A_n78A |  | 1 |  | 1955 |  | 5 |  | 25 |  | 2145 |  | N/A |  | N/A |  |
| DC_1A-8A_n78(2A) |  | 8 |  | 910 |  | 5 |  | 25 |  | 955 |  | 15.7 |  | IMD5 |  |
|  |  | n78 |  | 3410 |  | 10 |  | 50 |  | 3410 |  | N/A |  | N/A |  |
| DC_1A_n8A-n78A |  | 1 |  | 1940 |  | 5 |  | 25 |  | 2130 |  | N/A |  | N/A |  |
|  |  | n8 |  | N/A |  | 5 |  | N/A |  | 940 |  | 15 |  | IMD5 |  |
|  |  | n78 |  | 3380 |  | 10 |  | 50 |  | 3330 |  | N/A |  | N/A |  |
| DC_1A-11A_n77A |  | 1 |  | 1955 |  | 5 |  | 25 |  | 2145 |  | N/A |  | N/A |  |
|  |  | 11 |  | N\|/A |  | 5 |  | N/A |  | 1486 |  | 37.6 |  | IMD2 |  |
|  |  | n77 |  | 3441 |  | 10 |  | 50 |  | 3441 |  | N/A |  | N/A |  |
| DC_1A-11A_n79A |  | 1 |  | 1970 |  | 5 |  | 25 |  | 2160 |  | N/A |  | N/A |  |
|  |  | 11 |  | N/A |  | 5 |  | N/A |  | 1483 |  | 22.2 |  | IMD4 |  |
|  |  | n79 |  | 4427 |  | 40 |  | 216 |  | 4427 |  | N/A |  | N/A |  |
| DC_1A-18A_n77A |  | 1 |  | 1970 |  | 5 |  | 25 |  | 2160 |  | N/A |  | N/A |  |
|  |  | 18 |  | N/A |  | 5 |  | N/A |  | 870 |  | 15.8 |  | IMD5 |  |
|  |  | n77 |  | 3390 |  | 10 |  | 50 |  | 3390 |  | N/A |  | N/A |  |
|  |  | 1 |  | N/A |  | 5 |  | N/A |  | 2120 |  | 25.0 |  | IMD3 |  |
|  |  | 18 |  | 825 |  | 5 |  | 25 |  | 870 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3770 |  | 10 |  | 50 |  | 3770 |  | N/A |  | N/A |  |
| DC_1A-19A_n77ADC_1A-19A_n77(2A) |  | 1 |  | N/A |  | 5 |  | N/A |  | 2130 |  | 26.7 |  | IMD3 |  |
|  |  | 19 |  | 832.5 |  | 5 |  | 25 |  | 877.5 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3795 |  | 10 |  | 50 |  | 3795 |  | N/A |  | N/A |  |
|  |  | 1 |  | 1940 |  | 5 |  | 25 |  | 2130 |  | N/A |  | N/A |  |
|  |  | 19 |  | N/A |  | 5 |  | N/A |  | 880 |  | 18.5 |  | IMD5 |  |
|  |  | n77 |  | 3350 |  | 10 |  | 50 |  | 3350 |  | N/A |  | N/A |  |
| DC_1A-19A_n78ADC_1A-19A_n78(2A) |  | 1 |  | N/A |  | 5 |  | N/A |  | 2130 |  | 26.7 |  | IMD3 |  |
|  |  | 19 |  | 832.5 |  | 5 |  | 25 |  | 877.5 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3795 |  | 10 |  | 50 |  | 3795 |  | N/A |  | N/A |  |
|  |  | 1 |  | 1940 |  | 5 |  | 25 |  | 2130 |  | N/A |  | N/A |  |
|  |  | 19 |  | N/A |  | 5 |  | N/A |  | 880 |  | 18.5 |  | IMD5 |  |
|  |  | n78 |  | 3350 |  | 10 |  | 50 |  | 3350 |  | N/A |  | N/A |  |
| DC_1A-19A_n79A |  | 1 |  | 1950 |  | 5 |  | 25 |  | 2140 |  | N/A |  | N/A |  |
|  |  | 19 |  | N/A |  | 5 |  | N/A |  | 882.5 |  | 33.3 |  | IMD35 |  |
|  |  | n79 |  | 4782.5 |  | 10 |  | 50 |  | 4782.5 |  | N/A |  | N/A |  |
|  |  | 1 |  | N/A |  | 5 |  | N/A |  | 2140 |  | 26.1 |  | IMD4 |  |
|  |  | 19 |  | 837.5 |  | 5 |  | 25 |  | 882.5 |  | N/A |  | N/A |  |
|  |  | n79 |  | 4652.5 |  | 10 |  | 50 |  | 4652.5 |  | N/A |  | N/A |  |
| DC_1A-21A_n77ADC_1A-21A_n77(2A) |  | 1 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |
|  |  | 21 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | IMD2 |  |
|  |  | n77 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |
|  |  | 1 |  | 1950 |  | 5 |  | 25 |  | 2140 |  | N/A |  | N/A |  |
|  |  | 21 |  | N/A |  | 5 |  | N/A |  | 1500 |  | 17.9 |  | IMD5 |  |
|  |  | n77 |  | 3605 |  | 10 |  | 50 |  | 3605 |  | N/A |  | N/A |  |
|  |  | 1 |  | N/A |  | 5 |  | N/A |  | 2154.6 |  | 36.6 |  | IMD21 |  |
|  |  | 21 |  | 1450.4 |  | 5 |  | 25 |  | 1498.4 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3605 |  | 10 |  | 50 |  | 3605 |  | N/A |  | N/A |  |
| DC_1A-21A_n78ADC_1A-21A_n78(2A) |  | 1 |  | N/A |  | 5 |  | N/A |  | 2154.6 |  | 36.6 |  | IMD2 |  |
|  |  | 21 |  | 1450.4 |  | 5 |  | 25 |  | 1498.4 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3605 |  | 10 |  | 50 |  | 3605 |  | N/A |  | N/A |  |
|  |  | 1 |  | N/A |  | 5 |  | N/A |  | 2154.6 |  | 16.2 |  | IMD5 |  |
|  |  | 21 |  | 1450.4 |  | 5 |  | 25 |  | 1498.4 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3647 |  | 10 |  | 50 |  | 3647 |  | N/A |  | N/A |  |
|  |  | 1 |  | 1950 |  | 5 |  | 25 |  | 2140 |  | N/A |  | N/A |  |
|  |  | 21 |  | N/A |  | 5 |  | N/A |  | 1500 |  | 37.5 |  | IMD2 |  |
|  |  | n78 |  | 3450 |  | 10 |  | 50 |  | 3450 |  | N/A |  | N/A |  |
|  |  | 1 |  | 1950 |  | 5 |  | 25 |  | 2140 |  | N/A |  | N/A |  |
|  |  | 21 |  | N/A |  | 5 |  | N/A |  | 1500 |  | 14.9 |  | IMD5 |  |
|  |  | n78 |  | 3675 |  | 10 |  | 50 |  | 3675 |  | N/A |  | N/A |  |
| DC_1A-21A_n79A7,8 |  | 1 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |
|  |  | 21 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | IMD4 |  |
|  |  | n79 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |
| DC_1A_n28A-n77ADC_1A_n28A-n77(2A) |  | 1 |  | 1950 |  | 5 |  | 25 |  | 2140 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3320 |  | 10 |  | 50 |  | 3320 |  | N/A |  | N/A |  |
|  |  | n28 |  | N/A |  | 5 |  | 25 |  | 790 |  | 18.7 |  | IMD5 |  |
| DC_1A-41A_n77A |  | 1 |  | 1970 |  | 5 |  | 25 |  | 2160 |  | N/A |  | N/A |  |
| DC_1A-41C_n77A |  | 41 |  | N/A |  | 5 |  | N/A |  | 2510 |  | 22.5 |  | IMD4 |  |
|  |  | n77 |  | 3400 |  | 10 |  | 50 |  | 3400 |  | N/A |  | N/A |  |
|  |  | 1 |  | 1930 |  | 5 |  | 25 |  | 2120 |  | N/A |  | N/A |  |
|  |  | 41 |  | N/A |  | 5 |  | N/A |  | 2510 |  | 15.6 |  | IMD5 |  |
|  |  | n77 |  | 4150 |  | 10 |  | 50 |  | 4150 |  | N/A |  | N/A |  |
| DC_1A_n41A-n77A |  | 1 |  | 1975 |  | 5 |  | 25 |  | 2165 |  | N/A |  | N/A |  |
|  |  | n41 |  | N/A |  | 10 |  | N/A |  | 2515 |  | 22.0 |  | IMD41 |  |
|  |  | n77 |  | 3410 |  | 10 |  | 50 |  | 3410 |  | N/A |  | N/A |  |
|  |  | 1 |  | 1970 |  | 5 |  | 25 |  | 2160 |  | N/A |  | N/A |  |
|  |  | n41 |  | 2650 |  | 10 |  | 25 |  | 2650 |  | N/A |  | N/A |  |
|  |  | n77 |  | N/A |  | 10 |  | N/A |  | 3330 |  | 28.2 |  | IMD31,5 |  |
| DC_1A-42A_n79ADC_1A-42C_n79ADC_1A-42D_n79ADC_1A-42E_n79A |  | 1 |  | 1977.5 |  | 5 |  | 25 |  | 2167.5 |  | N/A |  | N/A |  |
|  |  | 42 |  | N/A |  | 5 |  | N/A |  | 3490 |  | 25.8 |  | IMD5 |  |
|  |  | n79 |  | 4420 |  | 10 |  | 50 |  | 4420 |  | N/A |  | N/A |  |
| DC_1A_n78A-n79A |  | 1 |  | 1950 |  | 5 |  | 25 |  | 2140 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3410 |  | 10 |  | 50 |  | 3410 |  | N/A |  | N/A |  |
|  |  | n79 |  | N/A |  | 10 |  | N/A |  | 4870 |  | 24.9 |  | IMD31 |  |
|  |  | 1 |  | 1950 |  | 5 |  | 25 |  | 2140 |  | N/A |  | N/A |  |
|  |  | n78 |  | N/A |  | 10 |  | N/A |  | 3490 |  | 22.6 |  | IMD5 |  |
|  |  | n79 |  | 4670 |  | 10 |  | 50 |  | 4670 |  | N/A |  | N/A |  |
| DC_2A_n2A-n77ADC_2A_n2A-n77C |  | 2 |  | 1875 |  | 5 |  | 25 |  | 1955 |  | N/A |  | N/A |  |
|  |  | n2 |  | 1855 |  | 5 |  | 25 |  | 1935 |  | 32.0 |  | IMD25 |  |
|  |  | n77 |  | 3810 |  | 10 |  | 50 |  | 3810 |  | N/A |  | N/A |  |
| DC_2A-5A_n77A2DC_2A-5A_n77(2A)2 DC_2A-2A-5A_n77A2DC_2A-2A-5A_n77(2A)2DC_2A-5A_n77C2DC_2A-2A-5A_n77C2 |  | 2 |  | 1907.5 |  | 5 |  | 25 |  | 1987.5 |  | N/A |  | N/A |  |
|  |  | 5 |  | N/A |  | 5 |  | N/A |  | 887.5 |  | 13.6 |  | IMD5 |  |
|  |  | n77 |  | 3305 |  | 10 |  | 50 |  | 3305 |  | N/A |  | N/A |  |
|  |  | 2 |  | N/A |  | 5 |  | N/A |  | 1987 |  | 24.8 |  | IMD3 |  |
|  |  | 5 |  | 846.5 |  | 5 |  | 25 |  | 891.5 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3680 |  | 10 |  | 50 |  | 3680 |  | N/A |  | N/A |  |
| DC_2A_n5A-n77A2 DC_2A-2A_n5A-n77A2DC_2A_n5A-n77C2DC_2A-2A_n5A-n77C2 |  | 2 |  | 1907 |  | 5 |  | 25 |  | 1987 |  | N/A |  | N/A |  |
|  |  | n5 |  | N/A |  | 5 |  | N/A |  | 889 |  | 13.6 |  | IMD52 |  |
|  |  | n77 |  | 3305 |  | 10 |  | 50 |  | 3305 |  | N/A |  | N/A |  |
| DC_2A-7A_n78A |  | 2 |  | 1870 |  | 5 |  | 25 |  | 1950 |  | 20.0 |  | IMD4 |  |
|  |  | 7 |  | 2550 |  | 5 |  | 25 |  | 2685 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3525 |  | 10 |  | 50 |  | 3525 |  | N/A |  | N/A |  |
| DC_2A-12A_n77ADC_2A-12A_n77(2A)DC_2A-2A-12A_n77ADC_2A-2A-12A_n77(2A) |  | 2 |  | N/A |  | 5 |  | N/A |  | 1960 |  | 24.8 |  | IMD32, 5 |  |
|  |  | 12 |  | 707.5 |  | 5 |  | 25 |  | 737.5 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3375 |  | 10 |  | 50 |  | 3375 |  | N/A |  | N/A |  |
| DC_2A-13A_n77ADC_2A-2A-13A_n77ADC_2A-13A_n77CDC_2A-2A-13A_n77C |  | 2 |  | N/A |  | 5 |  | N/A |  | 1944 |  | 24.2 |  | IMD3 |  |
|  |  | 13 |  | 783 |  | 5 |  | 25 |  | 752 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3510 |  | 10 |  | 50 |  | 3510 |  | N/A |  | N/A |  |
| DC_2A-14A_n77ADC_2A-14A_n77(2A)DC_2A-2A-14A_n77ADC_2A-2A-14A_n77(2A) |  | 2 |  | N/A |  | 5 |  | N/A |  | 1954 |  | 24.8 |  | IMD3 |  |
|  |  | 14 |  | 793 |  | 5 |  | 25 |  | 763 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3540 |  | 10 |  | 50 |  | 3540 |  | N/A |  | N/A |  |
| DC_2A-30A_n77ADC_2A-30A_n77(2A)DC_2A-2A-30A_n77ADC_2A-2A-30A_n77(2A) |  | 2 |  | N/A |  | 5 |  | N/A |  | 1986 |  | 19.3 |  | IMD42 |  |
|  |  | 30 |  | 2312 |  | 5 |  | 25 |  | 2357 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3305 |  | 10 |  | 50 |  | 3305 |  | N/A |  | N/A |  |
|  |  | 2 |  | 1905 |  | 5 |  | 25 |  | 1985 |  | N/A |  | N/A |  |
|  |  | 30 |  | N/A |  | 5 |  | N/A |  | 2354 |  | 22.2 |  | IMD42 |  |
|  |  | n77 |  | 3361 |  | 10 |  | 50 |  | 3361 |  | N/A |  | N/A |  |
|  |  | 2 |  | 1860 |  | 5 |  | 25 |  | 1940 |  | N/A |  | N/A |  |
|  |  | 30 |  | N/A |  | 5 |  | N/A |  | 2354 |  | 12.9 |  | IMD5 |  |
|  |  | n77 |  | 3967 |  | 10 |  | 50 |  | 3967 |  | N/A |  | N/A |  |
| DC_2A-66A_n41A |  | 2 |  | N/A |  | 5 |  | N/A |  | 1940 |  | 21.5 |  | IMD4 |  |
|  |  | 66 |  | 1715 |  | 5 |  | 25 |  | 2115 |  | N/A |  | N/A |  |
|  |  | n41 |  | 2685 |  | 10 |  | 50 |  | 2685 |  | N/A |  | N/A |  |
| DC_2A-66A_n77ADC_2A-66A_n77(2A)DC_2A-2A-66A_n77ADC_2A-2A-66A_n77(2A)DC_2A-66A-66A_n77ADC_2A-66A-66A_n77(2A)DC_2A-2A-66A-66A_n77ADC_2A-66A_n77CDC_2A-66A-66A_n77CDC_2A-2A-66A-66A_n77C |  | 2 |  | 1855 |  | 5 |  | 25 |  | 1935 |  | N/A |  | N/A |  |
|  |  | 66 |  | N/A |  | 5 |  | N/A |  | 2115 |  | 34.7 |  | IMD25 |  |
|  |  | n77 |  | 3970 |  | 10 |  | 50 |  | 3970 |  | N/A |  | N/A |  |
|  |  | 2 |  | N/A |  | 5 |  | N/A |  | 1960 |  | 37.6 |  | IMD25 |  |
|  |  | 66 |  | 1760 |  | 5 |  | 25 |  | 2160 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3720 |  | 10 |  | 50 |  | 3720 |  | N/A |  | N/A |  |
| DC_2A_n66A-n77A DC_2A-2A_n66A-n77ADC_2A_n66A-n77CDC_2A-2A_n66A-n77C |  | 2 |  | 1855 |  | 5 |  | 25 |  | 1935 |  | N/A |  | N/A |  |
|  |  | n66 |  | N/A |  | 5 |  | N/A |  | 2115 |  | 35.2 |  | IMD25 |  |
|  |  | n77 |  | 3970 |  | 10 |  | 50 |  | 3970 |  | N/A |  | N/A |  |
| DC_2A-66A_n78A |  | 2 |  | 1880 |  | 5 |  | 25 |  | 1960 |  | M/A |  | N/A |  |
|  |  | 66 |  | 1740 |  | 5 |  | 25 |  | 2140 |  | 21.1 |  | IMD4 |  |
|  |  | n78 |  | 3500 |  | 10 |  | 50 |  | 3500 |  | N/A |  | N/A |  |
|  |  | 2 |  | 1880 |  | 5 |  | 25 |  | 1960 |  | 37.6 |  | IMD25 |  |
|  |  | 66 |  | 1760 |  | 5 |  | 25 |  | 2160 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3720 |  | 10 |  | 50 |  | 3720 |  | N/A |  | N/A |  |
|  |  | 2 |  | 1880 |  | 5 |  | 25 |  | 1960 |  | 13.2 |  | IMD5 |  |
|  |  | 66 |  | 1760 |  | 5 |  | 25 |  | 2160 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3620 |  | 10 |  | 50 |  | 3620 |  | N/A |  | N/A |  |
| DC_3A_n1A-n78ADC_3A-3A_n1A-n78A |  | 3 |  | 1770 |  | 5 |  | 25 |  | 1865 |  | N/A |  | N/A |  |
|  |  | n1 |  | N/A |  | 5 |  | N/A |  | 2130 |  | 17.8 |  | IMD5 |  |
|  |  | n78 |  | 3720 |  | 10 |  | 50 |  | 3720 |  | N/A |  | N/A |  |
| DC_3A_n1A-n79A |  | n1 |  | N/A |  | 5 |  | N/A |  | 2140 |  | 18.7 |  | IMD5 |  |
|  |  | 3 |  | 1750 |  | 5 |  | 25 |  | 1845 |  | N/A |  | N/A |  |
|  |  | n79 |  | 4860 |  | 40 |  | 216 |  | 4860 |  | N/A |  | N/A |  |
| DC_3A-7A_n78ADC_3A-3A-7A_n78ADC_3A-7A-7A_n78ADC_3A-3A-7A-7A_n78A |  | 3 |  | N/A |  | 5 |  | N/A |  | 1820 |  | 26.5 |  | IMD35 |  |
|  |  | 7 |  | 2565 |  | 5 |  | 25 |  | 2685 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3310 |  | 10 |  | 50 |  | 3310 |  | N/A |  | N/A |  |
| DC_3A-8A_n77A |  | 3 |  | 1715 |  | 5 |  | 25 |  | 1810 |  | N/A |  | N/A |  |
| DC_3C-8A_n77A |  | 8 |  | 910 |  | 5 |  | 25 |  | 955 |  | 21.2 |  | IMD4 |  |
| DC_3A-8A_n77(2A) |  | n77 |  | 4190 |  | 10 |  | 50 |  | 4190 |  | N/A |  | N/A |  |
| DC_3C-8A_n77(2A)DC_3A-8A_n77(3A) |  | 3 |  | 1725 |  | 5 |  | 25 |  | 1820 |  | 24.8 |  | IMD3 |  |
|  |  | 8 |  | 910 |  | 5 |  | 25 |  | 955 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3640 |  | 10 |  | 50 |  | 3640 |  | N/A |  | N/A |  |
| DC_3A-8A_n78ADC_3A-8B_n78ADC_3A-3A-8A_n78ADC_3A-3A-8B_n78ADC_3C-8A_n78ADC_3A-8A_n78(2A) |  | 8 |  | 910 |  | 5 |  | 25 |  | 955 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3640 |  | 10 |  | 50 |  | 3640 |  | N/A |  | N/A |  |
|  |  | 3 |  | N/A |  | 5 |  | N/A |  | 1820 |  | 24.8 |  | IMD3 |  |
| DC_3A-8A_n79A |  | 8 |  | 910 |  | 5 |  | 25 |  | 955 |  | N/A |  | N/A |  |
|  |  | n79 |  | 4580 |  | 40 |  | 216 |  | 4580 |  | N/A |  | N/A |  |
|  |  | 3 |  | N/A |  | 5 |  | N/A |  | 1850 |  | 21.2 |  | IMD4 |  |
| DC_3A-11A_n77A |  | 3 |  | 1720 |  | 5 |  | 25 |  | 1815 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3675 |  | 10 |  | 50 |  | 3675 |  | N/A |  | N/A |  |
|  |  | 11 |  | N/A |  | 5 |  | N/A |  | 1491 |  | 20.2 |  | IMD4 |  |
| DC_3A-18A_n77A |  | 3 |  | N/A |  | 5 |  | N/A |  | 1865 |  | 24.2 |  | IMD3 |  |
|  |  | 18 |  | 820 |  | 5 |  | 25 |  | 865 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3505 |  | 10 |  | 50 |  | 3505 |  | N/A |  | N/A |  |
| DC_3A-19A_n77ADC_3A-19A_n77(2A) |  | 3 |  | N/A |  | 5 |  | N/A |  | 1850 |  | 26.3 |  | IMD3 |  |
|  |  | 19 |  | 835 |  | 5 |  | 25 |  | 880 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3520 |  | 10 |  | 50 |  | 3520 |  | N/A |  | N/A |  |
| DC_3A-19A_n78ADC_3A-19A_n78(2A) |  | 3 |  | N/A |  | 5 |  | N/A |  | 1850 |  | 26.3 |  | IMD3 |  |
|  |  | 19 |  | 835 |  | 5 |  | 25 |  | 880 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3520 |  | 10 |  | 50 |  | 3520 |  | N/A |  | N/A |  |
| DC_3A-19A_n79A |  | 3 |  | 1775 |  | 5 |  | 25 |  | 1870 |  | N/A |  | N/A |  |
|  |  | 19 |  | N/A |  | 5 |  | N/A |  | 885 |  | 27.5 |  | IMD35 |  |
|  |  | n79 |  | 4435 |  | 40 |  | 216 |  | 4435 |  | N/A |  | N/A |  |
|  |  | 3 |  | N/A |  | 5 |  | N/A |  | 1877.5 |  | 16.2 |  | IMD4 |  |
|  |  | 19 |  | 842.5 |  | 5 |  | 25 |  | 887.5 |  | N/A |  | N/A |  |
|  |  | n79 |  | 4420 |  | 40 |  | 216 |  | 4420 |  | N/A |  | N/A |  |
| DC_3A-21A_n77ADC_3A-21A_n77(2A) |  | 3 |  | 1767.5 |  | 5 |  | 25 |  | 1862.5 |  | N/A |  | N/A |  |
|  |  | 21 |  | N/A |  | 5 |  | N/A |  | 1507.5 |  | 20.8 |  | IMD4 |  |
|  |  | n77 |  | 3795 |  | 10 |  | 50 |  | 3795 |  | N/A |  | N/A |  |
|  |  | 3 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | IMD2 |  |
|  |  | 21 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |
|  |  | n77 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |
|  |  | 3 |  | N/A |  | 5 |  | N/A |  | 1866.6 |  | 18.4 |  | IMD5 |  |
|  |  | 21 |  | 1450.4 |  | 5 |  | 25 |  | 1498.4 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3935 |  | 10 |  | 50 |  | 3935 |  | N/A |  | N/A |  |
| DC_3A-21A_n78ADC_3A-21A_n78(2A) |  | 3 |  | N/A |  | 5 |  | N/A |  | 1862.5 |  | 36.6 |  | IMD2 |  |
|  |  | 21 |  | 1459.5 |  | 5 |  | 25 |  | 1507.5 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3322 |  | 10 |  | 50 |  | 3322 |  | N/A |  | N/A |  |
|  |  | 3 |  | 1767.5 |  | 5 |  | 25 |  | 1862.5 |  | N/A |  | N/A |  |
|  |  | 21 |  | 1459.5 |  | 5 |  | 25 |  | 1507.5 |  | 23.2 |  | IMD4 |  |
|  |  | n78 |  | 3795 |  | 10 |  | 50 |  | 3795 |  | N/A |  | N/A |  |
|  |  | 3 |  | 1767.5 |  | 5 |  | 25 |  | 1862.5 |  | N/A |  | N/A |  |
|  |  | 21 |  | N/A |  | 5 |  | N/A |  | 1503.5 |  | 9.5 |  | IMD5 |  |
|  |  | n78 |  | 3403 |  | 10 |  | 50 |  | 3403 |  | N/A |  | N/A |  |
| DC_3A-21A_n79A7 |  | 3 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |
|  |  | 21 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | IMD3 |  |
|  |  | n79 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |
|  |  | 3 |  | N/A |  | 5 |  | N/A |  | 1869.2 |  | 32.8 |  | IMD3 |  |
|  |  | 21 |  | 1450.4 |  | 5 |  | 25 |  | 1498.4 |  | N/A |  | N/A |  |
|  |  | n79 |  | 4770 |  | 10 |  | 50 |  | 4770 |  | N/A |  | N/A |  |
| DC_3A-28A_n41A |  | 3 |  | 1720 |  | 5 |  | 25 |  | 1815 |  | N/A |  | N/A |  |
|  |  | n41 |  | 2510 |  | 10 |  | 50 |  | 2510 |  | N/A |  | N/A |  |
|  |  | 28 |  | N/A |  | 5 |  | N/A |  | 790 |  | 30.5 |  | IMD211 |  |
|  |  | 3 |  | N/A |  | 5 |  | N/A |  | 1832.5 |  | 32 |  | IMD2 |  |
|  |  | n41 |  | 2543 |  | 10 |  | 50 |  | 2543 |  | N/A |  | N/A |  |
|  |  | 28 |  | 710.5 |  | 5 |  | 25 |  | 765.5 |  | N/A |  | N/A |  |
| DC_3A-28A_n77A |  | 3 |  | 1712.5 |  | 5 |  | 25 |  | 1807.5 |  | N/A |  | N/A |  |
|  |  | 28 |  | N/A |  | 5 |  | N/A |  | 770 |  | 24.2 |  | IMD3 |  |
|  |  | n77 |  | 4195 |  | 10 |  | 50 |  | 4195 |  | N/A |  | N/A |  |
|  |  | 3 |  | N/A |  | 5 |  | N/A |  | 1850 |  | 25.8 |  | IMD35 |  |
|  |  | 28 |  | 735 |  | 5 |  | 25 |  | 790 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3320 |  | 10 |  | 50 |  | 3320 |  | N/A |  | N/A |  |
| DC_3A_n28A-n77ADC_3A_n28A-n77(2A) |  | 3 |  | 1712.5 |  | 5 |  | 25 |  | 1807.5 |  | N/A |  | N/A |  |
|  |  | n28 |  | 715 |  | 5 |  | 25 |  | 770 |  | 24.2 |  | IMD3 |  |
|  |  | n77 |  | 4195 |  | 10 |  | 50 |  | 4195 |  | N/A |  | N/A |  |
| DC_3A-28A_n78A |  | 3 |  | N/A |  | 5 |  | N/A |  | 1850 |  | 25.9 |  | IMD3 |  |
|  |  | 28 |  | 735 |  | 5 |  | 25 |  | 790 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3320 |  | 10 |  | 50 |  | 3320 |  | N/A |  | N/A |  |
| DC_3A_n41A-n77A |  | 3 |  | 1720 |  | 5 |  | 25 |  | 1815 |  | N/A |  | N/A |  |
|  |  | n41 |  | 2580 |  | 10 |  | 50 |  | 2580 |  | N/A |  | N/A |  |
|  |  | n77 |  | N/A |  | 10 |  | N/A |  | 3440 |  | 23.9 |  | IMD31 |  |
|  |  | 3 |  | 1720 |  | 5 |  | 25 |  | 1815 |  | N/A |  | N/A |  |
|  |  | n41 |  | N/A |  | 10 |  | N/A |  | 2640 |  | 17.6 |  | IMD5 |  |
|  |  | n77 |  | 3900 |  | 10 |  | 50 |  | 3900 |  | N/A |  | N/A |  |
| DC_3A-41A_n77ADC_3A-41C_n77ADC_3A-41A_n77(2A)DC_3A-41C_n77(2A) |  | 3 |  | 1720 |  | 5 |  | 25 |  | 1815 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3900 |  | 10 |  | 50 |  | 3900 |  | N/A |  | N/A |  |
|  |  | 41 |  | N/A |  | 5 |  | N/A |  | 2640 |  | 13 |  | IMD5 |  |
| DC_3A-42A_n79A9DC_3A-42C_n79A9DC_3A-42D_n79A9DC_3A-42E_n79A9 |  | 3 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |
|  |  | 42 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | IMD5 |  |
|  |  | n79 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |
| DC_3A_n78A-n79A |  | 3 |  | 1770 |  | 5 |  | 25 |  | 1865 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3340 |  | 10 |  | 50 |  | 3340 |  | N/A |  | N/A |  |
|  |  | n79 |  | N/A |  | 10 |  | N/A |  | 4910 |  | 25.3 |  | IMD3 |  |
|  |  | 3 |  | 1770 |  | 5 |  | 25 |  | 1865 |  | N/A |  | N/A |  |
|  |  | n78 |  | N/A |  | 10 |  | N/A |  | 3710 |  | 25.2 |  | IMD5 |  |
|  |  | n79 |  | 4510 |  | 10 |  | 50 |  | 4510 |  | N/A |  | N/A |  |
| DC_5A_n2A-n77A2  DC_5A_n2A-n77C2 |  | n2 |  | N/A |  | 5 |  | N/A |  | 1987 |  | 25.5 |  | IMD3 |  |
|  |  | 5 |  | 846.5 |  | 5 |  | 25 |  | 891.5 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3680 |  | 10 |  | 50 |  | 3680 |  | N/A |  | N/A |  |
| DC_5A_n5A-n77A2  DC_5A_n5A-n77C2 |  | 5 |  | 834 |  | 5 |  | 25 |  | 879 |  | N/A |  | N/A |  |
|  |  | n5 |  | N/A |  | 5 |  | N/A |  | 889 |  | 20.3 |  | IMD41 |  |
|  |  | n77 |  | 3391 |  | 10 |  | 50 |  | 3391 |  | N/A |  | N/A |  |
| DC_5A-13A_n77A2DC_5A-13A_n77C2 |  | 5 |  | 840 |  | 5 |  | 25 |  | 885 |  | N/A |  | N/A |  |
|  |  | 13 |  | N/A |  | 5 |  | N/A |  | 750 |  | 19.4 |  | IMD5 |  |
|  |  | n77 |  | 4110 |  | 10 |  | 50 |  | 4110 |  | N/A |  | N/A |  |
|  |  | 5 |  | N/A |  | 5 |  | N/A |  | 885 |  | 19.5 |  | IMD5 |  |
|  |  | 13 |  | 782 |  | 5 |  | 20 |  | 751 |  | N/A |  | N/A |  |
|  |  | n77 |  | 4013 |  | 10 |  | 50 |  | 4013 |  | N/A |  | N/A |  |
| DC_5A-30A_n77ADC_5A-30A_n77(2A) |  | 5 |  | N/A |  | 5 |  | N/A |  | 880 |  | 23.5 |  | IMD31 |  |
|  |  | 30 |  | 2310 |  | 5 |  | 25 |  | 2355 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3740 |  | 10 |  | 50 |  | 3740 |  | N/A |  | N/A |  |
|  |  | 5 |  | 835 |  | 5 |  | 25 |  | 880 |  | N/A |  | N/A |  |
|  |  | 30 |  | N/A |  | 5 |  | N/A |  | 2355 |  | 21.4 |  | IMD32 |  |
|  |  | n77 |  | 4025 |  | 10 |  | 50 |  | 4025 |  | N/A |  | N/A |  |
| DC_5A-66A_n77ADC_5A-66A_n77(2A)DC_5A-66A-66A_n77ADC_5A-66A-66A_n77(2A) |  | 5 |  | 826.5 |  | 5 |  | 25 |  | 871.5 |  | N/A |  | N/A |  |
|  |  | 66 |  | N/A |  | 5 |  | N/A |  | 2142 |  | 22.2 |  | IMD3 |  |
|  |  | n77 |  | 3795 |  | 10 |  | 50 |  | 3795 |  | N/A |  | N/A |  |
| DC_5A_n66A-n77A  DC_5A_n66A-n77C |  | 5 |  | 826.5 |  | 5 |  | 25 |  | 871.5 |  | N/A |  | N/A |  |
|  |  | n66 |  | N/A |  | 5 |  | N/A |  | 2142 |  | 22.2 |  | IMD3 |  |
|  |  | n77 |  | 3795 |  | 10 |  | 50 |  | 3795 |  | N/A |  | N/A |  |
| DC_7A_n1A-n78ADC_7A-7A_n1A-n78A |  | 1 |  | N/A |  | 5 |  | N/A |  | 2140 |  | 19.7 |  | IMD4 |  |
|  |  | 7 |  | 2510 |  | 10 |  | 50 |  | 2630 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3580 |  | 10 |  | 50 |  | 3580 |  | N/A |  | N/A |  |
| DC_7A_n5A-n78A |  | 7 |  | 2555 |  | 5 |  | 25 |  | 2675 |  | N/A |  | N/A |  |
|  |  | n5 |  | N/A |  | 5 |  | N/A |  | 881 |  | 34.7 |  | IMD21 |  |
|  |  | n78 |  | 3436 |  | 10 |  | 50 |  | 3436 |  | N/A |  | N/A |  |
| DC_7A-8A_n78ADC_7A-8B_n78ADC_7A-7A-8A_n78ADC_7A-7A-8B_n78A |  | 7 |  | 2530 |  | 5 |  | 25 |  | 2650 |  | N/A |  | N/A |  |
|  |  | 8 |  | N/A |  | 5 |  | N/A |  | 940 |  | 35.5 |  | IMD21 |  |
|  |  | n78 |  | 3470 |  | 10 |  | 50 |  | 3470 |  | N/A |  | N/A |  |
|  |  | 7 |  | N/A |  | 5 |  | N/A |  | 2650 |  | 33 |  | IMD2 |  |
|  |  | 8 |  | 895 |  | 5 |  | 25 |  | 940 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3545 |  | 10 |  | 50 |  | 3545 |  | N/A |  | N/A |  |
| DC_7A_n8A-n78ADC_7A-7A_n8A-n78A |  | 7 |  | 2530 |  | 5 |  | 25 |  | 2650 |  | N/A |  | N/A |  |
|  |  | n8 |  | N/A |  | 5 |  | N/A |  | 940 |  | 35.5 |  | IMD21 |  |
|  |  | n78 |  | 3470 |  | 10 |  | 50 |  | 3470 |  | N/A |  | N/A |  |
| DC_7A-28A_n78A |  | 7 |  | 2567.5 |  | 5 |  | 25 |  | 2687.5 |  | N/A |  | N/A |  |
|  |  | 28 |  | N/A |  | 5 |  | N/A |  | 782.5 |  | 33.8 |  | IMD21 |  |
|  |  | n78 |  | 3350 |  | 10 |  | 50 |  | 3350 |  | N/A |  | N/A |  |
|  |  | 7 |  | N/A |  | 5 |  | N/A |  | 2650 |  | 35.5 |  | IMD2 |  |
|  |  | 28 |  | 740 |  | 5 |  | 25 |  | 795 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3390 |  | 10 |  | 50 |  | 3390 |  | N/A |  | N/A |  |
| DC_7A_n28A-n78ADC_7A-7A_n28A-n78A |  | 7 |  | 2565 |  | 5 |  | 25 |  | 2685 |  | N/A |  | N/A |  |
|  |  | n78 |  | 3365 |  | 10 |  | 50 |  | 3365 |  | N/A |  | N/A |  |
|  |  | n28 |  | N/A |  | 5 |  | N/A |  | 800 |  | 33.8 |  | IMD21 |  |
| DC_7A-66A_n78A |  | 7 |  | 2540 |  | 5 |  | 25 |  | 2660 |  | N/A |  | N/A |  |
|  |  | 66 |  | 1760 |  | 5 |  | 25 |  | 2160 |  | 20.5 |  | IMD4 |  |
|  |  | n78 |  | 3620 |  | 10 |  | 50 |  | 3620 |  | N/A |  | N/A |  |
| DC_8A_n1A-n77ADC_8A_n1A-n77(2A) |  | 8 |  | 910 |  | 5 |  | 25 |  | 955 |  | N/A |  | N/A |  |
|  |  | n1 |  | N/A |  | 5 |  | N/A |  | 2140 |  | 27.5 |  | IMD3 |  |
|  |  | n77 |  | 3960 |  | 10 |  | 50 |  | 3960 |  | N/A |  | N/A |  |
| DC_8A_n1A-n79A |  | 8 |  | 900 |  | 5 |  | 25 |  | 945 |  | N/A |  | N/A |  |
|  |  | n1 |  | N/A |  | 5 |  | 25 |  | 2145 |  | 25.7 |  | IMD4 |  |
|  |  | n79 |  | 4845 |  | 40 |  | 216 |  | 4845 |  | N/A |  | N/A |  |
| DC_8A_n3A-n77ADC_8A_n3A-n77(2A) |  | 8 |  | 910 |  | 5 |  | 25 |  | 955 |  | N/A |  | N/A |  |
|  |  | n3 |  | N/A |  | 5 |  | N/A |  | 1820 |  | 24.5 |  | IMD3 |  |
|  |  | n77 |  | 3640 |  | 10 |  | 50 |  | 3640 |  | N/A |  | N/A |  |
| DC_8A_n3A-n79A |  | 8 |  | 910 |  | 5 |  | 25 |  | 955 |  | N/A |  | N/A |  |
|  |  | n3 |  | N/A |  | 5 |  | N/A |  | 1850 |  | 22.7 |  | IMD4 |  |
|  |  | n79 |  | 4580 |  | 40 |  | 216 |  | 4580 |  | N/A |  | N/A |  |
| DC_8A-11A_n77A |  | 8 |  | 910 |  | 5 |  | 25 |  | 955 |  | N/A |  | N/A |  |
|  |  | n77 |  | 3311 |  | 10 |  | 50 |  | 3311 |  | N/A |  | N/A |  |
|  |  | 11 |  | N/A |  | 5 |  | N/A |  | 1491 |  | 28.4 |  | IMD3 |  |
| DC_8A-11A_n79A |  | 8 |  | 882.5 |  | 5 |  | 25 |  | 927.5 |  | N/A |  | N/A |  |
|  |  | n79 |  | 4980 |  | 40 |  | 216 |  | 4980 |  | N/A |  | N/A |  |
|  |  | 11 |  | N/A |  | 5 |  | N/A |  | 1478.4 |  | 16.2 |  | IMD5 |  |
| DC_8A_n28A-n77ADC_8A_n28A-n77(2A) |  | 8 |  | 910 |  | 5 |  | 25 |  | 955 |  | N/A |  | N/A |  |
|  |  | n28 |  | N/A |  | 5 |  | N/A |  | 765 |  | 23 |  | IMD4 |  |
|  |  | n77 |  | 3495 |  | 10 |  | 50 |  | 3495 |  | N/A |  | N/A |  |
| DC_8A_n28A-n78A |  | 8 |  | 910 |  | 5 |  | 25 |  | 955 |  | N/A |  | N/A |  |
|  | n28 |  | N/A |  | 5 |  | N/A |  | 765 |  | 23 |  | IMD4 |  |  |
|  | n78 |  | 3495 |  | 10 |  | 50 |  | 3495 |  | N/A |  | N/A |  |  |
| DC_8A_n28A-n79A | 8 |  | 905 |  | 5 |  | 25 |  | 950 |  | N/A |  | N/A |  |  |
|  | n79 |  | 4420 |  | 40 |  | 216 |  | 4420 |  | N/A |  | N/A |  |  |
|  | n28 |  | N/A |  | 5 |  | N/A |  | 800 |  | 24.0 |  | IMD5 |  |  |
| DC_8A-41A_n77ADC_8A-41C_n77A | 8 |  | 895 |  | 5 |  | 25 |  | 940 |  | N/A |  | N/A |  |  |
|  | 41 |  | N/A |  | 5 |  | N/A |  | 2650 |  | 34.0 |  | IMD2 |  |  |
|  | n77 |  | 3545 |  | 10 |  | 50 |  | 3545 |  | N/A |  | N/A |  |  |
| DC_12A-30A_n77ADC_12A-30A_n77(2A) | 12 |  | N/A |  | 5 |  | N/A |  | 740 |  | 23.5 |  | IMD31 |  |  |
|  | 30 |  | 2310 |  | 5 |  | 25 |  | 2355 |  | N/A |  | N/A |  |  |
|  | n77 |  | 3880 |  | 10 |  | 50 |  | 3880 |  | N/A |  | N/A |  |  |
|  | 12 |  | 707.5 |  | 5 |  | 25 |  | 737.5 |  | N/A |  | N/A |  |  |
|  | 30 |  | N/A |  | 5 |  | N/A |  | 2355 |  | 21.4 |  | IMD3 |  |  |
|  | n77 |  | 3770 |  | 10 |  | 50 |  | 3770 |  | N/A |  | N/A |  |  |
| DC_12A-66A_n77ADC_12A-66A_n77(2A)DC_12A-66A-66A_n77ADC_12A-66A-66A_n77(2A) | 12 |  | N/A |  | 5 |  | N/A |  | 740 |  | 23.5 |  | IMD32 |  |  |
|  | 66 |  | 1720 |  | 5 |  | 25 |  | 2120 |  | N/A |  | N/A |  |  |
|  | n77 |  | 4180 |  | 10 |  | 50 |  | 4180 |  | N/A |  | N/A |  |  |
|  | 12 |  | 707 |  | 5 |  | 25 |  | 737 |  | N/A |  | N/A |  |  |
|  | 66 |  | N/A |  | 5 |  | N/A |  | 2126 |  | 21.4 |  | IMD3 |  |  |
|  | n77 |  | 3540 |  | 10 |  | 50 |  | 3540 |  | N/A |  | N/A |  |  |
| DC_12A-71A_n2A | 12 |  | 713.5 |  | 5 |  | 25 |  | 743.5 |  | 4.2 |  | IMD5 |  |  |
|  | 71 |  | 665.5 |  | 5 |  | 25 |  | 619.5 |  | N/A |  | N/A |  |  |
|  | n2 |  | 1907.5 |  | 5 |  | 25 |  | 1987.5 |  | N/A |  | N/A |  |  |
| DC_12A-71A_n77A | 12 |  | 702 |  | 5 |  | 25 |  | 732 |  | 4.4 |  | IMD5 |  |  |
|  | 71 |  | 667 |  | 5 |  | 25 |  | 621 |  | N/A |  | N/A |  |  |
|  | n77 |  | 3400 |  | 10 |  | 50 |  | 3400 |  | N/A |  | N/A |  |  |
|  | 12 |  | 701.5 |  | 5 |  | 25 |  | 731.5 |  | N/A |  | N/A |  |  |
|  | 71 |  | 690 |  | 5 |  | 25 |  | 644 |  | 3.9 |  | IMD5 |  |  |
|  | n77 |  | 3450 |  | 10 |  | 50 |  | 3450 |  | N/A |  | N/A |  |  |
| DC_13A_n2A-n77ADC_13A_n2A-n77C | 13 |  | 782 |  | 5 |  | 25 |  | 751 |  | N/A |  | N/A |  |  |
|  | n2 |  | N/A |  | 5 |  | N/A |  | 1960 |  | 25.0 |  | IMD3 |  |  |
|  | n77 |  | 3524 |  | 10 |  | 50 |  | 3524 |  | N/A |  | N/A |  |  |
| DC_13A_n5A-n77A2DC_13A_n5A-n77C2 | n5 |  | 840 |  | 5 |  | 25 |  | 885 |  | 19.5 |  | IMD5 |  |  |
|  | 13 |  | 782 |  | 5 |  | 20 |  | 751 |  | N/A |  | N/A |  |  |
|  | n77 |  | 4013 |  | 10 |  | 50 |  | 4013 |  | N/A |  | N/A |  |  |
| DC_13A-66A_n77ADC_13A-66A-66A_n77ADC_13A-66A_n77CDC_13A-66A-66A_n77C | 13 |  | 782 |  | 5 |  | 25 |  | 751 |  | N/A |  | N/A |  |  |
|  | 66 |  | N/A |  | 5 |  | N/A |  | 2156 |  | 25.3 |  | IMD3 |  |  |
|  | n77 |  | 3720 |  | 10 |  | 50 |  | 3720 |  | N/A |  | N/A |  |  |
|  | 13 |  | N/A |  | 5 |  | N/A |  | 750 |  | 23.4 |  | IMD32 |  |  |
|  | 66 |  | 1720 |  | 5 |  | 25 |  | 2120 |  | N/A |  | N/A |  |  |
|  | n77 |  | 4190 |  | 10 |  | 50 |  | 4190 |  | N/A |  | N/A |  |  |
| DC_13A_n66A-n77ADC_13A_n66A-n77C | 13 |  | 782 |  | 5 |  | 25 |  | 751 |  | N/A |  | N/A |  |  |
|  | n66 |  | N/A |  | 5 |  | N/A |  | 2156 |  | 26.1 |  | IMD3 |  |  |
|  | n77 |  | 3720 |  | 10 |  | 50 |  | 3720 |  | N/A |  | N/A |  |  |
| DC_14A-30A_n77ADC_14A-30A_n77(2A) | 14 |  | N/A |  | 5 |  | N/A |  | 763 |  | 23.5 |  | IMD31 |  |  |
|  | 30 |  | 2310 |  | 5 |  | 25 |  | 2355 |  | N/A |  | N/A |  |  |
|  | n77 |  | 3857 |  | 10 |  | 50 |  | 3857 |  | N/A |  | N/A |  |  |
|  | 14 |  | 793 |  | 5 |  | 25 |  | 763 |  | N/A |  | N/A |  |  |
|  | 30 |  | N/A |  | 5 |  | N/A |  | 2355 |  | 21.4 |  | IMD3 |  |  |
|  | n77 |  | 3941 |  | 10 |  | 50 |  | 3941 |  | N/A |  | N/A |  |  |
| DC_14A-66A_n77ADC_14A-66A_n77(2A)DC_14A-66A-66A_n77ADC_14A-66A-66A_n77(2A) | 14 |  | N/A |  | 5 |  | N/A |  | 763 |  | 23.5 |  | IMD32 |  |  |
|  | 66 |  | 1712.5 |  | 5 |  | 25 |  | 2112.5 |  | N/A |  | N/A |  |  |
|  | n77 |  | 4188 |  | 10 |  | 50 |  | 4188 |  | N/A |  | N/A |  |  |
|  | 14 |  | 793 |  | 5 |  | 25 |  | 763 |  | N/A |  | N/A |  |  |
|  | 66 |  | N/A |  | 5 |  | N/A |  | 2155 |  | 21.4 |  | IMD3 |  |  |
|  | n77 |  | 3741 |  | 10 |  | 50 |  | 3741 |  | N/A |  | N/A |  |  |
| DC_18A_n28A-n77A | 18 |  | 820 |  | 5 |  | 25 |  | 865 |  | N/A |  | N/A |  |  |
|  | n28 |  | 723 |  | 5 |  | 25 |  | 778 |  | 17.5 |  | IMD5 |  |  |
|  | n77 |  | 4058 |  | 10 |  | 50 |  | 4058 |  | N/A |  | N/A |  |  |
| DC_19A-21A_n77ADC_19A-21A_n77(2A) | 19 |  | N/A |  | 5 |  | N/A |  | 882.5 |  | 27.7 |  | IMD3 |  |  |
|  | 21 |  | 1450.4 |  | 5 |  | 25 |  | 1498.4 |  | N/A |  | N/A |  |  |
|  | n77 |  | 3783.3 |  | 10 |  | 50 |  | 3783.3 |  | N/A |  | N/A |  |  |
|  | 19 |  | N/A |  | 5 |  | N/A |  | 882.5 |  | 25.2 |  | IMD4 |  |  |
|  | 21 |  | 1450.4 |  | 5 |  | 25 |  | 1498.4 |  | N/A |  | N/A |  |  |
|  | n77 |  | 3468.7 |  | 10 |  | 50 |  | 3468.7 |  | N/A |  | N/A |  |  |
|  | 19 |  | 837.5 |  | 5 |  | 25 |  | 882.5 |  | N/A |  | N/A |  |  |
|  | 21 |  | N/A |  | 5 |  | N/A |  | 1502.5 |  | 21.0 |  | IMD4 |  |  |
|  | n77 |  | 4015 |  | 10 |  | 50 |  | 4015 |  | N/A |  | N/A |  |  |
| DC_19A-21A_n78ADC_19A-21A_n78(2A) | 19 |  | N/A |  | 5 |  | N/A |  | 882.5 |  | 27.7 |  | IMD3 |  |  |
|  | 21 |  | 1450.4 |  | 5 |  | 25 |  | 1498.4 |  | N/A |  | N/A |  |  |
|  | n78 |  | 3783.3 |  | 10 |  | 50 |  | 3783.3 |  | N/A |  | N/A |  |  |
|  | 19 |  | N/A |  | 5 |  | N/A |  | 882.5 |  | 25.2 |  | IMD4 |  |  |
|  | 21 |  | 1450.4 |  | 5 |  | 25 |  | 1498.4 |  | N/A |  | N/A |  |  |
|  | n78 |  | 3468.7 |  | 10 |  | 50 |  | 3468.7 |  | N/A |  | N/A |  |  |
| DC_19A-21A_n79A7 | 19 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | IMD5 |  |  |
|  | 21 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |  |
|  | n79 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |  |
|  | 19 |  | 837.5 |  | 5 |  | 25 |  | 882.5 |  | N/A |  | N/A |  |  |
|  | 21 |  | N/A |  | 5 |  | N/A |  | 1500 |  | 24.8 |  | IMD5 |  |  |
|  | n79 |  | 4850 |  | 10 |  | 50 |  | 4850 |  | N/A |  | N/A |  |  |
| DC_19A-42A_n79A10DC_19A-42C_n79A10 | 19 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |  |
|  | 42 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | IMD2 |  |  |
|  | n79 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |  |
| DC_19A_n78A-n79A | 19 |  | 835 |  | 5 |  | 25 |  | 880 |  | N/A |  | N/A |  |  |
|  | n78 |  | 3680 |  | 10 |  | 50 |  | 3680 |  | N/A |  | N/A |  |  |
|  | n79 |  | N/A |  | 40 |  | N/A |  | 4515 |  | 35.3 |  | IMD2 |  |  |
|  | 19 |  | 835 |  | 5 |  | 25 |  | 880 |  | N/A |  | N/A |  |  |
|  | n78 |  | N/A |  | 10 |  | N/A |  | 3715 |  | 34.8 |  | IMD2 |  |  |
|  | n79 |  | 4550 |  | 40 |  | 216 |  | 4550 |  | N/A |  | N/A |  |  |
| DC_21A-42A_n79A10DC_21A-42C_n79A10 | 21 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |  |
|  | 42 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | IMD2 |  |  |
|  | n79 |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  | N/A |  |  |
| DC_21A_n78A-n79A | 21 |  | 1453 |  | 5 |  | 25 |  | 1501 |  | N/A |  | N/A |  |  |
|  | n78 |  | 3420 |  | 10 |  | 50 |  | 3420 |  | N/A |  | N/A |  |  |
|  | n79 |  | N/A |  | 10 |  | N/A |  | 4873 |  | 36.1 |  | IMD25 |  |  |
|  | 21 |  | 1453 |  | 5 |  | 25 |  | 1501 |  | N/A |  | N/A |  |  |
|  | n78 |  | N/A |  | 10 |  | N/A |  | 3487 |  | 38.8 |  | IMD2 |  |  |
|  | n79 |  | 4940 |  | 10 |  | 50 |  | 4940 |  | N/A |  | N/A |  |  |
| DC_29A-30A_n77A | 29 |  | N/A |  | 5 |  | N/A |  | 722 |  | 23.5 |  | IMD31 |  |  |
|  | 30 |  | 2310 |  | 5 |  | 25 |  | 2355 |  | N/A |  | N/A |  |  |
|  | n77 |  | 3898 |  | 10 |  | 50 |  | 3898 |  | N/A |  | N/A |  |  |
| DC_29A-66A_n77ADC_29A-66A-66A_n77A | 29 |  | N/A |  | 5 |  | N/A |  | 722 |  | 23.5 |  | IMD32 |  |  |
|  | 66 |  | 1734 |  | 5 |  | 25 |  | 2134 |  | N/A |  | N/A |  |  |
|  | n77 |  | 4190 |  | 10 |  | 50 |  | 4190 |  | N/A |  | N/A |  |  |
| DC_30A-66A_n77ADC_30A-66A_n77(2A)DC_30A-66A-66A_n77ADC_30A-66A-66A_n77(2A) | 30 |  | N/A |  | 5 |  | N/A |  | 2355 |  | 34.2 |  | IMD22 |  |  |
|  | 66 |  | 1745 |  | 5 |  | 25 |  | 2145 |  | N/A |  | N/A |  |  |
|  | n77 |  | 4100 |  | 10 |  | 50 |  | 4100 |  | N/A |  | N/A |  |  |
|  | 30 |  | N/A |  | 5 |  | N/A |  | 2355 |  | 12.9 |  | IMD5 |  |  |
|  | 66 |  | 1735 |  | 5 |  | 25 |  | 2135 |  | N/A |  | N/A |  |  |
|  | n77 |  | 3780 |  | 10 |  | 50 |  | 3780 |  | N/A |  | N/A |  |  |
|  | 30 |  | 2310 |  | 5 |  | 25 |  | 2355 |  | N/A |  | N/A |  |  |
|  | 66 |  | N/A |  | 5 |  | N/A |  | 2160 |  | 19.2 |  | IMD42 |  |  |
|  | n77 |  | 3390 |  | 10 |  | 50 |  | 3390 |  | N/A |  | N/A |  |  |
| DC_41A_n28A-n77A | n28 |  | 743 |  | 5 |  | 25 |  | 798 |  | 36.8 |  | IMD21,11 |  |  |
|  | 41 |  | 2642 |  | 5 |  | 25 |  | 2642 |  | N/A |  | N/A |  |  |
|  | n77 |  | 3440 |  | 10 |  | 50 |  | 3440 |  | N/A |  | N/A |  |  |
| DC_66A_n2A-n77ADC_66A-66A_n2A-n77ADC_66A_n2A-n77C | n2 |  | N/A |  | 5 |  | N/A |  | 1960 |  | 37.6 |  | IMD25 |  |  |
|  | 66 |  | 1760 |  | 5 |  | 25 |  | 2160 |  | N/A |  | N/A |  |  |
|  | n77 |  | 3720 |  | 10 |  | 50 |  | 3720 |  | N/A |  | N/A |  |  |
| DC_66A_n66A-n77A | 66 |  | 1750 |  | 5 |  | 25 |  | 2150 |  | N/A |  | N/A |  |  |
|  | n66 |  | N/A |  | 5 |  | N/A |  | 2150 |  | 37 |  | IMD2 |  |  |
|  | n77 |  | 3900 |  | 10 |  | 50 |  | 3900 |  | N/A |  | N/A |  |  |
|  | 66 |  | 1750 |  | 5 |  | 25 |  | 2150 |  | N/A |  | N/A |  |  |
|  | n66 |  | N/A |  | 5 |  | N/A |  | 2170 |  | 20 |  | IMD5 |  |  |
|  | n77 |  | 3710 |  | 10 |  | 50 |  | 3710 |  | N/A |  | N/A |  |  |
| NOTE 1: This band is subject to IMD5 also which MSD is not specified.NOTE 2:  For a UE which supports this band combination only when the Band n77 frequency range restriction defined in NOTE 12 of Table 5.2-1 from TS 38.101-1 applies, the MSD test point(s) cannot be verified for the band combination and the test point(s) can be skipped.NOTE 3: This UE channel bandwidth is optional in this release of the specificationNOTE 4: VoidNOTE 5: This band is subject to IMD4 also which MSD is not specified.NOTE 6: E-UTRA carrier shall be set to min(+23 dBm, PCMAX_L_E-UTRA,c) and NR carrier shall be set to min(+23 dBm, PCMAX_L,f,c,NR) as defined in clause 6.2B.4.1.3.NOTE 7: The frequency range in band n79 is restricted for this band combination to 4400 - 4900 MHz for both the UL and the DL.NOTE 8: The frequency range in band 1 is restricted for this band combination to 1940 - 1960 MHz for the UL and 2130 - 2150 MHz for the DL.NOTE 9: The frequency range in band n79 is restricted for this band combination to 4500 - 5000 MHz for both the UL and the DLNOTE 10: The frequency range in band n79 is restricted for this band combination to 4500 - 4600 MHz for both the UL and the DLNOTE 11: This band is subject to IMD3 also which MSD is not specified |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

###### 7.3B.2.3.5.3 Void

###### 7.3B.2.3.5.4 MSD test points for intermodulation interference due to dual uplink operation for EN-DC in NR FR1 involving four bands

Table 7.3B.2.3.5.4-1: MSD test points for Scell due to dual uplink operation for EN-DC in NR FR1 (four bands)

| NR or E-UTRA Band / Channel bandwidth / NRB / MSD |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EN-DC Configuration | EUTRA / NR band | UL Fc  (MHz) | UL/DL BW  (MHz) | ULLCRB | DL Fc (MHz) | MSD  (dB) | IMD order |
| DC_1A-7A_n7A-n78A | 1 | N/A | 5 | N/A | 2140 | 8.7 | IMD4 |
|  | 7, n7 | 2510 | 10 | 50 | 2630 | N/A | N/A |
|  | n78 | 3580 | 10 | 50 | 3580 | N/A | N/A |
|  | 1 | 1977.5 | 5 | 25 | 2167.5 | N/A | N/A |
|  | 7, n7 | N/A | 5 | N/A | 2627.5 | 9.1 | IMD4 |
|  | n78 | 3305 | 10 | 50 | 3305 | N/A | N/A |
|  | 1 | 1970 | 5 | 25 | 2160 | N/A | N/A |
|  | 7, n7 | 2520 | 5 | 25 | 2640 | N/A | N/A |
|  | n78 | N/A | 10 | N/A | 3390 | 10.1 | IMD4 |
| DC_3A-7A_n7A-n78ADC_3A-3A-7A_n7A-n78ADC_3C-7A_n7A-n78A | 3 | N/A | 5 | N/A | 1820 | 17.6 | IMD3 |
|  | 7, n7 | 2565 | 5 | 25 | 2685 | N/A | N/A |
|  | n78 | 3310 | 10 | 50 | 3310 | N/A | N/A |
|  | 3 | N/A | 5 | N/A | 1820 | 8.6 | IMD4 |
|  | 7, n7 | 2565 | 5 | 25 | 2685 | N/A | N/A |
|  | n78 | 3475 | 10 | 50 | 3475 | N/A | N/A |
|  | 3 | 1730 | 5 | 25 | 1825 | N/A | N/A |
|  | n7, n7 | 2560 | 5 | 25 | 2680 | N/A | N/A |
|  | n78 | N/A | 10 | N/A | 3390 | 16.1 | IMD3 |
| DC_7A-28A_n7A-n78A | 7, n7 | 2565 | 5 | 25 | 2685 | N/A | N/A |
|  | 28 | N/A | 5 | N/A | 800 | 28.8 | IMD2 |
|  | n78 | 3365 | 10 | 50 | 3365 | N/A | N/A |
|  | 7, n7 | 2570 | 5 | 25 | 2670 | N/A | N/A |
|  | 28 | N/A | 5 | N/A | 790 | 3.0 | IMD5 |
|  | n78 | 3460 | 10 | 50 | 3421 | N/A | N/A |
|  | 7, n7 | N/A | 5 | N/A | 2650 | 30.5 | IMD2 |
|  | 28 | 740 | 5 | 25 | 768 | N/A | N/A |
|  | n78 | 3390 | 10 | 50 | 3421 | N/A | N/A |
|  | 7, n7 | 2565 | 5 | 25 | 2685 | N/A | N/A |
|  | 28 | 745 | 5 | 25 | 800 | N/A | N/A |
|  | n78 | N/A | 10 | N/A | 3310 | 29.7 | IMD2 |
| NOTE 1:  VoidNOTE 2: E-UTRA carrier shall be set to min(+20 dBm, PCMAX_L_E-UTRA,c) and NR carrier shall be set to min(+20 dBm, PCMAX_L,f,c,NR) as defined in clause 6.2B.4.1.3. |  |  |  |  |  |  |  |

#### 7.3B.2.3a Inter-band NE-DC within FR1

##### 7.3B.2.3a.0 General

Reference sensitivity exceptions are specified for the condition when there is uplink transmission only in the aggressor band. This clause addresses directly only NE-DC configurations that don't have a corresponding specified EN-DC configuration or specific NE-DC exceptions.

##### 7.3B.2.3a.1 Reference sensitivity exceptions due to UL harmonic interference for NE-DC in NR FR1

Sensitivity degradation is allowed for a band if it is impacted by UL harmonic interference from another band part of the same NE-DC configuration. For the NE-DC cconfigurations that have an EN-DC defined configuration, the reference sensitivity exceptions for the victim band (high) are specified in Table 7.3B.2.3.1-1 with uplink configuration of the aggressor band (low) are applicable.

##### 7.3B.2.3a.2 Reference sensitivity exceptions due to receiver harmonic mixing for NE-DC in NR FR1

Sensitivity degradation is allowed for a band if it is impacted by receiver harmonic mixing due to another band part of the same NE-DC configuration. For the NE-DC cconfigurations that have an EN-DC defined configuration, the reference sensitivity exceptions for the victim band (low) are specified in Table 7.3B.2.3.2-1 with uplink configuration of the agressor band (high).

Table 7.3B.2.3a.2-1: Reference sensitivity exceptions (MSD) due to receiver harmonic mixing for NE-DC in NR FR1

| UL band | DL band | UL BW | SCS of UL band | UL RB Allocation | DL BW | MSD | UL/DL fc condition | UL/DL harmonic order |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | (MHz) | (kHz) | LCRB | (MHz) | (dB) |  |  |
| 42 | n40 | 5 | 15 | 12 (RBstart=0) | 5 | 14.7 | NOTE 1 | UL2/DL3 |
| 42 | n40 | 5 | 15 | 12 (RBstart=0) | 20 | 9.1 | NOTE 1 | UL2/DL3 |
| NOTE 1: The requirements should be verified for DL EARFCN of the  victim (lower) band (superscript LB) such that $ f_{DL}^{LB}=\lfloor  f_{UL}^{HB}/0.15\rfloor  0.1 $  with![](media_svg/image21.svg) [公式≈: _{f}_{DL}LB] the DL carrier frequency in the lower band and $ f_{UL}^{HB}$ the UL carrier frequency in the higher band, both in MHz. |  |  |  |  |  |  |  |  |

##### 7.3B.2.3a.3 Reference sensitivity exceptions due to cross band isolation for NE-DC in NR FR1

Sensitivity degradation is allowed for a band if it is impacted by UL of another band part of the same NE-DC configuration due to cross band isolation issues. Reference sensitivity exceptions for the victim band are specified in Table 7.3B.2.3a.3-1.

For the NE-DC configurations that have an EN-DC defined configuration, the reference sensitivity exceptions for the victim band are specified in Table 7.3B.2.3.4-1 and Table 7.3B.2.3.4-1a.

Table 7.3B.2.3a.3-1: Reference sensitivity exceptions (MSD) due to cross band isolation and uplink/downlink configurations for PC3 NE-DC in NR FR1

| UL band | DL band | UL Fc | UL BW | SCS of UL band | UL RB Allocation | DL Fc | DL BW | MSD | Cross-bandInterferencesource |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | (MHz) | (MHz) | (kHz) | LCRB | (MHz) | (MHz) | (dB) |  |
| 34 | n28 | 2017.5 | 15 | 15 | 75 (RBSTART=0) | 785.5 | 5 | 3.4 | >ACLR2 |
| 39 | n28 | 1890 | 20 | 15 | 100 (RBSTART=0) | 785.5 | 5 | 3.4 | >ACLR2 |
| NOTE 1: Void.NOTE 2: Void. |  |  |  |  |  |  |  |  |  |

Table 7.3B.2.3a.3-2: Void

##### 7.3B.2.3a.4 MSD for intermodulation interference due to dual uplink operation for NE-DC in NR FR1

###### 7.3B.2.3a.4.1 (Reserved)

###### 7.3B.2.3a.4.2 MSD test points for intermodulation interference due to dual uplink operation for NE-DC in NR FR1 involving three bands

Table 7.3B.2.3a.4.2-1

| NR or E-UTRA Band / Channel bandwidth / NRB / MSD |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EN-DC Configuration | EUTRA / NR band | UL Fc  (MHz) | UL/DL BW  (MHz) | ULLCRB | DL Fc (MHz) | MSD  (dB) | IMD order |
| DC_3(n)AA_n77A | 3 | 1740 | 5 | 25 | 1835 | 31.9 | IMD21 |
|  | n3 | N/A | 5 | N/A | 1840 | [28.9] | IMD21 |
|  | n77 | 3575 | 10 | 50 | 3575 | N/A | N/A |
| NOTE 1: This band is subject to IMD5 also which MSD is not specified. |  |  |  |  |  |  |  |

#### 7.3B.2.4 Inter-band EN-DC including FR2

##### 7.3B.2.4.1 Void

#### 7.3B.2.5 Inter-band EN-DC including both FR1 and FR2

##### 7.3B.2.5.1 Reference sensitivity exceptions due to UL harmonic interference for EN-DC including both FR1 and FR2

For inter-band EN-DC of E-UTRA and NR in both FR1 and FR2, the UE is allowed to apply each sensitivity degradation for EN-DC in FR1 specified in clause 7.3B.2.3 TS 38.101-3 and for EN-DC including FR2 specified in clause 7.3B.2.3 of TS 38.101-3 independently.

#### 7.3B.2.3.6 Void

#### 7.3B.2.3.7 Lower-MSD requirements for inter-band EN-DC within FR1

A UE can report better MSD performance than the minimum requirements as specified in clause 7.3B.2.3.1, 7.3B.2.3.2, 7.3B.2.3.4, 7.3B.2.3.5, 7B.2.3.2.0.1, and 7B.2.3.2.0.2 by lowerMSD-r18 capability, except that the reporting for MSD caused by IMD with order higher than 5, IMD of UL intra-band CA or triple-beat is not supported in this release of the specification. The MSD performance after improvement is categorized into different lower-MSD capability classes, which are defined in Table 7.3A.7-1 of TS 38.101-1 [2].

The reported lower-MSD capability classes are subject to the same uplink/downlink configurations as defined for the minimum MSD requirements in clause 7.3B.2.3, 7B.2.3.2.0.1, and 7B.2.3.2.0.2. If a UE can support more than one test points for a given REFSENS exception case, the reported lower-MSD capability class is applicable for the test point having the largest specified MSD value. Otherwise, it’s only applicable for the test point which can be supported by the UE. If one or multiple power classes are requested by the network, the UE can, if supported, report lowerMSD-r18 capability for the requested power classes; otherwise, the UE shall report lowerMSD-r18 capability for the highest supported power class for the given DC configuration.

The UE shall meet one of the following conditions in order to report lowerMSD-r18 capability for a given REFSENS exception case:

If the specified minimum requirement is tightly bounded by the range of a lower-MSD capability class (i.e, Thresholdi-1 < MSD ≤ Thresholdi, where i and (i-1) are two adjacent lower-MSD capability classes), the actual MSD shall be at least one-level lower (i.e., actual MSD ≤ Thresholdi-1); or

If the specified minimum requirement is larger than the maximum threshold (corresponding to lower-MSD capability class VIII), the actual MSD shall be no more than the maximum threshold.

Otherwise, the UE shall not report lowerMSD-r18 capability for this REFSENS exception case.

If the special MSD type “ALL” is indicated in the lowerMSD-r18 capability, the reporting conditions as specified above shall be met for each MSD type that has been specified in this release for the given DC configuration.

NOTE 1:  The lowerMSD-r18 capability is verified by reusing the MSD test point parameters and only replacing the minimum MSD requirement value by the threshold of the reported lower-MSD capability class. UE supporting lower MSD shall indicate the lower MSD capability for the requested power class if supported. If no power class is explicitly requested, the UE supporting lower MSD shall indicate the lower MSD capability for the highest supported power class of the band combination including victim band and aggressor band(s).. And, similar to the specified MSD minimum requirements, only the highest supported power class or the power class required by the certification/regulation body per UL configuration is verified.

NOTE 2: If the UE is equipped with four or eight Rx antenna ports for the victim band of the BC, the lowerMSD-r18 capability is verified with four or eight Rx antenna ports according to clause 7.1 under the condition mentioned above, but with the increased MSD values by the absolute value of ΔRIB,4Ror ΔRIB,8Rapplied for the requirement based on the description in clause 7.3B.1.

### 7.3B.3 ΔRIB,c, ΔRIBNC for DC

#### 7.3B.3.0 General

For the UE which supports inter-band EN-DC or NE-DC configuration, the minimum requirement for reference sensitivity in Table 7.3.1-1 and Table 7.3.1-1a in TS 36.101 [4], clause 7.3.2, 7.3A.2, 7.3C.2 in TS 38.101-1 [2] and clause 7.3.2, 7.3A.2 in TS 38.101-2 [3] shall be increased by the amount given in ΔRIB,c, ΔRIBNC in Tables below where unless otherwise stated, the same ΔRIB,c, ΔRIBNC are applicable to NR band(s) part for DC configurations which have the same NR operating band combination. Unless otherwise stated, ΔRIB,c or ΔRIBNC is set to zero.

In case the UE supports more than one of band combinations for CA, SUL or DC, and an operating band belongs to more than one band combinations then

- When the operating band frequency range is ≤ 1 GHz, the applicable additional ΔRIB,c shall be the average value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in TS 38.101-1 [2] and 7.3A, 7.3B in this specification, truncated to one decimal place that apply for that operating band among the supported band combinations. In case there is a harmonic relation between low band UL and high band DL, then the maximum ΔRIB,c among the different supported band combinations involving such band shall be applied

- When the operating band frequency range is > 1 GHz, the applicable additional ΔRIB,c shall be the maximum value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in TS 38.101-1 [2] and 7.3A, 7.3B in this specification for the applicable operating bands.

Unless ΔRIB,c is specified for the NE-DC configuration, the specified ΔRIB,c for the EN-DC configuration including same bands as the corresponding NE-DC configuration is applicable for the NE-DC configuration.

#### 7.3B.3.1 Intra-band contiguous EN-DC

#### 7.3B.3.2 Intra-band non-contiguous EN-DC

Table 7.3B.3.2-1: Intra-band non-contiguous EN-DC with one uplink configuration on E-UTRA for reference sensitivity (E-UTRA uplink carrier is closer to the NR downlink carrier than it is to the E-UTRA downlink carrier)

| DC configuration | Aggregated channel bandwidth |  | Wgap / (MHz) | UL E-UTRA allocation(LCRB) | ΔRIBNC (dB) | Duplex mode |
| --- | --- | --- | --- | --- | --- | --- |
|  | E-UTRA | NR |  |  |  |  |
| DC_3A_n3A | 5 MHz | 5 MHz | 45.0 < Wgap ≤ 65.0 | 121 | 4.7 | FDD |
|  |  |  | 0.0 < Wgap ≤ 45.0 | 251 | 0 |  |
|  | 5 MHz | 10 MHz | 40.0 < Wgap ≤ 60.0 | 121 | 3.8 |  |
|  |  |  | 0.0 < Wgap ≤ 40.0 | 251 | 0 |  |
|  | 5 MHz | 15 MHz | 35.0 < Wgap ≤ 55.0 | 121 | 3.6 |  |
|  |  |  | 0.0 < Wgap ≤ 35.0 | 251 | 0 |  |
|  | 5 MHz | 20 MHz | 30.0 < Wgap ≤ 50.0 | 121 | 3.4 |  |
|  |  |  | 0.0 < Wgap ≤ 30.0 | 251 | 0 |  |
|  | 5 MHz | 25 MHz | 25.0 < Wgap ≤ 45.0 | 121 | 3.2 |  |
|  |  |  | 0.0 < Wgap ≤ 25.0 | 251 | 0 |  |
|  | 5 MHz | 30 MHz | 20.0 < Wgap ≤ 40.0 | 121 | 3.0 |  |
|  |  |  | 0.0 < Wgap ≤ 20.0 | 251 | 0 |  |
|  | 10 MHz | 5 MHz | 30.0 < Wgap ≤ 60.0 | 12 (RBstart = 25) | 5.1 |  |
|  |  |  | 0.0 < Wgap ≤ 30.0 | 321 | 0 |  |
|  | 10 MHz | 10MHz | 25.0 < Wgap ≤ 55.0 | 12 (RBstart = 25) | 4.3 |  |
|  |  |  | 0.0 < Wgap ≤ 25.0 | 321 | 0 |  |
|  | 10 MHz | 15 MHz | 20.0 < Wgap ≤ 50.0 | 12 (RBstart = 25) | 3.8 |  |
|  |  |  | 0.0 < Wgap ≤ 20.0 | 321 | 0 |  |
|  | 10 MHz | 20 MHz | 15.0 < Wgap ≤ 45.0 | 12 (RBstart = 25) | 3.5 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 321 | 0 |  |
|  | 10 MHz | 25 MHz | 10.0 < Wgap ≤ 40.0 | 12 (RBstart = 25) | 3.2 |  |
|  |  |  | 0.0 < Wgap ≤ 10.0 | 321 | 0 |  |
|  | 10 MHz | 30 MHz | 5.0 < Wgap ≤ 35.0 | 12 (RBstart = 25) | 2.8 |  |
|  |  |  | 0.0 < Wgap ≤ 5.0 | 321 | 0 |  |
|  | 15 MHz | 5 MHz | 25.0 < Wgap ≤ 55.0 | 12 (RBstart = 35) | 6.0 |  |
|  |  |  | 0.0 < Wgap ≤ 25.0 | 321 | 0 |  |
|  | 15 MHz | 10 MHz | 20.0 < Wgap ≤ 50.0 | 12 (RBstart = 35) | 4.7 |  |
|  |  |  | 0.0 < Wgap ≤ 20.0 | 321 | 0 |  |
|  | 15 MHz | 15 MHz | 15.0 < Wgap ≤ 45.0 | 12 (RBstart = 35) | 4.2 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 321 | 0 |  |
|  | 15 MHz | 20 MHz | 10.0 < Wgap ≤ 40.0 | 12 (RBstart = 35) | 3.8 |  |
|  |  |  | 0.0 < Wgap ≤ 10.0 | 321 | 0 |  |
|  | 15 MHz | 25 MHz | 5.0 < Wgap ≤ 35.0 | 12 (RBstart = 35) | 3.5 |  |
|  |  |  | 0.0 < Wgap ≤ 5.0 | 321 | 0 |  |
|  | 15 MHz | 30 MHz | 0.0 < Wgap ≤ 30.0 | 12 (RBstart = 35) | 3.3 |  |
|  | 20 MHz | 5 MHz | 15.0 < Wgap ≤ 50.0 | 16 (RBstart = 50) | 6.5 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 321 | 0 |  |
|  | 20 MHz | 10 MHz | 10.0 < Wgap ≤ 45.0 | 16 (RBstart = 50) | 5.1 |  |
|  |  |  | 0.0 < Wgap ≤ 10.0 | 321 | 0 |  |
|  | 20 MHz | 15 MHz | 5.0 < Wgap ≤ 40.0 | 16 (RBstart = 50) | 4.5 |  |
|  |  |  | 0.0 < Wgap ≤ 5.0 | 321 | 0 |  |
|  | 20 MHz | 20 MHz | 0.0 < Wgap ≤ 35.0 | 16 (RBstart = 50) | 4.1 |  |
|  | 20 MHz | 25 MHz | 0.0 < Wgap ≤ 30.0 | 16 (RBstart = 50) | 3.8 |  |
|  | 20 MHz | 30 MHz | 0.0 < Wgap ≤ 25.0 | 16 (RBstart = 50) | 3.6 |  |
| DC_7A_n7A | 5MHz | 5MHz | 0< Wgap ≤ 60 | 25 | 0.0 | FDD |
|  | 5MHz | 10MHz | 0 < Wgap ≤ 55 | 25 | 0.0 |  |
|  | 5MHz | 15MHz | 0 < Wgap ≤ 50 | 25 | 0.0 |  |
|  | 5MHz | 20MHz | 0 < Wgap ≤ 45 | 25 | 0.0 |  |
|  | 10MHz | 5MHz | 30 < Wgap ≤ 55 | 321 | 0.0 |  |
|  |  |  | 0 < Wgap ≤ 30 | 50 | 0.0 |  |
|  | 10MHz | 10MHz | 25.0 < Wgap ≤ 50.0 | 321 | 0.0 |  |
|  |  |  | 0.0 < Wgap ≤ 25.0 | 50 | 0.0 |  |
|  | 10MHz | 15MHz | 20 < Wgap ≤ 45 | 321 | 0.0 |  |
|  |  |  | 0 < Wgap ≤ 20 | 50 | 0.0 |  |
|  | 10MHz | 20MHz | 15 < Wgap ≤ 40 | 321 | 0.0 |  |
|  |  |  | 0 < Wgap ≤ 15 | 50 | 0.0 |  |
|  | 15MHz | 5MHz | 20.0 < Wgap ≤ 50.0 | 321 | 0.0 |  |
|  |  |  | 0.0 < Wgap ≤ 20.0 | 501 | 0.0 |  |
|  | 15MHz | 10MHz | 20.0 < Wgap ≤ 45.0 | 321 | 0.0 |  |
|  |  |  | 0.0 < Wgap ≤ 20.0 | 501 | 0.0 |  |
|  | 15MHz | 15MHz | 15.0 < Wgap ≤ 40.0 | 321 | 0.0 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 501 | 0.0 |  |
|  | 15MHz | 20MHz | 10 < Wgap ≤ 35 | 321 | 0.0 |  |
|  |  |  | 0 < Wgap ≤ 10 | 501 | 0.0 |  |
|  | 20MHz | 5MHz | 25 < Wgap ≤ 45 | 321 | 0.0 |  |
|  |  |  | 0 < Wgap ≤ 25 | 451 | 0.0 |  |
|  | 20MHz | 10MHz | 20 < Wgap ≤ 40 | 321 | 0.0 |  |
|  |  |  | 0 < Wgap  ≤ 20 | 451 | 0.0 |  |
|  | 20MHz | 15MHz | 15.0 < Wgap ≤ 35.0 | 361 | 0.0 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 501 | 0.0 |  |
|  | 20MHz | 20MHz | 15.0 < Wgap ≤ 30.0 | 321 | 0.0 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 451 | 0.0 |  |
| DC_66A_n66A | NOTE 4 |  | NOTE 8 | NOTE 9 | 0 | FDD |
| NOTE 1: UL resource blocks shall be located as close as possible to the downlink operating band but confined within the transmission.NOTE 2: Wgap is the sub-block gap between the two sub-blocks.NOTE 3: The E-UTRA uplink carrier is the aggressor and the ΔRIBNC applies to the NR DL carrier only. The E-UTRA uplink carrier shall be located as close as possible to the NR downlink carrier centre frequency.NOTE 4: All combinations of channel bandwidths defined in Table 5.3B.1.3-1.NOTE 5: Void.NOTE 6: Void.NOTE 7: Void.NOTE 8: All applicable sub-block gap sizes.NOTE 9: The UL LTE allocation is same as Transmission bandwidth configuration NRB as defined in Table 5.6-1 in TS 36.101 [4]. |  |  |  |  |  |  |

Table 7.3B.3.2-2: Intra-band non-contiguous EN-DC with one uplink configuration on NR for reference sensitivity (NR uplink carrier is closer to the E-UTRA downlink carrier than it is to the NR downlink carrier)

| DC configuration | Aggregated bandwidth |  | Wgap / (MHz) | UL NR allocation(LCRB) | ΔRIBNC (dB) | Duplex mode |
| --- | --- | --- | --- | --- | --- | --- |
|  | NR | E-UTRA |  |  |  |  |
| DC_1A_n1A | 5 MHz | 5 MHz | 0.0 < Wgap ≤ 50.0 | 25 | 0.5 | FDD |
| DC_2A_n2A | 5MHz | 5MHz | 30.0 < Wgap ≤ 50.0 | 121 | 5.3 | FDD |
|  |  |  | 0.0 < Wgap ≤ 30.0 | 251 | 0 |  |
|  | 5MHz | 10MHz | 25.0 < Wgap ≤ 45.0 | 121 | 4.4 |  |
|  |  |  | 0.0 < Wgap ≤ 25.0 | 251 | 0 |  |
|  | 5MHz | 15MHz | 20.0 < Wgap ≤ 40.0 | 121 | 4.2 |  |
|  |  |  | 0.0 < Wgap ≤ 20.0 | 251 | 0 |  |
|  | 5MHz | 20MHz | 15.0 < Wgap ≤ 35.0 | 121 | 3.8 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 251 | 0 |  |
|  | 10MHz | 5MHz | 15.0 < Wgap ≤ 45.0 | 121 | 5.9 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 321 | 0 |  |
|  | 10MHz | 10MHz | 10.0 < Wgap ≤ 40.0 | 121 | 4.6 |  |
|  |  |  | 0.0 < Wgap ≤ 10.0 | 321 | 0 |  |
|  | 10MHz | 15MHz | 5.0 < Wgap ≤ 35.0 | 121 | 4.1 |  |
|  |  |  | 0.0 < Wgap ≤ 5.0 | 321 | 0 |  |
|  | 10MHz | 20MHz | 0.0 < Wgap ≤ 30.0 | 121 | 4.0 |  |
|  | 15MHz | 5MHz | 10.0 < Wgap ≤ 40.0 | 12 (RBstart = 39) | 6.7 |  |
|  |  |  | 0.0 < Wgap ≤ 10.0 | 361 | 0 |  |
|  | 15MHz | 10MHz | 5.0 < Wgap ≤ 35.0 | 12 (RBstart = 39) | 5.4 |  |
|  |  |  | 0.0 < Wgap ≤ 5.0 | 361 | 0 |  |
|  | 15MHz | 15MHz | 0.0 < Wgap  ≤ 30.0 | 12 (RBstart = 39) | 4.6 |  |
|  | 15MHz | 20MHz | 0.0 < Wgap ≤ 25.0 | 12 (RBstart = 39) | 4.2 |  |
|  | 20MHz | 5MHz | 0.0 < Wgap ≤ 35.0 | 16 (RBstart = 57) | 7.2 |  |
|  | 20MHz | 10MHz | 0.0 < Wgap ≤ 30.0 | 16 (RBstart = 57) | 5.8 |  |
|  | 20MHz | 15MHz | 0.0 < Wgap ≤ 25.0 | 16 (RBstart = 57) | 5.0 |  |
|  | 20MHz | 20MHz | 0.0 < Wgap ≤ 20.0 | 16 (RBstart = 57) | 4.6 |  |
| DC_3A_n3A | 5MHz | 5MHz | 45.0 < Wgap ≤ 65.0 | 121 | 4.7 | FDD |
|  |  |  | 0.0 < Wgap ≤ 45.0 | 251 | 0 |  |
|  | 5MHz | 10MHz | 40.0 < Wgap ≤ 60.0 | 121 | 3.8 |  |
|  |  |  | 0.0 < Wgap ≤ 40.0 | 251 | 0 |  |
|  | 5MHz | 15MHz | 35.0 < Wgap ≤ 55.0 | 121 | 3.6 |  |
|  |  |  | 0.0 < Wgap ≤ 35.0 | 251 | 0 |  |
|  | 5MHz | 20MHz | 30.0 < Wgap ≤ 50.0 | 121 | 3.4 |  |
|  |  |  | 0.0 < Wgap ≤ 30.0 | 251 | 0 |  |
|  | 10MHz | 5MHz | 30.0 < Wgap ≤ 60.0 | 12 (RBstart = 25) | 5.1 |  |
|  |  |  | 0.0 < Wgap ≤ 30.0 | 321 | 0 |  |
|  | 10MHz | 10MHz | 25.0 < Wgap ≤ 55.0 | 12 (RBstart = 25) | 4.3 |  |
|  |  |  | 0.0 < Wgap ≤ 25.0 | 321 | 0 |  |
|  | 10MHz | 15MHz | 20.0 < Wgap ≤ 50.0 | 12 (RBstart = 25) | 3.8 |  |
|  |  |  | 0.0 < Wgap ≤ 20.0 | 321 | 0 |  |
|  | 10MHz | 20MHz | 15.0 < Wgap ≤ 45.0 | 12 (RBstart = 25) | 3.5 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 321 | 0 |  |
|  | 15MHz | 5MHz | 25.0 < Wgap ≤ 55.0 | 12 (RBstart = 35) | 6.0 |  |
|  |  |  | 0.0 < Wgap ≤ 25.0 | 321 | 0 |  |
|  | 15MHz | 10MHz | 20.0 < Wgap ≤ 50.0 | 12 (RBstart = 35) | 4.7 |  |
|  |  |  | 0.0 < Wgap ≤ 20.0 | 321 | 0 |  |
|  | 15MHz | 15MHz | 15.0 < Wgap  ≤ 45.0 | 12 (RBstart = 35) | 4.2 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 321 | 0 |  |
|  | 15MHz | 20MHz | 10.0 < Wgap ≤ 40.0 | 12 (RBstart = 35) | 3.8 |  |
|  |  |  | 0.0 < Wgap ≤ 10.0 | 321 | 0 |  |
|  | 20MHz | 5MHz | 15.0 < Wgap ≤ 50.0 | 16 (RBstart = 50) | 6.5 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 321 | 0 |  |
|  | 20MHz | 10MHz | 10.0 < Wgap ≤ 45.0 | 16 (RBstart = 50) | 5.1 |  |
|  |  |  | 0.0 < Wgap  ≤ 10.0 | 321 | 0 |  |
|  | 20MHz | 15MHz | 5.0 < Wgap ≤ 40.0 | 16 (RBstart = 50) | 4.5 |  |
|  |  |  | 0.0 < Wgap  ≤ 5.0 | 321 | 0 |  |
|  | 20MHz | 20MHz | 0.0 < Wgap ≤ 35.0 | 16 (RBstart = 50) | 4.1 |  |
|  | 25MHz | 5MHz | 10.0 < Wgap ≤ 45.0 | 16 (RBstart = 60) | 7.4 |  |
|  |  |  | 0.0 < Wgap ≤ 10.0 | 321 | 0 |  |
|  | 25MHz | 10MHz | 5.0 < Wgap ≤ 40.0 | 16 (RBstart = 60) | 5.5 |  |
|  |  |  | 0.0 < Wgap ≤ 5.0 | 321 | 0 |  |
|  | 25MHz | 15MHz | 0.0 < Wgap ≤ 35.0 | 16 (RBstart = 60) | 4.9 |  |
|  | 25MHz | 20MHz | 0.0 < Wgap ≤ 30.0 | 16 (RBstart = 60) | 4.6 |  |
|  | 30MHz | 5MHz | 5.0 < Wgap ≤ 40.0 | 16 (RBstart = 75) | 8.3 |  |
|  |  |  | 0.0 < Wgap ≤ 5.0 | 321 | 0 |  |
|  | 30MHz | 10MHz | 0.0 < Wgap ≤ 35.0 | 16 (RBstart = 75) | 5.9 |  |
|  | 30MHz | 15MHz | 0.0 < Wgap ≤ 30.0 | 16 (RBstart = 75) | 5.5 |  |
|  | 30MHz | 20MHz | 0.0 < Wgap ≤ 25.0 | 16 (RBstart = 75) | 4.9 |  |
| DC_5A_n5A | 5 MHz | 5 MHz | NOTE 10 | 121 | 5.3 | FDD |
|  | 10 MHz | 5 MHz |  |  | 4.4 |  |
|  | 15 MHz | 5 MHz |  |  | 6.1 |  |
|  | 5 MHz | 10 MHz |  |  | 5.9 |  |
|  | 10 MHz | 10 MHz |  |  | 4.6 |  |
| DC_7A_n7A | 5MHz | 5MHz | 0< Wgap ≤ 60 | 25 | 0.0 | FDD |
|  | 5MHz | 10MHz | 0 < Wgap ≤ 55 | 25 | 0.0 |  |
|  | 5MHz | 15MHz | 0 < Wgap ≤ 50 | 25 | 0.0 |  |
|  | 5MHz | 20MHz | 0 < Wgap ≤ 45 | 25 | 0.0 |  |
|  | 10MHz | 5MHz | 30 < Wgap ≤ 55 | 321 | 0.0 |  |
|  |  |  | 0 < Wgap ≤ 30 | 50 | 0.0 |  |
|  | 10MHz | 10MHz | 25.0 < Wgap ≤ 50.0 | 321 | 0.0 |  |
|  |  |  | 0.0 < Wgap ≤ 25.0 | 50 | 0.0 |  |
|  | 10MHz | 15MHz | 20 < Wgap ≤ 45 | 321 | 0.0 |  |
|  |  |  | 0 < Wgap ≤ 20 | 50 | 0.0 |  |
|  | 10MHz | 20MHz | 15 < Wgap ≤ 40 | 321 | 0.0 |  |
|  |  |  | 0 < Wgap ≤ 15 | 50 | 0.0 |  |
|  | 15MHz | 5MHz | 20.0 < Wgap ≤ 50.0 | 321 | 0.0 |  |
|  |  |  | 0.0 < Wgap ≤ 20.0 | 501 | 0.0 |  |
|  | 15MHz | 10MHz | 20.0 < Wgap ≤ 45.0 | 321 | 0.0 |  |
|  |  |  | 0.0 < Wgap ≤ 20.0 | 501 | 0.0 |  |
|  | 15MHz | 15MHz | 15.0 < Wgap ≤ 40.0 | 321 | 0.0 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 501 | 0.0 |  |
|  | 15MHz | 20MHz | 10 < Wgap ≤ 35 | 321 | 0.0 |  |
|  |  |  | 0 < Wgap ≤ 10 | 501 | 0.0 |  |
|  | 20MHz | 5MHz | 25 < Wgap ≤ 45 | 321 | 0.0 |  |
|  |  |  | 0 < Wgap ≤ 25 | 451 | 0.0 |  |
|  | 20MHz | 10MHz | 20 < Wgap ≤ 40 | 321 | 0.0 |  |
|  |  |  | 0 < Wgap  ≤ 20 | 451 | 0.0 |  |
|  | 20MHz | 15MHz | 15.0 < Wgap ≤ 35.0 | 361 | 0.0 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 501 | 0.0 |  |
|  | 20MHz | 20MHz | 15.0 < Wgap ≤ 30.0 | 321 | 0.0 |  |
|  |  |  | 0.0 < Wgap ≤ 15.0 | 451 | 0.0 |  |
| DC_71A_n71A | 5 MHz | 5 MHz | 5 < Wgap ≤ 25 | 5 | 4.0 | FDD |
|  |  |  | 0 < Wgap ≤ 5 | 20 | 0 |  |
|  | 10 MHz | 5 MHz | 5 < Wgap ≤ 20 | 5 (RBstart = 9) | 4.6 |  |
|  |  |  | 0 < Wgap ≤ 5 | 20 (RBstart = 9) | 2.3 |  |
|  | 10 MHz | 10 MHz | 5 < Wgap ≤ 15 | 5 (RBstart = 9) | 4.3 |  |
|  |  |  | 0 < Wgap ≤ 5 | 20 (RBstart = 9) | 3.2 |  |
|  | 15 MHz | 10 MHz | 5 < Wgap ≤ 10 | 5 (RBstart = 2) | 22.2 |  |
|  |  |  | 0 < Wgap ≤ 5 | 20 (RBstart = 19) | 5.2 |  |
|  | 20 MHz | 10 MHz | Wgap = 5 | 5 | [22.2] |  |
| NOTE 1: 1 refers to the UL resource blocks shall be located as close as possible to the downlink operating band but confined within the transmission.NOTE 2: Wgap is the sub-block gap between the two sub-blocks.NOTE 3: The NR uplink carrier is the aggressor and the ΔRIBNC applies to the E-UTRA DL carrier only. The NR uplink carrier shall be located as close as possible to the E-UTRA downlink carrier center frequency. The NR SCS should be the smallest SCS that is compatible with the highest uplink channel bandwidth.NOTE 4: All combinations of channel bandwidths defined in Table 5.3B.1.3-1.NOTE 5: Void.NOTE 6: Void.NOTE 7: Void. NOTE 8: Void. NOTE 9:  Void.9 refers to the UL resource blocks shall be located at RBstart=75. NOTE 10: All applicable sub-block gap sizes.NOTE 11: Void.NOTE 12: Void.NOTE 13: Void.NOTE 14: Void.NOTE 15: Void. |  |  |  |  |  |  |

#### 7.3B.3.3 Inter-band EN-DC within FR1

##### 7.3B.3.3.1 ΔRIB,c for EN-DC in two bands

Table 7.3B.3.3.1-1: ΔRIB,c due to EN-DC(two bands)

| Inter-band EN-DC configuration | ΔRIB,c for E-UTRA band / NR band (dB)6 |  |
| --- | --- | --- |
|  | Component band in order of bands in configuration7 |  |
| DC_1_n28 | - | 0.2 |
| DC_1_n51 | - | 0.1 |
| DC_1_n77 | 0.2 | 0.5 |
| DC_1_n78 | - | 0.5 |
| DC_1_n105 | 0.3 | 0.6 |
| DC_2_n14 | - | 0.2 |
| DC_2_n30DC_2-2_n30 | 0.4 | 0.5 |
| DC_2_n48 | 0.2 | 0.5 |
| DC_2_n66DC_2-2_n66 | 0.3 | 0.3 |
| DC_2_n77DC_2-2_n77 | 0.2 | 0.5 |
| DC_2_n78DC_2-2_n78 | 0.2 | 0.5 |
| DC_3_n41DC_3-3_n41 | - | 03 / 0.54 |
| DC_3_n51 | 0.2 | 0.2 |
| DC_3_n77DC_3-3_n77 | 0.2 | 0.5 |
| DC_3_n78DC_3-3_n78 | 0.2 | 0.5 |
| DC_3_n105 | - | 0.3 |
| DC_4_n2 | 0.3 | 0.3 |
| DC_4_n28 | - | 0.2 |
| DC_4_n38 | 0.5 | 0.5 |
| DC_4_n41 | 0.5 | 0.51 / 12 |
| DC_4_n78 | 0.2 | 0.5 |
| DC_5_n3 | 0.2 | 0.2 |
| DC_5_n12 | 0.5 | 0.3 |
| DC_5_n41 | 0.2 | - |
| DC_5_n77 | 0.2 | 0.5 |
| DC_5_n78 | 0.2 | 0.5 |
| DC_7_n8DC_7-7_n8 | - | 0.2 |
| DC_7_n40 DC_7-7_n40 | - | 0.5 |
| DC_7_n51 | - | 0.2 |
| DC_7_n66DC_7-7_n66 | 0.5 | 0.5 |
| DC_7_n71 | - | 0.2 |
| DC_7_n77DC_7-7_n77 | - | 0.5 |
| DC_7_n78DC_7-7_n78 | - | 0.5 |
| DC_7_n79DC_7-7_n79 | - | 0.5 |
| DC_7_n105 | - | 0.2 |
| DC_8_n7 | - | 0.2 |
| DC_8_n28 | 0.2 | 0.1 |
| DC_8_n71 | 0.1 | 0.1 |
| DC_8_n77 | 0.2 | 0.5 |
| DC_8_n78 | 0.2 | 0.5 |
| DC_11_n3 | 0.3 | 0.5 |
| DC_11_n28 | - | 0.2 |
| DC_11_n77 | - | 0.5 |
| DC_11_n78 | - | 0.5 |
| DC_12_n5 | 0.3 | 0.5 |
| DC_12_n66 | 0.5 | - |
| DC_12_n71 | 0.8 | 0.8 |
| DC_12_n77 | 0.2 | 0.5 |
| DC_12_n78 | 0.2 | 0.5 |
| DC_13_n7 | 0.5 | 0.5 |
| DC_13_n77 | 0.2 | 0.5 |
| DC_13_n78 | 0.2 | 0.5 |
| DC_14_n77 | 0.2 | 0.5 |
| DC_18_n41 | - | 03 |
| DC_18_n77 | - | 0.5 |
| DC_19_n77 | - | 0.5 |
| DC_19_n78 | - | 0.5 |
| DC_20_n38 | 0.2 | - |
| DC_20_n40 | - | 0.5 |
| DC_20_n51 | - | 0.2 |
| DC_20_n77 | - | 0.5 |
| DC_20_n78 | - | 0.5 |
| DC_21_n77 | - | 0.5 |
| DC_21_n78 | - | 0.5 |
| DC_25_n41DC_25-25_n41 | - | 01 / 0.52 |
| DC_25_n77DC_25-25_n77DC_25-25_n77 | 0.2 | 0.5 |
| DC_25_n78DC_25-25_n78 | 0.2 | 0.5 |
| DC_26_n77 | - | 0.5 |
| DC_26_n78 | - | 0.5 |
| DC_28_n1 | 0.2 | - |
| DC_28_n8 | 0.1 | 0.2 |
| DC_28_n51 | - | 0.2 |
| DC_28_n66 | 0.2 | - |
| DC_28_n71 | 0.7 | 0.7 |
| DC_28_n77 | 0.2 | 0.5 |
| DC_28_n78 | 0.2 | 0.5 |
| DC_28_n105 | 0.7 | 0.7 |
| DC_30_n12 | - | 0.2 |
| DC_30_n14 | - | 0.2 |
| DC_30_n66 | 0.5 | 0.4 |
| DC_30_n77 | - | 0.5 |
| DC_38_n78 | 0.4 | 0.5 |
| DC_38_n79 | - | 0.5 |
| DC_39_n40 | 0.3 | 0.3 |
| DC_39_n41 | 0.2 | 0.2 |
| DC_39_n78 | - | 0.5 |
| DC_39_n79 | - | 0.5 |
| DC_40_n7 | 0.5 | - |
| DC_40_n77 | 0.4 | 0.5 |
| DC_40_n78 | 0.45 | 0.55 |
| DC_40_n79 | - | 0.5 |
| DC_41_n3 | 03 / 0.54 | - |
| DC_41_n77 | - | 0.5 |
| DC_41_n78 | - | 0.5 |
| DC_41_n79 | - | 0.5 |
| DC_42_n1 | 0.5 | - |
| DC_42_n3 | 0.5 | 0.2 |
| DC_42_n28 | 0.2 | 0.5 |
| DC_42_n51 | - | 0.2 |
| DC_48_n2 | 0.5 | 0.2 |
| DC_48_n25 | 0.5 | 0.2 |
| DC_48_n46 | 0.5 | - |
| DC_48_n66 | 0.5 | 0.2 |
| DC_66_n2DC_66-66_n2DC_66-66-66_n2 | 0.3 | 0.3 |
| DC_66_n7DC_66-66_n7 | 0.5 | 0.5 |
| DC_66_n12 | 0.5 | - |
| DC_66_n14 | - | 0.2 |
| DC_66_n25 | 0.3 | 0.3 |
| DC_66_n28 | - | 0.2 |
| DC_66_n30DC_66-66_n30 | 0.5 | 0.4 |
| DC_66_n38DC_66-66_n38 | 0.5 | 0.5 |
| DC_66_n41 | 0.5 | 0.51 / 12 |
| DC_66_n48DC_66-66_n48 | 0.2 | 0.5 |
| DC_66_n77DC_66-66_n77DC_66-66-66_n77 | 0.2 | 0.5 |
| DC_66_n78DC_66-66_n78 | 0.2 | 0.5 |
| DC_68_n1 | 0.2 | - |
| DC_68_n8 | 0.1 | 0.2 |
| DC_68_n77 | 0.2 | 0.5 |
| DC_68_n78 | 0.2 | 0.5 |
| DC_71_n7 | 0.2 | - |
| DC_71_n12 | 0.8 | 0.8 |
| DC_71_n38 | 0.2 | - |
| DC_71_n41 | 0.2 | - |
| DC_71_n77 | 0.2 | 0.5 |
| DC_71_n78 | 0.2 | 0.5 |
| DC_106_n41 | 0.2 | - |
| DC_106_n48 | 0.2 | 0.5 |
| NOTE 1: The requirement is applied for UE transmitting on the frequency range of 2545 – 2690 MHz.NOTE 2: The requirement is applied for UE transmitting on the frequency range of 2496 – 2545 MHz.NOTE 3: Applicable for the frequency range of 2515 – 2690 MHz.NOTE 4: Applicable for the frequency range of 2496 – 2515 MHz.NOTE 5: Only applicable for UE supporting inter-band carrier aggregation with uplink in one E-UTRA band and without simultaneous Rx/Tx.NOTE 6:  “-” denotes ΔRIB,c = 0.NOTE 7: The component band order in the configuration should be listed by the order of E-UTRA band and NR band respectively, such as for DC_1_n77 the band order from left to right is 1 and n77. |  |  |

##### 7.3B.3.3.2 ΔRIB,c for EN-DC three bands

Table 7.3B.3.3.2-1: ΔRIB,c due to EN-DC (three bands)

| Inter-band EN-DC configuration | ΔRIB,c for E-UTRA band / NR band (dB)7 |  |  |
| --- | --- | --- | --- |
|  | Component band in order of bands in configuration8 |  |  |
| DC_1_n1-n78 | - | - | 0.5 |
| DC_1-3_n28 | - | - | 0.2 |
| DC_1_n3-n28 | - | - | 0.2 |
| DC_1-3_n41DC_1-3-3_n41 | - | - | 03 / 0.54 |
| DC_1_n3-n41 | - | - | 03 / 0.54 |
| DC_1-41_n3 | - | - | 03 / 0.54 |
| DC_1-3_n77 | 0.2 | 0.2 | 0.5 |
| DC_1_n3-n77 | 0.2 | 0.2 | 0.5 |
| DC_1-3_n78DC_1-3-3_n78DC_1-1-3-3_n78 | 0.2 | 0.2 | 0.5 |
| DC_1_n3-n78 | 0.2 | 0.2 | 0.5 |
| DC_1_n3-n79 | - | - | 0.5 |
| DC_1-3_n105 | - | - | 0.3 |
| DC_1-5_n28 | - | - | 0.2 |
| DC_1-5_n40 | - | 0.2 | - |
| DC_1_n5-n40 | - | 0.2 | 0.8 |
| DC_1-5_n77 | 0.2 | 0.2 | 0.5 |
| DC_1-5_n78 | 0.2 | 0.2 | 0.5 |
| DC_1-7_n8DC_1-7-7_n8 | - | - | 0.2 |
| DC_1-7_n20 | 0.2 | 0.1 | - |
| DC_1-7_n28 | - | - | 0.2 |
| DC_1-7_n38 | - | - | 0.2 |
| DC_1-7_n40DC_1-7-7_n40 | - | 0.3 | 0.8 |
| DC_1-7_n77 | 0.2 | 0.2 | 0.5 |
| DC_1-7_n78DC_1-7-7_n78 | 0.2 | 0.2 | 0.5 |
| DC_1_n7-n78 | 0.2 | 0.2 | 0.5 |
| DC_1-7_n105 | - | - | 0.3 |
| DC_1-8_n28 | - | 0.2 | 0.2 |
| DC_1_n8-n40 | - | 0.2 | 0.5 |
| DC_1-8_n41 | - | 0.2 | - |
| DC_1-8_n71 | - | 0.2 | 0.2 |
| DC_1-8_n77 | - | 0.2 | 0.5 |
| DC_1_n8-n77 | - | 0.2 | 0.5 |
| DC_1-8_n78 | - | 0.2 | 0.5 |
| DC_1_n8-n78 | 0.2 | 0.2 | 0.5 |
| DC_1-11_n3 | - | 0.3 | 0.5 |
| DC_1-11_n28 | - | - | 0.2 |
| DC_1-11_n77 | 0.2 | - | 0.5 |
| DC_1-11_n78 | - | - | 0.5 |
| DC_1-18_n77 | - | - | 0.5 |
| DC_1-18_n78 | - | - | 0.5 |
| DC_1-19_n77 | - | - | 0.5 |
| DC_1-19_n78 | - | - | 0.5 |
| DC_1-19_n79 | 0.3 | 0.3 | - |
| DC_1-20_n28 | - | 0.2 | 0.2 |
| DC_1-20_n78 | - | - | 0.5 |
| DC_1-21_n28 | - | - | 0.2 |
| DC_1-21_n77 | - | - | 0.5 |
| DC_1-21_n78 | 0.2 | - | 0.5 |
| DC_1-20_n38 | - | 0.2 | - |
| DC_1-26_n78 | 0.2 | 0.2 | 0.5 |
| DC_1_n26-n78 | 0.2 | 0.2 | 0.5 |
| DC_1-28-n3 | - | 0.2 | - |
| DC_1-28_n7 | - | 0.2 | - |
| DC_1_n28-n40 | - | 0.2 | - |
| DC_1-28_n40 | - | 0.2 | - |
| DC_1-28_n71 | - | 0.7 | 0.7 |
| DC_1_n28-n75 | 0.2 | - | - |
| DC_1-28_n77 | - | 0.2 | 0.5 |
| DC_1_n28-n77 | 0.2 | 0.2 | 0.5 |
| DC_1-28_n78 | - | 0.2 | 0.5 |
| DC_1_n28-n78 | - | 0.2 | 0.5 |
| DC_1_n28-n79 | - | 0.2 | - |
| DC_1-32_n28 | - | - | 0.2 |
| DC_1-32_n78 | - | - | 0.5 |
| DC_1-38_n7 | - | 0.2 | - |
| DC_1-38_n28 | - | - | 0.2 |
| DC_1-38_n78 | - | - | 0.5 |
| DC_1_n38-n78 | - | - | 0.5 |
| DC_1A-40A_n28A | - | - | 0.2 |
| DC_1_n40-n41 | - | 0.8 | 0.3 |
| DC_1_n40-n71 | - | - | 0.3 |
| DC_1_n40-n77 | - | - | 0.5 |
| DC_1-40-n78 | 0.2 | 0.45 | 0.55 |
| DC_1_n40-n105 | - | - | 0.3 |
| DC_1-41_n78 | - | - | 0.5 |
| DC_1_n41-n78 | - | - | 0.5 |
| DC_1-41_n3 | - | 03/0.54 | - |
| DC_1-41_n28 | - | - | 0.2 |
| DC_1-41_n77 | - | - | 0.5 |
| DC_1_n41-n77 | - | - | 0.5 |
| DC_1-41_n78 | - | - | 0.5 |
| DC_1-42_n3 | - | 0.5 | 0.2 |
| DC_1-42_n28 | - | 0.5 | 0.5 |
| DC_1-42_n77 | 0.2 | 0.5 | 0.5 |
| DC_1-42_n78 | 0.2 | 0.5 | 0.5 |
| DC_1-42_n79 | - | 0.5 | - |
| DC_1_n71-n77 | 0.2 | 0.2 | 0.5 |
| DC_1_n75-n78 | - | - | 0.5 |
| DC_1_n77-n79 | 0.2 | - | 0.5 |
| DC_1_SUL_n77-n80 | 0.2 | 0.5 | - |
| DC_1_SUL_n77-n84 | 0.2 | 0.5 | - |
| DC_1_n78-n79 | - | 0.5 | - |
| DC_1_SUL_n78-n80 | 0.2 | 0.5 | - |
| DC_1-SUL_n78-n84 | - | 0.5 | - |
| DC_1_n78-n105 | - | 0.5 | 0.3 |
| DC_2_n2-n66 | 0.3 | 0.3 | 0.3 |
| DC_2_n2-n77 | 0.2 | 0.2 | 0.5 |
| DC_2_n2-n78 | 0.2 | 0.2 | 0.5 |
| DC_2-4-n28 | 0.3 | 0.3 | 0.5 |
| DC_2-4_n38 | 0.3 | 0.5 | 0.5 |
| DC_2-4_n41 | 0.3 | 0.5 | 0.5 |
| DC_2-4_n78 | 0.3 | 0.3 | 0.5 |
| DC_2-5_n12 | - | 0.5 | 0.3 |
| DC_2-5_n30DC_2-2-5_n30 | 0.4 | - | 0.5 |
| DC_2-5_n48 | 0.2 | - | 0.5 |
| DC_2-5_n66DC_2-5-5_n66 | 0.3 | - | 0.3 |
| DC_2-5_n77DC_2-2-5_n77 | 0.2 | 0.2 | 0.5 |
| DC_2_n5-n77 | 0.2 | - | 0.5 |
| DC_2-5_n78 | 0.2 | 0.2 | 0.5 |
| DC_2-7_n38DC_2-2-7_n38 | - | - | 0.2 |
| DC_2-7_n66DC_2-7-7_n66 | 0.3 | 0.5 | 0.5 |
| DC_2_n7-n66 | 0.3 | 0.5 | 0.5 |
| DC_2-7_n71 | - | - | 0.2 |
| DC_2_n7-n71 | 0.3 | 0.3 | - |
| DC_2-7_n77DC_2-7-7_n77 | 0.2 | 0.5 | 0.5 |
| DC_2_n7-n77 | 0.2 | 0.5 | 0.5 |
| DC_2_n7-n78 | 0.2 | 0.5 | 0.5 |
| DC_2-12_n5DC_2-2-12_n5 | - | 0.3 | 0.5 |
| DC_2-12_n30DC_2-2-12_n30 | 0.4 | - | 0.5 |
| DC_2-12_n66 DC_2-2-12_n66 | 0.3 | 0.5 | 0.3 |
| DC_2-12_n77 DC_2-2-12_n77 | 0.2 | 0.2 | 0.5 |
| DC_2_n12-n77DC_2-2_n12-n77 | 0.2 | 0.2 | 0.5 |
| DC_2-12_n78 | 0.2 | 0.2 | 0.5 |
| DC_2_n12-n78 | 0.2 | 0.2 | 0.5 |
| DC_2-13_n48 | 0.2 | - | 0.5 |
| DC_2-13_n66DC_2-2-13_n66 | 0.3 | - | 0.3 |
| DC_2-13_n77DC_2-2-13_n77 | 0.2 | 0.2 | 0.5 |
| DC_2-14_n5DC_2-2-14_n5 | - | 0.3 | 0.5 |
| DC_2-14_n30DC_2-2-14_n30 | 0.3 | - | 0.3 |
| DC_2-14_n66DC_2-2-14_n66 | 0.3 | - | 0.3 |
| DC_2-14_n77 DC_2-2-14_n77 | 0.2 | 0.2 | 0.5 |
| DC_2_n25-n66 | 0.3 | 0.3 | 0.3 |
| DC_2-28_n66 | 0.3 | 0.2 | 0.3 |
| DC_2-28_n78 | 0.2 | 0.2 | 0.5 |
| DC_2-29_n30DC_2-2-29_n30 | 0.3 | - | 0.3 |
| DC_2-29_n66DC_2-2-29_n66 | 0.3 | - | 0.3 |
| DC_2-29_n77 DC_2-2-29_n77 | 0.2 | 0.2 | 0.5 |
| DC_2-29-n78 | 0.2 | - | 0.5 |
| DC_2-30_n2 | 0.5 | 0.3 | 0.5 |
| DC_2-30_n5  DC_2-2-30_n5 | 0.4 | 0.5 | - |
| DC_2-30_n66  DC_2-2-30_n66 | 0.4 | 0.5 | 0.4 |
| DC_2-30_n77 DC_2-2-30_n77 | 0.2 | - | 0.5 |
| DC_2_n38-n66 | 0.3 | 0.5 | 0.5 |
| DC_2-38_n78 | 0.5 | 0.5 | 0.5 |
| DC_2_n38-n78 | 0.5 | 0.5 | 0.5 |
| DC_2_n41-n66DC_2-2_n41-n66 | 0.3 | 0.5 | 0.5 |
| DC_2_n41-n77 | 0.2 | 0.5 | 0.5 |
| DC_2_n41-n78 | 0.2 | 0.5 | 0.5 |
| DC_2-48_n2 | 0.2 | 0.5 | 0.2 |
| DC_2-48_n5 | 0.2 | 0.5 | - |
| DC_2-48_n12 | 0.2 | 0.5 | - |
| DC_2-48_n48 | 0.2 | 0.5 | 0.5 |
| DC_2-48_n66 | 0.3 | 0.5 | 0.3 |
| DC_2-48_n77DC_2-48-48_n77DC_2-48-48-48_n77 | - | 0.2 | 0.1 |
| DC_2-48_n71 | 0.2 | 0.5 | - |
| DC_2-66_n2 DC_2-66-66_n2 | 0.3 | 0.3 | 0.3 |
| DC_2-66_n5DC_2-2-66_n5DC_2-66-66_n5DC_2-2-66-66_n5DC_2-66-66-66_n5 | 0.3 | 0.3 | - |
| DC_2-66-n7 | 0.3 | 0.5 | 0.5 |
| DC_2-66_n12 | 0.3 | 0.3 | 0.5 |
| DC_2-66_n25 | 0.3 | 0.3 | 0.3 |
| DC_2-66-n28 | 0.3 | 0.3 | 0.2 |
| DC_2-66_n30DC_2-2-66_n30 DC_2-66-66_n30 DC_2-2-66-66_n30 | 0.4 | 0.4 | 0.5 |
| DC_2-66_n38DC_2-2-66_n38DC_2-66-66_n38 | 0.3 | 0.5 | 0.5 |
| DC_2-66_n41 | 0.3 | 0.5 | 0.51 / 12 |
| DC_2-66_n48DC_2-66-66_n48 | 0.3 | 0.3 | 0.5 |
| DC_2-(n)66DC_2-66_n66 DC_2-2-(n)66DC_2-2-66-(n)66DC_2-2-66-66_n66DC_2-66-(n)66 | 0.3 | 0.3 | 0.3 |
| DC_2_(n)66 | 0.3 | 0.3 | 0.3 |
| DC_2-66_n71 | 0.3 | 0.3 | - |
| DC_2_n66-n71DC_2-2_n66-n71 | 0.3 | 0.3 | - |
| DC_2-66_n77DC_2-2-66_n77DC_2-66-66_n77DC_2-2-66-66_n77 | 0.2 | 0.2 | 0.5 |
| DC_2_n66-n77DC_2-2_n66-n77 | 0.3 | 0.3 | 0.5 |
| DC_2-66_n78DC_2-66-66_n78DC_2_n66-n78 | 0.3 | 0.3 | 0.5 |
| DC_2-71_n7 | - | 0.2 | - |
| DC_2-71_n66DC_2-2-71_n66 | 0.3 | - | 0.3 |
| DC_2_n71-n77DC_2-2_n71-n77 | 0.2 | 0.2 | 0.5 |
| DC_2-71_n77 | 0.2 | 0.2 | 0.5 |
| DC_2-71_n78DC_2-2-71_n78 | 0.2 | 0.2 | 0.5 |
| DC_2_n71-n78DC_2-2_n71-n78 | 0.2 | 0.2 | 0.5 |
| DC_3_n1-n28 | - | - | 0.2 |
| DC_3_n1-n77 | 0.2 | 0.2 | 0.5 |
| DC_3_n1-n78 | 0.2 | 0.2 | 0.5 |
| DC_3_n1-n105 | - | - | 0.3 |
| DC_3_n3-n41 | - | - | 03/0.54 |
| DC_(n)3-n67 | 0.3 | 0.3 | - |
| DC_3_n3-n67 | 0.3 | 0.3 | - |
| DC_3_n3-n77 | 0.2 | 0.2 | 0.5 |
| DC_(n)3-n77 | - | 0.2 | 0.5 |
| DC_(n)3-n78 | - | 0.2 | 0.5 |
| DC_3_n3-n78 | 0.2 | 0.2 | 0.5 |
| DC_3-5_n28 | - | 0.2 | 0.2 |
| DC_3-5_n77 | 0.2 | 0.2 | 0.5 |
| DC_3-5_n78 | 0.2 | 0.2 | 0.5 |
| DC_3_n5-n105 | - | - | 0.3 |
| DC_3-7_n38 | - | - | 0.2 |
| DC_3-7_n40DC_3-7-7_n40 | - | 0.3 | 0.8 |
| DC_3-7_n77DC_3-3-7_n77DC_3-7-7_n77DC_3-3-7-7_n77 | 0.2 | 0.2 | 0.5 |
| DC_3-7_n8DC_3-3-7_n8DC_3-7-7_n8DC_3-3-7-7_n8 | - | - | 0.2 |
| DC_3-7_n78DC_3-7-7_n78DC_3-3-7_n78DC_3-3-7-7_n78 | 0.2 | 0.2 | 0.5 |
| DC_3_n7-n78 | 0.2 | 0.2 | 0.5 |
| DC_3-7_n79DC_3-3-7_n79DC_3-7-7_n79DC_3-3-7-7_n79 | - | - | 0.5 |
| DC_3-7_n105 | - | - | 0.3 |
| DC_3-8_n28 | - | 0.2 | 0.1 |
| DC_3-8_n41DC_3-3-8_n41 | - | - | 03/0.54 |
| DC_3_n8-n41 | - | - | 03/0.54 |
| DC_3-8_n71 | - | 0.2 | 0.1 |
| DC_3-8_n77 | 0.2 | 0.2 | 0.5 |
| DC_3_n8-n77 | 0.2 | 0.2 | 0.5 |
| DC_3-8_n78DC_3-3-8_n78 | 0.2 | 0.2 | 0.5 |
| DC_3_n8-n78 DC_3-3_n8-n78 | 0.2 | 0.2 | 0.5 |
| DC_3-11_n28 | 0.3 | 0.5 | 0.2 |
| DC_3-11_n77 | 0.3 | 0.5 | 0.5 |
| DC_3-11_n79 | 0.3 | 0.5 | - |
| DC_3-18_n41 | - | - | 03 / 0.54 |
| DC_3-18-n77 | 0.2 | - | 0.5 |
| DC_3-18-n78 | 0.2 | - | 0.5 |
| DC_3-19_n77 | 0.2 | - | 0.5 |
| DC_3-19_n78 | 0.2 | - | 0.5 |
| DC_3-20_n28 | - | 0.1 | 0.1 |
| DC_3-20_n38 | - | 0.2 | - |
| DC_3_n20-n67 | - | 0.1 | 0.1 |
| DC_3-20_n78 | 0.2 | - | 0.5 |
| DC_3_n20-n78DC_3-3_n20-n78 | 0.2 | - | 0.5 |
| DC_3-21_n1 | 0.3 | 0.5 | - |
| DC_3-21_n28 | 0.3 | 0.5 | - |
| DC_3-21_n77 | 0.3 | 0.5 | 0.5 |
| DC_3-21_n78 | 0.3 | 0.5 | 0.5 |
| DC_3-21_n79 | 0.3 | 0.5 | - |
| DC_3_n26-n78 | 0.2 | 0.2 | 0.5 |
| DC_3-28_n1 | - | 0.2 | - |
| DC_3-28_n5 | - | 0.1 | 0.1 |
| DC_3-28_n41 | - | - | 03 / 0.54 |
| DC_3-28_n71 | - | 0.7 | 0.7 |
| DC_3_n28-n75 | 0.5 | 0.5 | - |
| DC_3-28_n77 | 0.2 | 0.2 | 0.5 |
| DC_3_n28-n77 | 0.2 | 0.2 | 0.5 |
| DC_3-28_n78 | 0.2 | - | 0.5 |
| DC_3_n28-n78 | 0.2 | - | 0.5 |
| DC_3-32_n28 | 0.5 | - | 0.5 |
| DC_3-32_n41 | - | - | 03 / 0.54 |
| DC_3-32_n78 | 0.2 | - | 0.5 |
| DC_3-38_n7 | - | 0.2 | - |
| DC_3-38_n28 | - | - | 0.2 |
| DC_3-38_n78 | 0.2 | 0.4 | 0.5 |
| DC_8A-38A_n78A | 0.2 | 0.4 | 0.5 |
| DC_3_n38-n78 | 0.5 | - | 0.5 |
| DC_3_n40-n41 | - | - | 03 / 0.54 |
| DC_3_n40-n71 | - | - | 0.3 |
| DC_3_n40-n77 | 0.2 | - | 0.5 |
| DC_3-40-n78 | 0.2 | 0.45 | 0.55 |
| DC_3_n40-n105 | - | - | 0.3 |
| DC_3-41_n3 | - | 03/0.54 | - |
| DC_3-41_n28 | - | 03/0.54 | - |
| DC_3-41_n41DC_3-3-41_n41 | - | 03 / 0.54 | 03 / 0.54 |
| DC_3-(n)41 | - | 03 / 0.54 | 03 / 0.54 |
| DC_3A_n41A-n71A | - | 03 / 0.54 | 0.2 |
| DC_3-41-n77 | 0.2 | 03 / 0.54 | 0.54 |
| DC_3-41_n78DC_3_n41-n78 | 0.2 | 03 / 0.54 | 0.54 |
| DC_3-41-n79 | 0.2 | 03 / 0.54 | - |
| DC_3_n41-n79 | 0.2 |  | - |
| DC_3_SUL_n41-n80 | - | 03 / 0.54 | - |
| DC_3-42_n1 | 0.2 | 0.5 | 0.2 |
| DC_3-42_n28 | 0.2 | 0.5 | 0.2 |
| DC_3-42_n77 | 0.2 | 0.5 | 0.5 |
| DC_3-42_n78 | 0.2 | 0.5 | 0.5 |
| DC_3-42_n79 | 0.2 | 0.5 | - |
| DC_3-67_n3 | 0.3 | - | 0.3 |
| DC_3_n71-n77 | 0.2 | 0.3 | 0.5 |
| DC_3A_n71A-n78A | - | 0.3 | 0.5 |
| DC_3_n75-n78 | 0.2 | - | 0.5 |
| DC_3_n77-n79 | 0.2 | 0.5 | - |
| DC_3_SUL_n77-n80 | 0.2 | 0.5 | - |
| DC_3_SUL_n77-n84 | 0.2 | 0.5 | - |
| DC_3_n78-n79DC_3-3_n78-n79 | 0.2 | 0.5 | - |
| DC_3-SUL_n78-n80 | 0.2 | 0.5 | - |
| DC_3-SUL_n78-n82 | 0.2 | 0.5 | - |
| DC_3_SUL_n78-n84 | 0.2 | 0.5 | - |
| DC_3_n78-n105 | - | 0.5 | 0.3 |
| DC_4-5_n78 | 0.2 | 0.2 | 0.5 |
| DC_4-7_n28 | 0.5 | 0.5 | 0.2 |
| DC_4-7_n78 | 0.5 | 0.5 | 0.5 |
| DC_5_n1-n28 | - | - | 0.2 |
| DC_5_n1-n78 | 0.2 | 0.2 | 0.5 |
| DC_5_n2-n41 | 0.2 | - | - |
| DC_5_n2-n66 | - | 0.3 | 0.3 |
| DC_5_n2-n77 | 0.2 | 0.2 | 0.5 |
| DC_5_n3-n28 | 0.1 | - | 0.1 |
| DC_5_n3-n78 | 0.2 | 0.2 | 0.5 |
| DC_5_n5-n77 | 0.2 | 0.2 | 0.5 |
| DC_5-7_n28DC_5-7-7_n28 | 0.2 | - | 0.2 |
| DC_5-7_n40DC_5-7-7_n40 | 0.2 | 0.3 | 0.7 |
| DC_5-7_n66 | - | 0.5 | 0.5 |
| DC_5_n7-n66 | - | 0.5 | 0.5 |
| DC_5-7_n71 | - | - | 0.2 |
| DC_5-7_n77 | 0.2 | 0.2 | 0.5 |
| DC_5_n7-n77 | 0.2 | 0.2 | 0.5 |
| DC_5-7_n78, DC_5-7-7_n78 | 0.2 | 0.2 | 0.5 |
| DC_5_n7-n78 | 0.2 | 0.2 | 0.5 |
| DC_5_(n)12 | 0.5 | 0.3 | 0.3 |
| DC_5-13_n77 | 0.2 | 0.2 | 0.5 |
| DC_5_n28-n77 | 0.2 | 0.2 | 0.8 |
| DC_5_n28-n78 | 0.2 | 0.2 | 0.8 |
| DC_5_n28-n79 | 0.2 | 0.2 | 0.5 |
| DC_5-30_n2 | - | 0.5 | 0.4 |
| DC_5_30_n66 | - | 0.5 | 0.4 |
| DC_5-30_n77 | 0.2 | - | 0.5 |
| DC_5_n38-n66 | 0.2 | - | - |
| DC_5_n40-n77 | 0.2 | - | 0.5 |
| DC_5_n40-n78 | 0.2 | 0.4 | 0.5 |
| DC_5_n41-n66 | 0.2 | 0.51 / 12 | 0.5 |
| DC_5_n41-n77 | 0.2 | - | 0.5 |
| DC_5_n41-n78 | 0.2 | - | 0.5 |
| DC_5-48_n12 | 0.5 | - | 0.3 |
| DC_5-48_n77 | 0.2 | 0.5 | 0.5 |
| DC_5-66_n2DC_5-5-66_n2DC_5-66-66_n2DC_5-5-66-66_n2 | - | 0.3 | 0.3 |
| DC_5-66-n7 | - | 0.5 | 0.5 |
| DC_5-66_n12 | - | 0.5 | 0.5 |
| DC_5-66_n30DC_5-66-66_n30 | - | 0.4 | 0.5 |
| DC_5-66_n48DC_5-66-66_n48 | - | 0.2 | 0.5 |
| DC_5-(n)66DC_5-66-(n)66 | - | 0.5 | 0.5 |
| DC_5-66_n77 DC_5-66-66_n77 | 0.2 | 0.2 | 0.5 |
| DC_5_n66-n77 | 0.2 | 0.2 | 0.5 |
| DC_5-66_n78 | 0.2 | 0.2 | 0.5 |
| DC_5_n66-n78 | 0.2 | 0.2 | 0.5 |
| DC_5_SUL_n78-n89 | 0.2 | 0.5 | - |
| DC_7_n1-n8DC_7-7_n1-n8 | - | - | 0.2 |
| DC_7_n1-n28 | - | - | 0.2 |
| DC_7_n1-n78 | 0.2 | 0.2 | 0.5 |
| DC_7_n2-n66 | 0.5 | 0.3 | 0.5 |
| DC_7_n2-n71 | 0.3 | 0.3 | - |
| DC_7_n2-n77 | 0.5 | 0.2 | 0.5 |
| DC_7_n2-n78 | 0.5 | 0.2 | 0.5 |
| DC_7_n3-n78 | 0.2 | 0.2 | 0.5 |
| DC_7_n5-n40 | 0.3 | 0.2 | 0.8 |
| DC_7_n7-n78 | 0.5 | 0.5 | 0.5 |
| DC_7-8_n1DC_7-7-8_n1 | - | 0.2 | - |
| DC_7-8_n28 | - | 0.2 | 0.1 |
| DC_7-8_n40 | - | 0.2 | 0.5 |
| DC_7_n8-n40 | - | 0.2 | 0.5 |
| DC_7-8_n3 | - | 0.2 | - |
| DC_7-8_n77 | - | 0.2 | 0.5 |
| DC_7-8_n78DC_7-7-8_n78 | - | 0.2 | 0.5 |
| DC_7_n8-n78 DC_7-7_n8-n78 | - | 0.2 | 0.5 |
| DC_7-12_n66 | 0.5 | 0.1 | 0.5 |
| DC_7_n12-n77 | 0.2 | 0.5 | 0.5 |
| DC_7-12_n77 | 0.2 | 0.5 | 0.5 |
| DC_7-12_n78 | 0.2 | 0.5 | 0.5 |
| DC_7_n12-n78 | 0.2 | 0.2 | 0.5 |
| DC_7-13_n66 | 0.5 | - | 0.5 |
| DC_7-20_n28 | - | 0.2 | 0.2 |
| DC_7-20_n38 | - | - | 0.2 |
| DC_7-20_n78 | - | - | 0.5 |
| DC_7_n25-n71 | - | - | 0.2 |
| DC_7-25_n77DC_7-7-25_n77DC_7-25-25_n77DC_7-7-25-25_n77 | 0.5 | 0.2 | 0.5 |
| DC_7-25_n78DC_7-7-25_n78DC_7-25-25_n78DC_7-7-25-25_n78 | 0.5 | 0.2 | 0.5 |
| DC_7_n25-n66 | 0.5 | 0.3 | 0.5 |
| DC_7-26_n78 | 0.2 | 0.2 | 0.5 |
| DC_7_n26-n78 | 0.2 | 0.2 | 0.5 |
| DC_7-28_n1DC_7-7-28_n1 | - | 0.2 | - |
| DC_7_n28-n40 | - | - | 0.5 |
| DC_7-28_n40 | - | - | 0.5 |
| DC_7-28_n66 | - | 0.2 | - |
| DC_7-28_n78 | - | - | 0.5 |
| DC_7_n28-n78DC_7-7_n28-n78 | - | - | 0.5 |
| DC_7-29_n78 | - | - | 0.5 |
| DC_7-32_n8 | - | - | 0.2 |
| DC_7-32_n28 | - | - | 0.2 |
| DC_7-32_n78 | - | - | 0.5 |
| DC_7-38_n78 | - | - | 0.5 |
| DC_7_n38-n78 | - | - | 0.5 |
| DC_7-40_n1 | 0.3 | 0.8 | - |
| DC_7_n40-n77DC_7-7_n40-n77 | - | 0.5 | 0.5 |
| DC_7_n1-n40 | 0.3 | - | 0.8 |
| DC_7-40-n78 | - | 0.45 | 0.55 |
| DC_7-46_n78 | - | - | 0.5 |
| DC_7_n40-n78DC_7-7_n40-n78 | - | 0.5 | 0.5 |
| DC_7_n40-n105 | - | 0.5 | 0.2 |
| DC_7-66_n7DC_7-66-66_n7 | 0.5 | 0.5 | 0.5 |
| DC_7-66_n12 | 0.5 | 0.5 | 0.5 |
| DC_7-66_n25DC_7-7-66_n25 | 0.3 | 0.5 | 0.5 |
| DC_7-66-n28 | 0.5 | 0.5 | 0.2 |
| DC_7-66_n38 | - | - | 0.2 |
| DC_7-(n)66DC_7-66_n66DC_7-7-(n)66DC_7-7-66_n66DC_7-7-66-(n)66DC_7-66-(n)66 | 0.5 | 0.5 | 0.5 |
| DC_7-66_n77DC_7-7-66_n77 | 0.5 | 0.5 | 0.5 |
| DC_7_n66-n77 | 0.5 | 0.5 | 0.5 |
| DC_7_n66-n78DC_7-7_n66-n78 | 0.5 | 0.5 | 0.5 |
| DC_7-66_n71 DC_7-66-66_n71 | 0.5 | 0.5 | 0.1 |
| DC_7_n66-n71 | 0.5 | 0.5 | 0.1 |
| DC_7-71_n25 | 0.3 | - | 0.3 |
| DC_7_n71-n78 | - | 0.2 | 0.5 |
| DC_7-71_n66 | 0.5 | 0.1 | 0.5 |
| DC_7_n71-n77 | - | 0.2 | 0.5 |
| DC_7-71_n77 | 0.2 | 0.5 | 0.5 |
| DC_7-71_n78 | 0.2 | 0.5 | 0.5 |
| DC_7_n75-n78 | - | - | 0.5 |
| DC_7_SUL_n78-n80 | 0.2 | 0.5 | - |
| DC_7_n78-n79DC_7-7_n78-n79 | 0.5 | 0.5 | 0.5 |
| DC_7_n78-n105 | - | 0.5 | 0.2 |
| DC_8_n1-n28 | 0.2 | - | 0.2 |
| DC_8_n1-n40 | 0.2 | - | 0.5 |
| DC_8_n1-n41 | 0.2 | - | 0.5 |
| DC_8_n1-n77 | 0.2 | 0.2 | 0.5 |
| DC_8_n3-n77 | 0.2 | 0.2 | 0.5 |
| DC_8_n3-n78 | 0.2 | 0.2 | 0.5 |
| DC_8_n3-n79 | - | - | 0.5 |
| DC_8_n7-n78 | 0.2 | - | 0.5 |
| DC_8-11_n1 | 0.3 | 0.4 | 0.3 |
| DC_8_n1-n78 | 0.2 | - | 0.5 |
| DC_8_n3-n28 | 0.2 | - | 0.1 |
| DC_8-11_n3 | - | 0.3 | 0.5 |
| DC_8-11_n28 | 0.2 | - | 0.2 |
| DC_8-11_n77 | 0.2 | - | 0.5 |
| DC_8-11_n78 | 0.2 | - | 0.2 |
| DC_8-11_n79 | 0.3 | 0.4 | - |
| DC_8-20_n28 | 0.2 | - | 0.1 |
| DC_8-20_n78 | 0.2 | - | 0.5 |
| DC_8A-28A_n1A | 0.2 | 0.2 | - |
| DC_8-28_n40 | 0.2 | 0.2 | - |
| DC_8-28_n71 | 0.2 | 0.7 | 0.7 |
| DC_8-28_n77 | 0.2 | 0.2 | 0.5 |
| DC_8_n28-n78 | 0.2 | 0.2 | 0.5 |
| DC_8-32_n3 | - | 0.5 | 0.3 |
| DC_8A-38A_n28A | 0.2 | - | 0.1 |
| DC_8_n39-n40 | - | 0.3 | 0.3 |
| DC_8-40_n1 | 0.2 | 0.5 | - |
| DC_8A-40A_n28A | 0.2 | - | 0.1 |
| DC_8_n40-n71 | 0.2 | 0.8 | 0.2 |
| DC_8_n40-n77 | 0.2 | 0.4 | 0.5 |
| DC_8-40-n78 | 0.2 | 0.45 | 0.55 |
| DC_8-41_n3 | - | 03/0.54 | - |
| DC_8-41_n77 | 0.2 | - | 0.5 |
| DC_8_n41-n78 | 0.2 | - | 0.5 |
| DC_8-42_n1 | 0.2 | 0.5 | - |
| DC_8-42_n3 | 0.2 | 0.5 | 0.2 |
| DC_8-42_n28 | 0.2 | 0.5 | 0.5 |
| DC_8-42_n77 | 0.2 | 0.5 | 0.5 |
| DC_8-42_n79 | 0.2 | 0.5 | - |
| DC_8_n71-n77 | 0.2 | 0.2 | 0.5 |
| DC_8_SUL_n78-n80 | 0.2 | 0.5 | - |
| DC_8_n28-n77 | 0.2 | 0.2 | 0.5 |
| DC_8_n77-n79 | 0.2 | 0.5 | - |
| DC_8-SUL_n78-n81 | 0.2 | 0.2 | - |
| DC_11_n1-n3 | 0.3 | - | 0.5 |
| DC_11_n1-n77 | 0.5 | 0.2 | 0.5 |
| DC_11_n3-n28 | 0.3 | 0.5 | 0.2 |
| DC_11_n3-n77 | 0.3 | 0.5 | 0.5 |
| DC_11_n3-n79 | 0.3 | 0.5 | 0.5 |
| DC_11-18_n77 | - | - | 0.5 |
| DC_11-18_n78 | - | - | 0.5 |
| DC_11_n28-n77 | - | 0.2 | 0.5 |
| DC_12_(n)5 | 0.5 | 0.3 | 0.5 |
| DC_12_n2-n66 | 0.5 | 0.3 | 0.3 |
| DC_12_n2-n77 | 0.2 | 0.2 | 0.5 |
| DC_12_n2-n78 | 0.2 | 0.2 | 0.5 |
| DC_12_n7-n66 | 0.5 | 0.5 | 0.5 |
| DC_12_n7-n77 | 0.5 | 0.2 | 0.5 |
| DC_12_n7-n78 | 0.2 | 0.5 | 0.5 |
| DC_12_n25-n66 | 0.5 | 0.3 | 0.3 |
| DC_12_n25-n77 | 0.2 | - | 0.5 |
| DC_12-30_n2 | - | 0.5 | 0.4 |
| DC_12-30_n5 | 0.5 | 0.5 | - |
| DC_12-30_n66 | 0.5 | 0.5 | 0.4 |
| DC_12-30_n77 | 0.2 | - | 0.5 |
| DC_12_n41-n66 | 0.5 | 0.51 / 12 | 0.5 |
| DC_12-48_n5 | 0.3 | - | 0.5 |
| DC_12-66_n2 | 0.5 | 0.3 | 0.3 |
| DC_12-66_n5DC_12-66-66_n5 | 0.5 | 0.5 | - |
| DC_12-66_n7 | 0.5 | 0.5 | 0.5 |
| DC_12-66_n25 | 0.5 | 0.3 | 0.3 |
| DC_12-66_n30DC_12-66-66_n30 | 0.5 | 0.4 | 0.5 |
| DC_12-66_n41 | 0.5 | 0.5 | 0.51 / 12 |
| DC_12-(n)66 | 0.5 | 0.5 | 0.5 |
| DC_12_n66-n77 | 0.5 | 0.5 | 0.5 |
| DC_12-66_n77 DC_12-66-66_n77 | 0.5 | 0.5 | 0.5 |
| DC_12-66_n78 | 0.2 | 0.2 | 0.5 |
| DC_12_n66-n78 | 0.2 | 0.2 | 0.5 |
| DC_13_n2-n77 | - | 0.2 | 0.5 |
| DC_13_n5-n48 | 0.3 | 0.5 | - |
| DC_13_n5-n77 | 0.2 | 0.2 | 0.5 |
| DC_13_n7-n78 | 0.2 | 0.5 | 0.5 |
| DC_13_n25-n66 | - | 0.3 | 0.3 |
| DC_13-48_n2 | - | 0.5 | 0.2 |
| DC_13-48_n66 | - | 0.5 | 0.2 |
| DC_13_n48-n66 | - | 0.5 | 0.2 |
| DC_13-48_n77 | 0.2 | 0.5 | 0.5 |
| DC_13-66_n2DC_13-66-66_n2 | - | 0.3 | 0.3 |
| DC_13-66_n48DC_13-66-66_n48 | - | 0.2 | 0.5 |
| DC_13-(n)66DC_13-66-(n)66 | - | 0.5 | 0.5 |
| DC_13-66_n77DC_13-66-66_n77 | 0.3 | 0.3 | 0.5 |
| DC_13_n66-n77 | - | 0.2 | 0.5 |
| DC_14-30_n2 | - | 0.5 | 0.4 |
| DC_14-30_n5 | 0.5 | 0.5 | - |
| DC_14-30_n66 | - | 0.5 | 0.4 |
| DC_14-30_n77 | 0.2 | - | 0.5 |
| DC_14-66_n2 DC_14-66-66_n2 | - | 0.3 | 0.3 |
| DC_14-66_n5DC_14-66-66_n5 | 0.5 | 0.5 | - |
| DC_14-66_n30DC_14-66-66_n30 | - | 0.4 | 0.5 |
| DC_14-66_n77 DC_14-66-66_n77 | 0.2 | 0.5 | 0.5 |
| DC_18_n3-n77 | - | 0.2 | 0.5 |
| DC_18_n3-n78 | - | 0.2 | 0.5 |
| DC_18-28_n77 | - | - | 0.5 |
| DC_18_n28-n77 | - | - | 0.5 |
| DC_18-28_n78 | - | - | 0.5 |
| DC_18_n28-n78 | - | - | 0.5 |
| DC_18-41_n3 | - | 03 / 0.54 | - |
| DC_18-41_n77 | - | - | 0.5 |
| DC_18_n41-n77 | - | - | 0.5 |
| DC_18-41_n78 | - | - | 0.5 |
| DC_18_n41-n78 | - | - | 0.5 |
| DC_18-42_n77 | - | 0.5 | 0.5 |
| DC_18-42_n78 | - | 0.5 | 0.5 |
| DC_18-42_n79 | - | 0.5 | - |
| DC_19_n1-n77 | - | - | 0.5 |
| DC_19_n1-n78 | - | - | 0.5 |
| DC_19_n1-n79 | 0.3 | 0.3 | - |
| DC_19-21_n77 | - | - | 0.5 |
| DC_19-21_n78 | - | - | 0.5 |
| DC_19-42_n1 | - | 0.5 | - |
| DC_19-42_n77 | - | 0.5 | 0.5 |
| DC_19-42_n78 | - | 0.5 | 0.5 |
| DC_19-42_n79 | - | 0.5 | - |
| DC_19_n77-n79 | - | 0.5 | - |
| DC_19_n78-n79 | - | 0.5 | - |
| DC_20_n1-n28 | - | 0.2 | 0.2 |
| DC_20_n1-n41 | 0.2 | - | 0.5 |
| DC_20_n1-n67 | - | 0.2 | 0.2 |
| DC_20_n3-n67 | 0.1 | - | 0.1 |
| DC_20_n1-n78 | - | - | 0.5 |
| DC_20_n3-n78 | - | 0.2 | 0.5 |
| DC_20_n7-n28 | 0.2 | - | 0.2 |
| DC_20_n7-n78 | - | - | 0.5 |
| DC_20_n8-n78 | 0.2 | 0.2 | 0.5 |
| DC_20-28_n1 | 0.2 | 0.2 | - |
| DC_20-28_n3 | 0.3 | 0.2 | 0.3 |
| DC_20-28_n7 | 0.2 | 0.2 | - |
| DC_20_n28-n75 | - | 0.2 | - |
| DC_20_n28-n78 | 0.2 | 0.2 | 0.5 |
| DC_20-32_n28 | - | - | 0.2 |
| DC_20-32_n78 | - | - | 0.5 |
| DC_20-38_n1 | 0.2 | - | - |
| DC_20A-38A_n28A | 0.2 | - | 0.2 |
| DC_20-38_n78 | - | 0.4 | 0.5 |
| DC_20_n38-n78 | 0.2 | - | 0.5 |
| DC_20A-40A_n28A | - | 0.5 | - |
| DC_20-40-n78 | 0.2 | 0.45 | 0.55 |
| DC_20_n41-n78 | - | - | 0.5 |
| DC_20-(n)41 | 0.3 | 0.3 | 0.3 |
| DC_20-67_n3 | 0.1 | 0.1 | - |
| DC_20_n75-n78 | - | - | 0.5 |
| DC_20_n76-n78 | - | - | 0.5 |
| DC_20_SUL_n78-n80 | - | 0.5 | - |
| DC_20-SUL_n78-n82 | - | 0.5 | - |
| DC_20-SUL_n78-n83 | 0.2 | 0.5 | - |
| DC_20_n78-n92 | - | 0.5 | - |
| DC_21_n1-n77 | - | - | 0.5 |
| DC_21_n1-n78 | - | 0.2 | 0.5 |
| DC_21_n28-n77 | 0.5 | 0.2 | 0.5 |
| DC_21_n28-n78 | 0.5 | 0.2 | 0.5 |
| DC_21-42_n1 | - | 0.5 | - |
| DC_21-42_n77 | - | 0.5 | 0.5 |
| DC_21-42_n78 | - | 0.5 | 0.5 |
| DC_21-42_n79 | - | 0.5 | - |
| DC_21_n77-n79 | - | 0.5 | - |
| DC_21_n78-n79 | - | 0.5 | - |
| DC_25-41_n41DC_25_(n)41DC_25-25-41_n41DC_25-25_(n)41 | - | 01 / 0.52 | 01 / 0.52 |
| DC_25-66_n77DC_25-25-66_n77 | 0.2 | 0.2 | 0.5 |
| DC_25-66_n78DC_25-25-66_n78 | 0.2 | 0.2 | 0.5 |
| DC_28-SUL_n78-n83 | 0.2 | 0.5 | - |
| DC_28_n1-n5 | 0.2 | - | - |
| DC_28_n1-n40 | 0.2 | - | - |
| DC_28_n1-n78 | 0.2 | - | 0.5 |
| DC_28_n1-n105 | 0.7 | - | 0.7 |
| DC_28_n3-n77 | 0.2 | 0.2 | 0.5 |
| DC_28_n3-n78 | - | 0.2 | 0.5 |
| DC_28_n5-n40 | 0.2 | 0.2 | 0.8 |
| DC_28_n5-n78 | 0.2 | 0.2 | 0.5 |
| DC_28_n5-n105 | 0.7 | 0.2 | 0.7 |
| DC_28_n7-n78 | - | - | 0.5 |
| DC_28-32_n1 | 0.2 | - | - |
| DC_28-32_n41 | 0.2 | - | - |
| DC_28-38_n1 | 0.2 | - | - |
| DC_28-38_n78 | 0.2 | 0.4 | 0.5 |
| DC_28A-40A_n1A | 0.2 | - | - |
| DC_28_n40-n71 | 0.7 | 0.2 | 0.7 |
| DC_28_n40-n77 | - | - | 0.5 |
| DC_28-40_n78 | 0.2 | 0.4 | 0.5 |
| DC_28_n40-n78 | 0.2 | 0.45 | 0.55 |
| DC_28-41_n77 | 0.2 | - | 0.5 |
| DC_28-41_n78 | 0.2 | - | 0.5 |
| DC_28-41_n79 | - | - | 0.5 |
| DC_28-42_n77 | 0.2 | 0.5 | 0.5 |
| DC_28-42_n78 | 0.2 | 0.5 | 0.5 |
| DC_28-42_n79 | 0.2 | 0.5 | - |
| DC_28-66_n7 | 0.2 | 0.5 | 0.5 |
| DC_28-66_n66 | 0.2 | - | - |
| DC_28_n71-n77 | 0.7 | 0.75 | 0.57 |
| DC_28_n78-n105 | 0.7 | 0.5 | 0.7 |
| DC_29-30_n2 | - | 0.3 | 0.5 |
| DC_29-30-n66 | - | 0.5 | 0.4 |
| DC_29-30_n77 | 0.2 | - | 0.5 |
| DC_29-66_n2DC_29-66-66_n2 | - | 0.3 | 0.3 |
| DC_29-66_n30DC_29-66-66_n30 | - | 0.4 | 0.5 |
| DC_29-(n)66 | - | 0.5 | 0.5 |
| DC_29-66_n77 DC_29-66-66_n77 | 0.5 | 0.5 | 0.5 |
| DC_29-66-n78 | - | 0.2 | 0.5 |
| DC_30-66_n2 | 0.5 | 0.4 | 0.4 |
| DC_30-66_n5DC_30-66-66_n5DC_30-66-66-66_n5 | - | 0.4 | 0.5 |
| DC_30-66-n66 | 0.5 | 0.5 | 0.4 |
| DC_30-66_n77 DC_30-66-66_n77 | 0.5 | 0.4 | 0.5 |
| DC_32-38_n28 | - | - | 0.2 |
| DC_38_n3-n78 | - | 0.5 | 0.5 |
| DC_38_n28-n78 |  | 0.2 | 0.5 |
| DC_38A-40A_n1A | 0.5 | 0.5 | - |
| DC_38A-40A_n28A | 0.5 | 0.5 | - |
| DC_39_n40-n41 | 0.3 | 0.6 | 0.6 |
| DC_39_n40-n79 | 0.3 | 0.3 | 0.5 |
| DC_39_n41-n79 | 0.2 | 0.2 | 0.5 |
| DC_40_n1-n78 | 0.4 | 0.2 | 0.5 |
| DC_41_n1-n78 | - | - | 0.5 |
| DC_41_n1-n3 | 03 / 0.54 | - | - |
| DC_41_n1-n77 | - | - | 0.5 |
| DC_40-42_n77 | 0.45 | 0.55 | 0.55 |
| DC_40-42_n78 | 0.45 | 0.55 | 0.55 |
| DC_41_n3-n41 | 03 / 0.54 | - | 03 / 0.54 |
| DC_41_n3-n77 | 03 / 0.54 | 0.2 | 0.5 |
| DC_41_n3-n78 | 03 / 0.54 | 0.2 | 0.5 |
| DC_41_n28-n77 | - | 0.2 | 0.5 |
| DC_41_n28-n78 | - | 0.2 | 0.5 |
| DC_41_n41-n77 | - | - | 0.5 |
| DC_41_n41-n78 | - | - | 0.5 |
| DC_(n)41-n78 | - | - | 0.5 |
| DC_41-42_n77 | - | 0.5 | 0.5 |
| DC_41-42_n78 | - | 0.5 | 0.5 |
| DC_41-42_n79 | - | 0.5 | - |
| DC_42_n1-n3 | 0.5 | - | 0.2 |
| DC_42_n1-n77 | 0.5 | 0.2 | 0.5 |
| DC_42_n1-n78 | 0.5 | 0.2 | 0.5 |
| DC_42_n1-n79 | 0.5 | - | - |
| DC_42_n3-n28 | 0.5 | 0.2 | 0.5 |
| DC_42_n3-n77 | 0.5 | 0.2 | 0.5 |
| DC_42_n28-n77 | 0.2 | 0.5 | 0.5 |
| DC_46-48_n5 | - | 0.5 | - |
| DC_46-48_n66 | - | 0.5 | 0.3 |
| DC_48_n25-n48 | 0.4 | 0.3 | 0.4 |
| DC_48_n48-n66 | 0.4 | 0.4 | 0.3 |
| DC_46-66_n41 | - | 0.5 | 0.51 / 12 |
| DC_48-66_n2 | 0.5 | 0.3 | 0.3 |
| DC_48-66_n5 | 0.5 | 0.2 | - |
| DC_48-66_n12 | 0.5 | 0.2 | - |
| DC_48-66_n25 | 0.5 | 0.2 | 0.2 |
| DC_48-66_n48 | 0.5 | 0.2 | 0.5 |
| DC_48-66_n66 | 0.5 | 0.2 | 0.2 |
| DC_48-66_n71 | 0.5 | 0.2 | - |
| DC_48-66_n77 | 0.5 | 0.2 | 0.5 |
| DC_66_n2-n7 | 0.5 | 0.3 | 0.5 |
| DC_66_n2-n38 | 0.5 | 0.3 | 0.5 |
| DC_66_n2-n41 | 0.3 | 0.5 | 0.51 / 12 |
| DC_66_n2-n66 | 0.3 | 0.3 | 0.3 |
| DC_66_n2-n71 | 0.3 | 0.3 | - |
| DC_66_n2-n77 | 0.3 | 0.3 | 0.5 |
| DC_66_n2-n78 | 0.3 | 0.3 | 0.5 |
| DC_67-(n)3 | 0.3 | - | 0.3 |
| DC_66_n5-n48 | 0.2 | - | 0.5 |
| DC_66_n5-n77 | 0.2 | - | 0.5 |
| DC_66_n7-n12 | 0.5 | 0.5 | 0.1 |
| DC_66_n7-n25 | 0.5 | 0.3 | 0.5 |
| DC_66_n7-n66 | 0.5 | 0.5 | 0.5 |
| DC_66_n7-n71 | 0.5 | 0.5 | 0.1 |
| DC_66_n7-n77 | 0.5 | 0.5 | 0.5 |
| DC_66_n7-n78 | 0.2 | 0.5 | 0.5 |
| DC_66_n12-n77 | 0.5 | 0.5 | 0.5 |
| DC_66_n12-n78 | 0.2 | 0.2 | 0.5 |
| DC_66_n25-n41 | 0.5 | 0.5 | 0.51 / 12 |
| DC_66_n25-n48 | 0.3 | 0.3 | 0.4 |
| DC_66_n25-n66 | 0.3 | 0.3 | 0.3 |
| DC_66_n25-n71 | 0.3 | 0.5 | - |
| DC_66_n38-n66 | 0.5 | 0.5 | 0.5 |
| DC_66_n38-n71 | 0.5 | 0.5 | 0.5 |
| DC_66_n38-n78 | 0.5 | 0.5 | 0.5 |
| DC_66_n41-n66 | 0.5 | 0.5 | 0.5 |
| DC_66_n41-n71 | 0.5 | 0.51 / 12 | 0.5 |
| DC_66_n41-n77 | 0.5 | 0.51 / 12 | 0.5 |
| DC_66_n41-n78 | 0.5 | 0.51 / 12 | 0.5 |
| DC_66_n66-n77 | 0.2 | 0.2 | 0.5 |
| DC_(n)66-n78DC_66_n66-n78 | 0.2 | 0.2 | 0.5 |
| DC_66-71_n7 | 0.5 | 0.5 | 0.5 |
| DC_66-71_n38 | 0.5 | 0.5 | 0.5 |
| DC_66-71_n41 | 0.5 | 0.5 | 0.51 / 12 |
| DC_66-71_n77 | 0.2 | 0.2 | 0.5 |
| DC_66_n71-n77 | 0.2 | 0.2 | 0.5 |
| DC_66-71_n78 | 0.2 | 0.2 | 0.5 |
| DC_66_n71-n78 | 0.2 | 0.2 | 0.5 |
| DC_66-SUL_n78-n86 | 0.2 | 0.5 | - |
| DC_71_n2-n7 | 0.2 | - | - |
| DC_71_n2-n66 | - | 0.3 | 0.3 |
| DC_71_n2-n77 | 0.2 | 0.2 | 0.5 |
| DC_71_n2-n78 | 0.2 | 0.2 | 0.5 |
| DC_71_n7-n25 | - | 0.3 | - |
| DC_71_n7-n66 | 0.1 | 0.5 | 0.5 |
| DC_71_n7-n77 | 0.5 | 0.2 | 0.5 |
| DC_71_n25-n41 | - | - | 0.2 |
| DC_71_n25-n66 | 0.3 | 0.3 | 0.3 |
| DC_71_n25-n77 | 0.2 | 0.2 | 0.5 |
| DC_71_n38-n66 | 0.5 | 0.5 | 0.5 |
| DC_71_n38-n78 | 0.2 | - | 0.5 |
| DC_71_n41-n66 | 0.5 | 0.51 / 12 | 0.5 |
| DC_71_n66-n77 | 0.2 | 0.2 | 0.5 |
| DC_71_n66-n78 | 0.2 | 0.2 | 0.5 |
| NOTE 1: The requirement is applied for UE transmitting on the frequency range of 2545 – 2690 MHz.NOTE 2: The requirement is applied for UE transmitting on the frequency range of 2496 – 2545 MHz.NOTE 3: The requirement is applied for UE transmitting on the frequency range of 2515 - 2690 MHz.NOTE 4: The requirement is applied for UE transmitting on the frequency range of 2496 – 2515 MHz.NOTE 5: Only applicable for UE supporting inter-band carrier aggregation with uplink in one NR band and without simultaneous Rx/Tx.NOTE 6: This band is subject to IMD3 also which MSD is not specified.NOTE 7: “-” denotes ΔRIB,c = 0.NOTE 8: The component band order in the configuration should be listed by the order of E-UTRA band and NR band respectively, such as for DC_5_(n)12 the band order from left to right is 5, 12 and n12. |  |  |  |

##### 7.3B.3.3.3 ΔRIB,c for EN-DC four bands

Table 7.3B.3.3.3-1: ΔRIB,c due to EN-DC (four bands)

| Inter-band EN-DC configuration | ΔRIB,c for E-UTRA band / NR band (dB)11 |  |  |  |
| --- | --- | --- | --- | --- |
|  | Component band in order of bands in configuration12 |  |  |  |
| DC_1-3_n1-n41DC_1-3-3_n1-n41 | - | - | - | 03 / 0.54 |
| DC_1-(n)3-n8 | - | - | - | - |
| DC_1-3_n1-n78DC_1-3-3_n1-n78 | - | - | - | 0.5 |
| DC_1-3_n3-n41 | - | - | - | 03 / 0.54 |
| DC_1-3_n3-n77DC_1-(n)3-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-5_n28 | - | - | 0.2 | 0.2 |
| DC_1-3_n5-n40 | - | - | 0.2 | 0.8 |
| DC_1-3-5_n40 | - | - | 0.2 | 0.8 |
| DC_1-3-5_n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3_n3-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3_n3-n78DC_1-(n)3-n78 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-7_n8DC_1-3-3-7_n8DC_1-3-7-7_n8DC_1-3-3-7-7_n8 | - | - | - | 0.2 |
| DC_1-3-7_n28DC_1-3-7-7_n28 | - | - | - | 0.2 |
| DC_1-3-7_n40 | - | - | 0.3 | 0.8 |
| DC_1-3-7_n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7_n78DC_1-3-3-7_n78DC_1-3-3-7-7_n78DC_1-3-7-7_n78DC_1-1-3-3-7_n78 | 0.3 | 0.3 | 0.3 | 0.5 |
| DC_1-3_n7-n78 | 0.3 | 0.3 | 0.3 | 0.5 |
| DC_1-3-7_n105 | - | - | - | 0.3 |
| DC_1-3-8_n7 | - | - | 0.2 | - |
| DC_1-3-8_n28 | - | - | 0.2 | 0.2 |
| DC_1-3-8_n40 | - | - | 0.2 | 0.8 |
| DC_1-3-8_n41DC_1-3-3-8_n41 | - | - | - | 03 / 0.54 |
| DC_1-3-8_n71 | - | - | 0.2 | 0.2 |
| DC_1-3-8_n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1_n3-n8-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8_n3-n79 | - | - | - | 0.5 |
| DC_1-3-8_n78DC_1-3-3-8_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3_n8-n78DC_1-3-3_n8-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-11_n28 | - | 0.3 | 0.5 | 0.2 |
| DC_1-3-11_n77 | 0.2 | 0.3 | 0.5 | 0.5 |
| DC_1-3-18_n28 | - | - | - | 0.2 |
| DC_1-3-18_n41 | - | - | - | 0.26 |
| DC_1-3-28_n3 | - | - | 0.2 | - |
| DC_1-3-18_n77 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-18_n78 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-19_n78 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-20_n28 | - | - | 0.2 | 0.2 |
| DC_1-3-20_n41 | - | - | - | 01 / 0.54 |
| DC_1-3-20_n78DC_1-1-3-20_n78DC_1-3-3-20_n78 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-21_n77 | 0.2 | 0.3 | 0.5 | 0.5 |
| DC_1-3-21_n78 | 0.2 | 0.3 | 0.5 | 0.5 |
| DC_1-3-21_n79 | - | 0.3 | 0.5 | - |
| DC_1-3-26_n78 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_1-3_n26-n78 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-28_n5 | - | - | 0.2 | 0.2 |
| DC_1-3-28_n7 | - | - | 0.2 | - |
| DC_1-3-28_n38 | - | - | 0.2 | - |
| DC_1-3-28_n40 | - | - | 0.2 | - |
| DC_1-3_n28-n75 | 0.2 | - | 0.2 | - |
| DC_1-3-28_n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3_n28-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1_n3-n28-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-28_n71 | - | - | 0.7 | 0.7 |
| DC_1-3-28_n78DC_1-3-3-28_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3_n28-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-28_n79 | 0.2 | 0.2 | 0.2 | - |
| DC_1-3_n28-n79 | 0.2 | 0.2 | 0.2 | - |
| DC_1_n3-n28-n79 | 0.2 | 0.2 | 0.2 | - |
| DC_1-3-32_n28 | - | 0.5 | - | 0.5 |
| DC_1-3-32_n78 | - | - | - | 0.5 |
| DC_1-3-38_n28 | - | - | - | 0.2 |
| DC_1-3_n38-n78 | - | 0.2 | - | 0.5 |
| DC_1-3-38_n78 | 0.2 | 0.2 | 0.4 | 0.5 |
| DC_1-3-40_n28 | - | - | - | 0.2 |
| DC_1-3_n40-n71 | - | 0.2 | 0.4 | 0.3 |
| DC_1-3_n40-n77 | - | 0.2 | 0.45 | 0.55 |
| DC_1-3-40_n78 | 0.2 | 0.2 | 0.48 | 0.58 |
| DC_1-3_n40-n78 | - | 0.2 | 0.45 | 0.55 |
| DC_1-3_n40-n105 | - | 0.2 | 0.4 | 0.3 |
| DC_1-3-41_n1DC_1-3-3-41_n1 | - | - | 03 / 0.54 | - |
| DC_1-3-41_n3 | - | - | 03 / 0.54 | - |
| DC_1-3-41_n28 | - | - | 03 / 0.54 | 0.2 |
| DC_1-3-41_n41DC_1-3-3-41_n41 | - | - | 03 / 0.54 | 03 / 0.54 |
| DC_1-3_(n)41 | - | - | 03 / 0.54 | 03 / 0.54 |
| DC_1-3-41_n77 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3_n41-n77 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-41_n78DC_1-3-3-41_n78 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3_n41-n78 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-41_n79 | - | - | 03 / 0.54 | - |
| DC_1-3-42_n28 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_1-3-42_n77 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_1-3-42_n78 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_1-3-42_n79 | 0.2 | 0.2 | 0.5 | - |
| DC_1-3_n71-n77 | 0.2 | 0.2 | 0.3 | 0.5 |
| DC_1-3_n75-n78 | - | - | - | 0.5 |
| DC_1-3_n77-n79 | 0.2 | 0.2 | 0.5 | - |
| DC_1_n3-n77-n79 | 0.2 | 0.2 | 0.5 | - |
| DC_1-3_n78-n79 | 0.2 | 0.2 | 0.5 | - |
| DC_1-3_n78-n105 | 0.2 | 0.2 | 0.5 | 0.3 |
| DC_1-3_SUL_n78-n80 | 0.2 | 0.2 | 0.5 | - |
| DC_1-5-7_n28DC_1-5-7-7_n28 | - | 0.2 | - | 0.2 |
| DC_1-5-7_n40DC_1-5-7-7_n40 | - | 0.2 | 0.3 | 0.8 |
| DC_1-5-7_n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-5-7_n40DC_1-5-7-7_n40 | 0.6 | 0.6 | 0.8 | 0.9 |
| DC_1-5-7_n78DC_1-5-7-7_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-5_n28-n78 | - | 0.2 | 0.2 | 0.8 |
| DC_1-5_n40-n77 | 0.2 | 0.2 | 0.48 | 0.5 |
| DC_1-5_n40-n78 | 0.2 | 0.2 | 0.48 | 0.5 |
| DC_1-7_n3-n38 | - | - | - | 0.2 |
| DC_1-7_n3-n78 | - | - | - | 0.5 |
| DC_1-7_n5-n40 | - | 0.3 | 0.2 | 0.8 |
| DC_1-7_n7-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7-8_n7 | 0.2 | 0.2 | 0.2 | 0.2 |
| DC_1-7-8_n20 | - | - | 0.2 | 0.2 |
| DC_1-7-8_n28DC_1-7-7-8_n28 | - | - | 0.2 | 0.2 |
| DC_1-7-8_n78DC_1-7-7-8_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7_n8-n78DC_1-7-7_n8-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7-20_n28 | - | - | 0.2 | 0.2 |
| DC_1-7-20_n38 | - | - | - | 0.2 |
| DC_1-7-20_n78DC_1-1-7-20_n78DC_1-7-7-20_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7-26_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7_n26-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7-28_n3 | - | - | 0.2 | - |
| DC_1-7-28_n5 | - | - | 0.2 | 0.2 |
| DC_1-7-28_n7 | - | - | 0.2 | - |
| DC_1-7-28_n20 | - | - | 0.2 | 0.2 |
| DC_1-7-28_n38 | - | - | 0.2 | - |
| DC_1-7-28_n40 | - | 0.3 | 0.2 | 0.8 |
| DC_1-7-28_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7_n28-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7-32_n8 | - | - | - | 0.2 |
| DC_1-7-32_n28 | - | - | - | 0.2 |
| DC_1-7-32_n78 | 0.2 | 0.2 | - | 0.5 |
| DC_1-7-38_n8 | - | - | 0.2 | - |
| DC_1-7-38_n28 | - | - | 0.2 | 0.2 |
| DC_1-7-38_n78 | 0.6 | 0.6 | - | 0.8 |
| DC_1-7_n40-n77DC_1-7-7_n40-n77 | 0.2 | - | 0.4 | 0.5 |
| DC_1-7-40_n78 | 0.2 | - | 0.48 | 0.58 |
| DC_1-7_n40-n78DC_1-7-7_n40-n78 | 0.2 | - | 0.4 | 0.5 |
| DC_1-7_n40-n105 | 0.2 | - | 0.4 | 0.3 |
| DC_1-7_n75-n78 | 0.6 | 0.6 | - | 0.8 |
| DC_1-7_n78-n105 | 0.6 | 0.6 | 0.5 | 0.3 |
| DC_1-8_n1-n41 | - | 0.2 | - | - |
| DC_1-8_n1-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8_n3-n28 | - | 0.2 | - | 0.2 |
| DC_1-8_n3-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8_n3-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8_n7-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8-11_n3 | - | - | 0.3 | 0.5 |
| DC_1-8-11_n28 | - | 0.2 | - | 0.2 |
| DC_1-8-11_n77 | 0.2 | 0.2 | - | 0.5 |
| DC_1-8-11_n78 | - | 0.2 | - | 0.5 |
| DC_1-8-20_n28 | - | 0.2 | 0.2 | 0.2 |
| DC_1-8-20_n78 | - | 0.2 | - | 0.5 |
| DC_1-8-28_n3 | - | 0.2 | 0.2 | - |
| DC_1-8-28_n40 | - | 0.2 | 0.2 | 0.3 |
| DC_1-8-28_n71 | - | 0.2 | 0.7 | 0.7 |
| DC_1-8-28_n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8_n28-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8-28_n78 | - | 0.2 | 0.2 | 0.5 |
| DC_1-8_n28-n78 | - | 0.2 | 0.2 | 0.5 |
| DC_1-8_n28-n79 | 0.3 | 0.3 | 0.6 | 0.5 |
| DC_1-8-32_n3 | - | - | 0.5 | 0.3 |
| DC_1-8-32_n78 | - | 0.2 | - | 0.5 |
| DC_1-8-38_n28 |  | 0.2 |  | 0.2 |
| DC_1-8-38_n78 |  | 0.2 |  | 0.5 |
| DC_1-8-40_n28 |  | 0.2 |  | 0.2 |
| DC_1-8_n40-n77 | - | 0.2 | 0.4 | 0.5 |
| DC_1-8_n40-n78 | - | 0.2 | 0.4 | 0.5 |
| DC_1-8-40_n78 | 0.2 | 0.2 | 0.48 | 0.58 |
| DC_1-8_n40-n71 | 0.2 | 0.2 | 0.3 | 0.3 |
| DC_1-8-41_n41 | 0.2 | 0.2 | 0.2 | 0.2 |
| DC_1-8-41_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8_n41-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8-42_n3 | - | 0.2 | 0.5 | 0.2 |
| DC_1-8-42_n28 | - | 0.2 | 0.5 | 0.5 |
| DC_1-8-42_n77 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_1-8_n71-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8_n77-n79 | 0.2 | 0.2 | 0.5 | - |
| DC_1-11_n3-n28 | - | 0.3 | 0.5 | 0.2 |
| DC_1-11_n3-n77 | 0.2 | 0.3 | 0.5 | 0.5 |
| DC_1-11-18_n77 | 0.2 | - | - | 0.5 |
| DC_1-11-18_n78 | - | - | - | 0.5 |
| DC_1-11_n28-n77 | 0.2 | - | 0.2 | 0.5 |
| DC_1-18_n3-n77 | 0.2 | - | 0.2 | 0.5 |
| DC_1-18_n3-n78 | 0.2 | - | 0.2 | 0.5 |
| DC_1-11_n3-n79 | - | 0.3 | 0.5 | 0.5 |
| DC_1-11-18_n3 | - | 0.5 | - | 0.3 |
| DC_1-11-18_n28 | - | - | - | 0.1 |
| DC_1-11_n77-n79 | 0.2 | - | 0.5 | - |
| DC_1-18_n28-n41 | - | - | 0.2 | - |
| DC_1-18-28_n77 | - | - | - | 0.5 |
| DC_1-18_n28-n77 | - | - | - | 0.5 |
| DC_1-18-28_n78 | - | - | - | 0.5 |
| DC_1-18_n28-n78 | - | - | - | 0.5 |
| DC_1-18-41_n3 | - | - | 03 / 0.54 | - |
| DC_1-18-41_n77 | 0.2 | - | - | 0.5 |
| DC_1-18_n41-n77 | 0.2 | - | - | 0.5 |
| DC_1-18-41_n78 | - | - | - | 0.5 |
| DC_1-18_n41-n78 | - | - | - | 0.5 |
| DC_1-18-42_n77 | - | - | 0.5 | 0.5 |
| DC_1-18-42_n78 | - | - | 0.5 | 0.5 |
| DC_1-18-42_n79 | - | - | 0.5 | - |
| DC_1-19-42_n77 | 0.2 | - | 0.5 | 0.5 |
| DC_1-19-42_n78 | - | - | 0.5 | 0.5 |
| DC_1-19-42_n79 | - | - | 0.5 | - |
| DC_1-19_n77-n79 | 0.3 | 0.3 | 0.5 | - |
| DC_1-19_n78-n79 | 0.3 | 0.3 | 0.5 | - |
| DC_1-20_n1-n78 | - | - | - | 0.5 |
| DC_1-20_n3-n78 | - | - | - | 0.5 |
| DC_1-20_n7-n78 | - | - | - | 0.5 |
| DC_1-20_n8-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-20-28_n3 | - | 0.2 | 0.2 | - |
| DC_1-20_n28-n75 | - | 0.2 | 0.2 | - |
| DC_1-20-28_n78 | - | 0.2 | 0.2 | 0.5 |
| DC_1-20_n28-n78 | - | 0.2 | 0.2 | 0.5 |
| DC_1-20-32_n8 | 0.5 | 0.4 | - | 0.4 |
| DC_1-20-32_n28 | - | 0.2 | - | 0.2 |
| DC_1-20-32_n78 | - | - | - | 0.5 |
| DC_1-20-38_n28 | - | 0.2 | - | 0.2 |
| DC_1-20-40_n28 | - | 0.2 | - | 0.2 |
| DC_1-20-38_n78 | - | - | 0.4 | 0.5 |
| DC_1-20-40_n78 | - | - | - | 0.88 |
| DC_1-20-41-n78 | - | - | - | 0.5 |
| DC_1-20_n41-n78 | - | - | - | 0.5 |
| DC_1-21_n28-n77 | 0.2 | - | 0.2 | 0.5 |
| DC_1-21_n28-n78 | 0.2 | - | 0.2 | 0.5 |
| DC_1-21_n28-n79 | 0.3 | - | 0.3 | - |
| DC_1-21-42_n77 | 0.2 | - | 0.5 | 0.5 |
| DC_1-21-42_n78 | - | - | 0.5 | 0.5 |
| DC_1-21-42_n79 | - | - | 0.5 | - |
| DC_1-21_n77-n79 | - | - | 0.5 | - |
| DC_1-21_n78-n79 | - | - | 0.5 | - |
| DC_1-28_n3-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-28_n3-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-28_n5-n40 | - | 0.2 | 0.2 | 0.8 |
| DC_1-28-(n)7 | - | 0.2 | - | - |
| DC_1-28_n7-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-28-32_n3 | - | 0.2 | - | - |
| DC_1-28-32_n41 | - | 0.2 | - | - |
| DC_1-28_n40-n41 | - | 0.2 | 0.8 | 0.3 |
| DC_1-28_n40-n71 | 0.2 | 0.7 | 0.2 | 0.7 |
| DC_1-28_n40-n77 | - | - | - | 0.5 |
| DC_1-28-40_n78 | - | 0.2 | 0.45 | 0.55 |
| DC_1-28_n40-n78 | - | 0.2 | 0.45 | 0.55 |
| DC_1-28_n41-n77 | - | 0.2 | 0.4 | 0.5 |
| DC_1-28-42_n77 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_1-28-42_n78 | - | 0.2 | 0.5 | 0.5 |
| DC_1-28-42_n79 | - | 0.2 | 0.5 | - |
| DC_1-28_n71-n77 | 0.2 | 0.7 | 0.7 | 0.5 |
| DC_1_n28-n77-n79 | 0.3 | 0.3 | 0.5 | - |
| DC_1_n28-n78-n79 | 0.3 | 0.3 | 0.5 | - |
| DC_1-32_n28-n78 | - | - | 0.2 | 0.5 |
| DC_1-38_n3-n78 | - | - | 0.2 | 0.5 |
| DC_1-38_n7-n78 | 0.2 | - | 0.2 | 0.5 |
| DC_1-38_n28-n78 | - | - | 0.2 | 0.5 |
| DC_1_n40-n78-n105 | - | 0.4 | 0.5 | 0.3 |
| DC_1-41_n1-n41 | - | 03 / 0.54 | - | 03 / 0.54 |
| DC_1-41_n1-n78 | - | 03 / 0.54 | - | 0.5 |
| DC_1-41_n3-n41 | - | 03 / 0.54 | - | 03 / 0.54 |
| DC_1-41_n3-n77 | 0.2 | 03 / 0.54 | 0.2 | 0.5 |
| DC_1-41_n3-n78 | 0.2 | 03 / 0.54 | 0.2 | 0.5 |
| DC_1-41_n28-n41 | - | 03 / 0.54 | - | 03 / 0.54 |
| DC_1-41_n28-n77 | 0.2 | - | 0.2 | 0.5 |
| DC_1-41_n28-n78 | - | - | 0.2 | 0.5 |
| DC_1-41_n41-n77 | - | - | - | 0.5 |
| DC_1-41_n41-n78 | - | - | - | 0.5 |
| DC_1-41-42_n77 | - | - | 0.5 | 0.5 |
| DC_1-41-42_n78 | - | - | 0.5 | 0.5 |
| DC_1-41-42_n79 | - | - | 0.5 | - |
| DC_1-41-42_n79 | - | - | 0.5 | - |
| DC_1-42_n3-n28 | - | 0.5 | 0.2 | 0.5 |
| DC_1-42_n3-n77 | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_1-42_n28-n77 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_1-42_n77-n79 | 0.2 | 0.5 | 0.5 | - |
| DC_1-42_n78-n79 | 0.2 | 0.5 | 0.5 | - |
| DC_2-4-7_n28 | 0.3 | 0.5 | 0.5 | 0.2 |
| DC_2-4-7_n78 | 0.3 | 0.3 | - | 0.8 |
| DC_2-5_n2-n41 | - | 0.2 | - | - |
| DC_2-5_n2-n66 | 0.3 | - | 0.3 | 0.3 |
| DC_2-5_n2-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-5_n2-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-5_n5-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-5-7_n66  DC_2-2-5-7_n66DC_2-5-7-7_n66 | 0.3 | - | 0.5 | 0.5 |
| DC_2-5-7_n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-5-7_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-5_(n)12 | - | 0.5 | 0.3 | 0.3 |
| DC_2-12_(n)5 | - | 0.5 | 0.5 | - |
| DC_2-5-30_n2 | 0.4 | - | 0.5 | 0.4 |
| DC_2-5-30_n66 | 0.4 | - | 0.5 | 0.4 |
| DC_2-5-30_n77DC_2-2-5-30_n77 | 0.2 | 0.2 | - | 0.5 |
| DC_2-5_n41-n66 | 0.3 | 0.2 | 0.51 / 12 | 0.5 |
| DC_2-5_n41-n77 | 0.2 | 0.2 | - | 0.5 |
| DC_2-5_n41-n78 | 0.2 | 0.2 | - | 0.5 |
| DC_2-5-48_n12 | 0.2 | 0.5 | 0.5 | 0.3 |
| DC_2-5-48_n71 | 0.2 | - | 0.5 | - |
| DC_2-5-48_n77 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_2-5-66_n2 | 0.3 | - | 0.3 | 0.3 |
| DC_2-5-66_n5 | 0.3 | - | 0.3 | - |
| DC_2-5-66_n7 | 0.3 | - | 0.5 | 0.5 |
| DC_2-5-66_n12 | 0.2 | 0.5 | 0.5 | 0.3 |
| DC_2-5-66_n30DC_2-2-5-66_n30DC_2-5-66-66_n30 | 0.4 | - | 0.4 | 0.5 |
| DC_2-5-66_n41DC_2-2-5-66_n41 | 0.3 | - | 0.5 | 0.51 / 12 |
| DC_2-5-66_n48DC_2-5-66-66_n48 | 0.3 | - | 0.3 | 0.5 |
| DC_2-2-5-(n)66DC_2-2-5-66-(n)66DC_2-5-(n)66DC_2-5-66_n66DC_2-5-66-(n)66 | 0.3 | - | 0.3 | 0.3 |
| DC_2-5-66_n71 | 0.3 | - | 0.3 | - |
| DC_2-5-66_n77DC_2-2-5-66_n77DC_2-5-66-66_n77 | 0.3 | - | 0.3 | 0.5 |
| DC_2-5_n66-n77 | 0.3 | 0.2 | 0.3 | 0.5 |
| DC_2-5-66_n78 | 0.3 | 0.5 | 0.3 | 0.5 |
| DC_2-5_n66-n78 | 0.3 | - | 0.3 | 0.5 |
| DC_2-7_n2-n66 | 0.3 | 0.5 | 0.3 | 0.5 |
| DC_2-7_n2-n71 | - | - | - | 0.2 |
| DC_2-7_n2-n77 | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_2-7_n2-n78 | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_2-7-12_n66 DC_2-2-7-12_n66 | 0.3 | 0.5 | 0.5 | 0.3 |
| DC_2-7-12_n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-7_n12-n77 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_2-7-12_n78 DC_2-2-7-12_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-7-13_n66DC_2-7-7-13_n66 DC_2-2-7-7-13_n66 | 0.3 | 0.5 | - | 0.5 |
| DC_2-7_n25-n66 | 0.3 | 0.5 | 0.3 | 0.5 |
| DC_2-7-28_n66 | 0.3 | 0.5 | 0.2 | 0.5 |
| DC_2-7-28_n78 | 0.3 | 0.5 | 0.2 | 0.5 |
| DC_2-7-29_n78DC_2-7-7-29_n78 | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_2-7_n38-n66DC_2-7-7_n38-n66 | 0.3 | - | - | 0.5 |
| DC_2-7-38_n78 | 0.2 | - | - | 0.5 |
| DC_2-7_n38-n78DC_2-7-7_n38-n78 | 0.2 | - | - | 0.5 |
| DC_2-7-66_n2 | 0.3 | 0.5 | 0.5 | 0.3 |
| DC_2-7-66_n7DC_2-7-66-66_n7 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_2-7-66_n12 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_2-7-66_n25 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_2-7-66_n28 | 0.3 | 0.5 | 0.5 | 0.2 |
| DC_2-7-66_n38DC_2-2-7-66_n38 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_2-7-(n)66DC_2-7-66_n66DC_2-7-7-(n)66DC_2-7-7-66_n66DC_2-7-7-66-(n)66DC_2-7-66-(n)66 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_2-7-66_n71 DC_2-2-7-66_n71 | 0.3 | 0.5 | 0.5 | - |
| DC_2-7_n66-n71 | 0.3 | 0.5 | 0.5 | - |
| DC_2-7-66_n77 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_2-7_n66-n77 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_2-7-66_n78  DC_2-2-7-66_n78DC_2-7-7-66_n78DC_2-7-66-66_n78DC_2-7-7-66-66_n78 | 0.3 | - | 0.3 | 0.5 |
| DC_2-7_n66-n78DC_2-7-7_n66-n78 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_2-7-71_n2 | - | - | 0.2 | - |
| DC_2-7-71_n66 DC_2-2-7-71_n66 | 0.3 | 0.5 | - | 0.3 |
| DC_2-7-71_n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-7_n71-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-7-71_n78 DC_2-2-7 -71_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-7_n71-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-12_n2-n66 | 0.3 | 0.5 | 0.3 | 0.3 |
| DC_2-12_n2-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-12_n2-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-12-30_n2 | 0.4 | - | 0.5 | 0.4 |
| DC_2-12-30_n66 | 0.4 | 0.5 | 0.5 | 0.4 |
| DC_2-12-30_n77DC_2-2-12-30_n77 | 0.2 | 0.2 | - | 0.5 |
| DC_2-12_n41-n66 | 0.3 | 0.5 | 0.5 | 0.3 |
| DC_2-12-48_n5 | 0.3 | 0.3 | 0.5 | 0.5 |
| DC_2-12-66_n2 | 0.3 | 0.5 | 0.3 | 0.3 |
| DC_2-12-66_n5 | 0.3 | 0.5 | 0.5 | 0.3 |
| DC_2-12-66_n7 | 0.3 | 0.5 | 0.3 | 0.3 |
| DC_2-12-66_n30DC_2-2-12-66_n30DC_2-12-66-66_n30 | 0.4 | 0.5 | 0.4 | 0.5 |
| DC_2-12-66_n41 DC_2-2-12-66_n41 | 0.5 | 0.8 | 0.5 | 0.5 |
| DC_2-2-12-(n)66DC_2-12-(n)66DC_2-12-66_n66 | 0.3 | 0.5 | 0.3 | 0.3 |
| DC_2-12-66_n77DC_2-2-12-66_n77DC_2-12-66-66_n77 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_2-12_n66-n77 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_2-12-66_n78 DC_2-2-12-66_n78 | 0.3 | - | 0.3 | 0.5 |
| DC_2-12_n66-n78 | 0.3 | - | 0.3 | 0.5 |
| DC_2-13_n2-n77 | 0.2 | - | 0.2 | 0.5 |
| DC_2-13_n5-n77DC_2-2-13_n5-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-13_n25-n66 | 0.3 | - | 0.3 | 0.3 |
| DC_2-13-48_n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-13-66_n2 | 0.3 | - | 0.3 | 0.3 |
| DC_2-13-66_n5 | 0.3 | - | 0.3 | - |
| DC_2-13-66_n48 | 0.3 | - | 0.3 | 0.5 |
| DC_2-2-13-(n)66DC_2-2-13-66-(n)66DC_2-13-(n)66DC_2-13-66_n66DC_2-13-66-(n)66 | 0.3 | - | 0.3 | 0.3 |
| DC_2-13-66_n77DC_2-2-13-66_n77DC_2-2-13-66-66_n77DC_2-13-66-66_n77 | 0.3 | - | 0.3 | 0.5 |
| DC_2-13_n66-n77 | 0.3 | - | 0.3 | 0.5 |
| DC_2-14-30_n2 | 0.3 | - | 0.3 | 0.3 |
| DC_2-14-30_n66 | 0.4 | - | 0.5 | 0.4 |
| DC_2-14-30_n77DC_2-2-14-30_n77 | 0.2 | 0.2 | - | 0.5 |
| DC_2-14-66_n2DC_2-14-66-66_n2 | 0.3 | - | 0.3 | 0.3 |
| DC_2-14-66_n30DC_2-2-14-66_n30DC_2-14-66-66_n30 | 0.4 | - | 0.4 | 0.5 |
| DC_2-14-66_n66DC_2-2-14-66_n66 | 0.3 | - | 0.3 | 0.3 |
| DC_2-14-66_n77DC_2-2-14-66_n77DC_2-14-66-66_n77 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_2-28-66_n7 | 0.3 | 0.2 | 0.5 | 0.5 |
| DC_2-28-66_n66 | 0.3 | 0.2 | 0.3 | 0.3 |
| DC_2-29-30_n2 | 0.4 | - | 0.5 | 0.4 |
| DC_2-29-30_n66 | 0.4 | - | 0.5 | 0.4 |
| DC_2-29-30_n77DC_2-2-29-30_n77 | 0.2 | 0.2 | - | 0.5 |
| DC_2-29-66_n2DC_2-29-66-66_n2 | 0.3 | - | 0.3 | 0.3 |
| DC_2-29-66_n30DC_2-2-29-66_n30DC_2-29-66-66_n30 | 0.4 | - | 0.4 | 0.5 |
| DC_2-29-(n)66DC_2-2-29-(n)66DC_2-29-66_n66 | 0.3 | - | 0.3 | 0.3 |
| DC_2-29-66_n77 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_2-29-66_n78 | 0.3 | - | 0.3 | 0.5 |
| DC_2-30-(n)5DC_2-2-30-(n)5 | 0.4 | - | 0.5 | - |
| DC_2-30-66_n2DC_2-30-66-66_n2 | 0.4 | 0.5 | 0.4 | 0.4 |
| DC_2-30-66_n5 | 0.4 | 0.5 | 0.4 | - |
| DC_2-30-66_n66 | 0.4 | 0.5 | 0.4 | 0.4 |
| DC_2-30-66_n77DC_2-2-30-66_n77DC_2-30-66-66_n77 | 0.2 | 0.5 | 0.4 | 0.5 |
| DC_2-46_n41-n66 | 0.3 | - | 0.5 | 0.5 |
| DC_2-46_n41-n71 | - | - | - | 0.2 |
| DC_2-46-48_n2 | 0.3 | - | 0.5 | 0.3 |
| DC_2-46-48_n5 | 0.2 | - | 0.5 | - |
| DC_2-46-48_n66 | 0.3 | - | 0.5 | 0.3 |
| DC_2-46-66_n5 | 0.3 | - | 0.3 | - |
| DC_2-46-66_n41 | 0.3 | - | 0.5 | 0.51 / 12 |
| DC_2-48_(n)5 | 0.2 | - | 0.5 | - |
| DC_2-48_n48-n66 | 0.3 | 0.4 | 0.4 | 0.3 |
| DC_2-48-66_n2 | 0.3 | 0.5 | 0.3 | 0.3 |
| DC_2-48-66_n5 | 0.3 | 0.5 | 0.3 | - |
| DC_2-48-66_n12 | 0.3 | 0.5 | 0.3 | - |
| DC_2-48-66_n66 | 0.3 | 0.5 | 0.3 | 0.3 |
| DC_2-48-66_n71 | 0.3 | 0.5 | 0.3 | - |
| DC_2-48-66_n77 | 0.3 | 0.5 | 0.3 | 0.5 |
| DC_2-66_n2-n41 | 0.3 | 0.5 | 0.3 | 0.5 |
| DC_2-66_n2-n66 | 0.3 | 0.3 | 0.3 | 0.3 |
| DC_2-66_n2-n71 | 0.3 | 0.3 | 0.3 | - |
| DC_2-66_n2-n77DC_2-66-66_n2-n77 | 0.2 | 0.3 | 0.3 | 0.5 |
| DC_2-66_n2-n78 | 0.3 | 0.3 | 0.3 | 0.5 |
| DC_2-66_(n)5DC_2-2-66_(n)5DC_2-66-66_(n)5 | 0.3 | - | 0.3 | - |
| DC_2-66_n5-n77 | 0.3 | 0.3 | - | 0.5 |
| DC_2-66_n12-n77 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_2-66_n12-n78 | 0.3 | 0.3 | - | 0.5 |
| DC_2-66_n25-n66 | 0.3 | 0.3 | 0.3 | 0.3 |
| DC_2-66_n38-n78 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-66_n41-n66 | 0.3 | 0.5 | 0.51 / 12 | 0.5 |
| DC_2-66_n41-n71 | 0.3 | 0.3 | 0.51 / 12 | 0.5 |
| DC_2-66_n41-n77 | 0.6 | 0.6 | 0.51 / 12 | 0.8 |
| DC_2-66_n41-n78 | 0.6 | 0.6 | 0.51 / 12 | 0.8 |
| DC_2-66_n66-n71 | 0.3 | 0.3 | 0.3 | - |
| DC_2-66-71_n38DC_2-2-66-71_n38 | 0.3 | 0.5 | - | 0.5 |
| DC_2-66-71_n41 DC_2-2-66-71_n41 | 0.3 | 0.3 | 0.5 | 0.51 / 12 |
| DC_2-66-71_n66 | 0.3 | 0.3 | - | 0.3 |
| DC_2-66-(n)71 | 0.3 | 0.3 | - | - |
| DC_2-66-71_n71 | 0.3 | 0.3 | - | - |
| DC_2-66-71_n77 | 0.3 | 0.3 | 0.2 | 0.5 |
| DC_2-66_n71-n77 | 0.3 | 0.3 | 0.2 | 0.5 |
| DC_2-66-71_n78DC_2-2-66-71_n78 | 0.3 | 0.5 | - | 0.5 |
| DC_2-66_n71-n78 | 0.3 | 0.5 | - | 0.5 |
| DC_2-66_n66-n77 | 0.3 | 0.3 | 0.3 | 0.5 |
| DC_2-(n)66-n78DC_2-66_n66-n78 | 0.3 | 0.3 | 0.3 | 0.5 |
| DC_2-66-71_n2 | 0.3 | 0.3 | - | 0.3 |
| DC_2-71_n2-n41 | - | 0.2 | - | - |
| DC_2-71_n2-n66 | 0.3 | - | 0.3 | 0.3 |
| DC_2-71_n2-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-71_n2-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-71_n41-n66 | 0.3 | 0.5 | 0.51 / 12 | 0.3 |
| DC_2-71_n66-n77 | 0.3 | - | 0.5 | 0.5 |
| DC_2-71_n66-n78 | 0.3 | - | 0.5 | 0.5 |
| DC_3_n1-n20-n78DC_3-3_n1-n20-n78 | 0.2 | 0.2 | - | 0.5 |
| DC_3_n1-n28-n75 | 0.3 | 0.3 | 0.7 | - |
| DC_3_n1-n75-n78 | 0.6 | 0.6 | - | 0.8 |
| DC_3_n1-n40-n78 | 0.2 | 0.2 | 0.48 | 0.5 |
| DC_3_n1-n77-n79 | 0.2 | 0.2 | 0.5 | - |
| DC_3_n1-n78-n79 | 0.2 | 0.2 | 0.5 | - |
| DC_3-5_n1-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-5-7_n28DC_3-5-7-7_n28 | - | 0.2 | - | 0.2 |
| DC_3-5-7_n40DC_3-5-7-7_n40 | - | 0.2 | 0.3 | 0.8 |
| DC_3-5-7_n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-5-7_n78DC_3-5-7-7_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-5_n28-n78 | 0.2 | 0.2 | 0.2 | 0.8 |
| DC_3-5_n40-n77 | 0.2 | 0.2 | 0.48 | 0.5 |
| DC_3-5_n40-n78 | 0.2 | 0.2 | 0.48 | 0.5 |
| DC_3_n5-n40-n78 | 0.2 | 0.2 | 0.48 | 0.5 |
| DC_3-5-41_n79 | - | - | 03 / 0.54 | - |
| DC_3-7_n1-n8DC_3-3-7_n1-n8DC_3-7-7_n1-n8DC_3-3-7-7_n1-n8 | - | - | - | 0.2 |
| DC_3-7_n1-n28 | - | - | - | 0.2 |
| DC_3-7_n1-n40 | - | 0.3 | - | 0.8 |
| DC_3-7_n1-n78 | 0.3 | 0.3 | 0.3 | 0.5 |
| DC_3-7_n3-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7_n5-n40 | - | 0.3 | 0.2 | 0.8 |
| DC_3-7-7_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-8_n1DC_3-3-7-8_n1DC_3-7-7-8_n1DC_3-3-7-7-8_n1 | - | - | 0.2 | - |
| DC_3-7-8_n7 | - | - | 0.2 | - |
| DC_3-7-8_n28DC_3-7-7-8_n28 | - | - | 0.2 | 0.1 |
| DC_3-7-8_n40 | - | - | 0.2 | 0.5 |
| DC_3-7-8_n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-8_n78DC_3-3-7-8_n78DC_3-7-7-8_n78DC_3-3-7-7-8_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7_n8-n78,DC_3-3-7_n8-n78, DC_3-7-7_n8-n78, DC_3-3-7-7_n8-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7_n7-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-20_n28 | - | - | 0.2 | 0.1 |
| DC_3-7-20_n38 | - | - | - | 0.2 |
| DC_3-7-20_n78DC_3-3-7-20_n78DC_3-7-7-20_n78 | 0.2 | 0.2 | - | 0.5 |
| DC_3-7_n26-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-26_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-28_n1DC_3-7-7-28_n1 | - | - | 0.2 | - |
| DC_3-7-28_n40 | - | 0.3 | - | 0.8 |
| DC_3-7-28_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7_n28-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-32_n28 | 0.5 | - | - | 0.5 |
| DC_3-7-32_n78 | 0.2 | 0.2 | - | 0.5 |
| DC_3-7-38_n28 | - | - | 0.2 | 0.2 |
| DC_3-7-38_n78 | 0.2 | - | - | 0.5 |
| DC_3-7-40_n1 | - | 0.3 | 0.8 | - |
| DC_3-7_n40-n77DC_3-7-7_n40-n77 | 0.2 | - | 0.48 | 0.58 |
| DC_3-7_n40-n78DC_3-7-7_n40-n78 | 0.2 | - | 0.48 | 0.58 |
| DC_3-7_n40-n105 | 0.2 | - | 0.4 | 0.3 |
| DC_3-7_n75-n78 | 0.2 | 0.2 | - | 0.5 |
| DC_3-7_n78-n79DC_3-3-7_n78-n79DC_3-7-7_n78-n79DC_3-3-7-7_n78-n79 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_3-7_n78-n105 | 0.2 | 0.2 | 0.5 | 0.3 |
| DC_3-7_SUL_n78-n80 | 0.2 | 0.2 | 0.5 | - |
| DC_3-8_n71-n77 | 0.6 | 0.3 | 0.2 | 0.8 |
| DC_3-8_n77-n79 | 0.6 | 0.3 | 0.8 | - |
| DC_3-8_n1-n28 | - | 0.2 | - | 0.2 |
| DC_3-8_n1-n40 | - | - | 0.1 | 0.2 |
| DC_3-8_n1-n41DC_3-3-8_n1-n41 | - | - | 0.2 | - |
| DC_3-8_n1-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-8_n1-n78DC_3-3-8_n1-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-8_n7-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-8-11_n28 | 0.3 | 0.2 | 0.5 | 0.2 |
| DC_3-8-11_n77 | 0.3 | 0.2 | 0.5 | 0.5 |
| DC_3-8-20_n28 | - | 0.2 | 0.1 | 0.1 |
| DC_3-8-20_n78 | 0.2 | 0.2 | - | 0.5 |
| DC_3-8-28_n40 | - | - | 0.2 | 0.8 |
| DC_3-8-28_n71 | - | 0.2 | 0.7 | 0.7 |
| DC_3-8-28_n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-8_n28-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-8-28_n1 | - | 0.2 | 0.2 | - |
| DC_3-8-28_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-8_n28-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-8-32_n1 | - | - | 0.5 | 0.3 |
| DC_3-8-32_n28 | - | - | - | 0.2 |
| DC_3-8-32_n78 | 0.3 | 0.2 | 0.5 | 0.5 |
| DC_3-8-38_n1 | - | - | 0.2 | - |
| DC_3-8-38_n28 | - | - | 0.2 | - |
| DC_3-8-38_n78 | - | - | 0.2 | 0.5 |
| DC_3-8-40_n28 | - | - | 0.2 | - |
| DC_3-8_n40-n41 | - | - | - | 03/0.54 |
| DC_3-8-40_n1 | - | - | 0.2 | 0.1 |
| DC_3-8_n40-n71 | 0.2 | 0.2 | 0.3 | 0.3 |
| DC_3-8_n40-n77 | 0.2 | 0.2 | 0.4 | 0.5 |
| DC_3-8-40_n78 | 0.2 | 0.2 | 0.48 | 0.58 |
| DC_3-8_n40-n78 | 0.2 | 0.2 | 0.4 | 0.5 |
| DC_3-8-41_n1DC_3-3-8-41_n1 | - | 0.2 | - | - |
| DC_3-8-41_n41DC_3-3-8-41_n41 | - | - | 03/0.54 | 03/0.54 |
| DC_3-8-41_n78DC_3-3-8-41_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-8_n41-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-8_n41-n79 | 0.2 | - | 03/0.54 | - |
| DC_3-8-42_n77 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_(n)3-n8-n77 | 0.6 | 0.6 | 0.3 | 0.8 |
| DC_3-8_SUL_n78-n80 | 0.2 | 0.2 | 0.5 | - |
| DC_3-11_n28-n77 | 0.3 | 0.5 | 0.2 | 0.5 |
| DC_3-18_n3-n41 | 0.2 | - | 0.2 | - |
| DC_3-18_n3-n77 | 0.2 | - | 0.2 | 0.5 |
| DC_3-18_n3-n78 | 0.2 | - | 0.2 | 0.5 |
| DC_3-18_n28-n41 | 0.2 | - | 0.2 | - |
| DC_3-18_n28-n77 | 0.2 | - | 0.2 | 0.5 |
| DC_3-18_n28-n78 | 0.2 | - | 0.2 | 0.5 |
| DC_3-18_n41-n77 | 0.2 | - | - | 0.5 |
| DC_3-18_n41-n78 | 0.2 | - | - | 0.5 |
| DC_3-18-42_n77 | - | - | 0.5 | 0.5 |
| DC_3-18-42_n78 | - | - | 0.5 | 0.5 |
| DC_3-18-42_n79 | 0.2 | - | 0.5 | - |
| DC_3-19_n1-n77 | 0.2 | - | 0.2 | 0.5 |
| DC_3-19_n1-n78 | 0.2 | - | 0.2 | 0.5 |
| DC_3-19-21_n77 | 0.3 | - | 0.5 | 0.5 |
| DC_3-19-21_n78 | 0.3 | - | 0.5 | 0.5 |
| DC_3-19-21_n79 | 0.3 | - | 0.5 | - |
| DC_3-19-42_n1 | 0.2 | - | 0.5 | 0.2 |
| DC_3-19-42_n77 | 0.2 | - | 0.5 | 0.5 |
| DC_3-19-42_n78 | 0.2 | - | 0.5 | 0.5 |
| DC_3-19-42_n79 | 0.2 | - | 0.5 | - |
| DC_3-19_n77-n79 | 0.2 | - | 0.5 | - |
| DC_3-19_n78-n79 | 0.2 | - | 0.5 | - |
| DC_3-20_n1-n28 | - | - | 0.2 | 0.2 |
| DC_3-20_n1-n41DC_3-3-20_n1-n41 | - | - | - | 03 / 0.54 |
| DC_3-20_n1-n78 | 0.2 | - | 0.2 | 0.5 |
| DC_3-20_n7-n28 | - | 0.1 | - | 0.1 |
| DC_3-20_n3-n67 | - | 0.1 | - | 0.1 |
| DC_3-20_n8-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-20-28_n1 | - | 0.2 | 0.2 | - |
| DC_3-20-28_n7 | - | 0.2 | 0.2 | - |
| DC_3-20_n28-n75 | 0.5 | - | 0.5 | - |
| DC_3-20-28_n78DC_3-3-20-28_n78 | 0.2 | 0.1 | 0.2 | 0.5 |
| DC_3-20_n28-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-20-32_n28 | 0.5 | - | - | 0.5 |
| DC_3-20-32_n78 | 0.2 | - | - | 0.5 |
| DC_3-20-38_n1 | 0.2 | - | 0.2 | 0.5 |
| DC_3-20-38_n28 | 0.2 | - | 0.2 | 0.2 |
| DC_3-20-38_n78 | 0.2 | 0.2 | 0.4 | 0.5 |
| DC_3-20_n38-n78 | 0.2 | 0.2 | 0.4 | 0.5 |
| DC_3-20-40_n1 | 0.2 | - | 0.2 | 0.5 |
| DC_3-20-40_n28 | 0.2 | - | 0.2 | 0.2 |
| DC_3-20-40_n78 | 0.2 | 0.2 | 0.45 | 0.55 |
| DC_3-20-41_n1DC_3-3-20-41_n1 | 0.2 | - | 0.2 | 0.5 |
| DC_3-20-41_n78DC_3-3-20-41_n78DC_3-20_n41-n78 | - | - | - | 0.5 |
| DC_3-20-67_n3 | - | 0.1 | 0.1 | - |
| DC_3_20_SUL_n78-n80 | 0.2 | - | 0.5 | - |
| DC_3-21_n1-n77 | 0.3 | 0.5 | 0.2 | 0.5 |
| DC_3-21_n1-n78 | 0.3 | 0.5 | 0.2 | 0.5 |
| DC_3-21_n1-n79 | 0.3 | 0.5 | - | - |
| DC_3-21_n28-n77 | 0.3 | 0.5 | 0.2 | 0.5 |
| DC_3-21_n28-n78 | 0.3 | 0.5 | 0.2 | 0.5 |
| DC_3-21_n28-n79 | 0.3 | 0.5 | 0.3 | - |
| DC_3-21-42_n1 | 0.3 | 0.5 | 0.5 | 0.2 |
| DC_3-21-42_n77 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_3-21-42_n78 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_3-21-42_n79 | 0.3 | 0.5 | 0.5 | - |
| DC_3-21_n77-n79 | 0.3 | 0.5 | 0.5 | - |
| DC_3-21_n78-n79 | 0.3 | 0.5 | 0.5 | - |
| DC_3-28_n1-n5 | 0.3 | 0.6 | 0.3 | 0.6 |
| DC_3-28_n1-n40 | - | 0.2 | - | - |
| DC_3-28_n1-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-28_n1-n105 | 0.3 | 1 | 0.3 | 1 |
| DC_3-28_n3-n78 | - | 0.2 | - | 0.5 |
| DC_3-28_n5-n40 | - | 0.2 | 0.2 | 0.8 |
| DC_3-28_n5-n105 | 0.3 | 1 | 0.6 | 1 |
| DC_3-28_n7-n78DC_3-3-28_n7-n78 | 0.5 | 0.2 | 0.4 | 0.5 |
| DC_3-28-32_n1 | 0.5 | 0.5 | - | - |
| DC_3-28-38_n1 | - | 0.2 | - | - |
| DC_3-28-40_n1 | - | 0.2 | - | - |
| DC_3-28_n40-n71 | 0.2 | 0.7 | 0.2 | 0.7 |
| DC_3-28_n40-n77 | - | - | - | 0.5 |
| DC_3-28-40_n78 | 0.2 | 0.2 | 0.45 | 0.55 |
| DC_3-28_n40-n78 | 0.2 | 0.2 | 0.45 | 0.55 |
| DC_3-28_n41-n77 | 0.5 | 0.2 | 0.43 / 0.54 | 0.5 |
| DC_3-28-41_n78 | 0.5 | 0.2 | 0.43 / 0.54 | 0.5 |
| DC_3-28-42_n77 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_3-28-42_n78 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_3-28-42_n79 | 0.2 | 0.2 | 0.5 | - |
| DC_3-28_n71-n77 | 0.2 | 0.7 | 0.7 | 0.5 |
| DC_3_n28-n77-n79 | 0.2 | 0.2 | 0.5 | - |
| DC_3_n28-n78-n79 | 0.2 | 0.2 | 0.5 | - |
| DC_3-28_n78-n105 | 0.2 | 0.7 | 0.5 | 0.7 |
| DC_3-32_n1-n28 | - | - | 0.2 | 0.2 |
| DC_3-32_n1-n78 | - | - | - | 0.5 |
| DC_3-32-38_n28 | - | - | - | 0.2 |
| DC_3-32_n28-n78 | 0.2 | - | 0.2 | 0.5 |
| DC_3-32-38_n28 | - | - | - | 0.2 |
| DC_3-38_n7-n78 | 0.6 | N/A | N/A | 0.8 |
| DC_3-38_n28-n78 | 0.5 | 0.4 | 0.2 | 0.5 |
| DC_3-38-40_n1 | - | 0.4 | 0.5 | - |
| DC_3-38-40_n28 | - | 0.4 | 0.5 | 0.2 |
| DC_3-40_n1-n78 | 0.2 | 0.45 | - | 0.55 |
| DC_3_n40-n41-n79 | - | - | 03/0.54 | 0.5 |
| DC_3_n40-n78-n105 | - | 0.4 | 0.8 | 0.3 |
| DC_3-41_n1-n41DC_3-3-41_n1-n41 | - | 03 / 0.54 | - | 03 / 0.54 |
| DC_3-41_n1-n78DC_3-3-41_n1-n78 | 0.2 | - | 0.2 | 0.5 |
| DC_3-41_n3-n41 | - | 03 / 0.54 | - | 03 / 0.54 |
| DC_3-41_n3-n77 | 0.2 | 03 / 0.54 | 0.2 | 0.5 |
| DC_3-41_n3-n78 | 0.2 | 03 / 0.54 | 0.2 | 0.5 |
| DC_3-41_n28-n41 | 0.2 | 03 / 0.54 | 0.2 | 03 / 0.54 |
| DC_3-41_n28-n77 | 0.2 | 03 / 0.54 | 0.2 | 0.5 |
| DC_3-41_n28-n78 | 0.5 | 0.43 / 0.54 | 0.2 | 0.5 |
| DC_3-41_n41-n77 | 0.2 | 03 / 0.54 | 03 / 0.54 | 0.5 |
| DC_3-41_n41-n78 | 0.2 | 03 / 0.54 | 03 / 0.54 | 0.5 |
| DC_3-41-42_n77 | 0.5 | 03 / 0.54 | 0.5 | 0.5 |
| DC_3-41-42_n78 | 0.5 | 03 / 0.54 | 0.5 | 0.5 |
| DC_3-41-42_n79 | 0.5 | 03 / 0.54 | 0.5 | - |
| DC_3-42_n1-n77 | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_3-42_n1-n78 | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_3-42_n1-n79 | 0.2 | 0.5 | 0.2 | - |
| DC_3-42_n28-n77 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_3-42_n77-n79 | 0.2 | 0.5 | 0.5 | - |
| DC_3-42_n78-n79 | 0.2 | 0.5 | 0.5 | - |
| DC_5-7_n1-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_5-7_n2-n66 | - | 0.5 | 0.3 | 0.5 |
| DC_5-7_n2-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_5-7_n2-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_5-7-7_n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_5-7_n28-n78 | 0.2 | - | 0.2 | 0.8 |
| DC_5-7_n40-n77DC_5-7-7_n40-n77 | 0.2 | - | 0.4 | 0.5 |
| DC_5-7_n40-n78DC_5-7-7_n40-n78 | 0.2 | - | 0.4 | 0.5 |
| DC_5-7-66_n2 | - | 0.5 | 0.5 | 0.3 |
| DC_5-7-66_n7DC_5-7-66-66_n7 | - | 0.5 | 0.5 | 0.5 |
| DC_5-7-(n)66DC_5-7-7-(n)66DC_5-7-66_n66 DC_5-7-7-66_n66 | 0.3 | - | 0.3 | 0.3 |
| DC_5-7-66_n77 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_5-7_n66-n77 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_5-7_n66-n78 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_5-7-66_n78 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_5-30-66_n2 | - | 0.5 | 0.4 | 0.4 |
| DC_5-30-66_n66 | - | 0.5 | 0.4 | 0.4 |
| DC_5-30-66_n77DC_5-30-66-66_n77 | 0.2 | 0.5 | 0.4 | 0.5 |
| DC_5-48_(n)12 | 0.5 | 0.3 | - | 0.5 |
| DC_5-48-66_n12 | 0.5 | 0.5 | 0.2 | 0.3 |
| DC_5-48-66_n71 | - | 0.5 | 0.2 | - |
| DC_5-48-66_n77 | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_5-66_n2-n41 | 0.2 | 0.3 | 0.5 | 0.51 / 12 |
| DC_5-66_n2-n66 | - | 0.3 | 0.3 | 0.3 |
| DC_5-66_n2-n77DC_5-66-66_n2-n77 | 0.2 | 0.3 | 0.3 | 0.5 |
| DC_5-66_n2-n78 | - | 0.3 | 0.3 | 0.5 |
| DC_5-66_n5-n77DC_5-66-66_n5-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_5-66_(n)12 | - | 0.5 | 0.5 | 0.5 |
| DC_5-66_n41-n66 | 0.6 | 0.5 | 0.81 / 1.32 | 0.5 |
| DC_5-66_n41-n77 | 0.6 | 0.5 | 0.81 / 1.32 | 0.8 |
| DC_5-66_n41-n78 | 0.6 | 0.5 | 0.81 / 1.32 | 0.8 |
| DC_5-66_n66-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_7_n1-n75-n78 | 0.2 | 0.2 | - | 0.5 |
| DC_7-8_n1-n78 | 0.3 | 0.2 | - | 0.8 |
| DC_7_n1-n8-n78 | 0.3 | - | 0.2 | 0.8 |
| DC_7-8_n1-n78DC_7-7-8_n1-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_7-8_n7-n78 | - | 0.2 | - | 0.5 |
| DC_7-8-20_n1 | - | 0.2 | 0.2 | - |
| DC_7-8-20_n3 | - | 0.2 | - | - |
| DC_7-8_n28-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_7-8-32_n1 | - | 0.2 | - | - |
| DC_7-8-32_n78 | - | 0.2 | - | 0.5 |
| DC_7-8-38_n1 | - | - | 0.2 | - |
| DC_7-8-40_n1 | 0.3 | 0.2 | 0.8 | - |
| DC_7-8-40_n78 | - | 0.2 | 0.48 | 0.58 |
| DC_7-8_n40-n78 | - | 0.2 | 0.4 | 0.5 |
| DC_7-12_n2-n66 | 0.5 | 0.5 | 0.3 | 0.3 |
| DC_7-12_n2-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_7-12_n2-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_7-12-66_n2 | 0.5 | 0.5 | 0.3 | 0.3 |
| DC_7-12-66_n25 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_7-12-66_n66 | 0.5 | - | 0.5 | 0.5 |
| DC_7-12-66_n77 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_7-12_n66-n77 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_7-12-66_n78 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_7-12_n66-n78 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_7-12-71_n77 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_7-13_n25-n66 | 0.5 | - | 0.3 | 0.5 |
| DC_7-7-13-(n)66DC_7-13-(n)66DC_7-13-66_n66 | 0.5 | - | 0.5 | 0.5 |
| DC_7-20_n1-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_7-20_n3-n38 | - | 0.2 | - | 0.2 |
| DC_7-20_n3-n78 | - | - | - | 0.5 |
| DC_7-20_n8-n78 | - | 0.2 | 0.2 | 0.5 |
| DC_7-20-28_n1 | - | 0.2 | 0.2 | - |
| DC_7-20-28_n3 | - | 0.2 | 0.1 | - |
| DC_7-20-28_n78 | 0.3 | 0.6 | 0.6 | 0.8 |
| DC_7-20_n28-n78 | - | 0.2 | 0.2 | 0.5 |
| DC_7-20-32_n8 | - | 0.2 | - | 0.2 |
| DC_7-20-32_n28 | - | - | - | 0.2 |
| DC_7-20-32_n78 | - | - | - | 0.5 |
| DC_7-20-38_n3 | - | - | 0.2 | - |
| DC_7-20-38_n8 | - | 0.2 | 0.2 | 0.2 |
| DC_7-20-38_n78 | - | - | 0.4 | 0.6 |
| DC_7-28_n1-n40 | 0.3 | 0.2 | - | 0.8 |
| DC_7-28_n3-n78 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_7-28_n5-n40 | 0.3 | 0.2 | 0.2 | 0.8 |
| DC_7-28_n7-n78 | - | - | - | 0.5 |
| DC_7-28-32_n1 | - | 0.2 | - | - |
| DC_7-28-38_n1 | - | 0.2 | 0.2 | - |
| DC_7-28-38_n78 | - | 0.2 | 0.4 | 0.5 |
| DC_7-28_n38-n78 | - | 0.2 | 0.4 | 0.5 |
| DC_7-28_n40-n78 | - | 0.2 | 0.4 | 0.5 |
| DC_7-29-66_n78 | 0.5 | - | 0.5 | 0.5 |
| DC_7-32_n1-n28 | - | - | - | 0.2 |
| DC_7-32_n1-n78 | 0.6 | - | 0.6 | 0.8 |
| DC_7-32_n28-n78 | - | - | 0.2 | 0.5 |
| DC_7-38_n3-n78 | 0.5 | 0.5 | 0.2 | 0.5 |
| DC_7_n40-n78-n105 | - | 0.4 | 0.8 | 0.3 |
| DC_7-66_n38-n78DC_7-7-66_n38-n78 | - | 0.2 | - | 0.5 |
| DC_7-28_n1-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_7-28-66_n7 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_7-28-66_n66 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_7-40_n1-n78 | - | 0.45 | 0.2 | 0.55 |
| DC_7-66_n2-n66 | 0.5 | 0.3 | 0.3 | 0.5 |
| DC_7-66_n2-n71 | 0.5 | 0.5 | 0.3 | 0.2 |
| DC_7-66_n2-n77 | - | 0.3 | 0.3 | 0.5 |
| DC_7-66_n2-n78 | - | 0.3 | 0.3 | 0.5 |
| DC_7-66_n12-n77 | 0.5 | 0.5 | 0.2 | 0.5 |
| DC_7-66_n12-n77 | 0.5 | 0.5 | 0.2 | 0.5 |
| DC_7-66_n25-n66 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_7-66_n66-n71 | 0.5 | 0.5 | 0.5 | 0.1 |
| DC_7-66_n66-n77 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_7-(n)66-n78DC_7-7-(n)66-n78DC_7-66_n66-n78DC_7-7-66_n66-n78 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_7-66-71_n2 | 0.5 | 0.5 | - | 0.3 |
| DC_7-66-71_n25 | 0.3 | 0.5 | - | 0.5 |
| DC_7-66-71_n77 | 0.2 | 0.2 | - | 0.5 |
| DC_7-66_n71-n77 | 0.2 | 0.2 | - | 0.5 |
| DC_7-66-71_n78 | 0.2 | 0.2 | - | 0.5 |
| DC_7-66_n71-n78 | 0.2 | 0.2 | - | 0.5 |
| DC_7-71_n2-n66 | 0.5 | 0.2 | 0.2 | 0.5 |
| DC_7-71_n2-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_7-71_n2-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_7-71_n66-n77 | 0.2 | - | 0.2 | 0.5 |
| DC_7-71_n66-n78 | 0.2 | - | 0.2 | 0.5 |
| DC_8_n1-n3-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_8_n3-n28-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_8_n3-n77-n79 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_8-11_n1-n3 | - | 0.3 | - | 0.5 |
| DC_8-11_n1-n77 | 0.2 | - | 0.2 | 0.5 |
| DC_8-11_n3-n28 | 0.2 | 0.3 | 0.5 | 0.2 |
| DC_8-11_n3-n77 | 0.2 | 0.3 | 0.5 | - |
| DC_8-11_n3-n79 | - | 0.3 | 0.5 | 0.5 |
| DC_8-11_n28-n77 | 0.2 | - | 0.2 | 0.5 |
| DC_8-11_n77-n79 | 0.2 | - | 0.5 | - |
| DC_8-20_n1-n78 | 0.2 | 0.1 | - | 0.5 |
| DC_8-20-28_n1 | 0.2 | 0.2 | 0.2 | - |
| DC_8-20-28_n78 | 0.2 | 0.1 | 0.2 | 0.5 |
| DC_8-20-32_n3 | - | - | 0.5 | 0.3 |
| DC_8-20-38_n28 | 0.2 | 0.1 | - | 0.2 |
| DC_8-20-38_n78 | 0.2 | 0.1 | - | 0.2 |
| DC_8-20-40_n1 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_8-20-40_n28 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_8-20-40_n78 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_8-28-38_n1 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_8-28-40_n1 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_8-28_n40-n71 | 0.2 | 0.7 | - | 0.7 |
| DC_8-28_n40-n77 | - | - | - | 0.5 |
| DC_8-28_n71-n77 | 0.2 | 0.7 | 0.7 | 0.5 |
| DC_8_n28-n77-n79 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_8-32_n1-n78 | 0.2 | - | - | 0.5 |
| DC_8-38-40_n28 | 0.2 | 0.5 | 0.5 | 0.2 |
| DC_8_n39-n40-n79 | - | 0.3 | 0.3 | 0.5 |
| DC_8-39_n40-n79 | - | 0.3 | 0.3 | 0.5 |
| DC_8-40_n1-n78 | 0.2 | 0.45 | - | 0.55 |
| DC_8-41_n1-n3 | - | 03 / 0.54 | - | - |
| DC_8-41_n1-n77 | 0.2 | - | 0.2 | 0.5 |
| DC_8-41_n1-n78 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_8-41_n3-n77 | 0.2 | 09 / 0.510 | 0.2 | 0.5 |
| DC_8-42_n1-n3 | 0.2 | 0.5 | - | 0.2 |
| DC_8-42_n1-n77 | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_8-42_n3-n28 | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_8-42_n3-n77 | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_8-42_n28-n77 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_11_n3-n28-n77 | 0.3 | 0.5 | 0.2 | 0.5 |
| DC_11_n3-n77-n79 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_12-30-66_n2 | 0.5 | 0.5 | 0.4 | 0.4 |
| DC_12-30-66_n66 | 0.5 | 0.5 | 0.4 | 0.4 |
| DC_12-30-66_n77DC_12-30-66-66_n77 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_12-48_(n)5 | 0.5 | 0.3 | - | 0.5 |
| DC_12-48-66_n5 | 0.5 | 0.5 | 0.5 | - |
| DC_12-66_(n)5 | - | 0.5 | 0.5 | - |
| DC_12-66_n2-n41 | 0.5 | 0.3 | 0.3 | 0.5 |
| DC_12-66_n2-n66 | 0.5 | 0.3 | 0.3 | 0.3 |
| DC_12-66_n2-n77 | - | 0.3 | 0.3 | 0.5 |
| DC_12-66_n2-n78 | - | 0.3 | 0.3 | 0.5 |
| DC_12-66_n66-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_13-48-66_n77 | - | 0.5 | 0.2 | 0.5 |
| DC_13-66_n2-n77 | - | 0.2 | 0.2 | 0.5 |
| DC_13-66_n5-n48 | 0.3 | 0.2 | 0.5 | 0.5 |
| DC_13-66_n5-n77 DC_13-66-66_n5-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_13-66_n66-n77 | - | 0.2 | 0.2 | 0.5 |
| DC_14-30-66-n2 | - | 0.5 | 0.4 | 0.4 |
| DC_14-30-66_n66 | - | 0.5 | 0.4 | 0.4 |
| DC_14-30-66_n77DC_14-30-66-66_n77 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_18-41_n3-n77 | 0.2 | 03 / 0.54 | 0.2 | 0.5 |
| DC_18-41_n3-n78 | 0.2 | 03 / 0.54 | 0.2 | 0.5 |
| DC_19_n1-n77-n79 | 0.3 | 0.3 | 0.5 | - |
| DC_19_n1-n78-n79 | 0.3 | 0.3 | 0.5 | - |
| DC_19-21_n1-n77 | - | - | - | 0.5 |
| DC_19-21_n1-n78 | - | - | 0.2 | 0.5 |
| DC_19-21-42_n1 | - | - | 0.5 | - |
| DC_19-21-42_n77 | - | - | 0.5 | 0.5 |
| DC_19-21-42_n78 | - |  | 0.5 | 0.5 |
| DC_19-21-42_n79 | - | - | 0.5 | - |
| DC_19-21_n77-n79 | - | - | 0.5 | - |
| DC_19-21_n78-n79 | - | - | 0.5 | - |
| DC_19-42_n1-n77 | - | 0.5 | 0.2 | 0.5 |
| DC_19-42_n1-n78 | - | 0.5 | - | 0.5 |
| DC_19-42_n1-n79 | - | 0.5 | - | - |
| DC_19-42_n77-n79 | - | 0.5 | 0.5 | - |
| DC_19-42_n78-n79 | - | 0.5 | 0.5 | - |
| DC_20-(n)3-n67 | 0.1 | - | - | 0.1 |
| DC_20-28-32_n1 | 0.2 | 0.2 | - | - |
| DC_20-28-32_n3 | 0.3 | 0.2 | - | 0.3 |
| DC_20-28-38_n1 | 0.2 | 0.2 | - | - |
| DC_20-28-40_n1 | 0.2 | 0.2 | 0.5 | - |
| DC_20-28-40_n78 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_20-32_n1-n28 | 0.2 | - | - | 0.2 |
| DC_20-32_n1-n78 | 0.2 | - | - | 0.5 |
| DC_20-38-40_n1 | 0.2 | 0.4 | 0.5 | - |
| DC_20-38-40_n28 | 0.2 | 0.4 | 0.5 | 0.2 |
| DC_20-38_n3-n78 | 0.2 | 0.4 | 0.2 | 0.5 |
| DC_20-41_n1-n78 | - | - | - | 0.5 |
| DC_20-67-(n)3 | 0.1 | 0.1 | - | - |
| DC_21_n1-n77-n79 | - | 0.2 | 0.5 | - |
| DC_21_n1-n78-n79 | - | 0.2 | 0.5 | - |
| DC_21-28-42_n77 | - | 0.2 | 0.5 | 0.5 |
| DC_21-28-42_n78 | - | 0.2 | 0.5 | 0.5 |
| DC_21-28-42_n79 | - | 0.2 | 0.5 | - |
| DC_21_n28-n77-n79 | - | 0.2 | 0.5 | - |
| DC_21_n28-n78-n79 | - | 0.2 | 0.5 | - |
| DC_21-42_n1-n77 | - | 0.5 | 0.2 | 0.5 |
| DC_21-42_n1-n78 | - | 0.5 | - | 0.5 |
| DC_21-42_n1-n79 | - | 0.5 | - | - |
| DC_21-42_n77-n79 | - | 0.5 | 0.5 | - |
| DC_21-42_n78-n79 | - | 0.5 | 0.5 | - |
| DC_28_n5-n40-n78 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_28-32-38_n1 | 0.2 | - | - | - |
| DC_28-32_n40-n41 | 0.2 | - | 0.8 | 0.3 |
| DC_28-41-42_n78 | 0.2 | 0.4 | 0.5 | 0.5 |
| DC_29-30-66_n2DC_29-30-66-66_n2 | - | 0.5 | 0.4 | 0.4 |
| DC_29-30-66_n66 | - | 0.5 | 0.3 | 0.3 |
| DC_29-30-66_n77 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_30-66-(n)5 | 0.5 | - | 0.4 | 0.5 |
| DC_42_n1-n77-n79 | 0.5 | 0.2 | 0.5 | - |
| DC_42_n1-n78-n79 | 0.5 | 0.2 | 0.5 | - |
| DC_42_n3-n28-n77 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_46-66_n25-n41 | - | 0.3 | 0.3 | 0.51 / 12 |
| DC_46-66_n41-n71 | - | 0.3 | 0.51 / 12 | 0.2 |
| DC_48-66_n25-n48 | 0.4 | 0.3 | 0.3 | 0.4 |
| DC_66-71_n2-n41 | 0.5 | - | 0.3 | 0.5 |
| DC_66-71_n2-n66 | 0.3 | - | 0.3 | 0.3 |
| DC_2-5-66_n2-n66 | 0.5 | 0.3 | 0.5 | 0.5 |
| DC_66-71_n2-n77 | 0.5 | - | 0.3 | 0.5 |
| DC_66-71_n2-n78 | 0.5 | - | 0.3 | 0.5 |
| DC_66-71_n66-n77 | 0.2 | 0.2 | 0.2 | 0.5 |
| NOTE 1: The requirement is applied for UE transmitting on the frequency range of 2545 - 2690 MHz.NOTE 2: The requirement is applied for UE transmitting on the frequency range of 2496 - 2545 MHz.NOTE 3: The requirement is applied for UE transmitting on the frequency range of 2515 - 2690 MHz NOTE 4: The requirement is applied for UE transmitting on the frequency range of 2496 – 2515 MHz.NOTE 5: Only applicable for UE supporting inter-band carrier aggregation with uplink in one E-UTRA band and without simultaneous Rx/Tx.NOTE 6: Void.NOTE 7: Void.NOTE 8: Only applicable for UE supporting inter-band carrier aggregation with uplink in one NR band and without simultaneous Rx/Tx.NOTE 9: The requirement is applied for UE transmitting on the frequency range of 2515 - 2690 MHz.NOTE 10: The requirement is applied for UE transmitting on the frequency range of 2496 – 2515 MHz.NOTE 11: “-” denotes ΔRIB,c = 0.NOTE 12: The component band order in the configuration should be listed by the order of E-UTRA band and NR band respectively, such as for DC_30-66-(n)5 the band order from left to right is 5, 30, 66 and n5. |  |  |  |  |

##### 7.3B.3.3.4 ΔRIB,c for EN-DC five bands

Table 7.3B.3.3.4-1: ΔRIB,c due to EN-DC (five bands)

| Inter-band EN-DC configuration | ΔRIB,c for E-UTRA band / NR band (dB)6 |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Component band in order of bands in configuration7 |  |  |  |  |
| DC_1-3-5-7_n28DC_1-3-5-7-7_n28 | - | - | 0.2 | - | 0.2 |
| DC_1-3-5-7_n40DC_1-3-5-7-7_n40 | - | - | 0.2 | 0.3 | 0.8 |
| DC_1-3-5-7_n77 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-5-7_n78DC_1-3-5-7-7_n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-5_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.8 |
| DC_1-3-5_n40-n77 | 0.2 | 0.2 | 0.2 | 0.45 | 0.55 |
| DC_1-3-5_n40-n78 | 0.2 | 0.2 | 0.2 | 0.45 | 0.55 |
| DC_1-3-5-41_n79 | - | - | - | 03 / 0.54 | - |
| DC_1-3-7_n3-n78 | 0.3 | 0.3 | 0.3 | 0.3 | 0.5 |
| DC_1-3-7_n5-n40 | - | - | 0.3 | 0.2 | 0.8 |
| DC_1-3-7_n7-n78 | 0.3 | 0.3 | 0.3 | 0.3 | 0.5 |
| DC_1-3-7-8_n7 | - | - | - | 0.2 | - |
| DC_1-3-7-8_n28 | - | - | - | 0.2 | 0.2 |
| DC_1-3-7-8_n78DC_1-3-3-7-8_n78DC_1-3-7-7-8_n78DC_1-3-3-7-7-8_n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7_n8-n78DC_1-3-3-7_n8-n78DC_1-3-7-7_n8-n78DC_1-3-3-7-7_n8-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7-20_n28 | - | - | - | 0.2 | 0.2 |
| DC_1-3-7-20_n38 | - | - | - | - | 0.2 |
| DC_1-3-7-20_n78 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-7_n26-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7-26_n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7-28_n3 | - | - | - | 0.2 | - |
| DC_1-3-7-28_n5 | - | - | - | 0.2 | 0.2 |
| DC_1-3-7-28_n7DC_1-3-28-(n)7 | - | - | - | 0.2 | - |
| DC_1-3-7-28_n38 | - | - | - | 0.2 | - |
| DC_1-3-7_n28-n38 | - | - | - | 0.2 | - |
| DC_1-3-7-28_n40 | - | - | 0.3 | 0.2 | 0.8 |
| DC_1-3-7-28_n78DC_1-3-7-7-28_n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7-32_n28 | - | 0.5 | - | - | 0.5 |
| DC_1-3-7-32_n78 | 0.3 | 0.3 | 0.3 | - | 0.5 |
| DC_1-3-7-38_n28 | - | - | - | 0.2 | 0.2 |
| DC_1-3-7-40_n78 | 0.2 | 0.2 | - | 0.45 | 0.55 |
| DC_1-3-7_n40-n77DC_1-3-7-7_n40-n77 | - | - | 0.3 | 0.8 | 0.5 |
| DC_1-3-7_n40-n78DC_1-3-7-7_n40-n78 | - | - | 0.3 | 0.8 | 0.5 |
| DC_1-3-7_n40-n105 | 0.2 | 0.2 | 0.2 | 0.5 | 0.3 |
| DC_1-3-7_n75-n78 | 0.3 | 0.3 | 0.3 | - | 0.5 |
| DC_1-3-7_n78-n105 | 0.6 | 0.6 | 0.3 | 0.5 | 0.3 |
| DC_1-3-8_n1-n41DC_1-3-3-8_n1-n41 | - | - | - | - | 03 / 0.54 |
| DC_1-3-8_n1-n78DC_1-3-3-8_n1-n78 | 0.2 | 0.2 | 0.2 |  | 0.5 |
| DC_1-3-8_n7-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-8-11_n28 | - | 0.3 | 0.2 | 0.5 | 0.2 |
| DC_1-3-8-11_n77 | 0.2 | 0.3 | 0.2 | 0.5 | 0.5 |
| DC_1-3-8-20_n28 | 0.2 | 0.2 | 0.2 | - | 0.2 |
| DC_1-3-8-20_n78 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-8-28_n40 | 0.2 | 0.2 | 0.2 | 0.2 | 0.3 |
| DC_1-3-8-28_n71 | - | - | 0.2 | 0.7 | 0.7 |
| DC_1-3-8-28_n77 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-8_n28-n77 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-8-28_n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-8_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-8-32_n78 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-8-38_n28 | 0.2 | 0.2 | 0.2 | - | 0.2 |
| DC_1-3-8-38_n78 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-8-40_n28 | 0.2 | 0.2 | 0.2 | - | 0.2 |
| DC_1-3-8_n40-n71 | 0.2 | 0.2 | 0.2 | 0.3 | 0.3 |
| DC_1-3-8_n40-n77 | 0.2 | 0.2 | 0.2 | 0.4 | 0.5 |
| DC_1-3-8-40_n78 | 0.2 | 0.2 | 0.2 | 0.45 | 0.55 |
| DC_1-3-8-41_n1DC_1-3-3-8-41_n1 | - | - | - | 03 / 0.54 | - |
| DC_1-3-8-41_n41DC_1-3-3-8-41_n41 | - | - | - | 03 / 0.54 | 03 / 0.54 |
| DC_1-3-8_n41-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-8-42_n77 | 0.2 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_1-(n)3-n8-n77 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-8_n71-n77 | 0.2 | 0.3 | 0.3 | 0.2 | 0.5 |
| DC_1-3-8_n77-n79 | 0.2 | 0.3 | 0.3 | 0.5 | - |
| DC_1-3-11_n28-n77 | 0.2 | 0.3 | 0.5 | 0.2 | 0.5 |
| DC_1-3-18_n3-n41 | - | 0.5 | - | 0.5 | 03 / 0.54 |
| DC_1-3-18_n3-n77 | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_1-3-18_n3-n78 | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_1-3-18_n28-n41 | - | 0.5 | - | 0.2 | 03 / 0.54 |
| DC_1-3-18_n28-n77 | - | - | - | 0.2 | 0.5 |
| DC_1-3-18_n28-n78 | - | - | - | 0.2 | 0.5 |
| DC_1-3-18_n41-n77 | - | 0.5 | - | 03 / 0.54 | 0.5 |
| DC_1-3-18_n41-n78 | - | 0.5 | - | 03 / 0.54 | 0.5 |
| DC_1-3-18-42_n77 | 0.2 | 0.2 | - | 0.5 | 0.5 |
| DC_1-3-18-42_n78 | 0.2 | 0.2 | - | 0.5 | 0.5 |
| DC_1-3-18-42_n79 | 0.2 | 0.2 | - | 0.5 | - |
| DC_1-3-19-21_n77 | 0.2 | 0.3 | - | 0.5 | 0.5 |
| DC_1-3-19-21_n78 | 0.2 | 0.3 | - | 0.5 | 0.5 |
| DC_1-3-19-21_n79 | - | 0.3 | - | 0.5 | - |
| DC_1-3-19-42_n77 | 0.2 | 0.2 | - | 0.5 | 0.5 |
| DC_1-3-19-42_n78 | 0.2 | 0.2 | - | 0.5 | 0.5 |
| DC_1-3-19-42_n79 | 0.2 | 0.2 | - | 0.5 | - |
| DC_1-3-20_n1-n78 | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_1-3-20_n7-n78 | 0.2 | 0.2 | - | - | 0.5 |
| DC_1-3-20_n8-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-20_n28-n75 | 0.2 | 0.5 | 0.2 | 0.5 | - |
| DC_1-3-20_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-20-28_n78DC_1-3-3-20-28_n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-20-32_n28 | - | 0.5 | 0.2 | - | 0.5 |
| DC_1-3-20-32_n78 | 0.2 | 0.2 | - | - | 0.5 |
| DC_1-3-20-38_n28 | - | 0.2 | 0.2 | 0.4 | 0.5 |
| DC_1-3-20-38_n78 | - | 0.2 | 0.2 | 0.4 | 0.5 |
| DC_1-3-20_n38-n78 | - | 0.2 | 0.2 | 0.4 | 0.5 |
| DC_1-3-20-40_n28 | - | 0.2 | 0.2 | 0.4 | 0.5 |
| DC_1-3-20-40_n78 | - | - | - | 05 | 0.55 |
| DC_1-3-20-41_n1DC_1-3-3-20-41_n1 | - | - | - | 03 / 0.54 | - |
| DC_1-3-20-41_n78 | - | - | - | 03 / 0.54 | 0.5 |
| DC_1-3-20_n41-n78 | - | - | - | - | 0.5 |
| DC_1-3-21-42_n77 | 0.2 | 0.3 | 0.5 | 0.5 | 0.2 |
| DC_1-3-21-42_n78 | 0.2 | 0.3 | 0.5 | 0.5 | 0.2 |
| DC_1-3-21-42_n79 | 0.2 | 0.3 | 0.5 | 0.5 | - |
| DC_1-3-21_n77-n79 | 0.2 | 0.3 | 0.5 | 0.5 | - |
| DC_1-3-21_n78-n79 | 0.2 | 0.3 | 0.5 | 0.5 | - |
| DC_1-3-28_n3-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-28_n7-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-28_n40-n71 | 0.2 | 0.2 | 0.7 | 0.2 | 0.7 |
| DC_1-3-28_n40-n77 | - | - | - | - | 0.5 |
| DC_1-3-28-40_n78 | - | - | 0.2 | - | 0.5 |
| DC_1-3-28_n40-n78 | - | 0.2 | 0.2 | 0.45 | 0.55 |
| DC_1-3-28-42_n77 | 0.2 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_1-3-28-42_n78 | 0.2 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_1-3-28-42_n79 | 0.2 | 0.2 | 0.2 | 0.5 | - |
| DC_1-3-28_n71-n77 | 0.2 | 0.2 | 0.7 | 0.7 | 0.5 |
| DC_1-3_n28-n77-n79 | 0.2 | 0.2 | 0.2 | 0.5 | - |
| DC_1_n3-n28-n77-n79 | 0.3 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_1-3_n28-n78-n79 | 0.2 | 0.2 | 0.2 | 0.5 | - |
| DC_1-3-32_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-38_n7-n78 | 0.3 | 0.3 | 0.4 | 0.3 | 0.5 |
| DC_1-3-38_n28-n78 | - | 0.2 | - | 0.2 | 0.5 |
| DC_1-3-41_n1-n41DC_1-3-3-41_n1-n41 | - | - | 03 / 0.54 | - | 03 / 0.54 |
| DC_1-3-41_n1-n78DC_1-3-3-41_n1-n78 | - | - | 03 / 0.54 | - | 0.5 |
| DC_1-3-41_n3-n41 | - | - | 03 / 0.54 | - | 03 / 0.54 |
| DC_1-3-41_n3-n77 | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_1-3-41_n3-n78 | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_1-3-41_n28-n41 | - | - | 03 / 0.54 | 0.2 | 03 / 0.54 |
| DC_1-3-41_n28-n77 | 0.2 | 0.2 | 03 / 0.54 | 0.2 | 0.5 |
| DC_1-3-41_n28-n78 | - | 0.2 | 03 / 0.54 | 0.2 | 0.5 |
| DC_1-3-41_n41-n77 | 0.2 | 0.2 | - | - | 0.5 |
| DC_1-3-41_n41-n78 | 0.2 | 0.2 | - | - | 0.5 |
| DC_1-3-41-42_n77 | 0.2 | 0.2 | - | 0.5 | 0.5 |
| DC_1-3-41-42_n78 | 0.2 | 0.2 | - | 0.5 | 0.5 |
| DC_1-3-41-42_n79 | 0.2 | 0.2 | - | 0.5 | - |
| DC_1-3-42_n28-n77 | 0.2 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_1-5-7_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.8 |
| DC_1-5-7_n40-n77DC_1-5-7-7_n40-n77 | 0.2 | 0.2 | - | 0.45 | 0.55 |
| DC_1-5-7_n40-n78DC_1-5-7-7_n40-n78 | 0.2 | 0.2 | - | 0.45 | 0.55 |
| DC_1-7-8_n7-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7-8-20 _n3 | - | - | 0.2 | 0.2 | - |
| DC_1-7-8-20 _n28 | - | - | 0.2 | 0.2 | 0.2 |
| DC_1-7-8-20_n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7-8_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7-8-32_n78 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_1-7-8-40_n78 | 0.2 | - | 0.2 | 0.45 | 0.55 |
| DC_1-7-20_n3-n38 | - | - | 0.2 | - | 0.2 |
| DC_1-7-20_n3-n78 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_1-7-20_n8-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7-20-28_n3 | - | - | 0.2 | 0.2 | - |
| DC_1-7-20_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7-20-32_n8 | - | - | 0.2 | - | 0.2 |
| DC_1-7-20-32_n28 | - | - | 0.2 | - | 0.2 |
| DC_1-7-20-32_n78 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_1-7-20-38_n3 | - | - | - | 0.2 | - |
| DC_1-7-28_n3-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7-28_n5-n40 | - | 0.3 | 0.2 | 0.2 | 0.8 |
| DC_1-7-28_n7-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7-28-32_n3 | - | - | 0.2 | - | - |
| DC_1-7-28_n40-n78 | 0.2 | - | 0.2 | 0.4 | 0.5 |
| DC_1-7-32_n28-n78 | - | - | - | 0.2 | 0.5 |
| DC_1-7-38_n3-n78 | 0.6 | 0.6 | - | - | 0.8 |
| DC_1-7_n40-n78-n105 | 0.2 | 0.2 | 0.2 | 0.5 | 0.3 |
| DC_1-8_n3-n28-n77 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8_n3-n28-n79 | 0.3 | 0.3 | 0.2 | 0.2 | 0.5 |
| DC_1-8_n3-n77-n79 | 0.2 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_1-8-11_n3-n28 | - | 0.2 | 0.3 | 0.5 | 0.2 |
| DC_1-8-11_n3-n77 | 0.2 | 0.2 | 0.3 | 0.5 | 0.5 |
| DC_1-8-11_n28-n77 | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_1-8-11_n3-n79 | - | - | 0.3 | 0.5 | 0.5 |
| DC_1-8-11_n77-n79 | 0.2 | 0.2 | - | 0.5 | - |
| DC_1-8-20-28_n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8-20-38_n28 | 0.2 | 0.2 | 0.2 | - | 0.2 |
| DC_1-8-20-38_n78 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_1-8-20-40_n28 | 0.2 | 0.2 | 0.2 | - | 0.2 |
| DC_1-8-28_n40-n71 | - | 0.2 | 0.7 | - | 0.7 |
| DC_1-8-28_n40-n77 | - | - | - | - | 0.5 |
| DC_1-8-28_n71-n77 | 0.2 | 0.2 | 0.7 | 0.7 | 0.5 |
| DC_1-8_n28-n77-n79 | 0.3 | 0.3 | 0.3 | 0.5 | 0.5 |
| DC_1-8-41_n1-n41 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 |
| DC_1-8-41_n1-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8-42_n28-n77 | 0.2 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_1-11_n3-n28-n77 | 0.2 | 0.3 | 0.5 | 0.2 | 0.3 |
| DC_1-18-41_n3-n77 | 0.2 | - | 03 / 0.54 | 0.2 | 0.5 |
| DC_1-18-41_n3-n78 | 0.2 | - | 03 / 0.54 | 0.2 | 0.5 |
| DC_1-8-(n)3-n77 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8-(n)3-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-8-42_n3-n28 | - | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_1-8-42_n3-n77 | 0.2 | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_1-11_n3-n77-n79 | 0.2 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_1-19-21-42_n77 | 0.2 | - | - | 0.5 | 0.5 |
| DC_1-19-21-42_n78 | - | - | - | 0.5 | 0.5 |
| DC_1-19-21-42_n79 | - | - | - | 0.5 | - |
| DC_1-19-42_n77-n79 | 0.2 | - | 0.5 | 0.5 | - |
| DC_1-19-42_n78-n79 | - | - | 0.5 | 0.5 | - |
| DC_1-20-28-32_n3 | - | 0.2 | 0.2 | - | - |
| DC_1-20-38_n3-n78 | - | - | - | 0.2 | 0.5 |
| DC_1-20-41_n1-n78 | - | - | - | - | 0.5 |
| DC_1-21-28-42_n77 | 0.2 | - | 0.2 | 0.5 | 0.5 |
| DC_1-21-28-42_n78 | - | - | 0.2 | 0.5 | 0.5 |
| DC_1-21-28-42_n79 | - | - | 0.2 | 0.5 | - |
| DC_1-21_n28-n77-n79 | 0.3 | - | 0.3 | 0.5 | - |
| DC_1-21_n28-n78-n79 | 0.3 | - | 0.3 | 0.5 | - |
| DC_1-21-42_n77-n79 | 0.2 | 0.2 | 0.5 | 0.5 | - |
| DC_1-21-42_n78-n79 | - | 0.2 | 0.5 | 0.5 | - |
| DC_1-28-32_n40-n41 | - | 0.2 | - | 0.8 | 0.3 |
| DC_1-42_n3-n28-n77 | 0.2 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_2-5-7_n2-n66 | 0.3 | - | 0.5 | 0.3 | 0.5 |
| DC_2-5-7_n2-n77 | 0.2 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_2-5-7_n2-n78 | 0.2 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_2-5-7-66_n2 | 0.3 | - | 0.5 | 0.5 | 0.3 |
| DC_2-5-7-66_n7DC_2-5-7-66-66_n7 | 0.3 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_2-5-7-(n)66DC_2-5-7-7-(n)66DC_2-5-7-66_n66 | 0.3 | - | 0.5 | 0.5 | 0.5 |
| DC_2-5-7-66_n77DC_2-5-7_n66-n77 | 0.2 | - | 0.2 | 0.2 | 0.5 |
| DC_2-5-7-66_n78DC_2-5-7_n66-n78 | 0.2 | - | 0.2 | 0.2 | 0.5 |
| DC_2-5-30-66_n2 | 0.4 | - | 0.5 | 0.4 | 0.4 |
| DC_2-5-30-66_n66 | 0.4 | - | 0.5 | 0.4 | 0.4 |
| DC_2-5-30-66_n77 | 0.3 | 0.2 | 0.5 | 0.4 | 0.5 |
| DC_2-5-66_n2-n41 | 0.3 | 0.2 | 0.5 | 0.5 | 0.51 / 12 |
| DC_2-5-66_n2-n66 | 0.3 | - | 0.3 | 0.3 | 0.3 |
| DC_2-5-66_n2-n77DC_2-5-66-66_n2-n77 | 0.2 | 0.2 | 0.3 | 0.3 | 0.5 |
| DC_2-5-66_n2-n78 | 0.2 | 0.2 | 0.3 | 0.3 | 0.5 |
| DC_2-5-66_n5-n77DC_2-5-66-66_n5-n77 | 0.3 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-5-66_n41-n66 | 0.3 | - | 0.6 | 0.5 | 0.6 |
| DC_2-5-66_n41-n77 | 0.3 | 0.2 | 0.6 | 0.51 / 12 | 0.6 |
| DC_2-5-66_n41-n78 | 0.3 | 0.2 | 0.6 | 0.51 / 12 | 0.6 |
| DC_2-5-66_n66-n77 | 0.3 | - | 0.3 | 0.3 | 0.5 |
| DC_2-7-12_n2-n66 | 0.3 | 0.3 | 0.5 | 0.3 | 0.5 |
| DC_2-7-12_n2-n77 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_2-7-12_n2-n78 | 0.3 | 0.3 | 0.5 | 0.3 | 0.5 |
| DC_2-7-12-66_n2 | 0.3 | 0.3 | 0.5 | 0.5 | 0.3 |
| DC_2-7-12-66_n66 | 0.3 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_2-7-12-66_n77DC_2-7-12_n66-n77 | 0.2 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_2-7-12-66_n78DC_2-7-12_n66-n78 | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_2-7-13-(n)66DC_2-7-7-13-(n)66DC_2-7-13_n25-n66 | 0.3 | 0.5 | - | 0.3 | 0.5 |
| DC_2-7-13-66_n66 | 0.3 | 0.5 | - | 0.5 | 0.5 |
| DC_2-7-28-66_n7 | 0.3 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_2-7-28-66_n66 | 0.3 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_2-7-29-66_n78DC_2-7-7-29-66_n78 | 0.2 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_2-7-66_n2-n66 | 0.3 | 0.5 | 0.3 | 0.3 | 0.5 |
| DC_2-7-66_n2-n71 | 0.3 | 0.5 | 0.3 | 0.5 | - |
| DC_2-7-66_n2-n77 | 0.3 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-7-66_n2-n78 | 0.3 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-7-66_n25-n66 | 0.3 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-7-66_n66-n71 | 0.3 | 0.5 | 0.5 | 0.5 | 0.2 |
| DC_2-7-66_n66-n77 | 0.3 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-7-(n)66-n78DC_2-7-66_n66-n78DC_2-7-7-(n)66-n78DC_2-7-7-66_n66-n78 | 0.3 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-7-66-71_n2 | 0.3 | 0.5 | 0.5 | - | 0.3 |
| DC_2-7-66-71_n66 | 0.3 | 0.5 | 0.5 | 0.2 | 0.5 |
| DC_2-7-66-71_n77DC_2-7-66_n71-n77 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_2-7-66-71_n78DC_2-7-66_n71-n78 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_2-7-71_n2-n66 | 0.3 | 0.5 | - | 0.3 | 0.5 |
| DC_2-7-71_n2-n77 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_2-7-71_n2-n78 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_2-7-71_n66-n77 | 0.3 | 0.5 | 0.2 | 0.3 | 0.5 |
| DC_2-7-71_n66-n78 | 0.3 | 0.5 | 0.2 | 0.3 | 0.5 |
| DC_2-12-30-66_n2 | 0.4 | 0.5 | 0.5 | 0.4 | 0.4 |
| DC_2-12-30-66_n66 | 0.4 | 0.5 | 0.5 | 0.4 | 0.4 |
| DC_2-12-30-66_n77 | 0.2 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-12-66_n2-n41 | 0.3 | 0.5 | 0.3 | 0.3 | 0.5 |
| DC_2-12-66_n2-n66 | 0.5 | 0.3 | 0.3 | 0.3 | 0.3 |
| DC_2-12-66_n2-n77 | 0.2 | - | 0.3 | 0.3 | 0.5 |
| DC_2-12-66_n2-n78 | 0.2 | - | 0.3 | 0.3 | 0.5 |
| DC_2-12-66_n66-n77 | 0.3 | - | 0.3 | 0.3 | 0.5 |
| DC_2-13-66_n2-n77DC_2-13-66-66_n2-n77 | 0.2 | - | 0.3 | 0.3 | 0.5 |
| DC_2-13-66_n5-n77DC_2-2-13-66_n5-n77DC_2-13-66-66_n5-n77 | 0.3 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_2-13-66_n66-n77DC_2-2-13-66_n66-n77 | 0.3 | - | 0.3 | 0.3 | 0.5 |
| DC_2-14-30-66_n2 | 0.4 | - | 0.5 | 0.4 | 0.4 |
| DC_2-14-30-66_n66 | 0.4 | - | 0.5 | 0.4 | 0.4 |
| DC_2-14-30-66_n77 | 0.2 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_2-29-30-66_n2 | 0.4 | - | 0.5 | 0.4 | 0.4 |
| DC_2-29-30-66_n66 | 0.4 | - | 0.5 | 0.4 | 0.4 |
| DC_2-29-30-66_n77 | 0.2 | 0.5 | 0.5 | 0.5 | 0.5 |
| DC_2-30-66-(n)5 | 0.4 | - | 0.5 | 0.4 | - |
| DC_2-46-66_n41-n71 | 0.3 | - | 0.3 | 0.51 / 12 | 0.5 |
| DC_2-66-71_n2-n41 | 0.3 | 0.3 | 0.2 | 0.3 | 0.3 |
| DC_2-66-71_n2-n66 | 0.3 | 0.3 | - | 0.3 | 0.3 |
| DC_2-66-71_n2-n77 | 0.3 | 0.5 | - | 0.3 | 0.5 |
| DC_2-66-71_n2-n78 | 0.3 | 0.5 | - | 0.3 | 0.5 |
| DC_2-66-71_n66-n77 | 0.3 | 0.3 | - | 0.3 | 0.5 |
| DC_3-5-7_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.8 |
| DC_3-5-7_n40-n77DC_3-5-7-7_n40-n77 | 0.2 | 0.2 | - | 0.45 | 0.55 |
| DC_3-5-7_n40-n78DC_3-5-7-7_n40-n78 | 0.2 | 0.2 | - | 0.45 | 0.55 |
| DC_3-7_n1-n40-n78 | 0.6 | 0.8 | 0.6 | 0.9 | 0.8 |
| DC_3-7_n1-n75-n78 | 0.3 | 0.3 | 0.3 | - | 0.5 |
| DC_3-7-8_n1-n40 | - | 0.3 | 0.2 | 0.1 | 0.8 |
| DC_3-7-8_n1-n78DC_3-3-7-8_n1-n78DC_3-7-7-8_n1-n78DC_3-3-7-7-8_n1-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-8_n7-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-8-20_n1 | - | - | 0.2 | 0.2 | - |
| DC_3-7-8-20_n78 | - | - | 0.2 | 0.2 | 0.5 |
| DC_3-7-20-28_n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-8_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-8-40_n78 | 0.2 | - | 0.2 | 0.45 | 0.55 |
| DC_3-7-20_n1-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-20_n8-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-20-28_n1 | - | - | 0.2 | 0.2 | - |
| DC_3-7-20_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | - |
| DC_3-7-20-38_n78 | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_3-7-28_n1-n40 | - | 0.3 | 0.2 | - | 0.8 |
| DC_3-7-28_n1-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-28_n3-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-28_n5-n40 | - | 0.7 | 0.2 | 0.2 | 0.8 |
| DC_3-7-28_n7-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-32_n1-n28 | 0.2 | 0.2 | - | 0.2 | 0.2 |
| DC_3-7-32_n28-n78 | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_3-7-28_n40-n78 | 0.2 | - | 0.2 | 0.4 | 0.5 |
| DC_3-7-32_n1-n78 | 0.3 | 0.3 | - | 0.3 | 0.5 |
| DC_3-7-40_n1-n78 | 0.2 | - | 0.45 | 0.2 | 0.55 |
| DC_3-7_n40-n78-n105 | 0.2 | 0.2 | 0.2 | 0.5 | 0.3 |
| DC_3-8-11_n28-n77 | 0.3 | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_3-8-20_n1-n78 | 0.2 | 0.2 | 0.2 | 0.3 | 0.5 |
| DC_3-8-20-28_n1 | 02 | 0.2 | 0.2 | 0.2 | 0.2 |
| DC_3-8-20-38_n1 | 02 | 0.2 | 0.2 | 0.4 | 0.2 |
| DC_3-8-20-38_n28 | 02 | 0.2 | 0.2 | 0.4 | 0.2 |
| DC_3-8-20-40_n1 | 02 | 0.2 | 0.2 | 0.4 | 0.2 |
| DC_3-8-20-40_n28 | 02 | 0.2 | 0.2 | 0.4 | 0.2 |
| DC_3-8-20-40_n78 | 02 | 0.2 | 0.2 | 0.4 | 0.5 |
| DC_3-8-28-38_n1 | 02 | 0.2 | 0.2 | 0.4 | 0.2 |
| DC_3-8-28-40_n1 | 02 | 0.2 | 0.2 | 0.4 | 0.2 |
| DC_3-8-28_n40-n71 | - | 0.2 | 0.7 | - | 0.7 |
| DC_3-8-28_n40-n77 | - | - | - | - | 0.5 |
| DC_3-8-28_n71-n77 | 0.2 | 0.2 | 0.7 | 0.7 | 0.5 |
| DC_3-8-32_n1-n78 | 0.2 | 0.2 | 0.5 | 0.3 | 0.5 |
| DC_3-8-40_n1-n78 | 0.2 | 0.2 | 0.45 | 0.2 | 0.55 |
| DC_3-8-41_n1-n41DC_3-3-8-41_n1-n41 | - | - | 03 / 0.54 | - | 03 / 0.54 |
| DC_3-8-41_n1-n78DC_3-3-8-41_n1-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-19-21-42_n77 | 0.3 | - | 0.5 | 0.5 | 0.5 |
| DC_3-19-21-42_n78 | 0.3 | - | 0.5 | 0.5 | 0.5 |
| DC_3-19-21-42_n79 | 0.3 | - | 0.5 | 0.5 | - |
| DC_3-19-42_n1-n77 | 0.2 | - | 0.5 | 0.2 | 0.5 |
| DC_3-19-42_n1-n78 | 0.2 | - | 0.5 | 0.2 | 0.5 |
| DC_3-19-42_n1-n79 | 0.2 | - | 0.5 | 0.2 | - |
| DC_3-20_n1-n28-n75 | 0.5 | 0.2 | - | 0.5 | - |
| DC_3-20-28-38_n1 | 0.2 | 0.2 | 0.2 | 0.4 | 0.2 |
| DC_3-20-28-40_n1 | 0.2 | 0.2 | 0.2 | 0.4 | 0.2 |
| DC_3-20-28-40_n78 | 0.2 | 0.2 | 0.2 | 0.4 | 0.5 |
| DC_3-20-32_n1-n28 | 0.5 | 0.2 | - | 0.2 | 0.5 |
| DC_3-20-32_n1-n78 | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_3-20-38-40_n1 | 0.2 | 0.2 | 0.4 | 0.4 | 0.2 |
| DC_3-20-38-40_n28 | 0.2 | 0.2 | 0.4 | 0.4 | 0.2 |
| DC_3-20-41_n1-n78DC_3-3-20-41_n1-n78 | - | - | - | - | 0.5 |
| DC_3-21_n1-n77-n79 | 0.3 | 0.5 | 0.2 | 0.5 | - |
| DC_3-21_n1-n78-n79 | 0.3 | 0.5 | 0.2 | 0.5 | - |
| DC_3-21_n28-n77-n79 | 0.3 | 0.5 | 0.2 | 0.5 | - |
| DC_3-21-42_n1-n77 | 0.3 | 0.5 | 0.5 | 0.2 | 0.2 |
| DC_3-21-42_n1-n78 | 0.3 | 0.5 | 0.5 | 0.2 | 0.2 |
| DC_3-21-42_n1-n79 | 0.3 | 0.5 | 0.5 | 0.2 | - |
| DC_3-28_n1-n40-n78 | 0.2 | 0.2 | 0.2 | 0.8 | 0.5 |
| DC_3-28-41-42_n78 | 0.5 | 0.2 | 0.43 / 0.54 | N/A | 0.5 |
| DC_5-7-66_n2-n66 | - | 0.5 | 0.3 | 0.3 | 0.5 |
| DC_5-7-66_n2-n77 | 0.5 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_5-7-66_n2-n78 | 0.5 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_5-7-66_n66-n77 | 0.5 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_7-8-20-32_n1 | - | 0.2 | 0.2 | - | - |
| DC_7-8-20-38_n1 | - | 0.2 | 0.2 | 0.2 | - |
| DC_7-8-20_n1-n78 | - | 0.2 | 0.2 | - | 0.5 |
| DC_7-8-32_n1-n78 | - | 0.2 | - | - | 0.5 |
| DC_7-8-32-38_n1 | - | 0.2 | - | 0.2 | - |
| DC_7-8-40_n1-n78 | - | 0.2 | 0.45 | 0.2 | 0.55 |
| DC_7-12-66_n2-n66 | 0.5 | 0.5 | 0.3 | 0.3 | 0.3 |
| DC_7-12-66_n2-n77 | 0.5 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_7-12-66_n2-n78 | 0.5 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_7-12-66_n66-n77 | 0.5 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_7-20-28-32_n3 | - | 0.2 | 0.1 | - | - |
| DC_7-20-28-38_n1 | - | 0.2 | - | - | - |
| DC_7-20-32_n1-n78 | - | - | - | - | 0.5 |
| DC_7-20-32-38_n1 | - | - | - | 0.2 | - |
| DC_7-28-32-38_n1 | - | 0.2 | - | 0.2 | - |
| DC_7-20-32-38_n1 | - | - | - | 0.2 | - |
| DC_7-20-38_n3-n78 | - | - | 0.4 | - | 0.6 |
| DC_7-28_n1-n40-n78 | 0.3 | 0.2 | 0.2 | 0.8 | 0.5 |
| DC_7-66-71_n2-n66 | 0.5 | 0.3 | 0.2 | 0.3 | 0.5 |
| DC_7-66-71_n2-n77 | 0.5 | 0.5 | - | 0.3 | 0.5 |
| DC_7-66-71_n2-n78 | 0.5 | 0.5 | - | 0.3 | 0.5 |
| DC_7-66-71_n66-n77 | 0.5 | 0.5 | 0.1 | 0.5 | 0.5 |
| DC_8_n3-n28-n77-n79 | 0.2 | 0.2 | 0.2 | 0.5 | 0.5 |
| DC_8-11_n3-n28-n77 | 0.2 | 0.3 | 0.5 | 0.2 | 0.5 |
| DC_8-11_n3-n77-n79 | 0.2 | 0.3 | 0.5 | 0.5 | 0.5 |
| DC_8-20-28-38_n1 | - | 0.2 | - | - | - |
| DC_8-20-28-40_n1 | - | 0.2 | - | - | - |
| DC_8-20-38-40_n28 | - | 0.2 | - | - | - |
| DC_8-42_n3-n28-n77 | 0.2 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_19-21-42_n1-n77 | - | - | 0.5 | 0.2 | 0.5 |
| DC_19-21-42_n1-n78 | - | - | 0.5 | - | 0.5 |
| DC_19-21-42_n1-n79 | - | - | 0.5 | - | - |
| DC_19-21-42_n77-n79 | - | - | 0.5 | 0.5 | - |
| DC_19-21-42_n78-n79 | - | - | 0.5 | 0.5 | - |
| DC_19-42_n1-n77-n79 | 0.3 | 0.5 | 0.3 | 0.5 | - |
| DC_19-42_n1-n78-n79 | 0.3 | 0.5 | 0.3 | 0.5 | - |
| DC_20-28-32-38_n1 | 0.2 | 0.2 | - | - | - |
| NOTE 1: The requirement is applied for UE transmitting on the frequency range of 2545 – 2690 MHz.NOTE 2: The requirement is applied for UE transmitting on the frequency range of 2496 – 2545 MHz.NOTE 3: The requirement is applied for UE transmitting on the frequency range of 2515 - 2690 MHz.NOTE 4: The requirement is applied for UE transmitting on the frequency range of 2496 – 2515 MHz.NOTE 5: Only applicable for UE supporting inter-band carrier aggregation with uplink in one E-UTRA band and without simultaneous Rx/Tx.NOTE 6: “-” denotes ΔRIB,c = 0.NOTE 7: The component band order in the configuration should be listed by the order of E-UTRA band and NR band respectively, such as for DC_2-30-66-(n)5 the band order from left to right is 2, 5, 30, 66 and n5. |  |  |  |  |  |

##### 7.3B.3.3.5 ΔRIB,c for EN-DC six bands

Table 7.3B.3.3.5-1: ΔRIB,c due to EN-DC (six bands)

| Inter-band EN-DC configuration | ΔRIB,c for E-UTRA band / NR band (dB)3 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Component band in order of bands in configuration4 |  |  |  |  |  |
| DC_1A-3-5-7_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.8 |
| DC_1-3-5-7_n40-n77DC_1-3-5-7-7_n40-n77 | 0.2 | 0.2 | 0.2 | - | 0.41 | 0.51 |
| DC_1-3-5-7_n40-n78DC_1-3-5-7-7_n40-n78 | 0.2 | 0.2 | 0.2 | - | 0.41 | 0.51 |
| DC_1-3-7-8_n7-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7-8_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7-8-32_n78 | 0.2 | 0.2 | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-7-8-40_n78 | 0.2 | 0.2 | - | 0.2 | 0.41 | 0.51 |
| DC_1-3-7-20_n8-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7-20-28_n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7-20_n28-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7-20-32_n78 | 0.2 | - | 0.2 | 0.2 | - | 0.5 |
| DC_1-3-7-20-38_n78 | 0.7 | 0.7 | - | 0.6 | - | 0.8 |
| DC_1-3-7-20_n38-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7-28_n3-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7-28_n5-n40 | - | - | 0.3 | 0.2 | 0.2 | 0.8 |
| DC_1-3-7-28_n7-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7-28_n38-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-7-28_n40-n78 | - | - | 0.3 | 0.2 | 0.8 | 0.5 |
| DC_1-3-7-32_n28-n78 | 0.2 | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_1-3-7_n40-n78-n105 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 | 0.2 |
| DC_1-3-8-11_n28-n77 | 0.2 | 0.3 | 0.2 | 0.5 | 0.2 | 0.5 |
| DC_1-3-8-20-28_n78 | - | - | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-8-20_n28-n78 | - | - | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-3-8-20-38_n28 | - | - | 0.2 | 0.2 | - | 0.2 |
| DC_1-3-8-20-40_n28 | - | - | 0.2 | 0.2 | 0.4 | 0.2 |
| DC_1-3-8-28_n40-n71 | - | - | 0.2 | 0.7 | - | 0.7 |
| DC_1-3-8-28_n40-n77 | - | - | - | - | - | 0.5 |
| DC_1-3-8-28_n71_n77 | 0.2 | 0.2 | 0.2 | 0.7 | 0.7 | 0.5 |
| DC_1-3-8-38_n28-n78 | - | - | 0.2 | - | 0.2 | 0.5 |
| DC_1-3-20-38_n28-n78 | - | - | 0.2 | - | 0.2 | 0.5 |
| DC_1-3-20-40_n28-n78 | - | - | 0.2 | 0.4 | 0.2 | 0.5 |
| DC_1-3-8-41_n1-n41DC_1-3-3-8-41_n1-n41 | - | - | - | 05 / 0.56 | - | 05 / 0.56 |
| DC_1-3-8-41_n1-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_1-7-20-28-32_n3 | - | - | 0.2 | 0.2 | - | - |
| DC_1-7-20-38_n3-n78 | 0.6 | 0.6 | 0.2 | 0.4 | - | 0.8 |
| DC_1-8_n3-n28-n77-n79 | 0.3 | 0.3 | 0.2 | 0.5 | 0.5 | 0.5 |
| DC_1-8-11_n3-n28-n77 | 0.2 | 0.2 | 0.3 | 0.5 | 0.2 | 0.5 |
| DC_1-8-20-38_n28-n78 | - | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_1-8-42_n3-n28-n77 | 0.2 | 0.2 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_2-5-7-66_n2-n66 | 0.3 | - | 0.5 | 0.3 | 0.3 | 0.5 |
| DC_2-5-7-66_n2-n77 | 0.3 | - | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-5-7-66_n2-n78 | 0.3 | - | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-5-7-66_n66-n77 | 0.3 | - | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-7-12-66_n2-n77 | 0.3 | 0.3 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-7-12-66_n2-n66 | 0.5 | 0.5 | 0.5 | 0.3 | 0.3 | 0.5 |
| DC_2-7-12-66_n2-n78 | 0.3 | 0.3 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-7-66-71_n2-n66 | 0.,3 | 0.5 | 0.3 | 0.2 | 0.3 | 0.5 |
| DC_2-7-66-71_n2-n77 | 0.3 | 0.5 | 0.5 | - | 0.3 | 0.5 |
| DC_2-7-12-66_n66-n77 | 0.3 | 0.3 | 0.5 | 0.5 | 0.3 | 0.5 |
| DC_2-7-66-71_n2-n78 | 0.3 | 0.5 | 0.5 | - | 0.3 | 0.5 |
| DC_2-7-66-71_n66-n77 | 0.3 | 0.5 | 0.5 | 0.2 | 0.5 | 0.5 |
| DC_3-7-8-20_n1-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.5 |
| DC_3-7-8-32_n1-n78 | 0.2 | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_3-7-8-40_n1-n78 | 0.2 | - | 0.2 | 0.42 | 0.2 | 0.52 |
| DC_3-7-20-32_n1-n78 | 0.2 | 0.2 | 0.2 | - | 0.2 | 0.5 |
| DC_3-7-28_n1-n40-n78 | 0.2 | 0.3 | 0.2 | 0.2 | 0.8 | 0.5 |
| DC_3-8-20-28_n1-n78 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.8 |
| DC_3-8-20-28-38_n1 | 0.2 | 0.2 | 0.2 | 0.2 | 0.4 | 0.2 |
| DC_3-8-20-28-40_n1 | 0.2 | 0.2 | 0.2 | 0.2 | 0.4 | 0.2 |
| DC_3-8-20-38_n1-n28 | 0.2 | 0.2 | 0.2 | 0.4 | 0.2 | 0.2 |
| DC_3-8-20-40_n1-n28 | 0.2 | 0.2 | 0.2 | 0.4 | 0.2 | 0.2 |
| DC_3-8-20-40_n1-n78 | 0.2 | 0.2 | 0.2 | 0.4 | 0.2 | 0.8 |
| DC_3-20-28-40_n1-n78 | 0.2 | 0.2 | 0.2 | 0.4 | 0.2 | 0.8 |
| DC_3-20-38-40_n1-n28 | 0.2 | 0.2 | 0.4 | 0.4 | 0.2 | 0.2 |
| DC_7-8-20-32-38_n1 | - | 0.2 | 0.2 | - | - | - |
| DC_7-20-28-32-38_n1 | - | 0.2 | 0.2 | - | 0.2 | - |
| NOTE 1: Only applicable for UE supporting inter-band carrier aggregation with uplink in one NR band and without simultaneous Rx/Tx.NOTE 2: Only applicable for UE supporting inter-band carrier aggregation with uplink in one E-UTRA band and without simultaneous Rx/Tx.NOTE 3: “-” denotes ΔRIB,c = 0.NOTE 4: The component band order in the configuration should be listed by the order of E-UTRA band and NR band respectively.NOTE 5: The requirement is applied for UE transmitting on the frequency range of 2515 – 2690 MHz.NOTE 6: The requirement is applied for UE transmitting on the frequency range of 2496 – 2515 MHz. |  |  |  |  |  |  |

#### 7.3B.3.3a Inter-band NE-DC within FR1

Unless ΔRIB,c is specified in this clause, the value of ΔRIB,c for the correspondingly specified EN-DC configuration in clause 7.3B.3.3 is applicable.

Table 7.3B.3.3a.1-1: ΔRIB,c due to NE-DC(two bands)

| Inter-band NE-DC configuration | ΔRIB,c for E-UTRA band / NR band (dB)6 |  |
| --- | --- | --- |
|  | Component band in order of bands in configuration7 |  |
| DC_n40_42 | 0.4 | 0.5 |

#### 7.3B.3.4 Inter-band EN-DC including FR2

##### 7.3B.3.4.1 ΔRIB,c for EN-DC in two bands

Unless otherwise stated, ΔRIB,c for E-UTRA and FR2 NR bands of inter-band EN-DC combinations defined in table 5.5B.5.1-1 is set to zero.

Table 7.3B.3.4.1-1: Void

##### 7.3B.3.4.2 ΔRIB,c for EN-DC three bands

Unless otherwise stated, ΔRIB,c for FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA bands for inter-band EN-DC defined in table 5.5B.5.3-1 is the same as those for the corresponding E-UTRA CA configuration specified in TS 36.101 [4], without the FR2 NR bands.

Table 7.3B.3.4.2-1: Void

##### 7.3B.3.4.3 ΔRIB,c for EN-DC four bands

Unless otherwise stated, ΔRIB,c for FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA bands for inter-band EN-DC defined in table 5.5B.5.3-1 is the same as those for the corresponding E-UTRA CA configuration specified in TS 36.101 [4], without the FR2 NR bands.

Table 7.3B.3.4.3-1: Void

##### 7.3B.3.4.4 ΔRIB,c for EN-DC five bands

Unless otherwise stated, ΔRIB,c for FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA bands for inter-band EN-DC defined in table 5.5B.5.4-1 is the same as those for the corresponding E-UTRA CA configuration specified in TS 36.101 [4], without the FR2 NR bands.

Table 7.3B.3.4.4-1: Void

##### 7.3B.3.4.5 Void

#### 7.3B.3.4a (Void)

#### 7.3B.3.5 Inter-band EN-DC including both FR1 and FR2

##### 7.3B.3.5.2 ΔRIB,c for EN-DC three bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.2-1, ΔRIB,c for constituent FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 7.3B.3.3.

Table 7.3B.3.5.2-1: Void

##### 7.3B.3.5.3 ΔRIB,c for EN-DC four bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.3-1, ΔRIB,c for constituent FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 7.3B.3.3.

##### 7.3B.3.5.4 ΔRIB,c for EN-DC five bands

Unless otherwise stated, for a certain inter-band EN-DC configurations defined in table 5.5B.6.4-1, ΔRIB,c for constituent FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 7.3B.3.3.

##### 7.3B.3.5.5 ΔRIB,c for EN-DC six bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.5-1, ΔRIB,c for constituent FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 7.3B.3.3.

## 7.3E Reference sensitivity for V2X operation in FR1

### 7.3E.1 General

For V2X operation, REFSENS requirements defined in TS 38.101-1 [2] and TS 36.101 [4] apply to all downlink bands of V2X configurations listed in clause 5.5E, unless sensitivity degradation exception is allowed in this clause of this specification, clause 7.3E in TS 38.101-1 [2] or clause 7.3.1G in TS 36.101 [4].

### 7.3E.2 Reference sensitivity for V2X

#### 7.3E.2.1 Intra-band contiguous V2X

For intra-band contiguous V2X listed in Table 5.5E.2-1, the each REFSENS requirements specified in clause 7.3.1G of TS 36.101 [4] and clause 7.3E.2 of TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

#### 7.3E.2.2 Intra-band non-contiguous V2X

For intra-band non-contiguous V2X listed in Table 5.5E.3-1, the each REFSENS requirements specified in clause 7.3.1G of TS 36.101 [4] and clause 7.3E.2 of TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

#### 7.3E.2.3 Inter-band V2X con-current operation

#### 7.3E.2.3.0 General

When UE is configured for NR V2X reception on V2X carrier con-current with E-UTRA uplink and downlink, NR V2X sidelink throughput for the carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.7.2 with parameters specified in table 7.3E.2-1 and 7.3E.2-2 in TS 38.101-1. Also the E-UTRA downlink throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.3 with parameters specified in Table 7.3.1-1 and Table 7.3.1-2 in TS 36.101.

When UE is configured for E-UTRA V2X reception on V2X carrier con-current with NR uplink and downlink, E-UTRA V2X sidelink throughput for the carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.8.2 with parameters specified in Table 7.3.1G-1 in TS 36.101. Also the NR downlink throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2.2, A3.2 and A.3.3 with parameters specified in Table 7.3.2-1a, Table 7.3.2-1b and Table 7.3.2-2 in TS 38.101-1.

The reference sensitivity is defined to be met with all downlink component carriers active. The REFSENS of Uu downlink and PC5 sidelink will be tested at the same time.

Table 7.3E.2.3.0-1: Void

Table 7.3E.2.3.0-2 is specified the additional Rx insertion loss according to different RF architecture with DC/CA UE with same band combinations to reduce the self interference problem based on specific self desense analysis according to specific NR V2X inter-band con-current operation.

Table 7.3E.2.3.0-2: ΔRIB,V2X (two bands)

| V2X inter-band con-current band Combination | E-UTRA or NR Band | ΔRIB,V2X [dB] |
| --- | --- | --- |
| V2X_20_n38 | 20 | 0.01 |
| V2X_n79-47 | n79 | TBD |
|  | 47 | TBD |
| Note 1: The ΔRIB,V2X is applied on top of ΔRIB,c of DC_20_n38 UE that is considered harmonic trap filter to reduce 3rd harmonic impact from Band 20. |  |  |

Table 7.3E.2.3.0-3: Void

Table 7.3E.2.3.0-4: Void

##### 7.3E.2.3.1 Reference sensitivity exception due to UL harmonic problem

Sensitivity degradation is allowed for a band if it is impacted by UL harmonic interference from another band part of the inter-band con-current V2X UE. Reference sensitivity exceptions (MSD) for the victim band (high) are specified in Table 7.3E.2.3.1-1 with uplink configuration of the aggressor band (low) specified in Table 7.3E.2.3.1-2.

Table 7.3E.2.3.1-1: Reference sensitivity exceptions (MSD) due to UL harmonic for inter-band con-current operation

| V2X inter-band con-current band combinations | Operating Bands / Channel bandwidth of the affected DL band / MSD |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| V2X_20_n38 | UL band | SL operation | 10 MHz(dB) | 20 MHz(dB) | 30 MHz (dB) | 40 MHz(dB) |
|  | 20 | n38 | 10.7 | 7.7 | 5.8 | 4.7 |
| NOTE 1: These requirements apply when there is at least one individual RE within the uplink transmission bandwidth of the aggressor (lower) for which the 3rd transmitter harmonic is within the sidelink transmission bandwidth of a victim (higher) band.NOTE 2: The requirements should be verified for UL EARFCN of the aggressor (lower) band (superscript LB such that ![](media_svg/image11.svg) [公式≈: ff_{ULDL}^{LBHB}=⋅∂_{√∃}/0.30.1] in MHz and ![](media_svg/image10.svg) [公式≈: ^{FBWfFBW}ULlowChannelULULhighChannel^{LBLBLBLBLB}__^{+≥≥−}^{/2/2}] with ![](media_svg/image28.svg) [公式≈: _{f}_{DL}HB]the carrier frequency in the victim (higher) band in MHz and ![](media_svg/image29.svg) [公式≈: ^{BW}Channel^{LB}] the channel bandwidth configured in the low band.NOTE 3: The MSD level applied to all supported SCSs in victim band. |  |  |  |  |  |  |

Table 7.3E.2.3.1-2: Uplink configuration for reference sensitivity exceptions due to UL harmonic interference for inter-band con-current V2X in NR FR1

| E-UTRA or NR Band / Channel bandwidth of the affected DL band / UL RB allocation of the agressor band |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| UL band | SL operation | 10MHz(LCRB) | 20 MHz(LCRB) | 30 MHz(LCRB) | 40 MHz(LCRB) |
| 20 | n38 | 25 | 50 | 50 | 50 |
| NOTE 1: The UL configuration applies regardless of the channel bandwidth of the UL band unless the UL resource blocks exceed that specified in Table 7.3.1-2 in TS 36.101 [4] or Table 7.3.2-3 in TS 38.101-1 [2] for the uplink bandwidth in which case the allocation according to Table 7.3.1-2 in TS 36.101 [4] or Table 7.3.2-3 in TS 38.101-1 [2] applies |  |  |  |  |  |

## 7.4 Void

## 7.4A Maximum input level for CA

For inter-band NR CA between FR1 and FR2, the maximum input level specified in TS 38.101-1 [2] and TS38.101-2[3] apply for FR1 and FR2 respectively.

## 7.4B Maximum input level for DC in FR1

### 7.4B.1 Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC maximum input level requirement and parameters are defined in Table 7.4B.1-1.

Table 7.4B.1-1: Maximum Input

| Power in Largest CC, E-UTRA or NR, dBm | X1 |
| --- | --- |
| Power in each other CC, dBm | X1 – 10*log10(NxSCSx/NySCSy) |
| NOTE 1: Power in Largest E-UTRA or NR bandwidth CC, listed in Table 7.4-1 [2]NOTE 2: Nx, SCSx is the number of RB's and Sub carrier spacing in the largest carrier bandwidth and could be E-UTRA or NR carrierNOTE 3: Ny, SCSy is the number of RB's in any other carrier.NOTE 4: Void.NOTE 5: Void. |  |

### 7.4B.1a (Void)

### 7.4B.2 Intra-band non-contiguous EN-DC in FR1

For the E-UTRA sub-block containing one or multiple CC's, the requirement is defined in clause 7.4.1 for single carrier operation and in clause 7.4.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.4 in TS 38.101-1 [2].

### 7.4B.3 Inter-band EN-DC within FR1

Maximum input level requirement for E-UTRA single carrier and CA operation specified in clauses 7.4.1 and 7.4.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.4 and 7.4A of TS 38.101-1[2] apply.

### 7.4B.3a (Void)

### 7.4B.4 Inter-band EN-DC including FR2

Maximum input level requirement for E-UTRA single carrier and CA operation specified in clauses 7.4.1 and 7.4.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.4, 7.4A and 7.4B of TS38.101-2 [3] apply.

### 7.4B.4a (Void)

### 7.4B.5 Inter-band EN-DC including both FR1 and FR2

Maximum input level requirement for E-UTRA single carrier and CA operation specified in clauses 7.4.1 and 7.4.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.4, 7.4A and 7.4B of TS38.101-1 [2] and TS 38.101-2 [3] apply.

## 7.4E Maximum input level for V2X operation in FR1

For intra-band V2X UE, the maximum input requirements specified in clause 7.4.1G of TS 36.101 [4] and clause 7.4E.2 of TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

For the inter-band con-current NR V2X operation, the requirements specified in subclause 7.4E of TS 38.101-1 [2] shall apply for the NR sidelink reception in Band n47 and the requirements specified in subclause 7.4.1 of TS 36.101 [4] shall apply for the E-UTRA downlink reception in licensed band while all downlink carriers are active.

## 7.5 Void

## 7.5A Adjacent channel selectivity for CA

For inter-band NR CA between FR1 and FR2, the adjacent channel selectivity specified in TS 38.101-1 [2] and TS38.101-2 [3] apply for FR1 and FR2 respectively.

## 7.5B Adjacent channel selectivity for DC in FR1

### 7.5B.1 Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC ACS requirement and parameters are defined for test case 1 in Table 7.5B.1-1 and for test case 2 in Table 7.5B.1-2.

Table 7.5B.1-1: ACS test case 1

| EN-DC Aggregated Bandwidth, MHz | <=100 | >100, <=120 | >120, <=140 | >140, <=160 |
| --- | --- | --- | --- | --- |
| ACS, dB | X1 | 19.2 | 18.5 | 17.9 |
| Pinterferer, dBm | PI 2 | Aggregated power + 17.7 dB | Aggregated power + 17 dB | Aggregated power + 16.4dB |
| Pw in Transmission BW configuration, per CC, dBm | REFSENS +14dB |  |  |  |
| NOTE 1: X is ACS level at the specified EN-DC aggregated bandwidth from Table 7.5.1A-1 in TS 36.101 [4]NOTE 2: PI is from Table 7.5.1A-2 in TS 36.101 [4]NOTE 3: Jammer BW and offset is from Table 7.5.1A-2 [4] and is applied from the lowest edge of the lowest carrier and the highest edge of the highest carrierNOTE 4: Void.NOTE 5: Void. |  |  |  |  |

Table 7.5B.1-2: ACS test case 2

| EN-DC Aggregated Bandwidth, ENBW, MHz | ≤100 | >100, ≤120 | >120, ≤140 | >140, ≤160 |
| --- | --- | --- | --- | --- |
| Pw in Transmission Bandwidth Configuration, perCC, dBm | PW 1 | -42.7 +10log10(NRB,c/ NRB_agg) | -42 +10log10(NRB,c/ NRB_agg) | -41.4 +10log10(NRB,c/ NRB_agg) |
| Pinterferer, dBm | -25 |  |  |  |
| NOTE 1: PW is wanted signal power level at the specified EN-DC aggregated Bandwidth from Table 7.5.1A-3 in TS 36.101 [4]NOTE 2: Jammer BW and offset is from Table 7.5.1A-3 [4] and is applied from the lowest edge of the lowest carrier and the highest edge of the highest carrierNOTE 3: Void.NOTE 4: Void. |  |  |  |  |

### 7.5B.1a (Void)

### 7.5B.2 Intra-band non-contiguous EN-DC in FR1

For the E-UTRA sub-block containing one or multiple CC's, the requirement is defned in clause 7.5.1 for single carrier operation and in clause 7.5.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.5 in TS 38.101-1 [2].

The blocker configuration is defined in the general clause 7.1.

### 7.5B.3 Inter-band EN-DC within FR1

Adjacent channel selectivity requirement for E-UTRA single carrier and CA operation specified in clauses 7.5.1 and 7.5.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.5 and 7.5A of TS 38.101-1 [2] apply.

### 7.5B.3a (Void)

### 7.5B.4 Inter-band EN-DC including FR2

Adjacent channel selectivity requirement for E-UTRA single carrier and CA operation specified in clauses 7.5.1 and 7.5.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.5, 7.5A and 7.5B of TS38.101-2 [3] apply.

### 7.5B.4a (Void)

7.5B.5 Inter-band EN-DC including both FR1 and FR2

Adjacent channel selectivity requirement for E-UTRA single carrier and CA operation specified in clauses 7.5.1 and 7.5.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.5, 7.5A and 7.5Bof TS38.101-1 [2] and TS 38.101-2 [3] apply.

## 7.5E Adjacent channel selectivity for V2X operation in FR1

For intra-band V2X operation, the adjacent channel selectivity specified in clause 7.5.1G in TS 36.101 [4] and specified in clause 7.5C in TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

For the inter-band con-current NR V2X operation, the requirements specified in subclause 7.5E of TS 38.101-1 [2] shall apply for the NR sidelink reception in Band n47 and the requirements specified in subclause 7.5.1 of TS 36.101 [4] shall apply for the E-UTRA downlink reception in licensed band while all downlink carriers are active.

## 7.6 Void

## 7.6A Blocking characteristics for CA

For inter-band NR CA between FR1 and FR2, the in-band blocking characteristics specified in TS 38.101-1 [2] and TS38.101-2 [3] apply for FR1 and FR2 respectively. The narrow band blocking and out-of-band blocking specified in TS 38.101-1 [2] apply for FR1.

## 7.6B Blocking characteristics for DC in FR1

### 7.6B.1 General

### 7.6B.2 In-band blocking for DC in FR1

#### 7.6B.2.1 Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC in-band blocking requirement and parameters are defined in Table 7.6B.2.1-1.

Table 7.6B.2.1-1: In-band blocking

| EN-DC Aggregated Bandwidth, MHz | ≤100 | >100, ≤120 | >120, ≤140 | >140, ≤160 |
| --- | --- | --- | --- | --- |
| Pw in Transmission Bandwidth Configuration, perCC, dBm |  | REFSENS + Aggregated BW specific value below |  |  |
|  | PW 1 | 16.8 | 17.5 | 18 |
| NOTE 1: PW is wanted signal power level at the specified EN-DC aggregated Bandwidth from Table 7.6.1.1A-1 in TS 36.101 [4]NOTE 2: Interferer values are specified from Table 7.6.1.1A-2 in TS 36.101 [4]NOTE 3: Jammer BW and offset is from Table 7.6.1.1A-1 [4] and is applied from the lowest edge of the lowest carrier and the highest edge of the highest carrierNOTE 4: Void.NOTE 5: Void. |  |  |  |  |

#### 7.6B.2.1a (Void)

#### 7.6B.2.2 Intra-band non-contiguous EN-DC in FR1

For the E-TRA sub-block containing one or multiple CC's, the requirement is deined in clause 7.6.1.1 for single carrier operation and in clause 7.6.1.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.6.2 in TS 38.101-1 [2].

The blocker configuration is defined in the general clause 7.1.

#### 7.6B.2.3 Inter-band EN-DC within FR1

Inband blocking requirement for E-UTRA single carrier and CA operation specified in clauses 7.6.1.1 and 7.6.1.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.2 and 7.6A.2 of TS 38.101-1 [2] apply.

#### 7.6B.2.3a (Void)

#### 7.6B.2.4 Inter-band EN-DC including FR2

Inband blocking requirement for E-UTRA single carrier and CA operation specified in clauses 7.6.1.1 and 7.6.1.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.2, 7.6A.2 and 7.6B.2 of TS38.101-2 [3] apply.

#### 7.6B.2.4a (Void)

#### 7.6B.2.5 Inter-band EN-DC including both FR1 and FR2

Inband blocking requirement for E-UTRA single carrier and CA operation specified in clauses 7.6.1.1 and 7.6.1.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.2, 7.6A.2 and 7.6B.2 of TS38.101-1 [2] and TS 38.101-2 [3] apply.

#### 7.6B.2.6 Void

Table 7.6B.2.6-1: Void

Table 7.6B.2.6-2: Void

### 7.6B.3 Out-of-band blocking for DC in FR1

#### 7.6B.3.1 Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC out-of-band requirement and parameters are defined in Table 7.6B.3.1-1.

Table 7.6B.3.1-1: Out-of-band blocking

| EN-DC Aggregated Bandwidth, MHz | ≤100 | >100, ≤120 | >120, ≤140 | >140, ≤160 |
| --- | --- | --- | --- | --- |
| Pw in Transmission Bandwidth Configuration, perCC, dBm | REFSENS + Aggregated BW specific value below |  |  |  |
|  | 9 |  |  |  |
| NOTE 1: Interferer values and offsets are specified from Table 7.6.2.1A-2 in TS 36.101 [4]NOTE 2: Void.NOTE 3: Void. |  |  |  |  |

For Table .1A-2 from TS 36.101 [4] in frequency range 1, 2 and 3, up to ![](media_svg/image30.svg) [公式≈: max(24,6∪_{⊥}N_{RB}∪/6_{∀})]exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a 1MHz step size. For these exceptions the requirements of subclause 7.7B.1 Spurious response are applicable.

#### 7.6B.3.1a (Void)

#### 7.6B.3.2 Intra-band non-contiguous EN-DC in FR1

For the E-UTRA sub-block containing one or multiple CC's, the requirement is dfined in clause 7.6.2.1 for single carrier operation and in clause 7.6.2.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.6.3 is [2].

#### 7.6B.3.3 Inter-band EN-DC within FR1

Out-of band blocking requirements for E-UTRA single carrier and CA operation specified in clauses 7.6.2.1 and 7.6.2.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.3 and 7.6A.3 of TS 38.101-1 [2] apply for lowest level EN-DC fallbacks (two bands) in clause 5.5B.4.1 with following conditions

- one E-UTRA uplink carrier with the output power set to 4 dB below PCMAX_L,c and the NR band whose downlink is being tested has its uplink carrier output power set to 29 dB below PCMAX_L,f,c.

- one NR uplink carrier with the output power set to 4 dB below PCMAX_L,f,c on the NR band with both E-UTRA and NR downlinks being tested with E-UTRA output power set to 29 dB below PCMAX_L,c.

If CW interferer falls in a gap between FDL_high of the E-UTRA or NR band and FDL_low of the NR or EUTRA band, where the corresponding OOB ranges 1 and 2 overlap, then the lower level interferer limit of the overlapping OOB ranges applies.

If FDL_high of the lower E-UTRA or NR band is greater than or equal to the FDL_low of the upper NR or E-UTRA band as in overlapping RX frequency ranges, then the OOB range shall start from the FDL_low of the lower E-UTRA or NR band, and from the FDL_high of the upper NR or E-UTRA band.

For ENDC combination listed in Table 7.6B.3.3-1 under the first test condition above, exceptions to the requirement specified in Table 7.6B.3.3-2 are allowed when the second order intermodulation product of the lower frequency band UL carrier and the CW interfering signal fully or partially overlaps with the higher frequency band DL carrier.

Table 7.6B.3.3-1: ENDC combination with exceptions allowed

| EN-DC combination |
| --- |
| DC_5_n77 |
| DC_5_n78 |
| DC_8_n77 |
| DC_8_n78 |
| DC_8_n79 |
| DC_11_n77 |
| DC_13_n77 |
| DC_18_n77 |
| DC_18_n78 |
| DC_18_n79 |
| DC_19_n77 |
| DC_19_n78 |
| DC_19_n79 |
| DC_20_n77 |
| DC_20_n78 |
| DC_21_n77 |
| DC_26_n77 |
| DC_26_n78 |
| DC_26_n79 |
| DC_28_n77 |
| DC_28_n78 |
| DC_28_n79 |

| Parameter | Unit | Level |
| --- | --- | --- |
| PInterferer (CW) | dBm | -441 |
| NOTE 1: The requirement applies when $\left \| f_{Interferer}\pm  f_{UL}^{LB}-f_{DL}^{HB}\right \| \leq  (BW_{UL}^{LB}+BW_{DL}^{HB})/2 $, where $ f_{UL}^{LB}$ and $ f_{DL}^{HB}$ are the carrier frequencies for lower frequency band UL and higher frequency band DL, respectively. $ BW_{UL}^{LB}$ and $ BW_{DL}^{HB}$ are the channel bandwidths configured for lower frequency band UL carrier and higher frequency band DL carrier in MHz, respectively. |  |  |

For each of the two test cases in clauses 7.6.2.1 and 7.6.2.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.3 and 7.6A.3 of TS 38.101-1 [2] for all interferer frequency ranges a maximum of

![](media_svg/image31.svg) [公式≈: _{√}max{24,6∪_{⊥}n∪N_{RB}/6_{∀}}min{_{√}n∪N_{RB}/10_{∃},5}_{∃}]

exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a step size of ![](media_svg/image32.svg) [公式: min(_{√}CBW/2_{∃},5)] MHz with NRB the number of resource blocks in the downlink transmission bandwidth configuration, CBW the bandwidth of the frequency channel in MHz and n = 1, 2, 3 for SCS = 15, 30, 60 kHz, respectively. For these exceptions, the requirements in clause 7.7 apply.

#### 7.6B.3.3a (Void)

#### 7.6B.3.4 Inter-band EN-DC including FR2

Out-of band blocking requirements specified for E-UTRA single carrier and CA operation specified in clauses 7.6.2.1 and 7.6.2.1A of TS 36.101 [4] apply for lowest level EN-DC fallbacks (two bands) in clause 5.5B.5.1 with only E-UTRA UL with output power as in TS 36.101 [4] (4 dB below PCMAX_L).

#### 7.6B.3.4a (Void)

#### 7.6B.3.5 Inter-band EN-DC including both FR1 and FR2

Out-of band blocking requirements specified for E-UTRA single carrier and CA operation specified in clauses 7.6.2.1 and 7.6.2.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.3 and 7.6A.3 of TS 38.101-1 [2] apply for lowest level EN-DC fallbacks (three bands) in clause 5.5B.6.2 with only E-UTRA UL with output power as in TS 36.101 [4] (4 dB below PCMAX_L).

### 7.6B.4 Narrow band blocking for DC in FR1

#### 7.6B.4.1 Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC narrow band blocking requirement and parameters are defined in Table 7.6B.4.1-1.

Table 7.6B.4.1-1: Narrow band blocking parameters

| EN-DC Aggregated Bandwidth, MHz | ≤100 | >100, ≤120 | >120, ≤140 | >140, ≤160 |
| --- | --- | --- | --- | --- |
| Pw in Transmission Bandwidth Configuration, perCC, dBm | REFSENS + Aggregated BW specific value below |  |  |  |
|  | 16 |  |  |  |
| PUW, dBm (CW) | -55 |  |  |  |
| NOTE 1: Jammer offset is from Table 7.6.3.1A-1 [4] and is applied from the lowest edge of the lowest carrier and the highest edge of the highest carrierNOTE 2: Void.NOTE 3: Void.NOTE 4: If NR carrier BW > 40 MHz, no narrow band blocking requirements apply when blocker is applied at the edge of the NR carrier. |  |  |  |  |

#### 7.6B.4.1a (Void)

#### 7.6B.4.2 Intra-band non-contiguous EN-DC in FR1

For the E-TRA sub-block containing one or multiple CC's, the requirement is deined in clause 7.6.3.1 for single carrier operation and in clause 7.6.3.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.6.4 in TS 38.101-1 [2].

The blocker configuration is defined in the general clause 7.1.

#### 7.6B.4.3 Inter-band EN-DC within FR1

Narrow band blocking requirement for E-UTRA single carrier and CA operation specified in clauses 7.6.3.1 and 7.6.3.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.4 and 7.6A.4 of TS38.101-1 [2] apply.

#### 7.6B.4.3a (Void)

#### 7.6B.4.4 Inter-band EN-DC including FR2

Narrow band blocking requirement for E-UTRA single carrier and CA operation specified in clauses 7.6.3.1 and 7.6.3.1A of TS 36.101 [4] apply.

#### 7.6B.4.4a (Void)

#### 7.6B.4.5 Inter-band EN-DC including both FR1 and FR2

Narrow band blocking requirement for E-UTRA single carrier and CA operation specified in clauses 7.6.3.1 and 7.6.3.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.4 and 7.6A.4 of TS38.101-1 [2] apply.

## 7.6E Blocking characteristics for V2X in FR1

For intra-band V2X operation, the blocking charateristics specified in clause 7.6.1.1G in TS 36.101 [4] and specified in clause 7.6E in TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

For inter-band con-current NR V2X operation, the in-band blocking and out of band blocking requirement specified in clause 7.6E in TS 38.101-1 [2] shall apply on NR V2X carrier and the requirement specified in clause 7.6 in TS 36.101 [4] shall apply for the E-UTRA downlink reception in licensed band while all downlink carriers are active. PInterferer power is increased by ΔRIB,c in the requirement.

No narrow band blocking requirement applied for NR V2X carrier.

## 7.7 Void

## 7.7A Spurious response for CA

For inter-band NR CA between FR1 and FR2, the spurious response specified in TS 38.101-1 [2] apply for FR1.

## 7.7B Spurious response for DC in FR1

### 7.7B.1 Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC spurious response requirement and parameters are defined in Table 7.7B.1-1.

Table 7.7B.1-1: Spurious Response Parameters

| EN-DC Aggregated Bandwidth, MHz | ≤100 | >100, ≤120 | >120, ≤140 | >140, ≤160 |
| --- | --- | --- | --- | --- |
| Pw in Transmission Bandwidth Configuration, perCC, dBm | REFSENS + Aggregated BW specific value below |  |  |  |
|  | 9 |  |  |  |
| Pinterferer, dBm (CW) | -44 |  |  |  |
| NOTE 1: Void.NOTE 2: Void. |  |  |  |  |

### 7.7B.1a (Void)

### 7.7B.2 Intra-band non-contiguous EN-DC in FR1

For the E-UTRA sub-block containing one or multiple CC's, the requirement is defined in clause 7.7.1 for single carrier operation and in clause 7.7.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.7 is [2].

### 7.7B.3 Inter-band EN-DC within FR1

Spurious response requirement for E-UTRA single carrier and CA operation specified in clauses 7.7.1 and 7.7.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.7 and 7.7A of TS 38.101-1 [2] apply for lowest level EN-DC fallbacks (two bands) in clause 5.5.B.4.1 with following conditions

- one E-UTRA uplink carrier with the output power set to 4 dB below PCMAX_L and the NR band whose downlink is being tested has its uplink carrier output power set to 29 dB below PCMAX_L,f,c.

- one NR uplink carrier with the output power set to 4 dB below PCMAX_L,f,c on the NR band with both E-UTRA and NR downlinks being tested with E-UTRA output power set to 29 dB below PCMAX_L,c.

7.7B.3a (Void)

7.7B.4 Inter-band EN-DC including FR2

Spurious response requirement for E-UTRA single carrier and CA operation specified in clauses 7.7.1 and 7.7.1A of TS 36.101 [4] apply for lowest level EN-DC fallbacks (two bands) in clause 5.5B.5.1 with only E-UTRA UL with output power as in TS 36.101 [4] (4 dB below PCMAX_L).

### 7.7B.4a (Void)

### 7.7B.5 Inter-band EN-DC including both FR1 and FR2

Spurious response requirement for E-UTRA single carrier and CA operation specified in clauses 7.7.1 and 7.7.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.7 and 7.7A of TS 38.101-1 [2] apply for lowest level EN-DC fallbacks (three bands) in clause 5.5B.6.2 with only E-UTRA UL with output power as in TS 36.101 [4] (4 dB below PCMAX_L).

## 7.7E Spurious response for V2X in FR1

For intra-band V2X operation, the spurious response specified in clause 7.7.1G in TS 36.101 [4] and specified in clause 7.7E in TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

For the inter-band con-current NR V2X operation, the requirements specified in subclause 7.7E of TS 38.101-1 [2] shall apply for the NR sidelink reception in Band n47 and the requirements specified in subclause 7.7.1 of TS 36.101 [4] shall apply for the E-UTRA downlink reception in licensed band while all downlink carriers are active.

## 7.8 Void

## 7.8A Intermodulation characteristics for CA

For inter-band NR CA between FR1 and FR2, the intermodulation characteristics specified in TS 38.101-1 [2] apply for FR1.

## 7.8B Intermodulation characteristics for DC in FR1

### 7.8B.1 General

### 7.8B.2 Wide band Intermodulation

#### 7.8B.2.1 Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC wide band intermodulation requirement and parameters are defined in Table 7.8B.2.1-1.

Table 7.8B.2.1-1: Wide band intermodulation

| EN-DC Aggregated Bandwidth, MHz | <=100 | >100, <=120 | >120, <=140 | >140, <=160 |
| --- | --- | --- | --- | --- |
| Pw in Transmission Bandwidth Configuration, perCC, dBm | PW 1 | REFSENS + Aggregated BW specific value below |  |  |
|  |  | 16.8 | 17.5 | 18.0 |
| Pinterferer 1, dBm (CW)2 | -46 |  |  |  |
| Pinterferer 2, dBm (Modulated)2 | -46 |  |  |  |
| NOTE 1: PW is wanted signal power level from Table 7.8.1A-1 in TS 36.101 [4]NOTE 2: Jammer BW and offsets is from Table 7.8.1A-1 [4] and is applied from the lowest edge of the lowest carrier and the highest edge of the highest carrierNOTE 3: Void.NOTE 4: Void. |  |  |  |  |

#### 7.8B.2.1a (Void)

#### 7.8B.2.2 Intra-band non-contiguous EN-DC in FR1

For the E-UTRA sub-block containing one or multiple CC's, the requirement is defined in clause 7.8.1 for single carrier operation and in clause 7.8.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.8.2 in TS 38.101-1 [2].

The blocker configuration is defined in the general clause 7.1 and the requirement only apply for out of gap interferers.

#### 7.8B.2.3 Inter-band EN-DC within FR1

Wide band Intermodulation requirement for E-UTRA single carrier and CA operation specified in clauses 7.8.1 and 7.8.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.8.2 and 7.8A.2 of TS38.101-1 [2] apply.

#### 7.8B.2.3a (Void)

#### 7.8B.2.4 Inter-band EN-DC including FR2

Wide band Intermodulation requirement for E-UTRA single carrier and CA operation specified in clauses 7.8.1 and 7.8.1A of TS 36.101 [4] apply.

#### 7.8B.2.4a (Void)

#### 7.8B.2.5 Inter-band EN-DC including both FR1 and FR2

Wide band Intermodulation requirement for E-UTRA single carrier and CA operation specified in clauses 7.8.1 and 7.8.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.8.2 and 7.8A.2 of TS38.101-1 [2] apply.

## 7.8E Intermodulation characteristics for V2X operation in FR1

For intra-band V2X operation, the intermodulation characteristics specified in clause 7.8.1G in TS 36.101 [4] and specified in clause 7.8E in TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

For inter-band NR V2X con-current operation, the wideband inter-modulation requirement specified in clause 7.8E in TS 38.101-1 [2] shall apply on NR V2X carrier and the requirement specified in clause 7.8.1 in TS 36.101 [4] shall apply on E-UTRA downlink reception in licensed band while all downlink carriers are active. PInterferer power is increased by ΔRIB,c in the requirement.

## 7.9 Void

## 7.9A Spurious emissions for CA

For inter-band NR CA between FR1 and FR2, the spurious emission specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for FR1 and FR2 respectively.

## 7.9B Spurious emissions for DC in FR1

### 7.9B.1 Intra-band contiguous EN-DC in FR1

The requirement is defined in clause 7.9A.1 in TS 38.101-1 [2].

### 7.9B.1a (Void)

### 7.9B.2 Intra-band non-contiguous EN-DC in FR1

Spurious emissions requirement for E-UTRA single carrier and CA operation specified in clauses 7.9.1 and 7.9.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.9 and 7.9A of TS 38.101-1 [2] apply.

### 7.9B.3 Inter-band EN-DC within FR1

E-UTRA requirements from TS 36.101 [4] and NR requirements from TS 38.101-1 [2] apply.

### 7.9B.3a (Void)

### 7.9B.4 Inter-band EN-DC including FR2

Spurious emissions requirement for E-UTRA single carrier and CA operation specified in clauses 7.9.1 and 7.9.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 7.9 of TS 38.101-2 [3] apply.

### 7.9B.4a (Void)

7.9B.5 Inter-band EN-DC including both FR1 and FR2

Spurious emissions requirement for E-UTRA single carrier and CA operation specified in clauses 7.9.1 and 7.9.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.9 and 7.9A of TS 38.101-1 [2] and TS 38.101-2 [3] apply.

## 7.10 Void

## 7.10A Void

## 7.10B Power imbalance for DC in FR1

### 7.10B.1 General

Power imbalance requirement is a measure of the receiver’s ability to receive a wanted signal (E-UTRA or NR) in the presence of another carrier signal (E-UTRA or NR) with 6 - 25dB power imbalance at a specific frequency offset from the wanted signal.

Power imbalance requirement in subclause 7.10B.3 is applicable for:

- A UE capable of interBandMRDC-WithOverlapDL-Bands-r16 and not capable of requirementTypeIndication-r18 or a UE capable of interBandMRDC-WithOverlapDL-Bands-r16 and requirementTypeIndication-r18 but is not provided with nonCollocatedTypeMRDC and is configured with maxMIMO-Layerswith value less than or equal to 2; or,

- A UE capable of interBandMRDC-WithOverlapDL-Bands-r19 and nonCollocatedTypeMRDC-v1900 is provided with value type4 and is configured with maxMIMO-Layers equal to four.

### 7.10B.3 Inter-band EN-DC within FR1

For these test parameters in table 7.10B.3-1, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1 in 38.101-1).

Table 7.10B.3-1: Test parameters for FDD-FDD or TDD-TDD inter-band EN-DC operation with overlapping or partially overlapping DL bands

| Test configurations | Carriers | Rx Power in transmission bandwidth configuration (dBm) | channel bandwidth | Frequency relationship(Center of BWanother Relative to edge of BWwanted) |
| --- | --- | --- | --- | --- |
| 1 | Wanted carrier | REFSENS + 1 | BWwanted ≤ BWanother | < max (5/2* BWanother, 50MHz) |
|  | Another wanted carrier with overlapping DL bands | Power of wanted carrier + 25 |  |  |
| 2 | Wanted carrier | REFSENS + 1 | BWwanted > BWanother |  |
|  | Another wanted carrier with overlapping DL bands | Power of wanted carrier + 25 – 10*log10(BWwanted /BWanother) |  |  |
| 3 | Wanted carrier | REFSENS + 1 | NA | ≥ max (5/2* BWanother, 50MHz) |
|  | Another wanted carrier with overlapping DL bands | Power of wanted carrier + 25 |  |  |
| NOTE 1: For NR carrier, the transmitter shall be set to 24dB below PCMAX_L,f,c,NR at the minimum uplink configuration specified in Table 7.3.2-3 [2] with PCMAX_L,f,c,NR as defined in clause 6.2B.4.NOTE 2: For E-UTRA carrier, the transmitter shall be set to 24 dB below PCMAX_L_E-UTRA,c at the minimum uplink configuration specified in Table 7.3.1-2 [4] with PCMAX_L_E-UTRA,c as defined in clause 6.2B.4 for single carrier.NOTE 3: BWwanted is the channel bandwidth of wanted carrier. BWanother is the channel bandwidth of another wanted carrier with overlapping DL bandsNOTE 4: When a UE reports interBandMRDC-WithOverlapDL-Bands-r16, the REFSENS is the reference sensitivity level of two antenna ports in Table 7.3.2-1a or in Table 7.3.2-1b of TS 38.101-1, or in Table 7.3.1-1 of TS 36.101. When a UE reports interBandMRDC-WithOverlapDL-Bands-r19, the REFSENS is the reference sensitivity level of four antenna ports in Table 7.3.2-1b of TS 38.101-1, which is modified by the amount of ΔRIB,4R  given in Table 7.3.2-2 of TS 38.101-1, or in Table 7.3.1-1 of TS 36.101, which is modified by the amount of ΔRIB,4R  given Table 7.3.1-1a of TS 36.101.NOTE 5: For TDD-TDD combination, the minimum requirements apply only when there is non-simultaneous Rx/Tx operation between E-UTRA and NR carriers for the EN-DC combinations in Table 7.10B.3-2. This restriction applies also for these carriers when applicable EN-DC configuration is part of a higher order EN-DC configuration.NOTE 6: For Inter-band EN-DC configurations with multiple contiguous E-UTRA CCs in one band, REFSENS in this table equals to 5MHz REFSENS+10*log(aggregated BW(MHz)/5) of all the contiguous E-UTRA CCs of the wanted band. BWwanted and BWanother represent the aggregated BWs of all the CCs of the wanted and another band, respectively. The maximum power spectral density imbalance between the contiguous E-UTRA CCs in one band, is within 6 dB.”NOTE 7:   Only FWA UE is intended for supporting interBandMRDC-WithOverlapDL-Bands-r19. |  |  |  |  |

It’s allowed to use only one of the test configurations to verify the RX power imbalance requirement for a UE indicating capability interBandMRDC-WithOverlapDL-Bands-r16.

If the UE indicates interBandMRDC-WithOverlapDL-Bands-r16 but does not indicate requirementTypeIndication-r18 or a UE indicates both interBandMRDC-WithOverlapDL-Bands-r16 and requirementTypeIndication-r18 and IE nonCollocatedTypeMRDC is not provided when maxMIMO-Layerswith value less than or equal to 2, the Rx requirements for two Rx ports are applicable  for each band in EN-DC operating mode for the following EN-DC band combinations in Table 7.10B.3-2.

For NR and EUTRA component carriers for the EN-DC band combinations in Table 7.10B.3-2, if the UE indicates interBandMRDC-WithOverlapDL-Bands-r19 and nonCollocatedTypeMRDC-v1900 is provided with value type4,

When the UE is provided with maxMIMO-Layers equals to four and maxLayersMIMO equals to two, the Rx requirements for four and two Rx ports are applicable for NR and EUTRA component carriers, repectively.

When UE is provided with maxMIMO-Layers and maxLayersMIMO equal to four, the Rx requirements for four Rx ports are applicable.

Table 7.10B.3-2: TDD-TDD ENDC combinations

| EN-DC combination |
| --- |
| DC_42_n771 |
| DC_42_n781 |
| NOTE 1: These combinations are not used alone as a fall-back mode of another band combination in which the UL in Band 42 is not used. |
