| 3GPP TS 38.101-1 V19.6.0 (2026-06) |  |
| --- | --- |
| Technical Specification |  |
| 3rd Generation Partnership Project;Technical Specification Group Radio Access Network;NR;User Equipment (UE) radio transmission and reception;Part 1: Range 1 Standalone(Release 19) |  |
|  |  |
| ![](media/image1.emf) | ![](media/image2.emf) |
|  |  |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. |  |

|  |
| --- |
| 3GPPPostal address3GPP support office address650 Route des Lucioles - Sophia AntipolisValbonne - FRANCETel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16Internethttps://www.3gpp.org |
| Copyright NotificationNo part may be reproduced except as authorized by written permission. The copyright and the foregoing restriction extend to reproduction in all media.© 2026, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).All rights reserved.UMTS™ is a Trade Mark of ETSI registered for the benefit of its members3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersGSM® and the GSM logo are registered and owned by the GSM Association |

Contents

Foreword 26

1 Scope 28

2 References 28

3 Definitions, symbols and abbreviations 29

3.1 Definitions 29

3.2 Symbols 30

3.3 Abbreviations 33

4 General 35

4.1 Relationship between minimum requirements and test requirements 35

4.2 Applicability of minimum requirements 35

4.3 Specification suffix information 35

5 Operating bands and channel arrangement 37

5.1 General 37

5.2 Operating bands 37

5.2A Operating bands for CA 39

5.2A.0 General 39

5.2A.1 Intra-band CA 39

5.2A.2 Inter-band CA 40

5.2A.2.1 Inter-band CA (two bands) 41

5.2A.2.2 Inter-band CA (three bands) 45

5.2A.2.3 Inter-band CA (four bands) 52

5.2A.2.4 Inter-band CA (five bands) 55

5.2A.2.5 Inter-band CA (six bands) 56

5.2B Operating bands for DC 56

5.2C Operating band combination for SUL 56

5.2D Operating bands for UL MIMO 59

5.2E Operating band for V2X 60

5.2E.1 V2X operating bands 60

5.2E.1A Sidelink CA operating bands 60

5.2E.1F Operating bands for Sidelink Unlicensed 61

5.2E.2 V2X operating bands for concurrent operation 61

5.2E.2F Operating bands for SL-U concurrent operation 62

5.2J Operating band for ATG 62

5.2J.1 General 62

5.2J.1A Operating band for ATG CA 62

5.2J.1A.1 Operating band for ATG intra-band CA 62

5.2J.1A.2 Operating band for ATG inter-band CA 62

5.2J.1D Operating band for ATG UL MIMO 63

5.2K Operating bands for Aerial UE 63

5.2M Operating bands for LP-WUS/WUR 63

5.3 UE channel bandwidth 63

5.3.1 General 63

5.3.2 Maximum transmission bandwidth configuration 65

5.3.3 Minimum guardband and transmission bandwidth configuration 65

5.3.4 RB alignment 67

5.3.5 UE channel bandwidth per operating band 67

5.3.6 Asymmetric channel bandwidths 74

5.3A UE channel bandwidth for CA 75

5.3A.1 General 75

5.3A.2 Maximum transmission bandwidth configuration for CA 75

5.3A.3 Minimum guardband and transmission bandwidth configuration for CA 75

5.3A.4 Void 77

5.3A.5 UE channel bandwidth per operating band for CA 77

5.3E Channel bandwidth for V2X 78

5.3E.1 General 78

5.3E.1A Channel bandwidth for Sidelink CA 79

5.3E.1F Channel bandwidth for Sidelink Unlicensed 79

5.3E.2 Channel bandwidth for V2X concurrent operation 80

5.3E.2F Channel bandwidth for SL-U concurrent operation 81

5.3I Channel bandwidth for (e)RedCap 82

5.3M UE channel bandwidth for LP-WUS/WUR 82

5.3M.1 General 82

5.3M.2 Maximum transmission bandwidth configuration 82

5.4 Channel arrangement 82

5.4.1 Channel spacing 82

5.4.1.1 Channel spacing for adjacent NR carriers 82

5.4.2 Channel raster 83

5.4.2.1 NR-ARFCN and channel raster 83

5.4.2.2 Channel raster to resource element mapping 83

5.4.2.3 Channel raster entries for each operating band 84

5.4.3 Synchronization raster 88

5.4.3.1 Synchronization raster and numbering 88

5.4.3.3 Synchronization raster entries for each operating band 89

5.4.4 TX–RX frequency separation 91

5.4A Channel arrangement for CA 92

5.4A.1 Channel spacing for CA 92

5.4A.2 Channel raster for CA 92

5.4A.3 Synchronization raster for CA 93

5.4A.4 Tx-Rx frequency separation for CA 93

5.4B Reserved 93

5.4C Reserved 93

5.4D Reserved 93

5.4E Channel arrangement for V2X 93

5.4E.1 Channel spacing 93

5.4E.1A Channel spacing for Sidelink CA 93

5.4E.1F Channel spacing for Sidelink Unlicensed 93

5.4E.2 Channel raster 93

5.4E.2.1 NR-ARFCN and channel raster 93

5.4E.2.1A Void 93

5.4E.2.1F Void 93

5.4E.2.2 Channel raster to resource element mapping 94

5.4E.2.2A Void 94

5.4E.2.2F Void 94

5.4E.2.3 Channel raster entries for each operating band 94

5.4E.2.3A Void 94

5.4E.2.3F Void 94

5.4E.3 Synchronization raster for V2X 95

5.4E.3A Synchronization raster for Sidelink CA 95

5.4E.3F Synchronization raster for Sidelink Unlicensed 95

5.4I Channel arrangement for (e)RedCap 95

5.4I.1 Channel spacing for (e)RedCap 95

5.4I.2 Channel raster for (e)RedCap 95

5.4I.2.1 NR-ARFCN and channel raster 95

5.4I.2.2 Channel raster to resource element mapping 95

5.4I.2.3 Channel raster entries for each operating band 95

5.4I.3 Synchronization raster for (e)RedCap 95

5.4I.4 Tx-Rx frequency separation for (e)RedCap 96

5.5 Void 97

5.5A Configurations for CA 97

5.5A.0 General 97

5.5A.1 Configurations for intra-band contiguous CA 98

5.5A.2 Configurations for intra-band non-contiguous CA 102

5.5A.3 Configurations for inter-band CA 107

5.5A.3.0 General 107

5.5A.3.1 Configurations for inter-band CA (two bands) 108

Table 5.5A.3.1-1a ~ Table 5.5A.3.1-1e 108

Table 5.5A.3.1-1f ~ Table 5.5A.3.1-1j 132

Table 5.5A.3.1-1k ~ Table 5.5A.3.1-1o 157

5.5A.3.2 Configurations for inter-band CA (three bands) 176

Table 5.5A.3.2-1a 176

Table 5.5A.3.2-1b 274

Table 5.5A.3.2-1c 330

5.5A.3.3 Configurations for inter-band CA (four bands) 356

Table 5.5A.3.3-1a 357

Table 5.5A.3.3-1b 448

5.5A.3.4 Configurations for inter-band CA (five bands) 510

5.5A.3.5 Configurations for inter-band CA (six bands) 551

5.5B Configurations for DC 553

5.5C Configurations for SUL 567

5.5D Reserved 580

5.5E Configurations for Sidelink 580

5.5E.1A Configurations for Sidelink CA 580

5.5E.1A.1 Configurations for Sidelink intra-band contiguous CA 580

5.5E.1A.2 Configurations for Sidelink intra-band non-contiguous CA 580

5.5J Configurations for ATG 581

5.5J.1A Configurations for ATG CA 581

5.5J.1A.1 Configurations for ATG intra-band contiguous CA 581

5.5J.1A.2 Configurations for ATG inter-band CA 581

6 Transmitter characteristics 582

6.1 General 582

6.1A General 582

6.1F General 582

6.1G (Reserved) 582

6.1H (Reserved) 582

6.1I (Reserved) 582

6.1J General 582

6.1K (Reserved) 583

6.1L (Reserved) 583

6.2 Transmitter power 583

6.2.1 UE maximum output power 583

6.2.1I Void 585

6.2.2 UE maximum output power reduction 585

6.2.3 UE additional maximum output power reduction 589

6.2.3.1 General 589

6.2.3.2 A-MPR for NS_04 594

6.2.3.3 A-MPR for NS_10 597

6.2.3.4 A-MPR for NS_05 and NS_05U 598

6.2.3.5 A-MPR for NS_40 601

6.2.3.6 A-MPR for NS_43 and NS_43U 602

6.2.3.7 A-MPR for NS_03 and NS_03U 604

6.2.3.8 A-MPR for NS_37 605

6.2.3.9 A-MPR for NS_38 606

6.2.3.10 A-MPR for NS_39 606

6.2.3.11 A-MPR for NS_41 607

6.2.3.12 A-MPR for NS_42 607

6.2.3.13 A-MPR for NS_18 608

6.2.3.14 A-MPR for NS_21 610

6.2.3.15 A-MPR for NS_24 612

6.2.3.16 A-MPR for NS_27 613

6.2.3.17 A-MPR for NS_46 615

6.2.3.18 A-MPR for NS_47 620

6.2.3.19 A-MPR for NS_50 622

6.2.3.20 A-MPR for NS_44 625

6.2.3.21 A-MPR for NS_12 626

6.2.3.22 A-MPR for NS_13 627

6.2.3.23 A-MPR for NS_14 628

6.2.3.24 A-MPR for NS_15 629

6.2.3.25 A-MPR for NS_45 632

6.2.3.26 A-MPR for NS_48 633

