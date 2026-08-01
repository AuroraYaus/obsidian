---
type: spec
aliases:
  - 38.133_38133-j50_sA.13-A.14
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.13-A.14/content.md"
---
# TS 38.133 38133-j50_sA.13-A.14

## A.13NR Standalone Tests with NR SCell under CCA and All Other NR Cells in FR1

## A.13.1Void

## A.13.1.1Void

## A.13.1.2Void

## A.13.2Signalling characteristics

## A.13.2.1Void

## A.13.2.2SCell activation and deactivation delay

## A.13.2.2.1SCell Activation and Deactivation of known SCell under CCA, 160 ms SCell measurement cycle

## A.13.2.2.1.1Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for SCell on NR-U SCC with CCA are within the requirements stated in clause 8.3A, when the SCell is known by the UE at the time of activation and the configured SCell measurement cycle is 160 ms.

The supported test configurations are shown in table A.13.2.2.1.1-1.

The test parameters are given in table A.13.2.2.1.1-2 and cell-specific parameters in table A.13.2.2.1.1-3 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two carriers, each with one cell: Cell 1 (PCell) on radio channel 1 (PCC) in NR FR1, and Cell 2 (SCell) on radio channel 2 (SCC) in NR with CCA. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2, as the UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. At the end of T1, the test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. The UE shall be able to report a valid CSI in PCell for the activated SCell at latest in slot m + , as defined in clause 8.3A.2. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot m+  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption shall fall within the time window specified in clause 8.3A.2. At the end of T2 the test equipment sends a MAC message for deactivation of the SCell.THARQ+Tactivation_time_withCCA+TCSI_Reporting_withCCANR slot lengthTHARQ+3 msNR slot length

The point in time at which the MAC message is received by at the UE antenna connector, in a slot # denoted n, defines the start of time period T3. The UE shall complete the activation at latest in slot . Any PCell interruption shall fall within the time window specified in clause 8.3A.3.n+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received, while taking into account CCA failures on SCC.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.13.2.2.1.1-1: Supported test configurations for SCell Activation and Deactivation of known SCell under CCA, 160 ms SCell measurement cycle

Table A.13.2.2.1.1-2: General test parameters for known SCell activation with SCell under CCA, 160 ms SCell measurement cycle

Table A.13.2.2.1.1-3: Cell specific test parameters for known FR1 SCell activation case with SCell under CCA, 160 ms SCell measurement cycle

## A.13.2.2.1.2Test Requirements

During T2, the UE shall send the first CSI report for SCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot m+1+THARQ+3 msNR slot length.

During T2, conditioned on that downlink CCA failures L1 and L2,2 experienced in the SCell fulfill L1 ≤ L1,max and L2,2 ≤ L2,2,max with L1,max = 2 and L2,2,max = 2, respectively, the UE shall send the first valid CSI report (non-zero CQI) for the SCell no later than slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB + L1*Trs + 5 ms and TCSI_reporting_withCCA = TCSI_reporting + L2,2*TCSI-RS + TCSI_ReportingDelay, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot , as defined in clause 8.3A.3.n+THARQ+3 msNR slot length

During T2, interruption on PCell shall not occur outside slot m +1+  to slot m +1+ with TX = TFirstSSB.THARQNR slot lengthTHARQ+3+TXNR slot length

During T3, interruption on PCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PCell shall not be more than specified for SA in clause 8.2.2.2.2.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

## A.13.2.2.2 SCell Activation and Deactivation of known SCell under CCA, 640 ms SCell measurement cycle

## A.13.2.2.2.1Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for SCell on NR-U SCC with CCA are within the requirements stated in clause 8.3A, when the SCell is known by the UE at the time of activation and the configured SCell measurement cycle is 640 ms.

The supported test configurations are same as in table A.13.2.2.1.1-1 above.

The test parameters are same as in table A.13.2.2.1.1-2 above, except for parameters listed below in table A.13.2.2.2.1-1. The cell-specific parameters are same as in table A.13.2.2.1.1-3 above.

The test execution is the same as described in clause A.13.2.2.1 above, except that downlink CCA failures L2,1 and L2,2 with limits L2,1 ≤ L2,1,max and L2,2 ≤ L2,2,max replace L1 as described in clause 8.3A.2 for activation of known SCell with a measurement cycle larger than 160 ms.

Table A.13.2.2.2.1-1: General test parameters for known SCell activation with SCell under CCA, 640 ms SCell measurement cycle

## A.13.2.2.2.2Test Requirements

During T2, the UE shall send the first CSI report for SCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot m+1+THARQ+3 msNR slot length.

During T2, conditioned on that downlink CCA failures L2,1 and L2,2 experienced in the SCell fulfill L2,1 ≤ L2,1,max and L2,2 ≤ L2,2,max with L2,1,max = 2 and L2,2,max = 2, respectively, the UE shall send the first valid CSI report (non-zero CQI) for the SCell no later than slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB_MAX + L2,1*TSMTC_MAX + (1 +L2,2)*Trs + 5 ms and TCSI_reporting_withCCA = TCSI_reporting + TCSI_ReportingDelay, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot , as defined in clause 8.3A.3.n+THARQ+3 msNR slot length

During T2, interruption on PCell shall not occur outside slot m +1+  to slot m +1+ with TX = TFirstSSB.THARQNR slot lengthTHARQ+3+TXNR slot length

During T3, interruption on PCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PCell shall not be more than specified for SA in clause 8.2.2.2.2.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

## A.13.2.2.3SCell Activation and Deactivation of unknown SCell under CCA

## A.13.2.2.3.1Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for SCell on NR-U SCC with CCA are within the requirements stated in clause 8.3A, when the SCell is unknown to the UE at the time of activation.

The supported test configurations are same as in table A.13.2.2.1.1-1 above.

The test parameters are same as in table A.13.2.2.1.1-2 above, except for parameters listed below in table A.13.2.2.3.1-1. The cell-specific parameters are same as in table A.13.2.2.1.1-3 above.

The test execution is the same as described in clause A.13.2.2.1 above, except that downlink CCA failures L3,1 and L3,2 with limits L3,1 ≤ L3,1,max and L3,2 ≤ L3,2,max replace L1 as described in clause 8.3A.2 for activation of unknown SCell.

Table A.13.2.2.3.1-1: General test parameters for unknown SCell activation with SCell under CCA

## A.13.2.2.3.2Test Requirements

During T2, the UE shall send the first CSI report for SCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot m+1+THARQ+3 msNR slot length.

During T2, conditioned on that downlink CCA failures L3,1 and L3,2 experienced in the SCell fulfill L3,1 ≤ L3,1,max and L3,2 ≤ L3,2,max with L3,1,max = 2 and L3,2,max = 2, respectively, the UE shall send the first valid CSI report (non-zero CQI) for the SCell no later than slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB_MAX + (1 + L3,1)*TSMTC_MAX + (2 + L3,2)*Trs + 5 ms and TCSI_reporting_withCCA = TCSI_reporting + TCSI_ReportingDelay, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot , as defined in clause 8.3A.3.n+THARQ+3 msNR slot length

During T2, interruption on PCell shall not occur outside slot m +1+  to slot m +1+ with TX = TFirstSSB.THARQNR slot lengthTHARQ+3+TXNR slot length

During T3, interruption on PCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PCell shall not be more than specified for SA in clause 8.2.2.2.2.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

## A.13.2.3Void

## A.13.3Measurement procedure

## A.13.3.1Intra-frequency measurements

## A.13.3.1.1Event-triggered reporting tests on SCC without gaps under non-DRX

## A.13.3.1.1.1Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.5.1 and 9.2A.5.2.

## A.13.3.1.1.2Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), and two cells on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model: SCell (Cell 2) and a neighbour cell (Cell 3). The test parameters for the three cells are given in table A.13.3.1.1.2-1 and A.13.3.1.1.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

Table A.13.3.1.1.2-1: Supported test configurations

Table A.13.3.1.1.2-2: General test parameters for intra-frequency event triggered reporting without gaps

Table A.13.3.1.1.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gaps

## A.13.3.1.1.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_intra_without_index_CCA ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

Tidentify_intra_cca_without_index = (TPSS/SSS_sync_intra_cca + T SSB_measurement_period_intra_cca) ms, where

TPSS/SSS_sync_intra_cca: it is the time period used in PSS/SSS detection given in table 9.2A.5.1-1.

T SSB_measurement_period_intra_cca: equal to a measurement period of SSB based measurement given in table 9.2A.5.2-1.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.13.3.1.2Event-triggered reporting tests on SCC without gaps under DRX

## A.13.3.1.2.1Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.5.1 and 9.2A.5.2.

## A.13.3.1.2.2Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), and two cells on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model: SCell (Cell 2) and a neighbour cell (Cell 3). The test parameters for the three cells are given in table A.13.3.1.2.2-1 and A.13.3.1.2.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.13.3.1.2.2-1: Supported test configurations

Table A.13.3.1.2.2-2: General test parameters for intra-frequency event triggered reporting without gaps with DRX

Table A.13.3.1.2.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gaps

## A.13.3.1.2.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_intra_without_index_CCA ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

Tidentify_intra_cca_without_index = (TPSS/SSS_sync_intra_cca + T SSB_measurement_period_intra_cca) ms, where

TPSS/SSS_sync_intra_cca: it is the time period used in PSS/SSS detection given in table 9.2A.5.1-1.

T SSB_measurement_period_intra_cca: equal to a measurement period of SSB based measurement given in table 9.2A.5.2-1.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.13.3.1.3Event-triggered reporting tests on SCC with per-UE gaps under non-DRX

## A.13.3.1.3.1Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.6.1 and 9.2A.6.2.

## A.13.3.1.3.2Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), and two cells on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model: SCell (Cell 2) and a neighbour cell (Cell 3). The test parameters for the three cells are given in table A.13.3.1.3.2-1 and A.13.3.1.3.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There are two BWPs configured in Cell 1, BWP0 which contains the cell defining SSB, and BWP1 which does not contain any SSB of Cell 1. During the whole test, BWP1 is always scheduled as the active BWP for the UE.

Table A.13.3.1.3.2-1: Supported test configurations

Table A.13.3.1.3.2-2: General test parameters for intra-frequency event triggered reporting with per-UE gaps

Table A.13.3.1.3.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gap

## A.13.3.1.3.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_intra_without_index_CCA ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

Tidentify_intra_cca_without_index = (TPSS/SSS_sync_intra_cca + T SSB_measurement_period_intra_cca) ms, where

TPSS/SSS_sync_intra_cca: it is the time period used in PSS/SSS detection given in table 9.2A.6.1-1.

T SSB_measurement_period_intra_cca: equal to a measurement period of SSB based measurement given in table 9.2A.6.2-1.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.13.3.1.4Event-triggered reporting tests on SCC with per-UE gaps under DRX

## A.13.3.1.4.1Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.6.1 and 9.2A.6.2.

## A.13.3.1.4.2Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), and two cells on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model: SCell (Cell 2) and a neighbour cell (Cell 3). The test parameters for the three cells are given in table A.13.3.1.4.2-1 and A.13.3.1.4.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There are two BWPs configured in Cell 1, BWP0 which contains the cell defining SSB, and BWP1 which does not contain any SSB of Cell 1. During the whole test, BWP1 is always scheduled as the active BWP for the UE.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.13.3.1.4.2-1: Supported test configurations

Table A.13.3.1.4.2-2: General test parameters for intra-frequency event triggered reporting without gap with DRX

Table A.13.3.1.4.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gap

## A.13.3.1.4.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_intra_without_index_CCA ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

Tidentify_intra_cca_without_index = (TPSS/SSS_sync_intra_cca + T SSB_measurement_period_intra_cca) ms, where

TPSS/SSS_sync_intra_cca: it is the time period used in PSS/SSS detection given in table 9.2A.6.1-1.

T SSB_measurement_period_intra_cca: equal to a measurement period of SSB based measurement given in table 9.2A.6.2-1.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.13.3.1.5Void

## A.13.3.1.6Void

## A.13.3.2Inter-frequency measurements

## A.13.3.2.1Void

## A.13.3.2.2Void

## A.13.3.2.3Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used

## A.13.3.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements for NR cell with CCA in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as SCell in FR1 with CCA on NR RF channel 2 and NR Cell 3 as neighbour cell in FR1 with CCA on NR RF channel 3.  The test parameters are given in tables A.13.3.2.3.1-1, A.13.3.2.3.1-2 and A.13.3.2.3.1-3.

In this test, measurement gap pattern configuration # 0 as defined in table A.13.3.2.3.1-2 is provided

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

Table A.13.3.2.3.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1 with CCA

Table A.13.3.2.3.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

Table A.13.3.2.3.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

## A.13.3.2.3.2Test Requirements

In this test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

For test 1, MGRP = 40 ms and for test 2 MGRP = 20 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.13.3.2.4Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used

## A.13.3.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as SCell in FR1 with CCA on NR RF channel 2 and NR Cell 3 as neighbour cell in FR1 with CCA on NR RF channel 3.  The test parameters are given in tables A.13.3.2.4.1-1, A.13.3.2.4.1-2 and A.13.3.2.4.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.13.3.2.4.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.13.3.2.4.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1 with CCA

Table A.13.3.2.4.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

Table A.13.3.2.4.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

Table A.13.3.2.4.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.13.3.2.4.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.13.3.2.4.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2 UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1 DRX cycle = 40 ms and for test 2 DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.13.3.2.5Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used

## A.13.3.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as SCell in FR1 with CCA on NR RF channel 2 and NR Cell 3 as neighbour cell in FR1 with CCA on NR RF channel 3.   The test parameters are given in tables A.13.3.2.5.1-1, A.13.3.2.5.1-2 and A.13.3.2.5.1-3.

Measurement gap pattern configuration # 0 as defined in table A.13.3.2.5.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

Table A.13.3.2.5.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1 with CCA

Table A.13.3.2.5.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

Table A.13.3.2.5.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

## A.13.3.2.5.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In this test UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.13.3.2.6Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used

## A.13.3.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as SCell in FR1 with CCA on NR RF channel 2 and NR Cell 3 as neighbour cell in FR1 with CCA on NR RF channel 3.  The test parameters are given in tables A.13.3.2.6.1-1, A.13.3.2.6.1-2 and A.13.3.2.6.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.13.3.2.6.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.13.3.2.6.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1 with CCA

Table A.13.3.2.6.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

Table A.13.3.2.6.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

Table A.13.3.2.6.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.13.3.2.6.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.13.3.2.6.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.In test 2 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2 UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1 DRX cycle = 40 ms and for test 2 DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.13.3.3L1-RSRP measurements for beam reporting

## A.13.3.3.1SSB based L1-RSRP measurement when DRX is not used

## A.13.3.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.13.3.3.1.1-1.

Table A.13.3.3.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.13.3.3.1.2Test parameters

There are two cells in the tests, FR1 PCell (Cell 1) and FR1 SCell (Cell 2). Cell 2 operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. The test parameters and applicability for Cell 1 and Cell 2 are given in table A.13.3.3.1.2-1 and table A.13.3.3.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.13.3.3.1.2-1: General test parameters

Table A.13.3.3.1.2-2: SSB specific test parameters

## A.13.3.3.1.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 2.

