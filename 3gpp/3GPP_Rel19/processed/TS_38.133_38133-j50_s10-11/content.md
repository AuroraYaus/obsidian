---
type: spec
aliases:
  - 38.133_38133-j50_s10-11
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_s10-11/content.md"
---
# TS 38.133 38133-j50_s10-11

## 10Measurement Performance requirements

## 10.1NR measurements

## 10.1.1Introduction

The requirements in clause 10.1 apply as follows:

-intra-frequency requirements apply for PCell measurements in SA, NR-DC, or NE-DC operation mode,

-intra-frequency requirements apply for PSCell measurements in NR-DC or EN-DC operation mode,

-intra-frequency requirements apply for SCell measurements in SA operation mode with NR CA or any MR-DC operation mode with NR CA,

-inter-frequency requirements apply for non-serving cell measurements on NR carrier frequencies.

-inter-frequency requirements apply for measurements from one cell on a frequency compared to the measurement from another cell on a different frequency.

In the requirements of clause 10.1, the exceptions for side conditions apply as follows:

-for the UE capable of CA but not configured with any SCell, the applicable exceptions for side conditions are specified in annex B, clause B.3.2.1 for UE supporting CA in FR1, and clause B.3.2.3 for UE supporting CA in FR2, respectively;

-for the UE capable of CA and configured with at least one SCell, the applicable exceptions for side conditions are specified in Annex B, clause B.3.2.2 for UE configured with CA in FR1, and clause B.3.2.4 for UE supporting CA in FR2, respectively;

-for the UE capable of SUL but not configured with SUL, the applicable exceptions for side conditions are specified in annex B, clause B.3.4.1 for UE supporting SUL in FR1;

-for the UE capable of SUL and configured with at least one SUL, the applicable exceptions for side conditions are specified in annex B, clause B.3.4.2 for UE configured with SUL in FR1.

## 10.1.2Intra-frequency RSRP accuracy requirements for FR1

## 10.1.2.1Intra-frequency SS-RSRP accuracy requirements

## 10.1.2.1.1Absolute SS-RSRP Accuracy

Unless otherwise specified, the accuracy requirements for absolute SS-RSRP in this clause apply to a cell on the same frequency as that of the serving cell in FR1. The accuracy requirements in this clause are also applicable when highSpeedMeasFlag-r16 or highSpeedMeasCA-Scell-r17 is configured.

The accuracy requirements in table 10.1.2.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for each relevant SSB.

Table 10.1.2.1.1-1: SS-RSRP Intra-frequency absolute accuracy in FR1

## 10.1.2.1.2Relative SS-RSRP Accuracy

The relative SS-RSRP accuracy is defined as the SS-RSRP measured from one cell compared to the SS-RSRP measured from another cell on the same frequency, or between any two SS-RSRP levels measured on the same cell in FR1. The accuracy requirements in this clause are also applicable when highSpeedMeasFlag-r16 or highSpeedMeasCA-Scell-r17 is configured.

The accuracy requirements in table 10.1.2.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for each relevant SSB.

Table 10.1.2.1.2-1: SS-RSRP Intra-frequency relative accuracy in FR1

## 10.1.2.2Void

## 10.1.2.3Intra-frequency CSI-RSRP accuracy requirements

## 10.1.2.3.1Absolute CSI-RSRP Accuracy

Unless otherwise specified, the requirements for absolute CSI-RSRP accuracy in this clause apply to a cell where the CSI-RS resources to be measured have the same center frequency as the CSI-RS resources indicated for measurement in the serving cell in FR1.

The accuracy requirements in table 10.1.2.3.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for each associated SSB.

-Conditions for intra-frequency measurements are fulfilled according to Annex B.2.12 for a corresponding Band for each relevant CSI-RS to be measured.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3. The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in Table 10.1.2.3.1-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE:The reference measurement timing for one layer for intra-frequency measurement is serving cell timing.

Table 10.1.2.3.1-1: CSI-RSRP Intra-frequency absolute accuracy in FR1

## 10.1.2.3.2Relative CSI-RSRP Accuracy

The relative CSI-RSRP accuracy is defined as the CSI-RSRP measured from one cell compared to the CSI-RSRP measured from another cell on the same center frequency, or between any two CSI-RSRP levels measured on the same cell in FR1.

The accuracy requirements in table 10.1.2.3.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for each associated SSB.

-Conditions for intra-frequency measurements are fulfilled according to Annex B.2.12 for a corresponding Band for each relevant CSI-RS to be measured.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3. The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in Table 10.1.2.3.2-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE:The reference measurement timing for one layer for intra-frequency measurement is serving cell timing.

Table 10.1.2.3.2-1: CSI-RSRP Intra-frequency relative accuracy in FR1

## 10.1.2BIntra-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode Measurements

## 10.1.2B.1Intra-frequency SS-RSRP accuracy requirements

The requirements in this clause are applicable for a UE:

-in state RRC_IDLE or RRC_INACTIVE

-that is synchronised to the cell that is measured.

The requirements are for absolute SS-RSRP accuracy.

## 10.1.2B.1.1Absolute SS-RSRP Accuracy

Unless otherwise specified, the requirements for absolute SS-RSRP accuracy in this clause apply to the serving cell in FR1.

The accuracy requirements in table 10.1.2B.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.1.2 for a corresponding Band for each relevant SSB.

Table 10.1.2B.1.1-1: SS-RSRP Intra-frequency absolute accuracy in FR1

## 10.1.2CIntra-frequency RSRP accuracy requirements for FR1 SAN

## 10.1.2C.1Intra-frequency SS-RSRP accuracy requirements

## 10.1.2C.1.1Absolute SS-RSRP Accuracy

Unless otherwise specified, the requirements for absolute SS-RSRP accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR1.

The accuracy requirements in table 10.1.2C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.17 for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.2C.1.1-1: SS-RSRP Intra-frequency absolute accuracy in FR1

## 10.1.2C.1.2Relative SS-RSRP Accuracy

The relative SS-RSRP accuracy is defined as the SS-RSRP measured from one cell compared to the SS-RSRP measured from another cell on the same frequency, or between any two SS-RSRP levels measured on the same cell in FR1.

The accuracy requirements in table 10.1.2C.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.17 for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.2C.1.2-1: SS-RSRP Intra-frequency relative accuracy in FR1

<End of Change 1>

## 10.1.2DIntra-frequency RSRP accuracy requirements for RedCap UE with Satellite Access in FR1

## 10.1.2D.1Intra-frequency SS-RSRP accuracy requirements

## 10.1.2D.1.1Absolute SS-RSRP Accuracy

Unless otherwise specified, the requirements for absolute SS-RSRP accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR1.

The accuracy requirements in clause 10.1.2C.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the absolute accuracy requirements in table 10.1.2D.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.17 for both 1Rx and 2Rx RedCap UE for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.2D.1.1-1: SS-RSRP Intra-frequency absolute accuracy for 1Rx RedCap UE in FR1

## 10.1.2D.1.2Relative SS-RSRP Accuracy

The relative SS-RSRP accuracy is defined as the SS-RSRP measured from one cell compared to the SS-RSRP measured from another cell on the same frequency, or between any two SS-RSRP levels measured on the same cell in FR1.

The accuracy requirements in clause 10.1.2C.1.2 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the relative accuracy requirements in table 10.1.2D.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.17 for both 1Rx and 2Rx RedCap UE for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.2D.1.2-1: SS-RSRP Intra-frequency relative accuracy for 1Rx RedCap UE in FR1

## 10.1.3Intra-frequency RSRP accuracy requirements for FR2

## 10.1.3.1Intra-frequency SS-RSRP accuracy requirements

## 10.1.3.1.1Absolute SS-RSRP Accuracy

Unless otherwise specified, the requirements for absolute SS-RSRP accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR2.

The accuracy requirements in table 10.1.3.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.3.1.1-1: SS-RSRP Intra-frequency absolute accuracy in FR2

## 10.1.3.1.2Relative SS-RSRP Accuracy

The relative SS-RSRP accuracy is defined as the SS-RSRP measured from one cell compared to the SS-RSRP measured from another cell on the same frequency, or between any two SS-RSRP levels measured on the same cell in FR2.

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.3.1.2-1: SS-RSRP Intra-frequency relative accuracy in FR2

## 10.1.3.2Void

## 10.1.3.3Intra-frequency CSI-RSRP accuracy requirements

## 10.1.3.3.1Absolute CSI-RSRP Accuracy

Unless otherwise specified, the requirements for absolute CSI-RSRP accuracy in this clause apply to a cell where the CSI-RS resources to be measured have the same center frequency as the CSI-RS resources indicated for measurement in the serving cell in FR2.

The accuracy requirements in table 10.1.3.3.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for each associated SSB(s).

-Conditions for intra-frequency measurements are fulfilled according to Annex B.2.12 for a corresponding Band for each relevant CSI-RS to be measured.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3. The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.3.3.1-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE:The reference measurement timing for one layer for intra-frequency measurement is serving cell timing.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.3.3.1-1: CSI-RSRP Intra-frequency absolute accuracy in FR2

## 10.1.3.3.2Relative CSI-RSRP Accuracy

The relative CSI-RSRP accuracy is defined as the CSI-RSRP measured from one cell compared to the CSI-RSRP measured from another cell on the same center frequency, or between any two CSI-RSRP levels measured on the same cell in FR2.

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for each associated SSB(s).

-Conditions for intra-frequency measurements are fulfilled according to Annex B.2.12 for a corresponding Band for each CSI-RS to be measured.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3. The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.3.3.2-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE:The reference measurement timing for one layer for intra-frequency measurement is serving cell timing.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.3.3.2-1: CSI-RSRP Intra-frequency relative accuracy in FR2

## 10.1.3BIntra-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode Measurements

## 10.1.3B.1Intra-frequency SS-RSRP accuracy requirements

The requirements in this clause are applicable for a UE:

-in state RRC_IDLE or RRC_INACTIVE

-that is synchronised to the cell that is measured.

The requirements are for absolute SS-RSRP accuracy.

## 10.1.3B.1.1Absolute SS-RSRP Accuracy

Unless otherwise specified, the requirements for absolute SS-RSRP accuracy in this clause apply to the serving cell in FR2.

The accuracy requirements in table 10.1.3B.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.1.2 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.3B.1.1-1: SS-RSRP Intra-frequency absolute accuracy in FR2

## 10.1.3CIntra-frequency RSRP accuracy requirements for FR2-NTN

## 10.1.3C.1Intra-frequency SS-RSRP accuracy requirements

## 10.1.3C.1.1Absolute SS-RSRP Accuracy

Unless otherwise specified, the requirements for absolute SS-RSRP accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR2-NTN.

The accuracy requirements in table 10.1.3C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 10.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.17 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

Table 10.1.3C.1.1-1: SS-RSRP Intra-frequency absolute accuracy in FR2-NTN

## 10.1.3C.1.2Relative SS-RSRP Accuracy

The relative SS-RSRP accuracy is defined as the SS-RSRP measured from one cell compared to the SS-RSRP measured from another cell on the same frequency, or between any two SS-RSRP levels measured on the same cell in FR2-NTN.

-Conditions defined in clause 10.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.17 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

Table 10.1.3C.1.2-1: SS-RSRP Intra-frequency relative accuracy in FR2-NTN

## 10.1.4Inter-frequency RSRP accuracy requirements for FR1

## 10.1.4.1Inter-frequency SS-RSRP accuracy requirements

## 10.1.4.1.1Absolute SS-RSRP Accuracy in FR1

The requirements for absolute SS-RSRP accuracy in this clause apply to a cell on a frequency in FR1 that has different carrier frequency from the serving cell. The accuracy requirements in this clause are also applicable when highSpeedMeasInterFreq-r17 is configured.

The accuracy requirements in table 10.1.4.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for each relevant SSB.

Table 10.1.4.1.1-1: SS-RSRP Inter-frequency Absolute accuracy in FR1

## 10.1.4.1.2Relative SS-RSRP Accuracy in FR1

The relative SS-RSRP accuracy in inter-frequency case is defined as the RSRP measured from one cell on a frequency in FR1compared to the RSRP measured from another cell on a different frequency in FR1. The accuracy requirements in this clause are also applicable when highSpeedMeasInterFreq-r17 is configured.

The accuracy requirements in Table 10.1.4.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] Clause 7.3 for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.3 for a corresponding Band for each relevant SSB.

-|SSB_RP1dBm - SSB_RP2dBm|  27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

Table 10.1.4.1.2-1: SS-RSRP Inter-frequency relative accuracy in FR1

## 10.1.4.2Void

## 10.1.4.3Inter-frequency CSI-RSRP accuracy requirements

## 10.1.4.3.1Absolute CSI-RSRP Accuracy in FR1

The requirements for absolute CSI-RSRP accuracy in this clause apply to a cell where the CSI-RS resources to be measured have the different center frequency as the CSI-RS resources indicated for measurement in the serving cell in FR1.

The accuracy requirements in table 10.1.4.3.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for each relevant SSB.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.13 for a corresponding Band for each relevant CSI-RS to be measured.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3. The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.4.3.1-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE:The reference measurement timing for one layer for inter-frequency measurement is up to UE implementation and shall be based on the timing of one of the target cells.

Table 10.1.4.3.1-1: CSI-RSRP Inter-frequency Absolute accuracy in FR1

## 10.1.4.3.2Relative CSI-RSRP Accuracy in FR1

The relative CSI-RSRP accuracy in inter-frequency case is defined as the CSI-RSRP measured from one cell on a frequency in FR1compared to the CSI-RSRP measured from another cell on a different frequency in FR1.

The accuracy requirements in table 10.1.4.3.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] clause 7.3 for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for each relevant SSB.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.13 for a corresponding Band for each relevant CSI-RS to be measured.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3. The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.4.3.2-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

•NOTE: The reference measurement timing for one layer for inter-frequency measurement is up to UE implementation and shall be based on the timing of one of the target cells.

-|CSI_RP1dBm - CSI_RP2dBm|  27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

Table 10.1.4.3.2-1: CSI-RSRP Inter-frequency relative accuracy in FR1

## 10.1.4BInter-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode Measurements

## 10.1.4B.1Inter-frequency SS-RSRP accuracy requirements

The requirements in this clause are applicable for a UE:

-in state RRC_IDLE or RRC_INACTIVE

-that is synchronised to the cell that is measured.

The requirements are for absolute SS-RSRP accuracy.

## 10.1.4B.1.1Absolute SS-RSRP Accuracy in FR1

The requirements for absolute SS-RSRP accuracy in this clause apply to a cell on a frequency in FR1 that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.4B.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.1.3 for a corresponding Band for each relevant SSB.

Table 10.1.4B.1.1-1: SS-RSRP Inter-frequency Absolute accuracy in FR1

## 10.1.4CInter-frequency RSRP accuracy requirements for FR1 SAN

## 10.1.4C.1Inter-frequency SS-RSRP accuracy requirements

## 10.1.4C.1.1Absolute SS-RSRP Accuracy in FR1

The requirements for absolute SS-RSRP accuracy in this clause apply to a cell on a frequency in FR1 that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.4C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.4C.1.1-1: SS-RSRP Inter-frequency Absolute accuracy in FR1

## 10.1.4C.1.2Relative SS-RSRP Accuracy in FR1

The relative SS-RSRP accuracy in inter-frequency case is defined as the RSRP measured from one cell on a frequency in FR1compared to the RSRP measured from another cell on a different frequency in FR1.

The accuracy requirements in Table 10.1.4C.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] Clause 7.3 for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.18 for a corresponding Band for each relevant SSB.

-|SSB_RP1dBm - SSB_RP2dBm|  27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

Table 10.1.4C.1.2-1: SS-RSRP Inter-frequency relative accuracy in FR1

## 10.1.4DInter-frequency RSRP accuracy requirements for RedCap UE with Satellite Access in FR1

## 10.1.4D.1Inter-frequency SS-RSRP accuracy requirements

## 10.1.4D.1.1Absolute SS-RSRP Accuracy in FR1

The requirements for absolute SS-RSRP accuracy in this clause apply to a cell on a frequency in FR1 that has different carrier frequency from the serving cell.

The accuracy requirements in clause 10.1.4C.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the absolute accuracy requirements in table 10.1.4D.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for both 1Rx and 2Rx RedCap UE for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.4D.1.1-1: SS-RSRP Inter-frequency Absolute accuracy for 1Rx RedCap UE in FR1

## 10.1.4D.1.2Relative SS-RSRP Accuracy in FR1

The relative SS-RSRP accuracy in inter-frequency case is defined as the RSRP measured from one cell on a frequency in FR1compared to the RSRP measured from another cell on a different frequency in FR1.

The accuracy requirements in clause 10.1.4C.1.2 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the relative accuracy requirements in table 10.1.4D.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] Clause 7.3 for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.18 for both 1Rx and 2Rx RedCap UE for a corresponding Band for each relevant SSB.

-|SSB_RP1dBm - SSB_RP2dBm|  27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

Table 10.1.4D.1.2-1: SS-RSRP Inter-frequency relative accuracy for 1Rx RedCap UE in FR1

## 10.1.5Inter-frequency RSRP accuracy requirements for FR2

## 10.1.5.1Inter-frequency SS-RSRP accuracy requirements

## 10.1.5.1.1Absolute SS-RSRP Accuracy

Unless otherwise specified, the requirements for absolute SS-RSRP accuracy in this clause apply to a cell on a frequency in FR2 that is on a different frequency than the serving cell.

The accuracy requirements in table 10.1.5.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.5.1.1-1: SS-RSRP Inter-frequency absolute accuracy in FR2

## 10.1.5.1.2Relative SS-RSRP Accuracy

The relative SS-RSRP accuracy is defined as the SS-RSRP measured from one cell on a frequency in FR2 compared to the SS-RSRP measured from another cell on another frequency in FR2.

The accuracy requirements in table 10.1.5.1.2-1 are valid under the following conditions:

-Conditions defined in TS 38.101-2 [19] clause 7.3 for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for each relevant SSB.

--|SSB_RP1dBm - SSB_RP2dBm|  27dB

-|Channel 1_Io Channel 2_Io |  20 dB

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.5.1.2-1: SS-RSRP Inter-frequency relative accuracy in FR2

## 10.1.5.2Void

## 10.1.5.3Inter-frequency CSI-RSRP accuracy requirements

## 10.1.5.3.1Absolute CSI-RSRP Accuracy

Unless otherwise specified, the requirements for absolute CSI-RSRP accuracy in this clause apply to a cell on a frequency in FR2 where the CSI-RS resources to be measured have the different center frequency as the CSI-RS resources indicated for measurement in the serving cell.

The accuracy requirements in table 10.1.5.3.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for each relevant associated SSB.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.13 for a corresponding Band for each relevant CSI-RS to be measured.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3. The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.5.3.1-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE:The reference measurement timing for one layer for inter-frequency measurement is up to UE implementation and shall be based on the timing of one of the target cells.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.5.3.1-1: CSI-RSRP Inter-frequency absolute accuracy in FR2

## 10.1.5.3.2Relative CSI-RSRP Accuracy

The relative CSI-RSRP accuracy in inter-frequency case is defined as the CSI-RSRP measured from one cell on a frequency in FR2 compared to the CSI-RSRP measured from another cell on another frequency in FR2.

The accuracy requirements in table 10.1.5.3.2-1 are valid under the following conditions:

-Conditions defined in TS 38.101-2 [19] clause 7.3 for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for each relevant associated SSB.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.13 for a corresponding Band for each relevant CSI-RS to be measured.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3. The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.5.3.2-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE:The reference measurement timing for one layer for inter-frequency measurement is up to UE implementation and shall be based on the timing of one of the target cells.

-|CSI_RP1dBm - CSI_RP2dBm|  27dB

-|Channel 1_Io Channel 2_Io |  20 dB

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.5.3.2-1: CSI-RSRP Inter-frequency relative accuracy in FR2

## 10.1.5BInter-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode Measurements

## 10.1.5B.1Inter-frequency SS-RSRP accuracy requirements

The requirements in this clause are applicable for a UE:

-in state RRC_IDLE or RRC_INACTIVE

-that is synchronised to the cell that is measured.

The requirements are for absolute SS-RSRP accuracy.

## 10.1.5B.1.1Absolute SS-RSRP Accuracy

Unless otherwise specified, the requirements for absolute SS-RSRP accuracy in this clause apply to a cell on a frequency in FR2 that is on a different frequency than the serving cell.

The accuracy requirements in table 10.1.5B.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.1.3 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.5B.1.1-1: SS-RSRP Inter-frequency absolute accuracy in FR2

## 10.1.5CInter-frequency RSRP accuracy requirements for FR2-NTN

## 10.1.5C.1Inter-frequency SS-RSRP accuracy requirements

## 10.1.5C.1.1Absolute SS-RSRP Accuracy

Unless otherwise specified, the requirements for absolute SS-RSRP accuracy in this clause apply to a cell on a frequency in FR2-NTN that is on a different frequency than the serving cell.

The accuracy requirements in table 10.1.5C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 10.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

Table 10.1.5C.1.1-1: SS-RSRP Inter-frequency absolute accuracy in FR2-NTN

## 10.1.5C.1.2Relative SS-RSRP Accuracy

The relative SS-RSRP accuracy is defined as the SS-RSRP measured from one cell on a frequency in FR2-NTN compared to the SS-RSRP measured from another cell on another frequency in FR2-NTN.

The accuracy requirements in table 10.1.5C.1.2-1 are valid under the following conditions:

-Conditions defined in 38.101-5 [19] clause 10.3 for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for a corresponding Band for each relevant SSB.

-|SSB_RP1dBm - SSB_RP2dBm|  27dB

-|Channel 1_Io Channel 2_Io |  20 dB

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

Table 10.1.5C.1.2-1: SS-RSRP Inter-frequency relative accuracy in FR2-NTN

## 10.1.6RSRP Measurement Report Mapping

The reporting range of SS-RSRP and CSI-RSRP for L3 reporting is defined from -156 dBm to -31 dBm with 1 dB resolution. The reporting range of SS-RSRP, CSI-RSRP and P-L1-RSRP for L1 reporting is defined from -140 to -44 dBm with 1 dB resolution.

The mapping of measured quantity is defined in table 10.1.6.1-1. The range in the signalling may be larger than the guaranteed accuracy range.

The reporting range of differential SS-RSRP, CSI-RSRP and P-L1-RSRP for L1 reporting is defined from 0 dB to -30 dB with 2 dB resolution.

The mapping of measured quantity is defined in table 10.1.6.1-2. The range in the signalling may be larger than the guaranteed accuracy range.

Table 10.1.6.1-1: SS-RSRP, CSI-RSRP measurement report mapping and P-L1-RSRP report mapping

Table 10.1.6.1-2: Differential SS-RSRP, CSI-RSRP measurement (for L1 reporting) report mapping and  P-L1-RSRP report mapping

## 10.1.7Intra-frequency RSRQ accuracy requirements for FR1

## 10.1.7.1Intra-frequency SS-RSRQ accuracy requirements in FR1

## 10.1.7.1.1Absolute SS-RSRQ Accuracy in FR1

Unless otherwise specified, the requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR1. The accuracy requirements in this clause are also applicable when highSpeedMeasFlag-r16 or highSpeedMeasCA-Scell-r17 is configured.

The accuracy requirements in table 10.1.7.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for each relevant SSB.

Table 10.1.7.1.1-1: SS-RSRQ Intra-frequency absolute accuracy in FR1

## 10.1.7.2Intra-frequency CSI-RSRQ accuracy requirements

## 10.1.7.2.1Absolute CSI-RSRQ Accuracy

Unless otherwise specified, the requirements for absolute CSI-RSRQ accuracy in this clause apply to the intra-frequency measurement defined in clause 9.10.2.1 in FR1.

The accuracy requirements in table 10.1.7.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for associated SSB.

-Conditions for intra-frequency measurements are fulfilled according to Annex B.2.12 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in Table 10.1.7.2.1-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE:The reference measurement timing for one layer for intra-frequency measurement is serving cell timing.

Table 10.1.7.2.1-1: CSI-RSRQ Intra-frequency absolute accuracy in FR1

## 10.1.7BIntra-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode Measurements

## 10.1.7B.1Intra-frequency SS-RSRQ accuracy requirements in FR1

The requirements in this clause are applicable for a UE:

-in state RRC_IDLE or RRC_INACTIVE

-that is synchronised to the cell that is measured.

The requirements are for absolute SS-RSRQ accuracy.

## 10.1.7B.1.1Absolute SS-RSRQ Accuracy in FR1

Unless otherwise specified, the requirements for absolute SS-RSRQ accuracy in this clause apply to the serving cell in FR1.

The accuracy requirements in table 10.1.7B.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.1.2 for a corresponding Band for each relevant SSB.

Table 10.1.7B.1.1-1: SS-RSRQ Intra-frequency absolute accuracy in FR1

## 10.1.7CIntra-frequency RSRQ accuracy requirements for FR1 SAN

## 10.1.7C.1Intra-frequency SS-RSRQ accuracy requirements in FR1

## 10.1.7C.1.1Absolute SS-RSRQ Accuracy in FR1

Unless otherwise specified, the requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR1.

The accuracy requirements in table 10.1.7C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.17 for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.7C.1.1-1: SS-RSRQ Intra-frequency absolute accuracy in FR1

## 10.1.7DIntra-frequency RSRQ accuracy requirements for RedCap UE with Satellite Access in FR1

## 10.1.7D.1Intra-frequency SS-RSRQ accuracy requirements in FR1

## 10.1.7D.1.1Absolute SS-RSRQ Accuracy in FR1

Unless otherwise specified, the requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR1.

The accuracy requirements in clause 10.1.7C.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the absolute accuracy requirements in table 10.1.7D.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.17 for both 1Rx and 2Rx RedCap UE for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.7D.1.1-1: SS-RSRQ Intra-frequency absolute accuracy for 1Rx RedCap UE in FR1

## 10.1.8Intra-frequency RSRQ accuracy requirements for FR2

## 10.1.8.1Intra-frequency SS-RSRQ accuracy requirements in FR2

## 10.1.8.1.1Absolute SS-RSRQ Accuracy in FR2

Unless otherwise specified, the requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR2.

The accuracy requirements in table 10.1.8.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.8.1.1-1: SS-RSRQ Intra-frequency absolute accuracy in FR2

## 10.1.8.2Intra-frequency CSI-RSRQ accuracy requirements

## 10.1.8.2.1Absolute CSI-RSRQ Accuracy

Unless otherwise specified, the requirements for absolute CSI-RSRQ accuracy in this clause apply to the intra-frequency measurement defined in clause 9.10.2.1 in FR2.

The accuracy requirements in table 10.1.8.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for each relevant SSB.

-Conditions for intra-frequency measurements are fulfilled according to Annex B.2.12 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in Table 10.1.8.2.1-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE:The reference measurement timing for one layer for intra-frequency measurement is serving cell timing.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.8.2.1-1: CSI-RSRQ Intra-frequency absolute accuracy in FR2

## 10.1.8BIntra-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode Measurements

## 10.1.8B.1Intra-frequency SS-RSRQ accuracy requirements in FR2

The requirements in this clause are applicable for a UE:

-in state RRC_IDLE or RRC_INACTIVE

-that is synchronised to the cell that is measured.

The requirements are for absolute SS-RSRQ accuracy.

## 10.1.8B.1.1Absolute SS-RSRQ Accuracy in FR2

Unless otherwise specified, the requirements for absolute SS-RSRQ accuracy in this clause apply to the serving cell in FR2.

The accuracy requirements in table 10.1.8B.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.1.2 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.8B.1.1-1: SS-RSRQ Intra-frequency absolute accuracy in FR2

## 10.1.8CIntra-frequency RSRQ accuracy requirements for FR2-NTN

## 10.1.8C.1Intra-frequency SS-RSRQ accuracy requirements in FR2-NTN

## 10.1.8C.1.1Absolute SS-RSRQ Accuracy in FR2-NTN

Unless otherwise specified, the requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR2-NTN.

The accuracy requirements in table 10.1.8C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 10.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.17 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

Table 10.1.8C.1.1-1: SS-RSRQ Intra-frequency absolute accuracy in FR2-NTN

## 10.1.9Inter-frequency RSRQ accuracy requirements for FR1

## 10.1.9.1Inter-frequency SS-RSRQ accuracy requirements in FR1

## 10.1.9.1.1Absolute SS-RSRQ Accuracy in FR1

The requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on a frequency in FR1 that has different carrier frequency from the serving cell. The accuracy requirements in this clause are also applicable when highSpeedMeasInterFreq-r17 is configured.

The accuracy requirements in table 10.1.9.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for each relevant SSB.

Table 10.1.9.1.1-1: SS-RSRQ Inter-frequency absolute accuracy in FR1

## 10.1.9.1.2Relative SS-RSRQ Accuracy in FR1

The relative SS-RSRQ accuracy in inter-frequency case is defined as the RSRQ measured from one cell on a frequency in FR1 compared to the RSRP measured from another cell on a different frequency in FR1. The accuracy requirements in this clause are also applicable when highSpeedMeasInterFreq-r17 is configured.

The accuracy requirements in table 10.1.9.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for each relevant SSB.

-|SSB_RP1dBm - SSB_RP2dBm|  27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

Table 10.1.9.1.2-1: SS-RSRQ Inter-frequency relative accuracy in FR1

## 10.1.9.2Inter-frequency CSI-RSRQ accuracy requirements

## 10.1.9.2.1Absolute CSI-RSRQ Accuracy