6.2.3.27 A-MPR for NS_49 635

6.2.3.28 A-MPR for NS_51 639

6.2.3.29 A-MPR for NS_07 640

6.2.3.30 A-MPR for NS_56 641

6.2.3.31 A-MPR for NS_35 642

6.2.3.32 A-MPR for NS_06 642

6.2.3.33 A-MPR for NS_17 643

6.2.3.34 A-MPR for NS_26 644

6.2.3.35 A-MPR for NS_36 644

6.2.4 Configured transmitted power 645

6.2A Transmitter power for CA 651

6.2A.0 General 651

6.2A.1 UE maximum output power for CA 652

6.2A.1.1 UE maximum output power for Intra-band contiguous CA 652

6.2A.1.2 UE maximum output power for Intra-band non-contiguous CA 653

6.2A.1.3 UE maximum output power for Inter-band CA 655

6.2A.1.4 Void 661

6.2A.1.5 Void 661

6.2A.2 UE maximum output power reduction for CA 662

6.2A.2.1 UE maximum output power reduction for Intra-band contiguous CA 662

6.2A.2.2 UE maximum output power reduction for Intra-band non-contiguous CA 667

6.2A.2.2.0 General 667

6.2A.2.2.1 MPR to meet -30dBm/MHz 668

6.2A.2.2.2 MPR to meet -13dBm/MHz 670

6.2A.2.3 UE maximum output power reduction for Inter-band CA 672

6.2A.2.4 Void 673

6.2A.3 UE additional maximum output power reduction for CA 673

6.2A.3.1 UE additional maximum output power reduction for Intra-band CA 673

6.2A.3.1.1 UE additional maximum output power reduction for Intra-band contiguous CA 673

6.2A.3.1.2 UE additional maximum output power reduction for Intra-band non-contiguous CA 680

6.2A.3.1.3 UE additional maximum output power reduction for Inter-band CA 684

6.2A.4 Configured output power for CA 686

6.2A.4.1 Configured transmitted power level 686

6.2A.4.1.1 Configured transmitted power for Intra-band contiguous CA 686

6.2A.4.1.2 Configured transmitted power for Intra-band non-contiguous CA 689

6.2A.4.1.3 Configured transmitted power for Inter-band CA 691

6.2A.4.1.4 Void 696

6.2A.4.2 ΔTIB,c for CA 696

6.2A.4.2.1 Void 696

6.2A.4.2.2 Void 696

6.2A.4.2.3 ΔTIB,c for Inter-band CA (two bands) 696

6.2A.4.2.4 ΔTIB,c for Inter-band CA (three bands) 700

6.2A.4.2.5 ΔTIB,c for Inter-band CA (four bands) 708

6.2A.4.2.6 ΔTIB,c for Inter-band CA (five bands) 713

6.2A.4.2.7 ΔTIB,c for Inter-band CA (six bands) 714

6.2B Transmitter power for NR-DC 714

6.2B.0 General 714

6.2B.1 UE maximum output power for NR-DC 715

6.2B.2 UE maximum output power reduction for NR-DC 716

6.2B.3 UE additional maximum output power reduction for NR-DC 717

6.2B.4.1 Configured transmitted power level for NR-DC 717

6.2B.4.2 ΔTIB,c for NR-DC 721

6.2C Transmitter power for SUL 721

6.2C.1 Configured transmitted power for SUL 721

6.2C.2 ΔTIB,c 722

6.2D Transmitter power for UL MIMO 725

6.2D.1 UE maximum output power for UL MIMO 725

6.2D.2 UE maximum output power reduction for UL MIMO 728

6.2D.3 UE additional maximum output power reduction for UL MIMO 730

6.2D.4 Configured transmitted power for UL MIMO 731

6.2E Transmitter power for V2X 732

6.2E.1 UE maximum output power for V2X 732

6.2E.1.1 General 732

6.2E.1.1A Void 733

6.2E.1.2 UE maximum output power for V2X concurrent operation 733

6.2E.1A UE maximum output power for Sidelink CA 735

6.2E.1F UE maximum output power for Sidelink Unlicensed 735

6.2E.1F.1 General 735

6.2E.1.2F Void 736

6.2E.1F.2 UE Maximum output power for SL-U concurrent operation 736

6.2E.2 UE maximum output power reduction for V2X 737

6.2E.2.1 General 737

6.2E.2.1A MPR for sidelink CA 737

6.2E.2.1A.1 MPR for sidelink intra-band contiguous CA 737

6.2E.2.1A.2 MPR for sidelink intra-band non-contiguous CA 740

6.2E.2.1A.2.0 General 740

6.2E.2.1A.2.1 MPR with indicating dualPA-Architecture supported 741

6.2E.2.1A.2.2 MPR without indicating dualPA-Architecture supported 742

6.2E.2.2 MPR for Power class 2 and Power class 3 V2X UE 743

6.2E.2.3 MPR for Power class 2 and Power class 3 V2X concurrent operation 745

6.2E.2.4 MPR for Power class 1 UE in Band n14 747

6.2E.2F UE maximum output power reduction for Sidelink Unlicensed 748

6.2E.2F.1 General 748

6.2E.2F.2 MPR for NR SL-U UE 748

6.2E.2F.3 MPR for SL-U concurrent operation 750

6.2E.3 UE additional maximum output power reduction for V2X 750

6.2E.3.1 General 750

6.2E.3.2 A-MPR for V2X UE by NS_33 751

6.2E.3.2A A-MPR for sidelink CA by NS_33 756

6.2E.3.2A.1 A-MPR for sidelink intra-band non-contiguous CA 756

6.2E.3.2A.1.1 A-MPR for SLCA_NC_NS_33 (SLCA_n47(2A)) 756

6.2E.3.3 A-MPR for Power class 3 V2X UE by NS_52 760

6.2E.3.4 A-MPR for V2X concurrent operation 762

6.2E.3F UE additional maximum output power reduction for Sidelink Unlicensed 762

6.2E.3F.1 General 762

6.2E.3F.2 A-MPR for NS_31 763

6.2E.3F.3 Void 764

6.2E.3F.4 Void 764

6.2E.3F.5 Void 764

6.2E.3F.6 A-MPR for NS_61 764

6.2E.3F.7 A-MPR for SL-U concurrent operation 765

6.2E.3F.8 A-MPR for NS_28 766

6.2E.3F.9 A-MPR for NS_29 767

6.2E.3F.10 A-MPR for NS_30 768

6.2E.3F.11 A-MPR for NS_54 770

6.2E.3F.12 A-MPR for NS_64 771

6.2E.3F.13 A-MPR for NS_65 773

6.2E.3F.14 A-MPR for NS_66 774

6.2E.3F.15 A-MPR for NS_67 or NS_71 775

6.2E.3F.16 A-MPR for NS_68 776

6.2E.3F.17 A-MPR for NS_69 777

6.2E.4 Configured transmitted power for V2X 778

6.2E.4.1 General 778

6.2E.4.2 Configured transmitted power for inter-band V2X concurrent operation 779

6.2E.4.3 Configured transmitted power for intra-band V2X concurrent operation 780

6.2E.4A Configured transmitted power for Sidelink CA 782

6.2E.4F Configured transmitted power for Sidelink Unlicensed 783

6.2E.4F.1 General 783

6.2E.4F.2 Configured transmitted power for inter-band concurrent operation 784

6.2F Transmitter power for shared spectrum channel access 785

6.2F.1 UE maximum output power 785

6.2F.1A UE maximum output power for CA 786

6.2F.1A.1 UE maximum output power for inter-band CA 786

6.2F.1A.2 UE maximum output power for intra-band contiguous CA 787

6.2F.1A.2.1 Additional requirements for transmit power density for intra-band contiguous CA for CA_NS_53 787

6.2F.1A.2.2 Additional requirements for transmit power density for intra-band contiguous CA for CA_NS_54 787

6.2F.1B UE maximum output power for NR-DC 788

6.2F.1D UE maximum output power for UL MIMO 788

6.2F.2 UE maximum output power reduction 788

6.2F.2A UE maximum output power reduction for CA 791

6.2F.2A.1 UE maximum output power reduction for inter-band CA 791

6.2F.2A.2 UE maximum output power reduction for intra-band contiguous CA 791

6.2F.2D UE maximum output power reduction for UL MIMO 794

6.2F.3 UE additional maximum output power reduction 794

6.2F.3.1 General 794

6.2F.3.2 A-MPR for NS_28 795

6.2F.3.3 A-MPR for NS_29 796

6.2F.3.4 A-MPR for NS_30 797

6.2F.3.5 A-MPR for NS_31 798

6.2F.3.6 A-MPR for NS_53 799

6.2F.3.7 A-MPR for NS_54 799

6.2F.3.8 A-MPR for NS_58 800

6.2F.3.9 A-MPR for NS_59 801

6.2F.3.10 A-MPR for NS_60 802

6.2F.3.11 A-MPR for NS_61 803

6.2F.3.12 A-MPR for NS_63 804

6.2F.3.13 A-MPR for NS_64 805

6.2F.3.14 A-MPR for NS_65 805

6.2F.3.15 A-MPR for NS_66 806

6.2F.3.16 A-MPR for "NS_67" or "NS_71" 806

6.2F.3.17 A-MPR for NS_68 807

6.2F.3.18 A-MPR for NS_69 807

6.2F.3A UE additional maximum output power reduction for CA 808

6.2F.3A.1 UE additional maximum output power reduction for inter-band CA 808

6.2F.3A.2 UE additional maximum output power reduction for intra-band CA 808

6.2F.3A.2.0 General 808