NOTE:The actual overall delays measured in the test may be up to 2xTTI DCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.13.3.3.2SSB based L1-RSRP measurement when DRX is used

## A.13.3.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.13.3.3.1.1-1.

Table A.13.3.3.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.13.3.3.2.2Test parameters

There are two cells in the tests, FR1 Pcell (Cell 1) and FR1 Scell (Cell 2). Cell 2 operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. The test parameters and applicability for Cell 1  and Cell 2 are given in table A.13.3.3.2.2-1 and table A.13.3.3.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.13.3.3.2.2-1: General test parameters

Table A.13.3.3.2.2-2: SSB specific test parameters

## A.13.3.3.2.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 2.

NOTE:The actual overall delays measured in the test may be up to 2xTTI DCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.13.4Measurement performance

## A.13.4.1SS-RSRP

## A.13.4.1.1Intra-frequency measurement accuracy on a carrier frequency with CCA

## A.13.4.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy on the carrier frequency with CCA is within the specified limits. This test will verify the requirements in clauses 10.1.36.1.1 and 10.1.36.1.2 for intra-frequency measurements under CCA.

## A.13.4.1.1.2Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), and two cells on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model: SCell (Cell 2) and a neighbour cell (Cell 3). Supported test configurations are shown in table A.13.4.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.13.4.1.1.2-2.

Table A.13.4.1.1.2-1: SS-RSRP  Intra frequency SS-RSRP supported test configurations

Table A.13.4.1.1.2-2: SS-RSRP Intra frequency test parameters

## A.13.4.1.1.3Test Requirements

The SS-RSRP measurement accuracy for Cell 2 and Cell 3 shall fulfil absolute requirement in clause 10.1.36.1.1 and relative requirement in clause 10.1.36.1.2.

## A.13.4.2SS-RSRQ

## A.13.4.2.1Intra-frequency measurement accuracy on SCC

## A.13.4.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.29.1.1.

## A.13.4.2.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.13.4.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.13.4.2.1.2-2 and table A.13.4.2.1.2-3. In all test cases, Cell 1 is the PCell, Cell 2 is the SCell with CCA, and Cell 3 is the target cell with CCA. Three sub-tests (Test 1, Test 2, and Test 3) are provided different Noc on Cells 1, 2, and 3.

Table A.13.4.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

Table A.13.4.2.1.2-2: SS-RSRQ Intra frequency test parameters

Table A.13.4.2.1.2-3: SS-RSRQ Intra frequency test parameters for NR PCell

## A.13.4.2.1.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.29.1.1.

## A.13.4.3SS-SINR

## A.13.4.3.1Intra-frequency measurement accuracy on SCC

## A.13.4.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.31.1.1.

## A.13.4.3.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.13.4.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.13.4.3.1.2-2 and table A.13.4.3.1.2-3. In all test cases, Cell 1 is the PCell, Cell 2 is the SCell with CCA, and Cell 3 is the target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 1, 2, and 3.

Table A.13.4.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

A.13.4.3.1.2-2: SS-SINR Intra frequency test parameters

A.13.4.3.1.2-3: SS-SINR Intra frequency test parameters for NR PCell

## A.13.4.3.1.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.31.1.1.

## A.13.4.4L1-RSRP measurement for beam reporting with CCA serving cell

## A.13.4.4.1SSB based L1-RSRP measurement

## A.13.4.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.33.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.13.4.4.1.1-1.

Table A.13.4.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.13.4.4.1.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a SCell under CCA (Cell 2). Cell 2 operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model.

Two sub-tests (Test 1 and Test 2) are provided with different Noc  on Cell 2. The test parameters for the Cell 1 and Cell 2 are given in table A.13.4.4.1.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.13.4.4.1.2-1.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. On Cell 2, UE is configured to perform L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.13.4.4.1.2-1: FR1 SSB based L1-RSRP test parameters

## A.13.4.4.1.3Test Requirements

In both Test 1 and Test 2, the L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 2 shall fulfil the requirements in clauses 10.1.33.1.

## A.13.4.5RSSI

## A.13.4.5.1 Intra-frequency RSSI measurement accuracy on a carrier with CCA

## A.13.4.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.1.

## A.13.4.5.1.2Test parameters

In all test cases, Cell 1 is the PCell on a licensed FR1 band and Cell 2 is the SCell with CCA. RSSI is measured on channel number 2. Supported test configurations are shown in table A.13.4.5.1.2-1. The accuracy of RSSI intra-frequency measurements is tested by using the parameters in A.13.4.5.1.2-2 and A.13.4.5.1.2-3.

Table A.13.4.5.1.2-1: Intra frequency RSSI supported test configurations

Table A.13.4.5.1.2-2: RSSI Intra frequency test parameters

Table A.13.4.5.1.2-3: RSSI RMTC parameters

## A.13.4.5.1.3Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.1. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

## A.13.4.5.2Inter-frequency RSSI measurement accuracy on a carrier with CCA

## A.13.4.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.2.

## A.13.4.5.2.2Test parameters

In all test cases, Cell 1 is the PCell on a licensed FR1 band and Cell 2 is the neighbour with CCA. RSSI is measured on channel number 2. Supported test configurations are shown in table A.13.4.5.2.2-1. The accuracy of RSSI inter-frequency measurements is tested by using the parameters in A.13.4.5.2.2-2 and A.13.4.5.2.3.

Table A.13.4.5.2.2-1: Inter frequency RSSI supported test configurations

Table A.13.4.5.2.2-2: RSSI Inter frequency test parameters

Table A.13.4.5.2.2-3: RSSI RMTC parameters

## A.13.4.5.2.3Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.2. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

## A.13.4.6Channel occupancy

## A.13.4.6.1Intra-frequency channel occupancy measurement accuracy on SCC with CCA

## A.13.4.6.1.1Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.1.

## A.13.4.6.1.2Test parameters

In all test cases, Cell 1 is the PCell on a licensed FR1 band and Cell 2 is the SCell with CCA. Channel occupancy is measured on channel number 2. Supported test configurations are shown in table A.13.4.6.1.2-1. The accuracy of channel occupancy intra-frequency measurements is tested by using the parameters in A.13.4.6.1.2-2 and A.13.4.6.1.2-3.

Table A.13.4.6.1.2-1: Intra frequency CO supported test configurations

Table A.13.4.6.1.2-2: CO Intra frequency test parameters

Table A.13.4.6.1.2-3: CO RMTC parameters

## A.13.4.6.1.3Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

## A.13.4.6.2Inter-frequency channel occupancy measurement accuracy on a carrier with CCA

## A.13.4.6.2.1Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.2.

## A.13.4.6.2.2Test parameters

In all test cases, Cell 1 is the PCell on a licensed FR1 band and Cell 2 is the neighbour with CCA. Channel occupancy is measured on channel number 2. Supported test configurations are shown in table A.13.4.6.2.2-1. The accuracy of channel occupancy inter-frequency measurements is tested by using the parameters in A.13.4.6.2.2-2 and A.13.4.6.2.3.

Table A.13.4.6.2.2-1: Inter frequency CO supported test configurations

Table A.13.4.6.2.2-2: CO Inter frequency test parameters

Table A.13.4.6.2.2-3: CO RMTC parameters

## A.13.4.6.2.3Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

## A.14NR standalone tests for Satellite access

## A.14.1RRC_IDLE state mobility

## A.14.1.1Cell reselection to FR1 intra-frequency NR case

## A.14.1.1.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.3, including the SSB periodicity of the target cell is 160ms.

## A.14.1.1.2Test Parameters

The test scenario comprises of 2 cells on 1 NR carrier configured each in a different satellite as given in tables A.14.1.1.2-1, A.14.1.1.2-2 and A.14.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.14.1.1.2-1: Supported test configurations

Table A.14.1.1.2-2: General test parameters for intra frequency NR cell re-selection test case

Table A.14.1.1.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case

## A.14.1.1.3Test Requirements

For test configuration 1, 2 and 3, the cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than:

## 34 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.1.2-2); or

## 66 s if Kmulti_SMTC is equal to 2.

For test configuration 1 and 2, the cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than:

## 8 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.1.2-2); or

## 14.5 s if Kmulti_SMTC is equal to 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Kmulti_SMTC *Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Kmulti_SMTC *Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_IntraSee Table 4.2C.2.3-1 in clause 4.2C.2.3

Tevaluate, NR_ intraSee Table 4.2C.2.3-1 in clause 4.2C.2.3

Kmulti_SMTC  is described in clause 4.2C.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 20 ms period and 80 ms period, respectively.

If Kmulti_SMTC = 1, Kmulti_SMTC *Tevaluate, NR_Intra + TSI-NR = 7.68 s; allow 8 s. And Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 33.28 s, allow 34 s.

If K_multi_SMTC = 2,  Kmulti_SMTC *Tevaluate, NR_Intra + TSI-NR = 14.08 s; allow 14.5 s. And Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 65.28 s, allow 66 s.

## A.14.1.2Cell reselection to FR1 intra-frequency NR cell for UE configured with the feature for enhanced requirements

## A.14.1.2.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.3.

## A.14.1.2.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.14.1.2.2-1, A.14.1.2.2-2 and A.14.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. The flag enhancedMeasurementNGSO-r17 should be set.

Table A.14.1.2.2-1: Supported test configurations

Table A.14.1.2.2-2: General test parameters for intra frequency NR cell re-selection test case

Table A.14.1.2.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case

## A.14.1.2.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than:

## 11 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.2.2-2); or

## 20 s if Kmulti_SMTC is equal to 2.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than:

## 6 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.2.2-2); or

## 9 s if Kmulti_SMTC is equal to 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Kmulti_SMTC *Tdetect, NR_Intra_enh + TSI-NR, and to an already detected cell can be expressed as: Kmulti_SMTC *Tevaluate, NR_ intra_enh + TSI-NR,

Where:

Tdetect, NR_Intra_enhSee Table 4.2C.2.3-2 in clause 4.2C.2.3

Tevaluate, NR_ Intra_enhSee Table 4.2C.2.3-2 in clause 4.2C.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 20 ms period and 80 ms period, respectively.

If Kmulti_SMTC = 1, Kmulti_SMTC *Tevaluate, NR_Intra_enh + TSI-NR = 5.12 s; allow 6 s. And Kmulti_SMTC *Tdetect, NR_ Intra_enh + TSI-NR = 10.24 s, allow 11 s.

If K_multi_SMTC = 2,  Kmulti_SMTC *Tevaluate, NR_Intra_enh + TSI-NR = 8.96 s; allow 9 s. And Kmulti_SMTC *Tdetect, NR_Intra_enh + TSI-NR = 19.2 s, allow 20 s.

## A.14.1.3Time-based measurement initiation to FR1 intra-frequency NR cell reselection

## A.14.1.3.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.3.

## A.14.1.3.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.14.1.3.2-1, A.14.1.3.2-2 and A.14.1.3.2-3. The test consists of two successive time periods, with time duration of T1 and T2, respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. t-Service broadcasted in SIB19 of Cell 1 is set to the time point that is 36 s after start of T2.

Table A.14.1.3.2-1: Supported test configurations

Table A.14.1.3.2-2: General test parameters for intra frequency NR cell re-selection test case

Table A.14.1.3.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case

## A.14.1.3.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than :

## 36 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.3.2-2); or

## 66 s if Kmulti_SMTC is equal to 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Kmulti_SMTC *Tdetect, NR_Intra + TSI-NR,

Where:

Tdetect, NR_IntraSee Table 4.2C.2.3-1 in clause 4.2C.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 20 ms period and 80 ms period, respectively.

If Kmulti_SMTC = 1, Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 33.28 s, allow 34 s.

If Kmulti_SMTC = 2, Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 65.28 s, allow 66 s.

## A.14.1.4Location-based measurement initiation to FR1 intra-frequency NR cell reselection

## A.14.1.4.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.3.

## A.14.1.4.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.14.1.a4.2-1, A.14.1.a4.2-2 and A.14.1.a4.2-3. The test consists of two successive time periods, with time duration of T1 and T2, respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

At 4 s after the start of T2, the UE location is changed such that the distance to the reference location broadcasted in SIB19 of Cell 1 is exceeded by the configured value in distanceThresh plus 50m.

Table A.14.1.4.2-1: Supported test configurations

Table A.14.1.4.2-2: General test parameters for intra frequency NR cell re-selection test case

Table A.14.1.4.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case

## A.14.1.4.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than:

## 34 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.3.2-2); or

## 66 s if Kmulti_SMTC is equal to 2.

The UE starts searching for the cell only after 4 s after the start of T2 when the UE location is changed such that the distance to the reference location broadcasted in SIB19 of Cell 1 is exceeded by the configured value in distanceThresh plus 50m. Consideing that the cell re-selection delay to a newly detectable cell shall be less than 38 s if Kmulti_SMTC  is  equal to 1 or 70 s if Kmulti_SMTC is equal to 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Kmulti_SMTC *Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Kmulti_SMTC *Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_IntraSee Table 4.2C.2.3-1 in clause 4.2C.2.3

Tevaluate, NR_ intraSee Table 4.2C.2.3-1 in clause 4.2C.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 20 ms period and 80 ms period, respectively.

If Kmulti_SMTC = 1, Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 33.28 s, allow 34 s.

If Kmulti_SMTC = 2, Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 65.28 s, allow 66 s.

## A.14.1.5Cell reselection to FR1 inter-frequency NR case

## A.14.1.5.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.4.

## A.14.1.5.2Test Parameters

The test scenario comprises of 2 NR carriers and 2 cells as given in tables A.14.1.5.2-1, A.14.1.5.2-2 and A.14.1.5.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.14.1.5.2-1: Supported test configurations

Table A.14.1.5.2-2: General test parameters for inter frequency NR cell re-selection test case

Table A.14.1.5.2-3: Cell specific test parameters for inter frequency NR cell re-selection test case

## A.14.1.5.3Test Requirements

The cell reselection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps again on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Thigher_priority_searchSee clause 4.2C.2.9

Tevaluate, NR_ interSee tables 4.2C.2.4-1 in clause 4.2C.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority

## A.14.1.6Cell re-selection to FR1 inter-frequency NR cell for UE configured with feature for enhanced requirements

## A.14.1.6.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell re-selection requirements for satellite access specified in clause 4.2C.2.4.

## A.14.1.6.2Test Parameters

The test scenario comprises of 2 NR carriers and 2 cells as given in tables A.14.1.6.2-1, A.14.1.6.2-2 and A.14.1.6.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3, respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1. The flag enhancedMeasurementNGSO-r17 should be set.

Table A.14.1.6.2-1: Supported test configurations

Table A.14.1.6.2-2: General test parameters for inter frequency NR cell re-selection test case

Table A.14.1.6.2-3: Cell specific test parameters for inter frequency NR cell re-selection test case

## A.14.1.6.3Test Requirements

The cell re-selection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps again on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 66 s.

The cell re-selection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 6 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_inter_enh + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR_inter_enh + TSI-NR,

Where:

Thigher_priority_searchSee clause 4.2C.9

Tevaluate, NR_inter_enhSee tables 4.2C.2.4-2 in clause 4.2C.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 65.12 s, allow 66 s for the cell re-selection delay to a higher priority

## A.14.1.7Time-based measurement initiation to FR1 inter-frequency cell reselection

## A.14.1.7.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.4.