Unless otherwise specified, the requirements for absolute CSI-RSRQ accuracy in this clause apply to the inter-frequency measurement defined in clause 9.10.3.1 in FR1.

The accuracy requirements in table 10.1.9.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for associated SSB.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.13 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

•The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.9.2.1-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE:The reference measurement timing for one layer for inter-frequency measurement is up to UE implementation and shall be based on the timing of one of the target cells.

Table 10.1.9.2.1-1: CSI-RSRQ Inter-frequency absolute accuracy in FR1

## 10.1.9.2.2Relative CSI-RSRQ Accuracy

The relative CSI-RSRQ accuracy is defined as the CSI-RSRQ measured from one cell compared to the CSI-RSRQ measured from another cell with the same center frequency, or between any two CSI-RSRQ levels measured on the same cell in FR1.

The accuracy requirements in table 10.1.9.2.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for the associated SSB.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.13 for a corresponding Band for each relevant CSI-RS.

-|CSI_RP1dBm - CSI_RP2dBm|  27 dB

-|Channel 1_Io  Channel 2_Io |  20 dB

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

•The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.9.2.2-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE:The reference measurement timing for one layer for inter-frequency measurement is up to UE implementation and shall be based on the timing of one of the target cells.

Table 10.1.9.2.2-1: CSI-RSRQ Inter-frequency relative accuracy in FR1

## 10.1.9BInter-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode Measurements

## 10.1.9B.1Inter-frequency SS-RSRQ accuracy requirements in FR1

The requirements in this clause are applicable for a UE:

-in state RRC_IDLE or RRC_INACTIVE

-that is synchronised to the cell that is measured.

The requirements are for absolute SS-RSRQ accuracy.

## 10.1.9B.1.1Absolute SS-RSRQ Accuracy in FR1

The requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on a frequency in FR1 that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.9B.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.1.3 for a corresponding Band for each relevant SSB.

Table 10.1.9B.1.1-1: SS-RSRQ Inter-frequency absolute accuracy in FR1

## 10.1.9CInter-frequency RSRQ accuracy requirements for FR1 SAN

## 10.1.9C.1Inter-frequency SS-RSRQ accuracy requirements in FR1

## 10.1.9C.1.1Absolute SS-RSRQ Accuracy in FR1

The requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on a frequency in FR1 that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.9C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.9C.1.1-1: SS-RSRQ Inter-frequency absolute accuracy in FR1

## 10.1.9C.1.2Relative SS-RSRQ Accuracy in FR1

The relative SS-RSRQ accuracy in inter-frequency case is defined as the RSRQ measured from one cell on a frequency in FR1 compared to the RSRP measured from another cell on a different frequency in FR1.

The accuracy requirements in table 10.1.9C.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for a corresponding Band for each relevant SSB.

-|SSB_RP1dBm - SSB_RP2dBm|  27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.9C.1.2-1: SS-RSRQ Inter-frequency relative accuracy in FR1

## 10.1.9DInter-frequency RSRQ accuracy requirements for RedCap UE with Satellite Access in FR1

## 10.1.9D.1Inter-frequency SS-RSRQ accuracy requirements in FR1

## 10.1.9D.1.1Absolute SS-RSRQ Accuracy in FR1

The requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on a frequency in FR1 that has different carrier frequency from the serving cell.

The accuracy requirements in clause 10.1.9C.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the absolute accuracy requirements in table 10.1.9D.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for both 1Rx and 2Rx RedCap UE for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.9D.1.1-1: SS-RSRQ Inter-frequency absolute accuracy for 1Rx RedCap UE in FR1

## 10.1.9D.1.2Relative SS-RSRQ Accuracy in FR1

The relative SS-RSRQ accuracy in inter-frequency case is defined as the RSRQ measured from one cell on a frequency in FR1 compared to the RSRP measured from another cell on a different frequency in FR1.

The accuracy requirements in clause 10.1.9C.1.2 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the relative accuracy requirements in table 10.1.9D.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for both 1Rx and 2Rx RedCap UE for a corresponding Band for each relevant SSB.

-|SSB_RP1dBm - SSB_RP2dBm|  27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.9D.1.2-1: SS-RSRQ Inter-frequency relative accuracy for 1Rx RedCap UE in FR1

## 10.1.10Inter-frequency RSRQ accuracy requirements for FR2

## 10.1.10.1Inter-frequency SS-RSRQ accuracy requirements in FR2

## 10.1.10.1.1Absolute SS-RSRQ Accuracy in FR2

The requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on a frequency in FR2 that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.10.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.10.1.1-1: SS-RSRQ Inter-frequency absolute accuracy in FR2

## 10.1.10.1.2Relative SS-RSRQ Accuracy in FR2

The relative SS-RSRQ accuracy in inter-frequency case is defined as the RSRQ measured from one cell on a frequency in FR2 compared to the RSRP measured from another cell on a different frequency in FR2.

The accuracy requirements in table 10.1.10.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for each relevant SSB.

-|SSB_RP1 dBm - SSB_RP2 dBm|  27 dB

-| Channel 1_Io Channel 2_Io |  20 dB

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.10.1.2-1: SS-RSRQ Inter-frequency relative accuracy in FR2

## 10.1.10.2Inter-frequency CSI-RSRQ accuracy requirements

## 10.1.10.2.1Absolute CSI-RSRQ Accuracy

Unless otherwise specified, the requirements for absolute CSI-RSRQ accuracy in this clause apply the inter-frequency measurement defined in clause 9.10.3.1 in FR2.

The accuracy requirements in table 10.1.10.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for associated SSB.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.13 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

•The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.10.2.1-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE: The reference measurement timing for one layer for inter-frequency measurement is up to UE implementation and shall be based on the timing of one of the target cells.

Table 10.1.10.2.1-1: CSI-RSRQ Inter-frequency absolute accuracy in FR2

## 10.1.10.2.2Relative CSI-RSRQ Accuracy

The relative CSI-RSRQ accuracy is defined as the CSI-RSRQ measured from one cell compared to the CSI-RSRQ measured from another cell with the same center frequency, or between any two CSI-RSRQ levels measured on the same cell in FR2.

The accuracy requirements in table 10.1.10.2.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band for the associated SSB.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.13 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

•The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.10.2.2-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE: The reference measurement timing for one layer for inter-frequency measurement is up to UE implementation and shall be based on the timing of one of the target cells.

Table 10.1.10.2.2-1: CSI-RSRQ Inter-frequency relative accuracy in FR2

## 10.1.10BInter-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode Measurements

## 10.1.10B.1Inter-frequency SS-RSRQ accuracy requirements in FR2

The requirements in this clause are applicable for a UE:

-in state RRC_IDLE or RRC_INACTIVE

-that is synchronised to the cell that is measured.

The requirements are for absolute SS-RSRQ accuracy.

## 10.1.10B.1.1Absolute SS-RSRQ Accuracy in FR2

The requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on a frequency in FR2 that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.10B.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.1.3 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.10B.1.1-1: SS-RSRQ Inter-frequency absolute accuracy in FR2

## 10.1.10CInter-frequency RSRQ accuracy requirements for FR2-NTN

## 10.1.10C.1Inter-frequency SS-RSRQ accuracy requirements in FR2-NTN

## 10.1.10C.1.1Absolute SS-RSRQ Accuracy in FR2-NTN

The requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on a frequency in FR2-NTN that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.10C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 10.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

Table 10.1.10C.1.1-1: SS-RSRQ Inter-frequency absolute accuracy in FR2-NTN

## 10.1.10C.1.2Relative SS-RSRQ Accuracy in FR2-NTN

The relative SS-RSRQ accuracy in inter-frequency case is defined as the RSRQ measured from one cell on a frequency in FR2-NTN compared to the RSRP measured from another cell on a different frequency in FR2-NTN.

The accuracy requirements in table 10.1.10C.1.2-1 are valid under the following conditions:

-Conditions defined in clause 10.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for a corresponding Band for each relevant SSB.

-|SSB_RP1 dBm - SSB_RP2 dBm|  27 dB

-| Channel 1_Io Channel 2_Io |  20 dB

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

Table 10.1.10C.1.2-1: SS-RSRQ Inter-frequency relative accuracy in FR2-NTN

## 10.1.11RSRQ report mapping

10.1.11.1SS-RSRQ and CSI-RSRQ measurement report mapping

The reporting range of SS-RSRQ and CSI-RSRQ measurement is defined from -43 dB to 20 dB with 0.5 dB resolution. The mapping of measured quantity is defined in table 10.1.11.1-1. The range in the signalling may be larger than the guaranteed accuracy range.

Table 10.1.11.1-1: SS-RSRQ and CSI-RSRQ measurement report mapping

## 10.1.12Intra-frequency SINR accuracy requirements for FR1

## 10.1.12.1Intra-frequency SS-SINR accuracy requirements in FR1

## 10.1.12.1.1Absolute SS-SINR Accuracy in FR1

Unless otherwise specified, the requirements for absolute SS-SINR accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR1.

The accuracy requirements in table 10.1.12.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band.

Table 10.1.12.1.1-1: SS-SINR Intra-frequency absolute accuracy in FR1

## 10.1.12.2Intra-frequency CSI-SINR accuracy requirements in FR1

## 10.1.12.2.1Absolute CSI-SINR Accuracy in FR1

Unless otherwise specified, the requirements for absolute CSI-SINR accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR1.

The accuracy requirements in table 10.1.12.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to Annex B.2.12 for a corresponding Band.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

•NOTE: The reference measurement timing for intra-frequency measurement is serving cell timing.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

•The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.12.2.1-1.

Table 10.1.12.2.1-1: CSI-SINR Intra-frequency absolute accuracy in FR1

## 10.1.12CIntra-frequency SINR accuracy requirements for FR1 SAN

## 10.1.12C.1Intra-frequency SS-SINR accuracy requirements in FR1

## 10.1.12C.1.1Absolute SS-SINR Accuracy in FR1

Unless otherwise specified, the requirements for absolute SS-SINR accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR1.

The accuracy requirements in table 10.1.12C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.17 for a corresponding Band.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.12C.1.1-1: SS-SINR Intra-frequency absolute accuracy in FR1

## 10.1.12DIntra-frequency SINR accuracy requirements for RedCap UE with Satellite Access in FR1

## 10.1.12D.1Intra-frequency SS-SINR accuracy requirements in FR1

## 10.1.12D.1.1Absolute SS-SINR Accuracy in FR1

Unless otherwise specified, the requirements for absolute SS-SINR accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR1.

The accuracy requirements in clause 10.1.12D.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the absolute accuracy requirements in table 10.1.12D.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.17 for both 1Rx and 2Rx RedCap UE for a corresponding Band.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.12D.1.1-1: SS-SINR Intra-frequency absolute accuracy for 1Rx RedCap UE in FR1

## 10.1.13Intra-frequency SINR accuracy requirements for FR2

## 10.1.13.1Intra-frequency SS-SINR accuracy requirements in FR2

## 10.1.13.1.1Absolute SS-SINR Accuracy in FR2

Unless otherwise specified, the requirements for absolute SS-SINR accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR2.

The accuracy requirements in table 10.1.13.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.13.1.1-1: SS-SINR Intra-frequency absolute accuracy in FR2

## 10.1.13.2Intra-frequency CSI-SINR accuracy requirements in FR2

## 10.1.13.2.1Absolute CSI-SINR Accuracy in FR2

Unless otherwise specified, the requirements for absolute CSI-SINR accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR2.

The accuracy requirements in table 10.1.13.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.12 for a corresponding Band.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

•NOTE: The reference measurement timing for intra-frequency measurement is serving cell timing.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

•The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.13.2.1-1.

Table 10.1.13.2.1-1: CSI-SINR Intra-frequency absolute accuracy in FR2

## 10.1.13CIntra-frequency SINR accuracy requirements for FR2-NTN

## 10.1.13C.1Intra-frequency SS-SINR accuracy requirements in FR2-NTN

## 10.1.13C.1.1Absolute SS-SINR Accuracy in FR2-NTN

Unless otherwise specified, the requirements for absolute SS-SINR accuracy in this clause apply to a cell on the same frequency as that of the serving cell in FR2-NTN.

The accuracy requirements in table 10.1.13C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 10.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.17 for a corresponding Band.

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

Table 10.1.13C.1.1-1: SS-SINR Intra-frequency absolute accuracy in FR2-NTN

## 10.1.14Inter-frequency SINR accuracy requirements for FR1

## 10.1.14.1Inter-frequency SS-SINR accuracy requirements in FR1

## 10.1.14.1.1Absolute SS-SINR Accuracy in FR1

The requirements for absolute SS-SINR accuracy in this clause apply to a cell on a frequency in FR1 that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.14.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band.

Table 10.1.14.1.1-1: SS-SINR Inter-frequency absolute accuracy in FR1

## 10.1.14.1.2Relative SS-SINR Accuracy in FR1

The relative SS-SINR accuracy in inter-frequency case is defined as the SS-SINR measured from one cell on a frequency in FR1 compared to the SS-SINR measured from another cell on a different frequency in FR1.

The accuracy requirements in table 10.1.14.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band.

-|SSB_RP1dBm - SSB_RP2dBm|  27 dB

-| Channel 1_Io Channel 2_Io |  20 dB

Table 10.1.14.1.2-1: SS-SINR Inter-frequency relative accuracy in FR1

## 10.1.14.2Inter-frequency CSI-SINR accuracy requirements in FR1

## 10.1.14.2.1Absolute CSI-SINR Accuracy in FR1

The requirements for absolute CSI-SINR accuracy in this clause apply to a cell on a frequency in FR1 that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.14.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.3 for a corresponding Band for the associated SSB.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.13 for a corresponding Band.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

Note: The reference measurement timing for inter-frequency measurement is up to UE implementation and shall be based on the timing of one of the target cells.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in Table 10.1.14.2.1-1.

Table 10.1.14.2.1-1: CSI-SINR Inter-frequency absolute accuracy in FR1

## 10.1.14.2.2Relative CSI-SINR Accuracy in FR1

The relative CSI-SINR accuracy in inter-frequency case is defined as the CSI-SINR measured from one cell on a frequency in FR1 compared to the CSI-SINR measured from another cell on a different frequency in FR1.

The accuracy requirements in table 10.1.14.2.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.3 for a corresponding Band for the associated SSB.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.13 for a corresponding Band.

-|CSI_RP1dBm - CSI_RP2dBm|  27 dB

-| Channel 1_Io Channel 2_Io |  20 dB

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE: The reference measurement timing for inter-frequency measurement is up to UE implementation and shall be based on the timing of one of the target cells.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in Table 10.1.14.2.2-1.

Table 10.1.14.2.2-1: CSI-SINR Inter-frequency relative accuracy in FR1

## 10.1.14CInter-frequency SINR accuracy requirements for FR1 SAN

## 10.1.14C.1Inter-frequency SS-SINR accuracy requirements in FR1

## 10.1.14C.1.1Absolute SS-SINR Accuracy in FR1

The requirements for absolute SS-SINR accuracy in this clause apply to a cell on a frequency in FR1 that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.14C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for a corresponding Band.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.14C.1.1-1: SS-SINR Inter-frequency absolute accuracy in FR1

## 10.1.14C.1.2Relative SS-SINR Accuracy in FR1

The relative SS-SINR accuracy in inter-frequency case is defined as the SS-SINR measured from one cell on a frequency in FR1 compared to the SS-SINR measured from another cell on a different frequency in FR1.

The accuracy requirements in table 10.1.14C.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for a corresponding Band.

-|SSB_RP1dBm - SSB_RP2dBm|  27 dB

-| Channel 1_Io Channel 2_Io |  20 dB

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.14C.1.2-1: SS-SINR Inter-frequency relative accuracy in FR1

## 10.1.14DInter-frequency SINR accuracy requirements for RedCap UE with Satellite Access in FR1

## 10.1.14D.1Inter-frequency SS-SINR accuracy requirements in FR1

## 10.1.14D.1.1Absolute SS-SINR Accuracy in FR1

The requirements for absolute SS-SINR accuracy in this clause apply to a cell on a frequency in FR1 that has different carrier frequency from the serving cell.

The accuracy requirements in clause 10.1.14C.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the absolute accuracy requirements in table 10.1.14D.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for both 1Rx and 2Rx RedCap UE for a corresponding Band.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.14D.1.1-1: SS-SINR Inter-frequency absolute accuracy for 1Rx RedCap UE in FR1

## 10.1.14D.1.2Relative SS-SINR Accuracy in FR1

The relative SS-SINR accuracy in inter-frequency case is defined as the SS-SINR measured from one cell on a frequency in FR1 compared to the SS-SINR measured from another cell on a different frequency in FR1.

The accuracy requirements in clause 10.1.14C.1.2 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the relative accuracy requirements in table 10.1.14D.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for both 1Rx and 2Rx RedCap UE for a corresponding Band.

-|SSB_RP1dBm - SSB_RP2dBm|  27 dB

-| Channel 1_Io Channel 2_Io |  20 dB

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.14D.1.2-1: SS-SINR Inter-frequency relative accuracy for 1Rx RedCap UE in FR1

## 10.1.15Inter-frequency SINR accuracy requirements for FR2

## 10.1.15.1Inter-frequency SS-SINR accuracy requirements in FR2

## 10.1.15.1.1Absolute SS-SINR Accuracy in FR2

The requirements for absolute SS-SINR accuracy in this clause apply to a cell on a frequency in FR2 that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.15.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.15.1.1-1: SS-SINR Inter-frequency absolute accuracy in FR2

## 10.1.15.1.2Relative SS-SINR Accuracy in FR2

The relative SS-SINR accuracy in inter-frequency case is defined as the SS-SINR measured from one cell on a frequency in FR2 compared to the SS-SINR measured from another cell on a different frequency in FR2.

The accuracy requirements in table 10.1.15.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.3 for a corresponding Band.

-|SSB_RP1 dBm - SSB_RP2 dBm|  27 dB

-| Channel 1_Io Channel 2_Io |  20 dB

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.15.1.2-1: SS-SINR Inter-frequency relative accuracy in FR2

## 10.1.15.2Inter-frequency CSI-SINR accuracy requirements in FR2

## 10.1.15.2.1Absolute CSI-SINR Accuracy in FR2

The requirements for absolute CSI-SINR accuracy in this clause apply to a cell on a frequency in FR2 that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.15.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.13 for a corresponding Band.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

•NOTE: The reference measurement timing for inter-frequency measurement is up to UE implementation and shall be based on the timing of one of the target cells.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

•The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.15.2.1-1.

Table 10.1.15.2.1-1: CSI-SINR Inter-frequency absolute accuracy in FR2

## 10.1.15.2.2Relative CSI-SINR Accuracy in FR2

The relative CSI-SINR accuracy in inter-frequency case is defined as the CSI-SINR measured from one cell on a frequency in FR2 compared to the CSI-SINR measured from another cell on a different frequency in FR2.

The accuracy requirements in table 10.1.15.2.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to Annex B.2.13 for a corresponding Band.

-|CSI_RP1 dBm - CSI_RP2 dBm|  27 dB

-| Channel 1_Io Channel 2_Io |  20 dB

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

Note: The reference measurement timing for inter-frequency measurement is up to UE implementation and shall be based on the timing of one of the target cells.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in Table 10.1.15.2.2-1.

Table 10.1.15.2.2-1: CSI-SINR Inter-frequency relative accuracy in FR2

## 10.1.15CInter-frequency SINR accuracy requirements for FR2-NTN

## 10.1.15C.1Inter-frequency SS-SINR accuracy requirements in FR2-NTN

## 10.1.15C.1.1Absolute SS-SINR Accuracy in FR2-NTN

The requirements for absolute SS-SINR accuracy in this clause apply to a cell on a frequency in FR2-NTN that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.15C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 10.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for a corresponding Band.

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

Table 10.1.15C.1.1-1: SS-SINR Inter-frequency absolute accuracy in FR2-NTN

## 10.1.15C.1.2Relative SS-SINR Accuracy in FR2-NTN

The relative SS-SINR accuracy in inter-frequency case is defined as the SS-SINR measured from one cell on a frequency in FR2-NTN compared to the SS-SINR measured from another cell on a different frequency in FR2-NTN.

The accuracy requirements in table 10.1.15C.1.2-1 are valid under the following conditions:

-Conditions defined in clause 10.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.18 for a corresponding Band.

-|SSB_RP1 dBm - SSB_RP2 dBm|  27 dB

-| Channel 1_Io Channel 2_Io |  20 dB

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

Table 10.1.15C.1.2-1: SS-SINR Inter-frequency relative accuracy in FR2-NTN

## 10.1.16SINR report mapping

## 10.1.16.1SS-SINR and CSI-SINR measurement report mapping

The reporting range of SS-SINR and CSI-SINR for L3 reporting and L1 reporing is defined from -23 dB to 40 dB with 0.5 dB resolution. The mapping of measured quantity is defined in table 10.1.16.1-1. The range in the signalling may be larger than the guaranteed accuracy range.

The reporting range of differential SS-SINR and CSI-SINR for L1 reporting is defined from -15 dB to 0 dB with 1 dB resolution.

The mapping of measured quantity is defined in table 10.1.16.1-2. The range in the signalling may be larger than the guaranteed accuracy range.

Table 10.1.16.1-1: SS-SINR and CSI-SINR measurement report mapping

Table 10.1.16.1-2: Differential SS-SINR and CSI-SINR measurement (for L1 reporting) report mapping

## 10.1.17Power Headroom

## 10.1.17.1Power Headroom Report

## 10.1.17.1.1Power Headroom Report Mapping

The power headroom reporting range is from -32 ...+38 dB. table 10.1.17.1-1 defines the report mapping.

Table 10.1.17.1-1: Power headroom report mapping

## 10.1.18PCMAX,c,f

The UE is required to report the UE configured maximum output  power (PCMAX,c,f) together with the power headroom. This clause defines the requirements for the PCMAX,c,f reporting.

## 10.1.18.1Report Mapping

The PCMAX,c,f reporting range is defined from -29 dBm to 33 dBm with 1 dB resolution. table 10.1.18.1-1 defines the reporting mapping.

Table 10.1.18.1-1 Mapping of PCMAX,c.f

## 10.1.19L1-RSRP accuracy requirements for FR1

## 10.1.19.1SSB based L1-RSRP accuracy requirements

Unless otherwise specified, the requirements for absolute and relative SSB based L1-RSRP accuracy in this clause apply to all SSBs of the serving cell configured for L1-RSRP measurement and all SSBs of cell(s) with different PCI from serving cell configured for L1-RSRP measurement in FR1.

## 10.1.19.1.1Absolute Accuracy

The accuracy requirements in table 10.1.19.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

Table 10.1.19.1.1-1: SSB based L1-RSRP absolute accuracy in FR1

## 10.1.19.1.2Relative Accuracy

The relative SSB based L1-RSRP accuracy is defined as the L1-RSRP measured from one SSB compared to the largest measured value of L1-RSRP among all SSBs of the cell (serving cell or cell with different PCI from serving cell) on which UE performs L1-RSRP measurements.

The accuracy requirements in table 10.1.19.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

Table 10.1.19.1.2-1: SSB based L1-RSRP relative accuracy in FR1

## 10.1.19.2CSI-RS based L1-RSRP accuracy requirements

## 10.1.19.2.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute CSI-RS based L1-RSRP accuracy in this clause apply to all CSI-RS resources of the serving cell configured for L1-RSRP measurement.

The accuracy requirements in table 10.1.19.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.19.2.1-1.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled, and

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS, and

-The CSI-RS density is 3.

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.19.2.1-1 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.19.2.1-1 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.19.2.1-1: CSI-RS based L1-RSRP absolute accuracy in FR1

## 10.1.19.2.2Relative Accuracy

The relative CSI-RS based L1-RSRP accuracy is defined as the L1-RSRP measured from one CSI-RS compared to the largest measured value of L1-RSRP among all CSI-RS resources of the serving cell.

The accuracy requirements in table 10.1.19.2.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.19.2.2-1.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled, and

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS, and

-The CSI-RS density is 3.

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.19.2.2-1 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.19.2.2-1 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.19.2.2-1: CSI-RS based L1-RSRP relative accuracy in FR1

## 10.1.19CL1-RSRP accuracy requirements for FR1 SAN

## 10.1.19C.1SSB based L1-RSRP accuracy requirements

## 10.1.19C.1.1Absolute Accuracy

Unless otherwise specified, the accuracy requirements for absolute SSB based L1-RSRP in this clause apply to all SSBs of the serving cell configured for L1-RSRP measurement.

The accuracy requirements in table 10.1.19C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.19.1 for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.19C.1.1-1: SSB based L1-RSRP absolute accuracy in FR1

## 10.1.19C.1.2Relative Accuracy

The relative SSB based L1-RSRP accuracy is defined as the L1-RSRP measured from one SSB compared to the largest measured value of L1-RSRP among all SSBs of the serving cell.

The accuracy requirements in table 10.1.19C.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.19.1 for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.19C.1.2-1: SSB based L1-RSRP relative accuracy in FR1

## 10.1.19C.2CSI-RS based L1-RSRP accuracy requirements

## 10.1.19C.2.1Absolute Accuracy

Unless otherwise specified, the accuracy requirements for absolute CSI-RS based L1-RSRP in this clause apply to all CSI-RS resources of the serving cell configured for L1-RSRP measurement.

The accuracy requirements in table 10.1.19C.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.19.2 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-Valid information for the SAN serving the target cell has been provided.

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.19C.2.1-1.

Table 10.1.19C.2.1-1: CSI-RS based L1-RSRP absolute accuracy in FR1

## 10.1.19C.2.2Relative Accuracy

The relative CSI-RS based L1-RSRP accuracy is defined as the L1-RSRP measured from one CSI-RS compared to the largest measured value of L1-RSRP among all CSI-RS resources of the serving cell.

The accuracy requirements in table 10.1.19C.2.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.19.2 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-Valid information for the SAN serving the target cell has been provided.

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.19C.2.2-1.

Table 10.1.19C.2.2-1: CSI-RS based L1-RSRP relative accuracy in FR1

## 10.1.19DLTM Intra-frequency L1-RSRP accuracy requirements for FR1

## 10.1.19D.1SSB based intra-frequency L1-RSRP accuracy requirements

## 10.1.19D.1.1Absolute Accuracy

Unless otherwise specified, the accuracy requirements for SSB based intra-frequency L1-RSRP in this clause apply to all SSBs of candidate neighbour cell(s) on the same frequency as that of the serving cell in FR1.

The accuracy requirements in table 10.1.19D.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

Table 10.1.19D.1.1-1: SSB based L1-RSRP absolute accuracy in FR1

## 10.1.19D.1.2Relative Accuracy

The relative SSB based L1-RSRP accuracy is defined as the L1-RSRP measured on one SSB configured in LTM-CSI-ResourceConfig compared to the L1-RSRP measured on another  SSB configured in LTM-CSI-ResourceConfig for the cell(s) on the same frequency in FR1.The accuracy requirements in Table 10.1.19D.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

Table 10.1.19D.1.2-1: SSB based L1-RSRP relative accuracy in FR1

## 10.1.19D.2CSI-RS based intra-frequency L1-RSRP accuracy requirements

## 10.1.19D.2.1Absolute CSI-RSRP Accuracy

Unless otherwise specified, the requirements for absolute CSI-RSRP accuracy in this clause apply to a cell where the LTM candidate cell CSI-RS resources to be measured are within the same active BWP as the CSI-RS resources indicated for measurement in the serving cell in FR1.

The accuracy requirements in table 10.1.19D.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for each associated SSB.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.8 for a corresponding Band for each relevant CSI-RS to be measured.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3. The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.19D.2.1-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE:The reference measurement timing for one layer for intra-frequency measurement is serving cell timing.

Table 10.1.19D.2.1-1: CSI-RSRP Intra-frequency absolute accuracy in FR1

## 10.1.19D.2.2Relative CSI-RSRP Accuracy

The relative CSI-RSRP accuracy is defined as the CSI-RSRP measured from one cell compared to the CSI-RSRP measured from another cell within the same active BWP, or between any two CSI-RSRP levels measured on the same cell in FR1.

The accuracy requirements in table 10.1.19D.2.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.2 for a corresponding Band for each associated SSB.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.8 for a corresponding Band for each relevant CSI-RS to be measured.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3. The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.19D.2.2-1.

-The timing offset between the reference measurement timing and the target CSI-RS in one layer is no larger than CP.

NOTE:The reference measurement timing for one layer for intra-frequency measurement is serving cell timing.

Table 10.1.19D.2.2-1: CSI-RSRP Intra-frequency relative accuracy in FR1

## 10.1.19ELTM Inter-frequency L1-RSRP accuracy requirements for FR1

## 10.1.19E.1SSB based Inter-frequency L1-RSRP accuracy requirements

## 10.1.19E.1.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute SSB based L1-RSRP accuracy in this clause apply to all SSBs of candidate neighbour cell(s) on a frequency in FR1 that is on a different frequency than the serving cell.

The accuracy requirements in table 10.1.19E.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

Table 10.1.19E.1.1-1: Inter-frequency L1-RSRP absolute accuracy in FR1

## 10.1.19E.1.2Relative Accuracy

The relative SSB based L1-RSRP accuracy is defined as the L1-RSRP measured on one SSB configured in LTM-CSI-ResourceConfig from one cell on a frequency in FR1 compared to another SSB configured in LTM-CSI-ResourceConfig from any other cell on another frequency in FR1.

The accuracy requirements in table 10.1.19E.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

-|SSB_RP1 dBm - SSB_RP2 dBm| ≤ 27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

Table 10.1.19E.1.2-1: Inter-frequency L1-RSRP relative accuracy in FR1

