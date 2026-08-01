| 3GPP TS 36.213 V19.3.0 (2026-03) |  |
| --- | --- |
| Technical Specification |  |
| 3rd Generation Partnership Project;Technical Specification Group Radio Access Network;Evolved Universal Terrestrial Radio Access (E-UTRA);Physical layer procedures(Release 19) |  |
|  |  |
| ![](media/image1.emf) |  |
|  |  |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. |  |

|  |
| --- |
| 3GPPPostal address3GPP support office address650 Route des Lucioles - Sophia AntipolisValbonne - FRANCETel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16Internethttp://www.3gpp.org |
| Copyright NotificationNo part may be reproduced except as authorized by written permission. The copyright and the foregoing restriction extend to reproduction in all media.© 2026, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).All rights reserved.UMTS™ is a Trade Mark of ETSI registered for the benefit of its members3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersGSM® and the GSM logo are registered and owned by the GSM Association |

Contents

Foreword 8

1 Scope 9

2 References 9

3 Symbols and abbreviations 10

3.1 Symbols 10

3.2 Abbreviations 10

4 Synchronization procedures 12

4.1 Cell search 12

4.2 Timing synchronization 12

4.2.1 Radio link monitoring 12

4.2.2 Inter-cell synchronization 12

4.2.3 Transmission timing adjustments 12

4.3 Timing for Secondary Cell Activation / Deactivation 14

5 Power control 16

5.1 Uplink power control 16

5.1.1 Physical uplink shared channel 17

5.1.1.1 UE behaviour 17

5.1.1.2 Power headroom 32

5.1.2 Physical uplink control channel 35

5.1.2.1 UE behaviour 36

5.1.3 Sounding Reference Symbol (SRS) 41

5.1.3.1 UE behaviour 41

5.1.3.2 Power headroom for Type3 report 44

5.1.4 Power allocation for EUTRA dual connectivity 45

5.1.4.1 Dual connectivity power control Mode 1 45

5.1.4.2 Dual connectivity power control Mode 2 52

5.1.4a Power allocation for dual active protocol stack 57

5.1.5 Power allocation for PUCCH-SCell 57

5.2 Downlink power allocation 58

5.2.1 eNodeB Relative Narrowband TX Power (RNTP) restrictions 61

6 Random access procedure 62

6.1 Physical non-synchronized random access procedure 62

6.1.1 Timing 63

6.2 Random Access Response Grant 64

7 Physical downlink shared channel related procedures 69

7.1 UE procedure for receiving the physical downlink shared channel 71

7.1.1 Single-antenna port scheme 90

7.1.2 Transmit diversity scheme 90

7.1.3 Large delay CDD scheme 91

7.1.4 Closed-loop spatial multiplexing scheme 91

7.1.5 Multi-user MIMO scheme 91

7.1.5A Dual layer scheme 91

7.1.5B Up to 8 layer transmission scheme 91

7.1.6 Resource allocation 91

7.1.6.1 Resource allocation type 0 93

7.1.6.2 Resource allocation type 1 94

7.1.6.3 Resource allocation type 2 95

7.1.6.4 PDSCH starting position 98

7.1.6.4A PDSCH starting position for BL/CE UEs 100

7.1.6.5 Physical Resource Block (PRB) bundling 100

7.1.7 Modulation order and transport block size determination 102

7.1.7.1 Modulation order and redundancy version determination 105

7.1.7.2 Transport block size determination 111

7.1.7.2.1 Transport blocks not mapped to two or more layer spatial multiplexing 116

7.1.7.2.2 Transport blocks mapped to two-layer spatial multiplexing 125

7.1.7.2.3 Transport blocks mapped for DCI Format 1C and DCI Format 6-2 125

7.1.7.2.4 Transport blocks mapped to three-layer spatial multiplexing 126

7.1.7.2.5 Transport blocks mapped to four-layer spatial multiplexing 126

7.1.7.2.6 Transport blocks mapped for BL/CE UEs configured with CEModeB and PDSCH bandwidth up to 1.4MHz 127