## A.14.1.7.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.14.1.7.2-1, A.14.1.7.2-2 and A.14.1.7.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas, and Cell 2 is of lower priority than Cell 1. Furthermore, UE has not registered with network for the tracking area containing Cell 2. t-Service broadcasted in SIB19 of Cell 1 is set to the time point that is 36 s after start of T2.

Table A.14.1.7.2-1: Supported test configurations

Table A.14.1.7.2-2: General test parameters for inter frequency NR cell re-selection test case

Table A.14.1.7.2-3: Cell specific test parameters for inter frequency NR cell re-selection test case

## A.14.1.7.3Test Requirements

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 36 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Tevaluate, NR_ interSee Table 4.2C.2.4-1 in clause 4.2C.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 80 ms period.

## A.14.1.8Location-based measurement initiation to FR1 inter-frequency NR cell reselection

## A.14.1.8.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.4.

## A.14.1.8.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.14.1.8.2-1, A.14.1.8.2-2 and A.14.1.8.2-3. The test consists of two successive time periods, with time duration of T1and T2, respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas, and Cell 2 is of lower priority than Cell 1. Furthermore, UE has not registered with network for the tracking area containing Cell 2.At 4 s after the start of T2, the UE location is changed such that the distance to the reference location broadcasted in SIB19 of Cell 1 is exceeded by the configured value in distanceThresh plus 50m.

Table A.14.1.8.2-1: Supported test configurations

Table A.14.1.8.2-2: General test parameters for inter frequency NR cell re-selection test case

Table A.14.1.8.2-3: Cell specific test parameters for inter frequency NR cell re-selection test case

## A.14.1.8.3Test Requirements

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 36 s.The UE starts searching for the cell only after 4 s after the start of T2 when the UE location is changed such that the distance to the reference location broadcasted in SIB19 of Cell 1 is exceeded by the configured value in distanceThresh plus 50m. Consideing that the cell re-selection delay to a newly detectable cell shall be less than 40 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Tevaluate, NR_ interSee Table 4.2C.2.4-1 in clause 4.2C.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 80 ms period.

## A.14.1.9Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion

## A.14.1.9.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements specified in clause 4.2C.2.8, for UEs that support Relaxed cell reselection on GSO feature, as defined in clause 5.4 in 38.306 [14], and fulfilling low mobility relaxed measurement criterion.

## A.14.1.9.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.14.1.9.2-1, A.14.1.9.2-2 and A.14.1.9.2-3. The test consists of two successive time periods, with time duration of T1 and T2, respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

As specified in the Test Purpose, the UE is configured with the relaxed measurement criterion for UE with low mobility defined in clause 5.2.4.9.1 in TS 38.304 [1]. So, Cell 2 and Cell 1 configure the UE as follows:

lowMobilityEvalutation TS 38.331 [2] criterion is configured according to the parameters listed in table A.14.1.9.2-3;

cellEdgeEvaluation TS 38.331 [2] criterion is not configured;

combineRelaxedMeasCondition TS 38.331 [2] is not configured;

Table A.14.1.9.2-1: Supported test configurations

Table A.14.1.9.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case for UE fulfilling low mobility criterion

Table A.14.1.9.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

## A.14.1.9.3Test Requirements

The cell reselection delay to an already detected lower priority cell for UE fulfilling low mobility relaxed measurements is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to a lower priority cell for UE fulfilling low mobility relaxed measurements shall be less than 17 s.

The cell reselection delay to an already detected higher priority cell for UE fulfilling low mobility relaxed measurements is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected higher priority cell for UE fulfilling low mobility relaxed measurements shall be less than 17 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a known lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Tevaluate, NR_ interSee Table 4.2.2.10.2-1 in clause 4.2.2.10.2

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 16.64 s, allow 17 s for the cell re-selection delay to an already detected lower priority cell and 16.64 s for the cell re-selection delay to an already detected higher priority cell, which we allow 17 s for UE fulfilling low mobility relaxed measurements in the test case.

## A.14.1.10Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion

## A.14.1.10.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements specified in clause 4.2C.2.8, for UEs that support Relaxed cell reselection on GSO feature, as defined in clause 5.4 in 38.306 [14], and fulfilling not-at-cell edge relaxed measurement criterion.

## A.14.1.10.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.14.1.10.2-1, A.14.1.10.2-2 and A.14.1.10.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

As specified in the Test Purpose, the UE is configured with the relaxed measurement criterion for UE not-at-cell edge as defined in clause 5.2.4.9.2 in TS 38.304 [1]. So, Cell 2 and Cell 1configures the UE as follows:

cellEdgeEvaluation TS 38.331 [2] criterion is configured according to the parameters listed in table A.14.1.9.2-3;

lowMobilityEvalutation TS 38.331 [2] criterion is not configured;

combineRelaxedMeasCondition TS 38.331 [2] is not configured;

Table A.14.1.10.2-1: Supported test configurations

Table A.14.1.10.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case for UE fulfilling not-at-cell edge criterion

Table A.14.1.10.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN for UE fulfilling not-at-cell edge criterion

## A.14.1.10.3Test Requirements

The cell reselection delay to an already detected lower priority cell for UE fulfilling not-at-cell edge relaxed measurements is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected lower priority cell for UE fulfilling not-at-cell edge relaxed measurements shall be less than 17 s.

The cell reselection delay to an already detected higher priority cell for UE fulfilling not-at-cell-edge relaxed measurements is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected higher priority cell for UE fulfilling not-at-cell-edge relaxed measurements shall be less than 17 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Tevaluate, NR_ interSee Table 4.2.2.10.3-1 in clause 4.2.2.10

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 16.64 s, allow 17 s for the cell re-selection delay to an already detected lower priority cell and 16.64 s for the cell re-selection delay to an already higher priority cell, which we allow 17 s for UE fulfilling not-at-cell edge relaxed measurements in the test case.

## A.14.1.11Cell reselection to FR1 inter-RAT E-UTRAN cells with TN carrier

## A.14.1.11.1Test purpose and Environment

This test is to verify the requirement for the NR NTN to E-UTRAN TN inter-RAT cell reselection requirements specified in clause 4.2C.2.11 when the E-UTRAN cell is of higher priority.

## A.14.1.11.2Test parameters

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A.14.1.11.2-1, A.14.1.11.2-2, A.14.1.11.2-3 and A.14.1.11.2-4. The test consists of two successive time periods, with time duration of T1 and T2, respectively. NR Cell 1 is already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of higher priority than Cell 1.

A.14.1.11.2-1: Supported test configurations

Table A.14.1.11.2-2: General test parameters for NR to E-UTRAN cell re-selection test case

Table A.14.1.11.2-3: Cell specific test parameters for NR Cell 1

Table A.14.1.11.2-4: Cell specific test parameters for E-UTRA Cell 2

## A.14.1.11.3Test requirements

The cell reselection delay to a higher priority E-UTRAN cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, E-UTRAN + TSI-E-UTRA,

Where:

Thigher_priority_searchSee clause 4.2C.2.9

Tevaluate, NR_ interSee clause 4.2C.2.11

TSI-E-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority E-UTRAN cell.

## A.14.1.12Cell re-selection to FR1 inter-frequency NR case with TN carrier

## A.14.1.12.1Test purpose and Environment

This test is to verify the requirement for the inter frequency NR NTN to TN cell re-selection requirements specified in clause 4.2C.2.10.

## A.14.1.12.2Test parameters

The test scenario comprises of 2 cells on 2 different NR carriers, including NR NTN cell 1 on RF channel 1 and NR TN cell 2 on RF channel 2, respectively as given in tables A.14.1.12.2-1, A.14.1.12.2-2 and A.14.1.12.3-3. The test consists of two successive time periods, with time duration of T1 and T2, respectively. Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.14.1.12.2-1: Supported test configurations

TableA.14.1.12.2-2: General test parameters for inter frequency NR cell re-selection test case

Table A.14.1.12.3-3: Cell specific test parameters for inter frequency NR cell re-selection test case

## A.14.1.12.3Test requirements

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter_TN + TSI-NR

Where:

Thigher_priority_searchSee clause 4.2C.2.9

Tevaluate, NR_ inter_TNSee clause 4.2C.2.10

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority

## A.14.1.13Cell reselection to FR1 intra-frequency NR case for UE operating on a cell with less than 5 MHz BW

## A.14.1.13.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.3 for UE capable of operating on a cell with less than 5 MHz BW.

## A.14.1.13.2Test Parameters

The test scenario comprises of 2 cells on 1 NR carrier configured each in a different satellite as given in tables A.14.1.13.2-1, A.14.1.13.2-2 and A.14.1.13.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.14.1.13.2-1: Supported test configurations

Table A.14.1.13.2-2: General test parameters for intra frequency NR cell re-selection test case

Table A.14.1.13.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case

## A.14.1.13.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than:

## 34 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.13.2-2); or

## 66 s if Kmulti_SMTC is equal to 2.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than:

## 8 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.13.2-2); or

## 14.5 s if Kmulti_SMTC is equal to 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Kmulti_SMTC *Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Kmulti_SMTC *Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_Intra + 40ms See Table 4.2C.2.3-1 in clause 4.2C.2.3

Tevaluate, NR_ intraSee Table 4.2C.2.3-1 in clause 4.2C.2.3

Kmulti_SMTC  is described in clause 4.2C.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1320 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 20 ms period and 80 ms period, respectively.

If Kmulti_SMTC = 1, Kmulti_SMTC *Tevaluate, NR_Intra + TSI-NR = 7.68 s; allow 8 s. And Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 33.36 s, allow 34 s.

If K_multi_SMTC = 2, Kmulti_SMTC *Tevaluate, NR_Intra + TSI-NR = 14.08 s; allow 14.5 s. And Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 65.4 s, allow 66 s.

## A.14.2RRC_CONNECTED state mobility

## A.14.2.1Handover

## A.14.2.1.1Intra-frequency SAN Handover from FR1 to FR1

## A.14.2.1.1.1Test Purpose and Environment

This test is to verify the requirement for Intra-frequency SAN Handover from FR1 to FR1 specified in clause 6.1C.1.

## A.14.2.1.1.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2.1.1.2-1, A.14.2.1.1.2-2, and A.14.2.1.1.2-3. Both handover delay and interruption length are tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure intra-frequency neighbour cell with Event A3 report.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The start of T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.14.2.1.1.2-1: Supported test configurations

Table A.14.2.1.1.2-2: General test parameters Intra-frequency SAN handover from FR1 to FR1

Table A.14.2.1.1.2-3: Cell specific test parameters for Intra frequency SAN handover test case

## A.14.2.1.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2]. Tinterrupt is defined in clause 6.1C.1.2.2.

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin ms

Here: Tsearch = 0; TIU = 20 ms; Tprocessing = 20 ms; T∆ = 20 ms; Tmargin = 2 ms.

This gives a total of 72 ms.

## A.14.2.1.2Inter-frequency SAN Handover from FR1 to FR1

## A.14.2.1.2.1Test Purpose and Environment

This test is to verify the requirement for Inter-frequency SAN Handover from FR1 to FR1 specified in clause 6.1C.1.

## A.14.2.1.2.2Test Parameters

The test scenario comprises of 2 NR FDD carriers and one cell on each carrier as given in table A.14.2.1.2.2-1, A.14.2.1.2.2-2 and A.14.2.1.2.2-3. Both handover delay and interruption length are tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure inter frequency neighbour cell with Event A3 report and Gap Pattern 0 is configured in the test case.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The start of T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.14.2.1.2.2-1: Supported test configurations

Table A.14.2.1.2.2-2: General test parameters Inter-frequency SAN handover from FR1 to FR1

Table A.14.2.1.2.2-3: Cell specific test parameters for Inter frequency SAN handover test case

## A.14.2.1.2.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2]. Tinterrupt is defined in clause 6.1C.1.2.2.

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin ms

Here: Tsearch = 0; TIU = 20 ms; Tprocessing = 20 ms; T∆ = 20 ms; Tmargin = 2 ms.

This gives a total of 72 ms.

## A.14.2.1.3Intra-frequency SAN time-based conditional Handover from FR1 to FR1

## A.14.2.1.3.1Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover from FR1 to FR1 specified in clause 6.1C.2.

## A.14.2.1.3.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2.1.3.2-1, and A.14.2.1.3.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. Immediately before the start of T1, the UE is configured to measure intra-frequency neighbour cell with a time-based handover trigger to Cell 2 with Event CondEvent T1 shall be sent to UE.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and time condition event CondEvent T1 is fulfilled.

Table A.14.2.1.3.2-1: Supported test configurations

Table A.14.2.1.3.2-2: General test parameters for Intra-frequency SAN time-based conditional handover from FR1 to FR1

Table A.14.2.1.3.2-3: Cell specific test parameters for Intra-frequency SAN time-based conditional handover from FR1 to FR1

## A.14.2.1.3.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 872 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay is defined in clause 6.1C.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

Tmeasure = 600 + 200 ms; Tinterrupt = 62 ms; TCHO_execution = 10 ms.

This gives a total of 872 ms.

## A.14.2.1.4Inter-frequency SAN time-based conditional Handover from FR1 to FR1

## A.14.2.1.4.1Test Purpose and Environment

This test is to verify the requirement for inter -frequency SAN time-based conditional handover from FR1 to FR1 specified in clause 6.1C.2.

## A.14.2.1.4.2Test Parameters

The test scenario comprises of 2 NR FDD carrier and one cell on each carrier as given in table A.14.2.1.4.2-1, and A.14.2.1.4.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. Immediately before the start of T1, the UE is configured to measure inter-frequency neighbour cell with Gap pattern ID gp0 and time-based handover trigger to Cell 2 with Event CondEvent T1.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and after 1000 ms of T2, time condition event CondEvent T1 is fulfilled.

Table A.14.2.1.4.2-1: Supported test configurations

Table A.14.2.1.4.2-2: General test parameters for Inter-frequency SAN time-based conditional handover from FR1 to FR1

Table A.14.2.1.4.2-3: Cell specific test parameters for Inter-frequency SAN time-based conditional handover from FR1 to FR1

## A.14.2.1.4.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 later than 1000 ms and less than 1072 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay is defined in clause 6.1C.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

Tmeasure = max(600 + 200, 1000) ms; Tinterrupt = 62 ms; TCHO_execution = 10 ms.

This gives a total of 1072 ms.

## A.14.2.1.5Intra-frequency SAN distance-based conditional Handover from FR1 to FR1

## A.14.2.1.5.1Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN distance-based conditional handover from FR1 to FR1 specified in clause 6.1C.2.

## A.14.2.1.5.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2.1.5.2-1, and A.14.2.1.5.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure intra-frequency neighbour cell. The RRC message implying distance-based handover to Cell 2 with Event D1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and location condition event condEventD1-r17 is fulfilled.

Table A.14.2.1.5.2-1: Supported test configurations

Table A.14.2.1.5.2-2: General test parameters for Intra-frequency SAN distance-based conditional handover from FR1 to FR1

Table A.14.2.1.5.2-3: Cell specific test parameters for Intra-frequency SAN distance-based conditional handover from FR1 to FR1

## A.14.2.1.5.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 872 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay is defined in clause 6.1C.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

UE moving speed, v = (108km/h*1000/3600) = 30m/s.

At start of T2,