## 10.1.19FL1-RSRP accuracy requirements for RedCap UE with Satellite Access in FR1

## 10.1.19F.1SSB based L1-RSRP accuracy requirements

## 10.1.19F.1.1Absolute Accuracy

Unless otherwise specified, the accuracy requirements for absolute SSB based L1-RSRP in this clause apply to all SSBs of the serving cell configured for L1-RSRP measurement.

The accuracy requirements in clause 10.1.19C.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the absolute accuracy requirements in table 10.1.19F.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.19.1 for both 1Rx and 2Rx RedCap UE for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.19F.1.1-1: SSB based L1-RSRP absolute accuracy for 1Rx RedCap UE in FR1

## 10.1.19F.1.2Relative Accuracy

The relative SSB based L1-RSRP accuracy is defined as the L1-RSRP measured from one SSB compared to the largest measured value of L1-RSRP among all SSBs of the serving cell.

The accuracy requirements in clause 10.1.19C.1.2 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the relative accuracy requirements in table 10.1.19F.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [43] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.19.1 for both 1Rx and 2Rx RedCap UE for a corresponding Band for each relevant SSB.

-Valid information for the SAN serving the target cell has been provided.

Table 10.1.19F.1.2-1: SSB based L1-RSRP relative accuracy for 1Rx RedCap UE in FR1

## 10.1.19F.2CSI-RS based L1-RSRP accuracy requirements

## 10.1.19F.2.1Absolute Accuracy

Unless otherwise specified, the accuracy requirements for absolute CSI-RS based L1-RSRP in this clause apply to all CSI-RS resources of the serving cell configured for L1-RSRP measurement.

The accuracy requirements in clause 10.1.19C.2.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the absolute accuracy requirements in table 10.1.19F.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.19.2 for both 1Rx and 2Rx RedCap UE for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-Valid information for the SAN serving the target cell has been provided.

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.19C.2.1-1.

Table 10.1.19F.2.1-1: CSI-RS based L1-RSRP absolute accuracy for 1Rx RedCap UE in FR1

## 10.1.19F.2.2Relative Accuracy

The relative CSI-RS based L1-RSRP accuracy is defined as the L1-RSRP measured from one CSI-RS compared to the largest measured value of L1-RSRP among all CSI-RS resources of the serving cell.

The accuracy requirements in clause 10.1.19F.2.2 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1Rx, the relative accuracy requirements in table 10.1.19F.2.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.19.2 for both 1Rx and 2Rx RedCap UE for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-Valid information for the SAN serving the target cell has been provided.

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.19C.2.2-1.

Table 10.1.19F.2.2-1: CSI-RS based L1-RSRP relative accuracy for 1Rx RedCap UE in FR1

## 10.1.20L1-RSRP accuracy requirements for FR2

## 10.1.20.1SSB based L1-RSRP accuracy requirements

Unless otherwise specified, the accuracy requirements for absolute and relative SSB based L1-RSRP in this clause apply to all SSBs of the serving cell configured for L1-RSRP measurement, all the SSBs of the serving cell configured for L1-RSRP measurement when the UE is configured with groupBasedBeamReporting-r17 set to 'enabled' and all SSBs of cell(s) with different PCI from serving cell configured for L1-RSRP measurement in FR2.

## 10.1.20.1.1Absolute Accuracy

The accuracy requirements in table 10.1.20.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.20.1.1-1: SSB based L1-RSRP absolute accuracy in FR2

## 10.1.20.1.2Relative Accuracy

The relative SSB based L1-RSRP accuracy is defined as the L1-RSRP measured from one SSB compared to the largest measured value of L1-RSRP among all SSBs of the cell (serving cell or cell with different PCI from serving cell) on which UE performs L1-RSRP measurements.

When the UE is configured with groupBasedBeamReporting-r17 set to 'enabled', the relative SSB based L1-RSRP accuracy is defined as the L1-RSRP measured from one SSB compared to the largest measured value of L1-RSRP among all SSBs of the serving cell on which UE performs L1-RSRP measurements with different Rx beams, the all SSBs are in the same or different resource set (s) in one CSI resource setting.

The accuracy requirements in table 10.1.20.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.20.1.2-1: SSB based L1-RSRP relative accuracy in FR2

## 10.1.20.2CSI-RS based L1-RSRP accuracy requirements

## 10.1.20.2.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute CSI-RS based L1-RSRP accuracy in this clause apply to all CSI-RS resources of the serving cell configured for L1-RSRP measurement, and all the CSI-RSs of the serving cell configured for L1-RSRP measurement when the UE is configured with groupBasedBeamReporting-r17 set to 'enabled'.

The accuracy requirements in table 10.1.20.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.20.2.1-1.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled, and

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS, and

-The CSI-RS density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.20.2.1-1 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.20.2.1-1 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.20.2.1-1: CSI-RS based L1-RSRP absolute accuracy in FR2

## 10.1.20.2.2Relative Accuracy

The relative CSI-RS based L1-RSRP accuracy is defined as the L1-RSRP measured from one CSI-RS compared to the largest measured value of L1-RSRP among all CSI-RSs of the cell (serving cell or cell with different PCI from serving cell) on which UE performs L1-RSRP measurements.

For simultaneous reception from multiple directions, when the UE is configured with groupBasedBeamReporting-r17 set to 'enabled', the relative CSI-RS based L1-RSRP accuracy is defined as the L1-RSRP measured from one CSI-RS compared to the largest measured value of L1-RSRP among all CSI-RSs of the serving cell on which UE performs L1-RSRP measurements with different Rx beams, the all CSI-RSs are in the same or different resource set (s) in one CSI resource setting. RSRP among all CSI-RS resources of the serving cell.

The accuracy requirements in table 10.1.20.2.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.20.2.2-1.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled, and

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS, and

-The CSI-RS density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.20.2.2-1 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.20.2.2-1 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.20.2.2-1: CSI-RS based L1-RSRP relative accuracy in FR2

## 10.1.20ALTM Intra-frequency L1-RSRP accuracy requirements for FR2

## 10.1.20A.1SSB based intra-frequency L1-RSRP accuracy requirements

## 10.1.20A.1.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute accuracy of SSB based intra-frequency L1-RSRP in this clause apply to all SSBs of candidate neighbour cell(s) on the same frequency as that of the serving cell in FR2.

The accuracy requirements in table 10.1.20A.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.20A.1.1-1: SSB based L1-RSRP absolute accuracy in FR2

## 10.1.20A.1.2Relative Accuracy

The relative SSB based L1-RSRP accuracy is defined as the L1-RSRP measured on one SSB configured in LTM-CSI-ResourceConfig compared to the L1-RSRP measured from another SSB configured in LTM-CSI-ResourceConfig from the cell(s) on the same frequency in FR2.

The accuracy requirements in table 10.1.20A.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.20A.1.2-1: SSB based L1-RSRP relative accuracy in FR2

## 10.1.20A.2CSI-RS based intra-frequency L1-RSRP accuracy requirements

## 10.1.20A.2.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute accuracy of CSI-RS based intra-frequency L1-RSRP in this clause apply to all intra-frequency CSI-RS resources of candidate neighbour cell(s) in FR2 as defined in clause 9.14a.

The accuracy requirements in table 10.1.20A.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.20A.2.1-1.

Table 10.1.20A.2.1-1: CSI-RS based L1-RSRP absolute accuracy in FR2

## 10.1.20A.2.2Relative Accuracy

The relative CSI-RS based L1-RSRP accuracy is defined as the L1-RSRP measured on one CSI-RS configured in LTM-CSI-ResourceConfig compared to the L1-RSRP measured from another intra-frequency CSI-RS configured in LTM-CSI-ResourceConfig from the cell(s) in FR2 as defined in clause 9.14a.

The accuracy requirements in table 10.1.20A.2.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1.20A.2.2-1.

Table 10.1.20A.2.2-1: CSI-RS based L1-RSRP relative accuracy in FR2

## 10.1.20BLTM Inter-frequency L1-RSRP accuracy requirements for FR2

## 10.1.20B.1SSB based inter-frequency L1-RSRP accuracy requirements

## 10.1.20B.1.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute SSB based L1-RSRP accuracy in this clause apply to all SSBs of candidate neighbour cell(s) on a frequency in FR2 that is on a different frequency than the serving cell.

The accuracy requirements in table 10.1.20B.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.20B.1.1-1: SSB based L1-RSRP absolute accuracy in FR2

## 10.1.20B.1.2Relative Accuracy

The relative SSB based L1-RSRP accuracy is defined as the L1-RSRP measured on one SSB configured in LTM-CSI-ResourceConfig on one cell on a frequency in FR2 compared to the value of L1-RSRP measured from another SSB configured in LTM-CSI-ResourceConfig from any other cell on another frequency in FR2.

The accuracy requirements in table 10.1.20B.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

-|SSB_RP1 dBm - SSB_RP2 dBm| ≤ 27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.20B.1.2-1: SSB based L1-RSRP relative accuracy in FR2

## 10.1.20CL1-RSRP accuracy requirements for FR2-NTN

## 10.1.20C.1SSB based L1-RSRP accuracy requirements

Unless otherwise specified, the requirements for absolute accuracy and relative accuracy of SSB based L1-RSRP in this clause apply to all SSBs of the serving cell configured for L1-RSRP measurement in FR2-NTN.

## 10.1.20C.1.1Absolute Accuracy

The accuracy requirements in Table 10.1.20C.1.1-1 are valid under the following conditions:

-Conditions defined in clause 10.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to Annex B.2.19 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

Table 10.1.20C.1.1-1: SSB based L1-RSRP absolute accuracy in FR2-NTN

## 10.1.20C.1.2Relative Accuracy

The relative accuracy of SSB based L1-RSRP is defined as the L1-RSRP measured from one SSB compared to the largest measured value of L1-RSRP among all SSBs of the serving cell on which UE performs L1-RSRP measurements.

The accuracy requirements in Table 10.1.20C.1.2-1 are valid under the following conditions:

-Conditions defined in clause 10.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to Annex B.2.19 for a corresponding Band for each relevant SSB.

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

Table 10.1.20C.1.2-1: SSB based L1-RSRP relative accuracy in FR2-NTN

## 10.1.20C.2CSI-RS based L1-RSRP accuracy requirements

## 10.1.20C.2.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute accuracy of CSI-RS based L1-RSRP in this clause apply to all CSI-RS resources of the serving cell configured for L1-RSRP measurement.

The accuracy requirements in Table 10.1.20C.2.1-1 are valid under the following conditions:

-Conditions defined in clause 10.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to Annex B.2.19 for a corresponding Band for each relevant CSI-RS.

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in Table 10.1.20C.2.1-1.

Table 10.1.20C.2.1-1: CSI-RS based L1-RSRP absolute accuracy in FR2-NTN

## 10.1.20C.2.2Relative Accuracy

The relative accuracy of CSI-RS based L1-RSRP is defined as the L1-RSRP measured from one CSI-RS compared to the largest measured value of L1-RSRP among all CSI-RS resources of the serving cell.

The accuracy requirements in Table 10.1.20C.2.2-1 are valid under the following conditions:

-Conditions defined in clause 10.3 of TS 38.101-5 [42] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to Annex B.2.19 for a corresponding Band for each relevant CSI-RS.

-The measured signals are in the directions within the declared minimum elevation angle supported for receiving.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in Table 10.1.20C.2.2-1.

Table 10.1.20C.2.2-1: CSI-RS based L1-RSRP relative accuracy in FR2-NTN

## 10.1.20D Predicted L1-RSRP accuracy requirements for FR2

## 10.1.20D.1CSI-RS based predicted L1-RSRP accuracy requirements

## 10.1.20D.1.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute accuracy of CSI-RS based predicted L1-RSRP in this clause apply to all the CSI-RS resources of the serving cell reported by the UE configured with reportQuantity-r19 set to ‘'p-cri-RSRP-r19’. The CSI-RS resources for prediction and the number of reported resources among them is indicated to the UE by ‘resourcesForSetA-r19’ and ‘nrofreportedpredictedrs-r19’, respectively, in the CSI-ReportConfig.

Any L1-RSRP measurements used for the verification of the prediction accuracy requirements in Tables 10.1.20D.1.1-2 and 10.1.20D.1.1-3 are valid under the following conditions:

-Conditions for L1-RSRP measurements are fulfilled according to [Annex B.2.4.2] for the actual strongest CSI-RS as the total power received by the UE for a corresponding Band for each relevant CSI-RS.

- Conditions for L1-RSRP measurements are fulfilled according to annex [B.2.4.1] for the actual strongest SSB as the total power received by the UE for a corresponding Band for each relevant SSB.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-Further conditions are captured in Table 10.1.20D.1.1-1.

Table 10.1.20D.1.1-1: Conditions for CSI-RS based predicted L1-RSRP accuracy requirements

Note: The simulation results to derive accuracy requirements of this section were generated based on the parameters of A.x.y.z

The performance with larger bandwidth of CSI-RS for the reported P-L1-RSRP in nrofreportedpredictedrs-r19 is equal to or better than the accuracy requirements in table 10.1.20D.1.1-2, when resourcesForChannelMeasurement are CSI-RS beams. In both Table 10.1.20D.1.1-2 and 10.1.20D.1.1-3, absolute accuracy is defined as the difference between reported P-L1-RSRP of the P-CRI and the ground truth L1-RSRP of the same P-CRI.

Table 10.1.20D.1.1-2: CSI-RS based predicted L1-RSRP absolute accuracy in FR2 when resourcesForChannelMeasurement are CSI-RS beams

The performance with larger bandwidth of CSI-RS for the reported P-L1-RSRP in nrofreportedpredictedrs-r19 is equal to or better than the accuracy requirements in table 10.1.20D.1.1-3, when resourcesForChannelMeasurement are SSB beams.

Table 10.1.20D.1.1-3: CSI-RS based predicted L1-RSRP absolute accuracy in FR2 when resourcesForChannelMeasurement are SSB beams

## 10.1.21SFTD accuracy requirements

## 10.1.21.1SFTD acuracy requirements for NE-DC

The SFN and frame timing difference (SFTD) is measured between PCell and E-UTRAN PSCell under NE-DC.

The accuracy requirements in table 10.1.21.1-4 are appilicable under the following conditions:

For FR1 PCell SFN and frame timing measurement:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Io range defined in Table 10.1.21.1-1.

Table 10.1.21.1-1: PCell Io range conditions in FR1

For FR2 PCell SFN and frame timing measurement:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Io range defined in Table 10.1.21.1-2.

Table 10.1.21.1-2: PCell Io range conditions in FR2

For E-UTRA PSCell SFN and frame timing measurement:

-Cell specific reference signals are transmitted either from one, two or four antenna ports.

-Conditions defined in TS 36.101 [25] clause 7.3 for reference sensitivity are fulfilled.

-No changes to the uplink transmission timing are applied during the measurement period.

-RSRP|dBm according to annex B.3.5 in TS 36.101 [25] for a corresponding Band.

-Io range defined in Table 10.1.21.1-3.

Table 10.1.21.1-3: E-UTRA PSCell Io range conditions

Table 10.1.21.1-4: SFTD measurement accuracy

## 10.1.21.2SFTD acuracy requirements for NR-DC

The SFN and frame timing difference (SFTD) is measured between PCell in FR1 and PSCell in FR2 under NR dual connectivity.

The accuracy requirements in table 10.1.21.2-3 are appilicable under the following conditions:

For FR1 PCell SFN and frame timing measurement:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Io range defined in Table 10.1.21.2-1.

Table 10.1.21.2-1: PCell Io range conditions in FR1

For FR2 PSCell SFN and frame timing measurement:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Io range defined in Table 10.1.21.2-2.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.21.2-2: PSCell Io range conditions in FR2

Table 10.1.21.2-3: SFTD measurement accuracy

## 10.1.21.3Inter-frequency SFTD acuracy requirements

The SFN and frame timing difference (SFTD) is measured between PCell and inter-frequency neighbour cell.

The accuracy requirements in table 10.1.21.3-3 are appilicable under the following conditions:

For FR1 PCell, inter-frequency neighbour cell SFN and frame timing measurement:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Io range defined in Table 10.1.21.3-1.

Table 10.1.21.3-1: PCell, inter-frequency neighbour cell Io range conditions in FR1

For FR2 PCell, inter-frequency neighbour cell SFN and frame timing measurement:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Io range defined in Table 10.1.21.3-2.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

Table 10.1.21.3-2: PCell, inter-frequency neighbour cell Io range conditions in FR2

Table 10.1.21.3-3: Inter-frequency SFTD measurement accuracy

## 10.1.22CLI measurement accuracy requirements

## 10.1.22.1SRS-RSRP

## 10.1.22.1.1SRS-RSRP Accuracy

The SRS-RSRP measurement reported by the UE shall fulfil the accuracy requirements defined in table 10.1.22.1.1-1 for FR1 and table 10.1.22.1.1-2 for FR2, provided that the following conditions are met. The accuracy requirements in this clause are derived based on AWGN radio propagation conditions.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for SRS-RSRP measurements are fulfilled according to annex B.2.7 for a corresponding Band for each relevant SRS resource configured for measurement.

-The time difference between UE’s DL reference timing in the serving cell and SRS arrival time is no larger than Terror_SRS_RSRP, where

-Terror_SRS_RSRP = TC × NTA_offset + 4.67µs for FR1

-Terror_SRS_RSRP = TC × NTA_offset + 3.67µs for FR2

-NTA_offset is defined in table 7.1.2-2

-TC is 0.509 ns

-The number of SRS ports in the SRS resource configured for measurement is 1,

-The number of symbols in the SRS resource configured for measurement is 1,

-The number of repetitions in the SRS resource configured for measurement is 1,

-Frequency hopping, sequence group hopping or sequence hopping is disabled in the SRS resource configured for measurement,

-The bandwidth of the SRS resource is 48 PRBs.

-One of the following conditions is met

-There is no other SRS resource with the same root sequence and on the same symbol and with same comb as the relevant SRS resource.

-If multiple SRS resources are on the same symbol and with same comb, the distance between cyclic shifts of any two resources is no less than 6 if transmissionComb = n4, and no less than 4 if transmissionComb = n2.

Table 10.1.22.1.1-1:  SRS-RSRP absolute accuracy in FR1

Table 10.1.22.1.1-2: SRS-RSRP absolute accuracy in FR2

## 10.1.22.1.2SRS-RSRP report mapping

The reporting range of SRS-RSRP is defined from -140 dBm to -44 dBm with 1 dB resolution. The mapping of measured quantity is defined in table 10.1.22.1.2-1. The range in the signalling may be larger than the guaranteed accuracy range.

Table 10.1.22.1.2-1: SRS-RSRP measurement report mapping

## 10.1.22.2CLI-RSSI

## 10.1.22.2.1CLI-RSSI Accuracy

The CLI-RSSI measurement reported by the UE shall fulfil the accuracy requirements defined in table 10.1.22.2.1-1 for FR1 and table 10.1.22.2.1-2 for FR2, provided that the following conditions are met.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

Table 10.1.22.2.1-1: CLI-RSSI absolute accuracy in FR1

Table 10.1.22.2.1-2: CLI-RSSI absolute accuracy in FR2

## 10.1.22.2.2CLI-RSSI report mapping

The reporting range of CLI-RSSI is defined from -100 dBm to -25 dBm with 1 dB resolution. The mapping of measured quantity is defined in table 10.1.22.2.2-1. The range in the signalling may be larger than the guaranteed accuracy range. UE shall scale the measured CLI-RSSI to report a nominal RSSI equivalent to 6RB measurement with 15 kHz SCS.

Table 10.1.22.2.2-1: CLI-RSSI measurement report mapping

## 10.1.23RSTD Measurements

## 10.1.23.1Introduction

The requirements in clause 10.1.23 shall apply, provided the UE has received nr-DL-TDOA-RequestLocationInformation message from LMF via LPP [34] requesting the UE to report one or more DL RSTD measurements defined in TS 38.215 [4]. The requirements in clause 10.1.23 shall apply:

-when UE is in RRC_CONNECTED state and the measurement is performed with MG or without MG,

-when UE is in RRC_INACTIVE state.

-when UE is in RRC_IDLE state.

## 10.1.23.2Measurement Accuracy Requirements

The accuracy requirements for RSTD measurement shall be within ±(X+Y+Z+Δ) Tc.

X is defined in table 10.1.23.2-1 for AWGN channel and table 10.1.23.2-3 for fading channel for FR1, provided that the following conditions are met.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for RSTD measurements are fulfilled according to annex B.2.14 for a corresponding Band for each relevant PRS resource configured for measurement.

-UE does not perform positioning measurement with reduced number of samples.

X is defined in table 10.1.23.2-2 for AWGN channel and table 10.1.23.2-4 for fading channel for FR2, provided that the following conditions are met.

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for RSTD measurements are fulfilled according to annex B.2.14 for a corresponding Band for each relevant PRS resource configured for measurement.

- UE does not perform positioning measurement with reduced number of samples.

X is defined in table 10.1.23.2-7 for AWGN channel in FR1 provided that the following conditions are met.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for RSTD measurements are fulfilled according to annex B.2.14 for a corresponding Band for each relevant PRS resource configured for measurement.

-UE supports positioning measurement with reduced number of sample and is indicated by LMF to perform positioning measurement with reduced number of samples.

X is defined in table 10.1.23.2-8 for AWGN channel in FR2 provided that the following conditions are met.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for RSTD measurements are fulfilled according to annex B.2.14 for a corresponding Band for each relevant PRS resource configured for measurement.

-UE supports positioning measurement with reduced number of sample and is indicated by LMF to perform positioning measurement with reduced number of samples.

NOTE: The requirements for fading channel in this clause are derived based on TDL-A (30 ns delay spread, 5 Hz) and TDL-C (60 ns delay spread, 300 Hz) channel models for FR1 and FR2 respectively.

When UE measures RSTD on PRS resources belonging to different PFLs, then the RSTD accuracy is defined as the accuracy corresponding to the largest accuracy value among different PFLs.

If the UE doesn’t support Rx TEG reporting for RSTD measurement or when the measurements of reference cell and neighbour cell belong to different Rx TEGs, Y, Z and Δ are defined as follows:

-When UE measures RSTD on PRS resources belonging to same PFL, Y=32 Tc, provided that the time offset between the two PRS resource instances from the reference cell and the neighbor cell, which are used for a single RSTD estimate, is no greater than 160 ms.

-When UE measures RSTD on PRS resources belonging different PFLs, Y=256 Tc, provided that the time offset between the two PRS resource instances from the reference cell and the neighbor cell, which are used for a single RSTD estimate, is no greater than 1280 ms.

-Z is defined in table 10.1.23.2-5 for FR1 and table 10.1.23.2-6 for FR2, respectively.

-Δ is zero for single PFL, and is defined in table 10.1.23.2-5a for FR1 and table 10.1.23.2-6a for FR2, respectively, for dual PFL.

If the measurements of reference cell and neighbour cell belong to the same Rx TEG, i.e. associated and reported with a common Rx TEG ID, then the sum of Y+Z+Δ is equal to the timing error margin of the Rx TEG reported in nr-UE-RxTEG-TimingErrorMargin. The timing error margin reported via nr-UE-RxTEG-TimingErrorMargin cannot be larger than the value of (Y+Z+Δ) defined when the UE does not associate the measurements with the same Rx TEG.

Table 10.1.23.2-1: RSTD absolute accuracy in FR1 for AWGN channel

Table 10.1.23.2-2: RSTD absolute accuracy in FR2 for AWGN channel

Table 10.1.23.2-3: RSTD absolute accuracy in FR1 for fading channel

Table 10.1.23.2-4: RSTD absolute accuracy in FR2 for fading channel

Table 10.1.23.2-5: Margin for RSTD measurement accuracy in FR1

Table 10.1.23.2-5a: Margin Δ for RSTD measurement accuracy in FR1

Table 10.1.23.2-6: Margin for RSTD measurement accuracy in FR2

Table 10.1.23.2-6a: Margin Δ for RSTD measurement accuracy in FR2

Table 10.1.23.2-7: RSTD absolute accuracy in FR1 for AWGN channel with reduced number of samples

Table 10.1.23.2-8: RSTD absolute accuracy in FR2 for AWGN channel with reduced number of samples

## 10.1.23.3Report mapping

## 10.1.23.3.1Absolute DL RSTD Measurement Reporting

The reporting range for the DL RSTD measurement is defined from -985024Tc to 985024Tc with the resolution step of 2kTc, where

Tc is defined in TS 38.211 [6],

kmin≤k≤kmax,

kmin = -6 and kmax = 5,

k≥ timingReportingGranularityFactor [34] configured by LMF via LPP for the RSTD measurement.

The measurement report mapping for different k values are specified in tables 10.1.23.3.1-1  10.1.23.3.1-12.

Table 10.1.23.3.1-1: Report mapping for k=0

Table 10.1.23.3.1-2: Report mapping for k=1

Table 10.1.23.3.1-3: Report mapping for k=2

Table 10.1.23.3.1-4: Report mapping for k=3

Table 10.1.23.3.1-5: Report mapping for k=4

Table 10.1.23.3.1-6: Report mapping for k=5

Table 10.1.23.3.1-7: Report mapping for k=-1

Table 10.1.23.3.1-8: Report mapping for k=-2

Table 10.1.23.3.1-9: Report mapping for k=-3

Table 10.1.23.3.1-10: Report mapping for k=-4

Table 10.1.23.3.1-11: Report mapping for k=-5

Table 10.1.23.3.1-12: Report mapping for k=-6

## 10.1.23.3.2Differential Reporting for DL RSTD Measurement

A first DL RSTD measurement is reported by means of differential reporting, i.e. as RSTD, relative to a second DL RSTD measurement (RSTD2), provided that:

-the absolute measured quantity value of the second DL RSTD measurement (RSTD2) is not larger than the absolute measured quantity value of the first DL RSTD measurement (RSTD1), i.e., RSTD=RSTD1-RSTD2≥0, and

-the absolute value of the second DL RSTD measurement (RSTD2) is reported together with RSTD for the first DL RSTD measurement.

The reporting range for differential reporting RSTD of the first DL RSTD measurement is defined from 0 up to 8191Tc with the resolution step of 2kTc, where

Tc is defined in TS 38.211 [6],

kmin≤k≤kmax,

kmin = -6 and kmax = 5,

k≥ timingReportingGranularityFactor [34] configured by LMF via LPP for the RSTD measurement.

The measurement report mapping for different k values are specified in tables 10.1.23.3.2-1  10.1.23.3.2-12.

Table 10.1.23.3.2-1: Report mapping for k=0

Table 10.1.23.3.2-2: Report mapping for k=1

Table 10.1.23.3.2-3: Report mapping for k=2

Table 10.1.23.3.2-4: Report mapping for k=3

Table 10.1.23.3.2-5: Report mapping for k=4

Table 10.1.23.3.2-6: Report mapping for k=5

Table 10.1.23.3.2-7: Report mapping for k=-1

Table 10.1.23.3.2-8: Report mapping for k=-2

Table 10.1.23.3.2-9: Report mapping for k=-3

Table 10.1.23.3.2-10: Report mapping for k=-4

Table 10.1.23.3.2-11: Report mapping for k=-5

Table 10.1.23.3.2-12: Report mapping for k=-6

## 10.1.23.3.3Additional Path Report Mapping for DL RSTD

The reporting range for the additional path reporting for an RSTD measurement is defined up to the range from -8175Tc to 8175Tc with the resolution step of 2kTc, where

Tc is defined in TS 38.211 [6],

kmin≤k≤kmax,

kmin = -6 and kmax = 5,

k≥ timingReportingGranularityFactor [34] configured by LMF via LPP for the RSTD measurement.

The UE can report the timing of up to two additional paths with respect to the path timing determining the RSTD measurement.

A UE capable of  additionalPathsExtSupport-r17 can report the timing for a number additional paths, up to its capability, with respect to the path timing determining the RSTD measurement.

The report mappings for different k values are specified in tables 10.1.23.3.3-1  10.1.23.3.3-12.

Table 10.1.23.3.3-1: Report mapping for k=0

Table 10.1.23.3.3-2: Report mapping for k=1

Table 10.1.23.3.3-3: Report mapping for k=2

Table 10.1.23.3.3-4: Report mapping for k=3

Table 10.1.23.3.3-5: Report mapping for k=4

Table 10.1.23.3.3-6: Report mapping for k=5

Table 10.1.23.3.3-7: Report mapping for k=-1

Table 10.1.23.3.3-8: Report mapping for k=-2

Table 10.1.23.3.3-9: Report mapping for k=-3

Table 10.1.23.3.3-10: Report mapping for k=-4

Table 10.1.23.3.3-11: Report mapping for k=-5

Table 10.1.23.3.3-12: Report mapping for k=-6

## 10.1.23ARSTD Measurements Based on PRS Aggregation

## 10.1.23A.1Introduction

The requirements in clause 10.1.23A shall apply, provided the UE has received nr-DL-TDOA-RequestLocationInformation message with nr-DL-PRS-JointMeasurementRequestedPFL-List from LMF via LPP TS 37.355 [34] requesting the UE to report one or more DL RSTD measurements defined in TS 38.215 [4] with aggregated measurement. The requirements in clause 10.1.23A shall apply:

-when UE is in RRC_CONNECTED state and the measurement is performed with MG or without MG,

-when UE is in RRC_INACTIVE state,

-when UE is in RRC_IDLE state.

10.1.23A.2Measurement Accuracy Requirements

When UE measures RSTD on PRS resources belonging to different PFLs or different PFL combinations, then the RSTD accuracy is defined as the accuracy corresponding to the largest accuracy value among different PFLs or different PFL combinations.

