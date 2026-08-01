| 3GPP TS 36.101 V19.6.0 (2026-06) |  |
| --- | --- |
| Technical Specification |  |
| 3rd Generation Partnership Project;Technical Specification Group Radio Access Network;Evolved Universal Terrestrial Radio Access (E-UTRA);User Equipment (UE) radio transmission and reception(Release 19) |  |
|  |  |
| ![](media/image1.emf) |  |
|  |  |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. |  |

|  |
| --- |
| 3GPPPostal address3GPP support office address650 Route des Lucioles - Sophia AntipolisValbonne - FRANCETel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16Internethttp://www.3gpp.org |
| Copyright NotificationNo part may be reproduced except as authorized by written permission. The copyright and the foregoing restriction extend to reproduction in all media.© 2026, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).All rights reserved.UMTS™ is a Trade Mark of ETSI registered for the benefit of its members3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersGSM® and the GSM logo are registered and owned by the GSM Association |

Contents

Foreword 32

1 Scope 34

2 References 34

3 Definitions, symbols and abbreviations 35

3.1 Definitions 35

3.2 Symbols 37

3.3 Abbreviations 39

4 General 41

4.1 Relationship between minimum requirements and test requirements 41

4.2 Applicability of minimum requirements 41

4.3 Void 41

4.3A Applicability of feature-specific minimum requirements 41

4.4 RF requirements in later releases 43

5 Operating bands and channel arrangement 43

5.1 General 43

5.2 Void 43

5.3 Void 43

5.4 Void 43

5.5 Operating bands 43

5.5A Operating bands for CA 46

5.5B Operating bands for UL-MIMO 67

5.5C Operating bands for Dual Connectivity 67

5.5D Operating bands for ProSe 70

5.5E Operating bands for UE category 0, UE category M1 and M2 and UE category 1bis 71

5.5F Operating bands for category NB1 and NB2 71

5.5G Operating bands for V2X Communication 72

5.5H Operating bands for LTE based 5G terrestrial broadcast 73

5.5K Operating bands for Aerial UE 73

5.6 Channel bandwidth 74

5.6.1 Channel bandwidths per operating band 74

5.6A Channel bandwidth for CA 77

5.6A.1 Channel bandwidths per operating band for CA 79

5.6B Channel bandwidth for UL-MIMO 219

5.6B.1 Void 219

5.6C Channel bandwidth for Dual Connectivity 219

5.6C.1 Void 219

5.6D Channel bandwidth for ProSe 219

5.6D.1 Channel bandwidths per operating band for ProSe 219

5.6F Channel bandwidth for category NB1 and NB2 220

5.6G Channel bandwidth for V2X Communication 221

5.6G.1 Channel bandwidths per operating band for V2X Communication 221

5.6H PMCH bandwidth for LTE based 5G terrestrial broadcast 223

5.6H.1 PMCH bandwidths per operating band for LTE based 5G terrestrial broadcast 224

5.7 Channel arrangement 224

5.7.1 Channel spacing 224

5.7.1A Channel spacing for CA 224

5.7.1F Channel spacing for category NB1 and NB2 224

5.7.1H Channel spacing for LTE based 5G terrestrial broadcast 224

5.7.2 Channel raster 225

5.7.2A Channel raster for CA 225

5.7.2F Channel raster for category NB1 and NB2 225

5.7.3 Carrier frequency and EARFCN 225

5.7.3F Carrier frequency and EARFCN for category NB1 and NB2 228

5.7.3H Carrier frequency and EARFCN for LTE based 5G terrestrial broadcast 229

5.7.4 TX–RX frequency separation 229

5.7.4A TX–RX frequency separation for CA 230

5.7.4E TX–RX frequency separation for category M1 and M2 230

5.7.4F TX–RX frequency separation for category NB1 and NB2 231

6 Transmitter characteristics 231

6.1 General 231

6.2 Transmit power 231

6.2.1 Void 231

6.2.2 UE maximum output power 231

6.2.2A UE maximum output power for CA 234

6.2.2B UE maximum output power for UL-MIMO 239

6.2.2C Void 242

6.2.2D UE maximum output power for ProSe 242

6.2.2E UE maximum output power for Category M1 and M2 UE 242

6.2.2F UE maximum output power for category NB1 and NB2 243

6.2.2G UE maximum output power for V2X Communication 244

6.2.2K UE maximum output power for Aerial UE 246

6.2.3 UE maximum output power for modulation / channel bandwidth 246

6.2.3A UE Maximum Output power for modulation / channel bandwidth for CA 247

6.2.3B UE maximum output power for modulation / channel bandwidth for UL-MIMO 252

6.2.3D UE maximum output power for modulation / channel bandwidth for ProSe 252

6.2.3E UE maximum output power for modulation / channel bandwidth for category M1 and M2 253

6.2.3F UE maximum output power for modulation / channel bandwidth for category NB1 and NB2 255

6.2.3G UE maximum output power for modulation / channel bandwidth for V2X Communication 256

6.2.3G.1 MPR for Power class 3 V2X UE 256

6.2.3G.2 MPR for Power class 2 V2X UE 257

6.2.3K UE maximum output power for modulation / channel bandwidth for Aerial UE 258

6.2.4 UE maximum output power with additional requirements 258

6.2.4A UE maximum output power with additional requirements for CA 278

6.2.4A.1 A-MPR for CA_NS_01 for CA_1C 280

6.2.4A.2 A-MPR for CA_NS_02 for CA_1C 281

6.2.4A.3 A-MPR for CA_NS_03 for CA_1C 282

6.2.4A.4 A-MPR for CA_NS_04 283

6.2.4A.5 A-MPR for CA_NS_05 for CA_38C 285

6.2.4A.6 A-MPR for CA_NS_06 286

6.2.4A.7 A-MPR for CA_NS_07 287

6.2.4A.8 A-MPR for CA_NS_08 288

6.2.4A.9 Void 289

6.2.4A.10 A-MPR for CA_NS_10 289

6.2.4A.11 A-MPR for CA_NS_11 294

6.2.4A.12 A-MPR for CA_NS_12 294

6.2.4A.13 A-MPR for CA_NS_13 295

6.2.4A.14 A-MPR for CA_NS_17 296

6.2.4A.15 A-MPR for CA_NS_18 297

6.2.4B UE maximum output power with additional requirements for UL-MIMO 299

6.2.4D UE maximum output power with additional requirements for ProSe 299

6.2.4E UE maximum output power with additional requirements for category M1 and M2 UE 299

6.2.4F UE maximum output power with additional requirements for category NB1 and NB2 UE 310

6.2.4G UE maximum output power with additional requirements for V2X Communication 310

6.2.5 Configured transmitted power 313

6.2.5A Configured transmitted power for CA 352

6.2.5B Configured transmitted power for UL-MIMO 355

6.2.5C Configured transmitted power for Dual Connectivity 356

6.2.5D Configured transmitted power for ProSe 357

6.2.5F Configured transmitted Power for category NB1 and NB2 359

6.2.5G Configured transmitted power for V2X Communication 360

6.2.5K Configured transmitted power for Aerial UE 364

6.3 Output power dynamics 364

6.3.1 (Void) 364

6.3.2 Minimum output power 364

6.3.2.1 Minimum requirement 364

6.3.2A  UE Minimum output power for CA 364

6.3.2A.1 Minimum requirement for CA 364

6.3.2B  UE Minimum output power for UL-MIMO 365

6.3.2B.1 Minimum requirement 365

6.3.2C  Void 365

6.3.2D UE Minimum output power for ProSe 365

6.3.2F UE Minimum output power for category NB1 and NB2 365

6.3.2G UE Minimum output power for V2X Communication 366

6.3.3 Transmit OFF power 366

6.3.3.1. Minimum requirement 366

6.3.3A  UE Transmit OFF power for CA 366

6.3.3A.1 Minimum requirement for CA 367

6.3.3B  UE Transmit OFF power for UL-MIMO 367

6.3.3B.1 Minimum requirement 367

6.3.3D Transmit OFF power for ProSe 367

6.3.3F Transmit OFF power for category NB1 and NB2 368

6.3.3G Transmit OFF power for V2X Communication 368

6.3.4 ON/OFF time mask 368

6.3.4.1 General ON/OFF time mask 368

6.3.4.2 PRACH and SRS time mask 370

6.3.4.2.1 PRACH time mask 370

6.3.4.2.2 SRS time mask 370

6.3.4.3 Slot / Sub frame boundary time mask for subframe TTI 372

6.3.4.4 PUCCH / PUSCH / SRS time mask for subframe TTI 374

6.3.4.5 Symbol / Subslot boundary time mask for subslot TTI 376

6.3.4.6 Subslot PUCCH / subslot PUSCH / SRS time mask for subslot TTI 378

6.3.4.7 Symbol / Slot boundary time mask for slot TTI 381

6.3.4.8 Slot PUCCH / slot PUSCH / SRS time mask for slot TTI 381

6.3.4.9 Consecutive subslot and slot TTI or consecutive subslot and subframe TTI  time mask 382

6.3.4.10 Consecutive subframe and subslot TTI or consecutive slot and subslot TTI time mask 382

6.3.4.11 Consecutive TTI and slot TTI or consecutive slot TTI and TTI time mask 383

6.3.4A ON/OFF time mask for CA 383

6.3.4B ON/OFF time mask for UL-MIMO 383

6.3.4D ON/OFF time mask for ProSe 384

6.3.4D.1  General time mask for ProSe 384

6.3.4D.2  PSSS/SSSS time mask 384

6.3.4D.3  PSSS / SSSS / PSBCH time mask 385

6.3.4D.4  PSSCH / SRS time mask 386

6.3.4F ON/OFF time mask for category NB1 and NB2 386

6.3.4F.1 General ON/OFF time mask 386

6.3.4F.2 NPRACH time mask 386

6.3.4G ON/OFF time mask for V2X Communication 387

6.3.4G.1 PSSS / SSSS / PSBCH time mask 387

6.3.5 Power Control 388

6.3.5.1 Absolute power tolerance 388

6.3.5.1.1  Minimum requirements 388

6.3.5.2 Relative Power tolerance 389

6.3.5.2.1 Minimum requirements 389

6.3.5.3 Aggregate power control tolerance 390

6.3.5.3.1 Minimum requirement 390

6.3.5A Power control for CA 390

6.3.5A.1 Absolute power tolerance 390

6.3.5A.1.1  Minimum requirements 390

6.3.5A.2 Relative power tolerance 391

6.3.5A.2.1 Minimum requirements 391

6.3.5A.3 Aggregate power control tolerance 391

6.3.5A.3.1  Minimum requirements 391

6.3.5B Power control for UL-MIMO 392

6.3.5D Power Control for ProSe 392

6.3.5D.1 Absolute power tolerance 392

6.3.5E Power control for category M1 and M2 392

6.3.5E.1 Absolute power tolerance 392

6.3.5E.2 Relative Power tolerance 392

6.3.5E.3 Aggregate power control tolerance 393

6.3.5E.3.1 Minimum requirement 393

6.3.5F Power Control for category NB1 and NB2 393

6.3.5F.1 Absolute power tolerance 394

6.3.5F.2 Relative power tolerance 394

6.3.5F.3 Aggregate power control tolerance for category NB1 and NB2 395

6.3.5F.3.1 Minimum requirement 395

6.3.5G Power Control for V2X Communication 395

6.3.5G.1 Absolute power tolerance 395

6.4 Void 396

6.5 Transmit signal quality 396

6.5.1 Frequency error 396

6.5.1A  Frequency error for CA 396

6.5.1B Frequency error for UL-MIMO 396

6.5.1D Frequency error for ProSe 396

6.5.1E Frequency error for UE category M1 and M2 396

6.5.1F Frequency error for UE category NB1 and NB2 397

6.5.1G Frequency error for V2X Communication 397

6.5.2 Transmit modulation quality 397

6.5.2.1  Error Vector Magnitude 398

6.5.2.1.1 Minimum requirement 398

6.5.2.2  Carrier leakage 398

6.5.2.2.1  Minimum requirements 399

6.5.2.3 In-band emissions 399

6.5.2.3.1  Minimum requirements 399

6.5.2.4  EVM equalizer spectrum flatness 400

6.5.2.4.1 Minimum requirements 400

6.5.2A Transmit modulation quality for CA 401

6.5.2A.1 Error Vector Magnitude 402

6.5.2A.2 Carrier leakage for CA 402

6.5.2A.2.1 Minimum requirements 402

6.5.2A.3 In-band emissions 402

6.5.2A.3.1 Minimum requirement for CA 402

6.5.2B Transmit modulation quality for UL-MIMO 405

6.5.2B.1 Error Vector Magnitude 405

6.5.2B.2 Carrier leakage 405

6.5.2B.3 In-band emissions 405

6.5.2B.4 EVM equalizer spectrum flatness for UL-MIMO 405

6.5.2D Transmit modulation quality for ProSe 405

6.5.2D.1 Error Vector Magnitude 405

6.5.2D.2 Carrier leakage 406

6.5.2D.3 In-band emissions 406

6.5.2D.4 EVM equalizer spectrum flatness for ProSe 406

6.5.2E Transmit modulation quality for category M1 and M2 406

6.5.2E.1 Error Vector Magnitude 406

6.5.2E.2 Carrier leakage 406

6.5.2E.2.1 Minimum requirements 406

6.5.2E.3 In-band emissions 406

6.5.2E.3.1 Minimum requirements 406

6.5.2F Transmit modulation quality for Category NB1 and NB2 408

6.5.2F.1 Error Vector Magnitude 408

6.5.2F.2 Carrier leakage 408

6.5.2F.3 In-band emissions 408

6.5.2G Transmit modulation quality for V2X Communication 409

6.5.2G.1 Error Vector Magnitude 409

6.5.2G.2 Carrier leakage 410

6.5.2G.3 In-band emissions 410

6.5.2G.4 EVM equalizer spectrum flatness 410

6.6 Output RF spectrum emissions 410

6.6.1 Occupied bandwidth 410

6.6.1.1 Additional minimum requirement for E-UTRA (network signalled value “NS_29”) 411

6.6.1A Occupied bandwidth for CA 411