6.2F.3A.2.1 UE additional maximum output power reduction for intra-band contiguous CA 808

6.2F.3A.2.2 A-MPR for CA_NS_53 810

6.2F.3A.2.3 A-MPR for CA_NS_54 811

6.2F.3D UE additional maximum output power reduction for UL MIMO 811

6.2F.4 Configured transmitted power 811

6.2F.4D Configured transmitted power UL MIMO 811

6.2G Transmitter power for Tx Diversity 812

6.2G.1 UE maximum output power for Tx Diversity 812

6.2G.2 UE maximum output power reduction for Tx Diversity 812

6.2G.3 UE additional maximum output power reduction for Tx Diversity 812

6.2G.4 Configured transmitted power for Tx Diversity 812

6.2H Transmitter power for CA with UL MIMO 813

6.2H.1 Transmitter power for intra-band UL contiguous CA with UL MIMO 813

6.2H.1.1 UE maximum output power for intra-band UL contiguous CA with UL MIMO 813

6.2H.1.2 UE maximum output power reduction for intra-band UL contiguous CA with UL MIMO 814

6.2H.1.3 UE additional maximum output power reduction for intra-band UL contiguous CA with UL MIMO 814

6.2H.1.4 Configured transmitted power for intra-band UL contiguous CA with UL MIMO 814

6.2H.2 Void 815

6.2H.3 Transmitter power for inter-band UL CA with UL MIMO 815

6.2H.3.1 UE maximum output power for inter-band UL CA with UL MIMO 815

6.2H.3.2 UE maximum output power reduction for inter-band UL CA with UL MIMO 818

6.2H.3.3 UE additional maximum output power reduction for inter-band UL CA with UL MIMO 818

6.2H.3.4 Configured transmitted power for inter-band UL CA with UL MIMO 818

6.2I Transmitter power for (e)RedCap 819

6.2I.1 Maximum output power for RedCap 819

6.2J Transmitter power for ATG 819

6.2J.0 Reserved 819

6.2J.0D General 819

6.2J.1 UE maximum output power for ATG 819

6.2J.1A UE maximum output power for ATG CA 819

6.2J.1A.1 UE maximum output power for ATG intra-band contiguous CA 819

6.2J.1A.2 UE maximum output power for ATG inter-band CA 820

6.2J.1A.3 (void) 820

6.2J.1D UE maximum output power for ATG UL MIMO 820

6.2J.2 Configured transmitted power for ATG 821

6.2J.2D Configured transmitted power for UL MIMO 821

6.2K Transmitter power for Aerial UE 822

6.2K.1 Maximum output power for Aerial UE 822

6.2K.2 Maximum output power reduction for Aerial UE 822

6.2K.3 Additional maximum output power reduction for Aerial UE 822

6.2K.3.1 General 822

6.2K.3.2 A-MPR for NS_UAV_44 823

6.2K.3.3 A-MPR for NS_UAV_70 824

6.2K.4 Configured transmitted power for Aerial UE 825

6.2L Transmitter power for CA with Tx Diversity 826

6.2L.1 Void 826

6.2L.2 Void 826

6.2L.3 Transmitter power for inter-band UL CA with Tx Diversity 826

6.2L.3.1 UE maximum output power for inter-band UL CA with Tx Diversity 826

6.2L.3.2 UE maximum output power reduction for inter-band UL CA with Tx Diversity 827

6.2L.3.3 UE additional maximum output power reduction for inter-band UL CA with Tx Diversity 828

6.2L.3.4 Configured transmitted power for inter-band UL CA with Tx Diversity 828

6.3 Output power dynamics 828

6.3.1 Minimum output power 828

6.3.2 Transmit OFF power 828

6.3.3 Transmit ON/OFF time mask 829

6.3.3.1 General 829

6.3.3.2 General ON/OFF time mask 829

6.3.3.3 Transmit power time mask for slot and short or long subslot boundaries 830

6.3.3.4 PRACH time mask 830

6.3.3.5 Void 831

6.3.3.6 SRS time mask 831

6.3.3.7 PUSCH-PUCCH and PUSCH-SRS time masks 833

6.3.3.8 Transmit power time mask for consecutive slot or long subslot transmission and short subslot transmission boundaries 834

6.3.3.9 Transmit power time mask for consecutive short subslot transmissions boundaries 835

6.3.4 Power control 835

6.3.4.1 General 835

6.3.4.2 Absolute power tolerance 835

6.3.4.3 Relative power tolerance 836

6.3.4.4 Aggregate power tolerance 836

6.3A Output power dynamics for CA 837

6.3A.1 Minimum output power for CA 837

6.3A.1.1 Minimum output power for intra-band contiguous CA 837

6.3A.1.2 Minimum output power for intra-band non-contiguous CA 837

6.3A.1.3 Minimum output power for inter-band CA 837

6.3A.1.4 Void 837

6.3A.2 Transmit OFF power for CA 837

6.3A.2.1 Transmit OFF power for intra-band contiguous CA 837

6.3A.2.2 Transmit OFF power for intra-band non-contiguous CA 837

6.3A.2.3 Transmit OFF power for inter-band CA 837

6.3A.2.4 Void 838

6.3A.3 Transmit ON/OFF time mask for CA 838

6.3A.3.1 Transmit ON/OFF time mask for intra-band contiguous CA 838

6.3A.3.2 Transmit ON/OFF time mask for intra-band non-contiguous CA 838

6.3A.3.3 Transmit ON/OFF time mask for inter-band CA 838

6.3A.3.3.1 General 838

6.3A.3.3.2 Time mask for switching between two uplink carriers 839

6.3A.3.3.3 Time mask for switching between two uplink carriers with two transmit antenna connectors 840

6.3A.3.3.4 Time mask for switching between one uplink band with one transmit antenna connector and one uplink band with two transmit antenna connectors 841

6.3A.3.3.5 Time mask for switching between two uplink bands with two transmit antenna connectors 843

6.3A.3.3.6 Time mask for switching across up to four uplink bands 844

6.3A.3.3.6a Additional requirements for three-band switching with dual TAG 848

6.3A.3.3.7 Time mask for low NR band carrier aggregation via switching 848

6.3A.3.3.8 Time mask for switching between two uplink bands with three transmit antenna connectors and maximum two transmit antenna connectors for each band 848

6.3A.3.4 Void 850

6.3A.4 Power control for CA 850

6.3A.4.1 Power control for intra-band contiguous CA 850

6.3A.4.1.1 Absolute power tolerance 850

6.3A.4.1.2 Relative power tolerance 850

6.3A.4.1.3 Aggregate power control tolerance 850

6.3A.4.2 Power control for intra-band non-contiguous CA 850

6.3A.4.2.1 Absolute power tolerance 850

6.3A.4.2.1.1  Minimum requirements 851

6.3A.4.2.2 Relative power tolerance 851

6.3A.4.2.2.1 Minimum requirements 851

6.3A.4.2.3 Aggregate power control tolerance 851

6.3A.4.3 Power control for inter-band CA 851

6.3A.4.4 Void 851

6.3B Output power dynamics for NR-DC 851

6.3C Output power dynamics for SUL 852

6.3C.1 Void 852

6.3C.2 Void 852

6.3C.3 Transmit ON/OFF time mask for SUL 852

6.3C.3.0 General 852

6.3C.3.1 Time mask for switching between two uplink carriers 852

6.3C.3.2 Time mask for switching between two uplink carriers with two transmit antenna connectors 853

6.3C.3.3 Time mask for switching between one uplink band with one transmit antenna connector and one uplink band with two transmit antenna connectors 854

6.3C.3.4 Time mask for switching between two uplink bands with two transmit antenna connectors 856

6.3C.3.5 Time mask for switching across up to four uplink bands 857

6.3C.3.5a Additional requirements for three-band switching with dual TAG 861

6.3D Output power dynamics for UL MIMO 861

6.3D.1 Minimum output power for UL MIMO 861

6.3D.2 Transmit OFF power for UL MIMO 861

6.3D.3 Transmit ON/OFF time mask for UL MIMO 861

6.3D.4 Power control for UL MIMO 861

6.3E Output power dynamics for V2X 862

6.3E.1 Minimum output power for V2X 862

6.3E.1.1 General 862

6.3E.1.1A Minimum output power for sidelink CA 862

6.3E.1.2 Minimum output power for V2X concurrent operation 862

6.3E.1F Minimum output power for Sidelink Unlicensed 862

6.3E.1F.1 Minimum output power for SL-U concurrent operation 863

6.3E.2 Transmit OFF power for V2X 863

6.3E.2.1 General 863

6.3E.2.1A Transmit OFF power for sidelink CA 863

6.3E.2.2 Transmit OFF power for V2X concurrent operation 863

6.3E.2F Transmit OFF power for Sidelink Unlicensed 863

6.3E.2F.1 Transmit OFF power for SL-U concurrent operation 864

6.3E.3 Transmit ON/OFF time mask for V2X 864

6.3E.3.1 General 864

6.3E.3.1A Transmit ON/OFF time mask for sidelink CA 864

6.3E.3.2 General time mask 864

6.3E.3.3 S-SSB time mask 864

6.3E.3.4 Transmit ON/OFF time mask for V2X concurrent operation 865

6.3E.3F Transmit ON/OFF time mask for Sidelink Unlicensed 866

6.3E.3F.1 General 866

6.3E.3F.2 General ON/OFF time mask 866

6.3E.3F.3 S-SSB time mask 867

6.3E.3F.4 Transmit ON/OFF time mask for NR SL-U concurrent operation 867

6.3E.4 Power control for V2X 867

6.3E.4.1 General 867