The requirements in this clause for 3-PFL and 2-PFL apply provided that:

-PRS resources linked for aggregation saftisfy all the conditions specified in TS 38.214 [26] clause 5.1.6.5.3.

-The spacing between the center frequencies of adjacent PFLs containing PRS resources linked for aggregation does not exceed the nominal channel spacing for intra-band contiguous CA defined in TS 38.101-1 [18], clause 5.4A.1 for FR1, and in TS 38.101-2, [19] clause 5.4A.1 for FR2-1.

The accuracy requirements for RSTD measurement based on PRS Aggregation shall be within ±(X+Y+Z+Δ) Tc.

X is defined in table 10.1.23A.2-1 for AWGN channel and table 10.1.23A.2-3 for fading channel for FR1, provided that the following conditions are met:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for RSTD measurements are fulfilled according to annex B.2.14 for a corresponding Band for each relevant PRS resource configured for measurement.

-UE does not perform positioning measurement with reduced number of samples.

X is defined in table 10.1.23A.2-2 for AWGN channel and table 10.1.23A.2-4 for fading channel for FR2, provided that the following conditions are met:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for RSTD measurements are fulfilled according to annex B.2.14 for a corresponding Band for each relevant PRS resource configured for measurement.

- UE does not perform positioning measurement with reduced number of samples.

X is defined in table 10.1.23A.2-5 for AWGN channel in FR1, provided that the following conditions are met:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for RSTD measurements are fulfilled according to annex B.2.14 for a corresponding Band for each relevant PRS resource configured for measurement.

-UE supports positioning measurement with reduced number of sample and is indicated by LMF to perform positioning measurement with reduced number of samples.

X is defined in table 10.1.23A.2-6 for AWGN channel in FR2, provided that the following conditions are met:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for RSTD measurements are fulfilled according to annex B.2.14 for a corresponding Band for each relevant PRS resource configured for measurement.

-UE supports positioning measurement with reduced number of sample and is indicated by LMF to perform positioning measurement with reduced number of samples.

NOTE: The requriements for fading channel in this clause are derived based on TDL-A (30 ns delay spread, 5Hz) and TDL-C (60 ns delay spread, 300 Hz) channel models for FR1 and FR2 respectively.

If the UE doesn’t support Rx TEG reporting for RSTD measurement or when the measurements of reference cell and neighbour cell belong to different Rx TEGs, Y, Z and Δ are defined as follows:

-When UE measures RSTD on PRS resources belonging to same PFL or same PFL combination, Y=32 Tc, provided that the time offset between the two PRS resource instances from the reference cell and the neighbor cell, which are used for a single RSTD estimate, is no greater than 160 ms.

-When UE measures RSTD on PRS resources belonging different PFLs or different PFL combinations, Y=256 Tc, provided that the time offset between the two PRS resource instances from the reference cell and the neighbor cell, which are used for a single RSTD estimate, is no greater than 1280 ms.

-Z is defined in table 10.1.23A.2-7 for FR1 and table 10.1.23A.2-9 for FR2, respectively, where the PRS BW refers to the sum of the PRS PRB numbers across the aggregated PFLs.

-Δ is zero when UE measures RSTD on PRS resources belonging to same PFL or same PFL combination and is defined in table 10.1.23A.2-8 for FR1 and table 10.1.23A.2-10 for FR2, respectively, when UE measures RSTD on PRS resources belonging different PFLs or different PFL combinations, where the PRS BW refers to the sum of the PRS PRB numbers across the aggregated PFLs.

If the measurements of reference cell and neighbour cell belong to the same Rx TEG, i.e. associated and reported with a common Rx TEG ID, then the sum of Y+Z+Δ is equal to the timing error margin of the Rx TEG reported in nr-UE-RxTEG-TimingErrorMargin. The timing error margin reported via nr-UE-RxTEG-TimingErrorMargin cannot be larger than the value of (Y+Z+Δ) defined when the UE does not associate the measurements with the same Rx TEG.

Table 10.1.23A.2-1: RSTD absolute accuracy in FR1 for AWGN channel

Table 10.1.23A.2-2: RSTD absolute accuracy in FR2 for AWGN channel

Table 10.1.23A.2-3: RSTD absolute accuracy in FR1 for fading channel

Table 10.1.23A.2-4: RSTD absolute accuracy in FR2 for fading channel

Table 10.1.23A.2-5: RSTD absolute accuracy in FR1 for AWGN channel with reduced number of samples

Table 10.1.23A.2-6: RSTD absolute accuracy in FR2 for AWGN channel with reduced number of samples

Table 10.1.23A.2-7: Margin for RSTD measurement accuracy in FR1

Table 10.1.23A.2-8: Margin Δ for RSTD measurement accuracy in FR1

Table 10.1.23A.2-9: Margin for RSTD measurement accuracy in FR2

Table 10.1.23A.2-10: Margin Δ for RSTD measurement accuracy in FR2

## 10.1.23A.3Report Mapping

## 10.1.23A.3.1Absolute DL RSTD Measurement Reporting

The report mapping as defined in clause 10.1.23.3.1 shall apply.

## 10.1.23A.3.2Differential Reporting for DL RSTD Measurement

The report mapping as defined in clause 10.1.23.3.2 shall apply.

## 10.1.23A.3.3Additional Path Report Mapping for DL RSTD

The report mapping as defined in clause 10.1.23.3.3 shall apply.

## 10.1.24PRS-RSRP Measurements

## 10.1.24.1Introduction

The requirements in clause 10.1.24 shall apply, provided the UE has received nr-DL-TDOA-RequestLocationInformation or nr-Multi-RTT-RequestLocationInformation or nr-DL-AoD-RequestLocationInformation message from LMF via LPP [34] requesting the UE to report one or more DL PRS-RSRP measurements defined in TS 38.215 [4].

The requirements in clause 10.1.24 apply for UE in RRC_CONNECTED, including PRS-RSRP measurement with MG and outside MG, as well as for UE in RRC_INACTIVE and RRC_IDLE state. For PRS-RSRP measurement in FR2, the requirements apply with and without reduced Rx beam sweeping factor.

## 10.1.24.2Measurement Accuracy Requirements

## 10.1.24.2.1Absolute PRS-RSRP accuracy

The absolute accuracy requirements for PRS-RSRP measurement for FR1 defined in table 10.1.24.2.1-1 are valid under the following conditions:

-Conditions defined in 38.101-1 clause 7.3 for reference sensitivity are fulfilled.

-PRP 1,2|dBm according to annex B.2.14 for a corresponding Band

-UE does not support positioning measurements with reduced number of samples, or LMF does not indicate UE to perform positioning measurements with reduced number of samples

The absolute accuracy requirements for PRS-RSRP measurement for FR2 defined in table 10.1.24.2.1-2 are valid under the following conditions:

-Conditions defined in 38.101-2 [19] clause 7.3 for reference sensitivity are fulfilled.

-PRP 1,2|dBm according to annex B.2.14 for a corresponding Band

-UE does not support positioning measurements with reduced number of samples, or LMF does not indicate UE to perform positioning measurements with reduced number of samples

Table 10.1.24.2.1-1: PRS-RSRP absolute accuracy for FR1

Table 10.1.24.2.1-2: PRS-RSRP absolute accuracy for FR2

The absolute accuracy requirements for PRS-RSRP measurement for FR1 defined in table 10.1.24.2.1-3 are valid under the following conditions:

-Conditions defined in 38.101-1 clause 7.3 for reference sensitivity are fulfilled.

-PRP 1,2|dBm according to annex B.2.14 for a corresponding Band

-UE supports positioning measurements with reduced number of samples, and LMF indicates UE to perform positioning measurements with reduced number of samples

-AWGN channel

The absolute accuracy requirements for PRS-RSRP measurement for FR2 defined in table 10.1.24.2.1-4 are valid under the following conditions:

-Conditions defined in 38.101-2 [19] clause 7.3 for reference sensitivity are fulfilled.

-PRP 1,2|dBm according to annex B.2.14 for a corresponding Band

-UE supports positioning measurements with reduced number of samples, and LMF indicates UE to perform positioning measurements with reduced number of samples

-AWGN channel

Table 10.1.24.2.1-3: PRS-RSRP absolute accuracy for FR1 with reduced sample number

Table 10.1.24.2.1-4: PRS-RSRP absolute accuracy for FR2 with reduced sample number

## 10.1.24.2.2Relative PRS RSRP accuracy

The relative PRS-RSRP accuracy is defined as accuracy of the difference between two PRS-RSRP measurements.

The relative PRS-RSRP accuracy requirements apply for the cases when PRS-RSRP is measured from PRS resources in the same PRS resource set in FR1 or FR2, and measured with same Rx beam in case of FR2.

The accuracy requirements for PRS-RSRP measurement for FR1 defined in table 10.1.24.2.2-1 are valid under the following conditions:

-Conditions defined in 38.101-1 clause 7.3 for reference sensitivity are fulfilled.

-PRP 1,2|dBm according to annex B.2.14 for a corresponding Band

-UE does not support positioning measurements with reduced number of samples, or LMF does not indicate UE to perform positioning measurements with reduced number of samples

The accuracy requirements for PRS-RSRP measurement for FR2 defined in table 10.1.24.2.2-2 are valid under the following conditions:

-Conditions defined in 38.101-2 clause 7.3 for reference sensitivity are fulfilled.

-PRP 1,2|dBm according to annex B.2.14 for a corresponding Band

-UE does not support positioning measurements with reduced number of samples, or LMF does not indicate UE to perform positioning measurements with reduced number of samples

Table 10.1.24.2.2-1: PRS-RSRP relative accuracy for FR1

Table 10.1.24.2.2-2: PRS-RSRP relative accuracy for FR2

The absolute accuracy requirements for PRS-RSRP measurement for FR1 defined in table 10.1.24.2.2-3 are valid under the following conditions:

-Conditions defined in 38.101-1 clause 7.3 for reference sensitivity are fulfilled.

-PRP 1,2|dBm according to annex B.2.14 for a corresponding Band

-UE supports positioning measurements with reduced number of samples, and LMF indicates UE to perform positioning measurements with reduced number of samples

-AWGN channel

The absolute accuracy requirements for PRS-RSRP measurement for FR2 defined in table 10.1.24.2.2-4 are valid under the following conditions:

-Conditions defined in 38.101-2 [19] clause 7.3 for reference sensitivity are fulfilled.

-PRP 1,2|dBm according to annex B.2.14 for a corresponding Band

-UE supports positioning measurements with reduced number of samples, and LMF indicates UE to perform positioning measurements with reduced number of samples

-AWGN channel

Table 10.1.24.2.2-3: PRS-RSRP relative accuracy for FR1 with reduced sample number

Table 10.1.24.2.2-4: PRS-RSRP relative accuracy for FR2 with reduced sample number

## 10.1.24.3Report mapping

## 10.1.24.3.1Absolute PRS-RSRP Measurement Report Mapping

The reporting range of absolute PRS-RSRP measurement is defined from -156 dBm to -31 dBm with 1 dB resolution.

The mapping of measured quantity is defined in table 10.1.24.3.1-1. The range in the signalling may be larger than the guaranteed accuracy range.

Table 10.1.24.3.1-1: Measurement report mapping for PRS-RSRP

## 10.1.24.3.2Differential Report Mapping for PRS-RSRP Measurement

The reporting range of differential PRS-RSRP is defined from -30 dB to 0 dB with 1 dB resolution when nr-DL-AoD-RequestLocationInformation message is received.

The mapping of measured quantity is defined in table 10.1.24.3.2-1. The range in the signalling may be larger than the guaranteed accuracy range.

The reporting range of differential PRS-RSRP is defined from -30 dB to 30 dB with 1 dB resolution when nr-DL-TDOA-RequestLocationInformation or nr-Multi-RTT-RequestLocationInformation is received.

The mapping of measured quantity is defined in Table 10.1.24.3.2-2. The range in the signalling may be larger than the guaranteed accuracy range or the range supported by the UE receiver for differential RSRP measured on different PRS resources in frequency domain at the same time.

Table 10.1.24.3.2-1: Measurement report mapping for differential PRS-RSRP

Table 10.1.24.3.2-2: Measurement report mapping for differential PRS-RSRP

## 10.1.24APRS-RSRP Measurements Based on PRS Aggregation

## 10.1.24A.1Introduction

The requirements in clause 10.1.24A shall apply, provided that the UE has received nr-DL-TDOA-RequestLocationInformation or nr-Multi-RTT-RequestLocationInformation message from LMF via LPP TS 37.355 [34] requesting the UE to report one or more DL PRS-RSRP measurements defined in TS 38.215 [4] performed by aggregating PRS resources from multiple PFLs via nr-DL-PRS-JointMeasurementRequested TS 37.355 [34].

The requirements in clause 10.1.24A shall apply:

-when UE is in RRC_CONNECTED state and the measurement is performed with MG,

-when UE is in RRC_INACTIVE state,

-when UE is in RRC_IDLE state.

## 10.1.24A.2Measurement Accuracy Requirements

## 10.1.24A.2.1Absolute PRS RSRP Accuracy Requirement

The accuracy requirements in clause 10.1.24.2.1 corresponding to the total aggregated PRS bandwidth shall apply.

## 10.1.24A.2.2Relative PRS RSRP Accuracy Requirement

The accuracy requirements in clause 10.1.24.2.2 corresponding to the total aggregated PRS bandwidth shall apply.

## 10.1.24A.3Report Mapping

## 10.1.24A.3.1Absolute PRS-RSRP Measurement Report Mapping

The absolute report mapping for PRS-RSRP measurement in clause 10.1.24.3.1 shall apply.

## 10.1.24A.3.2Differential Report Mapping for PRS-RSRP Measurement

The differential report mapping for PRS-RSRP measurement in clause 10.1.24.3.2 shall apply.

## 10.1.25UE Rx-Tx Time Difference Measurements

## 10.1.25.1Introduction

The requirements in clause 10.1.25 shall apply, provided the UE has received nr-Multi-RTT-RequestLocationInformation message from LMF via LPP [31] requesting the UE to report one or more UE Rx-Tx time difference measurements defined in TS 38.215 [4]. The requirements in clause 10.1.25 shall apply:

-when UE is in RRC_CONNECTED state and the measurement is performed with MG or without MG,

-when UE is in RRC_INACTIVE state.

## 10.1.25.2Measurement Accuracy Requirements

The UE Rx-Tx time difference measurement accuracy requirements in this clause shall not apply, if:

NTA_offset defined in table 7.1.2-2 changes during the UE Rx-Tx measurement period or

if the uplink transmission timing changes during the UE Rx-Tx measurement period due to the network-configured Timing Advance.

The UE Rx-Tx time difference measurement accuracy requirements in this clause shall apply provided that:

-The UE transmits SRS within the range from -160 ms to 160 ms of at least one DL PRS resource of each of the TRPs in the assistance data.

If the uplink transmission timing changes during the UE Rx-Tx measurement period due to the autonomous timing adjustment defined in clause 7.1.2 then:

-UE Rx-Tx measurement accuracy requirements shall apply for a cell, which is also the downlink reference cell (defined in clause 7.1.1) for SRS transmission even if the uplink transmission timing changes during the UE Rx-Tx measurement period due to autonomous adjustment.

-UE Rx-Tx measurement accuracy requirements shall not apply for a cell, which is not the downlink reference cell (defined in clause 7.1.1) for SRS transmission, if the uplink transmission timing changes during the UE Rx-Tx measurement period due to autonomous adjustment.

When a serving cell change occurs during the UE Rx-Tx measurement period, the UE Rx-Tx time difference measurement accuracy requirements in this clause shall apply provided that the serving cell change does not impact SRS configuration for the UE Rx-Tx measurement.

The relative UE Rx-Tx measurement accuracy in this clause is defined as accuracy of the difference between two UE Rx-Tx measurements.

The accuracy requirements in table 10.1.25.2-1 for FR1 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

AWGN propagation condition.

Table 10.1.25.2-1: UE Rx-Tx time difference measurement accuracy in FR1 in AWGN

The accuracy requirements in table 10.1.25.2-1a for FR1 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

Number of measurement samples is less than 4

AWGN propagation condition.

Table 10.1.25.2-1a: UE Rx-Tx time difference measurement accuracy in FR1 in AWGN with reduced measurement samples

The relative accuracy requirements in table 10.1.25.2-1b for FR1 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

AWGN propagation condition.

the two UE Rx-Tx time difference measurements are associated with the same RxTx TEG

Table 10.1.25.2-1b: UE Rx-Tx time difference relative measurement accuracy in FR1 in AWGN with TEG reporting

The accuracy requirements in table 10.1.25.2-2 for FR1 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

Fading propagation condition.

Table 10.1.25.2-2: UE Rx-Tx time difference measurement accuracy in FR1 in fading

The accuracy requirements in table 10.1.25.2-3 for FR2 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

AWGN propagation condition.

Table 10.1.25.2-3: UE Rx-Tx time difference measurement accuracy in FR2 in AWGN

The accuracy requirements in table 10.1.25.2-3a for FR2 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band

Number of measurement samples is less than 4

AWGN propagation condition.

Table 10.1.25.2-3a: UE Rx-Tx time difference measurement accuracy in FR2 in AWGN with reduced measurement samples

The relative accuracy requirements in table 10.1.25.2-3b for FR2 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band

AWGN propagation condition.

the two UE Rx-Tx time difference measurements are associated with the same RxTx TEG

Table 10.1.25.2-3b: UE Rx-Tx time difference relative measurement accuracy in FR2 in AWGN with TEG reporting

The accuracy requirements in table 10.1.25.2-4 for FR2 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

Fading propagation condition.

Table 10.1.25.2-4: UE Rx-Tx time difference measurement accuracy in FR2 in fading

Table 10.1.25.2-5: Margin for UE Rx-Tx time difference measurement accuracy in FR1

Table 10.1.25.2-6: Margin for UE Rx-Tx time difference measurement accuracy in FR2

## 10.1.25.3Report mapping

Absolute UE Rx-Tx measurement reporting in clause 10.1.25.3.1, differential reporting for UE Rx-Tx measurement in clause 10.1.25.3.2, and additional path report mapping for UE Rx-Tx measurement in clause 10.1.25.3.3 applies, regardless of number of samples used to measure PRS, to report:

-TEG based measurement corresponding to UE reported Rx TEG in nr-UE-Rx-TEG-ID-r17 [34],

-gap-based UE Rx-Tx measurement,

-gapless UE Rx-Tx measurement,

-UE Rx-Tx in RRC_INACTIVE state.

## 10.1.25.3.1Absolute UE Rx-Tx Measurement Report Mapping

The reporting range for the absolute UE Rx-Tx time difference measurement (TUE Rx-Tx) is defined from -985024Tc to 985024Tc with the resolution step of 2kTc, where:

Tc is defined in TS 38.211 [6],

kmin≤k≤kmax,

kmin = -6 and kmax = 5,

k≥ timingReportingGranularityFactor TS 34.355 [34] configured by LMF via LPP for the UE Rx-Tx time difference measurement.

The TUE Rx-Tx report mapping for k = {0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6} are specified in tables 10.1.25.3.1-1, 10.1.25.3.1-2, 10.1.25.3.1-3, 10.1.25.3.1-4, 10.1.25.3.1-5, 10.1.25.3.1-6, 10.1.25.3.1-7, 10.1.25.3.1-8, 10.1.25.3.1-9, 10.1.25.3.1-10, 10.1.25.3.1-11, and 10.1.25.3.1-12, respectively.

Table 10.1.25.3.1-1: Absolute UE Rx-Tx time difference measurement report mapping for k=0

Table 10.1.25.3.1-2: Absolute UE Rx-Tx time difference measurement report mapping for k=1

Table 10.1.25.3.1-3: Absolute UE Rx-Tx time difference measurement report mapping for k=2

Table 10.1.25.3.1-4: Absolute UE Rx-Tx time difference measurement report mapping for k=3

Table 10.1.25.3.1-5: Absolute UE Rx-Tx time difference measurement report mapping for k=4

Table 10.1.25.3.1-6: Absolute UE Rx-Tx time difference measurement report mapping for k=5

Table 10.1.25.3.1-7: Absolute UE Rx-Tx time difference measurement report mapping for k=-1

Table 10.1.25.3.1-8: Absolute UE Rx-Tx time difference measurement report mapping for k=-2

Table 10.1.25.3.1-9: Absolute UE Rx-Tx time difference measurement report mapping for k=-3

Table 10.1.25.3.1-10: Absolute UE Rx-Tx time difference measurement report mapping for k=-4

Table 10.1.25.3.1-11: Absolute UE Rx-Tx time difference measurement report mapping for k=-5

Table 10.1.25.3.1-12: Absolute UE Rx-Tx time difference measurement report mapping for k=-6

## 10.1.25.3.2Differential UE Rx-Tx Measurement Report Mapping

The reporting range for differential UE Rx-Tx time difference measurement (TUE Rx-Tx) is defined from 0 up to 8191Tc where:

TUE Rx-Tx = TUE Rx-Tx1 - TUE Rx-Tx2; where:

TUE Rx-Tx1 > TUE Rx-Tx2,

TUE Rx-Tx1 is the first absolute UE Rx-Tx time difference measurement,

TUE Rx-Tx1 is the second absolute UE Rx-Tx time difference measurement,

Tc is defined in TS 38.211 [6],

kmin≤k≤kmax,

kmin = -6 and kmax = 5,

k≥ timingReportingGranularityFactor [34] configured by LMF via LPP for the UE Rx-Tx time difference measurement.

The TUE Rx-Tx report mapping for k = {0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6} are specified in tables 10.1.25.3.2-1, 10.1.25.3.2-2, 10.1.25.3.2-3, 10.1.25.3.2-4, 10.1.25.3.2-5, 10.1.25.3.2-6, 10.1.25.3.2-7, 10.1.25.3.2-8, 10.1.25.3.2-9, 10.1.25.3.2-10, 10.1.25.3.2-11, and 10.1.25.3.2-12, respectively.

Table 10.1.25.3.2-1: Differential UE Rx-Tx time difference measurement report mapping for k=0

Table 10.1.25.3.2-2: Differential UE Rx-Tx time difference measurement report mapping for k=1

Table 10.1.25.3.2-3: Differential UE Rx-Tx time difference measurement report mapping for k=2

Table 10.1.25.3.2-4: Differential UE Rx-Tx time difference measurement report mapping for k=3

Table 10.1.25.3.2-5: Differential UE Rx-Tx time difference measurement report mapping for k=4

Table 10.1.25.3.2-6: Differential UE Rx-Tx time difference measurement report mapping for k=5

Table 10.1.25.3.2-7: Differential UE Rx-Tx time difference measurement report mapping for k=-1

Table 10.1.25.3.2-8: Differential UE Rx-Tx time difference measurement report mapping for k=-2

Table 10.1.25.3.2-9: Differential UE Rx-Tx time difference measurement report mapping for k=-3

Table 10.1.25.3.2-10: Differential UE Rx-Tx time difference measurement report mapping for k=-4

Table 10.1.25.3.2-11: Differential UE Rx-Tx time difference measurement report mapping for k=-5

Table 10.1.25.3.2-12: Differential UE Rx-Tx time difference measurement report mapping for k=-6

## 10.1.25.3.3Additional Path Report Mapping for UE Rx-Tx Time Difference

The reporting range for the additional path reporting for an UE Rx-Tx time difference measurement is defined up to the range from -8175Tc to 8175Tc with the resolution step of 2kTc, where

Tc is defined in TS 38.211 [6],

kmin≤k≤kmax,

kmin = -6 and kmax = 5,

k≥ timingReportingGranularityFactor [34] configured by LMF via LPP for the UE Rx-Tx time difference measurement.

The UE can report the timing of up to two additional paths with respect to the path timing determining the UE Rx-Tx time difference measurement.

The UE capable of  additionalPathsExtSupport-r17 can report the timing of up to its supported number of additional paths with respect to the path timing determining the UE Rx-Tx measurement.

The report mappings for different k values are specified in tables 10.1.25.3.3-1  10.1.25.3.3-12.

Table 10.1.25.3.3-1: Report mapping for k=0

Table 10.1.25.3.3-2: Report mapping for k=1

Table 10.1.25.3.3-3: Report mapping for k=2

Table 10.1.25.3.3-4: Report mapping for k=3

Table 10.1.25.3.3-5: Report mapping for k=4

Table 10.1.25.3.3-6: Report mapping for k=5

Table 10.1.25.3.3-7: Report mapping for k=-1

Table 10.1.25.3.3-8: Report mapping for k=-2

Table 10.1.25.3.3-9: Report mapping for k=-3

Table 10.1.25.3.3-10: Report mapping for k=-4

Table 10.1.25.3.3-11: Report mapping for k=-5

Table 10.1.25.3.3-12: Report mapping for k=-6

## 10.1.25AUE Rx-Tx Time Difference Measurement Based on PRS Aggregation

## 10.1.25A.1Introduction

The requirements in clause 10.1.25A apply provided the UE has received nr-Multi-RTT-RequestLocationInformation message from LMF via LPP TS 37.355 [34] requesting the UE to report one or more UE Rx-Tx time difference measurements, defined in TS 38.215 [4], performed by aggregating PRS resources on multiple PFLs. The requirements in clause 10.1.25A apply:

-when UE is in RRC_CONNECTED state and the measurement is performed with MG,

-when UE is in RRC_INACTIVE state.

## 10.1.25A.2Measurement Accuracy Requirements

The UE Rx-Tx time difference measurement accuracy requirements in this clause shall not apply, if:

NTA_offset defined in table 7.1.2-2 changes during the UE Rx-Tx measurement period or

if the uplink transmission timing changes during the UE Rx-Tx measurement period due to the network-configured Timing Advance.

The UE Rx-Tx time difference measurement accuracy requirements in this clause shall apply provided that:

-The UE transmits SRS within the range from -160 ms to 160 ms of at least one DL PRS resource of each of the TRPs in the assistance data.

-PRS resources linked for aggregation saftisfy all the conditions specified in TS 38.214 [26] clause 5.1.6.5.3.

-the spacing between the center frequencies of adjacent PFLs containing PRS resources linked for aggregation does not exceed the nominal channel spacing for intra-band contiguous CA defined in TS 38.101-1 [18], clause 5.4A.1 for FR1 and in TS 38.101-2 [19], clause 5.4A.1 for FR2-1.

If the uplink transmission timing changes during the UE Rx-Tx measurement period due to the autonomous timing adjustment defined in clause 7.1.2 then:

-UE Rx-Tx measurement accuracy requirements shall apply for a cell, which is also the downlink reference cell (defined in clause 7.1.1) for SRS transmission even if the uplink transmission timing changes during the UE Rx-Tx measurement period due to autonomous adjustment.

-UE Rx-Tx measurement accuracy requirements shall not apply for a cell, which is not the downlink reference cell (defined in clause 7.1.1) for SRS transmission, if the uplink transmission timing changes during the UE Rx-Tx measurement period due to autonomous adjustment.

When a serving cell change occurs during the UE Rx-Tx measurement period, the UE Rx-Tx time difference measurement accuracy requirements in this clause shall apply provided that the serving cell change does not impact SRS configuration for the UE Rx-Tx measurement.

The accuracy requirements in table 10.1.25A.2-1 for FR1 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

AWGN propagation condition.

Table 10.1.25A.2-1: UE Rx-Tx time difference measurement accuracy in FR1 in AWGN

The accuracy requirements in table 10.1.25A.2-1a for FR1 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

Number of measurement samples is less than 4.

AWGN propagation condition.

Table 10.1.25A.2-1a: UE Rx-Tx time difference measurement accuracy in FR1 in AWGN with reduced measurement samples

The accuracy requirements in table 10.1.25A.2-2 for FR1 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

Fading propagation condition.

Table 10.1.25A.2-2: UE Rx-Tx time difference measurement accuracy in FR1 for fading channel

The accuracy requirements in table 10.1.25A.2-3 for FR2 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

AWGN propagation condition.

Table 10.1.25A.2-3: UE Rx-Tx time difference measurement accuracy in FR2 in AWGN

The accuracy requirements in table 10.1.25A.2-3a for FR2 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

Number of measurement samples is less than 4.

AWGN propagation condition.

Table 10.1.25A.2-3a: UE Rx-Tx time difference measurement accuracy in FR2 in AWGN with reduced measurement samples

The accuracy requirements in table 10.1.25A.2-4 for FR2 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

Fading propagation condition.

Table 10.1.25A.2-4: UE Rx-Tx time difference measurement accuracy in FR2 for fading channel

Table 10.1.25A.2-5: Margin for UE Rx-Tx time difference measurement accuracy in FR1

Table 10.1.25A.2-6: Margin for UE Rx-Tx time difference measurement accuracy in FR2

The relative accuracy of UE Rx-Tx measurement in this clause is defined as accuracy of the difference between two UE Rx-Tx measurements.

The relative accuracy requirements in table 10.1.25A.2-7 for FR1 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

AWGN propagation condition.

The two UE Rx-Tx time difference measurements are associated with the same RxTx TEG.

Table 10.1.25A.2-7: UE Rx-Tx time difference relative measurement accuracy in FR1 in AWGN with TEG reporting

The relative accuracy requirements in table 10.1.25A.2-8 for FR2 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

AWGN propagation condition.

the two UE Rx-Tx time difference measurements are associated with the same RxTx TEG.

Table 10.1.25A.2-8: UE Rx-Tx time difference relative measurement accuracy in FR2 in AWGN with TEG reporting

## 10.1.25A.3Report mapping