6.6.1B  Occupied bandwidth for UL-MIMO 411

6.6.1F Occupied bandwidth for category NB1 and NB2 412

6.6.1G Occupied bandwidth for V2X Communication 412

6.6.2 Out of band emission 412

6.6.2.1 Spectrum emission mask 412

6.6.2.1.1 Minimum requirement 412

6.6.2.1A Spectrum emission mask for CA 413

6.6.2.2 Additional spectrum emission mask 414

6.6.2.2.1 Minimum requirement (network signalled value "NS_03", “NS_11”, "NS_20", and “NS_21”) 414

6.6.2.2.2 Minimum requirement (network signalled value "NS_04") 415

6.6.2.2.3 Minimum requirement (network signalled value "NS_06" or “NS_07”) 415

6.6.2.2.4 Minimum requirement (network signalled value "NS_33" or “NS_34”) 416

6.6.2.2.5 Minimum requirement (network signalled value “NS_27” and “NS_43”) 416

6.6.2.2.6 Minimum requirement (network signalled value "NS_28”) 417

6.6.2.2.7 Minimum requirement (network signalled value "NS_35") 417

6.6.2.2A Additional Spectrum Emission Mask for CA 418

6.6.2.2A.1 Minimum requirement (network signalled value "CA_NS_04") 418

6.6.2.2A.2 Minimum requirement CA_66B (network signalled value "CA_NS_09") 418

6.6.2.2A.3 Minimum requirement CA_66C (network signalled value "CA_NS_09") 419

6.6.2.2A.4 Minimum requirement CA_48B and CA_48C (network signalled value "CA_NS_10") 419

6.6.2.2A.5 Minimum requirement CA_2C (network signalled value "CA_NS_11") 420

6.6.2.3 Adjacent Channel Leakage Ratio 421

6.6.2.3.1 Minimum requirement E-UTRA 421

6.6.2.3.1a Additional minimum requirement for E-UTRA (network signalled value “NS_29”) 422

6.6.2.3.1A Void 423

6.6.2.3.1Aa Void 423

6.6.2.3.2 Minimum requirements UTRA 423

6.6.2.3.2A Minimum requirement UTRA for CA 424

6.6.2.3.3A Minimum requirements for CA E-UTRA 426

6.6.2.4 Void 427

6.6.2.4.1 Void 427

6.6.2A Void 427

6.6.2B  Out of band emission for UL-MIMO 427

6.6.2C  Void 427

6.6.2D  Out of band emission for ProSe 427

6.6.2F Out of band emission for category NB1 and NB2 428

6.6.2F.1 Spectrum emission mask 428

6.6.2F.2 Additional Spectrum Emission Mask for Category NB1 and NB2 428

6.6.2F.2.1 Minimum requirement (network signalled value "NS_02") 428

6.6.2F.2.2 Minimum requirement (network signalled value "NS_03") 428

6.6.2F.3 Adjacent Channel Leakage Ratio for category NB1 and NB2 429

6.6.2G  Out of band emission for V2X Communication 429

6.6.3 Spurious emissions 430

6.6.3.1 Minimum requirements 430

6.6.3.1A Minimum requirements for CA 431

6.6.3.2 Spurious emission band UE co-existence 432

6.6.3.2A Spurious emission band UE co-existence for CA 441

6.6.3.3 Additional spurious emissions 451

6.6.3.3.1  Minimum requirement (network signalled value "NS_05") 451

6.6.3.3.2  Minimum requirement (network signalled value “NS_07”) 451

6.6.3.3.3  Minimum requirement (network signalled value “NS_08”) 452

6.6.3.3.4  Minimum requirement (network signalled value “NS_09”) 452

6.6.3.3.5  Minimum requirement (network signalled value "NS_12") 452

6.6.3.3.6  Minimum requirement (network signalled value “NS_13”) 452

6.6.3.3.7  Minimum requirement (network signalled value “NS_14”) 453

6.6.3.3.8  Minimum requirement (network signalled value “NS_15”) 453

6.6.3.3.9  Minimum requirement (network signalled value “NS_16”) 453

6.6.3.3.10  Minimum requirement (network signalled value “NS_17”) 454

6.6.3.3.11  Minimum requirement (network signalled value “NS_18”) 454

6.6.3.3.12  Minimum requirement (network signalled value “NS_19”) 454

6.6.3.3.13  Minimum requirement (network signalled value “NS_11”) 454

6.6.3.3.14 Minimum requirement (network signalled value “NS_20”) 455

6.6.3.3.15 Minimum requirement (network signalled value “NS_21”) 455

6.6.3.3.16 Minimum requirement (network signalled value "NS_22") 455

6.6.3.3.17 Minimum requirement (network signalled value “NS_23”) 456

6.6.3.3.18 Void 456

6.6.3.3.19 Minimum requirement (network signalled value "NS_04") 456

6.6.3.3.20 Minimum requirement (network signalled value “NS_24”) 457

6.6.3.3.21 Minimum requirement (network signalled value “NS_25”) 457

6.6.3.3.22 Minimum requirement (network signalled value “NS_26”) 457

6.6.3.3.23 Minimum requirement (network signalled value “NS_27” and “NS_43”) 458

6.6.3.3.24 Minimum requirement (network signalled value “NS_28”) 458

6.6.3.3.25 Minimum requirement (network signalled value “NS_29”) 458

6.6.3.3.26 Minimum requirement (network signalled value “NS_30”) 459

6.6.3.3.27 Minimum requirement (network signalled value “NS_31”) 460

6.6.3.3.28 Minimum requirement (network signalled value “NS_36”) 461

6.6.3.3.29 Minimum requirement (network signalled value “NS_38”) 461

6.6.3.3.30 Minimum requirement (network signalled value “NS_39”) 461

6.6.3.3.31 Minimum requirement (network signalled value “NS_40” and “NS_41”) 461

6.6.3.3.32 Minimum requirement (network signalled value “NS_42”) 462

6.6.3.3.33 Minimum requirement (network signalled value “NS_44”) 462

6.6.3.3.34 Minimum requirement (network signalled value “NS_45”) 462

6.6.3.3.35 Minimum requirement (network signalled value “NS_56”) 463

6.6.3.3.36 Minimum requirement (network signalled value “NS_62”) 463

6.6.3.3A Additional spurious emissions for CA 464

6.6.3.3A.1 Minimum requirement for CA_1C (network signalled value "CA_NS_01") 464

6.6.3.3A.2  Minimum requirement for CA_1C (network signalled value "CA_NS_02") 464

6.6.3.3A.3 Minimum requirement for CA_1C (network signalled value "CA_NS_03") 465

6.6.3.3A.4 Minimum requirement for CA_38C (network signalled value "CA_NS_05") 465

6.6.3.3A.5 Minimum requirement for CA_7C (network signalled value "CA_NS_06") 465

6.6.3.3A.6 Minimum requirement for CA_39C and CA_39C-41A (network signalled value "CA_NS_07") 466

6.6.3.3A.7 Minimum requirement for CA_42C (network signalled value "CA_NS_08") 466

6.6.3.3A.8 Minimum requirement for CA_41C and CA_41D (network signalled value "CA_NS_04") 466

6.6.3.3A.9 Void 467

6.6.3.3A.10 Minimum requirement for CA_48B and CA_48C (network signalled value "CA_NS_10") 467

6.6.3.3A.11 Minimum requirement for CA_28C (network signalled value "CA_NS_12") 467

6.6.3.3A.12 Minimum requirement for CA_28C (network signalled value "CA_NS_13") 467

6.6.3A Void 468

6.6.3B  Spurious emission for UL-MIMO 468

6.6.3C  Void 468

6.6.3D  Spurious emission for ProSe 468

6.6.3F Spurious emission for category NB1 and NB2 468

6.6.3F.1 Additional spurious emissions 468

6.6.3F.1.2  Minimum requirement (network signalled value "NS_06") 468

6.6.3G Spurious emission for V2X Communication 469

6.6.3K Spurious emission for Aerial UE 471

6.6A Void 472

6.6B Void 472

6.7 Transmit intermodulation 472

6.7.1 Minimum requirement 472

6.7.1A Minimum requirement for CA 472

6.7.1B Minimum requirement for UL-MIMO 473

6.7.1F Minimum requirement for category NB1 and NB2 473

6.7.1G Minimum requirement for V2X Communication 473

6.8 Void 474

6.8A Void 474

6.8B  Time alignment error for UL-MIMO 474

6.8B.1  Minimum Requirements 474

6.8C Void 474

6.8D Void 474

6.8E Void 474

6.8F Void 474

6.8G Time alignment error 474

7 Receiver characteristics 474

7.1 General 474

7.2 Diversity characteristics 475

7.3 Reference sensitivity power level 475

7.3.1 Minimum requirements (QPSK) 476

7.3.1A Minimum requirements (QPSK) for CA 518

7.3.1B Minimum requirements (QPSK) for UL-MIMO 568

7.3.1D Minimum requirements (QPSK) for ProSe 568

7.3.1E Minimum requirements (QPSK) for UE category 0, M1, M2 and 1bis 570

7.3.1F Minimum requirements for UE category NB1 and NB2 582

7.3.1F.1 Reference sensitivity for UE category NB1 and NB2 582

7.3.1F.2 Void 583

7.3.1G Minimum requirements (QPSK) for V2X 583

7.3.1H Minimum requirements for LTE based 5G terrestrial broadcast 585

7.3.2 Void 586

7.4 Maximum input level 586

7.4.1 Minimum requirements 586

7.4.1A Minimum requirements for CA 586

7.4.1B Minimum requirements for UL-MIMO 588

7.4.1D Minimum requirements for ProSe 588

7.4.1F Minimum requirements for category NB1 and NB2 588

7.4.1G Minimum requirements for V2X 588

7.4.1H Minimum requirements for LTE based 5G terrestrial broadcast 589

7.4A Void 589

7.4A.1 Void 589

7.5 Adjacent Channel Selectivity (ACS) 589

7.5.1 Minimum requirements 589

7.5.1A Minimum requirements for CA 590

7.5.1B Minimum requirements for UL-MIMO 595

7.5.1D Minimum requirements for ProSe 595

7.5.1F Minimum requirements for category NB1 and NB2 595

7.5.1G Minimum requirements for V2X 596

7.5.1H Minimum requirements for LTE based 5G terrestrial broadcast 598

7.6 Blocking characteristics 599

7.6.1 In-band blocking 599

7.6.1.1 Minimum requirements 599

7.6.1.1A Minimum requirements for CA 601

7.6.1.1D Minimum requirements for ProSe 604

7.6.1.1F Minimum requirements for category NB1 and NB2 605

7.6.1.1G Minimum requirements for V2X 605

7.6.1.1H Minimum requirements for LTE based 5G terrestrial broadcast 607

7.6.2 Out-of-band blocking 608

7.6.2.1 Minimum requirements 608

7.6.2.1A Minimum requirements for CA 609

7.6.2.1D Minimum requirements for ProSe 613

7.6.2.1F Minimum requirements for category NB1 and NB2 613

7.6.2.1G Minimum requirements for V2X 614

7.6.2.1H Minimum requirements for LTE based 5G terrestrial broadcast 615

7.6.3 Narrow band blocking 616

7.6.3.1 Minimum requirements 616

7.6.3.1A Minimum requirements for CA 617

7.6.3.1D Minimum requirements for ProSe 618

7.6.3.1H Minimum requirements for LTE based 5G terrestrial broadcast 618

7.6A Void 618

7.6B Blocking characteristics for UL-MIMO 618

7.7 Spurious response 619

7.7.1 Minimum requirements 619

7.7.1A Minimum requirements for CA 619

7.7.1B Minimum requirements for UL-MIMO 620

7.7.1D Minimum requirements for ProSe 620

7.7.1F Minimum requirements for UE category NB1 and NB2 621

7.7.1G Minimum requirements for V2X 621

7.7.1H Minimum requirements for LTE based 5G terrestrial broadcast 622

7.8 Intermodulation characteristics 623

7.8.1 Wide band intermodulation 623

7.8.1.1 Minimum requirements 623

7.8.1A Minimum requirements for CA 624

7.8.1B Minimum requirements for UL-MIMO 627

7.8.1D Minimum requirements for ProSe 627

7.8.1F Minimum requirements for category NB1 and NB2 628

7.8.1G Minimum requirements 628

7.8.1H Minimum requirements for LTE based 5G terrestrial broadcast 629

7.8.2 Void 630

7.9 Spurious emissions 630

7.9.1 Minimum requirements 630

7.9.1A Minimum requirements 631

7.10 Receiver image 631

7.10.1 Void 631

7.10.1A Minimum requirements for CA 631

7.10.1G Minimum requirements for V2X Communication 631

8 Performance requirement 633

8.1 General 633

8.1.1 Receiver antenna capability 633

8.1.1.1 Simultaneous unicast and MBMS operations 634

8.1.1.2 Dual-antenna receiver capability in idle mode 634

8.1.2 Applicability of requirements 634

8.1.2.1 Applicability of requirements for different channel bandwidths 634

8.1.2.2 Definition of CA capability 634

8.1.2.2A Definition of dual connectivity capability 639

8.1.2.3 Applicability and test rules for different CA configurations and bandwidth combination sets 640

8.1.2.3A Applicability and test rules for different dual connectivity configuration and bandwidth combination set 643

8.1.2.3B Applicability and test rules for different TDD-FDD CA configurations and bandwidth combination sets 644

8.1.2.3C Applicability and test rules for SDR tests for 4Rx capable UEs 646

8.1.2.3D Applicability and test rules for different CA with LAA SCell(s) configurations and bandwidth combination sets 646

8.1.2.3E Applicability and test rules for SDR tests for 8Rx capable UEs 647

8.1.2.4 Test coverage for different number of component carriers 648

8.1.2.5 Applicability of performance requirements for Type B receiver 649

8.1.2.6 Applicability of performance requirements for 4Rx capable UEs 649

8.1.2.6.1 Applicability rule and antenna connection for single carrier tests with 2Rx 649

8.1.2.6.2 Applicability rule and antenna connection for CA and DC tests with 2Rx 651

8.1.2.6.3 Applicability rule and antenna connection for single carrier tests with 4Rx 651

8.1.2.6.4 Applicability rule for 256QAM tests 652

8.1.2.6.5 Applicability rule and antenna connection for CA and DC tests with 4Rx 652

8.1.2.6.6 Applicability rule for Type C with 4Rx 656

8.1.2.6.7 Applicability rule for 1024QAM tests 656

8.1.2.7 Applicability of Enhanced Downlink Control Channel Performance Requirements 656

8.1.2.8 Applicability of performance requirements for CDM-multiplexed DM RS with interfering simultaneous transmission (FRC) with multiple CSI-RS configurations 658

8.1.2.8A Applicability of performance requirements for UE supporting coverage enhancement 658

8.1.2.9 Applicability of SDR requirements for CA and LAA 659

8.1.2.10 Applicability of performance requirements for Multi-user Superposed Transmission 660

8.1.2.11 Applicability CRS interference mitigation receivers performance requirements 660

8.1.2.12 Applicability of performance requirements for 8Rx capable UEs 661

8.1.2.12.1 Applicability rule and antenna connection for single carrier PDSCH tests 661

8.1.2.12.2 Applicability rule and antenna connection for control channel tests 667

8.1.2.12.3 Applicability rule and antenna connection for CA and DC tests 667

8.1.3 UE category and UE DL category 668

8.2 Demodulation of PDSCH (Cell-Specific Reference Symbols) 668

8.2.1 FDD (Fixed Reference Channel) 668

8.2.1.1 Single-antenna port performance 669

8.2.1.1.1 Minimum Requirement 669

8.2.1.1.2 Void 675

8.2.1.1.3 Void 675

8.2.1.1.4 Minimum Requirement 1 PRB allocation in presence of MBSFN 675

8.2.1.1.4A Minimum Requirement 1 PRB allocation in presence of FeMBMS Unicast-mixed Cell under CA 675

8.2.1.2 Transmit diversity performance 676

8.2.1.2.1 Minimum Requirement 2 Tx Antenna Port 676

8.2.1.2.2 Minimum Requirement 4 Tx Antenna Port 677

8.2.1.2.3 Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps with aggressor cell ABS) 677

