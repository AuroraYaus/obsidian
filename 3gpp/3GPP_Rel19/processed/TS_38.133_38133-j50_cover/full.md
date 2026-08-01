| 3GPP TS 38.133 V19.5.0 (2026-06) |  |
| --- | --- |
| Technical Specification |  |
| 3rd Generation Partnership Project;Technical Specification Group Radio Access Network;NR;Requirements for support of radio resource management(Release 19) |  |
|  |  |
| ![](media/image1.emf) |  |
|  |  |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. |  |

|  |
| --- |
| 3GPPPostal address3GPP support office address650 Route des Lucioles - Sophia AntipolisValbonne - FRANCETel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16Internethttp://www.3gpp.org |
| Copyright NotificationNo part may be reproduced except as authorized by written permission. The copyright and the foregoing restriction extend to reproduction in all media.© 2026, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).All rights reserved.UMTS™ is a Trade Mark of ETSI registered for the benefit of its members3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersGSM® and the GSM logo are registered and owned by the GSM Association |

Contents

Foreword 189

1 Scope 191

2 References 191

3 Definitions, symbols and abbreviations 193

3.1 Definitions 193

3.2 Symbols 194

3.3 Abbreviations 195

3.4 Test tolerances 199

3.5 Frequency bands grouping 199

3.5.1 Introduction 199

3.5.2 NR operating bands in FR1 199

3.5.2A NR operating bands for satellite access in FR1 148

3.5.3 NR operating bands in FR2 148

3.6 Applicability of requirements in this specification version 149

3.6.1 RRC connected state requirements in DRX 149

3.6.2 Number of serving carriers 150

3.6.2.1 Number of serving carriers for SA 150

3.6.2.2 Number of serving carriers for EN-DC 150

3.6.2.3 Number of serving carriers for NE-DC 150

3.6.2.4 Number of serving carriers for NR-DC 150

3.6.3 Applicability for intra-band FR2 150

3.6.4 Applicability for FR2 UE power classes 150

3.6.5 Applicability for SDL bands 151

3.6.6 Applicability of requirements for NGEN-DC operation 151

3.6.7 Applicability of QCL 151

3.6.9 Applicability of requirements for scheduling availability 152

3.6.10 Applicability of requirements for measurement restrictions 152

3.6.11 Applicability of requirements for Redcap UEs 152

3.6.11.1 RRC connected state requirements in DRX 152

3.6.11.2 Applicability for FR2 Redcap UE power classes 152

3.6.11.3 Applicability of QCL 152

3.6.12 Applicability of requirements for Satellite Access 152

3.6.13 Applicability of requirements for FR2 152

3.6.14 Applicability of requirements for FR2 Power Class 6 153

3.6.15 Applicability of requirements for per-FR gap 153

3.6.16 Applicability of requirements for ATG 153

3.6.17 Applicability of requirements for MUSIM gaps 153

3.6.18 Applicability of requirements for a UE operating on a cell with less than 5 MHz BW 153

3.6.19 Applicability of requirements for multi-Rx operation in FR2-1 153

3.6.20 Applicability of requirements for RedCap UE with satellite access 153

3.6.21 Applicability of requirements for UE supporting L3 fast beam sweeping operation in FR2-1 154

3.6.22 Applicability of requirements for UE with LP-WUR 154

3.6.23 Applicability of requirements for SBFD 154

4 SA: RRC_IDLE state mobility 154

4.1 Cell Selection 154

4.2 Cell Re-selection 155

4.2.1 Introduction 155

4.2.2 Requirements 155

4.2.2.1 UE measurement capability 155

4.2.2.2 Measurement and evaluation of serving cell 155

4.2.2.3 Measurements of intra-frequency NR cells 157

4.2.2.4 Measurements of inter-frequency NR cells 161

4.2.2.5 Measurements of inter-RAT E-UTRAN cells 166

4.2.2.6 Maximum interruption in paging reception 168

4.2.2.7 General requirements 169

4.2.2.8 Minimum requirement at transitions 169

4.2.2.9 Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion 170

4.2.2.9.1 Introduction 170

4.2.2.9.2 Measurements for UE fulfilling low mobility criterion 170

4.2.2.9.3 Measurements for UE fulfilling not-at-cell edge criterion 172

4.2.2.9.4 Measurements for UE fulfilling low mobility and not-at-cell edge criteria 174

4.2.2.10 Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion 175

4.2.2.10.1 Introduction 175

4.2.2.10.2 Measurements for UE fulfilling low mobility criterion 175

4.2.2.10.3 Measurements for UE fulfilling not-at-cell edge criterion 177

4.2.2.10.4 Measurements for UE fulfilling low mobility and not-at-cell edge criterion 180

4.2.2.11 Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion 180

4.2.2.11.1 Introduction 180

4.2.2.11.2 Measurements for UE fulfilling low mobility criterion 181

4.2.2.11.3 Measurements for UE fulfilling with not-at-cell edge criterion 182

4.2.2.11.4 Measurements for UE fulfilling low mobility and not-at-cell edge criterion 184

4.2.2.12  Measurements of inter-frequency NR cells with NTN carrier 184

4.2A Cell Re-selection when subject to CCA 187

4.2A.1 Introduction 187

4.2A.2 Requirements 187

4.2A.2.1 UE measurement capability 187

4.2A.2.2 Measurement and evaluation when subject to CCA on the serving cell 188

4.2A.2.3 Measurements of intra-frequency NR cells when subject to CCA on the serving cell and target cell 189

4.2A.2.4 Measurements of inter-frequency NR cells when subject to CCA on the target cell 190

4.2A.2.5 Measurements of inter-RAT E-UTRAN cells when subject to CCA on the serving cell 192

4.2A.2.6 Maximum interruption in paging reception when subject to CCA on the target cell 192

4.2A.2.7 General requirements 192

4.2B Cell Re-selection for RedCap 193

4.2B.1 Introduction 193

4.2B.2 Requirements 193

4.2B.2.1 UE measurement capability for RedCap 193

4.2B.2.1.1 UE measurement capability for 1 Rx RedCap 193

4.2B.2.1.2 UE measurement capability for 2 Rx RedCap 193

4.2B.2.2 Measurement and evaluation of serving cell for RedCap UE 193

4.2B.2.3 Measurements of intra-frequency NR cells for RedCap UE 195

4.2B.2.4 Measurements of inter-frequency NR cells for RedCap UE 197

4.2B.2.5 Measurements of inter-RAT E-UTRAN cells for RedCap UE 200

4.2B.2.6 Maximum interruption in paging reception for RedCap 202

4.2B.2.7 General requirements for RedCap 202

4.2B.2.8 Minimum requirement at transitions 202

4.2B.2.9 Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion for RedCap 203

4.2B.2.9.1 Introduction 203

4.2B.2.9.2 Measurements for UE fulfilling stationary criterion 203

4.2B.2.9.3 Measurements for a UE fulfilling not-at-cell edge while stationary criterion 206

4.2B.2.9.3A Measurements for a UE fulfilling stationary and not-at-cell-edge criteria 206

4.2B.2.9.4 Measurements for a UE fulfilling low mobility and stationary criteria 207

4.2B.2.9.5 Measurements for a UE fulfilling low mobility and not-at-cell-edge while stationary criteria 207

4.2B.2.9.6 Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge while stationary criteria 207

4.2B.2.9.7 Measurements for a UE fulfilling low mobility and not-at-cell edge criteria and not-at-cell-edge while stationary criteria 207

4.2B.2.9.8 Measurements for a UE fulfilling low mobility, not-at-cell edge and stationary criterion 207

4.2B.2.9.9 Measurements for UE fulfilling low mobility criterion 208

4.2B.2.9.10 Measurements for UE fulfilling not-at-cell edge criterion 210

4.2B.2.9.11 Measurements for UE fulfilling low mobility and not-at-cell edge criteria 212

4.2B.2.10 Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion 213

4.2B.2.10.1 Introduction 213

4.2B.2.10.2 Measurements for UE fulfilling stationary criterion 213

4.2B.2.10.3 Measurements for a UE fulfilling not-at-cell edge while stationary  criterion 215

4.2B.2.10.3A Measurements for a UE fulfilling stationary and not-at-cell-edge criterion 216

4.2B.2.10.4 Measurements for a UE fulfilling low mobility and stationary criteria 216

4.2B.2.10.5 Measurements for a UE fulfilling low mobility and not-at-cell-edge while stationary criteria 216

4.2B.2.10.6 Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge while stationary criteria 217

4.2B.2.10.7 Measurements for a UE fulfilling low mobility and not-at-cell edge criteria and not-at-cell-edge while stationary criteria 217

4.2B.2.10.8 Measurements for a UE fulfilling low mobility, not-at-cell edge and stationary  criteria 217

4.2B.2.10.9 Measurements for UE fulfilling low mobility criterion 217

4.2B.2.10.10 Measurements for UE fulfilling not-at-cell edge criterion 220

4.2B.2.10.11 Measurements for UE fulfilling low mobility and not-at-cell edge criterion 222

4.2B.2.11 Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion 222

4.2B.2.11.1 Introduction 222

4.2B.2.11.2 Measurements for UE fulfilling stationary criterion 223

4.2B.2.11.3 Measurements for a UE fulfilling not-at-cell edge while stationary criterion 224

4.2B.2.11.3A Measurements for a UE fulfilling stationary and not-at-cell-edge criterion 224

4.2B.2.11.4 Measurements for a UE fulfilling low mobility and stationary criteria 225

4.2B.2.11.5 Measurements for a UE fulfilling low mobility and not-at-cell-edge while stationary  criteria 225

4.2B.2.11.6 Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge while stationary criteria 225

4.2B.2.11.7 Measurements for a UE fulfilling low mobility and not-at-cell edge criteria and not-at-cell-edge while stationary criteria 225

4.2B.2.11.8 Measurements for a UE fulfilling low mobility, not-at-cell edge and stationary  criteria 226

4.2B.2.11.9 Measurements for UE fulfilling low mobility criterion 226

4.2B.2.11.10 Measurements for UE fulfilling with not-at-cell edge criterion 227

4.2B.2.11.11 Measurements for UE fulfilling low mobility and not-at-cell edge criterion 228

4.2C Cell Re-selection for NR UE for Satellite Access 229

4.2C.1 Introduction 229

4.2C.2 Requirements 229

4.2C.2.1 UE measurement capability 229

4.2C.2.2 Measurement and evaluation of serving cell 229

4.2C.2.3 Measurements of intra-frequency NR cells 231

4.2C.2.4 Measurements of inter-frequency NR cells 233

4.2C.2.5 Maximum interruption in paging reception 237

4.2C.2.6 Minimum requirement at transitions 238

4.2C.2.7 Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion 238

4.2C.2.8 Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion 238

4.2C.2.9 General requirements 238

4.2C.2.10 Measurements of inter-frequency NR cells with TN carrier 238

4.2C.2.11 Measurements of inter-RAT E-UTRAN cells with TN carrier 241

4.2C.3 Void 243

4.2C.4 Void 243

4.2D Cell Re-selection for ATG 243

4.2D.1 Introduction 243

4.2D.2 Requirements 243

4.2D.2.1 UE measurement capability 243

4.2D.2.2 Measurement and evaluation of serving cell 243

4.2D.2.3 Measurements of intra-frequency NR cells 244

4.2D.2.4 Measurements of inter-frequency NR cells 245

4.2D.2.5 Maximum interruption in paging reception 247

4.2D.2.6 General requirements 247

4.2E Cell Re-selection for NR RedCap UE with Satellite Access 247

4.2E.1 Introduction 247

4.2E.2 Requirements for RedCap UE with Satellite Access 248

4.2E.2.1 UE measurement capability for RedCap with Satellite Access 248

4.2E.2.1.1 UE measurement capability for 1Rx RedCap UEs 248

4.2E.2.1.2 UE measurement capability for 2Rx RedCap UEs 248

4.2E.2.2 Measurement and evaluation of serving cell for RedCap UEs 248

4.2E.2.3 Measurements of intra-frequency NR cells for RedCap UE 250

4.2E.2.4 Measurements of inter-frequency NR cells for RedCap UE 252

4.2E.2.5 Maximum interruption in paging reception 255

4.2E.2.6 Minimum requirement at transitions for RedCap UE 255

4.2E.2.7 Measurements of intra-frequency NR cells for RedCap UE configured with relaxed measurement criterion 255

4.2E.2.7.1 Introduction 255

4.2E.2.7.2 Measurements for UE fulfilling low mobility criterion 256

4.2E.2.7.3 Measurements for UE fulfilling not-at-cell edge criterion 256

4.2E.2.7.4 Measurements for UE fulfilling low mobility and not-at-cell edge criteria 256

4.2E.2.8 Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion 257

4.2E.2.8.1 Introduction 257

4.2E.2.8.2 Measurements for UE fulfilling low mobility criterion 257

4.2E.2.8.3 Measurements for UE fulfilling not-at-cell edge criterion 257

4.2E.2.8.4 Measurements for UE fulfilling low mobility and not-at-cell edge criterion 258

4.2E.2.9 General requirements 258

4.2E.2.10 Measurements of inter-frequency NR cells with TN carrier 258

4.2E.2.11 Measurements of inter-RAT E-UTRAN cells with TN carrier 262

4.3 Minimization of Drive Tests (MDT) 263

4.3.1 Introduction 263

4.3.2 Measurement Requirements 263

4.3.3 Requirements for Relative Time Stamp Accuracy 264

4.3.4 Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting 264

4.3.5 Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting 264

4.3C Minimization of Drive Tests (MDT) for Satellite Access 264

4.3C.1 Introduction 264

4.3C.2 Measurement Requirements 265

4.3C.3 Requirements for Relative Time Stamp Accuracy 265

4.3C.4 Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting 265

4.3C.5 Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting 266

4.3D Minimization of Drive Tests (MDT) for NR RedCap UE with Satellite Access 266

4.3D.1 Introduction 266

4.3D.2 Measurement Requirements 266

4.3D.3 Requirements for Relative Time Stamp Accuracy 266

4.3D.4 Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting 266

4.3D.5 Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting 266

4.4 Idle Mode CA/DC Measurements 267

4.4.1 Introduction 267

4.4.2 Measurement Requirements 267

4.4.2.1 Detected cell requirement during state transition and Idle mode 267

4.4.2.2 Measurements of inter-frequency CA/DC candidate cells 267

4.4.2.3 Measurements on serving cell 268

4.4.2.4 Measurements of E-UTRAN inter-RAT DC candidate cells 269

4.5 NR measurements for positioning 269

4.5.1 Introduction 269

4.5.2 RSTD measurements 270

4.5.2.1 Introduction 270

4.5.2.2 Requirements Applicability 270

4.5.2.3 Measurement Capability 270

4.5.2.4 Measurement Reporting Requirements 270

4.5.2.5 Measurements Period Requirements 270

4.5.2.6 Measurements Period Requirements with Bandwidth Aggregation 273

4.5.3 PRS-RSRP measurements 277

4.5.3.1 Introduction 277

4.5.3.2 Requirements applicability 277

4.5.3.3 Measurement Capability 277

4.5.3.4 Measurement Reporting Requirements 277

4.5.3.5 Measurement Period Requirements 278

4.5.4 PRS-RSRPP measurements 280

4.5.4.1 Introduction 280

4.5.4.2 Requirements Applicability 280

4.5.4.3 Measurement Capability 280

4.5.4.4 Measurement Reporting Requirements 280

4.5.4.5 Measurement Period Requirements 281

4.5.5 Measurement requirements for DL RSCPD reported with RSTD 281

4.5.5.1 Introduction 281

4.5.5.2 Requirements Applicability 281

4.5.5.3 Measurement Capability 281

4.5.5.4 Measurement Reporting Requirements 281

4.5.5.5 Measurements Period Requirements 282

4.5A Reporting Delay Requirements for DL AI/ML Positioning 286

4.5A.1 Introduction 286

4.5A.2 Measurements Period Requirements 286

4.5A.3 Measurements Period Requirements with Bandwidth Aggregation 289

4.6 NR measurements for positioning for RedCap 292

4.6.1 Introduction 292

4.6.2 RSTD measurements for RedCap 293

4.6.2.1 Introduction 293

4.6.2.2 Requirements Applicability 293

4.6.2.3 Measurement Capability 293

4.6.2.4 Measurement Reporting Requirements 293

4.6.2.5 Measurements Period Requirements without RX FH 293

4.6.2.6 Measurement Period Requirements with RX FH 294

4.6.3 PRS-RSRP measurements for RedCap 296

4.6.3.1 Introduction 296

4.6.3.2 Requirements applicability 296

4.6.3.3 Measurement Capability 296

4.6.3.4 Measurement Reporting Requirements 296

4.6.3.5 Measurement Period Requirements without RX FH 297

4.6.3.6 Measurement Period Requirements with RX FH 299

4.6.4 PRS-RSRPP measurements for RedCap 301

4.6.4.1 Introduction 301

4.6.4.2 Requirements Applicability 301

4.6.4.3 Measurement Capability 301

4.6.4.4 Measurement Reporting Requirements 301

4.6.4.5 Measurement Period Requirements without RX FH 302

4.6.4.6 Measurement Period Requirements with RX FH 302

4.7 Measurement report for fast CA/DC setup 302

4.7.1 Introduction 302

4.7.2 Void 302

4.7.3 Measurement Report Requirements 302

4.8 IDLE mode measurement for LP-WUS operation 303

4.8.1 Introduction 303

4.8.2 Requirements 303

4.8.2.1 UE Measurement Capability 303

4.8.2.1.1 LP-WUR measurement capability 303

4.8.2.1.2 MR measurement capability with LP-WUR 303

4.8.2.2 LP-WUR Serving cell measurement and evaluation requirement 303

4.8.2.2.1 General description 303

4.8.2.2.2 LP-WUR measurement and evaluation requirements for PSS/SSS 304

4.8.2.2.3 LP-WUR measurement and evaluation requirements for LP-SS 305

4.8.2.3 Measurement and evaluation of serving cell by MR 305

4.8.2.3.1 Requirements for evaluation of cell selection criterion 305

4.8.2.3.2 Requirements for evaluation of LP-WUS related conditions 306

4.8.2.3A Measurement and evaluation of serving cell by RedCap UE 306

4.8.2.3A.1 Requirements for evaluation of cell selection criterion for RedCap UE 306

4.8.2.3A.2 Requirements for evaluation of LP-WUS related conditions for RedCap UE 306

4.8.2.4 Measurements of intra-frequency NR cells for UE with LP-WUR 307

4.8.2.4A Measurements of intra-frequency NR cells for RedCap UE with LP-WUR 307

4.8.2.5 Measurements of inter-frequency NR cells for UE with LP-WUR 308

4.8.2.5.1 Introduction 308

4.8.2.5.2 Measurements for UE with LP-WUR fulfilling relaxed measurement criterion 308

4.8.2.5.3 Measurements for UE with LP-WUR fulfilling serving cell measurement offloading criterion 309

4.8.2.5A Measurements of inter-frequency NR cells for Redcap with LP-WUR 309

4.8.2.5A.1 Introduction 309

4.8.2.5A.2 Measurements for UE with LP-WUR fulfilling relaxed measurement criterion 309

4.8.2.5A.3 Measurements for UE with LP-WUR fulfilling serving cell measurement offloading criterion 310

4.8.2.6     Measurements of inter-RAT E-UTRAN cells for UE with LP-WUR 310

4.8.2.6.1 Introduction 310

4.8.2.6.2 Measurements for UE fulfilling relaxed measurement criteria 310

4.8.2.6.3 Measurements for UE fulfilling serving cell measurement offloading entry criteria 311

4.8.2.6A Measurements of inter-RAT E-UTRAN cells for RedCap with LP-WUR 311

4.8.2.6A.1 Introduction 311

4.8.2.6A.2 Measurements for UE fulfilling relaxed measurement criteria 311

4.8.2.6A.3 Measurements for UE fulfilling serving cell measurement offloading entry criteria 312

5 SA: RRC_INACTIVE state mobility 312

5.1 Cell Re-selection 312

5.1.1 Introduction 312

5.1.2 Requirements 312

5.1.2.1 UE measurement capability 312

5.1.2.2 Measurement and evaluation of serving cell 312

5.1.2.3 Measurements of intra-frequency NR cells 314

5.1.2.4 Measurements of inter-frequency NR cells 316

5.1.2.5 Measurements of inter-RAT E-UTRAN cells 318

5.1.2.6 Maximum interruption in paging reception 319

5.1.2.7 General requirements 319

5.1.2.8 Measurement of inter-frequency NR cells with NTN carrier 320

5.1.2.9 Minimum requirement at transitions 320

5.1.2.10 Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion 320

5.1.2.11 Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion 321

5.1.2.12 Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion 322

5.1A Cell Re-selection with CCA 322

5.1A.1 Introduction 322

5.1A.2 Requirements 323

5.1A.2.1 UE measurement capability 323

5.1A.2.2 Measurement and evaluation when CCA is used on the serving cell 323

5.1A.2.3 Measurements of intra-frequency NR cells when CCA is used on the serving cell and target cell 323

5.1A.2.4 Measurements of inter-frequency NR cells when CCA is used on the target cell 323

5.1A.2.5 Measurements of inter-RAT E-UTRAN cells when CCA is used on the serving cell 323

5.1A.2.6 Maximum interruption in paging reception when CCA is used on the target cell 323

5.1A.2.7 General requirements 323

5.1B Cell Re-selection for RedCap 323

5.1B.1 Introduction 323

5.1B.2 Requirements 323

5.1B.2.1 UE measurement capability 323

5.1B.2.2 Measurement and evaluation of serving cell 323

5.1B.2.3 Measurements of intra-frequency NR cells 326

5.1B.2.4 Measurements of inter-frequency NR cells 328

5.1B.2.5 Measurements of inter-RAT E-UTRAN cells 330

5.1B.2.6 Maximum interruption in paging reception 331

5.1B.2.7 General requirements 331

5.1B.2.8 Minimum requirement at transitions 331

5.1B.2.9 Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion 331

5.1B.2.10 Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion 333

5.1B.2.11 Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion 336

5.1C Cell Re-selection for Satellite Access 337

5.1C.1 Introduction 337

5.1C.2 Requirements 337

5.1C.2.1 UE measurement capability 337

5.1C.2.2 Measurement and evaluation of serving cell 337

5.1C.2.3 Measurements of intra-frequency NR cells 337

5.1C.2.4 Measurements of inter-frequency NR cells 338

5.1C.2.5 Maximum interruption in paging reception 338

5.1C.2.6 General requirements 338

5.1C.2.7 Measurements of inter-frequency NR cells with TN carrier 338

5.1C.2.8 Measurements of inter-RAT E-UTRAN cells with TN carrier 338

5.1C.3 Void 338

5.1C.4 Void 338

5.1D Cell Re-selection for ATG 338

5.1D.1 Introduction 338

5.1D.2 Requirements 338

5.1D.2.1 UE measurement capability 338

5.1D.2.2 Measurement and evaluation of serving cell 338

5.1D.2.3 Measurements of intra-frequency NR cells 338

5.1D.2.4 Measurements of inter-frequency NR cells 338

5.1D.2.5 Maximum interruption in paging reception 339

5.1D.2.6 General requirements 339

5.1E Cell Re-selection for RedCap UE with Satellite Access 339

5.1E.1 Introduction 339

5.1E.2 Requirements 339

5.1E.2.1 UE measurement capability 339

5.1E.2.2 Measurement and evaluation of serving cell 339

5.1E.2.3 Measurements of intra-frequency NR cells 340

5.1E.2.4 Measurements of inter-frequency NR cells 341

5.1E.2.5 Maximum interruption in paging reception 341

5.1E.2.6 General requirements 341

5.1E.2.7 Minimum requirement at transitions 341

5.1E.2.8 Measurements of inter-frequency NR cells with TN carrier 341

5.1E.2.9 Measurements of inter-RAT E-UTRAN cells with TN carrier 342

5.2 Void 342

5.2B Configured Grant based Small Data Transmissions (CG-SDT) for RedCap 342

5.2B.1 Introduction 342

5.2B.2 Requirements on UE synchronization for small data transmissions for RedCap 342

5.2B.2.1 Void 342

5.2B.3 TA validation requirements for RedCap 342

5.2B.3.1 Void 343

5.2B.3.2 Void 343

5.2B.4 Scheduling restriction 343

5.2B.5 Applicability conditions for CG-SDT for RedCap 343

5.3 Minimization of Drive Tests (MDT) 344

5.3.1 Introduction 344

5.3.2 Measurement Requirements 344

5.3.3 Requirements for Relative Time Stamp Accuracy 344

5.3.4 Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting 344

5.3.5 Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting 344

5.3.6 Requirements for Relative Time Stamp Accuracy for RRC Resume Failure Log Reporting 344

5.3C Minimization of Drive Tests (MDT) for Satellite Access 345

5.3C.1 Introduction 345

5.3C.2 Measurement Requirements 345

5.3C.3 Requirements for Relative Time Stamp Accuracy 345

5.3C.4 Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting 345

5.3C.5 Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting 345

5.3C.6 Requirements for Relative Time Stamp Accuracy for RRC Resume Failure Log Reporting 345

5.3D Minimization of Drive Tests (MDT) for NR RedCap UE with Satellite Access 346

5.3D.1 Introduction 346

5.3D.2 Measurement Requirements 346

5.3D.3 Requirements for Relative Time Stamp Accuracy 346

5.3D.4 Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting 346

5.3D.5 Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting 346

5.3D.6 Requirements for Relative Time Stamp Accuracy for RRC Resume Failure Log Reporting 346

5.4 Inactive Mode CA/DC Measurements 347

5.4.1 Introduction 347

5.4.2 Measurement Requirements 347

5.4.2.1 Detected cell requirement during state transition and inactive mode 347

5.4.2.2 Measurements of inter-frequency CA/DC candidate cells 347

5.4.2.3 Measurements on serving cell 347

5.4.2.4 Measurements on E-UTRAN inter-RAT DC candidate cells 347

5.5 Configured Grant based Small Data Transmissions (CG-SDT) 347

5.5.1 Introduction 347

5.5.2 Requirements on UE synchronization for small data transmissions 347

5.5.3 TA validation requirements 347

5.5.4 Scheduling restriction 349

5.5.4.1 Scheduling availability of UE performing measurements in TDD bands on FR1 349

5.5.4.2 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1 349

5.5.4.3 Scheduling availability of UE performing measurements on FR2 349

5.5.5 Applicability conditions for SDT 350

The UE is allowed to delay the reception of PRS resources on the positioning frequency layer until the SDT session is completed if the measurement using PRS resource overlaps with the SDT resources. 350

5.5D Configured Grant based Small Data Transmissions (CG-SDT) for ATG 350

5.5D.1 Scheduling availability of UE performing measurements on FR1 350

5.5E Configured Grant based Small Data Transmissions (CG-SDT) for RedCap UEs with NTN 351

5.5E.1 Introduction 351

5.5E.2 Requirements on UE synchronization for small data transmissions 351

5.5E.3 TA validation requirements 351

5.5E.4 Scheduling restriction 351

5.5E.5 Applicability conditions for SDT 351

5.6 NR measurements for positioning 352

5.6.1 Introduction 352

5.6.1A Cell re-selection for positioning 352

5.6.1A.1 Measurement and evaluation of serving cell 353

5.6.1A.2 Measurements of intra-frequency NR cells 354

5.6.2 RSTD measurements 355

5.6.2.1 Introduction 355

5.6.2.2 Requirements Applicability 355

5.6.2.3 Measurement Capability 355

5.6.2.5 Measurements Period Requirements 355

5.6.2.6 Measurements Period Requirements with Bandwidth Aggregation 358

5.6.3 PRS-RSRP measurements 362

5.6.3.1 Introduction 362

5.6.3.2 Requirements applicability 362

5.6.3.3 Measurement Capability 362

5.6.3.4 Measurement Reporting Requirements 362

5.6.3.5 Measurement Period Requirements 363

5.6.4 UE Rx-Tx time difference measurements 365

5.6.4.1 Introduction 365

5.6.4.2 Requirements Applicability 365

5.6.4.3 Measurement Capability 365

5.6.4.4 Measurement Reporting Requirements 365

5.6.4.5 Measurement Period Requirements 366

5.6.4.6 Measurement Period Requirements with Bandwidth Aggregation 369

5.6.5 PRS-RSRPP measurements 373

5.6.5.1 Introduction 373

5.6.5.2 Requirements Applicability 373

5.6.5.3 Measurement Capability 373

5.6.5.4 Measurement Reporting Requirements 373

5.6.5.5 Measurement Period Requirements 373

5.6.6 TA validation requirements for positioning 373

5.6.6.1 Introduction 373

5.6.6.2 TA validation requirements 374

5.6.6.3 TA validation requirements when configured with validity area 374

5.6.7 Measurement requirements for DL RSCPD reported with RSTD 375

5.6.7.1 Introduction 375

5.6.7.2 Requirements Applicability 375

5.6.7.3 Measurement Capability 376

5.6.7.4 Measurement Reporting Requirements 376

5.6.7.5 Measurements Period Requirements 376

5.6.8 Measurement requirements for DL RSCP reported with UE Rx-Tx time difference 378

5.6.8.1 Introduction 378

5.6.8.2 Requirements Applicability 378

5.6.8.3 Measurement Capability 379

5.6.8.4 Measurement Reporting Requirements 379

5.6.8.5 Measurement Period Requirements 379

5.6A NR measurements for positioning for RedCap 382

5.6A.1 Introduction 382

5.6A.2 Cell re-selection for positioning 382

5.6A.2.1 Measurement and evaluation of serving cell 383

5.6A.2.2 Measurements of intra-frequency NR cells 383

5.6A.3 TA validation requirements for positioning SRS 384

5.6A.3.1 Introduction 384

5.6A.3.2 TA validation requirements 384

5.6A.3.3 TA validation requirements when configured with validity area 384

5.6A.4 RSTD measurements for RedCap 385

5.6A.4.1  Introduction 385

5.6A.4.2 Requirements applicability 385

5.6A.4.3 Measurement Capability 385

5.6A.4.4 Measurement Reporting Requirements 385

5.6A.4.5 Measurement Period Requirement without RX FH 386

5.6A.4.6 Measurement Period Requirement with RX FH 389

5.6A.5 PRS-RSRP measurements for RedCap 391

5.6A.5.1 Introduction 391

5.6A.5.2 Requirements applicability 391

5.6A.5.3 Measurement Capability 391

5.6A.5.4 Measurement Reporting Requirements 391

5.6A.5.5 Measurement Period Requirements without RX FH 392

5.6A.5.6 Measurement Period Requirement with RX FH 395

5.6A.6 UE Rx-Tx time difference measurements for RedCap 396

5.6A.6.1 Introduction 396

5.6A.6.2 Requirements Applicability 397

5.6A.6.3 Measurement Capability 397

5.6A.6.4 Measurement Reporting Requirements 397

5.6A.6.5 Measurement Period Requirements without RX FH 398

5.6A.6.6 Measurement Period Requirements with RX FH 398

5.6A.7 PRS-RSRPP measurements for RedCap 400

5.6A.7.1  Introduction 400

5.6A.7.2 Requirements applicability 400

5.6A.7.3 Measurement Capability 401

5.6A.7.4 Measurement Reporting Requirements 401

5.6A.7.5 Measurement Period Requirements without FH 401

5.6A.7.6 Measurement period requirement with FH 401

5.6B Reporting Delay Requirements for DL AI/ML Positioning 401

5.6B.1 Introduction 401

5.6B.2 Measurements Period Requirements 402

5.6B.3  Measurements Period Requirements with Bandwidth Aggregation 405

5.7 Random access based Small Data Transmissions (RA-SDT) 408

5.7.1 Introduction 408

5.7.2 Requirements for small data transmissions based on 2-step RA 408

5.7.3 Requirements for small data transmissions based on 4-step RA 408

5.7.4 Applicability conditions for SDT 408

5.7B Random access based Small Data Transmissions (RA-SDT) for RedCap 408

5.7B.1 Introduction 408

5.7B.2 Requirements for small data transmissions based on 2-step RA 408

5.7B.3 Requirements for small data transmissions based on 4-step RA 409

5.7B.4 Applicability conditions for RA-SDT for RedCap 409

5.7D Random access based Small Data Transmissions (RA-SDT) for ATG 409

5.7E Random access based Small Data Transmissions (RA-SDT) for RedCap UEs with NTN 409

5.7E.1 Introduction 409

5.7E.2 Requirements for small data transmissions based on 2-step RA 409

5.7E.3 Requirements for small data transmissions based on 4-step RA 409

5.7E.4 Applicability conditions for RA-SDT 409

5.8 Measurement report for fast CA/DC setup 409

5.8.1 Introduction 409

5.8.2 Void 410

5.8.3 Measurement Report Requirements 410

5.9 INACTIVE mode measurement for LP-WUS operation 410

5.9.1 Introduction 410

5.9.2 Requirements 410

5.9.2.1 UE measurement capability 410

5.9.2.1.1 LP-WUR measurement capability 410

5.9.2.1.2 MR measurement capability with LP-WUR 410

5.9.2.2 LP-WUR serving cell measurement and evaluation requirements 410

5.9.2.3 Measurement and evaluation of serving cell by MR 410

5.9.2.3A  Measurement and evaluation of serving cell by Redcap 410

5.9.2.4 Measurements of intra-frequency NR cells for UE with LP-WUR 411

5.9.2.4A Measurements of intra-frequency NR cells for RedCap UE with LP-WUR 411

5.9.2.5 Measurements of inter-frequency NR cells for UE with LP-WUR 411

5.9.2.5A Measurements of inter-frequency NR cells for Redcap with LP-WUR 411

5.9.2.6 Measurements of inter-RAT E-UTRAN cells for UE with LP-WUR 411

5.9.2.6A Measurements of inter-RAT E-UTRAN cells for Redcap with LP-WUR 411

6 RRC_CONNECTED state mobility 411

6.1 Handover 411

6.1.1 NR Handover 411

6.1.1.1 Introduction 411

6.1.1.2 NR FR1 - NR FR1 Handover 411

6.1.1.2.1 Handover delay 412

6.1.1.2.2 Interruption time 412

6.1.1.3 NR FR2- NR FR1 Handover 413

6.1.1.3.1 Handover delay 413

6.1.1.3.2 Interruption time 413

6.1.1.4 NR FR2- NR FR2 Handover 414

6.1.1.4.1 Handover delay 414

6.1.1.4.2 Interruption time 414

6.1.1.5 NR FR1- NR FR2 Handover 415

6.1.1.5.1 Handover delay 416

6.1.1.5.2 Interruption time 416

6.1.2 NR Handover to other RATs 417

6.1.2.1 NR – E-UTRAN Handover 417

6.1.2.1.1 Introduction 417

6.1.2.1.2 Handover delay 417

6.1.2.1.3 Interruption time 417

6.1.2.2 NR – UTRAN Handover 418

6.1.2.2.1 Introduction 418

6.1.2.2.2 Handover delay 418

6.1.2.2.3 Interruption time 418

6.1.3 NR DAPS Handover 419

6.1.3.1 Introduction 419

6.1.3.2 NR FR1 - NR FR1 DAPS Handover 419

6.1.3.2.1 DAPS handover delay 419

6.1.3.2.2 Interruption time 420

6.1.3.3 NR FR2- NR FR1 DAPS Handover 421

6.1.3.3.1 DAPS handover delay 422

6.1.3.3.2 Interruption time 422

6.1.3.4 NR FR1- NR FR2 DAPS Handover 422

6.1.3.4.1 DAPS handover delay 423

6.1.3.4.2 Interruption time 423

6.1.4 NR Conditional Handover 424

6.1.4.1 Introduction 424

6.1.4.2 NR FR1 – NR FR1 conditional handover 424

6.1.4.2.2 Measurement time 424

6.1.4.3 NR FR2 – NR FR1 conditional handover 426

6.1.4.4 NR FR2 – NR FR2 conditional handover 426

6.1.4.4.1 Handover delay 426

6.1.4.4.2 Measurement time 427

6.1.4.4.3 Preparation time 428

6.1.4.4.4 Interruption time 428

6.1.4.5 NR FR1 – NR FR2 conditional handover 428

6.1.5 NR Handover with PSCell 428

6.1.5.1 Introduction 428

6.1.5.2 Handover with PSCell from NR SA to EN-DC 429

6.1.5.2.1 Interruption time for inter-RAT HO from NR to E-UTRAN 429

6.1.5.2.2 PSCell addition in HO with PSCell for NR SA to EN-DC 429

6.1.5.3 HO with PSCell from NE-DC to NE-DC 430

6.1.5.3.1 Handover delay 430

6.1.5.3.2 HO with PSCell - PCell Interruption time 430

6.1.5.3.3 PSCell addition/change in NE-DC to NE-DC HO with PSCell 430

6.1.5.4 HO with PSCell from NR-DC to NR-DC 431

6.1.5.5 Handover with PSCell from NR SA to EN-DC with PSCell using CCA 432

6.1.5.5.1 Introduction 432

6.1.5.5.2 NR SA to EN-DC HO with PSCell- NR to E-UTRA HO Interruption time 432

6.1.5.5.3 NR SA to EN-DC HO with PSCell - NR PSCell Addition Delay requirements 433

6.1.6 NR Conditional Handover including target MCG and target SCG 434

6.1.6.1 Conditional handover including target MCG in FR1 and target SCG in FR1 in NR-DC 434

6.1.6.1.1 CHO with PSCell – PCell Interruption time 434

6.1.6.1.2 CHO with PSCell – PSCell change delay 435

6.1.6.2 Conditional handover including target MCG in FR1 and target SCG in FR2 in NR-DC 435

6.1.6.2.2 CHO with PSCell – PSCell change delay 436

6.1.7 NR Conditional Handover including target MCG and candidate SCG 437

6.1.7.1 Conditional handover including target MCG and candidate SCG for CPC in FR1 NR-DC 437

6.1.7.1.1 PCell conditional handover delay 438

6.1.7.1.2 PSCell conditional change delay 439

6.1.7.2 Conditional handover including target MCG in FR1 and Candidate SCG for CPC in FR2 in NR-DC 440

6.1.7.2.1 PCell handover delay 440

6.1.7.2.2 PSCell conditional change delay 441

6.1A Void 443

6.1A.1 Void 443

6.1A.1.1 Void 443

6.1A.1.2 Void 443

6.1A.1.2.1 Void 443

6.1A.1.2.2 Void 443

6.1B Handover to target cell using CCA 443

6.1B.1 NR Handover 443

6.1B.1.1 Introduction 443

6.1B.1.2 NR FR1 - NR FR1 Handover 443

6.1B.1.2.1 Handover delay 443

6.1B.1.2.2 Interruption time 443

6.1B.1.3 NR FR2-2 NR FR2-2 Handover 444

6.1B.1.3.1 Handover delay 444

6.1B.1.3.2 Interruption time 444

6.1B.1.4 NR FR1- NR FR2-2 Handover 445

6.1B.1.4.1 Handover delay 445

6.1B.1.4.2 Interruption time 446

6.1C Handover for SAN 447

6.1C.1 NR SAN Handover 447

6.1C.1.1 Introduction 447

6.1C.1.2 NR SAN FR1 – NR SAN FR1 Handover 447

6.1C.1.2.1 Handover delay 447

6.1C.1.2.2 Interruption time 447

6.1C.1.3 NR SAN FR2-NTN – NR SAN FR2-NTN Handover 448

6.1C.1.3.1 Handover delay 448

6.1C.1.3.2 Interruption time 449

6.1C.2 NR SAN Conditional Handover 449

6.1C.2.1 Introduction 449

6.1C.2.2 NR SAN FR1 – NR SAN FR1 conditional handover 450

6.1C.2.2.1 Handover delay 450

6.1C.2.2.2 Measurement time 450

6.1C.2.2.3 Preparation time 452

6.1C.2.2.4 Interruption time 452

6.1C.2.3 NR SAN FR1 – NR SAN FR1 conditional handover without L3 measurement criteria 452

6.1C.2.3.1 Handover delay 452

6.1C.2.3.2 Preparation time 453

6.1C.2.3.3 Interruption time 453

6.1C.2.4 NR SAN FR2-NTN – NR SAN FR2-NTN conditional handover 454

6.1C.3 NR SAN Satellite switching with re-synchronization 454

6.1C.3.1 Introduction 454

6.1C.3.2 NR SAN FR1 – NR SAN FR1 Satellite switching with re-synchronization 454

6.1C.3.2.1 Satellite switching delay 454

6.1C.3.2.2 Interruption time for hard satellite switch with re-sync 454

6.1C.3.3 NR SAN FR2 – NR SAN FR2 Satellite switching with re-synchronization 456

6.1C.3.3.1 Satellite switching delay 456

6.1C.3.3.2 Interruption time for hard satellite switch with re-sync 456

6.1C.3.3.3 Satellite switch delay for soft satellite switch with re-sync 457

6.1D Handover for RedCap 457

6.1D.1 NR Handover 457

6.1D.1.1 Introduction 457

6.1D.1.2 NR FR1 - NR FR1 Handover 458

6.1D.1.2.1 Handover delay 458

6.1D.1.2.2 Interruption time 458

6.1D.1.3 NR FR2- NR FR2 Handover 459

6.1D.1.3.1 Handover delay 459

6.1D.1.3.2 Interruption time 459

6.1D.2 NR Handover to other RATs 461

6.1D.2.1 NR – E-UTRAN Handover 461

6.1E Handover for ATG 461

6.1E.1 NR Handover 461

6.1E.1.1 Introduction 461

6.1E.1.2 NR FR1 - NR FR1 Handover 461

6.1E.1.2.1 Handover delay 461

6.1E.1.2.2 Interruption time 461

6.1E.2 NR Conditional Handover 462

6.1E.2.1 Introduction 462

6.1E.2.2 NR FR1 – NR FR1 conditional handover 462

6.1E.2.2.1 Handover delay 462

6.1E.2.2.2 Measurement time 463

6.1E.2.2.3 Preparation time 463

6.1E.2.2.4 Interruption time 463

6.1F Handover for RedCap UE with satellite access 464

6.1F.1 NR SAN Handover 464

6.1F.1.1 Introduction 464

6.1F.1.2 NR SAN FR1 – NR SAN FR1 Handover 464

6.1F.1.2.1 Handover delay 464

6.1F.1.2.2 Interruption time 464

6.1F.2 NR SAN Conditional Handover 464

6.1F.2.1 Introduction 464

6.1F.2.2 NR SAN FR1 – NR SAN FR1 conditional handover 465

6.1F.2.2.1 Handover delay 465

6.1F.2.2.2 Measurement time 465

6.1F.2.2.3 Preparation time 465

6.1F.2.2.4 Interruption time 465

6.1F.2.3 NR SAN FR1 – NR SAN FR1 conditional handover without L3 measurement criteria 465

6.1F.2.3.1 Handover delay 465

6.1F.2.3.2 Preparation time 465

6.1F.2.3.3 Interruption time 465

6.1F.3 NR SAN Satellite switching with re-synchronization 466

6.1F.3.1 Introduction 466

6.1F.3.2 NR SAN FR1 – NR SAN FR1 Satellite switching with re-synchronization 466

6.1F.3.2.1 Satellite switching delay 466

6.1F.3.2.2 Interruption time for hard satellite switch with re-sync 466

6.1F.3.2.3 Satellite switch delay for soft satellite switch with re-sync 466

6.2 RRC Connection Mobility Control 467

6.2.1 SA: RRC Re-establishment 467

6.2.1.1 Introduction 467

6.2.1.2 Requirements 467

6.2.1.2.1 UE Re-establishment delay requirement 467

6.2.1A RRC Re-establishment with CCA 469

6.2.1A.1 Introduction 469

6.2.1A.2 Requirements 470

6.2.1A.2.1 UE Re-establishment with CCA delay requirement 470

6.2.1B SA: RRC Re-establishment for RedCap 471

6.2.1B.1 Introduction 471

6.2.1B.2 Requirements 472

6.2.2 Random access 472

6.2.2.1 Introduction 472

6.2.2.2 Requirements for 4-step RA type 472

6.2.2.2.1 Contention based random access 473

6.2.2.2.1.1 Correct behaviour when transmitting Random Access Preamble 473

6.2.2.2.1.2 Correct behaviour when receiving Random Access Response 473

6.2.2.2.1.3 Correct behaviour when not receiving Random Access Response 473

6.2.2.2.1.4 Correct behaviour when receiving an UL grant for msg3 retransmission 473

6.2.2.2.1.5 SA: Correct behaviour when receiving a message over Temporary C-RNTI 473

6.2.2.2.1.6 Correct behaviour when contention Resolution timer expires 473

6.2.2.2.2 Non-Contention based random access 474

6.2.2.2.2.1 Correct behaviour when transmitting Random Access Preamble 474

6.2.2.2.2.2 Correct behaviour when receiving Random Access Response 474

6.2.2.2.2.3 Correct behaviour when not receiving Random Access Response 474

6.2.2.2.3 UE behaviour when configured with supplementary UL 475

6.2.2.3 Requirements for 2-step RA type 475

6.2.2.3.1 Contention based random access 475

6.2.2.3.1.1 Correct behaviour when transmitting MsgA 475

6.2.2.3.1.2 Correct behaviour when receiving MsgB 475

6.2.2.3.1.3 Correct behaviour when not receiving MsgB 476

6.2.2.3.2 Non-Contention based random access 476

6.2.2.3.2.1 Correct behaviour when transmitting MsgA 476

6.2.2.3.2.2 Correct behaviour when receiving MsgB 476

6.2.2.3.2.3 Correct behaviour when not receiving MsgB 476

6.2.2.3.3 UE behaviour when configured with supplementary UL 476

6.2.2A Random access when CCA is used on target frequency 477

6.2.2A.1 Introduction 477

6.2.2A.2 Requirements for 4-step RA type 477

6.2.2A.2.1 Contention based random access 477

6.2.2A.2.1.1 Correct behaviour when transmitting Random Access Preamble 477

6.2.2A.2.1.2 Correct behaviour when receiving Random Access Response 478

6.2.2A.2.1.3 Correct behaviour when not receiving Random Access Response 478

6.2.2A.2.1.4 Correct behaviour when receiving an UL grant for msg3 retransmission 478

6.2.2A.2.1.6 Correct behaviour when contention Resolution timer expires 478

6.2.2A.2.2 Non-Contention based random access 478

6.2.2A.2.2.1 Correct behaviour when transmitting Random Access Preamble 478

6.2.2A.2.2.2 Correct behaviour when receiving Random Access Response 479

6.2.2A.2.2.3 Correct behaviour when not receiving Random Access Response 479

6.2.2A.3 Requirements for 2-step RA type 479

6.2.2A.3.1 Contention based random access 479

6.2.2A.3.1.1 Correct behaviour when transmitting MsgA 479

6.2.2A.3.1.2 Correct behaviour when receiving MsgB 480

6.2.2A.3.1.3 Correct behaviour when not receiving MsgB 480

6.2.2A.3.2 Non-Contention based random access 480

6.2.2A.3.2.1 Correct behaviour when transmitting MsgA 480

6.2.2A.3.2.2 Correct behaviour when receiving MsgB 481

6.2.2A.3.2.3 Correct behaviour when not receiving MsgB 481

6.2.2B Random access for RedCap 481

6.2.2B.1 Introduction 481

6.2.2B.2 Requirements 482

6.2.2C PDCCH ordered Random Access for LTM 482

6.2.2C.1 Introduction 482

6.2.2C.2 PDCCH ordered Random Access delay 482

6.2.3 SA: RRC Connection Release with Redirection 483

6.2.3.1 Introduction 483

6.2.3.2 Requirements 483

6.2.3.2.1 RRC connection release with redirection to NR 483

6.2.3.2.2 RRC connection release with redirection to E-UTRAN 484

6.2.3.2.3 RRC connection release with redirection to NR carrier subject to CCA 485

6.2.3A SA: RRC Connection Release with Redirection for RedCap 486

6.2.3A.1 Introduction 486

6.2.3A.2 Requirements 486

6.2.3A.2.1 RRC connection release with redirection to NR 486

6.2.3A.2.2 RRC connection release with redirection to E-UTRAN 486

6.2C RRC Connection Mobility Control for Satellite Access 487

6.2C.1 SA: RRC Re-establishment for Satellite Access 487

6.2C.1.1 Introduction 487

6.2C.1.2 Requirements 487

6.2C.1.2.1 UE Re-establishment delay requirement 487

6.2C.1.2.2 UE Re-establishment delay requirement for VSAT 489

6.2C.2 Random access for satellite access 489

6.2C.2.1 Introduction 489

6.2C.2.2 Requirements for 4-step RA type 489

6.2C.2.2.1 Contention based random access 490

6.2C.2.2.1.1 Correct behaviour when transmitting Random Access Preamble 490

6.2C.2.2.1.2 Correct behaviour when receiving Random Access Response 490

6.2C.2.2.1.3 Correct behaviour when not receiving Random Access Response 490

6.2C.2.2.1.4 Correct behaviour when receiving an UL grant for msg3 retransmission 490

6.2C.2.2.1.5 SA: Correct behaviour when receiving a message over Temporary C-RNTI 490

6.2C.2.2.1.6 Correct behaviour when Contention Resolution Timer expires 490

6.2C.2.2.2 Non-Contention based random access 491

6.2C.2.2.2.1 Correct behaviour when transmitting Random Access Preamble 491

6.2C.2.2.2.2 Correct behaviour when receiving Random Access Response 491

6.2C.2.2.2.3 Correct behaviour when not receiving Random Access Response 491

6.2C.2.3 Requirements for 2-step RA type 492

6.2C.2.3.1 Contention based random access 492

6.2C.2.3.1.1 Correct behaviour when transmitting MsgA 492

6.2C.2.3.1.2 Correct behaviour when receiving MsgB 492

6.2C.2.3.1.3 Correct behaviour when not receiving MsgB 493

6.2C.2.3.2 Non-Contention based random access 493

6.2C.2.3.2.1 Correct behaviour when transmitting MsgA 493

6.2C.2.3.2.2 Correct behaviour when receiving MsgB 493

6.2C.2.3.2.3 Correct behaviour when not receiving MsgB 493

6.2C.3 SA: RRC Connection Release with Redirection for Satellite Access 493

6.2C.3.1 Introduction 493

6.2C.3.2 Requirements 494

6.2C.3.2.1 RRC connection release with redirection to NR 494

6.2D RRC Connection Mobility Control for ATG 495

6.2D.1 SA: RRC Re-establishment 495

6.2D.1.1 Introduction 495

6.2D.1.2 Requirements 495

6.2D.1.2.1 UE Re-establishment delay requirement 495

6.2D.2 Random access 496

6.2D.2.1 Introduction 496

6.2D.2.2 Requirements for 4-step RA type 496

6.2D.2.3 Requirements for 2-step RA type 497

6.2D.3 SA: RRC Connection Release with Redirection 497

6.2D.3.1 Introduction 497

6.2D.3.2 Requirements 497

6.2D.3.2.1 RRC connection release with redirection to NR 497

6.2E RRC Connection Mobility Control for RedCap UE with Satellite Access 498

6.2E.1 SA: RRC Re-establishment for RedCap UE with Satellite Access 498

6.2E.1.1 Introduction 498

6.2E.1.2 Requirements 498

6.2E.2 Random access for RedCap UE with satellite access 499

6.2E.2.1 Introduction 499

6.2E.2.2 Requirements 499

6.2E.3 SA: RRC Connection Release with Redirection for RedCap UE with Satellite Access 499

6.2E.3.1 Introduction 499

6.2E.3.2 Requirements 500

6.2E.3.2.1 RRC connection release with redirection to NR 500

6.3 L1/L2-Triggered Mobility 500

6.3.1 LTM PCell Cell Switch 500

6.3.1.1 Introduction 500

6.3.1.2 LTM Cell Switch delay 502

6.3.1.3 Interruption time 502

6.3.2 Conditional L1/L2-Triggered Mobility 503

6.3.2.1 Introduction 503

6.3.2.2 CLTM Cell Switch delay 504

6.3.2.2.1 Measurement time 504

6.3.2.2.2 CLTM RRC processing time 505

6.3.2.2.3 Interruption time 506

6.3.2.3 Subsequent CLTM Cell Switch delay 507

7 Timing 507

7.1 UE transmit timing 507

7.1.1 Introduction 507

7.1.2 Requirements 508

7.1.2.1 Gradual timing adjustment 510

7.1.2.2 Void 511

7.1.2.3 One shot large UL timing adjustment for FR2 Power Class 6 UE 511

7.1.2.4 UE transmit timing for positioning measurements 512

7.1A UE transmit timing for RedCap 512

7.1A.1 Introduction 512

7.1A.2 Requirements 512

7.1A.2.1 Gradual timing adjustment 513

7.1A.2.2 UE transmit timing for positioning measurements 514

7.1C UE transmit timing for Satellite Access 514

7.1C.1 Introduction 514

7.1C.2 Requirements 514

7.1C.2.1 Gradual timing adjustment 516

7.1D UE transmit timing for ATG 516

7.1D.1 Introduction 516

7.1D.2 Requirements 516

7.1D.2.1 Gradual timing adjustment 517

7.1E UE transmit timing for RedCap with Satellite Access 517

7.1E.1 Introduction 517

7.1E.2 Requirements 518

7.1E.2.1 Gradual timing adjustment 518

7.2 UE timer accuracy 518

7.2.1 Introduction 518

7.2.2 Requirements 518

7.2A UE timer accuracy for RedCap 518

7.2A.1 Introduction 518

7.2A.2 Requirements 518

7.2C UE timer accuracy for satellite access 519

7.2C.1 Introduction 519

7.2C.2 Requirements 519

7.2D UE timer accuracy for ATG 519

7.2D.1 Introduction 519

7.2D.2 Requirements 519

7.2E UE timer accuracy for RedCap with Satellite Access 520

7.2E.1 Introduction 520

7.2E.2 Requirements 520

7.3 Timing advance 520

7.3.1 Introduction 520

7.3.2 Requirements 520

7.3.2.1 Timing Advance adjustment delay 520

7.3.2.2 Timing Advance adjustment accuracy 520

7.3A Timing Advance for RedCap 520

7.3A.1 Introduction 520

7.3A.2 Requirements 521

7.3A.2.1 Timing Advance adjustment delay 521

7.3A.2.2 Timing Advance adjustment accuracy 521

7.3C Timing advance for satellite access 521

7.3C.1 Introduction 521

7.3C.2 Requirements 521

7.3C.2.1 Timing Advance adjustment delay 521

7.3C.2.2 Timing Advance adjustment accuracy 521

7.3D Timing advance for ATG 522

7.3D.1 Introduction 522

7.3D.2 Requirements 522

7.3D.2.1 Timing Advance adjustment delay 522

7.3D.2.2 Timing Advance adjustment accuracy 522

7.3E Timing advance for RedCap with Satellite Access 522

7.3E.1 Introduction 522

7.3E.2 Requirements 522

7.3E.2.1 Timing Advance adjustment delay 522

7.3E.2.2 Timing Advance adjustment accuracy 522

7.4 Cell phase synchronization accuracy 522

7.4.1 Definition 522

7.4.2 Minimum requirements 523

7.5 Maximum Transmission Timing Difference 523

7.5.1 Introduction 523

7.5.2 Minimum requirements for inter-band EN-DC 523

7.5.2.1 Minimum requirements for inter-band synchronous EN-DC 523

7.5.3 Minimum requirements for intra-band EN-DC 524

7.5.4 Minimum requirements for NR Carrier Aggregation 525

7.5.5 Minimum requirements for inter-band NE-DC 526

7.5.5.1 Minimum requirements for inter-band synchronous NE-DC 526

7.5.6 Minimum requirements for inter-band NR-DC 526

7.5.7 Minimum requirements for multi-TRP 527

7.6 Maximum Receive Timing Difference 528

7.6.1 Introduction 528

7.6.2 Minimum requirements for inter-band EN-DC 528

7.6.2.1 Minimum requirements for inter-band synchronous EN-DC 529

7.6.3 Minimum requirements for intra-band EN-DC 530

7.6.4 Minimum requirements for NR Carrier Aggregation 530

7.6.5 Minimum requirements for inter-band NE-DC 532

7.6.5.1 Minimum requirements for inter-band synchronous NE-DC 532

7.6.6 Minimum requirements for inter-band NR-DC 532

7.6.7 Minimum requirements for PC6 UE in FR2 533

7.6.8 Minimum requirements for Multi-TRPs 533

7.6D Maximum Receive Timing Difference for ATG UE 534

7.6D.1 Introduction 534

7.6D.2 Minimum requirements for NR Carrier Aggregation 534

7.7 deriveSSB-IndexFromCell tolerance 534

7.7.1 Minimum requirements 534

7.7A deriveSSB-IndexFromCell tolerance for RedCap 535

7.7A.1 Minimum requirements 535

7.7D DeriveSSB-IndexFromCell tolerance for ATG 535

7.7D.1 Minimum requirements 535

7.8 Void 535

7.9 deriveSSB-IndexFromCellInter-r17 tolerance 535

7.9.1 Minimum requirements 535

7.9D DeriveSSB-IndexFromCellInter-r17 tolerance for ATG 536

7.9D.1 Minimum requirements 536

8 Signalling characteristics 590

8.1 Radio Link Monitoring 590

8.1.1 Introduction 590

8.1.1.1 Introduction of Requirement on Radio Link Monitoring for UE Configured with Relaxed Measurement Criteria 591

8.1.2 Requirements for SSB based radio link monitoring 592

8.1.2.1 Introduction 592

8.1.2.2 Minimum requirement 593

8.1.2.3 Measurement restrictions for SSB based RLM 597

8.1.2.4 Minimum requirement of SSB based radio link monitoring for UE fulfilling relaxed measurement criteria 598

8.1.3 Requirements for CSI-RS based radio link monitoring 599

8.1.3.1 Introduction 599

8.1.3.2 Minimum requirement 599

8.1.3.3 Measurement restrictions for CSI-RS based RLM 604

8.1.3.4 Minimum requirement of CSI-RS based radio link monitoring for UE fulfilling relaxed measurement criteria 606

8.1.4 Minimum requirement at transitions 606

8.1.5 Minimum requirement for UE turning off the transmitter 607

8.1.6 Minimum requirement for L1 indication 607

8.1.7 Scheduling availability of UE during radio link monitoring 607

8.1.7.1 Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1 607

8.1.7.2 Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1 608

8.1.7.3 Scheduling availability of UE performing radio link monitoring on FR2 608

8.1.7.4 Scheduling availability of UE performing radio link monitoring on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC 609

8.1.8 Minimum requirement under IDC Interference 610

8.1A Radio Link Monitoring with CCA on Target Frequency 610

8.1A.1 Introduction 610

8.1A.2 Requirements for SSB Based Radio Link Monitoring 611

8.1A.2.1 Introduction 611

8.1A.2.2 Minimum Requirement 611

8.1A.2.3 Measurement Restrictions for SSB based RLM 614

8.1A.3 Minimum requirement at transitions 614

8.1A.4 Minimum requirement for UE turning off the transmitter 615

8.1A.5 Minimum requirement for L1 indication 615

8.1A.6 Scheduling availability of UE during radio link monitoring 615

8.1A.6.3 Scheduling availability of UE performing radio link monitoring on FR2-2 615

8.1A.6.4 Scheduling availability of UE performing radio link monitoring on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR-DC 616

8.1B Radio Link Monitoring for RedCap 616

8.1B.1 Introduction 616

8.1B.2 Requirements for SSB based radio link monitoring 617

8.1B.2.1 Introduction 617

8.1B.2.2 Minimum requirement 618

8.1B.2.3 Measurement restrictions for SSB based RLM 620

8.1B.3 Requirements for CSI-RS based radio link monitoring 620

8.1B.3.1 Introduction 620

8.1B.3.2 Minimum requirement 621

8.1B.3.3 Measurement restrictions for CSI-RS based RLM 623

8.1B.4 Minimum requirement at transitions 624

8.1B.5 Minimum requirement for UE turning off the transmitter 624

8.1B.6 Minimum requirement for L1 indication 624

8.1B.7 Scheduling availability of UE during radio link monitoring 625

8.1B.7.1 Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1 625

8.1B.7.2 Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1 625

8.1B.7.3 Scheduling availability of UE performing radio link monitoring on FR2 625

8.1C Radio Link Monitoring for Satellite Access 626

8.1C.1 Introduction 626

8.1C.2 Requirements for SSB based radio link monitoring 627

8.1C.2.1 Introduction 627

8.1C.2.2 Minimum requirement 628

8.1C.2.3 Measurement restrictions for SSB based RLM 629

8.1C.3 Requirements for CSI-RS based radio link monitoring 630

8.1C.3.1 Introduction 630

8.1C.3.2 Minimum requirement 630

8.1C.3.3 Measurement restrictions for CSI-RS based RLM 632

8.1C.4 Minimum requirement at transitions 632

8.1C.5 Minimum requirement for UE turning off the transmitter 632

8.1C.6 Minimum requirement for L1 indication 633

8.1C.7 Scheduling availability of UE during radio link monitoring 633

8.1C.7.1 Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1-NTN and FR2-NTN 633

8.1C.7.2 Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1-NTN and FR2-NTN 633

8.1D Radio Link Monitoring for ATG 633

8.1D.1 Introduction 633

8.1D.2 Requirements for SSB based radio link monitoring 634

8.1D.2.1 Introduction 634

8.1D.2.2 Minimum requirement 635

8.1D.2.3 Measurement restrictions for SSB based RLM 636

8.1D.3 Requirements for CSI-RS based radio link monitoring 636

8.1D.3.1 Introduction 636

8.1D.3.2 Minimum requirement 636

8.1D.3.3 Measurement restrictions for CSI-RS based RLM 638

8.1D.4 Minimum requirement at transitions 638

8.1D.5 Minimum requirement for UE turning off the transmitter 638

8.1D.6 Minimum requirement for L1 indication 638

8.1D.7 Scheduling availability of UE during radio link monitoring 638

8.1D.7.1 Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1 638

8.1D.7.2 Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1 638

8.1E Radio Link Monitoring for RedCap UE with Satellite Access 639

8.1E.1 Introduction 639

8.1E.2 Requirements for SSB based radio link monitoring 639

8.1E.2.1 Introduction 639

8.1E.2.2 Minimum requirement 640

8.1E.2.3 Measurement restrictions for SSB based RLM 640

8.1E.3 Requirements for CSI-RS based radio link monitoring 640

8.1E.3.1 Introduction 640

8.1E.3.2 Minimum requirement 641

8.1E.3.3 Measurement restrictions for CSI-RS based RLM 642

8.1E.4 Minimum requirement at transitions 642

8.1E.5 Minimum requirement for UE turning off the transmitter 642

8.1E.6 Minimum requirement for L1 indication 642

8.1E.7 Scheduling availability of UE during radio link monitoring 642

8.1E.7.1 Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH 642

8.1E.7.2 Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH 642

8.2 Interruption 642

8.2.1 EN-DC Interruption 642

8.2.1.1 Introduction 642

8.2.1.2 Requirements 643

8.2.1.2.1 Interruptions at transitions between active and non-active during DRX 643

8.2.1.2.2 Interruptions at transitions from non-DRX to DRX 644

8.2.1.2.3 Interruptions at SCell addition/release 644

8.2.1.2.4 Interruptions at SCell activation/deactivation 646

8.2.1.2.5 Interruptions during measurements on SCC 649

8.2.1.2.6 Interruptions at UL carrier RRC reconfiguration 651

8.2.1.2.7 Interruptions due to Active BWP switching Requirement 651

8.2.1.2.8 Interruptions at direct SCell activation and hibernation 652

8.2.1.2.9 Interruptions at SCell hibernation 653

8.2.1.2.10 Interruptions at SCell activation/deactivation with multiple downlink SCells 653

8.2.1.2.11 Interruptions due to UE-specific CBW change 653

8.2.1.2.12 Interruptions at NR SRS carrier based switching 654

8.2.1.2.13 Interruptions at E-UTRA SRS carrier based switching 655

8.2.1.2.14 DL Interruptions at switching between two uplink carriers 656

8.2.1.2.15 Interruptions due to SCell dormancy 656

8.2.1.2.16 Interruptions when identifying CGI of an NR cell with autonomous gaps 657

8.2.1.2.17 Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps 657

8.2.1.2.18 Interruptions at NR SRS antenna port switching 658

8.2.1.2.19 Interruptions at fast SCell activation 659

8.2.1.2.20 Interruptions due to PUCCH SCell activation/deactivation 660

8.2.1.2.21 Interruptions at OD-SSB activation/deactivation 660

8.2.2 SA: Interruptions with Standalone NR Carrier Aggregation 661

8.2.2.1 Introduction 661

8.2.2.2 Requirements 662

8.2.2.2.1 Interruptions at SCell addition/release 662

8.2.2.2.2 Interruptions at SCell activation/deactivation 663

8.2.2.2.3 Interruptions during measurements on deactivated SCC 665

8.2.2.2.4 Interruptions at UL carrier RRC reconfiguration 667

8.2.2.2.5 Interruptions due to Active BWP switching Requirement 667

8.2.2.2.6 Interruptions at inter-frequency SFTD measurement 669

8.2.2.2.7 Interruptions at SCell activation/deactivation with multiple downlink SCells 670

8.2.2.2.8 Interruptions due to UE-specific CBW change 670

8.2.2.2.9 Interruptions at NR SRS carrier based switching 670

8.2.2.2.10 DL Interruptions at UE switching between two uplink carriers 672

8.2.2.2.10A DL Interruptions at UE switching between two uplink carriers with two transmit antenna connectors 672

8.2.2.2.10B DL Interruptions at UE switching between one uplink band with one transmit antenna connector and one uplink band with two transmit antenna connectors 673

8.2.2.2.10C DL Interruptions at UE switching between two uplink bands with two transmit antenna connectors 673

8.2.2.2.10D DL Interruptions at UE switching across three or four uplink bands 673

8.2.2.2.10E DL Interruptions at UE switching between two uplink bands with three transmit antenna connectors and maximum two transmit antenna connectors for each band 674

8.2.2.2.11 Interruptions at direct SCell activation 675

8.2.2.2.12 Interruptions due to SCell dormancy 675

8.2.2.2.12.1 Interruptions due to SCell dormancy switch 675

8.2.2.2.12.2 Interruptions due to CQI measurements during SCell dormancy 675

8.2.2.2.12.3 Interruptions due to RRM measurements during SCell dormancy 675

8.2.2.2.13 Interruptions at transitions between active and non-active during DRX 675

8.2.2.2.14 Interruptions when identifying CGI of an NR cell with autonomous gaps 675

8.2.2.2.15 Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps 676

8.2.2.2.16 Interruptions at NR SRS antenna port switching 677

8.2.2.2.17 Interruptions at fast SCell activation 677

8.2.2.2.18 Interruptions due to PUCCH SCell activation/deactivation 678

8.2.2.2.19 Interruptions due to measurements without gap carried out by UE supporting NeedForInterruptionInfoNR 678

8.2.2.2.20 Interruptions due to PDCCH ordered RACH on target LTM cell 679

8.2.2.2.21 Interruptions at NR SRS bandwidth aggregation for positioning 680

8.2.2.2.22 Interruptions at OD-SSB activation/deactivation 682

8.2.3 NE-DC Interruptions 683

8.2.3.1 Introduction 683

8.2.3.2 Requirements 684

8.2.3.2.1 Interruptions at transitions between active and non-active during DRX 684

8.2.3.2.2 Interruptions at transitions from non-DRX to DRX 684

8.2.3.2.3 Interruptions at PSCell/SCell addition/release 684

8.2.3.2.4 Interruptions at SCell activation/deactivation 685

8.2.3.2.5 Interruptions during measurements on SCC 687

8.2.3.2.5.1 Interruptions during measurements on deactivated NR SCC 687

8.2.3.2.5.2 Interruptions during measurements on deactivated E-UTRAN SCC 687

8.2.3.2.5.3 Interruptions during CQI measurements on dormant E-UTRAN SCC 687

8.2.3.2.5.4 Interruptions during RRM measurements on dormant E-UTRAN SCC 687

8.2.3.2.6 Interruptions at UL carrier RRC reconfiguration 688

8.2.3.2.7 Interruptions due to Active BWP switching Requirement 688

8.2.3.2.8 Interruptions at direct SCell activation and hibernation 688

8.2.3.2.9 Interruptions at SCell hibernation 689

8.2.3.2.10 Interruptions at SCell activation/deactivation with multiple downlink SCells 689

8.2.3.2.11 Interruptions at NR SRS carrier based switching 689

8.2.3.2.12 Interruptions at E-UTRA SRS carrier based switching 691

8.2.3.2.13 Interruptions due to SCell dormancy 691

8.2.3.2.14 Interruptions when identifying CGI of an NR cell with autonomous gaps 692

8.2.3.2.15  Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps 692

8.2.3.2.17 Interruptions at fast SCell activation 694

8.2.3.2.18 Interruptions due to UE-specific CBW change 694

8.2.3.2.19 Interruptions due to PUCCH SCell activation/deactivation 695

8.2.3.2.20 Interruptions at OD-SSB activation/deactivation 695

8.2.4 NR-DC: Interruptions 695

8.2.4.1 Introduction 695

8.2.4.2 Requirements 696

8.2.4.2.1 Interruptions at PSCell/SCell addition/release 696

8.2.4.2.2 Interruptions at SCell activation/deactivation 697

8.2.4.2.3 Interruptions during measurements on SCC 698

8.2.4.2.4 Interruptions at UL carrier RRC reconfiguration 698

8.2.4.2.5 Interruptions due to Active BWP switching Requirement 699

8.2.4.2.6 Interruptions at transitions between active and non-active during DRX 699

8.2.4.2.7 Interruptions at transitions from non-DRX to DRX 699

8.2.4.2.8 Interruptions at SCell activation/deactivation with multiple downlink SCells 700

8.2.4.2.9 Interruptions at NR SRS carrier based switching 700

8.2.4.2.10 Interruptions at direct SCell activation 701

8.2.4.2.11 Interruptions when identifying CGI of an NR cell with autonomous gaps 702

8.2.4.2.12 Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps 702

8.2.4.2.13  Interruptions due to SCell dormancy 703

8.2.4.2.14 Interruptions at NR SRS antenna port switching 703

8.2.4.2.15 Interruptions at fast SCell activation 704

8.2.4.2.16 Interruptions at SCG activation/deactivation 705

8.2.4.2.17 Interruptions due to RRM measurements on deactivated SCG 705

8.2.4.2.18 Interruptions during RLM/BFD measurements on deactivated PSCell 705

8.2.4.2.19 Interruptions due to UE-specific CBW change 705

8.2.4.2.20 Interruptions due to PDCCH ordered RACH on target LTM cell 706

8.2.4.2.21 Interruptions at PSCell Cell switch 706

8.2.4.2.22 Interruptions at OD-SSB activation/deactivation 706

8.2.4.2A Void 707

8.2.4.2A.1 Void 707

8.2.4.2A.2 Void 707

8.2.4.2A.3 Void 707

8.2D Interruption for ATG UE 707

8.2D.1 Interruptions with Standalone NR Carrier Aggregation 707

8.2D.1.1 Introduction 707

8.2D.1.2 Requirements 708

8.2D.1.2.1 Interruptions at SCell addition/release 708

8.2D.1.2.2 Interruptions at SCell activation/deactivation 708

8.2D.1.2.3 Interruptions during measurements on deactivated SCC 709

8.2D.1.2.4 Interruptions at direct SCell activation 709

8.2D.1.2.5 Interruptions due to SCell dormancy 710

8.2D.1.2.6 Interruptions at fast SCell activation 710

8.2D.1.2.8 Interruptions due to UE-specific CBW change 711

8.2D.1.2.9 Interruptions when identifying CGI of an NR cell with autonomous gaps 712

8.2D.1.2.10 Interruptions at NR SRS antenna port switching 712

8.3 SCell Activation and Deactivation Delay 713

8.3.1 Introduction 713

8.3.2 SCell Activation Delay Requirement for Deactivated SCell 713

8.3.2A SCell Activation Delay Requirement for Deactivated SCell based on measurement in IDLE/INACTIVE mode 721

8.3.3 SCell Deactivation Delay Requirement for Activated SCell 723

8.3.4 Direct SCell Activation at SCell addition 724

8.3.5 Direct SCell Activation at Handover 726

8.3.7 SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells 728

8.3.8 SCell Deactivation Delay Requirement for Activated SCell with Multiple Downlink SCells 732

8.3.9 Direct SCell Activation of Multiple Downlink SCells at SCell addition 732

8.3.10 Direct SCell Activation of Multiple Downlink SCells at Handover 733

8.3.12 SCell Activation Delay Requirement for Deactivated PUCCH SCell 735

8.3.13 SCell activation delay Requirement for Deactivated PUCCH SCell with Multiple SCells 739

8.3.14 SCell Deactivation Delay Requirement for Activated PUCCH SCell 741

8.3.15 SCell Deactivation Delay Requirement for Activated PUCCH SCell with Multiple Downlink SCells 741

8.3.16 Fast SCell Activation Delay Requirement for Deactivated SCell 742

8.3.17 SCell Activation Delay Requirement for Deactivated SCell with the L3 reporting during activation 744

8.3.18 SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells with L3 reporting 748

8.3.19 OD-SSB based SCell Activation Delay Requirement for Deactivated SCell 751

8.3.20 OD-SSB based SCell Deactivation Delay Requirement for Activated SCell 755

8.3.21 OD-SSB based Direct SCell Activation at SCell addition 756

8.3.22 OD-SSB based SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells 757

8.3.23 OD-SSB based SCell Deactivation Delay Requirement for Activated SCell with Multiple Downlink SCells 761

8.3.25 OD-SSB based SCell Deactivation Delay Requirement for Activated PUCCH SCell 762

8.3.26 OD-SSB based SCell Activation Delay Requirement for Deactivated SCell with the L3 reporting during activation 762

8.3A SCell Activation and Deactivation Delay in Carriers with CCA 763

8.3A.1 Introduction 763

8.3A.2 SCell Activation Delay Requirement for Deactivated SCell 763

8.3A.3 SCell Deactivation Delay Requirement for Activated SCell 767

8.3D SCell Activation and Deactivation Delay for ATG 768

8.3D.1 Introduction 768

8.3D.2 SCell Activation Delay Requirement for Deactivated SCell 768

8.3D.3 SCell Deactivation Delay Requirement for Activated SCell 773

8.3D.4 Direct SCell Activation at SCell addition 773

8.3D.5 Direct SCell Activation at Handover 774

8.3D.6 Direct SCell Activation at RRC Resume 776

8.3D.7 Fast SCell Activation Delay Requirement for Deactivated SCell 776

8.3D.8 SCell Activation Delay Requirement for Deactivated SCell with the L3 reporting during activation 778

8.4 UE UL carrier RRC reconfiguration delay 780

8.4.1 Introduction 780

8.4.2 UE UL carrier configuration delay requirement 781

8.4.3 UE UL carrier deconfiguration delay requirement 781

8.5 Link Recovery Procedures 781

8.5.1 Introduction 781

8.5.1.1 Introduction of Requirement on Link Recovery Procedures for UE configured with relaxed measurement criteria 782

8.5.2 Requirements for SSB based beam failure detection 783

8.5.2.1 Introduction 783

8.5.2.2 Minimum requirement 784

8.5.2.3 Measurement restriction for SSB based beam failure detection 788

8.5.2.4 Minimum requirement of SSB based beam failure detection for UE fulfilling relaxed measurement criteria 789

8.5.3 Requirements for CSI-RS based beam failure detection 790

8.5.3.1 Introduction 790

8.5.3.2 Minimum requirement 791

8.5.3.3 Measurement restrictions for CSI-RS beam failure detection 795

8.5.3.4 Minimum requirement of CSI-RS based beam failure detection for UE fulfilling relaxed measurement criteria 797

8.5.4 Minimum requirement for L1 indication 798

8.5.5 Requirements for SSB based candidate beam detection 798

8.5.5.1 Introduction 798

8.5.5.2 Minimum requirement 799

8.5.5.3 Measurement restriction for SSB based candidate beam detection 803

8.5.6 Requirements for CSI-RS based candidate beam detection 804

8.5.6.1 Introduction 804

8.5.6.2 Minimum requirement 804

8.5.6.3 Measurement restriction for CSI-RS based candidate beam detection 809

8.5.7 Scheduling availability of UE during beam failure detection 810

8.5.7.1 Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1 810

8.5.7.2 Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1 810

8.5.7.3 Scheduling availability of UE performing beam failure detection on FR2 811

8.5.7.4 Scheduling availability of UE performing beam failure detection on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC 812

8.5.8 Scheduling availability of UE during candidate beam detection 812

8.5.8.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 812

8.5.8.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 812

8.5.8.3 Scheduling availability of UE performing L1-RSRP measurement on FR2 813

8.5.8.4 Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC 814

8.5.9 Requirements for Beam Failure Recovery in SCell 814

8.5.9.1 Introduction 814

8.5.9.2 Requirement 814

8.5.10 Minimum requirement at transitions for beam failure detection 814

8.5.11 Minimum requirement under IDC Interference 815

8.5.12 Minimum requirement at transitions for candidate beam detection 815

8.5A Link Recovery Procedures when CCA is used on target frequency 815

8.5A.1 Introduction 815

8.5A.2 Requirements for SSB based beam failure detection 816

8.5A.2.1 Introduction 816

8.5A.2.2 Minimum requirement 816

8.5A.2.3 Measurement restriction for SSB based beam failure detection 818

8.5A.3 Void 819

8.5A.4 Minimum requirement for L1 indication 819

8.5A.5 Requirements for SSB based candidate beam detection 819

8.5A.5.1 Introduction 819

8.5A.5.2 Minimum requirement 819

8.5A.5.3 Measurement restriction for SSB based candidate beam detection 822

8.5A.6 Void 822

8.5A.7 Scheduling availability of UE during beam failure detection 822

8.5A.7.1 Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH 822

8.5A.7.2 Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH 822

8.5A.7.3 Scheduling availability of UE performing beam failure detection on FR2-2 823

8.5A.7.4 Scheduling availability of UE performing beam failure detection on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR-DC 823

8.5A.8 Scheduling availability of UE during candidate beam detection 823

8.5A.8.3 Scheduling availability of UE performing L1-RSRP measurement on FR2-2 823

8.5.8A.4 Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR-DC 823

8.5B Link Recovery Procedures for Redcap 823

8.5B.1 Introduction 823

8.5B.2 Requirements for SSB based beam failure detection for Redcap 824

8.5B.2.1 Introduction 824

8.5B.2.2 Minimum requirement 824

8.5B.2.3 Measurement restriction for SSB based beam failure detection 826

8.5B.3 Requirements for CSI-RS based beam failure detection for Redcap 826

8.5B.3.1 Introduction 826

8.5B.3.2 Minimum requirement 826

8.5B.3.3 Measurement restrictions for CSI-RS beam failure detection 828

8.5B.4 Minimum requirement for L1 indication for Redcap 829

8.5B.5 Requirements for SSB based candidate beam detection for Redcap 830

8.5B.5.1 Introduction 830

8.5B.5.2 Minimum requirement 830

8.5B.5.3 Measurement restriction for SSB based candidate beam detection 831

8.5B.6 Requirements for CSI-RS based candidate beam detection for Redcap 832

8.5B.6.1 Introduction 832

8.5B.6.2 Minimum requirement 832

8.5B.6.3 Measurement restriction for CSI-RS based candidate beam detection 834

8.5B.7 Scheduling availability of UE during beam failure detection for Redcap 834

8.5B.7.1 Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1 835

8.5B.7.2 Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1 835

8.5B.7.3 Scheduling availability of UE performing beam failure detection on FR2 835

8.5B.8 Scheduling availability of UE during candidate beam detection for Redcap 835

8.5B.8.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 835

8.5B.8.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 836

8.5B.8.3 Scheduling availability of UE performing L1-RSRP measurement on FR2 836

8.5B.9 Minimum requirement at transitions for beam failure detection for Redcap 836

8.5C Link Recovery Procedures for Satellite Access 836

8.5C.1 Introduction 836

8.5C.2 Requirements for SSB based beam failure detection 837

8.5C.2.1 Introduction 837

8.5C.2.2 Minimum requirement 838

8.5C.2.3 Measurement restriction for SSB based beam failure detection 838

8.5C.3 Requirements for CSI-RS based beam failure detection 839

8.5C.3.1 Introduction 839

8.5C.3.2 Minimum requirement 839

8.5C.3.3 Measurement restrictions for CSI-RS beam failure detection 840

8.5C.4 Minimum requirement for L1 indication 841

8.5C.5 Requirements for SSB based candidate beam detection 841

8.5C.5.1 Introduction 841

8.5C.5.2 Minimum requirement 841

8.5C.5.3 Measurement restriction for SSB based candidate beam detection 842

8.5C.6 Requirements for CSI-RS based candidate beam detection 842

8.5C.6.1 Introduction 842

8.5C.6.2 Minimum requirement 842

8.5C.6.3 Measurement restriction for CSI-RS based candidate beam detection 843

8.5C.7 Scheduling availability of UE during beam failure detection 844

8.5C.7.1 Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1-NTN 844

8.5C.7.2 Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1-NTN 844

8.5C.8 Scheduling availability of UE during candidate beam detection 844

8.5C.8.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1-NTN 844

8.5C.8.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1-NTN 844

8.5C.9 Minimum requirement at transitions for beam failure detection 845

8.5D Link Recovery Procedures for ATG 845

8.5D.1 Introduction 845

8.5D.2 Requirements for SSB based beam failure detection 846

8.5D.2.1 Introduction 846

8.5D.2.2 Minimum requirement 846

8.5D.2.3 Measurement restriction for SSB based beam failure detection 847

8.5D.3 Requirements for CSI-RS based beam failure detection 848

8.5D.3.1 Introduction 848

8.5D.3.2 Minimum requirement 848

8.5D.3.3 Measurement restrictions for CSI-RS beam failure detection 849

8.5D.4 Minimum requirement for L1 indication 850

8.5D.5 Requirements for SSB based candidate beam detection 850

8.5D.5.1 Introduction 850

8.5D.5.2 Minimum requirement 850

8.5D.5.3 Measurement restriction for SSB based candidate beam detection 851

8.5D.6 Requirements for CSI-RS based candidate beam detection 852

8.5D.6.1 Introduction 852

8.5D.6.2 Minimum requirement 852

8.5D.6.3 Measurement restriction for CSI-RS based candidate beam detection 853

8.5D.7 Scheduling availability of UE during beam failure detection 854

8.5D.7.1 Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1 854

8.5D.7.2 Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1 854

8.5D.8 Scheduling availability of UE during candidate beam detection 854

8.5D.8.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 854

8.5D.8.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 854

8.5D.9 Minimum requirement at transitions for beam failure detection 855

8.5D.10 Requirements for Beam Failure Recovery in SCell 855

8.5E Link Recovery Procedures for RedCap UE with Satellite Access 855

8.5E.1 Introduction 855

8.5E.2 Requirements for SSB based beam failure detection for RedCap UE with satellite access 855

8.5E.2.1 Introduction 855

8.5E.2.2 Minimum requirement 856

8.5E.2.3 Measurement restrictions for SSB beam failure detection 856

8.5E.3 Requirements for CSI-RS based beam failure detection for RedCap UE with satellite access 856

8.5E.3.1 Introduction 856

8.5E.3.2 Minimum requirement 857

8.5E.3.3 Measurement restrictions for CSI-RS beam failure detection 857

8.5E.4 Minimum requirement for L1 indication for RedCap UE with satellite access 857

8.5E.5 Requirements for SSB based candidate beam detection for RedCap UE with satellite access 858

8.5E.6 Requirements for CSI-RS based candidate beam detection for RedCap UE with satellite access 858

8.5E.7 Scheduling availability of UE during beam failure detection for RedCap UE with satellite access 858

8.5E.8 Scheduling availability of UE during candidate beam detection for RedCap UE with satellite access 858

8.5E.9 Minimum requirement at transitions for beam failure detection for RedCap UE with satellite access 858

8.6 Active BWP switch delay 858

8.6.1 Introduction 858

8.6.2 DCI and timer based BWP switch delay on a single CC 859

8.6.2A DCI based BWP switch delay on multiple CCs 860

8.6.2A.1 Simultaneous DCI based BWP switch delay on multiple CCs 860

8.6.2A.2 Non-simultaneous DCI based BWP switch delay on multiple CCs 862

8.6.2B Timer based BWP switch delay on multiple CCs 862

8.6.2B.1 Simultaneous timer based BWP switch delay on multiple CCs 862

8.6.2B.2 Non-simultaneous timer based BWP switch delay on multiple CCs 863

8.6.3 RRC based BWP switch delay on a single CC 863

8.6.3A RRC based BWP switch delay on multiple CCs 864

8.6.3A.1 Simultaneous RRC based BWP switch delay on multiple CCs 864

8.6.3A.2 Non-simultaneous RRC based BWP switch delay on multiple CCs 864

8.6.4 BWP switch delay on Consistent UL CCA recovery 865

8.6A Active BWP switch delay for RedCap 865

8.6A.1 Introduction 865

8.6A.2 DCI and timer based BWP switch delay on a single CC 865

8.6A.3 RRC based BWP switch delay on a single CC 867

8.6C Active BWP switch delay for satellite access 867

8.6C.1 Introduction 867

8.6C.2 DCI and timer based BWP switch delay on a single CC 867

8.6C.3 RRC based BWP switch delay on a single CC 869

8.6D Active BWP switch delay for ATG 869

8.6D.1 Introduction 869

8.6D.2 DCI and timer based BWP switch delay on a single CC 869

8.6D.2A DCI based BWP switch delay on multiple CCs 871

8.6D.2A.1 Simultaneous DCI based BWP switch delay on multiple CCs 871

8.6D.2B Timer based BWP switch delay on multiple CCs 872

8.6D.2B.1 Simultaneous timer based BWP switch delay on multiple CCs 872

8.6D.2B.2 Non-simultaneous timer based BWP switch delay on multiple CCs 873

8.6D.3 RRC based BWP switch delay on a single CC 874

8.6D.3A RRC based BWP switch delay on multiple CCs 874

8.6D.3A.1 Simultaneous RRC based BWP switch delay on multiple CCs 874

8.6E Active BWP switch delay for RedCap UE with satellite access 875

8.6E.1 Introduction 875

8.6E.2 DCI and timer based BWP switch delay on a single CC 875

8.6E.3 RRC based BWP switch delay on a single CC 875

8.7 Void 875

8.8 NE-DC: E-UTRAN PSCell Addition and Release Delay 875

8.8.1 Introduction 875

8.8.2 E-UTRAN PSCell Addition Delay Requirement 875

8.8.3 E-UTRAN PSCell Release Delay Requirement 876

8.9 NR-DC: PSCell Addition and Release Delay 876

8.9.1 Introduction 876

8.9.2 PSCell Addition Delay Requirement 876

8.9.3 PSCell Release Delay Requirement 877

8.9A Conditional PSCell Addition Delay 877

8.9A.1 Introduction 877

8.9A.2 Conditional PSCell Addition Delay Requirement 877

8.9A.2.1 Measurement time 878

8.9B NR-DC: PSCell Addition and Release Delay in Carriers with CCA 878

8.9B.1 Introduction 878

8.9B.2 PSCell Addition Delay Requirement 878

8.9B.3 PSCell Release Delay Requirement 879

8.9C Subsequent Conditional PSCell Addition Delay 880

8.9C.1 Introduction 880

8.9C.2 Subsequent Conditional PSCell Addition Delay Requirement 880

8.9C.2.1 Measurement time 880

8.10 Active TCI state switching delay 881

8.10.1 Introduction 881

8.10.2 Known conditions for TCI state 881

8.10.2A Known conditions for TCI state with beam prediction 881

8.10.3A MAC-CE based TCI state switch delay in HST FR2 scenarios 883

8.10.4 DCI based TCI state switch delay 883

8.10.5 RRC based TCI state switch delay 883

8.10.6 Active TCI state list update delay 884

8.10A Active TCI state switching delay with CCA 884

8.10A.1 Introduction 884

8.10A.2 Known conditions for TCI state 884

8.10A.3 MAC-CE based TCI state switch delay 885

8.10A.4 DCI based TCI state switch delay 886

8.10A.5 RRC based TCI state switch delay 886

8.10A.6 Active TCI state list update delay 887

8.10B Active TCI state switching delay for RedCap 887

8.10B.1 Introduction 887

8.10B.2 Known conditions for TCI state 887

8.10B.3 MAC-CE based TCI state switch delay 887

8.10B.4 DCI based TCI state switch delay 888

8.10B.5 RRC based TCI state switch delay 889

8.10B.6 Active TCI state list update delay 889

8.10C Active TCI state switching delay for satellite access 889

8.10C.1 Introduction 889

8.10C.2 MAC-CE based TCI state switch delay 890

8.10C.4 DCI based TCI state switch delay 890

8.10C.5 RRC based TCI state switch delay 890

8.10C.6 Active TCI state list update delay 890

8.10D Active TCI state switching delay for ATG 890

8.10D.2 Void 891

8.10D.6 Active TCI state list update delay 891

8.10E Active TCI state switching delay for UE operating in FR2-1 and configured with groupBasedBeamReporting-r17 892

8.10E.1 Introduction 892

8.10E.2 Known conditions for TCI state 892

8.10E.3 MAC-CE based dual DL TCI state switch delay 892

8.10E.3.1 MAC-CE based dual DL TCI state switching delay for sDCI 892

8.10E.3.2 MAC-CE based dual DL TCI state switching delay for mDCI 893

8.10E.4 DCI based dual DL TCI state switch delay for sDCI and mDCI 893

8.10E.4.1 DCI based dual DL TCI state switching delay for sDCI 893

8.10E.4.2 DCI based dual DL TCI state switching delay for mDCI 893

8.10E.5 RRC based dual DL TCI state switch delay 894

8.10E.6 Active DL TCI state list update delay 894

8.10E.6.1 Active DL TCI state list update delay for sDCI 894

8.10E.6.2 Active DL TCI state list update delay for mDCI 894

8.10F Active TCI state switching delay for RedCap UE with satellite access 894

8.10F.1 Introduction 894

8.10F.2 MAC-CE based TCI state switch delay 894

8.10F.4 DCI based TCI state switch delay 894

8.10F.5 RRC based TCI state switch delay 894

8.10F.6 Active TCI state list update delay 894

8.11 PSCell Change 894

8.11A PSCell Change in Carriers with CCA 895

8.11B Conditional PSCell Change 895

8.11B.1 Introduction 895

8.11B.2 Conditional PSCell Change delay 895

8.11B.2.1 Measurement time 896

8.11D Conditional PSCell Change in Carriers with CCA 897

8.11D.1 Introduction 897

8.11D.2 Conditional PSCell Change delay 897

8.11D.2.1 Measurement time 898

8.11E Subsequent Conditional PSCell Change 898

8.11E.1 Introduction 898

8.11E.2 Subsequent Conditional PSCell Change delay 898

8.11E.2.1 Measurement time 899

8.12 Uplink spatial relation switch delay 899

8.12.1 Introduction 899

8.12.2 Known conditions for spatial relation when associated with DL-RS 899

8.12.3 MAC-CE based spatial relation switch delay 900

8.12.4 DCI based spatial relation switch delay 900

8.12.5 RRC based spatial relation switch delay 901

8.12A Uplink spatial relation switch delay for RedCap 901

8.12A.1 Introduction 901

8.12A.2 Known conditions for spatial relation when associated with DL-RS 901

8.12A.3 MAC-CE based spatial relation switch delay 902

8.12A.4 DCI based spatial relation switch delay 902

8.12A.5 RRC based spatial relation switch delay 903

8.12C Uplink spatial relation switch delay for satellite access 903

8.12C.1 Void 903

8.12C.2 Void 903

8.12C.3 Void 903

8.12C.4 Void 903

8.12C.5 Void 903

8.13 UE-specific CBW change 903

8.13.1 Introduction 903

8.13.2 UE-specific CBW change delay 904

8.13A UE-specific CBW change for RedCap 904

8.13A.1 Introduction 904

8.13A.2 UE-specific CBW change delay 904

8.13C UE-specific CBW change for satellite access 904

8.13C.1 Introduction 904

8.13C.2 UE-specific CBW change delay 905

8.13D UE-specific CBW change for ATG 905

8.13D.1 Introduction 905

8.13D.2 UE-specific CBW change delay 905

8.13E UE-specific CBW change for RedCap UE with satellite access 905

8.13E.1 Introduction 905

8.13E.2 UE-specific CBW change delay 905

8.14 Pathloss reference signal switching delay 905

8.14.1 Introduction 905

8.14.2 Known conditions for pathloss reference signal 906

8.14.3 MAC-CE based pathloss reference signal switch delay 906

8.14C Pathloss reference signal switching delay for satellite access 907

8.14C.1 Introduction 907

8.14C.2 Known conditions for pathloss reference signal 907

8.14C.3 MAC-CE based pathloss reference signal switch delay 908

8.14D Pathloss reference signal switching delay for ATG 908

8.14D.1 Introduction 908

8.14D.2 Known conditions for pathloss reference signal 908

8.14D.3 MAC-CE based pathloss reference signal switch delay 908

8.14E Pathloss reference signal switching delay for RedCap UE with satellite access 908

8.14E.1 Introduction 908

8.14E.2 Known conditions for pathloss reference signal 909

8.14E.3 MAC-CE based pathloss reference signal switch delay 909

8.15 Active downlink TCI state switching delay for unified TCI 909

8.15.1 Introduction 909

8.15.4 DCI based downlink TCI state switch delay 911

8.15.5 Active Downlink TCI state list update delay 911

8.15D Active downlink TCI state switching delay for unified TCI for ATG 912

8.15D.1 Introduction 912

8.15D.2 Void 912

8.15D.4 DCI based downlink TCI state switch delay 912

8.15D.5 Active Downlink TCI state list update delay 913

8.16 Active uplink TCI state switching delay for unified TCI 913

8.16.1 Introduction 913

8.16.3 MAC-CE based uplink TCI state switch delay 914

8.16.4 DCI based uplink TCI state switch delay 916

8.16.5 Active Uplink TCI state list update delay 916

8.16D Active uplink TCI state switching delay for unified TCI for ATG 918

8.16D.1 Introduction 918

8.16D.2 Void 918

8.16D.3 MAC-CE based uplink TCI state switch delay 918

8.16D.4 DCI based uplink TCI state switch delay 919

8.16D.5 Active Uplink TCI state list update delay 919

8.17 SCG Activation and Deactivation Delay 919

8.17.1 Introduction 919

8.17.2 SCG Activation Delay Requirement 920

8.17.3 SCG Deactivation Delay Requirement 921

8.18 TRP specific Link Recovery Procedures 921

8.18.1 Introduction 921

8.18.2 Requirements for TRP specific SSB based beam failure detection 922

8.18.2.1 Introduction 922

8.18.2.2 Minimum requirement 922

8.18.2.3 Measurement restriction for SSB based beam failure detection 924

8.18.3 Requirements for CSI-RS based beam failure detection 925

8.18.3.1 Introduction 925

8.18.3.2 Minimum requirement 925

8.18.3.3 Measurement restrictions for CSI-RS beam failure detection 929

8.18.4 Minimum requirement for L1 indication 930

8.18.5 Requirements for SSB based candidate beam detection 930

8.18.5.1 Introduction 930

8.18.5.2 Minimum requirement 930

8.18.5.3 Measurement restriction for SSB based candidate beam detection 933

8.18.6 Requirements for CSI-RS based candidate beam detection 934

8.18.6.1 Introduction 934

8.18.6.2 Minimum requirement 934

8.18.6.3 Measurement restriction for CSI-RS based candidate beam detection 936

8.18.7 Requirements for TRP specific Beam Failure Recovery 937

8.18.7.1 Introduction 937

8.18.7.2 Requirement 938

8.18.8 Scheduling availability of UE during TRP specific beam failure detection 938

8.18.8.1 Scheduling availability of UE performing TRP specific beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1 938

8.18.8.2 Scheduling availability of UE performing TRP specific beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1 938

8.18.8.3 Scheduling availability of UE performing TRP specific beam failure detection on FR2 938

8.18.8.4 Scheduling availability of UE performing TRP specific beam failure detection on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC 939

8.18.9 Scheduling availability of UE during TRP specific candidate beam detection 939

8.18.9.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 939

8.18.9.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 940

8.18.9.3 Scheduling availability of UE performing L1-RSRP measurement on FR2 940

8.18.9.4 Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC 940

8.19 Pre-configured measurement gap activation/deactivation delay 941

8.19.1 Introduction 941

8.19.2 Pre-configured measurement gap activation/deactivation upon DCI/timer-based BWP switch 941

8.19.2.1 Activation/deactivation upon DCI/timer-based BWP switch delay on a single CC 941

8.19.3 Pre-configured measurement gap activation/deactivation upon SCell activation/deactivation 941

8.19.4 Pre-configured measurement gap activation/deactivation upon RRC reconfiguration 941

8.19.5 Activation/deactivation delay requirements for concurrent measurement gaps with Pre-MG 941

8.19.5.1 Activation/deactivation delay requirements for non-overlapped activation/deactivation of concurrent measurement gaps with Pre- MG 942

8.19.5.2 Activation/deactivation delay requirements for fully overlapped activation/deactivation of concurrent measurement gaps with Pre- MG 942

8.19.5.3 Pre-MG activation/deactivation delay when colliding with a concurrent measurement gap 942

8.19D Pre-configured measurement gap activation/deactivation delay for ATG 942

8.19D.1 Introduction 942

8.19D.2 Pre-configured measurement gap activation/deactivation upon DCI/timer-based BWP switch 942

8.19D.2.1 Activation/deactivation upon DCI/timer-based BWP switch delay on a single CC 942

8.19D.3 Pre-configured measurement gap activation/deactivation upon RRC reconfiguration 943

8.19D.4 Pre-configured measurement gap activation/deactivation upon SCell activation/deactivation 943

8.20 LTM PSCell Cell Switch 943

8.20.1 Introduction 943

8.20.2 LTM Cell Switch delay 944

8.20.3 Void 944

8.21 Active downlink TCI state switching delay for unified TCI for single-DCI mTRP 944

8.21.1 Introduction 944

8.21.2 Known conditions for downlink TCI state 945

8.21.3 MAC-CE based downlink TCI state switch delay 945

8.21.4 DCI based downlink TCI state switch delay 946

8.21.5 Active Downlink TCI state list update delay 946

8.22 Active downlink TCI state switching delay for unified TCI for multi-DCI mTRP 947

8.22.1 Introduction 947

8.22.2 Known conditions for downlink TCI state 948

8.22.3 MAC-CE based downlink TCI state switch delay 948

8.22.4 DCI based downlink TCI state switch delay 949

8.22.5 Active Downlink TCI state list update delay 949

8.23 Active uplink TCI state switching delay for unified TCI for single-DCI mTRP 950

8.23.1 Introduction 950

8.23.2 Known conditions for uplink TCI state 950

8.23.3 MAC-CE based uplink TCI state switch delay 951

8.23.4 DCI based uplink TCI state switch delay 952

8.23.5 Active uplink TCI state list update delay 952

8.24 Active uplink TCI state switching delay for unified TCI for multi-DCI mTRP 953

8.24.1 Introduction 953

8.24.2 Known conditions for uplink TCI state 954

8.24.3 MAC-CE based uplink TCI state switch delay 954

8.24.4 DCI based uplink TCI state switch delay 955

8.24.5 Active Uplink TCI state list update delay 955

8.25 TCI state activation for LTM candidate cell 956

8.25.1 Introduction 956

8.25.2 Known TCI state conditions 957

8.25.3 SSB based TCI state activation delay 957

9 Measurement Procedure 958

9.1 General measurement requirement 958

9.1.1 Introduction 958

9.1.2 Measurement gap 958

9.1.2.1 EN-DC: Measurement Gap Sharing 968

9.1.2.1a SA: Measurement Gap Sharing 968

9.1.2.1b NE-DC: Measurement Gap Sharing 969

9.1.2.1c NR-DC: Measurement Gap Sharing 970

9.1.3 UE Measurement capability 971

9.1.3.1 EN-DC: Monitoring of multiple layers using gaps 971

9.1.3.1a SA: Monitoring of multiple layers using gaps 972

9.1.3.1b NE-DC: Monitoring of multiple layers using gaps 972

9.1.3.1c NR-DC: Monitoring of multiple layers using gaps 973

9.1.3.2 EN-DC: Maximum allowed layers for multiple monitoring 973

9.1.3.2a SA: Maximum allowed layers for multiple monitoring 974

9.1.3.2b NE-DC: Maximum allowed layers for multiple monitoring 975

9.1.3.2c NR-DC: Maximum allowed layers for multiple monitoring 975

9.1A.3.2 Void 976

9.1.3A UE Measurement capability under operation mode with CCA 976

9.1.3A.1 EN-DC: Monitoring of multiple layers using gaps under CCA 976

9.1.3A.1a SA: Monitoring of multiple layers using gaps under CCA 976

9.1.3A.2 EN-DC: Maximum allowed layers for multiple monitoring under CCA 976

9.1.3A.2a SA: Maximum allowed layers for multiple monitoring under CCA 977

9.1.3C UE Measurement capability under operation mode with satellite access 977

9.1.3C.1a SA: Monitoring of multiple layers using gaps under satellite access 977

9.1.3C.2a SA: Maximum allowed layers for multiple monitoring for SAN 978

9.1.4 Capabilities for Support of Event Triggering and Reporting Criteria 978

9.1.4.1 Introduction 978

9.1.4.2 Requirements 978

9.1.5 Carrier-specific scaling factor 981

9.1.5.1 Monitoring of multiple layers outside gaps 981

9.1.5.1.1 EN-DC mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3 measurements and RSSI and channel occupancy measurements performed outside gaps 984

9.1.5.1.2 SA mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3 measurements and RSSI and channel occupancy measurements performed outside gaps 988

9.1.5.1.3 NR-DC mode: carrier-specific scaling factor for SSB-based and CSI-RS based L3 measurements performed outside gaps 991

9.1.5.1.4 NE-DC mode: carrier-specific scaling factor for SSB-based and CSI-RS based measurements performed outside gaps 992

9.1.5.2 Monitoring of multiple layers within gaps 994

9.1.5.2.1 EN-DC mode: carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements and RSSI and channel occupancy measurements performed within gaps 996

9.1.5.2.2 SA mode: carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements and RSSI and channel occupancy measurements performed within gaps 998

9.1.5.2.3 NE-DC: carrier-specific scaling factor for SSB-based and CSI-RS based L3 measurements performed within gaps 1000

9.1.5.2.4 NR-DC: carrier-specific scaling factor for SSB-based and CSI-RS-based L3 measurements performed within gaps 1002

9.1.5.2.5 SA mode: carrier-specific scaling factor for PRS-based measurements performed within gaps 1004

9.1.5.2.6 NE-DC: carrier-specific scaling factor for PRS-based measurements performed within gaps 1004

9.1.5.2.7 NR-DC: carrier-specific scaling factor for PRS-based measurements performed within gaps 1004

9.1.5.3 Monitoring of multiple layers within NCSG 1005

9.1.5.3.1 SA mode: carrier-specific scaling factor for measurements performed within NCSG 1006

9.1.5.4 L1-RSRP measurements within measurement gap 1007

9.1.5.4.1 SA mode: carrier-specific scaling factor for L1-RSRP measurements performed within measurement gap 1008

9.1.5.4.2 NR-DC: carrier-specific scaling factor for L1-RSRP measurements performed within measurement gap 1009

9.1.6 Minimum requirement at transitions 1011

9.1.7 Pre-configured measurement gap 1011

9.1.7.1 Introduction 1011

9.1.7.2 Requirements applicability 1012

9.1.7.3 Requirements 1012

9.1.7.3.1 Requirements for autonomous activation/deactivation mechanism 1012

9.1.7.3.2 Requirements for network-controlled activation/deactivation mechanism 1013

9.1.7.3.3 Requirements for reception/transmission during activation/deactivation 1014

9.1.8 Concurrent measurement gaps 1014

9.1.8.1 Introduction 1014

9.1.8.2 Requirements 1014

9.1.8.3 Collision between concurrent measurement gaps 1015

9.1.8.4 Measurement gap related requirements of concurrent measurement gaps 1015

9.1.9 Network controlled small gap 1016

9.1.9.1 Introduction 1016

9.1.9.2 Requirements applicability 1017

9.1.10 MUSIM gaps 1019

9.1.10.1 Introduction 1020

9.1.10.2 Priorities for MUSIM gaps 1021

9.1.10.3 Keep solution for MUSIM gaps 1021

9.1.10.4 Collisions between different MUSIM gaps 1021

9.1.10.5 Collisions between MUSIM gaps and measurement gaps 1021

9.1.10.6 MUSIM gap related requirements 1022

9.1.11 UL gap for Tx power management 1022

9.1.12 Concurrent measurement gaps with Pre-MG 1022

9.1.12.1 Introduction 1022

9.1.12.2 Requirements 1023

9.1.12.3 Collisions involving Pre-MG(s) 1023

9.1.12.4 Collision between Pre-MG activation/deactivation and measurement gap 1024

9.1.12.5 Pre-MG related requirements 1024

9.1.13 Concurrent measurement gaps with NCSG 1024

9.1.13.1 Introduction 1024

9.1.13.2 Requirements 1025

9.1.13.3 Collision involving NCSGs 1026

9.1.14 Measurement gap occasion cancellation 1026

9.1.14.1 Introduction 1026

9.1.14.2 Applicable measurement gap configurations 1026

9.1.14.3 Applicability 1027

9.1.14.4 Requirements for cancelling measurement gap occasions 1027

9.1A General measurement requirement for RedCap 1027

9.1A.1 Introduction 1027

9.1A.2 Measurement gap 1027

9.1A.2.1 SA: Measurement Gap Sharing 1031

9.1A.3 UE Measurement capability 1032

9.1A.3.1 SA: Monitoring of multiple layers using gaps 1032

9.1A.3.2 SA: Maximum allowed layers for multiple monitoring 1032

9.1A.4 Capabilities for Support of Event Triggering and Reporting Criteria 1032

9.1A.4.1 Introduction 1032

9.1A.4.2 Requirements 1033

9.1A.5 Carrier-specific scaling factor 1033

9.1A.5.1 Monitoring of multiple layers outside gaps 1033

9.1A.5.1.1 SA mode: carrier-specific scaling factor for SSB-based measurements performed outside gaps 1034

9.1A.5.2 Monitoring of multiple layers within gaps 1034

9.1A.5.2.1 SA mode: carrier-specific scaling factor for SSB measurements performed within gaps 1034

9.1A.6 Minimum requirement at transitions 1036

9.1C General measurement requirement for SAN 1036

9.1C.1 Introduction 1036

9.1C.2 Measurement gap 1037

9.1C.8 Concurrent measurement gaps for SAN 1039

9.1C.8.1 Introduction 1039

9.1C.8.2 Requirements 1039

9.1C.8.3 Collision between concurrent measurement gaps 1040

9.1C.8.4 Measurement gap related requirements of concurrent measurement gaps 1040

9.1C.9 Collision between SMTC and measurement gap for SAN 1040

9.1C.9.1 Introduction 1040

9.1C.9.2 Collision between SMTCs and measurement gap 1040

9.1C.9.3 Collision between multiple SMTCs on a SAN carrier 1041

9.1D General measurement requirement for ATG 1041

9.1D.1 Introduction 1041

9.1D.2 Measurement gap 1041

9.1D.2.1a SA: Measurement Gap Sharing 1044

9.1D.3 UE Measurement capability 1044

9.1D.3.1 SA: Monitoring of multiple layers using gaps 1044

9.1D.3.2 SA: Maximum allowed layers for multiple monitoring 1044

9.1D.4 Void 1045

9.1D.5 Carrier-specific scaling factor 1045

9.1D.5.1 Monitoring of multiple layers outside gaps 1045

9.1D.5.1.1 Void 1045

9.1D.5.1.2 SA mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3 measurements performed outside gaps 1045

9.1D.5.2 Monitoring of multiple layers within gaps 1046

9.1D.5.2.1 Void 1047

9.1D.5.2.2 SA mode: carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements performed within gaps 1047

9.1D.6 Void 1047

9.1D.7 Pre-configured measurement gap 1047

9.1D.7.1 Introduction 1047

9.1D.7.2 Requirements applicability 1048

9.1D.7.3 Requirements 1048

9.1D.7.3.1 Requirements for autonomous activation/deactivation mechanism 1048

9.1D.7.3.2 Requirements for network-controlled activation/deactivation mechanism 1049

9.1D.7.3.3 Requirements for reception/transmission during activation/deactivation 1049

9.1D.8 Capabilities for Support of Event Triggering and Reporting Criteria 1049

9.1D.8.1 Introduction 1049

9.1D.8.2 Requirements 1050

9.1D.9 Minimum requirement at transitions 1050

9.1E General measurement requirement for RedCap with satellite access 1050

9.1E.1 Introduction 1050

9.1E.2 Measurement gap 1051

9.1E.8 Concurrent measurement gaps for RedCap with SAN 1051

9.1E.8.1 Introduction 1051

9.1E.8.2 Requirements 1051

9.1E.8.3 Collision between concurrent measurement gaps 1051

9.1E.8.4 Measurement gap related requirements of concurrent measurement gaps 1051

9.1E.9 Collision between SMTC and measurement gap for RedCap with satellite access 1051

9.1E.9.1 Introduction 1051

9.1E.9.2 Collision between SMTCs and measurement gap 1051

9.1E.9.3 Collision between multiple SMTCs on a SAN carrier 1052

9.2 NR intra-frequency measurements 1052

9.2.1 Introduction 1052

9.2.2 Requirements applicability 1055

9.2.3 Number of cells and number of SSB 1056

9.2.3.1 Requirements for FR1 1056

9.2.3.2 Requirements for FR2 1056

9.2.4 Measurement Reporting Requirements 1057

9.2.4.1 Periodic Reporting 1057

9.2.4.2 Event-triggered Periodic Reporting 1057

9.2.4.3 Event Triggered Reporting 1057

9.2.4.4 SCell activation Triggered Reporting 1058

9.2.5 Intrafrequency measurements without measurement gaps 1058

9.2.5.1 Intra-frequency cell identification 1058

9.2.5.2 Measurement period 1066

9.2.5.3 Scheduling availability of UE during intra-frequency measurements 1070

9.2.5.3.1 Scheduling availability of UE performing measurements in TDD bands on FR1 1070

9.2.5.3.2 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1 1071

9.2.5.3.3 Scheduling availability of UE performing measurements on FR2 1072

9.2.5.3.4 Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA 1074

9.2.5.4 SFTD Measurements between PCell and PSCell 1074

9.2.5.4.1 Introduction 1074

9.2.5.4.2 SFTD Measurement delay 1074

9.2.5.4.3 SFTD Measurement Reporting Delay 1075

9.2.6 Intra-frequency measurements with measurement gaps 1075

9.2.6.1 Void 1075

9.2.6.2 Intra-frequency cell identification 1075

9.2.6.3 Intra-frequency Measurement Period 1081

9.2.7 Intra-frequency measurements with NCSG 1084

9.2.7.1 Intra-frequency cell identification 1084

9.2.7.2 Measurement period 1086

9.2.7.3 Scheduling availability during intra-frequency measurement with NCSG 1087

9.2A NR intra-frequency measurements with CCA 1087

9.2A.1 Introduction 1087

9.2A.2 Requirements applicability 1088

9.2A.3 Number of cells and number of SSB 1088

9.2A.3.1 Requirements for FR1 1088

9.2A.3.2 Requirements for FR2-2 1088

9.2A.4 Measurement Reporting Requirements 1089

9.2A.5 Intra-frequency measurements without measurement gaps 1089

9.2A.5.2 Measurement period 1094

9.2A.5.3 Scheduling availability of UE during intra-frequency measurements 1096

9.2A.5.3.1 Scheduling availability of UE performing measurements in TDD bands on FR1 1096

9.2A.5.3.2 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1 1097

9.2A.5.3.3 Scheduling availability of UE performing measurements in TDD bands on FR2-2 1097

9.2A.6 Intra-frequency measurements with measurement gaps 1097

9.2A.6.1 Intra-frequency cell identification 1097

9.2A.6.2 Intra-frequency Measurement Period 1099

9.2A.7 Intra-frequency RSSI and Channel occupancy measurements 1100

9.2A.7.1 Intra-frequency RSSI measurements 1100

9.2A.7.2 Intra-frequency Channel occupancy measurements 1102

9.2A.7.3 Scheduling restriction during RSSI and Channel Occupancy measurements in FR1 1104

9.2A.7.4 Scheduling restriction during RSSI measurements in FR2-2 1104

9.2B NR intra-frequency measurements for RedCap 1104

9.2B.1 Introduction 1104

9.2B.2 Requirements applicability 1105

9.2B.3 Number of cells and number of SSB 1105

9.2B.3.1 Requirements for FR1 1105

9.2B.3.2 Requirements for FR2 1105

9.2B.4 Measurement Reporting Requirements 1106

9.2B.4.1 Periodic Reporting 1106

9.2B.4.2 Event-triggered Periodic Reporting 1106

9.2B.4.3 Event Triggered Reporting 1106

9.2B.5 Intra-frequency measurements without measurement gaps 1107

9.2B.5.1 Intra-frequency cell identification 1107

9.2B.5.2 Measurement period 1109

9.2B.5.3 Scheduling availability of UE during intra-frequency measurements 1110

9.2B.5.3.1 Scheduling availability of UE performing measurements in TDD bands on FR1 1110

9.2B.5.3.2 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1 1110

9.2B.5.3.3 Scheduling availability of UE performing measurements on FR2 1111

9.2B.5.3.4 Scheduling availability of HD-FDD UE performing measurements on FR1 1111

9.2B.6 Intra-frequency measurements with measurement gaps 1112

9.2B.6.1 Intra-frequency cell identification 1112

9.2B.6.2 Intra-frequency Measurement Period 1113

9.2C NR intra-frequency measurements for SAN 1114

9.2C.1 Introduction 1114

9.2C.2 Requirements applicability 1115

9.2C.3 Number of cells and number of SSB 1115

9.2C.3.1 Requirements for FR1-NTN 1115

9.2C.4 Measurement Reporting Requirements 1116

9.2C.4.1 Periodic Reporting 1116

9.2C.4.2 Event-triggered Periodic Reporting 1116

9.2C.4.3 Event Triggered Reporting 1116

9.2C.5 Intra-frequency measurements without measurement gaps 1116

9.2C.5.1 Intra-frequency cell identification 1116

9.2C.5.2 Measurement period 1119

9.2C.5.3 Scheduling availability of UE during intra-frequency measurements 1119

9.2C.5.3.1 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1-NTN 1119

9.2C.5.3.2 Scheduling availability of UE performing measurements on a neighbor cell served by a different satellite in LEO 1119

9.2C.6 Intra-frequency measurements with measurement gaps 1120

9.2C.6.1 Void 1120

9.2C.6.2 Intra-frequency cell identification 1120

9.2C.6.3 Intrafrequency Measurement Period 1121

9.2C.7 Intra-frequency measurements without measurement gaps for NTN band above 10 GHz 1122

9.2C.7.1 Intra-frequency cell identification 1122

9.2C.7.2 Measurement period 1123

9.2C.7.3 Scheduling availability of UE during intra-frequency measurements 1124

9.2C.7.3.1 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on NTN bands above 10 GHz 1124

9.2C.8 Intra-frequency measurements with measurement gaps for NTN band above 10 GHz 1124

9.2C.8.1 Intra-frequency cell identification 1124

9.2C.8.3 Intra-frequency Measurement Period 1125

9.2D NR intra-frequency measurements for ATG 1125

9.2D.1 Introduction 1125

9.2D.2 Requirements applicability 1126

9.2D.3 Number of cells and number of SSB 1126

9.2D.3.1 Requirements for FR1 1126

9.2D.4 Measurement Reporting Requirements 1127

9.2D.4.1 Periodic Reporting 1127

9.2D.4.2 Event-triggered Periodic Reporting 1127

9.2D.4.3 Event Triggered Reporting 1127

9.2D.4.4 SCell activation Triggered Reporting 1127

9.2D.5 Intra-frequency measurements without measurement gaps 1128

9.2D.5.1 Intra-frequency cell identification 1128

9.2D.5.2 Measurement period 1131

9.2D.5.3 Scheduling availability of UE during intra-frequency measurements 1132

9.2D.5.3.1 Scheduling availability of UE performing measurements on FR1 1132

9.2D.5.3.2 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1 1134

9.2D.6 Intra-frequency measurements with measurement gaps 1134

9.2D.6.1 Void 1134

9.2D.6.2 Intra-frequency cell identification 1134

9.2D.6.3 Intra-frequency Measurement Period 1135

9.2E NR intra-frequency measurements for RedCap with SAN 1136

9.2E.1 Introduction 1136

9.2E.2 Requirements applicability 1136

9.2E.3 Number of cells and number of SSB 1137

9.2E.3.1 Requirements for FR1 1137

9.2E.4 Measurement Reporting Requirements 1137

9.2E.4.1 Periodic Reporting 1137

9.2E.4.2 Event-triggered Periodic Reporting 1137

9.2E.4.3 Event Triggered Reporting 1137

9.2E.5 Intra-frequency measurements without measurement gaps 1137

9.2E.5.1 Intra-frequency cell identification 1137

9.2E.5.2 Measurement period 1138

9.2E.5.3 Scheduling availability of UE during intra-frequency measurements 1138

9.2E.5.3.1 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1 1138

9.2E.5.3.2 Scheduling availability of UE performing measurements on a neighbor cell served by a different satellite in LEO 1138

9.2E.5.3.4 Scheduling availability of UE performing measurements in HD-FDD bands on FR1 1138

9.2E.6 Intra-frequency measurements with measurement gaps 1138

9.2E.6.1 Intra-frequency cell identification 1138

9.2E.6.2 Intra-frequency Measurement Period 1139

9.3 NR inter-frequency measurements 1139

9.3.1 Introduction 1139

9.3.2 Requirements applicability 1142

9.3.2.1 Void 1143

9.3.2.2 Void 1143

9.3.3 Number of cells and number of SSB 1143

9.3.3.1 Requirements for FR1 1143

9.3.3.2 Requirements for FR2 1143

9.3.4 Inter-frequency measurement with measurement gaps 1143

9.3.4.1 Void 1149

9.3.4.2 Void 1149

9.3.5 Inter-frequency measurements 1149

9.3.5.1 Void 1152

9.3.5.2 Void 1152

9.3.5.3 Void 1152

9.3.6 Inter-frequency measurements reporting requirements 1152

9.3.6.1 Periodic Reporting 1152

9.3.6.2 Event-triggered Periodic Reporting 1152

9.3.6.3 Event-triggered Reporting 1152

9.3.7 Void 1153

9.3.8 Inter-frequency SFTD measurement requirements 1153

9.3.8.1 Introduction 1153

9.3.8.2 SFTD Measurement delay 1153

9.3.8.3 SFTD Measurement reporting delay 1154

9.3.9 Inter-frequency measurements without measurement gaps 1154

9.3.9.1 Inter-frequency Cell identification 1154

9.3.9.2 Measurement period 1159

9.3.9.3 Scheduling availability of UE during inter-frequency measurements when the SSB is completely contained in the active BWP of the UE 1161

9.3.9.3.1 Scheduling availability of UE performing measurements in TDD bands on FR1 1162

9.3.9.3.2 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1 1163

9.3.9.3.3 Scheduling availability of UE performing measurements on FR2 1164

9.3.9.3.4 Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA 1164

9.3.9.4 Scheduling availability of UE during inter-frequency measurements when the SSB is not completely contained in the active BWP of the UE 1164

9.3.9.4.1 Scheduling availability of UE performing measurements in TDD bands on FR1 1165

9.3.9.4.2 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1 1165

9.3.9.4.3 Scheduling availability of UE performing measurements on FR2 1166

9.3.9.4.4 Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA 1167

9.3.10 Inter-frequency measurement with NCSG 1168

9.3.10.1 Inter-frequency cell identification 1168

9.3.10.2 Measurement period 1170

9.3.10.3 Scheduling availability during inter-frequency measurement with NCSG 1170

9.3.10.3.1 Scheduling availability of UE performing measurements in TDD bands on FR1 1170

9.3.10.3.2 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1 1171

9.3.10.3.3 Scheduling availability of UE performing measurements on FR2 1171

9.3.10.3.4 Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA 1173

9.3A NR inter-frequency measurements in carrier frequencies with CCA 1173

9.3A.1 Introduction 1173

9.3A.2 Requirements applicability 1174

9.3A.3 Number of cells and number of SSB 1174

9.3A.3.1 Requirements for FR1 1174

9.3A.3.2 Requirements for FR2-2 1174

9.3A.4 Inter-frequency cell identification 1175

9.3A.5 Inter-frequency measurements 1177

9.3A.6 Inter-frequency measurements reporting requirements 1178

9.3A.6.1 Periodic Reporting 1178

9.3A.6.2 Event-triggered Periodic Reporting 1178

9.3A.6.3 Event-triggered Reporting 1178

9.3A.8 Inter-frequency RSSI measurements 1179

9.3A.9 Inter-frequency channel occupancy measurements 1180

9.3B NR inter-frequency measurements for RedCap 1180

9.3B.1 Introduction 1180

9.3B.2 Requirements applicability 1181

9.3B.3 Number of cells and number of SSB 1181

9.3B.3.1 Requirements for FR1 1181

9.3B.3.2 Requirements for FR2 1181

9.3B.4 Inter-frequency measurement with measurement gaps 1181

9.3B.5 Inter-frequency measurements 1183

9.3B.6 Inter-frequency measurements reporting requirements 1184

9.3B.6.1 Periodic Reporting 1184

9.3B.6.2 Event-triggered Periodic Reporting 1184

9.3B.6.3 Event-triggered Reporting 1184

9.3B.7 Inter-frequency measurements without measurement gaps 1184

9.3B.7.1 Inter-frequency Cell identification 1184

9.3B.7.2 Measurement period 1186

9.3B.7.3 Scheduling availability of UE during inter-frequency measurements 1187

9.3B.7.3.1 Scheduling availability of UE performing measurements in TDD bands on FR1 1187

9.3B.7.3.2 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1 1188

9.3B.7.3.3 Scheduling availability of UE performing measurements on FR2 1188

9.3B.7.3.4 Scheduling availability of HD-FDD UE performing measurements on FR1 1188

9.3C NR inter-frequency measurements for SAN 1189

9.3C.1 Introduction 1189

9.3C.2 Requirements applicability 1190

9.3C.3 Number of cells and number of SSB 1190

9.3C.3.1 Requirements for FR1-NTN 1190

9.3C.4 Inter-frequency measurement with measurement gaps 1190

9.3C.5 Inter-frequency measurements 1192

9.3C.6 Inter-frequency measurements reporting requirements 1192

9.3C.6.1 Periodic Reporting 1192

9.3C.6.2 Event-triggered Periodic Reporting 1193

9.3C.6.3 Event-triggered Reporting 1193

9.3C.7 Inter-frequency measurements without measurement gaps 1193

9.3C.7.1 Inter-frequency Cell identification 1193

9.3C.7.2 Measurement period 1195

9.3C.7.3 Scheduling availability of UE during inter-frequency measurements 1195

9.3C.7.3.1 Void 1196

9.3C.7.3.2 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1-NTN 1196

9.3C.7.3.3 Scheduling availability of UE performing measurements on a neighbor cell served by a different satellite in LEO 1196

9.3C.8 Inter-frequency measurement with measurement gaps for NTN band above 10 GHz 1196

9.3C.9 Inter-frequency measurements for NTN band above 10 GHz 1197

9.3C.10 Inter-frequency measurements without measurement gaps for NTN band above 10 GHz 1197

9.3C.10.1 Inter-frequency Cell identification 1197

9.3C.10.2 Measurement period 1199

9.3C.10.3 Scheduling availability of UE during inter-frequency measurements 1199

9.3C.10.3.1 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on NTN bands above 10 GHz 1199

9.3D NR inter-frequency measurements for ATG 1199

9.3D.1 Introduction 1199

9.3D.2 Requirements applicability 1200

9.3D.3 Number of cells and number of SSB 1201

9.3D.3.1 Requirements for FR1 1201

9.3D.4 Inter-frequency measurement with measurement gaps 1201

9.3D.5 Inter-frequency measurements 1202

9.3D.6 Inter-frequency measurements reporting requirements 1202

9.3D.6.1 Periodic Reporting 1202

9.3D.6.2 Event-triggered Periodic Reporting 1203

9.3D.6.3 Event-triggered Reporting 1203

9.3D.7 Void 1203

9.3D.8 Void 1203

9.3D.9 Inter-frequency measurements without measurement gaps 1203

9.3D.9.1 Inter-frequency Cell identification 1203

9.3D.9.2 Measurement period 1205

9.3D.9.3 Scheduling availability of UE during inter-frequency measurements 1205

9.3D.9.3.1 Scheduling availability of UE performing measurements on FR1 1206

9.3D.9.3.2 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1 1207

9.3E NR inter-frequency measurements for Redcap UEs with satellite access 1207

9.3E.1 Introduction 1207

9.3E.2 Requirements applicability 1207

9.3E.3 Number of cells and number of SSB 1208

9.3E.3.1 Requirements for FR1 1208

9.3E.4 Inter-frequency measurement with measurement gaps 1208

9.3E.5 Inter-frequency measurements 1209

9.3E.6 Inter-frequency measurements reporting requirements 1209

9.3E.6.1 Periodic Reporting 1209

9.3E.6.2 Event-triggered Periodic Reporting 1210

9.3E.6.3 Event-triggered Reporting 1210

9.3E.7 Inter-frequency measurements without measurement gaps 1210

9.3E.7.1 Inter-frequency Cell identification 1210

9.3E.7.2 Measurement period 1211

9.3E.7.3 Scheduling availability of UE during inter-frequency measurements 1211

9.3E.7.3.1 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1 1211

9.3E.7.3.2 Scheduling availability of UE performing measurements in HD-FDD bands on FR1 1211

9.4 Inter-RAT measurements 1212

9.4.1 Introduction 1212

9.4.2 NR − E-UTRAN FDD measurements 1214

9.4.2.1 Introduction 1214

9.4.2.2 Requirements when no DRX is used 1214

9.4.2.3 Requirements when DRX is used 1216

9.4.2.4 Measurement reporting requirements 1218

9.4.2.4.1 Periodic Reporting 1218

9.4.2.4.2 Event-Triggered Periodic Reporting 1218

9.4.2.4.3 Event-Triggered Reporting 1219

9.4.2.5 Scheduling Availability During NR − E-UTRAN FDD measurements with NCSG 1219

9.4.3 NR − E-UTRAN TDD measurements 1219

9.4.3.1 Introduction 1219

9.4.3.2 Requirements when no DRX is used 1219

9.4.3.3 Requirements when DRX is used 1222

9.4.3.4 Measurement reporting requirements 1224

9.4.3.4.1 Periodic Reporting 1224

9.4.3.4.2 Event-Triggered Periodic Reporting 1224

9.4.3.4.3 Event-Triggered Reporting 1225

9.4.3.5 Scheduling Availability During NR − E-UTRAN TDD measurements with NCSG 1225

9.4.4 Inter-RAT RSTD measurements 1225

9.4.4.1 NR − E-UTRAN FDD RSTD measurements 1225

9.4.4.1.1 Introduction 1225

9.4.4.1.2 Requirements 1226

9.4.4.2 NR − E-UTRAN TDD RSTD measurements 1228

9.4.4.2.1 Introduction 1228

9.4.4.2.2 Requirements 1229

9.4.5 Inter-RAT E-CID measurements 1232

9.4.5.1 NR−E-UTRAN FDD E-CID RSRP and RSRQ measurements 1232

9.4.5.1.1 Introduction 1232

9.4.5.1.2 Requirements 1232

9.4.5.1.3 Measurement Reporting Delay 1232

9.4.5.2 NR−E-UTRAN TDD E-CID RSRP and RSRQ measurements 1233

9.4.5.2.1 Introduction 1233

9.4.5.2.2 Requirements 1233

9.4.5.2.3 Measurement Reporting Delay 1233

9.4.6 NR − UTRAN FDD measurements 1233

9.4.6.1 Introduction 1233

9.4.6.2 Requirements when no DRX is used 1233

9.4.6.3 Requirements when DRX is used 1234

9.4.7 NR – E-UTRAN measurements with autonomous gaps 1236

9.4.7.1 CGI identification of an E-UTRA cell with autonomous gaps 1236

9.4.7.2 CGI reporting delay 1236

9.4.8 NR – E-UTRAN measurements without measurement gaps 1237

9.4.8.1 Introduction 1237

9.4.8.2 General requirements 1237

9.4.8.3 NR − E-UTRAN FDD measurements 1238

9.4.8.3.1 Introduction 1238

9.4.8.3.2 Requirements when no DRX is used 1238

9.4.8.3.3 Requirements when DRX is used 1239

9.4.8.3.4 Measurement reporting requirements 1240

9.4.8.3.5 Scheduling availability during NR − E-UTRAN FDD measurements 1240

9.4.8.4 NR − E-UTRAN TDD measurements 1240

9.4.8.4.1 Introduction 1240

9.4.8.4.2 Requirements when no DRX is used 1241

9.4.8.4.3 Requirements when DRX is used 1242

9.4.8.4.4 Measurement reporting requirements 1243

9.4.8.4.5 Scheduling availability during NR − E-UTRAN TDD measurements 1243

9.4A Inter-RAT measurements for RedCap 1244

9.4A.1 Introduction 1244

9.4A.2 NR − E-UTRAN FDD measurements 1245

9.4A.2.1 Introduction 1245

9.4A.2.2 Requirements when no DRX is used 1246

9.4A.2.3 Requirements when DRX is used 1247

9.4A.2.4 Measurement reporting requirements 1248

9.4A.2.4.1 Periodic Reporting 1248

9.4A.2.4.2 Event-Triggered Periodic Reporting 1248

9.4A.2.4.3 Event-Triggered Reporting 1248

9.4A.3 NR − E-UTRAN TDD measurements 1248

9.4A.3.1 Introduction 1248

9.4A.3.2 Requirements when no DRX is used 1249

9.4A.3.3 Requirements when DRX is used 1250

9.4A.3.4 Measurement reporting requirements 1251

9.4A.3.4.1 Periodic Reporting 1251

9.4A.3.4.2 Event-Triggered Periodic Reporting 1251

9.4A.3.4.3 Event-Triggered Reporting 1252

9.4A.4 NR – E-UTRAN measurements with autonomous gaps 1252

9.4A.4.1 CGI identification of an E-UTRA cell with autonomous gaps 1252

9.4A.4.2 CGI reporting delay 1253

9.4A.4.3 CGI reporting scheduling restriction 1253

9.5 L1-RSRP measurements for Reporting 1253

9.5.1 Introduction 1253

9.5.2 Requirements applicability 1254

9.5.3 Measurement Reporting Requirements 1255

9.5.3.1 Periodic Reporting 1255

9.5.3.2 Semi-Persistent Reporting 1255

9.5.3.3 Aperiodic Reporting 1256

9.5.3.4 Event Triggered Reporting for the UE initiated beam management 1256

9.5.4 L1-RSRP measurement requirements 1257

9.5.4.1 SSB based L1-RSRP Reporting 1257

9.5.4.2 CSI-RS based L1-RSRP Reporting 1264

9.5.4A Void 1268

9.5.4A.1 Void 1268

9.5.5 Measurement restriction for CSI-RS and SSB for L1-RSRP measurement 1268

9.5.5.1 Measurement restriction for SSB based L1-RSRP 1269

9.5.5.2 Measurement restriction for CSI-RS based L1-RSRP 1269

9.5.6 Scheduling availability of UE during L1-RSRP measurement 1271

9.5.6.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 1271

9.5.6.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 1271

9.5.6.3 Scheduling availability of UE performing L1-RSRP measurement on FR2 1272

9.5.6.4 Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA 1274

9.5.7 Minimum requirement at transitions 1274

9.5A L1-RSRP measurements for Reporting under CCA 1275

9.5A.1 Introduction 1275

9.5A.2 Requirements applicability 1275

9.5A.3 Measurement Reporting Requirements 1275

9.5A.3.1 Periodic Reporting 1276

9.5A.3.2 Semi-Persistent Reporting 1276

9.5A.3.3 Aperiodic Reporting 1276

9.5A.4 L1-RSRP measurement requirements 1276

9.5A.4.1 SSB based L1-RSRP Reporting 1276

9.5A.5 Measurement restriction for L1-RSRP measurement 1279

9.5A.5.1 Measurement restriction for SSB based L1-RSRP 1279

9.5A.6 Scheduling availability of UE during L1-RSRP measurement 1280

9.5A.6.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 1280

9.5A.6.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 1280

9.5A.6.3 Void 1280

9.5A.6.3A Scheduling availability of UE performing L1-RSRP measurement in case of FR1-FR2 inter-band CA 1280

9.5A.6.3B Scheduling availability of UE performing L1-RSRP measurement on FR2-2 1280

9.5A.6.4 Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA 1281

9.5B L1-RSRP measurements for Reporting for RedCap 1281

9.5B.1 Introduction 1281

9.5B.2 Requirements applicability 1281

9.5B.3 Measurement Reporting Requirements 1282

9.5B.3.1 Periodic Reporting 1282

9.5B.3.2 Semi-Persistent Reporting 1282

9.5B.3.3 Aperiodic Reporting 1283

9.5B.4 L1-RSRP measurement requirements 1283

9.5B.4.1 SSB based L1-RSRP Reporting 1283

9.5B.4.2 CSI-RS based L1-RSRP Reporting 1285

9.5B.5 Measurement restriction for CSI-RS and SSB for L1-RSRP measurement 1288

9.5B.5.1 Measurement restriction for SSB based L1-RSRP 1288

9.5B.5.2 Measurement restriction for CSI-RS based L1-RSRP 1288

9.5B.6 Scheduling availability of UE during L1-RSRP measurement 1288

9.5B.6.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 1289

9.5B.6.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 1289

9.5B.6.3 Scheduling availability of UE performing L1-RSRP measurement on FR2 1289

9.5C L1-RSRP measurements for Reporting for satellite access 1290

9.5C.1 Introduction 1290

9.5C.3 Measurement Reporting Requirements 1290

9.5C.3.1 Periodic Reporting 1291

9.5C.3.2 Semi-Persistent Reporting 1291

9.5C.3.3 Aperiodic Reporting 1291

9.5C.4 L1-RSRP measurement requirements 1291

9.5C.4.1 SSB based L1-RSRP Reporting 1291

9.5C.5 Measurement restriction for L1-RSRP measurement 1293

9.5C.5.1 Measurement restriction for SSB based L1-RSRP 1293

9.5C.5.2 Measurement restriction for CSI-RS based L1-RSRP 1293

9.5C.6 Scheduling availability of UE during L1-RSRP measurement 1294

9.5C.6.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1-NTN 1294

9.5C.6.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1-NTN 1294

9.5C.7 L1-RSRP measurement requirements for NTN band above 10 GHz 1294

9.5C.7.1 SSB based L1-RSRP Reporting 1294

9.5C.7.2 CSI-RS based L1-RSRP Reporting 1295

9.5C.8 Measurement restriction for L1-RSRP measurement for NTN band above 10 GHz 1296

9.5C.8.1 Measurement restriction for SSB based L1-RSRP 1296

9.5C.8.2 Measurement restriction for CSI-RS based L1-RSRP 1296

9.5C.9 Scheduling availability of UE during L1-RSRP measurement for NTN band above 10 GHz 1297

9.5C.9.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on NTN bands above 10 GHz 1297

9.5C.9.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on NTN bands above 10 GHz 1297

9.5D L1-RSRP measurements for Reporting for ATG 1297

9.5D.1 Introduction 1297

9.5D.2 Requirements applicability 1297

9.5D.3 Measurement Reporting Requirements 1298

9.5D.3.1 Periodic Reporting 1298

9.5D.3.2 Semi-Persistent Reporting 1298

9.5D.3.3 Aperiodic Reporting 1298

9.5D.4 L1-RSRP measurement requirements 1298

9.5D.4.1 SSB based L1-RSRP Reporting 1298

9.5D.4.2 CSI-RS based L1-RSRP Reporting 1300

9.5D.5 Measurement restriction for CSI-RS and SSB for L1-RSRP measurement 1302

9.5D.5.1 Measurement restriction for SSB based L1-RSRP 1302

9.5D.5.2 Measurement restriction for CSI-RS based L1-RSRP 1302

9.5D.6 Scheduling availability of UE during L1-RSRP measurement 1303

9.5D.6.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 1303

9.5D.6.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 1303

9.5E L1-RSRP measurements for Reporting for RedCap UEs with satellite access 1303

9.5E.1 Introduction 1303

9.5E.2 Requirements applicability 1303

9.5E.3 Measurement Reporting Requirements 1304

9.5E.3.1 Periodic Reporting 1304

9.5E.3.2 Semi-Persistent Reporting 1304

9.5E.3.3 Aperiodic Reporting 1305

9.5E.4 L1-RSRP measurement requirements 1305

9.5E.4.1 SSB based L1-RSRP Reporting 1305

9.5E.4.2 CSI-RS based L1-RSRP Reporting 1305

9.5E.5 Measurement restriction for L1-RSRP measurement 1305

9.5E.6 Scheduling availability of UE during L1-RSRP measurement 1305

9.5E.6.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 1305

9.5E.6.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 1306

9.5F L1-RSRP measurements Reporting for Beam Prediction 1306

9.5F.1 Introduction 1306

9.5F.2 Requirements applicability 1306

9.5F.3 Measurement Reporting Requirements 1307

9.5F.3.1 Periodic Reporting 1307

9.5F.3.2 Semi-Persistent Reporting 1307

9.5F.3.3 Aperiodic Reporting 1307

9.5F.4 L1-RSRP measurement and prediction requirements 1308

9.5F.4.1 SSB based RS prediction reporting 1308

9.5F.4.2 CSI-RS based RS prediction reporting 1309

9.6 NE-DC: Measurements 1311

9.6.1 Introduction 1311

9.6.2 SFTD Measurements 1312

9.6.2.1 Introduction 1312

9.6.2.2 SFTD Measurement requirements 1312

9.7 Cross Link Interference measurements 1312

9.7.1 Introduction 1312

9.7.2 SRS-RSRP measurements 1313

9.7.2.1 Introduction 1313

9.7.2.2 Requirements applicability 1313

9.7.2.3 Measurement Reporting Requirements 1313

9.7.2.3.1 Periodic Reporting 1313

9.7.2.3.2 Event-triggered Periodic Reporting 1313

9.7.2.3.3 Event Triggered Reporting 1313

9.7.2.4 Measurement capability 1314

9.7.2.5 SRS-RSRP measurement period 1314

9.7.3 CLI-RSSI measurements 1314

9.7.3.1 Introduction 1314

9.7.3.2 Requirements applicability 1314

9.7.3.3 Measurement Reporting Requirements 1314

9.7.3.3.1 Periodic Reporting 1315

9.7.3.3.2 Event-triggered Periodic Reporting 1315

9.7.3.3.3 Event Triggered Reporting 1315

9.7.3.4 Measurement capability 1315

9.7.3.5 CLI-RSSI measurement period 1315

9.7.4 Scheduling availability of UE during CLI measurements 1315

9.7.4.1 Scheduling availability of UE performing measurement on FR1 1315

9.7.4.2 Scheduling availability of UE performing measurement on FR2 1316

9.8 L1-SINR measurements for Reporting 1317

9.8.1 Introduction 1317

9.8.2 Requirements applicability 1318

9.8.3 Measurement Reporting Requirements 1319

9.8.3.1 Periodic Reporting 1319

9.8.3.2 Semi-Persistent Reporting 1319

9.8.4 L1-SINR measurement requirements 1319

9.8.4.1 L1-SINR reporting with CSI-RS based CMR and no dedicated IMR configured 1319

9.8.4.2 L1-SINR reporting with SSB based CMR and dedicated IMR configured 1324

9.8.4.3 L1-SINR reporting with CSI-RS based CMR and dedicated IMR configured 1326

9.8.5 Measurement restriction for L1-SINR measurement 1329

9.8.5.1 Measurement restriction if SSB configured for L1-SINR Measurement 1329

9.8.5.2 Measurement restriction if CSI-RS configured for L1-SINR measurement 1330

9.8.5.3 Measurement restriction if CSI-IM configured for L1-SINR measurement 1331

9.8.6 Scheduling availability of UE during L1-SINR measurement 1332

9.8.6.1 Scheduling availability of UE performing L1-SINR measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 1332

9.8.6.2 Scheduling availability of UE performing L1-SINR measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 1332

9.8.6.4 Scheduling availability of UE performing L1-SINR measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA 1334

9.8.7 Minimum requirement at transitions 1334

9.8D L1-SINR measurements for Reporting for ATG 1334

9.8D.1 Introduction 1334

9.8D.2 Requirements applicability 1335

9.8D.3 Measurement Reporting Requirements 1335

9.8D.3.1 Periodic Reporting 1336

9.8D.3.2 Semi-Persistent Reporting 1336

9.8D.3.3 Aperiodic Reporting 1336

9.8D.4 L1-SINR measurement requirements 1336

9.8D.4.1 L1-SINR reporting with CSI-RS based CMR and no dedicated IMR configured 1336

9.8D.4.2 L1-SINR reporting with SSB based CMR and dedicated IMR configured 1338

9.8D.4.3 L1-SINR reporting with CSI-RS based CMR and dedicated IMR configured 1339

9.8D.5 Measurement restriction for L1-SINR measurement 1340

9.8D.5.1 Measurement restriction if SSB configured for L1-SINR Measurement 1340

9.8D.5.2 Measurement restriction if CSI-RS configured for L1-SINR measurement 1340

9.8D.5.3 Measurement restriction if CSI-IM configured for L1-SINR measurement 1341

9.8D.6 Scheduling availability of UE during L1-SINR measurement 1341

9.8D.6.1 Scheduling availability of UE performing L1-SINR measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 1341

9.8D.6.2 Scheduling availability of UE performing L1-SINR measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 1341

9.9 NR measurements for positioning 1341

9.9.1 Introduction 1341

9.9.1.1 General Aspects of Gap-based Measurement 1341

9.9.1.2 General Aspects of Gapless Measurement 1342

9.9.1.3 Scheduling Availability of UE during PRS Measurement without Measurement Gaps 1343

9.9.2 RSTD measurements 1344

9.9.2.1 Introduction 1344

9.9.2.2 Requirements Applicability 1344

9.9.2.3 Measurement Capability 1345

9.9.2.4 Measurement Reporting Requirements 1345

9.9.2.4.1 Void 1345

9.9.2.4.2 Void 1345

9.9.2.4.3 Void 1345

9.9.2.5 Measurements Period Requirements 1345

9.9.2.6 Void 1348

9.9.2.7 Measurements Period Requirements without Measurement Gaps 1348

9.9.2.8 Void 1351

9.9.2.9 Measurements Period Requirements with both MG and PPW 1351

9.9.2.10 Measurements Period Requirements with Bandwidth Aggregation 1352

9.9.3 PRS-RSRP measurements 1355

9.9.3.1 Introduction 1355

9.9.3.2 Requirements applicability 1355

9.9.3.3 Measurement Capability 1355

9.9.3.4 Measurement Reporting Requirements 1356

9.9.3.5 Measurement Period Requirements 1356

9.9.3.6 Measurement Period Requirements without Measurement Gaps 1358

9.9.3.7 Void 1361

9.9.3.8 Measurements Period Requirements with both MG and PPW 1361

9.9.4 UE Rx-Tx time difference measurements 1361

9.9.4.1 Introduction 1361

9.9.4.2 Requirements Applicability 1362

9.9.4.3 Measurement Capability 1362

9.9.4.4 Measurement Reporting Requirements 1362

9.9.4.5 Measurement Period Requirements 1362

9.9.4.6 Measurement Period Requirements without Measurement Gaps 1366

9.9.4.7 Void 1369

9.9.4.8 Measurements Period Requirements with both MG and PPW 1369

9.9.4.9 Measurements Period Requirements with Bandwidth Aggregation 1369

9.9.5 E-CID measurements 1374

9.9.5.1 Introduction 1374

9.9.5.2 Measurement Requirements 1374

9.9.5.2.1 Intra-frequency Measurement Requirements 1374

9.9.5.2.2 Inter-frequency Measurement Requirements 1374

9.9.5.2.3 Measurement Reporting Delay 1374

9.9.6 PRS-RSRPP measurements 1375

9.9.6.1 Introduction 1375

9.9.6.2 Requirements applicability 1375

9.9.6.3 Measurement capability 1375

9.9.6.4 Measurement reporting requirements 1375

9.9.6.5 Measurement period requirements 1375

9.9.6.6 Measurement Period Requirements without Measurement Gaps 1375

9.9.6.7 Void 1376

9.9.6.8 Measurements Period Requirements with both MG and PPW 1376

9.9.7 Measurement requirements for DL RSCPD reported with RSTD 1376

9.9.7.1 Introduction 1376

9.9.7.2 Requirements Applicability 1376

9.9.7.3 Measurement Capability 1376

9.9.7.4 Measurement Reporting Requirements 1376

9.9.7.5 Measurements Period Requirements for DL RSCPD reported with RSTD 1376

9.9.8 Measurement requirements for DL RSCP reported with UE Rx-Tx time difference 1379

9.9.8.1 Introduction 1379

9.9.8.2 Requirements Applicability 1379

9.9.8.3 Measurement Capability 1380

9.9.8.4 Measurement Reporting Requirements 1380

9.9.8.5 Measurement Period Requirements for DL RSCP and UE Rx-Tx time difference 1380

9.9A NR measurements for positioning for RedCap 1384

9.9A.1 Introduction 1384

9.9A.1.1 General Aspects of Gap-based Measurement 1384

9.9A.1.2 General Aspects of Gapless Measurement for RedCap positioning without FH 1385

9.9A.1.3 Scheduling Availability of UE during PRS Measurement without Measurement Gaps for RedCap positioning without FH 1386

9.9A.2 RSTD measurements for RedCap 1387

9.9A.2.1 Introduction 1387

9.9A.2.2 Requirements Applicability 1387

9.9A.2.3 Measurement Capability 1387

9.9A.2.4 Measurement Reporting Requirements 1387

9.9A.2.5 Measurements Period Requirements without FH 1387

9.9A.2.5.1 Measurements Period Requirements without FH with MG 1387

9.9A.2.5.2 Measurements Period Requirements without FH without MG 1390

9.9A.2.5.3 Measurements Period Requirements without FH with both MG and PPW 1393

9.9A.2.6 Measurements Period Requirements with FH 1394

9.9A.2.6.1 Measurements Period Requirements with FH with MG 1394

9.9A.3 PRS-RSRP measurements for RedCap 1396

9.9A.3.1 Introduction 1396

9.9A.3.2 Requirements applicability 1396

9.9A.3.3 Measurement Capability 1396

9.9A.3.4 Measurement Reporting Requirements 1396

9.9A.3.5 Measurements Period Requirements without FH 1396

9.9A.3.5.1 Measurement Period Requirements without FH with MG 1396

9.9A.3.5.2 Measurement Period Requirements without FH without MG 1399

9.9A.3.5.3 Measurements Period Requirements without FH with both MG and PPW 1401

9.9A.3.6 Measurements Period Requirements with FH 1402

9.9A.3.6.1 Measurements Period Requirements with FH with MG 1402

9.9A.4 UE Rx-Tx time difference measurements for RedCap 1404

9.9A.4.1 Introduction 1404

9.9A.4.2 Requirements Applicability 1404

9.9A.4.3 Measurement Capability 1404

9.9A.4.4 Measurement Reporting Requirements 1404

9.9A.4.5 Measurement Period Requirements without FH with MG 1404

9.9A.4.6 Measurement Period Requirements without FH without MG 1404

9.9A.4.7 Measurements Period Requirements without FH with both MG and PPW 1404

9.9A.4.8 Measurements Period Requirements with FH 1404

9.9A.5 PRS-RSRPP measurements for RedCap 1406

9.9A.5.1 Introduction 1406

9.9A.5.2 Requirements Applicability 1406

9.9A.5.3 Measurement Capability 1406

9.9A.5.4 Measurement Reporting Requirements 1407

9.9A.5.5 Measurement Period Requirements without FH with MG 1407

9.9A.5.6 Measurement Period Requirements without FH without MG 1407

9.9A.5.7 Measurements Period Requirements without FH with both MG and PPW 1407

9.9A.5.8 Measurements Period Requirements with FH 1407

9.9C NR measurements for positioning in Satellite Access 1407

9.9C.1 Introduction 1407

9.9C.1.1 General Aspects of Gap-based Measurement 1407

9.9C.1.2 General Aspects of Gapless Measurement 1408

9.9C.1.3 Scheduling Availability of UE during PRS Measurement without Measurement Gaps 1409

9.9C.2 Void 1409

9.9C.3 Void 1409

9.9C.4 UE Rx-Tx time difference measurements 1409

9.9C.4.1 Introduction 1409

9.9C.4.2 Requirements Applicability 1409

9.9C.4.3 Measurement Capability 1409

9.9C.4.4 Measurement Reporting Requirements 1409

9.9C.4.5 Measurement Period Requirements 1409

9.9C.4.6 Measurement Period Requirements without Measurement Gaps 1412

9.9D NR measurements for positioning for RedCap in Satellite Access 1414

9.9D.1 Introduction 1414

9.9D.1.1 General Aspects of Gap-based Measurement 1414

9.9D.1.2 General Aspects of Gapless Measurement 1414

9.9D.1.3 Scheduling Availability of UE during PRS Measurement without Measurement Gaps 1414

9.9D.2 Void 1415

9.9D.3 Void 1415

9.9D.4 UE Rx-Tx time difference measurements 1415

9.9D.4.1 Introduction 1415

9.9D.4.2 Requirements Applicability 1415

9.9D.4.3 Measurement Capability 1415

9.9D.4.4 Measurement Reporting Requirements 1415

9.9D.4.5 Measurement Period Requirements 1415

9.9D.4.6 Measurement Period Requirements without Measurement Gaps 1416

9.9E Reporting Delay Requirements for DL AI/ML Positioning 1416

9.9E.1 Introduction 1416

9.9E.2 General Aspects Relating to Gap-based Measurement 1416

9.9E.3 General Aspects Relating to Gapless Measurement 1417

9.9E.4 Scheduling Availability Relating to Gapless Measurement 1418

9.9E.5 Measurement Delay Requirement with Measurement Gaps 1418

9.9E.6 Measurement Delay Requirement without Measurement Gaps 1420

9.9E.7 Measurement Delay Requirement with Bandwidth Aggregation 1422

9.10 CSI-RS based L3 measurements 1426

9.10.1 Introduction 1426

9.10.2 CSI-RS based intra-frequency measurements 1426

9.10.2.1 Introduction 1426

9.10.2.2 Requirements applicability 1427

9.10.2.3 Number of cells and number of CSI-RS 1428

9.10.2.3.1 Requirements for FR1 1428

9.10.2.3.2 Requirements for FR2 1428

9.10.2.4 Measurement Reporting Requirements 1428

9.10.2.4.1 Periodic Reporting 1428

9.10.2.4.2 Event-triggered Periodic Reporting 1428

9.10.2.4.3 Event Triggered Reporting 1429

9.10.2.5 Intra-frequency measurements without measurement gaps 1429

9.10.2.6 Scheduling availability of UE during CSI-RS based intra-frequency measurements 1431

9.10.2.6.1 Scheduling availability of UE performing CSI-RS based measurements in TDD bands 1431

9.10.2.6.2 Scheduling availability of UE performing CSI-RS based measurements in FR2 1432

9.10.3 CSI-RS based Inter-frequency measurements 1432

9.10.3.1 Introduction 1432

9.10.3.2 Requirements applicability 1432

9.10.3.3 Number of cells and number of CSI-RS resources 1433

9.10.3.3.1 Requirements for FR1 1433

9.10.3.3.2 Requirements for FR2 1433

9.10.3.4 Measurements reporting requirements 1433

9.10.3.4.1 Periodic Reporting 1433

9.10.3.4.2 Event-triggered Periodic Reporting 1433

9.10.3.4.3 Event-triggered Reporting 1434

9.10.3.5 Inter-frequency measurements with measurement gaps 1434

9.10D CSI-RS based L3 measurements for ATG 1436

9.10D.1 Introduction 1436

9.10D.2 CSI-RS based intra-frequency measurements 1436

9.10D.2.1 Introduction 1436

9.10D.2.2 Requirements applicability 1436

9.10D.2.3 Number of cells and number of CSI-RS 1437

9.10D.2.3.1 Requirements for FR1 1437

9.10D.2.4 Measurement Reporting Requirements 1437

9.10D.2.4.1 Periodic Reporting 1438

9.10D.2.4.2 Event-triggered Periodic Reporting 1438

9.10D.2.4.3 Event Triggered Reporting 1438

9.10D.2.5 Intra-frequency measurements without measurement gaps 1438

9.10D.2.6 Scheduling availability of UE during CSI-RS based intra-frequency measurements 1440

9.10D.2.6.1 Scheduling availability of UE performing CSI-RS based measurements on FR1 1441

9.10D.3 CSI-RS based Inter-frequency measurements 1441

9.10D.3.1 Introduction 1441

9.10D.3.2 Requirements applicability 1441

9.10D.3.3 Number of cells and number of CSI-RS resources 1442

9.10D.3.3.1 Requirements for FR1 1442

9.10D.3.4 Measurements reporting requirements 1442

9.10D.3.4.1 Periodic Reporting 1442

9.10D.3.4.2 Event-triggered Periodic Reporting 1442

9.10D.3.4.3 Event-triggered Reporting 1442

9.10D.3.5 Inter-frequency measurements with measurement gaps 1443

9.11 NR measurements with autonomous gaps 1444

9.11.1 Introduction 1444

9.11.2 CGI identification of an NR cell with autonomous gaps 1444

9.11.3 CGI reporting delay 1445

9.11A NR measurements with autonomous gaps for RedCap 1445

9.11A.1 Introduction 1445

9.11A.2 CGI identification of an NR cell with autonomous gaps 1446

9.11A.3 CGI reporting delay 1446

9.11A.4 CGI reporting scheduling restriction 1447

9.11D NR measurements with autonomous gaps for ATG 1447

9.11D.1 Introduction 1447

9.11D.2 CGI identification of an NR cell with autonomous gaps 1448

9.11D.3 CGI reporting delay 1448

9.12 Measurement for Propagation Delay Compensation 1449

9.12.1 Introduction 1449

9.12.2 Requirements Applicability 1449

9.12.3 Measurement Capability 1449

9.12.4 Measurement period requirements 1449

9.12.4.1 PRS Measurement Period 1449

9.12.4.2 TRS Measurement Period 1450

9.12.5 Measurement Reporting Requirements 1451

9.12.6 Scheduling availability during measurement for Propagation Delay Compensation 1451

9.12.7 Measurement restriction for measurement for Propagation Delay Compensation 1451

9.12.8 Measurement requirement for Propagation Delay Compensation with MUSIM gaps 1452

9.13 L1-RSRP measurements for a cell with different PCI from serving cell 1452

9.13.1 Introduction 1452

9.13.2 Requirements Applicability 1452

9.13.3 Measurement Reporting Requirements 1453

9.13.3.1 Periodic Reporting 1453

9.13.3.2 Semi-Persistent Reporting 1453

9.13.3.3 Aperiodic Reporting 1453

9.13.3.4 Event triggered reporting for UE initiated beam management 1454

9.13.4 L1-RSRP measurement requirements 1455

9.13.4.1 Inter-cell SSB based L1-RSRP Reporting 1455

9.13.5 Measurement restriction for L1-RSRP measurement 1458

9.13.5.1 Measurement restriction for SSB based L1-RSRP 1458

9.13.6 Scheduling availability of UE during L1-RSRP measurement 1459

9.13.6.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 1459

9.13.6.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 1459

9.13.6.3 Scheduling availability of UE performing L1-RSRP measurement on FR2 1460

9.13.6.4 Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA 1461

9.13.6.5 Scheduling availability of UE performing L1-RSRP measurement in TDD bands on FR1 1461

9.14 NR intra-frequency L1-RSRP measurements for neighbor cell 1461

9.14.1 Introduction 1461

9.14.2 Requirements Applicability 1461

9.14.3 Measurement Reporting Requirements 1462

9.14.3.1 Periodic Reporting 1462

9.14.3.2 Semi-Persistent Reporting 1462

9.14.3.3 Aperiodic Reporting 1462

9.14.3.4 Event Triggered Reporting 1462

9.14.3.5 Event-triggered Periodic Reporting 1463

9.14.4 Number of SSB frequency layers, number of cells and number of SSBs 1463

9.14.5 L1-RSRP intra-frequency measurement requirements without measurement gaps 1463

9.14.5.1 SSB based L1-RSRP reporting 1463

9.14.6 Measurement restriction for L1-RSRP measurement 1466

9.14.6.1 Measurement restriction for SSB based L1-RSRP 1466

9.14.7 Scheduling availability of UE during L1-RSRP measurement 1467

9.14.7.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 1467

9.14.7.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 1467

9.14.7.3 Scheduling availability of UE performing L1-RSRP measurement on FR2 1468

9.14.7.4 Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA 1468

9.14.7.5 Scheduling availability of UE performing L1-RSRP measurement in TDD bands on FR1 1468

9.14a CSI-RS based Intra-frequency L1-RSRP measurements for neighbour cell 1469

9.14a.1 Introduction 1469

9.14a.2 Requirements Applicability 1469

9.14a.3 Measurement Reporting Requirements 1470

9.14a.3.1 Periodic Reporting 1470

9.14a.3.2 Semi-Persistent Reporting 1470

9.14a.3.3 Aperiodic Reporting 1470

9.14a.3.4 Event-triggered Periodic Reporting 1470

9.14a.3.5 Event Triggered Reporting 1470

9.14a.4 Number of CSI-RS resources, number of cells 1471

9.14a.5 CSI-RS based L1-RSRP measurement requirements without measurement gaps 1471

9.14a.6 Measurement restriction for CSI-RS based L1-RSRP measurement 1472

9.14a.6.1 Measurement restriction for CSI-RS based L1-RSRP measurement 1473

9.14a.7 Scheduling availability of UE during CSI-RS based L1-RSRP measurement 1474

9.14a.7.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 1474

9.14a.7.2 Scheduling availability of UE performing L1-RSRP measurement on FR2 1474

9.14a.7.3 Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA 1475

9.14a.7.4 Scheduling availability of UE performing L1-RSRP measurement in TDD bands on FR1 1475

9.15 NR inter-frequency L1-RSRP measurements for neighbor cell 1475

9.15.1 Introduction 1475

9.15.2 Requirements Applicability 1475

9.15.3 Measurement Reporting Requirements 1476

9.15.3.1 Periodic Reporting 1476

9.15.3.2 Semi-Persistent Reporting 1476

9.15.3.3 Aperiodic Reporting 1476

9.15.3.4 Event Triggered Reporting 1477

9.15.3.5 Event Triggered Periodic Reporting 1477

9.15.4 Number of SSB frequency layers, number of cells and number of SSBs 1477

9.15.5 L1-RSRP inter-frequency measurement requirements with measurement gaps 1477

9.15.5.1 Inter-frequency SSB based L1-RSRP reporting 1477

9.15.6 L1-RSRP inter-frequency L1-RSRP measurement requirements without measurement gaps 1479

9.15.6.1 Inter-frequency L1-RSRP measurement requirements 1479

9.15.6.1.1 Inter-frequency SSB based L1-RSRP measurement 1479

9.15.6.2 Measurement restriction for inter-frequency L1-RSRP measurement 1482

9.15.6.2.1 Measurement restriction for SSB based L1-RSRP 1482

9.15.6.3 Scheduling availability of UE during inter-frequency L1-RSRP measurements 1483

9.15.6.3.1 Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1 1483

9.15.6.3.2 Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1 1483

9.15.6.3.3 Scheduling availability of UE performing L1-RSRP measurement on FR2 1484

9.15.6.3.4 Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA 1484

9.15.6.3.5 Scheduling availability of UE performing L1-RSRP measurement in TDD bands on FR1 1484

9.16 CJT calibration reporting for Delay offset and Frequency offset 1485

9.16.1 Introduction 1485

9.16.2 Requirements applicability 1485

9.16.3 Measurement Reporting Requirements 1485

9.16.3.1 Aperiodic Reporting 1485

After the UE receives CSI request in DCI with (reportQuantity set to ‘cjtc-Dd’, ‘cjtc-F’), the UE shall transmit the aperiodic CJTC reporting on PUSCH over the air interface at the time specified according to relevant clause in [26].9.16.4 Measurement Requirements 1485

9.16.4.1 CSI -RS based delay and frequency offset reporting 1485

9.16.5 Measurement restriction for UE during CJT calibration reporting 1487

9.16.5.1 Measurement restriction for CJT calibration reporting 1487

9.16.6 Scheduling availability of UE during CJT calibration reporting 1487

9.16.6.1 Scheduling availability of UE performing measurement for CJT calibration reporting on FR1 1487

9.17 OD-SSB based L3 measurement for an SCell 1488

9.17.1 Introduction 1488

9.17.2 Requirements Applicability 1488

9.17.3 Number of cells and number of SSB 1488

9.17.4 Measurement Reporting Requirements 1489

9.17.5 OD-SSB based Intra-frequency measurements without measurement gaps 1489

9.17.5.1 Intra-frequency cell identification for active SCell 1489

9.17.5.2 Measurement period for active SCell 1494

9.17.5.3 Intra-frequency cell identification for deactivated SCell 1496

9.17.5.4 Measurement period for deactivated SCell 1499

9.17.5.5 Scheduling availability of UE during intra-frequency measurements based on On-demand SSB 1500

9.17.5.5.1 Scheduling availability of UE performing measurements in TDD bands on FR1 1500

9.17.5.5.2 Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1 1500

9.17.5.5.3 Scheduling availability of UE performing measurements on FR2-1 1501

9.17.5.5.4 Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA 1502

9.18 L1 Cross Link Interference measurements 1502

9.18.1 Introduction 1502

9.18.2 L1-SRS-RSRP measurements 1503

9.18.2.1 Introduction 1503

9.18.2.2 Requirements applicability 1503

9.18.2.3 Measurement Reporting Requirements 1503

9.18.2.3.1 Aperiodic Reporting 1503

9.18.2.4 Measurement capability 1504

9.18.2.5 L1-SRS-RSRP measurement period 1504

9.18.2.6 Scheduling availability of UE during L1-CLI measurements 1504

9.18.2.6.1 Scheduling availability of UE performing L1-SRS-RSRP measurement on FR1 1504

9.18.2.6.2 Scheduling availability of UE performing L1-SRS-RSRP measurement on FR2 1505

9.18.3 L1-CLI-RSSI measurements 1506

9.18.3.1 Introduction 1506

9.18.3.2 Requirements applicability 1506

9.18.3.3 Measurement Reporting Requirements 1506

9.18.3.3.1 Periodic Reporting 1506

9.18.3.3.2 Aperiodic Reporting 1506

9.18.3.4 Measurement capability 1507

9.18.3.5 L1-CLI-RSSI measurement period 1507

9.18.3.6 Scheduling availability of UE during L1-CLI-RSSI measurements 1507

9.18.3.6.1 Scheduling availability of UE performing L1-CLI-RSSI measurement on FR1 1508

9.18.3.6.2 Scheduling availability of UE performing L1-CLI-RSSI measurement on FR2 1508

10 Measurement Performance requirements 1509

10.1 NR measurements 1509

10.1.1 Introduction 1509

10.1.2 Intra-frequency RSRP accuracy requirements for FR1 1509

10.1.2.1 Intra-frequency SS-RSRP accuracy requirements 1509

10.1.2.1.1 Absolute SS-RSRP Accuracy 1509

10.1.2.1.2 Relative SS-RSRP Accuracy 1510

10.1.2.2 Void 1511

10.1.2.3 Intra-frequency CSI-RSRP accuracy requirements 1511

10.1.2.3.1 Absolute CSI-RSRP Accuracy 1511

10.1.2.3.2 Relative CSI-RSRP Accuracy 1512

10.1.2B Intra-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode Measurements 1513

10.1.2B.1 Intra-frequency SS-RSRP accuracy requirements 1513

10.1.2B.1.1 Absolute SS-RSRP Accuracy 1513

10.1.2C Intra-frequency RSRP accuracy requirements for FR1 SAN 1514

10.1.2C.1 Intra-frequency SS-RSRP accuracy requirements 1514

10.1.2C.1.1 Absolute SS-RSRP Accuracy 1514

10.1.2C.1.2 Relative SS-RSRP Accuracy 1515

10.1.2D Intra-frequency RSRP accuracy requirements for RedCap UE with Satellite Access in FR1 1516

10.1.2D.1 Intra-frequency SS-RSRP accuracy requirements 1516

10.1.2D.1.1 Absolute SS-RSRP Accuracy 1516

10.1.2D.1.2 Relative SS-RSRP Accuracy 1516

10.1.3 Intra-frequency RSRP accuracy requirements for FR2 1517

10.1.3.1 Intra-frequency SS-RSRP accuracy requirements 1517

10.1.3.1.1 Absolute SS-RSRP Accuracy 1517

10.1.3.1.2 Relative SS-RSRP Accuracy 1518

10.1.3.2 Void 1518

10.1.3.3 Intra-frequency CSI-RSRP accuracy requirements 1518

10.1.3.3.1 Absolute CSI-RSRP Accuracy 1518

10.1.3.3.2 Relative CSI-RSRP Accuracy 1519

10.1.3B Intra-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode Measurements 1520

10.1.3B.1 Intra-frequency SS-RSRP accuracy requirements 1520

10.1.3B.1.1 Absolute SS-RSRP Accuracy 1520

10.1.3C Intra-frequency RSRP accuracy requirements for FR2-NTN 1521

10.1.3C.1 Intra-frequency SS-RSRP accuracy requirements 1521

10.1.3C.1.1 Absolute SS-RSRP Accuracy 1521

10.1.3C.1.2 Relative SS-RSRP Accuracy 1522

10.1.4 Inter-frequency RSRP accuracy requirements for FR1 1522

10.1.4.1 Inter-frequency SS-RSRP accuracy requirements 1522

10.1.4.1.1 Absolute SS-RSRP Accuracy in FR1 1522

10.1.4.1.2 Relative SS-RSRP Accuracy in FR1 1523

10.1.4.2 Void 1524

10.1.4.3 Inter-frequency CSI-RSRP accuracy requirements 1524

10.1.4.3.1 Absolute CSI-RSRP Accuracy in FR1 1524

10.1.4.3.2 Relative CSI-RSRP Accuracy in FR1 1525

10.1.4B Inter-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode Measurements 1526

10.1.4B.1 Inter-frequency SS-RSRP accuracy requirements 1526

10.1.4B.1.1 Absolute SS-RSRP Accuracy in FR1 1527

10.1.4C Inter-frequency RSRP accuracy requirements for FR1 SAN 1528

10.1.4C.1 Inter-frequency SS-RSRP accuracy requirements 1528

10.1.4C.1.1 Absolute SS-RSRP Accuracy in FR1 1528

10.1.4C.1.2 Relative SS-RSRP Accuracy in FR1 1528

10.1.4D Inter-frequency RSRP accuracy requirements for RedCap UE with Satellite Access in FR1 1529

10.1.4D.1 Inter-frequency SS-RSRP accuracy requirements 1529

10.1.4D.1.1 Absolute SS-RSRP Accuracy in FR1 1529

10.1.4D.1.2 Relative SS-RSRP Accuracy in FR1 1529

10.1.5 Inter-frequency RSRP accuracy requirements for FR2 1530

10.1.5.1 Inter-frequency SS-RSRP accuracy requirements 1530

10.1.5.1.1 Absolute SS-RSRP Accuracy 1530

10.1.5.1.2 Relative SS-RSRP Accuracy 1531

10.1.5.2 Void 1532

10.1.5.3 Inter-frequency CSI-RSRP accuracy requirements 1532

10.1.5.3.1 Absolute CSI-RSRP Accuracy 1532

10.1.5.3.2 Relative CSI-RSRP Accuracy 1532

10.1.5B Inter-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode Measurements 1533

10.1.5B.1 Inter-frequency SS-RSRP accuracy requirements 1533

10.1.5B.1.1 Absolute SS-RSRP Accuracy 1533

10.1.5C Inter-frequency RSRP accuracy requirements for FR2-NTN 1534

10.1.5C.1 Inter-frequency SS-RSRP accuracy requirements 1534

10.1.5C.1.1 Absolute SS-RSRP Accuracy 1534

10.1.5C.1.2 Relative SS-RSRP Accuracy 1535

10.1.6 RSRP Measurement Report Mapping 1535

10.1.7 Intra-frequency RSRQ accuracy requirements for FR1 1537

10.1.7.1 Intra-frequency SS-RSRQ accuracy requirements in FR1 1537

10.1.7.1.1 Absolute SS-RSRQ Accuracy in FR1 1537

10.1.7.2 Intra-frequency CSI-RSRQ accuracy requirements 1538

10.1.7.2.1 Absolute CSI-RSRQ Accuracy 1538

10.1.7B Intra-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode Measurements 1539

10.1.7B.1 Intra-frequency SS-RSRQ accuracy requirements in FR1 1539

10.1.7B.1.1 Absolute SS-RSRQ Accuracy in FR1 1539

10.1.7C Intra-frequency RSRQ accuracy requirements for FR1 SAN 1540

10.1.7C.1 Intra-frequency SS-RSRQ accuracy requirements in FR1 1540

10.1.7C.1.1 Absolute SS-RSRQ Accuracy in FR1 1540

10.1.7D Intra-frequency RSRQ accuracy requirements for RedCap UE with Satellite Access in FR1 1541

10.1.7D.1 Intra-frequency SS-RSRQ accuracy requirements in FR1 1541

10.1.7D.1.1 Absolute SS-RSRQ Accuracy in FR1 1541

10.1.8 Intra-frequency RSRQ accuracy requirements for FR2 1542

10.1.8.1 Intra-frequency SS-RSRQ accuracy requirements in FR2 1542

10.1.8.1.1 Absolute SS-RSRQ Accuracy in FR2 1542

10.1.8.2 Intra-frequency CSI-RSRQ accuracy requirements 1542

10.1.8.2.1 Absolute CSI-RSRQ Accuracy 1542

10.1.8B Intra-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode Measurements 1543

10.1.8B.1 Intra-frequency SS-RSRQ accuracy requirements in FR2 1543

10.1.8B.1.1 Absolute SS-RSRQ Accuracy in FR2 1543

10.1.8C Intra-frequency RSRQ accuracy requirements for FR2-NTN 1544

10.1.8C.1 Intra-frequency SS-RSRQ accuracy requirements in FR2-NTN 1544

10.1.8C.1.1 Absolute SS-RSRQ Accuracy in FR2-NTN 1544

10.1.9 Inter-frequency RSRQ accuracy requirements for FR1 1545

10.1.9.1 Inter-frequency SS-RSRQ accuracy requirements in FR1 1545

10.1.9.1.1 Absolute SS-RSRQ Accuracy in FR1 1545

10.1.9.1.2 Relative SS-RSRQ Accuracy in FR1 1545

10.1.9.2 Inter-frequency CSI-RSRQ accuracy requirements 1546

10.1.9.2.1 Absolute CSI-RSRQ Accuracy 1546

10.1.9.2.2 Relative CSI-RSRQ Accuracy 1547

10.1.9B Inter-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode Measurements 1548

10.1.9B.1 Inter-frequency SS-RSRQ accuracy requirements in FR1 1548

10.1.9B.1.1 Absolute SS-RSRQ Accuracy in FR1 1548

10.1.9C Inter-frequency RSRQ accuracy requirements for FR1 SAN 1549

10.1.9C.1 Inter-frequency SS-RSRQ accuracy requirements in FR1 1549

10.1.9C.1.1 Absolute SS-RSRQ Accuracy in FR1 1549

10.1.9C.1.2 Relative SS-RSRQ Accuracy in FR1 1550

10.1.9D Inter-frequency RSRQ accuracy requirements for RedCap UE with Satellite Access in FR1 1551

10.1.9D.1 Inter-frequency SS-RSRQ accuracy requirements in FR1 1551

10.1.9D.1.1 Absolute SS-RSRQ Accuracy in FR1 1551

10.1.9D.1.2 Relative SS-RSRQ Accuracy in FR1 1551

10.1.10 Inter-frequency RSRQ accuracy requirements for FR2 1552

10.1.10.1 Inter-frequency SS-RSRQ accuracy requirements in FR2 1552

10.1.10.1.1 Absolute SS-RSRQ Accuracy in FR2 1552

10.1.10.1.2 Relative SS-RSRQ Accuracy in FR2 1552

10.1.10.2 Inter-frequency CSI-RSRQ accuracy requirements 1553

10.1.10.2.1 Absolute CSI-RSRQ Accuracy 1553

10.1.10.2.2 Relative CSI-RSRQ Accuracy 1554

10.1.10B  Inter-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode Measurements 1555

10.1.10B.1 Inter-frequency SS-RSRQ accuracy requirements in FR2 1555

10.1.10B.1.1 Absolute SS-RSRQ Accuracy in FR2 1555

10.1.10C Inter-frequency RSRQ accuracy requirements for FR2-NTN 1556

10.1.10C.1 Inter-frequency SS-RSRQ accuracy requirements in FR2-NTN 1556

10.1.10C.1.1 Absolute SS-RSRQ Accuracy in FR2-NTN 1556

10.1.10C.1.2 Relative SS-RSRQ Accuracy in FR2-NTN 1556

10.1.11 RSRQ report mapping 1557

10.1.12 Intra-frequency SINR accuracy requirements for FR1 1558

10.1.12.1 Intra-frequency SS-SINR accuracy requirements in FR1 1558

10.1.12.1.1 Absolute SS-SINR Accuracy in FR1 1558

10.1.12.2 Intra-frequency CSI-SINR accuracy requirements in FR1 1558

10.1.12.2.1 Absolute CSI-SINR Accuracy in FR1 1558

10.1.12C  Intra-frequency SINR accuracy requirements for FR1 SAN 1559

10.1.12C.1 Intra-frequency SS-SINR accuracy requirements in FR1 1559

10.1.12C.1.1 Absolute SS-SINR Accuracy in FR1 1559

10.1.12D  Intra-frequency SINR accuracy requirements for RedCap UE with Satellite Access in FR1 1560

10.1.12D.1 Intra-frequency SS-SINR accuracy requirements in FR1 1560

10.1.12D.1.1 Absolute SS-SINR Accuracy in FR1 1560

10.1.13 Intra-frequency SINR accuracy requirements for FR2 1561

10.1.13.1 Intra-frequency SS-SINR accuracy requirements in FR2 1561

10.1.13.1.1 Absolute SS-SINR Accuracy in FR2 1561

10.1.13.2 Intra-frequency CSI-SINR accuracy requirements in FR2 1561

10.1.13.2.1 Absolute CSI-SINR Accuracy in FR2 1561

10.1.13C Intra-frequency SINR accuracy requirements for FR2-NTN 1562

10.1.13C.1 Intra-frequency SS-SINR accuracy requirements in FR2-NTN 1562

10.1.13C.1.1 Absolute SS-SINR Accuracy in FR2-NTN 1562

10.1.14 Inter-frequency SINR accuracy requirements for FR1 1563

10.1.14.1 Inter-frequency SS-SINR accuracy requirements in FR1 1563

10.1.14.1.1 Absolute SS-SINR Accuracy in FR1 1563

10.1.14.1.2 Relative SS-SINR Accuracy in FR1 1563

10.1.14.2 Inter-frequency CSI-SINR accuracy requirements in FR1 1564

10.1.14.2.1 Absolute CSI-SINR Accuracy in FR1 1564

10.1.14.2.2 Relative CSI-SINR Accuracy in FR1 1565

10.1.14C  Inter-frequency SINR accuracy requirements for FR1 SAN 1566

10.1.14C.1 Inter-frequency SS-SINR accuracy requirements in FR1 1566

10.1.14C.1.1 Absolute SS-SINR Accuracy in FR1 1566

10.1.14C.1.2 Relative SS-SINR Accuracy in FR1 1567

10.1.14D  Inter-frequency SINR accuracy requirements for RedCap UE with Satellite Access in FR1 1568

10.1.14D.1 Inter-frequency SS-SINR accuracy requirements in FR1 1568

10.1.14D.1.1 Absolute SS-SINR Accuracy in FR1 1568

10.1.14D.1.2 Relative SS-SINR Accuracy in FR1 1568

10.1.15 Inter-frequency SINR accuracy requirements for FR2 1569

10.1.15.1 Inter-frequency SS-SINR accuracy requirements in FR2 1569

10.1.15.1.1 Absolute SS-SINR Accuracy in FR2 1569

10.1.15.1.2 Relative SS-SINR Accuracy in FR2 1569

10.1.15.2 Inter-frequency CSI-SINR accuracy requirements in FR2 1570

10.1.15.2.1 Absolute CSI-SINR Accuracy in FR2 1570

10.1.15.2.2 Relative CSI-SINR Accuracy in FR2 1571

10.1.15C Inter-frequency SINR accuracy requirements for FR2-NTN 1572

10.1.15C.1 Inter-frequency SS-SINR accuracy requirements in FR2-NTN 1572

10.1.15C.1.1 Absolute SS-SINR Accuracy in FR2-NTN 1572

10.1.15C.1.2 Relative SS-SINR Accuracy in FR2-NTN 1572

10.1.16 SINR report mapping 1573

10.1.16.1 SS-SINR and CSI-SINR measurement report mapping 1573

10.1.17 Power Headroom 1574

10.1.17.1 Power Headroom Report 1574

10.1.17.1.1 Power Headroom Report Mapping 1574

10.1.18 PCMAX,c,f 1574

10.1.18.1 Report Mapping 1574

10.1.19 L1-RSRP accuracy requirements for FR1 1575

10.1.19.1 SSB based L1-RSRP accuracy requirements 1575

10.1.19.1.1 Absolute Accuracy 1575

10.1.19.1.2 Relative Accuracy 1576

10.1.19.2 CSI-RS based L1-RSRP accuracy requirements 1577

10.1.19.2.1 Absolute Accuracy 1577

10.1.19.2.2 Relative Accuracy 1579

10.1.19C L1-RSRP accuracy requirements for FR1 SAN 1581

10.1.19C.1 SSB based L1-RSRP accuracy requirements 1581

10.1.19C.1.1 Absolute Accuracy 1581

10.1.19C.1.2 Relative Accuracy 1582

10.1.19C.2 CSI-RS based L1-RSRP accuracy requirements 1582

10.1.19C.2.1 Absolute Accuracy 1582

10.1.19C.2.2 Relative Accuracy 1583

10.1.19D LTM Intra-frequency L1-RSRP accuracy requirements for FR1 1584

10.1.19D.1 SSB based intra-frequency L1-RSRP accuracy requirements 1584

10.1.19D.1.1 Absolute Accuracy 1584

10.1.19D.1.2 Relative Accuracy 1585

10.1.19D.2 CSI-RS based intra-frequency L1-RSRP accuracy requirements 1585

10.1.19D.2.1 Absolute CSI-RSRP Accuracy 1585

10.1.19D.2.2 Relative CSI-RSRP Accuracy 1586

10.1.19E LTM Inter-frequency L1-RSRP accuracy requirements for FR1 1587

10.1.19E.1 SSB based Inter-frequency L1-RSRP accuracy requirements 1587

10.1.19E.1.1 Absolute Accuracy 1587

10.1.19E.1.2 Relative Accuracy 1588

10.1.19F L1-RSRP accuracy requirements for RedCap UE with Satellite Access in FR1 1589

10.1.19F.1 SSB based L1-RSRP accuracy requirements 1589

10.1.19F.1.1 Absolute Accuracy 1589

10.1.19F.1.2 Relative Accuracy 1590

10.1.19F.2 CSI-RS based L1-RSRP accuracy requirements 1590

10.1.19F.2.1 Absolute Accuracy 1590

10.1.19F.2.2 Relative Accuracy 1591

10.1.20 L1-RSRP accuracy requirements for FR2 1592

10.1.20.1 SSB based L1-RSRP accuracy requirements 1592

10.1.20.1.1 Absolute Accuracy 1592

10.1.20.1.2 Relative Accuracy 1592

10.1.20.2 CSI-RS based L1-RSRP accuracy requirements 1593

10.1.20.2.1 Absolute Accuracy 1593

10.1.20.2.2 Relative Accuracy 1594

10.1.20A   LTM Intra-frequency L1-RSRP accuracy requirements for FR2 1595

10.1.20A.1 SSB based intra-frequency L1-RSRP accuracy requirements 1595

10.1.20A.1.1 Absolute Accuracy 1595

10.1.20A.1.2 Relative Accuracy 1596

10.1.20A.2 CSI-RS based intra-frequency L1-RSRP accuracy requirements 1597

10.1.20A.2.1 Absolute Accuracy 1597

10.1.20A.2.2 Relative Accuracy 1597

10.1.20B LTM Inter-frequency L1-RSRP accuracy requirements for FR2 1598

10.1.20B.1 SSB based inter-frequency L1-RSRP accuracy requirements 1598

10.1.20B.1.1 Absolute Accuracy 1598

10.1.20B.1.2 Relative Accuracy 1599

10.1.20C L1-RSRP accuracy requirements for FR2-NTN 1599

10.1.20C.1 SSB based L1-RSRP accuracy requirements 1599

10.1.20C.1.1 Absolute Accuracy 1599

10.1.20C.1.2 Relative Accuracy 1600

10.1.20C.2 CSI-RS based L1-RSRP accuracy requirements 1601

10.1.20C.2.1 Absolute Accuracy 1601

10.1.20C.2.2 Relative Accuracy 1601

10.1.20D  Predicted L1-RSRP accuracy requirements for FR2 1602

10.1.20D.1 CSI-RS based predicted L1-RSRP accuracy requirements 1602

10.1.20D.1.1 Absolute Accuracy 1602

10.1.21 SFTD accuracy requirements 1604

10.1.21.1 SFTD acuracy requirements for NE-DC 1604

10.1.21.2 SFTD acuracy requirements for NR-DC 1606

10.1.21.3 Inter-frequency SFTD acuracy requirements 1607

10.1.22 CLI measurement accuracy requirements 1608

10.1.22.1 SRS-RSRP 1608

10.1.22.1.1 SRS-RSRP Accuracy 1608

10.1.22.1.2 SRS-RSRP report mapping 1609

10.1.22.2 CLI-RSSI 1610

10.1.22.2.1 CLI-RSSI Accuracy 1610

10.1.22.2.2 CLI-RSSI report mapping 1611

10.1.23 RSTD Measurements 1611

10.1.23.1 Introduction 1611

10.1.23.2 Measurement Accuracy Requirements 1611

10.1.23.3 Report mapping 1619

10.1.23.3.1 Absolute DL RSTD Measurement Reporting 1619

10.1.23.3.2 Differential Reporting for DL RSTD Measurement 1622

10.1.23.3.3 Additional Path Report Mapping for DL RSTD 1625

10.1.23A RSTD Measurements Based on PRS Aggregation 1629

10.1.23A.1 Introduction 1629

10.1.23A.3 Report Mapping 1636

10.1.23A.3.1 Absolute DL RSTD Measurement Reporting 1636

10.1.23A.3.2 Differential Reporting for DL RSTD Measurement 1636

10.1.23A.3.3 Additional Path Report Mapping for DL RSTD 1636

10.1.24 PRS-RSRP Measurements 1636

10.1.24.1 Introduction 1636

10.1.24.2 Measurement Accuracy Requirements 1637

10.1.24.2.1 Absolute PRS-RSRP accuracy 1637

10.1.24.2.2 Relative PRS RSRP accuracy 1641

10.1.24.3 Report mapping 1645

10.1.24.3.1 Absolute PRS-RSRP Measurement Report Mapping 1645

10.1.24.3.2 Differential Report Mapping for PRS-RSRP Measurement 1646

10.1.24A PRS-RSRP Measurements Based on PRS Aggregation 1648

10.1.24A.1 Introduction 1648

10.1.24A.2 Measurement Accuracy Requirements 1649

10.1.24A.2.1 Absolute PRS RSRP Accuracy Requirement 1649

10.1.24A.2.2 Relative PRS RSRP Accuracy Requirement 1649

10.1.24A.3 Report Mapping 1649

10.1.24A.3.1 Absolute PRS-RSRP Measurement Report Mapping 1649

10.1.24A.3.2 Differential Report Mapping for PRS-RSRP Measurement 1649

10.1.25 UE Rx-Tx Time Difference Measurements 1649

10.1.25.1 Introduction 1649

10.1.25.2 Measurement Accuracy Requirements 1649

10.1.25.3 Report mapping 1661

10.1.25.3.1 Absolute UE Rx-Tx Measurement Report Mapping 1661

10.1.25.3.2 Differential UE Rx-Tx Measurement Report Mapping 1664

10.1.25.3.3 Additional Path Report Mapping for UE Rx-Tx Time Difference 1667

10.1.25A UE Rx-Tx Time Difference Measurement Based on PRS Aggregation 1670

10.1.25A.1 Introduction 1670

10.1.25A.2 Measurement Accuracy Requirements 1671

10.1.25A.3 Report mapping 1687

10.1.25C UE Rx-Tx Time Difference Measurements in Satellite Accesss 1687

10.1.25C.1 Introduction 1687

10.1.25C.2 Measurement Accuracy Requirements 1687

10.1.25C.3 Report mapping 1688

10.1.25D UE Rx-Tx Time Difference Measurements RedCap UE with Satellite Access in FR1 1688

10.1.25D.1 Introduction 1688

10.1.25D.2 Measurement Accuracy Requirements 1689

10.1.25D.2.1 UE Rx-Tx Accuracy Requirement for 2Rx RedCap UE without FH 1689

10.1.25D.2.2 UE Rx-Tx Accuracy Requirement for 1Rx RedCap UE without FH 1689

10.1.25D.3 Report mapping 1689

10.1.26 FR2 P-MPR report 1689

10.1.26.1 Report mapping 1690

10.1.27 L1-SINR accuracy requirements for FR1 1690

10.1.27.1 L1-SINR accuracy requirements with CSI-RS based CMR and no dedicated IMR configured 1690

10.1.27.1.1 Absolute Accuracy 1690

10.1.27.1.2 Relative Accuracy 1691

10.1.27.2 L1-SINR accuracy requirements with SSB based CMR and dedicated IMR configured 1693

10.1.27.2.1 Absolute Accuracy 1693

10.1.27.2.2 Relative Accuracy 1696

10.1.27.3 L1-SINR accuracy requirements with CSI-RS based CMR and dedicated IMR configured 1698

10.1.27.3.1 Absolute Accuracy 1698

10.1.27.3.2 Relative Accuracy 1701

10.1.28 L1-SINR accuracy requirements for FR2 1704

10.1.29 Intra-frequency RSRQ accuracy requirements under CCA 1715

10.1.29.1 Intra-frequency SS-RSRQ accuracy requirements in FR1 1715

10.1.29.1.1 Absolute SS-RSRQ Accuracy 1715

10.1.30 Inter-frequency RSRQ accuracy requirements under CCA 1715

10.1.30.1 Inter-frequency SS-RSRQ accuracy requirements in FR1 1715

10.1.30.1.1 Absolute SS-RSRQ Accuracy 1715

10.1.30.1.2 Relative SS-RSRQ Accuracy 1716

10.1.31 Intra-frequency SINR accuracy requirements under CCA 1717

10.1.31.1 Intra-frequency SS-SINR accuracy requirements in FR1 1717

10.1.31.1.1 Absolute SS-SINR Accuracy 1717

10.1.32 Inter-frequency SINR accuracy requirements under CCA 1717

10.1.32.1 Inter-frequency SS-SINR accuracy requirements in FR1 1717

10.1.32.1.1 Absolute SS-SINR Accuracy 1717

10.1.32.1.2 Relative SS-SINR Accuracy 1718

10.1.33 L1-RSRP accuracy requirements under CCA 1719

10.1.33.1 SSB based L1-RSRP accuracy requirements in FR1 1719

10.1.33.1.1 Absolute Accuracy 1719

10.1.33.1.2 Relative Accuracy 1719

10.1.34 RSSI measurements under CCA 1720

10.1.34.1 Intra-frequency absolute RSSI measurement accuracy requirements in FR1 1720

10.1.34.2 Inter-frequency absolute RSSI measurement accuracy requirements in FR1 1720

10.1.34.3 RSSI measurement report mapping 1720

10.1.35 Channel occupancy measurements under CCA 1721

10.1.35.1 Intra-frequency channel occupancy measurement accuracy requirements in FR1 1721

10.1.35.2 Inter-frequency channel occupancy measurement accuracy requirements in FR1 1721

10.1.36 Intra-frequency RSRP accuracy requirements under CCA 1721

10.1.36.1 Intra-frequency SS-RSRP accuracy requirements in FR1 1721

10.1.36.1.1 Absolute SS-RSRP Accuracy 1721

10.1.36.1.2 Relative SS-RSRP Accuracy 1722

10.1.37 Inter-frequency RSRP accuracy requirements under CCA 1722

10.1.37.1 Inter-frequency SS-RSRP accuracy requirements in FR1 1722

10.1.37.1.1 Absolute SS-RSRP 1722

10.1.37.1.2 Relative SS-RSRP Accuracy 1723

10.1.38 PRS-RSRPP Measurements 1724

10.1.38.1 Introduction 1724

10.1.38.2 Measurement Accuracy Requirements 1724

10.1.38.2.1 Absolute PRS RSRPP accuracy 1724

10.1.38.3 Report mapping 1728

10.1.38.3.1 Absolute PRS-RSRPP Measurement Report Mapping 1728

10.1.38.3.2 Differential Report Mapping for PRS-RSRPP Measurement 1729

10.1.38A PRS-RSRPP Measurements Based on PRS Aggregation 1730

10.1. 38A.1 Introduction 1730

10.1.38A.2 Measurement Accuracy Requirements 1731

10.1.38A.2.1 Absolute PRS RSRPP accuracy 1731

10.1.38A.3 Report mapping 1731

10.1.38A.3.1 Absolute PRS-RSRPP Measurement Report Mapping 1731

10.1.38A.3.2 Differential Report Mapping for PRS-RSRPP Measurement 1731

10.1.39 UE Rx-Tx time difference measurements for RTT-based PDC 1731

10.1.39.1 Void 1731

10.1.39.2  Measurement Accuracy Requirements for PRS 1731

10.1.39.3  Measurement Accuracy Requirements for TRS 1734

10.1.40 Void 1738

10.1.41 FR1 DPC report 1738

10.1.41.1 Report mapping 1738

10.1.42 TDCP Measurement Report Mapping 1738

10.1.43 DL-RSCPD Measurements 1740

10.1.43.1 Introduction 1740

10.1.43.2.1 Measurement Accuracy Requirements 1740

10.1.43.3 Report Mapping 1747

10.1.43.3.1 Absolute DL RSCPD Measurement Reporting 1747

10.1.44 DL-RSCP Measurements 1748

10.1.44.1 Introduction 1748

10.1.44.2 Measurement Accuracy Requirements 1748

10.1.44.3 Report Mapping 1756

10.1.44.3.1 Relative DL RSCP Measurement Reporting 1756

10.1.45 CJT calibration measurements 1757

10.1.45.1 Introduction 1757

10.1.45.2 CJTC calibration delay offset report 1758

10.1.45.3 CJTC calibration frequency offset report 1760

10.1.46 CJT Calibration Report Mapping 1762

10.1.46.1 CJT Calibration Delay Offset Measurement Report Mapping 1762

10.1.46.2 CJT Calibration Frequency Offset Measurement Report Mapping 1762

10.1.46.3 CJT Calibration Phase Offset Measurement Report Mapping 1762

10.1.47 L1 CLI measurement accuracy requirements 1763

10.1.47.1 L1-SRS-RSRP 1763

10.1.47.1.1 L1-SRS-RSRP Accuracy 1763

10.1.47.1.2 L1-SRS-RSRP report mapping 1764

10.1.47.2 L1-CLI-RSSI 1765

10.1.47.2.1 L1-CLI-RSSI Accuracy 1765

10.1.47.2.2 L1-CLI-RSSI report mapping 1766

10.1.48 RS resource prediction accuracy requirements for FR2 1767

10.1.48.1 CSI-RS based RS resource prediction accuracy requirements 1767

10.1A NR measurements for RedCap 1769

10.1A.1 Introduction 1769

10.1A.2 Intra-frequency RSRP accuracy requirements for FR1 1769

10.1A.2.1 Intra-frequency SS-RSRP accuracy requirements 1769

10.1A.2.1.1 Absolute SS-RSRP Accuracy 1769

10.1A.2.1.2 Relative SS-RSRP Accuracy 1770

10.1A.3 Intra-frequency RSRP accuracy requirements for FR2 1771

10.1A.3.1 Intra-frequency SS-RSRP accuracy requirements 1771

10.1A.3.1.1 Absolute SS-RSRP Accuracy 1771

10.1A.3.1.2 Relative SS-RSRP Accuracy 1771

10.1A.4 Inter-frequency RSRP accuracy requirements for FR1 1771

10.1A.4.1 Inter-frequency SS-RSRP accuracy requirements 1771

10.1A.4.1.1 Absolute SS-RSRP Accuracy in FR1 1771

10.1A.4.1.2 Relative SS-RSRP Accuracy in FR1 1772

10.1A.5 Inter-frequency RSRP accuracy requirements for FR2 1773

10.1A.5.1 Inter-frequency SS-RSRP accuracy requirements 1773

10.1A.5.1.1 Absolute SS-RSRP Accuracy 1773

10.1A.5.1.2 Relative SS-RSRP Accuracy 1773

10.1A.6 Intra-frequency RSRQ accuracy requirements for FR1 1773

10.1A.6.1 Intra-frequency SS-RSRQ accuracy requirements in FR1 1773

10.1A.6.1.1 Absolute SS-RSRQ Accuracy in FR1 1773

10.1A.7 Intra-frequency RSRQ accuracy requirements for FR2 1774

10.1A.7.1 Intra-frequency SS-RSRQ accuracy requirements in FR2 1774

10.1A.7.1.1 Absolute SS-RSRQ Accuracy in FR2 1774

10.1A.8 Inter-frequency RSRQ accuracy requirements for FR1 1774

10.1A.8.1 Inter-frequency SS-RSRQ accuracy requirements in FR1 1774

10.1A.8.1.1 Absolute SS-RSRQ in FR1 1774

10.1A.8.1.2 Relative SS-RSRQ Accuracy in FR1 1775

10.1A.9 Inter-frequency RSRQ accuracy requirements for FR2 1776

10.1A.9.1 Inter-frequency SS-RSRQ accuracy requirements in FR2 1776

10.1A.9.1.1 Absolute SS-RSRQ Accuracy in FR2 1776

10.1A.9.1.2 Relative SS-RSRQ Accuracy in FR2 1776

10.1A.10  Intra-frequency SINR accuracy requirements for FR1 1776

10.1A.10.1 Intra-frequency SS-SINR accuracy requirements in FR1 1776

10.1A.10.1.1 Absolute SS-SINR Accuracy in FR1 1776

10.1A.11 Intra-frequency SINR accuracy requirements for FR2 1777

10.1A.11.1 Intra-frequency SS-SINR accuracy requirements in FR2 1777

10.1A.11.1.1 Absolute SS-SINR Accuracy in FR2 1777

10.1A.12  Inter-frequency SINR accuracy requirements for FR1 1777

10.1A.12.1 Inter-frequency SS-SINR accuracy requirements in FR1 1777

10.1A.12.1.1 Absolute SS-SINR Accuracy in FR1 1777

10.1A.12.1.2 Relative SS-SINR Accuracy in FR1 1778

10.1A.13  Inter-frequency SINR accuracy requirements for FR2 1779

10.1A.13.1 Inter-frequency SS-SINR accuracy requirements in FR2 1779

10.1A.13.1.1 Absolute SS-SINR Accuracy in FR2 1779

10.1A.13.1.2 Relative SS-SINR Accuracy in FR2 1779

10.1A.14 L1-RSRP accuracy requirements for FR1 1779

10.1A.14.1 SSB based L1-RSRP accuracy requirements 1779

10.1A.14.1.1 Absolute Accuracy 1779

10.1A.14.1.2 Relative Accuracy 1780

10.1A.14.2 CSI-RS based L1-RSRP accuracy requirements 1781

10.1A.14.2.1 Absolute Accuracy 1781

10.1A.14.2.2 Relative Accuracy 1782

10.1A.15  L1-RSRP accuracy requirements for FR2 1783

10.1A.15.1 SSB based L1-RSRP accuracy requirements 1783

10.1A.15.1.1 Absolute Accuracy 1783

10.1A.15.1.2 Relative Accuracy 1783

10.1A.15.2 CSI-RS based L1-RSRP accuracy requirements 1783

10.1A.15.2.1 Absolute Accuracy 1783

10.1A.15.2.2 Relative Accuracy 1783

10.1A.16 RSTD Measurements for RedCap Positioning 1784

10.1A.16.1 Introduction 1784

10.1A.16.2 Measurement Accuracy Requirements 1784

10.1A.16.2.1 Accuracy requirement for RSTD measurement without RX FH 1784

10.1A.16.2.2 Accuracy requirement for RSTD measurement with RX FH 1791

10.1A.16.3 Report Mapping 1806

10.1A.16.3.1 Absolute DL RSTD Measurement Reporting 1806

10.1A.16.3.2 Differential Reporting for DL RSTD Measurement 1806

10.1A.16.3.3 Additional Path Report Mapping for DL RSTD 1806

10.1A.17 PRS-RSRP Measurements for RedCap positioning 1806

10.1A.17.1 Introduction 1806

10.1A.17.2 Measurement Accuracy Requirements 1806

10.1A.17.2.1 Absolute PRS RSRP Accuracy Requirement 1806

10.1A.17.2.2 Relative PRS RSRP Accuracy Requirement 1809

10.1A.17.3 Report Mapping 1809

10.1A.17.3.1 Absolute PRS-RSRP Measurement Report Mapping 1809

10.1A.17.3.2 Differential Report Mapping for PRS-RSRP Measurement 1809

10.1A.18   UE Rx-Tx Time Difference Measurements for RedCap Positioning 1810

10.1A.18.1 Introduction 1810

10.1A.18.2 Measurement Accuracy Requirements 1810

10.1A.18.2.1 UE Rx-Tx Accuracy Requirement for 2RX RedCap UE without FH 1810

10.1A.18.2.2 UE Rx-Tx Accuracy Requirement for 1RX RedCap UE without FH 1811

10.1A.18.2.3 UE Rx-Tx Accuracy Requirement for 2RX RedCap UE with FH 1816

10.1A.18.3 Report mapping 1826

10.1A.18.3.1 Absolute UE Rx-Tx Measurement Report Mapping 1826

10.1A.18.3.2 Differential UE Rx-Tx Measurement Report Mapping 1826

10.1A.18.3.3 Additional Path Report Mapping for UE Rx-Tx Time Difference 1826

10.1A.19 PRS-RSRPP Measurements for RedCap Positioning 1826

10.1A.19.1 Introduction 1826

10.1A.19.2 Measurement Accuracy Requirements 1827

10.1A.19.2.1 Absolute PRS RSRPP accuracy 1827

10.1A.19.3 Report mapping 1829

10.1A.19.3.1 Absolute PRS-RSRPP Measurement Report Mapping 1829

10.1A.19.3.2 Differential Report Mapping for PRS-RSRPP Measurement 1830

10.2 E-UTRAN measurements 1830

10.2.1 Introduction 1830

10.2.2 E-UTRAN RSRP measurements 1830

10.2.3 E-UTRAN RSRQ measurements 1830

10.2.4 E-UTRAN RSTD measurements 1830

10.2.5 E-UTRAN RS-SINR measurements 1831

10.2.6 E-UTRAN RSRP measurements for CA/DC Idle Mode Measurements 1831

10.2.7 E-UTRAN RSRQ measurements for CA/DC Idle Mode Measurements 1831

10.2A E-UTRAN measurements for RedCap 1832

10.2A.1 Introduction 1832

10.2A.2 E-UTRAN RSRP measurements 1832

10.2A.3 E-UTRAN RSRQ measurements 1832

10.2A.4 E-UTRAN RS-SINR measurements 1833

10.3 UTRAN FDD Measurements 1833

10.3.1 UTRAN FDD CPICH RSCP 1833

10.3.2 UTRAN FDD CPICH Ec/No 1834

10.4 V2X measurements 1834

10.4.1 Introduction 1834

10.4.2 Intra-frequency PSBCH-RSRP accuracy requirements for FR1 1834

10.4.2.1 PSBCH-RSRP Absolute Accuracy 1834

10.4.2.2 PSBCH-RSRP Relative Accuracy 1835

10.4.2A Intra-frequency PSBCH-RSRP accuracy requirements for FR1 under CCA 1836

10.4.2A.1 PSBCH-RSRP Absolute Accuracy 1836

10.4.2A.2 PSBCH-RSRP Relative Accuracy 1836

10.4.3 Intra-Frequency SL-RSSI Measurement Accuracy Requirements for FR1 1837

10.4.3.1 Absolute SL-RSSI Accuracy 1837

10.4.3A Intra-Frequency SL-RSSI Measurement Accuracy Requirements for FR1 under CCA 1837

10.4.3A.1 Absolute SL-RSSI Accuracy 1837

10.4.4 Intra-Frequency L1 SL-RSRP Measurement Accuracy Requirements for FR1 1838

10.4.4.1 Absolute L1 SL-RSRP Accuracy 1838

10.4.4A Intra-Frequency L1 SL-RSRP Measurement Accuracy Requirements for FR1 under CCA 1838

10.4.4A.1 Absolute L1 SL-RSRP Accuracy 1838

10.4.5 Intra-Frequency Discovery Signal Measurement Accuracy Requirements 1839

10.4.5.1 Absolute Discovery Signal Measurement Accuracy 1839

10.4A NR Sidelink Measurements for Positioning 1840

10.4A.1 Introduction 1840

10.4A.2 SL RSTD measurements 1840

10.4A.2.1 Measurement Report Mapping 1840

10.4A.2.1.1 Absolute SL RSTD Measurement Reporting 1840

10.4A.2.2 Measurement Accuracy Requirements 1841

10.4A.3 SL PRS-RSRP measurements 1843

10.4A.3.1 Measurement Report Mapping 1843

10.4A.3.1.1 Absolute SL PRS-RSRP Measurement Report Mapping 1843

10.4A.3.2 Measurement Accuracy Requirements 1844

10.4A.3.2.1 Absolute SL PRS-RSRP accuracy 1844

10.4A.4 SL Rx-Tx measurements 1845

10.4A.4.1 Measurement Report Mapping 1845

10.4A.4.1.1 Absolute SL Rx-Tx Measurement Report Mapping 1845

10.4A.4.2 Measurement Accuracy 1847

10.4A.5 SL PRS-RSRPP measurements 1848

10.4A.5.1 Measurement Report Mapping 1848

10.4A.5.1.1 Absolute SL PRS-RSRPP Measurement Report Mapping 1848

10.4A.5.2 Measurement Accuracy 1849

10.4A.5.2.1 Introduction 1849

10.4A.5.2.2 Measurement Accuracy Requirements 1850

10.4A.5.2.2.2 Absolute SL PRS-RSRPP accuracy 1850

10.4A.6 SL AoA measurements 1851

10.4A.6.1 Measurement Report Mapping 1851

10.4A.6.1.1 Absolute SL AoA Measurement Report Mapping 1851

10.4A.7 SL RTOA measurements 1852

10.4A.7.1 Measurement Report Mapping 1852

10.4A.7.1.1 Absolute SL RTOA Measurement Report Mapping 1852

11 Void 1854

12 V2X Requirements 1855

12.1 Introduction 1855

12.2 UE Transmit Timing 1855

12.2.1 Introduction 1855

12.2.2 GNSS as synchronization reference source 1856

12.2.3 NR Cell as synchronization reference source 1856

12.2.4 E-URTAN Cell as synchronization reference source 1856

12.2.5 SyncRef UE as synchronization reference source 1857

12.3 Initiation/Cease of SLSS Transmissions 1857

12.3.1 Introduction 1857

12.3.1.1 Initiation/Cease of SLSS transmissions with NR cell as synchronization reference source 1857

12.3.1.2 Initiation/Cease of SLSS transmissions with EUTRAN cell as synchronization reference source 1858

12.3.1.3 Initiation/Cease of SLSS transmissions with GNSS as synchronization reference source 1859

12.3.1.4 Initiation/Cease of SLSS transmissions with SyncRef UE as synchronization reference source 1859

12.3A Initiation/Cease of SLSS Transmissions with CCA 1860

12.3A.1 Introduction 1860

12.3A.1.1 Initiation/Cease of SLSS transmissions with NR cell as synchronization reference source 1860

12.3A.1.2 Initiation/Cease of SLSS transmissions with EUTRAN cell as synchronization reference source 1860

12.3A.1.3 Initiation/Cease of SLSS transmissions with GNSS as synchronization reference source 1860

12.3A.1.4 Initiation/Cease of SLSS transmissions with SyncRef UE as synchronization reference source 1861

12.4 Selection / Reselection of V2X Synchronization Reference Source 1861

12.4A Selection / Reselection of Sidelink Synchronization Reference Source with CCA 1863

12.5 L1 SL-RSRP measurements 1865

12.5.1 Introduction 1865

12.5.2 SL-RSRP measurements 1865

12.6 Congestion Control measurements 1866

12.7 Interruption 1866

12.7.1 Interruptions to WAN due to V2X Sidelink Communication 1866

12.7.2 V2X Sidelink Communication Dropping due to synchronization source change 1866

12.7.3 Interruptions to WAN due to switching between E-UTRA V2X Sidelink and NR V2X Sidelink 1868

12.7.4 Interruptions to WAN at transitions between active and non-active during SL-DRX 1868

12.7.5 Interruptions to V2X sidelink at transitions between active and non-active during DRX 1869

12.7.6 Interruptions to V2X sidelink due to Active BWP switching Requirement 1869

12.7.7 Interruptions to WAN due to SyncRef UE detection and/or Sensing during SL DRX off duration 1870

12.7.8 Interruptions at NR sidelink discovery configuration 1870

12.7.9 Interruptions to WAN due to sidelink carrier addition/release 1870

12.8 Reliability of GNSS signal 1871

12.9 Scheduling availability 1871

12.9.1 Scheduling availability of UE switching between E-UTRA sidelink and NR sidelink 1871

12.9.2 Scheduling availability of UE switching between Uu uplink  and V2X sidelink 1871

12.10 Selection / Reselection of relay UE 1872

12.10.1 Introduction 1872

12.10.2 Selection / Reselection of relay UE 1872

12.11 Component Carrier Addition and Release Delay for Sidelink Carrier Aggregation 1872

12.12 Selection / Reselection of Synchronization Reference Source for NR SL Carrier Aggregation 1873

12A NR Sidelink Measurements for Positioning 1874

12A.1 Introduction 1874

12A.2 SL RSTD measurements 1875

12A.2.1 Introduction 1875

12A.2.3 Measurement Capability 1875

12A.2.4 Measurement Reporting Requirements 1875

12A.2.5 Measurements Period Requirements 1875

12A.3 SL PRS-RSRP measurements 1876

12A.3.1 Introduction 1876

12A.3.2 Requirements Applicability 1877

12A.3.4 Measurement Reporting Requirements 1877

12A.3.5 Measurements Period Requirements 1877

12A.4 SL Rx-Tx measurements 1878

12A.4.1 Introduction 1878

12A.4.2 Requirements Applicability 1878

12A.4.3 Measurement Capability 1878

12A.4.4 Measurement Reporting Requirements 1878

12A.4.5 Measurement Period Requirements 1879

12A.5 SL PRS-RSRPP measurements 1880

12A.5.1 Introduction 1880

12A.5.2 Requirements Applicability 1880

12A.5.3 Measurement Capability 1880

12A.5.4 Measurement Reporting Requirements 1880

12A.5.5 Measurement Period Requirements 1880

12A.6 SL AoA measurements 1881

12A.6.1 Introduction 1881

12A.6.2 Requirements Applicability 1881

12A.6.3 Measurement Capability 1881

12A.6.4 Measurement Reporting Requirements 1881

12A.6.5 Measurement Period Requirements 1882

12A.7 SL RTOA measurements 1882

12A.7.1 Introduction 1882

12A.7.2 Requirements Applicability 1883

12A.7.3 Measurement Capability 1883

12A.7.4 Measurement Reporting Requirements 1883

12A.7.5 Measurement Period Requirements 1883

13 Measurement Performance Requirements for NR gNB 1884

13.1 UL-RTOA 1884

13.1.1 Report mapping 1884

13.1.1A Additional Path Report Mapping for UL-RTOA 1888

13.2 gNB Rx-Tx time difference 1891

13.2.1 Report mapping 1891

13.2.1A Additional Path Report Mapping for gNB Rx-Tx 1895

13.2.2 Measurement Accuracy Requirements 1898

13.2.2.1 Introduction 1898

13.2.2.2 Requirements 1899

13.3 UL SRS RSRP measurement 1900

13.3.1 Report mapping 1900

13.3.2 Measurement accuracy requirements 1900

13.3.2.1 Introduction 1900

13.3.2.2 Requirements 1901

13.4 AoA/ZoA 1901

13.4.1 Report mapping 1901

13.5 Timing advance (TADV) 1902

13.5.1 Report mapping 1902

13.6 UL SRS RSRPP measurement 1903

13.6.1 Report mapping 1903

13.7 gNB Rx-Tx time difference measurements for RTT-based PDC 1903

13.7.1 Report mapping 1903

13.7.2 Measurement Accuracy Requirements 1904

13.7.2.1 Introduction 1904

13.7.2.2 Requirements 1904

13.8 UL-RSCP measurement 1905

13.8.1 Report mapping 1905

13.9 UL SRS-TDCT measurement 1905

13.9.1 Report mapping 1905

13.10 UL SRS-TDCP measurement 1908

13.10.1 Report mapping 1908

Annex A (normative): Test Cases 1910

A.1 Purpose of annex 1910

A.2 Requirement classification for statistical testing 1910

A.2.1 Types of requirements in TS 38.133 1910

A.2.1.1 Time and delay requirements on UE higher layer actions 1910

A.2.1.2 Measurements of power levels, relative powers and time 1911

A.2.1.3 Implementation requirements 1911

A.2.1.4 Physical layer timing requirements 1911

A.2.1.5 Requirements under CCA 1911

A.3 RRM test configurations 1912

A.3.1 Reference measurement channels 1912

A.3.1.1 PDSCH 1912

A.3.1.1.1 FDD 1912

A.3.1.1.2 TDD 1913

A.3.1.2 CORESET for RMSI scheduling 1916

A.3.1.2.1 FDD 1916

A.3.1.2.2 TDD 1917

A.3.1.3 CORESET for RMC scheduling 1919

A.3.1.3.1 FDD 1919

A.3.1.3.2 TDD 1921

A.3.1.4 TDD UL/DL configuration 1925

A.3.1A Reference measurement channels under CCA 1928

A.3.1A.1 PDSCH 1928

A.3.1A.1.1 TDD 1928

A.3.1A.2 CORESET for RMSI scheduling 1929

A.3.1A.2.1 TDD 1929

A.3.1A.3 CORESET for RMC scheduling 1930

A.3.1A.3.1 TDD 1930

A.3.1A.4 TDD UL/DL configuration 1930

A.3.1A.5 RMC burst transmission model 1931

A.3.2.1 Generic OFDMA Channel Noise Generator (OCNG) 1931

A.3.2.1.1 OCNG pattern 1: Generic OCNG pattern for all unused REs 1931

A.3.2.1.2 OCNG pattern 2: Generic OCNG pattern for all unused REs for 2AoA setup 1932

A.3.2.1.3 OCNG pattern 3: Generic OCNG pattern for unused REs in the same bandwidth as CORESET 1932

A.3.2.1.4 OCNG pattern 4: Generic OCNG pattern for all unused REs outside SSB slot(s) 1933

A.3.2.2 Void 1934

A.3.3 Reference DRX configurations 1934

A.3.3.1 DRX Configuration 1: DRX cycle = 40 ms and TAT = 500 ms 1934

A.3.3.2 DRX Configuration 2: DRX cycle = 640 ms and TAT = 500 ms 1934

A.3.3.3 DRX Configuration 3: DRX cycle = 40 ms and TAT = Infinity 1934

A.3.3.4 DRX Configuration 4: DRX cycle = 160 ms and TAT = Infinity 1935

A.3.3.5 DRX Configuration 5: DRX cycle = 320 ms and TAT = Infinity 1935

A.3.3.6 DRX Configuration 6: DRX cycle = 320 ms and TAT = 500 ms 1935

A.3.3.7 DRX Configuration 7: DRX cycle = 640 ms and TAT = Infinity 1935

A.3.3.8 DRX Configuration 8: DRX cycle = 320 ms and TAT = Infinity 1936

A.3.3.9 DRX Configuration 9: DRX cycle = 40 ms and TAT = 500 ms 1936

A.3.3.10 DRX Configuration 10: DRX cycle = 640 ms and TAT = 500 ms 1936

A.3.3.11 DRX Configuration 11: DRX cycle = 20 ms and TAT = Infinity 1936

A.3.3.12 DRX Configuration 12: DRX cycle = 640 ms and TAT = Infinity 1937

A.3.3.13 DRX Configuration X1: DRX cycle = 80 ms and TAT = Infinity 1937

A.3.3.14 DRX Configuration 14: DRX cycle = 160 ms and TAT = Infinity 1937

A.3.4 Test Cases with Different Channel Bandwidths 1937

A.3.4.1 Test Cases with Different E-UTRA Channel Bandwidths 1937

A.3.4.1.1 Introduction 1937

A.3.4.1.2 Principle of testing 1938

A.3.5 Test Cases for Synchronous and Asynchronous DC Operations 1938

A.3.5.1 EN-DC Test Cases for Synchronous and Asynchronous EN-DC Operations 1938

A.3.5.1.1 Introduction 1938

A.3.5.1.2 Principle of Testing 1938

A.3.6 Antenna configurations 1938

A.3.6.1 Antenna configurations for FR1 1938

A.3.6.1.1 Antenna connection for 4 Rx capable UEs 1938

A.3.6.1.1.1 Introduction 1938

A.3.6.1.1.2 Principle of testing 1938

A.3.6.1.2 Antenna connection for 8 Rx capable UEs 1941

A.3.6.1.2.1 Introduction 1941

A.3.6.1.2.2 Principle of testing 1941

A.3.6.1.3 Antenna connection for 6 Rx capable UEs 1943

A.3.6.1.3.1 Introduction 1943

A.3.6.1.3.2 Principle of testing 1943

A.3.6.2 Antenna configurations for FR2 1944

A.3.6A Antenna configurations with unlicensed bands 1944

A.3.6A.1 Antenna configurations for FR1 1944

A.3.6A.1.1 Antenna connection for 4 Rx capable UEs 1944

A.3.6A.1.1.1 Introduction 1944

A.3.6A.1.1.2 Principle of testing 1944

A.3.7 EN-DC test setup 1946

A.3.7.1 Introduction 1946

A.3.7.2 E-UTRAN Serving Cell Parameters 1946

A.3.7.2.1 E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR1 1946

A.3.7.2.2 E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR2 1947

A.3.7A NR FR1-FR2 test setup 1948

A.3.7B EN-DC test setup with unlicensed bands 1948

A.3.7B.1 Introduction 1948

A.3.7B.2 E-UTRAN Serving Cell Parameters 1948

A.3.7B.2.1 E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) under CCA in FR1 1948

A.3.7C LTE-FR1/FR2 test setup 1949

A.3.7D NE-DC test setup 1950

A.3.7D.1 Introduction 1950

A.3.7D.2 E-UTRAN Serving Cell Parameters 1950

A.3.7D.2.1 E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR1 1950

A.3.7D.2.2 E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR2 1950

A.3.8 PRACH configurations 1950

A.3.8.1 Introduction 1950

A.3.8.2 PRACH configurations in FR1 1950

A.3.8.2.1 FR1 PRACH configuration 1 1950

A.3.8.2.2 FR1 PRACH configuration 2 1951

A.3.8.2.3 FR1 PRACH configuration 3 1951

A.3.8.2.4 FR1 PRACH configuration 4 1952

A.3.8.2.5 FR1 PRACH configuration 5 1952

A.3.8.2.6 FR1 PRACH configuration 6 1953

A.3.8.3 PRACH configurations in FR2 1953

A.3.8.3.1 FR2 PRACH configuration 1 1953

A.3.8.3.2 FR2 PRACH configuration 2 1954

A.3.8.3.3 FR2 PRACH configuration 3 1955

A.3.8.3.4 FR2 PRACH configuration 4 1955

A.3.8.3.5 FR2 PRACH configuration 5 1956

A.3.8.3.6 FR2 PRACH configuration 6 1956

A.3.8A PRACH configurations under CCA 1957

A.3.8A.1 Introduction 1957

A.3.8A.2 PRACH configurations in FR1 1957

A.3.8A.2.1 FR1 PRACH configuration 1 under CCA 1957

A.3.8A.2.2 FR1 PRACH configuration 2 under CCA 1958

A.3.9 BWP configurations 1959

A.3.9.1 Introduction 1959

A.3.9.2 Downlink BWP configurations 1959

A.3.9.2.1 Initial BWP 1959

A.3.9.2.2 Dedicated BWP 1960

A.3.9.3 Uplink BWP configurations 1960

A.3.9.3.1 Initial BWP 1960

A.3.9.3.2 Dedicated BWP 1961

A.3.9A BWP configurations for RedCap 1961

A.3.9A.1 Introduction 1961

A.3.9A.2 Downlink BWP configurations 1961

A.3.9A.2.1 Dedicated BWP 1961

A.3.9A.3 Uplink BWP configurations 1962

A.3.9A.3.1 Dedicated BWP 1962

A.3.10 SSB Configurations 1962

A.3.10.1 SSB Configurations for FR1 1962

A.3.10.1.1 SSB pattern 1 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz 1962

A.3.10.1.5 SSB pattern 5 in FR1: SSB allocation for SSB SCS=15 kHz starting from odd SFN in 10 MHz 1964

A.3.10.1.6 SSB pattern 6 in FR1: SSB allocation for SSB SCS=30 kHz starting from odd SFN in 40 MHz 1964

A.3.10.1.7 SSB pattern 7 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz 1964

A.3.10.1.8 SSB pattern 8 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz 1965

A.3.10.1.9 SSB pattern 9 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz 1965

A.3.10.1.10 SSB pattern 10 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz 1965

A.3.10.1.11 SSB pattern 11 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz 1966

A.3.10.1.12 SSB pattern 12 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz 1966

A.3.10.1.13 SSB pattern 13 in FR1: SSB allocation for SSB SCS=15 kHz in 3 MHz 1966

A.3.10.1.14 SSB pattern 14 in FR1: SSB allocation for SSB SCS=15 kHz with 160 ms periodicity in 10MHz 1967

A.3.10.1.15 SSB pattern 15 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz 1967

A.3.10.1.16 SSB pattern 16 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz 1967

A.3.10.1.17 SSB pattern 17 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz 1968

A.3.10.1.18 SSB pattern 18 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz 1968

A.3.10.1.19 SSB pattern 19 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz 1968

A.3.10.1.20 SSB pattern 20 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz 1969

A.3.10.1.21 SSB pattern 21 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz 1969

A.3.10.1.23 SSB pattern 23 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz 1970

A.3.10.1.24 SSB pattern 24 in FR1: SSB allocation for SSB SCS=30 kHz in 100 MHz 1970

A.3.10.2 SSB Configurations for FR2 1971

A.3.10.2.1 SSB pattern 1 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1971

A.3.10.2.2 SSB pattern 2 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1971

A.3.10.2.3 SSB pattern 3 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1972

A.3.10.2.4 SSB pattern 4 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1972

A.3.10.2.5 SSB pattern 5 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1973

A.3.10.2.6 SSB pattern 6 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1973

A.3.10.2.7 SSB pattern 7 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1973

A.3.10.2.8 SSB pattern 8 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1974

A.3.10.2.9 SSB pattern 9 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1974

A.3.10.2.10 SSB pattern 10 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1974

A.3.10.2.19 SSB pattern 19 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1979

A.3.10.2.20 SSB pattern 20 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1979

A.3.10.2.21 SSB pattern 21 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1980

A.3.10.2.22 SSB pattern 22 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1980

A.3.10.2.23 SSB pattern 23 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1980

A.3.10.2.24 SSB pattern 24 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1981

A.3.10.2.25 SSB pattern 25 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1981

A.3.10.2.26 SSB pattern 26 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1981

A.3.10.2.27 SSB pattern 27 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1982

A.3.10.2.28 SSB pattern 28 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1982

A.3.10.2.29 SSB pattern 29 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1982

A.3.10.2.30 SSB pattern 30 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1983

A.3.10.2.31 SSB pattern 31 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1983

A.3.10.2.32 SSB pattern 32 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1983

A.3.10.2.33 SSB pattern 33 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1984

A.3.10.2.34 SSB pattern 34 in FR2: SSB allocation for SSB SCS=120 kHz in 200 MHz 1984

A.3.10A SSB Configurations under CCA 1985

A.3.10A.1 SSB Configurations under CCA for FR1 1985

A.3.10A.1.1 SSB pattern 1 under CCA for semi-static channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz 1985

A.3.10A.1.2 SSB pattern 2 under CCA for dynamic channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz 1985

A.3.10A.1.3 SSB pattern 3 under CCA for semi-static channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz 1986

A.3.10A.1.4 SSB pattern 4 under CCA for dynamic channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz 1986

A.3.10B SSB Configurations for RedCap 1987

A.3.10B.1 SSB Configurations for FR1 1987

A.3.10B.1.1 SSB pattern 1 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz 1987

A.3.10B.1.2 SSB pattern 2 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz 1987

A.3.10B.1.3 SSB pattern 3 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz starting from odd SFN in 20 MHz 1988

A.3.10B.1.4 SSB pattern 4 for RedCap in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz 1988

A.3.10B.1.5 SSB pattern 5 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz 1989

A.3.10B.1.6 SSB pattern 6 for RedCap in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz 1989

A.3.10B.1.7 SSB pattern 7 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz 1990

A.3.10B.2 SSB Configurations for FR2 1990

A.3.10B.2.1 SSB pattern 1 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1990

A.3.10B.2.2 SSB pattern 2 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1991

A.3.10B.2.3 SSB pattern 3 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1991

A.3.10B.2.4 SSB pattern 4 for RedCap in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1992

A.3.10B.2.5 SSB pattern 5 for RedCap in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1992

A.3.11 SMTC Configurations 1992

A.3.11.1 SMTC pattern 1: SMTC period = 20 ms with SMTC duration = 1 ms 1992

A.3.11.2 SMTC pattern 2: SMTC period = 20 ms with SMTC duration = 5 ms 1993

A.3.11.3 SMTC pattern 3: SMTC period = 160 ms with SMTC duration = 1 ms 1993

A.3.11.4 SMTC pattern 4: SMTC period = 20 ms with SMTC duration = 1 ms 1993

A.3.11.5 SMTC pattern 5: SMTC period = 20 ms with SMTC duration = 5 ms 1993

A.3.11.6 SMTC pattern 6: SMTC period = 20 ms with SMTC duration = 5 ms 1993

A.3.11.7 SMTC pattern 7: SMTC period = 20 ms with SMTC duration = 5 ms 1993

A.3.11.8 SMTC pattern 8: SMTC period = 10 ms with SMTC duration = 1 ms 1994

A.3.11.9 SMTC pattern 9: SMTC period = 20 ms with SMTC duration = 1 ms 1994

A.3.11.10 SMTC pattern 10: SMTC period = 80 ms with SMTC duration = 1 ms 1994

A.3.11.11 SMTC pattern 11: SMTC period = 80 ms with SMTC duration = 5 ms 1994

A.3.11.12 SMTC pattern 12: SMTC period = 20 ms with SMTC duration = 5 ms 1994

A.3.11.13 SMTC pattern 13: SMTC period = 160 ms with SMTC duration = 1 ms 1995

A.3.11.14 SMTC pattern 14: SMTC period = 20 ms with SMTC duration = 1 ms 1995

A.3.11A SMTC Configurations for RedCap 1995

A.3.11A.0 Introduction 1995

A.3.11A.1 SMTC pattern 1 for RedCap: SMTC period = 40 ms with SMTC duration = 1 ms 1995

A.3.11A.2 SMTC pattern 2 for RedCap: SMTC period = 80 ms with SMTC duration = 1 ms 1995

A.3.11A.3 SMTC pattern 3 for RedCap: SMTC period = 40 ms with SMTC duration = 1 ms 1996

A.3.11A.4 SMTC pattern 4 for RedCap: SMTC period = 80 ms with SMTC duration = 5 ms 1996

A.3.12 Test Cases with Different CC Configurations 1996

A.3.12.1 EN-DC Test Cases with Different EN-DC Configurations 1996

A.3.12.1.1 Introduction 1996

A.3.12.1.2 Principle of testing 1996

A.3.12.2 Carrier Aggregation Test Cases with Different CA Configurations 1996

A.3.12.2.1 Introduction 1996

A.3.12.2.2 Principle of testing 1997

A.3.13 Test Cases in SA and EN-DC Operations 1997

A.3.13.1 Introduction 1997

A.3.13.2 Principle of Testing 1997

A.3.13B  Test Cases for EN-DC and NE-DC Operations 1998

A.3.13B.1 Active BWP switch Test Cases for EN-DC and NE-DC Operations 1998

A.3.13B.1.1 Introduction 1998

A.3.13B.1.2 Principle of Testing 1998

A.3.13B.2 SFTD accuracy Test Cases for EN-DC and NE-DC Operations 1998

A.3.13B.2.1 Introduction 1998

A.3.13B.2.2 Principle of Testing 1998

A.3.14 CSI-RS configurations 1999

A.3.14.1 FDD 1999

A.3.14.2 TDD 2001

A.3.15 Angle of Arrival (AoA) for FR2 RRM test cases 2006

A.3.15.1 Setup 1: Single AoA in Rx beam peak direction 2006

A.3.15.2 Setup 2: Single AoA in non Rx beam peak direction 2006

A.3.15.2.1 Setup 2a: Single AoA in non Rx beam peak direction without change in direction 2006

A.3.15.2.2 Setup 2b: Single AoA in non Rx beam peak direction with change in direction 2007

A.3.15.3 Setup 3: 2 AoAs 2007

A.3.15.4 Setup 4: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak 2007

A.3.15.4.1 Setup 4a: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak without change in direction 2007

A.3.15.4.2 Setup 4b: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak with change in direction 2007

A.3.15.4.3 Setup 4c: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak for power class 6 UE supporting simultaneous reception from multiple directions 2007

A.3.15.5 Setup 5: 2 AoAs for simultaneous reception with QCL Type-D 2008

A.3.15.6 Setup 6: 3 AoAs for simultaneous reception with different QCL Type-D 2008

A.3.15.7 Setup 7: 3 AoAs 2008

A.3.15.8 Setup 8: 4 AoAs 2008

A.3.15C Angle of Arrival (AoA) for FR2-NTN RRM test cases 2008

A.3.15C.1 Setup 1: Single AoA 2009

A.3.15C.2 Setup 2: 2 AoAs 2009

A.3.16 TCI State Configuration 2009

A.3.16.1 Introduction 2009

A.3.16.2 TCI states 2009

A.3.16A Unified TCI State Configuration 2009

A.3.16A.1 Introduction 2009

A.3.16A.2 DLorJoint TCI states 2010

A.3.16A.3 UL TCI states 2011

A.3.16B  LTM Candidate TCI State Configuration 2011

A.3.16B.1 Introduction 2011

A.3.16B.2 LTM candidate DLorJoint TCI states 2012

A.3.16B.3 LTM candidate UL TCI states 2012

A.3.17 Configurations of CSI-RS for tracking 2013

A.3.17.1 Configuration of CSI-RS for tracking for FR1 2013

A.3.17.1.1 FDD 2013

A.3.17.1.2 TDD 2016

A.3.17.2 Configuration of CSI-RS for tracking for FR2 2020

A.3.17.2.1 TDD 2020

A.3.17.2.2 FDD 2023

A.3.18 Additional definitions related to OTA testing for FR2 RRM test cases 2023

A.3.18.1 Introduction 2023

A.3.18.2 PRACH Power Measurement 2024

A.3.19 Test applicability for DAPS handover 2024

A.3.19.1 Introduction 2024

A.3.19.2 Principle of testing 2024

A.3.20 MsgA configurations 2024

A.3.20.1 Introduction 2024

A.3.20.2 MsgA configurations in FR1 2024

A.3.20.2.1 FR1 MsgA configuration 1 2024

A.3.20.2.2 FR1 MsgA configuration 2 2025

A.3.20.3 MsgA configurations in FR2 2026

A.3.20.3.1 FR2 MsgA configuration 1 2026

A.3.20.3.2 FR2 MsgA configuration 2 2027

A.3.20A MsgA configurations under CCA 2028

A.3.20A.1 Introduction 2028

A.3.20A.2 MsgA configurations in FR1 2028

A.3.20A.2.1 FR1 MsgA configuration 1 under CCA 2028

A.3.20A.2.2 FR1 MsgA configuration 2 under CCA 2029

A.3.21 V2X sidelink communication 2030

A.3.21.1 Introduction 2030

A.3.21.2 Reference resource pool configurations for V2X Sidelink Communication 2031

A.3.21.3 Reference measurement channels for V2X Sidelink Communication 2034

A.3.21.4 Reference SL-DRX configurations 2035

A.3.21.4.1 SL-DRX Configuration 1: SL-DRX cycle = 40 ms 2035

A.3.21.4.2 SL-DRX Configuration 2: SL-DRX cycle = 320 ms 2035

A.3.21.4.3 SL-DRX Configuration 3: SL-DRX cycle = 640 ms 2035

A.3.21A NR Sidelink Measurements for Positioning 2035

A.3.21A.1 Introduction 2035

A.3.21A.2 NR SL-PRS configurations 2036

A.3.21A.2.1 NR SL-PRS configurations for FR1 2036

A.3.22 CSI-IM configurations 2036

A.3.22.1 FDD 2036

A.3.22.2 TDD 2036

A.3.23 Spatial Relation Configuration 2037

A.3.23.1 Introduction 2037

A.3.23.2 Spatial Relation 2038

A.3.24 SRS configuration 2038

A.3.25 Channel bandwidth (CBW) configurations 2040

A.3.25.1 DL UE specific CBW 2040

A.3.25.2 UL UE specific CBW 2041

A.3.26 CCA model 2041

A.3.26.1 Introduction 2041

A.3.26.2 CCA model for operation on a carrier frequency with CCA in FR1 2041

A.3.26.2.1 DL CCA model 2041

A.3.26.2.2 UL CCA model 2042

A.3.26.3 CCA model for operation on a carrier frequency with CCA in FR2-2 2043

A.3.26.3.1 DL CCA model 2043

A.3.26.3.2 UL CCA model 2043

A.3.26.4 CCA model for operation on a sidelink carrier frequency with CCA 2044

A.3.26.4.1 CCA model for SyncRef UE 2044

A.3.27 Void 2045

A.3.27.1 Void 2045

A.3.27.2 Void 2045

A.3.27.3 Void 2045

A.3.27.4 Void 2045

A.3.27.5 Void 2045

A.3.28 Discovery Burst Transmission Window configuration under CCA 2045

A.3.28.1 DBT Window pattern 1: DBT Window period = 20 ms with DBT Window duration = 1 ms 2045

A.3.29 Testing principles for UE capable of only NR bands with shared spectrum access 2045

A.3.29.1 Introduction 2045

A.3.29.2 Principle of testing for UE capable of EN-DC with only NR bands with shared spectrum access 2045

A.3.29.3 Principle of testing for UE capable of SA operation with only NR bands with shared spectrum access 2046

A.3.30 CSI-RS configurations for RRM 2046

A.3.30.1 FDD 2046

A.3.30.2 TDD 2047

A.3.31 PRS Configurations 2048

A.3.31.1 PRS Configurations for FR1 2048

A.3.31.1.1 PRS pattern 1 in FR1: SCS=15 kHz 2048

A.3.31.1.2 PRS pattern 2 in FR1: SCS=30 kHz 2049

A.3.31.2 PRS Configurations for FR2 2050

A.3.31.2.1 PRS pattern 1 in FR2: SCS=120 kHz 2050

A.3.32 NR sidelink discovery 2050

A.3.32.1 Introduction 2050

A.3.32.2 Reference resource pool configurations for NR Sidelink Discovery 2050

A.3.32.3 Principle of Testing 2051

A.3.33 PRS Processing Window (PPW) configurations 2051

A.3.34 Testing principles for test cases related to PRS measurements 2051

A.3.34.1 Introduction 2051

A.3.34.2 Test cases in RRC_INACTIVE state 2051

A.3.34.3 Test cases for PRS measurements with gaps in RRC_CONNECTED state 2052

A.3.34.4 Test cases for PRS measurements without gaps in RRC_CONNECTED state 2052

A.3.34.5 Testing principles for positioning measurements by aggregating PRS resources from multiple PFLs 2052

A.3.34.6 Testing principles for carrier phase measurement for positioning 2053

A.3.34.7 Test cases in RRC_IDLE state 2053

A.3.35 Testing principle for RedCap UE 2053

A.3.35.1 Introduction 2053

A.3.35.2 Principle of testing for FR1 2053

A.3.35.3 Principle of testing for FR2 2053

A.3.35.4 Principle of testing for PRS measurement 2053

A.3.36 Testing related to Satellite access 2054

A.3.36.1 Introduction 2054

A.3.36.2 Principle of testing GSO and NGSO scenarios 2054

A.3.36.3 Principle of testing different RRM requirements 2054

A.3.36.4 Principle of testing different ephemeris formats 2055

A.3.36.5 General setup for SIB19 2057

A.3.36.6 Satellite specific parameters configuration 2058

A.3.36.6.1 Satellite specific configuration for serving cell 2058

A.3.36.6.2 Satellite specific configuration for neighbour cell 2058

A.3.37 Reference Cell DTX configurations 2059

A.3.37.1 Cell DTX Configuration 1: Cell DTX cycle = 160 ms and TAT = Infinity 2059

A.3.38 DL-PRS Measurement Time Window configurations 2059

A.3.39 Testing related to RedCap UE with Satellite Access 2059

A.3.39.1 Introduction 2059

A.3.39.2 Principle of testing 1Rx and 2Rx (e)RedCap UE in FR1 2060

A.3.39.3 Principle of testing GSO and NGSO scenarios 2060

A.3.39.4 Principle of testing different RRM requirements 2060

A.3.39.5 Principle of testing HD-FDD RedCap UE 2061

A.3.39.6 Principle of testing different ephemeris formats 2061

A.3.39.7 General setup for SIB19 2063

A.3.39.8 Satellite specific parameters configuration 2064

A.3.39.8.1 Satellite specific configuration for serving cell 2064

A.3.39.8.2 Satellite specific configuration for neighbour cell 2064

A.3.40 Testing principles for eEMR based fast SCell activation 2065

A.3.40.1 Introduction 2065

A.3.40.2 Principle of testing 2065

A.3.41 Test configurations related to SBFD 2065

A.3.41.1 SBFD configurations for FR1 2065

A.3.41.1.0 Introduction 2065

A.3.41.1.1 SBFD.1 FR1 2066

A.3.41.1.2 SBFD.2 FR1 2066

A.3.41.2 SBFD configurations for FR2 2066

A.3.41.2.0 Introduction 2066

A.3.41.2.1 SBFD.1 FR2 2066

A.3.41.2.2 SBFD.2 FR2 2067

A.3.41.3 Principle of testing L1-RSRP and L1-SINR measurements 2067

A.3.41.4 Collision configurations between CSI-RS and UL scheduling for SBFD 2067

A.3.41.5 Configurations of DL RMC for SBFD 2067

A.3.41.6 Configurations of OCNG for SBFD 2067

A.3.41.7 Configuration of Noc for SBFD 2067

A.3.42 LP-SS configurations 2068

A.3.42.1 LP-SS Configuration 1: M=1 2068

A.3.42.2 LP-SS Configuration 2: M=4 2068

A.3.43 Test conditions for AI/ML 2068

A.3.43.1 Channel models for AI/ML based Beam Management FR2 2068

A.4 EN-DC tests with all NR cells in FR1 2070

A.4.1 Void 2070

A.4.2 Void 2070

A.4.3 RRC_CONNECTED state mobility 2070

A.4.3.1 Void 2070

A.4.3.2 RRC Connection Mobility Control 2070

A.4.3.2.1 Void 2070

A.4.3.2.2 Random Access 2070

A.4.3.2.2.1 4-step RA type contention based random access test in FR1 for PSCell in EN-DC 2070

A.4.3.2.2.2 4-step RA type n on-contention based random access test in FR1 for PSCell in EN-DC 2073

A.4.3.2.2.3 2-step RA type contention based random access test in FR1 for PSCell in EN-DC 2076

A.4.3.2.2.4 2-step RA type non-contention based random access test in FR1 for PSCell in EN-DC 2078

A.4.3.2.3 Void 2080

A.4.3.3 Handover with PSCell from EN-DC to EN-DC with known target PSCell in FR1 2080

A.4.3.3.1 Test Purpose and Environment 2080

A.4.3.3.2 Test Requirements 2084

A.4.4 Timing 2084

A.4.4.1 UE transmit timing 2084

A.4.4.1.1 NR UE Transmit Timing Test for FR1 2084

A.4.4.1.1.1 Test Purpose and environment 2084

A.4.4.1.1.2 Test requirements 2087

A.4.4.1.2 NR UE Transmit Timing Test for two TRPs in FR1 2087

A.4.4.1.2.1 Test Purpose and environment 2087

A.4.4.1.2.2 Test requirements 2090

A.4.4.1.3 NR UE Transmit Timing Test with 2-TA and two TRPs for FR1 UE supporting single DCI 2091

A.4.4.1.3.1 Test Purpose and environment 2091

A.4.4.1.3.2 Test requirements 2093

A.4.4.2 UE timer accuracy 2094

A.4.4.3 Timing advance 2094

A.4.4.3.1 EN-DC FR1 timing advance adjustment accuracy 2094

A.4.4.3.1.1 Test Purpose and Environment 2094

A.4.4.3.1.2 Test Parameters 2094

A.4.4.3.1.3 Test Requirements 2097

A.4.4.3.2 EN-DC FR1 timing advance adjustment accuracy for asymmetric DL sTRP/UL mTRP deployment with two TAs 2097

A.4.4.3.2.1 Test Purpose and Environment 2097

A.4.4.3.2.2 Test Parameters 2097

A.4.4.3.2.3 Test Requirements 2100

A.4.5 Signaling characteristics 2100

A.4.5.1 Radio link Monitoring 2100

A.4.5.1.1 Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode 2100

A.4.5.1.1.1 Test Purpose and Environment 2100

A.4.5.1.1.2 Test Requirements 2104

A.4.5.1.2 Radio Link Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode 2104

A.4.5.1.2.1 Test Purpose and Environment 2104

A.4.5.1.2.2 Test Requirements 2107

A.4.5.1.3 Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode 2107

A.4.5.1.3.1 Test Purpose and Environment 2107

A.4.5.1.3.2 Test Requirements 2110

A.4.5.1.4 Radio Link Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode 2110

A.4.5.1.4.1 Test Purpose and Environment 2110

A.4.5.1.4.2 Test Requirements 2113

A.4.5.1.5 EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode 2113

A.4.5.1.5.1 Test Purpose and Environment 2113

A.4.5.1.5.2 Test Requirements 2116

A.4.5.1.6 EN-DC Radio Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode 2117

A.4.5.1.6.1 Test Purpose and Environment 2117

A.4.5.1.6.2 Test Requirements 2119

A.4.5.1.7 EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in DRX mode 2120

A.4.5.1.7.1 Test Purpose and Environment 2120

A.4.5.1.7.2 Test Requirements 2122

A.4.5.1.8 EN-DC Radio Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM in DRX mode 2123

A.4.5.1.8.1 Test Purpose and Environment 2123

A.4.5.1.8.2 Test Requirements 2126

A.4.5.1.9 Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS for UE fulfilling relaxed measurement criterion 2126

A.4.5.1.9.1 Test Purpose and Environment 2126

A.4.5.1.10 EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP 2129

A.4.5.1.10.1 Test Purpose and Environment 2129

A.4.5.1.11 Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP 2129

A.4.5.1.11.1 Test Purpose and Environment 2129

A.4.5.1.11.2 Test Requirements 2130

A.4.5.1.12 EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP 2130

A.4.5.1.12.1 Test Purpose and Environment 2130

A.4.5.1.12.2 Test Requirements 2133

A.4.5.2 Interruption 2133

A.4.5.2.1 E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in synchronous EN-DC 2133

A.4.5.2.1.1 Test Purpose and Environment 2133

A.4.5.2.1.2 Test Requirements 2135

A.4.5.2.2 E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC 2135

A.4.5.2.2.1 Test Purpose and Environment 2135

A.4.5.2.2.2 Test Requirements 2137

A.4.5.2.3 E-UTRAN – NR FR1 interruptions during measurements on deactivated NR SCC in synchronous EN-DC 2137

A.4.5.2.3.1 Test Purpose and Environment 2137

A.4.5.2.3.2 Test Requirements 2141

A.4.5.2.4 E-UTRAN – NR FR1 interruptions during measurements on deactivated NR SCC in asynchronous EN-DC 2142

A.4.5.2.4.1 Test Purpose and Environment 2142

A.4.5.2.4.2 Test Requirements 2146

A.4.5.2.5 E-UTRAN – NR FR1 interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC 2146

A.4.5.2.5.1 Test Purpose and Environment 2146

A.4.5.2.5.2 Test Requirements 2148

A.4.5.2.6 E-UTRAN – NR FR1 interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC 2149

A.4.5.2.6.1 Test Purpose and Environment 2149

A.4.5.2.6.2 Test Requirements 2151

A.4.5.2.7 Void 2151

A.4.5.2.8 E-UTRAN - NR FR1 interruptions at NR SRS carrier based switching in asynchronous EN-DC 2151

A.4.5.2.8.1 Test Purpose and Environment 2151

A.4.5.2.8.2 Test Requirements 2154

A.4.5.2.9 E-UTRAN – NR interruptions at E-UTRA SRS carrier based switching 2154

A.4.5.2.9.1 Test Purpose and Environment 2154

A.4.5.2.9.2 Test Requirements 2157

A.4.5.2.10 E-UTRAN – NR FR1 interruptions due to RRM and RLM/BFD measurements on deactivated NR PSCell 2157

A.4.5.2.10.1 Test Purpose and Environment 2157

A.4.5.2.10.2 Test Requirements 2159

A.4.5.2.11 E-UTRAN - NR FR1 interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in synchronous EN-DC 2159

A.4.5.2.11.1 Test Purpose and Environment 2159

A.4.5.2.11.2 Test Requirements 2163

A.4.5.2.12 E-UTRAN - NR FR1 interruptions at NR SRS antenna port switching in asynchronous EN-DC 2164

A.4.5.2.12.1 Test Purpose and Environment 2164

A.4.5.3 SCell Activation and Deactivation Delay 2170

A.4.5.3.1 SCell Activation and deactivation of known SCell in FR1 for 160 ms SCell measurement cycle 2170

A.4.5.3.1.1 Test Purpose and Environment 2170

A.4.5.3.1.2 Test Requirements 2175

A.4.5.3.2 SCell Activation and deactivation of known SCell in FR1 for 640 ms SCell measurement cycle 2176

A.4.5.3.2.1 Test Purpose and Environment 2176

A.4.5.3.2.2 Test Requirements 2176

A.4.5.3.3 SCell Activation and deactivation of unknown SCell in FR1 2176

A.4.5.3.3.1 Test Purpose and Environment 2176

A.4.5.3.3.2 Test Requirements 2177

A.4.5.3.4 SCell Activation and deactivation of multiple unknown SCells in FR1 with single activation/deactivation command 2177

A.4.5.3.4.1 Test Purpose and Environment 2177

A.4.5.3.4.2 Test Requirements 2179

A.4.5.3.5 Direct SCell activation at SCell addition of known SCell in FR1 2180

A.4.5.3.5.1 Test Purpose and Environment 2180

A.4.5.3.5.2 Test Requirements 2184

A.4.5.3.6 Fast SCell Activation of known SCell in FR1 for 160 ms SCell measurement cycle 2184

A.4.5.3.6.1 Test Purpose and Environment 2184

A.4.5.3.6.2 Test Requirements 2188

A.4.5.3.7 Fast SCell Activation of known SCell in FR1 for 640 ms SCell measurement cycle 2188

A.4.5.3.7.1 Test Purpose and Environment 2188

A.4.5.3.7.2 Test Requirements 2188

A.4.5.3.8 SCell Activation and deactivation of unknown SCell in FR1 for UE capable of short measurement interval 2189

A.4.5.3.8.1 Test Purpose and Environment 2189

A.4.5.3.8.2 Test Requirements 2190

A.4.5.3.9 SCell Activation of unknown SCell with valid L3 measurement results in FR1 for 160 ms SCell measurement cycle 2190

A.4.5.3.9.1 Test Purpose and Environment 2190

A.4.5.3.9.2 Test Requirements 2195

A.4.5.3.10 SCell Activation of multiple unknown SCells in FR1 with L3 reporting with single activation/deactivation command in non-DRX 2196

A.4.5.3.10.1 Test Purpose and Environment 2196

A.4.5.3.10.2 Test Requirements 2198

A.4.5.3.11 TRS-based SCell Activation of SSB-less SCell in FR1 collocated inter-band 2199

A.4.5.3.11.1 Test Purpose and Environment 2199

A.4.5.3.11.2 Test Requirements 2202

A.4.5.3.12 Inter-band SSB-less Scell activation using A-TRS 2203

A.4.5.3.12.1 Test Purpose and Environment 2203

A.4.5.3.12.2 Test Requirements 2206

A.4.5.4 UE UL carrier RRC reconfiguration Delay 2206

A.4.5.4.1 UE UL carrier RRC reconfiguration Delay 2206

A.4.5.4.1.1 Test Purpose and Environment 2206

A.4.5.4.1.2 Test Requirements 2211

A.4.5.5 Beam Failure Detection and Link recovery procedures 2211

A.4.5.5.1 EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode 2211

A.4.5.5.1.1 Test Purpose and Environment 2211

A.4.5.5.1.2 Test Requirements 2215

A.4.5.5.2 EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in DRX mode 2215

A.4.5.5.2.1 Test Purpose and Environment 2215

A.4.5.5.2.2 Test Requirements 2218

A.4.5.5.3 EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with CSI-RS-based BFD and LR in non-DRX mode 2219

A.4.5.5.3.1 Test Purpose and Environment 2219

A.4.5.5.3.2 Test Requirements 2222

A.4.5.5.4 EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with CSI-RS-based BFD and LR in DRX mode 2223

A.4.5.5.4.1 Test Purpose and Environment 2223

A.4.5.5.4.2 Test Requirements 2226

A.4.5.5.5 EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode 2227

A.4.5.5.5.1 Test Purpose and Environment 2227

A.4.5.5.5.2 Test Requirements 2230

A.4.5.5.6 EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in DRX mode 2231

A.4.5.5.6.1 Test Purpose and Environment 2231

A.4.5.5.6.2 Test Requirements 2234

A.4.5.5.7 EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode 2235

A.4.5.5.7.1 Test Purpose and Environment 2235

A.4.5.5.7.2 Test Requirements 2238

A.4.5.5.8 EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode 2239

A.4.5.5.8.1 Test Purpose and Environment 2239

A.4.5.5.8.2 Test Requirements 2243

A.4.5.6 Active BWP switch 2243

A.4.5.6.1 DCI-based and Timer-based Active BWP Switch 2243

A.4.5.6.1.1 E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC 2243

A.4.5.6.1.2 E-UTRAN – NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC 2247

A.4.5.6.2 RRC-based Active BWP Switch 2252

A.4.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs 2255

A.4.5.6.3.1 Simultaneous E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in EN-DC on multiple CCs 2255

A.4.5.6.4 Simultaneous RRC-based Active BWP Switch on multiple CCs 2260

A.4.5.6.4.1 E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC on multiple CCs 2260

A.4.5.6.4.1.1 Test Purpose and Environment 2260

A.4.5.6.4.1.2 Test Requirements 2264

A.4.5.6.4.2 E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR1 SCells inside active time 2264

A.4.5.6.4.2.1 Test Purpose and Environment 2264

A.4.5.6.4.2.2 Test Requirements 2270

A.4.5.6.5 SCell dormancy switch 2270

A.4.5.6.5.1 E-UTRAN – NR FR1 PSCell SCell dormancy switch of single FR1 SCell outside active time 2270

A.4.5.6.5.2 E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR1 SCells inside active time 2275

A.4.5.6.5.2.1 Test Purpose and Environment 2275

A.4.5.6.5.2.2 Test Requirements 2279

A.4.5.7 PSCell addition and release delay 2279

A.4.5.7.1 Addition and Release Delay of known NR PSCell 2279

A.4.5.7.1.1 Test purpose and environment 2279

A.4.5.7.1.2 Test Requirements 2282

A.4.5.8 DL Interruptions at switching between two uplink carriers 2282

A.4.5.8.1 Test Purpose and Environment 2282

A.4.5.8.2 Test Requirements 2286

A.4.5.9 UE specific CBW change 2286

A.4.5.9.1 UE specific CBW change on FR1 NR PSCell with non-DRX in synchronous EN- DC 2286

A.4.5.9.1.1 Test Purpose and Environment 2286

A.4.5.9.1.2 Test Requirements 2289

A.4.5.10 PSCell activation and deactivation delay 2289

A.4.5.10.1 PSCell activation and deactivation delay 2289

A.4.5.10.1.1 Test purpose and environment 2289

A.4.5.10.1.2 Test Requirements 2291

A.4.5.11 Conditional PSCell addition and release delay (FR1 EN-DC) 2292

A.4.5.11.1 Conditional PSCell Addition and Release Delay 2292

A.4.5.11.1.1 Test purpose and environment 2292

A.4.5.11.1.2 Test Parameters 2292

A.4.5.11.1.3 Test Requirements 2294

A.4.6 Measurement procedure 2294

A.4.6.1 Intra-frequency Measurements 2294

A.4.6.1.1 EN-DC event triggered reporting tests without gap under non-DRX 2294

A.4.6.1.1.1 Test purpose and Environment 2294

A.4.6.1.1.2 Test parameters 2295

A.4.6.1.1.3 Test Requirements 2296

A.4.6.1.2 EN-DC event triggered reporting tests without gap under DRX 2296

A.4.6.1.2.1 Test purpose and Environment 2297

A.4.6.1.2.2 Test parameters 2297

A.4.6.1.2.3 Test Requirements 2299

A.4.6.1.3 EN-DC event triggered reporting tests with per-UE gaps under non-DRX 2299

A.4.6.1.3.1 Test purpose and Environment 2299

A.4.6.1.3.2 Test parameters 2299

A.4.6.1.3.3 Test Requirements 2301

A.4.6.1.4 EN-DC event triggered reporting tests with per-UE gaps under DRX 2301

A.4.6.1.4.1 Test purpose and Environment 2301

A.4.6.1.4.2 Test parameters 2301

A.4.6.1.4.3 Test Requirements 2303

A.4.6.1.5 EN-DC event triggered reporting tests without gap under non-DRX with SSB index reading 2304

A.4.6.1.5.1 Test purpose and Environment 2304

A.4.6.1.5.2 Test parameters 2304

A.4.6.1.5.3 Test Requirements 2305

A.4.6.1.6 EN-DC event triggered reporting tests with SSB index reading with per-UE gaps 2305

A.4.6.1.6.1 Test purpose and Environment 2305

A.4.6.1.6.2 Test parameters 2305

A.4.6.1.6.3 Test Requirements 2307

A.4.6.1.7 EN-DC event triggered reporting tests under DRX for UE configured with highSpeedMeasFlag-r16 2307

A.4.6.1.7.1 Test purpose and Environment 2307

A.4.6.1.7.2 Test parameters 2307

A.4.6.1.7.3 Test Requirements 2309

A.4.6.1.8 EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with highSpeedMeasCA-Scell-r17 2309

A.4.6.1.8.1 Test Purpose and Environment 2309

A.4.6.1.8.2 Test Requirements 2313

A.4.6.1.9 EN-DC event triggered reporting tests without gap under non-DRX with NCD-SSB 2313

A.4.6.1.9.1 Test purpose and Environment 2313

A.4.6.1.9.2 Test parameters 2313

A.4.6.1.9.3 Test Requirements 2315

A.4.6.1.10 EN-DC event triggered reporting tests without gap under non-DRX when CD-SSB is outside active BWP 2315

A.4.6.110.1 Test purpose and Environment 2315

A.4.6.1.10.2 Test Requirements 2315

A.4.6.2 Inter-frequency Measurements 2315

A.4.6.2.1 EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is not used 2316

A.4.6.2.1.1 Test Purpose and Environment 2316

A.4.6.2.1.2 Test Requirements 2318

A.4.6.2.2 EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used 2318

A.4.6.2.2.1 Test Purpose and Environment 2318

A.4.6.2.2.2 Test Requirements 2321

A.4.6.2.3 Void 2321

A.4.6.2.4 Void 2321

A.4.6.2.5 EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is not used 2321

A.4.6.2.5.1 Test Purpose and Environment 2321

A.4.6.2.5.2 Test Requirements 2324

A.4.6.2.6 EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is used 2324

A.4.6.2.6.1 Test Purpose and Environment 2324

A.4.6.2.6.2 Test Requirements 2326

A.4.6.2.7 Void 2327

A.4.6.2.8 Void 2327

A.4.6.2.9 EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with highSpeedMeasInterFreq-r17 2327

A.4.6.2.9.1 Test Purpose and Environment 2327

A.4.6.2.9.2 Test Requirements 2330

A.4.6.2.10 EN-DC: event triggered reporting tests under non-DRX in FR1 for UE supporting threeCarrierMeasWithoutGap-r19 2330

A.4.6.2.10.1 Test purpose and Environment 2330

A.4.6.2.10.2 Test parameters 2330

A.4.6.2.10.3 Test Requirements 2332

A.4.6.3 Void 2332

A.4.6.4 L1-RSRP measurement for beam reporting 2332

A.4.6.4.1 SSB based L1-RSRP measurement when DRX is not used 2332

A.4.6.4.1.1 Test Purpose and Environment 2332

A.4.6.4.1.2 Test parameters 2333

A.4.6.4.1.3 Test Requirements 2334

A.4.6.4.2 SSB based L1-RSRP measurement when DRX is used 2334

A.4.6.4.2.1 Test Purpose and Environment 2334

A.4.6.4.2.2 Test parameters 2335

A.4.6.4.2.3 Test Requirements 2336

A.4.6.4.3 CSI-RS based L1-RSRP measurement when DRX is not used 2336

A.4.6.4.3.1 Test Purpose and Environment 2336

A.4.6.4.3.2 Test parameters 2337

A.4.6.4.3.3 Test Requirements 2338

A.4.6.4.4 CSI-RS based L1-RSRP measurement when DRX is used 2338

A.4.6.4.4.1 Test Purpose and Environment 2338

A.4.6.4.4.2 Test parameters 2339

A.4.6.4.4.3 Test Requirements 2340

A.4.6.4.5 SSB based L1-RSRP measurement when DRX is used for UE configured with highSpeedMeasFlag-r16 2340

A.4.6.4.5.1 Test Purpose and Environment 2340

A.4.6.4.5.2 Test parameters 2341

A.4.6.4.5.3 Test Requirements 2342

A.4.6.4.6 CSI-RS based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP 2342

A.4.6.4.6.1 Test Purpose and Environment 2342

A.4.6.4.7 SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP 2343

A.4.6.4.7.1 Test Purpose and Environment 2343

A.4.6.4.7.2 Test Requirements 2343

A.4.6.4.8 SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used 2343

A.4.6.4.8.1 Test Purpose and Environment 2343

A.4.6.4.8.2 Test parameters 2343

A.4.6.4.8.3 Test Requirements 2345

A.4.6.5 CLI measurements 2345

A.4.6.5.1 SRS-RSRP measurement with non-DRX 2345

A.4.6.5.1.1 Test Purpose and Environment 2345

A.4.6.5.1.2 Test Parameters 2345

A.4.6.5.1.3 Test Requirements 2348

A.4.6.5.2 CLI-RSSI measurement with non-DRX 2348

A.4.6.5.2.1 Test Purpose and Environment 2348

A.4.6.5.2.2 Test Parameters 2348

A.4.6.5.2.3 Test Requirements 2349

A.4.6.6.1.2 Test Requirements 2353

A.4.6.7 L1-SINR measurement for beam reporting 2353

A.4.6.7.2 L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is used 2355

A.4.6.7.2.1 Test Purpose and Environment 2355

A.4.6.7.2.2 Test parameters 2356

A.4.6.7.2.3 Test Requirements 2357

A.4.6.7.3 L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is used 2357

A.4.6.7.3.1 Test Purpose and Environment 2358

A.4.6.7.3.2 Test parameters 2358

A.4.6.7.3.3 Test Requirements 2359

A.4.6.8 CSI-RS based intra-frequency Measurement 2360

A.4.6.8.1 EN-DC event triggered reporting tests without gap under DRX 2360

A.4.6.8.1.1 Test purpose and Environment 2360

A.4.6.8.1.2 Test Requirements 2362

A.4.6.9 CSI-RS based inter-frequency Measurement 2362

A.4.6.9.1 EN-DC event triggered reporting tests for FR1 cell when non-DRX is used 2362

A.4.6.9.1.1 Test Purpose and Environment 2362

A.4.6.9.1.2 Test Requirements 2364

A.4.7 Measurement Performance requirements 2366

A.4.7.1 SS-RSRP 2366

A.4.7.1.1 EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 2366

A.4.7.1.1.1 Test Purpose and Environment 2366

A.4.7.1.1.2 Test parameters 2366

A.4.7.1.1.3 Test Requirements 2371

A.4.7.1.2 EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 2371

A.4.7.1.2.1 Test Purpose and Environment 2371

A.4.7.1.2.2 Test parameters 2371

A.4.7.1.2.3 Test Requirements 2374

A.4.7.1.3 Void 2374

A.4.7.2 SS-RSRQ 2374

A.4.7.2.1 EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 2374

A.4.7.2.1.1 Test Purpose and Environment 2374

A.4.7.2.1.2 Test Parameters 2374

A.4.7.2.1.3 Test Requirements 2378

A.4.7.2.2 EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 2378

A.4.7.2.2.1 Test Purpose and Environment 2378

A.4.7.2.2.2 Test Parameters 2378

A.4.7.2.2.3 Test Requirements 2382

A.4.7.3 SS-SINR 2382

A.4.7.3.1 EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 2382

A.4.7.3.1.1 Test Purpose and Environment 2382

A.4.7.3.1.2 Test Parameters 2382

A.4.7.3.1.3 Test Requirements 2386

A.4.7.3.2 EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 2386

A.4.7.3.2.1 Test Purpose and Environment 2386

A.4.7.3.2.2 Test Parameters 2386

A.4.7.3.2.3 Test Requirements 2389

A.4.7.4 L1-RSRP measurement for beam reporting 2389

A.4.7.4.1 SSB based L1-RSRP measurement 2389

A.4.7.4.1.1 Test Purpose and Environment 2389

A.4.7.4.1.2 Test parameters 2389

A.4.7.4.1.3 Test Requirements 2392

A.4.7.4.2 CSI-RS based L1-RSRP measurement on resource set with repetition off 2392

A.4.7.4.2.1 Test Purpose and Environment 2392

A.4.7.4.2.2 Test parameters 2393

A.4.7.4.2.3 Test Requirements 2396

A.4.7.5 SFTD accuracy 2396

A.4.7.5.1 SFTD accuracy 2396

A.4.7.5.1.1 Test Purpose and Environment 2396

A.4.7.5.1.2 Test Parameters 2396

A.4.7.5.1.3 Test Requirements 2399

A.4.7.5.2 Void 2399

A.4.7.5.3 Void 2399

A.4.7.6 CLI measurements 2399

A.4.7.6.1 EN-DC SRS-RSRP measurement accuracy with FR1 serving cell 2399

A.4.7.6.1.1 Test Purpose and Environment 2399

A.4.7.6.1.2 Test parameters 2399

A.4.7.6.1.3 Test Requirements 2402

A.4.7.6.2 EN-DC CLI-RSSI measurement accuracy with FR1 serving cell 2402

A.4.7.6.2.1 Test Purpose and Environment 2402

A.4.7.6.2.2 Test parameters 2403

A.4.7.6.2.3 Test Requirements 2404

A.4.7.7 L1-SINR measurement for beam reporting 2404

A.4.7.7.2 L1-SINR measurement with SSB based CMR and dedicated IMR 2408

A.4.7.7.2.1 Test Purpose and Environment 2408

A.4.7.7.2.2 Test parameters 2408

A.4.7.7.2.3 Test Requirements 2411

A.4.7.7.3 L1-SINR measurement with CSI-RS based CMR and dedicated IMR 2411

A.4.7.7.3.1 Test Purpose and Environment 2411

A.4.7.7.3.2 Test parameters 2412

A.4.7.7.3.3 Test Requirements 2415

A.4.7.8 CSI-RSRP 2415

A.4.7.8.1 EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 2415

A.4.7.8.1.1 Test Purpose and Environment 2415

A.4.7.8.1.2 Test parameters 2415

A.4.7.8.1.3 Test Requirements 2419

A.4.7.8.2 EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 2419

A.4.7.8.2.1 Test Purpose and Environment 2419

A.4.7.8.2.2 Test parameters 2420

A.4.7.8.2.3 Test Requirements 2423

A.4.7.9 CSI-RSRQ 2423

A.4.7.9.1 EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 2423

A.4.7.9.1.1 Test Purpose and Environment 2423

A.4.7.9.1.2 Test Parameters 2423

A.4.7.9.1.3 Test Requirements 2427

A.4.7.9.2 EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 2427

A.4.7.9.2.1 Test Purpose and Environment 2427

A.4.7.9.2.2 Test Parameters 2427

A.4.7.9.2.3 Test Requirements 2431

A.4.7.10 CSI-SINR 2431

A.4.7.10.1 EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 2431

A.4.7.10.1.1 Test Purpose and Environment 2431

A.4.7.10.1.2 Test Parameters 2431

A.4.7.10.1.3 Test Requirements 2434

A.4.7.10.2 EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 2435

A.4.7.10.2.1 Test Purpose and Environment 2435

A.4.7.10.2.2 Test Parameters 2435

A.4.7.10.2.3 Test Requirements 2438

A.4.7.11 TDCP amplitude measurement accuracy 2438

A.4.7.11.1 TDCP amplitude measurement accuracy in EN-DC 2438

A.4.7.11.1.1 Test Purpose and Environment 2438

A.4.7.11.1.2 Test parameters 2439

A.4.7.11.1.3 Test Requirements 2440

A.4.8 Void 2440

A.4A NE-DC test with all NR cells in FR1 2440

A.4A.1 Signaling characteristics 2440

A.4A.1.1 E-UTRAN PSCell addition 2440

A.4A.1.1.1 Test purpose and environment 2440

A.4A.1.1.2 Test Requirements 2444

A.4A.1.2 Active BWP switch 2444

A.4A.1.2.1 E-UTRAN PSCell – NR PCell FR1 DCI-based and Timer-based DL active BWP switch in non-DRX in synchronous NE-DC 2444

A.4A.1.2.1.1 Test Purpose and Environment 2444

A.4A.1.2.1.2 Test Requirements 2447

A.4A.1.3 Intra-frequency handover with E-UTRAN PSCell 2448

A.4A.1.3.1 Test purpose and environment 2448

A.4A.1.3.2 Test Requirements 2452

A.4A.1.4 Handover with PSCell from NE-DC to NE-DC with unknown target PSCell 2452

A.4A.1.4.1 Test Purpose and Environment 2452

A.4A.1.4.2 Test Parameters 2452

A.4A.1.4.3 Test Requirements 2457

A.4A.1.4.3.1 Test Requirements for NR HO 2457

A.4A.1.4.3.2 Test Requirements for LTE PSCell Change 2457

A.4A.2 Measurement performance 2458

A.4A.2.1 SFTD accuracy 2458

A.4A.2.1.1 SFTD accuracy 2458

A.4A.2.1.1.1 Test Purpose 2458

A.4A.2.1.1.2 Test Environment 2458

A.4A.2.1.1.3 Test Requirements 2460

A.5 EN-DC tests with one or more NR cells in FR2 2461

A.5.1 Void 2461

A.5.2 Void 2461

A.5.3 RRC_CONNECTED state mobility 2461

A.5.3.1 Void 2461

A.5.3.2 RRC Connection Mobility Control 2461

A.5.3.2.1 Void 2461

A.5.3.2.2 Random Access 2461

A.5.3.2.2.1 4-step RA type c ontention based random access test in FR2 for PSCell/SCell in EN-DC 2461

A.5.3.2.2.2 4-step RA type non-contention based random access test in FR2 for PSCell/SCell in EN-DC 2464

A.5.3.2.2.3 2-step RA type contention based random access test in FR2 for PSCell/SCell in EN-DC 2467

A.5.3.2.2.4 2-step RA type non-contention based random access test in FR2 for PSCell/SCell in EN-DC 2470

A.5.3.2.3 Void 2472

A.5.3.3 Handover with PSCell with known FR2 target PSCell 2472

A.5.3.3.1 Test purpose and environment 2472

A.5.3.3.2 Test Requirements 2475

A.5.3.3.3 Void 2476

A.5.3.3.4 Void 2476

A.5.3.3.5 Void 2476

A.5.3.3.6 Void 2476

A.5.4 Timing 2476

A.5.4.1 UE transmit timing 2476

A.5.4.1.1 NR UE Transmit Timing Test for FR2 2476

A.5.4.1.1.1 Test Purpose and environment 2476

A.5.4.1.1.2 Test requirements 2478

A.5.4.1.2 NR UE Transmit Timing Test with 2-TA for FR2 UE supporting multiDCI-IntraCellMultiTRP-TwoTA-r18 2479

A.5.4.1.2.1 Test Purpose and environment 2479

A.5.4.1.2.2 Test requirements 2483

A.5.4.1.3 NR UE Transmit Timing Test with 2-TA for FR2 UE supporting single DCI 2483

A.5.4.1.3.1 Test Purpose and environment 2483

A.5.4.1.3.2 Test requirements 2486

A.5.4.2 UE timer accuracy 2487

A.5.4.3 Timing advance 2487

A.5.4.3.1 EN-DC FR2 timing advance adjustment accuracy 2487

A.5.4.3.1.1 Test Purpose and Environment 2487

A.5.4.3.1.2 Test Parameters 2487

A.5.4.3.1.3 Test Requirements 2489

A.5.4.3.2 EN-DC FR2 timing advance adjustment accuracy for asymmetric DL sTRP/UL mTRP deployment with two TAs 2490

A.5.4.3.2.1 Test Purpose and Environment 2490

A.5.4.3.2.2 Test Parameters 2490

A.5.4.3.2.3 Test Requirements 2493

A.5.5 Signaling characteristics 2493

A.5.5.1 Radio link Monitoring 2493

A.5.5.1.1 Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode 2493

A.5.5.1.1.1 Test Purpose and Environment 2493

A.5.5.1.1.2 Test Requirements 2496

A.5.5.1.2 Radio Link Monitoring In-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode 2496

A.5.5.1.2.1 Test Purpose and Environment 2496

A.5.5.1.2.2 Test Requirements 2499

A.5.5.1.3 Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode 2500

A.5.5.1.3.1 Test Purpose and Environment 2500

A.5.5.1.3.2 Test Requirements 2502

A.5.5.1.4 Radio Link Monitoring In-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode 2502

A.5.5.1.4.1 Test Purpose and Environment 2502

A.5.5.1.4.2 Test Requirements 2505

A.5.5.1.5 EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode 2505

A.5.5.1.6 EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode 2508

A.5.5.1.7 EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode 2511

A.5.5.1.8 EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode 2514

A.5.5.1.8.2 Test Requirements 2518

A.5.5.1.9 EN-DC Radio Link Monitoring UE Scheduling Restrictions on FR2 2518

A.5.5.1.9.1 Test Purpose and Environment 2518

A.5.5.1.9.2 Test Requirements 2520

A.5.5.1.10 Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS for UE fulfilling relaxed measurement criterion 2520

A.5.5.1.10.1 Test Purpose and Environment 2520

A.5.5.1.10.2 Test Requirements 2522

A.5.5.1.11 Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode for UE supporting fast beam sweeping in multi-Rx 2523

A.5.5.1.11.1 Test Purpose and Environment 2523

A.5.5.1.11.2 Test Requirements 2525

A.5.5.1.12 EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP 2526

A.5.5.1.12.1 Test Purpose and Environment 2526

A.5.5.1.13 Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP 2526

A.5.5.1.13.1 Test Purpose and Environment 2526

A.5.5.1.13.2 Test Requirements 2526

A.5.5.1.14 EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP 2526

A.5.5.1.14.1 Test Purpose and Environment 2526

A.5.5.1.14.2 Test Requirements 2529

A.5.5.2 Interruption 2530

A.5.5.2.1 E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in synchronous EN-DC 2530

A.5.5.2.1.1 Test Purpose and Environment 2530

A.5.5.2.1.2 Test Requirements 2532

A.5.5.2.2 E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC 2532

A.5.5.2.2.1 Test Purpose and Environment 2532

A.5.5.2.2.2 Test Requirements 2534

A.5.5.2.3 E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in synchronous EN-DC 2534

A.5.5.2.3.1 Test Purpose and Environment 2534

A.5.5.2.3.2 Test Requirements 2536

A.5.5.2.4 E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in asynchronous EN-DC 2537

A.5.5.2.4.1 Test Purpose and Environment 2537

A.5.5.2.4.2 Test Requirements 2539

A.5.5.2.5 E-UTRAN – NR FR2 interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC 2539

A.5.5.2.5.1 Test Purpose and Environment 2539

A.5.5.2.5.2 Test Requirements 2541

A.5.5.2.6 E-UTRAN – NR FR2 interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC 2542

A.5.5.2.6.1 Test Purpose and Environment 2542

A.5.5.2.6.2 Test Requirements 2543

A.5.5.2.7 E-UTRAN – NR FR2 interruptions at E-UTRA SRS carrier based switching 2544

A.5.5.2.7.1 Test Purpose and Environment 2544

A.5.5.2.7.2 Test Requirements 2546

A.5.5.2.8 E-UTRAN – NR FR2 interruptions at NR SRS carrier based switching 2546

A.5.5.2.8.1 Test Purpose and Environment 2546

A.5.5.2.8.3 Test Requirements 2548

A.5.5.2.9 E-UTRAN – NR FR2 interruptions during measurements on deactivated NR PSCell 2548

A.5.5.2.9.1 Test Purpose and Environment 2548

A.5.5.2.9.2 Test Requirements 2551

A.5.5.3 SCell Activation and Deactivation Delay 2551

A.5.5.3.1 SCell Activation and deactivation of SCell in FR2 intra-band 2551

A.5.5.3.1.1 Test Purpose and Environment 2551

A.5.5.3.1.2 Test Requirements 2552

A.5.5.3.2 SCell Activation and deactivation of known SCell in FR1 for 160 ms SCell measurement cycle 2553

A.5.5.3.2.1 Test Purpose and Environment 2553

A.5.5.3.2.2 Test Requirements 2555

A.5.5.3.3 Void 2555

A.5.5.3.4 Void 2555

A.5.5.3.5 SCell Activation and deactivation of SCell in FR2 2555

A.5.5.3.5.1 Test Purpose and Environment 2555

A.5.5.3.5.2 Test Requirements 2558

A.5.5.3.6 Multiple SCell Activation and deactivation of one unknown SCell and one known SCell in FR2 2558

A.5.5.3.6.1 Test Purpose and Environment 2558

A.5.5.3.6.2 Test Requirements 2561

A.5.5.3.7 Direct SCell activation at SCell addition of known SCell in FR2 2561

A.5.5.3.7.1 Test Purpose and Environment 2561

A.5.5.3.7.2 Test Requirements 2564

A.5.5.3.8 Fast SCell Activation of SCell in FR2 intra-band 2564

A.5.5.3.8.1 Test Purpose and Environment 2564

A.5.5.3.8.2 Test Requirements 2567

A.5.5.3.9 PUCCH SCell Activation and deactivation of known SCell in FR2 2567

A.5.5.3.9.1 Test Purpose and Environment 2567

A.5.5.3.9.2 Test Requirements 2570

A.5.5.3.10 PUCCH SCell Activation and deactivation of unknown SCell in FR2 2570

A.5.5.3.10.1 Test Purpose and Environment 2570

A.5.5.3.10.2 Test Requirements 2573

A.5.5.3.11 Multiple SCell activation and deactivation of one known PUCCH SCell and one unknown SCell in FR2 2573

A.5.5.3.11.1 Test Purpose and Environment 2573

A.5.5.3.11.2 Test Requirements 2576

A.5.5.3.12 SCell Activation and deactivation of unknown PUCCH SCell and unknown DL SCell in FR2 in non-DRX 2577

A.5.5.3.12.1 Test Purpose and Environment 2577

A.5.5.3.12.2 Test Requirements 2580

A.5.5.3.13 SCell Activation and deactivation of unknown SCell in FR2 for UE in DRX, capable of small beam sweeping factors and/or short measurement interval 2580

A.5.5.3.13.1 Test Purpose and Environment 2580

A.5.5.3.13.2 Test Requirements 2583

A.5.5.3.14 PUCCH SCell activation and deactivation with FR1 PSCell based on L3 reporting after SCell activation command 2585

A.5.5.3.14.1 Test Purpose and Environment 2585

A.5.5.3.14.2 Test Requirements 2589

A.5.5.3.15 SCell Activation of unknown SCell in FR2 in non-DRX for 160 ms SCell measurement cycle with the L3 reporting during activation 2590

A.5.5.3.15.1 Test Purpose and Environment 2590

A.5.5.3.15.2 Test Requirements 2594

A.5.5.4 Void 2595

A.5.5.5 Beam Failure Detection and Link recovery procedures 2595

A.5.5.5.1 EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in non-DRX mode 2595

A.5.5.5.1.1 Test Purpose and Environment 2595

A.5.5.5.1.2 Test Requirements 2598

A.5.5.5.2 EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in DRX mode 2598

A.5.5.5.2.1 Test Purpose and Environment 2598

A.5.5.5.2.2 Test Requirements 2602

A.5.5.5.3 EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in non-DRX mode 2602

A.5.5.5.3.1 Test Purpose and Environment 2602

A.5.5.5.3.2 Test Requirements 2605

A.5.5.5.4 EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in DRX mode 2606

A.5.5.5.4.1 Test Purpose and Environment 2606

A.5.5.5.4.2 Test Requirements 2609

A.5.5.5.5 EN-DC scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PSCell configured with SSB-based BFD and LR in non-DRX mode 2609

A.5.5.5.5.1 Test Purpose and Environment 2609

A.5.5.5.5.2 Test Requirements 2612

A.5.5.5.6 EN-DC Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in non-DRX mode 2612

A.5.5.5.6.1 Test Purpose and Environment 2612

A.5.5.5.6.2 Test Requirements 2616

A.5.5.5.7 EN-DC Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode 2616

A.5.5.5.7.1 Test Purpose and Environment 2616

A.5.5.5.7.2 Test Requirements 2619

A.5.5.5.8 EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in DRX mode 2620

A.5.5.5.8.1 Test Purpose and Environment 2620

A.5.5.5.8.2 Test Requirements 2623

A.5.5.5.9 Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in DRX mode for UE fulfilling relaxed measurement criterion 2623

A.5.5.5.9.1 Test Purpose and Environment 2623

A.5.5.5.9.2 Test Requirements 2626

A.5.5.6 Active BWP switch 2627

A.5.5.6.1 DCI-based and Timer-based Active BWP Switch 2627

A.5.5.6.1.1 E-UTRAN – NR PSCell FR2 DL active BWP switch with non-DRX in synchronous EN-DC 2627

A.5.5.6.1.1.1 Test Purpose and Environment 2627

A.5.5.6.1.1.2 Test Requirements 2629

A.5.5.6.1.2 E-UTRAN – NR PSCell FR2 with FR2 SCell DL active BWP switch in non-DRX in synchronous EN-DC 2630

A.5.5.6.2 RRC-based Active BWP Switch 2633

A.5.5.6.2.1 E-UTRAN – NR PSCell FR2 DL active BWP switch with non-DRX in synchronous EN-DC 2633

A.5.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs 2636

A.5.5.6.3.1 E-UTRAN – NR PSCell FR2 and NR SCell FR2 DL active BWP switch on multiple CCs in synchronous EN-DC 2636

A.5.5.6.4 SCell dormancy switch 2639

A.5.5.6.4.1 E-UTRAN – NR FR2 PSCell SCell dormancy switch of single FR2 SCell inside active time 2639

A.5.5.6.4.1.1 Test Purpose and Environment 2639

A.5.5.6.4.1.2 Test Requirements 2642

A.5.5.6.4.2 E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR2 SCells outside active time 2643

A.5.5.6.4.2.1 Test Purpose and Environment 2643

A.5.5.6.4.2.2 Test Requirements 2647

A.5.5.6.5 Simultaneous RRC-based Active BWP Switch on multiple CCs 2647

A.5.5.6.5.1 E-UTRAN – NR PSCell FR2  and NR SCell FR2 DL active BWP switch on multiple CCs with non-DRX in synchronous EN-DC 2647

A.5.5.7 PSCell addition and release delay 2650

A.5.5.7.1 Addition and Release Delay of NR PSCell 2650

A.5.5.7.1.1 Test purpose and environment 2650

A.5.5.7.1.2 Test Requirements 2652

A.5.5.8 Active TCI state switch delay 2652

A.5.5.8.1 MAC-CE based active TCI state switch 2653

A.5.5.8.1.1 E-UTRAN – NR PSCell FR2 active TCI state switch for a known TCI state 2653

A.5.5.8.1.1.1 Test Purpose and Environment 2653

A.5.5.8.1.1.2 Test Requirements 2655

A.5.5.8.2 RRC based active TCI state switch 2656

A.5.5.8.2.1 E-UTRAN – NR PSCell FR2 active TCI state switch for a known TCI state 2656

A.5.5.8.2.1.1 Test Purpose and Environment 2656

A.5.5.8.2.1.2 Test Requirements 2659

A.5.5.9 Uplink spatial relation switch delay 2659

A.5.5.9.1 MAC-CE based uplink spatial relation switch 2659

A.5.5.9.1.1 E-UTRAN – NR PSCell FR2 uplink spatial relation switch for a known spatial relation 2659

A.5.5.9.1.1.1 Test Purpose and Environment 2659

A.5.5.9.1.1.2 Test Requirements 2661

A.5.5.9.2 RRC based spatial relation switch 2661

A.5.5.9.2.1 E-UTRAN – NR PSCell FR2 spatial relation switch associated with a known DL-RS 2661

A.5.5.9.2.1.1 Test Purpose and Environment 2662

A.5.5.9.2.1.2 Test Requirements 2663

A.5.5.10 UE specific CBW change 2664

A.5.5.10.1 UE specific CBW change on FR2 NR PSCell 2664

A.5.5.10.1.1 Test Purpose and Environment 2664

A.5.5.10.1.2 Test Requirements 2666

A.5.5.11 Unified TCI state switch delay 2667

A.5.5.11.1 MAC-CE based active joint TCI state switch 2667

A.5.5.11.1.1 E-UTRAN – NR PSCell FR2 active joint TCI state switch for a known TCI state 2667

A.5.5.11.1.1.1 Test Purpose and Environment 2667

A.5.5.11.1.1.2 Test parameters 2667

A.5.5.11.1.1.3 Test Requirements 2669

A.5.5.11.2 MAC-CE based active uplink TCI state switch 2669

A.5.5.11.2.1 E-UTRAN – NR PSCell FR2 active uplink TCI state switch for a known TCI state 2669

A.5.5.11.2.1.1 Test Purpose and Environment 2669

A.5.5.11.2.1.2 Test parameters 2670

A.5.5.11.2.1.3 Test Requirements 2671

A.5.5.11.3 MAC-CE based active downlink TCI state switch 2672

A.5.5.11.3.1 E-UTRAN – NR PSCell FR2 downlink TCI state switch to cell with additional PCI for a known TCI state 2672

A.5.5.11.3.1.1 Test Purpose and Environment 2672

A.5.5.11.3.1.2 Test Parameters 2672

A.5.5.11.3.1.3 Test Requirements 2675

A.5.5.12 PSCell activation and deactivation delay 2675

A.5.5.12.1 PSCell activation and deactivation delay 2675

A.5.5.12.1.1 Test purpose and environment 2675

A.5.5.12.1.2 Test Requirements 2677

A.5.5.13 Conditional PSCell addition and release delay 2678

A.5.5.13.1 Addition and Release Delay of NR PSCell 2678

A.5.5.13.1.1 Test purpose and environment 2678

A.5.5.13.1.2 Test Requirements 2680

A.5.6 Measurement procedure 2680

A.5.6.1 Intra-frequency Measurements 2680

A.5.6.1.1 EN-DC event triggered reporting test without gap under non-DRX 2680

A.5.6.1.1.1 Test purpose and Environment 2680

A.5.6.1.1.2 Test Requirements 2683

A.5.6.1.2 EN-DC event triggered reporting test without gap under DRX 2683

A.5.6.1.2.1 Test purpose and Environment 2683

A.5.6.1.2.2 Test Requirements 2685

A.5.6.1.3 EN-DC event triggered reporting test with per-UE gaps under non-DRX 2686

A.5.6.1.3.1 Test purpose and Environment 2686

A.5.6.1.3.2 Test Requirements 2688

A.5.6.1.4 EN-DC event triggered reporting test with per-UE gaps under DRX 2688

A.5.6.1.4.1 Test purpose and Environment 2688

A.5.6.1.4.2 Test Requirements 2690

A.5.6.1.5 EN-DC event triggered reporting test without gap under non-DRX when CD-SSB is outside active BWP 2691

A.5.6.1.5.1 Test purpose and Environment 2691

A.5.6.1.5.2 Test Requirements 2691

A.5.6.1.6 EN-DC event triggered reporting test without gap under non-DRX 2691

A.5.6.1.6.1 Test purpose and Environment 2691

A.5.6.1.6.2 Test Requirements 2693

A.5.6.1.7 EN-DC event triggered reporting test without gap under non-DRX for UE configured with cssf-Config 2694

A.5.6.1.7.1 Test purpose and Environment 2694

A.5.6.1.7.2 Test Requirements 2697

A.5.6.2 Inter-frequency Measurements 2697

A.5.6.2.1 EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is not used 2697

A.5.6.2.1.1 Test Purpose and Environment 2697

A.5.6.2.1.2 Test Requirements 2700

A.5.6.2.2  EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is used 2700

A.5.6.2.2.1 Test Purpose and Environment 2700

A.5.6.2.2.2 Test Requirements 2702

A.5.6.2.3  EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is not used 2703

A.5.6.2.3.1 Test Purpose and Environment 2703

A.5.6.2.3.2 Test Requirements 2705

A.5.6.2.4 EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is used 2705

A.5.6.2.4.1 Test Purpose and Environment 2705

A.5.6.2.4.2 Test Requirements 2708

A.5.6.2.5 EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is not used 2708

A.5.6.2.5.1 Test Purpose and Environment 2708

A.5.6.2.5.2 Test Requirements 2711

A.5.6.2.6 EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is used 2711

A.5.6.2.6.1 Test Purpose and Environment 2711

A.5.6.2.6.2 Test Requirements 2714

A.5.6.2.7 EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is not used 2715

A.5.6.2.7.1 Test Purpose and Environment 2715

A.5.6.2.7.2 Test Requirements 2717

A.5.6.2.8 EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is used 2718

A.5.6.2.8.1 Test Purpose and Environment 2718

A.5.6.2.8.2 Test Requirements 2721

A.5.6.2.9 EN-DC event triggered reporting tests without gap under non-DRX in FR for UE supporting [FR1 only EN-DC 3-searcher capability] 2721

A.5.6.2.9.1 Test purpose and Environment 2721

A.5.6.2.9.2 Test parameters 2721

A.5.6.2.9.3 Test Requirements 2724

A.5.6.3 L1-RSRP measurement for beam reporting 2724

A.5.6.3.1 SSB based L1-RSRP measurement when DRX is not used 2724

A.5.6.3.1.1 Test Purpose and Environment 2724

A.5.6.3.1.2 Test parameters 2724

A.5.6.3.1.3 Test Requirements 2726

A.5.6.3.2 SSB based L1-RSRP measurement when DRX is used 2726

A.5.6.3.2.1 Test Purpose and Environment 2726

A.5.6.3.2.2 Test parameters 2726

A.5.6.3.2.3 Test Requirements 2728

A.5.6.3.3 CSI-RS based L1-RSRP measurement when DRX is not used 2728

A.5.6.3.3.1 Test Purpose and Environment 2728

A.5.6.3.3.2 Test parameters 2728

A.5.6.3.3.3 Test Requirements 2729

A.5.6.3.4 CSI-RS based L1-RSRP measurement when DRX is used 2730

A.5.6.3.4.1 Test Purpose and Environment 2730

A.5.6.3.4.2 Test parameters 2730

A.5.6.3.4.3 Test Requirements 2731

A.5.6.3.5 CSI-RS based L1-RSRP measurement when DRX is not used and when CD-SSB is outside active BWP 2732

A.5.6.3.5.1 Test Purpose and Environment 2732

A.5.6.3.6 SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP 2732

A.5.6.3.6.1 Test Purpose and Environment 2732

A.5.6.3.6.2 Test Requirements 2732

A.5.6.3.7 SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used 2732

A.5.6.3.7.1 Test Purpose and Environment 2732

A.5.6.3.7.2 Test parameters 2733

A.5.6.3.7.3 Test Requirements 2734

A.5.6.4 CLI measurements 2734

A.5.6.4.1 SRS-RSRP measurement with DRX 2734

A.5.6.4.1.1 Test Purpose and Environment 2734

A.5.6.4.1.2 Test Parameters 2735

A.5.6.4.1.3 Test Requirements 2736

A.5.6.4.2 CLI-RSSI measurement with DRX 2737

A.5.6.4.2.1 Test Purpose and Environment 2737

A.5.6.4.2.2 Test Parameters 2737

A.5.6.4.2.3 Test Requirements 2738

A.5.6.5 Measurements with autonomous gaps 2738

A.5.6.5.1  EN-DC inter-frequency CGI identification of NR neighbor cell in FR2 2738

A.5.6.5.1.1 Test Purpose and Environment 2738

A.5.6.5.1.2 Test Requirements 2741

A.5.6.6 L1-SINR measurement for beam reporting 2741

A.5.6.6.2 L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used 2743

A.5.6.6.2.1 Test Purpose and Environment 2743

A.5.6.6.2.2 Test parameters 2743

A.5.6.6.2.3 Test Requirements 2745

A.5.6.6.3 L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used 2745

A.5.6.6.3.1 Test Purpose and Environment 2745

A.5.6.6.3.2 Test parameters 2746

A.5.6.6.3.3 Test Requirements 2747

A.5.6.7 CSI-RS based Intra-frequency Measurements 2747

A.5.6.7.1 EN-DC event triggered reporting test without gap under non-DRX 2747

A.5.6.7.1.1 Test purpose and Environment 2747

A.5.6.7.1.2 Test Requirements 2749

A.5.6.8 CSI-RS based Inter-frequency Measurements 2749

A.5.6.8.1  EN-DC event triggered reporting tests for NR FR2 cell when DRX is used 2749

A.5.6.8.1.1 Test Purpose and Environment 2749

A.5.6.8.1.2 Test Requirements 2751

A.5.7 Measurement Performance requirements 2752

A.5.7.1 SS-RSRP 2752

A.5.7.1.1 EN-DC intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell 2752

A.5.7.1.1.1 Test Purpose and Environment 2752

A.5.7.1.1.2 Test parameters 2752

A.5.7.1.1.3 Test Requirements 2754

A.5.7.1.2 EN-DC inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell 2754

A.5.7.1.2.1 Test Purpose and Environment 2754

A.5.7.1.2.2 Test parameters 2755

A.5.7.1.2.3 Test Requirements 2757

A.5.7.1.3 EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR2 target cell 2758

A.5.7.1.3.1 Test Purpose and Environment 2758

A.5.7.1.3.2 Test parameters 2758

A.5.7.1.3.3 Test Requirements 2760

A.5.7.2 SS-RSRQ 2760

A.5.7.2.1 EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell 2760

A.5.7.2.1.1 Test Purpose and Environment 2760

A.5.7.2.1.2 Test Parameters 2761

A.5.7.2.1.3 Test Requirements 2762

A.5.7.2.2 EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell 2762

A.5.7.2.2.1 Test Purpose and Environment 2762

A.5.7.2.2.2 Test Parameters 2762

A.5.7.2.2.3 Test Requirements 2764

A.5.7.3 SS-SINR 2764

A.5.7.3.1 EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell 2764

A.5.7.3.1.1 Test Purpose and Environment 2764

A.5.7.3.1.2 Test Parameters 2764

A.5.7.3.1.3 Test Requirements 2766

A.5.7.3.2 EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell 2766

A.5.7.3.2.1 Test Purpose and Environment 2766

A.5.7.3.2.2 Test Parameters 2766

A.5.7.3.2.3 Test Requirements 2767

A.5.7.4 L1-RSRP measurement for beam reporting 2767

A.5.7.4.1 SSB based L1-RSRP measurement 2768

A.5.7.4.1.1 Test Purpose and Environment 2768

A.5.7.4.1.2 Test parameters 2768

A.5.7.4.1.3 Test Requirements 2769

A.5.7.4.2 CSI-RS based L1-RSRP measurement on resource set with repetition off 2770

A.5.7.4.2.1 Test Purpose and Environment 2770

A.5.7.4.2.2 Test parameters 2770

A.5.7.4.2.3 Test Requirements 2771

A.5.7.5 CLI measurements 2772

A.5.7.5.1 EN-DC SRS-RSRP measurement accuracy with FR2 serving cell 2772

A.5.7.5.1.1 Test Purpose and Environment 2772

A.5.7.5.1.2 Test parameters 2772

A.5.7.5.1.3 Test Requirements 2774

A.5.7.5.2 EN-DC CLI-RSSI measurement accuracy with FR2 serving cell 2774

A.5.7.5.2.1 Test Purpose and Environment 2774

A.5.7.5.2.2 Test parameters 2774

A.5.7.5.2.3 Test Requirements 2776

A.5.7.6 L1-SINR measurement for beam reporting 2776

A.5.7.6.2 L1-SINR measurement with SSB based CMR and dedicated IMR 2778

A.5.7.6.2.1 Test Purpose and Environment 2779

A.5.7.6.2.2 Test parameters 2779

A.5.7.6.2.3 Test Requirements 2780

A.5.7.6.3 L1-SINR measurement with CSI-RS based CMR and dedicated IMR 2781

A.5.7.6.3.1 Test Purpose and Environment 2781

A.5.7.6.3.2 Test parameters 2781

A.5.7.6.3.3 Test Requirements 2783

A.5.7.7 CSI-RSRP 2783

A.5.7.7.1 EN-DC intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell 2783

A.5.7.7.1.1 Test Purpose and Environment 2783

A.5.7.7.1.2 Test parameters 2783

A.5.7.7.1.3 Test Requirements 2785

A.5.7.7.2 EN-DC inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell 2786

A.5.7.7.2.1 Test Purpose and Environment 2786

A.5.7.7.2.2 Test parameters 2786

A.5.7.7.2.3 Test Requirements 2788

A.5.7.8 CSI-RSRQ 2789

A.5.7.8.1 EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell 2789

A.5.7.8.1.1 Test Purpose and Environment 2789

A.5.7.8.1.2 Test Parameters 2789

A.5.7.8.1.3 Test Requirements 2791

A.5.7.8.2 EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell 2791

A.5.7.8.2.1 Test Purpose and Environment 2791

A.5.7.8.2.2 Test Parameters 2791

A.5.7.8.2.3 Test Requirements 2793

A.5.7.9 CSI-SINR 2793

A.5.7.9.1 EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell 2793

A.5.7.9.1.1 Test Purpose and Environment 2793

A.5.7.9.1.2 Test Parameters 2793

A.5.7.9.1.3 Test Requirements 2795

A.5.7.9.2 EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell 2795

A.5.7.9.2.1 Test Purpose and Environment 2795

A.5.7.9.2.2 Test Parameters 2795

A.5.7.9.2.3 Test Requirements 2797

A.5.8 Void 2797

A.6 NR standalone tests with all NR cells in FR1 2798

A.6.1 SA: RRC_IDLE state mobility 2798

A.6.1.1 Cell re-selection to NR 2798

A.6.1.1.1 Cell reselection to FR1 intra-frequency NR case 2798

A.6.1.1.1.1 Test Purpose and Environment 2798

A.6.1.1.1.2 Test Parameters 2798

A.6.1.1.1.3 Test Requirements 2800

A.6.1.1.2 Cell reselection to FR1 inter-frequency NR case 2800

A.6.1.1.2.1 Test Purpose and Environment 2800

A.6.1.1.2.2 Test Parameters 2801

A.6.1.1.2.3 Test Requirements 2803

A.6.1.1.3 Cell reselection to FR1 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion 2803

A.6.1.1.3.1 Test Purpose and Environment 2803

A.6.1.1.3.2 Test Parameters 2803

A.6.1.1.3.3 Test Requirements 2806

A.6.1.1.4 Cell reselection to FR1 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion 2806

A.6.1.1.4.1 Test Purpose and Environment 2806

A.6.1.1.4.2 Test Parameters 2806

A.6.1.1.4.3 Test Requirements 2808

A.6.1.1.5 Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion 2809

A.6.1.1.5.1 Test Purpose and Environment 2809

A.6.1.1.5.2 Test Parameters 2809

A.6.1.1.5.3 Test Requirements 2811

A.6.1.1.6 Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion 2812

A.6.1.1.6.1 Test Purpose and Environment 2812

A.6.1.1.6.2 Test Parameters 2812

A.6.1.1.6.3 Test Requirements 2814

A.6.1.1.7 Cell reselection to FR1 intra-frequency NR case for UE configured with highSpeedMeasFlag-r16 2815

A.6.1.1.7.1 Test Purpose and Environment 2815

A.6.1.1.7.2 Test Parameters 2815

A.6.1.1.7.3 Test Requirements 2818

A.6.1.1.8 Cell reselection to FR1 inter-frequency NR case for UE configured with highSpeedMeasInterFreq-r17 2818

A.6.1.1.8.1 Test Purpose and Environment 2818

A.6.1.1.8.2 Test Parameters 2818

A.6.1.1.8.3 Test Requirements 2821

A.6.1.1.9 Cell reselection to FR1 intra-frequency NR case for UE operating on a cell with less than 5 MHz BW 2821

A.6.1.1.9.1 Test Purpose and Environment 2821

A.6.1.1.9.2 Test Parameters 2821

A.6.1.1.9.3 Test Requirements 2822

A.6.1.1.10 Cell reselection to FR1 intra-frequency NR cell supporting OD-SIB1 2823

A.6.1.1.10.1 Test Purpose and Environment 2823

A.6.1.1.10.2 Test Parameters 2823

A.6.1.1.10.3 Test Requirements 2824

A.6.1.1.11 Cell reselection to FR1 inter-frequency NR cell supporting OD-SIB1 2825

A.6.1.1.11.1 Test Purpose and Environment 2825

A.6.1.1.11.2 Test Parameters 2825

A.6.1.1.11.3 Test Requirements 2827

A.6.1.2 Inter-RAT E-UTRAN cell re-selection 2827

A.6.1.2.1 Cell reselection to higher priority E-UTRAN 2827

A.6.1.2.1.1 Test Purpose and Environment 2827

A.6.1.2.1.2 Test Parameters 2827

A.6.1.2.1.3 Test Requirements 2829

A.6.1.2.2 Cell reselection to lower priority E-UTRAN 2830

A.6.1.2.2.1 Test Purpose and Environment 2830

A.6.1.2.2.2 Test Parameters 2830

A.6.1.2.2.3 Test Requirements 2832

A.6.1.2.3 Cell reselection to lower priority E-UTRAN for UE fulfilling low mobility relaxed measurement criterion 2833

A.6.1.2.3.1 Test Purpose and Environment 2833

A.6.1.2.3.2 Test Parameters 2833

A.6.1.2.3.3 Test Requirements 2836

A.6.1.2.4 Cell reselection to lower priority E-UTRAN for UE fulfilling not-at-cell edge relaxed measurement criterion 2836

A.6.1.2.4.1 Test Purpose and Environment 2836

A.6.1.2.4.2 Test Parameters 2836

A.6.1.2.4.3 Test Requirements 2839

A.6.1.2.5 Cell reselection to lower priority E-UTRAN cell for UE configured with highSpeedMeasFlag-r16 2839

A.6.1.2.5.1 Test Purpose and Environment 2839

A.6.1.2.5.2 Test Parameters 2839

A.6.1.2.5.3 Test Requirements 2842

A.6.1.1.7 Void 2842

A.6.2 SA: RRC_INACTIVE state mobility 2842

A.6.2.1 Configured Grant based Small Data Transmissions (CG-SDT) 2842

A.6.2.1.1 Test purpose and Environment 2842

A.6.2.1.2 Test Parameters 2844

A.6.2.1.3 Test requirements 2845

A.6.2.2 Cell reselection for positioning 2845

A.6.2.2.1 Cell reselection to FR1 intra-frequency NR case with RRC_ INACTIVE eDRX and positioning SRS 2845

A.6.2.2.1.1 Test Purpose and Environment 2845

A.6.2.2.1.2 Test Parameters 2846

A.6.2.2.1.3 Test Requirements 2849

A.6.3 RRC_CONNECTED state mobility 2849

A.6.3.1 Handover 2849

A.6.3.1.1 Intra-frequency handover from FR1 to FR1; known target cell 2849

A.6.3.1.1.1 Test Purpose and Environment 2849

A.6.3.1.1.2 Test Parameters 2849

A.6.3.1.1.3 Test Requirements 2851

A.6.3.1.2 Intra-frequency handover from FR1 to FR1; unknown target cell 2851

A.6.3.1.2.1 Test Purpose and Environment 2851

A.6.3.1.2.2 Test Parameters 2851

A.6.3.1.2.3 Test Requirements 2853

A.6.3.1.3 Inter-frequency handover from FR1 to FR1; unknown target cell 2853

A.6.3.1.3.1 Test Purpose and Environment 2853

A.6.3.1.3.2 Test Parameters 2853

A.6.3.1.3.3 Test Requirements 2855

A.6.3.1.4 SA NR - E-UTRAN handover 2855

A.6.3.1.4.1 Test Purpose and Environment 2855

A.6.3.1.4.2 Test Requirements 2858

A.6.3.1.5 SA NR - E-UTRAN handover with unknown target cell 2859

A.6.3.1.5.1 Test Purpose and Environment 2859

A.6.3.1.5.2 Test Requirements 2862

A.6.3.1.6  SA NR - UTRAN FDD handover 2862

A.6.3.1.6.1 Test Purpose and Environment 2862

A.6.3.1.6.2 Test Requirements 2864

A.6.3.1.7 Intra-frequency synchronous DAPS handover in FR1 2864

A.6.3.1.7.1 Test Purpose and Environment 2864

A.6.3.1.7.2 Test Parameters 2864

A.6.3.1.7.3 Test Requirements 2867

A.6.3.1.8 Intra-frequency asynchronous DAPS handover in FR1 2867

A.6.3.1.8.1 Test Purpose and Environment 2867

A.6.3.1.8.2 Test Parameters 2868

A.6.3.1.8.3 Test Requirements 2870

A.6.3.1.9 Intra-band inter-frequency synchronous DAPS handover test in SA for FR1 2870

A.6.3.1.9.1 Test Purpose and Environment 2870

A.6.3.1.9.2 Test Parameters 2871

A.6.3.1.9.3 Test Requirements 2873

A.6.3.1.10 Intra-band inter-frequency asynchronous DAPS handover test in SA for FR1 2873

A.6.3.1.10.1 Test Purpose and Environment 2873

A.6.3.1.10.2 Test Parameters 2873

A.6.3.1.10.3 Test Requirements 2875

A.6.3.1.11 Inter-band inter-frequency synchronous DAPS handover from FR1 to FR1 2875

A.6.3.1.11.1 Test Purpose and Environment 2875

A.6.3.1.11.2 Test Parameters 2875

A.6.3.1.11.3 Test Requirements 2879

A.6.3.1.12 Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR1 2880

A.6.3.1.12.1 Test Purpose and Environment 2880

A.6.3.1.12.2 Test Parameters 2880

A.6.3.1.12.3 Test Requirements 2884

A.6.3.1.13 SA NR - E-UTRAN with NR PSCell addition in FR1 2884

A.6.3.1.13.1 Test Purpose and Environment 2884

A.6.3.1.13.2 Test Requirements 2889

A.6.3.1.14 SA NR - E-UTRAN handover with NR FR1 PSCell addition 2889

A.6.3.1.14.1 Test Purpose and Environment 2889

A.6.3.1.14.2 Test Requirements 2895

A.6.3.1.15 Intra-frequency handover from FR1 to FR1; known target cell configured with NCD-SSB 2895

A.6.3.1.15.1 Test Purpose and Environment 2896

A.6.3.1.15.2 Test Parameters 2896

A.6.3.1.15.3 Test Requirements 2898

A.6.3.1.16 Inter-frequency handover from FR1 to FR1; known target cell configured with NCD-SSB 2898

A.6.3.1.16.1 Test Purpose and Environment 2898

A.6.3.1.16.2 Test Parameters 2898

A.6.3.1.16.3 Test Requirements 2900

A.6.3.1.17 Handover with PSCell change delay from NR-DC (FR1-FR1) to NR-DC (FR1-FR1) 2900

A.6.3.1.17.1 Test Purpose and Environment 2901

A.6.3.1.17.2 Test Requirements 2904

A.6.3.1.18 Intra-frequency handover from FR1 to FR1; unknown target cell operating with 12 PRB SSB bandwidth 2904

A.6.3.1.18.2 Test Parameters 2905

A.6.3.1.18.3 Test Requirements 2905

A.6.3.1.19 Handover with PSCell change delay where target PSCell is with 12PRB SSB bandwidth 2906

A.6.3.1.19.1 Test Purpose and Environment 2906

A.6.3.1.19.2 Test Parameters 2906

A.6.3.1.19.3 Test Requirements 2908

A.6.3.2 RRC Connection Mobility Control 2909

A.6.3.2.1 SA: RRC Re-establishment 2909

A.6.3.2.1.1 Intra-frequency RRC Re-establishment in FR1 2909

A.6.3.2.1.2 Inter-frequency RRC Re-establishment in FR1 2912

A.6.3.2.1.3 Intra-frequency RRC Re-establishment in FR1 without serving cell timing 2914

A.6.3.2.2 Random Access 2917

A.6.3.2.2.1 4-step RA type contention based random access test in FR1 for NR standalone 2917

A.6.3.2.2.2 4-step RA type non-contention based random access test in FR1 for NR standalone 2920

A.6.3.2.2.3 2-step RA type contention based random access test in FR1 for NR standalone 2923

A.6.3.2.2.4 2-step RA type non-contention based test in FR1 for NR standalone 2925

A.6.3.2.3 SA: RRC Connection Release with Redirection 2928

A.6.3.2.3.1 Redirection from NR in FR1 to NR in FR1 2928

A.6.3.2.3.2 Redirection from NR in FR1 to E-UTRAN 2930

A.6.3.2.4 LTM PDCCH-order Random Access 2933

A.6.3.2.4.1 PDCCH-order RACH on neighbor cell in FR1 when RACH BW is within active UL BWP 2933

A.6.3.2.4.2 PDCCH-ordered RACH to an inter-frequency candidate cell in FR1 for LTM 2937

A.6.3.2.4.3 PDCCH-order RACH on neighbor cell without L1-RSRP measurement in FR1 when RACH BW is within active UL BWP 2941

A.6.3.3 Conditional handover 2944

A.6.3.3.1 Intra-frequency conditional handover from FR1 to FR1 2944

A.6.3.3.1.1 Test Purpose and Environment 2944

A.6.3.3.1.2 Test Parameters 2944

A.6.3.3.1.3 Test Requirements 2946

A.6.3.3.2 Inter-frequency conditional handover from FR1 to FR1 2946

A.6.3.3.2.1 Test Purpose and Environment 2946

A.6.3.3.2.2 Test Parameters 2946

A.6.3.3.2.3 Test Requirements 2948

A.6.3.3.3 NR conditional handover including target MCG and target SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC 2948

A.6.3.3.3.1 Test Purpose and Environment 2948

A.6.3.3.3.2 Test Requirements 2951

A.6.3.3.4 NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC 2952

A.6.3.3.4.1 Test Purpose and Environment 2952

A.6.3.3.4.2 Test Parameters 2952

A.6.3.3.4.3 Test Requirements 2956

A.6.3.3.5 NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC with complementary conditional handover configuration 2956

A.6.3.3.5.1 Test Purpose and Environment 2956

A.6.3.3.5.2 Test Parameters 2956

A.6.3.3.5.3 Test Requirements 2960

A.6.3.3.6 NES triggering intra-frequency conditional handover from FR1 to FR1 2960

A.6.3.3.6.1 Test Purpose and Environment 2960

A.6.3.3.6.2 Test Parameters 2960

A.6.3.3.6.3 Test Requirements 2962

A.6.3.3.7 NES-based Inter-frequency conditional handover from FR1 to FR1 2962

A.6.3.3.7.1 Test Purpose and Environment 2962

A.6.3.3.7.2 Test Parameters 2962

A.6.3.3.7.3 Test Requirements 2964

A.6.3.4 LTM PCell Switch 2964

A.6.3.4.1 RACH-based Intra-frequency PCell switch from FR1 to FR1 2964

A.6.3.4.1.1 Test Purpose and Environment 2964

A.6.3.4.1.2 Test Parameters 2964

A.6.3.4.1.3 Test Requirements 2967

A.6.3.4.2 RACH based Inter-frequency LTM PCell switch from FR1 to FR1 2968

A.6.3.4.2.1 Test Purpose and Environment 2968

A.6.3.4.2.2 Test Parameters 2968

A.6.3.4.2.3 Test Requirements 2971

A.6.3.4.3 RACH-less Intra-frequency PCell switch from FR1 to FR1 2972

A.6.3.4.3.1 Test Purpose and Environment 2972

A.6.3.4.3.2 Test Parameters 2972

A.6.3.4.3.3 Test Requirements 2976

A.6.3.4.4 RACH-less Intra-frequency PCell switch from FR1 to FR1 without L1-RSRP measurement 2976

A.6.3.4.4.1 Test Purpose and Environment 2976

A.6.3.4.4.2 Test Parameters 2976

A.6.3.4.4.3 Test Requirements 2980

A.6.3.5 LTM PSCell Switch 2980

A.6.3.5.1 RACH-based intra-frequency LTM PSCell switch from FR1 to FR1 2980

A.6.3.5.1.1 Test Purpose and Environment 2980

A.6.3.5.1.2 Test Parameters 2980

A.6.3.5.1.3 Test Requirements 2985

A.6.3.6 CLTM PCell Switch 2985

A.6.3.6.1 RACH-based intra-frequency CLTM PCell switch from FR1 to FR1 triggered by SSB based L1-RSRP measurement 2985

A.6.3.6.1.1 Test Purpose and Environment 2985

A.6.3.6.1.2 Test Parameters 2985

A.6.3.6.1.3 Test Requirements 2988

A.6.3.6.2 RACH-based inter-frequency CLTM PCell switch from FR1 to FR1 triggered by SSB based L1-RSRP measurement 2989

A.6.3.6.2.1 Test Purpose and Environment 2989

A.6.3.6.2.2 Test Parameters 2989

A.6.3.6.2.3 Test Requirements 2994

A.6.3.6.3 RACH-less intra-frequency CLTM PCell switch from FR1 to FR1 triggered by SSB-based L1-RSRP measurement 2994

A.6.3.6.3.1 Test Purpose and Environment 2994

A.6.3.6.3.2 Test Parameters 2994

A.6.3.6.3.3 Test Requirements 2998

A.6.3.6.4 RACH-less intra-frequency CLTM Pcell switch from FR1 to FR1 triggered by SSB-based L3-RSRP measurement 2998

A.6.3.6.4.1 Test Purpose and Environment 2998

A.6.3.6.4.2 Test Parameters 2998

A.6.3.6.4.3 Test Requirements 3002

A.6.4 Timing 3003

A.6.4.1 UE transmit timing 3003

A.6.4.1.1 NR UE Transmit Timing Test for FR1 3003

A.6.4.1.1.1 Test Purpose and environment 3003

A.6.4.1.1.2 Test requirements 3005

A.6.4.1.2 NR UE Transmit Timing Test for two TRPs in FR1 3005

A.6.4.1.2.1 Test Purpose and environment 3005

A.6.4.1.2.2 Test requirements 3008

A.6.4.1.3 NR UE Transmit Timing Test with 2-TA and two TRPs for FR1 UE supporting single DCI 3009

A.6.4.1.3.1 Test Purpose and environment 3009

A.6.4.1.3.2 Test requirements 3012

A.6.4.2 UE timer accuracy 3012

A.6.4.3 Timing advance 3012

A.6.4.3.1 SA FR1 timing advance adjustment accuracy 3012

A.6.4.3.1.1 Test Purpose and Environment 3012

A.6.4.3.1.2 Test Parameters 3012

A.6.4.3.1.3 Test Requirements 3015

A.6.4.3.2 SA FR1 timing advance adjustment accuracy for asymmetric DL sTRP/UL mTRP deployment with two TAs 3015

A.6.4.3.2.1 Test Purpose and Environment 3015

A.6.4.3.2.2 Test Parameters 3015

A.6.4.3.2.3 Test Requirements 3018

A.6.5 Signalling characteristics 3018

A.6.5.1 Radio link Monitoring 3018

A.6.5.1.1 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode 3019

A.6.5.1.1.1 Test Purpose and Environment 3019

A.6.5.1.1.2 Test Requirements 3021

A.6.5.1.2 Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode 3022

A.6.5.1.2.1 Test Purpose and Environment 3022

A.6.5.1.2.2 Test Requirements 3024

A.6.5.1.3 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode 3024

A.6.5.1.3.1 Test Purpose and Environment 3025

A.6.5.1.3.2 Test Requirements 3027

A.6.5.1.4 Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode 3027

A.6.5.1.4.1 Test Purpose and Environment 3027

A.6.5.1.4.2 Test Requirements 3030

A.6.5.1.5 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode 3030

A.6.5.1.5.1 Test Purpose and Environment 3030

A.6.5.1.5.2 Test Requirements 3033

A.6.5.1.6 Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode 3033

A.6.5.1.6.1 Test Purpose and Environment 3033

A.6.5.1.6.2 Test Requirements 3036

A.6.5.1.7 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode 3037

A.6.5.1.7.1 Test Purpose and Environment 3037

A.6.5.1.7.2 Test Requirements 3039

A.6.5.1.8 Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode 3040

A.6.5.1.8.1 Test Purpose and Environment 3040

A.6.5.1.8.2 Test Requirements 3043

A.6.5.1.9 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM for UE fulfilling relaxed measurement criterion 3043

A.6.5.1.9.1 Test Purpose and Environment 3043

A.6.5.1.9.2 Test Requirements 3046

A.6.5.1.10 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP 3046

A.6.5.1.10.1 Test Purpose and Environment 3046

A.6.5.1.11 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP 3047

A.6.5.1.11.1 Test Purpose and Environment 3047

A.6.5.1.11.2 Test Requirements 3047

A.6.5.1.12 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP 3047

A.6.5.1.12.1 Test Purpose and Environment 3047

A.6.5.1.12.2 Test Requirements 3050

A.6.5.1.13 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for UE operating on a cell with less than 5 MHz BW 3050

A.6.5.1.13.1 Test Purpose and Environment 3050

A.6.5.1.13.2 Test Requirements 3051

A.6.5.1.14 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for UE operating on a cell with less than 5 MHz BW 3051

A.6.5.1.14.1 Test Purpose and Environment 3051

A.6.5.1.14.2 Test Requirements 3052

A.6.5.1.15 Radio Link Monitoring In-sync Test for FR1 PCell with 3 MHz Channel Bandwidth configured with SSB-based RLM RS in non-DRX mode 3052

A.6.5.1.15.1 Test Purpose and Environment 3052

A.6.5.1.15.2 Test Requirements 3053

A.6.5.1.16 Radio Link Monitoring In-sync Test for FR1 PCell with 3MHz Channel Bandwidth configured with SSB-based RLM RS in DRX mode 3053

A.6.5.1.16.1 Test Purpose and Environment 3053

A.6.5.1.16.2 Test Requirements 3054

Test requirements specified in Clause A.6.5.1.4.2 apply to this test.A.6.5.1.17 Radio Link Monitoring Out-of-sync Test for FR1 PCell with LowBandCA-Switching-r19 configured with SSB-based RLM RS in non-DRX mode 3054

A.6.5.1.17.1 Test Purpose and Environment 3054

A.6.5.1.17.2 Test Requirements 3056

A.6.5.1.18 Radio Link Monitoring In-sync Test for FR1 PCell with LowBandCA-Switching-r19 configured with SSB-based RLM RS in non-DRX mode 3057

A.6.5.1.18.1 Test Purpose and Environment 3057

A.6.5.1.18.2 Test Requirements 3059

A.6.5.1.19 Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for a UE operating with SBFD 3059

A.6.5.1.19.1 Test Purpose and Environment 3059

A.6.5.1.19.2 Test Requirements 3062

A.6.5.2 Interruption 3062

A.6.5.2.1 Interruptions during measurements on deactivated NR SCC in FR1 3062

A.6.5.2.1.1 Test Purpose and Environment 3062

A.6.5.2.1.2 Test Requirements 3065

A.6.5.2.1A Interruptions during measurements on deactivated NR SCC in FR1 for UE supporting intraBandNR-CA-non-collocated-r19 3066

A.6.5.2.1A.1 Test Purpose and Environment 3066

A.6.5.2.1A.2 Test Requirements 3070

A.6.5.2.2 SA interruptions at NR SRS carrier based switching 3070

A.6.5.2.2.1 Test Purpose and Environment 3070

A.6.5.2.2.2 Test Parameters 3071

A.6.5.2.2.3 Test Requirements 3073

A.6.5.2.3 SA interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in NR-CA 3073

A.6.5.2.3.1 Test Purpose and Environment 3073

A.6.5.2.3.2 Test Parameters 3073

A.6.5.2.3.3 Test Requirements 3075

A.6.5.2.4 SA interruptions at NR SRS antenna port switching 3076

A.6.5.2.4.1 Test Purpose and Environment 3076

A.6.5.2.4.2 Test Parameters 3076

A.6.5.2.4.3 Test Requirements 3078

A.6.5.2.5 Interruptions during measurements on deactivated NR SCC in FR1 3079

A.6.5.2.5.1 Test Purpose and Environment 3079

A.6.5.2.5.2 Test Requirements 3081

A.6.5.3 SCell Activation and Deactivation Delay 3081

A.6.5.3.1 SCell Activation and deactivation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle 3081

A.6.5.3.1.1 Test Purpose and Environment 3082

A.6.5.3.1.2 Test Requirements 3086

A.6.5.3.2 SCell Activation and deactivation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle 3086

A.6.5.3.2.1 Test Purpose and Environment 3086

A.6.5.3.2.2 Test Requirements 3087

A.6.5.3.3 SCell Activation and deactivation of unknown SCell in FR1 in non-DRX 3087

A.6.5.3.3.1 Test Purpose and Environment 3087

A.6.5.3.3.2 Test Requirements 3088

A.6.5.3.4 Direct SCell activation at SCell addition of known SCell in FR1 3088

A.6.5.3.4.1 Test Purpose and Environment 3088

A.6.5.3.4.2 Test Requirements 3091

A.6.5.3.5 Direct SCell activation at handover with known SCell in FR1 3092

A.6.5.3.5.1 Test Purpose and Environment 3092

A.6.5.3.5.2 Test Requirements 3096

A.6.5.3.6 PUCCH SCell Activation and deactivation of known SCell in FR1 3097

A.6.5.3.6.1 Test Purpose and Environment 3097

A.6.5.3.6.2 Test Requirements 3100

A.6.5.3.7 SCell Activation and deactivation of unknown SCell in FR1 in non-DRX 3100

A.6.5.3.7.1 Test Purpose and Environment 3100

A.6.5.3.7.2 Test Requirements 3103

A.6.5.3.8 SCell Activation and Deactivation of one FR1 known PUCCH SCell and one FR1 unknown SCell with single activation/deactivation command 3104

A.6.5.3.8.1 Test Purpose and Environment 3104

A.6.5.3.8.2 Test Requirements 3107

A.6.5.3.9 SCell Activation and deactivation of unknown PUCCH SCell and unknown DL SCell in FR1 in non-DRX 3108

A.6.5.3.9.1 Test Purpose and Environment 3108

A.6.5.3.9.2 Test Requirements 3111

A.6.5.3.10 Fast SCell Activation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle 3111

A.6.5.3.10.1 Test Purpose and Environment 3111

A.6.5.3.10.2 Test Requirements 3114

A.6.5.3.11 SCell Activation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle 3115

A.6.5.3.11.1 Test Purpose and Environment 3115

A.6.5.3.11.2 Test Requirements 3115

A.6.5.3.12 SCell Activation and deactivation of unknown SCell in FR1 in DRX for UE capable of short measurement interval 3115

A.6.5.3.12.1 Test Purpose and Environment 3115

A.6.5.3.12.2 Test Requirements 3118

A.6.5.3.13 SCell Activation of multiple unknown SCells in FR1 with L3 reporting with single activation/deactivation commandin non-DRX 3118

A.6.5.3.13.1 Test Purpose and Environment 3118

A.6.5.3.13.2 Test Requirements 3123

A.6.5.3.14 SCell Activation of unknown SCell with valid L3 measurement results in FR1 in non-DRX for 160 ms SCell measurement cycle 3123

A.6.5.3.14.1 Test Purpose and Environment 3123

A.6.5.3.14.2 Test Requirements 3128

A.6.5.3.15 TRS based SCell Activation of SSB-less SCell in FR1 inter-band CA in non-DRX 3129

A.6.5.3.15.1 Test Purpose and Environment 3129

A.6.5.3.15.2 Test Requirements 3133

A.6.5.3.16 Inter-band SSB-less SCell Activation based on A-TRS 3133

A.6.5.3.16.1 Test Purpose and Environment 3133

A.6.5.3.16.2 Test Requirements 3137

A.6.5.3.17.1 Test Purpose and Environment 3138

A.6.5.3.17.2 Test Requirements 3139

A.6.5.3.18 OD-SSB based SCell Activation and deactivation of unknown SCell in FR1 in DRX (OD-SSB Case 1) 3139

A.6.5.3.18.1 Test Purpose and Environment 3139

A.6.5.3.18.2 Test Requirements 3143

A.6.5.3.19 OD-SSB based SCell Activation and deactivation of unknown SCell in FR1 DRX mode(OD-SSB Case 2, Alt Time-C1) 3144

A.6.5.3.19.1 Test Purpose and Environment 3144

A.6.5.3.19.2 Test Requirements 3148

A.6.5.3.20 OD-SSB based SCell Activation and deactivation of known SCell in FR1 non-DRX mode(OD-SSB Case 2, Alt Time-C1) 3149

A.6.5.3.20.1 Test Purpose and Environment 3149

A.6.5.3.20.2 Test Requirements 3154

A.6.5.3.21 OD-SSB based Direct SCell activation at SCell addition in FR1(OD-SSB Case 2) 3154

A.6.5.3.21.1 Test Purpose and Environment 3154

A.6.5.3.21.2 Test Requirements 3158

A.6.5.3.22 OD-SSB based Direct SCell activation at SCell addition in FR1 without first SSB transmission 3158

A.6.5.3.22.1 Test Purpose and Environment 3158

A.6.5.3.22.2 Test Requirements 3161

A.6.5.3.23 SDL SCell Activation and deactivation of unknown SCell in FR1 for LBCA 3161

A.6.5.3.23.1 Test Purpose and Environment 3161

A.6.5.3.23.2 Test Requirements 3162

A.6.5.3.24 Direct SCell activation at SCell addition of known SCell in FR1 for LBCA 3162

A.6.5.3.24.1 Test Purpose and Environment 3162

A.6.5.3.24.2 Test Requirements 3163

A.6.5.3.25 PUCCH SCell Activation and deactivation for UE supporting EMR in FR1 3164

A.6.5.3.25.1 Test Purpose and Environment 3164

A.6.5.3.25.2 Test Requirements 3167

A.6.5.3.26 EMR based SCell activation of unknown SCell in FR1 3167

A.6.5.3.26.1 Test Purpose and Environment 3167

A.6.5.3.26.2 Test Requirements 3172

A.6.5.3.27 EMR based Direct SCell activation at SCell addition of unknown SCell in FR1 3172

A.6.5.3.27.1 Test Purpose and Environment 3172

A.6.5.3.27.2 Test Requirements 3176

A.6.5.4 UE UL carrier RRC reconfiguration Delay 3176

A.6.5.4.1 UE UL carrier RRC reconfiguration Delay 3176

A.6.5.4.1.1 Test Purpose and Environment 3176

A.6.5.4.1.2 Test Requirements 3179

A.6.5.4.2 Void 3179

A.6.5.5 Beam Failure Detection and Link recovery procedures 3179

A.6.5.5.1 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode 3179

A.6.5.5.1.1 Test Purpose and Environment 3179

A.6.5.5.1.2 Test Requirements 3183

A.6.5.5.2 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode 3183

A.6.5.5.2.1 Test Purpose and Environment 3183

A.6.5.5.2.2 Test Requirements 3187

A.6.5.5.3 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode 3187

A.6.5.5.3.1 Test Purpose and Environment 3187

A.6.5.5.3.2 Test Requirements 3190

A.6.5.5.4 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode 3191

A.6.5.5.4.1 Test Purpose and Environment 3191

A.6.5.5.4.2 Test Requirements 3195

A.6.5.5.5 Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode 3195

A.6.5.5.5.1 Test Purpose and Environment 3195

A.6.5.5.5.2 Test Requirements 3198

A.6.5.5.6 Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in DRX mode 3199

A.6.5.5.6.1 Test Purpose and Environment 3199

A.6.5.5.6.2 Test Requirements 3202

A.6.5.5.7 TRP Specific Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode 3203

A.6.5.5.7.1 Test Purpose and Environment 3203

A.6.5.5.7.2 Test Requirements 3206

A.6.5.5.8 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for a UE operating on a cell with less than 5 MHz BW 3207

A.6.5.5.8.1 Test Purpose and Environment 3207

A.6.5.5.8.2 Test Requirements 3208

A.6.5.5.9 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode for a UE operating with SBFD 3208

A.6.5.5.9.1 Test Purpose and Environment 3208

A.6.5.5.9.2 Test Requirements 3209

A.6.5.6 Active BWP switch 3209

A.6.5.6.1 DCI-based and Timer-based Active BWP Switch 3209

A.6.5.6.1.1 NR FR1- NR FR1 DL active BWP switch of SCell with non-DRX in SA 3209

A.6.5.6.1.2 NR FR1 DL active BWP switch with non-DRX in SA 3214

A.6.5.6.2 RRC-based Active BWP Switch 3217

A.6.5.6.2.1 NR FR1 DL active BWP switch of Cell with non-DRX in SA 3217

A.6.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs 3219

A.6.5.6.3.1 NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA 3219

A.6.5.6.4 SCell dormancy switch 3225

A.6.5.6.4.1 NR FR1 PCell SCell dormancy switch of single FR1 SCell outside active time 3225

A.6.5.6.4.1.1 Test Purpose and Environment 3225

A.6.5.6.4.1.2 Test Requirements 3229

A.6.5.6.4.2 NR FR1 PCell SCell dormancy switch of two FR1 SCells inside active time 3230

A.6.5.6.4.2.1  Test Purpose and Environment 3230

A.6.5.6.4.2.2 Test Requirements 3235

A.6.5.6.5 Simultaneous RRC-based Active BWP Switch on multiple CCs 3235

A.6.5.6.5.1 NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA 3235

A.6.5.7 DL interruptions at switching between two uplink carriers 3239

A.6.5.7.1 DL interruptions at switching between two uplink carriers in FDD-TDD CA 3239

A.6.5.7.1.1 Test Purpose and Environment 3239

A.6.5.7.1.2 Test Requirements 3243

A.6.5.7.2 DL interruptions at switching between two uplink carriers in TDD-TDD CA 3243

A.6.5.7.2.1 Test Purpose and Environment 3243

A.6.5.7.2.2 Test Requirements 3246

A.6.5.7A DL interruptions at switching between two uplink carriers with two transmit antenna connectors 3246

A.6.5.7A.1 DL interruptions at switching between two uplink carriers in FDD-TDD CA 3246

A.6.5.7A.1.1 Test Purpose and Environment 3246

A.6.5.7A.1.2 Test Requirements 3250

A.6.5.7A.2 DL interruptions at switching between two uplink carriers in TDD-TDD CA 3250

A.6.5.7A.2.1 Test Purpose and Environment 3250

A.6.5.7A.2.2 Test Requirements 3252

A.6.5.7B DL interruptions at switching between one uplink band with one transmit antenna connector and one uplink band with two transmit antenna connectors 3253

A.6.5.7B.1 DL interruptions at switching between two uplink bands in FDD-TDD CA 3253

A.6.5.7B.1.1 Test Purpose and Environment 3253

A.6.5.7B.1.2 Test Requirements 3257

A.6.5.7B.2 DL interruptions at switching between two uplink bands in TDD-TDD CA 3257

A.6.5.7B.2.1 Test Purpose and Environment 3257

A.6.5.7B.2.2 Test Requirements 3262

A.6.5.7C DL interruptions at switching between two uplink bands with two transmit antenna connectors 3262

A.6.5.7C.1 DL interruptions at switching between two uplink bands with two transmit antenna connectors in FDD-TDD CA 3262

A.6.5.7C.1.1 Test Purpose and Environment 3262

A.6.5.7C.1.2 Test Requirements 3268

A.6.5.7C.2 DL interruptions at switching between two uplink bands with two transmit antenna connectors in TDD-TDD CA 3268

A.6.5.7C.2.1 Test Purpose and Environment 3268

A.6.5.7C.2.2 Test Requirements 3273

A.6.5.7D DL interruptions at UE switching across three or four uplink bands 3273

A.6.5.7D.1 DL interruptions at switching across three uplink bands in TDD-TDD CA for single TAG 3273

A.6.5.7D.1.1 Test Purpose and Environment 3273

A.6.5.7D.1.2 Test Requirements 3277

A.6.5.7D.2 DL interruptions at switching across four uplink bands in FDD-TDD CA for single TAG 3277

A.6.5.7D.2.1 Test Purpose and Environment 3277

A.6.5.7D.2.2 Test Requirements 3281

A.6.5.7D.3 DL interruptions at switching across three uplink bands in FDD-TDD CA for two TAGs 3281

A.6.5.7D.3.1 Test Purpose and Environment 3281

A.6.5.7D.3.2 Test Requirements 3285

A.6.5.7D.4 DL interruptions at switching across four uplink bands in TDD-TDD CA for two TAGs 3285

A.6.5.7D.4.1 Test Purpose and Environment 3285

A.6.5.7D.7.2 Test Requirements 3290

A.6.5.8 UE specific CBW change 3290

A.6.5.8.1 UE specific CBW change on PCell in FR1 in non-DRX 3290

A.6.5.8.1.1 Test Purpose and Environment 3290

A.6.5.8.1.2 Test Requirements 3292

A.6.5.9 Pathloss reference signal switching delay 3292

A.6.5.9.1 MAC-CE based pathloss reference signal switch delay 3292

A.6.5.9.1.1 Test Purpose and Environment 3292

A.6.5.9.1.2 Test Requirements 3295

A.6.5.9.2 MAC-CE based pathloss reference signal switch delay  for LB CA 3295

A.6.5.9.2.1 Test Purpose and Environment 3295

A.6.5.9.2.2 Test Requirements 3296

A.6.5.10 Conditional PSCell addition and release delay (FR1 NR-DC) 3296

A.6.5.10.1 Conditional PSCell Addition and Release Delay 3296

A.6.5.10.1.1 Test purpose and environment 3296

A.6.5.10.1.2 Test Parameters 3296

A.6.5.10.1.3 Test Requirements 3299

A.6.5.11 PSCell addition and release delay 3299

A.6.5.11.1 Addition and Release Delay of unknown NR FR1 PSCell 3299

A.6.5.11.1.1 Test purpose and environment 3299

A.6.5.11.1.2 Test Requirements 3301

A.6.5.11.2 Addition and Release Delay of unknown NR FR1 PSCell with less than 5 MHz 3302

A.6.5.11.2.1 Test purpose and environment 3302

A.6.5.11.2.2 Test Requirements 3302

A.6.5.12 Subsequent conditional PSCell addition/change 3303

A.6.5.12.1 Intra-frequency subsequent CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC 3303

A.6.5.12.1.1 Test purpose and environment 3303

A.6.5.12.1.2 Test Parameters 3303

A.6.5.12.1.3 Test Requirements 3305

A.6.5.12.2 Inter-frequency subsequent CPA from FR1-FR1 NR-DC to FR1-FR1 NR-DC 3306

A.6.5.12.2.1 Test purpose and environment 3306

A.6.5.12.2.2 Test Parameters 3306

A.6.5.12.2.3 Test Requirements 3309

A.6.5.12.3 Intra-frequency subsequent CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC with 12 PRB SSB bandwidth 3309

A.6.5.12.3.1 Test purpose and environment 3309

A.6.5.12.3.2 Test Parameters 3309

A.6.5.12.3.3 Test Requirements 3310

A.6.5.12.4 Inter-frequency subsequent CPA from FR1-FR1 NR-DC to FR1-FR1 NR-DC with 12 PRB SSB bandwidth 3310

A.6.5.12.4.1 Test purpose and environment 3310

A.6.5.12.4.2 Test Parameters 3310

A.6.5.12.4.3 Test Requirements 3311

A.6.5.13 Active TCI state switch delay 3311

A.6.5.13.1 MAC-CE based joint TCI state switch for mDCI with two TA when RTD is larger than CP 3312

A.6.5.13.1.1 Test Purpose and Environment 3312

A.6.5.13.1.2 Test Requirements 3314

A.6.6 Measurement procedure 3315

A.6.6.1 Intra-frequency Measurements 3315

A.6.6.1.1 SA event triggered reporting tests without gap under non-DRX 3315

A.6.6.1.1.1 Test purpose and Environment 3315

A.6.6.1.1.2 Test parameters 3315

A.6.6.1.1.3 Test Requirements 3317

A.6.6.1.2 SA event triggered reporting tests without gap under DRX 3317

A.6.6.1.2.1 Test purpose and Environment 3317

A.6.6.1.2.2 Test parameters 3317

A.6.6.1.2.3 Test Requirements 3319

A.6.6.1.3 SA event triggered reporting tests with per-UE gaps under non-DRX 3319

A.6.6.1.3.1 Test purpose and Environment 3319

A.6.6.1.3.2 Test parameters 3319

A.6.6.1.3.3 Test Requirements 3321

A.6.6.1.4 SA event triggered reporting tests with per-UE gaps under DRX 3321

A.6.6.1.4.1 Test purpose and Environment 3321

A.6.6.1.4.2 Test parameters 3322

A.6.6.1.4.3 Test Requirements 3324

A.6.6.1.5 SA event triggered reporting tests without gap under non-DRX with SSB index reading 3324

A.6.6.1.5.1 Test purpose and Environment 3324

A.6.6.1.5.2 Test parameters 3324

A.6.6.1.5.3 Test Requirements 3325

A.6.6.1.6 SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading 3325

A.6.6.1.6.1 Test purpose and Environment 3325

A.6.6.1.6.2 Test parameters 3326

A.6.6.1.6.3 Test Requirements 3327

A.6.6.1.7 SA event triggered reporting tests under DRX for UE configured with highSpeedMeasFlag-r16 3327

A.6.6.1.7.1 Test purpose and Environment 3327

A.6.6.1.7.2 Test parameters 3327

A.6.6.1.7.3 Test Requirements 3329

A.6.6.1.8 SA event triggered reporting tests without gap under DRX for UE configured with highSpeedMeasCA-Scell-r17 3330

A.6.6.1.8.1 Test purpose and Environment 3330

A.6.6.1.8.2 Test parameters 3330

A.6.6.1.8.3 Test Requirements 3332

A.6.6.1.9 SA event triggered reporting tests with MUSIM gap configured 3332

A.6.6.1.9.1 Test purpose and Environment 3332

A.6.6.1.9.2 Test parameters 3332

A.6.6.1.9.3 Test requirements 3334

A.6.6.1.10 SA event triggered reporting tests without gap under non-DRX when CD-SSB is outside active BWP 3334

A.6.6.1.10.1 Test purpose and Environment 3334

A.6.6.1.10.2 Test Requirements 3335

A.6.6.1.11 SA event triggered reporting tests without gap under non-DRX with NCD-SSB 3335

A.6.6.1.11.1 Test purpose and Environment 3335

A.6.6.1.11.2 Test parameters 3335

A.6.6.1.11.3 Test Requirements 3336

A.6.6.1.12 SA event triggered reporting tests without gap under non-DRX with SSB index reading and 12 PRB SSB 3337

A.6.6.1.12.1 Test purpose and Environment 3337

A.6.6.1.12.2 Test parameters 3337

A.6.6.1.12.3 Test Requirements 3337

A.6.6.1.13 SA event triggered reporting tests without gap under Cell DTX 3337

A.6.6.1.13.1 Test purpose and Environment 3338

A.6.6.1.13.2 Test parameters 3338

A.6.6.1.13.3 Test Requirements 3339

A.6.6.1.14 Deactivated PSCell measurement test with 12 PRB SSB bandwidth in FR1 3340

A.6.6.1.14.1 Test Purpose and Environment 3340

A.6.6.1.14.2 Test Parameters 3340

A.6.6.1.14.3 Test Requirements 3343

A.6.6.1.15 SA event triggered reporting test without gap under non-DRX with SSB index reading and 12 PRB SSB for a deactivated SCell 3343

A.6.6.1.15.1 Test purpose and Environment 3343

A.6.6.1.15.2 Test parameters 3343

A.6.6.1.15.3 Test requirements 3345

A.6.6.1.16 OD-SSB based deactivated SCell measurement under non-DRX mode in FR1 (OD-SSB Case 1) 3345

A.6.6.1.16.1 Test Purpose and Environment 3345

A.6.6.1.16.2 Test Requirements 3351

A.6.6.1.17 SA event triggered reporting test without gap under non-DRX on deactivated SCell based on OD-SSB 3352

A.6.6.1.17.1 Test purpose and Environment 3352

A.6.6.1.17.2 Test Requirements 3354

A.6.6.1.18 SA event triggered reporting tests without gap under non-DRX based on OD-SSB 3355

A.6.6.1.18.1 Test purpose and Environment 3355

A.6.6.1.18.2 Test parameters 3355

A.6.6.1.18.3 Test Requirements 3357

A.6.6.1.19 SA event triggered reporting test for a UE configured with LB CA via switching 3357

A.6.6.1.19.1 Test purpose and Environment 3357

A.6.6.1.19.2 Test parameters 3357

A.6.6.1.19.3 Test requirements 3360

A.6.6.1.20 SA event triggered reporting tests without gap under non-DRX in FR1 for UE supporting [FR1 only CA and FR1 only NR-DC 3-searcher capability] 3360

A.6.6.1.20.1 Test purpose and Environment 3360

A.6.6.1.20.2 Test parameters 3361

A.6.6.1.20.3 Test Requirements 3365

A.6.6.2 Inter-frequency Measurements 3365

A.6.6.2.1 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used 3365

A.6.6.2.1.1 Test Purpose and Environment 3365

A.6.6.2.1.2 Test Requirements 3368

A.6.6.2.2 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used 3368

A.6.6.2.2.1 Test Purpose and Environment 3368

A.6.6.2.2.2 Test Requirements 3371

A.6.6.2.3 Void 3371

A.6.6.2.4 Void 3371

A.6.6.2.5 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used 3371

A.6.6.2.5.1 Test Purpose and Environment 3371

A.6.6.2.5.2 Test Requirements 3373

A.6.6.2.6 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used 3373

A.6.6.2.6.1 Test Purpose and Environment 3374

A.6.6.2.6.2 Test Requirements 3376

A.6.6.2.7 Void 3376

A.6.6.2.8 Void 3376

A.6.6.2.9 SA event triggered reporting tests with additional mandatory gap pattern 3376

A.6.6.2.9.1 Test Purpose and Environment 3376

A.6.6.2.9.2 Test Requirements 3378

A.6.6.2.10 SA event triggered reporting tests for FR1 when DRX is used 3379

A.6.6.2.10.1 Test Purpose and Environment 3379

A.6.6.2.10.2 Test Requirements 3381

A.6.6.2.12 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for UE configured with highSpeedMeasInterFreq-r17 3384

A.6.6.2.12.1 Test Purpose and Environment 3384

A.6.6.2.12.2 Test Requirements 3386

A.6.6.2.13 SA event triggered reporting tests for FR1 with measurement gap with priority and periodic MUSIM gap configured 3387

A.6.6.2.13.1 Test Purpose and Environment 3387

A.6.6.2.13.2 Test Requirements 3389

A.6.6.2.14 SA event triggered reporting tests for FR1 with measurement gap without priority and periodic MUSIM gap configured 3389

A.6.6.2.14.1 Test Purpose and Environment 3389

A.6.6.2.14.2 Test Requirements 3392

A.6.6.2.15 SA event triggered reporting tests for FR1 with 3 MHz Channel Bandwidth configured with SSB time index detection when DRX is used 3392

A.6.6.2.15.1 Test Purpose and Environment 3392

A.6.6.2.15.2 Test Requirements 3393

A.6.6.2.16 SA event triggered reporting tests with SSB adaptation without SSB time index detection without gap under non-DRX 3393

A.6.6.2.16.1 Test purpose and Environment 3393

A.6.6.2.16.2 Test parameters 3393

A.6.6.2.16.3 Test Requirements 3395

A.6.6.2.17 SA event triggered reporting tests under non-DRX 3395

A.6.6.2.17.1 Test purpose and Environment 3395

A.6.6.2.17.2 Test parameters 3396

A.6.6.2.17.3 Test Requirements 3398

A.6.6.2.18 SA event-triggered reporting tests for FR1 without SSB time index detection when DRX is not used for UE configured with measurement gap cancellation 3398

A.6.6.2.18.1 Test Purpose and Environment 3398

A.6.6.2.18.2 Test Requirements 3399

A.6.6.3 Inter-RAT Measurements 3399

A.6.6.3.1 SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 3399

A.6.6.3.1.1 Test Purpose and Environment 3399

A.6.6.3.1.2 Test Requirements 3402

A.6.6.3.2 SA NR - E-UTRAN event-triggered reporting in DRX in FR1 3402

A.6.6.3.2.1 Test Purpose and Environment 3402

A.6.6.3.2.2 Test Requirements 3405

A.6.6.3.3 SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for UE configured with highSpeedMeasFlag-r16 3406

A.6.6.3.3.1 Test Purpose and Environment 3406

A.6.6.3.3.2 Test Requirements 3409

A.6.6.4 L1-RSRP measurement for beam reporting 3409

A.6.6.4.1 SSB based L1-RSRP measurement when DRX is not used 3409

A.6.6.4.1.1 Test Purpose and Environment 3409

A.6.6.4.1.2 Test parameters 3409

A.6.6.4.1.3 Test Requirements 3411

A.6.6.4.2 SSB based L1-RSRP measurement when DRX is used 3411

A.6.6.4.2.1 Test Purpose and Environment 3411

A.6.6.4.2.2 Test parameters 3411

A.6.6.4.2.3 Test Requirements 3413

A.6.6.4.3 CSI-RS based L1-RSRP measurement when DRX is not used 3413

A.6.6.4.3.1 Test Purpose and Environment 3413

A.6.6.4.3.2 Test parameters 3413

A.6.6.4.3.3 Test Requirements 3415

A.6.6.4.4 CSI-RS based L1-RSRP measurement when DRX is used 3415

A.6.6.4.4.1 Test Purpose and Environment 3415

A.6.6.4.4.2 Test parameters 3415

A.6.6.4.4.3 Test Requirements 3417

A.6.6.4.5 SSB based L1-RSRP measurement when DRX is used for UE configured with highSpeedMeasFlag-r16 3417

A.6.6.4.5.1 Test Purpose and Environment 3417

A.6.6.4.5.2 Test parameters 3417

A.6.6.4.5.3 Test Requirements 3419

A.6.6.4.6 Inter-cell SSB based L1-RSRP measurements on FR1 PCell when DRX is used 3419

A.6.6.4.6.1 Test Purpose and Environment 3419

A.6.6.4.6.2 Test parameters 3419

A.6.6.4.6.3 Test Requirements 3421

A.6.6.4.7 SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP 3421

A.6.6.4.7.1 Test Purpose and Environment 3421

A.6.6.4.7.2 Test Requirements 3421

A.6.6.4.8 CSI-RS based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP 3421

A.6.6.4.8.1 Test Purpose and Environment 3421

A.6.6.4.9 SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used 3422

A.6.6.4.9.1 Test Purpose and Environment 3422

A.6.6.4.9.2 Test parameters 3422

A.6.6.4.9.3 Test Requirements 3423

A.6.6.4.10 OD-SSB based L1-RSRP measurement when DRX is not used 3424

A.6.6.4.10.1 Test Purpose and Environment 3424

A.6.6.4.10.2 Test parameters 3424

A.6.6.4.10.3 Test Requirements 3427

A.6.6.4.11 Event Triggered Reporting for UE initiated beam management without eventDetectionTimeWindowLength-r19 3427

A.6.6.4.11.1 Test Purpose and Environment 3427

A.6.6.4.11.2 Test parameters 3428

A.6.6.4.11.3 Test Requirements 3430

A.6.6.4.12 Event Triggered Reporting for UE initiated beam management with eventDetectionTimeWindowLength-r19 3430

A.6.6.4.12.1 Test Purpose and Environment 3430

A.6.6.4.12.2 Test parameters 3430

A.6.6.4.12.3 Test Requirements 3432

A.6.6.4.13 Event triggered reporting for UE initiated beam management for UE configured with Inter-cell SSB based L1-RSRP measurement on FR1 when DRX is not used 3432

A.6.6.4.13.1 Test Purpose and Environment 3432

A.6.6.4.13.2 Test Parameters 3432

A.6.6.4.13.3 Test Requirements 3434

A.6.6.4.14 SSB based L1-RSRP measurement on SDL SCell for UE supporting LB CA via switching 3434

A.6.6.4.14.1 Test Purpose and Environment 3434

A.6.6.4.14.2 Test parameters 3435

A.6.6.4.14.3 Test Requirements 3436

A.6.6.4.15 CSI-RS based L1-RSRP measurement when DRX is not used for SBFD aware UE with DU configuration 3436

A.6.6.4.15.1 Test Purpose and Environment 3436

A.6.6.4.15.2 Test parameters 3437

A.6.6.4.15.3 Test Requirements 3438

A.6.6.5 Inter-RAT UTRAN FDD measurements 3438

A.6.6.5.1 SA NR - UTRAN FDD event-triggered reporting in non-DRX in FR1 3438

A.6.6.5.1.1 Test Purpose and Environment 3438

A.6.6.5.1.2 Test Requirements 3440

A.6.6.6 CLI measurements 3440

A.6.6.6.1 SRS-RSRP measurement with DRX 3440

A.6.6.6.1.1 Test Purpose and Environment 3440

A.6.6.6.1.2 Test Parameters 3441

A.6.6.6.1.3 Test Requirements 3443

A.6.6.6.2 CLI-RSSI measurement with DRX 3443

A.6.6.6.2.1 Test Purpose and Environment 3443

A.6.6.6.2.2 Test Parameters 3443

A.6.6.6.2.3 Test Requirements 3444

A.6.6.7 NR measurements with autonomous gaps 3445

A.6.6.7.1 SA intra-frequency CGI identification of NR neighbor cell in FR1 3445

A.6.6.7.1.1 Test Purpose and Environment 3445

A.6.6.7.1.2 Test Parameters 3445

A.6.6.7.1.3 Test Requirements 3448

A.6.6.7.2 Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA 3448

A.6.6.7.2.1 Test Purpose and Environment 3448

A.6.6.7.2.2 Test Requirements 3450

A.6.6.8 L1-SINR measurement for beam reporting 3451

A.6.6.8.1 L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is used 3451

A.6.6.8.1.1 Test Purpose and Environment 3451

A.6.6.8.1.2 Test parameters 3451

A.6.6.8.1.3 Test Requirements 3453

A.6.6.8.2 L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used 3453

A.6.6.8.2.1 Test Purpose and Environment 3453

A.6.6.8.2.2 Test parameters 3453

A.6.6.8.2.3 Test Requirements 3455

A.6.6.8.3 L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used 3455

A.6.6.8.3.1 Test Purpose and Environment 3455

A.6.6.8.3.2 Test parameters 3456

A.6.6.8.3.3 Test Requirements 3457

A.6.6.8.4 L1-SINR measurement with SSB based CMR and dedicated IMR for SSB adaptation 3457

A.6.6.8.4.1 Test Purpose and Environment 3457

A.6.6.8.4.2 Test parameters 3458

A.6.6.8.4.3 Test Requirements 3462

A.6.6.8.5 L1-SINR measurement with SSB based CMR and dedicated IMR with SBFD 3462

A.6.6.8.5.1 Test Purpose and Environment 3462

A.6.6.8.5.2 Test parameters 3462

A.6.6.8.5.3 Test Requirements 3464

A.6.6.9 Idle Mode CA/DC Measurements 3464

A.6.6.9.1 SA Idle mode CA/DC measurement for FR1 3464

A.6.6.9.1.1 Test Purpose and Environment 3464

A.6.6.9.1.2 Test Requirements 3467

A.6.6.9.2  Idle mode fast CA/DC eEMR measurement for FR1 without valid reporting 3468

A.6.6.9.2.1 Test Purpose and Environment 3468

A.6.6.9.2.2 Test Requirements 3470

A.6.6.9.3 Idle mode fast CA/DC cell reselection measurement for FR1 without valid reporting 3470

A.6.6.9.3.1 Test Purpose and Environment 3470

A.6.6.9.3.2 Test Requirements 3473

A.6.6.9.4 Idle mode fast CA/DC cell reselection measurement for FR1 with valid reporting 3473

A.6.6.9.4.1 Test Purpose and Environment 3473

A.6.6.9.4.2 Test Requirements 3476

A.6.6.9.5 SA Idle mode CA/DC measurement for FR1 with 12RB SSB 3476

A.6.6.9.5.1 Test Purpose and Environment 3476

A.6.6.9.5.2 Test Requirements 3477

A.6.6.10 CSI-RS based intra-frequency Measurements 3477

A.6.6.10.1 SA event triggered reporting tests without gap under non-DRX 3477

A.6.6.10.1.1 Test purpose and Environment 3477

A.6.6.10.1.2 Test Requirements 3479

A.6.6.11 CSI-RS based inter-frequency Measurements 3479

A.6.6.11.1  SA event triggered reporting tests with gap under DRX 3479

A.6.6.11.1.1 Test Purpose and Environment 3479

A.6.6.11.1.2 Test Requirements 3482

A.6.6.12 RSTD measurements 3482

A.6.6.12.1 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA 3482

A.6.6.12.1.1 Test Purpose and Environment 3482

A.6.6.12.1.2 Test Requirements 3485

A.6.6.12.2 NR RSTD measurement reporting delay test case for dual positioning frequency layers in FR1 SA 3486

A.6.6.12.2.1 Test Purpose and Environment 3486

A.6.6.12.2.2 Test Requirements 3489

A.6.6.12.3 NR RSTD measurement reporting delay test case for single positioning frequency layer with reduced number of samples in FR1 SA 3489

A.6.6.12.3.1 Test Purpose and Environment 3489

A.6.6.12.3.2 Test Requirements 3492

A.6.6.12.4 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA without measurement gap 3493

A.6.6.12.4.1 Test Purpose and Environment 3493

A.6.6.12.4.2 Test Requirements 3496

A.6.6.12.5 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_CONNECTED state with Rx TEG 3496

A.6.6.12.5.1 Test Purpose and Environment 3496

A.6.6.12.5.2 Test Requirements 3499

A.6.6.12.6 NR RSTD measurement reporting delay test case for PRS aggregation in FR1 SA in RRC_CONNECTED mode 3499

A.6.6.12.6.1 Test Purpose and Environment 3499

A.6.6.12.6.2 Test Requirements 3505

A.6.6.13 PRS-RSRP measurements 3505

A.6.6.13.1 PRS-RSRP reporting delay test case for single positioning frequency layer 3505

A.6.6.13.1.1 Test purpose and Environment 3505

A.6.6.13.1.2 Test Requirements 3507

A.6.6.13.2 PRS-RSRP reporting delay test case for dual positioning frequency layer 3507

A.6.6.13.2.1 Test purpose and Environment 3507

A.6.6.13.2.2 Test Requirements 3510

A.6.6.13.3 PRS-RSRP reporting delay test case for reduced number of samples 3510

A.6.6.13.3.1 Test purpose and Environment 3510

A.6.6.13.3.2 Test Requirements 3512

A.6.6.13.4 PRS-RSRP reporting delay test case for single positioning frequency layer outside MG 3512

A.6.6.13.4.1 Test purpose and Environment 3512

A.6.6.14 UE Rx-Tx time difference measurements 3515

A.6.6.14.1 UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA 3515

A.6.6.14.1.1 Test purpose and environment 3515

A.6.6.14.1.2 Test requirements 3517

A.6.6.14.2 UE Rx-Tx time difference measurement for dual positioning frequency layers in FR1 SA 3517

A.6.6.14.2.1 Test purpose and environment 3517

A.6.6.14.2.2 Test requirements 3519

A.6.6.14.3 UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA with reduced sample number 3520

A.6.6.14.3.1 Test purpose and environment 3520

A.6.6.14.3.2 Test requirements 3522

A.6.6.14.4 UE Rx-Tx time difference measurement without gaps in FR1 SA 3522

A.6.6.14.4.1 Test purpose and environment 3522

A.6.6.14.4.2 Test requirements 3524

A.6.6.14.5 UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA with multiple RxTx TEGs 3524

A.6.6.14.4.1 Test purpose and environment 3524

A.6.6.14.4.2 Test requirements 3526

A.6.6.14.6 UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR1 SA 3527

A.6.6.14.6.1 Test purpose and environment 3527

A.6.6.14.6.2 Test requirements 3530

A.6.6.15 Idle Mode measurements of inter-RAT DC candidate cells for early reporting 3530

A.6.6.15.1 Test Purpose and Environment 3530

A.6.6.15.2 Test Requirements 3534

A.6.6.16 PRS-RSRPP measurements 3535

A.6.6.16.1 PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC_CONNECTED state 3535

A.6.6.16.1.1 Test purpose and Environment 3535

A.6.6.16.1.2 Test Requirements 3537

A.6.6.16.2 PRS-RSRPP reporting delay test case with reduced number of samples for single positioning frequency layer in FR1 in RRC_CONNECTED state 3537

A.6.6.16.2.1 Test purpose and Environment 3537

A.6.6.16.2.2 Test Requirements 3539

A.6.6.16.3 PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC_CONNECTED state without measurement gap 3539

A.6.6.16.3.1 Test purpose and Environment 3539

A.6.6.16.3.2 Test Requirements 3541

A.6.6.17 SA event triggered reporting tests with Pre-MG 3542

A.6.6.17.1 SA event triggered reporting tests with autonomous activation/deactivation Pre-MG 3542

A.6.6.17.1.1 Test purpose and Environment 3542

A.6.6.17.1.2 Test parameters 3542

A.6.6.17.1.3 Test Requirements 3544

A.6.6.17.2 SA event triggered reporting tests with pre-configured measurement gaps and network-controlled activation/deactivation 3545

A.6.6.17.2.1 Test purpose and Environment 3545

A.6.6.17.2.2 Test parameters 3545

A.6.6.17.2.3 Test Requirements 3547

A.6.6.17.3 Void 3548

A.6.6.17.3.1 Void 3548

A.6.6.17.3.2 Void 3548

A.6.6.17.3.3 Void 3548

A.6.6.18 SA event triggered reporting tests with concurrent gaps 3548

A.6.6.18.1 SA event triggered reporting tests for FR1 concurrent gaps with non-overalpping scenario for SSB-based measurements in both inter-frequency layers 3548

A.6.6.18.1.1 Test Purpose and Environment 3548

A.6.6.18.1.2 Test Requirements 3550

A.6.6.18.2 SA event triggered reporting tests for FR1 concurrent gap with partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers 3550

A.6.6.18.2.1 Test Purpose and Environment 3550

A.6.6.18.2.2 Test Requirements 3553

A.6.6.18.3 SA NR - E-UTRAN and NR FR1 concurrent event-triggered reporting in non-DRX in FR1 3553

A.6.6.18.3.1 Test Purpose and Environment 3553

A.6.6.18.3.2 Test Requirements 3557

A.6.6.18.4 SA event triggered reporting tests for PRS and SSB measurement in FR1 without SSB time index detection when DRX is not used 3558

A.6.6.18.4.1 Test Purpose and Environment 3558

A.6.6.18.4.2 Test Requirements 3561

A.6.6.19 SA event triggered reporting tests with NCSG 3561

A.6.6.19.1 SA event triggered reporting tests with NCSG under non-DRX in FR1 3561

A.6.6.19.1.1 Test purpose and Environment 3561

A.6.6.19.1.2 Test parameters 3561

A.6.6.19.1.3 Test Requirements 3564

A.6.6.19.2 SA event triggered reporting tests for FR1 with NCSG for inter-frequency measurement 3564

A.6.6.19.2.1 Test Purpose and Environment 3564

A.6.6.19.2.2 Test parameters 3564

A.6.6.19.2.3 Test Requirements 3566

A.6.6.19.3 SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 with NCSG 3567

A.6.6.19.3.1 Test Purpose and Environment 3567

A.6.6.19.3.2 Test parameters 3567

A.6.6.19.3.3 Test Requirements 3570

A.6.6.19.4 Event triggered reporting on SCC with deactivated SCell test with per-UE NCSG under non-DRX 3570

A.6.6.19.4.1 Test purpose and Environment 3570

A.6.6.19.4.2 Test parameters 3570

A.6.6.19.4.3 Test Requirements 3572

A.6.6.20 UE Rx-Tx time difference measurement for propagation delay compensation 3572

A.6.6.20.1 Test purpose and environment 3572

A.6.6.20.2 Test requirements 3574

A.6.6.21 UE Rx-Tx time difference measurement with TRS for RTT-based PDC in FR1 SA 3574

A.6.6.21.1 Test purpose and environment 3574

A.6.6.21.2 Test requirements 3576

A.6.6.22 SA event triggered reporting tests for concurrent measurement gaps with Pre-MG 3576

A.6.6.22.1 SA event triggered reporting tests for FR1 concurrent gap with Pre-MG with partially partial overalpping scenario for SSB-based measurements in both intra-frequency and inter-frequency layers 3576

A.6.6.22.1.1 Test Purpose and Environment 3576

A.6.6.22.1.2 Test Requirements 3579

A.6.6.22.2 SA event triggered reporting tests for concurrent gap with pre-configured gaps and network-controlled activation/deactivation 3580

A.6.6.22.2.1 Test purpose and Environment 3580

A.6.6.22.2.2 Test parameters 3580

A.6.6.22.2.3 Test Requirements 3583

A.6.6.23 SA event triggered reporting tests for concurrent measurement gaps with NCSG 3583

A.6.6.23.1 SA event triggered reporting tests for FR1 concurrent gaps with NCSG for partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers [one MG + one NCSG] 3583

A.6.6.23.1.1 Test Purpose and Environment 3583

A.6.6.23.1.2 Test Requirements 3586

A.6.6.23.2 SA event triggered reporting tests for FR1 concurrent gaps with NCSG for partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers [two NCSG] 3586

A.6.6.23.2.1 Test Purpose and Environment 3586

A.6.6.23.2.2 Test Requirements 3588

A.6.6.23.3 Event triggered reporting on SCC with deactivated SCell test with per-UE Con-NCSG under non-DRX 3589

A.6.6.23.3.1 Test purpose and Environment 3589

A.6.6.23.3.2 Test parameters 3589

A.6.6.23.3.3 Test Requirements 3591

A.6.6.24 SA event triggered reporting tests with NeedForGap in FR1 3591

A.6.6.24.1 SA event triggered reporting tests without gaps, with interruptions, under non-DRX 3591

A.6.6.24.1.1 Test purpose and Environment 3591

A.6.6.24.1.2 Test parameters 3592

A.6.6.24.1.3 Test Requirements 3593

A.6.6.24.2 SA event triggered reporting tests for FR1 without gap with interruption for inter-frequency measurement with SSB time index detection when DRX is not used 3594

A.6.6.24.2.1 Test Purpose and Environment 3594

A.6.6.24.2.2 Test parameters 3594

A.6.6.24.2.3 Test Requirements 3596

A.6.6.24.3 SA event triggered reporting tests for FR1 with ‘no-gap-with-interruption’, without measurement gap or DRX 3596

A.6.6.24.3.1 Test Purpose and Environment 3596

A.6.6.24.3.2 Test Requirements 3598

A.6.6.24.4 SA event triggered reporting tests for FR1 NeedForGaps without gap without interruption when DRX is not used 3599

A.6.6.24.4.1 Test Purpose and Environment 3599

A.6.6.24.4.2 Test parameters 3599

A.6.6.24.4.3 Test Requirements 3601

A.6.6.24.5 SA event triggered reporting tests without gap under non-DRX for UE indicating no-gap-no-interruption 3601

A.6.6.24.5.1 Test purpose and Environment 3601

A.6.6.24.5.2 Test parameters 3601

A.6.6.24.5.3 Test Requirements 3603

A.6.6.25 SA NR - E-UTRAN event-triggered without measurement gaps 3603

A.6.6.25.1 SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 3604

A.6.6.25.1.1 Test Purpose and Environment 3604

A.6.6.25.1.2 Test Requirements 3607

A.6.6.25.2 SA NR - E-UTRAN event-triggered reporting without gap under non-DRX in FR1 3607

A.6.6.25.2.1 Test Purpose and Environment 3607

A.6.6.25.2.2 Test parameters 3607

A.6.6.25.2.3 Test Requirements 3608

A.6.6.25.3 SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for UE capable of inter-RAT EUTRAN measurement without gap when CRS is contained within UE’s active DL BWP 3608

A.6.6.25.3.1 Test Purpose and Environment 3608

A.6.6.25.3.2 Test Requirements 3612

A.6.6.26 LTM Intra-frequency L1-RSRP measurement 3612

A.6.6.26.1 Intra-frequency SSB based L1-RSRP measurement in FR1 3612

A.6.6.26.1.1 Test Purpose and Environment 3612

A.6.6.26.1.2 Test Parameters 3612

A.6.6.26.1.3 Test Requirements 3614

A.6.6.26.2 Intra-frequency SSB based L1-RSRP measurement in FR1 3614

A.6.6.26.2.1 Test Purpose and Environment 3614

A.6.6.26.2.2 Test Parameters 3615

A.6.6.26.2.3 Test Requirements 3615

A.6.6.26.3 CSI-RS based L1 RSRP measurement for neighbour cell in FR1 with event triggered reporting or periodic reporting 3616

A.6.6.26.3.1 Test purpose and Environment 3616

A.6.6.26.3.2 Test Parameters 3616

A.6.6.10.1.2 Test Requirements 3618

A.6.6.27 LTM Inter-frequency L1-RSRP measurement with measurement gap 3619

A.6.6.27.1 Inter-frequency SSB based L1-RSRP measurement with measurement gap 3619

A.6.6.27.1.1 Test Purpose and Environment 3619

A.6.6.27.1.2 Test parameters 3619

A.6.6.27.1.3 Test Requirements 3621

A.6.6.27.2 Inter-frequency SSB based L1-RSRP measurement with measurement gap with event triggered reporting 3621

A.6.6.27.2.1 Test Purpose and Environment 3621

A.6.6.27.2.2 Test parameters 3621

A.6.6.27.2.3 Test Requirements 3622

A.6.6.28 LTM Inter-frequency L1-RSRP measurement without measurement gap 3622

A.6.6.28.1 Inter-frequency SSB based L1-RSRP measurement without measurement gap 3622

A.6.6.28.1.1 Test Purpose and Environment 3622

A.6.6.28.1.2 Test parameters 3622

A.6.6.28.1.3 Test Requirements 3625

A.6.6.28.2 Inter-frequency SSB based L1-RSRP measurement without measurement gap with event triggered reporting 3625

A.6.6.28.2.1 Test Purpose and Environment 3625

A.6.6.28.2.2 Test parameters 3625

A.6.6.28.2.3 Test Requirements 3626

A.6.6.29 RSCPD Measurements 3626

A.6.6.29.1 NR RSCPD with RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_CONNECTED state 3626

A.6.6.29.1.1 Test Purpose and Environment 3626

A.6.6.29.1.2 Test Requirements 3633

A.6.6.30 RSCP Measurements 3633

A.6.6.30.1 DL RSCP with UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA 3633

A.6.6.30.1.1 Test purpose and environment 3633

A.6.6.30.1.2 Test requirements 3637

A.6.6.31 CJT calibration measurements and accuracy 3637

A.6.6.31.1 CJTC Delay offset measurement period and accuracy in FR1 3637

A.6.6.31.1.1 Test Purpose and Environment 3637

A.6.6.31.1.2 Test parameters 3638

A.6.6.31.1.3 Test Requirements 3640

A.6.6.31.2 CJTC frequency offset measurement period and accuracy in FR1 3640

A.6.6.31.2.1 Test Purpose and Environment 3640

A.6.6.31.2.2 Test requirements 3642

A.6.6.32 L1 CLI measurements 3642

A.6.6.32.1 L1-SRS-RSRP measurement with DRX with SBFD 3642

A.6.6.32.1.1 Test Purpose and Environment 3642

A.6.6.32.1.2 Test Parameters 3642

A.6.6.32.1.3 Test Requirements 3644

A.6.6.32.2 L1-CLI-RSSI measurement with DRX with SBFD 3644

A.6.6.32.2.1 Test Purpose and Environment 3644

A.6.6.32.2.2 Test Parameters 3644

A.6.6.32.2.3 Test Requirements 3645

A.6.6.33 LTM Inter-frequency L1-RSRP measurement with measurement gap cancellation 3646

A.6.6.33.1 Inter-frequency SSB based L1-RSRP measurement with measurement gap cancellation 3646

A.6.6.33.1.1 Test Purpose and Environment 3646

A.6.6.33.1.2 Test parameters 3646

A.6.6.33.1.3 Test Requirements 3646

A.6.6.34 DL AI/ML positioning reporting delay test case for single positioning frequency layer in FR1 SA in RRC_CONNECTED state 3647

A.6.6.34.1 Test Purpose and Environment 3647

A.6.6.34.2 Test Requirements 3650

A.6.7 Measurement Performance requirements 3650

A.6.7.1 SS-RSRP 3650

A.6.7.1.1 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell 3650

A.6.7.1.1.1 Test Purpose and Environment 3650

A.6.7.1.1.2 Test parameters 3650

A.6.7.1.1.3 Test Requirements 3654

A.6.7.1.2 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell 3654

A.6.7.1.2.1 Test Purpose and Environment 3654

A.6.7.1.2.2 Test parameters 3654

A.6.7.1.2.3 Test Requirements 3657

A.6.7.1.3 Void 3657

A.6.7.1.4 SA inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for UE configured with measurement gap cancellation 3657

A.6.7.1.4.1 Test Purpose and Environment 3657

A.6.7.1.4.2 Test parameters 3657

A.6.7.1.4.3 Test Requirements 3658

A.6.7.2 SS-RSRQ 3658

A.6.7.2.1 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 3658

A.6.7.2.1.1 Test Purpose and Environment 3658

A.6.7.2.1.2 Test Parameters 3658

A.6.7.2.1.3 Test Requirements 3662

A.6.7.2.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 3662

A.6.7.2.2.1 Test Purpose and Environment 3662

A.6.7.2.2.2 Test Parameters 3662

A.6.7.2.2.3 Test Requirements 3666

A.6.7.3 SS-SINR 3666

A.6.7.3.1 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 3666

A.6.7.3.1.1 Test Purpose and Environment 3666

A.6.7.3.1.2 Test Parameters 3666

A.6.7.3.1.3 Test Requirements 3669

A.6.7.3.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 3669

A.6.7.3.2.1 Test Purpose and Environment 3669

A.6.7.3.2.2 Test Parameters 3669

A.6.7.3.2.3 Test Requirements 3673

A.6.7.4 L1-RSRP measurement for beam reporting 3673

A.6.7.4.1 SSB based L1-RSRP measurement 3673

A.6.7.4.1.1 Test Purpose and Environment 3673

A.6.7.4.1.2 Test parameters 3673

A.6.7.4.1.3 Test Requirements 3676

A.6.7.4.2 CSI-RS based L1-RSRP measurement on resource set with repetition off 3676

A.6.7.4.2.1 Test Purpose and Environment 3676

A.6.7.4.2.2 Test parameters 3676

A.6.7.4.2.3 Test Requirements 3679

A.6.7.5 E-UTRAN RSRP 3680

A.6.7.5.1 SA: inter-RAT measurement accuracy with FR1 serving cell 3680

A.6.7.5.1.1 Test Purpose and Environment 3680

A.6.7.5.1.2 Test parameters 3680

A.6.7.5.1.3 Test Requirements 3683

A.6.7.6 E-UTRAN RSRQ 3683

A.6.7.6.1 SA: inter-RAT measurement accuracy with FR1 serving cell 3683

A.6.7.6.1.1 Test Purpose and Environment 3683

A.6.7.6.1.2 Test parameters 3683

A.6.7.6.1.3 Test Requirements 3686

A.6.7.7 E-UTRAN RS-SINR 3687

A.6.7.7.1 SA: inter-RAT measurement accuracy with FR1 serving cell 3687

A.6.7.7.1.1 Test Purpose and Environment 3687

A.6.7.7.1.2 Test parameters 3687

A.6.7.7.1.3 Test Requirements 3690

A.6.7.8 CLI measurements 3690

A.6.7.8.1 SA SRS-RSRP measurement accuracy with FR1 serving cell 3690

A.6.7.8.1.1 Test Purpose and Environment 3690

A.6.7.8.1.2 Test parameters 3690

A.6.7.8.1.3 Test Requirements 3693

A.6.7.8.2 SA CLI-RSSI measurement accuracy with FR1 serving cell 3693

A.6.7.8.2.1 Test Purpose and Environment 3693

A.6.7.8.2.2 Test parameters 3694

A.6.7.8.2.3 Test Requirements 3695

A.6.7.9 L1-SINR measurement for beam reporting 3695

A.6.7.9.2 L1-SINR measurement with SSB based CMR and dedicated IMR 3698

A.6.7.9.2.1 Test Purpose and Environment 3699

A.6.7.9.2.2 Test parameters 3699

A.6.7.9.2.3 Test Requirements 3702

A.6.7.9.3 L1-SINR measurement with CSI-RS based CMR and dedicated IMR 3702

A.6.7.9.3.1 Test Purpose and Environment 3702

A.6.7.9.3.2 Test parameters 3703

A.6.7.9.3.3 Test Requirements 3706

A.6.7.10 CSI-RSRP 3706

A.6.7.10.1 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell 3706

A.6.7.10.1.1 Test Purpose and Environment 3706

A.6.7.10.1.2 Test parameters 3706

A.6.7.10.1.3 Test Requirements 3709

A.6.7.10.2 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell 3709

A.6.7.10.2.1 Test Purpose and Environment 3710

A.6.7.10.2.2 Test parameters 3710

A.6.7.10.2.3 Test Requirements 3713

A.6.7.11 CSI-RSRQ 3713

A.6.7.11.1 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 3713

A.6.7.11.1.1 Test Purpose and Environment 3713

A.6.7.11.1.2 Test Parameters 3713

A.6.7.11.1.3 Test Requirements 3717

A.6.7.11.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 3717

A.6.7.11.2.1 Test Purpose and Environment 3717

A.6.7.11.2.2 Test Parameters 3717

A.6.7.11.2.3 Test Requirements 3721

A.6.7.12 CSI-SINR 3721

A.6.7.12.1 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 3721

A.6.7.12.1.1 Test Purpose and Environment 3721

A.6.7.12.1.2 Test Parameters 3721

A.6.7.12.1.3 Test Requirements 3724

A.6.7.12.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 3725

A.6.7.12.2.1 Test Purpose and Environment 3725

A.6.7.12.2.2 Test Parameters 3725

A.6.7.12.2.3 Test Requirements 3728

A.6.7.13 RSTD measurements 3728

A.6.7.13.1 RSTD measurement accuracy test case for single positioning frequency layer 3728

A.6.7.13.1.1 Test purpose and Environment 3728

A.6.7.13.1.2 Test Requirements 3730

A.6.7.13.2 RSTD measurement accuracy test case for dual positioning frequency layer 3730

A.6.7.13.2.1 Test purpose and Environment 3730

A.6.7.13.2.2 Test Requirements 3732

A.6.7.13.3 RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR1 in RRC_CONNECTED state 3732

A.6.7.13.3.1 Test purpose and Environment 3732

A.6.7.13.3.2 Test Requirements 3734

A.6.7.13.4 RSTD measurement accuracy test case with Rx TEG 3734

A.6.7.13.5 NR RSTD measurement accuracy test case for PRS aggregation in FR1 SA in RRC_CONNECTED mode 3736

A.6.7.13.5.1 Test purpose and Environment 3736

A.6.7.13.5.2 Test Requirements 3739

A.6.7.14 PRS-RSRP measurements 3739

A.6.7.14.1 SA: measurement accuracy with PRS in FR1 3739

A.6.7.14.1.1 Test Purpose and Environment 3739

A.6.7.14.1.2 Test parameters 3739

A.6.7.14.1.3 Test Requirements 3741

A.6.7.14.2 SA: measurement accuracy with PRS in FR1 with reduced sample number 3741

A.6.7.14.2.1 Test Purpose and Environment 3741

A.6.7.14.2.2 Test parameters 3741

A.6.7.14.2.3 Test Requirements 3743

A.6.7.14.3 Void 3743

A.6.7.14.3.1 Void 3743

A.6.7.14.3.2 Void 3743

A.6.7.14.3.3 Void 3743

A.6.7.15 UE Rx-Tx time difference measurements 3743

A.6.7.15.1 UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA 3743

A.6.7.15.1.1 Test purpose and environment 3743

A.6.7.15.1.2 Test parameters 3744

A.6.7.15.1.3 Test requirements 3745

A.6.7.15.2 UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR1 SA 3745

A.6.7.15.2.1 Test purpose and environment 3745

A.6.7.15.2.2 Test parameters 3746

A.6.7.15.2.3 Test requirements 3747

A.6.7.15.3 UE Rx-Tx time difference measurement accuracy with RxTx TEG 3747

A.6.7.15.3.1 Test purpose and environment 3747

A.6.7.15.3.2 Test parameters 3748

A.6.7.15.3.3 Test requirements 3750

A.6.7.15.4 UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR1 SA 3750

A.6.7.15.4.1 Test purpose and environment 3750

A.6.7.15.4.2 Test requirements 3753

A.6.7.16 PRS-RSRPP measurements 3753

A.6.7.16.1 SA: measurement accuracy with PRS in FR1 3753

A.6.7.16.1.1 Test Purpose and Environment 3753

A.6.7.16.1.2 Test parameters 3753

A.6.7.16.1.3 Test Requirements 3755

A.6.7.16.2 SA: measurement accuracy with reduced PRS samples in FR1 3755

A.6.7.16.2.1 Test Purpose and Environment 3755

A.6.7.16.2.2 Test parameters 3755

A.6.7.17 LTM L1-RSRP measurement 3757

A.6.7.17.1 SSB based Inter-frequency L1-RSRP accuracy requirements for neighbour cell in FR1 3757

A.6.7.17.1.1 Test Purpose and Environment 3757

A.6.7.17.1.2 Test parameters 3758

A.6.7.17.1.3 Test Requirements 3761

A.6.7.17.2 CSI-RS based intra-frequency L1-RSRP accuracy requirement for neighbour cell 3761

A.6.7.17.2.1 Test Purpose and Environment 3761

A.6.7.17.2.2 Test parameters 3761

A.6.7.17.2.3 Test Requirements 3765

A.6.7.18 TDCP amplitude measurement accuracy 3766

A.6.7.18.1 TDCP amplitude measurement accuracy in FR1 3766

A.6.7.18.1.1 Test Purpose and Environment 3766

A.6.7.18.1.2 Test parameters 3766

A.6.7.18.1.3 Test Requirements 3767

A.6.7.19 RSCPD Measurements 3767

A.6.7.19.1 RSCPD with RSTD measurement accuracy in FR1 SA in RRC_CONNECTED 3767

A.6.7.19.1.1 Test purpose and environment 3767

A.6.7.19.1.2 Test parameters 3768

A.6.7.19.1.3 Test requirements 3771

A.6.7.20 RSCP Measurements 3771

A.6.7.20.1 RSCP with UE Rx-Tx time difference measurement accuracy in FR1 SA 3771

A.6.7.20.1.1 Test purpose and environment 3771

A.6.7.20.1.2 Test parameters 3772

A.6.7.20.1.3 Test requirements 3775

A.6.7.21 L1 CLI measurements 3775

A.6.7.21.1 SA L1-SRS-RSRP measurement accuracy with FR1 serving cell with SBFD 3775

A.6.7.21.1.1 Test Purpose and Environment 3775

A.6.7.21.1.2 Test Parameters 3775

A.6.7.21.1.3 Test Requirements 3778

A.6.7.21.2 L1-CLI-RSSI measurement accuracy in FR1 with SBFD 3778

A.6.7.21.2.1 Test Purpose and Environment 3778

A.6.7.21.2.2 Test parameters 3778

A.6.7.21.2.3 Test Requirements 3779

A.6.8 Measurement procedure in RRC_INACTIVE 3779

A.6.8.1 RSTD measurements 3779

A.6.8.1.1 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state 3779

A.6.8.1.1.1 Test Purpose and Environment 3780

A.6.8.1.1.2 Test Requirements 3782

A.6.8.1.2 NR RSTD measurement reporting delay test case with reduced number of samples in RRC_INACTIVE, FR1 SA 3783

A.6.8.1.2.1 Test Purpose and Environment 3783

A.6.8.1.2.1 Test Purpose and Environment 3783

A.6.8.1.2.2 Test Requirements 3786

A.6.8.1.3 NR RSTD measurement reporting delay test case for PRS aggregation in FR1 SA in RRC_INACTIVE state 3786

A.6.8.1.3.1 Test purpose and environment 3786

A.6.8.1.3.2 Test requirements 3790

A.6.8.1.4 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state when eDRX cycle > 10.24s for non-RedCap UE 3790

A.6.8.1.4.1 Test Purpose and Environment 3790

A.6.8.1.4.2 Test Requirements 3794

A.6.8.2 PRS-RSRP measurements 3794

A.6.8.2.1 PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_INACTIVE 3794

A.6.8.2.1.1 Test purpose and Environment 3794

A.6.8.2.1.2 Test Requirements 3796

A.6.8.2.2 PRS-RSRP reporting delay test case with reduced number of samples in RRC_INACTIVE 3796

A.6.8.2.2.1 Test purpose and Environment 3796

A.6.8.2.2.2 Test Requirements 3798

A.6.8.2.3 PRS-RSRP reporting delay test case in RRC_INACTIVE state in FR1 with eDRX cycle > 10.24s 3799

A.6.8.2.3.1 Test purpose and Environment 3799

A.6.8.2.3.2 Test Requirements 3801

A.6.8.3 UE Rx-Tx time difference measurements 3802

A.6.8.3.1 UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA 3802

A.6.8.3.1.1 Test purpose and environment 3802

A.6.8.3.1.2 Test requirements 3804

A.6.8.3.2 UE Rx-Tx time difference measurement with reduced number of samples in RRC_INACTIVE, FR1 SA 3804

A.6.8.3.2.1 Test purpose and environment 3804

A.6.8.3.2.2 Test requirements 3806

A.6.8.3.3 UE Rx-Tx time difference measurement for single positioning frequency layer with eDRX > 10.24s in FR1 SA 3807

A.6.8.3.3.1 Test purpose and environment 3807

A.6.8.3.3.2 Test requirements 3811

A.6.8.3.4 UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR1 SA 3811

A.6.8.3.4.1 Test purpose and environment 3811

A.6.8.3.4.2 Test requirements 3814

A.6.8.4 PRS-RSRPP measurements 3814

A.6.8.4.1 PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC_INACTIVE state 3814

A.6.8.4.1.1 Test purpose and Environment 3815

A.6.8.4.1.2 Test Requirements 3816

A.6.8.4.2 PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC_INACTIVE state for reduced number of samples 3817

A.6.8.4.2.1 Test purpose and Environment 3817

A.6.8.4.2.2 Test Requirements 3819

A.6.8.4.3 PRS-RSRPP reporting delay in RRC_INACTIVE with eDRX 3819

A.6.8.4.3.1 Test purpose and Environment 3819

A.6.8.4.3.2 Test Requirements 3822

A.6.8.5 RSCPD Measurements 3822

A.6.8.5.1 DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state 3822

A.6.8.5.1.1 Test Purpose and Environment 3822

A.6.8.5.1.2 Test Requirements 3822

A.6.8.6 RSCP Measurements 3823

A.6.8.6.1 DL RSCP with UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA 3823

A.6.8.6.1.1 Test purpose and environment 3823

A.6.8.6.1.2 Test requirements 3827

A.6.9 Measurement performance requirements in RRC_INACTIVE 3827

A.6.9.1 RSTD measurements 3827

A.6.9.1.1 RSTD measurement accuracy test case for single positioning frequency layer in FR1 in RRC_INACTIVE state 3827

A.6.9.1.1.1 Test purpose and Environment 3827

A.6.9.1.1.2 Test Requirements 3829

A.6.9.1.2 RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR1 in RRC_INACTIVE state 3829

A.6.9.1.2.1 Test purpose and Environment 3829

A.6.9.1.2.2 Test Requirements 3831

A.6.9.1.3 RSTD measurement accuracy for PRS aggregation in FR1 in RRC_INACTIVE state 3831

A.6.9.1.3.1 Test purpose and Environment 3831

A.6.9.1.3.2 Test Requirements 3834

A.6.9.2 PRS-RSRP measurements 3834

A.6.9.2.1 SA: measurement accuracy with PRS in FR1 in RRC_INACTIVE 3834

A.6.9.2.1.1 Test Purpose and Environment 3834

A.6.9.2.1.2 Test parameters 3834

A.6.9.2.1.3 Test Requirements 3836

A.6.9.2.2 SA: measurement accuracy with PRS in FR1 with reduced number of samples in RRC_INACTIVE state 3836

A.6.9.2.2.1 Test Purpose and Environment 3836

A.6.9.2.2.2 Test parameters 3836

A.6.9.2.2.3 Test Requirements 3838

A.6.9.3 UE Rx-Tx time difference measurements 3838

A.6.9.3.1.1 UE Rx-Tx time difference measurement accuracy in FR1 SA 3838

A.6.9.3.1.1.1 Test purpose and environment 3838

A.6.9.3.1.1.2 Test parameters 3839

A.6.9.3.1.1.3 Test requirements 3840

A.6.9.3.2 UE Rx-Tx time difference measurement accuracy with reduced number of samples 3840

A.6.9.3.2.1 Test purpose and environment 3840

A.6.9.3.2.2 Test parameters 3840

A.6.9.3.2.3 Test requirements 3842

A.6.9.3.3 UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR1 SA 3842

A.6.9.3.3.1 Test purpose and environment 3842

A.6.9.3.3.2 Test requirements 3845

A.6.9.4 PRS-RSRPP measurements 3845

A.6.9.4.1 SA: PRS-RSRPP measurement accuracy in FR1 in RRC INACTIVE 3845

A.6.9.4.1.1 Test Purpose and Environment 3845

A.6.9.4.1.2 Test parameters 3845

A.6.9.4.1.3 Test Requirements 3847

A.6.9.4.2 SA: measurement accuracy with reduced PRS samples in FR1 in RRC INACTIVE 3847

A.6.9.4.2.1 Test Purpose and Environment 3847

A.6.9.4.2.2 Test parameters 3848

A.6.9.4.2.3 Test Requirements 3849

A.6.9.5 RSCPD Measurements 3850

A.6.9.5.1 RSCPD with RSTD measurement accuracy in FR1 SA in RRC_INACTIVE 3850

A.6.9.5.1.1 Test purpose and environment 3850

A.6.9.5.1.2 Test parameters 3850

A.6.9.5.1.3 Test requirements 3853

A.6.9.6 RSCP Measurements 3853

A.6.9.6.1 RSCP with UE Rx-Tx time difference measurement accuracy in FR1 SA 3853

A.6.9.6.1.1 Test purpose and environment 3853

A.6.9.6.1.2 Test parameters 3854

A.6.9.6.1.3 Test requirements 3857

A.6.10 Measurement Procedure in RRC_IDLE 3857

A.6.10.1 RSTD Measurements 3857

A.6.10.1.1 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_IDLE state for non-RedCap UE 3857

A.6.10.1.1.1 Test purpose and environment 3857

A.6.10.1.1.2 Test requirements 3860

A.6.10.1.2 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_IDLE state with eDRX cycle > 10.24s for non-RedCap UE 3861

A.6.10.1.2.1 Test Purpose and Environment 3861

A.6.10.1.2.2 Test Requirements 3864

A.6.10.1.3 NR RSTD measurement reporting delay test case for PRS aggregation in FR1 SA in RRC_IDLE state 3864

A.6.10.1.3.1 Test purpose and environment 3864

A.6.10.1.3.2 Test requirements 3864

A.6.10.2  PRS-RSRP Measurements 3865

A.6.10.2.1 PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_IDLE state for non-RedCap UE in FR1 3865

A.6.10.2.1.1 Test purpose and Environment 3865

A.6.10.2.1.2 Test Requirements 3867

A.6.10.2.2 PRS-RSRP reporting delay test case in RRC_IDLE state in FR1 when eDRX cycle > 10.24s 3868

A.6.10.2.2.1 Test purpose and Environment 3868

A.6.10.2.2.2 Test Requirements 3868

A.6.10.3 RSCPD Measurements 3868

A.6.10.3.1 DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_IDLE state 3868

A.6.10.3.1.1 Test Purpose and Environment 3868

A.6.10.3.1.2 Test Requirements 3869

A.6.11 Measurement Performance Requirements in RRC_IDLE 3869

A.6.11.1 RSTD Measurements 3869

A.6.11.1.1 NR RSTD measurement accuracy test case for single positioning frequency layer in FR1 SA in RRC_IDLE state for non-RedCap UE 3869

A.6.11.1.1.1 Test purpose and environment 3869

A.6.11.1.1.2 Test requirements 3871

A.6.11.1.2 RSTD measurement accuracy test case for single positioning frequency layer in FR1 in RRC_IDLE state with eDRX>10.24s for non-RedCap UE 3871

A.6.11.1.2.1 Test purpose and Environment 3871

A.6.11.1.2.2 Test Requirements 3873

A.6.11.1.3 NR RSTD measurement accuracy test case for PRS aggregation in FR1 SA in RRC_IDLE state 3873

A.6.11.1.3.1 Test purpose and environment 3873

A.6.11.1.3.2 Test requirements 3873

A.6.11.2 PRS-RSRP measurements 3873

A.6.11.2.1 PRS-RSRP measurement accuracy test case for non-RedCap UE in FR1 in RRC_IDLE state 3873

A.6.11.2.1.1 Test Purpose and Environment 3873

A.6.11.2.1.2 Test parameters 3874

A.6.11.2.1.3 Test Requirements 3876

A.6.11.2.2 PRS-RSRP measurement accuracy test case in RRC_IDLE state in FR1 when eDRX cycle > 10.24s 3876

A.6.11.2.2.1 Test purpose and Environment 3876

A.6.11.2.2.2 Test parameters 3876

A.6.11.2.2.3 Test Requirements 3877

A.6.11.3 RSCPD Measurements 3877

A.6.11.3.1 RSCPD with RSTD measurement accuracy in FR1 SA in RRC_IDLE 3877

A.6.11.3.1.1 Test purpose and environment 3877

A.6.11.3.1.2 Test parameters 3877

A.6. 11.3.1.3 Test requirements 3880

A.7 NR standalone tests with one or more NR cells in FR2 3881

A.7.1 SA: RRC_IDLE state mobility 3881

A.7.1.1 Cell re-selection to NR 3881

A.7.1.1.1 Cell reselection to FR2 intra-frequency NR case 3881

A.7.1.1.1.1 Test Purpose and Environment 3881

A.7.1.1.1.2 Test Parameters 3881

A.7.1.1.1.3 Test Requirements 3883

A.7.1.1.2 Cell reselection to FR2 inter-frequency NR case 3883

A.7.1.1.2.1 Test Purpose and Environment 3884

A.7.1.1.2.2 Test Parameters 3884

A.7.1.1.2.3 Test Requirements 3885

A.7.1.1.3 Cell reselection to FR2 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion 3886

A.7.1.1.3.1 Test Purpose and Environment 3886

A.7.1.1.3.2 Test Parameters 3886

A.7.1.1.3.3 Test Requirements 3888

A.7.1.1.4 Cell reselection to FR2 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion 3888

A.7.1.1.4.1 Test Purpose and Environment 3888

A.7.1.1.4.2 Test Parameters 3889

A.7.1.1.4.3 Test Requirements 3890

A.7.1.1.5 Cell reselection to FR2 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion 3891

A.7.1.1.5.1 Test Purpose and Environment 3891

A.7.1.1.5.2 Test Parameters 3891

A.7.1.1.5.3 Test Requirements 3893

A.7.1.1.6 Cell reselection to FR2 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion 3893

A.7.1.1.6.1 Test Purpose and Environment 3893

A.7.1.1.6.2 Test Parameters 3894

A.7.1.1.6.3 Test Requirements 3895

A.7.1.1.7 Cell reselection to FR2 intra-frequency NR case for FR2 power class 6 UE configured with highSpeedMeasFlagFR2-r17 3896

A.7.1.1.7.1 Test Purpose and Environment 3896

A.7.1.1.7.2 Test Parameters 3896

A.7.1.1.7.3 Test Requirements 3898

A.7.1.1.8 Cell reselection to FR2 inter-frequency NR case for UE configured with highSpeedMeasFlagFR2-r17 3898

A.7.1.1.8.1 Test Purpose and Environment 3898

A.7.1.1.8.2 Test Parameters 3899

A.7.1.1.8.3 Test Requirements 3900

A.7.1.1.9 Cell reselection to FR2 intra-frequency NR case for FR2 cell supporting OD-SIB1 3901

A.7.1.1.9.1 Test Purpose and Environment 3901

A.7.1.1.9.2 Test Parameters 3901

A.7.1.1.9.3 Test Requirements 3903

A.7.1.1.10 Cell reselection to FR2 inter-frequency NR case for FR2 cell supporting OD- SIB1 3903

A.7.1.1.10.1 Test Purpose and Environment 3903

A.7.1.1.10.2 Test Parameters 3904

A.7.1.1.10.3 Test Requirements 3905

A.7.2 SA: RRC_INACTIVE state mobility 3906

A.7.2.1 Small Data Transmission 3906

A.7.2.1.1 TA validation for CG-SDT in FR2 3906

A.7.2.1.1.1 Test Purpose and Environment 3906

A.7.2.1.1.2 Test Requirements 3909

A.7.2.2 Cell reselection for positioning 3909

A.7.2.2.1 Cell reselection to FR2 intra-frequency NR case with RRC_ INACTIVE eDRX and positioning SRS 3909

A.7.2.2.1.1 Test Purpose and Environment 3909

A.7.2.2.1.2 Test Parameters 3909

A.7.2.2.1.3 Test Requirements 3912

A.7.3 RRC_CONNECTED state mobility 3912

A.7.3.1 Handover 3912

A.7.3.1.1 Inter-frequency handover from FR1 to FR2; unknown target cell 3912

A.7.3.1.1.1 Test Purpose and Environment 3912

A.7.3.1.1.2 Test Parameters 3912

A.7.3.1.1.3 Test Requirements 3914

A.7.3.1.2 Intra-frequency handover from FR2 to FR2; unknown target cell 3915

A.7.3.1.2.1 Test Purpose and Environment 3915

A.7.3.1.2.2 Test Parameters 3915

A.7.3.1.2.3 Test Requirements 3916

A.7.3.1.3 Inter-frequency handover from FR2 to FR2; unknown target cell 3916

A.7.3.1.3.1 Test Purpose and Environment 3916

A.7.3.1.3.2 Test Parameters 3916

A.7.3.1.3.3 Test Requirements 3918

A.7.3.1.4 Inter-band inter-frequency synchronous DAPS handover from FR1 to FR2 3918

A.7.3.1.4.1 Test Purpose and Environment 3918

A.7.3.1.4.2 Test Parameters 3918

A.7.3.1.4.3 Test Requirements 3921

A.7.3.1.5 Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR2 3922

A.7.3.1.5.1 Test Purpose and Environment 3922

A.7.3.1.5.2 Test Parameters 3922

A.7.3.1.5.3 Test Requirements 3925

A.7.3.1.6 Handover with PSCell from SA to EN-DC with unknown FR2 target PScell 3926

A.7.3.1.6.1 Test Purpose and Environment 3926

A.7.3.1.6.2 Test Parameters 3926

A.7.3.1.6.3 Test Requirements 3931

A.7.3.1.7 HO with PSCell from FR1 NR-SA to EN-DC with known E-UTRA PCell and known FR2 PSCell 3931

A.7.3.1.7.1 Test purpose and environment 3931

A.7.3.1.7.2 Test Requirements 3935

A.7.3.1.8 NR PSCell change delay in HO with PSCell from NR-DC to NR-DC 3936

A.7.3.1.8.1 Test Purpose and Environment 3936

A.7.3.1.8.2 Test Requirements 3939

A.7.3.1.9 Intra-frequency handover from FR2-2 to FR2-2; unknown target cell 3939

A.7.3.1.9.1 Test Purpose and Environment 3939

A.7.3.1.9.2 Test Parameters 3939

A.7.3.1.9.3 Test Requirements 3941

A.7.3.1.10 Inter-frequency handover from FR2-2 to FR2-2; unknown target cell 3942

A.7.3.1.10.1 Test Purpose and Environment 3942

A.7.3.1.10.2 Test Parameters 3942

A.7.3.1.10.3 Test Requirements 3944

A.7.3.1.11 Inter-frequency handover from FR1 to FR2-2; unknown target cell 3944

A.7.3.1.11.1 Test Purpose and Environment 3944

A.7.3.1.11.2 Test Parameters 3944

A.7.3.1.11.3 Test Requirements 3946

A.7.3.1.12 Intra-frequency handover from FR2 to FR2; known target cell configured with NCD-SSB 3947

A.7.3.1.12.1 Test Purpose and Environment 3947

A.7.3.1.12.2 Test Parameters 3947

A.7.3.1.12.3 Test Requirements 3948

A.7.3.1.13 Inter-frequency handover from FR2 to FR2; known target cell configured with NCD-SSB 3949

A.7.3.1.13.1 Test Purpose and Environment 3949

A.7.3.1.13.2 Test Parameters 3949

A.7.3.1.13.3 Test Requirements 3951

A.7.3.1.14 Handover with PSCell from FR1-FR2 NR-DC to FR1-FR1 NR-DC with target PSCell in FR1 3951

A.7.3.1.14.1 Test Purpose and Environment 3951

A.7.3.1.14.2 Test Requirements 3955

A.7.3.1.15 HO with PSCell from FR1-FR1 NR-DC to FR1-FR2 NR-DC 3955

A.7.3.1.15.1 Test Purpose and Environment 3955

A.7.3.1.15.2 Test Requirements 3960

A.7.3.1.16 Intra-frequency handover from FR2 to FR2; unknown target cell; for UE supporting fast beam sweeping 3960

A.7.3.1.16.1 Test Purpose and Environment 3960

A.7.3.1.16.2 Test Parameters 3960

A.7.3.1.16.3 Test Requirements 3962

A.7.3.1.17 Inter-frequency handover from FR2 to FR2; unknown target cell; for UE supporting fast beam sweeping 3962

A.7.3.1.17.1 Test Purpose and Environment 3962

A.7.3.1.17.2 Test Parameters 3962

A.7.3.1.17.3 Test Requirements 3964

A.7.3.2 RRC Connection Mobility Control 3964

A.7.3.2.1 SA: RRC Re-establishment 3964

A.7.3.2.1.1 Intra-frequency RRC Re-establishment in FR2 3964

A.7.3.2.1.2 Inter-frequency RRC Re-establishment in FR2 3966

A.7.3.2.1.3 Intra-frequency RRC Re-establishment in FR2 without serving cell timing 3968

A.7.3.2.1.3.1 Test Purpose and Environment 3968

A.7.3.2.1.3.2 Test Requirements 3970

A.7.3.2.1.4 Intra-frequency RRC Re-establishment in FR2-2 3971

A.7.3.2.1.4.1 Test Purpose and Environment 3971

A.7.3.2.1.4.2 Test Requirements 3972

A.7.3.2.1.5 Inter-frequency RRC Re-establishment in FR2-2 3973

A.7.3.2.1.5.1 Test Purpose and Environment 3973

A.7.3.2.1.5.2 Test Requirements 3975

A.7.3.2.1.6 Intra-frequency RRC Re-establishment in FR2-2 without serving cell timing 3975

A.7.3.2.1.6.1 Test Purpose and Environment 3975

A.7.3.2.1.6.2 Test Requirements 3977

A.7.3.2.1.7 Intra-frequency RRC Re-establishment in FR2 with UE capable of reduced beam sweeping factor 3978

A.7.3.2.1.7.1 Test Purpose and Environment 3978

A.7.3.2.1.7.2 Test Requirements 3979

A.7.3.2.1.8 Inter-frequency RRC Re-establishment in FR2 without serving cell timing with UE capable of reduced beam sweeping factor 3980

A.7.3.2.1.8.1 Test Purpose and Environment 3980

A.7.3.2.1.8.2 Test Requirements 3982

A.7.3.2.2 Random Access 3982

A.7.3.2.2.1 4-step RA type c ontention based random access test in FR2 for NR Standalone 3982

A.7.3.2.2.2 4-step RA type n on-contention based random access test in FR2 for NR Standalone 3986

A.7.3.2.2.3 2-step RA type contention based random access test in FR2 for NR Standalone 3989

A.7.3.2.2.4 2-step RA type n on-contention based random access test in FR2 for NR Standalone 3991

A.7.3.2.3 SA: RRC Connection Release with Redirection 3994

A.7.3.2.3.1 Redirection from NR in FR2 to NR in FR2 3994

A.7.3.2.3.2 Redirection from NR in FR2 to NR in FR2 with UE capable of reduced beam sweeping factor 3996

A.7.3.2.4 LTM PDCCH-order Random Access 3998

A.7.3.2.4.1 PDCCH-order RACH on neighbor cell in FR2 when RACH BW is within active BWP 3998

A.7.3.2.4.2 PDCCH-order RACH on inter-frequency neighbor cell in FR2 4001

A.7.3.3 Conditional Handover 4004

A.7.3.3.1 Intra-frequency conditional handover from FR2 to FR2 4004

A.7.3.3.1.1 Test Purpose and Environment 4004

A.7.3.3.1.2 Test Parameters 4004

A.7.3.3.1.2.3 Test Requirements 4006

A.7.3.3.2 Inter-frequency conditional handover from FR2 to FR2; unknown target cell 4006

A.7.3.3.2.1 Test Purpose and Environment 4006

A.7.3.3.2.2 Test Parameters 4006

A.7.3.3.2.3 Test Requirements 4007

A.7.3.3.3 NES triggering intra-frequency target CHO delay From FR2 to FR2 4008

A.7.3.3.3.1 Test Purpose and Environment 4008

A.7.3.3.3.2 Test Parameters 4008

A.7.3.3.3.2.3 Test Requirements 4009

A.7.3.3.4 NES triggering inter-frequency conditional handover from FR2 to FR1 4010

A.7.3.3.4.1 Test Purpose and Environment 4010

A.7.3.3.4.2 Test Parameters 4010

A.7.3.3.4.3 Test Requirements 4012

A.7.3.3.5 NR conditional handover including target MCG and target SCG from FR1-FR2 NR-DC to FR1-FR2 NR-DC 4012

A.7.3.3.5.1 Test Purpose and Environment 4012

A.7.3.3.5.2 Test Requirements 4015

A.7.3.3.5.2.1 Test Requirements for NR conditional handover 4015

A.7.3.3.5.2.2 Test Requirements for NR PSCell change 4015

A.7.3.3.6 NR conditional Handover including target MCG and candidate SCG from FR1-FR2 NR-DC to FR1-FR2 NR-DC 4015

A.7.3.3.6.1 Test Purpose and Environment 4015

A.7.3.3.6.2 Test Parameters 4015

A.7.3.3.6.3 Test Requirements 4019

A.7.3.4 LTM PCell Switch 4019

A.7.3.4.1 RACH based Intra-frequency PCell switch from FR2 to FR2 4019

A.7.3.4.1.1 Test Purpose and Environment 4019

A.7.3.4.1.2 Test Parameters 4019

A.7.3.4.1.3 Test Requirements 4022

A.7.3.4.2 RACH-less Intra-frequency PCell switch from FR2 to FR2 4023

A.7.3.4.2.1 Test Purpose and Environment 4023

A.7.3.4.2.2 Test Parameters 4023

A.7.3.4.2.3 Test Requirements 4027

A.7.3.4.3 RACH-based Inter-frequency LTM PCell switch from FR2 to FR2 4027

A.7.3.4.3.1 Test Purpose and Environment 4027

A.7.3.4.3.2 Test Parameters 4027

A.7.3.4.3.3 Test Requirements 4030

A.7.3.4.4 RACH-less Intra-frequency CLTM PCell switch from FR2 to FR2 triggered by SSB based L1-RSRP measurement 4031

A.7.3.4.4.1 Test Purpose and Environment 4031

A.7.3.4.4.2 Test Parameters 4031

A.7.3.4.4.3 Test Requirements 4036

A.7.3.4.5 RACH-based Intra-frequency CLTM PCell switch from FR2 to FR2 triggered by SSB based L1-RSRP measurement 4037

A.7.3.4.5.1 Test Purpose and Environment 4037

A.7.3.4.5.2 Test Parameters 4037

A.7.3.4.5.3 Test Requirements 4040

A.7.3.5 LTM PSCell Switch 4040

A.7.3.5.1 RACH-based Intra-frequency LTM PSCell switch from FR2 to FR2 4040

A.7.3.5.1.1 Test Purpose and Environment 4040

A.7.3.5.1.2 Test Parameters 4040

A.7.3.5.1.3 Test Requirements 4045

A.7.4 Timing 4045

A.7.4.1 UE transmit timing 4045

A.7.4.1.1 NR UE Transmit Timing Test for FR2 4045

A.7.4.1.1.1 Test Purpose and environment 4045

A.7.4.1.1.2 Test requirements 4047

A.7.4.1.2 NR UE Transmit Timing Test for FR2-2 4048

A.7.4.1.2.1 Test Purpose and environment 4048

A.7.4.1.2.2 Test requirements 4051

A.7.4.1.3 NR UE Transmit Timing Test with 2-TA for FR2 UE supporting multiDCI-IntraCellMultiTRP-TwoTA-r18 4051

A.7.4.1.3.1 Test Purpose and environment 4051

A.7.4.1.3.2 Test requirements 4054

A.7.4.1.4 NR UE Transmit Timing Test with 2-TA for FR2 UE supporting single DCI 4055

A.7.4.1.4.1 Test Purpose and environment 4055

A.7.4.1.4.2 Test requirements 4059

A.7.4.2 UE timer accuracy 4060

A.7.4.3 Timing advance 4060

A.7.4.3.1 SA FR2 timing advance adjustment accuracy 4060

A.7.4.3.1.1 Test Purpose and Environment 4060

A.7.4.3.1.2 Test Parameters 4060

A.7.4.3.1.3 Test Requirements 4062

A.7.4.3.2 SA FR2-2 timing advance adjustment accuracy 4063

A.7.4.3.2.1 Test Purpose and Environment 4063

A.7.4.3.2.2 Test Parameters 4063

A.7.4.3.2.3 Test Requirements 4065

A.7.4.3.3 SA FR2 timing advance adjustment accuracy for asymmetric DL sTRP/UL mTRP deployment with two TAs 4066

A.7.4.3.3.1 Test Purpose and Environment 4066

A.7.4.3.3.2 Test Parameters 4066

A.7.5 Signaling characteristics 4069

A.7.5.1 Radio link Monitoring 4069

A.7.5.1.1 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode 4069

A.7.5.1.1.1 Test Purpose and Environment 4069

A.7.5.1.1.2 Test Requirements 4072

A.7.5.1.2 Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode 4072

A.7.5.1.2.1 Test Purpose and Environment 4072

A.7.5.1.2.2 Test Requirements 4075

A.7.5.1.3 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode 4075

A.7.5.1.3.1 Test Purpose and Environment 4075

A.7.5.1.3.2 Test Requirements 4077

A.7.5.1.4 Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode 4078

A.7.5.1.4.1 Test Purpose and Environment 4078

A.7.5.1.4.2 Test Requirements 4080

A.7.5.1.5 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode 4080

A.7.5.1.5.1 Test Purpose and Environment 4080

A.7.5.1.5.2 Test Requirements 4084

A.7.5.1.6 Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode 4084

A.7.5.1.6.1 Test Purpose and Environment 4084

A.7.5.1.6.2 Test Requirements 4088

A.7.5.1.7 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode 4088

A.7.5.1.7.1 Test Purpose and Environment 4088

A.7.5.1.7.2 Test Requirements 4091

A.7.5.1.8 Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode 4091

A.7.5.1.8.1 Test Purpose and Environment 4091

A.7.5.1.8.2 Test Requirements 4095

A.7.5.1.9 UE Radio Link Monitoring Scheduling Restrictions on FR2 4095

A.7.5.1.9.1 Test Purpose and Environment 4095

A.7.5.1.9.2 Test Requirements 4097

A.7.5.1.10 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode for UE supporting fast beam sweeping in multi-Rx 4097

A.7.5.1.10.1 Test Purpose and Environment 4097

A.7.5.1.10.2 Test Requirements 4100

A.7.5.1.11 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP 4100

A.7.5.1.11.1 Test Purpose and Environment 4100

A.7.5.1.12 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP 4100

A.7.5.1.12.1 Test Purpose and Environment 4100

A.7.5.1.12.2 Test Requirements 4101

A.7.5.1.13 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP 4101

A.7.5.1.13.1 Test Purpose and Environment 4101

A.7.5.1.13.2 Test Requirements 4104

A.7.5.1.14 Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode  for a UE operating with SBFD 4104

A.7.5.1.14.1 Test Purpose and Environment 4104

A.7.5.1.14.2 Test Requirements 4107

A.7.5.2 Interruption 4107

A.7.5.2.1 Interruptions during measurements on deactivated NR SCC in FR2 4107

A.7.5.2.1.1 Test Purpose and Environment 4107

A.7.5.2.1.2 Test Requirements 4109

A.7.5.2.2 SA interruptions at NR SRS carrier-based switching 4110

A.7.5.2.2.1 Test Purpose and Environment 4110

A.7.5.2.2.2 Test Parameters 4110

A.7.5.2.2.3 Test Requirements 4112

A.7.5.3 SCell Activation and Deactivation Delay 4112

A.7.5.3.1 SCell Activation and deactivation for SCell in FR2 intra-band in non-DRX 4112

A.7.5.3.1.1 Test Purpose and Environment 4112

A.7.5.3.1.2 Test Requirements 4113

A.7.5.3.2 SCell Activation and deactivation for FR1+FR2 inter-band with target SCell in FR2 4113

A.7.5.3.2.1 Test Purpose and Environment 4113

A.7.5.3.2.2 Test Requirements 4116

A.7.5.3.3 SCell Activation and deactivation for SCell in FR2 inter-band in non-DRX 4116

A.7.5.3.3.1 Test Purpose and Environment 4116

A.7.5.3.3.2 Test Requirements 4119

A.7.5.3.4 Direct SCell activation at SCell addition of known SCell in FR2 4119

A.7.5.3.4.1 Test Purpose and Environment 4119

A.7.5.3.4.2 Test Requirements 4121

A.7.5.3.5 Direct SCell activation at handover with known SCell in FR2 4122

A.7.5.3.5.1 Test Purpose and Environment 4122

A.7.5.3.5.2 Test Requirements 4124

A.7.5.3.6 PUCCH SCell activation and deactivation for FR1+FR2 inter-band with target SCell in FR2 and known 4125

A.7.5.3.6.1 Test Purpose and Environment 4125

A.7.5.3.6.2 Test Requirements 4128

A.7.5.3.7 PUCCH SCell activation and deactivation delay requirements of FR2 unknown cell with FR1 PCell 4128

A.7.5.3.7.1 Test Purpose and Environment 4128

A.7.5.3.7.2 Test Requirements 4131

A.7.5.3.8 SCell Activation and deactivation for known PUCCH SCell in FR2 inter-band in non-DRX 4132

A.7.5.3.8.1 Test Purpose and Environment 4132

A.7.5.3.8.2 Test Requirements 4135

A.7.5.3.9 PUCCH SCell Activation and deactivation of unknown SCell in FR2 4136

A.7.5.3.9.1 Test Purpose and Environment 4136

A.7.5.3.9.2 Test Requirements 4138

A.7.5.3.10 SCell Activation and deactivation of FR2 known PUCCH SCell and one FR2 unknown SCell with FR2 PCell 4139

A.7.5.3.10.1 Test Purpose and Environment 4139

A.7.5.3.10.2 Test Requirements 4142

A.7.5.3.11 PUCCH SCell activation and deactivation delay requirements of FR2 unknown cell with FR2 PCell 4143

A.7.5.3.11.1 PUCCH SCell activation with non-PUCCH SCell in a secondary PUCCH Group 4143

A.7.5.3.11.1.1 Test Purpose and Environment 4143

A.7.5.3.11.1.2 Test Requirements 4146

A.7.5.3.11.2 PUCCH SCell activation with non-PUCCH SCell in a primary PUCCH Group 4147

A.7.5.3.11.2.1 Test Purpose and Environment 4147

A.7.5.3.11.2.2 Test Requirements 4150

A.7.5.3.12 Void 4151

A.7.5.3.13 SCell Activation for SCell in FR2 intra-band in non-DRX 4151

A.7.5.3.13.1 Test Purpose and Environment 4151

A.7.5.3.13.2 Test Requirements 4153

A.7.5.3.14 SCell Activation for known SCell in FR2 inter-band 4153

A.7.5.3.14.1 Test Purpose and Environment 4153

A.7.5.3.14.2 Test Requirements 4155

A.7.5.3.15 PUCCH SCell activation and deactivation with FR1 PCell based on L3 reporting after SCell activation command 4156

A.7.5.3.15.1 Test Purpose and Environment 4156

A.7.5.3.15.2 Test Requirements 4160

A.7.5.3.16 PUCCH SCell activation and deactivation with FR2 PCell based on L3 reporting after SCell activation command 4160

A.7.5.3.16.1 Test Purpose and Environment 4160

A.7.5.3.16.2 Test Requirements 4163

A.7.5.3.17 SCell Activation and deactivation for SCell in FR2 inter-band in DRX for UE capable of small beam sweeping factors and/or short measurement interval 4164

A.7.5.3.17.1 Test Purpose and Environment 4164

A.7.5.3.17.2 Test Requirements 4166

A.7.5.3.18 SCell Activation and deactivation for FR1+FR2 inter-band with target SCell in FR2, in DRX, for UE capable of small beam sweeping factors and/or short measurement interval 4168

A.7.5.3.18.1 Test Purpose and Environment 4168

A.7.5.3.18.2 Test Requirements 4171

A.7.5.3.19 SCell Activation and deactivation of FR2 unknown SCell with FR1 PCell in non-DRX with L3 reporting during activation 4173

A.7.5.3.19.1 Test Purpose and Environment 4173

A.7.5.3.19.2 Test Requirements 4176

A.7.5.3.20 SCell Activation and Deactivation of FR2 unkown SCell with FR2 PCell in non-DRX with L3 reporting during activation 4176

A.7.5.3.20.1 Test Purpose and Environment 4177

A.7.5.3.20.2 Test Requirements 4179

A.7.5.3.21 OD-SSB based SCell Activation and deactivation of unknown SCell in FR2 DRX mode(OD-SSB Case 1) 4180

A.7.5.3.21.1 Test Purpose and Environment 4180

A.7.5.3.21.2 Test Requirements 4183

A.7.5.3.22 OD-SSB based SCell Activation for known SCell in FR2 inter-band 4183

A.7.5.3.22.1 Test Purpose and Environment 4183

A.7.5.3.22.2 Test Requirements 4186

A.7.5.3.23 EMR based SCell activation of unknown SCell in FR2 4186

A.7.5.3.23.1 Test Purpose and Environment 4186

A.7.5.3.23.2 Test Requirements 4190

A.7.5.3.24 EMR based SCell activation of unknown SCell in FR2 in RRC Inactive 4190

A.7.5.3.24.1 Test Purpose and Environment 4190

A.7.5.3.25 PUCCH SCell Activation of unknown SCell for UE supporting EMR in FR2 4195

A.7.5.3.25.1 Test Purpose and Environment 4195

A.7.5.3.25.2 Test Requirements 4198

A.7.5.4 Void 4198

A.7.5.5 Beam Failure Detection and Link recovery procedures 4198

A.7.5.5.1 Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode 4198

A.7.5.5.1.1 Test Purpose and Environment 4198

A.7.5.5.1.2 Test Requirements 4201

A.7.5.5.2 Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode 4202

A.7.5.5.2.1 Test Purpose and Environment 4202

A.7.5.5.2.2 Test Requirements 4205

A.7.5.5.3 Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode 4205

A.7.5.5.3.1 Test Purpose and Environment 4205

A.7.5.5.3.2 Test Requirements 4208

A.7.5.5.4 Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode 4208

A.7.5.5.4.1 Test Purpose and Environment 4208

A.7.5.5.4.2 Test Requirements 4211

A.7.5.5.5 Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode 4212

A.7.5.5.5.1 Test Purpose and Environment 4212

A.7.5.5.5.2 Test Requirements 4215

A.7.5.5.6 Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in non-DRX mode 4215

A.7.5.5.6.1 Test Purpose and Environment 4215

A.7.5.5.6.2 Test Requirements 4218

A.7.5.5.7 Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode 4218

A.7.5.5.7.1 Test Purpose and Environment 4218

A.7.5.5.7.2 Test Requirements 4221

A.7.5.5.8 Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode for UE fulfilling relaxed measurement criterion 4222

A.7.5.5.8.1 Test Purpose and Environment 4222

A.7.5.5.8.2 Test Requirements 4225

A.7.5.5.9 TRP specific Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode 4225

A.7.5.5.9.1 Test Purpose and Environment 4225

A.7.5.5.9.2 Test Requirements 4228

A.7.5.5.10 TRP specific Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode 4229

A.7.5.5.10.1 Test Purpose and Environment 4229

A.7.5.5.10.2 Test Requirements 4232

A.7.5.5.11 Beam Failure Detection and Link Recovery Test for FR2-2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode 4232

A.7.5.5.11.1 Test Purpose and Environment 4232

A.7.5.5.11.2 Test Requirements 4235

A.7.5.5.12 Beam Failure Detection and Link Recovery Test for FR2-2 PCell configured with CSI-RS-based BFD and LR in DRX mode 4235

A.7.5.5.12.1 Test Purpose and Environment 4235

A.7.5.5.12.2 Test Requirements 4238

A.7.5.5.13 Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2-2 PCell configured with SSB-based BFD and LR in non-DRX mode 4239

A.7.5.5.13.1 Test Purpose and Environment 4239

A.7.5.5.13.2 Test Requirements 4241

A.7.5.5.14 TRP specific Beam Failure Detection and Link Recovery for FR2 PCell configured with CSI-RS-based BFD and LR and multi-Rx operation in DRX mode 4241

A.7.5.5.14.1 Test Purpose and Environment 4241

A.7.5.5.14.2 Test Requirements 4245

A.7.5.5.15 Beam Failure Detection and Link Recovery Test for FR2 Pcell configured with CSI-RS-based BFD and LR in non-DRX mode for a UE operating with SBFD 4245

A.7.5.5.15.1 Test Purpose and Environment 4245

A.7.5.5.15.2 Test Requirements 4247

A.7.5.6 Active BWP switch 4247

A.7.5.6.1 DCI-based and Timer-based Active BWP Switch 4247

A.7.5.6.1.1 NR FR2- NR FR2 DL active BWP switch of SCell with non-DRX in SA 4247

A.7.5.6.1.2 NR FR1- NR FR2 DL active BWP switch of SCell with non-DRX in SA 4251

A.7.5.6.1.3 NR FR2 DL active BWP switch with non-DRX in SA 4255

A.7.5.6.1.3.1 Test Purpose and Environment 4255

A.7.5.6.1.3.2 Test Requirements 4257

A.7.5.6.1.4 NR FR2-2- NR FR2-2 DL active BWP switch of SCell with non-DRX in SA 4257

A.7.5.6.1.4.1 Test Purpose and Environment 4257

A.7.5.6.1.4.2 Test Requirements 4260

A.7.5.6.2 RRC-based Active BWP Switch 4261

A.7.5.6.2.1.1 Test Purpose and Environment 4261

A.7.5.6.2.1.2 Test Requirements 4264

A.7.5.6.2.2 NR FR2-2 DL active BWP switch of PCell with non-DRX in SA 4264

A.7.5.6.2.2.1 Test Purpose and Environment 4264

A.7.5.6.2.2.2 Test Requirements 4266

A.7.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs 4267

A.7.5.6.3.1.1 Test Purpose and Environment 4267

A.7.5.6.3.1.2 Test Requirements 4269

A.7.5.6.4 SCell dormancy switch 4270

A.7.5.6.4.1 NR FR2 PCell SCell dormancy switch of single FR2 SCell inside active time 4270

A.7.5.6.4.1.1 Test Purpose and Environment 4270

A.7.5.6.4.1.2 Test Requirements 4272

A.7.5.6.4.2 NR FR1 PCell SCell dormancy switch of two FR2 SCells outside active time 4273

A.7.5.6.4.2.1  Test Purpose and Environment 4273

A.7.5.6.4.2.2  Test Requirements 4276

A.7.5.6.5 Simultaneous RRC-based Active BWP Switch on multiple CCs 4276

A.7.5.6.5.1 Active BWP switch on multiple SCells with non-DRX in SA 4276

A.7.5.6.5.2 NR FR2-2 Active BWP switch on multiple SCells with non-DRX in SA 4278

A.7.5.6.5.2.1 Test Purpose and Environment 4278

A.7.5.6.5.2.2 Test Requirements 4281

A.7.5.7 PSCell addition and release delay 4281

A.7.5.7.1 Addition and Release Delay of known NR PSCell 4281

A.7.5.7.1.1 Test Purpose and Environment 4281

A.7.5.7.1.2 Test Requirements 4284

A.7.5.7.2 Addition and Release Delay of unknown NR PSCell in 4284

A.7.5.7.2.1 Test Purpose and Environment 4284

A.7.5.7.2.2 Test Requirements 4286

A.7.5.7.3 Addition and Release Delay of known NR PSCell in FR2-2 4286

A.7.5.7.3.1 Test Purpose and Environment 4286

A.7.5.7.3.2 Test Requirements 4289

A.7.5.7.4 Addition and Release Delay of unknown NR PSCell in FR2-2 4289

A.7.5.7.4.1 Test Purpose and Environment 4289

A.7.5.7.4.2 Test Requirements 4291

A.7.5.8 Active TCI state switch delay 4292

A.7.5.8.1 MAC-CE based active TCI state switch 4292

A.7.5.8.2 RRC based active TCI state switch 4295

A.7.5.8.3 MAC-CE based active TCI state switch for HST FR2 scenario 4298

A.7.5.8.3.1 NR PCell FR2 HST active TCI state switch for a known TCI state 4298

A.7.5.8.3.1.1 Test Purpose and Environment 4298

A.7.5.8.3.1.2 Test Requirements 4301

A.7.5.8.3.2 NR PCell FR2 HST active TCI state switch for PC6 UE supporting tciStateSwitchIndr18 for a known TCI state 4302

A.7.5.8.3.2.1 Test Purpose and Environment 4302

A.7.5.8.3.2.2 Test Requirements 4305

A.7.5.8.4 DCI based active TCI state switch with m-DCI for simultaneous reception 4305

A.7.5.8.4.1 Test Purpose and Environment 4305

A.7.5.8.4.2 Test Requirements 4308

A.7.5.8.5 Single-DCI FR2 DCI based active TCI state switch with known target TCI states for simultaneous reception 4308

A.7.5.8.5.1 Test Purpose and Environment 4308

A.7.5.8.5.1.2 Test Requirements 4310

A.7.5.9 Uplink spatial relation switch delay 4311

A.7.5.9.1.1.1 Test Purpose and Environment 4311

A.7.5.9.1.1.2 Test Requirements 4313

A.7.5.9.2 RRC based spatial relation switch 4313

A.7.5.9.2.1 NR PCell FR2 spatial relation switch associated with a known DL-RS 4313

A.7.5.9.2.1.1 Test Purpose and Environment 4313

A.7.5.9.2.1.2 Test Requirements 4315

A.7.5.10 UE specific CBW change 4315

A.7.5.10.1 NR FR2 UE specific CBW change of PCell with non-DRX in SA 4315

A.7.5.10.1.1 Test Purpose and Environment 4315

A.7.5.10.1.2 Test Requirements 4317

A.7.5.11 UE UL carrier RRC reconfiguration Delay 4318

A.7.5.11.1 UE UL carrier RRC reconfiguration Delay 4318

A.7.5.11.1.1 Test Purpose and Environment 4318

A.7.5.11.1.2 Test Requirements 4320

A.7.5.12 Conditional PSCell addition and release delay (FR2 SA) 4320

A.7.5.12.1 Addition and Release Delay of PSCell 4320

A.7.5.12.1.1 Test purpose and environment 4320

A.7.5.12.1.2 Test Parameters 4320

A.7.5.12.1.3 Test Requirements 4322

A.7.5.13 Unified TCI state switching delay 4322

A.7.5.13.1 MAC-CE based active joint TCI state switching 4322

A.7.5.13.1.1 NR PCell FR2 active joint TCI state switch for a known TCI state 4322

A.7.5.13.1.1.1 Test Purpose and Environment 4322

A.7.5.13.1.1.2 Test parameters 4323

A.7.5.13.1.1.3 Test Requirements 4324

A.7.5.13.2  MAC-CE based active uplink TCI state switch 4325

A.7.5.13.2.1  NR FR2 PCell uplink TCI state switch for a known TCI state 4325

A.7.5.13.2.1.1 Test Purpose and Environment 4325

A.7.5.13.2.1.2 Test parameters 4325

A.7.5.13.2.1.3 Test Requirements 4327

A.7.5.13.3 MAC-CE based active downlink TCI state switch 4327

A.7.5.13.3.1 NR PCell FR2 active downlink TCI state switch to cell with additional PCI for a known TCI state 4327

A.7.5.13.3.1.1 Test Purpose and Environment 4327

A.7.5.13.3.1.2 Test Parameters 4327

A.7.5.13.3.1.3 Test Requirements 4330

A.7.5.13.4 sDCI MAC-CE based joint TCI state switching 4331

A.7.5.13.4.1 NR PCell FR2 dual downlink and uplink TCI state switch in sDCI for known case 4331

A.7.5.13.4.1.1 Test Purpose and Environment 4331

A.7.5.13.4.1.2 Test parameters 4331

A.7.5.13.4.1.3 Test Requirements 4333

A.7.5.13.5 MAC-CE based dual downlink TCI state switching delay for unified TCI for single-DCI mTRP 4333

A.7.5.13.5.1 NR PCell FR2 dual downlink TCI state switch in sDCI for known case 4333

A.7.5.13.5.1.1 Test Purpose and Environment 4333

A.7.5.13.5.1.2 Test Parameters 4334

A.7.5.13.5.1.3 Test Requirements 4336

A.7.5.13.6  MAC-CE based active uplink TCI state switch for single-DCI mTRP 4336

A.7.5.13.6.1  NR FR2 PCell uplink TCI state switch for two known TCI states 4336

A.7.5.13.6.1.1 Test Purpose and Environment 4336

A.7.5.13.6.1.2 Test parameters 4337

A.7.5.13.6.1.3 Test Requirements 4338

A.7.5.14 PSCell RACH-less based Activation and deactivation for FR1+FR2 inter-band with target PSCell in FR2 4338

A.7.5.14.1 Test Purpose and Environment 4338

A.7.5.14.2 Test Requirements 4341

A.7.5.15 Void 4341

A.7.5.16 UE L1-RSRP Scheduling and Measurement Restrictions on FR2-1 4342

A.7.5.16.1 Test Purpose and Environment 4342

A.7.5.16.2 Test Requirements 4344

A.7.5.17 SCG Activation and deactivation for FR1+FR1 inter-band with target PSCell in FR1 4345

A.7.5.17.1 Test Purpose and Environment 4345

A.7.5.17.2 Test Requirements 4347

A.7.5.18 Subsequent conditional PSCell addition/change 4348

A.7.5.18.1 Intra-frequency subsequent CPC from FR1-FR2 NR-DC to FR1-FR2 NR-DC 4348

A.7.5.18.1.1 Test purpose and environment 4348

A.7.5.18.1.2 Test Requirements 4351

A.7.5.18.2 Inter-frequency subsequent CPA from FR1-FR2 NR-DC to FR1-FR2 NR-DC 4352

A.7.5.18.2.1 Test Purpose and Environment 4352

A.7.5.18.2.2 Test Requirements 4354

A.7.6 Measurement procedure 4356

A.7.6.1 Intra-frequency Measurements 4356

A.7.6.1.1 SA event triggered reporting test without gap under non-DRX 4356

A.7.6.1.1.1 Test purpose and Environment 4356

A.7.6.1.1.2 Test Requirements 4358

A.7.6.1.2 SA event triggered reporting test without gap under DRX 4358

A.7.6.1.2.1 Test purpose and Environment 4358

A.7.6.1.2.2 Test Requirements 4360

A.7.6.1.3 SA event triggered reporting test with per-UE gaps under non-DRX 4360

A.7.6.1.3.1 Test purpose and Environment 4360

A.7.6.1.3.2 Test Requirements 4363

A.7.6.1.4 SA event triggered reporting test with per-UE gaps under DRX 4363

A.7.6.1.4.1 Test purpose and Environment 4363

A.7.6.1.4.2 Test Requirements 4365

A.7.6.1.5 SA event triggered reporting test without gap under non-DRX for UE configured with highSpeedMeasFlagFR2-r17 4366

A.7.6.1.5.1 Test purpose and Environment 4366

A.7.6.1.5.2 Test Requirements 4368

A.7.6.1.6 SA event triggered reporting test without gap under non-DRX for FR2-2 4368

A.7.6.1.6.1 Test purpose and Environment 4368

A.7.6.1.6.2 Test Requirements 4370

A.7.6.1.7 SA event triggered reporting test without gap under DRX for FR2-2 4371

A.7.6.1.7.1 Test purpose and Environment 4371

A.7.6.1.7.2 Test Requirements 4373

A.7.6.1.8 SA event triggered reporting test with per-UE gaps under non-DRX for FR2-2 4374

A.7.6.1.8.1 Test purpose and Environment 4374

A.7.6.1.8.2 Test Requirements 4376

A.7.6.1.9 SA event triggered reporting test with per-UE gaps under DRX for FR2-2 4377

A.7.6.1.9.1 Test purpose and Environment 4377

A.7.6.1.9.2 Test Requirements 4379

A.7.6.1.10 SA event triggered reporting test with SSB time index detection without gap under non-DRX for FR2-2 4380

A.7.6.1.10.1 Test purpose and Environment 4380

A.7.6.1.10.2 Test Requirements 4382

A.7.6.1.11 SA event triggered reporting test with SSB time index detection with per-UE gaps under non-DRX for FR2-2 4382

A.7.6.1.11.1 Test purpose and Environment 4382

A.7.6.1.11.2 Test Requirements 4384

A.7.6.1.12 SA event triggered reporting test without gap under non-DRX when CD-SSB is outside active BWP 4385

A.7.6.1.12.1 Test purpose and Environment 4385

A.7.6.1.12.2 Test Requirements 4385

A.7.6.1.13 SA event triggered reporting test without gap under non-DRX with NCD-SSB 4385

A.7.6.1.13.1 Test purpose and Environment 4385

A.7.6.1.13.2 Test Requirements 4387

A.7.6.1.14 SA event triggered reporting test without gap under non-DRX for power class 6 UE supporting measEnhCAInterFreqFR2-r18 4388

A.7.6.1.14.1 Test Purpose and Environment 4388

A.7.6.1.14.2 Test Requirements 4389

A.7.6.1.15 SA event triggered reporting test without gap for SCell under non-DRX based on OD-SSB 4389

A.7.6.1.15.1 Test purpose and Environment 4389

A.7.6.1.15.2 Test Requirements 4392

A.7.6.1.16 SA event triggered reporting test without gap under non-DRX on deactivated SCell based on OD-SSB 4392

A.7.6.1.16.1 Test purpose and Environment 4392

A.7.6.1.16.2 Test Requirements 4394

A.7.6.1.17 SA event triggered reporting test under non-DRX on Rx BSF optimization for SSB based intra-frequency measurement without MG 4394

A.7.6.1.17.1 Test purpose and Environment 4394

A.7.6.1.17.2 Test Requirements 4396

A.7.6.1.18 SA event triggered reporting test with per-UE gaps under DRX for UE supporting multi-Rx based L3 measurement in FR2 4396

A.7.6.1.18.1 Test purpose and Environment 4396

A.7.6.1.18.2 Test Requirements 4398

A.7.6.1.19 SA event triggered reporting test without gap under non-DRX for UE configured with cssf-Config 4399

A.7.6.1.19.1 Test purpose and Environment 4399

A.7.6.1.19.2 Test Requirements 4401

A.7.6.2 Inter-frequency Measurements 4402

A.7.6.2.1 SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (PCell in FR2) 4402

A.7.6.2.1.1 Test Purpose and Environment 4402

A.7.6.2.1.2 Test Requirements 4404

A.7.6.2.2 SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used (PCell in FR2) 4404

A.7.6.2.2.1 Test Purpose and Environment 4404

A.7.6.2.2.2 Test Requirements 4406

A.7.6.2.3 SA event triggered reporting tests for FR2 with SSB time index detection when DRX is not used (PCell in FR2) 4407

A.7.6.2.3.1 Test Purpose and Environment 4407

A.7.6.2.3.2 Test Requirements 4409

A.7.6.2.4 SA event triggered reporting tests for FR2 with SSB time index detection when DRX is used (PCell in FR2) 4409

A.7.6.2.4.1 Test Purpose and Environment 4409

A.7.6.2.4.2 Test Requirements 4411

A.7.6.2.5 SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (PCell in FR1) 4412

A.7.6.2.5.1 Test Purpose and Environment 4412

A.7.6.2.5.2 Test Requirements 4414

A.7.6.2.6 SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used (PCell in FR1) 4415

A.7.6.2.6.1 Test Purpose and Environment 4415

A.7.6.2.6.2 Test Requirements 4417

A.7.6.2.7 SA event triggered reporting tests for FR2 with SSB time index detection when DRX is not used (PCell in FR1) 4418

A.7.6.2.7.1 Test Purpose and Environment 4418

A.7.6.2.7.2 Test Requirements 4420

A.7.6.2.8 SA event triggered reporting tests for FR2 with SSB time index detection when DRX is used (PCell in FR1) 4421

A.7.6.2.8.1 Test Purpose and Environment 4421

A.7.6.2.8.2 Test Requirements 4423

A.7.6.2.9 SA event triggered reporting tests For FR2 without SSB time index detection when DRX is not used (PCell in FR2) (rel16 additional mandatory gap pattern 17) 4424

A.7.6.2.9.1 Test Purpose and Environment 4424

A.7.6.2.9.2 Test Requirements 4426

A.7.6.2.10 SA event triggered reporting test without gap under non-DRX 4426

A.7.6.2.10.1 Test Purpose and Environment 4426

A.7.6.2.10.2 Test Requirements 4428

A.7.6.2.11 SA event triggered reporting test without gap under DRX 4428

A.7.6.2.11.1 Test Purpose and Environment 4428

A.7.6.2.11.2 Test Requirements 4430

A.7.6.2.12 SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is not used (PCell in FR2-2) 4430

A.7.6.2.12.1 Test Purpose and Environment 4430

A.7.6.2.12.2 Test Requirements 4433

A.7.6.2.13 SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is used (PCell in FR2-2) 4433

A.7.6.2.13.1 Test Purpose and Environment 4433

A.7.6.2.13.2 Test Requirements 4436

A.7.6.2.14 SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is not used (PCell in FR2-2) 4436

A.7.6.2.14.1 Test Purpose and Environment 4436

A.7.6.2.14.2 Test Requirements 4439

A.7.6.2.15 SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is used (PCell in FR2-2) 4439

A.7.6.2.15.1 Test Purpose and Environment 4439

A.7.6.2.15.2 Test Requirements 4442

A.7.6.2.16 SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is not used (PCell in FR1) 4443

A.7.6.2.16.1 Test Purpose and Environment 4443

A.7.6.2.16.2 Test Requirements 4447

A.7.6.2.17 SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is used (PCell in FR1) 4447

A.7.6.2.17.1 Test Purpose and Environment 4447

A.7.6.2.17.2 Test Requirements 4451

A.7.6.2.18 SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is not used (PCell in FR1) 4452

A.7.6.2.18.1 Test Purpose and Environment 4452

A.7.6.2.18.2 Test Requirements 4455

A.7.6.2.19 SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is used (PCell in FR1) 4456

A.7.6.2.19.1 Test Purpose and Environment 4456

A.7.6.2.19.2 Test Requirements 4460

A.7.6.2.20 SA event triggered reporting tests for FR2 with measurement gap with priority and two periodic MUSIM gaps configured 4461

A.7.6.2.20.1 Test Purpose and Environment 4461

A.7.6.2.20.2 Test Requirements 4463

A.7.6.2.21 SA event triggered reporting tests for FR2 with measurement gap without priority and periodic MUSIM gap configured 4463

A.7.6.2.21.1 Test Purpose and Environment 4463

A.7.6.2.21.2 Test Requirements 4465

A.7.6.2.22 SA event triggered reporting tests with SSB time index detection when DRX is not used (PCell in FR2) for FR2 power class 6 UE configured with highSpeedMeasFlagFR2-r17 4466

A.7.6.2.22.1 Test Purpose and Environment 4466

A.7.6.2.22.2 Test Requirements 4468

A.7.6.2.23 SA event triggered reporting tests without SSB time index detection when DRX is not used (PCell in FR2) for FR2 power class 6 UE configured with highSpeedMeasFlagFR2-r17 4468

A.7.6.2.23.1 Test Purpose and Environment 4468

A.7.6.2.23.2 Test Requirements 4470

A.7.6.2.24 SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (FR1+FR2 CA and LTE+ FR2 EN-DC) for UE supporting [CSSF enhancement for one CC measurement per-band] 4470

A.7.6.2.24.1 Test Purpose and Environment 4470

A.7.6.2.24.2 Test Requirements 4475

A.7.6.2.25 SA event triggered reporting tests for FR2 under non-DRX in FR1+FR2 CA for UE supporting threeCarrierMeasWithoutGap-r19 4475

A.7.6.2.25.1 Test purpose and Environment 4475

A.7.6.2.25.2 Test parameters 4475

A.7.6.2.25.3 Test Requirements 4479

A.7.6.2.26 SA event triggered reporting tests without gap under non-DRX in FR1+FR2 CA for UE supporting threeCarrierMeasWithoutGap-r19 4479

A.7.6.2.26.1 Test purpose and Environment 4479

A.7.6.2.26.2 Test parameters 4479

A.7.6.2.26.3 Test Requirements 4484

A.7.6.2.27 SA serving cell quality triggered reporting tests for FR2 with SSB time index detection when DRX is used (PCell in FR2) 4484

A.7.6.2.27.1 Test Purpose and Environment 4484

A.7.6.2.27.2 Test Requirements 4486

A.7.6.2.28 SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used 4487

A.7.6.2.28.1 Test Purpose and Environment 4487

A.7.6.2.28.2 Test Requirements 4488

A.7.6.3 L1-RSRP measurement for beam reporting 4488

A.7.6.3.1 SSB based L1-RSRP measurement when DRX is not used 4488

A.7.6.3.1.1 Test Purpose and Environment 4488

A.7.6.3.1.2 Test parameters 4488

A.7.6.3.1.3 Test Requirements 4490

A.7.6.3.2 SSB based L1-RSRP measurement when DRX is used 4490

A.7.6.3.2.1 Test Purpose and Environment 4490

A.7.6.3.2.2 Test parameters 4490

A.7.6.3.2.3 Test Requirements 4492

A.7.6.3.3 CSI-RS based L1-RSRP measurement when DRX is not used 4492

A.7.6.3.3.1 Test Purpose and Environment 4492

A.7.6.3.3.2 Test parameters 4492

A.7.6.3.3.3 Test Requirements 4494

A.7.6.3.4 CSI-RS based L1-RSRP measurement when DRX is used 4494

A.7.6.3.4.1 Test Purpose and Environment 4494

A.7.6.3.4.2 Test parameters 4494

A.7.6.3.3.3 Test Requirements 4496

A.7.6.3.5 SSB based L1-RSRP measurement when DRX is used for power class 6 UE configured with highSpeedMeasFlagFR2-r17 4496

A.7.6.3.5.1 Test Purpose and Environment 4496

A.7.6.3.5.2 Test parameters 4496

A.7.6.3.5.3 Test Requirements 4498

A.7.6.3.6 Inter-cell SSB based L1-RSRP measurements on FR2 SCell when DRX is not used 4498

A.7.6.3.6.1 Test Purpose and Environment 4498

A.7.6.3.6.2 Test parameters 4498

A.7.6.3.6.3 Test Requirements 4501

A.7.6.3.7 SSB based L1-RSRP measurement for FR2-2 when DRX is used 4501

A.7.6.3.7.1 Test Purpose and Environment 4501

A.7.6.3.7.2 Test parameters 4502

A.7.6.3.7.3 Test Requirements 4503

A.7.6.3.8 CSI-RS based L1-RSRP measurement when DRX is not used and when CD-SSB is outside active BWP 4503

A.7.6.3.8.1 Test Purpose and Environment 4503

A.7.6.3.9 SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP 4504

A.7.6.3.9.1 Test Purpose and Environment 4504

A.7.6.3.9.2 Test Requirements 4504

A.7.6.3.10 SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used 4504

A.7.6.3.10.1 Test Purpose and Environment 4504

A.7.6.3.10.2 Test parameters 4504

A.7.6.3.10.3 Test Requirements 4506

A.7.6.3.11 SSB based L1-RSRP measurement when DRX is used for power class 6 UE supporting simultaneousReceptionTwoQCL-r18 4506

A.7.6.3.11.1 Test Purpose and Environment 4506

A.7.6.3.11.2 Test parameters 4506

A.7.6.3.11.3 Test Requirements 4508

A.7.6.3.12 SSB based L1-RSRP measurement when DRX is not used 4508

A.7.6.3.12.1 Test Purpose and Environment 4508

A.7.6.3.12.2 Test parameters 4508

A.7.6.3.12.3 Test Requirements 4511

A.7.6.3.13 Event Triggered Reporting for the UE initiated beam management 4511

A.7.6.3.13.1 Test Purpose and Environment 4511

A.7.6.3.13.2 Test parameters 4511

A.7.6.3.13.3 Test Requirements 4513

A.7.6.3.14 CSI-RS based UE-initiated/event-driven beam management of event2 4513

A.7.6.3.14.1 Test Purpose and Environment 4513

A.7.6.3.14.2 Test parameters 4513

A.7.6.3.14.3 Test Requirements 4515

A.7.6.3.15 Event triggered reporting for UE initiated beam management for UE configured with Inter-cell SSB based L1-RSRP measurement on FR2 when DRX is not used 4515

A.7.6.3.15.1 Test Purpose and Environment 4515

A.7.6.3.15.2 Test parameters 4515

A.7.6.3.15.3 Test Requirements 4518

A.7.6.3.16 CSI-RS based L1-RSRP measurement when DRX is not used with SBFD 4518

A.7.6.3.16.1 Test Purpose and Environment 4518

A.7.6.3.16.2 Test parameters 4518

A.7.6.3.16.3 Test Requirements 4520

A.7.6.4 CLI measurements 4520

A.7.6.4.1 SRS-RSRP measurement with non-DRX 4520

A.7.6.4.1.1 Test Purpose and Environment 4520

A.7.6.4.1.2 Test Parameters 4520

A.7.6.4.1.3 Test Requirements 4522

A.7.6.4.2 CLI-RSSI measurement with non-DRX 4522

A.7.6.4.2.1 Test Purpose and Environment 4522

A.7.6.4.2.2 Test Parameters 4522

A.7.6.4.2.3 Test Requirements 4524

A.7.6.5.1 SA interfrequency CGI reporting in autonomous gaps test (PCell in FR2) 4524

A.7.6.5.1.1 Test Purpose and Environment 4524

A.7.6.5.1.2 Test Requirements 4526

A.7.6.6 L1-SINR measurement for beam reporting 4526

A.7.6.6.2 L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is used 4528

A.7.6.6.2.1 Test Purpose and Environment 4528

A.7.6.6.2.2 Test parameters 4529

A.7.6.6.2.3 Test Requirements 4530

A.7.6.6.3 L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is used 4530

A.7.6.6.3.1 Test Purpose and Environment 4530

A.7.6.6.3.2 Test parameters 4530

A.7.6.6.3.3 Test Requirements 4532

A.7.6.6.4 L1-SINR measurement with SSB based CMR and dedicated IMR with SBFD 4532

A.7.6.6.4.1 Test Purpose and Environment 4532

A.7.6.6.4.2 Test parameters 4532

A.7.6.6.4.3 Test Requirements 4533

A.7.6.7 CSI-RS based intra-frequency Measurements 4534

A.7.6.7.1 SA event triggered reporting test without gap under DRX for CSI-RS based intra-frequency measurement 4534

A.7.6.7.1.1 Test purpose and Environment 4534

A.7.6.7.1.2 Test Requirements 4535

A.7.6.8 CSI-RS based inter-frequency Measurements 4536

A.7.6.8.1 SA event triggered reporting tests for FR2 CSI-RS based measurement when non-DRX is used (PCell in FR2) 4536

A.7.6.8.1.1 Test Purpose and Environment 4536

A.7.6.8.1.2 Test Requirements 4538

A.7.6.9 RSTD measurements 4538

A.7.6.9.1  NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA 4538

A.7.6.9.1.1 Test Purpose and Environment 4538

A.7.6.9.1.2 Test Requirements 4542

A.7.6.9.2  NR RSTD measurement reporting delay test case for dual positioning frequency layers in FR2 SA 4542

A.7.6.9.2.1 Test Purpose and Environment 4542

A.7.6.9.2.2 Test Requirements 4545

A.7.6.9.3 NR RSTD measurement reporting delay test case for single positioning frequency layer with reduced number of samples in FR2 SA 4546

A.7.6.9.3.1 Test Purpose and Environment 4546

A.7.6.9.3.2 Test Requirements 4548

A.7.6.9.4 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA without measurement gap 4549

A.7.6.9.4.1 Test Purpose and Environment 4549

A.7.6.9.4.2 Test Requirements 4551

A.7.6.9.5 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_CONNECTED state with Rx TEG 4552

A.7.6.9.5.1 Test Purpose and Environment 4552

A.7.6.9.5.2 Test Requirements 4555

A.7.6.9.6 NR RSTD measurement reporting delay test case for PRS aggregation in FR2 SA in RRC_CONNECTED mode 4555

A.7.6.9.6.1 Test Purpose and Environment 4555

A.7.6.9.6.2 Test Requirements 4563

A.7.6.10 PRS-RSRP measurements 4563

A.7.6.10.1 PRS-RSRP reporting delay test case for single positioning frequency layer 4563

A.7.6.10.1.1 Test Purpose and Environment 4563

A.7.6.10.1.2 Test Requirements 4565

A.7.6.10.2 PRS-RSRP reporting delay test case for dual positioning frequency layer 4566

A.7.6.10.2.1 Test Purpose and Environment 4566

A.7.6.10.2.2 Test Requirements 4568

A.7.6.10.3 PRS-RSRP reporting delay test case for reduced number of samples 4568

A.7.6.10.3.1 Test Purpose and Environment 4568

A.7.6.10.3.2 Test Requirements 4570

A.7.6.10.4 PRS-RSRP reporting delay test case for single positioning frequency layer outside MG 4571

A.7.6.10.4.1 Test Purpose and Environment 4571

A.7.6.10.4.2 Test Requirements 4573

A.7.6.11 UE Rx-Tx time difference measurements 4573

A.7.6.11.1 UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA 4573

A.7.6.11.1.1 Test purpose and environment 4573

A.7.6.11.1.2 Test requirements 4575

A.7.6.11.2 UE Rx-Tx time difference measurement period for dual positioning frequency layers in FR2 SA 4575

A.7.6.11.2.1 Test purpose and environment 4575

A.7.6.11.2.2 Test requirements 4577

A.7.6.11.3 UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA with reduced sample number 4578

A.7.6.11.3.1 Test purpose and environment 4578

A.7.6.11.3.2 Test requirements 4579

A.7.6.11.4 UE Rx-Tx time difference measurements without gaps in FR2 SA 4580

A.7.6.11.4.1 Test purpose and environment 4580

A.7.6.11.4.2 Test requirements 4581

A.7.6.11.5 UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA with RxTx TEG 4582

A.7.6.11.5.1 Test purpose and environment 4582

A.7.6.11.5.2 Test requirements 4583

A.7.6.11.6 UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR2 SA 4584

A.7.6.11.6.1 Test purpose and environment 4584

A.7.6.11.6.2 Test requirements 4587

A.7.6.12 PRS-RSRPP measurements 4587

A.7.6.12.1 PRS-RSRPP reporting delay test case for single positioning frequency layer in FR2 in RRC_CONNECTED state 4587

A.7.6.12.1.1 Test Purpose and Environment 4587

A.7.6.12.1.2 Test Requirements 4590

A.7.6.12.2 PRS-RSRPP reporting delay test case for reduced number of samples for single positioning frequency layer in FR2 in RRC_CONNECTED state 4590

A.7.6.12.2.1 Test Purpose and Environment 4590

A.7.6.12.2.2 Test Requirements 4592

A.7.6.12.3 PRS-RSRPP reporting delay test case for gapless measurement in FR2 4593

A.7.6.12.3.1 Test Purpose and Environment 4593

A.7.6.12.3.2 Test Requirements 4595

A.7.6.13 UE Rx-Tx time difference measurements for PDC 4595

A.7.6.13.1 UE Rx-Tx time difference measurement for propagation delay compensation using PRS in FR2 4595

A.7.6.13.1.1 Test purpose and environment 4595

A.7.6.13.1.2 Test requirements 4597

A.7.6.13.2 UE Rx-Tx time difference measurement for propagation delay compensation using TRS in FR2 4597

A.7.6.13.2.1 Test purpose and environment 4597

A.7.6.13.2.2 Test requirements 4598

A.7.6.14 SA event triggered reporting tests with Pre-MG 4599

A.7.6.14.1 Intra-frequency measurement test with SA event triggered reporting tests: with autonomous activation/deactivation of Pre-MG in FR2 4599

A.7.6.14.1.1 Test purpose and Environment 4599

A.7.6.14.1.2 Test parameters 4599

A.7.6.14.1.3 Test Requirements 4601

A.7.6.14.2 Intra-frequency measurement test with SA event triggered reporting tests: with network-controlled activation/deactivation of Pre-MG in FR2 4601

A.7.6.14.2.1 Test purpose and Environment 4601

A.7.6.14.2.2 Test parameters 4601

A.7.6.14.2.3 Test Requirements 4603

A.7.6.15 SA event triggered reporting tests with concurrent gaps 4604

A.7.6.15.1 SA event triggered reporting tests For FR2 with fully non-overlapping concurrent MGs for SSB-based inter-frequency measurements 4604

A.7.6.15.1.1 Test Purpose and Environment 4604

A.7.6.15.1.2 Test Requirements 4606

A.7.6.15.2 SA event triggered reporting tests For FR2 with concurrent measurement gaps without SSB time index detection when DRX is not used (PCell in FR2) 4606

A.7.6.15.2.1 Test Purpose and Environment 4606

A.7.6.15.2.2 Test Requirements 4609

A.7.6.15.3 SA event triggered reporting tests for FR2 concurrent gap with partially partial overlapping scenario for SSB-based measurements and PRS-based measurement 4609

A.7.6.15.3.1 Test Purpose and Environment 4609

A.7.6.15.3.2 Test Requirements 4611

A.7.6.16 SA event triggered reporting tests with NCSG 4612

A.7.6.16.1 SA event triggered reporting test with per-UE NCSG under non-DRX 4612

A.7.6.16.1.1 Test purpose and Environment 4612

A.7.6.16.1.2 Test Requirements 4614

A.7.6.16.2 SA event triggered reporting tests on inter-frequency measurement with NCSG for FR2 when DRX is not used (PCell in FR2) 4615

A.7.6.16.2.1 Test Purpose and Environment 4615

A.7.6.16.2.2 Test Requirements 4617

A.7.6.16.3 Event triggered reporting test on deactivated SCell measurement via NCSG in FR2 in non-DRX 4617

A.7.6.16.3.1 Test Purpose and Environment 4617

A.7.6.16.3.2 Test Requirements 4619

A.7.6.17 SA event triggered reporting tests for concurrent measurement gaps with Pre-MG in FR2 4620

A.7.6.17.1 SA event triggered reporting test for FR2 with one pre-configured gap and one measurement gap 4620

A.7.6.17.1.1 Test Purpose and Environment 4620

A.7.6.17.1.2 Test Requirements 4622

A.7.6.17.2 Inter-frequency measurement test with SA event triggered reporting tests: with autonomous activation/deactivation of Pre-MGs in FR2 4623

A.7.6.17.2.1 Test purpose and Environment 4623

A.7.6.17.2.2 Test parameters 4623

A.7.6.17.2.3 Test Requirements 4625

A.7.6.18 SA event triggered reporting tests with concurrent gaps and NCSG 4626

A.7.6.18.1 SA event triggered reporting tests For FR2 with concurrent measurement gaps and NCSG without SSB time index detection when DRX is not used (PCell in FR2) 4626

A.7.6.18.1.1 Test Purpose and Environment 4626

A.7.6.18.1.2 Test Requirements 4628

A.7.6.19 SA event triggered reporting tests with NeedForGap in FR2 4629

A.7.6.19.1 SA event triggered reporting test for UE indicating NeedforInterruptionInfoNR under non-DRX and no interruption outside configured measurement gaps 4629

A.7.6.19.1.1 Test purpose and Environment 4629

A.7.6.19.1.2 Test Requirements 4631

A.7.6.19.2 SA event triggered reporting test without gap under non-DRX 4631

A.7.6.19.2.1 Test purpose and Environment 4631

A.7.6.19.2.2 Test Requirements 4633

A.7.6.19.3 SA event triggered reporting test without gap without interruption under non-DRX 4634

A.7.6.19.3.1 Test Purpose and Environment 4634

A.7.6.19.3.2 Test Requirements 4636

A.7.6.20 LTM Intra-frequency L1-RSRP measurement 4636

A.7.6.20.1 Intra-frequency SSB based L1-RSRP measurement in FR2 4636

A.7.6.20.1.1 Test Purpose and Environment 4636

A.7.6.20.1.2 Test parameters 4637

A.7.6.20.1.3 Test Requirements 4639

A.7.6.20.2 Intra-frequency SSB based L1-RSRP measurement in FR2 with event triggered reporting 4639

A.7.6.20.2.1 Test Purpose and Environment 4639

A.7.6.20.2.2 Test parameters 4639

A.7.6.20.2.3 Test Requirements 4640

A.7.6.20.3 CSI-RS based L1-RSRP intra-frequency measurement for neighbour cell in FR2 without SSB based L1-RSRP measurement 4640

A.7.6.20.3.1 Test purpose and Environment 4640

A.7.6.20.3.2 Test parameters 4640

A.7.6.20.3.3 Test Requirements 4642

A.7.6.20.4 Intra-frequency CSI-RS based L1-RSRP measurement in FR2 4643

A.7.6.20.4.1 Test Purpose and Environment 4643

A.7.6.20.4.3 Test Requirements 4645

A.7.6.21 LTM Inter-frequency L1-RSRP measurement with measurement gap 4646

A.7.6.21.1 Inter-frequency SSB-based L1-RSRP measurement with measurement gap for LTM in FR2 4646

A.7.6.21.1.1 Test Purpose and Environment 4646

A.7.6.21.1.2 Test parameters 4646

A.7.6.21.1.3 Test Requirements 4648

A.7.6.21.2 Inter-frequency SSB-based L1-RSRP measurement with measurement gap in FR2 with event triggered reporting 4648

A.7.6.21.2.3 Test Requirements 4649

A.7.6.22 LTM Inter-frequency L1-RSRP measurement without measurement gap 4649

A.7.6.22.1 Inter-frequency SSB based L1-RSRP measurement without measurement gap in FR2 4649

A.7.6.22.1.1 Test Purpose and Environment 4649

A.7.6.22.1.2 Test parameters 4649

A.7.6.22.1.3 Test Requirements 4651

A.7.6.23 Idle Mode CA/DC Measurements 4652

A.7.6.23.1 Test case for Idle mode fast CA/DC eEMR measurement for FR2 without valid reporting 4652

A.7.6.23.1.1 Test Purpose and Environment 4652

A.7.6.23.1.2 Test Requirements 4655

A.7.6.23.2 Test case for Idle mode fast CA/DC cell reselection measurement for FR2 without valid reporting 4655

A.7.6.23.2.1 Test Purpose and Environment 4655

A.7.6.23.2.2 Test Requirements 4658

A.7.6.23.3 Test case for Idle mode fast CA/DC cell reselection measurement for FR2 with valid reporting 4659

A.7.6.23.3.1 Test Purpose and Environment 4659

A.7.6.23.3.2 Test Requirements 4662

A.7.6.24 RSCPD measurements 4662

A.7.6.24.1 NR RSCPD with RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_CONNECTED state 4662

A.7.6.24.1.1 Test Purpose and Environment 4662

A.7.6.24.1.2 Test Requirements 4670

A.7.6.25 RSCP measurements 4670

A.7.6.25.1 DL RSCP with UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA 4670

A.7.6.25.1.1 Test purpose and environment 4670

A.7.6.25.1.2 Test requirements 4674

A.7.6.26 Inter-RAT Measurements 4674

A.7.6.26.1 SA event triggered reporting test without gap under non-DRX for UE configured with [MeasuringoneCCperFR2band] in FR2 inter-band CA 4674

A.7.6.26.1.1 Test purpose and Environment 4674

A.7.6.26.1.2 Test Requirements 4676

A.7.6.27 L1 CLI measurements 4677

A.7.6.27.1 L1-SRS-RSRP measurement with DRX with SBFD 4677

A.7.6.27.1.1 Test Purpose and Environment 4677

A.7.6.27.1.2 Test Parameters 4677

A.7.6.27.1.3 Test Requirements 4679

A.7.6.27.2 L1-CLI-RSSI measurement with DRX with SBFD 4679

A.7.6.27.2.1 Test Purpose and Environment 4679

A.7.6.27.2.2 Test Parameters 4679

A.7.6.27.2.3 Test Requirements 4681

A.7.6.28 LTM Inter-frequency L1-RSRP event triggered reporting without measurement gap 4681

A.7.6.28.1 Inter-frequency SSB based L1-RSRP measurement without measurement gap in FR2 4681

A.7.6.28.1.1 Test Purpose and Environment 4681

A.7.6.28.1.2 Test parameters 4681

A.7.6.28.1.3 Test Requirements 4682

A.7.6.29 LTM Inter-frequency L1-RSRP measurement with measurement gap cancellation 4682

A.7.6.29.1 Inter-frequency SSB-based L1-RSRP measurement with measurement gap cancellation for LTM in FR2 4682

A.7.6.29.1.1 Test Purpose and Environment 4682

A.7.6.29.1.2 Test parameters 4682

A.7.6.29.1.3 Test Requirements 4683

A.7.6.30 DL AI/ML positioning reporting delay test case for single positioning frequency layer in FR2 SA 4683

A.7.6.30.1 Test Purpose and Environment 4683

A.7.6.30.2 Test Requirements 4686

A.7.7 Measurement Performance requirements 4686

A.7.7.1 SS-RSRP 4686

A.7.7.1.1 SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell 4686

A.7.7.1.1.1 Test Purpose and Environment 4687

A.7.7.1.1.2 Test parameters 4687

A.7.7.1.1.3 Test Requirements 4688

A.7.7.1.2 SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell 4689

A.7.7.1.2.1 Test Purpose and Environment 4689

A.7.7.1.2.2 Test parameters 4689

A.7.7.1.2.3 Test Requirements 4691

A.7.7.1.3 SA inter-frequency measurement accuracy with FR1 serving cell and FR2 target cell 4692

A.7.7.1.3.1 Test Purpose and Environment 4692

A.7.7.1.3.2 Test parameters 4692

A.7.7.1.3.3 Test Requirements 4694

A.7.7.2 SS-RSRQ 4695

A.7.7.2.1 SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell 4695

A.7.7.2.1.1 Test Purpose and Environment 4695

A.7.7.2.1.2 Test Parameters 4695

A.7.7.2.1.3 Test Requirements 4696

A.7.7.2.2 SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell 4697

A.7.7.2.2.1 Test Purpose and Environment 4697

A.7.7.2.2.2 Test Parameters 4697

A.7.7.2.2.3 Test Requirements 4698

A.7.7.3 SS-SINR 4698

A.7.7.3.1 SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell 4698

A.7.7.3.1.1 Test Purpose and Environment 4698

A.7.7.3.1.2 Test Parameters 4698

A.7.7.3.1.3 Test Requirements 4700

A.7.7.3.2 SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell 4700

A.7.7.3.2.1 Test Purpose and Environment 4700

A.7.7.3.2.2 Test Parameters 4700

A.7.7.3.2.3 Test Requirements 4701

A.7.7.4 L1-RSRP measurement for beam reporting 4702

A.7.7.4.1 SSB based L1-RSRP measurement 4702

A.7.7.4.1.1 Test Purpose and Environment 4702

A.7.7.4.1.2 Test parameters 4702

A.7.7.4.1.3 Test Requirements 4703

A.7.7.4.2 CSI-RS based L1-RSRP measurement on resource set with repetition off 4704

A.7.7.4.2.1 Test Purpose and Environment 4704

A.7.7.4.2.2 Test parameters 4704

A.7.7.4.2.3 Test Requirements 4705

A.7.7.4.3 CSI-RS based L1-RSRP measurement with SBFD DUD 4706

A.7.7.4.3.1 Test Purpose and Environment 4706

A.7.7.4.3.2 Test parameters 4706

A.7.7.4.3.3 Test Requirements 4707

A.7.7.4.4 CSI-RS based L1-RSRP measurement with SBFD DU 4708

A.7.7.4.4.1 Test Purpose and Environment 4708

A.7.7.4.4.2 Test parameters 4708

A.7.7.4.4.3 Test Requirements 4709

A.7.7.5 CLI measurements 4710

A.7.7.5.1 SA SRS-RSRP measurement accuracy with FR2 serving cell 4710

A.7.7.5.1.1 Test Purpose and Environment 4710

A.7.7.5.1.2 Test parameters 4710

A.7.7.5.1.3 Test Requirements 4712

A.7.7.5.2 SA CLI-RSSI measurement accuracy with FR2 serving cell 4712

A.7.7.5.2.1 Test Purpose and Environment 4712

A.7.7.5.2.2 Test parameters 4712

A.7.7.5.2.3 Test Requirements 4714

A.7.7.6 L1-SINR measurement for beam reporting 4714

A.7.7.6.1.1 Test Purpose and Environment 4714

A.7.7.6.1.2 Test parameters 4715

A.7.7.6.1.3 Test Requirements 4716

A.7.7.6.2 L1-SINR measurement with SSB based CMR and dedicated IMR 4716

A.7.7.6.2.1 Test Purpose and Environment 4716

A.7.7.6.2.2 Test parameters 4717

A.7.7.6.2.3 Test Requirements 4718

A.7.7.6.3 L1-SINR measurement with CSI-RS based CMR and dedicated IMR 4718

A.7.7.6.3.1 Test Purpose and Environment 4718

A.7.7.6.3.2 Test parameters 4719

A.7.7.6.3.3 Test Requirements 4720

A.7.7.7 CSI-RSRP 4720

A.7.7.7.1 SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell 4720

A.7.7.7.1.1 Test Purpose and Environment 4720

A.7.7.7.1.2 Test parameters 4721

A.7.7.7.1.3 Test Requirements 4722

A.7.7.7.2 SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell 4723

A.7.7.7.2.1 Test Purpose and Environment 4723

A.7.7.7.2.2 Test parameters 4723

A.7.7.7.2.3 Test Requirements 4725

A.7.7.8 CSI-RSRQ 4726

A.7.7.8.1 SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell 4726

A.7.7.8.1.1 Test Purpose and Environment 4726

A.7.7.8.1.2 Test Parameters 4726

A.7.7.8.1.3 Test Requirements 4727

A.7.7.8.2 SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell 4727

A.7.7.8.2.1 Test Purpose and Environment 4727

A.7.7.8.2.2 Test Parameters 4728

A.7.7.8.2.3 Test Requirements 4729

A.7.7.9 CSI-SINR 4729

A.7.7.9.1 SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell 4729

A.7.7.9.1.1 Test Purpose and Environment 4729

A.7.7.9.1.2 Test Parameters 4729

A.7.7.9.1.3 Test Requirements 4731

A.7.7.9.2 SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell 4731

A.7.7.9.2.1 Test Purpose and Environment 4731

A.7.7.9.2.2 Test Parameters 4731

A.7.7.9.2.3 Test Requirements 4733

A.7.7.10 RSTD measurements 4733

A.7.7.10.1 RSTD measurement accuracy test case for single positioning frequency layer 4733

A.7.7.10.1.1 Test purpose and Environment 4733

A.7.7.10.1.2 Test Requirements 4734

A.7.7.10.2 RSTD measurement accuracy test case for dual positioning frequency layer 4735

A.7.7.10.2.1 Test purpose and Environment 4735

A.7.7.10.2.2 Test Requirements 4736

A.7.7.10.3 RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR2 in RRC_CONNECTED state 4736

A.7.7.10.3.1 Test purpose and Environment 4736

A.7.7.10.3.2 Test Requirements 4738

A.7.7.10.4 RSTD measurement accuracy test case with Rx TEG 4738

A.7.7.10.4.1 Test purpose and Environment 4738

A.7.7.10.4.2 Test Requirements 4740

A.7.7.10.5 NR RSTD measurement accuracy test case for PRS aggregation in FR2 SA in RRC_CONNECTED mode 4740

A.7.7.10.5.1 Test purpose and Environment 4740

A.7.7.10.5.2 Test Requirements 4742

A.7.7.11 PRS-RSRP measurements 4742

A.7.7.11.1 SA measurement accuracy with PRS in FR2 4742

A.7.7.11.1.1 Test Purpose and Environment 4742

A.7.7.11.1.2 Test parameters 4742

A.7.7.11.1.3 Test Requirements 4744

A.7.7.11.2 SA measurement accuracy with PRS in FR2 with reduced sample number 4744

A.7.7.11.2.1 Test Purpose and Environment 4744

A.7.7.11.2.2 Test parameters 4744

A.7.7.11.2.3 Test Requirements 4746

A.7.7.12 UE Rx-Tx time difference measurements 4746

A.7.7.12.1 UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR2 SA 4746

A.7.7.12.1.1 Test purpose and environment 4746

A.7.7.12.1.2 Test parameters 4747

A.7.7.12.1.3 Test requirements 4748

A.7.7.12.2 UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR2 SA 4748

A.7.7.12.2.1 Test purpose and environment 4749

A.7.7.12.2.2 Test parameters 4749

A.7.7.12.2.3 Test requirements 4750

A.7.7.12.3 UE Rx-Tx time difference measurement accuracy with RxTx TEG 4750

A.7.7.12.3.1 Test purpose and environment 4750

A.7.7.12.3.2 Test parameters 4751

A.7.7.12.3.3 Test requirements 4752

A.7.7.12.4 UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR2 SA 4753

A.7.7.12.4.1 Test purpose and environment 4753

A.7.7.12.4.2 Test requirements 4757

A.7.7.13 PRS-RSRPP measurements 4757

A.7.7.13.1 SA measurement accuracy with PRS in FR2 4757

A.7.7.13.1.1 Test Purpose and Environment 4757

A.7.7.13.1.2 Test parameters 4757

A.7.7.13.1.3 Test Requirements 4759

A.7.7.13.2 SA measurement accuracy with reduced PRS samples in FR2 4759

A.7.7.13.2.1 Test Purpose and Environment 4759

A.7.7.13.2.2 Test parameters 4759

A.7.7.13.2.3 Test Requirements 4761

A.7.7.14 L1-RSRP measurement for group-based beam reporting 4761

A.7.7.14.1 SSB based L1-RSRP measurement 4761

A.7.7.14.1.1 Test Purpose and Environment 4761

A.7.7.14.1.2 Test parameters 4761

A.7.7.14.1.3 Test Requirements 4763

A.7.7.14.2 CSI-RS based L1-RSRP measurement on resource set with repetition off 4763

A.7.7.14.2.1 Test Purpose and Environment 4763

A.7.7.14.2.2 Test parameters 4763

A.7.7.14.2.3 Test Requirements 4765

A.7.7.15 LTM L1-RSRP measurement 4765

A.7.7.15.1 SSB based inter-frequency L1-RSRP measurement 4765

A.7.7.15.1.1 Test Purpose and Environment 4765

A.7.7.15.1.2 Test parameters 4766

A.7.7.15.1.3 Test Requirements 4767

A.7.7.15.2 CSI-RS based L1-RSRP measurement on resource set with repetition off 4768

A.7.7.15.2.1 Test Purpose and Environment 4768

A.7.7.15.2.2 Test parameters 4768

A.7.7.15.2.3 Test Requirements 4770

A.7.7.16 RSCPD Measurements 4770

A.7.7.16.1 RSCPD with RSTD measurement accuracy in FR2 SA in RRC_CONNECTED 4770

A.7.7.16.1.1 Test purpose and environment 4770

A.7.7.16.1.2 Test parameters 4771

A.7.7.16.1.3 Test requirements 4772

A.7.7.17 RSCP with UE Rx-Tx time difference measurements 4772

A.7.7.17.1 RSCP with UE Rx-Tx time difference measurement accuracy in FR2 SA 4772

A.7.7.17.1.1 Test purpose and environment 4772

A.7.7.17.1.2 Test parameters 4773

A.7.7.17.1.3 Test requirements 4776

A.7.7.18 L1 CLI measurements 4776

A.7.7.18.1 SA L1-SRS-RSRP measurement accuracy with FR2 serving cell with SBFD 4776

A.7.7.18.1.1 Test Purpose and Environment 4776

A.7.7.18.1.2 Test parameters 4776

A.7.7.18.1.3 Test Requirements 4778

A.7.7.18.2 L1-CLI-RSSI measurement accuracy in FR2 with SBFD 4778

A.7.7.18.2.1 Test Purpose and Environment 4778

A.7.7.18.2.2 Test parameters 4779

A.7.7.18.2.3 Test Requirements 4780

A.7.8 Measurement procedure in RRC_INACTIVE 4780

A.7.8.1 RSTD measurements 4780

A.7.8.1.1 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state 4780

A.7.8.1.1.1 Test Purpose and Environment 4780

A.7.8.1.1.2 Test Requirements 4783

A.7.8.1.2 NR RSTD measurement reporting delay test case with reduced number of samples in RRC_INACTIVE, FR1 SA 4784

A.7.8.1.2.1 Test Purpose and Environment 4784

A.7.8.1.2.2 Test Requirements 4786

A.7.8.1.3 NR RSTD measurement reporting delay test case for PRS aggregation in FR2 SA in RRC_INACTIVE state 4787

A.7.8.1.3.1 Test purpose and environment 4787

A.7.8.1.3.2 Test requirements 4790

A.7.8.1.4 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state with eDRX > 10.24s 4790

A.7.8.1.4.1 Test purpose and environment 4790

A.7.8.1.4.2 Test requirements 4794

A.7.8.2 PRS-RSRP measurements 4794

A.7.8.2.1 PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_INACTIVE 4794

A.7.8.2.1.1 Test Purpose and Environment 4794

A.7.8.2.1.2 Test Requirements 4796

A.7.8.2.2 PRS-RSRP reporting delay test case with reduced number of samples in RRC_INACTIVE 4797

A.7.8.2.2.1 Test purpose and Environment 4797

A.7.8.2.2.2 Test Requirements 4799

A.7.8.2.3 PRS-RSRP reporting delay in RRC_INACTIVE with eDRX 4799

A.7.8.2.3.1 Test Purpose and Environment 4799

A.7.8.2.3.2 Test Requirements 4803

A.7.8.3 UE Rx-Tx time difference measurements 4803

A.7.8.3.1 UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA 4803

A.7.8.3.1.1 Test purpose and environment 4803

A.7.8.3.1.2 Test requirements 4805

A.7.8.3.2 UE Rx-Tx time difference measurement with reduced number of samples in RRC_INACTIVE, FR2 SA 4805

A.7.8.3.2.1 Test purpose and environment 4805

A.7.8.3.2.2 Test requirements 4807

A.7.8.3.3 UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR2 SA 4807

A.7.8.3.3.1 Test purpose and environment 4807

A.7.8.3.3.2 Test requirements 4810

A.7.8.3.4 UE Rx-Tx time difference measurements for single positioning frequency layer with eDRX > 10.24s in FR2 SA 4810

A.7.8.3.4.1 Test purpose and environment 4810

A.7.8.3.4.2 Test requirements 4813

A.7.8.4 PRS-RSRPP measurements 4813

A.7.8.4.1 PRS-RSRPP reporting delay test case for single positioning frequency layer in FR2 in RRC_INACTIVE state 4813

A.7.8.4.1.1 Test Purpose and Environment 4813

A.7.8.4.1.2 Test Requirements 4816

A.7.8.4.2 PRS-RSRPP reporting delay test with reduced number of samples for single positioning frequency layer in FR2 in RRC_INACTIVE state 4816

A.7.8.4.2.1 Test Purpose and Environment 4816

A.7.8.4.2.2 Test Requirements 4818

A.7.8.4.3 PRS-RSPP reporting delay in RRC_INACTIVE state with eDRX > 10.24s in FR2 4819

A.7.8.4.3.1 Test purpose and environment 4819

A.7.8.4.3.2 Test requirements 4822

A.7.8.5 RSCPD Measurements 4822

A.7.8.5.1 DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state 4822

A.7.8.5.1.1 Test Purpose and Environment 4822

A.7.8.5.1.2 Test Requirements 4823

A.7.8.6 RSCP Measurements 4823

A.7.8.6.1 DL RSCP with UE Rx-Tx time difference measurements in RRC_INACTIVE for single positioning frequency layer in FR2 SA 4823

A.7.8.6.1.1 Test purpose and environment 4823

A.7.8.6.1.2 Test requirements 4827

A.7.9 Measurement performance requirements in RRC_INACTIVE 4827

A.7.9.1 RSTD measurements 4827

A.7.9.1.1 RSTD measurement accuracy test case for single positioning frequency layer in FR2 in RRC_INACTIVE state 4827

A.7.9.1.1.1 Test purpose and Environment 4827

A.7.9.1.1.2 Test Requirements 4829

A.7.9.1.2 RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR2 in RRC_INACTIVE state 4829

A.7.9.1.2.1 Test purpose and Environment 4829

A.7.9.1.2.2 Test Requirements 4831

A.7.9.2 PRS-RSRP measurements 4833

A.7.9.2.1 SA measurement accuracy with PRS in FR2 in RRC_INACTIVE 4833

A.7.9.2.1.1 Test Purpose and Environment 4833

A.7.9.2.1.2 Test parameters 4833

A.7.9.2.1.3 Test Requirements 4834

A.7.9.2.2 PRS-RSRP measurements with reduced number of sample in RRC_INACTIVE 4835

A.7.9.2.2.1 Test Purpose and Environment 4835

A.7.9.2.2.2 Test parameters 4835

A.7.9.2.2.3 Test Requirements 4836

A.7.9.3 UE Rx-Tx time difference measurements 4837

A.7.9.3.1 UE Rx-Tx time difference measurements in RRC_INACTIVE 4837

A.7.9.3.1.1 Test purpose and environment 4837

A.7.9.3.1.2 Test parameters 4837

A.7.9.3.1.3 Test requirements 4838

A.7.9.3.2 UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR2 SA 4838

A.7.9.3.2.1 Test purpose and environment 4838

A.7.9.3.2.2 Test parameters 4839

A.7.9.3.2.3 Test requirements 4840

A.7.9.3.3 UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR2 SA in RRC_INACTIVE state 4840

A.7.9.3.3.1 Test purpose and environment 4840

A.7.9.3.3.2 Test requirements 4844

A.7.9.4 PRS-RSRPP measurements 4844

A.7.9.4.1 SA measurement accuracy in FR2 in RRC INACTIVE 4844

A.7.9.4.1.1 Test Purpose and Environment 4844

A.7.9.4.1.2 Test parameters 4844

A.7.9.4.1.3 Test Requirements 4846

A.7.9.4.2 SA measurement accuracy with reduced PRS samples in FR2 in RRC INACTIVE 4846

A.7.9.4.2.1 Test Purpose and Environment 4846

A.7.9.4.2.2 Test parameters 4846

A.7.9.4.2.3 Test Requirements 4848

A.7.9.5 RSCPD Measurements 4848

A.7.9.5.1 RSCPD with RSTD measurement accuracy in FR2 SA in RRC_INACTIVE 4848

A.7.9.5.1.1 Test purpose and environment 4848

A.7.9.5.1.2 Test parameters 4848

A.7.9.5.1.3 Test requirements 4850

A.7.9.6 RSCP Measurements 4850

A.7.9.6.1 RSCP with UE Rx-Tx time difference measurement accuracy in FR2 SA 4850

A.7.9.6.1.1 Test purpose and environment 4850

A.7.9.6.1.2 Test parameters 4851

A.7.9.6.1.3 Test requirements 4852

A.7.10 Measurement Procedure in RRC_IDLE 4852

A.7.10.1 RSTD Measurements 4852

A.7.10.1.1 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_IDLE state for non-RedCap UE 4852

A.7.10.1.1.1 Test purpose and environment 4852

A.7.10.1.1.2 Test requirements 4855

A.7.10.1.2 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s 4855

A.7.10.1.2.1 Test purpose and environment 4855

A.7.10.1.2.2 Test requirements 4858

A.7.10.1.3 NR RSTD measurement reporting delay test case for PRS aggregation in FR2 SA in RRC_IDLE state 4858

A.7.10.1.3.1 Test purpose and environment 4858

A.7.10.1.3.2 Test requirements 4859

A.7.10.2 PRS-RSRP Measurements 4859

A.7.10.2.1 PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_IDLE state for non-RedCap UE in FR2 4859

A.7.10.2.1.1 Test Purpose and Environment 4859

A.7.10.2.1.2 Test Requirements 4863

A.7.10.2.2 PRS-RSRP reporting delay test case in RRC_IDLE state in FR2 when eDRX cycle > 10.24s 4863

A.7.10.2.2.1 Test Purpose and Environment 4863

A.7.10.2.2.2 Test Requirements 4863

A.7.10.3 RSCPD Measurements 4864

A.7.10.3.1 DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_IDLE state 4864

A.7.10.3.1.1 Test Purpose and Environment 4864

A.7.10.3.1.2 Test Requirements 4864

A.7.11 Measurement Performance Requirements in RRC_IDLE 4865

A.7.11.1 RSTD Measurements 4865

A.7.11.1.1 NR RSTD measurement accuracy test case for single positioning frequency layer in FR2 SA in RRC_IDLE state for non-RedCap UE 4865

A.7.11.1.1.1 Test purpose and environment 4865

A.7.11.1.1.2 Test requirements 4866

A.7.11.1.2 RSTD measurement accuracy test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s 4867

A.7.11.1.2.1 Test purpose and environment 4867

A.7.11.1.2.2 Test requirements 4868

A.7.11.1.3 NR RSTD measurement accuracy test case for PRS aggregation in FR2 SA in RRC_IDLE state 4869

A.7.11.1.3.1 Test purpose and environment 4869

A.7.11.1.3.2 Test requirements 4869

A.7.11.2 PRS-RSRP measurements 4869

A.7.11.2.1 PRS-RSRP measurement accuracy test case for non-RedCap UE in FR2 in RRC_IDLE state 4869

A.7.11.2.1.1 Test Purpose and Environment 4869

A.7.11.2.1.2 Test parameters 4869

A.7.11.2.1.3 Test Requirements 4871

A.7.11.2.2 PRS-RSRP measurement accuracy test case in RRC_IDLE state in FR2 for case 2 when eDRX cycle > 10.24s 4871

A.7.11.2.2.1 Test purpose and Environment 4871

A.7.11.2.2.1 Test parameters 4872

A.7.11.2.2.2 Test Requirements 4872

A.7.11.3 RSCPD measurements 4872

A.7.11.3.1 RSCPD with RSTD measurement accuracy in FR2 SA in RRC_IDLE 4872

A.7.11.3.1.1 Test purpose and environment 4872

A.7.11.3.1.2 Test parameters 4872

A.7.11.3.1.3 Test requirements 4874

A.8 E-UTRA standalone tests for NR RRM 4875

A.8.1 Void 4875

A.8.2 RRC_IDLE state mobility 4875

A.8.2.1 Inter-RAT NR Cell re-selection 4875

A.8.2.1.1 E-UTRA Cell reselection to higher priority NR target Cell in FR1 4875

A.8.2.1.1.1 Test Purpose and Environment 4875

A.8.2.1.1.2 Test Requirements 4878

A.8.2.1.2 E-UTRA Cell reselection to lower priority NR target Cell in FR1 for UE configured with highSpeedInterRAT-NR-r16 4878

A.8.2.1.2.1 Test Purpose and Environment 4878

A.8.2.1.2.2 Test Requirements 4881

A.8.2.2 E-UTRA – NR Inter-RAT Early Measruement Reporting 4882

A.8.2.2.1 E-UTRA – NR Early Measurement Reporting for NR in FR1 4882

A.8.2.2.1.1 Test Purpose and Environment 4882

A.8.2.2.1.2 Test Requirements 4884

A.8.2.2.2 E-UTRA – NR Early Measurement Reporting for NR in FR2 4885

A.8.2.2.2.1 Test Purpose and Environment 4885

A.8.2.2.2.2 Test Requirements 4887

A.8.3 RRC_CONNECTED state mobility 4887

A.8.3.1 Handover 4887

A.8.3.1.1 E-UTRAN - NR handover in FR1 4887

A.8.3.1.1.1 Test Purpose and Environment 4887

A.8.3.1.1.2 Test Requirements 4891

A.8.4 Measurement procedure 4891

A.8.4.1 E-UTRA – NR Inter-RAT SFTD Measurement Delay 4891

A.8.4.1.1 E-UTRA – NR Inter-RAT SFTD Measurement Delay in non-DRX 4891

A.8.4.1.1.1 Test Purpose and Environment 4891

A.8.4.1.1.2 Test Requirements 4893

A.8.4.1.2 E-UTRA – NR Inter-RAT SFTD Measurement Delay in DRX 4893

A.8.4.1.2.1 Test Purpose and Environment 4893

A.8.4.1.2.2 Test Requirements 4894

A.8.4.2 E-UTRA – NR Inter-RAT Measurements 4894

A.8.4.2.1 NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used 4894

A.8.4.2.1.1 Test Purpose and Environment 4894

A.8.4.2.1.2 Test Requirements 4897

A.8.4.2.2 NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used 4897

A.8.4.2.2.1 Test Purpose and Environment 4897

A.8.4.2.2.2 Test Requirements 4900

A.8.4.2.3 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used 4901

A.8.4.2.3.1 Test Purpose and Environment 4901

A.8.4.2.3.2 Test Requirements 4904

A.8.4.2.4 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used 4904

A.8.4.2.4.1 Test Purpose and Environment 4904

A.8.4.2.4.2 Test Requirements 4907

A.8.4.2.5 NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is not used 4907

A.8.4.2.5.1 Test Purpose and Environment 4907

A.8.4.2.5.2 Test Requirements 4909

A.8.4.2.6 NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is used 4910

A.8.4.2.6.1 Test Purpose and Environment 4910

A.8.4.2.6.2 Test Requirements 4911

A.8.4.2.7 NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is not used 4912

A.8.4.2.7.1 Test Purpose and Environment 4912

A.8.4.2.7.2 Test Requirements 4914

A.8.4.2.8 NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is used 4914

A.8.4.2.8.1 Test Purpose and Environment 4914

A.8.4.2.8.2 Test Requirements 4916

A.8.4.2.9 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection in DRX for UE configured with highSpeedInterRAT-NR-r16 4916

A.8.4.2.9.1 Test Purpose and Environment 4916

A.8.4.2.9.2 Test Requirements 4919

A.8.4.3 E-UTRAN - NR Inter-RAT event-triggered without measurement gaps 4920

A.8.4.3.1 NR Inter-RAT event triggered reporting tests for FR2 without MG nor DRX 4920

A.8.4.3.1.1 Test Purpose and Environment 4920

A.8.4.3.1.2 Test Requirements 4921

A.8.4.3.2 NR Inter-RAT event triggered reporting tests for FR1 without gaps when DRX is not used 4922

A.8.4.3.2.1 Test Purpose and Environment 4922

A.8.4.3.2.2 Test Requirements 4925

A.8.5 Measurement performance 4925

A.8.5.1 SFTD accuracy 4925

A.8.5.1.1 SFTD accuracy 4925

A.8.5.1.1.1 Test Purpose 4925

A.8.5.1.1.2 Test Environment 4925

A.8.5.1.1.3 Test Requirements 4929

A.8.5.2 E-UTRA – NR Inter-RAT Measurement Performance requirements 4929

A.8.5.2.1.1 E-UTRAN – NR inter-RAT measurements with FR1 target cell 4929

A.8.5.2.1.2 E-UTRAN – NR inter-RAT measurements with FR2 target cell 4932

A.8.5.2.1.2.1 Test Purpose and Environment 4932

A.8.5.2.1.2.2 Test Parameters 4932

A.8.5.2.1.2.3 Test Requirements 4934

A.8.5.2.2 SS-RSRQ 4934

A.8.5.2.2.1 E-UTRAN – NR inter-RAT measurements with FR1 target cell 4934

A.8.5.2.2.2 E-UTRAN – NR inter-RAT measurements with FR2 target cell 4937

A.8.5.2.2.2.1 Test Purpose and Environment 4937

A.8.5.2.2.2.2 Test Parameters 4937

A.8.5.2.2.2.3 Test Requirements 4939

A.8.5.2.3 SS-SINR 4939

A.8.5.2.3.1 E-UTRAN – NR inter-RAT measurements with FR1 target cell 4939

A.8.5.2.3.2 E-UTRAN – NR inter-RAT measurements with FR2 target cell 4942

A.8.5.2.3.2.1 Test Purpose and Environment 4942

A.8.5.2.3.2.2 Test Parameters 4943

A.8.5.2.3.2.3 Test Requirements 4944

A.9 V2X Tests 4944

A.9.1 V2X Tests in FR1 4944

A.9.1.1 Test for V2X UE Transmit Timing 4944

A.9.1.1.1 Test for GNSS as Synchronization Reference Source 4944

A.9.1.1.1.1 Test Purpose and Environment 4944

A.9.1.1.1.2 Test requirements 4945

A.9.1.1.2 Test for SyncRef UE as Synchronization Reference Source 4945

A.9.1.1.2.1 Test Purpose and Environment 4945

A.9.1.1.2.2 Test requirements 4945

A.9.1.1.3 Test for FR1 NR Cell as Synchronization Reference Source 4945

A.9.1.1.3.1 Test Purpose and Environment 4946

A.9.1.1.3.2 Test requirements 4947

A.9.1.2 Test for Initiation/Cease of S-SSB Transmission with V2X Sidelink Communication 4947

A.9.1.2.1 Test for FR1 NR Cell as synchronization reference source without gap under non-DRX 4947

A.9.1.2.1.1 Test Purpose and Environment 4947

A.9.1.2.1.2 Test Requirements 4949

A.9.1.2.2 Test for SyncRef UE as synchronization reference source 4949

A.9.1.2.2.1 Test Purpose and Environment 4949

A.9.1.2.2.2 Test Requirements 4951

A.9.1.2.3 Test for SyncRef UE as synchronization reference source when SL-DRX is used 4951

A.9.1.2.3.1 Test Purpose and Environment 4951

A.9.1.2.3.2 Test Requirements 4953

A.9.1.2.4 Test for SyncRef UE as synchronization reference source with CCA 4953

A.9.1.2.4.1 Test Purpose and Environment 4953

A.9.1.2.4.2 Test Requirements 4954

A.9.1.3  Test for V2X Synchronization Reference Selection/Reselection 4955

A.9.1.3.1  Test for GNSS configured as the highest priority 4955

A.9.1.3.1.1 Test Purpose and Environment 4955

A.9.1.3.1.2 Test Requirements 4956

A.9.1.3.2  Test for FR1 NR Cell configured as the highest priority 4957

A.9.1.3.2.1 Test Purpose and Environment 4957

A.9.1.3.2.2 Test Requirements 4959

A.9.1.3.3 Test for GNSS configured as the highest priority under SL-DRX 4960

A.9.1.3.3.1 Test Purpose and Environment 4960

A.9.1.3.3.2 Test Requirements 4961

A.9.1.3.4 Test for FR1 NR Cell configured as the highest priority under SL-DRX 4962

A.9.1.3.4.1 Test Purpose and Environment 4962

A.9.1.3.4.2 Test Requirements 4964

A.9.1.4 Test for L1 SL-RSRP Measurement 4964

A.9.1.4.1 Test for V2X UE Autonomous Resource Selection/Reselection 4964

A.9.1.4.1.1 Test Purpose and Environment 4964

A.9.1.4.1.2 Test Requirements 4966

A.9.1.4.2 Test for V2X UE Resource Pre-emption 4967

A.9.1.4.2.1 Test Purpose and Environment 4967

A.9.1.4.2.2 Test Requirements 4968

A.9.1.4.3  Test for V2X UE Resource Re-evaluation 4969

A.9.1.4.3.1 Test Purpose and Environment 4969

A.9.1.4.3.2 Test Requirements 4972

A.9.1.4.4 Test for V2X UE Autonomous Resource Selection/Reselection with Periodic Sensing 4972

A.9.1.4.4.1 Test Purpose and Environment 4972

A.9.1.4.4.2 Test Requirements 4974

A.9.1.4.5 Test for V2X UE Autonomous Resource Selection/Reselection with Contiguous Sensing 4974

A.9.1.4.5.1 Test Purpose and Environment 4974

A.9.1.4.5.2 Test Requirements 4976

A.9.1.4.6 Test for V2X UE Autonomous Resource Selection/Reselection in SL-DRX 4977

A.9.1.4.6.1 Test Purpose and Environment 4977

A.9.1.4.6.2 Test Requirements 4979

A.9.1.5 Test for Congestion Control Measurement 4979

A.9.1.5.1 Test Purpose and Environment 4979

A.9.1.5.2 Test Requirements 4982

A.9.1.6 Test for Interruption 4982

A.9.1.6.1 Test for Interruption to WAN due to V2X Sidelink Communication 4982

A.9.1.6.1.1 Test Purpose and Environment 4982

A.9.1.6.1.2 Test Requirements 4985

A.9.1.6.2 Test for interruption to WAN at transitions between active and non-active during SL-DRX in asynchronous case 4985

A.9.1.6.2.1 Test Purpose and Environment 4985

A.9.1.6.2.2 Test Requirements 4987

A.9.1.6.3 Test for Interruption at NR Sidelink Diccovery Configuration 4987

A.9.1.6.3.1 Test Purpose and Environment 4987

A.9.1.6.3.2 Test Requirements 4990

A.9.1.7 Selection / Reselection of relay UE 4990

A.9.1.7.1 Test Purpose and Environment 4990

A.9.1.7.2 Test Requirements 4994

A.9A Tests for NR Sidelink Measurements for Positioning 4995

A.9A.1 Tests for NR Sidelink Measurements for Positioning in FR1 4995

A.9A.1.1 Measurement delay tests 4995

A.9A.1.1.1 NR SL RSTD measurement reporting delay test case in FR1 SA 4995

A.9A.1.1.1.1 Test Purpose and Environment 4995

A.9A.1.1.1.2 Test Requirements 5000

A.9A.1.1.2 SL Rx-Tx measurement delay tests 5000

A.9A.1.1.2.1 Test Purpose and Environment 5000

A.9A.1.1.2.2 Test Requirements 5003

A.9A.1.1.3 NR SL AoA measurements reporting delay test in FR1 SA 5004

A.9A.1.1.3.1 Test Purpose and Environment 5004

A.9A.1.1.3.2 Test Requirements 5007

A.9A.1.1.4 NR SL RTOA measurements reporting delay test in FR1 SA 5008

A.9A.1.1.4.1 Test Purpose and Environment 5008

A.9A.1.1.4.2 Test Requirements 5011

A.9A.1.1.5 NR SL PRS-RSRP measurement reporting delay test case in FR1 SA 5012

A.9A.1.1.5.1 Test Purpose and Environment 5012

A.9A.1.1.5.2 Test Requirements 5012

A.9A.1.1.6 NR SL PRS-RSRPP measurement reporting delay test case in FR1 SA 5012

A.9A.1.1.6.1 Test Purpose and Environment 5012

A.9A.1.1.6.2 Test Requirements 5012

A.9A.1.2 Measurement Accuracy Tests 5013

A.9A.1.2.1 NR SL RSTD measurement accuracy test case in FR1 SA 5013

A.9A.1.2.1.1 Test Purpose and Environment 5013

A.9A.1.2.1.2 Test Requirements 5016

A.9A.1.2.2 SL Rx-Tx measurement accuracy test case in FR1 5017

A.9A.1.2.2.1 Test Purpose and Environment 5017

A.9A.1.2.2.2 Test Requirements 5020

A.9A.1.2.3 NR SL PRS-RSRP measurement accuracy test case in FR1 SA 5020

A.9A.1.2.3.1 Test Purpose and Environment 5020

A.9A.1.2.3.2 Test Requirements 5021

A.9A.1.2.4 NR SL PRS-RSRPP measurement accuracy test case in FR1 SA 5021

A.9A.1.2.4.1 Test Purpose and Environment 5021

A.9A.1.2.4.2 Test Requirements 5021

A.10 EN-DC Tests with NR PSCell under CCA and Other NR Cells in FR1 5022

A.10.1 RRC_CONNECTED state mobility 5022

A.10.1.1 RRC connection mobility control 5022

A.10.1.1.1 Random Access 5022

A.10.1.1.1.1 4-step RA type contention-based random access for NR PSCell with CCA 5022

A.10.1.1.1.1.1 Test Purpose and Environment 5022

A.10.1.1.1.1.2 Test Requirements 5023

A.10.1.1.1.1.2.1 Random Access Preamble Transmission 5024

A.10.1.1.1.1.2.2 Random Access Response Reception 5024

A.10.1.1.1.1.2.3 No Random Access Response Reception 5024

A.10.1.1.1.1.2.4 Receiving an UL grant for msg3 retransmission 5025

A.10.1.1.1.1.2.5  Contention Resolution Timer expiry 5025

A.10.1.1.1.2 4-step RA type non-contention based random access for NR PSCell with CCA 5025

A.10.1.1.1.2.1 Test Purpose and Environment 5025

A.10.1.1.1.2.2 Test Requirements 5026

A.10.1.1.1.2.2.1 SSB-based Random Access Preamble Transmission 5027

A.10.1.1.1.2.2.2 Random Access Response Reception 5027

A.10.1.1.1.2.2.3 No Random Access Response Reception 5027

A.10.1.1.1.3 2-step RA type contention-based random access for NR PSCell with CCA 5028

A.10.1.1.1.3.1 Test Purpose and Environment 5028

A.10.1.1.1.3.2 Test Requirements 5029

A.10.1.1.1.3.2.1 MsgA Transmission 5030

A.10.1.1.1.3.2.2 MsgB Reception 5030

A.10.1.1.1.3.2.3 No MsgB Reception 5030

A.10.1.1.1.4 2-step RA type non-contention based random access for NR PSCell with CCA 5031

A.10.1.1.1.4.1 Test Purpose and Environment 5031

A.10.1.1.1.4.2 Test Requirements 5032

A.10.1.1.1.4.2.1 MsgA Transmission 5033

A.10.1.1.1.4.2.2 MsgB Reception 5033

A.10.1.1.1.4.2.3 No MsgB Reception 5033

A.10.1.2 Handover with PSCell from EN-DC to EN-DC with known target PSCell using CCA 5034

A.10.1.2.1 Test Purpose and Environment 5034

A.10.1.2.2 Test Requirements 5038

A.10.2 Timing 5039

A.10.2.1 UE transmit timing 5039

A.10.2.1.1 UE Transmit Timing Test with PSCell under DL CCA 5039

A.10.2.1.1.1 Test Purpose and environment 5039

A.10.2.1.1.2 Test requirements 5041

A.10.2.2 UE timing advance 5042

A.10.2.2.1 UE Timing Advance Adjustment Accuracy with PSCell under DL CCA 5042

A.10.2.2.1.1 Test Purpose and Environment 5042

A.10.2.2.1.2 Test Parameters 5042

A.10.2.2.1.3 Test Requirements 5044

A.10.3 Signalling characteristics 5044

A.10.3.1 Radio link monitoring 5044

A.10.3.1.1 Introduction 5044

A.10.3.1.2 Radio link monitoring out-of-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode 5045

A.10.3.1.2.1 Test purpose and environment 5045

A.10.3.1.2.2 Test requirements 5047

A.10.3.1.3 Radio link monitoring in-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode 5048

A.10.3.1.3.1 Test purpose and environment 5048

A.10.3.1.3.2 Test requirements 5050

A.10.3.1.4 Void 5050

A.10.3.1.4.1 Void 5050

A.10.3.1.4.2 Void 5050

A.10.3.1.5 Void 5051

A.10.3.1.5.1 Void 5051

A.10.3.1.5.2 Void 5051

A.10.3.2 Void 5051

A.10.3.3 SCell activation and deactivation delay 5051

A.10.3.3.1 SCell Activation and Deactivation of known NR SCell with NR PSCell and NR SCell under CCA, 160 ms SCell measurement cycle 5051

A.10.3.3.1.1 Test Purpose and Environment 5051

A.10.3.3.1.2 Test Requirements 5054

A.10.3.3.2 SCell Activation and Deactivation of known NR SCell with NR PSCell and NR SCell under CCA, 640 ms SCell measurement cycle 5054

A.10.3.3.2.1 Test Purpose and Environment 5054

A.10.3.3.2.2 Test Requirements 5055

A.10.3.3.3 SCell Activation and Deactivation of unknown NR SCell with NR PSCell and NR SCell under CCA 5055

A.10.3.3.3.1 Test Purpose and Environment 5055

A.10.3.3.3.2 Test Requirements 5055

A.10.3.4 Beam failure detection and link recovery procedures 5056

A.10.3.4.1 EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode 5056

A.10.3.4.1.1 Test Purpose and Environment 5056

A.10.3.4.1.2 Test Requirements 5059

A.10.3.4.2 EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in DRX mode 5059

A.10.3.4.2.1 Test Purpose and Environment 5059

A.10.3.4.2.2 Test Requirements 5062

A.10.3.5 Active BWP switching 5063

A.10.3.5.1 UL active BWP switch delay with consistent UL LBT failure on PSCell subject to UL CCA in EN-DC 5063

A.10.3.5.1.2 Test Requirements 5065

A.10.3.5.2 DCI-based and Timer-based Active BWP Switch 5066

A.10.3.5.2.1 E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC 5066

A.10.3.5.2.2 E-UTRAN – NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC 5069

A.10.3.5.3 RRC-based Active BWP Switch 5073

A.10.3.5.3.1 E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC 5073

A.10.3.6 PSCell addition and release delay 5075

A.10.3.6.1 Addition and Release Delay of known NR PSCell on the carrier under CCA 5075

A.10.3.6.1.1 Test purpose and environment 5075

A.10.3.6.1.2 Test Requirements 5078

A.10.3.7 Void 5078

A.10.4 Measurement procedure 5078

A.10.4.1 Intra-frequency measurements 5079

A.10.4.1.1 Event-triggered reporting tests on PSCC without gaps under non-DRX 5079

A.10.4.1.1.1 Test purpose and environment 5079

A.10.4.1.1.2 Test parameters 5079

A.10.4.1.1.3 Test Requirements 5081

A.10.4.1.2 Void 5081

A.10.4.1.3 Void 5081

A.10.4.1.4 Event-triggered reporting tests on PSCC with per-UE gaps under DRX 5081

A.10.4.1.4.1 Test purpose and environment 5081

A.10.4.1.4.2 Test parameters 5081

A.10.4.1.4.3 Test Requirements 5084

A.10.4.1.5 Void 5084

A.10.4.1.6 Void 5084

A.10.4.1.7 Void 5084

A.10.4.1.8 Void 5084

A.10.4.1.9 Void 5084

A.10.4.1.10 Void 5084

A.10.4.1.11 Void 5084

A.10.4.1.12 Void 5084

A.10.4.2 Inter-frequency measurements 5084

A.10.4.2.1 Void 5084

A.10.4.2.2 Void 5084

A.10.4.2.3 EN-DC event triggered reporting tests for FR1 with CCA cell without SSB time index detection when DRX is not used 5085

A.10.4.2.3.1 Test Purpose and Environment 5085

A.10.4.2.3.2 Test Requirements 5087

A.10.4.2.4 EN-DC event triggered reporting tests for FR1 cell with CCA without SSB time index detection when DRX is used 5087

A.10.4.2.4.1 Test Purpose and Environment 5087

A.10.4.2.4.2 Test Requirements 5090

A.10.4.2.5 EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is not used 5091

A.10.4.2.5.1 Test Purpose and Environment 5091

A.10.4.2.5.2 Test Requirements 5093

A.10.4.2.6 EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is used 5093

A.10.4.2.6.1 Test Purpose and Environment 5093

A.10.4.2.6.2 Test Requirements 5096

A.10.4.2.7 EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is not used 5097

A.10.4.2.7.1 Test Purpose and Environment 5097

A.10.4.2.7.2 Test Requirements 5100

A.10.4.2.8 EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used 5100

A.10.4.2.8.1 Test Purpose and Environment 5100

A.10.4.2.8.2 Test Requirements 5104

A.10.4.2.9 EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is not used 5105

A.10.4.2.9.1 Test Purpose and Environment 5105

A.10.4.2.9.2 Test Requirements 5108

A.10.4.2.10 EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is used 5108

A.10.4.2.10.1 Test Purpose and Environment 5108

A.10.4.2.10.2 Test Requirements 5112

A.10.4.3 L1-RSRP measurements for beam reporting 5113

A.10.4.3.1 SSB based L1-RSRP measurement on PSCC when DRX is not used 5113

A.10.4.3.1.1 Test Purpose and Environment 5113

A.10.4.3.1.2 Test parameters 5113

A.10.4.3.1.3 Test Requirements 5114

A.10.4.3.2 SSB based L1-RSRP measurement on PSCC when DRX is used 5115

A.10.4.3.2.1 Test Purpose and Environment 5115

A.10.4.3.2.2 Test parameters 5115

A.10.4.3.2.3 Test Requirements 5116

A.10.4.3.3 SSB based L1-RSRP measurement on SCC when DRX is not used 5117

A.10.4.3.3.1 Test Purpose and Environment 5117

A.10.4.3.3.2 Test parameters 5117

A.10.4.3.3.3 Test Requirements 5118

A.10.4.3.4 SSB based L1-RSRP measurement on SCC when DRX is used 5119

A.10.4.3.4.1 Test Purpose and Environment 5119

A.10.4.3.4.2 Test parameters 5119

A.10.4.3.4.3 Test Requirements 5120

A.10.4.4 E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA 5121

A.10.4.4.1 E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used 5121

A.10.4.4.1.1 Test Purpose and Environment 5121

A.10.4.4.1.2 Test Requirements 5124

A.10.4.4.2 E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used 5125

A.10.4.4.2.1 Test Purpose and Environment 5125

A.10.4.4.2.2 Test Requirements 5128

A.10.4.4.3 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used 5129

A.10.4.4.3.1 Test Purpose and Environment 5129

A.10.4.4.3.2 Test Requirements 5132

A.10.4.4.4 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used 5132

A.10.4.4.4.1 Test Purpose and Environment 5132

A.10.4.4.4.2 Test Requirements 5136

A.10.5 Measurement performance 5136

A.10.5.1 SS-RSRP 5136

A.10.5.1.1 Intra-frequency measurement accuracy on a CCA serving cell 5136

A.10.5.1.1.1 Test Purpose and Environment 5136

A.10.5.1.1.2 Test parameters 5137

A.10.5.1.1.3 Test Requirements 5138

A.10.5.1.2 Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell 5138

A.10.5.1.2.1 Test Purpose and Environment 5138

A.10.5.1.2.2 Test parameters 5139

A.10.5.1.2.3 Test Requirements 5140

A.10.5.2 SS-RSRQ 5140

A.10.5.2.1 Intra-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell 5140

A.10.5.2.1.1 Test Purpose and Environment 5140

A.10.5.2.1.2 Test Parameters 5140

A.10.5.2.1.3 Test Requirements 5142

A.10.5.2.2 Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell 5142

A.10.5.2.2.1 Test Purpose and Environment 5142

A.10.5.2.2.2 Test Parameters 5142

A.10.5.2.2.3 Test Requirements 5144

A.10.5.3 SS-SINR 5144

A.10.5.3.1 Intra-frequency measurement accuracy on PSCC 5144

A.10.5.3.1.1 Test Purpose and Environment 5144

A.10.5.3.1.2 Test Parameters 5144

A.10.5.3.1.3 Test Requirements 5145

A.10.5.3.2 Inter-frequency measurement accuracy on PSCC 5146

A.10.5.3.2.1 Test Purpose and Environment 5146

A.10.5.3.2.2 Test Parameters 5146

A.10.5.3.2.3 Test Requirements 5147

A.10.5.3.3 Intra-frequency measurement accuracy on SCC 5147

A.10.5.3.3.1 Test Purpose and Environment 5147

A.10.5.3.3.2 Test Parameters 5147

A.10.5.3.3.3 Test Requirements 5149

A.10.5.4 L1-RSRP measurement for beam reporting with CCA serving cell 5149

A.10.5.4.1 SSB based L1-RSRP measurement 5149

A.10.5.4.1.1 Test Purpose and Environment 5149

A.10.5.4.1.2 Test parameters 5150

A.10.5.4.1.3 Test Requirements 5151

A.10.5.5 RSSI 5151

A.10.5.5.1  RSSI measurement accuracy on PSCC with CCA 5151

A.10.5.5.1.1 Test Purpose and Environment 5151

A.10.5.5.1.2 Test parameters 5151

A.10.5.5.1.3 Test Requirements 5153

A.10.5.5.2 RSSI measurement accuracy on SCC with CCA 5153

A.10.5.5.2.1 Test Purpose and Environment 5153

A.10.5.5.2.2 Test parameters 5153

A.10.5.5.2.3 Test Requirements 5154

A.10.5.5.3  Inter-frequency RSSI measurement accuracy on a carrier with CCA 5154

A.10.5.5.3.1 Test Purpose and Environment 5154

A.10.5.5.3.2 Test parameters 5155

A.10.5.5.3.3 Test Requirements 5156

A.10.5.6 Channel occupancy 5156

A.10.5.6.1  Channel occupancy measurement accuracy on PSCC with CCA 5156

A.10.5.6.1.1 Test Purpose and Environment 5156

A.10.5.6.1.2 Test parameters 5156

A.10.5.6.1.3 Test Requirements 5158

A.10.5.6.2  Channel occupancy measurement accuracy on SCC with CCA 5158

A.10.5.6.2.1 Test Purpose and Environment 5158

A.10.5.6.2.2 Test parameters 5158

A.10.5.6.2.3 Test Requirements 5160

A.10.5.6.3  Inter-frequency channel occupancy measurement accuracy on a carrier with CCA 5160

A.10.5.6.3.1 Test Purpose and Environment 5160

A.10.5.6.3.2 Test parameters 5160

A.10.5.6.3.3 Test Requirements 5162

A.11 NR Standalone Tests with NR PCell under CCA and Other NR Cells in FR1 5163

A.11.1 RRC_IDLE state mobility 5163

A.11.1.1 Cell re-selection with both source and target NR carrier frequencies under CCA 5163

A.11.1.1.1 Cell reselection to FR1 intra-frequency NR cells when subject to CCA on the serving and target cell 5163

A.11.1.1.1.1 Test Purpose and Environment 5163

A.11.1.1.1.2 Test Parameters 5163

A.11.1.1.1.3 Test Requirements 5165

A.11.1.1.2 Cell reselection to FR1 inter-frequency NR case when subject to CCA on the serving and target cell 5166

A.11.1.1.2.1 Test Purpose and Environment 5166

A.11.1.1.2.2 Test Parameters 5166

A.11.1.1.2.3 Test Requirements 5168

A.11.1.2 Cell re-selection to NR with source NR carrier frequency under CCA 5168

A.11.1.2.1 Cell reselection to FR1 inter-frequency NR case when serving cell is subject to CCA 5168

A.11.1.2.1.1 Test Purpose and Environment 5168

A.11.1.2.1.2 Test Parameters 5169

A.11.1.2.1.3 Test Requirements 5171

A.11.1.3 Cell re-selection from NR carrier with target NR carrier frequency under CCA 5172

A.11.1.3.1 Cell reselection to FR1 inter-frequency NR case when target cell is subject to CCA 5172

A.11.1.3.1.1 Test Purpose and Environment 5172

A.11.1.3.1.2 Test Parameters 5172

A.11.1.3.1.3 Test Requirements 5175

A.11.1.4 Inter-RAT cell re-selection to E-UTRAN with source NR carrier frequency under CCA 5176

A.11.1.4.1 Cell reselection to higher priority E-UTRAN when serving cell is subject to CCA 5176

A.11.1.4.1.1 Test Purpose and Environment 5176

A.11.1.4.1.2 Test Parameters 5176

A.11.1.4.1.3 Test Requirements 5179

A.11.1.4.2 Cell reselection to lower priority E-UTRAN when serving cell is subject to CCA 5179

A.11.1.4.2.1 Test Purpose and Environment 5179

A.11.1.4.2.2 Test Requirements 5181

A.11.2 RRC_CONNECTED state mobility 5182

A.11.2.1 Handover 5182

A.11.2.1.1 Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; known target cell 5182

A.11.2.1.1.1 Test Purpose and Environment 5182

A.11.2.1.1.2 Test Parameters 5182

A.11.2.1.1.3 Test Requirements 5184

A.11.2.1.2 Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell 5185

A.11.2.1.2.1 Test Purpose and Environment 5185

A.11.2.1.2.2 Test Parameters 5185

A.11.2.1.2.3 Test Requirements 5187

A.11.2.1.3 Inter-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell 5187

A.11.2.1.3.1 Test Purpose and Environment 5187

A.11.2.1.3.2 Test Parameters 5187

A.11.2.1.3.3 Test Requirements 5189

A.11.2.1.4 Inter-frequency handover from FR1 carrier under CCA to FR1; known target cell 5190

A.11.2.1.4.1 Test Purpose and Environment 5190

A.11.2.1.4.2 Test Parameters 5190

A.11.2.1.4.3 Test Requirements 5193

A.11.2.1.5 Inter-frequency handover from FR1 carrier under CCA to FR1; unknown target cell 5193

A.11.2.1.5.1 Test Purpose and Environment 5193

A.11.2.1.5.2 Test Parameters 5193

A.11.2.1.5.3 Test Requirements 5196

A.11.2.1.6 Inter-frequency handover from FR1 to FR1 carrier under CCA; unknown target cell 5196

A.11.2.1.6.1 Test Purpose and Environment 5196

A.11.2.1.6.2 Test Parameters 5196

A.11.2.1.6.3 Test Requirements 5199

A.11.2.1.7  SA NR FR1 carrier under CCA - E-UTRAN handover with known target cell 5199

A.11.2.1.7.1 Test Purpose and Environment 5199

A.11.2.1.7.2 Test Requirements 5202

A.11.2.1.8 SA NR FR1 carrier under CCA - E-UTRAN handover with unknown target cell 5203

A.11.2.1.8.1 Test Purpose and Environment 5203

A.11.2.1.8.2 Test Requirements 5206

A.11.2.1.9 Handover with PSCell from NR SA to EN-DC with known target PSCell using CCA 5206

A.11.2.1.9.1 Test Purpose and Environment 5206

A.11.2.1.9.2 Test Requirements 5212

A.11.2.2 RRC connection mobility control 5213

A.11.2.2.1 RRC re-establishment 5213

A.11.2.2.1.1 Intra-frequency RRC Re-establishment with CCA in FR1 5213

A.11.2.2.1.2 Inter-frequency RRC Re-establishment with CCA in FR1 5216

A.11.2.2.1.4 Inter-frequency RRC Re-establishment from NR FR1 carrier without CCA to NR FR1 carrier under CCA 5222

A.11.2.2.2 Random Access 5225

A.11.2.2.2.1 4-step RA type contention-based random access for NR PCell with CCA 5225

A.11.2.2.2.1.1 Test Purpose and Environment 5225

A.11.2.2.2.1.2 Test Requirements 5226

A.11.2.2.2.1.2.1 Random Access Preamble Transmission 5226

A.11.2.2.2.1.2.2 Random Access Response Reception 5227

A.11.2.2.2.1.2.3 No Random Access Response Reception 5227

A.11.2.2.2.1.2.4 Receiving an UL grant for msg3 retransmission 5227

A.11.2.2.2.1.2.5 Reception of an Incorrect Message over Temporary C-RNTI 5227

A.11.2.2.2.1.2.6 Reception of a Correct Message over Temporary C-RNTI 5228

A.11.2.2.2.1.2.7 Contention Resolution Timer expiry 5228

A.11.2.2.2.2 4-step RA type non-contention based random access for NR PSCell with CCA 5228

A.11.2.2.2.2.1 Test Purpose and Environment 5228

A.11.2.2.2.2.2 Test Requirements 5229

A.11.2.2.2.2.2.1 SSB-based Random Access Preamble Transmission 5230

A.11.2.2.2.2.2.2 Random Access Response Reception 5230

A.11.2.2.2.2.2.3 No Random Access Response Reception 5230

A.11.2.2.2.3 2-step RA type contention-based random access for NR PCell with CCA 5231

A.11.2.2.2.3.1 Test Purpose and Environment 5231

A.11.2.2.2.3.2 Test Requirements 5232

A.11.2.2.2.3.2.1 MsgA Transmission 5232

A.11.2.2.2.3.2.2 MsgB Reception 5233

A.11.2.2.2.3.2.3 No MsgB Reception 5233

A.11.2.2.2.4 2-step RA type non-contention-based random access for NR PCell with CCA 5234

A.11.2.2.2.4.1 Test Purpose and Environment 5234

A.11.2.2.2.4.2 Test Requirements 5235

A.11.2.2.2.4.2.1 MsgA Transmission 5235

A.11.2.2.2.4.2.2 MsgB Reception 5236

A.11.2.2.2.4.2.3 No MsgB Reception 5236

A.11.2.2.3 RRC connection release with redirection 5237

A.11.2.2.3.1 Redirection from NR FR1 carrier under CCA to NR FR1 carrier under CCA 5237

A.11.2.2.3.2 Redirection from NR FR1 carrier without CCA to NR FR1 carrier with CCA 5239

A.11.3 Timing 5242

A.11.3.1 UE transmit timing 5242

A.11.3.1.1 UE Transmit Timing Test with PCell under DL CCA 5242

A.11.3.1.1.1 Test Purpose and environment 5242

A.11.3.1.1.2 Test requirements 5244

A.11.3.2 UE timing advance 5245

A.11.3.2.1 UE Timing Advance Adjustment Accuracy with PCell under DL CCA 5245

A.11.3.2.1.1 Test Purpose and Environment 5245

A.11.3.2.1.2 Test Parameters 5245

A.11.3.2.1.3 Test Requirements 5247

A.11.4 Signalling characteristics 5247

A.11.4.1 Radio link monitoring 5247

A.11.4.1.1 Introduction 5247

A.11.4.1.2 Radio link monitoring out-of-sync test for PCell configured with SSB-based RLM RS in non-DRX mode 5248

A.11.4.1.2.1 Test purpose and environment 5248

A.11.4.1.2.2 Test requirements 5250

A.11.4.1.3 Radio link monitoring in-sync test for PCell configured with SSB-based RLM RS in non-DRX mode 5251

A.11.4.1.3.1 Test purpose and environment 5251

A.11.4.1.3.2 Test requirements 5254

A.11.4.1.4 Void 5254

A.11.4.1.4.1 Void 5254

A.11.4.1.4.2 Void 5254

A.11.4.1.5 Void 5254

A.11.4.1.5.1 Void 5254

A.11.4.1.5.2 Void 5254

A.11.4.2 Void 5254

A.11.4.3 SCell activation and deactivation delay 5254

A.11.4.3.1 SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 160 ms SCell measurement cycle 5254

A.11.4.3.1.1 Test Purpose and Environment 5254

A.11.4.3.1.2 Test Requirements 5257

A.11.4.3.2 SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 640 ms SCell measurement cycle 5257

A.11.4.3.2.1 Test Purpose and Environment 5257

A.11.4.3.2.2 Test Requirements 5258

A.11.4.3.3 SCell Activation and Deactivation of unknown SCell with PCell and SCell under CCA 5258

A.11.4.3.3.1 Test Purpose and Environment 5258

A.11.4.3.3.2 Test Requirements 5258

A.11.4.4 Beam failure detection and link recovery procedures 5259

A.11.4.4.1 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode 5259

A.11.4.4.1.1 Test Purpose and Environment 5259

A.11.4.4.1.2 Test Requirements 5262

A.11.4.4.2 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode 5263

A.11.4.4.2.1 Test Purpose and Environment 5263

A.11.4.4.2.2 Test Requirements 5266

A.11.4.5 Active BWP switching 5266

A.11.4.5.1 UL active BWP switch delay with consistent UL LBT failure on PCell subject to UL CCA 5266

A.11.4.5.1.1 Test Purpose and Environment 5266

A.11.4.5.1.2 Test Requirements 5269

A.11.4.5.2 DCI-based and Timer-based Active BWP Switch 5269

A.11.4.5.2.1 NR FR1- NR FR1 DL active BWP switch of PCell with non-DRX in SA 5269

A.11.4.5.2.2 NR FR1 DL active BWP switch with non-DRX in SA 5272

A.11.4.5.3 RRC-based Active BWP Switch 5275

A.11.4.5.3.1 NR FR1 DL active BWP switch of Cell with non-DRX in SA 5275

A.11.4.6 Void 5277

A.11.5 Measurement procedure 5277

A.11.5.1 Intra-frequency measurements 5277

A.11.5.1.1 Event-triggered reporting tests on PCC without gaps under non-DRX 5277

A.11.5.1.1.1 Test purpose and environment 5277

A.11.5.1.1.2 Test parameters 5277

A.11.5.1.1.3 Test Requirements 5279

A.11.5.1.2 Event-triggered reporting tests on PCC without gaps under DRX 5279

A.11.5.1.2.1 Test purpose and environment 5279

A.11.5.1.2.2 Test parameters 5279

A.11.5.1.2.3 Test Requirements 5281

A.11.5.1.3 Void 5282

A.11.5.1.4 Void 5282

A.11.5.1.5 Void 5282

A.11.5.1.6 Void 5282

A.11.5.1.7 Void 5282

A.11.5.1.8 Void 5282

A.11.5.1.9 Void 5282

A.11.5.1.10 Void 5282

A.11.5.1.11 Void 5282

A.11.5.1.12 Void 5282

A.11.5.2 Inter-frequency measurements 5282

A.11.5.2.1 Void 5282

A.11.5.2.2 Void 5282

A.11.5.2.3 Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used 5282

A.11.5.2.3.1 Test Purpose and Environment 5282

A.11.5.2.3.2 Test Requirements 5285

A.11.5.2.4 Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used 5285

A.11.5.2.4.1 Test Purpose and Environment 5285

A.11.5.2.4.2 Test Requirements 5288

A.11.5.2.5 Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used 5288

A.11.5.2.5.1 Test Purpose and Environment 5288

A.11.5.2.5.2 Test Requirements 5291

A.11.5.2.6 Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used 5291

A.11.5.2.6.1 Test Purpose and Environment 5291

A.11.5.2.6.2 Test Requirements 5294

A.11.5.2.7 Event triggered reporting tests for FR1 without SSB time index detection when DRX is not used 5295

A.11.5.2.7.1 Test Purpose and Environment 5295

A.11.5.2.7.2 Test Requirements 5297

A.11.5.2.8 Event triggered reporting tests for FR1 without SSB time index detection when DRX is used 5298

A.11.5.2.8.1 Test Purpose and Environment 5298

A.11.5.2.8.2 Test Requirements 5301

A.11.5.2.9 Event triggered reporting tests for FR1 with SSB time index detection when DRX is not used 5301

A.11.5.2.9.1 Test Purpose and Environment 5301

A.11.5.2.9.2 Test Requirements 5304

A.11.5.2.10 Event triggered reporting tests for FR1 with SSB time index detection when DRX is used 5304

A.11.5.2.10.1 Test Purpose and Environment 5304

A.11.5.2.10.2 Test Requirements 5308

A.11.5.3 Inter-RAT E-UTRAN measurements 5308

A.11.5.3.1 SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 5308

A.11.5.3.1.1 Test Purpose and Environment 5308

A.11.5.3.1.2 Test Requirements 5311

A.11.5.3.2 SA NR - E-UTRAN event-triggered reporting in DRX in FR1 5311

A.11.5.3.2.1 Test Purpose and Environment 5311

A.11.5.3.2.2 Test Requirements 5315

A.11.5.4 L1-RSRP measurements for beam reporting 5315

A.11.5.4.1 SSB based L1-RSRP measurement when DRX is not used 5315

A.11.5.4.1.1 Test Purpose and Environment 5315

A.11.5.4.1.2 Test parameters 5315

A.11.5.4.1.3 Test Requirements 5317

A.11.5.4.2 SSB based L1-RSRP measurement when DRX is used 5317

A.11.5.4.2.1 Test Purpose and Environment 5317

A.11.5.4.2.2 Test parameters 5317

A.11.5.4.2.3 Test Requirements 5319

A.11.5.4.3 SSB based L1-RSRP measurement on SCC when DRX is not used 5319

A.11.5.4.3.1 Test Purpose and Environment 5319

A.11.5.4.3.2 Test parameters 5320

A.11.5.4.3.3 Test Requirements 5321

A.11.5.4.4 SSB based L1-RSRP measurement on SCC when DRX is used 5321

A.11.5.4.4.1 Test Purpose and Environment 5321

A.11.5.4.4.2 Test parameters 5322

A.11.5.4.4.3 Test Requirements 5323

A.11.6 Measurement performance 5323

A.11.6.1 SS-RSRP 5323

A.11.6.1.1 Intra-frequency measurement accuracy on a carrier frequency with CCA 5323

A.11.6.1.1.1 Test Purpose and Environment 5323

A.11.6.1.1.2 Test parameters 5324

A.11.6.1.1.3 Test Requirements 5325

A.11.6.1.2 Intra-frequency measurement accuracy on SCC on a carrier frequency with CCA 5325

A.11.6.1.2.1 Test Purpose and Environment 5325

A.11.6.1.2.2 Test parameters 5325

A.11.6.1.2.3 Test Requirements 5327

A.11.6.2 SS-RSRQ 5327

A.11.6.2.1 Intra-frequency measurement accuracy 5327

A.11.6.2.1.1 Test Purpose and Environment 5327

A.11.6.2.1.2 Test Parameters 5327

A.11.6.2.1.3 Test Requirements 5329

A.11.6.2.2 Inter-frequency measurement accuracy 5329

A.11.6.2.2.1 Test Purpose and Environment 5329

A.11.6.2.2.2 Test Parameters 5329

A.11.6.2.2.3 Test Requirements 5332

A.11.6.2.3 Intra-frequency measurement accuracy on SCC 5332

A.11.6.2.3.1 Test Purpose and Environment 5332

A.11.6.2.3.2 Test Parameters 5332

A.11.6.2.3.3 Test Requirements 5334

A.11.6.2.4 Inter-frequency measurement accuracy 5334

A.11.6.2.4.1 Test Purpose and Environment 5334

A.11.6.2.4.2 Test Parameters 5334

A.11.6.2.4.3 Test Requirements 5340

A.11.6.3 SS-SINR 5340

A.11.6.3.1 Intra-frequency measurement accuracy 5340

A.11.6.3.1.1 Test Purpose and Environment 5340

A.11.6.3.1.2 Test Parameters 5340

A.11.6.3.1.3 Test Requirements 5342

A.11.6.3.2 Inter-frequency measurement accuracy 5342

A.11.6.3.2.1 Test Purpose and Environment 5342

A.11.6.3.2.2 Test Parameters 5342

A.11.6.3.2.3 Test Requirements 5344

A.11.6.3.3 Intra-frequency measurement accuracy on SCC 5344

A.11.6.3.3.1 Test Purpose and Environment 5344

A.11.6.3.3.2 Test Parameters 5344

A.11.6.3.3.3 Test Requirements 5346

A.11.6.3.4 Inter-frequency measurement accuracy 5346

A.11.6.3.4.1 Test Purpose and Environment 5346

A.11.6.3.4.2 Test Parameters 5346

A.11.6.3.4.3 Test Requirements 5350

A.11.6.4 L1-RSRP measurement for beam reporting with CCA serving cell 5350

A.11.6.4.1 SSB based L1-RSRP measurement 5350

A.11.6.4.1.1 Test Purpose and Environment 5350

A.11.6.4.1.2 Test parameters 5350

A.11.6.4.1.3 Test Requirements 5352

A.11.6.5 RSSI 5352

A.11.6.5.1 Intra-frequency RSSI measurement accuracy on PCC with CCA 5352

A.11.6.5.1.1 Test Purpose and Environment 5352

A.11.6.5.1.2 Test parameters 5352

A.11.6.5.1.3 Test Requirements 5353

A.11.6.5.2 Intra-frequency RSSI measurement accuracy on SCC with CCA 5353

A.11.6.5.2.1 Test Purpose and Environment 5353

A.11.6.5.2.2 Test parameters 5353

A.11.6.5.2.3 Test Requirements 5355

A.11.6.5.3 Inter-frequency RSSI measurement accuracy on a carrier with CCA 5355

A.11.6.5.3.1 Test Purpose and Environment 5355

A.11.6.5.3.2 Test parameters 5355

A.11.6.5.3.3 Test Requirements 5357

A.11.6.6 Channel occupancy 5357

A.11.6.6.1 Intra-frequency channel occupancy measurement accuracy on PCC with CCA 5357

A.11.6.6.1.1 Test Purpose and Environment 5357

A.11.6.6.1.2 Test parameters 5357

A.11.6.6.1.3 Test Requirements 5359

A.11.6.6.2 Intra-frequency channel occupancy measurement accuracy on SCC with CCA 5359

A.11.6.6.2.1 Test Purpose and Environment 5359

A.11.6.6.2.2 Test parameters 5359

A.11.6.6.2.3 Test Requirements 5360

A.11.6.6.3 Inter-frequency channel occupancy measurement accuracy on a carrier with CCA 5360

A.11.6.6.3.1 Test Purpose and Environment 5361

A.11.6.6.3.2 Test parameters 5361

A.11.6.6.3.3 Test Requirements 5362

A.11.6.7 E-UTRAN RSRP 5362

A.11.6.8 E-UTRAN RSRQ 5362

A.11.6.9 E-UTRAN SINR 5362

A.12 E-UTRA Standalone Tests with at Least One NR Cell under CCA 5363

A.12.1 RRC_IDLE state mobility 5363

A.12.1.1 Inter-RAT cell re-selection to NR on a carrier frequency with CCA 5363

A.12.1.1.1 E-UTRA Cell reselection to higher priority NR target Cell in FR1 when target cell is subject to CCA 5363

A.12.1.1.1.1 Test Purpose and Environment 5363

A.12.1.1.1.2 Test Requirements 5366

A.12.2 RRC_CONNECTED state mobility 5366

A.12.2.1 Handover 5366

A.12.2.1.1 E-UTRAN - NR with CCA handover 5366

A.12.2.1.1.1 Test Purpose and Environment 5366

A.12.2.1.1.2 Test Requirements 5370

A.12.3 Void 5370

A.12.4 Measurement procedure 5370

A.12.4.1 E-UTRANNR inter-RAT SFTD measurements 5370

A.12.4.1.1 E-UTRA – NR Inter-RAT SFTD Measurement Delay with NR under CCA in non-DRX 5370

A.12.4.1.1.1 Test Purpose and Environment 5370

A.12.4.1.1.2 Test Requirements 5372

A.12.4.2 E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA 5372

A.12.4.2.1 E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used 5372

A.12.4.2.1.1 Test Purpose and Environment 5372

A.12.4.2.1.2 Test Requirements 5376

A.12.4.2.2 E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used 5376

A.12.4.2.2.1 Test Purpose and Environment 5376

A.12.4.2.2.2 Test Requirements 5379

A.12.4.2.3 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used 5380

A.12.4.2.3.1 Test Purpose and Environment 5380

A.12.4.2.3.2 Test Requirements 5383

A.12.4.2.4 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used 5383

A.12.4.2.4.1 Test Purpose and Environment 5383

A.12.4.2.4.2 Test Requirements 5386

A.12.4.2.5 Void 5387

A.12.4.2.6 Void 5387

A.12.5 Measurement performance 5387

A.12.5.1 E-UTRANNR SFTD 5387

A.12.5.1.1 Inter-RAT SFTD accuracy with NR target cell under CCA 5387

A.12.5.1.1.1 Test Purpose 5387

A.12.5.1.1.2 Test Environment 5387

A.12.5.1.1.3 Test Requirements 5389

A.12.5.2 Void 5389

A.12.5.3 Void 5389

A.12.5.4 Void 5390

A.12.5.5 Void 5390

A.12.5.6 Void 5390

A.13 NR Standalone Tests with NR SCell under CCA and All Other NR Cells in FR1 5391

A.13.1 Void 5391

A.13.1.1 Void 5391

A.13.1.2 Void 5391

A.13.2 Signalling characteristics 5391

A.13.2.1 Void 5391

A.13.2.2 SCell activation and deactivation delay 5391

A.13.2.2.1 SCell Activation and Deactivation of known SCell under CCA, 160 ms SCell measurement cycle 5391

A.13.2.2.1.1 Test Purpose and Environment 5391

A.13.2.2.1.2 Test Requirements 5394

A.13.2.2.2 SCell Activation and Deactivation of known SCell under CCA, 640 ms SCell measurement cycle 5394

A.13.2.2.2.1 Test Purpose and Environment 5394

A.13.2.2.2.2 Test Requirements 5395

A.13.2.2.3 SCell Activation and Deactivation of unknown SCell under CCA 5395

A.13.2.2.3.1 Test Purpose and Environment 5395

A.13.2.2.3.2 Test Requirements 5395

A.13.2.3 Void 5396

A.13.3 Measurement procedure 5396

A.13.3.1 Intra-frequency measurements 5396

A.13.3.1.1 Event-triggered reporting tests on SCC without gaps under non-DRX 5396

A.13.3.1.1.1 Test purpose and environment 5396

A.13.3.1.1.2 Test parameters 5396

A.13.3.1.1.3 Test Requirements 5399

A.13.3.1.2 Event-triggered reporting tests on SCC without gaps under DRX 5399

A.13.3.1.2.1 Test purpose and environment 5399

A.13.3.1.2.2 Test parameters 5399

A.13.3.1.2.3 Test Requirements 5402

A.13.3.1.3 Event-triggered reporting tests on SCC with per-UE gaps under non-DRX 5402

A.13.3.1.3.1 Test purpose and environment 5402

A.13.3.1.3.2 Test parameters 5402

A.13.3.1.3.3 Test Requirements 5405

A.13.3.1.4 Event-triggered reporting tests on SCC with per-UE gaps under DRX 5406

A.13.3.1.4.1 Test purpose and environment 5406

A.13.3.1.4.2 Test parameters 5406

A.13.3.1.4.3 Test Requirements 5409

A.13.3.1.5 Void 5409

A.13.3.1.6 Void 5409

A.13.3.2 Inter-frequency measurements 5409

A.13.3.2.1 Void 5409

A.13.3.2.2 Void 5409

A.13.3.2.3 Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used 5409

A.13.3.2.3.1 Test Purpose and Environment 5409

A.13.3.2.3.2 Test Requirements 5412

A.13.3.2.4 Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used 5413

A.13.3.2.4.1 Test Purpose and Environment 5413

A.13.3.2.4.2 Test Requirements 5416

A.13.3.2.5 Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used 5416

A.13.3.2.5.1 Test Purpose and Environment 5416

A.13.3.2.5.2 Test Requirements 5419

A.13.3.2.6 Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used 5419

A.13.3.2.6.1 Test Purpose and Environment 5419

A.13.3.2.6.2 Test Requirements 5423

A.13.3.3 L1-RSRP measurements for beam reporting 5423

A.13.3.3.1 SSB based L1-RSRP measurement when DRX is not used 5423

A.13.3.3.1.1 Test Purpose and Environment 5423

A.13.3.3.1.2 Test parameters 5423

A.13.3.3.1.3 Test Requirements 5425

A.13.3.3.2 SSB based L1-RSRP measurement when DRX is used 5426

A.13.3.3.2.1 Test Purpose and Environment 5426

A.13.3.3.2.2 Test parameters 5426

A.13.3.3.2.3 Test Requirements 5428

A.13.4 Measurement performance 5428

A.13.4.1 SS-RSRP 5428

A.13.4.1.1 Intra-frequency measurement accuracy on a carrier frequency with CCA 5428

A.13.4.1.1.1 Test Purpose and Environment 5428

A.13.4.1.1.2 Test parameters 5428

A.13.4.1.1.3 Test Requirements 5430

A.13.4.2 SS-RSRQ 5430

A.13.4.2.1 Intra-frequency measurement accuracy on SCC 5430

A.13.4.2.1.1 Test Purpose and Environment 5430

A.13.4.2.1.2 Test Parameters 5430

A.13.4.2.1.3 Test Requirements 5434

A.13.4.3 SS-SINR 5434

A.13.4.3.1 Intra-frequency measurement accuracy on SCC 5434

A.13.4.3.1.1 Test Purpose and Environment 5434

A.13.4.3.1.2 Test Parameters 5434

A.13.4.3.1.3 Test Requirements 5438

A.13.4.4 L1-RSRP measurement for beam reporting with CCA serving cell 5438

A.13.4.4.1 SSB based L1-RSRP measurement 5438

A.13.4.4.1.1 Test Purpose and Environment 5438

A.13.4.4.1.2 Test parameters 5439

A.13.4.4.1.3 Test Requirements 5441

A.13.4.5 RSSI 5441

A.13.4.5.1  Intra-frequency RSSI measurement accuracy on a carrier with CCA 5441

A.13.4.5.1.1 Test Purpose and Environment 5441

A.13.4.5.1.2 Test parameters 5441

A.13.4.5.1.3 Test Requirements 5443

A.13.4.5.2 Inter-frequency RSSI measurement accuracy on a carrier with CCA 5443

A.13.4.5.2.1 Test Purpose and Environment 5443

A.13.4.5.2.2 Test parameters 5443

A.13.4.5.2.3 Test Requirements 5445

A.13.4.6 Channel occupancy 5445

A.13.4.6.1 Intra-frequency channel occupancy measurement accuracy on SCC with CCA 5445

A.13.4.6.1.1 Test Purpose and Environment 5445

A.13.4.6.1.2 Test parameters 5445

A.13.4.6.1.3 Test Requirements 5447

A.13.4.6.2 Inter-frequency channel occupancy measurement accuracy on a carrier with CCA 5447

A.13.4.6.2.1 Test Purpose and Environment 5447

A.13.4.6.2.2 Test parameters 5447

A.13.4.6.2.3 Test Requirements 5448

A.14 NR standalone tests for Satellite access 5449

A.14.1 RRC_IDLE state mobility 5449

A.14.1.1 Cell reselection to FR1 intra-frequency NR case 5449

A.14.1.1.1 Test Purpose and Environment 5449

A.14.1.1.2 Test Parameters 5449

A.14.1.1.3 Test Requirements 5450

A.14.1.2 Cell reselection to FR1 intra-frequency NR cell for UE configured with the feature for enhanced requirements 5451

A.14.1.2.1 Test Purpose and Environment 5451

A.14.1.2.2 Test Parameters 5451

A.14.1.2.3 Test Requirements 5453

A.14.1.3 Time-based measurement initiation to FR1 intra-frequency NR cell reselection 5453

A.14.1.3.1 Test Purpose and Environment 5453

A.14.1.3.2 Test Parameters 5453

A.14.1.3.3 Test Requirements 5455

A.14.1.4 Location-based measurement initiation to FR1 intra-frequency NR cell reselection 5455

A.14.1.4.1 Test Purpose and Environment 5455

A.14.1.4.2 Test Parameters 5455

A.14.1.4.3 Test Requirements 5457

A.14.1.5 Cell reselection to FR1 inter-frequency NR case 5457

A.14.1.5.1 Test Purpose and Environment 5457

A.14.1.5.2 Test Parameters 5457

A.14.1.5.3 Test Requirements 5459

A.14.1.6 Cell re-selection to FR1 inter-frequency NR cell for UE configured with feature for enhanced requirements 5460

A.14.1.6.1 Test Purpose and Environment 5460

A.14.1.6.2 Test Parameters 5460

A.14.1.6.3 Test Requirements 5462

A.14.1.7 Time-based measurement initiation to FR1 inter-frequency cell reselection 5462

A.14.1.7.1 Test Purpose and Environment 5462

A.14.1.7.2 Test Parameters 5463

A.14.1.7.3 Test Requirements 5464

A.14.1.8 Location-based measurement initiation to FR1 inter-frequency NR cell reselection 5464

A.14.1.8.1 Test Purpose and Environment 5464

A.14.1.8.2 Test Parameters 5464

A.14.1.8.3 Test Requirements 5466

A.14.1.9 Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion 5466

A.14.1.9.1 Test Purpose and Environment 5466

A.14.1.9.2 Test Parameters 5466

A.14.1.9.3 Test Requirements 5468

A.14.1.10 Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion 5469

A.14.1.10.1 Test Purpose and Environment 5469

A.14.1.10.2 Test Parameters 5469

A.14.1.10.3 Test Requirements 5471

A.14.1.11 Cell reselection to FR1 inter-RAT E-UTRAN cells with TN carrier 5471

A.14.1.11.1 Test purpose and Environment 5471

A.14.1.11.2 Test parameters 5471

A.14.1.11.3 Test requirements 5473

A.14.1.12 Cell re-selection to FR1 inter-frequency NR case with TN carrier 5474

A.14.1.12.1 Test purpose and Environment 5474

A.14.1.12.2 Test parameters 5474

A.14.1.12.3 Test requirements 5476

A.14.1.13 Cell reselection to FR1 intra-frequency NR case for UE operating on a cell with less than 5 MHz BW 5476

A.14.1.13.1 Test Purpose and Environment 5476

A.14.1.13.2 Test Parameters 5476

A.14.1.13.3 Test Requirements 5478

A.14.2 RRC_CONNECTED state mobility 5478

A.14.2.1 Handover 5478

A.14.2.1.1 Intra-frequency SAN Handover from FR1 to FR1 5478

A.14.2.1.1.1 Test Purpose and Environment 5478

A.14.2.1.1.2 Test Parameters 5478

A.14.2.1.1.3 Test Requirements 5480

A.14.2.1.2 Inter-frequency SAN Handover from FR1 to FR1 5480

A.14.2.1.2.1 Test Purpose and Environment 5480

A.14.2.1.2.2 Test Parameters 5480

A.14.2.1.2.3 Test Requirements 5482

A.14.2.1.3 Intra-frequency SAN time-based conditional Handover from FR1 to FR1 5482

A.14.2.1.3.1 Test Purpose and Environment 5482

A.14.2.1.3.2 Test Parameters 5483

A.14.2.1.3.3 Test Requirements 5484

A.14.2.1.4 Inter-frequency SAN time-based conditional Handover from FR1 to FR1 5484

A.14.2.1.4.1 Test Purpose and Environment 5484

A.14.2.1.4.2 Test Parameters 5485

A.14.2.1.4.3 Test Requirements 5486

A.14.2.1.5 Intra-frequency SAN distance-based conditional Handover from FR1 to FR1 5486

A.14.2.1.5.1 Test Purpose and Environment 5487

A.14.2.1.5.2 Test Parameters 5487

A.14.2.1.5.3 Test Requirements 5488

A.14.2.1.6 Inter-frequency SAN distance-based conditional Handover from FR1 to FR1 5489

A.14.2.1.6.1 Test Purpose and Environment 5489

A.14.2.1.6.2 Test Parameters 5489

A.14.2.1.6.3 Test Requirements 5491

A.14.2.1.7 Intra-frequency intra-satellite Handover from FR2-NTN to FR2-NTN 5491

A.14.2.1.7.1 Test Purpose and Environment 5491

A.14.2.1.7.2 Test Parameters 5491

A.14.2.1.7.3 Test Requirements 5493

A.14.2.1.8 Intra-frequency SAN Handover from FR1 to FR1 5494

A.14.2.1.8.1 Test Purpose and Environment 5494

A.14.2.1.8.2 Test Parameters 5494

A.14.2.1.8.3 Test Requirements 5496

A.14.2.1.9 Intra-frequency inter-satellite handover from FR2-NTN to FR2-NTN 5496

A.14.2.1.9.1 Test Purpose and Environment 5496

A.14.2.1.9.2 Test Parameters 5496

A.14.2.1.9.3 Test Requirements 5498

A.14.2.1.10 Intra-frequency SAN Handover from FR1 to FR1 for UE operating on a cell with less than 5 MHz BWA.14.2.1.10.1 Test Purpose and Environment 5498

A.14.2.1.10.2 Test Parameters 5498

A.14.2.1.10.3 Test Requirements 5500

A.14.2.1.11 Intra-frequency SAN time-based conditional Handover from FR1 to FR1 for UE operating on a cell with less than 5 MHz BW 5500

A.14.2.11.1 Test Purpose and Environment 5500

A.14.2.11.2 Test Parameters 5500

A.14.2.11.3 Test Requirements 5502

A.14.2.2 RRC Connection Mobility Control 5502

A.14.2.2.1 SA: RRC Re-establishment for SAN 5502

A.14.2.2.1.1 Intra-frequency RRC Re-establishment in FR1 5502

A.14.2.2.1.2 Inter-frequency RRC Re-establishment in FR1 5505

A.14.2.2.1.3 Inter-frequency RRC Re-establishment in FR1 with 160ms SSB periodicity 5507

A.14.2.2.2 Random Access 5509

A.14.2.2.2.1 4-step RA type contention based random access test in FR1 for NR standalone 5509

A.14.2.2.2.1.1 Test Purpose and Environment 5509

A.14.2.2.2.1.2 Test Requirements 5510

A.14.2.2.2.2 4-step RA type non-contention based random access test in FR1 for NR standalone 5512

A.14.2.2.2.2.1 Test Purpose and Environment 5512

A.14.2.2.2.2.2 Test Requirements 5513

A.14.2.2.3 RRC Connection Release with Redirection 5515

A.14.2.2.3.1 Redirection from NR in FR1 to NR in FR1 5515

A.14.2.2.3.1.1 Test Purpose and Environment 5515

A.14.2.2.3.1.2 Test Parameters 5515

A.14.2.2.3.1.3 Test Requirements 5516

A.14.2.2.4 RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 5517

A.14.2.2.4.1 Test Purpose and Environment 5517

A.14.2.2.4.2 Test Parameters 5517

A.14.2.2.4.3 Test Requirements 5519

A.14.2.2.5 RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1 5519

A.14.2.2.5.1 Test Purpose and Environment 5519

A.14.2.2.5.2 Test Parameters 5519

A.14.2.2.5.3 Test Requirements 5521

A.14.2.2.6 RACH-based hard Satellite switching with re-synchronization from FR1 to FR1 for less than 5MHz with NTN 5521

A.14.2.2.6.1 Test Purpose and Environment 5521

A.14.2.2.6.2 Test Parameters 5521

A.14.2.2.6.3 Test Requirements 5522

A.14.2.2.7 RACH-based Hard Satellite switching with re-synchronization from FR2 to FR2 5523

A.14.2.2.7.1 Test Purpose and Environment 5523

A.14.2.2.7.2 Test Parameters 5523

A.14.2.2.7.3 Test Requirements 5525

A.14.2.2.8 RACH-less Soft Satellite switching with re-synchronization from FR2 to FR2 5525

A.14.2.2.8.1 Test Purpose and Environment 5525

A.14.2.2.8.2 Test Parameters 5525

A.14.2.2.8.3 Test Requirements 5528

A.14.2.3 Intra-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1 5528

A.14.2.3.1 Test Purpose and Environment 5528

A.14.2.3.2 Test Parameters 5528

A.14.2.3.3 Test Requirements 5530

A.14.2.4 Inter-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1 5530

A.14.2.4.1 Test Purpose and Environment 5530

A.14.2.4.2 Test Parameters 5530

A.14.2.4.3 Test Requirements 5532

A.14.3 Timing for Satellite Access 5532

A.14.3.1 UE transmit timing for Satellite Access 5532

A.14.3.1.1 NR UE Transmit Timing Test for FR1 5532

A.14.3.1.1.1 Test Purpose and environment 5532

A.14.3.1.1.2 Test requirements 5534

A.14.3.1.2 NR UE Transmit Timing Test for FR2-NTN 5535

A.14.3.1.2.1 Test Purpose and environment 5535

A.14.3.1.2.2 Test requirements 5537

A.14.3.2 Timing advance for satellite access 5538

A.14.3.2.1 SA FR1 timing advance adjustment accuracy 5538

A.14.3.2.1.1 Test Purpose and Environment 5538

A.14.3.2.1.2 Test Parameters 5538

A.14.3.2.1.3 Test Requirements 5540

A.14.3.2.3 SA FR2-NTN timing advance adjustment accuracy 5540

A.14.3.2.3.1 Test Purpose and Environment 5540

A.14.3.2.3.2 Test Parameters 5540

A.14.3.2.1.3 Test Requirements 5543

A.14.4 Signalling characteristics 5543

A.14.4.1 Radio link Monitoring 5543

A.14.4.1.1 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode 5544

A.14.4.1.1.1 Test Purpose and Environment 5544

A.14.4.1.1.2 Test Requirements 5546

A.14.4.1.2 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode 5546

A.14.4.1.2.1 Test Purpose and Environment 5546

A.14.4.1.2.2 Test Requirements 5548

A.14.4.1.3 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode 5549

A.14.4.1.3.1 Test Purpose and Environment 5549

A.14.4.1.3.2 Test Requirements 5551

A.14.4.1.4 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode 5551

A.14.4.1.4.1 Test Purpose and Environment 5551

A.14.4.1.4.2 Test Requirements 5554

A.14.4.1.5 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode 5554

A.14.4.1.5.1 Test Purpose and Environment 5554

A.14.4.1.5.2 Test Requirements 5556

A.14.4.1.6 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode 5556

A.14.4.1.6.1 Test Purpose and Environment 5556

A.14.4.1.6.2 Test Requirements 5559

A.14.4.1.7 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode 5559

A.14.4.1.7.1 Test Purpose and Environment 5559

A.14.4.1.7.2 Test Requirements 5562

A.14.4.1.8 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode 5562

A.14.4.1.8.1 Test Purpose and Environment 5562

A.14.4.1.8.2 Test Requirements 5565

A.14.4.1.9 Radio Link Monitoring Out-of-sync Test for FR2 SAN PCell configured with SSB-based RLM RS in non-DRX mode 5565

A.14.4.1.9.1 Test Purpose and Environment 5565

A.14.4.1.9.2 Test Requirements 5567

A.14.4.1.10 Radio Link Monitoring In-sync Test for FR2 SAN PCell configured with SSB-based RLM RS in non-DRX mode 5568

A.14.4.1.10.1 Test Purpose and Environment 5568

A.14.4.1.10.2 Test Requirements 5570

A.14.4.1.11 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode 5570

A.14.4.1.11.1 Test Purpose and Environment 5570

A.14.4.1.11.2 Test Requirements 5571

A.14.4.1.12 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode for less than 5 MHz BW 5571

A.14.4.1.12.1 Test Purpose and Environment 5571

A.14.4.1.12.2 Test Requirements 5572

A.14.4.2 Beam Failure Detection and Link recovery procedures for satellite access 5573

A.14.4.2.1 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode 5573

A.14.4.2.1.1 Test Purpose and Environment 5573

A.14.4.2.1.2 Test Requirements 5575

A.14.4.2.2 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode 5576

A.14.4.2.2.1 Test Purpose and Environment 5576

A.14.4.2.2.2 Test Requirements 5578

A.14.4.2.3 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode 5579

A.14.4.2.3.1 Test Purpose and Environment 5579

A.14.4.2.3.2 Test Requirements 5581

A.14.4.2.4 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode 5582

A.14.4.2.4.1 Test Purpose and Environment 5582

A.14.4.2.4.2 Test Requirements 5584

A.14.4.2.5 Void 5585

A.14.4.2.6 Void 5585

A.14.4.2.7 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode for a UE operating on a cell with less than 5 MHz BW 5585

A.14.4.2.7.1 Test Purpose and Environment 5585

A.14.4.2.7.2 Test Requirements 5586

A.14.4.3 Active BWP switch for satellite access 5586

A.14.4.3.1 DCI-based and Timer-based Active BWP Switch 5586

A.14.4.3.1.1 NR FR1 DL active BWP switch with non-DRX in SA 5586

A.14.4.3.1.1.1 Test Purpose and Environment 5586

A.14.4.3.1.1.2 Test Requirements 5588

A.14.4.3.2 RRC-based Active BWP Switch 5589

A.14.4.3.2.1 NR FR1 DL active BWP switch of Cell with non-DRX in SA 5589

A.14.4.3.2.1.1 Test Purpose and Environment 5589

A.14.4.3.2.1.2 Test Requirements 5590

A.14.4.4 UE specific CBW change for satellite access 5591

A.14.4.4.1 UE specific CBW change on PCell in FR1 in non-DRX 5591

A.14.4.4.1.1 Test Purpose and Environment 5591

A.14.4.4.1.2 Test Requirements 5593

A.14.4.5 Pathloss reference signal switching delay 5593

A.14.4.5.1 MAC-CE based pathloss reference signal switch delay 5593

A.14.4.5.1.1 Test Purpose and Environment 5593

A.14.4.5.1.2 Test Requirements 5595

A.14.5 Measurement procedure 5595

A.14.5.1 Intra-frequency Measurements 5595

A.14.5.1.1 SA event triggered reporting tests without gap under non-DRX 5596

A.14.5.1.1.1 Test purpose and Environment 5596

A.14.5.1.1.2 Test parameters 5596

A.14.5.1.1.3 Test Requirements 5597

A.14.5.1.2 SA event triggered reporting tests without gap under DRX 5597

A.14.5.1.2.1 Test purpose and Environment 5597

A.14.5.1.2.2 Test parameters 5597

A.14.5.1.2.3 Test Requirements 5599

A.14.5.1.3 SA event triggered reporting tests without gap under non-DRX with SSB index reading 5599

A.14.5.1.3.1 Test purpose and Environment 5599

A.14.5.1.3.2 Test parameters 5599

A.14.5.1.3.3 Test Requirements 5601

A.14.5.1.4 SA event triggered reporting tests with single measurement gap under non-DRX for satellite access 5601

A.14.5.1.4.1 Test purpose and Environment 5601

A.14.5.1.4.2 Test parameters 5601

A.14.5.1.4.3 Test Requirements 5603

A.14.5.1.5 SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access 5603

A.14.5.1.5.1 Test purpose and Environment 5603

A.14.5.1.5.2 Test parameters 5603

A.15.5.1.5.3 Test Requirements 5605

A.14.5.1.6 SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access 5605

A.14.5.1.6.1 Test purpose and Environment 5605

A.14.5.1.6.2 Test parameters 5605

A.14.5.1.6.3 Test Requirements 5607

A.14.5.1.7 SA event triggered reporting test with SSB time index reading without gap under non-DRX for FR2-NTN 5607

A.14.5.1.7.1 Test purpose and Environment 5607

A.14.5.1.7.2 Test parameters 5607

A.14.5.1.7.3 Test Requirements 5609

A.14.5.1.8 SA event triggered reporting tests without gap under non-DRX with SSB index reading under less 5MHz BW 5609

A.14.5.1.8.1 Test purpose and Environment 5609

A.14.5.1.8.2 Test parameters 5609

A.14.5.1.8.3 Test Requirements 5611

A.14.5.1.9 SA event triggered reporting tests without gap under non-DRX 5611

A.14.5.1.9.1 Test purpose and Environment 5611

A.14.5.1.9.2 Test parameters 5611

A.14.5.1.9.3 Test Requirements 5613

A.14.5.2 Inter-frequency Measurements 5613

A.14.5.2.1 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with single gap for satellite access 5613

A.14.5.2.1.1 Test Purpose and Environment 5613

A.14.5.2.1.2 Test Requirements 5615

A.14.5.2.2 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for satellite access 5615

A.14.5.2.2.1 Test Purpose and Environment 5615

A.14.5.2.2.2 Test Requirements 5618

A.14.5.2.3 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for satellite access 5618

A.14.5.2.3.1 Test Purpose and Environment 5618

A.14.5.2.3.2 Test Requirements 5620

A.14.5.2.4 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for satellite access 5620

A.14.5.2.4.1 Test Purpose and Environment 5620

A.14.5.2.4.2 Test Requirements 5622

A.14.5.2.5 void 5622

A.14.5.2.5.1 void 5622

A.14.5.2.5.2 void 5622

A.14.5.2.6 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for satellite access 5623

A.14.5.2.6.1 Test Purpose and Environment 5623

A.14.5.2.6.2 Test Requirements 5625

A.14.5.2.7 Event triggered reporting test without gap under non-DRX 5625

A.14.5.2.7.1 Test purpose and Environment 5625

A.14.5.2.7.2 Test parameters 5625

A.14.5.2.7.3 Test Requirements 5626

A.14.5.2.8 Event triggered reporting tests without gap under DRX 5626

A.14.5.2.8.1 Test purpose and Environment 5626

A.14.5.2.8.2 Test parameters 5627

A.14.5.2.8.3 Test Requirements 5628

A.14.5.2.9 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used with single gap for 3 MHz channel bandwidth in satellite access 5628

A.14.5.2.9.1 Test Purpose and Environment 5628

A.14.5.2.9.2 Test Requirements 5630

A.14.5.3 L1-RSRP measurement for beam reporting for satellite access 5630

A.14.5.3.1 SSB based L1-RSRP measurement for satellite access when DRX is not used 5630

A.14.5.3.1.1 Test Purpose and Environment 5630

A.14.5.3.1.2 Test parameters 5630

A.14.5.3.1.3 Test Requirements 5632

A.14.5.3.2 SSB based L1-RSRP measurement for satellite access when DRX is used 5632

A.14.5.3.2.1 Test Purpose and Environment 5632

A.14.5.3.2.2 Test parameters 5632

A.14.5.3.2.3 Test Requirements 5634

A.14.5.3.3 CSI-RS based L1-RSRP measurement for satellite access when DRX is not used 5634

A.14.5.3.3.1 Test Purpose and Environment 5634

A.14.5.3.3.2 Test parameters 5634

A.14.5.3.3.3 Test Requirements 5636

A.14.5.3.4 CSI-RS based L1-RSRP measurement for satellite access when DRX is used 5636

A.14.5.3.4.1 Test Purpose and Environment 5636

A.14.5.3.4.2 Test parameters 5636

A.14.5.3.4.3 Test Requirements 5638

A.14.5.3.5 SSB based L1-RSRP measurement when DRX is not used in FR2-NTN 5638

A.14.5.3.5.1 Test Purpose and Environment 5638

A.14.5.3.5.2 Test parameters 5638

A.14.5.3.5.3 Test Requirements 5640

A.14.6 Measurement Performance requirements 5640

A.14.6.1 SS-RSRP for SAN 5640

A.14.6.1.1 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell 5640

A.14.6.1.1.1 Test Purpose and Environment 5640

A.14.6.1.1.2 Test parameters 5640

A.14.6.1.1.3 Test Requirements 5642

A.14.6.1.2 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell 5642

A.14.6.1.2.1 Test Purpose and Environment 5642

A.14.6.1.2.2 Test parameters 5642

A.14.6.1.2.3 Test Requirements 5643

A.14.6.1.3 SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell 5643

A.14.6.1.3.1 Test Purpose and Environment 5643

A.14.6.1.3.2 Test parameters 5644

A.14.6.1.3.3 Test Requirements 5646

A.14.6.2 SS-RSRQ 5647

A.14.6.2.1 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access 5647

A.14.6.2.1.1 Test Purpose and Environment 5647

A.14.6.2.1.2 Test Parameters 5647

A.14.6.2.1.3 Test Requirements 5648

A.14.6.2.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access 5648

A.14.6.2.2.1 Test Purpose and Environment 5648

A.14.6.2.2.2 Test Parameters 5648

A.14.6.2.2.3 Test Requirements 5650

A.14.6.3 SS-SINR 5650

A.14.6.3.1 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 5650

A.14.6.3.1.1 Test Purpose and Environment 5650

A.14.6.3.1.2 Test Parameters 5650

A.14.6.3.1.3 Test Requirements 5651

A.14.6.3.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 5652

A.14.6.3.2.1 Test Purpose and Environment 5652

A.14.6.3.2.2 Test Parameters 5652

A.14.6.3.2.3 Test Requirements 5653

A.14.6.4 L1-RSRP measurement for beam reporting 5653

A.14.6.4.1 SSB based L1-RSRP measurement 5653

A.14.6.4.1.1 Test Purpose and Environment 5653

A.14.6.4.1.2 Test parameters 5653

A.14.6.4.1.3 Test Requirements 5655

A.14.6.4.2 CSI-RS based L1-RSRP measurement on resource set with repetition off 5655

A.14.6.4.2.1 Test Purpose and Environment 5655

A.14.6.4.2.2 Test parameters 5655

A.14.6.4.2.3 Test Requirements 5656

A.14.6.4.3 SSB based L1-RSRP measurement for VSAT UE in FR2-NTN when DRX is not used 5656

A.14.6.4.3.1 Test Purpose and Environment 5656

A.14.6.4.3.2 Test parameters 5656

A.14.6.4.3.3 Test Requirements 5658

A.15 NR standalone tests with one or more NR cells in FR2-2 5659

A.15.1 SA: RRC_IDLE state mobility 5659

A.15.1.1 Cell re-selection to NR 5659

A.15.1.1.1 Cell re-selection to FR2-2 intra-frequency NR case 5659

A.15.1.1.1.1 Test Purpose and Environment 5659

A.15.1.1.1.2 Test Parameters 5659

A.15.1.1.1.3 Test Requirements 5661

A.15.1.2 Cell re-selection to FR2-2 inter-frequency NR case 5661

A.15.1.2.1 Test Purpose and Environment 5661

A.15.1.2.2 Test Parameters 5662

A.15.1.2.3 Test Requirements 5664

A.15.1.3 Cell re-selection to FR2-2 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion 5664

A.15.1.3.1 Test Purpose and Environment 5664

A.15.1.3.2 Test Parameters 5664

A.15.1.3.3 Test Requirements 5666

A.15.1.4 Cell re-selection to FR2-2 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion 5667

A.15.1.4.1 Test Purpose and Environment 5667

A.15.1.4.2 Test Parameters 5667

A.15.1.4.3 Test Requirements 5669

A.15.1.5 Cell re-selection to FR2-2 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion 5669

A.15.1.5.1 Test Purpose and Environment 5669

A.15.1.5.2 Test Parameters 5669

A.15.1.5.3 Test Requirements 5671

A.15.1.6 Cell re-selection to FR2-2 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion 5672

A.15.1.6.1 Test Purpose and Environment 5672

A.15.1.6.2 Test Parameters 5672

A.15.1.6.3 Test Requirements 5674

A.15.2 Signaling characteristics 5674

A.15.2.1 SCell Activation and Deactivation Delay 5674

A.15.2.1.1 SCell Activation and deactivation for SCell in FR2-2 intra-band in non-DRX 5674

A.15.2.1.1.1 Test Purpose and Environment 5674

A.15.2.1.1.2 Test Requirements 5676

A.15.2.1.2 SCell Activation and deactivation for FR1+FR2-2 inter-band with target SCell in FR2-2 5676

A.15.2.1.2.1 Test Purpose and Environment 5676

A.15.2.1.2.2 Test Requirements 5679

A.15.2.1.3 SCell Activation and deactivation for SCell in FR2-2 inter-band in non-DRX 5679

A.15.2.1.3.1 Test Purpose and Environment 5680

A.15.2.1.3.2 Test Requirements 5682

A.15.2.1.4 Direct SCell activation at SCell addition of known SCell in FR2-2 5683

A.15.2.1.4.1 Test Purpose and Environment 5683

A.15.2.1.4.2 Test Requirements 5685

A.15.2.1.5 Direct SCell activation at handover with known SCell in FR2-2 5686

A.15.2.1.5.1 Test Purpose and Environment 5686

A.15.2.1.5.2 Test Requirements 5688

A.15.3 RRC_CONNECTED state mobility 5689

A.15.3.1 Handover 5689

A.15.3.1.1 Intra-frequency handover from FR2-2 carrier with CCA to FR2-2 carrier with CCA; unknown target cell 5689

A.15.3.1.1.1 Test Purpose and Environment 5689

A.15.3.1.1.2 Test Parameters 5689

A.15.3.1.1.3 Test Requirements 5691

A.15.3.1.2 Inter-frequency handover from FR1 to FR2-2 carrier with CCA; unknown target cell 5692

A.15.3.1.2.1 Test Purpose and Environment 5692

A.15.3.1.2.2 Test Parameters 5692

A.15.3.1.2.3 Test Requirements 5694

A.15.4 Measurement procedure 5694

A.15.4.1 Intra-frequency Measurements 5694

A.15.4.1.1 SA event triggered reporting test without gap under non-DRX for FR2-2 with CCA 5694

A.15.4.1.1.1 Test purpose and Environment 5694

A.15.4.1.1.2 Test Requirements 5697

A.15.4.2 Inter-frequency Measurements 5698

A.15.4.2.1 SA event triggered reporting tests for FR2-2 with CCA without SSB time index detection when DRX is not used (PCell in FR2-2) 5698

A.15.4.2.1.1 Test Purpose and Environment 5698

A.15.4.2.1.2 Test Requirements 5700

A.16 NR standalone tests with all NR cells in FR1 for RedCap 5701

A.16.1 SA: RRC_IDLE state mobility for RedCap 5701

A.16.1.1 Cell re-selection to NR 5701

A.16.1.1.1 Cell re-selection to FR1 intra-frequency NR case for 1 Rx UE 5701

A.16.1.1.1.1 Test Purpose and Environment 5701

A.16.1.1.1.2 Test Parameters 5701

A.16.1.1.1.3 Test Requirements 5703

A.16.1.1.2 Cell re-selection to FR1 intra-frequency NR case for 2 Rx UE 5704

A.16.1.1.2.1 Test Purpose and Environment 5704

A.16.1.1.2.2 Test Parameters 5704

A.16.1.1.2.3 Test Requirements 5706

A.16.1.1.3 Cell re-selection to FR1 inter-frequency NR case for 1 Rx UE 5706

A.16.1.1.3.1 Test Purpose and Environment 5706

A.16.1.1.3.2 Test Parameters 5706

A.16.1.1.3.3 Test Requirements 5709

A.16.1.1.4 Cell re-selection to FR1 inter-frequency NR case for 2 Rx UE 5709

A.16.1.1.4.1 Test Purpose and Environment 5709

A.16.1.1.4.2 Test Parameters 5709

A.16.1.1.4.3 Test Requirements 5712

A.16.1.1.5 Cell re-selection to FR1 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE 5712

A.16.1.1.5.1 Test Purpose and Environment 5712

A.16.1.1.5.2 Test Parameters 5712

A.16.1.1.5.3 Test Requirements 5715

A.16.1.1.6 Cell re-selection to FR1 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE 5715

A.16.1.1.6.1 Test Purpose and Environment 5715

A.16.1.1.6.2 Test Parameters 5715

A.16.1.1.6.3 Test Requirements 5717

A.16.1.1.7 Cell re-selection to FR1 inter-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE 5718

A.16.1.1.7.1 Test Purpose and Environment 5718

A.16.1.1.7.2 Test Parameters 5718

A.16.1.1.7.3 Test Requirements 5720

A.16.1.1.8 Cell re-selection to FR1 inter-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE 5721

A.16.1.1.8.1 Test Purpose and Environment 5721

A.16.1.1.8.2 Test Parameters 5721

A.16.1.1.8.3 Test Requirements 5723

A.16.1.2 Inter-RAT E-UTRAN cell re-selection for RedCap 5724

A.16.1.2.1 Cell re-selection to higher priority E-UTRAN for 1 RX 5724

A.16.1.2.1.1 Test Purpose and Environment 5724

A.16.1.2.1.2 Test Parameters 5724

A.16.1.2.1.3 Test Requirements 5727

A.16.1.2.2 Cell re-selection to higher priority E-UTRAN for 2 RX 5727

A.16.1.2.2.1 Test Purpose and Environment 5727

A.16.1.2.2.2 Test Parameters 5727

A.16.1.2.2.3 Test Requirements 5730

A.16.1.2.3.1 Test Purpose and Environment 5730

A. 16.1.2.3.2 Test Parameters 5730

A.16.1.2.3.3 Test Requirements 5733

A.16.1.2.4.1 Test Purpose and Environment 5733

A.16.1.2.4.2 Test Parameters 5733

A.16.1.3.1.3 Test Requirements 5736

A.16.1.2.5 Cell re-selection to lower priority E-UTRAN for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE 5736

A.16.1.2.5.1 Test Purpose and Environment 5736

A.16.1.2.5.2 Test Parameters 5736

A.16.1.2.5.3 Test Requirements 5739

A.16.1.2.6 Cell re-selection to lower priority E-UTRAN for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE 5739

A.16.1.2.6.1 Test Purpose and Environment 5740

A.16.1.2.6.2 Test Parameters 5740

A.16.1.2.6.3 Test Requirements 5742

A.16.2 SA: RRC_INACTIVE state mobility for RedCap 5743

A.16.2.1 Configured Grant based Small Data Transmissions (CG-SDT) for RedCap 5743

A.16.2.1.1 NR UE CG-SDT Test in FR1 for 1 Rx RedCap UE 5743

A.16.2.1.1.1 Test purpose and Environment 5743

A.16.2.1.1.2 Test Parameters 5744

A.16.2.1.1.3 Test requirements 5746

A.16.2.1.2 NR UE CG-SDT Test in FR1 for 2 Rx RedCap UE 5746

A.16.2.1.2.1 Test purpose and Environment 5746

A.16.2.1.2.2 Test Parameters 5748

A.16.2.1.2.3 Test requirements 5749

A.16.2.2 Cell Reselection for Positioning 5750

A.16.2.2.1 Cell re-selection to FR1 intra-frequency NR case with RRC_INACTIVE eDRX and positioning SRS 5750

A.16.2.2.1.1 Test Purpose and Environment 5750

A.16.2.2.1.2 Test Parameters 5750

A.16.2.2.1.3 Test Requirements 5753

A.16.3 RRC_CONNECTED state mobility for RedCap 5753

A.16.3.1 Handover 5753

A.16.3.1.1 Intra-frequency handover from FR1 to FR1; known target cell for 1 Rx UE 5753

A.16.3.1.1.1 Test Purpose and Environment 5753

A.16.3.1.1.2 Test Parameters 5753

A.16.3.1.1.3 Test Requirements 5755

A.16.3.1.2 Intra-frequency handover from FR1 to FR1; known target cell for 2 Rx UE 5755

A.16.3.1.2.1 Test Purpose and Environment 5755

A.16.3.1.2.2 Test Parameters 5755

A.16.3.1.2.3 Test Requirements 5757

A.16.3.1.3 Intra-frequency handover from FR1 to FR1; unknown target cell for 1 Rx UE 5757

A.16.3.1.3.1 Test Purpose and Environment 5757

A.16.3.1.3.2 Test Parameters 5758

A.16.3.1.3.3 Test Requirements 5760

A.16.3.1.4 Intra-frequency handover from FR1 to FR1; unknown target cell for 2 Rx UE 5760

A.16.3.1.4.1 Test Purpose and Environment 5760

A.16.3.1.4.2 Test Parameters 5760

A.16.3.1.5 Inter-frequency handover from FR1 to FR1; unknown target cell for 1 Rx UE 5762

A.16.3.1.5.1 Test Purpose and Environment 5762

A.16.3.1.5.2 Test Parameters 5762

A.16.3.1.5.3 Test Requirements 5764

A.16.3.1.6 Inter-frequency handover from FR1 to FR1; unknown target cell for 2 Rx UE 5765

A.16.3.1.6.1 Test Purpose and Environment 5765

A.16.3.1.6.2 Test Parameters 5765

A.16.3.1.6.3 Test Requirements 5767

A.16.3.1.7 SA NR - E-UTRAN handover for 1 Rx UE 5767

A.16.3.1.7.1 Test Purpose and Environment 5767

A.16.3.1.7.2 Test Requirements 5771

A.16.3.1.8 SA NR - E-UTRAN handover for 2 Rx UE 5771

A.16.3.1.8.1 Test Purpose and Environment 5771

A.16.3.1.8.2 Test Requirements 5774

A.16.3.1.9 SA NR - E-UTRAN handover with unknown target cell for 1 Rx UE 5774

A.16.3.1.9.1 Test Purpose and Environment 5774

A.16.3.1.9.2 Test Requirements 5777

A.16.3.1.10 SA NR - E-UTRAN handover with unknown target cell for 2 Rx UE 5777

A.16.3.1.10.1 Test Purpose and Environment 5778

A.16.3.1.10.2 Test Requirements 5781

A.16.3.2 RRC Connection Mobility Control 5781

A.16.3.2.1 SA: RRC Re-establishment 5781

A.16.3.2.1.1 Intra-frequency RRC Re-establishment in FR1 for 1 Rx UE 5781

A.16.3.2.1.2 Intra-frequency RRC Re-establishment in FR1 for 2 Rx UE 5784

A.16.3.2.1.3 Inter-frequency RRC Re-establishment in FR1 for 1 Rx UE 5787

A.16.3.2.1.4 Inter-frequency RRC Re-establishment in FR1 for 2 Rx UE 5790

A.16.3.2.1.5 Intra-frequency RRC Re-establishment in FR1 for 1 Rx UE without serving cell timing 5793

A.16.3.2.1.6 Intra-frequency RRC Re-establishment in FR1 for 2 Rx UE without serving cell timing 5795

A.16.3.2.2 Random Access 5798

A.16.3.2.2.1 4-step RA type contention based random access test in FR1 for NR standalone for 1 Rx UE 5798

A.16.3.2.2.2 4-step RA type contention based random access test in FR1 for NR standalone for 2 Rx UE 5802

A.16.3.2.2.3 4-step RA type non-contention based random access test in FR1 for NR standalone for 1 Rx UE 5805

A.16.3.2.2.4 4-step RA type non-contention based random access test in FR1 for NR standalone for 2 Rx UE 5808

A.16.3.2.2.5 2-step RA type contention based random access test in FR1 for NR standalone for 1 Rx UE 5811

A.16.3.2.2.6 2-step RA type contention based random access test in FR1 for NR standalone for 2 Rx UE 5814

A.16.3.2.2.7 2-step RA type non-contention based test in FR1 for NR standalone for 1 RX UE 5817

A.16.3.2.2.8 2-step RA type non-contention based test in FR1 for NR standalone for 2 RX UE 5820

A.16.3.2.3 SA: RRC Connection Release with Redirection 5822

A.16.3.2.3.1 Redirection from NR in FR1 to NR in FR1 for 1 Rx UE 5822

A.16.3.2.3.2 Redirection from NR in FR1 to NR in FR1 for 2 Rx UE 5825

A.16.3.2.3.3 Redirection from NR in FR1 to E-UTRAN for 1 Rx UE 5827

A.16.3.2.3.4 Redirection from NR in FR1 to E-UTRAN for 2 Rx UE 5830

A.16.4 Timing for RedCap 5834

A.16.4.1 UE transmit timing 5834

A.16.4.1.1 NR UE Transmit Timing Test for FR1 for 1 Rx RedCap UE 5834

A.16.4.1.1.1 Test Purpose and environment 5834

A.16.4.1.1.2 Test requirements 5836

A.16.4.1.2 NR UE Transmit Timing Test for FR1 for 2 Rx RedCap UE 5836

A.16.4.1.2.1 Test Purpose and environment 5836

A.16.4.1.2.2 Test requirements 5838

A.16.4.2 Void 5838

A.16.4.3 Timing advance 5838

A.16.4.3.1 SA FR1 timing advance adjustment accuracy for 1 Rx UE 5838

A.16.4.3.1.1 Test Purpose and Environment 5838

A.16.4.3.1.2 Test Parameters 5838

A.16.4.3.1.3 Test Requirements 5841

A.16.4.3.2 SA FR1 timing advance adjustment accuracy for 2 Rx UE 5841

A.16.4.3.2.1 Test Purpose and Environment 5841

A.16.4.3.2.2 Test Parameters 5841

A.16.4.3.2.3 Test Requirements 5843

A.16.5 Signalling characteristics for RedCap 5844

A.16.5.1 Radio link Monitoring 5844

A.16.5.1.1 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 1 Rx UE 5844

A.16.5.1.1.1 Test Purpose and Environment 5844

A.16.5.1.1.2 Test Requirements 5846

A.16.5.1.2 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 2 Rx UE 5847

A.16.5.1.2.1 Test Purpose and Environment 5847

A.16.5.1.2.2 Test Requirements 5849

A.16.5.1.3 Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 1 Rx UE 5850

A.16.5.1.3.1 Test Purpose and Environment 5850

A.16.5.1.3.2 Test Requirements 5852

A.16.5.1.4 Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 2 Rx UE 5853

A.16.5.1.4.1 Test Purpose and Environment 5853

A.16.5.1.4.2 Test Requirements 5855

A.16.5.1.5 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 1 Rx UE 5856

A.16.5.1.5.1 Test Purpose and Environment 5856

A.16.5.1.5.2 Test Requirements 5858

A.16.5.1.6 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 2 Rx UE 5858

A.16.5.1.6.1 Test Purpose and Environment 5858

A.16.5.1.6.2 Test Requirements 5861

A.16.5.1.7 Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 1 Rx UE 5861

A.16.5.1.7.1 Test Purpose and Environment 5861

A.16.5.1.7.2 Test Requirements 5864

A.16.5.1.8 Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 2 Rx UE 5865

A.16.5.1.8.1 Test Purpose and Environment 5865

A.16.5.1.8.2 Test Requirements 5868

A.16.5.1.9 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 1 Rx UE 5868

A.16.5.1.9.1 Test Purpose and Environment 5868

A.16.5.1.9.2 Test Requirements 5871

A.16.5.1.10 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 2 Rx UE 5871

A.16.5.1.10.1 Test Purpose and Environment 5871

A.16.5.1.10.2 Test Requirements 5874

A.16.5.1.11 Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 1 Rx UE 5874

A.16.5.1.11.1 Test Purpose and Environment 5874

A.16.5.1.11.2 Test Requirements 5877

A.16.5.1.12 Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 2 Rx UE 5877

A.16.5.1.12.1 Test Purpose and Environment 5877

A.16.5.1.12.2 Test Requirements 5880

A.16.5.1.13 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 1 Rx UE 5881

A.16.5.1.13.1 Test Purpose and Environment 5881

A.16.5.1.13.2 Test Requirements 5883

A.16.5.1.14 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 2 Rx UE 5884

A.16.5.1.14.1 Test Purpose and Environment 5884

A.16.5.1.14.2 Test Requirements 5886

A.16.5.1.15 Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 1 Rx UE 5887

A.16.5.1.15.1 Test Purpose and Environment 5887

A.16.5.1.15.2 Test Requirements 5890

A.16.5.1.16 Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 2 Rx UE 5890

A.16.5.1.16.1 Test Purpose and Environment 5890

A.16.5.1.16.2 Test Requirements 5893

A.16.5.2 Beam Failure Detection and Link recovery procedures 5893

A.16.5.2.1 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for 1 Rx UE 5893

A.16.5.2.1.1 Test Purpose and Environment 5893

A.16.5.2.1.2 Test Requirements 5896

A.16.5.2.2 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for 2 Rx UE 5897

A.16.5.2.2.1 Test Purpose and Environment 5897

A.16.5.2.2.2 Test Requirements 5900

A.16.5.2.3 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode for 1 Rx UE 5900

A.16.5.2.3.1 Test Purpose and Environment 5900

A.16.5.2.3.2 Test Requirements 5903

A.16.5.2.4 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode for 2 Rx UE 5904

A.16.5.2.4.1 Test Purpose and Environment 5904

A.16.5.2.4.2 Test Requirements 5907

A.16.5.2.5 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode for 1 Rx UE 5907

A.16.5.2.5.1 Test Purpose and Environment 5907

A.16.5.2.5.2 Test Requirements 5910

A.16.5.2.6 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode for 2 Rx UE 5911

A.16.5.2.6.1 Test Purpose and Environment 5911

A.16.5.2.6.2 Test Requirements 5914

A.16.5.2.7 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode for 1 Rx UE 5914

A.16.5.2.7.1 Test Purpose and Environment 5914

A.16.5.2.7.2 Test Requirements 5917

A.16.5.2.8 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode for 2 Rx UE 5918

A.16.5.2.8.1 Test Purpose and Environment 5918

A.16.5.2.8.2 Test Requirements 5921

A.16.5.3 Active BWP switch 5921

A.16.5.3.1 DCI-based and Timer-based Active BWP Switch 5921

A.16.5.3.1.1 NR FR1 DL active BWP switch with non-DRX in SA for 1 Rx UE 5921

A.16.5.3.1.1.1 Test Purpose and Environment 5921

A.16.5.3.1.1.2 Test Requirements 5924

A.16.5.3.1.2 NR FR1 DL active BWP switch with non-DRX in SA for 2 Rx UE 5924

A.16.5.3.1.2.1 Test Purpose and Environment 5924

A.16.5.3.1.2.2 Test Requirements 5926

A.16.5.3.2 RRC-based Active BWP Switch 5927

A.16.5.3.2.1 NR FR1 DL active BWP switch of Cell with non-DRX in SA for 1 Rx UE 5927

A.16.5.3.2.1.1 Test Purpose and Environment 5927

A.16.5.3.2.1.2 Test Requirements 5929

A.16.5.3.2.2 NR FR1 DL active BWP switch of Cell with non-DRX in SA for 2 Rx UE 5929

A.16.5.3.2.2.1 Test Purpose and Environment 5929

A.16.5.3.2.2.2 Test Requirements 5931

A.16.5.4 UE specific CBW change 5932

A.16.5.4.1 UE specific CBW change on PCell in FR1 in non-DRX for 1 Rx UE 5932

A.16.5.4.1.1 Test Purpose and Environment 5932

A.16.5.4.1.2 Test Requirements 5934

A.16.5.4.2 UE specific CBW change on PCell in FR1 in non-DRX for 2 Rx UE 5934

A.16.5.4.2.1 Test Purpose and Environment 5934

A.16.5.4.2.2 Test Requirements 5937

A.16.6 Measurement procedure for RedCap 5937

A.16.6.1 Intra-frequency Measurements 5937

A.16.6.1.1 SA event triggered reporting tests without gap under non-DRX for 1 Rx UE 5937

A.16.6.1.1.1 Test purpose and Environment 5937

A.16.6.1.1.2 Test parameters 5937

A.16.6.1.1.3 Test Requirements 5939

A.16.6.1.2 SA event triggered reporting tests without gap under non-DRX for 2 Rx UE 5939

A.16.6.1.2.1 Test purpose and Environment 5939

A.16.6.1.2.2 Test parameters 5939

A.16.6.1.2.3 Test Requirements 5941

A.16.6.1.3 SA event triggered reporting tests without gap under DRX for 1 Rx UE 5941

A.16.6.1.3.1 Test purpose and Environment 5941

A.16.6.1.3.2 Test parameters 5941

A.16.6.1.3.3 Test Requirements 5943

A.16.6.1.4 SA event triggered reporting tests without gap under DRX for 2 Rx UE 5944

A.16.6.1.4.1 Test purpose and Environment 5944

A.16.6.1.4.2 Test parameters 5944

A.16.6.1.4.3 Test Requirements 5946

A.16.6.1.5 SA event triggered reporting tests with per-UE gaps under non-DRX for 1 Rx UE 5946

A.16.6.1.5.1 Test purpose and Environment 5946

A.16.6.1.5.2 Test parameters 5946

A.16.6.1.5.3 Test Requirements 5948

A.16.6.1.6 SA event triggered reporting tests with per-UE gaps under non-DRX for 2 Rx UE 5948

A.16.6.1.6.1 Test purpose and Environment 5948

A.16.6.1.6.2 Test parameters 5948

A.16.6.1.6.3 Test Requirements 5950

A.16.6.1.7 SA event triggered reporting tests with per-UE gaps under DRX for 1 Rx UE 5951

A.16.6.1.7.1 Test purpose and Environment 5951

A.16.6.1.7.2 Test parameters 5951

A.16.6.1.7.3 Test Requirements 5953

A.16.6.1.8 SA event triggered reporting tests with per-UE gaps under DRX for 2 Rx UE 5953

A.16.6.1.8.1 Test purpose and Environment 5953

A.16.6.1.8.2 Test parameters 5953

A.16.6.1.8.3 Test Requirements 5955

A.16.6.1.9 SA event triggered reporting tests without gap under non-DRX with SSB index reading for 1 Rx UE 5955

A.16.6.1.9.1 Test purpose and Environment 5955

A.16.6.1.9.2 Test parameters 5956

A.16.6.1.9.3 Test Requirements 5957

A.16.6.1.10 SA event triggered reporting tests without gap under non-DRX with SSB index reading for 2 Rx UE 5957

A.16.6.1.10.1 Test purpose and Environment 5957

A.16.6.1.10.2 Test parameters 5957

A.16.6.1.10.3 Test Requirements 5959

A.16.6.1.11 SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading for 1 Rx UE 5959

A.16.6.1.11.1 Test purpose and Environment 5959

A.16.6.1.11.2 Test parameters 5959

A.16.6.1.11.3 Test Requirements 5961

A.16.6.1.12 SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading for 2 Rx UE 5961

A.16.6.1.12.1 Test purpose and Environment 5961

A.16.6.1.12.2 Test parameters 5961

A.16.6.1.12.3 Test Requirements 5962

A.16.6.2 Inter-frequency Measurements 5963

A.16.6.2.1 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for 1 Rx UE 5963

A.16.6.2.1.1 Test Purpose and Environment 5963

A.16.6.2.1.2 Test Requirements 5965

A.16.6.2.2 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for 2 Rx UE 5966

A.16.6.2.2.1 Test Purpose and Environment 5966

A.16.6.2.2.2 Test Requirements 5968

A.16.6.2.3 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used for 1 Rx UE 5969

A.16.6.2.3.1 Test Purpose and Environment 5969

A.16.6.2.3.2 Test Requirements 5971

A.16.6.2.4 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used for 2 Rx UE 5971

A.16.6.2.4.1 Test Purpose and Environment 5971

A.16.6.2.4.2 Test Requirements 5973

A.16.6.2.5 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used for 1 Rx UE 5974

A.16.6.2.5.1 Test Purpose and Environment 5974

A.16.6.2.5.2 Test Requirements 5976

A.16.6.2.6 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used for 2 Rx UE 5976

A.16.6.2.6.1 Test Purpose and Environment 5976

A.16.6.2.6.2 Test Requirements 5978

A.16.6.2.7 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used for 1 Rx UE 5979

A.16.6.2.7.1 Test Purpose and Environment 5979

A.16.6.2.7.2 Test Requirements 5981

A.16.6.2.8 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used for 2 Rx UE 5981

A.16.6.2.8.1 Test Purpose and Environment 5981

A.16.6.2.8.2 Test Requirements 5983

A.16.6.2.9 SA event triggered reporting tests with additional mandatory gap pattern for 1 Rx UE 5984

A.16.6.2.9.1 Test Purpose and Environment 5984

A.16.6.2.9.2 Test Requirements 5986

A.16.6.2.10 SA event triggered reporting tests with additional mandatory gap pattern for 2 Rx UE 5986

A.16.6.2.10.1 Test Purpose and Environment 5986

A.16.6.2.10.2 Test Requirements 5988

A.16.6.2.11 SA event triggered reporting tests for FR1 when DRX is used for 1 Rx UE 5989

A.16.6.2.11.1 Test Purpose and Environment 5989

A.16.6.2.11.2 Test Requirements 5991

A.16.6.2.12 SA event triggered reporting tests for FR1 when DRX is used for 2 Rx UE 5991

A.16.6.2.12.1 Test Purpose and Environment 5991

A.16.6.2.12.2 Test Requirements 5994

A.16.6.3 Inter-RAT Measurements 5994

A.16.6.3.1 SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for 1 Rx UE 5994

A.16.6.3.1.1 Test purpose and Environment 5994

A.16.6.3.1.2 Test Requirements 5997

A.16.6.3.2 SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for 2 Rx UE 5998

A.16.6.3.2.1 Test purpose and Environment 5998

A.16.6.3.2.2 Test Requirements 6001

A.16.6.3.3 SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for 1 Rx UE 6001

A.16.6.3.3.1 Test purpose and Environment 6001

A.16.6.3.3.2 Test Requirements 6005

A.16.6.3.4 SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for 2 Rx UE 6005

A.16.6.3.4.1 Test purpose and Environment 6005

A.16.6.3.4.2 Test Requirements 6008

A.16.6.4 L1-RSRP measurement for beam reporting 6009

A.16.6.4.1 SSB based L1-RSRP measurement when DRX is not used for 1 Rx UE 6009

A.16.6.4.1.1 Test Purpose and Environment 6009

A.16.6.4.1.2 Test parameters 6009

A.16.6.4.1.3 Test Requirements 6010

A.16.6.4.2 SSB based L1-RSRP measurement when DRX is not used for 2 Rx UE 6011

A.16.6.4.2.1 Test Purpose and Environment 6011

A.16.6.4.2.2 Test parameters 6011

A.16.6.4.2.3 Test Requirements 6012

A.16.6.4.3 SSB based L1-RSRP measurement when DRX is used for 1 Rx UE 6012

A.16.6.4.3.1 Test Purpose and Environment 6012

A.16.6.4.3.2 Test parameters 6013

A.16.6.4.3.3 Test Requirements 6014

A.16.6.4.4 SSB based L1-RSRP measurement when DRX is used for 2 Rx UE 6014

A.16.6.4.4.1 Test Purpose and Environment 6014

A.16.6.4.4.2 Test parameters 6015

A.16.6.4.4.3 Test Requirements 6016

A.16.6.4.5 CSI-RS based L1-RSRP measurement when DRX is not used for 1 Rx UE 6016

A.16.6.4.5.1 Test Purpose and Environment 6016

A.16.6.4.5.2 Test parameters 6017

A.16.6.4.5.3 Test Requirements 6018

A.16.6.4.6 CSI-RS based L1-RSRP measurement when DRX is not used for 2 Rx UE 6018

A.16.6.4.6.1 Test Purpose and Environment 6018

A.16.6.4.6.2 Test parameters 6019

A.16.6.4.6.3 Test Requirements 6020

A.16.6.4.7 CSI-RS based L1-RSRP measurement when DRX is used for 1 Rx UE 6020

A.16.6.4.7.1 Test Purpose and Environment 6020

A.16.6.4.7.2 Test parameters 6021

A.16.6.4.7.3 Test Requirements 6022

A.16.6.4.8 CSI-RS based L1-RSRP measurement when DRX is used for 2 Rx UE 6022

A.16.6.4.8.1 Test Purpose and Environment 6022

A.16.6.4.8.2 Test parameters 6023

A.16.6.4.8.3 Test Requirements 6024

A.16.6.5 NR measurements with autonomous gaps 6025

A.16.6.5.1 SA intra-frequency CGI identification of NR neighbor cell in FR1 for 1 Rx UE 6025

A.16.6.5.1.1 Test Purpose and Environment 6025

A.16.6.5.1.2 Test Parameters 6025

A.16.6.5.1.3 Test Requirements 6027

A.16.6.5.2 SA intra-frequency CGI identification of NR neighbor cell in FR1 for 2 Rx UE 6027

A.16.6.5.2.1 Test Purpose and Environment 6027

A.16.6.5.2.2 Test Parameters 6027

A.16.6.5.2.3 Test Requirements 6029

A.16.6.5.3 Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA for 1 Rx UE 6029

A.16.6.5.3.1 Test Purpose and Environment 6029

A.16.6.5.3.2 Test Requirements 6032

A.16.6.5.4 Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA for 2 Rx UE 6032

A.16.6.5.4.1 Test Purpose and Environment 6032

A.16.6.5.4.2 Test Requirements 6035

A.16.6.6 RSTD Measurements 6035

A.16.6.6.1 NR RSTD measurement reporting delay test case for RedCap UE without FH in FR1 SA 6035

A.16.6.6.1.1 Test Purpose and Environment 6035

A.16.6.6.1.2 Test Requirements 6040

A.16.6.6.2 NR RSTD measurement reporting delay test case with PRS frequency hopping 6040

A.16.6.6.2.1 Test Purpose and Environment 6040

A.16.6.6.2.2 Test Requirements 6044

A.16.6.7 UE Rx-Tx Measurements 6045

A.16.6.7.1 UE Rx-Tx measurement reporting delay test case for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC_CONNECTED mode 6045

A.16.6.7.1.1 Test purpose and environment 6045

A.16.6.7.1.2 Test requirements 6049

A.16.6.7.2 UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR1 SA in RRC_CONNECTED state 6049

A.16.6.7.2.1 Test purpose and environment 6049

A.16.6.7.2.2 Test requirements 6053

A.16.6.8 PRS-RSRP measurements 6053

A.16.6.8.1 PRS-RSRP measurement delay test case for single positioning frequency layer 6053

A.16.6.8.1.1 Test purpose and Environment 6053

A.16.6.8.1.2 Test Requirements 6057

A.16.6.8.2 PRS-RSRP measurement delay with FH in RRC_CONNECTED state in FR1 6057

A.16.6.8.2.1 Test purpose and Environment 6057

A.16.6.8.2.2 Test Requirements 6061

A.16.6.9 PRS-RSRPP Measurements 6061

A.16.6.9.1 PRS-RSRPP measurement delay without FH in RRC_CONNECTED state in FR1 6061

A.16.6.9.1.1 Test purpose and Environment 6061

A.16.6.9.1.2 Test Requirements 6063

A.16.6.9.2 PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR1 SA in RRC_CONNECTED state 6064

A.16.6.9.2.1 Test purpose and Environment 6064

A.16.6.9.2.2 Test Requirements 6066

A.16.7 Measurement Performance requirements for RedCap 6066

A.16.7.1 SS-RSRP 6066

A.16.7.1.1 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE 6066

A.16.7.1.1.1 Test Purpose and Environment 6066

A.16.7.1.1.2 Test parameters 6066

A.16.7.1.1.3 Test Requirements 6070

A.16.7.1.2 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2 RX UE 6070

A.16.7.1.2.1 Test Purpose and Environment 6070

A.16.7.1.2.2 Test parameters 6070

A.16.7.1.2.3 Test Requirements 6074

A.16.7.1.3 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE 6074

A.16.7.1.3.1 Test Purpose and Environment 6074

A.16.7.1.3.2 Test parameters 6074

A.16.7.1.3.3 Test Requirements 6077

A.16.7.1.4 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE 6077

A.16.7.1.4.1 Test Purpose and Environment 6077

A.16.7.1.4.2 Test parameters 6077

A.16.7.1.4.3 Test Requirements 6080

A.16.7.2 SS-RSRQ 6080

A.16.7.2.1 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE 6080

A.16.7.2.1.1 Test Purpose and Environment 6080

A.16.7.2.1.2 Test Parameters 6080

A.16.7.2.1.3 Test Requirements 6084

A.16.7.2.2 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE 6084

A.16.7.2.2.1 Test Purpose and Environment 6084

A.16.7.2.2.2 Test Parameters 6084

A.16.7.2.2.3 Test Requirements 6087

A.16.7.2.3 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE 6087

A.16.7.2.3.1 Test Purpose and Environment 6087

A.16.7.2.3.2 Test parameters 6088

A.16.7.2.3.3 Test Requirements 6091

A.16.7.2.4 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE 6091

A.16.7.2.4.1 Test Purpose and Environment 6091

A.16.7.2.4.2 Test parameters 6091

A.16.7.2.4.3 Test Requirements 6095

A.16.7.3 SS-SINR 6095

A.16.7.3.1 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE 6095

A.16.7.3.1.1 Test Purpose and Environment 6095

A.16.7.3.1.2 Test parameters 6095

A.16.7.3.1.3 Test Requirements 6098

A.16.7.3.2 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE 6098

A.16.7.3.2.1 Test Purpose and Environment 6098

A.16.7.3.2.2 Test parameters 6098

A.16.7.3.3 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE 6101

A.16.7.3.3.1 Test Purpose and Environment 6101

A.16.7.3.3.2 Test parameters 6101

A.16.7.3.3.3 Test Requirements 6104

A.16.7.3.4 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE 6104

A.16.7.3.4.1 Test Purpose and Environment 6104

A.16.7.3.4.2 Test parameters 6104

A.16.7.3.4.3 Test Requirements 6107

A.16.7.4 L1-RSRP measurement for beam reporting 6108

A.16.7.4.1 SSB based L1-RSRP measurement for 1 Rx UE 6108

A.16.7.4.1.1 Test Purpose and Environment 6108

A.16.7.4.1.2 Test parameters 6108

A.16.7.4.1.3 Test Requirements 6110

A.16.7.4.2 SSB based L1-RSRP measurement for 2 Rx UE 6110

A.16.7.4.2.1 Test Purpose and Environment 6110

A.16.7.4.2.2 Test parameters 6111

A.16.7.4.2.3 Test Requirements 6111

A.16.7.4.3 CSI-RS based L1-RSRP measurement on resource set with repetition off for 1 Rx UE 6111

A.16.7.4.3.1 Test Purpose and Environment 6111

A.16.7.4.3.2 Test parameters 6111

A.16.7.4.3.3 Test Requirements 6114

A.16.7.4.4 CSI-RS based L1-RSRP measurement on resource set with repetition off for 2 Rx UE 6114

A.16.7.4.4.1 Test Purpose and Environment 6114

A.16.7.4.4.2 Test parameters 6114

A.16.7.4.4.3 Test Requirements 6114

A.16.7.5 E-UTRAN RSRP 6114

A.16.7.5.1 SA: inter-RAT measurement accuracy with FR1 serving cell for 1 Rx UE 6114

A.16.7.5.1.1 Test Purpose and Environment 6114

A.16.7.5.1.2 Test parameters 6114

A.16.7.5.1.3 Test Requirements 6118

A.16.7.5.2 SA: inter-RAT measurement accuracy with FR1 serving cell for 2 Rx UE 6118

A.16.7.5.2.1 Test Purpose and Environment 6118

A.16.7.5.2.2 Test parameters 6118

A.16.7.5.2.3 Test Requirements 6121

A.16.7.6 E-UTRAN RSRQ 6121

A.16.7.6.1 SA: inter-RAT measurement accuracy with FR1 serving cell for 1 Rx UE 6121

A.16.7.6.1.1 Test Purpose and Environment 6121

A.16.7.6.1.2 Test parameters 6121

A.16.7.6.1.3 Test Requirements 6125

A.16.7.6.2 SA: inter-RAT measurement accuracy with FR1 serving cell for 2 Rx UE 6125

A.16.7.6.2.1 Test Purpose and Environment 6125

A.16.7.6.2.2 Test parameters 6125

A.16.7.6.2.3 Test Requirements 6128

A.16.7.7 RSTD measurements 6128

A.16.7.7.1 RSTD measurement accuracy test case for RedCap UE without FH 6128

A.16.7.7.1.1 Test purpose and Environment 6128

A.16.7.7.1.2 Test Requirements 6130

A.16.7.8 UE Rx-Tx measurements 6134

A.16.7.8.1 UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC_CONNECTED mode 6134

A.16.7.8.1.1 Test purpose and environment 6134

A.16.7.8.1.2 Test parameters 6135

A.16.7.8.1.3 Test requirements 6138

A.16.7.8.2 SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_CONNECTED state in FR1 6138

A.16.7.8.2.1  Test purpose and Environment 6138

A.16.7.8.2.2 Test parameters 6139

A.16.7.8.2.3 Test requirements 6142

A.16.7.9 PRS-RSRP Measurements 6142

A.16.7.9.1 PRS-RSRP measurement accuracy without FH in RRC_CONNECTED state in FR1 6142

A.16.7.9.1.1 Test Purpose and Environment 6142

A.16.7.9.1.2 Test parameters 6142

A.16.7.9.1.3 Test Requirements 6146

A.16.7.9.2 PRS-RSRP measurement accuracy with FH in RRC_CONNECTED state in FR1 6147

A.16.7.9.2.1 Test Purpose and Environment 6147

A.16.7.9.2.2 Test parameters 6147

A.16.7.9.2.3 Test Requirements 6150

A.16.7.10 PRS-RSRPP measurements 6151

A.16.7.10.1 PRS-RSRPP measurement accuracy without FH in RRC_CONNECTED state in FR1 6151

A.16.7.10.1.1 Test Purpose and Environment 6151

A.16.7.10.1.2 Test parameters 6151

A.16.7.10.1.3 Test Requirements 6154

A.16.7.10.2 SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_CONNECTED state in FR1 6154

A.16.7.10.2.1 Test purpose and Environment 6154

A.16.7.10.2.2 Test parameters 6154

A.16.7.10.2.3 Test requirements 6158

A.16.8 Measurement Procedure for RedCap in RRC_INACTIVE 6158

A.16.8.1 RSTD Measurements 6158

A.16.8.1.1 NR RSTD measurement reporting delay test case for for RedCap UE without FH in FR1 SA in RRC_INACTIVE state 6158

A.16.8.1.1.1 Test Purpose and Environment 6158

A.16.8.1.1.2 Test Requirements 6162

A.16.8.1.2 NR RSTD measurement reporting delay test case with PRS frequency hopping 6162

A.16.8.1.2.1 Test Purpose and Environment 6162

A.16.8.1.2.2 Test Requirements 6166

A.16.8.1.3 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state when eDRX cycle > 10.24s for RedCap UE 6166

A.16.8.1.3.1 Test Purpose and Environment 6166

A.16.8.1.3.2 Test Requirements 6170

A.16.8.2 UE Rx-Tx Measurements 6170

A.16.8.2.1 UE Rx-Tx measurement reporting delay test case for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC_INACTIVE mode 6170

A.16.8.2.1.1 Test purpose and environment 6170

A.16.8.2.1.2 Test requirements 6174

A.16.8.2.2 UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR1 SA in RRC_INACTIVE state 6174

A.16.8.2.2.1 Test purpose and environment 6174

A.16.8.2.2.2 Test requirements 6178

A.16.8.2.3. UE Rx-Tx time difference measurement for single positioning frequency layer with eDRX > 10.24s in FR1 SA 6178

A.16.8.2.3.1 Test purpose and environment 6178

A.16.8.2.3.2 Test requirements 6182

A.16.8.3 PRS-RSRP Measurements 6182

A.16.8.3.1 PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_INACTIVE 6182

A.16.8.3.1.1 Test purpose and Environment 6182

A.16.8.3.1.2 Test Requirements 6184

A.16.8.3.3 PRS-RSRP reporting delay test case in RRC_INACTIVE state in FR1 when eDRX cycle > 10.24s 6185

A.16.8.3.3.1 Test purpose and Environment 6185

A.16.8.3.3.2 Test Requirements 6187

A.16.8.4 PRS-RSRPP Measurements 6188

A.16.8.4.1 PRS-RSRPP measurement delay without FH in RRC_INACTIVE state in FR1 6188

A.16.8.4.1.1 Test purpose and Environment 6188

A.16.8.4.2 PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state 6191

A.16.8.4.2.1 Test purpose and Environment 6191

A.16.8.4.2.2 Test Requirements 6193

A.16.9 Measurement Performance Requirements for RedCap in RRC_INACTIVE 6196

A.16.9.1  RSTD Measurements 6196

A.16.9.1.1 RSTD measurement accuracy test case for RedCap UE without FH in FR1 in RRC_INACTIVE state 6196

A.16.9.1.1.1 Test purpose and Environment 6196

A.16.9.1.1.2 Test Requirements 6198

A.16.9.1.2 RSTD measurement accuracy test case for RedCap UE with FH in FR1 in RRC_INACTIVE state 6198

A.16.9.1.2.1 Test purpose and Environment 6198

A.16.9.1.2.2 Test Requirements 6200

A.16.9.2 UE Rx-Tx measurements 6200

A.16.9.2.1 UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC_INACTIVE mode 6200

A.16.9.2.1.1 Test purpose and environment 6200

A.16.9.2.1.2 Test parameters 6201

A.16.9.2.1.3 Test requirements 6203

A.16.9.2.2 SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_INACTIVE state in FR1 6203

A.16.9.2.2.1 Test purpose and Environment 6203

A.16.9.2.2.2 Test parameters 6203

A.16.9.2.2.3 Test requirements 6206

A.16.9.3 PRS-RSRP Measurements 6206

A.16.9.3.1 PRS-RSRP measurement accuracy without FH in RRC_INACTIVE state in FR1 6206

A.16.9.3.1.1 Test Purpose and Environment 6206

A.16.9.3.1.2 Test parameters 6206

A.16.9.3.1.3 Test Requirements 6209

A.16.9.3.2 PRS-RSRP measurement accuracy with FH in RRC_INACTIVE state in FR1 6209

A.16.9.3.2.1 Test Purpose and Environment 6209

A.16.9.3.2.2 Test parameters 6209

A.16.9.3.2.3 Test Requirements 6212

A.16.9.4 PRS-RSRPP measurements 6212

A.16.9.4.1 PRS-RSRPP measurement accuracy without Rx FH in RRC_INACTIVE state in FR1 6212

A.16.9.4.1.1 Test purpose and Environment 6212

A.16.9.4.1.2 Test parameters 6212

A.16.9.4.1.3 Test requirements 6216

A.16.9.4.2 SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_INACTIVE state in FR1 6216

A.16.9.4.2.1 Test purpose and Environment 6216

A.16.9.4.2.2 Test parameters 6216

A.16.9.4.2.3 Test requirements 6219

A.16.10  Measurement procedure for RedCap in RRC_IDLE 6219

A.16.10.1 RSTD measurements 6219

A.16.10.1.1 NR RSTD measurement reporting delay test case for RedCap UE without FH in FR1 SA in RRC_IDLE state without eDRX 6219

A.16.10.1.1.1 Test Purpose and Environment 6219

A.16.10.1.1.2 Test Requirements 6223

A.16.10.1.2 NR RSTD measurement reporting delay test case for RedCap UE without RX FH in FR1 SA in RRC_IDLE state when eDRX > 10.24s 6223

A.16.10.1.2.1 Test Purpose and Environment 6223

A.16.10.1.2.2 Test Requirements 6227

A.16.10.2 PRS-RSRP Measurements 6227

A.16.10.2.1 PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_IDLE 6227

A.16.10.2.1.1 Test purpose and Environment 6227

A.16.10.2.1.2 Test Requirements 6229

A.16.10.2.2 PRS-RSRP measurement without Rx FH reporting delay test case for single positioning frequency layer in FR1 SA in RRC_IDLE state with eDRX cycle > 10.24s 6230

A.16.10.2.2.1 Test purpose and Environment 6230

A.16.10.2.2.2 Test Requirements 6232

A.16.11  Measurement Performance Requirements for RedCap in RRC_IDLE 6232

A.16.11.1 RSTD Measurements 6232

A.16.11.1.1 RSTD measurement accuracy test case for RedCap UE without FH in FR1 in RRC_IDLE state without eDRX 6232

A.16.11.1.1.1 Test purpose and Environment 6232

A.16.11.1.1.2 Test Requirements 6234

A.16.11.1.2 RSTD measurement accuracy test case for RedCap UE without FH in FR1 in RRC_IDLE state with eDRX > 10.24s 6235

A.16.11.1.2.1 Test purpose and Environment 6235

A.16.11.1.2.2 Test Requirements 6237

A.16.11.2 PRS-RSRP Measurements 6237

A.16.11.2.1 PRS-RSRP measurement accuracy test case for RedCap UE in FR1 in RRC_IDLE state 6237

A.16.11.2.1.1 Test Purpose and Environment 6237

A.16.11.2.1.2 Test parameters 6237

A.16.11.2.1.3 Test Requirements 6239

A.16.11.2.2 PRS-RSRP measurement without Rx FH accuracy test case for single positioning frequency layer in FR1 SA in RRC_IDLE state with eDRX cycle > 10.24s 6239

A.16.11.2.2.1 Test purpose and Environment 6239

A.16.11.2.2.2 Test Requirements 6241

A.17 NR standalone tests with one or more NR cells in FR2 for RedCap 6242

A.17.1 SA: RRC_IDLE state mobility for RedCap 6242

A.17.1.1 Cell re-selection to NR 6242

A.17.1.1.1 Cell reselection to FR2 intra-frequency NR case for 2 Rx 6242

A.17.1.1.1.1 Test Purpose and Environment 6242

A.17.1.1.1.2 Test Parameters 6242

A.17.1.1.1.3 Test Requirements 6244

A.17.1.1.2 Cell reselection to FR2 inter-frequency NR case 6244

A.17.1.1.2.1 Test Purpose and Environment 6244

A.17.1.1.2.2 Test Parameters 6244

A.17.1.1.2.3 Test Requirements 6246

A.17.1.1.3 Cell reselection to FR2 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE 6247

A.17.1.1.3.1 Test Purpose and Environment 6247

A.17.1.1.3.2 Test Parameters 6247

A.17.1.1.3.3 Test Requirements 6249

A.17.1.1.4 Cell reselection to FR2 inter-frequency NR case for UE fulfilling stationary mobility relaxed measurement criterion for 2 Rx UE 6249

A.17.1.1.4.1 Test Purpose and Environment 6249

A.17.1.1.4.2 Test Parameters 6249

A.17.1.1.4.3 Test Requirements 6251

A.17.2 SA: RRC_INACTIVE state mobility for RedCap 6252

A.17.2.1 Configured Grant based Small Data Transmissions (CG-SDT) for RedCap 6252

A.17.2.1.1 TA validation for CG-SDT in FR2 for RedCap 6252

A.17.2.1.1.1 Test Purpose and Environment 6252

A.17.2.1.1.2 Test Requirements 6255

A.17.2.2 Cell Reselection for Positioning 6255

A.17.2.2.1 Cell reselection to FR2 intra-frequency NR case with RRC_INACTIVE eDRX and positioning SRS 6255

A.17.2.2.1.1 Test Purpose and Environment 6255

A.17.2.2.1.2 Test Parameters 6255

A.17.2.2.1.3 Test Requirements 6255

A.17.3 RRC_CONNECTED state mobility for RedCap 6255

A.17.3.1 Handover for RedCap 6255

A.17.3.1.1 Intra-frequency handover from FR2 to FR2; unknown target cell for 2 Rx 6255

A.17.3.1.1.1 Test Purpose and Environment 6255

A.17.3.1.1.2 Test Parameters 6255

A.17.3.1.1.3 Test Requirements 6257

A.17.3.1.2 Inter-frequency handover from FR2 to FR2; unknown target cell for 2 Rx 6257

A.17.3.1.2.1 Test Purpose and Environment 6257

A.17.3.1.2.2 Test Parameters 6257

A.17.3.1.2.3 Test Requirements 6259

A.17.3.2 RRC Connection Mobility Control for RedCap 6259

A.17.3.2.1 SA: RRC Re-establishment 6259

A.17.3.2.1.1 Intra-frequency RRC Re-establishment in FR2 6259

A.17.3.2.1.1.1 Test Purpose and Environment 6259

A.17.3.2.1.2 Inter-frequency RRC Re-establishment in FR2 6261

A.17.3.2.1.2.1 Test Purpose and Environment 6261

A.17.3.2.1.3 Intra-frequency RRC Re-establishment in FR2 without serving cell timing 6263

A.17.3.2.1.3.1 Test Purpose and Environment 6263

A.17.3.2.1.3.2 Test Requirements 6265

A.17.3.2.2 Random Access 6265

A.17.3.2.2.1 4-step RA type contention based random access test in FR2 for NR Standalone 6265

A.17.3.2.2.1.1 Test Purpose and Environment 6265

A.17.3.2.2.1.2 Test Requirements 6267

A.17.3.2.2.2 4-step RA type non-contention based random access test in FR2 for NR Standalone 6269

A.17.3.2.2.2.1 Test Purpose and Environment 6269

A.17.3.2.2.2.2 Test Requirements 6270

A.17.3.2.2.3 2-step RA type contention based random access test in FR2 for NR Standalone 6272

A.17.3.2.2.3.1 Test Purpose and Environment 6272

A.17.3.2.2.3.2 Test Requirements 6273

A.17.3.2.2.4 2-step RA type non-contention based random access test in FR2 for NR Standalone 6274

A.17.3.2.2.4.1 Test Purpose and Environment 6274

A.17.3.2.2.4.2 Test Requirements 6276

A.17.3.2.3 SA: RRC Connection Release with Redirection 6277

A.17.3.2.3.1 Redirection from NR in FR2 to NR in FR2 6277

A.17.3.2.3.1.1 Test Purpose and Environment 6277

A.17.3.2.3.1.2 Test Parameters 6277

A.17.3.2.3.1.3 Test Requirements 6279

A.17.4 Timing 6279

A.17.4.1 UE transmit timing 6279

A.17.4.1.1 NR UE Transmit Timing Test for FR2 6279

A.17.4.1.1.1 Test Purpose and environment 6279

A.17.4.1.1.2 Test requirements 6281

A.17.4.2 UE timer accuracy 6282

A.17.4.3 Timing advance 6282

A.17.4.3.1 SA FR2 timing advance adjustment accuracy 6282

A.17.4.3.1.1 Test Purpose and Environment 6282

A.17.4.3.1.2 Test Parameters 6282

A.17.4.3.1.3 Test Requirements 6285

A.17.5 Signaling characteristics for RedCap 6285

A.17.5.1 Radio link Monitoring for RedCap 6285

A.17.5.1.1 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode 6285

A.17.5.1.1.1 Test Purpose and Environment 6285

A.17.5.1.1.2 Test Requirements 6288

A.17.5.1.2 Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode 6288

A.17.5.1.2.1 Test Purpose and Environment 6288

A.17.5.1.2.2 Test Requirements 6291

A.17.5.1.3 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode 6291

A.17.5.1.3.1 Test Purpose and Environment 6291

A.17.5.1.3.2 Test Requirements 6294

A.17.5.1.4 Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode 6294

A.17.5.1.4.1 Test Purpose and Environment 6294

A.17.5.1.4.2 Test Requirements 6296

A.17.5.1.5 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode 6297

A.17.5.1.5.1 Test Purpose and Environment 6297

A.17.5.1.5.2 Test Requirements 6299

A.17.5.1.6 Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode 6300

A.17.5.1.6.1 Test Purpose and Environment 6300

A.17.5.1.6.2 Test Requirements 6302

A.17.5.1.7 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode 6303

A.17.5.1.7.1 Test Purpose and Environment 6303

A.17.5.1.7.2 Test Requirements 6305

A.17.5.1.8 Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode 6305

A.17.5.1.8.1 Test Purpose and Environment 6305

A.17.5.1.8.2 Test Requirements 6308

A.17.5.1.9 UE Radio Link Monitoring Scheduling Restrictions on FR2 6309

A.17.5.1.9.1 Test Purpose and Environment 6309

A.17.5.1.9.2 Test Requirements 6310

A.17.5.2 Beam Failure Detection and Link recovery procedures 6311

A.17.5.2.1 Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode 6311

A.17.5.2.1.1 Test Purpose and Environment 6311

A.17.5.2.1.2 Test Requirements 6313

A.17.5.2.2 Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode 6314

A.17.5.2.2.1 Test Purpose and Environment 6314

A.17.5.2.2.2 Test Requirements 6317

A.17.5.2.3 Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode 6317

A.17.5.2.3.1 Test Purpose and Environment 6317

A.17.5.2.3.2 Test Requirements 6320

A.17.5.2.4 Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode 6320

A.17.5.2.4.1 Test Purpose and Environment 6320

A.17.5.2.4.2 Test Requirements 6323

A.17.5.2.5 Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode for 2 Rx UE 6323

A.17.5.2.5.1 Test Purpose and Environment 6323

A.17.5.2.5.2 Test Requirements 6326

A.17.5.3 Active BWP switch for RedCap 6327

A.17.5.3.1 DCI-based and Timer-based Active BWP Switch 6327

A.17.5.3.1.1 NR FR2 DL active BWP switch with non-DRX in SA 6327

A.17.5.3.1.1.1 Test Purpose and Environment 6327

A.17.5.3.1.1.2 Test Requirements 6329

A.17.5.3.2 RRC-based Active BWP Switch 6329

A.17.5.3.2.1 NR FR2 DL active BWP switch of PCell with non-DRX in SA 6329

A.17.5.3.2.1.1 Test Purpose and Environment 6329

A.17.5.3.2.1.2 Test Requirements 6332

A.17.5.4 Active TCI state switch delay 6332

A.17.5.4.1 MAC-CE based active TCI state switch 6332

A.17.5.4.1.1 NR PCell FR2 active TCI state switch for a known TCI state 6332

A.17.5.4.1.1.1 Test Purpose and Environment 6332

A.17.5.4.1.1.2 Test Requirements 6335

A.17.5.4.2 RRC based active TCI state switch 6335

A.17.5.4.2.1 NR PCell FR2 active TCI state switch for a known TCI state 6335

A.17.5.4.2.1.1 Test Purpose and Environment 6335

A.17.5.4.2.1.2 Test Requirements 6338

A.17.5.5 Uplink spatial relation switch delay 6338

A.17.5.5.1 MAC-CE based Spatial Relation switch 6338

A.17.5.5.1.1  NR PCell FR2 spatial relation associated with known DL-RS 6338

A.17.5.5.1.1.1 Test Purpose and Environment 6338

A.17.5.5.1.1.2 Test Requirements 6340

A.17.5.5.2 RRC based spatial relation switch 6341

A.17.5.5.2.1 NR PCell FR2 spatial relation switch associated with a known DL-RS 6341

A.17.5.5.2.1.2 Test Requirements 6343

A.17.5.6 UE specific CBW change 6343

A.17.5.6.1 NR FR2 UE specific CBW change of PCell with non-DRX in SA 6343

A.17.5.6.1.1 Test Purpose and Environment 6343

A.17.5.6.1.2 Test Requirements 6345

A.17.6 Measurement procedure for RedCap 6346

A.17.6.1 Intra-frequency Measurements 6346

A.17.6.1.1 SA event triggered reporting test without gap under non-DRX 6346

A.17.6.1.1.1 Test purpose and Environment 6346

A.17.6.1.1.2 Test Requirements 6348

A.17.6.1.2 SA event triggered reporting test without gap under DRX 6348

A.17.6.1.2.1 Test purpose and Environment 6348

A.7.6.1.2.2 Test Requirements 6349

A.17.6.1.3 SA event triggered reporting test with per-UE gaps under non-DRX 6349

A.17.6.1.3.1 Test purpose and Environment 6349

A.17.6.1.3.2 Test Requirements 6352

A.17.6.1.4 SA event triggered reporting test with per-UE gaps under DRX 6352

A.17.6.1.4.1 Test purpose and Environment 6352

A.17.6.1.4.2 Test Requirements 6354

A.17.6.2 Inter-frequency Measurements 6355

A.17.6.2.1 SA event triggered reporting tests For FR2 without SSB time index detection when DRX is not used (PCell in FR2) 6355

A.17.6.2.1.1 Test Purpose and Environment 6355

A.17.6.2.1.2 Test Requirements 6357

A.17.6.2.2 SA event triggered reporting tests For FR2 without SSB time index detection when DRX is used (PCell in FR2) 6357

A.17.6.2.2.1 Test Purpose and Environment 6357

A.17.6.2.2.2 Test Requirements 6359

A.17.6.2.3 SA event triggered reporting tests For FR2 with SSB time index detection when DRX is not used (PCell in FR2) 6360

A.17.6.2.3.1 Test Purpose and Environment 6360

A.17.6.2.3.2 Test Requirements 6362

A.17.6.2.4 SA event triggered reporting tests For FR2 with SSB time index detection when DRX is used (PCell in FR2) for 2 RX UE 6362

A.17.6.2.4.1 Test Purpose and Environment 6362

A.17.6.2.4.2 Test Requirements 6364

A.17.6.3 L1-RSRP measurement for beam reporting 6365

A.17.6.3.1 SSB based L1-RSRP measurement when DRX is not used 6365

A.17.6.3.1.1 Test Purpose and Environment 6365

A.17.6.3.1.2 Test parameters 6365

A.17.6.3.1.3 Test Requirements 6365

A.17.6.3.2 SSB based L1-RSRP measurement when DRX is used 6365

A.17.6.3.2.1 Test Purpose and Environment 6365

A.17.6.3.2.2 Test parameters 6366

A.17.6.3.2.3 Test Requirements 6367

A.17.6.3.3 CSI-RS based L1-RSRP measurement when DRX is not used 6367

A.17.6.3.3.1 Test Purpose and Environment 6367

A.17.6.3.3.2 Test parameters 6367

A.17.6.3.3.3 Test Requirements 6369

A.17.6.3.4 CSI-RS based L1-RSRP measurement when DRX is used 6369

A.17.6.3.4.1 Test Purpose and Environment 6369

A.17.6.3.4.2 Test parameters 6370

A.7.6.3.3.3 Test Requirements 6371

A.17.6.4.1 SA interfrequency CGI reporting in autonomous gaps test (PCell in FR2) for 2 RX UE 6371

A.17.6.4.1.1 Test Purpose and Environment 6371

A.17.6.4.1.2 Test Requirements 6374

A.17.6.5 RSTD measurements 6374

A.17.6.5.1 NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA 6374

A.17.6.5.1.1 Test Purpose and Environment 6374

A.17.6.5.1.2 Test Requirements 6381

A.17.6.5.2 NR RSTD measurement reporting delay test case with PRS frequency hopping 6381

A.17.6.5.2.1 Test Purpose and Environment 6381

A.17.6.5.2.2 Test Requirements 6386

A.17.6.6 UE Rx-Tx Measurements 6387

A.17.6.6.1 UE Rx-Tx measurement reporting delay for single positioning frequency layer in FR2 SA without RX FH in RRC_CONNECTED mode 6387

A.17.6.6.1.1 Test purpose and environment 6387

A.17.6.6.1.2 Test requirements 6391

A.17.6.6.2 UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR2 SA in RRC_CONNECTED state 6391

A.17.6.6.2.1 Test purpose and environment 6391

A.17.6.6.2.2 Test requirements 6395

A.17.6.7 PRS-RSRP measurements 6395

A.17.6.7.1 PRS-RSRP measurement delay test case for RedCap positioning without Rx FH in RRC_CONNECTED state in FR2 6395

A.17.6.7.1.1 PRS-RSRP measurement delay test case for single positioning frequency layer 6395

A.17.6.7.1.1.1 Test Purpose and Environment 6395

A.17.6.7.1.1.2 Test Requirements 6399

A.17.6.7.1.2 PRS-RSRP measurement delay test case for dual positioning frequency layer 6399

A.17.6.7.1.2.1 Test Purpose and Environment 6399

A.17.6.7.1.2.2 Test Requirements 6403

A.17.6.7.2 PRS-RSRP measurement delay with FH in RRC_CONNECTED state in FR2 6403

A.17.6.7.2.1 Test Purpose and Environment 6403

A.17.6.7.2.2 Test Requirements 6407

A.17.6.8 PRS-RSRPP Measurements 6407

A.17.6.8.1 PRS-RSRPP measurement delay without FH in RRC_CONNECTED state in FR2 6407

A.17.6.8.1.1 Test Purpose and Environment 6407

A.17.6.8.1.2 Test Requirements 6410

A.17.6.8.2 PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR2 SA in RRC_CONNECTED state 6410

A.17.6.8.2.1 Test Purpose and Environment 6410

A.17.6.8.2.2 Test Requirements 6412

A.17.7 Measurement Performance requirements 6413

A.17.7.1 SS-RSRP 6413

A.17.7.1.1 SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell 6413

A.17.7.1.1.1 Test Purpose and Environment 6413

A.17.7.1.1.2 Test parameters 6413

A.17.7.1.1.3 Test Requirements 6415

A.17.7.1.2 SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell 6415

A.17.7.1.2.1 Test Purpose and Environment 6415

A.17.7.1.2.2 Test parameters 6415

A.17.7.1.2.3 Test Requirements 6417

A.17.7.2 SS-RSRQ 6418

A.17.7.2.1 SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell 6418

A.17.7.2.1.1 Test Purpose and Environment 6418

A.17.7.2.1.2 Test Parameters 6418

A.17.7.2.1.3 Test Requirements 6420

A.17.7.2.2 SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell for 2 Rx UE 6420

A.17.7.2.2.1 Test Purpose and Environment 6420

A.17.7.2.2.2 Test parameters 6420

A.17.7.2.2.3 Test Requirements 6422

A.17.7.2.3 SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell 6422

A.17.7.3 L1-RSRP measurement for beam reporting 6422

A.17.7.3.1 SSB based L1-RSRP measurement 6422

A.17.7.3.1.1 Test Purpose and Environment 6422

A.17.7.3.1.2 Test parameters 6422

A.17.7.3.1.3 Test Requirements 6423

A.17.7.3.2 CSI-RS based L1-RSRP measurement on resource set with repetition off 6423

A.17.7.3.2.1 Test Purpose and Environment 6423

A.17.7.3.2.2 Test parameters 6423

A.17.7.3.2.3 Test Requirements 6423

A.17.7.4 SS-SINR 6424

A.17.7.4 SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell for 2Rx UE 6424

A.17.7.4.1.1 Test Purpose and Environment 6424

A.17.7.4.1.2 Test parameters 6424

A.17.7.4.1.3 Test Requirements 6426

A.17.7.5 RSTD measurements 6426

A.17.7.5.1 RSTD measurement accuracy test case for RedCap UE without FH 6426

A.17.7.5.1.1 Test purpose and Environment 6426

A.17.7.5.1.2 Test Requirements 6428

A.17.7.6 UE Rx-Tx Measurements 6430

A.17.7.6.1 UE Rx-Tx measurement accuracy for single positioning frequency layer in FR2 SA without RX FH in RRC_CONNECTED mode 6430

A.17.7.6.1.1 Test purpose and environment 6430

A.17.7.6.1.2 Test parameters 6431

A.17.7.6.1.3 Test requirements 6434

A.17.7.6.2 SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_CONNECTED state in FR2 6434

A.17.7.6.2.1 Test purpose and Environment 6434

A.17.7.6.2.2 Test parameters 6435

A.17.7.6.2.3 Test requirements 6437

A.17.7.7 PRS-RSRP Measurements 6437

A.17.7.7.1 PRS-RSRP measurement accuracy without FH in RRC_CONNECTED state in FR2 6437

A.17.7.7.1.1 Test Purpose and Environment 6437

A.17.7.7.1.2 Test parameters 6437

A.17.7.7.1.3 Test Requirements 6439

A.17.7.7.2 PRS-RSRP measurement accuracy with FH in RRC_CONNECTED state in FR2 6439

A.17.7.7.2.1 Test Purpose and Environment 6439

A.17.7.7.2.2 Test parameters 6440

A.17.7.7.2.3 Test Requirements 6442

A.17.7.8 PRS-RSRPP Measurements 6442

A.17.7.8.1 PRS-RSRPP measurement accuracy without FH in RRC_CONNECTED state in FR2 6442

A.17.7.8.1.1 Test Purpose and Environment 6442

A.17.7.8.1.2 Test parameters 6443

A.17.7.8.1.3 Test Requirements 6445

A.17.7.8.2 SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_CONNECTED state in FR2 6445

A.17.7.8.2.1 Test purpose and Environment 6445

A.17.7.8.2.2 Test parameters 6446

A.17.7.8.2.3 Test requirements 6448

A.17.8 Measurement Procedure for RedCap in RRC_INACTIVE 6449

A.17.8.1 RSTD Measurements 6449

A.17.8.1.1 NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA in RRC_INACTIVE state 6449

A.17.8.1.1.1 Test Purpose and Environment 6449

A.17.8.1.1.2 Test Requirements 6452

A.17.8.1.2 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state 6452

A.17.8.1.2.1 Test Purpose and Environment 6452

A.17.8.1.2.2 Test Requirements 6455

A.17.8.1.3 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state with eDRX > 10.24s 6455

A.17.8.1.3.1 Test purpose and environment 6455

A.17.8.1.3.2 Test requirements 6455

A.17.8.2 UE Rx-Tx Measurements 6456

A.17.8.2.1 UE Rx-Tx measurement reporting delay for single positioning frequency layer in FR2 SA without RX FH in RRC_INACTIVE mode 6456

A.17.8.2.1.1 Test purpose and environment 6456

A.17.8.2.1.2 Test requirements 6459

A.17.8.2.2 UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR2 SA in RRC_INACTIVE state 6459

A.17.8.2.2.1 Test purpose and environment 6459

A.17.8.2.2.2 Test requirements 6463

A.17.8.2.3 UE Rx-Tx time difference measurements for single positioning frequency layer with eDRX > 10.24s in FR2 SA 6463

A.17.8.2.3.1 Test purpose and environment 6463

A.17.8.2.3.2 Test requirements 6463

A.17.8.3 PRS-RSRP Measurements 6464

A.17.8.3.1 PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_INACTIVE 6464

A.17.8.3.1.1 Test Purpose and Environment 6464

A.17.8.3.1.2 Test Requirements 6468

A.17.8.3.2.2 Test Requirements 6472

A.17.8.3.3 PRS-RSRP reporting delay in RRC_INACTIVE with eDRX 6472

A.17.8.3.3.1 Test Purpose and Environment 6472

A.17.8.3.3.2 Test Requirements 6476

A.17.8.4 PRS-RSRPP Measurements 6476

A.17.8.4.1 PRS-RSRPP measurement delay without FH in RRC_INACTIVE state in FR2 6476

A.17.8.4.1.1 Test Purpose and Environment 6476

A.17.8.4.2 PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state 6479

A.17.8.4.2.1 Test Purpose and Environment 6479

A.17.8.4.2.2 Test Requirements 6481

A.17.8.4.3 PRS-RSPP reporting delay in RRC_INACTIVE state with eDRX > 10.24s 6481

A.17.8.4.3.1 Test purpose and environment 6481

A.17.8.4.3.2 Test requirements 6481

A.17.9 Measurement Performance Requirements for RedCap in RRC_INACTIVE 6482

A.17.9.1 RSTD Measurements 6482

A.17.9.1.1 RSTD measurement accuracy test case for RedCap UE without FH in FR2 in RRC_INACTIVE state 6482

A.17.9.1.1.1 Test purpose and Environment 6482

A.17.9.1.1.2 Test Requirements 6484

A.17.9.1.2 RSTD measurement accuracy test case for RedCap UE with FH in FR2 in RRC_INACTIVE state 6484

A.17.9.1.2.1 Test purpose and Environment 6484

A.17.9.1.2.2 Test Requirements 6486

A.17.9.2 UE Rx-Tx Measurements 6486

A.17.9.2.1 UE Rx-Tx measurement accuracy for single positioning frequency layer in FR2 SA without RX FH in RRC_INACTIVE mode 6486

A.17.9.2.1.1 Test purpose and environment 6486

A.17.9.2.1.2 Test parameters 6487

A.17.9.2.1.3 Test requirements 6490

A.17.9.2.2 SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_INACTIVE state in FR2 6490

A.17.9.2.2.1 Test purpose and Environment 6490

A.17.9.2.2.2 Test parameters 6490

A.17.9.2.2.3 Test requirements 6491

A.17.9.3 PRS-RSRP Measurements 6492

A.17.9.3.2 PRS-RSRP measurement accuracy with FH in RRC_INACTIVE state in FR2 6494

A.17.9.3.2.1 Test Purpose and Environment 6494

A.17.9.3.2.2 Test parameters 6495

A.17.9.3.2.3 Test Requirements 6496

A.17.9.4 PRS-RSRPP Measurements 6496

A.17.9.4.1 SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_INACTIVE state in FR2 6496

A.17.9.4.1.1 Test Purpose and Environment 6496

A.17.9.4.1.2 Test parameters 6497

A.17.9.4.1.3 Test Requirements 6499

A.17.9.4.2 SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_INACTIVE state in FR2 6499

A.17.9.4.2.1 Test Purpose and Environment 6499

A.17.9.4.2.2 Test parameters 6500

A.17.9.4.2.3 Test Requirements 6502

A.17.10 Measurement Procedure for RedCap in RRC_IDLE 6503

A.17.10.1 RSTD Measurements 6503

A.17.10.1.1 NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA in RRC_IDLE state without eDRX 6503

A.17.10.1.1.1 Test Purpose and Environment 6503

A.17.10.1.1.2 Test Requirements 6506

A.17.10.1.2 NR RSTD without FH measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s 6506

A.17.10.1.2.1 Test purpose and environment 6506

A.17.10.1.2.2 Test requirements 6506

A.17.10.2 PRS-RSRP Measurements 6507

A.17.10.2.1 PRS-RSRP measurement delay test case for single positioning frequency layer in RRC_IDLE 6507

A.17.10.2.1.1 Test Purpose and Environment 6507

A.17.10.2.1.2 Test Requirements 6511

A.17.10.2.2 PRS-RSRP reporting delay test case in RRC_IDLE state in FR2 when eDRX cycle > 10.24s 6511

A.17.10.2.2.1 Test Purpose and Environment 6511

A.17.10.2.2.2 Test Requirements 6511

A.17.11  Measurement Performance Requirements for RedCap in RRC_IDLE 6512

A.17.11.1 RSTD Measurements 6512

A.17.11.1.1 RSTD measurement accuracy test case for RedCap UE without FH in FR2 in RRC_IDLE state without eDRX 6512

A.17.11.1.1.1 Test purpose and Environment 6512

11.1.1.2 Test Requirements 6514

A.17.11.1.2 RSTD without FH measurement accuracy test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s 6514

A.17.11.1.2.1 Test purpose and environment 6514

A.17.11.1.2.2 Test requirements 6516

A.17.11.2 PRS-RSRP Measurements 6516

A.17.11.2.1 PRS-RSRP measurement accuracy test case for RedCap UE in FR2 in RRC_IDLE state 6516

A.17.11.2.1.1 Test Purpose and Environment 6516

A.17.11.2.1.2 Test parameters 6516

A.17.11.2.2 PRS-RSRP measurement accuracy test case in RRC_IDLE state in FR2 when eDRX cycle > 10.24s 6518

A.17.11.2.2.1 Test purpose and Environment 6518

A.17.11.2.2.1 Test parameters 6519

A.17.11.2.2.2 Test Requirements 6519

A.18 E-UTRA standalone tests for NR RRM for RedCap 6519

A.18.1 RRC_IDLE state mobility 6519

A.18.1.1 Inter-RAT NR Cell re-selection 6519

A.18.1.1.1 E-UTRA Cell reselection to higher priority NR target Cell in FR1 6519

A.18.1.1.1.1 Test Purpose and Environment 6519

A.18.1.1.1.2 Test Requirements 6522

A.18.2 RRC_CONNECTED state mobility 6522

A.18.2.1 Handover 6522

A.18.2.1.1 E-UTRAN - NR handover in FR1 6522

A.18.2.1.1.1 Test Purpose and Environment 6522

A.18.2.1.1.2 Test Requirements 6526

A.18.2.2 RRC connection release with redirection 6526

A.18.2.2.1 Redirection from E-UTRA to NR FR1 for redcap UE 6526

A.18.2.2.1.1 Test Purpose and Environment 6526

A.18.2.2.1.2 Test Parameters 6526

A.18.2.2.1.3 Test Requirements 6529

A.18.3 Measurement procedure 6530

A.18.3.1 E-UTRA – NR Inter-RAT Measurements 6530

A.18.3.1.1 NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used 6530

A.18.3.1.1.1 Test Purpose and Environment 6530

A.18.3.1.1.2 Test Requirements 6533

A.18.3.1.2 NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used 6533

A.18.3.1.2.1 Test Purpose and Environment 6533

A.18.3.1.2.2 Test Requirements 6537

A.18.3.1.3 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used 6537

A.18.3.1.3.1 Test Purpose and Environment 6537

A.18.3.1.3.2 Test Requirements 6541

A.18.3.1.4 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used 6541

A.18.3.1.4.1 Test Purpose and Environment 6541

A.18.3.1.4.2 Test Requirements 6545

A.18.3.1.5 NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is not used 6545

A.18.3.1.5.1 Test Purpose and Environment 6545

A.18.3.1.5.2 Test Requirements 6547

A.18.3.1.6 NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is used 6547

A.18.3.1.6.1 Test Purpose and Environment 6547

A.18.3.1.6.2 Test Requirements 6549

A.18.3.1.7 NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is not used 6550

A.18.3.1.7.1 Test Purpose and Environment 6550

A.18.3.1.7.2 Test Requirements 6551

A.18.3.1.8 NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is used 6552

A.18.3.1.8.1 Test Purpose and Environment 6552

A.18.3.1.8.2 Test Requirements 6554

A.19 NR standalone tests for ATG 6555

A.19.1 RRC_IDLE state mobility 6555

A.19.1.1 Cell reselection to FR1 intra-frequency NR case 6555

A.19.1.1.1 Test Purpose and Environment 6555

A.19.1.1.2 Test Parameters 6555

A.19.1.1.3 Test Requirements 6556

A.19.1.2 Cell reselection to FR1 inter-frequency NR case 6556

A.19.1.2.1 Test Purpose and Environment 6556

A.19.1.2.2 Test Parameters 6556

A.19.1.2.3 Test Requirements 6558

A.19.1.3 Cell reselection to FR1 inter-frequency NR case for UE configured with hs-ATG-cellReselectionSet-r18 6559

A.19.1.3.1 Test Purpose and Environment 6559

A.19.1.3.2 Test Parameters 6559

A.19.1.3.3 Test Requirements 6561

A.19.2 RRC_CONNECTED state mobility 6561

A.19.2.1 Handover 6561

A.19.2.1.1 Intra-frequency handover from FR1 to FR1; known target cell 6561

A19.2.1.1.1 Test Purpose and Environment 6561

A.19.2.1.1.2 Test Parameters 6561

A.19.2.1.2.3 Test Requirements 6562

A.19.2.1.2 Inter-frequency handover from FR1 to FR1; unknown target cell 6562

A.19.2.1.2.1 Test Purpose and Environment 6562

A.19.2.1.2.2 Test Parameters 6562

A.19.2.1.2.3 Test Requirements 6563

A.19.2.2 Conditional Handover 6563

A.19.2.2.1 Intra-frequency distance-based conditional Handover from FR1 to FR1 6563

A.19.2.2.1.1 Test Purpose and Environment 6563

A.19.2.2.1.2 Test Parameters 6564

A.19.2.2.1.3 Test Requirements 6566

A.19.2.2.2 Inter-frequency distance-based conditional Handover from FR1 to FR1 6566

A.19.2.2.2.1 Test Purpose and Environment 6566

A.19.2.2.2.2 Test Parameters 6566

A.19.2.2.2.3 Test Requirements 6568

A.19.2.3 RRC Connection Mobility Control 6569

A.19.2.3.1 SA: RRC Re-establishment 6569

A.19.2.3.1.1 Intra-frequency RRC Re-establishment in FR1 for ATG 6569

A.19.2.3.1.1.1 Test Purpose and Environment 6569

A.19.2.3.1.1.2 Test Requirements 6570

A.19.2.3.1.2 Inter-frequency RRC Re-establishment in FR1 with unknown target cell without serving cell timing for ATG 6570

A.19.2.3.1.2.1 Test Purpose and Environment 6570

A.19.2.3.1.2.2 Test Requirements 6572

A.19.2.3.2 Random Access for ATG UE 6573

A.19.2.3.2.1.1 Test Purpose and Environment 6573

A.19.2.3.2.1.2 Test Requirements 6573

A.19.2.3.2.2.1 Test Purpose and Environment 6573

A.19.2.3.2.2.2 Test Requirements 6574

A.19.2.3.2.3 2-step RA type contention based random access test in FR1 for NR standalone 6574

A.19.2.3.2.3.1 Test Purpose and Environment 6574

A.19.2.3.2.3.2 Test Requirements 6575

A.19.2.3.2.4 2-step RA type non-contention based test in FR1 for NR standalone 6575

A.19.2.3.2.4.1 Test Purpose and Environment 6575

A.19.2.3.2.4.2 Test Requirements 6575

A.19.2.3.3.1.1 Test Purpose and Environment 6575

A.19.2.3.3.1.2 Test Parameters 6575

A.19.2.3.3.1.3 Test Requirements 6576

A.19.3 Timing 6577

A.19.3.1 UE transmit timing 6577

A.19.3.1.1 ATG UE Transmit Timing Test for FR1 6577

A.19.3.1.1.1 Test Purpose and environment 6577

A.19.3.1.1.2 Test requirements 6578

A.19.3.2 UE timer accuracy 6579

A.19.3.3 Timing advance 6579

A.19.3.3.1 SA FR1 timing advance adjustment accuracy 6579

A.19.3.3.1.1 Test Purpose and Environment 6579

A.19.3.3.1.2 Test Parameters 6579

A.19.3.3.1.3 Test Requirements 6580

A.19.4 Signalling characteristics 6580

A.19.4.1 Radio link Monitoring 6580

A.19.4.1.1 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode 6580

A.19.4.1.1.1 Test Purpose and Environment 6580

A.19.4.1.1.2 Test Requirements 6583

A.19.4.1.2 Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode 6583

A.19.4.1.2.1 Test Purpose and Environment 6583

A.19.4.1.2.2 Test Requirements 6586

A.19.4.1.3 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode 6586

A.19.4.1.3.1 Test Purpose and Environment 6586

A.19.4.1.3.2 Test Requirements 6589

A.19.4.1.4 Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode 6590

A.19.4.1.4.1 Test Purpose and Environment 6590

A.19.4.1.4.2 Test Requirements 6593

A.19.4.2 Beam Failure Detection and Link recovery procedures 6593

A.19.4.2.1 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode 6593

A.19.4.2.1.1 Test Purpose and Environment 6593

A.19.4.2.1.2 Test Requirements 6597

A.19.4.2.2 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode 6597

A.19.4.2.2.1 Test Purpose and Environment 6597

A.19.4.2.2.2 Test Requirements 6601

A.19.4.2.3 Beam Failure Detection and Link Recovery Test for FR1 SCell configured with with CSI-RS-based BFD and SSB-based LR in non-DRX mode 6601

A.19.4.2.3.1 Test Purpose and Environment 6601

A.19.4.2.3.2 Test Requirements 6602

A.19.4.3 Active BWP switch 6602

A.19.4.3.1 DCI-based and Timer-based Active BWP Switch 6602

A.19.4.3.1.1 NR FR1 DL active BWP switch with non-DRX in SA 6602

A.19.4.3.2 RRC-based Active BWP Switch 6605

A.19.4.3.2.1 NR FR1 DL active BWP switch of Cell with non-DRX in SA 6605

A.19.4.4 UE specific CBW change 6607

A19.4.4.1 UE specific CBW change on PCell in FR1 in non-DRX 6607

A19.4.4.1.1 Test Purpose and Environment 6608

A.19.4.4.1.2 Test Requirements 6610

A.19.4.5 Pathloss reference signal switching delay 6610

A.19.4.5.1 MAC-CE based pathloss reference signal switch delay 6610

A.19.4.5.1.1 Test Purpose and Environment 6610

A.19.4.5.1.2 Test Requirements 6612

A.19.4.6 Interruption 6613

A.19.4.6.1 SA interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in NR-CA 6613

A.19.4.6.1.1 Test Purpose and Environment 6613

A.19.4.6.1.2 Test Parameters 6613

A.19.4.6.1.3 Test Requirements 6615

A.19.4.6.2 SA interruptions at NR SRS antenna port switching with more than 1 SRS symbol in a slot in NR-CA 6615

A.19.4.6.2.1 Test Purpose and Environment 6615

A.19.4.6.2.2 Test Parameters 6615

A.19.4.6.2.3 Test Requirements 6617

A.19.4.7 SCell Activation and Deactivation Delay for ATG 6618

A.19.4.7.1 SCell Activation and deactivation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle 6618

A.19.4.7.1.1 Test Purpose and Environment 6618

A.19.4.7.1.2 Test Requirements 6622

A.19.4.7.2 SCell Activation and deactivation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle 6623

A.19.4.7.2.1 Test Purpose and Environment 6623

A.19.4.7.2.2 Test Requirements 6623

A.19.4.7.3 SCell Activation and deactivation of unknown SCell in FR1 in non-DRX 6623

A.19.4.7.3.1 Test Purpose and Environment 6623

A.19.4.7.3.2 Test Requirements 6624

A.19.4.7.4 Direct SCell activation at SCell addition of known SCell in FR1 6624

A.19.4.7.4.1 Test Purpose and Environment 6624

A.19.4.7.4.2 Test Requirements 6628

A.19.4.7.5 Direct SCell activation at handover with known SCell in FR1 6628

A.19.4.7.5.1 Test Purpose and Environment 6628

A.19.4.7.5.2 Test Requirements 6632

A.19.4.7.6 Fast SCell Activation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle 6633

A.19.4.7.6.1 Test Purpose and Environment 6633

A.19.4.7.6.2 Test Requirements 6634

A.19.4.7.7 Fast SCell Activation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle 6634

A.19.4.7.7.1 Test Purpose and Environment 6634

A.19.4.7.7.2 Test Requirements 6635

A.19.4.7.8 SCell Activation of unknown SCell with valid L3 measurement results in FR1 in non-DRX for 160 ms SCell measurement cycle 6635

A.19.4.7.8.1 Test Purpose and Environment 6635

A.19.4.7.8.2 Test Requirements 6640

A.19.4.7.9 TRS based SCell Activation of SSB-less SCell in FR1 inter-band CA in non-DRX for ATG 6640

A.19.4.7.9.1 Test Purpose and Environment 6640

A.19.4.7.9.2 Test Requirements 6642

A.19.5 Measurement procedure 6642

A.19.5.1 Intra-frequency Measurements 6642

A.19.5.1.1 SA event triggered reporting tests without gap without SSB index reading under non-DRX 6642

A.19.5.1.1.1 Test purpose and Environment 6642

A.19.5.1.1.2 Test parameters 6642

A.19.5.1.1.3 Test Requirements 6643

A.19.5.1.2 SA event triggered reporting tests with per-UE gaps under non-DRX 6643

A.19.5.1.2.1 Test purpose and Environment 6643

A.19.5.1.2.2 Test parameters 6643

A.19.5.1.2.3 Test Requirements 6643

A.19.5.1.3 SA event triggered reporting tests without gap under non-DRX with SSB index reading 6644

A.19.5.1.3.1 Test purpose and Environment 6644

A.19.5.1.3.2 Test parameters 6644

A.19.5.1.3.3 Test Requirements 6644

A.19.5.1.4 SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading 6644

A.19.5.1.4.1 Test purpose and Environment 6644

A.19.5.1.4.2 Test parameters 6645

A.19.5.1.4.3 Test Requirements 6645

A.19.5.1.5 Event triggered reporting tests on SCC with deactivated SCell under non-DRX with measurement cycle of 640ms 6645

A.19.5.1.5.1 Test purpose and Environment 6645

A.19.5.1.5.2 Test parameters 6645

A.19.5.1.5.3 Test Requirements 6648

A.19.5.2 Inter-frequency Measurements 6648

A.19.5.2.1.2 Test parameters 6648

A.19.5.2.1.3 Test Requirements 6650

A.19.5.2.2.2 Test parameters 6650

A.19.5.2.3.2 Test parameters 6651

A.19.5.2.3.3 Test Requirements 6651

A.19.5.3 L1-RSRP measurement for beam reporting for ATG 6651

A.19.5.3.1 SSB based L1-RSRP measurement when DRX is not used 6651

A.19.5.3.1.1 Test Purpose and Environment 6651

A.19.5.3.1.2 Test parameters 6652

A.19.5.3.1.3 Test Requirements 6652

A.19.5.3.2 CSI-RS based L1-RSRP measurement when DRX is not used 6652

A.19.5.3.2.1 Test Purpose and Environment 6652

A.19.5.3.2.2 Test parameters 6652

A.19.5.3.2.3 Test Requirements 6653

A.19.5.4 L1-SINR measurement for beam reporting for ATG 6653

A.19.5.4.1 L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is not used 6653

A.19.5.4.1.3 Test Requirements 6653

A.19.5.4.2 L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used 6653

A.19.5.4.2.1 Test Purpose and Environment 6653

A.19.5.4.2.2 Test parameters 6654

A.19.5.4.2.3 Test Requirements 6654

A.19.5.4.3 L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used 6654

A.19.5.4.3.1 Test Purpose and Environment 6654

A.19.5.4.3.2 Test parameters 6654

A.19.5.4.3.3 Test Requirements 6655

A.19.5.5 NR measurements with autonomous gaps for ATG 6655

A.19.5.5.1 SA intra-frequency CGI identification of NR neighbor cell in FR1 6655

A.19.5.5.1.1 Test Purpose and Environment 6655

A.19.5.5.1.2 Test Parameters 6655

A.19.5.5.1.3 Test Requirements 6656

A.19.6 Measurement Performance requirements 6656

A.19.6.1 SS-RSRP for ATG UE 6656

A.19.6.1.1 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell 6656

A.19.6.1.1.1 Test Purpose and Environment 6656

A.19.6.1.1.2 Test parameters 6656

A.19.6.1.1.3 Test Requirements 6657

A.19.6.1.2 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell 6657

A.19.6.1.2.1 Test Purpose and Environment 6657

A.19.6.1.2.2 Test parameters 6657

A.19.6.1.2.3 Test Requirements 6657

A.19.6.2 SS-RSRQ for ATG UE 6657

A.19.6.2.1 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 6658

A.19.6.2.1.1 Test Purpose and Environment 6658

A.19.6.2.1.2 Test Parameters 6658

A.19.6.2.1.3 Test Requirements 6658

A.19.6.2.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 6658

A.19.6.2.2.1 Test Purpose and Environment 6658

A.19.6.2.2.2 Test Parameters 6658

A.19.6.2.2.3 Test Requirements 6659

A.19.6.3 SS-SINR for ATG UE 6659

A.19.6.3.1 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 6659

A.19.6.3.1.1 Test Purpose and Environment 6659

A.19.6.3.1.2 Test Parameters 6659

A.19.6.3.1.3 Test Requirements 6660

A.19.6.3.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 6660

A.19.6.3.2.1 Test Purpose and Environment 6660

A.19.6.3.2.2 Test Parameters 6660

A.19.6.3.2.3 Test Requirements 6660

A.19.6.4 L1-RSRP measurement for beam reporting for ATG UE 6660

A.19.6.4.1 SSB based L1-RSRP measurement 6660

A.19.6.4.1.1 Test Purpose and Environment 6660

A.19.6.4.1.2 Test parameters 6661

A.19.6.4.1.3 Test Requirements 6661

A.19.6.4.2 CSI-RS based L1-RSRP measurement on resource set with repetition off 6661

A.19.6.4.2.1 Test Purpose and Environment 6661

A.19.6.4.2.2 Test parameters 6661

A.19.6.4.2.3 Test Requirements 6662

A.19.6.5 L1-SINR measurement for beam reporting based CMR for ATG UE 6662

A.19.6.5.1 L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured and CSI-RS resource set with repetition off 6662

A.19.6.5.1.1 Test Purpose and Environment 6662

A.19.6.5.1.2 Test parameters 6662

A.19.6.5.1.3 Test Requirements 6662

A.19.6.5.2 L1-SINR measurement with SSB based CMR and dedicated IMR 6662

A.19.6.5.2.1 Test Purpose and Environment 6663

A.19.6.5.2.2 Test parameters 6663

A.19.6.5.2.3 Test Requirements 6663

A.19.6.5.3 L1-SINR measurement with CSI-RS based CMR and dedicated IMR 6663

A.19.6.5.3.1 Test Purpose and Environment 6663

A.19.6.5.3.2 Test parameters 6664

A.19.6.5.3.3 Test Requirements 6664

A.19.6.6 CSI-RSRP for ATG UE 6664

A.19.6.6.1 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell 6664

A.19.6.6.1.1 Test Purpose and Environment 6664

A.19.6.6.1.2 Test parameters 6664

A.19.6.6.1.3 Test Requirements 6665

A.19.6.6.2 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell 6665

A.19.6.6.2.1 Test Purpose and Environment 6665

A.19.6.6.2.2 Test parameters 6665

A.19.6.6.2.3 Test Requirements 6665

A.19.6.7 CSI-RSRQ for ATG UE 6665

A.19.6.7.1 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 6665

A.19.6.7.1.1 Test Purpose and Environment 6665

A.19.6.7.1.2 Test Parameters 6666

A.19.6.7.1.3 Test Requirements 6666

A.19.6.7.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 6666

A.19.6.7.2.1 Test Purpose and Environment 6666

A.19.6.7.2.2 Test Parameters 6666

A.19.6.7.2.3 Test Requirements 6667

A.19.6.8 CSI-SINR for ATG UE 6667

A.19.6.8.1 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell 6667

A.19.6.8.1.1 Test Purpose and Environment 6667

A.19.6.8.1.2 Test Parameters 6667

A.19.6.8.1.3 Test Requirements 6667

A.19.6.8.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell 6668

A.19.6.8.2.1 Test Purpose and Environment 6668

A.19.6.8.2.2 Test Parameters 6668

A.19.6.8.2.3 Test Requirements 6668

A.20 NR standalone tests for RedCap UE with Satellite Access 6668

A.20.1 RRC_IDLE state mobility 6668

A.20.1.1 Cell reselection to FR1 intra-frequency NR case for 1Rx RedCap UE 6668

A.20.1.1.1 Test Purpose and Environment 6668

A.20.1.1.2 Test Parameters 6668

A.20.1.1.3 Test Requirements 6669

A.20.1.2 Cell reselection to FR1 intra-frequency NR case  for 2Rx RedCap UE 6669

A.20.1.2.1 Test Purpose and Environment 6669

A.20.1.2.2 Test Parameters 6669

A.20.1.2.3 Test Requirements 6669

A.20.1.3 Cell reselection to FR1 intra-frequency NR cell for 1Rx RedCap UE configured with the feature for enhanced requirements 6669

A.20.1.3.1 Test Purpose and Environment 6669

A.20.1.3.2 Test Parameters 6670

A.20.1.3.3 Test Requirements 6670

A.20.1.4 Cell reselection to FR1 intra-frequency NR cell for 2Rx RedCap UE configured with the feature for enhanced requirements 6670

A.20.1.4.1 Test Purpose and Environment 6670

A.20.1.4.2 Test Parameters 6670

A.20.1.4.3 Test Requirements 6670

A.20.1.5 Time-based measurement initiation to FR1 intra-frequency NR cell reselection for 1Rx RedCap UE 6670

A.20.1.5.1 Test Purpose and Environment 6670

A.20.1.5.2 Test Parameters 6670

A.20.1.5.3 Test Requirements 6671

A.20.1.6 Time-based measurement initiation to FR1 intra-frequency NR cell reselection for 2Rx RedCap UE 6671

A.20.1.6.1 Test Purpose and Environment 6671

A.20.1.6.2 Test Parameters 6671

A.20.1.6.3 Test Requirements 6671

A.20.1.7 Location-based measurement initiation to FR1 inter-frequency NR cell reselection for 1Rx RedCap UE 6671

A.20.1.7.1 Test Purpose and Environment 6671

A.20.1.7.2 Test Parameters 6671

A.20.1.7.3 Test Requirements 6672

A.20.1.8 Location-based measurement initiation to FR1 inter-frequency NR cell reselection for 2Rx RedCap UE 6672

A.20.1.8.1 Test Purpose and Environment 6672

A.20.1.8.2 Test Parameters 6672

A.20.1.8.3 Test Requirements 6672

A.20.1.9 Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion for 1Rx RedCap UE 6673

A.20.1.9.1 Test Purpose and Environment 6673

A.20.1.9.2 Test Parameters 6673

A.20.1.9.3 Test Requirements 6674

A.20.1.10 Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion for 2Rx RedCap UE 6674

A.20.1.10.1 Test Purpose and Environment 6674

A.20.1.10.2 Test Parameters 6675

A.20.1.10.3 Test Requirements 6675

A.20.1.11 Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion for 1Rx RedCap UEs 6675

A.20.1.11.1 Test Purpose and Environment 6675

A.20.1.11.2 Test Parameters 6675

A.20.1.11.3 Test Requirements 6677

A.20.1.12 Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion for 2Rx RedCap UEs 6677

A.20.1.12.1 Test Purpose and Environment 6677

A.20.1.12.2 Test Parameters 6677

A.20.1.12.3 Test Requirements 6678

A.20.1.13 Cell reselection to FR1 inter-RAT for NR NTN carrier for 1Rx RedCap UE 6678

A.20.1.13.1 Test purpose and Environment 6678

A.20.1.13.2 Test Parameters 6678

A.20.1.13.3 Test requirements 6680

A.20.1.14 Cell reselection to FR1 inter-RAT for NR NTN carrier for 2Rx RedCap UE 6680

A.20.1.14.1 Test purpose and Environment 6680

A.20.1.14.2 Test Parameters 6680

A.20.1.14.3 Test requirements 6681

A.20.1.15 Cell re-selection to FR1 inter-frequency NR case with TN carrier for 1Rx RedCap UE 6681

A.20.1.15.1 Test purpose and Environment 6681

A.20.1.15.2 Test parameters 6681

A.20.1.15.3 Test requirements 6683

A.20.1.16 Cell re-selection to FR1 inter-frequency NR case with TN carrier for 2Rx RedCap UE 6683

A.20.1.16.1 Test purpose and Environment 6683

A.20.1.16.2 Test parameters 6683

A.20.1.16.3 Test requirements 6683

A.20.2 RRC_CONNECTED state mobility 6683

A.20.2.1 Handover 6683

A.20.2.1.1 Intra-frequency SAN Handover from FR1 to FR1 for 1Rx RedCap UE 6683

A.20.2.1.1.1 Test Purpose and Environment 6683

A.20.2.1.1.2 Test Parameters 6684

A.20.2.1.1.3 Test Requirements 6684

A.20.2.1.2 Intra-frequency SAN Handover from FR1 to FR1 for 2Rx RedCap UE 6684

A.20.2.1.2.1 Test Purpose and Environment 6684

A.20.2.1.2.2 Test Parameters 6684

A.20.2.1.2.3 Test Requirements 6684

A.20.2.1.3 Inter-frequency SAN Handover from FR1 to FR1 for 1Rx RedCap UE 6684

A.20.2.1.3.1 Test Purpose and Environment 6684

A.20.2.1.3.2 Test Parameters 6685

A.20.2.1.3.3 Test Requirements 6685

A.20.2.1.4 Inter-frequency SAN Handover from FR1 to FR1 for 2Rx RedCap UE 6685

A.20.2.1.4.1 Test Purpose and Environment 6685

A.20.2.1.4.2 Test Parameters 6685

A.20.2.1.4.3 Test Requirements 6685

A.20.2.1.5 Intra-frequency SAN RACH-less Handover from FR1 to FR1 for 1Rx RedCap UE 6685

A.20.2.1.5.1 Test Purpose and Environment 6685

A.20.2.1.5.2 Test Parameters 6685

A.20.2.1.5.3 Test Requirements 6685

A.20.2.1.6 Intra-frequency SAN RACH-less Handover from FR1 to FR1 for 2Rx RedCap UE 6685

A.20.2.1.6.1 Test Purpose and Environment 6685

A.20.2.1.6.2 Test Parameters 6686

A.20.2.1.6.3 Test Requirements 6686

A.20.2.1.7 Intra-frequency SAN time-based conditional Handover from FR1 to FR1 for 1Rx RedCap UE 6686

A.20.2.1.7.1 Test Purpose and Environment 6686

A.20.2.1.7.2 Test Parameters 6686

A.20.2.1.7.3 Test Requirements 6686

A.20.2.1.8 Intra-frequency SAN time-based conditional Handover from FR1 to FR1 for 2Rx RedCap UE 6686

A.20.2.1.8.1 Test Purpose and Environment 6686

A.20.2.1.8.2 Test Parameters 6687

A.20.2.1.8.3 Test Requirements 6687

A.20.2.1.9 Inter-frequency SAN distance-based conditional Handover from FR1 to FR1 for 1Rx RedCap UE 6687

A.20.2.1.9.1 Test Purpose and Environment 6687

A.20.2.1.9.2 Test Parameters 6687

A.20.2.1.9.3 Test Requirements 6687

A.20.2.1.10 Inter-frequency SAN distance-based conditional Handover from FR1 to FR1 for 2Rx RedCap UE 6687

A.20.2.1.10.1 Test Purpose and Environment 6687

A.20.2.1.10.2 Test Parameters 6687

A.20.2.1.10.3 Test Requirements 6687

A.20.2.1.11 Intra-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 1Rx RedCap UE 6687

A.20.2.1.11.1 Test Purpose and Environment 6687

A.20.2.1.11.2 Test Parameters 6687

A.20.2.1.11.3 Test Requirements 6688

A.20.2.1.12 Intra-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 2Rx RedCap UE 6688

A.20.2.1.12.1 Test Purpose and Environment 6688

A.20.2.1.12.2 Test Parameters 6688

A.20.2.1.12.3 Test Requirements 6688

A.20.2.1.13 Inter-frequency SAN distance-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 1Rx RedCap UE 6688

A.20.2.1.13.1 Test Purpose and Environment 6688

A.20.2.1.13.2 Test Parameters 6688

A.20.2.1.13.3 Test Requirements 6689

A.20.2.1.14 Inter-frequency SAN distance-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 2Rx RedCap UE 6689

A.20.2.1.14.1 Test Purpose and Environment 6689

A.20.2.1.14.2 Test Parameters 6689

A.20.2.1.14.3 Test Requirements 6689

A.20.2.2 RRC Connection Mobility Control 6690

A.20.2.2.1 SA: RRC Re-establishment for SAN 6690

A.20.2.2.1.1 Intra-frequency RRC Re-establishment in FR1 for 1 Rx RedCap UE 6690

A.20.2.2.1.2 Intra-frequency RRC Re-establishment in FR1 for 2 Rx RedCap UE 6692

A.20.2.2.1.3 Inter-frequency RRC Re-establishment in FR1 for 1 Rx RedCap UE 6694

A.20.2.2.1.4 Inter-frequency RRC Re-establishment in FR1 for 2 Rx RedCap UE 6696

A.20.2.2.2 Random Access 6699

A.20.2.2.2.1 4-step RA type contention based random access test in FR1 for NR standalone for 1 Rx RedCap UE 6699

A.20.2.2.2.2 4-step RA type contention based random access test in FR1 for NR standalone for 2 Rx RedCap UE 6702

A.20.2.2.2.3 4-step RA type non-contention based random access test in FR1 for NR standalone for 1 Rx RedCap UE 6705

A.20.2.2.2.4 4-step RA type non-contention based random access test in FR1 for NR standalone for 2 Rx RedCap UE 6707

A.20.2.2.3 RRC Connection Release with Redirection 6710

A.20.2.2.3.1 Redirection from NR in FR1 to NR in FR1 for 1 Rx RedCap UE 6710

A.20.2.2.3.2 Redirection from NR in FR1 to NR in FR1 for 2 Rx RedCap UE 6713

A.20.2.3 Satellite switching with re-synchronization from FR1 to FR1 for RedCap UE with Satellite Access 6715

A.20.2.3.1 RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 for RedCap UEs with 2Rx RedCap UE 6715

A.20.2.3.1.1 Test Purpose and Environment 6715

A.20.2.3.1.2 Test Parameters 6715

A.20.2.3.1.3 Test Requirements 6717

A.20.2.3.2 RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 for RedCap UEs with 1 Rx RedCap UE 6717

A.20.2.3.2.1 Test Purpose and Environment 6717

A.20.2.3.2.2 Test Parameters 6717

A.20.2.3.2.3 Test Requirements 6719

A.20.2.3.3 RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1 for 2Rx RedCap UEs 6720

A.20.2.3.3.1 Test Purpose and Environment 6720

A.20.2.3.3.2 Test Parameters 6720

A.20.2.3.3.3 Test Requirements 6722

A.20.2.3.4 RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1 for 1Rx RedCap UEs 6722

A.20.2.3.4.1 Test Purpose and Environment 6722

A.20.2.3.4.2 Test Parameters 6722

A.20.2.3.4.3 Test Requirements 6722

A.20.3 Timing for RedCap UE with Satellite Access 6723

A.20.3.1 UE transmit timing for RedCap UE with Satellite Access 6723

A.20.3.1.1 NR UE Transmit Timing Test for FR1 6723

A.20.3.1.1.1 Test Purpose and environment 6723

A.20.3.1.1.2 Test requirements 6724

A.20.3.2 Timing advance for RedCap UE with Satellite Access 6724

A.20.3.2.1 SA FR1 timing advance adjustment accuracy for RedCap UE 6724

A.20.3.2.1.1 Test Purpose and Environment 6724

A.20.3.2.1.2 Test Parameters 6724

A.20.3.2.1.3 Test Requirements 6726

A.20.4 Signalling characteristics for RedCap UE with Satellite Access 6726

A.20.4.1 Radio link Monitoring 6726

A.20.4.1.1 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode for 2Rx RedCap UE with NTN 6726

A.20.4.1.1.1 Test Purpose and Environment 6726

A.20.4.1.1.2 Test Requirements 6726

A.20.4.1.2 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode for 1Rx RedCap UE with NTN 6726

A.20.4.1.2.1 Test Purpose and Environment 6726

A.20.4.1.2.2 Test Requirements 6727

A.20.4.1.3 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode for 2Rx RedCap UE with NTN 6728

A.20.4.1.3.1 Test Purpose and Environment 6728

A.20.4.1.3.2 Test Requirements 6728

A.20.4.1.4 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode for 1Rx RedCap UE with NTN 6728

A.20.4.1.4.1 Test Purpose and Environment 6728

A.20.4.1.4.2 Test Requirements 6729

A.20.4.1.5 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode for 2Rx RedCap UE with NTN 6729

A.20.4.1.5.1 Test Purpose and Environment 6729

A.20.4.1.5.2 Test Requirements 6729

A.20.4.1.6 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode for 1Rx RedCap UE with NTN 6730

A.20.4.1.6.1 Test Purpose and Environment 6730

A.20.4.1.6.2 Test Requirements 6731

A.20.4.1.7 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode for 2Rx RedCap UE with NTN 6731

A.20.4.1.7.1 Test Purpose and Environment 6731

A.20.4.1.7.2 Test Requirements 6731

A.20.4.1.8 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode for 1Rx RedCap UE with NTN 6731

A.20.4.1.8.1 Test Purpose and Environment 6731

A.20.4.1.8.2 Test Requirements 6732

A.20.4.2 Beam Failure Detection and Link recovery procedures for RedCap UE with satellite access 6733

A.20.4.2.1 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode for 1Rx RedCap UE 6733

A.20.4.2.1.1 Test Purpose and Environment 6733

A.20.4.2.1.2 Test Requirements 6733

A.20.4.2.2 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode for 2Rx RedCap UE 6733

A.20.4.2.2.1 Test Purpose and Environment 6733

A.20.4.2.2.2 Test Requirements 6734

A.20.4.2.3 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode for 1Rx RedCap UE 6734

A.20.4.2.3.1 Test Purpose and Environment 6734

A.20.4.2.3.2 Test Requirements 6734

A.20.4.2.4 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode for 2Rx RedCap UE 6735

A.20.4.2.4.1 Test Purpose and Environment 6735

A.20.4.2.4.2 Test Requirements 6735

A.20.4.2.5 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode for 1Rx RedCap UE 6735

A.20.4.2.5.1 Test Purpose and Environment 6735

A.20.4.2.5.2 Test Requirements 6736

A.20.4.2.6 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode for 2Rx RedCap UE 6736

A.20.4.2.6.1 Test Purpose and Environment 6736

A.20.4.2.6.2 Test Requirements 6736

A.20.4.2.7 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode for 1Rx RedCap UE 6736

A.20.4.2.7.1 Test Purpose and Environment 6736

A.20.4.2.7.2 Test Requirements 6737

A.20.4.2.8 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode for 2Rx RedCap UE 6737

A.20.4.2.8.1 Test Purpose and Environment 6737

A.20.4.2.8.2 Test Requirements 6737

A.20.4.3 Active BWP switch for RedCap UE with Satellite Access 6737

A.20.4.3.1 DCI-based and Timer-based Active BWP Switch 6737

A.20.4.3.1.1 NR FR1 DL active BWP switch with non-DRX in SA 6737

A.20.4.3.2 RRC-based Active BWP Switch 6738

A.20.4.3.2.1 NR FR1 DL active BWP switch of Cell with non-DRX in SA 6738

A.20.4.3.2.1.2 Test Requirements 6738

A.20.4.4 UE specific CBW change for RedCap UE with Satellite Access 6738

A.20.4.4.1 UE specific CBW change on PCell in FR1 in non-DRX 6738

A.20.4.4.1.1 Test Purpose and Environment 6738

A.20.4.4.1.2 Test Requirements 6740

A.20.4.5 Pathloss reference signal switching delay for RedCap UE with Satellite Access 6740

A.20.4.5.1 MAC-CE based pathloss reference signal switch delay 6740

A.20.4.5.1.1 Test Purpose and Environment 6740

A.20.4.5.1.2 Test Requirements 6740

A.20.5 Measurement procedure 6741

A.20.5.1 Intra-frequency Measurements 6741

A.20.5.1.1 SA event triggered reporting tests without gap under non-DRX for 1Rx RedCap UE 6741

A.20.5.1.1.1 Test purpose and Environment 6741

A.20.5.1.1.2 Test parameters 6741

A.20.5.1.1.3 Test Requirements 6741

A.20.5.1.2 SA event triggered reporting tests without gap under non-DRX for 2Rx RedCap UE 6741

A.20.5.1.2.1 Test purpose and Environment 6741

A.20.5.1.2.2 Test parameters 6741

A.20.5.1.2.3 Test Requirements 6742

A.20.5.1.3 SA event triggered reporting tests without gap under DRX for 1Rx RedCap UE 6742

A.20.5.1.3.1 Test purpose and Environment 6742

A.20.5.1.3.2 Test parameters 6742

A.20.5.1.3.3 Test Requirements 6743

A.20.5.1.4 SA event triggered reporting tests without gap under DRX for 2Rx RedCap UE 6743

A.20.5.1.4.1 Test purpose and Environment 6743

A.20.5.1.4.2 Test parameters 6743

A.20.5.1.4.3 Test Requirements 6743

A.20.5.1.5 SA event triggered reporting tests without gap under non-DRX with SSB index reading for 1Rx RedCap UE 6744

A.20.5.1.5.1 Test purpose and Environment 6744

A.20.5.1.5.2 Test parameters 6744

A.20.5.1.5.3 Test Requirements 6744

A.20.5.1.6 SA event triggered reporting tests without gap under non-DRX with SSB index reading for 2Rx RedCap UE 6744

A.20.5.1.6.1 Test purpose and Environment 6744

A.20.5.1.6.2 Test parameters 6744

A.20.5.1.6.3 Test Requirements 6745

A.20.5.1.7 SA event triggered reporting tests with single measurement gap under non-DRX for satellite access for 1Rx RedCap UE 6745

A.20.5.1.7.1 Test purpose and Environment 6745

A.20.5.1.7.2 Test parameters 6745

A.20.5.1.7.3 Test Requirements 6746

A.20.5.1.8 SA event triggered reporting tests with single measurement gap under non-DRX for satellite access for 2Rx RedCap UE 6746

A.20.5.1.8.1 Test purpose and Environment 6746

A.20.5.1.8.2 Test parameters 6746

A.20.5.1.8.3 Test Requirements 6746

A.20.5.1.9 SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access for 1Rx RedCap UE 6746

A.20.5.1.9.1 Test purpose and Environment 6746

A.20.5.1.9.2 Test parameters 6746

A.20.5.1.9.3 Test Requirements 6747

A.20.5.1.10 SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access for 2Rx RedCap UE 6747

A.20.5.1.10.1 Test purpose and Environment 6747

A.20.5.1.10.2 Test parameters 6747

A.20.5.1.10.3 Test Requirements 6748

A.20.5.1.11 SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access for 1Rx RedCap UE 6748

A.20.5.1.11.1 Test purpose and Environment 6748

A.20.5.1.11.2 Test parameters 6748

A.20.5.1.11.3 Test Requirements 6748

A.20.5.1.12 SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access for 2Rx RedCap UE 6749

A.20.5.1.12.1 Test purpose and Environment 6749

A.20.5.1.12.2 Test parameters 6749

A.20.5.1.12.3 Test Requirements 6749

A.20.5.2 Inter-frequency Measurements 6749

A.20.5.2.1 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for 2Rx RedCap UE with satellite access 6749

A.20.5.2.1.1 Test Purpose and Environment 6749

A.20.5.2.1.2 Test Requirements 6750

A.20.5.2.2 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for 1Rx RedCap UE with satellite access 6750

A.20.5.2.2.1 Test Purpose and Environment 6750

A.20.5.2.2.2 Test Requirements 6750

A.20.5.2.3 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for 2Rx RedCap UE with satellite access 6751

A.20.5.2.3.1 Test Purpose and Environment 6751

A.20.5.2.3.2 Test Requirements 6751

A.20.5.2.4 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for 1Rx RedCap UE with satellite access 6751

A.20.5.2.4.1 Test Purpose and Environment 6751

A.20.5.2.4.2 Test Requirements 6752

A.20.5.2.5 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for 2Rx RedCap UE with satellite access 6752

A.20.5.2.5.1 Test Purpose and Environment 6752

A.20.5.2.5.2 Test Requirements 6752

A.20.5.2.6 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for 1Rx RedCap UE with satellite access 6752

A.20.5.2.6.1 Test Purpose and Environment 6752

A.20.5.2.6.2 Test Requirements 6753

A.20.5.2.7 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for 2Rx RedCap UE with satellite access 6753

A.20.5.2.7.1 Test Purpose and Environment 6753

A.20.5.2.7.2 Test Requirements 6753

A.20.5.2.8 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for 1Rx RedCap UE with satellite access 6754

A.20.5.2.8.1 Test Purpose and Environment 6754

A.20.5.2.8.2 Test Requirements 6754

A.20.5.2.9 Event triggered reporting test without gap under non-DRX for 2Rx RedCap UE with satellite access 6755

A.20.5.2.9.1 Test purpose and Environment 6755

A.20.5.2.9.2 Test parameters 6755

A.20.5.2.9.3 Test Requirements 6755

A.20.5.2.10 Event triggered reporting test without gap under non-DRX for 1Rx RedCap UE with satellite access 6755

A.20.5.2.10.1 Test purpose and Environment 6755

A.20.5.2.10.2 Test parameters 6755

A.20.5.2.10.3 Test Requirements 6755

A.20.5.2.11 Event triggered reporting tests without gap under DRX for 2Rx RedCap UE with satellite access 6755

A.20.5.2.11.1 Test purpose and Environment 6755

A.20.5.2.11.2 Test parameters 6755

A.20.5.2.11.3 Test Requirements 6756

A.20.5.2.12 Event triggered reporting tests without gap under DRX for 1Rx RedCap UE with satellite access 6756

A.20.5.2.12.1 Test purpose and Environment 6756

A.20.5.2.12.2 Test parameters 6756

A.20.5.2.12.3 Test Requirements 6757

A.20.5.3 L1-RSRP measurement for beam reporting for (e)RedCap UE with Satellite Access 6757

A.20.5.3.1 SSB based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is not used for 1Rx (e)RedCap UE with NTN 6757

A.20.5.3.1.1 Test Purpose and Environment 6757

A.20.5.3.1.2 Test parameters 6757

A.20.5.3.1.3 Test Requirements 6759

A.20.5.3.2 SSB based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is not used for 2Rx (e)RedCap UE with NTN 6759

A.20.5.3.2.1 Test Purpose and Environment 6759

A.20.5.3.2.2 Test parameters 6759

A.20.5.3.2.3 Test Requirements 6761

A.20.5.3.3 CSI-RS based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is used for 1Rx (e)RedCap UE with NTN 6761

A.20.5.3.3.1 Test Purpose and Environment 6761

A.20.5.3.3.2 Test parameters 6761

A.20.5.3.3.3 Test Requirements 6763

A.20.5.3.4 CSI-RS based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is used for 2Rx (e)RedCap UE with NTN 6763

A.20.5.3.4.1 Test Purpose and Environment 6763

A.20.5.3.4.2 Test parameters 6764

A.20.5.3.4.3 Test Requirements 6765

A.20.6 Measurement Performance requirements 6765

A.20.6.1 SS-RSRP for SAN 6765

A.20.6.1.1 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE 6765

A.20.6.1.1.1 Test Purpose and Environment 6765

A.20.6.1.1.2 Test parameters 6765

A.20.6.1.1.3 Test Requirements 6767

A.20.6.1.2 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE 6767

A.20.6.1.2.1 Test Purpose and Environment 6767

A.20.6.1.2.2 Test parameters 6767

A.20.6.1.2.3 Test Requirements 6768

A.20.6.1.3 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE 6768

A.20.6.1.3.1 Test Purpose and Environment 6768

A.20.6.1.3.2 Test parameters 6769

A.20.6.1.3.3 Test Requirements 6770

A.20.6.1.4 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE 6770

A.20.6.1.4.1 Test Purpose and Environment 6770

A.20.6.1.4.2 Test parameters 6770

A.20.6.1.4.3 Test Requirements 6772

A.20.6.2 SS-RSRQ 6772

A.20.6.2.1 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 1Rx RedCap UE 6772

A.20.6.2.1.1 Test Purpose and Environment 6772

A.20.6.2.1.2 Test Parameters 6772

A.20.6.2.1.3 Test Requirements 6773

A.20.6.2.2 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 2Rx RedCap UE 6773

A.20.6.2.2.1 Test Purpose and Environment 6773

A.20.6.2.2.2 Test Parameters 6773

A.20.6.2.2.3 Test Requirements 6775

A.20.6.2.3 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 1Rx RedCap UE 6775

A.20.6.2.3.1 Test Purpose and Environment 6775

A.20.6.2.3.2 Test Parameters 6775

A.20.6.2.3.3 Test Requirements 6776

A.20.6.2.4 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 2Rx RedCap UE 6776

A.20.6.2.4.1 Test Purpose and Environment 6776

A.20.6.2.4.2 Test Parameters 6776

A.20.6.2.4.3 Test Requirements 6778

A.20.6.3 SS-SINR 6778

A.20.6.3.1 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE 6778

A.20.6.3.1.1 Test Purpose and Environment 6778

A.20.6.3.1.2 Test Parameters 6778

A.20.6.3.1.3 Test Requirements 6779

A.20.6.3.2 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE 6780

A.20.6.3.2.1 Test Purpose and Environment 6780

A.20.6.3.2.2 Test Parameters 6780

A.20.6.3.2.3 Test Requirements 6781

A.20.6.3.3 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE 6781

A.20.6.3.3.1 Test Purpose and Environment 6781

A.20.6.3.3.2 Test Parameters 6781

A.20.6.3.3.3 Test Requirements 6783

A.20.6.3.4 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE 6783

A.20.6.3.4.1 Test Purpose and Environment 6783

A.20.6.3.4.2 Test Parameters 6783

A.20.6.3.4.3 Test Requirements 6784

A.20.6.4 L1-RSRP measurement for beam reporting 6785

A.20.6.4.1 SSB based L1-RSRP measurement for 1Rx RedCap UE 6785

A.20.6.4.1.1 Test Purpose and Environment 6785

A.20.6.4.1.2 Test parameters 6785

A.20.6.4.1.3 Test Requirements 6786

A.20.6.4.2 SSB based L1-RSRP measurement for 2Rx RedCap UE 6786

A.20.6.4.2.1 Test Purpose and Environment 6786

A.20.6.4.2.2 Test parameters 6786

A.20.6.4.2.3 Test Requirements 6788

A.20.6.4.3 CSI-RS based L1-RSRP measurement on resource set with repetition off for 1Rx RedCap UE 6788

A.20.6.4.3.1 Test Purpose and Environment 6788

A.20.6.4.3.2 Test parameters 6788

A.20.6.4.3.3 Test Requirements 6789

A.20.6.4.4 CSI-RS based L1-RSRP measurement on resource set with repetition off for 2Rx RedCap UE 6789

A.20.6.4.4.1 Test Purpose and Environment 6789

A.20.6.4.4.2 Test parameters 6790

A.20.6.4.4.3 Test Requirements 6791

A.21 NR standalone tests for LP-WUR 6791

A.21.1 RRC_IDLE state mobility 6791

A.21.1.1 UE exits offloading mode to legacy mode with LR using LP-SS signal 6791

A.21.1.1.1 Test Purpose and Environment 6791

A.21.1.1.2 Test Parameters 6791

A.21.1.1.3 Test Requirements 6794

A.21.1.2 UE exits from relaxed measurement mode with LR using PSS/SSS in FR1 6794

A.21.1.2.1 Test Procedure and Environment 6794

A.21.1.2.2 Test Parameters 6794

A.21.1.2.3 Test Requirements 6798

A.21.1.3 UE exits relaxed measurement mode to legacy mode with LR using LP-SS signal 6798

A.21.1.3.1 Test Purpose and Environment 6798

A.21.1.3.2 Test Parameters 6798

A.21.1.3.3 Test Requirements 6801

A.21.1.4 UE exit from relaxed measurement mode with LR using PSS/SSS in FR2 6801

A.21.1.4.1 Test Purpose and Environment 6801

A.21.1.4.2 Test Parameters 6801

A.21.1.4.3 Test Requirements 6804

Annex B (normative): Conditions for RRM requirements applicability for operating bands 6805

B.1 Conditions for NR RRC_IDLE state mobility 6805

B.1.1 Introduction 6805

B.1.2 Conditions for measurements on NR intra-frequency cells for cell re-selection 6805

B.1.2A Conditions for measurements on NR intra-frequency cells under CCA for cell re-selection 6807

B.1.3 Conditions for measurements on NR inter-frequency cells for cell re-selection 6808

B.1.3A Conditions for measurements on NR inter-frequency cells under CCA for cell re-selection 6808

B.1.4 Conditions for measurements on NR intra-frequency cells for cell re-selection for RedCap 6808

B.1.5 Conditions for measurements on NR inter-frequency cells for cell re-selection for RedCap 6811

B.1.6 Conditions for measurements on NR intra-frequency cells for cell re-selection for satellite access 6811

B.1.7 Conditions for measurements on NR inter-frequency cells for cell re-selection for satellite access 6811

B.1.8 Conditions for measurements on NR serving cells by LP-WUR 6811

B.2 Conditions for UE measurements procedures and performance requirements in RRC_CONNECTED state 6812

B.2.1 Introduction 6812

B.2.1.1 General 6812

B.2.1.2 Derivation of Minimum SSB_RP values for FR1 6812

B.2.1.3 Derivation of Minimum SSB_RP values for FR2 6812

B.2.1.3.1 Minimum SSB_RP values for Rx Beam Peak angle of arrival 6813

B.2.1.3.2 Minimum SSB_RP values for angle of arrival within Spherical coverage 6813

B.2.1.4 Gain to SS-RSRP and CSI-RSRP measurement point for FR1 6814

B.2.1.5 Gain to SS-RSRP and CSI-RSRP measurement point for FR2 6814

B.2.1.5.1 Gain to SS-RSRP and CSI-RSRP measurement point for Rx Beam Peak angle of arrival 6814

B.2.1.5.2 Gain to SS-RSRP measurement point for different frequency 6815

B.2.1.5.3 Alignment of Rough beam to Rx beam Peak 6815

B.2.1.6 Gain to PRS-RSRP measurement point for FR2 6815

B.2.1.6.1 Gain to PRS-RSRP measurement point for Rx Beam Peak angle of arrival 6815

B.2.1.7 Derivation of Minimum SSB_RP values for FR2-NTN for satellite access 6816

B.2.1.7.1 Minimum SSB_RP values for Rx Beam 6816

B.2.1.8 Gain to SS-RSRP for FR2-NTN for satellite access 6817

B.2.2 Conditions for NR intra-frequency measurements 6817

B.2.3 Conditions for NR inter-frequency measurements 6820

B.2.4 Conditions for NR L1-RSRP reporting 6822

B.2.4.1 Conditions for SSB based L1-RSRP reporting 6822

B.2.4.2 Conditions for CSI-RS based L1-RSRP reporting 6824

B.2.5 Conditions for RRC connection release with redirection to NR 6826

B.2.6 Void 6828

B.2.6.1 Void 6828

B.2.6.2 Void 6828

B.2.7 Conditions for SRS-RSRP measurements 6828

B.2.8 Conditions for NR L1-SINR reporting 6829

B.2.8.1 Conditions for L1-SINR reporting with CSI-RS based CMR and no dedicated IMR configured 6829

B.2.8.2 Conditions for L1-SINR reporting with SSB based CMR and dedicated IMR configured 6831

B.2.8.2.1 L1-SINR reporting with SSB based CMR and dedicated ZP-IMR configured 6831

B.2.8.2.2 L1-SINR reporting with SSB based CMR and dedicated NZP-IMR configured 6833

B.2.8.3 Conditions for L1-SINR reporting with CSI-RS based CMR and dedicated IMR configured 6835

B.2.8.3.1 L1-SINR reporting with CSI-RS based CMR and dedicated ZP-IMR configured 6835

B.2.8.3.2 L1-SINR reporting with CSI-RS based CMR and dedicated NZP-IMR configured 6837

B.2.9 Conditions for NR intra-frequency measurements under CCA 6839

B.2.10 Conditions for NR inter-frequency measurements under CCA 6839

B.2.11 Conditions for NR L1-RSRP reporting under CCA 6839

B.2.11.1 Conditions for SSB based L1-RSRP reporting 6839

B.2.12 Conditions for NR CSI-RS based intra-frequency measurements 6840

B.2.13 Conditions for NR CSI-RS based inter-frequency measurements 6841

B.2.14 Conditions for NR PRS-based measurements 6842

B.2.15 Conditions for NR intra-frequency measurements for RedCap 6844

B.2.16 Conditions for NR inter-frequency measurements for RedCap 6845

B.2.17 Conditions for NR intra-frequency measurements for satellite access 6847

B.2.18 Conditions for NR inter-frequency measurements for satellite access 6847

B.2.19 Conditions for NR L1-RSRP reporting for satellite access 6848

B.2.19.1 Conditions for SSB based L1-RSRP reporting for satellite access 6848

B.2.19.2 Conditions for CSI-RS based L1-RSRP reporting for satellite access 6848

B.2.20 Conditions for RRC connection release with redirection to NR for satellite access 6849

B.3 RRM Requirements Exceptions 6849

B.3.1 Introduction 6849

B.3.2 Receiver sensitivity relaxation for CA 6849

B.3.2.1 Receiver sensitivity relaxation for UE supporting CA in FR1 6849

B.3.2.2 Receiver sensitivity relaxation for UE configured with CA in FR1 6849

B.3.2.2.1 Inter-band carrier aggregation 6849

B.3.2.2.2 Reference sensitivity exceptions due to UL harmonic interference for CA 6850

B.3.2.2.3 Reference sensitivity exceptions due to intermodulation interference due to 2UL CA 6850

B.3.2.3 Receiver sensitivity relaxation for UE supporting CA in FR2 6850

B.3.2.4 Receiver sensitivity relaxation for UE configured with CA in FR2 6850

B.3.2.4.1 Intra-band contiguous carrier aggregation 6850

B.3.2.4.2 Intra-band non-contiguous carrier aggregation 6850

B.3.3 Receiver sensitivity relaxation for DC 6850

B.3.3.1 Receiver sensitivity relaxation for EN-DC 6850

B.3.3.2 Receiver sensitivity relaxation for NE-DC 6851

B.3.4 Receiver sensitivity relaxation for SUL 6851

B.3.4.1 Receiver sensitivity relaxation for UE supporting SUL in FR1 6851

B.3.4.2 Receiver sensitivity relaxation for UE configured with SUL in FR1 6851

B.3.4.2.1 Reference sensitivity exceptions due to UL harmonic interference for SUL 6851

B.4 Conditions for V2X 6851

B.4.1 Test parameters for GNSS signals 6851

B.4.2 Conditions for PSBCH-RSRP Accuracy Requirements 6851

B.4.3 Conditions for Selection/Reselection to Intra-frequency SyncRef UE 6852

B.4.4 Conditions for L1 SL-RSRP Accuracy Requirements 6852

B.4.5 Conditions for PSBCH-RSRP Accuracy Requirements under CCA 6852

B.4.6 Conditions for Selection/Reselection to Intra-frequency SyncRef UE under CCA 6853

B.4.7 Conditions for L1 SL-RSRP Accuracy Requirements under CCA 6853

B.4A Conditions for NR Sidelink Positioning Measurement Procedures and Performance Requirements 6854

B.4A.1 Conditions for NR SL-PRS based measurements 6854

B.5 High level test procedure for SAN RRM tests 6854

Annex C (informative): Change history 6856