7.1.7.2.7 Transport blocks mapped for BL/CE UEs SystemInformationBlockType1-BR 128

7.1.7.2.8 Transport blocks mapped for UEs configured with ce-pdsch-maxBandwidth-config value of 5 MHz or with pdsch-MaxBandwidth-SC-MTCH value of 24 PRBs 128

7.1.7.3 Redundancy Version determination for Format 1C 128

7.1.8 Storing soft channel bits 129

7.1.9 PDSCH resource mapping parameters 129

7.1.10 Antenna ports quasi co-location for PDSCH 131

7.1.11 PDSCH subframe assignment for BL/CE UE 132

7.2 UE procedure for reporting Channel State Information (CSI) 134

7.2.1 Aperiodic CSI Reporting using PUSCH 144

7.2.2 Periodic CSI Reporting using PUCCH 170

7.2.3 Channel Quality Indicator (CQI) definition 211

7.2.4 Precoding Matrix Indicator (PMI) definition 225

7.2.5 Channel-State Information – Reference Signal (CSI-RS) definition 253

7.2.6 Channel-State Information – Interference Measurement (CSI-IM) Resource definition 255

7.2.7 Zero Power CSI-RS Resource definition 255

7.2.8 CSI-RS Activation / Deactivation 255

7.3 UE procedure for reporting HARQ-ACK 256

7.3.1 FDD HARQ-ACK reporting procedure 261

7.3.2 TDD HARQ-ACK reporting procedure 266

7.3.2.1 TDD HARQ-ACK reporting procedure for same UL/DL configuration 266

7.3.2.2 TDD HARQ-ACK reporting procedure for different UL/DL configurations 281

7.3.3 FDD-TDD HARQ-ACK reporting procedure for primary cell frame structure type 1 289

7.3.4 FDD-TDD HARQ-ACK reporting procedure for primary cell frame structure type 2 290

8 Physical uplink shared channel related procedures 292

8.0 UE procedure for transmitting the physical uplink shared channel 293

8.0.1 Single-antenna port scheme 320

8.0.2 Closed-loop spatial multiplexing scheme 320

8.1 Resource allocation for PDCCH/EPDCCH/SPDCCH with uplink DCI format 321

8.1.1 Uplink resource allocation type 0 321

8.1.2 Uplink resource allocation type 1 322

8.1.3 Uplink resource allocation type 2 322

8.1.4 Uplink resource allocation type 3 323

8.1.5 Uplink resource allocation type 4 324

8.1.5.1 UL Resource Block Groups 324

8.1.6 Uplink resource allocation type 5 325

8.2 UE sounding procedure 327

8.3 UE HARQ-ACK procedure 339

8.3A Autonomous uplink feedback procedure 341

8.4 UE PUSCH hopping procedure 341

8.4.1 Type 1 PUSCH hopping 342

8.4.2 Type 2 PUSCH hopping 342

8.5 UE Reference Symbol (RS) procedure 343

8.6 Modulation order, redundancy version and transport block size determination 344

8.6.1 Modulation order and redundancy version determination 344

8.6.2 Transport block size determination 352

8.6.3 Control information MCS offset determination 359

8.7 UE transmit antenna selection 363

8.8 Transmission timing adjustments 363

9 Physical downlink control channel procedures 363

9.1 UE procedure for determining physical downlink control channel assignment 364

9.1.1 PDCCH assignment procedure 364

9.1.2 PHICH assignment procedure 368

9.1.3 Control Format Indicator (CFI) assignment procedure 371

9.1.4 EPDCCH assignment procedure 372

9.1.4.1 EPDCCH starting position 379

9.1.4.2 Antenna ports quasi co-location for EPDCCH 379

9.1.4.3 Resource mapping parameters for EPDCCH 380

9.1.4.4 PRB-pair indication for EPDCCH 380

9.1.5 MPDCCH assignment procedure 381

9.1.5.1 MPDCCH starting position 389