8.2.1.2.3A Minimum Requirement 2 Tx Antenna Ports (demodulation subframe overlaps with aggressor cell ABS and CRS assistance information are configured) 679

8.2.1.2.4 Enhanced Performance Requirement Type A - 2 Tx Antenna Ports with TM3 interference model 681

8.2.1.2.5 Enhanced Performance Requirement Type B - 2 Tx Antenna Ports with TM2 interference model 683

8.2.1.2.6 Enhanced Performance Requirement Type B - 2 Tx Antenna Ports with TM9 interference model 684

8.2.1.2.7 Minimum Requirement 2 Tx Antenna Port (Superposed transmission) 685

8.2.1.3 Open-loop spatial multiplexing performance 685

8.2.1.3.1 Minimum Requirement 2 Tx Antenna Port 685

8.2.1.3.1A Soft buffer management test 689

8.2.1.3.1B Enhanced Performance Requirement Type C –2Tx Antenna Ports 690

8.2.1.3.1C Enhanced Performance Requirement Type C - 2 Tx Antenna Ports with TM1 interference 691

8.2.1.3.2 Minimum Requirement 4 Tx Antenna Port 692

8.2.1.3.3 Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps with aggressor cell ABS) 692

8.2.1.3.4 Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps with aggressor cell ABS and CRS assistance information are configured) 696

8.2.1.3.5 Minimum Requirement 2 Tx Antenna Port (Superposed transmission) 698

8.2.1.3.6 Minimum Requirement 2 Tx Antenna Port (network-based CRS interference mitigation) 699

8.2.1.4 Closed-loop spatial multiplexing performance 700

8.2.1.4.1 Minimum Requirement Single-Layer Spatial Multiplexing 2 Tx Antenna Port 700

8.2.1.4.1A Minimum Requirement Single-Layer Spatial Multiplexing 4 Tx Antenna Port 701

8.2.1.4.1B Enhanced Performance Requirement Type A - Single-Layer Spatial Multiplexing 2 Tx Antenna Port with TM4 interference model 701

8.2.1.4.1C Minimum Requirement Single-Layer Spatial Multiplexing 2 Tx Antenna Ports (demodulation subframe overlaps with aggressor cell ABS and CRS assistance information are configured) 703

8.2.1.4.1D Enhanced Performance Requirement Type B - Single-layer Spatial Multiplexing 2 Tx Antenna Port with TM4 interference model 706

8.2.1.4.1E Minimum Requirement Single-Layer Spatial Multiplexing 2 Tx Antenna Ports with CRS assistance information 708

8.2.1.4.1F Minimum Requirement Single-Layer Spatial Multiplexing 4 Tx Antenna Ports with CRS assistance information 709

8.2.1.4.2 Minimum Requirement Multi-Layer Spatial Multiplexing 2 Tx Antenna Port 710

8.2.1.4.2A Enhanced Performance Requirement Type C – Multi-layer Spatial Multiplexing 2Tx Antenna Ports 711

8.2.1.4.3 Minimum Requirement Multi-Layer Spatial Multiplexing 4 Tx Antenna Port 711

8.2.1.4.3A Minimum Requirement Multi-Layer Spatial Multiplexing 4 Tx Antenna Port for dual connectivity 715

8.2.1.4.4 Minimum Requirement Multi-Layer Spatial Multiplexing 2 Tx Antenna Port (Superposed transmission) 717

8.2.1.5 MU-MIMO 718

8.2.1.6 [Control channel performance: D-BCH and PCH] 718

8.2.1.7 Carrier aggregation with power imbalance 718

8.2.1.7.1 Minimum Requirement 718

8.2.1.8 Intra-band non-contiguous carrier aggregation with timing offset 719

8.2.1.8.1 Minimum Requirement 719

8.2.1.9 HST-SFN performance 720

8.2.1.9.1 Minimum Requirement 720

8.2.1.9.2 Minimum Requirement for Rel-16 further enhanced HST 723

8.2.1.10 Intra-band contiguous carrier aggregation with minimum channel spacing 723

8.2.1.10.1 Minimum Requirement 724

8.2.2 TDD (Fixed Reference Channel) 724

8.2.2.1 Single-antenna port performance 725

8.2.2.1.1 Minimum Requirement 725

8.2.2.1.2 Void 730

8.2.2.1.3 Void 730

8.2.2.1.4 Minimum Requirement 1 PRB allocation in presence of MBSFN 730

8.2.2.2 Transmit diversity performance 730

8.2.2.2.1 Minimum Requirement 2 Tx Antenna Port 730

8.2.2.2.2 Minimum Requirement 4 Tx Antenna Port 731

8.2.2.2.3 Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps with aggressor cell ABS) 732

8.2.2.2.3A Minimum Requirement 2 Tx Antenna Ports (demodulation subframe overlaps with aggressor cell ABS and CRS assistance information are configured) 733

8.2.2.2.4 Enhanced Performance Requirement Type A – 2 Tx Antenna Ports with TM3 interference model 735

8.2.2.2.5 Minimum Requirement 2 Tx Antenna Port (when EIMTA-MainConfigServCell-r12 is configured) 737

8.2.2.2.6 Enhanced Performance Requirement Type B - 2 Tx Antenna Ports with TM2 interference model 737

8.2.2.2.7 Enhanced Performance Requirement Type B - 2 Tx Antenna Ports with TM9 interference model 739

8.2.2.2.8 Minimum Requirement 2 Tx Antenna Port (Superposed transmission) 740

8.2.2.3 Open-loop spatial multiplexing performance 741

8.2.2.3.1 Minimum Requirement 2 Tx Antenna Port 741

8.2.2.3.1A Soft buffer management test 744

8.2.2.3.1B Enhanced Performance Requirement Type C - 2Tx Antenna Ports 744

8.2.2.3.1C Enhanced Performance Requirement Type C - 2 Tx Antenna Ports with TM1 interference 745

8.2.2.3.2 Minimum Requirement 4 Tx Antenna Port 746

8.2.2.3.3 Minimum Requirement 2Tx antenna port (demodulation subframe overlaps with aggressor cell ABS) 747

8.2.2.3.4 Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps with aggressor cell ABS and CRS assistance information are configured) 751

8.2.2.3.5 Minimum Requirement 2 Tx Antenna Port (Superposed transmission) 753

8.2.2.3.6 Minimum Requirement 2 Tx Antenna Port (network-based CRS interference mitigation) 754

8.2.2.4 Closed-loop spatial multiplexing performance 755

8.2.2.4.1 Minimum Requirement Single-Layer Spatial Multiplexing 2 Tx Antenna Port 755

8.2.2.4.1A Minimum Requirement Single-Layer Spatial Multiplexing 4 Tx Antenna Port 756

8.2.2.4.1B Enhanced Performance Requirement Type A – Single-Layer Spatial Multiplexing 2 Tx Antenna Port with TM4 interference model 756

8.2.2.4.1C Minimum Requirement Single-Layer Spatial Multiplexing 2 Tx Antenna Ports (demodulation subframe overlaps with aggressor cell ABS and CRS assistance information are configured) 758

8.2.2.4.1D Enhanced Performance Requirement Type B - Single-layer Spatial Multiplexing 2 Tx Antenna Port with TM4 interference model 760

8.2.2.4.1E Minimum Requirement Single-Layer Spatial Multiplexing 2 Tx Antenna Ports with CRS assistance information 762

8.2.2.4.1F Minimum Requirement Single-Layer Spatial Multiplexing 4 Tx Antenna Ports with CRS assistance information 763

8.2.2.4.2 Minimum Requirement Multi-Layer Spatial Multiplexing 2 Tx Antenna Port 765

8.2.2.4.2A Enhanced Performance Requirement Type C Multi-Layer Spatial Multiplexing 2 Tx Antenna Port 765

8.2.2.4.3 Minimum Requirement Multi-Layer Spatial Multiplexing 4 Tx Antenna Port 766

8.2.2.4.3A Minimum Requirement Multi-Layer Spatial Multiplexing 4 Tx Antenna Port for dual connectivity 770

8.2.2.4.4 Void 771

8.2.2.4.5 Minimum Requirement Multi-Layer Spatial Multiplexing 2 Tx Antenna Port (Superposed transmission) 771

8.2.2.5 MU-MIMO 772

8.2.2.6 [Control channel performance: D-BCH and PCH] 772

8.2.2.7 Carrier aggregation with power imbalance 772

8.2.2.7.1 Minimum Requirement 772

8.2.2.8 Intra-band contiguous carrier aggregation with minimum channel spacing 773

8.2.2.8.1 Minimum Requirement 773

8.2.2.9 HST-SFN performance 774

8.2.2.9.1 Minimum Requirement 774

8.2.2.9.2 Minimum Requirement for Rel-16 further enhanced HST 776

8.2.3 TDD FDD CA (Fixed Reference Channel) 777

8.2.3.1 Single-antenna port performance 778

8.2.3.1.1 Minimum Requirement for FDD PCell 778

8.2.3.1.2 Minimum Requirement for TDD PCell 782

8.2.3.2 Open-loop spatial multiplexing performance 2Tx Antenna port 786

8.2.3.2.1 Minimum Requirement for FDD PCell 786

8.2.3.2.1A Soft buffer management test for FDD PCell 790

8.2.3.2.2 Minimum Requirement for TDD PCell 791

8.2.3.2.2A Soft buffer management test for TDD PCell 795

8.2.3.3 Closed-loop spatial multiplexing performance 4Tx Antenna Port 796

8.2.3.3.1 Minimum Requirement for FDD PCell 796

8.2.3.3.2 Minimum Requirement for TDD PCell 800

8.2.3.4 Minimum Requirement for Closed-loop spatial multiplexing performance 4Tx Antenna Port for dual connectivity 804

8.2.3.5 HST-SFN performance 806

8.2.3.5.0 General 806

8.2.3.5.1 Minimum Requirement for FDD PCell 806

8.2.3.5.2 Minimum Requirement for TDD PCell 809

8.2.4 LAA 812

8.2.4.1 Closed-loop spatial multiplexing performance 4Tx Antenna Port 812

8.2.4.1.1 FDD PCell (FDD single carrier) 812

8.2.4.1.2 TDD PCell (TDD single carrier) 816

8.3 Demodulation of PDSCH (User-Specific Reference Symbols) 819

8.3.1 FDD 819

8.3.1.1 Single-layer Spatial Multiplexing 820

8.3.1.1A Enhanced Performance Requirement Type A – Single-layer Spatial Multiplexing with TM9 interference model 822

8.3.1.1B Single-layer Spatial Multiplexing (demodulation subframe overlaps with aggressor cell ABS and CRS assistance information are configured) 825

8.3.1.1C Enhanced Performance Requirement Type B – Single-layer Spatial Multiplexing with TM9 interference model 828

8.3.1.1D Enhanced Performance Requirement Type B – Single-layer Spatial Multiplexing with CRS interference model 830

8.3.1.1E Enhanced Performance Requirement Type B – Single-layer Spatial Multiplexing with TM3 interference model 831

8.3.1.1F Enhanced Performance Requirement Type B – Single-layer Spatial Multiplexing with TM10 serving cell configuration and TM9 interference model 832

8.3.1.1G Single-layer Spatial Multiplexing (CRS assistance information is configured) 834

8.3.1.1H Single-layer Spatial Multiplexing (With Enhanced DMRS table configured) 836

8.3.1.1I Single-layer Spatial Multiplexing (with assistance information for simultaneous transmition interfering PDSCH) 837

8.3.1.2 Dual-Layer Spatial Multiplexing 839

8.3.1.2A Enhanced Performance Requirement Type C - Dual-Layer Spatial Multiplexing 840

8.3.1.3 Performance requirements for DCI format 2D and non Quasi Co-located Antenna Ports 841

8.3.1.3.1 Minimum requirement with Same Cell ID (with single NZP CSI-RS resource) 841

8.3.1.3.2 Minimum requirements with Same Cell ID (with multiple NZP CSI-RS resources) 843

8.3.1.3.3 Minimum requirement with Different Cell ID and Colliding CRS (with single NZP CSI-RS resource) 845

