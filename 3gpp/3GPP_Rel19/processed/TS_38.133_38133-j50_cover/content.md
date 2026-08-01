---
type: spec
aliases:
  - 38.133_38133-j50_cover
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_cover/content.md"
---
# TS 38.133 38133-j50_cover

Contents

Foreword189

1Scope191

2References191

3Definitions, symbols and abbreviations193

3.1Definitions193

3.2Symbols194

3.3Abbreviations195

3.4Test tolerances199

3.5Frequency bands grouping199

3.5.1Introduction199

3.5.2NR operating bands in FR1199

3.5.2ANR operating bands for satellite access in FR1148

3.5.3NR operating bands in FR2148

3.6Applicability of requirements in this specification version149

3.6.1RRC connected state requirements in DRX149

3.6.2Number of serving carriers150

3.6.2.1Number of serving carriers for SA150

3.6.2.2Number of serving carriers for EN-DC150

3.6.2.3Number of serving carriers for NE-DC150

3.6.2.4Number of serving carriers for NR-DC150

3.6.3Applicability for intra-band FR2150

3.6.4Applicability for FR2 UE power classes150

3.6.5Applicability for SDL bands151

3.6.6Applicability of requirements for NGEN-DC operation151

3.6.7Applicability of QCL151

3.6.9Applicability of requirements for scheduling availability152

3.6.10Applicability of requirements for measurement restrictions152

3.6.11Applicability of requirements for Redcap UEs152

3.6.11.1RRC connected state requirements in DRX152

3.6.11.2Applicability for FR2 Redcap UE power classes152

3.6.11.3Applicability of QCL152

3.6.12Applicability of requirements for Satellite Access152

3.6.13Applicability of requirements for FR2152

3.6.14Applicability of requirements for FR2 Power Class 6153

3.6.15Applicability of requirements for per-FR gap153

3.6.16Applicability of requirements for ATG153

3.6.17Applicability of requirements for MUSIM gaps153

3.6.18Applicability of requirements for a UE operating on a cell with less than 5 MHz BW153

3.6.19Applicability of requirements for multi-Rx operation in FR2-1153

3.6.20Applicability of requirements for RedCap UE with satellite access153

3.6.21Applicability of requirements for UE supporting L3 fast beam sweeping operation in FR2-1154

3.6.22Applicability of requirements for UE with LP-WUR154

3.6.23Applicability of requirements for SBFD154

4SA: RRC_IDLE state mobility154

4.1Cell Selection154

4.2Cell Re-selection155

4.2.1Introduction155

4.2.2Requirements155

4.2.2.1UE measurement capability155

4.2.2.2Measurement and evaluation of serving cell155

4.2.2.3Measurements of intra-frequency NR cells157

4.2.2.4Measurements of inter-frequency NR cells161

4.2.2.5Measurements of inter-RAT E-UTRAN cells166

4.2.2.6Maximum interruption in paging reception168

4.2.2.7General requirements169

4.2.2.8Minimum requirement at transitions169

4.2.2.9Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion170

4.2.2.9.1Introduction170

4.2.2.9.2Measurements for UE fulfilling low mobility criterion170

4.2.2.9.3Measurements for UE fulfilling not-at-cell edge criterion172

4.2.2.9.4Measurements for UE fulfilling low mobility and not-at-cell edge criteria174

4.2.2.10Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion175

4.2.2.10.1Introduction175

4.2.2.10.2Measurements for UE fulfilling low mobility criterion175

4.2.2.10.3Measurements for UE fulfilling not-at-cell edge criterion177

4.2.2.10.4Measurements for UE fulfilling low mobility and not-at-cell edge criterion180

4.2.2.11Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion180

4.2.2.11.1Introduction180

4.2.2.11.2Measurements for UE fulfilling low mobility criterion181

4.2.2.11.3Measurements for UE fulfilling with not-at-cell edge criterion182

4.2.2.11.4Measurements for UE fulfilling low mobility and not-at-cell edge criterion184

## 4.2.2.12 Measurements of inter-frequency NR cells with NTN carrier184

4.2ACell Re-selection when subject to CCA187

4.2A.1Introduction187

4.2A.2Requirements187

4.2A.2.1UE measurement capability187

4.2A.2.2Measurement and evaluation when subject to CCA on the serving cell188

4.2A.2.3Measurements of intra-frequency NR cells when subject to CCA on the serving cell and target cell189

4.2A.2.4Measurements of inter-frequency NR cells when subject to CCA on the target cell190

4.2A.2.5Measurements of inter-RAT E-UTRAN cells when subject to CCA on the serving cell192

4.2A.2.6Maximum interruption in paging reception when subject to CCA on the target cell192

4.2A.2.7General requirements192

4.2BCell Re-selection for RedCap193

4.2B.1Introduction193

4.2B.2Requirements193

4.2B.2.1UE measurement capability for RedCap193

4.2B.2.1.1UE measurement capability for 1 Rx RedCap193

4.2B.2.1.2UE measurement capability for 2 Rx RedCap193

4.2B.2.2Measurement and evaluation of serving cell for RedCap UE193

4.2B.2.3Measurements of intra-frequency NR cells for RedCap UE195

4.2B.2.4Measurements of inter-frequency NR cells for RedCap UE197

4.2B.2.5Measurements of inter-RAT E-UTRAN cells for RedCap UE200

4.2B.2.6Maximum interruption in paging reception for RedCap202

4.2B.2.7General requirements for RedCap202

4.2B.2.8Minimum requirement at transitions202

4.2B.2.9Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion for RedCap203

4.2B.2.9.1Introduction203

4.2B.2.9.2Measurements for UE fulfilling stationary criterion203

4.2B.2.9.3Measurements for a UE fulfilling not-at-cell edge while stationary criterion206

4.2B.2.9.3AMeasurements for a UE fulfilling stationary and not-at-cell-edge criteria206

4.2B.2.9.4Measurements for a UE fulfilling low mobility and stationary criteria207

4.2B.2.9.5Measurements for a UE fulfilling low mobility and not-at-cell-edge while stationary criteria207

4.2B.2.9.6Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge while stationary criteria207

4.2B.2.9.7Measurements for a UE fulfilling low mobility and not-at-cell edge criteria and not-at-cell-edge while stationary criteria207

4.2B.2.9.8Measurements for a UE fulfilling low mobility, not-at-cell edge and stationary criterion207

4.2B.2.9.9Measurements for UE fulfilling low mobility criterion208

4.2B.2.9.10Measurements for UE fulfilling not-at-cell edge criterion210

4.2B.2.9.11Measurements for UE fulfilling low mobility and not-at-cell edge criteria212

4.2B.2.10Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion213

4.2B.2.10.1Introduction213

4.2B.2.10.2Measurements for UE fulfilling stationary criterion213

4.2B.2.10.3Measurements for a UE fulfilling not-at-cell edge while stationary  criterion215

4.2B.2.10.3AMeasurements for a UE fulfilling stationary and not-at-cell-edge criterion216

4.2B.2.10.4Measurements for a UE fulfilling low mobility and stationary criteria216

4.2B.2.10.5Measurements for a UE fulfilling low mobility and not-at-cell-edge while stationary criteria216

4.2B.2.10.6Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge while stationary criteria217

4.2B.2.10.7Measurements for a UE fulfilling low mobility and not-at-cell edge criteria and not-at-cell-edge while stationary criteria217

4.2B.2.10.8Measurements for a UE fulfilling low mobility, not-at-cell edge and stationary  criteria217

4.2B.2.10.9Measurements for UE fulfilling low mobility criterion217

4.2B.2.10.10Measurements for UE fulfilling not-at-cell edge criterion220

4.2B.2.10.11Measurements for UE fulfilling low mobility and not-at-cell edge criterion222

4.2B.2.11Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion222

4.2B.2.11.1Introduction222

4.2B.2.11.2Measurements for UE fulfilling stationary criterion223

4.2B.2.11.3Measurements for a UE fulfilling not-at-cell edge while stationary criterion224

4.2B.2.11.3AMeasurements for a UE fulfilling stationary and not-at-cell-edge criterion224

4.2B.2.11.4Measurements for a UE fulfilling low mobility and stationary criteria225

4.2B.2.11.5Measurements for a UE fulfilling low mobility and not-at-cell-edge while stationary  criteria225

4.2B.2.11.6Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge while stationary criteria225

4.2B.2.11.7Measurements for a UE fulfilling low mobility and not-at-cell edge criteria and not-at-cell-edge while stationary criteria225

4.2B.2.11.8Measurements for a UE fulfilling low mobility, not-at-cell edge and stationary  criteria226

4.2B.2.11.9Measurements for UE fulfilling low mobility criterion226

4.2B.2.11.10Measurements for UE fulfilling with not-at-cell edge criterion227

4.2B.2.11.11Measurements for UE fulfilling low mobility and not-at-cell edge criterion228

4.2CCell Re-selection for NR UE for Satellite Access229

4.2C.1Introduction229

4.2C.2Requirements229

4.2C.2.1UE measurement capability229

4.2C.2.2Measurement and evaluation of serving cell229

4.2C.2.3Measurements of intra-frequency NR cells231

4.2C.2.4Measurements of inter-frequency NR cells233

4.2C.2.5Maximum interruption in paging reception237

4.2C.2.6Minimum requirement at transitions238

4.2C.2.7Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion238

4.2C.2.8Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion238

4.2C.2.9General requirements238

4.2C.2.10Measurements of inter-frequency NR cells with TN carrier238

4.2C.2.11Measurements of inter-RAT E-UTRAN cells with TN carrier241

4.2C.3Void243

4.2C.4Void243

4.2DCell Re-selection for ATG243

4.2D.1Introduction243

4.2D.2Requirements243

4.2D.2.1UE measurement capability243

4.2D.2.2Measurement and evaluation of serving cell243

4.2D.2.3Measurements of intra-frequency NR cells244

4.2D.2.4Measurements of inter-frequency NR cells245

4.2D.2.5Maximum interruption in paging reception247

4.2D.2.6General requirements247

4.2ECell Re-selection for NR RedCap UE with Satellite Access247

4.2E.1Introduction247

4.2E.2Requirements for RedCap UE with Satellite Access248

4.2E.2.1UE measurement capability for RedCap with Satellite Access248

4.2E.2.1.1UE measurement capability for 1Rx RedCap UEs248

4.2E.2.1.2UE measurement capability for 2Rx RedCap UEs248

4.2E.2.2Measurement and evaluation of serving cell for RedCap UEs248

4.2E.2.3Measurements of intra-frequency NR cells for RedCap UE250

4.2E.2.4Measurements of inter-frequency NR cells for RedCap UE252

4.2E.2.5Maximum interruption in paging reception255

4.2E.2.6Minimum requirement at transitions for RedCap UE255

4.2E.2.7Measurements of intra-frequency NR cells for RedCap UE configured with relaxed measurement criterion255

4.2E.2.7.1Introduction255

4.2E.2.7.2Measurements for UE fulfilling low mobility criterion256

4.2E.2.7.3Measurements for UE fulfilling not-at-cell edge criterion256

4.2E.2.7.4Measurements for UE fulfilling low mobility and not-at-cell edge criteria256

4.2E.2.8Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion257

4.2E.2.8.1Introduction257

4.2E.2.8.2Measurements for UE fulfilling low mobility criterion257

4.2E.2.8.3Measurements for UE fulfilling not-at-cell edge criterion257

4.2E.2.8.4Measurements for UE fulfilling low mobility and not-at-cell edge criterion258

4.2E.2.9General requirements258

4.2E.2.10Measurements of inter-frequency NR cells with TN carrier258

4.2E.2.11Measurements of inter-RAT E-UTRAN cells with TN carrier262

4.3Minimization of Drive Tests (MDT)263

4.3.1Introduction263

4.3.2Measurement Requirements263

4.3.3Requirements for Relative Time Stamp Accuracy264

4.3.4Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting264

4.3.5Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting264

4.3CMinimization of Drive Tests (MDT) for Satellite Access264

4.3C.1Introduction264

4.3C.2Measurement Requirements265

4.3C.3Requirements for Relative Time Stamp Accuracy265

4.3C.4Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting265

4.3C.5Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting266

4.3DMinimization of Drive Tests (MDT) for NR RedCap UE with Satellite Access266

4.3D.1Introduction266

4.3D.2Measurement Requirements266

4.3D.3Requirements for Relative Time Stamp Accuracy266

4.3D.4Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting266

4.3D.5Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting266

4.4Idle Mode CA/DC Measurements267

4.4.1Introduction267

4.4.2Measurement Requirements267

4.4.2.1Detected cell requirement during state transition and Idle mode267

4.4.2.2Measurements of inter-frequency CA/DC candidate cells267

4.4.2.3Measurements on serving cell268

4.4.2.4Measurements of E-UTRAN inter-RAT DC candidate cells269

4.5NR measurements for positioning269

4.5.1Introduction269

4.5.2RSTD measurements270

4.5.2.1Introduction270

4.5.2.2Requirements Applicability270

4.5.2.3Measurement Capability270

4.5.2.4Measurement Reporting Requirements270

4.5.2.5Measurements Period Requirements270

4.5.2.6Measurements Period Requirements with Bandwidth Aggregation273

4.5.3PRS-RSRP measurements277

4.5.3.1Introduction277

4.5.3.2Requirements applicability277

4.5.3.3Measurement Capability277

4.5.3.4Measurement Reporting Requirements277

4.5.3.5Measurement Period Requirements278

4.5.4PRS-RSRPP measurements280

4.5.4.1Introduction280

4.5.4.2Requirements Applicability280

4.5.4.3Measurement Capability280

4.5.4.4Measurement Reporting Requirements280

4.5.4.5Measurement Period Requirements281

4.5.5Measurement requirements for DL RSCPD reported with RSTD281

4.5.5.1Introduction281

4.5.5.2Requirements Applicability281

4.5.5.3Measurement Capability281

4.5.5.4Measurement Reporting Requirements281

4.5.5.5Measurements Period Requirements282

4.5AReporting Delay Requirements for DL AI/ML Positioning286

4.5A.1Introduction286

4.5A.2Measurements Period Requirements286

4.5A.3Measurements Period Requirements with Bandwidth Aggregation289

4.6NR measurements for positioning for RedCap292

4.6.1Introduction292

4.6.2RSTD measurements for RedCap293

4.6.2.1Introduction293

4.6.2.2Requirements Applicability293

4.6.2.3Measurement Capability293

4.6.2.4Measurement Reporting Requirements293

4.6.2.5Measurements Period Requirements without RX FH293

4.6.2.6Measurement Period Requirements with RX FH294

4.6.3PRS-RSRP measurements for RedCap296

4.6.3.1Introduction296

4.6.3.2Requirements applicability296

4.6.3.3Measurement Capability296

4.6.3.4Measurement Reporting Requirements296

4.6.3.5Measurement Period Requirements without RX FH297

4.6.3.6Measurement Period Requirements with RX FH299

4.6.4PRS-RSRPP measurements for RedCap301

4.6.4.1Introduction301

4.6.4.2Requirements Applicability301

4.6.4.3Measurement Capability301

4.6.4.4Measurement Reporting Requirements301

4.6.4.5Measurement Period Requirements without RX FH302

4.6.4.6Measurement Period Requirements with RX FH302

4.7Measurement report for fast CA/DC setup302

4.7.1Introduction302

4.7.2Void302

4.7.3Measurement Report Requirements302

4.8IDLE mode measurement for LP-WUS operation303

4.8.1Introduction303

## 4.8.2 Requirements303

## 4.8.2.1 UE Measurement Capability303

## 4.8.2.1.1 LP-WUR measurement capability303

## 4.8.2.1.2 MR measurement capability with LP-WUR303

4.8.2.2LP-WUR Serving cell measurement and evaluation requirement303

4.8.2.2.1General description303

4.8.2.2.2LP-WUR measurement and evaluation requirements for PSS/SSS304

4.8.2.2.3LP-WUR measurement and evaluation requirements for LP-SS305

4.8.2.3Measurement and evaluation of serving cell by MR305

4.8.2.3.1Requirements for evaluation of cell selection criterion305

4.8.2.3.2Requirements for evaluation of LP-WUS related conditions306

4.8.2.3AMeasurement and evaluation of serving cell by RedCap UE306

4.8.2.3A.1Requirements for evaluation of cell selection criterion for RedCap UE306

4.8.2.3A.2Requirements for evaluation of LP-WUS related conditions for RedCap UE306

## 4.8.2.4 Measurements of intra-frequency NR cells for UE with LP-WUR307

4.8.2.4AMeasurements of intra-frequency NR cells for RedCap UE with LP-WUR307

4.8.2.5Measurements of inter-frequency NR cells for UE with LP-WUR308

4.8.2.5.1Introduction308

4.8.2.5.2Measurements for UE with LP-WUR fulfilling relaxed measurement criterion308

4.8.2.5.3Measurements for UE with LP-WUR fulfilling serving cell measurement offloading criterion309

4.8.2.5AMeasurements of inter-frequency NR cells for Redcap with LP-WUR309

4.8.2.5A.1Introduction309

4.8.2.5A.2Measurements for UE with LP-WUR fulfilling relaxed measurement criterion309

4.8.2.5A.3Measurements for UE with LP-WUR fulfilling serving cell measurement offloading criterion310

## 4.8.2.6     Measurements of inter-RAT E-UTRAN cells for UE with LP-WUR310

4.8.2.6.1Introduction310

4.8.2.6.2Measurements for UE fulfilling relaxed measurement criteria310

4.8.2.6.3Measurements for UE fulfilling serving cell measurement offloading entry criteria311

4.8.2.6AMeasurements of inter-RAT E-UTRAN cells for RedCap with LP-WUR311

4.8.2.6A.1Introduction311

4.8.2.6A.2Measurements for UE fulfilling relaxed measurement criteria311

4.8.2.6A.3Measurements for UE fulfilling serving cell measurement offloading entry criteria312

5SA: RRC_INACTIVE state mobility312

5.1Cell Re-selection312

5.1.1Introduction312

5.1.2Requirements312

5.1.2.1UE measurement capability312

5.1.2.2Measurement and evaluation of serving cell312

5.1.2.3Measurements of intra-frequency NR cells314

5.1.2.4Measurements of inter-frequency NR cells316

5.1.2.5Measurements of inter-RAT E-UTRAN cells318

5.1.2.6Maximum interruption in paging reception319

5.1.2.7General requirements319

5.1.2.8Measurement of inter-frequency NR cells with NTN carrier320

5.1.2.9Minimum requirement at transitions320

5.1.2.10Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion320

5.1.2.11Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion321

5.1.2.12Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion322

5.1ACell Re-selection with CCA322

5.1A.1Introduction322

5.1A.2Requirements323

5.1A.2.1UE measurement capability323

5.1A.2.2Measurement and evaluation when CCA is used on the serving cell323

5.1A.2.3Measurements of intra-frequency NR cells when CCA is used on the serving cell and target cell323

5.1A.2.4Measurements of inter-frequency NR cells when CCA is used on the target cell323

5.1A.2.5Measurements of inter-RAT E-UTRAN cells when CCA is used on the serving cell323

5.1A.2.6Maximum interruption in paging reception when CCA is used on the target cell323

5.1A.2.7General requirements323

5.1BCell Re-selection for RedCap323

5.1B.1Introduction323

5.1B.2Requirements323

5.1B.2.1UE measurement capability323

5.1B.2.2Measurement and evaluation of serving cell323

5.1B.2.3Measurements of intra-frequency NR cells326

5.1B.2.4Measurements of inter-frequency NR cells328

5.1B.2.5Measurements of inter-RAT E-UTRAN cells330

5.1B.2.6Maximum interruption in paging reception331

5.1B.2.7General requirements331

5.1B.2.8Minimum requirement at transitions331

5.1B.2.9Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion331

5.1B.2.10Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion333

5.1B.2.11Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion336

5.1CCell Re-selection for Satellite Access337

5.1C.1Introduction337

5.1C.2Requirements337

5.1C.2.1UE measurement capability337

5.1C.2.2Measurement and evaluation of serving cell337

5.1C.2.3Measurements of intra-frequency NR cells337

5.1C.2.4Measurements of inter-frequency NR cells338

5.1C.2.5Maximum interruption in paging reception338

5.1C.2.6General requirements338

5.1C.2.7Measurements of inter-frequency NR cells with TN carrier338

5.1C.2.8Measurements of inter-RAT E-UTRAN cells with TN carrier338

5.1C.3Void338

5.1C.4Void338

5.1DCell Re-selection for ATG338

5.1D.1Introduction338

5.1D.2Requirements338

5.1D.2.1UE measurement capability338

5.1D.2.2Measurement and evaluation of serving cell338

5.1D.2.3Measurements of intra-frequency NR cells338

5.1D.2.4Measurements of inter-frequency NR cells338

5.1D.2.5Maximum interruption in paging reception339

5.1D.2.6General requirements339

5.1ECell Re-selection for RedCap UE with Satellite Access339

5.1E.1Introduction339

5.1E.2Requirements339

5.1E.2.1UE measurement capability339

5.1E.2.2Measurement and evaluation of serving cell339

5.1E.2.3Measurements of intra-frequency NR cells340

5.1E.2.4Measurements of inter-frequency NR cells341

5.1E.2.5Maximum interruption in paging reception341

5.1E.2.6General requirements341

5.1E.2.7Minimum requirement at transitions341

5.1E.2.8Measurements of inter-frequency NR cells with TN carrier341

5.1E.2.9Measurements of inter-RAT E-UTRAN cells with TN carrier342

5.2Void342

5.2BConfigured Grant based Small Data Transmissions (CG-SDT) for RedCap342

5.2B.1Introduction342

5.2B.2Requirements on UE synchronization for small data transmissions for RedCap342

5.2B.2.1Void342

5.2B.3TA validation requirements for RedCap342

5.2B.3.1Void343

5.2B.3.2Void343

5.2B.4Scheduling restriction343

5.2B.5Applicability conditions for CG-SDT for RedCap343

5.3Minimization of Drive Tests (MDT)344

5.3.1Introduction344

5.3.2Measurement Requirements344

5.3.3Requirements for Relative Time Stamp Accuracy344

5.3.4Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting344

5.3.5Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting344

5.3.6Requirements for Relative Time Stamp Accuracy for RRC Resume Failure Log Reporting344

5.3CMinimization of Drive Tests (MDT) for Satellite Access345

5.3C.1Introduction345

5.3C.2Measurement Requirements345

5.3C.3Requirements for Relative Time Stamp Accuracy345

5.3C.4Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting345

5.3C.5Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting345

5.3C.6Requirements for Relative Time Stamp Accuracy for RRC Resume Failure Log Reporting345

5.3DMinimization of Drive Tests (MDT) for NR RedCap UE with Satellite Access346

5.3D.1Introduction346

5.3D.2Measurement Requirements346

5.3D.3Requirements for Relative Time Stamp Accuracy346

5.3D.4Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting346

5.3D.5Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting346

5.3D.6Requirements for Relative Time Stamp Accuracy for RRC Resume Failure Log Reporting346

5.4Inactive Mode CA/DC Measurements347

5.4.1Introduction347

5.4.2Measurement Requirements347

5.4.2.1Detected cell requirement during state transition and inactive mode347

5.4.2.2Measurements of inter-frequency CA/DC candidate cells347

5.4.2.3Measurements on serving cell347

5.4.2.4Measurements on E-UTRAN inter-RAT DC candidate cells347

5.5Configured Grant based Small Data Transmissions (CG-SDT)347

5.5.1Introduction347

5.5.2Requirements on UE synchronization for small data transmissions347

5.5.3TA validation requirements347

5.5.4Scheduling restriction349

5.5.4.1Scheduling availability of UE performing measurements in TDD bands on FR1349

5.5.4.2Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1349

5.5.4.3Scheduling availability of UE performing measurements on FR2349

5.5.5Applicability conditions for SDT350

The UE is allowed to delay the reception of PRS resources on the positioning frequency layer until the SDT session is completed if the measurement using PRS resource overlaps with the SDT resources.350

5.5DConfigured Grant based Small Data Transmissions (CG-SDT) for ATG350

5.5D.1Scheduling availability of UE performing measurements on FR1350

5.5EConfigured Grant based Small Data Transmissions (CG-SDT) for RedCap UEs with NTN351

5.5E.1Introduction351

5.5E.2Requirements on UE synchronization for small data transmissions351

5.5E.3TA validation requirements351

5.5E.4Scheduling restriction351

5.5E.5Applicability conditions for SDT351

5.6NR measurements for positioning352

5.6.1Introduction352

5.6.1ACell re-selection for positioning352

5.6.1A.1Measurement and evaluation of serving cell353

5.6.1A.2Measurements of intra-frequency NR cells354

5.6.2RSTD measurements355

5.6.2.1Introduction355

5.6.2.2Requirements Applicability355

5.6.2.3Measurement Capability355

5.6.2.5Measurements Period Requirements355

5.6.2.6Measurements Period Requirements with Bandwidth Aggregation358

5.6.3PRS-RSRP measurements362

5.6.3.1Introduction362

5.6.3.2Requirements applicability362

5.6.3.3Measurement Capability362

5.6.3.4Measurement Reporting Requirements362

5.6.3.5Measurement Period Requirements363

5.6.4UE Rx-Tx time difference measurements365

5.6.4.1Introduction365

5.6.4.2Requirements Applicability365

5.6.4.3Measurement Capability365

5.6.4.4Measurement Reporting Requirements365

5.6.4.5Measurement Period Requirements366

5.6.4.6Measurement Period Requirements with Bandwidth Aggregation369

5.6.5PRS-RSRPP measurements373

5.6.5.1Introduction373

5.6.5.2Requirements Applicability373

5.6.5.3Measurement Capability373

5.6.5.4Measurement Reporting Requirements373

5.6.5.5Measurement Period Requirements373

5.6.6TA validation requirements for positioning373

5.6.6.1Introduction373

5.6.6.2TA validation requirements374

5.6.6.3TA validation requirements when configured with validity area374

5.6.7Measurement requirements for DL RSCPD reported with RSTD375

5.6.7.1Introduction375

5.6.7.2Requirements Applicability375

5.6.7.3Measurement Capability376

5.6.7.4Measurement Reporting Requirements376

5.6.7.5Measurements Period Requirements376

5.6.8Measurement requirements for DL RSCP reported with UE Rx-Tx time difference378

5.6.8.1Introduction378

5.6.8.2Requirements Applicability378

5.6.8.3Measurement Capability379

5.6.8.4Measurement Reporting Requirements379

5.6.8.5Measurement Period Requirements379

5.6ANR measurements for positioning for RedCap382

5.6A.1Introduction382

5.6A.2Cell re-selection for positioning382

5.6A.2.1Measurement and evaluation of serving cell383

5.6A.2.2Measurements of intra-frequency NR cells383

5.6A.3TA validation requirements for positioning SRS384

5.6A.3.1Introduction384

5.6A.3.2TA validation requirements384

5.6A.3.3TA validation requirements when configured with validity area384

5.6A.4RSTD measurements for RedCap385

5.6A.4.1 Introduction385

5.6A.4.2Requirements applicability385

5.6A.4.3Measurement Capability385

5.6A.4.4Measurement Reporting Requirements385

5.6A.4.5Measurement Period Requirement without RX FH386

5.6A.4.6Measurement Period Requirement with RX FH389

5.6A.5PRS-RSRP measurements for RedCap391

5.6A.5.1Introduction391

5.6A.5.2Requirements applicability391

5.6A.5.3Measurement Capability391

5.6A.5.4Measurement Reporting Requirements391

5.6A.5.5Measurement Period Requirements without RX FH392

5.6A.5.6Measurement Period Requirement with RX FH395

5.6A.6UE Rx-Tx time difference measurements for RedCap396

5.6A.6.1Introduction396

5.6A.6.2Requirements Applicability397

5.6A.6.3Measurement Capability397

5.6A.6.4Measurement Reporting Requirements397

5.6A.6.5Measurement Period Requirements without RX FH398

5.6A.6.6Measurement Period Requirements with RX FH398

5.6A.7PRS-RSRPP measurements for RedCap400

5.6A.7.1 Introduction400

5.6A.7.2Requirements applicability400

5.6A.7.3Measurement Capability401

5.6A.7.4Measurement Reporting Requirements401

5.6A.7.5Measurement Period Requirements without FH401

5.6A.7.6Measurement period requirement with FH401

5.6BReporting Delay Requirements for DL AI/ML Positioning401

5.6B.1Introduction401

5.6B.2Measurements Period Requirements402

5.6B.3 Measurements Period Requirements with Bandwidth Aggregation405

5.7Random access based Small Data Transmissions (RA-SDT)408

5.7.1Introduction408

5.7.2Requirements for small data transmissions based on 2-step RA408

5.7.3Requirements for small data transmissions based on 4-step RA408

5.7.4Applicability conditions for SDT408

5.7BRandom access based Small Data Transmissions (RA-SDT) for RedCap408

5.7B.1Introduction408

5.7B.2Requirements for small data transmissions based on 2-step RA408

5.7B.3Requirements for small data transmissions based on 4-step RA409

5.7B.4Applicability conditions for RA-SDT for RedCap409

5.7DRandom access based Small Data Transmissions (RA-SDT) for ATG409

5.7ERandom access based Small Data Transmissions (RA-SDT) for RedCap UEs with NTN409

5.7E.1Introduction409

5.7E.2Requirements for small data transmissions based on 2-step RA409

5.7E.3Requirements for small data transmissions based on 4-step RA409

5.7E.4Applicability conditions for RA-SDT409

5.8Measurement report for fast CA/DC setup409

5.8.1Introduction409

5.8.2Void410

5.8.3Measurement Report Requirements410

5.9INACTIVE mode measurement for LP-WUS operation410

5.9.1Introduction410

## 5.9.2 Requirements410

## 5.9.2.1 UE measurement capability410

## 5.9.2.1.1 LP-WUR measurement capability410

## 5.9.2.1.2 MR measurement capability with LP-WUR410

5.9.2.2LP-WUR serving cell measurement and evaluation requirements410

5.9.2.3Measurement and evaluation of serving cell by MR410

5.9.2.3A Measurement and evaluation of serving cell by Redcap410

5.9.2.4Measurements of intra-frequency NR cells for UE with LP-WUR411

5.9.2.4AMeasurements of intra-frequency NR cells for RedCap UE with LP-WUR411

5.9.2.5Measurements of inter-frequency NR cells for UE with LP-WUR411

5.9.2.5AMeasurements of inter-frequency NR cells for Redcap with LP-WUR411

5.9.2.6Measurements of inter-RAT E-UTRAN cells for UE with LP-WUR411

5.9.2.6AMeasurements of inter-RAT E-UTRAN cells for Redcap with LP-WUR411

6RRC_CONNECTED state mobility411

6.1Handover411

6.1.1NR Handover411

6.1.1.1Introduction411

6.1.1.2NR FR1 - NR FR1 Handover411

6.1.1.2.1Handover delay412

6.1.1.2.2Interruption time412

6.1.1.3NR FR2- NR FR1 Handover413

6.1.1.3.1Handover delay413

6.1.1.3.2Interruption time413

6.1.1.4NR FR2- NR FR2 Handover414

6.1.1.4.1Handover delay414

6.1.1.4.2Interruption time414

6.1.1.5NR FR1- NR FR2 Handover415

6.1.1.5.1Handover delay416

6.1.1.5.2Interruption time416

6.1.2NR Handover to other RATs417

6.1.2.1NR – E-UTRAN Handover417

6.1.2.1.1Introduction417

6.1.2.1.2Handover delay417

6.1.2.1.3Interruption time417

6.1.2.2NR – UTRAN Handover418

6.1.2.2.1Introduction418

6.1.2.2.2Handover delay418

6.1.2.2.3Interruption time418

6.1.3NR DAPS Handover419

6.1.3.1Introduction419

6.1.3.2NR FR1 - NR FR1 DAPS Handover419

6.1.3.2.1DAPS handover delay419

6.1.3.2.2Interruption time420

6.1.3.3NR FR2- NR FR1 DAPS Handover421

6.1.3.3.1DAPS handover delay422

6.1.3.3.2Interruption time422

6.1.3.4NR FR1- NR FR2 DAPS Handover422

6.1.3.4.1DAPS handover delay423

6.1.3.4.2Interruption time423

6.1.4NR Conditional Handover424

6.1.4.1Introduction424

6.1.4.2NR FR1 – NR FR1 conditional handover424

6.1.4.2.2Measurement time424

6.1.4.3NR FR2 – NR FR1 conditional handover426

6.1.4.4NR FR2 – NR FR2 conditional handover426

6.1.4.4.1Handover delay426

6.1.4.4.2Measurement time427

6.1.4.4.3Preparation time428

6.1.4.4.4Interruption time428

6.1.4.5NR FR1 – NR FR2 conditional handover428

6.1.5NR Handover with PSCell428

6.1.5.1Introduction428

6.1.5.2Handover with PSCell from NR SA to EN-DC429

6.1.5.2.1Interruption time for inter-RAT HO from NR to E-UTRAN429

6.1.5.2.2PSCell addition in HO with PSCell for NR SA to EN-DC429

6.1.5.3HO with PSCell from NE-DC to NE-DC430

6.1.5.3.1Handover delay430

6.1.5.3.2HO with PSCell - PCell Interruption time430

6.1.5.3.3PSCell addition/change in NE-DC to NE-DC HO with PSCell430

6.1.5.4HO with PSCell from NR-DC to NR-DC431

6.1.5.5Handover with PSCell from NR SA to EN-DC with PSCell using CCA432

6.1.5.5.1Introduction432

6.1.5.5.2NR SA to EN-DC HO with PSCell- NR to E-UTRA HO Interruption time432

6.1.5.5.3NR SA to EN-DC HO with PSCell - NR PSCell Addition Delay requirements433

6.1.6NR Conditional Handover including target MCG and target SCG434

6.1.6.1Conditional handover including target MCG in FR1 and target SCG in FR1 in NR-DC434

6.1.6.1.1CHO with PSCell – PCell Interruption time434

6.1.6.1.2CHO with PSCell – PSCell change delay435

6.1.6.2Conditional handover including target MCG in FR1 and target SCG in FR2 in NR-DC435

6.1.6.2.2CHO with PSCell – PSCell change delay436

6.1.7NR Conditional Handover including target MCG and candidate SCG437

6.1.7.1Conditional handover including target MCG and candidate SCG for CPC in FR1 NR-DC437

6.1.7.1.1PCell conditional handover delay438

6.1.7.1.2PSCell conditional change delay439

6.1.7.2Conditional handover including target MCG in FR1 and Candidate SCG for CPC in FR2 in NR-DC440

6.1.7.2.1PCell handover delay440

6.1.7.2.2PSCell conditional change delay441

6.1AVoid443

6.1A.1Void443

6.1A.1.1Void443

6.1A.1.2Void443

6.1A.1.2.1Void443

6.1A.1.2.2Void443

6.1BHandover to target cell using CCA443

6.1B.1NR Handover443

6.1B.1.1Introduction443

6.1B.1.2NR FR1 - NR FR1 Handover443

6.1B.1.2.1Handover delay443

6.1B.1.2.2Interruption time443

6.1B.1.3NR FR2-2 NR FR2-2 Handover444

6.1B.1.3.1Handover delay444

6.1B.1.3.2Interruption time444

6.1B.1.4NR FR1- NR FR2-2 Handover445

6.1B.1.4.1Handover delay445

6.1B.1.4.2Interruption time446

6.1CHandover for SAN447

6.1C.1NR SAN Handover447

6.1C.1.1Introduction447

6.1C.1.2NR SAN FR1 – NR SAN FR1 Handover447

6.1C.1.2.1Handover delay447

6.1C.1.2.2Interruption time447

6.1C.1.3NR SAN FR2-NTN – NR SAN FR2-NTN Handover448

6.1C.1.3.1Handover delay448

6.1C.1.3.2Interruption time449

6.1C.2NR SAN Conditional Handover449

6.1C.2.1Introduction449

6.1C.2.2NR SAN FR1 – NR SAN FR1 conditional handover450

6.1C.2.2.1Handover delay450

6.1C.2.2.2Measurement time450

6.1C.2.2.3Preparation time452

6.1C.2.2.4Interruption time452

6.1C.2.3NR SAN FR1 – NR SAN FR1 conditional handover without L3 measurement criteria452

6.1C.2.3.1Handover delay452

6.1C.2.3.2Preparation time453

6.1C.2.3.3Interruption time453

6.1C.2.4NR SAN FR2-NTN – NR SAN FR2-NTN conditional handover454

6.1C.3NR SAN Satellite switching with re-synchronization454

6.1C.3.1Introduction454

6.1C.3.2NR SAN FR1 – NR SAN FR1 Satellite switching with re-synchronization454

6.1C.3.2.1Satellite switching delay454

6.1C.3.2.2Interruption time for hard satellite switch with re-sync454

6.1C.3.3NR SAN FR2 – NR SAN FR2 Satellite switching with re-synchronization456

6.1C.3.3.1Satellite switching delay456

6.1C.3.3.2Interruption time for hard satellite switch with re-sync456

6.1C.3.3.3Satellite switch delay for soft satellite switch with re-sync457

6.1DHandover for RedCap457

6.1D.1NR Handover457

6.1D.1.1Introduction457

6.1D.1.2NR FR1 - NR FR1 Handover458

6.1D.1.2.1Handover delay458

6.1D.1.2.2Interruption time458

6.1D.1.3NR FR2- NR FR2 Handover459

6.1D.1.3.1Handover delay459

6.1D.1.3.2Interruption time459

6.1D.2NR Handover to other RATs461

6.1D.2.1NR – E-UTRAN Handover461

6.1EHandover for ATG461

6.1E.1NR Handover461

6.1E.1.1Introduction461

6.1E.1.2NR FR1 - NR FR1 Handover461

6.1E.1.2.1Handover delay461

6.1E.1.2.2Interruption time461

6.1E.2NR Conditional Handover462

6.1E.2.1Introduction462

6.1E.2.2NR FR1 – NR FR1 conditional handover462

6.1E.2.2.1Handover delay462

6.1E.2.2.2Measurement time463

6.1E.2.2.3Preparation time463

6.1E.2.2.4Interruption time463

6.1FHandover for RedCap UE with satellite access464

6.1F.1NR SAN Handover464

6.1F.1.1Introduction464

6.1F.1.2NR SAN FR1 – NR SAN FR1 Handover464

6.1F.1.2.1Handover delay464

6.1F.1.2.2Interruption time464

6.1F.2NR SAN Conditional Handover464

6.1F.2.1Introduction464

6.1F.2.2NR SAN FR1 – NR SAN FR1 conditional handover465

6.1F.2.2.1Handover delay465

6.1F.2.2.2Measurement time465

6.1F.2.2.3Preparation time465

6.1F.2.2.4Interruption time465

6.1F.2.3NR SAN FR1 – NR SAN FR1 conditional handover without L3 measurement criteria465

6.1F.2.3.1Handover delay465

6.1F.2.3.2Preparation time465

6.1F.2.3.3Interruption time465

6.1F.3NR SAN Satellite switching with re-synchronization466

6.1F.3.1Introduction466

6.1F.3.2NR SAN FR1 – NR SAN FR1 Satellite switching with re-synchronization466

6.1F.3.2.1Satellite switching delay466

6.1F.3.2.2Interruption time for hard satellite switch with re-sync466

6.1F.3.2.3Satellite switch delay for soft satellite switch with re-sync466

6.2RRC Connection Mobility Control467

6.2.1SA: RRC Re-establishment467

6.2.1.1Introduction467

6.2.1.2Requirements467

6.2.1.2.1UE Re-establishment delay requirement467

6.2.1ARRC Re-establishment with CCA469

6.2.1A.1Introduction469

6.2.1A.2Requirements470

6.2.1A.2.1UE Re-establishment with CCA delay requirement470

6.2.1BSA: RRC Re-establishment for RedCap471

6.2.1B.1Introduction471

6.2.1B.2Requirements472

6.2.2Random access472

6.2.2.1Introduction472

6.2.2.2Requirements for 4-step RA type472

6.2.2.2.1Contention based random access473

6.2.2.2.1.1Correct behaviour when transmitting Random Access Preamble473

6.2.2.2.1.2Correct behaviour when receiving Random Access Response473

6.2.2.2.1.3Correct behaviour when not receiving Random Access Response473

6.2.2.2.1.4Correct behaviour when receiving an UL grant for msg3 retransmission473

6.2.2.2.1.5SA: Correct behaviour when receiving a message over Temporary C-RNTI473

6.2.2.2.1.6Correct behaviour when contention Resolution timer expires473

6.2.2.2.2Non-Contention based random access474

6.2.2.2.2.1Correct behaviour when transmitting Random Access Preamble474

6.2.2.2.2.2Correct behaviour when receiving Random Access Response474

6.2.2.2.2.3Correct behaviour when not receiving Random Access Response474

6.2.2.2.3UE behaviour when configured with supplementary UL475

6.2.2.3Requirements for 2-step RA type475

6.2.2.3.1Contention based random access475

6.2.2.3.1.1Correct behaviour when transmitting MsgA475

6.2.2.3.1.2Correct behaviour when receiving MsgB475

6.2.2.3.1.3Correct behaviour when not receiving MsgB476

6.2.2.3.2Non-Contention based random access476

6.2.2.3.2.1Correct behaviour when transmitting MsgA476

6.2.2.3.2.2Correct behaviour when receiving MsgB476

6.2.2.3.2.3Correct behaviour when not receiving MsgB476

6.2.2.3.3UE behaviour when configured with supplementary UL476

6.2.2ARandom access when CCA is used on target frequency477

6.2.2A.1Introduction477

6.2.2A.2Requirements for 4-step RA type477

6.2.2A.2.1Contention based random access477

6.2.2A.2.1.1Correct behaviour when transmitting Random Access Preamble477

6.2.2A.2.1.2Correct behaviour when receiving Random Access Response478

6.2.2A.2.1.3Correct behaviour when not receiving Random Access Response478

6.2.2A.2.1.4Correct behaviour when receiving an UL grant for msg3 retransmission478

6.2.2A.2.1.6Correct behaviour when contention Resolution timer expires478

6.2.2A.2.2Non-Contention based random access478

6.2.2A.2.2.1Correct behaviour when transmitting Random Access Preamble478

6.2.2A.2.2.2Correct behaviour when receiving Random Access Response479

6.2.2A.2.2.3Correct behaviour when not receiving Random Access Response479

6.2.2A.3Requirements for 2-step RA type479

6.2.2A.3.1Contention based random access479

6.2.2A.3.1.1Correct behaviour when transmitting MsgA479

6.2.2A.3.1.2Correct behaviour when receiving MsgB480

6.2.2A.3.1.3Correct behaviour when not receiving MsgB480

6.2.2A.3.2Non-Contention based random access480

6.2.2A.3.2.1Correct behaviour when transmitting MsgA480

6.2.2A.3.2.2Correct behaviour when receiving MsgB481

6.2.2A.3.2.3Correct behaviour when not receiving MsgB481

6.2.2BRandom access for RedCap481

6.2.2B.1Introduction481

6.2.2B.2Requirements482

6.2.2CPDCCH ordered Random Access for LTM482

6.2.2C.1Introduction482

6.2.2C.2PDCCH ordered Random Access delay482

6.2.3SA: RRC Connection Release with Redirection483

6.2.3.1Introduction483

6.2.3.2Requirements483

6.2.3.2.1RRC connection release with redirection to NR483

6.2.3.2.2RRC connection release with redirection to E-UTRAN484

6.2.3.2.3RRC connection release with redirection to NR carrier subject to CCA485

6.2.3ASA: RRC Connection Release with Redirection for RedCap486

6.2.3A.1Introduction486

6.2.3A.2Requirements486

6.2.3A.2.1RRC connection release with redirection to NR486

6.2.3A.2.2RRC connection release with redirection to E-UTRAN486

6.2CRRC Connection Mobility Control for Satellite Access487

6.2C.1SA: RRC Re-establishment for Satellite Access487

6.2C.1.1Introduction487

6.2C.1.2Requirements487

6.2C.1.2.1UE Re-establishment delay requirement487

6.2C.1.2.2UE Re-establishment delay requirement for VSAT489

6.2C.2Random access for satellite access489

6.2C.2.1Introduction489

6.2C.2.2Requirements for 4-step RA type489

6.2C.2.2.1Contention based random access490

6.2C.2.2.1.1Correct behaviour when transmitting Random Access Preamble490

6.2C.2.2.1.2Correct behaviour when receiving Random Access Response490

6.2C.2.2.1.3Correct behaviour when not receiving Random Access Response490

6.2C.2.2.1.4Correct behaviour when receiving an UL grant for msg3 retransmission490

6.2C.2.2.1.5SA: Correct behaviour when receiving a message over Temporary C-RNTI490

6.2C.2.2.1.6Correct behaviour when Contention Resolution Timer expires490

6.2C.2.2.2Non-Contention based random access491

6.2C.2.2.2.1Correct behaviour when transmitting Random Access Preamble491

6.2C.2.2.2.2Correct behaviour when receiving Random Access Response491

6.2C.2.2.2.3Correct behaviour when not receiving Random Access Response491

6.2C.2.3Requirements for 2-step RA type492

6.2C.2.3.1Contention based random access492

6.2C.2.3.1.1Correct behaviour when transmitting MsgA492

6.2C.2.3.1.2Correct behaviour when receiving MsgB492

6.2C.2.3.1.3Correct behaviour when not receiving MsgB493

6.2C.2.3.2Non-Contention based random access493

6.2C.2.3.2.1Correct behaviour when transmitting MsgA493

6.2C.2.3.2.2Correct behaviour when receiving MsgB493

6.2C.2.3.2.3Correct behaviour when not receiving MsgB493

6.2C.3SA: RRC Connection Release with Redirection for Satellite Access493

6.2C.3.1Introduction493

6.2C.3.2Requirements494

6.2C.3.2.1RRC connection release with redirection to NR494

6.2DRRC Connection Mobility Control for ATG495

6.2D.1SA: RRC Re-establishment495

6.2D.1.1Introduction495

6.2D.1.2Requirements495

6.2D.1.2.1UE Re-establishment delay requirement495

6.2D.2Random access496

6.2D.2.1Introduction496

6.2D.2.2Requirements for 4-step RA type496

6.2D.2.3Requirements for 2-step RA type497

6.2D.3SA: RRC Connection Release with Redirection497

6.2D.3.1Introduction497

6.2D.3.2Requirements497

6.2D.3.2.1RRC connection release with redirection to NR497

6.2ERRC Connection Mobility Control for RedCap UE with Satellite Access498

6.2E.1SA: RRC Re-establishment for RedCap UE with Satellite Access498

6.2E.1.1Introduction498

6.2E.1.2Requirements498

6.2E.2Random access for RedCap UE with satellite access499

6.2E.2.1Introduction499

6.2E.2.2Requirements499

6.2E.3SA: RRC Connection Release with Redirection for RedCap UE with Satellite Access499

6.2E.3.1Introduction499

6.2E.3.2Requirements500

6.2E.3.2.1RRC connection release with redirection to NR500

6.3L1/L2-Triggered Mobility500

6.3.1LTM PCell Cell Switch500

6.3.1.1Introduction500

6.3.1.2LTM Cell Switch delay502

6.3.1.3Interruption time502

6.3.2Conditional L1/L2-Triggered Mobility503

6.3.2.1Introduction503

6.3.2.2CLTM Cell Switch delay504

6.3.2.2.1Measurement time504

6.3.2.2.2CLTM RRC processing time505

6.3.2.2.3Interruption time506

6.3.2.3Subsequent CLTM Cell Switch delay507

7Timing507

7.1UE transmit timing507

7.1.1Introduction507

7.1.2Requirements508

7.1.2.1Gradual timing adjustment510

7.1.2.2Void511

7.1.2.3One shot large UL timing adjustment for FR2 Power Class 6 UE511

7.1.2.4UE transmit timing for positioning measurements512

7.1AUE transmit timing for RedCap512

7.1A.1Introduction512

7.1A.2Requirements512

7.1A.2.1Gradual timing adjustment513

7.1A.2.2UE transmit timing for positioning measurements514

7.1CUE transmit timing for Satellite Access514

7.1C.1Introduction514

7.1C.2Requirements514

7.1C.2.1Gradual timing adjustment516

7.1DUE transmit timing for ATG516

7.1D.1Introduction516

7.1D.2Requirements516

7.1D.2.1Gradual timing adjustment517

7.1EUE transmit timing for RedCap with Satellite Access517

7.1E.1Introduction517

7.1E.2Requirements518

7.1E.2.1Gradual timing adjustment518

7.2UE timer accuracy518

7.2.1Introduction518

7.2.2Requirements518

7.2AUE timer accuracy for RedCap518

7.2A.1Introduction518

7.2A.2Requirements518

7.2CUE timer accuracy for satellite access519

7.2C.1Introduction519

7.2C.2Requirements519

7.2DUE timer accuracy for ATG519

7.2D.1Introduction519

7.2D.2Requirements519

7.2EUE timer accuracy for RedCap with Satellite Access520

7.2E.1Introduction520

7.2E.2Requirements520

7.3Timing advance520

7.3.1Introduction520

7.3.2Requirements520

7.3.2.1Timing Advance adjustment delay520

7.3.2.2Timing Advance adjustment accuracy520

7.3ATiming Advance for RedCap520

7.3A.1Introduction520

7.3A.2Requirements521

7.3A.2.1Timing Advance adjustment delay521

7.3A.2.2Timing Advance adjustment accuracy521

7.3CTiming advance for satellite access521

7.3C.1Introduction521

7.3C.2Requirements521

7.3C.2.1Timing Advance adjustment delay521

7.3C.2.2Timing Advance adjustment accuracy521

7.3DTiming advance for ATG522

7.3D.1Introduction522

7.3D.2Requirements522

7.3D.2.1Timing Advance adjustment delay522

7.3D.2.2Timing Advance adjustment accuracy522

7.3ETiming advance for RedCap with Satellite Access522

7.3E.1Introduction522

7.3E.2Requirements522

7.3E.2.1Timing Advance adjustment delay522

7.3E.2.2Timing Advance adjustment accuracy522

7.4Cell phase synchronization accuracy522

7.4.1Definition522

7.4.2Minimum requirements523

7.5Maximum Transmission Timing Difference523

7.5.1Introduction523

7.5.2Minimum requirements for inter-band EN-DC523

7.5.2.1Minimum requirements for inter-band synchronous EN-DC523

7.5.3Minimum requirements for intra-band EN-DC524

7.5.4Minimum requirements for NR Carrier Aggregation525

7.5.5Minimum requirements for inter-band NE-DC526

7.5.5.1Minimum requirements for inter-band synchronous NE-DC526

7.5.6Minimum requirements for inter-band NR-DC526

7.5.7Minimum requirements for multi-TRP527

7.6Maximum Receive Timing Difference528

7.6.1Introduction528

7.6.2Minimum requirements for inter-band EN-DC528

7.6.2.1Minimum requirements for inter-band synchronous EN-DC529

7.6.3Minimum requirements for intra-band EN-DC530

7.6.4Minimum requirements for NR Carrier Aggregation530

7.6.5Minimum requirements for inter-band NE-DC532

7.6.5.1Minimum requirements for inter-band synchronous NE-DC532

7.6.6Minimum requirements for inter-band NR-DC532

7.6.7Minimum requirements for PC6 UE in FR2533

7.6.8Minimum requirements for Multi-TRPs533

7.6DMaximum Receive Timing Difference for ATG UE534

7.6D.1Introduction534

7.6D.2Minimum requirements for NR Carrier Aggregation534

7.7deriveSSB-IndexFromCell tolerance534

7.7.1Minimum requirements534

7.7AderiveSSB-IndexFromCell tolerance for RedCap535

7.7A.1Minimum requirements535

7.7DDeriveSSB-IndexFromCell tolerance for ATG535

7.7D.1Minimum requirements535

7.8Void535

7.9deriveSSB-IndexFromCellInter-r17 tolerance535

7.9.1Minimum requirements535

7.9DDeriveSSB-IndexFromCellInter-r17 tolerance for ATG536

7.9D.1Minimum requirements536

8Signalling characteristics590

8.1Radio Link Monitoring590

8.1.1Introduction590

8.1.1.1Introduction of Requirement on Radio Link Monitoring for UE Configured with Relaxed Measurement Criteria591

8.1.2Requirements for SSB based radio link monitoring592

8.1.2.1Introduction592

8.1.2.2Minimum requirement593

8.1.2.3Measurement restrictions for SSB based RLM597

8.1.2.4Minimum requirement of SSB based radio link monitoring for UE fulfilling relaxed measurement criteria598

8.1.3Requirements for CSI-RS based radio link monitoring599

8.1.3.1Introduction599

8.1.3.2Minimum requirement599

8.1.3.3Measurement restrictions for CSI-RS based RLM604

8.1.3.4Minimum requirement of CSI-RS based radio link monitoring for UE fulfilling relaxed measurement criteria606

8.1.4Minimum requirement at transitions606

8.1.5Minimum requirement for UE turning off the transmitter607

8.1.6Minimum requirement for L1 indication607

8.1.7Scheduling availability of UE during radio link monitoring607

8.1.7.1Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1607

8.1.7.2Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1608

8.1.7.3Scheduling availability of UE performing radio link monitoring on FR2608

8.1.7.4Scheduling availability of UE performing radio link monitoring on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC609

8.1.8Minimum requirement under IDC Interference610

8.1ARadio Link Monitoring with CCA on Target Frequency610

8.1A.1Introduction610

8.1A.2Requirements for SSB Based Radio Link Monitoring611

8.1A.2.1Introduction611

8.1A.2.2Minimum Requirement611

8.1A.2.3Measurement Restrictions for SSB based RLM614

8.1A.3Minimum requirement at transitions614

8.1A.4Minimum requirement for UE turning off the transmitter615

8.1A.5Minimum requirement for L1 indication615

8.1A.6Scheduling availability of UE during radio link monitoring615

8.1A.6.3Scheduling availability of UE performing radio link monitoring on FR2-2615

8.1A.6.4Scheduling availability of UE performing radio link monitoring on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR-DC616

8.1BRadio Link Monitoring for RedCap616

8.1B.1Introduction616

8.1B.2Requirements for SSB based radio link monitoring617

8.1B.2.1Introduction617

8.1B.2.2Minimum requirement618

8.1B.2.3Measurement restrictions for SSB based RLM620

8.1B.3Requirements for CSI-RS based radio link monitoring620

8.1B.3.1Introduction620

8.1B.3.2Minimum requirement621

8.1B.3.3Measurement restrictions for CSI-RS based RLM623

8.1B.4Minimum requirement at transitions624

8.1B.5Minimum requirement for UE turning off the transmitter624

8.1B.6Minimum requirement for L1 indication624

8.1B.7Scheduling availability of UE during radio link monitoring625

8.1B.7.1Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1625

8.1B.7.2Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1625

8.1B.7.3Scheduling availability of UE performing radio link monitoring on FR2625

8.1CRadio Link Monitoring for Satellite Access626

8.1C.1Introduction626

8.1C.2Requirements for SSB based radio link monitoring627

8.1C.2.1Introduction627

8.1C.2.2Minimum requirement628

8.1C.2.3Measurement restrictions for SSB based RLM629

8.1C.3Requirements for CSI-RS based radio link monitoring630

8.1C.3.1Introduction630

8.1C.3.2Minimum requirement630

8.1C.3.3Measurement restrictions for CSI-RS based RLM632

8.1C.4Minimum requirement at transitions632

8.1C.5Minimum requirement for UE turning off the transmitter632

8.1C.6Minimum requirement for L1 indication633

8.1C.7Scheduling availability of UE during radio link monitoring633

8.1C.7.1Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1-NTN and FR2-NTN633

8.1C.7.2Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1-NTN and FR2-NTN633

8.1DRadio Link Monitoring for ATG633

8.1D.1Introduction633

8.1D.2Requirements for SSB based radio link monitoring634

8.1D.2.1Introduction634

8.1D.2.2Minimum requirement635

8.1D.2.3Measurement restrictions for SSB based RLM636

8.1D.3Requirements for CSI-RS based radio link monitoring636

8.1D.3.1Introduction636

8.1D.3.2Minimum requirement636

8.1D.3.3Measurement restrictions for CSI-RS based RLM638

8.1D.4Minimum requirement at transitions638

8.1D.5Minimum requirement for UE turning off the transmitter638

8.1D.6Minimum requirement for L1 indication638

8.1D.7Scheduling availability of UE during radio link monitoring638

8.1D.7.1Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1638

8.1D.7.2Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1638

8.1ERadio Link Monitoring for RedCap UE with Satellite Access639

8.1E.1Introduction639

8.1E.2Requirements for SSB based radio link monitoring639

8.1E.2.1Introduction639

8.1E.2.2Minimum requirement640

8.1E.2.3Measurement restrictions for SSB based RLM640

8.1E.3Requirements for CSI-RS based radio link monitoring640

8.1E.3.1Introduction640

8.1E.3.2Minimum requirement641

8.1E.3.3Measurement restrictions for CSI-RS based RLM642

8.1E.4Minimum requirement at transitions642

8.1E.5Minimum requirement for UE turning off the transmitter642

8.1E.6Minimum requirement for L1 indication642

8.1E.7Scheduling availability of UE during radio link monitoring642

8.1E.7.1Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH642

8.1E.7.2Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH642

8.2Interruption642

8.2.1EN-DC Interruption642

8.2.1.1Introduction642

8.2.1.2Requirements643

8.2.1.2.1Interruptions at transitions between active and non-active during DRX643

8.2.1.2.2Interruptions at transitions from non-DRX to DRX644

8.2.1.2.3Interruptions at SCell addition/release644

8.2.1.2.4Interruptions at SCell activation/deactivation646

8.2.1.2.5Interruptions during measurements on SCC649

8.2.1.2.6Interruptions at UL carrier RRC reconfiguration651

8.2.1.2.7Interruptions due to Active BWP switching Requirement651

8.2.1.2.8Interruptions at direct SCell activation and hibernation652

8.2.1.2.9Interruptions at SCell hibernation653

8.2.1.2.10Interruptions at SCell activation/deactivation with multiple downlink SCells653

8.2.1.2.11Interruptions due to UE-specific CBW change653

8.2.1.2.12Interruptions at NR SRS carrier based switching654

8.2.1.2.13Interruptions at E-UTRA SRS carrier based switching655

8.2.1.2.14DL Interruptions at switching between two uplink carriers656

8.2.1.2.15Interruptions due to SCell dormancy656

8.2.1.2.16Interruptions when identifying CGI of an NR cell with autonomous gaps657

8.2.1.2.17Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps657

8.2.1.2.18Interruptions at NR SRS antenna port switching658

8.2.1.2.19Interruptions at fast SCell activation659

8.2.1.2.20Interruptions due to PUCCH SCell activation/deactivation660

8.2.1.2.21Interruptions at OD-SSB activation/deactivation660

8.2.2SA: Interruptions with Standalone NR Carrier Aggregation661

8.2.2.1Introduction661

8.2.2.2Requirements662

8.2.2.2.1Interruptions at SCell addition/release662

8.2.2.2.2Interruptions at SCell activation/deactivation663

8.2.2.2.3Interruptions during measurements on deactivated SCC665

8.2.2.2.4Interruptions at UL carrier RRC reconfiguration667

8.2.2.2.5Interruptions due to Active BWP switching Requirement667

8.2.2.2.6Interruptions at inter-frequency SFTD measurement669

8.2.2.2.7Interruptions at SCell activation/deactivation with multiple downlink SCells670

8.2.2.2.8Interruptions due to UE-specific CBW change670

8.2.2.2.9Interruptions at NR SRS carrier based switching670

8.2.2.2.10DL Interruptions at UE switching between two uplink carriers672

8.2.2.2.10ADL Interruptions at UE switching between two uplink carriers with two transmit antenna connectors672

8.2.2.2.10BDL Interruptions at UE switching between one uplink band with one transmit antenna connector and one uplink band with two transmit antenna connectors673

8.2.2.2.10CDL Interruptions at UE switching between two uplink bands with two transmit antenna connectors673

8.2.2.2.10DDL Interruptions at UE switching across three or four uplink bands673

8.2.2.2.10EDL Interruptions at UE switching between two uplink bands with three transmit antenna connectors and maximum two transmit antenna connectors for each band674

8.2.2.2.11Interruptions at direct SCell activation675

8.2.2.2.12Interruptions due to SCell dormancy675

8.2.2.2.12.1Interruptions due to SCell dormancy switch675

8.2.2.2.12.2Interruptions due to CQI measurements during SCell dormancy675

8.2.2.2.12.3Interruptions due to RRM measurements during SCell dormancy675

8.2.2.2.13Interruptions at transitions between active and non-active during DRX675

8.2.2.2.14Interruptions when identifying CGI of an NR cell with autonomous gaps675

8.2.2.2.15Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps676

8.2.2.2.16Interruptions at NR SRS antenna port switching677

8.2.2.2.17Interruptions at fast SCell activation677

8.2.2.2.18Interruptions due to PUCCH SCell activation/deactivation678

8.2.2.2.19Interruptions due to measurements without gap carried out by UE supporting NeedForInterruptionInfoNR678

8.2.2.2.20Interruptions due to PDCCH ordered RACH on target LTM cell679

8.2.2.2.21Interruptions at NR SRS bandwidth aggregation for positioning680

8.2.2.2.22Interruptions at OD-SSB activation/deactivation682

8.2.3NE-DC Interruptions683

8.2.3.1Introduction683

8.2.3.2Requirements684

8.2.3.2.1Interruptions at transitions between active and non-active during DRX684

8.2.3.2.2Interruptions at transitions from non-DRX to DRX684

8.2.3.2.3Interruptions at PSCell/SCell addition/release684

8.2.3.2.4Interruptions at SCell activation/deactivation685

8.2.3.2.5Interruptions during measurements on SCC687

8.2.3.2.5.1Interruptions during measurements on deactivated NR SCC687

8.2.3.2.5.2Interruptions during measurements on deactivated E-UTRAN SCC687

8.2.3.2.5.3Interruptions during CQI measurements on dormant E-UTRAN SCC687

8.2.3.2.5.4Interruptions during RRM measurements on dormant E-UTRAN SCC687

8.2.3.2.6Interruptions at UL carrier RRC reconfiguration688

8.2.3.2.7Interruptions due to Active BWP switching Requirement688

8.2.3.2.8Interruptions at direct SCell activation and hibernation688

8.2.3.2.9Interruptions at SCell hibernation689

8.2.3.2.10Interruptions at SCell activation/deactivation with multiple downlink SCells689

8.2.3.2.11Interruptions at NR SRS carrier based switching689

8.2.3.2.12Interruptions at E-UTRA SRS carrier based switching691

8.2.3.2.13Interruptions due to SCell dormancy691

8.2.3.2.14Interruptions when identifying CGI of an NR cell with autonomous gaps692

## 8.2.3.2.15 Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps692

8.2.3.2.17Interruptions at fast SCell activation694

8.2.3.2.18Interruptions due to UE-specific CBW change694

8.2.3.2.19Interruptions due to PUCCH SCell activation/deactivation695

8.2.3.2.20Interruptions at OD-SSB activation/deactivation695

8.2.4NR-DC: Interruptions695

8.2.4.1Introduction695

8.2.4.2Requirements696

8.2.4.2.1Interruptions at PSCell/SCell addition/release696

8.2.4.2.2Interruptions at SCell activation/deactivation697

8.2.4.2.3Interruptions during measurements on SCC698

8.2.4.2.4Interruptions at UL carrier RRC reconfiguration698

8.2.4.2.5Interruptions due to Active BWP switching Requirement699

8.2.4.2.6Interruptions at transitions between active and non-active during DRX699

8.2.4.2.7Interruptions at transitions from non-DRX to DRX699

8.2.4.2.8Interruptions at SCell activation/deactivation with multiple downlink SCells700

8.2.4.2.9Interruptions at NR SRS carrier based switching700

8.2.4.2.10Interruptions at direct SCell activation701

8.2.4.2.11Interruptions when identifying CGI of an NR cell with autonomous gaps702

8.2.4.2.12Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps702

## 8.2.4.2.13 Interruptions due to SCell dormancy703

8.2.4.2.14Interruptions at NR SRS antenna port switching703

8.2.4.2.15Interruptions at fast SCell activation704

8.2.4.2.16Interruptions at SCG activation/deactivation705

8.2.4.2.17Interruptions due to RRM measurements on deactivated SCG705

8.2.4.2.18Interruptions during RLM/BFD measurements on deactivated PSCell705

8.2.4.2.19Interruptions due to UE-specific CBW change705

8.2.4.2.20Interruptions due to PDCCH ordered RACH on target LTM cell706

8.2.4.2.21Interruptions at PSCell Cell switch706

8.2.4.2.22Interruptions at OD-SSB activation/deactivation706

8.2.4.2AVoid707

8.2.4.2A.1Void707

8.2.4.2A.2Void707

8.2.4.2A.3Void707

8.2DInterruption for ATG UE707

8.2D.1Interruptions with Standalone NR Carrier Aggregation707

8.2D.1.1Introduction707

8.2D.1.2Requirements708

8.2D.1.2.1Interruptions at SCell addition/release708

8.2D.1.2.2Interruptions at SCell activation/deactivation708

8.2D.1.2.3Interruptions during measurements on deactivated SCC709

8.2D.1.2.4Interruptions at direct SCell activation709

8.2D.1.2.5Interruptions due to SCell dormancy710

8.2D.1.2.6Interruptions at fast SCell activation710

8.2D.1.2.8Interruptions due to UE-specific CBW change711

8.2D.1.2.9Interruptions when identifying CGI of an NR cell with autonomous gaps712

8.2D.1.2.10Interruptions at NR SRS antenna port switching712

8.3SCell Activation and Deactivation Delay713

8.3.1Introduction713

8.3.2SCell Activation Delay Requirement for Deactivated SCell713

8.3.2ASCell Activation Delay Requirement for Deactivated SCell based on measurement in IDLE/INACTIVE mode721

8.3.3SCell Deactivation Delay Requirement for Activated SCell723

8.3.4Direct SCell Activation at SCell addition724

8.3.5Direct SCell Activation at Handover726

8.3.7SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells728

8.3.8SCell Deactivation Delay Requirement for Activated SCell with Multiple Downlink SCells732

8.3.9Direct SCell Activation of Multiple Downlink SCells at SCell addition732

8.3.10Direct SCell Activation of Multiple Downlink SCells at Handover733

8.3.12SCell Activation Delay Requirement for Deactivated PUCCH SCell735

8.3.13SCell activation delay Requirement for Deactivated PUCCH SCell with Multiple SCells739

8.3.14SCell Deactivation Delay Requirement for Activated PUCCH SCell741

8.3.15SCell Deactivation Delay Requirement for Activated PUCCH SCell with Multiple Downlink SCells741

8.3.16Fast SCell Activation Delay Requirement for Deactivated SCell742

8.3.17SCell Activation Delay Requirement for Deactivated SCell with the L3 reporting during activation744

8.3.18SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells with L3 reporting748

8.3.19OD-SSB based SCell Activation Delay Requirement for Deactivated SCell751

8.3.20OD-SSB based SCell Deactivation Delay Requirement for Activated SCell755

8.3.21OD-SSB based Direct SCell Activation at SCell addition756

8.3.22OD-SSB based SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells757

8.3.23OD-SSB based SCell Deactivation Delay Requirement for Activated SCell with Multiple Downlink SCells761

8.3.25OD-SSB based SCell Deactivation Delay Requirement for Activated PUCCH SCell762

8.3.26OD-SSB based SCell Activation Delay Requirement for Deactivated SCell with the L3 reporting during activation762

8.3ASCell Activation and Deactivation Delay in Carriers with CCA763

8.3A.1Introduction763

8.3A.2SCell Activation Delay Requirement for Deactivated SCell763

8.3A.3SCell Deactivation Delay Requirement for Activated SCell767

8.3DSCell Activation and Deactivation Delay for ATG768

8.3D.1Introduction768

8.3D.2SCell Activation Delay Requirement for Deactivated SCell768

8.3D.3SCell Deactivation Delay Requirement for Activated SCell773

8.3D.4Direct SCell Activation at SCell addition773

8.3D.5Direct SCell Activation at Handover774

8.3D.6Direct SCell Activation at RRC Resume776

8.3D.7Fast SCell Activation Delay Requirement for Deactivated SCell776

8.3D.8SCell Activation Delay Requirement for Deactivated SCell with the L3 reporting during activation778

8.4UE UL carrier RRC reconfiguration delay780

8.4.1Introduction780

8.4.2UE UL carrier configuration delay requirement781

8.4.3UE UL carrier deconfiguration delay requirement781

8.5Link Recovery Procedures781

8.5.1Introduction781

8.5.1.1Introduction of Requirement on Link Recovery Procedures for UE configured with relaxed measurement criteria782

8.5.2Requirements for SSB based beam failure detection783

8.5.2.1Introduction783

8.5.2.2Minimum requirement784

8.5.2.3Measurement restriction for SSB based beam failure detection788

8.5.2.4Minimum requirement of SSB based beam failure detection for UE fulfilling relaxed measurement criteria789

8.5.3Requirements for CSI-RS based beam failure detection790

8.5.3.1Introduction790

8.5.3.2Minimum requirement791

8.5.3.3Measurement restrictions for CSI-RS beam failure detection795

8.5.3.4Minimum requirement of CSI-RS based beam failure detection for UE fulfilling relaxed measurement criteria797

8.5.4Minimum requirement for L1 indication798

8.5.5Requirements for SSB based candidate beam detection798

8.5.5.1Introduction798

8.5.5.2Minimum requirement799

8.5.5.3Measurement restriction for SSB based candidate beam detection803

8.5.6Requirements for CSI-RS based candidate beam detection804

8.5.6.1Introduction804

8.5.6.2Minimum requirement804

8.5.6.3Measurement restriction for CSI-RS based candidate beam detection809

8.5.7Scheduling availability of UE during beam failure detection810

8.5.7.1Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1810

8.5.7.2Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1810

8.5.7.3Scheduling availability of UE performing beam failure detection on FR2811

8.5.7.4Scheduling availability of UE performing beam failure detection on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC812

8.5.8Scheduling availability of UE during candidate beam detection812

8.5.8.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1812

8.5.8.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1812

8.5.8.3Scheduling availability of UE performing L1-RSRP measurement on FR2813

8.5.8.4Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC814

8.5.9Requirements for Beam Failure Recovery in SCell814

8.5.9.1Introduction814

8.5.9.2Requirement814

8.5.10Minimum requirement at transitions for beam failure detection814

8.5.11Minimum requirement under IDC Interference815

8.5.12Minimum requirement at transitions for candidate beam detection815

8.5ALink Recovery Procedures when CCA is used on target frequency815

8.5A.1Introduction815

8.5A.2Requirements for SSB based beam failure detection816

8.5A.2.1Introduction816

8.5A.2.2Minimum requirement816

8.5A.2.3Measurement restriction for SSB based beam failure detection818

8.5A.3Void819

8.5A.4Minimum requirement for L1 indication819

8.5A.5Requirements for SSB based candidate beam detection819

8.5A.5.1Introduction819

8.5A.5.2Minimum requirement819

8.5A.5.3Measurement restriction for SSB based candidate beam detection822

8.5A.6Void822

8.5A.7Scheduling availability of UE during beam failure detection822

8.5A.7.1Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH822

8.5A.7.2Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH822

8.5A.7.3Scheduling availability of UE performing beam failure detection on FR2-2823

8.5A.7.4Scheduling availability of UE performing beam failure detection on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR-DC823

8.5A.8Scheduling availability of UE during candidate beam detection823

8.5A.8.3Scheduling availability of UE performing L1-RSRP measurement on FR2-2823

8.5.8A.4Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR-DC823

8.5BLink Recovery Procedures for Redcap823

8.5B.1Introduction823

8.5B.2Requirements for SSB based beam failure detection for Redcap824

8.5B.2.1Introduction824

8.5B.2.2Minimum requirement824

8.5B.2.3Measurement restriction for SSB based beam failure detection826

8.5B.3Requirements for CSI-RS based beam failure detection for Redcap826

8.5B.3.1Introduction826

8.5B.3.2Minimum requirement826

8.5B.3.3Measurement restrictions for CSI-RS beam failure detection828

8.5B.4Minimum requirement for L1 indication for Redcap829

8.5B.5Requirements for SSB based candidate beam detection for Redcap830

8.5B.5.1Introduction830

8.5B.5.2Minimum requirement830

8.5B.5.3Measurement restriction for SSB based candidate beam detection831

8.5B.6Requirements for CSI-RS based candidate beam detection for Redcap832

8.5B.6.1Introduction832

8.5B.6.2Minimum requirement832

8.5B.6.3Measurement restriction for CSI-RS based candidate beam detection834

8.5B.7Scheduling availability of UE during beam failure detection for Redcap834

8.5B.7.1Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1835

8.5B.7.2Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1835

8.5B.7.3Scheduling availability of UE performing beam failure detection on FR2835

8.5B.8Scheduling availability of UE during candidate beam detection for Redcap835

8.5B.8.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1835

8.5B.8.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1836

8.5B.8.3Scheduling availability of UE performing L1-RSRP measurement on FR2836

8.5B.9Minimum requirement at transitions for beam failure detection for Redcap836

8.5CLink Recovery Procedures for Satellite Access836

8.5C.1Introduction836

8.5C.2Requirements for SSB based beam failure detection837

8.5C.2.1Introduction837

8.5C.2.2Minimum requirement838

8.5C.2.3Measurement restriction for SSB based beam failure detection838

8.5C.3Requirements for CSI-RS based beam failure detection839

8.5C.3.1Introduction839

8.5C.3.2Minimum requirement839

8.5C.3.3Measurement restrictions for CSI-RS beam failure detection840

8.5C.4Minimum requirement for L1 indication841

8.5C.5Requirements for SSB based candidate beam detection841

8.5C.5.1Introduction841

8.5C.5.2Minimum requirement841

8.5C.5.3Measurement restriction for SSB based candidate beam detection842

8.5C.6Requirements for CSI-RS based candidate beam detection842

8.5C.6.1Introduction842

8.5C.6.2Minimum requirement842

8.5C.6.3Measurement restriction for CSI-RS based candidate beam detection843

8.5C.7Scheduling availability of UE during beam failure detection844

8.5C.7.1Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1-NTN844

8.5C.7.2Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1-NTN844

8.5C.8Scheduling availability of UE during candidate beam detection844

8.5C.8.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1-NTN844

8.5C.8.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1-NTN844

8.5C.9Minimum requirement at transitions for beam failure detection845

8.5DLink Recovery Procedures for ATG845

8.5D.1Introduction845

8.5D.2Requirements for SSB based beam failure detection846

8.5D.2.1Introduction846

8.5D.2.2Minimum requirement846

8.5D.2.3Measurement restriction for SSB based beam failure detection847

8.5D.3Requirements for CSI-RS based beam failure detection848

8.5D.3.1Introduction848

8.5D.3.2Minimum requirement848

8.5D.3.3Measurement restrictions for CSI-RS beam failure detection849

8.5D.4Minimum requirement for L1 indication850

8.5D.5Requirements for SSB based candidate beam detection850

8.5D.5.1Introduction850

8.5D.5.2Minimum requirement850

8.5D.5.3Measurement restriction for SSB based candidate beam detection851

8.5D.6Requirements for CSI-RS based candidate beam detection852

8.5D.6.1Introduction852

8.5D.6.2Minimum requirement852

8.5D.6.3Measurement restriction for CSI-RS based candidate beam detection853

8.5D.7Scheduling availability of UE during beam failure detection854

8.5D.7.1Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1854

8.5D.7.2Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1854

8.5D.8Scheduling availability of UE during candidate beam detection854

8.5D.8.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1854

8.5D.8.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1854

8.5D.9Minimum requirement at transitions for beam failure detection855

8.5D.10Requirements for Beam Failure Recovery in SCell855

8.5ELink Recovery Procedures for RedCap UE with Satellite Access855

8.5E.1Introduction855

8.5E.2Requirements for SSB based beam failure detection for RedCap UE with satellite access855

8.5E.2.1Introduction855

8.5E.2.2Minimum requirement856

8.5E.2.3Measurement restrictions for SSB beam failure detection856

8.5E.3Requirements for CSI-RS based beam failure detection for RedCap UE with satellite access856

8.5E.3.1Introduction856

8.5E.3.2Minimum requirement857

8.5E.3.3Measurement restrictions for CSI-RS beam failure detection857

8.5E.4Minimum requirement for L1 indication for RedCap UE with satellite access857

8.5E.5Requirements for SSB based candidate beam detection for RedCap UE with satellite access858

8.5E.6Requirements for CSI-RS based candidate beam detection for RedCap UE with satellite access858

8.5E.7Scheduling availability of UE during beam failure detection for RedCap UE with satellite access858

8.5E.8Scheduling availability of UE during candidate beam detection for RedCap UE with satellite access858

8.5E.9Minimum requirement at transitions for beam failure detection for RedCap UE with satellite access858

8.6Active BWP switch delay858

8.6.1Introduction858

8.6.2DCI and timer based BWP switch delay on a single CC859

8.6.2ADCI based BWP switch delay on multiple CCs860

8.6.2A.1Simultaneous DCI based BWP switch delay on multiple CCs860

8.6.2A.2Non-simultaneous DCI based BWP switch delay on multiple CCs862

8.6.2BTimer based BWP switch delay on multiple CCs862

8.6.2B.1Simultaneous timer based BWP switch delay on multiple CCs862

8.6.2B.2Non-simultaneous timer based BWP switch delay on multiple CCs863

8.6.3RRC based BWP switch delay on a single CC863

8.6.3ARRC based BWP switch delay on multiple CCs864

8.6.3A.1Simultaneous RRC based BWP switch delay on multiple CCs864

8.6.3A.2Non-simultaneous RRC based BWP switch delay on multiple CCs864

8.6.4BWP switch delay on Consistent UL CCA recovery865

8.6AActive BWP switch delay for RedCap865

8.6A.1Introduction865

8.6A.2DCI and timer based BWP switch delay on a single CC865

8.6A.3RRC based BWP switch delay on a single CC867

8.6CActive BWP switch delay for satellite access867

8.6C.1Introduction867

8.6C.2DCI and timer based BWP switch delay on a single CC867

8.6C.3RRC based BWP switch delay on a single CC869

8.6DActive BWP switch delay for ATG869

8.6D.1Introduction869

8.6D.2DCI and timer based BWP switch delay on a single CC869

8.6D.2ADCI based BWP switch delay on multiple CCs871

8.6D.2A.1Simultaneous DCI based BWP switch delay on multiple CCs871

8.6D.2BTimer based BWP switch delay on multiple CCs872

8.6D.2B.1Simultaneous timer based BWP switch delay on multiple CCs872

8.6D.2B.2Non-simultaneous timer based BWP switch delay on multiple CCs873

8.6D.3RRC based BWP switch delay on a single CC874

8.6D.3ARRC based BWP switch delay on multiple CCs874

8.6D.3A.1Simultaneous RRC based BWP switch delay on multiple CCs874

8.6EActive BWP switch delay for RedCap UE with satellite access875

8.6E.1Introduction875

8.6E.2DCI and timer based BWP switch delay on a single CC875

8.6E.3RRC based BWP switch delay on a single CC875

8.7Void875

8.8NE-DC: E-UTRAN PSCell Addition and Release Delay875

8.8.1Introduction875

8.8.2E-UTRAN PSCell Addition Delay Requirement875

8.8.3E-UTRAN PSCell Release Delay Requirement876

8.9NR-DC: PSCell Addition and Release Delay876

8.9.1Introduction876

8.9.2PSCell Addition Delay Requirement876

8.9.3PSCell Release Delay Requirement877

8.9AConditional PSCell Addition Delay877

8.9A.1Introduction877

8.9A.2Conditional PSCell Addition Delay Requirement877

8.9A.2.1Measurement time878

8.9BNR-DC: PSCell Addition and Release Delay in Carriers with CCA878

8.9B.1Introduction878

8.9B.2PSCell Addition Delay Requirement878

8.9B.3PSCell Release Delay Requirement879

8.9CSubsequent Conditional PSCell Addition Delay880

8.9C.1Introduction880

8.9C.2Subsequent Conditional PSCell Addition Delay Requirement880

8.9C.2.1Measurement time880

8.10Active TCI state switching delay881

8.10.1Introduction881

8.10.2Known conditions for TCI state881

8.10.2AKnown conditions for TCI state with beam prediction881

8.10.3AMAC-CE based TCI state switch delay in HST FR2 scenarios883

8.10.4DCI based TCI state switch delay883

8.10.5RRC based TCI state switch delay883

8.10.6Active TCI state list update delay884

8.10AActive TCI state switching delay with CCA884

8.10A.1Introduction884

8.10A.2Known conditions for TCI state884

8.10A.3MAC-CE based TCI state switch delay885

8.10A.4DCI based TCI state switch delay886

8.10A.5RRC based TCI state switch delay886

8.10A.6Active TCI state list update delay887

8.10BActive TCI state switching delay for RedCap887

8.10B.1Introduction887

8.10B.2Known conditions for TCI state887

8.10B.3MAC-CE based TCI state switch delay887

8.10B.4DCI based TCI state switch delay888

8.10B.5RRC based TCI state switch delay889

8.10B.6Active TCI state list update delay889

8.10CActive TCI state switching delay for satellite access889

8.10C.1Introduction889

8.10C.2MAC-CE based TCI state switch delay890

8.10C.4DCI based TCI state switch delay890

8.10C.5RRC based TCI state switch delay890

8.10C.6Active TCI state list update delay890

8.10DActive TCI state switching delay for ATG890

8.10D.2Void891

8.10D.6Active TCI state list update delay891

8.10EActive TCI state switching delay for UE operating in FR2-1 and configured with groupBasedBeamReporting-r17892

8.10E.1Introduction892

8.10E.2Known conditions for TCI state892

8.10E.3MAC-CE based dual DL TCI state switch delay892

8.10E.3.1MAC-CE based dual DL TCI state switching delay for sDCI892

8.10E.3.2MAC-CE based dual DL TCI state switching delay for mDCI893

8.10E.4DCI based dual DL TCI state switch delay for sDCI and mDCI893

8.10E.4.1DCI based dual DL TCI state switching delay for sDCI893

8.10E.4.2DCI based dual DL TCI state switching delay for mDCI893

8.10E.5RRC based dual DL TCI state switch delay894

8.10E.6Active DL TCI state list update delay894

8.10E.6.1Active DL TCI state list update delay for sDCI894

8.10E.6.2Active DL TCI state list update delay for mDCI894

8.10FActive TCI state switching delay for RedCap UE with satellite access894

8.10F.1Introduction894

8.10F.2MAC-CE based TCI state switch delay894

8.10F.4DCI based TCI state switch delay894

8.10F.5RRC based TCI state switch delay894

8.10F.6Active TCI state list update delay894

8.11PSCell Change894

8.11APSCell Change in Carriers with CCA895

8.11BConditional PSCell Change895

8.11B.1Introduction895

8.11B.2Conditional PSCell Change delay895

8.11B.2.1Measurement time896

8.11DConditional PSCell Change in Carriers with CCA897

8.11D.1Introduction897

8.11D.2Conditional PSCell Change delay897

8.11D.2.1Measurement time898

8.11ESubsequent Conditional PSCell Change898

8.11E.1Introduction898

8.11E.2Subsequent Conditional PSCell Change delay898

8.11E.2.1Measurement time899

8.12Uplink spatial relation switch delay899

8.12.1Introduction899

8.12.2Known conditions for spatial relation when associated with DL-RS899

8.12.3MAC-CE based spatial relation switch delay900

8.12.4DCI based spatial relation switch delay900

8.12.5RRC based spatial relation switch delay901

8.12AUplink spatial relation switch delay for RedCap901

8.12A.1Introduction901

8.12A.2Known conditions for spatial relation when associated with DL-RS901

8.12A.3MAC-CE based spatial relation switch delay902

8.12A.4DCI based spatial relation switch delay902

8.12A.5RRC based spatial relation switch delay903

8.12CUplink spatial relation switch delay for satellite access903

8.12C.1Void903

8.12C.2Void903

8.12C.3Void903

8.12C.4Void903

8.12C.5Void903

8.13UE-specific CBW change903

8.13.1Introduction903

8.13.2UE-specific CBW change delay904

8.13AUE-specific CBW change for RedCap904

8.13A.1Introduction904

8.13A.2UE-specific CBW change delay904

8.13CUE-specific CBW change for satellite access904

8.13C.1Introduction904

8.13C.2UE-specific CBW change delay905

8.13DUE-specific CBW change for ATG905

8.13D.1Introduction905

8.13D.2UE-specific CBW change delay905

8.13EUE-specific CBW change for RedCap UE with satellite access905

8.13E.1Introduction905

8.13E.2UE-specific CBW change delay905

8.14Pathloss reference signal switching delay905

8.14.1Introduction905

8.14.2Known conditions for pathloss reference signal906

8.14.3MAC-CE based pathloss reference signal switch delay906

8.14CPathloss reference signal switching delay for satellite access907

8.14C.1Introduction907

8.14C.2Known conditions for pathloss reference signal907

8.14C.3MAC-CE based pathloss reference signal switch delay908

8.14DPathloss reference signal switching delay for ATG908

8.14D.1Introduction908

8.14D.2Known conditions for pathloss reference signal908

8.14D.3MAC-CE based pathloss reference signal switch delay908

8.14EPathloss reference signal switching delay for RedCap UE with satellite access908

8.14E.1Introduction908

8.14E.2Known conditions for pathloss reference signal909

8.14E.3MAC-CE based pathloss reference signal switch delay909

8.15Active downlink TCI state switching delay for unified TCI909

8.15.1Introduction909

8.15.4DCI based downlink TCI state switch delay911

8.15.5Active Downlink TCI state list update delay911

8.15DActive downlink TCI state switching delay for unified TCI for ATG912

8.15D.1Introduction912

8.15D.2Void912

8.15D.4DCI based downlink TCI state switch delay912

8.15D.5Active Downlink TCI state list update delay913

8.16Active uplink TCI state switching delay for unified TCI913

8.16.1Introduction913

8.16.3MAC-CE based uplink TCI state switch delay914

8.16.4DCI based uplink TCI state switch delay916

8.16.5Active Uplink TCI state list update delay916

8.16DActive uplink TCI state switching delay for unified TCI for ATG918

8.16D.1Introduction918

8.16D.2Void918

8.16D.3MAC-CE based uplink TCI state switch delay918

8.16D.4DCI based uplink TCI state switch delay919

8.16D.5Active Uplink TCI state list update delay919

8.17SCG Activation and Deactivation Delay919

8.17.1Introduction919

8.17.2SCG Activation Delay Requirement920

8.17.3SCG Deactivation Delay Requirement921

8.18TRP specific Link Recovery Procedures921

8.18.1Introduction921

8.18.2Requirements for TRP specific SSB based beam failure detection922

8.18.2.1Introduction922

8.18.2.2Minimum requirement922

8.18.2.3Measurement restriction for SSB based beam failure detection924

8.18.3Requirements for CSI-RS based beam failure detection925

8.18.3.1Introduction925

8.18.3.2Minimum requirement925

8.18.3.3Measurement restrictions for CSI-RS beam failure detection929

8.18.4Minimum requirement for L1 indication930

8.18.5Requirements for SSB based candidate beam detection930

8.18.5.1Introduction930

8.18.5.2Minimum requirement930

8.18.5.3Measurement restriction for SSB based candidate beam detection933

8.18.6Requirements for CSI-RS based candidate beam detection934

8.18.6.1Introduction934

8.18.6.2Minimum requirement934

8.18.6.3Measurement restriction for CSI-RS based candidate beam detection936

8.18.7Requirements for TRP specific Beam Failure Recovery937

8.18.7.1Introduction937

8.18.7.2Requirement938

8.18.8Scheduling availability of UE during TRP specific beam failure detection938

8.18.8.1Scheduling availability of UE performing TRP specific beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1938

8.18.8.2Scheduling availability of UE performing TRP specific beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1938

8.18.8.3Scheduling availability of UE performing TRP specific beam failure detection on FR2938

8.18.8.4Scheduling availability of UE performing TRP specific beam failure detection on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC939

8.18.9Scheduling availability of UE during TRP specific candidate beam detection939

8.18.9.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1939

8.18.9.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1940

8.18.9.3Scheduling availability of UE performing L1-RSRP measurement on FR2940

8.18.9.4Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC940

8.19Pre-configured measurement gap activation/deactivation delay941

8.19.1Introduction941

8.19.2Pre-configured measurement gap activation/deactivation upon DCI/timer-based BWP switch941

8.19.2.1Activation/deactivation upon DCI/timer-based BWP switch delay on a single CC941

8.19.3Pre-configured measurement gap activation/deactivation upon SCell activation/deactivation941

8.19.4Pre-configured measurement gap activation/deactivation upon RRC reconfiguration941

8.19.5Activation/deactivation delay requirements for concurrent measurement gaps with Pre-MG941

8.19.5.1Activation/deactivation delay requirements for non-overlapped activation/deactivation of concurrent measurement gaps with Pre- MG942

8.19.5.2Activation/deactivation delay requirements for fully overlapped activation/deactivation of concurrent measurement gaps with Pre- MG942

8.19.5.3Pre-MG activation/deactivation delay when colliding with a concurrent measurement gap942

8.19DPre-configured measurement gap activation/deactivation delay for ATG942

8.19D.1Introduction942

8.19D.2Pre-configured measurement gap activation/deactivation upon DCI/timer-based BWP switch942

8.19D.2.1Activation/deactivation upon DCI/timer-based BWP switch delay on a single CC942

8.19D.3Pre-configured measurement gap activation/deactivation upon RRC reconfiguration943

8.19D.4Pre-configured measurement gap activation/deactivation upon SCell activation/deactivation943

8.20LTM PSCell Cell Switch943

8.20.1Introduction943

8.20.2LTM Cell Switch delay944

8.20.3Void944

8.21Active downlink TCI state switching delay for unified TCI for single-DCI mTRP944

8.21.1Introduction944

8.21.2Known conditions for downlink TCI state945

8.21.3MAC-CE based downlink TCI state switch delay945

8.21.4DCI based downlink TCI state switch delay946

8.21.5Active Downlink TCI state list update delay946

8.22Active downlink TCI state switching delay for unified TCI for multi-DCI mTRP947

8.22.1Introduction947

8.22.2Known conditions for downlink TCI state948

8.22.3MAC-CE based downlink TCI state switch delay948

8.22.4DCI based downlink TCI state switch delay949

8.22.5Active Downlink TCI state list update delay949

8.23Active uplink TCI state switching delay for unified TCI for single-DCI mTRP950

8.23.1Introduction950

8.23.2Known conditions for uplink TCI state950

8.23.3MAC-CE based uplink TCI state switch delay951

8.23.4DCI based uplink TCI state switch delay952

8.23.5Active uplink TCI state list update delay952

8.24Active uplink TCI state switching delay for unified TCI for multi-DCI mTRP953

8.24.1Introduction953

8.24.2Known conditions for uplink TCI state954

8.24.3MAC-CE based uplink TCI state switch delay954

8.24.4DCI based uplink TCI state switch delay955

8.24.5Active Uplink TCI state list update delay955

8.25TCI state activation for LTM candidate cell956

8.25.1Introduction956

8.25.2Known TCI state conditions957

8.25.3SSB based TCI state activation delay957

9Measurement Procedure958

9.1General measurement requirement958

9.1.1Introduction958

9.1.2Measurement gap958

9.1.2.1EN-DC: Measurement Gap Sharing968

9.1.2.1aSA: Measurement Gap Sharing968

9.1.2.1bNE-DC: Measurement Gap Sharing969

9.1.2.1cNR-DC: Measurement Gap Sharing970

9.1.3UE Measurement capability971

9.1.3.1EN-DC: Monitoring of multiple layers using gaps971

9.1.3.1aSA: Monitoring of multiple layers using gaps972

9.1.3.1bNE-DC: Monitoring of multiple layers using gaps972

9.1.3.1cNR-DC: Monitoring of multiple layers using gaps973

9.1.3.2EN-DC: Maximum allowed layers for multiple monitoring973

9.1.3.2aSA: Maximum allowed layers for multiple monitoring974

9.1.3.2bNE-DC: Maximum allowed layers for multiple monitoring975

9.1.3.2cNR-DC: Maximum allowed layers for multiple monitoring975

9.1A.3.2Void976

9.1.3AUE Measurement capability under operation mode with CCA976

9.1.3A.1EN-DC: Monitoring of multiple layers using gaps under CCA976

9.1.3A.1aSA: Monitoring of multiple layers using gaps under CCA976

9.1.3A.2EN-DC: Maximum allowed layers for multiple monitoring under CCA976

9.1.3A.2aSA: Maximum allowed layers for multiple monitoring under CCA977

9.1.3CUE Measurement capability under operation mode with satellite access977

9.1.3C.1aSA: Monitoring of multiple layers using gaps under satellite access977

9.1.3C.2aSA: Maximum allowed layers for multiple monitoring for SAN978

9.1.4Capabilities for Support of Event Triggering and Reporting Criteria978

9.1.4.1Introduction978

9.1.4.2Requirements978

9.1.5Carrier-specific scaling factor981

9.1.5.1Monitoring of multiple layers outside gaps981

9.1.5.1.1EN-DC mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3 measurements and RSSI and channel occupancy measurements performed outside gaps984

9.1.5.1.2SA mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3 measurements and RSSI and channel occupancy measurements performed outside gaps988

9.1.5.1.3NR-DC mode: carrier-specific scaling factor for SSB-based and CSI-RS based L3 measurements performed outside gaps991

9.1.5.1.4NE-DC mode: carrier-specific scaling factor for SSB-based and CSI-RS based measurements performed outside gaps992

9.1.5.2Monitoring of multiple layers within gaps994

9.1.5.2.1EN-DC mode: carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements and RSSI and channel occupancy measurements performed within gaps996

9.1.5.2.2SA mode: carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements and RSSI and channel occupancy measurements performed within gaps998

9.1.5.2.3NE-DC: carrier-specific scaling factor for SSB-based and CSI-RS based L3 measurements performed within gaps1000

9.1.5.2.4NR-DC: carrier-specific scaling factor for SSB-based and CSI-RS-based L3 measurements performed within gaps1002

9.1.5.2.5SA mode: carrier-specific scaling factor for PRS-based measurements performed within gaps1004

9.1.5.2.6NE-DC: carrier-specific scaling factor for PRS-based measurements performed within gaps1004

9.1.5.2.7NR-DC: carrier-specific scaling factor for PRS-based measurements performed within gaps1004

9.1.5.3Monitoring of multiple layers within NCSG1005

9.1.5.3.1SA mode: carrier-specific scaling factor for measurements performed within NCSG1006

9.1.5.4L1-RSRP measurements within measurement gap1007

9.1.5.4.1SA mode: carrier-specific scaling factor for L1-RSRP measurements performed within measurement gap1008

9.1.5.4.2NR-DC: carrier-specific scaling factor for L1-RSRP measurements performed within measurement gap1009

9.1.6Minimum requirement at transitions1011

9.1.7Pre-configured measurement gap1011

9.1.7.1Introduction1011

9.1.7.2Requirements applicability1012

9.1.7.3Requirements1012

9.1.7.3.1Requirements for autonomous activation/deactivation mechanism1012

9.1.7.3.2Requirements for network-controlled activation/deactivation mechanism1013

9.1.7.3.3Requirements for reception/transmission during activation/deactivation1014

9.1.8Concurrent measurement gaps1014

9.1.8.1Introduction1014

9.1.8.2Requirements1014

9.1.8.3Collision between concurrent measurement gaps1015

9.1.8.4Measurement gap related requirements of concurrent measurement gaps1015

9.1.9Network controlled small gap1016

9.1.9.1Introduction1016

9.1.9.2Requirements applicability1017

9.1.10MUSIM gaps1019

9.1.10.1Introduction1020

9.1.10.2Priorities for MUSIM gaps1021

9.1.10.3Keep solution for MUSIM gaps1021

9.1.10.4Collisions between different MUSIM gaps1021

9.1.10.5Collisions between MUSIM gaps and measurement gaps1021

9.1.10.6MUSIM gap related requirements1022

9.1.11UL gap for Tx power management1022

9.1.12Concurrent measurement gaps with Pre-MG1022

9.1.12.1Introduction1022

9.1.12.2Requirements1023

9.1.12.3Collisions involving Pre-MG(s)1023

9.1.12.4Collision between Pre-MG activation/deactivation and measurement gap1024

9.1.12.5Pre-MG related requirements1024

9.1.13Concurrent measurement gaps with NCSG1024

9.1.13.1Introduction1024

9.1.13.2Requirements1025

9.1.13.3Collision involving NCSGs1026

9.1.14Measurement gap occasion cancellation1026

9.1.14.1Introduction1026

9.1.14.2Applicable measurement gap configurations1026

9.1.14.3Applicability1027

9.1.14.4Requirements for cancelling measurement gap occasions1027

9.1AGeneral measurement requirement for RedCap1027

9.1A.1Introduction1027

9.1A.2Measurement gap1027

9.1A.2.1SA: Measurement Gap Sharing1031

9.1A.3UE Measurement capability1032

9.1A.3.1SA: Monitoring of multiple layers using gaps1032

9.1A.3.2SA: Maximum allowed layers for multiple monitoring1032

9.1A.4Capabilities for Support of Event Triggering and Reporting Criteria1032

9.1A.4.1Introduction1032

9.1A.4.2Requirements1033

9.1A.5Carrier-specific scaling factor1033

9.1A.5.1Monitoring of multiple layers outside gaps1033

9.1A.5.1.1SA mode: carrier-specific scaling factor for SSB-based measurements performed outside gaps1034

9.1A.5.2Monitoring of multiple layers within gaps1034

9.1A.5.2.1SA mode: carrier-specific scaling factor for SSB measurements performed within gaps1034

9.1A.6Minimum requirement at transitions1036

9.1CGeneral measurement requirement for SAN1036

9.1C.1Introduction1036

9.1C.2Measurement gap1037

9.1C.8Concurrent measurement gaps for SAN1039

9.1C.8.1Introduction1039

9.1C.8.2Requirements1039

9.1C.8.3Collision between concurrent measurement gaps1040

9.1C.8.4Measurement gap related requirements of concurrent measurement gaps1040

9.1C.9Collision between SMTC and measurement gap for SAN1040

9.1C.9.1Introduction1040

9.1C.9.2Collision between SMTCs and measurement gap1040

9.1C.9.3Collision between multiple SMTCs on a SAN carrier1041

9.1DGeneral measurement requirement for ATG1041

9.1D.1Introduction1041

9.1D.2Measurement gap1041

9.1D.2.1aSA: Measurement Gap Sharing1044

9.1D.3UE Measurement capability1044

9.1D.3.1SA: Monitoring of multiple layers using gaps1044

9.1D.3.2SA: Maximum allowed layers for multiple monitoring1044

9.1D.4Void1045

9.1D.5Carrier-specific scaling factor1045

9.1D.5.1Monitoring of multiple layers outside gaps1045

9.1D.5.1.1Void1045

9.1D.5.1.2SA mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3 measurements performed outside gaps1045

9.1D.5.2Monitoring of multiple layers within gaps1046

9.1D.5.2.1Void1047

9.1D.5.2.2SA mode: carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements performed within gaps1047

9.1D.6Void1047

9.1D.7Pre-configured measurement gap1047

9.1D.7.1Introduction1047

9.1D.7.2Requirements applicability1048

9.1D.7.3Requirements1048

9.1D.7.3.1Requirements for autonomous activation/deactivation mechanism1048

9.1D.7.3.2Requirements for network-controlled activation/deactivation mechanism1049

9.1D.7.3.3Requirements for reception/transmission during activation/deactivation1049

9.1D.8Capabilities for Support of Event Triggering and Reporting Criteria1049

9.1D.8.1Introduction1049

9.1D.8.2Requirements1050

9.1D.9Minimum requirement at transitions1050

9.1EGeneral measurement requirement for RedCap with satellite access1050

9.1E.1Introduction1050

9.1E.2Measurement gap1051

9.1E.8Concurrent measurement gaps for RedCap with SAN1051

9.1E.8.1Introduction1051

9.1E.8.2Requirements1051

9.1E.8.3Collision between concurrent measurement gaps1051

9.1E.8.4Measurement gap related requirements of concurrent measurement gaps1051

9.1E.9Collision between SMTC and measurement gap for RedCap with satellite access1051

9.1E.9.1Introduction1051

9.1E.9.2Collision between SMTCs and measurement gap1051

9.1E.9.3Collision between multiple SMTCs on a SAN carrier1052

9.2NR intra-frequency measurements1052

9.2.1Introduction1052

9.2.2Requirements applicability1055

9.2.3Number of cells and number of SSB1056

9.2.3.1Requirements for FR11056

9.2.3.2Requirements for FR21056

9.2.4Measurement Reporting Requirements1057

9.2.4.1Periodic Reporting1057

9.2.4.2Event-triggered Periodic Reporting1057

9.2.4.3Event Triggered Reporting1057

9.2.4.4SCell activation Triggered Reporting1058

9.2.5Intrafrequency measurements without measurement gaps1058

9.2.5.1Intra-frequency cell identification1058

9.2.5.2Measurement period1066

9.2.5.3Scheduling availability of UE during intra-frequency measurements1070

9.2.5.3.1Scheduling availability of UE performing measurements in TDD bands on FR11070

9.2.5.3.2Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR11071

9.2.5.3.3Scheduling availability of UE performing measurements on FR21072

9.2.5.3.4Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA1074

9.2.5.4SFTD Measurements between PCell and PSCell1074

9.2.5.4.1Introduction1074

9.2.5.4.2SFTD Measurement delay1074

9.2.5.4.3SFTD Measurement Reporting Delay1075

9.2.6Intra-frequency measurements with measurement gaps1075

9.2.6.1Void1075

9.2.6.2Intra-frequency cell identification1075

9.2.6.3Intra-frequency Measurement Period1081

9.2.7Intra-frequency measurements with NCSG1084

9.2.7.1Intra-frequency cell identification1084

9.2.7.2Measurement period1086

9.2.7.3Scheduling availability during intra-frequency measurement with NCSG1087

9.2ANR intra-frequency measurements with CCA1087

9.2A.1Introduction1087

9.2A.2Requirements applicability1088

9.2A.3Number of cells and number of SSB1088

9.2A.3.1Requirements for FR11088

9.2A.3.2Requirements for FR2-21088

9.2A.4Measurement Reporting Requirements1089

9.2A.5Intra-frequency measurements without measurement gaps1089

9.2A.5.2Measurement period1094

9.2A.5.3Scheduling availability of UE during intra-frequency measurements1096

9.2A.5.3.1Scheduling availability of UE performing measurements in TDD bands on FR11096

9.2A.5.3.2Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR11097

9.2A.5.3.3Scheduling availability of UE performing measurements in TDD bands on FR2-21097

9.2A.6Intra-frequency measurements with measurement gaps1097

9.2A.6.1Intra-frequency cell identification1097

9.2A.6.2Intra-frequency Measurement Period1099

9.2A.7Intra-frequency RSSI and Channel occupancy measurements1100

9.2A.7.1Intra-frequency RSSI measurements1100

9.2A.7.2Intra-frequency Channel occupancy measurements1102

9.2A.7.3Scheduling restriction during RSSI and Channel Occupancy measurements in FR11104

9.2A.7.4Scheduling restriction during RSSI measurements in FR2-21104

9.2BNR intra-frequency measurements for RedCap1104

9.2B.1Introduction1104

9.2B.2Requirements applicability1105

9.2B.3Number of cells and number of SSB1105

9.2B.3.1Requirements for FR11105

9.2B.3.2Requirements for FR21105

9.2B.4Measurement Reporting Requirements1106

9.2B.4.1Periodic Reporting1106

9.2B.4.2Event-triggered Periodic Reporting1106

9.2B.4.3Event Triggered Reporting1106

9.2B.5Intra-frequency measurements without measurement gaps1107

9.2B.5.1Intra-frequency cell identification1107

9.2B.5.2Measurement period1109

9.2B.5.3Scheduling availability of UE during intra-frequency measurements1110

9.2B.5.3.1Scheduling availability of UE performing measurements in TDD bands on FR11110

9.2B.5.3.2Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR11110

9.2B.5.3.3Scheduling availability of UE performing measurements on FR21111

9.2B.5.3.4Scheduling availability of HD-FDD UE performing measurements on FR11111

9.2B.6Intra-frequency measurements with measurement gaps1112

9.2B.6.1Intra-frequency cell identification1112

9.2B.6.2Intra-frequency Measurement Period1113

9.2CNR intra-frequency measurements for SAN1114

9.2C.1Introduction1114

9.2C.2Requirements applicability1115

9.2C.3Number of cells and number of SSB1115

9.2C.3.1Requirements for FR1-NTN1115

9.2C.4Measurement Reporting Requirements1116

9.2C.4.1Periodic Reporting1116

9.2C.4.2Event-triggered Periodic Reporting1116

9.2C.4.3Event Triggered Reporting1116

9.2C.5Intra-frequency measurements without measurement gaps1116

9.2C.5.1Intra-frequency cell identification1116

9.2C.5.2Measurement period1119

9.2C.5.3Scheduling availability of UE during intra-frequency measurements1119

9.2C.5.3.1Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1-NTN1119

9.2C.5.3.2Scheduling availability of UE performing measurements on a neighbor cell served by a different satellite in LEO1119

9.2C.6Intra-frequency measurements with measurement gaps1120

9.2C.6.1Void1120

9.2C.6.2Intra-frequency cell identification1120

9.2C.6.3Intrafrequency Measurement Period1121

9.2C.7Intra-frequency measurements without measurement gaps for NTN band above 10 GHz1122

9.2C.7.1Intra-frequency cell identification1122

9.2C.7.2Measurement period1123

9.2C.7.3Scheduling availability of UE during intra-frequency measurements1124

9.2C.7.3.1Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on NTN bands above 10 GHz1124

9.2C.8Intra-frequency measurements with measurement gaps for NTN band above 10 GHz1124

9.2C.8.1Intra-frequency cell identification1124

9.2C.8.3Intra-frequency Measurement Period1125

9.2DNR intra-frequency measurements for ATG1125

9.2D.1Introduction1125

9.2D.2Requirements applicability1126

9.2D.3Number of cells and number of SSB1126

9.2D.3.1Requirements for FR11126

9.2D.4Measurement Reporting Requirements1127

9.2D.4.1Periodic Reporting1127

9.2D.4.2Event-triggered Periodic Reporting1127

9.2D.4.3Event Triggered Reporting1127

9.2D.4.4SCell activation Triggered Reporting1127

9.2D.5Intra-frequency measurements without measurement gaps1128

9.2D.5.1Intra-frequency cell identification1128

9.2D.5.2Measurement period1131

9.2D.5.3Scheduling availability of UE during intra-frequency measurements1132

9.2D.5.3.1Scheduling availability of UE performing measurements on FR11132

9.2D.5.3.2Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR11134

9.2D.6Intra-frequency measurements with measurement gaps1134

9.2D.6.1Void1134

9.2D.6.2Intra-frequency cell identification1134

9.2D.6.3Intra-frequency Measurement Period1135

9.2ENR intra-frequency measurements for RedCap with SAN1136

9.2E.1Introduction1136

9.2E.2Requirements applicability1136

9.2E.3Number of cells and number of SSB1137

9.2E.3.1Requirements for FR11137

9.2E.4Measurement Reporting Requirements1137

9.2E.4.1Periodic Reporting1137

9.2E.4.2Event-triggered Periodic Reporting1137

9.2E.4.3Event Triggered Reporting1137

9.2E.5Intra-frequency measurements without measurement gaps1137

9.2E.5.1Intra-frequency cell identification1137

9.2E.5.2Measurement period1138

9.2E.5.3Scheduling availability of UE during intra-frequency measurements1138

9.2E.5.3.1Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR11138

9.2E.5.3.2Scheduling availability of UE performing measurements on a neighbor cell served by a different satellite in LEO1138

9.2E.5.3.4Scheduling availability of UE performing measurements in HD-FDD bands on FR11138

9.2E.6Intra-frequency measurements with measurement gaps1138

9.2E.6.1Intra-frequency cell identification1138

9.2E.6.2Intra-frequency Measurement Period1139

9.3NR inter-frequency measurements1139

9.3.1Introduction1139

9.3.2Requirements applicability1142

9.3.2.1Void1143

9.3.2.2Void1143

9.3.3Number of cells and number of SSB1143

9.3.3.1Requirements for FR11143

9.3.3.2Requirements for FR21143

9.3.4Inter-frequency measurement with measurement gaps1143

9.3.4.1Void1149

9.3.4.2Void1149

9.3.5Inter-frequency measurements1149

9.3.5.1Void1152

9.3.5.2Void1152

9.3.5.3Void1152

9.3.6Inter-frequency measurements reporting requirements1152

9.3.6.1Periodic Reporting1152

9.3.6.2Event-triggered Periodic Reporting1152

9.3.6.3Event-triggered Reporting1152

9.3.7Void1153

9.3.8Inter-frequency SFTD measurement requirements1153

9.3.8.1Introduction1153

9.3.8.2SFTD Measurement delay1153

9.3.8.3SFTD Measurement reporting delay1154

9.3.9Inter-frequency measurements without measurement gaps1154

9.3.9.1Inter-frequency Cell identification1154

9.3.9.2Measurement period1159

9.3.9.3Scheduling availability of UE during inter-frequency measurements when the SSB is completely contained in the active BWP of the UE1161

9.3.9.3.1Scheduling availability of UE performing measurements in TDD bands on FR11162

9.3.9.3.2Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR11163

9.3.9.3.3Scheduling availability of UE performing measurements on FR21164

9.3.9.3.4Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA1164

9.3.9.4Scheduling availability of UE during inter-frequency measurements when the SSB is not completely contained in the active BWP of the UE1164

9.3.9.4.1Scheduling availability of UE performing measurements in TDD bands on FR11165

9.3.9.4.2Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR11165

9.3.9.4.3Scheduling availability of UE performing measurements on FR21166

9.3.9.4.4Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA1167

9.3.10Inter-frequency measurement with NCSG1168

9.3.10.1Inter-frequency cell identification1168

9.3.10.2Measurement period1170

9.3.10.3Scheduling availability during inter-frequency measurement with NCSG1170

9.3.10.3.1Scheduling availability of UE performing measurements in TDD bands on FR11170

9.3.10.3.2Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR11171

9.3.10.3.3Scheduling availability of UE performing measurements on FR21171

9.3.10.3.4Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA1173

9.3ANR inter-frequency measurements in carrier frequencies with CCA1173

9.3A.1Introduction1173

9.3A.2Requirements applicability1174

9.3A.3Number of cells and number of SSB1174

9.3A.3.1Requirements for FR11174

9.3A.3.2Requirements for FR2-21174

9.3A.4Inter-frequency cell identification1175

9.3A.5Inter-frequency measurements1177

9.3A.6Inter-frequency measurements reporting requirements1178

9.3A.6.1Periodic Reporting1178

9.3A.6.2Event-triggered Periodic Reporting1178

9.3A.6.3Event-triggered Reporting1178

9.3A.8Inter-frequency RSSI measurements1179

9.3A.9Inter-frequency channel occupancy measurements1180

9.3BNR inter-frequency measurements for RedCap1180

9.3B.1Introduction1180

9.3B.2Requirements applicability1181

9.3B.3Number of cells and number of SSB1181

9.3B.3.1Requirements for FR11181

9.3B.3.2Requirements for FR21181

9.3B.4Inter-frequency measurement with measurement gaps1181

9.3B.5Inter-frequency measurements1183

9.3B.6Inter-frequency measurements reporting requirements1184

9.3B.6.1Periodic Reporting1184

9.3B.6.2Event-triggered Periodic Reporting1184

9.3B.6.3Event-triggered Reporting1184

9.3B.7Inter-frequency measurements without measurement gaps1184

9.3B.7.1Inter-frequency Cell identification1184

9.3B.7.2Measurement period1186

9.3B.7.3Scheduling availability of UE during inter-frequency measurements1187

9.3B.7.3.1Scheduling availability of UE performing measurements in TDD bands on FR11187

9.3B.7.3.2Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR11188

9.3B.7.3.3Scheduling availability of UE performing measurements on FR21188

9.3B.7.3.4Scheduling availability of HD-FDD UE performing measurements on FR11188

9.3CNR inter-frequency measurements for SAN1189

9.3C.1Introduction1189

9.3C.2Requirements applicability1190

9.3C.3Number of cells and number of SSB1190

9.3C.3.1Requirements for FR1-NTN1190

9.3C.4Inter-frequency measurement with measurement gaps1190

9.3C.5Inter-frequency measurements1192

9.3C.6Inter-frequency measurements reporting requirements1192

9.3C.6.1Periodic Reporting1192

9.3C.6.2Event-triggered Periodic Reporting1193

9.3C.6.3Event-triggered Reporting1193

9.3C.7Inter-frequency measurements without measurement gaps1193

9.3C.7.1Inter-frequency Cell identification1193

9.3C.7.2Measurement period1195

9.3C.7.3Scheduling availability of UE during inter-frequency measurements1195

9.3C.7.3.1Void1196

9.3C.7.3.2Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1-NTN1196

9.3C.7.3.3Scheduling availability of UE performing measurements on a neighbor cell served by a different satellite in LEO1196

9.3C.8Inter-frequency measurement with measurement gaps for NTN band above 10 GHz1196

9.3C.9Inter-frequency measurements for NTN band above 10 GHz1197

9.3C.10Inter-frequency measurements without measurement gaps for NTN band above 10 GHz1197

9.3C.10.1Inter-frequency Cell identification1197

9.3C.10.2Measurement period1199

9.3C.10.3Scheduling availability of UE during inter-frequency measurements1199

9.3C.10.3.1Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on NTN bands above 10 GHz1199

9.3DNR inter-frequency measurements for ATG1199

9.3D.1Introduction1199

9.3D.2Requirements applicability1200

9.3D.3Number of cells and number of SSB1201

9.3D.3.1Requirements for FR11201

9.3D.4Inter-frequency measurement with measurement gaps1201

9.3D.5Inter-frequency measurements1202

9.3D.6Inter-frequency measurements reporting requirements1202

9.3D.6.1Periodic Reporting1202

9.3D.6.2Event-triggered Periodic Reporting1203

9.3D.6.3Event-triggered Reporting1203

9.3D.7Void1203

9.3D.8Void1203

9.3D.9Inter-frequency measurements without measurement gaps1203

9.3D.9.1Inter-frequency Cell identification1203

9.3D.9.2Measurement period1205

9.3D.9.3Scheduling availability of UE during inter-frequency measurements1205

9.3D.9.3.1Scheduling availability of UE performing measurements on FR11206

9.3D.9.3.2Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR11207

9.3ENR inter-frequency measurements for Redcap UEs with satellite access1207

9.3E.1Introduction1207

9.3E.2Requirements applicability1207

9.3E.3Number of cells and number of SSB1208

9.3E.3.1Requirements for FR11208

9.3E.4Inter-frequency measurement with measurement gaps1208

9.3E.5Inter-frequency measurements1209

9.3E.6Inter-frequency measurements reporting requirements1209

9.3E.6.1Periodic Reporting1209

9.3E.6.2Event-triggered Periodic Reporting1210

9.3E.6.3Event-triggered Reporting1210

9.3E.7Inter-frequency measurements without measurement gaps1210

9.3E.7.1Inter-frequency Cell identification1210

9.3E.7.2Measurement period1211

9.3E.7.3Scheduling availability of UE during inter-frequency measurements1211

9.3E.7.3.1Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR11211

9.3E.7.3.2Scheduling availability of UE performing measurements in HD-FDD bands on FR11211

9.4Inter-RAT measurements1212

9.4.1Introduction1212

9.4.2NR − E-UTRAN FDD measurements1214

9.4.2.1Introduction1214

9.4.2.2Requirements when no DRX is used1214

9.4.2.3Requirements when DRX is used1216

9.4.2.4Measurement reporting requirements1218

9.4.2.4.1Periodic Reporting1218

9.4.2.4.2Event-Triggered Periodic Reporting1218

9.4.2.4.3Event-Triggered Reporting1219

9.4.2.5Scheduling Availability During NR − E-UTRAN FDD measurements with NCSG1219

9.4.3NR − E-UTRAN TDD measurements1219

9.4.3.1Introduction1219

9.4.3.2Requirements when no DRX is used1219

9.4.3.3Requirements when DRX is used1222

9.4.3.4Measurement reporting requirements1224

9.4.3.4.1Periodic Reporting1224

9.4.3.4.2Event-Triggered Periodic Reporting1224

9.4.3.4.3Event-Triggered Reporting1225

9.4.3.5Scheduling Availability During NR − E-UTRAN TDD measurements with NCSG1225

9.4.4Inter-RAT RSTD measurements1225

9.4.4.1NR − E-UTRAN FDD RSTD measurements1225

9.4.4.1.1Introduction1225

9.4.4.1.2Requirements1226

9.4.4.2NR − E-UTRAN TDD RSTD measurements1228

9.4.4.2.1Introduction1228

9.4.4.2.2Requirements1229

9.4.5Inter-RAT E-CID measurements1232

9.4.5.1NR−E-UTRAN FDD E-CID RSRP and RSRQ measurements1232

9.4.5.1.1Introduction1232

9.4.5.1.2Requirements1232

9.4.5.1.3Measurement Reporting Delay1232

9.4.5.2NR−E-UTRAN TDD E-CID RSRP and RSRQ measurements1233

9.4.5.2.1Introduction1233

9.4.5.2.2Requirements1233

9.4.5.2.3Measurement Reporting Delay1233

9.4.6NR − UTRAN FDD measurements1233

9.4.6.1Introduction1233

9.4.6.2Requirements when no DRX is used1233

9.4.6.3Requirements when DRX is used1234

9.4.7NR – E-UTRAN measurements with autonomous gaps1236

9.4.7.1CGI identification of an E-UTRA cell with autonomous gaps1236

9.4.7.2CGI reporting delay1236

9.4.8NR – E-UTRAN measurements without measurement gaps1237

9.4.8.1Introduction1237

9.4.8.2General requirements1237

9.4.8.3NR − E-UTRAN FDD measurements1238

9.4.8.3.1Introduction1238

9.4.8.3.2Requirements when no DRX is used1238

9.4.8.3.3Requirements when DRX is used1239

9.4.8.3.4Measurement reporting requirements1240

9.4.8.3.5Scheduling availability during NR − E-UTRAN FDD measurements1240

9.4.8.4NR − E-UTRAN TDD measurements1240

9.4.8.4.1Introduction1240

9.4.8.4.2Requirements when no DRX is used1241

9.4.8.4.3Requirements when DRX is used1242

9.4.8.4.4Measurement reporting requirements1243

9.4.8.4.5Scheduling availability during NR − E-UTRAN TDD measurements1243

9.4AInter-RAT measurements for RedCap1244

9.4A.1Introduction1244

9.4A.2NR − E-UTRAN FDD measurements1245

9.4A.2.1Introduction1245

9.4A.2.2Requirements when no DRX is used1246

9.4A.2.3Requirements when DRX is used1247

9.4A.2.4Measurement reporting requirements1248

9.4A.2.4.1Periodic Reporting1248

9.4A.2.4.2Event-Triggered Periodic Reporting1248

9.4A.2.4.3Event-Triggered Reporting1248

9.4A.3NR − E-UTRAN TDD measurements1248

9.4A.3.1Introduction1248

9.4A.3.2Requirements when no DRX is used1249

9.4A.3.3Requirements when DRX is used1250

9.4A.3.4Measurement reporting requirements1251

9.4A.3.4.1Periodic Reporting1251

9.4A.3.4.2Event-Triggered Periodic Reporting1251

9.4A.3.4.3Event-Triggered Reporting1252

9.4A.4NR – E-UTRAN measurements with autonomous gaps1252

9.4A.4.1CGI identification of an E-UTRA cell with autonomous gaps1252

9.4A.4.2CGI reporting delay1253

9.4A.4.3CGI reporting scheduling restriction1253

9.5L1-RSRP measurements for Reporting1253

9.5.1Introduction1253

9.5.2Requirements applicability1254

9.5.3Measurement Reporting Requirements1255

9.5.3.1Periodic Reporting1255

9.5.3.2Semi-Persistent Reporting1255

9.5.3.3Aperiodic Reporting1256

9.5.3.4Event Triggered Reporting for the UE initiated beam management1256

9.5.4L1-RSRP measurement requirements1257

9.5.4.1SSB based L1-RSRP Reporting1257

9.5.4.2CSI-RS based L1-RSRP Reporting1264

9.5.4AVoid1268

9.5.4A.1Void1268

9.5.5Measurement restriction for CSI-RS and SSB for L1-RSRP measurement1268

9.5.5.1Measurement restriction for SSB based L1-RSRP1269

9.5.5.2Measurement restriction for CSI-RS based L1-RSRP1269

9.5.6Scheduling availability of UE during L1-RSRP measurement1271

9.5.6.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR11271

9.5.6.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR11271

9.5.6.3Scheduling availability of UE performing L1-RSRP measurement on FR21272

9.5.6.4Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA1274

9.5.7Minimum requirement at transitions1274

9.5AL1-RSRP measurements for Reporting under CCA1275

9.5A.1Introduction1275

9.5A.2Requirements applicability1275

9.5A.3Measurement Reporting Requirements1275

9.5A.3.1Periodic Reporting1276

9.5A.3.2Semi-Persistent Reporting1276

9.5A.3.3Aperiodic Reporting1276

9.5A.4L1-RSRP measurement requirements1276

9.5A.4.1SSB based L1-RSRP Reporting1276

9.5A.5Measurement restriction for L1-RSRP measurement1279

9.5A.5.1Measurement restriction for SSB based L1-RSRP1279

9.5A.6Scheduling availability of UE during L1-RSRP measurement1280

9.5A.6.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR11280

9.5A.6.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR11280

9.5A.6.3Void1280

9.5A.6.3AScheduling availability of UE performing L1-RSRP measurement in case of FR1-FR2 inter-band CA1280

9.5A.6.3BScheduling availability of UE performing L1-RSRP measurement on FR2-21280

9.5A.6.4Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA1281

9.5BL1-RSRP measurements for Reporting for RedCap1281

9.5B.1Introduction1281

9.5B.2Requirements applicability1281

9.5B.3Measurement Reporting Requirements1282

9.5B.3.1Periodic Reporting1282

9.5B.3.2Semi-Persistent Reporting1282

9.5B.3.3Aperiodic Reporting1283

9.5B.4L1-RSRP measurement requirements1283

9.5B.4.1SSB based L1-RSRP Reporting1283

9.5B.4.2CSI-RS based L1-RSRP Reporting1285

9.5B.5Measurement restriction for CSI-RS and SSB for L1-RSRP measurement1288

9.5B.5.1Measurement restriction for SSB based L1-RSRP1288

9.5B.5.2Measurement restriction for CSI-RS based L1-RSRP1288

9.5B.6Scheduling availability of UE during L1-RSRP measurement1288

9.5B.6.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR11289

9.5B.6.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR11289

9.5B.6.3Scheduling availability of UE performing L1-RSRP measurement on FR21289

9.5CL1-RSRP measurements for Reporting for satellite access1290

9.5C.1Introduction1290

9.5C.3Measurement Reporting Requirements1290

9.5C.3.1Periodic Reporting1291

9.5C.3.2Semi-Persistent Reporting1291

9.5C.3.3Aperiodic Reporting1291

9.5C.4L1-RSRP measurement requirements1291

9.5C.4.1SSB based L1-RSRP Reporting1291

9.5C.5Measurement restriction for L1-RSRP measurement1293

9.5C.5.1Measurement restriction for SSB based L1-RSRP1293

9.5C.5.2Measurement restriction for CSI-RS based L1-RSRP1293

9.5C.6Scheduling availability of UE during L1-RSRP measurement1294

9.5C.6.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1-NTN1294

9.5C.6.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1-NTN1294

9.5C.7L1-RSRP measurement requirements for NTN band above 10 GHz1294

9.5C.7.1SSB based L1-RSRP Reporting1294

9.5C.7.2CSI-RS based L1-RSRP Reporting1295

9.5C.8Measurement restriction for L1-RSRP measurement for NTN band above 10 GHz1296

9.5C.8.1Measurement restriction for SSB based L1-RSRP1296

9.5C.8.2Measurement restriction for CSI-RS based L1-RSRP1296

9.5C.9Scheduling availability of UE during L1-RSRP measurement for NTN band above 10 GHz1297

9.5C.9.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on NTN bands above 10 GHz1297

9.5C.9.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on NTN bands above 10 GHz1297

9.5DL1-RSRP measurements for Reporting for ATG1297

9.5D.1Introduction1297

9.5D.2Requirements applicability1297

9.5D.3Measurement Reporting Requirements1298

9.5D.3.1Periodic Reporting1298

9.5D.3.2Semi-Persistent Reporting1298

9.5D.3.3Aperiodic Reporting1298

9.5D.4L1-RSRP measurement requirements1298

9.5D.4.1SSB based L1-RSRP Reporting1298

9.5D.4.2CSI-RS based L1-RSRP Reporting1300

9.5D.5Measurement restriction for CSI-RS and SSB for L1-RSRP measurement1302

9.5D.5.1Measurement restriction for SSB based L1-RSRP1302

9.5D.5.2Measurement restriction for CSI-RS based L1-RSRP1302

9.5D.6Scheduling availability of UE during L1-RSRP measurement1303

9.5D.6.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR11303

9.5D.6.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR11303

9.5EL1-RSRP measurements for Reporting for RedCap UEs with satellite access1303

9.5E.1Introduction1303

9.5E.2Requirements applicability1303

9.5E.3Measurement Reporting Requirements1304

9.5E.3.1Periodic Reporting1304

9.5E.3.2Semi-Persistent Reporting1304

9.5E.3.3Aperiodic Reporting1305

9.5E.4L1-RSRP measurement requirements1305

9.5E.4.1SSB based L1-RSRP Reporting1305

9.5E.4.2CSI-RS based L1-RSRP Reporting1305

9.5E.5Measurement restriction for L1-RSRP measurement1305

9.5E.6Scheduling availability of UE during L1-RSRP measurement1305

9.5E.6.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR11305

9.5E.6.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR11306

9.5FL1-RSRP measurements Reporting for Beam Prediction1306

9.5F.1Introduction1306

9.5F.2Requirements applicability1306

9.5F.3Measurement Reporting Requirements1307

9.5F.3.1Periodic Reporting1307

9.5F.3.2Semi-Persistent Reporting1307

9.5F.3.3Aperiodic Reporting1307

9.5F.4L1-RSRP measurement and prediction requirements1308

9.5F.4.1SSB based RS prediction reporting1308

9.5F.4.2CSI-RS based RS prediction reporting1309

9.6NE-DC: Measurements1311

9.6.1Introduction1311

9.6.2SFTD Measurements1312

9.6.2.1Introduction1312

9.6.2.2SFTD Measurement requirements1312

9.7Cross Link Interference measurements1312

9.7.1Introduction1312

9.7.2SRS-RSRP measurements1313

9.7.2.1Introduction1313

9.7.2.2Requirements applicability1313

9.7.2.3Measurement Reporting Requirements1313

9.7.2.3.1Periodic Reporting1313

9.7.2.3.2Event-triggered Periodic Reporting1313

9.7.2.3.3Event Triggered Reporting1313

9.7.2.4Measurement capability1314

9.7.2.5SRS-RSRP measurement period1314

9.7.3CLI-RSSI measurements1314

9.7.3.1Introduction1314

9.7.3.2Requirements applicability1314

9.7.3.3Measurement Reporting Requirements1314

9.7.3.3.1Periodic Reporting1315

9.7.3.3.2Event-triggered Periodic Reporting1315

9.7.3.3.3Event Triggered Reporting1315

9.7.3.4Measurement capability1315

9.7.3.5CLI-RSSI measurement period1315

9.7.4Scheduling availability of UE during CLI measurements1315

9.7.4.1Scheduling availability of UE performing measurement on FR11315

9.7.4.2Scheduling availability of UE performing measurement on FR21316

9.8L1-SINR measurements for Reporting1317

9.8.1Introduction1317

9.8.2Requirements applicability1318

9.8.3Measurement Reporting Requirements1319

9.8.3.1Periodic Reporting1319

9.8.3.2Semi-Persistent Reporting1319

9.8.4L1-SINR measurement requirements1319

9.8.4.1L1-SINR reporting with CSI-RS based CMR and no dedicated IMR configured1319

9.8.4.2L1-SINR reporting with SSB based CMR and dedicated IMR configured1324

9.8.4.3L1-SINR reporting with CSI-RS based CMR and dedicated IMR configured1326

9.8.5Measurement restriction for L1-SINR measurement1329

9.8.5.1Measurement restriction if SSB configured for L1-SINR Measurement1329

9.8.5.2Measurement restriction if CSI-RS configured for L1-SINR measurement1330

9.8.5.3Measurement restriction if CSI-IM configured for L1-SINR measurement1331

9.8.6Scheduling availability of UE during L1-SINR measurement1332

9.8.6.1Scheduling availability of UE performing L1-SINR measurement with a same subcarrier spacing as PDSCH/PDCCH on FR11332

9.8.6.2Scheduling availability of UE performing L1-SINR measurement with a different subcarrier spacing than PDSCH/PDCCH on FR11332

9.8.6.4Scheduling availability of UE performing L1-SINR measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA1334

9.8.7Minimum requirement at transitions1334

9.8DL1-SINR measurements for Reporting for ATG1334

9.8D.1Introduction1334

9.8D.2Requirements applicability1335

9.8D.3Measurement Reporting Requirements1335

9.8D.3.1Periodic Reporting1336

9.8D.3.2Semi-Persistent Reporting1336

9.8D.3.3Aperiodic Reporting1336

9.8D.4L1-SINR measurement requirements1336

9.8D.4.1L1-SINR reporting with CSI-RS based CMR and no dedicated IMR configured1336

9.8D.4.2L1-SINR reporting with SSB based CMR and dedicated IMR configured1338

9.8D.4.3L1-SINR reporting with CSI-RS based CMR and dedicated IMR configured1339

9.8D.5Measurement restriction for L1-SINR measurement1340

9.8D.5.1Measurement restriction if SSB configured for L1-SINR Measurement1340

9.8D.5.2Measurement restriction if CSI-RS configured for L1-SINR measurement1340

9.8D.5.3Measurement restriction if CSI-IM configured for L1-SINR measurement1341

9.8D.6Scheduling availability of UE during L1-SINR measurement1341

9.8D.6.1Scheduling availability of UE performing L1-SINR measurement with a same subcarrier spacing as PDSCH/PDCCH on FR11341

9.8D.6.2Scheduling availability of UE performing L1-SINR measurement with a different subcarrier spacing than PDSCH/PDCCH on FR11341

9.9NR measurements for positioning1341

9.9.1Introduction1341

9.9.1.1General Aspects of Gap-based Measurement1341

9.9.1.2General Aspects of Gapless Measurement1342

9.9.1.3Scheduling Availability of UE during PRS Measurement without Measurement Gaps1343

9.9.2RSTD measurements1344

9.9.2.1Introduction1344

9.9.2.2Requirements Applicability1344

9.9.2.3Measurement Capability1345

9.9.2.4Measurement Reporting Requirements1345

9.9.2.4.1Void1345

9.9.2.4.2Void1345

9.9.2.4.3Void1345

9.9.2.5Measurements Period Requirements1345

9.9.2.6Void1348

9.9.2.7Measurements Period Requirements without Measurement Gaps1348

9.9.2.8Void1351

9.9.2.9Measurements Period Requirements with both MG and PPW1351

9.9.2.10Measurements Period Requirements with Bandwidth Aggregation1352

9.9.3PRS-RSRP measurements1355

9.9.3.1Introduction1355

9.9.3.2Requirements applicability1355

9.9.3.3Measurement Capability1355

9.9.3.4Measurement Reporting Requirements1356

9.9.3.5Measurement Period Requirements1356

9.9.3.6Measurement Period Requirements without Measurement Gaps1358

9.9.3.7Void1361

9.9.3.8Measurements Period Requirements with both MG and PPW1361

9.9.4UE Rx-Tx time difference measurements1361

9.9.4.1Introduction1361

9.9.4.2Requirements Applicability1362

9.9.4.3Measurement Capability1362

9.9.4.4Measurement Reporting Requirements1362

9.9.4.5Measurement Period Requirements1362

9.9.4.6Measurement Period Requirements without Measurement Gaps1366

9.9.4.7Void1369

9.9.4.8Measurements Period Requirements with both MG and PPW1369

9.9.4.9Measurements Period Requirements with Bandwidth Aggregation1369

9.9.5E-CID measurements1374

9.9.5.1Introduction1374

9.9.5.2Measurement Requirements1374

9.9.5.2.1Intra-frequency Measurement Requirements1374

9.9.5.2.2Inter-frequency Measurement Requirements1374

9.9.5.2.3Measurement Reporting Delay1374

9.9.6PRS-RSRPP measurements1375

9.9.6.1Introduction1375

9.9.6.2Requirements applicability1375

9.9.6.3Measurement capability1375

9.9.6.4Measurement reporting requirements1375

9.9.6.5Measurement period requirements1375

9.9.6.6Measurement Period Requirements without Measurement Gaps1375

9.9.6.7Void1376

9.9.6.8Measurements Period Requirements with both MG and PPW1376

9.9.7Measurement requirements for DL RSCPD reported with RSTD1376

9.9.7.1Introduction1376

9.9.7.2Requirements Applicability1376

9.9.7.3Measurement Capability1376

9.9.7.4Measurement Reporting Requirements1376

9.9.7.5Measurements Period Requirements for DL RSCPD reported with RSTD1376

9.9.8Measurement requirements for DL RSCP reported with UE Rx-Tx time difference1379

9.9.8.1Introduction1379

9.9.8.2Requirements Applicability1379

9.9.8.3Measurement Capability1380

9.9.8.4Measurement Reporting Requirements1380

9.9.8.5Measurement Period Requirements for DL RSCP and UE Rx-Tx time difference1380

9.9ANR measurements for positioning for RedCap1384

9.9A.1Introduction1384

9.9A.1.1General Aspects of Gap-based Measurement1384

9.9A.1.2General Aspects of Gapless Measurement for RedCap positioning without FH1385

9.9A.1.3Scheduling Availability of UE during PRS Measurement without Measurement Gaps for RedCap positioning without FH1386

9.9A.2RSTD measurements for RedCap1387

9.9A.2.1Introduction1387

9.9A.2.2Requirements Applicability1387

9.9A.2.3Measurement Capability1387

9.9A.2.4Measurement Reporting Requirements1387

9.9A.2.5Measurements Period Requirements without FH1387

9.9A.2.5.1Measurements Period Requirements without FH with MG1387

9.9A.2.5.2Measurements Period Requirements without FH without MG1390

9.9A.2.5.3Measurements Period Requirements without FH with both MG and PPW1393

9.9A.2.6Measurements Period Requirements with FH1394

9.9A.2.6.1Measurements Period Requirements with FH with MG1394

9.9A.3PRS-RSRP measurements for RedCap1396

9.9A.3.1Introduction1396

9.9A.3.2Requirements applicability1396

9.9A.3.3Measurement Capability1396

9.9A.3.4Measurement Reporting Requirements1396

9.9A.3.5Measurements Period Requirements without FH1396

9.9A.3.5.1Measurement Period Requirements without FH with MG1396

9.9A.3.5.2Measurement Period Requirements without FH without MG1399

9.9A.3.5.3Measurements Period Requirements without FH with both MG and PPW1401

9.9A.3.6Measurements Period Requirements with FH1402

9.9A.3.6.1Measurements Period Requirements with FH with MG1402

9.9A.4UE Rx-Tx time difference measurements for RedCap1404

9.9A.4.1Introduction1404

9.9A.4.2Requirements Applicability1404

9.9A.4.3Measurement Capability1404

9.9A.4.4Measurement Reporting Requirements1404

9.9A.4.5Measurement Period Requirements without FH with MG1404

9.9A.4.6Measurement Period Requirements without FH without MG1404

9.9A.4.7Measurements Period Requirements without FH with both MG and PPW1404

9.9A.4.8Measurements Period Requirements with FH1404

9.9A.5PRS-RSRPP measurements for RedCap1406

9.9A.5.1Introduction1406

9.9A.5.2Requirements Applicability1406

9.9A.5.3Measurement Capability1406

9.9A.5.4Measurement Reporting Requirements1407

9.9A.5.5Measurement Period Requirements without FH with MG1407

9.9A.5.6Measurement Period Requirements without FH without MG1407

9.9A.5.7Measurements Period Requirements without FH with both MG and PPW1407

9.9A.5.8Measurements Period Requirements with FH1407

9.9CNR measurements for positioning in Satellite Access1407

9.9C.1Introduction1407

9.9C.1.1General Aspects of Gap-based Measurement1407

9.9C.1.2General Aspects of Gapless Measurement1408

9.9C.1.3Scheduling Availability of UE during PRS Measurement without Measurement Gaps1409

9.9C.2Void1409

9.9C.3Void1409

9.9C.4UE Rx-Tx time difference measurements1409

9.9C.4.1 Introduction1409

9.9C.4.2 Requirements Applicability1409

9.9C.4.3Measurement Capability1409

9.9C.4.4Measurement Reporting Requirements1409

9.9C.4.5Measurement Period Requirements1409

9.9C.4.6Measurement Period Requirements without Measurement Gaps1412

9.9DNR measurements for positioning for RedCap in Satellite Access1414

9.9D.1Introduction1414

9.9D.1.1General Aspects of Gap-based Measurement1414

9.9D.1.2General Aspects of Gapless Measurement1414

9.9D.1.3Scheduling Availability of UE during PRS Measurement without Measurement Gaps1414

9.9D.2Void1415

9.9D.3Void1415

9.9D.4UE Rx-Tx time difference measurements1415

9.9D.4.1 Introduction1415

9.9D.4.2 Requirements Applicability1415

9.9D.4.3Measurement Capability1415

9.9D.4.4Measurement Reporting Requirements1415

9.9D.4.5Measurement Period Requirements1415

9.9D.4.6Measurement Period Requirements without Measurement Gaps1416

9.9EReporting Delay Requirements for DL AI/ML Positioning1416

9.9E.1Introduction1416

9.9E.2General Aspects Relating to Gap-based Measurement1416

9.9E.3General Aspects Relating to Gapless Measurement1417

9.9E.4Scheduling Availability Relating to Gapless Measurement1418

9.9E.5Measurement Delay Requirement with Measurement Gaps1418

9.9E.6Measurement Delay Requirement without Measurement Gaps1420

9.9E.7Measurement Delay Requirement with Bandwidth Aggregation1422

9.10CSI-RS based L3 measurements1426

9.10.1Introduction1426

9.10.2CSI-RS based intra-frequency measurements1426

9.10.2.1Introduction1426

9.10.2.2Requirements applicability1427

9.10.2.3Number of cells and number of CSI-RS1428

9.10.2.3.1Requirements for FR11428

9.10.2.3.2Requirements for FR21428

9.10.2.4Measurement Reporting Requirements1428

9.10.2.4.1Periodic Reporting1428

9.10.2.4.2Event-triggered Periodic Reporting1428

9.10.2.4.3Event Triggered Reporting1429

9.10.2.5Intra-frequency measurements without measurement gaps1429

9.10.2.6Scheduling availability of UE during CSI-RS based intra-frequency measurements1431

9.10.2.6.1Scheduling availability of UE performing CSI-RS based measurements in TDD bands1431

9.10.2.6.2Scheduling availability of UE performing CSI-RS based measurements in FR21432

9.10.3CSI-RS based Inter-frequency measurements1432

9.10.3.1Introduction1432

9.10.3.2Requirements applicability1432

9.10.3.3Number of cells and number of CSI-RS resources1433

9.10.3.3.1Requirements for FR11433

9.10.3.3.2Requirements for FR21433

9.10.3.4Measurements reporting requirements1433

9.10.3.4.1Periodic Reporting1433

9.10.3.4.2Event-triggered Periodic Reporting1433

9.10.3.4.3Event-triggered Reporting1434

9.10.3.5Inter-frequency measurements with measurement gaps1434

9.10DCSI-RS based L3 measurements for ATG1436

9.10D.1Introduction1436

9.10D.2CSI-RS based intra-frequency measurements1436

9.10D.2.1Introduction1436

9.10D.2.2Requirements applicability1436

9.10D.2.3Number of cells and number of CSI-RS1437

9.10D.2.3.1Requirements for FR11437

9.10D.2.4Measurement Reporting Requirements1437

9.10D.2.4.1Periodic Reporting1438

9.10D.2.4.2Event-triggered Periodic Reporting1438

9.10D.2.4.3Event Triggered Reporting1438

9.10D.2.5Intra-frequency measurements without measurement gaps1438

9.10D.2.6Scheduling availability of UE during CSI-RS based intra-frequency measurements1440

9.10D.2.6.1Scheduling availability of UE performing CSI-RS based measurements on FR11441

9.10D.3CSI-RS based Inter-frequency measurements1441

9.10D.3.1Introduction1441

9.10D.3.2Requirements applicability1441

9.10D.3.3Number of cells and number of CSI-RS resources1442

9.10D.3.3.1Requirements for FR11442

9.10D.3.4Measurements reporting requirements1442

9.10D.3.4.1Periodic Reporting1442

9.10D.3.4.2Event-triggered Periodic Reporting1442

9.10D.3.4.3Event-triggered Reporting1442

9.10D.3.5Inter-frequency measurements with measurement gaps1443

9.11NR measurements with autonomous gaps1444

9.11.1Introduction1444

9.11.2CGI identification of an NR cell with autonomous gaps1444

9.11.3CGI reporting delay1445

9.11ANR measurements with autonomous gaps for RedCap1445

9.11A.1Introduction1445

9.11A.2CGI identification of an NR cell with autonomous gaps1446

9.11A.3CGI reporting delay1446

9.11A.4CGI reporting scheduling restriction1447

9.11DNR measurements with autonomous gaps for ATG1447

9.11D.1Introduction1447

9.11D.2CGI identification of an NR cell with autonomous gaps1448

9.11D.3CGI reporting delay1448

9.12Measurement for Propagation Delay Compensation1449

9.12.1Introduction1449

9.12.2Requirements Applicability1449

9.12.3Measurement Capability1449

9.12.4Measurement period requirements1449

9.12.4.1PRS Measurement Period1449

9.12.4.2TRS Measurement Period1450

9.12.5Measurement Reporting Requirements1451

9.12.6Scheduling availability during measurement for Propagation Delay Compensation1451

9.12.7Measurement restriction for measurement for Propagation Delay Compensation1451

9.12.8Measurement requirement for Propagation Delay Compensation with MUSIM gaps1452

9.13L1-RSRP measurements for a cell with different PCI from serving cell1452

9.13.1Introduction1452

9.13.2Requirements Applicability1452

9.13.3Measurement Reporting Requirements1453

9.13.3.1Periodic Reporting1453

9.13.3.2Semi-Persistent Reporting1453

9.13.3.3Aperiodic Reporting1453

9.13.3.4Event triggered reporting for UE initiated beam management1454

9.13.4L1-RSRP measurement requirements1455

9.13.4.1Inter-cell SSB based L1-RSRP Reporting1455

9.13.5Measurement restriction for L1-RSRP measurement1458

9.13.5.1Measurement restriction for SSB based L1-RSRP1458

9.13.6Scheduling availability of UE during L1-RSRP measurement1459

9.13.6.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR11459

9.13.6.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR11459

9.13.6.3Scheduling availability of UE performing L1-RSRP measurement on FR21460

9.13.6.4Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA1461

9.13.6.5Scheduling availability of UE performing L1-RSRP measurement in TDD bands on FR11461

9.14NR intra-frequency L1-RSRP measurements for neighbor cell1461

9.14.1Introduction1461

9.14.2Requirements Applicability1461

9.14.3Measurement Reporting Requirements1462

9.14.3.1Periodic Reporting1462

9.14.3.2Semi-Persistent Reporting1462

9.14.3.3Aperiodic Reporting1462

9.14.3.4Event Triggered Reporting1462

9.14.3.5Event-triggered Periodic Reporting1463

9.14.4Number of SSB frequency layers, number of cells and number of SSBs1463

9.14.5L1-RSRP intra-frequency measurement requirements without measurement gaps1463

9.14.5.1SSB based L1-RSRP reporting1463

9.14.6Measurement restriction for L1-RSRP measurement1466

9.14.6.1Measurement restriction for SSB based L1-RSRP1466

9.14.7Scheduling availability of UE during L1-RSRP measurement1467

9.14.7.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR11467

9.14.7.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR11467

9.14.7.3Scheduling availability of UE performing L1-RSRP measurement on FR21468

9.14.7.4Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA1468

9.14.7.5Scheduling availability of UE performing L1-RSRP measurement in TDD bands on FR11468

9.14aCSI-RS based Intra-frequency L1-RSRP measurements for neighbour cell1469

9.14a.1Introduction1469

9.14a.2Requirements Applicability1469

9.14a.3Measurement Reporting Requirements1470

9.14a.3.1Periodic Reporting1470

9.14a.3.2Semi-Persistent Reporting1470

9.14a.3.3Aperiodic Reporting1470

9.14a.3.4Event-triggered Periodic Reporting1470

9.14a.3.5Event Triggered Reporting1470

9.14a.4Number of CSI-RS resources, number of cells1471

9.14a.5CSI-RS based L1-RSRP measurement requirements without measurement gaps1471

9.14a.6Measurement restriction for CSI-RS based L1-RSRP measurement1472

9.14a.6.1Measurement restriction for CSI-RS based L1-RSRP measurement1473

9.14a.7Scheduling availability of UE during CSI-RS based L1-RSRP measurement1474

9.14a.7.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR11474

9.14a.7.2Scheduling availability of UE performing L1-RSRP measurement on FR21474

9.14a.7.3Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA1475

9.14a.7.4Scheduling availability of UE performing L1-RSRP measurement in TDD bands on FR11475

9.15NR inter-frequency L1-RSRP measurements for neighbor cell1475

9.15.1Introduction1475

9.15.2Requirements Applicability1475

9.15.3Measurement Reporting Requirements1476

9.15.3.1Periodic Reporting1476

9.15.3.2Semi-Persistent Reporting1476

9.15.3.3Aperiodic Reporting1476

9.15.3.4Event Triggered Reporting1477

9.15.3.5Event Triggered Periodic Reporting1477

9.15.4Number of SSB frequency layers, number of cells and number of SSBs1477

9.15.5L1-RSRP inter-frequency measurement requirements with measurement gaps1477

9.15.5.1Inter-frequency SSB based L1-RSRP reporting1477

9.15.6L1-RSRP inter-frequency L1-RSRP measurement requirements without measurement gaps1479

9.15.6.1Inter-frequency L1-RSRP measurement requirements1479

9.15.6.1.1Inter-frequency SSB based L1-RSRP measurement1479

9.15.6.2Measurement restriction for inter-frequency L1-RSRP measurement1482

9.15.6.2.1Measurement restriction for SSB based L1-RSRP1482

9.15.6.3Scheduling availability of UE during inter-frequency L1-RSRP measurements1483

9.15.6.3.1Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR11483

9.15.6.3.2Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR11483

9.15.6.3.3Scheduling availability of UE performing L1-RSRP measurement on FR21484

9.15.6.3.4Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA1484

9.15.6.3.5Scheduling availability of UE performing L1-RSRP measurement in TDD bands on FR11484

9.16CJT calibration reporting for Delay offset and Frequency offset1485

9.16.1Introduction1485

9.16.2Requirements applicability1485

9.16.3Measurement Reporting Requirements1485

9.16.3.1Aperiodic Reporting1485

After the UE receives CSI request in DCI with (reportQuantity set to ‘cjtc-Dd’, ‘cjtc-F’), the UE shall transmit the aperiodic CJTC reporting on PUSCH over the air interface at the time specified according to relevant clause in [26].9.16.4 Measurement Requirements1485

## 9.16.4.1 CSI -RS based delay and frequency offset reporting1485

9.16.5Measurement restriction for UE during CJT calibration reporting1487

9.16.5.1Measurement restriction for CJT calibration reporting1487

9.16.6Scheduling availability of UE during CJT calibration reporting1487

9.16.6.1Scheduling availability of UE performing measurement for CJT calibration reporting on FR11487

9.17OD-SSB based L3 measurement for an SCell1488

9.17.1Introduction1488

9.17.2Requirements Applicability1488

9.17.3Number of cells and number of SSB1488

9.17.4Measurement Reporting Requirements1489

9.17.5OD-SSB based Intra-frequency measurements without measurement gaps1489

9.17.5.1Intra-frequency cell identification for active SCell1489

9.17.5.2Measurement period for active SCell1494

9.17.5.3Intra-frequency cell identification for deactivated SCell1496

9.17.5.4Measurement period for deactivated SCell1499

9.17.5.5Scheduling availability of UE during intra-frequency measurements based on On-demand SSB1500

9.17.5.5.1Scheduling availability of UE performing measurements in TDD bands on FR11500

9.17.5.5.2Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR11500

9.17.5.5.3Scheduling availability of UE performing measurements on FR2-11501

9.17.5.5.4Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA1502

9.18L1 Cross Link Interference measurements1502

9.18.1Introduction1502

9.18.2L1-SRS-RSRP measurements1503

9.18.2.1Introduction1503

9.18.2.2Requirements applicability1503

9.18.2.3Measurement Reporting Requirements1503

9.18.2.3.1Aperiodic Reporting1503

9.18.2.4Measurement capability1504

9.18.2.5L1-SRS-RSRP measurement period1504

9.18.2.6Scheduling availability of UE during L1-CLI measurements1504

9.18.2.6.1Scheduling availability of UE performing L1-SRS-RSRP measurement on FR11504

9.18.2.6.2Scheduling availability of UE performing L1-SRS-RSRP measurement on FR21505

9.18.3L1-CLI-RSSI measurements1506

9.18.3.1Introduction1506

9.18.3.2Requirements applicability1506

9.18.3.3Measurement Reporting Requirements1506

9.18.3.3.1Periodic Reporting1506

9.18.3.3.2Aperiodic Reporting1506

9.18.3.4Measurement capability1507

9.18.3.5L1-CLI-RSSI measurement period1507

9.18.3.6Scheduling availability of UE during L1-CLI-RSSI measurements1507

9.18.3.6.1Scheduling availability of UE performing L1-CLI-RSSI measurement on FR11508

9.18.3.6.2Scheduling availability of UE performing L1-CLI-RSSI measurement on FR21508

10Measurement Performance requirements1509

10.1NR measurements1509

10.1.1Introduction1509

10.1.2Intra-frequency RSRP accuracy requirements for FR11509

10.1.2.1Intra-frequency SS-RSRP accuracy requirements1509

10.1.2.1.1Absolute SS-RSRP Accuracy1509

10.1.2.1.2Relative SS-RSRP Accuracy1510

10.1.2.2Void1511

10.1.2.3Intra-frequency CSI-RSRP accuracy requirements1511

10.1.2.3.1Absolute CSI-RSRP Accuracy1511

10.1.2.3.2Relative CSI-RSRP Accuracy1512

10.1.2BIntra-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode Measurements1513

10.1.2B.1Intra-frequency SS-RSRP accuracy requirements1513

10.1.2B.1.1Absolute SS-RSRP Accuracy1513

10.1.2CIntra-frequency RSRP accuracy requirements for FR1 SAN1514

10.1.2C.1Intra-frequency SS-RSRP accuracy requirements1514

10.1.2C.1.1Absolute SS-RSRP Accuracy1514

10.1.2C.1.2Relative SS-RSRP Accuracy1515

10.1.2DIntra-frequency RSRP accuracy requirements for RedCap UE with Satellite Access in FR11516

10.1.2D.1Intra-frequency SS-RSRP accuracy requirements1516

10.1.2D.1.1Absolute SS-RSRP Accuracy1516

10.1.2D.1.2Relative SS-RSRP Accuracy1516

10.1.3Intra-frequency RSRP accuracy requirements for FR21517

10.1.3.1Intra-frequency SS-RSRP accuracy requirements1517

10.1.3.1.1Absolute SS-RSRP Accuracy1517

10.1.3.1.2Relative SS-RSRP Accuracy1518

10.1.3.2Void1518

10.1.3.3Intra-frequency CSI-RSRP accuracy requirements1518

10.1.3.3.1Absolute CSI-RSRP Accuracy1518

10.1.3.3.2Relative CSI-RSRP Accuracy1519

10.1.3BIntra-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode Measurements1520

10.1.3B.1Intra-frequency SS-RSRP accuracy requirements1520

10.1.3B.1.1Absolute SS-RSRP Accuracy1520

10.1.3CIntra-frequency RSRP accuracy requirements for FR2-NTN1521

10.1.3C.1Intra-frequency SS-RSRP accuracy requirements1521

10.1.3C.1.1Absolute SS-RSRP Accuracy1521

10.1.3C.1.2Relative SS-RSRP Accuracy1522

10.1.4Inter-frequency RSRP accuracy requirements for FR11522

10.1.4.1Inter-frequency SS-RSRP accuracy requirements1522

10.1.4.1.1Absolute SS-RSRP Accuracy in FR11522

10.1.4.1.2Relative SS-RSRP Accuracy in FR11523

10.1.4.2Void1524

10.1.4.3Inter-frequency CSI-RSRP accuracy requirements1524

10.1.4.3.1Absolute CSI-RSRP Accuracy in FR11524

10.1.4.3.2Relative CSI-RSRP Accuracy in FR11525

10.1.4BInter-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode Measurements1526

10.1.4B.1Inter-frequency SS-RSRP accuracy requirements1526

10.1.4B.1.1Absolute SS-RSRP Accuracy in FR11527

10.1.4CInter-frequency RSRP accuracy requirements for FR1 SAN1528

10.1.4C.1Inter-frequency SS-RSRP accuracy requirements1528

10.1.4C.1.1Absolute SS-RSRP Accuracy in FR11528

10.1.4C.1.2Relative SS-RSRP Accuracy in FR11528

10.1.4DInter-frequency RSRP accuracy requirements for RedCap UE with Satellite Access in FR11529

10.1.4D.1Inter-frequency SS-RSRP accuracy requirements1529

10.1.4D.1.1Absolute SS-RSRP Accuracy in FR11529

10.1.4D.1.2Relative SS-RSRP Accuracy in FR11529

10.1.5Inter-frequency RSRP accuracy requirements for FR21530

10.1.5.1Inter-frequency SS-RSRP accuracy requirements1530

10.1.5.1.1Absolute SS-RSRP Accuracy1530

10.1.5.1.2Relative SS-RSRP Accuracy1531

10.1.5.2Void1532

10.1.5.3Inter-frequency CSI-RSRP accuracy requirements1532

10.1.5.3.1Absolute CSI-RSRP Accuracy1532

10.1.5.3.2Relative CSI-RSRP Accuracy1532

10.1.5BInter-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode Measurements1533

10.1.5B.1Inter-frequency SS-RSRP accuracy requirements1533

10.1.5B.1.1Absolute SS-RSRP Accuracy1533

10.1.5CInter-frequency RSRP accuracy requirements for FR2-NTN1534

10.1.5C.1Inter-frequency SS-RSRP accuracy requirements1534

10.1.5C.1.1Absolute SS-RSRP Accuracy1534

10.1.5C.1.2Relative SS-RSRP Accuracy1535

10.1.6RSRP Measurement Report Mapping1535

10.1.7Intra-frequency RSRQ accuracy requirements for FR11537

10.1.7.1Intra-frequency SS-RSRQ accuracy requirements in FR11537

10.1.7.1.1Absolute SS-RSRQ Accuracy in FR11537

10.1.7.2Intra-frequency CSI-RSRQ accuracy requirements1538

10.1.7.2.1Absolute CSI-RSRQ Accuracy1538

10.1.7BIntra-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode Measurements1539

10.1.7B.1Intra-frequency SS-RSRQ accuracy requirements in FR11539

10.1.7B.1.1Absolute SS-RSRQ Accuracy in FR11539

10.1.7CIntra-frequency RSRQ accuracy requirements for FR1 SAN1540

10.1.7C.1Intra-frequency SS-RSRQ accuracy requirements in FR11540

10.1.7C.1.1Absolute SS-RSRQ Accuracy in FR11540

10.1.7DIntra-frequency RSRQ accuracy requirements for RedCap UE with Satellite Access in FR11541

10.1.7D.1Intra-frequency SS-RSRQ accuracy requirements in FR11541

10.1.7D.1.1Absolute SS-RSRQ Accuracy in FR11541

10.1.8Intra-frequency RSRQ accuracy requirements for FR21542

10.1.8.1Intra-frequency SS-RSRQ accuracy requirements in FR21542

10.1.8.1.1Absolute SS-RSRQ Accuracy in FR21542

10.1.8.2Intra-frequency CSI-RSRQ accuracy requirements1542

10.1.8.2.1Absolute CSI-RSRQ Accuracy1542

10.1.8BIntra-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode Measurements1543

10.1.8B.1Intra-frequency SS-RSRQ accuracy requirements in FR21543

10.1.8B.1.1Absolute SS-RSRQ Accuracy in FR21543

10.1.8CIntra-frequency RSRQ accuracy requirements for FR2-NTN1544

10.1.8C.1Intra-frequency SS-RSRQ accuracy requirements in FR2-NTN1544

10.1.8C.1.1Absolute SS-RSRQ Accuracy in FR2-NTN1544

10.1.9Inter-frequency RSRQ accuracy requirements for FR11545

10.1.9.1Inter-frequency SS-RSRQ accuracy requirements in FR11545

10.1.9.1.1Absolute SS-RSRQ Accuracy in FR11545

10.1.9.1.2Relative SS-RSRQ Accuracy in FR11545

10.1.9.2Inter-frequency CSI-RSRQ accuracy requirements1546

10.1.9.2.1Absolute CSI-RSRQ Accuracy1546

10.1.9.2.2Relative CSI-RSRQ Accuracy1547

10.1.9BInter-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode Measurements1548

10.1.9B.1Inter-frequency SS-RSRQ accuracy requirements in FR11548

10.1.9B.1.1Absolute SS-RSRQ Accuracy in FR11548

10.1.9CInter-frequency RSRQ accuracy requirements for FR1 SAN1549

10.1.9C.1Inter-frequency SS-RSRQ accuracy requirements in FR11549

10.1.9C.1.1Absolute SS-RSRQ Accuracy in FR11549

10.1.9C.1.2Relative SS-RSRQ Accuracy in FR11550

10.1.9DInter-frequency RSRQ accuracy requirements for RedCap UE with Satellite Access in FR11551

10.1.9D.1Inter-frequency SS-RSRQ accuracy requirements in FR11551

10.1.9D.1.1Absolute SS-RSRQ Accuracy in FR11551

10.1.9D.1.2Relative SS-RSRQ Accuracy in FR11551

10.1.10Inter-frequency RSRQ accuracy requirements for FR21552

10.1.10.1Inter-frequency SS-RSRQ accuracy requirements in FR21552

10.1.10.1.1Absolute SS-RSRQ Accuracy in FR21552

10.1.10.1.2Relative SS-RSRQ Accuracy in FR21552

10.1.10.2Inter-frequency CSI-RSRQ accuracy requirements1553

10.1.10.2.1Absolute CSI-RSRQ Accuracy1553

10.1.10.2.2Relative CSI-RSRQ Accuracy1554

10.1.10B Inter-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode Measurements1555

10.1.10B.1Inter-frequency SS-RSRQ accuracy requirements in FR21555

10.1.10B.1.1Absolute SS-RSRQ Accuracy in FR21555

10.1.10CInter-frequency RSRQ accuracy requirements for FR2-NTN1556

10.1.10C.1Inter-frequency SS-RSRQ accuracy requirements in FR2-NTN1556

10.1.10C.1.1Absolute SS-RSRQ Accuracy in FR2-NTN1556

10.1.10C.1.2Relative SS-RSRQ Accuracy in FR2-NTN1556

10.1.11RSRQ report mapping1557

10.1.12Intra-frequency SINR accuracy requirements for FR11558

10.1.12.1Intra-frequency SS-SINR accuracy requirements in FR11558

10.1.12.1.1Absolute SS-SINR Accuracy in FR11558

10.1.12.2Intra-frequency CSI-SINR accuracy requirements in FR11558

10.1.12.2.1Absolute CSI-SINR Accuracy in FR11558

10.1.12C Intra-frequency SINR accuracy requirements for FR1 SAN1559

10.1.12C.1Intra-frequency SS-SINR accuracy requirements in FR11559

10.1.12C.1.1Absolute SS-SINR Accuracy in FR11559

10.1.12D Intra-frequency SINR accuracy requirements for RedCap UE with Satellite Access in FR11560

10.1.12D.1Intra-frequency SS-SINR accuracy requirements in FR11560

10.1.12D.1.1Absolute SS-SINR Accuracy in FR11560

10.1.13Intra-frequency SINR accuracy requirements for FR21561

10.1.13.1Intra-frequency SS-SINR accuracy requirements in FR21561

10.1.13.1.1Absolute SS-SINR Accuracy in FR21561

10.1.13.2Intra-frequency CSI-SINR accuracy requirements in FR21561

10.1.13.2.1Absolute CSI-SINR Accuracy in FR21561

10.1.13CIntra-frequency SINR accuracy requirements for FR2-NTN1562

10.1.13C.1Intra-frequency SS-SINR accuracy requirements in FR2-NTN1562

10.1.13C.1.1Absolute SS-SINR Accuracy in FR2-NTN1562

10.1.14Inter-frequency SINR accuracy requirements for FR11563

10.1.14.1Inter-frequency SS-SINR accuracy requirements in FR11563

10.1.14.1.1Absolute SS-SINR Accuracy in FR11563

10.1.14.1.2Relative SS-SINR Accuracy in FR11563

10.1.14.2Inter-frequency CSI-SINR accuracy requirements in FR11564

10.1.14.2.1Absolute CSI-SINR Accuracy in FR11564

10.1.14.2.2Relative CSI-SINR Accuracy in FR11565

10.1.14C Inter-frequency SINR accuracy requirements for FR1 SAN1566

10.1.14C.1Inter-frequency SS-SINR accuracy requirements in FR11566

10.1.14C.1.1Absolute SS-SINR Accuracy in FR11566

10.1.14C.1.2Relative SS-SINR Accuracy in FR11567

10.1.14D Inter-frequency SINR accuracy requirements for RedCap UE with Satellite Access in FR11568

10.1.14D.1Inter-frequency SS-SINR accuracy requirements in FR11568

10.1.14D.1.1Absolute SS-SINR Accuracy in FR11568

10.1.14D.1.2Relative SS-SINR Accuracy in FR11568

10.1.15Inter-frequency SINR accuracy requirements for FR21569

10.1.15.1Inter-frequency SS-SINR accuracy requirements in FR21569

10.1.15.1.1Absolute SS-SINR Accuracy in FR21569

10.1.15.1.2Relative SS-SINR Accuracy in FR21569

10.1.15.2Inter-frequency CSI-SINR accuracy requirements in FR21570

10.1.15.2.1Absolute CSI-SINR Accuracy in FR21570

10.1.15.2.2Relative CSI-SINR Accuracy in FR21571

10.1.15CInter-frequency SINR accuracy requirements for FR2-NTN1572

10.1.15C.1Inter-frequency SS-SINR accuracy requirements in FR2-NTN1572

10.1.15C.1.1Absolute SS-SINR Accuracy in FR2-NTN1572

10.1.15C.1.2Relative SS-SINR Accuracy in FR2-NTN1572

10.1.16SINR report mapping1573

10.1.16.1SS-SINR and CSI-SINR measurement report mapping1573

10.1.17Power Headroom1574

10.1.17.1Power Headroom Report1574

10.1.17.1.1Power Headroom Report Mapping1574

10.1.18PCMAX,c,f1574

10.1.18.1Report Mapping1574

10.1.19L1-RSRP accuracy requirements for FR11575

10.1.19.1SSB based L1-RSRP accuracy requirements1575

10.1.19.1.1Absolute Accuracy1575

10.1.19.1.2Relative Accuracy1576

10.1.19.2CSI-RS based L1-RSRP accuracy requirements1577

10.1.19.2.1Absolute Accuracy1577

10.1.19.2.2Relative Accuracy1579

10.1.19CL1-RSRP accuracy requirements for FR1 SAN1581

10.1.19C.1SSB based L1-RSRP accuracy requirements1581

10.1.19C.1.1Absolute Accuracy1581

10.1.19C.1.2Relative Accuracy1582

10.1.19C.2CSI-RS based L1-RSRP accuracy requirements1582

10.1.19C.2.1Absolute Accuracy1582

10.1.19C.2.2Relative Accuracy1583

10.1.19DLTM Intra-frequency L1-RSRP accuracy requirements for FR11584

10.1.19D.1SSB based intra-frequency L1-RSRP accuracy requirements1584

10.1.19D.1.1Absolute Accuracy1584

10.1.19D.1.2Relative Accuracy1585

10.1.19D.2CSI-RS based intra-frequency L1-RSRP accuracy requirements1585

10.1.19D.2.1Absolute CSI-RSRP Accuracy1585

10.1.19D.2.2Relative CSI-RSRP Accuracy1586

10.1.19ELTM Inter-frequency L1-RSRP accuracy requirements for FR11587

10.1.19E.1SSB based Inter-frequency L1-RSRP accuracy requirements1587

10.1.19E.1.1Absolute Accuracy1587

10.1.19E.1.2Relative Accuracy1588

10.1.19FL1-RSRP accuracy requirements for RedCap UE with Satellite Access in FR11589

10.1.19F.1SSB based L1-RSRP accuracy requirements1589

10.1.19F.1.1Absolute Accuracy1589

10.1.19F.1.2Relative Accuracy1590

10.1.19F.2CSI-RS based L1-RSRP accuracy requirements1590

10.1.19F.2.1Absolute Accuracy1590

10.1.19F.2.2Relative Accuracy1591

10.1.20L1-RSRP accuracy requirements for FR21592

10.1.20.1SSB based L1-RSRP accuracy requirements1592

10.1.20.1.1Absolute Accuracy1592

10.1.20.1.2Relative Accuracy1592

10.1.20.2CSI-RS based L1-RSRP accuracy requirements1593

10.1.20.2.1Absolute Accuracy1593

10.1.20.2.2Relative Accuracy1594

10.1.20A  LTM Intra-frequency L1-RSRP accuracy requirements for FR21595

10.1.20A.1SSB based intra-frequency L1-RSRP accuracy requirements1595

10.1.20A.1.1Absolute Accuracy1595

10.1.20A.1.2Relative Accuracy1596

10.1.20A.2CSI-RS based intra-frequency L1-RSRP accuracy requirements1597

10.1.20A.2.1Absolute Accuracy1597

10.1.20A.2.2Relative Accuracy1597

10.1.20BLTM Inter-frequency L1-RSRP accuracy requirements for FR21598

10.1.20B.1SSB based inter-frequency L1-RSRP accuracy requirements1598

10.1.20B.1.1Absolute Accuracy1598

10.1.20B.1.2Relative Accuracy1599

10.1.20CL1-RSRP accuracy requirements for FR2-NTN1599

10.1.20C.1SSB based L1-RSRP accuracy requirements1599

10.1.20C.1.1Absolute Accuracy1599

10.1.20C.1.2Relative Accuracy1600

10.1.20C.2CSI-RS based L1-RSRP accuracy requirements1601

10.1.20C.2.1Absolute Accuracy1601

10.1.20C.2.2Relative Accuracy1601

10.1.20D Predicted L1-RSRP accuracy requirements for FR21602

10.1.20D.1CSI-RS based predicted L1-RSRP accuracy requirements1602

10.1.20D.1.1Absolute Accuracy1602

10.1.21SFTD accuracy requirements1604

10.1.21.1SFTD acuracy requirements for NE-DC1604

10.1.21.2SFTD acuracy requirements for NR-DC1606

10.1.21.3Inter-frequency SFTD acuracy requirements1607

10.1.22CLI measurement accuracy requirements1608

10.1.22.1SRS-RSRP1608

10.1.22.1.1SRS-RSRP Accuracy1608

10.1.22.1.2SRS-RSRP report mapping1609

10.1.22.2CLI-RSSI1610

10.1.22.2.1CLI-RSSI Accuracy1610

10.1.22.2.2CLI-RSSI report mapping1611

10.1.23RSTD Measurements1611

10.1.23.1Introduction1611

10.1.23.2Measurement Accuracy Requirements1611

10.1.23.3Report mapping1619

10.1.23.3.1Absolute DL RSTD Measurement Reporting1619

10.1.23.3.2Differential Reporting for DL RSTD Measurement1622

10.1.23.3.3Additional Path Report Mapping for DL RSTD1625

10.1.23ARSTD Measurements Based on PRS Aggregation1629

10.1.23A.1Introduction1629

10.1.23A.3Report Mapping1636

10.1.23A.3.1Absolute DL RSTD Measurement Reporting1636

10.1.23A.3.2Differential Reporting for DL RSTD Measurement1636

10.1.23A.3.3Additional Path Report Mapping for DL RSTD1636

10.1.24PRS-RSRP Measurements1636

10.1.24.1Introduction1636

10.1.24.2Measurement Accuracy Requirements1637

10.1.24.2.1Absolute PRS-RSRP accuracy1637

10.1.24.2.2Relative PRS RSRP accuracy1641

10.1.24.3Report mapping1645

10.1.24.3.1Absolute PRS-RSRP Measurement Report Mapping1645

10.1.24.3.2Differential Report Mapping for PRS-RSRP Measurement1646

10.1.24APRS-RSRP Measurements Based on PRS Aggregation1648

10.1.24A.1Introduction1648

10.1.24A.2Measurement Accuracy Requirements1649

10.1.24A.2.1Absolute PRS RSRP Accuracy Requirement1649

10.1.24A.2.2Relative PRS RSRP Accuracy Requirement1649

10.1.24A.3Report Mapping1649

10.1.24A.3.1Absolute PRS-RSRP Measurement Report Mapping1649

10.1.24A.3.2Differential Report Mapping for PRS-RSRP Measurement1649

10.1.25UE Rx-Tx Time Difference Measurements1649

10.1.25.1Introduction1649

10.1.25.2Measurement Accuracy Requirements1649

10.1.25.3Report mapping1661

10.1.25.3.1Absolute UE Rx-Tx Measurement Report Mapping1661

10.1.25.3.2Differential UE Rx-Tx Measurement Report Mapping1664

10.1.25.3.3Additional Path Report Mapping for UE Rx-Tx Time Difference1667

10.1.25AUE Rx-Tx Time Difference Measurement Based on PRS Aggregation1670

10.1.25A.1Introduction1670

10.1.25A.2Measurement Accuracy Requirements1671

10.1.25A.3Report mapping1687

10.1.25CUE Rx-Tx Time Difference Measurements in Satellite Accesss1687

10.1.25C.1Introduction1687

10.1.25C.2Measurement Accuracy Requirements1687

10.1.25C.3Report mapping1688

10.1.25DUE Rx-Tx Time Difference Measurements RedCap UE with Satellite Access in FR11688

10.1.25D.1Introduction1688

10.1.25D.2Measurement Accuracy Requirements1689

10.1.25D.2.1UE Rx-Tx Accuracy Requirement for 2Rx RedCap UE without FH1689

10.1.25D.2.2UE Rx-Tx Accuracy Requirement for 1Rx RedCap UE without FH1689

10.1.25D.3Report mapping1689

10.1.26FR2 P-MPR report1689

10.1.26.1Report mapping1690

10.1.27L1-SINR accuracy requirements for FR11690

10.1.27.1L1-SINR accuracy requirements with CSI-RS based CMR and no dedicated IMR configured1690

10.1.27.1.1Absolute Accuracy1690

10.1.27.1.2Relative Accuracy1691

10.1.27.2L1-SINR accuracy requirements with SSB based CMR and dedicated IMR configured1693

10.1.27.2.1Absolute Accuracy1693

10.1.27.2.2Relative Accuracy1696

10.1.27.3L1-SINR accuracy requirements with CSI-RS based CMR and dedicated IMR configured1698

10.1.27.3.1Absolute Accuracy1698

10.1.27.3.2Relative Accuracy1701

10.1.28L1-SINR accuracy requirements for FR21704

10.1.29Intra-frequency RSRQ accuracy requirements under CCA1715

10.1.29.1Intra-frequency SS-RSRQ accuracy requirements in FR11715

10.1.29.1.1Absolute SS-RSRQ Accuracy1715

10.1.30Inter-frequency RSRQ accuracy requirements under CCA1715

10.1.30.1Inter-frequency SS-RSRQ accuracy requirements in FR11715

10.1.30.1.1Absolute SS-RSRQ Accuracy1715

10.1.30.1.2Relative SS-RSRQ Accuracy1716

10.1.31Intra-frequency SINR accuracy requirements under CCA1717

10.1.31.1Intra-frequency SS-SINR accuracy requirements in FR11717

10.1.31.1.1Absolute SS-SINR Accuracy1717

10.1.32Inter-frequency SINR accuracy requirements under CCA1717

10.1.32.1Inter-frequency SS-SINR accuracy requirements in FR11717

10.1.32.1.1Absolute SS-SINR Accuracy1717

10.1.32.1.2Relative SS-SINR Accuracy1718

10.1.33L1-RSRP accuracy requirements under CCA1719

10.1.33.1SSB based L1-RSRP accuracy requirements in FR11719

10.1.33.1.1Absolute Accuracy1719

10.1.33.1.2Relative Accuracy1719

10.1.34RSSI measurements under CCA1720

10.1.34.1Intra-frequency absolute RSSI measurement accuracy requirements in FR11720

10.1.34.2Inter-frequency absolute RSSI measurement accuracy requirements in FR11720

10.1.34.3RSSI measurement report mapping1720

10.1.35Channel occupancy measurements under CCA1721

10.1.35.1Intra-frequency channel occupancy measurement accuracy requirements in FR11721

10.1.35.2Inter-frequency channel occupancy measurement accuracy requirements in FR11721

10.1.36Intra-frequency RSRP accuracy requirements under CCA1721

10.1.36.1Intra-frequency SS-RSRP accuracy requirements in FR11721

10.1.36.1.1Absolute SS-RSRP Accuracy1721

10.1.36.1.2Relative SS-RSRP Accuracy1722

10.1.37Inter-frequency RSRP accuracy requirements under CCA1722

10.1.37.1Inter-frequency SS-RSRP accuracy requirements in FR11722

10.1.37.1.1Absolute SS-RSRP1722

10.1.37.1.2Relative SS-RSRP Accuracy1723

10.1.38PRS-RSRPP Measurements1724

10.1.38.1Introduction1724

10.1.38.2Measurement Accuracy Requirements1724

10.1.38.2.1Absolute PRS RSRPP accuracy1724

10.1.38.3Report mapping1728

10.1.38.3.1Absolute PRS-RSRPP Measurement Report Mapping1728

10.1.38.3.2Differential Report Mapping for PRS-RSRPP Measurement1729

10.1.38APRS-RSRPP Measurements Based on PRS Aggregation1730

10.1. 38A.1Introduction1730

10.1.38A.2Measurement Accuracy Requirements1731

10.1.38A.2.1Absolute PRS RSRPP accuracy1731

10.1.38A.3Report mapping1731

10.1.38A.3.1Absolute PRS-RSRPP Measurement Report Mapping1731

10.1.38A.3.2Differential Report Mapping for PRS-RSRPP Measurement1731

10.1.39UE Rx-Tx time difference measurements for RTT-based PDC1731

10.1.39.1Void1731

## 10.1.39.2 Measurement Accuracy Requirements for PRS1731

## 10.1.39.3 Measurement Accuracy Requirements for TRS1734

10.1.40Void1738

10.1.41FR1 DPC report1738

10.1.41.1Report mapping1738

10.1.42TDCP Measurement Report Mapping1738

10.1.43DL-RSCPD Measurements1740

10.1.43.1Introduction1740

10.1.43.2.1Measurement Accuracy Requirements1740

10.1.43.3Report Mapping1747

10.1.43.3.1Absolute DL RSCPD Measurement Reporting1747

10.1.44DL-RSCP Measurements1748

10.1.44.1Introduction1748

10.1.44.2Measurement Accuracy Requirements1748

10.1.44.3Report Mapping1756

10.1.44.3.1Relative DL RSCP Measurement Reporting1756

10.1.45CJT calibration measurements1757

10.1.45.1Introduction1757

10.1.45.2CJTC calibration delay offset report1758

10.1.45.3CJTC calibration frequency offset report1760

10.1.46CJT Calibration Report Mapping1762

10.1.46.1CJT Calibration Delay Offset Measurement Report Mapping1762

10.1.46.2CJT Calibration Frequency Offset Measurement Report Mapping1762

10.1.46.3CJT Calibration Phase Offset Measurement Report Mapping1762

10.1.47L1 CLI measurement accuracy requirements1763

10.1.47.1L1-SRS-RSRP1763

10.1.47.1.1L1-SRS-RSRP Accuracy1763

10.1.47.1.2L1-SRS-RSRP report mapping1764

10.1.47.2L1-CLI-RSSI1765

10.1.47.2.1L1-CLI-RSSI Accuracy1765

10.1.47.2.2L1-CLI-RSSI report mapping1766

## 10.1.48 RS resource prediction accuracy requirements for FR21767

## 10.1.48.1 CSI-RS based RS resource prediction accuracy requirements1767

10.1ANR measurements for RedCap1769

10.1A.1Introduction1769

10.1A.2Intra-frequency RSRP accuracy requirements for FR11769

10.1A.2.1Intra-frequency SS-RSRP accuracy requirements1769

10.1A.2.1.1Absolute SS-RSRP Accuracy1769

10.1A.2.1.2Relative SS-RSRP Accuracy1770

10.1A.3Intra-frequency RSRP accuracy requirements for FR21771

10.1A.3.1Intra-frequency SS-RSRP accuracy requirements1771

10.1A.3.1.1Absolute SS-RSRP Accuracy1771

10.1A.3.1.2Relative SS-RSRP Accuracy1771

10.1A.4Inter-frequency RSRP accuracy requirements for FR11771

10.1A.4.1Inter-frequency SS-RSRP accuracy requirements1771

10.1A.4.1.1Absolute SS-RSRP Accuracy in FR11771

10.1A.4.1.2Relative SS-RSRP Accuracy in FR11772

10.1A.5Inter-frequency RSRP accuracy requirements for FR21773

10.1A.5.1Inter-frequency SS-RSRP accuracy requirements1773

10.1A.5.1.1Absolute SS-RSRP Accuracy1773

10.1A.5.1.2Relative SS-RSRP Accuracy1773

10.1A.6Intra-frequency RSRQ accuracy requirements for FR11773

10.1A.6.1Intra-frequency SS-RSRQ accuracy requirements in FR11773

10.1A.6.1.1Absolute SS-RSRQ Accuracy in FR11773

10.1A.7Intra-frequency RSRQ accuracy requirements for FR21774

10.1A.7.1Intra-frequency SS-RSRQ accuracy requirements in FR21774

10.1A.7.1.1Absolute SS-RSRQ Accuracy in FR21774

10.1A.8Inter-frequency RSRQ accuracy requirements for FR11774

10.1A.8.1Inter-frequency SS-RSRQ accuracy requirements in FR11774

10.1A.8.1.1Absolute SS-RSRQ in FR11774

10.1A.8.1.2Relative SS-RSRQ Accuracy in FR11775

10.1A.9Inter-frequency RSRQ accuracy requirements for FR21776

10.1A.9.1Inter-frequency SS-RSRQ accuracy requirements in FR21776

10.1A.9.1.1Absolute SS-RSRQ Accuracy in FR21776

10.1A.9.1.2Relative SS-RSRQ Accuracy in FR21776

10.1A.10 Intra-frequency SINR accuracy requirements for FR11776

10.1A.10.1Intra-frequency SS-SINR accuracy requirements in FR11776

10.1A.10.1.1Absolute SS-SINR Accuracy in FR11776

10.1A.11Intra-frequency SINR accuracy requirements for FR21777

10.1A.11.1Intra-frequency SS-SINR accuracy requirements in FR21777

10.1A.11.1.1Absolute SS-SINR Accuracy in FR21777

10.1A.12 Inter-frequency SINR accuracy requirements for FR11777

10.1A.12.1Inter-frequency SS-SINR accuracy requirements in FR11777

10.1A.12.1.1Absolute SS-SINR Accuracy in FR11777

10.1A.12.1.2Relative SS-SINR Accuracy in FR11778

10.1A.13 Inter-frequency SINR accuracy requirements for FR21779

10.1A.13.1Inter-frequency SS-SINR accuracy requirements in FR21779

10.1A.13.1.1Absolute SS-SINR Accuracy in FR21779

10.1A.13.1.2Relative SS-SINR Accuracy in FR21779

10.1A.14L1-RSRP accuracy requirements for FR11779

10.1A.14.1SSB based L1-RSRP accuracy requirements1779

10.1A.14.1.1Absolute Accuracy1779

10.1A.14.1.2Relative Accuracy1780

10.1A.14.2CSI-RS based L1-RSRP accuracy requirements1781

10.1A.14.2.1Absolute Accuracy1781

10.1A.14.2.2Relative Accuracy1782

10.1A.15 L1-RSRP accuracy requirements for FR21783

10.1A.15.1SSB based L1-RSRP accuracy requirements1783

10.1A.15.1.1Absolute Accuracy1783

10.1A.15.1.2Relative Accuracy1783

10.1A.15.2CSI-RS based L1-RSRP accuracy requirements1783

10.1A.15.2.1Absolute Accuracy1783

10.1A.15.2.2Relative Accuracy1783

10.1A.16RSTD Measurements for RedCap Positioning1784

10.1A.16.1Introduction1784

10.1A.16.2Measurement Accuracy Requirements1784

10.1A.16.2.1Accuracy requirement for RSTD measurement without RX FH1784

10.1A.16.2.2Accuracy requirement for RSTD measurement with RX FH1791

10.1A.16.3Report Mapping1806

10.1A.16.3.1Absolute DL RSTD Measurement Reporting1806

10.1A.16.3.2Differential Reporting for DL RSTD Measurement1806

10.1A.16.3.3Additional Path Report Mapping for DL RSTD1806

10.1A.17PRS-RSRP Measurements for RedCap positioning1806

10.1A.17.1Introduction1806

10.1A.17.2Measurement Accuracy Requirements1806

10.1A.17.2.1Absolute PRS RSRP Accuracy Requirement1806

10.1A.17.2.2Relative PRS RSRP Accuracy Requirement1809

10.1A.17.3Report Mapping1809

10.1A.17.3.1Absolute PRS-RSRP Measurement Report Mapping1809

10.1A.17.3.2Differential Report Mapping for PRS-RSRP Measurement1809

10.1A.18  UE Rx-Tx Time Difference Measurements for RedCap Positioning1810

10.1A.18.1Introduction1810

10.1A.18.2Measurement Accuracy Requirements1810

10.1A.18.2.1UE Rx-Tx Accuracy Requirement for 2RX RedCap UE without FH1810

10.1A.18.2.2UE Rx-Tx Accuracy Requirement for 1RX RedCap UE without FH1811

10.1A.18.2.3UE Rx-Tx Accuracy Requirement for 2RX RedCap UE with FH1816

10.1A.18.3Report mapping1826

10.1A.18.3.1Absolute UE Rx-Tx Measurement Report Mapping1826

10.1A.18.3.2Differential UE Rx-Tx Measurement Report Mapping1826

10.1A.18.3.3Additional Path Report Mapping for UE Rx-Tx Time Difference1826

10.1A.19PRS-RSRPP Measurements for RedCap Positioning1826

10.1A.19.1Introduction1826

10.1A.19.2Measurement Accuracy Requirements1827

10.1A.19.2.1Absolute PRS RSRPP accuracy1827

10.1A.19.3Report mapping1829

10.1A.19.3.1Absolute PRS-RSRPP Measurement Report Mapping1829

10.1A.19.3.2Differential Report Mapping for PRS-RSRPP Measurement1830

10.2E-UTRAN measurements1830

10.2.1Introduction1830

10.2.2E-UTRAN RSRP measurements1830

10.2.3E-UTRAN RSRQ measurements1830

10.2.4E-UTRAN RSTD measurements1830

10.2.5E-UTRAN RS-SINR measurements1831

10.2.6E-UTRAN RSRP measurements for CA/DC Idle Mode Measurements1831

10.2.7E-UTRAN RSRQ measurements for CA/DC Idle Mode Measurements1831

10.2AE-UTRAN measurements for RedCap1832

10.2A.1Introduction1832

10.2A.2E-UTRAN RSRP measurements1832

10.2A.3E-UTRAN RSRQ measurements1832

10.2A.4E-UTRAN RS-SINR measurements1833

10.3UTRAN FDD Measurements1833

10.3.1UTRAN FDD CPICH RSCP1833

10.3.2UTRAN FDD CPICH Ec/No1834

10.4V2X measurements1834

10.4.1Introduction1834

10.4.2Intra-frequency PSBCH-RSRP accuracy requirements for FR11834

10.4.2.1PSBCH-RSRP Absolute Accuracy1834

10.4.2.2PSBCH-RSRP Relative Accuracy1835

10.4.2AIntra-frequency PSBCH-RSRP accuracy requirements for FR1 under CCA1836

10.4.2A.1PSBCH-RSRP Absolute Accuracy1836

10.4.2A.2PSBCH-RSRP Relative Accuracy1836

10.4.3Intra-Frequency SL-RSSI Measurement Accuracy Requirements for FR11837

10.4.3.1Absolute SL-RSSI Accuracy1837

10.4.3AIntra-Frequency SL-RSSI Measurement Accuracy Requirements for FR1 under CCA1837

10.4.3A.1Absolute SL-RSSI Accuracy1837

10.4.4Intra-Frequency L1 SL-RSRP Measurement Accuracy Requirements for FR11838

10.4.4.1Absolute L1 SL-RSRP Accuracy1838

10.4.4AIntra-Frequency L1 SL-RSRP Measurement Accuracy Requirements for FR1 under CCA1838

10.4.4A.1Absolute L1 SL-RSRP Accuracy1838

10.4.5Intra-Frequency Discovery Signal Measurement Accuracy Requirements1839

10.4.5.1Absolute Discovery Signal Measurement Accuracy1839

10.4ANR Sidelink Measurements for Positioning1840

10.4A.1Introduction1840

10.4A.2SL RSTD measurements1840

10.4A.2.1Measurement Report Mapping1840

10.4A.2.1.1Absolute SL RSTD Measurement Reporting1840

10.4A.2.2Measurement Accuracy Requirements1841

10.4A.3SL PRS-RSRP measurements1843

10.4A.3.1Measurement Report Mapping1843

10.4A.3.1.1Absolute SL PRS-RSRP Measurement Report Mapping1843

10.4A.3.2Measurement Accuracy Requirements1844

10.4A.3.2.1Absolute SL PRS-RSRP accuracy1844

10.4A.4SL Rx-Tx measurements1845

10.4A.4.1Measurement Report Mapping1845

10.4A.4.1.1Absolute SL Rx-Tx Measurement Report Mapping1845

10.4A.4.2Measurement Accuracy1847

10.4A.5SL PRS-RSRPP measurements1848

10.4A.5.1Measurement Report Mapping1848

10.4A.5.1.1Absolute SL PRS-RSRPP Measurement Report Mapping1848

10.4A.5.2Measurement Accuracy1849

10.4A.5.2.1Introduction1849

10.4A.5.2.2Measurement Accuracy Requirements1850

10.4A.5.2.2.2Absolute SL PRS-RSRPP accuracy1850

10.4A.6SL AoA measurements1851

10.4A.6.1Measurement Report Mapping1851

10.4A.6.1.1Absolute SL AoA Measurement Report Mapping1851

10.4A.7SL RTOA measurements1852

10.4A.7.1Measurement Report Mapping1852

10.4A.7.1.1Absolute SL RTOA Measurement Report Mapping1852

11Void1854

12V2X Requirements1855

12.1Introduction1855

12.2UE Transmit Timing1855

12.2.1Introduction1855

12.2.2GNSS as synchronization reference source1856

12.2.3NR Cell as synchronization reference source1856

12.2.4E-URTAN Cell as synchronization reference source1856

12.2.5SyncRef UE as synchronization reference source1857

12.3Initiation/Cease of SLSS Transmissions1857

12.3.1Introduction1857

12.3.1.1Initiation/Cease of SLSS transmissions with NR cell as synchronization reference source1857

12.3.1.2Initiation/Cease of SLSS transmissions with EUTRAN cell as synchronization reference source1858

12.3.1.3Initiation/Cease of SLSS transmissions with GNSS as synchronization reference source1859

12.3.1.4Initiation/Cease of SLSS transmissions with SyncRef UE as synchronization reference source1859

12.3AInitiation/Cease of SLSS Transmissions with CCA1860

12.3A.1Introduction1860

12.3A.1.1Initiation/Cease of SLSS transmissions with NR cell as synchronization reference source1860

12.3A.1.2Initiation/Cease of SLSS transmissions with EUTRAN cell as synchronization reference source1860

12.3A.1.3Initiation/Cease of SLSS transmissions with GNSS as synchronization reference source1860

12.3A.1.4Initiation/Cease of SLSS transmissions with SyncRef UE as synchronization reference source1861

12.4Selection / Reselection of V2X Synchronization Reference Source1861

12.4ASelection / Reselection of Sidelink Synchronization Reference Source with CCA1863

12.5L1 SL-RSRP measurements1865

12.5.1Introduction1865

12.5.2SL-RSRP measurements1865

12.6Congestion Control measurements1866

12.7Interruption1866

12.7.1Interruptions to WAN due to V2X Sidelink Communication1866

12.7.2V2X Sidelink Communication Dropping due to synchronization source change1866

12.7.3Interruptions to WAN due to switching between E-UTRA V2X Sidelink and NR V2X Sidelink1868

12.7.4Interruptions to WAN at transitions between active and non-active during SL-DRX1868

12.7.5Interruptions to V2X sidelink at transitions between active and non-active during DRX1869

12.7.6Interruptions to V2X sidelink due to Active BWP switching Requirement1869

12.7.7Interruptions to WAN due to SyncRef UE detection and/or Sensing during SL DRX off duration1870

12.7.8Interruptions at NR sidelink discovery configuration1870

12.7.9Interruptions to WAN due to sidelink carrier addition/release1870

12.8Reliability of GNSS signal1871

12.9Scheduling availability1871

12.9.1Scheduling availability of UE switching between E-UTRA sidelink and NR sidelink1871

12.9.2Scheduling availability of UE switching between Uu uplink  and V2X sidelink1871

12.10Selection / Reselection of relay UE1872

12.10.1Introduction1872

12.10.2Selection / Reselection of relay UE1872

12.11Component Carrier Addition and Release Delay for Sidelink Carrier Aggregation1872

12.12Selection / Reselection of Synchronization Reference Source for NR SL Carrier Aggregation1873

12ANR Sidelink Measurements for Positioning1874

12A.1Introduction1874

12A.2SL RSTD measurements1875

12A.2.1Introduction1875

12A.2.3Measurement Capability1875

12A.2.4Measurement Reporting Requirements1875

12A.2.5Measurements Period Requirements1875

12A.3SL PRS-RSRP measurements1876

12A.3.1Introduction1876

12A.3.2Requirements Applicability1877

12A.3.4Measurement Reporting Requirements1877

12A.3.5Measurements Period Requirements1877

12A.4SL Rx-Tx measurements1878

12A.4.1Introduction1878

12A.4.2Requirements Applicability1878

12A.4.3Measurement Capability1878

12A.4.4Measurement Reporting Requirements1878

12A.4.5Measurement Period Requirements1879

12A.5SL PRS-RSRPP measurements1880

12A.5.1Introduction1880

12A.5.2Requirements Applicability1880

12A.5.3Measurement Capability1880

12A.5.4Measurement Reporting Requirements1880

12A.5.5Measurement Period Requirements1880

12A.6SL AoA measurements1881

12A.6.1Introduction1881

12A.6.2Requirements Applicability1881

12A.6.3Measurement Capability1881

12A.6.4Measurement Reporting Requirements1881

12A.6.5Measurement Period Requirements1882

12A.7SL RTOA measurements1882

12A.7.1Introduction1882

12A.7.2Requirements Applicability1883

12A.7.3Measurement Capability1883

12A.7.4Measurement Reporting Requirements1883

12A.7.5Measurement Period Requirements1883

13Measurement Performance Requirements for NR gNB1884

13.1UL-RTOA1884

13.1.1Report mapping1884

13.1.1AAdditional Path Report Mapping for UL-RTOA1888

13.2gNB Rx-Tx time difference1891

13.2.1Report mapping1891

13.2.1AAdditional Path Report Mapping for gNB Rx-Tx1895

13.2.2Measurement Accuracy Requirements1898

13.2.2.1Introduction1898

13.2.2.2Requirements1899

13.3UL SRS RSRP measurement1900

13.3.1Report mapping1900

13.3.2Measurement accuracy requirements1900

13.3.2.1Introduction1900

13.3.2.2Requirements1901

13.4AoA/ZoA1901

13.4.1Report mapping1901

13.5Timing advance (TADV)1902

13.5.1Report mapping1902

13.6UL SRS RSRPP measurement1903

13.6.1Report mapping1903

13.7gNB Rx-Tx time difference measurements for RTT-based PDC1903

13.7.1Report mapping1903

13.7.2Measurement Accuracy Requirements1904

13.7.2.1Introduction1904

13.7.2.2Requirements1904

13.8UL-RSCP measurement1905

13.8.1Report mapping1905

13.9UL SRS-TDCT measurement1905

13.9.1Report mapping1905

13.10UL SRS-TDCP measurement1908

13.10.1Report mapping1908

Annex A (normative):Test Cases1910

A.1Purpose of annex1910

A.2Requirement classification for statistical testing1910

A.2.1Types of requirements in TS 38.1331910

A.2.1.1Time and delay requirements on UE higher layer actions1910

A.2.1.2Measurements of power levels, relative powers and time1911

A.2.1.3Implementation requirements1911

A.2.1.4Physical layer timing requirements1911

A.2.1.5Requirements under CCA1911

A.3RRM test configurations1912

A.3.1Reference measurement channels1912

A.3.1.1PDSCH1912

A.3.1.1.1FDD1912

A.3.1.1.2TDD1913

A.3.1.2CORESET for RMSI scheduling1916

A.3.1.2.1FDD1916

A.3.1.2.2TDD1917

A.3.1.3CORESET for RMC scheduling1919

A.3.1.3.1FDD1919

A.3.1.3.2TDD1921

A.3.1.4TDD UL/DL configuration1925

A.3.1AReference measurement channels under CCA1928

A.3.1A.1PDSCH1928

A.3.1A.1.1TDD1928

A.3.1A.2CORESET for RMSI scheduling1929

A.3.1A.2.1TDD1929

A.3.1A.3CORESET for RMC scheduling1930

A.3.1A.3.1TDD1930

A.3.1A.4TDD UL/DL configuration1930

A.3.1A.5RMC burst transmission model1931

A.3.2.1Generic OFDMA Channel Noise Generator (OCNG)1931

A.3.2.1.1OCNG pattern 1: Generic OCNG pattern for all unused REs1931

A.3.2.1.2OCNG pattern 2: Generic OCNG pattern for all unused REs for 2AoA setup1932

A.3.2.1.3OCNG pattern 3: Generic OCNG pattern for unused REs in the same bandwidth as CORESET1932

A.3.2.1.4OCNG pattern 4: Generic OCNG pattern for all unused REs outside SSB slot(s)1933

A.3.2.2Void1934

A.3.3Reference DRX configurations1934

A.3.3.1DRX Configuration 1: DRX cycle = 40 ms and TAT = 500 ms1934

A.3.3.2DRX Configuration 2: DRX cycle = 640 ms and TAT = 500 ms1934

A.3.3.3DRX Configuration 3: DRX cycle = 40 ms and TAT = Infinity1934

A.3.3.4DRX Configuration 4: DRX cycle = 160 ms and TAT = Infinity1935

A.3.3.5DRX Configuration 5: DRX cycle = 320 ms and TAT = Infinity1935

A.3.3.6DRX Configuration 6: DRX cycle = 320 ms and TAT = 500 ms1935

A.3.3.7DRX Configuration 7: DRX cycle = 640 ms and TAT = Infinity1935

A.3.3.8DRX Configuration 8: DRX cycle = 320 ms and TAT = Infinity1936

A.3.3.9DRX Configuration 9: DRX cycle = 40 ms and TAT = 500 ms1936

A.3.3.10DRX Configuration 10: DRX cycle = 640 ms and TAT = 500 ms1936

A.3.3.11DRX Configuration 11: DRX cycle = 20 ms and TAT = Infinity1936

A.3.3.12DRX Configuration 12: DRX cycle = 640 ms and TAT = Infinity1937

A.3.3.13DRX Configuration X1: DRX cycle = 80 ms and TAT = Infinity1937

A.3.3.14DRX Configuration 14: DRX cycle = 160 ms and TAT = Infinity1937

A.3.4Test Cases with Different Channel Bandwidths1937

A.3.4.1Test Cases with Different E-UTRA Channel Bandwidths1937

A.3.4.1.1Introduction1937

A.3.4.1.2Principle of testing1938

A.3.5Test Cases for Synchronous and Asynchronous DC Operations1938

A.3.5.1EN-DC Test Cases for Synchronous and Asynchronous EN-DC Operations1938

A.3.5.1.1Introduction1938

A.3.5.1.2Principle of Testing1938

A.3.6Antenna configurations1938

A.3.6.1Antenna configurations for FR11938

A.3.6.1.1Antenna connection for 4 Rx capable UEs1938

A.3.6.1.1.1Introduction1938

A.3.6.1.1.2Principle of testing1938

A.3.6.1.2Antenna connection for 8 Rx capable UEs1941

A.3.6.1.2.1Introduction1941

A.3.6.1.2.2Principle of testing1941

A.3.6.1.3Antenna connection for 6 Rx capable UEs1943

A.3.6.1.3.1Introduction1943

A.3.6.1.3.2Principle of testing1943

A.3.6.2Antenna configurations for FR21944

A.3.6AAntenna configurations with unlicensed bands1944

A.3.6A.1Antenna configurations for FR11944

A.3.6A.1.1Antenna connection for 4 Rx capable UEs1944

A.3.6A.1.1.1Introduction1944

A.3.6A.1.1.2Principle of testing1944

A.3.7EN-DC test setup1946

A.3.7.1Introduction1946

A.3.7.2E-UTRAN Serving Cell Parameters1946

A.3.7.2.1E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR11946

A.3.7.2.2E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR21947

A.3.7ANR FR1-FR2 test setup1948

A.3.7BEN-DC test setup with unlicensed bands1948

A.3.7B.1Introduction1948

A.3.7B.2E-UTRAN Serving Cell Parameters1948

A.3.7B.2.1E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) under CCA in FR11948

A.3.7CLTE-FR1/FR2 test setup1949

A.3.7DNE-DC test setup1950

A.3.7D.1Introduction1950

A.3.7D.2E-UTRAN Serving Cell Parameters1950

A.3.7D.2.1E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR11950

A.3.7D.2.2E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR21950

A.3.8PRACH configurations1950

A.3.8.1Introduction1950

A.3.8.2PRACH configurations in FR11950

A.3.8.2.1FR1 PRACH configuration 11950

A.3.8.2.2FR1 PRACH configuration 21951

A.3.8.2.3FR1 PRACH configuration 31951

A.3.8.2.4FR1 PRACH configuration 41952

A.3.8.2.5FR1 PRACH configuration 51952

A.3.8.2.6FR1 PRACH configuration 61953

A.3.8.3PRACH configurations in FR21953

A.3.8.3.1FR2 PRACH configuration 11953

A.3.8.3.2FR2 PRACH configuration 21954

A.3.8.3.3FR2 PRACH configuration 31955

A.3.8.3.4FR2 PRACH configuration 41955

A.3.8.3.5FR2 PRACH configuration 51956

A.3.8.3.6FR2 PRACH configuration 61956

A.3.8APRACH configurations under CCA1957

A.3.8A.1Introduction1957

A.3.8A.2PRACH configurations in FR11957

A.3.8A.2.1FR1 PRACH configuration 1 under CCA1957

A.3.8A.2.2FR1 PRACH configuration 2 under CCA1958

A.3.9BWP configurations1959

A.3.9.1Introduction1959

A.3.9.2Downlink BWP configurations1959

A.3.9.2.1Initial BWP1959

A.3.9.2.2Dedicated BWP1960

A.3.9.3Uplink BWP configurations1960

A.3.9.3.1Initial BWP1960

A.3.9.3.2Dedicated BWP1961

A.3.9ABWP configurations for RedCap1961

A.3.9A.1Introduction1961

A.3.9A.2Downlink BWP configurations1961

A.3.9A.2.1Dedicated BWP1961

A.3.9A.3Uplink BWP configurations1962

A.3.9A.3.1Dedicated BWP1962

A.3.10SSB Configurations1962

A.3.10.1SSB Configurations for FR11962

A.3.10.1.1SSB pattern 1 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz1962

A.3.10.1.5SSB pattern 5 in FR1: SSB allocation for SSB SCS=15 kHz starting from odd SFN in 10 MHz1964

A.3.10.1.6SSB pattern 6 in FR1: SSB allocation for SSB SCS=30 kHz starting from odd SFN in 40 MHz1964

A.3.10.1.7SSB pattern 7 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz1964

A.3.10.1.8SSB pattern 8 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz1965

A.3.10.1.9SSB pattern 9 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz1965

A.3.10.1.10SSB pattern 10 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz1965

A.3.10.1.11SSB pattern 11 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz1966

A.3.10.1.12SSB pattern 12 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz1966

A.3.10.1.13SSB pattern 13 in FR1: SSB allocation for SSB SCS=15 kHz in 3 MHz1966

A.3.10.1.14SSB pattern 14 in FR1: SSB allocation for SSB SCS=15 kHz with 160 ms periodicity in 10MHz1967

A.3.10.1.15SSB pattern 15 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz1967

A.3.10.1.16SSB pattern 16 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz1967

A.3.10.1.17SSB pattern 17 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz1968

A.3.10.1.18SSB pattern 18 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz1968

A.3.10.1.19SSB pattern 19 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz1968

A.3.10.1.20SSB pattern 20 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz1969

A.3.10.1.21SSB pattern 21 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz1969

A.3.10.1.23SSB pattern 23 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz1970

A.3.10.1.24SSB pattern 24 in FR1: SSB allocation for SSB SCS=30 kHz in 100 MHz1970

A.3.10.2SSB Configurations for FR21971

A.3.10.2.1SSB pattern 1 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1971

A.3.10.2.2SSB pattern 2 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1971

A.3.10.2.3SSB pattern 3 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1972

A.3.10.2.4SSB pattern 4 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1972

A.3.10.2.5SSB pattern 5 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1973

A.3.10.2.6SSB pattern 6 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1973

A.3.10.2.7SSB pattern 7 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1973

A.3.10.2.8SSB pattern 8 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1974

A.3.10.2.9SSB pattern 9 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1974

A.3.10.2.10SSB pattern 10 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1974

A.3.10.2.19SSB pattern 19 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1979

A.3.10.2.20SSB pattern 20 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1979

A.3.10.2.21SSB pattern 21 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1980

A.3.10.2.22SSB pattern 22 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1980

A.3.10.2.23SSB pattern 23 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1980

A.3.10.2.24SSB pattern 24 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1981

A.3.10.2.25SSB pattern 25 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1981

A.3.10.2.26SSB pattern 26 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1981

A.3.10.2.27SSB pattern 27 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1982

A.3.10.2.28SSB pattern 28 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1982

A.3.10.2.29SSB pattern 29 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1982

A.3.10.2.30SSB pattern 30 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1983

A.3.10.2.31SSB pattern 31 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1983

A.3.10.2.32SSB pattern 32 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1983

A.3.10.2.33SSB pattern 33 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1984

A.3.10.2.34SSB pattern 34 in FR2: SSB allocation for SSB SCS=120 kHz in 200 MHz1984

A.3.10ASSB Configurations under CCA1985

A.3.10A.1SSB Configurations under CCA for FR11985

A.3.10A.1.1SSB pattern 1 under CCA for semi-static channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz1985

A.3.10A.1.2SSB pattern 2 under CCA for dynamic channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz1985

A.3.10A.1.3SSB pattern 3 under CCA for semi-static channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz1986

A.3.10A.1.4SSB pattern 4 under CCA for dynamic channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz1986

A.3.10BSSB Configurations for RedCap1987

A.3.10B.1SSB Configurations for FR11987

A.3.10B.1.1SSB pattern 1 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz1987

A.3.10B.1.2SSB pattern 2 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz1987

A.3.10B.1.3SSB pattern 3 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz starting from odd SFN in 20 MHz1988

A.3.10B.1.4SSB pattern 4 for RedCap in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz1988

A.3.10B.1.5SSB pattern 5 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz1989

A.3.10B.1.6SSB pattern 6 for RedCap in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz1989

A.3.10B.1.7SSB pattern 7 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz1990

A.3.10B.2SSB Configurations for FR21990

A.3.10B.2.1SSB pattern 1 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1990

A.3.10B.2.2SSB pattern 2 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1991

A.3.10B.2.3SSB pattern 3 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz1991

A.3.10B.2.4SSB pattern 4 for RedCap in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1992

A.3.10B.2.5SSB pattern 5 for RedCap in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz1992

A.3.11SMTC Configurations1992

A.3.11.1SMTC pattern 1: SMTC period = 20 ms with SMTC duration = 1 ms1992

A.3.11.2SMTC pattern 2: SMTC period = 20 ms with SMTC duration = 5 ms1993

A.3.11.3SMTC pattern 3: SMTC period = 160 ms with SMTC duration = 1 ms1993

A.3.11.4SMTC pattern 4: SMTC period = 20 ms with SMTC duration = 1 ms1993

A.3.11.5SMTC pattern 5: SMTC period = 20 ms with SMTC duration = 5 ms1993

A.3.11.6SMTC pattern 6: SMTC period = 20 ms with SMTC duration = 5 ms1993

A.3.11.7SMTC pattern 7: SMTC period = 20 ms with SMTC duration = 5 ms1993

A.3.11.8SMTC pattern 8: SMTC period = 10 ms with SMTC duration = 1 ms1994

A.3.11.9SMTC pattern 9: SMTC period = 20 ms with SMTC duration = 1 ms1994

A.3.11.10SMTC pattern 10: SMTC period = 80 ms with SMTC duration = 1 ms1994

A.3.11.11SMTC pattern 11: SMTC period = 80 ms with SMTC duration = 5 ms1994

A.3.11.12SMTC pattern 12: SMTC period = 20 ms with SMTC duration = 5 ms1994

A.3.11.13SMTC pattern 13: SMTC period = 160 ms with SMTC duration = 1 ms1995

A.3.11.14SMTC pattern 14: SMTC period = 20 ms with SMTC duration = 1 ms1995

A.3.11ASMTC Configurations for RedCap1995

A.3.11A.0Introduction1995

A.3.11A.1SMTC pattern 1 for RedCap: SMTC period = 40 ms with SMTC duration = 1 ms1995

A.3.11A.2SMTC pattern 2 for RedCap: SMTC period = 80 ms with SMTC duration = 1 ms1995

A.3.11A.3SMTC pattern 3 for RedCap: SMTC period = 40 ms with SMTC duration = 1 ms1996

A.3.11A.4SMTC pattern 4 for RedCap: SMTC period = 80 ms with SMTC duration = 5 ms1996

A.3.12Test Cases with Different CC Configurations1996

A.3.12.1 EN-DC Test Cases with Different EN-DC Configurations1996

A.3.12.1.1Introduction1996

A.3.12.1.2Principle of testing1996

A.3.12.2Carrier Aggregation Test Cases with Different CA Configurations1996

A.3.12.2.1Introduction1996

A.3.12.2.2Principle of testing1997

A.3.13Test Cases in SA and EN-DC Operations1997

A.3.13.1Introduction1997

A.3.13.2Principle of Testing1997

A.3.13B Test Cases for EN-DC and NE-DC Operations1998

A.3.13B.1Active BWP switch Test Cases for EN-DC and NE-DC Operations1998

A.3.13B.1.1Introduction1998

A.3.13B.1.2Principle of Testing1998

A.3.13B.2SFTD accuracy Test Cases for EN-DC and NE-DC Operations1998

A.3.13B.2.1Introduction1998

A.3.13B.2.2Principle of Testing1998

A.3.14CSI-RS configurations1999

A.3.14.1FDD1999

A.3.14.2TDD2001

A.3.15Angle of Arrival (AoA) for FR2 RRM test cases2006

A.3.15.1Setup 1: Single AoA in Rx beam peak direction2006

A.3.15.2Setup 2: Single AoA in non Rx beam peak direction2006

A.3.15.2.1Setup 2a: Single AoA in non Rx beam peak direction without change in direction2006

A.3.15.2.2Setup 2b: Single AoA in non Rx beam peak direction with change in direction2007

A.3.15.3Setup 3: 2 AoAs2007

A.3.15.4Setup 4: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak2007

A.3.15.4.1Setup 4a: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak without change in direction2007

A.3.15.4.2Setup 4b: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak with change in direction2007

A.3.15.4.3Setup 4c: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak for power class 6 UE supporting simultaneous reception from multiple directions2007

A.3.15.5Setup 5: 2 AoAs for simultaneous reception with QCL Type-D2008

A.3.15.6Setup 6: 3 AoAs for simultaneous reception with different QCL Type-D2008

A.3.15.7Setup 7: 3 AoAs2008

A.3.15.8Setup 8: 4 AoAs2008

A.3.15CAngle of Arrival (AoA) for FR2-NTN RRM test cases2008

A.3.15C.1Setup 1: Single AoA2009

A.3.15C.2Setup 2: 2 AoAs2009

A.3.16TCI State Configuration2009

A.3.16.1Introduction2009

A.3.16.2TCI states2009

A.3.16AUnified TCI State Configuration2009

A.3.16A.1Introduction2009

A.3.16A.2DLorJoint TCI states2010

A.3.16A.3UL TCI states2011

A.3.16B LTM Candidate TCI State Configuration2011

A.3.16B.1Introduction2011

A.3.16B.2LTM candidate DLorJoint TCI states2012

A.3.16B.3LTM candidate UL TCI states2012

A.3.17Configurations of CSI-RS for tracking2013

A.3.17.1Configuration of CSI-RS for tracking for FR12013

A.3.17.1.1FDD2013

A.3.17.1.2TDD2016

A.3.17.2Configuration of CSI-RS for tracking for FR22020

A.3.17.2.1TDD2020

A.3.17.2.2FDD2023

A.3.18Additional definitions related to OTA testing for FR2 RRM test cases2023

A.3.18.1Introduction2023

A.3.18.2PRACH Power Measurement2024

A.3.19Test applicability for DAPS handover2024

A.3.19.1Introduction2024

A.3.19.2Principle of testing2024

A.3.20MsgA configurations2024

A.3.20.1Introduction2024

A.3.20.2MsgA configurations in FR12024

A.3.20.2.1FR1 MsgA configuration 12024

A.3.20.2.2FR1 MsgA configuration 22025

A.3.20.3MsgA configurations in FR22026

A.3.20.3.1FR2 MsgA configuration 12026

A.3.20.3.2FR2 MsgA configuration 22027

A.3.20AMsgA configurations under CCA2028

A.3.20A.1Introduction2028

A.3.20A.2MsgA configurations in FR12028

A.3.20A.2.1FR1 MsgA configuration 1 under CCA2028

A.3.20A.2.2FR1 MsgA configuration 2 under CCA2029

A.3.21V2X sidelink communication2030

A.3.21.1Introduction2030

A.3.21.2Reference resource pool configurations for V2X Sidelink Communication2031

A.3.21.3Reference measurement channels for V2X Sidelink Communication2034

A.3.21.4Reference SL-DRX configurations2035

A.3.21.4.1SL-DRX Configuration 1: SL-DRX cycle = 40 ms2035

A.3.21.4.2SL-DRX Configuration 2: SL-DRX cycle = 320 ms2035

A.3.21.4.3SL-DRX Configuration 3: SL-DRX cycle = 640 ms2035

A.3.21ANR Sidelink Measurements for Positioning2035

A.3.21A.1Introduction2035

A.3.21A.2NR SL-PRS configurations2036

A.3.21A.2.1NR SL-PRS configurations for FR12036

A.3.22CSI-IM configurations2036

A.3.22.1FDD2036

A.3.22.2TDD2036

A.3.23Spatial Relation Configuration2037

A.3.23.1Introduction2037

A.3.23.2Spatial Relation2038

A.3.24SRS configuration2038

A.3.25Channel bandwidth (CBW) configurations2040

A.3.25.1DL UE specific CBW2040

A.3.25.2UL UE specific CBW2041

A.3.26CCA model2041

A.3.26.1Introduction2041

A.3.26.2CCA model for operation on a carrier frequency with CCA in FR12041

A.3.26.2.1DL CCA model2041

A.3.26.2.2UL CCA model2042

A.3.26.3CCA model for operation on a carrier frequency with CCA in FR2-22043

A.3.26.3.1DL CCA model2043

A.3.26.3.2UL CCA model2043

A.3.26.4CCA model for operation on a sidelink carrier frequency with CCA2044

A.3.26.4.1CCA model for SyncRef UE2044

A.3.27Void2045

A.3.27.1Void2045

A.3.27.2Void2045

A.3.27.3Void2045

A.3.27.4Void2045

A.3.27.5Void2045

A.3.28Discovery Burst Transmission Window configuration under CCA2045

A.3.28.1DBT Window pattern 1: DBT Window period = 20 ms with DBT Window duration = 1 ms2045

A.3.29Testing principles for UE capable of only NR bands with shared spectrum access2045

A.3.29.1Introduction2045

A.3.29.2Principle of testing for UE capable of EN-DC with only NR bands with shared spectrum access2045

A.3.29.3Principle of testing for UE capable of SA operation with only NR bands with shared spectrum access2046

A.3.30CSI-RS configurations for RRM2046

A.3.30.1FDD2046

A.3.30.2TDD2047

A.3.31PRS Configurations2048

A.3.31.1PRS Configurations for FR12048

A.3.31.1.1PRS pattern 1 in FR1: SCS=15 kHz2048

A.3.31.1.2PRS pattern 2 in FR1: SCS=30 kHz2049

A.3.31.2PRS Configurations for FR22050

A.3.31.2.1PRS pattern 1 in FR2: SCS=120 kHz2050

A.3.32NR sidelink discovery2050

A.3.32.1Introduction2050

A.3.32.2Reference resource pool configurations for NR Sidelink Discovery2050

A.3.32.3Principle of Testing2051

A.3.33PRS Processing Window (PPW) configurations2051

A.3.34Testing principles for test cases related to PRS measurements2051

A.3.34.1Introduction2051

A.3.34.2Test cases in RRC_INACTIVE state2051

A.3.34.3Test cases for PRS measurements with gaps in RRC_CONNECTED state2052

A.3.34.4Test cases for PRS measurements without gaps in RRC_CONNECTED state2052

A.3.34.5Testing principles for positioning measurements by aggregating PRS resources from multiple PFLs2052

A.3.34.6Testing principles for carrier phase measurement for positioning2053

A.3.34.7Test cases in RRC_IDLE state2053

A.3.35Testing principle for RedCap UE2053

A.3.35.1Introduction2053

A.3.35.2Principle of testing for FR12053

A.3.35.3Principle of testing for FR22053

A.3.35.4Principle of testing for PRS measurement2053

A.3.36Testing related to Satellite access2054

A.3.36.1Introduction2054

A.3.36.2Principle of testing GSO and NGSO scenarios2054

A.3.36.3Principle of testing different RRM requirements2054

A.3.36.4Principle of testing different ephemeris formats2055

A.3.36.5General setup for SIB192057

A.3.36.6Satellite specific parameters configuration2058

A.3.36.6.1Satellite specific configuration for serving cell2058

A.3.36.6.2Satellite specific configuration for neighbour cell2058

A.3.37Reference Cell DTX configurations2059

A.3.37.1Cell DTX Configuration 1: Cell DTX cycle = 160 ms and TAT = Infinity2059

A.3.38DL-PRS Measurement Time Window configurations2059

A.3.39Testing related to RedCap UE with Satellite Access2059

A.3.39.1Introduction2059

A.3.39.2Principle of testing 1Rx and 2Rx (e)RedCap UE in FR12060

A.3.39.3Principle of testing GSO and NGSO scenarios2060

A.3.39.4Principle of testing different RRM requirements2060

A.3.39.5Principle of testing HD-FDD RedCap UE2061

A.3.39.6Principle of testing different ephemeris formats2061

A.3.39.7General setup for SIB192063

A.3.39.8Satellite specific parameters configuration2064

A.3.39.8.1Satellite specific configuration for serving cell2064

A.3.39.8.2Satellite specific configuration for neighbour cell2064

A.3.40Testing principles for eEMR based fast SCell activation2065

A.3.40.1Introduction2065

A.3.40.2Principle of testing2065

A.3.41Test configurations related to SBFD2065

A.3.41.1SBFD configurations for FR12065

A.3.41.1.0Introduction2065

A.3.41.1.1SBFD.1 FR12066

A.3.41.1.2SBFD.2 FR12066

A.3.41.2SBFD configurations for FR22066

A.3.41.2.0Introduction2066

A.3.41.2.1SBFD.1 FR22066

A.3.41.2.2SBFD.2 FR22067

A.3.41.3Principle of testing L1-RSRP and L1-SINR measurements2067

A.3.41.4Collision configurations between CSI-RS and UL scheduling for SBFD2067

A.3.41.5Configurations of DL RMC for SBFD2067

A.3.41.6Configurations of OCNG for SBFD2067

A.3.41.7Configuration of Noc for SBFD2067

A.3.42LP-SS configurations2068

A.3.42.1LP-SS Configuration 1: M=12068

A.3.42.2LP-SS Configuration 2: M=42068

A.3.43Test conditions for AI/ML2068

A.3.43.1Channel models for AI/ML based Beam Management FR22068

A.4EN-DC tests with all NR cells in FR12070

A.4.1Void2070

A.4.2Void2070

A.4.3RRC_CONNECTED state mobility2070

A.4.3.1Void2070

A.4.3.2RRC Connection Mobility Control2070

A.4.3.2.1Void2070

A.4.3.2.2Random Access2070

A.4.3.2.2.14-step RA type contention based random access test in FR1 for PSCell in EN-DC2070

A.4.3.2.2.24-step RA type n on-contention based random access test in FR1 for PSCell in EN-DC2073

A.4.3.2.2.32-step RA type contention based random access test in FR1 for PSCell in EN-DC2076

A.4.3.2.2.42-step RA type non-contention based random access test in FR1 for PSCell in EN-DC2078

A.4.3.2.3Void2080

A.4.3.3Handover with PSCell from EN-DC to EN-DC with known target PSCell in FR12080

A.4.3.3.1Test Purpose and Environment2080

A.4.3.3.2Test Requirements2084

A.4.4Timing2084

A.4.4.1UE transmit timing2084

A.4.4.1.1NR UE Transmit Timing Test for FR12084

A.4.4.1.1.1Test Purpose and environment2084

A.4.4.1.1.2Test requirements2087

A.4.4.1.2NR UE Transmit Timing Test for two TRPs in FR12087

A.4.4.1.2.1Test Purpose and environment2087

A.4.4.1.2.2Test requirements2090

A.4.4.1.3NR UE Transmit Timing Test with 2-TA and two TRPs for FR1 UE supporting single DCI2091

A.4.4.1.3.1Test Purpose and environment2091

A.4.4.1.3.2Test requirements2093

A.4.4.2UE timer accuracy2094

A.4.4.3Timing advance2094

A.4.4.3.1EN-DC FR1 timing advance adjustment accuracy2094

A.4.4.3.1.1Test Purpose and Environment2094

A.4.4.3.1.2Test Parameters2094

A.4.4.3.1.3Test Requirements2097

A.4.4.3.2EN-DC FR1 timing advance adjustment accuracy for asymmetric DL sTRP/UL mTRP deployment with two TAs2097

A.4.4.3.2.1Test Purpose and Environment2097

A.4.4.3.2.2Test Parameters2097

A.4.4.3.2.3Test Requirements2100

A.4.5Signaling characteristics2100

A.4.5.1Radio link Monitoring2100

A.4.5.1.1Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode2100

A.4.5.1.1.1Test Purpose and Environment2100

A.4.5.1.1.2Test Requirements2104

A.4.5.1.2Radio Link Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode2104

A.4.5.1.2.1Test Purpose and Environment2104

A.4.5.1.2.2Test Requirements2107

A.4.5.1.3Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode2107

A.4.5.1.3.1Test Purpose and Environment2107

A.4.5.1.3.2Test Requirements2110

A.4.5.1.4Radio Link Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode2110

A.4.5.1.4.1Test Purpose and Environment2110

A.4.5.1.4.2Test Requirements2113

A.4.5.1.5EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode2113

A.4.5.1.5.1Test Purpose and Environment2113

A.4.5.1.5.2Test Requirements2116

A.4.5.1.6EN-DC Radio Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode2117

A.4.5.1.6.1Test Purpose and Environment2117

A.4.5.1.6.2Test Requirements2119

A.4.5.1.7EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in DRX mode2120

A.4.5.1.7.1Test Purpose and Environment2120

A.4.5.1.7.2Test Requirements2122

A.4.5.1.8EN-DC Radio Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM in DRX mode2123

A.4.5.1.8.1Test Purpose and Environment2123

A.4.5.1.8.2Test Requirements2126

A.4.5.1.9Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS for UE fulfilling relaxed measurement criterion2126

A.4.5.1.9.1Test Purpose and Environment2126

A.4.5.1.10EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP2129

A.4.5.1.10.1Test Purpose and Environment2129

A.4.5.1.11Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP2129

A.4.5.1.11.1Test Purpose and Environment2129

A.4.5.1.11.2Test Requirements2130

A.4.5.1.12EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP2130

A.4.5.1.12.1Test Purpose and Environment2130

A.4.5.1.12.2Test Requirements2133

A.4.5.2Interruption2133

A.4.5.2.1E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in synchronous EN-DC2133

A.4.5.2.1.1Test Purpose and Environment2133

A.4.5.2.1.2Test Requirements2135

A.4.5.2.2E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC2135

A.4.5.2.2.1Test Purpose and Environment2135

A.4.5.2.2.2Test Requirements2137

A.4.5.2.3E-UTRAN – NR FR1 interruptions during measurements on deactivated NR SCC in synchronous EN-DC2137

A.4.5.2.3.1Test Purpose and Environment2137

A.4.5.2.3.2Test Requirements2141

A.4.5.2.4E-UTRAN – NR FR1 interruptions during measurements on deactivated NR SCC in asynchronous EN-DC2142

A.4.5.2.4.1Test Purpose and Environment2142

A.4.5.2.4.2Test Requirements2146

A.4.5.2.5E-UTRAN – NR FR1 interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC2146

A.4.5.2.5.1Test Purpose and Environment2146

A.4.5.2.5.2Test Requirements2148

A.4.5.2.6E-UTRAN – NR FR1 interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC2149

A.4.5.2.6.1Test Purpose and Environment2149

A.4.5.2.6.2Test Requirements2151

A.4.5.2.7Void2151

A.4.5.2.8E-UTRAN - NR FR1 interruptions at NR SRS carrier based switching in asynchronous EN-DC2151

A.4.5.2.8.1Test Purpose and Environment2151

A.4.5.2.8.2Test Requirements2154

A.4.5.2.9E-UTRAN – NR interruptions at E-UTRA SRS carrier based switching2154

A.4.5.2.9.1Test Purpose and Environment2154

A.4.5.2.9.2Test Requirements2157

A.4.5.2.10E-UTRAN – NR FR1 interruptions due to RRM and RLM/BFD measurements on deactivated NR PSCell2157

A.4.5.2.10.1Test Purpose and Environment2157

A.4.5.2.10.2Test Requirements2159

A.4.5.2.11E-UTRAN - NR FR1 interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in synchronous EN-DC2159

A.4.5.2.11.1Test Purpose and Environment2159

A.4.5.2.11.2Test Requirements2163

A.4.5.2.12E-UTRAN - NR FR1 interruptions at NR SRS antenna port switching in asynchronous EN-DC2164

A.4.5.2.12.1Test Purpose and Environment2164

A.4.5.3SCell Activation and Deactivation Delay2170

A.4.5.3.1SCell Activation and deactivation of known SCell in FR1 for 160 ms SCell measurement cycle2170

A.4.5.3.1.1Test Purpose and Environment2170

A.4.5.3.1.2Test Requirements2175

A.4.5.3.2SCell Activation and deactivation of known SCell in FR1 for 640 ms SCell measurement cycle2176

A.4.5.3.2.1Test Purpose and Environment2176

A.4.5.3.2.2Test Requirements2176

A.4.5.3.3SCell Activation and deactivation of unknown SCell in FR12176

A.4.5.3.3.1Test Purpose and Environment2176

A.4.5.3.3.2Test Requirements2177

A.4.5.3.4SCell Activation and deactivation of multiple unknown SCells in FR1 with single activation/deactivation command2177

A.4.5.3.4.1Test Purpose and Environment2177

A.4.5.3.4.2Test Requirements2179

A.4.5.3.5Direct SCell activation at SCell addition of known SCell in FR12180

A.4.5.3.5.1Test Purpose and Environment2180

A.4.5.3.5.2Test Requirements2184

A.4.5.3.6Fast SCell Activation of known SCell in FR1 for 160 ms SCell measurement cycle2184

A.4.5.3.6.1Test Purpose and Environment2184

A.4.5.3.6.2Test Requirements2188

A.4.5.3.7Fast SCell Activation of known SCell in FR1 for 640 ms SCell measurement cycle2188

A.4.5.3.7.1Test Purpose and Environment2188

A.4.5.3.7.2Test Requirements2188

A.4.5.3.8SCell Activation and deactivation of unknown SCell in FR1 for UE capable of short measurement interval2189

A.4.5.3.8.1Test Purpose and Environment2189

A.4.5.3.8.2Test Requirements2190

A.4.5.3.9SCell Activation of unknown SCell with valid L3 measurement results in FR1 for 160 ms SCell measurement cycle2190

A.4.5.3.9.1Test Purpose and Environment2190

A.4.5.3.9.2Test Requirements2195

A.4.5.3.10SCell Activation of multiple unknown SCells in FR1 with L3 reporting with single activation/deactivation command in non-DRX2196

A.4.5.3.10.1Test Purpose and Environment2196

A.4.5.3.10.2Test Requirements2198

A.4.5.3.11TRS-based SCell Activation of SSB-less SCell in FR1 collocated inter-band2199

A.4.5.3.11.1Test Purpose and Environment2199

A.4.5.3.11.2Test Requirements2202

A.4.5.3.12Inter-band SSB-less Scell activation using A-TRS2203

A.4.5.3.12.1Test Purpose and Environment2203

A.4.5.3.12.2Test Requirements2206

A.4.5.4UE UL carrier RRC reconfiguration Delay2206

A.4.5.4.1UE UL carrier RRC reconfiguration Delay2206

A.4.5.4.1.1 Test Purpose and Environment2206

A.4.5.4.1.2Test Requirements2211

A.4.5.5Beam Failure Detection and Link recovery procedures2211

A.4.5.5.1EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode2211

A.4.5.5.1.1Test Purpose and Environment2211

A.4.5.5.1.2Test Requirements2215

A.4.5.5.2EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in DRX mode2215

A.4.5.5.2.1Test Purpose and Environment2215

A.4.5.5.2.2Test Requirements2218

A.4.5.5.3EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with CSI-RS-based BFD and LR in non-DRX mode2219

A.4.5.5.3.1Test Purpose and Environment2219

A.4.5.5.3.2Test Requirements2222

A.4.5.5.4EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with CSI-RS-based BFD and LR in DRX mode2223

A.4.5.5.4.1Test Purpose and Environment2223

A.4.5.5.4.2Test Requirements2226

A.4.5.5.5EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode2227

A.4.5.5.5.1Test Purpose and Environment2227

A.4.5.5.5.2Test Requirements2230

A.4.5.5.6EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in DRX mode2231

A.4.5.5.6.1Test Purpose and Environment2231

A.4.5.5.6.2Test Requirements2234

A.4.5.5.7EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode2235

A.4.5.5.7.1Test Purpose and Environment2235

A.4.5.5.7.2Test Requirements2238

A.4.5.5.8EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode2239

A.4.5.5.8.1Test Purpose and Environment2239

A.4.5.5.8.2Test Requirements2243

A.4.5.6Active BWP switch2243

A.4.5.6.1DCI-based and Timer-based Active BWP Switch2243

A.4.5.6.1.1E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC2243

A.4.5.6.1.2E-UTRAN – NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC2247

A.4.5.6.2RRC-based Active BWP Switch2252

A.4.5.6.3Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs2255

A.4.5.6.3.1Simultaneous E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in EN-DC on multiple CCs2255

A.4.5.6.4Simultaneous RRC-based Active BWP Switch on multiple CCs2260

A.4.5.6.4.1E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC on multiple CCs2260

A.4.5.6.4.1.1Test Purpose and Environment2260

A.4.5.6.4.1.2Test Requirements2264

A.4.5.6.4.2E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR1 SCells inside active time2264

A.4.5.6.4.2.1Test Purpose and Environment2264

A.4.5.6.4.2.2Test Requirements2270

A.4.5.6.5SCell dormancy switch2270

A.4.5.6.5.1E-UTRAN – NR FR1 PSCell SCell dormancy switch of single FR1 SCell outside active time2270

A.4.5.6.5.2E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR1 SCells inside active time2275

A.4.5.6.5.2.1Test Purpose and Environment2275

A.4.5.6.5.2.2Test Requirements2279

A.4.5.7PSCell addition and release delay2279

A.4.5.7.1Addition and Release Delay of known NR PSCell2279

A.4.5.7.1.1Test purpose and environment2279

A.4.5.7.1.2Test Requirements2282

A.4.5.8DL Interruptions at switching between two uplink carriers2282

A.4.5.8.1Test Purpose and Environment2282

A.4.5.8.2Test Requirements2286

A.4.5.9UE specific CBW change2286

A.4.5.9.1UE specific CBW change on FR1 NR PSCell with non-DRX in synchronous EN- DC2286

A.4.5.9.1.1Test Purpose and Environment2286

A.4.5.9.1.2Test Requirements2289

A.4.5.10PSCell activation and deactivation delay2289

A.4.5.10.1PSCell activation and deactivation delay2289

A.4.5.10.1.1Test purpose and environment2289

A.4.5.10.1.2Test Requirements2291

A.4.5.11Conditional PSCell addition and release delay (FR1 EN-DC)2292

A.4.5.11.1Conditional PSCell Addition and Release Delay2292

A.4.5.11.1.1Test purpose and environment2292

A.4.5.11.1.2Test Parameters2292

A.4.5.11.1.3Test Requirements2294

A.4.6Measurement procedure2294

A.4.6.1Intra-frequency Measurements2294

A.4.6.1.1EN-DC event triggered reporting tests without gap under non-DRX2294

A.4.6.1.1.1Test purpose and Environment2294

A.4.6.1.1.2Test parameters2295

A.4.6.1.1.3Test Requirements2296

A.4.6.1.2EN-DC event triggered reporting tests without gap under DRX2296

A.4.6.1.2.1Test purpose and Environment2297

A.4.6.1.2.2Test parameters2297

A.4.6.1.2.3Test Requirements2299

A.4.6.1.3EN-DC event triggered reporting tests with per-UE gaps under non-DRX2299

A.4.6.1.3.1Test purpose and Environment2299

A.4.6.1.3.2Test parameters2299

A.4.6.1.3.3Test Requirements2301

A.4.6.1.4EN-DC event triggered reporting tests with per-UE gaps under DRX2301

A.4.6.1.4.1Test purpose and Environment2301

A.4.6.1.4.2Test parameters2301

A.4.6.1.4.3Test Requirements2303

A.4.6.1.5EN-DC event triggered reporting tests without gap under non-DRX with SSB index reading2304

A.4.6.1.5.1Test purpose and Environment2304

A.4.6.1.5.2Test parameters2304

A.4.6.1.5.3Test Requirements2305

A.4.6.1.6EN-DC event triggered reporting tests with SSB index reading with per-UE gaps2305

A.4.6.1.6.1Test purpose and Environment2305

A.4.6.1.6.2Test parameters2305

A.4.6.1.6.3Test Requirements2307

A.4.6.1.7EN-DC event triggered reporting tests under DRX for UE configured with highSpeedMeasFlag-r162307

A.4.6.1.7.1Test purpose and Environment2307

A.4.6.1.7.2Test parameters2307

A.4.6.1.7.3Test Requirements2309

A.4.6.1.8EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with highSpeedMeasCA-Scell-r172309

A.4.6.1.8.1Test Purpose and Environment2309

A.4.6.1.8.2Test Requirements2313

A.4.6.1.9EN-DC event triggered reporting tests without gap under non-DRX with NCD-SSB2313

A.4.6.1.9.1Test purpose and Environment2313

A.4.6.1.9.2Test parameters2313

A.4.6.1.9.3Test Requirements2315

A.4.6.1.10EN-DC event triggered reporting tests without gap under non-DRX when CD-SSB is outside active BWP2315

A.4.6.110.1Test purpose and Environment2315

A.4.6.1.10.2Test Requirements2315

A.4.6.2Inter-frequency Measurements2315

A.4.6.2.1EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is not used2316

A.4.6.2.1.1Test Purpose and Environment2316

A.4.6.2.1.2Test Requirements2318

A.4.6.2.2EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used2318

A.4.6.2.2.1Test Purpose and Environment2318

A.4.6.2.2.2Test Requirements2321

A.4.6.2.3Void2321

A.4.6.2.4Void2321

A.4.6.2.5EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is not used2321

A.4.6.2.5.1Test Purpose and Environment2321

A.4.6.2.5.2Test Requirements2324

A.4.6.2.6EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is used2324

A.4.6.2.6.1Test Purpose and Environment2324

A.4.6.2.6.2Test Requirements2326

A.4.6.2.7Void2327

A.4.6.2.8Void2327

A.4.6.2.9EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with highSpeedMeasInterFreq-r172327

A.4.6.2.9.1Test Purpose and Environment2327

A.4.6.2.9.2Test Requirements2330

A.4.6.2.10EN-DC: event triggered reporting tests under non-DRX in FR1 for UE supporting threeCarrierMeasWithoutGap-r192330

A.4.6.2.10.1Test purpose and Environment2330

A.4.6.2.10.2Test parameters2330

A.4.6.2.10.3Test Requirements2332

A.4.6.3Void2332

A.4.6.4L1-RSRP measurement for beam reporting2332

A.4.6.4.1SSB based L1-RSRP measurement when DRX is not used2332

A.4.6.4.1.1Test Purpose and Environment2332

A.4.6.4.1.2Test parameters2333

A.4.6.4.1.3Test Requirements2334

A.4.6.4.2SSB based L1-RSRP measurement when DRX is used2334

A.4.6.4.2.1Test Purpose and Environment2334

A.4.6.4.2.2Test parameters2335

A.4.6.4.2.3Test Requirements2336

A.4.6.4.3CSI-RS based L1-RSRP measurement when DRX is not used2336

A.4.6.4.3.1Test Purpose and Environment2336

A.4.6.4.3.2Test parameters2337

A.4.6.4.3.3Test Requirements2338

A.4.6.4.4CSI-RS based L1-RSRP measurement when DRX is used2338

A.4.6.4.4.1Test Purpose and Environment2338

A.4.6.4.4.2Test parameters2339

A.4.6.4.4.3Test Requirements2340

A.4.6.4.5SSB based L1-RSRP measurement when DRX is used for UE configured with highSpeedMeasFlag-r162340

A.4.6.4.5.1Test Purpose and Environment2340

A.4.6.4.5.2Test parameters2341

A.4.6.4.5.3Test Requirements2342

A.4.6.4.6CSI-RS based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP2342

A.4.6.4.6.1Test Purpose and Environment2342

A.4.6.4.7SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP2343

A.4.6.4.7.1Test Purpose and Environment2343

A.4.6.4.7.2Test Requirements2343

A.4.6.4.8SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used2343

A.4.6.4.8.1Test Purpose and Environment2343

A.4.6.4.8.2Test parameters2343

A.4.6.4.8.3Test Requirements2345

A.4.6.5CLI measurements2345

A.4.6.5.1SRS-RSRP measurement with non-DRX2345

A.4.6.5.1.1Test Purpose and Environment2345

A.4.6.5.1.2Test Parameters2345

A.4.6.5.1.3Test Requirements2348

A.4.6.5.2CLI-RSSI measurement with non-DRX2348

A.4.6.5.2.1Test Purpose and Environment2348

A.4.6.5.2.2Test Parameters2348

A.4.6.5.2.3Test Requirements2349

A.4.6.6.1.2Test Requirements2353

A.4.6.7L1-SINR measurement for beam reporting2353

A.4.6.7.2L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is used2355

A.4.6.7.2.1Test Purpose and Environment2355

A.4.6.7.2.2Test parameters2356

A.4.6.7.2.3Test Requirements2357

A.4.6.7.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is used2357

A.4.6.7.3.1Test Purpose and Environment2358

A.4.6.7.3.2Test parameters2358

A.4.6.7.3.3Test Requirements2359

A.4.6.8CSI-RS based intra-frequency Measurement2360

A.4.6.8.1EN-DC event triggered reporting tests without gap under DRX2360

A.4.6.8.1.1Test purpose and Environment2360

A.4.6.8.1.2Test Requirements2362

A.4.6.9CSI-RS based inter-frequency Measurement2362

A.4.6.9.1EN-DC event triggered reporting tests for FR1 cell when non-DRX is used2362

A.4.6.9.1.1Test Purpose and Environment2362

A.4.6.9.1.2Test Requirements2364

A.4.7Measurement Performance requirements2366

A.4.7.1SS-RSRP2366

A.4.7.1.1EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell2366

A.4.7.1.1.1Test Purpose and Environment2366

A.4.7.1.1.2Test parameters2366

A.4.7.1.1.3Test Requirements2371

A.4.7.1.2EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell2371

A.4.7.1.2.1Test Purpose and Environment2371

A.4.7.1.2.2Test parameters2371

A.4.7.1.2.3Test Requirements2374

A.4.7.1.3Void2374

A.4.7.2SS-RSRQ2374

A.4.7.2.1EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell2374

A.4.7.2.1.1Test Purpose and Environment2374

A.4.7.2.1.2Test Parameters2374

A.4.7.2.1.3Test Requirements2378

A.4.7.2.2EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell2378

A.4.7.2.2.1Test Purpose and Environment2378

A.4.7.2.2.2Test Parameters2378

A.4.7.2.2.3Test Requirements2382

A.4.7.3SS-SINR2382

A.4.7.3.1EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell2382

A.4.7.3.1.1Test Purpose and Environment2382

A.4.7.3.1.2Test Parameters2382

A.4.7.3.1.3Test Requirements2386

A.4.7.3.2EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell2386

A.4.7.3.2.1Test Purpose and Environment2386

A.4.7.3.2.2Test Parameters2386

A.4.7.3.2.3Test Requirements2389

A.4.7.4L1-RSRP measurement for beam reporting2389

A.4.7.4.1SSB based L1-RSRP measurement2389

A.4.7.4.1.1Test Purpose and Environment2389

A.4.7.4.1.2Test parameters2389

A.4.7.4.1.3Test Requirements2392

A.4.7.4.2CSI-RS based L1-RSRP measurement on resource set with repetition off2392

A.4.7.4.2.1Test Purpose and Environment2392

A.4.7.4.2.2Test parameters2393

A.4.7.4.2.3Test Requirements2396

A.4.7.5SFTD accuracy2396

A.4.7.5.1SFTD accuracy2396

A.4.7.5.1.1Test Purpose and Environment2396

A.4.7.5.1.2Test Parameters2396

A.4.7.5.1.3Test Requirements2399

A.4.7.5.2Void2399

A.4.7.5.3Void2399

A.4.7.6CLI measurements2399

A.4.7.6.1EN-DC SRS-RSRP measurement accuracy with FR1 serving cell2399

A.4.7.6.1.1Test Purpose and Environment2399

A.4.7.6.1.2Test parameters2399

A.4.7.6.1.3Test Requirements2402

A.4.7.6.2EN-DC CLI-RSSI measurement accuracy with FR1 serving cell2402

A.4.7.6.2.1Test Purpose and Environment2402

A.4.7.6.2.2Test parameters2403

A.4.7.6.2.3Test Requirements2404

A.4.7.7L1-SINR measurement for beam reporting2404

A.4.7.7.2L1-SINR measurement with SSB based CMR and dedicated IMR2408

A.4.7.7.2.1Test Purpose and Environment2408

A.4.7.7.2.2Test parameters2408

A.4.7.7.2.3Test Requirements2411

A.4.7.7.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR2411

A.4.7.7.3.1Test Purpose and Environment2411

A.4.7.7.3.2Test parameters2412

A.4.7.7.3.3Test Requirements2415

A.4.7.8CSI-RSRP2415

A.4.7.8.1EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell2415

A.4.7.8.1.1Test Purpose and Environment2415

A.4.7.8.1.2Test parameters2415

A.4.7.8.1.3Test Requirements2419

A.4.7.8.2EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell2419

A.4.7.8.2.1Test Purpose and Environment2419

A.4.7.8.2.2Test parameters2420

A.4.7.8.2.3Test Requirements2423

A.4.7.9CSI-RSRQ2423

A.4.7.9.1EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell2423

A.4.7.9.1.1Test Purpose and Environment2423

A.4.7.9.1.2Test Parameters2423

A.4.7.9.1.3Test Requirements2427

A.4.7.9.2EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell2427

A.4.7.9.2.1Test Purpose and Environment2427

A.4.7.9.2.2Test Parameters2427

A.4.7.9.2.3Test Requirements2431

A.4.7.10CSI-SINR2431

A.4.7.10.1EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell2431

A.4.7.10.1.1Test Purpose and Environment2431

A.4.7.10.1.2Test Parameters2431

A.4.7.10.1.3Test Requirements2434

A.4.7.10.2EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell2435

A.4.7.10.2.1Test Purpose and Environment2435

A.4.7.10.2.2Test Parameters2435

A.4.7.10.2.3Test Requirements2438

A.4.7.11TDCP amplitude measurement accuracy2438

A.4.7.11.1TDCP amplitude measurement accuracy in EN-DC2438

A.4.7.11.1.1Test Purpose and Environment2438

A.4.7.11.1.2Test parameters2439

A.4.7.11.1.3Test Requirements2440

A.4.8Void2440

A.4ANE-DC test with all NR cells in FR12440

A.4A.1Signaling characteristics2440

A.4A.1.1E-UTRAN PSCell addition2440

A.4A.1.1.1Test purpose and environment2440

A.4A.1.1.2Test Requirements2444

A.4A.1.2Active BWP switch2444

A.4A.1.2.1E-UTRAN PSCell – NR PCell FR1 DCI-based and Timer-based DL active BWP switch in non-DRX in synchronous NE-DC2444

A.4A.1.2.1.1Test Purpose and Environment2444

A.4A.1.2.1.2Test Requirements2447

A.4A.1.3Intra-frequency handover with E-UTRAN PSCell2448

A.4A.1.3.1Test purpose and environment2448

A.4A.1.3.2Test Requirements2452

A.4A.1.4Handover with PSCell from NE-DC to NE-DC with unknown target PSCell2452

A.4A.1.4.1Test Purpose and Environment2452

A.4A.1.4.2Test Parameters2452

A.4A.1.4.3Test Requirements2457

A.4A.1.4.3.1Test Requirements for NR HO2457

A.4A.1.4.3.2Test Requirements for LTE PSCell Change2457

A.4A.2Measurement performance2458

A.4A.2.1SFTD accuracy2458

A.4A.2.1.1SFTD accuracy2458

A.4A.2.1.1.1Test Purpose2458

A.4A.2.1.1.2Test Environment2458

A.4A.2.1.1.3Test Requirements2460

A.5EN-DC tests with one or more NR cells in FR22461

A.5.1Void2461

A.5.2Void2461

A.5.3RRC_CONNECTED state mobility2461

A.5.3.1Void2461

A.5.3.2RRC Connection Mobility Control2461

A.5.3.2.1Void2461

A.5.3.2.2Random Access2461

A.5.3.2.2.14-step RA type c ontention based random access test in FR2 for PSCell/SCell in EN-DC2461

A.5.3.2.2.24-step RA type non-contention based random access test in FR2 for PSCell/SCell in EN-DC2464

A.5.3.2.2.32-step RA type contention based random access test in FR2 for PSCell/SCell in EN-DC2467

A.5.3.2.2.42-step RA type non-contention based random access test in FR2 for PSCell/SCell in EN-DC2470

A.5.3.2.3Void2472

A.5.3.3Handover with PSCell with known FR2 target PSCell2472

A.5.3.3.1Test purpose and environment2472

A.5.3.3.2Test Requirements2475

A.5.3.3.3Void2476

A.5.3.3.4Void2476

A.5.3.3.5Void2476

A.5.3.3.6Void2476

A.5.4Timing2476

A.5.4.1UE transmit timing2476

A.5.4.1.1NR UE Transmit Timing Test for FR22476

A.5.4.1.1.1Test Purpose and environment2476

A.5.4.1.1.2Test requirements2478

A.5.4.1.2NR UE Transmit Timing Test with 2-TA for FR2 UE supporting multiDCI-IntraCellMultiTRP-TwoTA-r182479

A.5.4.1.2.1Test Purpose and environment2479

A.5.4.1.2.2Test requirements2483

A.5.4.1.3NR UE Transmit Timing Test with 2-TA for FR2 UE supporting single DCI2483

A.5.4.1.3.1Test Purpose and environment2483

A.5.4.1.3.2Test requirements2486

A.5.4.2UE timer accuracy2487

A.5.4.3Timing advance2487

A.5.4.3.1EN-DC FR2 timing advance adjustment accuracy2487

A.5.4.3.1.1Test Purpose and Environment2487

A.5.4.3.1.2Test Parameters2487

A.5.4.3.1.3Test Requirements2489

A.5.4.3.2EN-DC FR2 timing advance adjustment accuracy for asymmetric DL sTRP/UL mTRP deployment with two TAs2490

A.5.4.3.2.1Test Purpose and Environment2490

A.5.4.3.2.2Test Parameters2490

A.5.4.3.2.3Test Requirements2493

A.5.5Signaling characteristics2493

A.5.5.1Radio link Monitoring2493

A.5.5.1.1Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode2493

A.5.5.1.1.1Test Purpose and Environment2493

A.5.5.1.1.2Test Requirements2496

A.5.5.1.2Radio Link Monitoring In-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode2496

A.5.5.1.2.1Test Purpose and Environment2496

A.5.5.1.2.2Test Requirements2499

A.5.5.1.3Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode2500

A.5.5.1.3.1Test Purpose and Environment2500

A.5.5.1.3.2Test Requirements2502

A.5.5.1.4Radio Link Monitoring In-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode2502

A.5.5.1.4.1Test Purpose and Environment2502

A.5.5.1.4.2Test Requirements2505

A.5.5.1.5EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode2505

A.5.5.1.6EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode2508

A.5.5.1.7EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode2511

A.5.5.1.8EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode2514

A.5.5.1.8.2Test Requirements2518

A.5.5.1.9EN-DC Radio Link Monitoring UE Scheduling Restrictions on FR22518

A.5.5.1.9.1Test Purpose and Environment2518

A.5.5.1.9.2Test Requirements2520

A.5.5.1.10Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS for UE fulfilling relaxed measurement criterion2520

A.5.5.1.10.1Test Purpose and Environment2520

A.5.5.1.10.2Test Requirements2522

A.5.5.1.11Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode for UE supporting fast beam sweeping in multi-Rx2523

A.5.5.1.11.1Test Purpose and Environment2523

A.5.5.1.11.2Test Requirements2525

A.5.5.1.12EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP2526

A.5.5.1.12.1Test Purpose and Environment2526

A.5.5.1.13Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP2526

A.5.5.1.13.1Test Purpose and Environment2526

A.5.5.1.13.2Test Requirements2526

A.5.5.1.14EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP2526

A.5.5.1.14.1Test Purpose and Environment2526

A.5.5.1.14.2Test Requirements2529

A.5.5.2Interruption2530

A.5.5.2.1E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in synchronous EN-DC2530

A.5.5.2.1.1Test Purpose and Environment2530

A.5.5.2.1.2Test Requirements2532

A.5.5.2.2E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC2532

A.5.5.2.2.1Test Purpose and Environment2532

A.5.5.2.2.2Test Requirements2534

A.5.5.2.3E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in synchronous EN-DC2534

A.5.5.2.3.1Test Purpose and Environment2534

A.5.5.2.3.2Test Requirements2536

A.5.5.2.4E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in asynchronous EN-DC2537

A.5.5.2.4.1Test Purpose and Environment2537

A.5.5.2.4.2Test Requirements2539

A.5.5.2.5E-UTRAN – NR FR2 interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC2539

A.5.5.2.5.1Test Purpose and Environment2539

A.5.5.2.5.2Test Requirements2541

A.5.5.2.6E-UTRAN – NR FR2 interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC2542

A.5.5.2.6.1Test Purpose and Environment2542

A.5.5.2.6.2Test Requirements2543

A.5.5.2.7E-UTRAN – NR FR2 interruptions at E-UTRA SRS carrier based switching2544

A.5.5.2.7.1Test Purpose and Environment2544

A.5.5.2.7.2Test Requirements2546

A.5.5.2.8 E-UTRAN – NR FR2 interruptions at NR SRS carrier based switching2546

A.5.5.2.8.1 Test Purpose and Environment2546

A.5.5.2.8.3Test Requirements2548

A.5.5.2.9E-UTRAN – NR FR2 interruptions during measurements on deactivated NR PSCell2548

A.5.5.2.9.1Test Purpose and Environment2548

A.5.5.2.9.2Test Requirements2551

A.5.5.3SCell Activation and Deactivation Delay2551

A.5.5.3.1SCell Activation and deactivation of SCell in FR2 intra-band2551

A.5.5.3.1.1Test Purpose and Environment2551

A.5.5.3.1.2Test Requirements2552

A.5.5.3.2SCell Activation and deactivation of known SCell in FR1 for 160 ms SCell measurement cycle2553

A.5.5.3.2.1Test Purpose and Environment2553

A.5.5.3.2.2Test Requirements2555

A.5.5.3.3Void2555

A.5.5.3.4Void2555

A.5.5.3.5SCell Activation and deactivation of SCell in FR22555

A.5.5.3.5.1Test Purpose and Environment2555

A.5.5.3.5.2Test Requirements2558

A.5.5.3.6Multiple SCell Activation and deactivation of one unknown SCell and one known SCell in FR22558

A.5.5.3.6.1Test Purpose and Environment2558

A.5.5.3.6.2Test Requirements2561

A.5.5.3.7Direct SCell activation at SCell addition of known SCell in FR22561

A.5.5.3.7.1Test Purpose and Environment2561

A.5.5.3.7.2Test Requirements2564

A.5.5.3.8Fast SCell Activation of SCell in FR2 intra-band2564

A.5.5.3.8.1Test Purpose and Environment2564

A.5.5.3.8.2Test Requirements2567

A.5.5.3.9PUCCH SCell Activation and deactivation of known SCell in FR22567

A.5.5.3.9.1Test Purpose and Environment2567

A.5.5.3.9.2Test Requirements2570

A.5.5.3.10PUCCH SCell Activation and deactivation of unknown SCell in FR22570

A.5.5.3.10.1Test Purpose and Environment2570

A.5.5.3.10.2Test Requirements2573

A.5.5.3.11Multiple SCell activation and deactivation of one known PUCCH SCell and one unknown SCell in FR22573

A.5.5.3.11.1Test Purpose and Environment2573

A.5.5.3.11.2Test Requirements2576

A.5.5.3.12SCell Activation and deactivation of unknown PUCCH SCell and unknown DL SCell in FR2 in non-DRX2577

A.5.5.3.12.1Test Purpose and Environment2577

A.5.5.3.12.2Test Requirements2580

A.5.5.3.13SCell Activation and deactivation of unknown SCell in FR2 for UE in DRX, capable of small beam sweeping factors and/or short measurement interval2580

A.5.5.3.13.1Test Purpose and Environment2580

A.5.5.3.13.2Test Requirements2583

A.5.5.3.14PUCCH SCell activation and deactivation with FR1 PSCell based on L3 reporting after SCell activation command2585

A.5.5.3.14.1Test Purpose and Environment2585

A.5.5.3.14.2Test Requirements2589

A.5.5.3.15SCell Activation of unknown SCell in FR2 in non-DRX for 160 ms SCell measurement cycle with the L3 reporting during activation2590

A.5.5.3.15.1Test Purpose and Environment2590

A.5.5.3.15.2Test Requirements2594

A.5.5.4Void2595

A.5.5.5Beam Failure Detection and Link recovery procedures2595

A.5.5.5.1EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in non-DRX mode2595

A.5.5.5.1.1Test Purpose and Environment2595

A.5.5.5.1.2Test Requirements2598

A.5.5.5.2EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in DRX mode2598

A.5.5.5.2.1Test Purpose and Environment2598

A.5.5.5.2.2Test Requirements2602

A.5.5.5.3EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in non-DRX mode2602

A.5.5.5.3.1Test Purpose and Environment2602

A.5.5.5.3.2Test Requirements2605

A.5.5.5.4EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in DRX mode2606

A.5.5.5.4.1Test Purpose and Environment2606

A.5.5.5.4.2Test Requirements2609

A.5.5.5.5EN-DC scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PSCell configured with SSB-based BFD and LR in non-DRX mode2609

A.5.5.5.5.1Test Purpose and Environment2609

A.5.5.5.5.2Test Requirements2612

A.5.5.5.6EN-DC Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in non-DRX mode2612

A.5.5.5.6.1Test Purpose and Environment2612

A.5.5.5.6.2Test Requirements2616

A.5.5.5.7EN-DC Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode2616

A.5.5.5.7.1Test Purpose and Environment2616

A.5.5.5.7.2Test Requirements2619

A.5.5.5.8EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in DRX mode2620

A.5.5.5.8.1Test Purpose and Environment2620

A.5.5.5.8.2Test Requirements2623

A.5.5.5.9Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in DRX mode for UE fulfilling relaxed measurement criterion2623

A.5.5.5.9.1Test Purpose and Environment2623

A.5.5.5.9.2Test Requirements2626

A.5.5.6Active BWP switch2627

A.5.5.6.1DCI-based and Timer-based Active BWP Switch2627

A.5.5.6.1.1E-UTRAN – NR PSCell FR2 DL active BWP switch with non-DRX in synchronous EN-DC2627

A.5.5.6.1.1.1Test Purpose and Environment2627

A.5.5.6.1.1.2Test Requirements2629

A.5.5.6.1.2E-UTRAN – NR PSCell FR2 with FR2 SCell DL active BWP switch in non-DRX in synchronous EN-DC2630

A.5.5.6.2RRC-based Active BWP Switch2633

A.5.5.6.2.1E-UTRAN – NR PSCell FR2 DL active BWP switch with non-DRX in synchronous EN-DC2633

A.5.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs2636

A.5.5.6.3.1E-UTRAN – NR PSCell FR2 and NR SCell FR2 DL active BWP switch on multiple CCs in synchronous EN-DC2636

A.5.5.6.4SCell dormancy switch2639

A.5.5.6.4.1E-UTRAN – NR FR2 PSCell SCell dormancy switch of single FR2 SCell inside active time2639

A.5.5.6.4.1.1Test Purpose and Environment2639

A.5.5.6.4.1.2Test Requirements2642

A.5.5.6.4.2E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR2 SCells outside active time2643

A.5.5.6.4.2.1Test Purpose and Environment2643

A.5.5.6.4.2.2Test Requirements2647

A.5.5.6.5Simultaneous RRC-based Active BWP Switch on multiple CCs2647

A.5.5.6.5.1E-UTRAN – NR PSCell FR2  and NR SCell FR2 DL active BWP switch on multiple CCs with non-DRX in synchronous EN-DC2647

A.5.5.7PSCell addition and release delay2650

A.5.5.7.1Addition and Release Delay of NR PSCell2650

A.5.5.7.1.1Test purpose and environment2650

A.5.5.7.1.2Test Requirements2652

A.5.5.8Active TCI state switch delay2652

A.5.5.8.1MAC-CE based active TCI state switch2653

A.5.5.8.1.1E-UTRAN – NR PSCell FR2 active TCI state switch for a known TCI state2653

A.5.5.8.1.1.1Test Purpose and Environment2653

A.5.5.8.1.1.2Test Requirements2655

A.5.5.8.2RRC based active TCI state switch2656

A.5.5.8.2.1E-UTRAN – NR PSCell FR2 active TCI state switch for a known TCI state2656

A.5.5.8.2.1.1Test Purpose and Environment2656

A.5.5.8.2.1.2Test Requirements2659

A.5.5.9Uplink spatial relation switch delay2659

A.5.5.9.1MAC-CE based uplink spatial relation switch2659

A.5.5.9.1.1E-UTRAN – NR PSCell FR2 uplink spatial relation switch for a known spatial relation2659

A.5.5.9.1.1.1Test Purpose and Environment2659

A.5.5.9.1.1.2Test Requirements2661

A.5.5.9.2RRC based spatial relation switch2661

A.5.5.9.2.1E-UTRAN – NR PSCell FR2 spatial relation switch associated with a known DL-RS2661

A.5.5.9.2.1.1Test Purpose and Environment2662

A.5.5.9.2.1.2Test Requirements2663

A.5.5.10UE specific CBW change2664

A.5.5.10.1UE specific CBW change on FR2 NR PSCell2664

A.5.5.10.1.1Test Purpose and Environment2664

A.5.5.10.1.2Test Requirements2666

A.5.5.11Unified TCI state switch delay2667

A.5.5.11.1MAC-CE based active joint TCI state switch2667

A.5.5.11.1.1E-UTRAN – NR PSCell FR2 active joint TCI state switch for a known TCI state2667

A.5.5.11.1.1.1Test Purpose and Environment2667

A.5.5.11.1.1.2Test parameters2667

A.5.5.11.1.1.3Test Requirements2669

A.5.5.11.2MAC-CE based active uplink TCI state switch2669

A.5.5.11.2.1E-UTRAN – NR PSCell FR2 active uplink TCI state switch for a known TCI state2669

A.5.5.11.2.1.1Test Purpose and Environment2669

A.5.5.11.2.1.2Test parameters2670

A.5.5.11.2.1.3Test Requirements2671

A.5.5.11.3MAC-CE based active downlink TCI state switch2672

A.5.5.11.3.1E-UTRAN – NR PSCell FR2 downlink TCI state switch to cell with additional PCI for a known TCI state2672

A.5.5.11.3.1.1Test Purpose and Environment2672

A.5.5.11.3.1.2Test Parameters2672

A.5.5.11.3.1.3Test Requirements2675

A.5.5.12PSCell activation and deactivation delay2675

A.5.5.12.1PSCell activation and deactivation delay2675

A.5.5.12.1.1Test purpose and environment2675

A.5.5.12.1.2Test Requirements2677

A.5.5.13Conditional PSCell addition and release delay2678

A.5.5.13.1Addition and Release Delay of NR PSCell2678

A.5.5.13.1.1Test purpose and environment2678

A.5.5.13.1.2Test Requirements2680

A.5.6Measurement procedure2680

A.5.6.1Intra-frequency Measurements2680

A.5.6.1.1EN-DC event triggered reporting test without gap under non-DRX2680

A.5.6.1.1.1Test purpose and Environment2680

A.5.6.1.1.2Test Requirements2683

A.5.6.1.2EN-DC event triggered reporting test without gap under DRX2683

A.5.6.1.2.1Test purpose and Environment2683

A.5.6.1.2.2Test Requirements2685

A.5.6.1.3EN-DC event triggered reporting test with per-UE gaps under non-DRX2686

A.5.6.1.3.1Test purpose and Environment2686

A.5.6.1.3.2Test Requirements2688

A.5.6.1.4EN-DC event triggered reporting test with per-UE gaps under DRX2688

A.5.6.1.4.1Test purpose and Environment2688

A.5.6.1.4.2Test Requirements2690

A.5.6.1.5EN-DC event triggered reporting test without gap under non-DRX when CD-SSB is outside active BWP2691

A.5.6.1.5.1Test purpose and Environment2691

A.5.6.1.5.2Test Requirements2691

A.5.6.1.6EN-DC event triggered reporting test without gap under non-DRX2691

A.5.6.1.6.1Test purpose and Environment2691

A.5.6.1.6.2Test Requirements2693

A.5.6.1.7EN-DC event triggered reporting test without gap under non-DRX for UE configured with cssf-Config2694

A.5.6.1.7.1Test purpose and Environment2694

A.5.6.1.7.2Test Requirements2697

A.5.6.2Inter-frequency Measurements2697

A.5.6.2.1EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is not used2697

A.5.6.2.1.1Test Purpose and Environment2697

A.5.6.2.1.2Test Requirements2700

A.5.6.2.2 EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is used2700

A.5.6.2.2.1Test Purpose and Environment2700

A.5.6.2.2.2Test Requirements2702

A.5.6.2.3 EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is not used2703

A.5.6.2.3.1Test Purpose and Environment2703

A.5.6.2.3.2Test Requirements2705

A.5.6.2.4EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is used2705

A.5.6.2.4.1Test Purpose and Environment2705

A.5.6.2.4.2Test Requirements2708

A.5.6.2.5EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is not used2708

A.5.6.2.5.1Test Purpose and Environment2708

A.5.6.2.5.2Test Requirements2711

A.5.6.2.6EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is used2711

A.5.6.2.6.1Test Purpose and Environment2711

A.5.6.2.6.2Test Requirements2714

A.5.6.2.7EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is not used2715

A.5.6.2.7.1Test Purpose and Environment2715

A.5.6.2.7.2Test Requirements2717

A.5.6.2.8EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is used2718

A.5.6.2.8.1Test Purpose and Environment2718

A.5.6.2.8.2Test Requirements2721

A.5.6.2.9EN-DC event triggered reporting tests without gap under non-DRX in FR for UE supporting [FR1 only EN-DC 3-searcher capability]2721

A.5.6.2.9.1Test purpose and Environment2721

A.5.6.2.9.2Test parameters2721

A.5.6.2.9.3Test Requirements2724

A.5.6.3L1-RSRP measurement for beam reporting2724

A.5.6.3.1SSB based L1-RSRP measurement when DRX is not used2724

A.5.6.3.1.1Test Purpose and Environment2724

A.5.6.3.1.2Test parameters2724

A.5.6.3.1.3Test Requirements2726

A.5.6.3.2SSB based L1-RSRP measurement when DRX is used2726

A.5.6.3.2.1Test Purpose and Environment2726

A.5.6.3.2.2Test parameters2726

A.5.6.3.2.3Test Requirements2728

A.5.6.3.3CSI-RS based L1-RSRP measurement when DRX is not used2728

A.5.6.3.3.1Test Purpose and Environment2728

A.5.6.3.3.2Test parameters2728

A.5.6.3.3.3Test Requirements2729

A.5.6.3.4CSI-RS based L1-RSRP measurement when DRX is used2730

A.5.6.3.4.1Test Purpose and Environment2730

A.5.6.3.4.2Test parameters2730

A.5.6.3.4.3Test Requirements2731

A.5.6.3.5CSI-RS based L1-RSRP measurement when DRX is not used and when CD-SSB is outside active BWP2732

A.5.6.3.5.1Test Purpose and Environment2732

A.5.6.3.6SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP2732

A.5.6.3.6.1Test Purpose and Environment2732

A.5.6.3.6.2Test Requirements2732

A.5.6.3.7SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used2732

A.5.6.3.7.1Test Purpose and Environment2732

A.5.6.3.7.2Test parameters2733

A.5.6.3.7.3Test Requirements2734

A.5.6.4CLI measurements2734

A.5.6.4.1SRS-RSRP measurement with DRX2734

A.5.6.4.1.1Test Purpose and Environment2734

A.5.6.4.1.2Test Parameters2735

A.5.6.4.1.3Test Requirements2736

A.5.6.4.2CLI-RSSI measurement with DRX2737

A.5.6.4.2.1Test Purpose and Environment2737

A.5.6.4.2.2Test Parameters2737

A.5.6.4.2.3Test Requirements2738

A.5.6.5Measurements with autonomous gaps2738

A.5.6.5.1 EN-DC inter-frequency CGI identification of NR neighbor cell in FR22738

A.5.6.5.1.1Test Purpose and Environment2738

A.5.6.5.1.2Test Requirements2741

A.5.6.6L1-SINR measurement for beam reporting2741

A.5.6.6.2L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used2743

A.5.6.6.2.1Test Purpose and Environment2743

A.5.6.6.2.2Test parameters2743

A.5.6.6.2.3Test Requirements2745

A.5.6.6.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used2745

A.5.6.6.3.1Test Purpose and Environment2745

A.5.6.6.3.2Test parameters2746

A.5.6.6.3.3Test Requirements2747

A.5.6.7CSI-RS based Intra-frequency Measurements2747

A.5.6.7.1EN-DC event triggered reporting test without gap under non-DRX2747

A.5.6.7.1.1Test purpose and Environment2747

A.5.6.7.1.2Test Requirements2749

A.5.6.8CSI-RS based Inter-frequency Measurements2749

A.5.6.8.1 EN-DC event triggered reporting tests for NR FR2 cell when DRX is used2749

A.5.6.8.1.1Test Purpose and Environment2749

A.5.6.8.1.2Test Requirements2751

A.5.7Measurement Performance requirements2752

A.5.7.1SS-RSRP2752

A.5.7.1.1EN-DC intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell2752

A.5.7.1.1.1Test Purpose and Environment2752

A.5.7.1.1.2Test parameters2752

A.5.7.1.1.3Test Requirements2754

A.5.7.1.2EN-DC inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell2754

A.5.7.1.2.1Test Purpose and Environment2754

A.5.7.1.2.2Test parameters2755

A.5.7.1.2.3Test Requirements2757

A.5.7.1.3EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR2 target cell2758

A.5.7.1.3.1Test Purpose and Environment2758

A.5.7.1.3.2Test parameters2758

A.5.7.1.3.3Test Requirements2760

A.5.7.2SS-RSRQ2760

A.5.7.2.1EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell2760

A.5.7.2.1.1Test Purpose and Environment2760

A.5.7.2.1.2Test Parameters2761

A.5.7.2.1.3Test Requirements2762

A.5.7.2.2EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell2762

A.5.7.2.2.1Test Purpose and Environment2762

A.5.7.2.2.2Test Parameters2762

A.5.7.2.2.3Test Requirements2764

A.5.7.3SS-SINR2764

A.5.7.3.1EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell2764

A.5.7.3.1.1Test Purpose and Environment2764

A.5.7.3.1.2Test Parameters2764

A.5.7.3.1.3Test Requirements2766

A.5.7.3.2EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell2766

A.5.7.3.2.1Test Purpose and Environment2766

A.5.7.3.2.2Test Parameters2766

A.5.7.3.2.3Test Requirements2767

A.5.7.4L1-RSRP measurement for beam reporting2767

A.5.7.4.1SSB based L1-RSRP measurement2768

A.5.7.4.1.1Test Purpose and Environment2768

A.5.7.4.1.2Test parameters2768

A.5.7.4.1.3Test Requirements2769

A.5.7.4.2CSI-RS based L1-RSRP measurement on resource set with repetition off2770

A.5.7.4.2.1Test Purpose and Environment2770

A.5.7.4.2.2Test parameters2770

A.5.7.4.2.3Test Requirements2771

A.5.7.5CLI measurements2772

A.5.7.5.1EN-DC SRS-RSRP measurement accuracy with FR2 serving cell2772

A.5.7.5.1.1Test Purpose and Environment2772

A.5.7.5.1.2Test parameters2772

A.5.7.5.1.3Test Requirements2774

A.5.7.5.2EN-DC CLI-RSSI measurement accuracy with FR2 serving cell2774

A.5.7.5.2.1Test Purpose and Environment2774

A.5.7.5.2.2Test parameters2774

A.5.7.5.2.3Test Requirements2776

A.5.7.6L1-SINR measurement for beam reporting2776

A.5.7.6.2L1-SINR measurement with SSB based CMR and dedicated IMR2778

A.5.7.6.2.1Test Purpose and Environment2779

A.5.7.6.2.2Test parameters2779

A.5.7.6.2.3Test Requirements2780

A.5.7.6.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR2781

A.5.7.6.3.1Test Purpose and Environment2781

A.5.7.6.3.2Test parameters2781

A.5.7.6.3.3Test Requirements2783

A.5.7.7CSI-RSRP2783

A.5.7.7.1EN-DC intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell2783

A.5.7.7.1.1Test Purpose and Environment2783

A.5.7.7.1.2Test parameters2783

A.5.7.7.1.3Test Requirements2785

A.5.7.7.2EN-DC inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell2786

A.5.7.7.2.1Test Purpose and Environment2786

A.5.7.7.2.2Test parameters2786

A.5.7.7.2.3Test Requirements2788

A.5.7.8CSI-RSRQ2789

A.5.7.8.1EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell2789

A.5.7.8.1.1Test Purpose and Environment2789

A.5.7.8.1.2Test Parameters2789

A.5.7.8.1.3Test Requirements2791

A.5.7.8.2EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell2791

A.5.7.8.2.1Test Purpose and Environment2791

A.5.7.8.2.2Test Parameters2791

A.5.7.8.2.3Test Requirements2793

A.5.7.9CSI-SINR2793

A.5.7.9.1EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell2793

A.5.7.9.1.1Test Purpose and Environment2793

A.5.7.9.1.2Test Parameters2793

A.5.7.9.1.3Test Requirements2795

A.5.7.9.2EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell2795

A.5.7.9.2.1Test Purpose and Environment2795

A.5.7.9.2.2Test Parameters2795

A.5.7.9.2.3Test Requirements2797

A.5.8Void2797

A.6NR standalone tests with all NR cells in FR12798

A.6.1SA: RRC_IDLE state mobility2798

A.6.1.1Cell re-selection to NR2798

A.6.1.1.1Cell reselection to FR1 intra-frequency NR case2798

A.6.1.1.1.1Test Purpose and Environment2798

A.6.1.1.1.2Test Parameters2798

A.6.1.1.1.3Test Requirements2800

A.6.1.1.2Cell reselection to FR1 inter-frequency NR case2800

A.6.1.1.2.1Test Purpose and Environment2800

A.6.1.1.2.2Test Parameters2801

A.6.1.1.2.3Test Requirements2803

A.6.1.1.3Cell reselection to FR1 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion2803

A.6.1.1.3.1Test Purpose and Environment2803

A.6.1.1.3.2Test Parameters2803

A.6.1.1.3.3Test Requirements2806

A.6.1.1.4Cell reselection to FR1 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion2806

A.6.1.1.4.1Test Purpose and Environment2806

A.6.1.1.4.2Test Parameters2806

A.6.1.1.4.3Test Requirements2808

A.6.1.1.5Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion2809

A.6.1.1.5.1Test Purpose and Environment2809

A.6.1.1.5.2Test Parameters2809

A.6.1.1.5.3Test Requirements2811

A.6.1.1.6Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion2812

A.6.1.1.6.1Test Purpose and Environment2812

A.6.1.1.6.2Test Parameters2812

A.6.1.1.6.3Test Requirements2814

A.6.1.1.7Cell reselection to FR1 intra-frequency NR case for UE configured with highSpeedMeasFlag-r162815

A.6.1.1.7.1Test Purpose and Environment2815

A.6.1.1.7.2Test Parameters2815

A.6.1.1.7.3Test Requirements2818

A.6.1.1.8Cell reselection to FR1 inter-frequency NR case for UE configured with highSpeedMeasInterFreq-r172818

A.6.1.1.8.1Test Purpose and Environment2818

A.6.1.1.8.2Test Parameters2818

A.6.1.1.8.3Test Requirements2821

A.6.1.1.9Cell reselection to FR1 intra-frequency NR case for UE operating on a cell with less than 5 MHz BW2821

A.6.1.1.9.1Test Purpose and Environment2821

A.6.1.1.9.2Test Parameters2821

A.6.1.1.9.3Test Requirements2822

A.6.1.1.10Cell reselection to FR1 intra-frequency NR cell supporting OD-SIB12823

A.6.1.1.10.1Test Purpose and Environment2823

A.6.1.1.10.2Test Parameters2823

A.6.1.1.10.3Test Requirements2824

A.6.1.1.11Cell reselection to FR1 inter-frequency NR cell supporting OD-SIB12825

A.6.1.1.11.1Test Purpose and Environment2825

A.6.1.1.11.2Test Parameters2825

A.6.1.1.11.3Test Requirements2827

A.6.1.2Inter-RAT E-UTRAN cell re-selection2827

A.6.1.2.1Cell reselection to higher priority E-UTRAN2827

A.6.1.2.1.1Test Purpose and Environment2827

A.6.1.2.1.2Test Parameters2827

A.6.1.2.1.3Test Requirements2829

A.6.1.2.2Cell reselection to lower priority E-UTRAN2830

A.6.1.2.2.1Test Purpose and Environment2830

A.6.1.2.2.2Test Parameters2830

A.6.1.2.2.3Test Requirements2832

A.6.1.2.3Cell reselection to lower priority E-UTRAN for UE fulfilling low mobility relaxed measurement criterion2833

A.6.1.2.3.1Test Purpose and Environment2833

A.6.1.2.3.2Test Parameters2833

A.6.1.2.3.3Test Requirements2836

A.6.1.2.4Cell reselection to lower priority E-UTRAN for UE fulfilling not-at-cell edge relaxed measurement criterion2836

A.6.1.2.4.1Test Purpose and Environment2836

A.6.1.2.4.2Test Parameters2836

A.6.1.2.4.3Test Requirements2839

A.6.1.2.5Cell reselection to lower priority E-UTRAN cell for UE configured with highSpeedMeasFlag-r162839

A.6.1.2.5.1Test Purpose and Environment2839

A.6.1.2.5.2Test Parameters2839

A.6.1.2.5.3Test Requirements2842

A.6.1.1.7Void2842

A.6.2SA: RRC_INACTIVE state mobility2842

A.6.2.1Configured Grant based Small Data Transmissions (CG-SDT)2842

A.6.2.1.1Test purpose and Environment2842

A.6.2.1.2Test Parameters2844

A.6.2.1.3Test requirements2845

A.6.2.2Cell reselection for positioning2845

A.6.2.2.1Cell reselection to FR1 intra-frequency NR case with RRC_ INACTIVE eDRX and positioning SRS2845

A.6.2.2.1.1Test Purpose and Environment2845

A.6.2.2.1.2Test Parameters2846

A.6.2.2.1.3Test Requirements2849

A.6.3RRC_CONNECTED state mobility2849

A.6.3.1Handover2849

A.6.3.1.1Intra-frequency handover from FR1 to FR1; known target cell2849

A.6.3.1.1.1Test Purpose and Environment2849

A.6.3.1.1.2Test Parameters2849

A.6.3.1.1.3 Test Requirements2851

A.6.3.1.2Intra-frequency handover from FR1 to FR1; unknown target cell2851

A.6.3.1.2.1Test Purpose and Environment2851

A.6.3.1.2.2Test Parameters2851

A.6.3.1.2.3Test Requirements2853

A.6.3.1.3Inter-frequency handover from FR1 to FR1; unknown target cell2853

A.6.3.1.3.1Test Purpose and Environment2853

A.6.3.1.3.2Test Parameters2853

A.6.3.1.3.3Test Requirements2855

A.6.3.1.4SA NR - E-UTRAN handover2855

A.6.3.1.4.1Test Purpose and Environment2855

A.6.3.1.4.2Test Requirements2858

A.6.3.1.5SA NR - E-UTRAN handover with unknown target cell2859

A.6.3.1.5.1Test Purpose and Environment2859

A.6.3.1.5.2Test Requirements2862

A.6.3.1.6 SA NR - UTRAN FDD handover2862

A.6.3.1.6.1Test Purpose and Environment2862

A.6.3.1.6.2Test Requirements2864

A.6.3.1.7Intra-frequency synchronous DAPS handover in FR12864

A.6.3.1.7.1Test Purpose and Environment2864

A.6.3.1.7.2Test Parameters2864

A.6.3.1.7.3Test Requirements2867

A.6.3.1.8Intra-frequency asynchronous DAPS handover in FR12867

A.6.3.1.8.1Test Purpose and Environment2867

A.6.3.1.8.2Test Parameters2868

A.6.3.1.8.3Test Requirements2870

A.6.3.1.9Intra-band inter-frequency synchronous DAPS handover test in SA for FR12870

A.6.3.1.9.1Test Purpose and Environment2870

A.6.3.1.9.2Test Parameters2871

A.6.3.1.9.3Test Requirements2873

A.6.3.1.10Intra-band inter-frequency asynchronous DAPS handover test in SA for FR12873

A.6.3.1.10.1Test Purpose and Environment2873

A.6.3.1.10.2Test Parameters2873

A.6.3.1.10.3Test Requirements2875

A.6.3.1.11Inter-band inter-frequency synchronous DAPS handover from FR1 to FR12875

A.6.3.1.11.1Test Purpose and Environment2875

A.6.3.1.11.2Test Parameters2875

A.6.3.1.11.3 Test Requirements2879

A.6.3.1.12Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR12880

A.6.3.1.12.1Test Purpose and Environment2880

A.6.3.1.12.2Test Parameters2880

A.6.3.1.12.3Test Requirements2884

A.6.3.1.13SA NR - E-UTRAN with NR PSCell addition in FR12884

A.6.3.1.13.1Test Purpose and Environment2884

A.6.3.1.13.2Test Requirements2889

A.6.3.1.14SA NR - E-UTRAN handover with NR FR1 PSCell addition2889

A.6.3.1.14.1Test Purpose and Environment2889

A.6.3.1.14.2Test Requirements2895

A.6.3.1.15Intra-frequency handover from FR1 to FR1; known target cell configured with NCD-SSB2895

A.6.3.1.15.1Test Purpose and Environment2896

A.6.3.1.15.2Test Parameters2896

A.6.3.1.15.3Test Requirements2898

A.6.3.1.16Inter-frequency handover from FR1 to FR1; known target cell configured with NCD-SSB2898

A.6.3.1.16.1Test Purpose and Environment2898

A.6.3.1.16.2Test Parameters2898

A.6.3.1.16.3 Test Requirements2900

A.6.3.1.17Handover with PSCell change delay from NR-DC (FR1-FR1) to NR-DC (FR1-FR1)2900

A.6.3.1.17.1Test Purpose and Environment2901

A.6.3.1.17.2Test Requirements2904

A.6.3.1.18Intra-frequency handover from FR1 to FR1; unknown target cell operating with 12 PRB SSB bandwidth2904

A.6.3.1.18.2Test Parameters2905

A.6.3.1.18.3Test Requirements2905

A.6.3.1.19Handover with PSCell change delay where target PSCell is with 12PRB SSB bandwidth2906

A.6.3.1.19.1Test Purpose and Environment2906

A.6.3.1.19.2Test Parameters2906

A.6.3.1.19.3Test Requirements2908

A.6.3.2RRC Connection Mobility Control2909

A.6.3.2.1SA: RRC Re-establishment2909

A.6.3.2.1.1Intra-frequency RRC Re-establishment in FR12909

A.6.3.2.1.2Inter-frequency RRC Re-establishment in FR12912

A.6.3.2.1.3Intra-frequency RRC Re-establishment in FR1 without serving cell timing2914

A.6.3.2.2Random Access2917

A.6.3.2.2.14-step RA type contention based random access test in FR1 for NR standalone2917

A.6.3.2.2.24-step RA type non-contention based random access test in FR1 for NR standalone2920

A.6.3.2.2.32-step RA type contention based random access test in FR1 for NR standalone2923

A.6.3.2.2.42-step RA type non-contention based test in FR1 for NR standalone2925

A.6.3.2.3SA: RRC Connection Release with Redirection2928

A.6.3.2.3.1Redirection from NR in FR1 to NR in FR12928

A.6.3.2.3.2Redirection from NR in FR1 to E-UTRAN2930

A.6.3.2.4LTM PDCCH-order Random Access2933

A.6.3.2.4.1PDCCH-order RACH on neighbor cell in FR1 when RACH BW is within active UL BWP2933

A.6.3.2.4.2PDCCH-ordered RACH to an inter-frequency candidate cell in FR1 for LTM2937

A.6.3.2.4.3PDCCH-order RACH on neighbor cell without L1-RSRP measurement in FR1 when RACH BW is within active UL BWP2941

A.6.3.3Conditional handover2944

A.6.3.3.1Intra-frequency conditional handover from FR1 to FR12944

A.6.3.3.1.1Test Purpose and Environment2944

A.6.3.3.1.2Test Parameters2944

A.6.3.3.1.3Test Requirements2946

A.6.3.3.2Inter-frequency conditional handover from FR1 to FR12946

A.6.3.3.2.1Test Purpose and Environment2946

A.6.3.3.2.2Test Parameters2946

A.6.3.3.2.3Test Requirements2948

A.6.3.3.3NR conditional handover including target MCG and target SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC2948

A.6.3.3.3.1Test Purpose and Environment2948

A.6.3.3.3.2Test Requirements2951

A.6.3.3.4NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC2952

A.6.3.3.4.1Test Purpose and Environment2952

A.6.3.3.4.2Test Parameters2952

A.6.3.3.4.3Test Requirements2956

A.6.3.3.5NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC with complementary conditional handover configuration2956

A.6.3.3.5.1Test Purpose and Environment2956

A.6.3.3.5.2Test Parameters2956

A.6.3.3.5.3Test Requirements2960

A.6.3.3.6NES triggering intra-frequency conditional handover from FR1 to FR12960

A.6.3.3.6.1Test Purpose and Environment2960

A.6.3.3.6.2Test Parameters2960

A.6.3.3.6.3Test Requirements2962

A.6.3.3.7NES-based Inter-frequency conditional handover from FR1 to FR12962

A.6.3.3.7.1Test Purpose and Environment2962

A.6.3.3.7.2Test Parameters2962

A.6.3.3.7.3Test Requirements2964

A.6.3.4LTM PCell Switch2964

A.6.3.4.1RACH-based Intra-frequency PCell switch from FR1 to FR12964

A.6.3.4.1.1Test Purpose and Environment2964

A.6.3.4.1.2Test Parameters2964

A.6.3.4.1.3Test Requirements2967

A.6.3.4.2RACH based Inter-frequency LTM PCell switch from FR1 to FR12968

A.6.3.4.2.1Test Purpose and Environment2968

A.6.3.4.2.2Test Parameters2968

A.6.3.4.2.3Test Requirements2971

A.6.3.4.3RACH-less Intra-frequency PCell switch from FR1 to FR12972

A.6.3.4.3.1Test Purpose and Environment2972

A.6.3.4.3.2Test Parameters2972

A.6.3.4.3.3Test Requirements2976

A.6.3.4.4RACH-less Intra-frequency PCell switch from FR1 to FR1 without L1-RSRP measurement2976

A.6.3.4.4.1Test Purpose and Environment2976

A.6.3.4.4.2Test Parameters2976

A.6.3.4.4.3Test Requirements2980

A.6.3.5LTM PSCell Switch2980

A.6.3.5.1 RACH-based intra-frequency LTM PSCell switch from FR1 to FR12980

A.6.3.5.1.1Test Purpose and Environment2980

A.6.3.5.1.2Test Parameters2980

A.6.3.5.1.3Test Requirements2985

A.6.3.6CLTM PCell Switch2985

A.6.3.6.1RACH-based intra-frequency CLTM PCell switch from FR1 to FR1 triggered by SSB based L1-RSRP measurement2985

A.6.3.6.1.1Test Purpose and Environment2985

A.6.3.6.1.2Test Parameters2985

A.6.3.6.1.3Test Requirements2988

A.6.3.6.2RACH-based inter-frequency CLTM PCell switch from FR1 to FR1 triggered by SSB based L1-RSRP measurement2989

A.6.3.6.2.1Test Purpose and Environment2989

A.6.3.6.2.2Test Parameters2989

A.6.3.6.2.3Test Requirements2994

A.6.3.6.3RACH-less intra-frequency CLTM PCell switch from FR1 to FR1 triggered by SSB-based L1-RSRP measurement2994

A.6.3.6.3.1Test Purpose and Environment2994

A.6.3.6.3.2Test Parameters2994

A.6.3.6.3.3Test Requirements2998

A.6.3.6.4RACH-less intra-frequency CLTM Pcell switch from FR1 to FR1 triggered by SSB-based L3-RSRP measurement2998

A.6.3.6.4.1Test Purpose and Environment2998

A.6.3.6.4.2Test Parameters2998

A.6.3.6.4.3Test Requirements3002

A.6.4Timing3003

A.6.4.1UE transmit timing3003

A.6.4.1.1NR UE Transmit Timing Test for FR13003

A.6.4.1.1.1Test Purpose and environment3003

A.6.4.1.1.2Test requirements3005

A.6.4.1.2NR UE Transmit Timing Test for two TRPs in FR13005

A.6.4.1.2.1Test Purpose and environment3005

A.6.4.1.2.2Test requirements3008

A.6.4.1.3NR UE Transmit Timing Test with 2-TA and two TRPs for FR1 UE supporting single DCI3009

A.6.4.1.3.1Test Purpose and environment3009

A.6.4.1.3.2Test requirements3012

A.6.4.2UE timer accuracy3012

A.6.4.3Timing advance3012

A.6.4.3.1SA FR1 timing advance adjustment accuracy3012

A.6.4.3.1.1Test Purpose and Environment3012

A.6.4.3.1.2Test Parameters3012

A.6.4.3.1.3Test Requirements3015

A.6.4.3.2SA FR1 timing advance adjustment accuracy for asymmetric DL sTRP/UL mTRP deployment with two TAs3015

A.6.4.3.2.1Test Purpose and Environment3015

A.6.4.3.2.2Test Parameters3015

A.6.4.3.2.3Test Requirements3018

A.6.5Signalling characteristics3018

A.6.5.1Radio link Monitoring3018

A.6.5.1.1Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode3019

A.6.5.1.1.1Test Purpose and Environment3019

A.6.5.1.1.2Test Requirements3021

A.6.5.1.2Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode3022

A.6.5.1.2.1Test Purpose and Environment3022

A.6.5.1.2.2Test Requirements3024

A.6.5.1.3Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode3024

A.6.5.1.3.1Test Purpose and Environment3025

A.6.5.1.3.2Test Requirements3027

A.6.5.1.4Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode3027

A.6.5.1.4.1Test Purpose and Environment3027

A.6.5.1.4.2Test Requirements3030

A.6.5.1.5Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode3030

A.6.5.1.5.1Test Purpose and Environment3030

A.6.5.1.5.2Test Requirements3033

A.6.5.1.6Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode3033

A.6.5.1.6.1Test Purpose and Environment3033

A.6.5.1.6.2Test Requirements3036

A.6.5.1.7Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode3037

A.6.5.1.7.1Test Purpose and Environment3037

A.6.5.1.7.2Test Requirements3039

A.6.5.1.8Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode3040

A.6.5.1.8.1Test Purpose and Environment3040

A.6.5.1.8.2Test Requirements3043

A.6.5.1.9Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM for UE fulfilling relaxed measurement criterion3043

A.6.5.1.9.1Test Purpose and Environment3043

A.6.5.1.9.2Test Requirements3046

A.6.5.1.10Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP3046

A.6.5.1.10.1Test Purpose and Environment3046

A.6.5.1.11Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP3047

A.6.5.1.11.1Test Purpose and Environment3047

A.6.5.1.11.2Test Requirements3047

A.6.5.1.12Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP3047

A.6.5.1.12.1Test Purpose and Environment3047

A.6.5.1.12.2Test Requirements3050

A.6.5.1.13Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for UE operating on a cell with less than 5 MHz BW3050

A.6.5.1.13.1Test Purpose and Environment3050

A.6.5.1.13.2Test Requirements3051

A.6.5.1.14Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for UE operating on a cell with less than 5 MHz BW3051

A.6.5.1.14.1Test Purpose and Environment3051

A.6.5.1.14.2Test Requirements3052

A.6.5.1.15Radio Link Monitoring In-sync Test for FR1 PCell with 3 MHz Channel Bandwidth configured with SSB-based RLM RS in non-DRX mode3052

A.6.5.1.15.1Test Purpose and Environment3052

A.6.5.1.15.2Test Requirements3053

A.6.5.1.16Radio Link Monitoring In-sync Test for FR1 PCell with 3MHz Channel Bandwidth configured with SSB-based RLM RS in DRX mode3053

A.6.5.1.16.1Test Purpose and Environment3053

A.6.5.1.16.2Test Requirements3054

Test requirements specified in Clause A.6.5.1.4.2 apply to this test.A.6.5.1.17Radio Link Monitoring Out-of-sync Test for FR1 PCell with LowBandCA-Switching-r19 configured with SSB-based RLM RS in non-DRX mode3054

A.6.5.1.17.1Test Purpose and Environment3054

A.6.5.1.17.2Test Requirements3056

A.6.5.1.18Radio Link Monitoring In-sync Test for FR1 PCell with LowBandCA-Switching-r19 configured with SSB-based RLM RS in non-DRX mode3057

A.6.5.1.18.1Test Purpose and Environment3057

A.6.5.1.18.2Test Requirements3059

A.6.5.1.19Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for a UE operating with SBFD3059

A.6.5.1.19.1Test Purpose and Environment3059

A.6.5.1.19.2Test Requirements3062

A.6.5.2Interruption3062

A.6.5.2.1Interruptions during measurements on deactivated NR SCC in FR13062

A.6.5.2.1.1Test Purpose and Environment3062

A.6.5.2.1.2Test Requirements3065

A.6.5.2.1AInterruptions during measurements on deactivated NR SCC in FR1 for UE supporting intraBandNR-CA-non-collocated-r193066

A.6.5.2.1A.1Test Purpose and Environment3066

A.6.5.2.1A.2Test Requirements3070

A.6.5.2.2SA interruptions at NR SRS carrier based switching3070

A.6.5.2.2.1Test Purpose and Environment3070

A.6.5.2.2.2Test Parameters3071

A.6.5.2.2.3Test Requirements3073

A.6.5.2.3SA interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in NR-CA3073

A.6.5.2.3.1Test Purpose and Environment3073

A.6.5.2.3.2Test Parameters3073

A.6.5.2.3.3Test Requirements3075

A.6.5.2.4SA interruptions at NR SRS antenna port switching3076

A.6.5.2.4.1Test Purpose and Environment3076

A.6.5.2.4.2Test Parameters3076

A.6.5.2.4.3Test Requirements3078

A.6.5.2.5Interruptions during measurements on deactivated NR SCC in FR13079

A.6.5.2.5.1Test Purpose and Environment3079

A.6.5.2.5.2Test Requirements3081

A.6.5.3SCell Activation and Deactivation Delay3081

A.6.5.3.1SCell Activation and deactivation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle3081

A.6.5.3.1.1Test Purpose and Environment3082

A.6.5.3.1.2Test Requirements3086

A.6.5.3.2SCell Activation and deactivation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle3086

A.6.5.3.2.1Test Purpose and Environment3086

A.6.5.3.2.2Test Requirements3087

A.6.5.3.3SCell Activation and deactivation of unknown SCell in FR1 in non-DRX3087

A.6.5.3.3.1Test Purpose and Environment3087

A.6.5.3.3.2Test Requirements3088

A.6.5.3.4Direct SCell activation at SCell addition of known SCell in FR13088

A.6.5.3.4.1Test Purpose and Environment3088

A.6.5.3.4.2Test Requirements3091

A.6.5.3.5Direct SCell activation at handover with known SCell in FR13092

A.6.5.3.5.1Test Purpose and Environment3092

A.6.5.3.5.2Test Requirements3096

A.6.5.3.6PUCCH SCell Activation and deactivation of known SCell in FR13097

A.6.5.3.6.1Test Purpose and Environment3097

A.6.5.3.6.2Test Requirements3100

A.6.5.3.7SCell Activation and deactivation of unknown SCell in FR1 in non-DRX3100

A.6.5.3.7.1Test Purpose and Environment3100

A.6.5.3.7.2Test Requirements3103

A.6.5.3.8SCell Activation and Deactivation of one FR1 known PUCCH SCell and one FR1 unknown SCell with single activation/deactivation command3104

A.6.5.3.8.1Test Purpose and Environment3104

A.6.5.3.8.2Test Requirements3107

A.6.5.3.9SCell Activation and deactivation of unknown PUCCH SCell and unknown DL SCell in FR1 in non-DRX3108

A.6.5.3.9.1Test Purpose and Environment3108

A.6.5.3.9.2Test Requirements3111

A.6.5.3.10Fast SCell Activation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle3111

A.6.5.3.10.1Test Purpose and Environment3111

A.6.5.3.10.2Test Requirements3114

A.6.5.3.11SCell Activation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle3115

A.6.5.3.11.1Test Purpose and Environment3115

A.6.5.3.11.2Test Requirements3115

A.6.5.3.12SCell Activation and deactivation of unknown SCell in FR1 in DRX for UE capable of short measurement interval3115

A.6.5.3.12.1Test Purpose and Environment3115

A.6.5.3.12.2Test Requirements3118

A.6.5.3.13SCell Activation of multiple unknown SCells in FR1 with L3 reporting with single activation/deactivation commandin non-DRX3118

A.6.5.3.13.1Test Purpose and Environment3118

A.6.5.3.13.2Test Requirements3123

A.6.5.3.14SCell Activation of unknown SCell with valid L3 measurement results in FR1 in non-DRX for 160 ms SCell measurement cycle3123

A.6.5.3.14.1Test Purpose and Environment3123

A.6.5.3.14.2Test Requirements3128

A.6.5.3.15TRS based SCell Activation of SSB-less SCell in FR1 inter-band CA in non-DRX3129

A.6.5.3.15.1Test Purpose and Environment3129

A.6.5.3.15.2Test Requirements3133

A.6.5.3.16Inter-band SSB-less SCell Activation based on A-TRS3133

A.6.5.3.16.1Test Purpose and Environment3133

A.6.5.3.16.2Test Requirements3137

A.6.5.3.17.1Test Purpose and Environment3138

A.6.5.3.17.2Test Requirements3139

A.6.5.3.18OD-SSB based SCell Activation and deactivation of unknown SCell in FR1 in DRX (OD-SSB Case 1)3139

A.6.5.3.18.1Test Purpose and Environment3139

A.6.5.3.18.2Test Requirements3143

A.6.5.3.19OD-SSB based SCell Activation and deactivation of unknown SCell in FR1 DRX mode(OD-SSB Case 2, Alt Time-C1)3144

A.6.5.3.19.1Test Purpose and Environment3144

A.6.5.3.19.2Test Requirements3148

A.6.5.3.20OD-SSB based SCell Activation and deactivation of known SCell in FR1 non-DRX mode(OD-SSB Case 2, Alt Time-C1)3149

A.6.5.3.20.1Test Purpose and Environment3149

A.6.5.3.20.2Test Requirements3154

A.6.5.3.21OD-SSB based Direct SCell activation at SCell addition in FR1(OD-SSB Case 2)3154

A.6.5.3.21.1Test Purpose and Environment3154

A.6.5.3.21.2Test Requirements3158

A.6.5.3.22OD-SSB based Direct SCell activation at SCell addition in FR1 without first SSB transmission3158

A.6.5.3.22.1Test Purpose and Environment3158

A.6.5.3.22.2Test Requirements3161

A.6.5.3.23SDL SCell Activation and deactivation of unknown SCell in FR1 for LBCA3161

A.6.5.3.23.1Test Purpose and Environment3161

A.6.5.3.23.2Test Requirements3162

A.6.5.3.24Direct SCell activation at SCell addition of known SCell in FR1 for LBCA3162

A.6.5.3.24.1Test Purpose and Environment3162

A.6.5.3.24.2Test Requirements3163

A.6.5.3.25PUCCH SCell Activation and deactivation for UE supporting EMR in FR13164

A.6.5.3.25.1Test Purpose and Environment3164

A.6.5.3.25.2Test Requirements3167

A.6.5.3.26EMR based SCell activation of unknown SCell in FR13167

A.6.5.3.26.1Test Purpose and Environment3167

A.6.5.3.26.2Test Requirements3172

A.6.5.3.27EMR based Direct SCell activation at SCell addition of unknown SCell in FR13172

A.6.5.3.27.1Test Purpose and Environment3172

A.6.5.3.27.2Test Requirements3176

A.6.5.4UE UL carrier RRC reconfiguration Delay3176

A.6.5.4.1UE UL carrier RRC reconfiguration Delay3176

A.6.5.4.1.1Test Purpose and Environment3176

A.6.5.4.1.2Test Requirements3179

A.6.5.4.2Void3179

A.6.5.5Beam Failure Detection and Link recovery procedures3179

A.6.5.5.1Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode3179

A.6.5.5.1.1Test Purpose and Environment3179

A.6.5.5.1.2Test Requirements3183

A.6.5.5.2Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode3183

A.6.5.5.2.1Test Purpose and Environment3183

A.6.5.5.2.2Test Requirements3187

A.6.5.5.3Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode3187

A.6.5.5.3.1Test Purpose and Environment3187

A.6.5.5.3.2Test Requirements3190

A.6.5.5.4Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode3191

A.6.5.5.4.1Test Purpose and Environment3191

A.6.5.5.4.2Test Requirements3195

A.6.5.5.5Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode3195

A.6.5.5.5.1Test Purpose and Environment3195

A.6.5.5.5.2Test Requirements3198

A.6.5.5.6Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in DRX mode3199

A.6.5.5.6.1Test Purpose and Environment3199

A.6.5.5.6.2Test Requirements3202

A.6.5.5.7TRP Specific Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode3203

A.6.5.5.7.1Test Purpose and Environment3203

A.6.5.5.7.2Test Requirements3206

A.6.5.5.8Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for a UE operating on a cell with less than 5 MHz BW3207

A.6.5.5.8.1Test Purpose and Environment3207

A.6.5.5.8.2Test Requirements3208

A.6.5.5.9Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode for a UE operating with SBFD3208

A.6.5.5.9.1Test Purpose and Environment3208

A.6.5.5.9.2Test Requirements3209

A.6.5.6Active BWP switch3209

A.6.5.6.1DCI-based and Timer-based Active BWP Switch3209

A.6.5.6.1.1NR FR1- NR FR1 DL active BWP switch of SCell with non-DRX in SA3209

A.6.5.6.1.2NR FR1 DL active BWP switch with non-DRX in SA3214

A.6.5.6.2RRC-based Active BWP Switch3217

A.6.5.6.2.1NR FR1 DL active BWP switch of Cell with non-DRX in SA3217

A.6.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs3219

A.6.5.6.3.1NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA3219

A.6.5.6.4SCell dormancy switch3225

A.6.5.6.4.1NR FR1 PCell SCell dormancy switch of single FR1 SCell outside active time3225

A.6.5.6.4.1.1Test Purpose and Environment3225

A.6.5.6.4.1.2Test Requirements3229

A.6.5.6.4.2NR FR1 PCell SCell dormancy switch of two FR1 SCells inside active time3230

A.6.5.6.4.2.1 Test Purpose and Environment3230

A.6.5.6.4.2.2Test Requirements3235

A.6.5.6.5Simultaneous RRC-based Active BWP Switch on multiple CCs3235

A.6.5.6.5.1NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA3235

A.6.5.7DL interruptions at switching between two uplink carriers3239

A.6.5.7.1DL interruptions at switching between two uplink carriers in FDD-TDD CA3239

A.6.5.7.1.1Test Purpose and Environment3239

A.6.5.7.1.2Test Requirements3243

A.6.5.7.2DL interruptions at switching between two uplink carriers in TDD-TDD CA3243

A.6.5.7.2.1Test Purpose and Environment3243

A.6.5.7.2.2Test Requirements3246

A.6.5.7ADL interruptions at switching between two uplink carriers with two transmit antenna connectors3246

A.6.5.7A.1DL interruptions at switching between two uplink carriers in FDD-TDD CA3246

A.6.5.7A.1.1Test Purpose and Environment3246

A.6.5.7A.1.2Test Requirements3250

A.6.5.7A.2DL interruptions at switching between two uplink carriers in TDD-TDD CA3250

A.6.5.7A.2.1Test Purpose and Environment3250

A.6.5.7A.2.2Test Requirements3252

A.6.5.7BDL interruptions at switching between one uplink band with one transmit antenna connector and one uplink band with two transmit antenna connectors3253

A.6.5.7B.1DL interruptions at switching between two uplink bands in FDD-TDD CA3253

A.6.5.7B.1.1Test Purpose and Environment3253

A.6.5.7B.1.2Test Requirements3257

A.6.5.7B.2DL interruptions at switching between two uplink bands in TDD-TDD CA3257

A.6.5.7B.2.1Test Purpose and Environment3257

A.6.5.7B.2.2Test Requirements3262

A.6.5.7CDL interruptions at switching between two uplink bands with two transmit antenna connectors3262

A.6.5.7C.1DL interruptions at switching between two uplink bands with two transmit antenna connectors in FDD-TDD CA3262

A.6.5.7C.1.1Test Purpose and Environment3262

A.6.5.7C.1.2Test Requirements3268

A.6.5.7C.2DL interruptions at switching between two uplink bands with two transmit antenna connectors in TDD-TDD CA3268

A.6.5.7C.2.1Test Purpose and Environment3268

A.6.5.7C.2.2Test Requirements3273

A.6.5.7DDL interruptions at UE switching across three or four uplink bands3273

A.6.5.7D.1DL interruptions at switching across three uplink bands in TDD-TDD CA for single TAG3273

A.6.5.7D.1.1Test Purpose and Environment3273

A.6.5.7D.1.2Test Requirements3277

A.6.5.7D.2DL interruptions at switching across four uplink bands in FDD-TDD CA for single TAG3277

A.6.5.7D.2.1Test Purpose and Environment3277

A.6.5.7D.2.2Test Requirements3281

A.6.5.7D.3DL interruptions at switching across three uplink bands in FDD-TDD CA for two TAGs3281

A.6.5.7D.3.1Test Purpose and Environment3281

A.6.5.7D.3.2Test Requirements3285

A.6.5.7D.4DL interruptions at switching across four uplink bands in TDD-TDD CA for two TAGs3285

A.6.5.7D.4.1Test Purpose and Environment3285

A.6.5.7D.7.2Test Requirements3290

A.6.5.8UE specific CBW change3290

A.6.5.8.1UE specific CBW change on PCell in FR1 in non-DRX3290

A.6.5.8.1.1Test Purpose and Environment3290

A.6.5.8.1.2Test Requirements3292

A.6.5.9Pathloss reference signal switching delay3292

A.6.5.9.1MAC-CE based pathloss reference signal switch delay3292

A.6.5.9.1.1Test Purpose and Environment3292

A.6.5.9.1.2Test Requirements3295

A.6.5.9.2MAC-CE based pathloss reference signal switch delay  for LB CA3295

A.6.5.9.2.1Test Purpose and Environment3295

A.6.5.9.2.2Test Requirements3296

A.6.5.10Conditional PSCell addition and release delay (FR1 NR-DC)3296

A.6.5.10.1Conditional PSCell Addition and Release Delay3296

A.6.5.10.1.1Test purpose and environment3296

A.6.5.10.1.2Test Parameters3296

A.6.5.10.1.3Test Requirements3299

A.6.5.11PSCell addition and release delay3299

A.6.5.11.1Addition and Release Delay of unknown NR FR1 PSCell3299

A.6.5.11.1.1Test purpose and environment3299

A.6.5.11.1.2Test Requirements3301

A.6.5.11.2Addition and Release Delay of unknown NR FR1 PSCell with less than 5 MHz3302

A.6.5.11.2.1Test purpose and environment3302

A.6.5.11.2.2Test Requirements3302

A.6.5.12Subsequent conditional PSCell addition/change3303

A.6.5.12.1Intra-frequency subsequent CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC3303

A.6.5.12.1.1Test purpose and environment3303

A.6.5.12.1.2Test Parameters3303

A.6.5.12.1.3Test Requirements3305

A.6.5.12.2Inter-frequency subsequent CPA from FR1-FR1 NR-DC to FR1-FR1 NR-DC3306

A.6.5.12.2.1Test purpose and environment3306

A.6.5.12.2.2Test Parameters3306

A.6.5.12.2.3Test Requirements3309

A.6.5.12.3Intra-frequency subsequent CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC with 12 PRB SSB bandwidth3309

A.6.5.12.3.1Test purpose and environment3309

A.6.5.12.3.2Test Parameters3309

A.6.5.12.3.3Test Requirements3310

A.6.5.12.4Inter-frequency subsequent CPA from FR1-FR1 NR-DC to FR1-FR1 NR-DC with 12 PRB SSB bandwidth3310

A.6.5.12.4.1Test purpose and environment3310

A.6.5.12.4.2Test Parameters3310

A.6.5.12.4.3Test Requirements3311

A.6.5.13Active TCI state switch delay3311

A.6.5.13.1MAC-CE based joint TCI state switch for mDCI with two TA when RTD is larger than CP3312

A.6.5.13.1.1Test Purpose and Environment3312

A.6.5.13.1.2Test Requirements3314

A.6.6Measurement procedure3315

A.6.6.1Intra-frequency Measurements3315

A.6.6.1.1SA event triggered reporting tests without gap under non-DRX3315

A.6.6.1.1.1Test purpose and Environment3315

A.6.6.1.1.2Test parameters3315

A.6.6.1.1.3Test Requirements3317

A.6.6.1.2SA event triggered reporting tests without gap under DRX3317

A.6.6.1.2.1Test purpose and Environment3317

A.6.6.1.2.2Test parameters3317

A.6.6.1.2.3Test Requirements3319

A.6.6.1.3SA event triggered reporting tests with per-UE gaps under non-DRX3319

A.6.6.1.3.1Test purpose and Environment3319

A.6.6.1.3.2Test parameters3319

A.6.6.1.3.3Test Requirements3321

A.6.6.1.4SA event triggered reporting tests with per-UE gaps under DRX3321

A.6.6.1.4.1Test purpose and Environment3321

A.6.6.1.4.2Test parameters3322

A.6.6.1.4.3Test Requirements3324

A.6.6.1.5SA event triggered reporting tests without gap under non-DRX with SSB index reading3324

A.6.6.1.5.1Test purpose and Environment3324

A.6.6.1.5.2Test parameters3324

A.6.6.1.5.3Test Requirements3325

A.6.6.1.6SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading3325

A.6.6.1.6.1Test purpose and Environment3325

A.6.6.1.6.2Test parameters3326

A.6.6.1.6.3Test Requirements3327

A.6.6.1.7SA event triggered reporting tests under DRX for UE configured with highSpeedMeasFlag-r163327

A.6.6.1.7.1Test purpose and Environment3327

A.6.6.1.7.2Test parameters3327

A.6.6.1.7.3Test Requirements3329

A.6.6.1.8SA event triggered reporting tests without gap under DRX for UE configured with highSpeedMeasCA-Scell-r173330

A.6.6.1.8.1Test purpose and Environment3330

A.6.6.1.8.2Test parameters3330

A.6.6.1.8.3Test Requirements3332

A.6.6.1.9SA event triggered reporting tests with MUSIM gap configured3332

A.6.6.1.9.1Test purpose and Environment3332

A.6.6.1.9.2Test parameters3332

A.6.6.1.9.3Test requirements3334

A.6.6.1.10SA event triggered reporting tests without gap under non-DRX when CD-SSB is outside active BWP3334

A.6.6.1.10.1Test purpose and Environment3334

A.6.6.1.10.2Test Requirements3335

A.6.6.1.11SA event triggered reporting tests without gap under non-DRX with NCD-SSB3335

A.6.6.1.11.1Test purpose and Environment3335

A.6.6.1.11.2Test parameters3335

A.6.6.1.11.3Test Requirements3336

A.6.6.1.12SA event triggered reporting tests without gap under non-DRX with SSB index reading and 12 PRB SSB3337

A.6.6.1.12.1Test purpose and Environment3337

A.6.6.1.12.2Test parameters3337

A.6.6.1.12.3Test Requirements3337

A.6.6.1.13SA event triggered reporting tests without gap under Cell DTX3337

A.6.6.1.13.1Test purpose and Environment3338

A.6.6.1.13.2Test parameters3338

A.6.6.1.13.3Test Requirements3339

A.6.6.1.14Deactivated PSCell measurement test with 12 PRB SSB bandwidth in FR13340

A.6.6.1.14.1Test Purpose and Environment3340

A.6.6.1.14.2Test Parameters3340

A.6.6.1.14.3Test Requirements3343

A.6.6.1.15SA event triggered reporting test without gap under non-DRX with SSB index reading and 12 PRB SSB for a deactivated SCell3343

A.6.6.1.15.1Test purpose and Environment3343

A.6.6.1.15.2Test parameters3343

A.6.6.1.15.3Test requirements3345

A.6.6.1.16OD-SSB based deactivated SCell measurement under non-DRX mode in FR1 (OD-SSB Case 1)3345

A.6.6.1.16.1Test Purpose and Environment3345

A.6.6.1.16.2Test Requirements3351

A.6.6.1.17SA event triggered reporting test without gap under non-DRX on deactivated SCell based on OD-SSB3352

A.6.6.1.17.1Test purpose and Environment3352

A.6.6.1.17.2Test Requirements3354

A.6.6.1.18SA event triggered reporting tests without gap under non-DRX based on OD-SSB3355

A.6.6.1.18.1Test purpose and Environment3355

A.6.6.1.18.2Test parameters3355

A.6.6.1.18.3Test Requirements3357

A.6.6.1.19SA event triggered reporting test for a UE configured with LB CA via switching3357

A.6.6.1.19.1Test purpose and Environment3357

A.6.6.1.19.2Test parameters3357

A.6.6.1.19.3Test requirements3360

A.6.6.1.20SA event triggered reporting tests without gap under non-DRX in FR1 for UE supporting [FR1 only CA and FR1 only NR-DC 3-searcher capability]3360

A.6.6.1.20.1Test purpose and Environment3360

A.6.6.1.20.2Test parameters3361

A.6.6.1.20.3Test Requirements3365

A.6.6.2Inter-frequency Measurements3365

A.6.6.2.1SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used3365

A.6.6.2.1.1Test Purpose and Environment3365

A.6.6.2.1.2Test Requirements3368

A.6.6.2.2SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used3368

A.6.6.2.2.1Test Purpose and Environment3368

A.6.6.2.2.2Test Requirements3371

A.6.6.2.3Void3371

A.6.6.2.4Void3371

A.6.6.2.5SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used3371

A.6.6.2.5.1Test Purpose and Environment3371

A.6.6.2.5.2Test Requirements3373

A.6.6.2.6SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used3373

A.6.6.2.6.1Test Purpose and Environment3374

A.6.6.2.6.2Test Requirements3376

A.6.6.2.7Void3376

A.6.6.2.8Void3376

A.6.6.2.9SA event triggered reporting tests with additional mandatory gap pattern3376

A.6.6.2.9.1Test Purpose and Environment3376

A.6.6.2.9.2Test Requirements3378

A.6.6.2.10SA event triggered reporting tests for FR1 when DRX is used3379

A.6.6.2.10.1Test Purpose and Environment3379

A.6.6.2.10.2Test Requirements3381

A.6.6.2.12SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for UE configured with highSpeedMeasInterFreq-r173384

A.6.6.2.12.1Test Purpose and Environment3384

A.6.6.2.12.2Test Requirements3386

A.6.6.2.13SA event triggered reporting tests for FR1 with measurement gap with priority and periodic MUSIM gap configured3387

A.6.6.2.13.1Test Purpose and Environment3387

A.6.6.2.13.2Test Requirements3389

A.6.6.2.14SA event triggered reporting tests for FR1 with measurement gap without priority and periodic MUSIM gap configured3389

A.6.6.2.14.1Test Purpose and Environment3389

A.6.6.2.14.2Test Requirements3392

A.6.6.2.15SA event triggered reporting tests for FR1 with 3 MHz Channel Bandwidth configured with SSB time index detection when DRX is used3392

A.6.6.2.15.1Test Purpose and Environment3392

A.6.6.2.15.2Test Requirements3393

A.6.6.2.16SA event triggered reporting tests with SSB adaptation without SSB time index detection without gap under non-DRX3393

A.6.6.2.16.1Test purpose and Environment3393

A.6.6.2.16.2Test parameters3393

A.6.6.2.16.3Test Requirements3395

A.6.6.2.17SA event triggered reporting tests under non-DRX3395

A.6.6.2.17.1Test purpose and Environment3395

A.6.6.2.17.2Test parameters3396

A.6.6.2.17.3Test Requirements3398

A.6.6.2.18SA event-triggered reporting tests for FR1 without SSB time index detection when DRX is not used for UE configured with measurement gap cancellation3398

A.6.6.2.18.1Test Purpose and Environment3398

A.6.6.2.18.2Test Requirements3399

A.6.6.3Inter-RAT Measurements3399

A.6.6.3.1SA NR - E-UTRAN event-triggered reporting in non-DRX in FR13399

A.6.6.3.1.1Test Purpose and Environment3399

A.6.6.3.1.2Test Requirements3402

A.6.6.3.2SA NR - E-UTRAN event-triggered reporting in DRX in FR13402

A.6.6.3.2.1Test Purpose and Environment3402

A.6.6.3.2.2Test Requirements3405

A.6.6.3.3SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for UE configured with highSpeedMeasFlag-r163406

A.6.6.3.3.1Test Purpose and Environment3406

A.6.6.3.3.2Test Requirements3409

A.6.6.4L1-RSRP measurement for beam reporting3409

A.6.6.4.1SSB based L1-RSRP measurement when DRX is not used3409

A.6.6.4.1.1Test Purpose and Environment3409

A.6.6.4.1.2Test parameters3409

A.6.6.4.1.3Test Requirements3411

A.6.6.4.2SSB based L1-RSRP measurement when DRX is used3411

A.6.6.4.2.1Test Purpose and Environment3411

A.6.6.4.2.2Test parameters3411

A.6.6.4.2.3Test Requirements3413

A.6.6.4.3CSI-RS based L1-RSRP measurement when DRX is not used3413

A.6.6.4.3.1Test Purpose and Environment3413

A.6.6.4.3.2Test parameters3413

A.6.6.4.3.3Test Requirements3415

A.6.6.4.4CSI-RS based L1-RSRP measurement when DRX is used3415

A.6.6.4.4.1Test Purpose and Environment3415

A.6.6.4.4.2Test parameters3415

A.6.6.4.4.3Test Requirements3417

A.6.6.4.5SSB based L1-RSRP measurement when DRX is used for UE configured with highSpeedMeasFlag-r163417

A.6.6.4.5.1Test Purpose and Environment3417

A.6.6.4.5.2Test parameters3417

A.6.6.4.5.3Test Requirements3419

A.6.6.4.6Inter-cell SSB based L1-RSRP measurements on FR1 PCell when DRX is used3419

A.6.6.4.6.1Test Purpose and Environment3419

A.6.6.4.6.2Test parameters3419

A.6.6.4.6.3Test Requirements3421

A.6.6.4.7SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP3421

A.6.6.4.7.1Test Purpose and Environment3421

A.6.6.4.7.2Test Requirements3421

A.6.6.4.8CSI-RS based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP3421

A.6.6.4.8.1Test Purpose and Environment3421

A.6.6.4.9SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used3422

A.6.6.4.9.1Test Purpose and Environment3422

A.6.6.4.9.2Test parameters3422

A.6.6.4.9.3Test Requirements3423

A.6.6.4.10OD-SSB based L1-RSRP measurement when DRX is not used3424

A.6.6.4.10.1Test Purpose and Environment3424

A.6.6.4.10.2Test parameters3424

A.6.6.4.10.3Test Requirements3427

A.6.6.4.11Event Triggered Reporting for UE initiated beam management without eventDetectionTimeWindowLength-r193427

A.6.6.4.11.1Test Purpose and Environment3427

A.6.6.4.11.2Test parameters3428

A.6.6.4.11.3Test Requirements3430

A.6.6.4.12Event Triggered Reporting for UE initiated beam management with eventDetectionTimeWindowLength-r193430

A.6.6.4.12.1Test Purpose and Environment3430

A.6.6.4.12.2Test parameters3430

A.6.6.4.12.3Test Requirements3432

A.6.6.4.13Event triggered reporting for UE initiated beam management for UE configured with Inter-cell SSB based L1-RSRP measurement on FR1 when DRX is not used3432

A.6.6.4.13.1Test Purpose and Environment3432

A.6.6.4.13.2Test Parameters3432

A.6.6.4.13.3Test Requirements3434

A.6.6.4.14SSB based L1-RSRP measurement on SDL SCell for UE supporting LB CA via switching3434

A.6.6.4.14.1Test Purpose and Environment3434

A.6.6.4.14.2Test parameters3435

A.6.6.4.14.3Test Requirements3436

A.6.6.4.15CSI-RS based L1-RSRP measurement when DRX is not used for SBFD aware UE with DU configuration3436

A.6.6.4.15.1Test Purpose and Environment3436

A.6.6.4.15.2Test parameters3437

A.6.6.4.15.3Test Requirements3438

A.6.6.5Inter-RAT UTRAN FDD measurements3438

A.6.6.5.1SA NR - UTRAN FDD event-triggered reporting in non-DRX in FR13438

A.6.6.5.1.1Test Purpose and Environment3438

A.6.6.5.1.2Test Requirements3440

A.6.6.6CLI measurements3440

A.6.6.6.1SRS-RSRP measurement with DRX3440

A.6.6.6.1.1Test Purpose and Environment3440

A.6.6.6.1.2Test Parameters3441

A.6.6.6.1.3Test Requirements3443

A.6.6.6.2CLI-RSSI measurement with DRX3443

A.6.6.6.2.1Test Purpose and Environment3443

A.6.6.6.2.2Test Parameters3443

A.6.6.6.2.3Test Requirements3444

A.6.6.7NR measurements with autonomous gaps3445

A.6.6.7.1SA intra-frequency CGI identification of NR neighbor cell in FR13445

A.6.6.7.1.1Test Purpose and Environment3445

A.6.6.7.1.2Test Parameters3445

A.6.6.7.1.3Test Requirements3448

A.6.6.7.2Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA3448

A.6.6.7.2.1Test Purpose and Environment3448

A.6.6.7.2.2Test Requirements3450

A.6.6.8L1-SINR measurement for beam reporting3451

A.6.6.8.1L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is used3451

A.6.6.8.1.1Test Purpose and Environment3451

A.6.6.8.1.2Test parameters3451

A.6.6.8.1.3Test Requirements3453

A.6.6.8.2L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used3453

A.6.6.8.2.1Test Purpose and Environment3453

A.6.6.8.2.2Test parameters3453

A.6.6.8.2.3Test Requirements3455

A.6.6.8.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used3455

A.6.6.8.3.1Test Purpose and Environment3455

A.6.6.8.3.2Test parameters3456

A.6.6.8.3.3Test Requirements3457

A.6.6.8.4L1-SINR measurement with SSB based CMR and dedicated IMR for SSB adaptation3457

A.6.6.8.4.1Test Purpose and Environment3457

A.6.6.8.4.2Test parameters3458

A.6.6.8.4.3Test Requirements3462

A.6.6.8.5L1-SINR measurement with SSB based CMR and dedicated IMR with SBFD3462

A.6.6.8.5.1Test Purpose and Environment3462

A.6.6.8.5.2Test parameters3462

A.6.6.8.5.3Test Requirements3464

A.6.6.9Idle Mode CA/DC Measurements3464

A.6.6.9.1SA Idle mode CA/DC measurement for FR13464

A.6.6.9.1.1Test Purpose and Environment3464

A.6.6.9.1.2Test Requirements3467

A.6.6.9.2 Idle mode fast CA/DC eEMR measurement for FR1 without valid reporting3468

A.6.6.9.2.1Test Purpose and Environment3468

A.6.6.9.2.2Test Requirements3470

A.6.6.9.3Idle mode fast CA/DC cell reselection measurement for FR1 without valid reporting3470

A.6.6.9.3.1Test Purpose and Environment3470

A.6.6.9.3.2Test Requirements3473

A.6.6.9.4Idle mode fast CA/DC cell reselection measurement for FR1 with valid reporting3473

A.6.6.9.4.1Test Purpose and Environment3473

A.6.6.9.4.2Test Requirements3476

A.6.6.9.5SA Idle mode CA/DC measurement for FR1 with 12RB SSB3476

A.6.6.9.5.1Test Purpose and Environment3476

A.6.6.9.5.2Test Requirements3477

A.6.6.10CSI-RS based intra-frequency Measurements3477

A.6.6.10.1SA event triggered reporting tests without gap under non-DRX3477

A.6.6.10.1.1Test purpose and Environment3477

A.6.6.10.1.2Test Requirements3479

A.6.6.11CSI-RS based inter-frequency Measurements3479

A.6.6.11.1 SA event triggered reporting tests with gap under DRX3479

A.6.6.11.1.1Test Purpose and Environment3479

A.6.6.11.1.2Test Requirements3482

A.6.6.12RSTD measurements3482

A.6.6.12.1NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA3482

A.6.6.12.1.1Test Purpose and Environment3482

A.6.6.12.1.2Test Requirements3485

A.6.6.12.2NR RSTD measurement reporting delay test case for dual positioning frequency layers in FR1 SA3486

A.6.6.12.2.1Test Purpose and Environment3486

A.6.6.12.2.2Test Requirements3489

A.6.6.12.3NR RSTD measurement reporting delay test case for single positioning frequency layer with reduced number of samples in FR1 SA3489

A.6.6.12.3.1Test Purpose and Environment3489

A.6.6.12.3.2Test Requirements3492

A.6.6.12.4NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA without measurement gap3493

A.6.6.12.4.1Test Purpose and Environment3493

A.6.6.12.4.2Test Requirements3496

A.6.6.12.5NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_CONNECTED state with Rx TEG3496

A.6.6.12.5.1Test Purpose and Environment3496

A.6.6.12.5.2Test Requirements3499

A.6.6.12.6NR RSTD measurement reporting delay test case for PRS aggregation in FR1 SA in RRC_CONNECTED mode3499

A.6.6.12.6.1Test Purpose and Environment3499

A.6.6.12.6.2Test Requirements3505

A.6.6.13 PRS-RSRP measurements3505

A.6.6.13.1PRS-RSRP reporting delay test case for single positioning frequency layer3505

A.6.6.13.1.1Test purpose and Environment3505

A.6.6.13.1.2Test Requirements3507

A.6.6.13.2PRS-RSRP reporting delay test case for dual positioning frequency layer3507

A.6.6.13.2.1Test purpose and Environment3507

A.6.6.13.2.2Test Requirements3510

A.6.6.13.3PRS-RSRP reporting delay test case for reduced number of samples3510

A.6.6.13.3.1Test purpose and Environment3510

A.6.6.13.3.2Test Requirements3512

A.6.6.13.4PRS-RSRP reporting delay test case for single positioning frequency layer outside MG3512

A.6.6.13.4.1Test purpose and Environment3512

A.6.6.14UE Rx-Tx time difference measurements3515

A.6.6.14.1UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA3515

A.6.6.14.1.1Test purpose and environment3515

A.6.6.14.1.2Test requirements3517

A.6.6.14.2UE Rx-Tx time difference measurement for dual positioning frequency layers in FR1 SA3517

A.6.6.14.2.1Test purpose and environment3517

A.6.6.14.2.2Test requirements3519

A.6.6.14.3UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA with reduced sample number3520

A.6.6.14.3.1Test purpose and environment3520

A.6.6.14.3.2Test requirements3522

A.6.6.14.4UE Rx-Tx time difference measurement without gaps in FR1 SA3522

A.6.6.14.4.1Test purpose and environment3522

A.6.6.14.4.2Test requirements3524

A.6.6.14.5UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA with multiple RxTx TEGs3524

A.6.6.14.4.1Test purpose and environment3524

A.6.6.14.4.2Test requirements3526

A.6.6.14.6UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR1 SA3527

A.6.6.14.6.1Test purpose and environment3527

A.6.6.14.6.2Test requirements3530

A.6.6.15Idle Mode measurements of inter-RAT DC candidate cells for early reporting3530

A.6.6.15.1Test Purpose and Environment3530

A.6.6.15.2Test Requirements3534

A.6.6.16PRS-RSRPP measurements3535

A.6.6.16.1PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC_CONNECTED state3535

A.6.6.16.1.1Test purpose and Environment3535

A.6.6.16.1.2Test Requirements3537

A.6.6.16.2PRS-RSRPP reporting delay test case with reduced number of samples for single positioning frequency layer in FR1 in RRC_CONNECTED state3537

A.6.6.16.2.1Test purpose and Environment3537

A.6.6.16.2.2Test Requirements3539

A.6.6.16.3PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC_CONNECTED state without measurement gap3539

A.6.6.16.3.1Test purpose and Environment3539

A.6.6.16.3.2Test Requirements3541

A.6.6.17SA event triggered reporting tests with Pre-MG3542

A.6.6.17.1SA event triggered reporting tests with autonomous activation/deactivation Pre-MG3542

A.6.6.17.1.1Test purpose and Environment3542

A.6.6.17.1.2Test parameters3542

A.6.6.17.1.3Test Requirements3544

A.6.6.17.2SA event triggered reporting tests with pre-configured measurement gaps and network-controlled activation/deactivation3545

A.6.6.17.2.1Test purpose and Environment3545

A.6.6.17.2.2Test parameters3545

A.6.6.17.2.3Test Requirements3547

A.6.6.17.3Void3548

A.6.6.17.3.1Void3548

A.6.6.17.3.2Void3548

A.6.6.17.3.3Void3548

A.6.6.18SA event triggered reporting tests with concurrent gaps3548

A.6.6.18.1SA event triggered reporting tests for FR1 concurrent gaps with non-overalpping scenario for SSB-based measurements in both inter-frequency layers3548

A.6.6.18.1.1Test Purpose and Environment3548

A.6.6.18.1.2Test Requirements3550

A.6.6.18.2SA event triggered reporting tests for FR1 concurrent gap with partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers3550

A.6.6.18.2.1Test Purpose and Environment3550

A.6.6.18.2.2Test Requirements3553

A.6.6.18.3SA NR - E-UTRAN and NR FR1 concurrent event-triggered reporting in non-DRX in FR13553

A.6.6.18.3.1Test Purpose and Environment3553

A.6.6.18.3.2Test Requirements3557

A.6.6.18.4SA event triggered reporting tests for PRS and SSB measurement in FR1 without SSB time index detection when DRX is not used3558

A.6.6.18.4.1Test Purpose and Environment3558

A.6.6.18.4.2Test Requirements3561

A.6.6.19SA event triggered reporting tests with NCSG3561

A.6.6.19.1SA event triggered reporting tests with NCSG under non-DRX in FR13561

A.6.6.19.1.1Test purpose and Environment3561

A.6.6.19.1.2Test parameters3561

A.6.6.19.1.3Test Requirements3564

A.6.6.19.2SA event triggered reporting tests for FR1 with NCSG for inter-frequency measurement3564

A.6.6.19.2.1Test Purpose and Environment3564

A.6.6.19.2.2Test parameters3564

A.6.6.19.2.3Test Requirements3566

A.6.6.19.3SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 with NCSG3567

A.6.6.19.3.1Test Purpose and Environment3567

A.6.6.19.3.2Test parameters3567

A.6.6.19.3.3Test Requirements3570

A.6.6.19.4Event triggered reporting on SCC with deactivated SCell test with per-UE NCSG under non-DRX3570

A.6.6.19.4.1Test purpose and Environment3570

A.6.6.19.4.2Test parameters3570

A.6.6.19.4.3Test Requirements3572

A.6.6.20UE Rx-Tx time difference measurement for propagation delay compensation3572

A.6.6.20.1Test purpose and environment3572

A.6.6.20.2Test requirements3574

A.6.6.21UE Rx-Tx time difference measurement with TRS for RTT-based PDC in FR1 SA3574

A.6.6.21.1Test purpose and environment3574

A.6.6.21.2Test requirements3576

A.6.6.22SA event triggered reporting tests for concurrent measurement gaps with Pre-MG3576

A.6.6.22.1SA event triggered reporting tests for FR1 concurrent gap with Pre-MG with partially partial overalpping scenario for SSB-based measurements in both intra-frequency and inter-frequency layers3576

A.6.6.22.1.1Test Purpose and Environment3576

A.6.6.22.1.2Test Requirements3579

A.6.6.22.2SA event triggered reporting tests for concurrent gap with pre-configured gaps and network-controlled activation/deactivation3580

A.6.6.22.2.1Test purpose and Environment3580

A.6.6.22.2.2Test parameters3580

A.6.6.22.2.3Test Requirements3583

A.6.6.23SA event triggered reporting tests for concurrent measurement gaps with NCSG3583

A.6.6.23.1SA event triggered reporting tests for FR1 concurrent gaps with NCSG for partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers [one MG + one NCSG]3583

A.6.6.23.1.1Test Purpose and Environment3583

A.6.6.23.1.2Test Requirements3586

A.6.6.23.2SA event triggered reporting tests for FR1 concurrent gaps with NCSG for partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers [two NCSG]3586

A.6.6.23.2.1Test Purpose and Environment3586

A.6.6.23.2.2Test Requirements3588

A.6.6.23.3Event triggered reporting on SCC with deactivated SCell test with per-UE Con-NCSG under non-DRX3589

A.6.6.23.3.1Test purpose and Environment3589

A.6.6.23.3.2Test parameters3589

A.6.6.23.3.3Test Requirements3591

A.6.6.24SA event triggered reporting tests with NeedForGap in FR13591

A.6.6.24.1SA event triggered reporting tests without gaps, with interruptions, under non-DRX3591

A.6.6.24.1.1Test purpose and Environment3591

A.6.6.24.1.2Test parameters3592

A.6.6.24.1.3Test Requirements3593

A.6.6.24.2SA event triggered reporting tests for FR1 without gap with interruption for inter-frequency measurement with SSB time index detection when DRX is not used3594

A.6.6.24.2.1Test Purpose and Environment3594

A.6.6.24.2.2Test parameters3594

A.6.6.24.2.3Test Requirements3596

A.6.6.24.3SA event triggered reporting tests for FR1 with ‘no-gap-with-interruption’, without measurement gap or DRX3596

A.6.6.24.3.1Test Purpose and Environment3596

A.6.6.24.3.2Test Requirements3598

A.6.6.24.4SA event triggered reporting tests for FR1 NeedForGaps without gap without interruption when DRX is not used3599

A.6.6.24.4.1Test Purpose and Environment3599

A.6.6.24.4.2Test parameters3599

A.6.6.24.4.3Test Requirements3601

A.6.6.24.5SA event triggered reporting tests without gap under non-DRX for UE indicating no-gap-no-interruption3601

A.6.6.24.5.1Test purpose and Environment3601

A.6.6.24.5.2Test parameters3601

A.6.6.24.5.3Test Requirements3603

A.6.6.25SA NR - E-UTRAN event-triggered without measurement gaps3603

A.6.6.25.1SA NR - E-UTRAN event-triggered reporting in non-DRX in FR13604

A.6.6.25.1.1Test Purpose and Environment3604

A.6.6.25.1.2Test Requirements3607

A.6.6.25.2SA NR - E-UTRAN event-triggered reporting without gap under non-DRX in FR13607

A.6.6.25.2.1Test Purpose and Environment3607

A.6.6.25.2.2Test parameters3607

A.6.6.25.2.3Test Requirements3608

A.6.6.25.3SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for UE capable of inter-RAT EUTRAN measurement without gap when CRS is contained within UE’s active DL BWP3608

A.6.6.25.3.1Test Purpose and Environment3608

A.6.6.25.3.2Test Requirements3612

A.6.6.26LTM Intra-frequency L1-RSRP measurement3612

A.6.6.26.1Intra-frequency SSB based L1-RSRP measurement in FR13612

A.6.6.26.1.1Test Purpose and Environment3612

A.6.6.26.1.2Test Parameters3612

A.6.6.26.1.3Test Requirements3614

A.6.6.26.2Intra-frequency SSB based L1-RSRP measurement in FR13614

A.6.6.26.2.1Test Purpose and Environment3614

A.6.6.26.2.2Test Parameters3615

A.6.6.26.2.3Test Requirements3615

A.6.6.26.3CSI-RS based L1 RSRP measurement for neighbour cell in FR1 with event triggered reporting or periodic reporting3616

A.6.6.26.3.1Test purpose and Environment3616

A.6.6.26.3.2Test Parameters3616

A.6.6.10.1.2Test Requirements3618

A.6.6.27LTM Inter-frequency L1-RSRP measurement with measurement gap3619

A.6.6.27.1Inter-frequency SSB based L1-RSRP measurement with measurement gap3619

A.6.6.27.1.1Test Purpose and Environment3619

A.6.6.27.1.2Test parameters3619

A.6.6.27.1.3Test Requirements3621

A.6.6.27.2Inter-frequency SSB based L1-RSRP measurement with measurement gap with event triggered reporting3621

A.6.6.27.2.1Test Purpose and Environment3621

A.6.6.27.2.2Test parameters3621

A.6.6.27.2.3Test Requirements3622

A.6.6.28LTM Inter-frequency L1-RSRP measurement without measurement gap3622

A.6.6.28.1Inter-frequency SSB based L1-RSRP measurement without measurement gap3622

A.6.6.28.1.1Test Purpose and Environment3622

A.6.6.28.1.2Test parameters3622

A.6.6.28.1.3Test Requirements3625

A.6.6.28.2Inter-frequency SSB based L1-RSRP measurement without measurement gap with event triggered reporting3625

A.6.6.28.2.1Test Purpose and Environment3625

A.6.6.28.2.2Test parameters3625

A.6.6.28.2.3Test Requirements3626

A.6.6.29RSCPD Measurements3626

A.6.6.29.1NR RSCPD with RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_CONNECTED state3626

A.6.6.29.1.1Test Purpose and Environment3626

A.6.6.29.1.2Test Requirements3633

A.6.6.30RSCP Measurements3633

A.6.6.30.1DL RSCP with UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA3633

A.6.6.30.1.1Test purpose and environment3633

A.6.6.30.1.2Test requirements3637

A.6.6.31CJT calibration measurements and accuracy3637

A.6.6.31.1CJTC Delay offset measurement period and accuracy in FR13637

A.6.6.31.1.1Test Purpose and Environment3637

A.6.6.31.1.2Test parameters3638

A.6.6.31.1.3Test Requirements3640

A.6.6.31.2CJTC frequency offset measurement period and accuracy in FR13640

A.6.6.31.2.1Test Purpose and Environment3640

A.6.6.31.2.2Test requirements3642

A.6.6.32L1 CLI measurements3642

A.6.6.32.1L1-SRS-RSRP measurement with DRX with SBFD3642

A.6.6.32.1.1Test Purpose and Environment3642

A.6.6.32.1.2Test Parameters3642

A.6.6.32.1.3Test Requirements3644

A.6.6.32.2L1-CLI-RSSI measurement with DRX with SBFD3644

A.6.6.32.2.1Test Purpose and Environment3644

A.6.6.32.2.2Test Parameters3644

A.6.6.32.2.3Test Requirements3645

A.6.6.33LTM Inter-frequency L1-RSRP measurement with measurement gap cancellation3646

A.6.6.33.1Inter-frequency SSB based L1-RSRP measurement with measurement gap cancellation3646

A.6.6.33.1.1Test Purpose and Environment3646

A.6.6.33.1.2Test parameters3646

A.6.6.33.1.3Test Requirements3646

A.6.6.34DL AI/ML positioning reporting delay test case for single positioning frequency layer in FR1 SA in RRC_CONNECTED state3647

A.6.6.34.1Test Purpose and Environment3647

A.6.6.34.2Test Requirements3650

A.6.7Measurement Performance requirements3650

A.6.7.1SS-RSRP3650

A.6.7.1.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell3650

A.6.7.1.1.1Test Purpose and Environment3650

A.6.7.1.1.2Test parameters3650

A.6.7.1.1.3Test Requirements3654

A.6.7.1.2SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell3654

A.6.7.1.2.1Test Purpose and Environment3654

A.6.7.1.2.2Test parameters3654

A.6.7.1.2.3Test Requirements3657

A.6.7.1.3Void3657

A.6.7.1.4SA inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for UE configured with measurement gap cancellation3657

A.6.7.1.4.1Test Purpose and Environment3657

A.6.7.1.4.2Test parameters3657

A.6.7.1.4.3Test Requirements3658

A.6.7.2SS-RSRQ3658

A.6.7.2.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell3658

A.6.7.2.1.1Test Purpose and Environment3658

A.6.7.2.1.2Test Parameters3658

A.6.7.2.1.3Test Requirements3662

A.6.7.2.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell3662

A.6.7.2.2.1Test Purpose and Environment3662

A.6.7.2.2.2Test Parameters3662

A.6.7.2.2.3Test Requirements3666

A.6.7.3SS-SINR3666

A.6.7.3.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell3666

A.6.7.3.1.1Test Purpose and Environment3666

A.6.7.3.1.2Test Parameters3666

A.6.7.3.1.3Test Requirements3669

A.6.7.3.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell3669

A.6.7.3.2.1Test Purpose and Environment3669

A.6.7.3.2.2Test Parameters3669

A.6.7.3.2.3Test Requirements3673

A.6.7.4L1-RSRP measurement for beam reporting3673

A.6.7.4.1SSB based L1-RSRP measurement3673

A.6.7.4.1.1Test Purpose and Environment3673

A.6.7.4.1.2Test parameters3673

A.6.7.4.1.3Test Requirements3676

A.6.7.4.2CSI-RS based L1-RSRP measurement on resource set with repetition off3676

A.6.7.4.2.1Test Purpose and Environment3676

A.6.7.4.2.2Test parameters3676

A.6.7.4.2.3Test Requirements3679

A.6.7.5E-UTRAN RSRP3680

A.6.7.5.1SA: inter-RAT measurement accuracy with FR1 serving cell3680

A.6.7.5.1.1Test Purpose and Environment3680

A.6.7.5.1.2Test parameters3680

A.6.7.5.1.3Test Requirements3683

A.6.7.6E-UTRAN RSRQ3683

A.6.7.6.1SA: inter-RAT measurement accuracy with FR1 serving cell3683

A.6.7.6.1.1Test Purpose and Environment3683

A.6.7.6.1.2Test parameters3683

A.6.7.6.1.3Test Requirements3686

A.6.7.7E-UTRAN RS-SINR3687

A.6.7.7.1SA: inter-RAT measurement accuracy with FR1 serving cell3687

A.6.7.7.1.1Test Purpose and Environment3687

A.6.7.7.1.2Test parameters3687

A.6.7.7.1.3Test Requirements3690

A.6.7.8CLI measurements3690

A.6.7.8.1SA SRS-RSRP measurement accuracy with FR1 serving cell3690

A.6.7.8.1.1Test Purpose and Environment3690

A.6.7.8.1.2Test parameters3690

A.6.7.8.1.3Test Requirements3693

A.6.7.8.2SA CLI-RSSI measurement accuracy with FR1 serving cell3693

A.6.7.8.2.1Test Purpose and Environment3693

A.6.7.8.2.2Test parameters3694

A.6.7.8.2.3Test Requirements3695

A.6.7.9L1-SINR measurement for beam reporting3695

A.6.7.9.2L1-SINR measurement with SSB based CMR and dedicated IMR3698

A.6.7.9.2.1Test Purpose and Environment3699

A.6.7.9.2.2Test parameters3699

A.6.7.9.2.3Test Requirements3702

A.6.7.9.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR3702

A.6.7.9.3.1Test Purpose and Environment3702

A.6.7.9.3.2Test parameters3703

A.6.7.9.3.3Test Requirements3706

A.6.7.10CSI-RSRP3706

A.6.7.10.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell3706

A.6.7.10.1.1Test Purpose and Environment3706

A.6.7.10.1.2Test parameters3706

A.6.7.10.1.3Test Requirements3709

A.6.7.10.2SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell3709

A.6.7.10.2.1Test Purpose and Environment3710

A.6.7.10.2.2Test parameters3710

A.6.7.10.2.3Test Requirements3713

A.6.7.11CSI-RSRQ3713

A.6.7.11.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell3713

A.6.7.11.1.1Test Purpose and Environment3713

A.6.7.11.1.2Test Parameters3713

A.6.7.11.1.3Test Requirements3717

A.6.7.11.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell3717

A.6.7.11.2.1Test Purpose and Environment3717

A.6.7.11.2.2Test Parameters3717

A.6.7.11.2.3Test Requirements3721

A.6.7.12CSI-SINR3721

A.6.7.12.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell3721

A.6.7.12.1.1Test Purpose and Environment3721

A.6.7.12.1.2Test Parameters3721

A.6.7.12.1.3Test Requirements3724

A.6.7.12.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell3725

A.6.7.12.2.1Test Purpose and Environment3725

A.6.7.12.2.2Test Parameters3725

A.6.7.12.2.3Test Requirements3728

A.6.7.13RSTD measurements3728

A.6.7.13.1RSTD measurement accuracy test case for single positioning frequency layer3728

A.6.7.13.1.1Test purpose and Environment3728

A.6.7.13.1.2Test Requirements3730

A.6.7.13.2RSTD measurement accuracy test case for dual positioning frequency layer3730

A.6.7.13.2.1Test purpose and Environment3730

A.6.7.13.2.2Test Requirements3732

A.6.7.13.3RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR1 in RRC_CONNECTED state3732

A.6.7.13.3.1Test purpose and Environment3732

A.6.7.13.3.2Test Requirements3734

A.6.7.13.4RSTD measurement accuracy test case with Rx TEG3734

A.6.7.13.5NR RSTD measurement accuracy test case for PRS aggregation in FR1 SA in RRC_CONNECTED mode3736

A.6.7.13.5.1Test purpose and Environment3736

A.6.7.13.5.2Test Requirements3739

A.6.7.14PRS-RSRP measurements3739

A.6.7.14.1SA: measurement accuracy with PRS in FR13739

A.6.7.14.1.1Test Purpose and Environment3739

A.6.7.14.1.2Test parameters3739

A.6.7.14.1.3Test Requirements3741

A.6.7.14.2SA: measurement accuracy with PRS in FR1 with reduced sample number3741

A.6.7.14.2.1Test Purpose and Environment3741

A.6.7.14.2.2Test parameters3741

A.6.7.14.2.3Test Requirements3743

A.6.7.14.3Void3743

A.6.7.14.3.1Void3743

A.6.7.14.3.2Void3743

A.6.7.14.3.3Void3743

A.6.7.15UE Rx-Tx time difference measurements3743

A.6.7.15.1UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA3743

A.6.7.15.1.1Test purpose and environment3743

A.6.7.15.1.2Test parameters3744

A.6.7.15.1.3Test requirements3745

A.6.7.15.2UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR1 SA3745

A.6.7.15.2.1Test purpose and environment3745

A.6.7.15.2.2Test parameters3746

A.6.7.15.2.3Test requirements3747

A.6.7.15.3UE Rx-Tx time difference measurement accuracy with RxTx TEG3747

A.6.7.15.3.1Test purpose and environment3747

A.6.7.15.3.2Test parameters3748

A.6.7.15.3.3Test requirements3750

A.6.7.15.4UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR1 SA3750

A.6.7.15.4.1Test purpose and environment3750

A.6.7.15.4.2Test requirements3753

A.6.7.16PRS-RSRPP measurements3753

A.6.7.16.1SA: measurement accuracy with PRS in FR13753

A.6.7.16.1.1Test Purpose and Environment3753

A.6.7.16.1.2Test parameters3753

A.6.7.16.1.3Test Requirements3755

A.6.7.16.2SA: measurement accuracy with reduced PRS samples in FR13755

A.6.7.16.2.1Test Purpose and Environment3755

A.6.7.16.2.2Test parameters3755

A.6.7.17LTM L1-RSRP measurement3757

A.6.7.17.1SSB based Inter-frequency L1-RSRP accuracy requirements for neighbour cell in FR13757

A.6.7.17.1.1Test Purpose and Environment3757

A.6.7.17.1.2Test parameters3758

A.6.7.17.1.3Test Requirements3761

A.6.7.17.2CSI-RS based intra-frequency L1-RSRP accuracy requirement for neighbour cell3761

A.6.7.17.2.1Test Purpose and Environment3761

A.6.7.17.2.2Test parameters3761

A.6.7.17.2.3Test Requirements3765

A.6.7.18TDCP amplitude measurement accuracy3766

A.6.7.18.1TDCP amplitude measurement accuracy in FR13766

A.6.7.18.1.1Test Purpose and Environment3766

A.6.7.18.1.2Test parameters3766

A.6.7.18.1.3Test Requirements3767

A.6.7.19RSCPD Measurements3767

A.6.7.19.1RSCPD with RSTD measurement accuracy in FR1 SA in RRC_CONNECTED3767

A.6.7.19.1.1Test purpose and environment3767

A.6.7.19.1.2Test parameters3768

A.6.7.19.1.3Test requirements3771

A.6.7.20RSCP Measurements3771

A.6.7.20.1RSCP with UE Rx-Tx time difference measurement accuracy in FR1 SA3771

A.6.7.20.1.1Test purpose and environment3771

A.6.7.20.1.2Test parameters3772

A.6.7.20.1.3Test requirements3775

A.6.7.21L1 CLI measurements3775

A.6.7.21.1SA L1-SRS-RSRP measurement accuracy with FR1 serving cell with SBFD3775

A.6.7.21.1.1Test Purpose and Environment3775

A.6.7.21.1.2Test Parameters3775

A.6.7.21.1.3Test Requirements3778

A.6.7.21.2L1-CLI-RSSI measurement accuracy in FR1 with SBFD3778

A.6.7.21.2.1Test Purpose and Environment3778

A.6.7.21.2.2Test parameters3778

A.6.7.21.2.3Test Requirements3779

A.6.8Measurement procedure in RRC_INACTIVE3779

A.6.8.1RSTD measurements3779

A.6.8.1.1NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state3779

A.6.8.1.1.1Test Purpose and Environment3780

A.6.8.1.1.2Test Requirements3782

A.6.8.1.2NR RSTD measurement reporting delay test case with reduced number of samples in RRC_INACTIVE, FR1 SA3783

A.6.8.1.2.1Test Purpose and Environment3783

A.6.8.1.2.1Test Purpose and Environment3783

A.6.8.1.2.2Test Requirements3786

A.6.8.1.3NR RSTD measurement reporting delay test case for PRS aggregation in FR1 SA in RRC_INACTIVE state3786

A.6.8.1.3.1Test purpose and environment3786

A.6.8.1.3.2Test requirements3790

A.6.8.1.4NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state when eDRX cycle > 10.24s for non-RedCap UE3790

A.6.8.1.4.1Test Purpose and Environment3790

A.6.8.1.4.2Test Requirements3794

A.6.8.2PRS-RSRP measurements3794

A.6.8.2.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_INACTIVE3794

A.6.8.2.1.1Test purpose and Environment3794

A.6.8.2.1.2Test Requirements3796

A.6.8.2.2PRS-RSRP reporting delay test case with reduced number of samples in RRC_INACTIVE3796

A.6.8.2.2.1Test purpose and Environment3796

A.6.8.2.2.2Test Requirements3798

A.6.8.2.3PRS-RSRP reporting delay test case in RRC_INACTIVE state in FR1 with eDRX cycle > 10.24s3799

A.6.8.2.3.1Test purpose and Environment3799

A.6.8.2.3.2Test Requirements3801

A.6.8.3UE Rx-Tx time difference measurements3802

A.6.8.3.1UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA3802

A.6.8.3.1.1Test purpose and environment3802

A.6.8.3.1.2Test requirements3804

A.6.8.3.2UE Rx-Tx time difference measurement with reduced number of samples in RRC_INACTIVE, FR1 SA3804

A.6.8.3.2.1Test purpose and environment3804

A.6.8.3.2.2Test requirements3806

A.6.8.3.3UE Rx-Tx time difference measurement for single positioning frequency layer with eDRX > 10.24s in FR1 SA3807

A.6.8.3.3.1Test purpose and environment3807

A.6.8.3.3.2Test requirements3811

A.6.8.3.4UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR1 SA3811

A.6.8.3.4.1Test purpose and environment3811

A.6.8.3.4.2Test requirements3814

A.6.8.4PRS-RSRPP measurements3814

A.6.8.4.1PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC_INACTIVE state3814

A.6.8.4.1.1Test purpose and Environment3815

A.6.8.4.1.2Test Requirements3816

A.6.8.4.2PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC_INACTIVE state for reduced number of samples3817

A.6.8.4.2.1Test purpose and Environment3817

A.6.8.4.2.2Test Requirements3819

A.6.8.4.3PRS-RSRPP reporting delay in RRC_INACTIVE with eDRX3819

A.6.8.4.3.1Test purpose and Environment3819

A.6.8.4.3.2Test Requirements3822

A.6.8.5RSCPD Measurements3822

A.6.8.5.1DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state3822

A.6.8.5.1.1Test Purpose and Environment3822

A.6.8.5.1.2Test Requirements3822

A.6.8.6RSCP Measurements3823

A.6.8.6.1DL RSCP with UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA3823

A.6.8.6.1.1Test purpose and environment3823

A.6.8.6.1.2Test requirements3827

A.6.9Measurement performance requirements in RRC_INACTIVE3827

A.6.9.1RSTD measurements3827

A.6.9.1.1RSTD measurement accuracy test case for single positioning frequency layer in FR1 in RRC_INACTIVE state3827

A.6.9.1.1.1Test purpose and Environment3827

A.6.9.1.1.2Test Requirements3829

A.6.9.1.2RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR1 in RRC_INACTIVE state3829

A.6.9.1.2.1Test purpose and Environment3829

A.6.9.1.2.2Test Requirements3831

A.6.9.1.3RSTD measurement accuracy for PRS aggregation in FR1 in RRC_INACTIVE state3831

A.6.9.1.3.1Test purpose and Environment3831

A.6.9.1.3.2Test Requirements3834

A.6.9.2PRS-RSRP measurements3834

A.6.9.2.1SA: measurement accuracy with PRS in FR1 in RRC_INACTIVE3834

A.6.9.2.1.1Test Purpose and Environment3834

A.6.9.2.1.2Test parameters3834

A.6.9.2.1.3Test Requirements3836

A.6.9.2.2SA: measurement accuracy with PRS in FR1 with reduced number of samples in RRC_INACTIVE state3836

A.6.9.2.2.1Test Purpose and Environment3836

A.6.9.2.2.2Test parameters3836

A.6.9.2.2.3Test Requirements3838

A.6.9.3UE Rx-Tx time difference measurements3838

A.6.9.3.1.1UE Rx-Tx time difference measurement accuracy in FR1 SA3838

A.6.9.3.1.1.1Test purpose and environment3838

A.6.9.3.1.1.2 Test parameters3839

A.6.9.3.1.1.3Test requirements3840

A.6.9.3.2UE Rx-Tx time difference measurement accuracy with reduced number of samples3840

A.6.9.3.2.1Test purpose and environment3840

A.6.9.3.2.2Test parameters3840

A.6.9.3.2.3Test requirements3842

A.6.9.3.3UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR1 SA3842

A.6.9.3.3.1Test purpose and environment3842

A.6.9.3.3.2Test requirements3845

A.6.9.4PRS-RSRPP measurements3845

A.6.9.4.1SA: PRS-RSRPP measurement accuracy in FR1 in RRC INACTIVE3845

A.6.9.4.1.1Test Purpose and Environment3845

A.6.9.4.1.2Test parameters3845

A.6.9.4.1.3Test Requirements3847

A.6.9.4.2SA: measurement accuracy with reduced PRS samples in FR1 in RRC INACTIVE3847

A.6.9.4.2.1Test Purpose and Environment3847

A.6.9.4.2.2Test parameters3848

A.6.9.4.2.3Test Requirements3849

A.6.9.5RSCPD Measurements3850

A.6.9.5.1RSCPD with RSTD measurement accuracy in FR1 SA in RRC_INACTIVE3850

A.6.9.5.1.1Test purpose and environment3850

A.6.9.5.1.2Test parameters3850

A.6.9.5.1.3Test requirements3853

A.6.9.6RSCP Measurements3853

A.6.9.6.1RSCP with UE Rx-Tx time difference measurement accuracy in FR1 SA3853

A.6.9.6.1.1Test purpose and environment3853

A.6.9.6.1.2Test parameters3854

A.6.9.6.1.3Test requirements3857

A.6.10Measurement Procedure in RRC_IDLE3857

A.6.10.1RSTD Measurements3857

A.6.10.1.1NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_IDLE state for non-RedCap UE3857

A.6.10.1.1.1Test purpose and environment3857

A.6.10.1.1.2Test requirements3860

A.6.10.1.2NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_IDLE state with eDRX cycle > 10.24s for non-RedCap UE3861

A.6.10.1.2.1Test Purpose and Environment3861

A.6.10.1.2.2Test Requirements3864

A.6.10.1.3NR RSTD measurement reporting delay test case for PRS aggregation in FR1 SA in RRC_IDLE state3864

A.6.10.1.3.1Test purpose and environment3864

A.6.10.1.3.2Test requirements3864

A.6.10.2 PRS-RSRP Measurements3865

A.6.10.2.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_IDLE state for non-RedCap UE in FR13865

A.6.10.2.1.1Test purpose and Environment3865

A.6.10.2.1.2Test Requirements3867

A.6.10.2.2PRS-RSRP reporting delay test case in RRC_IDLE state in FR1 when eDRX cycle > 10.24s3868

A.6.10.2.2.1Test purpose and Environment3868

A.6.10.2.2.2Test Requirements3868

A.6.10.3RSCPD Measurements3868

A.6.10.3.1DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_IDLE state3868

A.6.10.3.1.1Test Purpose and Environment3868

A.6.10.3.1.2Test Requirements3869

A.6.11Measurement Performance Requirements in RRC_IDLE3869

A.6.11.1RSTD Measurements3869

A.6.11.1.1NR RSTD measurement accuracy test case for single positioning frequency layer in FR1 SA in RRC_IDLE state for non-RedCap UE3869

A.6.11.1.1.1Test purpose and environment3869

A.6.11.1.1.2Test requirements3871

A.6.11.1.2RSTD measurement accuracy test case for single positioning frequency layer in FR1 in RRC_IDLE state with eDRX>10.24s for non-RedCap UE3871

A.6.11.1.2.1Test purpose and Environment3871

A.6.11.1.2.2Test Requirements3873

A.6.11.1.3NR RSTD measurement accuracy test case for PRS aggregation in FR1 SA in RRC_IDLE state3873

A.6.11.1.3.1Test purpose and environment3873

A.6.11.1.3.2Test requirements3873

A.6.11.2PRS-RSRP measurements3873

A.6.11.2.1PRS-RSRP measurement accuracy test case for non-RedCap UE in FR1 in RRC_IDLE state3873

A.6.11.2.1.1Test Purpose and Environment3873

A.6.11.2.1.2Test parameters3874

A.6.11.2.1.3Test Requirements3876

A.6.11.2.2PRS-RSRP measurement accuracy test case in RRC_IDLE state in FR1 when eDRX cycle > 10.24s3876

A.6.11.2.2.1Test purpose and Environment3876

A.6.11.2.2.2Test parameters3876

A.6.11.2.2.3Test Requirements3877

A.6.11.3RSCPD Measurements3877

A.6.11.3.1RSCPD with RSTD measurement accuracy in FR1 SA in RRC_IDLE3877

A.6.11.3.1.1Test purpose and environment3877

A.6.11.3.1.2Test parameters3877

A.6. 11.3.1.3Test requirements3880

A.7NR standalone tests with one or more NR cells in FR23881

A.7.1SA: RRC_IDLE state mobility3881

A.7.1.1Cell re-selection to NR3881

A.7.1.1.1Cell reselection to FR2 intra-frequency NR case3881

A.7.1.1.1.1Test Purpose and Environment3881

A.7.1.1.1.2Test Parameters3881

A.7.1.1.1.3Test Requirements3883

A.7.1.1.2Cell reselection to FR2 inter-frequency NR case3883

A.7.1.1.2.1Test Purpose and Environment3884

A.7.1.1.2.2Test Parameters3884

A.7.1.1.2.3Test Requirements3885

A.7.1.1.3Cell reselection to FR2 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion3886

A.7.1.1.3.1Test Purpose and Environment3886

A.7.1.1.3.2Test Parameters3886

A.7.1.1.3.3Test Requirements3888

A.7.1.1.4Cell reselection to FR2 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion3888

A.7.1.1.4.1Test Purpose and Environment3888

A.7.1.1.4.2Test Parameters3889

A.7.1.1.4.3Test Requirements3890

A.7.1.1.5Cell reselection to FR2 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion3891

A.7.1.1.5.1Test Purpose and Environment3891

A.7.1.1.5.2Test Parameters3891

A.7.1.1.5.3Test Requirements3893

A.7.1.1.6Cell reselection to FR2 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion3893

A.7.1.1.6.1Test Purpose and Environment3893

A.7.1.1.6.2Test Parameters3894

A.7.1.1.6.3Test Requirements3895

A.7.1.1.7Cell reselection to FR2 intra-frequency NR case for FR2 power class 6 UE configured with highSpeedMeasFlagFR2-r173896

A.7.1.1.7.1Test Purpose and Environment3896

A.7.1.1.7.2Test Parameters3896

A.7.1.1.7.3Test Requirements3898

A.7.1.1.8Cell reselection to FR2 inter-frequency NR case for UE configured with highSpeedMeasFlagFR2-r173898

A.7.1.1.8.1Test Purpose and Environment3898

A.7.1.1.8.2Test Parameters3899

A.7.1.1.8.3Test Requirements3900

A.7.1.1.9Cell reselection to FR2 intra-frequency NR case for FR2 cell supporting OD-SIB13901

A.7.1.1.9.1Test Purpose and Environment3901

A.7.1.1.9.2Test Parameters3901

A.7.1.1.9.3Test Requirements3903

A.7.1.1.10Cell reselection to FR2 inter-frequency NR case for FR2 cell supporting OD- SIB13903

A.7.1.1.10.1Test Purpose and Environment3903

A.7.1.1.10.2Test Parameters3904

A.7.1.1.10.3Test Requirements3905

A.7.2SA: RRC_INACTIVE state mobility3906

A.7.2.1Small Data Transmission3906

A.7.2.1.1TA validation for CG-SDT in FR23906

A.7.2.1.1.1Test Purpose and Environment3906

A.7.2.1.1.2Test Requirements3909

A.7.2.2Cell reselection for positioning3909

A.7.2.2.1Cell reselection to FR2 intra-frequency NR case with RRC_ INACTIVE eDRX and positioning SRS3909

A.7.2.2.1.1Test Purpose and Environment3909

A.7.2.2.1.2Test Parameters3909

A.7.2.2.1.3Test Requirements3912

A.7.3RRC_CONNECTED state mobility3912

A.7.3.1Handover3912

A.7.3.1.1Inter-frequency handover from FR1 to FR2; unknown target cell3912

A.7.3.1.1.1Test Purpose and Environment3912

A.7.3.1.1.2Test Parameters3912

A.7.3.1.1.3Test Requirements3914

A.7.3.1.2Intra-frequency handover from FR2 to FR2; unknown target cell3915

A.7.3.1.2.1Test Purpose and Environment3915

A.7.3.1.2.2Test Parameters3915

A.7.3.1.2.3Test Requirements3916

A.7.3.1.3Inter-frequency handover from FR2 to FR2; unknown target cell3916

A.7.3.1.3.1Test Purpose and Environment3916

A.7.3.1.3.2Test Parameters3916

A.7.3.1.3.3Test Requirements3918

A.7.3.1.4Inter-band inter-frequency synchronous DAPS handover from FR1 to FR23918

A.7.3.1.4.1Test Purpose and Environment3918

A.7.3.1.4.2Test Parameters3918

A.7.3.1.4.3 Test Requirements3921

A.7.3.1.5Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR23922

A.7.3.1.5.1Test Purpose and Environment3922

A.7.3.1.5.2Test Parameters3922

A.7.3.1.5.3 Test Requirements3925

A.7.3.1.6Handover with PSCell from SA to EN-DC with unknown FR2 target PScell3926

A.7.3.1.6.1Test Purpose and Environment3926

A.7.3.1.6.2Test Parameters3926

A.7.3.1.6.3Test Requirements3931

A.7.3.1.7HO with PSCell from FR1 NR-SA to EN-DC with known E-UTRA PCell and known FR2 PSCell3931

A.7.3.1.7.1Test purpose and environment3931

A.7.3.1.7.2Test Requirements3935

A.7.3.1.8NR PSCell change delay in HO with PSCell from NR-DC to NR-DC3936

A.7.3.1.8.1Test Purpose and Environment3936

A.7.3.1.8.2Test Requirements3939

A.7.3.1.9Intra-frequency handover from FR2-2 to FR2-2; unknown target cell3939

A.7.3.1.9.1Test Purpose and Environment3939

A.7.3.1.9.2Test Parameters3939

A.7.3.1.9.3Test Requirements3941

A.7.3.1.10Inter-frequency handover from FR2-2 to FR2-2; unknown target cell3942

A.7.3.1.10.1Test Purpose and Environment3942

A.7.3.1.10.2Test Parameters3942

A.7.3.1.10.3Test Requirements3944

A.7.3.1.11Inter-frequency handover from FR1 to FR2-2; unknown target cell3944

A.7.3.1.11.1Test Purpose and Environment3944

A.7.3.1.11.2Test Parameters3944

A.7.3.1.11.3Test Requirements3946

A.7.3.1.12Intra-frequency handover from FR2 to FR2; known target cell configured with NCD-SSB3947

A.7.3.1.12.1Test Purpose and Environment3947

A.7.3.1.12.2Test Parameters3947

A.7.3.1.12.3Test Requirements3948

A.7.3.1.13Inter-frequency handover from FR2 to FR2; known target cell configured with NCD-SSB3949

A.7.3.1.13.1Test Purpose and Environment3949

A.7.3.1.13.2Test Parameters3949

A.7.3.1.13.3Test Requirements3951

A.7.3.1.14Handover with PSCell from FR1-FR2 NR-DC to FR1-FR1 NR-DC with target PSCell in FR13951

A.7.3.1.14.1Test Purpose and Environment3951

A.7.3.1.14.2Test Requirements3955

A.7.3.1.15HO with PSCell from FR1-FR1 NR-DC to FR1-FR2 NR-DC3955

A.7.3.1.15.1Test Purpose and Environment3955

A.7.3.1.15.2Test Requirements3960

A.7.3.1.16Intra-frequency handover from FR2 to FR2; unknown target cell; for UE supporting fast beam sweeping3960

A.7.3.1.16.1Test Purpose and Environment3960

A.7.3.1.16.2Test Parameters3960

A.7.3.1.16.3Test Requirements3962

A.7.3.1.17Inter-frequency handover from FR2 to FR2; unknown target cell; for UE supporting fast beam sweeping3962

A.7.3.1.17.1Test Purpose and Environment3962

A.7.3.1.17.2Test Parameters3962

A.7.3.1.17.3Test Requirements3964

A.7.3.2RRC Connection Mobility Control3964

A.7.3.2.1SA: RRC Re-establishment3964

A.7.3.2.1.1Intra-frequency RRC Re-establishment in FR23964

A.7.3.2.1.2Inter-frequency RRC Re-establishment in FR23966

A.7.3.2.1.3Intra-frequency RRC Re-establishment in FR2 without serving cell timing3968

A.7.3.2.1.3.1Test Purpose and Environment3968

A.7.3.2.1.3.2Test Requirements3970

A.7.3.2.1.4Intra-frequency RRC Re-establishment in FR2-23971

A.7.3.2.1.4.1Test Purpose and Environment3971

A.7.3.2.1.4.2Test Requirements3972

A.7.3.2.1.5Inter-frequency RRC Re-establishment in FR2-23973

A.7.3.2.1.5.1Test Purpose and Environment3973

A.7.3.2.1.5.2Test Requirements3975

A.7.3.2.1.6Intra-frequency RRC Re-establishment in FR2-2 without serving cell timing3975

A.7.3.2.1.6.1Test Purpose and Environment3975

A.7.3.2.1.6.2Test Requirements3977

A.7.3.2.1.7Intra-frequency RRC Re-establishment in FR2 with UE capable of reduced beam sweeping factor3978

A.7.3.2.1.7.1Test Purpose and Environment3978

A.7.3.2.1.7.2Test Requirements3979

A.7.3.2.1.8Inter-frequency RRC Re-establishment in FR2 without serving cell timing with UE capable of reduced beam sweeping factor3980

A.7.3.2.1.8.1Test Purpose and Environment3980

A.7.3.2.1.8.2Test Requirements3982

A.7.3.2.2Random Access3982

A.7.3.2.2.14-step RA type c ontention based random access test in FR2 for NR Standalone3982

A.7.3.2.2.24-step RA type n on-contention based random access test in FR2 for NR Standalone3986

A.7.3.2.2.32-step RA type contention based random access test in FR2 for NR Standalone3989

A.7.3.2.2.42-step RA type n on-contention based random access test in FR2 for NR Standalone3991

A.7.3.2.3SA: RRC Connection Release with Redirection3994

A.7.3.2.3.1Redirection from NR in FR2 to NR in FR23994

A.7.3.2.3.2Redirection from NR in FR2 to NR in FR2 with UE capable of reduced beam sweeping factor3996

A.7.3.2.4LTM PDCCH-order Random Access3998

A.7.3.2.4.1PDCCH-order RACH on neighbor cell in FR2 when RACH BW is within active BWP3998

A.7.3.2.4.2PDCCH-order RACH on inter-frequency neighbor cell in FR24001

A.7.3.3Conditional Handover4004

A.7.3.3.1Intra-frequency conditional handover from FR2 to FR24004

A.7.3.3.1.1Test Purpose and Environment4004

A.7.3.3.1.2Test Parameters4004

A.7.3.3.1.2.3Test Requirements4006

A.7.3.3.2Inter-frequency conditional handover from FR2 to FR2; unknown target cell4006

A.7.3.3.2.1Test Purpose and Environment4006

A.7.3.3.2.2Test Parameters4006

A.7.3.3.2.3Test Requirements4007

A.7.3.3.3NES triggering intra-frequency target CHO delay From FR2 to FR24008

A.7.3.3.3.1Test Purpose and Environment4008

A.7.3.3.3.2Test Parameters4008

A.7.3.3.3.2.3Test Requirements4009

A.7.3.3.4NES triggering inter-frequency conditional handover from FR2 to FR14010

A.7.3.3.4.1Test Purpose and Environment4010

A.7.3.3.4.2Test Parameters4010

A.7.3.3.4.3Test Requirements4012

A.7.3.3.5NR conditional handover including target MCG and target SCG from FR1-FR2 NR-DC to FR1-FR2 NR-DC4012

A.7.3.3.5.1Test Purpose and Environment4012

A.7.3.3.5.2Test Requirements4015

A.7.3.3.5.2.1Test Requirements for NR conditional handover4015

A.7.3.3.5.2.2Test Requirements for NR PSCell change4015

A.7.3.3.6NR conditional Handover including target MCG and candidate SCG from FR1-FR2 NR-DC to FR1-FR2 NR-DC4015

A.7.3.3.6.1Test Purpose and Environment4015

A.7.3.3.6.2Test Parameters4015

A.7.3.3.6.3 Test Requirements4019

A.7.3.4LTM PCell Switch4019

A.7.3.4.1RACH based Intra-frequency PCell switch from FR2 to FR24019

A.7.3.4.1.1Test Purpose and Environment4019

A.7.3.4.1.2Test Parameters4019

A.7.3.4.1.3Test Requirements4022

A.7.3.4.2RACH-less Intra-frequency PCell switch from FR2 to FR24023

A.7.3.4.2.1Test Purpose and Environment4023

A.7.3.4.2.2Test Parameters4023

A.7.3.4.2.3Test Requirements4027

A.7.3.4.3RACH-based Inter-frequency LTM PCell switch from FR2 to FR24027

A.7.3.4.3.1Test Purpose and Environment4027

A.7.3.4.3.2Test Parameters4027

A.7.3.4.3.3Test Requirements4030

A.7.3.4.4RACH-less Intra-frequency CLTM PCell switch from FR2 to FR2 triggered by SSB based L1-RSRP measurement4031

A.7.3.4.4.1Test Purpose and Environment4031

A.7.3.4.4.2Test Parameters4031

A.7.3.4.4.3Test Requirements4036

A.7.3.4.5RACH-based Intra-frequency CLTM PCell switch from FR2 to FR2 triggered by SSB based L1-RSRP measurement4037

A.7.3.4.5.1Test Purpose and Environment4037

A.7.3.4.5.2Test Parameters4037

A.7.3.4.5.3Test Requirements4040

A.7.3.5LTM PSCell Switch4040

A.7.3.5.1RACH-based Intra-frequency LTM PSCell switch from FR2 to FR24040

A.7.3.5.1.1Test Purpose and Environment4040

A.7.3.5.1.2Test Parameters4040

A.7.3.5.1.3Test Requirements4045

A.7.4Timing4045

A.7.4.1UE transmit timing4045

A.7.4.1.1NR UE Transmit Timing Test for FR24045

A.7.4.1.1.1Test Purpose and environment4045

A.7.4.1.1.2Test requirements4047

A.7.4.1.2NR UE Transmit Timing Test for FR2-24048

A.7.4.1.2.1Test Purpose and environment4048

A.7.4.1.2.2Test requirements4051

A.7.4.1.3NR UE Transmit Timing Test with 2-TA for FR2 UE supporting multiDCI-IntraCellMultiTRP-TwoTA-r184051

A.7.4.1.3.1Test Purpose and environment4051

A.7.4.1.3.2Test requirements4054

A.7.4.1.4NR UE Transmit Timing Test with 2-TA for FR2 UE supporting single DCI4055

A.7.4.1.4.1Test Purpose and environment4055

A.7.4.1.4.2Test requirements4059

A.7.4.2UE timer accuracy4060

A.7.4.3Timing advance4060

A.7.4.3.1SA FR2 timing advance adjustment accuracy4060

A.7.4.3.1.1Test Purpose and Environment4060

A.7.4.3.1.2Test Parameters4060

A.7.4.3.1.3 Test Requirements4062

A.7.4.3.2SA FR2-2 timing advance adjustment accuracy4063

A.7.4.3.2.1Test Purpose and Environment4063

A.7.4.3.2.2Test Parameters4063

A.7.4.3.2.3Test Requirements4065

A.7.4.3.3SA FR2 timing advance adjustment accuracy for asymmetric DL sTRP/UL mTRP deployment with two TAs4066

A.7.4.3.3.1Test Purpose and Environment4066

A.7.4.3.3.2Test Parameters4066

A.7.5Signaling characteristics4069

A.7.5.1Radio link Monitoring4069

A.7.5.1.1Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode4069

A.7.5.1.1.1Test Purpose and Environment4069

A.7.5.1.1.2Test Requirements4072

A.7.5.1.2Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode4072

A.7.5.1.2.1Test Purpose and Environment4072

A.7.5.1.2.2Test Requirements4075

A.7.5.1.3Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode4075

A.7.5.1.3.1Test Purpose and Environment4075

A.7.5.1.3.2Test Requirements4077

A.7.5.1.4Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode4078

A.7.5.1.4.1Test Purpose and Environment4078

A.7.5.1.4.2Test Requirements4080

A.7.5.1.5Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode4080

A.7.5.1.5.1Test Purpose and Environment4080

A.7.5.1.5.2Test Requirements4084

A.7.5.1.6Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode4084

A.7.5.1.6.1Test Purpose and Environment4084

A.7.5.1.6.2Test Requirements4088

A.7.5.1.7Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode4088

A.7.5.1.7.1Test Purpose and Environment4088

A.7.5.1.7.2Test Requirements4091

A.7.5.1.8Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode4091

A.7.5.1.8.1Test Purpose and Environment4091

A.7.5.1.8.2Test Requirements4095

A.7.5.1.9UE Radio Link Monitoring Scheduling Restrictions on FR24095

A.7.5.1.9.1Test Purpose and Environment4095

A.7.5.1.9.2Test Requirements4097

A.7.5.1.10Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode for UE supporting fast beam sweeping in multi-Rx4097

A.7.5.1.10.1Test Purpose and Environment4097

A.7.5.1.10.2Test Requirements4100

A.7.5.1.11Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP4100

A.7.5.1.11.1Test Purpose and Environment4100

A.7.5.1.12Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP4100

A.7.5.1.12.1Test Purpose and Environment4100

A.7.5.1.12.2Test Requirements4101

A.7.5.1.13Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP4101

A.7.5.1.13.1Test Purpose and Environment4101

A.7.5.1.13.2Test Requirements4104

A.7.5.1.14Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode  for a UE operating with SBFD4104

A.7.5.1.14.1Test Purpose and Environment4104

A.7.5.1.14.2Test Requirements4107

A.7.5.2Interruption4107

A.7.5.2.1Interruptions during measurements on deactivated NR SCC in FR24107

A.7.5.2.1.1Test Purpose and Environment4107

A.7.5.2.1.2Test Requirements4109

A.7.5.2.2SA interruptions at NR SRS carrier-based switching4110

A.7.5.2.2.1Test Purpose and Environment4110

A.7.5.2.2.2Test Parameters4110

A.7.5.2.2.3Test Requirements4112

A.7.5.3SCell Activation and Deactivation Delay4112

A.7.5.3.1SCell Activation and deactivation for SCell in FR2 intra-band in non-DRX4112

A.7.5.3.1.1Test Purpose and Environment4112

A.7.5.3.1.2Test Requirements4113

A.7.5.3.2SCell Activation and deactivation for FR1+FR2 inter-band with target SCell in FR24113

A.7.5.3.2.1Test Purpose and Environment4113

A.7.5.3.2.2Test Requirements4116

A.7.5.3.3SCell Activation and deactivation for SCell in FR2 inter-band in non-DRX4116

A.7.5.3.3.1Test Purpose and Environment4116

A.7.5.3.3.2Test Requirements4119

A.7.5.3.4Direct SCell activation at SCell addition of known SCell in FR24119

A.7.5.3.4.1Test Purpose and Environment4119

A.7.5.3.4.2Test Requirements4121

A.7.5.3.5Direct SCell activation at handover with known SCell in FR24122

A.7.5.3.5.1Test Purpose and Environment4122

A.7.5.3.5.2Test Requirements4124

A.7.5.3.6PUCCH SCell activation and deactivation for FR1+FR2 inter-band with target SCell in FR2 and known4125

A.7.5.3.6.1Test Purpose and Environment4125

A.7.5.3.6.2Test Requirements4128

A.7.5.3.7PUCCH SCell activation and deactivation delay requirements of FR2 unknown cell with FR1 PCell4128

A.7.5.3.7.1Test Purpose and Environment4128

A.7.5.3.7.2Test Requirements4131

A.7.5.3.8SCell Activation and deactivation for known PUCCH SCell in FR2 inter-band in non-DRX4132

A.7.5.3.8.1Test Purpose and Environment4132

A.7.5.3.8.2Test Requirements4135

A.7.5.3.9PUCCH SCell Activation and deactivation of unknown SCell in FR24136

A.7.5.3.9.1Test Purpose and Environment4136

A.7.5.3.9.2Test Requirements4138

A.7.5.3.10SCell Activation and deactivation of FR2 known PUCCH SCell and one FR2 unknown SCell with FR2 PCell4139

A.7.5.3.10.1Test Purpose and Environment4139

A.7.5.3.10.2Test Requirements4142

A.7.5.3.11PUCCH SCell activation and deactivation delay requirements of FR2 unknown cell with FR2 PCell4143

A.7.5.3.11.1PUCCH SCell activation with non-PUCCH SCell in a secondary PUCCH Group4143

A.7.5.3.11.1.1Test Purpose and Environment4143

A.7.5.3.11.1.2Test Requirements4146

A.7.5.3.11.2PUCCH SCell activation with non-PUCCH SCell in a primary PUCCH Group4147

A.7.5.3.11.2.1Test Purpose and Environment4147

A.7.5.3.11.2.2Test Requirements4150

A.7.5.3.12Void4151

A.7.5.3.13SCell Activation for SCell in FR2 intra-band in non-DRX4151

A.7.5.3.13.1Test Purpose and Environment4151

A.7.5.3.13.2Test Requirements4153

A.7.5.3.14SCell Activation for known SCell in FR2 inter-band4153

A.7.5.3.14.1Test Purpose and Environment4153

A.7.5.3.14.2Test Requirements4155

A.7.5.3.15PUCCH SCell activation and deactivation with FR1 PCell based on L3 reporting after SCell activation command4156

A.7.5.3.15.1Test Purpose and Environment4156

A.7.5.3.15.2Test Requirements4160

A.7.5.3.16PUCCH SCell activation and deactivation with FR2 PCell based on L3 reporting after SCell activation command4160

A.7.5.3.16.1Test Purpose and Environment4160

A.7.5.3.16.2Test Requirements4163

A.7.5.3.17SCell Activation and deactivation for SCell in FR2 inter-band in DRX for UE capable of small beam sweeping factors and/or short measurement interval4164

A.7.5.3.17.1Test Purpose and Environment4164

A.7.5.3.17.2Test Requirements4166

A.7.5.3.18SCell Activation and deactivation for FR1+FR2 inter-band with target SCell in FR2, in DRX, for UE capable of small beam sweeping factors and/or short measurement interval4168

A.7.5.3.18.1Test Purpose and Environment4168

A.7.5.3.18.2Test Requirements4171

A.7.5.3.19SCell Activation and deactivation of FR2 unknown SCell with FR1 PCell in non-DRX with L3 reporting during activation4173

A.7.5.3.19.1Test Purpose and Environment4173

A.7.5.3.19.2Test Requirements4176

A.7.5.3.20SCell Activation and Deactivation of FR2 unkown SCell with FR2 PCell in non-DRX with L3 reporting during activation4176

A.7.5.3.20.1Test Purpose and Environment4177

A.7.5.3.20.2Test Requirements4179

A.7.5.3.21OD-SSB based SCell Activation and deactivation of unknown SCell in FR2 DRX mode(OD-SSB Case 1)4180

A.7.5.3.21.1Test Purpose and Environment4180

A.7.5.3.21.2Test Requirements4183

A.7.5.3.22OD-SSB based SCell Activation for known SCell in FR2 inter-band4183

A.7.5.3.22.1Test Purpose and Environment4183

A.7.5.3.22.2Test Requirements4186

A.7.5.3.23EMR based SCell activation of unknown SCell in FR24186

A.7.5.3.23.1Test Purpose and Environment4186

A.7.5.3.23.2Test Requirements4190

A.7.5.3.24EMR based SCell activation of unknown SCell in FR2 in RRC Inactive4190

A.7.5.3.24.1Test Purpose and Environment4190

A.7.5.3.25PUCCH SCell Activation of unknown SCell for UE supporting EMR in FR24195

A.7.5.3.25.1Test Purpose and Environment4195

A.7.5.3.25.2Test Requirements4198

A.7.5.4Void4198

A.7.5.5Beam Failure Detection and Link recovery procedures4198

A.7.5.5.1Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode4198

A.7.5.5.1.1Test Purpose and Environment4198

A.7.5.5.1.2Test Requirements4201

A.7.5.5.2Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode4202

A.7.5.5.2.1Test Purpose and Environment4202

A.7.5.5.2.2Test Requirements4205

A.7.5.5.3Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode4205

A.7.5.5.3.1Test Purpose and Environment4205

A.7.5.5.3.2Test Requirements4208

A.7.5.5.4Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode4208

A.7.5.5.4.1Test Purpose and Environment4208

A.7.5.5.4.2Test Requirements4211

A.7.5.5.5Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode4212

A.7.5.5.5.1Test Purpose and Environment4212

A.7.5.5.5.2Test Requirements4215

A.7.5.5.6Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in non-DRX mode4215

A.7.5.5.6.1Test Purpose and Environment4215

A.7.5.5.6.2Test Requirements4218

A.7.5.5.7Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode4218

A.7.5.5.7.1Test Purpose and Environment4218

A.7.5.5.7.2Test Requirements4221

A.7.5.5.8Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode for UE fulfilling relaxed measurement criterion4222

A.7.5.5.8.1Test Purpose and Environment4222

A.7.5.5.8.2Test Requirements4225

A.7.5.5.9TRP specific Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode4225

A.7.5.5.9.1Test Purpose and Environment4225

A.7.5.5.9.2Test Requirements4228

A.7.5.5.10TRP specific Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode4229

A.7.5.5.10.1Test Purpose and Environment4229

A.7.5.5.10.2Test Requirements4232

A.7.5.5.11Beam Failure Detection and Link Recovery Test for FR2-2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode4232

A.7.5.5.11.1Test Purpose and Environment4232

A.7.5.5.11.2Test Requirements4235

A.7.5.5.12Beam Failure Detection and Link Recovery Test for FR2-2 PCell configured with CSI-RS-based BFD and LR in DRX mode4235

A.7.5.5.12.1Test Purpose and Environment4235

A.7.5.5.12.2Test Requirements4238

A.7.5.5.13Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2-2 PCell configured with SSB-based BFD and LR in non-DRX mode4239

A.7.5.5.13.1Test Purpose and Environment4239

A.7.5.5.13.2Test Requirements4241

A.7.5.5.14TRP specific Beam Failure Detection and Link Recovery for FR2 PCell configured with CSI-RS-based BFD and LR and multi-Rx operation in DRX mode4241

A.7.5.5.14.1Test Purpose and Environment4241

A.7.5.5.14.2Test Requirements4245

A.7.5.5.15Beam Failure Detection and Link Recovery Test for FR2 Pcell configured with CSI-RS-based BFD and LR in non-DRX mode for a UE operating with SBFD4245

A.7.5.5.15.1Test Purpose and Environment4245

A.7.5.5.15.2Test Requirements4247

A.7.5.6Active BWP switch4247

A.7.5.6.1DCI-based and Timer-based Active BWP Switch4247

A.7.5.6.1.1NR FR2- NR FR2 DL active BWP switch of SCell with non-DRX in SA4247

A.7.5.6.1.2NR FR1- NR FR2 DL active BWP switch of SCell with non-DRX in SA4251

A.7.5.6.1.3NR FR2 DL active BWP switch with non-DRX in SA4255

A.7.5.6.1.3.1Test Purpose and Environment4255

A.7.5.6.1.3.2Test Requirements4257

A.7.5.6.1.4NR FR2-2- NR FR2-2 DL active BWP switch of SCell with non-DRX in SA4257

A.7.5.6.1.4.1Test Purpose and Environment4257

A.7.5.6.1.4.2Test Requirements4260

A.7.5.6.2RRC-based Active BWP Switch4261

A.7.5.6.2.1.1Test Purpose and Environment4261

A.7.5.6.2.1.2Test Requirements4264

A.7.5.6.2.2NR FR2-2 DL active BWP switch of PCell with non-DRX in SA4264

A.7.5.6.2.2.1Test Purpose and Environment4264

A.7.5.6.2.2.2Test Requirements4266

A.7.5.6.3Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs4267

A.7.5.6.3.1.1Test Purpose and Environment4267

A.7.5.6.3.1.2Test Requirements4269

A.7.5.6.4SCell dormancy switch4270

A.7.5.6.4.1NR FR2 PCell SCell dormancy switch of single FR2 SCell inside active time4270

A.7.5.6.4.1.1Test Purpose and Environment4270

A.7.5.6.4.1.2Test Requirements4272

A.7.5.6.4.2NR FR1 PCell SCell dormancy switch of two FR2 SCells outside active time4273

A.7.5.6.4.2.1 Test Purpose and Environment4273

A.7.5.6.4.2.2 Test Requirements4276

A.7.5.6.5Simultaneous RRC-based Active BWP Switch on multiple CCs4276

A.7.5.6.5.1Active BWP switch on multiple SCells with non-DRX in SA4276

A.7.5.6.5.2NR FR2-2 Active BWP switch on multiple SCells with non-DRX in SA4278

A.7.5.6.5.2.1Test Purpose and Environment4278

A.7.5.6.5.2.2Test Requirements4281

A.7.5.7PSCell addition and release delay4281

A.7.5.7.1Addition and Release Delay of known NR PSCell4281

A.7.5.7.1.1Test Purpose and Environment4281

A.7.5.7.1.2Test Requirements4284

A.7.5.7.2Addition and Release Delay of unknown NR PSCell in4284

A.7.5.7.2.1Test Purpose and Environment4284

A.7.5.7.2.2Test Requirements4286

A.7.5.7.3Addition and Release Delay of known NR PSCell in FR2-24286

A.7.5.7.3.1Test Purpose and Environment4286

A.7.5.7.3.2Test Requirements4289

A.7.5.7.4Addition and Release Delay of unknown NR PSCell in FR2-24289

A.7.5.7.4.1Test Purpose and Environment4289

A.7.5.7.4.2Test Requirements4291

A.7.5.8Active TCI state switch delay4292

A.7.5.8.1MAC-CE based active TCI state switch4292

A.7.5.8.2RRC based active TCI state switch4295

A.7.5.8.3MAC-CE based active TCI state switch for HST FR2 scenario4298

A.7.5.8.3.1NR PCell FR2 HST active TCI state switch for a known TCI state4298

A.7.5.8.3.1.1Test Purpose and Environment4298

A.7.5.8.3.1.2Test Requirements4301

A.7.5.8.3.2NR PCell FR2 HST active TCI state switch for PC6 UE supporting tciStateSwitchIndr18 for a known TCI state4302

A.7.5.8.3.2.1Test Purpose and Environment4302

A.7.5.8.3.2.2Test Requirements4305

A.7.5.8.4DCI based active TCI state switch with m-DCI for simultaneous reception4305

A.7.5.8.4.1Test Purpose and Environment4305

A.7.5.8.4.2Test Requirements4308

A.7.5.8.5Single-DCI FR2 DCI based active TCI state switch with known target TCI states for simultaneous reception4308

A.7.5.8.5.1Test Purpose and Environment4308

A.7.5.8.5.1.2Test Requirements4310

A.7.5.9Uplink spatial relation switch delay4311

A.7.5.9.1.1.1Test Purpose and Environment4311

A.7.5.9.1.1.2Test Requirements4313

A.7.5.9.2RRC based spatial relation switch4313

A.7.5.9.2.1NR PCell FR2 spatial relation switch associated with a known DL-RS4313

A.7.5.9.2.1.1Test Purpose and Environment4313

A.7.5.9.2.1.2Test Requirements4315

A.7.5.10UE specific CBW change4315

A.7.5.10.1NR FR2 UE specific CBW change of PCell with non-DRX in SA4315

A.7.5.10.1.1Test Purpose and Environment4315

A.7.5.10.1.2Test Requirements4317

A.7.5.11UE UL carrier RRC reconfiguration Delay4318

A.7.5.11.1UE UL carrier RRC reconfiguration Delay4318

A.7.5.11.1.1Test Purpose and Environment4318

A.7.5.11.1.2Test Requirements4320

A.7.5.12Conditional PSCell addition and release delay (FR2 SA)4320

A.7.5.12.1Addition and Release Delay of PSCell4320

A.7.5.12.1.1Test purpose and environment4320

A.7.5.12.1.2Test Parameters4320

A.7.5.12.1.3Test Requirements4322

A.7.5.13Unified TCI state switching delay4322

A.7.5.13.1MAC-CE based active joint TCI state switching4322

A.7.5.13.1.1NR PCell FR2 active joint TCI state switch for a known TCI state4322

A.7.5.13.1.1.1Test Purpose and Environment4322

A.7.5.13.1.1.2Test parameters4323

A.7.5.13.1.1.3Test Requirements4324

A.7.5.13.2 MAC-CE based active uplink TCI state switch4325

A.7.5.13.2.1 NR FR2 PCell uplink TCI state switch for a known TCI state4325

A.7.5.13.2.1.1Test Purpose and Environment4325

A.7.5.13.2.1.2Test parameters4325

A.7.5.13.2.1.3Test Requirements4327

A.7.5.13.3MAC-CE based active downlink TCI state switch4327

A.7.5.13.3.1NR PCell FR2 active downlink TCI state switch to cell with additional PCI for a known TCI state4327

A.7.5.13.3.1.1Test Purpose and Environment4327

A.7.5.13.3.1.2Test Parameters4327

A.7.5.13.3.1.3Test Requirements4330

A.7.5.13.4sDCI MAC-CE based joint TCI state switching4331

A.7.5.13.4.1NR PCell FR2 dual downlink and uplink TCI state switch in sDCI for known case4331

A.7.5.13.4.1.1Test Purpose and Environment4331

A.7.5.13.4.1.2Test parameters4331

A.7.5.13.4.1.3Test Requirements4333

A.7.5.13.5MAC-CE based dual downlink TCI state switching delay for unified TCI for single-DCI mTRP4333

A.7.5.13.5.1NR PCell FR2 dual downlink TCI state switch in sDCI for known case4333

A.7.5.13.5.1.1Test Purpose and Environment4333

A.7.5.13.5.1.2Test Parameters4334

A.7.5.13.5.1.3Test Requirements4336

A.7.5.13.6 MAC-CE based active uplink TCI state switch for single-DCI mTRP4336

A.7.5.13.6.1 NR FR2 PCell uplink TCI state switch for two known TCI states4336

A.7.5.13.6.1.1Test Purpose and Environment4336

A.7.5.13.6.1.2Test parameters4337

A.7.5.13.6.1.3Test Requirements4338

A.7.5.14PSCell RACH-less based Activation and deactivation for FR1+FR2 inter-band with target PSCell in FR24338

A.7.5.14.1Test Purpose and Environment4338

A.7.5.14.2Test Requirements4341

A.7.5.15Void4341

A.7.5.16UE L1-RSRP Scheduling and Measurement Restrictions on FR2-14342

A.7.5.16.1Test Purpose and Environment4342

A.7.5.16.2Test Requirements4344

A.7.5.17SCG Activation and deactivation for FR1+FR1 inter-band with target PSCell in FR14345

A.7.5.17.1Test Purpose and Environment4345

A.7.5.17.2Test Requirements4347

A.7.5.18Subsequent conditional PSCell addition/change4348

A.7.5.18.1Intra-frequency subsequent CPC from FR1-FR2 NR-DC to FR1-FR2 NR-DC4348

A.7.5.18.1.1Test purpose and environment4348

A.7.5.18.1.2Test Requirements4351

A.7.5.18.2Inter-frequency subsequent CPA from FR1-FR2 NR-DC to FR1-FR2 NR-DC4352

A.7.5.18.2.1Test Purpose and Environment4352

A.7.5.18.2.2Test Requirements4354

A.7.6Measurement procedure4356

A.7.6.1Intra-frequency Measurements4356

A.7.6.1.1SA event triggered reporting test without gap under non-DRX4356

A.7.6.1.1.1Test purpose and Environment4356

A.7.6.1.1.2Test Requirements4358

A.7.6.1.2SA event triggered reporting test without gap under DRX4358

A.7.6.1.2.1Test purpose and Environment4358

A.7.6.1.2.2Test Requirements4360

A.7.6.1.3SA event triggered reporting test with per-UE gaps under non-DRX4360

A.7.6.1.3.1Test purpose and Environment4360

A.7.6.1.3.2Test Requirements4363

A.7.6.1.4SA event triggered reporting test with per-UE gaps under DRX4363

A.7.6.1.4.1Test purpose and Environment4363

A.7.6.1.4.2Test Requirements4365

A.7.6.1.5SA event triggered reporting test without gap under non-DRX for UE configured with highSpeedMeasFlagFR2-r174366

A.7.6.1.5.1Test purpose and Environment4366

A.7.6.1.5.2Test Requirements4368

A.7.6.1.6SA event triggered reporting test without gap under non-DRX for FR2-24368

A.7.6.1.6.1Test purpose and Environment4368

A.7.6.1.6.2Test Requirements4370

A.7.6.1.7SA event triggered reporting test without gap under DRX for FR2-24371

A.7.6.1.7.1Test purpose and Environment4371

A.7.6.1.7.2Test Requirements4373

A.7.6.1.8SA event triggered reporting test with per-UE gaps under non-DRX for FR2-24374

A.7.6.1.8.1Test purpose and Environment4374

A.7.6.1.8.2Test Requirements4376

A.7.6.1.9SA event triggered reporting test with per-UE gaps under DRX for FR2-24377

A.7.6.1.9.1Test purpose and Environment4377

A.7.6.1.9.2Test Requirements4379

A.7.6.1.10SA event triggered reporting test with SSB time index detection without gap under non-DRX for FR2-24380

A.7.6.1.10.1Test purpose and Environment4380

A.7.6.1.10.2Test Requirements4382

A.7.6.1.11SA event triggered reporting test with SSB time index detection with per-UE gaps under non-DRX for FR2-24382

A.7.6.1.11.1Test purpose and Environment4382

A.7.6.1.11.2Test Requirements4384

A.7.6.1.12SA event triggered reporting test without gap under non-DRX when CD-SSB is outside active BWP4385

A.7.6.1.12.1Test purpose and Environment4385

A.7.6.1.12.2Test Requirements4385

A.7.6.1.13SA event triggered reporting test without gap under non-DRX with NCD-SSB4385

A.7.6.1.13.1Test purpose and Environment4385

A.7.6.1.13.2Test Requirements4387

A.7.6.1.14SA event triggered reporting test without gap under non-DRX for power class 6 UE supporting measEnhCAInterFreqFR2-r184388

A.7.6.1.14.1Test Purpose and Environment4388

A.7.6.1.14.2Test Requirements4389

A.7.6.1.15SA event triggered reporting test without gap for SCell under non-DRX based on OD-SSB4389

A.7.6.1.15.1Test purpose and Environment4389

A.7.6.1.15.2Test Requirements4392

A.7.6.1.16SA event triggered reporting test without gap under non-DRX on deactivated SCell based on OD-SSB4392

A.7.6.1.16.1Test purpose and Environment4392

A.7.6.1.16.2Test Requirements4394

A.7.6.1.17SA event triggered reporting test under non-DRX on Rx BSF optimization for SSB based intra-frequency measurement without MG4394

A.7.6.1.17.1Test purpose and Environment4394

A.7.6.1.17.2Test Requirements4396

A.7.6.1.18SA event triggered reporting test with per-UE gaps under DRX for UE supporting multi-Rx based L3 measurement in FR24396

A.7.6.1.18.1Test purpose and Environment4396

A.7.6.1.18.2Test Requirements4398

A.7.6.1.19SA event triggered reporting test without gap under non-DRX for UE configured with cssf-Config4399

A.7.6.1.19.1Test purpose and Environment4399

A.7.6.1.19.2Test Requirements4401

A.7.6.2Inter-frequency Measurements4402

A.7.6.2.1SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (PCell in FR2)4402

A.7.6.2.1.1Test Purpose and Environment4402

A.7.6.2.1.2Test Requirements4404

A.7.6.2.2SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used (PCell in FR2)4404

A.7.6.2.2.1Test Purpose and Environment4404

A.7.6.2.2.2Test Requirements4406

A.7.6.2.3SA event triggered reporting tests for FR2 with SSB time index detection when DRX is not used (PCell in FR2)4407

A.7.6.2.3.1Test Purpose and Environment4407

A.7.6.2.3.2Test Requirements4409

A.7.6.2.4SA event triggered reporting tests for FR2 with SSB time index detection when DRX is used (PCell in FR2)4409

A.7.6.2.4.1Test Purpose and Environment4409

A.7.6.2.4.2Test Requirements4411

A.7.6.2.5SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (PCell in FR1)4412

A.7.6.2.5.1Test Purpose and Environment4412

A.7.6.2.5.2Test Requirements4414

A.7.6.2.6SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used (PCell in FR1)4415

A.7.6.2.6.1Test Purpose and Environment4415

A.7.6.2.6.2Test Requirements4417

A.7.6.2.7SA event triggered reporting tests for FR2 with SSB time index detection when DRX is not used (PCell in FR1)4418

A.7.6.2.7.1Test Purpose and Environment4418

A.7.6.2.7.2Test Requirements4420

A.7.6.2.8SA event triggered reporting tests for FR2 with SSB time index detection when DRX is used (PCell in FR1)4421

A.7.6.2.8.1Test Purpose and Environment4421

A.7.6.2.8.2Test Requirements4423

A.7.6.2.9SA event triggered reporting tests For FR2 without SSB time index detection when DRX is not used (PCell in FR2) (rel16 additional mandatory gap pattern 17)4424

A.7.6.2.9.1Test Purpose and Environment4424

A.7.6.2.9.2Test Requirements4426

A.7.6.2.10SA event triggered reporting test without gap under non-DRX4426

A.7.6.2.10.1Test Purpose and Environment4426

A.7.6.2.10.2Test Requirements4428

A.7.6.2.11SA event triggered reporting test without gap under DRX4428

A.7.6.2.11.1Test Purpose and Environment4428

A.7.6.2.11.2Test Requirements4430

A.7.6.2.12SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is not used (PCell in FR2-2)4430

A.7.6.2.12.1Test Purpose and Environment4430

A.7.6.2.12.2Test Requirements4433

A.7.6.2.13SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is used (PCell in FR2-2)4433

A.7.6.2.13.1Test Purpose and Environment4433

A.7.6.2.13.2Test Requirements4436

A.7.6.2.14SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is not used (PCell in FR2-2)4436

A.7.6.2.14.1Test Purpose and Environment4436

A.7.6.2.14.2Test Requirements4439

A.7.6.2.15SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is used (PCell in FR2-2)4439

A.7.6.2.15.1Test Purpose and Environment4439

A.7.6.2.15.2Test Requirements4442

A.7.6.2.16SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is not used (PCell in FR1)4443

A.7.6.2.16.1Test Purpose and Environment4443

A.7.6.2.16.2Test Requirements4447

A.7.6.2.17SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is used (PCell in FR1)4447

A.7.6.2.17.1Test Purpose and Environment4447

A.7.6.2.17.2Test Requirements4451

A.7.6.2.18SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is not used (PCell in FR1)4452

A.7.6.2.18.1Test Purpose and Environment4452

A.7.6.2.18.2Test Requirements4455

A.7.6.2.19SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is used (PCell in FR1)4456

A.7.6.2.19.1Test Purpose and Environment4456

A.7.6.2.19.2Test Requirements4460

A.7.6.2.20SA event triggered reporting tests for FR2 with measurement gap with priority and two periodic MUSIM gaps configured4461

A.7.6.2.20.1Test Purpose and Environment4461

A.7.6.2.20.2Test Requirements4463

A.7.6.2.21SA event triggered reporting tests for FR2 with measurement gap without priority and periodic MUSIM gap configured4463

A.7.6.2.21.1Test Purpose and Environment4463

A.7.6.2.21.2Test Requirements4465

A.7.6.2.22SA event triggered reporting tests with SSB time index detection when DRX is not used (PCell in FR2) for FR2 power class 6 UE configured with highSpeedMeasFlagFR2-r174466

A.7.6.2.22.1Test Purpose and Environment4466

A.7.6.2.22.2Test Requirements4468

A.7.6.2.23SA event triggered reporting tests without SSB time index detection when DRX is not used (PCell in FR2) for FR2 power class 6 UE configured with highSpeedMeasFlagFR2-r174468

A.7.6.2.23.1Test Purpose and Environment4468

A.7.6.2.23.2Test Requirements4470

A.7.6.2.24SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (FR1+FR2 CA and LTE+ FR2 EN-DC) for UE supporting [CSSF enhancement for one CC measurement per-band]4470

A.7.6.2.24.1Test Purpose and Environment4470

A.7.6.2.24.2Test Requirements4475

A.7.6.2.25SA event triggered reporting tests for FR2 under non-DRX in FR1+FR2 CA for UE supporting threeCarrierMeasWithoutGap-r194475

A.7.6.2.25.1Test purpose and Environment4475

A.7.6.2.25.2Test parameters4475

A.7.6.2.25.3Test Requirements4479

A.7.6.2.26SA event triggered reporting tests without gap under non-DRX in FR1+FR2 CA for UE supporting threeCarrierMeasWithoutGap-r194479

A.7.6.2.26.1Test purpose and Environment4479

A.7.6.2.26.2Test parameters4479

A.7.6.2.26.3Test Requirements4484

A.7.6.2.27SA serving cell quality triggered reporting tests for FR2 with SSB time index detection when DRX is used (PCell in FR2)4484

A.7.6.2.27.1Test Purpose and Environment4484

A.7.6.2.27.2Test Requirements4486

A.7.6.2.28SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used4487

A.7.6.2.28.1Test Purpose and Environment4487

A.7.6.2.28.2Test Requirements4488

A.7.6.3L1-RSRP measurement for beam reporting4488

A.7.6.3.1SSB based L1-RSRP measurement when DRX is not used4488

A.7.6.3.1.1Test Purpose and Environment4488

A.7.6.3.1.2Test parameters4488

A.7.6.3.1.3Test Requirements4490

A.7.6.3.2SSB based L1-RSRP measurement when DRX is used4490

A.7.6.3.2.1Test Purpose and Environment4490

A.7.6.3.2.2Test parameters4490

A.7.6.3.2.3Test Requirements4492

A.7.6.3.3CSI-RS based L1-RSRP measurement when DRX is not used4492

A.7.6.3.3.1Test Purpose and Environment4492

A.7.6.3.3.2Test parameters4492

A.7.6.3.3.3Test Requirements4494

A.7.6.3.4CSI-RS based L1-RSRP measurement when DRX is used4494

A.7.6.3.4.1Test Purpose and Environment4494

A.7.6.3.4.2Test parameters4494

A.7.6.3.3.3Test Requirements4496

A.7.6.3.5SSB based L1-RSRP measurement when DRX is used for power class 6 UE configured with highSpeedMeasFlagFR2-r174496

A.7.6.3.5.1Test Purpose and Environment4496

A.7.6.3.5.2Test parameters4496

A.7.6.3.5.3Test Requirements4498

A.7.6.3.6Inter-cell SSB based L1-RSRP measurements on FR2 SCell when DRX is not used4498

A.7.6.3.6.1Test Purpose and Environment4498

A.7.6.3.6.2Test parameters4498

A.7.6.3.6.3Test Requirements4501

A.7.6.3.7SSB based L1-RSRP measurement for FR2-2 when DRX is used4501

A.7.6.3.7.1Test Purpose and Environment4501

A.7.6.3.7.2Test parameters4502

A.7.6.3.7.3Test Requirements4503

A.7.6.3.8CSI-RS based L1-RSRP measurement when DRX is not used and when CD-SSB is outside active BWP4503

A.7.6.3.8.1Test Purpose and Environment4503

A.7.6.3.9SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP4504

A.7.6.3.9.1Test Purpose and Environment4504

A.7.6.3.9.2Test Requirements4504

A.7.6.3.10SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used4504

A.7.6.3.10.1Test Purpose and Environment4504

A.7.6.3.10.2Test parameters4504

A.7.6.3.10.3Test Requirements4506

A.7.6.3.11SSB based L1-RSRP measurement when DRX is used for power class 6 UE supporting simultaneousReceptionTwoQCL-r184506

A.7.6.3.11.1Test Purpose and Environment4506

A.7.6.3.11.2Test parameters4506

A.7.6.3.11.3Test Requirements4508

A.7.6.3.12SSB based L1-RSRP measurement when DRX is not used4508

A.7.6.3.12.1Test Purpose and Environment4508

A.7.6.3.12.2Test parameters4508

A.7.6.3.12.3Test Requirements4511

A.7.6.3.13Event Triggered Reporting for the UE initiated beam management4511

A.7.6.3.13.1Test Purpose and Environment4511

A.7.6.3.13.2Test parameters4511

A.7.6.3.13.3Test Requirements4513

A.7.6.3.14CSI-RS based UE-initiated/event-driven beam management of event24513

A.7.6.3.14.1Test Purpose and Environment4513

A.7.6.3.14.2Test parameters4513

A.7.6.3.14.3Test Requirements4515

A.7.6.3.15Event triggered reporting for UE initiated beam management for UE configured with Inter-cell SSB based L1-RSRP measurement on FR2 when DRX is not used4515

A.7.6.3.15.1Test Purpose and Environment4515

A.7.6.3.15.2Test parameters4515

A.7.6.3.15.3Test Requirements4518

A.7.6.3.16CSI-RS based L1-RSRP measurement when DRX is not used with SBFD4518

A.7.6.3.16.1Test Purpose and Environment4518

A.7.6.3.16.2Test parameters4518

A.7.6.3.16.3Test Requirements4520

A.7.6.4CLI measurements4520

A.7.6.4.1SRS-RSRP measurement with non-DRX4520

A.7.6.4.1.1Test Purpose and Environment4520

A.7.6.4.1.2Test Parameters4520

A.7.6.4.1.3Test Requirements4522

A.7.6.4.2CLI-RSSI measurement with non-DRX4522

A.7.6.4.2.1Test Purpose and Environment4522

A.7.6.4.2.2Test Parameters4522

A.7.6.4.2.3Test Requirements4524

A.7.6.5.1SA interfrequency CGI reporting in autonomous gaps test (PCell in FR2)4524

A.7.6.5.1.1Test Purpose and Environment4524

A.7.6.5.1.2Test Requirements4526

A.7.6.6L1-SINR measurement for beam reporting4526

A.7.6.6.2L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is used4528

A.7.6.6.2.1Test Purpose and Environment4528

A.7.6.6.2.2Test parameters4529

A.7.6.6.2.3Test Requirements4530

A.7.6.6.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is used4530

A.7.6.6.3.1Test Purpose and Environment4530

A.7.6.6.3.2Test parameters4530

A.7.6.6.3.3Test Requirements4532

A.7.6.6.4L1-SINR measurement with SSB based CMR and dedicated IMR with SBFD4532

A.7.6.6.4.1Test Purpose and Environment4532

A.7.6.6.4.2Test parameters4532

A.7.6.6.4.3Test Requirements4533

A.7.6.7CSI-RS based intra-frequency Measurements4534

A.7.6.7.1SA event triggered reporting test without gap under DRX for CSI-RS based intra-frequency measurement4534

A.7.6.7.1.1Test purpose and Environment4534

A.7.6.7.1.2Test Requirements4535

A.7.6.8CSI-RS based inter-frequency Measurements4536

A.7.6.8.1SA event triggered reporting tests for FR2 CSI-RS based measurement when non-DRX is used (PCell in FR2)4536

A.7.6.8.1.1Test Purpose and Environment4536

A.7.6.8.1.2Test Requirements4538

A.7.6.9RSTD measurements4538

A.7.6.9.1 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA4538

A.7.6.9.1.1Test Purpose and Environment4538

A.7.6.9.1.2Test Requirements4542

A.7.6.9.2 NR RSTD measurement reporting delay test case for dual positioning frequency layers in FR2 SA4542

A.7.6.9.2.1Test Purpose and Environment4542

A.7.6.9.2.2Test Requirements4545

A.7.6.9.3NR RSTD measurement reporting delay test case for single positioning frequency layer with reduced number of samples in FR2 SA4546

A.7.6.9.3.1Test Purpose and Environment4546

A.7.6.9.3.2Test Requirements4548

A.7.6.9.4NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA without measurement gap4549

A.7.6.9.4.1Test Purpose and Environment4549

A.7.6.9.4.2Test Requirements4551

A.7.6.9.5NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_CONNECTED state with Rx TEG4552

A.7.6.9.5.1Test Purpose and Environment4552

A.7.6.9.5.2Test Requirements4555

A.7.6.9.6NR RSTD measurement reporting delay test case for PRS aggregation in FR2 SA in RRC_CONNECTED mode4555

A.7.6.9.6.1Test Purpose and Environment4555

A.7.6.9.6.2Test Requirements4563

A.7.6.10 PRS-RSRP measurements4563

A.7.6.10.1 PRS-RSRP reporting delay test case for single positioning frequency layer4563

A.7.6.10.1.1Test Purpose and Environment4563

A.7.6.10.1.2Test Requirements4565

A.7.6.10.2PRS-RSRP reporting delay test case for dual positioning frequency layer4566

A.7.6.10.2.1Test Purpose and Environment4566

A.7.6.10.2.2Test Requirements4568

A.7.6.10.3PRS-RSRP reporting delay test case for reduced number of samples4568

A.7.6.10.3.1Test Purpose and Environment4568

A.7.6.10.3.2Test Requirements4570

A.7.6.10.4PRS-RSRP reporting delay test case for single positioning frequency layer outside MG4571

A.7.6.10.4.1Test Purpose and Environment4571

A.7.6.10.4.2Test Requirements4573

A.7.6.11UE Rx-Tx time difference measurements4573

A.7.6.11.1UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA4573

A.7.6.11.1.1Test purpose and environment4573

A.7.6.11.1.2Test requirements4575

A.7.6.11.2UE Rx-Tx time difference measurement period for dual positioning frequency layers in FR2 SA4575

A.7.6.11.2.1Test purpose and environment4575

A.7.6.11.2.2Test requirements4577

A.7.6.11.3UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA with reduced sample number4578

A.7.6.11.3.1Test purpose and environment4578

A.7.6.11.3.2Test requirements4579

A.7.6.11.4UE Rx-Tx time difference measurements without gaps in FR2 SA4580

A.7.6.11.4.1Test purpose and environment4580

A.7.6.11.4.2Test requirements4581

A.7.6.11.5UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA with RxTx TEG4582

A.7.6.11.5.1Test purpose and environment4582

A.7.6.11.5.2Test requirements4583

A.7.6.11.6UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR2 SA4584

A.7.6.11.6.1Test purpose and environment4584

A.7.6.11.6.2Test requirements4587

A.7.6.12PRS-RSRPP measurements4587

A.7.6.12.1 PRS-RSRPP reporting delay test case for single positioning frequency layer in FR2 in RRC_CONNECTED state4587

A.7.6.12.1.1Test Purpose and Environment4587

A.7.6.12.1.2Test Requirements4590

A.7.6.12.2PRS-RSRPP reporting delay test case for reduced number of samples for single positioning frequency layer in FR2 in RRC_CONNECTED state4590

A.7.6.12.2.1Test Purpose and Environment4590

A.7.6.12.2.2Test Requirements4592

A.7.6.12.3PRS-RSRPP reporting delay test case for gapless measurement in FR24593

A.7.6.12.3.1Test Purpose and Environment4593

A.7.6.12.3.2Test Requirements4595

A.7.6.13UE Rx-Tx time difference measurements for PDC4595

A.7.6.13.1UE Rx-Tx time difference measurement for propagation delay compensation using PRS in FR24595

A.7.6.13.1.1Test purpose and environment4595

A.7.6.13.1.2Test requirements4597

A.7.6.13.2UE Rx-Tx time difference measurement for propagation delay compensation using TRS in FR24597

A.7.6.13.2.1Test purpose and environment4597

A.7.6.13.2.2Test requirements4598

A.7.6.14SA event triggered reporting tests with Pre-MG4599

A.7.6.14.1Intra-frequency measurement test with SA event triggered reporting tests: with autonomous activation/deactivation of Pre-MG in FR24599

A.7.6.14.1.1Test purpose and Environment4599

A.7.6.14.1.2Test parameters4599

A.7.6.14.1.3Test Requirements4601

A.7.6.14.2Intra-frequency measurement test with SA event triggered reporting tests: with network-controlled activation/deactivation of Pre-MG in FR24601

A.7.6.14.2.1Test purpose and Environment4601

A.7.6.14.2.2Test parameters4601

A.7.6.14.2.3Test Requirements4603

A.7.6.15SA event triggered reporting tests with concurrent gaps4604

A.7.6.15.1SA event triggered reporting tests For FR2 with fully non-overlapping concurrent MGs for SSB-based inter-frequency measurements4604

A.7.6.15.1.1Test Purpose and Environment4604

A.7.6.15.1.2Test Requirements4606

A.7.6.15.2SA event triggered reporting tests For FR2 with concurrent measurement gaps without SSB time index detection when DRX is not used (PCell in FR2)4606

A.7.6.15.2.1Test Purpose and Environment4606

A.7.6.15.2.2Test Requirements4609

A.7.6.15.3SA event triggered reporting tests for FR2 concurrent gap with partially partial overlapping scenario for SSB-based measurements and PRS-based measurement4609

A.7.6.15.3.1Test Purpose and Environment4609

A.7.6.15.3.2Test Requirements4611

A.7.6.16SA event triggered reporting tests with NCSG4612

A.7.6.16.1SA event triggered reporting test with per-UE NCSG under non-DRX4612

A.7.6.16.1.1Test purpose and Environment4612

A.7.6.16.1.2Test Requirements4614

A.7.6.16.2SA event triggered reporting tests on inter-frequency measurement with NCSG for FR2 when DRX is not used (PCell in FR2)4615

A.7.6.16.2.1Test Purpose and Environment4615

A.7.6.16.2.2Test Requirements4617

A.7.6.16.3Event triggered reporting test on deactivated SCell measurement via NCSG in FR2 in non-DRX4617

A.7.6.16.3.1Test Purpose and Environment4617

A.7.6.16.3.2Test Requirements4619

A.7.6.17SA event triggered reporting tests for concurrent measurement gaps with Pre-MG in FR24620

A.7.6.17.1SA event triggered reporting test for FR2 with one pre-configured gap and one measurement gap4620

A.7.6.17.1.1Test Purpose and Environment4620

A.7.6.17.1.2Test Requirements4622

A.7.6.17.2Inter-frequency measurement test with SA event triggered reporting tests: with autonomous activation/deactivation of Pre-MGs in FR24623

A.7.6.17.2.1Test purpose and Environment4623

A.7.6.17.2.2Test parameters4623

A.7.6.17.2.3Test Requirements4625

A.7.6.18SA event triggered reporting tests with concurrent gaps and NCSG4626

A.7.6.18.1SA event triggered reporting tests For FR2 with concurrent measurement gaps and NCSG without SSB time index detection when DRX is not used (PCell in FR2)4626

A.7.6.18.1.1Test Purpose and Environment4626

A.7.6.18.1.2Test Requirements4628

A.7.6.19SA event triggered reporting tests with NeedForGap in FR24629

A.7.6.19.1SA event triggered reporting test for UE indicating NeedforInterruptionInfoNR under non-DRX and no interruption outside configured measurement gaps4629

A.7.6.19.1.1Test purpose and Environment4629

A.7.6.19.1.2Test Requirements4631

A.7.6.19.2SA event triggered reporting test without gap under non-DRX4631

A.7.6.19.2.1Test purpose and Environment4631

A.7.6.19.2.2Test Requirements4633

A.7.6.19.3SA event triggered reporting test without gap without interruption under non-DRX4634

A.7.6.19.3.1Test Purpose and Environment4634

A.7.6.19.3.2Test Requirements4636

A.7.6.20LTM Intra-frequency L1-RSRP measurement4636

A.7.6.20.1Intra-frequency SSB based L1-RSRP measurement in FR24636

A.7.6.20.1.1Test Purpose and Environment4636

A.7.6.20.1.2Test parameters4637

A.7.6.20.1.3Test Requirements4639

A.7.6.20.2Intra-frequency SSB based L1-RSRP measurement in FR2 with event triggered reporting4639

A.7.6.20.2.1Test Purpose and Environment4639

A.7.6.20.2.2Test parameters4639

A.7.6.20.2.3Test Requirements4640

A.7.6.20.3CSI-RS based L1-RSRP intra-frequency measurement for neighbour cell in FR2 without SSB based L1-RSRP measurement4640

A.7.6.20.3.1Test purpose and Environment4640

A.7.6.20.3.2Test parameters4640

A.7.6.20.3.3Test Requirements4642

A.7.6.20.4Intra-frequency CSI-RS based L1-RSRP measurement in FR24643

A.7.6.20.4.1Test Purpose and Environment4643

A.7.6.20.4.3Test Requirements4645

A.7.6.21LTM Inter-frequency L1-RSRP measurement with measurement gap4646

A.7.6.21.1Inter-frequency SSB-based L1-RSRP measurement with measurement gap for LTM in FR24646

A.7.6.21.1.1Test Purpose and Environment4646

A.7.6.21.1.2Test parameters4646

A.7.6.21.1.3Test Requirements4648

A.7.6.21.2Inter-frequency SSB-based L1-RSRP measurement with measurement gap in FR2 with event triggered reporting4648

A.7.6.21.2.3Test Requirements4649

A.7.6.22LTM Inter-frequency L1-RSRP measurement without measurement gap4649

A.7.6.22.1Inter-frequency SSB based L1-RSRP measurement without measurement gap in FR24649

A.7.6.22.1.1Test Purpose and Environment4649

A.7.6.22.1.2Test parameters4649

A.7.6.22.1.3Test Requirements4651

A.7.6.23Idle Mode CA/DC Measurements4652

A.7.6.23.1Test case for Idle mode fast CA/DC eEMR measurement for FR2 without valid reporting4652

A.7.6.23.1.1Test Purpose and Environment4652

A.7.6.23.1.2Test Requirements4655

A.7.6.23.2Test case for Idle mode fast CA/DC cell reselection measurement for FR2 without valid reporting4655

A.7.6.23.2.1Test Purpose and Environment4655

A.7.6.23.2.2Test Requirements4658

A.7.6.23.3 Test case for Idle mode fast CA/DC cell reselection measurement for FR2 with valid reporting4659

A.7.6.23.3.1Test Purpose and Environment4659

A.7.6.23.3.2Test Requirements4662

A.7.6.24RSCPD measurements4662

A.7.6.24.1NR RSCPD with RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_CONNECTED state4662

A.7.6.24.1.1Test Purpose and Environment4662

A.7.6.24.1.2Test Requirements4670

A.7.6.25RSCP measurements4670

A.7.6.25.1DL RSCP with UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA4670

A.7.6.25.1.1Test purpose and environment4670

A.7.6.25.1.2Test requirements4674

A.7.6.26Inter-RAT Measurements4674

A.7.6.26.1SA event triggered reporting test without gap under non-DRX for UE configured with [MeasuringoneCCperFR2band] in FR2 inter-band CA4674

A.7.6.26.1.1Test purpose and Environment4674

A.7.6.26.1.2Test Requirements4676

A.7.6.27L1 CLI measurements4677

A.7.6.27.1L1-SRS-RSRP measurement with DRX with SBFD4677

A.7.6.27.1.1Test Purpose and Environment4677

A.7.6.27.1.2Test Parameters4677

A.7.6.27.1.3Test Requirements4679

A.7.6.27.2L1-CLI-RSSI measurement with DRX with SBFD4679

A.7.6.27.2.1Test Purpose and Environment4679

A.7.6.27.2.2Test Parameters4679

A.7.6.27.2.3Test Requirements4681

A.7.6.28LTM Inter-frequency L1-RSRP event triggered reporting without measurement gap4681

A.7.6.28.1Inter-frequency SSB based L1-RSRP measurement without measurement gap in FR24681

A.7.6.28.1.1Test Purpose and Environment4681

A.7.6.28.1.2Test parameters4681

A.7.6.28.1.3Test Requirements4682

A.7.6.29LTM Inter-frequency L1-RSRP measurement with measurement gap cancellation4682

A.7.6.29.1Inter-frequency SSB-based L1-RSRP measurement with measurement gap cancellation for LTM in FR24682

A.7.6.29.1.1Test Purpose and Environment4682

A.7.6.29.1.2Test parameters4682

A.7.6.29.1.3Test Requirements4683

A.7.6.30DL AI/ML positioning reporting delay test case for single positioning frequency layer in FR2 SA4683

A.7.6.30.1Test Purpose and Environment4683

A.7.6.30.2Test Requirements4686

A.7.7Measurement Performance requirements4686

A.7.7.1SS-RSRP4686

A.7.7.1.1SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell4686

A.7.7.1.1.1Test Purpose and Environment4687

A.7.7.1.1.2Test parameters4687

A.7.7.1.1.3Test Requirements4688

A.7.7.1.2SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell4689

A.7.7.1.2.1Test Purpose and Environment4689

A.7.7.1.2.2Test parameters4689

A.7.7.1.2.3Test Requirements4691

A.7.7.1.3SA inter-frequency measurement accuracy with FR1 serving cell and FR2 target cell4692

A.7.7.1.3.1Test Purpose and Environment4692

A.7.7.1.3.2Test parameters4692

A.7.7.1.3.3Test Requirements4694

A.7.7.2SS-RSRQ4695

A.7.7.2.1SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell4695

A.7.7.2.1.1Test Purpose and Environment4695

A.7.7.2.1.2Test Parameters4695

A.7.7.2.1.3Test Requirements4696

A.7.7.2.2SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell4697

A.7.7.2.2.1Test Purpose and Environment4697

A.7.7.2.2.2Test Parameters4697

A.7.7.2.2.3Test Requirements4698

A.7.7.3SS-SINR4698

A.7.7.3.1SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell4698

A.7.7.3.1.1Test Purpose and Environment4698

A.7.7.3.1.2Test Parameters4698

A.7.7.3.1.3Test Requirements4700

A.7.7.3.2SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell4700

A.7.7.3.2.1Test Purpose and Environment4700

A.7.7.3.2.2Test Parameters4700

A.7.7.3.2.3Test Requirements4701

A.7.7.4L1-RSRP measurement for beam reporting4702

A.7.7.4.1SSB based L1-RSRP measurement4702

A.7.7.4.1.1Test Purpose and Environment4702

A.7.7.4.1.2Test parameters4702

A.7.7.4.1.3Test Requirements4703

A.7.7.4.2CSI-RS based L1-RSRP measurement on resource set with repetition off4704

A.7.7.4.2.1Test Purpose and Environment4704

A.7.7.4.2.2Test parameters4704

A.7.7.4.2.3Test Requirements4705

A.7.7.4.3CSI-RS based L1-RSRP measurement with SBFD DUD4706

A.7.7.4.3.1Test Purpose and Environment4706

A.7.7.4.3.2Test parameters4706

A.7.7.4.3.3Test Requirements4707

A.7.7.4.4CSI-RS based L1-RSRP measurement with SBFD DU4708

A.7.7.4.4.1Test Purpose and Environment4708

A.7.7.4.4.2Test parameters4708

A.7.7.4.4.3Test Requirements4709

A.7.7.5CLI measurements4710

A.7.7.5.1SA SRS-RSRP measurement accuracy with FR2 serving cell4710

A.7.7.5.1.1Test Purpose and Environment4710

A.7.7.5.1.2Test parameters4710

A.7.7.5.1.3Test Requirements4712

A.7.7.5.2SA CLI-RSSI measurement accuracy with FR2 serving cell4712

A.7.7.5.2.1Test Purpose and Environment4712

A.7.7.5.2.2Test parameters4712

A.7.7.5.2.3Test Requirements4714

A.7.7.6L1-SINR measurement for beam reporting4714

A.7.7.6.1.1Test Purpose and Environment4714

A.7.7.6.1.2Test parameters4715

A.7.7.6.1.3Test Requirements4716

A.7.7.6.2L1-SINR measurement with SSB based CMR and dedicated IMR4716

A.7.7.6.2.1Test Purpose and Environment4716

A.7.7.6.2.2Test parameters4717

A.7.7.6.2.3Test Requirements4718

A.7.7.6.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR4718

A.7.7.6.3.1Test Purpose and Environment4718

A.7.7.6.3.2Test parameters4719

A.7.7.6.3.3Test Requirements4720

A.7.7.7CSI-RSRP4720

A.7.7.7.1SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell4720

A.7.7.7.1.1Test Purpose and Environment4720

A.7.7.7.1.2Test parameters4721

A.7.7.7.1.3Test Requirements4722

A.7.7.7.2SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell4723

A.7.7.7.2.1Test Purpose and Environment4723

A.7.7.7.2.2Test parameters4723

A.7.7.7.2.3Test Requirements4725

A.7.7.8CSI-RSRQ4726

A.7.7.8.1SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell4726

A.7.7.8.1.1Test Purpose and Environment4726

A.7.7.8.1.2Test Parameters4726

A.7.7.8.1.3Test Requirements4727

A.7.7.8.2SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell4727

A.7.7.8.2.1Test Purpose and Environment4727

A.7.7.8.2.2Test Parameters4728

A.7.7.8.2.3Test Requirements4729

A.7.7.9CSI-SINR4729

A.7.7.9.1SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell4729

A.7.7.9.1.1Test Purpose and Environment4729

A.7.7.9.1.2Test Parameters4729

A.7.7.9.1.3Test Requirements4731

A.7.7.9.2SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell4731

A.7.7.9.2.1Test Purpose and Environment4731

A.7.7.9.2.2Test Parameters4731

A.7.7.9.2.3Test Requirements4733

A.7.7.10RSTD measurements4733

A.7.7.10.1RSTD measurement accuracy test case for single positioning frequency layer4733

A.7.7.10.1.1Test purpose and Environment4733

A.7.7.10.1.2Test Requirements4734

A.7.7.10.2RSTD measurement accuracy test case for dual positioning frequency layer4735

A.7.7.10.2.1Test purpose and Environment4735

A.7.7.10.2.2Test Requirements4736

A.7.7.10.3RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR2 in RRC_CONNECTED state4736

A.7.7.10.3.1Test purpose and Environment4736

A.7.7.10.3.2Test Requirements4738

A.7.7.10.4RSTD measurement accuracy test case with Rx TEG4738

A.7.7.10.4.1Test purpose and Environment4738

A.7.7.10.4.2Test Requirements4740

A.7.7.10.5NR RSTD measurement accuracy test case for PRS aggregation in FR2 SA in RRC_CONNECTED mode4740

A.7.7.10.5.1Test purpose and Environment4740

A.7.7.10.5.2Test Requirements4742

A.7.7.11PRS-RSRP measurements4742

A.7.7.11.1SA measurement accuracy with PRS in FR24742

A.7.7.11.1.1Test Purpose and Environment4742

A.7.7.11.1.2Test parameters4742

A.7.7.11.1.3Test Requirements4744

A.7.7.11.2SA measurement accuracy with PRS in FR2 with reduced sample number4744

A.7.7.11.2.1Test Purpose and Environment4744

A.7.7.11.2.2Test parameters4744

A.7.7.11.2.3Test Requirements4746

A.7.7.12UE Rx-Tx time difference measurements4746

A.7.7.12.1UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR2 SA4746

A.7.7.12.1.1Test purpose and environment4746

A.7.7.12.1.2Test parameters4747

A.7.7.12.1.3Test requirements4748

A.7.7.12.2UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR2 SA4748

A.7.7.12.2.1Test purpose and environment4749

A.7.7.12.2.2Test parameters4749

A.7.7.12.2.3Test requirements4750

A.7.7.12.3UE Rx-Tx time difference measurement accuracy with RxTx TEG4750

A.7.7.12.3.1Test purpose and environment4750

A.7.7.12.3.2Test parameters4751

A.7.7.12.3.3Test requirements4752

A.7.7.12.4UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR2 SA4753

A.7.7.12.4.1Test purpose and environment4753

A.7.7.12.4.2Test requirements4757

A.7.7.13PRS-RSRPP measurements4757

A.7.7.13.1SA measurement accuracy with PRS in FR24757

A.7.7.13.1.1Test Purpose and Environment4757

A.7.7.13.1.2Test parameters4757

A.7.7.13.1.3Test Requirements4759

A.7.7.13.2SA measurement accuracy with reduced PRS samples in FR24759

A.7.7.13.2.1Test Purpose and Environment4759

A.7.7.13.2.2Test parameters4759

A.7.7.13.2.3Test Requirements4761

A.7.7.14L1-RSRP measurement for group-based beam reporting4761

A.7.7.14.1SSB based L1-RSRP measurement4761

A.7.7.14.1.1Test Purpose and Environment4761

A.7.7.14.1.2Test parameters4761

A.7.7.14.1.3Test Requirements4763

A.7.7.14.2CSI-RS based L1-RSRP measurement on resource set with repetition off4763

A.7.7.14.2.1Test Purpose and Environment4763

A.7.7.14.2.2Test parameters4763

A.7.7.14.2.3Test Requirements4765

A.7.7.15LTM L1-RSRP measurement4765

A.7.7.15.1SSB based inter-frequency L1-RSRP measurement4765

A.7.7.15.1.1Test Purpose and Environment4765

A.7.7.15.1.2Test parameters4766

A.7.7.15.1.3Test Requirements4767

A.7.7.15.2CSI-RS based L1-RSRP measurement on resource set with repetition off4768

A.7.7.15.2.1Test Purpose and Environment4768

A.7.7.15.2.2Test parameters4768

A.7.7.15.2.3Test Requirements4770

A.7.7.16RSCPD Measurements4770

A.7.7.16.1RSCPD with RSTD measurement accuracy in FR2 SA in RRC_CONNECTED4770

A.7.7.16.1.1Test purpose and environment4770

A.7.7.16.1.2Test parameters4771

A.7.7.16.1.3Test requirements4772

A.7.7.17RSCP with UE Rx-Tx time difference measurements4772

A.7.7.17.1RSCP with UE Rx-Tx time difference measurement accuracy in FR2 SA4772

A.7.7.17.1.1Test purpose and environment4772

A.7.7.17.1.2Test parameters4773

A.7.7.17.1.3Test requirements4776

A.7.7.18L1 CLI measurements4776

A.7.7.18.1SA L1-SRS-RSRP measurement accuracy with FR2 serving cell with SBFD4776

A.7.7.18.1.1Test Purpose and Environment4776

A.7.7.18.1.2Test parameters4776

A.7.7.18.1.3Test Requirements4778

A.7.7.18.2L1-CLI-RSSI measurement accuracy in FR2 with SBFD4778

A.7.7.18.2.1Test Purpose and Environment4778

A.7.7.18.2.2Test parameters4779

A.7.7.18.2.3Test Requirements4780

A.7.8Measurement procedure in RRC_INACTIVE4780

A.7.8.1RSTD measurements4780

A.7.8.1.1NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state4780

A.7.8.1.1.1Test Purpose and Environment4780

A.7.8.1.1.2Test Requirements4783

A.7.8.1.2NR RSTD measurement reporting delay test case with reduced number of samples in RRC_INACTIVE, FR1 SA4784

A.7.8.1.2.1Test Purpose and Environment4784

A.7.8.1.2.2Test Requirements4786

A.7.8.1.3NR RSTD measurement reporting delay test case for PRS aggregation in FR2 SA in RRC_INACTIVE state4787

A.7.8.1.3.1Test purpose and environment4787

A.7.8.1.3.2Test requirements4790

A.7.8.1.4NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state with eDRX > 10.24s4790

A.7.8.1.4.1Test purpose and environment4790

A.7.8.1.4.2Test requirements4794

A.7.8.2PRS-RSRP measurements4794

A.7.8.2.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_INACTIVE4794

A.7.8.2.1.1Test Purpose and Environment4794

A.7.8.2.1.2Test Requirements4796

A.7.8.2.2PRS-RSRP reporting delay test case with reduced number of samples in RRC_INACTIVE4797

A.7.8.2.2.1Test purpose and Environment4797

A.7.8.2.2.2Test Requirements4799

A.7.8.2.3PRS-RSRP reporting delay in RRC_INACTIVE with eDRX4799

A.7.8.2.3.1Test Purpose and Environment4799

A.7.8.2.3.2Test Requirements4803

A.7.8.3UE Rx-Tx time difference measurements4803

A.7.8.3.1UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA4803

A.7.8.3.1.1Test purpose and environment4803

A.7.8.3.1.2Test requirements4805

A.7.8.3.2UE Rx-Tx time difference measurement with reduced number of samples in RRC_INACTIVE, FR2 SA4805

A.7.8.3.2.1Test purpose and environment4805

A.7.8.3.2.2Test requirements4807

A.7.8.3.3UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR2 SA4807

A.7.8.3.3.1Test purpose and environment4807

A.7.8.3.3.2Test requirements4810

A.7.8.3.4UE Rx-Tx time difference measurements for single positioning frequency layer with eDRX > 10.24s in FR2 SA4810

A.7.8.3.4.1Test purpose and environment4810

A.7.8.3.4.2Test requirements4813

A.7.8.4PRS-RSRPP measurements4813

A.7.8.4.1PRS-RSRPP reporting delay test case for single positioning frequency layer in FR2 in RRC_INACTIVE state4813

A.7.8.4.1.1Test Purpose and Environment4813

A.7.8.4.1.2Test Requirements4816

A.7.8.4.2PRS-RSRPP reporting delay test with reduced number of samples for single positioning frequency layer in FR2 in RRC_INACTIVE state4816

A.7.8.4.2.1Test Purpose and Environment4816

A.7.8.4.2.2Test Requirements4818

A.7.8.4.3PRS-RSPP reporting delay in RRC_INACTIVE state with eDRX > 10.24s in FR24819

A.7.8.4.3.1Test purpose and environment4819

A.7.8.4.3.2Test requirements4822

A.7.8.5RSCPD Measurements4822

A.7.8.5.1DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state4822

A.7.8.5.1.1Test Purpose and Environment4822

A.7.8.5.1.2Test Requirements4823

A.7.8.6RSCP Measurements4823

A.7.8.6.1DL RSCP with UE Rx-Tx time difference measurements in RRC_INACTIVE for single positioning frequency layer in FR2 SA4823

A.7.8.6.1.1Test purpose and environment4823

A.7.8.6.1.2Test requirements4827

A.7.9Measurement performance requirements in RRC_INACTIVE4827

A.7.9.1RSTD measurements4827

A.7.9.1.1RSTD measurement accuracy test case for single positioning frequency layer in FR2 in RRC_INACTIVE state4827

A.7.9.1.1.1Test purpose and Environment4827

A.7.9.1.1.2Test Requirements4829

A.7.9.1.2RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR2 in RRC_INACTIVE state4829

A.7.9.1.2.1Test purpose and Environment4829

A.7.9.1.2.2Test Requirements4831

A.7.9.2PRS-RSRP measurements4833

A.7.9.2.1SA measurement accuracy with PRS in FR2 in RRC_INACTIVE4833

A.7.9.2.1.1Test Purpose and Environment4833

A.7.9.2.1.2Test parameters4833

A.7.9.2.1.3Test Requirements4834

A.7.9.2.2PRS-RSRP measurements with reduced number of sample in RRC_INACTIVE4835

A.7.9.2.2.1Test Purpose and Environment4835

A.7.9.2.2.2Test parameters4835

A.7.9.2.2.3Test Requirements4836

A.7.9.3UE Rx-Tx time difference measurements4837

A.7.9.3.1UE Rx-Tx time difference measurements in RRC_INACTIVE4837

A.7.9.3.1.1Test purpose and environment4837

A.7.9.3.1.2Test parameters4837

A.7.9.3.1.3Test requirements4838

A.7.9.3.2UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR2 SA4838

A.7.9.3.2.1Test purpose and environment4838

A.7.9.3.2.2Test parameters4839

A.7.9.3.2.3Test requirements4840

A.7.9.3.3UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR2 SA in RRC_INACTIVE state4840

A.7.9.3.3.1Test purpose and environment4840

A.7.9.3.3.2Test requirements4844

A.7.9.4PRS-RSRPP measurements4844

A.7.9.4.1SA measurement accuracy in FR2 in RRC INACTIVE4844

A.7.9.4.1.1Test Purpose and Environment4844

A.7.9.4.1.2Test parameters4844

A.7.9.4.1.3Test Requirements4846

A.7.9.4.2SA measurement accuracy with reduced PRS samples in FR2 in RRC INACTIVE4846

A.7.9.4.2.1Test Purpose and Environment4846

A.7.9.4.2.2Test parameters4846

A.7.9.4.2.3Test Requirements4848

A.7.9.5RSCPD Measurements4848

A.7.9.5.1RSCPD with RSTD measurement accuracy in FR2 SA in RRC_INACTIVE4848

A.7.9.5.1.1Test purpose and environment4848

A.7.9.5.1.2Test parameters4848

A.7.9.5.1.3Test requirements4850

A.7.9.6RSCP Measurements4850

A.7.9.6.1RSCP with UE Rx-Tx time difference measurement accuracy in FR2 SA4850

A.7.9.6.1.1Test purpose and environment4850

A.7.9.6.1.2Test parameters4851

A.7.9.6.1.3Test requirements4852

A.7.10Measurement Procedure in RRC_IDLE4852

A.7.10.1RSTD Measurements4852

A.7.10.1.1NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_IDLE state for non-RedCap UE4852

A.7.10.1.1.1Test purpose and environment4852

A.7.10.1.1.2Test requirements4855

A.7.10.1.2NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s4855

A.7.10.1.2.1Test purpose and environment4855

A.7.10.1.2.2Test requirements4858

A.7.10.1.3NR RSTD measurement reporting delay test case for PRS aggregation in FR2 SA in RRC_IDLE state4858

A.7.10.1.3.1Test purpose and environment4858

A.7.10.1.3.2Test requirements4859

A.7.10.2PRS-RSRP Measurements4859

A.7.10.2.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_IDLE state for non-RedCap UE in FR24859

A.7.10.2.1.1Test Purpose and Environment4859

A.7.10.2.1.2Test Requirements4863

A.7.10.2.2PRS-RSRP reporting delay test case in RRC_IDLE state in FR2 when eDRX cycle > 10.24s4863

A.7.10.2.2.1Test Purpose and Environment4863

A.7.10.2.2.2Test Requirements4863

A.7.10.3RSCPD Measurements4864

A.7.10.3.1DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_IDLE state4864

A.7.10.3.1.1Test Purpose and Environment4864

A.7.10.3.1.2Test Requirements4864

A.7.11Measurement Performance Requirements in RRC_IDLE4865

A.7.11.1RSTD Measurements4865

A.7.11.1.1NR RSTD measurement accuracy test case for single positioning frequency layer in FR2 SA in RRC_IDLE state for non-RedCap UE4865

A.7.11.1.1.1Test purpose and environment4865

A.7.11.1.1.2Test requirements4866

A.7.11.1.2RSTD measurement accuracy test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s4867

A.7.11.1.2.1Test purpose and environment4867

A.7.11.1.2.2Test requirements4868

A.7.11.1.3NR RSTD measurement accuracy test case for PRS aggregation in FR2 SA in RRC_IDLE state4869

A.7.11.1.3.1Test purpose and environment4869

A.7.11.1.3.2Test requirements4869

A.7.11.2PRS-RSRP measurements4869

A.7.11.2.1PRS-RSRP measurement accuracy test case for non-RedCap UE in FR2 in RRC_IDLE state4869

A.7.11.2.1.1Test Purpose and Environment4869

A.7.11.2.1.2Test parameters4869

A.7.11.2.1.3Test Requirements4871

A.7.11.2.2PRS-RSRP measurement accuracy test case in RRC_IDLE state in FR2 for case 2 when eDRX cycle > 10.24s4871

A.7.11.2.2.1Test purpose and Environment4871

A.7.11.2.2.1Test parameters4872

A.7.11.2.2.2Test Requirements4872

A.7.11.3RSCPD measurements4872

A.7.11.3.1RSCPD with RSTD measurement accuracy in FR2 SA in RRC_IDLE4872

A.7.11.3.1.1Test purpose and environment4872

A.7.11.3.1.2Test parameters4872

A.7.11.3.1.3Test requirements4874

A.8E-UTRA standalone tests for NR RRM4875

A.8.1Void4875

A.8.2RRC_IDLE state mobility4875

A.8.2.1Inter-RAT NR Cell re-selection4875

A.8.2.1.1E-UTRA Cell reselection to higher priority NR target Cell in FR14875

A.8.2.1.1.1Test Purpose and Environment4875

A.8.2.1.1.2Test Requirements4878

A.8.2.1.2E-UTRA Cell reselection to lower priority NR target Cell in FR1 for UE configured with highSpeedInterRAT-NR-r164878

A.8.2.1.2.1Test Purpose and Environment4878

A.8.2.1.2.2Test Requirements4881

A.8.2.2E-UTRA – NR Inter-RAT Early Measruement Reporting4882

A.8.2.2.1E-UTRA – NR Early Measurement Reporting for NR in FR14882

A.8.2.2.1.1Test Purpose and Environment4882

A.8.2.2.1.2Test Requirements4884

A.8.2.2.2E-UTRA – NR Early Measurement Reporting for NR in FR24885

A.8.2.2.2.1Test Purpose and Environment4885

A.8.2.2.2.2Test Requirements4887

A.8.3RRC_CONNECTED state mobility4887

A.8.3.1Handover4887

A.8.3.1.1E-UTRAN - NR handover in FR14887

A.8.3.1.1.1Test Purpose and Environment4887

A.8.3.1.1.2Test Requirements4891

A.8.4Measurement procedure4891

A.8.4.1E-UTRA – NR Inter-RAT SFTD Measurement Delay4891

A.8.4.1.1E-UTRA – NR Inter-RAT SFTD Measurement Delay in non-DRX4891

A.8.4.1.1.1Test Purpose and Environment4891

A.8.4.1.1.2Test Requirements4893

A.8.4.1.2E-UTRA – NR Inter-RAT SFTD Measurement Delay in DRX4893

A.8.4.1.2.1Test Purpose and Environment4893

A.8.4.1.2.2Test Requirements4894

A.8.4.2E-UTRA – NR Inter-RAT Measurements4894

A.8.4.2.1NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used4894

A.8.4.2.1.1Test Purpose and Environment4894

A.8.4.2.1.2Test Requirements4897

A.8.4.2.2NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used4897

A.8.4.2.2.1Test Purpose and Environment4897

A.8.4.2.2.2Test Requirements4900

A.8.4.2.3NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used4901

A.8.4.2.3.1Test Purpose and Environment4901

A.8.4.2.3.2Test Requirements4904

A.8.4.2.4NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used4904

A.8.4.2.4.1Test Purpose and Environment4904

A.8.4.2.4.2Test Requirements4907

A.8.4.2.5NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is not used4907

A.8.4.2.5.1Test Purpose and Environment4907

A.8.4.2.5.2Test Requirements4909

A.8.4.2.6NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is used4910

A.8.4.2.6.1Test Purpose and Environment4910

A.8.4.2.6.2Test Requirements4911

A.8.4.2.7NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is not used4912

A.8.4.2.7.1Test Purpose and Environment4912

A.8.4.2.7.2Test Requirements4914

A.8.4.2.8NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is used4914

A.8.4.2.8.1Test Purpose and Environment4914

A.8.4.2.8.2Test Requirements4916

A.8.4.2.9NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection in DRX for UE configured with highSpeedInterRAT-NR-r164916

A.8.4.2.9.1Test Purpose and Environment4916

A.8.4.2.9.2Test Requirements4919

A.8.4.3E-UTRAN - NR Inter-RAT event-triggered without measurement gaps4920

A.8.4.3.1NR Inter-RAT event triggered reporting tests for FR2 without MG nor DRX4920

A.8.4.3.1.1Test Purpose and Environment4920

A.8.4.3.1.2Test Requirements4921

A.8.4.3.2NR Inter-RAT event triggered reporting tests for FR1 without gaps when DRX is not used4922

A.8.4.3.2.1Test Purpose and Environment4922

A.8.4.3.2.2Test Requirements4925

A.8.5Measurement performance4925

A.8.5.1SFTD accuracy4925

A.8.5.1.1SFTD accuracy4925

A.8.5.1.1.1Test Purpose4925

A.8.5.1.1.2Test Environment4925

A.8.5.1.1.3Test Requirements4929

A.8.5.2E-UTRA – NR Inter-RAT Measurement Performance requirements4929

A.8.5.2.1.1E-UTRAN – NR inter-RAT measurements with FR1 target cell4929

A.8.5.2.1.2E-UTRAN – NR inter-RAT measurements with FR2 target cell4932

A.8.5.2.1.2.1Test Purpose and Environment4932

A.8.5.2.1.2.2Test Parameters4932

A.8.5.2.1.2.3Test Requirements4934

A.8.5.2.2SS-RSRQ4934

A.8.5.2.2.1E-UTRAN – NR inter-RAT measurements with FR1 target cell4934

A.8.5.2.2.2E-UTRAN – NR inter-RAT measurements with FR2 target cell4937

A.8.5.2.2.2.1Test Purpose and Environment4937

A.8.5.2.2.2.2Test Parameters4937

A.8.5.2.2.2.3Test Requirements4939

A.8.5.2.3SS-SINR4939

A.8.5.2.3.1E-UTRAN – NR inter-RAT measurements with FR1 target cell4939

A.8.5.2.3.2E-UTRAN – NR inter-RAT measurements with FR2 target cell4942

A.8.5.2.3.2.1Test Purpose and Environment4942

A.8.5.2.3.2.2Test Parameters4943

A.8.5.2.3.2.3Test Requirements4944

A.9V2X Tests4944

A.9.1V2X Tests in FR14944

A.9.1.1Test for V2X UE Transmit Timing4944

A.9.1.1.1 Test for GNSS as Synchronization Reference Source4944

A.9.1.1.1.1Test Purpose and Environment4944

A.9.1.1.1.2Test requirements4945

A.9.1.1.2Test for SyncRef UE as Synchronization Reference Source4945

A.9.1.1.2.1Test Purpose and Environment4945

A.9.1.1.2.2Test requirements4945

A.9.1.1.3Test for FR1 NR Cell as Synchronization Reference Source4945

A.9.1.1.3.1Test Purpose and Environment4946

A.9.1.1.3.2Test requirements4947

A.9.1.2Test for Initiation/Cease of S-SSB Transmission with V2X Sidelink Communication4947

A.9.1.2.1Test for FR1 NR Cell as synchronization reference source without gap under non-DRX4947

A.9.1.2.1.1Test Purpose and Environment4947

A.9.1.2.1.2Test Requirements4949

A.9.1.2.2Test for SyncRef UE as synchronization reference source4949

A.9.1.2.2.1Test Purpose and Environment4949

A.9.1.2.2.2Test Requirements4951

A.9.1.2.3Test for SyncRef UE as synchronization reference source when SL-DRX is used4951

A.9.1.2.3.1Test Purpose and Environment4951

A.9.1.2.3.2Test Requirements4953

A.9.1.2.4Test for SyncRef UE as synchronization reference source with CCA4953

A.9.1.2.4.1Test Purpose and Environment4953

A.9.1.2.4.2Test Requirements4954

A.9.1.3 Test for V2X Synchronization Reference Selection/Reselection4955

A.9.1.3.1 Test for GNSS configured as the highest priority4955

A.9.1.3.1.1Test Purpose and Environment4955

A.9.1.3.1.2Test Requirements4956

A.9.1.3.2 Test for FR1 NR Cell configured as the highest priority4957

A.9.1.3.2.1Test Purpose and Environment4957

A.9.1.3.2.2Test Requirements4959

A.9.1.3.3Test for GNSS configured as the highest priority under SL-DRX4960

A.9.1.3.3.1Test Purpose and Environment4960

A.9.1.3.3.2Test Requirements4961

A.9.1.3.4Test for FR1 NR Cell configured as the highest priority under SL-DRX4962

A.9.1.3.4.1Test Purpose and Environment4962

A.9.1.3.4.2Test Requirements4964

A.9.1.4Test for L1 SL-RSRP Measurement4964

A.9.1.4.1Test for V2X UE Autonomous Resource Selection/Reselection4964

A.9.1.4.1.1Test Purpose and Environment4964

A.9.1.4.1.2Test Requirements4966

A.9.1.4.2Test for V2X UE Resource Pre-emption4967

A.9.1.4.2.1Test Purpose and Environment4967

A.9.1.4.2.2Test Requirements4968

A.9.1.4.3 Test for V2X UE Resource Re-evaluation4969

A.9.1.4.3.1Test Purpose and Environment4969

A.9.1.4.3.2Test Requirements4972

A.9.1.4.4Test for V2X UE Autonomous Resource Selection/Reselection with Periodic Sensing4972

A.9.1.4.4.1Test Purpose and Environment4972

A.9.1.4.4.2Test Requirements4974

A.9.1.4.5Test for V2X UE Autonomous Resource Selection/Reselection with Contiguous Sensing4974

A.9.1.4.5.1Test Purpose and Environment4974

A.9.1.4.5.2Test Requirements4976

A.9.1.4.6Test for V2X UE Autonomous Resource Selection/Reselection in SL-DRX4977

A.9.1.4.6.1Test Purpose and Environment4977

A.9.1.4.6.2Test Requirements4979

A.9.1.5Test for Congestion Control Measurement4979

A.9.1.5.1Test Purpose and Environment4979

A.9.1.5.2Test Requirements4982

A.9.1.6Test for Interruption4982

A.9.1.6.1Test for Interruption to WAN due to V2X Sidelink Communication4982

A.9.1.6.1.1Test Purpose and Environment4982

A.9.1.6.1.2Test Requirements4985

A.9.1.6.2Test for interruption to WAN at transitions between active and non-active during SL-DRX in asynchronous case4985

A.9.1.6.2.1Test Purpose and Environment4985

A.9.1.6.2.2Test Requirements4987

A.9.1.6.3Test for Interruption at NR Sidelink Diccovery Configuration4987

A.9.1.6.3.1Test Purpose and Environment4987

A.9.1.6.3.2Test Requirements4990

A.9.1.7Selection / Reselection of relay UE4990

A.9.1.7.1Test Purpose and Environment4990

A.9.1.7.2Test Requirements4994

A.9ATests for NR Sidelink Measurements for Positioning4995

A.9A.1Tests for NR Sidelink Measurements for Positioning in FR14995

A.9A.1.1Measurement delay tests4995

A.9A.1.1.1NR SL RSTD measurement reporting delay test case in FR1 SA4995

A.9A.1.1.1.1Test Purpose and Environment4995

A.9A.1.1.1.2Test Requirements5000

A.9A.1.1.2SL Rx-Tx measurement delay tests5000

A.9A.1.1.2.1Test Purpose and Environment5000

A.9A.1.1.2.2Test Requirements5003

A.9A.1.1.3NR SL AoA measurements reporting delay test in FR1 SA5004

A.9A.1.1.3.1Test Purpose and Environment5004

A.9A.1.1.3.2Test Requirements5007

A.9A.1.1.4NR SL RTOA measurements reporting delay test in FR1 SA5008

A.9A.1.1.4.1Test Purpose and Environment5008

A.9A.1.1.4.2Test Requirements5011

A.9A.1.1.5NR SL PRS-RSRP measurement reporting delay test case in FR1 SA5012

A.9A.1.1.5.1Test Purpose and Environment5012

A.9A.1.1.5.2Test Requirements5012

A.9A.1.1.6NR SL PRS-RSRPP measurement reporting delay test case in FR1 SA5012

A.9A.1.1.6.1Test Purpose and Environment5012

A.9A.1.1.6.2Test Requirements5012

A.9A.1.2Measurement Accuracy Tests5013

A.9A.1.2.1NR SL RSTD measurement accuracy test case in FR1 SA5013

A.9A.1.2.1.1Test Purpose and Environment5013

A.9A.1.2.1.2Test Requirements5016

A.9A.1.2.2SL Rx-Tx measurement accuracy test case in FR15017

A.9A.1.2.2.1Test Purpose and Environment5017

A.9A.1.2.2.2Test Requirements5020

A.9A.1.2.3NR SL PRS-RSRP measurement accuracy test case in FR1 SA5020

A.9A.1.2.3.1Test Purpose and Environment5020

A.9A.1.2.3.2Test Requirements5021

A.9A.1.2.4NR SL PRS-RSRPP measurement accuracy test case in FR1 SA5021

A.9A.1.2.4.1Test Purpose and Environment5021

A.9A.1.2.4.2Test Requirements5021

A.10EN-DC Tests with NR PSCell under CCA and Other NR Cells in FR15022

A.10.1RRC_CONNECTED state mobility5022

A.10.1.1RRC connection mobility control5022

A.10.1.1.1Random Access5022

A.10.1.1.1.14-step RA type contention-based random access for NR PSCell with CCA5022

A.10.1.1.1.1.1Test Purpose and Environment5022

A.10.1.1.1.1.2Test Requirements5023

A.10.1.1.1.1.2.1Random Access Preamble Transmission5024

A.10.1.1.1.1.2.2Random Access Response Reception5024

A.10.1.1.1.1.2.3No Random Access Response Reception5024

A.10.1.1.1.1.2.4Receiving an UL grant for msg3 retransmission5025

A.10.1.1.1.1.2.5 Contention Resolution Timer expiry5025

A.10.1.1.1.24-step RA type non-contention based random access for NR PSCell with CCA5025

A.10.1.1.1.2.1Test Purpose and Environment5025

A.10.1.1.1.2.2Test Requirements5026

A.10.1.1.1.2.2.1SSB-based Random Access Preamble Transmission5027

A.10.1.1.1.2.2.2Random Access Response Reception5027

A.10.1.1.1.2.2.3No Random Access Response Reception5027

A.10.1.1.1.32-step RA type contention-based random access for NR PSCell with CCA5028

A.10.1.1.1.3.1Test Purpose and Environment5028

A.10.1.1.1.3.2Test Requirements5029

A.10.1.1.1.3.2.1MsgA Transmission5030

A.10.1.1.1.3.2.2MsgB Reception5030

A.10.1.1.1.3.2.3No MsgB Reception5030

A.10.1.1.1.42-step RA type non-contention based random access for NR PSCell with CCA5031

A.10.1.1.1.4.1Test Purpose and Environment5031

A.10.1.1.1.4.2Test Requirements5032

A.10.1.1.1.4.2.1MsgA Transmission5033

A.10.1.1.1.4.2.2MsgB Reception5033

A.10.1.1.1.4.2.3No MsgB Reception5033

A.10.1.2Handover with PSCell from EN-DC to EN-DC with known target PSCell using CCA5034

A.10.1.2.1Test Purpose and Environment5034

A.10.1.2.2Test Requirements5038

A.10.2Timing5039

A.10.2.1UE transmit timing5039

A.10.2.1.1UE Transmit Timing Test with PSCell under DL CCA5039

A.10.2.1.1.1Test Purpose and environment5039

A.10.2.1.1.2Test requirements5041

A.10.2.2UE timing advance5042

A.10.2.2.1UE Timing Advance Adjustment Accuracy with PSCell under DL CCA5042

A.10.2.2.1.1Test Purpose and Environment5042

A.10.2.2.1.2Test Parameters5042

A.10.2.2.1.3Test Requirements5044

A.10.3Signalling characteristics5044

A.10.3.1Radio link monitoring5044

A.10.3.1.1Introduction5044

A.10.3.1.2Radio link monitoring out-of-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode5045

A.10.3.1.2.1Test purpose and environment5045

A.10.3.1.2.2Test requirements5047

A.10.3.1.3Radio link monitoring in-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode5048

A.10.3.1.3.1Test purpose and environment5048

A.10.3.1.3.2Test requirements5050

A.10.3.1.4Void5050

A.10.3.1.4.1Void5050

A.10.3.1.4.2Void5050

A.10.3.1.5Void5051

A.10.3.1.5.1Void5051

A.10.3.1.5.2Void5051

A.10.3.2Void5051

A.10.3.3SCell activation and deactivation delay5051

A.10.3.3.1SCell Activation and Deactivation of known NR SCell with NR PSCell and NR SCell under CCA, 160 ms SCell measurement cycle5051

A.10.3.3.1.1Test Purpose and Environment5051

A.10.3.3.1.2Test Requirements5054

A.10.3.3.2 SCell Activation and Deactivation of known NR SCell with NR PSCell and NR SCell under CCA, 640 ms SCell measurement cycle5054

A.10.3.3.2.1Test Purpose and Environment5054

A.10.3.3.2.2Test Requirements5055

A.10.3.3.3SCell Activation and Deactivation of unknown NR SCell with NR PSCell and NR SCell under CCA5055

A.10.3.3.3.1Test Purpose and Environment5055

A.10.3.3.3.2Test Requirements5055

A.10.3.4Beam failure detection and link recovery procedures5056

A.10.3.4.1EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode5056

A.10.3.4.1.1Test Purpose and Environment5056

A.10.3.4.1.2Test Requirements5059

A.10.3.4.2EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in DRX mode5059

A.10.3.4.2.1Test Purpose and Environment5059

A.10.3.4.2.2Test Requirements5062

A.10.3.5Active BWP switching5063

A.10.3.5.1UL active BWP switch delay with consistent UL LBT failure on PSCell subject to UL CCA in EN-DC5063

A.10.3.5.1.2Test Requirements5065

A.10.3.5.2DCI-based and Timer-based Active BWP Switch5066

A.10.3.5.2.1E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC5066

A.10.3.5.2.2E-UTRAN – NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC5069

A.10.3.5.3RRC-based Active BWP Switch5073

A.10.3.5.3.1E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC5073

A.10.3.6PSCell addition and release delay5075

A.10.3.6.1Addition and Release Delay of known NR PSCell on the carrier under CCA5075

A.10.3.6.1.1Test purpose and environment5075

A.10.3.6.1.2Test Requirements5078

A.10.3.7Void5078

A.10.4Measurement procedure5078

A.10.4.1Intra-frequency measurements5079

A.10.4.1.1Event-triggered reporting tests on PSCC without gaps under non-DRX5079

A.10.4.1.1.1Test purpose and environment5079

A.10.4.1.1.2Test parameters5079

A.10.4.1.1.3Test Requirements5081

A.10.4.1.2Void5081

A.10.4.1.3Void5081

A.10.4.1.4Event-triggered reporting tests on PSCC with per-UE gaps under DRX5081

A.10.4.1.4.1Test purpose and environment5081

A.10.4.1.4.2Test parameters5081

A.10.4.1.4.3Test Requirements5084

A.10.4.1.5Void5084

A.10.4.1.6Void5084

A.10.4.1.7Void5084

A.10.4.1.8Void5084

A.10.4.1.9Void5084

A.10.4.1.10Void5084

A.10.4.1.11Void5084

A.10.4.1.12Void5084

A.10.4.2Inter-frequency measurements5084

A.10.4.2.1Void5084

A.10.4.2.2Void5084

A.10.4.2.3EN-DC event triggered reporting tests for FR1 with CCA cell without SSB time index detection when DRX is not used5085

A.10.4.2.3.1Test Purpose and Environment5085

A.10.4.2.3.2Test Requirements5087

A.10.4.2.4EN-DC event triggered reporting tests for FR1 cell with CCA without SSB time index detection when DRX is used5087

A.10.4.2.4.1Test Purpose and Environment5087

A.10.4.2.4.2Test Requirements5090

A.10.4.2.5EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is not used5091

A.10.4.2.5.1Test Purpose and Environment5091

A.10.4.2.5.2Test Requirements5093

A.10.4.2.6EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is used5093

A.10.4.2.6.1Test Purpose and Environment5093

A.10.4.2.6.2Test Requirements5096

A.10.4.2.7EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is not used5097

A.10.4.2.7.1Test Purpose and Environment5097

A.10.4.2.7.2Test Requirements5100

A.10.4.2.8EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used5100

A.10.4.2.8.1Test Purpose and Environment5100

A.10.4.2.8.2Test Requirements5104

A.10.4.2.9EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is not used5105

A.10.4.2.9.1Test Purpose and Environment5105

A.10.4.2.9.2Test Requirements5108

A.10.4.2.10EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is used5108

A.10.4.2.10.1Test Purpose and Environment5108

A.10.4.2.10.2Test Requirements5112

A.10.4.3L1-RSRP measurements for beam reporting5113

A.10.4.3.1SSB based L1-RSRP measurement on PSCC when DRX is not used5113

A.10.4.3.1.1Test Purpose and Environment5113

A.10.4.3.1.2Test parameters5113

A.10.4.3.1.3Test Requirements5114

A.10.4.3.2SSB based L1-RSRP measurement on PSCC when DRX is used5115

A.10.4.3.2.1Test Purpose and Environment5115

A.10.4.3.2.2Test parameters5115

A.10.4.3.2.3Test Requirements5116

A.10.4.3.3SSB based L1-RSRP measurement on SCC when DRX is not used5117

A.10.4.3.3.1Test Purpose and Environment5117

A.10.4.3.3.2Test parameters5117

A.10.4.3.3.3Test Requirements5118

A.10.4.3.4SSB based L1-RSRP measurement on SCC when DRX is used5119

A.10.4.3.4.1Test Purpose and Environment5119

A.10.4.3.4.2Test parameters5119

A.10.4.3.4.3Test Requirements5120

A.10.4.4E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA5121

A.10.4.4.1E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used5121

A.10.4.4.1.1Test Purpose and Environment5121

A.10.4.4.1.2Test Requirements5124

A.10.4.4.2E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used5125

A.10.4.4.2.1Test Purpose and Environment5125

A.10.4.4.2.2Test Requirements5128

A.10.4.4.3NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used5129

A.10.4.4.3.1Test Purpose and Environment5129

A.10.4.4.3.2Test Requirements5132

A.10.4.4.4NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used5132

A.10.4.4.4.1Test Purpose and Environment5132

A.10.4.4.4.2Test Requirements5136

A.10.5Measurement performance5136

A.10.5.1SS-RSRP5136

A.10.5.1.1Intra-frequency measurement accuracy on a CCA serving cell5136

A.10.5.1.1.1Test Purpose and Environment5136

A.10.5.1.1.2Test parameters5137

A.10.5.1.1.3Test Requirements5138

A.10.5.1.2Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell5138

A.10.5.1.2.1Test Purpose and Environment5138

A.10.5.1.2.2Test parameters5139

A.10.5.1.2.3Test Requirements5140

A.10.5.2SS-RSRQ5140

A.10.5.2.1Intra-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell5140

A.10.5.2.1.1Test Purpose and Environment5140

A.10.5.2.1.2Test Parameters5140

A.10.5.2.1.3Test Requirements5142

A.10.5.2.2Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell5142

A.10.5.2.2.1Test Purpose and Environment5142

A.10.5.2.2.2Test Parameters5142

A.10.5.2.2.3Test Requirements5144

A.10.5.3SS-SINR5144

A.10.5.3.1Intra-frequency measurement accuracy on PSCC5144

A.10.5.3.1.1Test Purpose and Environment5144

A.10.5.3.1.2Test Parameters5144

A.10.5.3.1.3Test Requirements5145

A.10.5.3.2Inter-frequency measurement accuracy on PSCC5146

A.10.5.3.2.1Test Purpose and Environment5146

A.10.5.3.2.2Test Parameters5146

A.10.5.3.2.3Test Requirements5147

A.10.5.3.3Intra-frequency measurement accuracy on SCC5147

A.10.5.3.3.1Test Purpose and Environment5147

A.10.5.3.3.2Test Parameters5147

A.10.5.3.3.3Test Requirements5149

A.10.5.4L1-RSRP measurement for beam reporting with CCA serving cell5149

A.10.5.4.1SSB based L1-RSRP measurement5149

A.10.5.4.1.1Test Purpose and Environment5149

A.10.5.4.1.2Test parameters5150

A.10.5.4.1.3Test Requirements5151

A.10.5.5RSSI5151

A.10.5.5.1 RSSI measurement accuracy on PSCC with CCA5151

A.10.5.5.1.1Test Purpose and Environment5151

A.10.5.5.1.2Test parameters5151

A.10.5.5.1.3Test Requirements5153

A.10.5.5.2RSSI measurement accuracy on SCC with CCA5153

A.10.5.5.2.1Test Purpose and Environment5153

A.10.5.5.2.2Test parameters5153

A.10.5.5.2.3Test Requirements5154

A.10.5.5.3 Inter-frequency RSSI measurement accuracy on a carrier with CCA5154

A.10.5.5.3.1Test Purpose and Environment5154

A.10.5.5.3.2Test parameters5155

A.10.5.5.3.3Test Requirements5156

A.10.5.6Channel occupancy5156

A.10.5.6.1 Channel occupancy measurement accuracy on PSCC with CCA5156

A.10.5.6.1.1Test Purpose and Environment5156

A.10.5.6.1.2Test parameters5156

A.10.5.6.1.3Test Requirements5158

A.10.5.6.2 Channel occupancy measurement accuracy on SCC with CCA5158

A.10.5.6.2.1Test Purpose and Environment5158

A.10.5.6.2.2Test parameters5158

A.10.5.6.2.3Test Requirements5160

A.10.5.6.3 Inter-frequency channel occupancy measurement accuracy on a carrier with CCA5160

A.10.5.6.3.1Test Purpose and Environment5160

A.10.5.6.3.2Test parameters5160

A.10.5.6.3.3Test Requirements5162

A.11NR Standalone Tests with NR PCell under CCA and Other NR Cells in FR15163

A.11.1RRC_IDLE state mobility5163

A.11.1.1Cell re-selection with both source and target NR carrier frequencies under CCA5163

A.11.1.1.1Cell reselection to FR1 intra-frequency NR cells when subject to CCA on the serving and target cell5163

A.11.1.1.1.1Test Purpose and Environment5163

A.11.1.1.1.2Test Parameters5163

A.11.1.1.1.3Test Requirements5165

A.11.1.1.2Cell reselection to FR1 inter-frequency NR case when subject to CCA on the serving and target cell5166

A.11.1.1.2.1Test Purpose and Environment5166

A.11.1.1.2.2Test Parameters5166

A.11.1.1.2.3Test Requirements5168

A.11.1.2Cell re-selection to NR with source NR carrier frequency under CCA5168

A.11.1.2.1Cell reselection to FR1 inter-frequency NR case when serving cell is subject to CCA5168

A.11.1.2.1.1Test Purpose and Environment5168

A.11.1.2.1.2Test Parameters5169

A.11.1.2.1.3Test Requirements5171

A.11.1.3Cell re-selection from NR carrier with target NR carrier frequency under CCA5172

A.11.1.3.1Cell reselection to FR1 inter-frequency NR case when target cell is subject to CCA5172

A.11.1.3.1.1Test Purpose and Environment5172

A.11.1.3.1.2Test Parameters5172

A.11.1.3.1.3Test Requirements5175

A.11.1.4Inter-RAT cell re-selection to E-UTRAN with source NR carrier frequency under CCA5176

A.11.1.4.1Cell reselection to higher priority E-UTRAN when serving cell is subject to CCA5176

A.11.1.4.1.1Test Purpose and Environment5176

A.11.1.4.1.2Test Parameters5176

A.11.1.4.1.3Test Requirements5179

A.11.1.4.2Cell reselection to lower priority E-UTRAN when serving cell is subject to CCA5179

A.11.1.4.2.1Test Purpose and Environment5179

A.11.1.4.2.2Test Requirements5181

A.11.2RRC_CONNECTED state mobility5182

A.11.2.1Handover5182

A.11.2.1.1Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; known target cell5182

A.11.2.1.1.1Test Purpose and Environment5182

A.11.2.1.1.2Test Parameters5182

A.11.2.1.1.3 Test Requirements5184

A.11.2.1.2Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell5185

A.11.2.1.2.1Test Purpose and Environment5185

A.11.2.1.2.2Test Parameters5185

A.11.2.1.2.3Test Requirements5187

A.11.2.1.3Inter-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell5187

A.11.2.1.3.1Test Purpose and Environment5187

A.11.2.1.3.2Test Parameters5187

A.11.2.1.3.3Test Requirements5189

A.11.2.1.4Inter-frequency handover from FR1 carrier under CCA to FR1; known target cell5190

A.11.2.1.4.1Test Purpose and Environment5190

A.11.2.1.4.2Test Parameters5190

A.11.2.1.4.3Test Requirements5193

A.11.2.1.5Inter-frequency handover from FR1 carrier under CCA to FR1; unknown target cell5193

A.11.2.1.5.1Test Purpose and Environment5193

A.11.2.1.5.2Test Parameters5193

A.11.2.1.5.3 Test Requirements5196

A.11.2.1.6Inter-frequency handover from FR1 to FR1 carrier under CCA; unknown target cell5196

A.11.2.1.6.1Test Purpose and Environment5196

A.11.2.1.6.2Test Parameters5196

A.11.2.1.6.3Test Requirements5199

A.11.2.1.7 SA NR FR1 carrier under CCA - E-UTRAN handover with known target cell5199

A.11.2.1.7.1Test Purpose and Environment5199

A.11.2.1.7.2Test Requirements5202

A.11.2.1.8SA NR FR1 carrier under CCA - E-UTRAN handover with unknown target cell5203

A.11.2.1.8.1Test Purpose and Environment5203

A.11.2.1.8.2Test Requirements5206

A.11.2.1.9Handover with PSCell from NR SA to EN-DC with known target PSCell using CCA5206

A.11.2.1.9.1Test Purpose and Environment5206

A.11.2.1.9.2Test Requirements5212

A.11.2.2RRC connection mobility control5213

A.11.2.2.1RRC re-establishment5213

A.11.2.2.1.1Intra-frequency RRC Re-establishment with CCA in FR15213

A.11.2.2.1.2Inter-frequency RRC Re-establishment with CCA in FR15216

A.11.2.2.1.4Inter-frequency RRC Re-establishment from NR FR1 carrier without CCA to NR FR1 carrier under CCA5222

A.11.2.2.2Random Access5225

A.11.2.2.2.14-step RA type contention-based random access for NR PCell with CCA5225

A.11.2.2.2.1.1Test Purpose and Environment5225

A.11.2.2.2.1.2Test Requirements5226

A.11.2.2.2.1.2.1Random Access Preamble Transmission5226

A.11.2.2.2.1.2.2Random Access Response Reception5227

A.11.2.2.2.1.2.3No Random Access Response Reception5227

A.11.2.2.2.1.2.4Receiving an UL grant for msg3 retransmission5227

A.11.2.2.2.1.2.5Reception of an Incorrect Message over Temporary C-RNTI5227

A.11.2.2.2.1.2.6Reception of a Correct Message over Temporary C-RNTI5228

A.11.2.2.2.1.2.7Contention Resolution Timer expiry5228

A.11.2.2.2.24-step RA type non-contention based random access for NR PSCell with CCA5228

A.11.2.2.2.2.1Test Purpose and Environment5228

A.11.2.2.2.2.2Test Requirements5229

A.11.2.2.2.2.2.1SSB-based Random Access Preamble Transmission5230

A.11.2.2.2.2.2.2Random Access Response Reception5230

A.11.2.2.2.2.2.3No Random Access Response Reception5230

A.11.2.2.2.32-step RA type contention-based random access for NR PCell with CCA5231

A.11.2.2.2.3.1Test Purpose and Environment5231

A.11.2.2.2.3.2Test Requirements5232

A.11.2.2.2.3.2.1MsgA Transmission5232

A.11.2.2.2.3.2.2MsgB Reception5233

A.11.2.2.2.3.2.3No MsgB Reception5233

A.11.2.2.2.42-step RA type non-contention-based random access for NR PCell with CCA5234

A.11.2.2.2.4.1Test Purpose and Environment5234

A.11.2.2.2.4.2Test Requirements5235

A.11.2.2.2.4.2.1MsgA Transmission5235

A.11.2.2.2.4.2.2MsgB Reception5236

A.11.2.2.2.4.2.3No MsgB Reception5236

A.11.2.2.3RRC connection release with redirection5237

A.11.2.2.3.1Redirection from NR FR1 carrier under CCA to NR FR1 carrier under CCA5237

A.11.2.2.3.2Redirection from NR FR1 carrier without CCA to NR FR1 carrier with CCA5239

A.11.3Timing5242

A.11.3.1UE transmit timing5242

A.11.3.1.1UE Transmit Timing Test with PCell under DL CCA5242

A.11.3.1.1.1Test Purpose and environment5242

A.11.3.1.1.2Test requirements5244

A.11.3.2UE timing advance5245

A.11.3.2.1UE Timing Advance Adjustment Accuracy with PCell under DL CCA5245

A.11.3.2.1.1Test Purpose and Environment5245

A.11.3.2.1.2Test Parameters5245

A.11.3.2.1.3Test Requirements5247

A.11.4Signalling characteristics5247

A.11.4.1Radio link monitoring5247

A.11.4.1.1Introduction5247

A.11.4.1.2Radio link monitoring out-of-sync test for PCell configured with SSB-based RLM RS in non-DRX mode5248

A.11.4.1.2.1Test purpose and environment5248

A.11.4.1.2.2Test requirements5250

A.11.4.1.3Radio link monitoring in-sync test for PCell configured with SSB-based RLM RS in non-DRX mode5251

A.11.4.1.3.1Test purpose and environment5251

A.11.4.1.3.2Test requirements5254

A.11.4.1.4Void5254

A.11.4.1.4.1Void5254

A.11.4.1.4.2Void5254

A.11.4.1.5Void5254

A.11.4.1.5.1Void5254

A.11.4.1.5.2Void5254

A.11.4.2Void5254

A.11.4.3SCell activation and deactivation delay5254

A.11.4.3.1SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 160 ms SCell measurement cycle5254

A.11.4.3.1.1Test Purpose and Environment5254

A.11.4.3.1.2Test Requirements5257

A.11.4.3.2SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 640 ms SCell measurement cycle5257

A.11.4.3.2.1Test Purpose and Environment5257

A.11.4.3.2.2Test Requirements5258

A.11.4.3.3SCell Activation and Deactivation of unknown SCell with PCell and SCell under CCA5258

A.11.4.3.3.1Test Purpose and Environment5258

A.11.4.3.3.2Test Requirements5258

A.11.4.4Beam failure detection and link recovery procedures5259

A.11.4.4.1Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode5259

A.11.4.4.1.1Test Purpose and Environment5259

A.11.4.4.1.2Test Requirements5262

A.11.4.4.2Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode5263

A.11.4.4.2.1Test Purpose and Environment5263

A.11.4.4.2.2Test Requirements5266

A.11.4.5Active BWP switching5266

A.11.4.5.1UL active BWP switch delay with consistent UL LBT failure on PCell subject to UL CCA5266

A.11.4.5.1.1Test Purpose and Environment5266

A.11.4.5.1.2Test Requirements5269

A.11.4.5.2DCI-based and Timer-based Active BWP Switch5269

A.11.4.5.2.1NR FR1- NR FR1 DL active BWP switch of PCell with non-DRX in SA5269

A.11.4.5.2.2NR FR1 DL active BWP switch with non-DRX in SA5272

A.11.4.5.3RRC-based Active BWP Switch5275

A.11.4.5.3.1NR FR1 DL active BWP switch of Cell with non-DRX in SA5275

A.11.4.6Void5277

A.11.5Measurement procedure5277

A.11.5.1Intra-frequency measurements5277

A.11.5.1.1Event-triggered reporting tests on PCC without gaps under non-DRX5277

A.11.5.1.1.1Test purpose and environment5277

A.11.5.1.1.2Test parameters5277

A.11.5.1.1.3Test Requirements5279

A.11.5.1.2Event-triggered reporting tests on PCC without gaps under DRX5279

A.11.5.1.2.1Test purpose and environment5279

A.11.5.1.2.2Test parameters5279

A.11.5.1.2.3Test Requirements5281

A.11.5.1.3Void5282

A.11.5.1.4Void5282

A.11.5.1.5Void5282

A.11.5.1.6Void5282

A.11.5.1.7Void5282

A.11.5.1.8Void5282

A.11.5.1.9Void5282

A.11.5.1.10Void5282

A.11.5.1.11Void5282

A.11.5.1.12Void5282

A.11.5.2Inter-frequency measurements5282

A.11.5.2.1Void5282

A.11.5.2.2Void5282

A.11.5.2.3Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used5282

A.11.5.2.3.1Test Purpose and Environment5282

A.11.5.2.3.2Test Requirements5285

A.11.5.2.4Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used5285

A.11.5.2.4.1Test Purpose and Environment5285

A.11.5.2.4.2Test Requirements5288

A.11.5.2.5Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used5288

A.11.5.2.5.1Test Purpose and Environment5288

A.11.5.2.5.2Test Requirements5291

A.11.5.2.6Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used5291

A.11.5.2.6.1Test Purpose and Environment5291

A.11.5.2.6.2Test Requirements5294

A.11.5.2.7Event triggered reporting tests for FR1 without SSB time index detection when DRX is not used5295

A.11.5.2.7.1Test Purpose and Environment5295

A.11.5.2.7.2Test Requirements5297

A.11.5.2.8Event triggered reporting tests for FR1 without SSB time index detection when DRX is used5298

A.11.5.2.8.1Test Purpose and Environment5298

A.11.5.2.8.2Test Requirements5301

A.11.5.2.9Event triggered reporting tests for FR1 with SSB time index detection when DRX is not used5301

A.11.5.2.9.1Test Purpose and Environment5301

A.11.5.2.9.2Test Requirements5304

A.11.5.2.10Event triggered reporting tests for FR1 with SSB time index detection when DRX is used5304

A.11.5.2.10.1Test Purpose and Environment5304

A.11.5.2.10.2Test Requirements5308

A.11.5.3Inter-RAT E-UTRAN measurements5308

A.11.5.3.1SA NR - E-UTRAN event-triggered reporting in non-DRX in FR15308

A.11.5.3.1.1Test Purpose and Environment5308

A.11.5.3.1.2Test Requirements5311

A.11.5.3.2SA NR - E-UTRAN event-triggered reporting in DRX in FR15311

A.11.5.3.2.1Test Purpose and Environment5311

A.11.5.3.2.2Test Requirements5315

A.11.5.4L1-RSRP measurements for beam reporting5315

A.11.5.4.1SSB based L1-RSRP measurement when DRX is not used5315

A.11.5.4.1.1Test Purpose and Environment5315

A.11.5.4.1.2Test parameters5315

A.11.5.4.1.3Test Requirements5317

A.11.5.4.2SSB based L1-RSRP measurement when DRX is used5317

A.11.5.4.2.1Test Purpose and Environment5317

A.11.5.4.2.2Test parameters5317

A.11.5.4.2.3Test Requirements5319

A.11.5.4.3SSB based L1-RSRP measurement on SCC when DRX is not used5319

A.11.5.4.3.1Test Purpose and Environment5319

A.11.5.4.3.2Test parameters5320

A.11.5.4.3.3Test Requirements5321

A.11.5.4.4SSB based L1-RSRP measurement on SCC when DRX is used5321

A.11.5.4.4.1Test Purpose and Environment5321

A.11.5.4.4.2Test parameters5322

A.11.5.4.4.3Test Requirements5323

A.11.6Measurement performance5323

A.11.6.1SS-RSRP5323

A.11.6.1.1Intra-frequency measurement accuracy on a carrier frequency with CCA5323

A.11.6.1.1.1Test Purpose and Environment5323

A.11.6.1.1.2Test parameters5324

A.11.6.1.1.3Test Requirements5325

A.11.6.1.2Intra-frequency measurement accuracy on SCC on a carrier frequency with CCA5325

A.11.6.1.2.1Test Purpose and Environment5325

A.11.6.1.2.2Test parameters5325

A.11.6.1.2.3Test Requirements5327

A.11.6.2SS-RSRQ5327

A.11.6.2.1Intra-frequency measurement accuracy5327

A.11.6.2.1.1Test Purpose and Environment5327

A.11.6.2.1.2Test Parameters5327

A.11.6.2.1.3Test Requirements5329

A.11.6.2.2Inter-frequency measurement accuracy5329

A.11.6.2.2.1Test Purpose and Environment5329

A.11.6.2.2.2Test Parameters5329

A.11.6.2.2.3Test Requirements5332

A.11.6.2.3Intra-frequency measurement accuracy on SCC5332

A.11.6.2.3.1Test Purpose and Environment5332

A.11.6.2.3.2Test Parameters5332

A.11.6.2.3.3Test Requirements5334

A.11.6.2.4Inter-frequency measurement accuracy5334

A.11.6.2.4.1Test Purpose and Environment5334

A.11.6.2.4.2Test Parameters5334

A.11.6.2.4.3Test Requirements5340

A.11.6.3SS-SINR5340

A.11.6.3.1Intra-frequency measurement accuracy5340

A.11.6.3.1.1Test Purpose and Environment5340

A.11.6.3.1.2Test Parameters5340

A.11.6.3.1.3Test Requirements5342

A.11.6.3.2Inter-frequency measurement accuracy5342

A.11.6.3.2.1Test Purpose and Environment5342

A.11.6.3.2.2Test Parameters5342

A.11.6.3.2.3Test Requirements5344

A.11.6.3.3Intra-frequency measurement accuracy on SCC5344

A.11.6.3.3.1Test Purpose and Environment5344

A.11.6.3.3.2Test Parameters5344

A.11.6.3.3.3Test Requirements5346

A.11.6.3.4Inter-frequency measurement accuracy5346

A.11.6.3.4.1Test Purpose and Environment5346

A.11.6.3.4.2Test Parameters5346

A.11.6.3.4.3Test Requirements5350

A.11.6.4L1-RSRP measurement for beam reporting with CCA serving cell5350

A.11.6.4.1SSB based L1-RSRP measurement5350

A.11.6.4.1.1Test Purpose and Environment5350

A.11.6.4.1.2Test parameters5350

A.11.6.4.1.3Test Requirements5352

A.11.6.5RSSI5352

A.11.6.5.1Intra-frequency RSSI measurement accuracy on PCC with CCA5352

A.11.6.5.1.1Test Purpose and Environment5352

A.11.6.5.1.2Test parameters5352

A.11.6.5.1.3Test Requirements5353

A.11.6.5.2Intra-frequency RSSI measurement accuracy on SCC with CCA5353

A.11.6.5.2.1Test Purpose and Environment5353

A.11.6.5.2.2Test parameters5353

A.11.6.5.2.3Test Requirements5355

A.11.6.5.3Inter-frequency RSSI measurement accuracy on a carrier with CCA5355

A.11.6.5.3.1Test Purpose and Environment5355

A.11.6.5.3.2Test parameters5355

A.11.6.5.3.3Test Requirements5357

A.11.6.6Channel occupancy5357

A.11.6.6.1Intra-frequency channel occupancy measurement accuracy on PCC with CCA5357

A.11.6.6.1.1Test Purpose and Environment5357

A.11.6.6.1.2Test parameters5357

A.11.6.6.1.3Test Requirements5359

A.11.6.6.2Intra-frequency channel occupancy measurement accuracy on SCC with CCA5359

A.11.6.6.2.1Test Purpose and Environment5359

A.11.6.6.2.2Test parameters5359

A.11.6.6.2.3Test Requirements5360

A.11.6.6.3Inter-frequency channel occupancy measurement accuracy on a carrier with CCA5360

A.11.6.6.3.1Test Purpose and Environment5361

A.11.6.6.3.2Test parameters5361

A.11.6.6.3.3Test Requirements5362

A.11.6.7E-UTRAN RSRP5362

A.11.6.8E-UTRAN RSRQ5362

A.11.6.9E-UTRAN SINR5362

A.12E-UTRA Standalone Tests with at Least One NR Cell under CCA5363

A.12.1RRC_IDLE state mobility5363

A.12.1.1Inter-RAT cell re-selection to NR on a carrier frequency with CCA5363

A.12.1.1.1E-UTRA Cell reselection to higher priority NR target Cell in FR1 when target cell is subject to CCA5363

A.12.1.1.1.1Test Purpose and Environment5363

A.12.1.1.1.2Test Requirements5366

A.12.2RRC_CONNECTED state mobility5366

A.12.2.1Handover5366

A.12.2.1.1E-UTRAN - NR with CCA handover5366

A.12.2.1.1.1Test Purpose and Environment5366

A.12.2.1.1.2Test Requirements5370

A.12.3Void5370

A.12.4Measurement procedure5370

A.12.4.1E-UTRANNR inter-RAT SFTD measurements5370

A.12.4.1.1E-UTRA – NR Inter-RAT SFTD Measurement Delay with NR under CCA in non-DRX5370

A.12.4.1.1.1Test Purpose and Environment5370

A.12.4.1.1.2Test Requirements5372

A.12.4.2E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA5372

A.12.4.2.1E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used5372

A.12.4.2.1.1Test Purpose and Environment5372

A.12.4.2.1.2Test Requirements5376

A.12.4.2.2E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used5376

A.12.4.2.2.1Test Purpose and Environment5376

A.12.4.2.2.2Test Requirements5379

A.12.4.2.3NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used5380

A.12.4.2.3.1Test Purpose and Environment5380

A.12.4.2.3.2Test Requirements5383

A.12.4.2.4NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used5383

A.12.4.2.4.1Test Purpose and Environment5383

A.12.4.2.4.2Test Requirements5386

A.12.4.2.5Void5387

A.12.4.2.6Void5387

A.12.5Measurement performance5387

A.12.5.1E-UTRANNR SFTD5387

A.12.5.1.1Inter-RAT SFTD accuracy with NR target cell under CCA5387

A.12.5.1.1.1Test Purpose5387

A.12.5.1.1.2Test Environment5387

A.12.5.1.1.3Test Requirements5389

A.12.5.2Void5389

A.12.5.3Void5389

A.12.5.4Void5390

A.12.5.5Void5390

A.12.5.6Void5390

A.13NR Standalone Tests with NR SCell under CCA and All Other NR Cells in FR15391

A.13.1Void5391

A.13.1.1Void5391

A.13.1.2Void5391

A.13.2Signalling characteristics5391

A.13.2.1Void5391

A.13.2.2SCell activation and deactivation delay5391

A.13.2.2.1SCell Activation and Deactivation of known SCell under CCA, 160 ms SCell measurement cycle5391

A.13.2.2.1.1Test Purpose and Environment5391

A.13.2.2.1.2Test Requirements5394

A.13.2.2.2 SCell Activation and Deactivation of known SCell under CCA, 640 ms SCell measurement cycle5394

A.13.2.2.2.1Test Purpose and Environment5394

A.13.2.2.2.2Test Requirements5395

A.13.2.2.3SCell Activation and Deactivation of unknown SCell under CCA5395

A.13.2.2.3.1Test Purpose and Environment5395

A.13.2.2.3.2Test Requirements5395

A.13.2.3Void5396

A.13.3Measurement procedure5396

A.13.3.1Intra-frequency measurements5396

A.13.3.1.1Event-triggered reporting tests on SCC without gaps under non-DRX5396

A.13.3.1.1.1Test purpose and environment5396

A.13.3.1.1.2Test parameters5396

A.13.3.1.1.3Test Requirements5399

A.13.3.1.2Event-triggered reporting tests on SCC without gaps under DRX5399

A.13.3.1.2.1Test purpose and environment5399

A.13.3.1.2.2Test parameters5399

A.13.3.1.2.3Test Requirements5402

A.13.3.1.3Event-triggered reporting tests on SCC with per-UE gaps under non-DRX5402

A.13.3.1.3.1Test purpose and environment5402

A.13.3.1.3.2Test parameters5402

A.13.3.1.3.3Test Requirements5405

A.13.3.1.4Event-triggered reporting tests on SCC with per-UE gaps under DRX5406

A.13.3.1.4.1Test purpose and environment5406

A.13.3.1.4.2Test parameters5406

A.13.3.1.4.3Test Requirements5409

A.13.3.1.5Void5409

A.13.3.1.6Void5409

A.13.3.2Inter-frequency measurements5409

A.13.3.2.1Void5409

A.13.3.2.2Void5409

A.13.3.2.3Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used5409

A.13.3.2.3.1Test Purpose and Environment5409

A.13.3.2.3.2Test Requirements5412

A.13.3.2.4Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used5413

A.13.3.2.4.1Test Purpose and Environment5413

A.13.3.2.4.2Test Requirements5416

A.13.3.2.5Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used5416

A.13.3.2.5.1Test Purpose and Environment5416

A.13.3.2.5.2Test Requirements5419

A.13.3.2.6Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used5419

A.13.3.2.6.1Test Purpose and Environment5419

A.13.3.2.6.2Test Requirements5423

A.13.3.3L1-RSRP measurements for beam reporting5423

A.13.3.3.1SSB based L1-RSRP measurement when DRX is not used5423

A.13.3.3.1.1Test Purpose and Environment5423

A.13.3.3.1.2Test parameters5423

A.13.3.3.1.3Test Requirements5425

A.13.3.3.2SSB based L1-RSRP measurement when DRX is used5426

A.13.3.3.2.1Test Purpose and Environment5426

A.13.3.3.2.2Test parameters5426

A.13.3.3.2.3Test Requirements5428

A.13.4Measurement performance5428

A.13.4.1SS-RSRP5428

A.13.4.1.1Intra-frequency measurement accuracy on a carrier frequency with CCA5428

A.13.4.1.1.1Test Purpose and Environment5428

A.13.4.1.1.2Test parameters5428

A.13.4.1.1.3Test Requirements5430

A.13.4.2SS-RSRQ5430

A.13.4.2.1Intra-frequency measurement accuracy on SCC5430

A.13.4.2.1.1Test Purpose and Environment5430

A.13.4.2.1.2Test Parameters5430

A.13.4.2.1.3Test Requirements5434

A.13.4.3SS-SINR5434

A.13.4.3.1Intra-frequency measurement accuracy on SCC5434

A.13.4.3.1.1Test Purpose and Environment5434

A.13.4.3.1.2Test Parameters5434

A.13.4.3.1.3Test Requirements5438

A.13.4.4L1-RSRP measurement for beam reporting with CCA serving cell5438

A.13.4.4.1SSB based L1-RSRP measurement5438

A.13.4.4.1.1Test Purpose and Environment5438

A.13.4.4.1.2Test parameters5439

A.13.4.4.1.3Test Requirements5441

A.13.4.5RSSI5441

A.13.4.5.1 Intra-frequency RSSI measurement accuracy on a carrier with CCA5441

A.13.4.5.1.1Test Purpose and Environment5441

A.13.4.5.1.2Test parameters5441

A.13.4.5.1.3Test Requirements5443

A.13.4.5.2Inter-frequency RSSI measurement accuracy on a carrier with CCA5443

A.13.4.5.2.1Test Purpose and Environment5443

A.13.4.5.2.2Test parameters5443

A.13.4.5.2.3Test Requirements5445

A.13.4.6Channel occupancy5445

A.13.4.6.1Intra-frequency channel occupancy measurement accuracy on SCC with CCA5445

A.13.4.6.1.1Test Purpose and Environment5445

A.13.4.6.1.2Test parameters5445

A.13.4.6.1.3Test Requirements5447

A.13.4.6.2Inter-frequency channel occupancy measurement accuracy on a carrier with CCA5447

A.13.4.6.2.1Test Purpose and Environment5447

A.13.4.6.2.2Test parameters5447

A.13.4.6.2.3Test Requirements5448

A.14NR standalone tests for Satellite access5449

A.14.1RRC_IDLE state mobility5449

A.14.1.1Cell reselection to FR1 intra-frequency NR case5449

A.14.1.1.1Test Purpose and Environment5449

A.14.1.1.2Test Parameters5449

A.14.1.1.3Test Requirements5450

A.14.1.2Cell reselection to FR1 intra-frequency NR cell for UE configured with the feature for enhanced requirements5451

A.14.1.2.1Test Purpose and Environment5451

A.14.1.2.2Test Parameters5451

A.14.1.2.3Test Requirements5453

A.14.1.3Time-based measurement initiation to FR1 intra-frequency NR cell reselection5453

A.14.1.3.1Test Purpose and Environment5453

A.14.1.3.2Test Parameters5453

A.14.1.3.3Test Requirements5455

A.14.1.4Location-based measurement initiation to FR1 intra-frequency NR cell reselection5455

A.14.1.4.1Test Purpose and Environment5455

A.14.1.4.2Test Parameters5455

A.14.1.4.3Test Requirements5457

A.14.1.5Cell reselection to FR1 inter-frequency NR case5457

A.14.1.5.1Test Purpose and Environment5457

A.14.1.5.2Test Parameters5457

A.14.1.5.3Test Requirements5459

A.14.1.6Cell re-selection to FR1 inter-frequency NR cell for UE configured with feature for enhanced requirements5460

A.14.1.6.1Test Purpose and Environment5460

A.14.1.6.2Test Parameters5460

A.14.1.6.3Test Requirements5462

A.14.1.7Time-based measurement initiation to FR1 inter-frequency cell reselection5462

A.14.1.7.1Test Purpose and Environment5462

A.14.1.7.2Test Parameters5463

A.14.1.7.3Test Requirements5464

A.14.1.8Location-based measurement initiation to FR1 inter-frequency NR cell reselection5464

A.14.1.8.1Test Purpose and Environment5464

A.14.1.8.2Test Parameters5464

A.14.1.8.3Test Requirements5466

A.14.1.9Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion5466

A.14.1.9.1Test Purpose and Environment5466

A.14.1.9.2Test Parameters5466

A.14.1.9.3Test Requirements5468

A.14.1.10Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion5469

A.14.1.10.1Test Purpose and Environment5469

A.14.1.10.2Test Parameters5469

A.14.1.10.3Test Requirements5471

A.14.1.11Cell reselection to FR1 inter-RAT E-UTRAN cells with TN carrier5471

A.14.1.11.1Test purpose and Environment5471

A.14.1.11.2Test parameters5471

A.14.1.11.3Test requirements5473

A.14.1.12Cell re-selection to FR1 inter-frequency NR case with TN carrier5474

A.14.1.12.1Test purpose and Environment5474

A.14.1.12.2Test parameters5474

A.14.1.12.3Test requirements5476

A.14.1.13Cell reselection to FR1 intra-frequency NR case for UE operating on a cell with less than 5 MHz BW5476

A.14.1.13.1Test Purpose and Environment5476

A.14.1.13.2Test Parameters5476

A.14.1.13.3Test Requirements5478

A.14.2RRC_CONNECTED state mobility5478

A.14.2.1Handover5478

A.14.2.1.1Intra-frequency SAN Handover from FR1 to FR15478

A.14.2.1.1.1Test Purpose and Environment5478

A.14.2.1.1.2Test Parameters5478

A.14.2.1.1.3Test Requirements5480

A.14.2.1.2Inter-frequency SAN Handover from FR1 to FR15480

A.14.2.1.2.1Test Purpose and Environment5480

A.14.2.1.2.2Test Parameters5480

A.14.2.1.2.3Test Requirements5482

A.14.2.1.3Intra-frequency SAN time-based conditional Handover from FR1 to FR15482

A.14.2.1.3.1Test Purpose and Environment5482

A.14.2.1.3.2Test Parameters5483

A.14.2.1.3.3Test Requirements5484

A.14.2.1.4Inter-frequency SAN time-based conditional Handover from FR1 to FR15484

A.14.2.1.4.1Test Purpose and Environment5484

A.14.2.1.4.2Test Parameters5485

A.14.2.1.4.3Test Requirements5486

A.14.2.1.5Intra-frequency SAN distance-based conditional Handover from FR1 to FR15486

A.14.2.1.5.1Test Purpose and Environment5487

A.14.2.1.5.2Test Parameters5487

A.14.2.1.5.3Test Requirements5488

A.14.2.1.6Inter-frequency SAN distance-based conditional Handover from FR1 to FR15489

A.14.2.1.6.1Test Purpose and Environment5489

A.14.2.1.6.2Test Parameters5489

A.14.2.1.6.3Test Requirements5491

A.14.2.1.7Intra-frequency intra-satellite Handover from FR2-NTN to FR2-NTN5491

A.14.2.1.7.1Test Purpose and Environment5491

A.14.2.1.7.2Test Parameters5491

A.14.2.1.7.3Test Requirements5493

A.14.2.1.8Intra-frequency SAN Handover from FR1 to FR15494

A.14.2.1.8.1Test Purpose and Environment5494

A.14.2.1.8.2Test Parameters5494

A.14.2.1.8.3Test Requirements5496

A.14.2.1.9Intra-frequency inter-satellite handover from FR2-NTN to FR2-NTN5496

A.14.2.1.9.1Test Purpose and Environment5496

A.14.2.1.9.2Test Parameters5496

A.14.2.1.9.3Test Requirements5498

A.14.2.1.10Intra-frequency SAN Handover from FR1 to FR1 for UE operating on a cell with less than 5 MHz BWA.14.2.1.10.1 Test Purpose and Environment5498

A.14.2.1.10.2Test Parameters5498

A.14.2.1.10.3Test Requirements5500

A.14.2.1.11Intra-frequency SAN time-based conditional Handover from FR1 to FR1 for UE operating on a cell with less than 5 MHz BW5500

A.14.2.11.1Test Purpose and Environment5500

A.14.2.11.2Test Parameters5500

A.14.2.11.3Test Requirements5502

A.14.2.2RRC Connection Mobility Control5502

A.14.2.2.1SA: RRC Re-establishment for SAN5502

A.14.2.2.1.1Intra-frequency RRC Re-establishment in FR15502

A.14.2.2.1.2Inter-frequency RRC Re-establishment in FR15505

A.14.2.2.1.3Inter-frequency RRC Re-establishment in FR1 with 160ms SSB periodicity5507

A.14.2.2.2Random Access5509

A.14.2.2.2.14-step RA type contention based random access test in FR1 for NR standalone5509

A.14.2.2.2.1.1Test Purpose and Environment5509

A.14.2.2.2.1.2Test Requirements5510

A.14.2.2.2.24-step RA type non-contention based random access test in FR1 for NR standalone5512

A.14.2.2.2.2.1Test Purpose and Environment5512

A.14.2.2.2.2.2Test Requirements5513

A.14.2.2.3RRC Connection Release with Redirection5515

A.14.2.2.3.1Redirection from NR in FR1 to NR in FR15515

A.14.2.2.3.1.1Test Purpose and Environment5515

A.14.2.2.3.1.2Test Parameters5515

A.14.2.2.3.1.3Test Requirements5516

A.14.2.2.4RACH-based Hard Satellite switching with re-synchronization from FR1 to FR15517

A.14.2.2.4.1Test Purpose and Environment5517

A.14.2.2.4.2Test Parameters5517

A.14.2.2.4.3Test Requirements5519

A.14.2.2.5RACH-less Soft Satellite switching with re-synchronization from FR1 to FR15519

A.14.2.2.5.1Test Purpose and Environment5519

A.14.2.2.5.2Test Parameters5519

A.14.2.2.5.3Test Requirements5521

A.14.2.2.6RACH-based hard Satellite switching with re-synchronization from FR1 to FR1 for less than 5MHz with NTN5521

A.14.2.2.6.1Test Purpose and Environment5521

A.14.2.2.6.2Test Parameters5521

A.14.2.2.6.3Test Requirements5522

A.14.2.2.7RACH-based Hard Satellite switching with re-synchronization from FR2 to FR25523

A.14.2.2.7.1Test Purpose and Environment5523

A.14.2.2.7.2Test Parameters5523

A.14.2.2.7.3Test Requirements5525

A.14.2.2.8RACH-less Soft Satellite switching with re-synchronization from FR2 to FR25525

A.14.2.2.8.1Test Purpose and Environment5525

A.14.2.2.8.2Test Parameters5525

A.14.2.2.8.3Test Requirements5528

A.14.2.3Intra-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR15528

A.14.2.3.1Test Purpose and Environment5528

A.14.2.3.2Test Parameters5528

A.14.2.3.3Test Requirements5530

A.14.2.4Inter-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR15530

A.14.2.4.1Test Purpose and Environment5530

A.14.2.4.2Test Parameters5530

A.14.2.4.3Test Requirements5532

A.14.3Timing for Satellite Access5532

A.14.3.1UE transmit timing for Satellite Access5532

A.14.3.1.1NR UE Transmit Timing Test for FR15532

A.14.3.1.1.1Test Purpose and environment5532

A.14.3.1.1.2Test requirements5534

A.14.3.1.2NR UE Transmit Timing Test for FR2-NTN5535

A.14.3.1.2.1Test Purpose and environment5535

A.14.3.1.2.2Test requirements5537

A.14.3.2Timing advance for satellite access5538

A.14.3.2.1SA FR1 timing advance adjustment accuracy5538

A.14.3.2.1.1Test Purpose and Environment5538

A.14.3.2.1.2Test Parameters5538

A.14.3.2.1.3Test Requirements5540

A.14.3.2.3SA FR2-NTN timing advance adjustment accuracy5540

A.14.3.2.3.1Test Purpose and Environment5540

A.14.3.2.3.2Test Parameters5540

A.14.3.2.1.3Test Requirements5543

A.14.4Signalling characteristics5543

A.14.4.1Radio link Monitoring5543

A.14.4.1.1Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode5544

A.14.4.1.1.1Test Purpose and Environment5544

A.14.4.1.1.2Test Requirements5546

A.14.4.1.2Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode5546

A.14.4.1.2.1Test Purpose and Environment5546

A.14.4.1.2.2Test Requirements5548

A.14.4.1.3Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode5549

A.14.4.1.3.1Test Purpose and Environment5549

A.14.4.1.3.2Test Requirements5551

A.14.4.1.4Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode5551

A.14.4.1.4.1Test Purpose and Environment5551

A.14.4.1.4.2Test Requirements5554

A.14.4.1.5Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode5554

A.14.4.1.5.1Test Purpose and Environment5554

A.14.4.1.5.2Test Requirements5556

A.14.4.1.6Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode5556

A.14.4.1.6.1Test Purpose and Environment5556

A.14.4.1.6.2Test Requirements5559

A.14.4.1.7Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode5559

A.14.4.1.7.1Test Purpose and Environment5559

A.14.4.1.7.2Test Requirements5562

A.14.4.1.8Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode5562

A.14.4.1.8.1Test Purpose and Environment5562

A.14.4.1.8.2Test Requirements5565

A.14.4.1.9Radio Link Monitoring Out-of-sync Test for FR2 SAN PCell configured with SSB-based RLM RS in non-DRX mode5565

A.14.4.1.9.1Test Purpose and Environment5565

A.14.4.1.9.2Test Requirements5567

A.14.4.1.10Radio Link Monitoring In-sync Test for FR2 SAN PCell configured with SSB-based RLM RS in non-DRX mode5568

A.14.4.1.10.1Test Purpose and Environment5568

A.14.4.1.10.2Test Requirements5570

A.14.4.1.11Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode5570

A.14.4.1.11.1Test Purpose and Environment5570

A.14.4.1.11.2Test Requirements5571

A.14.4.1.12Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode for less than 5 MHz BW5571

A.14.4.1.12.1Test Purpose and Environment5571

A.14.4.1.12.2Test Requirements5572

A.14.4.2Beam Failure Detection and Link recovery procedures for satellite access5573

A.14.4.2.1Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode5573

A.14.4.2.1.1Test Purpose and Environment5573

A.14.4.2.1.2Test Requirements5575

A.14.4.2.2Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode5576

A.14.4.2.2.1Test Purpose and Environment5576

A.14.4.2.2.2Test Requirements5578

A.14.4.2.3Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode5579

A.14.4.2.3.1Test Purpose and Environment5579

A.14.4.2.3.2Test Requirements5581

A.14.4.2.4Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode5582

A.14.4.2.4.1Test Purpose and Environment5582

A.14.4.2.4.2Test Requirements5584

A.14.4.2.5Void5585

A.14.4.2.6Void5585

A.14.4.2.7Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode for a UE operating on a cell with less than 5 MHz BW5585

A.14.4.2.7.1Test Purpose and Environment5585

A.14.4.2.7.2Test Requirements5586

A.14.4.3Active BWP switch for satellite access5586

A.14.4.3.1DCI-based and Timer-based Active BWP Switch5586

A.14.4.3.1.1NR FR1 DL active BWP switch with non-DRX in SA5586

A.14.4.3.1.1.1Test Purpose and Environment5586

A.14.4.3.1.1.2Test Requirements5588

A.14.4.3.2RRC-based Active BWP Switch5589

A.14.4.3.2.1NR FR1 DL active BWP switch of Cell with non-DRX in SA5589

A.14.4.3.2.1.1Test Purpose and Environment5589

A.14.4.3.2.1.2Test Requirements5590

A.14.4.4UE specific CBW change for satellite access5591

A.14.4.4.1UE specific CBW change on PCell in FR1 in non-DRX5591

A.14.4.4.1.1Test Purpose and Environment5591

A.14.4.4.1.2Test Requirements5593

A.14.4.5Pathloss reference signal switching delay5593

A.14.4.5.1MAC-CE based pathloss reference signal switch delay5593

A.14.4.5.1.1Test Purpose and Environment5593

A.14.4.5.1.2Test Requirements5595

A.14.5Measurement procedure5595

A.14.5.1Intra-frequency Measurements5595

A.14.5.1.1SA event triggered reporting tests without gap under non-DRX5596

A.14.5.1.1.1Test purpose and Environment5596

A.14.5.1.1.2Test parameters5596

A.14.5.1.1.3Test Requirements5597

A.14.5.1.2SA event triggered reporting tests without gap under DRX5597

A.14.5.1.2.1Test purpose and Environment5597

A.14.5.1.2.2Test parameters5597

A.14.5.1.2.3Test Requirements5599

A.14.5.1.3SA event triggered reporting tests without gap under non-DRX with SSB index reading5599

A.14.5.1.3.1Test purpose and Environment5599

A.14.5.1.3.2Test parameters5599

A.14.5.1.3.3Test Requirements5601

A.14.5.1.4SA event triggered reporting tests with single measurement gap under non-DRX for satellite access5601

A.14.5.1.4.1Test purpose and Environment5601

A.14.5.1.4.2Test parameters5601

A.14.5.1.4.3Test Requirements5603

A.14.5.1.5SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access5603

A.14.5.1.5.1Test purpose and Environment5603

A.14.5.1.5.2Test parameters5603

A.15.5.1.5.3Test Requirements5605

A.14.5.1.6SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access5605

A.14.5.1.6.1Test purpose and Environment5605

A.14.5.1.6.2Test parameters5605

A.14.5.1.6.3Test Requirements5607

A.14.5.1.7SA event triggered reporting test with SSB time index reading without gap under non-DRX for FR2-NTN5607

A.14.5.1.7.1Test purpose and Environment5607

A.14.5.1.7.2Test parameters5607

A.14.5.1.7.3Test Requirements5609

A.14.5.1.8SA event triggered reporting tests without gap under non-DRX with SSB index reading under less 5MHz BW5609

A.14.5.1.8.1Test purpose and Environment5609

A.14.5.1.8.2Test parameters5609

A.14.5.1.8.3Test Requirements5611

A.14.5.1.9SA event triggered reporting tests without gap under non-DRX5611

A.14.5.1.9.1Test purpose and Environment5611

A.14.5.1.9.2Test parameters5611

A.14.5.1.9.3Test Requirements5613

A.14.5.2Inter-frequency Measurements5613

A.14.5.2.1SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with single gap for satellite access5613

A.14.5.2.1.1Test Purpose and Environment5613

A.14.5.2.1.2Test Requirements5615

A.14.5.2.2SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for satellite access5615

A.14.5.2.2.1Test Purpose and Environment5615

A.14.5.2.2.2Test Requirements5618

A.14.5.2.3SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for satellite access5618

A.14.5.2.3.1Test Purpose and Environment5618

A.14.5.2.3.2Test Requirements5620

A.14.5.2.4SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for satellite access5620

A.14.5.2.4.1Test Purpose and Environment5620

A.14.5.2.4.2Test Requirements5622

A.14.5.2.5void5622

A.14.5.2.5.1void5622

A.14.5.2.5.2void5622

A.14.5.2.6SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for satellite access5623

A.14.5.2.6.1Test Purpose and Environment5623

A.14.5.2.6.2Test Requirements5625

A.14.5.2.7Event triggered reporting test without gap under non-DRX5625

A.14.5.2.7.1Test purpose and Environment5625

A.14.5.2.7.2Test parameters5625

A.14.5.2.7.3Test Requirements5626

A.14.5.2.8Event triggered reporting tests without gap under DRX5626

A.14.5.2.8.1Test purpose and Environment5626

A.14.5.2.8.2Test parameters5627

A.14.5.2.8.3Test Requirements5628

A.14.5.2.9SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used with single gap for 3 MHz channel bandwidth in satellite access5628

A.14.5.2.9.1Test Purpose and Environment5628

A.14.5.2.9.2Test Requirements5630

A.14.5.3L1-RSRP measurement for beam reporting for satellite access5630

A.14.5.3.1SSB based L1-RSRP measurement for satellite access when DRX is not used5630

A.14.5.3.1.1Test Purpose and Environment5630

A.14.5.3.1.2Test parameters5630

A.14.5.3.1.3Test Requirements5632

A.14.5.3.2SSB based L1-RSRP measurement for satellite access when DRX is used5632

A.14.5.3.2.1Test Purpose and Environment5632

A.14.5.3.2.2Test parameters5632

A.14.5.3.2.3Test Requirements5634

A.14.5.3.3CSI-RS based L1-RSRP measurement for satellite access when DRX is not used5634

A.14.5.3.3.1Test Purpose and Environment5634

A.14.5.3.3.2Test parameters5634

A.14.5.3.3.3Test Requirements5636

A.14.5.3.4CSI-RS based L1-RSRP measurement for satellite access when DRX is used5636

A.14.5.3.4.1Test Purpose and Environment5636

A.14.5.3.4.2Test parameters5636

A.14.5.3.4.3Test Requirements5638

A.14.5.3.5SSB based L1-RSRP measurement when DRX is not used in FR2-NTN5638

A.14.5.3.5.1Test Purpose and Environment5638

A.14.5.3.5.2Test parameters5638

A.14.5.3.5.3Test Requirements5640

A.14.6Measurement Performance requirements5640

A.14.6.1SS-RSRP for SAN5640

A.14.6.1.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell5640

A.14.6.1.1.1Test Purpose and Environment5640

A.14.6.1.1.2Test parameters5640

A.14.6.1.1.3Test Requirements5642

A.14.6.1.2SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell5642

A.14.6.1.2.1Test Purpose and Environment5642

A.14.6.1.2.2Test parameters5642

A.14.6.1.2.3Test Requirements5643

A.14.6.1.3SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell5643

A.14.6.1.3.1Test Purpose and Environment5643

A.14.6.1.3.2Test parameters5644

A.14.6.1.3.3Test Requirements5646

A.14.6.2SS-RSRQ5647

A.14.6.2.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access5647

A.14.6.2.1.1Test Purpose and Environment5647

A.14.6.2.1.2Test Parameters5647

A.14.6.2.1.3Test Requirements5648

A.14.6.2.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access5648

A.14.6.2.2.1Test Purpose and Environment5648

A.14.6.2.2.2Test Parameters5648

A.14.6.2.2.3Test Requirements5650

A.14.6.3SS-SINR5650

A.14.6.3.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell5650

A.14.6.3.1.1Test Purpose and Environment5650

A.14.6.3.1.2Test Parameters5650

A.14.6.3.1.3Test Requirements5651

A.14.6.3.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell5652

A.14.6.3.2.1Test Purpose and Environment5652

A.14.6.3.2.2Test Parameters5652

A.14.6.3.2.3Test Requirements5653

A.14.6.4L1-RSRP measurement for beam reporting5653

A.14.6.4.1SSB based L1-RSRP measurement5653

A.14.6.4.1.1Test Purpose and Environment5653

A.14.6.4.1.2Test parameters5653

A.14.6.4.1.3Test Requirements5655

A.14.6.4.2CSI-RS based L1-RSRP measurement on resource set with repetition off5655

A.14.6.4.2.1Test Purpose and Environment5655

A.14.6.4.2.2Test parameters5655

A.14.6.4.2.3Test Requirements5656

A.14.6.4.3SSB based L1-RSRP measurement for VSAT UE in FR2-NTN when DRX is not used5656

A.14.6.4.3.1Test Purpose and Environment5656

A.14.6.4.3.2Test parameters5656

A.14.6.4.3.3Test Requirements5658

A.15NR standalone tests with one or more NR cells in FR2-25659

A.15.1SA: RRC_IDLE state mobility5659

A.15.1.1Cell re-selection to NR5659

A.15.1.1.1Cell re-selection to FR2-2 intra-frequency NR case5659

A.15.1.1.1.1Test Purpose and Environment5659

A.15.1.1.1.2Test Parameters5659

A.15.1.1.1.3Test Requirements5661

A.15.1.2Cell re-selection to FR2-2 inter-frequency NR case5661

A.15.1.2.1Test Purpose and Environment5661

A.15.1.2.2Test Parameters5662

A.15.1.2.3Test Requirements5664

A.15.1.3Cell re-selection to FR2-2 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion5664

A.15.1.3.1Test Purpose and Environment5664

A.15.1.3.2Test Parameters5664

A.15.1.3.3Test Requirements5666

A.15.1.4Cell re-selection to FR2-2 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion5667

A.15.1.4.1Test Purpose and Environment5667

A.15.1.4.2Test Parameters5667

A.15.1.4.3Test Requirements5669

A.15.1.5Cell re-selection to FR2-2 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion5669

A.15.1.5.1Test Purpose and Environment5669

A.15.1.5.2Test Parameters5669

A.15.1.5.3Test Requirements5671

A.15.1.6Cell re-selection to FR2-2 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion5672

A.15.1.6.1Test Purpose and Environment5672

A.15.1.6.2Test Parameters5672

A.15.1.6.3Test Requirements5674

A.15.2Signaling characteristics5674

A.15.2.1SCell Activation and Deactivation Delay5674

A.15.2.1.1SCell Activation and deactivation for SCell in FR2-2 intra-band in non-DRX5674

A.15.2.1.1.1Test Purpose and Environment5674

A.15.2.1.1.2Test Requirements5676

A.15.2.1.2SCell Activation and deactivation for FR1+FR2-2 inter-band with target SCell in FR2-25676

A.15.2.1.2.1Test Purpose and Environment5676

A.15.2.1.2.2Test Requirements5679

A.15.2.1.3SCell Activation and deactivation for SCell in FR2-2 inter-band in non-DRX5679

A.15.2.1.3.1Test Purpose and Environment5680

A.15.2.1.3.2Test Requirements5682

A.15.2.1.4Direct SCell activation at SCell addition of known SCell in FR2-25683

A.15.2.1.4.1Test Purpose and Environment5683

A.15.2.1.4.2Test Requirements5685

A.15.2.1.5Direct SCell activation at handover with known SCell in FR2-25686

A.15.2.1.5.1Test Purpose and Environment5686

A.15.2.1.5.2Test Requirements5688

A.15.3RRC_CONNECTED state mobility5689

A.15.3.1Handover5689

A.15.3.1.1Intra-frequency handover from FR2-2 carrier with CCA to FR2-2 carrier with CCA; unknown target cell5689

A.15.3.1.1.1Test Purpose and Environment5689

A.15.3.1.1.2Test Parameters5689

A.15.3.1.1.3Test Requirements5691

A.15.3.1.2Inter-frequency handover from FR1 to FR2-2 carrier with CCA; unknown target cell5692

A.15.3.1.2.1Test Purpose and Environment5692

A.15.3.1.2.2Test Parameters5692

A.15.3.1.2.3Test Requirements5694

A.15.4Measurement procedure5694

A.15.4.1Intra-frequency Measurements5694

A.15.4.1.1SA event triggered reporting test without gap under non-DRX for FR2-2 with CCA5694

A.15.4.1.1.1Test purpose and Environment5694

A.15.4.1.1.2Test Requirements5697

A.15.4.2Inter-frequency Measurements5698

A.15.4.2.1SA event triggered reporting tests for FR2-2 with CCA without SSB time index detection when DRX is not used (PCell in FR2-2)5698

A.15.4.2.1.1Test Purpose and Environment5698

A.15.4.2.1.2Test Requirements5700

A.16NR standalone tests with all NR cells in FR1 for RedCap5701

A.16.1SA: RRC_IDLE state mobility for RedCap5701

A.16.1.1Cell re-selection to NR5701

A.16.1.1.1Cell re-selection to FR1 intra-frequency NR case for 1 Rx UE5701

A.16.1.1.1.1Test Purpose and Environment5701

A.16.1.1.1.2Test Parameters5701

A.16.1.1.1.3Test Requirements5703

A.16.1.1.2Cell re-selection to FR1 intra-frequency NR case for 2 Rx UE5704

A.16.1.1.2.1Test Purpose and Environment5704

A.16.1.1.2.2Test Parameters5704

A.16.1.1.2.3Test Requirements5706

A.16.1.1.3Cell re-selection to FR1 inter-frequency NR case for 1 Rx UE5706

A.16.1.1.3.1Test Purpose and Environment5706

A.16.1.1.3.2Test Parameters5706

A.16.1.1.3.3Test Requirements5709

A.16.1.1.4Cell re-selection to FR1 inter-frequency NR case for 2 Rx UE5709

A.16.1.1.4.1Test Purpose and Environment5709

A.16.1.1.4.2Test Parameters5709

A.16.1.1.4.3Test Requirements5712

A.16.1.1.5Cell re-selection to FR1 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE5712

A.16.1.1.5.1Test Purpose and Environment5712

A.16.1.1.5.2Test Parameters5712

A.16.1.1.5.3Test Requirements5715

A.16.1.1.6Cell re-selection to FR1 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE5715

A.16.1.1.6.1Test Purpose and Environment5715

A.16.1.1.6.2Test Parameters5715

A.16.1.1.6.3Test Requirements5717

A.16.1.1.7Cell re-selection to FR1 inter-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE5718

A.16.1.1.7.1Test Purpose and Environment5718

A.16.1.1.7.2Test Parameters5718

A.16.1.1.7.3Test Requirements5720

A.16.1.1.8Cell re-selection to FR1 inter-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE5721

A.16.1.1.8.1Test Purpose and Environment5721

A.16.1.1.8.2Test Parameters5721

A.16.1.1.8.3Test Requirements5723

A.16.1.2Inter-RAT E-UTRAN cell re-selection for RedCap5724

A.16.1.2.1Cell re-selection to higher priority E-UTRAN for 1 RX5724

A.16.1.2.1.1Test Purpose and Environment5724

A.16.1.2.1.2Test Parameters5724

A.16.1.2.1.3Test Requirements5727

A.16.1.2.2Cell re-selection to higher priority E-UTRAN for 2 RX5727

A.16.1.2.2.1Test Purpose and Environment5727

A.16.1.2.2.2Test Parameters5727

A.16.1.2.2.3Test Requirements5730

A.16.1.2.3.1Test Purpose and Environment5730

A. 16.1.2.3.2Test Parameters5730

A.16.1.2.3.3Test Requirements5733

A.16.1.2.4.1Test Purpose and Environment5733

A.16.1.2.4.2Test Parameters5733

A.16.1.3.1.3Test Requirements5736

A.16.1.2.5Cell re-selection to lower priority E-UTRAN for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE5736

A.16.1.2.5.1Test Purpose and Environment5736

A.16.1.2.5.2Test Parameters5736

A.16.1.2.5.3Test Requirements5739

A.16.1.2.6Cell re-selection to lower priority E-UTRAN for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE5739

A.16.1.2.6.1Test Purpose and Environment5740

A.16.1.2.6.2Test Parameters5740

A.16.1.2.6.3Test Requirements5742

A.16.2SA: RRC_INACTIVE state mobility for RedCap5743

A.16.2.1Configured Grant based Small Data Transmissions (CG-SDT) for RedCap5743

A.16.2.1.1NR UE CG-SDT Test in FR1 for 1 Rx RedCap UE5743

A.16.2.1.1.1Test purpose and Environment5743

A.16.2.1.1.2Test Parameters5744

A.16.2.1.1.3Test requirements5746

A.16.2.1.2NR UE CG-SDT Test in FR1 for 2 Rx RedCap UE5746

A.16.2.1.2.1Test purpose and Environment5746

A.16.2.1.2.2Test Parameters5748

A.16.2.1.2.3Test requirements5749

A.16.2.2Cell Reselection for Positioning5750

A.16.2.2.1Cell re-selection to FR1 intra-frequency NR case with RRC_INACTIVE eDRX and positioning SRS5750

A.16.2.2.1.1Test Purpose and Environment5750

A.16.2.2.1.2Test Parameters5750

A.16.2.2.1.3Test Requirements5753

A.16.3RRC_CONNECTED state mobility for RedCap5753

A.16.3.1Handover5753

A.16.3.1.1Intra-frequency handover from FR1 to FR1; known target cell for 1 Rx UE5753

A.16.3.1.1.1Test Purpose and Environment5753

A.16.3.1.1.2Test Parameters5753

A.16.3.1.1.3Test Requirements5755

A.16.3.1.2Intra-frequency handover from FR1 to FR1; known target cell for 2 Rx UE5755

A.16.3.1.2.1Test Purpose and Environment5755

A.16.3.1.2.2Test Parameters5755

A.16.3.1.2.3Test Requirements5757

A.16.3.1.3Intra-frequency handover from FR1 to FR1; unknown target cell for 1 Rx UE5757

A.16.3.1.3.1Test Purpose and Environment5757

A.16.3.1.3.2Test Parameters5758

A.16.3.1.3.3Test Requirements5760

A.16.3.1.4Intra-frequency handover from FR1 to FR1; unknown target cell for 2 Rx UE5760

A.16.3.1.4.1Test Purpose and Environment5760

A.16.3.1.4.2Test Parameters5760

A.16.3.1.5Inter-frequency handover from FR1 to FR1; unknown target cell for 1 Rx UE5762

A.16.3.1.5.1Test Purpose and Environment5762

A.16.3.1.5.2Test Parameters5762

A.16.3.1.5.3Test Requirements5764

A.16.3.1.6Inter-frequency handover from FR1 to FR1; unknown target cell for 2 Rx UE5765

A.16.3.1.6.1Test Purpose and Environment5765

A.16.3.1.6.2Test Parameters5765

A.16.3.1.6.3Test Requirements5767

A.16.3.1.7SA NR - E-UTRAN handover for 1 Rx UE5767

A.16.3.1.7.1Test Purpose and Environment5767

A.16.3.1.7.2Test Requirements5771

A.16.3.1.8SA NR - E-UTRAN handover for 2 Rx UE5771

A.16.3.1.8.1Test Purpose and Environment5771

A.16.3.1.8.2Test Requirements5774

A.16.3.1.9SA NR - E-UTRAN handover with unknown target cell for 1 Rx UE5774

A.16.3.1.9.1Test Purpose and Environment5774

A.16.3.1.9.2Test Requirements5777

A.16.3.1.10SA NR - E-UTRAN handover with unknown target cell for 2 Rx UE5777

A.16.3.1.10.1Test Purpose and Environment5778

A.16.3.1.10.2Test Requirements5781

A.16.3.2RRC Connection Mobility Control5781

A.16.3.2.1SA: RRC Re-establishment5781

A.16.3.2.1.1Intra-frequency RRC Re-establishment in FR1 for 1 Rx UE5781

A.16.3.2.1.2Intra-frequency RRC Re-establishment in FR1 for 2 Rx UE5784

A.16.3.2.1.3Inter-frequency RRC Re-establishment in FR1 for 1 Rx UE5787

A.16.3.2.1.4Inter-frequency RRC Re-establishment in FR1 for 2 Rx UE5790

A.16.3.2.1.5Intra-frequency RRC Re-establishment in FR1 for 1 Rx UE without serving cell timing5793

A.16.3.2.1.6Intra-frequency RRC Re-establishment in FR1 for 2 Rx UE without serving cell timing5795

A.16.3.2.2Random Access5798

A.16.3.2.2.14-step RA type contention based random access test in FR1 for NR standalone for 1 Rx UE5798

A.16.3.2.2.24-step RA type contention based random access test in FR1 for NR standalone for 2 Rx UE5802

A.16.3.2.2.34-step RA type non-contention based random access test in FR1 for NR standalone for 1 Rx UE5805

A.16.3.2.2.44-step RA type non-contention based random access test in FR1 for NR standalone for 2 Rx UE5808

A.16.3.2.2.52-step RA type contention based random access test in FR1 for NR standalone for 1 Rx UE5811

A.16.3.2.2.62-step RA type contention based random access test in FR1 for NR standalone for 2 Rx UE5814

A.16.3.2.2.72-step RA type non-contention based test in FR1 for NR standalone for 1 RX UE5817

A.16.3.2.2.82-step RA type non-contention based test in FR1 for NR standalone for 2 RX UE5820

A.16.3.2.3SA: RRC Connection Release with Redirection5822

A.16.3.2.3.1Redirection from NR in FR1 to NR in FR1 for 1 Rx UE5822

A.16.3.2.3.2Redirection from NR in FR1 to NR in FR1 for 2 Rx UE5825

A.16.3.2.3.3Redirection from NR in FR1 to E-UTRAN for 1 Rx UE5827

A.16.3.2.3.4Redirection from NR in FR1 to E-UTRAN for 2 Rx UE5830

A.16.4Timing for RedCap5834

A.16.4.1UE transmit timing5834

A.16.4.1.1NR UE Transmit Timing Test for FR1 for 1 Rx RedCap UE5834

A.16.4.1.1.1Test Purpose and environment5834

A.16.4.1.1.2Test requirements5836

A.16.4.1.2NR UE Transmit Timing Test for FR1 for 2 Rx RedCap UE5836

A.16.4.1.2.1Test Purpose and environment5836

A.16.4.1.2.2Test requirements5838

A.16.4.2Void5838

A.16.4.3Timing advance5838

A.16.4.3.1SA FR1 timing advance adjustment accuracy for 1 Rx UE5838

A.16.4.3.1.1Test Purpose and Environment5838

A.16.4.3.1.2Test Parameters5838

A.16.4.3.1.3Test Requirements5841

A.16.4.3.2SA FR1 timing advance adjustment accuracy for 2 Rx UE5841

A.16.4.3.2.1Test Purpose and Environment5841

A.16.4.3.2.2Test Parameters5841

A.16.4.3.2.3Test Requirements5843

A.16.5Signalling characteristics for RedCap5844

A.16.5.1Radio link Monitoring5844

A.16.5.1.1Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 1 Rx UE5844

A.16.5.1.1.1Test Purpose and Environment5844

A.16.5.1.1.2Test Requirements5846

A.16.5.1.2Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 2 Rx UE5847

A.16.5.1.2.1Test Purpose and Environment5847

A.16.5.1.2.2Test Requirements5849

A.16.5.1.3Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 1 Rx UE5850

A.16.5.1.3.1Test Purpose and Environment5850

A.16.5.1.3.2Test Requirements5852

A.16.5.1.4Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 2 Rx UE5853

A.16.5.1.4.1Test Purpose and Environment5853

A.16.5.1.4.2Test Requirements5855

A.16.5.1.5Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 1 Rx UE5856

A.16.5.1.5.1Test Purpose and Environment5856

A.16.5.1.5.2Test Requirements5858

A.16.5.1.6Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 2 Rx UE5858

A.16.5.1.6.1Test Purpose and Environment5858

A.16.5.1.6.2Test Requirements5861

A.16.5.1.7Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 1 Rx UE5861

A.16.5.1.7.1Test Purpose and Environment5861

A.16.5.1.7.2Test Requirements5864

A.16.5.1.8Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 2 Rx UE5865

A.16.5.1.8.1Test Purpose and Environment5865

A.16.5.1.8.2Test Requirements5868

A.16.5.1.9Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 1 Rx UE5868

A.16.5.1.9.1Test Purpose and Environment5868

A.16.5.1.9.2Test Requirements5871

A.16.5.1.10Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 2 Rx UE5871

A.16.5.1.10.1Test Purpose and Environment5871

A.16.5.1.10.2Test Requirements5874

A.16.5.1.11Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 1 Rx UE5874

A.16.5.1.11.1Test Purpose and Environment5874

A.16.5.1.11.2Test Requirements5877

A.16.5.1.12Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 2 Rx UE5877

A.16.5.1.12.1Test Purpose and Environment5877

A.16.5.1.12.2Test Requirements5880

A.16.5.1.13Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 1 Rx UE5881

A.16.5.1.13.1Test Purpose and Environment5881

A.16.5.1.13.2Test Requirements5883

A.16.5.1.14Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 2 Rx UE5884

A.16.5.1.14.1Test Purpose and Environment5884

A.16.5.1.14.2Test Requirements5886

A.16.5.1.15Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 1 Rx UE5887

A.16.5.1.15.1Test Purpose and Environment5887

A.16.5.1.15.2Test Requirements5890

A.16.5.1.16Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 2 Rx UE5890

A.16.5.1.16.1Test Purpose and Environment5890

A.16.5.1.16.2Test Requirements5893

A.16.5.2Beam Failure Detection and Link recovery procedures5893

A.16.5.2.1Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for 1 Rx UE5893

A.16.5.2.1.1Test Purpose and Environment5893

A.16.5.2.1.2Test Requirements5896

A.16.5.2.2Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for 2 Rx UE5897

A.16.5.2.2.1Test Purpose and Environment5897

A.16.5.2.2.2Test Requirements5900

A.16.5.2.3Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode for 1 Rx UE5900

A.16.5.2.3.1Test Purpose and Environment5900

A.16.5.2.3.2Test Requirements5903

A.16.5.2.4Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode for 2 Rx UE5904

A.16.5.2.4.1Test Purpose and Environment5904

A.16.5.2.4.2Test Requirements5907

A.16.5.2.5Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode for 1 Rx UE5907

A.16.5.2.5.1Test Purpose and Environment5907

A.16.5.2.5.2Test Requirements5910

A.16.5.2.6Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode for 2 Rx UE5911

A.16.5.2.6.1Test Purpose and Environment5911

A.16.5.2.6.2Test Requirements5914

A.16.5.2.7Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode for 1 Rx UE5914

A.16.5.2.7.1Test Purpose and Environment5914

A.16.5.2.7.2Test Requirements5917

A.16.5.2.8Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode for 2 Rx UE5918

A.16.5.2.8.1Test Purpose and Environment5918

A.16.5.2.8.2Test Requirements5921

A.16.5.3Active BWP switch5921

A.16.5.3.1DCI-based and Timer-based Active BWP Switch5921

A.16.5.3.1.1NR FR1 DL active BWP switch with non-DRX in SA for 1 Rx UE5921

A.16.5.3.1.1.1Test Purpose and Environment5921

A.16.5.3.1.1.2Test Requirements5924

A.16.5.3.1.2NR FR1 DL active BWP switch with non-DRX in SA for 2 Rx UE5924

A.16.5.3.1.2.1Test Purpose and Environment5924

A.16.5.3.1.2.2Test Requirements5926

A.16.5.3.2RRC-based Active BWP Switch5927

A.16.5.3.2.1NR FR1 DL active BWP switch of Cell with non-DRX in SA for 1 Rx UE5927

A.16.5.3.2.1.1Test Purpose and Environment5927

A.16.5.3.2.1.2Test Requirements5929

A.16.5.3.2.2NR FR1 DL active BWP switch of Cell with non-DRX in SA for 2 Rx UE5929

A.16.5.3.2.2.1Test Purpose and Environment5929

A.16.5.3.2.2.2Test Requirements5931

A.16.5.4UE specific CBW change5932

A.16.5.4.1UE specific CBW change on PCell in FR1 in non-DRX for 1 Rx UE5932

A.16.5.4.1.1Test Purpose and Environment5932

A.16.5.4.1.2Test Requirements5934

A.16.5.4.2UE specific CBW change on PCell in FR1 in non-DRX for 2 Rx UE5934

A.16.5.4.2.1Test Purpose and Environment5934

A.16.5.4.2.2Test Requirements5937

A.16.6Measurement procedure for RedCap5937

A.16.6.1Intra-frequency Measurements5937

A.16.6.1.1SA event triggered reporting tests without gap under non-DRX for 1 Rx UE5937

A.16.6.1.1.1Test purpose and Environment5937

A.16.6.1.1.2Test parameters5937

A.16.6.1.1.3Test Requirements5939

A.16.6.1.2SA event triggered reporting tests without gap under non-DRX for 2 Rx UE5939

A.16.6.1.2.1Test purpose and Environment5939

A.16.6.1.2.2Test parameters5939

A.16.6.1.2.3Test Requirements5941

A.16.6.1.3SA event triggered reporting tests without gap under DRX for 1 Rx UE5941

A.16.6.1.3.1Test purpose and Environment5941

A.16.6.1.3.2Test parameters5941

A.16.6.1.3.3Test Requirements5943

A.16.6.1.4SA event triggered reporting tests without gap under DRX for 2 Rx UE5944

A.16.6.1.4.1Test purpose and Environment5944

A.16.6.1.4.2Test parameters5944

A.16.6.1.4.3Test Requirements5946

A.16.6.1.5SA event triggered reporting tests with per-UE gaps under non-DRX for 1 Rx UE5946

A.16.6.1.5.1Test purpose and Environment5946

A.16.6.1.5.2Test parameters5946

A.16.6.1.5.3Test Requirements5948

A.16.6.1.6SA event triggered reporting tests with per-UE gaps under non-DRX for 2 Rx UE5948

A.16.6.1.6.1Test purpose and Environment5948

A.16.6.1.6.2Test parameters5948

A.16.6.1.6.3Test Requirements5950

A.16.6.1.7SA event triggered reporting tests with per-UE gaps under DRX for 1 Rx UE5951

A.16.6.1.7.1Test purpose and Environment5951

A.16.6.1.7.2Test parameters5951

A.16.6.1.7.3Test Requirements5953

A.16.6.1.8SA event triggered reporting tests with per-UE gaps under DRX for 2 Rx UE5953

A.16.6.1.8.1Test purpose and Environment5953

A.16.6.1.8.2Test parameters5953

A.16.6.1.8.3Test Requirements5955

A.16.6.1.9SA event triggered reporting tests without gap under non-DRX with SSB index reading for 1 Rx UE5955

A.16.6.1.9.1Test purpose and Environment5955

A.16.6.1.9.2Test parameters5956

A.16.6.1.9.3Test Requirements5957

A.16.6.1.10SA event triggered reporting tests without gap under non-DRX with SSB index reading for 2 Rx UE5957

A.16.6.1.10.1Test purpose and Environment5957

A.16.6.1.10.2Test parameters5957

A.16.6.1.10.3Test Requirements5959

A.16.6.1.11SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading for 1 Rx UE5959

A.16.6.1.11.1Test purpose and Environment5959

A.16.6.1.11.2Test parameters5959

A.16.6.1.11.3Test Requirements5961

A.16.6.1.12SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading for 2 Rx UE5961

A.16.6.1.12.1Test purpose and Environment5961

A.16.6.1.12.2Test parameters5961

A.16.6.1.12.3Test Requirements5962

A.16.6.2Inter-frequency Measurements5963

A.16.6.2.1SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for 1 Rx UE5963

A.16.6.2.1.1Test Purpose and Environment5963

A.16.6.2.1.2Test Requirements5965

A.16.6.2.2SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for 2 Rx UE5966

A.16.6.2.2.1Test Purpose and Environment5966

A.16.6.2.2.2Test Requirements5968

A.16.6.2.3SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used for 1 Rx UE5969

A.16.6.2.3.1Test Purpose and Environment5969

A.16.6.2.3.2Test Requirements5971

A.16.6.2.4SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used for 2 Rx UE5971

A.16.6.2.4.1Test Purpose and Environment5971

A.16.6.2.4.2Test Requirements5973

A.16.6.2.5SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used for 1 Rx UE5974

A.16.6.2.5.1Test Purpose and Environment5974

A.16.6.2.5.2Test Requirements5976

A.16.6.2.6SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used for 2 Rx UE5976

A.16.6.2.6.1Test Purpose and Environment5976

A.16.6.2.6.2Test Requirements5978

A.16.6.2.7SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used for 1 Rx UE5979

A.16.6.2.7.1Test Purpose and Environment5979

A.16.6.2.7.2Test Requirements5981

A.16.6.2.8SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used for 2 Rx UE5981

A.16.6.2.8.1Test Purpose and Environment5981

A.16.6.2.8.2Test Requirements5983

A.16.6.2.9SA event triggered reporting tests with additional mandatory gap pattern for 1 Rx UE5984

A.16.6.2.9.1Test Purpose and Environment5984

A.16.6.2.9.2Test Requirements5986

A.16.6.2.10SA event triggered reporting tests with additional mandatory gap pattern for 2 Rx UE5986

A.16.6.2.10.1Test Purpose and Environment5986

A.16.6.2.10.2Test Requirements5988

A.16.6.2.11SA event triggered reporting tests for FR1 when DRX is used for 1 Rx UE5989

A.16.6.2.11.1Test Purpose and Environment5989

A.16.6.2.11.2Test Requirements5991

A.16.6.2.12SA event triggered reporting tests for FR1 when DRX is used for 2 Rx UE5991

A.16.6.2.12.1Test Purpose and Environment5991

A.16.6.2.12.2Test Requirements5994

A.16.6.3Inter-RAT Measurements5994

A.16.6.3.1SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for 1 Rx UE5994

A.16.6.3.1.1Test purpose and Environment5994

A.16.6.3.1.2Test Requirements5997

A.16.6.3.2SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for 2 Rx UE5998

A.16.6.3.2.1Test purpose and Environment5998

A.16.6.3.2.2Test Requirements6001

A.16.6.3.3SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for 1 Rx UE6001

A.16.6.3.3.1Test purpose and Environment6001

A.16.6.3.3.2Test Requirements6005

A.16.6.3.4SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for 2 Rx UE6005

A.16.6.3.4.1Test purpose and Environment6005

A.16.6.3.4.2Test Requirements6008

A.16.6.4L1-RSRP measurement for beam reporting6009

A.16.6.4.1SSB based L1-RSRP measurement when DRX is not used for 1 Rx UE6009

A.16.6.4.1.1Test Purpose and Environment6009

A.16.6.4.1.2Test parameters6009

A.16.6.4.1.3Test Requirements6010

A.16.6.4.2SSB based L1-RSRP measurement when DRX is not used for 2 Rx UE6011

A.16.6.4.2.1Test Purpose and Environment6011

A.16.6.4.2.2Test parameters6011

A.16.6.4.2.3Test Requirements6012

A.16.6.4.3SSB based L1-RSRP measurement when DRX is used for 1 Rx UE6012

A.16.6.4.3.1Test Purpose and Environment6012

A.16.6.4.3.2Test parameters6013

A.16.6.4.3.3Test Requirements6014

A.16.6.4.4SSB based L1-RSRP measurement when DRX is used for 2 Rx UE6014

A.16.6.4.4.1Test Purpose and Environment6014

A.16.6.4.4.2Test parameters6015

A.16.6.4.4.3Test Requirements6016

A.16.6.4.5CSI-RS based L1-RSRP measurement when DRX is not used for 1 Rx UE6016

A.16.6.4.5.1Test Purpose and Environment6016

A.16.6.4.5.2Test parameters6017

A.16.6.4.5.3Test Requirements6018

A.16.6.4.6CSI-RS based L1-RSRP measurement when DRX is not used for 2 Rx UE6018

A.16.6.4.6.1Test Purpose and Environment6018

A.16.6.4.6.2Test parameters6019

A.16.6.4.6.3Test Requirements6020

A.16.6.4.7CSI-RS based L1-RSRP measurement when DRX is used for 1 Rx UE6020

A.16.6.4.7.1Test Purpose and Environment6020

A.16.6.4.7.2Test parameters6021

A.16.6.4.7.3Test Requirements6022

A.16.6.4.8CSI-RS based L1-RSRP measurement when DRX is used for 2 Rx UE6022

A.16.6.4.8.1Test Purpose and Environment6022

A.16.6.4.8.2Test parameters6023

A.16.6.4.8.3Test Requirements6024

A.16.6.5NR measurements with autonomous gaps6025

A.16.6.5.1SA intra-frequency CGI identification of NR neighbor cell in FR1 for 1 Rx UE6025

A.16.6.5.1.1Test Purpose and Environment6025

A.16.6.5.1.2Test Parameters6025

A.16.6.5.1.3Test Requirements6027

A.16.6.5.2SA intra-frequency CGI identification of NR neighbor cell in FR1 for 2 Rx UE6027

A.16.6.5.2.1Test Purpose and Environment6027

A.16.6.5.2.2Test Parameters6027

A.16.6.5.2.3Test Requirements6029

A.16.6.5.3Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA for 1 Rx UE6029

A.16.6.5.3.1Test Purpose and Environment6029

A.16.6.5.3.2Test Requirements6032

A.16.6.5.4Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA for 2 Rx UE6032

A.16.6.5.4.1Test Purpose and Environment6032

A.16.6.5.4.2Test Requirements6035

A.16.6.6RSTD Measurements6035

A.16.6.6.1NR RSTD measurement reporting delay test case for RedCap UE without FH in FR1 SA6035

A.16.6.6.1.1Test Purpose and Environment6035

A.16.6.6.1.2Test Requirements6040

A.16.6.6.2NR RSTD measurement reporting delay test case with PRS frequency hopping6040

A.16.6.6.2.1Test Purpose and Environment6040

A.16.6.6.2.2Test Requirements6044

A.16.6.7UE Rx-Tx Measurements6045

A.16.6.7.1UE Rx-Tx measurement reporting delay test case for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC_CONNECTED mode6045

A.16.6.7.1.1Test purpose and environment6045

A.16.6.7.1.2Test requirements6049

A.16.6.7.2UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR1 SA in RRC_CONNECTED state6049

A.16.6.7.2.1Test purpose and environment6049

A.16.6.7.2.2Test requirements6053

A.16.6.8PRS-RSRP measurements6053

A.16.6.8.1PRS-RSRP measurement delay test case for single positioning frequency layer6053

A.16.6.8.1.1Test purpose and Environment6053

A.16.6.8.1.2Test Requirements6057

A.16.6.8.2PRS-RSRP measurement delay with FH in RRC_CONNECTED state in FR16057

A.16.6.8.2.1Test purpose and Environment6057

A.16.6.8.2.2Test Requirements6061

A.16.6.9PRS-RSRPP Measurements6061

A.16.6.9.1PRS-RSRPP measurement delay without FH in RRC_CONNECTED state in FR16061

A.16.6.9.1.1Test purpose and Environment6061

A.16.6.9.1.2Test Requirements6063

A.16.6.9.2PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR1 SA in RRC_CONNECTED state6064

A.16.6.9.2.1Test purpose and Environment6064

A.16.6.9.2.2Test Requirements6066

A.16.7Measurement Performance requirements for RedCap6066

A.16.7.1SS-RSRP6066

A.16.7.1.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE6066

A.16.7.1.1.1Test Purpose and Environment6066

A.16.7.1.1.2Test parameters6066

A.16.7.1.1.3Test Requirements6070

A.16.7.1.2SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2 RX UE6070

A.16.7.1.2.1Test Purpose and Environment6070

A.16.7.1.2.2Test parameters6070

A.16.7.1.2.3Test Requirements6074

A.16.7.1.3SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE6074

A.16.7.1.3.1Test Purpose and Environment6074

A.16.7.1.3.2Test parameters6074

A.16.7.1.3.3Test Requirements6077

A.16.7.1.4SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE6077

A.16.7.1.4.1Test Purpose and Environment6077

A.16.7.1.4.2Test parameters6077

A.16.7.1.4.3Test Requirements6080

A.16.7.2SS-RSRQ6080

A.16.7.2.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE6080

A.16.7.2.1.1Test Purpose and Environment6080

A.16.7.2.1.2Test Parameters6080

A.16.7.2.1.3Test Requirements6084

A.16.7.2.2SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE6084

A.16.7.2.2.1Test Purpose and Environment6084

A.16.7.2.2.2Test Parameters6084

A.16.7.2.2.3Test Requirements6087

A.16.7.2.3SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE6087

A.16.7.2.3.1Test Purpose and Environment6087

A.16.7.2.3.2Test parameters6088

A.16.7.2.3.3Test Requirements6091

A.16.7.2.4SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE6091

A.16.7.2.4.1Test Purpose and Environment6091

A.16.7.2.4.2Test parameters6091

A.16.7.2.4.3Test Requirements6095

A.16.7.3SS-SINR6095

A.16.7.3.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE6095

A.16.7.3.1.1Test Purpose and Environment6095

A.16.7.3.1.2Test parameters6095

A.16.7.3.1.3Test Requirements6098

A.16.7.3.2SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE6098

A.16.7.3.2.1Test Purpose and Environment6098

A.16.7.3.2.2Test parameters6098

A.16.7.3.3SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE6101

A.16.7.3.3.1Test Purpose and Environment6101

A.16.7.3.3.2Test parameters6101

A.16.7.3.3.3Test Requirements6104

A.16.7.3.4SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE6104

A.16.7.3.4.1Test Purpose and Environment6104

A.16.7.3.4.2Test parameters6104

A.16.7.3.4.3Test Requirements6107

A.16.7.4L1-RSRP measurement for beam reporting6108

A.16.7.4.1SSB based L1-RSRP measurement for 1 Rx UE6108

A.16.7.4.1.1Test Purpose and Environment6108

A.16.7.4.1.2Test parameters6108

A.16.7.4.1.3Test Requirements6110

A.16.7.4.2SSB based L1-RSRP measurement for 2 Rx UE6110

A.16.7.4.2.1Test Purpose and Environment6110

A.16.7.4.2.2Test parameters6111

A.16.7.4.2.3Test Requirements6111

A.16.7.4.3CSI-RS based L1-RSRP measurement on resource set with repetition off for 1 Rx UE6111

A.16.7.4.3.1Test Purpose and Environment6111

A.16.7.4.3.2Test parameters6111

A.16.7.4.3.3Test Requirements6114

A.16.7.4.4CSI-RS based L1-RSRP measurement on resource set with repetition off for 2 Rx UE6114

A.16.7.4.4.1Test Purpose and Environment6114

A.16.7.4.4.2Test parameters6114

A.16.7.4.4.3Test Requirements6114

A.16.7.5E-UTRAN RSRP6114

A.16.7.5.1SA: inter-RAT measurement accuracy with FR1 serving cell for 1 Rx UE6114

A.16.7.5.1.1Test Purpose and Environment6114

A.16.7.5.1.2Test parameters6114

A.16.7.5.1.3Test Requirements6118

A.16.7.5.2SA: inter-RAT measurement accuracy with FR1 serving cell for 2 Rx UE6118

A.16.7.5.2.1Test Purpose and Environment6118

A.16.7.5.2.2Test parameters6118

A.16.7.5.2.3Test Requirements6121

A.16.7.6E-UTRAN RSRQ6121

A.16.7.6.1SA: inter-RAT measurement accuracy with FR1 serving cell for 1 Rx UE6121

A.16.7.6.1.1Test Purpose and Environment6121

A.16.7.6.1.2Test parameters6121

A.16.7.6.1.3Test Requirements6125

A.16.7.6.2SA: inter-RAT measurement accuracy with FR1 serving cell for 2 Rx UE6125

A.16.7.6.2.1Test Purpose and Environment6125

A.16.7.6.2.2Test parameters6125

A.16.7.6.2.3Test Requirements6128

A.16.7.7RSTD measurements6128

A.16.7.7.1RSTD measurement accuracy test case for RedCap UE without FH6128

A.16.7.7.1.1Test purpose and Environment6128

A.16.7.7.1.2Test Requirements6130

A.16.7.8UE Rx-Tx measurements6134

A.16.7.8.1UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC_CONNECTED mode6134

A.16.7.8.1.1Test purpose and environment6134

A.16.7.8.1.2Test parameters6135

A.16.7.8.1.3Test requirements6138

A.16.7.8.2SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_CONNECTED state in FR16138

A.16.7.8.2.1 Test purpose and Environment6138

A.16.7.8.2.2Test parameters6139

A.16.7.8.2.3Test requirements6142

A.16.7.9PRS-RSRP Measurements6142

A.16.7.9.1PRS-RSRP measurement accuracy without FH in RRC_CONNECTED state in FR16142

A.16.7.9.1.1Test Purpose and Environment6142

A.16.7.9.1.2Test parameters6142

A.16.7.9.1.3Test Requirements6146

A.16.7.9.2PRS-RSRP measurement accuracy with FH in RRC_CONNECTED state in FR16147

A.16.7.9.2.1Test Purpose and Environment6147

A.16.7.9.2.2Test parameters6147

A.16.7.9.2.3Test Requirements6150

A.16.7.10PRS-RSRPP measurements6151

A.16.7.10.1PRS-RSRPP measurement accuracy without FH in RRC_CONNECTED state in FR16151

A.16.7.10.1.1Test Purpose and Environment6151

A.16.7.10.1.2Test parameters6151

A.16.7.10.1.3Test Requirements6154

A.16.7.10.2SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_CONNECTED state in FR16154

A.16.7.10.2.1Test purpose and Environment6154

A.16.7.10.2.2Test parameters6154

A.16.7.10.2.3Test requirements6158

A.16.8Measurement Procedure for RedCap in RRC_INACTIVE6158

A.16.8.1RSTD Measurements6158

A.16.8.1.1NR RSTD measurement reporting delay test case for for RedCap UE without FH in FR1 SA in RRC_INACTIVE state6158

A.16.8.1.1.1Test Purpose and Environment6158

A.16.8.1.1.2Test Requirements6162

A.16.8.1.2NR RSTD measurement reporting delay test case with PRS frequency hopping6162

A.16.8.1.2.1Test Purpose and Environment6162

A.16.8.1.2.2Test Requirements6166

A.16.8.1.3NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state when eDRX cycle > 10.24s for RedCap UE6166

A.16.8.1.3.1Test Purpose and Environment6166

A.16.8.1.3.2Test Requirements6170

A.16.8.2UE Rx-Tx Measurements6170

A.16.8.2.1UE Rx-Tx measurement reporting delay test case for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC_INACTIVE mode6170

A.16.8.2.1.1Test purpose and environment6170

A.16.8.2.1.2Test requirements6174

A.16.8.2.2UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR1 SA in RRC_INACTIVE state6174

A.16.8.2.2.1Test purpose and environment6174

A.16.8.2.2.2Test requirements6178

A.16.8.2.3.UE Rx-Tx time difference measurement for single positioning frequency layer with eDRX > 10.24s in FR1 SA6178

A.16.8.2.3.1Test purpose and environment6178

A.16.8.2.3.2Test requirements6182

A.16.8.3PRS-RSRP Measurements6182

A.16.8.3.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_INACTIVE6182

A.16.8.3.1.1Test purpose and Environment6182

A.16.8.3.1.2Test Requirements6184

A.16.8.3.3PRS-RSRP reporting delay test case in RRC_INACTIVE state in FR1 when eDRX cycle > 10.24s6185

A.16.8.3.3.1Test purpose and Environment6185

A.16.8.3.3.2Test Requirements6187

A.16.8.4PRS-RSRPP Measurements6188

A.16.8.4.1PRS-RSRPP measurement delay without FH in RRC_INACTIVE state in FR16188

A.16.8.4.1.1Test purpose and Environment6188

A.16.8.4.2PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state6191

A.16.8.4.2.1Test purpose and Environment6191

A.16.8.4.2.2Test Requirements6193

A.16.9Measurement Performance Requirements for RedCap in RRC_INACTIVE6196

A.16.9.1 RSTD Measurements6196

A.16.9.1.1RSTD measurement accuracy test case for RedCap UE without FH in FR1 in RRC_INACTIVE state6196

A.16.9.1.1.1Test purpose and Environment6196

A.16.9.1.1.2Test Requirements6198

A.16.9.1.2RSTD measurement accuracy test case for RedCap UE with FH in FR1 in RRC_INACTIVE state6198

A.16.9.1.2.1Test purpose and Environment6198

A.16.9.1.2.2Test Requirements6200

A.16.9.2UE Rx-Tx measurements6200

A.16.9.2.1UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC_INACTIVE mode6200

A.16.9.2.1.1Test purpose and environment6200

A.16.9.2.1.2Test parameters6201

A.16.9.2.1.3Test requirements6203

A.16.9.2.2SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_INACTIVE state in FR16203

A.16.9.2.2.1Test purpose and Environment6203

A.16.9.2.2.2Test parameters6203

A.16.9.2.2.3Test requirements6206

A.16.9.3PRS-RSRP Measurements6206

A.16.9.3.1PRS-RSRP measurement accuracy without FH in RRC_INACTIVE state in FR16206

A.16.9.3.1.1Test Purpose and Environment6206

A.16.9.3.1.2Test parameters6206

A.16.9.3.1.3Test Requirements6209

A.16.9.3.2PRS-RSRP measurement accuracy with FH in RRC_INACTIVE state in FR16209

A.16.9.3.2.1Test Purpose and Environment6209

A.16.9.3.2.2Test parameters6209

A.16.9.3.2.3Test Requirements6212

A.16.9.4PRS-RSRPP measurements6212

A.16.9.4.1PRS-RSRPP measurement accuracy without Rx FH in RRC_INACTIVE state in FR16212

A.16.9.4.1.1Test purpose and Environment6212

A.16.9.4.1.2Test parameters6212

A.16.9.4.1.3Test requirements6216

A.16.9.4.2SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_INACTIVE state in FR16216

A.16.9.4.2.1Test purpose and Environment6216

A.16.9.4.2.2Test parameters6216

A.16.9.4.2.3Test requirements6219

A.16.10 Measurement procedure for RedCap in RRC_IDLE6219

A.16.10.1RSTD measurements6219

A.16.10.1.1NR RSTD measurement reporting delay test case for RedCap UE without FH in FR1 SA in RRC_IDLE state without eDRX6219

A.16.10.1.1.1Test Purpose and Environment6219

A.16.10.1.1.2Test Requirements6223

A.16.10.1.2NR RSTD measurement reporting delay test case for RedCap UE without RX FH in FR1 SA in RRC_IDLE state when eDRX > 10.24s6223

A.16.10.1.2.1Test Purpose and Environment6223

A.16.10.1.2.2Test Requirements6227

A.16.10.2PRS-RSRP Measurements6227

A.16.10.2.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_IDLE6227

A.16.10.2.1.1Test purpose and Environment6227

A.16.10.2.1.2Test Requirements6229

A.16.10.2.2PRS-RSRP measurement without Rx FH reporting delay test case for single positioning frequency layer in FR1 SA in RRC_IDLE state with eDRX cycle > 10.24s6230

A.16.10.2.2.1Test purpose and Environment6230

A.16.10.2.2.2Test Requirements6232

A.16.11 Measurement Performance Requirements for RedCap in RRC_IDLE6232

A.16.11.1RSTD Measurements6232

A.16.11.1.1RSTD measurement accuracy test case for RedCap UE without FH in FR1 in RRC_IDLE state without eDRX6232

A.16.11.1.1.1Test purpose and Environment6232

A.16.11.1.1.2Test Requirements6234

A.16.11.1.2RSTD measurement accuracy test case for RedCap UE without FH in FR1 in RRC_IDLE state with eDRX > 10.24s6235

A.16.11.1.2.1Test purpose and Environment6235

A.16.11.1.2.2Test Requirements6237

A.16.11.2PRS-RSRP Measurements6237

A.16.11.2.1PRS-RSRP measurement accuracy test case for RedCap UE in FR1 in RRC_IDLE state6237

A.16.11.2.1.1Test Purpose and Environment6237

A.16.11.2.1.2Test parameters6237

A.16.11.2.1.3Test Requirements6239

A.16.11.2.2PRS-RSRP measurement without Rx FH accuracy test case for single positioning frequency layer in FR1 SA in RRC_IDLE state with eDRX cycle > 10.24s6239

A.16.11.2.2.1Test purpose and Environment6239

A.16.11.2.2.2Test Requirements6241

A.17NR standalone tests with one or more NR cells in FR2 for RedCap6242

A.17.1SA: RRC_IDLE state mobility for RedCap6242

A.17.1.1Cell re-selection to NR6242

A.17.1.1.1Cell reselection to FR2 intra-frequency NR case for 2 Rx6242

A.17.1.1.1.1Test Purpose and Environment6242

A.17.1.1.1.2Test Parameters6242

A.17.1.1.1.3Test Requirements6244

A.17.1.1.2Cell reselection to FR2 inter-frequency NR case6244

A.17.1.1.2.1Test Purpose and Environment6244

A.17.1.1.2.2Test Parameters6244

A.17.1.1.2.3Test Requirements6246

A.17.1.1.3Cell reselection to FR2 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE6247

A.17.1.1.3.1Test Purpose and Environment6247

A.17.1.1.3.2Test Parameters6247

A.17.1.1.3.3Test Requirements6249

A.17.1.1.4Cell reselection to FR2 inter-frequency NR case for UE fulfilling stationary mobility relaxed measurement criterion for 2 Rx UE6249

A.17.1.1.4.1Test Purpose and Environment6249

A.17.1.1.4.2Test Parameters6249

A.17.1.1.4.3Test Requirements6251

A.17.2SA: RRC_INACTIVE state mobility for RedCap6252

A.17.2.1Configured Grant based Small Data Transmissions (CG-SDT) for RedCap6252

A.17.2.1.1TA validation for CG-SDT in FR2 for RedCap6252

A.17.2.1.1.1Test Purpose and Environment6252

A.17.2.1.1.2Test Requirements6255

A.17.2.2Cell Reselection for Positioning6255

A.17.2.2.1Cell reselection to FR2 intra-frequency NR case with RRC_INACTIVE eDRX and positioning SRS6255

A.17.2.2.1.1Test Purpose and Environment6255

A.17.2.2.1.2Test Parameters6255

A.17.2.2.1.3Test Requirements6255

A.17.3RRC_CONNECTED state mobility for RedCap6255

A.17.3.1Handover for RedCap6255

A.17.3.1.1Intra-frequency handover from FR2 to FR2; unknown target cell for 2 Rx6255

A.17.3.1.1.1Test Purpose and Environment6255

A.17.3.1.1.2Test Parameters6255

A.17.3.1.1.3Test Requirements6257

A.17.3.1.2Inter-frequency handover from FR2 to FR2; unknown target cell for 2 Rx6257

A.17.3.1.2.1Test Purpose and Environment6257

A.17.3.1.2.2Test Parameters6257

A.17.3.1.2.3 Test Requirements6259

A.17.3.2RRC Connection Mobility Control for RedCap6259

A.17.3.2.1SA: RRC Re-establishment6259

A.17.3.2.1.1Intra-frequency RRC Re-establishment in FR26259

A.17.3.2.1.1.1Test Purpose and Environment6259

A.17.3.2.1.2Inter-frequency RRC Re-establishment in FR26261

A.17.3.2.1.2.1Test Purpose and Environment6261

A.17.3.2.1.3Intra-frequency RRC Re-establishment in FR2 without serving cell timing6263

A.17.3.2.1.3.1Test Purpose and Environment6263

A.17.3.2.1.3.2Test Requirements6265

A.17.3.2.2Random Access6265

A.17.3.2.2.14-step RA type contention based random access test in FR2 for NR Standalone6265

A.17.3.2.2.1.1Test Purpose and Environment6265

A.17.3.2.2.1.2Test Requirements6267

A.17.3.2.2.24-step RA type non-contention based random access test in FR2 for NR Standalone6269

A.17.3.2.2.2.1Test Purpose and Environment6269

A.17.3.2.2.2.2Test Requirements6270

A.17.3.2.2.32-step RA type contention based random access test in FR2 for NR Standalone6272

A.17.3.2.2.3.1Test Purpose and Environment6272

A.17.3.2.2.3.2Test Requirements6273

A.17.3.2.2.42-step RA type non-contention based random access test in FR2 for NR Standalone6274

A.17.3.2.2.4.1Test Purpose and Environment6274

A.17.3.2.2.4.2Test Requirements6276

A.17.3.2.3SA: RRC Connection Release with Redirection6277

A.17.3.2.3.1Redirection from NR in FR2 to NR in FR26277

A.17.3.2.3.1.1Test Purpose and Environment6277

A.17.3.2.3.1.2Test Parameters6277

A.17.3.2.3.1.3Test Requirements6279

A.17.4Timing6279

A.17.4.1UE transmit timing6279

A.17.4.1.1NR UE Transmit Timing Test for FR26279

A.17.4.1.1.1Test Purpose and environment6279

A.17.4.1.1.2Test requirements6281

A.17.4.2UE timer accuracy6282

A.17.4.3Timing advance6282

A.17.4.3.1SA FR2 timing advance adjustment accuracy6282

A.17.4.3.1.1Test Purpose and Environment6282

A.17.4.3.1.2Test Parameters6282

A.17.4.3.1.3 Test Requirements6285

A.17.5Signaling characteristics for RedCap6285

A.17.5.1Radio link Monitoring for RedCap6285

A.17.5.1.1Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode6285

A.17.5.1.1.1Test Purpose and Environment6285

A.17.5.1.1.2Test Requirements6288

A.17.5.1.2Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode6288

A.17.5.1.2.1Test Purpose and Environment6288

A.17.5.1.2.2Test Requirements6291

A.17.5.1.3Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode6291

A.17.5.1.3.1Test Purpose and Environment6291

A.17.5.1.3.2Test Requirements6294

A.17.5.1.4Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode6294

A.17.5.1.4.1Test Purpose and Environment6294

A.17.5.1.4.2Test Requirements6296

A.17.5.1.5Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode6297

A.17.5.1.5.1Test Purpose and Environment6297

A.17.5.1.5.2Test Requirements6299

A.17.5.1.6Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode6300

A.17.5.1.6.1Test Purpose and Environment6300

A.17.5.1.6.2Test Requirements6302

A.17.5.1.7Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode6303

A.17.5.1.7.1Test Purpose and Environment6303

A.17.5.1.7.2Test Requirements6305

A.17.5.1.8Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode6305

A.17.5.1.8.1Test Purpose and Environment6305

A.17.5.1.8.2Test Requirements6308

A.17.5.1.9UE Radio Link Monitoring Scheduling Restrictions on FR26309

A.17.5.1.9.1Test Purpose and Environment6309

A.17.5.1.9.2Test Requirements6310

A.17.5.2Beam Failure Detection and Link recovery procedures6311

A.17.5.2.1Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode6311

A.17.5.2.1.1Test Purpose and Environment6311

A.17.5.2.1.2Test Requirements6313

A.17.5.2.2Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode6314

A.17.5.2.2.1Test Purpose and Environment6314

A.17.5.2.2.2Test Requirements6317

A.17.5.2.3Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode6317

A.17.5.2.3.1Test Purpose and Environment6317

A.17.5.2.3.2Test Requirements6320

A.17.5.2.4Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode6320

A.17.5.2.4.1Test Purpose and Environment6320

A.17.5.2.4.2Test Requirements6323

A.17.5.2.5Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode for 2 Rx UE6323

A.17.5.2.5.1Test Purpose and Environment6323

A.17.5.2.5.2Test Requirements6326

A.17.5.3Active BWP switch for RedCap6327

A.17.5.3.1DCI-based and Timer-based Active BWP Switch6327

A.17.5.3.1.1NR FR2 DL active BWP switch with non-DRX in SA6327

A.17.5.3.1.1.1Test Purpose and Environment6327

A.17.5.3.1.1.2Test Requirements6329

A.17.5.3.2RRC-based Active BWP Switch6329

A.17.5.3.2.1NR FR2 DL active BWP switch of PCell with non-DRX in SA6329

A.17.5.3.2.1.1Test Purpose and Environment6329

A.17.5.3.2.1.2Test Requirements6332

A.17.5.4Active TCI state switch delay6332

A.17.5.4.1MAC-CE based active TCI state switch6332

A.17.5.4.1.1NR PCell FR2 active TCI state switch for a known TCI state6332

A.17.5.4.1.1.1Test Purpose and Environment6332

A.17.5.4.1.1.2Test Requirements6335

A.17.5.4.2RRC based active TCI state switch6335

A.17.5.4.2.1NR PCell FR2 active TCI state switch for a known TCI state6335

A.17.5.4.2.1.1Test Purpose and Environment6335

A.17.5.4.2.1.2Test Requirements6338

A.17.5.5Uplink spatial relation switch delay6338

A.17.5.5.1MAC-CE based Spatial Relation switch6338

A.17.5.5.1.1 NR PCell FR2 spatial relation associated with known DL-RS6338

A.17.5.5.1.1.1Test Purpose and Environment6338

A.17.5.5.1.1.2Test Requirements6340

A.17.5.5.2RRC based spatial relation switch6341

A.17.5.5.2.1NR PCell FR2 spatial relation switch associated with a known DL-RS6341

A.17.5.5.2.1.2Test Requirements6343

A.17.5.6UE specific CBW change6343

A.17.5.6.1NR FR2 UE specific CBW change of PCell with non-DRX in SA6343

A.17.5.6.1.1Test Purpose and Environment6343

A.17.5.6.1.2Test Requirements6345

A.17.6Measurement procedure for RedCap6346

A.17.6.1Intra-frequency Measurements6346

A.17.6.1.1SA event triggered reporting test without gap under non-DRX6346

A.17.6.1.1.1Test purpose and Environment6346

A.17.6.1.1.2Test Requirements6348

A.17.6.1.2SA event triggered reporting test without gap under DRX6348

A.17.6.1.2.1Test purpose and Environment6348

A.7.6.1.2.2Test Requirements6349

A.17.6.1.3SA event triggered reporting test with per-UE gaps under non-DRX6349

A.17.6.1.3.1Test purpose and Environment6349

A.17.6.1.3.2Test Requirements6352

A.17.6.1.4SA event triggered reporting test with per-UE gaps under DRX6352

A.17.6.1.4.1Test purpose and Environment6352

A.17.6.1.4.2Test Requirements6354

A.17.6.2Inter-frequency Measurements6355

A.17.6.2.1SA event triggered reporting tests For FR2 without SSB time index detection when DRX is not used (PCell in FR2)6355

A.17.6.2.1.1Test Purpose and Environment6355

A.17.6.2.1.2Test Requirements6357

A.17.6.2.2SA event triggered reporting tests For FR2 without SSB time index detection when DRX is used (PCell in FR2)6357

A.17.6.2.2.1Test Purpose and Environment6357

A.17.6.2.2.2Test Requirements6359

A.17.6.2.3SA event triggered reporting tests For FR2 with SSB time index detection when DRX is not used (PCell in FR2)6360

A.17.6.2.3.1Test Purpose and Environment6360

A.17.6.2.3.2Test Requirements6362

A.17.6.2.4SA event triggered reporting tests For FR2 with SSB time index detection when DRX is used (PCell in FR2) for 2 RX UE6362

A.17.6.2.4.1Test Purpose and Environment6362

A.17.6.2.4.2Test Requirements6364

A.17.6.3L1-RSRP measurement for beam reporting6365

A.17.6.3.1SSB based L1-RSRP measurement when DRX is not used6365

A.17.6.3.1.1Test Purpose and Environment6365

A.17.6.3.1.2Test parameters6365

A.17.6.3.1.3Test Requirements6365

A.17.6.3.2SSB based L1-RSRP measurement when DRX is used6365

A.17.6.3.2.1Test Purpose and Environment6365

A.17.6.3.2.2Test parameters6366

A.17.6.3.2.3Test Requirements6367

A.17.6.3.3CSI-RS based L1-RSRP measurement when DRX is not used6367

A.17.6.3.3.1Test Purpose and Environment6367

A.17.6.3.3.2Test parameters6367

A.17.6.3.3.3Test Requirements6369

A.17.6.3.4CSI-RS based L1-RSRP measurement when DRX is used6369

A.17.6.3.4.1Test Purpose and Environment6369

A.17.6.3.4.2Test parameters6370

A.7.6.3.3.3Test Requirements6371

A.17.6.4.1SA interfrequency CGI reporting in autonomous gaps test (PCell in FR2) for 2 RX UE6371

A.17.6.4.1.1Test Purpose and Environment6371

A.17.6.4.1.2Test Requirements6374

A.17.6.5RSTD measurements6374

A.17.6.5.1NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA6374

A.17.6.5.1.1Test Purpose and Environment6374

A.17.6.5.1.2Test Requirements6381

A.17.6.5.2NR RSTD measurement reporting delay test case with PRS frequency hopping6381

A.17.6.5.2.1Test Purpose and Environment6381

A.17.6.5.2.2Test Requirements6386

A.17.6.6UE Rx-Tx Measurements6387

A.17.6.6.1UE Rx-Tx measurement reporting delay for single positioning frequency layer in FR2 SA without RX FH in RRC_CONNECTED mode6387

A.17.6.6.1.1Test purpose and environment6387

A.17.6.6.1.2Test requirements6391

A.17.6.6.2UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR2 SA in RRC_CONNECTED state6391

A.17.6.6.2.1Test purpose and environment6391

A.17.6.6.2.2Test requirements6395

A.17.6.7PRS-RSRP measurements6395

A.17.6.7.1PRS-RSRP measurement delay test case for RedCap positioning without Rx FH in RRC_CONNECTED state in FR26395

A.17.6.7.1.1PRS-RSRP measurement delay test case for single positioning frequency layer6395

A.17.6.7.1.1.1Test Purpose and Environment6395

A.17.6.7.1.1.2Test Requirements6399

A.17.6.7.1.2PRS-RSRP measurement delay test case for dual positioning frequency layer6399

A.17.6.7.1.2.1Test Purpose and Environment6399

A.17.6.7.1.2.2Test Requirements6403

A.17.6.7.2PRS-RSRP measurement delay with FH in RRC_CONNECTED state in FR26403

A.17.6.7.2.1Test Purpose and Environment6403

A.17.6.7.2.2Test Requirements6407

A.17.6.8PRS-RSRPP Measurements6407

A.17.6.8.1PRS-RSRPP measurement delay without FH in RRC_CONNECTED state in FR26407

A.17.6.8.1.1Test Purpose and Environment6407

A.17.6.8.1.2Test Requirements6410

A.17.6.8.2PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR2 SA in RRC_CONNECTED state6410

A.17.6.8.2.1Test Purpose and Environment6410

A.17.6.8.2.2Test Requirements6412

A.17.7Measurement Performance requirements6413

A.17.7.1SS-RSRP6413

A.17.7.1.1SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell6413

A.17.7.1.1.1Test Purpose and Environment6413

A.17.7.1.1.2Test parameters6413

A.17.7.1.1.3Test Requirements6415

A.17.7.1.2SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell6415

A.17.7.1.2.1Test Purpose and Environment6415

A.17.7.1.2.2Test parameters6415

A.17.7.1.2.3Test Requirements6417

A.17.7.2SS-RSRQ6418

A.17.7.2.1SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell6418

A.17.7.2.1.1Test Purpose and Environment6418

A.17.7.2.1.2Test Parameters6418

A.17.7.2.1.3Test Requirements6420

A.17.7.2.2SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell for 2 Rx UE6420

A.17.7.2.2.1Test Purpose and Environment6420

A.17.7.2.2.2Test parameters6420

A.17.7.2.2.3Test Requirements6422

A.17.7.2.3SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell6422

A.17.7.3L1-RSRP measurement for beam reporting6422

A.17.7.3.1SSB based L1-RSRP measurement6422

A.17.7.3.1.1Test Purpose and Environment6422

A.17.7.3.1.2Test parameters6422

A.17.7.3.1.3Test Requirements6423

A.17.7.3.2CSI-RS based L1-RSRP measurement on resource set with repetition off6423

A.17.7.3.2.1Test Purpose and Environment6423

A.17.7.3.2.2Test parameters6423

A.17.7.3.2.3Test Requirements6423

A.17.7.4SS-SINR6424

A.17.7.4SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell for 2Rx UE6424

A.17.7.4.1.1Test Purpose and Environment6424

A.17.7.4.1.2Test parameters6424

A.17.7.4.1.3Test Requirements6426

A.17.7.5RSTD measurements6426

A.17.7.5.1RSTD measurement accuracy test case for RedCap UE without FH6426

A.17.7.5.1.1Test purpose and Environment6426

A.17.7.5.1.2Test Requirements6428

A.17.7.6UE Rx-Tx Measurements6430

A.17.7.6.1UE Rx-Tx measurement accuracy for single positioning frequency layer in FR2 SA without RX FH in RRC_CONNECTED mode6430

A.17.7.6.1.1Test purpose and environment6430

A.17.7.6.1.2Test parameters6431

A.17.7.6.1.3Test requirements6434

A.17.7.6.2SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_CONNECTED state in FR26434

A.17.7.6.2.1Test purpose and Environment6434

A.17.7.6.2.2Test parameters6435

A.17.7.6.2.3Test requirements6437

A.17.7.7PRS-RSRP Measurements6437

A.17.7.7.1PRS-RSRP measurement accuracy without FH in RRC_CONNECTED state in FR26437

A.17.7.7.1.1Test Purpose and Environment6437

A.17.7.7.1.2Test parameters6437

A.17.7.7.1.3Test Requirements6439

A.17.7.7.2PRS-RSRP measurement accuracy with FH in RRC_CONNECTED state in FR26439

A.17.7.7.2.1Test Purpose and Environment6439

A.17.7.7.2.2Test parameters6440

A.17.7.7.2.3Test Requirements6442

A.17.7.8PRS-RSRPP Measurements6442

A.17.7.8.1PRS-RSRPP measurement accuracy without FH in RRC_CONNECTED state in FR26442

A.17.7.8.1.1Test Purpose and Environment6442

A.17.7.8.1.2Test parameters6443

A.17.7.8.1.3Test Requirements6445

A.17.7.8.2SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_CONNECTED state in FR26445

A.17.7.8.2.1Test purpose and Environment6445

A.17.7.8.2.2Test parameters6446

A.17.7.8.2.3Test requirements6448

A.17.8Measurement Procedure for RedCap in RRC_INACTIVE6449

A.17.8.1RSTD Measurements6449

A.17.8.1.1NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA in RRC_INACTIVE state6449

A.17.8.1.1.1Test Purpose and Environment6449

A.17.8.1.1.2Test Requirements6452

A.17.8.1.2NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state6452

A.17.8.1.2.1Test Purpose and Environment6452

A.17.8.1.2.2Test Requirements6455

A.17.8.1.3NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state with eDRX > 10.24s6455

A.17.8.1.3.1Test purpose and environment6455

A.17.8.1.3.2Test requirements6455

A.17.8.2UE Rx-Tx Measurements6456

A.17.8.2.1UE Rx-Tx measurement reporting delay for single positioning frequency layer in FR2 SA without RX FH in RRC_INACTIVE mode6456

A.17.8.2.1.1Test purpose and environment6456

A.17.8.2.1.2Test requirements6459

A.17.8.2.2UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR2 SA in RRC_INACTIVE state6459

A.17.8.2.2.1Test purpose and environment6459

A.17.8.2.2.2Test requirements6463

A.17.8.2.3UE Rx-Tx time difference measurements for single positioning frequency layer with eDRX > 10.24s in FR2 SA6463

A.17.8.2.3.1Test purpose and environment6463

A.17.8.2.3.2Test requirements6463

A.17.8.3PRS-RSRP Measurements6464

A.17.8.3.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_INACTIVE6464

A.17.8.3.1.1Test Purpose and Environment6464

A.17.8.3.1.2Test Requirements6468

A.17.8.3.2.2Test Requirements6472

A.17.8.3.3PRS-RSRP reporting delay in RRC_INACTIVE with eDRX6472

A.17.8.3.3.1Test Purpose and Environment6472

A.17.8.3.3.2Test Requirements6476

A.17.8.4PRS-RSRPP Measurements6476

A.17.8.4.1PRS-RSRPP measurement delay without FH in RRC_INACTIVE state in FR26476

A.17.8.4.1.1Test Purpose and Environment6476

A.17.8.4.2PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state6479

A.17.8.4.2.1Test Purpose and Environment6479

A.17.8.4.2.2Test Requirements6481

A.17.8.4.3PRS-RSPP reporting delay in RRC_INACTIVE state with eDRX > 10.24s6481

A.17.8.4.3.1Test purpose and environment6481

A.17.8.4.3.2Test requirements6481

A.17.9Measurement Performance Requirements for RedCap in RRC_INACTIVE6482

A.17.9.1RSTD Measurements6482

A.17.9.1.1RSTD measurement accuracy test case for RedCap UE without FH in FR2 in RRC_INACTIVE state6482

A.17.9.1.1.1Test purpose and Environment6482

A.17.9.1.1.2Test Requirements6484

A.17.9.1.2RSTD measurement accuracy test case for RedCap UE with FH in FR2 in RRC_INACTIVE state6484

A.17.9.1.2.1Test purpose and Environment6484

A.17.9.1.2.2Test Requirements6486

A.17.9.2UE Rx-Tx Measurements6486

A.17.9.2.1UE Rx-Tx measurement accuracy for single positioning frequency layer in FR2 SA without RX FH in RRC_INACTIVE mode6486

A.17.9.2.1.1Test purpose and environment6486

A.17.9.2.1.2Test parameters6487

A.17.9.2.1.3Test requirements6490

A.17.9.2.2SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_INACTIVE state in FR26490

A.17.9.2.2.1Test purpose and Environment6490

A.17.9.2.2.2Test parameters6490

A.17.9.2.2.3Test requirements6491

A.17.9.3PRS-RSRP Measurements6492

A.17.9.3.2PRS-RSRP measurement accuracy with FH in RRC_INACTIVE state in FR26494

A.17.9.3.2.1Test Purpose and Environment6494

A.17.9.3.2.2Test parameters6495

A.17.9.3.2.3Test Requirements6496

A.17.9.4PRS-RSRPP Measurements6496

A.17.9.4.1SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_INACTIVE state in FR26496

A.17.9.4.1.1Test Purpose and Environment6496

A.17.9.4.1.2Test parameters6497

A.17.9.4.1.3Test Requirements6499

A.17.9.4.2SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_INACTIVE state in FR26499

A.17.9.4.2.1Test Purpose and Environment6499

A.17.9.4.2.2Test parameters6500

A.17.9.4.2.3Test Requirements6502

A.17.10Measurement Procedure for RedCap in RRC_IDLE6503

A.17.10.1RSTD Measurements6503

A.17.10.1.1NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA in RRC_IDLE state without eDRX6503

A.17.10.1.1.1Test Purpose and Environment6503

A.17.10.1.1.2Test Requirements6506

A.17.10.1.2NR RSTD without FH measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s6506

A.17.10.1.2.1Test purpose and environment6506

A.17.10.1.2.2Test requirements6506

A.17.10.2PRS-RSRP Measurements6507

A.17.10.2.1PRS-RSRP measurement delay test case for single positioning frequency layer in RRC_IDLE6507

A.17.10.2.1.1Test Purpose and Environment6507

A.17.10.2.1.2Test Requirements6511

A.17.10.2.2PRS-RSRP reporting delay test case in RRC_IDLE state in FR2 when eDRX cycle > 10.24s6511

A.17.10.2.2.1Test Purpose and Environment6511

A.17.10.2.2.2Test Requirements6511

A.17.11 Measurement Performance Requirements for RedCap in RRC_IDLE6512

A.17.11.1RSTD Measurements6512

A.17.11.1.1RSTD measurement accuracy test case for RedCap UE without FH in FR2 in RRC_IDLE state without eDRX6512

A.17.11.1.1.1Test purpose and Environment6512

11.1.1.2Test Requirements6514

A.17.11.1.2RSTD without FH measurement accuracy test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s6514

A.17.11.1.2.1Test purpose and environment6514

A.17.11.1.2.2Test requirements6516

A.17.11.2PRS-RSRP Measurements6516

A.17.11.2.1PRS-RSRP measurement accuracy test case for RedCap UE in FR2 in RRC_IDLE state6516

A.17.11.2.1.1Test Purpose and Environment6516

A.17.11.2.1.2Test parameters6516

A.17.11.2.2PRS-RSRP measurement accuracy test case in RRC_IDLE state in FR2 when eDRX cycle > 10.24s6518

A.17.11.2.2.1Test purpose and Environment6518

A.17.11.2.2.1Test parameters6519

A.17.11.2.2.2Test Requirements6519

A.18E-UTRA standalone tests for NR RRM for RedCap6519

A.18.1RRC_IDLE state mobility6519

A.18.1.1Inter-RAT NR Cell re-selection6519

A.18.1.1.1E-UTRA Cell reselection to higher priority NR target Cell in FR16519

A.18.1.1.1.1Test Purpose and Environment6519

A.18.1.1.1.2Test Requirements6522

A.18.2RRC_CONNECTED state mobility6522

A.18.2.1Handover6522

A.18.2.1.1E-UTRAN - NR handover in FR16522

A.18.2.1.1.1Test Purpose and Environment6522

A.18.2.1.1.2Test Requirements6526

A.18.2.2RRC connection release with redirection6526

A.18.2.2.1Redirection from E-UTRA to NR FR1 for redcap UE6526

A.18.2.2.1.1Test Purpose and Environment6526

A.18.2.2.1.2Test Parameters6526

A.18.2.2.1.3Test Requirements6529

A.18.3Measurement procedure6530

A.18.3.1E-UTRA – NR Inter-RAT Measurements6530

A.18.3.1.1NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used6530

A.18.3.1.1.1Test Purpose and Environment6530

A.18.3.1.1.2Test Requirements6533

A.18.3.1.2NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used6533

A.18.3.1.2.1Test Purpose and Environment6533

A.18.3.1.2.2Test Requirements6537

A.18.3.1.3NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used6537

A.18.3.1.3.1Test Purpose and Environment6537

A.18.3.1.3.2Test Requirements6541

A.18.3.1.4NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used6541

A.18.3.1.4.1Test Purpose and Environment6541

A.18.3.1.4.2Test Requirements6545

A.18.3.1.5NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is not used6545

A.18.3.1.5.1Test Purpose and Environment6545

A.18.3.1.5.2Test Requirements6547

A.18.3.1.6NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is used6547

A.18.3.1.6.1Test Purpose and Environment6547

A.18.3.1.6.2Test Requirements6549

A.18.3.1.7NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is not used6550

A.18.3.1.7.1Test Purpose and Environment6550

A.18.3.1.7.2Test Requirements6551

A.18.3.1.8NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is used6552

A.18.3.1.8.1Test Purpose and Environment6552

A.18.3.1.8.2Test Requirements6554

A.19NR standalone tests for ATG6555

A.19.1RRC_IDLE state mobility6555

A.19.1.1Cell reselection to FR1 intra-frequency NR case6555

A.19.1.1.1Test Purpose and Environment6555

A.19.1.1.2Test Parameters6555

A.19.1.1.3Test Requirements6556

A.19.1.2Cell reselection to FR1 inter-frequency NR case6556

A.19.1.2.1Test Purpose and Environment6556

A.19.1.2.2Test Parameters6556

A.19.1.2.3Test Requirements6558

A.19.1.3Cell reselection to FR1 inter-frequency NR case for UE configured with hs-ATG-cellReselectionSet-r186559

A.19.1.3.1Test Purpose and Environment6559

A.19.1.3.2Test Parameters6559

A.19.1.3.3Test Requirements6561

A.19.2RRC_CONNECTED state mobility6561

A.19.2.1Handover6561

A.19.2.1.1Intra-frequency handover from FR1 to FR1; known target cell6561

A19.2.1.1.1Test Purpose and Environment6561

A.19.2.1.1.2Test Parameters6561

A.19.2.1.2.3Test Requirements6562

A.19.2.1.2Inter-frequency handover from FR1 to FR1; unknown target cell6562

A.19.2.1.2.1Test Purpose and Environment6562

A.19.2.1.2.2Test Parameters6562

A.19.2.1.2.3Test Requirements6563

A.19.2.2Conditional Handover6563

A.19.2.2.1Intra-frequency distance-based conditional Handover from FR1 to FR16563

A.19.2.2.1.1Test Purpose and Environment6563

A.19.2.2.1.2Test Parameters6564

A.19.2.2.1.3Test Requirements6566

A.19.2.2.2Inter-frequency distance-based conditional Handover from FR1 to FR16566

A.19.2.2.2.1Test Purpose and Environment6566

A.19.2.2.2.2Test Parameters6566

A.19.2.2.2.3Test Requirements6568

A.19.2.3RRC Connection Mobility Control6569

A.19.2.3.1SA: RRC Re-establishment6569

A.19.2.3.1.1Intra-frequency RRC Re-establishment in FR1 for ATG6569

A.19.2.3.1.1.1Test Purpose and Environment6569

A.19.2.3.1.1.2 Test Requirements6570

A.19.2.3.1.2Inter-frequency RRC Re-establishment in FR1 with unknown target cell without serving cell timing for ATG6570

A.19.2.3.1.2.1Test Purpose and Environment6570

A.19.2.3.1.2.2Test Requirements6572

A.19.2.3.2Random Access for ATG UE6573

A.19.2.3.2.1.1Test Purpose and Environment6573

A.19.2.3.2.1.2Test Requirements6573

A.19.2.3.2.2.1Test Purpose and Environment6573

A.19.2.3.2.2.2Test Requirements6574

A.19.2.3.2.32-step RA type contention based random access test in FR1 for NR standalone6574

A.19.2.3.2.3.1Test Purpose and Environment6574

A.19.2.3.2.3.2Test Requirements6575

A.19.2.3.2.42-step RA type non-contention based test in FR1 for NR standalone6575

A.19.2.3.2.4.1Test Purpose and Environment6575

A.19.2.3.2.4.2Test Requirements6575

A.19.2.3.3.1.1Test Purpose and Environment6575

A.19.2.3.3.1.2Test Parameters6575

A.19.2.3.3.1.3Test Requirements6576

A.19.3Timing6577

A.19.3.1UE transmit timing6577

A.19.3.1.1ATG UE Transmit Timing Test for FR16577

A.19.3.1.1.1Test Purpose and environment6577

A.19.3.1.1.2Test requirements6578

A.19.3.2UE timer accuracy6579

A.19.3.3Timing advance6579

A.19.3.3.1SA FR1 timing advance adjustment accuracy6579

A.19.3.3.1.1Test Purpose and Environment6579

A.19.3.3.1.2Test Parameters6579

A.19.3.3.1.3Test Requirements6580

A.19.4Signalling characteristics6580

A.19.4.1Radio link Monitoring6580

A.19.4.1.1Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode6580

A.19.4.1.1.1Test Purpose and Environment6580

A.19.4.1.1.2Test Requirements6583

A.19.4.1.2Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode6583

A.19.4.1.2.1Test Purpose and Environment6583

A.19.4.1.2.2Test Requirements6586

A.19.4.1.3Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode6586

A.19.4.1.3.1Test Purpose and Environment6586

A.19.4.1.3.2Test Requirements6589

A.19.4.1.4Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode6590

A.19.4.1.4.1Test Purpose and Environment6590

A.19.4.1.4.2Test Requirements6593

A.19.4.2Beam Failure Detection and Link recovery procedures6593

A.19.4.2.1Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode6593

A.19.4.2.1.1Test Purpose and Environment6593

A.19.4.2.1.2Test Requirements6597

A.19.4.2.2Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode6597

A.19.4.2.2.1Test Purpose and Environment6597

A.19.4.2.2.2Test Requirements6601

A.19.4.2.3Beam Failure Detection and Link Recovery Test for FR1 SCell configured with with CSI-RS-based BFD and SSB-based LR in non-DRX mode6601

A.19.4.2.3.1Test Purpose and Environment6601

A.19.4.2.3.2Test Requirements6602

A.19.4.3Active BWP switch6602

A.19.4.3.1DCI-based and Timer-based Active BWP Switch6602

A.19.4.3.1.1NR FR1 DL active BWP switch with non-DRX in SA6602

A.19.4.3.2RRC-based Active BWP Switch6605

A.19.4.3.2.1NR FR1 DL active BWP switch of Cell with non-DRX in SA6605

A.19.4.4UE specific CBW change6607

A19.4.4.1UE specific CBW change on PCell in FR1 in non-DRX6607

A19.4.4.1.1Test Purpose and Environment6608

A.19.4.4.1.2Test Requirements6610

A.19.4.5Pathloss reference signal switching delay6610

A.19.4.5.1MAC-CE based pathloss reference signal switch delay6610

A.19.4.5.1.1Test Purpose and Environment6610

A.19.4.5.1.2Test Requirements6612

A.19.4.6Interruption6613

A.19.4.6.1SA interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in NR-CA6613

A.19.4.6.1.1Test Purpose and Environment6613

A.19.4.6.1.2Test Parameters6613

A.19.4.6.1.3Test Requirements6615

A.19.4.6.2SA interruptions at NR SRS antenna port switching with more than 1 SRS symbol in a slot in NR-CA6615

A.19.4.6.2.1Test Purpose and Environment6615

A.19.4.6.2.2Test Parameters6615

A.19.4.6.2.3Test Requirements6617

A.19.4.7SCell Activation and Deactivation Delay for ATG6618

A.19.4.7.1SCell Activation and deactivation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle6618

A.19.4.7.1.1Test Purpose and Environment6618

A.19.4.7.1.2Test Requirements6622

A.19.4.7.2SCell Activation and deactivation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle6623

A.19.4.7.2.1Test Purpose and Environment6623

A.19.4.7.2.2Test Requirements6623

A.19.4.7.3SCell Activation and deactivation of unknown SCell in FR1 in non-DRX6623

A.19.4.7.3.1Test Purpose and Environment6623

A.19.4.7.3.2Test Requirements6624

A.19.4.7.4Direct SCell activation at SCell addition of known SCell in FR16624

A.19.4.7.4.1Test Purpose and Environment6624

A.19.4.7.4.2Test Requirements6628

A.19.4.7.5Direct SCell activation at handover with known SCell in FR16628

A.19.4.7.5.1Test Purpose and Environment6628

A.19.4.7.5.2Test Requirements6632

A.19.4.7.6Fast SCell Activation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle6633

A.19.4.7.6.1Test Purpose and Environment6633

A.19.4.7.6.2Test Requirements6634

A.19.4.7.7Fast SCell Activation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle6634

A.19.4.7.7.1Test Purpose and Environment6634

A.19.4.7.7.2Test Requirements6635

A.19.4.7.8SCell Activation of unknown SCell with valid L3 measurement results in FR1 in non-DRX for 160 ms SCell measurement cycle6635

A.19.4.7.8.1Test Purpose and Environment6635

A.19.4.7.8.2Test Requirements6640

A.19.4.7.9TRS based SCell Activation of SSB-less SCell in FR1 inter-band CA in non-DRX for ATG6640

A.19.4.7.9.1Test Purpose and Environment6640

A.19.4.7.9.2Test Requirements6642

A.19.5Measurement procedure6642

A.19.5.1Intra-frequency Measurements6642

A.19.5.1.1SA event triggered reporting tests without gap without SSB index reading under non-DRX6642

A.19.5.1.1.1Test purpose and Environment6642

A.19.5.1.1.2Test parameters6642

A.19.5.1.1.3Test Requirements6643

A.19.5.1.2SA event triggered reporting tests with per-UE gaps under non-DRX6643

A.19.5.1.2.1Test purpose and Environment6643

A.19.5.1.2.2Test parameters6643

A.19.5.1.2.3Test Requirements6643

A.19.5.1.3SA event triggered reporting tests without gap under non-DRX with SSB index reading6644

A.19.5.1.3.1Test purpose and Environment6644

A.19.5.1.3.2Test parameters6644

A.19.5.1.3.3Test Requirements6644

A.19.5.1.4SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading6644

A.19.5.1.4.1Test purpose and Environment6644

A.19.5.1.4.2Test parameters6645

A.19.5.1.4.3Test Requirements6645

A.19.5.1.5Event triggered reporting tests on SCC with deactivated SCell under non-DRX with measurement cycle of 640ms6645

A.19.5.1.5.1Test purpose and Environment6645

A.19.5.1.5.2Test parameters6645

A.19.5.1.5.3Test Requirements6648

A.19.5.2Inter-frequency Measurements6648

A.19.5.2.1.2Test parameters6648

A.19.5.2.1.3Test Requirements6650

A.19.5.2.2.2Test parameters6650

A.19.5.2.3.2Test parameters6651

A.19.5.2.3.3Test Requirements6651

A.19.5.3L1-RSRP measurement for beam reporting for ATG6651

A.19.5.3.1SSB based L1-RSRP measurement when DRX is not used6651

A.19.5.3.1.1Test Purpose and Environment6651

A.19.5.3.1.2Test parameters6652

A.19.5.3.1.3Test Requirements6652

A.19.5.3.2CSI-RS based L1-RSRP measurement when DRX is not used6652

A.19.5.3.2.1Test Purpose and Environment6652

A.19.5.3.2.2Test parameters6652

A.19.5.3.2.3Test Requirements6653

A.19.5.4L1-SINR measurement for beam reporting for ATG6653

A.19.5.4.1L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is not used6653

A.19.5.4.1.3Test Requirements6653

A.19.5.4.2L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used6653

A.19.5.4.2.1Test Purpose and Environment6653

A.19.5.4.2.2Test parameters6654

A.19.5.4.2.3Test Requirements6654

A.19.5.4.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used6654

A.19.5.4.3.1Test Purpose and Environment6654

A.19.5.4.3.2Test parameters6654

A.19.5.4.3.3Test Requirements6655

A.19.5.5NR measurements with autonomous gaps for ATG6655

A.19.5.5.1SA intra-frequency CGI identification of NR neighbor cell in FR16655

A.19.5.5.1.1Test Purpose and Environment6655

A.19.5.5.1.2Test Parameters6655

A.19.5.5.1.3Test Requirements6656

A.19.6Measurement Performance requirements6656

A.19.6.1SS-RSRP for ATG UE6656

A.19.6.1.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell6656

A.19.6.1.1.1Test Purpose and Environment6656

A.19.6.1.1.2Test parameters6656

A.19.6.1.1.3Test Requirements6657

A.19.6.1.2SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell6657

A.19.6.1.2.1Test Purpose and Environment6657

A.19.6.1.2.2Test parameters6657

A.19.6.1.2.3Test Requirements6657

A.19.6.2SS-RSRQ for ATG UE6657

A.19.6.2.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell6658

A.19.6.2.1.1Test Purpose and Environment6658

A.19.6.2.1.2Test Parameters6658

A.19.6.2.1.3Test Requirements6658

A.19.6.2.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell6658

A.19.6.2.2.1Test Purpose and Environment6658

A.19.6.2.2.2Test Parameters6658

A.19.6.2.2.3Test Requirements6659

A.19.6.3SS-SINR for ATG UE6659

A.19.6.3.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell6659

A.19.6.3.1.1Test Purpose and Environment6659

A.19.6.3.1.2Test Parameters6659

A.19.6.3.1.3Test Requirements6660

A.19.6.3.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell6660

A.19.6.3.2.1Test Purpose and Environment6660

A.19.6.3.2.2Test Parameters6660

A.19.6.3.2.3Test Requirements6660

A.19.6.4L1-RSRP measurement for beam reporting for ATG UE6660

A.19.6.4.1SSB based L1-RSRP measurement6660

A.19.6.4.1.1Test Purpose and Environment6660

A.19.6.4.1.2Test parameters6661

A.19.6.4.1.3Test Requirements6661

A.19.6.4.2CSI-RS based L1-RSRP measurement on resource set with repetition off6661

A.19.6.4.2.1Test Purpose and Environment6661

A.19.6.4.2.2Test parameters6661

A.19.6.4.2.3Test Requirements6662

A.19.6.5L1-SINR measurement for beam reporting based CMR for ATG UE6662

A.19.6.5.1L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured and CSI-RS resource set with repetition off6662

A.19.6.5.1.1Test Purpose and Environment6662

A.19.6.5.1.2Test parameters6662

A.19.6.5.1.3Test Requirements6662

A.19.6.5.2L1-SINR measurement with SSB based CMR and dedicated IMR6662

A.19.6.5.2.1Test Purpose and Environment6663

A.19.6.5.2.2Test parameters6663

A.19.6.5.2.3Test Requirements6663

A.19.6.5.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR6663

A.19.6.5.3.1Test Purpose and Environment6663

A.19.6.5.3.2Test parameters6664

A.19.6.5.3.3Test Requirements6664

A.19.6.6CSI-RSRP for ATG UE6664

A.19.6.6.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell6664

A.19.6.6.1.1Test Purpose and Environment6664

A.19.6.6.1.2Test parameters6664

A.19.6.6.1.3Test Requirements6665

A.19.6.6.2SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell6665

A.19.6.6.2.1Test Purpose and Environment6665

A.19.6.6.2.2Test parameters6665

A.19.6.6.2.3Test Requirements6665

A.19.6.7CSI-RSRQ for ATG UE6665

A.19.6.7.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell6665

A.19.6.7.1.1Test Purpose and Environment6665

A.19.6.7.1.2Test Parameters6666

A.19.6.7.1.3Test Requirements6666

A.19.6.7.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell6666

A.19.6.7.2.1Test Purpose and Environment6666

A.19.6.7.2.2Test Parameters6666

A.19.6.7.2.3Test Requirements6667

A.19.6.8CSI-SINR for ATG UE6667

A.19.6.8.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell6667

A.19.6.8.1.1Test Purpose and Environment6667

A.19.6.8.1.2Test Parameters6667

A.19.6.8.1.3Test Requirements6667

A.19.6.8.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell6668

A.19.6.8.2.1Test Purpose and Environment6668

A.19.6.8.2.2Test Parameters6668

A.19.6.8.2.3Test Requirements6668

A.20NR standalone tests for RedCap UE with Satellite Access6668

A.20.1RRC_IDLE state mobility6668

A.20.1.1Cell reselection to FR1 intra-frequency NR case for 1Rx RedCap UE6668

A.20.1.1.1Test Purpose and Environment6668

A.20.1.1.2Test Parameters6668

A.20.1.1.3Test Requirements6669

A.20.1.2Cell reselection to FR1 intra-frequency NR case  for 2Rx RedCap UE6669

A.20.1.2.1Test Purpose and Environment6669

A.20.1.2.2Test Parameters6669

A.20.1.2.3Test Requirements6669

A.20.1.3Cell reselection to FR1 intra-frequency NR cell for 1Rx RedCap UE configured with the feature for enhanced requirements6669

A.20.1.3.1Test Purpose and Environment6669

A.20.1.3.2Test Parameters6670

A.20.1.3.3Test Requirements6670

A.20.1.4Cell reselection to FR1 intra-frequency NR cell for 2Rx RedCap UE configured with the feature for enhanced requirements6670

A.20.1.4.1Test Purpose and Environment6670

A.20.1.4.2Test Parameters6670

A.20.1.4.3Test Requirements6670

A.20.1.5Time-based measurement initiation to FR1 intra-frequency NR cell reselection for 1Rx RedCap UE6670

A.20.1.5.1Test Purpose and Environment6670

A.20.1.5.2Test Parameters6670

A.20.1.5.3Test Requirements6671

A.20.1.6Time-based measurement initiation to FR1 intra-frequency NR cell reselection for 2Rx RedCap UE6671

A.20.1.6.1Test Purpose and Environment6671

A.20.1.6.2Test Parameters6671

A.20.1.6.3Test Requirements6671

A.20.1.7Location-based measurement initiation to FR1 inter-frequency NR cell reselection for 1Rx RedCap UE6671

A.20.1.7.1Test Purpose and Environment6671

A.20.1.7.2Test Parameters6671

A.20.1.7.3Test Requirements6672

A.20.1.8Location-based measurement initiation to FR1 inter-frequency NR cell reselection for 2Rx RedCap UE6672

A.20.1.8.1Test Purpose and Environment6672

A.20.1.8.2Test Parameters6672

A.20.1.8.3Test Requirements6672

A.20.1.9Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion for 1Rx RedCap UE6673

A.20.1.9.1Test Purpose and Environment6673

A.20.1.9.2Test Parameters6673

A.20.1.9.3Test Requirements6674

A.20.1.10Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion for 2Rx RedCap UE6674

A.20.1.10.1Test Purpose and Environment6674

A.20.1.10.2Test Parameters6675

A.20.1.10.3Test Requirements6675

A.20.1.11Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion for 1Rx RedCap UEs6675

A.20.1.11.1Test Purpose and Environment6675

A.20.1.11.2Test Parameters6675

A.20.1.11.3Test Requirements6677

A.20.1.12Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion for 2Rx RedCap UEs6677

A.20.1.12.1Test Purpose and Environment6677

A.20.1.12.2Test Parameters6677

A.20.1.12.3Test Requirements6678

A.20.1.13Cell reselection to FR1 inter-RAT for NR NTN carrier for 1Rx RedCap UE6678

A.20.1.13.1Test purpose and Environment6678

A.20.1.13.2Test Parameters6678

A.20.1.13.3Test requirements6680

A.20.1.14Cell reselection to FR1 inter-RAT for NR NTN carrier for 2Rx RedCap UE6680

A.20.1.14.1Test purpose and Environment6680

A.20.1.14.2Test Parameters6680

A.20.1.14.3Test requirements6681

A.20.1.15Cell re-selection to FR1 inter-frequency NR case with TN carrier for 1Rx RedCap UE6681

A.20.1.15.1Test purpose and Environment6681

A.20.1.15.2Test parameters6681

A.20.1.15.3Test requirements6683

A.20.1.16Cell re-selection to FR1 inter-frequency NR case with TN carrier for 2Rx RedCap UE6683

A.20.1.16.1Test purpose and Environment6683

A.20.1.16.2Test parameters6683

A.20.1.16.3Test requirements6683

A.20.2RRC_CONNECTED state mobility6683

A.20.2.1Handover6683

A.20.2.1.1Intra-frequency SAN Handover from FR1 to FR1 for 1Rx RedCap UE6683

A.20.2.1.1.1Test Purpose and Environment6683

A.20.2.1.1.2Test Parameters6684

A.20.2.1.1.3Test Requirements6684

A.20.2.1.2Intra-frequency SAN Handover from FR1 to FR1 for 2Rx RedCap UE6684

A.20.2.1.2.1Test Purpose and Environment6684

A.20.2.1.2.2Test Parameters6684

A.20.2.1.2.3Test Requirements6684

A.20.2.1.3Inter-frequency SAN Handover from FR1 to FR1 for 1Rx RedCap UE6684

A.20.2.1.3.1Test Purpose and Environment6684

A.20.2.1.3.2Test Parameters6685

A.20.2.1.3.3Test Requirements6685

A.20.2.1.4Inter-frequency SAN Handover from FR1 to FR1 for 2Rx RedCap UE6685

A.20.2.1.4.1Test Purpose and Environment6685

A.20.2.1.4.2Test Parameters6685

A.20.2.1.4.3Test Requirements6685

A.20.2.1.5Intra-frequency SAN RACH-less Handover from FR1 to FR1 for 1Rx RedCap UE6685

A.20.2.1.5.1Test Purpose and Environment6685

A.20.2.1.5.2Test Parameters6685

A.20.2.1.5.3Test Requirements6685

A.20.2.1.6Intra-frequency SAN RACH-less Handover from FR1 to FR1 for 2Rx RedCap UE6685

A.20.2.1.6.1Test Purpose and Environment6685

A.20.2.1.6.2Test Parameters6686

A.20.2.1.6.3Test Requirements6686

A.20.2.1.7Intra-frequency SAN time-based conditional Handover from FR1 to FR1 for 1Rx RedCap UE6686

A.20.2.1.7.1Test Purpose and Environment6686

A.20.2.1.7.2Test Parameters6686

A.20.2.1.7.3Test Requirements6686

A.20.2.1.8Intra-frequency SAN time-based conditional Handover from FR1 to FR1 for 2Rx RedCap UE6686

A.20.2.1.8.1Test Purpose and Environment6686

A.20.2.1.8.2Test Parameters6687

A.20.2.1.8.3Test Requirements6687

A.20.2.1.9Inter-frequency SAN distance-based conditional Handover from FR1 to FR1 for 1Rx RedCap UE6687

A.20.2.1.9.1Test Purpose and Environment6687

A.20.2.1.9.2Test Parameters6687

A.20.2.1.9.3Test Requirements6687

A.20.2.1.10Inter-frequency SAN distance-based conditional Handover from FR1 to FR1 for 2Rx RedCap UE6687

A.20.2.1.10.1Test Purpose and Environment6687

A.20.2.1.10.2Test Parameters6687

A.20.2.1.10.3Test Requirements6687

A.20.2.1.11Intra-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 1Rx RedCap UE6687

A.20.2.1.11.1Test Purpose and Environment6687

A.20.2.1.11.2Test Parameters6687

A.20.2.1.11.3Test Requirements6688

A.20.2.1.12Intra-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 2Rx RedCap UE6688

A.20.2.1.12.1Test Purpose and Environment6688

A.20.2.1.12.2Test Parameters6688

A.20.2.1.12.3Test Requirements6688

A.20.2.1.13Inter-frequency SAN distance-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 1Rx RedCap UE6688

A.20.2.1.13.1Test Purpose and Environment6688

A.20.2.1.13.2Test Parameters6688

A.20.2.1.13.3Test Requirements6689

A.20.2.1.14Inter-frequency SAN distance-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 2Rx RedCap UE6689

A.20.2.1.14.1Test Purpose and Environment6689

A.20.2.1.14.2Test Parameters6689

A.20.2.1.14.3Test Requirements6689

A.20.2.2RRC Connection Mobility Control6690

A.20.2.2.1SA: RRC Re-establishment for SAN6690

A.20.2.2.1.1Intra-frequency RRC Re-establishment in FR1 for 1 Rx RedCap UE6690

A.20.2.2.1.2Intra-frequency RRC Re-establishment in FR1 for 2 Rx RedCap UE6692

A.20.2.2.1.3Inter-frequency RRC Re-establishment in FR1 for 1 Rx RedCap UE6694

A.20.2.2.1.4Inter-frequency RRC Re-establishment in FR1 for 2 Rx RedCap UE6696

A.20.2.2.2Random Access6699

A.20.2.2.2.14-step RA type contention based random access test in FR1 for NR standalone for 1 Rx RedCap UE6699

A.20.2.2.2.24-step RA type contention based random access test in FR1 for NR standalone for 2 Rx RedCap UE6702

A.20.2.2.2.34-step RA type non-contention based random access test in FR1 for NR standalone for 1 Rx RedCap UE6705

A.20.2.2.2.44-step RA type non-contention based random access test in FR1 for NR standalone for 2 Rx RedCap UE6707

A.20.2.2.3RRC Connection Release with Redirection6710

A.20.2.2.3.1Redirection from NR in FR1 to NR in FR1 for 1 Rx RedCap UE6710

A.20.2.2.3.2Redirection from NR in FR1 to NR in FR1 for 2 Rx RedCap UE6713

A.20.2.3Satellite switching with re-synchronization from FR1 to FR1 for RedCap UE with Satellite Access6715

A.20.2.3.1RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 for RedCap UEs with 2Rx RedCap UE6715

A.20.2.3.1.1Test Purpose and Environment6715

A.20.2.3.1.2Test Parameters6715

A.20.2.3.1.3Test Requirements6717

A.20.2.3.2RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 for RedCap UEs with 1 Rx RedCap UE6717

A.20.2.3.2.1Test Purpose and Environment6717

A.20.2.3.2.2Test Parameters6717

A.20.2.3.2.3Test Requirements6719

A.20.2.3.3RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1 for 2Rx RedCap UEs6720

A.20.2.3.3.1Test Purpose and Environment6720

A.20.2.3.3.2Test Parameters6720

A.20.2.3.3.3Test Requirements6722

A.20.2.3.4RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1 for 1Rx RedCap UEs6722

A.20.2.3.4.1Test Purpose and Environment6722

A.20.2.3.4.2Test Parameters6722

A.20.2.3.4.3Test Requirements6722

A.20.3Timing for RedCap UE with Satellite Access6723

A.20.3.1UE transmit timing for RedCap UE with Satellite Access6723

A.20.3.1.1NR UE Transmit Timing Test for FR16723

A.20.3.1.1.1Test Purpose and environment6723

A.20.3.1.1.2Test requirements6724

A.20.3.2Timing advance for RedCap UE with Satellite Access6724

A.20.3.2.1SA FR1 timing advance adjustment accuracy for RedCap UE6724

A.20.3.2.1.1Test Purpose and Environment6724

A.20.3.2.1.2Test Parameters6724

A.20.3.2.1.3Test Requirements6726

A.20.4Signalling characteristics for RedCap UE with Satellite Access6726

A.20.4.1Radio link Monitoring6726

A.20.4.1.1Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode for 2Rx RedCap UE with NTN6726

A.20.4.1.1.1Test Purpose and Environment6726

A.20.4.1.1.2Test Requirements6726

A.20.4.1.2Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode for 1Rx RedCap UE with NTN6726

A.20.4.1.2.1Test Purpose and Environment6726

A.20.4.1.2.2Test Requirements6727

A.20.4.1.3Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode for 2Rx RedCap UE with NTN6728

A.20.4.1.3.1Test Purpose and Environment6728

A.20.4.1.3.2Test Requirements6728

A.20.4.1.4Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode for 1Rx RedCap UE with NTN6728

A.20.4.1.4.1Test Purpose and Environment6728

A.20.4.1.4.2Test Requirements6729

A.20.4.1.5Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode for 2Rx RedCap UE with NTN6729

A.20.4.1.5.1Test Purpose and Environment6729

A.20.4.1.5.2Test Requirements6729

A.20.4.1.6Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode for 1Rx RedCap UE with NTN6730

A.20.4.1.6.1Test Purpose and Environment6730

A.20.4.1.6.2Test Requirements6731

A.20.4.1.7Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode for 2Rx RedCap UE with NTN6731

A.20.4.1.7.1Test Purpose and Environment6731

A.20.4.1.7.2Test Requirements6731

A.20.4.1.8Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode for 1Rx RedCap UE with NTN6731

A.20.4.1.8.1Test Purpose and Environment6731

A.20.4.1.8.2Test Requirements6732

A.20.4.2Beam Failure Detection and Link recovery procedures for RedCap UE with satellite access6733

A.20.4.2.1Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode for 1Rx RedCap UE6733

A.20.4.2.1.1Test Purpose and Environment6733

A.20.4.2.1.2Test Requirements6733

A.20.4.2.2Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode for 2Rx RedCap UE6733

A.20.4.2.2.1Test Purpose and Environment6733

A.20.4.2.2.2Test Requirements6734

A.20.4.2.3Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode for 1Rx RedCap UE6734

A.20.4.2.3.1Test Purpose and Environment6734

A.20.4.2.3.2Test Requirements6734

A.20.4.2.4Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode for 2Rx RedCap UE6735

A.20.4.2.4.1Test Purpose and Environment6735

A.20.4.2.4.2Test Requirements6735

A.20.4.2.5Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode for 1Rx RedCap UE6735

A.20.4.2.5.1Test Purpose and Environment6735

A.20.4.2.5.2Test Requirements6736

A.20.4.2.6Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode for 2Rx RedCap UE6736

A.20.4.2.6.1Test Purpose and Environment6736

A.20.4.2.6.2Test Requirements6736

A.20.4.2.7Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode for 1Rx RedCap UE6736

A.20.4.2.7.1Test Purpose and Environment6736

A.20.4.2.7.2Test Requirements6737

A.20.4.2.8Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode for 2Rx RedCap UE6737

A.20.4.2.8.1Test Purpose and Environment6737

A.20.4.2.8.2Test Requirements6737

A.20.4.3Active BWP switch for RedCap UE with Satellite Access6737

A.20.4.3.1DCI-based and Timer-based Active BWP Switch6737

A.20.4.3.1.1NR FR1 DL active BWP switch with non-DRX in SA6737

A.20.4.3.2RRC-based Active BWP Switch6738

A.20.4.3.2.1NR FR1 DL active BWP switch of Cell with non-DRX in SA6738

A.20.4.3.2.1.2Test Requirements6738

A.20.4.4UE specific CBW change for RedCap UE with Satellite Access6738

A.20.4.4.1UE specific CBW change on PCell in FR1 in non-DRX6738

A.20.4.4.1.1Test Purpose and Environment6738

A.20.4.4.1.2Test Requirements6740

A.20.4.5Pathloss reference signal switching delay for RedCap UE with Satellite Access6740

A.20.4.5.1MAC-CE based pathloss reference signal switch delay6740

A.20.4.5.1.1Test Purpose and Environment6740

A.20.4.5.1.2Test Requirements6740

A.20.5Measurement procedure6741

A.20.5.1Intra-frequency Measurements6741

A.20.5.1.1SA event triggered reporting tests without gap under non-DRX for 1Rx RedCap UE6741

A.20.5.1.1.1Test purpose and Environment6741

A.20.5.1.1.2Test parameters6741

A.20.5.1.1.3Test Requirements6741

A.20.5.1.2SA event triggered reporting tests without gap under non-DRX for 2Rx RedCap UE6741

A.20.5.1.2.1Test purpose and Environment6741

A.20.5.1.2.2Test parameters6741

A.20.5.1.2.3Test Requirements6742

A.20.5.1.3SA event triggered reporting tests without gap under DRX for 1Rx RedCap UE6742

A.20.5.1.3.1Test purpose and Environment6742

A.20.5.1.3.2Test parameters6742

A.20.5.1.3.3Test Requirements6743

A.20.5.1.4SA event triggered reporting tests without gap under DRX for 2Rx RedCap UE6743

A.20.5.1.4.1Test purpose and Environment6743

A.20.5.1.4.2Test parameters6743

A.20.5.1.4.3Test Requirements6743

A.20.5.1.5SA event triggered reporting tests without gap under non-DRX with SSB index reading for 1Rx RedCap UE6744

A.20.5.1.5.1Test purpose and Environment6744

A.20.5.1.5.2Test parameters6744

A.20.5.1.5.3Test Requirements6744

A.20.5.1.6SA event triggered reporting tests without gap under non-DRX with SSB index reading for 2Rx RedCap UE6744

A.20.5.1.6.1Test purpose and Environment6744

A.20.5.1.6.2Test parameters6744

A.20.5.1.6.3Test Requirements6745

A.20.5.1.7SA event triggered reporting tests with single measurement gap under non-DRX for satellite access for 1Rx RedCap UE6745

A.20.5.1.7.1Test purpose and Environment6745

A.20.5.1.7.2Test parameters6745

A.20.5.1.7.3Test Requirements6746

A.20.5.1.8SA event triggered reporting tests with single measurement gap under non-DRX for satellite access for 2Rx RedCap UE6746

A.20.5.1.8.1Test purpose and Environment6746

A.20.5.1.8.2Test parameters6746

A.20.5.1.8.3Test Requirements6746

A.20.5.1.9SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access for 1Rx RedCap UE6746

A.20.5.1.9.1Test purpose and Environment6746

A.20.5.1.9.2Test parameters6746

A.20.5.1.9.3Test Requirements6747

A.20.5.1.10SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access for 2Rx RedCap UE6747

A.20.5.1.10.1Test purpose and Environment6747

A.20.5.1.10.2Test parameters6747

A.20.5.1.10.3Test Requirements6748

A.20.5.1.11SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access for 1Rx RedCap UE6748

A.20.5.1.11.1Test purpose and Environment6748

A.20.5.1.11.2Test parameters6748

A.20.5.1.11.3Test Requirements6748

A.20.5.1.12SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access for 2Rx RedCap UE6749

A.20.5.1.12.1Test purpose and Environment6749

A.20.5.1.12.2Test parameters6749

A.20.5.1.12.3Test Requirements6749

A.20.5.2Inter-frequency Measurements6749

A.20.5.2.1SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for 2Rx RedCap UE with satellite access6749

A.20.5.2.1.1Test Purpose and Environment6749

A.20.5.2.1.2Test Requirements6750

A.20.5.2.2SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for 1Rx RedCap UE with satellite access6750

A.20.5.2.2.1Test Purpose and Environment6750

A.20.5.2.2.2Test Requirements6750

A.20.5.2.3SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for 2Rx RedCap UE with satellite access6751

A.20.5.2.3.1Test Purpose and Environment6751

A.20.5.2.3.2Test Requirements6751

A.20.5.2.4SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for 1Rx RedCap UE with satellite access6751

A.20.5.2.4.1Test Purpose and Environment6751

A.20.5.2.4.2Test Requirements6752

A.20.5.2.5SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for 2Rx RedCap UE with satellite access6752

A.20.5.2.5.1Test Purpose and Environment6752

A.20.5.2.5.2Test Requirements6752

A.20.5.2.6SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for 1Rx RedCap UE with satellite access6752

A.20.5.2.6.1Test Purpose and Environment6752

A.20.5.2.6.2Test Requirements6753

A.20.5.2.7SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for 2Rx RedCap UE with satellite access6753

A.20.5.2.7.1Test Purpose and Environment6753

A.20.5.2.7.2Test Requirements6753

A.20.5.2.8SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for 1Rx RedCap UE with satellite access6754

A.20.5.2.8.1Test Purpose and Environment6754

A.20.5.2.8.2Test Requirements6754

A.20.5.2.9Event triggered reporting test without gap under non-DRX for 2Rx RedCap UE with satellite access6755

A.20.5.2.9.1Test purpose and Environment6755

A.20.5.2.9.2Test parameters6755

A.20.5.2.9.3Test Requirements6755

A.20.5.2.10Event triggered reporting test without gap under non-DRX for 1Rx RedCap UE with satellite access6755

A.20.5.2.10.1Test purpose and Environment6755

A.20.5.2.10.2Test parameters6755

A.20.5.2.10.3Test Requirements6755

A.20.5.2.11Event triggered reporting tests without gap under DRX for 2Rx RedCap UE with satellite access6755

A.20.5.2.11.1Test purpose and Environment6755

A.20.5.2.11.2Test parameters6755

A.20.5.2.11.3Test Requirements6756

A.20.5.2.12Event triggered reporting tests without gap under DRX for 1Rx RedCap UE with satellite access6756

A.20.5.2.12.1Test purpose and Environment6756

A.20.5.2.12.2Test parameters6756

A.20.5.2.12.3Test Requirements6757

A.20.5.3L1-RSRP measurement for beam reporting for (e)RedCap UE with Satellite Access6757

A.20.5.3.1SSB based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is not used for 1Rx (e)RedCap UE with NTN6757

A.20.5.3.1.1Test Purpose and Environment6757

A.20.5.3.1.2Test parameters6757

A.20.5.3.1.3Test Requirements6759

A.20.5.3.2SSB based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is not used for 2Rx (e)RedCap UE with NTN6759

A.20.5.3.2.1Test Purpose and Environment6759

A.20.5.3.2.2Test parameters6759

A.20.5.3.2.3Test Requirements6761

A.20.5.3.3CSI-RS based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is used for 1Rx (e)RedCap UE with NTN6761

A.20.5.3.3.1Test Purpose and Environment6761

A.20.5.3.3.2Test parameters6761

A.20.5.3.3.3Test Requirements6763

A.20.5.3.4CSI-RS based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is used for 2Rx (e)RedCap UE with NTN6763

A.20.5.3.4.1Test Purpose and Environment6763

A.20.5.3.4.2Test parameters6764

A.20.5.3.4.3Test Requirements6765

A.20.6Measurement Performance requirements6765

A.20.6.1SS-RSRP for SAN6765

A.20.6.1.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE6765

A.20.6.1.1.1Test Purpose and Environment6765

A.20.6.1.1.2Test parameters6765

A.20.6.1.1.3Test Requirements6767

A.20.6.1.2SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE6767

A.20.6.1.2.1Test Purpose and Environment6767

A.20.6.1.2.2Test parameters6767

A.20.6.1.2.3Test Requirements6768

A.20.6.1.3SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE6768

A.20.6.1.3.1Test Purpose and Environment6768

A.20.6.1.3.2Test parameters6769

A.20.6.1.3.3Test Requirements6770

A.20.6.1.4SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE6770

A.20.6.1.4.1Test Purpose and Environment6770

A.20.6.1.4.2Test parameters6770

A.20.6.1.4.3Test Requirements6772

A.20.6.2SS-RSRQ6772

A.20.6.2.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 1Rx RedCap UE6772

A.20.6.2.1.1Test Purpose and Environment6772

A.20.6.2.1.2Test Parameters6772

A.20.6.2.1.3Test Requirements6773

A.20.6.2.2SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 2Rx RedCap UE6773

A.20.6.2.2.1Test Purpose and Environment6773

A.20.6.2.2.2Test Parameters6773

A.20.6.2.2.3Test Requirements6775

A.20.6.2.3SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 1Rx RedCap UE6775

A.20.6.2.3.1Test Purpose and Environment6775

A.20.6.2.3.2Test Parameters6775

A.20.6.2.3.3Test Requirements6776

A.20.6.2.4SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 2Rx RedCap UE6776

A.20.6.2.4.1Test Purpose and Environment6776

A.20.6.2.4.2Test Parameters6776

A.20.6.2.4.3Test Requirements6778

A.20.6.3SS-SINR6778

A.20.6.3.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE6778

A.20.6.3.1.1Test Purpose and Environment6778

A.20.6.3.1.2Test Parameters6778

A.20.6.3.1.3Test Requirements6779

A.20.6.3.2SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE6780

A.20.6.3.2.1Test Purpose and Environment6780

A.20.6.3.2.2Test Parameters6780

A.20.6.3.2.3Test Requirements6781

A.20.6.3.3SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE6781

A.20.6.3.3.1Test Purpose and Environment6781

A.20.6.3.3.2Test Parameters6781

A.20.6.3.3.3Test Requirements6783

A.20.6.3.4SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE6783

A.20.6.3.4.1Test Purpose and Environment6783

A.20.6.3.4.2Test Parameters6783

A.20.6.3.4.3Test Requirements6784

A.20.6.4L1-RSRP measurement for beam reporting6785

A.20.6.4.1SSB based L1-RSRP measurement for 1Rx RedCap UE6785

A.20.6.4.1.1Test Purpose and Environment6785

A.20.6.4.1.2Test parameters6785

A.20.6.4.1.3Test Requirements6786

A.20.6.4.2SSB based L1-RSRP measurement for 2Rx RedCap UE6786

A.20.6.4.2.1Test Purpose and Environment6786

A.20.6.4.2.2Test parameters6786

A.20.6.4.2.3Test Requirements6788

A.20.6.4.3CSI-RS based L1-RSRP measurement on resource set with repetition off for 1Rx RedCap UE6788

A.20.6.4.3.1Test Purpose and Environment6788

A.20.6.4.3.2Test parameters6788

A.20.6.4.3.3Test Requirements6789

A.20.6.4.4CSI-RS based L1-RSRP measurement on resource set with repetition off for 2Rx RedCap UE6789

A.20.6.4.4.1Test Purpose and Environment6789

A.20.6.4.4.2Test parameters6790

A.20.6.4.4.3Test Requirements6791

A.21NR standalone tests for LP-WUR6791

A.21.1RRC_IDLE state mobility6791

A.21.1.1UE exits offloading mode to legacy mode with LR using LP-SS signal6791

A.21.1.1.1Test Purpose and Environment6791

A.21.1.1.2Test Parameters6791

A.21.1.1.3Test Requirements6794

A.21.1.2UE exits from relaxed measurement mode with LR using PSS/SSS in FR16794

A.21.1.2.1Test Procedure and Environment6794

A.21.1.2.2Test Parameters6794

A.21.1.2.3Test Requirements6798

A.21.1.3UE exits relaxed measurement mode to legacy mode with LR using LP-SS signal6798

A.21.1.3.1Test Purpose and Environment6798

A.21.1.3.2Test Parameters6798

A.21.1.3.3Test Requirements6801

A.21.1.4UE exit from relaxed measurement mode with LR using PSS/SSS in FR26801

A.21.1.4.1Test Purpose and Environment6801

A.21.1.4.2Test Parameters6801

A.21.1.4.3Test Requirements6804

Annex B (normative):Conditions for RRM requirements applicability for operating bands6805

B.1Conditions for NR RRC_IDLE state mobility6805

B.1.1Introduction6805

B.1.2Conditions for measurements on NR intra-frequency cells for cell re-selection6805

B.1.2AConditions for measurements on NR intra-frequency cells under CCA for cell re-selection6807

B.1.3Conditions for measurements on NR inter-frequency cells for cell re-selection6808

B.1.3AConditions for measurements on NR inter-frequency cells under CCA for cell re-selection6808

B.1.4Conditions for measurements on NR intra-frequency cells for cell re-selection for RedCap6808

B.1.5Conditions for measurements on NR inter-frequency cells for cell re-selection for RedCap6811

B.1.6Conditions for measurements on NR intra-frequency cells for cell re-selection for satellite access6811

B.1.7Conditions for measurements on NR inter-frequency cells for cell re-selection for satellite access6811

B.1.8Conditions for measurements on NR serving cells by LP-WUR6811

B.2Conditions for UE measurements procedures and performance requirements in RRC_CONNECTED state6812

B.2.1Introduction6812

B.2.1.1General6812

B.2.1.2Derivation of Minimum SSB_RP values for FR16812

B.2.1.3Derivation of Minimum SSB_RP values for FR26812

B.2.1.3.1Minimum SSB_RP values for Rx Beam Peak angle of arrival6813

B.2.1.3.2Minimum SSB_RP values for angle of arrival within Spherical coverage6813

B.2.1.4Gain to SS-RSRP and CSI-RSRP measurement point for FR16814

B.2.1.5Gain to SS-RSRP and CSI-RSRP measurement point for FR26814

B.2.1.5.1Gain to SS-RSRP and CSI-RSRP measurement point for Rx Beam Peak angle of arrival6814

B.2.1.5.2Gain to SS-RSRP measurement point for different frequency6815

B.2.1.5.3Alignment of Rough beam to Rx beam Peak6815

B.2.1.6Gain to PRS-RSRP measurement point for FR26815

B.2.1.6.1Gain to PRS-RSRP measurement point for Rx Beam Peak angle of arrival6815

B.2.1.7Derivation of Minimum SSB_RP values for FR2-NTN for satellite access6816

B.2.1.7.1Minimum SSB_RP values for Rx Beam6816

B.2.1.8Gain to SS-RSRP for FR2-NTN for satellite access6817

B.2.2Conditions for NR intra-frequency measurements6817

B.2.3Conditions for NR inter-frequency measurements6820

B.2.4Conditions for NR L1-RSRP reporting6822

B.2.4.1Conditions for SSB based L1-RSRP reporting6822

B.2.4.2Conditions for CSI-RS based L1-RSRP reporting6824

B.2.5Conditions for RRC connection release with redirection to NR6826

B.2.6Void6828

B.2.6.1Void6828

B.2.6.2Void6828

B.2.7Conditions for SRS-RSRP measurements6828

B.2.8Conditions for NR L1-SINR reporting6829

B.2.8.1Conditions for L1-SINR reporting with CSI-RS based CMR and no dedicated IMR configured6829

B.2.8.2Conditions for L1-SINR reporting with SSB based CMR and dedicated IMR configured6831

B.2.8.2.1L1-SINR reporting with SSB based CMR and dedicated ZP-IMR configured6831

B.2.8.2.2L1-SINR reporting with SSB based CMR and dedicated NZP-IMR configured6833

B.2.8.3Conditions for L1-SINR reporting with CSI-RS based CMR and dedicated IMR configured6835

B.2.8.3.1L1-SINR reporting with CSI-RS based CMR and dedicated ZP-IMR configured6835

B.2.8.3.2L1-SINR reporting with CSI-RS based CMR and dedicated NZP-IMR configured6837

B.2.9Conditions for NR intra-frequency measurements under CCA6839

B.2.10Conditions for NR inter-frequency measurements under CCA6839

B.2.11Conditions for NR L1-RSRP reporting under CCA6839

B.2.11.1Conditions for SSB based L1-RSRP reporting6839

B.2.12Conditions for NR CSI-RS based intra-frequency measurements6840

B.2.13Conditions for NR CSI-RS based inter-frequency measurements6841

B.2.14Conditions for NR PRS-based measurements6842

B.2.15Conditions for NR intra-frequency measurements for RedCap6844

B.2.16Conditions for NR inter-frequency measurements for RedCap6845

B.2.17Conditions for NR intra-frequency measurements for satellite access6847

B.2.18Conditions for NR inter-frequency measurements for satellite access6847

B.2.19Conditions for NR L1-RSRP reporting for satellite access6848

B.2.19.1Conditions for SSB based L1-RSRP reporting for satellite access6848

B.2.19.2Conditions for CSI-RS based L1-RSRP reporting for satellite access6848

B.2.20Conditions for RRC connection release with redirection to NR for satellite access6849

B.3RRM Requirements Exceptions6849

B.3.1Introduction6849

B.3.2Receiver sensitivity relaxation for CA6849

B.3.2.1Receiver sensitivity relaxation for UE supporting CA in FR16849

B.3.2.2Receiver sensitivity relaxation for UE configured with CA in FR16849

B.3.2.2.1Inter-band carrier aggregation6849

B.3.2.2.2Reference sensitivity exceptions due to UL harmonic interference for CA6850

B.3.2.2.3Reference sensitivity exceptions due to intermodulation interference due to 2UL CA6850

B.3.2.3Receiver sensitivity relaxation for UE supporting CA in FR26850

B.3.2.4Receiver sensitivity relaxation for UE configured with CA in FR26850

B.3.2.4.1Intra-band contiguous carrier aggregation6850

B.3.2.4.2Intra-band non-contiguous carrier aggregation6850

B.3.3Receiver sensitivity relaxation for DC6850

B.3.3.1Receiver sensitivity relaxation for EN-DC6850

B.3.3.2Receiver sensitivity relaxation for NE-DC6851

B.3.4Receiver sensitivity relaxation for SUL6851

B.3.4.1Receiver sensitivity relaxation for UE supporting SUL in FR16851

B.3.4.2Receiver sensitivity relaxation for UE configured with SUL in FR16851

B.3.4.2.1Reference sensitivity exceptions due to UL harmonic interference for SUL6851

B.4Conditions for V2X6851

B.4.1Test parameters for GNSS signals6851

B.4.2Conditions for PSBCH-RSRP Accuracy Requirements6851

B.4.3Conditions for Selection/Reselection to Intra-frequency SyncRef UE6852

B.4.4Conditions for L1 SL-RSRP Accuracy Requirements6852

B.4.5Conditions for PSBCH-RSRP Accuracy Requirements under CCA6852

B.4.6Conditions for Selection/Reselection to Intra-frequency SyncRef UE under CCA6853

B.4.7Conditions for L1 SL-RSRP Accuracy Requirements under CCA6853

B.4AConditions for NR Sidelink Positioning Measurement Procedures and Performance Requirements6854

B.4A.1Conditions for NR SL-PRS based measurements6854

B.5High level test procedure for SAN RRM tests6854

Annex C (informative):Change history6856
