# TS 38.101 38101-3-j60_s06-XX

## 6Transmitter characteristics

## 6.1General

Unless otherwise stated the transmitter characteristics are specified at the antenna connector(s) of the UE for the bands operating on frequency range 1 and over the air of the UE for the bands operating on frequency range 2. The requirements for frequency range 1 and frequency range 2 can be verified separately. For the carrier in frequency range 1, requirements can be verified with NR FR2 link disabled. For the carrier in frequency range 2, requirements can be verified in OTA mode with E-UTRA or NR FR1 connecting to the network by OTA without calibration.

Unless otherwise stated, requirements for NR transmitter written in TS 38.101-1 [2] and TS 38.101-2 [3] apply and are assumed anchor agnostic. Requirements are verified under conditions where anchor resources do not interfere NR operation. If UE indicates IE powerClassNRPart-r16 as defined in TS 38.331 [9] in EN-DC, UE shall meet NR requirements according to this power class.

For sub-clauses with suffix A or B: the minimum requirements for band combinations including Band n41 also apply for the corresponding band combinations with Band n90 replacing Band n41 but with otherwise identical parameters. For brevity the said band combinations with Band n90 are not listed in the tables below but are covered by this specification.

## 6.2Void

## 6.2ATransmitter power for CA

## 6.2A.1UE maximum output power for CA

## 6.2A.1.1Inter-band CA between FR1 and FR2

Table 6.2A.1.1-1: Void

For inter-band NR CA in FR1 and FR2 combined, the UE shall meet each transmitter power requirement specified in TS 38.101-1 [2] and TS 38.101-2 [3] for each frequency range independently.

## 6.2A.2UE maximum output power reduction for CA

## 6.2A.2.1Inter-band CA between FR1 and FR2

For inter-band NR CA between FR1 and FR2, UE maximum output power reduction specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for each frequency range respectively.

## 6.2A.3UE additional maximum output power reduction for CA

For inter-band NR CA between FR1 and FR2, UE additional maximum output power reduction specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for each frequency range respectively.

## 6.2A.4Configured output power for CA

## 6.2A.4.1Configured output power level

For inter-band NR CA between FR1 and FR2, UE configured output power specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for each frequency range respectively.

For inter-band NR CA between FR1 and FR2 with a single uplink component carrier configured in FR1, when the powerBoostPi2BPSK-r18 or powerBoostQPSK-r18 is set to 1 for a UE supporting the capability of powerBoosting-pi2BPSK-QPSK-Modified-r18 or powerBoosting-pi2BPSK-QPSK-r18, the configured maximum output power PCMAX,c  on serving cell c shall be set as specified for PCMAX,f,c in clause 6.2.4.

## 6.2A.4.2ΔTIB,c for CA

## 6.2A.4.2.1ΔTIB,c for Inter-band CA between FR1 and FR2

Unless otherwise stated, ΔTIB,c for NR FR1 band and FR2 band of inter-band CA defined in table 5.5A.1-1 is set to zero.

Table 6.2A.4.2.1-1: Void

Table 6.2A.4.2.1-2: Void

Table 6.2A.4.2.1-3: Void

## 6.2BTransmitter power for DC

## 6.2B.1UE maximum output power for DC

## 6.2B.1.1Intra-band contiguous EN-DC

The following UE Power Classes define the total maximum output power for any transmission bandwidth(s) of the CG(s) configured.

The maximum output power is measured as the total maximum output power across the UE antenna connector(s). The period of measurement shall be at least one sub frame.

Table 6.2B.1.1-1: Maximum output power for EN-DC (continuous sub-blocks)

If UE supports a different power class than the default UE power class for EN-DC band combination, and the supported power class enables higher maximum output power than that of the default power class:

-if the E-UTRA UL/DL configuration is 0 or 6; or

-if the E-UTRA UL/DL configuration is 1 and special subframe configuration is 0 or 5; or

-if the IE p-maxUE-FR1-r15 as defined in TS 36.331 [8] is provided and set to the maximum output power of the default power class or lower;

-apply all requirements for the default power class, and set the configured transmitted power as specified in clause 6.2B.4;

-else

-if the UE does not support a power class with higher maximum output power than power class 2; or

-if the E-UTRA UL/DL configuration is not 2 or 4 or 5; or

-if the field of UE IE maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.331 is absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than 25% (The exact evaluation period is no less than one radio frame); or

-if the field of UE IE maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-PC2-FR1 (The exact evaluation period is no less than one radio frame); or

-if the IE P-Max as defined in TS 38.331 [9] is provided and set to the maximum output power of the power class 2 or lower;

- apply all requirements for the power class 2 and set the configured transmitted power as specified in clause 6.2B.4;

-else

-apply all requirements for the supported power class, and set the configured transmitted power class as specified in clause 6.2B.4;

## 6.2B.1.1aIntra-band contiguous NE-DC

The following UE Power Classes define the total maximum output power for any transmission bandwidth(s) of the CG(s) configured.

The maximum output power is measured as the total maximum output power across the UE antenna connector(s). The period of measurement shall be at least one sub frame.

Table 6.2B.1.1a-1: Maximum output power for NE-DC (continuous sub-blocks)

## 6.2B.1.2Intra-band non-contiguous EN-DC

Table 6.2B.1.2-1: Maximum output power for EN-DC (non-continuous sub-blocks)

If UE supports a different power class than the default UE power class for EN-DC band combination, and the supported power class enables higher maximum output power than that of the default power class:

-if the E-UTRA UL/DL configuration is 0 or 6; or

-if the E-UTRA UL/DL configuration is 1 and special subframe configuration is 0 or 5; or

-if the IE p-maxUE-FR1-r15 as defined in TS 36.331 [8] is provided and set to the maximum output power of the default power class or lower;

-apply all requirements for the default power class, and set the configured transmitted power as specified in clause 6.2B.4;

-else

-if the UE does not support a power class with higher maximum output power than power class 2; or

-if the E-UTRA UL/DL configuration is not 2 or 4 or 5; or

-if the field of UE IE maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.331 is absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than 25% (The exact evaluation period is no less than one radio frame); or

-if the field of UE IE maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-PC2-FR1 (The exact evaluation period is no less than one radio frame); or

-if the IE P-Max as defined in TS 38.331 [9] is provided and set to the maximum output power of the power class 2 or lower;

- apply all requirements for the power class 2 and set the configured transmitted power as specified in clause 6.2B.4;

-else

-apply all requirements for the supported power class, and set the configured transmitted power class as specified in clause 6.2B.4;

## 6.2B.1.3Inter-band EN-DC within FR1

For inter-band EN-DC of E-UTRA and NR in FR1, the following UE Power Classes define the maximum output power for any transmission bandwidth within the aggregated channel bandwidth. The maximum output power is measured as the sum of the maximum output power at each UE antenna connector. The period of measurement shall be at least one sub frame (1ms). UE maximum output power shall be measured over all component carriers from different bands. If each band has separate antenna connectors, maximum output power is measured as the sum of maximum output power at each UE antenna connector.

The maximum output power for inter-band EN-DC with one Tx per band is specified in Table 6.2B.1.3-1. The per band power class for each band applicable to REFSENS exceptions for a given inter-band UL EN-DC power class are specified in Table 6.2B.3.1-1a. These configurations are subject to the applicable power class of each E-UTRA band and NR band specified in Table 6.2.2-1 of TS 36.101 and Table 6.2.1-1 of TS 38.101-1 respectively. The power classes referenced are according to the reported ue-PowerClass-N-r13 for the E-UTRA band or ue-CA-PowerClass-N for the E-UTRA intra-band UL CA of the EN-DC combination, and reported powerClassNRPart-r16 for the NR band and for NR intra-band UL CA of the EN-DC combination if indicated or ue-PowerClass otherwise.

If higherPowerLimitMRDC-r17 is indicated for an UL inter-band EN-DC configuration as specified in Table 6.2B.1.3-1  and with uplink bands of different power class capabilities, the UE maximum output power specified in Table 6.2B.1.3-1 for this UL EN-DC configuration is modified in accordance with sub-clause 6.2B.4.1.3.

Table 6.2B.1.3-1: Maximum output power for inter-band EN-DC (two bands)

Table 6.2B.1.3-1a: Per band power class applicable to REFSENS exceptions (two band UL EN-DC)

If a UE supports a different power class than the default UE power class for an E-UTRA TDD and NR TDD Inter-band EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

–if the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 30% (The exact evaluation period is no less than one radio frame); or

