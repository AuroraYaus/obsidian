---
type: spec
aliases:
  - 38.133_38133-j50_s12-13
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_s12-13/content.md"
---
# TS 38.133 38133-j50_s12-13

## 12V2X Requirements

## 12.1Introduction

This clause contains the requirements for the UE capable of V2X sidelink communication when the UE is out of coverage on the carrier used for V2X sidelink operation, as defined in TS 38.304 [1]. The requirements apply when the UE is:

-in any cell selection state, or any of the below applies:

-configured for V2X SL operation on a V2X carrier which is dedicated to only V2X SL operation and configured with only a PCell on WAN carrier,

-configured for SL operation on a sidelink carrier with CCA and configured with only a PCell on WAN carrier,

-configured for inter-band con-current V2X operation,

-configured for intra-band con-current V2X operation with different carriers,

-configured in co-channel coexistence for LTE SL and NR SL operation with same carrier.

NOTE:Any cell selection state refers to a UE that is out of network coverage and is not associated with a serving cell on any carrier as defined in TS 38.304 [1].

NOTE:When a UE in RRC_CONNECTED state is performing transmissions and/or reception for V2X sidelink communication, the UE shall meet all the requirements specified in Clause 9 assuming that UE has a dedicated RX/TX chain for V2X sidelink communication. Otherwise, the UE may interrupt the V2X sidelink communication in order to meet the measurement requirements specified in Clause 9.

This clause also contains the requirements for the UE capable of V2X sidelink communication when the UE is in coverage on the carrier used for V2X sidelink operation, as defined in TS 38.304 [1]. The requirements apply when the UE is:

-configured for intra-band con-current NR V2X cooperation with same carrier.

-configured in co-channel coexistence for LTE SL and NR SL operation with same carrier，

For UE capable of Public Safety sidelink communication and/or other commercial sidelink communication, unless explicitly stated, V2X requirements apply.

For sidelink communication in unlicensed spectrum,

-the term SyncRef UE subject to CCA is not available at the UE refers to when all the candidate S-SSB positions monitored in every S-SSB period are not available during the last 1280 ms. Otherwise, the SyncRef UE subject to CCA is considered as available at the UE.

-the term S-SSB period subject to CCA is not available at the UE refers to the S-SSB period in which all the candidate S-SSB positions are not available. Otherwise, the S-SSB period subject to CCA is considered as available at the UE.

## 12.2UE Transmit Timing

## 12.2.1Introduction

This clause contains requirements of transmission timing for V2X sidelink communication when:

-GNSS is used as the synchronization reference source;

-NR Cell is used as the synchronization reference source;

-E-UTRAN Cell is used as the synchronization reference source;

-SyncRef UE is used as the synchronization reference source.

The requirements for 60 kHz SCS of sidelink signal defined in this clause do not apply to the sidelink communication in unlicensed spectrum.

## 12.2.2GNSS as synchronization reference source

The requirements in this subclause are applicable when the reference timing used by the UE for V2X sidelink communication is derived from GNSS.

The sidelink transmissions takes place  before the subframe starting boundary as defined in TS 38.331 [2], where  = 0 and=0.

The transmission timing error for sidelink transmissions shall be less than or equal to Te where the timing error limit value Te is defined in table 12.2.2-1.

Table 12.2.2-1: Te Timing Error Limit

## 12.2.3NR Cell as synchronization reference source

The requirements in this subclause are applicable when the reference timing used for sidelink transmissions is a NR serving cell on a non-V2X sidelink carrier or a V2X sidelink carrier.

The sidelink transmissions takes place  before the reception of the first detected path (in time) of the corresponding downlink frame from the reference cell, where  = 0. If uplink transmission and sidelink transmission are in the same band,  is defined in table 7.1.2-2, otherwise  is 0.

The transmission timing error for sidelink transmissions shall be less than or equal to Te where the timing error limit value Te is defined in table 12.2.3-1.

Table 12.2.3-1: Te Timing Error Limit

## 12.2.4E-URTAN Cell as synchronization reference source

The requirements in this subclause are applicable when the reference timing used for sidelink transmissions is an E-UTRAN serving cell on a non-V2X sidelink carrier.

The sidelink transmissions takes place  before the reception of the first detected path (in time) of the corresponding E-UTRAN downlink frame from the reference cell, where  = 0 and=0.

The transmission timing error for sidelink transmissions shall be less than or equal to Te where the timing error limit value Te is defined in table 12.2.4-1.

Table 12.2.4-1: Te Timing Error Limit

## 12.2.5SyncRef UE as synchronization reference source

The requirements in this subclause are applicable when the reference timing used for deriving sidelink transmission is from SyncRef UE transmitting sidelink synchronization signals.

The sidelink transmissions takes place  before the reception of the first detected path (in time) of the corresponding timing reference frame from the SyncRef UE, where  = 0 and=0.

The transmission timing error for sidelink transmissions shall be less than or equal to Te where the timing error limit value Te is defined in table 12.2.5-1.

Table 12.2.5-1: Te Timing Error Limit

If the UE uses SyncRefUE on a carrier frequency subject to CCA for deriving the UE transmit timing, then the UE shall meet all the transmit timing requirements defined in clause 12.2.5: The transmission timing error for sidelink transmissions shall be less than or equal to Te where the timing error limit value Te is defined in table 12.2.5-1 provided that at least one S-SSB is available at the UE during the last 160 ms.

## 12.3Initiation/Cease of SLSS Transmissions

## 12.3.1Introduction

The requirements in this subclause are applicable to the UE capable of V2X sidelink communication when:

-GNSS is used as the synchronization reference source;

-NR Cell is used as the synchronization reference source;

-EUTRAN Cell is used as the synchronization reference source;

-SyncRef UE is used as the synchronization reference source.

## 12.3.1.1Initiation/Cease of SLSS transmissions with NR cell as synchronization reference source

The requirements apply when the NR Cell is used as synchronization reference source and when the UE is

-out of coverage on the V2X NR sidelink carrier and in coverage with a serving cell on a NR non-V2X sidelink carrier, or

- in coverage with a serving cell on a NR V2X sidelink carrier,

and when the conditions for SLSS transmissions specified in TS 38.331 [2] are met; networkControlledSyncTx is not configured; and syncTxThreshIC is included in SystemInformationBlockType12. The UE shall be capable of measuring the RSRP of the cell used as synchronization reference source to evaluate to initiate/cease SLSS transmissions within Tevaluate,SLSS

where,

-Tevaluate,SLSS is as specified in table 12.3.1.1-1 when UE performs SSB based measurements without measurement gaps.

-Tevaluate,SLSS is as specified in table 12.3.1.1-2 when UE performs SSB based measurements with measurement gaps.

Table 12.3.1.1-1: Tevaluate,SLSS for measurements without measurement gaps when NR cell is used as synchronization reference source (FR1)

Table 12.3.1.1-2: Tevaluate,SLSS for measurements with measurement gaps when NR cell is used as synchronization reference source (FR1)

If higher layer filtering is configured, an additional delay in evaluation to initiate/cease SLSS transmissions can be expected.

For the NR cell as synchronization reference source:

-SS-RSRP related side conditions given in clauses 10.1.2 for FR1, respectively, for a corresponding Band,

-SS-RSRQ related side conditions given in clauses 10.1.7 for FR1, respectively, for a corresponding Band,

-SS-SINR related side conditions given in clauses 10.1.12 for FR1, respectively, for a corresponding Band,

-SSB_RP and SSB Ês/Iot according to annex B.2.2 for a corresponding Band.

## 12.3.1.2Initiation/Cease of SLSS transmissions with EUTRAN cell as synchronization reference source

The requirements apply when the EUTRAN Cell is used as synchronization reference source and when the UE is

-out of coverage on the V2X NR sidelink carrier and in coverage with a serving cell on a LTE non-V2X sidelink carrier,

and when the conditions for SLSS transmissions specified in TS 36.331 [16] are met; networkControlledSyncTx is not configured; and syncTxThreshIC is included in SystemInformationBlockType28. The UE shall be capable of measuring the RSRP of the cell used as synchronization reference source to evaluate to initiate/cease SLSS transmissions within Tevaluate,SLSS

where,

-Tevaluate,SLSS = 0.4 seconds when UE is not configured with DRX.

-Tevaluate,SLSS = as specified in table 12.3.1.2-1 when UE is configured with DRX.

Table 12.3.1.2-1: Tevaluate,SLSS when EUTRAN cell is used as synchronization reference source

If higher layer filtering is configured, an additional delay in evaluation to initiate/cease SLSS transmissions can be expected.

For the cell as synchronization reference source:

-RSRP related side conditions given in TS 36.133[15] clauses 9.1.2.1 and 9.1.2.2 and RSRQ related side conditions given in TS 36.133[15] clause 9.1.5.1 for a corresponding Band are fulfilled,

-SCH_RP and SCH Ês/Iot according to TS 36.133[15] annex B.2.1 for a corresponding Band are fulfilled.

## 12.3.1.3Initiation/Cease of SLSS transmissions with GNSS as synchronization reference source

The requirements apply when GNSS is used as synchronization reference source and when the UE is

-out of coverage on the V2X sidelink carrier and in coverage with a serving cell on a non-V2X sidelink carrier, or

-in coverage with a serving cell on a NR V2X sidelink carrier,

and when the conditions for SLSS transmissions specified in TS 38.331 [2] are met; networkControlledSyncTx is not configured; and syncTxThreshIC is included in SystemInformationBlockType12 in a NR cell.

When the conditions for SLSS transmissions specified in TS 36.331 [16] are met; networkControlledSyncTx is not configured; and syncTxThreshIC is included in SystemInformationBlockType28 in a EUTRAN cell.

The requirements in clause 12.3.1.1 shall apply if the serving cell is a NR cell.

The requirements in clause 12.3.1.2 shall apply if the serving cell is a EUTRAN cell.

## 12.3.1.4Initiation/Cease of SLSS transmissions with SyncRef UE as synchronization reference source

The requirements apply when SyncRef UE is used as synchronization reference source and when the UE is

-in any cell selection state, or

-out of coverage on the V2X sidelink carrier and is associated with a serving cell on a non-V2X sidelink carrier, or

-in coverage with a serving cell on a NR V2X sidelink carrier,

and when the conditions for SLSS transmissions specified in TS 38.331 [2] are met and when SyncRef UE is used as synchronization reference source and if syncTxThreshOoC is included in the preconfigured V2X parameters.

The UE shall be capable of measuring the PSBCH-RSRP of the selected SyncRef UE used as synchronization reference source and evaluate it to initiate/cease SLSS transmissions within Tevaluate,SLSS, as shown in table 12.3.1.4-1.

Table 12.3.1.4-1: Tevaluate,SLSS when SyncRef UE is used as synchronization reference source

If higher layer filtering for PSBCH-RSRP measurements is pre-configured, an additional delay in evaluation to initiate/cease SLSS transmissions can be expected.

For the selected SyncRef UE as defined in TS 38.331 [2] used to derive transmission timing for V2X sidelink communication:

-PSBCH-RSRP related side conditions given in clause 12.4 for a corresponding Band are fulfilled,

-V2X S-SSB_RP and S-SSB Ês/Iot according to annex B. 4 for a corresponding Band are fulfilled.

## 12.3AInitiation/Cease of SLSS Transmissions with CCA

## 12.3A.1Introduction

The requirements in this subclause are applicable to the UE capable of sidelink communication in unlicensed spectrum when:

-GNSS is used as the synchronization reference source;

-NR Cell is used as the synchronization reference source;

-EUTRAN Cell is used as the synchronization reference source;

-SyncRef UE is used as the synchronization reference source on a carrier frequency subject to CCA.

## 12.3A.1.1Initiation/Cease of SLSS transmissions with NR cell as synchronization reference source

The requirements defined in subclause 12.3.1.1 apply when the NR Cell is used as synchronization reference source and when the UE is

-out of coverage on the NR sidelink carrier and in coverage with a serving cell on a NR non- sidelink carrier.

## 12.3A.1.2Initiation/Cease of SLSS transmissions with EUTRAN cell as synchronization reference source

The requirements defined in subclause 12.3.1.2 apply when the EUTRAN Cell is used as synchronization reference source and when the UE is

-out of coverage on the NR sidelink carrier and in coverage with a serving cell on a LTE non-sidelink carrier.

## 12.3A.1.3Initiation/Cease of SLSS transmissions with GNSS as synchronization reference source

