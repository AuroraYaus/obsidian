# TS 38.101 38101-1-j60_s06-06

## 6Transmitter characteristics

## 6.1General

Unless otherwise stated, the transmitter characteristics are specified at the antenna connector of the UE with a single or multiple transmit antenna(s). For UE with integral antenna only, a reference antenna with a gain of 0 dBi is assumed.

For UEs that do not indicate IE dualPA-Architecture, transmitter requirements for CA operation apply only when the DMRS initialization parameters (including the case when the UE applies cell ID as DMRS scrambling ID) are different across all CCs. The UE may use higher MPR values outside this limitation.

Transmitter requirements for UL MIMO operation apply when the UE transmits on 2 ports/4 ports on the same CDM group. The UE may use higher MPR values outside this limitation.

The applicability of transmitter requirements for Band n90 is in accordance with that for Band n41; a UE supporting Band n90 shall meet the minimum requirements for Band n41.

NOTE:For FRMCS (Future Railway Mobile Communication System) operation in bands n100 and n101, the principle described in annex M applies to account for the post chipset unit antenna connector gain Gn100post connector or Gn101post connector declared for the FRMCS cab-radio UE.

## 6.1AGeneral

The minimum requirements for band combinations including Band n41 also apply for the corresponding band combinations with Band n90 replacing Band n41 but with otherwise identical parameters. For brevity the said band combinations with Band n90 are not listed in the tables below but are covered by this specification.

UE supporting the IE posSRS-BWA-IndependentCA-RRC-Connected-r18 for SRS bandwidth aggregation shall meet the minimum requirements for intra-band contiguous CA for SRS transmission only.

## 6.1FGeneral

For wideband operations, the minimum requirements for the transmitter characteristics are specified for transmissions on one scheduled RB set or ≥ 1 scheduled contiguous RB set(s) within the UE channel. The requirements apply with configured UL intra-cell guard bands of non-zero size according to Table 5.3.3-2, with the union of the scheduled RB sets and the intra-cell guard bands.

Unless stated otherwise, when a clause is not present for shared spectrum channel access, the general requirements and the additional clause requirements (suffices A,B,D) in clause 6 apply.

## 6.1G(Reserved)

## 6.1H(Reserved)

## 6.1I(Reserved)

## 6.1JGeneral

Unless otherwise stated, the transmitter characteristics are specified at the antenna connector(s) of the ATG UE with one or multiple omni-directional antenna(s) or at the transceiver array boundary (TAB) connectors of the ATG UE with the antenna array. The definition about transceiver array boundary (TAB) is specified in clause 4.3.2 of TS 38.104 [16].

## 6.1K(Reserved)

## 6.1L(Reserved)

## 6.2Transmitter power

## 6.2.1UE maximum output power

The following UE Power Classes define the maximum output power for any transmission bandwidth within the channel bandwidth of NR carrier unless otherwise stated. The period of measurement shall be at least one sub frame (1ms).

Table 6.2.1-1: UE Power Class

If a UE supports a different power class than the default UE power class for the band and the supported power class enables the higher maximum output power than that of the default power class:

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is absent and the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than 50% (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is not absent and half the percentage of uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-PC1dot5-MPE-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or

-if the IE P-Max as defined in TS 38.331 [7] is provided and set to 23 dBm or lower;

-shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified in clause 6.2.4;

-else if the UE does not support a power class with higher maximum output power than PC2; or

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is absent and the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than 25% (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-PC2-FR1 (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is not absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-PC1dot5-MPE-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or

-if the IE P-Max as defined in TS 38.331 [7] is provided and set to 26 dBm or lower;

-shall apply all requirements for power class 2 to the supported power class and set the configured transmitted power as specified in clause 6.2.4;

-else shall apply all requirements for the supported power class and set the configured transmitted power as specified in clause 6.2.4.

## 6.2.1IVoid

## 6.2.2UE maximum output power reduction

UE is allowed to reduce the maximum output power due to higher order modulations and transmit bandwidth configurations. For UE power class 2 and 3 and UE power class 1, the allowed maximum power reduction (MPR) is defined in Table 6.2.2-2, Table 6.2.2-1, Table 6.2.2-1a, Table 6.2.2-4b and Table 6.2.2-5, respectively for channel bandwidths  ≤ 100 MHz.  For UE power class 1.5 with 2Tx, the allowed maximum power reduction  (MPR) is defined in Table 6.2D.2-2 and Table 6.2D.2-3 in accordance with the indicated modifiedMPR-Behaviour specified in Table L.1-1 for channel bandwidths ≤ 100 MHz. For UE power class 1.5 with 4 Tx, the allowed maximum power reduction is defined in Table 6.2D.2-4, 6.2D.2-5. When A UE that indicates PC1.5 for a given band is limited to PC2 by the rules in clause 6.2.1, the MPR requirements in Table 6.2.2-2 apply. Unless otherwise specified, ‘pi/2 BPSK’ refers to both variants of pi/2 BPSK referenced in Table 6.2.2-1 and Table 6.2.2-1a.

If the relative channel bandwidth ≤ 4% for TDD bands or ≤ 3% for FDD band, the ∆MPR is set to zero.

If the relative channel bandwidth > 4% for TDD bands or > 3% for FDD bands, the ∆MPR is defined in Table 6.2.2-3.

Where relative channel bandwidth = 2*BWChannel / (FUL_low + FUL_high)

The allowed MPR for SRS, PUCCH formats 0, 1, 3 and 4, and PRACH shall be as specified for QPSK modulated DFT-s-OFDM of equivalent RB allocation. The allowed MPR for PUCCH format 2 shall be as specified for QPSK modulated CP-OFDM of equivalent RB allocation.

Table 6.2.2-1 Maximum power reduction (MPR) for power class 3

Table 6.2.2-1a Maximum power reduction (MPR) for power class 3 with specific requirement for n104

Table 6.2.2-2 Maximum power reduction (MPR) for power class 2

Table 6.2.2-3: ∆MPR

Table 6.2.2-4 Void

Table 6.2.2-4a Void

Table 6.2.2-4b: Maximum power reduction (MPR) for power class 1 for bands other than Band n14

Table 6.2.2-5 Maximum power reduction (MPR) for power class 1 for Band n14

Where the following parameters are defined to specify valid RB allocation ranges for Outer and Inner RB allocations:

NRB is the maximum number of RBs for a given Channel bandwidth and sub-carrier spacing defined in Table 5.3.2-1. RBStart,Low = max(1, floor(LCRB/2))

where max() indicates the largest value of all arguments and floor(x) is the greatest integer less than or equal to x.

RBStart,High = NRB – RBStart,Low – LCRB

The RB allocation is an Inner RB allocation if the following conditions are met

RBStart,Low  ≤ RBStart  ≤ RBStart,High, and

LCRB ≤ ceil(NRB/2)

where ceil(x) is the smallest integer greater than or equal to x.

An Edge RB allocation is the one for which the RB(s) is (are) allocated at the lowermost or uppermost edge of the channel LCRB ≤ 2 RBs, except for PC1 UE supporting other bands than n14.

And for PC1 UE supporting other bands than n14 RB allocation is an Edge RB allocation if

AND (  OR  ),LCRB≤LCRB,edgeRBstart≤RBstart,edgeRBstart≥NRB-RBstart,edge-LCRB

where

LCRB,edge=6, CBW<50 MHz12, CBW≥50 MHz.

For  with DFT-S-OFDM waveform and pi/2-BPSK, QPSK, or 16-QAM modulation, Otherwise,  CBW≥70 MHz RBstart,edge=1.RBstart,edge=0.

The RB allocation is an Outer RB allocation for all other allocations which are not an Inner RB allocation or Edge RB allocation.

If ΔPPowerBoost is a positive value and the UE supports powerBoosting-pi2BPSK-QPSK-r18 and the UE does not indicate support for mpr-SingleCC-SingleValue-r19 or mpr-SingleCC-MultipleValue-r19, or if ΔPPowerBoost is a positive value and the UE supports powerBoosting-pi2BPSK-QPSK-r18 and indicates support for mpr-SingleCC-SingleValue-r19 or mpr-SingleCC-MultipleValue-r19, and the UE does not indicate support for [exclusive-MPR-Enh-PowerBoosting-r19], and is configured with the IE mprReductionExtensionRatio-r19

-An enhanced power inner allocation region within the inner region is defined so any waveform it contains satisfies the following condition:

RBStart,Low + P1  ≤ RBStart  ≤  RBStart,High - P1

Where P1 = MIN{12,CEIL(2+NRB/25)}

-When a UE that supports powerBoosting-pi2BPSK-QPSK-r18 but does not support powerBoosting-pi2BPSK-QPSK-Modified-r18 an RB allocation that belongs to the inner region but is outside the enhanced power inner region, the applicable MPR from Tables 6.2.2-1 and 6.2.2-2 is increased by the value of ΔPPowerBoost.

Else if ΔPPowerBoost is a positive value and the UE supports powerBoosting-pi2BPSK-QPSK-r18 and [exclusive-MPR-Enh-PowerBoosting-r19] and indicates support for mpr-SingleCC-SingleValue-r19 or mpr-SingleCC-MultipleValue-r19, and is configured with the IE mprReductionExtensionRatio-r19 then the enhanced power extended inner allocation region within the extended inner region is defined so any waveform it contains satisfies the following condition:

RBStart,Low_new + P1  ≤  RBStart  ≤  RBStart,High_new - P1

Where

RBStart,Low_new = max(0, max(1, floor(LCRB/2)) -ceil(Rext_low * NRB))

RBStart,High_new = = min(NRB-LCRB, NRB + ceil (Rext_high * NRB) - max(1, floor(LCRB/2))- LCRB)

P1 = MIN{12,ceil(2+(1+ Rext_low + Rext_high )NRB/25)}

-When a UE that supports powerBoosting-pi2BPSK-QPSK-r18 but does not support powerBoosting-pi2BPSK-QPSK-Modified-r18 and indicates support for mpr-SingleCC-SingleValue-r19 or mpr-SingleCC-MultipleValue-r19, and is configured with the IE mprReductionExtensionRatio-r19 an RB allocation that belongs to the extended inner region but is outside the enhanced power extended inner allocation region, the applicable MPR from Tables 6.2.2-1 and 6.2.2-2 is increased by the value of ΔPPowerBoost.

If all of the following conditions are simultaneously met:

-The UE is a PC3 or PC2 UE operating in any channel bandwidth except 3MHz or 7MHz.

-The UE indicates support for mpr-SingleCC-SingleValue-r19 or mpr-SingleCC-MultipleValue-r19, and is configured with the IE mprReductionExtensionRatio-r19.

-The uplink modulation order is either QPSK or 16QAM

-When no A-MPR is applicable to the configured channel

then:

-The RB allocation is an Inner RB allocation if the following conditions are met:

max(0, RBStart,Low – ceil(Rext_low * NRB )) ≤ RBStart ≤ min(NRB – LCRB, NRB + ceil(Rext_high * NRB ) – RBStart,Low – LCRB)

and LCRB ≤ ceil((NRB+ ceil(Rext_low * NRB ) + ceil(Rext_high * NRB ))/2)

-An Edge RB allocation is the one for which the RB(s) is (are) allocated at the lowermost edge of the channel LCRB ≤ 2 RBs with Rext_low = 0, or the one for which the RB(s) is (are) allocated at the uppermost edge of the channel LCRB ≤ 2 RBs with Rext_high = 0.

-The RB allocation is an Outer RB allocation for all other allocations which are not an Inner RB allocation or Edge RB allocation.

If CP-OFDM allocation satisfies following conditions, it is considered as almost contiguous allocation

NRB_gap / (NRB_alloc + NRB_gap ) ≤ 0.25

and NRB_alloc + NRB_gap is larger than 106, 51 or 24 RBs for 15 kHz, 30 kHz or 60 kHz respectively where NRB_gap is the total number of unallocated RBs between allocated RBs and NRB_alloc is the total number of allocated RBs. The size and location of allocated and unallocated RBs are restricted by RBG parameters specified in clause 6.1.2.2 of TS 38.214 [10]. For UE that indicates support for almostContiguousCP-OFDM-UL, the almost contiguous signals in power class 1.5, 2 and 3, the allowed maximum power reduction defined in Table 6.2.2-2, Table 6.2.2-1 and Tables 6.2D.2-1 to 6.2D.2-5 are increased by

CEIL{ 10 log10(1 + NRB_gap / NRB_alloc), 0.5 } dB,

where CEIL{x,0.5} means x rounding upwards to closest 0.5dB. The parameter of LCRB which is used to specify valid RB allocation ranges for Outer and Inner RB allocations is replaced by (NRB_alloc + NRB_gap) for almost contiguous allocation cases

For the UE maximum output power modified by MPR, the power limits specified in clause 6.2.4 apply.

## 6.2.3UE additional maximum output power reduction

## 6.2.3.1General

Additional emission requirements can be signalled by the network. Each additional emission requirement is associated with a unique network signalling (NS) value indicated in RRC signalling by an NR frequency band number of the applicable operating band and an associated value in the field additionalSpectrumEmission. Throughout this specification, the notion of indication or signalling of an NS value refers to the corresponding indication of an NR frequency band number of the applicable operating band, the IE field freqBandIndicatorNR and an associated value of additionalSpectrumEmission in the relevant RRC information elements [7].

To meet the additional requirements, additional maximum power reduction (A-MPR) is allowed for the maximum output power as specified in Table 6.2.1-1. Unless stated otherwise, the total reduction to UE maximum output power is max(MPR+∆MPR, A-MPR) where MPR and ∆MPR are defined in clause 6.2.2. Outer and inner allocation notation used in clause 6.2.3 is defined in clause 6.2.2. Unless stated otherwise, Edge RB allocations get the same AMPR as Outer RB allocations. In absence of modulation and waveform types the A-MPR applies to all modulation and waveform types.

Table 6.2.3.1-1 specifies the additional requirements with their associated network signalling values and the allowed A-MPR and applicable operating band(s) for each NS value. In case of a power class 3 UE, when IE powerBoostPi2BPSK is set to 1, power class 2 A-MPR values apply. When IE powerBoostPi2BPSK-r18 or powerBoostQPSK-r18 is enabled, A-MPR, if larger than zero, is increased by ΔPPowerBoost. The mapping of NR frequency band numbers and values of the additionalSpectrumEmission to network signalling labels is specified in Table 6.2.3.1-1A.

For almost contiguous allocations in CP-OFDM waveforms in power class 1.5, 2 and 3, the allowed A-MPR defined in clause 6.2.3 is increased by CEIL{ 10 log10(1 + NRB_gap / NRB_alloc), 0.5 } dB, where CEIL{x, 0.5} means x rounding upwards to closest 0.5dB, NRB_gap is the total number of unallocated RBs between allocated RBs and NRB_alloc is the total number of allocated RBs, and the parameter LCRB is replaced by NRB_alloc + NRB_gap in specifying the RB allocation regions.

Unless otherwise specified, pi/2 BPSK in following A-MPR tables refers to both variants of pi/2 BPSK referenced in clause 6.2.2 Table 6.2.2-1.

Table 6.2.3.1-1: Additional maximum power reduction (A-MPR)

Table 6.2.3.1-1A: Mapping of network signalling label

Table 6.2.3.1-2: A-MPR for NS_100 (UTRA protection) (Power Class 3 and Power Class 2)

## 6.2.3.2A-MPR for NS_04

For NS_04, A-MPR is not added to MPR. Also, when NS_04 is signalled, MPR shall be set to zero in the PCMAX equations to avoid double counting MPR.

For power Class 1.5, 2 and 3, allowed maximum power reduction is defined as A-MPR = max(MPR, A-MPR'),

Note that A-MPR' = 0 dB means only MPR is applied,

where A-MPR' is defined as

if RBstart ≤ fstart,max,IMD3 / (12SCS) and LCRB ≤ AWmax,IMD3 / (12SCS) and FC - BWChannel/2 < FUL_low + offsetIMD3,then

the A-MPR' is defined according to Table 6.2.3.2-2 PC3_A2 relative to 23 dBm for power class 3,  PC2_A4 relative to 26 dBm for power class 2, and PC1.5_A6 relative to 29 dBm for power class 1.5,

else,

if RBstart ≤ LCRB/2 + start / (12SCS) and LCRB ≤ AWmax,regrowth / (12SCS) and FC - BWChannel/2 < FUL_low + offsetregrowth,then

the A-MPR' is defined according to Table 6.2.3.2-2 PC3_A1 relative to 23 dBm for power class 3,  PC2_A3 relative to 26 dBm for power class 2, , and PC1.5_A5 relative to 29 dBm for power class 1.5,

else

A-MPR' = 0 dB and apply MPR.

With the parameters defined in Table 6.2.3.2-1.

Table 6.2.3.2-1: Parameters for region edges and frequency offsets (Power Class 1.5, 2 and 3)

Table 6.2.3.2-2: A-MPR' values Access (Power Class 1.5, 2 and 3)

For Power Class 1, NS_04 A-MPR is defined as A-MPR = max(MPR, A-MPRregrowth, A-MPRIMD3, A-MPRCIM3, A-MPRedge).

A-MPRregrowth is obtained from Table 6.2.3.2-3 in terms of total guard bandwidth (TGBW). The TGBW is defined as the frequency distance between the RB allocation and the additional spurious emission limit defined in Table 6.5.3.3.1-1, i.e.,

,TGBW=falloc,low-2496 MHz

where

falloc,low=FC-BWChannel2+BWGB+RBstart∙12 SCS

is the lower edge frequency of the RB allocation,  is the channel centre frequency,  is the channel bandwidth, and  is the minimum guard bandwidth defined in Table 5.3.3-1. FCBWChannelBWGB

Table 6.2.3.2-3: A-MPRregrowth for NS_04 (Power Class 1)

Each function  defines the required minimum total guard bandwidth for A-MPR value  and is defined asGA(BWalloc)A

,GA(BWalloc)=max⁡(0,  C2BWalloc100MHz2+C1BWalloc100MHz+C0)

where  is the allocation bandwidth, and , , and  are obtained from Table 6.2.3.2-4 for each combination of waveform, modulation, and back-off value . BWalloc=LCRB∙12 SCSC2C1C0A

Table 6.2.3.2-4: Polynomial coefficients for determining the required total guard bandwidth for each value of A-MPRregrowth (Power Class 1)

For both OFDM and DFT-S-OFDM, A-MPRIMD3 =  if  ; otherwise, A-MPRIMD3 = 0 dB.max0,  min3,  4-2.77 BWalloc1 MHz dB3falloc,low-2FC  2490.5 MHz

For OFDM, A-MPRCIM3 =  dB if  ; otherwise, A-MPRCIM3 = 0.max0,  min11,  12-2 BWalloc1 MHz4 FC-3 falloc,high   2490.5 MHz

For DFT-S-OFDM, A-MPRCIM3 = 3 dB if  and ; otherwise, A-MPRCIM3 = 0.BWalloc 1.08 MHz4 FC-3 falloc,high   2490.5 MHz

Here,  is the upper edge frequency of the RB allocation.falloc,high=falloc,low+BWalloc

For both OFDM and DFT-S-OFDM, if , ,  and , A-MPRedge is defined in Table 6.2.3.2-5. Otherwise, A-MPRedge = 0 dB.RBstart=0LCRB=1FC-BWChannel2-2496 MHz<360 kHz

Table 6.2.3.2-5: A-MPRedge for NS_04 (Power Class 1)

## 6.2.3.3A-MPR for NS_10

Table 6.2.3.3-1: A-MPR for NS_10

## 6.2.3.4A-MPR for NS_05 and NS_05U

Table 6.2.3.4-1: A-MPR regions for NS_05 and NS_05U (Power Class 3)

Table 6.2.3.4-2: A-MPR for NS_05 and NS_05U (Power Class 3)

Table 6.2.3.4-3: Void

Table 6.2.3.4-4 - Table 6.2.3.4-9: Void

Table 6.2.3.4-10: Void

Table 6.2.3.4-11: A-MPR regions for NS_05 and NS_05U (Power Class 2)

Table 6.2.3.4-12: A-MPR for NS_05 and NS_05U (Power Class 2)

Table 6.2.3.4-13: Void

## 6.2.3.5A-MPR for NS_40

Table 6.2.3.5-1: A-MPR for NS_40

## 6.2.3.6A-MPR for NS_43 and NS_43U

Table 6.2.3.6-1: A-MPR regions for NS_43 (Power class 3 and 2)

Table 6.2.3.6-2: A-MPR for NS_43 (Power class 3)

Table 6.2.3.6-2a: A-MPR for NS_43 (Power Class 2)

Table 6.2.3.6-3: Void

For power class 3 operation, when NS_43U is signalled for 5 and 10 MHz channel bandwidths A-MPR is defined in Table 6.2.3.1-2 except for DFT-s-OFDM QPSK when LCRB > 5.4 MHz/12/SCS the A-MPR is 2.5 dB. For 15 MHz channel bandwidth Table 6.2.3.6-4 applies.

Table 6.2.3.6-4: A-MPR for NS_43U

For power class 2 operation, when NS_43U is signalled, the larger one between the PC2 A-MPR for NS_100 defined in Table 6.2.3.1-2 and the PC2 A-MPR for NS_43 defined in this clause applies.

## 6.2.3.7A-MPR for NS_03 and NS_03U

Table 6.2.3.7-1 A-MPR for NS_03

In case UE operates in a band where NS_03U applies and it receives additionalSpectrumEmission value of 3 then A-MPR values specified in Table 6.2.3.7-1 apply with an exception that DFT-s-OFDM Pi/2 BPSK A-MPR is 2 dB.

When power class 2 UE receives network signalling NS_03, A-MPR values specified in Table 6.2.3.7-1 apply.

## 6.2.3.8A-MPR for NS_37

Table 6.2.3.8-1: A-MPR regions for B11/B21 protection (NS_37) (1447.9 - 1462.9 MHz)

Table 6.2.3.8-2: A-MPR for NS_37

## 6.2.3.9A-MPR for NS_38

Table 6.2.3.9-1: A-MPR for EESS (NS_38) Protection (1430 – 1470 MHz)

## 6.2.3.10A-MPR for NS_39

Table 6.2.3.10-1: A-MPR for own RX (NS_39) Protection (1440 – 1470 MHz)

## 6.2.3.11A-MPR for NS_41

Table 6.2.3.11-1: A-MPR for NS_41

## 6.2.3.12A-MPR for NS_42

Table 6.2.3.12-1: A-MPR for NS_42

## 6.2.3.13A-MPR for NS_18

Table 6.2.3.13-0: A-MPR regions for NS_18 (power class 3)

Table 6.2.3.13-1: A-MPR for NS_18 (power class 3)

Table 6.2.3.13-2: A-MPR regions for NS_18 (power class 2)

Table 6.2.3.13-3: A-MPR for NS_18 for 1Tx and 2Tx (power class 2)

## 6.2.3.14A-MPR for NS_21

Table 6.2.3.14-1: A-MPR for "NS_21"

Table 6.2.3.14-2: A-MPR for "NS_21"

## 6.2.3.15A-MPR for NS_24

Table 6.2.3.15-1: A-MPR for NS_24

Table 6.2.3.15-2: A-MPR for modulation and waveform type

## 6.2.3.16A-MPR for NS_27

Table 6.2.3.16-1: A-MPR for NS_27

Table 6.2.3.16-2: A-MPR for modulation and waveform type

## 6.2.3.17A-MPR for NS_46

Table 6.2.3.17-1: A-MPR regions for NS_46 (Power class 3)

Table 6.2.3.17-2: A-MPR for NS_46 (Power class 3)

Table 6.2.3.17-3: A-MPR regions for NS_46 (Power class 1)

Table 6.2.3.17-4: A-MPR for NS_46 (Power class 1)

Table 6.2.3.17-5: A-MPR regions for NS_46 (power class 2)

Table 6.2.3.17-6: A-MPR for NS_46 (power class 2)

## 6.2.3.18A-MPR for NS_47

Table 6.2.3.18-1: A-MPR regions and types for NS_47 (Power Class 2 and 3)

Table 6.2.3.18-2: A-MPR for modulation and waveform type (Power Class 2 and 3)

Table 6.2.3.18-3: A-MPR regions and types for NS_47 (Power Class 1.5)

Table 6.2.3.18-4: A-MPR for NS_47 (Power Class 1.5)

## 6.2.3.19A-MPR for NS_50

Table 6.2.3.19-1: A-MPR regions for NS_50 (Power Class 3)

Table 6.2.3.19-2: A-MPR for NS_50 (Power Class 3)

Table 6.2.3.19-3: A-MPR regions for NS_50 (Power Class 2)

Table 6.2.3.19-4: A-MPR for NS_50 (Power Class 2)

Table 6.2.3.19-5: A-MPR regions for NS_50 (Power Class 1.5)

Table 6.2.3.19-6: A-MPR for NS_50 (Power Class 1.5)

## 6.2.3.20A-MPR for NS_44

Table 6.2.3.20-1: A-MPR regions for NS_44

Table 6.2.3.20-2: A-MPR for NS_44

## 6.2.3.21A-MPR for NS_12

Table 6.2.3.21-1: A-MPR regions for NS_12 (Power Class 3)

Table 6.2.3.21-2: A-MPR for NS_12 (Power Class 3)

Table 6.2.3.21-3: A-MPR regions for NS_12 (Power Class 2)

Table 6.2.3.21-4: A-MPR for NS_12 (Power Class 2)

## 6.2.3.22A-MPR for NS_13

Table 6.2.3.22-1: A-MPR regions for NS_13 (Power Class 3)

Table 6.2.3.22-2: A-MPR for NS_13 (Power Class 3)

Table 6.2.3.22-3: A-MPR regions for NS_13 (Power Class 2)

Table 6.2.3.22-4: A-MPR for NS_13 (Power Class 2)

## 6.2.3.23A-MPR for NS_14

Table 6.2.3.23-1: A-MPR regions for NS_14 (Power Class 3)

Table 6.2.3.23-2: A-MPR for NS_14 (Power Class 3)

Table 6.2.3.23-3: A-MPR regions for NS_14 (Power Class 2)

Table 6.2.3.23-4: A-MPR for NS_14 (Power Class 2)

## 6.2.3.24A-MPR for NS_15

Table 6.2.3.24-1: A-MPR regions for NS_15 (Power Class 3)

Table 6.2.3.24-2: A-MPR for NS_15 (Power Class 3)

Table 6.2.3.24-3: A-MPR regions for NS_15 (Power Class 2)

## 6.2.3.25A-MPR for NS_45

Table 6.2.3.25-1: A-MPR for NS_45

## 6.2.3.26A-MPR for NS_48

Table 6.2.3.26-1: A-MPR regions for NS_48 (Power Class 3)

Table 6.2.3.26-2: A-MPR for NS_48 (Power Class 3)

Table 6.2.3.26-3: A-MPR regions for NS_48 (Power Class 2)

Table 6.2.3.26-4: A-MPR for NS_48 (Power Class 2)

## 6.2.3.27A-MPR for NS_49

Table 6.2.3.27-1: A-MPR regions for NS_49 (Power Class 3)

Table 6.2.3.27-2: A-MPR for NS_49 (Power Class 3)

Table 6.2.3.27-3: A-MPR regions for NS_49 (Power Class 2)

Table 6.2.3.27-4: A-MPR for NS_49 (Power Class 2)

## 6.2.3.28A-MPR for NS_51

Table 6.2.3.28-1: A-MPR regions for NS_51

Table 6.2.3.28-2: A-MPR for NS_51

## 6.2.3.29A-MPR for NS_07

Table 6.2.3.29-1: A-MPR regions for NS_07 (Power class 3)

Table 6.2.3.29-2: A-MPR for NS_07 (Power class 3)

Table 6.2.3.29-3: A-MPR regions for NS_07 (Power class 2)

Table 6.2.3.29-4: A-MPR for NS_07 (Power class 2)

## 6.2.3.30A-MPR for NS_56

For 5 MHz channel centered on frequencies (FC) = 1630.0, 1630.3 MHz, A-MPR is defined as

if RBstart <= ceil{3/SCS/15 kHz)}and LCRB <= ceil{17/SCS/15 kHz)},

then

the A-MPR = 14 dB for SCS = 15 kHz and AMPR = 8 dB for SCS >= 30 kHz,

else,

if RBstart <= ceil{3/(SCS/15 kHz)} and LCRB > ceil{17/(SCS/15 kHz)},

then

the A-MPR = 6 dB,

else,

if RBstart <= ceil{8/(SCS/15 kHz)},

then

the A-MPR = 4 dB.

For 5 MHz channel centered on frequencies (Fc) = 1635.0, 1649.0, 1654.0 MHz, no A-MPR is needed.

For Channel 10 MHz with center frequency of 1632.5 MHz, A-MPR is defined as

if RBstart < ceil{3/(SCS/15 kHz)} and LCRB <= ceil{8/(SCS/15 kHz)},

then

the A-MPR = 12 dB for SCS = 15 kHz and AMPR = 8 dB for SCS >= 30 kHz,

else,

if RBstart < ceil{9/(SCS/15 kHz)}, and LCRB > ceil{8/(SCS/15 kHz)},

then

the A-MPR = 8 dB,

else,

if RBstart <= ceil{18/(SCS/15 kHz)},

then

the A-MPR = 6 dB,

else,

if RBstart >= floor{40/(SCS/15 kHz)}], and LCRB <= ceil{7/(SCS/15 kHz)},

then

the A-MPR = 5 dB,

else,

if RBstart >= floor{40/(SCS/15 kHz)} and LCRB > ceil{7/(SCS/15 kHz)},

then

the A-MPR = 3 dB,

else,

if RBstart >= floor{35/(SCS/15 kHz)} and LCRB <= ceil{7/(SCS/15 kHz)},

then

the A-MPR = 4 dB,

else,

if RBstart >= floor{35/(SCS/15 kHz)} and LCRB > ceil{7/(SCS/15 kHz)},

then

the A-MPR = 2 dB.

For 10 MHz channel centered on frequency of 1651.5 MHz, no A-MPR is needed.

## 6.2.3.31A-MPR for NS_35

For power class 1 operation A-MPR = 8.5 dB if

( LCRB ≤ 0.20 ∙ NRB and ( RBstart = 0 or RBstart + LCRB = NRB ) )

or

( LCRB = 1 and 5 ∙ | RBstart + 0.5 – NRB / 2 | ∙ 12 ∙ SCS ≥ 1.5 ∙ CBW + 5 MHz ).

[For power class 2 operation A-MPR = 3dB  for DFT-s-OFDM and A-MPR = 4.5dB for and CP-OFDM if

( LCRB ≤ 0.20 ∙ NRB and ( RBstart = 0 or RBstart + LCRB = NRB ) )

or

( LCRB = 1 and 5 ∙ | RBstart + 0.5 – NRB / 2 | ∙ 12 ∙ SCS ≥ 1.5 ∙ CBW + 5 MHz ).]

## 6.2.3.32A-MPR for NS_06

For power class 3 operation on bands n12, n13, n14, n85 and n110, no A-MPR is applicable.

For power class 1 operation on band n14, no A-MPR is applicable.

For power class 1 operation on band n85 A-MPR = 8.5 dB if

( LCRB ≤ 0.20 ∙ NRB and ( RBstart = 0 or RBstart + LCRB = NRB ) )

or

( LCRB = 1 and 5 ∙ | RBstart + 0.5 – NRB / 2 | ∙ 12 ∙ SCS ≥ 1.5 ∙ CBW + 5 MHz ).

For power class 2 operation on bands n13, n14 and n85, the PC2 A-MPR requirements for NS_06 are defined below in Table 6.2.3.32-1.

Table 6.2.3.32-1: A-MPR for NS_06 (Power Class 2)

## 6.2.3.33A-MPR for NS_17

Table 6.2.3.33-1: A-MPR regions for NS_17 (power class 2)

Table 6.2.3.33-2: A-MPR for NS_17 for 1Tx and 2Tx (power class 2)

## 6.2.3.34A-MPR for NS_26

Table 6.2.3.34-1: A-MPR regions for "NS_26"

Table 6.2.3.34-2: A-MPR for NS_26

## 6.2.3.35A-MPR for NS_36

Table 6.2.3.35-1: A-MPR regions for "NS_36"

Table 6.2.3.35-2: A-MPR for NS_36

## 6.2.4Configured transmitted power

The UE is allowed to set its configured maximum output power PCMAX,f,c for carrier f of serving cell c in each slot. The configured maximum output power PCMAX,f,c is set within the following bounds:

PCMAX_L,f,c ≤  PCMAX,f,c  ≤  PCMAX_H,f,c with

PCMAX_L,f,c = MIN {PEMAX,c– ∆TC,c,  (PPowerClass – ΔPPowerClass + ΔPPowerBoost) – MAX(MAX(MPRc+∆MPRc, A-MPRc)+ ΔTIB,c + ∆TC,c + ∆TRxSRS, P-MPRc) }

PCMAX_H,f,c = MIN {PEMAX,c,  PPowerClass – ΔPPowerClass + ΔPPowerBoost}

where

PEMAX,c is the value given by either the p-Max IE or the field additionalPmax of the NR-NS-PmaxList IE, whichever is applicable according to TS 38.331[7];

PPowerClass is the maximum UE power specified in Table 6.2.1-1 and in Table 6.2F.1-1 for shared spectrum access operation, without taking into account the tolerance specified in the Table 6.2.1-1 and in Table 6.2F.1-1 for shared spectrum access operation;

When  the IE powerBoostPi2BPSK is set to 1, PEMAX,c is increased by +3 dB for a power class 3 UE operating in TDD bands n40, n41, n77, n78, and n79 with PI/2 BPSK modulation with Rel-15 DMRS and UE indicates support for UE capability powerBoosting-pi2BPSK and 40% or less symbols in certain evaluation period are used for UL transmission when PEMAX,c ≥ 20 dBm (The exact evaluation period is no less than one radio frame).

When the IE powerBoostPi2BPSK is set to 1, ΔPPowerClass = -3 dB for a power class 3 UE operating in TDD bands n40, n41, n77, n78, and n79 with Pi/2 BPSK modulation with Rel-15 DMRS and UE indicates support for UE capability powerBoosting-pi2BPSK and 40% or less slots in radio frame are used for UL transmission.

ΔPPowerClass =

-3 dB for a power class 2 UE or 6 dB for a power class 1.5 UE when P-max of 23 dBm or lower is indicated; or when the field of UE capability maxUplinkDutyCycle-PC2-FR1 is absent and the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than 50%; or when the field of UE capability maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or when the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is not absent and half the percentage of uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-PC1dot5-MPE-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame).

-3 dB for a power class 1.5 UE when P-max of between 23 dBm and 26 dB is indicated; or when the field of UE capability maxUplinkDutyCycle-PC2-FR1 is absent and the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is absent and the percentage of uplink symbols transmitted in a certain evaluation period is between 25% and 50%; or when the field of UE capability maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of uplink symbols transmitted in a certain evaluation period is between maxUplinkDutyCycle-PC2-FR1 and maxUplinkDutyCycle-PC2-FR1/2 and 0.5*maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or when the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is not absent and the percentage of uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-PC1dot5-MPE-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame).

-3dB when the UE is configured with SUL configurations and the requirements of default power class are applied as specified in sub-clause 6.2C.1 on the band where UE indicates power class 2;

-3dB is applied during SRS transmission occasions with usage in SRS-ResourceSet set as ‘antennaSwitching’ with configured SRS resources in each SRS resource set(s) consisting of one SRS port when PC2 UE with txDiversity-r16 or txDiversity2Tx-r18 capability or PC1.5 UE further indicates SRS-TxSwitch capability ‘t1r2’ or ‘t1r4’ or ‘t1r1-t1r2’ or ‘t1r1-t1r2-t1r4’ or further indicates srs-AntennaSwitchingBeyond4RX-r17 as ‘t1r6’ or ‘t1r8’;

-0 dB otherwise;

NOTE:UE reports ∆PPowerClass when deltaPowerClassReporting-r18 is present, dpc-Reporting-FR1 [7] is configured and the reporting is triggered only by uplink duty cycle exceedance or by return to the ue-PowerClass after the duty cycle exceedance.

∆TIB,c is the additional tolerance for serving cell c as specified in clause 6.2A.4.2 for NR CA, clause 6.2C.2 for SUL, or TS 38.101-3 clause  6.2B.4.2 for EN-DC; ∆TIB,c = 0 dB otherwise; In case the UE supports more than one of band combinations for V2X operating bands for concurrent operation, CA, SUL or DC, and an operating band belongs to more than one band combinations then

a)When the operating band frequency range is ≤ 1 GHz, the applicable additional ∆TIB,c shall be the average value for all band combinations defined in clause 6.2A.4.2, 6.2C.2 in this specification and 6.2B.4.2 in TS 38.101-3 [3], truncated to one decimal place that apply for that operating band among the supported band combinations. In case there is a harmonic relation between low band UL and high band DL, then the maximum ∆TIB,c among the different supported band combinations involving such band shall be applied

b)When the operating band frequency range is > 1 GHz, the applicable additional ∆TIB,c shall be the maximum value for all band combinations defined in clause 6.2A.4.2, 6.2C.2 in this specification and 6.2B.4.2 in TS 38.101-3 [3] for the applicable operating bands.

ΔPPowerBoost is defined as 1dB for power class 3 and 0.5dB for power class 2, when all of the following conditions are met:

-If the UE indicates support for UE capability powerBoosting-pi2BPSK-QPSK-r18 and/or powerBoosting-pi2BPSK-QPSK-Modified-r18, and if IE powerBoostPi2BPSK-r18 and/or powerBoostQPSK-r18 is set to 1 and PEMAX,c, if configured, is increased by at least ΔPPowerBoost

-If UE indicates power class 2 in a TDD band or power class 3

-IfΔPPowerClass is 0dB

-If scheduled UL transmission is DFT-s-OFDM with either PI/2 BPSK modulation (with either Rel-15 DMRS or with pi/2 BPSK DMRS) or QPSK modulation

-If the RB allocation belongs to the inner region defined in clause 6.2.2.

-If UE indicates power class 3, the percentage of uplink symbols transmitted in a certain evaluation period is less than 80%

-If UE indicates power class 2, when the field of UE capability maxUplinkDutyCycle-PC2-FR1 is absent and the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is absent and the percentage of uplink symbols transmitted in a certain evaluation period is less than 0.9*50%; or when the field of UE capability maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of uplink symbols transmitted in a certain evaluation period is less than 0.9*maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or when the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is not absent and half the percentage of uplink symbols transmitted in a certain evaluation period is less than 0.9*maxUplinkDutyCycle-PC1dot5-MPE-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame)

-0 dB otherwise;

∆TC,c = 1.5dB when NOTE 3 in Table 6.2.1-1 in 38.101-1 applies for a serving cell c, otherwise ∆TC,c = 0 dB ;

MPRc and A-MPRc for serving cell c are specified in clause 6.2.2 and clause 6.2.3, respectively and in clause 6.2F.2 and clause 6.2F.3 respectively for shared spectrum access operation;

∆MPRc for serving cell c is specified in clause 6.2.2 and in clause 6.2F.2 for shared spectrum access operation.

∆TRxSRS is applied during SRS transmission occasions with usage in SRS-ResourceSet set as ‘antennaSwitching’ when

a)UE transmits SRS on the second SRS resource in every configured SRS resource set when the SRS-TxSwitch capability is indicated as 't1r2' or 't1r1-t1r2'

b)UE transmits SRS on the second, third and fourth SRS resources of the total 4 SRS resources from all configured SRS resource set(s) consisting of one SRS port when the SRS-TxSwitch capability is indicated as 't1r4' or, 't1r4-t2r4' or 't1r1-t1r2-t1r4' or, 't1r1-t1r2-t2r2-t1r4-t2r4'

c)UE transmits SRS from the SRS port pair on the second SRS resource in every configured SRS resource set consisting of two SRS ports when the SRS-TxSwitch capability is indicated as ' t2r4' or ' t1r4-t2r4', or 't1r1-t1r2-t2r2-t2r4' or 't1r1-t1r2-t2r2-t1r4-t2r4', or

d)UE transmits SRS to a DL-only carrier

e)UE transmits SRS on the second, third, fourth, fifth, sixth, seventh and eighth SRS resources of the total 8 SRS resources from all configured SRS resource set(s) consisting of one SRS port when the srs-AntennaSwitchingBeyond4RX-r17 capability is indicated as at least 't1r8', or

f)UE transmits SRS from the SRS port pair on the second, third and fourth SRS resource in every configured SRS resource set consisting of two SRS ports when the srs-AntennaSwitchingBeyond4RX-r17 capability is indicated as at least 't2r8', or

g)UE transmits SRS from the set of SRS ports on the second SRS resource in every configured SRS resource set consisting of four SRS ports when the srs-AntennaSwitchingBeyond4RX-r17 capability is indicated as at least 't4r8',

h)UE transmits SRS on the second, third, fourth, fifth and sixth SRS resources of the total 6 SRS resources from all configured SRS resource set(s) consisting of one SRS port when the srs-AntennaSwitchingBeyond4Rx-r17 capability is indicated as at least ‘t1r6’, or

i)UE transmits SRS from the SRS port pair on the second and third SRS resource in every configured SRS resource set consisting of two SRS ports when the srs-AntennaSwitchingBeyond4RX-r17 capability is indicated as at least ‘t2r6’, or

j)UE transmits SRS from the set of SRS ports on the second SRS resource in every configured SRS resource set consisting of four SRS ports and when fourPortSRS-3Tx capability is indicated and srs-AntennaSwitching3T6R-r19 capability is indicated as ‘t3r6’.

The following ∆TRxSRS applies according to the indicated SRS-TxSwitch or srs-AntennaSwitchingBeyond4RX-r17 or both srs-AntennaSwitchingBeyond4RX-r17 and srs-AntennaSwitching3T6R-r19 capabilities:

if 't1r8' and 't4r8' are indicated:

-The value of ∆TRxSRS is 7.3 dB for bands whose FUL_high is higher than the FUL_low of n79 and 5.8 dB for bands whose FUL_high is lower than the FUL_low of n79 when the device is power class 3 or power class 5 or power class 1.5 in the band, or when the device is power class 2 in the band and ΔPPowerClass = 3 dB, or when UE indicating Tx diversity capability.

-The value of ∆TRxSRS is 10.3 dB for bands whose FUL_high is higher than the FUL_low of n79 and 8.8 dB for bands whose FUL_high is lower than the FUL_low of n79 during SRS transmission occasions with configured SRS resources consisting of one SRS port when the device is power class 2 in the band and ΔPPowerClass = 0 dB and not indicating Tx diversity capability.

else, if 't1r8' and 't2r8' are indicated:

-The value of ∆TRxSRS is 6.0 dB for bands whose FUL_high is higher than the FUL_low of n79 and 4.5 dB for bands whose FUL_high is lower than the FUL_low of n79 when the device is power class 3 or power class 5 or power class 1.5 in the band, or when the device is power class 2 in the band and ΔPPowerClass = 3 dB, or when UE indicating txDiversity-r16.

-The value of ∆TRxSRS is 9.0 dB for bands whose FUL_high is higher than the FUL_low of n79 and 7.5 dB for bands whose FUL_high is lower than the FUL_low of n79 during SRS transmission occasions with configured SRS resources consisting of one SRS port when the device is power class 2 in the band and ΔPPowerClass = 0 dB and not indicating Tx diversity capability.

else, if 't1r8' or 't2r8', but not both is indicated:

-The value of ∆TRxSRS is 5.5 dB for bands whose FUL_high is higher than the FUL_low of n79 and 4.0 dB for bands whose FUL_high is lower than the FUL_low of n79 when the device is power class 3 or power class 5 or power class 1.5 in the band, or when the device is power class 2 in the band and ΔPPowerClass = 3 dB, or when UE indicating Tx diversity capability.

-The value of ∆TRxSRS is 8.5 dB for bands whose FUL_high is higher than the FUL_low of n79 and 7.0 dB for bands whose FUL_high is lower than the FUL_low of n79 during SRS transmission occasions with configured SRS resources consisting of one SRS port when the device is power class 2 in the band and ΔPPowerClass = 0 dB and not indicating Tx diversity capability.

else, if 't1r2', 't1r1-t1r2', 't1r4', 't1r4-t2r4', 't1r1-t1r2-t1r4', 't2r4', 't1r1-t1r2-t2r2-t2r4', 't1r1-t1r2-t2r2-t1r4-t2r4' or 't4r8' is indicated:

-The value of ∆TRxSRS is 4.5dB for bands whose FUL_high is higher than the FUL_low of n79 and 3 dB for bands whose FUL_high is lower than the FUL_low of n79 when the device is power class 3 or power class 5 or power class 1.5 in the band, or when the device is power class 2 in the band and ΔPPowerClass = 3 dB, or when UE indicating Tx diversity capability.

-The value of ∆TRxSRS is 7.5dB for bands whose FUL_high is higher than the FUL_low of n79 and 6 dB for bands whose FUL_high is lower than the FUL_low of n79 during SRS transmission occasions with configured SRS resources consisting of one SRS port when the device is power class 2 in the band and ΔPPowerClass = 0 dB and not indicating Tx diversity capability.

else, if ‘t1r6’ and ‘t2r6’ and ‘t3r6’ are all indicated:

-The value of ∆TRxSRS is 8.0 dB for bands whose FUL_high is higher than the FUL_low of n104 and 7.0 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 5.5 dB for bands whose FUL_high is lower than the FUL_low of n79 when the device is power class 3 or power class 5 in the band, or when the device is power class 2 in the band and ΔPPowerClass = 3 dB, or when UE indicating Tx diversity capability.

-The value of ∆TRxSRS is 11.0 dB for bands whose FUL_high is higher than the FUL_low of n104 and 10.0 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 8.5 dB for bands whose FUL_high is lower than the FUL_low of n79 during SRS transmission occasions with configured SRS resources consisting of one SRS port when the device is power class 2 in the band and ΔPPowerClass = 0 dB and not indicating Tx diversity capability.

else, if ‘t1r6’ and ‘t2r6’ are indicated:

-The value of ∆TRxSRS is 7.0 dB for bands whose FUL_high is higher than the FUL_low of n104 and 6.0 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 4.5 dB for bands whose FUL_high is lower than the FUL_low of n79 when the device is power class 3 or power class 5 or power class 1.5 in the band, or when the device is power class 2 in the band and ΔPPowerClass = 3 dB, or when UE indicating Tx diversity capability.

-The value of ∆TRxSRS is 10.0 dB for bands whose FUL_high is higher than the FUL_low of n104 and 9.0 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 7.5 dB for bands whose FUL_high is lower than the FUL_low of n79 during SRS transmission occasions with configured SRS resources consisting of one SRS port when the device is power class 2 in the band and ΔPPowerClass = 0 dB and not indicating Tx diversity capability.

else, if ‘t1r6’ and ‘t3r6’ are indicated:

-The value of ∆TRxSRS is 7.0 dB for bands whose FUL_high is higher than the FUL_low of n104 and 6.0 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 4.5 dB for bands whose FUL_high is lower than the FUL_low of n79 when the device is power class 3 or power class 5 in the band, or when the device is power class 2 in the band and ΔPPowerClass = 3 dB, or when UE indicating Tx diversity capability.

-The value of ∆TRxSRS is 10.0 dB for bands whose FUL_high is higher than the FUL_low of n104 and 9.0 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 7.5 dB for bands whose FUL_high is lower than the FUL_low of n79 during SRS transmission occasions with configured SRS resources consisting of one SRS port when the device is power class 2 in the band and ΔPPowerClass = 0 dB and not indicating Tx diversity capability.

else, if ‘t2r6’ and ‘t3r6’ are indicated:

-The value of ∆TRxSRS is 6.0 dB for bands whose FUL_high is higher than the FUL_low of n104 and 5.5 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 4.0 dB for bands whose FUL_high is lower than the FUL_low of n79 when the device is power class 3 or power class 5 in the band, or when the device is power class 2 in the band and ΔPPowerClass = 3 dB, or when UE indicating Tx diversity capability.

-The value of ∆TRxSRS is 9.0 dB for bands whose FUL_high is higher than the FUL_low of n104 and 8.5 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 7.0 dB for bands whose FUL_high is lower than the FUL_low of n79 during SRS transmission occasions with configured SRS resources consisting of one SRS port when the device is power class 2 in the band and ΔPPowerClass = 0 dB and not indicating Tx diversity capability.

else, if ‘t3r6’ is indicated:

-The value of ∆TRxSRS is 5.0 dB for bands whose FUL_high is higher than the FUL_low of n104 and 4.5 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 3.0 dB for bands whose FUL_high is lower than the FUL_low of n79 when the device is power class 3 or power class 5 in the band, or when the device is power class 2 in the band and ΔPPowerClass = 3 dB, or when UE indicating Tx diversity capability.

-The value of ∆TRxSRS is 8.0 dB for bands whose FUL_high is higher than the FUL_low of n104 and 7.5 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 6.0 dB for bands whose FUL_high is lower than the FUL_low of n79 during SRS transmission occasions with configured SRS resources consisting of one SRS port when the device is power class 2 in the band and ΔPPowerClass = 0 dB and not indicating Tx diversity capability.

else, if ‘t2r6’ is indicated:

-The value of ∆TRxSRS is 5.5 dB for bands whose FUL_high is higher than the FUL_low of n104 and 5.0 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 3.5 dB for bands whose FUL_high is lower than the FUL_low of n79 when the device is power class 3 or power class 5 or power class 1.5 in the band, or when the device is power class 2 in the band and ΔPPowerClass = 3 dB, or when UE indicatingTx diversity capability.

-The value of ∆TRxSRS is 8.5 dB for bands whose FUL_high is higher than the FUL_low of n104 and 8.0 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 6.5 dB for bands whose FUL_high is lower than the FUL_low of n79 during SRS transmission occasions with configured SRS resources consisting of one SRS port when the device is power class 2 in the band and ΔPPowerClass = 0 dB and not indicating Tx diversity capability.

else, if ‘t1r6’ is indicated:

-The value of ∆TRxSRS is 6.5 dB for bands whose FUL_high is higher than the FUL_low of n104 and 5.5 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 4.0 dB for bands whose FUL_high is lower than the FUL_low of n79 when the device is power class 3 or power class 5 or power class 1.5 in the band, or when the device is power class 2 in the band and ΔPPowerClass = 3 dB, or when UE indicatingTx diversity capability.

-The value of ∆TRxSRS is 9.5 dB for bands whose FUL_high is higher than the FUL_low of n104 and 8.5 dB for bands whose FUL_high is lower than the FUL_low of n104 and higher than the FUL_low of n79 and 7.0 dB for bands whose FUL_high is lower than the FUL_low of n79 during SRS transmission occasions with configured SRS resources consisting of one SRS port when the device is power class 2 in the band and ΔPPowerClass = 0 dB and not indicating Tx diversity capability.

For other SRS transmissions ∆TRxSRS is zero;

P-MPRc is the power management maximum power reduction for

a)ensuring compliance with applicable electromagnetic energy absorption requirements and addressing unwanted emissions / self desense requirements in case of simultaneous transmissions on multiple RAT(s) for scenarios not in scope of 3GPP RAN specifications;

b)ensuring compliance with applicable electromagnetic energy absorption requirements in case of proximity detection is used to address such requirements that require a lower maximum output power.

The UE shall apply P-MPRc for serving cell c only for the above cases. For UE conducted conformance testing P-MPRc shall be 0 dB

NOTE 1:P-MPRc was introduced in the PCMAX,f,c equation such that the UE can report to the gNB the available maximum output transmit power. This information can be used by the gNB for scheduling decisions.

NOTE 2:P-MPRc may impact the maximum uplink performance for the selected UL transmission path.

TREF and Teval are specified in Table 6.2.4-1. For each TREF, the PCMAX,L,c for serving cell c are evaluated per Teval and given by the minimum  value taken over the transmission(s) within the Teval; the minimum PCMAX_L,f,c over one or more Teval is then applied for the entire TREF

Table 6.2.4-1: Evaluation and reference periods for PCMAX

The measured configured maximum output power PUMAX,f,c shall be within the following bounds:

PCMAX_L,f,c  –  MAX{TL,c, T(PCMAX_L,f,c)}  ≤  PUMAX,f,c  ≤  PCMAX_H,f,c  +  T(PCMAX_H,f,c).

where the tolerance T(PCMAX,f,c) for applicable values of PCMAX,f,c is specified in Table 6.2.4-1. The tolerance TL,c is the absolute value of the lower tolerance for the applicable operating band as specified in Table 6.2.1-1 and in Table 6.2F.1-1 for shared spectrum access operation.

Table 6.2.4-1: PCMAX tolerance

## 6.2ATransmitter power for CA

## 6.2A.0General

As an exception, HPUE applicability notes in 5.5A do not restrict power class indication for single configured UL CC with DL CA. UE can indicate power class for the single configured UL CC with DL CA as specified in Table 6.2.1-1 and if UE supports UL MIMO in this carrier, UE can indicate power class for the CA configuration as specified in Table 6.2D.1-1.

## 6.2A.1UE maximum output power for CA

## 6.2A.1.1UE maximum output power for Intra-band contiguous CA

For uplink intra-band contiguous carrier aggregation, the maximum output power is specified in Table 6.2A.1.1-1. For downlink intra-band contiguous carrier aggregation with a single uplink component carrier configured in the NR band, the maximum output power is specified in Table 6.2.1-1 for power class 3 and other power classes if indicated in clause 5.5A.1.

Table 6.2A.1.1-1: UE Power Class for intra-band contiguous CA

If a UE supports power class 2 for the band combination listed in Table 6.2A.1.1-1 and the supported power class enables the higher maximum output power than that of the default power class:

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than 50% (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or

-if 10 log10 ∑ pEMAX,c or PEMAX,CA which defined in clause 6.2A.4.1.1 is 23dBm or lower;

-shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified in clause 6.2A.4.1.1;

-else

-shall apply all requirements for the supported power class and set the configured transmitted power as specified in clause 6.2A.4.1.1.

If a UE supports power class 1.5 for the band combination listed in Table 6.2A.1.1-1 and the supported power class enables the higher maximum output power than that of the power class 2:

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is absent and the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than 50% (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is not absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than 2*maxUplinkDutyCycle-PC1dot5-MPE-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or

-if 10 log10 ∑ pEMAX,c or PEMAX,CA which defined in 6.2A.4.1.1 is 23dBm or lower;

-shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as 6.2A.4.1.1.

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is absent and the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than 25% but less than or equal to 50% (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-PC2-FR1 but less than or equal to maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is not absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than maxUplinkDutyCycle-PC1dot5-MPE-FR1 but less than or equal to 2*maxUplinkDutyCycle-PC1dot5-MPE-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or

-if 10 log10 ∑ pEMAX,c or PEMAX,CA which defined in clause 6.2A.4.1.1 is between 23dBm and 26dBm;

-shall apply all requirements for the power class 2 to the supported power class and set the configured transmitted power as specified in clause 6.2A.4.1.1.

-else

-shall apply all requirements for the power class 1.5 to the supported power class and set the configured transmitted power as 6.2A.4.1.1.

## 6.2A.1.2UE maximum output power for Intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation with one uplink carrier on the PCC, the requirements in clause 6.2.1 apply for power class 3 and other power classes if indicated in clause 5.5A.2. For intra-band non-contiguous carrier aggregation with two uplink carriers the maximum output power is specified in Table 6.2A.1.2-1.

Table 6.2A.1.2-1: UE Power Class for intra-band non-contiguous CA

If a UE supports power class 2 for the band combination listed in Table 6.2A.1.2-1 and the supported power class enables the higher maximum output power than that of the default power class:

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than 50% (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or

-if 10 log10 ∑ pEMAX,c or PEMAX,CA which defined in clause 6.2A.4.1.2 is 23dBm or lower;

-shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified in clause 6.2A.4.1.2;

-else shall apply all requirements for the supported power class and set the configured transmitted power as specified in clause 6.2A.4.1.2.

If a UE supports power class 1.5 for the band combination listed in Table 6.2A.1.2-1 and the supported power class enables the higher maximum output power than that of the power class 2:

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is absent and the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than 50% (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is not absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than 2*maxUplinkDutyCycle-PC1dot5-MPE-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or

-if 10 log10 ∑ pEMAX,c or PEMAX,CA which defined in 6.2A.4.1.2 is 23dBm or lower;

-shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as 6.2A.4.1.2;

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is absent and the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than 25% but less than or equal to 50% (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC2-FR1 is not absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-PC2-FR1 but less than or equal to maxUplinkDutyCycle-PC2-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or

-if the field of UE capability maxUplinkDutyCycle-PC1dot5-MPE-FR1 is not absent and the percentage of total uplink symbols transmitted on all UL CCs in a certain evaluation period is larger than maxUplinkDutyCycle-PC1dot5-MPE-FR1 but less than or equal to 2*maxUplinkDutyCycle-PC1dot5-MPE-FR1 as defined in TS 38.306 (The exact evaluation period is no less than one radio frame); or

-if 10 log10 ∑ pEMAX,c or PEMAX,CA which defined in clause 6.2A.4.1.2 is between 23dBm and 26dBm;

-shall apply all requirements for the power class 2 to the supported power class and set the configured transmitted power as specified in clause 6.2A.4.1.2;

-else

-shall apply all requirements for the power class 1.5 to the supported power class and set the configured transmitted power as specified in clause 6.2A.4.1.2;

## 6.2A.1.3UE maximum output power for Inter-band CA

For inter-band downlink carrier aggregation with one uplink carrier assigned to one NR band, the transmitter power requirements in Table 6.2.1-1 apply for power class 3 and other power classes if indicated in clause 5.5A.3.

For inter-band carrier aggregation with two uplink contiguous carrier assigned to one NR band, the transmitter power requirements specified in subclause 6.2A.1.1 apply.

For inter-band carrier aggregation with two uplink non-contiguous carrier assigned to one NR band, the transmitter power requirements specified in subclause 6.2A.1.2 apply. For inter-band uplink carrier aggregation with uplink assigned to two NR bands, UE maximum output power shall be measured over all component carriers from different bands. If each band has separate antenna connectors, maximum output power is defined as the sum of maximum output power from each UE antenna connector. The period of measurement shall be at least one sub frame (1 ms). The two band UL CA maximum output power with one Tx per band is specified in Table 6.2A.1.3-1, and Table 6.2A.1.3-3 for FRMCS in bands n100 and n101. The per band power class for each band applicable to REFSENS exceptions for a given inter-band ULCA power class are specified in Table 6.2A.1.3-2. These configurations are subject to the applicable power class of each NR band as specified in Table 6.2.1-1. The power classes referenced are according to the reported ue-PowerClassPerBandPerBC-r17 if indicated or ue-PowerClass otherwise.

If higherPowerLimit-r17 is indicated for an UL inter-band CA configuration as specified in Table 6.2A.1.3-1 and with uplink bands of different power class capabilities, the UE maximum output power specified in Table 6.2A.1.3-1 for this UL CA configuration is modified in accordance with sub-clause 6.2A.4.1.3

Table 6.2A.1.3-1: UE Power Class for uplink inter-band CA (two bands)

Table 6.2A.1.3-2: Per band power class applicable to REFSENS exceptions (two bands UL CA with 1Tx in each band)

If a UE supports a different power class than the default UE power class for the band combination listed in Table 6.2A.1.3-1 and the supported power class enables the higher maximum output power than that of the default power class:

–if the field of UE capability maxUplinkDutyCycle-interBandCA-PC2 is not absent and the average percentage of uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-interBandCA-PC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

– if 10 log10 ∑ pEMAX,c or PEMAX,CA which defined in clause 6.2A.4.1.3 is 23dBm or lower;

–shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified in clause 6.2A.4.1.3;

–else if the field of UE capability maxUplinkDutyCycle-interBandCA-PC2 is not absent and the average percentage of uplink symbols transmitted in a certain evaluation period is larger than 0.5*maxUplinkDutyCycle-interBandCA-PC2 as defined in TS 38. 306 (The exact evaluation period is no less than one radio frame); or

–if 10 log10 ∑ pEMAX,c or PEMAX,CA which defined in clause 6.2A.4.1.3 is 26dBm or lower;

–shall apply all requirements for the power class 2 to the supported power class and set the configured transmitted power as specified in clause 6.2A.4.1.3;

–else;

–shall apply all requirements for the supported power class and set the configured transmitted power as specified in clause 6.2A.4.1.3 (regardless of the average percentage of uplink symbols if the field of UE capability maxUplinkDutyCycle-interBandCA-PC2 is absent).

The average percentage of uplink symbols is defined as 50%  (DutyNR, x /maxDutyNR,x + DutyNR, y /maxDutyNR,y, ). DutyNR, x, DutyNR, y represent the actual percentage of uplink symbols transmitted in the same evaluation period (The exact evaluation period is no less than one radio frame) for NR Band x, NR Band y respectively; maxDutyNR,x, maxDutyNR,y represent the field of UE capability maxUplinkDutyCycle-PC2-FR1 per band as defined in TS 38.331.  For NR Band x or NR Band y,

–if power class of one or both of the bands within the band combination is power class 2 and the corresponding UE capability maxUplinkDutyCycle-PC2-FR1 is absent;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 50%;

–if the IE P-Max as defined in TS 38.331 [7] is provided for one of the bands and set to 23 dBm or lower or UE indicates power class 3 for one of the bands;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 100%.

–else if power class of one or both of the bands within the band combination is power class 2 and the corresponding UE capability maxUplinkDutyCycle-PC2-FR1 is absent;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 50%;

Table 6.2A.1.3-2 Void

Table 6.2A.1.3-3: UE Power Class for uplink inter-band CA (two bands) for FRMCS in bands n100 and n101

## 6.2A.1.4Void

## 6.2A.1.5Void

## 6.2A.2UE maximum output power reduction for CA

## 6.2A.2.1UE maximum output power reduction for Intra-band contiguous CA

For intra-band contiguous carrier aggregation the allowed Maximum Power Reduction (MPR) for the maximum output power in 6.2A.1.1-1 with contiguous RB allocation is specified in Table 6.2A.2.1-1 for UE power class 3 CA bandwidth classes B and C. The MPR with contiguous RB allocation is specified in Table 6.2A.2.1-1a for power class 2 CA bandwidth classes B and C when the signalling is absent for dualPA-Architecture IE, and for power class 2 CA bandwidth class C when the signalling is indicated for dualPA-Architecture IE. The MPR with contiguous RB allocation is specified in Table 6.2A.2.1-1b for power class 2 CA bandwidth classes B and C with TxD supported. The MPR with contiguous RB allocation is specified in Table 6.2A.2.1-1c and 6.2A.2.1-1d for 2Tx power class 1.5 CA bandwidth class C for hand-held UE and large FWA form factor respectively.

For UE indicating mpr-ActiveCarrierEnh-r19 supported and if single CC is activated for intra-band contiguous CA, the allowed MPR is specified in clause 6.2.2 for PC3 CA bandwidth classes B and C, clause 6.2D.2 for PC2 CA bandwidth classes B and C when TxD is indicated, clause 6.2.2 for PC2 CA bandwidth classes B and C when TxD is absent.

In case the modulation format or waveform type is different on different component carriers then the requirement is set by rules applied to the waveform type (DFT-s-OFDM or CP-OFDM) and modulation order used in the configuration with the largest MPR.

Unless otherwise specified, pi/2 BPSK in following MPR tables refers to both variants of pi/2 BPSK referenced in clause 6.2.2 Table 6.2.2-1.

Table 6.2A.2.1-1: Contiguous RB allocation for Power Class 3

Table 6.2A.2.1-1a: Contiguous RB allocation for Power Class 2

Table 6.2A.2.1-1b: Contiguous RB allocation for Power Class 2 with 2Tx2

Table 6.2A.2.1-1c: Contiguous RB allocation for Power Class 1.5 with 2Tx1

Table 6.2A.2.1-1d: Contiguous RB allocation for large FWA form factor Power Class 1.5 with 2Tx1

For CA bandwidth class B and bandwidth class C with contiguous RB allocation, the following parameters are defined to specify valid RB allocation ranges for Inner and Outer RB allocations:

An RB allocation is contiguous if LCRB1 = 0 or LCRB2 = 0 or (LCRB1  0 and LCRB2  0 and RBStart1 + LCRB1 = NRB1 and RBStart2 = 0), where RBStart1, LCRB1, and NRB1 are for CC1, RBStart2, LCRB2, and NRB2 are for CC2, CC1 is the component carrier with lower frequency.

In contiguous CA, a contiguous allocation is an inner allocation if

RBStart,Low  ≤  RBStart_CA  ≤  RBStart,High, and NRB_alloc  ≤  ceil(NRB,agg /2),

where

RBStart,Low = max(1, floor(NRB_alloc /2))

RBStart,High = NRB,agg – RBStart,Low – NRB,alloc,

with

NRB_alloc= LCRB1 ∙ 2^µ1 + LCRB2 ∙ 2^µ2,

NRB,agg=NRB1∙2^µ1+ NRB2∙2^µ2.

If LCRB1 =0, RBStart_CA = NRB1∙2^µ1+ RBStart2∙2^µ2,

if LCRB1 > 0, RBStart_CA = RBStart1∙2^µ1.

A contiguous allocation that is not an Inner contiguous allocation is an Outer contiguous allocation.

For intra-band contiguous carrier aggregation the allowed Maximum Power Reduction (MPR) for the maximum output power in Table 6.2A.1.1-1 with non-contiguous RB allocation is specified in Table 6.2A.2.1-2 for UE power class 3 CA bandwidth classes B and C. The MPR with non-contiguous RB allocation is specified in Table 6.2A.2.1-3 for power class 2 CA bandwidth classes B and C when the signalling is absent for dualPA-Architecture IE, and for power class 2 CA bandwidth class C when the signalling is indicated for dualPA-Architecture IE. The MPR with non-contiguous RB allocation is specified in Table 6.2A.2.1-4 for power class 2 CA bandwidth classes B and C with TxD supported. The MPR with non-contiguous RB allocation is specified in Table 6.2A.2.1-5 and Table 6.2A.2.1-6 for 2Tx power class 1.5 for CA bandwidth class C for hand-held UE and large FWA form factor respectively.

Table 6.2A.2.1-2: non-contiguous RB allocation for Power Class 3

Table 6.2A.2.1-3: non-contiguous RB allocation for Power Class 2

Table 6.2A.2.1-4: non-contiguous RB allocation for Power Class 2 with 2Tx4

Table 6.2A.2.1-5: non-contiguous RB allocation for Power Class 1.5 with 2Tx3

Table 6.2A.2.1-6: non-contiguous RB allocation for large FWA form factor Power Class 1.5 with 2Tx3

For CA bandwidth classes B and C with non-contiguous RB allocation, the following parameters are defined to specify valid RB allocation ranges for Inner, Outer1 and Outer2 RB allocations:

Non-Contiguous RB allocation is defined as RBStart1 + LCRB1 < NRB1, or RBStart2 > 0, when both uplink CCs are activated and allocated with RB(s), where RBStart1, LCRB1, and NRB1 are for CC1, RBStart2, LCRB2, and NRB2 are for CC2, CC1 is the component carrier with lower frequency.

In contiguous CA, a non-contiguous RB allocation is a non-contiguous Inner RB allocation if the following conditions are met:

RBStart,Low  ≤  RBStart_CA  ≤  RBStart,High and NRB_alloc ≤  ceil((BWChannel_CA / 3 – BWgap ) / 0.18MHz),

where

NRB_alloc = (NRB1 - RBStart1)∙ 2^µ1 + (RBStart2 + LCRB2 ) ∙ 2^µ2,

RBStart_CA = RBStart1∙2^1

RBStart,Low = max(1, floor(NRB_alloc + (BWgap – BWGB,low)/0.18MHz))

RBStart,High = floor((BWChannel_CA – 2 ∙ BWgap – BWGB,low)/0.18MHz – 2 ∙ NRB_alloc)

BWGB,low =Foffset,low – (NRB1∙12+1)∙SCS1/2

where Foffset,low is the offset obtained as specified in sub-clause 5.3A.3 while SCS1 is the subcarrier spacing of subcarrier configuration µ1. BWgap is the bandwidth of the gap between the upper edge of the Transmission Bandwidth Configuration NRB1 of CC1 and the lower edge of the Transmisson Bandwidth Configuration NRB2 of CC2.

In contiguous CA, a non-contiguous RB allocation is a non-contiguous outer 1 RB allocation when it is not satisfying inner allocation conditions and when the following conditions are met:

RBStart,Low  ≤  RBStart_CA  ≤  RBStart,High and NRB_alloc ≤  ceil((3 BWChannel_CA / 5 – BWgap) / 0.18MHz)

where

RBStart,Low = max(1, 2 ∙ NRB_alloc – floor( (BWChannel_CA – 2 ∙ BWgap + BWGB,low)/0.18MHz)),

RBStart,High = floor((2 ∙ BWChannel_CA – 3 ∙ BWgap – BWGB,low) / 0.18MHz – 3 ∙ NRB_alloc)

NRB_alloc , RBStart_CA , BWgap and BWGB,low are as defined for the Inner region.

In contiguous CA, a non-contiguous allocation is an Outer 2 allocation if it is neither a non-contiguous Inner allocation nor an Outer 1 allocation.

## 6.2A.2.2UE maximum output power reduction for Intra-band non-contiguous CA

## 6.2A.2.2.0General

For intra-band non-contiguous CA, the allowed Maximum Power Reduction (MPR) for the maximum output power is specified into 2 types: MPR to meet -30dBm/MHz and -13dBm/MHz. The UE determines the MPR type as follows:

For UE indicating dualPA-Architecture supported

If OR (LCRB1 = 0, LCRB2 = 0), only CC1 is activated, only CC2 is activated)

MPR defined in Table 6.2.2-1 applies to PC3 intra-band NC UL CA. MPR defined in Table 6.2.2-2 applies to PC2 and PC1.5 intra-band NC UL CA.

Else If AND (FIM3,low_block,low > SEM-13,low , FIM3,high_block,high < SEM-13,high)

MPR defined in Clause 6.2A.2.2.2.1, Clause 6.2A.2.2.2.2 and clause 6.2A.2.2.2.5 applies to PC3, PC2 and PC1.5 intra-band NC UL CA respectively.

Else

MPR defined in Clause 6.2A.2.2.1.1, Clause 6.2A.2.2.1.2 and clause 6.2A.2.2.1.5 applies to PC3, PC2 and PC1.5 intra-band NC UL CA respectively.

For UE without indicating dualPA-Architecture supported

If OR (LCRB1 = 0, LCRB2 = 0), only CC1 is activated, only CC2 is activated)

For PC3 UE, MPR defined in Table 6.2.2-1, except for B < 9 MHz where 5.5 dB MPR is used;

For PC2 UE without indicating TxD, MPR defined in Table 6.2.2-2 is used, except for B < 11.52 MHz where 6.5 dB MPR is used;

For PC2 UE indicating TxD, MPR defined in Table 6.2D.2-1 is used, except for B < 11.52 MHz where the maximum value between 6.5 dB and MPR defined in Table 6.2D.2-1 is used.

Else If AND (FIM3,low_block,low > SEM-13,low ,  FIM3,high_block,high < SEM-13,high)

MPR defined in Clause 6.2A.2.2.2.3 and Clause 6.2A.2.2.2.4 for PC3 and PC2 UE respectively.

Else

MPR defined in Clause 6.2A.2.2.1.3 and Clause 6.2A.2.2.1.4 for PC3 and PC2 UE respectively.

where

-LCRB1 is for CC1 which is the component carrier with lower frequency

-LCRB2 is for CC2 which is the component carrier with higher frequency

-B =  (LCRB1* 12* SCS1 + LCRB2 * 12 * SCS2)/1,000 (MHz), where SCS1 and SCS2 are expressed in kHz.

-FIM3,high_block,high = (2 * Fhigh_alloc,high_edge ) – Flow_alloc,low_edge

-FIM3,low_block,low = (2 * Flow_alloc,low_edge) – Fhigh_alloc,high_edge

-Flow_alloc,low_edge is the lowermost frequency of the lower transmission bandwidth allocation.

-Flow_alloc,high_edge is the uppermost frequency of the lower transmission bandwidth allocation.

-Fhigh_alloc,low_edge is the lowermost frequency of the upper transmission bandwidth allocation.

-Fhigh_alloc,high_edge is the uppermost frequency of the upper transmission bandwidth allocation.

-SEM-13,low = Threshold frequency where lower spectral emission mask below the lower channel drops from -13 dBm / MHz to -25 dBm / MHz, as specified in Clause 6.5A.2.2.2.

-SEM-13,high = Threshold frequency where upper spectral emission mask above the upper channel drops from -13 dBm / MHz to -25 dBm / MHz, as specified in Clause 6.5A.2.2.2.

MPRs in section 6.2A.2.2.1.3, 6.2A.2.2.1.4, 6.2A.2.2.2.3 and 6.2A.2.2.2.4 are applicable only when the Gap between the component carriers is ≤ the overall channel bandwidth summed across all the component carriers and when UE declares intraBandFreqSeparationUL-AggBW-GapBW-r16 value ≤ 200 MHz.

The definition of the gap is between the component carriers in a spectrum that is not part of any configured component carrier that is located in between the lowest edge of the component carrier with higher center frequency and the highest edge of the component carrier with center frequency that is located lower in frequency.

## 6.2A.2.2.1MPR to meet -30dBm/MHz

6.2A.2.2.1.1PC3 with indicating dualPA-Architecture supported

MPR in this clause is for intra-band non-contiguous CA power class 3 for UEs indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

MPR=MA

Where MA is defined as follows

MA = 15; 0 ≤ B < 1.08

14.5; 1.08 ≤ B < 2.16

13.5; 2.16 ≤ B < 3.24

12.5;       3.24 ≤ B < 5.04

11.5; 5.04≤ B < 10.08

10.5; 10.08 ≤ B < 16.38

10;        16.38 ≤ B < 21.78

9;       21.78 ≤ B

6.2A.2.2.1.2PC2 with indicating dualPA-Architecture supported

MPR in this clause is for intra-band non-contiguous CA power class 2 for UEs indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

MPR=MA

Where MA is defined as follows

MA = 15.5; 0 ≤ B < 1.44

15.0; 1.44 ≤ B < 2.88

14.0;    2.88 ≤ B < 5.76

12.0; 5.76 ≤ B < 10.8

10.5; 10.8 ≤ B < 23.04

9.0;  23.04 ≤ B

6.2A.2.2.1.3PC3 without indicating dualPA-Architecture supported

MPR in this clause is for intra-band non-contiguous CA power class 3 for UEs without indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

MPR=MA

Where MA is defined as follows

MA = 17.5; 0 ≤ B < 1.08

17.0; 1.08 ≤ B < 2.16

16.5; 2.16 ≤ B < 3.24

16;      3.24 ≤ B < 5.04

15; 5.04≤ B < 10.08

14.5; 10.08 ≤ B < 36

10;      36 ≤ B < 56.88

9;       56.88 ≤ B

6.2A.2.2.1.4PC2 without indicating dualPA-Architecture supported

MPR in this clause is for intra-band non-contiguous CA power class 2 for UEs without indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

MPR=MA

Where MA is defined as follows

MA = 19.5; 0 ≤ B < 1.08

19; 1.08 ≤ B < 2.16

18; 2.16 ≤ B < 5.04

16.5; 5.04≤ B < 10.08

16; 10.08 ≤ B < 36

12;      36 ≤ B < 56.88

10.5; 56.88 ≤ B

6.2A.2.2.1.5PC1.5 with indicating dualPA-Architecture supported

MPR in this clause is for intra-band non-contiguous CA power class 1.5 for UEs indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

MPR=MA+2, where MA is defined in clause 6.2A.2.2.1.2.

MPR in this clause is for intra-band non-contiguous CA power class 1.5 for large FWA form factor indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

MPR=MA+1.5, where MA is defined in clause 6.2A.2.2.1.2.

## 6.2A.2.2.2MPR to meet -13dBm/MHz

6.2A.2.2.2.1PC3 with indicating dualPA-Architecture supported

MPR in this clause is for intra-band non-contiguous CA power class 3 for UEs indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

MPR=MA

Where MA is defined as follows

MA = 9; 0 ≤ B < 0.54

8; 0.54 ≤ B < 1.08

7; 1.08 ≤ B < 2.16

6.5; 2.16 ≤ B < 3.24

5.5; 3.24 ≤ B < 5.4

4; 5.4 ≤ B

6.2A.2.2.2.2PC2 with indicating dualPA-Architecture supported

MPR in this clause is for intra-band non-contiguous CA power class 2 for UEs indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

MPR=MA

Where MA is defined as follows

MA = 9; 0 ≤ B < 0.54

8; 0.54 ≤ B < 1.08

7; 1.08 ≤ B < 2.16

6.5; 2.16 ≤ B < 3.24

6; 3.24 ≤ B < 5.4

5.5; 5.4 ≤ B ≤ 10.8

4; 10.8 < B

6.2A.2.2.2.3PC3 without indicating dualPA-Architecture supported

MPR in this clause is for intra-band non-contiguous CA power class 3 for UEs without indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

MPR=MA

Where MA is defined as follows

MA = 11; 0 ≤ B < 1.08

10.5; 1.08 ≤ B < 2.16

10; 2.16 ≤ B < 3.24

9.5; 3.24≤ B < 5.04

8.5; 5.04 ≤ B < 10.08

7.5;      10.08 ≤ B < 36

7; 36 ≤ B

6.2A.2.2.2.4PC2 without indicating dualPA-Architecture supported

MPR in this clause is for intra-band non-contiguous CA power class 2 for UEs without indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

MPR=MA

Where MA is defined as follows

MA = 14; 0 ≤ B < 1.08

12; 1.08 ≤ B < 2.16

11.5; 2.16 ≤ B < 3.24

11; 3.24≤ B < 5.04

9.5; 5.04 ≤ B < 10.08

8.5;      10.08 ≤ B < 36

6.5; 36 ≤ B

6.2A.2.2.2.5PC1.5 with indicating dualPA-Architecture supported

MPR in this clause is for intra-band non-contiguous CA power class 1.5 for UEs indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

MPR=MA+2, where MA is defined in clause 6.2A.2.2.2.2.

MPR in this clause is for intra-band non-contiguous CA power class 1.5 for large FWA form factor indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

MPR=MA+1.5, where MA is defined in clause 6.2A.2.2.2.2.

## 6.2A.2.3UE maximum output power reduction for Inter-band CA

For inter-band carrier aggregation with one uplink carrier assigned to one NR band, the requirements in subclause 6.2.2 apply.

For inter-band carrier aggregation with two uplink contiguous carrier assigned to one NR band, the maximum output power reduction requirements for intra-band contiguous carrier aggregation in subclause 6.2A.2.1 apply for that band.

For inter-band carrier aggregation with two uplink non-contiguous carrier assigned to one NR band, the maximum output power reduction requirements for intra-band non-contiguous carrier aggregation in subclause 6.2A.2.2 apply for that band.

For inter-band carrier aggregation with uplink assigned to two NR bands, the requirements in clause 6.2.2 apply for each uplink component carrier.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per operating band), the maximum output power reduction requirements specified in subclause 6.2.2 apply for the NR band supporting one component carrier, and for the NR band supporting two contiguous component carriers the requirements specified in subclause 6.2A.2.1 apply.

## 6.2A.2.4Void

## 6.2A.3UE additional maximum output power reduction for CA

## 6.2A.3.1UE additional maximum output power reduction for Intra-band CA

## 6.2A.3.1.1UE additional maximum output power reduction for Intra-band contiguous CA

Additional emission requirements can be signalled by the network. Each additional emission requirement is associated with a unique network signalling (NS) value indicated in RRC signalling by an NR frequency band number of the applicable operating band and an associated value in the field additionalSpectrumEmission. Throughout this specification, the notion of indication or signalling of an NS value refers to the corresponding indication of an NR frequency band number of the applicable operating band, the IE field freqBandIndicatorNR and an associated value of additionalSpectrumEmission in the relevant RRC information elements [7]. Relation between NR CA band and NR frequency band is specified in Table 5.2A.1-1.

To meet the additional requirements, additional maximum power reduction (A-MPR) is allowed for the maximum output power as specified in Table 6.2A.1.1-1. Unless stated otherwise, the total reduction to UE maximum output power is max(MPR, A-MPR) where MPR is defined in clause 6.2A.2.1. In absense of modulation and waveform types the A-MPR applies to all modulation and waveform types.

Table 6.2A.3.1.1-1 specifies the additional requirements with their associated network signalling values and the allowed A-MPR and applicable CA band(s) for each CA_NS value. The CA_NS_xy value indicates the additional unwanted emissions requirements that apply for intra-band contiguous CA bands with NS_xy indicated or configured in multiple uplink serving cells, except CA_NS_01 that indicates the general emission requirements for intra-band contiguous CA bands. The mapping of NR CA band numbers and values of the additionalSpectrumEmission to network signalling labels is specified in Table 6.2A.3.1.1-2. For any NR CA band not listed in Table 6.2A.3.1.1-2 the network signalling label CA_NS_01 applies.

Table 6.2A.3.1.1-1: Additional maximum power reduction (A-MPR)

For UEs configured with intra-band contiguous CA in n77 and if NS_01 is indicated for an uplink component carrier in the range 3450-3650 MHz and NS_01 or NS_57 for another uplink component carrier below 3980 MHz and partly or fully confined within the range 3650-3980 MHz, the allowed additional spurious emission and maximum output power reduction requirements are according to CA_NS_01.

Table 6.2A.3.1.1-2: Mapping of network signaling label

6.2A.3.1.1.1A-MPR for CA_NS_04

6.2A.3.1.1.1.1Contiguous allocations

For all waveform type, modulations and scs when Fedge, low - BWChannel_CA ≥ 2490.5 MHz, A-MPR = MPR

For all modulations and SCS when Fedge, low - BWChannel_CA < 2490.5 MHz

if the RB allocation is an inner allocation as defined in clause 6.2A.2.1, then A-MPR = MPR

Except for RBstart ≤ 0.33*BWchannel_CA/0.18MHz, AMPR= max (MPR, AMPRcc).

if the RB allocation is an outer allocation as defined in clause 6.2A.2.1,

then for PC3 and PC2, A-MPR = MPR+1.5dB for BW Class B, A-MPR = MPR for BW class C. For PC1.5 BW Class C, A-MPR = MPR+1.5dB with MPR values in Table 6.2A.2.1-1c and Table 6.2A.2.1-1d for handheld UE and large FWA form factor respectively.

Where

-MPR is the MPR as defined in Table 6.2A.2.1-1 for PC3, Table 6.2A.2.1-1a and Table 6.2A.2.1-1b for PC2 and Table 6.2A.2.1-1c and Table 6.2A.2.1-1d for PC1.5 and the respective CA bandwidth class

-AMPRcc is defined as the PC3_A2, PC2_A4 or PC1.5 A6 AMPR in Table 6.2.3.2-2 for PC3, PC2 and PC1.5 respectively.

6.2A.3.1.1.1.2Non-contiguous allocations

For intra-band contiguous CA_n41B and CA_n41C and it receives IE CA_ NS_04, the UE determines the allowed Additional Maximum Power Reduction (AMPR) for the maximum output power as specified in this clause. The AMPR is specified by AMPRIM3 to meet -25dBm/MHz when IM3 falls in -25dBm/MHz region of Table 6.5A.2.3.1.1-1 or Table 6.5A.3.3.1.1-1. And uses MPR for all other cases.

The UE determines the A-MPR for all waveforms, modulations, and SCSs as follows:

If FIM3, low_block,low 2490.5 MHz AND FIM3,low_block,high > Ffilter,low,

-A-MPR = A-MPRIM3 defined in Clause 6.2A.3.1.1.1.3.

else,

-if RB allocation is an inner or outer 1 allocation as defined in clause 6.2A.2.1 then A-MPR = MPR.

-if RB allocation is an outer 2 allocation as defined in clause 6.2A.2.1 then A-MPR = MPR + 1 dB.

where

-MPR is the MPR as defined in Table 6.2A.2.1-2 for PC3, Table 6.2A.2.1-3 and Table 6.2A.2.1-4 for PC2 and PC2 2Tx respectively and the respective CA bandwidth class, and Table 6.2A.2.1-5 and Table 6.2A.2.1-5 for Class C PC1.5 2Tx and large FWA form factor PC1.5 2Tx respectively.

-FIM3,low_block,low = (2 * Flow_alloc,low_edge ) – Fhigh_alloc,high_edge

-FIM3,low_block,high = (2 * Flow_alloc,high_edge ) – Fhigh_alloc,low_edge

-Flow_alloc,low_edge is the lowermost frequency of lower transmission bandwidth allocation.

-Flow_alloc,high_edge is the uppermost frequency of lower transmission bandwidth allocation.

-Fhigh_alloc,low_edge is the lowermost frequency of upper transmission bandwidth allocation.

-Fhigh_alloc,high_edge is the uppermost frequency of upper transmission bandwidth allocation.

-Ffilter,low = 2480 MHz

6.2A.3.1.1.1.3AMPRIM3 to meet -25dBm/MHz

AMPR in this clause is for intra-band contiguous CA_n41B and CA_n41C. The allowed maximum output power reduction is defined as:

AMPRIM3=MA, Where MA is defined as follows for PC3

MA = 13; 0 ≤ B < 2.16

11.5; 2.16 ≤ B < 3.24

10.5;       3.24 ≤ B < 5.04

9.5; 5.04 ≤ B < 10.08

8; 10.08 ≤ B < 16.56

7;        16.56 ≤ B < 21.96

6;       21.96 ≤ B

AMPRIM3=MA, Where MA is defined as follows for 1Tx PC2 and MA is increased by 1dB for 2Tx PC2.

MA = 14; 0 ≤ B < 2.16

12.5; 2.16 ≤ B < 3.24

11.5;       3.24 ≤ B < 5.04

10.5; 5.04 ≤ B < 10.08

9; 10.08 ≤ B < 16.56

8;        16.56 ≤ B < 21.96

7;       21.96 ≤ B

AMPRIM3=MA, Where MA is defined as follows for hand-held 2Tx PC1.5 and MA is reduced by 0.5dB for large FWA form factor 2Tx PC1.5.

MA = 16.5; 0 ≤ B < 1.44

15.5; 1.44 ≤ B < 2.88

14.5;     2.88 ≤ B < 5.76

12.5; 5.76 ≤ B < 10.8

10.5; 10.8 ≤ B <23.04

10;       23.04 ≤ B

Where:

B = (LCRB1* 12* SCS1 + LCRB2 * 12 * SCS2)/1,000 (MHz), where SCS1 and SCS2 are expressed in kHz.

and LCRB1, SCS1 are for CC1, LCRB2, SCS2 are for CC2, CC1 is the component carrier with lower frequency.

6.2A.3.1.1.2A-MPR for CA_NS_27

6.2A.3.1.1.2.1Contiguous allocations

For all modulations and scs when Fedge, low - BWChannel_CA ≥ 3540 MHz AND Fedge, high + BWChannel_CA ≤ 3710 MHz

if allocation is inner 1 then A-MPR = 0 dB where inner 1 is defined as

RBStart,Low = max(1, floor(LCRB_agg/2))

where max() indicates the largest value of all arguments and floor(x) is the greatest integer less than or equal to x and,

LCRB_agg= LCRB1* 2µ1 + LCRB2*2µ2

where μ is defined in TS 38.211 [6], and LCRB1, µ1 are for CC1, LCRB2, µ2 are for CC2, CC1 is the component carrier with lower frequency, and

RBStart,High = NRB_agg – RBStart,Low – LCRB_agg

with the following conditions:

RBStart,Low  ≤  RBStart  ≤  RBStart,High, and

LCRB_agg ≤ ceil(NRB_agg /2)

where,

For LCRB1>0, RBStart=RBStart1*2µ1,

For LCRB1=0, RBStart=NRB1*2µ1 + RBStart2*2µ2,

and RBStart1, µ1 and LCRB1 are for CC1, RBStart2, and µ2 is for CC2.

A-MPR = 5 dB for some exceptions for inner 1 region. These exceptions are defined when LCRB_agg < 8 and any of the following conditions are met:

RBStart ≤ 30 or RBend ≥ 164 for BWSum_CA = 40MHz,

or

for the subset of frequencies that satisfy 3540 MHz + BWChannel_CA ≤ Fedge, low < 3530 MHz + 2*BWChannel_CA, the following exception thresholds apply

for BWSum_CA = 35MHz threshold of RBstart ≤ 25, and

for BWSum_CA = 30MHz threshold of RBstart ≤ 19, and

for BWSum_CA = 25MHz threshold of RBstart ≤ 14, and

for BWSum_CA = 20MHz threshold of RBstart ≤ 9, and

for BWSum_CA = 15MHz threshold of RBstart ≤ 3

or for the subset of frequencies that satisfy 3720 MHz – 2*BWChannel_CA < Fedge, high ≤ 3710 MHz – BWChannel_CA, the following exception thresholds apply

for BWSum_CA = 35MHz threshold of RBend ≥ 144, and

for BWSum_CA = 30MHz threshold of RBend ≥ 124, and

for BWSum_CA = 25MHz threshold of RBend ≥ 104, and

for BWSum_CA = 20MHz threshold of RBend ≥ 80, and

for BWSum_CA = 15MHz threshold of RBend ≥ 68,

else for non-inner 1 allocations A-MPR= 5 dB when Fedge, low - BWChannel_CA ≥ 3540 MHz AND Fedge, high + BWChannel_CA ≤ 3710 MHz

For all modulations and scs when 3550 MHz ≤ Fedge, low < 3540 MHz + BWChannel_CA

if allocation is inner 3 then A-MPR = 0 dB, where inner 3 is defined as

NRB_agg /4 < RBStart < NRB_agg 3/4  LCRB_agg AND LCRB_agg < NRB_agg/4

Inner 3 region exceptions thresholds are

for BWSum_CA = 40MHz threshold of RBstart ≤ 63, and

for BWSum_CA = 35MHz threshold of RBstart ≤ 52, and

for BWSum_CA = 30MHz threshold of RBstart ≤ 42, and

For which AMPR = 11.5dB

else for non-inner 3 allocations when BWSum_CA ≤ 20 MHz, A-MPR = 7 dB or when BWSum_CA > 20 MHz, A-MPR = 11.5dB when 3550 MHz ≤ Fedge, low < 3540 MHz + BWChannel_CA.

For all modulations and scs when 3710 MHz - BWChannel_CA < Fedge, high ≤ 3700

if allocation is inner 3 then A-MPR = 0 dB.

Inner 3 region exceptions thresholds are

for BWSum_CA = 40MHz threshold of RBend ≥ 132, and

for BWSum_CA = 35MHz threshold of RBend ≥ 121, and

for BWSum_CA = 30MHz threshold of RBend ≥ 110, and

For which A-MPR 11.5dB

else for non-inner 3 allocation when BWSum_CA ≤ 20 MHz, A-MPR = 7 dB or when BWSum_CA > 20 MHz, A-MPR = 11.5dB when 3710 MHz - BWChannel_CA < Fedge, high ≤ 3700.

6.2A.3.1.1.2.2Non-contiguous allocations

For all modulations and SCS when Fedge, low - BWChannel_CA ≥ 3540 MHz AND Fedge, high + BWChannel_CA ≤ 3710 MHz

A-MPR=

13; 0 ≤B<1.08

12; 1.08 ≤B<2.16

11; 2.16 ≤B<3.24

10.5; 3.24 ≤ B < 5.04

9.5; 5.04≤B< 10.08

8; 10.08 ≤B< 16.56

7; 16.56 ≤ B < 21.96

6.5; 21.96 ≤B

For all modulations and SCS when 3550 MHz ≤ Fedge, low < 3540 MHz + BWChannel_CA or 3710 MHz - BWChannel_CA < Fedge, high ≤ 3700

when BWSum_CA ≤ 20 MHz

A-MPR=

13; 0 ≤B<1.08

12; 1.08 ≤B<2.16

11; 2.16 ≤B<3.24

10.5; 3.24 ≤ B < 5.04

9.5; 5.04 ≤B< 10.08

8; 10.08 ≤B< 16.56

7; 16.56 ≤ B < 21.96

6.5; 21.96 ≤B

or when BWSum_CA > 20 MHz

A-MPR =

20; 0 ≤B<1.08

19.5; 1.08 ≤B<2.16

19; 2.16 ≤B<3.24

18.5; 3.24 ≤ B < 5.04

18; 5.04 ≤B< 10.08

17; 10.08 ≤B< 16.56

16; 16.56 ≤ B < 21.96

13; 21.96 ≤B.

Where:

B=(LCRB1* 12* SCS1 + LCRB2 * 12 * SCS2)/ 1MHz,

and LCRB1, SCS1 are for CC1, LCRB2, SCS2 are for CC2, CC1 is the component carrier with lower frequency.

6.2A.3.1.1.3A-MPR for CA_NS_46

6.2A.3.1.1.3.1Contiguous allocations

For all modulations and scs when BWChannel_CA > 25 MHz

IFRBend > NRB_agg 5/6 for all BW’s except for BWChannel_CA=50MHz where the threshold is RBend>NRB_agg 3/4 OR for all BW’s RBend > 4/3 NRB_agg - LCRB

THENA-MPR = 11dB

ELSE IF RBend < NRB_agg /6 AND LCRB < 5

THENA-MPR = 5dB

ELSE IFLCRB 3/2< RBend < NRB_agg 3/4 AND LCRB < NRB_agg /4

THEN A-MPR = 0 dB,

OTHERWISEA-MPR = 7 dB.

For all modulations and scs when BWChannel_CA <= 25 MHz and 2595 MHz – 2*BWChannel_CA < Fedge,high ≤ 2570 MHz

IF RBend ≥ 4/3 NRB_agg - LCRB

THEN A-MPR = 6 dB.

OTHERWISEA-MPR = 0 dB.

For all modulations and scs when BWChannel_CA <= 25 MHz and Fedge_high <= 2595 MHz – 2*BWChannel_CA,

A-MPR = 0 dB.

6.2A.3.1.1.3.2Non-contiguous allocations

[For all modulations and scs when BWChannel_CA > 25 MHz and 2595 MHz - BWChannel_CA ≤ Fedge_high ≤ 2570 MHz

A-MPRCA_IM3 =

20; 0 ≤B<1.08

19.5; 1.08 ≤B<2.16

19; 2.16 ≤B<3.24

18.5; 3.24 ≤ B < 5.04

18; 5.04 ≤B< 10.08

17; 10.08 ≤B< 16.56

16; 16.56 ≤ B < 21.96

13; 21.96 ≤B

For all modulations and scs when BWChannel_CA > 25 MHz and Fedge_high < 2595 MHz - BWChannel_CA

A-MPRCA_IM5 =

13; 0 ≤B<1.08

12; 1.08 ≤B<2.16

11; 2.16 ≤B<3.24

10.5; 3.24 ≤ B < 5.04

9.5; 5.04 ≤B< 10.08

8; 10.08 ≤B< 16.56

7.5; 16.56 ≤ B < 21.96

7; 21.96 ≤B

For all modulations and scs when BWChannel_CA <= 25 MHz and 2595 MHz – 2*BWChannel_CA ≤ Fedge_high ≤ 2570 MHz

A-MPRCA_IM5 =

13; 0 ≤B<1.08

12; 1.08 ≤B<2.16

11; 2.16 ≤B<3.24

10.5; 3.24 ≤ B < 5.04

9.5; 5.04 ≤B< 10.08

8; 10.08 ≤B< 16.56

7.5; 16.56 ≤ B < 21.96

7; 21.96 ≤B

Where:

B = (LCRB1* 12* SCS1 + LCRB2 * 12 * SCS2)/1,000 (MHz), where SCS1 and SCS2 are expressed in kHz.

and LCRB1, SCS1 are for CC1, LCRB2, SCS2 are for CC2, CC1 is the component carrier with lower frequency.]

## 6.2A.3.1.2UE additional maximum output power reduction for Intra-band non-contiguous CA

6.2A.3.1.2.0General

Table 6.2A.3.1.2-1 specifies the additional requirements with their associated network signalling values and the allowed A-MPR and applicable CA band(s) for each CA_NC_NS value. The CA_NC_NS_xy value indicates the additional unwanted emissions requirements that apply for intra-band non-contiguous CA bands with NS_xy indicated or configured in multiple uplink serving cells, except CA_NC_NS_01 that indicates the general emission requirements for intra-band non-contiguous CA bands. The mapping of NR CA band numbers and values of the additionalSpectrumEmission to network signalling labels is specified in Table 6.2A.3.1.2-2. For any NR CA band not listed in Table 6.2A.3.1.2-2 the network signalling label CA_NC_NS_01 applies.

Table 6.2A.3.1.2-1: Additional Maximum Power Reduction (A-MPR) forintra-band non-contiguous CA

For UEs configured with intra-band non-contiguous CA in n77 and if NS_01 is indicated for an uplink component carrier in the range 3700-3980 MHz and NS_01 or NS_55 for another uplink component carrier in the range 3450-3550 MHz, or if NS_01 is indicated for an uplink component carrier in the range 3450-3650 MHz and NS_01 or NS_57 for another uplink component carrier below 3980 MHz and partly or fully confined within the range 3650-3980 MHz, the allowed additional spurious emission and maximum output power reduction requirements are according to CA_NC_NS_01.

Table 6.2A.3.1.2-2: Mapping of network signaling label

6.2A.3.1.2.1AMPR for CA_NC_NS_04 (CA_n41(2A))

For intra-band non-contiguous CA_n41(2A) and it receives CA_NC_NS_04 for UE indicating dualPA-Architecture supported for PC3 and PC2 operation, the UE determines the allowed Additional Maximum Power Reduction (AMPR) for the maximum output power as specified in this clause. The AMPR is specified into 2 types: AMPR to meet -25dBm/MHz and -13dBm/MHz. The A-MPR defined in this clause is used instead of MPR defined in 6.2A.2.2, not additively, so CA MPR=0 when CA_NC_NS_04 is signaled.

The UE determines the AMPR type as follows:

If AND( MIN(FIM3,low_block,high, SEM-13,low) < Ffilter,low ,  MAX( SEM-13,high, FIM3,high_block,low ) > Ffilter,high )

-A-MPRIM3 defined in Clause 6.2A.3.1.2.1.2 for PC3, 6.2A.3.1.2.1.4 for PC2 and 6.2A.3.1.2.1.6 for PC1.5

Else

-A-MPRIM3 defined in Clause 6.2A.3.1.2.1.1 for PC3, 6.2A.3.1.2.1.3 for PC2 and 6.2A.3.1.2.1.5 for PC1.5

where

-LCRB1 is for CC1 which is the component carrier with lower frequency

-LCRB2 is for CC2 which is the component carrier with higher frequency

-B = (LCRB1* 12* SCS1 + LCRB2 * 12 * SCS2)/1,000 (MHz), where SCS1 and SCS2 are expressed in kHz.

-FIM3,low_block,high = (2 * Flow_alloc,high_edge ) – Fhigh_alloc,low_edge

-FIM3,high_block,low = (2 * Fhigh_alloc,low_edge) – Flow_alloc,high_edge

-Flow_alloc,low_edge is the lowermost frequency of lower transmission bandwidth allocation.

-Flow_alloc,high_edge is the uppermost frequency of lower transmission bandwidth allocation.

-Fhigh_alloc,low_edge is the lowermost frequency of upper transmission bandwidth allocation.

-Fhigh_alloc,high_edge is the uppermost frequency of upper transmission bandwidth allocation.

-Ffilter,low = 2480 MHz

-Ffilter,high = 2745 MHz

-SEM-13,high = Threshold frequency where upper spectral emission mask for upper channel drops from -13 dBm / 1MHz to -25 dBm / 1MHz, as specified in Clause 6.5A.2.3.2.

-SEM-13,low = Threshold frequency where lower spectral emission mask below the lower channel drops from -13 dBm / MHz to -25 dBm / MHz, as specified in Clause 6.5A.2.3.2.

6.2A.3.1.2.1.1AMPRIM3 to meet -25dBm/MHz for PC3

AMPR in this clause is for intra-band non-contiguous CA_n41(2A) power class 3 for UEs indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

AMPRIM3=MAWhere MA is defined as follows

MA = 12; 0 ≤ B < 1.08

12; 1.08 ≤ B < 2.16

11; 2.16 ≤ B < 3.24

10;       3.24 ≤ B < 5.04

9; 5.04 ≤ B < 10.08

8; 10.08 ≤ B < 16.38

7;        16.38 ≤ B < 21.78

6;       21.78 ≤ B

6.2A.3.1.2.1.2AMPRIM3 to meet -13dBm/MHz for PC3

AMPR in this clause is for intra-band non-contiguous CA_n41(2A) power class 3 for UEs indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

AMPRIM3=MA

Where MA is defined as follows

MA = 9; 0 ≤ B < 0.54

8; 0.54 ≤ B < 1.08

7; 1.08 ≤ B < 2.16

6.5; 2.16 ≤ B < 3.24

5.5; 3.24 ≤ B < 5.4

4; 5.4 ≤ B

6.2A.3.1.2.1.3AMPRIM3 to meet -25dBm/MHz for PC2

AMPR in this clause is for intra-band non-contiguous CA_n41(2A) power class 2 for UEs indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

AMPRIM3=MA

Where MA is defined as follows

MA = 14.5; 0 ≤ B < 1.44

14.0; 1.44 ≤ B < 2.88

13.0;    2.88 ≤ B < 5.76

11.0; 5.76 ≤ B < 10.8

9.5; 10.8 ≤ B < 23.04

9.0;  23.04 ≤ B

Where:

B=(LCRB_alloc, 1* 12* SCS1 + LCRB_alloc,2 * 12 * SCS2)/1,000 (MHz), where SCS1 and SCS2 are expressed in kHz.

6.2A.3.1.2.1.4AMPRIM3 to meet -13dBm/MHz for PC2

AMPR in this clause is for intra-band non-contiguous CA_n41(2A) power class 2 for UEs indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

AMPRIM3=MA

Where MA is defined as follows

MA = 9; 0 ≤ B < 0.54

8; 0.54 ≤ B < 1.08

7; 1.08 ≤ B < 2.16

6.5; 2.16 ≤ B < 3.24

6; 3.24 ≤ B < 5.4

5.5; 5.4 ≤ B ≤ 10.8

4; 10.8 < B

Where:

B = (LCRB_alloc, 1* 12* SCS1 + LCRB_alloc,2 * 12 * SCS2)/1,000 (MHz), where SCS1 and SCS2 are expressed in kHz.

6.2A.3.1.2.1.5AMPRIM3 to meet -25dBm/MHz for PC1.5

AMPR in this clause is for intra-band non-contiguous CA_n41(2A) power class 1.5 for UEs indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

AMPRIM3=MA+2, where MA is defined 6.2A.3.1.2.1.3.

6.2A.3.1.2.1.6AMPRIM3 to meet -13dBm/MHz for PC1.5

AMPR in this clause is for intra-band non-contiguous CA_n41(2A) power class 1.5 for UEs indicating IE dualPA-Architecture supported. The allowed maximum output power reduction is defined as:

AMPRIM3=MA+2, where MA is defined in clause 6.2A.3.1.2.1.4.

## 6.2A.3.1.3UE additional maximum output power reduction for Inter-band CA

Unless otherwise stated, for inter-band carrier aggregation with one uplink carrier assigned to one NR band, the requirements in subclause 6.2.3 apply.

Unless otherwise stated, for inter-band carrier aggregation with two uplink contiguous carrier assigned to one NR band, the additional maximum output power reduction requirements for intra-band contiguous carrier aggregation in subclause 6.2A.3.1.1 apply for that band, for inter-band carrier aggregation with two uplink non-contiguous carrier assigned to one NR band, the additional maximum output power reduction requirements for intra-band contiguous carrier aggregation in subclause 6.2A.3.1.2 apply for that band.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per operating band), the additional maximum output power reduction requirements specified in subclause 6.2.3 apply for the NR band supporting one component carrier, and for the NR band supporting two contiguous component carriers the requirements specified in subclause 6.2A.3.1.1apply.

Unless specified in Table 6.2A.3.1.3-1, for inter-band carrier aggregation with uplink assigned to two NR bands, the requirements in clause 6.2.3 apply only to the indicated carrier. The requirements in Table 6.2A.3.1.3-1 are specified in terms of an additional spectrum emission requirement with their associated network signalling values and the allowed A-MPR. Unless otherwise stated, the combined requirements and allowed A-MPR are applicable on both bands when both component carriers are active. Additional spurious emission requirements are signalled by the network to indicate that the UE shall meet the additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

To meet the additional requirements, additional maximum power reduction (A-MPR) is allowed for the maximum output power as specified in Table 6.2.1-1. Unless stated otherwise, the total reduction to UE maximum output power is max(MPR+∆MPR, A-MPR) where MPR and ∆MPR are defined in clause 6.2.2. In case of a power class 3 UE, when IE powerBoostPi2BPSK is set to 1, power class 2 A-MPR values apply.

For almost contiguous allocations in CP-OFDM waveforms in power class 1.5, 2 and 3, the allowed A-MPR defined in clause 6.2.3 is increased by CEIL{ 10 log10(1 + NRB_gap / NRB_alloc), 0.5 } dB, where NRB_gap is the total number of unallocated RBs between allocated RBs and NRB_alloc is the total number of allocated RBs, and the parameter LCRB is replaced by NRB_alloc + NRB_gap in specifying the RB allocation regions.

Unless otherwise specified, pi/2 BPSK in following A-MPR tables refers to both variants of pi/2 BPSK referenced in clause 6.2.2 Table 6.2.2-1.

The emission requirements specified in Table 6.2A.3.1.3-1 also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.2A.3.1.3-1: Additional Requirements for uplink inter-band carrier aggregation (two-bands)

## 6.2A.4Configured output power for CA

## 6.2A.4.1Configured transmitted power level

## 6.2A.4.1.1Configured transmitted power for Intra-band contiguous CA

For uplink carrier aggregation the UE is allowed to set its configured maximum output power PCMAX,c for serving cell c and its total configured maximum output power PCMAX.

The configured maximum output power PCMAX,c  on serving cell c shall be set as specified in clause 6.2.4, but with MPRc = MPR and A-MPRc = A-MPR with MPR and A-MPR as determined by subclause 6.2A.2 and 6.2A.3, respectively. For PH reporting the following exception applies: if the UE is configured with multiple uplink serving cells, the power PCMAX,c  used for the purpose of PH reporting on first serving cell c = c1 does not consider for computation of the PH report transmissions on a second serving cell c2 as exempted  in subclause 7.7.1 in [8]. There is one power management term for the UE, denoted P-MPR, and P-MPR c = P-MPR.

The total configured maximum output power PCMAX shall be set within the following bounds:

PCMAX_L ≤ PCMAX ≤ PCMAX_H

For uplink intra-band contiguous carrier aggregation when same slot pattern is used in all aggregated serving cells,

PCMAX_L  = MIN{10 log10 ∑ pEMAX,c  - TC , PEMAX,CA,(PPowerClass,CA– ΔPPowerClass,CA) – MAX(MAX(MPR, A-MPR) + ΔTIB,c + TC + TRxSRS, P-MPRc ) }

PCMAX_H  = MIN{10 log10 ∑ pEMAX,c , PEMAX,CA ,PPowerClass,CA– ΔPPowerClass,CA }

where

-pEMAX,c is the linear value of PEMAX,c which is given by IE P-Max for serving cell c in [7];

PPowerClass,CA is the maximum UE power specified in Table 6.2A.1.1-1 without taking into account the tolerance;

-MPR and A-MPR are specified in clause 6.2A.2 and 6.2A.3, respectively;

-ΔPPowerClass,CA = 3 dB for a power class 2 or 6 dB for a power class 1.5 UE when the requirements of default power class are applied as specified in sub-clause 6.2.A.1.1; otherwise ΔPPowerClass,CA = 0 dB;

NOTE:UE reports ∆PPowerClass,CA when deltaPowerClassReporting-r18 is present, dpc-Reporting-FR1 [7] is configured and the reporting is triggered only by uplink duty cycle exceedance or by return to the powerClass after the duty cycle exceedance.

-TIB,c is the additional tolerance for serving cell c as specified in clause 6.2A.4.2 for NR CA, clause 6.2C.2 for SUL, or TS 38.101-3 clause  6.2B.4.2 for EN-DC; In case the UE supports more than one of band combinations for CA, SUL or DC, and an operating band belongs to more than one band combinations then

a)When the operating band frequency range is ≤ 1 GHz, the applicable additional ∆TIB,c shall be the average value for all band combinations defined in clause 6.2A.4.2, 6.2C.2 in this specification and 6.2B.4.2 in TS 38.101-3 [3], truncated to one decimal place that apply for that operating band among the supported band combinations. In case there is a harmonic relation between low band UL and high band DL, then the maximum ∆TIB,c among the different supported band combinations involving such band shall be applied

b)When the operating band frequency range is > 1 GHz, the applicable additional ∆TIB,c shall be the maximum value for all band combinations defined in clause 6.2A.4.2, 6.2C.2 in this specification and 6.2B.4.2 in TS 38.101-3 [3] for the applicable operating bands.

-P-MPR is the power management term for the UE;

-TC is the highest value TC,c among all serving cells c;

-∆TRxSRS is the highest value among all serving cells c;

-PEMAX,CA is the value indicated by p-NR-FR1 or by p-UE-FR1 whichever is the smallest if both are present.

For uplink intra-band contiguous carrier aggregation, when at least one different numerology/slot pattern is used in aggregated cells, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of slot numerology type i, and its total configured maximum output power PCMAX.

The configured maximum output power PCMAX,c(i),i (p) in slot p of serving cell c(i) on slot numerology type i shall be set within the following bounds:

PCMAX_L,f,c(i),i (p) ≤  PCMAX,f,c(i), i (p) ≤  PCMAX_H,f,c(i),i (p)

where PCMAX_L,f,c (i),i (p) and PCMAX_H,f,c(i),i (p) are the limits for a serving cell c(i) of slot numerology type i as specified in clause 6.2.4.

The total UE configured maximum output power PCMAX (p,q) in a slot p of slot numerology or symbol pattern i,  and a slot q of slot numerology or symbol pattern j that overlap in time shall be set within the following bounds unless stated otherwise:

PCMAX_L(p,q) ≤  PCMAX (p,q)  ≤  PCMAX_H (p,q)

When slots p and q have different transmissions lengths and belong to different cells on different or same bands:

PCMAX_L (p,q) = MIN {10 log10 [pCMAX_L,f,c(i),i (p) + pCMAX_L,f,c(i),j (q)], PPowerClass,CA, PEMAX,CA}

PCMAX_H (p,q) = MIN {10 log10 [pCMAX_ H,f,c(i),i (p) + pCMAX_ H,f,c(i),j (q)], PPowerClass,CA, PEMAX,CA}

where pCMAX_L,f,c (i),i  and pCMAX_ H,f,c(i),i  are the respective limits PCMAX_L,f,c (i),i and PCMAX_H,f,c(i),i expressed in linear scale.

TREF and Teval are specified in Table 6.2A.4.1.1-0 when same and different slot patterns are used in aggregated carriers. For each TREF, the PCMAX_L is evaluated per Teval and given by the minimum value taken over the transmission(s) within the Teval; the minimum PCMAX_L over the one or more Teval is then applied for the entire TREF. The lesser of PPowerClass,CA and PEMAX,CA shall not be exceeded by the UE during any period of time.

Table 6.2A.4.1.1-0: PCMAX evaluation window for different slot and channel durations

If the UE is configured with multiple TAGs and transmissions of the UE on slot i for any serving cell in one TAG overlap some portion of the first symbol of the transmission on slot i +1 for a different serving cell in another TAG, the UE minimum of PCMAX_L for slots i and i + 1 applies for any overlapping portion of slots i and i + 1. The lesser of PPowerClass,CA and PEMAX,CA shall not be exceeded by the UE during any period of time.

The measured maximum output power PUMAX over all serving cells with same slot pattern shall be within the following range:

PCMAX_L  – MAX{TL, TLOW(PCMAX_L) }  ≤  PUMAX  ≤  PCMAX_H  +  THIGH(PCMAX_H)

PUMAX = 10 log10 ∑ pUMAX,c

where pUMAX,c  denotes the measured maximum output power for serving cell c expressed in linear scale. The tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX are specified in Table 6.2A.4.1.1-1. The tolerance TL is the absolute value of the lower tolerance for applicable NR CA configuration as specified in Table 6.2A.1.1-1 for intra-band carrier aggregation.

The measured maximum output power PUMAX over all serving cells, when at least one slot has a different transmission numerology or slot pattern, shall be within the following range:

P'CMAX_L– MAX{TL, TLOW (P'CMAX_L)} ≤  P'UMAX  ≤  P'CMAX_H + THIGH (P'CMAX_H)

P'UMAX = 10 log10 ∑ p'UMAX,c

where p'UMAX,c  denotes the average measured maximum output power for serving cell c expressed in linear scale over TREF. The tolerances TLOW(P'CMAX) and THIGH(P'CMAX) for applicable values of P'CMAX are specified in Table 6.2A.4.1.1-1 for intra-band carrier aggregation. The tolerance TL is the absolute value of the lower tolerance for applicable NR CA configuration as specified in Table 6.2A.1.1-1 for intra-band carrier aggregation.

where:

P'CMAX_L  = MIN{ MIN {10log10∑( pCMAX_L,f,c(i),i), PPowerClass,CA} over all overlapping slots in TREF}

P'CMAX_H = MAX{ MIN{10 log10 ∑ pEMAX,c , PPowerClass,CA} over all overlapping slots in TREF}

Table 6.2A.4.1.1-1: PCMAX tolerance for uplink intra-band contiguous CA

## 6.2A.4.1.2Configured transmitted power for Intra-band non-contiguous CA

For uplink carrier aggregation the UE is allowed to set its configured maximum output power PCMAX,c for serving cell c and its total configured maximum output power PCMAX.

The configured maximum output power PCMAX,c  on serving cell c shall be set as specified in subclause 6.2.4.

For a UE supporting PC1.5 intra-band NC UL CA, the maximum output power of each CC is limited to 26 dBm.

The configured maximum output power PCMAX,c  on serving cell c shall be set as specified in subclause 6.2.4, but with MPRc = MPR and A-MPRc = A-MPR with MPR and A-MPR as determined by subclause 6.2A.2 and 6.2A.3, respectively. For PH reporting the following exception applies: if the UE is configured with multiple uplink serving cells, the power PCMAX,c  used for the purpose of PH reporting on first serving cell c = c1 does not consider for computation of the PH report transmissions on a second serving cell c2 as exempted  in subclause 7.7.1 in [8]. There is one power management term for the UE, denoted P-MPR, and P-MPR c = P-MPR.

The total configured maximum output power PCMAX shall be set within the following bounds:

PCMAX_L ≤ PCMAX ≤ PCMAX_H

For uplink intra-band non-contiguous carrier aggregation when same slot pattern is used in all aggregated serving cells,

PCMAX_L  = MIN{10 log10 ∑ pEMAX,c  - TC , PEMAX,CA,(PPowerClass,CA– ΔPPowerClass,CA) – MAX(MAX(MPRc, A-MPRc) + ΔTIB,c + TC + DTRxSRS, P-MPR ) }

PCMAX_H  = MIN{10 log10 ∑ pEMAX,c , PEMAX,CA ,PPowerClass,CA– ΔPPowerClass,CA)}

where

-pEMAX,c is the linear value of PEMAX,c which is given by IE P-Max for serving cell c in [7];

-PPowerClass,CA is the maximum UE power specified in Table 6.2A.1.2-1 without taking into account the tolerance;

-MPR and A-MPR are specified in subclause 6.2A.2 and subclause 6.2A.3 respectively;

-ΔPPowerClass,CA = 3 dB for a power class 2 or 6 dB for a power class 1.5 UE when the requirements of default power class are applied as specified in sub-clause 6.2.A.1.2; otherwise ΔPPowerClass,CA = 0 dB;

NOTE:UE reports ∆PPowerClass,CA when deltaPowerClassReporting-r18 is present, dpc-Reporting-FR1 [7] is configured and the reporting is triggered only by uplink duty cycle exceedance or by return to the powerClass after the duty cycle exceedance.

-TIB,c is the additional tolerance for serving cell c as specified in clause 6.2A.4.2 for NR CA, clause 6.2C.2 for SUL, or TS 38.101-3 clause  6.2B.4.2 for EN-DC; In case the UE supports more than one of band combinations for CA, SUL or DC, and an operating band belongs to more than one band combinations then

a)When the operating band frequency range is ≤ 1 GHz, the applicable additional ∆TIB,c shall be the average value for all band combinations defined in clause 6.2A.4.2, 6.2C.2 in this specification and 6.2B.4.2 in TS 38.101-3 [3], truncated to one decimal place that apply for that operating band among the supported band combinations. In case there is a harmonic relation between low band UL and high band DL, then the maximum ∆TIB,c among the different supported band combinations involving such band shall be applied

b)When the operating band frequency range is > 1 GHz, the applicable additional ∆TIB,c shall be the maximum value for all band combinations defined in clause 6.2A.4.2, 6.2C.2 in this specification and 6.2B.4.2 in TS 38.101-3 [3] for the applicable operating bands.

-P-MPR is the power management term for the UE;

-TC is the highest value TC,c among all serving cells c;

-∆TRxSRS is the highest value among all serving cells c;

-PEMAX,CA is the value indicated by p-NR-FR1 or by p-UE-FR1 whichever is the smallest if both are present.

[For uplink intra-band non-contiguous carrier aggregation, when at least one different numerology/slot pattern is used in aggregated cells, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of slot numerology type i, and its total configured maximum output power PCMAX.

The configured maximum output power PCMAX,c(i),i (p) in slot p of serving cell c(i) on slot numerology type i shall be set within the following bounds:

PCMAX_L,f,c(i),i (p) ≤  PCMAX,f,c(i), i (p) ≤  PCMAX_H,f,c(i),i (p)

where PCMAX_L,f,c (i),i (p) and PCMAX_H,f,c(i),i (p) are the limits for a serving cell c(i) of slot numerology type i as specified in subclause 6.2.4.

The total UE configured maximum output power PCMAX (p,q) in a slot p of slot numerology or symbol pattern i,  and a slot q of slot numerology or symbol pattern j that overlap in time shall be set within the following bounds unless stated otherwise:

PCMAX_L(p,q) ≤  PCMAX (p,q)  ≤  PCMAX_H (p,q)

When slots p and q have different transmissions lengths and belong to different cells on different or same bands:

PCMAX_L (p,q) = MIN {10 log10 [pCMAX_L,f,c(i),i (p) + pCMAX_L,f,c(i),j (q)], PPowerClass,CA, PEMAX,CA}

PCMAX_H (p,q) = MIN {10 log10 [pCMAX_ H,f,c(i),i (p) + pCMAX_ H,f,c(i),j (q)], PPowerClass,CA, PEMAX,CA}

where pCMAX_L,f,c (i),i  and pCMAX_ H,f,c(i),i  are the respective limits PCMAX_L,f,c (i),i and PCMAX_H,f,c(i),i expressed in linear scale.]

TREF and Teval are specified in Table 6.2A.4.1.2-1 when same and different slot patterns are used in aggregated carriers. For each TREF, the PCMAX_L is evaluated per Teval and given by the minimum value taken over the transmission(s) within the Teval; the minimum PCMAX_L over the one or more Teval is then applied for the entire TREF. The lesser of PPowerClass,CA and PEMAX,CA shall not be exceeded by the UE during any period of time.

Table 6.2A.4.1.2-1: PCMAX evaluation window for different slot and channel durations

If the UE is configured with multiple TAGs and transmissions of the UE on slot i for any serving cell in one TAG overlap some portion of the first symbol of the transmission on slot i +1 for a different serving cell in another TAG, the UE minimum of PCMAX_L for slots i and i + 1 applies for any overlapping portion of slots i and i + 1. The lesser of PPowerClass,CA and PEMAX,CA shall not be exceeded by the UE during any period of time.

The measured maximum output power PUMAX over all serving cells with same slot pattern shall be within the following range:

PCMAX_L  – MAX{TL, TLOW(PCMAX_L) }  ≤  PUMAX  ≤  PCMAX_H  +  THIGH(PCMAX_H)

PUMAX = 10 log10 ∑ pUMAX,c

where pUMAX,c  denotes the measured maximum output power for serving cell c expressed in linear scale. The tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX are specified in Table 6.2A.4.1.2-2. The tolerance TL is the absolute value of the lower tolerance for applicable NR CA configuration as specified in Table 6.2A.1.2-1 for intra-band carrier aggregation.

The measured maximum output power PUMAX over all serving cells, when at least one slot has a different transmission numerology or slot pattern, shall be within the following range:

P'CMAX_L–  MAX{TL, TLOW (P'CMAX_L)} ≤  P'UMAX  ≤  P'CMAX_H + THIGH (P'CMAX_H)

P'UMAX = 10 log10 ∑ p'UMAX,c

where p'UMAX,c  denotes the average measured maximum output power for serving cell c expressed in linear scale over TREF. The tolerances TLOW(P'CMAX) and THIGH(P'CMAX) for applicable values of P'CMAX are specified in Table 6.2A.4.1.2-2 for intra-band carrier aggregation. The tolerance TL is the absolute value of the lower tolerance for applicable NR CA configuration as specified in Table 6.2A.1.2-1 for intra-band carrier aggregation.

where:

P'CMAX_L  = MIN{ MIN {10log10∑( pCMAX_L,f,c(i),i), PPowerClass,CA} over all overlapping slots in TREF}

P'CMAX_H = MAX{ MIN{10 log10 ∑ pEMAX,c , PPowerClass,CA} over all overlapping slots in TREF}

Table 6.2A.4.1.2-2: PCMAX tolerance for uplink intra-band non-contiguous CA

## 6.2A.4.1.3Configured transmitted power for Inter-band CA

For uplink carrier aggregation the UE is allowed to set its configured maximum output power PCMAX,c for serving cell c and its total configured maximum output power PCMAX.

The configured maximum output power PCMAX,c  on serving cell c shall be set as specified in clause 6.2.4, except that the UE power class for serving cell c on the specific operating band shall be determined by the ue-PowerClassPerBandPerBC-r17 IE [7] as indicated for the band combination if signalled.

For uplink inter-band carrier aggregation, MPRc and A-MPRc apply per serving cell c and are specified in clause 6.2.2 and clause 6.2.3, respectively. P-MPR c accounts for power management for serving cell c. PCMAX,c  is calculated under the assumption that the transmit power is increased independently on all component carriers.

The total configured maximum output power PCMAX shall be set within the following bounds:

PCMAX_L ≤ PCMAX ≤ PCMAX_H

For uplink inter-band carrier aggregation with one serving cell c per operating band when same slot symbol pattern is used in all aggregated serving cells,

PCMAX_L = MIN {10log10∑ MIN [ pEMAX,c/ (tC,c),  pPowerClass.c/(MAX(mprc·∆mprc, a-mprc)·tC,c ·tIB,c·tRxSRS,c) , pPowerClass,c/pmprc], PEMAX,CA, PPowerClass,CA-ΔPPowerClass, CA}

PCMAX_H = MIN{10 log10 ∑ pEMAX,c , PEMAX,CA, PPowerClass,CA-ΔPPowerClass, CA}

where

-pEMAX,c is the linear value of PEMAX, c which is given by IE P-Max for serving cell c in [7];

-PPowerClass,CA is the maximum UE power specified in Table 6.2A.1.3-1, and Table 6.2A.1.3-3 for FRMCS in bands n100 and n101, without taking into account the tolerance specified in the Table 6.2A.1.3-1, and Table 6.2A.1.3-3 for FRMCS in bands n100 and n101; If the UE indicates higherPowerLimit-r17 for an UL inter-band CA configuration with uplink bands of different power class capabilities  specified in Table 6.2A.1.3-1  and ΔPPowerClass, CA = 0, PPowerClass,CA is replaced by 10 log10 ∑ pPowerClass,c.

-pPowerClass,c is the linear value of the maximum UE power for serving cell c specified in Table 6.2.1-1 according to ue-PowerClassPerBandPerBC-r17 if indicated or ue-PowerClass otherwise without taking into account the tolerance;

-For uplink inter-band UL carrier aggregation with a single uplink component carrier configured in any bands;

-If the UE indicates the support of higherPowerLimit-r17 for this band combination which is an eligible CA configuration as specified in Table 6.2A.1.3, and;

-If the UE further indicates support of powerBoosting-pi2BPSK-QPSK-Modified-r18 or powerBoosting-pi2BPSK-QPSK-r18 for any of the bands that comprise the band combination, pPowerClass,c is replaced by pPowerClass,c ∙ ∆pPowerBoost,c, for the one band for which IE powerBoostPi2BPSK-r18 or powerBoostQPSK-r18  is set to 1, where ∆pPowerBoost,c is linear value of ΔPPowerBoost.c as specified in 6.2.4, with the power class according to ue-PowerClassPerBandPerBC-r17 if indicated or ue-PowerClass otherwise.

-ΔPPowerClass,CA:

- For a power class 2 UE, it is 3 dB when the requirements of default power class are applied as specified in sub-clause 6.2.A.1.3; otherwise ΔPPowerClass, CA = 0 dB;

- For a power class 1.5 UE, it is 6 dB when the requirements of default power class are applied as specified in sub-clause 6.2.A.1.3; and it is 3 dB when the requirements of power class 2 are applied as specified in sub-clause 6.2.A.1.3; otherwise ΔPPowerClass, CA = 0 dB.

NOTE:UE reports ∆PPowerClass,CA when deltaPowerClassReporting-r18 is present, dpc-Reporting-FR1 [7] is configured and the reporting is triggered only by uplink duty cycle exceedance or by return to the powerClass after the duty cycle exceedance.

-mpr c and a-mpr c are the linear values of MPR c and A-MPR c as specified in clause 6.2.2 and clause 6.2.3, respectively;

-∆mpr c is the linear value of ∆MPR c as specified in clause 6.2.2;

-pmprc is the linear value of P-MPR c;

-∆tRxSRS,c  is the linear value of ∆TRxSRS,c;

-tC,c is the linear value of TC,ctC,c = 1.41 when NOTE 2 in Table 6.2A.1.3-1 applies for a serving cell c, otherwise tC,c = 1;

-tIB,c  is the linear value of the inter-band relaxation term TIB,c of the serving cell c as specified in clause 6.2A.4.2 for NR CA, clause 6.2C.2 for SUL, or TS 38.101-3 clause  6.2B.4.2 for EN-DC; otherwise tIB,c In case the UE supports more than one of band combinations for CA, SUL or DC, and an operating band belongs to more than one band combinations then

a)When the operating band frequency range is ≤ 1 GHz, the applicable additional TIB,c shall be the average value for all band combinations defined in clause 6.2A.4.2, 6.2C.2 in this specification and 6.2B.4.2 in TS 38.101-3 [3], truncated to one decimal place that apply for that operating band among the supported band combinations. In case there is a harmonic relation between low band UL and high band DL, then the maximum ∆TIB,c among the different supported band combinations involving such band shall be applied

b)When the operating band frequency range is > 1 GHz, the applicable additional ∆TIB,c shall be the maximum value for all band combinations defined in clause 6.2A.4.2, 6.2C.2 in this specification and 6.2B.4.2 in TS 38.101-3 [3] for the applicable operating bands.

-PEMAX,CA is the value indicated by p-NR-FR1 or by p-UE-FR1 whichever is the smallest if both are present.For uplink inter-band carrier aggregation with one serving cell c per operating band when at least one different numerology/slot pattern is used in aggregated cells, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of slot numerology type i, and its total configured maximum output power PCMAX.

The configured maximum output power PCMAX,c(i),i (p) in slot p of serving cell c(i) on slot numerology type i shall be set within the following bounds:

PCMAX_L,f,c(i),i (p) ≤  PCMAX,f,c(i), i (p) ≤  PCMAX_H,f,c(i),i (p)

where PCMAX_L,f,c (i),i (p) and PCMAX_H,f,c(i),i (p) are the limits for a serving cell c(i) of slot numerology type i as specified in clause 6.2.4, except that the UE power class for the serving cell c(i) on the specific operating band shall be determined by the ue-PowerClassPerBandPerBC-r17 IE [7] as indicated for the band combination if signalled.

The total UE configured maximum output power PCMAX (p,q) in a slot p of slot numerology or symbol pattern i,  and a slot q of slot numerology or symbol pattern j that overlap in time shall be set within the following bounds unless stated otherwise:

PCMAX_L(p,q) ≤  PCMAX (p,q)  ≤  PCMAX_H (p,q)

When slots p and q have different transmissions lengths and belong to different cells on different bands:

PCMAX_L (p,q) = MIN {10 log10 [pCMAX_L,f,c(i),i (p) + pCMAX_L,f,c(i),j (q)], PPowerClass,CA, PEMAX,CA}

PCMAX_H (p,q) = MIN {10 log10 [pCMAX_ H,f,c(i),i (p) + pCMAX_ H,f,c(i),j (q)], PPowerClass,CA, PEMAX,CA}

where pCMAX_L,f,c (i),i  and pCMAX_ H,f,c(i),i  are the respective limits PCMAX_L,f,c (i),i and PCMAX_H,f,c(i),i expressed in linear scale and pPowerClass,c is the linear value of the maximum UE power for serving cell c specified in Table 6.2.1-1 according to ue-PowerClassPerBandPerBC-r17 if indicated or ue-PowerClass otherwise without taking into account the tolerance; If the UE indicates higherPowerLimit-r17, PPowerClass,CA is replaced by 10 log10 ∑ pPowerClass,c.

For combinations of intra-band and inter-band carrier aggregation with UE configured for transmission on three serving cells (up to two contiguously aggregated carriers per operating band), the following apply:

The UE power class for the serving cell(s) on the operating band Bi including intra-band carrier aggregation shall be determined by the ue-PowerClassPerBandPerBC-r17 IE [7] as indicated for the band combination if signalled.

For the case when the UE indicates higherPowerLimit-r17, PPowerClass,CA is replaced by 10 log10 (pPowerClass,A + pPowerClass,CA,B).

Where

-pPowerClass,A is the linear value of the maximum UE power for serving cell c on the operating band A specified in Table 6.2.1-1 according to ue-PowerClassPerBandPerBC-r17 if indicated or ue-PowerClass otherwise without taking into account the tolerance;

-pPowerClass,CA,B is the linear value of the maximum UE power for serving cell(s) on the operating band B including intra-band carrier aggregation specified in Table 6.2F.1A.2-1 or Table 6.2A.1.1-1 according to ue-PowerClassPerBandPerBC-r17 if indicated or ue-PowerClass, otherwise without taking into account the tolerance.

For the case when p and q belong to the same band and k belongs to a different band, but p, q and k are of the same numerology and slot patterns.

PCMAX_L = MIN {10log10∑( pCMAX_L, Bi), PEMAX,CA, PPowerClass.CA }

PCMAX_H = MIN{10 log10 ∑ pEMAX,c , PEMAX,CA, PPowerClass.CA }

Where

-pCMAX_L, Bi is the linear values of PCMAX_L specified for the specific operating band Bi.

-The linear value of PCMAX_L specified for uplink intra-band contiguous carrier aggregation in subclause 6.2A.4.1.1 applies for operating band supporting two contiguous serving cells, designated by its band index Bi. The linear value of PCMAX_L specified for single carrier in subclause 6.2.4 applies for operating band Bj supporting one serving cell.

For the case when p and q belong to the same band and are of the same numerology i and slot patterns (p,q),while k belong to a different band and is of different numerology j and/or slot pattern on the 3rd cell then:

PCMAX_L (p,q,k) = MIN {10 log10 [pCMAX_L,Bi,i(p,q) + pCMAX_L,c(3),Bj,j(k)], PEMAX,CA, PPowerClass.CA }

PCMAX_H (p,q,k) = MIN {10 log10 [pCMAX_ H,Bi,i (p,q) + pCMAX_ H,c(3), Bj,j(k)], PEMAX,CA, PPowerClass.CA }

Where

-pEMAX,c is the linear value of PEMAX, c which is given by IE P-Max for serving cell c in [7];

-PEMAX,CA is p-UE-FR1 value signalled by RRC and defined in [38.331];

-PPowerClass.CA is the maximum UE power specified in Table 6.2A.1.3-1 without taking into account the tolerance specified in the Table 6.2A.1.3-1 or Table 6.2F.1A.1-1 for shared spectrum bands;

-pCMAX_L,c(3),Bj,j(k) and pCMAX_ H,c(3), Bj,j(k) are the linear values of PCMAX_L and PCMAX_H respectively, specified for single carrier in subclause 6.2.4 and applies for operating band supporting one serving cell in the Bj band on numerology j, using slot pattern k;

-pCMAX_L,Bi,i(p,q)  and pCMAX_ H,Bi,i (p,q) are the linear values of PCMAX_L respectively PCMAX_H for uplink intra-band contiguous carrier aggregation specified in subclause 6.2A.4.1.1 which applies for operating band Bi on numerology i, supporting two contiguous serving cells, using the same slot pattern (p,q).

TREF and Teval are specified in Table 6.2A.4.1.3-0 when same and different slot patterns are used in aggregated carriers. For each TREF, the PCMAX_L is evaluated per Teval and given by the minimum value taken over the transmission(s) within the Teval; the minimum PCMAX_L over the one or more Teval is then applied for the entire TREF. The lesser of PPowerClass,CA and PEMAX,CA shall not be exceeded by the UE during any period of time.

Table 6.2A.4.1.3-0: PCMAX evaluation window for different slot and channel durations

If the UE is configured with multiple TAGs and transmissions of the UE on slot i for any serving cell in one TAG overlap some portion of the first symbol of the transmission on slot i +1 for a different serving cell in another TAG, the UE minimum of PCMAX_L for slots i and i + 1 applies for any overlapping portion of slots i and i + 1. The lesser of PPowerClass,CA and PEMAX,CA shall not be exceeded by the UE during any period of time.

The measured maximum output power PUMAX over all serving cells with same slot pattern shall be within the following range:

PCMAX_L  – MAX{TL, TLOW(PCMAX_L) }  ≤  PUMAX  ≤  PCMAX_H  +  THIGH(PCMAX_H)

PUMAX = 10 log10 ∑ pUMAX,c

where pUMAX,c  denotes the measured maximum output power for serving cell c expressed in linear scale. The tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX are specified in Table 6.2A.4.1.3-1. The tolerance TL is the absolute value of the lower tolerance for applicable NR CA configuration as specified in Table 6.2A.1.3-1 for inter-band carrier aggregation.

The measured maximum output power PUMAX over all serving cells, when at least one slot has a different transmission numerology or symbol pattern, shall be within the following range:

P'CMAX_L–  MAX{TL, TLOW (P'CMAX_L)} ≤  P'UMAX  ≤  P'CMAX_H + THIGH (P'CMAX_H)

P'UMAX = 10 log10 ∑ p'UMAX,c

where p'UMAX,c  denotes the average measured maximum output power for serving cell c expressed in linear scale over TREF. The tolerances TLOW(P'CMAX) and THIGH(P'CMAX) for applicable values of P'CMAX are specified in Table 6.2A.4.1.3-1 for inter-band carrier aggregation. The tolerance TL is the absolute value of the lower tolerance for applicable NR CA configuration as specified in Table 6.2A.1.3-1 for inter-band carrier aggregation.

where:

P'CMAX_L  = MIN{ MIN {10log10∑( pCMAX_L,f,c(i),i), PPowerClass,CA} over all overlapping slots in TREF}

P'CMAX_H = MAX{ MIN{10 log10 ∑ pEMAX,c , PPowerClass,CA} over all overlapping slots in TREF}

If the UE indicates higherPowerLimit-r17, PPowerClass,CA is replaced by 10 log10 ∑ pPowerClass,c

Table 6.2A.4.1.3-1: PCMAX tolerance for uplink inter-band CA (two bands)

## 6.2A.4.1.4Void

## 6.2A.4.2ΔTIB,c for CA

For the UE which supports inter-band NR CA configuration, ΔTIB,c in tables below applies. Unless otherwise stated, ΔTIB,c is set to zero.

## 6.2A.4.2.1Void

## 6.2A.4.2.2Void

## 6.2A.4.2.3ΔTIB,c for Inter-band CA (two bands)

Table 6.2A.4.2.3-1: ΔTIB,c due to NR CA (two bands)

Table 6.2A.4.2.3-2: Void

Table 6.2A.4.2.3-3: Void

## 6.2A.4.2.4ΔTIB,c for Inter-band CA (three bands)

Table 6.2A.4.2.4-1: ΔTIB,c due to NR CA (three bands)

## 6.2A.4.2.5ΔTIB,c for Inter-band CA (four bands)

Table 6.2A.4.2.5-1: ΔTIB,c due to NR CA (four bands)

## 6.2A.4.2.6ΔTIB,c for Inter-band CA (five bands)

Table 6.2A.4.2.6-1: ΔTIB,c due to NR CA (five bands)

## 6.2A.4.2.7ΔTIB,c for Inter-band CA (six bands)

Table 6.2A.4.2.7-1: ΔTIB,c due to NR CA (six bands)

## 6.2BTransmitter power for NR-DC

## 6.2B.0General

The requirements apply for inter-band NR-DC with one uplink serving cell configured per CG.

## 6.2B.1UE maximum output power for NR-DC

For inter-band NR-DC with one uplink carrier assigned per NR band, the transmitter power requirements in clause 6.2 apply per band.

For inter-band NR-DC with one uplink assigned per band, the UE maximum output power shall be measured over all component carriers from different bands. If each band has separate antenna connectors, the maximum output power is defined as the sum of maximum output power from each UE antenna connector. The period of measurement shall be at least one sub frame (1 ms). The maximum output power is specified in Table 6.2B.1.3-1, and Table 6.2B.1.3-2 for FRMCS in bands n100 and n101.

Table 6.2B.1.3-1 UE Power Class for inter-band NR-DC

Table 6.2B.1.3-2: UE Power Class for uplink inter-band NR_DC for FRMCS in bands n100 and n101

## 6.2B.2UE maximum output power reduction for NR-DC

For inter-band NR-DC with one uplink assigned per band, the requirements in clause 6.2.2 or 6.2F.2 when the uplink belongs to a spectrum sharing defined band apply for each uplink component carrier.

When inter-band NR-DC is configured with intra-band contiguous carrier aggregation in one of the cell groups or both, the requirements in clause 6.2A.2 apply for each cell group configured with uplink contiguous carrier aggregation.

## 6.2B.3UE additional maximum output power reduction for NR-DC

For inter-band NR-DC with one uplink assigned per band, the requirements in clause 6.2.3 apply for each uplink component carrier.

For inter-band NR-DC with one uplink assigned per band, the requirements in clause 6.2.3 or 6.2F.3 when the uplink belongs to a spectrum sharing defined band apply for each uplink component carrier.

For inter-band NR-DC where the corresponding inter-band CA configuration is specified in Table 6.2A.3.1.3-1, the combined requirements and allowed A-MPR are applicable on both bands when both component carriers are active.

When inter-band NR-DC is configured with intra-band contiguous carrier aggregation in one of the cell groups or both, the requirements in clause 6.2A.3 or 6.2F.3A for shared spectrum defined bands, are applicable for each cell group configured with uplink contiguous carrier aggregation.

6.2B.4Configured output power for NR-DC

## 6.2B.4.1Configured transmitted power level for NR-DC

The UE is allowed to set its configured maximum output power PCMAX,f,c,MCG and PCMAX,f,c,SCG for the respective MCG and SCG and its total configured maximum output power for NR-DC operation   with  as specified in clause 7.6.2 of [8]. The UE is configured with an inter-CG power sharing mode by NR-DC-PC-mode.The requirements apply for one uplink serving cell configured per CG and for asynchronous and synchronous NR-DC if not otherwise stated.PTotalNR-DC=10log10(PTotalNR-DC)PTotalNR-DC

Unless otherwise stated, the configured maximum output power PCMAX,f,c,MCG (q) in physical-channel q for carrier f of serving cell c shall be set within the bounds if contained in the MCG,

PCMAX_L,f,c,MCG (q) ≤  PCMAX,f,c,MCG (q) ≤  PCMAX_H,f,c,MCG (q)

and the corresponding PCMAX_L,f,c,SCG (q) for a serving cell contained in the SCG,

PCMAX_L,f,c,SCG (q) ≤  PCMAX,f,c,SCG (q) ≤  PCMAX_H,f,c,SCG (q)

where PCMAX_L,f,c,MCG, PCMAX_H,f,c,MCG, PCMAX_L,f,c,SCG and PCMAX_H,f,c,SCG are the limits for a serving cell c as specified in clause 6.2.4 modified as follows:

PCMAX_L,f,c,MCG = MIN{MIN(PEMAX,c , PEMAX,NR-DC, PNR) – ∆TC,c, (PPowerClass,NR-DC – ΔPPowerClass,NR-DC) – MAX(MAX(MPRc+∆MPRc, A-MPRc)+ ΔTIB,c + ∆TC,c + ∆TRxSRS, P-MPRc)}

PCMAX_H,f,c,MCG = MIN{PEMAX,c, PEMAX,NR-DC, PNR, PPowerClass, NR-DC – ΔPPowerClass,NR-DC}

for the MCG and

PCMAX_L,f,c,SCG = MIN{MIN(PEMAX,c , PEMAX,NR-DC, PNR) – ∆TC,c, (PPowerClass,NR-DC – ΔPPowerClass,NR-DC) – MAX(MAX(MPRc+∆MPRc, A-MPRc)+ ΔTIB,c + ∆TC,c + ∆TRxSRS, P-MPRc)}

PCMAX_H,f,c,SCG = MIN{PEMAX,c, PEMAX,NR-DC, PNR, PPowerClass,NR-DC – ΔPPowerClass,NR-DC}

for the SCG, where

-PEMAX,NR-DC is the value given by the field p-UE-FR1 of the PhysicalCellGroupConfig IE for the MCG as defined in [7];

-PNR is the value given by the field p-NR-FR1 of the PhysicalCellGroupConfig IE as defined in [7];

-PPowerClass,NR-DC is the maximum UE power specified in Table 6.2B.1.3-1 without taking into account the tolerance specified in the Table 6.2B.1.3-1;

-∆TIB,c is the additional tolerance for serving cell c as specified in clause 6.2B.4.2 for NR-DC; ∆TIB,c = 0 dB otherwise;

-∆TC,c = 1.5dB when NOTE 2 in Table 6.2B.1.3-1 applies for a serving cell c, otherwise ∆TC,c = 0 dB ;

-∆MPRc for serving cell c is specified in clause 6.2.2.

-ΔPPowerClass,NR-DC = 0 dB for a power class 3 UE.

When MSG or SCG are configured with intra-band contiguous carrier aggregation, then intra-band carrier aggregation PCMAX,CA,MCG (q) and/or PCMAX,CA,SCG (q) in physical-channel q shall be set within the bounds:

PCMAX_L,CA, MCG (q) ≤  PCMAX,CA,MCG (q) ≤  PCMAX_H,CA,MCG (q)

for MSG, and/or

PCMAX_L,CA,SCG (q) ≤  PCMAX,CA,SCG (q) ≤  PCMAX_H,CA,SCG (q)

for SCG, where PCMAX_L,CA,MCG, PCMAX_H,CA,MCG, PCMAX,CA,SCG and PCMAX_H,CA,SCG are the limits for a carrier aggregation uplink as specified in clause 6.2A.4.1.1 modified as follows:

PCMAX_L,CA,MCG = MIN{10 log10 ∑ pEMAX,c  - TC , PEMAX,CA, PEMAX,NR-DC, PNR,MCG, (PPowerClass,NR-DC – ΔPPowerClass,NR-DC)  – MAX(MAX(MPR, A-MPR) + ΔTIB,c + TC + TRxSRS, P-MPRc ) }

PCMAX_H,CA,MCG  = MIN{10 log10 ∑ pEMAX,c , PEMAX,CA , PEMAX,NR-DC, PNR,MCG, PPowerClass,NR-DC – ΔPPowerClass,NR-DC }

for the MCG, and

PCMAX_L,CA,SCG = MIN{10 log10 ∑ pEMAX,c  - TC , PEMAX,CA, PEMAX,NR-DC, PNR,SCG, (PPowerClass,NR-DC – ΔPPowerClass,NR-DC)  – MAX(MAX(MPR, A-MPR) + ΔTIB,c + TC + TRxSRS, P-MPRc ) }

PCMAX_H,CA,SCG  = MIN{10 log10 ∑ pEMAX,c , PEMAX,CA , PEMAX,NR-DC, PNR,SCG, PPowerClass,NR-DC – ΔPPowerClass,NR-DC}

for SCG.

For a UE provided with NR-DC-PC-mode = Semi-static-mode1,

= MIN{PEMAX, NR-DC, PPowerClass,NR-DC} + 0.3 dBPTotalNR-DC

with PPowerClass,NR-DC set to power class 3 in case the UE indicates a higher power class in any CG. The UE determines the maximum transmission power for the MCG and the SCG using the respective configured maximum power PCMAX,f,c,MCG and PCMAX,f,c,SCG.

If for synchronous NR-DC operation a UE is provided NR-DC-PC-mode = Semi-static-mode2, the  is determined as above and PTotalNR-DC

-if at least one symbol of slot  of the MCG/SCG is indicated as uplink or flexible to a UE by tdd-UL-DL-ConfigurationCommon and tdd-UL-DL-ConfigurationDedicated, if provided, overlaps with a symbol for any ongoing transmission overlapping with slot  of the SCG/MCG, the UE determines a maximum power for the transmission on the SCG/MCG overlapping with slot  using the configured maximum power PCMAX,f,c,SCG or PCMAX,f,c,MCG for the SCG or MSG, respectively, i1i2i2

-otherwise (i.e. an ongoing transmission overlapping with slot  of the SCG/MCG overlaps with only semi-static downlink symbols within slot  of the MCG/SCG), the UE determines a maximum power for the transmission on MCG or the SCG overlapping with slot  using the configured maximum power as specified in clause 6.2.4.i2i1i2

If a UE indicates a capability for dynamic power sharing between the MCG and the SCG and is provided with NR-DC-PC-mode = Dynamic,

= MIN{PEMAX, NR-DC, PPowerClass,NR-DC}PTotalNR-DC

with PPowerClass,NR-DC set to power class 3 in case the UE indicates a higher power class in any CG. The UE determines the maximum transmission power for the MCG and the SCG using the respective configured maximum power PCMAX,f,c,MCG and PCMAX,f,c,SCG except

-if UE transmission(s) in slot  of the MCG or in slot  of the SCG do not overlap in time with any UE transmission(s) on the SCG or the MCG, respectively, the UE determines a maximum transmission power in slot  of the MCG or in slot  of the SCG using the configured maximum power as specified in clause 6.2.4.i1i2i1i2

If a UE indicates a capability to determine a total transmission power on the SCG at a first symbol of a transmission occasion on the SCG by determining transmissions on the MCG as specified in clause 7.6.2 of [8], and is provided with NR-DC-PC-mode = Dynamic,

= MIN{PEMAX, NR-DC, PPowerClass,NR-DC}PTotalNR-DC

with PPowerClass,NR-DC set to power class 3 in case the UE indicates a higher power class in any CG. The UE determines the maximum transmission power for the MCG and the SCG using the respective configured maximum power PCMAX,f,c,MCG and PCMAX,f,c,SCG.

The measured total maximum output power PUMAX over both CGs measured over the transmission reference time duration is

PUMAX = 10 log10 (pUMAX,c,MCG + pUMAX,c,SCG),

where pUMAX,c,MSG and pUMAX,c,SCG denote the measured output power of serving cells c contained in the respective MSG and SCG expressed in linear scale.

The measured total configured maximum output power PUMAX shall be within the following bounds:

PCMAX_L -TLOW (PCMAX_L)  ≤  PUMAX  ≤  PCMAX_H + THIGH (PCMAX_H)

with the tolerances TLOW(PCMAX_H) and THIGH(PCMAX_H) for applicable values of PCMAX specified in Table 6.2B.4.1.3-2.

When a subframe p on the MSG overlap with a physical-channel q on the SCG, then for PUMAX evaluation, the subframe p on the MCG is taken as reference period TREF and always considered as the reference measurement duration and the following rules are applicable.

TREF and Teval are specified in Table 6.2B.4.1.3-1 when same or different subframe and physical-channel durations are used on the carriers. The PPowerClass shall not be exceeded by the UE during any evaluation period of time.

Table 6.2B.4.1.3-1: PCMAX evaluation window

For each TREF, the PCMAX_H is evaluated per Teval and given by the maximum value over the transmission(s) within the Teval as follows:

PCMAX_H  = MAX{PCMAX_NR-DC_H(p,q), PCMAX_NR-DC_H(p,q+1), … , PCMAX_NR-DC_H(p,q+n)}

where PCMAX_NR-DC_H entries are the applicable upper limits for each overlapping scheduling unit pairs (p,q), (p, q+1), up to (p, q+n) for each applicable Teval duration, where q+n is the last physical-channel on the SCG overlapping with subframe p on the MCG, while PCMAX_L is computed as follows:

PCMAX_L = MIN{PCMAX_NR-DC_L(p,q), PCMAX_NR-DC_L(p,q+1), … , PCMAX_NR-DC_L(p,q+n)}

where PCMAX_NR-DC_L entries are the applicable lower limits for each overlapping scheduling unit pairs (p,q), (p, q+1) up to (p, q+n) for each applicable Teval duration, where q+n is the last physical-channel on the SCG overlapping with subframe p on the MCG.

For a UE provided with NR-DC-PC-mode = Semi-static-mode1 and configured with pNR,MCG + pNR,SCG ≤  with pNR,MCG and pNR,SCG the values of the PNR for the respective MCG and SCG expressed in linear scalePTotalNR-DC

PCMAX_NR-DC_L(p,q) = 10 log10 [pCMAX_L, MCG (p) + pCMAX_L, SCG (q)]

PCMAX_NR-DC_H(p,q) = 10 log10 [pCMAX_H, MCG (p) + pCMAX_H, SCG (q)]

where

pCMAX_L, MCG, pCMAX_L, SCG, pCMAX_H, MCG, pCMAX_H, SCG  can be  pCMAX_L,f,c,MCG, pCMAX_H,f,c,MCG, pCMAX_L,f,c,SCG, and pCMAX_H,f,c,SCG the values of the respective PCMAX_L,f,c,MCG, PCMAX_H,f,c,MCG, PCMAX_L,f,c,MCG, and PCMAX_H,f,c,SCG expressed in linear scale, or pCMAX_L,CA,MCG, pCMAX_H,CA,MCG, pCMAX_L,CA,SCG, and pCMAX_H,CA,SCG the values of the respective PCMAX_L,CA,MCG, PCMAX_H,CA,MCG, PCMAX_L,CA,SCG, and PCMAX_H,CA,SCG expressed in linear scale if the contiguous carrier aggregation is configured in MCG and/or SCG or a combinations of single cell and carrier aggregation while the measured configured maximum power PUMAX  for each CG shall meet the requirements as specified in clause 6.2.4 but with bounds for PCMAX,f,c,MCG (p) and PCMAX,f,c,SCG  as specified in this clause or 6.2A.4.1.1 as modified in this clause for contiguous carrier aggregation configured cell group.

If for synchronized NR-DC a UE is provided with NR-DC-PC-mode = Semi-static-mode2 and configured with pNR,MCG + pNR,SCG ≤  with pNR,MCG and pNR,SCG the linear-scale values of the PNR for the respective MCG and SCGPTotalNR-DC

PCMAX_NR-DC_L(p,q) = 10 log10 [pCMAX_L, MCG (p) + pCMAX_L, SCG (q)]

PCMAX_NR-DC_H(p,q) = 10 log10 [pCMAX_H, MCG (p) + pCMAX_H, SCG (q)]

while the measured configured maximum power PUMAX for each CG shall meet the requirements specified in Table 6.2.4-2 but with bounds for PCMAX,f,c,MCG (p) and PCMAX,f,c,SCG(q)  as specified in this clause or 6.2A.4.1.1-1when intra-band carrier aggregation contiguous is configured in the MCG and/or SCG with the bounds PCMAX,CA,MCG (p) and PCMAX,CA,SCG  defined in this clause except

-if an ongoing transmission overlapping with physical channel q of the SCG or subframe p of the MCG overlaps with only semi-static downlink symbols within the respective subframe p of the MCG or physical channel q of the SCG as indicated to a UE by tdd-UL-DL-ConfigurationCommon and tdd-UL-DL-ConfigurationDedicated, if provided,

then the measured configured maximum power PUMAX for the transmission subframe p on the MCG or physical channel q on the SCG shall meet the requirements as specified in clause 6.2.4 and with bounds for PCMAX,f,c,MCG (p) or PCMAX,f,c,SCG  as specified in this clause  or Table 6.2A.4.1.1-1when intra-band carrier aggregation contiguous is configured in the MCG and/or SCG with  bounds for PCMAX,CA,MCG (p) and PCMAX,CA,SCG  defined in this clause For a UE provided with NR-DC-PC-mode = Dynamic,

PCMAX_NR-DC_L(p,q) = MIN{10 log10 [pCMAX_L, MCG (p) + pCMAX_L, SCG (q)], }PTotalNR-DC

PCMAX_NR-DC_H(p,q) = MIN{10 log10 [pCMAX_H, MCG (p) + pCMAX_H, SCG (q)], }PTotalNR-DC

while the measured configured maximum power PUMAX on the MCG shall meet the requirements as specified in clause 6.2.4-2 but with bounds for PCMAX,f,c,MCG (p) as specified in this clause, or as specified in Table 6.2A.4.1.1-1 when intra-band carrier aggregation contiguous is configured in the MCG with the bounds for PCMAX,CA,MCG (p) as specified in this clause and the PUMAX on the SCG shall be within

PCMAX_L,  –  MAX{TL,c, T(PCMAX_L,)}  ≤  PUMAX  ≤  PCMAX_H  +  T(PCMAX_H,f,c)

where for single uplink cell SCG

PCMAX_L = MIN{PCMAX_L,f,c,SCG (p), 10 log10 ( – pNR,MSG)}PTotalNR-DC

PCMAX_H = MIN{PCMAX_H,f,c,SCG (p), 10 log10 ( – pNR,MSG)}PTotalNR-DC

and for intra-band carrier aggregation configured SCG

PCMAX_L = MIN{PCMAX_L,CA,SCG (p), 10 log10 ( – pNR,MSG)}PTotalNR-DC

PCMAX_H = MIN{PCMAX_H,CA,SCG (p), 10 log10 ( – pNR,MSG)}PTotalNR-DC

where PCMAX_L,CA,SCG and PCMAX_H,CA,SCG bounds are defined in this clause,

with limits as specified in Table 6.2.4-2 or as specified in Table 6.2A.4.1.1-1 when intra-band carrier aggregation contiguous is configured in the MCG and pNR,MCG the value of the PNR for the MCG expressed in linear scale.

Table 6.2B.4.1.3-2: PCMAX tolerance for NR-DC

## 6.2B.4.2ΔTIB,c for NR-DC

For inter-band NR-DC with one uplink carrier assigned per NR band, the ΔTIB,c for the corresponding inter-band CA configuration as specified in clause 6.2A.4.2 applies.

## 6.2CTransmitter power for SUL

## 6.2C.1Configured transmitted power for SUL

When a UE is configured with both NR UL and NR SUL carriers in a serving cell with active transmission either on the UL carrier(s) or SUL carrier, the configured transmit power requirements specified in the following clauses apply:

-clause 6.2A.4.1.1 if the NR UL is configured with intra-band contiguous CA;

-clause 6.2D.4 if the NR UL or NR SUL is configured with MIMO;

-clause 6.2G.4 if the NR UL or NR SUL supports TxDiversity;

-clause 6.2.4 otherwise.

If a UE supports a different power class than the default UE power class for NR UL/SUL band of SUL combination and the supported power class enables the higher maximum output power for SUL combination than that of the default power class:

–if the field of UE capability maxUplinkDutyCycle-SULcombination-PC2 is not absent and the average percentage of uplink symbols transmitted in a certain evaluation period is larger than the maximum percentage of uplink symbols that the UE indicates by maxUplinkDutyCycle-SULcombination-PC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

–if the IE P-Max as defined in TS 38.331 [7] is provided and set to 23 dBm or lower;

–shall apply all requirements for the default power class to the supported power class and set the configured transmitted power as specified in clause 6.2.4, clause 6.2D.4 or clause 6.2G.4 with ΔPPowerClass = 3dB,

or clause 6.2A.4.1.1 with ΔPPowerClass,CA = 3dB;

–else;

–shall apply all requirements for the supported power class and set the configured transmitted power as specified in clause 6.2.4 or clause 6.2D.4 or clause 6.2G.4 with ΔPPowerClass = 0dB or clause 6.2A.4.1.1 with ΔPPowerClass,CA = 0 dB (regardless of the average percentage of uplink symbols if the field of UE capability maxUplinkDutyCycle-SULcombination-PC2 is absent).

The average percentage of uplink symbols is defined as 50%  ( DutyNR, x /maxDutyNR,x + DutyNR, y /maxDutyNR,y, ). DutyNR, x, DutyNR, y represent the actual percentage of uplink symbols transmitted in the same evaluation period (The exact evaluation period is no less than one radio frame) for NR Band x, NR Band y respectively maxDutyNR,x, maxDutyNR,y represent the field of UE capability maxUplinkDutyCycle-PC2-FR1 per band as defined in TS 38.331.  For NR Band x or NR Band y,

–if power class of one or both of the bands within the band combination is power class 2 and the corresponding UE capability maxUplinkDutyCycle-PC2-FR1 is absent;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 50%;

–if the IE P-Max as defined in TS 38.331 [7] is provided for one of the bands and set to 23 dBm or lower or UE indicates power class 3 for one of the bands;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 100%.

–else if power class of one or both of the bands within the band combination is power class 2 and the corresponding UE capability maxUplinkDutyCycle-PC2-FR1 is absent;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 50%.

## 6.2C.2ΔTIB,c

For the UE which supports SUL band combination, ΔTIB,c in Tables below applies. Unless otherwise stated, ΔTIB,c is set to zero.

Table 6.2C.2-1: ΔTIB,c due to SUL

Table 6.2C.2-2: ΔTIB,c for SUL band combination (Three bands)

Table 6.2C.2-3: ΔTIB,c for SUL band combination (Four bands)

## 6.2DTransmitter power for UL MIMO

## 6.2D.1UE maximum output power for UL MIMO

For UE with multiple transmit antenna connectors up to a maximum of four in closed-loop spatial multiplexing scheme, the maximum output power for any transmission bandwidth within the channel bandwidth is specified in Table 6.2D.1-1. The requirements shall be met with the UL MIMO configurations specified in Table 6.2D.1-2. For UE supporting UL MIMO, the maximum output power is defined as the sum of the maximum output power from all UE antenna connectors. The period of measurement shall be at least one sub frame (1 ms).

The requirements shall be met with the UL MIMO configurations of using 2-layer UL MIMO codebook-based transmission with precoding matrix of W=, 3-layer UL MIMO codebook-based transmission with precoding matrix of  or 4-layer UL MIMO transmission with codebook of . DCI Format for UE configured in PUSCH transmission mode for uplink single-user MIMO shall be used.W=13100010001

Table 6.2D.1-1: UE Power Class for UL MIMO in closed loop spatial multiplexing scheme

Table 6.2D.1-2: UL MIMO configuration in closed-loop spatial multiplexing scheme

For UE support uplink full power transmission (ULFPTx) for UL MIMO, the maximum output power requirements specified in Table 6.2D.1-1 shall be met with the PUSCH configurations specified in Table 6.2D.1-3, based upon UE’s support of uplink full power transmission mode. For UE supporting uplink full power transmission (ULFPTx) for UL MIMO, the maximum output power is defined as the sum of the maximum output power from all UE antenna connectors. The period of measurement shall be at least one sub frame (1 ms).

Table 6.2D.1-3: PUSCH Configuration for uplink full power transmission (ULFPTx)

If the UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.2 apply for at least one antenna connector for the power class as indicated by the ue-PowerClass field in capability signalling with the following exception: for UEs indicating Tx diversity capability, the requirements in clause 6.2G for the power class indicated by the ue-PowerClass.

A UE with 2Tx indicating the feature ul-FullPwrMode-r16 or ul-FullPwrMode2-TPMIGroup-r16 for a band shall meet the requirement in clause 6.2 for at least one antenna connector when scheduled for single antenna-port transmission by DCI format 0_0 or by DCI format 0_1 for codebook-based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211].

## 6.2D.2UE maximum output power reduction for UL MIMO

For UE with multiple transmit antenna connectors, up to a maximum of four, in closed-loop spatial multiplexing scheme, the allowed Maximum Power Reduction (MPR) for the maximum output power in Table 6.2D.1-1 is specified in Table 6.2.2-1 for PC3, Table 6.2D.2-1 for 2Tx PC2 when the UE does not indicate ul-FullPwrMode-r16 or ul-FullPwrMode2-TPMIGroup-r16 for the band and Table 6.2.2-2 for 2Tx PC2 when the UE indicates ul-FullPwrMode-r16 or ul-FullPwrMode2-TPMIGroup-r16 for the band, Table 6.2D.2-2 and Table 6.2D.2-3 for PC1.5 with 2Tx, Table 6.2D.2-4, 6.2D.2-5 for PC1.5 with 4 Tx respectively. For PC2 UE with 3Tx, the allowed MPR for the maximum output power in Table 6.2D.1-1 is specified in Table 6.2D.2-1 when the UE does not indicate ul-FullPwrMode-r16, ul-FullPwrMode1-r16 or ul-FullPwrMode2-TPMIGroup-r16 for the band and Table 6.2.2-2 when the UE indicates ul-FullPwrMode-r16 for the band. For UE power class 1.5 with 2Tx, the allowed maximum power reduction (MPR) defined in Table 6.2D.2-3 is in accordance with the indicated modifiedMPR-Behaviour specified in Table L.1-1 for channel bandwidths ≤ 100 MHz. The requirements shall be met with UL MIMO configurations defined in Table 6.2D.1-2. For UE supporting UL MIMO, the maximum output power is defined as the sum of the maximum output power from both UE antenna connectors.

For UE support uplink full power transmission (ULFPTx) for UL MIMO except the feature ul-FullPwrMode-r16 or ul-FullPwrMode2-TPMIGroup-r16, the allowed MPR for the maximum output power in Table 6.2D.1-1 is specified in Table 6.2.2-1 for PC3, Table 6.2D.2-1 when TxD is indicated and Table 6.2.2-2  when TxD is not indicated for PC2 , Table 6.2D.2-2 and Table 6.2D.2-3 for PC1.5 with 2Tx, Table 6.2D.2-4, 6.2D.2-5 for PC1.5 with 4 Tx respectively, and the requirements shall be met with the PUSCH configurations specified in Table 6.2D.1-3, based upon UE’s support of uplink full power transmission mode. A UE with 2Tx indicating the feature ul-FullPwrMode-r16 or ul-FullPwrMode2-TPMIGroup-r16 for a band shall meet the maximum output power requirement with MPR according to clause 6.2.2. When a UE that indicates PC1.5 for a given band is limited to PC2 by the rules in clause 6.2.1, the MPR requirements in Table 6.2.2-2 apply. For UE support uplink full power transmission (ULFPTx) for UL MIMO, the maximum output power is defined as the sum of the maximum output power from all UE antenna connectors.

The same MPR requirements shall be applicable to UE with 1-layer UL MIMO transmission (either with or without ULPFTx) as with the UL MIMO configurations of using 2-layer UL MIMO transmission with codebook of.

For the UE maximum output power modified by MPR, the power limits specified in clause 6.2D.4 apply.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission, the corresponding requirements in clause 6.2D.1 apply for the power class as indicated by the ue-PowerClass field in capability signaling. A UE indicating the feature ul-FullPwrMode-r16 or ul-FullPwrMode2-TPMIGroup-r16 for a band shall meet the requirement in clause 6.2 with MPR according to clause 6.2.2 for at least one antenna connector when scheduled for single antenna-port transmission by DCI format 0_0 or by DCI format 0_1 for codebook-based transmission on a single antenna port with precoding matrix W=1 [6.3.1.5 TS 38.211].

Unless otherwise specified, ‘pi/2 BPSK’ refers to both variants of pi/2 BPSK referenced in Table 6.2.2-1 and table 6.2.2-1a.

Table 6.2D.2-1: Maximum power reduction (MPR) for power class 2 with 2Tx or 3Tx

Table 6.2D.2-2: Maximum power reduction (MPR) for power class 1.5 with 2Tx

Table 6.2D.2-3: Maximum power reduction (MPR) for power class 1.5 with 2Tx

Table 6.2D.2-4: Maximum power reduction (MPR) for power class 1.5 with 4 Tx

Table 6.2D.2-5: Maximum power reduction (MPR) for power class 1.5 with 4 Tx

Inner, outer and edge allocations are as defined in section 6.2.2 except for PC1.5 edge allocations which is for LCRB ≤ 4 RBs instead of LCRB ≤ 2 RBs for other power classes.

If all of the following conditions are simultaneously met:

-The UE is a PC2 2Tx UE operating in any channel bandwidth except 3MHz or 7MHz

-The UE indicates support for mpr-SingleCC-SingleValue-r19 or mpr-SingleCC-MultipleValue-r19, and is configured with the IE mprReductionExtensionRatio-r19

-The uplink modulation order is either QPSK or 16QAM

-When no A-MPR is applicable

then:

The inner, outer and edge allocations definition for mpr-SingleCC-SingleValue-r19 or mpr-SingleCC-MultipleValue-r19 in clause 6.2.2 applies.

## 6.2D.3UE additional maximum output power reduction for UL MIMO

For UE with two or four transmit antenna connectors in closed-loop spatial multiplexing scheme, the A-MPR values specified in clause 6.2.3 shall apply to the maximum output power specified in Table 6.2D.1-1. The requirements shall be met with the UL MIMO configurations specified in Table 6.2D.1-2. For UE supporting UL MIMO, the maximum output power is defined as the sum of the maximum output power from all UE antenna connector. Unless stated otherwise, an A-MPR of 0 dB shall be used.

For UE support uplink full power transmission (ULFPTx) for UL MIMO, the A-MPR values specified in clause 6.2.3 shall apply to the maximum output power specified in Table 6.2D.1-1. The requirements shall be met with the PUSCH configurations specified in Table 6.2D.1-3, based upon UE’s support of uplink full power transmission mode. For UE support uplink full power transmission (ULFPTx) for UL MIMO, the maximum output power is defined as the sum of the maximum output power from all UE antenna connector.

For the UE maximum output power modified by A-MPR, the power limits specified in clause 6.2D.4 apply.

If the UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook-based transmission, the corresponding requirements in clause 6.2D.1 apply for the power class as indicated by the ue-PowerClass field in capability signaling. A UE with 2Tx indicating the feature ul-FullPwrMode-r16 or ul-FullPwrMode2-TPMIGroup-r16 for a band shall meet the requirement in clause 6.2 for at least one connector with A-MPR according to clause 6.2.3 when scheduled for single antenna-port transmission by DCI format 0_0 or by DCI format 0_1 for codebook-based transmission on a single antenna port with precoding matrix W=1 [6.3.1.5 TS 38.211].

## 6.2D.4Configured transmitted power for UL MIMO

For UE supporting UL MIMO, the transmitted power is configured per each UE.

The definitions of configured maximum output power PCMAX,c, the lower bound PCMAX_L,c, and the higher bound PCMAX_H,c specified in clause 6.2.4 shall apply to UE supporting UL MIMO, where

-PPowerClass, ΔPPowerClass , ΔPPowerBoost and ∆TC,c are specified in clause 6.2.4 unless otherwise stated;

-MPRc is specified in clause 6.2D.2;

-A-MPRc is specified in clause 6.2D.3.

The measured configured maximum output power PUMAX,c for serving cell c shall be within the following bounds:

PCMAX_L,c  –  MAX{TL, T LOW(PCMAX_L,c)}  ≤  PUMAX,c  ≤  PCMAX_H,c  +  T HIGH(PCMAX_H,c)

where TLOW(PCMAX_L,c) and THIGH(PCMAX_H,c) are defined as the tolerance and applies to PCMAX_L,c and PCMAX_H,c separately, while TL is the absolute value of the lower tolerance in Table 6.2D.1-1 for the applicable operating band.

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the tolerance is specified in Table 6.2D.4-1. For UE with 3 transmit antenna connectors in closed-loop spatial multiplexing scheme, the tolerance is specified in Table 6.2D.4-1a. For UE with four transmit antenna connectors in closed-loop spatial multiplexing scheme, the tolerance is specified in Table 6.2D.4-2. The requirements shall be met with UL MIMO configurations specified in Table 6.2D.1-2.

For UE support uplink full power transmission (ULFPTx) for UL MIMO, the tolerance is specified in Table 6.2D.4-1. The requirements shall be met with the PUSCH configurations specified in Table 6.2D.1-3, based upon UE’s support of uplink full power transmission mode.

Table 6.2D.4-1: PCMAX,c tolerance in closed-loop spatial multiplexing scheme for 2Tx

Table 6.2D.4-1a: PCMAX,c tolerance in closed-loop spatial multiplexing scheme for 3Tx

Table 6.2D.4-2: PCMAX,c tolerance in closed-loop spatial multiplexing scheme for 4Tx

If the UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook-based transmission, the corresponding requirements in clause 6.2D.1 apply for the power class as indicated by the ue-PowerClass field in capability signaling.

## 6.2ETransmitter power for V2X

## 6.2E.1UE maximum output power for V2X

## 6.2E.1.1General

When NR V2X UE is configured for NR V2X sidelink transmissions non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, the allowed NR V2X UE maximum output power is specified in Table 6.2E.1.1-0.

Table 6.2E.1.1-0: NR V2X UE Power Class

When a UE is configured for NR V2X sidelink transmissions in NR Band n47, the V2X UE shall meet the following additional requirements for transmission within the frequency ranges 5855-5925 MHz:

-The maximum mean power spectral density shall be restricted to 23 dBm/MHz EIRP when the network signaling value NS_33 is indicated.

where the network signaling values are specified in clause 6.2E.3.

NOTE:The PSD limit in EIRP shall be converted to conducted requirement depend on the supported post antenna connector gain Gpost connector declared by the UE following the principle described in annex I in [11].

For NR V2X UE supporting SL MIMO or Tx diversity, the maximum output power requirements in Table 6.2E.1.1-1 is defined as the sum of the maximum output power from each UE antenna connector. The period of measurement shall be at least one sub frame (1 ms).

Table 6.2E.1.1-1: NR V2X UE Power Class for SL-MIMO

If the UE transmits on one antenna connector at a time, the requirements in Table 6.2E.1.1-0 shall apply to the active antenna connector.

## 6.2E.1.1AVoid

## 6.2E.1.2UE maximum output power for V2X concurrent operation

For the inter-band NR V2X concurrent operation, the maximum output power is specified in Table 6.2E.1.2-1 for each operating band. The period of measurement shall be at least one sub frame (1ms).

Table 6.2E.1.2-1: Power Class for NR V2X inter-band concurrent combination (two bands)

For the intra-band concurrent NR V2X operation, the maximum output power is specified in Table 6.2E.1.2-2. The period of measurement shall be at least one sub frame (1ms).

Table 6.2E.1.2-2: NR V2X UE Power Class for intra-band concurrent combination

## 6.2E.1AUE maximum output power for Sidelink CA

For SL intra-band contiguous carrier aggregation, the maximum output power is specified in Table 6.2E.1A-1. For SL intra-band non-contiguous carrier aggregation with two sidelink carriers, the maximum output power is specified in Table 6.2E.1A-2.

Table 6.2E.1A-1: UE Power Class for SL intra-band contiguous CA

Table 6.2E.1A-2: UE Power Class for SL intra-band non-contiguous CA

## 6.2E.1FUE maximum output power for Sidelink Unlicensed

## 6.2E.1F.1General

The following UE Power Classes define the maximum output power for any transmission bandwidth within the channel bandwidth of shared spectrum channel access carrier unless otherwise stated. The period of measurement shall be at least one sub frame (1ms).

Table 6.2E.1F-1: UE Power Class

The UE operating shall meet the following additional requirements for maximum mean transmission power density specified in Table 6.2E.1F-2 when NS is signaled and when transmission overlaps with any portion of the specified frequency range.  In case transmission overlaps multiple frequency ranges, the lowest power density requirement applies.

Table 6.2E.1F-2: Additional requirements for transmit power density

## 6.2E.1.2FVoid

## 6.2E.1F.2UE Maximum output power for SL-U concurrent operation

For the inter-band NR SL-U concurrent operation, the maximum output power is specified in Table 6.2E.1F.2-1 for each operating band. The period of measurement shall be at least one sub frame (1ms).

Table 6.2E.1F.2-1:NR UE Power Class for inter band SL-U concurrent combination

## 6.2E.2UE maximum output power reduction for V2X

## 6.2E.2.1General

When UE is configured for NR V2X sidelink transmissions non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, this clause specifies the allowed Maximum Power Reduction (MPR) power for V2X physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

## 6.2E.2.1AMPR for sidelink CA

## 6.2E.2.1A.1MPR for sidelink intra-band contiguous CA

For SL intra-band contiguous CA of PSCCH and PSSCH simultaneous transmission with contiguous RB allocation, the allowed MPR for the maximum output power are specified in Table 6.2E.2.1A.1-1 for UE power class 3. The MPR with contiguous RB allocation is specified in Table 6.2E.2.1A.1-2 for power class 2 when the signalling is absent for dualPA-Architecture IE. The MPR with contiguous RB allocation is specified in Table 6.2E.2.1A.1-3 for power class 2 with TxD supported.

Table 6.2E.2.1A.1-1: MPR for power class 3 SL CA with contiguous RB allocation

Table 6.2E.2.1A.1-2: MPR for power class 2 SL CA with contiguous RB allocation

Table 6.2E.2.1A.1-3: MPR for power class 2 SL CA with contiguous RB allocation with 2Tx

The contiguous allocation rule of inner and outer for SL intra-band contiguous CA refers to that for NR intra-band contiguous CA in 6.2A.2.1 in TS38.101-1.

For SL intra-band contiguous CA of PSCCH and PSSCH simultaneous transmission with non-contiguous RB allocation, the allowed MPR for the maximum output power are specified in Table 6.2E.2.1A.1-4 for UE power class 3. The MPR with non-contiguous RB allocation is specified in Table 6.2E.2.1A.1-5 for power class 2 when the signalling is absent for dualPA-Architecture IE. The MPR with non-contiguous RB allocation is specified in Table 6.2E.2.1A.1-6 for power class 2 with TxD supported.

Table 6.2E.2.1A.1-4: MPR for power class 3 SL CA with non-contiguous RB allocation

Table 6.2E.2.1A.1-5: MPR for power class 2 SL CA with non-contiguous RB allocation

Table 6.2E.2.1A.1-6: MPR for power class 2 SL CA with non-contiguous RB allocation with 2Tx

The non-contiguous allocation rule of inner, outer1, and outer2 for SL intra-band contiguous CA refers to that for NR intra-band contiguous CA in 6.2A.2.1 in TS38.101-1.

For SL intra-band CA of PSFCH with single RB transmission on each carrier, the required MPR are specified as Table 6.2E.2.1A.1-7 for UE power class 3. The MPR is specified in Table 6.2E.2.1A.1-8 for power class 2 when the signalling is absent for dualPA-Architecture IE. The MPR is specified in Table 6.2E.2.1A.1-9 for power class 2 with TxD supported.

Table 6.2E.2.1A.1-7: PSFCH MPR for power class 3 intra-band SL CA

Table 6.2E.2.1A.1-8: PSFCH MPR for power class 2 intra-band SL CA

Table 6.2E.2.1A.1-9: PSFCH MPR for power class 2 intra-band SL CA with 2Tx

Where,

R is the ratio of the gap bandwidth between the two PSFCH transmitted on the two intra-band carrier by the total bandwidth of the two carrier.

When single S-SSB is transmitted on intra-band contiguous carriers, required MPR for single cell V2X in Table 6.2E.2.2-1 and Table 6.2E.2.2-2 is reused for UE power class 3 and for UE power class 2 respectively. For two S-SSB transmissions on intra-band contiguous carriers, the required MPR are specified as Table 6.2E.2.1A.1-10 for UE power class 3. The MPR is specified in Table 6.2E.2.1A.1-11 for power class 2 when the signalling is absent for dualPA-Architecture IE. The MPR is specified in Table 6.2E.2.1A.1-12 for power class 2 with TxD supported.

Table 6.2E.2.1A.1-10: S-SSB MPR for power class 3 intra-band SL CA

Table 6.2E.2.1A.1-11: S-SSB MPR for power class 2 intra-band SL CA

Table 6.2E.2.1A.1-12: S-SSB MPR for power class 2 intra-band SL CA with 2Tx

## 6.2E.2.1A.2MPR for sidelink intra-band non-contiguous CA

## 6.2E.2.1A.2.0General

For SL intra-band non-contiguous CA, the allowed Maximum Power Reduction (MPR) for the maximum output power is specified into 2 types: MPR to meet -30dBm/MHz and -13dBm/MHz. The UE determines the MPR type as follows:

For UE indicating dualPA-Architecture supported

If OR (LCRB1 = 0, LCRB2 = 0)

MPR defined in Clause 6.2E.2.2 for PC3 and PC2 UE.

Else If AND (FIM3,low_block,low > SEM-13,low ,  FIM3,high_block,high < SEM-13,high )

MPR defined in Clause 6.2E.2.1A.2.1 to meet -13dBm/MHz for PC3 and PC2 UE.

Else

MPR defined in Clause 6.2E.2.1A.2.1 to meet -30dBm/MHz for PC3 and PC2 UE.

For UE without indicating dualPA-Architecture supported

If OR (LCRB1 = 0, LCRB2 = 0 )

MPR defined in Clause 6.2E.2.2 for PC3 and PC2 UE.

Else If AND (FIM3,low_block,low > SEM-13,low ,  FIM3,high_block,high < SEM-13,high )

MPR defined in Clause 6.2E.2.1A.2.2 to meet -13dBm/MHz for PC3 and PC2 UE.

Else

MPR defined in Clause 6.2E.2.1A.2.2 to meet -30dBm/MHz for PC3 and PC2 UE.

where

-LCRB1 is for CC1, which is the component carrier with lower frequency

-LCRB2 is for CC2, which is the component carrier with higher frequency

-B = (LCRB1* 12* SCS1 + LCRB2 * 12 * SCS2)/1,000 (MHz), where SCS1 and SCS2 are expressed in kHz.

-FIM3,high_block,high = (2 * Fhigh_alloc,high_edge ) – Flow_alloc,low_edge

-FIM3,low_block,low = (2 * Flow_alloc,low_edge) – Fhigh_alloc,high_edge

-Flow_alloc,low_edge is the lowermost frequency of the lower transmission bandwidth allocation.

-Flow_alloc,high_edge is the uppermost frequency of the lower transmission bandwidth allocation.

-Fhigh_alloc,low_edge is the lowermost frequency of the upper transmission bandwidth allocation.

-Fhigh_alloc,high_edge is the uppermost frequency of the upper transmission bandwidth allocation.

-SEM-13,low = Threshold frequency where lower spectral emission mask below the lower channel drops from -13 dBm / MHz to -25 dBm / MHz, as specified in Clause 6.5A.2.2.2.

-SEM-13,high = Threshold frequency where upper spectral emission mask above the upper channel drops from -13 dBm / MHz to -25 dBm / MHz, as specified in Clause 6.5A.2.2.2.

MPRs in section 6.2E.2.1A.2.2 are applicable only when the Gap between the component carriers is ≤ the overall channel bandwidth summed across all the component carriers.

The definition of the gap is between the component carriers in a spectrum that is not part of any configured component carrier that is located in between the lowest edge of the component carrier with higher center frequency and the highest edge of the component carrier with center frequency that is located lower in frequency.

## 6.2E.2.1A.2.1MPR with indicating dualPA-Architecture supported

MPR in this clause is for SL intra-band non-contiguous CA for UEs indicating IE dualPA-Architecture supported.

The allowed maximum output power reduction for PSSCH/PSCCH is defined in Table 6.2E.2.1A.2.1-1 for power class 3 and Table 6.2E.2.1A.2.1-2 for power class 2.

Table 6.2E.2.1A.2.1-1: PSSCH/PSCCH MPR for power class 3 intra-band SL CA

Table 6.2E.2.1A.2.1-2: PSSCH/PSCCH MPR for power class 2 intra-band SL CA

The allowed maximum output power reduction for PSFCH is defined in Table 6.2E.2.1A.2.1-3 for power class 3 and Table 6.2E.2.1A.2.1-4 for power class 2.

Table 6.2E.2.1A.2.1-3: PSFCH MPR for power class 3 intra-band SL CA

Table 6.2E.2.1A.2.1-4: PSFCH MPR for power class 2 intra-band SL CA

The allowed maximum output power reduction for S-SSB is defined in Table 6.2E.2.1A.2.1-5 for power class 3 and Table 6.2E.2.1A.2.1-6 for power class 2.

Table 6.2E.2.1A.2.1-5: S-SSB MPR for power class 3 intra-band SL CA

Table 6.2E.2.1A.2.1-6: S-SSB MPR for power class 2 intra-band SL CA

## 6.2E.2.1A.2.2MPR without indicating dualPA-Architecture supported

MPR in this clause is for SL intra-band non-contiguous CA for UEs without indicating IE dualPA-Architecture supported.

The allowed maximum output power reduction for PSSCH/PSCCH is defined in Table 6.2E.2.1A.2.2-1 for power class 3 and Table 6.2E.2.1A.2.2-2 for power class 2.

Table 6.2E.2.1A.2.2-1: PSSCH/PSCCH MPR for power class 3 intra-band SL CA

Table 6.2E.2.1A.2.2-2: PSSCH/PSCCH MPR for power class 2 intra-band SL CA

The allowed maximum output power reduction for PSFCH is defined in Table 6.2E.2.1A.2.2-3 for power class 3 and Table 6.2E.2.1A.2.2-4 for power class 2.

Table 6.2E.2.1A.2.2-3: PSFCH MPR for power class 3 intra-band SL CA

Table 6.2E.2.1A.2.2-4: PSFCH MPR for power class 2 intra-band SL CA

The allowed maximum output power reduction for S-SSB is defined in Table 6.2E.2.1A.2.2-5 for power class 3 and Table 6.2E.2.1A.2.2-6 for power class 2.

Table 6.2E.2.1A.2.2-5: S-SSB MPR for power class 3 intra-band SL CA

Table 6.2E.2.1A.2.2-6: S-SSB MPR for power class 2 intra-band SL CA

## 6.2E.2.2MPR for Power class 2 and Power class 3 V2X UE

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed MPR for the maximum output power for NR V2X physical channels PSCCH and PSSCH shall be as specified in Table 6.2E.2.2-1 for Power class 3 NR V2X UE and Table 6.2E.2.2-2 for power class 2 NR V2X UE.

Table 6.2E.2.2-1: Maximum Power Reduction (MPR) for power class 3 NR V2X

Table 6.2E.2.2-2: Maximum Power Reduction (MPR) for power class 2 NR V2X

For NR V2X UE supporting SL MIMO or Tx diversity, the allowed MPR for the maximum output power for NR V2X physical channels PSCCH and PSSCH are specified in Table 6.2E.2.2-3 for power class 2 UE.

Table 6.2E.2.2-3: Maximum Power Reduction (MPR) for power class 2 NR V2X with 2Tx

Where the following parameters are defined to specify valid RB allocation ranges for Outer and Inner RB allocations:

NRB is the maximum number of RBs for a given Channel bandwidth and sub-carrier spacing defined in Table 5.3.2-1.

RBStart,Low = max(1, floor(LCRB/2))

where max() indicates the largest value of all arguments and floor(x) is the greatest integer less than or equal to x.

RBStart,High = NRB – RBStart,Low – LCRB

The RB allocation is an Inner RB allocation if the following conditions are met

RBStart,Low  ≤  RBStart  ≤  RBStart,High, and

LCRB  ≤ ceil(NRB/2)

where ceil(x) is the smallest integer greater than or equal to x.

The RB allocation is an Outer RB allocation for all other allocations which are not an Inner RB allocation.

For PSFCH with single RB transmission for PC3 NR V2X UE, the required MPR is defined as follow

MPR_PSFCH = 3.5 dB

For contiguous and non-contiguous allocation for simultaneous PSFCH transmission for PC3 NR V2X UE, the required MPR are specified as follow

MPR_PSFCH = CEIL {MA_PSFCH, 0.5}

Where MA_PSFCH for power class 3 is defined as follows

MA_PSFCH =7.5; 0.00< NGap/NRB ≤ 0.55

=    12.0; 0.55< NGap/NRB ≤1.0

For PSFCH with single RB transmission for PC2 NR V2X UE, the required MPR is defined as follow

MPR_PSFCH = 4.5 dB

For contiguous and non-contiguous allocation for simultaneous PSFCH transmission for PC2 NR V2X UE, the required MPR are specified as follow

MPR_PSFCH = CEIL {MA_PSFCH, 0.5}

Where MA is defined as follows

Where MA_PSFCH for power class 2 is defined as follows

MA_PSFCH =8.5; 0.00 ≤ NGap/NRB < 0.4

=   10.0; 0.4 ≤ NGap/NRB < 0.55

=   14.0; 0.55 ≤ NGap/NRB ≤ 1.0

Where,

NGap is the gap RB amount between RBstart and RBend for contiguous and non-contiguous allocation simultaneous PSFCH transmission. (NGap = RBend - RBstart)

CEIL{MA, 0.5} means rounding upwards to closest 0.5dB.

The allowed MPR for the maximum output power for NR V2X physical channels on S-SSB transmission shall be specified in Table 6.2E.2.2-4 for power class 3 and power class 2.

Table 6.2E.2.2-4: Maximum Power Reduction (MPR) for S-SSB transmission for power class 3 and power class 2 NR V2X

For NR V2X UE with two transmit antenna connectors, the allowed Maximum Power Reduction (MPR) values specified in clause 6.2E.2 for PC3 and PC2 shall apply to the maximum output power specified in Table 6.2E.1.1-1.

For the UE maximum output power modified by MPR, the power limits specified in clause 6.2E.4 apply.

## 6.2E.2.3MPR for Power class 2 and Power class 3 V2X concurrent operation

For the inter-band concurrent NR V2X operation, the allowed maximum power reduction (MPR) for the maximum output power shall be applied per each component carrier. The MPR requirements in clause 6.2.2 apply for NR Uu operation in licensed band, and the MPR requirements in clause 6.2E.2 apply for NR sidelink operation in licensed band or Band n47.

For the intra-band concurrent NR V2X operation with contiguous RB allocation, the allowed maximum power reduction (MPR) for NR V2X physical channels PSCCH and PSSCH shall be as specified in Table 6.2E.2.3-1 for Power class 3 V2X concurrent UE.

Table 6.2E.2.3-1: MPR for contiguous RB allocation for power class 3 NR V2X concurrent UE

For bandwidth class B with contiguous RB allocation, the following parameters are defined to specify valid RB allocation ranges for Inner and Outer RB allocations:

An RB allocation is contiguous if LCRB1 = 0 or LCRB2 = 0 or (LCRB1  0 and LCRB2  0 and RBStart1 + LCRB1 = NRB1 and RBStart2 = 0), where RBStart1, LCRB1, and NRB1 are for SL CC1, RBStart2, LCRB2, and NRB2 are for UL CC2. SL CC1 is the component carrier with lower frequency.

In contiguous NR V2X intra-band concurrent operation, a contiguous allocation is an inner allocation if

RBStart,Low  ≤  RBStart_SL&UL  ≤  RBStart,High, and NRB_alloc  ≤  ceil(NRB,agg /2),

where

RBStart,Low = max(1, floor(NRB_alloc /2))

RBStart,High = NRB,agg – RBStart,Low – NRB,alloc,

with

NRB_alloc= LCRB1 ∙ 2µ1 + LCRB2 ∙ 2µ2

NRB_alloc= (NRB1 - RBStart1)∙ 2µ1 + (RBStart2 + LCRB2 ) ∙ 2µ2,

NRB,agg=NRB1∙2µ1+ NRB2∙2µ2.

If LCRB1 =0, RBStart_SL&UL = NRB1∙2µ1+ RBStart2∙2µ2,

if LCRB1 > 0, RBStart_SL&UL = RBStart1∙2µ1.

Where, µ1 and µ2 is 0, 1 and 2 for SCS of 15kHz, 30kHz and 60kHz respectively.

A contiguous allocation that is not an Inner contiguous allocation is an Outer contiguous allocation.

For the intra-band concurrent NR V2X operation with non-contiguous RB allocation, the allowed maximum power reduction (MPR) for NR V2X physical channels PSCCH and PSSCH shall be as specified in Table 6.2E.2.3-2 for Power class 3 V2X concurrent UE.

Table 6.2E.2.3-2: MPR for non-contiguous RB allocation for power class 3 NR V2X concurrent UE

For bandwidth classes B with non-contiguous RB allocation, the following parameters are defined to specify valid RB allocation ranges for Inner, Outer1 and Outer2 RB allocations:

Non-Contiguous RB allocation is defined as RBStart1 + LCRB1 < NRB1, or RBStart2 > 0, when both SL CC and UL CC are activated and allocated with RB(s), where RBStart1, LCRB1, and NRB1 are for SL CC1, RBStart2, LCRB2, and NRB2 are for UL CC2. SL CC1 is the component carrier with lower frequency.

In contiguous NR V2X intra-band concurrent operation, a non-contiguous RB allocation is a non-contiguous Inner RB allocation if the following conditions are met:

RBStart,Low  ≤  RBStart_CA  ≤  RBStart,High and NRB_alloc ≤  ceil((BWChannel_SL&UL / 3 – BWgap ) / 0.18MHz),

where

NRB_alloc = (NRB1 - RBStart1)∙ 2µ1 + (RBStart2 + LCRB2 ) ∙ 2µ2, RBStart_SL&UL = RBStart1∙21

RBStart,Low = max(1, floor(NRB_alloc + (BWgap – BWGB,low)/0.18MHz))

RBStart,High = floor((BWChannel_SL&UL – 2 ∙ BWgap – BWGB,low)/0.18MHz – 2 ∙ NRB_alloc)

BWGB,low =Foffset,low – (NRB1∙12+1)∙SCS1/2

BWgap is the bandwidth of the gap between NRB1 and NRB2 possible allocations of SL CC1 and UL CC2 respectively.

In contiguous NR V2X intra-band concurrent operation, a non-contiguous RB allocation is a non-contiguous outer 1 RB allocation if the following conditions are met:

RBStart,Low  ≤  RBStart_SL&UL  ≤  RBStart,High and NRB_alloc ≤  ceil((3 BWChannel_SL&UL / 5 – BWgap) / 0.18MHz)

where

RBStart,Low = max(1, 2 ∙ NRB_alloc – floor( (BWChannel_SL&UL – 2 ∙ BWgap + BWGB,low)/0.18MHz)),

RBStart,High = floor((2 ∙ BWChannel_SL&UL – 3 ∙ BWgap – BWGB,low) / 0.18MHz – 3 ∙ NRB_alloc)

NRB_alloc , RBStart_SL&UL , BWgap and BWGB,low are as defined for the Inner region.

In contiguous NR V2X intra-band concurrent operation, a non-contiguous allocation is an Outer 2 allocation if it is neither a non-contiguous Inner allocation nor an Outer 1 allocation.

For PSFCH with single RB transmission for PC3 NR V2X intra-band concurrent UE, the required MPR is specified in clause 6.2E.2.2 shall be applied.

For the allowed MPR for S-SSB transmission for PC3 NR V2X intra-band concurrent UE, the required MPR is specified in clasue 6.2E.2.2 shall be applied.

For the intra-band concurrent NR V2X operation with contiguous RB allocation in contiguous carrier, the allowed maximum power reduction (MPR) for NR V2X physical channels PSCCH and PSSCH shall be as specified in Table 6.2E.2.3-3 for Power class 2 V2X concurrent UE.

Table 6.2E.2.3-3: MPR for contiguous RB allocation for power class 2 NR V2X concurrent UE

For the intra-band concurrent NR V2X operation with non-contiguous RB allocation in contiguous carrier, the allowed maximum power reduction (MPR) for NR V2X physical channels PSCCH and PSSCH shall be as specified in Table 6.2E.2.3-4 for Power class 2 V2X concurrent UE.

Table 6.2E.2.3-4: MPR for non-contiguous RB allocation for power class 2 NR V2X concurrent UE

The parameters in clause 6.2E.2.3 are considered to determine MPR values according to RB allocation.

For PSFCH with single RB transmission for PC2 NR V2X intra-band concurrent UE, the required MPR is specified in clause 6.2E.2.2 shall be applied.

For the allowed MPR for S-SSB transmission for PC2 NR V2X intra-band concurrent UE, the required MPR is specified in clause 6.2E.2.2 shall be applied.

## 6.2E.2.4MPR for Power class 1 UE in Band n14

For NR Public Safety (PS) UE with contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed NR PS UE maximum output power reduction for power class 1 UE shall meet the NR V2X MPR values specified in Table 6.2E.2.2-1 of clause 6.2E.2.2.

For NR Public Safety (PS) UE of single or multiple PSFCH simultaneous transmission, the allowed NR PS UE maximum output power reduction for power class 1 UE shall meet the NR V2X MPR values for PC3 UE’s PSFCH transmission in clause 6.2E.2.2.

For NR Public Safety (PS) UE of S-SSB transmission, the allowed NR PS UE maximum output power reduction for power class 1 UE shall meet the NR V2X MPR values specified in Table 6.2E.2.2-2 of clause 6.2E.2.2.

## 6.2E.2FUE maximum output power reduction for Sidelink Unlicensed

## 6.2E.2F.1General

When UE is configured for NR sidelink transmissions in the unlicensed operating bands in FR1 defined in Table 5.2E.1F-1, this clause specifies the allowed Maximum Power Reduction (MPR) power for NR sidelink physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

For wideband operation, only sub-bands which are contiguously transmitted are considered in Table 6.2E.2F-3 for PSCCH/PSSCH.

For wideband operation, sub-bands which are contiguously transmitted and sub-bands which are non-contiguously transmitted in Table 6.2E.2F-3 are considered for PSFCH and S-SSB.

## 6.2E.2F.2MPR for NR SL-U UE

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed MPR for the maximum output power is specified in Table 6.2E.2F-1 for power class 5 NR sidelink UE.

Table 6.2E.2F-1 Maximum power reduction (MPR) for NR SL-U UE power class 5

Table 6.2E.2F-2: Exception MPR mapping for NR SL-U wideband operation

Table 6.2E.2F-3 Outer/Inner sub-band configuration for NR SL-U wideband operation

For PSFCH transmission with single RB set the allowed MPR for the maximum output power is 10dB for power class 5 NR sidelink UE.

For PSFCH transmission with multiple RB sets the allowed MPR for the maximum output power is specified in Table 6.2E.2F-4 for power class 5 NR sidelink UE.

Table 6.2E.2F-4 Maximum power reduction (MPR) forPSFCH transmission for NR SL-U UE power class 5

For S-SSB transmission, the allowed MPR for the maximum output power is specified in Table 6.2E.2F-5 for power class 5 NR sidelink UE.

Table 6.2E.2F-5 Maximum power reduction (MPR) forS-SSB transmission for NR SL-U UE power class 5

## 6.2E.2F.3MPR for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the allowed maximum power reduction (MPR) for the maximum output power shall be applied per each component carrier. The MPR requirements in clause 6.2.2 apply for NR Uu operation in licensed band, and the MPR requirements in clause 6.2E.2F apply for NR sidelink operation in unlicensed band.

## 6.2E.3UE additional maximum output power reduction for V2X

## 6.2E.3.1General

For the applied maximum output power reduction is obtained by taking the maximum value of MPR requirements specified in clause 6.2E.2 and A-MPR requirements specified in current clause.

Additional emission requirements can be indicated by the network or pre-configured radio parameters. Each additional emission requirement is associated with a unique network signalling (NS) value indicated in RRC signalling by an NR frequency band number of the applicable operating band and an associated value in the field [additionalSpectrumEmission]. Throughout this specification, the notion of indication or signalling of an NS value refers to the corresponding indication of an NR V2X frequency band number of the applicable operating band, the IE field [freqBandIndicatorNR] and an associated value of [additionalSpectrumEmission] in the relevant RRC information elements [7].

To meet the additional requirements, additional maximum power reduction (A-MPR) is allowed for the maximum output power as specified in Table 6.2.1-1. Outer and inner allocation notation used in clause 6.2E.3 is defined in clause 6.2E.2. In absence of modulation and waveform types the A-MPR applies to all modulation and waveform types.

Table 6.2E.3.1-1: Additional Maximum Power Reduction (A-MPR) for PC3 NR V2X

Table 6.2E.3.1-2: Mapping of network signaling label

For UE with two transmit antenna connectors, the A-MPR values specified in clause 6.2E.3.2 and 6.2E.3.3 shall apply to the maximum output power specified in Table 6.2E.1.1-1. Unless stated otherwise, an A-MPR of 0 dB shall be used.

For the UE maximum output power modified by A-MPR, the power limits specified in clause 6.2E.4 apply.

## 6.2E.3.2A-MPR for V2X UE by NS_33

When NS_33 is indicated by the network or pre-configured radio parameters for NR V2X UE, the additional maximum output power reduction specified as

A-MPR = CEIL {MA, 0.5}

Where MA is defined as follows

MA = A-MPRBase + Gpost connector* A-MPRStep

CEIL{MA, 0.5} means rounding upwards to closest 0.5dB.

A-MPRBase and A-MPRStep  are specified in Tables 6.2E.3.2-1, 6.2E.3.2-2 is allowed when network signalling value is provided. A-MPRBase is the default A-MPR value when no Gpost connector is declared. The supported post antenna connector gain Gpost connector is declared by the UE following the principle described in annex I in [11]. The A-MPRstep is the increase in A-MPR allowance to allow UE to meet tighter conducted A-SE and A-SEM requirements with higher value of declared Gpost connector.

For the contiguous PSSCH and PSCCH transmission when NS_33 is indicated by the network or pre-configured radio parameters for NR V2X UE, the NR UE allow the follow A-MPR requirements specified in Table 6.2E.3.2-1 and 6.2E.3.2-2 for power class 3. And A-MPR requirements specified in Table 6.2E.3.2-2a and 6.2E.3.2-2b for power class 2 are allowed for NR V2X UE.

Table 6.2E.3.2-1: PC3 A-MPR for PSSCH/PSCCH by NS_33 (at Fc =5860MHz, and 5920MHz)

Table 6.2E.3.2-2: PC3 A-MPR for PSSCH/PSCCH by NS_33 (at other carrier frequency)

Table 6.2E.3.2-2a: PC2 A-MPR for PSCCH/PSSCH by NS_33 (at Fc=5860MHz, and 5920MHz)

Table 6.2E.3.2-2b: PC2 A-MPR for PSSCH/PSCCH by NS_33 (at other carrier frequency)

For the simultaneous PSFCH transmission when NS_33 is indicated by the network or pre-configured radio parameters for NR V2X UE, the NR UE allow the follow A-MPR requirements specified in Table 6.2E.3.2-3 for power class 3 and in Table 6.2E.3.2-3a for power class 2.

Table 6.2E.3.2-3: PC3 A-MPR for simultaneous PSFCH by NS_33

Table 6.2E.3.2-3a: PC2 A-MPR for simultaneous PSFCH by NS_33

For the S-SSB transmission when NS_33 is indicated by the network or pre-configured radio parameters for NR V2X UE, the NR UE allow the follow A-MPR requirements specified in Table 6.2E.3.2-4 for power class 3 and in Table 6.2E.3.2-5 for power class 2.

Table 6.2E.3.2-4: PC3 A-MPR for S-SSB transmission by NS_33

Table 6.2E.3.2-5: PC2 A-MPR for S-SSB transmission by NS_33

## 6.2E.3.2AA-MPR for sidelink CA by NS_33

## 6.2E.3.2A.1A-MPR for sidelink intra-band non-contiguous CA

6.2E.3.2A.1.0General

Table 6.2E.3.2A.1.0-1 specifies the additional requirements with their associated network or pre-configured signalling values and the allowed A-MPR and applicable NR SL CA band(s) for each SLCA_NC_NS value. For any NR SL CA band not listed in Table 6.2E.3.2A.1.0-2 the network or pre-configured signalling label SLCA_NC_NS_01 applies.

Table 6.2E.3.2A.1.0-1: Additional Maximum Power Reduction (A-MPR) for SL CA

The mapping of NR SL CA band numbers and values of the additionalSpectrumEmission to network or pre-configured signalling labels is specified in Table 6.2E.3.2A.1.0-2.

Table 6.2E.3.2A.1.0-2: Mapping of network or pre-configured signaling label

## 6.2E.3.2A.1.1A-MPR for SLCA_NC_NS_33 (SLCA_n47(2A))

6.2E.3.2A.1.1.0General

For SL intra-band non-contiguous CA_n47(2A) and it receives SLCA_NC_NS_33, the UE determines the allowed Additional Maximum Power Reduction (A-MPR) for the maximum output power as specified in this clause. The A-MPR is specified into 2 types: A-MPR to meet -30dBm/MHz and -37dBm/100kHz. The UE determines the A-MPR type as follows:

For UE indicating dualPA-Architecture supported

If AND (FIM3,low_block,low > SEM-37/100kHz,low ,  FIM3,high_block,high < SEM-37/100kHz,high )

A-MPR defined for FIM3_Inner in Clause 6.2E.3.2A.1.1.1 for PC3 and PC2 UE.

Else

A-MPR defined for FIM3_Outer in Clause 6.2E.3.2A.1.1.1 for PC3 and PC2 UE.

For UE without indicating dualPA-Architecture supported

If AND (FIM3,low_block,low > SEM-37/100kHz,low ,  FIM3,high_block,high < SEM-37/100kHz,high)

A-MPR defined for FIM3_Inner in Clause 6.2E.3.2A.1.1.2 for PC3 and PC2 UE.

Else

A-MPR defined for FIM3_Outer in Clause 6.2E.3.2A.1.1.2 for PC3 and PC2 UE.

where

-LCRB1 is for CC1, which is the component carrier with lower frequency

-LCRB2 is for CC2, which is the component carrier with higher frequency

-B = (LCRB1* 12* SCS1 + LCRB2 * 12 * SCS2)/1,000 (MHz), where SCS1 and SCS2 are expressed in kHz.

-FIM3,high_block,high = (2 * Fhigh_alloc,high_edge ) – Flow_alloc,low_edge

-FIM3,low_block,low = (2 * Flow_alloc,low_edge) – Fhigh_alloc,high_edge

-Flow_alloc,low_edge is the lowermost frequency of the lower transmission bandwidth allocation.

-Flow_alloc,high_edge is the uppermost frequency of the lower transmission bandwidth allocation.

-Fhigh_alloc,low_edge is the lowermost frequency of the upper transmission bandwidth allocation.

-Fhigh_alloc,high_edge is the uppermost frequency of the upper transmission bandwidth allocation.

-SEM-37/100kHz,low = Threshold frequency where lower spectral emission mask below the lower channel corresponds to -37dBm/100kHz, as specified in Clause 6.5E.2.3.1A.

-SEM-37/100kHz,high = Threshold frequency where upper spectral emission mask above the upper channel corresponds to -37dBm /100kHz, as specified in Clause 6.5E.2.3.1A.

-FIM3_Inner is “AND (FIM3,low_block,low > SEM-37/100kHz,low ,  FIM3,high_block,high < SEM-37/100kHz,high)”

-FIM3_Outer is “AND (FIM3,low_block,low ≤  SEM-37/100kHz,low ,  FIM3,high_block,high ≥ SEM-37/100kHz,high)”

A-MPRs in section 6.2E.3.2A.1.1.2 are applicable only when the Gap between the component carriers is ≤ the overall channel bandwidth summed across all the component carriers.

The definition of the gap is between the component carriers in a spectrum that is not part of any configured component carrier that is located in between the lowest edge of the component carrier with higher center frequency and the highest edge of the component carrier with center frequency that is located lower in frequency.

6.2E.3.2A.1.1.1A-MPR with indicating dualPA-Architecture supported

A-MPR in this clause is for SL intra-band non-contiguous CA for UEs indicating IE dualPA-Architecture supported.

The allowed additional maximum output power reduction for PSSCH/PSCCH is defined in Table 6.2E.3.2A.1.1.1-1 for power class 3 and Table 6.2E.3.2A.1.1.1-2 for power class 2.

Table 6.2E.3.2A.1.1.1-1: PSSCH/PSCCH A-MPR for power class 3 intra-band SL CA

Table 6.2E.3.2A.1.1.1-2: PSSCH/PSCCH A-MPR for power class 2 intra-band SL CA

The allowed additional maximum output power reduction for PSFCH is defined in Table 6.2E.3.2A.1.1.1-3 for power class 3 and Table 6.2E.3.2A.1.1.1-4 for power class 2.

Table 6.2E.3.2A.1.1.1-3: PSFCH A-MPR for power class 3 intra-band SL CA

Table 6.2E.3.2A.1.1.1-4: PSFCH A-MPR for power class 2 intra-band SL CA

The allowed additional maximum output power reduction for S-SSB is defined in Table 6.2E.3.2A.1.1.1-5 for power class 3 and Table 6.2E.3.2A.1.1.1-6 for power class 2.

Table 6.2E.3.2A.1.1.1-5: S-SSB A-MPR for power class 3 intra-band SL CA

Table 6.2E.3.2A.1.1.1-6: S-SSB A-MPR for power class 2 intra-band SL CA

6.2E.3.2A.1.1.2A-MPR without indicating dualPA-Architecture supported

A-MPR in this clause is for SL intra-band non-contiguous CA for UEs not indicating IE dualPA-Architecture supported.

The allowed additional maximum output power reduction for PSSCH/PSCCH is defined in Table 6.2E.3.2A.1.1.2-1 for power class 3 and Table 6.2E.3.2A.1.1.2-2 for power class 2.

Table 6.2E.3.2A.1.1.2-1: PSSCH/PSCCH A-MPR for power class 3 intra-band SL CA

Table 6.2E.3.2A.1.1.2-2: PSSCH/PSCCH A-MPR for power class 2 intra-band SL CA

The allowed additional maximum output power reduction for PSFCH is defined in Table 6.2E.3.2A.1.1.2-3 for power class 3 and Table 6.2E.3.2A.1.1.2-4 for power class 2.

Table 6.2E.3.2A.1.1.2-3: PSFCH A-MPR for power class 3 intra-band SL CA

Table 6.2E.3.2A.1.1.2-4: PSFCH A-MPR for power class 2 intra-band SL CA

The allowed additional maximum output power reduction for S-SSB is defined in Table 6.2E.3.2A.1.1.2-5 for power class 3 and Table 6.2E.3.2A.1.1.2-6 for power class 2.

Table 6.2E.3.2A.1.1.2-5: S-SSB A-MPR for power class 3 intra-band SL CA

Table 6.2E.3.2A.1.1.2-6: S-SSB A-MPR for power class 2 intra-band SL CA

## 6.2E.3.3A-MPR for Power class 3 V2X UE by NS_52

When NS_52 is indicated by the network or pre-configured radio parameters for NR V2X UE, the additional maximum output power reduction specified as

A-MPR = CEIL {MA, 0.5}

Where MA is defined as follows

MA = A-MPR

CEIL{MA, 0.5} means rounding upwards to closest 0.5dB.

For the contiguous PSSCH and PSCCH transmission when NS_52 is indicated by the network or pre-configured radio parameters for NR V2X UE, the NR UE allow the follow A-MPR requirements.

Table 6.2E.3.3-1: A-MPR for PSSCH/PSCCH by NS_52

Where the following parameters are defined to specify valid RB allocation ranges for Region1, Region2 and Region3 according to RB allocations:

Table 6.2E.3.3-1a: A-MPR Region definitions for PSSCH/PSCCH by NS_52

NRB is the maximum number of RBs for a given Channel bandwidth and sub-carrier spacing defined in Table 5.3.2-1 [3].

For the simultaneous PSFCH transmission when NS_52 is indicated by the network or pre-configured radio parameters for NR V2X UE, the NR UE allow the follow A-MPR requirements

Table 6.2E.3.3-2: A-MPR for simultaneous PSFCH by NS_52

For the S-SSB transmission when NS_52 is indicated by the network or pre-configured radio parameters for NR V2X UE, the NR UE allow the follow A-MPR requirements

Table 6.2E.3.2-3: A-MPR for S-SSB transmission by NS_52

## 6.2E.3.4A-MPR for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the allowed additional maximum power reduction (A-MPR) for the maximum output power shall be applied per each component carrier. The A-MPR requirements in clause 6.2.3 apply for NR Uu operation in licensed band, and the A-MPR requirements in clause 6.2E.3.2 and 6.2E.3.3 apply for NR sidelink operation in Band n47.

For the intra-band concurrent NR V2X operation, the A-MPR requirements in [6.2E.3.4] apply for NR Uu and SL concurrent operation in the licensed band.

## 6.2E.3FUE additional maximum output power reduction for Sidelink Unlicensed

## 6.2E.3F.1General

Additional emission requirements can be signalled by the network or pre-configured radio parameters. Each additional emission requirement is associated with a unique network signalling (NS) value indicated in RRC signalling by an NR frequency band number of the applicable operating band and an associated value in the field additionalSpectrumEmission. Throughout this specification, the notion of indication or signalling of an NS value refers to the corresponding indication of an NR frequency band number of the applicable operating band, the IE field freqBandIndicatorNR and an associated value of additionalSpectrumEmission in the relevant RRC information elements [7].

To meet the additional requirements, additional maximum power reduction (A-MPR) is allowed for the maximum output power as specified in Table 6.2E.1F-1. Unless stated otherwise, the total reduction to UE maximum output power is max(MPR, A-MPR) where MPR is defined in clause 6.2E.2F.

Table 6.2E.3F.1-1 specifies the additional requirements with their associated network signalling values and the allowed A-MPR and applicable operating band(s) for each NS value. The mapping of NR frequency band numbers and values of the additionalSpectrumEmission to network signalling labels is specified in Table 6.2E.3F.1-1A.

Table 6.2E.3F.1-1: Additional maximum power reduction (A-MPR)

[The NS_01 label with the field additionalPmax [7] absent is default for all NR bands.]

Table 6.2E.3F.1-1A: Mapping of network signaling label

Table 6.2E.3F.1-1B: Mapping of extended network signaling label

## 6.2E.3F.2A-MPR for NS_31

When NS_31 is indicated by the network or pre-configured radio parameters for NR sidelink UE, this clause specifies the allowed Maximum Power Reduction (MPR) power for NR sidelink physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed A-MPR is specified in Table 6.2E.3F.2-1 for power class 5 NR sidelink UE.

Table 6.2E.3F.2-1: A-MPR for NS_31 NR SL-U UE power class 5

For PSFCH transmission with single RB set and multiple RB sets, the allowed A-MPR is specified in Table 6.2E.3F.2-2 for power class 5 NR sidelink UE.

Table 6.2E.3F.2-2: A-MPR for NS_31 for PSFCH transmission for NR SL-U UE power class 5

For S-SSB transmission, the allowed A-MPR is specified in Table 6.2E.3F.2-3 for power class 5 NR sidelink UE.

Table 6.2E.3F.2-3: A-MPR for NS_31 for S-SSB transmission for NR SL-U UE power class 5

## 6.2E.3F.3Void

## 6.2E.3F.4Void

## 6.2E.3F.5Void

## 6.2E.3F.6A-MPR for NS_61

When NS_61 is indicated by the network or pre-configured radio parameters for NR sidelink UE, this clause specifies the allowed Maximum Power Reduction (MPR) power for NR sidelink physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed A-MPR is specified in Table 6.2E.3F.6-1 for power class 5 NR sidelink UE.

Table 6.2E.3F.6-1: A-MPR for NS_61 NR SL-U UE power class 5

For PSFCH transmission with single RB set and multiple RB sets, the allowed A-MPR is specified in Table 6.2E.3F.6-2 for power class 5 NR sidelink UE.

Table 6.2E.3F.6-2: A-MPR for NS_61 for PSFCH transmission for NR SL-U UE power class 5

For S-SSB transmission, the allowed A-MPR is specified in Table 6.2E.3F.6-3 for power class 5 NR sidelink UE.

Table 6.2E.3F.6-3: A-MPR for NS_61 for S-SSB transmission for NR SL-U UE power class 5

## 6.2E.3F.7A-MPR for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the allowed additional maximum power reduction (A-MPR) for the maximum output power shall be applied per each component carrier. The A-MPR requirements in clause 6.2.3 apply for NR Uu operation in licensed band, and the A-MPR requirements in clause 6.2E.3F apply for NR sidelink operation in unlicensed band, n46, n96 and n102.

## 6.2E.3F.8A-MPR for NS_28

When NS_28 is indicated by the network or pre-configured radio parameters for NR sidelink UE, this clause specifies the allowed Maximum Power Reduction (MPR) power for NR sidelink physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed A-MPR is specified in Table 6.2F.3F.8-1 for power class 5 NR sidelink UE.

Table 6.2E.3F.8-1: A-MPR for NS_28 NR SL-U UE power class 5

For PSFCH transmission with single RB set and multiple RB sets, the allowed A-MPR is specified in Table 6.2E.3F.8-2 for power class 5 NR sidelink UE.

Table 6.2E.3F.8-2: A-MPR for NS_28 for PSFCH transmission for NR SL-U UE power class 5

For S-SSB transmission, the allowed A-MPR is specified in Table 6.2E.3F.8-3 for power class 5 NR sidelink UE.

Table 6.2E.3F.8-3: A-MPR for NS_28 for S-SSB transmission for NR SL-U UE power class 5

## 6.2E.3F.9A-MPR for NS_29

When NS_29 is indicated by the network or pre-configured radio parameters for NR sidelink UE, this clause specifies the allowed Maximum Power Reduction (MPR) power for NR sidelink physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed A-MPR is specified in Table 6.2E.3F.9-1 for power class 5 NR sidelink UE.

Table 6.2E.3F.9-1: A-MPR for NS_29 NR SL-U UE power class 5

For PSFCH transmission with single RB set and multiple RB sets, the allowed A-MPR is specified in Table 6.2E.3F.9-2 for power class 5 NR sidelink UE.

Table 6.2E.3F.9-2: A-MPR for NS_29 for PSFCH transmission for NR SL-U UE power class 5

For S-SSB transmission, the allowed A-MPR is specified in Table 6.2E.3F.9-3 for power class 5 NR sidelink UE.

Table 6.2E.3F.9-3: A-MPR for NS_29 for S-SSB transmission for NR SL-U UE power class 5

## 6.2E.3F.10A-MPR for NS_30

When NS_30 is indicated by the network or pre-configured radio parameters for NR sidelink UE, this clause specifies the allowed Maximum Power Reduction (MPR) power for NR sidelink physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed A-MPR is specified in Table 6.2E.3F.10-1 for power class 5 NR sidelink UE.

Table 6.2E.3F.10-1: A-MPR for NS_30 NR SL-U UE power class 5

For PSFCH transmission with single RB set and multiple RB sets, the allowed A-MPR is specified in Table 6.2E.3F.10-2 for power class 5 NR sidelink UE.

Table 6.2E.3F.10-2: A-MPR for NS_30 for PSFCH transmission for NR SL-U UE power class 5

For S-SSB transmission, the allowed A-MPR is specified in Table 6.2E.3F.10-3 for power class 5 NR sidelink UE.

Table 6.2E.3F.10-3: A-MPR for NS_30 for S-SSB transmission for NR SL-U UE power class 5

## 6.2E.3F.11A-MPR for NS_54

When NS_54 is indicated by the network or pre-configured radio parameters for NR sidelink UE, this clause specifies the allowed Maximum Power Reduction (MPR) power for NR sidelink physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed A-MPR is specified in Table 6.2E.3F.11-1 for power class 5 NR sidelink UE.

Table 6.2E.3F.11-1: A-MPR for NS_54 NR SL-U UE power class 5

For PSFCH transmission with single RB set and multiple RB sets, the allowed A-MPR is specified in Table 6.2E.3F.11-2 for power class 5 NR sidelink UE.

Table 6.2E.3F.11-2: A-MPR for NS_54 for PSFCH transmission for NR SL-U UE power class 5

For S-SSB transmission, the allowed A-MPR is specified in Table 6.2E.3F.11-3 for power class 5 NR sidelink UE.

Table 6.2E.3F.11-3: A-MPR for NS_54 for S-SSB transmission for NR SL-U UE power class 5

## 6.2E.3F.12A-MPR for NS_64

When NS_64 is indicated by the network or pre-configured radio parameters for NR sidelink UE, this clause specifies the allowed Maximum Power Reduction (MPR) power for NR sidelink physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed A-MPR is specified in Table 6.2E.3F.12-1 for power class 5 NR sidelink UE.

Table 6.2E.3F.12-1: A-MPR for NS_64 NR SL-U UE power class 5

For PSFCH transmission with single RB set and multiple RB sets, the allowed A-MPR is specified in Table 6.2E.3F.12-2 for power class 5 NR sidelink UE.

Table 6.2E.3F.12-2: A-MPR for NS_64 for PSFCH transmission for NR SL-U UE power class 5

For S-SSB transmission, the allowed A-MPR is specified in Table 6.2E.3F.12-3 for power class 5 NR sidelink UE.

Table 6.2E.3F.12-3: A-MPR for NS_64 for S-SSB transmission for NR SL-U UE power class 5

## 6.2E.3F.13A-MPR for NS_65

When NS_65 is indicated by the network or pre-configured radio parameters for NR sidelink UE, this clause specifies the allowed Maximum Power Reduction (MPR) power for NR sidelink physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed A-MPR is specified in Table 6.2E.3F.13-1 for power class 5 NR sidelink UE.

Table 6.2E.3F.13-1: A-MPR for NS_65 NR SL-U UE power class 5

For PSFCH transmission with single RB set and multiple RB sets, the allowed A-MPR is specified in Table 6.2E.3F.13-2 for power class 5 NR sidelink UE.

Table 6.2E.3F.13-2: A-MPR for NS_65 for PSFCH transmission for NR SL-U UE power class 5

For S-SSB transmission, the allowed A-MPR is specified in Table 6.2E.3F.13-3 for power class 5 NR sidelink UE.

Table 6.2E.3F.13-3: A-MPR for NS_65 for S-SSB transmission for NR SL-U UE power class 5

## 6.2E.3F.14A-MPR for NS_66

When NS_66 is indicated by the network or pre-configured radio parameters for NR sidelink UE, this clause specifies the allowed Maximum Power Reduction (MPR) power for NR sidelink physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed A-MPR is specified in Table 6.2E.3F.14-1 for power class 5 NR sidelink UE.

Table 6.2E.3F.14-1: A-MPR for NS_66 NR SL-U UE power class 5

For PSFCH transmission with single RB set and multiple RB sets, the allowed A-MPR is specified in Table 6.2E.3F.14-2 for power class 5 NR sidelink UE.

Table 6.2E.3F.14-2: A-MPR for NS_66 for PSFCH transmission for NR SL-U UE power class 5

For S-SSB transmission, the allowed A-MPR is specified in Table 6.2E.3F.14-3 for power class 5 NR sidelink UE.

Table 6.2E.3F.14-3: A-MPR for NS_66 for S-SSB transmission for NR SL-U UE power class 5

## 6.2E.3F.15A-MPR for NS_67 or NS_71

When NS_67 or NS_71 is indicated by the network or pre-configured radio parameters for NR sidelink UE, this clause specifies the allowed Maximum Power Reduction (MPR) power for NR sidelink physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed A-MPR is specified in Table 6.2E.3F.15-1 for power class 5 NR sidelink UE.

Table 6.2E.3F.15-1: A-MPR for NS_67 or NS_71 NR SL-U UE power class 5

For PSFCH transmission with single RB set and multiple RB sets, the allowed A-MPR is specified in Table 6.2E.3F.15-2 for power class 5 NR sidelink UE.

Table 6.2E.3F.15-2: A-MPR for NS_67 or NS_71 for PSFCH transmission for NR SL-U UE power class 5

For S-SSB transmission, the allowed A-MPR is specified in Table 6.2E.3F.15-3 for power class 5 NR sidelink UE.

Table 6.2E.3F.15-3: A-MPR for NS_67 or NS_71 for S-SSB transmission for NR SL-U UE power class 5

## 6.2E.3F.16A-MPR for NS_68

When NS_68 is indicated by the network or pre-configured radio parameters for NR sidelink UE, this clause specifies the allowed Maximum Power Reduction (MPR) power for NR sidelink physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed A-MPR is specified in Table 6.2E.3F.16-1 for power class 5 NR sidelink UE.

Table 6.2E.3F.16-1: A-MPR for NS_68 NR SL-U UE power class 5

For PSFCH transmission with single RB set and multiple RB sets, the allowed A-MPR is specified in Table 6.2E.3F.16-2 for power class 5 NR sidelink UE.

Table 6.2E.3F.16-2: A-MPR for NS_68 for PSFCH transmission for NR SL-U UE power class 5

For S-SSB transmission, the allowed A-MPR is specified in Table 6.2E.3F.16-3 for power class 5 NR sidelink UE.

Table 6.2E.3F.16-3: A-MPR for NS_68 for S-SSB transmission for NR SL-U UE power class 5

## 6.2E.3F.17A-MPR for NS_69

When NS_69 is indicated by the network or pre-configured radio parameters for NR sidelink UE, this clause specifies the allowed Maximum Power Reduction (MPR) power for NR sidelink physical channels and signals due to PSCCH/PSSCH, PSFCH and S-SSB transmission.

For contiguous allocation of PSCCH and PSSCH simultaneous transmission, the allowed A-MPR is specified in Table 6.2E.3F.17-1 for power class 5 NR sidelink UE.

Table 6.2E.3F.17-1: A-MPR for NS_69 NR SL-U UE power class 5

For PSFCH transmission with single RB set and multiple RB sets, the allowed A-MPR is specified in Table 6.2E.3F.17-2 for power class 5 NR sidelink UE.

Table 6.2E.3F.17-2: A-MPR for NS_69 for PSFCH transmission for NR SL-U UE power class 5

For S-SSB transmission, the allowed A-MPR is specified in Table 6.2E.3F.17-3 for power class 5 NR sidelink UE.

Table 6.2E.3F.17-3: A-MPR for NS_69 for S-SSB transmission for NR SL-U UE power class 5

## 6.2E.4Configured transmitted power for V2X

## 6.2E.4.1General

The NR V2X UE is allowed to set its configured maximum output power PCMAX,f,c for carrier f of serving cell c in each slot. The configured maximum output power PCMAX,f,c is set within the following bounds:

PCMAX_L,f,c ≤  PCMAX,f,c  ≤  PCMAX_H,f,c with

PCMAX_L,f, c = MIN {PEMAX,c,  PPowerClass, V2X – MAX(MAX(MPRc , A-MPRc) + TIB,c , P-MPRc), PRegulatory,c }

PCMAX_H,f, c = MIN {PEMAX,c, PPowerClass, V2X,  PRegulatory,c }

where

-PCMAX,f,c is configured for PSSCH\PSCCH, S-SSB and PSFCH, respectively;

-For the total transmitted power PCMAX,PSSCH/PSCCH, PEMAX,c is the value given by IE sl-maxTransPower, defined by TS 38.331

-For the total transmitted power PCMAX,S-SSB, the PCMAX_L,f,c and PCMAX_H,f,c are defined as follows:

PCMAX_L,f,c = MIN {PPowerClass, V2X – MAX(MAX(MPRc , A-MPRc) + TIB,c , P-MPRc), PRegulatory,c}

PCMAX_H,f,c = MIN {PPowerClass, V2X,  PRegulatory,c}

-For the total transmitted power PCMAX,PSFCH, PEMAX,c is the value given by IE sl-maxTransPower when single resource pool configured is transmitted at a given time and sum of the IEs sl-maxTransPower when multiple resource pools configured are transmitted at a given time, defined by TS 38.331.

-PPowerClass,V2X is the maximum UE power specified in Table 6.2E.1.1-1 without taking into account the tolerance specified in the Table 6.2E.1.1-1;

-MPRc and A-MPRc for serving cell c are specified in clause 6.2E.2 and clause 6.2E.3 for PSSCH\PSCCH, S-SSB and PSFCH, respectively;

-TIB,c,  and P-MPRc are specified in clause 6.2.4

-PRegulatory,c= 10 - Gpost connector dBm the V2X UE is within the protected zone [12] of CEN DSRC tolling system and operating in Band n47; PRegulatory,c= 33 - Gpost connector dBm otherwise.

The maximum output power PCMAX,PSSCH and PCMAX,PSCCH are derived from PCMAX,c based on 0dB PSD offset between PSSCH and PSCCH.

For the measured configured maximum output power PUMAX,c for NR V2X sidelink transmissions non-concurrent with NR uplink transmissions, the same requirement as in clause 6.2.4 shall be applied.

When NR V2X UE is configured to co-channel coexistence operation with LTE V2X and NR SCS is configured to 30kHz the evaluation period for PUMAX,c for NR V2X sidelink is the first slot of NR SL slots overlapping with an LTE SL subframe and the PCMAX,f,c tolerances in Table 6.2.4-1 are relaxed by 1dB i.e. T(PCMAX,f,c) = T(PCMAX,f,c) +1 (dB).

For NR V2X UE supporting SL MIMO or Tx Diversity, the transmitted power is configured per each UE.

For NR V2X UE with two transmit antenna connectors at the same time, the tolerance is specified in Table 6.2E.4.1-1.

Table 6.2E.4.1-1: PCMAX,c tolerance schemes for MIMO

## 6.2E.4.2Configured transmitted power for inter-band V2X concurrent operation

When a UE is configured for simultaneous NR V2X sidelink and NR uplink transmissions for inter-band concurrent operation, the UE is allowed to set its configured maximum output power PCMAX,c,NR and PCMAX,c,V2X for the configured NR uplink carrier and the configured NR V2X carrier, respectively, and its total configured maximum output power PCMAX,c.

The configured maximum output power PCMAX c,NR(p) in slot p for the configured NR uplink carrier shall be set within the bounds:

PCMAX_L,c,NR (p) ≤  PCMAX,c,NR (p) ≤  PCMAX_H,c,NR (p)

where PCMAX_L,c,NR and PCMAX_H,c,NR are the limit as specified in clause 6.2.4.1.

The configured maximum output power PCMAX c,V2X (q) in slot q for the configured NR V2X carrier shall be set within the bounds:

PCMAX,c,V2X (q) ≤  PCMAX_H,c,V2X (q)

where PCMAX_H,c,V2X is the limit as specified in clause 6.2E.4.1.

The total UE configured maximum output power PCMAX (p,q) in a slot p of NR uplink carrier and a slot q of NR V2X sidelink that overlap in time shall be set within the following bounds for synchronous and asynchronous operation unless stated otherwise:

PCMAX_L (p,q) ≤  PCMAX (p,q)  ≤  PCMAX_H (p,q)

with

PCMAX_L (p,q) =  PCMAX_L,c,NR (p)

PCMAX_H (p,q) = 10 log10 [pCMAX_H,c,NR (p) + pCMAX_H,c,V2X (q)]

where pCMAX_H,c,V2X and pCMAX_H,c,NR are the limits PCMAX_H,c,V2X (q) and PCMAX_H,c,NR (p) expressed in linear scale.

The measured total maximum output power PUMAX over both the NR uplink and NR V2X carriers is

PUMAX = 10 log10 [pUMAX,c,NR + pUMAX,c,V2X],

where pUMAX,c,NR  denotes the measured output power of serving cell c for the configured NR uplink carrier, and pUMAX,c,V2X  denotes the measured output power for the configured NR V2X carrier expressed in linear scale.

When a UE is configured for synchronous V2X sidelink and uplink transmissions,

PCMAX_L(p, q)   –  TLOW (PCMAX_L(p, q))  ≤  PUMAX  ≤  PCMAX_H(p, q)  + THIGH (PCMAX_H(p, q))

where PCMAX_L (p,q) and PCMAX_H (p,q) are the limits for the pair (p,q) and with the tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX specified in Table 6.2E.4.1-1.. PCMAX_L may be modified for any overlapping portion of slots (p, q) and (p +1, q+1).

## 6.2E.4.3Configured transmitted power for intra-band V2X concurrent operation

For intra-band concurrent operation, if transmission of Uu and SL does not overlap in time, the configured output power PCMAX,c  specified in clause 6.2E.4.1 and 6.2.4 apply for SL and Uu transmission respectively; otherwise, if transmission of Uu and SL overlap in time, the configured maximum output power PCMAX,c  on serving cell c for SL and Uu shall be set as specified in clause 6.2E.4.1 and in clause 6.2.4, but with MPRc = MPR and A-MPRc = A-MPR with MPR and A-MPR as determined by subclause 6.2E.2.3 for both PC3 and PC2 and subclause 6.2E.3.4, respectively. There is one power management term for the UE, denoted P-MPR, and P-MPR c = P-MPR.

The total configured maximum output power PCMAX shall be set within the following bounds:

PCMAX_L ≤ PCMAX ≤ PCMAX_H

For intra-band concurrent operation when same slot pattern is used in all aggregated serving cells,

PCMAX_L  = MIN{10 log10 ∑ pEMAX,c  - TC , PPowerClass,concurrent – MAX(MAX(MPR, A-MPR) + ΔTIB,c + TC, P-MPR ) }

PCMAX_H  = MIN{10 log10 ∑ pEMAX,c , PPowerClass,concurrent}

where

-pEMAX,c is the linear value of PEMAX,c which is given by IE P-Max for Uu serving cell c or by IE sl-MaxTransPower for SL defined in [7];

-PPowerClass,concurrent is the maximum UE power specified in Table 6.2E.1.2-2 without taking into account the tolerance;

-MPR and A-MPR are specified in clause 6.2E.2 and 6.2E.3, respectively;

-TIB,c is the additional tolerance for serving cell c as specified in clause 6.2E.4.3

-P-MPR is the power management term for the UE;

-TC is the highest value TC,c among all serving cells c;

For intra-band concurrent operation, when at least one different numerology/slot pattern is used in aggregated cells, the UE is allowed to set its configured maximum output power PCMAX,c(i),i for serving cell c(i) of slot numerology type i, and its total configured maximum output power PCMAX.

The configured maximum output power PCMAX,c(i),i (p) in slot p of serving cell c(i) on slot numerology type i shall be set within the following bounds:

PCMAX_L,f,c(i),i (p) ≤  PCMAX,f,c(i), i (p) ≤  PCMAX_H,f,c(i),i (p)

where PCMAX_L,f,c (i),i (p) and PCMAX_H,f,c(i),i (p) are the limits for a serving cell c(i) of slot numerology type i as specified in clause 6.2.4.

The total UE configured maximum output power PCMAX (p,q) in a slot p of slot numerology or symbol pattern i,  and a slot q of slot numerology or symbol pattern j that overlap in time shall be set within the following bounds unless stated otherwise:

PCMAX_L(p,q) ≤  PCMAX (p,q)  ≤  PCMAX_H (p,q)

When slots p and q have different transmissions lengths and belong to different cells on same band for intra-band operation:

PCMAX_L (p,q) = MIN {10 log10 [pCMAX_L,f,c(i),Uu,i (p) + pCMAX_L,f,c(i),V2X,j (q)], PPowerClass,concurrent}

PCMAX_H (p,q) = MIN {10 log10 [pCMAX_ H,f,c(i), Uu,,i (p) + pCMAX_ H,f,c(i),V2X,j (q)], PPowerClass,concurrent}

where pCMAX_L,f,c (i),Uu,i  and pCMAX_ H,f,c(i),Uu,i  are the respective limits PCMAX_L,f,c (i),Uu,i and PCMAX_H,f,c(i),Uu,i expressed in linear scale.

TREF and Teval are specified in Table 6.2E.4.3-1 when same and different slot patterns are used in aggregated carriers. For each TREF, the PCMAX_L is evaluated per Teval and given by the minimum value taken over the transmission(s) within the Teval; the minimum PCMAX_L over the one or more Teval is then applied for the entire TREF. PPowerClass,Concurrent shall not be exceeded by the UE during any period of time.

Table 6.2E.4.3-1: PCMAX evaluation window for different slot and channel durations

The measured maximum output power PUMAX over all serving cells with same slot pattern shall be within the following range:

PCMAX_L  – MAX{TL, TLOW(PCMAX_L) }  ≤  PUMAX  ≤  PCMAX_H  +  THIGH(PCMAX_H)

PUMAX = 10 log10 ∑ pUMAX,c

where pUMAX,c  denotes the measured maximum output power for serving cell c expressed in linear scale. The tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX are specified in Table 6.2E.4.3-2. The tolerance TL is the absolute value of the lower tolerance for applicable NRV2X concurrent operation configuration as specified in Table 6.2 E.1.2-2 for intra-band NR V2X concurrent operation.

The measured maximum output power PUMAX over all serving cells, when at least one slot has a different transmission numerology or slot pattern, shall be within the following range:

P'CMAX_L–  MAX{TL, TLOW (P'CMAX_L)} ≤  P'UMAX  ≤  P'CMAX_H + THIGH (P'CMAX_H)

P'UMAX = 10 log10 ∑ p'UMAX,c

where p'UMAX,c  denotes the average measured maximum output power for serving cell c expressed in linear scale over TREF. The tolerances TLOW(P'CMAX) and THIGH(P'CMAX) for applicable values of P'CMAX are specified in Table 6.2E.4.3-2. The tolerance TL is the absolute value of the lower tolerance for applicable NR V2X concurrent operation configuration as specified in Table 6.2E.1.2-2 for intra-band NR V2X concurrent operation.

where:

P'CMAX_L  = MIN{ MIN {10log10∑( pCMAX_L,f,c(i),i), PPowerClass,concurrent} over all overlapping slots in TREF}

P'CMAX_H = MAX{ MIN{10 log10 ∑ pEMAX,c , PPowerClass,concurrent} over all overlapping slots in TREF}

Table 6.2E.4.3-2: PCMAX tolerance for SL intra-band concurrent operation

A UE supporting sidelink operation can be configured by higher layers with one or more sidelink resource pools. A sidelink resource pool can be associated with either sidelink resource allocation mode 1 or sidelink resource allocation mode 2.

For sidelink resource allocation in either mode 1 or mode 2, if UE is in RRC_CONNECTED state, and the preparation procedure time for transmission of sidelink physical channel is available before of PUSCH preparation procedure time, for transmission of Uu and SL not overlap in time, the configured output power PCMAX,c  specified in clause 6.2E.4.1 and in clause 6.2.4 apply for SL and Uu transmission respectively, otherwise, the configured maximum output power PCMAX specified in this clause shall apply.

For sidelink resource allocation mode 2, if UE is in RRC_IDLE state, sidelink transmission is based on pre-configured sidelink resource pool, the UE configured output power is determined by sidelink only, where the configured output power specified in clause 6.2E.4.1 apply.

For sidelink resource allocation mode 2, if UE is in RRC_INACTIVE state, and Uu does not support SDT, the configured output power specified in clause 6.2E.4.1 apply, otherwise, the configured maximum output power PCMAX in this clause shall apply.

## 6.2E.4AConfigured transmitted power for Sidelink CA

For intra-band contiguous/non-contiguous SL CA operation, MPRc = MPR and A-MPRc = A-MPR with MPR and A-MPR specified in subclause 6.2E.2 and subclause 6.2E.3 respectively. There is one power management term for the UE, denoted P-MPR, and P-MPR c = P-MPR. PCMAX,c  is calculated under the assumption that the transmit power is increased by the same amount in dB on all component carriers.

The total configured maximum output power PCMAX shall be set within the following bounds:

PCMAX_L ≤  PCMAX,  ≤  PCMAX_H

For SL transmission of intra-band contiguous/non-contiguous CA when same slot pattern is used in all aggregated component carriers.

PCMAX_L = MIN{10 log10 ∑ pEMAX,C - TC,PEMAX,CA,  PPowerClass, SL_CA – MAX(MAX(MPR,  A-MPR) + ΔTIB,c+TC, P-MPR ), PRegulatory }

PCMAX_H = MIN{10 log10 ∑ pEMAX,C , PEMAX,CA, PPowerClass, SL_CA, PRegulatory }

where

-For the total transmitted power PCMAX,PSSCH/PSCCH, pEMAX, C is the linear value of PEMAX,c given by the IE sl-maxTransPower for each component carrier and PEMAX, CA is the value given by the IE sl-maxTransPower-CA for maximum transmitted power of SL CA, defined by TS 38.331;

-For the total transmitted power PCMAX,S-SSB, the PCMAX_L and PCMAX_H are defined as follows:

PCMAX_L = MIN {PPowerClass, SL_CA – MAX(MAX(MPR , A-MPR) + TIB,c , P-MPR), PEMAX,CA , PRegulatory}

PCMAX_H = MIN {PPowerClass, SL_CA,  PEMAX,CA , PRegulatory}

-For the total transmitted power PCMAX,PSFCH, pEMAX,C is the linear value of PEMAX,c given by IE sl-maxTransPower when single resource pool configured is transmitted at a given time and sum of the IEs sl-maxTransPower when multiple resource pools configured are transmitted at a given time, defined by TS 38.331;

-PPowerClass, SL_CA is the maximum UE power specified in Table 6.2E.1A-1 without taking into account the tolerance;

-MPR and A-MPR are specified in subclause 6.2E.2 and subclause 6.2E.3 respectively;

-TIB,c  and P-MPR are specified in clause 6.2.4 in TS38.101-1;

-TC is the highest value TC,c among all component carriers c in the subframe over both timeslots. TC,c = 1.5 dB when NOTE 3 in Table 6.2.1-1 in TS38.101-1 applies, otherwise TC,c = 0 dB;

-PRegulatory= 10 - Gpost connector dBm when V2X UE is within the protected zone in ETSI TS 102 792 of CEN DSRC tolling system and operating in Band n47; PRegulatory= 33 - Gpost connector dBm otherwise.

The maximum output power PCMAX,PSSCH and PCMAX,PSCCH are derived from PCMAX,c based on 0dB PSD offset between PSSCH and PSCCH.

For intra-band SL CA operation, when at least one different numerology/slot pattern is used in aggregated cells, the same requirement as specified in clause 6.2E.4.3 in TS38.101-1 shall be applied.

The measured configured maximum output power PUMAX,c for sidelink CA operation, when at least one slot has a different transmission numerology or slot pattern, the same requirement as specified in clause 6.2E.4.3 in TS38.101-1 shall be applied.

## 6.2E.4FConfigured transmitted power for Sidelink Unlicensed

## 6.2E.4F.1General

The NR SL-U UE is allowed to set its configured maximum output power PCMAX,f,c for carrier f of serving cell c in each slot. The configured maximum output power PCMAX,f,c is set within the following bounds:

PCMAX_L,f,c ≤  PCMAX,f,c  ≤  PCMAX_H,f,c with

PCMAX_L,f, c = MIN {PEMAX,c,  PPowerClass, SL – MAX(MAX(MPRc , A-MPRc) + TIB,c , P-MPRc), PRegulatory,c }

PCMAX_H,f, c = MIN {PEMAX,c, PPowerClass, SL,  PRegulatory,c }

where

-PCMAX,f,c is configured for PSSCH\PSCCH, S-SSB and PSFCH, respectively;

-For the total transmitted power PCMAX,PSSCH/PSCCH, PEMAX,c is the value given by IE sl-maxTransPower, defined by TS 38.331

-For the total transmitted power PCMAX,S-SSB, the PCMAX_L,f,c and PCMAX_H,f,c are defined as follows:

PCMAX_L,f,c = MIN {PPowerClass, SL – MAX(MAX(MPRc , A-MPRc) + TIB,c , P-MPRc), PRegulatory,c}

PCMAX_H,f,c = MIN {PPowerClass, SL,  PRegulatory,c}

-For the total transmitted power PCMAX,PSFCH, PEMAX,c is the value given by IE sl-maxTransPower when single resource pool configured is transmitted at a given time and sum of the IEs sl-maxTransPower when multiple resource pools configured are transmitted at a given time, defined by TS 38.331.

-PPowerClass,SL is the maximum UE power specified in Table 6.2E.1F-1 without taking into account the tolerance specified in the Table 6.2E.1F-1;

-MPRc and A-MPRc for serving cell c are specified in clause 6.2E.2F and clause 6.2E.3F for PSSCH\PSCCH, S-SSB and PSFCH, respectively;

-TIB,c,  and P-MPRc are specified in clause 6.2.4

-PRegulatory,c= 10 - Gpost connector dBm the V2X UE is within the protected zone [12] of CEN DSRC tolling system and operating in Band n47; PRegulatory,c= 33 - Gpost connector dBm otherwise.

The maximum output power PCMAX,PSSCH and PCMAX,PSCCH are derived from PCMAX,c based on 0dB PSD offset between PSSCH and PSCCH.

For the measured configured maximum output power PUMAX,c for NR SL-U transmissions non-concurrent with NR uplink transmissions, the same requirement as in clause 6.2.4 shall be applied.

## 6.2E.4F.2Configured transmitted power for inter-band concurrent operation

When a UE is configured for simultaneous NR sidelink and NR uplink transmissions for inter-band concurrent operation, the UE is allowed to set its configured maximum output power PCMAX,c,NR and PCMAX,c,SL for the configured NR uplink carrier and the configured NR SL carrier, respectively, and its total configured maximum output power PCMAX,c.

The configured maximum output power PCMAX c,NR(p) in slot p for the configured NR uplink carrier shall be set within the bounds:

PCMAX_L,c,NR (p) ≤  PCMAX,c,NR (p) ≤  PCMAX_H,c,NR (p)

where PCMAX_L,c,NR and PCMAX_H,c,NR are the limit as specified in TS 38.101-1 clause 6.2.4.

The configured maximum output power PCMAX c,SL (q) in slot q for the configured NR SL carrier shall be set within the bounds:

PCMAX,c,SL (q) ≤  PCMAX_H,c,SL (q)

where PCMAX_H,c,SL is the limit as specified in TS 38.101-1 clause 6.2E.4F.1.

The total UE configured maximum output power PCMAX (p,q) in a slot p of NR uplink carrier and a slot q of NR sidelink that overlap in time shall be set within the following bounds for synchronous and asynchronous operation unless stated otherwise:

PCMAX_L (p,q) ≤  PCMAX (p,q)  ≤  PCMAX_H (p,q)

with

PCMAX_L (p,q) =  PCMAX_L,c,NR (p)

PCMAX_H (p,q) = 10 log10 [pCMAX_H,c,NR (p) + pCMAX_H,c,SL (q)]

where pCMAX_H,c,SL and pCMAX_H,c,NR are the limits PCMAX_H,c,SL (q) and PCMAX_H,c,NR (p) expressed in linear scale.

The measured total maximum output power PUMAX over both the NR uplink and NR SL carriers is

PUMAX = 10 log10 [pUMAX,c,NR + pUMAX,c,SL],

where pUMAX,c,NR  denotes the measured output power of serving cell c for the configured NR uplink carrier, and pUMAX,c,SL  denotes the measured output power for the configured NR SL carrier expressed in linear scale.

When a UE is configured for synchronous NR sidelink and uplink transmissions,

PCMAX_L(p, q)   –  TLOW (PCMAX_L(p, q))  ≤  PUMAX  ≤  PCMAX_H(p, q)  + THIGH (PCMAX_H(p, q))

where PCMAX_L (p,q) and PCMAX_H (p,q) are the limits for the pair (p,q) and with the tolerances TLOW(PCMAX) and THIGH(PCMAX) for applicable values of PCMAX specified in Table 6.2E.4.1-1.. PCMAX_L may be modified for any overlapping portion of slots (p, q) and (p +1, q+1).

## 6.2FTransmitter power for shared spectrum channel access

## 6.2F.1UE maximum output power

The following UE Power Classes define the maximum output power for any transmission bandwidth within the channel bandwidth of shared spectrum channel access carrier unless otherwise stated. The period of measurement shall be at least one sub frame (1ms).

Table 6.2F.1-1: UE Power Class

The UE operating shall meet the following additional requirements for maximum mean transmission power density specified in Table 6.2F.1-2 when NS is signaled and when transmission overlaps with any portion of the specified frequency range.  In case transmission overlaps multiple frequency ranges, the lowest power density requirement applies.

Table 6.2F.1-2: Additional requirements for transmit power density

## 6.2F.1AUE maximum output power for CA

## 6.2F.1A.1UE maximum output power for inter-band CA

For inter-band carrier aggregation with one uplink carrier assigned to one NR band, the transmitter power requirements in clause 6.2 apply.

For inter-band carrier aggregation with uplink assigned to two bands and including one of the bands listed in Table 6.2F.1-1, the requirements in clause 6.2.2 apply for the NR uplink carrier and clause 6.2F.2 for the carrier operating with shared spectrum access.

For inter-band carrier aggregation with uplink assigned to two NR bands and including one of the bands listed in Table 6.2F.1-1, UE maximum output power shall be measured over all component carriers from different bands. If each band has separate antenna connectors, maximum output power is defined as the sum of maximum output power from each UE antenna connector. The period of measurement shall be at least one sub frame (1 ms). The maximum output power is specified in Table 6.2A.1.3-1.

Table 6.2F.1A.1-1 void

## 6.2F.1A.2UE maximum output power for intra-band contiguous CA

For uplink intra-band contiguous carrier aggregation, the maximum output power is specified in Table 6.2F.1A.2-1. For downlink intra-band contiguous carrier aggregation with a single uplink component carrier configured in the NR-U band, the maximum output power is specified in Table 6.2F.1-1 for power class 5.

Table 6.2F.1A.2-1: UE Power Class for intra-band contiguous CA

## 6.2F.1A.2.1Additional requirements for transmit power density for intra-band contiguous CA for CA_NS_53

The UE operating shall meet the following additional requirements for maximum mean transmission power density specified in Table 6.2F.1A.2.1-1 when CA_NS_53 is signalled.

Table 6.2F.1A.2.1-1: Additional requirements for transmit power density for CA_NS_53

## 6.2F.1A.2.2Additional requirements for transmit power density for intra-band contiguous CA for CA_NS_54

The UE operating shall meet the following additional requirements for maximum mean transmission power density specified in Table 6.2F.1A.2.2-1 when CA_NS_54 is signalled and when transmission overlaps with any portion of the specified frequency range.  In case transmission overlaps multiple frequency ranges, the lowest power density requirement applies.

Table 6.2F.1A.2.2-1: Additional requirements for transmit power density for CA_NS_54

## 6.2F.1BUE maximum output power for NR-DC

For inter-band NR-DC with uplink assigned to two bands and including one of the bands listed in Table 6.2F.1-1, the requirements in clause 6.2.2 apply for the NR uplink carrier and clause 6.2F.2 for the carrier operating with shared spectrum access.

For inter-band NR-DC with uplink assigned to two bands and including one of the bands listed in Table 6.2F.1-1, the UE maximum output power shall be measured over all component carriers from different bands. If each band has separate antenna connectors, the maximum output power is defined as the sum of maximum output power from each UE antenna connector. The period of measurement shall be at least one sub frame (1 ms). The maximum output power is specified in Table 6.2B.1.3-1.

## 6.2F.1DUE maximum output power for UL MIMO

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the maximum output power for any transmission bandwidth within the channel bandwidth is specified in Table 6.2F.1D-1. The requirements shall be met with the UL MIMO configurations specified in Table 6.2D.1-2. For UE supporting UL MIMO, the maximum output power is defined as the sum of the maximum output power from both UE antenna connectors. The period of measurement shall be at least one sub frame (1 ms).

The requirements shall be met with the UL MIMO configurations of using 2-layer UL MIMO transmission with codebook of. DCI Format for UE configured in PUSCH transmission mode for uplink single-user MIMO shall be used.

Table 6.2F.1D-1 UE Power Class for UL MIMO in closed loop spatial multiplexing scheme

For UE supporting uplink full power transmission (ULFPTx) for UL MIMO, the maximum output power requirements specified in Table 6.2F.1D-1 shall be met with the PUSCH configurations specified in Table 6.2D.1-3, based upon UE’s support of uplink full power transmission mode.

## 6.2F.2UE maximum output power reduction

For UE maximum output power reduction, the general requirements of clause 6.2.2 do not apply but instead the UE is allowed to reduce the maximum output power due to higher order modulations and transmit bandwidth configurations for power class 5 according to Table 6.2F.2-1 and Table 6.2F.2-2.

For wideband operation only sub-bands which are contiguously transmitted are considered in the current version of the specification as defined in clause 6.1F.

Unless otherwise specified, pi/2 BPSK in this clause refers to both variants of pi/2 BPSK referenced in Table 6.2.2-1.

Table 6.2F.2-1: Maximum power reduction (MPR) for shared spectrum access UE power class 5

Table 6.2F.2-2: Exception MPR mapping for wideband operation

Table 6.2F.2-3: Maximum power reduction (MPR) for shared spectrum access UE power class 3

Table 6.2F.2-4: Maximum power reduction (MPR)

for shared spectrum access UE power class 3 with 2Tx

For the UE maximum output power modified by MPR, the power limits specified in clause 6.2F.4 apply.

## 6.2F.2AUE maximum output power reduction for CA

## 6.2F.2A.1UE maximum output power reduction for inter-band CA

For inter-band carrier aggregation with uplink assigned to two bands and including one of the bands listed in Table 6.2F.1-1, the requirements in clause 6.2.2 apply for the NR uplink carrier and clause 6.2F.2 for the carrier operating with shared spectrum access.

When inter-band carrier aggregation is configured with intra-band contiguous carrier aggregation in one of the bands, the requirements in clause 6.2A.2 apply for the NR uplink contiguous carrier aggregation and 6.2F.2A.2 apply for the shared spectrum band.

## 6.2F.2A.2UE maximum output power reduction for intra-band contiguous CA

For intra-band contiguous carrier aggregation, the allowed Maximum Power Reduction (MPR) for the maximum output power in Table 6.2A.1.1-1 with contiguous RB allocation is specified in Table 6.2F.2A.2-1 and Table 6.2F.2A.2-2 for UE power class 5 CA bandwidth classes B and C. For UE maximum output power reduction, the general requirements of clause 6.2.2 do not apply but instead the UE is allowed to reduce the maximum output power due to higher order modulations and transmit bandwidth configurations for power class 5 according to Table 6.2F.2A.2-1 and Table 6.2F.2A.2-2.

For wideband operation only sub-bands which are contiguously transmitted are considered in the current version of the specification as defined in clause 6.1F.

Table 6.2F.2A.2-1: Maximum power reduction (MPR) for power class 5 shared spectrum access intra-band contiguous CA for bandwidth class B and class C.

Table 6.2F.2A.2-2: Exception MPR mapping for intra-band CA wideband operation

## 6.2F.2DUE maximum output power reduction for UL MIMO

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the allowed Maximum Power Reduction (MPR) for the maximum output power in Table 6.2F.1D-1 is specified in Table 6.2F.2-1 for power class 5, and in Table 6.2F.2-3 and Table 6.2F.2-4 for power class 3. The requirements shall be met with UL MIMO configurations defined in Table 6.2D.1-2. For UE supporting UL MIMO, the maximum output power is defined as the sum of the maximum output power from both UE antenna connectors.

For UE supporting uplink full power transmission (ULFPTx) for UL MIMO, the allowed MPR for the maximum output power in Table 6.2F.1D-1 is specified in Table 6.2F.2-1 for power class 5, and in Table 6.2F.2-3 and Table 6.2F.2-4 for power class 3, and the requirements shall be met with the PUSCH configurations specified in Table 6.2D.1-3, based upon UE’s support of uplink full power transmission mode.

The same MPR requirements shall be applicable to UE with 1-layer UL MIMO transmission (either with or without ULPFTx) as with the UL MIMO configurations of using 2-layer UL MIMO transmission with codebook of.

For the UE maximum output power modified by MPR, the power limits specified in clause 6.2D.4 apply.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission, the requirements in clause 6.2F.2 apply for the power class as indicated by the ue-PowerClass field in capability signaling.

## 6.2F.3UE additional maximum output power reduction

## 6.2F.3.1General

Additional emission requirements can be signalled by the network. Each additional emission requirement is associated with a unique network signalling (NS) value indicated in RRC signalling by an NR frequency band number of the applicable operating band and an associated value in the field additionalSpectrumEmission. Throughout this specification, the notion of indication or signalling of an NS value refers to the corresponding indication of an NR frequency band number of the applicable operating band, the IE field freqBandIndicatorNR and an associated value of additionalSpectrumEmission in the relevant RRC information elements [7].

To meet the additional requirements, additional maximum power reduction (A-MPR) is allowed for the maximum output power as specified in Table 6.2F.1-1. Unless stated otherwise, the total reduction to UE maximum output power is max(MPR, A-MPR) where MPR is defined in clause 6.2F.2.

Table 6.2F.3.1-1 specifies the additional requirements with their associated network signalling values and the allowed A-MPR and applicable operating band(s) for each NS value. The mapping of NR frequency band numbers and values of the additionalSpectrumEmission to network signalling labels is specified in Table 6.2F.3.1-1A and Table 6.2F.3.1-1B. The NS_01 label with the field additionalPmax [7] absent is default for all NR bands.

Unless otherwise specified, pi/2 BPSK  refers to both variants of pi/2 BPSK referenced in Table 6.2.2-1.

Table 6.2F.3.1-1: Additional maximum power reduction (A-MPR)

Table 6.2F.3.1-1A: Mapping of network signaling label

Table 6.2F.3.1-1B: Mapping of extended network signaling label

## 6.2F.3.2A-MPR for NS_28

When "NS_28" is indicated in the cell, the A-MPR is specified in Table 6.2F.3.2-1.

Table 6.2F.3.2-1: A-MPR for NS_28 power class 5

## 6.2F.3.3A-MPR for NS_29

When "NS_29" is indicated in the cell, the A-MPR is specified in Table 6.2F.3.3-1.

Table 6.2F.3.3-1: A-MPR for NS_29 power class 5

## 6.2F.3.4A-MPR for NS_30

When “NS_30” is indicated in the cell, the A-MPR is specified in Table 6.2F.3.4-1 for power class 5 and Table 6.2F.3.4-2 for power class 3.

Table 6.2F.3.4-1: A-MPR for NS_30 power class 5

Table 6.2F.3.4-2: A-MPR for NS_30 power class 3 with 1Tx

## 6.2F.3.5A-MPR for NS_31

When "NS_31" is indicated in the cell, the A-MPR is specified in Table 6.2F.3.5-1.

Table 6.2F.3.5-1: A-MPR for NS_31 power class 5

## 6.2F.3.6A-MPR for NS_53

When “NS_53” is indicated in the cell, the A-MPR is specified in Table 6.2F.3.6-1 for power class 5 and in Table 6.2F.3.6-2 for power class 3.

Table 6.2F.3.6-1: A-MPR for NS_53 power class 5

Table 6.2F.3.6-2: A-MPR for NS_53 power class 3 with 1Tx

## 6.2F.3.7A-MPR for NS_54

When “NS_54” is indicated in the cell, the A-MPR is specified in Table 6.2F.3.7-1 for power class 5 and Table 6.2F.3.7-2 for power class 3.

Table 6.2F.3.7-1: A-MPR for NS_54 power class 5

Table 6.2F.3.7-2: A-MPR for NS_54 power class 3 with 1Tx

## 6.2F.3.8A-MPR for NS_58

When “NS_58” is indicated in the cell, the A-MPR is specified in Table 6.2F.3.8-1 for power class 5. The Table 6.2F.3.8-2 is applicable for power class 3 with 1Tx.

Table 6.2F.3.8-1: A-MPR for NS_58 power class 5

Table 6.2F.3.8-2: A-MPR for NS_58 power class 3 with 1Tx

## 6.2F.3.9A-MPR for NS_59

When "NS_59" is indicated in the cell, the A-MPR is specified in Table 6.2F.3.9-1.

Table 6.2F.3.9-1: A-MPR for NS_59 power class 5

## 6.2F.3.10A-MPR for NS_60

When "NS_60" is indicated in the cell, the A-MPR is specified in Table 6.2F.3.10-1 for power class 5. The Table 6.2F.3.10-2 is applicable for power class 3 with 1Tx and Table 6.2F.3.10-3 is applicable for power class 3 with 2Tx.

Table 6.2F.3.10-1: A-MPR for NS_60 power class 5

Table 6.2F.3.10-2: A-MPR for NS_60 power class 3 with 1Tx

Table 6.2F.3.10-3: A-MPR for NS_60 power class 3 with 2Tx

## 6.2F.3.11A-MPR for NS_61

When "NS_61" is indicated in the cell, the A-MPR is specified in Table 6.2F.3.11-1.

Table 6.2F.3.11-1: A-MPR for NS_61 power class 5

## 6.2F.3.12A-MPR for NS_63

When "NS_63" is indicated in the cell, the A-MPR is specified in Table 6.2F.3.12-1.

Table 6.2F.3.12-1: A-MPR for NS_63 power class 5

## 6.2F.3.13A-MPR for NS_64

When "NS_64" is indicated in the cell, the A-MPR is specified in Table 6.2F.3.13-1.

Table 6.2F.3.13-1: A-MPR for NS_64 power class 5

## 6.2F.3.14A-MPR for NS_65

When "NS_65" is indicated in the cell, the A-MPR is specified in Table 6.2F.3.14-1.

Table 6.2F.3.14-1: A-MPR for NS_65 power class 5

## 6.2F.3.15A-MPR for NS_66

When "NS_66" is indicated in the cell, the A-MPR is specified in Table 6.2F.3.15-1.

Table 6.2F.3.15-1: A-MPR for NS_66 power class 5

## 6.2F.3.16A-MPR for "NS_67" or "NS_71"

When "NS_67" or "NS_71" is indicated in the cell, the A-MPR is specified in Table 6.2F.3.16-1.

Table 6.2F.3.16-1: A-MPR for "NS_67" and "NS_71" power class 5

## 6.2F.3.17A-MPR for NS_68

When "NS_68" is indicated in the cell, the A-MPR is specified in Table 6.2F.3.17-1.

Table 6.2F.3.17-1: A-MPR for NS_68 power class 5

## 6.2F.3.18A-MPR for NS_69

When "NS_69" is indicated in the cell, the A-MPR is specified in Table 6.2F.3.18-1.

Table 6.2F.3.18-1: A-MPR for NS_69 power class 5

## 6.2F.3AUE additional maximum output power reduction for CA

## 6.2F.3A.1UE additional maximum output power reduction for inter-band CA

For inter-band carrier aggregation with uplink assigned to two bands and including one of the bands listed in Table 6.2F.1-1, the requirements in clause 6.2.3 apply for the NR uplink carrier and clause 6.2F.3 for the carrier operating with shared spectrum access.

## 6.2F.3A.2UE additional maximum output power reduction for intra-band CA

## 6.2F.3A.2.0General

To meet the additional requirements, additional maximum power reduction (A-MPR) is allowed for the maximum output power as specified in Table 6.2F.1A.2-1. Unless stated otherwise, the total reduction to UE maximum output power is max(MPR, A-MPR) where MPR is defined in clause 6.2F.2A.2 for intra-band carrier aggregation.

Unless otherwise specified, pi/2 BPSK refers to both variants of pi/2 BPSK referenced in Table 6.2.2-1.

## 6.2F.3A.2.1UE additional maximum output power reduction for intra-band contiguous CA

Additional emission requirements can be signalled by the network. Each additional emission requirement is associated with a unique network signalling (NS) value indicated in RRC signalling by an NR frequency band number of the applicable operating band and an associated value in the field additionalSpectrumEmission. Throughout this specification, the notion of indication or signalling of an NS value refers to the corresponding indication of an NR frequency band number of the applicable operating band, the IE field freqBandIndicatorNR and an associated value of additionalSpectrumEmission in the relevant RRC information elements [7]. Relation between NR CA band and NR frequency band is specified in Table 5.2A.1-1.

To meet the additional requirements, additional maximum power reduction (A-MPR) is allowed for the maximum output power as specified in Table 6.2F.1A.2-1. Unless stated otherwise, the total reduction to UE maximum output power is max(MPR, A-MPR) where MPR is defined in clause 6.2F.2A.2. In absence of modulation and waveform types the A-MPR applies to all modulation and waveform types.

Table 6.2F.3A.2.1-1 specifies the additional requirements with their associated network signalling values and the allowed A-MPR and applicable CA band(s) for each CA_NS value. The CA_NS_xy value indicates the additional unwanted emissions requirements that apply for intra-band contiguous CA bands with NS_xy indicated or configured in multiple uplinks serving cells, except CA_NS_01 that indicates the general emission requirements for intra-band contiguous CA bands. The mapping of NR CA band numbers and values of the additionalSpectrumEmission to network signalling labels is specified in Table 6.2F.3A.2.1-2. For any NR CA band not listed in Table 6.2F.3A.2.1-2 the network signalling label CA_NS_01 applies.

Table 6.2F.3A.2.1-1: Additional maximum power reduction (A-MPR)

Table 6.2F.3A.2.1-2: Mapping of network signalling label

## 6.2F.3A.2.2A-MPR for CA_NS_53

When "CA_NS_53" is indicated in the cell, the A-MPR is specified in Table 6.2F.3A.2.2-1.

Table 6.2F.3A.2.2-1: A-MPR for CA_NS_53 power class 5

## 6.2F.3A.2.3A-MPR for CA_NS_54

When “CA_NS_54” is indicated in the cell, the A-MPR is specified in Table 6.2F.3A.2.3-1.

Table 6.2F.3A.2.3-1: A-MPR for CA_NS_54 power class 5

## 6.2F.3DUE additional maximum output power reduction for UL MIMO

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the A-MPR values specified in clause 6.2F.3 shall apply to the maximum output power specified in Table 6.2F.1D-1. The requirements shall be met with the UL MIMO configurations specified in Table 6.2D.1-2. For UE supporting UL MIMO, the maximum output power is defined as the sum of the maximum output power from both UE antenna connector.

For UE supporting uplink full power transmission (ULFPTx) for UL MIMO, the A-MPR values specified in clause 6.2F.3 shall apply to the maximum output power specified in Table 6.2F.1D-1. The requirements shall be met with the PUSCH configurations specified in Table 6.2D.1-3, based upon UE’s support of uplink full power transmission mode.

For the UE maximum output power modified by A-MPR, the power limits specified in clause 6.2D.4 apply.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission, the requirements in clause 6.2.4 apply for the power class as indicated by the ue-PowerClass field in capability signaling.

## 6.2F.4Configured transmitted power

The requirements for configured maximum output power in clause 6.2.4 apply.

## 6.2F.4DConfigured transmitted power UL MIMO

For UE supporting UL MIMO, the transmitted power is configured per each UE.

The definitions of configured maximum output power PCMAX,c, the lower bound PCMAX_L,c, and the higher bound PCMAX_H,c specified in clause 6.2.4 shall apply to UE supporting UL MIMO, where

-PPowerClass, ΔPPowerClass and ∆TC,c are specified in clause 6.2.4 unless otherwise stated;

-MPRc is specified in clause 6.2F.2D;

-A-MPRc is specified in clause 6.2F.3.

The measured configured maximum output power PUMAX,c for serving cell c shall be within the following bounds:

PCMAX_L,c  –  MAX{TL, T LOW(PCMAX_L,c)}  ≤  PUMAX,c  ≤  PCMAX_H,c  +  T HIGH(PCMAX_H,c)

where TLOW(PCMAX_L,c) and THIGH(PCMAX_H,c) are defined as the tolerance and applies to PCMAX_L,c and PCMAX_H,c separately, while TL is the absolute value of the lower tolerance in Table 6.2F.1D-1 for the applicable operating band.

For UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the tolerance is specified in Table 6.2F.4D-1. The requirements shall be met with UL MIMO configurations specified in Table 6.2D.1-2.

For UE supporting uplink full power transmission (ULFPTx) for UL MIMO, the tolerance is specified in Table 6.2F.4D-1. The requirements shall be met with the PUSCH configurations specified in Table 6.2D.1-3, based upon UE’s support of uplink full power transmission mode.

Table 6.2F.4D-1: PCMAX,c tolerance in closed-loop spatial multiplexing scheme

## 6.2GTransmitter power for Tx Diversity

## 6.2G.1UE maximum output power for Tx Diversity

For UE supporting Tx Diversity, the maximum output power as indicated by UE power class in Table 6.2.1-1is defined as the sum of the maximum output power from all UE transmit antenna connectors. The period of measurement shall be at least one sub frame (1 ms).

When a UE indicates PC1.5 for a given band it achieves maximum power by means of Tx Diversity in the current version of the spec. Therefore, Tx Diversity is implied for PC1.5 even if the UE does not indicate Tx diversity capability.

## 6.2G.2UE maximum output power reduction for Tx Diversity

For UE supporting Tx diversity, the allowed MPR for the maximum output power is specified in Table 6.2.2-1 and table 6.2.2-1a for UE power class 3, in Table 6.2D.2-1 for UE power class 2, in Table 6.2D.2-2 and Table 6.2D.2-3 for UE power class 1.5 with 2Tx, in  Table 6.2D.2-4 and 6.2D.2-5 for UE power class 1.5 with 4 Tx. For UE power class 1.5 with 2Tx, the allowed maximum power reduction (MPR) defined in Table 6.2D.2-3 is in accordance with the indicated modifiedMPR-Behaviour specified in Table L.1-1 for channel bandwidths ≤ 100 MHz. The maximum output power is defined as the sum of the maximum output power at each UE antenna connector. If a UE that supports PC1.5 has to apply the requirements of PC2 according to the rules in clause 6.2.1, the MPR requirements in Table 6.2.2-2 apply

## 6.2G.3UE additional maximum output power reduction for Tx Diversity

For UE supporting Tx diversity, the A-MPR values specified in clause 6.2.3 shall apply to the maximum output power specified in Table 6.2.1-1, and the maximum output power is defined as the sum of the maximum output power at each UE antenna connector. Unless stated otherwise, an A-MPR of 0 dB shall be used.

## 6.2G.4Configured transmitted power for Tx Diversity

For UE supporting Tx diversity, the transmitted power is configured per each UE.

The definitions of configured maximum output power PCMAX,c, the lower bound PCMAX_L,c, and the higher bound PCMAX_H,c specified in clause 6.2.4 shall apply to UE supporting Tx diversity, where

-PPowerClass, ΔPPowerClass + ΔPPowerBoost, and ∆TC,c are specified in clause 6.2.4 unless otherwise stated;

-MPRc is specified in clause 6.2G.2;

The measured configured maximum output power PUMAX,c for serving cell c shall be within the following bounds:

PCMAX_L,c  –  MAX{TL, T LOW(PCMAX_L,c)}  ≤  PUMAX,c  ≤  PCMAX_H,c  +  T HIGH(PCMAX_H,c)

where TLOW(PCMAX_L,c) and THIGH(PCMAX_H,c) are defined as the tolerance and applies to PCMAX_L,c and PCMAX_H,c separately, while TL is the absolute value of the lower tolerance in Table 6.2.1-1 for the applicable operating band.

For UE supporting Tx diversity, the tolerance is specified in Table 6.2G.4-1 and 6.2G.4-2.

Table 6.2G.4-1: PCMAX,c tolerance for Tx Diverstiy with 2Tx

Table 6.2G.4-2: PCMAX,c tolerance for Tx Diverstiy with 4Tx

## 6.2HTransmitter power for CA with UL MIMO

## 6.2H.1Transmitter power for intra-band UL contiguous CA with UL MIMO

## 6.2H.1.1UE maximum output power for intra-band UL contiguous CA with UL MIMO

For intra-band UL contiguous CA and UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the maximum output power is defined as the sum of the maximum output power from both UE antenna connectors and all UL CCs. The period of measurement shall be at least one sub frame (1 ms), as specified in Table 6.2H.1.1-1. The requirements shall be met with the UL MIMO configurations specified in Table 6.2D.1-2 for 2 layer configuration and the PUSCH configurations specified in Table 6.2D.1-3 for ULFPTx configuration.

Table 6.2H.1.1-1: UE Power Class for intra-band UL contiguous CA with UL MIMO in closed loop spatial multiplexing scheme

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.2A.1.1 apply for at least one antenna connector for the power class as indicated by the ue-PowerClass field in capability signalling.

## 6.2H.1.2UE maximum output power reduction for intra-band UL contiguous CA with UL MIMO

For intra-band UL contiguous CA and UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the allowed Maximum Power Reduction (MPR) for the maximum output power in Table 6.2H.1.1-1 is specified in Table 6.2A.2.1-1 and Table 6.2A.2.1-2 for power class 3 CA; Table 6.2A.2.1-1b and Table 6.2A.2.1-4 for power class 2 CA; Table 6.2A.2.1-1c, 6.2A.2.1-1d, Table 6.2A.2.1-5 and Table 6.2A.2.1-6 for power class 1.5 CA.

For UE indicating mpr-ActiveCarrierEnh-r19 supported and if single CC is activated for intra-band UL contiguous CA, the allowed MPR is specified in clause 6.2D.2.

The requirements shall be met with UL MIMO configurations defined in Table 6.2D.1-2 for 2 layer configuration and the PUSCH configurations specified in Table 6.2D.1-3 for ULFPTx configuration.  For the UE maximum output power modified by MPR, the power limits specified in clause 6.2H.1.4 apply.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.2A.2.1 apply for the power class as indicated by the ue-PowerClass field in capability signaling.

## 6.2H.1.3UE additional maximum output power reduction for intra-band UL contiguous CA with UL MIMO

For intra-band UL contiguous CA and UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the A-MPR values specified in clause 6.2A.3.1.1 shall apply to the maximum output power specified in Table 6.2H.1.1-1. The requirements shall be met with UL MIMO configurations defined in Table 6.2D.1-2 for 2 layer configuration and the PUSCH configurations specified in Table 6.2D.1-3 for ULFPTx configuration.

For the UE maximum output power modified by A-MPR, the power limits specified in clause 6.2H.1.4 apply.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.2A.3.1.1 apply for the power class as indicated by the ue-PowerClass field in capability signaling.

## 6.2H.1.4Configured transmitted power for intra-band UL contiguous CA with UL MIMO

For UE supporting intra-band UL contiguous CA with UL MIMO, the transmitted power is configured per each UE.

The definitions of configured maximum output power PCMAX,c, the lower bound PCMAX_L,c, and the higher bound PCMAX_H,c specified in clause 6.2A.4.1.1 shall apply to UE supporting intra-band UL contiguous CA with UL MIMO, where

-ΔPPowerClass,CA and ∆TC,c are specified in clause 6.2A.4.1.1 unless otherwise stated;

-PPowerClass,CA is the maximum UE power specified in Table 6.2H.1.1-1 without taking into account the tolerance;

-MPR, AMPR is specified in clause 6.2H.1.2 and 6.2H.1.3;

The measured configured maximum output power PUMAX over all serving cells shall be within the following bounds:

PCMAX_L  –  MAX{TL, T LOW(PCMAX_L)}  ≤  PUMAX  ≤  PCMAX_H  +  T HIGH(PCMAX_H)

where TLOW(PCMAX_L) and THIGH(PCMAX_H) are defined as the tolerance and applies to PCMAX_L and PCMAX_H separately, while TL is the absolute value of the lower tolerance in Table 6.2H.1.1-1 for the applicable operating band.

For UE supporting intra-band UL contiguous CA with UL MIMO, the tolerance is specified in Table 6.2H.1.4-1.

Table 6.2H.1.4-1: PCMAX tolerance for intra-band UL contiguous CA with UL MIMO

## 6.2H.2Void

## 6.2H.3Transmitter power for inter-band UL CA with UL MIMO

## 6.2H.3.1UE maximum output power for inter-band UL CA with UL MIMO

For inter-band UL CA with 2Tx UL MIMO in at least one of the two frequency bands, the maximum output power is defined as the sum of the maximum output power from all UE antenna connectors and all UL CCs, as specified in Table 6.2H.3.1-1. Unless otherwise specified, all band combinations in Table 6.2H.3.1-1 are enabled for 2Tx in one band and 1Tx in the second band.  The per band power class for each band applicable to REFSENS exceptions for a given inter-band ULCA power class with 3Tx and 4Tx are specified in Table 6.2H.3.1-2 and 6.2H.3.1-3 respectively. The power classes for each constituent band of these configurations are those specified in the references below:

-For the 1Tx band, in Table 6.2.1-1,

-For the 2Tx band supporting Tx Diversity, in Clause 6.2G.1,

-For the 2Tx band, in Table 6.2D.1-1.

The power classes referenced are according to the reported ue-PowerClassPerBandPerBC-r17 if indicated or ue-PowerClass otherwise. The period of measurement shall be at least one sub frame (1 ms). The requirements shall be met with the UL MIMO configurations specified in Table 6.2D.1-2 and 6.2D.1-3 for 2-layer configuration and ULFPTx configuration respectively for a component carrier configured with UL MIMO.

If higherPowerLimit-r17 is indicated for an UL inter-band CA configuration with UL-MIMO as specified in Table 6.2H.3.1-1 and with uplink bands of different power class capabilities, the UE maximum output power specified in Table 6.2H.3.1-1 for this UL CA configuration is modified in accordance with sub-clause 6.2H.3.4.

Table 6.2H.3.1-1: UE Power Class for inter-band UL CA with 2Tx UL MIMO or TxD in at least one frequency band.

Table 6.2H.3.1-2: Per band power class applicable to REFSENS exceptions (two band UL CA with 2Tx in one band and with 1Tx in the other band)

Table 6.2H.3.1-3: Per band power class applicable to REFSENS exceptions (two band UL CA with 2Tx in each band)

If a UE supports power class 2 for the band combination listed in Table 6.2H.3.1-1:

–if the field of UE capability maxUplinkDutyCycle-interBandCA-PC2 is present and the average percentage of uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-interBandCA-PC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

–if 10log10 ∑ pEMAX,c or PEMAX,CA which defined in clause 6.2H.3.4 is 23dBm or lower;

–shall apply all requirements for the default power class and set the configured transmitted power as specified in clause 6.2H.3.4;

–else;

–shall apply all requirements for the power class 2 and set the configured transmitted power as specified in clause 6.2H.3.4 (regardless of the average percentage of uplink symbols if the field of UE capability maxUplinkDutyCycle-interBandCA-PC2 is absent).

The average percentage of uplink symbols is defined as 0.5*(DutyNR, x /maxDutyNR,x + DutyNR, y /maxDutyNR,y, ). DutyNR, x, DutyNR, y represent the actual percentage of uplink symbols transmitted in the same evaluation period (The exact evaluation period is no less than one radio frame) for NR Band x, NR Band y respectively; maxDutyNR,x, maxDutyNR,y represent the field of UE capability maxUplinkDutyCycle-PC2-FR1 per band as defined in TS 38.331.  For NR Band x or NR Band y,

–if power class of one or both of the bands within the band combination is power class 2 and the corresponding UE capability maxUplinkDutyCycle-PC2-FR1 is absent;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 50%;

–else if the IE P-Max as defined in TS 38.331 [7] is provided for this band and set to 23 dBm or lower;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 100%.

If a UE supports power class 1.5 for the band combination listed in Table 6.2H.3.1-1:

–if the field of UE capability maxUplinkDutyCycle-interBandCA-PC2 is present and the average percentage of uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-interBandCA-PC2 (The exact evaluation period is no less than one radio frame); or

–if 10log10 ∑ pEMAX,c or PEMAX,CA which defined in clause 6.2H.3.4 is 23dBm or lower;

–shall apply all requirements for the default power class and set the configured transmitted power as specified in clause 6.2H.3.4;

–if the field of UE capability maxUplinkDutyCycle-interBandCA-PC2 is present and the average percentage of uplink symbols transmitted in a certain evaluation period is larger than 0.5maxUplinkDutyCycle-interBandCA-PC2 but less than or equal to maxUplinkDutyCycle-interBandCA-PC2; or

–if 10log10 ∑ pEMAX,c or PEMAX,CA which defined in clause 6.2H.3.4 is between 23dBm and 26dBm;

–shall apply all requirements for the power class 2 and set the configured transmitted power as specified in clause 6.2H.3.4;

–else;

–shall apply all requirements for the power class 1.5 and set the configured transmitted power as specified in clause 6.2H.3.4 (regardless of the average percentage of uplink symbols if the field of UE capability maxUplinkDutyCycle-interBandCA-PC2 is absent).

The average percentage of uplink symbols is defined as 0.5*(DutyNR, x /maxDutyNR,x + DutyNR, y /maxDutyNR,y, ). DutyNR, x, DutyNR, y represent the actual percentage of uplink symbols transmitted in the same evaluation period (The exact evaluation period is no less than one radio frame) for NR Band x, NR Band y respectively; maxDutyNR,x, maxDutyNR,y represent the field of UE capability 0.5maxUplinkDutyCycle-PC2-FR1 or maxUplinkDutyCycle-PC1dot5-MPE-FR1 per band as defined in TS 38.331.  For NR Band x or NR Band y,

–if power class of one band within the band combination is power class 1.5

–if the corresponding UE capability 0.5*maxUplinkDutyCycle-PC2-FR1 and maxUplinkDutyCycle-PC1dot5-MPE-FR1 are both absent;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 25%;

–else if only one of the corresponding UE capability 0.5*maxUplinkDutyCycle-PC2-FR1 and maxUplinkDutyCycle-PC1dot5-MPE-FR1 is reported;

–the corresponding maxDutyNR,x or maxDutyNR,y is according to the reported capability;

–else

–the corresponding maxDutyNR,x or maxDutyNR,y is the smaller of maxUplinkDutyCycle-PC1dot5-MPE-FR1 and 0.5*maxUplinkDutyCycle-PC2-FR1;

–if power class of one or both of the bands within the band combination is power class 2

–if the corresponding UE capability maxUplinkDutyCycle-PC2-FR1 is absent;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 50%;

–else the corresponding UE capability maxUplinkDutyCycle-PC2-FR1 is reported;

–the corresponding maxDutyNR,x or maxDutyNR,y is according to the reported capability;

–if the IE P-Max as defined in TS 38.331 [7] is provided for this band and set to 23 dBm or lower;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 100%.

## 6.2H.3.2UE maximum output power reduction for inter-band UL CA with UL MIMO

For inter-band UL CA with UL MIMO in at least one of the two frequency bands, the requirements in clause 6.2D.2 apply for a component carrier configured with UL MIMO, and for a component carrier not configured for UL MIMO, the requirements in clause 6.2G.2 apply if it supports TxD and the requirements in clause 6.2.2 apply if it does not support TxD .

## 6.2H.3.3UE additional maximum output power reduction for inter-band UL CA with UL MIMO

For inter-band UL CA with UL MIMO in at least one of the two frequency bands, unless specified in Table 6.2A.3.1.3-1, the requirements in clause 6.2.3 apply only to the indicated carrier.

## 6.2H.3.4Configured transmitted power for inter-band UL CA with UL MIMO

For inter-band UL CA with UL MIMO in at least one of the two frequency bands, the requirements in clause 6.2A.4.1.3 apply except that:

-PPowerClass,CA is the maximum UE power specified in Table 6.2H.3.1-1 without taking into account the tolerance;

If the UE indicates higherPowerLimit-r17 for an UL inter-band CA configuration with uplink bands of different power class capabilities specified in Table 6.2H.3.1-1 and ΔPPowerClass, CA = 0, PPowerClass,CA is replaced by 10 log10 ∑ pPowerClass,c.

-MPRc and A-MPRc are specified in clause 6.2D.2 and clause 6.2D.3 respectively for the component carrier configured with UL MIMO.

-ΔPPowerClass,CA:

–For a power class 2 UE, it is 3dB when the requirements of default power class are applied as specified in sub-clause 6.2.H.3.1, otherwise ΔPPowerClass, CA = 0 dB;

–For a power class 1.5 UE, it is 6dB when the requirements of default power class are applied as specified in sub-clause 6.2.H.3.1; and it is 3dB when the requirements of power class 2 are applied as specified in sub-clause 6.2.H.3.1; otherwise ΔPPowerClass, CA = 0 dB;

## 6.2ITransmitter power for (e)RedCap

## 6.2I.1Maximum output power for RedCap

For (e)Redcap UE, the requirements for power class 3 specified in clause 6.2.1 apply.

For (e)Redcap UE supporting PC2, the requirements specified for PC2 in clause 6.2.1 apply.

## 6.2JTransmitter power for ATG

## 6.2J.0Reserved

## 6.2J.0DGeneral

UE can indicate rated output power for the single configured UL CC with DL CA as specified in 6.2J.1 and if UE supports UL MIMO in this carrier, UE can indicate rated output power for the CA configuration as specified in 6.2J.1D.

## 6.2J.1UE maximum output power for ATG

For the ATG UE, the rated maximum output power is reported via UE capability maxOutputPowerATG-r18 at maximum modulation order reported by ATG UE and full PRB configurations within the channel bandwidth of NR carrier unless otherwise stated. The period of measurement shall be at least one sub frame (1ms). UE capability maxOutputPowerATG-r18 is an integer value in the range 23 to 40 dBm.

For ATG UE with multiple omni-directional antennas not indicating the capability antennaArrayType-r18, the measured maximum output power Pmax,c,AC shall remain within +2 dB and -2 dB of the rated maximum output power Prated,c,AC  reported by the ATG UE.

For ATG UE with antenna array indicating the capability antennaArrayType-r18, the measured maximum output power Pmax,c,TABC shall remain within +2 dB and -2 dB of the rated maximum output power Prated,c,TABC reported by the ATG UE.

## 6.2J.1AUE maximum output power for ATG CA

## 6.2J.1A.1UE maximum output power for ATG intra-band contiguous CA

For downlink intra-band contiguous carrier aggregation with a single uplink component carrier configured in the NR band, the rated output power specified in 6.2J.1 apply.

## 6.2J.1A.2UE maximum output power for ATG inter-band CA

For inter-band downlink carrier aggregation with one uplink carrier assigned to one NR band, the transmitter power requirements in 6.2J.1 apply.

## 6.2J.1A.3(void)

## 6.2J.1DUE maximum output power for ATG UL MIMO

For UE supporting UL MIMO, the rated maximum output power is defined as the sum of the rated maximum output power from all UE antenna connectors or all UE TAB connectors, which is reported via UE capability maxOutputPowerATG-r18 at maximum modulation order reported by ATG UE and full PRB configurations within the channel bandwidth of NR carrier unless otherwise stated. The period of measurement shall be at least one sub frame (1 ms). UE capability maxOutputPowerATG-r18 is an integer value in the range 23 to 40 dBm.

-For ATG UE with multiple omni-directional antennas not indicating the capability antennaArrayType-r18, the measured maximum output power over all UE antenna connectors Pmax,c,AC shall remain within +2 dB and -2 dB of the rated maximum output power Prated,c,AC reported.

-For ATG UE with antenna array indicating the capability antennaArrayType-r18, the measured maximum output power over all UE TAB connectors Pmax,c,TABC shall remain within +2 dB and -2 dB of the rated maximum output power Prated,c,TABC reported.

For ATG UE with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer) in closed-loop spatial multiplexing scheme, the requirements shall be met with the UL MIMO configurations specified in Table 6.2J.1D-1. The requirements shall be met with the UL MIMO configurations of using 2-layer UL MIMO codebook-based transmission with precoding matrix of W=. DCI Format for UE configured in PUSCH transmission mode for uplink single-user MIMO shall be used.

Table 6.2J.1D-1: UL MIMO configuration in closed-loop spatial multiplexing scheme

For UE supporting uplink full power transmission (ULFPTx) for UL MIMO, the rated output power requirements shall be met with the PUSCH configurations specified in Table 6.2J.1D-2, based upon UE’s support of uplink full power transmission mode.

Table 6.2J.1D-2: PUSCH Configuration for uplink full power transmission (ULFPTx)

If the UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.2J.1 apply for at least one antenna connector or one group of TAB connector for rated output power as indicated by the ue-PowerClass field in capability signalling.

A UE with 2Tx indicating the feature ul-FullPwrMode-r16 or ul-FullPwrMode2-TPMIGroup-r16 for a band shall meet the requirement in clause 6.2J.1 for at least one antenna connector when scheduled for single antenna-port transmission by DCI format 0_0 or by DCI format 0_1 for codebook-based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211].

## 6.2J.2Configured transmitted power for ATG

The UE is allowed to set its configured maximum output power PCMAX,f,c for carrier f of serving cell c in each slot. The configured maximum output power PCMAX,f,c is set within the following bounds:

PCMAX_L,f,c ≤  PCMAX,f,c  ≤  PCMAX_H,f,c with

PCMAX_L,f,c = MIN {PEMAX,c, Prated,c,AC or Prated,c,TABC}

PCMAX_H,f,c = PEMAX,c

where

PEMAX,c is the value given by ATG specific the p-Max IE or the field additionalPmax of the NR-NS-PmaxList IE], whichever is applicable according to TS 38.331[7]; It’s noted that the actual PEMAX,c value is (9 + field value) in ATG cell, according to p-Max IE definition in TS 38.331 [7];

Prated,c,AC is the rated maximum output power at maximum modulation order and full PRB configurations which is indicated by ATG UE capability maxOutputPowerATG-r18 for ATG UE with multiple omni-directional antennas not indicating the capability antennaArrayType-r18;

Prated,c,TABC is the rated maximum output power at maximum modulation order and full PRB configurations which is indicated by ATG UE capability maxOutputPowerATG-r18 for ATG UE with antenna array indicating the capability antennaArrayType-r18.

TREF and Teval are specified in Table 6.2J.2-0. For each TREF, the PCMAX,L,c for serving cell c are evaluated per Teval and given by the minimum  value taken over the transmission(s) within the Teval; the minimum PCMAX_L,f,c over one or more Teval is then applied for the entire TREF

Table 6.2J.2-0: Evaluation and reference periods for PCMAX

The measured configured maximum output power PUMAX,f,c shall be within the following bounds:

PCMAX_L,f,c  – T(PCMAX_L,f,c)  ≤  PUMAX,f,c  ≤  PCMAX_H,f,c  +  T(PCMAX_H,f,c).

where the tolerance T(PCMAX,f,c) for applicable values of PCMAX,f,c is specified in Table 6.2J.2-1.

Table 6.2J.2-1: ATG PCMAX tolerance

## 6.2J.2DConfigured transmitted power for UL MIMO

For ATG UE supporting UL MIMO, the transmitted power is configured per each UE.

The definitions of configured maximum output power PCMAX,c, the lower bound PCMAX_L,c, and the higher bound PCMAX_H,c specified in clause 6.2J.2 shall apply to UE supporting UL MIMO.

The measured configured maximum output power PUMAX,c for serving cell c shall be within the following bounds:

PCMAX_L,c  –  MAX{TL, T LOW(PCMAX_L,c)}  ≤  PUMAX,c  ≤  PCMAX_H,c  +  T HIGH(PCMAX_H,c)

where TLOW(PCMAX_L,c) and THIGH(PCMAX_H,c) are defined as the tolerance and applies to PCMAX_L,c and PCMAX_H,c separately, while TL is the absolute value of the lower tolerance in 6.2J.1.

For UE with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer) in closed-loop spatial multiplexing scheme, the tolerance is specified in Table 6.2J.2D-1. The requirements shall be met with UL MIMO configurations specified in Table 6.2J.1D-1.

For UE support uplink full power transmission (ULFPTx) for UL MIMO, the tolerance is specified in Table 6.2J.2D-1. The requirements shall be met with the PUSCH configurations specified in Table 6.2J.1D-2, based upon UE’s support of uplink full power transmission mode.

Table 6.2J.2D-1: PCMAX,c tolerance in closed-loop spatial multiplexing scheme

If the UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook-based transmission, the corresponding requirements in clause 6.2J.1D apply for the rated output power as indicated by the maxOutputPowerATG-r18 field in capability signaling.

## 6.2KTransmitter power for Aerial UE

## 6.2K.1Maximum output power for Aerial UE

For Aerial UE, the requirements for power class 3 specified in clause 6.2.1 apply.

## 6.2K.2Maximum output power reduction for Aerial UE

For Aerial UE, the requirements specified in clause 6.2.2 apply.

## 6.2K.3Additional maximum output power reduction for Aerial UE

## 6.2K.3.1General

Additional emission requirements can be signalled by the network. Each additional emission requirement is associated with a unique network signalling (NS) value indicated in RRC signalling by an NR frequency band number of the applicable operating band and an associated value in the field additionalSpectrumEmission as described in Clause 5.2.2.4 of [7]. In this specification, NS_UAV refers to a network signalling value applicable only for Aerial UEs [7]. The notion of indication or signalling of an NS_UAV value refers to the corresponding indication of an NR frequency band number of the applicable operating band, the IE field frequencyBandListAerial and an associated value of additionalSpectrumEmission in the relevant RRC information elements [7].

To meet the additional requirements, additional maximum power reduction (A-MPR) is allowed for the maximum output power as specified in Table 6.2.1-1. Unless stated otherwise, the total reduction to UE maximum output power is max(MPR, A-MPR) where MPR is defined in clause 6.2.2. Outer and inner allocation notation used in clause 6.2K.3 are defined in clause 6.2.2. Unless stated otherwise, Edge RB allocations get the same AMPR as Outer RB allocations. In absence of modulation and waveform types the A-MPR applies to all modulation and waveform types.

Table 6.2K.3.1-1 specifies the additional requirements with their associated Network Signalling label and the allowed A-MPR and applicable operating band(s). The mapping of NR frequency band numbers and values of the additionalSpectrumEmission to network signalling labels is specified in Table 6.2.3.1-1A.

For almost contiguous allocations in CP-OFDM waveforms in power class 3, the allowed A-MPR defined in clause 6.2K.3 is increased by CEIL{ 10 log10(1 + NRB_gap / NRB_alloc), 0.5 } dB, where CEIL{x, 0.5} means x rounding upwards to closest 0.5dB, NRB_gap is the total number of unallocated RBs between allocated RBs and NRB_alloc is the total number of allocated RBs, and the parameter LCRB is replaced by NRB_alloc + NRB_gap in specifying the RB allocation regions.

Unless otherwise specified, pi/2 BPSK refers to both variants of pi/2 BPSK referenced in Table 6.2.2-1.

Table 6.2K.3.1-1: Additional Maximum Power Reduction (A-MPR) for Uncrewed Aerial UE

Table 6.2K.3.1-1A: Mapping of network signalling label

## 6.2K.3.2A-MPR for NS_UAV_44

Table 6.2K.3.2-1: A-MPR regions for NS_UAV_44

Table 6.2K.3.2-2: A-MPR for NS_UAV_44

## 6.2K.3.3A-MPR for NS_UAV_70

Table 6.2K.3.3-1: A-MPR regions for NS_UAV_70 (Power Class 3)

Table 6.2K.3.3-2: A-MPR for NS_UAV_70 (Power Class 3)

## 6.2K.4Configured transmitted power for Aerial UE

For the Aerial UE, the requirements in clause 6.2.4 apply with the following modifications:

-only requirements related to Power Class 3 UEs are applicable for Aerial UEs. In the current Release Aerial UEs that are not PC3 are not considered; and

-when NR-NS-PmaxValueAerial is configured for the applicable operating band, the UE shall not consider the value of the additionalPmax of the NR-NS-PmaxList IE. In such case, the value of additionalPmax to be considered is the one related to NR-NS-PmaxValueAerial, when configured, according to TS 38.331[7]; and

-when determining the parameters in the formulas used to calculate the UE configured transmitted power, use clause 6.2K.3 for A-MPR determination instead of clause 6.2.3, whenever frequencyBandListAerial is configured for the operating band.

NOTE:When the aerial UE is not configured with NR-NS-PmaxValueAerial the determination of whether to use and which value to use for additionalPmax shall be performed as described in clause 6.2.4.

## 6.2LTransmitter power for CA with Tx Diversity

## 6.2L.1Void

## 6.2L.2Void

## 6.2L.3Transmitter power for inter-band UL CA with Tx Diversity

## 6.2L.3.1UE maximum output power for inter-band UL CA with Tx Diversity

For inter-band UL CA with Tx Diversity in at least one of the two frequency bands and neither band is configured with UL MIMO, the maximum output power is defined as the sum of the maximum output power from all UE antenna connectors and all UL CCs, as specified in Table 6.2H.3.1-1. The period of measurement shall be at least one sub frame (1 ms). For inter-band UL CA with UL MIMO in at least one of the two frequency bands, refer to clause 6.2H.3.

The per band power class for each band applicable to REFSENS exceptions for a given inter-band ULCA power class are specified in Tables 6.2H.3.1-2 and 6.2H.3.1-3. These configurations are subject to the applicable power class of each NR band as specified in Table 6.2.1-1. The power classes referenced are according to the reported ue-PowerClassPerBandPerBC-r17 if indicated or ue-PowerClass otherwise.

If higherPowerLimit-r17 is indicated for an UL inter-band CA configuration with Tx Diversity as specified in Table 6.2H.3.1-1 and with uplink bands of different power class capabilities, the UE maximum output power for this UL CA configuration specified in Table 6.2H.3.1-1 is increased in accordance with sub-clause 6.2L.3.4.

Table 6.2L.3.1-1: Void

If a UE supports power class 2 for the band combination listed in Table 6.2H.3.1-1:

–if the field of UE capability maxUplinkDutyCycle-interBandCA-PC2 is present and the average percentage of uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-interBandCA-PC2 as defined in TS 38.331 (The exact evaluation period is no less than one radio frame); or

–if 10log10 ∑ pEMAX,c or PEMAX,CA which defined in clause 6.2L.3.4 is 23dBm or lower;

–shall apply all requirements for the default power class and set the configured transmitted power as specified in clause 6.2L.3.4;

–else;

–shall apply all requirements for the power class 2 and set the configured transmitted power as specified in clause 6.2L.3.4 (regardless of the average percentage of uplink symbols if the field of UE capability maxUplinkDutyCycle-interBandCA-PC2 is absent).

The average percentage of uplink symbols is defined as 0.5*(DutyNR, x /maxDutyNR,x + DutyNR, y /maxDutyNR,y, ). DutyNR, x, DutyNR, y represent the actual percentage of uplink symbols transmitted in the same evaluation period (The exact evaluation period is no less than one radio frame) for NR Band x, NR Band y respectively; maxDutyNR,x, maxDutyNR,y represent the field of UE capability maxUplinkDutyCycle-PC2-FR1 per band as defined in TS 38.331.  For NR Band x or NR Band y,

–if power class of one or both of the bands within the band combination is power class 2 and the corresponding UE capability maxUplinkDutyCycle-PC2-FR1 is absent;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 50%;

–else if the IE P-Max as defined in TS 38.331 [7] is provided for this band and set to 23 dBm or lower;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 100%.

If a UE supports power class 1.5 for the band combination listed in Table 6.2H.3.1-1:

–if the field of UE capability maxUplinkDutyCycle-interBandCA-PC2 is present and the average percentage of uplink symbols transmitted in a certain evaluation period is larger than maxUplinkDutyCycle-interBandCA-PC2 (The exact evaluation period is no less than one radio frame); or

–if 10log10 ∑ pEMAX,c or PEMAX,CA which defined in clause 6.2L.3.4 is 23dBm or lower;

–shall apply all requirements for the default power class and set the configured transmitted power as specified in clause 6.2L.3.4;

–if the field of UE capability maxUplinkDutyCycle-interBandCA-PC2 is present and the average percentage of uplink symbols transmitted in a certain evaluation period is larger than 0.5maxUplinkDutyCycle-interBandCA-PC2 but less than or equal to maxUplinkDutyCycle-interBandCA-PC2; or

–if 10log10 ∑ pEMAX,c or PEMAX,CA which defined in clause 6.2L.3.4 is between 23dBm and 26dBm;

–shall apply all requirements for the power class 2 and set the configured transmitted power as specified in clause 6.2L.3.4;

–else;

–shall apply all requirements for the power class 1.5 and set the configured transmitted power as specified in clause 6.2L.3.4 (regardless of the average percentage of uplink symbols if the field of UE capability maxUplinkDutyCycle-interBandCA-PC2 is absent).

The average percentage of uplink symbols is defined as 0.5*(DutyNR, x /maxDutyNR,x + DutyNR, y /maxDutyNR,y, ). DutyNR, x, DutyNR, y represent the actual percentage of uplink symbols transmitted in the same evaluation period (The exact evaluation period is no less than one radio frame) for NR Band x, NR Band y respectively; maxDutyNR,x, maxDutyNR,y represent the field of UE capability 0.5*maxUplinkDutyCycle-PC2-FR1 or maxUplinkDutyCycle-PC1dot5-MPE-FR1 per band as defined in TS 38.331.  For NR Band x or NR Band y,

–if power class of one band within the band combination is power class 1.5

–if the corresponding UE capability 0.5*maxUplinkDutyCycle-PC2-FR1 and maxUplinkDutyCycle-PC1dot5-MPE-FR1 are both absent;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 25%;

–else if only one of the corresponding UE capability 0.5*maxUplinkDutyCycle-PC2-FR1 and maxUplinkDutyCycle-PC1dot5-MPE-FR1 is reported;

–the corresponding maxDutyNR,x or maxDutyNR,y is according to the reported capability;

–else

–the corresponding maxDutyNR,x or maxDutyNR,y is the smaller of maxUplinkDutyCycle-PC1dot5-MPE-FR1 and 0.5*maxUplinkDutyCycle-PC2-FR1;

–if power class of one or both of the bands within the band combination is power class 2

–if the corresponding UE capability maxUplinkDutyCycle-PC2-FR1 is absent;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 50%;

–else the corresponding UE capability maxUplinkDutyCycle-PC2-FR1 is reported;

–the corresponding maxDutyNR,x or maxDutyNR,y is according to the reported capability;

–if the IE P-Max as defined in TS 38.331 [7] is provided for this band and set to 23 dBm or lower;

–the corresponding maxDutyNR,x or maxDutyNR,y is equal to 100%.

## 6.2L.3.2UE maximum output power reduction for inter-band UL CA with Tx Diversity

For inter-band UL CA with Tx Diversity in at least one of the two frequency bands and neither band is configured with UL MIMO, the requirements in clause 6.2G.2 apply for a component carrier supporting Tx Diversity and the requirements in clause 6.2.2 apply for a component carrier not supporting Tx Diversity.  For inter-band UL CA with UL MIMO in at least one of the two frequency bands, refer to clause 6.2H.3.

## 6.2L.3.3UE additional maximum output power reduction for inter-band UL CA with Tx Diversity

For inter-band UL CA with Tx Diversity in at least one of the two frequency bands and neither band is configured with UL MIMO, unless specified in Table 6.2A.3.1.3-1, the requirements in clause 6.2.3 apply only to the indicated carrier For inter-band UL CA with UL MIMO in at least one of the two frequency bands, refer to clause 6.2H.3.

## 6.2L.3.4Configured transmitted power for inter-band UL CA with Tx Diversity

For inter-band UL CA with Tx Diversity in at least one of the two frequency bands and neither band is configured with UL MIMO, the requirements in clause 6.2A.4.1.3 apply except that:

-PPowerClass,CA is the maximum UE power specified in Table 6.2H.3.1-1 without taking into account the tolerance;

If the UE indicates higherPowerLimit-r17 for an UL inter-band CA configuration with uplink bands of different power class capabilities specified in Table 6.2H.3.1-1 and ΔPPowerClass, CA = 0, PPowerClass,CA is replaced by 10 log10 ∑ pPowerClass,c.

-MPRc and A-MPRc are specified in clause 6.2G.2 and clause 6.2G.3 respectively for the component carrier configured with Tx Diversity.

-ΔPPowerClass,CA:

–For a power class 2 UE, it is 3dB when the requirements of default power class are applied as specified in sub-clause 6.2.L.3.1, otherwise ΔPPowerClass, CA = 0 dB;

–For a power class 1.5 UE, it is 6dB when the requirements of default power class are applied as specified in sub-clause 6.2.L.3.1; and it is 3dB when the requirements of power class 2 are applied as specified in sub-clause 6.2.L.3.1; otherwise ΔPPowerClass, CA = 0 dB;

For inter-band UL CA with UL MIMO in at least one of the two frequency bands, refer to clause 6.2H.3.

## 6.3Output power dynamics

## 6.3.1Minimum output power

The minimum controlled output power of the UE is defined as the power in the channel bandwidth for all transmit bandwidth configurations (resource blocks), when the power is set to a minimum value.

The minimum output power is defined as the mean power in at least one sub-frame 1 ms. The minimum output power shall not exceed the values specified in Table 6.3.1-1.

Table 6.3.1-1: Minimum output power

## 6.3.2Transmit OFF power

Transmit OFF power is defined as the mean power in the channel bandwidth when the transmitter is OFF. The transmitter is considered OFF when the UE is not allowed to transmit on any of its ports.

The transmit OFF power is defined as the mean power in a duration of at least one sub-frame (1 ms) excluding any transient periods. The transmit OFF power shall not exceed the values specified in Table 6.3.2-1.

Table 6.3.2-1: Transmit OFF power

## 6.3.3Transmit ON/OFF time mask

## 6.3.3.1General

The transmit power time mask defines the transient period(s) allowed

-between transmit OFF power as defined in clause 6.3.2 and transmit ON power symbols (transmit ON/OFF)

-between continuous ON-power transmissions with power change or RB hopping is applied. When a UE signals the transient period capability, the transient period value (tp) can be 2, 4, or 7s. If no capability is signalled, the default transient period value of 10s applies.

In case of RB hopping, and in following figures where tpstart is specified, the transient period is shared symmetrically when the transient period is 10usec. If the UE signals a transient period (tp) of 2, 4 or 7s, the transient period start position is given by tpstart in Table 6.3.3.1-1.

Table 6.3.3.1-1 tpstart  values

Unless otherwise stated the requirements in clause 6.5 apply also in transient periods.

In the following clauses, following definitions apply:

-A slot or long subslot transmission is a transmission with more than 2 symbols.

-A short subslot transmission is a transmission with 1 or 2 symbols.

## 6.3.3.2General ON/OFF time mask

The general ON/OFF time mask defines the observation period between transmit OFF and ON power and between transmit ON and OFF power for each SCS. ON/OFF scenarios include contiguous, and non-contiguous transmission, etc.

The OFF power measurement period is defined in a duration of at least one slot excluding any transient periods. The ON power is defined as the mean power over one slot excluding any transient period.

Figure 6.3.3.2-1: General ON/OFF time mask for NR UL transmission in FR1

## 6.3.3.3Transmit power time mask for slot and short or long subslot boundaries

The transmit power time mask for slot and a long subslot transmission boundaries defines the transient periods allowed between slot and long subslot PUSCH transmissions. For PUSCH-PUCCH and PUSCH-SRS transitions and multiplexing the time masks in clause 6.3.3.7 apply.

The transmit power time mask for slot or long subslot and short subslot transmission boundaries defines the transient periods allowed between slot or long subslot and short subslot transmissions. The time masks in clause 6.3.3.8 apply.

The transmit power time mask for short subslot transmission boundaries defines the transient periods allowed between short subslot transmissions. The time masks in clause 6.3.3.9 apply.

## 6.3.3.4PRACH time mask

The PRACH ON power is specified as the mean power over the PRACH measurement period excluding any transient periods as shown in Figure 6.3.3.4-1. The measurement period for different PRACH preamble format is specified in Table 6.3.3.4-1.

Table 6.3.3.4-1: PRACH ON power measurement period

Figure 6.3.3.4-1: PRACH ON/OFF time mask

## 6.3.3.5Void

## 6.3.3.6SRS time mask

For SRS transmission mapped to one OFDM symbol, the ON power is defined as the mean power over the symbol duration excluding any transient period; See Figure 6.3.3.6-1

Figure 6.3.3.6-1: Single SRS time mask for NR UL transmission

For SRS transmission mapped to two or more OFDM symbols the ON power is defined as the mean power for each symbol duration excluding any transient period. For consecutive SRS transmissions without power change, Figure 6.3.3.6-2 applies.

Figure 6.3.3.6-2: Consecutive SRS time mask for the case when no power change is required with SRS usage other than antenna switching.

When power change between consecutive SRS transmissions is required, then Figure 6.3.3.6-3 and Figure 6.3.3.6-4 apply.

Figure 6.3.3.6-3: Consecutive SRS time mask for the case when power change is required and when 15 kHz and 30 kHz SCS is used in FR1 with SRS usage other than antenna switching.

Figure 6.3.3.6-4: Consecutive SRS time mask for the case when power change is required and when 60 kHz SCS is used in FR1, when the transient period is 10 µs

Figure 6.3.3.6-5: FR1 Time mask for 15 kHz and 30 kHz SCS for the case when consecutive SRS switching usage is between antenna switching & other sets

where "other sets" belongs to a "usage set" other than the set for antenna switching. The usage sets for SRS switching are defined in clause 6.2.1 of TS 38.214 [10].

NOTE:Guard period of one symbol is defined between two SRS resources of an SRS resource set for antenna switching for 15kHz, 30kHz and 60kHz SCS in Table 6.2.1.2-1 of TS 38.214 [10].

The above transient period applies to all the transmit CCs in CA with the CC sounding SRS. UE RF requirements do not apply during this transient period.

## 6.3.3.7PUSCH-PUCCH and PUSCH-SRS time masks

The PUCCH/PUSCH/SRS time mask defines the observation period between sounding reference symbol (SRS) and an adjacent PUSCH/PUCCH symbol and subsequent UL transmissions. The time masks apply for all types of frame structures and their allowed PUCCH/PUSCH/SRS transmissions unless otherwise stated.

Figure 6.3.3.7-1: PUCCH/PUSCH/SRS time mask when there is a transmission before or after or both before and after SRS, when sounded on the same antenna (Ant 'x')

Figure 6.3.3.7-2: PUCCH/PUSCH/SRS time mask when there is a transmission before or after or both before and after SRS, when sounded on a different antenna (Ant 'x' and Ant 'y' are different antenna ports)

Figure 6.3.3.7-3: Consecutive long subslot transmission and long subslot transmission time mask

This transient period of 15 µsec applies before and after SRS transmission to all the transmit CCs in CA with the CC sounding SRS. UE RF requirements do not apply during this transient period.

When there is no transmission preceding SRS transmission or succeeding SRS transmission, then the same time mask applies as shown in Figure 6.3.3.7-1.

## 6.3.3.8Transmit power time mask for consecutive slot or long subslot transmission and short subslot transmission boundaries

The transmit power time mask for consecutive slot or long subslot transmission and short slot transmission boundaries defines the transient periods allowed between such transmissions.

Figure 6.3.3.8-1: Consecutive slot or long subslot transmission andshort subslot transmission time mask

## 6.3.3.9Transmit power time mask for consecutive short subslot transmissions boundaries

The transmit power time mask for consecutive short subslot transmission boundaries defines the transient periods allowed between short subslot transmissions.

The transient period shall be equally shared as shown on Figure 6.3.3.9-2.

Figure 6.3.3.9-1: Void

Figure 6.3.3.9-2: Consecutive short subslot transmissions time mask

Figure 6.3.3.9-3: Consecutive short subslot (1 symbol gap) time mask for the case when transient period is required on both sides of the symbol and when 60 kHz SCS is used in FR1, where the transient period is 10 µs

## 6.3.4Power control

## 6.3.4.1General

The requirements on power control accuracy apply under normal conditions.

## 6.3.4.2Absolute power tolerance

The absolute power tolerance is the ability of the UE transmitter to set its initial output power to a specific value for the first sub-frame (1 ms) at the start of a contiguous transmission or non-contiguous transmission with a transmission gap larger than 20 ms. The tolerance includes the channel estimation error.

The minimum requirement specified in Table 6.3.4.2-1 apply in the power range bounded by the minimum output power as specified in clause 6.3.1 and the maximum output power as specified in clause 6.2.1.

Table 6.3.4.2-1: Absolute power tolerance

## 6.3.4.3Relative power tolerance

The relative power tolerance is the ability of the UE transmitter to set its output power in a target sub-frame (1 ms) relatively to the power of the most recently transmitted reference sub-frame (1 ms) if the transmission gap between these sub-frames is less than or equal to 20 ms.

The minimum requirements specified in Table 6.3.4.3-1 apply when the power of the target and reference sub-frames are within the power range bounded by the minimum output power as defined in clause 6.3.1 and the measured PUMAX as defined in clause 6.2.4.

To account for RF Power amplifier mode changes, 2 exceptions are allowed for each of two test patterns. The test patterns are a monotonically increasing power sweep and a monotonically decreasing power sweep over a range bounded by the requirements of minimum power and maximum power specified in clauses 6.3.1 and 6.2.1, respectively. For those exceptions, the power tolerance limit is a maximum of ± 6.0 dB in Table 6.3.4.3-1.

Table 6.3.4.3-1: Relative power tolerance

## 6.3.4.4Aggregate power tolerance

The aggregate power control tolerance is the ability of the UE transmitter to maintain its power in a sub-frame (1 ms) during non-contiguous transmissions within 21 ms in response to 0 dB commands with respect to the first UE transmission and all other power control parameters as specified in TS 38.213 [8] kept constant.

The minimum requirement specified in Table 6.3.4.4-1 apply in the power range bounded by the minimum output power as specified in clause 6.3.1 and the maximum output power as specified in clause 6.2.1.

Table 6.3.4.4-1: Aggregate power tolerance

## 6.3AOutput power dynamics for CA

## 6.3A.1Minimum output power for CA

## 6.3A.1.1Minimum output power for intra-band contiguous CA

For intra-band contiguous carrier aggregation, the minimum output power is defined per carrier and the requirement is specified in clause 6.3.1.

## 6.3A.1.2Minimum output power for intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation, the minimum output power is defined per carrier and the requirement is specified in clause 6.3.1.

## 6.3A.1.3Minimum output power for inter-band CA

For inter-band carrier aggregation with one uplink carrier assigned to one NR band, the minimum output power requirements in clause 6.3.1 apply.

For inter-band carrier aggregation with two uplink contiguous carrier assigned to one NR band, the minimum output power requirements in subclause 6.3A.1.1apply for those carriers. For inter-band carrier aggregation with uplink assigned to two NR bands, the minimum output power is defined per carrier and the requirement is specified in clause 6.3.1.

For inter-band carrier aggregation with two uplink non-contiguous carrier assigned to one NR band, the minimum output power requirements in subclause 6.3A.1.2 apply for those carriers.

For inter-band carrier aggregation with uplink assigned to two NR bands, the minimum output power is defined per carrier and the requirement is specified in clause 6.3.1.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per operating band), the minimum output power requirements specified in subclause 6.3.1 apply for the NR band supporting one component carrier, and for the NR band supporting two contiguous component carriers the requirements specified in subclause 6.3A.1.1 apply.

## 6.3A.1.4Void

## 6.3A.2Transmit OFF power for CA

## 6.3A.2.1Transmit OFF power for intra-band contiguous CA

For intra-band contiguous carrier aggregation, the transmit OFF power specified in clause 6.3.2 is applicable for each component carrier when the transmitter is OFF on all component carriers. The transmitter is considered to be OFF when the UE is not allowed to transmit on any of its ports.

## 6.3A.2.2Transmit OFF power for intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation, the transmit OFF power specified in clause 6.3.2 is applicable for each component carrier when the transmitter is OFF on all component carriers. The transmitter is considered to be OFF when the UE is not allowed to transmit on any of its ports.

## 6.3A.2.3Transmit OFF power for inter-band CA

For inter-band carrier aggregation with one uplink carrier assigned to one NR band, the transmit OFF power requirements in subclause 6.3.2 apply.

For inter-band carrier aggregation with two contiguous carriers assigned to one NR band, the transmit OFF power requirements in subclause 6.3A.2.1 apply for those carriers.

For inter-band carrier aggregation with two uplink non-contiguous carrier assigned to one NR band, the transmit OFF power requirements in subclause 6.3A.2.2 apply for those carriers.

For inter-band carrier aggregation with uplink assigned to two NR bands, the transmit OFF power specified in clause 6.3.2 is applicable for each component carrier when the transmitter is OFF on all component carriers. The transmitter is considered to be OFF when the UE is not allowed to transmit on any of its ports.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per operating band), the transmit OFF power requirements specified in subclause 6.3.2 apply for the NR band supporting one component carrier, and for the NR band supporting two contiguous component carriers the requirements specified in subclause 6.3A.2.1 apply.

## 6.3A.2.4Void

## 6.3A.3Transmit ON/OFF time mask for CA

## 6.3A.3.1Transmit ON/OFF time mask for intra-band contiguous CA

For intra-band contiguous carrier aggregation, the general output power ON/OFF time mask specified in clause 6.3.3.1 is applicable for each component carrier during the ON power period and the transient periods. The OFF period as specified in clause 6.3.3.1 shall only be applicable for each component carrier when all the component carriers are OFF.

## 6.3A.3.2Transmit ON/OFF time mask for intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation, the general output power ON/OFF time mask specified in clause 6.3.3.1 is applicable for each component carrier during the ON power period and the transient periods. The OFF period as specified in clause 6.3.3.1 shall only be applicable for each component carrier when all the component carriers are OFF.

## 6.3A.3.3Transmit ON/OFF time mask for inter-band CA

## 6.3A.3.3.1General

For inter-band carrier aggregation with one uplink carrier assigned to one NR band, the transmit ON/OFF time mask requirements in subclause 6.3.3 apply.

For inter-band carrier aggregation with two contiguous carriers assigned to one NR band, the transmit ON/OFF time mask requirements in subclause 6.3A.3.1 apply for those carriers.

For inter-band carrier aggregation with two uplink non-contiguous carrier assigned to one NR band, the transmit ON/OFF time mask requirements in subclause 6.3A.3.2 apply for those carriers.

For inter-band carrier aggregation with uplink assigned to two NR bands, the general output power ON/OFF time mask specified in clause 6.3.3.1 is applicable for each component carrier during the ON power period and the transient periods. The OFF period as specified in clause 6.3.3.1 shall only be applicable for each component carrier when all the component carriers are OFF.

For inter-band carrier aggregation with uplink assigned to two NR bands with maximum two transmit antenna connectors for each band for UEs with with three transmit antenna connectors, the transmit ON/OFF time mask requirements in subclause 6.3A.3.3.8 apply for those bands.

Time masks for Tx switching due to switching period are defined in clauses 6.3A.3.3.2-6.3A.3.3.5 and 6.3A.3.3.8 for both single TAG and dual-TAG scenarios. When a UE is configured with dual-TAG with at least two cells corresponding to two TAGs involved in one switching event, the timing advance difference should be considered in the time masks in sub-clauses 6.3A.3.3.2-6.3A.3.3.5 and 6.3A.3.3.8 for two uplink carriers or two uplink bands and in sub-clause 6.3A.3.3.6 for 3-4 uplink bands. The UE may omit uplink transmission on OFDM symbols that partially or fully overlap with the configured switching period for any timing advance difference.

When the location of the switching period by uplinkTxSwitchingPeriodLocation is ignored by the UE, the length and location of allowed transient periods for dual TAG are as specified in 6.3A.3.3.2 – 6.3A.3.3.5 and in 6.3A.3.3.6 for a switching band pair with the UE scheduled or configured with uplink transmissions that do not result in

-simultaneous transmission on two antenna ports on one uplink carrier on one band, and any transmission on another uplink carrier on another band

-transmission of any of the carriers for a duration of at least the uplink switching gap indicated by UE capability

When the location of the switching period by uplinkTxSwitchingPeriodLocation is ignored by the UE, the length and location of allowed transient periods for dual TAG are as specified in 6.3A.3.3.8 for a switching band pair with the UE scheduled or configured with uplink transmissions that do not result in

-transmission of any of the carriers for a duration of at least the uplink switching gap indicated by UE capability

for any timing difference between uplink carriers in different bands up to the MTTD specified for UL CA in clause 7.5.4 of [7] in case of dual TAG

Carriers within the same band belong to the same TAG in all cases.

For low NR band inter-band carrier aggregation via switching featureSetCombinationLowBandSwitching-r19, the general output power ON/OFF time mask specified in clause 6.3A.3.3.7 is applicable.

## 6.3A.3.3.2Time mask for switching between two uplink carriers

In addition to the requirements in 6.3A.3.3.1 and the maximum output power requirement specified in Table 6.2A.1.3-1 with uplink assigned to two NR bands, the switching time mask specified in this clause is applicable for an uplink band pair of a inter-band UL CA configuration when the capability uplinkTxSwitchingPeriod-r16 is supported. The requirement is only applicable for uplink switching mechanisms specified in clause 6.1.6 of TS 38.214 [10], where NR UL carrier 1 is capable of one transmit antenna connector and NR UL carrier 2 is capable of one or two transmit antenna connectors. 3dB boosting on the maximum output power for CA power class 3 on NR UL carrier 2 may be applied depending on the support of the capability uplinkTxSwitching-PowerBoosting-r16 and the IE uplinkTxSwitchingPowerBoosting-r16 being enabled.

For UE supporting 1Tx-2Tx switching, the UE shall support the switch between single layer transmission with one antenna port and two-layer transmission with two antenna ports on the two uplink carriers following the scheduling commands and rank adaptation, i.e., both single layer and two-layer transmission with 2 antenna ports, and single layer transmission with 1 antenna port shall be supported on NR UL carrier 2.

For UE supporting 1Tx-1Tx switching, the UE shall support the switch of single layer transmission with one antenna port on each carrier.

The switching periods described in Figure 6.3A.3.3.2-1a and Figure 6.3A.3.3.2-1b are located in either NR carrier 1 or carrier 2 as indicated in RRC signalling uplinkTxSwitchingPeriodLocation [7], and the length of uplink switching period X is less than the value indicated by UE capability uplinkTxSwitchingPeriod.

When switching from one carrier to another, if there is no uplink transmission scheduled or configured on the switch-from carrier for at least the duration of the switching period (X µs) before the point in time the UE is scheduled or configured to start the transmission on the switch-to carrier, the switching period is fully contained in the time period between the end of the transmission on the switch-from carrier and the start of the transmission on the switch-to carrier. In addition, the RRC signalling uplinkTxSwitchingPeriodLocation is ignored by the UE and does not take effect in this case.

Figure 6.3A.3.3.2-1a: Time mask for switching between UL carrier 1 and UL Carrier 2,where the switching period is located in carrier 1

Figure 6.3A.3.3.2-1b: Time mask for switching between UL carrier 1 and UL Carrier 2, where the switching period is located in carrier 2

The following applies for the uplink switching cases specified in clause 6.1.6.2 of [10] with uplinkTxSwitchingOption set to either switchedUL or dualUL when the configuration of the location of the switching period by uplinkTxSwitchingPeriodLocation is ignored by the UE:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the uplink switching gap indicated by uplinkTxSwitchingPeriod on any of the carriers before T0, transient periods of 10 ms are located at the end of the last symbol(s) configured or scheduled on the carriers before T0 and at the start of the first symbol(s) configured or scheduled at T0 on the switched-to carrier.

The requirements apply for the case of both non-co-located and co-located and synchronized network deployment for the two uplink carriers.

The time mask is applicable to uplink transmissions when configured with switchedUL or dualUL.

## 6.3A.3.3.3Time mask for switching between two uplink carriers with two transmit antenna connectors

In addition to the requirements in 6.3A.3.3.1 and the maximum output power requirement specified in Table 6.2A.1.3-1 with uplink assigned to two NR bands, the switching time mask specified in this clause is applicable for an uplink band pair of a inter-band UL CA configuration when the capability uplinkTxSwitchingPeriod2T2T is present, and is only applicable for uplink switching mechanisms specified in clause 6.1.6 of TS 38.214 [10], where NR UL carrier 1 is capable of two transmit antenna connectors and NR UL carrier 2 is capable of two transmit antenna connectors, and the two uplink carriers are in different bands with different carrier frequencies. The UE shall support the switch between two-layer transmission with two antenna ports and two-layer transmission with two antenna ports on the two uplink carriers following the scheduling commands and rank adaptation, i.e., both single layer and two-layer transmission with 2 antenna ports, and single layer transmission with 1 antenna port shall be supported on NR UL carrier 1 and carrier 2.

The switching periods described in Figure 6.3A.3.3.3-1a and Figure 6.3A.3.3.3-1b are located in either NR carrier 1 or carrier 2 as indicated in RRC signalling uplinkTxSwitchingPeriodLocation [7], and the length of uplink switching period X is less than the value indicated by UE capability uplinkTxSwitchingPeriod2T2T.

When switching from one carrier to another, if there is no uplink transmission scheduled or configured on the switch-from carrier for at least the duration of the switching period (X µs) before the point in time the UE is scheduled or configured to start the transmission on the switch-to carrier, the switching period is fully contained in the time period between the end of the transmission on the switch-from carrier and the start of the transmission on the switch-to carrier. In addition, the RRC signalling uplinkTxSwitchingPeriodLocation is ignored by the UE and does not take effect in this case.

Figure 6.3A.3.3.3-1a: Time mask for switching between UL carrier 1 and UL Carrier 2, where the switching period is located in carrier 1

Figure 6.3A.3.3.3-1b: Time mask for switching between UL carrier 1 and UL Carrier 2, where the switching period is located in carrier 2

The following applies for the uplink switching cases specified in clause 6.1.6.2 of [10] with uplinkTxSwitchingOption set to either switchedUL or dualUL when the configuration of the location of the switching period by uplinkTxSwitchingPeriodLocation is ignored by the UE:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the uplink switching gap indicated by uplinkTxSwitchingPeriod2T2T on any of the carriers before T0, transient periods of 10 ms are located at the end of the last symbol(s) configured or scheduled on the carriers before T0 and at the start of the first symbol(s) configured or scheduled at T0 on the switched-to carrier.

The requirements apply for the case of both non-co-located and co-located and synchronized network deployment for the two uplink carriers.

The time mask is applicable to uplink transmissions when configured with switchedUL or dualUL.

## 6.3A.3.3.4Time mask for switching between one uplink band with one transmit antenna connector and one uplink band with two transmit antenna connectors

In addition to the requirements in 6.3A.3.3.1 and the maximum output power requirement specified in Table 6.2A.1.3-1 with uplink assigned to two NR bands, the switching time mask specified in this clause is applicable for an uplink band pair of a inter-band UL CA configuration when the capability uplinkTxSwitchingPeriod is present, and is only applicable for uplink switching mechanisms specified in clause 6.1.6 of TS 38.214 [10], where NR UL carrier 1 in band A is capable of one transmit antenna connector, NR UL carrier 2 and carrier 3 in band B are capable of two transmit antenna connectors. NR UL carrier 2 and carrier 3 are two contiguous aggregated carriers, and band A and band B are different bands with different carrier frequencies. The UE shall support the switch between single layer transmission with one antenna port and two-layer transmission with two antenna ports on the two uplink bands following the scheduling commands and rank adaptation, i.e., both single layer and two-layer transmission with 2 antenna ports, and single layer transmission with 1 antenna port shall be supported on NR UL carrier 2 and carrier 3 in band B.

The switching periods described in Figure 6.3A.3.3.4-1a and Figure 6.3A.3.3.4-1b are located in either NR band A or band B as indicated in RRC signalling uplinkTxSwitchingPeriodLocation [7], and the length of uplink switching period X is less than the value indicated by UE capability uplinkTxSwitchingPeriod .

When switching from one carrier to another, if there is no uplink transmission scheduled or configured on the switch-from carrier for at least the duration of the switching period (X µs) before the point in time the UE is scheduled or configured to start the transmission on the switch-to carrier, the switching period is fully contained in the time period between the end of the transmission on the switch-from carrier and the start of the transmission on the switch-to carrier. In addition, the RRC signalling uplinkTxSwitchingPeriodLocation is ignored by the UE and does not take effect in this case.

Figure 6.3A.3.3.4-1a: Time mask for switching between one carrier in band A and two contiguous carriers in band B, where the switching period is located in band A

Figure 6.3A.3.3.4-1b: Time mask for switching between one carrier in band A and two contiguous carriers in band B, where the switching period is located in band B

The following applies for the uplink switching cases specified in clause 6.1.6.2 of [10] with uplinkTxSwitchingOption set to either switchedUL or dualUL when the configuration of the location of the switching period by uplinkTxSwitchingPeriodLocation is ignored by the UE:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the uplink switching gap indicated by uplinkTxSwitchingPeriod on any of the carriers before T0, transient periods of 10 ms are located at the end of the last symbol(s) configured or scheduled on the carriers before T0 and at the start of the first symbol(s) configured or scheduled at T0 on the switched-to carrier.

The requirements apply for the case of both non-co-located and co-located and synchronized network deployment for the three uplink carriers.

The time mask is applicable to uplink transmissions when configured with switchedUL or dualUL.

## 6.3A.3.3.5Time mask for switching between two uplink bands with two transmit antenna connectors

In addition to the requirements in 6.3A.3.3.1 and the maximum output power requirement specified in Table 6.2A.1.3-1 with uplink assigned to two NR bands, the switching time mask specified in this clause is applicable for an uplink band pair of a inter-band UL CA configuration when the capability uplinkTxSwitchingPeriod2T2T is present, and is only applicable for uplink switching mechanisms specified in clause 6.1.6 of TS 38.214 [10], where NR UL carriers in band A and B are capable of two transmit antenna connectors. NR UL carriers are two contiguous aggregated carriers in band B, and one or two contiguous aggregated carriers in band A. Band A and band B are different bands with different carrier frequencies. The UE shall support the switch between two-layer transmission with two antenna ports and two-layer transmission with two antenna ports on the two uplink bands following the scheduling commands and rank adaptation, i.e., both single layer and two-layer transmission with 2 antenna ports, and single layer transmission with 1 antenna port shall be supported on NR UL carriers in the two bands.

The switching periods described in Figure 6.3A.3.3.5-1a and Figure 6.3A.3.3.5-1b are located in either NR band A or band B as indicated in RRC signalling uplinkTxSwitchingPeriodLocation [7], and the length of uplink switching period X is less than the value indicated by UE capability uplinkTxSwitchingPeriod2T2T.

When switching from one carrier to another, if there is no uplink transmission scheduled or configured on the switch-from carrier for at least the duration of the switching period (X µs) before the point in time the UE is scheduled or configured to start the transmission on the switch-to carrier, the switching period is fully contained in the time period between the end of the transmission on the switch-from carrier and the start of the transmission on the switch-to carrier. In addition, the RRC signalling uplinkTxSwitchingPeriodLocation is ignored by the UE and does not take effect in this case.

Figure 6.3A.3.3.5-1a: Time mask for switching between band A and band B, where the switching period is located in band A

Figure 6.3A.3.3.5-1b: Time mask for switching between band A and band B, where the switching period is located in band B

The following applies for the uplink switching cases specified in clause 6.1.6.2 of [10] with uplinkTxSwitchingOption set to either switchedUL or dualUL when the configuration of the location of the switching period by uplinkTxSwitchingPeriodLocation is ignored by the UE:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the uplink switching gap indicated by uplinkTxSwitchingPeriod2T2T on any of the carriers before T0, transient periods of 10 ms are located at the end of the last symbol(s) configured or scheduled on the carriers before T0 and at the start of the first symbol(s) configured or scheduled at T0 on the switched-to carrier.

The requirements apply for the case of both non-co-located and co-located and synchronized network deployment for the three uplink carriers.

The time mask is applicable to uplink transmissions when configured with switchedUL or dualUL.

## 6.3A.3.3.6Time mask for switching across up to four uplink bands

The switching time mask requirements specified in this sub-clause are applicable for an NR inter-band CA configuration when the capability supportedBandPairListNR-r18 is present, and are only applicable for uplink switching mechanisms specified in clause [6.1.6] of TS 38.214 [10].

In the NR inter-band CA configuration, the number of NR uplink bands is up to four. NR UL carrier(s) in each of the up to four uplink bands are capable of one or two transmit antenna connector(s), according to the UE capability FeatureSetUplinkPerCC.

The switching time masks in Figure 6.3A.3.3.6-1 and Figure 6.3A.3.3.6-2 are applicable to each of the uplink band pairs in the CA configuration, and are applicable to uplink transmissions when configured with switchedUL or dualUL by the parameter switchingOptionConfigForBandPair-r18. To simplify the figures, the two bands in different band pairs are denoted as NR band X and band Y. The uplink transmission on either band X or band Y is with one or two transmit antenna connector(s),

–if NR UL carriers in both bands in one band pair are capable of one transmit antenna connector, 1Tx-1Tx switching is supported for the band pair;

–if NR UL carrier(s) in one band of one band pair is capable of one transmit antenna connector, and NR UL carrier(s) in the other band of the band pair is capable of two transmit antenna connectors, 1Tx-2Tx switching is supported for the band pair;

–if NR UL carriers in both bands of one band pair are capable of two transmit antenna connectors, 2Tx-2Tx switching is supported for the band pair.

For each band pair, the switching periods described in Figure 6.3A.3.3.6-1 and Figure 6.3A.3.3.6-2 are located in either NR band X or band Y as indicated in RRC signalling uplinkTxSwitchingBandList [7]. For each band pair, the length of uplink switching period X is indicated by RRC signalling switchingPeriodConfigForBandPair. UE shall be capable to transmit until the beginning of the switching period and after the end of switching period with the exception of transient periods.

Figure 6.3A.3.3.6-1: Time mask for switching between band X and band Y, where the switching period is located in band X

Figure 6.3A.3.3.6-2: Time mask for switching between band X and band Y, where the switching period is located in band Y

The following applies for the uplink switching cases specified in Figure 6.3A.3.3.6-1 and 6.3A.3.3.6-2 in a band pair with switchingOptionConfigForBandPair-r18 set to either switchedUL or dualUL:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the length of uplink switching period of X µs indicated by RRC signalling switchingPeriodConfigForBandPairon any of the carriers band X and band Y before T0,

-the configuration of the location of the switching period by uplinkTxSwitchingBandList is ignored by the UE;

-transient periods of 10 s are located at the end of the last symbol(s) configured or scheduled on the carrier(s) before T0 and at the start of the first symbol(s) configured or scheduled at T0 on the switch-to carrier(s).

In addition to the requirements in Figure 6.3A.3.3.6-1 and Figure 6.3A.3.3.6-2, the requirements in Figure 6.3A.3.3.6-3 to 6.3A.3.3.6-5 are applicable when dualUL are supported on certain band pair(s) in the CA configuration.

The switching time masks in Figure 6.3A.3.3.6-3 and Figure 6.3A.3.3.6-4 are applicable when dualUL is supported for at least two uplink band pairs in the CA configuration. The two band pairs supporting dualUL are denoted as band pairs of {band X and band Z} and {band Y and band Z}. When one transmitter is switched between band X and band Y,

–As baseline UE behaviour, the UE is not required to transmit on any of the three bands during time period T1 located on band X and band Z, where T1 is the length of switching period for the band pair of band X and band Y, as shown in Figure 6.3A.3.3.6-4.

–As optional UE behaviours, when the UE indicates band Z in the capability bandIndexUnaffected,

–if the UE indicates maintainedUL-Trans for band pair of {band X and band Y}, UE shall be capable of uplink transmission on band Z during the switching period that is located on band X, and UE is not required to transmit on band X and Y during time period T1 located on band X, where T1 is the length of switching period for the band pair of band X and band Y, as shown in Figure 6.3A.3.3.6-3;

–otherwise, the UE is not required to transmit on any of the three bands during the switching period indicated by UE capability periodOnULBands located on band X and band Z, as shown in Figure 6.3A.3.3.6-4.

In Figure 6.3A.3.3.6-3 and Figure 6.3A.3.3.6-4, the uplink transmission on band X, band Y and band Z are all with one transmit antenna connector and one antenna port.

Figure 6.3A.3.3.6-3: Time mask for one transmitter switching between band X and band Y, and UE is capable of uplink transmission on band Z during the switching period

The following applies for the uplink switching cases specified in Figure 6.3A.3.3.6-3 in a band pair with switchingOptionConfigForBandPair-r18 set to dualUL:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the length of uplink switching period X indicated by RRC signalling switchingPeriodConfigForBandPair on any of the carriers in band X and band Y before T0,

-the configuration of the location of the switching period by uplinkTxSwitchingBandList is ignored by the UE;

-transient periods of 10 s are located at the end of the last symbol(s) configured or scheduled on the carrier(s) before T0 and at the start of the first symbol(s) configured or scheduled at T0 on the switch-to carrier(s).

Figure 6.3A.3.3.6-4: Time mask for one transmitter switching between band X and band Y, and UE is not capable of uplink transmission on band Z during the switching period

The switching time mask in Figure 6.3A.3.3.6-5 is applicable when dualUL is supported for at least one uplink band pair including band X and band Y, and two transmit antenna connectors are supported on at least one uplink band of band Z. When one transmitter is switched between band X and band Z, and across the same time, the other transmitter is switched between Y and band Z, the switching time mask in Figure 6.3A.3.3.6-5 is applicable.

–As baseline UE behaviour, UE is not required to transmit on any of the three bands during time period with the larger one of swithching period T2 and T3, where T2 is the length of switching period for the band pair of band X and band Z, and T3 is the length of switching period for the band pair of band Y and band Z.

–As optional UE behaviour, when UE additionally reports band pair of {band X and band Y} and band Z in the capability uplinkTxSwitchingAdditionalPeriodDualUL-List , UE is not required to transmit on any of the three bands during time period indicated by UE capability switchingAdditionalPeriodDualUL.

In Figure 6.3A.3.3.6-5, the uplink transmission on band X and band Y is with one transmit antenna connector and one antenna port, and the uplink transmission on band Z is with two transmit antenna connectors and two antenna ports. The switching period location is configured according to [7], and band Z is with the highest priority according to the RRC configuration uplinkTxSwitchingBandList.

Figure 6.3A.3.3.6-5: Time mask for one transmitter switching between band X and band Z, and one transmitter switching between band Y and band Z

The following applies for the uplink switching case specified in Figure 6.3A.3.3.6-5 and with uplinkTxSwitchingOptionForBandPair-r18 set to dualUL for at least one band pair

-if uplink switching on a band pair is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the maximum of the lengths of uplink switching periods indicated by RRC signalling switchingPeriodConfigForBandPair on any of the carriers in band X, band Y and band Z before T0 on any switched-to carrier

-the configuration of the location of the switching period and the priority of bands in the uplinkTxSwitchingBandList are ignored by the UE

-transient periods of 10 ms are located at the end of the last symbol(s) configured or scheduled on the switched-from carrier(s) before T0 on any switched-to carrier and at the start of the first symbol(s) configured or scheduled at T0 on the switch-to carrier(s)

The requirements in this sub-clause apply for the case of synchronized network deployment for the uplink bands.

## 6.3A.3.3.6aAdditional requirements for three-band switching with dual TAG

The following applies for the uplink switching case specified in Figure 6.3A.3.3.6-5 with three bands involved in the switching and with uplinkTxSwitchingOptionForBandPair-r18 set to dualUL for at least one band pair.

If the UE is configured with dual TAG and not configured or scheduled with uplink transmissions for a duration of at least the maximum of the lengths of uplink switching periods indicated by   RRC signalling switchingPeriodConfigForBandPair on any of the carriers in band X, band Y and band Z including any timing difference between the uplink carriers before the first T0 on any switched-to carrier,

-the configuration of the location of the switching period and the priority of bands in the uplinkTxSwitchingBandList are ignored by the UE

-transient periods of 10 s are located at the end of the last symbol(s) configured or scheduled on the switched-from carrier(s) before the first T0 on any switched-to carrier and at the start of the first symbol(s) configured or scheduled at T0 on the switch-to carrier(s)

## 6.3A.3.3.7Time mask for low NR band carrier aggregation via switching

For low NR band inter-band carrier aggregation supported via switching featureSetCombinationLowBandSwitching-r19, the time mask for UL transmissions in slots configured with switching gaps via RRC is specified in Figure 6.3A.3.3.7-1.

Figure 6.3A.3.3.7-1: ON/OFF time mask for NR UL transmission for DL CA via switching with non-CA in the UL

In the figure above, the switching period is shown for information only and may not necessarily be adjacent to the transient period.

In the case of SDL to FDD transition:

-The switching period is located inside the switching gap, as configured by gapDurationSCelltoPCell-r19

-The switching period is not overlapping with the UL transient period

In the case of FDD to SDL transition:

-The switching period is located inside the switching gap, as configured by gapDurationPCelltoSCell-r19

-The switching period is after the UL transient period

## 6.3A.3.3.8Time mask for switching between two uplink bands with three transmit antenna connectors and maximum two transmit antenna connectors for each band

In addition to the requirements in 6.3A.3.3.1 and the maximum output power requirement specified in Table 6.2H.3.1-1 with uplink configured to two NR bands, the switching time mask specified in this clause is applicable for an uplink band pair of an inter-band UL CA configuration when the capability Uplink3TxSwitchingPeriodUpTo2TPerBandDualUL is present, and is only applicable for uplink switching mechanisms specified in clause 6.1.6 of TS 38.214 [10], where NR UL carriers in bands A and B are capable of a maximum of two transmit antenna connectors, but simultaneously only a maximum of three transmit antenna connectors are supported across both bands. Band A and band B are different bands with different carrier frequencies. The UE shall support the switch between the following two transmit configurations 1 and 2:

Configuration 1: Two antenna ports on band A and one antenna port on band B

Configuration 2: One antenna port on band A and two antenna ports on band B

In the above configurations 1 and 2, the UE shall follow the scheduling commands and rank adaptation, i.e., both single layer and two-layer transmission with 2 antenna ports and single layer transmission with 1 antenna port shall be supported on NR UL carriers of band A and band B.

The switching periods described in Figure 6.3A.3.3.8-1a and Figure 6.3A.3.3.8-1b are located in either band A or band B as indicated in RRC signalling uplinkTxSwitchingPeriodLocation [7], and the length of uplink switching period X is less than the value indicated by UE capability Uplink3TxSwitchingPeriodUpTo2TPerBandDualUL.

When switching from one configuration to another, if there is no uplink transmission scheduled or configured on the switch-from carrier for at least the duration of the switching period (X µs) before the point in time the UE is scheduled or configured to start the transmission on the switch-to carrier, the switching period is fully contained in the time period between the end of the transmission on the switch-from carrier and the start of the transmission on the switch-to carrier. In addition, the RRC signalling uplinkTxSwitchingPeriodLocation is ignored by the UE and does not take effect in this case.

Figure 6.3A.3.3.8-1a: Time mask for switching between UL Configuration 1 and UL Configuration 2, where the switching period is located in Configuration 1

Figure 6.3A.3.3.8-1b: Time mask for switching between UL Configuration 1 and UL Configuration 2, where the switching period is located in Configuration 2

The following applies for the uplink switching cases specified in clause 6.1.6.2 of [10] with uplinkTxSwitchingOption set to dualUL when the configuration of the location of the switching period by uplinkTxSwitchingPeriodLocation is ignored by the UE:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the uplink switching gap indicated by Uplink3TxSwitchingPeriodUpTo2TPerBandDualUL on any of the carriers before T0, transient periods of 10 ms are located at the end of the last symbol(s) configured or scheduled on the carriers before T0 and at the start of the first symbol(s) configured or scheduled at T0 on the switched-to carrier.

The requirements apply for the case of both non-co-located and co-located and synchronized network deployment for the two uplink carriers.

The time mask is applicable to uplink transmissions when configured with dualUL.

## 6.3A.3.4Void

## 6.3A.4Power control for CA

## 6.3A.4.1Power control for intra-band contiguous CA

## 6.3A.4.1.1Absolute power tolerance

The absolute power tolerance is the ability of the UE transmitter to set its initial output power to a specific value for the first sub-frame at the start of a contiguous transmission or non-contiguous transmission with a transmission gap on each active component carriers larger than 20ms. The requirement can be tested by time aligning any transmission gaps on the component carriers.

6.3A.4.1.1.1Minimum requirements

For intra-band contiguous carrier aggregation the absolute power control tolerance per component carrier is given in Table 6.3.4.2-1.

## 6.3A.4.1.2Relative power tolerance

6.3A.4.1.2.1Minimum requirements

For intra-band contiguous carrier aggregation, the requirements apply when the power of the target and reference sub-frames on each component carrier exceed the minimum output power as defined in clause 6.3A.1 and the total power is limited by PUMAX as defined in clause 6.2A.4. The UE shall meet the following requirements for transmission on both assigned component carriers when the average transmit power per PRB is aligned across both assigned carriers in the reference sub-frame:

a)for all possible combinations of PUSCH and PUCCH transitions per component carrier, the corresponding requirements given in Table 6.3.4.3-1;

b)for SRS transitions on each component carrier, the requirements for combinations of PUSCH/PUCCH and SRS transitions given in Table 6.3.4.2-1 with simultaneous SRS of constant SRS bandwidth allocated in the target and reference subrames;

c)for RACH on the primary component carrier, the requirements given in Table 6.3.4.3-1 for PRACH.

For a) and b) above, the power step P between the reference and target subframes shall be set by a TPC command and/or an uplink scheduling grant transmitted by means of an appropriate DCI Format.

## 6.3A.4.1.3Aggregate power control tolerance

For intra-band contiguous carrier aggregation, the aggregate power tolerance per component carrier is given in Table 6.3.4.4-1. The average power per PRB shall be aligned across both assigned carriers before the start of the test. The requirement can be tested with the transmission gaps time aligned between component carriers.

## 6.3A.4.2Power control for intra-band non-contiguous CA

## 6.3A.4.2.1Absolute power tolerance

The absolute power tolerance is the ability of the UE transmitter to set its initial output power to a specific value for the first sub-frame at the start of a contiguous transmission or non-contiguous transmission with a transmission gap on each active component carriers larger than 20ms. The requirement can be tested by time aligning any transmission gaps on the component carriers.

## 6.3A.4.2.1.1Minimum requirements

For intra-band non-contiguous carrier aggregation the absolute power control tolerance per component carrier is given in Table 6.3.4.2-1.

## 6.3A.4.2.2Relative power tolerance

## 6.3A.4.2.2.1Minimum requirements

For intra-band non-contiguous carrier aggregation, the requirements apply when the power of the target and reference sub-frames on each component carrier exceed the minimum output power as defined in subclause 6.3A.1 and the total power is limited by PUMAX as defined in subclause 6.2A.4. The UE shall meet the following requirements for transmission on both assigned component carriers when the average transmit power per PRB is aligned across both assigned carriers in the reference sub-frame:

a)for all possible combinations of PUSCH and PUCCH transitions per component carrier, the corresponding requirements given in Table 6.3.4.3-1;

b)for SRS transitions on each component carrier, the requirements for combinations of PUSCH/PUCCH and SRS transitions given in Table 6.3.4.3-1 with simultaneous SRS of constant SRS bandwidth allocated in the target and reference subrames;

c)for RACH on the primary component carrier, the requirements given in Table 6.3.4.3-1for PRACH.

For a) and b) above, the power step P between the reference and target subframes shall be set by a TPC command and/or an uplink scheduling grant transmitted by means of an appropriate DCI Format.

## 6.3A.4.2.3Aggregate power control tolerance

For intra-band non-contiguous carrier aggregation, the aggregate power tolerance per component carrier is given in Table 6.3.4.4-1. The average power per PRB shall be aligned across both assigned carriers before the start of the test. The requirement can be tested with the transmission gaps time aligned between component carriers.

## 6.3A.4.3Power control for inter-band CA

No requirements unique to CA operation are defined.

## 6.3A.4.4Void

## 6.3BOutput power dynamics for NR-DC

For inter-band NR-DC with one uplink carrier assigned per NR band, the output power dynamics for the corresponding inter-band CA configuration as specified in clause 6.3A applies.

## 6.3COutput power dynamics for SUL

## 6.3C.1Void

## 6.3C.2Void

## 6.3C.3Transmit ON/OFF time mask for SUL

## 6.3C.3.0General

Time masks for Tx switching due to switching period are defined in clause 6.3C.3.5 for both single TAG and dual-TAG scenarios. When a UE is configured with dual-TAG with at least two cells corresponding to two TAGs involved in one switching event, the timing advance difference is considered in the time masks in sub-clause 6.3C.3.5. The UE may omit uplink transmissionon OFDM symbols that partially or fully overlap with the configured switching period for any timing advance difference.

## 6.3C.3.1Time mask for switching between two uplink carriers

The switching time mask specified in this clause is applicable for an uplink band pair of a SUL configuration when the capability uplinkTxSwitchingPeriod is present, is only applicable for uplink switching mechanisms specified in clause 6.16 of TS 38.214 [10], where NR SUL carrier 1 is capable of one transmit antenna connector and NR UL carrier 2 is capable of one or two transmit antenna connectors, and the two uplink carriers are in different bands with different carrier frequencies.

For UE supporting 1Tx-2Tx switching, the UE shall support the switch between single layer transmission with one antenna port and two-layer transmission with two antenna ports on the two uplink carriers following the scheduling commands and rank adaptation, i.e., both single layer and two-layer transmission with 2 antenna ports, and single layer transmission with 1 antenna port shall be supported on NR UL carrier 2 as specified in [38.306].

For UE supporting 1Tx-1Tx switching, the UE shall support the switch of single layer transmission with one antenna port on each carrier.

The switching periods described in Figure 6.3C.3.1-1a and Figure 6.3C.3.1-1b are located in either NR carrier 1 or carrier 2 as indicated in RRC signalling uplinkTxSwitchingPeriodLocation [7], and the length of uplink switching period X is less than the value indicated by UE capability uplinkTxSwitchingPeriod.

When switching from one carrier to another, if there is no uplink transmission scheduled or configured on the switch-from carrier for at least the duration of the switching period (X µs) before the point in time the UE is scheduled or configured to start the transmission on the switch-to carrier, the switching period is fully contained in the time period between the end of the transmission on the switch-from carrier and the start of the transmission on the switch-to carrier. In addition, the RRC signalling uplinkTxSwitchingPeriodLocation is ignored by the UE and does not take effect in this case.

Figure 6.3C.3.1-1a: Time mask for switching between SUL carrier 1 and UL Carrier 2, where the switching period is located in carrier 1

Figure 6.3C.3.1-1b: Time mask for switching between SUL carrier 1 and UL Carrier 2, where the switching period is located in carrier 2

The following applies for the uplink switching case specified in clause 6.1.6.3 of [10] when the configuration of the location of the switching period by uplinkTxSwitchingPeriodLocation is ignored by the UE:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the uplink switching gap indicated by uplinkTxSwitchingPeriod on any of the carriers before T0, transient periods of 10 ms are located at the end of the last symbol(s) scheduled on the carriers before T0 and at the start of the first symbol(s) configured or scheduled at T0 on the switched-to carrier.

The requirements apply for the case of co-located and synchronized network deployment for the two uplink carriers.

The requirements apply for the case of single TAG for the two uplink carriers, i.e., the same uplink timing for the two carriers as described in clause 4.2 of TS 38.213 [8].

## 6.3C.3.2Time mask for switching between two uplink carriers with two transmit antenna connectors

The switching time mask specified in this clause is applicable for an uplink band pair of a SUL configuration when the capability uplinkTxSwitchingPeriod2T2T is present, is only applicable for uplink switching mechanisms specified in clause 6.1.6 of TS 38.214 [10], where NR SUL carrier 1 is capable of two transmit antenna connectors and NR UL carrier 2 is capable of two transmit antenna connectors, and the two uplink carriers are in different bands with different carrier frequencies. The UE shall support the switch between two-layer transmission with two antenna ports and two-layer transmission with two antenna ports on the two uplink carriers following the scheduling commands and rank adaptation, i.e., both single layer and two-layer transmission with 2 antenna ports, and single layer transmission with 1 antenna port shall be supported on NR UL carrier 1 and carrier 2.

The switching periods described in Figure 6.3C.3.2-1a and Figure 6.3C.3.2-1b are located in either NR carrier 1 or carrier 2 as indicated in RRC signalling uplinkTxSwitchingPeriodLocation [7], and the length of uplink switching period X is less than the value indicated by UE capability uplinkTxSwitchingPeriod2T2T.

When switching from one carrier to another, if there is no uplink transmission scheduled or configured on the switch-from carrier for at least the duration of the switching period (X µs) before the point in time the UE is scheduled or configured to start the transmission on the switch-to carrier, the switching period is fully contained in the time period between the end of the transmission on the switch-from carrier and the start of the transmission on the switch-to carrier. In addition, the RRC signalling uplinkTxSwitchingPeriodLocation is ignored by the UE and does not take effect in this case.

Figure 6.3C.3.2-1a: Time mask for switching between SUL carrier 1 and UL Carrier 2, where the switching period is located in carrier 1

Figure 6.3C.3.2-1b: Time mask for switching between SUL carrier 1 and UL Carrier 2, where the switching period is located in carrier 2

The following applies for the uplink switching case specified in clause 6.1.6.3 of [10] when the configuration of the location of the switching period by uplinkTxSwitchingPeriodLocation is ignored by the UE:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the uplink switching gap indicated by uplinkTxSwitchingPeriod2T2T on any of the carriers before T0, transient periods of 10 ms are located at the end of the last symbol(s) configured or scheduled on the carriers before T0 and at the start of the first symbol(s) configured or scheduled at T0 on the switched-to carrier.

The requirements apply for the case of co-located and synchronized network deployment for the two uplink carriers.

The requirements apply for the case of single TAG for the two uplink carriers, i.e., the same uplink timing for the two carriers as described in clause 4.2 of TS 38.213 [8].

## 6.3C.3.3Time mask for switching between one uplink band with one transmit antenna connector and one uplink band with two transmit antenna connectors

The switching time mask specified in this clause is applicable for an uplink band pair of a SUL configuration when the capability uplinkTxSwitchingPeriod  is present, is only applicable for uplink switching mechanisms specified in clause 6.1.6 of TS 38.214 [10], where NR SUL carrier 1 in band A is capable of one transmit antenna connector and NR UL carrier 2 and carrier 3 in band B are capable of two transmit antenna connectors. NR UL carrier 2 and carrier 3 are two contiguous aggregated carriers, and band A and band B are different bands with different carrier frequencies. The UE shall support the switch between single layer transmission with one antenna port and two-layer transmission with two antenna ports on the two uplink bands following the scheduling commands and rank adaptation, i.e., both single layer and two-layer transmission with 2 antenna ports, and single layer transmission with 1 antenna port shall be supported on NR UL carrier 2 and carrier 3 in band B.

The switching periods described in Figure 6.3C.3.3-1a and Figure 6.3C.3.3-1b are located in either NR band A or band B as indicated in RRC signalling uplinkTxSwitchingPeriodLocation [7], and the length of uplink switching period X is less than the value indicated by UE capability uplinkTxSwitchingPeriod .

When switching from one carrier to another, if there is no uplink transmission scheduled or configured on the switch-from carrier for at least the duration of the switching period (X µs) before the point in time the UE is scheduled or configured to start the transmission on the switch-to carrier, the switching period is fully contained in the time period between the end of the transmission on the switch-from carrier and the start of the transmission on the switch-to carrier. In addition, the RRC signalling uplinkTxSwitchingPeriodLocation is ignored by the UE and does not take effect in this case.

Figure 6.3C.3.3-1a: Time mask for switching between one carrier in band A and two contiguous carriers in band B, where the switching period is located in band A

Figure 6.3C.3.3-1b: Time mask for switching between one carrier in band A and two contiguous carriers in band B, where the switching period is located in band B

The following applies for the uplink switching case specified in clause 6.1.6.3 of [10] when the configuration of the location of the switching period by uplinkTxSwitchingPeriodLocation is ignored by the UE:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the uplink switching gap indicated by uplinkTxSwitchingPeriod on any of the carriers before T0, transient periods of 10 ms are located at the end of the last symbol(s) configured or scheduled on the carriers before T0 and at the start of the first symbol(s) configured or scheduled at T0 on the switched-to carrier.

The requirements apply for the case of co-located and synchronized network deployment for the three uplink carriers.

The requirements apply for the case of single TAG for the three uplink carriers, i.e., the same uplink timing for the three carriers as described in clause 4.2 of TS 38.213 [8].

## 6.3C.3.4Time mask for switching between two uplink bands with two transmit antenna connectors

The switching time mask specified in this clause is applicable for an uplink band pair of a SUL configuration when the capability uplinkTxSwitchingPeriod2T2T is present, is only applicable for uplink switching mechanisms specified in clause 6.1.6 of TS 38.214 [10], where NR SUL carrier 1 in band A is capable of two transmit antenna connectors and NR UL carrier 2 and carrier 3 in band B are capable of two transmit antenna connectors. NR UL carrier 2 and carrier 3 are two contiguous aggregated carriers, and band A and band B are different bands with different carrier frequencies. The UE shall support the switch between two-layer transmission with two antenna ports and two-layer transmission with two antenna ports on the two uplink bands following the scheduling commands and rank adaptation, i.e., both single layer and two-layer transmission with 2 antenna ports, and single layer transmission with 1 antenna port shall be supported on NR UL carrier 1, carrier 2 and carrier 3 in the two bands.

The switching periods described in Figure 6.3C.3.4-1a and Figure 6.3C.3.4-1b are located in either NR band A or band B as indicated in RRC signalling uplinkTxSwitchingPeriodLocation  [7], and the length of uplink switching period X is less than the value indicated by UE capability uplinkTxSwitchingPeriod2T2T.

When switching from one carrier to another, if there is no uplink transmission scheduled or configured on the switch-from carrier for at least the duration of the switching period (X µs) before the point in time the UE is scheduled or configured to start the transmission on the switch-to carrier, the switching period is fully contained in the time period between the end of the transmission on the switch-from carrier and the start of the transmission on the switch-to carrier. In addition, the RRC signalling uplinkTxSwitchingPeriodLocation is ignored by the UE and does not take effect in this case.

Figure 6.3C.3.4-1a: Time mask for switching between one carrier in band A and two contiguous carriers in band B, where the switching period is located in band A

Figure 6.3C.3.4-1b: Time mask for switching between one carrier in band A and two contiguous carriers in band B, where the switching period is located in band B

The following applies for the uplink switching case specified in clause 6.1.6.3 of [10] when the configuration of the location of the switching period by uplinkTxSwitchingPeriodLocation is ignored by the UE:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the uplink switching gap indicated by uplinkTxSwitchingPeriod2T2T on any of the carriers before T0, transient periods of 10 ms are located at the end of the last symbol(s) configured or scheduled on the carriers before T0 and at the start of the first symbol(s) configured or scheduled at T0 on the switched-to carrier.

The requirements apply for the case of co-located and synchronized network deployment for the three uplink carriers.

The requirements apply for the case of single TAG for the three uplink carriers, i.e., the same uplink timing for the three carriers as described in clause 4.2 of TS 38.213 [8].

## 6.3C.3.5Time mask for switching across up to four uplink bands

The switching time mask requirements specified in this sub-clause are applicable for an NR SUL band configuration with inter-band CA when the capability supportedBandPairListNR-r18 is present, and are only applicable for uplink switching mechanisms specified in clause [6.1.6] of TS 38.214 [10].

In the NR SUL band configuration with inter-band CA, the number of uplink bands with different carrier frequencies is up to four.  NR UL carrier(s) in each of the up to four uplink bands are capable of one or two transmit antenna connector(s), according to the UE capability FeatureSetUplinkPerCC.

The switching time masks in Figure 6.3C.3.5-1 and Figure 6.3C.3.5-2 are applicable to each of the uplink band pairs in the SUL band configuration with inter-band CA, and are applicable to uplink transmissions when configured with switchedUL or dualUL by the parameter switchingOptionConfigForBandPair. To simplify the figures, the two bands in different band pairs are denoted as NR band X and band Y. The uplink transmission on either band X or band Y is with one or two transmit antenna connector(s),

–if NR UL carriers in both bands in one band pair are capable of one transmit antenna connector, 1Tx-1Tx switching is supported for the band pair;

–if NR UL carrier(s) in one band of one band pair is capable of one transmit antenna connector, and NR UL carrier(s) in the other band of the band pair is capable of two transmit antenna connectors, 1Tx-2Tx switching is supported for the band pair;

–if NR UL carriers in both bands of one band pair are capable of two transmit antenna connectors, 2Tx-2Tx switching is supported for the band pair.

For each band pair, the switching periods described in Figure 6.3C.3.5-1 and Figure 6.3C.3.5-2 are located in either NR band X or band Y as indicated in RRC signalling uplinkTxSwitchingBandList [7]. For each band pair, the length of uplink switching period X is indicated by RRC signalling switchingPeriodConfigForBandPair [7]. UE shall be capable to transmit until the beginning of the switching period and after the end of switching period with the exception of transient periods.

Figure 6.3C.3.5-1: Time mask for switching between band X and band Y,where the switching period is located in band X

Figure 6.3C.3.5-2: Time mask for switching between band X and band Y,where the switching period is located in band Y

The following applies for the uplink switching cases specified in Figure 6.3C.3.5-1 and 6.3C.3.5-2 in a band pair with switchingOptionConfigForBandPair set to either switchedUL or dualUL:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the length of uplink switching period of X µs indicated by RRC signalling switchingPeriodConfigForBandPair on any of the carriers band X and band Y before T0,

-the configuration of the location of the switching period by [uplinkTxSwitchingBandList-r18] is ignored by the UE;

-transient periods of 10 s are located at the end of the last symbol(s) configured or scheduled on the carrier(s) before T0 and at the start of the first symbol(s) configured or scheduled at T0 on the switch-to carrier(s).

In addition to the requirements in Figure 6.3C.3.5-1 and Figure 6.3C.3.5-2, the requirements in Figure 6.3C.3.5-3 to 6.3C.3.5-5 are applicable when dualUL are supported on certain band pair(s) in the SUL band configuration with inter-band CA.

The switching time masks in Figure 6.3C.3.5-3 and Figure 6.3C.3.5-4 are applicable when dualUL is supported for at least two uplink band pairs in the band configuration. The two band pairs supporting dualUL are denoted as band pairs of {band X and band Z} and {band Y and band Z}. When one transmitter is switched between band X and band Y,

–As baseline UE behaviour, the UE is not required to transmit on any of the three bands during time period T1 located on band X and band Z, where T1 is the length of switching period for the band pair of band X and band Y, as shown in Figure 6.3C.3.5-4.

–As optional UE behaviours, when the UE indicates band Z in the capability bandIndexUnaffected,

–if the UE indicates maintainedUL-Trans for band pair of {band X and band Y}, UE shall be capable of uplink transmission on band Z during the switching period that is located on band X, and UE is not required to transmit on band X and Y during time period T1 located on band X, where T1 is the length of switching period for the band pair of band X and band Y, as shown in Figure 6.3C.3.5-3;

–otherwise, theUE is not required to transmit on any of the three bands during the switching period indicated by UE capability periodOnULBands [located on band X and band Z, as shown in Figure 6.3C.3.5-4.

In Figure 6.3C.3.5-3 and Figure 6.3C.3.5-4, the uplink transmission on band X, band Y and band Z are all with one transmit antenna connector and one antenna port.

Figure 6.3C.3.5-3: Time mask for one transmitter switching between band X and band Y, and UE is capable of uplink transmission on band Z during the switching period

The following applies for the uplink switching cases specified in Figure 6.3C.3.5-3 in a band pair with switchingOptionConfigForBandPair set to dualUL:

-if an uplink switching is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the length of uplink switching periods indicated by RRC signalling switchingPeriodConfigForBandPair on any of the carriers in band X and band Y before T0,

-the configuration of the location of the switching period by uplinkTxSwitchingBandList is ignored by the UE;

-transient periods of 10 s are located at the end of the last symbol(s) configured or scheduled on the carrier(s) before T0 and at the start of the first symbol(s) configured or scheduled at T0 on the switch-to carrier(s).

Figure 6.3C.3.5-4: Time mask for one transmitter switching between band X and band Y, and UE is not capable of uplink transmission on band Z during the switching period

The switching time mask in Figure 6.3C.3.5-5 is applicable when dualUL is supported for at least one uplink band pair including band X and band Y, and two transmit antenna connectors are supported on at least one uplink band of band Z. When one transmitter is switched between band X and band Z, and across the same time, the other transmitter is switched between Y and band Z, the switching time mask in Figure 6.3C.3.5-5 is applicable.

–As baseline UE behaviour, UE is not required to transmit on any of the three bands during time period with the larger one of swithching period T2 and T3, where T2 is the length of switching period for the band pair of band X and band Z, and T3 is the length of switching period for the band pair of band Y and band Z.

–As optional UE behaviour when UE additionally reports band pair of {band X and band Y} and band Z in the capability uplinkTxSwitchingAdditionalPeriodDualUL-List, UE is not required to transmit on any of the three bands during time period indicated by UE capability switchingAdditionalPeriodDualUL.

In Figure 6.3C.3.5-5, the uplink transmission on band X and band Y is with one transmit antenna connector and one antenna port, and the uplink transmission on band Z is with two transmit antenna connectors and two antenna ports. The switching period location is configured according to [7], and band Z is with the highest priority according to the RRC configuration uplinkTxSwitchingBandList.

Figure 6.3C.3.5-5: Time mask for one transmitter switching between band X and band Z,and one transmitter switching between band Y and band Z

The following applies for the uplink switching case specified in Figure 6.3C.3.5-5 and with uplinkTxSwitchingOptionForBandPair set to dualUL for at least one band pair.

-if uplink switching on a band pair is triggered for an uplink transmission starting at T0 based on higher layer configuration(s) or DCI(s) received before T0 − Toffset as specified in [10] and the UE is not configured or scheduled with uplink transmissions for a duration of at least the maximum of the lengths of uplink switching periods indicated by RRC signalling switchingPeriodConfigForBandPair on any of the carriers in band X, band Y and band Z before T0 on any switched-to carrier

-the configuration of the location of the switching period and the priority of bands in the uplinkTxSwitchingBandList are ignored by the UE

-transient periods of 10 ms are located at the end of the last symbol(s) configured or scheduled on the switched-from carrier(s) before T0 on any switched-to and at the start of the first symbol(s) configured or scheduled at T0 on the switch-to carrier(s)

The requirements in this sub-clause apply for the case of synchronized network deployment for the uplink bands.

## 6.3C.3.5aAdditional requirements for three-band switching with dual TAG

The following applies for the uplink switching case specified in Figure 6.3C.3.5-5 with three bands involved in the switching and with uplinkTxSwitchingOptionForBandPair-r18 set to dualUL for at least one band pair.

If the UE is configured with dual TAG and not configured or scheduled with uplink transmissions for a duration of at least the maximum of the lengths of uplink switching periods indicated by UE capability [uplinkTxSwitchingPeriodForBandPair-r18] on any of the carriers in band X, band Y and band Z including any timing difference between the uplink carriers before the first T0 on any switched-to carrier,

-the configuration of the location of the switching period and the priority of bands in the uplinkTxSwitchingBandList are ignored by the UE

-transient periods of 10 s are located at the end of the last symbol(s) configured or scheduled on the switched-from carrier(s) before the first T0 on any switched-to carrier and at the start of the first symbol(s) configured or scheduled at T0 on the switch-to carrier(s)

## 6.3DOutput power dynamics for UL MIMO

## 6.3D.1Minimum output power for UL MIMO

For UE with two or four transmit antenna connectors in closed-loop spatial multiplexing scheme, the minimum output power is defined as the sum of the mean power from all transmit connectors in one sub-frame (1 ms). The minimum output power shall not exceed the values specified in Table 6.3.1-1.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.3.1 apply when TxD is not indicated, and the requirements in clause 6.3G.1 apply when TxD is indicated.

## 6.3D.2Transmit OFF power for UL MIMO

The transmit OFF power is defined as the mean power at each transmit antenna connector in a duration of at least one sub-frame (1 ms) excluding any transient periods.

The transmit OFF power at each transmit antenna connector shall not exceed the values specified in Table 6.3.2-1.

## 6.3D.3Transmit ON/OFF time mask for UL MIMO

For UE supporting UL MIMO, the ON/OFF time mask requirements in clause 6.3.3 apply at each transmit antenna connector.

For UE with two or four transmit antenna connectors in closed-loop spatial multiplexing scheme, the general ON/OFF time mask requirements specified in clause 6.3.3.1 apply to each transmit antenna connector. The requirements shall be met with the UL MIMO configurations described in clause 6.2D.1.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.3.3 apply when TxD is not indicated, and the requirements in clause 6.3G.3 apply when TxD is indicated.

## 6.3D.4Power control for UL MIMO

For UE supporting UL MIMO, the power control tolerance applies to the sum of output powers from all transmit antenna connectors.

The power control requirements specified in clause 6.3.4 apply to UE with all transmit antenna connectors in closed-loop spatial multiplexing scheme. The requirements shall be met with UL MIMO configurations described in clause 6.2D.1.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.3.4 apply when TxD is not indicated, and the requirements in clause 6.3G.4 apply when TxD is indicated.

## 6.3EOutput power dynamics for V2X

## 6.3E.1Minimum output power for V2X

## 6.3E.1.1General

When UE is configured for NR V2X sidelink transmissions non-concurrent with NR uplink transmissions for NR V2X operating bands in Table 5.2E.1-1, the minimum output power is specified in Table 6.3E.1.1-1. The minimum output power is defined as the mean power in at least one sub-frame 1 ms.

Table 6.3E.1.1-1: Minimum output power

For NR V2X UE with two transmit antenna connectors, the minimum output power is defined as the sum of the mean power at each transmit connector in one sub-frame (1 ms). The minimum output power shall not exceed the values specified for single carrier.

If the UE transmits on one antenna connector at a time, the requirements specified for single carrier shall apply to the active antenna connector.

## 6.3E.1.1AMinimum output power for sidelink CA

For SL intra-band contiguous/non-contiguous CA, the minimum output power requirement as specified in Table 6.3E.1.1A -1 shall be applied per component carrier.

Table 6.3E.1.1A -1: Minimum output power

## 6.3E.1.2Minimum output power for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 6.3.1 shall apply for the uplink in licensed band and the requirements specified in clause 6.3E.1.1 shall apply for the sidelink in licensed band or Band n47.

For intra-band concurrent NR V2X operation, the minimum output power is defined per carrier and the requirement for NR uplink is specified in clause 6.3.1 and the requirement for NR sidelink is specified in clause 6.3E.1, respectively.

## 6.3E.1FMinimum output power for Sidelink Unlicensed

The requirements for minimum output power in clause 6.3.1 apply.

## 6.3E.1F.1Minimum output power for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the requirements specified in clause 6.3.1 shall apply for NR Uu operation in licensed band and the requirements specified in clause 6.3E.1F shall apply for NR sidelink operation in unlicensed band.

## 6.3E.2Transmit OFF power for V2X

## 6.3E.2.1General

When UE is configured for NR V2X sidelink transmissions non-concurrent with NR uplink transmissions for NR V2X operating bands in Table 5.2E.1-1, the requirements specified in current clause apply.

Table 6.3E.2.1-1: Transmit OFF power

For NR V2X UE supporting SL MIMO or Tx Diversity, the transmit OFF power at each transmit antenna connector shall not exceed the values specified in Table 6.3E.2.1-1 for single carrier. Transmit off power is defined as the mean power in at least one sub-frame 1 ms.

## 6.3E.2.1ATransmit OFF power for sidelink CA

For SL intra-band contiguous/non-contiguous CA, the transmit OFF power requirement as specified in Table 6.3E.2.1A -1 shall be applied per component carrier.

Table 6.3E.2.1A -1: Transmit OFF power

## 6.3E.2.2Transmit OFF power for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 6.3.2 shall apply for the uplink in licensed band and the requirements specified in clause 6.3E.2.1 shall apply for the sidelink in licensed band or Band n47.

For intra-band concurrent NR V2X operation, the transmit OFF power requirement is defined per carrier and the requirement for NR uplink is specified in clause 6.3.2 and the requirement for NR sidelink is specified in clause 6.3E.2, respectively.

## 6.3E.2FTransmit OFF power for Sidelink Unlicensed

The requirements for Transmit OFF power in clause 6.3.2 apply for SL-U operation.

## 6.3E.2F.1Transmit OFF power for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the requirements specified in TS 38.101-1 clause 6.3.2 shall apply for NR Uu operation in licensed band and the requirements specified in clause 6.3E.2F shall apply for NR sidelink operation in unlicensed band.

## 6.3E.3Transmit ON/OFF time mask for V2X

## 6.3E.3.1General

For NR V2X UE, additional requirements on ON/OFF time masks for V2X physical channels and signals are specified in this clause.

## 6.3E.3.1ATransmit ON/OFF time mask for sidelink CA

For SL intra-band contiguous/non-contiguous CA, the SL ON/OFF time masks specified in clause 6.3E.3.2, 6.3E.3.3 and 6.3E.3.4 are applicable to each component carrier during the ON power period and the transient periods. The OFF period shall only be applicable to each component carrier when all the component carriers are OFF.

## 6.3E.3.2General time mask

The General ON/OFF time mask defines the observation period between the Transmit OFF and ON power and between Transmit ON and OFF power for PSCCH, and PSSCH transmissions in a slot wherein the last symbol is punctured to create a guard period.

Figure 6.3E.3.2-1: General PSCCH/PSSCH time mask for NR V2X UE

For NR V2X UE supporting SL MIMO or Tx Diversity, the ON/OFF time mask requirements apply at each transmit antenna connector.

For UE with two transmit antenna connectors, the general ON/OFF time mask requirements specified in current subclause apply to each transmit antenna connector.

If the UE transmits on one antenna connector at a time, the general ON/OFF time mask requirements apply to the active antenna connector.

## 6.3E.3.3S-SSB time mask

The S-PSS/S-SSS/PSBCH time mask for NR V2X UE defines the observation period between transmit OFF and ON S-PSS power and between transmit ON PSBCH and OFF power in a slot wherein the last symbol is punctured to create a guard period.

Figure 6.3E.3.3-1: S-SSB time mask for NR V2X UE

For NR V2X UE supporting SL MIMO or Tx Divesity, the ON/OFF time mask requirements apply at each transmit antenna connector.

For UE with two transmit antenna connectors, the S-SSB ON/OFF time mask requirements specified in current subclause apply to each transmit antenna connector.

If the UE transmits on one antenna connector at a time, the S-SSB ON/OFF time mask requirements apply to the active antenna connector.

## 6.3E.3.4Transmit ON/OFF time mask for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 6.3.3 shall apply for the uplink in licensed band and the requirements specified in clause 6.3E.3.2 and 6.3E.3.3 shall apply for the sidelink in licensed band or Band n47.

For intra-band V2X concurrent operation band specified in subclause 5.2.E.2, the general output power ON/OFF time mask is defined per carrier during the ON power period and the transient periods. The ON/OFF time mask specified in clause 6.3.3.1 is applicable for NR uplink and the ON/OFF time mask in 6.3E.3.1 is applicable for NR sidelink. The OFF period as specified in clause 6.3.3.1 shall only be applicable for each component carrier when all the component carriers are OFF.

For the TDM operation in same carrier with same bandwidth, the switching time mask in Figure 6.3E.3.4-1 shall be applied.

Figure 6.3E.3.4-1: Time mask for switching between Uu and SL forsame carrier case with same bandwidth

For intra-band V2X concurrent operation band specified in subclause 5.3.E.2, the switching time mask in Figure 6.3E.3.4-2 shall apply for the different carrier case. The switching time shall be located on the RAT of low priority when NR Uu and NR SL have different priorities based on priority information specified in TS 38.321 and TS38.213. It is up to UE implementation when NR Uu and NR SL have the same priority based on priority information specified in TS 38.213.

Figure 6.3E.3.4-2: Time mask for switching between Uu and SL for different carrier case

In the real field, there is a timing advance difference, i.e.  between NR Uu slot and NR SL slot due to different timing advance of NR Uu and NR SL. The switching time masks do not include timing advance difference but the timing advance difference should be considered with the switching time for same carrier case and different carrier case.NTA∙Tc

## 6.3E.3FTransmit ON/OFF time mask for Sidelink Unlicensed

## 6.3E.3F.1General

The transmit power time mask defines the transient period(s) allowed between transmit OFF power as defined in clause 6.3E.2F and transmit ON power symbols (transmit ON/OFF). The transmit power ON/OFF time mask specified in clause 6.3E.3F.2 supercedes the ON/OFF masks specified in clause 6.3.3; however, between continuous ON-power transmissions the requirements in clause 6.3.3 apply. Unless otherwise stated the requirements in clause 6.5F apply also in transient periods.

## 6.3E.3F.2General ON/OFF time mask

The general ON/OFF time mask defines the observation period between transmit OFF and ON power and between transmit ON and OFF power for each SCS as illustrated below in Figure 6.3E.3F.2-1. ON/OFF scenarios include: contiguous, and non-contiguous transmission, etc.

The OFF power measurement period is defined in a duration of at least one slot excluding any transient periods. The ON power is defined as the mean power over the duration of at least one slot excluding any transient period and non-transmitted symbols. The leading transient period starts 5us before the beginning of the first symbol of transmission and extends 10us into the transmission including the CP extension if applicable. The last symbol is punctured to create a guard period where the trailing transient period of 10us is located inside.

Figure 6.3E.3F-1 General ON/OFF time mask for SL-U PSSCH and PSCCH

## 6.3E.3F.3S-SSB time mask

The S-PSS/S-SSS/PSBCH time mask for NR Sidelink Unlicensed UE defines the observation period between transmit OFF and ON S-PSS power and between transmit ON PSBCH and OFF power in a slot wherein the last symbol is punctured to create a guard period. The leading transient period starts 5us before the beginning of the first symbol of transmission and extends 10us into the transmission including the CP extension if applicable. The last symbol is punctured to create a guard period where the trailing transient period of 10us is located inside.

Figure 6.3E.3F-2 ON/OFF time mask for SL-U S-SSB

## 6.3E.3F.4Transmit ON/OFF time mask for NR SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the requirements specified in clause 6.3.3 shall apply for the uplink in licensed band and the requirements specified in clause 6.3E.3F.2 and 6.3E.3F.3 shall apply for NR sidelink operation in unlicensed band.

## 6.3E.4Power control for V2X

## 6.3E.4.1General

When UE is configured for NR V2X sidelink transmissions non-concurrent with NR uplink transmissions for NR V2X operating bands in Table 5.2E.1-1, the following requirements are applied for NR V2X sidelink transmission.

For NR V2X UE supporting SL MIMO or Tx Diversity, the power control tolerance for single carrier shall apply to the sum of output power at each transmit antenna connector.

If the UE transmits on one antenna connector at a time, the requirements for single carrier shall apply to the active antenna connector.

The relative slot power tolerance for V2X UE supporting co-channel coexistence with LTE SL is the ability of the NR V2X UE operating with 30kHz SCS to control the output power of transmitted slots during PSCCH/PSSCH transmission consisting of two slots overlapping with an LTE SL subframe (500us). The reference slot is the 1st slot overlapping with LTE SL subframe and target slot is the subsequent NR SL slot overlapping with the LTE SL subframe. The measurement period for reference and target slot is one NR SL slot with guard symbol omitted. The power of the target slot must be the same or lower than the power of the reference slot using the tolerance equal to relaxation given for Table 6.2.4-1 values in 6.2E.4.1.

## 6.3E.4.1APower control for sidelink CA

For SL intra-band contiguous/non-contiguous CA, the power control requirement as specified in clause 6.3E.4.2 shall be applied per component carrier.

## 6.3E.4.2Absolute power tolerance

The requirements in clause 6.3.4.2 shall apply for NR V2X transmission.

## 6.3E.4.3Power control for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 6.3.4 shall apply for the uplink in licensed band and the requirements specified in clause 6.3E.4.1 and 6.3E.4.2 shall apply for the sidelink in licensed band or Band n47.

For the intra-band concurrent NR V2X operation, the requirements specified in clause 6.3.4 shall apply for the uplink in licensed band and the requirements specified in clause 6.3E.4 shall apply for the sidelink in licensed band.

## 6.3E.4FPower control for Sidelink Unlicensed

## 6.3E.4F.1General

The requirements on power control accuracy apply under normal conditions.

## 6.3E.4F.2Absolute power tolerance

The absolute power tolerance requirements of clause 6.3.4.2 apply at the start of a contiguous transmission or non-contiguous transmission with a transmission gap larger than 40 ms.

## 6.3E.4F.3Power control for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the requirements specified in clause 6.3.4 shall apply for NR Uu operation in licensed band and the requirements specified in clause 6.3E.4F.1 and 6.3E.4F.2 shall apply for NR sidelink operation in unlicensed band.

## 6.3FOutput power dynamics for shared spectrum channel access

## 6.3F.1Minimum output power

The requirements for minimum output power in clause 6.3.1 apply.

## 6.3F.2Transmit OFF power

The requirements for Transmit OFF power in clause 6.3.2 apply.

## 6.3F.3Transmit ON/OFF time mask

## 6.3F.3.1General

The transmit power time mask defines the transient period(s) allowed between transmit OFF power as defined in clause 6.3F.2 and transmit ON power symbols (transmit ON/OFF).  The transmit power ON/OFF time mask specified in clause 6.3F.3.2 supersedes the ON/OFF masks specified in clause 6.3.3; however, between continuous ON-power transmissions the requirements in clause 6.3.3 apply. Unless otherwise stated the requirements in clause 6.5F apply also in transient periods.

## 6.3F.3.2General ON/OFF time mask

The general ON/OFF time mask defines the observation period between transmit OFF and ON power and between transmit ON and OFF power for each SCS as illustrated below in Figure 6.3F.3.2-1. ON/OFF scenarios include: contiguous, and non-contiguous transmission, etc.

The OFF power measurement period is defined in a duration of at least one slot excluding any transient periods. The ON power is defined as the mean power over the duration of at least one slot excluding any transient period and non-transmitted symbols.  The leading transient period starts 5us before the beginning of the first symbol of transmission and extends 10us into the transmission including the CP extension if applicable.  The trailing transient period starts 5us before the end of transmission and extends 5us beyond the end of transmission.

CP-ECP-EEnd of OFF power 5µs5µsTransient periodTransient periodStart of OFF power Start of ON power requirementStart of transmissionEnd of transmissionEnd of ON power requirement* The OFF power requirements does not apply for DTX and measurement gaps10µs5µsEnd of OFF power 5µs5µsTransient periodTransient periodStart of OFF power Start of ON power requirementStart of transmissionEnd of transmissionEnd of ON power requirement* The OFF power requirements does not apply for DTX and measurement gaps10µs5µsFigure 6.3F.3.2-1: General ON/OFF time mask for shared spectrum channel access

## 6.3F.3AGeneral ON/OFF mask for CA

## 6.3F.3A.1General ON/OFF mask for inter-band CA

For inter-band carrier aggregation with uplink assigned to two bands and including one of the bands listed in Table 6.2F.1-1, the general output power ON/OFF time mask specified in clause 6.3.3.1 is applicable for the NR uplink carrier while the general output power ON/OFF time mask specified in clause 6.3F.3 is applicable for the carrier operating with shared spectrum access. The OFF period as specified in clause 6.3.3.1 and clause 6.3F.3 shall only be applicable for each component carrier when all the component carriers are OFF.

## 6.3F.4Power control

## 6.3F.4.1General

The requirements on power control accuracy apply under normal conditions.

## 6.3F.4.2Absolute power tolerance

The absolute power tolerance requirements of clause 6.3.4.2 apply at the start of a contiguous transmission or non-contiguous transmission with a transmission gap larger than 40 ms.

## 6.3F.4.3Relative power tolerance

The relative power tolerance requirements of clause 6.3.4.3 apply if the transmission gap between the target sub-frame and the reference sub-frame is less than or equal to 40 ms.

## 6.3F.4.4Aggregate power tolerance

The aggregate power tolerance requirements of clause 6.3.4.4 apply during non-contiguous transmissions within 41ms with respect to the first UE transmission.

## 6.3F.4APower control for inter-band CA

No requirements unique to CA operation are defined.

## 6.3GOutput power dynamics for Tx Diversity

## 6.3G.1Minimum output power for Tx Diversity

For UE supporting Tx diversity, the minimum output power is defined as the sum of the mean power at each transmit connector in one sub-frame (1 ms). The minimum output power shall not exceed the values specified in Table 6.3.1-1.

## 6.3G.2Transmit OFF power for Tx Diversity

For UE supporting Tx diversity, the transmit OFF power is defined as the mean power at each transmit antenna connector in a duration of at least one sub-frame (1 ms) excluding any transient periods.

The transmit OFF power at each transmit antenna connector shall not exceed the values specified in Table 6.3.2-1.

## 6.3G.3Transmit ON/OFF time mask for Tx Diversity

For UE supporting Tx diversity, the ON/OFF time mask requirements in clause 6.3.3 apply at each transmit antenna connector.

## 6.3G.4Power control for Tx Diversity

For UE supporting Tx diversity, the power control tolerance applies to the sum of output power at each transmit antenna connector.

The requirements specified in clause 6.3.4 apply.

## 6.3HOutput power dynamics for CA with UL MIMO

## 6.3H.1Output power dynamics for intra-band UL contiguous CA with UL MIMO

## 6.3H.1.1Minimum output power for intra-band UL contiguous CA with UL MIMO

For intra-band UL contiguous CA and UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the minimum output power is defined as the sum of the mean power from both transmit connector in one sub-frame (1 ms) on each CC. The minimum output power shall not exceed the values specified in clause 6.3A.1.1.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.3A.1.1 apply.

## 6.3H.1.2Transmit OFF power for intra-band UL contiguous CA with UL MIMO

The transmit OFF power is defined as the mean power at each transmit antenna connector in a duration of at least one sub-frame (1 ms) excluding any transient periods.

The transmit OFF power at each transmit antenna connector on each CC shall not exceed the values specified in clause 6.3A.2.1.

## 6.3H.1.3Transmit ON/OFF time mask for intra-band UL contiguous CA with UL MIMO

For UE supporting intra-band UL contiguous CA and UL MIMO, the ON/OFF time mask requirements in clause 6.3A.3.1 apply at each transmit antenna connector on each CC. The requirements shall be met with the UL MIMO configurations described in Table 6.2D.1-2.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.3A.3.1 apply.

## 6.3H.1.4Power control for intra-band UL contiguous CA with UL MIMO

For UE supporting intra-band UL contiguous CA and UL MIMO, the power control tolerance in clause 6.3A.4.1 applies to the sum of output powers from both transmit antenna connector on each CC. The requirements shall be met with UL MIMO configurations described in Table 6.2D.1-2.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.3A.4.1 apply.

6.3H.2Void

## 6.3H.3Output power dynamics for inter-band UL CA with UL MIMO

## 6.3H.3.1Minimum output power for inter-band UL CA with UL MIMO

For inter-band UL CA with UL MIMO in one of the two frequency bands, the minimum output power is defined per carrier. The requirement is specified in clause 6.3.1 for the carrier without UL MIMO and specified in clause 6.3D.1 for the carrier configured with UL MIMO.

## 6.3H.3.2Transmit OFF power for inter-band UL CA with UL MIMO

For inter-band UL CA with UL MIMO in one of the two frequency bands, the transmit OFF power specified in clause 6.3.2 is applicable for the carrier without UL MIMO and the transmit OFF power specified in clause 6.3D.2 is applicable for the carrier configured with UL MIMO when the transmitter is OFF on all component carriers. The transmitter is considered to be OFF when the UE is not allowed to transmit on any of its ports.

## 6.3H.3.3Transmit ON/OFF time mask for inter-band UL CA with UL MIMO

For inter-band UL CA with UL MIMO in one of the two frequency bands, the general output power ON/OFF time mask specified in clause 6.3.3.1 is applicable for the component carrier without UL MIMO during the ON power period and the transient periods, the ON/OFF time mask specified in clause 6.3D.3 is applicable for the component carrier configured with UL MIMO. The OFF period as specified in clause 6.3.3.1 shall only be applicable for each component carrier when all the component carriers are OFF.

## 6.3H.3.4Power control for inter-band UL CA with UL MIMO

No requirements unique to CA operation are defined.

## 6.3I(Reserved)

## 6.3JOutput power dynamics for ATG

## 6.3J.1Minimum output power for ATG

The minimum controlled output power of the UE is defined as the power in the channel bandwidth for all transmit bandwidth configurations (resource blocks) when the power is set to a minimum value.

The minimum output power is defined as the sum of the mean power from all antenna connectors or all TAB connectors in at least one sub-frame (1 ms). The minimum output power shall not exceed the values specified in Table 6.3J.1-1for ATG UE with omni-directional antenna and in Table 6.3J.1-2 for ATG UE with antenna array.

Table 6.3J.1-1: Minimum output power for ATG UE with omni-directional antenna

Table 6.3J.1-2: Minimum output power for ATG UE with antenna array

## 6.3J.1DMinimum output power for ATG UL MIMO

For ATG UE with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer), the minimum output power is defined as the sum of the mean power from all antenna connectors or all TAB connectors in one sub-frame (1ms). The minimum output power shall not exceed the values specified in Table 6.3J.1-1.

If ATG UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.3J.1 apply when TxD is not indicated.

## 6.3J.2Transmit OFF power for ATG

The transmit OFF power is defined as the mean power at each transmit antenna connector or each TAB connector in a duration of at least one sub-frame (1 ms) excluding any transient periods.

The transmit OFF power requirements as specified in clause 6.3.2 are applicable for ATG UE.

## 6.3J.2DTransmit OFF power for ATG UL MIMO

The transmit OFF power is defined as the mean power at each transmit antenna connector or each TAB connector in a duration of at least one sub-frame (1ms) excluding any transient periods.

The transmit OFF power requirements as specified in clause 6.3J.2 are applicable for ATG UE with UL MIMO.

## 6.3J.3Transmit ON/OFF time mask for ATG

The transmit ON/OFF time mask requirements as specified in clause 6.3.3 are applicable for ATG UE at each transmit antenna connector or each TAB connector.

## 6.3J.3DTransmit ON/OFF time mask for ATG UL MIMO

The transmit ON/OFF time mask requirements as specified in clause 6.3J.3 are applicable for ATG UE at each transmit antenna connector or each TAB connector.

For ATG UE with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer) in closed-loop spatial multiplexing scheme, the general ON/OFF time mask requirements specified in clause 6.3J.3 apply to each transmit antenna connector or each TAB connector. The requirements shall be met with the UL MIMO configurations described in clause 6.2J.1D.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.3J.3 apply when TxD is not indicated, and the requirements in clause 6.3G.3 apply when TxD is indicated.

## 6.3J.4Power control for ATG

The power control requirements specified in clause 6.3.4 are applicable to the sum of output power at each transmit antenna connector for UE with omnidirectional antenna(s) or to the sum of output power at each transceiver array boundary (TAB) connectors for UE with antenna array for ATG UE.

## 6.3J.4DPower control for ATG UL MIMO

For ATG UE supporting UL MIMO, the power control tolerance applies to the sum of output powers from all transmit antenna connectors of ATG UE with omni-directional antenna or the sum of output powers from all TAB connectors of ATG UE with antenna array.

The power control requirements specified in clause 6.3J.4 apply to ATG UE with all transmit antenna connectors or all TAB connectors in closed-loop spatial multiplexing scheme. The requirements shall be met with UL MIMO configurations described in clause 6.2J.1D.

If ATG UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.3J.4 apply when TxD is not indicated.

## 6.3K(Reserved)

## 6.3LOutput power dynamics for CA with Tx Diversity

## 6.3L.1Void

## 6.3L.2Void

## 6.3L.3Output power dynamics for inter-band UL CA with Tx Diversity

## 6.3L.3.1Minimum output power for inter-band UL CA with Tx Diversity

For inter-band UL CA with Tx Diversity in one of the two frequency bands, the minimum output power is defined per carrier. The requirement is specified in clause 6.3.1 for the carrier without Tx Diversity and specified in clause 6.3G.1 for the carrier configured with Tx Diversity.

## 6.3L.3.2Transmit OFF power for inter-band UL CA with Tx Diversity

For inter-band UL CA with Tx Diversity in one of the two frequency bands, the transmit OFF power specified in clause 6.3.2 is applicable for the carrier without Tx Diversity and the transmit OFF power specified in clause 6.3G.2 is applicable for the carrier configured with Tx Diversity when the transmitter is OFF on all component carriers. The transmitter is considered to be OFF when the UE is not allowed to transmit on any of its ports.

## 6.3L.3.3Transmit ON/OFF time mask for inter-band UL CA with Tx Diversity

For inter-band UL CA with Tx Diversity in one of the two frequency bands, the general output power ON/OFF time mask specified in clause 6.3.3.1 is applicable for the component carrier without Tx Diversity during the ON power period and the transient periods, the ON/OFF time mask specified in clause 6.3G.3 is applicable for the component carrier configured with Tx Diversity. The OFF period as specified in clause 6.3.3.1 shall only be applicable for each component carrier when all the component carriers are OFF.

## 6.3L.3.4Power control for inter-band UL CA with Tx Diversity

No requirements unique to CA operation are defined.

## 6.4Transmit signal quality

## 6.4.1Frequency error

The UE basic measurement interval of modulated carrier frequency is 1 UL slot. The mean value of basic measurements of UE modulated carrier frequency shall be accurate to within ± 0.1 PPM observed over a period of 1 ms of cumulated measurement intervals compared to the carrier frequency received from the NR Node B.

## 6.4.2Transmit modulation quality

## 6.4.2.0General

Transmit modulation quality defines the modulation quality for expected in-channel RF transmissions from the UE. The transmit modulation quality is specified in terms of:

-Error Vector Magnitude (EVM) for the allocated resource blocks (RBs)

-EVM equalizer spectrum flatness derived from the equalizer coefficients generated by the EVM measurement process

-Carrier leakage

-In-band emissions for the non-allocated RB

All the parameters defined in clause 6.4.2 are defined using the measurement methodology specified in Annex F.

In case the parameter 3300 or 3301 is reported from UE via the parameter txDirectCurrentLocation in UplinkTxDirectCurrentList IE (as defined in TS 38.331 [7]), carrier leakage measurement requirement in clause 6.4.2.2 and 6.4.2.3 shall be waived, and the RF correction with regard to the carrier leakage and IQ image shall be omitted during the calculation of transmit modulation quality.

## 6.4.2.1Error Vector Magnitude

The Error Vector Magnitude is a measure of the difference between the reference waveform and the measured waveform. This difference is called the error vector. Before calculating the EVM the measured waveform is corrected by the sample timing offset and RF frequency offset. Then the carrier leakage shall be removed from the measured waveform before calculating the EVM.

The measured waveform is further equalised using the channel estimates subjected to the EVM equaliser spectrum flatness requirement specified in clause 6.4.2.4. For DFT-s-OFDM waveforms, the EVM result is defined after the front-end FFT and IDFT as the square root of the ratio of the mean error vector power to the mean reference power expressed as a %. For CP-OFDM waveforms, the EVM result is defined after the front-end FFT as the square root of the ratio of the mean error vector power to the mean reference power expressed as a %.

The basic EVM measurement interval in the time domain is one preamble sequence for the PRACH and one slot for PUCCH and PUSCH in the time domain. The EVM measurement interval is reduced by any symbols that contains an allowable power transient in the measurement interval, as defined in clause 6.3.3.

The RMS average of the basic EVM measurements over 10 subframes for the average EVM case, and over 60 subframes for the reference signal EVM case, for the different modulation schemes shall not exceed the values specified in Table 6.4.2.1-1 for the parameters defined in Table 6.4.2.1-2. For EVM evaluation purposes, all 13 PRACH preamble formats and all 5 PUCCH formats are considered to have the same EVM requirement as QPSK modulated.

Unless otherwise specified, pi/2 BPSK in this clause refers to both variants of pi/2 BPSK referenced in table 6.2.2-1 and table 6.2.2-1a.

Table 6.4.2.1-1: Requirements for Error Vector Magnitude

Table 6.4.2.1-2: Parameters for Error Vector Magnitude

## 6.4.2.1aError Vector Magnitude including symbols with transient period

In 6.4.2.1, EVM has been defined by excluding the symbols which have a transient period. In this section, measurement interval is defined for the symbols with a transient period to include these symbols in the RMS average EVM computation when the UE reports a transient period capability other than the default. Before calculating the EVM, the measured waveform is corrected for sample timing offset and RF frequency offset. Then the carrier leakage shall be removed from the measured waveform before calculating the EVM. The symbols with transient period should not be used for equalization. Only CP-OFDM waveform is used for conformance testing.

In the case of PUSCH or PUCCH transmissions when the mean power, modulation or RB allocation across slot or subslot boundaries is expected to change the EVM result over the symbols where the transient occurs is calculated according to Table 6.4.2.1a-1.

Table 6.4.2.1a-1: EVM definition for reported transient period

The RMS average of the basic EVM measurements over 108 subframes calculated only on the symbols where the transient occurs for the different modulation schemes shall not exceed the values specified in Table 6.4.2.1a-2 for the parameters defined in Table 6.4.2.1a-3. This requirement can be verified with 64 QAM and 256 QAM modulation.

Table 6.4.2.1a-2: Requirements for Error Vector Magnitude

Table 6.4.2.1a-3: Parameters for Error Vector Magnitude

## 6.4.2.2Carrier leakage

Carrier leakage is an additive sinusoid waveform whose frequency is the same as the modulated waveform carrier frequency. The measurement interval is one slot in the time domain.

In the case that uplink sharing, the carrier leakage may have 7.5 kHz shift with the carrier frequency.

The relative carrier leakage power is a power ratio of the additive sinusoid waveform and the modulated waveform. The relative carrier leakage power shall not exceed the values specified in Table 6.4.2.2-1.

Table 6.4.2.2-1: Requirements for Carrier Leakage

## 6.4.2.3In-band emissions

The in-band emission is defined as the average emission across 12 sub-carriers and as a function of the RB offset from the edge of the allocated UL transmission bandwidth. The in-band emission is measured as the ratio of the UE output power in a non–allocated RB to the UE output power in an allocated RB.

The basic in-band emissions measurement interval is defined over one slot in the time domain; however, the minimum requirement applies when the in-band emission measurement is averaged over 10 sub-frames. When the PUSCH or PUCCH transmission slot is shortened due to multiplexing with SRS, the in-band emissions measurement interval is reduced by one or more symbols, accordingly.

The average of the basic in-band emission measurement over 10 sub-frames shall not exceed the values specified in Table 6.4.2.3-1.

Unless otherwise specified, pi/2 BPSK in this clause refers to both variants of pi/2 BPSK referenced in Table 6.2.2-1 and table 6.2.2-1a.

Table 6.4.2.3-1: Requirements for in-band emissions

If the UE supports mpr-SingleCC-SingleValue-r19 or mpr-SingleCC-MultipleValue-r19, and is configured with the IE mprReductionExtensionRatio-r19, and the conditions for which corresponding MPR reduction apply as defined in Clause 6.2.2 for the extended RBs which are inside ceil(Rext_low* NRB) and ceil(Rext_high* NRB) but outside the NRB, the extended regions emissions requirement in Table 6.4.2.3-2 is applied and other OOBE emission requirements are waived. The average of the requirements for extended regions emissions measurement over 10 sub-frames shall not exceed the values specified in Table 6.4.2.3-2. Note that the UE does not expect any scheduling on these extended regions.

Table 6.4.2.3-2: Requirements for extended regions emissions

## 6.4.2.4EVM equalizer spectrum flatness

The zero-forcing equalizer correction applied in the EVM measurement process (as described in Annex F) must meet a spectral flatness requirement for the EVM measurement to be valid. The EVM equalizer spectrum flatness is defined in terms of the maximum peak-to-peak ripple of the equalizer coefficients (dB) across the allocated uplink block. The basic measurement interval is the same as for EVM.

The peak-to-peak variation of the EVM equalizer coefficients contained within the frequency range of the uplink allocation shall not exceed the maximum ripple specified in Table 6.4.2.4-1 for normal conditions. For uplink allocations contained within both Range 1 and Range 2, the coefficients evaluated within each of these frequency ranges shall meet the corresponding ripple requirement and the following additional requirement: the relative difference between the maximum coefficient in Range 1 and the minimum coefficient in Range 2 must not be larger than 5 dB, and the relative difference between the maximum coefficient in Range 2 and the minimum coefficient in Range 1 must not be larger than 7 dB (see Figure 6.4.2.4-1).

The EVM equalizer spectral flatness shall not exceed the values specified in Table 6.4.2.4-2 for extreme conditions. For uplink allocations contained within both Range 1 and Range 2, the coefficients evaluated within each of these frequency ranges shall meet the corresponding ripple requirement and the following additional requirement: the relative difference between the maximum coefficient in Range 1 and the minimum coefficient in Range 2 must not be larger than 6 dB, and the relative difference between the maximum coefficient in Range 2 and the minimum coefficient in Range 1 must not be larger than 10 dB (see Figure 6.4.2.4-1).

Table 6.4.2.4-1: Requirements for EVM equalizer spectrum flatness (normal conditions)

Table 6.4.2.4-2: Minimum requirements for EVM equalizer spectrum flatness (extreme conditions)

f    FUL_High  FUL_High – 3(5) MHz     < 4(4) dBp-p     Range 1Range 2  max(Range 1)-min(Range 2) < 5(6) dB    max(Range 2)-min(Range 1) < 7(10) dB     < 8(12) dBp-p      f    FUL_High  FUL_High – 3(5) MHz     < 4(4) dBp-p     Range 1Range 2  max(Range 1)-min(Range 2) < 5(6) dB    max(Range 2)-min(Range 1) < 7(10) dB     < 8(12) dBp-p

Figure 6.4.2.4-1: The limits for EVM equalizer spectral flatness with the maximum allowed variation of the coefficients indicated (the ETC minimum requirement are within brackets).

## 6.4.2.4.1Requirements for Pi/2 BPSK modulation with powerBoosting-pi2BPSK capability

These requirements apply if the IE powerBoostPi2BPSK is set to 1 for power class 3 UE operating in TDD bands n40, n41, n77, n78 and n79 with Pi/2 BPSK modulation and UE indicates support for UE capability powerBoosting-pi2BPSK and 40 % or less slots in radio frame are used for UL transmission. These requirements also apply if the IE dmrs-UplinkTransformPrecoding-r16 is configured and UE indicates support for UE capability lowPAPR-DMRS-PUSCHwithPrecoding-r16. Otherwise the requirements for EVM equalizer spectrum flatness defined in clause 6.4.2.4 apply

The EVM equalizer coefficients across the allocated uplink block shall be modified to fit inside the mask specified in Table 6.4.2.4.1-1 for normal conditions, prior to the calculation of EVM. The limiting mask shall be placed to minimize the change in equalizer coefficients in a sum of squares sense.

Table 6.4.2.4.1-1: Mask for EVM equalizer coefficients for Pi/2 BPSK, normal conditions

Figure 6.4.2.4.1-1: The limits for EVM equalizer spectral flatness with the maximum allowed variation

For Pi/2 BPSK modulation the UE shall be allowed to employ spectral shaping and the shaping filter shall be restricted so that the impulse response of the shaping filter itself shall meet

│ãt(t,0)│ ≥ │ãt(t, τ)│    ∀τ ≠ 0

20log10│ãt(t,τ)│< -15 dB    1< τ < M - 1,

where│ãt(t, τ)│=IDFT{│ãt(t,f)│ejφ (t,f)},   f  is the frequency of the M allocated subcarriers , ã(t,f) and φ(t,f) are the amplitude and phase response.

## 0 dB reference is defined as 20log10│ãt(t,0)│.

## 6.4.2.4.2Requirements for Pi/2 BPSK and QPSK modulation with powerBoosting-pi2BPSK-QPSK-Modified-r18 capability

These requirements apply when the IE powerBoostPi2BPSK-r18 or powerBoostQPSK-r18 is set to 1 for a UE supporting the capability of powerBoosting-pi2BPSK-QPSK-Modified-r18 and ΔPPowerBoost assumes a positive value. If the UE also indicates support for powerBoosting-pi2BPSK-QPSK-r18, and the allocation belongs to the enhanced power inner region, as defined in clause 6.2.2, these requirements do not apply, requirements in clause 6.4.2.4 apply instead.

The EVM equalizer coefficients across the allocated uplink block shall be modified to fit inside the mask specified in Table 6.4.2.4.2-1 for normal conditions, prior to the calculation of EVM. The limiting mask shall be placed to minimize the change in equalizer coefficients in a sum of squares sense.

Table 6.4.2.4.2-1: Mask for EVM equalizer coefficients forpowerBoosting-pi2BPSK-QPSK-Modified-r18 normal conditions

Figure 6.4.2.4.2-1: The limits for EVM equalizer spectral flatness referenced in table 6.4.2.4.2-1.

## 6.4.2.5Phase continuity requirements for DMRS bundling

For bands that UE indicates the support of DMRS bundling, when the UE is configured with DMRS bundling, the maximum allowable difference between the measured phase value in any slot p-1 and slot p, or slot 0 and any slot p for each antenna connector shall satisfy the requirements as listed in Table 6.4.2.5-1 for the measurement conditions defined in Table 6.4.2.5-2, within a measurement time window limited by the UE capability of maximum duration for DMRS bundling maxDurationDMRS-Bundling-r17, and defined for each frequency band separately. The phase value for each slot is measured as shown in Annex F.9. These requirements apply to PUCCH and PUSCH transmissions with DFT-s-OFDM and CP-OFDM waveforms.

Unless otherwise specified, pi/2 BPSK in this clause refers to both variants of pi/2 BPSK referenced in Table 6.2.2-1 and table 6.2.2-1a.

Table 6.4.2.5-1: Maximum allowable phase difference for DMRS bundling

The above requirements are applicable when all the following conditions are met within the measurement time window:

-RB allocation in terms of length and frequency position does not change, and intra-slot and inter-slot frequency hopping is not activated.

-Modulation order does not change.

-No network commanded TA takes effect.

-The TPMI precoder does not change.

-There is no change in UE transmission power level, and no change in the level of P-MPR applied by the UE.

-UE is not scheduled with uplink transmission of other physical channel/signal in-between the PUSCH or PUCCH transmissions.

-For TDD, no downlink slot(s) or downlink symbol(s) or flexible symbol(s) with/without DL monitoring occasion configured in-between the PUSCH or PUCCH transmissions.

Table 6.4.2.5-2: Measurement conditions for the maximum allowable phase difference

## 6.4ATransmit signal quality for CA

## 6.4A.1Frequency error for CA

## 6.4A.1.1Frequency error for intra-band contiguous CA

For intra-band contiguous carrier aggregation the UE modulated carrier frequencies per band shall be accurate to within ±0.1 PPM observed over a period of 1 ms of cumulated measurement intervals compared to the carrier frequency of primary component carrier received in the corresponding band

## 6.4A.1.2Frequency error for intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation the requirements in Section 6.4.1 applies per component carrier.

## 6.4A.1.3Frequency error for inter-band CA

For inter-band carrier aggregation with one uplink carrier assigned to one NR band, the frequency error requirements in subclause 6.4.1 apply.

For inter-band carrier aggregation with two uplink non-contiguous carrier assigned to one NR band, the frequency error requirements in subclause 6.4A.1.2 apply for those carriers.

For inter-band carrier aggregation with uplink assigned to two NR bands, the frequency error requirements defined in clause 6.4.1 shall apply on each component carrier with all component carriers active.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per operating band), the frequency error requirements specified in subclause 6.4.1 apply for the NR band supporting one component carrier, and for the NR band supporting two contiguous component carriers the requirements specified in subclause 6.4A.1.1 apply.

## 6.4A.1.4Void

## 6.4A.2Transmit modulation quality for CA

## 6.4A.2.1Transmit modulation quality for intra-band contiguous CA

## 6.4A.2.1.0General

For intra-band contiguous carrier aggregation, the requirements in clauses 6.4A.2.1.1, 6.4A.2.1.2 and 6.4A.2.1.3 applies.

The requirements in this clause apply with PCC and SCC in the UL configured and activated: PCC with PRB allocation and SCC without PRB allocation and without CSI reporting and SRS configured.

The Carrier leakage frequency is optionally indicated by the UE via IE UplinkTxDirectCurrentList , IE UplinkTxDirectCurrentTwoCarrierList-r16 for CA with two component carriers configured for uplink or IE UplinkTxDirectCurrentMoreCarrierList-r17 for CA of any configuration.

If the UE does not indicate DC location parameters, the carrier leakage measurement requirement in clauses 6.4A.2.2 and 6.4A.2.3 shall be waived and the UE’s UL signal left uncorrected for carrier leakage. Any requirement relaxation to accommodate the IQ image shall be omitted.

If the UE indicates carrier leakage frequency as 3300 or 3301 with IE UplinkTxDirectCurrentList or UplinkTxDirectCurrentTwoCarrierList-r16, or if the carrier leakage frequency is outside the activated UL component carriers, the carrier leakage measurement requirement in clauses 6.4A.2.2 and 6.4A.2.3 shall be waived and the UE’s UL signal left uncorrected for carrier leakage. Any requirement relaxation to accommodate the IQ image shall be omitted.

## 6.4A.2.1.1Error Vector Magnitude

For the intra-band contiguous carrier aggregation, the Error Vector Magnitude requirement should be defined for each component carrier. Requirements only apply with PRB allocation in one of the component carriers. Similar transmitter impairment removal procedures are applied for CA waveform before EVM calculation as is specified for non-CA waveform in sub-clause 6.4.2.1.

When a single component carrier is configured Table 6.4.2.1-1 apply.

The EVM requirements are according to Table 6.4A.2.1.1-1 if CA is configured in uplink with the parameters defined in Table 6.4.2.1-2.

Unless otherwise specified, pi/2 BPSK in this clause refers to both variants of pi/2 BPSK referenced in Table 6.2.2-1.

Table 6.4A.2.1.1-1: Minimum requirements for Error Vector Magnitude

## 6.4A.2.1.2In-band emissions

For intra-band contiguous carrier aggregation, the requirements in Table 6.4A.2.1.2-1 and 6.4A.2.1.2-2 apply within the aggregated transmission bandwidth configuration with both component carrier (s) active and one single contiguous PRB allocation of bandwidth  at the edge of the aggregated transmission bandwidth configuration.

The inband emission is defined as the interference falling into the non allocated resource blocks for all component carriers. The measurement method for the inband emissions in the component carrier with PRB allocation is specified in annex F.3. For a non allocated component carrier a spectral measurement is specified.

Table 6.4A.2.1.2-1: Minimum requirements for in-band emissions (allocated component carrier)

Table 6.4A.2.1.2-2: Minimum requirements for in-band emissions (not allocated component carrier)

## 6.4A.2.1.3Carrier leakage

Carrier leakage is an additive sinusoid waveform that is confined within the aggregated transmission bandwidth configuration. When only one uplink carrier is activated, the applicable carrier leakage requirement follows definition in clause 6.4.2. The measurement interval is one slot in the time domain.

The relative carrier leakage power is a power ratio of the additive sinusoid waveform and the modulated waveform. For intra-band contiguous CA, the relative carrier leakage power shall not exceed the values specified in Table 6.4A.2.1.3-1. The requirement does not apply if the indicated location of carrier leakage is outside the activated UL carriers.

Table 6.4A.2.1.3-1: Minimum requirements for Relative Carrier Leakage Power

## 6.4A.2.2Transmit modulation quality for intra-band non-contiguous CA

## 6.4A.2.2.0General

For intra-band non-contiguous carrier aggregation, the requirements in subclauses 6.4A.2.2.1, 6.4A.2.2.2 applies.

The requirements in this clause apply with PCC and SCC in the UL configured and activated: PCC with PRB allocation and SCC without PRB allocation and without CSI reporting and SRS configured.

Carrier leakage frequency is indicated by the UE with IE UplinkTxDirectCurrentMoreCarrierList-r17 or UplinkTxDirectCurrentTwoCarrierList-r16 or UplinkTxDirectCurrentList.

The carrier leakage measurement requirement in clause 6.4A.2.2.2 shall be waived and the UE’s UL signal left uncorrected for carrier leakage when one of the following qualifying conditions apply:

1.UE reports the parameter 3300 or 3301

2.UE doesn’t indicate the DC location parameters

Any requirement relaxation to accommodate the IQ image shall be omitted if the qualifying conditions above are present or if the IQ image frequency is outside the activated UL component carriers.

## 6.4A.2.2.1Error Vector Magnitude

For the intra-band non-contiguous carrier aggregation, the Error Vector Magnitude requirement should be defined for each component carrier. Requirements only apply with PRB allocation in one of the component carriers. Similar transmitter impairment removal procedures are applied for CA waveform before EVM calculation as is specified for non-CA waveform in sub-section 6.4.2.1.

When a single component carrier is configured Table 6.4.2.1-1 apply.

The EVM requirements are according to Table 6.4A.2.2.1-1 if CA is configured in uplink with the parameters defined in Table 6.4.2.1-2.

Unless otherwise specified, pi/2 BPSK in this clause refers to both variants of pi/2 BPSK referenced in Table 6.2.2-1.

Table 6.4A.2.2.1-1: Minimum requirements for Error Vector Magnitude

## 6.4A.2.2.2In-band emissions

For intra-band non-contiguous carrier aggregation the requirements for in-band emissions are defined for each component carrier. Requirements defined in clause 6.4A.2.1.2 only apply with PRB allocation in one of the component carriers.

When signalling for dualPA-Architecture IE is absent, carrier leakage or I/Q image may land inside the gap spectrum between 2 UL CCs.

For intra-band non-contiguous CA, the IQ image requirement is defined with the applicable frequencies based on symmetry with respect to the carrier leakage frequency, but excluding any allocated RBs.

## 6.4A.2.2.3Carrier leakage

The relative carrier leakage power is a power ratio of the additive sinusoid waveform and the modulated waveform. For intra-band non-contiguous CA,te relative carrier leakage power shall not exceed the values specified in Table 6.4A.2.1.3-1. The requirement does not apply if the indicated location of carrier leakage is outside the activated UL carriers.

## 6.4A.2.3Transmit modulation quality for inter-band CA

For inter-band carrier aggregation with one uplink carrier assigned to one NR band, the transmit modulation quality requirements in subclause 6.4.2 apply.

For inter-band downlink carrier aggregation with a single uplink carrier assigned to one NR band, DMRS bundling requirements in subclause 6.4.2.5 apply to the uplink carrier when the UE indicates support of maxDurationDMRS-Bundling-r17 for the NR band and is configured for DMRS bundling in the uplink carrier.

For inter-band carrier aggregation with two contiguous carriers assigned to one NR band, the transmit modulation quality requirements in subclause 6.4A.2.1 apply for those carriers.

For inter-band carrier aggregation with two uplink non-contiguous carrier assigned to one NR band, the transmit modulation quality requirements in subclause 6.4A.2.2 apply for those carriers.

For inter-band carrier aggregation with uplink assigned to two NR bands, the transmit modulation quality requirements shall apply on each component carrier as defined in clause 6.4.2 with all component carriers active: PCC with PRB allocation and SCC without PRB allocation and without CSI reporting and SRS configured. For DMRS bundling maxDurationDMRS-Bundling-r17, requirements for phase continuity in clause 6.4.2.5 apply when all of the following additional conditions are met:

-During DMRS bundling time window, concurrent transmissions scheduled/configured over multiple carriers [including any channels and/or signals] are not expected by UE

-Only one band is configured with DMRS bundling at a time

-All carriers are on same TAG

When the capability uplinkTxSwitchingPeriod is present, the UE indicates support of dmrs-BundlingPUCCH-RepPerBC-r17, and the UE is configured for uplink switching mechanisms specified in clause 6.1.6 of TS 38.214 [10], the phase continuity requirement in clause 6.4.2.5 for DMRS bundling is applicable under the following conditions:

-During the DMRS bundling time window, concurrent transmissions scheduled/configured over multiple carriers, including any channels and/or signals, are not expected by UE

-Only one carrier is configured with DMRS bundling at a time

-All carriers are on the same TAG

-DMRS bundling is not maintained across Tx switching period in the UL carrier configured with DMRS bundling

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per operating band): for the NR band supporting one component carrier the transmit modulation quality requirements specified in subclauses from 6.4.2.1 to 6.4.2.4 apply and for DMRS bundling maxDurationDMRS-Bundling-r17 the DMRS bundling requirements for inter-band carrier aggregation with uplink assigned to two NR bands apply. For the NR band supporting two contiguous component carriers the requirements specified in subclause 6.4A.2.1 apply.

## 6.4A.2.4Void

## 6.4BTransmit signal quality for NR-DC

For inter-band NR-DC with one uplink carrier assigned per NR band, the transmit signal quality for the corresponding inter-band CA configuration as specified in clause 6.4A applies with the exception of DMRS bundling maxDurationDMRS-Bundling-r17 requirements.

## 6.4CTransmit signal quality for SUL

For the UE which is configured with both NR UL and NR SUL carriers in a serving cell with active transmission either on the UL carrier(s) or SUL carrier, the transmit signal quality requirements specified in clause 6.4.2 and 6.4A.2 are applicable for the UL carrier(s) and the SUL carrier, respectively.

If the UE indicates that it is capable of DMRS bundling maxDurationDMRS-Bundling-r17 on the NR SUL band and UE is configured for DMRS bundling on SUL carrier or the UE indicates that it is capable of DMRS bundling maxDurationDMRS-Bundling-r17 on the NR UL band and UE is configured for DMRS bundling on NR UL carrier, the requirements for phase continuity in clause 6.4.2.5 apply for the corresponding SUL carrier or NR UL carrier, respectively. Only one band can be configured with DMRS bundling at a time.

## 6.4DTransmit signal quality for UL MIMO

## 6.4D.0General

For a UE supporting UL MIMO, the requirements in this section are defined per layer or as the sum of emissions from all UE antennas to account for the UL MIMO scheme.

Alternatively, when applicable, requirements may be verified per antenna connector using 2-layer UL MIMO transmission with codebook ofor 4-layer UL MIMO transmission with codebook of , and a configuration defined in Table 6.4D.0-1.

Table 6.4D.0-1: UL MIMO configuration for per connector measurements

## 6.4D.1Frequency error for UL MIMO

For UE(s) supporting UL MIMO, the basic measurement interval of modulated carrier frequency is 1 UL slot.  The mean value of basic measurements of UE modulated carrier frequency per layer shall be accurate to within ± 0.1 PPM observed over a period of 1 ms of cumulated measurement intervals compared to the carrier frequency received from the NR Node B.

## 6.4D.2Transmit modulation quality for UL MIMO

## 6.4D.2.0General

For UE supporting UL MIMO, the transmit modulation quality requirements are specified based on measurements made at each transmit antenna connector.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.4.2 apply when TxD is not indicated, and the requirements in clause 6.4G.2 apply when TxD is indicated.

The transmit modulation quality is specified in terms of:

-Error Vector Magnitude (EVM) for the allocated resource blocks (RBs)

-EVM equalizer spectrum flatness derived from the equalizer coefficients generated by the EVM measurement process

-Carrier leakage (caused by IQ offset)

-In-band emissions for the non-allocated RB

In case the parameter 3300 or 3301 is reported from UE via the parameter txDirectCurrentLocation in UplinkTxDirectCurrentList IE (as defined in TS 38.331 [7]), carrier leakage measurement requirement in clause 6.4D.2.2 and 6.4D.2.3 shall be waived, and the RF correction with regard to the carrier leakage and IQ image shall be omitted during the calculation of transmit modulation quality.

## 6.4D.2.1Error Vector Magnitude

For UE with two or four transmit antenna connectors in closed-loop spatial multiplexing scheme, the Error Vector Magnitude requirements specified in clause 6.4.2.1 apply per layer. The requirements shall be met with the UL MIMO configurations specified in Table 6.2D.1-2.

## 6.4D.2.2Carrier leakage

For UE with two or four transmit antenna connectors in closed-loop spatial multiplexing scheme, the Relative Carrier Leakage Power requirements specified in Table 6.4.2.2-1 which is defined in clause 6.4.2.2 apply per layer. The requirements shall be met with the UL MIMO configurations specified in Table 6.2D.1-2.

## 6.4D.2.3In-band emissions

For UE with two or four transmit antenna connectors in closed-loop spatial multiplexing scheme, the In-band Emission requirements specified in Table 6.4.2.3-1 which is defined in clause 6.4.2.3 apply at each transmit antenna connector. The requirements shall be met with the uplink MIMO configurations specified in Table 6.2D.1-2

## 6.4D.2.4EVM equalizer spectrum flatness for UL MIMO

For UE with two or four transmit antenna connectors in closed-loop spatial multiplexing scheme, the EVM Equalizer Spectrum Flatness requirements specified in clause 6.4.2.4 apply per layer. The requirements shall be met with the UL MIMO configurations specified in Table 6.2D.1-2

## 6.4D.3Time alignment error for UL MIMO

For UE(s) with multiple transmit antenna connectors supporting UL MIMO, this requirement applies to frame timing differences between transmissions on multiple transmit antenna connectors in the closed-loop spatial multiplexing scheme.

The time alignment error (TAE) is defined as the average frame timing difference between any two transmissions on different transmit antenna connectors.

For UE(s) with multiple transmit antenna connectors, the Time Alignment Error (TAE) shall not exceed 130 ns.

## 6.4D.4Requirements for coherent UL MIMO

For coherent UL MIMO, Table 6.4D.4-1 lists the maximum allowable difference between the measured relative power and phase errors between any two coherent ports out of the scheduled ports for UL transmission at their respective antenna connectors in any slot within the specified time window from the last transmitted SRS on the same antenna connectors, for the purpose of uplink transmission (codebook or non-codebook usage) and those measured at that last SRS. The requirements in Table 6.4D.4-1 apply when the UL transmission power at each antenna connector is larger than 0 dBm for SRS transmission and for the duration of time window.

Table 6.4D.4-1: Maximum allowable difference of relative phase and power errors in a given slot compared to those measured at last SRS transmitted

The above requirements when all the following conditions are met within the specified time window:

-UE is not signaled with a change in number of SRS ports in SRS-config, or a change in PUSCH-config

-UE remains in DRX active time (UE does not enter DRX OFF time)

-No measurement gap occurs

-No instance of SRS transmission with the usage antenna switching occurs

-Active BWP remains the same

-EN-DC and CA configuration is not changed for the UE (UE is not configured or de-configured with PSCell or SCell(s))

-When UE is not configured with uplink switching; or when UE is configured with uplink switching, and ‘fullCoherent’ codebook subset is supported in the corresponding carrier according to the capability uplinkTxSwitching-PUSCH-TransCoherence and/or uplinkTxSwitching2T2T-PUSCH-TransCoherence; or when UE is configured with uplink switching, ‘nonCoherent’ codebook subset is supported in the corresponding carrier according to the capability uplinkTxSwitching-PUSCH-TransCoherence and/or uplinkTxSwitching2T2T-PUSCH-TransCoherence, and uplink switching is not triggered by the switching mechanisms specified in sub-clause 6.1.6 of TS 38.214 [10] between last transmitted SRS and scheduled transmission.

## 6.4ETransmit signal quality for V2X

## 6.4E.1Frequency error for V2X

## 6.4E.1.1General

The UE modulated carrier frequency for NR V2X sidelink transmissions in Table 5.2E.1-1, shall be accurate to within ±0.1 PPM observed over a period of 1 ms compared to the absolute frequency in case of using GNSS synchronization source. The same requirements applied over a period of 1 ms compared to the carrier frequency received from the gNB or V2X synchronization reference UE in case of using the gNB or V2X synchronization reference UE sidelink synchronization signals.

For NR V2X UE supporting SL MIMO or Tx Diversity, the UE modulated carrier frequency at each transmit antenna connector shall be accurate to within ±0.1 PPM observed over a period of 1 ms in case of using GNSS synchronization source. The same requirements apply over a period of 1 ms compared to the relative frequency in case of using the NR gNode B or V2X synchronization reference UE sidelink synchronization signals.

If the UE transmits on one antenna connector at a time, the requirements for single carrier shall apply to the active antenna connector.

## 6.4E.1.1AFrequency error for sidelink CA

For SL intra-band contiguous/non-contiguous CA, ±0.1 PPM observed over a period of 1 ms will be applied per CC compared to the absolute frequency in case of using GNSS synchronization source. The same requirements will be applied to all SL synchronous reference sources (the gNB or V2X synchronization reference UE).

## 6.4E.1.2Frequency error for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 6.4.1 shall apply for the uplink in licensed band and the requirements specified in clause 6.4E.1.1 shall apply for the sidelink in licensed band or Band n47.

For the intra-band concurrent NR V2X operation, the requirements specified in clause 6.4.1 shall apply for the uplink in licensed band and the requirements specified in clause 6.4E.1 shall apply for the sidelink in licensed band.

## 6.4E.1FFrequency error for Sidelink Unlicensed

The requirements for frequency error in 6.4E.1 apply for SL-U operation.

## 6.4E.1F.1Frequency error for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the requirements specified in clause 6.4.1 shall apply for NR Uu operation in licensed band and the requirements specified in clause 6.4E.1 shall apply for NR sidelink operation in unlicensed band.

## 6.4E.2Transmit modulation quality for V2X

## 6.4E.2.1General

The transmit modulation quality requirements in this clause apply to V2X sidelink transmissions.

For NR V2X UE supporting SL MIMO or Tx Diversity, the transmit modulation quality requirements for single carrier shall apply to each transmit antenna connector.

If V2X UE transmits on one antenna connector at a time, the requirements specified for single carrier apply to the active antenna connector.

## 6.4E.2.2Error Vector Magnitude for V2X

For V2X sidelink physical channels PSCCH and PSSCH, the Error Vector Magnitude requirements shall be as specified for PUSCH in Table 6.4.2.1-1 except pi/2-BPSK for NR V2X operating bands in Table 5.2E.1-1. When sidelink transmissions are shortened due to transmission gap of one symbol at the end of the slot, the EVM measurement interval is reduced by one symbol, accordingly.

## 6.4E.2.2AError Vector Magnitude for sidelink CA

For SL intra-band contiguous/non-contiguous CA, the EVM requirement as specified in clause 6.4E.2.2 shall be applied per component carrier.

## 6.4E.2.3Carrier leakage for V2X

Carrier leakage of NR V2X sidelink transmission, the requirements for NR PUSCH in Table 6.4.2.2-1 shall be applied.

## 6.4E.2.3ACarrier leakage for sidelink CA

For SL intra-band contiguous/non-contiguous CA, the carrier leakage requirement as specified in clause 6.4E.2.3 shall be applied per component carrier when only one SL transmission carrier is activated in a time.

## 6.4E.2.4In-band emissions for V2X

For V2X sidelink physical channels PSCCH, PSSCH and PSBCH, the In-band emissions requirements shall be as specified for PUSCH in subclause 6.4.2.3 for the corresponding modulation and transmission bandwidth. When V2X transmissions are shortened due to transmission gap of one symbol at the end of the subframe, the In-band emissions measurement interval is reduced by one symbol, accordingly.

## 6.4E.2.4AIn-band emissions for sidelink CA

For SL intra-band contiguous/non-contiguous CA, the In-band emission requirement as specified in clause 6.4E.2.4 shall be applied to the SL aggregated transmission bandwidth. This is same as NR intra-band CA UE.

## 6.4E.2.5EVM equalizer spectrum flatness for V2X

For V2X sidelink physical channels PSCCH, PSSCH and PSBCH, the EVM equalizer spectrum flatness requirements shall be as specified for PUSCH in clause 6.4.2.4 for the corresponding modulation and transmission bandwidth.

## 6.4E.2.6Transmit modulation quality for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 6.4.2 shall apply for the uplink in licensed band and the requirements specified in clause 6.4E.2.1 through 6.4E.2.5 shall apply for the sidelink in licensed band or Band n47.

For the intra-band concurrent NR V2X operation, the requirements specified in clause 6.4.2 shall apply for the uplink in licensed band and the requirements specified in clause 6.4E.2 shall apply for the sidelink in licensed band.

## 6.4E.2FTransmit modulation quality for Sidelink Unlicensed

## 6.4E.2F.0General

Transmit modulation quality defines the modulation quality for expected in-channel RF transmissions from the UE. The transmit modulation quality is specified in terms of:

-Error Vector Magnitude (EVM) for the allocated resource blocks (RBs)

-EVM equalizer spectrum flatness derived from the equalizer coefficients generated by the EVM measurement process

-Carrier leakage

-In-band emissions for the non-allocated RB

All the parameters defined in clause 6.4.2 are defined using the measurement methodology specified in Annex F.

In case the parameter 3300 or 3301 is reported from UE via txDirectCurrentLocation IE (as defined in TS 38.331 [7]), carrier leakage measurement requirement in clause 6.4E.2F.2 and 6.4E.2F.3 shall be waived, and the RF correction with regard to the carrier leakage and IQ image shall be omitted during the calculation of transmit modulation quality.

## 6.4E.2F.1Error Vector Magnitude

The requirements for Error Vector Magnitude in clause 6.4E.2.2 apply for SL-U operation.

## 6.4E.2F.2Carrier leakage

The requirements for carrier leakage in clause 6.4.2.2 apply for SL-U operation.

## 6.4E.2F.3In-band emissions

The requirements for in-band emission in clause 6.4F.2.3 apply for SL-U operation.

## 6.4E.2F.4EVM equalizer spectrum flatness

The requirements for EVM equalizer spectrum flatness in clause 6.4.2.4 apply for SL-U operation.

## 6.4E.2F.5Transmit modulation quality for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the requirements specified in clause 6.4.2 shall apply for the uplink in licensed band and the requirements specified in clause 6.4E.2F.0 through 6.4E.2F.4 shall apply for NR sidelink operation in unlicensed band.

## 6.4FTransmit signal quality for shared spectrum channel access

## 6.4F.1Frequency error

The requirements for frequency error in clause 6.4.1 apply.

## 6.4F.2Transmit modulation quality

## 6.4F.2.0General

Transmit modulation quality defines the modulation quality for expected in-channel RF transmissions from the UE. The transmit modulation quality is specified in terms of:

-Error Vector Magnitude (EVM) for the allocated resource blocks (RBs)

-EVM equalizer spectrum flatness derived from the equalizer coefficients generated by the EVM measurement process

-Carrier leakage

-In-band emissions for the non-allocated RB

All the parameters defined in clause 6.4.2 are defined using the measurement methodology specified in Annex F.

In case the parameter 3300 or 3301 is reported from UE via txDirectCurrentLocation IE (as defined in TS 38.331 [7]), carrier leakage measurement requirement in clause 6.4F.2.2 and 6.4F.2.3 shall be waived, and the RF correction with regard to the carrier leakage and IQ image shall be omitted during the calculation of transmit modulation quality.

## 6.4F.2.1Error Vector Magnitude

The requirements for Error Vector Magnitude in clause 6.4.2.1 apply.

## 6.4F.2.2Carrier leakage

The requirements for carrier leakage in clause 6.4.2.2 apply.

## 6.4F.2.3In-band emissions

The in-band emission is defined as the average emission across 12 sub-carriers and as a function of the RB offset from the edge of the allocated UL transmission bandwidth. The in-band emission is measured as the ratio of the UE output power in a non–allocated RB to the UE output power in an allocated RB.

The basic in-band emissions measurement interval is defined over one slot in the time domain; however, the minimum requirement applies when the in-band emission measurement is averaged over 10 sub-frames. When the PUSCH or PUCCH transmission slot is shortened, the in-band emissions measurement interval is reduced by one or more symbols, accordingly.  The requirement applies for power class 5 UE for 20 MHz channel bandwidth and 15 kHz SCS,

Instead of the general requirement in clause 6.4.2.3, the average of the basic in-band emission measurement over 10 sub-frames shall not exceed the values specified in Table 6.4F.2.3-1.

Table 6.4F.2.3-1: Minimum requirements for in-band emissions

## 6.4F.2.4EVM equalizer spectrum flatness

The requirements for EVM equalizer spectrum flatness in clause 6.4.2.4 apply.

## 6.4F.2ATransmit modulation quality for CA

## 6.4F.2A.1Transmit modulation quality for inter-band CA

For inter-band carrier aggregation with uplink assigned to two bands and including one of the bands listed in Table 6.2F.1-1, the transmit modulation quality requirements shall apply on the NR carrier as defined in clause 6.4.2 and on the carrier operating with shared spectrum access as defined in clause 6.4F.2.  The requirements apply with all component carrier active: PCC with PRB allocation and SCC without PRB allocation and without CSI reporting and SRS configured.

## 6.4GTransmit signal quality for Tx Diversity

## 6.4G.1Frequency error for Tx Diversity

For UE(s) supporting Tx diversity, the basic measurement interval of modulated carrier frequency is 1 UL slot.  The mean value of basic measurements of UE modulated carrier frequency at each transmit antenna connector shall be accurate to within ± 0.1 PPM observed over a period of 1 ms of cumulated measurement intervals compared to the carrier frequency received from the NR Node B.

## 6.4G.2Transmit modulation quality for Tx Diversity

## 6.4G.2.0General

For UE supporting Tx diversity, the transmit modulation quality requirements are specified based on measurements made at each transmit antenna connector. The transmit modulation quality is specified in terms of:

-Error Vector Magnitude (EVM) for the allocated resource blocks (RBs)

-EVM equalizer spectrum flatness derived from the equalizer coefficients generated by the EVM measurement process

-Carrier leakage (caused by IQ offset)

-In-band emissions for the non-allocated RB

In case the parameter 3300 or 3301 is reported from UE via txDirectCurrentLocation IE (as defined in TS 38.331 [7]), carrier leakage measurement requirement in clause 6.4.2.2 and 6.4.2.3 shall be waived, and the RF correction with regard to the carrier leakage and IQ image shall be omitted during the calculation of transmit modulation quality.

6.4G.2.1Error Vector Magnitude

For UE supporting Tx diversity, the Error Vector Magnitude requirements specified in clause 6.4.2.1. The total EVM requirement is derived based on the measurement at each antenna connector according to Annex F.8.

6.4G.2.2Carrier leakage

For UE supporting Tx diversity, the Relative Carrier Leakage Power requirements specified in Table 6.4.2.2-1 which is defined in clause 6.4.2.2 apply at each transmit antenna connector.

6.4G.2.3In-band emissions

For UE supporting Tx diversity, the In-band Emission requirements specified in Table 6.4.2.3-1 which is defined in clause 6.4.2.3 apply at each transmit antenna connector.

6.4G.2.4EVM equalizer spectrum flatness for Tx Diversity

For UE supporting Tx diversity, the EVM Equalizer Spectrum Flatness requirements specified in Table 6.4.2.4-1 and Table 6.4.2.4-2 which are defined in clause 6.4.2.4. The composite EVM equalizer EC(f) is defined as

EC(f)=n=1kPn*ECn(f)n=1kPn

where

=2, 4k

ECn(f) represents equalizer coefficient for each antenna connector,  ，f is the allocated subcarriers within the transmission bandwidth ((|F|=12*);

denotes the linear power measured at the antenna connector n.Pn

## 6.4HTransmit signal quality for CA with UL MIMO

## 6.4H.1Transmit signal quality for intra-band UL contiguous CA with UL MIMO

## 6.4H.1.1Frequency error for intra-band UL contiguous CA with UL MIMO

For UE supporting intra-band UL contiguous CA and UL MIMO, the basic measurement interval of modulated carrier frequency is 1 UL slot.  The mean value of basic measurements of UE modulated carrier frequency at each transmit antenna connector on each CC shall be accurate to within ± 0.1 PPM observed over a period of 1 ms of cumulated measurement intervals compared to the carrier frequency of primary component carrier received from the NR Node B.

## 6.4H.1.2Transmit modulation quality for intra-band UL contiguous CA with UL MIMO

## 6.4H.1.2.0General

For UE supporting intra-band UL contiguous CA and UL MIMO, the transmit modulation quality requirements are specified based on measurements made at each transmit antenna connector on each CC.

The requirements in this clause apply with PCC and SCC in the UL configured and activated: PCC with PRB allocation and SCC without PRB allocation and without CSI reporting and SRS configured.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.4A.2.1 apply.

The transmit modulation quality requirements listed below shall be met with UL MIMO configurations specified in Table 6.2D.1-2.

For all Transmit modulation quality requirements the Carrier leakage frequency is indicted by the UE with IE UplinkTxDirectCurrentTwoCarrierList-r16 or UplinkTxDirectCurrentMoreCarrierList-r17 or UplinkTxDirectCurrentList.

The carrier leakage measurement requirement in clauses 6.4H.1.2.2 and 6.4H.1.2.3 shall be waived and the UE’s UL signal left uncorrected for carrier leakage when one of the following qualifying conditions apply:

1.UE reports the parameter 3300 or 3301

2.UE doesn’t indicate the DC location parameters

Any requirement relaxation to accommodate the IQ image shall be omitted if the qualifying conditions above are present or if the IQ image frequency is outside the activated UL component carriers.

## 6.4H.1.2.1Error Vector Magnitude

For intra-band UL contiguous CA and UE with two transmit antenna connectors in closed-loop spatial multiplexing scheme, the Error Vector Magnitude requirements specified in clause 6.4A.2.1.1 apply per layer.

## 6.4H.1.2.2Carrier leakage

For UE supporting intra-band UL contiguous CA and UL MIMO, the relative carrier leakage power requirements specified in clause 6.4A.2.1.3 apply at each transmit antenna connector.

## 6.4H.1.2.3In-band emissions

For UE supporting intra-band UL contiguous CA and UL MIMO, the In-band emission requirements specified in clause 6.4A.2.1.2 apply at each transmit antenna connector.

## 6.4H.1.3Time alignment error for intra-band UL contiguous CA with UL MIMO

For intra-band UL contiguous CA and UE(s) with multiple transmit antenna connectors supporting UL MIMO, this requirement applies as specified in clause 6.4D.3: The time alignment error (TAE) is defined as the average frame timing difference between any two transmissions on different transmit antenna connectors for each CC. For UE(s) with multiple transmit antenna connectors, the Time Alignment Error (TAE) shall not exceed 130 ns.

## 6.4H.1.4Coherent UL MIMO requirement for intra-band UL contiguous CA with UL MIMO

For UE supporting intra-band UL contiguous CA and UL MIMO, the coherent UL MIMO requirement are specified on each CC as in clause 6.4D.4.

## 6.4H.2Void

## 6.4H.3Transmit signal quality for inter-band UL CA with UL MIMO

## 6.4H.3.1Frequency error for inter-band UL CA with UL MIMO

For inter-band UL CA with UL MIMO in one of the two frequency bands, the frequency error requirement defined in clause 6.4.1 shall apply on the component carrier without UL MIMO and the frequency error requirement defined in clause 6.4D.1 shall apply on the component carrier configured with UL MIMO with all component carriers active.

## 6.4H.3.2Transmit modulation quality for inter-band UL CA with UL MIMO

For inter-band UL CA with UL MIMO in one of the two frequency bands, the transmit modulation quality requirements defined in clause 6.4.2 shall apply on the component carrier without UL MIMO and the transmit modulation quality requirements defined in clause 6.4D.2 shall apply on the component carrier configured with UL MIMO with all component carriers active: PCC with PRB allocation and SCC without PRB allocation and without CSI reporting and SRS configured.

## 6.4I(Reserved)

## 6.4JTransmit signal quality for ATG

## 6.4J.0Reserved

## 6.4J.0DGeneral

For a ATG UE supporting UL MIMO, the requirements in this section are defined per layer or as the sum of emissions from all UE antennas to account for the UL MIMO scheme.

Alternatively, when applicable, requirements may be verified per layer using 2-layer UL MIMO transmission with codebook of, and a configuration defined in Table 6.4J.0D-1.

Table 6.4J.0D-1: UL MIMO configuration for per connector measurements

## 6.4J.1Frequency error for ATG

The ATG UE basic measurement interval of modulated carrier frequency is 1 UL slot. The ATG UE pre-compensates the uplink modulated carrier frequency by the estimated Doppler shift. The mean value of basic measurements of ATG UE modulated carrier frequency per layer at each transmit antenna connector for UE with omni-directional antenna(s) or at each transceiver array boundary (TAB) connector for UE with antenna array shall be accurate to within ± 0.1 PPM observed over a period of 1 ms of cumulated measurement intervals compared to ideally pre-compensated reference uplink carrier frequency.

UE [shall] rely on the ATG BS location broadcasted by the SIB22 in TS 38.331 [7].

NOTE 1:the ideally pre-compensated reference uplink carrier frequency consists of the UL carrier frequency signalled to the UE by ATG BS and UL precompensated doppler frequency shift.

## 6.4J.2Transmit modulation quality for ATG

The requirements for transmit modulation quality defined in clause 6.4.2 shall apply for ATG UE at each transmit antenna connector for UE with omni-directional antenna(s) or at each transceiver array boundary (TAB) connector for UE with antenna array, except for the phase continuity requirements for DMRS bundling in 6.4.2.5. The requirements for 256QAM modulation are only applicable to ATG UE indicating support of 256QAM.

## 6.4J.2DTransmit modulation quality for ATG UL MIMO

## 6.4J.2D.0General

For ATG UE supporting UL MIMO, general description for transmit modulation quality as specified in clause 6.4D.2.0 apply.

## 6.4J.2D.1Error Vector Magnitude for ATG UL MIMO

For ATG UE with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer) in closed-loop spatial multiplexing scheme, the Error Vector Magnitude requirements specified in clause 6.4.2.1 apply per layer. The requirements shall be met with the UL MIMO configurations specified in Table 6.2J.1D-1.

## 6.4J.2D.2Carrier leakage for ATG UL MIMO

For ATG UE with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer) in closed-loop spatial multiplexing scheme, the Relative Carrier Leakage Power requirements specified in Table 6.4.2.2-1 which is defined in clause 6.4.2.2 apply per layer. The requirements shall be met with the UL MIMO configurations specified in Table 6.2J.1D-1.

## 6.4J.2D.3In-band emissions for ATG UL MIMO

For ATG UE with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer) in closed-loop spatial multiplexing scheme, the In-band Emission requirements specified in Table 6.4.2.3-1 which is defined in clause 6.4.2.3 apply at each transmit antenna connector or each TAB connector. The requirements shall be met with the UL MIMO configurations specified in Table 6.2J.1D-1.

## 6.4J.2D.4EVM equalizer spectrum flatness for ATG UL MIMO

For ATG UE with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer) in closed-loop spatial multiplexing scheme, the EVM Equalizer Spectrum Flatness requirements specified in clause 6.4.2.4 apply per layer. The requirements shall be met with the UL MIMO configurations specified in Table 6.2J.1D-1.

## 6.4J.3DTime alignment error for ATG

## 6.4J.3D.1Time alignment error for ATG UL MIMO

For ATG UE with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer) supporting UL MIMO, this requirement applies to frame timing differences between transmissions on two transmit antenna connectors or TAB connectors. The time alignment error (TAE) is defined as the average frame timing difference between any two transmissions on different transmit antenna connectors or TAB connectors belonging to different groups (each of which supporting one layer).

For ATG UE with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer), the Time Alignment Error (TAE) shall not exceed 130 ns.

## 6.4J.3DRequirement for ATG coherent UL MIMO

For ATG UE with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer), the requirements for coherent UL MIMO as specified in clause 6.4D.4 apply.

## 6.4K(Reserved)

## 6.4LTransmit signal quality for CA with Tx Diversity

## 6.4L.1Void

## 6.4L.2Void

## 6.4L.3Transmit signal quality for inter-band UL CA with Tx Diversity

## 6.4L.3.1Frequency error for inter-band UL CA with Tx Diversity

For inter-band UL CA with Tx Diversity in one of the two frequency bands, the frequency error requirement defined in clause 6.4.1 shall apply on the component carrier without Tx Diversity and the frequency error requirement defined in clause 6.4G.1 shall apply on the component carrier configured with Tx Diversity with all component carriers active.

## 6.4L.3.2Transmit modulation quality for inter-band UL CA with Tx Diversity

For inter-band UL CA with Tx Diversity in one of the two frequency bands, the transmit modulation quality requirements defined in clause 6.4.2 shall apply on the component carrier without Tx Diversity and the transmit modulation quality requirements defined in clause 6.4G.2 shall apply on the component carrier configured with Tx Diversity with all component carriers active: PCC with PRB allocation and SCC without PRB allocation and without CSI reporting and SRS configured.

## 6.5Output RF spectrum emissions

## 6.5.1Occupied bandwidth

Occupied bandwidth is defined as the bandwidth containing 99 % of the total integrated mean power of the transmitted spectrum on the assigned channel. The occupied bandwidth for all transmission bandwidth configurations (Resources Blocks) shall be less than the channel bandwidth specified in Table 6.5.1-1.

Table 6.5.1-1: Occupied channel bandwidth

## 6.5.2Out of band emission

## 6.5.2.1General

The Out of band emissions are unwanted emissions immediately outside the assigned channel bandwidth resulting from the modulation process and non-linearity in the transmitter but excluding spurious emissions. This out of band emission limit is specified in terms of a spectrum emission mask and an adjacent channel leakage power ratio.

To improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.5.2.2Spectrum emission mask

The spectrum emission mask of the UE applies to frequencies (ΔfOOB) starting from the  edge of the assigned NR channel bandwidth. For frequencies offset greater than ΔfOOB, the spurious requirements in clause 6.5.3 are applicable.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

The power of any UE emission shall not exceed the levels specified in Table 6.5.2.2-1 for the specified channel bandwidth.

Table 6.5.2.2-1: General NR spectrum emission mask

If the UE supports mpr-SingleCC-SingleValue-r19 or mpr-SingleCC-MultipleValue-r19 and is configured with the IE mprReductionExtensionRatio-r19, and the conditions for which corresponding MPR reduction apply as defined in Clause 6.2.2, then the ΔfOOB shall be offset down by Rext_low* BWChannel from the lower edge of the assigned NR channel bandwidth and offset up by Rext_high* BWChannel from the higher edge of the assigned NR channel bandwidth.

## 6.5.2.3Additional spectrum emission mask

## 6.5.2.3.1Requirements for network signalling value "NS_35"

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "NS_35" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.2.3.1-1.

Table 6.5.2.3.1-1: Additional requirements for "NS_35"

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.5.2.3.2Requirements for network signalling value "NS_04"

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message. The additional spectrum emission requirements in NS_04 are based on FCC rule 47 CFR 27.53(m)(4).

The n41 SEM transition point from -13 dBm/MHz to -25 dBm/MHz is based on the emission bandwidth. The emission bandwidth is defined as the width of the signal between two points, one below the carrier center frequency and one above the carrier center frequency, outside of which all emissions are attenuated at least 26 dB below the transmitter power based on FCC rule 47 CFR 27.53(m)(6).  Since the 26-dB emission bandwidth is implementation dependent, the maximum transmission bandwidth of the channel bandwidth in MHz (for CP-OFDM, this bandwidth equals NRB * SCS * 12 / 1,000, and for DFT-S-OFDM, this bandwidth equals the maximum applicable LCRB * SCS * 12 / 1,000) contained within the 26 dB emission bandwidth is used for determining the applicable SEM indicated by NS_04 as specified in Table 6.5.2.3.2-1 and Table 6.5.2.3.2-2.

Table 6.5.2.3.2-1: transmission bandwidth determining the NS_04 SEM for CP-OFDM

Table 6.5.2.3.2-2: transmission bandwidth determining the NS_04 SEM for DFT-S-OFDM

When "NS_04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.2.3.2-3.

Table 6.5.2.3.2-3: n41 and n90 SEM with "NS_04"

## 6.5.2.3.3Requirements for network signalling values "NS_03" and “NS_03U”

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "NS_03" or “NS_03U” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.2.3.3-1.

Table 6.5.2.3.3-1: Additional requirements for "NS_03" and “NS_03U”

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

Table 6.5.2.3.3-2: Void

## 6.5.2.3.4Requirements for network signalling value "NS_06" or “NS_07”

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "NS_06" or "NS_07" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.2.3.4-1.

Table 6.5.2.3.4-1: Additional requirements for "NS_06" or "NS_07"

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.5.2.3.5Void

## 6.5.2.3.6Void

## 6.5.2.3.7Void

## 6.5.2.3.8Requirements for network signalling value "NS_27"

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "NS_27" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.2.3.8-1.

Table 6.5.2.3.8-1: Additional requirements for "NS_27"

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.5.2.3.9Requirements for network signalling value "NS_21"

Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "NS_21" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.2.3.9-1.

Table 6.5.2.3.9-1: Additional requirements for "NS_21"

NOTE 1:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

NOTE 2:For ΔfOOB = ±0-1MHz, a resolution bandwidth of as close as possible to, without being less than 1% of the channel bandwidth, shall be employed provided that the measured power is integrated over the full required measurement bandwidth of 1 MHz.

## 6.5.2.4Adjacent channel leakage ratio

Adjacent Channel Leakage power Ratio (ACLR) is the ratio of the filtered mean power centred on the assigned channel frequency to the filtered mean power centred on an adjacent channel frequency.

To improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.5.2.4.1NR ACLR

NR Adjacent Channel Leakage power Ratio (NRACLR) is the ratio of the filtered mean power centred on the assigned NR channel frequency to the filtered mean power centred on an adjacent NR channel frequency at nominal channel spacing.

If the UE supports mpr-SingleCC-SingleValue-r19 or mpr-SingleCC-MultipleValue-r19, and is configured with the IE mprReductionExtensionRatio-r19, and the conditions for which corresponding MPR reduction apply as defined in clause 6.2.2, then

-The channel frequency of the lower adjacent channel shall be further offset down by Rext_low* BWChannel from the assigned NR channel bandwidth compared to the nominal channel spacing

-The channel frequency of the upper adjacent channel shall be further offset up by Rext_high* BWChannel from the assigned NR channel bandwidth compared to the nominal channel spacing

-The NR ACLR measurement bandwidth is as specified in Table 6.5.2.4.1-1 corresponding to the assigned NR channel bandwidth.

The assigned NR channel power and adjacent NR channel power are measured with rectangular filters with measurement bandwidths specified in Table 6.5.2.4.1-1.

If the measured adjacent channel power is greater than –50 dBm then the NRACLR shall be higher than the value specified in Table 6.5.2.4.1-2.

When the IE powerBoostPi2BPSK-r18 or powerBoostQPSK-r18 is set to 1 for a UE supporting the capability of powerBoosting-pi2BPSK-QPSK-r18 or capability of powerBoosting-pi2BPSK-QPSK-Modified-r18, for power class 2 UE, the ACLR requirement of PC2 applies. For power class 3 UE, the ACLR requirement of PC3 applies.

Table 6.5.2.4.1-1: NR ACLR measurement bandwidth

Table 6.5.2.4.1-2: NR ACLR requirement

Table 6.5.2.4.1-3: Band specific NR ACLR requirement

## 6.5.2.4.2UTRA ACLR

UTRA adjacent channel leakage power ratio (UTRAACLR) is the ratio of the filtered mean power centred on the assigned NR channel frequency to the filtered mean power centred on an adjacent(s) UTRA channel frequency.

UTRAACLR is specified for the first adjacent UTRA channel (UTRAACLR1) which center frequency is ± 2.5 MHz from NR channel edge and for the 2nd adjacent UTRA channel (UTRAACLR2) which center frequency is ± 7.5 MHz from NR channel edge.

The UTRA channel power is measured with a RRC filter with roll-off factor = 0.22 and bandwidth of 3.84 MHz. The assigned NR channel power is measured with a rectangular filter with measurement bandwidth specified in Table 6.5.2.4.1-1.

If the measured adjacent channel power is greater than – 50 dBm then the UTRAACLR1 and UTRAACLR2 shall be higher than the value specified in Table 6.5.2.4.2-1.

Table 6.5.2.4.2-1: UTRA ACLR requirement

UTRA ACLR requirement is applicable when the network signalling value NS_03U, NS_05U, NS_43U or NS_100 is signalled by the network in the field additionalSpectrumEmission.

## 6.5.3Spurious emissions

## 6.5.3.0General

Spurious emissions are emissions which are caused by unwanted transmitter effects such as harmonics emission, parasitic emissions, intermodulation products and frequency conversion products, but exclude out of band emissions unless otherwise stated. The spurious emission limits are specified in terms of general requirements in line with SM.329 [9] and NR operating band requirement to address UE co-existence.

To improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

## 6.5.3.1General spurious emissions

Unless otherwise stated, the spurious emission limits apply for the frequency ranges that are more than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth. The spurious emission limits in Table 6.5.3.1-2 apply for all transmitter band configurations (NRB) and channel bandwidths.

Table 6.5.3.1-1: Boundary between NR out of band and general spurious emission domain

Table 6.5.3.1-2: Requirement for general spurious emissions limits

If the UE supports mpr-SingleCC-SingleValue-r19 or mpr-SingleCC-MultipleValue-r19, and is configured with the IE mprReductionExtensionRatio-r19, and the conditions for which corresponding MPR reduction apply as defined in clause 6.2.2, then the FOOB (MHz) in Table 6.5.3.1-1 shall be offset down by Rext_low* BWChannel from the lower edge of the channel bandwidth and shall be offset up by Rext_high* BWChannel from the higher edge of the channel bandwidth.

## 6.5.3.2Spurious emissions for UE co-existence

This clause specifies the requirements for NR bands for coexistence with protected bands. Unless otherwise stated, the spurious emission for UE co-existence apply for the frequency ranges that are more than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.2-1: Requirements for spurious emissions for UE co-existence

NOTE:To simplify Table 6.5.3.2-1, E-UTRA band numbers are listed for bands which are specified only for E-UTRA operation or both E-UTRA and NR operation. NR band numbers are listed for bands which are specified only for NR operation.

## 6.5.3.3Additional spurious emissions

These requirements are specified in terms of an additional spectrum emission requirement. Additional spurious emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

## 6.5.3.3.1Requirement for network signalling value "NS_04"

When "NS_04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.1-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.1-1: Additional requirements for "NS_04"

## 6.5.3.3.2Requirement for network signalling value "NS_17"

When "NS_17" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.2-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.2-1: Additional requirements for "NS_17"

## 6.5.3.3.3Requirement for network signalling value "NS_18"

When "NS_18" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.3-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.3-1: Additional requirements for "NS_18"

## 6.5.3.3.4Requirement for network signalling values "NS_05" and “NS_05U”

When "NS_05" or “NS_05U” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.4-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.4-1: Additional requirements for "NS_05" and “NS_05U”

## 6.5.3.3.5Requirement for network signalling values "NS_43" and “NS_43U”

When "NS_43" or “NS_43U” is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.5-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.5-1: Additional requirements for "NS_43" and “NS_43U”

## 6.5.3.3.6Requirement for network signalling value "NS_37"

When "NS_37" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.6-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.6-1: Additional requirement for "NS_37"

## 6.5.3.3.7Requirement for network signalling value "NS_38"

When "NS_38" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.7-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.7-1: Additional requirements for NR channels assigned within 1430-1452MHz for "NS_38"

## 6.5.3.3.8Requirement for network signalling value "NS_39"

When "NS_39" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.8-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.8-1: Additional requirements for "NS_39"

## 6.5.3.3.9Requirement for network signalling value "NS_40"

When "NS_40" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.9-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.9-1: Additional requirements for NR channels assignedwithin 1427-1432MHz for "NS_40"

## 6.5.3.3.10Requirement for network signalling value "NS_41"

When "NS_41" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.10-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.10-1: Additional requirements for NR channels assigned within 1432-1517 MHz for "NS_41"

## 6.5.3.3.11Requirement for network signalling value "NS_42"

When "NS_42" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.11-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.11-1: Additional requirements for NR channels assigned within 1432-1517 MHz for "NS_42"

## 6.5.3.3.12Requirement for network signalling value "NS_21"

When "NS_21" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.12-1. These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.12-1: Additional requirements for "NS_21"

## 6.5.3.3.13Requirement for network signalling value "NS_24"

When "NS_24" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.13-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.13-1: Additional requirements for "NS_24"

## 6.5.3.3.14Requirement for network signalling value "NS_27"

When "NS_27" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.14-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.14-1: Additional requirements for "NS_27"

## 6.5.3.3.15Requirement for network signalling value "NS_47"

When "NS_47" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.15-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.15-1: Additional requirements for NR channels assigned within 2545 - 2575 MHz for "NS_47"

## 6.5.3.3.16Requirement for network signalling value "NS_50"

When "NS_50" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.16-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.16-1: Additional requirements for "NS_50"

## 6.5.3.3.17Requirement for network signalling value "NS_12"

When "NS_12" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.17-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.17-1: Additional requirements "NS_12"

## 6.5.3.3.18Requirement for network signalling value "NS_13"

When "NS_13" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.18-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.18-1: Additional requirements "NS_13"

## 6.5.3.3.19Requirement for network signalling value "NS_14"

When "NS_14" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.19-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.19-1: Additional requirements "NS_14"

## 6.5.3.3.20Requirement for network signalling value "NS_15"

When "NS_15" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.20-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.20-1: Additional requirements "NS_15"

## 6.5.3.3.21Requirement for network signalling value "NS_45"

When "NS_45" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.21-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.21-1: Additional requirements "NS_45"

## 6.5.3.3.22Requirement for network signalling values "NS_48" and "NS_51"

When "NS_48" or "NS_51" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.22-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.22-1: Additional requirements for "NS_48" and "NS_51"

## 6.5.3.3.23Requirement for network signalling value "NS_49"

When "NS_49" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.23-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.23-1: Additional requirements for "NS_49"

## 6.5.3.3.24Requirement for network signalling value "NS_44"

When "NS_44" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.24-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.24-1: Additional requirements for "NS_44"

## 6.5.3.3.25Requirement for network signalling value "NS_46"

When "NS_46" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.25-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.25-1: Additional requirements for “NS_46”

## 6.5.3.3.26Requirement for network signalling value "NS_07"

When "NS_07" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.26-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.26-1: Additional requirements for "NS_07"

## 6.5.3.3.27Requirement for network signalling value “NS_56”

When "NS_56" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.27-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.27-1: Additional requirements for "NS_56"

## 6.5.3.3.28Requirement for network signalling value “NS_62”

When "NS_62" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.28-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.28-1: Additional requirements for "NS_62"

## 6.5.3.3.29Requirement for network signalling value “NS_26”

When "NS_26" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.29-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.29-1: Additional requirements

## 6.5.3.3.30Requirement for network signalling value “NS_36”

When "NS_36" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5.3.3.30-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5.3.3.30-1: Additional requirements

## 6.5.4Transmit intermodulation

The transmit intermodulation performance is a measure of the capability of the transmitter to inhibit the generation of signals in its non linear elements caused by presence of the wanted signal and an interfering signal reaching the transmitter via the antenna.

UE transmit intermodulation is defined by the ratio of the mean power of the wanted signal to the mean power of the intermodulation product when an interfering CW signal is added at a level below the wanted signal at each transmitter antenna port with the other antenna port(s) if any terminated. Both the wanted signal power and the intermodulation product power are measured through NR rectangular filter with measurement bandwidth shown in Table 6.5.4-1.

The requirement of transmit intermodulation is specified in Table 6.5.4-1.

Table 6.5.4-1: Transmit Intermodulation

## 6.5AOutput RF spectrum emissions for CA

## 6.5A.0General

For inter-band carrier aggregation with one uplink carrier assigned to one NR band, the output RF spectrum emissions requirements in clause 6.5 apply.

## 6.5A.1Occupied bandwidth for CA

## 6.5A.1.1Void

## 6.5A.1.1aOccupied bandwidth for Intra-band contiguous CA

For intra-band contiguous carrier aggregation the occupied bandwidth is a measure of the bandwidth containing 99 % of the total integrated power of the transmitted spectrum. The occupied bandwidth shall be less than the aggregated channel bandwidth defined in clause 5.3A.3.

## 6.5A.1.2Occupied bandwidth for Intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation, the OBW requirement is met when the ratio of the transmitted power in all sub-blocks of the uplink CA configuration to the total integrated power of the transmitted spectrum is greater than 99%.

## 6.5A.1.3Occupied bandwidth for Inter-band CA

For inter-band carrier aggregation with two contiguous carriers assigned to one NR band, the occupied bandwidth requirements in subclause 6.5A.1.1a apply for that band.

For inter-band carrier aggregation with uplink assigned to two NR bands, the occupied bandwidth is defined per component carrier. Occupied bandwidth is the bandwidth containing 99 % of the total integrated mean power of the transmitted spectrum on assigned channel bandwidth on the component carrier. The occupied bandwidth shall be less than the channel bandwidth specified in Table 6.5.1-1.

## 6.5A.2Out of band emission for CA

## 6.5A.2.1General

This clause contains requirements for out of band emissions for UE configured of carrier aggregation.

## 6.5A.2.2Spectrum emission mask

## 6.5A.2.2.1Spectrum emission mask for intra-band contiguous CA

For intra-band contiguous carrier aggregation the spectrum emission mask of the UE applies to frequencies (ΔfOOB) starting from the  edge of the aggregated channel bandwidth. For intra-band contiguous carrier aggregation, the power of any UE emission shall not exceed the levels specified in Table 6.5A.2.2.1-1 for the specified channel bandwidth. For UE indicating mpr-ActiveCarrierEnh-r19 supported, if intra-band contiguous CA with single CC is activated, the spectrum emission mask applies based on the aggregated channel bandwidth.

For power class 2 intra-band contiguous carrier aggregation, the spectrum emission mask is measured as the sum from both UE transmit antenna connectors when UE indicates support for dualPA-Architecture IE.

Table 6.5A.2.2.1-1: General NR CA spectrum emission mask

## 6.5A.2.2.2Spectrum emission mask for intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation the spectrum emission mask requirement is defined as a composite spectrum emissions mask. Composite spectrum emission mask applies to frequencies up to ΔfOOB starting from the edges of the sub-blocks. Composite spectrum emission mask is defined as follows

a)Composite spectrum emission mask is a combination of individual sub-block spectrum emissions masks

b)In case the sub-block consist of one component carrier the sub-lock general spectrum emission mask is defined in subclause 6.5.2.1

c)If for some frequency sub-block spectrum emission masks overlap then spectrum emission mask allowing higher power spectral density applies for that frequency

d)If for some frequency a sub-block spectrum emission mask overlaps with the sub-block bandwidth of another sub-block, then the emission mask does not apply for that frequency.

For intra-band non-contiguous carrier aggregation, the spectrum emission mask is measured as the sum from both UE transmit antenna connectors when UE indicates support for dualPA-Architecture IE.

## 6.5A.2.2.3Spectrum emission mask for Inter-band CA

For inter-band carrier aggregation with two contiguous carriers assigned to one NR band, the spectrum emission mask requirements in subclause 6.5A.2.2.1 apply for that band.

For inter-band carrier aggregation with two uplink non-contiguous carrier assigned to one NR band, the spectrum emission mask requirements in subclause 6.5A.2.2.2 apply for that band.

For inter-band carrier aggregation with uplink assigned to two NR bands, the spectrum emission mask of the UE is defined per component carrier while both component carriers are active and the requirements are specified in clauses 6.5.2.1 and 6.5.2.2. If for some frequency spectrum emission masks of component carriers overlap then spectrum emission mask allowing higher power spectral density applies for that frequency. If for some frequency a component carrier spectrum emission mask overlaps with the channel bandwidth of another component carrier, then the emission mask does not apply for that frequency.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per operating band), the spectrum emission mask of the UE is defined per NR band while all component carriers are active. For the NR band supporting one component carrier the requirements in subclauses 6.5.2.1 and 6.5.2.2 apply. For the NR band supporting two contiguous component carriers the requirements specified in subclause 6.5A.2.2.1apply. If for some frequency spectrum emission masks of single component carrier and two contiguous component carriers overlap then spectrum emission mask allowing higher power spectral density applies for that frequency. If for some frequency spectrum emission masks of single component carrier or two contiguous component carriers overlap then the emission mask does not apply for that frequency.

## 6.5.A.2.2.4Void

## 6.5A.2.3Additional spectrum emission mask for CA

## 6.5A.2.3.1Additional spectrum emission mask for intra-band contiguous CA

6.5A.2.3.1.1Requirements for network signalling value "CA_NS_04"

When "CA_NS_04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5A.2.3.1.1-1. For power class 2 intra-band contiguous carrier aggregation, the additional spectrum emission mask is measured as the sum from both UE transmit antenna connectors when UE indicates support for dualPA-Architecture IE.

Table 6.5A.2.3.1.1-1: Additional requirements for "CA_NS_04"

6.5A.2.3.1.2Requirements for network signalling value "CA_NS_27"

When "CA_NS_27" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.2A.2.3.2.1.-1.

Table 6.2A.2.3.2.1-1: Additional requirements for "CA_NS_27"

NOTE:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.5A.2.3.2Additional spectrum emission mask for Intra-band non-contiguous CA

6.5A.2.3.2.1 Minimum requirement (network signalling value “CA_NC_NS_04”)

For intra-band non-cotiguous CA_n41(2A), the additional SEM requirements in subclause 6.5.2.3.2 (indicated by NS_04) applies in each uplink CC.

## 6.5A.2.3.3Additional spectrum emission mask for Inter-band CA

## 6.5A.2.4Adjacent channel leakage ratio

## 6.5A.2.4.1NR ACLR

6.5A.2.4.1.1NR ACLR for intra-band contiguous CA

For intra-band contiguous carrier aggregation, the carrier aggregation the Adjacent Channel Leakage power Ratio is the ratio of the filtered mean power centred on the aggregated channel bandwidth to the filtered mean power centred on an adjacent aggregated channel bandwidth at nominal channel spacing. The assigned aggregated channel bandwidth power and adjacent aggregated channel bandwidth power are measured with rectangular filters with measurement bandwidths specified in Table 6.5A.2.4.1.1-1 for power class 3 and 6.5A.2.4.1.1-2 for power class 2 and power class 1.5. If the measured adjacent channel power is greater than –50dBm then the NRACLR shall be higher than the value specified in Table 6.5A.2.4.1.1-1 for power class 3 and 6.5A.2.4.1.1-2 for power class 2 and power class 1.5. For UE indicating mpr-ActiveCarrierEnh-r19 supported, if intra-band contiguous CA with single CC is activated, the ACLR applies based on the aggregated channel bandwidth.

Table 6.5A.2.4.1.1-1: General requirements for intra-band contiguous CA ACLR power class 3

Table 6.5A.2.4.1.1-2: General requirements for intra-band contiguous CA ACLR power class 2 and power class 1.5

6.5A.2.4.1.2NR ACLR for intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation, CA Adjacent Channel Leakage power Ratio (CAACLR) is the ratio of the sum of the filtered mean power centred on each assigned channel frequency to the filtered mean power centred on an adjacent NR channel frequency at nominal channel spacing. In case the sub-block gap bandwidth Wgap between two uplink sub-blocks is smaller than maximum of the two uplink sub-block bandwidths then no CAACLR requirement is set for the gap. Each assigned NR channel power and adjacent NR channel power are measured with rectangular filters with measurement bandwidths specified in Table 6.5A.2.4.1.2-1 for power class 3 and 6.5A.2.4.1.2-2 for power class 2 and power class 1.5. If the measured adjacent channel power is greater than –50dBm then the ACLR shall be higher than the value specified in Table 6.5A.2.4.1.2-1 for power class 3 and 6.5A.2.4.1.2-2 for power class 2 and power class 1.5.

Table 6.5A.2.4.1.2-1: General requirements for intra-band non-contiguous CA ACLR power class 3

Table 6.5A.2.4.1.2-2: General requirements for intra-band non-contiguous CA ACLR power class 2 and power class 1.5

6.5A.2.4.1.3NR ACLR for Inter-band CA

For inter-band carrier aggregation with two contiguous carriers assigned to one NR band, the NR Adjacent Channel Leakage power Ratio (NRACLR) requirements in subclause 6.5A.2.4.1.1apply for that band. For inter-band carrier aggregation with two uplink non-contiguous carrier assigned to one NR band, the NR Adjacent Channel Leakage power Ratio (NRACLR) requirements in subclause 6.5A.2.4.1.2 apply for that band.

For inter-band carrier aggregation with uplink assigned to two NR bands, the NR Adjacent Channel Leakage power Ratio (NRACLR) is defined per component carrier while both component carriers are active and the requirement is specified in clause 6.5.2.4.1.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per operating band), the NR ACLR is defined as follows. For the NR band supporting one component carrier, the NR ACLR is the ratio of the filtered mean power centred on the assigned channel bandwidth of the component carrier to the filtered mean power centred on an adjacent channel frequency and the requirements in subclause 6.5.2.4.1 apply. For the NR band supporting two contiguous component carriers the NR ACLR is the ratio of the filtered mean power centred on the aggregated channel bandwidth to the filtered mean power centred on an adjacent(s) aggregated channel bandwidth at nominal channel spacing and the requirements of CA ACLR specified in subclause 6.5A.2.4.1.1apply.

6.5A.2.4.1.4Void

## 6.5A.2.4.2UTRA ACLR

6.5A.2.4.2.1Void

6.5A.2.4.2.2Void

6.5A.2.4.2.3UTRA ACLR for Inter-band CA

For inter-band carrier aggregation with uplink assigned to two NR bands, the UTRA Adjacent Channel Leakage power Ratio (UTRAACLR) is defined per component carrier while both component carrier are active and the requirement is specified in clause 6.5.2.4.2.

6.5A.2.4.2.4UTRA ACLR for Intra-band non-contiguous CA

For intra-band non-contiguous carrier aggregation, UTRA adjacent channel leakage power ratio (UTRAACLR) is the ratio of the sum of the filtered mean power centred on each assigned channel frequency to the filtered mean power centred on an adjacent(s) UTRA channel frequency. In case the gap bandwidth Wgap between 2 uplink CCs is smaller than 10MHz then no UTRA ACLR requirement is set for the gap. In case Wgap is greater than or equal to 10MHz but less than 20MHz, then only the first UTRA ACLR (UTRAACLR1) requirement applies in the gap. In case Wgap is greater than or equal to 20MHz, then both the first and the second UTRA ACLR (UTRAACLR1 and UTRAACLR2) requirements apply in the gap. Each assigned NR channel power is measured with rectangular filters with measurement bandwidths specified in Table 6.5.2.4.1-1 and adjacent UTRA channel power is measured with a RRC filter with roll-off factor = 0.22 and bandwidth of 3.84 MHz. If the measured adjacent channel power is greater than –50dBm then the UTRAACLR1 and UTRAACLR2 shall be higher than the value specified in Table 6.5A.2.4.2.4-1.

Table 6.5A.2.4.2.4-1: General requirements for intra-band non-contiguous CA ACLR

## 6.5A.3Spurious emission for CA

## 6.5A.3.1General spurious emissions

For inter-band carrier aggregation with uplink assigned to two NR bands, the spurious emission requirement Table 6.5.3.1-2 apply for the frequency ranges that are more than FOOB as defined in Table 6.5.3.1-1 away from edges of the assigned channel bandwidth on a component carrier. If for some frequency a spurious emission requirement of individual component carrier overlaps with the spectrum emission mask or channel bandwidth of another component carrier then it does not apply.

NOTE:For inter-band carrier aggregation with uplink assigned to two NR bands the requirements in Table 6.5.3.1-2 could be verified by measuring spurious emissions at the specific frequencies where second and third order intermodulation products generated by the two transmitted carriers can occur; in that case, the requirements for remaining applicable frequencies in Table 6.5.3.1-2 would be considered to be verified by the measurements verifying the one uplink inter-band CA spurious emission requirement.

For intra-band contiguous carrier aggregation the spurious emission limits apply for the frequency ranges that are more than FOOB (MHz) in Table 6.5A.3.1-1 from the edge of the aggregated channel bandwidth. For frequencies ΔfOOB greater than FOOB as specified in Table 6.5A.3.1-1 the spurious emission requirements in Table 6.5.3.1-2 are applicable. For power class 2 intra-band contiguous carrier aggregation, the spurious emissions is measured as the sum from both UE transmit antenna connectors when UE indicates support for dualPA-Architecture IE. For UE indicating mpr-ActiveCarrierEnh-r19 supported, if intra-band contiguous CA with single CC is activated, FOOB is defined based on the aggregated channel bandwidth.

Table 6.5A.3.1-1: Boundary between out of band and spurious emission domain for intra-band contiguous carrier aggregation

For intra-band non-contiguous carrier aggregation transmission the spurious emission requirement is defined as a composite spurious emission requirement. Composite spurious emission requirement applies to frequency ranges that are more than FOOB away from the edges of each carrier in the gap and out of the gap. Composite spurious emission requirement is defined as follows

a)Composite spurious emission requirement is a combination of individual sub-block spurious emission requirements

b)In case the sub-block consist of one component carrier the sub-lock spurious emission requirement and FOOB are defined in subclause 6.5.3.1

c)If for some frequency an individual sub-block spurious emission requirement overlaps with the general spectrum emission mask or the sub-block bandwidth of another sub-block then it does not apply

For intra-band non-contiguous carrier aggregation, the spurious emissions is measured as the sum from both UE transmit antenna connectors when UE indicates support for dualPA-Architecture IE.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per operating band), the spurious emission requirement is defined as follows. For the NR band supporting one component carrier the requirements in Table 6.5.3.1-2 apply for frequency ranges that are more than FOOB (MHz) from the edges of assigned channel bandwidth as defined in Table 6.5.3.1-1. For the NR band supporting two contiguous component carriers the requirements in Table 6.5.3.1-2 apply for frequency ranges that are more than FOOB (MHz) from the edges of assigned aggregated channel bandwidth as defined in Table 6.5A.3.1-1. If for some frequency a spurious emission requirement of a single component carrier or two contiguous component carriers overlap with the spurious emission requirement or channel bandwidth of another component carrier or two contiguously aggregated carriers then it does not apply.

## 6.5A.3.2Spurious emissions for UE co-existence

## 6.5A.3.2.0General

Unless otherwise stated, the spurious emission for UE co-existence apply for the frequency ranges that are more than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth configured on each component carrier.

## 6.5A.3.2.1Spurious emissions for UE co-existence for intra-band contiguous CA

This clause specifies the requirements for the specified intra-band contiguous carrier aggregation configurations for coexistence with protected bands, the requirements in Table 6.5A.3.2.1-1 apply. For power class 2 intra-band contiguous carrier aggregation, the spurious emissions is measured as the sum from both UE transmit antenna connectors when UE indicates support for dualPA-Architecture IE.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

Table 6.5A.3.2.1-1: Requirements for uplink intra-band contiguous carrier aggregation

## 6.5A.3.2.2Spurious emissions for UE co-existence for intra-band non-contiguous CA

This clause specifies the requirements for the specified intra-band non-contiguous carrier aggregation configurations for coexistence with protected bands, the requirements in Table 6.5A.3.2.2-1 apply. For intra-band non-contiguous carrier aggregation, the spurious emissions is measured as the sum from both UE transmit antenna connectors when UE indicates support for dualPA-Architecture IE.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

Table 6.5A.3.2.2-1: Requirements for uplink intra-band non-contiguous carrier aggregation

## 6.5A.3.2.3Spurious emissions for UE co-existence for Inter-band CA

This clause specifies the additional requirements for inter-band uplink carrier aggregation configurations with the single CC uplink assigned to two NR bands for coexistence with protected bandsfor the specified uplink carrier aggregation configurations in Table 6.5A.3.2.3-1. The intersection of the requirements for the individual bands specified in clause 6.5.3.2 shall also apply for the specified uplink carrier aggregation configurations. Intersection of a requirement means that both UL constituent bands have the same protected band requirement specified and if one or both protected bands have note(s) associated those note(s) also apply.

For inter-band carrier aggregation with two contiguous carriers assigned to one NR band, the requirements in subclause 6.5A.3.2.1 apply for that band.

For inter-band carrier aggregation with two uplink non-contiguous carrier assigned to one NR band, the spurious emissions for UE co-existence requirements in subclause 6.5A.3.2.2 apply for that band.

For inter-band carrier aggregation with the uplink assigned to two NR bands, the requirements in Table 6.5A.3.2.3-1 apply on each component carrier with all component carriers are active.

NOTE:For inter-band carrier aggregation with uplink assigned to two NR bands the requirements in Table 6.5A.3.2.3-1 could be verified by measuring spurious emissions at the specific frequencies where second and third order intermodulation products generated by the two transmitted carriers can occur; in that case, the requirements for remaining applicable frequencies in Table 6.5A.3.2.3-1 and in clause 6.5.3.2  would be considered to be verified by the measurements verifying the one uplink inter-band CA UE to UE co-existence requirements.

Table 6.5A.3.2.3-1: Requirements for uplink inter-band carrier aggregation (two bands)

## 6.5A.3.2.4Void

## 6.5A.3.2.5Void

## 6.5A.3.2.6Void

## 6.5A.3.3Additional spurious emissions for CA

## 6.5A.3.3.1Additional spurious emissions for intra-band contiguous  CA

6.5A.3.3.1.1Requirement for network signalling value "CA_ NS_04"

When "CA_NS04" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5A.3.3.1.1-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5A.3.1-1 from the edge of the aggregated channel bandwidth. For power class 2 intra-band contiguous carrier aggregation, the additional spurious emissions is measured as the sum from both UE transmit antenna connectors when UE indicates support for dualPA-Architecture IE.

Table 6.5A.3.3.1.1-1: Additional requirements for "CA_ NS_04"

6.5A.3.3.1.2Requirement for network signalling value "CA_NS_27"

When "CA_NS 27" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5A.3.3.1.2-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5A.3.1-1 from the edge of the aggregated channel bandwidth.

Table 6.5A.3.3.1.2-1: Additional requirements for "CA_NS_27"

6.5A.3.3.1.3Requirement for network signalling value "CA_NS_46"

When "CA_NS 46" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5A.3.3.1.3-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5A.3.1-1 from the edge of the aggregated channel bandwidth.

Table 6.5A.3.3.1.3-1: Additional requirements for “CA_NS_46”

## 6.5A.3.3.2Additional spurious emissions for intra-band non-contiguous CA

6.5A.3.3.2.1Requirement for network signalling value "CA_NC_NS_04"

For intra-band non-contiguous CA_n41(2A), the spurious emission requirements in subclause 6.5.3.3.1 (indicated by NS_04) applies in each uplink CC.

6.5A.3.3.2.2Requirement for network signalling value "CA_NC_NS_12"

For intra-band non-contiguous CA_n26(2A), the spurious emission requirements in subclause 6.5.3.3.17 (indicated by NS_12) applies in each uplink CC for 5MHz and 10MHz channel bandwidth.

6.5A.3.3.2.3Requirement for network signalling value "CA_NC_NS_13"

For intra-band non-contiguous CA_n26(2A), the spurious emission requirements in subclause 6.5.3.3.18 (indicated by NS_13) applies in each uplink CC for 5MHz channel bandwidth.

6.5A.3.3.2.4Requirement for network signalling value "CA_NC_NS_14"

For intra-band non-contiguous CA_n26(2A), the spurious emission requirements in subclause 6.5.3.3.19 (indicated by NS_14) applies in each uplink CC for 10MHz channel bandwidth.

6.5A.3.3.2.5Requirement for network signalling value "CA_NC_NS_15"

For intra-band non-contiguous CA_n26(2A), the spurious emission requirements in subclause 6.5.3.3.20 (indicated by NS_15) applies in each uplink CC for 5MHz, 10MHz and 15MHz channel bandwidth.

## 6.5A.4Transmit intermodulation for CA

## 6.5A.4.2.1Transmit intermodulation for intra-band contiguous CA

For intra-band contiguous carrier aggregation the requirement of transmitting intermodulation is specified in Table 6.5A.4.2.1-1.

Table 6.5A.4.2.1-1: Transmit Intermodulation

## 6.5A.4.2.2Void

6.5A.4.2.3Transmit intermodulation for Inter-band CA

For inter-band carrier aggregation with two contiguous carriers assigned to one NR band, the transmit intermodulation requirements in subclause 6.5A.4.2.1apply for that band.

For inter-band carrier aggregation with two uplink non-contiguous carrier assigned to one NR band, the transmit intermodulation requirements in subclause 6.5A.4.2.2 apply for that band.

For inter-band carrier aggregation with uplink assigned to two NR bands, the transmit intermodulation requirement is specified in Table 6.5.4-1 which shall apply on each component carrier with both component carriers active.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per operating band) transmit intermodulation is defined as follows. For the NR band supporting one component carrier the requirement specified in Table 6.5.4-1 apply. For the NR band supporting two contiguous component carriers the requirements specified in Table 6.5A.4.2.1-1 apply.

## 6.5BOutput RF spectrum emissions for NR-DC

For inter-band NR-DC with one uplink carrier assigned per NR band, the output RF spectrum emissions for the corresponding inter-band CA configuration as specified in clause 6.5A applies.

## 6.5DOutput RF spectrum emissions for UL MIMO

## 6.5D.1Occupied bandwidth for UL MIMO

For UE supporting UL MIMO, the requirements for occupied bandwidth apply to  the sum of the powers from all UE transmit antenna connectors. The occupied bandwidth is defined as the bandwidth containing 99 % of the total integrated mean power of the transmitted spectrum on the assigned channel at each transmit antenna connector.

For UE with two or four transmit antenna connectors in closed-loop spatial multiplexing scheme, the occupied bandwidth shall be less than the channel bandwidth specified in Table 6.5.1-1. The requirements shall be met with UL MIMO configurations described in clause 6.2D.1.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.5.1 apply when TxD is not indicated, and the requirements in clause 6.5G.1 apply when TxD is indicated.

## 6.5D.2Out of band emission for UL MIMO

For UE supporting UL MIMO or uplink full power transmission (ULFPTx) for UL MIMO, the requirements for Out of band emissions resulting from the modulation process and non-linearity in the transmitters is defined as the sum of the emissions from all UE transmit antenna connectors.

For UEs with two or four transmit antenna connectors in closed-loop spatial multiplexing scheme, the requirements in subclause 6.5.2 apply. The requirements shall be met with UL MIMO configurations described in clause 6.2D.1.

For UE support uplink full power transmission (ULFPTx) for UL MIMO, the requirements in clause 6.5.2 shall apply. The requirements shall be met with the PUSCH configurations specified in Table 6.2D.1-3, based upon UE’s support of uplink full power transmission mode.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.5.2 apply when TxD is not indicated, and the requirements in clause 6.5G.2 apply when TxD is indicated.

## 6.5D.3Spurious emission for UL MIMO

For UE supporting UL MIMO or uplink full power transmission (ULFPTx) for UL MIMO, the requirements for Spurious emissions which are caused by unwanted transmitter effects such as harmonics emission, parasitic emissions, intermodulation products and frequency conversion products is defined as the sum of the emissions from all UE transmit antenna connectors.

For UEs with two or four transmit antenna connectors in closed-loop spatial multiplexing scheme, the requirements specified in subclause 6.5.3 apply. The requirements shall be met with the UL MIMO configurations described in clause 6.2D.1.

For UE support uplink full power transmission (ULFPTx) for UL MIMO, the requirements in clause 6.5.3 shall apply. The requirements shall be met with the PUSCH configurations specified in Table 6.2D.1-3, based upon UE’s support of uplink full power transmission mode.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.5.3 apply when TxD is not indicated, and the requirements in clause 6.5G.3 apply when TxD is indicated.

## 6.5D.4Transmit intermodulation for UL MIMO

For UE supporting UL MIMO, the transmit intermodulation requirements are specified at each transmit antenna connector and the wanted signal is defined as the sum of output powers from all UE transmit antenna connectors.

For UEs with two or four transmit antenna connectors in closed-loop spatial multiplexing scheme, the requirements specified in clause 6.5.4 apply to each transmit antenna connector. The requirements shall be met with the UL MIMO configurations described in clause 6.2D.1.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.5.4 apply when TxD is not indicated, and the requirements in clause 6.5G.4 apply when TxD is indicated.

## 6.5EOutput RF spectrum emissions for V2X

## 6.5E.1Occupied bandwidth for V2X

## 6.5E.1.1General

When UE is configured for NR V2X sidelink transmissions non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, the requirements in clause 6.5.1 shall apply for NR V2X sidelink transmission.

For NR V2X UE with two transmit antenna connectors, the occupied bandwidth at each transmitter antenna shall be less than the channel bandwidth specified in Table 6.5.1-1.

If V2X UE transmits on one antenna connector at a time, the requirements specified for single carrier shall apply to the active antenna connector.

## 6.5E.1.1AOccupied bandwidth for sidelink CA

For SL intra-band contiguous/non-contiguous CA, the occupied bandwidth is a measure of the bandwidth containing 99 % of the total integrated power of the aggregated CBW. The occupied bandwidth shall be less than the aggregated channel bandwidth.

## 6.5E.1.2Occupied bandwidth for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 6.5.1 shall apply for the uplink in licensed band and the requirements specified in clause 6.5E.1.1 shall apply for the sidelink in licensed band or Band n47.

For the intra-band concurrent NR V2X operation, the requirements specified in clause 6.5.1 shall apply for the uplink in licensed band and the requirements specified in clause 6.5E.1 shall apply for the sidelink in licensed band.

## 6.5E.1FOccupied bandwidth for Sidelink Unlicensed

The requirements for occupied bandwidth in clause 6.5.1 apply for the specified SL-U channel bandwidths in Table 5.3E.1F-1.

## 6.5E.1F.1Occupied bandwidth for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the requirements specified in clause 6.5.1 shall apply for the uplink in licensed band and the requirements specified in clause 6.5E.1F shall apply for NR sidelink operation in unlicensed band.

## 6.5E.2Out of band emission for V2X

## 6.5E.2.1General

When UE is configured for NR V2X sidelink transmissions non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, the requirements in clause 6.5E.2.2.1, 6.5E.2.3 and 6.5E.2.4.1 apply for NR V2X sidelink transmission.

For NR V2X UE with two transmit antenna connectors, the requirements specified for single carrier shall apply to each transmit antenna connector.

## 6.5E.2.2Spectrum emission mask

## 6.5E.2.2.1General

For NR V2X UE, the existing NR general spectrum emission mask in subclause 6.5.2.2 applies for all supporting NR V2X channel bandwidths. The spectrum emission mask of the UE applies to frequencies (ΔfOOB) starting from the  edge of the assigned NR channel bandwidth. For frequencies greater than (ΔfOOB), the power of any UE emission shall not exceed the levels specified in Table 6.5.2.2-1 for the specified channel bandwidth for NR V2X operating bands in Table 5.2E.1-1.

## 6.5E.2.2.1ASpectrum emission mask for sidelink CA

For SL intra-band contiguous CA, the SEM requirement for NR intra-band contiguous CA as specified in clause 6.5A.2.2.1 shall be applied to the aggregated channel bandwidth with SL CA bandwidth class B.

For SL intra-band non-contiguous CA, the SEM requirement for NR intra-band non-contiguous CA as specified in clause 6.5A.2.2.2 shall be applied to the aggregated channel bandwidth with SL CA bandwidth class B.

## 6.5E.2.2.2Spectrum emission mask for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the general/additional SEM requirements specified in clause 6.5.2 shall apply for the uplink in licensed band and the general/additional SEM requirements specified in clause 6.5E.2.2.1 shall apply for the sidelink in licensed band or Band n47.

For intra-band NR V2X transmission with bandwidth class B where Uu and SL overlap in time the specifications in section 6.5A.2.2.1 and 6.5A.2.2.2 apply.

## 6.5E.2.3Additional Spectrum emission mask

## 6.5E.2.3.1Requirements for network signalling value "NS_33"

The additional spectrum mask in Table 6.5E.2.3.1-1 applies for NR V2X UE within 5855 MHz to 5925 MHz according to ETSI EN 302 571. Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "NS_33" is indicated in the cell or pre-configured radio parameters, the power of any V2X UE emission shall not exceed the levels specified in Table 6.5E.2.3.1-1.

Table 6.5E.2.3.1-1: Additional spectrum mask requirements for 10MHz channel bandwidth

NOTE 1:As a general rule, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

NOTE 2:Additional SEM for NR V2X overrides any other requirements in frequency range 5855-5925 MHz.

NOTE 3:The EIRP requirement is converted to conducted requirement depend on the supported post antenna connector gain Gpost connector declared by the UE following the principle described in annex I in [11].

## 6.5E.2.3.1ARequirements for network or pre-configured signalling value “SLCA_NC_NS_33”

For SL intra-band non-contiguous CA_n47(2A), the additional SEM requirements in subclause 6.5E.2.3.1 (indicated by NS_33) applies in each uplink CC.

## 6.5E.2.3.2Requirements for network signalling value "NS_52"

The additional spectrum mask in Table 6.5E.2.3.2-1 applies for NR V2X UE within 5 765 MHz to 6 005 MHz according to FCC regulation. Additional spectrum emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

When "NS_52" is indicated in the cell or pre-configured radio parameters, the power of any V2X UE emission shall not exceed the levels specified in Table 6.5E.2.3.2-1.

Table 6.5E.2.3.2-1: Additional spectrum mask requirements for 40MHz channel bandwidth (fc = 5885MHz)

NOTE:The ASE requirements for NS_52 will not be verified until the corresponding regulation release a formal rule for C-V2X emission limits.

## 6.5E.2.3.3Requirements for network signalling value "NS_06"

The additional spectrum mask are signalled by the network to indicate that the public safety (PS) UE in NR band n14 shall meet an additional for a specific deployement scenarios.

When "NS_06" is indicated by serving cell or pre-configured radio parameters, the power of any PS UE emission shall not exceed the levels specified in Table 6.5.2.3.4-1.

## 6.5E.2.4Adjacent channel leakage ratio

## 6.5E.2.4.1General

Adjacent Channel Leakage power Ratio (ACLR) is the ratio of the filtered mean power centred on the assigned channel frequency to the filtered mean power centred on an adjacent channel frequency.

For NR V2X UE, the existing ACLR requirement for NR uplink transmission in clause 6.5.2.4 are applied for NR V2X UE for NR V2X operating bands in 5.2E.1-1.

For NR V2X UE with two transmit antenna connectors, the requirements specified for single carrier shall apply to each transmit antenna connector.

If V2X UE transmits on one antenna connector at a time, the requirements specified for single carrier shall apply to the active antenna connector.

## 6.5E.2.4.1AACLR for sidelink CA

For SL intra-band contiguous CA, the general NR CA ACLR requirements for CA Bandwidth Class B specified in subclause 6.5A.2.4.1.1 shall be applied to the aggregated channel bandwidth with SL CA bandwidth class B.

For SL intra-band non-contiguous CA, the general NR CA ACLR requirements for CA Bandwidth Class B specified in subclause 6.5A.2.4.1.2 shall be applied to the aggregated channel bandwidth with SL CA bandwidth class B.

## 6.5E.2.4.2ACLR for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the ACLR requirement specified in clause 6.5.2.4 shall apply for the uplink in licensed band and the ACLR requirement specified in clause 6.5E.2.4.1 shall apply for the sidelink in licensed band or Band n47.

For the intra-band NR V2X operation with bandwidth classes B where Uu and SL transmission overlaps in time, the ACLR requirement specified in clause 6.5A.2.4.1 shall apply for the both uplink and sidelink transmission in licensed band.

## 6.5E.2FOut of band emission for Sidelink Unlicensed

## 6.5E.2F.1General

The Out of band emissions are unwanted emissions immediately outside the assigned channel bandwidth resulting from the modulation process and non-linearity in the transmitter but excluding spurious emissions. This out of band emission limit is specified in terms of a spectrum emission mask and an adjacent channel leakage power ratio.

To improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.5E.2F.2Spectrum emission mask for operation with shared spectrum channel access

The requirements for spectrum emission mask in clause 6.5F.2.2 apply for SL-U operation.

## 6.5E.2F.2.1Spectrum emission mask for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the general/additional SEM requirements specified in clause 6.5.2 shall apply for NR Uu operation in licensed band and the general/additional SEM requirements specified in clause 6.5E.2F shall apply for NR sidelink operation in unlicensed band.

## 6.5E.2F.3Additional spectrum emission mask

There are no additional spectrum emission mask requirements for SL-U operation. in this version of the specification.

## 6.5E.2F.4Adjacent channel leakage ratio

The requirements for ACLR in clause 6.5F.2.4 apply for SL-U operation.

## 6.5E.2F.4.1Adjacent channel leakage ratio for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the ACLR requirement specified in clause 6.5.2.4 shall apply for NR Uu operation in licensed band and the ACLR requirement specified in clause 6.5E.2F.4 shall apply for NR sidelink operation in unlicensed band.

## 6.5E.3Spurious emissions for V2X

## 6.5E.3.1General spurious emissions

When UE is configured for NR V2X sidelink transmissions non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, the general spurious emission requirements in clause 6.5.3.1 shall apply for NR V2X sidelink transmission.

For NR V2X UE with two transmit antenna connectors, the requirements specified for single carrier shall apply to each transmit antenna connector.

## 6.5E.3.1ASpurious emissions for sidelink CA

For SL intra-band contiguous/non-contiguous CA, the general NR CA general SE for CA Bandwidth specified in subclause 6.5A.3.1 shall be applied to the aggregated channel bandwidth with SL CA bandwidth class B.

## 6.5E.3.2Spurious emissions for UE co-existence

When UE is configured for NR V2X sidelink transmissions non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, the requirements in clause 6.5.3.2 shall apply for NR V2X sidelink transmission.

For NR V2X UE with two transmit antenna connectors, the requirements specified for single carrier shall apply to each transmit antenna connector.

## 6.5E.3.2ASpurious emissions band UE co-existence for sidelink CA

For SL intra-band contiguous CA, the protection operating band lists for n47 transmission is defined in Table 6.5.3.2-1 which shall be applied to NR SL intra-band contiguous CA UE.

For SL intra-band non-contiguous CA, the protection operating band lists for n47 transmission is defined in Table 6.5.3.2-1 which shall be applied to NR SL intra-band non-contiguous CA UE.

## 6.5E.3.3Spurious emissions for UE co-existence for V2X concurrent operation

This clause specifies the additional requirements for inter-band concurrent V2X operation with the single CC uplink assigned to two NR bands for coexistence with protected bands for the specified simultaneous transmission of the inter-band concurrent V2X configurations in Table 6.5E.3.3-1. The intersection of the requirements for the individual bands specified in clause 6.5.3.2 shall also apply for the specified simultaneous transmission of the inter-band concurrent V2X. Intersection of a requirement means that both UL or sidelink transmission constituent bands have the same protected band requirement specified and if one or both protected bands have note(s) associated those note(s) also apply.

For the inter-band concurrent NR V2X operation, the UE-coexistence requirements in Table 6.5E.3.3-1 apply for the corresponding inter-band concurrent operation with transmission assigned to both uplink in licensed band and sidelink in Band n47.

NOTE:For inter-band concurrent V2X operation with uplink assigned to NR band and slidelink transmission assigned to NR V2X operating bands, the requirements in Table 6.5E.3.3-1 could be verified by measuring spurious emissions at the specific frequencies where second and third order intermodulation products generated by the two transmitted carriers can occur; in that case, the requirements for remaining applicable frequencies in Table 6.5E.3.3-1 and in clause 6.5.3.2 would be considered to be verified by the measurements verifying the one uplink inter-band concurrent UE to UE co-existence requirements.

Table 6.5E.3.3-1: Requirements for inter-band concurrent V2X operation

For the intra-band NR V2X transmission where Uu and SL overlap in time, the UE-coexistence requirements in Table 6.5A.3.2.1-1 apply for the corresponding intra-band concurrent operation for the both uplink and sidelink transmission in licensed band.

## 6.5E.3.4Additional spurious emissions requirements for V2X

## 6.5E.3.4.1General

This clause specifies additional spurious emission requirements for V2X operation

## 6.5E.3.4.2Requirements for network signalling value "NS_33"

Table 6.5E.3.4.2-1: Additional requirements for "NS_33"

When "NS_33" is configured from pre-configured radio parameters or the cell, and the indication from upper layers has indicated that the UE is within the protection zone of CEN DSRC devices or HDR DSRC devices, the power of any NR V2X UE emission shall fulfil either one of the two sets of conditions.

Table 6.5E.3.4.2-2: Requirements for spurious emissions to protect CEN DSRC for V2X UE

## 6.5E.3.4AAdditional spurious emissions requirements for sidelink CA

## 6.5E.3.4A.1General

This clause specifies additional spurious emission requirements for sidelink intra-band non-contiguous CA.

## 6.5E.3.4A.2Requirements for network signalling value "SLCA_NC_NS_33"

Table 6.5E.3.4A.2-1: Additional requirements for "SLCA_NC_NS_33"

When "SLCA_NC_NS_33" is configured from pre-configured radio parameters or the cell, and the indication from upper layers has indicated that the UE is within the protection zone of CEN DSRC devices or HDR DSRC devices, the power of any NR V2X UE emission shall fulfil either one of the two sets of conditions.

Table 6.5E.3.4A.2-2: Requirements for spurious emissions to protect CEN DSRC for V2X UE

## 6.5E.3.4.3Void

## 6.5E.3FSpurious emissions for Sidelink Unlicensed

## 6.5E.3F.0General

Spurious emissions are emissions which are caused by unwanted transmitter effects such as harmonics emission, parasitic emissions, intermodulation products and frequency conversion products, but exclude out of band emissions unless otherwise stated. The spurious emission limits are specified in terms of general requirements in line with SM.329 [9] and NR operating band requirement to address UE co-existence.

To improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

## 6.5E.3F.1General spurious emissions

The requirements for general spurious emission requirements in clause 6.5.3.1 apply for SL-U operation.

## 6.5E.3F.2Spurious emissions for UE co-existence

Spurious emissions requirements for UE coexistence are not applicable to bands restricted to stand-alone operation with shared spectrum channel access as identified in Table 5.2-1.

## 6.5E.3F.2.1Spurious emissions for UE co-existence for SL-U concurrent operation

For NR SL-U inter-band concurrent operation, the UE-coexistence requirements in Table 6.5A.3.2.3-1 apply for the corresponding inter-band concurrent operation with transmission assigned to both uplink in licensed band and NR sidelink in unlicensed band.

## 6.5E.3F.3Additional spurious emissions

## 6.5E.3F.3.0General

These requirements are specified in terms of an additional spectrum emission requirement. Additional spurious emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

Editor’s note: Further new NS values with new requirements can be added here.

## 6.5E.4Transmit intermodulation

## 6.5E.4.1General

When UE is configured for NR V2X sidelink transmissions non-concurrent with NR uplink transmissions for NR V2X operating bands specified in Table 5.2E.1-1, the requirements in clause 6.5.4 apply for NR V2X sidelink transmission.

For NR V2X UE with two transmit antenna connectors, the requirements specified for single carrier shall apply to each transmit antenna connector.

## 6.5E.4.1ATransmit intermodulation for sidelink CA

For SL intra-band contiguous CA, the general NR CA Transmit Intermodulation requirements for CA Bandwidth Class B specified in clause 6.5A.4.2.1 shall be applied to the aggregated channel bandwidth with SL CA bandwidth class B.

## 6.5E.4.2Transmit intermodulation for V2X concurrent operation

For the inter-band concurrent NR V2X operation, the requirements specified in clause 6.5.4 shall apply for the uplink in licensed band and the requirements specified in clause 6.5E.4.1 shall apply for the sidelink in licensed band or Band n47.

For the intra-band NR V2X operation where Uu and SL transmission overlaps in time, the requirements specified in clause 6.5A.4 shall apply for both uplink and sidelink in licensed band.

6.5E.4FTransmit intermodulation for sidelink Unlicensed

The requirements for transmit intermodulation in clause 6.5.4 apply for SL-U operation.

6.5E.4F.1Transmit intermodulation for SL-U concurrent operation

For NR-U SL inter-band concurrent operation, the requirements specified in clause 6.5.4 shall apply for NR Uu operation in licensed band and the requirements specified in clause 6.5E.4F shall apply for NR sidelink operation in unlicensed band.

## 6.5FOutput RF spectrum emissions for shared spectrum channel access

## 6.5F.1Occupied bandwidth

The requirements for occupied bandwidth in clause 6.5.1 apply for the specified NR-U channel bandwidths in Table 5.3.5-1.

## 6.5F.2Out of band emission

## 6.5F.2.1General

The Out of band emissions are unwanted emissions immediately outside the assigned channel bandwidth resulting from the modulation process and non-linearity in the transmitter but excluding spurious emissions. This out of band emission limit is specified in terms of a spectrum emission mask and an adjacent channel leakage power ratio.

To improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.5F.2.2Spectrum emission mask for operation with shared spectrum channel access

## 6.5F.2.2.0General

Instead of the general spectrum emission mask requirement in clause 6.5.2.2, when operating with shared spectrum channel access the relative power of any UE emission shall not exceed the levels specified in Table 6.5F.2.2.0-1 for the specified channel bandwidth or -30 dBm/MHz whichever is the greatest. The spectrum emission mask for operation with shared spectrum channel access is defined relative to the maximum power density in a 1 MHz measurement bandwidth within the channel bandwidth.

The spectrum emission mask for operation with shared spectrum channel access applies to frequencies (ΔfOOB) starting from the  edge of the assigned channel bandwidth. For offsets greater than ΔfOOB, the spurious requirements in clause 6.5.3 are applicable.

Table 6.5F.2.2.0-1: Spectrum emission mask for operation with shared spectrum channel access

For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2.

## 6.5F.2.2.1Spectrum emission mask for non-transmitted channels

In the case of non-transmitted 20 MHz channel(s) on the edges of an assigned channel bandwidth the spectrum emission mask for operation with shared spectrum channel access, specified in Table 6.5F.2.2.0-1, is applied by using the total bandwidth of the remaining transmitted channels. The spectrum emission mask for non-transmitted channels is floored at -28dBr.

The relative power of any UE emission shall not exceed the most stringent levels given by the spectrum emission mask for operation with shared spectrum channel access with full channel bandwidth and the spectrum emission mask for non-transmitted channels with the channel bandwidth of the transmitted channels in the case of non-transmitted channels at the edge of an assigned channel bandwidth.

An exception to the spectrum emission mask for non-transmitted channels allows a single [2] MHz bandwidth to extend to [-28] dBc relative to total transmit power, or [-20] dBm, whichever is the greatest.

## 6.5F.2.3Additional spectrum emission mask

There are no additional spectrum emission mask requirements in this version of the specification.

## 6.5F.2.4Adjacent channel leakage ratio

## 6.5F.2.4.0General

Adjacent Channel Leakage power Ratio (ACLR) is the ratio of the filtered mean power centred on the assigned channel frequency to the filtered mean power centred on an adjacent channel frequency.

To improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

## 6.5F.2.4.1Shared spectrum channel access ACLR

The Adjacent Channel Leakage power Ratio is the ratio of the filtered mean power centred on the assigned channel frequency to the filtered mean power centred on an adjacent channel frequency at nominal channel spacing.  The assigned channel power and adjacent channel power are measured with rectangular filters with measurement bandwidths specified in Table 6.5.2.4.1-1.

Instead of the general ACLR requirement in clause 6.5.2.4, if the measured adjacent channel power is greater than –47 dBm then the ACLR shall be higher than the value specified in Table 6.5F.2.4.1-1.

Table 6.5F.2.4.1-1: Shared spectrum channel access ACLR requirement

## 6.5F.2.4.2Additional requirement for network signalled value "NS_29"

When "NS_29" is indicated in the cell, the UE emission shall meet the additional requirements specified in Table 6.5F.2.4.2-1 for shared spectrum channels assigned within 5150 – 5350 MHz and 5470 – 5730 MHz.

Table 6.5F.2.4.2-1: ACLR2 requirement for "NS_29"

## 6.5F.2AOut of band emission for CA

## 6.5F.2A.1Spectrum emission mask for CA

## 6.5F.2A.1.1Spectrum emission mask for Inter-band CA

For inter-band carrier aggregation with uplink assigned to two bands and including one of the bands listed in Table 6.2F.1-1, the spectrum emission mask requirements in clause 6.5.2.1 and 6.5.2.2 apply for the NR uplink carrier and clause 6.5F.2.1 and 6.5F.2.2 for the carrier operating with shared spectrum access.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per operating band and including one of the bands listed in Table 6.2F.1-1), the spectrum emission mask of the UE is defined per band while all component carriers are active. For the NR band supporting two contiguous component carriers the requirements specified in subclause 6.5A.2.2.1 apply. For the shared spectrum defined band supporting one component carrier the requirements in subclauses 6.5F.2.2 apply.

## 6.5F.2A.1.2Spectrum emission mask for Intra-band contiguous CA

## 6.5F.2A.1.2.1General

For intra-band contiguous carrier aggregation operation with shared spectrum channel access, the relative power of any UE emission shall not exceed the levels specified in Table 6.5F.2A.1.1-1 for the specified aggregated channel bandwidth or -30 dBm/MHz whichever is the greatest. The spectrum emission mask for operation with shared spectrum channel access is defined relative to the maximum power density in a 1 MHz measurement bandwidth within the aggregated channel bandwidth.

The spectrum emission mask for operation with shared spectrum channel access applies to frequencies (ΔfOOB) starting from the  edge of the assigned aggregated channel bandwidth. For frequencies offsets greater than ΔfOOB, the spurious requirements in clause 6.5.3 are applicable.

Table 6.5F.2A.1.2-1: Spectrum emission mask for intra-band contiguous CA operation with shared spectrum channel access

For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2.

## 6.5F.2A.1.2.2Intra-band contiguous CA spectrum emission mask for non-transmitted channels

In the case of non-transmitted 20 MHz channel(s) on the edges of an assigned aggregated channel bandwidth, the spectrum emission mask for operation with shared spectrum channel access specified in Table 6.5F.2A.1.2-1 is applied by using the total bandwidth of the remaining transmitted channels. The spectrum emission mask for non-transmitted channels is floored at -28dBr.

The relative power of any UE emission shall not exceed the most stringent levels given by the spectrum emission mask for operation with shared spectrum channel access with full aggregated channel bandwidth, and the spectrum emission mask for non-transmitted channels with the channel bandwidth of the transmitted channels in the case of non-transmitted channels at the edge of an assigned aggregated channel bandwidth.

An exception to the spectrum emission mask for non-transmitted channels allows a single [2] MHz bandwidth to extend to [-28] dBc relative to total transmit power, or [-20] dBm, whichever is the greatest.

## 6.5F.2A.2Adjacent channel leakage ratio for CA

## 6.5F.2A.2.1Adjacent channel leakage ratio for inter-band CA

For inter-band carrier aggregation with uplink assigned to two bands and including one of the bands listed in Table 6.2F.1-1, the ACLR requirements in clause 6.5.2.4 apply for the NR uplink carrier and clause 6.5F.2.4 for the carrier operating with shared spectrum access.

For combinations of intra-band and inter-band carrier aggregation with three uplink component carriers (up to two contiguously aggregated carriers per operating band and including one of the bands listed in Table 6.2F.1-1). For the NR band supporting two contiguous component carriers, the requirements in subclause 6.5A.2.4.1.1 apply. For the shared spectrum defined band supporting one component carrier, the requirements in subclause 6.5F.2.4.1 apply.

## 6.5F.2A.2.2Adjacent channel leakage ratio for intra-band contiguous CA

For intra-band contiguous carrier aggregation, the Carrier Aggregation Adjacent Channel Leakage Power Ratio (CAACLR) is the ratio of the filtered mean power centred on the aggregated channel bandwidth to the filtered mean power centred on an adjacent aggregated channel bandwidth at nominal channel spacing. The assigned aggregated channel bandwidth power and adjacent aggregated channel bandwidth power are measured with rectangular filters with measurement bandwidths specified in Table 6.5F.2A.2.2-1. If the measured adjacent channel power is greater than -47dBm then the ACLR shall be higher than the value specified in Table 6.5F.2A.2.2-1.

Table 6.5F.2A.2.2-1: General requirements for intra-band contiguous CA ACLR power class 5

## 6.5F.3Spurious emissions

## 6.5F.3.0General

Spurious emissions are emissions which are caused by unwanted transmitter effects such as harmonics emission, parasitic emissions, intermodulation products and frequency conversion products, but exclude out of band emissions unless otherwise stated. The spurious emission limits are specified in terms of general requirements in line with SM.329 [9] and NR operating band requirement to address UE co-existence.

To improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

## 6.5F.3.1General spurious emissions

The requirements for general spurious emission requirements in clause 6.5.3.1 apply.

## 6.5F.3.2Spurious emissions for UE co-existence

Spurious emissions requirements for UE coexistence are not applicable to bands restricted to stand-alone operation with shared spectrum channel access as identified in Table 5.2-1.

## 6.5F.3.3Additional spurious emissions

## 6.5F.3.3.0General

These requirements are specified in terms of an additional spectrum emission requirement. Additional spurious emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

## 6.5F.3.3.1Requirement for network signalling value "NS_28"

When "NS_28" is indicated in the cell, the power of any UE emission for channels assigned within 5150-5350 and 5470-5725 MHz shall not exceed the levels specified in Table 6.5F.3.3.1-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5F.3.3.1-1: Additional requirements

## 6.5F.3.3.2Requirement for network signalling value "NS_29"

When "NS_29" is indicated in the cell, the power of any UE emission for channels assigned within 5150-5350 and 5470-5730 MHz shall not exceed the levels specified in Table 6.5F.3.3.2-1, Table 6.5F.3.3.2-2, and Table 6.F.3.3.2-3. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5F.3.3.2-1: Additional requirements for 20 MHz channel bandwidth

Table 6.5F.3.3.2-2: Additional requirements for 40 MHz channel bandwidth

Table 6.5F.3.3.2-3: Additional requirements for 60 and 80 MHz channel bandwidth

## 6.5F.3.3.3Requirement for network signalling value "NS_30"

When "NS_30" is indicated in the cell, the power of any UE emission for channels assigned within 5150-5350 MHz, 5470-5725 MHz and 5725-5850 MHz shall not exceed the levels specified in Table 6.5F.3.3.3-1-1, Table 6.5F.3.3.3-1-2 and Table 6.5F.3.3.3-1-3, respectively. These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5F.3.3.3-1: Additional requirements for shared access channels assigned within 5150-5350 MHz

Table 6.5F.3.3.3-2: Additional requirements for shared access channels assigned within 5470-5725 MHz

Table 6.5F.3.3.3-3: Additional requirements for shared access channels assigned within 5725-5850 MHz

## 6.5F.3.3.4Requirement for network signalling value "NS_31"

When "NS_31" is indicated in the cell, the power of any UE emission for channels assigned within 5150-5250 MHz, 5250-5350 MHz, 5470-5725 MHz and 5725-5850 MHz shall not exceed the levels specified in Table 6.5F.3.3.4-1, Table 6.5F.3.3.4-2, Table 6.5F.3.3.4-3 and Table 6.5F.3.3.4-4, respectively. These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5F.3.3.4-1: Additional requirements for NR-U channels assigned within 5150-5250 MHz

Table 6.5F.3.3.4-2: Additional requirements for NR-U channels assigned within 5250-5350 MHz

Table 6.5F.3.3.4-3: Additional requirements for NR-U channels assigned within 5470-5725 MHz

Table 6.5F.3.3.4-4: Additional requirements for NR-U channels assigned within 5725-5850 MHz

## 6.5F.3.3.5Requirements for network signalling value "NS_53" or "NS_54" or "NS_60" or "NS_66" or "NS_67" or "NS_71"

When "NS_53" or "NS_54" or "NS_60" or "NS_66" or "NS_67" or "NS_71" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5F.3.3.5-1. These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5F.3.3.5-1: Additional requirements

## 6.5F.3.3.6Requirements for network signalling value "NS_58"

When "NS_58" is indicated in the cell, the power of any UE emission for channels assigned within 5945-6425 MHz shall not exceed the levels specified in Table 6.5F.3.3.6-1. These requirements also apply for frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5F.3.3.6-1: Additional requirements

## 6.5F.3.3.7Requirements for network signalling value "NS_61"

When "NS_61" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5F.3.3.7-1. These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5F.3.3.7-1: Additional requirements

## 6.5F.3.3.8Requirements for network signalling value “NS_63” or “NS_69”

When "NS_63" or “NS_69” is indicated in the cell, the power of any UE emission for channels assigned within 5945-6425 MHz shall not exceed the levels specified in Table 6.5F.3.3.8-1. These requirements also apply for frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5F.3.3.8-1: Additional requirements

ACLR is specified for the first adjacent channel (ACLR1) which centre frequency is ±CBW from assigned channel centre and for the 2nd adjacent channel (ACLR2) which centre frequency is ±2*CBW from assigned channel centre. The assigned channel power and ACLR1/ACLR2 are measured with rectangular filters with measurement bandwidth of CBW.

Instead of the general ACLR requirement in clause 6.5.2.4 and 6.5F.2.4.1, if the measured adjacent channel power is greater than –47 dBm then the ACLR shall be higher than the value specified in Table 6.5F.3.3.10-2.

Table 6.5F.3.3.10-2: Shared spectrum channel access ACLR requirement

## 6.5F.3.3.9Requirements for network signalling value “NS_64”

When "NS_64" is indicated in the cell, the power of any UE emission for channels assigned within 5945-6425 MHz shall not exceed the levels specified in Table 6.5F.3.3.9-1. These requirements also apply for frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5F.3.3.9-1: Additional requirements

## 6.5F.3ASpurious emissions for CA

## 6.5F.3A.0General

To improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

NOTE:For measurement conditions at the edge of each frequency range, the lowest frequency of the measurement position in each frequency range should be set at the lowest boundary of the frequency range plus MBW/2. The highest frequency of the measurement position in each frequency range should be set at the highest boundary of the frequency range minus MBW/2. MBW denotes the measurement bandwidth defined for the protected band.

## 6.5F.3A.1General spurious emissions

For intra-band contiguous carrier aggregation, the spurious emission limits apply for the frequency ranges that are more than FOOB (MHz) in Table 6.5F.3A.1-1 from the edge of the aggregated channel bandwidth. For frequencies ΔfOOB greater than FOOB as specified in Table 6.5F.3A.1-1 the spurious emission requirements in Table 6.5.3.1-2 are applicable.

Table 6.5F.3A.1-1: Boundary between out of band and spurious emission domain for intra-band contiguous carrier aggregation

## 6.5F.3A.2Spurious emissions for UE co-existence

Spurious emissions requirements for UE coexistence are not applicable to bands restricted to stand-alone operation with shared spectrum channel access as identified in Table 5.2-1.

## 6.5F.3A.3Additional spurious emissions

## 6.5F.3A.3.0General

These requirements are specified in terms of an additional spectrum emission requirement. Additional spurious emission requirements are signalled by the network to indicate that the UE shall meet an additional requirement for a specific deployment scenario as part of the cell handover/broadcast message.

## 6.5F.3A.3.1Requirements for network signalling value "CA_NS_53" or "CA_NS_54"

When "CA_NS_53" or "CA_NS_54" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5F.3A.3.1-1. These requirements also apply for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the aggregated channel bandwidth.

Table 6.5F.3A.3.1-1: Additional requirements

## 6.5F.4Transmit intermodulation

The requirements for transmit intermodulation in clause 6.5F.4 apply.

## 6.5GOutput RF spectrum emissions for Tx Diversity

## 6.5G.1Occupied bandwidth for Tx Diversity

For UE supporting Tx diversity, the requirements for occupied bandwidth apply to the transmitted spectrum as measured as the sum of the power from all UE transmit antenna connectors. The occupied bandwidth is defined as the bandwidth containing 99 % of the total integrated mean power of the transmitted spectrum on the assigned channel at each transmit antenna connector.

## 6.5G.2Out of band emission for Tx Diversity

For UE supporting Tx diversity, the requirements for Out of band emissions resulting from the modulation process and non-linearity in the transmitters apply to the sum of the emissions from all UE transmit antenna connectors.

If UE indicates Tx diversity capability, Adjacent Channel Leakage power Ratio (ACLR) is defined as the ratio of sum of the filtered mean power at each antenna connector centred on the assigned channel frequency to sum of the filtered mean power at each antenna connector centred on an adjacent channel frequency.

The requirements specified in clause 6.5.2 apply.

## 6.5G.3Spurious emission for Tx Diversity

For UE supporting Tx diversity, the requirements for Spurious emissions which are caused by unwanted transmitter effects such as harmonics emission, parasitic emissions, intermodulation products and frequency conversion products apply to the sum of the emissions from all UE transmit antenna connectors.

The requirements specified in clause 6.5.3 apply.

## 6.5G.4Transmit intermodulation for Tx Diversity

For UE supporting Tx diversity, the transmit intermodulation requirements are specified at each transmit antenna connector and the wanted signal is defined as the sum of output power from all UE transmit antenna connectors.

The requirements specified in clause 6.5.4 apply.

## 6.5HOutput RF spectrum emissions for CA with UL MIMO

## 6.5H.1Output RF spectrum emissions for intra-band UL contiguous CA with UL MIMO

## 6.5H.1.1Occupied bandwidth for intra-band UL contiguous CA with UL MIMO

For UE supporting intra-band UL contiguous CA and UL MIMO, the requirements for occupied bandwidth specified in clause 6.5A.1.1a apply to the sum of the powers from both UE transmit antenna connectors and all UL CCs. The requirements shall be met with UL MIMO configurations described in Table 6.2D.1-2.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.5A.1.1a apply.

## 6.5H.1.2Out of band emission for intra-band UL contiguous CA with UL MIMO

For UE supporting intra-band UL contiguous CA and UL MIMO, the requirements for Out of band emissions resulting from the modulation process and non-linearity in the transmitters is defined as the sum of the emissions from both UE transmit antenna connectors and all UL CCs, the requirements in subclause 6.5A.2.2.1, 6.5A.2.3.1 and 6.5A.2.4.1.1 apply. The requirements shall be met with UL MIMO configurations described in Table 6.2D.1-2.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.5A.2.2.1, 6.5A.2.3.1 and 6.5A.2.4.1.1 apply.

## 6.5H.1.3 Spurious emission for intra-band UL contiguous CA with UL MIMO

For UE supporting intra-band UL contiguous CA and UL MIMO, the requirements for Spurious emissions is defined as the sum of the emissions from both UE transmit antenna connectors and all UL CCs, the requirements specified in subclauses 6.5A.3.1, 6.5A.3.2.1 and 6.5A.3.3.1 apply. The requirements shall be met with the UL MIMO configurations described in Table 6.2D.1-2.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.5A.3.1, 6.5A.3.2.1 and 6.5A.3.3.1 apply.

## 6.5H.1.4Transmit intermodulation for intra-band UL contiguous CA with UL MIMO

For UE supporting intra-band UL contiguous CA and UL MIMO, the transmit intermodulation requirements are specified at each transmit antenna connector and the wanted signal is defined as the sum of output powers from both UE transmit antenna connectors, the requirements specified in clause 6.5A.4.2.1 apply. The requirements shall be met with the UL MIMO configurations described in Table 6.2D.1-2.

If UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.5A.4.2.1 apply.

## 6.5H.2Void

## 6.5H.3Output RF spectrum emissions for inter-band UL CA with UL MIMO

## 6.5H.3.1Occupied bandwidth for inter-band UL CA with UL MIMO

For inter-band UL CA with UL MIMO in one of the two frequency bands, the occupied bandwidth is defined per component carrier. The requirement specified in clause 6.5.1 shall apply for the component carrier without UL MIMO and the requirement specified in clause 6.5D.1 shall apply for the component carrier configured with UL MIMO.

## 6.5H.3.2Out of band emission for inter-band UL CA with UL MIMO

For inter-band UL CA with UL MIMO in one of the two frequency bands, the out of band emission requirement is defined per component carrier while both component carriers are active. The requirements specified in clauses 6.5.2.1 and 6.5.2.2 shall apply for the component carrier without UL MIMO and the requirements specified in clause 6.5D.2 shall apply for the component carrier configured with UL MIMO. If for some frequency spectrum emission masks of component carriers overlap, then spectrum emission mask allowing higher power spectral density applies for that frequency. If for some frequency a component carrier spectrum emission mask overlaps with the channel bandwidth of another component carrier, then the emission mask does not apply for that frequency.

## 6.5H.3.3Spurious emission for inter-band UL CA with UL MIMO

For inter-band UL CA with UL MIMO in one of the two frequency bands, the general spurious emission requirements in Table 6.5.3.1-2 apply for the frequency ranges that are more than FOOB as defined in Table 6.5.3.1-1 away from edges of the assigned channel bandwidth on a component carrier. The spurious emission requirements for co-existence in Table 6.5A.3.2.3-1 apply with all component carriers are active.

## 6.5H.3.4Transmit intermodulation for inter-band UL CA with UL MIMO

For inter-band UL CA with UL MIMO in one of the two frequency bands, the transmit intermodulation requirement specified in clause 6.5.4 shall apply for the component carrier without UL MIMO and the transmit intermodulation requirement specified in Table 6.5D.4 shall apply for the component carrier configured with UL MIMO with all component carriers active.

## 6.5I(Reserved)

## 6.5JOutput RF spectrum emissions for ATG

## 6.5J.1Occupied bandwidth for ATG

The requirements for occupied bandwidth in clause 6.5.1 apply. For ATG UE, the requirements for occupied bandwidth are defined at each transmit antenna connector or each TAB connector.

## 6.5J.1DOccupied bandwidth for ATG UL MIMO

For ATG UE supporting UL MIMO, the requirements for occupied bandwidth apply to the sum of the powers from all UE transmit antenna connectors or all UE TAB connectors. The occupied bandwidth is defined as the bandwidth containing 99 % of the total integrated mean power of the transmitted spectrum on the assigned channel at each transmit antenna connector or each TAB connector.

For ATG UE with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer) in closed-loop spatial multiplexing scheme, the occupied bandwidth shall be less than the channel bandwidth specified in Table 6.5.1-1. The requirements shall be met with UL MIMO configurations described in clause 6.2J.1D.

If ATG UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.5J.1 apply when TxD is not indicated.

## 6.5J.2Out of band emission for ATG

## 6.5J.2.1General

This clause contains requirements for out of band emissions for ATG UE, the requirement defined in general part of clause 6.5.2.1 should apply.

## 6.5J.2.2Spectrum emission mask

If the actual transmission power of ATG UE is less than or equal to 31dBm, the requirements for spectrum emission mask in clause 6.5.2.2 apply; if the actual transmission power of ATG UE is larger than 31dBm, the requirements of spectrum emission mask in clause 6.5.2.2 shall be relaxed with scaling factor equal to (the actual transmission power minus 31) dB. For ATG UE, the requirements for spectrum emission mask are defined as the sum of the emissions from all UE transmit antenna connectors or all TAB connectors.

NOTE:This scaling factor is only applicable to ATG airborne UE.

## 6.5J.2.3Adjacent channel leakage ratio

NR Adjacent Channel Leakage power Ratio (NRACLR) is the ratio of the filtered mean power centred on the assigned NR channel frequency to the filtered mean power centred on an adjacent NR channel frequency at nominal channel spacing. For ATG UE, the requirements for ACLR are defined as the sum of the emissions from all UE transmit antenna connectors or all TAB connectors.

The assigned NR channel power and adjacent NR channel power are measured with rectangular filters with measurement bandwidths specified in Table 6.5J.2.3-1.

If the measured adjacent channel power is greater than –50 dBm then the NRACLR shall be higher than the value 30dBc.

Table 6.5J.2.3-1: NR ACLR measurement bandwidth

## 6.5J.2DOut of band emission for ATG with UL MIMO

For ATG UE supporting UL MIMO or uplink full power transmission (ULFPTx) for UL MIMO, the requirements for Out of band emissions resulting from the modulation process and non-linearity in the transmitters is defined as the sum of the emissions from all transmit antenna connectors or all TAB connectors.

For ATG UEs with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer) in closed-loop spatial multiplexing scheme, the requirements in subclause 6.5J.2 apply. The requirements shall be met with UL MIMO configurations described in clause 6.2J.1D.

For ATG UE support uplink full power transmission (ULFPTx) for UL MIMO, the requirements in clause 6.5J.2 shall apply. The requirements shall be met with the PUSCH configurations specified in Table 6.2J.1D-2, based upon UE’s support of uplink full power transmission mode.

If ATG UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.5J.2 apply when TxD is not indicated.

## 6.5J.3Spurious emissions for ATG

The requirements for spurious emission in general part of clause 6.5.3.0 and clause 6.5.3.1 apply. For ATG UE, the requirements for Spurious emissions are defined as the sum of the emissions from all UE transmit antenna connectors or all TAB connectors.

## 6.5J.3DSpurious emissions for ATG with UL MIMO

For ATG UE supporting UL MIMO or uplink full power transmission (ULFPTx) for UL MIMO, the requirements for Spurious emissions which are caused by unwanted transmitter effects such as harmonics emission, parasitic emissions, intermodulation products and frequency conversion products is defined as the sum of the emissions from all transmit antenna connectors or all TAB connectors.

For ATG UEs with two transmit antenna connectors or two groups of TAB connectors (each of which supporting one layer) in closed-loop spatial multiplexing scheme, the requirements specified in subclause 6.5J.3 apply. The requirements shall be met with the UL MIMO configurations described in clause 6.2J.1D.

For ATG UE support uplink full power transmission (ULFPTx) for UL MIMO, the requirements in clause 6.5J.3 shall apply. The requirements shall be met with the PUSCH configurations specified in Table 6.2J.1D-2, based upon UE’s support of uplink full power transmission mode.

If ATG UE is scheduled for single antenna-port PUSCH transmission by DCI format 0_0 or by DCI format 0_1 for single antenna port codebook based transmission with precoding matrix W=1 [6.3.1.5 TS 38.211], the requirements in clause 6.5J.3 apply when TxD is not indicated

## 6.5KOutput RF spectrum emissions for Aerial UE

## 6.5K.1Occupied bandwidth for Aerial UE

For Aerial UE, the requirements specified in clause 6.5.1 apply.

## 6.5K.2Out of band emission for Aerial UE

For Aerial UE, the requirements specified in clause 6.5.2 apply.

## 6.5K.3Spurious emissions for Aerial UE

## 6.5K.3.0General

For Aerial UE, the requirements specified in clause 6.5.3.0 apply.

## 6.5K.3.1General spurious emissions

For Aerial UE, the requirements specified in clause 6.5.3.1 apply.

## 6.5K.3.2Spurious emissions for UE co-existence

For Aerial UE, the requirements specified in clause 6.5.3.2 apply.

## 6.5K.3.3Additional spurious emissions

## 6.5K.3.3.1Requirement for network signalling value "NS_UAV_44"

When "NS UAV_44" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5K.3.3.1-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5K.3.3.1-1: Additional requirements for "NS_UAV_44"

## 6.5K.3.3.2Requirement for network signalling value "NS_UAV_46"

When "NS_UAV_46" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5K.3.3.2-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5K.3.3.2-1: Additional requirements for "NS_UAV_46"

## 6.5K.3.3.3Requirement for network signalling value “NS_UAV_70"

When "NS UAV_70" is indicated in the cell, the power of any UE emission shall not exceed the levels specified in Table 6.5K.3.3.3-1. This requirement also applies for the frequency ranges that are less than FOOB (MHz) in Table 6.5.3.1-1 from the edge of the channel bandwidth.

Table 6.5K.3.3.3-1: Additional requirements for "NS_UAV_70"

## 6.5LOutput RF spectrum emissions for CA with Tx Diversity

## 6.5L.1Void

## 6.5L.2Void

## 6.5L.3Output RF spectrum emissions for inter-band UL CA with Tx Diversity

## 6.5L.3.1Occupied bandwidth for inter-band UL CA with Tx Diversity

For inter-band UL CA with Tx Diversity in one of the two frequency bands, the occupied bandwidth is defined per component carrier. The requirement specified in clause 6.5.1 shall apply for the component carrier without Tx Diversity and the requirement specified in clause 6.5G.1 shall apply for the component carrier configured with Tx Diversity.

## 6.5L.3.2Out of band emission for inter-band UL CA with Tx Diversity

For inter-band UL CA with Tx Diversity in one of the two frequency bands, the out of band emission requirement is defined per component carrier while both component carriers are active. The requirements specified in clauses 6.5.2.1 and 6.5.2.2 shall apply for the component carrier without Tx Diversity and the requirements specified in clause 6.5G.2 shall apply for the component carrier configured with Tx Diversity. If for some frequency spectrum emission masks of component carriers overlap, then spectrum emission mask allowing higher power spectral density applies for that frequency. If for some frequency a component carrier spectrum emission mask overlaps with the channel bandwidth of another component carrier, then the emission mask does not apply for that frequency.

## 6.5L.3.3Spurious emission for inter-band UL CA with Tx Diversity

For inter-band UL CA with Tx Diversity in one of the two frequency bands, the general spurious emission requirements in Table 6.5.3.1-2 apply for the frequency ranges that are more than FOOB as defined in Table 6.5.3.1-1 away from edges of the assigned channel bandwidth on a component carrier. The spurious emission requirements for co-existence in Table 6.5A.3.2.3-1 apply with all component carriers are active.

## 6.5L.3.4Transmit intermodulation for inter-band UL CA with Tx Diversity

For inter-band UL CA with Tx Diversity in one of the two frequency bands, the transmit intermodulation requirement specified in clause 6.5.4 shall apply for the component carrier without Tx Diversity and the transmit intermodulation requirement specified in Table 6.5G.4 shall apply for the component carrier configured with Tx Diversity with all component carriers active.

## 6.6Void

## 6.6ETime alignment error

For V2X UE(s) with two transmit antenna connectors in SL MIMO, this requirement applies to slot timing differences between transmissions on two transmit antenna connectors. The Time Alignment Error (TAE) shall not exceed 260 ns.