Applicable measurement report mappings are defined in clause 10.1.25.3.

## 10.1.25CUE Rx-Tx Time Difference Measurements in Satellite Accesss

## 10.1.25C.1Introduction

The requirements in clause 10.1.25C shall apply, provided the UE has received nr-Multi-RTT-RequestLocationInformation message from LMF via LPP [31] requesting the UE to report one or more UE Rx-Tx time difference measurements defined in TS 38.215 [4]. The requirements in clause 10.1.25C shall apply:

-when UE is in RRC_CONNECTED state and the measurement is performed with MG or without MG.

## 10.1.25C.2Measurement Accuracy Requirements

The UE Rx-Tx time difference measurement accuracy requirements in this clause shall not apply, if:

-NTA_offset defined in table 7.1.2-2 changes during the UE Rx-Tx measurement period or

-if the uplink transmission timing changes during the UE Rx-Tx measurement period due to the network-configured Timing Advance.

The UE Rx-Tx time difference measurement accuracy requirements in this clause shall apply provided that:

-The UE transmits SRS within -160, 160 msec of at least one DL PRS resource of each of the TRPs corresponding to the serving cell in the assistance data.

If the uplink transmission timing changes during the UE Rx-Tx measurement period due to the autonomous timing adjustment defined in clause 7.1C.2 then:

-UE Rx-Tx measurement accuracy requirements shall apply for a cell, which is also the downlink reference cell (defined in clause 7.1C.1) for SRS transmission even if the uplink transmission timing changes during the UE Rx-Tx measurement period due to autonomous adjustment.

The accuracy requirements in table 10.1.25C.2-1 for FR1-NTN are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-5 [18] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-AWGN propagation condition.

Table 10.1.25C.2-1: UE Rx-Tx time difference measurement accuracy in FR1 in AWGN with reduced measurement samples

Table 10.1.25C.2-2: Margin for UE Rx-Tx time difference measurement accuracy in FR1-NTN

## 10.1.25C.3Report mapping

The report mapping provided in clause 10.1.25.3 is applicable for NTN.

## 10.1.25DUE Rx-Tx Time Difference Measurements RedCap UE with Satellite Access in FR1

## 10.1.25D.1Introduction

The requirements in clause 10.1.25D shall apply, provided the UE has received nr-Multi-RTT-RequestLocationInformation message from LMF via LPP [31] requesting the UE to report one or more UE Rx-Tx time difference measurements defined in TS 38.215 [4]. The requirements in clause 10.1.25D shall apply:

-when UE is in RRC_CONNECTED state and the measurement is performed with MG or without MG.

## 10.1.25D.2Measurement Accuracy Requirements

## 10.1.25D.2.1UE Rx-Tx Accuracy Requirement for 2Rx RedCap UE without FH

For UE Rx-Tx time difference measurement performed by 2Rx RedCap UE without RX FH, the accuracy requirements corresponding to the PRS bandwidth supported by the RedCap UE for PRS measurement without RX FH in clause 10.1.25C.2 shall apply.

## 10.1.25D.2.2UE Rx-Tx Accuracy Requirement for 1Rx RedCap UE without FH

For UE Rx-Tx time difference measurement performed by 1Rx RedCap UE without Rx FH, the accuracy requirements corresponding to the PRS bandwidth supported by the RedCap UE for PRS measurement without RX FH in clause 10.1.25C.2 shall apply, except those defined in Table 10.1.25D.2.2-1 and Table 10.1.25D.2.2-2.

Table 10.1.25D.2.2-1: UE Rx-Tx time difference measurement accuracy for 1Rx RedCap UE in FR1 in AWGN with reduced measurement samples

Table 10.1.25D.2.2-2: Margin for UE Rx-Tx time difference measurement accuracy in FR1-NTN

## 10.1.25D.3Report mapping

The report mapping provided in clause 10.1.25.3 is applicable for RedCap with NTN.

## 10.1.26FR2 P-MPR report

The FR2 P-MPR report mapping is defined by this clause.

## 10.1.26.1Report mapping

table 10.1.26.1-1 defines the FR2 P-MPR report mapping.

Table 10.1.26.1-1 Mapping of FR2 P-MPR

## 10.1.27L1-SINR accuracy requirements for FR1

## 10.1.27.1L1-SINR accuracy requirements with CSI-RS based CMR and no dedicated IMR configured

## 10.1.27.1.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute CSI-RS based L1-SINR accuracy in this clause apply to all CSI-RS resources configured as CMR and no dedicated resource configured as IMR of the serving cell configured for L1-SINR measurement.

The accuracy requirements in table 10.1.27.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.1 for a corresponding Band for each relevant CSI-RS based CMR.

-The bandwidth of CSI-RS as CMR is 48 PRBs and the density is 3.

-AWGN radio propagation conditions.

The performance with larger bandwidth of CSI-RS as CMR is equal to or better than the accuracy requirements in table 10.1.27.1.1-1.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled, and

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.1 for a corresponding Band for each relevant CSI-RS based CMR, and

-The CSI-RS density is 3.

-AWGN radio propagation conditions.

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.27.2.1-1 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.27.2.1-1 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.27.1.1-1: L1-SINR absolute accuracy for CSI-RS based CMR only in FR1

## 10.1.27.1.2Relative Accuracy

The relative CSI-RS based L1-SINR accuracy is defined as the L1-SINR measured from one CSI-RS compared to the largest measured value of L1-SINR among all CSI-RS resources of the serving cell.

The accuracy requirements in table 10.1.27.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.1 for a corresponding Band for each relevant CSI-RS based CMR.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-AWGN radio propagation conditions.

The performance with larger bandwidth of CSI-RS as CMR is equal to or better than the accuracy requirements in table 10.1.27.1.2-1.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled, and

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.1 for a corresponding Band for each relevant CSI-RS based CMR, and

-The CSI-RS density is 3.

-AWGN radio propagation conditions.

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.27.1.2-1 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.27.1.2-1 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.27.1.2-1: L1-SINR relative accuracy for CSI-RS based CMR only in FR1

## 10.1.27.2L1-SINR accuracy requirements with SSB based CMR and dedicated IMR configured

## 10.1.27.2.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute SSB based L1-SINR accuracy in this clause apply to all SSBs configured as CMR and dedicated resources configured as IMR of the serving cell configured for L1-SINR measurement.

The accuracy requirements are defined in table 10.1.27.2.1-1 for SSB based CMR and NZP-IMR and in table 10.1.27.2.1-2 for SSB based CMR and ZP-IMR.

The accuracy requirements in tables 10.1.27.2.1-1 and 10.1.27.2.1-2 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.2 for a corresponding Band for each relevant SSB based CMR and IMR.

-The bandwidth of NZP-IMR and ZP-IMR is 48 PRBs and the density is 3.

-AWGN radio propagation conditions.

The performance with larger bandwidth of NZP-IMR and ZP-IMR is equal to or better than the accuracy requirements in tables 10.1.27.2.1-1 and 10.1.27.2.1-2.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS as NZP-IMR and ZP-IMR measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled, and

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.2 for a corresponding Band for each relevant SSB based CMR and IMR.

-The CSI-RS density is 3.

-AWGN radio propagation conditions.

If the bandwidth of CSI-RS as NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.27.2.1-1 and 10.1.27.2.1-2 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS as NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.27.2.1-1 and 10.1.27.2.1-2 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.27.2.1-1: L1-SINR absolute accuracy for SSB based CMR and NZP-IMR in FR1

Table 10.1.27.2.1-2: L1-SINR absolute accuracy for SSB based CMR and ZP-IMR in FR1

## 10.1.27.2.2Relative Accuracy

The relative SSB based L1-SINR accuracy is defined as the L1-SINR measured from one SSB configured as CMR and one IMR configured as IMR compared to the largest measured value of L1-SINR among all SSBs and IMRs of the serving cell.

The accuracy requirements are defined in table 10.1.27.2.2-1 for SSB based CMR and NZP-IMR and in table 10.1.27.2.2-2 for SSB based CMR and ZP-IMR.

The accuracy requirements in tables 10.1.27.2.2-1 and 10.1.27.2.2-2 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.2 for a corresponding Band for each relevant SSB based CMR and IMR.

-The bandwidth of NZP-IMR and ZP-IMR is 48 PRBs and the density is 3.

-AWGN radio propagation conditions.

The performance with larger bandwidth of NZP-IMR and ZP-IMR is equal to or better than the accuracy requirements in tables 10.1.27.2.2-1 and 10.1.27.2.2-2.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS as NZP-IMR and ZP-IMR measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled, and

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.2 for a corresponding Band for each relevant SSB based CMR and IMR.

-The CSI-RS density is 3.

-AWGN radio propagation conditions.

If the bandwidth of CSI-RS as NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.27.2.2-1 and 10.1.27.2.2-2 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS as NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.27.2.2-1 and 10.1.27.2.2-2 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.27.2.2-1: L1-SINR relative accuracy for SSB based CMR and NZP-IMR in FR1

Table 10.1.27.2.2-2: L1-SINR relative accuracy for SSB based CMR and ZP-IMR in FR1

## 10.1.27.3L1-SINR accuracy requirements with CSI-RS based CMR and dedicated IMR configured

## 10.1.27.3.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute CSI-RS based L1-SINR accuracy in this clause apply to all CSI-RS resources configured as CMR and dedicated resources configured as IMR of the serving cell configured for L1-SINR measurement.

The accuracy requirements are defined in table 10.1.27.3.1-1 for CSI-RS based CMR and NZP-IMR and in table 10.1.27.3.1-2 for CSI-RS based CMR and ZP-IMR.

The accuracy requirements in tables 10.1.27.3.1-1 and 10.1.27.3.1-2 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.3 for a corresponding Band for each relevant CSI-RS based CMR and IMR.

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is 48 PRBs and the density is 3.

-AWGN radio propagation conditions.

The performance with larger bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is equal to or better than the accuracy requirements in tables 10.1.27.3.1-1 and 10.1.27.3.1-2.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS as CMR, NZP-IMR and ZP-IMR measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled, and

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.3 for a corresponding Band for each relevant CSI-RS based CMR and IMR, and

-The CSI-RS density is 3.

-AWGN radio propagation conditions.

If the bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.27.3.1-1 and 10.1.27.3.1-2 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.27.3.1-1 and 10.1.27.3.1-2 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.27.3.1-1: L1-SINR absolute accuracy for CSI-RS based CMR and NZP-IMR in FR1

Table 10.1.27.3.1-2: L1-SINR absolute accuracy for CSI-RS based CMR and ZP-IMR in FR1

## 10.1.27.3.2Relative Accuracy

The relative CSI-RS based L1-SINR accuracy is defined as the L1-SINR measured from one CSI-RS configured as CMR and one IMR configured as IMR compared to the largest measured value of L1-SINR among all CSI-RS and IMR resources of the serving cell.

The accuracy requirements are defined in table 10.1.27.3.2-1 for CSI-RS based CMR and NZP-IMR and in table 10.1.27.3.2-2 for CSI-RS based CMR and ZP-IMR.

The accuracy requirements in tables 10.1.27.3.2-1 and 10.1.27.3.2-2 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.3 for a corresponding Band for each relevant CSI-RS based CMR and IMR.

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is 48 PRBs and the density is 3.

-AWGN radio propagation conditions.

The performance with larger bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is equal to or better than the accuracy requirements in tables 10.1.27.3.2-1 and 10.1.27.3.2-2.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS as CMR, NZP-IMR and ZP-IMR measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled, and

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.3 for a corresponding Band for each relevant CSI-RS based CMR and IMR, and

-The CSI-RS density is 3.

-AWGN radio propagation conditions.

If the bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.27.3.2-1 and 10.1.27.3.2-2 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.27.3.2-1 and 10.1.27.3.2-2 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.27.3.2-1: L1-SINR relative accuracy for CSI-RS based CMR and NZP-IMR in FR1

Table 10.1.27.3.2-2: L1-SINR relative accuracy for CSI-RS based CMR and ZP-IMR in FR1

## 10.1.28L1-SINR accuracy requirements for FR2

10.1.28.1L1-SINR accuracy requirements with CSI-RS based CMR and no dedicated IMR configured

10.1.28.1.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute CSI-RS based L1-SINR accuracy in this clause apply to all CSI-RS resources configured as CMR and no dedicated resource configured as IMR of the serving cell configured for L1-SINR measurement.

The accuracy requirements in table 10.1.28.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.1 for a corresponding Band for each relevant CSI-RS based CMR.

-The bandwidth of CSI-RS as CMR is 48 PRBs and the density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

-AWGN radio propagation conditions.

The performance with larger bandwidth of CSI-RS as CMR is equal to or better than the accuracy requirements in table 10.1.28.1.1-1.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled, and

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS based CMR, and

-The CSI-RS density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

-AWGN radio propagation conditions.

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.28.1.1-1 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.28.1.1-1 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.28.1.1-1: L1-SINR absolute accuracy for CSI-RS based CMR only in FR2

10.1.28.1.2Relative Accuracy

The relative CSI-RS based L1-SINR accuracy is defined as the L1-SINR measured from one CSI-RS compared to the largest measured value of L1-SINR among all CSI-RS resources of the serving cell.

The accuracy requirements in table 10.1.28.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.1 for a corresponding Band for each relevant CSI-RS based CMR.

-The bandwidth of CSI-RS as CMR is 48 PRBs and the density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

-AWGN radio propagation conditions.

The performance with larger bandwidth of CSI-RS as CMR is equal to or better than the accuracy requirements in table 10.1.28.1.2-1.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled, and

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS based CMR, and

-The CSI-RS density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

-AWGN radio propagation conditions.

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.28.1.2-1 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS meets the following condition the requirements in table 10.1.28.1.2-1 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.28.1.2-1: L1-SINR relative accuracy for CSI-RS based CMR only in FR2

10.1.28.2L1-SINR accuracy requirements with SSB based CMR and dedicated IMR configured

10.1.28.2.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute SSB based L1-SINR accuracy in this clause apply to all SSBs configured as CMR and dedicated resources configured as IMR of the serving cell configured for L1-SINR measurement.

The accuracy requirements are defined in table 10.1.28.2.1-1 for SSB based CMR and NZP-IMR and in table 10.1.28.2.1-2 for SSB based CMR and ZP-IMR.

The accuracy requirements in tables 10.1.28.2.1-1 and 10.1.28.2.1-2 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.2 for a corresponding Band for each relevant SSB based CMR and IMR.

-The bandwidth of NZP-IMR and ZP-IMR is 48 PRBs and the density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

-AWGN radio propagation conditions.

-SSB based CMR and IMR in the test come from the same direction.

The performance with larger bandwidth of NZP-IMR and ZP-IMR is equal to or better than the accuracy requirements in tables 10.1.28.2.1-1 and 10.1.28.2.1-2.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS as NZP-IMR and ZP-IMR measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.2 for a corresponding Band for each relevant SSB based CMR and IMR.

-The CSI-RS density is 3.

-AWGN radio propagation conditions.

If the bandwidth of CSI-RS as NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.28.2.1-1 and 10.1.28.2.1-2 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS as NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.28.2.1-1 and 10.1.28.2.1-2 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.28.2.1-1: L1-SINR absolute accuracy for SSB based CMR and NZP-IMR in FR2

Table 10.1.28.2.1-2: L1-SINR absolute accuracy for SSB based CMR and ZP-IMR in FR2

10.1.28.2.2Relative Accuracy

The relative SSB based L1-SINR accuracy is defined as the L1-SINR measured from one SSB configured as CMR and one IMR configured as IMR compared to the largest measured value of L1-SINR among all SSB based CMRs and IMRs of the serving cell.

The accuracy requirements are defined in table 10.1.28.2.2-1 for SSB based CMR and NZP-IMR and in table 10.1.28.2.2-2 for SSB based CMR and ZP-IMR.

The accuracy requirements in tables 10.1.28.2.2-1 and 10.1.28.2.2-2 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.2 for a corresponding Band for each relevant SSB based CMR and IMR.

-The bandwidth of NZP-IMR and ZP-IMR is 48 PRBs and the density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

-AWGN radio propagation conditions.

-SSB based CMR and IMR in the test come from the same direction.

The performance with larger bandwidth of NZP-IMR and ZP-IMR is equal to or better than the accuracy requirements in tables 10.1.28.2.2-1 and 10.1.28.2.2-2.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS as NZP-IMR and ZP-IMR measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.2 for a corresponding Band for each relevant SSB based CMR and IMR.

-The CSI-RS density is 3.

-AWGN radio propagation conditions.

If the bandwidth of CSI-RS as NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.28.2.2-1 and 10.1.28.2.2-2 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS as NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.28.2.2-1 and 10.1.28.2.2-2 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS as NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.28.2.2-1: L1-SINR relative accuracy for SSB based CMR and NZP-IMR in FR2

Table 10.1.28.2.2-2: L1-SINR relative accuracy for SSB based CMR and ZP-IMR in FR2

10.1.28.3L1-SINR accuracy requirements with CSI-RS based CMR and dedicated IMR configured

10.1.28.3.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute CSI-RS based L1-SINR accuracy in this clause apply to all CSI-RS resources as CMR and dedicated resources configured as IMR of the serving cell configured for L1-SINR measurement.

The accuracy requirements are defined in table 10.1.28.3.1-1 for CSI-RS based CMR and NZP-IMR and in table 10.1.28.3.1-2 for CSI-RS based CMR and ZP-IMR.

The accuracy requirements in tables 10.1.28.3.1-1 and 10.1.28.3.1-2 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.3 for a corresponding Band for each relevant CSI-RS based CMR and IMR.

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is 48 PRBs and the density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

-AWGN radio propagation conditions.

-CSI-RS based CMR and IMR in the test come from the same direction.

The performance with larger bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is equal to or better than the accuracy requirements in tables 10.1.28.3.1-1 and 10.1.28.3.1-2.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS as CMR, NZP-IMR and ZP-IMR measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled, and

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.3 for a corresponding Band for each relevant CSI-RS based CMR and IMR, and

-The CSI-RS density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

-AWGN radio propagation conditions.

-CSI-RS based CMR and IMR in the test come from the same direction

If the bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.28.3.1-1 and 10.1.28.3.1-2 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.28.3.1-1 and 10.1.28.3.1-2 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.28.3.1-1: L1-SINR absolute accuracy for CSI-RS based CMR and NZP-IMR in FR2

Table 10.1.28.3.1-2: L1-SINR absolute accuracy for CSI-RS based CMR and ZP-IMR in FR2

10.1.28.3.2Relative Accuracy

The relative CSI-RS based L1-SINR accuracy is defined as the L1-SINR measured from one CSI-RS configured as CMR and one IMR configured as IMR compared to the largest measured value of L1-SINR among all CSI-RS based CMRs and IMRs of the serving cell.

The accuracy requirements are defined in table 10.1.28.3.2-1 for CSI-RS based CMR and NZP-IMR and in table 10.1.28.3.2-2 for CSI-RS based CMR and ZP-IMR.

The accuracy requirements in tables 10.1.28.3.2-1 and 10.1.28.3.2-2 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.3 for a corresponding Band for each relevant CSI-RS based CMR and IMR.

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is 48 PRBs and the density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

-AWGN radio propagation conditions.

-CSI-RS based CMR and IMR in the test come from the same direction.

The performance with larger bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is equal to or better than the accuracy requirements in tables 10.1.28.3.2-1 and 10.1.28.3.2-2.

If UE supports sbfd-Aware-r19 and SBFD is configured by the network, for CSI-RS as CMR, NZP-IMR and ZP-IMR measurement in SBFD symbols the accuracy requirements apply under the following conditions and depending on the bandwith of CSI-RS.

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled, and

-Conditions for L1-SINR measurements are fulfilled according to annex B.2.8.3 for a corresponding Band for each relevant CSI-RS based CMR and IMR, and

-The CSI-RS density is 3.

-The measured signals are in the directions covered by the percentile EIS spherical coverage of the UE, defined in clause 7.3.4 of TS 38.101-2 [19].

-AWGN radio propagation conditions.

-CSI-RS based CMR and IMR in the test come from the same direction

If the bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.28.3.2-1 and 10.1.28.3.2-2 apply.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured, when one of the following conditions is met

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 48 PRBs in at least one DL subband

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is no less than 72 PRBs across two DL subbands

If the bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR meets the following condition the requirements in table 10.1.28.3.2-1 and 10.1.28.3.2-2 apply with additional 0.5dB margin.

-For the case when one DL subband is configured

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in the DL subband

-For the case when two DL subbands are configured

-The bandwidth of CSI-RS as CMR, NZP-IMR and ZP-IMR is no less than 24 PRBs but less than 48 PRBs in each DL subband, and the total bandwidth of CSI-RS is less than 72 PRBs across two DL subbands

Table 10.1.28.3.2-1: L1-SINR relative accuracy for CSI-RS based CMR and NZP-IMR in FR2

Table 10.1.28.3.2-2: L1-SINR relative accuracy for CSI-RS based CMR and ZP-IMR in FR2

## 10.1.29Intra-frequency RSRQ accuracy requirements under CCA

## 10.1.29.1Intra-frequency SS-RSRQ accuracy requirements in FR1

## 10.1.29.1.1Absolute SS-RSRQ Accuracy

Unless otherwise specified, the requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on the same frequency as that of the serving cell under CCA.

The accuracy requirements in table 10.1.29.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.9 for a corresponding Band for each relevant SSB.

Table 10.1.29.1.1-1: SS-RSRQ intra-frequency absolute accuracy under CCA

## 10.1.30Inter-frequency RSRQ accuracy requirements under CCA

## 10.1.30.1Inter-frequency SS-RSRQ accuracy requirements in FR1

## 10.1.30.1.1Absolute SS-RSRQ Accuracy

The requirements for absolute SS-RSRQ accuracy in this clause apply to a cell on a frequency under CCA that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.30.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.10 for a corresponding Band for each relevant SSB.

Table 10.1.30.1.1-1: SS-RSRQ inter-frequency absolute accuracy under CCA

## 10.1.30.1.2Relative SS-RSRQ Accuracy

The relative SS-RSRQ accuracy in inter-frequency case is defined as the RSRQ measured from one cell on a frequency compared to the RSRP measured from another cell on a different frequency, with at least one of the two frequencies being under CCA.

The accuracy requirements in table 10.1.30.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.10 for a corresponding Band for each relevant SSB.

-|SSB_RP1 dBm - SSB_RP2 dBm| ≤ 27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

Table 10.1.30.1.2-1: SS-RSRQ inter-frequency relative accuracy under CCA

## 10.1.31Intra-frequency SINR accuracy requirements under CCA

## 10.1.31.1Intra-frequency SS-SINR accuracy requirements in FR1

## 10.1.31.1.1Absolute SS-SINR Accuracy

Unless otherwise specified, the requirements for absolute SS-SINR accuracy in this clause apply to a cell on the same frequency as that of the serving cell under CCA.

The accuracy requirements in table 10.1.31.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.9 for a corresponding Band.

Table 10.1.31.1.1-1: SS-SINR intra-frequency absolute accuracy under CCA

## 10.1.32Inter-frequency SINR accuracy requirements under CCA

## 10.1.32.1Inter-frequency SS-SINR accuracy requirements in FR1

## 10.1.32.1.1Absolute SS-SINR Accuracy

The requirements for absolute SS-SINR accuracy in this clause apply to a cell on a frequency under CCA that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.32.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.10 for a corresponding Band.

Table 10.1.32.1.1-1: SS-SINR inter-frequency absolute accuracy under CCA

## 10.1.32.1.2Relative SS-SINR Accuracy

The relative SS-SINR accuracy in inter-frequency case is defined as the SS-SINR measured from one cell on a frequency compared to the SS-SINR measured from another cell on a different frequency, with at least one of the two frequencies being under CCA.

The accuracy requirements in table 10.1.32.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.10 for a corresponding Band.

-SSB_RP1 dBm - SSB_RP2 dBm| ≤ 27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

Table 10.1.32.1.2-1: SS-SINR inter-frequency relative accuracy under CCA

## 10.1.33L1-RSRP accuracy requirements under CCA

## 10.1.33.1SSB based L1-RSRP accuracy requirements in FR1

## 10.1.33.1.1Absolute Accuracy

Unless otherwise specified, the requirements for absolute SSB based L1-RSRP accuracy in this clause apply to all SSBs of the serving cell configured for L1-RSRP measurement under CCA.

The accuracy requirements in table 10.1.33.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.10.1 for a corresponding Band for each relevant SSB.

Table 10.1.33.1.1-1: SSB based L1-RSRP absolute accuracy under CCA

## 10.1.33.1.2Relative Accuracy

The relative SSB based L1-RSRP accuracy is defined as the L1-RSRP measured from one SSB compared to the largest measured value of L1-RSRP among all SSBs of the serving cell under CCA.

The accuracy requirements in table 10.1.33.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.10.1 for a corresponding Band for each relevant SSB.

Table 10.1.33.1.2-1: SSB based L1-RSRP relative accuracy under CCA

## 10.1.34RSSI measurements under CCA

## 10.1.34.1Intra-frequency absolute RSSI measurement accuracy requirements in FR1

The accuracy requirements for intra-frequency RSSI measurements on a carrier frequency under CCA are specified in table 10.1.34.1-1. The requirements apply for any configured RSSI measDuration [2], provided that:

-All symbols during each RSSI measurement duration are available for RSSI sampling within the same reporting interval.

The intra-frequency RSSI measurement bandwidth is the channel bandwidth defined in clause 4 of TS 37.213 [33], where the channel has the center frequency configured by ARFCN-valueNR.

Table 10.1.34.1-1: Intra-frequency RSSI accuracy under CCA

## 10.1.34.2Inter-frequency absolute RSSI measurement accuracy requirements in FR1

The accuracy requirements for inter-frequency RSSI measurements on a carrier frequency under CCA are the same as specified in clause 10.1.34.1.

The inter-frequency RSSI measurement bandwidth is the channel bandwidth defined in clause 4 of TS 37.213 [33], where the channel has the center frequency configured by ARFCN-valueNR.

## 10.1.34.3RSSI measurement report mapping

The reporting range of RSSI measurement is defined from -100 dBm to -25 dBm with 1 dBm resolution.

The mapping of the measured quantity is defined in table 10.1.34.3-1. The range in the signalling may be larger than the guaranteed accuracy range, provided that the following condition is met:

the RSSI measurement bandwidth is the channel bandwidth defined in clause 4 of TS 37.213 [33], where the channel has the center frequency configured by ARFCN-valueNR.

Table 10.1.34.3-1: RSSI measurement report mapping

## 10.1.35Channel occupancy measurements under CCA

## 10.1.35.1Intra-frequency channel occupancy measurement accuracy requirements in FR1

The UE shall be able to correctly evaluate the intra-frequency channel occupancy configured according to TS 38.331 [2], provided that the following conditions are met:

-All symbols during each RSSI measurement duration are available for RSSI sampling within the same reporting interval,

-RSSI at the UE receiver meets the following condition with respect to the configured channelOccupancyThreshold [2]:

-RSSI at the UE receiver is below channelOccupancyThreshold-, or

-RSSI at the UE receiver is above channelOccupancyThreshold+,

-where  is the applicable RSSI measurement accuracy value from the RSSI measurement accuracy requirements specified in clause 10.1.34.1.

The channel occupancy measurement bandwidth is the same as the RSSI measurement bandwidth in clause 10.1.34.1.

## 10.1.35.2Inter-frequency channel occupancy measurement accuracy requirements in FR1

The UE shall be able to correctly evaluate the inter-frequency channel occupancy configured according to TS 38.331 [2], provided that the following conditions are met:

-All symbols during each RSSI measurement duration are available for RSSI sampling within the same reporting interval,

-RSSI at the UE receiver meets the following condition with respect to the configured channelOccupancyThreshold [2]:

-RSSI at the UE receiver is below channelOccupancyThreshold-, or

-RSSI at the UE receiver is above channelOccupancyThreshold+,

-where  is the applicable RSSI measurement accuracy value from the RSSI measurement accuracy requirements specified in clause 10.1.34.2.

The channel occupancy measurement bandwidth is the same as the RSSI measurement bandwidth in clause 10.1.34.2.

## 10.1.36Intra-frequency RSRP accuracy requirements under CCA

## 10.1.36.1Intra-frequency SS-RSRP accuracy requirements in FR1

## 10.1.36.1.1Absolute SS-RSRP Accuracy

Unless otherwise specified, the requirements for absolute SS-RSRP accuracy in this clause apply to a cell on the same frequency as that of the serving cell under CCA.

The accuracy requirements in table 10.1.36.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.8 for a corresponding Band for each relevant SSB.

Table 10.1.36.1.1-1: SS-RSRP intra-frequency absolute accuracy

## 10.1.36.1.2Relative SS-RSRP Accuracy

The relative SS-RSRP accuracy is defined as the SS-RSRP measured from one cell compared to the SS-RSRP measured from another cell on the same frequency, or between any two SS-RSRP levels measured on the same cell under CCA.

The accuracy requirements in table 10.1.36.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.8 for a corresponding Band for each relevant SSB.

Table 10.1.36.1.2-1: SS-RSRP intra-frequency relative accuracy under CCA

## 10.1.37Inter-frequency RSRP accuracy requirements under CCA

## 10.1.37.1Inter-frequency SS-RSRP accuracy requirements in FR1

## 10.1.37.1.1Absolute SS-RSRP

The requirements for absolute SS-RSRP in this clause apply to a cell on a frequency under CCA that has different carrier frequency from the serving cell.

The accuracy requirements in table 10.1.37.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.9 for a corresponding Band for each relevant SSB.