6.3E.4.1A Power control for sidelink CA 867

6.3E.4.2 Absolute power tolerance 867

6.3E.4.3 Power control for V2X concurrent operation 868

6.3E.4F Power control for Sidelink Unlicensed 868

6.3E.4F.1 General 868

6.3E.4F.2 Absolute power tolerance 868

6.3E.4F.3 Power control for SL-U concurrent operation 868

6.3F Output power dynamics for shared spectrum channel access 868

6.3F.1 Minimum output power 868

6.3F.2 Transmit OFF power 868

6.3F.3 Transmit ON/OFF time mask 868

6.3F.3.1 General 868

6.3F.3.2 General ON/OFF time mask 868

6.3F.3A General ON/OFF mask for CA 869

6.3F.3A.1 General ON/OFF mask for inter-band CA 869

6.3F.4 Power control 869

6.3F.4.1 General 869

6.3F.4.2 Absolute power tolerance 869

6.3F.4.3 Relative power tolerance 869

6.3F.4.4 Aggregate power tolerance 869

6.3F.4A Power control for inter-band CA 869

6.3G Output power dynamics for Tx Diversity 870

6.3G.1 Minimum output power for Tx Diversity 870

6.3G.2 Transmit OFF power for Tx Diversity 870

6.3G.3 Transmit ON/OFF time mask for Tx Diversity 870

6.3G.4 Power control for Tx Diversity 870

6.3H Output power dynamics for CA with UL MIMO 870

6.3H.1 Output power dynamics for intra-band UL contiguous CA with UL MIMO 870

6.3H.1.1 Minimum output power for intra-band UL contiguous CA with UL MIMO 870

6.3H.1.2 Transmit OFF power for intra-band UL contiguous CA with UL MIMO 870

6.3H.1.3 Transmit ON/OFF time mask for intra-band UL contiguous CA with UL MIMO 870

6.3H.1.4 Power control for intra-band UL contiguous CA with UL MIMO 871

6.3H.3 Output power dynamics for inter-band UL CA with UL MIMO 871

6.3H.3.1 Minimum output power for inter-band UL CA with UL MIMO 871

6.3H.3.2 Transmit OFF power for inter-band UL CA with UL MIMO 871

6.3H.3.3 Transmit ON/OFF time mask for inter-band UL CA with UL MIMO 871

6.3H.3.4 Power control for inter-band UL CA with UL MIMO 871

6.3I (Reserved) 871

6.3J Output power dynamics for ATG 871

6.3J.1 Minimum output power for ATG 871

6.3J.1D Minimum output power for ATG UL MIMO 872

6.3J.2 Transmit OFF power for ATG 872

6.3J.2D Transmit OFF power for ATG UL MIMO 872

6.3J.3 Transmit ON/OFF time mask for ATG 872

6.3J.3D Transmit ON/OFF time mask for ATG UL MIMO 872

6.3J.4 Power control for ATG 873

6.3J.4D Power control for ATG UL MIMO 873

6.3K (Reserved) 873

6.3L Output power dynamics for CA with Tx Diversity 873

6.3L.1 Void 873

6.3L.2 Void 873

6.3L.3 Output power dynamics for inter-band UL CA with Tx Diversity 873

6.3L.3.1 Minimum output power for inter-band UL CA with Tx Diversity 873

6.3L.3.2 Transmit OFF power for inter-band UL CA with Tx Diversity 873

6.3L.3.3 Transmit ON/OFF time mask for inter-band UL CA with Tx Diversity 873

6.3L.3.4 Power control for inter-band UL CA with Tx Diversity 874

6.4 Transmit signal quality 874

6.4.1 Frequency error 874

6.4.2 Transmit modulation quality 874

6.4.2.0 General 874

6.4.2.1 Error Vector Magnitude 874

6.4.2.1a Error Vector Magnitude including symbols with transient period 875

6.4.2.2 Carrier leakage 876

6.4.2.3 In-band emissions 876

6.4.2.4 EVM equalizer spectrum flatness 878

6.4.2.4.1 Requirements for Pi/2 BPSK modulation with powerBoosting-pi2BPSK capability 879

6.4.2.4.2 Requirements for Pi/2 BPSK and QPSK modulation with powerBoosting-pi2BPSK-QPSK-Modified-r18 capability 880

6.4.2.5 Phase continuity requirements for DMRS bundling 881

6.4A Transmit signal quality for CA 882

6.4A.1 Frequency error for CA 882

6.4A.1.1 Frequency error for intra-band contiguous CA 882

6.4A.1.2 Frequency error for intra-band non-contiguous CA 882

6.4A.1.3 Frequency error for inter-band CA 882

6.4A.1.4 Void 882

6.4A.2 Transmit modulation quality for CA 882

6.4A.2.1 Transmit modulation quality for intra-band contiguous CA 882

6.4A.2.1.0 General 882

6.4A.2.1.1 Error Vector Magnitude 883

6.4A.2.1.2 In-band emissions 883

6.4A.2.1.3 Carrier leakage 886

6.4A.2.2 Transmit modulation quality for intra-band non-contiguous CA 886

6.4A.2.2.0 General 886

6.4A.2.2.1 Error Vector Magnitude 886

6.4A.2.2.2 In-band emissions 887

6.4A.2.2.3 Carrier leakage 887

6.4A.2.3 Transmit modulation quality for inter-band CA 887

6.4A.2.4 Void 888

6.4B Transmit signal quality for NR-DC 888

6.4C Transmit signal quality for SUL 888

6.4D Transmit signal quality for UL MIMO 888

6.4D.0 General 888

6.4D.1 Frequency error for UL MIMO 888

6.4D.2 Transmit modulation quality for UL MIMO 889

6.4D.2.0 General 889

6.4D.2.1 Error Vector Magnitude 889

6.4D.2.2 Carrier leakage 889

6.4D.2.3 In-band emissions 889

6.4D.2.4 EVM equalizer spectrum flatness for UL MIMO 889

6.4D.3 Time alignment error for UL MIMO 889

6.4D.4 Requirements for coherent UL MIMO 890

6.4E Transmit signal quality for V2X 890

6.4E.1 Frequency error for V2X 890

6.4E.1.1 General 890

6.4E.1.1A Frequency error for sidelink CA 891

6.4E.1.2 Frequency error for V2X concurrent operation 891

6.4E.1F Frequency error for Sidelink Unlicensed 891

6.4E.1F.1 Frequency error for SL-U concurrent operation 891

6.4E.2 Transmit modulation quality for V2X 891

6.4E.2.1 General 891

6.4E.2.2 Error Vector Magnitude for V2X 891

6.4E.2.2A Error Vector Magnitude for sidelink CA 891

6.4E.2.3 Carrier leakage for V2X 891

6.4E.2.3A Carrier leakage for sidelink CA 892

6.4E.2.4 In-band emissions for V2X 892

6.4E.2.4A In-band emissions for sidelink CA 892

6.4E.2.5 EVM equalizer spectrum flatness for V2X 892

6.4E.2.6 Transmit modulation quality for V2X concurrent operation 892

6.4E.2F Transmit modulation quality for Sidelink Unlicensed 892

6.4E.2F.0 General 892

6.4E.2F.1 Error Vector Magnitude 892

6.4E.2F.2 Carrier leakage 892

6.4E.2F.3 In-band emissions 893

6.4E.2F.4 EVM equalizer spectrum flatness 893

6.4E.2F.5 Transmit modulation quality for SL-U concurrent operation 893

6.4F Transmit signal quality for shared spectrum channel access 893

6.4F.1 Frequency error 893

6.4F.2 Transmit modulation quality 893

6.4F.2.0 General 893

6.4F.2.1 Error Vector Magnitude 893

6.4F.2.2 Carrier leakage 893

6.4F.2.3 In-band emissions 893

6.4F.2.4 EVM equalizer spectrum flatness 894

6.4F.2A Transmit modulation quality for CA 894

6.4F.2A.1 Transmit modulation quality for inter-band CA 894

6.4G Transmit signal quality for Tx Diversity 895

6.4G.1 Frequency error for Tx Diversity 895

6.4G.2  Transmit modulation quality for Tx Diversity 895

6.4G.2.0 General 895

6.4H Transmit signal quality for CA with UL MIMO 896

6.4H.1 Transmit signal quality for intra-band UL contiguous CA with UL MIMO 896

6.4H.1.1 Frequency error for intra-band UL contiguous CA with UL MIMO 896

6.4H.1.2 Transmit modulation quality for intra-band UL contiguous CA with UL MIMO 896

6.4H.1.2.0 General 896

6.4H.1.2.1 Error Vector Magnitude 896

6.4H.1.2.2 Carrier leakage 896

6.4H.1.2.3 In-band emissions 896

6.4H.1.3 Time alignment error for intra-band UL contiguous CA with UL MIMO 897

6.4H.1.4 Coherent UL MIMO requirement for intra-band UL contiguous CA with UL MIMO 897

6.4H.2 Void 897

6.4H.3 Transmit signal quality for inter-band UL CA with UL MIMO 897

6.4H.3.1 Frequency error for inter-band UL CA with UL MIMO 897

6.4H.3.2 Transmit modulation quality for inter-band UL CA with UL MIMO 897

6.4I (Reserved) 897

6.4J Transmit signal quality for ATG 897

6.4J.0 Reserved 897

6.4J.0D General 897

6.4J.1 Frequency error for ATG 898

6.4J.2 Transmit modulation quality for ATG 898

6.4J.2D Transmit modulation quality for ATG UL MIMO 898

6.4J.2D.0 General 898

6.4J.2D.1 Error Vector Magnitude for ATG UL MIMO 898