distance to source cell reference location is 30 m/s * 12 s – (-700)m = 1060m, and D1-1 = 1000m

distance to target cell reference location is 30 m/s * 12 s – 1300m = -940m, and D1-2 = 1000m

i.e. D1-1 and D1-2 conditions are fulfilled at start of T2 with >=50m location margin.

Tmeasure = max(600 + 200 ms, 0) = 800 ms;

Tinterrupt = 62 ms; TCHO_execution = 10 ms.

This gives a total of 800 ms + 62 ms + 10 ms = 872 ms.

## A.14.2.1.6Inter-frequency SAN distance-based conditional Handover from FR1 to FR1

## A.14.2.1.6.1Test Purpose and Environment

This test is to verify the requirement for inter -frequency SAN distance-based conditional handover from FR1 to FR1 specified in clause 6.1C.2.

## A.14.2.1.6.2Test Parameters

The test scenario comprises of 2 NR FDD carrier and one cell on each carrier as given in table A.14.2.1.6.2-1, and A.14.2.1.6.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure inter-frequency neighbour cell and Gap pattern ID gp0. The RRC message implying distance-based handover to Cell 2 with Event D1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and after 11670 ms of T2, location condition event condEventD1-r17 is fulfilled.

Table A.14.2.1.6.2-1: Supported test configurations

Table A.14.2.1.6.2-2: General test parameters for Inter -frequency SAN distance-based conditional handover from FR1 to FR1

Table A.14.2.1.6.2-3: Cell specific test parameters for Inter-frequency SAN distance-based conditional handover from FR1 to FR1

## A.14.2.1.6.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 later than 11670ms and less than 11742 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay is defined in clause 6.1C.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

UE moving speed, v = (108km/h*1000/3600) = 30m/s.

At 11670 ms after start of T2,

distance to source cell reference location is 30 m/s * 11.67 s – (-700)m = 1050m, and D1-1 = 1000m

distance to target cell reference location is 30 m/s * 11.67 s – 1300m = -950m, and D1-2 = 1000m

i.e. D1-1 and D1-2 conditions are fulfilled at T2 + 11670 ms with >=50m location margin.

Tmeasure = max(600 + 200 ms, 11670 ms) = 11670 ms;

Tinterrupt = 62 ms; TCHO_execution = 10 ms.

This gives a total of 11670ms + 62ms + 10ms = 11742 ms.

## A.14.2.1.7Intra-frequency intra-satellite Handover from FR2-NTN to FR2-NTN

## A.14.2.1.7.1Test Purpose and Environment

This test is to verify the requirement for intra-frequency intra-satellite handover from FR2-NTN to FR2-NTN specified in clause 6.1C.3.

## A.14.2.1.7.2Test Parameters

The test scenario comprises of one NR FDD carrier and 2 cells as given in table A.14.2.1.7.2-1, A.14.2.1.7.2-2, and A.14.2.1.7.2-3. Both handover delay and interruption length are tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure intra-frequency neighbour cell with Event A3 report. Starting T2, Cell 2 becomes detectable and offset better than Cell 1. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The start of T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.14.2.1.7.2-1: Supported test configurations

Table A.14.2.1.7.2-2: General test parameters Intra-frequency intra-satellite handover from FR2-NTN to FR2-NTN

Table A.14.2.1.7.2-3: Cell specific test parameters for intra-frequency intra-satellite handover from FR2-NTN to FR2-NTN

## A.14.2.1.7.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 no later than 72 ms from the beginning of T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2]. Tinterrupt is defined in clause 6.1C.1.3.2.

Tinterrupt_inter_sat = Tsearch + TIU + Tprocessing  + Tsat_beam + T∆ + Tmargin ms

Here: Tsearch = 0; TIU = 20 ms; Tprocessing = 20 ms; Tsat_beam = 0; T∆ = 20 ms; Tmargin = 2 ms.

This gives a total of 72 ms.

## A.14.2.1.8Intra-frequency SAN Handover from FR1 to FR1

## A.14.2.1.8.1Test Purpose and Environment

This test is to verify the requirement for Intra-frequency SAN RACH-less Handover from FR1 to FR1 specified in clause 6.1C.1.1.

## A.14.2.1.8.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2.1.8.2-1, A.14.2.1.8.2-2, and A.14.2.1.8.2-3. Both handover delay and interruption length are tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure intra-frequency neighbour cell with Event A3 report.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The start of T3 is defined as the end of the last TTI containing the RRC message implying handover. During T3, Cell 2 continuously schedules PUSCH for the UE.

Table A.14.2.1.8.2-1: Supported test configurations

Table A.14.2.1.8.2-2: General test parameters Intra-frequency SAN handover from FR1 to FR1

Table A.14.2.1.8.2-3: Cell specific test parameters for Intra frequency SAN handover test case

## A.14.2.1.8.3Test Requirements

The UE shall start to transmit the PUSCH to Cell 2 less than 52 + TIU ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2]. Tinterrupt is defined in clause 6.1C.1.2.2.2.

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin ms

Here: Tsearch = 0; TIU is the interruption uncertainty in acquiring the first UL transmission resource for PUSCH, which is scheduled by Cell 2 at the fist DL slot not earlier than 52 ms after the beginning of T3; Tprocessing = 20 ms; T∆ = 20 ms; Tmargin = 2 ms.

This gives a total of 52 + TIU ms.

## A.14.2.1.9Intra-frequency inter-satellite handover from FR2-NTN to FR2-NTN

## A.14.2.1.9.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NTN – NR FR2-NTN intra-frequency handover requirements specified in clause 6.1C.1.3.

## A.14.2.1.9.2Test Parameters

The test consists two sub-tests. Sub-test 1 is applicable for UE indicating ‘electronic’ via ntn-VSAT-AntennaType-r18, and sub-test 2 is applicable for UE indicating ‘mechanical’ via ntn-VSAT-AntennaType-r18. The test configurations are same for the two sub-tests unless specified otherwise.

Supported test configurations are shown in table A.14.2.1.9.2-1. Both handover delay and interruption length are tested by using the parameters in table A.14.2.1.9.2-2, and A.14.2.1.9.2-3.

The test scenario comprises of one carrier and two cells on the carrier. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network to handover from Cell 1 to Cell 2. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.14.2.1.9.2-1: Supported test configurations

Table A.14.2.1.9.2-2: General test parameters

Table A.14.2.1.9.2-3: Cell specific test parameters for NR FR2-FR2 Intra frequency handover test case

## A.14.2.1.9.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than X ms from the beginning of time period T2.

X = 152 ms for sub-test 1, and

X = TBD ms for sub-test 2, and

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 142 ms in sub-test 1 and TBD in sub-test 2. Tinterrupt is defined in clause 6.1C.1.3.2.

This gives a total of 152 ms sub-test 1 and TBD in sub-test 2.

## A.14.2.1.10Intra-frequency SAN Handover from FR1 to FR1 for UE operating on a cell with less than 5 MHz BWA.14.2.1.10.1Test Purpose and Environment

This test is to verify the requirement for NR FR1 NTN- NR FR1 NTN intra-frequency SAN handover requirements for unknown target cell operating with 12 PRB SSB bandwidth specified in clause 6.1C.1.

## A.14.2.1.10.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2.1.10.2-1, A.14.2.1.10.2-2, and A.14.X.1.1.2-3. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1, UE receives a RRC handover command from the network. The start of T2 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.14.2.1.10.2-1: Supported test configurations

Table A.14.2.1.10.2-2: General test parameters Intra-frequency SAN handover from FR1 to FR1

Table A.14.2.1.10.2-3: Cell specific test parameters for Intra frequency SAN handover test case

## A.14.2.1.10.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 132 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2]. Tinterrupt is defined in clause 6.1C.1.2.2.

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin ms

Here: Tsearch = 20ms; TIU = 20 ms; Tprocessing = 20 ms; T∆ = 60 ms; Tmargin = 2 ms.

This gives a total of 132 ms.

## A.14.2.1.11Intra-frequency SAN time-based conditional Handover from FR1 to FR1 for UE operating on a cell with less than 5 MHz BW

## A.14.2.11.1Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover from FR1 to FR1 specified in clause 6.1C.2.2.

## A.14.2.11.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2. 11.2-1, and A.14.2.1.11.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. Immediately before the start of T1, the UE is configured to measure intra-frequency neighbour cell with a time-based handover trigger to Cell 2 with Event CondEvent T1 shall be sent to UE.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and time condition event CondEvent T1 is fulfilled.

Table A.14.2. 11.2-1: Supported test configurations

Table A.14.2.1.11.2-2: General test parameters for Intra-frequency SAN time-based conditional handover from FR1 to FR1

Table A.14.2. 11.2-3: Cell specific test parameters for Intra-frequency SAN time-based conditional handover from FR1 to FR1

## A.14.2.11.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 892 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay is defined in clause 6.1C.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

Tmeasure = 600 + 200 ms; Tinterrupt = 82 ms; TCHO_execution = 10 ms.

This gives a total of 892 ms.

## A.14.2.2RRC Connection Mobility Control

## A.14.2.2.1SA: RRC Re-establishment for SAN

## A.14.2.2.1.1Intra-frequency RRC Re-establishment in FR1

A.14.2.2.1.1.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR1 with known target cell is within the specified limits. These tests will verify the requirements in clause 6.2C.1.

The test parameters are given in table A.14.2.2.1.1.1-1, table A.14.2.2.1.1.1-2 and table A.14.2.2.1.1.1-3  below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.2.2.1.1.1-1: Supported test configurations

Table A.14.2.2.1.1.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1

Table A.14.2.2.1.1.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1

A.14.2.2.1.1.2Test Requirements

The RRC re-establishment delay is defined as the time from the moment UE declares RLF, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to a known NR intra frequency cell shall be less than 1.6 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 1

Tidentify_intra_NR = 200 ms

TSI = 1280 ms, provided that SIB1 and SIB19 are scheduled with 20 ms period; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure, allow 1840 ms (240 ms + 1.6 s) from the beginning of T2 in the test case.

This gives a total of 1545 ms, allow 1.6 s in the test case.

## A.14.2.2.1.2Inter-frequency RRC Re-establishment in FR1

A.14.2.2.1.2.1Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR1 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2C.1.

The test parameters are given in table A.14.2.2.1.2.1-1, table A.14.2.2.1.2.1-2 and table A.14.2.2.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.2.2.1.2.1-1: Supported test configurations

Table A.14.2.2.1.2.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1

Table A.14.2.2.1.2.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1

A.14.2.2.1.2.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less than 3 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 2

Tidentify_intra_NR = 800 ms

Tidentify_inter_NR = 800 ms

TSI = 1280 ms, provided that SIB1 and SIB19 are scheduled with 20 ms period; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2945 ms, allow 3 s in the test case.

## A.14.2.2.1.3Inter-frequency RRC Re-establishment in FR1 with 160ms SSB periodicity

A.14.2.2.1.3.1Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR1 without known target cell is within the specified limits, where the SSB periodicity of the target cell is 160ms. The test will verify the requirements in clause 6.2C.1.

The test parameters are given in table A.14.2.2.1.3.1-1, table A.14.2.2.1.3.1-2 and table A.14.2.2.1.3.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.2.2.1.3.1-1: Supported test configurations

Table A.14.2.2.1.3.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1

Table A.14.2.2.1.3.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1

A.14.2.2.1.3.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less than 6 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 2

Tidentify_intra_NR = 800 ms

Tidentify_inter_NR = 3520 ms

TSI = 1280 ms, provided that SIB1 and SIB19 are scheduled with 160 ms period; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 5665 ms, allow 6 s in the test case.

## A.14.2.2.2Random Access

## A.14.2.2.2.14-step RA type contention based random access test in FR1 for NR standalone

## A.14.2.2.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2C.2.2 and clause 7.1C.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.14.2.2.2.1.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.14.2.2.2.1.1-2.

Table A.14.2.2.2.1.1-1: Supported test configurations for contention based random access test for satellite access

Table A.14.2.2.2.1.1-2: General test parameters for contention based random access test for satellite access

## A.14.2.2.2.1.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.14.2.2.2.1.2.1Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2C.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

A.14.2.2.2.1.2.2Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

A.14.2.2.2.1.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

A.14.2.2.2.1.2.4Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2C.2.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

A.14.2.2.2.1.2.5Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2C.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.14.2.2.2.1.2.6Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2C.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.14.2.2.2.1.2.7Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2C.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.14.2.2.2.24-step RA type non-contention based random access test in FR1 for NR standalone

## A.14.2.2.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2C.2.2 and clause 7.1C.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.14.2.2.2.2.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.14.2.2.2.2.1-2 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.14.2.2.2.2.1-1: Supported test configurations for non-contention based random access test for satellite access

Table A.14.2.2.2.2.1-2: General test parameters for non-contention based random access test satellite access

## A.14.2.2.2.2.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.14.2.2.2.2.2.1SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2C.2.2.2.1 for SSB-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

A.14.2.2.2.2.2.2CSI-RS-based Random Access Preamble Transmission

In Test-2, to test the UE behavior specified in clause 6.2C.2.2.2.1 for CSI-RS-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

A.14.2.2.2.2.2.3Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

A.14.2.2.2.2.2.4No Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

## A.14.2.2.3RRC Connection Release with Redirection

## A.14.2.2.3.1Redirection from NR in FR1 to NR in FR1

## A.14.2.2.3.1.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2C.3.2.1.

## A.14.2.2.3.1.2Test Parameters

Supported test configurations are shown in table A.14.2.2.3.1.2-1. The time delay is tested by using the parameters in table A.14.2.2.3.1.2-2, and A.14.2.2.3.1.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2. Cell 1 and Cell 2 belong to different tracking areas.

Table A.14.2.2.3.1.2-1: Redirection from NR to NR test configurations

Table A.14.2.2.3.1.2-2: General test parameters for Redirection from NR to NR test case

Table A.14.2.2.3.1.2-3: Cell specific test parameters for Redirection from NR to NR test case

## A.14.2.2.3.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2240 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

Where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR = 680 ms in the test.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH = 170 ms in the test.

This gives a total of 2240 ms.

## A.14.2.2.4RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1

## A.14.2.2.4.1Test Purpose and Environment

This test is to verify the requirement for RACH-based hard satellite switching with re-synchronization from SAN FR1 to SAN FR1 specified in clause 6.1C.3.

## A.14.2.2.4.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in table A.14.2.2.4.2-1, A.14.2.2.4.2-2, A.14.2.2.4.2-3 and A.14.2.2.4.2-4. Both satellite switching delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.14.2.2.4.2-3.

At the start of time duration T2, Cell 2 becomes detectable and t-service-r17 of Cell 1 is fulfilled.

Table A.14.2.2.4.2-1: Supported test configurations

Table A.14.2.2.4.2-2: General test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1

Table A.14.2.2.4.2-3: Target Satellite configuration pattern for hard satellite switching scenario

Table A.14.2.2.4.2-4: Cell specific test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 test case

## A.14.2.2.4.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 52.5 ms from the beginning of time period T2.

The rate of correct satellite switch observed during repeated tests shall be at least 90 %.

NOTE:The hard satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tinterrupt, where:

Tinterrupt is defined in clause 6.1C.3.2.2.

Dswitch_unchangedPCI = Tinterrupt = Tsearch + Tprocessing  + T∆ + Tmargin ms