The requirements defined in subclause 12.3.1.3 apply when GNSS is used as synchronization reference source and when the UE is

-out of coverage on the sidelink carrier and in coverage with a serving cell on a non-sidelink carrier.

## 12.3A.1.4Initiation/Cease of SLSS transmissions with SyncRef UE as synchronization reference source

The requirements apply when SyncRef UE is used as synchronization reference source and when the UE is

-in any cell selection state, or

-out of coverage on the sidelink carrier and is associated with a serving cell on a non-sidelink carrier.

and when the conditions for SLSS transmissions specified in TS 38.331[2] are met and when SyncRef UE is used as synchronization reference source and if syncTxThreshOoC is included in the preconfigured sidelink parameters.

The UE shall be capable of measuring the PSBCH-RSRP of the selected SyncRef UE used as synchronization reference source and evaluate it to initiate/cease SLSS transmissions within Tevaluate,SLSS_CCA, as shown in table 12.3A.1.4-1 when the SyncRef UE is transmitting S-SSB on a carrier frequency subject to CCA.

Table 12.3A.1.4-1: Tevaluate,SLSS_CCA when SyncRef UE is transmitting S-SSB on a carrier subject to CCA and is used as synchronization reference source

The UE shall initiate the procedure for selection/reselection of different synchronization reference source as defined in TS 38.331 [2] when the requirements cannot be met due to that LSLSS exceeding LSLSS, max during Tevaluate,SLSS_CCA.

If higher layer filtering for PSBCH-RSRP measurements is pre-configured, an additional delay in evaluation to initiate/cease SLSS transmissions can be expected.

For the selected SyncRef UE as defined in TS 38.331 [2] used to derive transmission timing for sidelink communication:

-PSBCH-RSRP related side conditions given in clause 12.4 for a corresponding Band are fulfilled,

-sidelink S-SSB_RP and S-SSB Ês/Iot according to annex B. 4 for a corresponding Band are fulfilled.

## 12.4Selection / Reselection of V2X Synchronization Reference Source

The requirements defined in this clause do not apply to the UEs that do not support transmission and reception of SLSS.

A SyncRef UE is considered to be detectable when

-PSBCH-RSRP related side conditions given in clause 10 are fulfilled for a corresponding Band,

-S-SSB_RP and S-SSB Ês/Iot according to annex B.4.3 for a corresponding Band are fulfilled.

When GNSS synchronization reference source is configured as the highest priority and

-UE is synchronized to GNSS directly,

-UE shall not drop any V2X SLSS and data transmission for the purpose of selection/reselection to the SyncRef UE.

-UE is synchronized to a SyncRef UE that is synchronized to GNSS directly or in-directly,

-UE shall not drop any V2X data transmission for the purpose of selection/reselection to the SyncRef UE. The UE shall be able to identify newly detectable intra-frequency SyncRef UE within Tdetect,SyncRef UE_V2X seconds if the SyncRef UE meets the selection / reselection criterion defined in TS 38.331 [2]. Tdetect,SyncRef UE_V2X is defined as 1.6 seconds at S-SSB Ês/Iot ≥ 0 dB, provided that the UE is allowed to drop a maximum of 30% of its SLSS transmissions during Tdetect,SyncRef UE_V2X for the purpose of selection / reselection to the SyncRef UE.

-in other case

-When UE is in non-SL-DRX

-The UE shall be able to identify newly detectable intra-frequency SyncRef UE within Tdetect,SyncRef UE_V2X seconds if the SyncRef UE meets the selection / reselection criterion defined in TS 38.331 [2]. Tdetect,SyncRef UE_V2X is defined as 8 seconds at S-SSB Ês/Iot ≥ 0 dB, provided that the UE is allowed to drop a maximum of 6 % of its V2X data and SLSS transmissions during Tdetect,SyncRef UE_V2X for the purpose of selection / reselection to the SyncRef UE.

-UE is allowed to drop up to 2 slots of its V2X data reception per PSBCH monitoring occasion and overall drop rate shall not exceed 0.3% of its V2X data reception during Tdetect,SyncRef UE_V2X for the purpose of selection / reselection to the SyncRef UE.

-When UE is in SL-DRX

-UE shall be able to identify newly detectable intra-frequency SyncRef UE within Tdetect,SyncRef UE_V2X seconds if the SyncRef UE meets the selection / reselection criterion defined in TS 38.331 [2]. Tdetect,SyncRef UE_V2X is defined as 8 seconds at S-SSB Ês/Iot ≥ 0 dB, provided that the V2X UE is allowed to drop a maximum of 6 % of its V2X data and SLSS transmissions for the purpose of selection / reselection to the SyncRef UE.

-UE is allowed to drop up to 2 slots of its V2X data reception per PSBCH monitoring occasion and UE is allowed to drop at most an aggregated window of 24 ms of its V2X data reception during Tdetect,SyncRef UE_V2X for the purpose of selection / reselection to the SyncRef UE.

-The UE is allowed to extend Tdetect,SyncRef UE_V2X to max(4 x 50 SL-DRX cycle length, 8 s) when the following conditions are satisfied over an evaluation period Tevaluate,SLSS in clause 12.3.1.1 if an NR cell is used as synchronization reference source, or Tevaluate,SLSS in clause 12.3.1.2 if an EUTRA cell is used as synchronization reference source, or Tevaluate,SLSS in clause 12.3.1.4 if an SLSS is used as synchronization reference source. If multiple SL-DRX cycles are configured, the SL-DRX cycle length is the longest one.

-SS-RSRP is larger than syncTxThreshOoC.

When serving cell/PCell synchronization reference source is configured as the highest priority,

-When UE is in non-SL-DRX

-UE shall be able to identify newly detectable intra-frequency SyncRef UE within Tdetect,SyncRef UE_V2X seconds if the SyncRef UE meets the selection / reselection criterion defined in TS 38.331 [2].  Tdetect,SyncRef UE_V2X is defined as 8  seconds at SCH Es/Iot ≥ 0 dB, provided that the V2X UE is allowed to drop a maximum of 6 % of its V2X data and SLSS transmissions for the purpose of selection / reselection to the SyncRef UE.

-UE is allowed to drop up to 2 slots of its V2X data reception per PSBCH monitoring occasion and overall drop rate shall not exceed 0.3% of its V2X data reception during Tdetect,SyncRef UE_V2X for the purpose of selection / reselection to the SyncRef UE.

-When UE is in SL-DRX

-The UE shall be able to identify newly detectable intra-frequency SyncRef UE within Tdetect,SyncRef UE_V2X seconds if the SyncRef UE meets the selection / reselection criterion defined in TS 38.331 [2]. Tdetect,SyncRef UE_V2X is defined as 8 seconds at SCH Es/Iot ≥ 0 dB, provided that the UE is allowed to drop its V2X data and SLSS transmissions at most in an aggregated window of 480ms during Tdetect,SyncRef UE_V2X for the purpose of selection / reselection to the SyncRef UE.

-UE is allowed to drop up to 2 slots of its V2X data reception per PSBCH monitoring occasion and UE is allowed to drop at most an aggregated window of 24 ms of its V2X data reception during Tdetect,SyncRef UE_V2X for the purpose of selection / reselection to the SyncRef UE.

-The UE is allowed to extend Tdetect,SyncRef UE_V2X to max(4 x 50 SL-DRX cycle length, 8 s) when the following conditions are satisfied over an evaluation period Tevaluate,SLSS in clause 12.3.1.1 if an NR cell is used as synchronization reference source, or Tevaluate,SLSS in clause 12.3.1.2 if an EUTRA cell is used as synchronization reference source, or Tevaluate,SLSS in clause 12.3.1.4 if an SLSS is used as synchronization reference source. If multiple SL-DRX cycles are configured, the SL-DRX cycle length is the longest one.

-SS-RSRP is larger than syncTxThreshOoC.

UE shall be capable of performing PSBCH-RSRP measurements for 3 identified intra-frequency SyncRef UE with the measurement period of Tmeasure,PSBCH-RSRP in table 12.4-1. It is assumed that the SyncRef UE do not drop or delay any SLSS transmission within the measurement period. Otherwise, the measurement period may be extended.

Table 12.4-1: PSBCH-RSRP measurement period for intra-frequency SyncRef UE

When UE is synchronized to GNSS directly, before selection / reselection of the new synchronization reference source UE shall evaluate the GNSS synchronization source reliability for at least 20 seconds before changing the synchronization reference from GNSS to another synchronization reference source. UE shall be always synchronized to GNSS directly during the evaluation of GNSS synchronization source reliability.

## 12.4ASelection / Reselection of Sidelink Synchronization Reference Source with CCA

The requirements defined in this clause do not apply to the UEs that do not support transmission and reception of SLSS.

A SyncRef UE is considered to be detectable when

-PSBCH-RSRP related side conditions given in clause 10 are fulfilled for a corresponding Band,

-S-SSB_RP and S-SSB Ês/Iot according to annex B.4.3 for a corresponding Band are fulfilled.

When GNSS synchronization reference source is configured as the highest priority and

-UE is synchronized to GNSS directly,

-UE shall not drop any sidelink SLSS and data transmission for the purpose of selection/reselection to the SyncRef UE.

-UE is synchronized to a SyncRef UE that is synchronized to GNSS directly or in-directly,

-UE shall not drop any sidelink data transmission for the purpose of selection/reselection to the SyncRef UE. The UE shall be able to identify newly detectable intra-frequency SyncRef UE within Tdetect,SyncRef UE_V2X_CCA seconds if the SyncRef UE meets the selection/reselection criterion defined in TS 38.331[2] and all S-SSB periods selected for SyncRefUE identification are available during the Tdetect,SyncRef UE_V2X_CCA seconds. Tdetect,SyncRef UE_V2X_CCA is defined as 1.6 seconds at S-SSB Ês/Iot ≥ 0 dB, provided that the UE is allowed to drop a maximum of 30% of its SLSS transmissions during Tdetect,SyncRef UE_V2X_CCA for the purpose of selection/reselection to the SyncRef UE.

-For other cases

-When UE is in non-SL-DRX

-The UE shall be able to identify newly detectable intra-frequency SyncRef UE within Tdetect,SyncRef UE_V2X_CCA seconds if the SyncRef UE meets the selection/reselection criterion defined in TS 38.331[2] and all S-SSB periods selected for SyncRefUE identification are available during the Tdetect,SyncRef UE_V2X_CCA seconds. Tdetect,SyncRef UE_V2X_CCA is defined as 8 seconds at S-SSB Ês/Iot ≥ 0 dB, provided that the UE is allowed to drop its sidelink data and SLSS transmissions at most in an aggregated window of 480 ms during Tdetect,SyncRef UE_V2X_CCA for the purpose of selection/reselection to the SyncRef UE. Only if UE additionally drops a maximum of 30% of its SLSS transmission, the UE shall be able to identify newly detectable intra-frequency SyncRef UE within T’detect,SyncRef UE_V2X_CCA seconds, when all S-SSB periods selected for SyncRefUE identification are available during the T’detect,SyncRef UE_V2X_CCA seconds. T’detect,SyncRef UE_V2X_CCA is defined as 1.6 seconds at S-SSB Ês/Iot ≥ 0 dB.

-UE is allowed to drop up to 2 slots of its sidelink data reception per PSBCH monitoring occasion and overall drop rate shall not exceed 0.3% of its sidelink data reception during Tdetect,SyncRef UE_V2X_CCA for the purpose of selection/reselection to the SyncRef UE.

-When UE is in SL-DRX

-UE shall be able to identify newly detectable intra-frequency SyncRef UE within Tdetect,SyncRef UE_V2X_CCA seconds if the SyncRef UE meets the selection/reselection criterion defined in TS 38.331[2] and all S-SSB periods selected for SyncRefUE identification are available during the Tdetect,SyncRef UE_V2X_CCA seconds. Tdetect,SyncRef UE_V2X_CCA is defined as 8 seconds at S-SSB Ês/Iot ≥ 0 dB, provided that the sidelink UE is allowed to drop a maximum of 6 % of its sidelink data and SLSS transmissions for the purpose of selection/reselection to the SyncRef UE. Only if UE additionally drops a maximum of 30% of its SLSS transmission, the UE shall be able to identify newly detectable intra-frequency SyncRef UE within T’detect,SyncRef UE_V2X_CCA seconds, when all S-SSB periods selected for SyncRefUE identification are available during the T’detect,SyncRef UE_V2X_CCA seconds. T’detect,SyncRef UE_V2X_CCA is defined as 1.6 seconds at S-SSB Ês/Iot ≥ 0 dB.