6.4J.2D.2 Carrier leakage for ATG UL MIMO 898

6.4J.2D.3 In-band emissions for ATG UL MIMO 898

6.4J.2D.4 EVM equalizer spectrum flatness for ATG UL MIMO 898

6.4J.3D Time alignment error for ATG 899

6.4J.3D.1 Time alignment error for ATG UL MIMO 899

6.4J.3D Requirement for ATG coherent UL MIMO 899

6.4K (Reserved) 899

6.4L Transmit signal quality for CA with Tx Diversity 899

6.4L.1 Void 899

6.4L.2 Void 899

6.4L.3 Transmit signal quality for inter-band UL CA with Tx Diversity 899

6.4L.3.1 Frequency error for inter-band UL CA with Tx Diversity 899

6.4L.3.2 Transmit modulation quality for inter-band UL CA with Tx Diversity 899

6.5 Output RF spectrum emissions 899

6.5.1 Occupied bandwidth 899

6.5.2 Out of band emission 900

6.5.2.1 General 900

6.5.2.2 Spectrum emission mask 900

6.5.2.3 Additional spectrum emission mask 900

6.5.2.3.1 Requirements for network signalling value "NS_35" 900

6.5.2.3.2 Requirements for network signalling value "NS_04" 901

6.5.2.3.3 Requirements for network signalling values "NS_03" and “NS_03U” 902

6.5.2.3.4 Requirements for network signalling value "NS_06" or “NS_07” 902

6.5.2.3.5 Void 903

6.5.2.3.6 Void 903

6.5.2.3.7 Void 903

6.5.2.3.8 Requirements for network signalling value "NS_27" 903

6.5.2.3.9 Requirements for network signalling value "NS_21" 903

6.5.2.4 Adjacent channel leakage ratio 904

6.5.2.4.1 NR ACLR 904

6.5.2.4.2 UTRA ACLR 905

6.5.3 Spurious emissions 905

6.5.3.0 General 905

6.5.3.1 General spurious emissions 906

6.5.3.2 Spurious emissions for UE co-existence 906

6.5.3.3 Additional spurious emissions 914

6.5.3.3.1 Requirement for network signalling value "NS_04" 915

6.5.3.3.2 Requirement for network signalling value "NS_17" 915

6.5.3.3.3 Requirement for network signalling value "NS_18" 915

6.5.3.3.4 Requirement for network signalling values "NS_05" and “NS_05U” 915

6.5.3.3.5 Requirement for network signalling values "NS_43" and “NS_43U” 916

6.5.3.3.6 Requirement for network signalling value "NS_37" 916

6.5.3.3.7 Requirement for network signalling value "NS_38" 916

6.5.3.3.8 Requirement for network signalling value "NS_39" 917

6.5.3.3.9 Requirement for network signalling value "NS_40" 917

6.5.3.3.10 Requirement for network signalling value "NS_41" 917

6.5.3.3.11 Requirement for network signalling value "NS_42" 917

6.5.3.3.12 Requirement for network signalling value "NS_21" 918

6.5.3.3.13 Requirement for network signalling value "NS_24" 918

6.5.3.3.14 Requirement for network signalling value "NS_27" 918

6.5.3.3.15 Requirement for network signalling value "NS_47" 919

6.5.3.3.16 Requirement for network signalling value "NS_50" 919

6.5.3.3.17 Requirement for network signalling value "NS_12" 919

6.5.3.3.18 Requirement for network signalling value "NS_13" 920

6.5.3.3.19 Requirement for network signalling value "NS_14" 920

6.5.3.3.20 Requirement for network signalling value "NS_15" 920

6.5.3.3.21 Requirement for network signalling value "NS_45" 920

6.5.3.3.22 Requirement for network signalling values "NS_48" and "NS_51" 921

6.5.3.3.23 Requirement for network signalling value "NS_49" 921

6.5.3.3.24 Requirement for network signalling value "NS_44" 921

6.5.3.3.25 Requirement for network signalling value "NS_46" 922

6.5.3.3.26 Requirement for network signalling value "NS_07" 922

6.5.3.3.27 Requirement for network signalling value “NS_56” 922

6.5.3.3.28 Requirement for network signalling value “NS_62” 923

6.5.3.3.29 Requirement for network signalling value “NS_26” 923

6.5.3.3.30 Requirement for network signalling value “NS_36” 923

6.5.4 Transmit intermodulation 924

6.5A Output RF spectrum emissions for CA 924

6.5A.0 General 924

6.5A.1 Occupied bandwidth for CA 924

6.5A.1.1 Void 924

6.5A.1.1a Occupied bandwidth for Intra-band contiguous CA 924

6.5A.1.2 Occupied bandwidth for Intra-band non-contiguous CA 925

6.5A.1.3 Occupied bandwidth for Inter-band CA 925

6.5A.2 Out of band emission for CA 925

6.5A.2.1 General 925

6.5A.2.2 Spectrum emission mask 925

6.5A.2.2.1 Spectrum emission mask for intra-band contiguous CA 925

6.5A.2.2.2 Spectrum emission mask for intra-band non-contiguous CA 925

6.5A.2.2.3 Spectrum emission mask for Inter-band CA 926

6.5.A.2.2.4 Void 926

6.5A.2.3 Additional spectrum emission mask for CA 926

6.5A.2.3.1 Additional spectrum emission mask for intra-band contiguous CA 926

6.5A.2.3.2 Additional spectrum emission mask for Intra-band non-contiguous CA 927

6.5A.2.3.3 Additional spectrum emission mask for Inter-band CA 927

6.5A.2.4 Adjacent channel leakage ratio 927

6.5A.2.4.1 NR ACLR 927

6.5A.2.4.2 UTRA ACLR 929

6.5A.3 Spurious emission for CA 929

6.5A.3.1 General spurious emissions 929

6.5A.3.2 Spurious emissions for UE co-existence 930

6.5A.3.2.0 General 930

6.5A.3.2.1 Spurious emissions for UE co-existence for intra-band contiguous CA 931

6.5A.3.2.2 Spurious emissions for UE co-existence for intra-band non-contiguous CA 932

6.5A.3.2.3 Spurious emissions for UE co-existence for Inter-band CA 933

6.5A.3.2.4 Void 938

6.5A.3.2.5 Void 938

6.5A.3.2.6 Void 938

6.5A.3.3 Additional spurious emissions for CA 938

6.5A.3.3.1 Additional spurious emissions for intra-band contiguous  CA 938

6.5A.3.3.2 Additional spurious emissions for intra-band non-contiguous CA 939

6.5A.4 Transmit intermodulation for CA 939

6.5A.4.2.1 Transmit intermodulation for intra-band contiguous CA 939

6.5A.4.2.2 Void 940

6.5B Output RF spectrum emissions for NR-DC 940

6.5D Output RF spectrum emissions for UL MIMO 940

6.5D.1 Occupied bandwidth for UL MIMO 940

6.5D.2 Out of band emission for UL MIMO 940

6.5D.3 Spurious emission for UL MIMO 941

6.5D.4 Transmit intermodulation for UL MIMO 941

6.5E Output RF spectrum emissions for V2X 941

6.5E.1 Occupied bandwidth for V2X 941

6.5E.1.1 General 941

6.5E.1.1A Occupied bandwidth for sidelink CA 942

6.5E.1.2 Occupied bandwidth for V2X concurrent operation 942

6.5E.1F Occupied bandwidth for Sidelink Unlicensed 942

6.5E.1F.1 Occupied bandwidth for SL-U concurrent operation 942

6.5E.2 Out of band emission for V2X 942

6.5E.2.1 General 942

6.5E.2.2 Spectrum emission mask 942

6.5E.2.2.1 General 942

6.5E.2.2.1A Spectrum emission mask for sidelink CA 942

6.5E.2.2.2 Spectrum emission mask for V2X concurrent operation 943

6.5E.2.3 Additional Spectrum emission mask 943

6.5E.2.3.1 Requirements for network signalling value "NS_33" 943

6.5E.2.3.1A Requirements for network or pre-configured signalling value “SLCA_NC_NS_33” 943

6.5E.2.3.2 Requirements for network signalling value "NS_52" 943

6.5E.2.3.3 Requirements for network signalling value "NS_06" 944

6.5E.2.4 Adjacent channel leakage ratio 944

6.5E.2.4.1 General 944

6.5E.2.4.1A ACLR for sidelink CA 944

6.5E.2.4.2 ACLR for V2X concurrent operation 944

6.5E.2F Out of band emission for Sidelink Unlicensed 945

6.5E.2F.1 General 945

6.5E.2F.2 Spectrum emission mask for operation with shared spectrum channel access 945

6.5E.2F.2.1 Spectrum emission mask for SL-U concurrent operation 945

6.5E.2F.3 Additional spectrum emission mask 945

6.5E.2F.4 Adjacent channel leakage ratio 945

6.5E.2F.4.1 Adjacent channel leakage ratio for SL-U concurrent operation 945

6.5E.3 Spurious emissions for V2X 945

6.5E.3.1 General spurious emissions 945

6.5E.3.1A Spurious emissions for sidelink CA 945

6.5E.3.2 Spurious emissions for UE co-existence 945

6.5E.3.2A Spurious emissions band UE co-existence for sidelink CA 946

6.5E.3.3 Spurious emissions for UE co-existence for V2X concurrent operation 946

6.5E.3.4 Additional spurious emissions requirements for V2X 947

6.5E.3.4.1 General 947

6.5E.3.4.2 Requirements for network signalling value "NS_33" 947

6.5E.3.4A Additional spurious emissions requirements for sidelink CA 947

6.5E.3.4A.1 General 947