8.3.1.3.4 Minimum requirement with Different Cell ID and non-colliding CRS (with single NZP CSI-RS resource and CRS assistance information is configured) 847

8.3.1.3.5 Minimum requirements with different Cell ID and non-colliding CRS (with multiple NZP CSI-RS resources and CRS assistance information is configured) 849

8.3.1.3.6 Minimum requirements for QCL Type C and 2 Layers Spatial Multiplexing 852

8.3.1.4 Performance Requirements for semiOpenLoop transmission 854

8.3.2 TDD 856

8.3.2.1 Single-layer Spatial Multiplexing 856

8.3.2.1A Single-layer Spatial Multiplexing (with multiple CSI-RS configurations) 858

8.3.2.1B Enhanced Performance Requirement Type A – Single-layer Spatial Multiplexing with TM9 interference model 860

8.3.2.1C Single-layer Spatial Multiplexing (demodulation subframe overlaps with aggressor cell ABS and CRS assistance information are configured) 863

8.3.2.1D Enhanced Performance Requirement Type B – Single-layer Spatial Multiplexing with TM9 interference 866

8.3.2.1E Enhanced Performance Requirement Type B – Single-layer Spatial Multiplexing with CRS interference model 868

8.3.2.1F Enhanced Performance Requirement Type B – Single-layer Spatial Multiplexing with TM3 interference 870

8.3.2.1G Enhanced Performance Requirement Type B – Single-layer Spatial Multiplexing with TM10 serving cell configuration and TM9 interference model 871

8.3.2.1H Single-layer Spatial Multiplexing (CRS assistance information is configured) 873

8.3.2.1I Single-layer Spatial Multiplexing (With Enhanced DMRS table configured) 875

8.3.2.1J Single-layer Spatial Multiplexing (with assistance information for simultaneous transmition interfering PDSCH) 876

8.3.2.2 Dual-Layer Spatial Multiplexing 878

8.3.2.2A Enhanced Performance Requirement Type C - Dual-Layer Spatial Multiplexing 878

8.3.2.3 Dual-Layer Spatial Multiplexing (with multiple CSI-RS configurations) 879

8.3.2.4 Performance requirements for DCI format 2D and non Quasi Co-located Antenna Ports 880

8.3.2.4.1 Minimum requirement with Same Cell ID (with single NZP CSI-RS resource) 880

8.3.2.4.2 Minimum requirements with Same Cell ID (with multiple NZP CSI-RS resources) 882

8.3.2.4.3 Minimum requirement with Different Cell ID and Colliding CRS (with single NZP CSI-RS resource) 884

8.3.2.4.4 Minimum requirement with Different Cell ID and non-Colliding CRS (with single NZP CSI-RS resource and CRS assistance information is configured) 886

8.3.2.4.5 Minimum requirements with different Cell ID and non-colliding CRS (with multiple NZP CSI-RS resources and CRS assistance information is configured) 888

8.3.2.4.6 Minimum requirements for QCL Type C and 2 Layers Spatial Multiplexing 891

8.3.2.5 Performance Requirements for semiOpenLoop transmission 893

8.3.3 LAA 895

8.3.3.1 Dual-Layer Spatial Multiplexing with DM-RS 895

8.3.3.1.1 FDD PCell (FDD single carrier) 895

8.3.3.1.2 TDD Pcell (TDD single carrier) 900

8.4 Demodulation of PDCCH/PCFICH 904

8.4.1 FDD 904

8.4.1.1 Single-antenna port performance 905

8.4.1.2 Transmit diversity performance 905

8.4.1.2.1 Minimum Requirement 2 Tx Antenna Port 905

8.4.1.2.2 Minimum Requirement 4 Tx Antenna Port 905

8.4.1.2.3 Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps with aggressor cell ABS) 906

8.4.1.2.4 Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps with aggressor cell ABS and CRS assistance information are configured) 911

8.4.1.2.5 Enhanced Downlink Control Channel Performance Requirement Type A - 2 Tx Antenna Port under Asynchronous Network 917

8.4.1.2.6 Enhanced Downlink Control Channel Performance Requirement Type A - 2 Tx Antenna Port with Non-Colliding CRS Dominant Interferer 918

8.4.1.2.7 Enhanced Downlink Control Channel Performance Requirement Type B - 2 Tx Antenna Port with Colliding CRS Dominant Interferer 919

8.4.1.2.8 Enhanced Downlink Control Channel Performance Requirement Type B - 2 Tx Antenna Port with Non-Colliding CRS Dominant Interferer 920

8.4.1.2.9 Enhanced Downlink Control Channel Performance Requirement Type A - 4 Tx Antenna Port with Non-Colliding CRS Dominant Interferer 921

8.4.2 TDD 922

8.4.2.1 Single-antenna port performance 923

8.4.2.2 Transmit diversity performance 923

8.4.2.2.1 Minimum Requirement 2 Tx Antenna Port 923

8.4.2.2.2 Minimum Requirement 4 Tx Antenna Port 924

8.4.2.2.3 Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps with aggressor cell ABS) 924

8.4.2.2.4 Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps with aggressor cell ABS and CRS assistance information are configured) 928

8.4.2.2.5 Enhanced Downlink Control Channel Performance Requirement Type A - 2 Tx Antenna Port with Colliding CRS Dominant Interferer 932

8.4.2.2.6 Enhanced Downlink Control Channel Performance Requirement Type A - 2 Tx Antenna Port with Non-Colliding CRS Dominant Interferer 933

8.4.2.2.7 Enhanced Downlink Control Channel Performance Requirement Type B - 2 Tx Antenna Port with Colliding CRS Dominant Interferer 934

8.4.2.2.8 Enhanced Downlink Control Channel Performance Requirement Type B - 2 Tx Antenna Port with Non-Colliding CRS Dominant Interferer 935

8.4.2.2.9 Enhanced Downlink Control Channel Performance Requirement Type A - 4 Tx Antenna Port with Non-Colliding CRS Dominant Interferer 936

8.4.3 LAA 937

8.4.3.1 Transmit diversity performance 937

8.4.3.1.1 FDD Pcell (FDD single carrier) 937

8.4.3.1.2 TDD Pcell (TDD single carrier) 938

8.5 Demodulation of PHICH 939

8.5.1 FDD 940

8.5.1.1 Single-antenna port performance 940

8.5.1.2 Transmit diversity performance 940

8.5.1.2.1 Minimum Requirement 2 Tx Antenna Port 940

8.5.1.2.2 Minimum Requirement 4 Tx Antenna Port 941

8.5.1.2.3 Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps with aggressor cell ABS) 941

8.5.1.2.4 Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps with aggressor cell ABS and CRS assistance information are configured) 943

8.5.1.2.5 Enhanced Downlink Control Channel Performance Requirement Type A - 2 Tx Antenna Ports under Asynchronous Network 946

8.5.1.2.6 Enhanced Downlink Control Channel Performance Requirement Type A - 2 Tx Antenna Ports with Non-Colliding CRS Dominant Interferer 947

8.5.1.2.7 Enhanced Downlink Control Channel Performance Requirement Type B - 2 Tx Antenna Ports with Colliding CRS Dominant Interferer 948

8.5.1.2.8 Enhanced Downlink Control Channel Performance Requirement Type B - 2 Tx Antenna Ports with Non-Colliding CRS Dominant Interferer 949

8.5.2 TDD 950

8.5.2.1 Single-antenna port performance 951

8.5.2.2 Transmit diversity performance 951

8.5.2.2.1 Minimum Requirement 2 Tx Antenna Port 951

8.5.2.2.2 Minimum Requirement 4 Tx Antenna Port 952

8.5.2.2.3 Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps with aggressor cell ABS) 952

8.5.2.2.4 Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps with aggressor cell ABS and CRS assistance information are configured) 954

8.5.2.2.5 Enhanced Downlink Control Channel Performance Requirement Type A - 2 Tx Antenna Ports with Colliding CRS Dominant Interferer 956

8.5.2.2.6 Enhanced Downlink Control Channel Performance Requirement Type A - 2 Tx Antenna Ports with Non-Colliding CRS Dominant Interferer 957

8.5.2.2.7 Enhanced Downlink Control Channel Performance Requirement Type B - 2 Tx Antenna Ports with Colliding CRS Dominant Interferer 958

8.5.2.2.8 Enhanced Downlink Control Channel Performance Requirement Type B - 2 Tx Antenna Ports with Non-Colliding CRS Dominant Interferer 959

8.6 Demodulation of PBCH 960

8.6.1 FDD 960

8.6.1.1 Single-antenna port performance 960

8.6.1.2 Transmit diversity performance 961

8.6.1.2.1 Minimum Requirement 2 Tx Antenna Port 961

8.6.1.2.2 Minimum Requirement 4 Tx Antenna Port 961

8.6.1.2.3 Minimum Requirement 2 Tx Antenna Port under Time Domain Measurement Resource Restriction with CRS Assistance Information 961

8.6.2 TDD 963

8.6.2.1 Single-antenna port performance 963

8.6.2.2 Transmit diversity performance 963

8.6.2.2.1 Minimum Requirement 2 Tx Antenna Port 963

8.6.2.2.2 Minimum Requirement 4 Tx Antenna Port 963

8.6.2.2.3 Minimum Requirement 2 Tx Antenna Port under Time Domain Measurement Resource Restriction with CRS Assistance Information 964

8.7 Sustained downlink data rate provided by lower layers 965

8.7.1 FDD (single carrier and CA) 965

8.7.2 TDD (single carrier and CA) 982

8.7.3 FDD (EPDCCH scheduling) 986

8.7.4 TDD (EPDCCH scheduling) 988

8.7.5 TDD FDD CA 990

8.7.5.1 Minimum Requirement FDD PCell 991

8.7.5.2 Minimum Requirement TDD PCell 999

8.7.6 FDD (DC) 1008

8.7.7 TDD (DC) 1015

8.7.8 TDD FDD (DC) 1018

8.7.9 FDD (4 Rx) 1021

8.7.10 TDD (4 Rx) 1023

8.7.11 TDD FDD CA (4 Rx) 1025

8.7.11.1 Void 1027

8.7.12 LAA 1027

8.7.12.1 FDD CA in licensed bands 1027

8.7.12.2 TDD CA in licensed bands 1029

8.7.12.3 TDD-FDD CA in licensed bands 1031

8.7.13 FDD DC (4 Rx) 1034

8.7.14 TDD DC (4 Rx) 1035

8.7.15 TDD FDD DC (4 Rx) 1037

8.7.16 FDD (1024QAM and up to 4Rx supported) 1039

8.7.17 TDD (1024QAM and up to 4 Rx supported) 1042

8.7.18 TDD FDD CA (1024QAM and up to 4 Rx supported) 1044

8.7.19 TDD (8 Rx) 1046

8.8 Demodulation of EPDCCH 1048

8.8.1 Distributed Transmission 1048

8.8.1.1 FDD 1048

8.8.1.1.1 Void 1049

8.8.1.2 TDD 1049

8.8.1.2.1 Void 1050

8.8.2 Localized Transmission with TM9 1050

8.8.2.1 FDD 1050

8.8.2.1.1 Void 1051

8.8.2.1.2 Void 1052

8.8.2.2 TDD 1052

8.8.2.2.1 Void 1053

8.8.2.2.2 Void 1053

8.8.3 Localized transmission with TM10 Type B quasi co-location type 1053

8.8.3.1 FDD 1053

8.8.3.2 TDD 1056

8.8.4 Enhanced Downlink Control Channel Performance Requirements Type A - Localized Transmission with CRS Interference Model 1059

8.8.4.1 FDD 1059

8.8.4.2 TDD 1060

8.8.5 Enhanced Downlink Control Channel Performance Requirements Type A - Distributed Transmission with TM9 Interference Model 1062

8.8.5.1 TDD 1062

8.8.6 Enhanced Downlink Control Channel Performance Requirements Type A - Distributed Transmission with TM3 Interference Model 1063

8.8.6.1 FDD 1063

8.9 Demodulation (single receiver antenna) 1064

8.9.1 PDSCH 1064

8.9.1.1 FDD and half-duplex FDD (Fixed Reference Channel) 1064

8.9.1.1.1 Transmit diversity performance (Cell-Specific Reference Symbols) 1064

8.9.1.1.2 Closed-loop spatial multiplexing performance (Cell-Specific Reference Symbols) 1065

8.9.1.1.3 Closed-loop spatial multiplexing performance (User-Specific Reference Symbols) 1067

8.9.1.2 TDD (Fixed Reference Channel) 1070

8.9.1.2.1 Transmit diversity performance (Cell-Specific Reference Symbols) 1070

8.9.1.2.2  Closed-loop spatial multiplexing performance (Cell-Specific Reference Symbols) 1071

8.9.1.2.3 Closed-loop spatial multiplexing performance (User-Specific Reference Symbols) 1074

8.9.2 PHICH 1076

8.9.2.1 FDD and half-duplex FDD 1076

8.9.2.1.1 Transmit diversity performance 1076

8.9.2.2 TDD 1076

8.9.2.2.1 Transmit diversity performance 1076

8.9.3 PBCH 1077

8.9.3.1 FDD and half-duplex FDD 1077

8.9.3.1.1 Transmit diversity performance 1077

8.9.3.2 TDD 1077

8.9.3.2.1 Transmit diversity performance 1077

8.9.4 PDCCH/PCFICH 1077

8.9.4.1 FDD and half-duplex FDD 1077

8.9.4.1.1 Enhanced Downlink Control Channel Performance Requirement Type A - 2 Tx Antenna Port with Non-Colliding CRS Dominant Interferer 1077

8.9.4.1.2 Enhanced Downlink Control Channel Performance Requirement Type A - 4 Tx Antenna Port with Non-Colliding CRS Dominant Interferer 1078

8.9.4.2 TDD 1079

8.9.4.2.1 Enhanced Downlink Control Channel Performance Requirement Type A - 2 Tx Antenna Port with Non-Colliding CRS Dominant Interferer 1079

8.9.4.2.2 Enhanced Downlink Control Channel Performance Requirement Type A - 4 Tx Antenna Port with Non-Colliding CRS Dominant Interferer 1080

8.10 Demodulation (4 receiver antenna ports) 1081