-UE is allowed to drop up to 2 slots of its sidelink data reception per PSBCH monitoring occasion and UE is allowed to drop at most an aggregated window of 24 ms of its sidelink data reception during Tdetect,SyncRef UE_V2X_CCA for the purpose of selection/reselection to the SyncRef UE.

-The UE is allowed to extend Tdetect,SyncRef UE_V2X_CCA to max(4 x 50 SL-DRX cycle length, 8 s) when the following conditions are satisfied over an evaluation period Tevaluate,SLSS in clause 12.3.1.1 if an NR cell is used as synchronization reference source, or Tevaluate,SLSS in clause 12.3.1.2 if an EUTRA cell is used as synchronization reference source, or Tevaluate,SLSS_CCA in clause 12.3A.1.4 if an SLSS is used as synchronization reference source. If multiple SL-DRX cycles are configured, the SL-DRX cycle length is the longest one.

-SS-RSRP is larger than syncTxThreshOoC.

When serving cell/PCell synchronization reference source is configured as the highest priority,

-When UE is in non-SL-DRX

-UE shall be able to identify newly detectable intra-frequency SyncRef UE within Tdetect,SyncRef UE_V2X_CCA seconds if the SyncRef UE meets the selection/reselection criterion defined in TS 38.331[2] and all S-SSB periods selected for SyncRefUE identification are available during the Tdetect,SyncRef UE_V2X_CCA seconds. Tdetect,SyncRef UE_V2X_CCA is defined as 8 seconds at SCH Es/Iot ≥ 0 dB, provided that the sidelink UE is allowed to drop a maximum of 6 % of its sidelink data and SLSS transmissions for the purpose of selection/reselection to the SyncRef UE. When GNSS is not available and only if UE additionally drops a maximum of 30% of its SLSS transmission, the UE shall be able to identify newly detectable intra-frequency SyncRef UE within T’detect,SyncRef UE_V2X_CCA seconds, when all S-SSB periods selected for SyncRefUE identification are available during the T’detect,SyncRef UE_V2X_CCA seconds. T’detect,SyncRef UE_V2X_CCA is defined as 1.6 seconds at S-SSB Ês/Iot ≥ 0 dB.

-UE is allowed to drop up to 2 slots of its sidelink data reception per PSBCH monitoring occasion and overall drop rate shall not exceed 0.3% of its sidelink data reception during Tdetect,SyncRef UE_V2X_CCA for the purpose of selection/reselection to the SyncRef UE.

-When UE is in SL-DRX

-The UE shall be able to identify newly detectable intra-frequency SyncRef UE within Tdetect,SyncRef UE_V2X_CCA seconds if the SyncRef UE meets the selection/reselection criterion defined in TS 38.331[2] and all S-SSB periods selected for SyncRefUE identification are available during the Tdetect,SyncRef UE_V2X_CCA seconds. Tdetect,SyncRef UE_V2X_CCA is defined as 8 seconds at SCH Es/Iot ≥ 0 dB, provided that the UE is allowed to drop its sidelink data and SLSS transmissions at most in an aggregated window of 480 ms during Tdetect,SyncRef UE_V2X_CCA for the purpose of selection/reselection to the SyncRef UE. When GNSS is not available and only if UE additionally drops a maximum of 30% of its SLSS transmission, the UE shall be able to identify newly detectable intra-frequency SyncRef UE within T’detect,SyncRef UE_V2X_CCA seconds, when all S-SSB periods selected for SyncRefUE identification are available during the T’detect,SyncRef UE_V2X_CCA seconds. T’detect,SyncRef UE_V2X_CCA is defined as 1.6 seconds at S-SSB Ês/Iot ≥ 0 dB.

UE is allowed to drop up to 2 slots of its sidelink data reception per PSBCH monitoring occasion and UE is allowed to drop at most an aggregated window of 24 ms of its sidelink data reception during Tdetect,SyncRef UE_V2X_CCA for the purpose of selection/reselection to the SyncRef UE.

-The UE is allowed to extend Tdetect,SyncRef UE_V2X_CCA to max(4 x 50 SL-DRX cycle length, 8 s) when the following conditions are satisfied over an evaluation period Tevaluate,SLSS in clause 12.3.1.1 if an NR cell is used as synchronization reference source, or Tevaluate,SLSS in clause 12.3.1.2 if an EUTRA cell is used as synchronization reference source, or Tevaluate,SLSS_CCA in clause 12.3A.1.4 if an SLSS is used as synchronization reference source. If multiple SL-DRX cycles are configured, the SL-DRX cycle length is the longest one.

-SS-RSRP is larger than syncTxThreshOoC.

The UE shall be capable of performing PSBCH-RSRP measurements for 3 identified intra-frequency SyncRef UE with the measurement period of Tmeasure,PSBCH-RSRP_CCA in table 12.4A-1. It is assumed that the SyncRef UE do not drop or delay any SLSS transmission within the measurement period. Otherwise, the measurement period may be extended.

Table 12.4A-1: PSBCH-RSRP measurement period for intra-frequency SyncRef UE

When UE is synchronized to GNSS directly, before selection/reselection of the new synchronization reference source UE shall evaluate the GNSS synchronization source reliability for at least 20 seconds before changing the synchronization reference from GNSS to another synchronization reference source. UE shall be always synchronized to GNSS directly during the evaluation of GNSS synchronization source reliability.

## 12.5L1 SL-RSRP measurements

## 12.5.1Introduction

This clause contains the measurement requirements related to resource reselection and resource pre-emption of the UE capable of V2X sidelink communication.

## 12.5.2SL-RSRP measurements

The UE physical layer shall be capable of performing the L1 SL-RSRP measurements on the carrier operating V2X sidelink communication for determining the subset of resources to be excluded in PSSCH resource selection in sidelink transmission mode 2 based on network configuration or pre-configuration. The L1 SL-RSRP measurement period corresponds to one slot and the measurement shall meet the L1 SL-RSRP measurement accuracy requirement in Clause 10. After resource (re-)selection procedure, re-evaluation is performed on the reserved resources by L1 SL-RSRP measurements before transmission of SCI with reservation when the conditions specified in TS 38.214 [26] are satisfied.

When the pre-emption mechanism is enabled for the resource pool that UE is monitoring and selecting resource from, after UE selects from the resource not excluded based on L1 SL-RSRP measurement procedure, the UE shall be capable of triggering reselection of already signalled resource(s) as a resource reservation when the conditions specified in TS 38.214 [26] are satisfied.

When partial sensing mechanism is enabled for the resource pool that UE is monitoring and selecting resource from, the UE shall be capable of performing the L1 SL-RSRP measurements on the sensing periods specified in TS 38.214 [26]. When SL-DRX is enabled, the UE shall be capable of performing the L1 SL-RSRP measurements and select resource during SL-DRX active time as specified in TS 38.214 [26].

## 12.6Congestion Control measurements

The UE shall be capable of estimating the channel busy ratio for one or more transmission pools indicated by higher layers in TS 38.331 [2], based on SL-RSSI measurements provided by the physical layer.

When no sidelink transmissions occur, the UE physical layer shall perform a single-shot SL-RSSI measurement for each sub-channel included in all the slots configured as transmission pools.

The SL-RSSI measurement performed according to this clause shall meet the SL-RSSI measurement accuracy requirements defined in clause 10.

The UE shall perform channel busy ratio (CBR) measurement based on SL-RSSI measurements as described in TS 38.215 [4].

## 12.7Interruption

## 12.7.1Interruptions to WAN due to V2X Sidelink Communication

This clause contains the requirements related to the interruptions on the PCell/serving cell due to V2X sidelink communication.

A UE capable of V2X sidelink communication may indicate its interest (initiation or termination) in V2X sidelink communication to the connected gNodeB using IE SidelinkUEInformationNR in TS 38.331 [2].

The UE is allowed an interruption of up to the duration shown in table 12.7.1-1 on the PCell/serving cell during the RRC reconfiguration procedure that includes the V2X sidelink communication configuration message SL-ConfigDedicatedNR in TS 38.331 [2] (setup and release). This interruption is for both uplink and downlink of the PCell/serving cell.

Table 12.7.1-1: Interruption length at V2X RRC reconfiguration

## 12.7.2V2X Sidelink Communication Dropping due to synchronization source change

This clause contains the requirements related to the interruptions on the V2X sidelink communication due to synchronization source change.

For NR V2X  UE not supporting gNB/eNB as synchronization reference source, UE is allowed to drop LTE and NR V2X SL transmission or reception for up to 1ms when synchronization source is changed, where the drop of  LTE V2X SL transmission or reception applies only to in-device coexistence scenario in TS 38.213 [3]:

-From GNSS

-to syncRef UE that is synchronized to GNSS directly/in-directly

-to syncRef UE that has the lowest priority

-From syncRef UE that is synchronized to GNSS directly/in-directly

-to GNSS

-to syncRef UE that has the lowest priority

-From syncRef UE that has the lowest priority

-to GNSS

-to syncRef UE that is synchronized to GNSS directly/in-directly

-to syncRef UE that has the lowest priority

For NR V2X UE supporting gNB/eNB as synchronization reference source, UE is allowed to drop LTE and NR V2X SL transmission or reception for up to 1 ms when synchronization source is changed, where the drop of  LTE V2X SL transmission or reception applies only to in-device coexistence scenario in TS38.213 [3]:

-From GNSS

-to syncRef UE that is synchronized to GNSS directly/in-directly

-to gNB/eNB

-to syncRef UE that is synchronized to gNB/eNB directly

-to syncRef UE that is synchronized to gNB/eNB in-directly

-to syncRef UE that has the lowest priority

-From syncRef UE that is synchronized to GNSS directly/in-directly

-to GNSS

-to gNB/eNB

-to syncRef UE that is synchronized to gNB/eNB directly

-to syncRef UE that is synchronized to gNB/eNB in-directly

-to syncRef UE that has the lowest priority

-From gNB or eNB

-to GNSS

-to syncRef UE that is synchronized to GNSS directly/in-directly

-to eNB or gNB

-to syncRef UE that is synchronized to gNB or eNB directly

-to syncRef UE that is synchronized to gNB or eNB in-directly

-to syncRef UE that has the lowest priority

-From syncRef UE that is synchronized to gNB/eNB directly

-to GNSS

-to syncRef UE that is synchronized to GNSS directly/in-directly

-to gNB/eNB

-to syncRef UE that is synchronized to gNB/eNB directly

-to syncRef UE that is synchronized to gNB/eNB in-directly

-to syncRef UE that has the lowest priority

-From syncRef UE that is synchronized to gNB/eNB in-directly

-to GNSS

-to syncRef UE that is synchronized to GNSS directly/in-directly

-to gNB/eNB

-to syncRef UE that is synchronized to gNB/eNB directly

-to syncRef UE that is synchronized to gNB/eNB in-directly

-to syncRef UE that has the lowest priority

-From syncRef UE that has the lowest priority

-to GNSS

-to syncRef UE that is synchronized to GNSS directly

-to syncRef UE that is synchronized to GNSS in-directly

-to gNB/eNB

-to syncRef UE that is synchronized to gNB/eNB directly

-to syncRef UE that is synchronized to gNB/eNB in-directly

-to syncRef UE that has the lowest priority

UE is allowed to interruption any V2X sidelink signals including PSSCH, PSCCH, PSBCH, PSFCH and SLSS signals.

## 12.7.3Interruptions to WAN due to switching between E-UTRA V2X Sidelink and NR V2X Sidelink

This sub-clause contains the requirements related to the interruptions on the PCell/serving cell due to switching between E-UTRA V2X sidelink and NR V2X sidelink transmissions on a dedicated carrier. It is applicable for UE capable of both NR V2X sidelink and E-UTRA V2X sidelink transmissions in TDM-ed manner.

When a UE capable of switching between E-UTRA V2X sidelink and NR V2X sidelink, the UE is allowed an interruption of up to the duration shown in table 12.7.3-1 on the PCell/serving cell during the E-UTRA V2X sidelink and NR V2X sidelink switch.

This interruption is for both uplink and downlink of the PCell/serving cell.

Table 12.7.3-1: Interruption length due to switching between E-UTRA V2X and NR V2X

## 12.7.4Interruptions to WAN at transitions between active and non-active during SL-DRX