Here: Tsearch = Tfirst_SSB = 0.5ms; Tprocessing = 10ms; T∆ = 20ms; Tmargin = 2ms.

Besides, interruption uncertainty TIU = 20ms in acquiring the first PRACH transmission resource is needed.

This gives a total of 52.5 ms.

## A.14.2.2.5RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1

## A.14.2.2.5.1Test Purpose and Environment

This test is to verify the requirement for RACH-less soft satellite switching with re-synchronization from SAN FR1 to SAN FR1 specified in clause 6.1C.3.

## A.14.2.2.5.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in tables A.14.2.2.5.2-1, A.14.2.2.5.2-2, A.14.2.2.5.2-3 and A.14.2.2.5.2-4. Satellite switching delay is tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.14.2.2.5.2-3. The configured grant PUSCH transmission in the Cell 2 is configured in the RRC message from Cell 1.

At the start of time duration T2, Cell 2 becomes detectable and t-ServiceStart-r18 is fulfilled.

At the start of time duration T3, t-service-r17 of Cell 1 is fulfilled.

Table A.14.2.2.5.2-1: Supported test configurations

Table A.14.2.2.5.2-2: General test parameters for RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1

Table A.14.2.2.5.2-3: Target Satellite configuration pattern for soft satellite switching scenario

Table A.14.2.2.5.2-4: Cell specific test parameters for Inter frequency SAN handover test case

## A.14.2.2.5.3Test Requirements

The UE shall start to transmit the PUSCH to Cell 2 less than 130 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tsoft_switch, where:

Tsoft_switch = max(t-service-t-seviceStart, Tsearch + T∆ + Tmargin) + TIU + Tprocessing  ms

Here: t-service-t-seviceStart= 100ms; Tsearch = 10.5ms; T∆ = 20ms; Tmargin = 2ms, Tprocessing = 10ms.

Besides, interruption uncertainty TIU = 20ms in acquiring the first configured grant based PUSCH transmission resource is needed.

This gives a total of 130 ms.

## A.14.2.2.6RACH-based hard Satellite switching with re-synchronization from FR1 to FR1 for less than 5MHz with NTN

## A.14.2.2.6.1Test Purpose and Environment

This test is to verify the requirement for RACH-based hard satellite switching with re-synchronization from SAN FR1 to SAN FR1 for unknown target cell operating with 12 PRB SSB bandwidth specified in clause 6.1C.3.

## A.14.2.2.6.2Test Parameters

Supported test configurations are shown in table A.14.2.2.6.2-1. General test parameters as specified in table A.14.2.2.6.2-2 apply except those specified in table A.14.2.2.4.2-2. Target Satellite configuration pattern specified in table A.14.2.2.4.2-3 shall apply. Cell specific test parameters as specified in table A.14.2.2.6.2-4 apply except those specified in table A.14.2.2.4.2-4.

The test procedure specified in clause A.14.2.2.4.2 applies to this test. The Cell 2 is the unknown target cell operating with 12 PRB SSB bandwidth.

Table A.14.2.2.6.2-1: Supported test configurations

Table A.14.2.2.6.2-2: General test parameters for RACH-based hard Satellite switching with re-synchronization from FR1 to FR1

Table A.14.2.2.6.2-3: Cell specific test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 test case

## A.14.2.2.6.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 52.5 ms from the beginning of time period T2.

The rate of correct satellite switch observed during repeated tests shall be at least 90 %.

NOTE:The hard satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tinterrupt, where:

Tinterrupt is defined in clause 6.1C.3.2.2.

Dswitch_unchangedPCI = Tinterrupt = Tsearch + Tprocessing + T∆ + Tmargin ms

Here: Tsearch = Tfirst_SSB = 0.5ms; Tprocessing = 10ms; T∆ = 20ms; Tmargin = 2ms.

This gives a total of 52.5 ms.

## A.14.2.2.7RACH-based Hard Satellite switching with re-synchronization from FR2 to FR2

## A.14.2.2.7.1Test Purpose and Environment

This test is to verify the requirements for RACH-based hard satellite switching with re-synchronization from SAN FR2 to SAN FR2 specified in clause 6.1C.3.

## A.14.2.2.7.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in table A.14.2.2.7.2-1, A.14.2.2.7.2-2, A.14.2.2.7.2-3 and A.14.2.2.7.2-4. Both satellite switching delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.14.2.2.7.2-3.

At the start of time duration T2, Cell 2 becomes detectable and t-service-r17 of Cell 1 is fulfilled.

Table A.14.2.2.7.2-1: Supported test configurations

Table A.14.2.2.7.2-2: General test parameters for RACH-based Hard Satellite switching with re-synchronization from FR2 to FR2

Table A.14.2.2.7.2-3: Target Satellite configuration pattern for hard satellite switching scenario

Table A.14.2.2.7.2-4: Cell specific test parameters for RACH-based Hard Satellite switching with re-synchronization from FR2 to FR2 test case

## A.14.2.2.7.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 112.5ms or (52.5+ 1000*Oangle / 22.5) ms from the beginning of time period T2.

The rate of correct satellite switch observed during repeated tests shall be at least 90 %.

NOTE:The hard satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tinterrupt, where:

Tinterrupt is defined in clause 6.1C.3.3.2.

Dswitch_unchangedPCI = Tinterrupt = Tsearch + Tprocessing  + T∆ +Tsat_beam+ Tmargin ms

Here: Tsearch = Tfirst_SSB = 0.5ms; Tprocessing = 10ms; T∆ = 20ms; Tmargin = 2ms,  Tsat_beam =60ms or Oangle / 22.5 s

Besides, interruption uncertainty TIU = 20ms in acquiring the first PRACH transmission resource is needed.

This gives a total of 112.5ms or (52.5+ 1000*Oangle / 22.5) ms.

## A.14.2.2.8RACH-less Soft Satellite switching with re-synchronization from FR2 to FR2

## A.14.2.2.8.1Test Purpose and Environment

This test is to verify the requirements for RACH-less soft satellite switching with re-synchronization from SAN FR2 to SAN FR2 specified in clause 6.1C.3.

## A.14.2.2.8.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in tables A.14.2.2.8.2-1, A.14.2.2.8.2-2, A.14.2.2.8.2-3 and A.14.2.2.8.2-4. Satellite switching delay is tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.14.2.2.8.2-3. The configured grant PUSCH transmission in the Cell 2 is configured in the RRC message from Cell 1.

At the start of time duration T2, Cell 2 becomes detectable and t-ServiceStart-r18 is fulfilled.

At the start of time duration T3, t-service-r17 of Cell 1 is fulfilled.

Table A.14.2.2.8.2-1: Supported test configurations

Table A.14.2.2.8.2-2: General test parameters for RACH-less Soft Satellite switching with re-synchronization with FR2 numerology

Table A.14.2.2.8.2-3: Target Satellite configuration pattern for soft satellite switching scenario

Table A.14.2.2.8.2-4: Cell specific test parameters for Inter frequency SAN handover test case

## A.14.2.2.8.3Test Requirements

The UE shall start to transmit the PUSCH to Cell 2 less than 190 ms or (130+1000* Oangle / 22.5) ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tsoft_switch, where:

Tsoft_switch = max(t-service-t-seviceStart, Tsearch + T∆+Tsat_beam + Tmargin) + TIU + Tprocessing  ms

Here: t-service-t-seviceStart= 100ms; Tsearch = 10.5ms; T∆ = 20ms; Tmargin = 2ms, Tprocessing = 10ms, Tsat_beam =60ms or Oangle / 22.5 s

Besides, interruption uncertainty TIU = 20ms in acquiring the first configured grant based PUSCH transmission resource is needed.

This gives a total of 190 ms or (130+1000* Oangle / 22.5) ms.

## A.14.2.3Intra-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1

## A.14.2.3.1Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover without L3 measurement criteria from FR1 to FR1 specified in clause 6.1C.2.3.

## A.14.2.3.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2.3.2-1, and A.14.2.3.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure intra-frequency neighbour cell. The RRC message implying time-based handover to Cell 2 with Event CondEvent T1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and time condition event CondEvent T1 is fulfilled.

Table A.14.2.3.2-1: Supported test configurations

Table A.14.2.3.2-2: General test parameters for Intra-frequency SAN time-based conditional handover without L3 measurement criteria from FR1 to FR1

Table A.14.2.3.2-3: Cell specific test parameters for Intra-frequency SAN time-based conditional handover without L3 measurement criteria from FR1 to FR1

## A.14.2.3.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 92 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay is defined in clause 6.1C.2.3, can be expressed as:

DCHO = TRRC + TEvent_DU + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

Tinterrupt = 82 ms; TCHO_execution = 10 ms.

This gives a total of 92 ms.

## A.14.2.4Inter-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1

## A.14.2.4.1Test Purpose and Environment

This test is to verify the requirement for inter -frequency SAN time-based conditional handover without L3 measurement criteria from FR1 to FR1 specified in clause 6.1C.2.

## A.14.2.4.2Test Parameters

The test scenario comprises of 2 NR FDD carrier and one cell on each carrier as given in table A.14.2.4.2-1, and A.14.2.4.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure inter-frequency neighbour cell and Gap pattern ID gp0. The RRC message implying time-based handover to Cell 2 with Event CondEvent T1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and time condition event CondEvent T1 is fulfilled.

Table A.14.2.4.2-1: Supported test configurations

Table A.14.2.4.2-2: General test parameters for Inter-frequency SAN time-based conditional handover from FR1 to FR1

Table A.14.2.4.2-3: Cell specific test parameters for Inter-frequency SAN time-based conditional handover from FR1 to FR1

## A.14.2.4.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 132 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay is defined in clause 6.1C.2.3, can be expressed as:

DCHO = TRRC + TEvent_DU + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

Tinterrupt = 122 ms; TCHO_execution = 10 ms.

This gives a total of 132 ms.

## A.14.3Timing for Satellite Access

## A.14.3.1UE transmit timing for Satellite Access

## A.14.3.1.1NR UE Transmit Timing Test for FR1

## A.14.3.1.1.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the reference cell and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1C.2. Supported test configurations are shown in table A.14.3.1.1.1-1.

Table A.14.3.1.1.1-1: Supported test configurations for FR1 PCell

The test consists a single NR cell (PCell). Table A.14.3.1.1.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.14.3.1.1.1-3.

Table A.14.3.1.1.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.14.3.1.1.1-3: SRS Configuration for Timing Accuracy Test

## A.14.3.1.1.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1)Set up PCell according to parameters given in table A.14.3.1.1.1-2.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within   of the first detected path of DL SSB.NTA+NTA-offset+NTA,adjcommon+NTA,adjUE×Tc±(Te_NTN -TGNSS_margin)

a.The NTA_offset value (in Tc units) is 25600

b.The  value is derived from the higher-layer parameters TACommon, TACommonDrift, and TACommonDriftVariation.NTA,adjcommon

c.The  value is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters. For Config 3,  is calculated based on the generated UL channel with time varying Doppler and delay shifts.NTA,adjUENTA,adjUE

d.The  values depend on the DL and UL SCS for which the test is being run and are given in table 7.1C.2-1Te_NTN

e.The counts for the margin for the GNSS position definition error considered in the core requirement, which needs to be substracted for the test requirement, due to the usage of AT commands or any other pre-configured means in the test. TGNSS_margin TGNSS_margin=327,68×Tc

3)If the NTN parameters are configured as GSO scenario, the test system shall adjust the timing of the DL path by values given in table A.14.3.1.1.2-1. If the NTN parameters are configured as NGSO scenario, the test system shall adjust the timing of the DL path according to the serving-satellite-ephemeris-related higher-layers parameters.

Table A.14.3.1.1.2-1: Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1C.2 Table 7.1C.2.1-1 until the UE transmit timing offset is within  respective to the first detected path (in time) of DL SSB. Skip this step for test 2 with DRX configured.NTA+NTA-offset+NTA,adjcommon+NTA,adjUE×Tc±(Te_NTN -TGNSS_margin)

5)The test system shall verify that the UE transmit timing offset stays within  of the first detected path of DL SSB. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.NTA+NTA-offset+NTA,adjcommon+NTA,adjUE×Tc±(Te_NTN -TGNSS_margin)

## A.14.3.1.2NR UE Transmit Timing Test for FR2-NTN

## A.14.3.1.2.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the reference cell and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1C.2. Supported test configurations are shown in table A.14.3.1.2.1-1.

Table A.14.3.1.2.1-1: Supported test configurations for FR2-NTN PCell

The test consists a single NR cell (PCell). Table A.14.3.1.2.1-2 and A.14.3.1.2.1-2A defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.14.3.1.2.1-3.

Table A.14.3.1.2.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.14.3.1.2.1-2A: OTA related test parameters

Table A.14.3.1.2.1-3: SRS Configuration for Timing Accuracy Test

## A.14.3.1.2.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1)Set up PCell according to parameters given in table A.14.3.1.2.1-2.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within   of the first detected path of DL SSB.NTA+NTA-offset+NTA,adjcommon+NTA,adjUE×Tc±(Te_NTN -TGNSS_margin)

a.The NTA_offset value (in Tc units) is 0

b.The  value is derived from the higher-layer parameters TACommon, TACommonDrift, and TACommonDriftVariation.NTA,adjcommon

c.The  value is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters.NTA,adjUE

d.The  values depend on the DL and UL SCS for which the test is being run and are given in table 7.1C.2-2 and 7.1C.2-3 for test configuration 1, 2 and 3, and in table 7.1C.2-1 for test configuration 4 and 5.Te_NTN

e.The counts for the margin for the GNSS position definition error considered in the core requirement, which needs to be subtracted for the test requirement, due to the usage of AT commands or any pre-configured means in the test. TGNSS_margin TGNSS_margin=98.304×Tc

3)If the NTN parameters are configured as GSO scenario, the test system shall adjust the timing of the DL path by values given in table A.14.3.1.2.2-1. If the NTN parameters are configured as NGSO scenario, the test system shall adjust the timing of the DL path according to the serving-satellite-ephemeris-related higher-layers parameters.

Table A.14.3.1.2.2-1: Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1C.2 Table 7.1C.2.1-1 until the UE transmit timing offset is within  respective to the first detected path (in time) of DL SSB. Skip this step for test 2 with DRX configured.NTA+NTA-offset+NTA,adjcommon+NTA,adjUE×Tc±(Te_NTN -TGNSS_margin)

5)The test system shall verify that the UE transmit timing offset stays within  of the first detected path of DL SSB. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.NTA+NTA-offset+NTA,adjcommon+NTA,adjUE×Tc±(Te_NTN -TGNSS_margin)

## A.14.3.2Timing advance for satellite access

## A.14.3.2.1SA FR1 timing advance adjustment accuracy

## A.14.3.2.1.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3C.

## A.14.3.2.1.2Test Parameters

Supported test configurations are shown in table A.14.3.2.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.14.3.2.1.2-2, A.14.3.2.1.2-3 and A.14.3.2.1.2-4.

In all test cases, single cell served by SAN is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.14.3.2.1.2-4, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

The UE shall be provided with the valid information about the SAN serving cell before the test.During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.14.3.2.1.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause 7.3C.2.1, the UE adjusts its uplink timing at slot n+k+1+2µ for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.∙Koffset

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.14.3.2.1.2-1: Timing advance supported test configurations