Table 10.1.37.1.1-1: SS-RSRP inter-frequency absolute accuracy under CCA

## 10.1.37.1.2Relative SS-RSRP Accuracy

The relative SS-RSRP accuracy in inter-frequency case is defined as the RSRP measured from one cell on a frequency compared to the RSRP measured from another cell on a different frequency, with at least one of the two frequencies being under CCA.

The accuracy requirements in table 10.1.37.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.9 for a corresponding Band for each relevant SSB.

-|SSB_RP1 dBm - SSB_RP2 dBm| ≤ 27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

Table 10.1.37.1.2-1: SS-RSRP inter-frequency relative accuracy under CCA

## 10.1.38PRS-RSRPP Measurements

## 10.1.38.1Introduction

The requirements in clause 10.1.38.2 shall apply, provided the UE has received nr-DL-AoD-RequestLocationInformation message from LMF via LPP [34] requesting the UE to report one or more DL PRS-RSRPP measurements defined in TS 38.215 [4]. The requirements in clause 10.1.38 shall apply:

-when UE is in RRC_CONNECTED state,

-when UE is in RRC_INACTIVE state,

-when UE is in RRC_IDLE state.

The requirements in clause 10.1.38.2 apply for the first path PRS-RSRP measurement.

## 10.1.38.2Measurement Accuracy Requirements

## 10.1.38.2.1Absolute PRS RSRPP accuracy

The absolute accuracy requirements for PRS-RSRPP measurement for FR1 defined in table 10.1.38.2.1-1 and table 10.1.38.2.1-3 are valid under the following conditions:

-Conditions defined in 38.101-1 clause 7.3 for reference sensitivity are fulfilled.

-PRP 1,2|dBm according to annex B.2.14 for a corresponding Band

The absolute accuracy requirements for PRS-RSRPP measurement for FR2 defined in table 10.1.38.2.1-2 and table 10.1.38.2.1-4 are valid under the following conditions:

-Conditions defined in 38.101-2 [19] clause 7.3 for reference sensitivity are fulfilled.

-PRP 1,2|dBm according to annex B.2.14 for a corresponding Band

The absolute accuracy requirements for PRS-RSRPP measurement defined in table 10.1.38.2.1-1 and table 10.1.38.2.1-2 apply for the UE not supporting supportedDL-PRS-ProcessingSamples [34] or LMF does not indicate UE to perform positioning measurements with reduced number of samples.

The absolute accuracy requirements for PRS-RSRPP measurement defined in table 10.1.38.2.1-3 and table 10.1.38.2.1-4 apply for the UE supporting supportedDL-PRS-ProcessingSamples [34].

NOTE: The requirements in this clause are derived based on two-tap channel defined in TS 38.101-4 [21] annex B.2.4 (a = 1, τd=0.45 µs and fD=5 Hz).

NOTE: The requirements in this clause are derived based on the difference between the estimated PRS-RSRPP compared to the ideal PRS-RSRPP defined as

RSRPPp∝kHkexpj2πDpkNIFFT2

Where:

is the effective channel frequency response (over REs occupied by PRS) measured without receiver noise.Hk

is the exact delay of the p-th path in the channel model.Dp

Table 10.1.38.2.1-1: PRS-RSRPP absolute accuracy for FR1

Table 10.1.38.2.1-2: PRS-RSRPP absolute accuracy for FR2

Table 10.1.38.2.1-3: PRS-RSRPP absolute accuracy for FR1 for reduced number of samples

Table 10.1.38.2.1-4: PRS-RSRPP absolute accuracy for FR2 for reduced number of samples

## 10.1.38.3Report mapping

## 10.1.38.3.1Absolute PRS-RSRPP Measurement Report Mapping

The reporting range of absolute PRS-RSRPP measurement is defined from -156 dBm to -31 dBm with 1 dB resolution.

The mapping of measured quantity is defined in table 10.1.38.3.1-1. The range in the signalling may be larger than the guaranteed accuracy range.

The UE capable of additionalPathsExtSupport-r17 can report the PRS-RSRPP measurement of up to its supported number of additional paths.

Table 10.1.38.3.1-1: Measurement report mapping for PRS-RSRPP

## 10.1.38.3.2Differential Report Mapping for PRS-RSRPP Measurement

The reporting range of differential PRS-RSRPP is defined from -30 dB to 30 dB with 1 dB resolution.

The mapping of measured quantity is defined in table 10.1.38.3.2-1. The range in the signalling may be larger than the guaranteed accuracy range.

For differential reporting, PRS-RSRPP is reported as the difference in dB with respect to the first reported PRS-RSRPP.

Table 10.1.38.3.2-1: Measurement report mapping for differential PRS-RSRPP

## 10.1.38APRS-RSRPP Measurements Based on PRS Aggregation

## 10.1. 38A.1Introduction

The requirements in clause 10.1.38A.2 shall apply, provided the UE has received nr-DL-TDOA-RequestLocationInformation or nr-Multi-RTT-RequestLocationInformation or nr-DL-AoD-RequestLocationInformation message from LMF via LPP TS 37.355 [34] with a request to perform measurement by aggregating PRS resources from multiple PFLs via nr-DL-PRS-JointMeasurementRequested for UE to report one or more DL PRS-RSRPP measurements defined in TS 38.215 [4]. The requirements in clause 10.1.38A.2 shall apply:

-when UE is in RRC_CONNECTED state, and the measurement is performed with MG,

-when UE is in RRC_INACTIVE state.

-when UE is in RRC_IDLE state.

The requirements in clause 10.1.38A.2 apply for the first path PRS-RSRP measurement.

## 10.1.38A.2Measurement Accuracy Requirements

## 10.1.38A.2.1Absolute PRS RSRPP accuracy

The accuracy requirements in clause 10.1.38.2.1 corresponding to the total aggregated PRS bandwidth shall apply.

## 10.1.38A.3Report mapping

## 10.1.38A.3.1Absolute PRS-RSRPP Measurement Report Mapping

The absolute report mapping for PRS-RSRPP measurement in clause 10.1.38.3.1 shall apply.

## 10.1.38A.3.2Differential Report Mapping for PRS-RSRPP Measurement

The differential report mapping for PRS-RSRPP measurement in clause 10.1.38.3.2 shall apply.

## 10.1.39UE Rx-Tx time difference measurements for RTT-based PDC

## 10.1.39.1Void

## 10.1.39.2Measurement Accuracy Requirements for PRS

The error in the reported value of UE Rx-Tx time difference measurement, including both the measurement error and the reporting quantization error, shall be within the accuracy requirements specified in this clause.

The UE Rx-Tx time difference measurement accuracy requirements in this clause shall not apply, if:

-NTA_offset defined in table 7.1.2-2 changes during the UE Rx-Tx measurement period or

-if the uplink transmission timing changes during the UE Rx-Tx measurement period due to the network-configured Timing Advance.

The UE Rx-Tx time difference measurement accuracy requirements in this clause shall apply provided that:

-The UE transmits SRS within -160, 160 msec of at least one PDC DL PRS resource from the serving cell (PCell).

When a serving cell change occurs during the UE Rx-Tx measurement period, the UE Rx-Tx time difference measurement accuracy requirements in this clause shall apply provided that the serving cell change does not impact SRS configuration for the UE Rx-Tx measurement.

The accuracy requirements in table 10.1.39.2-1 for FR1 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

PRP|dBm according to Annex B.2.14 for a corresponding Band.

AWGN propagation condition.

Table 10.1.39.2-1: UE Rx-Tx time difference measurement accuracy in FR1 in AWGN

The accuracy requirements in table 10.1.39.2-2 for FR2 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.14 for a corresponding Band.

AWGN propagation condition.

Table 10.1.39.2-2: UE Rx-Tx time difference measurement accuracy in FR2 in AWGN

Table 10.1.39.2-3: Margin for UE Rx-Tx time difference measurement accuracy in FR1

Table 10.1.39.2-4: Margin for UE Rx-Tx time difference measurement accuracy in FR2

## 10.1.39.3Measurement Accuracy Requirements for TRS

The error in the reported value of UE Rx-Tx time difference measurement, including both the measurement error and the reporting quantization error, shall be within the accuracy requirements specified in this clause.

The UE Rx-Tx time difference measurement accuracy requirements in this clause shall not apply, if:

-NTA_offset defined in table 7.1.2-2 changes during the UE Rx-Tx measurement period or

-if the uplink transmission timing changes during the UE Rx-Tx measurement period due to the network-configured Timing Advance.

The UE Rx-Tx time difference measurement accuracy requirements in this clause shall apply provided that:

-The UE transmits SRS within -160, 160 msec of at least one PDC TRS resource from the serving cell (PCell).

When a serving cell change occurs during the UE Rx-Tx measurement period, the UE Rx-Tx time difference measurement accuracy requirements in this clause shall apply provided that the serving cell change does not impact SRS configuration for the UE Rx-Tx measurement.

The accuracy requirements in table 10.1.39.3-1 for FR1 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.13 for a corresponding Band.

AWGN propagation condition.

Table 10.1.39.3-1: UE Rx-Tx time difference measurement accuracy in FR1 in AWGN

The accuracy requirements in table 10.1.39.3-2 for FR2 are valid under the following conditions:

Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

PRP|dBm according to annex B.2.13 for a corresponding Band.

AWGN propagation condition.

Table 10.1.39.3-2: UE Rx-Tx time difference measurement accuracy in FR2 in AWGN

Table 10.1.39.3-3: Margin for UE Rx-Tx time difference measurement accuracy in FR1

Table 10.1.39.3-4: Margin for UE Rx-Tx time difference measurement accuracy in FR2

## 10.1.40Void

## 10.1.41FR1 DPC report

The FR1 DPC report mapping is defined in this clause.

## 10.1.41.1Report mapping

table 10.1.41.1-1 defines the FR1 DPC report mapping.

Table 10.1.41.1-1 Mapping of FR1 DPC

## 10.1.42TDCP Measurement Report Mapping

The reporting range of TDCP amplitude is defined from 0 to 1. The reporting range of TDCP phase is 0 to 2p. The mapping of measured quantity is defined in tables 10.1.42-1, 10.1.42-2. The range in the signalling may be larger than the guaranteed accuracy range.

Table 10.1.42-1: TDCP amplitude measurement report mapping

Table 10.1.42-2: TDCP phase measurement report mapping

## 10.1.43DL-RSCPD Measurements

## 10.1.43.1Introduction

The requirements in clause 10.1.43 shall apply, provided the UE has received NR-DL-TDOA-RequestLocationInformation message with dl-PRS-RSCPD-Request-r18 from LMF via LPP TS 37.355 [34] requesting the UE to measure and report DL RSCPD measurement together with DL RSTD measurements defined in TS 38.215 [4]. The requirements in clause 10.1.43 shall apply:

-when UE is in RRC_CONNECTED state and the measurement is performed with MG,

-when UE is in RRC_IDLE or RRC_INACTIVE state.

## Measurement Accuracy Requirements

The accuracy requirements for DL RSCPD measurement are based on single measurement sample in single PFL and shall be within ±(X+Y) degree, provided that the following conditions are met:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled for FR1.

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled for FR2.

-Conditions for DL RSCPD measurements are fulfilled according to annex B.2.14 for a corresponding Band for each relevant PRS resource configured for measurement.

-The measurements to derive DL RSCPD are performed on PRS resources within same set of symbols.

-DL RSCPD measurements are based on PRS resources with comb size other than 12.

The requirements in this clause are derived based on AWGN channel and on two-tap channel defined in 38.101-4 [21] annex B.2.4 (a = 1, τd=0.45 µs and fD=5 Hz).

X is defined in table 10.1.43.2-1 for AWGN channel and table 10.1.43.2-2 for two-tap channel for FR1 and is derived assuming no carrier frequency offset at TRP.

X is defined in table 10.1.43.2-3 for AWGN channel and table 10.1.43.2-4 for two-tap channel for FR2 and is derived assuming no carrier frequency offset at TRP.

Y is 14 degrees for FR1 and 28 degrees for FR2.

Table 10.1.43.2-1: DL RSCPD absolute accuracy in FR1 for AWGN channel

Table 10.1.43.2-2: DL RSCPD absolute accuracy in FR1 for two-tap channel

Table 10.1.43.2-3: DL RSCPD absolute accuracy in FR2 for AWGN channel

Table 10.1.43.2-4: DL RSCPD absolute accuracy in FR2 for two-tap channel

## 10.1.43.3Report Mapping

## 10.1.43.3.1Absolute DL RSCPD Measurement Reporting

The reporting range of DL RSCPD, as defined in clause 5.1.43 of TS 38.215 [4], is defined from -180 degree to +180 degree. The reporting resolution is 0.1 degree.

The mapping of DL RSCPD measured quantity is defined in table 10.1.43.3.1-1.

Table 10.1.43.3.1-1: DL RSCPD measurement report mapping

## 10.1.44DL-RSCP Measurements

## 10.1.44.1Introduction

The requirements in clause 10.1.44 shall apply, provided the UE has received NR-Multi-RTT-RequestLocationInformation message with dl-PRS-RSCP-Request-r18 from LMF via LPP TS 37.355 [34] requesting the UE to measure and report DL RSCP measurement together with UE Rx-Tx time difference measurements defined in TS 38.215 [4].

The requirements in clause 10.1.44 shall apply:

-when UE is in RRC_CONNECTED state and the measurement is performed with MG,

-when UE is in RRC_INACTIVE state.

## 10.1.44.2Measurement Accuracy Requirements

The relative accuracy of DL RSCP measurement in this clause is defined as accuracy of the difference between two DL RSCP measurements, each based on single measurement sample in single PFL.

The requirements in this clause are derived based on AWGN channel and based on two-tap channel defined in 38.101-4 [21] annex B.2.4 (a = 1, τd=0.45 µs and fD=5 Hz).

The DL RSCP relative measurement accuracy requirements in this clause shall not apply, if:

-NTA_offset defined in table 7.1.2-2 changes during the DL RSCP with UE Rx-Tx measurement period, or

-if the uplink transmission timing changes during the DL RSCP with UE Rx-Tx measurement period due to the network-configured Timing Advance.

The DL RSCP relative measurement accuracy requirements in this clause shall apply provided that:

-The UE transmits SRS within the range from -160 ms to 160 ms of at least one DL PRS resource of each of the TRPs in the assistance data.

If the uplink transmission timing changes during the DL RSCP with UE Rx-Tx measurement period due to the autonomous timing adjustment defined in clause 7.1.2 then:

-DL RSCP and UE Rx-Tx measurement accuracy requirements shall apply for a cell, which is also the downlink reference cell (defined in section 7.1.1) for SRS transmission.

-UE Rx-Tx measurement accuracy requirements shall not apply for a cell, which is not the downlink reference cell (defined in section 7.1.1) for SRS transmission.

When a serving cell change occurs during the DL RSCP with UE Rx-Tx measurement period, UE Rx-Tx measurement accuracy requirements and DL RSCP measurement requirements do not apply.

The relative DL RSCP accuracy requirements defined in clause 10.1.44 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled for FR1.

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled for FR2.

-Conditions for DL RSCP measurements are fulfilled according to annex B.2.14 for a corresponding Band for each relevant PRS resource configured for measurement.

-DL RSCP measurements to derive the relative accuracy are performed on PRS resources within the same set of symbols.

-DL RSCPD measurements are based on PRS resources with comb size other than 12.

The accuracy requirement for relative DL-RSCP shall be within ±(X+Y) degree.

The values of X for accuracy requirements for relative DL-RSCP measurement in FR1 are defined in table 10.1.44.2-1 for AWGN channel and in table 10.1.44.2-2 for two-tap channel and is derived assuming no carrier frequency offset at TRP.

The values of X for accuracy requirements for relative DL-RSCP measurement in FR2 are defined in table 10.1.44.2-3 for AWGN channel and in table 10.1.44.2-4 for two-tap channel and is derived assuming no carrier frequency offset at TRP.

Y is 14 degrees for FR1 and 28 degrees for FR2.

Table 10.1.44.2-1: DL RSCP relative accuracy in FR1 for AWGN channel

Table 10.1.44.2-2: DL RSCP relative accuracy in FR1 for two-tap channel

Table 10.1.44.2-3: DL RSCP relative accuracy in FR2 for AWGN channel

Table 10.1.44.2-4: DL RSCP relative accuracy in FR2 for two-tap channel.

## 10.1.44.3Report Mapping

Relative DL RSCP measurement reporting in clause 10.1.44.3.1 applies to report:

-gap-based DL RSCP measurement, and

-DL RSCP in RRC_INACTIVE state.

## 10.1.44.3.1Relative DL RSCP Measurement Reporting

The reporting range of relative DL RSCP, as defined in clause 5.1.42 of TS 38.215 [4], is defined from 0 degree to 360 degree. The reporting resolution is 0.1 degree.

The mapping of DL RSCP measured quantity is defined in table 10.1.44.3.1-1.

Table 10.1.44.3.1-1: DL RSCP measurement report mapping

## 10.1.45CJT calibration measurements

## 10.1.45.1Introduction

The accuracy requirements in table 10.1.45.2-1, 10.1.45.2-2, 10.1.45.3-1, 10.1.45.3-2 and 10.1.45.3-3 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to Annex B.2.12 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

## 10.1.45.2CJTC calibration delay offset report

Table 10.1.45.2-1: CJTC calibration delay offset report absolute accuracy in FR1 for UE supporting cjtc-DdReport-r19 and not supporting cjtc-DdReportHighAccuracy-r19

Table 10.1.45.2-2: CJTC calibration delay offset report absolute accuracy in FR1 for UE supporting cjtc-DdReport-r19 and cjtc-DdReportHighAccuracy-r19

## 10.1.45.3CJTC calibration frequency offset report

Table 10.1.45.3-1: CJTC calibration frequency offset report absolute accuracy in FR1 for UE supporting cjtc-FO-Report-r19 and not supporting cjtc-DdReportHighAccuracy-r19

Table 10.1.45.3-2: CJTC calibration frequency offset report absolute accuracy in FR1 for UE supporting cjtc-FO-Report-r19 and cjtc-FO-ReportHighAccuracy-r19 high accuracy reporting level 1

Table 10.1.45.3-3: CJTC calibration frequency offset report absolute accuracy in FR1 for UE supporting cjtc-FO-Report-r19 and cjtc-FO-ReportHighAccuracy-r19 high accuracy reporting level 2

## 10.1.46CJT Calibration Report Mapping

## 10.1.46.1CJT Calibration Delay Offset Measurement Report Mapping

The reporting range of delay offset is defined from 0 to AD, where . The number of levels is defined by MD, where . The mapping of measured quantity is defined in tables 10.1.y.1-1. The range in the signaling may be larger than the guaranteed accuracy range.AD∈0.5CP,CPMD∈{32, 64, 128, 256}

Table 10.1.46.1-1: Mapping of cjtc-Dd

## 10.1.46.2CJT Calibration Frequency Offset Measurement Report Mapping

The reporting range of frequency offset is defined from 0 to AFO, where . The number of levels is defined by MFO, where . The mapping of measured quantity is defined in tables 10.1.46.2-1. The range in the signaling may be larger than the guaranteed accuracy range.10.1.46AFO∈0.1ppm,0.2ppmMFO∈{16, 32, 256}

Table 10.1.46.2-1: Mapping of cjtc-F

## 10.1.46.3CJT Calibration Phase Offset Measurement Report Mapping

The reporting range of phase offset is defined from 0 to 2p. The number of levels is defined by MF, where . The mapping of measured quantity is defined in tables 10.1.46.3-1. The range in the signaling may be larger than the guaranteed accuracy range.MΦ∈{16, 32}

Table 10.1.46.3-1: Mapping of cjtc-P

## 10.1.47L1 CLI measurement accuracy requirements

## 10.1.47.1L1-SRS-RSRP

## 10.1.47.1.1L1-SRS-RSRP Accuracy

The L1-SRS-RSRP measurement reported by the UE shall fulfil the accuracy requirements defined in table 10.1.47.1.1-1 for FR1 and table 10.1.47.1.1-2 for FR2-1, provided that the following conditions are met. The accuracy requirements in this clause are derived based on AWGN radio propagation conditions.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-SRS-RSRP measurements are fulfilled according to annex B.2.7 for a corresponding Band for each relevant SRS resource configured for measurement.

-The time difference between UE’s DL reference timing in the serving cell and SRS arrival time is no larger than Terror_SRS_RSRP, where

-Terror_SRS_RSRP = TC × NTA_offset + 4.67µs for 15 kHz SCS and 30 kHz SCS for FR1

-Terror_SRS_RSRP = TC × NTA_offset + 1.67 µs for 60 kHz SCS for FR1.

-Terror_SRS_RSRP = TC × NTA_offset + 0.67µs for FR2

-NTA_offset is defined in table 7.1.2-2

-TC is 0.509 ns

-The number of SRS ports in the SRS resource configured for measurement is 1,

-The number of symbols in the SRS resource configured for measurement is 1,

-The number of repetitions in the SRS resource configured for measurement is 1,

-Frequency hopping, sequence group hopping or sequence hopping is disabled in the SRS resource configured for measurement,

-The bandwidth of the SRS resource is 24 PRBs.

-One of the following conditions is met

-There is no other SRS resource with the same root sequence and on the same symbol and with same comb as the relevant SRS resource.

-If multiple SRS resources are on the same symbol and with same comb, the distance between cyclic shifts of any two resources is no less than 6 if transmissionComb = n4, and no less than 4 if transmissionComb = n2.

Table 10.1.47.1.1-1: L1-SRS-RSRP absolute accuracy in FR1

Table 10.1.47.1.1-2: L1-SRS-RSRP absolute accuracy in FR2

## 10.1.47.1.2L1-SRS-RSRP report mapping

The reporting range of L1-SRS-RSRP is defined from -140 dBm to -44 dBm with 1 dB resolution. The mapping of measured quantity is defined in table 10.1.47.1.2-1. The range in the signalling may be larger than the guaranteed accuracy range.

The reporting range of differential SRS-RSRP for L1 reporting is defined from 0 dB to -30 dB with 2 dB resolution. The mapping of measured quantity is defined in table 10.1.47.1.2-2. The range in the signalling may be larger than the guaranteed accuracy range.

Table 10.1.47.1.2-1: L1-SRS-RSRP measurement report mapping

Table 10.1.47.1.2-2: Differential SRS-RSRP measurement (for L1 reporting) report mapping

## 10.1.47.2L1-CLI-RSSI

## 10.1.47.2.1L1-CLI-RSSI Accuracy

The L1-CLI-RSSI measurement reported by the UE shall fulfil the accuracy requirements defined in table 10.1.47.2.1-1 for FR1 and table 10.1.47.2.1-2 for FR2, provided that the following conditions are met.

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

Table 10.1.47.2.1-1: L1-CLI-RSSI absolute accuracy in FR1

Table 10.1.47.2.1-2: L1-CLI-RSSI absolute accuracy in FR2

## 10.1.47.2.2L1-CLI-RSSI report mapping

The reporting range of L1-CLI-RSSI is defined from -100 dBm to -25 dBm with 1 dB resolution. The mapping of measured quantity is defined in table 10.1.47.2.2-1. The range in the signalling may be larger than the guaranteed accuracy range. UE shall scale the measured L1-CLI-RSSI to report a nominal RSSI equivalent to 6RB measurement with 15 kHz SCS.

The reporting range of differential L1-CLI-RSSI reporting is defined from 0 dB to -30 dB with 2 dB resolution. The mapping of measured quantity is defined in table 10.1.47.2.2-2. The range in the signalling may be larger than the guaranteed accuracy range.

Table 10.1.47.2.2-1: L1-CLI-RSSI measurement report mapping

Table 10.1.47.2.2-2: Differential CLI-RSSI measurement (for L1 reporting) report mapping

## 10.1.48 RS resource prediction accuracy requirements for FR2

## 10.1.48.1 CSI-RS based RS resource prediction accuracy requirements

Unless otherwise specified, the accuracy requirements for prediction accuracy of CSI-RS based RS resources in this clause apply to the case when only one CSI-RS based RS resource of the serving cell is configured to be predicted for CSI-RS based RS resource prediction in FR2 when the UE is configured with reportQuantity-r19 set to 'p-cri-r19'.

The accuracy requirements in Tables 10.1.48.1-2 and 10.1.48.1-3 are valid under the following conditions:

-Conditions for L1-RSRP measurements are fulfilled according to annex [B.2.4.2] for the actual strongest CSI-RS as the total power received by the UE for a corresponding Band for each relevant CSI-RS.

- Conditions for L1-RSRP measurements are fulfilled according to annex [B.2.4.1] for the actual strongest SSB as the total power received by the UE for a corresponding Band for each relevant SSB.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

-Further conditions are captured in Table 10.1.48.1-1.

Table 10.1.48.1-1: Conditions for CSI-RS based RS resource prediction accuracy requirements

Note: The simulation results to derive accuracy requirements of this section were generated based on the parameters of A.x.y.z

The performance with larger bandwidth of CSI-RS for the first reported P-CRI in nrofreportedpredictedrs-r19 is equal to or better than the accuracy requirements in table 10.1.48.1-2, when resourcesForChannelMeasurement are CSI-RS beams. The correct prediction is considered as the ground-truth L1-RSRP of the first reported P-CRI being larger than or equal to the ground-truth RSRP of the strongest beam in resourcesForSetA-r19 minus the tolerance margin.

Table 10.1.48.1-2: CSI-RS based RS resource prediction accuracy requirements in FR2 when resourcesForChannelMeasurement are CSI-RS beams

The performance with larger bandwidth of CSI-RS for the first reported P-CRI in nrofreportedpredictedrs-r19 is equal to or better than the accuracy requirements in table 10.1.48.1-3, when resourcesForChannelMeasurement are SSB beams. The correct prediction is considered as the ground-truth L1-RSRP of the first reported P-CRI being larger than or equal to the ground-truth RSRP of the strongest beam in resourcesForSetA-r19 minus the tolerance margin.

Table 10.1.48.1-3: CSI-RS based RS resource prediction accuracy requirements in FR2 when resourcesForChannelMeasurement are SSB beams

## 10.1ANR measurements for RedCap

## 10.1A.1Introduction

The requirements in this clause are applicable for RedCap UE as follows:

-intra-frequency requirements apply for PCell measurements in SA,

-inter-frequency requirements apply for non-serving cell measurements on NR carrier frequencies.

-inter-frequency requirements apply for measurements from one cell on a frequency compared to the measurement from another cell on a different frequency.

The accuracy requirements in this clause are applicable for AWGN radio propagation conditions. The accuracy requirements of RSRP, RSRQ and SINR are applicable provided that reference SSB is not changed during measurement period.

## 10.1A.2Intra-frequency RSRP accuracy requirements for FR1

## 10.1A.2.1Intra-frequency SS-RSRP accuracy requirements

## 10.1A.2.1.1Absolute SS-RSRP Accuracy

The accuracy requirements in clause 10.1.2.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.2.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.15 for a corresponding Band for each relevant SSB.

Table 10.1A.2.1.1-1: SS-RSRP Intra-frequency absolute accuracy for 1Rx RedCap UE in FR1

## 10.1A.2.1.2Relative SS-RSRP Accuracy

The accuracy requirements in clause 10.1.2.1.2 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.2.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.15 for a corresponding Band for each relevant SSB.

Table 10.1A.2.1.2-1: SS-RSRP Intra-frequency relative accuracy for 1Rx RedCap UE in FR1

## 10.1A.3Intra-frequency RSRP accuracy requirements for FR2

## 10.1A.3.1Intra-frequency SS-RSRP accuracy requirements

## 10.1A.3.1.1Absolute SS-RSRP Accuracy

The accuracy requirements in clause 10.1.3.1.1 shall apply.

## 10.1A.3.1.2Relative SS-RSRP Accuracy

The accuracy requirements in clause 10.1.3.1.2 shall apply.

## 10.1A.4Inter-frequency RSRP accuracy requirements for FR1

## 10.1A.4.1Inter-frequency SS-RSRP accuracy requirements

## 10.1A.4.1.1Absolute SS-RSRP Accuracy in FR1

The accuracy requirements in clause 10.1.4.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.4.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.16 for a corresponding Band for each relevant SSB.

Table 10.1A.4.1.1-1: SS-RSRP Inter-frequency Absolute accuracy for 1Rx RedCap UE in FR1

## 10.1A.4.1.2Relative SS-RSRP Accuracy in FR1

The accuracy requirements in clause 10.1.4.1.2 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.4.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] clause 7.3 for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.16 for a corresponding Band for each relevant SSB.

-|SSB_RP1dBm - SSB_RP2dBm|  27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

Table 10.1A.4.1.2-1: SS-RSRP Inter-frequency relative accuracy for 1Rx RedCap UE in FR1

## 10.1A.5Inter-frequency RSRP accuracy requirements for FR2

## 10.1A.5.1Inter-frequency SS-RSRP accuracy requirements

## 10.1A.5.1.1Absolute SS-RSRP Accuracy

The accuracy requirements in clause 10.1.5.1.1 shall apply.

## 10.1A.5.1.2Relative SS-RSRP Accuracy

The accuracy requirements in clause 10.1.5.1.2 shall apply.

## 10.1A.6Intra-frequency RSRQ accuracy requirements for FR1

## 10.1A.6.1Intra-frequency SS-RSRQ accuracy requirements in FR1

## 10.1A.6.1.1Absolute SS-RSRQ Accuracy in FR1

The accuracy requirements in clause 10.1.7.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.6.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.15 for a corresponding Band for each relevant SSB.