Interruption on PCell/serving cell if configured due to V2X transitions between active and non-active during SL-DRX are allowed with up to 1% probability of missed ACK/NACK when the configured SL-DRX cycle is less than 640 ms, and 0.625% probability of missed ACK/NACK is allowed when the configured SL-DRX cycle is 640 ms or longer. When multiple SL-DRX cycles are configured, the shortest SL-DRX cycle is applied. Each interruption shall not exceed X slot as defined in table 12.7.4-1.

Table 12.7.4-1: Interruption length X at transition between active and non-active during SL-DRX

For SL-DRX active to inactive state transition, when the UE is in non-DRX or DRX on WAN and V2X is in sidelink resource allocation mode 2, the interruptions in this clause shall not apply when one of the following conditions is met:

-While receiving paging,

-While receiving system information.

In addition, for SL-DRX active to inactive state transition, when the UE is in non-DRX or DRX on WAN and V2X is in sidelink resource allocation mode 2 and SL DRX cycle is less than 320 ms, the interruptions in this clause shall not apply when one of the following conditions is met:

-T310 timer is running for RLF on PCell

-performing candidate beam detection on PCell/serving cell as specfied in section 8.5.5. and 8.5.6

During the U2N relay operation as defined in clause 5.8.14 of TS 38.331 [2], the interruption requirements defined in this clause apply only to the sidelink relay UE.

During the multipath relay operation [2], the interruption requirements defined in this clause apply to the SL remote UE or the SL relay UE.

## 12.7.5Interruptions to V2X sidelink at transitions between active and non-active during DRX

Interruption on V2X sidelink if configured due to PCell transitions between active and non-active during DRX are allowed with up to 1% probability of missed ACK/NACK when the configured DRX cycle is less than 640 ms, and 0.625% probability of missed ACK/NACK is allowed when the configured DRX cycle is 640 ms or longer. It is only applied when HARQ process on V2X sidelink is supported. Each interruption shall not exceed X slot as defined in table 12.7.5-1.

Table 12.7.5-1: Interruption length X at transition between active and non-active during DRX

## 12.7.6Interruptions to V2X sidelink due to Active BWP switching Requirement

This clause contains the requirements related to the interruptions on the V2X sidelink due to BWP switch in FDM based intra-band concurrent V2X operation.

The requirements in clause 8.2.2.2.5 shall apply. The interrupted X slot is defined in table 12.7.6-1.

Table 12.7.6-1: Interruption length X

NOTE: No sidelink communication happens during BWP switching delay period for TDM based intra-band concurrent operation.

## 12.7.7Interruptions to WAN due to SyncRef UE detection and/or Sensing during SL DRX off duration

This sub-clause contains the requirements related to the interruptions on the PCell/serving cell due to SyncRef UE detection and/or Sensing during SL DRX off duration.

The requirements in clause 12.7.4 shall apply.

## 12.7.8Interruptions at NR sidelink discovery configuration

This clause contains the requirements related to the interruptions on the PCell/serving cell due to NR sidelink discovery.

A UE capable of NR sidelink discovery may indicate its interest (initiation or termination) in NR sidelink discovery to the connected gNodeB using IE SidelinkUEInformationNR in TS 38.331 [2].

The UE is allowed an interruption of up to the duration shown in Table 12.7.8-1 on the PCell/serving cell during the RRC reconfiguration procedure that includes the NR sidelink discovery configuration message sl-DiscConfig in TS 38.331 [2] (setup and release). This interruption is for both uplink and downlink of the PCell/serving cell.

12.7.8-1: Interruption length at NR sidelink discovery configuration

## 12.7.9Interruptions to WAN due to sidelink carrier addition/release

This sub-clause contains the requirements related to the interruptions on the PCell/serving cell due to sidelink component carrier addition/release. It is applicable for UE is in sidelink resource allocation mode 2.

A UE capable of V2X sidelink communication may indicate its interest (initiation or termination) in V2X sidelink communication to the connected gNodeB using IE SidelinkUEInformationNR in TS38.331[2].

The UE is allowed an interruption of up to the duration shown in table 12.7.9-1 on the PCell/serving cell when any number of sidelink component carriers is added or released. This interruption is for both uplink and downlink of the PCell/serving cell.

Table 12.7.9-1: Interruption length due to sidelink component carrier addition/release

For sidelink component carrier addition/release, when the UE is in RRC_IDLE/RRC_INACTIVE mode, the interruptions in this clause shall not apply when one of the following conditions is met:

-While the UE is receiving paging,

-While the UE is receiving system information.

## 12.8Reliability of GNSS signal

This clause contains requirements regarding reliability of GNSS signal for the UE capable of  V2X sidelink communication under the following additional condition:

-The UE is configured or pre-configured with parameters for enabling the UE to acquire the GNSS synchronization.

If UE considers GNSS is a reliable synchronization reference, the UE shall meet timing accuracy requirement as specified in clause 12.2 and frequency accuracy requirement as specified in clause 6.4E of TS 38.101-1 [18]. Otherwise, the UE shall be capable to select another synchronization reference source.

## 12.9Scheduling availability

## 12.9.1Scheduling availability of UE switching between E-UTRA sidelink and NR sidelink

This clause contains the restrictions on the scheduling availability for V2X sidelink due to switching between E-UTRA V2X sidelink and NR V2X sidelink transmission on a dedicated carrier. For the NR V2X sidelink, the assumed number of configured symbols in a slot is 14.

When switch from E-UTRA V2X sidelink to NR V2X sidelink occurs in NR slot ‘n’,

-UE is not expected to transmit or receive on NR V2X sidelink on the slot ‘n’.

When switch from NR V2X sidelink to E-UTRA V2X sidelink occurs in NR slot ‘n-1’,

-UE is not expected to transmit or receive on NR V2X sidelink on the slot ‘n-1’.

When switch from NR V2X sidelink to E-UTRA V2X sidelink occurs in E-UTRA subframe ‘n’,

-UE is not expected to transmit or receive on E-UTRA V2X sidelink on the subframe ‘n’.

When switch from E-UTRA V2X sidelink to NR V2X sidelink occurs in E-UTRA subframe ‘n-1’,

-UE is not expected to transmit or receive E-UTRA on V2X sidelink on the subframe ‘n-1’.

## 12.9.2Scheduling availability of UE switching between Uu uplink  and V2X sidelink

This clause contains the restrictions on the scheduling availability for V2X sidelink due to switching between Uu uplink and V2X sidelink. For NR V2X sidelink, the assumed number of configured symbols in a slot is 14.

When switch from Uu uplink slot to V2X sidelink slot occurs in sidelink slot ‘n’,

-UE is not expected to transmit or receive on V2X sidelink on the sidelink slot ‘n’.

When switch from V2X sidelink slot to Uu uplink slot occurs in sidelink slot ‘n-1’,

-UE is not expected to transmit or receive on V2X sidelink on the sidelink slot ‘n-1’.

When switch from V2X sidelink slot to Uu uplink slot occurs in Uu slot ‘n’,

-UE is not expected to transmit uplink or receive downlink on the Uu slot ‘n’.

When switch from Uu uplink slot to V2X sidelink slot occurs in Uu slot ‘n-1’,

-UE is not expected to transmit uplink or receive downlink on the Uu slot ‘n-1’.

-UE is not expected to transmit uplink or receive downlink on the Uu slot ‘n-1’.

## 12.10Selection / Reselection of relay UE

## 12.10.1Introduction

This section contains the requirements related to selection and reselection of relay UE.

The requirements apply for the selection and reselection of candidate relay UEs that are transmitting relay discovery signals within the resource pool as configured for the remote UE. The requirements are applicable to the following UE capabilities [2]:

-a remote UE that communicates with the network via a UE-to-network (U2N) relay UE or

-a remote UE that communicates with another via a UE-to-UE (U2U) relay UE.

## 12.10.2Selection / Reselection of relay UE

For a remote UE configured by upper layer for relay operation, the remote UE shall search for candidate relay UEs for selection and/or reselection every discovery period which is determined by resource reservation period or SPS transmission periodicity configured by network.

If the remote UE has a selected sidelink relay UE, then the remote UE shall measure the SD-RSRP or SL-RSRP of the selected relay once in every four discovery periods and evaluate if it meets the relay selection criterion as defined in TS 38.331 [2] (clause 5.8.15.3 for U2N relay and clause 5.8.17.3 for U2U relay).

The remote UE shall measure SD-RSRP or SL-RSRP of the candidate relay UEs every Tmeasure, SL_Relay_Intra for relay UEs that are detected and measured according to the measurement rules.

For intra-frequency relay UEs that are detected, but that has not been selected or reselected to, the remote UE shall be capable of evaluating that the intra-frequency relay UE has met selection or reselection criterion defined in TS 38.331 [2] (clause 5.8.15.3 for U2N relay and clause 5.8.17.3 for U2U relay) within Tevaluate, SL_Relay_Intra as specified in table 12.10.2-1.

The minimum requirements are required to meet when the selected and candidate relay UEs are transmitting relay discovery message every discovery period.

Table 12.10.2-1: Tmeasure, SL_Relay_Intra and Tevaluate, SL_Relay_Intra

## 12.11Component Carrier Addition and Release Delay for Sidelink Carrier Aggregation

Requirements in this clause are applicable to UE supporting NR sidelink carrier aggregation.

For UE configured in sidelink resource allocation mode 2, the delay within which the UE shall accomplish the NR sidelink component carrier addition/release is up to UE implementation.

## 12.12Selection / Reselection of Synchronization Reference Source for NR SL Carrier Aggregation

Requirements in this clause are applicable to UE supporting NR sidelink carrier aggregation.

When the UE is synchronized to a SyncRef UE in a carrier and required only to search other SyncRef UEs in the synchronized carrier, the UE shall be able to identify a newly detectable NR SL SyncRef UE within Tdetect,SyncRef UE_V2X if the SyncRef UE meets the selection/reselection criterion defined in TS 38.331 [2]. The UE shall be capable of performing PSBCH-RSRP measurements for 3 identified NR SL SyncRef UE with the measurement period of Tmeasure,PSBCH-RSRP in table 12.4-1.

When the synchronization reference source for NR sidelink carrier aggregation is lost and UE has to search SyncRef UE on the aggregated carriers which are configured as synchronization carrier, the UE shall be able to identify a newly detectable NR SL SyncRef UE within N×Tdetect,SyncRef UE_V2X if the SyncRef UE meets the selection/reselection criterion defined in TS 38.331 [2]. The UE shall be capable of performing PSBCH-RSRP measurements for 3 identified NR SL SyncRef UE per carrier with the measurement period of N×Tmeasure,PSBCH-RSRP. N is the number of aggregated carriers configured as synchronization carrier.

It is assumed that the identified NR SL SyncRef UE does not drop or delay any SLSS transmission within the measurement period. Otherwise, the measurement period may be extended.

When GNSS synchronization reference source is configured as the highest priority and

-UE is synchronized to a SyncRef UE that is synchronized to GNSS directly or in-directly,

-The value of Tdetect,SyncRef UE_V2X is as 1.6 seconds at S-SSB Es/Iot ≥0 dB, provided that the UE is allowed to drop a maximum of 30% of its SLSS transmissions on each carrier operating NR SL sidelink communication during Tdetect,SyncRef UE_V2X for the purpose of selection / reselection to the SyncRef UE.

-in other case:

-When UE is in non-SL-DRX

-The value of Tdetect,SyncRef UE_V2X is as 8 seconds at S-SSB Es/Iot ≥0 dB, provided that the UE is allowed to drop a maximum of 6%  of its SLSS transmissions on each carrier operating SL sidelink communication during Tdetect,SyncRef UE_V2X for the purpose of selection/reselection to the SyncRef UE.

-UE is allowed to drop up to 2 slots of its SL data reception on each carrier operating SL sidelink communication per PSBCH monitoring occasion and overall drop rate shall not exceed 0.3% of its SL data reception during Tdetect,SyncRef UE_V2X for the purpose of selection/reselection to the SyncRef UE.

-When UE is in SL-DRX

-The value of Tdetect,SyncRef UE_V2X is as 8 seconds at S-SSB Es/Iot ≥0 dB, provided that the UE is allowed to drop a maximum of 6%  of its SLSS transmissions on each carrier operating SL sidelink communication during Tdetect,SyncRef UE_V2X for the purpose of selection/reselection to the SyncRef UE.

-UE is allowed to drop up to 2 slots of its SL data reception on each carrier operating SL sidelink communication per PSBCH monitoring occasion and UE is allowed to drop at most an aggregated window of 24 ms of its SL data reception during Tdetect,SyncRef UE_V2X for the purpose of selection/reselection to the SyncRef UE.