Table A.14.3.2.1.2-2: General test parameters for timing advance

Table A.14.3.2.1.2-3: Cell specific test parameters for timing advance

Table A.14.3.2.1.2-4: Sounding Reference Symbol Configuration for timing advance

## A.14.3.2.1.3Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1+2µ slots after the reception of the timing advance command, where k=5.∙Koffset

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3C.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.14.3.2.3SA FR2-NTN timing advance adjustment accuracy

## A.14.3.2.3.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3C.

## A.14.3.2.3.2Test Parameters

Supported test configurations are shown in table A.14.3.2.3.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.14.3.2.3.2-2, A.14.3.2.3.2-3 and A.14.3.2.3.2-4.

In all test cases, single cell served by SAN is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.14.3.2.3.2-4, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

The UE shall be provided with the valid information about the SAN serving cell before the test. During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.14.3.2.3.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause 7.3C.2.1, the UE adjusts its uplink timing at slot n+k+1+2µ for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.∙Koffset

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.14.3.2.3.2-1: Timing advance supported test configurations

Table A.14.3.2.3.2-2: General test parameters for timing advance

Table A.14.3.2.3.2-3: Cell specific test parameters for timing advance

Table A.14.3.2.3.2-3A: OTA related test parameters

Table A.14.3.2.3.2-4: Sounding Reference Symbol Configuration for timing advance

## A.14.3.2.1.3Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1+2µ slots after the reception of the timing advance command, where k=11.∙Koffset

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3C.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.14.4Signalling characteristics

## A.14.4.1Radio link Monitoring

## A.14.4.1.1Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode

## A.14.4.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1C.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.14.4.1.1.1-1. The test parameters are given in tables A.14.4.1.1.1-2, A.14.4.1.1.1-3, and A.14.4.1.1.1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.1.1.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.4.1.1.1-1: Supported test configurations for FR1 PCell

Table A.14.4.1.1.1-2: General test parameters for FR1 out-of-sync testing in non-DRX mode

Table A.14.4.1.1.1-3: Cell specific test parameters for FR1 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode

Table A.14.4.1.1.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

Figure A.14.4.1.1.1-1: SNR variation for out-of-sync testing

## A.14.4.1.1.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.1.2Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode

## A.14.4.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1C.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.14.4.1.2.1-1. The test parameters are given in tables A.14.4.1.2.1-2, and A.14.4.1.2.1-3 below. There is one cell (Cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.1.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.4.1.2.1-1: Supported test configurations for FR1 PCell

Table A.14.4.1.2.1-2: General test parameters for FR1 in-sync testing in non-DRX mode

Table A.14.4.1.2.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

Figure A.14.4.1.2.1-1: SNR variation for in-sync testing

## A.14.4.1.2.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.1.3Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode

## A.14.4.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell when DRX is used. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1C.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.14.4.1.3.1-1. The test parameters are given in tables A.14.4.1.3.1-2, and A.14.4.1.3.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.1.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.4.1.3.1-1: Supported test configurations for FR1 PCell

Table A.14.4.1.3.1-2: General test parameters for FR1 out-of-sync testing in DRX mode

Table A.14.4.1.3.1-3: Cell specific test parameters for FR1 (Cell 1) for out-of-sync radio link monitoring tests in DRX mode

Figure A.14.4.1.3.1-1: SNR variation for out-of-sync testing

## A.14.4.1.3.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.1.4Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode

## A.14.4.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell when DRX is used. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1C.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.14.4.1.4.1-1. The test parameters are given in tables A.14.4.1.4.1-2, and A.14.4.1.4.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.1.4.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.4.1.4.1-1: Supported test configurations for FR1 PCell

Table A.14.4.1.4.1-2: General test parameters for FR1 in-sync testing in DRX mode

Table A.14.4.1.4.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in DRX mode

Table A.6.5.1C.4.1-4: Void

Table A.6.5.1C.4.1-5: Void

Figure A.14.4.1.4.1-1: SNR variation for in-sync testing.

## A.14.4.1.4.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.1.5Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode

## A.14.4.1.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the SAN PCell when no DRX is used. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1C.

The test parameters are given in tables A.14.4.1.5.1-1, A.14.4.1.5.1-2, A.14.4.1.5.1-3, and A.14.4.1.5.1-3A below. There is one cell, Cell 1 which is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.1.5.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting of 5 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 is configured as the BFD-RS.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.4.1.5.1-1: Supported test configurations for FR1 PCell

Table A.14.4.1.5.1-2: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in non-DRX mode

Table A.14.4.1.5.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.14.4.1.5.1-3A: Measurement gap configuration for FR1 CSI-RS out-of-sync radio link monitoring in non-DRX mode

Figure A.14.4.1.5.1-1: SNR variation for CSI-RS out-of-sync testing

## A.14.4.1.5.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 no later than time point C (D1 ms after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.1.6Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode

## A.14.4.1.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the SAN PCell when no DRX is used. This test will partly verify the FR1 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1C.

The test parameters are given in tables A.14.4.1.6.1-1, A.14.4.1.6.1-2, and A.14.4.1.6.1-3 below. There is one cells, Cell 1 which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.1.6.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled. In the test, SSB0 is configured as the BFD-RS.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.4.1.6.1-1: Supported test configurations for FR1 PCell

Table A.14.4.1.6.1-2: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

Table A.14.4.1.6.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in non-DRX mode

Figure A.14.4.1.6.1-1: SNR variation for CSI-RS in-sync testing

## A.14.4.1.6.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.1.7Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode

## A.14.4.1.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the SAN PCell when DRX is used. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1C.

The test parameters are given in tables A.14.4.1.7.1-1, A.14.4.1.7.1-2, and A.6.5.1.7C.1-3 below. There is one cell, Cell 1 is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.1.7.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test. In the test, SSB0 is configured as the BFD-RS.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.4.1.7.1-1: Supported test configurations for FR1 PCell

Table A.14.4.1.7.1-2: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in DRX mode

Table A.14.4.1.7.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in DRX mode

Figure A.14.4.1.7.1-1: SNR variation for CSI-RS out-of-sync testing

## A.14.4.1.7.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 (PCell) at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 (PCell) no later than time point C (D1 ms after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.1.8Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode

## A.14.4.1.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the SAN PCell when DRX is used. This test will partly verify the FR1 Pcell CSI-RS In-sync radio link monitoring requirements in clause 8.1C.

The test parameters are given in tables A.14.4.1.8.1-1, A.14.4.1.8.1-2, A.14.4.1.8.1-3 and A.14.4.1.8.1-3A below. There is one cells, Cell 1 which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.1.8.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 is configured as the BFD-RS.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.4.1.8.1-1: Supported test configurations for FR1 PSCell

Table A.14.4.1.8.1-2: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

Table A.14.4.1.8.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in non-DRX mode

Table A.6.5.1.8.1-3A: Measurement gap configuration for FR1 CSI-RS in-sync radio link monitoring in non-DRX mode

Figure A.14.4.1.8.1-1: SNR variation for CSI-RS in-sync testing

## A.14.4.1.8.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.1.9Radio Link Monitoring Out-of-sync Test for FR2 SAN PCell configured with SSB-based RLM RS in non-DRX mode

## A.14.4.1.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1C.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.14.4.1.9.1-1. The test parameters are given in tables A.14.4.1.9.1-2, A.14.4.1.9.1-3, and A.14.4.1.9.1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.1.9.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

The UE shall be provided with the valid information about the SAN serving each cell in the test before the test.

Table A.14.4.1.9.1-1: Supported test configurations for FR2 PCell

Table A.14.4.1.9.1-2: General test parameters for FR2 out-of-sync testing in non-DRX mode

Table A.14.4.1.9.1-3: Cell specific test parameters for FR2 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode

Table A.14.4.1.9.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

Figure A.14.4.1.9.1-1: SNR variation for out-of-sync testing

## A.14.4.1.9.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.1.10Radio Link Monitoring In-sync Test for FR2 SAN PCell configured with SSB-based RLM RS in non-DRX mode

## A.14.4.1.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1C.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.14.4.1.10.1-1. The test parameters are given in tables A.14.4.1.10.1-2, and A.14.4.1.10.1-3 below. There is one cell (Cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.1.10.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.4.1.10.1-1: Supported test configurations for FR2 PCell

Table A.14.4.1.10.1-2: General test parameters for FR2 in-sync testing in non-DRX mode

Table A.14.4.1.10.1-3: Cell specific test parameters for FR2 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

Figure A.14.4.1.10.1-1: SNR variation for in-sync testing

## A.14.4.1.10.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.1.11Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode

## A.14.4.1.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting support-3MHz-ChannelBW-r18 properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PCell operating on a 3 MHz channel bandwidth. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1C.

Supported test configurations are specified in table A.14.4.1.11.1-1. General test parameters as specified in table A.14.4.1.1.1-2 with config 1 apply except those specified in table A.14.4.1.11.1-2. Cell specific test parameters as specified in table A.14.4.1.1.1-3 apply except those specified in table A.14.4.1.11.1-3.

The test procedure specified in clause A.14.4.1.1.1 applies to this test.

Table A.14.4.1.11.1-1: Supported test configurations for FR1 PCell

Table A.14.4.1.11.1-2: General test parameters for FR1 OOS 15 PRB in non-DRX mode

Table A.14.4.1.11.1-3: Cell specific test parameters for FR1 PCell

## A.14.4.1.11.2Test Requirements

Test requirements specified in clause A.14.4.1.1.2 apply to this test.

## A.14.4.1.12Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode for less than 5 MHz BW

## A.14.4.1.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting support-3MHz-ChannelBW-r18 properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell operating on a 3 MHz channel bandwidth. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1C.

Supported test configurations are specified in table A.14.4.1.12.1-1. General test parameters as specified in table A.14.4.1.4.1-2 with config 1 apply to this test, except those specified in table A.14.4.1.12.1-2. Cell specific test parameters as specified in table A.14.4.1.4.1-3 apply except those specified in table A.14.4.1.12.1-3.

The test procedure specified in clause A.14.4.1.4.1 applies to this test.

Table A.14.4.1.12.1-1: Supported test configurations for FR1 PCell

Table A.14.4.1.12.1-2: General test parameters for FR1 in-sync testing in DRX mode

Table A.14.4.1.12.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in DRX mode

## A.14.4.1.12.2Test Requirements

Test requirements specified in clause A.14.4.1.4.2 apply to this test.

## A.14.4.2Beam Failure Detection and Link recovery procedures for satellite access

## A.14.4.2.1Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode

## A.14.4.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell which is served by satellite access node (SAN) and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.14.4.2.1.1-1, A.14.4.2.1.1-2, A.14.4.2.1.1-3 and A.14.4.2.1.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.2.1.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.14.4.2.1.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.14.4.2.1.1-1: Supported test configurations for FR1 Pcell

Table A.14.4.2.1.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.14.4.2.1.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.14.4.2.1.1-1: SNR and L1-RSRP variation SSB for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.14.4.2.1.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.2.2Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode

## A.14.4.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell which is served by satellite access node (SAN) and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.14.4.2.2.1-1, A.14.4.2.2.1-2, A.14.4.2.2.1-3, A.14.4.2.2.1-4 and A.14.4.2.2.1-5 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.2.2.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.14.4.2.2.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.14.4.2.2.1-1: Supported test configurations for FR1 Pcell

Table A.14.4.2.2.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.14.4.2.2.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Figure A.14.4.2.2.1-1: SNR and L1-RSRP variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.14.4.2.2.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 1920+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.2.3Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode

## A.14.4.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell which is served by satellite access node (SAN) and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.14.4.2.3.1-1, A.14.4.2.3.1-2, and below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.2.3.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.14.4.2.3.1-1 additionally shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.14.4.2.3.1-1: Supported test configurations for FR1 Pcell

Table A.14.4.2.3.1-2: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.14.4.2.3.1-3 Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Figure A.14.4.2.3.1-1: SNR and L1-RSRP variation for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

## A.14.4.2.3.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 30+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.2.4Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode

## A.14.4.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell which is served by satellite access node (SAN) and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.14.4.2.4.1-1, A.14.4.2.4.1-2, A.14.4.2.4.1-3, and A.14.4.2.4.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.2.4.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.14.4.2.4.1-1 additionally shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.14.4.2.4.1-1: Supported test configurations for FR1 Pcell

Table A.14.4.2.4.1-2: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.14.4.2.4.1-3: Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.14.4.2.4.1-1: SNR and L1-RSRP variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

## A.14.4.2.4.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 1920+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.2.5Void

## A.14.4.2.6Void

## A.14.4.2.7Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode for a UE operating on a cell with less than 5 MHz BW

## A.14.4.2.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting support-3MHz-ChannelBW-r18 properly detects SSB-based beam failure in the set q0 configured for a serving cell which is served by satellite access node (SAN) and operatw on a less than 5 MHz bandwidth, and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell which is served by satellite access node (SAN) requirements in clause 8.5C for a UE operating on a cell with less than 5 MHz BW.

Supported test configurations are specified in table A.14.4.2.7.1-1. General test parameters as specified in table A.14.4.2.2.1-2 with config 1 apply except those specified in table A.14.4.2.7.1-2. Cell specific test parameters as specified in table A.14.4.2.2.1-3 apply except those specified in table A.14.4.2.7.1-3.

The test procedure specified in clause A.14.4.2.2.1 applies to this test.

Table A.14.4.2.7.1-1: Supported test configurations for FR1 Pcell with less than 5 MHz BW

Table A.14.4.2.7.1-2: General test parameters for FR1 PCell with less than 5 MHz BW

Table A.14.4.2.7.1-3: Cell specific test parameters for FR1 PCell with less than 5 MHz BW

## A.14.4.2.7.2Test Requirements

Test requirements specified in clause A.14.4.2.2.1 apply to this test.

## A.14.4.3Active BWP switch for satellite access

## A.14.4.3.1DCI-based and Timer-based Active BWP Switch

## A.14.4.3.1.1NR FR1 DL active BWP switch with non-DRX in SA

## A.14.4.3.1.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6C.

The supported test configurations are shown in table A.14.4.3.1.1.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.14.4.3.1.1.1-2. Cell-specific parameters of the cell are specified in table A.14.4.3.1.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE is configured with 2 different UE-specific downlink bandwidth parts, BWP-1 and BWP-2 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1.

-UE is configured with a bwp-InactivityTimer timer value for Cell 1.

The cell has constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for DL BWP switch, sent from the test equipment to the UE, is received at the UE side in Cell 1’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6C and starts to report valid ACK/NACK for the Cell 1 no later than the first UL slot that occurs after the beginning of slot (). The UE shall be continuously scheduled on Cell 1’s BWP-2 starting from the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).i+TBWPswitchDelay+k1+2µ-µKoffsetKoffset

During T2, the test equipment won’t transmit DCI format for PDSCH reception on Cell 1.

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the subframe immediately after bwp-InactivityTimer timer expires. The UE shall switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s slot (j+TBWPswitchDelay) as defined in clause 8.6C and starts to report valid ACK/NACK for the Cell 1 at latest on the first UL slot that occurs after the beginning of slot (). The UE shall be continuously scheduled on Cell 1’s BWP-1 starting from the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).j+TBWPswitchDelay+k1+2µ-µKoffsetKoffset