–if the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is not absent and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS38.331 (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power of the default power class or lower;

–shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified sub-clause 6.2B.4;

–Else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 and larger than or equal to 0.5*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS 38.331; or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 30% and larger than or equal to 15% when maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent. (The exact evaluation period is no less than one radio frame):

–shall apply all requirements for power class 2 and set the configured transmitted power class as specified in sub-clause 6.2B.4.

Else shall apply all requirements for the supported power class and set the configured transmitted power class as specified in sub-clause 6.2B.4.

If a UE supports a different power class than the default UE power class for an E-UTRA FDD and NR TDD EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

If UE indicating the two capabilities maxUplinkDutyCycle-FDD-TDD-EN-DC1 and maxUplinkDutyCycle-FDD-TDD-EN-DC2:

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal tomaxUplinkDutyCycle-FDD-TDD-EN-DC1as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

–shall apply all requirements for the supported power class and set the configured transmitted power class as specified in sub-clause 6.2B.4.

–else

–shall apply all requirements for the default power class and set the configured transmitted power as specified sub-clause 6.2B.4;

else

–shall apply all requirements for the supported power class and set the configured transmitted power as specified sub-clause 6.2B.4;

## 6.2B.1.3aInter-band NE-DC within FR1

For inter-band NE-DC of E-UTRA and NR in FR1, the following UE power classes define the maximum output power for any transmission bandwidth within the aggregated channel bandwidth. The maximum output power is measured as the sum of the maximum output power at each UE antenna connector. The period of measurement shall be at least one sub frame (1 ms). UE maximum output power shall be measured over all component carriers from different bands. If each band has separate antenna connectors, maximum output power is measured as the sum of maximum output power at each UE antenna connector.

Table 6.2B.1.3a-1: Maximum output power for inter-band NE-DC (two bands)

## 6.2B.1.4Inter-band EN-DC including FR2

UE maximum output power requirement for E-UTRA single carrier and CA operation specified in clauses 6.2.2 and 6.2.2A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.2.1, 6.2A.1, and 6.2D.1 of TS 38.101-2 [3] apply.

## 6.2B.1.4a(Void)

## 6.2B.1.5Inter-band EN-DC including both FR1 and FR2

UE maximum output power requirement for E-UTRA single carrier and CA operation specified in clauses 6.2.2 and 6.2.2A of TS 36.101 [4] and for NR single carrier specified in clause 6.2.1 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.2.1, 6.2A.1, and 6.2D.1 of TS 38.101-2 [3] apply. When uplink is EN-DC mode within FR1 only then UE maximum output power requirement is specified in clause 6.2B.1.3 of this specification.

## 6.2B.2UE maximum output power reduction for DC

## 6.2B.2.0General

The UE maximum output power reduction (MPR) specified in this clause is applicable for UEs configured with EN-DC when NS_01 is indicated in the MCG and the SCG. The MPR applies subject to indication in the field modifiedMPRbehavior for the SCG [2].

## 6.2B.2.1Intra-band contiguous EN-DC

## 6.2B.2.1.1General

When the UE is configured for intra-band contiguous EN-DC, the UE determines the total allowed maximum output power reduction as specified in this clause.

For UE supporting dynamic power sharing the following:

-for the MCG, MPRc in accordance with TS 36.101 [4]

-for the SCG,

MPR'c = MPRNR = MAX( MPRsingle,NR, MPRENDC)

-for the total configured transmission power,

MPRtot = PPowerClass,EN-DC – min(PPowerClass,EN-DC ,10*log10(10^((PPowerClass,E-UTRA - MPRE-UTRA)/10) + 10^((PPowerClass,NR - MPRNR)/10))

where

MPRE-UTRA = MAX(MPRsingle,E-UTRA, MPRENDC )

with

-MPRsingle, E-UTRAis the MPR defined for the E-UTRA transmission in TS 36.101 [4]

-MPRsingle,NR is the MPR defined for the NR transmission in TS 38.101-1 [2]

For UEs not supporting dynamic power sharing the following:

-for the MCG,

MPRc = MAX(MPRsingle,E-UTRA, MPRENDC )

-for the SCG,

MPR'c = MAX( MPRsingle,NR, MPRENDC )

where

-MPRsingle,NR is the MPR defined for the NR transmission in TS 38.101-1 [2]

-MPRsingle,E-UTRA is the MPR defined for the E-UTRA transmission in TS 36.101 [4]

MPRENDC is defined in Clause 6.2B.2.1.2

## 6.2B.2.1a(Void)

## 6.2B.2.1.2MPR for power class 3 and power class 2

MPR in this clause is applicable for power class 3 and power class 2 UEs indicating IE dualPA-Architecture supported with EN-DC power class being the same as the E-UTRA and NR power class, otherwise the UE can use as much MPR as needed to fulfil emissions requirements when scheduled with dual uplink transmission. For UEs scheduled with single uplink transmission, MPR in clause 6.2.4 of TS 36.101 [4] and 6.2.2 of TS 38.101-1 [2] apply. For a UE supporting dynamic power sharing for DC_(n)71AA for which dual simultaneous uplink transmissions are mandatory and A-MPR defined in clause 6.2B.3.1.1 is applied as MPR. The allowed maximum output power reduction applied to transmission on the MCG and the SCG is defined as follows:

MPRENDC = MA

Where MA is defined as follows

MA = 15; 0 ≤ B < 0.5

10; 0.5 ≤ B < 1.0

8; 1.0 ≤ B < 2.0

6; 2.0 ≤ B

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

## 6.2B.2.2Intra-band non-contiguous EN-DC

## 6.2B.2.2.1General

When the UE is configured for intra-band non-contiguous EN-DC, the UE determines the total allowed maximum output power reduction as specified in this clause.

For UE supporting dynamic power sharing the following:

-for the MCG, MPRc in accordance with TS 36.101 [4]

-for the SCG,

MPR'c = MPRNR = MAX( MPRsingle,NR, MPRENDC)

-for the total configured transmission power,

MPRtot = PPowerClass,EN-DC – min(PPowerClass,EN-DC ,10*log10(10^((PPowerClass,E-UTRA - MPRE-UTRA)/10) + 10^((PPowerClass,NR - MPRNR)/10))

where

MPRE-UTRA = MAX(MPRsingle,E-UTRA, MPRENDC )

with

-MPRsingle, E-UTRAis the MPR defined for the E-UTRA transmission in TS 36.101 [4]

-MPRsingle,NR is the MPR defined for the NR transmission in TS 38.101-1 [2]

For UEs not supporting dynamic power sharing the following

-for the MCG,

MPRc = MAX(MPRsingle,E-UTRA, MPRENDC )

-for the SCG,

MPR'c = MAX( MPRsingle,NR, MPRENDC )

where

-MPRsingle,NR is the MPR defined for the NR transmission in TS 38.101-1 [2]

-MPRsingle,E-UTRA is the MPR defined for the E-UTRA transmission in TS 36.101 [4]

MPRENDC is defined in Clause 6.2B.2.2.2

## 6.2B.2.2.2MPR for power class 3 and power class 2

MPR in this clause is applicable for power class 3 and power class 2 UEs indicating IE dualPA-Architecture supported with EN-DC power class being the same as the E-UTRA and NR power class, otherwise the UE can use as much MPR as needed to fulfil emissions requirements when scheduled with dual uplink transmission. For UEs scheduled with single uplink transmission, MPR in clause 6.2.4 of TS 36.101 [4] and 6.2.2 of TS 38.101-1 [2] apply.  The allowed maximum output power reduction for IM3 related emissions applied to transmission on the MCG and the SCG is defined as follows:

MPRENDC = MA

Where MA is defined as follows

MA = 18; 0 ≤ B < 1.0

17; 1.0 ≤ B < 2.0

16; 2.0 ≤ B < 5.0

15; 5.0 ≤ B

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

## 6.2B.2.3Inter-band EN-DC within FR1

For inter-band EN-DC between E-UTRA and FR1 NR, UE maximum output power reduction specified in TS 36.101 [4] and TS 38.101-1 [2] apply for E-UTRA and NR respectively.

## 6.2B.2.3aInter-band NE-DC within FR1

For inter-band NE-DC between E-UTRA and FR1 NR, UE maximum output power reduction specified in TS 36.101 [4] and TS 38.101-1 [2] apply for E-UTRA and NR respectively.

## 6.2B.2.4Inter-band EN-DC including FR2

UE maximum output power reduction requirement for E-UTRA single carrier and CA operation specified in clauses 6.2.3 and 6.2.3A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.2.2, 6.2A.2 , and 6.2D.2 of TS 38.101-2 [3] apply.

## 6.2B.2.4a(Void)

## 6.2B.2.5Inter-band EN-DC including both FR1 and FR2

UE maximum output power reduction requirement for E-UTRA single carrier and CA operation specified in clauses 6.2.3 and 6.2.3A of TS 36.101 [4] and for NR single carrier specified in clause 6.2.2 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.2.2, 6.2A.2 , and 6.2D.2 of TS 38.101-2 [3] apply.

## 6.2B.3UE additional maximum output power reduction for EN-DC

## 6.2B.3.1Intra-band contiguous EN-DC

## 6.2B.3.1.0General

For intra-band contiguous EN-DC band combinations with additional requirements the allowed A-MPR is specified in Table 6.2B.3.1.0-1 for UEs configured with EN-DC and combinations of network signalling values indicated in the E-UTRA and NR cell groups.

Unless otherwise stated the A-MPR specified in clause 6.2B.3.1 for intra-band contiguous EN-DC configurations is the total power reduction allowed including MPR.

Table 6.2B.3.1.0-1: Additional maximum power reduction for Intra-band contiguous EN-DC

## 6.2B.3.1.1A-MPR for DC_(n)71AA

For UE supporting dynamic power sharing the following:

-for the MCG, A-MPRc in accordance with TS 36.101 [4]

-for the SCG, A-MPR'c = A-MPRDC

-for the total configured transmission power, A-MPRtot = A-MPRDC

with A-MPRDC as defined in this clause.

For UEs not supporting dynamic power sharing the following

-for the MCG,

A-MPRc = A-MPRE-UTRA

-for the SCG,

A-MPR'c = A-MPRNR

with A-MPRE-UTRA and A-MPRNR as defined in this clause.

For DC_(n)71AA with configured with network signaling values as per Table 6.2B.3.1.0-1 the allowed A-MPR is defined by

-for UE indicating support of dynamicPowerSharing in the UE-MRDC-Capability IE

A-MPRDC = CEIL{ MA,DC (A), 0.5}

where A-MPRDC is the total power reduction allowed (dB),

-for OFDM:

MA,DC =11.00 - 11.67*A;0.00 < A ≤ 0.30

## 8.10 - 2.00*A;0.30 < A ≤ 0.80

6.50;0.80 < A ≤ 1.00

-for DFT-S-OFDM:

MA,DC =11.00 - 13.33*A;  0.00 < A ≤ 0.30

## 8.00 - 3.33*A;   0.30 < A ≤ 0.60

6.00;0.60 < A ≤ 1.00

where

A=LCRB,E-UTRA+LCRB,NRNRB,E-UTRA+NRB,NR

with LCRB, E-UTRA and NRB, E-UTRA the number of allocated PRB and transmission bandwidth for MCG, LCRB,NR and NRB,NR the number of allocated PRB and transmission bandwidth for SCG with SCS = 15 kHz.

-for UE not indicating support of dynamicPowerSharing

A-MPRE-UTRA = CEIL{ MA,E-UTRA , 0.5}

A-MPRNR = CEIL{ MA,NR, 0.5}

where A-MPR is the total power reduction allowed per CG with

MA,E-UTRA=MA,DC(AE-UTRA,wc)-1-E-UTRA

MA,NR=MA,DC(ANR,wc)-1-NR

AE-UTRA,wc=LCRB,E-UTRA+1NRB,E-UTRA+NRB,NR

ANR,wc=1+LCRB,NRNRB,E-UTRA+NRB,NR

∆E-UTRA=10 log10NRB,E-UTRANRB,E-UTRA+NRB,NR

∆NR=10 log10NRB,NRNRB,E-UTRA+NRB,NR

Where LCRB,NR and NRB,NR the number of allocated PRB and transmission bandwidth for SCG with SCS = 15 kHz.

## 6.2B.3.1.2A-MPR for NS_04

6.2B.3.1.2.0General

When the UE is configured for B41/n41 intra-band contiguous EN-DC and it receives IE NS_04, the UE determines the total allowed maximum output power reduction as specified in this clause. The A-MPR for EN-DC defined in this clause is used instead of MPR defined in 6.2B.2.1, not additively, so EN-DC MPR = 0 when NS_04 is signaled. For UEs scheduled with single uplink transmission, AMPR in clause 6.2.4 of [4] and 6.2.3 of [2] apply.

For UE supporting dynamic power sharing the following:

-for the MCG, A-MPRc in accordance with TS 36.101 [4]

-for the SCG,

A-MPR'c = A-MPRNR = MAX( A-MPRsingle,NR, A-MPRIM3)

-for the total configured transmission power,

A-MPRtot = PPowerClass,EN-DC – min(PPowerClass,EN-DC ,10*log10(10^((PPowerClass,E-UTRA - A-MPRE-UTRA)/10) + 10^((PPowerClass,NR - A-MPRNR)/10))

where

A-MPRE-UTRA = MAX( A-MPRsingle,E-UTRA + MPRsingle,E-UTRA, A-MPRIM3 )

with

-A-MPRsingle, E-UTRA is the A-MPR defined for the E-UTRA transmission in TS 36.101 [4]

-A-MPRsingle,NR is the A-MPR defined for the NR transmission in TS 38.101-1 [2]

-MPRsingle,E-UTRA is the MPR defined for the E-UTRA transmission in TS 36.101 [4]

For UEs not supporting dynamic power sharing the following

-for the MCG,

A-MPRc = MAX( A-MPRsingle, E-UTRA + MPRsingle,E-UTRA, A-MPRIM3 )

-for the SCG,

A-MPR'c = MAX( A-MPRsingle,NR, A-MPRIM3 )

where

-A-MPRsingle, E-UTRAis the A-MPR defined for the E-UTRA transmission in TS 36.101 [4]

-A-MPRsingle,NR is the A-MPR defined for the NR transmission in TS 38.101-1 [2]

-MPRsingle,E-UTRA is the MPR defined for the E-UTRA transmission in TS 36.101 [4]

The UE determines the Allocation Configuration Case and the value of A-MPRIM3 as follows:

If FIM3,low_block,low < 2490.5 MHz

Allocation Configuration Case B. A-MPRIM3 defined in Clause 6.2B.3.1.2.2

Else

Allocation Configuration Case A. A-MPRIM3 defined in Clause 6.2B.3.1.2.1

where

-FIM3,low_block,low = (2 * Flow_alloc,low_edge) – Fhigh_alloc,high_edge

-Flow_alloc,low_edge is the lowermost frequency of lower transmission bandwidth configuration.

-Fhigh_alloc,high_edge is the uppermost frequency of upper transmission bandwidth configuration.

Where the transmission bandwidth configuration for NR is the maximum frequency span covering all the configured SCSSpecificCarrier for scenarios that carrier bandwidths with different SCS can be fully overlapped.

NOTE:For non-dynamic power sharing capable UEs, since the allocation is unknown for one RAT, the edges of the channel transmission bandwidth are used instead of the edges of the RB allocations for that RAT.

6.2B.3.1.2.1A-MPRIM3 for NS_04 to meet -13 dBm / 1MHz

A-MPR is relative to 26 dBm for a power class 2 Cell Group to support PC1.5 and PC2 EN-DC UE. The same A-MPR is used relative to 23 dBm for a power class 3 Cell Group to support PC2 and PC3 EN-DC UE. The detail A-MPR values are decided based on the modified MPR behaviour in in Annex H.1. For the UE is configured with allocation configurations Case A or Case C (defined in Clause 6.2B.3.2.1), the allowed maximum output power reduction for IM3s applied to transmission on the MCG and the SCG with non-contiguous resource allocation is defined as follows:

A-MPRIM3 = MA

Where MA is defined as follows

MA = 12;0 ≤ B < 0.54

10;0.54 ≤ B < 1.08

9;1.08 ≤ B < 2.16

8.5;2.16 ≤ B < 3.24

8;3.24 ≤ B < 5.4

6;5.4 ≤ B

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

6.2B.3.1.2.2A-MPR for NS_04 to meet -25 dBm / 1MHz

A-MPR is relative to 26 dBm for a power class 2 Cell Group to support PC1.5 and PC2 EN-DC UE. The same A-MPR is used relative to 23 dBm for a power class 3 Cell Group to support PC2 and PC3 EN-DC UE. The detail A-MPR values are decided based on the modified MPR behaviour in Annex H.1.  For the UE is configured with allocation configurations Case B or Case D (defined in Clause 6.2B.3.2.1), the allowed maximum output power reduction for IM3s applied to transmission on the MCG and the SCG with non-contiguous resource allocation is defined as follows:

A-MPRIM3 = MA

Where MA is defined as follows

MA = 15; 0 ≤ B < 1.08

14; 1.08 ≤ B < 5.4

13; 5.4 ≤ B < 8.1

12; 8.1 ≤ B < 25.2

10; 25.2 ≤ B

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

## 6.2B.3.2Intra-band non-contiguous EN-DC

## 6.2B.3.2.0General

For intra-band non-contiguous EN-DC band combinations with additional requirements the A-MPR allowed are specified in Table 6.2B.3.2.0-1 for UEs configured with EN-DC and combinations of network signalling values indicated in the E-UTRA and NR cell group(s). Unless otherwise stated the A-MPR specified in clause 6.2B.3.2 for intra-band non-contiguous EN-DC configurations is the total power reduction allowed including MPR. For UEs scheduled with single uplink transmission, AMPR in clause 6.2.4 of [4] and 6.2.3 of [2] apply.

Table 6.2B.3.2.0-1: Allowed power reduction for intra-band non-contiguous EN-DC

## 6.2B.3.2.1A-MPR for NS_04

When the UE is configured for B41/n41 intra-band non-contiguous EN-DC and it receives IE NS_04, the UE determines the total allowed maximum output power reduction as specified in this clause. The A-MPR for EN-DC defined in this clause is used instead of MPR defined in 6.2B.2.2, not additively, so EN-DC MPR=0 when NS_04 is signaled.

For UE supporting dynamic power sharing the following:

-for the MCG, A-MPRc in accordance with TS 36.101 [4]

-for the SCG,

A-MPR'c = A-MPRNR = MAX( A-MPRsingle,NR, A-MPREN-DC)

-for the total configured transmission power,

A-MPRtot = PPowerClass,EN-DC – min(PPowerClass,EN-DC ,10*log10(10^((PPowerClass,E-UTRA - A-MPRE-UTRA)/10) + 10^((PPowerClass,NR - A-MPRNR)/10))

where

A-MPRE-UTRA = MAX( A-MPRsingle,E-UTRA + MPRsingle,E-UTRA, A-MPREN-DC )

A-MPREN-DC = MAX(A-MPRIM3, A-MPRACLRoverlap )

with

-A-MPRsingle, E-UTRA is the A-MPR defined for the E-UTRA transmission in TS 36.101 [4]

-A-MPRsingle,NR is the A-MPR defined for the NR transmission in TS 38.101-1 [2]

-MPRsingle,E-UTRA is the MPR defined for the E-UTRA transmission in TS 36.101 [4]

For UEs not supporting dynamic power sharing the following

-for the MCG,

A-MPRc = MAX( A-MPRsingle, E-UTRA + MPRsingle,E-UTRA, A-MPRIM3, A-MPRACLRoverlap)

-for the SCG,

A-MPR'c = MAX( A-MPRsingle,NR, A-MPRIM3, A-MPRACLRoverlap)

where

-A-MPRsingle, E-UTRAis the A-MPR defined for the E-UTRA transmission in TS 36.101 [4]

-A-MPRsingle,NR is the A-MPR defined for the NR transmission in TS 38.101-1 [2]

-MPRsingle,E-UTRA is the MPR defined for the E-UTRA transmission in TS 36.101 [4]

The UE determines the Allocation Configuration Case and the value of A-MPRIM3 as follows:

If AND( FIM3,low_block,high < Ffilter,low ,  MAX( SEM-13,high, FIM3,high_block,low ) > Ffilter,high )

Allocation Configuration Case C. A-MPRIM3 defined in Clause 6.2B.3.1.2.1

Else

Allocation Configuration Case D. A-MPRIM3 defined in Clause 6.2B.3.1.2.2

where

-FIM3,low_block,high = (2 * Flow_alloc,high_edge ) – Fhigh_alloc,low_edge

-FIM3,high_block,low = (2 * Fhigh_alloc,low_edge) – Flow_alloc,high_edge

-Flow_alloc,low_edge is the lowermost frequency of lower transmission bandwidth allocation.

-Flow_alloc,high_edge is the uppermost frequency of lower transmission bandwidth allocation.

-Fhigh_alloc,low_edge is the lowermost frequency of upper transmission bandwidth allocation.

-Fhigh_alloc,high_edge is the uppermost frequency of upper transmission bandwidth allocation.

-Ffilter,low = 2480 MHz

-Ffilter,high = 2745 MHz

-SEM-13,high = Threshold frequency where upper spectral emission mask for upper channel drops from -13 dBm / 1MHz to -25 dBm / 1MHz, as specified in Clause6.6.2.2.2 in [4] and Clause 6.5.2.3.2 in [2] respectively.

Where the transmission bandwidth configuration for NR is the maximum frequency span covering all the configured SCSSpecificCarrier for scenarios that carrier bandwidths with different SCS can be fully overlapped

The UE determines the value of A-MPRACLRoverlap as specified in Table 6.2B.3.2.1-1:

Table 6.2B.3.2.1-1: A-MPRACLRoverlap

## 6.2B.3.3Inter-band EN-DC within FR1

For inter-band EN-DC between E-UTRA and FR1 NR, UE additional maximum output power reduction specified in TS 36.101 [4] and TS 38.101-1 [2] apply for E-UTRA and NR respectively.

Unless specified in Table 6.2B.3.3-1, for inter-band carrier aggregation with uplink assigned to LTE and NR bands, the requirements in [2] clause 6.2.3 apply for NR uplink component carrier and the requirements in [4] clause 6.2.4 apply for LTE uplink component carrier.

Unless otherwise stated, for inter-band EN-DC with uplink assigned to LTE and NR bands and specified in Table 6.2B.3.3-1, the combined requirements and allowed A-MPR are applibale on both LTE and NR bands when LTE and NR component carriers are active. The requirements in Table 6.2B.3.3-1 are specified in terms of an additional spectrum emission requirement. The emission requirements specified in Table 6.2B.3.3-1 also apply for the frequency ranges that are less than FOOB (MHz) from the edge of the channel bandwidth specified in TS 36.101 [4] and TS 38.101-1 [2], respectively.

Table 6.2B.3.3-1: Additional Requirements for inter-band EN-DC (two-bands)

## 6.2B.3.3AInter-band NE-DC within FR1

For inter-band NE-DC between E-UTRA and FR1 NR, UE additional maximum output power reduction specified in TS 36.101 [4] and TS 38.101-1 [2] apply for E-UTRA and NR respectively.

Unless specified in Table 6.2B.3.3A-1, for inter-band carrier aggregation with uplink assigned to LTE and NR bands, the requirements in [2] clause 6.2.3 apply for NR uplink component carrier and the requirements in [4] clause 6.2.4 apply for LTE uplink component carrier.

Unless otherwise stated, for inter-band NE-DC with uplink assigned to NR and LTE bands and specified in Table 6.2B.3.3A-1, the combined requirements and allowed A-MPR are applicable on both LTE and NR bands when LTE and NR component carriers are active. The requirements in Table 6.2B.3.3A-1 are specified in terms of an additional spectrum emission requirement. The emission requirements specified in Table 6.2B.3.3A-1 also apply for the frequency ranges that are less than FOOB (MHz) from the edge of the channel bandwidth specified in TS 36.101 [4] and TS 38.101-1 [2], respectively.

Table 6.2B.3.3A-1: Additional Requirements for inter-band NE-DC (two-bands)

## 6.2B.3.4Inter-band EN-DC including FR2

UE additional maximum output power reduction requirement for E-UTRA single carrier and CA operation specified in clauses 6.2.4 and 6.2.4A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.2.3, 6.2A.3 and 6.2D.3 of TS 38.101-2 [3] apply.

## 6.2B.3.4A(Void)

## 6.2B.3.5Inter-band EN-DC including both FR1 and FR2

UE additional maximum output power reduction requirement for E-UTRA single carrier and CA operation specified in clauses 6.2.4 and 6.2.4A of TS 36.101 [4] and for NR single carrier specified in clause 6.2.3 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.2.3, 6.2A.3 and 6.2D.3 of TS 38.101-2 [3] apply.

## 6.2B.4Configured output power for DC

## 6.2B.4.1Configured output power level

## 6.2B.4.1.1Intra-band contiguous EN-DC

The following requirements apply for one component carrier per CG configured for synchronous DC.

For intra-band dual connectivity with one uplink serving cell per CG on E-UTRA and NR respectively, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of CG i, i = 1,2, and its total configured maximum transmission power for EN-DC operation = 10log10() with  as specified in clause 7.6 of TS 38.213 [10].PTotalEN-DCPtotalEN-DCPtotalEN-DC

The configured maximum output power PCMAX_ E-UTRA,c (p) in sub-frame p for the configured E-UTRA uplink carrier shall be set within the bounds:

PCMAX_L_ E-UTRA,c (p) ≤ PCMAX_ E-UTRA,c (p) ≤  PCMAX H _ E-UTRA,c (p)

where PCMAX_L_ E-UTRA,c and PCMAX H _ E-UTRA,c are the limits for a serving cell c as specified in TS 36.101 [4] clause 6.2.5 modified by PLTE as follows:

PCMAX_L_ E-UTRA,c = MIN {MIN(PEMAX,c , PEMAX, EN-DC, PLTE) – tC_ E-UTRA, c,  (PPowerClass, EN-DC – ΔPPowerClass,EN-DC ), (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA) – MAX(MPRc + A-MPRc + ΔTIB,c  + TC_ E-UTRA, c + TProSe, P-MPRc)}

PCMAX H _ E-UTRA,c = MIN {PEMAX,c, PEMAX, EN-DC , PLTE, PPowerClass, EN-DC, PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA}

where

-PEMAX,EN-DC is the value given by the field p-maxUE-FR1 of the RRCConnectionReconfiguration-v1530 IE as defined in TS 36.331 [8];

-PLTE is the value given by the field p-maxEUTRA-r15 of the RRCConnectionReconfiguration-v1510 IE as defined in TS 36.331 [8] which is the same as PLTE in TS 38.213 [10];

-∆tC_EUTRA, c = 1.5 dB when NOTE 2 in Table 6.2.2-1 of TS 36.101 [4] applies; ∆tC_EUTRA, c = 0 dB otherwise;

and whenever NS_01 is not indicated within CG 1:

-for a UE indicating support of dynamicPowerSharing, the MPRc and the A-MPRc are determined in accordance with the DCI of serving cell c of the CG 1 and the specification in clause 6.2.4 of TS 36.101 [4];

-for a UE not indicating support of dynamicPowerSharing, the A-MPRc is determined in accordance with clause 6.2B.3.1 with parameters applicable for UEs not indicating support of dynamicPowerSharing and MPRc = 0 dB;

and whenever NS_01 is indicated in CG 1:

-for a UE indicating support of dynamicPowerSharing, the MPRc is determined in accordance with the DCI of serving cell c of the CG 1 and the specification in clause 6.2.4 of TS 36.101 [4];

-for a UE not indicating support of dynamicPowerSharing, the MPRc is determined in accordance with clause 6.2B.2.1 with parameters applicable for UEs not indicating support of dynamicPowerSharing and A-MPRc = 0 dB;

The configured maximum output power PCMAX,f,c,NR (q) in physical channel q for the configured NR carrier shall be set within the bounds:

PCMAX_L,f,c,,NR (q) ≤  PCMAX,f,c,NR (q) ≤  PCMAX_H,f,c,NR (q)

where PCMAX_L,f,c,NR and PCMAX_H,f,c,NR are the limits for a serving cell c as specified in clause 6.2.4 of TS 38.101-1 [2] modified  as follows:

PCMAX_L,f,c,,NR = MIN {MIN(PEMAX,c , PEMAX, EN-DC, PNR) - TC_NR, c, (PPowerClass, EN-DC – ΔPPowerClass,EN-DC ),  (PPowerClass,NR – ΔPPowerClass,NR) – MAX(MAX(MPRc,A-MPRc)+ ΔTIB,c + TC_NR, c + ∆TRxSRS,  P-MPRc) }

PCMAX_H,f,c,NR = MIN {PEMAX,c, PEMAX, EN-DC, PNR, PPowerClass, EN-DC, PPowerClass,NR – ΔPPowerClass,NR }

where

-PEMAX,EN-DC is the value given by the field p-maxUE-FR1 of the RRCConnectionReconfiguration-v1530 IE as defined in TS 36.331 [8];

-PLTE signalled by RRC as p-MaxEUTRA-r15 in TS 36.331 [8]

-PNR is the value given by the field  p-NR-FR1 of the PhysicalCellGroupConfig IE as defined in  [9] and signalled by RRC;

-ΔTc_E-UTRA, c = 1.5dB when NOTE 2 in Table 6.2.2-1 in TS 36.101 [4] applies for a serving cell c, otherwise TC_ E-UTRA,c = 0dB;

-TC_NR,c = 1.5dB when NOTE 3 in Table 6.2.1-1 in TS 38.101-1 [2] applies for a serving cell c, otherwise TC_NR,c = 0dB;

-ΔTIB,c specified in clause 6.2B.4.2.1 for EN-DC, the individual Power Class defined in table 6.2B.1.1 and any other additional power reductions parameters specified in clauses 6.2B.2 and 6.2B.3 for EN-DC are applicable to PCMAX_ E-UTRA,c and PCMAX,f,c,NR evaluations.

-PPowerClass, EN-DC is defined in clause 6.2B.1.1 for intra-band contiguous EN-DC;

-PPowerClass,NR is the nominal UE power of the power class that the UE supports for the NR band of the EN-DC combination as defined in clause 6.2.1 of 38.101-1 [2]; in case IE powerClassNRPart-r16 as defined in TS 38.331 [9] is indicated, PPowerClass,NR should use that value instead;

-ΔPPowerClass,NR is 3 dB, 6 dB, or 0 dB according to clause 6.2.4 of TS 38.101-1 [2] for a UE that supports power class 2 or power class 1.5 in the NR band of the EN-DC combination as defined in clause 6.2.1 of TS 38.101-1 [2];

-PPowerClass,E-UTRA is the nominal UE power of the power class that the UE supports for the E-UTRA band of the EN-DC combination as defined in clause 6.2.2 of 36.101 [4];

-ΔPPowerClass,E-UTRA is 3 dB or 0 dB according to clause 6.2.5 of TS 36.101 [4] for a UE that supports power class 2 in the E-UTRA band of the EN-DC combination as defined in clause 6.2.2 of TS 36.101 [4];

-ΔPPowerClass,EN-DC is 3 dB for a power class 2 capable EN-DC UE when  LTE UL/DL configuration is 0 or 6; or LTE UL/DL configuration is 1 and special subframe configuration is 0 or 5; ΔPPowerClass,EN-DC = 3 dB when the IE p-maxUE-FR1 as defined in TS 36.331 [4] is provided and set to the maximum output power of the default power class or lower; ΔPPowerClass,EN-DC is 6 dB for a power class 1.5 capable EN-DC UE when the LTE UL duty cycle is greater than max(50%, maxUplinkDutyCycle-PC2-FR1); ΔPPowerClass,EN-DC is 3 dB for a power class 1.5 capable EN-DC UE when the LTE UL duty cycle is between max(50%,maxUplinkDutyCycle-PC2-FR1) and max(25%,0.5*maxUplinkDutyCycle-PC2-FR1); otherwise ΔPPowerClass,EN-DC = 0 dB; The IE maxUplinkDutyCycle-PC2-FR1 is defined in TS 38.331 [9].

-NOTE: UE reports  ∆PPowerClass,EN-DC when deltaPowerClassReporting-r18 is present, dpc-Reporting-FR1 [7] is configuredand the reporting is triggered only by uplink duty cycle exceedance or by return to the powerClass after the duty cycle exceedance.

and whenever an NS signalling other than NS_01 is indicated within CG 2:

-for a UE indicating support of dynamicPowerSharing, A-MPRc = A-MPR'c with A-MPR'c determined in accordance with clause 6.2B.3.1 and MPRc = 0 dB if transmission(s) in subframe p on CG 1 overlap in time with physical channel q on CG 2;

-for a UE indicating support of dynamicPowerSharing, A-MPRc is determined in accordance with TS 38.101-1 [2] if transmission(s) in subframe p on CG 1 does not overlap in time with physical channel q on CG 2;

-for a UE not indicating support of dynamicPowerSharing, the A-MPRc is determined in accordance with clause 6.2B.3.1 with parameters applicable for UEs not indicating support of dynamicPowerSharing and MPRc = 0 dB;

and whenever NS_01 is indicated in CG 2.

-for a UE indicating support of dynamicPowerSharing, MPRc = MPR'c with MPR'c determined in accordance with clause 6.2B.2.1 and A-MPRc = 0 dB if transmission(s) in subframe p on CG 1 overlap in time with physical channel q on CG 2;

-for a UE indicating support of dynamicPowerSharing, MPRc is determined in accordance with TS 38.101-1 [2] if transmission(s) in subframe p on CG 1 does not overlap in time with physical channel q on CG 2;

-for a UE not indicating support of dynamicPowerSharing, the MPRc is determined in accordance with clause 6.2B.2.1 with parameters applicable for UEs not indicating support of dynamicPowerSharing and A-MPRc = 0 dB;

If the transmissions from NR and E-UTRA do not overlap, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications apply with the modifications specified above. The lower value between PPowerClass, EN-DC or PEMAX, EN-DC shall not be exceeded at any time by UE.

If the EN-DC UE is not supporting dynamic power sharing, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications TS 36.101 [4] and TS 38.101-1 [2] respectively apply with the modifications specified above.

If the UE does not support dynamic power sharing,

= MIN { PEMAX, EN-DC , PPowerClass, EN-DC - ΔPPowerClass,EN-DC } + 0.3 dBPTotalEN-DC

For UEs indicating support of dynamicPowerSharing in the UE-MRDC-Capability IE the UE can configure the total maximum transmission power  within the rangePTotalEN-DC

PEN-DC,tot_L ≤  ≤  PEN-DC,tot_HPTotalEN-DC

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

-pCMAX H _ E-UTRA,c (p) is the E-UTRA higher limit of the maximum configured power expressed in linear scale;

-pCMAX H,f,c,NR (q) is the NR higher limit of the maximum configured power expressed in linear scale;

-pCMAX L _ E-UTRA,c (p) is the E-UTRA lower limit of the maximum configured power expressed in linear scale;

-pCMAX L,f,c,NR (q) is the NR lower limit of the maximum configured power expressed in linear scale;

-PPowerClass, EN-DC is defined in clause 6.2B.1.1 for intra-band EN-DC;

-X_scale is the linear value of X dB which is configured by RRC and can only take values [0 , 6] dB

-pCMAX  E-UTRA,c (p) is the linear value of PCMAX  E-UTRA,c (p), the real configured max power for E-UTRA

-pCMAX,f,c  NR (q) is the linear value of PCMAX,f,c,NR (q), the real configured max power of NR

Table 6.2B.4.1.1-2: PCMAX tolerance for Dual Connectivity E-UTRA-NR

If the UE supports dynamic power sharing, and when E-UTRA and NR transmissions overlap and the condition (If (a=TRUE) AND (b=FALSE)) is met, SCG shall be transmitted and the following supplementary minimum requirement apply for the measured SCG power, PUMAX,f,c,NR (q), under nominal conditions and unless otherwise stated

10log(pCMAX L,f,c,NR(q)/X_scale)  –  TLOW (10log(pCMAX L,f,c,NR(q)/X_scale) )}  ≤  PUMAX,f,c,NR (q) ≤  10log(pCMAX H, f,c,NR (q)) + THIGH (10log(pCMAX H, f,c,NR (q))).

with the tolerances TLOW and THIGH for applicable values of PCMAX specified in Table 6.2B.4.1.1-2.

If the UE supports dynamic power sharing, the measured maximum output power in subframe p on CG 1, pUMAX,c,E-UTRA,  shall meet the requirements in clause 6.2.5 in TS 36.101 [4] with the limits PCMAX_L,c and PCMAX_H,c replaced by PCMAX_L_ E-UTRA,c and PCMAX_H_ E- UTRA,c as specified above, respectively.

If the configured transmission power spectral density between the MCG and SCG differs by more than 6 dB, then

PUMAX,f,c,NR (q) ≤ 10log(pCMAX H, f,c,NR (q)) + THIGH (10log(pCMAX H, f,c,NR (q))).

## 6.2B.4.1.1aIntra-band contiguous NE-DC

The following requirements apply for one component carrier per CG configured for synchronous DC.

For intra-band dual connectivity with one uplink serving cell per CG on E-UTRA and NR respectively, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of CG i, i = 1,2, and its total configured maximum transmission power for NE-DC operation = 10log10() with  as specified in clause 7.6.1A of TS 38.213 [10].PTotalNE-DCPtotalNE-DCPtotalNE-DC

The configured maximum output power PCMAX_ E-UTRA,c (p) in sub-frame p for the configured E-UTRA uplink carrier shall be set within the bounds:

PCMAX_L_ E-UTRA,c (p) ≤ PCMAX_ E-UTRA,c (p) ≤  PCMAX H _ E-UTRA,c (p)

where PCMAX_L_ E-UTRA,c and PCMAX H _ E-UTRA,c are the limits for a serving cell c as specified in TS 36.101 [4] clause 6.2.5 modified by PLTE as follows:

PCMAX_L_ E-UTRA,c = MIN { MIN(PEMAX, NE-DC , PEMAX,c , PLTE) – tC_E-UTRA, c, (PPowerClass, NE-DC – ΔPPowerClass, NE-DC), (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA) – MAX(MPRc + A-MPRc + ΔTIB,c  + TC_ E-UTRA, c + TProSe, P-MPRc)}

PCMAX H _ E-UTRA,c = MIN {PEMAX,c,  PEMAX, NE-DC , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC), PLTE, (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA)}

with exception that

-if no symbol of slot  of the NR that is indicated as uplink or flexible by TDD-UL-DL-ConfigurationCommon or TDD-UL-DL-ConfigDedicated overlaps with subframe  of the E-UTRA; or

-if NR slot(s) that is indicated as downlink by TDD-UL-DL-ConfigurationCommon or TDD-UL-DL-ConfigDedicated does not overlap with subframe  of the E-UTRA; then

PCMAX_L_ E-UTRA,c = MIN { MIN(PEMAX, NE-DC , PEMAX,c) – tC_E-UTRA, c, (PPowerClass, NE-DC – ΔPPowerClass, NE-DC), (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA) – MAX(MPRc + A-MPRc + ΔTIB,c  + TC_ E-UTRA, c + TProSe, P-MPRc)}

PCMAX H _ E-UTRA,c = MIN {PEMAX,c,  PEMAX, NE-DC , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC), (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA)}

The configured maximum output power PCMAX,f,c,NR (q) in physical-channel q for the configured NR carrier shall be set within the bounds:

PCMAX_L,f,c,NR (q) ≤  PCMAX,f,c,NR (q) ≤  PCMAX_H,f,c,NR (q)

where PCMAX_L,f,c,NR and PCMAX_H,f,c,NR are the limits for a serving cell c as specified in clause 6.2.4 of TS 38.101-1 [2] modified by PNR as follows:

PCMAX_L,f,c,NR = MIN { MIN(PEMAX, NE-DC , PEMAX,c , PNR) – tC_NR, c, (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), (PPowerClass,NR – ΔPPowerClass,NR) – MAX(MPRc + A-MPRc+ ΔTIB,c + TC_NR, c + ∆TRxSRS,  P-MPRc) }

PCMAX_H,f,c,NR = MIN {PEMAX,c, PEMAX, NE-DC, PNR, (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), PPowerClass,NR – ΔPPowerClass,NR}

-PEMAX,NE-DC signalled by RRC as p-UE-FR1 in TS 38.331 [9];

-PLTE signalled by RRC as p-MaxEUTRA in TS 36.331 [8];

-PNR signalled by RRC as p-NR-FR1 defined in TS 38.331 [9];

-ΔTc_E-UTRA,c = 1.5dB when NOTE 2 in Table 6.2.2-1 in TS 36.101 [4] applies for a serving cell c, otherwise TC_ E-UTRA,c = 0dB;

-TC_NR,c = 1.5dB when NOTE 3 in Table 6.2.1-1 in TS 38.101-1 [2] applies for a serving cell c, otherwise TC_NR,c = 0dB;

-ΔTIB,c is specified in clause 6.2B.4.2;

-PPowerClass, NE-DC is defined in clause 6.2B.1.1a for intra-band contiguous NE-DC;

-ΔPPowerClass,NE-DC = 3 dB for a power class 2 capable NE-DC UE when requirements of default power class had been applied as specified in sub-clause 6.2B.1; otherwise ΔPPowerClass,NE-DC = 0 dB;

-PPowerClass,NR is the nominal UE power of the power class that the UE supports for the NR band of the NE-DC combination as defined in clause 6.2.1 of 38.101-1 [2]; in case powerClassNRPart as defined in TS 38.331 [9] is indicated, PPowerClass,NR should use that value instead.

-ΔPPowerClass,NR is 3 dB or 0 dB according to clause 6.2.4 of TS 38.101-1 [2] for a UE that supports power class 2 in the NR band of the EN-DC combination as defined in clause 6.2.1 of TS 38.101-1 [2];

-PPowerClass,E-UTRA is the nominal UE power of the power class that the UE supports for the E-UTRA band of the NE-DC combination as defined in clause 6.2.2 of 36.101 [4];

-ΔPPowerClass,E-UTRA is 3 dB or 0 dB according to clause 6.2.5 of TS 36.101 [4] for a UE that supports power class 2 in the E-UTRA band of the EN-DC combination as defined in clause 6.2.2 of TS 36.101 [4];

If the transmissions from NR and E-UTRA do not overlap, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications apply with the modifications specified above. The lower value between PPowerClass, NE-DC or PEMAX, NE-DC shall not be exceeded at any time by UE.

= 10log10() with  the configured maximum transmission power for NE-DC operation as specified in clause 7.6 of TS 38.213 [10].PTotalNE-DCPtotalNE-DCPTotalNE-DC

The total configured maximum transmission power is

= MIN { PEMAX, NE-DC ,PPowerClass, NE-DC – ΔPPowerClass, NE-DC }PTotalNE-DC

If the UE does not support dynamic power sharing,

= MIN { PEMAX, NE-DC , PPowerClass, NE-DC - ΔPPowerClass,EN-DC } + 0.3 dBPTotalNE-DC

If the NE-DC UE is not supporting dynamic power sharing, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications TS 36.101 [4] and TS 38.101-1 [2] respectively apply with the modifications specified above and  applies.PTotalNE-DC

## 6.2B.4.1.2Intra-band non-contiguous EN-DC

The following requirements apply for one component carrier per CG configured for synchronous DC. The CG(s) are indexed by j = 1 for MCG and j = 2 for SCG.

The configured maximum output power PCMAX_ E-UTRA,c (p) in sub-frame p for the configured E-UTRA uplink carrier shall be set in accordance with clause 6.2B.4.1.1 but where

-for a UE not indicating support of dynamicPowerSharing, the A-MPRc determined in accordance with clause 6.2B.3.2 with parameters applicable for UEs not indicating support of dynamicPowerSharing and MPRc = 0 dB;

whenever NS_01 is not indicated within CG 1 while

-for a UE not indicating support of dynamicPowerSharing, the MPRc determined in accordance with clause 6.2B.2.2 with parameters applicable for UEs not indicating support of dynamicPowerSharing and A-MPRc = 0 dB;

whenever NS_01 is indicated in CG 1.

The configured maximum output power PCMAX,f,c,NR (q) in physical channel q for the configured NR carrier shall be set in accordance with clause 6.2B.4.1.1 but where

-for a UE indicating support of dynamicPowerSharing, A-MPRc = A-MPR'c with A-MPR'c determined in accordance with clause 6.2B.3.2 and MPRc = 0 dB if transmission(s) in subframe p on CG 1 overlap in time with physical channel q on CG 2;

-for a UE indicating support of dynamicPowerSharing, A-MPRc is determined in accordance with TS 38.101-1 [2] if transmission(s) in subframe p on CG 1 does not overlap in time with physical channel q on CG 2;

-for a UE not indicating support of dynamicPowerSharing, the A-MPRc is determined in accordance with clause 6.2B.3.2 with parameters applicable for UEs not indicating support of dynamicPowerSharing and MPRc = 0 dB;

whenever NS_01 is not indicated in CG 2 while

-for a UE indicating support of dynamicPowerSharing, MPRc = MPR'c with MPR'c determined in accordance with clause 6.2B.2.2 and A-MPRc = 0 dB if transmission(s) in subframe p on CG 1 overlap in time with physical channel q on CG 2;

-for a UE indicating support of dynamicPowerSharing, MPRc is determined in accordance with TS 38.101-1 [2] if transmission(s) in subframe p on CG 1 does not overlap in time with physical channel q on CG 2;

-for a UE not indicating support of dynamicPowerSharing, the MPRc is determined in accordance with clause 6.2B.2.2 with parameters applicable for UEs not indicating support of dynamicPowerSharing and A-MPRc = 0 dB;

whenever NS_01 is indicated in CG 2.

For UEs indicating support of dynamicPowerSharing in the UE-MRDC-Capability IE, the UE can configure the total transmission power in accordance with clause 6.2B.4.1.1 but with Ppowerclass,EN-DC the EN-DC power class of the intra-band non-contiguous band combination configured and A-MPR determined in accordance with clause 6.2B.3.2.

The total maximum output power PUMAX over both CGs is measured in accordance with clause 6.2B.4.1.1 and shall be within the limits specified in clause 6.2B.4.1.1 but with parameters applicable for the non-contiguous band combination configured.

The maximum output power levels pUMAX,c,E-UTRA and pUMAX,f,c,NR for the CGs are measured in accordance with clause 6.2B.4.1.1 and shall be within the limits specified in clause 6.2B.4.1.1 but with parameters applicable for the non-contiguous band combination configured.

6.2B.4.1.3Inter-band EN-DC within FR1

For inter-band dual connectivity with one uplink serving cell or more than one uplink serving cells configured for intra-band UL CA on the E-UTRA CG and one uplink serving cell on the NR CG or more than one uplink serving cells configured for intra-band UL CA, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of CG i, i = 1,2, and its total configured maximum transmission power for EN-DC operation, = 10log10() with  as specified in clause 7.6 of TS 38.213 [10]. For EN-DC with more than one uplink serving cells configured for intra-band UL CA on the E-UTRA CG, the PCMAX applies to the entire E-UTRA CG. For EN-DC with more than one uplink serving cells configured for intra-band UL CA on the NR CG, the PCMAX applies to the entire NR CG.PTotalEN-DCPtotalEN-DCPtotalEN-DC

For a UE configured with EN-DC and serving cell frame structure type 1, if the UE is configured with subframeAssignment-r15 for the serving cell and E-UTRA Pcell is FDD, the UE is not expected to be configured with more than one serving cells in the uplink.

The configured maximum output power PCMAX_ E-UTRA,c (p) in sub-frame p for the configured E-UTRA uplink carrier(s) shall be set within the bounds:

PCMAX_L_ E-UTRA,c (p) ≤  PCMAX_ E-UTRA,c (p) ≤  PCMAX H _ E-UTRA,c (p)

where PCMAX_L_ E-UTRA,c and PCMAX H _ E-UTRA,c are the limits for a serving cell c as specified in TS 36.101 [4] clause 6.2.5 modified by PLTE as follows:

PCMAX_L_ E-UTRA,c = MIN { PEMAX, EN-DC , (PPowerClass, EN-DC – ΔPPowerClass,EN-DC ), MIN(PEMAX,c , PLTE) – tC_ E-UTRA, c,  (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA) – MAX(MPRc + A-MPRc + ΔTIB,c  + tC_ E-UTRA, c + TProSe, P-MPRc)}

PCMAX H _ E-UTRA,c = MIN {PEMAX,c,  PEMAX, EN-DC  , (PPowerClass, EN-DC – ΔPPowerClass,EN-DC ), PLTE, PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA}

For EN-DC with more than one uplink serving cells configured for intra-band UL CA on the E-UTRA CG, PCMAX_L_ E-UTRA,c and PCMAX H _ E-UTRA,c are the limits for the E-UTRA CG as specified in TS 36.101 [4] clause 6.2.5A modified by PLTE as follows:

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

-PEMAX,EN-DC is the value given by the field p-maxUE-FR1 of the RRCConnectionReconfiguration-v1530 IE as defined in TS 36.331 [8];

-If more than one E-UTRA uplink serving cell is configured as intra-band UL CA in the E-UTRA CG, PPowerClass refers to the maximum output power of the E-UTRA intra-band CA power class given in Table 6.2.2A-1 of TS 36.101 [4],

-If more than one NR uplink serving cell is configured as intra-band UL CA in the NR CG, PPowerClass refers to the maximum output power of the NR intra-band CA power class given in sub clause 6.2A.1 of [2],

-PLTE is the value given by the field p-maxEUTRA-r15 of the RRCConnectionReconfiguration-v1510 IE as defined in TS 36.331 [8];

-If more than one E-UTRA uplink serving cell is configured as intra-band UL CA in the E-UTRA CG, MPRc = MPR and A-MPRc = A-MPR with MPR and A-MPR specified in clause 6.2.3A and clause 6.2.4A of TS 36.101 [4] respectively. There is one power management term for the UE, denoted P-MPR, and P-MPR c = P-MPR. PCMAX_ E-UTRA,c is calculated under the assumption that the transmit power is increased by the same amount in dB on all component carriers within the E-UTRA CG.

-If more than one NR uplink serving cell is configured as intra-band UL CA in the NR CG, MPRc and A-MPRc are determined by subclause 6.2.2 of [2]. There is one power management term for the UE, denoted P-MPR, and P-MPR c = P-MPR.

-PNR is the value given by the field p-NR-FR1 of the PhysicalCellGroupConfig IE as defined in TS 38.331 [9];

-Δtc_E-UTRA, c = 1.5 dB when NOTE 2 in Table 6.2.2-1 in TS 36.101 [4] applies for a serving cell c, otherwise TC_ E-UTRA,c = 0 dB;

-TC_NR,c = 1.5dB when NOTE 3 in Table 6.2.1-1 in TS 38.101-1 [2] applies for a serving cell c, otherwise TC_NR,c = 0 dB;TC_NR,C is the highest value TC_NR,C among all serving cells c if more than one NR uplink serving cell is configured as intra-band UL CA in the NR CG;

-PPowerClass, EN-DC is the nominal UE power class indicated by PowerClass defined in clause 6.2B.1.3 for inter-band EN-DC;

-If the UE indicates higherPowerLimitMRDC-r17 and ΔPPowerClass,EN-DC = 0, PPowerClass,EN-DC is replaced by the sum of the linear powers of PPowerClass,NR and PPowerClass,E-UTRA converted to dB;

-If the UE further indicates powerBoosting-pi2BPSK-QPSK-Modified-r18 or powerBoosting-pi2BPSK-QPSK-r18, and if IE powerBoostPi2BPSK-r18 and/or powerBoostQPSK-r18 is set to 1 as defined in TS 38.101-1 [2] for any of the NR bands that comprise the band combination, PPowerClass,NR is replaced by PPowerClass,NR + ΔPPowerBoost and PPowerClass,EN-DC is replaced by the sum of the linear powers of PPowerClass,NR + ΔPPowerBoost and PPowerClass,E-UTRA converted to dB;

-∆PPowerClass,EN-DC = 3 dB for a power class 2 capable EN-DC UE when requirements of default power class had been applied as specified in sub-clause 6.2B.1; otherwise ∆PPowerClass,EN-DC = 0 dB;

NOTE:UE reports ∆PPowerClass,EN-DC when deltaPowerClassReporting-r18 is present, dpc-Reporting-FR1 [7] is configured and the reporting is triggered only by uplink duty cycle exceedance or by return to the powerClass after the duty cycle exceedance.

-PPowerClass,NR is the nominal UE power of the power class indicated by ue-PowerClass that the UE supports for the NR band and for NR intra-band UL CA of the EN-DC combination as defined in clause 6.2.1 or 6.2A1.1 of 38.101-1 [2]; in case IE powerClassNRPart-r16 as defined in TS 38.331 [9] is indicated, PPowerClass,NR should use that value instead;

-ΔPPowerClass,NR is 3 dB or 0 dB according to clause 6.2.4 of TS 38.101-1 [2] for a UE that supports power class 2 in the NR band of the EN-DC combination as defined in clause 6.2.1 of TS 38.101-1 [2];

-PPowerClass,E-UTRA is the nominal UE power of the power class indicated by ue-PowerClass-N-r13 that the UE supports for the E-UTRA band or indicated by ue-CA-PowerClass-N E-UTRA intra-band UL CA of the EN-DC combination as defined in clause 6.2.2 or 6.2.2A of 36.101 [4];

-ΔPPowerClass,E-UTRA is 3 dB or 0 dB according to clause 6.2.5 of TS 36.101 [4] for a UE that supports power class 2 in the E-UTRA band of the EN-DC combination as defined in clause 6.2.2 of TS 36.101 [4];

-ΔTIB,c specified in clause 6.2B.4.2.3 for EN-DC, the individual Power Class defined in table 6.2B.1.3 and any other additional power reductions parameters specified in clauses 6.2B.2 and 6.2B.3for EN-DC are applicable to PCMAX_ E-UTRA,c and PCMAX,f,c,NR evaluations.

-∆TRxSRS is the highest value among all serving cells c.

If the transmissions from NR and E-UTRA do not overlap, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications apply with the modifications specified above. The lower value between PPowerClass, EN-DC or PEMAX, EN-DC shall not be exceeded at any time by UE.

= 10log10() with  the configured maximum transmission power for EN-DC operation as specified in clause 7.6 of TS 38.213 [10].PTotalEN-DCPtotalEN-DCPTotalEN-DC

The total configured maximum transmission power for both synchronous and non-synchronous operation is

= MIN { PEMAX, EN-DC ,PPowerClass, EN-DC – ΔPPowerClass, EN-DC }PTotalEN-DC

If the UE does not support dynamic power sharing,

= MIN { PEMAX, EN-DC ,PPowerClass, EN-DC  – ΔPPowerClass, EN-DC } + 0.3 dBPTotalEN-DC

If the EN-DC UE does not support dynamic power sharing, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications TS 36.101 [4] and TS 38.101-1 [2] respectively apply with the modifications specified above and  applies.PTotalEN-DC

When a UE supporting dynamic sharing is configured for overlapping E-UTRA uplink and NR uplink transmissions, the UE can set its configured maximum output power PCMAX_ E-UTRA,c and PCMAX,f,c,NR for the configured E-UTRA and NR uplink carriers, respectively, and its configured maximum transmission power for EN-DC operation, , as specified above.PTotalEN-DC

The measured total maximum output power PUMAX over both CGs/RATs, measured over the transmission reference time duration is

PUMAX = 10 log10 [pUMAX,c,E-UTRA + pUMAX,c,NR],

where pUMAX,c,E-UTRA and pUMAX,c,NR denotes the measured output power of serving cell c for E-UTRA and NR respectively, expressed in linear scale.

The measured total configured maximum output power PUMAX shall be within the following bounds:

PCMAX_L -TLOW (PCMAX_L)  ≤  PUMAX  ≤  PCMAX_H + THIGH (PCMAX_H)

with the tolerances TLOW(PCMAX_H) and THIGH(PCMAX_H) for applicable values of PCMAX specified in Table 6.2B.4.1.3-2.

When an UL subframe transmission p from E-UTRA overlap with a physical-channel q from the NR, then for PUMAX evaluation, the E-UTRA subframe p is taken as reference period TREF and always considered as the reference measurement duration and the following rules are applicable.

TREF and Teval are specified in Table 6.2B.4.1.3-1 when same or different subframe and physical-channel durations are used in aggregated carriers. The lesser of PPowerClass ,EN-DC and PEMAX,EN-DC shall not be exceeded by the UE during any evaluation period of time where PPowerClass ,EN-DC is replaced by the sum of the linear powers of PPowerClass,NR and PPowerClass,E-UTRA converted to dB if the UE indicates higherPowerLimitMRDC-r17.

Table 6.2B.4.1.3-1: PCMAX evaluation window

For each TREF, the PCMAX_H is evaluated per Teval and given by the maximum value over the transmission(s) within the Teval as follows:

PCMAX_H  = MAX { PCMAX_ EN-DC _H (p,q) , PCMAX_ EN-DC _H (p,q+1), … , PCMAX_ EN-DC _H (p,q+n) }

where PCMAX_ EN-DC _H are the applicable upper limits for each overlapping scheduling unit pairs (p,q) , (p, q+1) , up to (p, q+n) for each applicable Teval duration, where q+n is the last NR UL physical-channel overlapping with E-UTRA subframe p.

While PCMAX_L is computed as follows:

PCMAX_L = MIN { PCMAX_ EN-DC _L (p,q) , PCMAX_ EN-DC _L (p,q+1), … , PCMAX_ EN-DC _L (p,q+n)}

where PCMAX_EN-DC_L are the applicable lower limits for each overlapping scheduling unit pairs (p,q) , (p, q+1) , up to (p, q+n) for each applicable Teval duration, where q+n is the last NR UL physical-channel overlapping with E-UTRA subframe p,

With

PCMAX_ EN-DC _H(p,q) = MIN {10 log10 [pCMAX H _ E-UTRA,c (p) + pCMAX H,f,c,NR (q)], PEMAX, EN-DC ,PPowerClass, EN-DC}

And:

a= 10 log10 [pCMAX_ E-UTRA,c (p) +pCMAX,f,c,NR (q) ] > PTotalEN-DC

b= 10 log10 [pCMAX_ E-UTRA,c (p) +pCMAX,f,c,NR (q) /X_scale] > PTotalEN-DC

If a= FALSE

PCMAX_ EN-DC _L(p,q) = MIN {10 log10 [pCMAX L _ E-UTRA,c (p) + pCMAX L,f,c,NR (q)], PEMAX, EN-DC ,PPowerClass, EN-DC}

ELSE If (a=TRUE) AND (b=FALSE)

PCMAX_ EN-DC _L(p,q) = MIN {10 log10 [pCMAX L _ E-UTRA,c (p) + pCMAX L,f,c,NR (q) /X_scale ], PEMAX, EN-DC ,PPowerClass, EN-DC}

ELSE If b= TRUE

PCMAX_ EN-DC _L(p,q) = MIN {10 log10 [pCMAX L _ E-UTRA,c (p) ], PEMAX, EN-DC ,PPowerClass, EN-DC}

where

-pCMAX H _ E-UTRA,c (p) is the E-UTRA higher limit of the maximum configured power expressed in linear scale;

-pCMAX L,f,c,NR (q) is the NR higher limit of the maximum configured power expressed in linear scale;

-pCMAX L _ E-UTRA,c (p) is the E-UTRA lower limit of the maximum configured power expressed in linear scale;

-pCMAX L,f,c,NR (q) is the NR lower limit of the maximum configured power expressed in linear scale;

-PPowerClass, EN-DC is defined in clause 6.2B.1.3-1 for inter-band EN-DC; if the UE indicates higherPowerLimitMRDC-r17, PPowerClass,EN-DC is replaced by the sum of the linear powers of PPowerClass,NR and PPowerClass,E-UTRA converted to dB;

-X_scale is the linear value of X dB which is configured by RRC and can only take values [0 , 6]

-pCMAX_ E-UTRA,c (p) is the linear value of PCMAX_ E-UTRA,c (p), the configured max power for E-UTRA. If more than one E-UTRA uplink serving cell is configured as intra-band UL CA in the E-UTRA CG, PCMAX_ E-UTRA,c (p) will be replaced by PCMAX(p) which is the configured maximum power for the entire E-UTRA CG.

-pCMAX,f,c,NR (q) is the linear value of PCMAX,f,c,NR (q), the configured max power of NR, If more than one NR uplink serving cell is configured as intra-band UL CA in the NR CG,  PCMAX_ NR,c (q) will be replaced by PCMAX(q) which is the configured maximum power for the entire NR CG.

Table 6.2B.4.1.3-2: PCMAX tolerance for Dual Connectivity E-UTRA-NR

When E-UTRA and NR transmissions overlap and the condition (If (a=TRUE) AND (b=FALSE)) is met, SCG shall be transmitted and the following supplementary minimum requirement apply for the measured SCG power, PUMAX,f,c,NR (q), under nominal conditions.

10log(pCMAX L,f,c,NR (q)/X_scale)  –  TLOW (10log(pCMAX L,f,c,NR (q)/X_scale) )}  ≤  PUMAX,f,c,NR (q) ≤  10log(pCMAX H, f,c,NR (q)) + THIGH (10log(pCMAX H, f,c,NR (q))).

with the tolerances TLOW and THIGH for applicable values of PCMAX specified in Table 6.2B.4.1.3-2.

## 6.2B.4.1.3aInter-band NE-DC within FR1

For inter-band dual connectivity with one uplink serving cell per CG on E-UTRA and NR respectively, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of CG i, i = 1,2, and its total configured maximum transmission  power for NE-DC operation, = 10log10() with  as specified in clause 7.6.1A of TS 38.213 [10].PTotalNE-DCPtotalNE-DCPtotalNE-DC

The configured maximum output power PCMAX_ E-UTRA,c (p) in sub-frame p for the configured E-UTRA uplink carrier shall be set within the bounds:

PCMAX_L_ E-UTRA,c (p) ≤  PCMAX_ E-UTRA,c (p) ≤  PCMAX H _ E-UTRA,c (p)

where PCMAX_L_ E-UTRA,c and PCMAX H _ E-UTRA,c are the limits for a serving cell c as specified in TS 36.101 [4] clause 6.2.5 modified by PLTE as follows:

PCMAX_L_ E-UTRA,c = MIN { PEMAX, NE-DC , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), MIN(PEMAX,c , PLTE) – tC_ E-UTRA, c,  (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA) – MAX(MPRc + A-MPRc + ΔTIB,c  + TC_ E-UTRA, c + TProSe, P-MPRc)}