8.10.1 PDSCH 1081

8.10.1.1 FDD (Fixed Reference Channel) 1081

8.10.1.1.1 Transmit diversity performance with 2Tx Antenna Ports (Cell-Specific Reference Symbols) 1082

8.10.1.1.1A Transmit diversity performance wit Enhanced Performance Requirement Type A - 2 Tx Antenna Ports with TM3 interference model 1083

8.10.1.1.2 Open-loop spatial multiplexing performance with 2Tx Antenna Ports (Cell-Specific Reference Symbols) 1084

8.10.1.1.3 Closed-loop spatial multiplexing Enhanced Performance Requirements Type A - Single-Layer Spatial Multiplexing 2 Tx Antenna Port with TM4 interference model (Cell-Specific Reference Symbols) 1084

8.10.1.1.4 Closed-loop spatial multiplexing performance, Dual-Layer Spatial Multiplexing 4 Tx Antenna Port (Cell-Specific Reference Symbols) 1085

8.10.1.1.4A Enhanced Performance Requirement Type C - Dual-Layer Spatial Multiplexing with 2Tx Antenna Ports 1086

8.10.1.1.5 Enhanced Performance Requirement Type A – Single-layer Spatial Multiplexing with TM9 interference model (User-Specific Reference Symbols) 1087

8.10.1.1.5A Single-layer Spatial Multiplexing (User-Specific Reference Symbols) 1090

8.10.1.1.5B Single-layer Spatial Multiplexing (With Enhanced DMRS table configured) 1091

8.10.1.1.6 Dual-Layer Spatial Multiplexing (User-Specific Reference Symbols) 1092

8.10.1.1.6A Enhanced Performance Requirement Type C - Dual-Layer Spatial Multiplexing 1094

8.10.1.1.6B Dual-Layer Spatial Multiplexing with altCQI-Table-1024QAM configured (User-Specific Reference Symbols) 1095

8.10.1.1.7 Open-loop spatial multiplexing, 3 Layer Multiplexing with 4 Tx Antenna Ports (Cell-Specific Reference Symbols) 1096

8.10.1.1.7A Enhanced Performance Requirement Type C - Open-loop spatial multiplexing, 3 Layer Multiplexing with 4 Tx Antenna Ports (Cell-Specific Reference Symbols) 1096

8.10.1.1.8 Closed-loop spatial multiplexing performance, 4 Layers spatial multiplexing 4 Tx antennas (Cell-Specific Reference Symbols) 1097

8.10.1.1.9 4 Layer Spatial Multiplexing (User-Specific Reference Symbols) 1097

8.10.1.1.9A Enhanced Performance Requirement Type C - 4 Layer Spatial Multiplexing (User-Specific Reference Symbols) 1099

8.10.1.1.10 Closed loop spatial multiplexing performance - Single-Layer Spatial Multiplexing 2 Tx Antenna Port with CRS assistance information (Cell-Specific Reference Symbols) 1100

8.10.1.1.11 Closed loop spatial multiplexing performance - Single-Layer Spatial Multiplexing 4 Tx Antenna Port with CRS assistance information (Cell-Specific Reference Symbols) 1101

8.10.1.1.12 Closed loop spatial multiplexing performance - Single-Layer Spatial Multiplexing with CRS assistance information (User-Specific Reference Symbols) 1102

8.10.1.1.13 Performance requirements for DCI format 2D and non Quasi Co-located Antenna Ports 1103

8.10.1.1.14 HST-SFN performance 1107

8.10.1.2 TDD (Fixed Reference Channel) 1107

8.10.1.2.1 Transmit diversity performance with 2Tx Antenna Ports (Cell-Specific Reference Symbols) 1108

8.10.1.2.1A Transmit diversity performance with Enhanced Performance Requirement Type A – 2 Tx Antenna Ports with TM3 interference model 1109

8.10.1.2.2 Open-loop spatial multiplexing performance  with 2Tx Antenna Ports (Cell-Specific Reference Symbols) 1110

8.10.1.2.3  Closed-loop spatial multiplexing Enhanced Performance Requirements Type A - Single-Layer Spatial Multiplexing 2 Tx Antenna Port with TM4 interference model (Cell-Specific Reference Symbols) 1110

8.10.1.2.4 Closed-loop spatial multiplexing performance, Dual-Layer Spatial Multiplexing 4 Tx Antenna Ports (Cell-Specific Reference Symbols) 1111

8.10.1.2.4A Enhanced Performance Requirement Type C - Dual-Layer Spatial Multiplexing with 2Tx Antenna Ports 1112

8.10.1.2.5 Enhanced Performance Requirement Type A – Single-layer Spatial Multiplexing with TM9 interference model (User-Specific Reference Symbols) 1113

8.10.1.2.5A Single-layer Spatial Multiplexing (with multiple CSI-RS configurations) 1116

8.10.1.2.5B Single-layer Spatial Multiplexing (With Enhanced DMRS table configured) 1117

8.10.1.2.6 Dual-Layer Spatial Multiplexing (User-Specific Reference Symbols) 1118

8.10.1.2.6A Enhanced Performance Requirement Type C - Dual-Layer Spatial Multiplexing 1120

8.10.1.2.6B Dual-Layer Spatial Multiplexing with altCQI-Table-1024QAM configured (User-Specific Reference Symbols) 1121

8.10.1.2.7 Open-loop spatial multiplexing, 3 Layer Multiplexing with 4 Tx Antenna Ports (Cell-Specific Reference Symbols) 1122

8.10.1.2.7A Enhanced Performance Requirement Type C - Open-loop spatial multiplexing, 3 Layer Multiplexing with 4 Tx Antenna Ports (Cell-Specific Reference Symbols) 1122

8.10.1.2.8 Closed-loop spatial multiplexing performance, 4 Layers spatial multiplexing 4 Tx antennas 1123

8.10.1.2.9 4 Layer Spatial Multiplexing (User-Specific Reference Symbols) 1124

8.10.1.2.9A Enhanced Performance Requirement Type C - 4 Layer Spatial Multiplexing (User-Specific Reference Symbols) 1125

8.10.1.2.10 Closed loop spatial multiplexing performance - Single-Layer Spatial Multiplexing 2 Tx Antenna Port with CRS assistance information (Cell-Specific Reference Symbols) 1126

8.10.1.2.11 Closed loop spatial multiplexing performance - Single-Layer Spatial Multiplexing 4 Tx Antenna Port with CRS assistance information (Cell-Specific Reference Symbols) 1128

8.10.1.2.12 Closed loop spatial multiplexing performance - Single-Layer Spatial Multiplexing with CRS assistance information (User-Specific Reference Symbols) 1129

8.10.1.2.13 Performance requirements for DCI format 2D and non Quasi Co-located Antenna Ports 1130

8.10.1.2.14 HST-SFN performance 1134

8.10.2 PDCCH/PCFICH 1135

8.10.2.1 FDD 1135

8.10.2.1.1 Single-antenna port performance 1135

8.10.2.1.2 Transmit diversity performance with 2 Tx Antenna Ports 1135

8.10.2.1.3 Transmit diversity performance with 4 Tx Antenna Ports 1136

8.10.2.1.4 Enhanced Downlink Control Channel Performance Requirement Type A - 4 Tx Antenna Port with Non-Colliding CRS Dominant Interferer 1136

8.10.2.2 TDD 1138

8.10.2.2.1 Single-antenna port performance 1138

8.10.2.2.2 Transmit diversity performance with 2 Tx Antenna Ports 1138

8.10.2.2.3 Transmit diversity performance with 4 Tx Antenna Ports 1139

8.10.2.2.4 Enhanced Downlink Control Channel Performance Requirement Type A - 4 Tx Antenna Port with Non-Colliding CRS Dominant Interferer 1139

8.10.3 PHICH 1140

8.10.3.1  FDD 1140

8.10.3.1.1 Single Tx Antenna Port performance 1140

8.10.3.1.2 Transmit diversity performance with 2 Tx Antenna Ports 1141

8.10.3.1.3 Transmit diversity performance with 4 Tx Antenna Ports 1141

8.10.3.2 TDD 1141

8.10.3.2.1 Single Tx Antenna Port performance 1142

8.10.3.2.2 Transmit diversity performance with 2 Tx Antenna Ports 1142

8.10.3.2.3 Transmit diversity performance with 4 Tx Antenna Ports 1143

8.10.4 ePDCCH 1143

8.10.4.1 Distributed Transmission with 4Rx 1143

8.10.4.1.1 FDD 1143

8.10.4.1.2 TDD 1144

8.10.4.2 Localized Transmission with TM9 and 4Rx 1145

8.10.4.2.1 FDD 1145

8.10.4.2.2 TDD 1146

8.11 Demodulation (UE supporting coverage enhancement) 1147

8.11.1 PDSCH 1148

8.11.1.1 FDD and half-duplex FDD (Fixed Reference Channel) 1148

8.11.1.1.1 Closed-loop spatial multiplexing performance (Cell-Specific Reference Symbols) 1148

8.11.1.1.2 Closed-loop spatial multiplexing performance (User-Specific Reference Symbols) 1152

8.11.1.1.3 Transmit diversity performance (Cell-Specific Reference Symbols) 1154

8.11.1.2 TDD (Fixed Reference Channel) 1160

8.11.1.2.1 Closed-loop spatial multiplexing performance (Cell-Specific Reference Symbols) 1160

8.11.1.2.2 Closed-loop spatial multiplexing performance (User-Specific Reference Symbols) 1165

8.11.1.2.3 Transmit diversity performance (Cell-Specific Reference Symbols) 1167

8.11.2 MPDCCH 1171

8.11.2.1 FDD and half-duplex FDD 1172

8.11.2.1.1 CE Mode A 1173

8.11.2.1.2 CE Mode B 1174

8.11.2.1.3 CE Mode A with TM9 interference model 1174

8.11.2.1.4 CE Mode A with CRS interference model 1176

8.11.2.1.5 CE Mode A and CE Mode B when CRS-ChEstMPDCCH-Config is configured 1177

8.11.2.2.5 CE Mode A and CE Mode B when CRS-ChEstMPDCCH-Config is configured 1178

8.11.2.2 TDD 1180

8.11.2.2.1 CE Mode A 1181

8.11.2.2.2 CE Mode B 1182

8.11.2.2.3 CE Mode A with TM9 interference model 1182

8.11.2.2.4 CE Mode A with CRS interference model 1183

8.11.3 PBCH 1184

8.11.3.1 FDD and half-duplex FDD 1185

8.11.3.1.1 Transmit diversity performance 1185

8.11.3.2 TDD 1186

8.11.3.2.1 Transmit diversity performance 1186

8.12 Demodulation of Narrowband IoT 1186

8.12.1 NPDSCH 1186

8.12.1.1.1 Minimum Requirements for In-band 1187

8.12.1.1.2 Minimum Requirements for Standalone/Guard-band 1188

8.12.1.1.3 Minimum Requirements for Standalone for UE Category NB2 1189

8.12.1.1.4 Minimum Requirements for Standalone for UE with multiple TBs interleaved transmission 1190

8.12.1.1.5 Minimum Requirements for Standalone for UE with 16-QAM 1190

8.12.1.2 TDD 1192

8.12.1.2.1 Minimum Requirements for In-band 1192

8.12.1.2.2 Minimum Requirements for Standalone/Guard-band 1193

8.12.1.2.3 Minimum Requirements for Standalone for UE Category NB2 1194

8.12.1.2.4 Minimum Requirements for Standalone for UE with 16-QAM 1194

8.12.2 NPDCCH 1195

8.12.2.1 Half-duplex FDD 1195

8.12.2.1.1 Single-antenna performance 1196

8.12.2.1.2 Transmit diversity performance 1197

8.12.2.2 TDD 1197

8.12.2.2.1 Single-antenna performance 1199

8.12.2.2.2 Transmit diversity performance 1199

8.12.3 Demodulation of NPBCH 1199

8.12.3.1 HD-FDD 1200

8.12.3.1.1 Single-antenna port performance with single NPBCH TTI 1200

8.12.3.1.2 Transmit diversity performance 1200

8.12.3.2 TDD 1200

8.12.3.2.1 Single-antenna port performance with single NPBCH TTI 1201

8.12.3.2.2 Transmit diversity performance 1201

8.13 Demodulation of PDSCH CA and DC(4 receiver antenna ports) 1201

8.13.1 FDD (CA and DC) 1201

8.13.1.1 Closed-loop spatial multiplexing performance 1201

8.13.1.1.1 Minimum Requirement Multi-Layer Spatial Multiplexing 4 Tx Antenna Port 1201

8.13.1.1.2 Minimum Requirement Multi-Layer Spatial Multiplexing 4 Tx Antenna Port for dual connectivity 1205

8.13.1.1.3 Minimum Requirement Multi-Layer Spatial Multiplexing 4 Tx Antenna Port with 256QAM 1207

8.13.1.1.4 Minimum Requirement Four-Layer Spatial Multiplexing 4 Tx Antenna Port 1209

8.13.1.2 Dual-Layer Spatial Multiplexing (User-Specific Reference Symbols) 1210

8.13.1.2.1 Minimum Requirement Dual-Layer Spatial Multiplexing 2 Tx Antenna Port 1210

8.13.1.3 Enhanced Performance Requirements Type A Closed-loop spatial multiplexing 1213

8.13.1.3.1 Minimum Requirement Single-Layer Spatial Multiplexing 2 Tx Antenna Port with TM4 interference model (Cell-Specific Reference Symbols) 1213

8.13.1.4 Enhanced Performance Requirement Type A - Single-layer Spatial Multiplexing (User-Specific Reference Symbols) 1215

8.13.1.4.1 Minimum Requirement Enhanced Performance Requirement Type A – Single-layer Spatial Multiplexing with TM9 interference model (User-Specific Reference Symbols) 1215

8.13.2 TDD (CA and DC) 1218

8.13.2.1 Closed-loop spatial multiplexing performance 1219

8.13.2.1.1 Minimum Requirement Multi-Layer Spatial Multiplexing 4 Tx Antenna Port 1219

8.13.2.1.2 Minimum Requirement Multi-Layer Spatial Multiplexing 4 Tx Antenna Port for dual connectivity 1221