Table 10.1A.6.1.1-1: SS-RSRQ Intra-frequency absolute accuracy for 1Rx RedCap UE in FR1

## 10.1A.7Intra-frequency RSRQ accuracy requirements for FR2

## 10.1A.7.1Intra-frequency SS-RSRQ accuracy requirements in FR2

## 10.1A.7.1.1Absolute SS-RSRQ Accuracy in FR2

The accuracy requirements in clause 10.1.8.1.1 shall apply.

## 10.1A.8Inter-frequency RSRQ accuracy requirements for FR1

## 10.1A.8.1Inter-frequency SS-RSRQ accuracy requirements in FR1

## 10.1A.8.1.1Absolute SS-RSRQ in FR1

The accuracy requirements in clause 10.1.9.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.8.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.16 for a corresponding Band for each relevant SSB.

Table 10.1A.8.1.1-1: SS-RSRQ Inter-frequency absolute accuracy for 1Rx RedCap UE in FR1

## 10.1A.8.1.2Relative SS-RSRQ Accuracy in FR1

The accuracy requirements in clause 10.1.9.1.2 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.8.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.16 for a corresponding Band for each relevant SSB.

-|SSB_RP1dBm - SSB_RP2dBm|  27 dB

-|Channel 1_Io Channel 2_Io |  20 dB

Table 10.1A.8.1.2-1: SS-RSRQ Inter-frequency relative accuracy for 1Rx RedCap UE in FR1

## 10.1A.9Inter-frequency RSRQ accuracy requirements for FR2

## 10.1A.9.1Inter-frequency SS-RSRQ accuracy requirements in FR2

## 10.1A.9.1.1Absolute SS-RSRQ Accuracy in FR2

The accuracy requirements in clause 10.1.10.1.1 shall apply.

## 10.1A.9.1.2Relative SS-RSRQ Accuracy in FR2

The accuracy requirements in clause 10.1.10.1.2 shall apply.

## 10.1A.10 Intra-frequency SINR accuracy requirements for FR1

## 10.1A.10.1Intra-frequency SS-SINR accuracy requirements in FR1

## 10.1A.10.1.1Absolute SS-SINR Accuracy in FR1

The accuracy requirements in clause 10.1.12.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.10.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for intra-frequency measurements are fulfilled according to annex B.2.15 for a corresponding Band.

Table 10.1A.10.1.1-1: SS-SINR Intra-frequency absolute accuracy for 1Rx RedCap UE in FR1

## 10.1A.11Intra-frequency SINR accuracy requirements for FR2

## 10.1A.11.1Intra-frequency SS-SINR accuracy requirements in FR2

## 10.1A.11.1.1Absolute SS-SINR Accuracy in FR2

The accuracy requirements in clause 10.1.13.1.1 shall apply.

## 10.1A.12 Inter-frequency SINR accuracy requirements for FR1

## 10.1A.12.1Inter-frequency SS-SINR accuracy requirements in FR1

## 10.1A.12.1.1Absolute SS-SINR Accuracy in FR1

The accuracy requirements in clause 10.1.14.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.12.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.16 for a corresponding Band.

Table 10.1A.12.1.1-1: SS-SINR Inter-frequency absolute accuracy for 1Rx RedCap UE in FR1

## 10.1A.12.1.2Relative SS-SINR Accuracy in FR1

The accuracy requirements in clause 10.1.14.1.2 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.12.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for inter-frequency measurements are fulfilled according to annex B.2.16 for a corresponding Band.

-|SSB_RP1dBm - SSB_RP2dBm|  27 dB

-| Channel 1_Io Channel 2_Io |  20 dB

Table 10.1A.12.1.2-1: SS-SINR Inter-frequency relative accuracy for 1Rx RedCap UE in FR1

## 10.1A.13 Inter-frequency SINR accuracy requirements for FR2

## 10.1A.13.1Inter-frequency SS-SINR accuracy requirements in FR2

## 10.1A.13.1.1Absolute SS-SINR Accuracy in FR2

The accuracy requirements in clause 10.1.15.1.1 shall apply.

## 10.1A.13.1.2Relative SS-SINR Accuracy in FR2

The accuracy requirements in clause 10.1.15.1.1 shall apply.

## 10.1A.14L1-RSRP accuracy requirements for FR1

## 10.1A.14.1SSB based L1-RSRP accuracy requirements

## 10.1A.14.1.1Absolute Accuracy

The accuracy requirements in clause 10.1.19.1.1 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.14.1.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

Table 10.1A.14.1.1-1: SSB based L1-RSRP absolute accuracy for 1Rx RedCap UE in FR1

## 10.1A.14.1.2Relative Accuracy

The accuracy requirements in clause 10.1.19.1.2 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.14.1.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.1 for a corresponding Band for each relevant SSB.

Table 10.1A.14.1.2-1: SSB based L1-RSRP relative accuracy for 1Rx RedCap UE in FR1

## 10.1A.14.2CSI-RS based L1-RSRP accuracy requirements

## 10.1A.14.2.1Absolute Accuracy

The accuracy requirements in clause 10.1.19.2.2 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.14.2.1-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1A.19.2.1-1.

Table 10.1A.14.2.1-1: CSI-RS based L1-RSRP absolute accuracy for 1Rx RedCap UE in FR1

## 10.1A.14.2.2Relative Accuracy

The accuracy requirements in clause 10.1.19.2.2 shall apply when RedCap UE is capable of 2Rx. When UE is only required to support 1RX, the absolute accuracy requirements in table 10.1A.14.2.2-1 are valid under the following conditions:

-Conditions defined in clause 7.3I of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for L1-RSRP measurements are fulfilled according to annex B.2.4.2 for a corresponding Band for each relevant CSI-RS.

-The bandwidth of CSI-RS is 48 PRBs and the density is 3.

The performance with larger bandwidth of CSI-RS is equal to or better than the accuracy requirements in table 10.1A.14.2.2-1.

Table 10.1A.14.2.2-1: CSI-RS based L1-RSRP relative accuracy for 1Rx RedCap UE in FR1

## 10.1A.15 L1-RSRP accuracy requirements for FR2

## 10.1A.15.1SSB based L1-RSRP accuracy requirements

## 10.1A.15.1.1Absolute Accuracy

The accuracy requirements in clause 10.1.20.1.1 shall apply.

## 10.1A.15.1.2Relative Accuracy

The accuracy requirements in clause 10.1.20.1.1 shall apply.

## 10.1A.15.2CSI-RS based L1-RSRP accuracy requirements

## 10.1A.15.2.1Absolute Accuracy

The accuracy requirements in clause 10.1.20.1.1 shall apply.

## 10.1A.15.2.2Relative Accuracy

The accuracy requirements in clause 10.1.20.1.1 shall apply.

## 10.1A.16RSTD Measurements for RedCap Positioning

## 10.1A.16.1Introduction

The requirements in clause 10.1A.16 shall apply, provided the UE has received nr-DL-TDOA-RequestLocationInformation message from LMF via LPP TS 37.355 [34] requesting the UE to report one or more DL RSTD measurements defined in TS 38.215 [4].

The requirements in clause 10.1A.16 shall apply,

-When the RedCap UE is in RRC_CONNECTED state and the RSTD measurement is performed with and without RX FH within measurement gap.

-When RedCap UE is in RRC_CONNECTED state and the RSTD measurement is performed without RX FH outside of the measurement gap.

-When RedCap UE is in RRC_CONNECTED state and the RSTD measurement is performed without RX FH when both PPW and measurement gap is configured.

-When RedCap UE is in RRC_INACTIVE state and the RSTD measurement is performed with and without RX FH.

-When RedCap UE is in RRC_IDLE state and the RSTD measurement is performed with and without RX FH.

The requirements defined in clause 10.1A.16 are valid under the conditions defined in clause 10.1.23.

## 10.1A.16.2Measurement Accuracy Requirements

The accuracy requirements for RSTD measurement shall be within ±(X+Y+Z+Δ) Tc. The values of Y, Z and Δ and Rx TEG based requirement are as defined in clause 10.1.23.2. For Rx FH, PRS BW in tables 10.1.23.2-5, 10.1.23.2-5a, 10.1.23.2-6, and 10.1.23.2-6a refer to per hop BW. The requirements for fading channel in this clause are derived based on TDL-A (30 ns delay spread, 5Hz) and TDL-C (60 ns delay spread, 300 Hz) channel models for FR1 and FR2, respectively.

## 10.1A.16.2.1Accuracy requirement for RSTD measurement without RX FH

For 4 sample RSTD measurement performed by 2Rx RedCap UE without RX FH, the values of X, corresponding to the PRS bandwidth supported by the RedCap UE for PRS measurement without RX FH, in tables 10.1.23.2-1 in FR1 for AWGN, 10.1.23.2-2 in FR2 for AWGN, 10.1.23.2-3 in FR1 for fading channel, and 10.1.23.2-4 in FR2 for fading channel apply.

For reduced sample RSTD measurement performed by 2Rx RedCap UE without RX FH, the values of X, corresponding to the PRS bandwidth supported by the RedCap UE for PRS measurement without RX FH, in tables 10.1.23.2-7 in FR1 for AWGN, and 10.1.23.2-8 in FR2 for AWGN apply.

The value of X for 4 sample RSTD measurement performed by 1Rx RedCap UE without RX FH is defined in table 10.1A.16.2.1-1 in FR1 for AWGN, and in table 10.1A.16.2.1-2 in FR1 for fading channel.

The value of X for reduced sample RSTD measurement performed by 1Rx RedCap UE without RX FH is defined in table 10.1A.16.2.1-3 in FR1 for AWGN.

Table 10.1A.16.2.1-1: RSTD absolute accuracy for 1Rx RedCap UE in FR1 for AWGN channel (without RX FH)

Table 10.1A.16.2.1-2: RSTD absolute accuracy for 1Rx RedCap UE in FR1 for fading channel (without RX FH)

Table 10.1A.16.2.1-3: RSTD absolute accuracy for 1Rx RedCap UE in FR1 for AWGN channel with reduced number of samples (without RX FH)

## 10.1A.16.2.2Accuracy requirement for RSTD measurement with RX FH

The value of X for 4 sample RSTD measurement performed by 2Rx RedCap UE with RX FH is defined in tables 10.1A.16.2.2-1 in FR1 for AWGN, 10.1A.16.2.2-2 in FR2 for AWGN, 10.1A.16.2.2-3 in FR1 for fading channel, and 10.1.23.2-4 in FR2 for fading channel, respectively.

The value of X for reduced sample RSTD measurement performed by 2Rx RedCap UE with RX FH is defined in tables 10.1A.16.2.2-5 in FR1 for AWGN, and 10.1A.16.2.2-6 in FR2 for AWGN, respectively.

The value of for 4 sample RSTD measurement performed by 1Rx RedCap UE with RX FH is defined in tables 10.1A.16.2.2-7 in FR1 for AWGN, and 10.1A.16.2.2-8 in FR1 for fading channel, respectively.

The value of for reduced sample RSTD measurement performed by 1Rx RedCap UE with RX FH is defined in table 10.1A.16.2.2-9 in FR1 for AWGN.

Table 10.1A.16.2.2-1: RSTD absolute accuracy for 2Rx RedCap UE in FR1 for AWGN channel (with RX FH)

Table 10.1A.16.2.2-2: RSTD absolute accuracy for 2Rx RedCap UE in FR2 for AWGN channel (with RX FH)

Table 10.1A.16.2.2-3: RSTD absolute accuracy for 2Rx RedCap UE in FR1 for fading channel (with RX FH)

Table 10.1A.16.2.2-4: RSTD absolute accuracy for 2Rx RedCap UE in FR2 for fading channel (with RX FH)

Table 10.1A.16.2.2-5: RSTD absolute accuracy for 2Rx RedCap UE in FR1 for AWGN channel with reduced number of samples (with RX FH)

Table 10.1A.16.2.2-6: RSTD absolute accuracy for 2Rx RedCap UE in FR2 for AWGN channel with reduced number of samples (with RX FH)

Table 10.1A.16.2.2-7: RSTD absolute accuracy for 1Rx RedCap UE in FR1 for AWGN channel (with RX FH)

Table 10.1A.16.2.2-8: RSTD absolute accuracy for 1Rx RedCap UE in FR1 for fading channel (with RX FH)

Table 10.1A.16.2.2-9: RSTD absolute accuracy for 1Rx RedCap UE in FR1 for AWGN channel with reduced number of samples (with RX FH)

## 10.1A.16.3Report Mapping

## 10.1A.16.3.1Absolute DL RSTD Measurement Reporting

Measurement reporting range and report mapping tables defined in clause 10.1.23.3.1 apply to DL RSTD measurement reporting for both 1Rx and 2Rx RedCap UEs and DL RSTD measurement performed with and without RX FH.

## 10.1A.16.3.2Differential Reporting for DL RSTD Measurement

Measurement reporting range and report mapping tables defined in clause 10.1.23.3.2 apply to DL RSTD measurement reporting for both 1Rx and 2Rx RedCap UEs and DL RSTD measurement performed with and without RX FH.

## 10.1A.16.3.3Additional Path Report Mapping for DL RSTD

Measurement reporting range and report mapping tables defined in clause 10.1.23.3.3 apply to DL RSTD measurement reporting for both 1Rx and 2Rx RedCap UEs and DL RSTD measurement performed with and without RX FH.

## 10.1A.17PRS-RSRP Measurements for RedCap positioning

## 10.1A.17.1Introduction

The requirements in clause 10.1A.17 shall apply, provided the UE has received nr-DL-TDOA-RequestLocationInformation or nr-Multi-RTT-RequestLocationInformation or nr-DL-AoD-RequestLocationInformation message from LMF via LPP TS 37.355 [34] requesting the UE to report one or more DL PRS-RSRP measurements defined in TS 38.215 [4].

The requirements in clause 10.1A.17 shall apply,

-When the RedCap UE is in RRC_CONNECTED state and the PRS-RSRP measurement is performed with and without RX FH within measurement gap.

-When RedCap UE is in RRC_CONNECTED state and the PRS-RSRP measurement is performed without RX FH outside of the measurement gap.

-When RedCap UE is in RRC_CONNECTED state and the PRS-RSRP measurement is performed without RX FH when both PPW and measurement gap is configured.

-When RedCap UE is in RRC_INACTIVE state and the PRS-RSRP measurement is performed with and without RX FH.

-When RedCap UE is in RRC_IDLE state and the PRS-RSRP measurement is performed with and without RX FH.

The requirements defined in clause 10.1A.17 are valid under the conditions defined in clause 10.1.24.1.

## 10.1A.17.2Measurement Accuracy Requirements

## 10.1A.17.2.1Absolute PRS RSRP Accuracy Requirement

Accuracy requirement, corresponding to the PRS bandwidth supported by the RedCap UE for measurement without RX FH, defined in clause 10.1.24.2.1 apply to the PRS-RSRP measurement performed by 2Rx RedCap UE without RX FH.

Accuracy requirement in clause 10.1.24.2.1 apply to the PRS-RSRP measurement performed by 2Rx RedCap UE with RX FH, where the PRS bandwidth in clause 10.1.24.2.1 correspond to the PRS bandwidth measured by the RedCap UE per hop.

Accuracy requirement in table 10.1A.17.2.1-1 applies to the 4-sample PRS-RSRP measurement performed by 1Rx RedCap UE without RX FH.

Accuracy requirement in table 10.1A.17.2.1-2 applies to reduced sample PRS-RSRP measurement performed by 1Rx RedCap UE without RX FH

Accuracy requirement in table 10.1A.17.2.1-1 and table 10.1A.17.2.1-2 apply to the PRS-RSRP measurement performed by 1Rx RedCap UE with RX FH, where the PRS bandwidth in table 10.1A.17.2.1-1 and table 10.1A.17.2.1-2 correspond to the PRS bandwidth measured by the RedCap UE per hop.

Table 10.1A.17.2.1-1: PRS-RSRP absolute accuracy for 1Rx RedCap UE in FR1 (without RX FH)

Table 10.1A.17.2.1-2: PRS-RSRP absolute accuracy for 1Rx RedCap UE in FR1 with reduced sample number (without RX FH)

## 10.1A.17.2.2Relative PRS RSRP Accuracy Requirement

Relative accuracy requirement, corresponding to the PRS bandwidth supported by the RedCap UE for measurement without RX FH, defined in clause 10.1.24.2.2 apply to the PRS-RSRP measurement performed by 2Rx RedCap UE without RX FH.

Relative accuracy requirement in clause 10.1.24.2.2 apply to the PRS-RSRP measurement performed by 2Rx RedCap UE with RX FH, where the PRS bandwidth in clause 10.1.24.2.2 correspond to the PRS bandwidth measured by the RedCap UE per hop.

## 10.1A.17.3Report Mapping

## 10.1A.17.3.1Absolute PRS-RSRP Measurement Report Mapping

Measurement reporting range and report mapping tables defined in clause 10.1.24.3.1 apply to PRS-RSRP measurement reporting for both 1Rx and 2Rx RedCap UEs and PRS-RSRP measurement performed with and without RX FH.

## 10.1A.17.3.2Differential Report Mapping for PRS-RSRP Measurement

Measurement reporting range and report mapping tables defined in clause 10.1.24.3.2 apply to PRS-RSRP measurement reporting for both 1Rx and 2Rx RedCap UEs and PRS-RSRP measurement performed with and without RX FH.

## 10.1A.18UE Rx-Tx Time Difference Measurements for RedCap Positioning

## 10.1A.18.1Introduction

The requirements in clause 10.1A.18 shall apply, provided the RedCap UE has received nr-Multi-RTT-RequestLocationInformation message from LMF via LPP TS 37.355 [34] requesting the UE to report one or more UE Rx-Tx time difference measurements defined in TS 38.215 [4]. The requirements in clause 10.1A.18 shall apply:

­When the RedCap UE is in RRC_CONNECTED state and the UE Rx-Tx time difference measurement is performed with and without RX FH within measurement gap.

­When RedCap UE is in RRC_CONNECTED state and the UE Rx-Tx time difference measurement is performed without RX FH outside of the measurement gap.

­When RedCap UE is in RRC_CONNECTED state and the UE Rx-Tx time difference measurement is performed without RX FH when both PPW and measurement gap is configured.

­When RedCap UE is in RRC_INACTIVE state and the UE Rx-Tx time difference measurement is performed with and without RX FH.

## 10.1A.18.2Measurement Accuracy Requirements

The UE Rx-Tx time difference measurement accuracy requirements in this clause shall not apply, if:

-NTA_offset defined in table 7.1A.2-2 changes during the UE Rx-Tx measurement period or

-if the uplink transmission timing changes during the UE Rx-Tx measurement period due to the network-configured Timing Advance.

The UE Rx-Tx time difference measurement accuracy requirements in this clause shall apply provided that:

-The UE transmits SRS within the range from -160 ms to 160 ms of at least one DL PRS resource of each of the TRPs in the assistance data.

If the uplink transmission timing changes during the UE Rx-Tx measurement period due to the autonomous timing adjustment defined in clause 7.1A.2 then:

-UE Rx-Tx measurement accuracy requirements shall apply for a cell, which is also the downlink reference cell (defined in clause 7.1A.1) for SRS transmission even if the uplink transmission timing changes during the UE Rx-Tx measurement period due to autonomous adjustment.

-UE Rx-Tx measurement accuracy requirements shall not apply for a cell, which is not the downlink reference cell (defined in clause 7.1A.1) for SRS transmission, if the uplink transmission timing changes during the UE Rx-Tx measurement period due to autonomous adjustment.

When a serving cell change occurs during the UE Rx-Tx measurement period, the UE Rx-Tx time difference measurement accuracy requirements in this clause shall apply provided that the serving cell change does not impact SRS configuration for the UE Rx-Tx measurement.

The relative accuracy of UE Rx-Tx measurement in this clause is defined as accuracy of the difference between two UE Rx-Tx measurements.

## 10.1A.18.2.1UE Rx-Tx Accuracy Requirement for 2RX RedCap UE without FH

For UE Rx-Tx time difference measurement performed by 2RX RedCap UE without RX FH, the accuracy requirements corresponding to the PRS bandwidth supported by the RedCap UE for PRS measurement without RX FH in clause 10.1.25.2 shall apply.

## 10.1A.18.2.2UE Rx-Tx Accuracy Requirement for 1RX RedCap UE without FH

The accuracy requirements in table 10.1A.18.2.2-1 for FR1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-AWGN propagation condition.

Table 10.1A.18.2.2-1: UE Rx-Tx time difference measurement accuracy in FR1 in AWGN

The accuracy requirements in table 10.1A.18.2.2-1a for FR1 for are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-Number of measurement samples is less than 4.

-AWGN propagation condition.

Table 10.1A.18.2.2-1a: UE Rx-Tx time difference measurement accuracy in FR1 in AWGN with reduced measurement samples

The relative accuracy requirements in table 10.1A.18.2.2-1b for FR1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-AWGN propagation condition.

-the two UE Rx-Tx time difference measurements are associated with the same RxTx TEG.

Table 10.1A.18.2.2-1b: UE Rx-Tx time difference relative measurement accuracy in FR1 in AWGN with TEG reporting

The accuracy requirements in table 10.1A.18.2.2-2 for FR1 for are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-Fading propagation condition.

Table 10.1A.18.2.2-2: UE Rx-Tx time difference measurement accuracy in FR1 in fading

Table 10.1A.18.2.2-3: Margin for UE Rx-Tx time difference measurement accuracy in FR1

## 10.1A.18.2.3UE Rx-Tx Accuracy Requirement for 2RX RedCap UE with FH

The accuracy requirements in table 10.1A.18.2.3-1 for FR1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-AWGN propagation condition.

-The BWtotal as defined in clause 9.9A.4.8 for RRC_CONNECTED and in clause 5.6A.6.6 for RRC_INACTIVE is no less than the “Total PRS bandwidth after FH”.

Table 10.1A.18.2.3-1: UE Rx-Tx time difference measurement accuracy in FR1 in AWGN

The accuracy requirements in table 10.1A.18.2.3-1a for FR1 for are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-Number of measurement samples is less than 4.

-AWGN propagation condition.

-The BWtotal as defined in clause 9.9A.4.8 for RRC_CONNECTED and in clause 5.6A.6.6 for RRC_INACTIVE is no less than the “Total PRS bandwidth after FH”.

Table 10.1A.18.2.3-1a: UE Rx-Tx time difference measurement accuracy in FR1 in AWGN with reduced measurement samples

The accuracy requirements in table 10.1A.18.2.3-2 for FR1 for are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-Fading propagation condition.

-The BWtotal as defined in clause 9.9A.4.8 for RRC_CONNECTED and in clause 5.6A.6.6 for RRC_INACTIVE is no less than the “Total PRS bandwidth after FH”.

Table 10.1A.18.2.3-2: UE Rx-Tx time difference measurement accuracy in FR1 in fading

The accuracy requirements in table 10.1A.18.2.3-3 for FR2 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-AWGN propagation condition.

-The BWtotal as defined in clause 9.9A.4.8 for RRC_CONNECTED and in clause 5.6A.6.6 for RRC_INACTIVE is no less than the “Total PRS bandwidth after FH”.

Table 10.1A.18.2.3-3: UE Rx-Tx time difference measurement accuracy in FR2 in AWGN

The accuracy requirements in table 10.1A.18.2.3.3-3a for FR2 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-Number of measurement samples is less than 4.

-AWGN propagation condition.

-The BWtotal as defined in clause 9.9A.4.8 for RRC_CONNECTED and in clause 5.6A.6.6 for RRC_INACTIVE is no less than the “Total PRS bandwidth after FH”.

Table 10.1A.18.2.3-3a: UE Rx-Tx time difference measurement accuracy in FR2 in AWGN with reduced measurement samples

The accuracy requirements in table 10.1A.18.2.3-4 for FR2 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-2 [19] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-Fading propagation condition.

-The BWtotal as defined in clause 9.9A.4.8 for RRC_CONNECTED and in clause 5.6A.6.6 for RRC_INACTIVE is no less than the “Total PRS bandwidth after FH”.

Table 10.1A.18.2.3-4: UE Rx-Tx time difference measurement accuracy in FR2 in fading

Table 10.1A.18.2.3-5: Margin for UE Rx-Tx time difference measurement accuracy in FR1 with FH

Table 10.1A.18.2.3-6: Margin for UE Rx-Tx time difference measurement accuracy in FR2 with FH

10.1A.18.2.4UE Rx-Tx Accuracy Requirement for 1RX RedCap UE with FH

The accuracy requirements in table 10.1A.18.2.4-1 for FR1 are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-AWGN propagation condition.

Table 10.1A.18.2.4-1: UE Rx-Tx time difference measurement accuracy in FR1 in AWGN

The accuracy requirements in table 10.1A.18.2.4-1a for FR1 for are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-Number of measurement samples is less than 4.

-AWGN propagation condition.

Table 10.1A.18.2.4-1a: UE Rx-Tx time difference measurement accuracy in FR1 in AWGN with reduced measurement samples

The accuracy requirements in table 10.1A.18.2.4-2 for FR1 for are valid under the following conditions:

-Conditions defined in clause 7.3 of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-PRP|dBm according to annex B.2.14 for a corresponding Band.

-Fading propagation condition.

Table 10.1A.18.2.4-2: UE Rx-Tx time difference measurement accuracy in FR1 in fading

## 10.1A.18.3Report mapping

## 10.1A.18.3.1Absolute UE Rx-Tx Measurement Report Mapping

The report mapping as defined in clause 10.1.25.3.1 shall apply.

## 10.1A.18.3.2Differential UE Rx-Tx Measurement Report Mapping

The report mapping as defined in clause 10.1.25.3.2 shall apply.

## 10.1A.18.3.3Additional Path Report Mapping for UE Rx-Tx Time Difference

The report mapping as defined in clause 10.1.25.3.3 shall apply.

## 10.1A.19PRS-RSRPP Measurements for RedCap Positioning

## 10.1A.19.1Introduction

The requirements in clause 10.1A.19.2 shall apply, provided the RedCap UE has received nr-DL-AoD-RequestLocationInformation message from LMF via LPP 37.355 [34] requesting the RedCap UE to report one or more DL PRS-RSRPP measurements defined in TS 38.215 [4]. The requirements in clause 10.1A.19 shall apply:

-when RedCap UE is in RRC_CONNECTED state,

-when RedCap UE is in RRC_INACTIVE state,

-when RedCap UE is in RRC_IDLE state.

The requirements in clause 10.1A.19.2 apply for the first path PRS-RSRP measurement.

## 10.1A.19.2Measurement Accuracy Requirements

## 10.1A.19.2.1Absolute PRS RSRPP accuracy

The absolute accuracy requirements for PRS-RSRPP measurements for 1Rx RedCap UE for FR1 defined in table 10.1A.19.2.1-1 and table 10.1A.19.2.1-2 are valid under the following conditions:

-Conditions defined in TS 38.101-1 [18] clause 7.3 for reference sensitivity are fulfilled.

-PRP 1,2|dBm according to annex B.2.14 for a corresponding Band.

The absolute accuracy requirements for PRS-RSRPP measurements defined in clause 10.1.38.2.1 are reused for 2Rx RedCap UE.

The absolute accuracy requirements for PRS-RSRPP measurement defined in table 10.1A.19.2.1-1 apply for the RedCap UE not supporting supportedDL-PRS-ProcessingSamples TS 37.355 [34] or LMF does not indicate RedCap UE to perform positioning measurements with reduced number of samples.

The absolute accuracy requirements for PRS-RSRPP measurement defined in table 10.1A.19.2.1-2 apply for the RedCap UE supporting supportedDL-PRS-ProcessingSamples TS 37.355 [34].

The absolute accuracy requirements for PRS-RSRPP measurement defined in this clause apply to the measurements with and without frequency hopping. For the measurements with frequency hopping, the accuracy requirements apply for the corresponding PRS bandwidth per hop.

NOTE 1: The requriements in this clause are derived based on two-tap channel defined in TS 38.101-4 [21] annex B.2.4 (a = 1, τd=0.45 µs and fD=5 Hz).

NOTE 2: The requirements in this clause are derived based on the difference between the estimated PRS-RSRPP compared to the ideal PRS-RSRPP defined as

RSRPPp∝kHkexpj2πDpkNIFFT2

Where:

is the effective channel frequency response (over REs occupied by PRS) measured without receiver noise.Hk

is the exact delay of the p-th path in the channel model.Dp

Table 10.1A.19.2.1-1: PRS-RSRPP absolute accuracy for 1Rx RedCap UE for FR1

Table 10.1A.19.2.1-2: PRS-RSRPP absolute accuracy for 1Rx RedCap UE for FR1 for reduced number of samples

## 10.1A.19.3Report mapping

## 10.1A.19.3.1Absolute PRS-RSRPP Measurement Report Mapping

The absolute PRS-RSRPP measurement report mapping defined in clause 10.1.38.3.1 applies.

## 10.1A.19.3.2Differential Report Mapping for PRS-RSRPP Measurement

The differential report mapping for PRS-RSRPP measurement defined in clause 10.1.38.3.2 applies.

## 10.2E-UTRAN measurements

## 10.2.1Introduction

Accuracy requirements for measurements on E-UTRAN carrier frequencies are specified in clause 10.2 and apply for UE in SA or NR-DC or NE-DC operation mode, unless otherwise specified.

Unless otherwise specified, the requirements in clause 10.2 are applicable for a UE:

-in RRC_CONNECTED state

-performing measurements with appropriate measurement gaps according to clause 9.1.2.

-that is synchronised to the cell that is measured.