6.5E.3.4A.2 Requirements for network signalling value "SLCA_NC_NS_33" 948

6.5E.3.4.3 Void 948

6.5E.3F Spurious emissions for Sidelink Unlicensed 948

6.5E.3F.0 General 948

6.5E.3F.1 General spurious emissions 948

6.5E.3F.2 Spurious emissions for UE co-existence 948

6.5E.3F.2.1 Spurious emissions for UE co-existence for SL-U concurrent operation 949

6.5E.3F.3 Additional spurious emissions 949

6.5E.3F.3.0 General 949

6.5E.4 Transmit intermodulation 949

6.5E.4.1 General 949

6.5E.4.1A Transmit intermodulation for sidelink CA 949

6.5E.4.2 Transmit intermodulation for V2X concurrent operation 949

6.5F Output RF spectrum emissions for shared spectrum channel access 949

6.5F.1 Occupied bandwidth 949

6.5F.2 Out of band emission 950

6.5F.2.1 General 950

6.5F.2.2 Spectrum emission mask for operation with shared spectrum channel access 950

6.5F.2.2.0 General 950

6.5F.2.2.1 Spectrum emission mask for non-transmitted channels 950

6.5F.2.3 Additional spectrum emission mask 951

6.5F.2.4 Adjacent channel leakage ratio 951

6.5F.2.4.0 General 951

6.5F.2.4.1 Shared spectrum channel access ACLR 951

6.5F.2.4.2 Additional requirement for network signalled value "NS_29" 951

6.5F.2A Out of band emission for CA 952

6.5F.2A.1 Spectrum emission mask for CA 952

6.5F.2A.1.1 Spectrum emission mask for Inter-band CA 952

6.5F.2A.1.2 Spectrum emission mask for Intra-band contiguous CA 952

6.5F.2A.1.2.1 General 952

6.5F.2A.1.2.2 Intra-band contiguous CA spectrum emission mask for non-transmitted channels 953

6.5F.2A.2 Adjacent channel leakage ratio for CA 953

6.5F.2A.2.1 Adjacent channel leakage ratio for inter-band CA 953

6.5F.2A.2.2 Adjacent channel leakage ratio for intra-band contiguous CA 953

6.5F.3 Spurious emissions 953

6.5F.3.0 General 953

6.5F.3.1 General spurious emissions 954

6.5F.3.2 Spurious emissions for UE co-existence 954

6.5F.3.3 Additional spurious emissions 954

6.5F.3.3.0 General 954

6.5F.3.3.1 Requirement for network signalling value "NS_28" 954

6.5F.3.3.2 Requirement for network signalling value "NS_29" 954

6.5F.3.3.3 Requirement for network signalling value "NS_30" 956

6.5F.3.3.4 Requirement for network signalling value "NS_31" 957

6.5F.3.3.5 Requirements for network signalling value "NS_53" or "NS_54" or "NS_60" or "NS_66" or "NS_67" or "NS_71" 958

6.5F.3.3.6 Requirements for network signalling value "NS_58" 958

6.5F.3.3.7 Requirements for network signalling value "NS_61" 958

6.5F.3.3.8 Requirements for network signalling value “NS_63” or “NS_69” 958

6.5F.3.3.9 Requirements for network signalling value “NS_64” 959

6.5F.3A Spurious emissions for CA 959

6.5F.3A.0 General 959

6.5F.3A.1 General spurious emissions 960

6.5F.3A.2 Spurious emissions for UE co-existence 960

6.5F.3A.3 Additional spurious emissions 960

6.5F.3A.3.0 General 960

6.5F.3A.3.1 Requirements for network signalling value "CA_NS_53" or "CA_NS_54" 960

6.5F.4 Transmit intermodulation 960

6.5G Output RF spectrum emissions for Tx Diversity 960

6.5G.1 Occupied bandwidth for Tx Diversity 960

6.5G.2 Out of band emission for Tx Diversity 961

6.5G.3 Spurious emission for Tx Diversity 961

6.5G.4 Transmit intermodulation for Tx Diversity 961

6.5H Output RF spectrum emissions for CA with UL MIMO 961

6.5H.1 Output RF spectrum emissions for intra-band UL contiguous CA with UL MIMO 961

6.5H.1.1 Occupied bandwidth for intra-band UL contiguous CA with UL MIMO 961

6.5H.1.2 Out of band emission for intra-band UL contiguous CA with UL MIMO 961

6.5H.1.3  Spurious emission for intra-band UL contiguous CA with UL MIMO 961

6.5H.1.4 Transmit intermodulation for intra-band UL contiguous CA with UL MIMO 962

6.5H.2 Void 962

6.5H.3 Output RF spectrum emissions for inter-band UL CA with UL MIMO 962

6.5H.3.1 Occupied bandwidth for inter-band UL CA with UL MIMO 962

6.5H.3.2 Out of band emission for inter-band UL CA with UL MIMO 962

6.5H.3.3 Spurious emission for inter-band UL CA with UL MIMO 962

6.5H.3.4 Transmit intermodulation for inter-band UL CA with UL MIMO 962

6.5I (Reserved) 962

6.5J Output RF spectrum emissions for ATG 963

6.5J.1 Occupied bandwidth for ATG 963

6.5J.1D Occupied bandwidth for ATG UL MIMO 963

6.5J.2 Out of band emission for ATG 963

6.5J.2.1 General 963

6.5J.2.2 Spectrum emission mask 963

6.5J.2.3 Adjacent channel leakage ratio 963

6.5J.2D Out of band emission for ATG with UL MIMO 964

6.5J.3 Spurious emissions for ATG 964

6.5J.3D Spurious emissions for ATG with UL MIMO 964

6.5K Output RF spectrum emissions for Aerial UE 964

6.5K.1 Occupied bandwidth for Aerial UE 964

6.5K.2 Out of band emission for Aerial UE 965

6.5K.3 Spurious emissions for Aerial UE 965

6.5K.3.0 General 965

6.5K.3.1 General spurious emissions 965

6.5K.3.2 Spurious emissions for UE co-existence 965

6.5K.3.3 Additional spurious emissions 965

6.5K.3.3.1 Requirement for network signalling value "NS_UAV_44" 965

6.5K.3.3.2 Requirement for network signalling value "NS_UAV_46" 965

6.5K.3.3.3 Requirement for network signalling value “NS_UAV_70" 965

6.5L Output RF spectrum emissions for CA with Tx Diversity 966

6.5L.1 Void 966

6.5L.2 Void 966

6.5L.3 Output RF spectrum emissions for inter-band UL CA with Tx Diversity 966

6.5L.3.1 Occupied bandwidth for inter-band UL CA with Tx Diversity 966

6.5L.3.2 Out of band emission for inter-band UL CA with Tx Diversity 966

6.5L.3.3 Spurious emission for inter-band UL CA with Tx Diversity 966

6.5L.3.4 Transmit intermodulation for inter-band UL CA with Tx Diversity 966

6.6 Void 966

6.6E Time alignment error 966

7 Receiver characteristics 967

7.1 General 967

7.1A General 968

7.1F General 968

7.1G (Reserved) 968

7.1H (Reserved) 968

7.1I General 968

7.1J General for ATG 968

7.1K (Reserved) 968

7.1L (Reserved) 968

7.1M General for LP-WUS/WUR 968

7.2 Diversity characteristics 969

7.2J Diversity characteristics for ATG 969

7.2M Diversity characteristics for WUS/WUR 969

7.3 Reference sensitivity 969

7.3.1 General 969

7.3.2 Reference sensitivity power level 970

7.3.3 ΔRIB,c 980

7.3A Reference sensitivity for CA 980

7.3A.1 General 980

7.3A.2 Reference sensitivity power level for CA 981

7.3A.2.1 Reference sensitivity power level for Intra-band contiguous CA 981

7.3A.2.1.1 PC2 and PC1.5 MSD requirements with look-up tables for Intra-band CA 982

7.3A.2.2 Reference sensitivity power level for Intra-band non-contiguous CA 983

7.3A.2.3 Reference sensitivity power level for Inter-band CA 985

7.3A.2.3.1 PC2 and PC1.5 MSD requirements with look-up tables for two-band DL CA with 1UL band 985

7.3A.2.3.2 PC2 and PC1.5 MSD requirements with look-up tables for two-band or three-band DL CA with two-band UL CA 988

7.3A.2.4 Void 990

7.3A.2.5 Reference sensitivity power level for low NR band carrier aggregation via switching 990

7.3A.3 ΔRIB,c for CA 990

7.3A.3.1 General 990

7.3A.3.2 ΔRIB,c for Inter-band CA 990

7.3A.3.2.1 ΔRIB,c for two bands 991

7.3A.3.2.2 Void 993

7.3A.3.2.3 ΔRIB,c for three bands 993

7.3A.3.2.4 ΔRIB,c for four bands 999

7.3A.3.2.5 ΔRIB,c for five bands 1003

7.3A.3.2.6 ΔRIB,c for six bands 1004

7.3A.3.3 ΔRIB,c for Intra-band CA 1004

7.3A.4 Reference sensitivity exceptions due to harmonic interference for CA 1004

7.3A.5 Reference sensitivity exceptions due to intermodulation interference due to 2UL CA 1018

7.3A.6 Reference sensitivity exceptions due to cross band isolation for CA 1083

7.3A.7 Lower-MSD requirements for inter-band CA 1088

7.3B Reference sensitivity for NR-DC 1089

7.3C Reference sensitivity for SUL 1089

7.3C.1 General 1089

7.3C.2 Reference sensitivity power level for SUL 1090