-The UE is allowed to extend Tdetect,SyncRef UE_V2X to max(4×50 SL-DRX cycle length, 8 s) when the following conditions are satisfied over an evaluation period Tevaluate,SLSS in clause 12.3.1.1 if an NR cell is used as synchronization reference source, or Tevaluate,SLSS in clause 12.3.1.2 if an EUTRA cell is used as synchronization reference source, or Tevaluate,SLSS in clause 12.3.1.4 if an SLSS is used as synchronization reference source. If multiple SL-DRX cycles are configured, the SL-DRX cycle length is the longest one.

-SS-RSRP is larger than syncTxThreshOoC.

When serving cell/PCell synchronization reference source is configured as the highest priority,

-When UE is in non-SL-DRX

-The value of Tdetect,SyncRef UE_V2X is as 8 seconds at S-SSB Es/Iot ≥0 dB, provided that the UE is allowed to drop a maximum of 6%  of its SLSS transmissions on each carrier operating NR sidelink communication during Tdetect,SyncRef UE_V2X for the purpose of selection/reselection to the SyncRef UE.

-UE is allowed to drop up to 2 slots of its SL data reception on each carrier operating NR SL sidelink communication per PSBCH monitoring occasion and overall drop rate shall not exceed 0.3% of its SL data reception during Tdetect,SyncRef UE_V2X for the purpose of selection/reselection to the SyncRef UE.

-When UE is in SL-DRX

-The value of Tdetect,SyncRef UE_V2X is as 8 seconds at S-SSB Es/Iot ≥0 dB, provided that the UE is allowed to drop a maximum of 6%  of its SLSS transmissions on each carrier operating NR SL sidelink communication during Tdetect,SyncRef UE_V2X at most in an aggregated window of 480 ms during Tdetect,SyncRef UE_V2X for the purpose of selection/reselection to the SyncRef UE.

-UE is allowed to drop up to 2 slots of its SL data reception per PSBCH monitoring occasion and UE is allowed to drop at most an aggregated window of 24 ms of its SL data reception during Tdetect,SyncRef UE_V2X for the purpose of selection/reselection to the SyncRef UE.

-The UE is allowed to extend Tdetect,SyncRef UE_V2X to max(4×50 SL-DRX cycle length, 8 s) when the following conditions are satisfied over an evaluation period Tevaluate,SLSS in clause 12.3.1.1 if an NR cell is used as synchronization reference source, or Tevaluate,SLSS in clause 12.3.1.2 if an EUTRA cell is used as synchronization reference source, or Tevaluate,SLSS in clause 12.3.1.4 if an SLSS is used as synchronization reference source. If multiple SL-DRX cycles are configured, the SL-DRX cycle length is the longest one.

-SS-RSRP is larger than syncTxThreshOoC.

## 12ANR Sidelink Measurements for Positioning

## 12A.1Introduction

Clause 12A contains requirements for UE capable of V2X sidelink or 5G ProSe operation, which is also capable of performing SL positioning measurements defined in TS 38.215 [4], including SL RSTD, SL PRS-RSRP, SL Rx-Tx time difference, SL PRS-RSRPP measurements, SL AoA, and SL RTOA, provided that:

- The SL-PRS are received on NR PC5 interface within a single sidelink BWP on a single carrier,

-The UE is in any cell selection state or the UE is inside NG-RAN coverage while configured for SL positioning operation on a sidelink carrier, which is dedicated to only sidelink operation, and configured with only a PCell on WAN carrier, and

-The measuring UE is the location target UE or an anchor UE, and

-The UE is not required to monitor PSCCH, which is associated with SL-PRS in the same slot, outside the SL-DRX active time.

NOTE 1:Any cell selection state refers to a UE that is out of network coverage and is not associated with a serving cell on any carrier as defined in TS 38.304 [1].

NOTE 2:When a UE in RRC_CONNECTED state is performing transmissions and/or reception for SL positioning operation, the UE shall meet all the requirements specified in clause 9 assuming that UE has a dedicated RX/TX chain for the sidelink operation. Otherwise, the UE may interrup the SL positioning measurements in order to meet the measurement requirements specified in clause 9.

NOTE 3: When a UE in RRC_CONNECTED state is performing transmissions and/or reception for SL positioning operation, the UE shall meet all relevant requirements related to its WAN operation, assuming that UE has a dedicated RX/TX chain for the sidelink operation. Otherwise, the UE may interrup the SL positioning measurements or SL-PRS transmissions in order to meet the measurement requirements related to its WAN operation.

Prior to performing SL-PRS based measurements, the target UE may need to perform the discovery procedure to discover anchor UEs according to TS 38.305 [22].

## 12A.2SL RSTD measurements

## 12A.2.1Introduction

The requirements in clause 12A.2 apply for SL RSTD measurements of the first and additional paths.

The requirements in clause 12A.2 shall apply provided the UE has received a RequestLocationInformation message from LMF or another UE via SLPP specified in TS 38.355 [37] requesting the UE to measure and report SL RSTD measurements defined in TS 38.215 [4] based on SL-PRS.

12A.2.2Requirements Applicability

The requirements in clause 12A.2 apply for periodic, aperiodic, and triggered SL RSTD measurements, provided:

-SL RSTD related side conditions given in clause 10.4A.2.2 for FR1 are fulfilled, for a corresponding Band.

## 12A.2.3Measurement Capability

UE SL RSTD measurement capability is as indicated by the UE in:

SL-TDOA-ProvideCapabilities, according to TS 38.355 [37].

## 12A.2.4Measurement Reporting Requirements

The measurement reporting delay is defined as the time between the moment when the measurement report is triggered and the moment when the UE starts to transmit the measurement report over the air interface.

For UE reporting to LMF, this requirement assumes that the measurement report is not delayed by other SLPP signalling on the DCCH. This measurement reporting delay excludes a delay uncertainty resulted when inserting the measurement report to the TTI of the uplink DCCH. The delay uncertainty is: 2 x TTIDCCH where TTIDCCH is the duration of subframe or slot or subslot when the measurement report is transmitted on the PUSCH with subframe or slot or subslot duration.

For UE reporting to another UE, this requirement assumes that the measurement report is not delayed by other SLPP signalling on the STCH. This measurement reporting delay excludes a delay uncertainty resulted when inserting the measurement report to the TTI of the transmitted STCH. The delay uncertainty is: 2 x TTISTCH where TTISTCH is the duration of subframe or slot or subslot when the measurement report is transmitted on the PSSCH with subframe or slot or subslot duration.

This measurement reporting delay excludes any delay caused by no SL resources for UE to send the measurement report.

The reported SL RSTD measurement values contained in measurement reports shall be based on the measurement report mapping requirements specified in clause 10.4A.2.1.

The SL RSTD measurements performed and reported according to this section shall meet the SL RSTD measurement accuracy requirements in clause 10.4A.2.2, for each measured SL-PRS resource.

## 12A.2.5Measurements Period Requirements

When the UE physical layer receives the last of SL-TDOA-ProvideAssistanceData and SL-TDOA-RequestLocationInformation from LMF or another UE via SLPP specified in TS 38.355 [37], the UE shall be able to perform multiple SL RSTD measurements based on SL-PRS from one or more other SL UEs (up to the UE capability specified in clause 12A.2.3), with each SL RSTD measurement based on  SL-PRS from the reference UE and SL-PRS from another anchor UE, as defined in TS 38.215 [4]. The SL RSTD measurement for each anchor UE shall be performed during the measurement period  defined as:TSL RSTD,total

, TSL RSTD,total=s=1STSL RSTD,effect,s

where

S is the number of samples for each measured anchor link, defined below:

= 1 for SL-PRS bandwidth>48 PRBs,S

= 4 for SL-PRS bandwidth≤48 PRBs, andS

for each SL-PRS sample s of the target measured link, which is received within a slot where the UE receives SCI and the associated SL-PRS within its capabilities reported by UE via maxNumOfActiveSL-PRS-ResourcesInOneSlot and maxNumOfSlotsWIthActiveSL-PRS-Resources specified in TS 38.355 [37], is defined as:TSL RSTD,effect,s

, for s<S, where  and  are the beginning of the first slot of SL-PRS sample s+1 and SL-PRS sample s, respectively,TSL RSTD,effect,s=ts+1-tsts+1ts

for s=S, TSL RSTD,effect,s=Tdur,s+ΔSLproc ,

is the duration of the slot carrying SL-PRS sample s of the SL RSTD measurement,Tdur,s

is the processing time reported by the UE via minTimeAfterEndofSlotCarryActiveSL-PRS-Resources specified in TS 38.355 [37].ΔSLproc

the time starts from the first slot where the UE receives SCI and the associated SL-PRS within its capabilities reported by UE via maxNumOfActiveSL-PRS-ResourcesInOneSlot and maxNumOfSlotsWIthActiveSL-PRS-Resources specified in TS 38.355 [37]. TSL RSTD,total

The SL RSTD measurement period ends after the UE has measured SL-PRS resources from multiple anchor UEs including reference UE and one or more other anchor UEs.

A UE may drop one or more SL-PRS measurement samples if the number of active slots or the number of active resources per slot for the ongoing SL-PRS measurement exceed the UE capabilities reported by UE via sl-PRS-CommonProcCapabilityPerBand specified in TS 38.355 [37]. For a single-sample measurement, the whole measurement may not be performed.

If the synchronization reference source changes during  at the measuring UE, while the UE is performing the SL RSTD measurement, then the UE shall restart the SL RSTD measurement after the synchronization reference source change and shall send the measurement report during a measurement period, which can be longer than .TSL RSTD,totalTSL RSTD,total

The requirements in this clause do not apply, when the synchronization reference source changes during  at the UE transmitting SL-PRS for the SL RSTD measurement.TSL RSTD,total

The requirements in this clause apply, provided that no SL-PRS symbols are dropped due to, e.g., selection or reselection of synchronization reference source according to clause 12.4 during the measurement period . Otherwise, the measurement period can be longer.TSL RSTD,total

The requirements in this clause apply, provided that the reception of slots containing SL-PRS is not interrupted during the measurement period . Otherwise, if the reception of the slots containing SL-PRS is interrupted, the measurement period can be longer.TSL RSTD,total

## 12A.3SL PRS-RSRP measurements

## 12A.3.1Introduction

The requirements in clause 12A.3 apply for SL PRS-RSRP measurements and for SL PRS-RSRP path measurements of the first and additional paths.

The requirements in clause 12A.3 shall apply provided the UE has received a RequestLocationInformation message from LMF or another UE via SLPP specified in TS 38.355 [37] requesting the UE to measure and report SL PRS-RSRP measurements defined in TS 38.215 [4] based on SL-PRS.

## 12A.3.2Requirements Applicability

The requirements in clause 12A.3 apply for periodic, aperiodic, and triggered SL PRS-RSRP measurements, provided:

-SL PRS-RSRP related side conditions given in clause 10.4A.3.2 for FR1 are fulfilled, for a corresponding Band.

12A.3.3Measurement Capability

UE SL PRS-RSRP measurement capability is as indicated by the UE in:

-SL-TDOA-ProvideCapabilities, SL-RTT-ProvideCapabilities, SL-AOA-ProvideCapabilities, or SL-TOA-ProvideCapabilities, according to TS 38.355 [37].

## 12A.3.4Measurement Reporting Requirements

The measurement reporting delay is defined as the time between the moment when the measurement report is triggered and the moment when the UE starts to transmit the measurement report over the air interface.

For UE reporting to LMF, this requirement assumes that the measurement report is not delayed by other SLPP signalling on the DCCH. This measurement reporting delay excludes a delay uncertainty resulted when inserting the measurement report to the TTI of the uplink DCCH. The delay uncertainty is: 2 x TTIDCCH where TTIDCCH is the duration of subframe or slot or subslot when the measurement report is transmitted on the PUSCH with subframe or slot or subslot duration.

For UE reporting to another UE, this requirement assumes that the measurement report is not delayed by other SLPP signalling on the STCH. This measurement reporting delay excludes a delay uncertainty resulted when inserting the measurement report to the TTI of the transmitted STCH. The delay uncertainty is: 2 x TTISTCH where TTISTCH is the duration of subframe or slot or subslot when the measurement report is transmitted on the PSSCH with subframe or slot or subslot duration.

This measurement reporting delay excludes any delay caused by no SL resources for UE to send the measurement report.