The test equipment verifies the DL BWP switch time by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK/NACK is received.

Table A.14.4.3.1.1.1-1: DL BWP switch supported test configurations

Table A.14.4.3.1.1.1-2: General test parameters for DL BWP switch in SA

Table A.14.4.3.1.1.1-3 : NR Cell specific test parameters for DL BWP switch in SA

## A.14.4.3.1.1.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot ().i+TBWPswitchDelay+k1+2µ-µKoffsetKoffset

During T3, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (.j+TBWPswitchDelay+k1+2µ-µKoffsetKoffset

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6C.2-1.

All of the above test requirements shall be fulfilled in order for the observed Cell 1 active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.3.2RRC-based Active BWP Switch

## A.14.4.3.2.1NR FR1 DL active BWP switch of Cell with non-DRX in SA

## A.14.4.3.2.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6C.

The supported test configurations are shown in table A.14.4.3.2.1.1-1. The test scenario comprises of one Cell (Cell 1) as given in table A.14.4.3.2.1.1-2. Cell-specific parameters of Cell are specified in table A.14.4.3.2.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in Cell 1.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is completely received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot () as defined in clause 8.6C.3 and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot () on BWP-1 of final condition. The UE shall be continuously scheduled on PCell’s BWP-1 of final condition starting from the first DL slot right after slot ().i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot lengthi+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1+2µ-µKoffsetKoffseti+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause 8.6C.3.

The test equipment verifies the DL BWP switch time in Cell by counting the time from the time when the RRC Reconfiguration message including updated BWP configuration is sent till the time when a vaild ACK/NACK is received is received.

Table A.14.4.3.2.1.1-1: DL BWP switch supported test configurations in SA scenario

Table A.14.4.3.2.1.1-2: General test parameters for DL BWP switch in SA scenario

Table A.14.4.3.2.1.1-3: NR Cell specific test parameters for DL BWP switch in SA scenario

## A.14.4.3.2.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the Cell from the first DL slot that occurs right after the begining of slot () and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (). i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot lengthi+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1+2µ-µKoffsetKoffset

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed Cell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.4UE specific CBW change for satellite access

## A.14.4.4.1UE specific CBW change on PCell in FR1 in non-DRX

## A.14.4.4.1.1Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13C.

The supported test configurations are shown in table A.14.4.4.1.1-1. The test scenario comprises of one Cell (Cell 1), which is PCell as given in table A.14.4.4.1.1-2. Cell-specific parameters are specified in table A.14.4.4.1.1-3.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE sends ACK/NACK during the test.

Before the test starts:

UE is connected to Cell 1 (PCell) on radio channel 1.

UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PCell).

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PCell.

UE has been configured with UE specific CBW (CBW-1).

UE is indicated in SCS-SpecificCarrier [2] that the UE specific CBW is CBW-1 as the initial condition in Cell 1 (PCell).

Cell 1 (PCell) has constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration containing SCS-SpecificCarrier with updated UE specific CBW, sent from the test equipment to the UE, is completely received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its UE specific CBW with the updated CBW-2 for the final condition.

The UE shall be able to receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot () as defined in clause 8.13C and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot () on the PCell’s BWP-1 on CBW-2 for the final condition. The UE shall be continuously scheduled on the PCell’s BWP-1 on CBW-2  for the final condition starting from the first DL slot right after slot ().i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot lengthi+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length+k1+2µ-µKoffsetKoffseti+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length

and  are defined in clause 8.13C.TRRCprocessingDelayTCBWchangeDelayRRC

The test equipment verifies the UE specific CBW switching delay in PCell by estimating the time from the moment the RRC Reconfiguration message including updated UE specific CBW configuration is sent until the moment a vaild ACK/NACK is received.

Table A.14.4.4.1.1-1: Supported test configurations for UE specific CBW change in SA scenario

Table A.14.4.4.1.1-2: General test parameters for UE specific CBW change in SA scenario

Table A.14.4.4.1.1-3: NR Cell specific test parameters for UE specific CBW change in SA scenario

## A.14.4.4.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the PCell from the first DL slot that occurs right after the begining of slot () and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot ().i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot lengthi+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length+k1+2µ-µKoffsetKoffset

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed UE specific CBW change delay on the PCell to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.4.5Pathloss reference signal switching delay

## A.14.4.5.1MAC-CE based pathloss reference signal switch delay

## A.14.4.5.1.1Test Purpose and Environment

The purpose of this test is to verify the MAC-CE based pathloss reference signal switch delay requirement defined in clause 8.14C.

The supported test configurations are shown in table A.14.4.5.1.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.14.4.5.1.1-2. Cell-specific parameters of the cell are specified in table A.14.4.5.1.1-3 below.

The test consists of 3 successive time periods, with duration of T1, T2 and T3, respectively.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 on radio channel 1.

-UE shall be fully synchronized to SSB #0.

During T1,

-The UE shall track SSB #1 so that SSB #1 as a pathloss reference signal is known to the UE.

Time period T2 starts when the UE is configured of the power headroom reporting functionality by upper layers by the test equipment and the UE shall transmit a PHR during T2.

During T2,

-UE is configured with a phr-ProhibitTimer timer value for Cell 1.

-UE is configured with a phr-Tx-PowerFactorChange value for Cell 1.

During T3,

Time period T3 starts when a PDSCH carrying MAC-CE activation for pathloss reference signal switch, sent from the test equipment to the UE to swicth the pathloss reference signal from SSB 0 to SSB 1, is received at the UE side in Cell 1’s slot # denoted i. The UE shall switch its pathloss reference signal to the target one and send PHR.

The UE shall be able to apply the target pathloss reference signal of the serving cell on which pathloss reference signal switch occurs no later than the slot i + +  as defined in clause 8.14.  The UE shall be able to apply old pathloss reference signals until the slot i + +  as defined in clause 8.14.THARQ3 ms + 5*Ttarget_PL-RS + 2 msNR slot lengthTHARQ3Nslotsubframe,µ

The test equipment verifies the pathloss RS switch time by counting the slots from the time when the pathloss RS switch command is transmitted till a PHR is received during T3.

Table A.14.4.5.1.1-1: MAC-CE based pathloss reference signal switch supported test configurations

Table A.14.4.5.1.1-2: General test parameters for MAC-CE based pathloss reference signal switch

Table A.14.4.5.1.1-3: NR Cell specific test parameters for MAC-CE based pathloss reference signal switch

## A.14.4.5.1.2Test Requirements

During T3, the UE shall start to send the PHR for PCell no later than the slot i + + .THARQ3 ms + 5*Ttarget_PL-RS + 2 msNR slot length

During T3, the UE shall start to send the PHR for PCell no earlier than the slot i + + .THARQ3Nslotsubframe,µ

Where,  is the timing between pathloss reference MAC-CE activation command and acknowledgement as specified in [7],  is the periodicity of the target pathloss reference signal which is SSB in this test.THARQTtarget_PL-RS

During T3, UE shall send L1-RSRP report with measurement results for both SSB0 and SSB1.

All of the above test requirements shall be fulfilled in order for the observed pathloss RS switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The UE shall be given proper uplink transmission grant during T2 and T3.

## A.14.5Measurement procedure

## A.14.5.1Intra-frequency Measurements

## A.14.5.1.1SA event triggered reporting tests without gap under non-DRX

## A.14.5.1.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2C.5.1 and 9.2C.5.2.

## A.14.5.1.1.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell and neighbour cell are given in table A.14.5.1.1.2-1 and A.14.5.1.1.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

UE is configured with 2 non-overlapping SMTCs for the intra-frequency measurement. The SMTC periodicity is 20 ms, and SMTC1 is associated with Cell 1 with offset 0, and SMTC2 is associated with Cell 2 with offset 10 ms.

Table A.14.5.1.1.2-1: Supported test configurations

Table A.14.5.1.1.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1

Table A.14.5.1.1.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

## A.14.5.1.1.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.1.2SA event triggered reporting tests without gap under DRX

## A.14.5.1.2.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2C.5.1 and 9.2C.5.2.

## A.14.5.1.2.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.14.5.1.2.2-1, A.14.5.1.2.2-2 and A.14.5.1.2.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

The UE shall be provided with the valid information about the SAN serving cell in the test before the test.

UE is configured with 1 SMTC for the intra-frequency measurement. Both Cell 1 and Cell 2 are associated with the configured SMTC.

Table A.14.5.1.2.2-1: Supported test configurations

Table A.14.5.1.2.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 with DRX

Table A.14.5.1.2.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 with DRX

## A.14.5.1.2.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. X=1280 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC and supports parallelMeasurementWithoutRestriction-r17, X=1920 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC and not supports parallelMeasurementWithoutRestriction-r17, X=1080 for test configuration 2 and if UE indicates other than ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC and not supports parallelMeasurementWithoutRestriction-r17, otherwise X=920.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Y ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. Y=12800 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC and supports parallelMeasurementWithoutRestriction-r17, Y=20480 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC and not supports parallelMeasurementWithoutRestriction-r17, Y=10240 for test configuration 2 and if UE indicates other than ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC and not supports parallelMeasurementWithoutRestriction-r17, otherwise Y=6400.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.1.3SA event triggered reporting tests without gap under non-DRX with SSB index reading

## A.14.5.1.3.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2C.5.1 and 9.2C.5.2.

## A.14.5.1.3.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for FDD PCell and neighbour cell are given in table A.14.5.1.3.2-1 and A.14.5.1.3.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

UE is configured with 2 overlapping SMTC for the intra-frequency measurement. The SMTC periodicity is 20 ms, and SMTC1 is associated with Cell 1 with offset 0, and SMTC2 is associated with Cell 2 with offset 17 ms.

Table A.14.5.1.3.2-1: Supported test configurations

Table A.14.5.1.3.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

Table A.14.5.1.3.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

## A.14.5.1.3.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test. X=920 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=920.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.1.4SA event triggered reporting tests with single measurement gap under non-DRX for satellite access

## A.14.5.1.4.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2C.6.1 and 9.2C.6.2.

## A.14.5.1.4.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters are given in table A.14.5.1.4.2-1 and A.14.5.1.4.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP0 which contains the cell defining SSB, and BWP1 which does not contain any SSB of Cell 1. During the whole test, BWP1 is always scheduled as the active BWP for the UE.

The UE shall be provided with the valid information about the SAN serving each cell before the test.

UE is configured with 1 SMTC for the intra-frequency measurement. Both Cell 1 and Cell 2 are associated with the configured SMTC.

Table A.14.5.1.4.2-1: Supported test configurations

Table A.14.5.1.4.2-2: General test parameters for SA intra-frequency event triggered reporting with single measurement gap for PCell in FR1

Table A.14.5.1.4.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with single measurement gap for PCell in FR1

## A.14.5.1.4.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. X=1600 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=1000.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.1.5SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access

## A.14.5.1.5.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2C.6.1 and 9.2C.6.2.

## A.14.5.1.5.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters are given in table A.14.5.1.5.2-1, A. 14.5.1.5.2-2 and A. 14.5.1.5.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3.

There are two BWPs configured in Cell 1, BWP0 which contains the cell defining SSB, and BWP1 which does not contain any SSB of Cell 1. During the whole test, BWP1 is always scheduled as the active BWP for the UE.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

The UE shall be provided with the valid information about the SAN serving each cell before the test.

The UE is configured with 2 FNO concurrent measurement gaps for the intra-frequency measurement. Serving Cell 1 is expected to be measured within MeasGapId #0 and Neighbour Cell 2 is expected to be measured within MeasGapId #1.

Table A.14.5.1.5.2-1: Supported test configurations

Table A.14.5.1.5.2-2: General test parameters for SA intra-frequency event triggered reporting with FNO concurrent gaps for PCell in FR1 with DRX

Table A.14.5.1.5.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with FNO concurrent gaps for PCell in FR1 with DRX

Table A.14.5.1.5.2-4: Void

Table A.14.5.1.5.2-5: Void

## A.15.5.1.5.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 6400 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.1.6SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access

## A.14.5.1.6.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2C.6.1 and 9.2C.6.2.

## A.14.5.1.6.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for FDD PCell and neighbour cells are given in table A.14.5.1.6.2-1 and A.14.5.1.6.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP0 which contains the cell defining SSB, and BWP1 which does not contain any SSB of Cell 1. During the whole test, BWP1 is always scheduled as the active BWP for the UE.

The UE shall be provided with the valid information about the SAN serving each cell before the test.

The UE is configured with 2 PPO concurrent measurement gaps for the intra-frequency measurement. Serving Cell 1 is expected to be measured within MeasGapId #0 and Neighbour Cell 2 is expected to be measured within MeasGapId #1. And the priority for MeasGapId #1 is higher than the priority for MeasGapId #0.

Table A.14.5.1.6.2-1: Supported test configurations

Table A.14.5.1.6.2-2: General test parameters for SA intra-frequency event triggered reporting with PPO concurrent gaps for FDD PCell in FR1 with SSB index reading

Table A.14.5.1.6.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with PPO concurrent gaps for FDD PCell in FR1 with SSB index reading

## A.14.5.1.6.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1240 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.1.7SA event triggered reporting test with SSB time index reading without gap under non-DRX for FR2-NTN

## A.14.5.1.7.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in FR2-NTN in clause 9.2C.7.1 and 9.2C.7.2.

## A.14.5.1.7.2Test parameters

Two cells are deployed in the test, which are FR2 PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for FDD PCell and neighbour cell are given in table A.14.5.1.7.2-1 and A.14.5.1.7.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

UE is configured with 1 SMTC for the intra-frequency measurement. Both Cell 1 and Cell 2 are associated with the configured SMTC.

Table A.14.5.1.7.2-1: Supported test configurations

Table A.14.5.1.7.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR2-NTN with SSB index reading

Table A.14.5.1.7.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR2-NTN with SSB index reading

Table 14.5.1.7.2-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with FDD PCell in FR2-NTN without gap without DRX

## A.14.5.1.7.3Test Requirements

For both UE indicating [Type 1] and [Type 2] via UE capability [Beam steering], the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.1.8SA event triggered reporting tests without gap under non-DRX with SSB index reading under less 5MHz BW

## A.14.5.1.8.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2C.5.1 and 9.2C.5.2.

## A.14.5.1.8.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for FDD PCell and neighbour cell are given in table A.14.5.1.8.2-1 and A.14.5.1.8.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

UE is configured with 2 overlapping SMTC for the intra-frequency measurement. The SMTC periodicity is 20 ms, and SMTC1 is associated with Cell 1 with offset 0, and SMTC2 is associated with Cell 2 with offset 17 ms.

Table A.14.5.1.8.2-1: Supported test configurations

Table A.14.5.1.8.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

Table A.14.5.1.8.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

## A.14.5.1.8.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test. X=1000 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=880.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.1.9SA event triggered reporting tests without gap under non-DRX

## A.14.5.1.9.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event when configured with two different SMTC configurations. This test will partly verify the intra-frequency cell search requirements in clauses 9.2C.5.1 and 9.2C.5.2 for UEs that support the configuration of different SMTC periodicities for different cells.