The reported measurement result after layer 1 filtering shall be an estimate of the average value of the measured quantity over the measurement period. The reference point for the measurement result after layer 1 filtering is referred to as point B in the measurement model described in TS 36.300 [24].

The accuracy requirements of E-UTRA measurements in this clause are valid for the reported measurement result after layer 1 filtering. The accuracy requirements are verified from the measurement report at point D in the measurement model having the layer 3 filtering disabled.

If the UE needs measurement gaps to perform the inter-RAT NR ─ E-UTRAN FDD and NR ─ E-UTRAN TDD measurements, the relevant measurement procedure and measurement gap patterns stated in clause 9.1.2 shall apply.

## 10.2.2E-UTRAN RSRP measurements

NOTE:This measurement is for handover between NR and E-UTRAN.

The measurement period of E-UTRA RSRP in RRC_CONNECTED state is specified in clauses 9.4.2 and 9.4.3.

The accuracy requirements of E-UTRA RSRP measurements in RRC_CONNECTED state and the corresponding side conditions shall be the same as the inter-frequency RSRP Accuracy Requirements in clause 9.1.3 of TS 36.133 [15].

The reporting range and mapping specified for RSRP measurements in clause 9.1.4 of TS 36.133 [15] shall apply.

## 10.2.3E-UTRAN RSRQ measurements

NOTE:This measurement is for handover between NR and E-UTRAN.

The measurement period of E-UTRA RSRQ in RRC_CONNECTED state is specified in clauses 9.4.2 and 9.4.3.

The accuracy requirements of E-UTRA RSRQ measurements in RRC_CONNECTED state and the corresponding side conditions shall be the same as the inter-frequency RSRQ Accuracy Requirements in clause 9.1.6 of TS 36.133 [15].

The requirements for E-UTRA RSRQ measurements accuracy in RRC_CONNECTED state and the corresponding side conditions shall be the same as the inter-frequency RSRQ Accuracy Requirements in clause 9.1.6 of TS 36.133 [15].

The reporting range and mapping specified for RSRQ measurements in clause 9.1.7 of TS 36.133 [15] shall apply.

## 10.2.4E-UTRAN RSTD measurements

The requirements in this clause are valid for UE supporting this capability.

The measurement period is specified in clauses 9.4.4.1 and 9.4.4.2 for inter-RAT NR ─ E-UTRAN FDD and inter-RAT NR ─ E-UTRAN TDD RSTD measurements, respectively.

The accuracy requirements and the corresponding side conditions shall be the same as the inter-frequency measurement accuracy requirements for RSTD measurements in RRC_CONNECTED in clauses 9.1.10.2 of TS 36.133 [15].

If the UE needs measurement gaps to perform the inter-RAT NR ─ E-UTRAN FDD and NR ─ E-UTRAN TDD RSTD measurements, the relevant measurement procedure and measurement gap patterns stated in clause 9.1.2 shall apply.

The reporting range and mapping for the inter-RAT NR ─ E-UTRAN FDD and NR ─ E-UTRAN TDD RSTD measurements is the same as specified for RSTD measurements in TS 36.133 [15, clauses 9.1.10.3 and 9.1.10.4].

## 10.2.5E-UTRAN RS-SINR measurements

NOTE:This measurement is for handover between NR and E-UTRAN.

The measurement period of E-UTRA RS-SINR in RRC_CONNECTED state is specified in clauses 9.4.2 and 9.4.3.

The accuracy requirements of E-UTRA RS-SINR measurements in RRC_CONNECTED state and the corresponding side conditions shall be the same as the inter-frequency RS-SINR Accuracy Requirements in clause 9.1.17.3 of TS 36.133 [15].

The reporting range and mapping for E-UTRA RS-SINR measurements shall be the same as specified for RS-SINR measurements in clause 9.1.17.1 of TS 36.133 [15].

## 10.2.6E-UTRAN RSRP measurements for CA/DC Idle Mode Measurements

NOTE:This measurement is for CA/DC Idle Mode measurements between NR and E-UTRAN.

The requirements in this clause are applicable for a UE:

-in state RRC_IDLE or RRC_INACTIVE

-that is synchronised to the cell that is measured.

The requirements are for absolute E-UTRA RSRP accuracy.

The measurement period of E-UTRA RSRP in RRC_IDLE and RRC_INACTIVE states are specified in clause 4.4.2.

The accuracy requirements of E-UTRA RSRP measurements in RRC_IDLE and RRC_INACTIVE states and the corresponding side conditions shall be as the inter-frequency RSRP Accuracy Requirements in clause 9.1.3B.2 of TS 36.133 [15].

The reporting range and mapping specified for RSRP measurements in clause 9.1.4 of TS 36.133 [15] shall apply.

## 10.2.7E-UTRAN RSRQ measurements for CA/DC Idle Mode Measurements

NOTE:This measurement is for CA/DC Idle Mode measurements between NR and E-UTRAN.

The requirements in this clause are applicable for a UE:

-in state RRC_IDLE or RRC_INACTIVE

-that is synchronised to the cell that is measured.

The requirements are for absolute E-UTRA RSRQ accuracy.

The measurement period of E-UTRA RSRQ in RRC_IDLE and RRC_INACTIVE states are specified in clause 4.4.2.

The accuracy requirements of E-UTRA RSRQ measurements in RRC_IDLE and RRC_INACTIVE states and the corresponding side conditions shall be as the inter-frequency RSRQ Accuracy Requirements in clause 9.1.6B.2 of TS 36.133 [15].

The reporting range and mapping specified for RSRQ measurements in clause 9.1.7 of TS 36.133 [15] shall apply.

## 10.2AE-UTRAN measurements for RedCap

## 10.2A.1Introduction

Accuracy requirements for measurements on E-UTRAN carrier frequencies are specified in clause 10.2A and apply for RedCap UE in SA operation mode, unless otherwise specified.

Unless otherwise specified, the requirements in clause 10.2A are applicable for a UE:

-in RRC_CONNECTED state

-performing measurements with appropriate measurement gaps according to clause 9.1A.2.

-that is synchronised to the cell that is measured.

The reported measurement result after layer 1 filtering shall be an estimate of the average value of the measured quantity over the measurement period. The reference point for the measurement result after layer 1 filtering is referred to as point B in the measurement model described in TS 36.300 [24].

The accuracy requirements of E-UTRA measurements in this clause are valid for the reported measurement result after layer 1 filtering. The accuracy requirements are verified from the measurement report at point D in the measurement model having the layer 3 filtering disabled.

If the UE needs measurement gaps to perform the inter-RAT NR ─ E-UTRAN FDD and NR ─ E-UTRAN TDD measurements, the relevant measurement procedure and measurement gap patterns stated in clause 9.1A.2 shall apply.

## 10.2A.2E-UTRAN RSRP measurements

NOTE:This measurement is for handover between NR and E-UTRAN.

The measurement period of E-UTRA RSRP in RRC_CONNECTED state is specified in clauses 9.4A.2 and 9.4A.3.

For 2Rx RedCap,

-The accuracy requirements of E-UTRA RSRP measurements in RRC_CONNECTED state and the corresponding side conditions shall be the same as the inter-frequency RSRP accuracy requirements for UE other than Cat.1bis in clause 9.1.3 of TS 36.133 [15].

For 1Rx RedCap,

-The accuracy requirements of E-UTRA RSRP measurements in RRC_CONNECTED state and the corresponding side conditions shall be the same as the inter-frequency RSRP accuracy requirements for UE Cat.1bis in clause 9.1.3 of TS 36.133 [15].

The reporting range and mapping specified for RSRP measurements in clause 9.1.4 of TS 36.133 [15] shall apply.

## 10.2A.3E-UTRAN RSRQ measurements

NOTE:This measurement is for handover between NR and E-UTRAN.

The measurement period of E-UTRA RSRQ in RRC_CONNECTED state is specified in clauses 9.4A.2 and 9.4A.3.

For 2Rx RedCap,

-The accuracy requirements of E-UTRA RSRQ measurements in RRC_CONNECTED state and the corresponding side conditions shall be the same as the inter-frequency RSRQ accuracy requirements for UE other than Cat.1bis in clause 9.1.6 of TS 36.133 [15].

For 1Rx RedCap,

-The accuracy requirements of E-UTRA RSRQ measurements in RRC_CONNECTED state and the corresponding side conditions shall be the same as the inter-frequency RSRQ accuracy requirements for UE Cat.1bis in clause 9.1.6 of TS 36.133 [15].

The requirements for accuracy of E-UTRA RSRQ measurements in RRC_CONNECTED state and the corresponding side conditions shall be the same as the inter-frequency RSRQ Accuracy Requirements in clause 9.1.6 of TS 36.133 [15].

The reporting range and mapping specified for RSRQ measurements in clause 9.1.7 of TS 36.133 [15] shall apply.

## 10.2A.4E-UTRAN RS-SINR measurements

NOTE:This measurement is for handover between NR and E-UTRAN.

The measurement period of E-UTRA RS-SINR in RRC_CONNECTED state is specified in clauses 9.4A.2 and 9.4A.3.

For 2Rx RedCap,

-The accuracy requirements of E-UTRA RS-SINR measurements in RRC_CONNECTED state and the corresponding side conditions shall be the same as the inter-frequency RS-SINR accuracy requirements in clause 9.1.17.3 of TS 36.133 [15].

The reporting range and mapping for E-UTRA RS-SINR measurements shall be the same as specified for RS-SINR measurements in clause 9.1.17.1 of TS 36.133 [15].

## 10.3UTRAN FDD Measurements

The requirements in this clause are applicable for a UE:

-in state RRC_CONNECTED

-performing measurements according to clause 9.4.6 with appropriate measurement gaps

-that is synchronised to the cell that is measured.

The reported measurement result after layer 1 filtering shall be an estimate of the average value of the measured quantity over the measurement period. The reference point for the measurement result after layer 1 filtering is referred to as point B in the measurement model described in TS 25.302 [30].

The accuracy requirements in this clause are valid for the reported measurement result after layer 1 filtering. The accuracy requirements are verified from the measurement report at point D in the measurement model having the layer 3 filtering disabled.

## 10.3.1UTRAN FDD CPICH RSCP

NOTE:This measurement is for handover between E-UTRAN and UTRAN FDD.

The requirements in this clause are valid for terminals supporting this capability.

The measurement period for RRC_CONNECTED state is specified in clause 9.4.6.

In RRC_CONNECTED state the accuracy requirements shall meet the absolute accuracy requirements in table 10.3.1-1, under the following conditions:

-CPICH Ec/Io condition for a detectable cell is as specified in clause 9.4.6;

-SCH_Ec/Io condition for a detectable cell is as specified in clause 9.4.6.

Table 10.3.1-1: UTRAN FDD CPICH_RSCP absolute accuracy

If the UE, in RRC_CONNECTED state, needs measurement gaps to perform UTRAN FDD measurements, the relevant UTRAN FDD measurement procedure and measurement gap pattern stated in clause 9.4.6 shall apply.

The reporting range and mapping specified for FDD CPICH RSCP in TS 25.133 [29] shall apply.

## 10.3.2UTRAN FDD CPICH Ec/No

NOTE:This measurement is for handover between E-UTRAN and UTRAN FDD.

The requirements in this clause are valid for terminals supporting this capability.

The measurement period for RRC_CONNECTED state is specified in clause 9.4.6.

In RRC_CONNECTED state the accuracy requirements shall be the same as the inter-frequency measurement accuracy requirements for FDD CPICH Ec/No in TS 25.133 [29].

If the UE, in RRC_CONNECTED state, needs measurement gaps to perform UTRAN FDD measurements, the UTRAN FDD measurement procedure and measurement gap pattern stated in clause 9.4.6 shall apply.

The reporting range and mapping specified for FDD CPICH Ec/No in TS 25.133 [29] shall apply.

## 10.4V2X measurements

## 10.4.1Introduction

The requirements in this clause are applicable for a UE capable of V2X sidelink communication.

The accuracy requirements in this clause are:

-applicable for AWGN radio propagation conditions,

-assume independent interference (noise) at each receiver antenna port.

## 10.4.2Intra-frequency PSBCH-RSRP accuracy requirements for FR1

## 10.4.2.1PSBCH-RSRP Absolute Accuracy

The requirements for absolute PSBCH-RSRP accuracy in this clause apply to a V2X synchronization source on the same frequency as that of the own V2X UE performing the measurement in FR1.

The accuracy requirements in table 10.4.2.1-1 are valid under the following conditions:

-Demodulation reference signals are transmitted from one port.

-Conditions defined in clause 7.3E of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for PSBCH-RSRP measurements are fulfilled according to annex B.4.2 for a corresponding Band for each relevant PSBCH-DMRS.

Table 10.4.2.1-1: Intra-frequency PSBCH-RSRP absolute accuracy in FR1

## 10.4.2.2PSBCH-RSRP Relative Accuracy

The relative PSBCH-RSRP accuracy is defined as the PSBCH-RSRP measured from one V2X synchronization source compared to the PSBCH-RSRP measured from another V2X synchronization source on the same frequency in FR1.

The accuracy requirements in table 10.4.2.2-1 are valid under the following conditions:

-Demodulation reference signals are transmitted from one port.

-Conditions defined in clause 7.3E of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for PSBCH-RSRP accuracy measurements are fulfilled according to annex B.4.2 for a corresponding Band for each relevant PSBCH-DMRS.

Table 10.4.2.2-1: Intra-frequency PSBCH-RSRP relative accuracy in FR1

## 10.4.2AIntra-frequency PSBCH-RSRP accuracy requirements for FR1 under CCA

## 10.4.2A.1PSBCH-RSRP Absolute Accuracy

The requirements for absolute PSBCH-RSRP accuracy in this clause apply to a sidelink synchronization source on the same frequency as that of the own sidelink UE performing the measurement in FR1 under CCA.

The accuracy requirements in table 10.4.2A.1-1 are valid under the following conditions:

-Demodulation reference signals are transmitted from one port.

-Conditions defined in clause 7.3E of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for PSBCH-RSRP measurements are fulfilled according to annex B.4.2 for a corresponding Band for each relevant PSBCH-DMRS.

Table 10.4.2A.1-1: Intra-frequency PSBCH-RSRP absolute accuracy in FR1

## 10.4.2A.2PSBCH-RSRP Relative Accuracy

The relative PSBCH-RSRP accuracy is defined as the PSBCH-RSRP measured from one sidelink synchronization source compared to the PSBCH-RSRP measured from another sidelink synchronization source on the same frequency in FR1 under CCA.

The accuracy requirements in table 10.4.2A.2-1 are valid under the following conditions:

-Demodulation reference signals are transmitted from one port.

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for PSBCH-RSRP accuracy measurements are fulfilled according to annex B.4.2 for a corresponding Band for each relevant PSBCH-DMRS.

-The same number of S-SSB repetitions on frequency domain is configured between two sidelink synchronization sources.

Table 10.4.2A.2-1: Intra-frequency PSBCH-RSRP relative accuracy in FR1

## 10.4.3Intra-Frequency SL-RSSI Measurement Accuracy Requirements for FR1

## 10.4.3.1Absolute SL-RSSI Accuracy

The intra-frequency SL-RSSI requirements are specified in table 10.4.3.1-1. The requirements apply for measurement period of 1 slot and for any configured measurement bandwidth larger than 10 PRBs, provided that:

-All symbols duing each RSSI measurement duration are available for RSSI sampling within the same measurement interval.

Table 10.4.3.1-1: Intra-frequency SL-RSSI absolute accuracy

## 10.4.3AIntra-Frequency SL-RSSI Measurement Accuracy Requirements for FR1 under CCA

## 10.4.3A.1Absolute SL-RSSI Accuracy

The intra-frequency SL-RSSI requirements are specified in table 10.4.3A.1-1 under CCA. The requirements apply for measurement period of 1 slot and for any configured measurement bandwidth larger than 10 PRBs, provided that:

-All symbols during each RSSI measurement duration according to indication of first or second starting symbol within a slot are available for RSSI sampling within the same measurement interval.

Table 10.4.3A.1-1: Intra-frequency SL-RSSI absolute accuracy

## 10.4.4Intra-Frequency L1 SL-RSRP Measurement Accuracy Requirements for FR1

## 10.4.4.1Absolute L1 SL-RSRP Accuracy

The requirements for absolute L1 SL-RSRP accuracy in this clause apply to a UE performing PSCCH-RSRP and/or PSSCH-RSRP measurements on the same frequency as used by operating V2X sidelink communication.

The accuracy requirements in table 10.4.4.1-1 are valid under the following conditions:

-Demodulation reference signals for PSCCH and/or PSSCH are transmitted from one port.

-Conditions defined in clause 7.3E of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-PSCCH-RSRP|dBm and/or PSSCH-RSRP|dBm according to annex B.4.4 for a corresponding Band are fulfilled.

Table 10.4.4.1-1: Intra-frequency L1 SL-RSRP absolute accuracy for UE capable of V2X sidelink communication

## 10.4.4AIntra-Frequency L1 SL-RSRP Measurement Accuracy Requirements for FR1 under CCA

## 10.4.4A.1Absolute L1 SL-RSRP Accuracy

The requirements for absolute L1 SL-RSRP accuracy in this clause apply to a UE performing PSCCH-RSRP and/or PSSCH-RSRP measurements on the same frequency as used by operating sidelink communication under CCA.

The accuracy requirements in table 10.4.4A.1-1 are valid under the following conditions:

-Demodulation reference signals for PSCCH and/or PSSCH are transmitted from one port.

-Conditions defined in clause 7.3F of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-PSCCH-RSRP|dBm and/or PSSCH-RSRP|dBm according to annex B.4.4 for a corresponding Band are fulfilled.

Table 10.4.4A.1-1: Intra-frequency L1 SL-RSRP absolute accuracy for UE capable of sidelink communication

## 10.4.5Intra-Frequency Discovery Signal Measurement Accuracy Requirements

The requirements in this clause are applicable for a remote sidelink UE in U2N relay scenario provided that the remote UE:

-is out of coverage on the frequency used for sidelink, and

-that is synchronised to the sidelink relay UE that is measured.

The requirements in this clause are applicable for a remote sidelink UE in multipath relay scenario provided that the remote UE:

-is synchronised to the sidelink relay UE that is measured and

-is in coverage on the frequency used for sidelink if both the direct path and the sidelink on the indirect path are on the same frequency

-is out of coverage on the frequency used for sidelink if the direct path and the sidelink on the indirect path are on different frequencies.

## 10.4.5.1Absolute Discovery Signal Measurement Accuracy

The accuracy requirements for absolute discovery signal measurement in this clause apply to a sidelink UE performing SL-RSRP measurements for direct to indirect path switch or SL-RSRP measurements for indirect to direct path switch on the same frequency as used by the sidelink relay UE transmitting the relay Discovery message.

The accuracy requirements in table 10.4.5.1-1 are valid under the following conditions:

-Demodulation reference signals for PSCCH and/or PSSCH are transmitted from one port.

-Conditions defined in clause 7.3E of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-PSCCH-RSRP|dBm and/or PSSCH-RSRP|dBm according to annex B.4.4 for a corresponding Band are fulfilled.

Table 10.4.5.1-1: Intra-frequency discovery signal measurement absolute accuracy for a remote sidelink UE [2] capable of sidelink Communication and sidelink Discovery and configured by upper layers for relay operation.

## 10.4ANR Sidelink Measurements for Positioning

## 10.4A.1Introduction

The SL measurements for positioning are performed based on SL-PRS. The SL-PRS reception procedure is as described in TS 38.321 [7]. The UE shall monitor PSCCH to receive the associated SL-PRS in the same slot TS 38.214 [26].

## 10.4A.2SL RSTD measurements

## 10.4A.2.1Measurement Report Mapping

## 10.4A.2.1.1Absolute SL RSTD Measurement Reporting

The reporting range for the SL RSTD measurement is defined from -985024Tc to 985024Tc with the resolution step of 2kTc, where

Tc is defined in TS 38.211 [6],

kmin≤k≤kmax,

kmin=2 and kmax=5, when configured SL-PRS resources of both of the reference UE and the second anchor UE measured for the SL RSTD measurement are in FR1.

The measurement report mapping for different k values are specified in tables 10.4A.2.1.1-1  10.4A.2.1.1-4.

Table 10.4A.2.1.1-1: Report mapping for k=2

Table 10.4A.2.1.1-2: Report mapping for k=3

Table 10.4A.2.1.1-3: Report mapping for k=4

Table 10.4A.2.1.1-4: Report mapping for k=5

## 10.4A.2.2Measurement Accuracy Requirements

The accuracy requirements for SL RSTD measurement shall be within ±(X+Y+Z) Tc, where X, Y, and Z are defined as follows.

X is defined in table 10.4A.2.2-1 for AWGN propagation condition and table 10.4A.2.2-2 for fading propagation condition in FR1, provided that the following conditions are met:

-Conditions defined in clause 7.3E of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-Conditions for SL RSTD measurements are fulfilled according to annex B.4A.1 for a corresponding Band for each relevant SL-PRS resource configured for measurement.

-Y=32 Tc, provided that the time offset between the two SL-PRS resource instances from the reference UE and the second anchor UE, which are used for a single SL RSTD estimate, is no greater than 160 ms.

-Z is defined in table 10.4A.2.2-3 for FR1.

NOTE:The requriements for fading channel in this clause are derived based on TDL-A (30 ns delay spread, 5Hz) channel models for FR1.

Table 10.4A.2.2-1: SL RSTD absolute accuracy in FR1 for AWGN channel

Table 10.4A.2.2-2: SL RSTD absolute accuracy in FR1 for fading channel

Table 10.4A.2.2-3: Margin for SL RSTD measurement accuracy in FR1

## 10.4A.3SL PRS-RSRP measurements

## 10.4A.3.1Measurement Report Mapping

## 10.4A.3.1.1Absolute SL PRS-RSRP Measurement Report Mapping

The reporting range of absolute SL PRS-RSRP measurement is defined from -156 dBm to -31 dBm with 1 dB resolution.

The mapping of measured quantity is defined in table 10.4A.3.1.1-1. The range in the signalling may be larger than the guaranteed accuracy range.

Table 10.4A.3.1.1-1: Measurement report mapping for SL PRS-RSRP

## 10.4A.3.2Measurement Accuracy Requirements

## 10.4A.3.2.1Absolute SL PRS-RSRP accuracy

The absolute accuracy requirements for SL PRS-RSRP measurement for FR1 defined in table 10.4A.3.2.1-1 are valid under the following conditions:

-Conditions defined in 38.101-1 [18] clause 7.3E for reference sensitivity are fulfilled.

-PRP 1,2|dBm according to annex B.4A.1 for a corresponding Band.

Table 10.4A.3.2.1-1: SL PRS-RSRP absolute accuracy for FR1

## 10.4A.4SL Rx-Tx measurements

## 10.4A.4.1Measurement Report Mapping

## 10.4A.4.1.1Absolute SL Rx-Tx Measurement Report Mapping

The reporting range for the absolute SL Rx-Tx time difference measurement (TSL Rx-Tx) is defined from -985024´Tc to 985024´Tc with the resolution step of 2k´Tc, where:

Tc is defined in TS 38.211 [6],

kmin≤k≤kmax,

kmin=2 and kmax=5, when both of the transmitted SL-PRS and the received SL-PRS resources configured for TSL Rx-Tx are in FR1.

The TSL Rx-Tx report mapping for k = 2, 3, 4, and 5 are specified in tables 10.4A.4.1.1-1, 10.4A.4.1.1-2, 10.4A.4.1.1-3, and 10.4A.4.1.1-4, respectively.

Table 10.4A.4.1.1-1: Absolute SL Rx-Tx time difference measurement report mapping for k=2

Table 10.4A.4.1.1-2: Absolute SL Rx-Tx time difference measurement report mapping for k=3

Table 10.4A.4.1.1-3: Absolute SL Rx-Tx time difference measurement report mapping for k=4

Table 10.4A.4.1.1-4: Absolute SL Rx-Tx time difference measurement report mapping for k=5

## 10.4A.4.2Measurement Accuracy

The accuracy requirements for SL Rx-Tx time difference measurement shall be within ±(X+Y+) Tc, where X, Y, and  are defined as follows.

X is defined in table 10.4A.4.2-1 for AWGN propagation condition and table 10.4A.4.2-2 for fading propagation condition in FR1, provided that the following conditions are met:

-Conditions defined in clause 7.3E of TS 38.101-1 [18] for reference sensitivity are fulfilled.

-SL PRP|dBm according to annex B.4A.1 for a corresponding Band.

-The UE transmits SL PRS within -160, 160 msec of at least one SL PRS resource of each of the anchor UEs in the assistance data.

-NTA_offset defined in table 7.1.2-2 does not change during the UE Rx-Tx measurement period when the reference timing used for SL PRS transmissions is a NR serving cell.

If UE indicates tx-TimeInfo when reporting SL Rx-Tx time difference results, the frequency drift margin Y=32 Tc, provided that the time offset between the SL PRS transmission and reception, which are used for a single SL Rx-Tx estimate, is no greater than 160 ms. Otherwise, Y=0.

Margin  are defined in table 10.4A.4.2-3.

Table 10.4A.4.2-1: SL Rx-Tx time difference measurement accuracy in FR1 for AWGN channel

Table 10.4A.4.2-2: SL Rx-Tx time difference measurement accuracy in FR1 for fading channel

Table 10.4A.4.2-3: Margin for UE Rx-Tx time difference measurement accuracy in FR1

## 10.4A.5SL PRS-RSRPP measurements

## 10.4A.5.1Measurement Report Mapping

## 10.4A.5.1.1Absolute SL PRS-RSRPP Measurement Report Mapping

The reporting range of absolute SL PRS-RSRPP measurement is defined from -156 dBm to -31 dBm with 1 dB resolution.

The mapping of measured quantity is defined in table 10.4A.5.1.1-1. The range in the signalling may be larger than the guaranteed accuracy range.

Table 10.4A.5.1.1-1: Measurement report mapping for SL PRS-RSRPP

## 10.4A.5.2Measurement Accuracy

## 10.4A.5.2.1Introduction

The requirements in clause 10.4A.5.2 shall apply provided the UE has received SL-TDOA-RequestLocationInformation or SL-AOA-RequestLocationInformation or SL-TOA-RequestLocationInformation or SL-RTT-RequestLocationInformation from LMF or another UE via SLPP requesting the UE to measure and report SL PRS-RSRPP measurements defined in TS 38.215 [4].

The requirements in clause 10.4A.5.2 apply for the first path SL PRSRSRPP measurement.

## 10.4A.5.2.2Measurement Accuracy Requirements

## 10.4A.5.2.2.2Absolute SL PRS-RSRPP accuracy

The absolute accuracy requirements for SL PRS-RSRPP measurement for FR1 defined in table 10.4A.5.2.2.2-1 are valid under the following conditions:

-Conditions defined in 38.101-1 [18] clause 7.3E for reference sensitivity are fulfilled.

-PRP 1,2|dBm according to annex B.4A.1 for a corresponding Band.

NOTE 1: The requriements in this clause are derived based on two-tap channel defined in TS 38.101-4 [21] annex B.2.4 (a = 1, τd=0.45 µs and fD=5 Hz).

NOTE 2: The requirements in this clause are derived based on the difference between the estimated SL PRSRSRPP compared to the ideal SL PRSRSRPP defined as

RSRPPp∝kHkexpj2πDpkNIFFT2

where:

is the effective channel frequency response (over REs occupied by SL-PRS) measured without receiver noise.Hk

is the exact delay of the p-th path in the channel model.Dp

Table 10.4A.5.2.2.2-1: SL PRS-RSRPP absolute accuracy for FR1

## 10.4A.6SL AoA measurements

## 10.4A.6.1Measurement Report Mapping

## 10.4A.6.1.1Absolute SL AoA Measurement Report Mapping

The UE shall report A-AoA measurement results based on measurement report mapping in this clause. The UE shall report Z-AoA measurement results based on measurement report mapping in this clause.

The reporting range of SL AoA, as defined in TS 38.215 [4], is defined from -180 degree to +180 degree for A-AoA. The reporting resolution is 0.1 degree. The mapping of A-AoA measured quantity is defined in table 10.4A.6.1.1-1.

Table 10.4A.6.1.1-1: A-AoA measurement report mapping

The reporting range of SL AoA, as defined in TS 38.215 [4], is defined from 0 degree to +180 degree for Z-AoA. The reporting resolution is 0.1 degree. The reporting resolution is 0.1 degree. The mapping of Z-AoA measured quantity is defined in table 10.4A.6.1.1-2.

Table 10.4A.6.1.1-2: Z-AoA measurement report mapping

## 10.4A.7SL RTOA measurements

## 10.4A.7.1Measurement Report Mapping

## 10.4A.7.1.1Absolute SL RTOA Measurement Report Mapping

The reporting range of SL RTOA measurement, as defined in clause 5.2.2 of TS 38.215 [4], is defined from -985024Tc to +985024Tc. The reporting resolution is uniform across the reporting range and is defined as T = Tc*2k where

k is selected from the set {02, 3, 4, 5},

Tc is defined in TS 38.211 [6].

The mapping of measured quantity for each reporting resolution (k) is defined in table 10.4A.7.1.1-1 to table 10.4A.7.1.1-4.

Table 10.4A.7.1.1-1: Absolute SL RTOA measurement report mapping for k=2

Table 10.4A.7.1.1-2: Absolute SL RTOA measurement report mapping for k=3

Table 10.4A.7.1.1-3: Absolute SL RTOA measurement report mapping for k=4

Table 10.4A.7.1.1-4: Absolute SL RTOA measurement report mapping for k=5

## 11Void