8.13.2.1.3 Minimum Requirement Multi-Layer Spatial Multiplexing 4 Tx Antenna Port with 256QAM 1222

8.13.2.1.4 Minimum Requirement Four-Layer Spatial Multiplexing 4 Tx Antenna Port 1223

8.13.2.2 Dual-Layer Spatial Multiplexing (User-Specific Reference Symbols) 1225

8.13.2.2.1 Minimum Requirement Dual-Layer Spatial Multiplexing 2 Tx Antenna Port 1225

8.13.2.4 Enhanced Performance Requirement Type A - Single-layer Spatial Multiplexing (User-Specific Reference Symbols) 1229

8.13.2.4.1 Minimum Requirement Enhanced Performance Requirement Type A – Single-layer Spatial Multiplexing with TM9 interference model (User-Specific Reference Symbols) 1229

8.13.3 TDD-FDD (CA and DC) 1231

8.13.3.1  Closed-loop spatial multiplexing performance 4Tx Antenna Port 1232

8.13.3.1.1 Minimum Requirement for FDD PCell 1232

8.13.3.1.2 Minimum Requirement for TDD PCell 1235

8.13.3.2 Dual-Layer Spatial Multiplexing (User-Specific Reference Symbols) 1239

8.13.3.2.1 Minimum Requirement Dual-Layer Spatial Multiplexing 2 Tx Antenna Port for FDD PCell 1239

8.13.3.2.2 Minimum Requirement Dual-Layer Spatial Multiplexing 2 Tx Antenna Port for TDD PCell 1242

8.13.3.3 Enhanced Performance Requirements Type A Closed-loop spatial multiplexing 1245

8.13.3.3.1 Minimum Requirement Single-Layer Spatial Multiplexing 2 Tx Antenna Port with TM4 interference model (Cell-Specific Reference Symbols) for FDD PCell 1245

8.13.3.3.2 Minimum Requirement Single-Layer Spatial Multiplexing 2 Tx Antenna Port with TM4 interference model (Cell-Specific Reference Symbols) for TDD PCell 1247

8.13.3.4 Enhanced Performance Requirement Type A - Single-layer Spatial Multiplexing (User-Specific Reference Symbols) 1249

8.13.3.4.1 Minimum Requirement Enhanced Performance Requirement Type A – Single-layer Spatial Multiplexing with TM9 interference model (User-Specific Reference Symbols) for FDD PCell 1249

8.13.3.4.2 Minimum Requirement Enhanced Performance Requirement Type A – Single-layer Spatial Multiplexing with TM9 interference model (User-Specific Reference Symbols) for TDD PCell 1252

8.13.3.5  Closed-loop spatial multiplexing performance 4Tx Antenna Port for DC 1255

8.13.3.5.1 Minimum Requirement for FDD PCell 1255

8.13.3.5.2 Minimum Requirement for TDD PCell 1257

8.13.3.6  Closed-loop spatial multiplexing performance 4Tx Antenna Port with 256QAM 1259

8.13.3.6.1 Minimum Requirement for FDD PCell 1259

8.13.3.6.2 Minimum Requirement for TDD PCell 1261

8.13.3.7  Closed-loop spatial multiplexing performance 4Tx Antenna Port with Four layers 1262

8.13.3.7.1 Minimum Requirement for FDD PCell 1262

8.13.3.7.2 Minimum Requirement for TDD PCell 1264

8.14 Demodulation (UE supporting Short TTI) 1266

8.14.1 Slot-PDSCH and Subslot-PDSCH 1266

8.14.1.1 FDD (Fixed Reference Channel) 1266

8.14.1.1.1 Open-loop spatial multiplexing performance 1266

8.14.1.1.2 Closed-loop spatial multiplexing performance (User-Specific Reference Signals) 1267

8.14.1.2 TDD (Fixed Reference Channel) 1269

8.14.1.2.1 Open-loop spatial multiplexing performance 1269

8.14.1.2.2 Closed-loop spatial multiplexing performance (User-Specific Reference Signals) 1270

8.14.2 SPDCCH 1271

8.14.2.1 FDD 1271

8.14.2.1.1 Mimimum requirement 1272

8.14.2.2 TDD 1272

8.14.2.2.1 Mimimum requirement 1273

8.15 Demodulation (8 receiver antenna ports) 1274

8.15.1 PDSCH 1274

8.15.1.1 Void 1274

8.15.1.2 TDD (Fixed Reference Channel) 1274

8.15.1.2.1 Transmit diversity performance with 2Tx Antenna Ports (Cell-Specific Reference Symbols) 1274

8.15.1.2.2 Open-loop spatial multiplexing performance with 2Tx Antenna Ports (Cell-Specific Reference Symbols) 1275

8.15.1.2.3 8 Layer Spatial Multiplexing (User-Specific Reference Symbols) 1275

8.15.2 CA 1277

8.15.2.1 Void 1277

8.15.2.2 TDD 1277

8.15.2.2.1 Eight Layer Spatial Multiplexing (User-Specific Reference Symbols) 1277

9 Reporting of Channel State Information 1279

9.1 General 1279

9.1.1 Applicability of requirements 1279

9.1.1.1 Applicability of requirements for different channel bandwidths 1279

9.1.1.2 Applicability and test rules for different CA configurations and bandwidth combination sets 1279

9.1.1.2A Applicability and test rules for different TDD-FDD CA configurations and bandwidth combination sets 1280

9.1.1.3 Test coverage for different number of componenet carriers 1281

9.1.1.4 Applicability of performance requirements for 4Rx capable UEs 1281

9.1.1.4.1 Applicability rule and antenna connection for single carrier tests with 2Rx 1281

9.1.1.4.2 Applicability rule and antenna connection for CA tests with 2Rx 1283

9.1.1.4.3 Applicability rule and antenna connection for single carrier tests with 4Rx 1284

9.1.1.5 Applicability of requirements for UEs supporting coverage enhancement 1284

9.2  CQI reporting definition under AWGN conditions 1284

9.2.1 Minimum requirement PUCCH 1-0 (Cell-Specific Reference Symbols) 1284

9.2.1.1 FDD 1284

9.2.1.2 TDD 1285

9.2.1.3 FDD (CSI measurements in case two CSI subframe sets are configured) 1286

9.2.1.4 TDD (CSI measurements in case two CSI subframe sets are configured) 1289

9.2.1.5 FDD (CSI measurements in case two CSI subframe sets are configured and with CRS assistance information) 1292

9.2.1.6 TDD (CSI measurements in case two CSI subframe sets are configured and with CRS assistance information) 1295

9.2.1.7 FDD (Modulation and TBS index Table 2 and 4-bit CQI Table 2 are used) 1298

9.2.1.8 TDD (Modulation and TBS index Table 2 and 4-bit CQI Table 2 are used) 1299

9.2.1.9 FDD (Modulation and TBS index Table 3 and 4-bit CQI Table 4 are used) 1299

9.2.1.10 TDD (Modulation and TBS index Table 3 and 4-bit CQI Table 4 are used) 1300

9.2.2 Minimum requirement PUCCH 1-1 (Cell-Specific Reference Symbols) 1301

9.2.2.1 FDD 1301

9.2.2.2 TDD 1302

9.2.3 Minimum requirement PUCCH 1-1 (CSI Reference Symbols) 1303

9.2.3.1 FDD 1303

9.2.3.1A FDD (With channelMeasRestriction configured) 1304

9.2.3.2 TDD 1305

9.2.3.2A TDD (With channelMeasRestriction configured) 1306

9.2.4 Minimum requirement PUCCH 1-1 (With Single CSI Process) 1307

9.2.4.1 FDD 1308

9.2.4.1A FDD (With interferenceMeasRestriction configured) 1310

9.2.4.2 TDD 1313

9.2.4.2A TDD (With interferenceMeasRestriction configured) 1316

9.2.5 Minimum requirement PUCCH 1-1 (when csi-SubframeSet –r12 and EIMTA-MainConfigServCell-r12 are configured) 1319

9.2.6 Minimum requirement PUSCH 3-0 (Cell-Specific Reference Symbols) 1322

9.2.6.1 Frame structure type 3 with FDD Pcell 1322

9.2.6.2 Frame structure type 3 with TDD Pcell 1324

9.2.7 Minimum requirement PUSCH 3-1 (CSI Reference Symbol) 1326

9.2.7.1 Frame structure type 3 wth FDD Pcell 1326

9.2.7.2 Frame structure type 3 wth TDD Pcell 1328

9.3 CQI reporting under fading conditions 1332

9.3.1 Frequency-selective scheduling mode 1332

9.3.1.1 Minimum requirement PUSCH 3-0 (Cell-Specific Reference Symbols) 1332

9.3.1.1.1 FDD 1332

9.3.1.1.2 TDD 1333

9.3.1.1.3 FDD (CSI measurements in case two CSI subframe sets are configured and with CRS assistance information) 1334

9.3.1.1.4 TDD (CSI measurements in case two CSI subframe sets are configured and with CRS assistance information) 1338

9.3.1.1.5 TDD (when csi-SubframeSet –r12 is configured) 1341

9.3.1.2 Minimum requirement PUSCH 3-1 (CSI Reference Symbol) 1343

9.3.1.2.1 FDD 1343

9.3.1.2.2 TDD 1344

9.3.1.2.3 FDD (Modulation and TBS index Table 2 and 4-bit CQI Table 2 are used) 1346

9.3.1.2.4 TDD (Modulation and TBS index Table 2 and 4-bit CQI Table 2 are used) 1347

9.3.1.2.5 Void 1348

9.3.1.2.6 TDD (when csi-SubframeSet –r12 is configured with one CSI process) 1348

9.3.2 Frequency non-selective scheduling mode 1352

9.3.2.1 Minimum requirement PUCCH 1-0 (Cell-Specific Reference Symbol) 1352

9.3.2.1.1 FDD 1352

9.3.2.1.2 TDD 1354

9.3.2.2 Minimum requirement PUCCH 1-1 (CSI Reference Symbol) 1356

9.3.2.2.1 FDD 1356

9.3.2.2.2 TDD 1357

9.3.3 Frequency-selective interference 1359

9.3.3.1 Minimum requirement PUSCH 3-0 (Cell-Specific Reference Symbol) 1359

9.3.3.1.1 FDD 1359

9.3.3.1.2 TDD 1360

9.3.3.2 Void 1361

9.3.3.2.1 Void 1361

9.3.3.2.2 Void 1361

9.3.4 UE-selected subband CQI 1361

9.3.4.1 Minimum requirement PUSCH 2-0 (Cell-Specific Reference Symbols) 1362

9.3.4.1.1 FDD 1362

9.3.4.1.2 TDD 1363

9.3.4.2 Minimum requirement PUCCH 2-0 (Cell-Specific Reference Symbols) 1364

9.3.4.2.1 FDD 1364

9.3.4.2.2 TDD 1366

9.3.5 Additional requirements for enhanced receiver Type A 1368

9.3.5.1 Minimum requirement PUCCH 1-0 (Cell-Specific Reference Symbol) 1368

9.3.5.1.1 FDD 1368

9.3.5.1.2 TDD 1369

9.3.5.2 Minimum requirement PUCCH 1-1 (CSI Reference Symbol) 1372

9.3.5.2.1 FDD 1372

9.3.5.2.2 TDD 1375

9.3.6 Minimum requirement (With multiple CSI processes) 1378

9.3.6.1 FDD 1379

9.3.6.2 TDD 1383

9.3.7 Minimum requirement PUSCH 3-2 1387

9.3.7.1 FDD 1387

9.3.7.2 TDD 1388

9.3.8 Additional requirements for enhanced receiver Type B 1390

9.3.8.1 Minimum requirement PUCCH 1-1 (Cell-Specific Reference Symbols) 1390

9.3.8.1.1 FDD 1390

9.3.8.1.2 TDD 1391

9.3.8.2 Minimum requirement PUCCH 1-1 (CSI Reference Symbols) 1393

9.3.8.2.1 FDD 1393

9.3.8.2.2 TDD 1395

9.3.8.3 Minimum requirement with CSI process 1398

9.3.8.3.1 FDD 1398

9.3.8.3.2 TDD 1401

9.4 Reporting of Precoding Matrix Indicator (PMI) 1404

9.4.1 Single PMI 1405

9.4.1.1 Minimum requirement PUSCH 3-1 (Cell-Specific Reference Symbols) 1405

9.4.1.1.1 FDD 1405

9.4.1.1.2 TDD 1406

9.4.1.2  Minimum requirement PUCCH 2-1 (Cell-Specific Reference Symbols) 1407

9.4.1.2.1 FDD 1407

9.4.1.2.2 TDD 1409

9.4.1.3 Minimum requirement PUSCH 3-1 (CSI Reference Symbol) 1410

9.4.1.3.1 FDD 1410

9.4.1.3.2 TDD 1413

9.4.1.3.3 FDD (with Class A 12Tx codebook) 1416

9.4.1.3.4 TDD (with Class A 12Tx codebook) 1418

9.4.1.3.5 FDD (with Class A 24Tx codebook) 1421

9.4.1.3.6 TDD (with Class A 24Tx codebook) 1423

9.4.1.4 Minimum requirement PUCCH 1-1 (CSI Reference Symbol) 1426

9.4.1.4.1 FDD (with 4Tx enhanced codebook) 1426

9.4.1.4.2 TDD (with 4Tx enhanced codebook) 1428

9.4.1.4.3 FDD (with Class B alternative codebook for one CSI-RS resource configured) 1431

9.4.1.4.4 TDD (with Class B alternative codebook for one CSI-RS resource configured) 1433

9.4.1a Void 1436

9.4.1a.1 Void 1436

9.4.1a.1.1 Void 1436

9.4.1a.1.2 Void 1436

9.4.2 Multiple PMI 1436

9.4.2.1 Minimum requirement PUSCH 1-2 (Cell-Specific Reference Symbols) 1436

9.4.2.1.1 FDD 1436

9.4.2.1.2 TDD 1437

9.4.2.2  Minimum requirement PUSCH 2-2 (Cell-Specific Reference Symbols) 1438

9.4.2.2.1 FDD 1438

9.4.2.2.2 TDD 1439