## A.14.5.1.9.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The supported test configurations and general test configurations are given in table A.14.5.1.9.2-1 and A.14.5.1.9.2-2 below, respectively. The cell specific test parameters for PCell and neighbour cell are given in table A.14.5.1.9.2-3. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

UE is configured with 2 non-overlapping SMTCs for the intra-frequency measurement. The SMTC periodicity is 20 ms, for Cell 1 (serving cell at the beginning of the test case) with SMTC Config.1 is associated with Cell 1 with offset 0, and the SMTC periodicity for the neighbor cell is 160 ms, with SMTC Config.2 is associated with Cell 2 with offset 10 ms. The two cells are associated to the same satellite

Table A.14.5.1.9.2-1: Supported test configurations

Table A.14.5.1.9.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1

Table A.14.5.1.9.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

## A.14.5.1.9.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1600 ms from the beginning of the period T2. The UE is not required to read the neighbour cell SSB index in this test. The test requirement was obtained from:

Tidentify_intra_without_index = (TPSS/SSS_sync_intra + TSSB_measurement_period_intra) ms

Where:

-TPSS/SSS_sync_intra   = max( 600 ms, ceil( 5 x Kp x Klayer1_measurement) x Kmulti_SMTC x SMTC period ) x CSSFintra =

max(600 ms, ceil(5x 1 x 1) x 1 x 160) x 1

= 800 ms.

-max(200 ms, ceil( 5 x Kp x Klayer1_measurement) x Kmulti_SMTC x SMTC period) x CSSFintra

= 800 ms

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2Inter-frequency Measurements

## A.14.5.2.1SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with single gap for satellite access

## A.14.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3C.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.14.5.2.1.1-1, A.14.5.2.1.1-2 and A.14.5.2.1.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in table A.14.5.2.1.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.14.5.2.1.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

Table A.14.5.2.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.14.5.2.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

## A.14.5.2.1.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2.2SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for satellite access

## A.14.5.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3C.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.14.5.2.2.1-1, A.14.5.2.2.1-2 and A.14.5.2.2.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.14.5.2.2.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.14.5.2.2.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

Table A.14.5.2.2.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.14.5.2.2.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.14.5.2.2.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.14.5.2.2.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.14.5.2.2.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1080 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 10240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2 UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2.3SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for satellite access

## A.14.5.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3C.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.14.5.2.3.1-1, A.14.5.2.3.1-2 and A.14.5.2.3.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in table A.14.5.2.3.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.14.5.2.3.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1

Table A.14.5.2.3.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

Table A.14.5.2.3.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

## A.14.5.2.3.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1040 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2.4SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for satellite access

## A.14.5.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the multiple gaps capable UE makes correct reporting of events. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3C.4.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2, and NR Cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.14.5.2.4.1-1, A.14.5.2.4.1-2 and A.14.5.2.4.1-3.

In this test measurement gap pattern configuration # 0 as defined in table A.14.5.2.4.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2 and NR Cell 3.

Table A.14.5.2.4.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

Table A.14.5.2.4.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.14.5.2.4.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

## A.14.5.2.4.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2.5void

## A.14.5.2.5.1void

## A.14.5.2.5.2void

## A.14.5.2.6SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for satellite access

## A.14.5.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the multiple gaps capable UE makes correct reporting of events. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3C.4.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2, and NR Cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.14.5.2.6.1-1, A.14.5.2.6.1-2 and A.14.5.2.6.1-3.

In test 1 measurement gap pattern configuration # 0 and #1 as defined in table A.14.5.2.6.1-2 are provided. MeasGapId #2 is configured with a higher priority than MeasGapId #1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2 and NR Cell 3.

Table A.14.5.2.6.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

Table A.14.5.2.6.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.14.5.2.6.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

## A.14.5.2.6.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1280 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2.7Event triggered reporting test without gap under non-DRX

## A.14.5.2.7.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the inter-frequency cell search requirements in clauses 9.3C.7.

## A.14.5.2.7.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) on NR RF channel 1 and a FR1 neighbour cell (Cell 2) on NR RF channel 2. The test parameters for PCell and neighbour cell are given in table A.14.5.2.7.2-1, A.14.5.2.7.2-2 and A.14.5.2.7.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE shall be provided with the valid information about the SAN serving each cell in the test before the test.

UE is configured with 2 non-overlapping SMTCs. The SMTC periodicity is 20 ms, and SMTC1 is associated with Cell 1 with offset 0, and SMTC2 is associated with Cell 2 with offset 10 ms.

Table A.14.5.2.7.2-1: Supported test configurations

Table A.14.5.2.7.2-2: General test parameters for inter-frequency event triggered reporting without gap for FR1

Table A.14.5.2.7.2-3: NR Cell specific test parameters for inter-frequency event triggered reporting without gap for FR1

## A.14.5.2.7.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2.8Event triggered reporting tests without gap under DRX

## A.14.5.2.8.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the inter-frequency cell search requirements in clauses 9.3C.7.

## A.14.5.2.8.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) on NR RF channel 1 and a FR1 neighbour cell (Cell 2) on NR RF channel 2. The test parameters for PCell and neighbour cell are given in table A.14.5.2.8.2-1, A.14.5.2.8.2-2 and A.14.5.2.8.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

The UE shall be provided with the valid information about the SAN serving each cell in the test before the test.

UE is configured with 2 non-overlapping SMTCs. The SMTC periodicity is 20 ms, and SMTC1 is associated with Cell 1 with offset 0, and SMTC2 is associated with Cell 2 with offset 10 ms.

Table A.14.5.2.8.2-1: Supported test configurations

Table A.14.5.2.8.2-2: General test parameters for inter-frequency event triggered reporting without gap for PCell in FR1 with DRX

Table A.14.5.2.8.2-3: NR Cell specific test parameters for inter-frequency event triggered reporting without gap for PCell in FR1 with DRX

## A.14.5.2.8.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. X=1280 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=920.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Y ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. Y=12800 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise Y=6400.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.2.9SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used with single gap for 3 MHz channel bandwidth in satellite access

## A.14.5.2.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3C.4. This test is applicable for UEs that support less than 5 MHz operation.

The test procedure in clause A.14.5.2.3 applies for this test. Supported test configurations are specified in Table A.14.5.2.9.1-1. The list of general and NR specific test configuration reuse those in test clause A.14.5.2.3, except for those provided in Tables A.14.5.2.9.1-2 and A.14.5.2.9.1-3.

Table A.14.5.2.9.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1

Table A.14.5.2.9.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection in operation with 3 MHz Channel Bandwith

Table A.14.5.2.9.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection in operation with 3 MHz Channel Bandwith

## A.14.5.2.9.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1440 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.3L1-RSRP measurement for beam reporting for satellite access

## A.14.5.3.1SSB based L1-RSRP measurement for satellite access when DRX is not used

## A.14.5.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4C.1, with the testing configurations for NR cells served by satellite access node (SAN) in Table A.14.5.3.1.1-1.

Table A.14.5.3.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test for satellite access

## A.14.5.3.1.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.14.5.3.1.2-1 and table A.14.5.3.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.14.5.3.1.2-1: General test parameters

Table A.14.5.3.1.2-2: SSB specific test parameters

## A.14.5.3.1.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19C.1.1 and relative accuracy requirement in clause 10.1.19C.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.3.2SSB based L1-RSRP measurement for satellite access when DRX is used

## A.14.5.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells served by satellite access node (SAN)in table A.14.5.3.2.1-1.

Table A.14.5.3.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test for satellite access

## A.14.5.3.2.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.14.5.3.2.2-1 and table A.14.5.3.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.14.5.3.2.2-1: General test parameters

Table A.14.5.3.2.2-2: SSB specific test parameters

## A.14.5.3.2.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19C.1.1 and relative accuracy requirement in clause 10.1.19C.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.3.3CSI-RS based L1-RSRP measurement for satellite access when DRX is not used

## A.14.5.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells served by satellite access node (SAN)  in table A.14.5.3.3.1-1.

Table A.14.5.3.3.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test for satellite access

## A.14.5.3.3.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.14.5.3.3.2-1 and table A.14.5.3.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot 2 of a frame and UE provides the report back based on the reporting configuration as defined in table A.14.5.3.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.14.5.3.3.2-1: General test parameters

Table A.14.5.3.3.2-2: CSI-RS specific test parameters

## A.14.5.3.3.3Test Requirements

After 80ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.19C.1.1 and relative accuracy requirement in clause 10.1.19C.1.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.3.4CSI-RS based L1-RSRP measurement for satellite access when DRX is used

## A.14.5.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells served by satellite access node (SAN) in table A.14.5.3.4.1-1.

Table A.14.5.3.4.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test for satellite access

## A.14.5.3.4.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.14.5.3.4.2-1 and table A.14.5.3.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot 2 of a frame and UE provides the report back based on the reporting configuration as defined in table A.14.5.3.4.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.14.5.3.4.2-1: General test parameters

Table A.14.5.3.4.2-2: CSI-RS specific test parameters

## A.14.5.3.4.3Test Requirements

After 80ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.19C.1.1 and relative accuracy requirement in clause 10.1.19C.1.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.14.5.3.5SSB based L1-RSRP measurement when DRX is not used in FR2-NTN

## A.14.5.3.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5C.4.1, with the testing configurations for NR cells in table A.14.5.3.5.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15C.1.

Table A.14.5.3.5.1-1: Applicable NR configurations for FR2-NTN SSB based L1-RSRP test

## A.14.5.3.5.2Test parameters

There is one cells in the test, the FR2-NTN PCell (Cell 1). The test parameters for the Cell 1 are given in table A.14.5.3.5.2-1 and table A.14.5.3.5.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.14.5.3.5.2-1: General test parameters

Table A.14.5.3.5.2-2: SSB specific test parameters

## A.14.5.3.5.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than 1200 ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause 10.1.20C.1

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.6Measurement Performance requirements

## A.14.6.1SS-RSRP for SAN

## A.14.6.1.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

## A.14.6.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.2C.1.1 and 10.1.2C.1.2 for intra-frequency measurements.

## A.14.6.1.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.14.6.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.14.6.1.1.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.6.1.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

Table A.14.6.1.1.2-2: SS-RSRP Intra frequency test parameters

## A.14.6.1.1.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.2C.1.1 and relative requirement in clause 10.1.2C.1.2.

## A.14.6.1.2SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

## A.14.6.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.4C.1.1 and 10.1.4C.1.2 for inter-frequency measurements with the testing configurations for NR cells in table A.14.6.1.2.1-1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.6.1.2.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

## A.14.6.1.2.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.14.6.1.2.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.14.6.1.2.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.14.6.1.2.2-1: SS-RSRP inter-frequency test parameters

## A.14.6.1.2.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil the absolute requirement in clause 10.1.4C.1.1 and relative requirement in clause 10.1.4C.1.2.

## A.14.6.1.3SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

## A.14.6.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.3C.1.1 and 10.1.3C.1.2 for intra-frequency measurements.

## A.14.6.1.3.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.14.6.1.3.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in table A.14.6.1.3.2-2 and A.14.6.1.3.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. The TCI status for Cell 1 is defined in table [TBD] and TRS configuration for Cell 1 is defined in [TBD]. The test consists of two time phases T1 and T2.

Table A.14.6.1.3.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

Table A.14.6.1.3.2-2: SS-RSRP Intra frequency general test parameters

Table A.14.6.1.3.2-3: SS-RSRP Intra frequency OTA related test parameters

## A.14.6.1.3.3Test Requirements

The SS-RSRP measurement accuracy shall fulfil the absolute accuracy requirements in clauses 10.1.3.1.1 and relative accuracy requirements in clause 10.1.3.1.2. The following requirements are to be verified:

During T1:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.14.6.1.3.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3C.1.2-1.

During T2:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.14.6.1.3.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3C.1.2-1.

During T1 and T2:

Relative accuracy of Cell 1 during T2 compared with Cell 1 during T1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3C.1.2-1.

Relative accuracy of Cell 2 during T2 compared with Cell 2 during T1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3C.1.2-1.

Table A.14.6.1.3.3-1: SS-RSRP absolute accuracy test requirement

## A.14.6.2SS-RSRQ

## A.14.6.2.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access

## A.14.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.7C.

## A.14.6.2.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.14.6.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.14.6.2.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.14.6.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

Table A.14.6.2.1.2-2: SS-RSRQ Intra frequency test parameters

## A.14.6.2.1.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.7C.1.1.

## A.14.6.2.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access

## A.14.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.7C.

## A.14.6.2.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.14.6.2.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.14.6.2.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.14.6.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.14.6.2.2.2-2: SS-RSRQ Inter frequency test parameters

## A.14.6.2.2.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.9C.1.1 and 10.1.9C.1.2.

## A.14.6.3SS-SINR

## A.14.6.3.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.14.6.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.12C.1.1.

## A.14.6.3.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.14.6.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.14.6.3.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.14.6.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

Table A.14.6.3.1.2-2: SS-SINR Intra frequency test parameters

## A.14.6.3.1.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.12C.1.1.

## A.14.6.3.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.14.6.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.14C.1.1 and 10.1.14C.1.2.

## A.14.6.3.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.14.6.3.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.14.6.3.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.14.6.3.2.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

Table A.14.6.3.2.2-2: SS-SINR Inter frequency test parameters

## A.14.6.3.2.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.14C.1.1 and 10.1.14C.1.2.

## A.14.6.4L1-RSRP measurement for beam reporting

## A.14.6.4.1SSB based L1-RSRP measurement

## A.14.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.5C.4 and clause 10.1.19C.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.14.6.4.1.1-1.

Table A.14.6.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.14.6.4.1.2Test parameters

In this set of test cases there one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.14.6.4.1.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.14.6.4.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.14.6.4.1.2-1: FR1 SSB based L1-RSRP test parameters

## A.14.6.4.1.3Test Requirements

The L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 2 shall fulfil the requirements in clauses 10.1.19C.1.

## A.14.6.4.2CSI-RS based L1-RSRP measurement on resource set with repetition off

## A.14.6.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.5C.4 and clause 10.1.19C.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.14.6.4.2.1-1.

Table A.14.6.4.2.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.14.6.4.2.2Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.14.6.4.2.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.14.6.4.2.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.14.6.4.2.2-1: FR1 CSI-RS based L1-RSRP test parameters

## A.14.6.4.2.3Test Requirements

The L1-RSRP measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirements in clause 10.1.19C.2.

## A.14.6.4.3SSB based L1-RSRP measurement for VSAT UE in FR2-NTN when DRX is not used

## A.14.6.4.3.1Test Purpose and Environment

The purpose of this test is to verify that the VSAT UE makes correct reporting of L1-RSRP measurement in FR2-NTN. This test will partly verify the L1-RSRP measurement requirements in clause 9.5C.4.1, with the testing configurations for NR cells in table A.14.6.4.3.1-1.

The AoA setup for this test is [TBD] as defined in [clause TBD].

Table A.14.6.4.3.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test for VSAT UE

## A.14.6.4.3.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.14.6.4.3.2-1 and table A.14.6.4.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.14.6.4.3.2-1: General test parameters

Table A.14.6.4.3.2-2: SSB specific test parameters

## A.14.6.4.3.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than 640 ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in [clause TBD].

The reported L1-RSRP value shall include the Rx antenna gain in the range of table B.2.1.8.1-1.

The rate of correct events observed during repeated tests shall be at least 90 %.