9.1.5.2 Antenna ports quasi co-location for MPDCCH 389

9.1.5.3 Preconfigured Uplink Resource ACK/fallback procedure 389

9.1.6 SPDCCH assignment procedure 389

9.1.6.1 Resource mapping parameters for SPDCCH 391

9.1.6.2 PRB-pair indication for SPDCCH 391

9.1.6.3 Physical Resource Block (PRB) bundling for DMRS-based SPDCCH 392

9.1.6.4 Antenna ports quasi co-location for DMRS-based SPDCCH 392

9.2 PDCCH/EPDCCH/MPDCCH/SPDCCH validation for semi-persistent scheduling 393

9.2A PDCCH/EPDCCH validation for autonomous uplink transmissions 395

9.3 PDCCH/EPDCCH/MPDCCH/SPDCCH control information procedure 396

10 Physical uplink control channel procedures 397

10.1 UE procedure for determining physical uplink control channel assignment 398

10.1.1 PUCCH format information 403

10.1.2 FDD HARQ-ACK feedback procedures 410

10.1.2.1 FDD HARQ-ACK procedure for one configured serving cell 410

10.1.2.2 FDD HARQ-ACK procedures for more than one configured serving cell 414

10.1.2.2.1 PUCCH format 1b with channel selection HARQ-ACK procedure 414

10.1.2.2.2 PUCCH format 3 HARQ-ACK procedure 418

10.1.2.2.3 PUCCH format 4 HARQ-ACK procedure 420

10.1.2.2.4 PUCCH format 5 HARQ-ACK procedure 424

10.1.3 TDD HARQ-ACK feedback procedures 424

10.1.3.1 TDD HARQ-ACK procedure for one configured serving cell 426

10.1.3.2 TDD HARQ-ACK procedure for more than one configured serving cell 440

10.1.3.2.1 PUCCH format 1b with channel selection HARQ-ACK procedure 440

10.1.3.2.2 PUCCH format 3 HARQ-ACK procedure 456

10.1.3.2.3 PUCCH format 4 HARQ-ACK procedure 464

10.1.3.2.4 PUCCH format 5 HARQ-ACK procedure 480

10.1.3A FDD-TDD HARQ-ACK feedback procedures for primary cell frame structure type 2 480

10.1.4 HARQ-ACK Repetition procedure 482

10.1.5 Scheduling Request (SR) procedure 483

10.2 Uplink HARQ-ACK timing 485

11 Physical Multicast Channel (PMCH) related procedures 492

11.1 UE procedure for receiving the PMCH 492

11.2 UE procedure for receiving MCCH and system information change notification 495

12 Assumptions independent of physical channel 495

13 Uplink/Downlink configuration determination procedure for Frame Structure Type 2 496

13.1 UE procedure for determining eIMTA-uplink/downlink configuration 497

13A Subframe configuration for Frame Structure Type 3 498

14 UE procedures related to Sidelink 501

14.1 Physical Sidelink Shared Channel related procedures 502

14.1.1 UE procedure for transmitting the PSSCH 502

14.1.1.1 UE procedure for determining subframes for transmitting PSSCH for sidelink transmission mode 1 504

14.1.1.1.1 Determination of subframe indicator bitmap 504

14.1.1.2 UE procedure for determining resource blocks for transmitting PSSCH for sidelink transmission mode 1 507

14.1.1.2.1 PSSCH resource allocation for sidelink transmission mode 1 507

14.1.1.2.2 PSSCH frequency hopping for sidelink transmission mode 1 508

14.1.1.3 UE procedure for determining subframes for transmitting PSSCH for sidelink transmission mode 2 508

14.1.1.4 UE procedure for determining resource blocks for transmitting PSSCH for sidelink transmission mode 2 509

14.1.1.4A UE procedure for determining subframes and resource blocks for transmitting PSSCH for sidelink transmission mode 3 509

14.1.1.4B UE procedure for determining subframes and resource blocks for transmitting PSSCH and reserving resources for sidelink transmission mode 4 510