7.3C.2.1 PC2 and PC1.5 MSD requirements with look-up tables for SUL with downlink CA 1095

7.3C.3 ΔRIB,c for SUL 1096

7.3C.3.1 General 1096

7.3C.3.2 SUL band combination 1096

7.3C.3.2.1 ΔRIB,c  for two bands 1097

7.3C.3.2.2 ΔRIB,c  for three bands 1097

7.3C.3.2.3 ΔRIB,c  for four bands 1098

7.3D Reference sensitivity for UL MIMO 1098

7.3E Reference sensitivity for V2X 1099

7.3E.1 General 1099

7.3E.2 Minimum requirements 1099

7.3E.2A Minimum requirements for Sidelink CA 1099

7.3E.2A.1 Reference sensitivity power level for Sidelink CA 1100

7.3E.2F Minimum requirements for Sidelink Unlicensed 1100

7.3E.2F.1 General 1100

7.3E.2F.2 Reference sensitivity power level 1100

7.3E.3 Reference sensitivity power level for V2X concurrent operation 1101

7.3E.3.1 General 1101

7.3E.3F Minimum requirements for SL-U concurrent operation 1102

7.3E.3F.1 Reference sensitivity power level for SL-U concurrent operation 1102

7.3F Reference sensitivity for shared spectrum channel access 1102

7.3F.1 General 1102

7.3F.2 Reference sensitivity power level 1102

7.3F.3 Void 1103

7.3F.4 Void 1103

7.3F.4A Shared spectrum channel access CA 1103

7.3F.4A.1 Intra-band contiguous shared spectrum channel access CA 1103

7.3F.5 Void 1103

7.3F.5.1 Void 1103

7.3F.5.2 Void 1104

7.3F.5.3 Void 1104

7.3G Reference sensitivity for Tx Diversity 1104

7.3G.5 Void 1104

7.3G.5.0 Void 1104

7.3H (Reserved) 1104

7.3I Reference sensitivity for (e)RedCap 1104

7.3I.1 General 1104

7.3I.2 Reference sensitivity power level for RedCap 1104

7.3I.3 Reference sensitivity power level for eRedCap 1108

7.3J Reference sensitivity for ATG 1109

7.3J.1 General 1109

7.3J.2 Reference sensitivity power level 1109

7.3J.2A Reference sensitivity power level for ATG CA 1109

7.3J.2A.1 Reference sensitivity power level for ATG intra-band contiguous CA 1109

7.3J.2A.2 Reference sensitivity power level for ATG inter-band CA 1110

7.3J.3A ΔRIB,c for ATG CA 1110

7.3J.4A Reference sensitivity exceptions due to cross band isolation for ATG CA 1110

7.3K (Reserved) 1111

7.3L (Reserved) 1111

7.3M Reference sensitivity for LP-WUS/WUR 1111

7.3M.1 General 1111

7.3M.2 Reference sensitivity power level for LP-WUS/WUR 1111

7.4 Maximum input level 1111

7.4A Maximum input level for CA 1112

7.4A.1 Maximum input level for Intra-band contiguous CA 1112

7.4A.2 Maximum input level for Intra-band non-contiguous CA 1112

7.4A.3 Maximum input level for Inter-band CA 1113

7.4B Maximum input level for NR-DC 1113

7.4D Maximum input level for UL MIMO 1113

7.4E Maximum input level for V2X 1113

7.4E.1 General 1113

7.4E.1A Maximum input level for Sidelink CA 1113

7.4E.1F General requirement for Sidelink Unlicensed 1114

7.4E.2 Maximum input level for V2X concurrent operation 1114

7.4E.2F Maximum input level for SL-U concurrent operation 1114

7.4F (Reserved) 1114

7.4G (Reserved) 1114

7.4H (Reserved) 1114

7.4I (Reserved) 1114

7.4J Maximum input level for ATG 1114

7.4J.1 General 1114

7.4J.2A Maximum input level for ATG CA 1115

7.4J.2A.1 Minimum requirement for ATG intra-band contiguous CA 1115

7.4J.2A.1 Minimum requirement for ATG inter-band CA 1115

7.4K (Reserved) 1116

7.4L (Reserved) 1116

7.4M Maximum input level for LP-WUS/WUR 1116

7.5 Adjacent channel selectivity 1116

7.5A Adjacent channel selectivity for CA 1118

7.5A.1 Adjacent channel selectivity for Intra-band contiguous CA 1118

7.5A.2 Adjacent channel selectivity Intra-band non-contiguous CA 1120

7.5A.3 Adjacent channel selectivity Inter-band CA 1121

7.5B Adjacent channel selectivity for NR-DC 1121

7.5D Adjacent channel selectivity for UL MIMO 1121

7.5E Adjacent channel selectivity for V2X 1121

7.5E.1 General 1121

7.5E.1A Adjacent channel selectivity requirement for Sidelink CA 1123

7.5E.1F General requirement for Sidelink Unlicensed 1124

7.5E.2 Adjacent channel selectivity for V2X concurrent operation 1124

7.5E.2F Adjacent channel selectivity for SL-U concurrent operation 1124

7.5F Adjacent channel selectivity for shared spectrum channel access 1124

7.5F.1 General 1124

7.5F.1A Adjacent channel selectivity for shared spectrum channel access CA 1125

7.5F.1A.1 Intra-band contiguous shared spectrum channel access CA 1125

7.5F.2 Void 1125

7.5G (Reserved) 1125

7.5H (Reserved) 1125

7.5I (Reserved) 1126

7.5J Adjacent channel selectivity for ATG 1126

7.5J.1 General 1126

7.5J.2A Adjacent channel selectivity for ATG CA 1128

7.5J.2A.1 Minimum requirement for ATG intra-band contiguous CA 1128

7.5J.2A.2 Minimum requirement for ATG inter-band contiguous CA 1129

7.5K (Reserved) 1129

7.5L (Reserved) 1129

7.5M Adjacent channel and subcarrier selectivity for LP-WUS/WUR 1129

7.5M.1 General 1129

7.5M.2 Adjacent channel selectivity for LP-WUS/WUR 1130

7.5M.3 Adjacent subcarrier selectivity for LP-WUS/WUR 1131

7.6 Blocking characteristics 1131

7.6.1 General 1131

7.6.2 In-band blocking 1131

7.6.3 Out-of-band blocking 1134

7.6.4 Narrow band blocking 1137

7.6A Blocking characteristics for CA 1139

7.6A.1 General 1139

7.6A.2 In-band blocking for CA 1139

7.6A.2.1 In-band blocking for Intra-band contiguous CA 1139

7.6A.2.2 In-band blocking for Intra-band non-contiguous CA 1140

7.6A.2.3 In-band blocking for Inter-band CA 1140

7.6A.3 Out-of-band blocking for CA 1141

7.6A.3.1 Out-of-band blocking for Intra-band contiguous CA 1141

7.6A.3.2 Out-of-band blocking for Intra-band non-contiguous CA 1142

7.6A.3.3 Out-of-band blocking for Inter-band CA 1142

7.6A.4 Narrow band blocking for CA 1144

7.6A.4.1 Narrow band blocking for Intra-band contiguous CA 1144

7.6A.4.2 Narrow band blocking for Intra-band non-contiguous CA 1145

7.6A.4.3 Narrow band blocking for Inter-band CA 1145

7.6B Blocking characteristics for NR-DC 1145

7.6C Blocking characteristics for SUL 1145

7.6C.1 General 1145

7.6C.2 In-band blocking for SUL 1145

7.6C.3 Out-of-band blocking for SUL 1146

7.6C.4 Narrow band blocking for SUL 1146

7.6D Blocking characteristics for UL MIMO 1146

7.6E Blocking characteristics for V2X 1146

7.6E.1 General 1146

7.6E.2 In-band blocking 1147

7.6E.2.1 General 1147

7.6E.2.1A In-band blocking for Sidelink CA 1148

7.6E.2.2 In-band blocking for V2X concurrent operation 1148

7.6E.2.2F In-band blocking for SL-U concurrent operation 1148

7.6E.3 Out-of-band blocking 1148

7.6E.3.1 General 1148

7.6E.3.1A Out-of-band blocking for Sidelink CA 1149

7.6E.3.2 Out-of-band blocking for V2X concurrent operation 1150

7.6E.3.2F Out-of-band blocking for SL-U concurrent operation 1150

7.6E.3F Out-of-band blocking for Sidelink Unlicensed 1150

7.6F Blocking characteristics for shared spectrum channel access 1150

7.6F.1 General 1150

7.6F.2 In-band blocking 1151

7.6F.2.1 General 1151

7.6F.2.2 Void 1151

7.6F.2A In-band blocking for shared spectrum CA 1151

7.6F.2A.1 Intra-band contiguous shared spectrum channel access CA 1151

7.6F.3 Out-of-band blocking 1152

7.6F.3.1 General 1152

7.6F.3.2 Void 1153

7.6F.3A Out-of-band blocking for shared spectrum CA 1153

7.6F.3A.1 Intra-band contiguous shared spectrum channel access CA 1153

7.6G (Reserved) 1154

7.6H (Reserved) 1154

7.6I Blocking characteristics for RedCap 1154

7.6J Blocking characteristics for ATG 1154

7.6J.1 General 1154

7.6J.2 In-band blocking for ATG 1154

7.6J.2A In-band blocking for ATG CA 1154

7.6J.2A.1 In-band blocking for ATG Intra-band contiguous CA 1154

7.6J.2A.2 In-band blocking for ATG Inter-band CA 1154

7.6J.3 Out-of-band blocking for ATG 1154

7.6J.3A Out-of-band blocking for ATG CA 1154