PCMAX H _ E-UTRA,c = MIN {PEMAX,c,  PEMAX, NE-DC  , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), PLTE, PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA}

with exception that

-if no symbol of slot  of the NR that is indicated as uplink or flexible by TDD-UL-DL-ConfigurationCommon or TDD-UL-DL-ConfigDedicated overlaps with subframe  of the E-UTRA; or

-if NR slot(s) that is indicated as downlink by TDD-UL-DL-ConfigurationCommon or TDD-UL-DL-ConfigDedicated does not overlap with subframe  of the E-UTRA; then

PCMAX_L_ E-UTRA,c = MIN { PEMAX, NE-DC , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), PEMAX,c  – tC_ E-UTRA, c,  (PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA) – MAX(MPRc + A-MPRc + ΔTIB,c  + TC_ E-UTRA, c + TProSe, P-MPRc)}

PCMAX H _ E-UTRA,c = MIN {PEMAX,c,  PEMAX, NE-DC  , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), PPowerClass,E-UTRA – ΔPPowerClass,E-UTRA}

The configured maximum output power PCMAX,f,c,NR (q) in physical-channel q for the configured NR carrier shall be set within the bounds:

PCMAX_L,f,c,NR (q) ≤  PCMAX,f,c,NR (q) ≤  PCMAX_H,f,c,NR (q)

where PCMAX_L,f,c,NR and PCMAX_H,f,c,NR are the limits for a serving cell c as specified in clause 6.2.4 of TS 38.101-1 [2] modified by PNR as follows:

PCMAX_L,f,c,NR = MIN { PEMAX, NE-DC  , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), MIN(PEMAX,c , PNR ) - TC_NR, c,  (PPowerClass,NR – ΔPPowerClass,NR) – MAX(MPRc + A-MPRc+ ΔTIB,c + TC_NR, c + ∆TRxSRS,  P-MPRc) }

PCMAX_H,f,c,NR = MIN {PEMAX,c, PEMAX, NE-DC  , (PPowerClass, NE-DC – ΔPPowerClass,NE-DC ), PNR , PPowerClass,NR – ΔPPowerClass,NR }

-PEMAX,NE-DC signalled by RRC as p-UE-FR1 in TS 38.331 [9];

-PLTE signalled by RRC as p-MaxEUTRA in TS 36.331 [8];

-PNR signalled by RRC as p-NR-FR1 defined in TS 38.331 [9];

-ΔTc_E-UTRA, c = 1.5dB when NOTE 2 in Table 6.2.2-1 in TS 36.101 [4] applies for a serving cell c, otherwise TC_ E-UTRA,c = 0dB;

-TC_NR,c = 1.5dB when NOTE 3 in Table 6.2.1-1 in TS 38.101-1 [2] applies for a serving cell c, otherwise TC_NR,c = 0dB;

-ΔTIB,c specified in clause  6.2B.4.2.3 for NE-DC, the individual Power Class defined in table 6.2B.1.3a and any other additional power reductions parameters specified in clauses  6.2B.2.3a for NE-DC are applicable to PCMAX_ E-UTRA,c and PCMAX,f,c,NR evaluations.

-PPowerClass, NE-DC is defined in clause 6.2B.1.3a for inter-band NE-DC;

-PPowerClass,NR is the nominal UE power of the power class that the UE supports for the NR band of the NE-DC combination as defined in clause 6.2.1 of 38.101-1 [2]; in case powerClassNRPart as defined in TS 38.331 [9] is indicated, PPowerClass,NR should use that value instead.

-PPowerClass,E-UTRA is the nominal UE power of the power class that the UE supports for the E-UTRA band of the NE-DC combination as defined in clause 6.2.2 of 36.101 [4];

-ΔPPowerClass,NE-DC = 3 dB for a power class 2 capable NE-DC UE when requirements of default power class had been applied as specified in sub-clause 6.2B.1; otherwise ΔPPowerClass,NE-DC = 0 dB;

If the transmissions from NR and E-UTRA do not overlap, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications apply with the modifications specified above. The lower value between PPowerClass, NE-DC or PEMAX, NE-DC shall not be exceeded at any time by UE.

= 10log10() with  the configured maximum transmission power for NE-DC operation as specified in clause 7.6 of TS 38.213 [10].PTotalNE-DCPtotalNE-DCPTotalNE-DC

The total configured maximum transmission power for both synchronous and non-synchronous operation is

= MIN { PEMAX, NE-DC ,PPowerClass, NE-DC – ΔPPowerClass, NE-DC }PTotalNE-DC

If the UE does not support dynamic power sharing,

= MIN { PEMAX, NE-DC ,PPowerClass, NE-DC  – ΔPPowerClass, NE-DC } + 0.3 dBPTotalNE-DC

If the NE-DC UE does not support dynamic power sharing, then the complete clauses for configured transmitted power for E-UTRA and NR respectively from their own specifications TS 36.101 [4] and TS 38.101-1 [2] respectively apply with the modifications specified above and  applies.PTotalNE-DC

When a UE supporting dynamic  sharing is configured for overlapping E-UTRA uplink and NR uplink transmissions, the UE can set its configured maximum output power PCMAX_ E-UTRA,c and PCMAX,f,c,NR for the configured E-UTRA and NR uplink carriers, respectively, and its configured maximum transmission power for NE-DC operation, , as specified above.PTotalNE-DC

The measured total maximum output power PUMAX over both CGs/RATs, measured over the transmission reference time duration is

PUMAX = 10 log10 [pUMAX,c,E-UTRA + pUMAX,c,NR],

where pUMAX,c,E-UTRA and pUMAX,c,NR denotes the measured output power of serving cell c for E-UTRA and NR respectively, expressed in linear scale.

The measured total configured maximum output power PUMAX shall be within the following bounds:

PCMAX_L -TLOW (PCMAX_L)  ≤  PUMAX  ≤  PCMAX_H + THIGH (PCMAX_H)

with the tolerances TLOW(PCMAX_L) and THIGH(PCMAX_H) for applicable values of PCMAX specified in Table 6.2B.4.1.3a-2.

When an UL subframe transmission p from E-UTRA overlap with a physical-channel q from the NR, then for PUMAX evaluation, the E-UTRA subframe p is taken as reference period TREF and always considered as the reference measurement duration and the following rules are applicable.

TREF and Teval are specified in Table 6.2B.4.1.3a-1 when same or different subframe and physical-channel durations are used in aggregated carriers. PPowerClass ,NE-DC shall not be exceeded by the UE during any evaluation period of time.

Table 6.2B.4.1.3a-1: PCMAX evaluation window

For each TREF, the PCMAX_H is evaluated per Teval and given by the maximum value over the transmission(s) within the Teval as follows:

PCMAX_H  = MAX { PCMAX_ NE-DC _H (p,q) , PCMAX_ NE-DC _H (p,q+1), … , PCMAX_ NE-DC _H (p,q+n) }

where PCMAX_ NE-DC _H are the applicable upper limits for each overlapping scheduling unit pairs (p,q) , (p, q+1) , up to (p, q+n) for each applicable Teval duration, where q+n is the last NR UL physical-channel overlapping with LTE subframe p.

While PCMAX_L is computed as follows:

PCMAX_L = MIN { PCMAX_ NE-DC _L (p,q) , PCMAX_ NE-DC _L (p,q+1), … , PCMAX_ NE-DC _L (p,q+n)}

where PCMAX_NE-DC_L are the applicable lower limits for each overlapping scheduling unit pairs (p,q) , (p, q+1) , up to (p, q+n) for each applicable Teval duration, where q+n is the last NR UL physical-channel overlapping with LTE subframe p,

With

PCMAX_ NE-DC _H(p,q) = MIN {10 log10 [pCMAX H _ E-UTRA,c (p) + pCMAX H,f,c,NR (q)], PEMAX, NE-DC ,PPowerClass, NE-DC}

And:

a = 10 log10 [pCMAX_ E-UTRA,c (p) +pCMAX,f,c,NR (q) ] > PTotalNE-DC

If a = TRUE

PCMAX_ NE-DC _L(p,q) = MIN {10 log10 [pCMAX L _ E-UTRA,c (p) ], PEMAX, NE-DC ,PPowerClass, NE-DC}

Else

PCMAX_ NE-DC _L(p,q) = MIN {10 log10 [pCMAX L _ E-UTRA,c (p) + pCMAX L,f,c,NR (q)], PEMAX, NE-DC ,PPowerClass, NE-DC}

where

-pCMAX H _ E-UTRA,c (p) is the E-UTRA higher limit of the maximum configured power expressed in linear scale;

-pCMAX H,f,c,NR (q) is the NR higher limit of the maximum configured power expressed in linear scale;

-pCMAX L _ E-UTRA,c (p) is the E-UTRA lower limit of the maximum configured power expressed in linear scale;

-pCMAX L,f,c,NR (q) is the NR lower limit of the maximum configured power expressed in linear scale;

-PPowerClass, NE-DC is defined in clause 6.2B.1.3a for inter-band NE-DC;

-pCMAX_ E-UTRA,c (p) is the linear value of PCMAX_ E-UTRA,c (p), the real configured max power for E-UTRA

-pCMAX,f,c,NR (q) is the linear value of PCMAX,f,c,NR (q), the real configured max power of NR

Table 6.2B.4.1.3a-2: PCMAX tolerance for Dual Connectivity E-UTRA-NR

When E-UTRA and NR transmissions overlap and the condition a = TRUE, PUMAX,f,c,NR (q) for MCG, under nominal conditions, shall meet

PUMAX,f,c,NR (q) ≤  10log(pCMAX H, f,c,,NR c (q)) + THIGH (10log(pCMAX H, f,c,,NR c (q))).

with the tolerances TLOW and THIGH for applicable values of PCMAX specified in Table 6.2B.4a.1.3-2.

When LTE and NR transmissions overlap and the condition a = FALSE), then PUMAX, under nominal conditions, shall be within the following bounds:

PCMAX_L -TLOW (PCMAX_L)  ≤  PUMAX  ≤  PCMAX_H + THIGH (PCMAX_H)

where PCMAX_L, PCMAX_H, and PUMAX are specified above with the tolerances TLOW and THIGH specified in Table 6.2B.4a.1.3-2 for applicable values of PCMAX_L and PCMAX_H.

## 6.2B.4.1.4Inter-band EN-DC including FR2

For inter-band dual connectivity with one uplink serving cell per CG on E-UTRA and NR respectively, with NR configured in FR2, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of CG i, i = 1,2.

The UE maximum configured power PCMAX,c(i), on E-UTRA for the subframe i shall be set according to clause 6.2.5 from TS 36.101 [4]. Applicable inter-band ΔTIB,c parameters shall be used according to the clauses 6.2B.4.2.4 or 6.2B.4.2.5.

The UE maximum configured power PCMAX,c(j), on NR for the slot j shall be set according to subclase 6.2.4 from TS 38.101-2 [3].

For the configured power measurements TS 36.101 [4] clause 6.2.5 and TS 38.101-2 [3] clause 6.2.4 are applicable.

## 6.2B.4.1.4a(Void)

## 6.2B.4.1.5Inter-band EN-DC including both FR1 and FR2

For inter-band dual connectivity with one uplink serving cell per CG on E-UTRA and NR respectively, with both CGs configured in FR1, the requirements specified in clause 6.2B.4.1.3 apply.

For inter-band dual connectivity with one uplink serving cell per CG on E-UTRA and NR respectively, with NR configured in FR2, the requirements specified in clause 6.2B.4.1.4 apply.

For inter-band dual connectivity with one uplink serving cell in first CG on E-UTRA and two uplink serving cells in second CG on NR FR1 and NR FR2 respectively, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) , i = 1,2,3 with i=1 for E-UTRA, i=2 for NR FR1 and i=3 for NR FR2.

–For serving cell on FR2, the requirements specified in clause 6.2.4 in TS 38.101-2 [3] apply to the UE maximum configured power PCMAX,c(3),3 and the measured maximum configured power.

–For remaining inter-band dual connectivity involving CG1 and CG2, the requirements specified in clause 6.2B.4.1.3 apply.

## 6.2B.4.2ΔTIB,c for DC

## 6.2B.4.2.0General

For the UE which supports inter-band EN-DC or NE-DC configuration, ΔTIB,c in Tables below applies where unless otherwise stated, the same ΔTIB,c is applicable to NR band(s) part for DC configurations which have the same NR operating band combination. Unless otherwise stated, ΔTIB,c is set to zero.

Unless ΔTIB,c  is specified for the NE-DC configuration, the specified ΔTIB,c  for the EN-DC configuration including same bands as the corresponding NE-DC configuration is applicable for the NE-DC configuration.

## 6.2B.4.2.1Intra-band contiguous EN-DC

ΔTIB,c is not applicable for intra-band contiguous EN-DC.

## 6.2B.4.2.1a(Void)

## 6.2B.4.2.2Intra-band non-contiguous EN-DC

ΔTIB,c is not applicable for intra-band non-contiguous EN-DC.

## 6.2B.4.2.3Inter-band EN-DC within FR1

## 6.2B.4.2.3.1ΔTIB,c for EN-DC two bands

Table 6.2B.4.2.3.1-1: ΔTIB,c due to EN-DC(two bands)

## 6.2B.4.2.3.2ΔTIB,c for EN-DC three bands

Table 6.2B.4.2.3.2-1: ΔTIB,c due to EN-DC (three bands)

## 6.2B.4.2.3.3ΔTIB,c for EN-DC four bands

Table 6.2B.4.2.3.3-1: ΔTIB,c due to EN-DC(four bands)

## 6.2B.4.2.3.4ΔTIB,c for EN-DC five bands

Table 6.2B.4.2.3.4-1: ΔTIB,c due to EN-DC (five bands)

## 6.2B.4.2.3.5ΔTIB,c for EN-DC six bands

Table 6.2B.4.2.3.5-1: ΔTIB,c due to EN-DC (six bands)

## 6.2B.4.2.3aInter-band NE-DC within FR1

Unless ΔTIB,c  is specified in this clause, the value of ΔTIB,c  for the correspondingly specified EN-DC configuration in clause 6.2B.4.2.3 is applicable.

Table 6.2B.4.2.3a-1: ΔTIB,c due to NE-DC (two bands)

## 6.2B.4.2.4Inter-band EN-DC including FR2

## 6.2B.4.2.4.1ΔTIB,c for EN-DC two bands

Unless otherwise stated, ΔTIB,c for E-UTRA and FR2 NR bands of inter-band EN-DC combinations defined in table 5.5B.5.1-1 is set to zero.