The reported SL PRS-RSRP measurement values contained in measurement reports shall be based on the measurement report mapping requirements specified in clause 10.4A.3.1.

The SL PRS-RSRP measurements performed and reported according to this section shall meet the SL PRS-RSRP measurement accuracy requirements in clause 10.4A.3.2, for each measured SL-PRS resource.

## 12A.3.5Measurements Period Requirements

When the physical layer receives the last of:

-SL-TDOA-ProvideAssistanceData and SL-TDOA-RequestLocationInformation, or

-SL-AOA-ProvideAssistanceData and SL-AOA-RequestLocationInformation, or

-SL-TOA-ProvideAssistanceData and SL-TOA-RequestLocationInformation, or

-SL-RTT-ProvideAssistanceData and SL-RTT-RequestLocationInformation,

from LMF or another UE via SLPP specified in TS 38.355 [37], and the UE is configured to perform SL PRS-RSRP measurement together with the corresponding mandatory measurement (SL RSTD, SL AoA/ZoA, SL RTOA, and SL Rx-Tx, respectively), the UE shall be able to perform multiple SL PRS-RSRP measurements based on SL-PRS from one or more other SL UEs (up to the UE capability specified in clause 12A.3.3), as defined in TS 38.215 [4].

The SL PRS-RSRP measurement for the measured anchor UE SL-PRS shall be performed during the measurement period of the corresponding mandatory measurement, with which the SL PRS-RSRP measurement is configured, i.e., during:

defined in clause 12A.2.5, for SL PRS-RSRP configured together with SL RSTD, TSL RSTD,total

defined in clause 12A.4.5, for SL PRS-RSRP configured together with SL Rx-Tx, TSL Rx-Tx,total

defined in clause 12A.6.5, for SL PRS-RSRP configured together with SL AoA/ZoA, orTSL AoA,total

defined in clause 12A.7.5, for SL PRS-RSRP configured together with SL RTOA.TSL RTOA,total

A UE may drop one or more SL-PRS measurement samples if the number of active slots or the number of active resources per slot for the ongoing SL-PRS measurement exceed the UE capabilities reported by UE via sl-PRS-CommonProcCapabilityPerBand specified in TS 38.355 [37]. For a single-sample measurement, the whole measurement may not be performed.

## 12A.4SL Rx-Tx measurements

## 12A.4.1Introduction

The requirements in clause 12A.4 apply for SL Rx-Tx measurements of the first and additional paths.

The requirements in clause 12A.4 shall apply provided the UE has received SL-RTT-RequestLocationInformation from LMF or another UE via SLPP specified in TS 38.355 [37] requesting the UE to measure and report SL Rx-Tx time difference measurements defined in TS 38.215 [4] based on SL-PRS.

## 12A.4.2Requirements Applicability

The requirements in clause 12A.4 apply for periodic, aperiodic, and triggered SL Rx-Tx time difference measurements, provided:

-SL Rx-Tx time difference related side conditions given in clause 10.4A.4.2 for FR1 are met for a corresponding Band.

-The actual time difference between the corresponding SL-PRS transmission and reception used to derive the measurement is no larger than 160 ms.

## 12A.4.3Measurement Capability

SL Rx-Tx time difference measurement capability is as indicated by the UE in SL-RTT-ProvideCapabilities according to TS 38.355 [37].

## 12A.4.4Measurement Reporting Requirements

The measurement reporting delay is defined as the time between the moment when the measurement report is triggered and the moment when the UE starts to transmit the measurement report over the air interface.

For UE report to LMF, this requirement assumes that the measurement report is not delayed by other SLPP signalling on the DCCH. This measurement reporting delay excludes a delay uncertainty resulted when inserting the measurement report to the TTI of the uplink DCCH. The delay uncertainty is: 2 x TTIDCCH where TTIDCCH is the duration of subframe or slot or subslot when the measurement report is transmitted on the PSSCH with subframe or slot or subslot duration.

For UE report to another UE, this requirement assumes that the measurement report is not delayed by other SLPP signalling on the STCH. This measurement reporting delay excludes a delay uncertainty resulted when inserting the measurement report to the TTI of the sidelink STCH. The delay uncertainty is: 2 x TTISTCH where TTISTCH is the duration of subframe or slot or subslot when the measurement report is transmitted on the PSSCH with subframe or slot or subslot duration.

The measurement reporting delay excludes any delay caused by no SL resources for UE to send the measurement report.

The reported SL Rx-Tx time difference measurement values contained in measurement reports shall be based on the measurement report mapping requirements specified in clause 10.4A.4.1.

The SL Rx-Tx time difference measurements performed and reported according to this section shall meet the SL Rx-Tx time difference measurement accuracy requirements in clause 10.4A.4.2, for each measured SL-PRS resource.

## 12A.4.5Measurement Period Requirements

When the UE physical layer receives SL-RTT-ProvideAssistanceData message and SL-RTT-RequestLocationInformation message from LMF or another UE via SLPP specified in TS 38.355 [37], the UE shall be able to perform multiple SL Rx-Tx time difference measurements based on SL-PRS from one or more other SL UEs (up to the UE capability specified in clause 12A.4.3), as defined in TS 38.215 [4]. For each individual SL-PRS resource measured by a UE, the SL Rx-Tx time difference measurement is performed during  defined as:TSL Rx-Tx,total

TSL Rx-Tx,total=s=1STSL Rx-Tx,effect,s+Tuncertain ,

where,

S is the number of samples for a single SL Rx-Tx measurement defined below:

= 1 for SL-PRS bandwidth > 48 PRBs,S

= 4 for SL-PRS bandwidth48 PRBs, andS

for SL-PRS sample s, which is received within a slot where the UE receives SCI and the associated SL-PRS is within its capabilities reported by UE via maxNumOfActiveSL-PRS-ResourcesInOneSlot and maxNumOfSlotsWIthActiveSL-PRS-Resources specified in TS 38.355 [37],  is defined as:TSL Rx-Tx,effect,s

, for s<S, where  and  are the start of the s-th and (s+1)-th slot of SL-PRS samples s and SL-PRS samples s+1, respectively, TSL Rx-Tx,effect,s=ts+1-tststs+1

for s = S,TSL Rx-Tx,effect,s=Tdur,s+ΔSLproc ,

is the duration of the slot carrying SL-PRS sample s of SL Rx-Tx measurement, Tdur,s

is the processing time indicated by UE via  minTimeAfterEndofSlotCarryActiveSL-PRS-Resources specified in TS 38.355 [37] of the UE performing the SL Rx-Tx time difference measurement. ΔSLproc

is defined as below: Tuncertain

If the UE reports the transmission timestamp of a SL-PRS as defined in TS 38.215 [4], and the SL-PRS transmission occurs after the SL-PRS reception used to derive the measurement,  is the additional time delay from the SL PRS reception until the actual SL PRS transmission.Tuncertain

Otherwise, .Tuncertain=0

A UE may drop one or more SL-PRS measurement samples if the number of active slots or the number of active resources per slot for the ongoing SL-PRS measurement exceed the UE capabilities reported by UE via sl-PRS-CommonProcCapabilityPerBand specified in TS 38.355 [37]. For a single-sample measurement, the whole measurement may not be performed.

If the synchronization reference source changes during  at the measuring UE, while the measuring UE is performing the SL Rx-Tx time difference measurement, then the measuring UE shall restart the SL Rx-Tx time difference measurement and shall send the measurement report during a measurement period, which can be longer than .TSL Rx-Tx,totalTSL Rx-Tx,total

The requirements in this clause do not apply, when the synchronization reference source changes during  at the UE transmitting SL-PRS for the SL Rx-Tx measurement.TSL Rx-Tx,total

The requirements in this clause apply, provided that no SL-PRS symbols are dropped due to, e.g., selection or reselection of synchronization reference source according to clause 12.4 during the measurement period . Otherwise, the measurement period can be longer.TSL Rx-Tx,total

The requirements in this clause apply, provided that the reception of slots containing SL-PRS is not interrupted during the measurement period . Otherwise, if the reception of the slots containing SL-PRS is interrupted, the measurement period can be longer.TSL Rx-Tx,total

## 12A.5SL PRS-RSRPP measurements

## 12A.5.1Introduction

The requirements in clause 12A.5 shall apply provided the UE has received SL-TDOA-RequestLocationInformation or SL-AOA-RequestLocationInformation or SL-TOA-RequestLocationInformation or SL-RTT-RequestLocationInformation from LMF or another UE via SLPP requesting the UE to measure and report SL PRS-RSRPP measurements defined in TS 38.215 [4].

## 12A.5.2Requirements Applicability

The requirements in clause 12A.5 apply for periodic and triggered SL PRS-RSRPP measurements, provided:

-SL PRS-RSRPP related side conditions given in clause 10.4A.5.2 for FR1 are met for a corresponding Band.

## 12A.5.3Measurement Capability

SL PRS-RSRPP measurement capability is as indicated by the UE in SL-TDOA-ProvideCapabilities, SL-RTT-ProvideCapabilities, SL-AOA-ProvideCapabilities, or SL-TOA-ProvideCapabilities according to TS 38.355 [37].

## 12A.5.4Measurement Reporting Requirements

The measurement reporting delay is defined as the time between the moment when the measurement report is triggered and the moment when the UE starts to transmit the measurement report over the air interface.

For UE report to LMF, this requirement assumes that the measurement report is not delayed by other SLPP signalling on the DCCH. This measurement reporting delay excludes a delay uncertainty resulted when inserting the measurement report to the TTI of the uplink DCCH. The delay uncertainty is: 2 x TTIDCCH where TTIDCCH is the duration of subframe or slot or subslot when the measurement report is transmitted on the PSSCH with subframe or slot or subslot duration.

For UE report to another UE, this requirement assumes that the measurement report is not delayed by other SLPP signalling on the STCH. This measurement reporting delay excludes a delay uncertainty resulted when inserting the measurement report to the TTI of the sidelink STCH. The delay uncertainty is: 2 x TTISTCH where TTISTCH is the duration of subframe or slot or subslot when the measurement report is transmitted on the PSSCH with subframe or slot or subslot duration.

This measurement reporting delay excludes any delay caused by no SL resources for UE to send the measurement report.

The reported SL PRS-RSRPP measurement values contained in measurement reports shall be based on the measurement report mapping requirements specified in clauses 10.4A.5.1.

The SL PRS-RSRPP measurements performed and reported according to this section shall meet the SL PRS-RSRPP measurement accuracy requirements in clause 10.4A.5.2, for each measured SL-PRS resource.

## 12A.5.5Measurement Period Requirements

When the physical layer receives

-SL-TDOA-ProvideAssistanceData message and SL-TDOA-RequestLocationInformation message, or

-SL-AOA-ProvideAssistanceData message and SL-AOA-RequestLocationInformation message, or

-SL-TOA-ProvideAssistanceData message and SL-TOA-RequestLocationInformation message, or

-SL-RTT-ProvideAssistanceData message and SL-RTT-RequestLocationInformation message,

from LMF or another UE via SLPP specified in TS 38.355 [37], and the UE is configured to perform SL PRS-RSRPP measurement together with the corresponding mandatory measurement (SL RSTD, SL AoA/ZoA, SL RTOA, and SL Rx-Tx, respectively), the UE shall be able to perform multiple SL PRS-RSRPP measurements based on SL-PRS from one or more other SL UEs (up to the UE capability specified in clause 12A.5.3), as defined in TS 38.215 [4].

The SL PRS-RSRPP measurement for the measured anchor UE SL-PRS shall be performed during the measurement period of the corresponding mandatory measurement, with which the SL PRS-RSRPP measurement is configured, i.e., during:

- defined in clause 12A.2.5, for SL PRS-RSRPP configured together with SL RSTD, TSL RSTD,total

- defined in clause 12A.4.5, for SL PRS-RSRPP configured together with SL Rx-Tx, TSL Rx-Tx,total

- defined in clause 12A.6.5, for SL PRS-RSRPP configured together with SL AoA/ZoA, orTSL AoA,total

- defined in clause 12A.7.5, for SL PRS-RSRPP configured together with SL RTOA.TSL RTOA,total

A UE may drop one or more SL-PRS measurement samples if the number of active slots or the number of active resources per slot for the ongoing SL-PRS measurement exceed the UE capabilities reported by UE via sl-PRS-CommonProcCapabilityPerBand specified in TS 38.355 [37]. For a single-sample measurement, the whole measurement may not be performed.

## 12A.6SL AoA measurements

## 12A.6.1Introduction