7.6J.3A.1 Out-of-band blocking for ATG Intra-band contiguous CA 1155

7.6J.3A.2 Out-band blocking for ATG Inter-band CA 1155

7.6K (Reserved) 1155

7.6L (Reserved) 1155

7.7 Spurious response 1155

7.7A Spurious response for CA 1156

7.7A.1 Spurious response for Intra-band contiguous CA 1156

7.7A.2 Spurious response for Intra-band non-contiguous CA 1156

7.7A.3 Spurious response for Inter-band CA 1156

7.7B Spurious response for NR-DC 1157

7.7D Spurious response for UL MIMO 1157

7.7E Spurious response for V2X 1157

7.7E.1 General 1157

7.7E.1A Spurious response requirements for Sidelink CA 1157

7.7E.1F General requirement for Sidelink Unlicensed 1158

7.7E.2 Spurious response for V2X concurrent operation 1158

7.7E.2F Spurious response for SL-U concurrent operation 1158

7.7F Spurious response for shared spectrum channel access 1158

7.7F.1 General 1158

7.7F.1A Spurious response for shared spectrum channel access CA 1159

7.7F.1A.1 Intra-band contiguous shared spectrum channel access CA 1159

7.7F.2 Void 1159

7.7G (Reserved) 1159

7.7H (Reserved) 1159

7.7I (Reserved) 1159

7.7J Spurious response for ATG 1159

7.7J.1 General 1159

7.7J.1A Spurious response for ATG CA 1159

7.7J.1A.1 Spurious response for ATG intra-band contiguous CA 1159

7.7J.1A.2 Spurious response for ATG inter-band CA 1159

7.7K (Reserved) 1160

7.7L (Reserved) 1160

7.8 Intermodulation characteristics 1160

7.8.1 General 1160

7.8.2 Wide band Intermodulation 1160

7.8A Intermodulation characteristics for CA 1162

7.8A.1 General 1162

7.8A.2 Wide band intermodulation for CA 1162

7.8A.2.1 Wide band intermodulation for Intra-band contiguous CA 1162

7.8A.2.2 Wide band intermodulation for Intra-band non-contiguous CA 1163

7.8A.2.3 Wide band intermodulation for Inter-band CA 1163

7.8B Intermodulation characteristics for NR-DC 1164

7.8D Intermodulation characteristics for UL MIMO 1164

7.8E Intermodulation characteristics for V2X 1164

7.8E.1 General 1164

7.8E.2 Wide band Intermodulation 1164

7.8E.2.1 General 1164

7.8E.2.2 Wide band Intermodulation for V2X concurrent operation 1165

7.8E.2.2A Wide band intermodulation for Sidelink CA 1165

7.8E.2.2F Wide band Intermodulation for SL-U concurrent operation 1165

7.8E.2F Wide band Intermodulation for Sidelink Unlicensed 1166

7.8F Intermodulation characteristics for shared spectrum channel access 1166

7.8F.1 General 1166

7.8F.2 Wide band Intermodulation 1166

7.8G (Reserved) 1166

7.8H (Reserved) 1167

7.8I (Reserved) 1167

7.8J Intermodulation characteristics for ATG 1167

7.8J.1 General 1167

7.8J.2 Wide band intermodulation for ATG 1167

7.8J.2A Wide band intermodulation for ATG CA 1167

7.8J.2A.1 Wide band intermodulation for ATG intra-band contiguous CA 1167

7.8J.2A.2 Wide band intermodulation for ATG inter-band CA 1167

7.8K (Reserved) 1167

7.8L (Reserved) 1167

7.9 Spurious emissions 1167

7.9A Spurious emissions for CA 1168

7.9A.1 Void 1168

7.9A.2 Void 1168

7.9A.3 Spurious emissions for Inter-band CA 1168

7.9B Spurious emissions for NR-DC 1168

7.9J Spurious emissions for ATG 1168

7.9J.1 General 1168

7.9J.1A Spurious emissions for ATG CA 1168

7.9J.1A.1 Spurious emissions for ATG inter-band CA 1168

7.9M Spurious emissions for LP-WUS/WUR 1168

7.10 Power imbalance 1168

7.10A Power imbalance for CA 1168

7.10A.1 General 1168

7.10A.2 Minimum requirement 1169

Annex A (normative): Measurement channels 1170

A.1 General 1170

A.2 UL reference measurement channels 1170

A.2.1 General 1170

A.2.2 Reference measurement channels 1172

A.2.2.1 DFT-s-OFDM Pi/2-BPSK 1172

A.2.2.2 DFT-s-OFDM QPSK 1173

A.2.2.3 DFT-s-OFDM 16QAM 1175

A.2.2.4 DFT-s-OFDM 64QAM 1176

A.2.2.5 DFT-s-OFDM 256QAM 1178

A.2.2.6 CP-OFDM QPSK 1179

A.2.2.7 CP-OFDM 16QAM 1181

A.2.2.8 CP-OFDM 64QAM 1183

A.2.2.9 CP-OFDM 256QAM 1185

A.2.3 Reference measurement channels for TDD 1188

A.2.3.1 DFT-s-OFDM Pi/2-BPSK 1188

A.2.3.2 DFT-s-OFDM QPSK 1188

A.2.3.3 DFT-s-OFDM 16QAM 1188

A.2.3.4 DFT-s-OFDM 64QAM 1188

A.2.3.5 DFT-s-OFDM 256QAM 1188

A.2.3.6 CP-OFDM QPSK 1189

A.2.3.7 CP-OFDM 16QAM 1189

A.2.3.8 CP-OFDM 64QAM 1189

A.2.3.9 CP-OFDM 256QAM 1189

A.3 DL reference measurement channels 1189

A.3.1 General 1189

A.3.2 DL reference measurement channels for FDD 1192

A.3.2.1 General 1192

A.3.2.2 FRC for receiver requirements for QPSK 1193

A.3.2.3 FRC for maximum input level for 64QAM 1196

A.3.2.4 FRC for maximum input level for 256 QAM 1199

A.3.2.5 FRC for maximum input level for 1024 QAM 1202

A.3.3 DL reference measurement channels for TDD 1205

A.3.3.1 General 1205

A.3.3.2 FRC for receiver requirements for QPSK 1206

A.3.3.3 FRC for maximum input level for 64QAM 1209

A.3.3.4 FRC for maximum input level for 256 QAM 1212

A.3.3.5 FRC for maximum input level for 1024 QAM 1215

A.3M LP-WUR reference channel 1218

A.3M.1 General 1218

A.4 CSI reference measurement channels 1218

A.5 OFDMA Channel Noise Generator (OCNG) 1219

A.5.1 OCNG Patterns for FDD 1219

A.5.1.1 OCNG FDD pattern 1: Generic OCNG FDD Pattern for all unused REs 1219

A.5.2 OCNG Patterns for TDD 1219

A.5.2.1 OCNG TDD pattern 1: Generic OCNG TDD Pattern for all unused REs 1219

A.6 Void 1219

A.7 V2X reference measurement channels 1220

A.7.1 General 1220

A.7.2 FRC for V2X receiver requirements for QPSK 1220

A.7.3 FRC for maximum input level for 64QAM 1222

A.7.4 FRC for maximum input level for 256QAM 1223

A.8 Reference measurement channels for low NR band carrier aggregation via switching 1226

A.8.1 DL reference measurement channels for low NR band carrier aggregation via switching 1226

Annex B (informative): Void 1230

Annex C (informative): Downlink physical channels 1231

C.1 General 1231

C.2 Setup 1231

C.3 Connection 1231

C.3.1 Measurement of Receiver Characteristics 1231

Annex D (normative): Characteristics of the interfering signal 1232

D.1 General 1232

D.2 Void 1232

Annex E (normative):  Environmental conditions 1233

E.1 General 1233

E.2 Environmental 1233

E.2.1 Temperature 1233

E.2.2 Voltage 1233

E.2.3 Vibration 1234

Annex F (normative):  Transmit modulation 1235

F.0 General 1235

F.1 Measurement Point 1235

F.2 Basic Error Vector Magnitude measurement 1235

F.3 Basic in-band emissions measurement 1236

F.4 Modified signal under test 1237

F.5 Window length 1239

F.5.1 Timing offset 1239

F.5.2 Window length 1239

F.5.3 Window length for normal CP 1239

F.5.4 Window length for Extended CP 1240

F.5.5 Window length for PRACH 1241

F.6 Averaged EVM 1242

F.7 Spectrum Flatness 1243

F.8 EVM measurement for multiple Tx 1243

F.9 Phase offset measurement for DMRS bundling 1243

F.9.1 Measurement point 1243

F.9.2 Symbols used 1243

F.9.3 Modified test signal 1243

F.9.4 Phase offset measurement 1244

F.10 EVM for UL MIMO 1244

F10.1 General 1244

F10.2 MIMO Equalization 1245

F10.3 Layer processing 1246

Annex G (normative):  Difference of relative phase and power errors 1247

G.0 General 1247

G.1 Measurement Point 1247

G.2 Relative Phase Error Measurement 1247

G.2.1 Symbols and subcarriers used 1247

G.2.2 CFO (carrier frequency offset) correction 1248

G.2.3 Steps of the measurement method 1248

Annex H (informative): Void 1249

Annex I (informative): Void 1250

Annex J (informative): Void 1251

Annex K (informative): Void 1252

Annex L (normative): ModifiedMPR-Behavior 1253

L.1 Indication of modified MPR behavior 1253

Annex M (normative):  Declared Supported Post Antenna Gain for UE 1256

M.1 FRMCS operating bands 1256

Annex N (informative): Change history 1257