Table 6.2B.4.2.4.1-1: Void

## 6.2B.4.2.4.2ΔTIB,c for EN-DC three bands

Unless otherwise stated, ΔTIB,c for FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA bands for inter-band EN-DC defined in table 5.5B.5.2-1 is the same as those for the corresponding E-UTRA CA configuration specified in TS 36.101 [4], without the FR2 NR bands.

Table 6.2B.4.2.4.2-1: Void

## 6.2B.4.2.4.3ΔTIB,c for EN-DC four bands

Unless otherwise stated, ΔTIB,c for FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA bands for inter-band EN-DC defined in table 5.5B.5.3-1 is the same as those for the corresponding E-UTRA CA configuration specified in TS 36.101 [4], without the FR2 NR bands.

Table 6.2B.4.2.4.3-1: Void

## 6.2B.4.2.4.4ΔTIB,c for EN-DC five bands

Unless otherwise stated, ΔTIB,c for FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA bands for inter-band EN-DC defined in table 5.5B.5.4-1 is the same as those for the corresponding E-UTRA CA configuration specified in TS 36.101 [4], without the FR2 NR bands.

Table 6.2B.4.2.4.4-1: Void

## 6.2B.4.2.4.5Void

## 6.2B.4.2.4a(Void)

## 6.2B.4.2.5Inter-band EN-DC including both FR1 and FR2

## 6.2B.4.2.5.1ΔTIB,c for EN-DC three bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.2-1, ΔTIB,c for constituent FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 6.2B.4.2.3.

Table 6.2B.4.2.5.1-1: Void

## 6.2B.4.2.5.2ΔTIB,c for EN-DC four bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.3-1, ΔTIB,c for constituent FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 6.2B.4.2.3.

## 6.2B.4.2.5.3ΔTIB,c for EN-DC five bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.4-1, ΔTIB,c for constituent FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA and FR1 NR bands   is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 6.2B.4.2.3.

## 6.2B.4.2.5.4ΔTIB,c for EN-DC six bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.5-1, ΔTIB,c for constituent FR2 NR bands is set to zero, and ΔTIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 6.2B.4.2.3.

## 6.2B.5Configured output power for NR-DC

## 6.2B.5.1Configured output power level

## 6.2B.5.1.1Inter-band NR-DC between FR1 and FR2

For both synchronous and non-synchronous inter-band NR-DC [12] with MCG in FR1 and SCG in FR2 combined with one uplink serving cell per CG, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of CG i, i = 1,2 as specified in clause 6.2.4 of TS 38.101-1 [2] and clause 6.2.4 TS 38.101-2 [3] independently.

For inter-band NR-DC between FR1 and FR2 with a single uplink component carrier configured in FR1, when the powerBoostPi2BPSK-r18 or powerBoostQPSK-r18 is set to 1 for a UE supporting the capability of powerBoosting-pi2BPSK-QPSK-Modified-r18 or powerBoosting-pi2BPSK-QPSK-r18, the configured maximum output power PCMAX,c  on serving cell c shall be set as specified for PCMAX,f,c in clause 6.2.4.

## 6.2ETransmitter power for V2X in FR1

## 6.2E.1UE maximum output power for V2X

## 6.2E.1.1UE maximum output power for Intra-band contiguous V2X

For intra-band contiguous V2X operating UE, the allowed UE maximum output power shall be applied in Table 6.2.2-1 [4] for E-UTRA SL transmission or applied in Table 6.2.1-1 [2] for NR SL transmission, respectively.

Table 6.2E.1.1-1: Maximum output power for V2X combination (continuous sub-blocks)

## 6.2E.1.2UE maximum output power for Intra-band non-contiguous V2X

For intra-band non-contiguous V2X operating UE, the allowed UE maximum output power shall be applied in Table 6.2.2-1 [4] for E-UTRA SL transmission or applied in Table 6.2.1-1 [2] for NR SL transmission, respectively.

Table 6.2E.1.2-1: Maximum output power for V2X combination (non-contiguous sub-blocks)

## 6.2E.1.3UE maximum output power for Inter-band V2X

For the NR V2X inter-band con-current operation, the maximum output power is specified in Table 6.2E.1.3-1 for each operating band. The period of measurement shall be at least one sub frame (1ms).

Table 6.2E.1.3-1: Con-current V2X UE Power Class

## 6.2E.2UE maximum output power reduction for V2X

## 6.2E.2.1UE maximum output power reduction for Intra-band V2X

For intra-band V2X operating UE, maximum output power reduction specified in clause 6.2.3G [4] and in clause 6.2E.2 [2] apply, respectively.

## 6.2E.2.2UE maximum output power reduction for Inter-band V2X

For the inter-band con-current NR V2X operation, the allowed maximum power reduction (MPR) for the maximum output power shall be applied per each component carrier. The MPR requirements in subclause 6.2.3 of TS 36.101 [4] apply for E-UTRA Uu operation in licensed band, and the MPR requirements in subclause 6.2E.2 of TS 38.101-1 [2] apply for NR sidelink operation. The MPR requirements in subclause 6.2.3G of TS 36.101 [4] apply for E-UTRA V2X operation, and the MPR requirements in subclause 6.2.2 of TS 38.101-1 [2] apply for NR Uu operation.

## 6.2E.3UE additional maximum output power reduction for V2X

## 6.2E.3.1UE additional maximum output power reduction for Intra-band V2X

For intra-band V2X operating UE, additional maximum output power reduction specified in clause 6.2.4G [4] and in clause 6.2C.3 [2] apply, respectively.

## 6.2E.3.2UE additional maximum output power reduction for Inter-band V2X

For the inter-band con-current NR V2X operation, the allowed additional maximum power reduction (A-MPR) for the maximum output power shall be applied per each component carrier. The A-MPR requirements in subclause 6.2.3 of TS 36.101 [4] apply for E-UTRA Uu operation in licensed band, and the A-MPR requirements in in subclause 6.2C.3 of TS 38.101-1 [2] apply for NR sidelink operation in Band n47.

## 6.2E.4Configured output power for V2X

## 6.2E.4.1UE configured output power for Intra-band V2X

For intra-band V2X operating UE, each UE configured output power specified in clause 6.2.5G [4] and in clause 6.2E.4 [2] apply, respectively.

## 6.2E.4.2UE configured output power for Inter-band V2X

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

## 6.2HTransmitter power for DC with UL MIMO

## 6.2H.1UE maximum output power for DC with UL MIMO

## 6.2H.1.1void

## 6.2H.1.2void

## 6.2H.1.3Inter-band EN-DC with UL MIMO within FR1

For inter-band EN-DC of E-UTRA and NR in FR1, the following UE Power Classes define the maximum output power for any transmission bandwidth within the aggregated channel bandwidth. The maximum output power is measured as the sum of the maximum output power at each UE antenna connector. The period of measurement shall be at least one sub frame (1ms). UE maximum output power shall be measured over all component carriers from different bands. If each band has separate antenna connectors, maximum output power is measured as the sum of maximum output power at each UE antenna connector.

The maximum output power for inter-band EN-DC with one Tx in E-UTRA band and 2Tx in NR band is specified in Table 6.2H.1.3-1. The per band power class for each band applicable to REFSENS exceptions for a given inter-band UL EN-DC power class are specified in Table 6.2H.3.1-1a. These configurations are subject to the applicable power class of each E-UTRA band and NR band specified in Table 6.2.2-1 of TS 36.101 and Table 6.2D.1-1 of TS 38.101-1 respectively.The power classes referenced are according to the reported ue-PowerClass-N-r13 for the E-UTRA band or ue-CA-PowerClass-N for the E-UTRA intra-band UL CA of the EN-DC combination, and reported powerClassNRPart-r16 for the NR band and for NR intra-band UL CA of the EN-DC combination if indicated or ue-PowerClass otherwise.

If higherPowerLimitMRDC-r17 is indicated for an UL inter-band EN-DC configuration as specified in Table 6.2H.1.3-1 and with uplink bands of different power class capabilities, the UE maximum output power specified in Table 6.2H.1.3-1 for this UL EN-DC configuration is modified in accordance with sub-clause 6.2H.4.1.3.

Table 6.2H.1.3-1: Maximum output power for inter-band EN-DC with UL MIMO and/or TxD (two bands)

Table 6.2H.1.3-1a: Per band power class applicable to REFSENS exceptions (two band UL EN-DC)

If a UE supports power class 2 for an E-UTRA TDD and NR TDD Inter-band EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 30% when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power of the default power class or lower;

–shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified sub-clause 6.2H.4;

–Else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS 38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present; or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 30% when maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent. (The exact evaluation period is no less than one radio frame):

–shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2H.4.

If a UE supports power class 1.5 for an E-UTRA TDD and NR TDD Inter-band EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 15% when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power of the default power class or lower;

–shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified sub-clause 6.2H.4;