The requirements in clause 12A.6 apply for SL AoA measurements of the first and additional paths.

The requirements in clause 12A.6.5 shall apply for azimuth angle of arrival (A-AoA) and zenith angle of arrival (Z-AoA) first path measurement, provided the UE has received SL-AoA-RequestLocationInformation from LMF or another UE via SLPP specified in TS 38.355 [37] requesting the UE to measure and report SL AoA measurements defined in TS 38.215 [4] based on SL-PRS.

## 12A.6.2Requirements Applicability

The requirements in clause 12A.6 apply for periodic, aperiodic, and triggered SL AoA measurements, provided:

-Conditions defined in clause 7.3E of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-SL AoA related side conditions given in clause B.4A.1 for FR1 are met for a corresponding Band.

## 12A.6.3Measurement Capability

SL AoA measurement capability is as indicated by the UE in:

SL-AoA-ProvideCapabilities according to TS 38.355 [37].

## 12A.6.4Measurement Reporting Requirements

The measurement reporting delay is defined as the time between the moment when the measurement report is triggered and the moment when the UE starts to transmit the measurement report over the air interface.

For UE reporting to LMF, this requirement assumes that the measurement report is not delayed by other SLPP signalling on the DCCH. This measurement reporting delay excludes a delay uncertainty resulted when inserting the measurement report to the TTI of the uplink DCCH. The delay uncertainty is: 2 x TTIDCCH where TTIDCCH is the duration of subframe or slot or subslot when the measurement report is transmitted on the PUSCH with subframe or slot or subslot duration.

For UE reporting to another UE, this requirement assumes that the measurement report is not delayed by other SLPP signalling on the STCH. This measurement reporting delay excludes a delay uncertainty resulted when inserting the measurement report to the TTI of the sidelink STCH. The delay uncertainty is: 2 x TTISTCH where TTISTCH is the duration of subframe or slot or subslot when the measurement report is transmitted on the PSSCH with subframe or slot or subslot duration.

The measurement reporting delay excludes any delay caused by no SL resources or no SL-PRS resources for UE to send the measurement report.

The reported SL AoA measurement values contained in measurement reports shall be based on the measurement report mapping requirements specified in clauses 10.4A.6.1.

## 12A.6.5Measurement Period Requirements

When the UE physical layer receives the last of SL-AoA-ProvideAssistanceData message and SL-AoA-RequestLocationInformation message from LMF or another UE via SLPP specified in TS 38.355 [37], the UE shall be able to measure multiple SL AoA measurements based on SL-PRS from one or more other SL UEs (up to the UE capability specified in 12A.6.3), as defined in TS 38.215 [4]. The SL AoA measurement shall be performedduring the measurement period  defined as:TSL AoA,total

,TSL AoA,total=s=1STSL AoA, effect,s

where,

S is the number of samples for the SL AoA measurement, defined as below:

S = 1 for SL-PRS bandwidth > 48 PRBs,

S = 4 for SL-PRS bandwidth  48 PRBs, and

for each SL-PRS sample s, which is received within a slot where the UE receives SCI and the associated SL-PRS is within its capabilities reported by UE via maxNumOfActiveSL-PRS-ResourcesInOneSlot and maxNumOfSlotsWIthActiveSL-PRS-Resources specified in TS 38.355 [37].  is defined as below,TSL AoA,effect,s

for s < S, where  and  are the beginning of the slots of SL-PRS sample s and SL-PRS sample s+1, respectively, TSL AoA,effect,s=ts+1-tststs+1

for s = S, TSL AoA,effect,s=Tdur,s+ΔSLproc

- is the duration of slot carrying SL-PRS sample s of the SL AoA measurement,Tdur,s

- is the processing time indicated by UE minTimeAfterEndofSlotCarryActiveSL-PRS-Resources specified in TS 38.355 [37] of the UE performing SL AoA measurement.ΔSLproc

A UE may drop one or more SL-PRS measurement samples if the number of active slots or the number of active resources per slot for the ongoing SL-PRS measurement exceed the UE capabilities reported by UE via sl-PRS-CommonProcCapabilityPerBand specified in TS 38.355 [37]. For a single-sample measurement, the whole measurement may not be performed.

If the synchronization reference source of the measuring UE changes during , while the UE is performing the SL AoA measurements, then the measuring UE shall continue performing the SL AoA measurement after the synchronization reference source change, while meeting the requirements in this clause.TSL AoA,total

The requirements in this clause do not apply, when the synchronization reference source changes during  at the UE transmitting SL-PRS for the SL AoA measurement.TSL AoA,total

The requirements in this clause apply provided that no SL-PRS symbols for the SL AoA measurement are dropped due to e.g., the selection or reselection of synchronization reference source according to clause 12.4 during the measurement period. Otherwise, the measurement period can be extended.

The requirements in this clause, apply provided that reception of slots containing SL-PRS for the SL AoA measurement is not interrupted e.g., due to network coverage change. Otherwise, if the reception of the slots containing SL-PRS is interrupted, the measurement period can be extended.

## 12A.7SL RTOA measurements

## 12A.7.1Introduction

The requirements in clause 12A.7 apply for SL RTOA measurements of the first and additional paths.

The requirements in clause 12A.7.5 shall apply provided the UE has received SL-RTOA-RequestLocationInformation from LMF or another UE via SLPP requesting the UE to measure and report SL RTOA measurements defined in TS 38.215 [4].

## 12A.7.2Requirements Applicability

The requirements in clause 12A.7 apply for periodic, aperiodic, and triggered SL RTOA measurements, provided:

-Conditions defined in clause 7.3E of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-SL RTOA related side conditions given in clause B.4A.1 for FR1 are met for a corresponding Band.

## 12A.7.3Measurement Capability

SL RTOA measurement capability is as indicated by the UE in SL-RTOA-ProvideCapabilities according to TS 38.355 [37].

## 12A.7.4Measurement Reporting Requirements

The measurement reporting delay is defined as the time between the moment when the measurement report is triggered and the moment when the UE starts to transmit the measurement report over the air interface.

For UE reporting to LMF, this requirement assumes that the measurement report is not delayed by other SLPP signalling on the DCCH. This measurement reporting delay excludes a delay uncertainty resulted when inserting the measurement report to the TTI of the uplink DCCH. The delay uncertainty is: 2 x TTIDCCH where TTIDCCH is the duration of subframe or slot or subslot when the measurement report is transmitted on the PUSCH with subframe or slot or subslot duration.

For UE reporting to another UE, this requirement assumes that the measurement report is not delayed by other SLPP signalling on the STCH. This measurement reporting delay excludes a delay uncertainty resulted when inserting the measurement report to the TTI of the sidelink STCH. The delay uncertainty is: 2 x TTISTCH where TTISTCH is the duration of subframe or slot or subslot when the measurement report is transmitted on the PSSCH with subframe or slot or subslot duration.

The measurement reporting delay excludes any delay caused by no SL resources or no SL-PRS resources for UE to send the measurement report.

The reported SL RTOA measurement values contained in measurement reports shall be based on the measurement report mapping requirements specified in clauses 10.4A.7.1.

## 12A.7.5Measurement Period Requirements

When the UE physical layer receives the last of SL-RTOA-ProvideAssistanceData message and SL-RTOA-RequestLocationInformation message from LMF or another UE via SLPP specified in TS 38.355 [37], the UE shall be able to measure multiple SL RTOA measurements based on SL-PRS from one or more other SL UEs (up to the UE capability specified in 12A.7.3), as defined in TS 38.215 [4]. The SL RTOA measurement shall be performed during  defined as:TSL RTOA,total

,TSL RTOA,total=s=1STSL RTOA, effect,s

where,

S is the number of samples for the SL RTOA measurementdefined as below: ,

S = 1 for SL-PRS bandwidth > 48 PRBs,

S4 for SL-PRS bandwidth  48 PRBs, and =

for SL-PRS sample s, which is received within a slot where the UE receives SCI, provided that the associated SL-PRS is within its capabilities reported by UE via maxNumOfActiveSL-PRS-ResourcesInOneSlot and maxNumOfSlotsWIthActiveSL-PRS-Resources specified in TS 38.355 [37].  is defined as below,TSL RTOA,effect,s

, for s<S, where  and  are the beginning of the slots of SL-PRS sample s and SL-PRS sample s+1, respectively TSL RTOA,effect,s=ts+1-tststs+1,

for s = S, TSL RTOA,effect,s=Tdur,s+ΔSLproc

is the duration of the slot carrying SL-PRS sample s of the SL RTOA measurement, Tdur,s

is the processing time indicated by UE via minTimeAfterEndofSlotCarryActiveSL-PRS-Resources specified in TS 38.355 [37] of the UE performing SL RTOA measurement. ΔSLproc

A UE may drop one or more SL-PRS measurement samples if the number of active slots or the number of active resources per slot for the ongoing SL-PRS measurement exceed the UE capabilities reported by UE via sl-PRS-CommonProcCapabilityPerBand specified in TS 38.355 [37]. For a single-sample measurement, the whole measurement may not be performed.

If the synchronization reference source of the measuring UE changes during , while the UE is performing the SL RTOA measurements, then the measuring UE shall restart the SL RTOA measurement after the synchronization reference source change and shall send the measurement report during a measurement period, which can be longer than .TSL RTOA,totalTSL RTOA,total

The requirements in this clause do not apply, when the synchronization reference source changes during  at the UE transmitting SL-PRS for the SL RTOA measurement.TSL RTOA,total

The requirements in this clause apply provided that no SL-PRS symbols for the SL RTOA measurement that are dropped due to e.g., the selection or reselection of synchronization reference source according to clause 12.4 during the measurement period. Otherwise, the measurement period can be extended. The requirements in this clause apply, provided that reception of slots containing SL-PRS for the SL RTOA measurement is not interrupted due to network coverage change. Otherwise, if the reception of the slots containing SL-PRS is interrupted, the measurement period can be longer.

## 13Measurement Performance Requirements for NR gNB

## 13.1UL-RTOA

## 13.1.1Report mapping

The reporting range of UL Relative Time of Arrival (UL-RTOA), as defined in Clause 5.2.2 of TS 38.215 [4], is defined from -985024Tc to +985024Tc. The reporting resolution is uniform across the reporting range and is defined as T = Tc2k where k is selected by gNB from the set {-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}.

Tc is defined in TS 38.211 [6].

LMF provides a recommended resolution parameter, timingReportingGranularityFactor or timingReportingGranularityFactorExtended [35]. gNB selects parameter k based on timingReportingGranularityFactor or timingReportingGranularityFactorExtended [35] and informs the LMF.

The mapping of measured/inferred quantity for each reporting resolution (k) is defined in table 13.1.1-1 to table 13.1.1-12.

Table 13.1.1-1: Measurement report mapping for k=0

Table 13.1.1-2: Measurement report mapping for k=1

Table 13.1.1-3: Measurement report mapping for k=2

Table 13.1.1-4: Measurement report mapping for k=3

Table 13.1.1-5: Measurement report mapping for k=4

Table 13.1.1-6: Measurement report mapping for k=5

Table 13.1.1-7: Measurement report mapping for k=-1

Table 13.1.1-8: Measurement report mapping for k=-2

Table 13.1.1-9: Measurement report mapping for k=-3

Table 13.1.1-10: Measurement report mapping for k=-4

Table 13.1.1-11: Measurement report mapping for k=-5

Table 13.1.1-12: Measurement report mapping for k=-6

## 13.1.1AAdditional Path Report Mapping for UL-RTOA

The reporting range of additional path reporting for UL Relative Time of Arrival (UL-RTOA), as defined in Clause 5.2.2 of TS 38.215 [4], is defined from -8175Tc to +8175Tc. The reporting resolution is uniform across the reporting range and is defined as T = Tc2k where k is selected by gNB from the set {-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}.

Tc is defined in TS 38.211 [6].

LMF provides a recommended resolution parameter, timingReportingGranularityFactor or timingReportingGranularityFactorExtended [35]. gNB selects parameter k based on timingReportingGranularityFactor or timingReportingGranularityFactorExtended [35] and informs the LMF.

The mapping of measured/inferred quantity for each reporting resolution (k) is defined in Table 13.1.1A-1 to Table 13.1.1A-12.

Table 13.1.1A-1: Measurement report mapping for k=0

Table 13.1.1A-2: Measurement report mapping for k=1

Table 13.1.1A-3: Measurement report mapping for k=2

Table 13.1.1A-4: Measurement report mapping for k=3