14.1.1.4C UE procedure for determining subframes and resource blocks for PSSCH transmission associated with an SCI format 1 510

14.1.1.5 UE procedure for PSSCH power control 511

14.1.1.6 UE procedure for determining the subset of resources to be reported to higher layers in PSSCH resource selection in sidelink transmission mode 4 and in sensing measurement in sidelink transmission mode 3 513

14.1.1.7 Conditions for selecting resources when the number of HARQ transmissions is two in sidelink transmission mode 4 516

14.1.2 UE procedure for receiving the PSSCH 516

14.1.3 UE procedure for determining resource block pool and subframe pool for sidelink transmission mode 2 517

14.1.5 UE procedure for determining resource block pool and subframe pool for sidelink transmission mode 3 and 4 518

14.2 Physical Sidelink Control Channel related procedures 519

14.2.1 UE procedure for transmitting the PSCCH 519

14.2.1.1 UE procedure for determining subframes and resource blocks for transmitting PSCCH for sidelink transmission mode 1 522

14.2.1.2 UE procedure for determining subframes and resource blocks for transmitting PSCCH for sidelink transmission mode 2 522

14.2.1.3 UE procedure for PSCCH power control 523

14.2.2 UE procedure for receiving the PSCCH 524

14.2.3 UE procedure for determining resource block pool and subframe pool for PSCCH 524

14.2.4 UE procedure for determining resource block pool for PSCCH in sidelink transmission mode 3 and 4 525

15 Void 529

16 UE Procedures related to narrowband IoT 529

16.1 Synchronization procedures 529

16.1.1 Cell search 529

16.1.2 Timing synchronization 529

16.2 Power control 530

16.2.1 Uplink power control 530

16.2.1.1 Narrowband physical uplink shared channel 530

16.2.1.1.1 UE behaviour 530

16.2.1.1.2 Power headroom 531

16.2.1.2 SR 532

16.2.1.2.1 UE behaviour 532

16.2.2 Downlink power allocation 532

16.3 Random access procedure 533

16.3.1 Physical non-synchronized random access procedure 533

16.3.2 Timing 534

16.3.3 Narrowband random access response grant 535

16.4 Narrowband physical downlink shared channel related procedures 536

16.4.1 UE procedure for receiving the narrowband physical downlink shared channel 537

16.4.1.1 Single-antenna port scheme 541

16.4.1.2 Transmit diversity scheme 541

16.4.1.3 Resource allocation 541

16.4.1.4 NPDSCH starting position 544

16.4.1.5 Modulation order and transport block size determination 545

16.4.1.5.1 Transport blocks not mapped for SystemInformationBlockType1-NB 546

16.4.1.5.2 Transport blocks mapped for SystemInformationBlockType1-NB 546

16.4.2 UE procedure for reporting ACK/NACK 547

16.5 Narrowband physical uplink shared channel related procedures 549

16.5.1 UE procedure for transmitting format 1 narrowband physical uplink shared channel 549

16.5.1.1 Resource allocation 552

16.5.1.2 Modulation order, redundancy version and transport block size determination 554

16.5.2 UE procedure for NPUSCH retransmission 556

16.5.3 UE procedure for transmitting SR 556

16.6 Narrowband physical downlink control channel related procedures 556

16.6.1 NPDCCH starting position 563

16.6.2 NPDCCH control information procedure 563

16.6.3 NPDCCH validation for semi-persistent scheduling 563

16.6.4 Preconfigured uplink resource ACK/fallback procedure 564

16.7 Assumptions independent of physical channel related to narrowband IoT 564

16.8 UE procedure for acquiring cell-specific reference signal sequence and raster offset 564

16.9 UE procedure for receiving narrowband wake up signal 565

16.10 GNSS measurement gap related procedures 566

17 Wake-up signal related procedures for BL/CE UE 566

18 GNSS measurement gap related procedures for BL/CE UE 567

Annex A (informative): Change history 568