–Else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.25*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 but less than or equal to 0.5*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS 38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present; or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 7.5% but less than or equal to 15% when maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent. (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power between 23dBm and 26dBm;

–shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2H.4.

–Else

–shall apply all requirements for the power class 1.5 and set the configured transmitted power class as specified in sub-clause 6.2H.4.

If a UE supports power class 2 for an E-UTRA FDD and NR TDD EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

If UE indicating the two capabilities maxUplinkDutyCycle-FDD-TDD-EN-DC1 and maxUplinkDutyCycle-FDD-TDD-EN-DC2:

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal tomaxUplinkDutyCycle-FDD-TDD-EN-DC1as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

–shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2H.4.

–else

–shall apply all requirements for the default power class and set the configured transmitted power as specified sub-clause 6.2H.4;

else

–shall apply all requirements for the power class 2 and set the configured transmitted power as specified sub-clause 6.2H.4;

If a UE supports power class 1.5 for an E-UTRA FDD and NR TDD EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

If UE indicating the two capabilities maxUplinkDutyCycle-FDD-TDD-EN-DC1 and maxUplinkDutyCycle-FDD-TDD-EN-DC2:

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC1as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

–shall apply all requirements for the power class 1.5 and set the configured transmitted power class as specified in sub-clause 6.2H.4.

–else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC1 but less than or equal to 1.0*maxUplinkDutyCycle-FDD-TDD-EN-DC1 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC2 but less than or equal to 1.0*maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

–shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2H.4.

–else

–shall apply all requirements for the default power class and set the configured transmitted power as specified sub-clause 6.2H.4;

else

–shall apply all requirements for the power class 1.5 and set the configured transmitted power as specified sub-clause 6.2H.4;

## 6.2H.2UE maximum output power reduction for DC with UL MIMO

## 6.2H.2.1void

## 6.2H.2.2void

## 6.2H.2.3Inter-band EN-DC with UL MIMO within FR1

For inter-band EN-DC between E-UTRA and FR1 NR, UE maximum output power reduction specified in TS 36.101 [4] and TS 38.101-1 [2] apply for E-UTRA and NR respectively.

## 6.2H.3UE additional maximum output power reduction for EN-DC with UL MIMO

## 6.2H.3.1void

## 6.2H.3.2void

## 6.2H.3.3Inter-band EN-DC with UL MIMO within FR1

For inter-band EN-DC with UL MIMO in NR band, unless specified in Table 6.2B.3.3-1, the requirements in [2] clause 6.2.3 apply for NR uplink component carrier and the requirements in [4] clause 6.2.4 apply for LTE uplink component carrier.

## 6.2H.4Configured output power for DC with UL MIMO

## 6.2H.4.1Configured output power level

## 6.2H.4.1.1void

## 6.2H.4.1.2void

6.2H.4.1.3Inter-band EN-DC with UL MIMO within FR1

For inter-band EN-DC with UL MIMO in one NR band, the requirements in clause 6.2B.4.1.3 apply except that:

-PPowerClass,EN-DC is the maximum UE power specified in Table 6.2H.1.3-1 without taking into account the tolerance; if the UE indicates higherPowerLimitMRDC-r17 for an UL inter-band EN-DC configuration with uplink bands of different power class capabilities specified in Table 6.2H.1.3-1 and ΔPPowerClass,EN-DC = 0, PPowerClass,EN-DC is replaced by the sum of the linear powers of PPowerClass,NR and PPowerClass,E-UTRA converted to dBm;

-If the NR component carrier is configured with UL MIMO, the MPRc and A-MPRc are specified in clause 6.2D.2 and clause 6.2D.3 of [2] respectively.

-∆PPowerClass,EN-DC:

–For a power class 2 capable UE, it is 3dB when the requirements of default power class are applied as specified in sub-clause 6.2H.1.3, otherwise ΔPPowerClass,EN-DC = 0 dB;

## 6.2LTransmitter power for DC with Tx Diversity

## 6.2L.1UE maximum output power for DC with Tx Diversity

## 6.2L.1.1void

## 6.2L.1.2void

## 6.2L.1.3Inter-band EN-DC with Tx Diversity within FR1

For inter-band EN-DC of E-UTRA and NR in FR1, the UE Power Classes in table 6.2H.1.3 define the maximum output power for any transmission bandwidth within the aggregated channel bandwidth. The maximum output power is measured as the sum of the maximum output power at each UE antenna connector. The period of measurement shall be at least one sub frame (1ms). UE maximum output power shall be measured over all component carriers from different bands. If each band has separate antenna connectors, maximum output power is measured as the sum of maximum output power at each UE antenna connector. The per band power class for each band applicable to REFSENS exceptions for a given inter-band UL EN-DC power class are specified in Table 6.2H.3.1-1a. These configurations are subject to the applicable power class of each E-UTRA band and NR band specified in Table 6.2.2-1 of TS 36.101 and Table 6.2.1-1 of TS 38.101-1 respectively. The power classes referenced are according to the reported ue-PowerClass-N-r13 for the E-UTRA band or ue-CA-PowerClass-N for the E-UTRA intra-band UL CA of the EN-DC combination, and reported powerClassNRPart-r16 for the NR band and for NR intra-band UL CA of the EN-DC combination if indicated or ue-PowerClass otherwise.

If higherPowerLimitMRDC-r17 is indicated for an UL inter-band EN-DC configuration with Tx Diversity as specified in Table 6.2H.1.3-1 and with uplink bands of different power class capabilities, the UE maximum output power specified in Table 6.2H.1.3-1 for EN-DC configuration is increased in accordance with sub-clause 6.2L.4.1.3.

If a UE supports power class 2 for an E-UTRA TDD and NR TDD Inter-band EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 30% when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power of the default power class or lower;

–shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified sub-clause 6.2L.4;

–Else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS 38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present; or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 30% when maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent. (The exact evaluation period is no less than one radio frame):

–shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2L.4.

If a UE supports power class 1.5 for an E-UTRA TDD and NR TDD Inter-band EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 15% when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power of the default power class or lower;

–shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified sub-clause 6.2L.4;

–Else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.25*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 but less than or equal to 0.5*maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 as defined in TS 38.331 when the field of UE capability maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is present; or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 7.5% but less than or equal to 15% when maxUplinkDutyCycle-interBandENDC-TDD-PC2-r16 is absent. (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is provided and set to the maximum output power between 23dBm and 26dBm;

–shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2L.4.

–Else

–shall apply all requirements for the power class 1.5 and set the configured transmitted power class as specified in sub-clause 6.2L.4.

If a UE supports power class 2 for an E-UTRA FDD and NR TDD EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

If UE indicating the two capabilities maxUplinkDutyCycle-FDD-TDD-EN-DC1 and maxUplinkDutyCycle-FDD-TDD-EN-DC2:

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal tomaxUplinkDutyCycle-FDD-TDD-EN-DC1as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

–shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2L.4.

–else

–shall apply all requirements for the default power class and set the configured transmitted power as specified sub-clause 6.2L.4;

else

–shall apply all requirements for the power class2  and set the configured transmitted power as specified sub-clause 6.2L.4;

If a UE supports power class 1.5 for an E-UTRA FDD and NR TDD EN-DC band combination and the supported power class enables higher maximum output power than that of the default power class:

If UE indicating the two capabilities maxUplinkDutyCycle-FDD-TDD-EN-DC1 and maxUplinkDutyCycle-FDD-TDD-EN-DC2:

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC1as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is less than or equal to 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

–shall apply all requirements for the power class 1.5 and set the configured transmitted power class as specified in sub-clause 6.2L.4.

–else if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is between 40% and 70%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC1 but less than or equal to 1.0*maxUplinkDutyCycle-FDD-TDD-EN-DC1 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

–if the IE p-maxUE-FR1 as defined in TS 38.331 is not provided or set to the higher value than the maximum output power of the default power class, and the percentage of EUTRA uplink symbols transmitted in a certain evaluation period is no larger than 40%, and the percentage of NR uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-FDD-TDD-EN-DC2 but less than or equal to 1.0*maxUplinkDutyCycle-FDD-TDD-EN-DC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame)

–shall apply all requirements for the power class 2 and set the configured transmitted power class as specified in sub-clause 6.2L.4.

–else

–shall apply all requirements for the default power class and set the configured transmitted power as specified sub-clause 6.2L.4;

else

–shall apply all requirements for the power class 1.5 and set the configured transmitted power as specified sub-clause 6.2L.4;

## 6.2L.2UE maximum output power reduction for DC with Tx Diversity

## 6.2L.2.1void

## 6.2L.2.2void

## 6.2L.2.3Inter-band EN-DC with Tx Diversity within FR1

For inter-band EN-DC between E-UTRA and FR1 NR, UE maximum output power reduction specified in TS 36.101 [4] and TS 38.101-1 [2] apply for E-UTRA and NR respectively.

## 6.2L.3UE additional maximum output power reduction for EN-DC with Tx Diversity

## 6.2L.3.1void

## 6.2L.3.2void

## 6.2L.3.3Inter-band EN-DC with Tx Diversity within FR1

For inter-band EN-DC with Tx Diversity in one NR band, unless specified in Table 6.2B.3.3-1, the requirements in [2] clause 6.2.3 apply for NR uplink component carrier and the requirements in [4] clause 6.2.4 apply for LTE uplink component carrier.

## 6.2L.4Configured output power for DC with Tx Diversity

## 6.2L.4.1Configured output power level

## 6.2L.4.1.1void

## 6.2L.4.1.2void

6.2L.4.1.3Inter-band EN-DC with Tx Diversity within FR1

For inter-band EN-DC with Tx Diversity in one NR band, the requirements in clause 6.2B.4.1.3 apply except that:

-PPowerClass,EN-DC is the maximum UE power specified in Table 6.2H.1.3-1 without taking into account the tolerance; if the UE indicates higherPowerLimitMRDC-r17 for an UL inter-band EN-DC configuration with uplink bands of different power class capabilities specified in Table 6.2H.1.3-1 and ΔPPowerClass,EN-DC = 0, PPowerClass,EN-DC is replaced by the sum of the linear powers of PPowerClass,NR and PPowerClass,E-UTRA converted to dBm;

-If the NR component carrier is configured with Tx Diversity, the MPRc and A-MPRc are specified in clause 6.2G.2 and clause 6.2G.3 of [2] respectively.

-∆PPowerClass,EN-DC:

–For a power class 2 capable UE, it is 3dB when the requirements of default power class are applied as specified in sub-clause 6.2L.1.3, otherwise ΔPPowerClass,EN-DC = 0 dB;

## 6.3Output power dynamics

Output power dynamics for EN-DC operations in FR1 and FR2 as specified in TS 38.101-1 [2] and TS 38.101-2 [3], respectively. E-UTRA as specified in TS 36.101 [4]. For intra-band contiguous EN-DC operation in FR1, minimum output power requirements specified in clause 6.3.1 of TS 38.101-1 [2] and clause 6.3.2 of TS 36.101 [4] shall only apply when the power of all NR and E-UTRA carriers are set to minimum value. Similarly, OFF power requirements specified in clause 6.3.2 of TS 38.101-1 [2] and clause 6.3.3 of TS 36.101 [4] shall only apply when the power of all NR and E-UTRA carriers are OFF. The OFF power condition in transmit ON/OFF time mask requirements specified in clause 6.3.3 of TS 38.101-1 [2] and clause 6.3.4 of TS 36.101 [4] is applicable only when all NR and E-UTRA carriers are OFF. If both E-UTRA and NR transition between ON and OFF states simultaneously, the longer transient time shall apply to both. If either E-UTRA or NR is OFF and the other carrier transitions from OFF to ON, then the transiet time associated with that carrier applies.

## 6.3AOutput power dynamics for CA

For inter-band NR CA between FR1 and FR2, output power dynamics as specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for FR1 and FR2 respectively.

## 6.3BOutput power dynamics for DC

## 6.3B.0General

The E-UTRA and NR switching time mask defines the observation period between E-UTRA subframe and NR slot/mini-slot boundary. Both E-UTRA subframe and NR slot/mini-slot have ON power transmissions. The ON power is defined as the mean power over the symbol duration excluding any transient period. For E-UTRA subframe or NR slot/mini-slot having OFF power transmission, the general time mask for E-UTRA or NR shall apply.

For inter-band EN-DC or NE-DC, output power dynamics requirement for E-UTRA single carrier and CA operation specified in clauses 6.3 and 6.3A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.3 and 6.3A of TS 38.101-1 [2] and  for NR single carrier, CA operation and UL-MIMO specified in clause 6.3, 6.3A and 6.3D of TS 38.101-2 [3] apply.

## 6.3B.1Output power dynamics for EN-DC with UL sharing from UE perspective

## 6.3B.1.1E-UTRA and NR switching time mask for TDM based UL sharing from UE perspective

The E-UTRA and NR switching time mask is applicable for non-simultaneous transmissions between E-UTRA and NR in TDM based UL sharing from the UE perspective in the same channel, which is shared by E-UTRA and NR. The requirement applies on the condition that UE is capable of handling the uplink transmission timing difference between E-UTRA and NR which is less than or equal to [2.21]μs.

For UEs reporting E-UTRA and NR switching time capability of type 1 with switching time < 0.5 us for TDM based UL sharing from UE perspective within FR1 time masks in Figure 6.3B.1.1-1 and Figure 6.3B.1.1-2 shall apply. For UEs reporting E-UTRA and NR switching time capability of type 2 with switching time < 20 us for TDM based UL sharing from UE perspective within FR1, time masks in Figure 6.3B.1.1-3 and Figure 6.3B.1.1-4 shall apply. The additional time for the transient period on the succeeding E-UTRA subframe or NR slot is caused by the uplink transmission timing difference, for which the maximum value is [2.21]μs.

20µs Transient period  E-UTRA subframe (10+2.21)µs ON power Requirement    NR slot/mini-slotON power Requirement  20µs Transient period  E-UTRA subframe (10+2.21)µs ON power Requirement    NR slot/mini-slotON power Requirement

Figure 6.3B.1.1-1: E-UTRA to NR switching time mask for type 1 for TDM based UL sharing from UE perspective within FR1

(20+2.21)µs Transient period E-UTRA subframe  NR slot/mini-slot10µs    ON power Requirement ON power Requirement  (20+2.21)µs Transient period E-UTRA subframe  NR slot/mini-slot10µs    ON power Requirement ON power Requirement

Figure 6.3B.1.1-2: NR to E-UTRA switching time mask for type 1 for TDM based UL sharing from UE perspective within FR1

20µs Transient period NR slot/mini-slot(10+2.21)µsON power requirement  ON power requirement  OFF power requirement      Transient period E-UTRA subframe20µs 20µs Transient period NR slot/mini-slot(10+2.21)µsON power requirement  ON power requirement  OFF power requirement      Transient period E-UTRA subframe20µs

Figure 6.3B.1.1-3: E-UTRA to NR switching time mask for type 2 for TDM based UL sharing from UE perspective within FR1

20µs Transient period NR slot/mini-slot   10µs ON power requirement  ON power requirement     Transient period OFF power requirement   (20+2.21)µsNR slot/mini-slotE-UTRA subframe 20µs Transient period NR slot/mini-slot   10µs ON power requirement  ON power requirement     Transient period OFF power requirement   (20+2.21)µsNR slot/mini-slotE-UTRA subframe

Figure 6.3B.1.1-4: NR to E-UTRA switching time mask for type 2 for TDM based UL sharing from UE perspective within FR1

## 6.3B.1a(Void)

## 6.3B.2Output power dynamics for intra-band EN-DC without dual PA capability

For intra-band contiguous and intra-band non-contiguous EN-DC configurations without dual PA capability, maximum UL switching time is defined as 120 us and DL reception interruption is allowed during UL switching. Time masks in Figure 6.3B.2-1 and Figure 6.3B.2-2 shall apply.

Figure 6.3B.2-1: E-UTRA to NR switching time mask for intra-band EN-DC without dual PA capabilitywhen single UL is allowed

Figure 6.3B.2-2: NR to E-UTRA switching time mask for intra-band EN-DC without dual PA capabilitywhen single UL is allowed

## 6.3B.2a(Void)

## 6.3B.3Output power dynamics for intra-band EN-DC with dual PA capability

For both intra-band contiguous and non-contiguous EN-DC with dual PA capability, time masks in Figure 6.3B.3-1 and Figure 6.3B.3-2 shall apply.

Figure 6.3B.3-1: E-UTRA to NR switching time mask for intra-band EN-DC with dual PA capability

Figure 6.3B.3-2: NR to E-UTRA switching time mask for intra-band EN-DC with dual PA capability

## 6.3B.3a(Void)

## 6.3B.4Output power dynamics for switching between two uplink carriers

## 6.3B.4.1E-UTRA and NR switching time mask between two uplink carriers

In addition to the requirements in 6.3B.0 and the maximum output power requirement specified in Table 6.2B.1.3-1 with inter-band EN-DC (two bands), the switching time mask specified in this sub-clause is applicable for an uplink band pair of a inter-band EN-DC configuration without SUL band when the capability uplinkTxSwitchingPeriod is present, and is only applicable for uplink switching mechanisms specified in sub-clause 6.1.6 of TS 38.214 [14], where E-UTRA UL carrier 1 is capable of one transmit antenna connector and NR UL carrier 2 is capable of two transmit antenna connectors, and the two uplink carriers are in different bands with different carrier frequencies. The UE shall support the switch between single layer transmission with one antenna port and two-layer transmission with two antenna ports on the two uplink carriers following the scheduling commands and rank adaptation, i.e., both single layer and two-layer transmission with 2 antenna ports, and single layer transmission with 1 antenna port shall be supported on NR UL carrier 2 as specified in [38.306].

The switching periods described in Figure 6.3B.4.1-1 are only located in NR carrier, and the length of uplink switching period X is less than the value indicated by UE capability uplinkTxSwitchingPeriod.

When switching from one carrier to another, if there is no uplink transmission scheduled or configured on the switch-from carrier for at least the duration of the switching period (X µs) before the point in time the UE is scheduled or configured to start the transmission on the switch-to carrier, the switching period is fully contained in the time period between the end of the transmission on the switch-from carrier and the start of the transmission on the switch-to carrier. In addition, the RRC signalling uplinkTxSwitchingPeriodLocation is ignored by the UE.

Figure 6.3B.4.1-1: Time mask for switching between E-UTRA UL carrier and NR UL carrier, where the switching period is located in NR carrier

The following applies for the uplink switching cases specified in clause 6.1.6.1 of [14] with uplinkTxSwitchingOption set to either switchedUL or dualUL when the configuration of the location of the switching period by uplinkTxSwitchingPeriodLocation is ignored by the UE:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [14] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the uplink switching gap indicated by uplinkTxSwitchingPeriod on any of the carriers before T0, transient periods of 10 s are located at the end of the last symbol(s) configured or scheduled on the carriers before T0 and at the start of the first symbol(s) configured or scheduled or configured at T0.

The requirements apply for the case of co-located and synchronized network deployment with the max receiving timing difference of 3us between the two carriers.

The time mask is applicable to uplink transmissions when configured with switchedUL or dualUL.

## 6.3B.5Output power dynamics for inter-band EN-DC

The switching time mask defined in this clause is applicable for a UE indicating support of IE singleUL-Transmission for the specific inter-band EN-DC combination for which only single switched UL is supported . The maximum UL switching time is defined as 120 us. Time masks in Figure 6.3B.5-1 and Figure 6.3B.5-2 shall apply.

Figure 6.3B.5-1: E-UTRA to NR switching time mask for inter-band EN-DC when only single switched UL is supported

Figure 6.3B.5-2: NR to E-UTRA switching time mask for inter-band EN-DC when only single switched UL is supported

## 6.3EOutput power dynamics for V2X

## 6.3E.1General

The E-UTRA SL and NR SL switching time mask defines the observation period between E-UTRA subframe and NR slot/mini-slot boundary. Both E-UTRA subframe and NR slot/mini-slot have ON power transmissions. The ON power is defined as the mean power over the symbol duration excluding any transient period. For E-UTRA subframe or NR slot/mini-slot having OFF power transmission, the general time mask for E-UTRA or NR shall apply.

## 6.3E.2Output power dynamics for intra-band V2X operation

For intra-band V2X operation bands specified in subclause 5.3E.1 and 5.3E.2, the SL switching time masks in Figure 6.3E.2-1 shall apply.

The switching time shall be located on the RAT of lower priority when NR SL and LTE SL have different priorities based on priority information specified in TS 38.213. It is up to UE implementation when NR SL and LTE SL have the same priority based on priority information specified in TS 38.213.

Figure 6.3E.2-1: Time mask for switching between NR SL and E-UTRA SL

## 6.3E.3Output power dynamics for inter-band V2X con-current operation

For inter-band con-current NR V2X operation, the output power dynamics requirement shall be applied per each component carrier. The output dynamic requirements specified in clause 6.3 of TS 36.101 [4] apply for E-UTRA UL transmission and the requirements specified in clause 6.3E of TS 38.101-1 [2] apply for NR SL transmission. The output dynamic requirements specified in clause 6.3.2G, 6.3.3G, 6.3.4G of TS 36.101 [4] apply for E-UTRA SL transmission and the requirements specified in clause 6.3 of TS 38.101-1 [2] apply for NR UL transmission.

## 6.3HOutput power dynamics for DC with UL MIMO

## 6.3H.0General

The E-UTRA and NR switching time mask defines the observation period between E-UTRA subframe and NR slot/mini-slot boundary. Both E-UTRA subframe and NR slot/mini-slot have ON power transmissions. The ON power is defined as the mean power over the symbol duration excluding any transient period. For E-UTRA subframe or NR slot/mini-slot having OFF power transmission, the general time mask for E-UTRA or NR shall apply.

For inter-band EN-DC with UL MIMO, output power dynamics requirement for E-UTRA single carrier operation specified in clauses 6.3 of TS 36.101 [4] and for NR single carrier with UL MIMO operation specified in clause 6.3D of TS 38.101-1 [2] apply.

## 6.3H.1void

## 6.3H.2void

## 6.3H.3Output power dynamics for inter-band EN-DC with UL MIMO

For a UE indicating support of IE singleUL-Transmission for the specific inter-band EN-DC combination with UL MIMO for which only single switched UL is supported, the requirements defined in 6.3B.5 apply.

## 6.3LOutput power dynamics for DC with Tx Diversity

## 6.3L.0General

The E-UTRA and NR switching time mask defines the observation period between E-UTRA subframe and NR slot/mini-slot boundary. Both E-UTRA subframe and NR slot/mini-slot have ON power transmissions. The ON power is defined as the mean power over the symbol duration excluding any transient period. For E-UTRA subframe or NR slot/mini-slot having OFF power transmission, the general time mask for E-UTRA or NR shall apply.

For inter-band EN-DC with Tx Diversity, output power dynamics requirement for E-UTRA single carrier operation specified in clauses 6.3 of TS 36.101 [4] and for NR single carrier with Tx Diversity operation specified in clause 6.3D of TS 38.101-1 [2] apply.

## 6.3L.1void

## 6.3L.2void

## 6.3L.3Output power dynamics for inter-band EN-DC with Tx Diversity

For a UE indicating support of IE singleUL-Transmission for the specific inter-band EN-DC combination with Tx Diversity for which only single switched UL is supported, the requirements defined in 6.3B.5 apply.

## 6.4Void

## 6.4ATransmit signal quality for CA

## 6.4A.1Frequency error for CA

For inter-band NR CA between FR1 and FR2, frequency error as specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for FR1 and FR2 respectively.

## 6.4A.2Transmit modulation quality for CA

For inter-band NR CA between FR1 and FR2, transmit modulation quality as specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for FR1 and FR2 respectively.

DMRS bundling requirements, as specified in clause 6.4.2.5 in TS 38.101-1 [2] and clause 6.4.2.6 in TS 38.101-2 [3], apply when one uplink band and CC is configured for DMRS bundling at a time. If UE needs to apply P-MPR as described in 6.2.4 of TS 38.101-1 or TS 38.101-2 during a granted DMRS bundle on any uplink CC, phase continuity is not expected to be maintained in the bundle.

## 6.4BTransmit signal quality for DC

## 6.4B.1Frequency error for DC

## 6.4B.1.1Frequency error for Intra-band contiguous EN-DC

For intra-band contiguous EN-DC, the requirement shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4.1 in TS 38.101-1 [2], respectively.

## 6.4B.1.1aFrequency error for Intra-band contiguous NE-DC

For intra-band contiguous NE-DC, the requirement shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4.1 in TS 38.101-1 [2], respectively.

## 6.4B.1.2Frequency error for Intra-band non-contiguous EN-DC

For intra-band non-contiguous EN-DC, the requirement shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4.1 in TS 38.101-1 [2], respectively.

## 6.4B.1.3Frequency error for inter-band EN-DC within FR1

For inter-band EN-DC with uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4.1 in TS 38.101-1 [2], respectively, with all component carriers active. If multiple component carriers are assigned to one E-UTRA band, the requirements in clauses 6.5.1A in TS 36.101 [4] apply for those component carriers.

## 6.4B.1.3aFrequency error for inter-band NE-DC within FR1

For inter-band NE-DC with uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4.1 in TS 38.101-1 [2], respectively, with all component carriers active. If multiple component carriers are assigned to one E-UTRA band, the requirements in clauses 6.5.1A in TS 36.101 [4] apply for those component carriers, and if multiple component carriers are assigned to one NR band, the requirements in clauses 6.4A.1 in TS 38.101-1 [2] apply for those component carriers.

## 6.4B.1.4Frequency error for inter-band EN-DC including FR2

Frequency error requirement for E-UTRA single carrier and CA operation specified in clauses 6.5.1 and 6.5.1A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.4.1, 6.4A.1 and 6.4D.1 of TS 38.101-2 [3] apply.

## 6.4B.1.4a(Void)

## 6.4B.1.5Frequency error for inter-band EN-DC including both FR1 and FR2

Frequency error requirement for E-UTRA single carrier and CA operation specified in clauses 6.5.1 and 6.5.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.4.1 and 6.4A.1 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.4.1, 6.4A.1 and 6.4D.1 of TS 38.101-2 [3] apply.

## 6.4B.2Transmit modulation quality for DC

## 6.4B.2.1Transmit modulation quality for Intra-band contiguous EN-DC

## 6.4B.2.1.1Error Vector Magnitude

For the intra-band contiguous EN-DC with one component carrier per CG the EVM requirement applies with PRB allocation in one of the CG and the other CG unallocated.

The EVM requirements for each CG are according to clause 6.5.2 of TS 36.101 [4] for the MCG and 6.4.2 of TS 38.101-1 [2] for the SCG with EN-DC configured.

## 6.4B.2.1.2Carrier leakage

The carrier leakage requirements for each CG are according to clause 6.5.2 of TS 36.101 [4] for the MCG and 6.4.2 of TS 38.101-1 [2] for the SCG with EN-DC configured.

## 6.4B.2.1.3In-band emissions

For the MCG the in-band emission requirments in Table 6.5.2A.3.1-1 and 6.5.2A.3.1-2 in TS 36.101 [4] apply within the aggregated transmission bandwidth configuration of the EN-DC bandwidth with the carriers of both CGs active and one single contiguous PRB allocation of bandwidth LCRB within the MCG at the edge of the said aggregated transmission bandwidth configuration.

For the SCG the in-band emission requirements in Table 6.4.2.3-1 in TS 38.101-1 [2] apply within the aggregated transmission bandwidth configuration of the EN-DC bandwidth with the carriers of both CGs active and one single contiguous PRB allocation of bandwidth LCRB within the SCG at the edge of the aggregated transmission bandwidth configuration.

## 6.4B.2.1aTransmit modulation quality for Intra-band contiguous NE-DC

## 6.4B.2.1a.1Error Vector Magnitude

For the intra-band contiguous NE-DC with one component carrier per CG the EVM requirement applies with PRB allocation in one of the CG and the other CG unallocated.

The EVM requirements for each CG are according to clause 6.4.2 of TS 38.101-1 [2] for the MCG and 6.5.2 of TS 36.101 [4] for the SCG with NE-DC configured.

## 6.4B.2.1a.2Carrier leakage

The carrier leakage requirements for each CG are according to clause 6.4.2 of TS 38.101-1 [2] for the MCG and 6.5.2 of TS 36.101 [4] for the SCG with NE-DC configured.

## 6.4B.2.1a.3In-band emissions

For the MCG the in-band emission requirements in Table 6.4.2.3-1 in TS 38.101-1 [2] are applied within the aggregated transmission bandwidth configuration of the NE-DC bandwidth with the carriers of both CGs active and one single contiguous PRB allocation of bandwidth LCRB within the MCG at the edge of the aggregated transmission bandwidth configuration.

For the SCG the in-band emission requirements in Table 6.5.2A.3.1-1 and 6.5.2A.3.1-2 in TS 36.101 [4] are applied, within the aggregated transmission bandwidth configuration of the NE-DC bandwidth with the carriers of both CGs active and one single contiguous PRB allocation of bandwidth LCRB within the SCG at the edge of the said aggregated transmission bandwidth configuration.

## 6.4B.2.2Transmit modulation quality for Intra-band non-contiguous EN-DC

## 6.4B.2.2.1Error Vector Magnitude

For the intra-band non-contiguous EN-DC with one component carrier per CG the EVM requirement applies with PRB allocation in one of the CG and the other CG unallocated.

The EVM requirements for each CG are according to clause 6.5.2 of TS 36.101 [4] for the MCG and 6.4.2 of TS 38.101-1 [2] for the SCG with EN-DC configured.

## 6.4B.2.2.2Carrier leakage

The carrier leakage requirements for each CG are according to clause 6.5.2 of TS 36.101 [4] for the MCG and 6.4.2 of TS 38.101-1 [2] for the SCG with EN-DC configured and PRB allocation only in the CG being measured.

## 6.4B.2.2.3In-band emissions

For the MCG the in-band emission requirements in Table 6.5.2A.3.1-1 and 6.5.2A.3.1-2 in TS 36.101 [4] apply within the transmission bandwidth configuration of the MCG with the carriers of both CGs active and one single contiguous PRB allocation of bandwidth LCRB within the MCG at the edge of the transmission bandwidth configuration.

For the SCG the in-band emission requirements in Table 6.4.2.3-1 in TS 38.101-1 [2] apply within the transmission bandwidth configuration of the SCG with the carriers of both CGs active and one single contiguous PRB allocation of bandwidth LCRB within the SCG at the edge of the transmission bandwidth configuration.

6.4B.2.3Transmit modulation quality for Inter-band EN-DC within FR1

For inter-band EN-DC with uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.2 in TS 36.101 [4] and in clause 6.4.2 in TS 38.101-1 [2], respectively, with all component carriers active, applies with PRB allocation in one of the CG and the other CG unallocated. If multiple component carriers are assigned to one E-UTRA band, the requirements in subclauses 6.5.2A in TS 36.101 [4] apply for those component carriers.

## 6.4B.2.3aTransmit modulation quality for Inter-band NE-DC within FR1

For inter-band NE-DC with uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.2 in TS 36.101 [4] and in clause 6.4.2 in TS 38.101-1 [2], respectively, with all component carriers active, applies with PRB allocation in one of the CG and the other CG unallocated. If multiple component carriers are assigned to one E-UTRA band, the requirements in clauses 6.5.2A in TS 36.101 [4] apply for those component carriers, and if multiple component carriers are assigned to one NR band, the requirements in clauses 6.4A.2 in TS 38.101-1 [2] apply for those component carriers.

## 6.4B.2.4Transmit modulation quality for Inter-band EN-DC including FR2

Transmit modulation quality requirement for E-UTRA single carrier and CA operation specified in clauses 6.5.2 and 6.5.2A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.4.2, 6.4A.2 and 6.4D.2 of TS 38.101-2 [3] apply.

DMRS bundling requirements, as specified in clause 6.4.2.6 in TS 38.101-2 [3], apply when one uplink band and CC is configured for DMRS bundling at a time. If UE is needs to apply P-MPR as described in 6.2.5of TS 36.101-1 or 6.2.4 of TS 38.101-2, during a granted DMRS bundle on the uplink CC of FR2, phase continuity is not expected to be maintained in the bundle.

## 6.4B.2.4a(Void)

## 6.4B.2.5Transmit modulation quality for inter-band EN-DC including both FR1 and FR2

Transmit modulation quality requirement for E-UTRA single carrier and CA operation specified in clauses 6.5.2 and 6.5.2A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.4.2 and 6.4A.2  of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.4.2, 6.4A.2 and 6.4D.2 of TS 38.101-2 [3] apply.

## 6.4ETransmit signal quality for V2X operation in FR1

## 6.4E.1Frequency error for V2X

For intra-band V2X operating UE, the requirement shall apply on each component carrier as defined in clause 6.5.1G in TS 36.101 [4] and in clause 6.4E.1 in TS 38.101-1 [2], respectively.

For the inter-band con-current NR V2X operation, the requirements specified in subclause 6.4.1 of TS 36.101 [4] shall apply for the E-UTRA uplink in licensed band and the requirements specified in subclause 6.4E.1 of TS 38.101-1 [2] shall apply for the sidelink in NR Band n47.

## 6.4E.2Transmit modulation quality for V2X

## 6.4E.2.1Transmit modulation quality for Intra-band V2X

## 6.4E.2.2.1Error Vector Magnitude

For intra-band V2X operating UE, the requirement shall apply on each SL transmission as defined in clause 6.5.2G.1 in TS 36.101 [4] and in clause 6.4E.2.1 in TS 38.101-1 [2], respectively.

For the inter-band con-current NR V2X operation, the requirements specified in subclause 6.5.2 of TS 36.101 [4] shall apply for the E-UTRA uplink in licensed band and the requirements specified in subclause 6.4E.2.1 of TS 38.101-1 [2] shall apply for the sidelink in NR Band n47.

## 6.4E.2.2.2Carrier leakage

For intra-band V2X operating UE, the requirement shall apply on each SL transmission as defined in clause 6.5.2G.2 in TS 36.101 [4] and in clause 6.4E.2.2 in TS 38.101-1 [2], respectively.

## 6.4E.2.2.3In-band emissions

For intra-band V2X operating UE, the requirement shall apply on each SL transmission as defined in clause 6.5.2G.3 in TS 36.101 [4] and in clause 6.4E.2.3 in TS 38.101-1 [2], respectively.

## 6.4E.2.2Transmit modulation quality for Inter-band V2X

For inter-band V2X with transmission assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.2 in TS 36.101 [4] and in clause 6.4.2 in TS 38.101-1 [2], respectively, with all component carriers active. If multiple component carriers are assigned to one E-UTRA band, the requirements in clauses 6.5.2A in TS 36.101 [4] apply for those component carriers.

## 6.4HTransmit signal quality for DC with UL MIMO

## 6.4H.1Frequency error for DC with UL MIMO

## 6.4H.1.1void

## 6.4H.1.2void

## 6.4H.1.3Frequency error for inter-band EN-DC with UL MIMO within FR1

For inter-band EN-DC with UL MIMO and uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4D.1 in TS 38.101-1 [2], respectively, with all component carriers active.

## 6.4H.2Transmit modulation quality for DC with UL MIMO

## 6.4H.2.1void

## 6.4H.2.2void

## 6.4H.2.3Transmit modulation quality for inter-band EN-DC with UL MIMO within FR1

For inter-band EN-DC with UL MIMO and uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.2 in TS 36.101 [4] and in clause 6.4D.2 in TS 38.101-1 [2], respectively, with all component carriers active.

## 6.4LTransmit signal quality for DC with Tx Diversity

## 6.4L.1Frequency error for DC with Tx Diversity

## 6.4L.1.1void

## 6.4L.1.2void

## 6.4L.1.3Frequency error for inter-band EN-DC with Tx Diversity within FR1

For inter-band EN-DC with Tx Diversity and uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.1 in TS 36.101 [4] and in clause 6.4G.1 in TS 38.101-1 [2], respectively, with all component carriers active.

## 6.4L.2Transmit modulation quality for DC with Tx Diversity

## 6.4L.2.1void

## 6.4L.2.2void

## 6.4L.2.3Transmit modulation quality for inter-band EN-DC with Tx Diversity within FR1

For inter-band EN-DC with Tx Diversity and uplink assigned to one E-UTRA band and one NR band, the requirements shall apply on each component carrier as defined in clause 6.5.2 in TS 36.101 [4] and in clause 6.4G.2 in TS 38.101-1 [2], respectively, with all component carriers active.

## 6.5Void

## 6.5AOutput RF spectrum emissions for CA

## 6.5A.1Occupied bandwidth for CA

For inter-band NR CA between FR1 and FR2, occupied bandwidth specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for each frequency range respectively.

## 6.5A.2Out-of-band emissions for CA

For inter-band NR CA between FR1 and FR2, out-of-band emissions specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for each frequency range respectively.

## 6.5A.3Spurious emissions for CA

## 6.5A.3.1Inter-band CA between FR1 and FR2

Unless otherwise stated, for inter-band CA between FR1 and FR2, spurious emission and UE co-existence requirements specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for each component carrier respectively.

Table 6.5A.3.1-1: Void

## 6.5A.4Transmit intermodulation for CA

For inter-band NR CA between FR1 and FR2, transmit intermodulation specified in TS 38.101-1 [2] apply for each component carrier for NR FR1.

## 6.5BOutput RF spectrum emissions for DC

## 6.5B.1Occupied bandwidth for EN-DC

## 6.5B.1.1Intra-band contiguous EN-DC

For intra-band contiguous EN-DC the occupied bandwidth is a measure of the bandwidth containing 99% of the total integrated power of the transmitted spectrum. The OBW shall be less than the aggregated channel bandwidth for EN-DC, denoted as ENBW in clause 5.3B.

## 6.5B.1.2Intra-band non-contiguous EN-DC

For intra-band non-contiguous EN-DC, occupied bandwidth requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.1 and 6.6.1A of TS 36.101 [4] and for NR single carrier specified in clause 6.5.1 of TS 38.101-1 [2] apply.

## 6.5B.1.3Inter-band EN-DC within FR1

Occupied bandwidth requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.1 and 6.6.1A of TS 36.101 [4] and for NR single carrier specified in clause 6.5.1 of TS 38.101-1 [2] apply.

## 6.5B.1.3a(Void)

## 6.5B.1.4Inter-band EN-DC including FR2

Occupied bandwidth requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.1 and 6.6.1A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.1, 6.5A.1 and 6.5D.1 of TS 38.101-2 [3] apply.

## 6.5B.1.4a(Void)

## 6.5B.1.5Inter-band EN-DC including both FR1 and FR2

Occupied bandwidth requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.1 and 6.6.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.5.1 and 6.5A.1 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.1, 6.5A.1 and 6.5D.1 of TS 38.101-2 [3] apply.

## 6.5B.2Out-of-band emissions for DC

## 6.5B.2.1Intra-band contiguous EN-DC

The out of band emissions are unwanted emissions immediately outside the EN-DC aggregated channel bandwidth resulting from the modulation process and non-linearity in the transmitter but excluding spurious emissions. This out of band emission limit is specified in terms of a spectrum emission mask and an adjacent channel leakage power ratio.

Unless otherwise stated, the OOBE limits specified for the DC combination in this clause supercede any OOBE requirements specified for each sub-block in the respective TS [4] and TS 38.101-1 [2].

The requirements apply to the sum of transmissions across all antenna connectors.

## 6.5B.2.1.1Spectrum emissions mask

The spectrum emission mask of the UE applies to frequencies (ΔfOOB) starting from the ± edge of the EN-DC aggregated channel bandwidth. For frequencies offset greater than ΔfOOB as specified in Table 6.5B.2.1.1-1 the spurious requirements in clause 6.5B.3 are applicable.

The general spectrum emission for intra-band contiguous EN-DC is specified in Table 6.5B.2.1.1-1.

The power of any UE emission shall not exceed the levels specified in Table 6.5B.2.1.1-1 for the specified EN-DC aggregated channel bandwidth.

Table 6.5B.2.1.1-1: General spectrum emission mask for intra-band contiguous EN-DC

## 6.5B.2.1.2Additional spectrum emissions mask

## 6.5B.2.1.2.1Requirements for network signalled value "NS_35"

When NS_35 is indicated in the MCG and NS_35 is indicated in the SCG, the requirements in Table 6.5B.2.1.2.1-1 apply in the frequency ranges immediately adjacent and outside the aggregated sub-blocks of the EN-DC configuration for DC_(n)71AA.

Table 6.5B.2.1.2.1-1: Additional requirements

## 6.5B.2.1.2.2Requirements for network signalled value "NS_04"

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

The Band 41/n41 SEM transition point from -13 dBm/MHz to -25 dBm/MHz is based on the emission bandwidth. The emission bandwidth is defined as the width of the signal between two points, one below the carrier center frequency and one above the carrier center frequency, outside of which all emissions are attenuated at least 26 dB below the transmitter power. Since the 26 dB emission bandwidth is implementation dependent, the transmission bandwidths occupied by RBs is used for the SEM. The emission bandwidth for E-UTRA carriers is document in TS 36.101 [4], and the emission bandwidth for NR carriers is documented in TS 38.101-1 [2]. The total emission bandwidth for contiguous intra-band EN-DC is the sum of the emission bandwidth for each CC plus the guard band between contiguous CCs.

When "NS_04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5B.2.1.2.2-1.

Table 6.5B.2.1.2.2-1: DC_(n)41 SEM with NS_04

## 6.5B.2.1.3Adjacent channel leakage ratio

For EN-DC operation with an E-UTRA sub-block immediately adjacent to an NR sub-block, the ACLR is defined as the ratio of the filtered mean power centred on the aggregated sub-block bandwidth ENBW to the filtered mean power centred on an adjacent bandwidth of the same size ENBW at nominal channel spacing. The UE shall meet the ACLR minimum requirement EN-DCACLR specified in Table 6.5B.2.1.3-1 with ENBW the sum of the sub-block bandwidths.

The assigned channel power and adjacent channel power are measured with rectangular filters with measurement bandwidths specified in 6.5B.2.1.3-1.

Table 6.5B.2.1.3-1: ACLR for intra-band EN-DC (contiguous sub-blocks)

## 6.5B.2.2Intra-band non-contiguous EN-DC

## 6.5B.2.2.1Spectrum emissions mask

The spectral emission mask for intra-band non-contiguous EN-DC is a composite of the emission mask for each CC with the level set to the maximum value from each mask for each frequency outside of the transmission bandwidth of either carrier. A composite spectrum emission mask is a combination of individual CC spectrum emissions masks. Where two masks overlap the most relaxed limit is used. Composite spectrum emission mask applies to frequencies up to  ΔfOOB starting from the edges of the sub-blocks. If for some frequency an individual CC spectrum emission mask overlaps with the bandwidth of another CC then the emission mask does not apply for that frequency.

## 6.5B.2.2.2Additional spectrum emissions mask

When additional spectrum emission mask or masks apply, the additional SEM(s) shall be used to calculate the composite SEM described in 6.5B.2.2.1.

## 6.5B.2.2.3Adjacent channel leakage ratio

For intra-band non-contiguous EN-DC, the EN-DC Adjacent Channel Leakage power Ratio (EN-DCACLR) is the ratio of the sum of the filtered mean powers centred on the assigned E-UTRA and NR sub-block frequencies to the filtered mean power centred on an adjacent channel frequency at nominal channel spacing. In case the sub-block gap bandwidth Wgap is smaller than a E-UTRA or NR sub-block bandwidth, no EN-DCACLR requirement is set for the corresponding sub-block for the gap. The assigned EN-DC sub-block power and adjacent channel power are measured with rectangular filters with measurement bandwidths specified in TS 36.101 [4] for the E-UTRA sub-block, and TS 38.101-1 [2] for the NR sub-block. If the measured adjacent channel power is greater than –50dBm then the EN-DCACLR shall be higher than the value specified in for E-UTRAACLR and NRACLR.

## 6.5B.2.3Inter-band EN-DC within FR1

Unless otherewise stated, the OOBE requirements specified in clause 6.6.2.1 of TS 36.101 [4], sub- clause 6.6.2 of TS 36.101 [4] and clause 6.5.2 of TS 38.101-1 [2] apply for each component carrier.

## 6.5B.2.3a(Void)

## 6.5B.2.4Inter-band EN-DC including FR2

Unless otherewise stated, out-of-band emissions requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.2 of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.2, 6.5A.2 and 6.5D.2 of TS 38.101-2 [3] apply.

## 6.5B.2.4aInter-band NE-DC including FR2

Unless otherewise stated, out-of-band emissions requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.2 of TS 36.101 [4] and for NR single carrier, CA operation, and UL-MIMO specified in clause 6.5.2, 6.5A.2 and 6.5D.2 of TS 38.101-2 [3] apply.

## 6.5B.2.5Inter-band EN-DC including both FR1 and FR2

Unless otherewise stated, out-of-band emissions requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.2 of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.5.2 and 6.5A.2 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.2, 6.5A.2 and 6.5D.2 of TS 38.101-2 [3] apply.

## 6.5B.3Spurious emissions for DC

## 6.5B.3.1Intra-band contiguous EN-DC

## 6.5B.3.1.1General spurious emissions

The general spurious emissions requirements specified in clause 6.6.3.1 of TS 36.101 [4] and clause 6.5.3.1 of TS 38.101-1 [2] apply beyond any frequencies for which the out-of-band emissions requirements in clause 6.5B.2.1apply.

## 6.5B.3.1.2Spurious emission band UE co-existence

The requirements in Table 6.5B.3.1.2-1 apply on each component carrier with all component carriers are active. Unless otherwise stated, the spurious emission for UE co-existence requirements are not applicabe to the frequency ranges where out-of-band emissions requirements in clause 6.5B.2 are defined.

Table 6.5B.3.1.2-1: Requirements for intra-band contiguous EN-DC

NOTE:To simplify the above Table, E-UTRA band numbers are listed for bands which are specified only for E-UTRA operation or both E-UTRA and NR operation. NR band numbers are listed for bands which are specified only for NR operation.

## 6.5B.3.2Intra-band non-contiguous EN-DC

## 6.5B.3.2.1General spurious emissions

The general spurious emissions requirements specified in clause 6.6.3.1 of TS 36.101 [4] and clause 6.5.3.1 of TS 38.101-1 [2] apply beyond any frequencies for which the out-of-band emissions requirements in clause 6.5B.2.2 apply. If for some frequency an individual CC spurious emission requirement overlaps with the general spectrum emission mask or the bandwidth of another CC then it does not apply.

## 6.5B.3.2.2Spurious emission band UE co-existence

The requirements in Table 6.5B.3.2.2-1 apply with all component carriers are active. Unless otherwise stated, the spurious emission for UE co-existence requirements are not applicabe to the frequency ranges where out-of-band emissions requirements in clause 6.5B.2 are defined.

Table 6.5B.3.2.2-1: Requirements for intra-band non-contiguous EN-DC

NOTE:To simplify the above Table, E-UTRA band numbers are listed for bands which are specified only for E-UTRA operation or both E-UTRA and NR operation. NR band numbers are listed for bands which are specified only for NR operation.

## 6.5B.3.3Inter-band EN-DC within FR1

6.5B.3.3.1General spurious emissions

The general spurious emissions requirements specified in clause 6.6.3.1 of TS 36.101 [4], clause 6.5.3.1 of TS 38.101-1 [2] and TS 38.101-2 [3] apply for each component carrier. For the case of inter-band EN-DC with a single carrier per cell group, the general spurious emissions requirements also apply with both downlink carrier and both uplink carriers active. Limits on configured maximum output power for the uplink according to clause 6.2B.4 apply. If for some frequency a spurious emission requirement of an individual component carrier overlaps with the spectrum emission mask or channel bandwidth of another component carrier then it does not apply.

NOTE:The general spurious emission requirements with both uplink carriers active are allowed to be verified for only a single inter-band EN-DC configuration per NR band. Furthermore, the requirements are allowed to be verified by measuring spurious emissions at the specific frequencies where second and third order intermodulation products generated by the two transmitted carriers can occur.

Table 6.5B.3.3.1-1: (Void)

## 6.5B.3.3.2Spurious emission band UE co-existence

This clause specifies additional the requirements for uplink EN-DC coexistence with protected bands with the single CC uplink assigned to E-UTRA and NR bands for the specified uplink carrier aggregation configurations in Table 6.5B.3.3.2-1. The intersection of the requirements for the individual bands specified in clause 6.5.3.2 of [2] and clause 6.6.3.2 of [4] shall also apply for the specified uplink EN-DC configurations. Intersection of a requirement means that both UL constituent bands have the same protected band requirement specified and if one or both protected bands have note(s) associated those note(s) also apply.

The requirements in Table 6.5B.3.3.2-1 and the intersection of the requirements for the individual bands specified in clause 6.5.3.2 of [2] and clause 6.6.3.2 of [4] apply on each component carrier with all component carriers are active. Unless otherwise stated, the spurious emission for UE co-existence requirements are not applicable to the frequency ranges where out-of-band emissions requirements in clause 6.5B.2 are defined.

NOTE:For inter-band EN-DC with uplink assigned to one LTE band and one NR band the requirements in Table 6.5B.3.3.2-1 could be verified by measuring spurious emissions at the specific frequencies where second and third order intermodulation products generated by the two transmitted carriers can occur; in that case, the requirements for remaining applicable frequencies in Table 6.5B.3.3.2-1 and in 6.5.3.2 of [2] and clause 6.6.3.2 of [4] would be considered to be verified by the measurements verifying the uplink single carrier UE to UE co-existence requirements.

Table 6.5B.3.3.2-1: Requirements

## 6.5B.3.3aInter-band NE-DC within FR1

## 6.5B.3.3a.1Void

## 6.5B.3.3a.2Spurious emission band UE co-existence

This clause specifies the requirements for the specified NE-DC configurations that do not have a corresponding defined EN-DC, for coexistence with protected bands. For the NE-DC configurations that have a corresponding specified EN-DC configuration, the requirements in Table 6.5B.3.3.2-1 apply on each component carrier with all component carriers are active. Unless otherwise stated, the spurious emission for UE co-existence requirements are not applicabe to the frequency ranges where out-of-band emissions requirements in clause 6.5B.2 are defined.

Table 6.5B.3.3a.2-1: Requirements

## 6.5B.3.4Inter-band EN-DC including FR2

## 6.5B.3.4.0General spurious emission

General spurious requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.3.1 and 6.6.3.1A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.3, 6.5A.3 and 6.5D.3 of TS 38.101-2 [3] apply.

## 6.5B.3.4.1Spurious emission band UE co-existence

This clause specifies the requirements for the specified EN-DC, for coexistence with protected bands. Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.5.1-1, no requirements for FR2 NR bands to protect E-UTRA and FR1 NR bands are applied to the constituent FR2 NR bands. Spurious emission band UE co-existence requirements specified in TS 36.101 [4] are applied to the constituent E-UTRA bands for the EN-DC configuration.

Spurious emission band UE co-existence requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.3.2 and 6.6.3.2A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.3.1, 6.5A.3.1 and 6.5D.3.1 of TS 38.101-2 [3] apply.

Table 6.5B.3.4.1-1: Void

## 6.5B.3.4a(Void)

## 6.5B.3.4a.1(Void)

## 6.5B.3.5Inter-band EN-DC including both FR1 and FR2

## 6.5B.3.5.0General spurious emission

General spurious requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.3.1 and 6.6.3.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.5.3.1 and 6.5A.3.1 of TS 38.101-1 [2] and clause 6.5.3, 6.5A.3 and 6.5D.3 of TS 3801-2 [3] apply.

## 6.5B.3.5.1Spurious emission band UE co-existence

This clause specifies the requirements for the specified EN-DC, for coexistence with protected bands. Unless otherwise stated, for inter-band EN-DC configurations defined in clause 5.5B.6, no requirements for FR2 NR bands to protect E-UTRA and FR1 NR bands are applied to the constituent FR2 NR bands. Spurious emission band UE co-existence requirements for constituent E-UTRA and FR1 NR bands for the inter-band EN-DC are the same as those for the corresponding EN-DC configuration without the FR2 bands specified in 6.5B.3.2.2.

Spurious emission band UE co-existence requirement for E-UTRA single carrier and CA operation specified in clauses 6.6.3.2 and 6.6.3.2A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 6.5.3.2 and 6.5A.3.2 of TS 38.101-1 [2] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.3.1, 6.5A.3.1 and 6.5D.3.1 of TS 38.101-2 [3] apply.

Table 6.5B.3.5.1-1: Void

## 6.5B.4Additional spurious emissions

## 6.5B.4.1General

These requirements are specified in terms of an additional spectrum emission requirement. Additional spurious emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

## 6.5B.4.1.1Void

## 6.5B.4.2Intra-band contiguous EN-DC

## 6.5B.4.2.1Minimum requirement (network signalled value "NS_04")

When "NS 04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5B.4.1.1-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.5B.4.1.1-1: Additional requirements

## 6.5B.4.3Intra-band non-contiguous EN-DC

## 6.5B.4.3.1Minimum requirement (network signalled value "NS_04")

When "NS 04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5B.4.1.1-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.6.3.1-1 from the edge of the channel bandwidth.

Table 6.5B.4.1.1-1: Additional requirements

## 6.5B.4.4Inter-band EN-DC within FR1

The additional spurious emissions requirements specified for E-UTRA in clause 6.6.3.3 and 6.6.3.3A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.3.3, 6.5A.3.3 and 6.5D.3 of TS 38.101-1 [2] apply for each component carrier.

## 6.5B.4.4a(Void)

## 6.5B.4.5Inter-band EN-DC including FR2

The additional spurious emissions requirements specified for E-UTRA in clause 6.6.3.3 and 6.6.3.3A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.3.3, 6.5A.3.3 and 6.5D.3 of TS 38.101-2 [3] apply for each component carrier.

## 6.5B.4.6Inter-band EN-DC including both FR1 and FR2

The additional spurious emissions requirements specified for E-UTRA in clause 6.6.3.3 and 6.6.3.3A of TS 36.101 [4] and for NR single carrier, CA operation and UL-MIMO specified in clause 6.5.3.3, 6.5A.3.3 and 6.5D.3 of TS 38.101-1 [2] and in clause 6.5.3.3, 6.5A.3.3 and 6.5D.3 of TS 38.101-2 [3] apply for each component carrier.

## 6.5B.5Transmit intermodulation for DC

## 6.5B.5.1Intra-band contiguous EN-DC

Unless otherwise stated, no transmit intermodulation requirements are applied for intra band contiguous EN DC.

## 6.5B.5.1a(Void)

## 6.5B.5.2Intra-band non-contiguous EN-DC

Unless otherwise stated, no transmit intermodulation requirements are applied for intra band non contiguous EN DC.

## 6.5B.5.3Inter-band EN-DC within FR1

The transmit intermodulation requirement specified in clauses 6.7.1 of TS 36.101 [4] and clauses 6.5.4 and 6.5A.4 of TS 38.101-1 [2] apply for each component carrier in E-UTRA bands and NR bands, respectively.

## 6.5B.5.3a(Void)

## 6.5B.5.4Inter-band EN-DC including FR2

Transmit intermodulation requirements specified in clause 6.7.1 and 6.7.1A of TS 36.101 [4] apply for each component carrier in E-UTRA bands.

## 6.5B.5.4a(Void)

## 6.5B.5.5Inter-band EN-DC including both FR1 and FR2

Transmit intermodulation requirement specified in clauses 6.7.1 and 6.7.1A of TS 36.101 [4] and clauses 6.5.4 and 6.5A.4 of TS 38.101-1 [2] apply for each component carrier in E-UTRA bands and NR bands, respectively.

## 6.5EOutput RF spectrum emissions for V2X operation in FR1

## 6.5E.1Occupied bandwidth

## 6.5E.1.1Intra-band V2X

For intra-band V2X, the occupied bandwidth specified in clause 6.6.1G in TS 36.101 [4] and specified in clause 6.5E.1 in TS 38.101-1 [2] apply for each frequency range respectively.

## 6.5E.1.2inter-band V2X con-current operation

For the inter-band con-current NR V2X operation, the requirements specified in subclause 6.6.1 of TS 36.101 [4] shall apply for the E-UTRA uplink in licensed band and the requirements specified in subclause 6.5E.1 of TS 38.101-1 [2] shall apply for the sidelink in NR Band n47.

## 6.5E.2Out-of-band emissions

## 6.5E.2.1Intra-band V2X

For intra-band V2X, out-of-band emissions specified in clause 6.6.2G in TS 36.101 [4] and specified in clause 6.5E.2 in TS 38.101-1 [2] apply for each frequency range respectively.

## 6.5E.2.2Inter-band V2X con-current operation

For the inter-band con-current NR V2X operation, the general SEM/additional SEM requirements and ACLR specified in subclause 6.6.2 of TS 36.101 [4] shall apply for the E-UTRA uplink in licensed band and the general SEM/additional SEM and ACLR requirements specified in subclause 6.5E.2 of TS 38.101-1 [2] shall apply for the sidelink in NR Band n47.

## 6.5E.3Spurious emissions

## 6.5E.3.1Intra-band V2X

## 6.5E.3.1.1General spurious emissions

For intra-band V2X, the general spurious emissions requirements specified in clause 6.6.3.1 of TS 36.101 [4] and clause 6.5E.3.1 of TS 38.101-1 [2] apply for each frequency range respectively.

## 6.5E.3.1.2Spurious emission band UE co-existence

For intra-band V2X, the spurious emissions band UE co-existence requirements specified in clause 6.6.3.2 of TS 36.101 [4] and clause 6.5E.3.2 of TS 38.101-1 [2] apply for each frequency range respectively.

## 6.5E.3.2 Inter-band V2X con-current operation

## 6.5E.3.2.1General spurious emissions

For inter-band V2X, the general spurious emissions requirements specified in clause 6.6.3.1 of TS 36.101 [4] and clause 6.5E.3.1 of TS 38.101-1 [2] apply for each frequency range respectively.

## 6.5E.3.2.2Spurious emission band UE co-existence

This clause specifies the additional requirements for inter-band con-current V2X operation with the single CC uplink assigned to E-UTRA or NR bands for coexistence with protected bands for the specified simultaneous transmission of the inter-band con-current V2X configurations in Table 6.5E.3.2.2-1. The intersection of the requirements for the individual bands specified in clause 6.5.3.2 shall also apply for the specified simultaneous transmission of the inter-band con-current V2X. Intersection of a requirement means that both UL or sidelink transmission constituent bands have the same protected band requirement specified and if one or both protected bands have note(s) associated those note(s) also apply.

For the inter-band con-current NR V2X operation, the UE-coexistence requirements in Table 6.5E.3.2.2-1 apply for the corresponding inter-band con-current operation with transmission assigned to both E-UTRA/NR uplink in licensed band and sidelink in E-UTRA/NR Bands. Unless otherwise stated, the spurious emission for UE co-existence requirements are not applicabe to the frequency ranges where out-of-band emissions requirements in clause 6.5E.2 are defined.

NOTE:For inter-band con-current V2X operation with uplink assigned to E-UTRA/NR band and slidelink transmission assigned to E-UTRA/NR V2X operating bands, the requirements in Table 6.5E.3.2.2-1 could be verified by measuring spurious emissions at the specific frequencies where second and third order intermodulation products generated by the two transmitted carriers can occur; in that case, the requirements for remaining applicable frequencies in Table 6.5E.3.2.2-1 and in clause 6.5.3.2 would be considered to be verified by the measurements verifying the one uplink inter-band con-current UE to UE co-existence requirements.

Table 6.5E.3.2.2-1: Requirements for inter-band con-current V2X operation

## 6.5E.4Transmit intermodulation

## 6.5E.4.1Intra-band V2X

For intra-band V2X, transmit intermodulation requirements specified in clause 6.7.1G of TS 36.101 [4] and clause 6.5E.4 of TS 38.101-1 [2] apply for each frequency range respectively.

## 6.5E.4.2Inter-band V2X con-current operation

For the inter-band con-current NR V2X operation, the requirements specified in subclause 6.7.1 of TS 36.101 [4] shall apply for the E-UTRA uplink in licensed band and the requirements specified in subclause 6.5E.4 of TS 38.101-1 [2] shall apply for the sidelink in NR Band n47.

## 6.5HOutput RF spectrum emissions for DC with UL MIMO

## 6.5H.1Occupied bandwidth for EN-DC with UL MIMO

## 6.5H.1.1void

## 6.5H.1.2void

## 6.5H.1.3Inter-band EN-DC with UL MIMO within FR1

Occupied bandwidth requirement for E-UTRA single carrier specified in clauses 6.6.1 of TS 36.101 [4] and for NR single carrier specified in clause 6.5D.1 of TS 38.101-1 [2] apply.

## 6.5H.2Out-of-band emissions for DC with UL MIMO

## 6.5H.2.1void

## 6.5H.2.2void

## 6.5H.2.3Inter-band EN-DC with UL MIMO within FR1

Unless otherewise stated, the OOBE requirements specified in clause 6.6.2.1 of TS 36.101 [4], sub- clause 6.6.2 of TS 36.101 [4] and clause 6.5D.2 of TS 38.101-1 [2] apply for each component carrier.

## 6.5H.3Spurious emissions for DC with UL MIMO

## 6.5H.3.1void

## 6.5H.3.2void

6.5H.3.3Inter-band EN-DC with UL MIMO within FR1

The requirements in 6.5B.3.3 apply and for the NR component carrier configured with UL MIMO, the configurations of UL MIMO are according to clause 6.5D.3 of TS 38.101-1 [2].

## 6.5H.4Additional spurious emissions for DC with UL MIMO

## 6.5H.4.1void

## 6.5H.4.2void

## 6.5H.4.3Inter-band EN-DC with UL MIMO within FR1

The additional spurious emissions requirements specified for E-UTRA in clause 6.6.3.3 of TS 36.101 [4] and for NR UL MIMO specified in clause 6.5D.3 of TS 38.101-1 [2] apply for each component carrier.

## 6.5H.5Transmit intermodulation for DC with UL MIMO

## 6.5H.5.1void

## 6.5H.5.2void

## 6.5H.5.3Inter-band EN-DC with UL MIMO within FR1

The transmit intermodulation requirement specified in clauses 6.7.1 of TS 36.101 [4] and clauses 6.5D.4 of TS 38.101-1 [2] apply for each component carrier in E-UTRA bands and NR bands, respectively.

## 6.5LOutput RF spectrum emissions for DC with Tx Diversity

## 6.5L.1Occupied bandwidth for EN-DC with Tx Diversity

## 6.5L.1.1void

## 6.5L.1.2void

## 6.5L.1.3Inter-band EN-DC with Tx Diversity within FR1

Occupied bandwidth requirement for E-UTRA single carrier specified in clauses 6.6.1 of TS 36.101 [4] and for NR single carrier specified in clause 6.5G.1 of TS 38.101-1 [2] apply.

## 6.5L.2Out-of-band emissions for DC with Tx Diversity

## 6.5L.2.1void

## 6.5L.2.2void

## 6.5L.2.3Inter-band EN-DC with Tx Diversity within FR1

Unless otherewise stated, the OOBE requirements specified in clause 6.6.2.1 of TS 36.101 [4], sub- clause 6.6.2 of TS 36.101 [4] and clause 6.5D.2 of TS 38.101-1 [2] apply for each component carrier.

## 6.5L.3Spurious emissions for DC with Tx Diversity

## 6.5L.3.1void

## 6.5L.3.2void

## 6.5L.3.3Inter-band EN-DC with Tx Diversity within FR1

The requirements in 6.5B.3.3 apply except that:

-For the NR component carrier configured with Tx Diversity, the general spurious emissions specified in clause 6.5G.3.1 of TS 38.101-1 [2] are applied, and the coexistence band protection requirements specified in clause 6.5G.3.2 of [2] are applied.

## 6.5L.4Additional spurious emissions for DC with Tx Diversity

## 6.5L.4.1void

## 6.5L.4.2void

## 6.5L.4.3Inter-band EN-DC with Tx Diversity within FR1

The additional spurious emissions requirements specified for E-UTRA in clause 6.6.3.3 of TS 36.101 [4] and for NR Tx Diversity specified in clause 6.5G.3 of TS 38.101-1 [2] apply for each component carrier.

## 6.5L.5Transmit intermodulation for DC with Tx Diversity

## 6.5L.5.1void

## 6.5L.5.2void

## 6.5L.5.3Inter-band EN-DC with Tx Diversity within FR1

The transmit intermodulation requirement specified in clauses 6.7.1 of TS 36.101 [4] and clauses 6.5G.4 of TS 38.101-1 [2] apply for each component carrier in E-UTRA bands and NR bands, respectively.

## 6.6BBeam correspondence for DC

## 6.6B.1Void

## 6.6B.2Void

## 6.6B.3Void

## 6.6B.4Inter-band EN-DC including FR2

Beam correspondence requirement for RRC_CONNECTED state as specified in clause 6.6 and 6.6A of TS 38.101-2 [3] apply for NR FR2 bands.

## 6.6B.4a(Void)

## 6.6B.5Inter-band EN-DC including both FR1 and FR2

Beam correspondence requirement for RRC CONNECTED state as specified in clause 6.6 and 6.6A of TS 38.101-2 [3] apply for NR FR2 bands.

## 7Receiver characteristics

## 7.1General

Unless otherwise stated the receiver characteristics are specified at the antenna connector(s) of the UE for the bands operating on frequency range 1 and over the air of the UE for the bands operating on frequency range 2. The requirements for frequency range 1 and frequency range 2 can be verified separately. For the carrier in frequency range 1, requirements can be verified with NR FR2 link disabled. For the carrier in frequency range 2, requirements can be verified in OTA mode with E-UTRA or NR FR1 connecting to the network by OTA without calibration.

The requirements defined in this clause are the extra requirements compared with the single carrier requirements defined in TS 38.101-1 [2] and TS 38.101-2 [3].

Unless otherwise stated, the UL and DL reference measurement channels are the same with the configurations specified in TS 38.101-1 [2] and TS 38.101-2 [3].

Unless otherwise stated, requirements for NR receiver written in TS 38.101-1 [2] and TS 38.101-2 [3] apply and are assumed anchor agnostic. Requirements are verified under conditions where anchor resources do not interfere NR operation.

For intra-band EN-DC, the output power is configured as follows:

-One E-UTRA uplink carrier with the output power set to 29 dB below PCMAX_L and the NR band whose downlink is being tested has its uplink carrier output power set to 4 dB below PCMAX_L,f,c.

-One NR uplink carrier with the output power set to 29 dB below PCMAX_L,f,c and the E-UTRA band whose downlink is being tested has its uplink carrier output power set to 4 dB below PCMAX_L,c.

For the additional requirements for intra-band non-contiguous EN-DC of two sub-blocks, an in-gap test refers to the case when the interfering signal is located at a negative offset with respect to the assigned lowest channel frequency of the highest sub-block and located at a positive offset with respect to the assigned highest channel frequency of the lowest sub-block.

For the additional requirements for intra-band non-contiguous EN-DC of two sub-blocks, an out-of-gap test refers to the case when the interfering signal(s) is (are) located at a positive offset with respect to the assigned channel frequency of the highest carrier frequency or located at a negative offset with respect to the assigned channel frequency of the lowest carrier frequency.

For the additional requirements for intra-band non-contiguous EN-DC of two sub-blocks with channel bandwidth larger than or equal to 5 MHz, the existing adjacent channel selectivity requirements, in-band blocking requirements (for each case), and narrow band blocking requirements apply for in-gap tests only if the corresponding interferer frequency offsets with respect to the two measured carriers satisfy the following condition in relation to the sub-block gap size Wgap for at least one of the E-UTRA or NR sub-blocks, so that the interferer frequency position does not change the nature of the core requirement tested:

Wgap ≥ 2∙|FInterferer (offset)| – BWChannel

For the E-UTRA sub-block, the FInterferer (offset), for a sub-block with a single component carrier is the interferer frequency offset with respect to carrier as specified in clause 7.5.1, clause 7.6.1 and clause 7.6.3 for the respective requirement in TS 36.101 [4] and BWChannel. FInterferer (offset) for the E-UTRA sub-block with two or more contiguous component carriers is the interference frequency offset with respect to the carrier adjacent to the gap is specified in clause 7.5.1A, 7.6.1A and 7.6.3A in TS 36.101 [4].

For the NR sub-block, the FInterferer (offset), for a sub-block with a single component carrier is the interferer frequency offset with respect to carrier as specified in clause 7.5.1, clause 7.6.1 and clause 7.6.3 for the respective requirement in TS 38.101-1 [2] and BWChannel.

The interferer frequency offsets for adjacent channel selectivity, each in-band blocking case and narrow-band blocking shall be tested separately with a single in-gap interferer at a time.

For sub-clauses with suffix A or B: the minimum requirements for band combinations including Band n41 also apply for the corresponding band combinations with Band n90 replacing Band n41 but with otherwise identical parameters. For brevity the said band combinations with Band n90 are not listed in the tables below but are covered by this specification.

Unless otherwise stated, for the FR1 requirements in this clause,

-The UE shall be verified with four Rx antenna ports and skip two Rx antenna ports requirements in operating bands where the UE is equipped with four Rx antenna ports,

-the UE shall be verified with eight antenna ports and skip both two and four Rx antenna ports requirements in operating bands where the UE is equipped with eight Rx antenna ports unless UE is not supporting 8Rx ports for band(s) in band combination in which case those band(s) shall be verified with four Rx antenna ports in that band combination, otherwise, the UE shall be verified with two Rx antenna ports.

If a UE indicates both interBandMRDC-WithOverlapDL-Bands-r16 and requirementTypeIndication-r18 , it shall be verified with bothfour Rx antenna ports and two Rx antenna ports requirements.

If a UE indicates interBandMRDC-WithOverlapDL-Bands-r16 but does not indicate requirementTypeIndication-r18, it shall be verified with two Rx antenna ports requirements.Unless otherwise stated, the receiver requirements of inter-band EN-DC are applicable to UE with one or two Tx antenna connectors in NR band.

If a UE indicates interBandMRDC-WithOverlapDL-Bands-r19, it shall be verified with four Rx antenna ports requirements.  Moreover, it shall be verified with six or eight Rx antenna ports requirements when the maxMIMO-Layers is equal to six or eight, respectively.

## 7.2Void

## 7.3Void

## 7.3AReference sensitivity for CA

## 7.3A.1General

For NR CA operation, NR single carrier and CA operation of  REFSENS requirements defined in TS 38.101-1 [2] and TS 38.101-2 [3] apply to all downlink bands part of NR CA configurations listed in Table 5.2A.1-1unless sensitivity degradation is allowed as defined in clause 7.3A.

A UE which supports inter-band NR CA configuration is allowed to apply each sensitivity degradation for FR1 specified in clause 7.3A.2 TS 38.101-1 [2] and for FR2 specified in clause 7.3A.2 of TS 38.101-2 [3] independently.

## 7.3A.2Reference sensitivity power level for CA

## 7.3A.3ΔRIB,c for CA

For the UE which supports inter-band NR CA configuration, the minimum requirement for reference sensitivity in clause 7.3.2, 7.3A2  in TS 38.101-1 [2] and clause 7.3.2, 7.3A.2in TS 38.101-2 [3] shall be increased by the amount given in ΔRIB,c in Tables below. Unless otherwise stated, ΔRIB,c is set to zero.

In case the UE supports more than one of band combinations for CA, SUL or DC, and an operating band belongs to more than one band combinations then

-When the operating band frequency range is ≤ 1GHz, the applicable additional ∆RIB,c shall be the average value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in TS 38.101-1 [2] and 7.3A, 7.3B in this specification, truncated to one decimal place that apply for that operating band among the supported band combinations. In case there is a harmonic relation between low band UL and high band DL, then the maximum ΔRIB,c among the different supported band combinations involving such band shall be applied

-When the operating band frequency range is > 1 GHz, the applicable additional ΔRIB,c shall be the maximum value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in TS 38.101-1 [2] and 7.3A, 7.3B in this specification for the applicable operating bands.

## 7.3A.3.1ΔRIB,c for Inter-band CA between FR1 and FR2

ΔRIB,c is independent between FR1 and FR2. For inter-band CA between FR1 and FR2, ΔRIB,c for the FR1 band(s) from TS 38.101-1 [2] applies and ΔRIB,c for the FR2 NR band(s) is set to zero. Otherwise ΔRIB,c is set to zero.

Table 7.3A.3.1-1: Void

Table 7.3A.3.1-2: Void

Table 7.3A.3.1-3: Void

## 7.3A.4Void

## 7.3BReference sensitivity level for DC

## 7.3B.1General

For EN-DC, E-UTRA and NR single carrier, CA, and MIMO operation of REFSENS requirements defined in TS 38.101-1 [2], TS 38.101-2 [3] and TS 36.101 [4] apply to all downlink bands of EN-DC configurations listed in clause 5.5B, unless sensitivity degradation exception is allowed in this clause of this specification, clause 7.3 in TS 38.101-1 [2], clause 7.3 in TS 38.101-2 [3] or clause 7.3 in TS 36.101 [4]. Allowed exceptions specified in this clause of the specification, clause 7.3 in TS 38.101-1 [2], clause 7.3 in TS 38.101-2 [3] or clause 7.3 in TS 36.101 [4] also apply to any higher order EN-DC configuration combination containing one of the band combinations that exception is allowed for. Reference sensitivity exceptions are specified by applying maximum sensitivity degradation (MSD) into applicable REFSENS requirement. EN-DC REFSENS requirements shall be met for NR uplink transmissions using QPSK DFT-s-OFDM waveforms as defined in clause 7.3.2 [2]. Unless otherwise specified UL allocation uses the lowest SCS allowable for a given channel BW. Limits on configured maximum output power for the uplink according to clause 6.2B.4 shall apply.

In case of interband EN-DC the receiver REFSENS requirements in this clause do not apply for 1.4 and 3 MHz E-UTRA carriers. For the case of inter-band EN-DC with a single carrier per cell group and multi carrier per cell group, in addition to the E-UTRA and NR single carrier, CA, and MIMO operation of REFSENS requirements defined in TS 38.101-1 [2], TS 38.101-2 [3], and TS 36.101 [4], the REFSENS requirements specified therein also apply with both downlink carriers and both uplink carriers active unless sensitivity exceptions are allowed in this clause of this specification, clause 7.3 in TS 38.101-1 [2] or clause 7.3 in TS 36.101 [4].

For reference sensitivity exception test points where the specified carrier frequency does not correspond to a valid NR-ARFCN, the closest NR-ARFCN as specified in clause 5.4.2 applies.

For operations with 4 or 8 Rx antenna ports in an E-UTRA band or an NR band, the MSD in the applicable bands shall be increased by the absolute value of ΔRIB,4R in Table 7.3.1-1a or ΔRIB,8R in Table 7.3.1-1aa of TS 36.101[4] for the E-UTRA band or ΔRIB,4R in Table 7.3.2-2 or ΔRIB,8R in Table 7.3.2-2a of TS 38.101-1 for the NR band when MSD > 0.

NOTE:For inter-band EN-DC, the reference sensitivity requirement with both uplink carriers active is allowed to be verified for only a single inter-band EN-DC configuration per NR band.

For reference sensitivity level tests or reference sensitivity exception tests specified in clause 7.3B, SCS=15kHz based UL test configuration for NR bands can be replaced by SCS=30kHz based UL test configuration. The equivalent substitution relationship for NR bands between different SCS UL test configuration is shown in table 7.3B.1-1 for the NR operating bands above 2.2GHz.

Table 7.3B.1-1: Equivalent substitution relationship between different SCS UL test configurations for NR bands

## 7.3B.2Reference sensitivity for DC

## 7.3B.2.1Intra-band contiguous EN-DC

For intra-band contiguous EN-DC configurations, the reference sensitivity power level REFSENS is the minimum mean power applied to each one of the UE antenna ports at which the throughput for the carrier(s) of the E-UTRA and NR CGs shall meet or exceed the requirements for the specified E-UTRA and NR reference measurement channels. The reference sensitivity requirements apply with all uplink carriers and all downlink carriers active for EN-DC configuration and Uplink EN-DC configuration listed in Table 5.5B.2-1 and Table 5.5B.3-1, as supported by the UE. For EN-DC configurations where uplink is not available in either the MCG or the SCG or for EN-DC configurations where the UE only supports single uplink operation, reference sensitivity requirements are verified with the downlink carrier(s) from the cell group without uplink shall be configured closer to the uplink operating band than any of the downlink carriers from the cell group with uplink.

Sensitivity degradation is allowed for Intra-band contiguous EN-DC configurations listed in Table 7.3B.2.1-1 the reference sensitivity is defined only for the specific uplink and downlink test points which are specified in Table 7.3B.2.1-1 and E-UTRA and NR single carrier requriements do not apply.

Table 7.3B.2.1-1: Reference sensitivity (MSD) for intra-band contiguous EN-DC

## 7.3B.2.1a(Void)

## 7.3B.2.2Intra-band non-contiguous EN-DC

For intra-band non-contiguous EN-DC configurations, the reference sensitivity power level REFSENS is the minimum mean power applied to each one of the UE antenna ports at which the throughput for the carrier(s) of the E-UTRA and NR CGs shall meet or exceed the requirements for the specified E-UTRA and NR reference measurement channels.

Sensitivity degradation is allowed for Intra-band non-contiguous EN-DC configurations listed in Table 7.3B.2.2-1, the reference sensitivity is defined only for the specific uplink and downlink test points which are specified in Table 7.3B.2.2-1 and E-UTRA and NR single carrier requriements do not apply.

For UE supporting Intra-band non-contiguous EN-DC configurations with single switched UL, no MSD is specified and E-UTRA and NR single carrier requriements apply.

Table 7.3B.2.2-1: Reference sensitivity (MSD) for intra-band non-contiguous EN-DC

## 7.3B.2.3Inter-band EN-DC within FR1

## 7.3B.2.3.0General

7.3B.2.3.0.0MSD requirements with Look-Up tables

Reference sensitivity exceptions are specified for the condition when there is uplink transmission only in the aggressor band.

The PC2 and PC1.5 MSD requirements with look-up tables for two or three DL band EN-DC with 1UL or 2UL DC band do not apply when the UL band is either band 46/n46, band n96 or band n102.

7.3B.2.3.0.1PC2 and PC1.5 MSD requirements with look-up tables for two-band DL EN-DC with 1UL band single CC

The PC2 and the PC1.5 MSD requirements with look-up tables for two-band EN-DC reference sensitivity exceptions (MSD) due to 1UL band 1UL CC harmonic, harmonic mixing, and cross band isolation interference shall apply when the following criterias are met:

-A PC3 reference sensitivity exception requirement is specified either in Table 7.3B.2.3.1-1, or in Table 7.3B.2.3.2-1 or in Table 7.3B.2.3.4-1, and

-A PC2 reference sensitivity exception requirement is not specified respectively in Table 7.3B.2.3.2-1a, or in Table 7.3B.2.3.4-1a, and PC1.5 reference sensitivity exception requirement is not specified, and

-PC2 is specified in Table 6.2B.1.3-1 and PC2 output power is specified as a valid per band power class in Table 6.2B.1.3-1a, denoted here “PC21Tx”, or PC2 is specified in Table 6.2H.1.3-1 and PC2 is specified as a valid per band power class in Table 6.2H.1.3-1a, denoted here “PC22Tx”, or PC1.5 is specified in Table 6.2H.1.3-1 and PC1.5 output power is specified as a valid per band power class in Table 6.2H.1.3-1a, denoted here “PC1.52Tx”, and,

-The PCx aggressor UL band is the same aggressor UL band as in case of PC3 MSD.

For these cases, and where in the following PCx denotes either PC21Tx, PC22Tx or PC1.52Tx, the PCx MSD due to harmonic, harmonic mixing, and cross band isolation is specified as:

PCx MSD = PC3 MSD + MSD

where,

-PCx MSD is the reference sensitivity exception specified for PC21Tx, PC22Tx, or PC1.52Tx,

-PC3 MSD is the reference sensitivity exception specified for PC3 in Table 7.3B.2.3.1-1, or in Table 7.3B.2.3.2-1 or in Table 7.3B.2.3.4-1

-MSD values are specified in Table 7.3B.2.3.0.1-1 output columns denoted “MSDmax 3, 6, 9”. These apply to the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in Table 7.3B.2.3.1-1, or in Table 7.3B.2.3.2-1 or in Table 7.3B.2.3.4-1,

-The correspondence between the MSDmax specified in Table 7.3B.2.3.0.1-1, the source of interference and PCx MSD is specified in Table 7.3B.2.3.0.1-2,

Table 7.3B.2.3.0.1-1: MSD per MSDmax look-up table for MSD due to harmonic, harmonic mixing, cross band isolation

Table 7.3B.2.3.0.1-2: MSDmax correspondence look-up table for source of interference and PCx MSD

As an exception, for cases where:

-The PC21Tx MSD is specified in Table 7.3B.2.3.2-1a or in Table 7.3B.2.3.4-1a, and

-The PC3 MSD is not specified in Table 7.3B.2.3.2-1, or in Table 7.3B.2.3.4-1, and

-The PC1.5 MSD is not specified, and

-PC1.5 is specified in Table 6.2H.1.3-1 and PC1.5 output power is specified as a valid per band power class in Table 6.2H.1.3-1a, denoted here as “PC1.52Tx”, and,

then the PC1.52Tx MSD is specified as:

PC1.52Tx MSD = PC21Tx MSD + MSD,

where in the Table 7.3B.2.3.0.1-1,

-MSD is specified output column denoted “MSDmax 6”,

-The input column uses the specified “PC21Tx MSD” instead of “PC3 MSD”. These apply to the same uplink/downlink configurations as those specified for the minimum PC2 MSD requirements in Table 7.3B.2.3.2-1a or in Table 7.3B.2.3.4-1a.

7.3B.2.3.0.2PC2 and PC1.5 MSD requirements with look-up tables for two-band or three-band DL EN-DC with two-band UL EN-DC and a single CC per UL band.

The PC2 and the PC1.5 MSD requirements with look-up tables for two-band and three-band DL EN-DC reference sensitivity exceptions (MSD) due to 2UL EN-DC intermodulation interference shall apply when the following criterias are met:

-A PC3 reference sensitivity exception requirement is specified either in Table 7.3B.2.3.5.1-1, or in Table 7.3B.2.3.5.2-1, and,

-A PC2 reference sensitivity exception requirement is not specified respectively in Table 7.3B.2.3.5.1-1a or in Table 7.3B.2.3.5.2-1a and PC1.5 reference sensitivity exception requirement is not specified, and,

-PC2 or PC1.5 two-band UL EN-DC for a total of 2Tx or 3Tx and 1CC in each UL band is specified as a valid two-band UL EN-DC configuration in Table 6.2B.1.3-1, or in Table 6.2H.1.3-1, and,

-The PC2 or PC1.5 MSD is caused by the same uplink/downlink configurations as in case of PC3 MSD.

For these cases, and where in the following PCx denotes either PC2 or PC1.5, the PCx MSD due to 2UL EN-DC intermodulation interference is specified as:

PCx MSD = PC3 MSD + MSD

where,

-PCx MSD is the reference sensitivity exception specified for PC2 or PC1.5 with 2UL band EN-DC for a total of 2Tx or 3Tx and with 1UL CC in each UL band,

-PC3 MSD is the reference sensitivity exception specified for PC3 in Table 7.3B.2.3.5.1-1, or in Table 7.3B.2.3.5.2-1,

-MSD values are specified in Table 7.3B.2.3.0.2-1 output columns denoted “MSDmax 6, 9, 12, 15, 18, 24, 30”. These apply for the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in Table 7.3B.2.3.5.1-1, or in Table 7.3B.2.3.5.2-1, and,

-The correspondence between the MSDmax specified in Table 7.3B.2.3.0.2-1, the IMD order and PCx MSD is specified in Table 7.3B.2.3.0.2-2,

Table 7.3B.2.3.0.2-1: MSD per MSDmax look-up table for MSD due to 2UL EN-DC intermodulation interference

Table 7.3B.2.3.0.2-2: MSDmax correspondence look-up table for IMD order and PCx MSD

As an exception, for cases where:

-The PC2 MSD is specified in Table 7.3B.2.3.5.1-1a or in Table 7.3B.2.3.5.2-1a, and,

-The PC3 MSD is not specified in Table 7.3B.2.3.5.1-1or in Table 7.3B.2.3.5.2-1, and,

-The PC1.5 MSD is not specified, and,

-PC1.5 two-band UL EN-DC for a total of 2Tx or 3Tx and 1CC in each UL band is specified as a valid two-band UL EN-DC configuration in Table 6.2B.1.3-1, or in Table 6.2H.1.3-1.

then the PC1.5 MSD is specified as:

PC1.5 MSD = PC2 MSD + MSD,

where,

-In the Table 7.3B.2.3.0.2-1, MSD is specified with output columns denoted “MSDmax 6, 9, 12, 15” and where the input column uses the specified PC2 MSD specified in Table 7.3B.2.3.5.1-1a or in Table 7.3B.2.3.5.2-1a instead of the PC3 MSD, and

-In the Table 7.3B.2.3.0.2-2, the correspondence between the MSDmax and the IMD order is specified using the column specified for “PC2 MSD”, and

-These PC1.5 MSD requirements apply for the same uplink/downlink configurations as those specified in the PC2 MSD requirements of Table 7.3B.2.3.5.1-1a or in Table 7.3B.2.3.5.2-1a.

In all cases, the MSD requirements specified in Table 7.3B.2.3.0.2-1 and in Table 7.3B.2.3.0.2-2 do not apply to 2UL band EN-DC configurations with 3UL CCs, e.g. a combination of intra-band and inter-band dual connectivity.

7.3B.2.3.0.3PC2 and PC1.5 MSD requirements with look-up tables for two-band DL EN-DC with 2UL CC in NR TDD band.

The PC2 and the PC1.5 MSD requirements with look-up tables for two-band DL EN-DC reference sensitivity exceptions (MSD) due to 1UL NR TDD band with 2UL CC intermodulation interference shall apply when the following criteria are met:

-The UL band is a NR TDD band configured with intra-band contiguous UL CA, and,

-A PC3 reference sensitivity exception requirement is specified in Table 7.3B.2.3.5.1-1, and the corresponding PC2 reference sensitivity exception requirement is not specified in Table 7.3B.2.3.5.1-1a,

-PC2 or PC1.5 power class is specified in Table 6.2B.1.3-1 or Table 6.2H.1.3-1

-The PCx aggressor NR UL band is the same aggressor UL band as in case of PC3 MSD.

For these cases, and where in the following PCx denotes either PC2 or PC1.5, the PCx MSD due to 1UL NR TDD band with two contiguous UL CC intermodulation interference is specified as:

PCx MSD = PC3 MSD + MSD

where,

-PC3 MSD is the reference sensitivity exception specified in Table 7.3B.2.3.5.1-1,

-For IMD3 and IMD5 MSD values are specified in Table 7.3B.2.3.0.1-1 output column denoted “MSDmax 3” for PC2 and “MSDmax 6” for PC1.5,

-For IMD4 and ≥ IMD6 MSD values are specified in Table 7.3B.2.3.0.2-1 output columns denoted “MSDmax  9” for PC2 and “MSDmax 15” for PC1.5,

-These apply for the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in Table 7.3B.2.3.5.1-1,

-The correspondence between the MSDmax specified in Table 7.3A.2.3.2.1-1, the IMD order and PCx MSD is specified in Table 7.3B.2.3.0.3-1,

Table 7.3B.2.3.0.3-1: MSDmax correspondence look-up table for 1UL band 2UL CC IMD order and PCx MSD

In all cases, the MSD requirements specified in Table 7.3B.2.3.0.3-1 do not apply to 1UL FDD band CA configurations with two UL CCs, and in this case, MSD shall be specified in Table 7.3B.2.3.5.1-1a for PC2, or in a new table for PC1.5.

7.3B.2.3.0.4PC2 and PC1.5 MSD requirements with look-up tables for two-band or three-band DL EN-DC with two-band UL EN-DC with 2UL CC in NR TDD band.

The PC2 and the PC1.5 MSD requirements with look-up tables for two-band and three-band DL EN-DC reference sensitivity exceptions (MSD) due to 2UL band EN-DC IMD3 interference from 2UL CC in the NR TDD band and 1UL CC in the LTE FDD band, (also known as 1st order triple-beat MSD) shall apply when the following criteria are met:

-The NR UL band is configured with intra-band contiguous UL CA is a TDD band, and,

-The LTE UL band is configured with 1UL CC is a FDD band, and

-A PC3 reference sensitivity exception requirement is specified in Table 7.3B.2.3.5.1-1 or in Table 7.3B.2.3.5.2-1, and the corresponding PC2 reference sensitivity exception requirement is not specified in Table Table 7.3B.2.3.5.1-1a or Table 7.3B.2.3.5.2-1a,

-PC2 or PC1.5 power class is specified in Table 6.2B.1.2-1 or Table 6.2H.1.3-1,

-The PCx aggressor NR UL band is the same aggressor UL band as in case of PC3 MSD.

For these cases, and where in the following PCx denotes either PC2 or PC1.5, the PCx MSD due to 2UL band EN-DC IMD3 interference with two contiguous UL CC in the NR band and 1UL CC in the LTE band is specified as:

PCx MSD = PC3 MSD + MSD

where,

-PC3 MSD is the reference sensitivity exception specified for PC3 in 7.3B.2.3.5.1-1, or in 7.3B.2.3.5.2-1,

-MSD values are specified in Table 7.3B.2.3.0.2-1 column denoted “MSDmax 6” for PC2 and “MSDmax 12” for PC1.5. These apply for the same uplink/downlink configurations as those specified for the minimum PC3 MSD requirements in 7.3B.2.3.5.1-1, or in Table 7.3B.2.3.5.2-1,

## 7.3B.2.3.1Reference sensitivity exceptions due to UL harmonic interference for EN-DC in NR FR1

Sensitivity degradation is allowed for different combinations of UL configurations and DL channel bandwidths if a band if it is impacted by UL harmonic interference from another band part of the same EN-DC configuration. Reference sensitivity exceptions for the victim band (high) and uplink/downlink configurations due to UL harmonic from a PC3 aggressor UL band (low) for either single band uplink or PC3 or PC2 EN-DC are specified in Table 7.3B.2.3.1-1 For these exceptions, only the listed test points in Table 7.3B.2.3.1-1 need to be tested.

Table 7.3B.2.3.1-1: Reference sensitivity exceptions (MSD) due to UL harmonic for EN-DC in NR FR1

Table 7.3B.2.3.1-2: Void

Table 7.3B.2.3.1-3: Reference sensitivity QPSK PREFSENS (EN-DC with n46)

Table 7.3B.2.3.1-4: Void

Table 7.3B.2.3.1-5: Uplink configuration for reference sensitivity exceptions due to receiver harmonic mixing for EN-DC paring with n46

## 7.3B.2.3.2Reference sensitivity exceptions due to receiver harmonic mixing for EN-DC in NR FR1

Sensitivity degradation is allowed for different combinations of UL configurations and DL channel bandwidths if a band is impacted by receiver harmonic mixing due to another band part of the same EN-DC configuration. Reference sensitivity exceptions for the victim band (low) and uplink/downlink configurations due to UL harmonic from a PC3 aggressor UL band (high) for either single band uplink or PC3 or PC2 EN-DC are specified in Table 7.3B.2.3.2-1.

Reference sensitivity exceptions and uplink/downlink configurations due to harmonic mixing from a PC2 aggressor UL for PC2 EN-DC are specified in Table 7.3B.2.3.2-1a.

For these exceptions, only the listed test points in Table 7.3B.2.3.2-1 and Table 7.3B.2.3.2-1a need to be tested.

Table 7.3B.2.3.2-1: Reference sensitivity exceptions (MSD) due to receiver harmonic mixing for EN-DC in NR FR1

Table 7.3B.2.3.2-1a: Reference sensitivity exceptions (MSD) due to receiver harmonic mixing for PC2 EN-DC in NR FR1

Table 7.3B.2.3.2-2: Void

## 7.3B.2.3.3Void

## 7.3B.2.3.4Reference sensitivity exceptions due to cross band isolation for EN-DC in NR FR1

Sensitivity degradation is allowed for a band if it is impacted by UL of another band part of the same EN-DC configuration due to cross band isolation issues. Reference sensitivity exceptions for the victim band are specified only for the specific uplink and downlink test points specified in Table 7.3B.2.3.4-1 and Table 7.3B.2.3.4-1a.

In Tables 7.3B.2.3.4-1 and 7.3B.2.3.4-1a the following terminology is used to define the source of cross-band isolation interference:

- “ACLR1” indicates that the first adjacent channel of the aggressor UL band falls into the Rx channel of victim band.

- “ACLR2” indicates that the second adjacent channel of the aggressor UL band falls into the Rx channel of victim band.

- “>ACLR2” indicates that neither the first, nor the second adjacent channel of the aggressor UL band falls into the Rx channel of victim band.

Table 7.3B.2.3.4-1: Reference sensitivity exceptions (MSD) due to cross band isolation and uplink/downlink configurations for PC3 EN-DC in NR FR1

Table 7.3B.2.3.4-1a: Reference sensitivity exceptions (MSD) due to cross band isolation and uplink/downlink configurations for PC2 EN-DC in NR FR1

Table 7.3B.2.3.4-2: Void

## 7.3B.2.3.5MSD for intermodulation interference due to dual uplink operation for EN-DC in NR FR1

7.3B.2.3.5.0General

For EN-DC configurations in NR FR1 the UE may indicate capability of not supporting simultaneous dual uplink operation due to possible intermodulation interference overlapping in frequency to its own primary downlink channel bandwidth if

-the intermodulation order is 2;

-the intermodulation order is 3 when both operating bands are between 450 MHz – 960 MHz or between 1427 MHz – 2690 MHz

In the case for EN-DC configurations in NR FR1 for which the intermodulation products caused by dual uplink operation do not interfere with its own primary downlink channel bandwidth as defined in Annex I the UE is mandated to operate in dual and triple uplink mode.

For EN-DC configurations in NR FR1 with uplink and downlink assigned to E-UTRA and NR FR1 bands given in Table 7.3B.2.3.5.1-1, Table 7.3B.2.3.5.1-1a, Table 7.3B.2.3.5.2-0 and Table 7.3B.2.3.5.2-1 the reference sensitivity is defined only for the specific uplink and downlink test points specified in Table 7.3B.2.3.5.1-1, Table 7.3B.2.3.5.1-1a, Table 7.3B.2.3.5.2-0 and Table 7.3B.2.3.5.2-1. For these test points the reference sensitivity levels specified in clause 7.3.1 in TS 36.101 [4] and 7.3.2 of TS 38.101-1 [2] for the corresponding channel bandwidths or in clause 7.3.1 of TS 36.101 [4] are relaxed by the amount of the parameter MSD given in Table 7.3B.2.3.5.1-1, Table 7.3B.2.3.5.1-1a, Table 7.3B.2.3.5.2-0 and Table 7.3B.2.3.5.2-1.

The throughput on each of the CGs shall be ≥ 95% of the maximum throughput of the respective reference measurement channels as specified in Annex A of TS 38.101-1 [2] and Annex A of TS 36.101 [4], with parameters specified in Table 7.3B.2.3.5.1-1, Table 7.3B.2.3.5.1-1a, Table 7.3B.2.3.5.2-0 and Table 7.3B.2.3.5.2-1 with dual UL transmissions overlapping in time unless otherwise stated.

## 7.3B.2.3.5.1MSD test points for intermodulation interference due to dual uplink operation for PC3 EN-DC in NR FR1 involving two bands

Table 7.3B.2.3.5.1-1: MSD test points for PCell due to dual uplink operation for PC3 EN-DC in NR FR1 (two bands)

Table 7.3B.2.3.5.1-1a: MSD test points for PCell due to dual uplink operation for PC2 EN-DC in NR FR1 (two bands)

## 7.3B.2.3.5.2MSD test points for intermodulation interference due to dual uplink operation for EN-DC in NR FR1 involving three bands

Table 7.3B.2.3.5.2-0: MSD test points for Pcell due to dual uplink operation for EN-DC in NR FR1 (three bands)

Table 7.3B.2.3.5.2-1: MSD test points for Scell due to dual uplink operation for EN-DC in NR FR1 (three bands)

Table 7.3B.2.3.5.2-1a: MSD test points for SCell due to dual uplink operation for PC2 EN-DC in NR FR1 (three bands)

## 7.3B.2.3.5.3Void

## 7.3B.2.3.5.4MSD test points for intermodulation interference due to dual uplink operation for EN-DC in NR FR1 involving four bands

Table 7.3B.2.3.5.4-1: MSD test points for Scell due to dual uplink operation for EN-DC in NR FR1 (four bands)

## 7.3B.2.3aInter-band NE-DC within FR1

## 7.3B.2.3a.0General

Reference sensitivity exceptions are specified for the condition when there is uplink transmission only in the aggressor band. This clause addresses directly only NE-DC configurations that don't have a corresponding specified EN-DC configuration or specific NE-DC exceptions.

## 7.3B.2.3a.1Reference sensitivity exceptions due to UL harmonic interference for NE-DC in NR FR1

Sensitivity degradation is allowed for a band if it is impacted by UL harmonic interference from another band part of the same NE-DC configuration. For the NE-DC cconfigurations that have an EN-DC defined configuration, the reference sensitivity exceptions for the victim band (high) are specified in Table 7.3B.2.3.1-1 with uplink configuration of the aggressor band (low) are applicable.

## 7.3B.2.3a.2Reference sensitivity exceptions due to receiver harmonic mixing for NE-DC in NR FR1

Sensitivity degradation is allowed for a band if it is impacted by receiver harmonic mixing due to another band part of the same NE-DC configuration. For the NE-DC cconfigurations that have an EN-DC defined configuration, the reference sensitivity exceptions for the victim band (low) are specified in Table 7.3B.2.3.2-1 with uplink configuration of the agressor band (high).

Table 7.3B.2.3a.2-1: Reference sensitivity exceptions (MSD) due to receiver harmonic mixing for NE-DC in NR FR1

## 7.3B.2.3a.3Reference sensitivity exceptions due to cross band isolation for NE-DC in NR FR1

Sensitivity degradation is allowed for a band if it is impacted by UL of another band part of the same NE-DC configuration due to cross band isolation issues. Reference sensitivity exceptions for the victim band are specified in Table 7.3B.2.3a.3-1.

For the NE-DC configurations that have an EN-DC defined configuration, the reference sensitivity exceptions for the victim band are specified in Table 7.3B.2.3.4-1 and Table 7.3B.2.3.4-1a.

Table 7.3B.2.3a.3-1: Reference sensitivity exceptions (MSD) due to cross band isolation and uplink/downlink configurations for PC3 NE-DC in NR FR1

Table 7.3B.2.3a.3-2: Void

## 7.3B.2.3a.4MSD for intermodulation interference due to dual uplink operation for NE-DC in NR FR1

## 7.3B.2.3a.4.1(Reserved)

## 7.3B.2.3a.4.2MSD test points for intermodulation interference due to dual uplink operation for NE-DC in NR FR1 involving three bands

Table 7.3B.2.3a.4.2-1

## 7.3B.2.4Inter-band EN-DC including FR2

## 7.3B.2.4.1Void

## 7.3B.2.5Inter-band EN-DC including both FR1 and FR2

## 7.3B.2.5.1Reference sensitivity exceptions due to UL harmonic interference for EN-DC including both FR1 and FR2

For inter-band EN-DC of E-UTRA and NR in both FR1 and FR2, the UE is allowed to apply each sensitivity degradation for EN-DC in FR1 specified in clause 7.3B.2.3 TS 38.101-3 and for EN-DC including FR2 specified in clause 7.3B.2.3 of TS 38.101-3 independently.

## 7.3B.2.3.6Void

## 7.3B.2.3.7Lower-MSD requirements for inter-band EN-DC within FR1

A UE can report better MSD performance than the minimum requirements as specified in clause 7.3B.2.3.1, 7.3B.2.3.2, 7.3B.2.3.4, 7.3B.2.3.5, 7B.2.3.2.0.1, and 7B.2.3.2.0.2 by lowerMSD-r18 capability, except that the reporting for MSD caused by IMD with order higher than 5, IMD of UL intra-band CA or triple-beat is not supported in this release of the specification. The MSD performance after improvement is categorized into different lower-MSD capability classes, which are defined in Table 7.3A.7-1 of TS 38.101-1 [2].

The reported lower-MSD capability classes are subject to the same uplink/downlink configurations as defined for the minimum MSD requirements in clause 7.3B.2.3, 7B.2.3.2.0.1, and 7B.2.3.2.0.2. If a UE can support more than one test points for a given REFSENS exception case, the reported lower-MSD capability class is applicable for the test point having the largest specified MSD value. Otherwise, it’s only applicable for the test point which can be supported by the UE. If one or multiple power classes are requested by the network, the UE can, if supported, report lowerMSD-r18 capability for the requested power classes; otherwise, the UE shall report lowerMSD-r18 capability for the highest supported power class for the given DC configuration.

The UE shall meet one of the following conditions in order to report lowerMSD-r18 capability for a given REFSENS exception case:

If the specified minimum requirement is tightly bounded by the range of a lower-MSD capability class (i.e, Thresholdi-1 < MSD ≤ Thresholdi, where i and (i-1) are two adjacent lower-MSD capability classes), the actual MSD shall be at least one-level lower (i.e., actual MSD ≤ Thresholdi-1); or

If the specified minimum requirement is larger than the maximum threshold (corresponding to lower-MSD capability class VIII), the actual MSD shall be no more than the maximum threshold.

Otherwise, the UE shall not report lowerMSD-r18 capability for this REFSENS exception case.

If the special MSD type “ALL” is indicated in the lowerMSD-r18 capability, the reporting conditions as specified above shall be met for each MSD type that has been specified in this release for the given DC configuration.

NOTE 1: The lowerMSD-r18 capability is verified by reusing the MSD test point parameters and only replacing the minimum MSD requirement value by the threshold of the reported lower-MSD capability class. UE supporting lower MSD shall indicate the lower MSD capability for the requested power class if supported. If no power class is explicitly requested, the UE supporting lower MSD shall indicate the lower MSD capability for the highest supported power class of the band combination including victim band and aggressor band(s).. And, similar to the specified MSD minimum requirements, only the highest supported power class or the power class required by the certification/regulation body per UL configuration is verified.

NOTE 2: If the UE is equipped with four or eight Rx antenna ports for the victim band of the BC, the lowerMSD-r18 capability is verified with four or eight Rx antenna ports according to clause 7.1 under the condition mentioned above, but with the increased MSD values by the absolute value of ΔRIB,4R or ΔRIB,8R applied for the requirement based on the description in clause 7.3B.1.

## 7.3B.3ΔRIB,c, ΔRIBNC for DC

## 7.3B.3.0General

For the UE which supports inter-band EN-DC or NE-DC configuration, the minimum requirement for reference sensitivity in Table 7.3.1-1 and Table 7.3.1-1a in TS 36.101 [4], clause 7.3.2, 7.3A.2, 7.3C.2 in TS 38.101-1 [2] and clause 7.3.2, 7.3A.2 in TS 38.101-2 [3] shall be increased by the amount given in ΔRIB,c, ΔRIBNC in Tables below where unless otherwise stated, the same ΔRIB,c, ΔRIBNC are applicable to NR band(s) part for DC configurations which have the same NR operating band combination. Unless otherwise stated, ΔRIB,c or ΔRIBNC is set to zero.

In case the UE supports more than one of band combinations for CA, SUL or DC, and an operating band belongs to more than one band combinations then

-When the operating band frequency range is ≤ 1 GHz, the applicable additional ΔRIB,c shall be the average value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in TS 38.101-1 [2] and 7.3A, 7.3B in this specification, truncated to one decimal place that apply for that operating band among the supported band combinations. In case there is a harmonic relation between low band UL and high band DL, then the maximum ΔRIB,c among the different supported band combinations involving such band shall be applied

-When the operating band frequency range is > 1 GHz, the applicable additional ΔRIB,c shall be the maximum value for all band combinations defined in clause 7.3A, 7.3B, 7.3C in TS 38.101-1 [2] and 7.3A, 7.3B in this specification for the applicable operating bands.

Unless ΔRIB,c is specified for the NE-DC configuration, the specified ΔRIB,c for the EN-DC configuration including same bands as the corresponding NE-DC configuration is applicable for the NE-DC configuration.

## 7.3B.3.1Intra-band contiguous EN-DC

## 7.3B.3.2Intra-band non-contiguous EN-DC

Table 7.3B.3.2-1: Intra-band non-contiguous EN-DC with one uplink configuration on E-UTRA for reference sensitivity (E-UTRA uplink carrier is closer to the NR downlink carrier than it is to the E-UTRA downlink carrier)

Table 7.3B.3.2-2: Intra-band non-contiguous EN-DC with one uplink configuration on NR for reference sensitivity (NR uplink carrier is closer to the E-UTRA downlink carrier than it is to the NR downlink carrier)

## 7.3B.3.3Inter-band EN-DC within FR1

## 7.3B.3.3.1ΔRIB,c for EN-DC in two bands

Table 7.3B.3.3.1-1: ΔRIB,c due to EN-DC(two bands)

## 7.3B.3.3.2ΔRIB,c for EN-DC three bands

Table 7.3B.3.3.2-1: ΔRIB,c due to EN-DC (three bands)

## 7.3B.3.3.3ΔRIB,c for EN-DC four bands

Table 7.3B.3.3.3-1: ΔRIB,c due to EN-DC (four bands)

## 7.3B.3.3.4ΔRIB,c for EN-DC five bands

Table 7.3B.3.3.4-1: ΔRIB,c due to EN-DC (five bands)

## 7.3B.3.3.5ΔRIB,c for EN-DC six bands

Table 7.3B.3.3.5-1: ΔRIB,c due to EN-DC (six bands)

## 7.3B.3.3aInter-band NE-DC within FR1

Unless ΔRIB,c is specified in this clause, the value of ΔRIB,c for the correspondingly specified EN-DC configuration in clause 7.3B.3.3 is applicable.

Table 7.3B.3.3a.1-1: ΔRIB,c due to NE-DC(two bands)

## 7.3B.3.4Inter-band EN-DC including FR2

## 7.3B.3.4.1ΔRIB,c for EN-DC in two bands

Unless otherwise stated, ΔRIB,c for E-UTRA and FR2 NR bands of inter-band EN-DC combinations defined in table 5.5B.5.1-1 is set to zero.

Table 7.3B.3.4.1-1: Void

## 7.3B.3.4.2ΔRIB,c for EN-DC three bands

Unless otherwise stated, ΔRIB,c for FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA bands for inter-band EN-DC defined in table 5.5B.5.3-1 is the same as those for the corresponding E-UTRA CA configuration specified in TS 36.101 [4], without the FR2 NR bands.

Table 7.3B.3.4.2-1: Void

## 7.3B.3.4.3ΔRIB,c for EN-DC four bands

Unless otherwise stated, ΔRIB,c for FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA bands for inter-band EN-DC defined in table 5.5B.5.3-1 is the same as those for the corresponding E-UTRA CA configuration specified in TS 36.101 [4], without the FR2 NR bands.

Table 7.3B.3.4.3-1: Void

## 7.3B.3.4.4ΔRIB,c for EN-DC five bands

Unless otherwise stated, ΔRIB,c for FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA bands for inter-band EN-DC defined in table 5.5B.5.4-1 is the same as those for the corresponding E-UTRA CA configuration specified in TS 36.101 [4], without the FR2 NR bands.

Table 7.3B.3.4.4-1: Void

## 7.3B.3.4.5Void

## 7.3B.3.4a(Void)

## 7.3B.3.5Inter-band EN-DC including both FR1 and FR2

## 7.3B.3.5.2ΔRIB,c for EN-DC three bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.2-1, ΔRIB,c for constituent FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 7.3B.3.3.

Table 7.3B.3.5.2-1: Void

## 7.3B.3.5.3ΔRIB,c for EN-DC four bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.3-1, ΔRIB,c for constituent FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 7.3B.3.3.

## 7.3B.3.5.4ΔRIB,c for EN-DC five bands

Unless otherwise stated, for a certain inter-band EN-DC configurations defined in table 5.5B.6.4-1, ΔRIB,c for constituent FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 7.3B.3.3.

## 7.3B.3.5.5ΔRIB,c for EN-DC six bands

Unless otherwise stated, for inter-band EN-DC configurations defined in table 5.5B.6.5-1, ΔRIB,c for constituent FR2 NR bands is set to zero, and ΔRIB,c for constituent E-UTRA and FR1 NR bands is the same as those for the corresponding inter band EN-DC configuration without the FR2 bands specified in 7.3B.3.3.

## 7.3EReference sensitivity for V2X operation in FR1

## 7.3E.1General

For V2X operation, REFSENS requirements defined in TS 38.101-1 [2] and TS 36.101 [4] apply to all downlink bands of V2X configurations listed in clause 5.5E, unless sensitivity degradation exception is allowed in this clause of this specification, clause 7.3E in TS 38.101-1 [2] or clause 7.3.1G in TS 36.101 [4].

## 7.3E.2Reference sensitivity for V2X

## 7.3E.2.1Intra-band contiguous V2X

For intra-band contiguous V2X listed in Table 5.5E.2-1, the each REFSENS requirements specified in clause 7.3.1G of TS 36.101 [4] and clause 7.3E.2 of TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

## 7.3E.2.2Intra-band non-contiguous V2X

For intra-band non-contiguous V2X listed in Table 5.5E.3-1, the each REFSENS requirements specified in clause 7.3.1G of TS 36.101 [4] and clause 7.3E.2 of TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

## 7.3E.2.3Inter-band V2X con-current operation

## 7.3E.2.3.0General

When UE is configured for NR V2X reception on V2X carrier con-current with E-UTRA uplink and downlink, NR V2X sidelink throughput for the carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.7.2 with parameters specified in table 7.3E.2-1 and 7.3E.2-2 in TS 38.101-1. Also the E-UTRA downlink throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.3 with parameters specified in Table 7.3.1-1 and Table 7.3.1-2 in TS 36.101.

When UE is configured for E-UTRA V2X reception on V2X carrier con-current with NR uplink and downlink, E-UTRA V2X sidelink throughput for the carrier shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.8.2 with parameters specified in Table 7.3.1G-1 in TS 36.101. Also the NR downlink throughput shall be ≥ 95% of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2.2, A3.2 and A.3.3 with parameters specified in Table 7.3.2-1a, Table 7.3.2-1b and Table 7.3.2-2 in TS 38.101-1.

The reference sensitivity is defined to be met with all downlink component carriers active. The REFSENS of Uu downlink and PC5 sidelink will be tested at the same time.

Table 7.3E.2.3.0-1: Void

Table 7.3E.2.3.0-2 is specified the additional Rx insertion loss according to different RF architecture with DC/CA UE with same band combinations to reduce the self interference problem based on specific self desense analysis according to specific NR V2X inter-band con-current operation.

Table 7.3E.2.3.0-2: ΔRIB,V2X (two bands)

Table 7.3E.2.3.0-3: Void

Table 7.3E.2.3.0-4: Void

## 7.3E.2.3.1Reference sensitivity exception due to UL harmonic problem

Sensitivity degradation is allowed for a band if it is impacted by UL harmonic interference from another band part of the inter-band con-current V2X UE. Reference sensitivity exceptions (MSD) for the victim band (high) are specified in Table 7.3E.2.3.1-1 with uplink configuration of the aggressor band (low) specified in Table 7.3E.2.3.1-2.

Table 7.3E.2.3.1-1: Reference sensitivity exceptions (MSD) due to UL harmonic for inter-band con-current operation

Table 7.3E.2.3.1-2: Uplink configuration for reference sensitivity exceptions due to UL harmonic interference for inter-band con-current V2X in NR FR1

## 7.4Void

## 7.4AMaximum input level for CA

For inter-band NR CA between FR1 and FR2, the maximum input level specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for FR1 and FR2 respectively.

## 7.4BMaximum input level for DC in FR1

## 7.4B.1Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC maximum input level requirement and parameters are defined in Table 7.4B.1-1.

Table 7.4B.1-1: Maximum Input

## 7.4B.1a(Void)

## 7.4B.2Intra-band non-contiguous EN-DC in FR1

For the E-UTRA sub-block containing one or multiple CC's, the requirement is defined in clause 7.4.1 for single carrier operation and in clause 7.4.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.4 in TS 38.101-1 [2].

## 7.4B.3Inter-band EN-DC within FR1

Maximum input level requirement for E-UTRA single carrier and CA operation specified in clauses 7.4.1 and 7.4.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.4 and 7.4A of TS 38.101-1 [2] apply.

## 7.4B.3a(Void)

## 7.4B.4Inter-band EN-DC including FR2

Maximum input level requirement for E-UTRA single carrier and CA operation specified in clauses 7.4.1 and 7.4.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.4, 7.4A and 7.4B of TS 38.101-2 [3] apply.

## 7.4B.4a(Void)

## 7.4B.5Inter-band EN-DC including both FR1 and FR2

Maximum input level requirement for E-UTRA single carrier and CA operation specified in clauses 7.4.1 and 7.4.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.4, 7.4A and 7.4B of TS 38.101-1 [2] and TS 38.101-2 [3] apply.

## 7.4EMaximum input level for V2X operation in FR1

For intra-band V2X UE, the maximum input requirements specified in clause 7.4.1G of TS 36.101 [4] and clause 7.4E.2 of TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

For the inter-band con-current NR V2X operation, the requirements specified in subclause 7.4E of TS 38.101-1 [2] shall apply for the NR sidelink reception in Band n47 and the requirements specified in subclause 7.4.1 of TS 36.101 [4] shall apply for the E-UTRA downlink reception in licensed band while all downlink carriers are active.

## 7.5Void

## 7.5AAdjacent channel selectivity for CA

For inter-band NR CA between FR1 and FR2, the adjacent channel selectivity specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for FR1 and FR2 respectively.

## 7.5BAdjacent channel selectivity for DC in FR1

## 7.5B.1Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC ACS requirement and parameters are defined for test case 1 in Table 7.5B.1-1 and for test case 2 in Table 7.5B.1-2.

Table 7.5B.1-1: ACS test case 1

Table 7.5B.1-2: ACS test case 2

## 7.5B.1a(Void)

## 7.5B.2Intra-band non-contiguous EN-DC in FR1

For the E-UTRA sub-block containing one or multiple CC's, the requirement is defned in clause 7.5.1 for single carrier operation and in clause 7.5.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.5 in TS 38.101-1 [2].

The blocker configuration is defined in the general clause 7.1.

## 7.5B.3Inter-band EN-DC within FR1

Adjacent channel selectivity requirement for E-UTRA single carrier and CA operation specified in clauses 7.5.1 and 7.5.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.5 and 7.5A of TS 38.101-1 [2] apply.

## 7.5B.3a(Void)

## 7.5B.4Inter-band EN-DC including FR2

Adjacent channel selectivity requirement for E-UTRA single carrier and CA operation specified in clauses 7.5.1 and 7.5.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.5, 7.5A and 7.5B of TS 38.101-2 [3] apply.

## 7.5B.4a(Void)

7.5B.5Inter-band EN-DC including both FR1 and FR2

Adjacent channel selectivity requirement for E-UTRA single carrier and CA operation specified in clauses 7.5.1 and 7.5.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.5, 7.5A and 7.5Bof TS 38.101-1 [2] and TS 38.101-2 [3] apply.

## 7.5EAdjacent channel selectivity for V2X operation in FR1

For intra-band V2X operation, the adjacent channel selectivity specified in clause 7.5.1G in TS 36.101 [4] and specified in clause 7.5C in TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

For the inter-band con-current NR V2X operation, the requirements specified in subclause 7.5E of TS 38.101-1 [2] shall apply for the NR sidelink reception in Band n47 and the requirements specified in subclause 7.5.1 of TS 36.101 [4] shall apply for the E-UTRA downlink reception in licensed band while all downlink carriers are active.

## 7.6Void

## 7.6ABlocking characteristics for CA

For inter-band NR CA between FR1 and FR2, the in-band blocking characteristics specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for FR1 and FR2 respectively. The narrow band blocking and out-of-band blocking specified in TS 38.101-1 [2] apply for FR1.

## 7.6BBlocking characteristics for DC in FR1

## 7.6B.1General

## 7.6B.2In-band blocking for DC in FR1

## 7.6B.2.1Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC in-band blocking requirement and parameters are defined in Table 7.6B.2.1-1.

Table 7.6B.2.1-1: In-band blocking

## 7.6B.2.1a(Void)

## 7.6B.2.2Intra-band non-contiguous EN-DC in FR1

For the E-TRA sub-block containing one or multiple CC's, the requirement is deined in clause 7.6.1.1 for single carrier operation and in clause 7.6.1.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.6.2 in TS 38.101-1 [2].

The blocker configuration is defined in the general clause 7.1.

## 7.6B.2.3Inter-band EN-DC within FR1

Inband blocking requirement for E-UTRA single carrier and CA operation specified in clauses 7.6.1.1 and 7.6.1.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.2 and 7.6A.2 of TS 38.101-1 [2] apply.

## 7.6B.2.3a(Void)

## 7.6B.2.4Inter-band EN-DC including FR2

Inband blocking requirement for E-UTRA single carrier and CA operation specified in clauses 7.6.1.1 and 7.6.1.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.2, 7.6A.2 and 7.6B.2 of TS 38.101-2 [3] apply.

## 7.6B.2.4a(Void)

## 7.6B.2.5Inter-band EN-DC including both FR1 and FR2

Inband blocking requirement for E-UTRA single carrier and CA operation specified in clauses 7.6.1.1 and 7.6.1.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.2, 7.6A.2 and 7.6B.2 of TS 38.101-1 [2] and TS 38.101-2 [3] apply.

## 7.6B.2.6Void

Table 7.6B.2.6-1: Void

Table 7.6B.2.6-2: Void

## 7.6B.3Out-of-band blocking for DC in FR1

## 7.6B.3.1Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC out-of-band requirement and parameters are defined in Table 7.6B.3.1-1.

Table 7.6B.3.1-1: Out-of-band blocking

For Table 7.6.2.1A-2 from TS 36.101 [4] in frequency range 1, 2 and 3, up to exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a 1MHz step size. For these exceptions the requirements of subclause 7.7B.1 Spurious response are applicable.

## 7.6B.3.1a(Void)

## 7.6B.3.2Intra-band non-contiguous EN-DC in FR1

For the E-UTRA sub-block containing one or multiple CC's, the requirement is dfined in clause 7.6.2.1 for single carrier operation and in clause 7.6.2.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.6.3 is [2].

## 7.6B.3.3Inter-band EN-DC within FR1

Out-of band blocking requirements for E-UTRA single carrier and CA operation specified in clauses 7.6.2.1 and 7.6.2.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.3 and 7.6A.3 of TS 38.101-1 [2] apply for lowest level EN-DC fallbacks (two bands) in clause 5.5B.4.1 with following conditions

-one E-UTRA uplink carrier with the output power set to 4 dB below PCMAX_L,c and the NR band whose downlink is being tested has its uplink carrier output power set to 29 dB below PCMAX_L,f,c.

-one NR uplink carrier with the output power set to 4 dB below PCMAX_L,f,c on the NR band with both E-UTRA and NR downlinks being tested with E-UTRA output power set to 29 dB below PCMAX_L,c.

If CW interferer falls in a gap between FDL_high of the E-UTRA or NR band and FDL_low of the NR or EUTRA band, where the corresponding OOB ranges 1 and 2 overlap, then the lower level interferer limit of the overlapping OOB ranges applies.

If FDL_high of the lower E-UTRA or NR band is greater than or equal to the FDL_low of the upper NR or E-UTRA band as in overlapping RX frequency ranges, then the OOB range shall start from the FDL_low of the lower E-UTRA or NR band, and from the FDL_high of the upper NR or E-UTRA band.

For ENDC combination listed in Table 7.6B.3.3-1 under the first test condition above, exceptions to the requirement specified in Table 7.6B.3.3-2 are allowed when the second order intermodulation product of the lower frequency band UL carrier and the CW interfering signal fully or partially overlaps with the higher frequency band DL carrier.

Table 7.6B.3.3-1: ENDC combination with exceptions allowed

For each of the two test cases in clauses 7.6.2.1 and 7.6.2.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.3 and 7.6A.3 of TS 38.101-1 [2] for all interferer frequency ranges a maximum of

exceptions are allowed for spurious response frequencies in each assigned frequency channel when measured using a step size of  MHz with NRB the number of resource blocks in the downlink transmission bandwidth configuration, CBW the bandwidth of the frequency channel in MHz and n = 1, 2, 3 for SCS = 15, 30, 60 kHz, respectively. For these exceptions, the requirements in clause 7.7 apply.

## 7.6B.3.3a(Void)

## 7.6B.3.4Inter-band EN-DC including FR2

Out-of band blocking requirements specified for E-UTRA single carrier and CA operation specified in clauses 7.6.2.1 and 7.6.2.1A of TS 36.101 [4] apply for lowest level EN-DC fallbacks (two bands) in clause 5.5B.5.1 with only E-UTRA UL with output power as in TS 36.101 [4] (4 dB below PCMAX_L).

## 7.6B.3.4a(Void)

## 7.6B.3.5Inter-band EN-DC including both FR1 and FR2

Out-of band blocking requirements specified for E-UTRA single carrier and CA operation specified in clauses 7.6.2.1 and 7.6.2.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.3 and 7.6A.3 of TS 38.101-1 [2] apply for lowest level EN-DC fallbacks (three bands) in clause 5.5B.6.2 with only E-UTRA UL with output power as in TS 36.101 [4] (4 dB below PCMAX_L).

## 7.6B.4Narrow band blocking for DC in FR1

## 7.6B.4.1Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC narrow band blocking requirement and parameters are defined in Table 7.6B.4.1-1.

Table 7.6B.4.1-1: Narrow band blocking parameters

## 7.6B.4.1a(Void)

## 7.6B.4.2Intra-band non-contiguous EN-DC in FR1

For the E-TRA sub-block containing one or multiple CC's, the requirement is deined in clause 7.6.3.1 for single carrier operation and in clause 7.6.3.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.6.4 in TS 38.101-1 [2].

The blocker configuration is defined in the general clause 7.1.

## 7.6B.4.3Inter-band EN-DC within FR1

Narrow band blocking requirement for E-UTRA single carrier and CA operation specified in clauses 7.6.3.1 and 7.6.3.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.4 and 7.6A.4 of TS 38.101-1 [2] apply.

## 7.6B.4.3a(Void)

## 7.6B.4.4Inter-band EN-DC including FR2

Narrow band blocking requirement for E-UTRA single carrier and CA operation specified in clauses 7.6.3.1 and 7.6.3.1A of TS 36.101 [4] apply.

## 7.6B.4.4a(Void)

## 7.6B.4.5Inter-band EN-DC including both FR1 and FR2

Narrow band blocking requirement for E-UTRA single carrier and CA operation specified in clauses 7.6.3.1 and 7.6.3.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.6.4 and 7.6A.4 of TS 38.101-1 [2] apply.

## 7.6EBlocking characteristics for V2X in FR1

For intra-band V2X operation, the blocking charateristics specified in clause 7.6.1.1G in TS 36.101 [4] and specified in clause 7.6E in TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

For inter-band con-current NR V2X operation, the in-band blocking and out of band blocking requirement specified in clause 7.6E in TS 38.101-1 [2] shall apply on NR V2X carrier and the requirement specified in clause 7.6 in TS 36.101 [4] shall apply for the E-UTRA downlink reception in licensed band while all downlink carriers are active. PInterferer power is increased by ΔRIB,c in the requirement.

No narrow band blocking requirement applied for NR V2X carrier.

## 7.7Void

## 7.7ASpurious response for CA

For inter-band NR CA between FR1 and FR2, the spurious response specified in TS 38.101-1 [2] apply for FR1.

## 7.7BSpurious response for DC in FR1

## 7.7B.1Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC spurious response requirement and parameters are defined in Table 7.7B.1-1.

Table 7.7B.1-1: Spurious Response Parameters

## 7.7B.1a(Void)

## 7.7B.2Intra-band non-contiguous EN-DC in FR1

For the E-UTRA sub-block containing one or multiple CC's, the requirement is defined in clause 7.7.1 for single carrier operation and in clause 7.7.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.7 is [2].

## 7.7B.3Inter-band EN-DC within FR1

Spurious response requirement for E-UTRA single carrier and CA operation specified in clauses 7.7.1 and 7.7.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.7 and 7.7A of TS 38.101-1 [2] apply for lowest level EN-DC fallbacks (two bands) in clause 5.5.B.4.1 with following conditions

-one E-UTRA uplink carrier with the output power set to 4 dB below PCMAX_L and the NR band whose downlink is being tested has its uplink carrier output power set to 29 dB below PCMAX_L,f,c.

-one NR uplink carrier with the output power set to 4 dB below PCMAX_L,f,c on the NR band with both E-UTRA and NR downlinks being tested with E-UTRA output power set to 29 dB below PCMAX_L,c.

7.7B.3a(Void)

7.7B.4Inter-band EN-DC including FR2

Spurious response requirement for E-UTRA single carrier and CA operation specified in clauses 7.7.1 and 7.7.1A of TS 36.101 [4] apply for lowest level EN-DC fallbacks (two bands) in clause 5.5B.5.1 with only E-UTRA UL with output power as in TS 36.101 [4] (4 dB below PCMAX_L).

## 7.7B.4a(Void)

## 7.7B.5Inter-band EN-DC including both FR1 and FR2

Spurious response requirement for E-UTRA single carrier and CA operation specified in clauses 7.7.1 and 7.7.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.7 and 7.7A of TS 38.101-1 [2] apply for lowest level EN-DC fallbacks (three bands) in clause 5.5B.6.2 with only E-UTRA UL with output power as in TS 36.101 [4] (4 dB below PCMAX_L).

## 7.7ESpurious response for V2X in FR1

For intra-band V2X operation, the spurious response specified in clause 7.7.1G in TS 36.101 [4] and specified in clause 7.7E in TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

For the inter-band con-current NR V2X operation, the requirements specified in subclause 7.7E of TS 38.101-1 [2] shall apply for the NR sidelink reception in Band n47 and the requirements specified in subclause 7.7.1 of TS 36.101 [4] shall apply for the E-UTRA downlink reception in licensed band while all downlink carriers are active.

## 7.8Void

## 7.8AIntermodulation characteristics for CA

For inter-band NR CA between FR1 and FR2, the intermodulation characteristics specified in TS 38.101-1 [2] apply for FR1.

## 7.8BIntermodulation characteristics for DC in FR1

## 7.8B.1General

## 7.8B.2Wide band Intermodulation

## 7.8B.2.1Intra-band contiguous EN-DC in FR1

Intra-band contiguous EN-DC wide band intermodulation requirement and parameters are defined in Table 7.8B.2.1-1.

Table 7.8B.2.1-1: Wide band intermodulation

## 7.8B.2.1a(Void)

## 7.8B.2.2Intra-band non-contiguous EN-DC in FR1

For the E-UTRA sub-block containing one or multiple CC's, the requirement is defined in clause 7.8.1 for single carrier operation and in clause 7.8.1A for CA in TS 36.101 [4].

For the NR sub-block, the requirement is defined in clause 7.8.2 in TS 38.101-1 [2].

The blocker configuration is defined in the general clause 7.1 and the requirement only apply for out of gap interferers.

## 7.8B.2.3Inter-band EN-DC within FR1

Wide band Intermodulation requirement for E-UTRA single carrier and CA operation specified in clauses 7.8.1 and 7.8.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.8.2 and 7.8A.2 of TS 38.101-1 [2] apply.

## 7.8B.2.3a(Void)

## 7.8B.2.4Inter-band EN-DC including FR2

Wide band Intermodulation requirement for E-UTRA single carrier and CA operation specified in clauses 7.8.1 and 7.8.1A of TS 36.101 [4] apply.

## 7.8B.2.4a(Void)

## 7.8B.2.5Inter-band EN-DC including both FR1 and FR2

Wide band Intermodulation requirement for E-UTRA single carrier and CA operation specified in clauses 7.8.1 and 7.8.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.8.2 and 7.8A.2 of TS 38.101-1 [2] apply.

## 7.8EIntermodulation characteristics for V2X operation in FR1

For intra-band V2X operation, the intermodulation characteristics specified in clause 7.8.1G in TS 36.101 [4] and specified in clause 7.8E in TS 38.101-1 [2] apply when all SL reception CCs are activated at same time.

For inter-band NR V2X con-current operation, the wideband inter-modulation requirement specified in clause 7.8E in TS 38.101-1 [2] shall apply on NR V2X carrier and the requirement specified in clause 7.8.1 in TS 36.101 [4] shall apply on E-UTRA downlink reception in licensed band while all downlink carriers are active. PInterferer power is increased by ΔRIB,c in the requirement.

## 7.9Void

## 7.9ASpurious emissions for CA

For inter-band NR CA between FR1 and FR2, the spurious emission specified in TS 38.101-1 [2] and TS 38.101-2 [3] apply for FR1 and FR2 respectively.

## 7.9BSpurious emissions for DC in FR1

## 7.9B.1Intra-band contiguous EN-DC in FR1

The requirement is defined in clause 7.9A.1 in TS 38.101-1 [2].

## 7.9B.1a(Void)

## 7.9B.2Intra-band non-contiguous EN-DC in FR1

Spurious emissions requirement for E-UTRA single carrier and CA operation specified in clauses 7.9.1 and 7.9.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.9 and 7.9A of TS 38.101-1 [2] apply.

## 7.9B.3Inter-band EN-DC within FR1

E-UTRA requirements from TS 36.101 [4] and NR requirements from TS 38.101-1 [2] apply.

## 7.9B.3a(Void)

## 7.9B.4Inter-band EN-DC including FR2

Spurious emissions requirement for E-UTRA single carrier and CA operation specified in clauses 7.9.1 and 7.9.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clause 7.9 of TS 38.101-2 [3] apply.

## 7.9B.4a(Void)

7.9B.5Inter-band EN-DC including both FR1 and FR2

Spurious emissions requirement for E-UTRA single carrier and CA operation specified in clauses 7.9.1 and 7.9.1A of TS 36.101 [4] and for NR single carrier and CA operation specified in clauses 7.9 and 7.9A of TS 38.101-1 [2] and TS 38.101-2 [3] apply.

## 7.10Void

## 7.10AVoid

## 7.10BPower imbalance for DC in FR1

## 7.10B.1General

Power imbalance requirement is a measure of the receiver’s ability to receive a wanted signal (E-UTRA or NR) in the presence of another carrier signal (E-UTRA or NR) with 6 - 25dB power imbalance at a specific frequency offset from the wanted signal.

Power imbalance requirement in subclause 7.10B.3 is applicable for:

-A UE capable of interBandMRDC-WithOverlapDL-Bands-r16 and not capable of requirementTypeIndication-r18 or a UE capable of interBandMRDC-WithOverlapDL-Bands-r16 and requirementTypeIndication-r18 but is not provided with nonCollocatedTypeMRDC and is configured with maxMIMO-Layers with value less than or equal to 2; or,

-A UE capable of interBandMRDC-WithOverlapDL-Bands-r19 and nonCollocatedTypeMRDC-v1900 is provided with value type4 and is configured with maxMIMO-Layers equal to four.

## 7.10B.3Inter-band EN-DC within FR1

For these test parameters in table 7.10B.3-1, the throughput shall be ≥ 95 % of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.3.2, and A.3.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1 in 38.101-1).