Table 13.1.1A-5: Measurement report mapping for k=4

Table 13.1.1A-6: Measurement report mapping for k=5

Table 13.1.1A-7: Measurement report mapping for k=-1

Table 13.1.1A-8: Measurement report mapping for k=-2

Table 13.1.1A-9: Measurement report mapping for k=-3

Table 13.1.1A-10: Measurement report mapping for k=-4

Table 13.1.1A-11: Measurement report mapping for k=-5

Table 13.1.1A-12: Measurement report mapping for k=-6

## 13.2gNB Rx-Tx time difference

## 13.2.1Report mapping

The reporting range of gNB Rx-Tx time difference, as defined in Clause 5.2.3 of TS 38.215 [4], is defined from -985024Tc to +985024Tc. The reporting resolution is uniform across the reporting range and is defined as T = Tc2k where k is selected by gNB from the set {-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}.

Tc is defined in TS 38.211 [6].

LMF provides a recommended resolution parameter, timingReportingGranularityFactor or timingReportingGranularityFactorExtended [35]. gNB selects parameter k based on timingReportingGranularityFactor or timingReportingGranularityFactorExtended [35] and informs the LMF.

The mapping of measured/inferred quantity for each reporting resolution (k) is defined in table 13.2.1-1 to table 13.2.1-12.

Table 13.2.1-1: Measurement report mapping for k=0

Table 13.2.1-2: Measurement report mapping for k=1

Table 13.2.1-3: Measurement report mapping for k=1

Table 13.2.1-4: Measurement report mapping for k=3

Table 13.2.1-5: Measurement report mapping for k=4

Table 13.2.1-6: Measurement report mapping for k=5

Table 13.2.1-7: Measurement report mapping for k=-1

Table 13.2.1-8: Measurement report mapping for k=-2

Table 13.2.1-9: Measurement report mapping for k=-3

Table 13.2.1-10: Measurement report mapping for k=-4

Table 13.2.1-11: Measurement report mapping for k=-5

Table 13.2.1-12: Measurement report mapping for k=-6

## 13.2.1AAdditional Path Report Mapping for gNB Rx-Tx

The reporting range of additional path for gNB Rx-Tx time difference, as defined in Clause 5.2.3 of TS 38.215 [4], is defined from -8175Tc to 8175Tc. The reporting resolution is uniform across the reporting range and is defined as T = Tc2k where k is selected by gNB from the set {-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}.

Tc is defined in TS 38.211 [6].

LMF provides a recommended resolution parameter, timingReportingGranularityFactor or timingReportingGranularityFactorExtended [35]. gNB selects parameter k based on timingReportingGranularityFactor or timingReportingGranularityFactorExtended [35] and informs the LMF.

The mapping of measured/inferred quantity for each reporting resolution (k) is defined in table 13.2.1A-1 to table 13.2.1A-12.

Table 13.2.1A-1: Measurement report mapping for k=0

Table 13.2.1A-2: Measurement report mapping for k=1

Table 13.2.1A-3: Measurement report mapping for k=2

Table 13.2.1A-4: Measurement report mapping for k=3

Table 13.2.1A-5: Measurement report mapping for k=4

Table 13.2.1A-6: Measurement report mapping for k=5

Table 13.2.1A-7: Measurement report mapping for k=-1

Table 13.2.1A-8: Measurement report mapping for k=-2

Table 13.2.1A-9: Measurement report mapping for k=-3

Table 13.2.1A-10: Measurement report mapping for k=-4

Table 13.2.1A-11: Measurement report mapping for k=-5

Table 13.2.1A-12: Measurement report mapping for k=-6

## 13.2.2Measurement Accuracy Requirements

## 13.2.2.1Introduction

This clause defines accuracy requirements for measured/inferred gNB Rx-Tx time difference measurement in FR1 and FR2. The requirements are applicable for gNB supporting gNB Rx-Tx time difference measurement. The gNB, which declares the support for gNB Rx-Tx time difference measurement also declares that it meets gNB Rx-Tx time difference accuracy requirements at least for one side condition Ês/Iot ≥ +3 dB or Ês/Iot ≥ -13 dB.

## 13.2.2.2Requirements

The accuracy requirements for measured/inferred gNB Rx-Tx time difference measurement shall be within ±(X+Y) Tc under the following conditions:

-AWGN propagation conditions.

-The measured signals are in the directions covered by RoAoA of OTA reference sensitivity requirements for gNB type 1-O and 2-O BS

where

-X is defined in table 13.2.2.2-1 for gNB types 1-C, 1-H and 1-O and in table 13.2.2.2-2 for gNB type 2-O.

-Y is declared by manufacturer and can be different for different gNB types 1-C, 1-H, 1-O and 2-O.

NOTE:The measurement accuracy requirements in table 13.2.2.2-1 and table 13.2.2.2-2 are defined under an assumption that gNB is not mandated to perform receive beam sweeping.

Table 13.2.2.2-1: gNB Rx-Tx time difference absolute accuracy in FR1 for gNB type 1-C, 1-H and 1-O

Table 13.2.2.2-2: gNB Rx-Tx time difference absolute accuracy in FR2 for gNB type 2-O

## 13.3UL SRS RSRP measurement

## 13.3.1Report mapping

The reporting range of UL SRS RSRP, as defined in clause 5.2.5 of 38.215 [4], is defined from -156 dBm to -31 dBm with resolution 1 dB.

The mapping of measured quantity is defined in table 13.3.1-1. The range in the signalling may be larger than the guaranteed accuracy range.

Table 13.3.1-1: UL SRS RSRP report mapping

## 13.3.2Measurement accuracy requirements

## 13.3.2.1Introduction

This clause defines accuracy requirements for SRS-RSRP measurement in FR1 and FR2. The requirements are applicable for gNB supporting SRS-RSRP measurement. The gNB, which declares the support for SRS-RSRP measurement also declares that it meets SRS-RSRP accuracy requirements at least for one side condition Ês/Iot ≥ +3 dB or Ês/Iot ≥ -13 dB.

## 13.3.2.2Requirements

The accuracy requirements in table 13.3.2.2-1, table 13.3.2.2-2 and table 13.3.2.2-3 are valid under the following conditions:

-AWGN propagation conditions.

-The measured signals are in the directions covered by RoAoA of OTA reference sensitivity requirements for gNB type 1-O and 2-O BS

NOTE:The measurement accuracy requirements in table 13.3.2.2-1, table 13.3.2.2-2 and table 13.3.2.2-3 are defined under an assumption that gNB is not mandated to perform receive beam sweeping.

Table 13.3.2.2-1 gNB SRS-RSRP absolute accuracy requirements in FR1 for gNB type 1-C

Table 13.3.2.2-2 gNB SRS-RSRP absolute accuracy requirements in FR1 for gNB type 1-H and 1-O

Table 13.3.2.2-3 gNB SRS-RSRP absolute accuracy requirements in FR2 for gNB type 2-O

## 13.4AoA/ZoA

## 13.4.1Report mapping

The reporting range of UL Angle of Arrival (UL-AoA), as defined in clause 5.2.4 of TS 38.215 [4], is defined from -180 degree to +180 degree for azimuth angle of arrival (A-AoA). The reporting resolution is 0.1 degree.

The reporting range of UL Angle of Arrival, as defined in clause 5.2.4 of TS 38.215 [4], is defined from 0 degree to +180 degree for zenith angle of arrival (Z-AoA). The reporting resolution is 0.1 degree.

The mapping of A-AoA measured quantity is defined in table 13.4.1-1. The mapping of Z-AoA measured quantity is defined in table 13.4.1-2.

Table 13.4.1-1: Azimuth Angle of Arrival (A-AoA) measurement report mapping

Table 13.4.1-2: Zenith Angle of Arrival (Z-AoA) measurement report mapping

## 13.5Timing advance (TADV)

## 13.5.1Report mapping

The reporting range of TADV, as defined in clause 5.2.7 of TS 38.215 [4], is defined from 0 to 3150848 Tc with 128 Tc resolution for timing advance less than 262144 Tc, and 512 Tc for timing advance greater than or equal to 262144 Tc.

Tc is defined in TS 38.211 [6].

The mapping of measured quantity is defined in table 13.5.1-1.

Table 13.5.1-1: TADV measurement report mapping

NOTE:For report mapping, TADV is equal to (gNB Rx – Tx time difference) + NTA_offset, where NTA_offset is based on the information n-TimingAdvanceOffset as specified in TS 38.331 [2].

## 13.6UL SRS RSRPP measurement

## 13.6.1Report mapping

The reporting range of UL SRS RSRPP, as defined in clause 5.2.5 of 38.215 [4], is defined from -156 dBm to -31 dBm with resolution 1 dB.

The mapping of measured quantity is defined in table 13.6.1-1. The range in the signalling may be larger than the guaranteed accuracy range.

Table 13.6.1-1: UL SRS RSRPP report mapping

## 13.7gNB Rx-Tx time difference measurements for RTT-based PDC

## 13.7.1Report mapping

The reporting range of gNB Rx-Tx time difference, as defined in clause 5.2.3 of TS 38.215 [4], is defined from -985024Tc to +985024Tc. The reporting resolution is uniform across the reporting range and is defined as Tc*32.

Tc is defined in TS 38.211 [6].

The mapping of measured quantity is defined in table 13.7.1-1.

Table 13.7.1-1: gNB Rx-Tx time difference measurement report mapping

## 13.7.2Measurement Accuracy Requirements

## 13.7.2.1Introduction

This clause defines accuracy requirements for gNB Rx-Tx time difference measurement in FR1 and FR2. The requirements are applicable for gNB supporting gNB Rx-Tx time difference measurement for RTT-based PDC.

## 13.7.2.2Requirements

The accuracy requirements for gNB Rx-Tx time difference measurement for RTT-based PDC shall be within ±(X+Y) Tc under the following conditions:

-AWGN propagation conditions.

-The measured signals are in the directions covered by RoAoA of OTA reference sensitivity requirements for gNB type 1-O and 2-O BS

where

-X is defined in table 13.7.2.2-1 for gNB types 1-C, 1-H and 1-O and in table 13.7.2.2-2 for gNB type 2-O.

-Y is declared by manufacturer and can be different for different gNB types 1-C, 1-H, 1-O and 2-O.

NOTE:The measurement accuracy requirements in table 13.7.2.2-1 and table 13.7.2.2-2 are defined under an assumption that gNB is not mandated to perform receive beam sweeping.

Table 13.7.2.2-1: gNB Rx-Tx time difference absolute accuracy in FR1 for gNB type 1-C, 1-H and 1-O

Table 13.7.2.2-2: gNB Rx-Tx time difference absolute accuracy in FR2 for gNB type 2-O

## 13.8UL-RSCP measurement

## 13.8.1Report mapping

The reporting range of UL-RSCP, as defined in clause 5.2.8 of 38.215 [4], is defined from 0 degree to 360 degree. The reporting resolution is 0.1 degree.

The mapping of UL-RSCP measured quantity is defined in table 13.8.1-1.

Table 13.8.1-1: UL-RSCP report mapping

## 13.9UL SRS-TDCT measurement

## 13.9.1Report mapping

The reporting range of UL SRS-TDCT measurement, as defined in Clause 5.2.9 of TS 38.215 [4], is defined from -985024×Tc to +985024×Tc. The reporting resolution is uniform across the reporting range and is defined as T = Tc×2k, where k is selected by gNB from the set {0, 1, 2, 3, 4, 5}.

Tc is defined in TS 38.211 [6].

LMF provides a recommended resolution parameter, timingReportingGranularityFactor [35]. gNB selects parameter k based on timingReportingGranularityFactor [35] and informs the LMF.

The mapping of measured quantity for each reporting resolution (k) is defined in table 13.9.1-1 to table 13.9.1-6.

Table 13.9.1-1: Measurement report mapping for k=0

Table 13.9.1-2: Measurement report mapping for k=1

Table 13.9.1-3: Measurement report mapping for k=2

Table 13.9.1-4: Measurement report mapping for k=3

Table 13.9.1-5: Measurement report mapping for k=4

Table 13.9.1-6: Measurement report mapping for k=5

## 13.10UL SRS-TDCP measurement

## 13.10.1Report mapping

The reporting range of UL SRS-TDCP measurement, as defined in clause 5.2.10 of 38.215 [4], is defined from -156 dBm to -31 dBm with resolution 1 dB.

The mapping of measured quantity is defined in table 13.10.1-1.

Table 13.10.1-1: UL SRS-TDCP report mapping