9.4.2.3 Minimum requirement PUSCH 1-2 (CSI Reference Symbol) 1440

9.4.2.3.1 FDD 1440

9.4.2.3.2 TDD 1442

9.4.2.3.3 FDD (with 4Tx enhanced codebook) 1445

9.4.2.3.4 TDD (with 4Tx enhanced codebook) 1447

9.4.2.3.5 FDD (with Class A 16Tx codebook) 1449

9.4.2.3.6 TDD (with Class A 16Tx codebook) 1452

9.4.2.3.7 FDD (with Class A 32Tx codebook) 1455

9.4.2.3.8 TDD (with Class A 32Tx codebook) 1458

9.4.2.3.9 FDD (with Class A 16Tx advanced codebook) 1461

9.4.2.3.10 TDD (with Class A 16Tx advanced codebook) 1464

9.4.3 Void 1467

9.5 Reporting of Rank Indicator (RI) 1467

9.5.1 Minimum requirement (Cell-Specific Reference Symbols) 1467

9.5.1.1 FDD 1467

9.5.1.2 TDD 1468

9.5.2 Minimum requirement (CSI Reference Symbols) 1469

9.5.2.1 FDD 1469

9.5.2.2 TDD 1471

9.5.3 Minimum requirement (CSI measurements in case two CSI subframe sets are configured) 1473

9.5.3.1 FDD 1473

9.5.3.2 TDD 1476

9.5.4 Minimum requirement (CSI measurements in case two CSI subframe sets are configured and CRS assistance information are configured) 1479

9.5.4.1 FDD 1479

9.5.4.2 TDD 1482

9.5.5 Minimum requirement (with CSI process) 1485

9.5.5.1 FDD 1486

9.5.5.2 TDD 1489

9.6  Additional requirements for carrier aggregation 1492

9.6.1  Periodic reporting on multiple cells (Cell-Specific Reference Symbols) 1492

9.6.1.1 FDD 1492

9.6.1.2 TDD 1498

9.6.1.3 TDD-FDD CA with FDD PCell 1504

9.6.1.4 TDD-FDD CA with TDD PCell 1509

9.7 CSI reporting (Single receiver antenna) 1515

9.7.1 CQI reporting definition under AWGN conditions 1516

9.7.1.1 FDD and half-duplex FDD 1516

9.7.1.2 TDD 1516

9.7.1.3 FDD (Category 1bis UE) 1517

9.7.1.4 TDD (Category 1bis UE) 1518

9.7.2 CQI reporting under fading conditions 1519

9.7.2.1 FDD and half-duplex FDD 1519

9.7.2.2 TDD 1520

9.7.2.3 FDD (Category 1bis UE) 1521

9.7.2.4 TDD (Category 1bis UE) 1522

9.8 CSI reporting (UE supporting coverage enhancement) 1523

9.8.1 CQI reporting definition under AWGN conditions 1523

9.8.1.1 FDD and half-duplex FDD 1523

9.8.1.2 TDD 1524

9.8.2 UE-selected subband CQI 1525

9.8.2.1 FDD and half-duplex FDD 1525

9.8.2.2 TDD 1529

9.8.3 CQI reporting definition for UE supporting 64QAM under AWGN 1532

9.8.3.1 FDD and half-duplex FDD 1532

9.8.3.2 TDD 1533

9.8.4 CQI reporting definition for UE supporting alternative table under AWGN 1534

9.8.4.1 FDD and half-duplex FDD 1534

9.8.4.2 TDD 1535

9.8.5 PMI reporting with PUCCH 1-1 (CSI Reference Symbol) 1536

9.8.5.1 FDD 1537

9.8.5.2 TDD 1538

9.9 CSI reporting for 4Rx UE 1539

9.9.1 CQI reporting definition under AWGN conditions 1539

9.9.1.1 Minimum requirement PUCCH 1-0 with Rank 1 (Cell-Specific Reference Symbols) 1540

9.9.1.1.1 FDD 1540

9.9.1.1.2 TDD 1540

9.9.1.2 Minimum requirement PUCCH 1-1 with Rank 2 (CSI Reference Symbols) 1541

9.9.1.2.1 FDD 1541

9.9.1.2.2 TDD 1542

9.9.1.3  Minimum requirement PUCCH 1-1 with Rank 4 (Cell-Specific Reference Symbols) 1543

9.9.1.3.1 FDD 1544

9.9.1.3.2 TDD 1544

9.9.1.4 Minimum requirement PUCCH 1-1 with Rank 3 (CSI Reference Symbols) 1545

9.9.1.4.1 FDD 1545

9.9.1.4.2 TDD 1546

9.9.2 CQI reporting definition under fading conditions 1547

9.9.2.1 Minimum requirement PUCCH 1-0 (Cell-Specific Reference Symbol) for enhanced receiver Type A 1547

9.9.2.1.1 FDD 1548

9.9.2.1.2 TDD 1549

9.9.2.2 Minimum requirement PUCCH 1-1 (CSI Reference Symbol) for enhanced receiver Type A 1552

9.9.2.2.1 FDD 1552

9.9.2.2.2 TDD 1555

9.9.3 Reporting of Precoding Matrix Indicator (PMI) for 4Rx UE 1558

9.9.3.1 Minimum requirement PUSCH 3-1 (CSI Reference Symbol) 1559

9.9.3.1.1 TDD 1559

9.9.4  Reporting of Rank Indicator (RI) 1561

9.9.4.1 Minimum requirement (Cell-Specific Reference Symbols) 1561

9.9.4.1.1 FDD 1561

9.9.4.1.2 TDD 1563

9.9.4.2 Minimum requirement (CSI Reference Symbols) 1564

9.9.4.2.1 FDD 1564

9.9.4.2.2 TDD 1566

9.10 Reporting of CSI-RS Resource Indicator (CRI) 1568

9.10.1 Minimum requirement (PUSCH 3-1) 1569

9.10.1.1 FDD 1569

9.10.1.2 TDD 1571

9.10.2 Minimum requirement (PUSCH 3-1, QCL Type C) 1573

9.10.2.1 FDD 1573

9.10.2.2 TDD 1576

9.11 Reporting of Hybrid Channel state information 1579

9.11.1 Minimum requirement (with eMIMO-Type configured as Class B with more than one CSI-RS resource configured and eMIMO-Type2 as Class B with one CSI-RS resource configured) 1579

9.11.1.1 FDD 1580

9.11.1.2 TDD 1582

9.12 CSI reporting (UE supporting Short TTI) 1584

9.12.1 CQI reporting under fading conditions (Cell-Specific Reference Symbol) 1584

9.12.1.1 FDD 1584

9.12.1.2 TDD 1587

9.12.2 CQI reporting under fading conditions (CSI Reference Symbol) 1589

9.12.2.1 FDD 1589

9.12.2.2 TDD 1592

9.13 CSI reporting for 8Rx UE 1594

9.13.1 CQI reporting definition under AWGN conditions 1594

9.13.1.1 Minimum requirement PUCCH 1-1 with Rank 4 (CSI Reference Symbols) 1594

9.13.1.2.1 Void 1594

9.13.1.2.2 TDD 1594

9.14 CSI reporting of Narrowband IoT 1595

9.14.1 CQI reporting definition under AWGN conditions 1595

9.14.1.1 Half-duplex FDD 1595

9.14.1.2 TDD 1596

10 Performance requirement (MBMS) 1597

10.1 FDD (Fixed Reference Channel) 1597

10.1.1 Minimum requirement 1598

10.2 TDD (Fixed Reference Channel) 1599

10.2.1 Minimum requirement 1599

10.3 FDD (Fixed Reference Channel) with FeMBMS 1600

10.3.1 Minimum requirement for FeMBMS Unicast-mixed Cell under CA 1600

10.3.1.1 Minimum requirement with 1.25kHz subcarrier spacing 1600

10.3.1.2 Minimum requirement with 7.5kHz subcarrier spacing 1601

10.3.2 Minimum requirement for FeMBMS Unicast-mixed Cell as Non-Serving Cell 1602

10.3.2.1 Minimum requirement with 1.25kHz subcarrier spacing 1602

10.3.2.2 Minimum requirement with 7.5kHz subcarrier spacing 1603

10.3.3 Minimum requirement for MBMS Dedicated cell 1604

10.3.3.1 Minimum requirement with 1.25kHz subcarrier spacing 1604

10.3.3.2 Minimum requirement with 7.5kHz subcarrier spacing 1605

10.3.3.3 Minimum requirement with 15kHz subcarrier spacing 1606

10.4 FDD with LTE based 5G terrestrial broadcast 1607

10.4.1 Minimum requirement for PMCH decoding 1607

10.4.1.1 Minimum requirement with 0.37kHz subcarrier spacing 1607

10.4.1.2 Minimum requirement with 2.5kHz subcarrier spacing 1609

10.4.1.3  Minimum requirement with 1.25kHz subcarrier spacing 1610

10.4.2 Minimum requirement for CAS detection 1611

10.4.2.1 Minimum requirement for PBCH detection 1611

11 Performance requirement (ProSe Direct Discovery) 1612

11.1 General 1612

11.1.1 Applicability of requirements 1612

11.1.2 Reference DRX configuration 1613

11.2 Demodulation of PSDCH (single link performance) 1613

11.2.1 FDD (in-coverage) 1613

11.2.2 TDD (in-coverage) 1614

11.2.3 FDD (out-of-coverage) 1615

11.3 Power imbalance performance with two links 1615

11.3.1 FDD 1615

11.3.2 TDD 1616

11.4 Multiple timing reference test 1617

11.4.1 FDD 1618

11.5 Maximum Sidelink processes test 1619

11.5.1 FDD 1619

11.5.2 TDD 1620

12 Performance requirement (ProSe Direct Communication) 1622

12.1 General 1622

12.1.1 Applicability of requirements 1622

12.1.1.1 Applicability of requirements for different channel bandwidths 1622

12.1.1.2 Test coverage for different number of component carriers 1622

12.1.1.3 Applicability and test rules for different CA configurations and bandwidth combination sets 1622

12.1.2 Reference DRX configuration 1623

12.2 Demodulation of PSSCH 1623

12.2.1 FDD 1623

12.3 Demodulation of PSCCH 1624

12.3.1 FDD 1625

12.4 Demodulation of PSBCH 1626

12.4.1 FDD 1626

12.5 Power imbalance performance with two links 1626

12.5.1  FDD 1626

12.6 Multiple timing reference test 1628

12.6.1 FDD 1628

12.7 Maximum Sidelink processes test 1631

12.7.1 FDD 1631

12.8 Sustained downlink data rate with active Sidelink 1632

13 Void 1634

14 Performance requirement (V2X Sidelink Communication) 1634

14.1 General 1634

14.1.1 Applicability of requirements 1634

14.2 Demodulation of PSSCH 1635

14.3 Demodulation of PSCCH 1636

14.4 Power imbalance performance with two links 1636

14.5 Demodulation of PSBCH 1637

14.6 Demodulation of PSSCH with eNB based synchronization 1638

14.7 Soft buffer test 1638

14.8 PSCCH/PSSCH decoding capability test 1639

14.9 Sustained downlink data rate with active sidelink 1640

14.10 Soft buffer test (CA) 1641

14.11 PSCCH/PSSCH decoding capability test (CA) 1642

Annex A (normative):  Measurement channels 1645

A.1 General 1645

A.2 UL reference measurement channels 1645

A.2.1 General 1645

A.2.1.1 Applicability and common parameters 1645

A.2.1.2 Determination of payload size 1645

A.2.1.3 Overview of UL reference measurement channels 1646

A.2.2 Reference measurement channels for FDD 1669

A.2.2.1 Full RB allocation 1669

A.2.2.1.1 QPSK 1669

A.2.2.1.2 16-QAM 1671

A.2.2.1.3 64-QAM 1673

A.2.2.1.4 256 QAM 1674

A.2.2.2 Partial RB allocation 1674

A.2.2.2.1 QPSK 1675

A.2.2.2.2 16-QAM 1678

A.2.2.2.3 64-QAM 1680

A.2.2.2.4 256 QAM 1682

A.2.2.3 Void 1682

A.2.2.4 subPRB allocation 1683

A.2.3 Reference measurement channels for TDD 1683

A.2.3.1 Full RB allocation 1683

A.2.3.1.1 QPSK 1683

A.2.3.1.2 16-QAM 1686

A.2.3.1.3 64-QAM 1688

A.2.3.1.4 256 QAM 1689

A.2.3.2 Partial RB allocation 1689

A.2.3.2.1 QPSK 1690

A.2.3.2.2 16-QAM 1694

A.2.3.2.3 64-QAM 1699

A.2.3.2.4 256 QAM 1701

A.2.3.3 Void 1701

A.2.3.4 subPRB allocation 1702

A.2.4 Reference measurement channels for UE category NB1 1702

A.2.5 Reference measurement channels for LAA 1703

A.2.5.1 Full RB allocation 1703

A.2.5.1.1 QPSK 1703

A.2.5.1.2 16QAM 1704

A.2.5.1.3 64QAM 1704

A.2.5.2 Partial RB allocation 1704

A.2.5.2.1 QPSK 1705

A.2.5.2.2 16QAM 1705

A.2.5.2.3 64QAM 1706

A.3 DL reference measurement channels 1706

A.3.1 General 1706

A.3.1.1 Overview of DL reference measurement channels 1707

A.3.2 Reference measurement channel for receiver characteristics 1732

A.3.3 Reference measurement channels for PDSCH performance requirements (FDD) 1762

A.3.3.1 Single-antenna transmission (Common Reference Symbols) 1762

A.3.3.2 Multi-antenna transmission (Common Reference Symbols) 1767

A.3.3.2.1 Two antenna ports 1767

A.3.3.2.2 Four antenna ports 1776

A.3.3.3 Reference Measurement Channel for UE-Specific Reference Symbols 1781

A.3.3.3.0 Two antenna ports (no CSI-RS) 1781

A.3.3.3.1 Two antenna port (CSI-RS) 1782

A.3.3.3.2 Four antenna ports (CSI-RS) 1785

A.3.3.3.2A Eight antenna ports (CSI-RS) 1792

A.3.3.3.3 Twelve antenna port (CSI-RS) 1794