Table 7.10B.3-1: Test parameters for FDD-FDD or TDD-TDD inter-band EN-DC operation with overlapping or partially overlapping DL bands

It’s allowed to use only one of the test configurations to verify the RX power imbalance requirement for a UE indicating capability interBandMRDC-WithOverlapDL-Bands-r16.

If the UE indicates interBandMRDC-WithOverlapDL-Bands-r16 but does not indicate requirementTypeIndication-r18 or a UE indicates both interBandMRDC-WithOverlapDL-Bands-r16 and requirementTypeIndication-r18 and IE nonCollocatedTypeMRDC is not provided when maxMIMO-Layers with value less than or equal to 2, the Rx requirements for two Rx ports are applicable  for each band in EN-DC operating mode for the following EN-DC band combinations in Table 7.10B.3-2.

For NR and EUTRA component carriers for the EN-DC band combinations in Table 7.10B.3-2, if the UE indicates interBandMRDC-WithOverlapDL-Bands-r19 and nonCollocatedTypeMRDC-v1900 is provided with value type4,

When the UE is provided with maxMIMO-Layers equals to four and maxLayersMIMO equals to two, the Rx requirements for four and two Rx ports are applicable for NR and EUTRA component carriers, repectively.

When UE is provided with maxMIMO-Layers and maxLayersMIMO equal to four, the Rx requirements for four Rx ports are applicable.

Table 7.10B.3-2: TDD-TDD ENDC combinations