A.3.3.3.4 Sixteen antenna port (CSI-RS) 1795

A.3.3.3.5 Twenty-four antenna port (CSI-RS) 1796

A.3.3.3.6 Thirty-two antenna port (CSI-RS) 1797

A.3.4 Reference measurement channels for PDSCH performance requirements (TDD) 1799

A.3.4.1 Single-antenna transmission (Common Reference Symbols) 1799

A.3.4.2 Multi-antenna transmission (Common Reference Signals) 1807

A.3.4.2.1 Two antenna ports 1807

A.3.4.2.2 Four antenna ports 1820

A.3.4.3 Reference Measurement Channels for UE-Specific Reference Symbols 1827

A.3.4.3.1 Single antenna port (Cell Specific) 1827

A.3.4.3.2 Two antenna ports (Cell Specific) 1828

A.3.4.3.3 Two antenna ports (CSI-RS) 1830

A.3.4.3.4 Four antenna ports (CSI-RS) 1838

A.3.4.3.5 Eight antenna ports (CSI-RS) 1845

A.3.4.3.6 Twelve antenna ports (CSI-RS) 1851

A.3.4.3.7 Sixteen antenna ports (CSI-RS) 1852

A.3.4.3.8 Twenty-four antenna ports (CSI-RS) 1853

A.3.4.3.9 Thirty-two antenna ports (CSI-RS) 1854

A.3.5 Reference measurement channels for PDCCH/PCFICH performance requirements 1856

A.3.5.1 FDD 1856

A.3.5.2 TDD 1856

A.3.5.3 LAA 1857

A.3.6 Reference measurement channels for PHICH performance requirements 1857

A.3.7 Reference measurement channels for PBCH performance requirements 1857

A.3.8 Reference measurement channels for MBMS performance requirements 1858

A.3.8.1 FDD 1858

A.3.8.2 TDD 1864

A.3.9 Reference measurement channels for sustained downlink data rate provided by lower layers 1866

A.3.9.1 FDD 1866

A.3.9.2 TDD 1870

A.3.9.3 FDD (EPDCCH scheduling) 1884

A.3.9.4 TDD (EPDCCH scheduling) 1885

A.3.9.5 LAA 1887

A.3.10 Reference Measurement Channels for EPDCCH performance requirements 1889

A.3.10.1 FDD 1889

A.3.10.2 TDD 1889

A.3.11 Reference Measurement Channels for MPDCCH performance requirements 1889

A.3.11.1 FDD and half-duplex FDD 1889

A.3.11.2 TDD 1890

A.3.12 Reference measurement channels for NPDSCH performance requirements 1891

A.3.12.1 In-band 1891

A.3.12.1.2 Two-antenna transmission 1891

A.3.12.2 Standalone/Guard-band 1893

A.3.12.2.1 Single-antenna transmission 1893

A.3.13 Reference measurement channels for NPDCCH performance requirements 1896

A.3.13.1 Half-duplex FDD 1896

A.3.13.2 TDD 1897

A.3.14 Reference measurement channels for NPBCH performance requirements for Cat NB1 UEs 1897

A.3.15 Reference Measurement Channels for LAA SCell with frame structure Type-3 1898

A.3.15.1 Multi-antenna transmission (Common Reference Symbols) 1898

A.3.15.1.1 Four antenna ports 1898

A.3.15.2 Reference Measurement Channel for UE-Specific Reference Symbols 1898

A.3.15.2.1 Two antenna ports (CSI-RS) 1898

A.3.16 Reference measurement channels for Slot-PDSCH and Subslot-PDSCH performance requirements 1900

A.3.16.1 FDD 1900

A.3.16.2 TDD 1904

A.3.17 Reference measurement channels for SPDCCH performance requirements 1905

A.3.17.1 FDD 1905

A.3.17.2 TDD 1906

A.3.18 Reference Measurement Channels for LTE based 5G broadcast PMCH receiver requirements 1906

A.3.18.1 SDO 1906

A.4 CSI reference measurement channels 1908

A.5 OFDMA Channel Noise Generator (OCNG) 1923

A.5.1 OCNG Patterns for FDD 1923

A.5.1.1 OCNG FDD pattern 1: One sided dynamic OCNG FDD pattern 1923

A.5.1.2 OCNG FDD pattern 2: Two sided dynamic OCNG FDD pattern 1924

A.5.1.3 OCNG FDD pattern 3: 49 RB OCNG allocation with MBSFN in 10 MHz 1924

A.5.1.3A OCNG FDD pattern 3A: 49 RB OCNG allocation with MBSFN enhancement in 10 MHz 1925

A.5.1.4 OCNG FDD pattern 4: One sided dynamic OCNG FDD pattern for MBMS transmission 1925

A.5.1.4A OCNG FDD pattern 4A: One sided dynamic OCNG FDD pattern for enhanced MBMS transmission 1926

A.5.1.5 OCNG FDD pattern 5: One sided dynamic 16QAM modulated OCNG FDD pattern 1927

A.5.1.6 OCNG FDD pattern 6: dynamic OCNG FDD pattern when user data is in 2 non-contiguous blocks 1928

A.5.1.8 OCNG FDD pattern 8: Dynamic OCNG FDD pattern for TM10 transmission 1929

A.5.2 OCNG Patterns for TDD 1930

A.5.2.1 OCNG TDD pattern 1: One sided dynamic OCNG TDD pattern 1930

A.5.2.2 OCNG TDD pattern 2: Two sided dynamic OCNG TDD pattern 1931

A.5.2.3 OCNG TDD pattern 3: 49 RB OCNG allocation with MBSFN in 10 MHz 1932

A.5.2.4 OCNG TDD pattern 4: One sided dynamic OCNG TDD pattern for MBMS transmission 1932

A.5.2.5 OCNG TDD pattern 5: One sided dynamic 16QAM modulated OCNG TDD pattern 1933

A.5.2.6 OCNG TDD pattern 6: dynamic OCNG TDD pattern when user data is in 2 non-contiguous blocks 1934

A.5.2.8 OCNG TDD pattern 8: Dynamic OCNG TDD pattern for TM10 transmission 1935

A.5.3 OCNG Patterns for Narrowband IoT 1936

A.5.3.1 Narrowband IoT OCNG pattern 1 1936

A.5.4 OCNG Patterns for frame structure type 3 1937

A.5.4.1 OCNG FS3 pattern 1: One sided dynamic OCNG frame structure type 3 pattern 1937

A.5.4.2 OCNG FS3 pattern 2: Two sided dynamic OCNG frame structure 3 pattern 1938

A.6 Sidelink reference measurement channels 1939

A.6.1 General 1939

A.6.1.1 Overview of ProSe reference measurement channels 1939

A.6.2 Reference measurement channel for receiver characteristics 1940

A.6.3 Reference measurement channels for PSDCH performance requirements 1942

A.6.4 Reference measurement channels for PSCCH performance requirements 1943

A.6.5 Reference measurement channels for PSSCH performance requirements 1943

A.6.6 Reference measurement channels for PSBCH performance requirements 1944

A.7 Sidelink reference resource pool configurations 1945

A.7.1 Reference resource pool configurations for ProSe Direct Discovery demodulation tests 1945

A.7.1.1 FDD 1945

A.7.1.2 TDD 1948

A.7.2 Reference resource pool configurations for ProSe Direct Communication demodulation tests 1950

A.7.2.1 FDD 1950

A.8 V2X reference measurement channels 1955

A.8.1 General 1955

A.8.1.1 Overview of V2X reference measurement channels 1956

A.8.2 Reference measurement channel for receiver characteristics 1956

A.8.3 Reference measurement channel for transmitter characteristics 1958

A.8.4 Reference measurement for PSCCH performance requirements 1961

A.8.5 Reference measurement for PSSCH performance requirements 1962

A.8.6 Reference measurement for PSBCH performance requirements 1962

A.9 V2X reference resource pool configurations 1963

Annex B (normative):  Propagation conditions 1966

B.1 Static propagation condition 1966

B.1.1 UE Receiver with 2Rx 1966

B.1.2 UE Receiver with 4Rx 1966

B.1.3 UE Receiver with 8Rx 1967

B.2 Multi-path fading propagation conditions 1968

B.2.1 Delay profiles 1968

B.2.2 Combinations of channel model parameters 1969

B.2.3 MIMO Channel Correlation Matrices 1970

B.2.3.1 Definition of MIMO Correlation Matrices 1970

B.2.3.2 MIMO Correlation Matrices at High, Medium and Low Level 1976

B.2.3A MIMO Channel Correlation Matrices using cross polarized antennas 1979

B.2.3A.1 Definition of MIMO Correlation Matrices using cross polarized antennas 1980

B.2.3A.2 Spatial Correlation Matrices using cross polarized antennas at eNB and UE sides 1980

B.2.3A.2.1 Spatial Correlation Matrices at eNB side 1980

B.2.3A.2.2 Spatial Correlation Matrices at UE side 1981

B.2.3A.4 Beam steering approach 1984

B.2.3B MIMO Channel Correlation Matrices using two-dimension cross polarized antennas at eNB and cross polarized antennas at UE 1984

B.2.3B.1 Definition of MIMO Correlation Matrices using two-dimension cross polarized antennas at eNB and cross polarized antennas at UE 1985

B.2.3B.2 Spatial Correlation Matrices using two-dimension cross polarized antennas at eNB and cross polarized antennas at UE 1986

B.2.3B.2.1 Spatial Correlation Matrices at eNB side 1986

B.2.3B.2.2 Spatial Correlation Matrices at UE side 1986

B.2.3B.3 MIMO Correlation Matrices using two-dimension cross polarized antennas at eNB and cross polarized antennas at UE 1986

B.2.3B.4 Beam steering approach 1989

B.2.3B.4A Beam steering approach with dual cluster beams 1990

B.2.4 Propagation conditions for CQI tests 1991

B.2.4.1 Propagation conditions for CQI tests with multiple CSI processes 1991

B.2.5 Void 1991

B.2.6 MBSFN Propagation Channel Profile 1991

B.2.6.1 Subcarrier spacing 15kHz or 7.5kHz 1991

B.2.6.2 Subcarrier spacing 1.25kHz 1992

B.2.6.3 Subcarrier spacing 0.37kHz 1994

B.2.6.4 Subcarrier spacing 2.5kHz 1995

B.3 High speed train scenario 1995

B.3A HST-SFN scenario 1996

B.3B HST-SFN scenario for 500km/h speed 2000

B.3C HST scenario for 500km/h speed 2000

B.4 Beamforming Model 2000

B.4.1 Single-layer random beamforming (Antenna port 5, 7, or 8) 2000

B.4.1A Single-layer random beamforming (Antenna port 7, 8, 11 or 13 with enhanced DMRS table configured) 2001

B.4.2 Dual-layer random beamforming (antenna ports 7 and 8) 2001

B.4.3 Generic beamforming model (antenna ports 7-14) 2002

B.4.4 Random beamforming for EPDCCH distributed transmission (Antenna port 107 and 109) 2002

B.4.5 Random beamforming for EPDCCH localized transmission (Antenna port 107, 108, 109 or 110) 2003

B.4.6 Beamforming model for CRI test 2003

B.5 Interference models for enhanced performance requirements Type-A 2004

B.5.1 Dominant interferer proportion 2005

B.5.2 Transmission mode 3 interference model 2005

B.5.3 Transmission mode 4 interference model 2005

B.5.4 Transmission mode 9 interference model 2006

B.6 Interference models for enhanced performance requirements Type-B 2006

B.6.1 Transmission mode 2 interference model 2006

B.6.2 Transmission mode 3 interference model 2006

B.6.3 Transmission mode 4 interference model 2007

B.6.4 Transmission mode 9 interference model 2007

B.6.5 CRS interference model 2008

B.6.6 Random interference model 2008

B.7 Interference models for enhanced downlink control channel performance requirements Type A and B 2009

B.7.1 PDCCH, PCFICH and PHICH interference model 2009

B.8 Burst transmission models for Frame structure type 3 2010

B.8.1 Burst transmission model for one LAA SCell 2010

B.8.2 Burst transmission model for multiple LAA SCell(s) 2010

Annex C (normative):  Downlink Physical Channels 2012

C.1 General 2012

C.2 Set-up 2012

C.3 Connection 2012

C.3.1 Measurement of Receiver Characteristics 2012

C.3.2 Measurement of Performance requirements 2013

C.3.3 Aggressor cell power allocation for Measurement of Performance Requirements when ABS is Configured 2014

C.3.4 Power Allocation for Measurement of Performance Requirements when Quasi Co-location Type B: same Cell ID 2015

C.3.5 Simplified CA testing method 2015

C.3.6 Measurement of Receiver Characteristics for Narrowband IoT 2016

Annex D (normative):  Characteristics of the interfering signal 2017

D.1 General 2017

D.2 Interference signals 2017

Annex E (normative):  Environmental conditions 2018

E.1  General 2018

E.2  Environmental 2018

E.2.1 Temperature 2018

E.2.2 Voltage 2018

E.2.3 Vibration 2019

Annex F (normative):  Transmit modulation 2020

F.1 Measurement Point 2020

F.2 Basic Error Vector Magnitude measurement 2020

F.3 Basic in-band emissions measurement 2021

F.4 Modified signal under test 2021

F.5 Window length 2023

F.5.1 Timing offset 2023

F.5.2 Window length 2023

F.5.3 Window length for normal CP 2023

F.5.4 Window length for Extended CP 2024

F.5.5 Window length for PRACH 2024

F.5.F Window length for category NB1 2025

F.6 Averaged EVM 2025

F.6.F Averaged EVM for category NB1 2026

F.7 Spectrum Flatness 2026

Annex G (informative):  Reference sensitivity level in lower SNR 2027

G.1 General 2027

G.2 Typical receiver sensitivity performance (QPSK) 2027

G.3 Reference measurement channel for REFSENSE in lower SNR 2033

Annex H (normative):  Modified MPR behavior 2036

H.1 Indication of modified MPR behavior 2036

Annex I (normative):  Supported Post Antenna Gain 2037

I.1 Declared Supported Post Antenna Gain for UE 2037

Annex J (informative):  Change history 2038
