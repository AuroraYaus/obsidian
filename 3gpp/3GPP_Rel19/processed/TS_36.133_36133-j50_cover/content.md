---
type: spec
aliases:
  - 36.133_36133-j50_cover
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_36.133_36133-j50_cover/content.md"
---
# TS 36.133 36133-j50_cover

Contents

Foreword107

1Scope109

2References109

3Definitions, symbols and abbreviations111

3.1Definitions111

3.2Symbols113

3.3Abbreviations114

3.4Test tolerances117

3.5Additional notation117

3.5.1Groups of bands117

3.5.1AGroups of bands for satellite access120

3.6General121

3.6.1Applicability of requirements in this specification version121

3.6.1.1Applicability of requirements for UE capable of network-based CRS interference mitigation127

3.6.1.2Applicability of requirements with CRS muting for category M1 UE capable of CRS muting129

3.6.1.3Applicability of requirements with CRS muting for category M2 UE capable of CRS muting130

3.6.2Applicability of requirements for EN-DC operation131

3.6.3Applicability of requirements for NE-DC operation132

3.6.4Applicability of requirements for NGEN-DC operation133

3.6.5Applicability of 2-step RA and 4-step RA in RRM requirements133

## 3.6.6 Applicability of requirements for UE category NB-IoT for frame structure type 1 for NTN-TDD133

3.6.7Applicability of NB-IoT inband operation in NTN NR133

Rel-18 UEs supporting only standalone operation do not need to be tested for in-band operation with NR over NTN. In-band operation with NR NTN is not supported in Rel-17.133

4E-UTRAN RRC_IDLE state mobility133

4.1Cell Selection133

4.2Cell Re-selection134

4.2.1Introduction134

4.2.2Requirements134

4.2.2.1Measurement and evaluation of serving cell135

4.2.2.2Void136

4.2.2.3Measurements of intra-frequency E-UTRAN cells136

4.2.2.4Measurements of inter-frequency E-UTRAN cells138

4.2.2.5Measurements of inter-RAT cells140

4.2.2.5.1Measurements of UTRAN FDD cells140

4.2.2.5.2Measurements of UTRAN TDD cells142

4.2.2.5.3Measurements of GSM cells144

4.2.2.5.4Measurements of HRPD cells145

4.2.2.5.5Measurements of cdma2000 1X146

4.2.2.5.6Measurements of NR cells147

4.2.2.5.7Measurements of NR cells subject to CCA150

4.2.2.5.8Measurements of NR cells for RedCap152

4.2.2.6Evaluation of cell re-selection criteria154

4.2.2.7Maximum interruption in paging reception154

4.2.2.8void155

4.2.2.9UE measurement capability155

4.2.2.9aUE measurement capability (Increased UE carrier monitoring)156

4.2.2.10Reselection to CSG cells156

4.2.2.10.1Reselection from a non CSG to an inter-frequency CSG cell156

4.2.2.10.2Reselection from a non CSG to an inter-RAT UTRAN FDD CSG cell157

4.2.2.11Void158

4.2.2.12Void158

4.2.2.13Void158

4.2.2.14UE measurement capability for RedCap158

4.3Minimization of Drive Tests (MDT)159

4.3.1Introduction159

4.3.2Measurements159

4.3.2.1Requirements159

4.3.3Relative Time Stamp Accuracy159

4.3.3.1Requirements159

4.3.4Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting160

## 4.3.4.1 Requirements160

4.3.5Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting160

4.3.5.1Requirements for timeSinceFailure160

4.4MBSFN Measurements160

4.4.1Introduction160

4.4.2MBSFN RSRP measurements160

4.4.3MBSFN RSRQ measurements161

4.4.4MCH BLER measurements161

4.5Proximity-based Services161

4.5.1Introduction161

4.5.2Requirements161

4.5.2.1Interruptions with ProSe Direct Discovery161

4.5.2.2Interruptions with ProSe Direct Communication161

4.5.2.3Initiation/Cease of SLSS transmissions with ProSe Direct Discovery162

4.5.2.4Initiation/Cease of SLSS transmissions with ProSe Direct Communication162

4.6Cell Selection and Re-selection Requirements for UE category NB1163

4.6.1Cell Selection163

4.6.2Cell Re-selection163

4.6.2.1Measurement and evaluation of serving NB-IoT cell for UE category NB1 in normal coverage163

4.6.2.1AMeasurement and evaluation of serving NB-IoT cell for HD-FDD UE category NB1 in normal coverage when configured with WUS164

4.6.2.2Measurements of intra-frequency NB-IoT cells for UE category NB1 in normal coverage165

4.6.2.3Measurement and evaluation of serving NB-IoT cell for UE category NB1 in enhanced coverage166

4.6.2.3AMeasurement and evaluation of serving NB-IoT cell for HD-FDD UE category NB1 in enhanced coverage when configured with WUS168

4.6.2.4Measurements of intra-frequency NB-IoT cells for UE category NB1 in enhanced coverage169

4.6.2.5Measurements of inter-frequency NB cells for UE category NB1 in normal coverage170

4.6.2.6Measurements of inter-frequency NB-IoT cells for UE category NB1 in enhanced coverage171

4.6.2.7Maximum interruption in paging reception in normal coverage173

4.6.2.7AMaximum interruption in paging reception in enhanced coverage173

4.6.2.8UE measurement capability173

4.6.2.9WUS receptions for NB1173

4.6.3Requirements for transmission using preconfigured uplink resources for UE category NB1174

4.6.3.1Introduction174

4.6.3.2Requirements on UE synchronization for transmission using PUR174

4.6.3.3Requirements on TA validation for transmission using PUR174

4.6ACell Selection and Re-selection Requirements for UE category NB-IoT for Satellite Access175

4.6A.1Cell Selection175

4.6A.2Cell Re-selection for UE category NB-IoT for Satellite Access175

4.6A.2.1Measurement and evaluation of serving NB-IoT cell for UE category NB1 in normal coverage176

4.6A.2.1AMeasurement and evaluation of serving NB-IoT cell for HD-FDD UE category NB1 in normal coverage when configured with WUS177

4.6A.2.2Measurements of intra-frequency NB-IoT cells for UE category NB1 in normal coverage178

4.6A.2.3Measurement and evaluation of serving NB-IoT cell for UE category NB1 in enhanced coverage180

4.6A.2.3AMeasurement and evaluation of serving NB-IoT cell for HD-FDD UE category NB1 in enhanced coverage when configured with WUS182

4.6A.2.4Measurements of intra-frequency NB-IoT cells for UE category NB1 in enhanced coverage183

4.6A.2.5Measurements of inter-frequency NB cells for UE category NB1 in normal coverage185

4.6A.2.6Measurements of inter-frequency NB-IoT cells for UE category NB1 in enhanced coverage187

4.6A.2.7Maximum interruption in paging reception in normal coverage189

4.6A.2.7AMaximum interruption in paging reception in enhanced coverage189

4.6A.2.8UE measurement capability190

4.6A.2.9WUS receptions for NB1190

4.6A.3Requirements for transmission using preconfigured uplink resources for UE category NB-IoT for Satellite Access191

4.6A.3.1Introduction191

4.6A.3.2Requirements on UE synchronization for transmission using PUR191

4.6A.3.3Requirements on TA validation for transmission using PUR191

4.6BCell Selection and Re-selection Requirements for UE category NB-IoT for frame structure type 1 for NTN-TDD191

4.6B.1Cell Selection191

4.6B.2Cell Re-selection for UE category NB-IoT for Satellite Access191

4.6B.2.1Measurement and evaluation of serving NB-IoT cell for UE category NB1 in normal coverage192

4.6B.2.2Measurements of intra-frequency NB-IoT cells for UE category NB1 in normal coverage193

4.6B.2.5Measurements of inter-frequency NB cells for UE category NB1 in normal coverage194

4.6B.2.7Maximum interruption in paging reception in normal coverage195

4.6B.2.8UE measurement capability195

4.7Cell Selection and Re-selection Requirements for UE category M1196

4.7.1Cell Selection196

4.7.2Cell Re-selection196

4.7.2.1Cell Re-selection requirements for UE category M1 in normal coverage196

4.7.2.1.1Measurement and evaluation of serving cell for UE category M1 in normal coverage196

4.7.2.1.1ARelaxed measurement and evaluation of serving cell for UE category M1 in normal coverage197

4.7.2.1.2Measurements of intra-frequency cells for UE category M1 in normal coverage198

4.7.2.1.3Measurements of inter-frequency cells for UE category M1 in normal coverage199

4.7.2.1.4Maximum allowed layers for multiple monitoring for UE category M1 in normal coverage201

4.7.2.1.5Maximum interruption in paging reception for Category M1 UEs in normal coverage201

4.7.2.2Cell Re-selection requirements for UE category M1 in enhanced coverage202

4.7.2.2.1Measurement and evaluation of serving cell for UE category M1 in enhanced coverage202

4.7.2.2.1ARelaxed measurement and evaluation of serving cell for UE category M1 in enhaned coverage203

4.7.2.2.2Measurements of intra-frequency cells for UE category M1 in enhanced coverage204

4.7.2.2.3Measurements of inter-frequency cells for UE category M1 in enhanced coverage207

4.7.2.2.4Maximum allowed layers for multiple monitoring for UE category M1 in enhanced coverage208

4.7.2.2.5Maximum interruption in paging reception for Category M1 UEs in enhanced coverage209

4.7.2.3WUS receptions for UE category M1209

4.7.3Channel quality report for UE Category M1 in idle mode209

4.7.4Requirements for transmission using preconfigured uplink resources for UE category M1210

4.7.4.1Introduction210

4.7.4.2Requirements on UE synchronization for transmission using PUR210

4.7.4.3Requirements on TA validation for transmission using PUR210

4.7ACell Selection and Re-selection Requirements for UE category M1 for Satellite Access211

4.7A.1Cell Selection211

4.7A.2Cell Re-selection for UE category M1 for Satellite Access211

4.7A.2.1Cell Re-selection requirements for UE category M1 in normal coverage212

4.7A.2.1.1Measurement and evaluation of serving cell for UE category M1 in normal coverage212

4.7A.2.1.1ARelaxed measurement and evaluation of serving cell for UE category M1 in normal coverage214

4.7A.2.1.2Measurements of intra-frequency cells for UE category M1 in normal coverage215

4.7A.2.1.3Measurements of inter-frequency cells for UE category M1 in normal coverage218

4.7A.2.1.4Maximum allowed layers for multiple monitoring for UE category M1 in normal coverage220

4.7A.2.1.5Maximum interruption in paging reception for Category M1 UEs in normal coverage220

4.7A.2.2Cell Re-selection requirements for UE category M1 in enhanced coverage221

4.7A.2.2.1Measurement and evaluation of serving cell for UE category M1 in enhanced coverage221

4.7A.2.2.1ARelaxed measurement and evaluation of serving cell for UE category M1 in enhaned coverage222

4.7A.2.2.2Measurements of intra-frequency cells for UE category M1 in enhanced coverage224

4.7A.2.2.3Measurements of inter-frequency cells for UE category M1 in enhanced coverage226

4.7A.2.2.4Maximum allowed layers for multiple monitoring for UE category M1 in enhanced coverage229

4.7A.2.2.5Maximum interruption in paging reception for Category M1 UEs in enhanced coverage229

4.7A.2.3WUS receptions for UE category M1230

4.7A.3Channel quality report for UE Category M1 in idle mode for Satellite Access230

4.7A.4Requirements for transmission using preconfigured uplink resources for UE category M1 for Satellite Access231

4.7A.4.1Introduction231

4.7A.4.2Requirements on UE synchronization for transmission using PUR231

4.7A.4.3Requirements on TA validation for transmission using PUR231

4.8Idle State Positioning Measurement Requirements for UE category NB1231

4.8.1OTDOA Intra-Frequency RSTD Measurements for UE category NB1 for normal coverage231

4.8.1.1RSTD Measurement Reporting Delay233

4.8.2OTDOA Intra-Frequency RSTD Measurements for UE category NB1 for enhanced coverage233

4.8.2.1RSTD Measurement Reporting Delay234

4.8.3OTDOA Inter-Frequency RSTD Measurements for UE category NB1 for normal coverage235

4.8.3.1RSTD Measurement Reporting Delay236

4.8.4OTDOA Inter-Frequency RSTD Measurements for UE category NB1 for enhanced coverage237

4.8.4.1RSTD Measurement Reporting Delay238

4.8.5Intra-Frequency E-CID NRSRP and NRSRQ Measurements for UE category NB2 for normal coverage239

4.8.5.1Measurement Reporting Delay240

4.8.6Intra-Frequency E-CID NRSRP and NRSRQ Measurements for UE category NB2 for enhanced coverage240

4.8.6.1Measurement Reporting Delay241

4.8.7Inter-Frequency E-CID NRSRP and NRSRQ Measurements for UE category NB2 for normal coverage242

4.8.7.1Measurement Reporting Delay243

4.8.8Inter-Frequency E-CID NRSRP and NRSRQ Measurements for UE category NB2 for enhanced coverage243

4.8.8.1Measurement Reporting Delay244

4.9Idle Mode CA Measurement245

4.9.1Introduction245

4.9.2Requirement245

4.9.2.1Detected cell requirement during state transition and Idle mode245

4.9.2.2Measurements of inter-frequency CA candidate cells246

4.9.2.3Measurements on serving cell246

4AE-UTRAN RRC_INACTIVE state mobility247

4A.1Cell Re-selection247

4A.1.1Introduction248

4A.1.2Requirements248

4A.1.2.1UE measurement capability248

4A.1.2.2Measurement and evaluation of serving cell248

4A.1.2.3Measurements of intra-frequency E-UTRAN cells248

4A.1.2.4Measurements of inter-frequency E-UTRAN cells248

4A.1.2.5Evaluation of cell re-selection criteria248

4A.1.2.6Maximum interruption in paging reception248

4A.1.2.7Measurements of inter-RAT NR cells248

4A.1.2.8UE measurement capability for RedCap248

4A.1.2.9Measurements of inter-RAT NR cells for RedCap248

4A.2Requirements for UE Category M1249

4A.2.1Introduction249

4A.2.2Cell Selection249

4A.2.3Cell Reselection249

4A.2.3.1Cell Re-selection requirements for UE category M1 in normal coverage249

4A.2.3.1.1Measurement and evaluation of serving cell for UE category M1 in normal coverage249

4A.2.3.1.2Measurements of intra-frequency cells for UE category M1 in normal coverage250

4A.2.3.1.3Measurements of inter-frequency cells for UE category M1 in normal coverage250

4A.2.3.1.4Maximum allowed layers for multiple monitoring for UE category M1 in normal coverage250

4A.2.3.1.5Maximum interruption in paging reception for Category M1 UEs in normal coverage250

4A.2.4Channel quality report for UE Category M1 in idle mode252

5E-UTRAN RRC_CONNECTED state mobility252

5.1E-UTRAN Handover253

5.1.1Introduction253

5.1.2Requirements253

5.1.2.1E-UTRAN FDD – FDD253

5.1.2.1.1Handover delay253

5.1.2.1.2Interruption time253

5.1.2.2E-UTRAN FDD – TDD254

5.1.2.2.1(Void)255

5.1.2.2.2(Void)255

5.1.2.3E-UTRAN TDD – FDD255

5.1.2.3.1(Void)255

5.1.2.3.2(Void)255

5.1.2.4E-UTRAN TDD – TDD255

5.1.2.4.1Handover delay255

5.1.2.4.2Interruption time255

5.1.2.5E-UTRAN HD–FDD257

5.1.2.5.1Handover delay257

5.1.2.5.2Interruption time257

5.1.2.6E-UTRAN FDD – FDD conditional handover258

5.1.2.6.1Handover delay258

5.1.2.6.2Measurement time259

5.1.2.6.3Preparation time259

5.1.2.6.4Interruption time259

5.1.2.7E-UTRAN FDD – TDD conditional handover259

5.1.2.8E-UTRAN TDD – FDD conditional handover260

5.1.2.9E-UTRAN TDD – TDD conditional handover260

5.2Void260

5.3Handover to other RATs260

5.3.1E-UTRAN - UTRAN FDD Handover260

5.3.1.1Introduction260

5.3.1.1.1Handover delay260

5.3.1.1.2Interruption time260

5.3.2E-UTRAN - UTRAN TDD Handover261

5.3.2.1Introduction261

5.3.2.2Requirements261

5.3.2.2.1Handover delay261

5.3.2.2.2Interruption time261

5.3.3E-UTRAN - GSM Handover262

5.3.3.1Introduction262

5.3.3.2Requirements262

5.3.3.2.1Handover delay262

5.3.3.2.2Interruption time262

5.3.4E-UTRAN - NR FR1 Handover262

5.3.4.1Introduction262

5.3.4.2Handover delay263

5.3.4.3Interruption time263

5.3.4AE-UTRAN - NR FR1 Handover to target cell using CCA263

5.3.4A.1Introduction263

5.3.4A.2Handover delay264

5.3.4A.3Interruption time264

5.3.4BE-UTRAN - NR FR1 Handover for RedCap265

5.3.4B.1Introduction265

5.3.4B.2Requirements265

5.3.5E-UTRAN - NR FR2 Handover265

5.3.5.1Introduction265

5.3.5.2Handover delay265

5.3.5.3Interruption time265

5.4Handover to Non-3GPP RATs266

5.4.1E-UTRAN – HRPD Handover266

5.4.1.1Introduction266

5.4.1.1.1Handover delay266

5.4.1.1.2Interruption time266

5.4.2E-UTRAN – cdma2000 1X Handover267

5.4.2.1Introduction267

5.4.2.1.1Handover delay267

5.4.2.1.2Interruption time267

5.5E-UTRAN Handover for Cat-M1 UEs267

5.5.1Introduction267

5.5.2Requirements in CEModeA268

5.5.2.1E-UTRAN FDD – FDD for Cat-M1 FDD UEs268

5.5.2.1.1Handover delay268

5.5.2.1.2Interruption time268

5.5.2.2E-UTRAN FDD – FDD for Cat-M1 HD – FDD UEs268

5.5.2.3E-UTRAN TDD – TDD for Cat-M1 TDD UEs269

5.5.2.3.1Void269

5.5.2.3.2Void269

5.5.3Requirements in CEModeB269

5.5.3.1E-UTRAN FDD – FDD for Cat-M1 FDD UEs269

5.5.3.1.1Handover delay269

5.5.3.1.2Interruption time269

5.5.3.2E-UTRAN FDD – FDD for Cat-M1 HD – FDD UEs270

5.5.3.3E-UTRAN TDD – TDD for Cat-M1 TDD UEs270

5.5AE-UTRAN Handover for Cat-M1 UEs for Satellite Access270

5.5A.1Introduction270

5.5A.2Requirements in CEModeA270

5.5A.2.1E-UTRAN FDD – FDD HO for Cat-M1 FDD UEs270

5.5A.2.1.1Handover delay270

5.5A.2.1.2Interruption time270

5.5A.2.2E-UTRAN FDD – FDD HO for Cat-M1 HD – FDD UEs271

5.5A.2.3E-UTRAN FDD – FDD conditional HO for Cat-M1 FDD UEs271

5.5A.2.3.1Handover delay271

5.5A.2.3.2Measurement time272

5.5A.2.3.3Preparation time273

5.5A.2.3.4Interruption time273

5.5A.2.4E-UTRAN FDD – FDD conditional HO for Cat-M1 HD – FDD UEs274

5.5A.3Requirements in CEModeB274

5.5A.3.1E-UTRAN FDD – FDD HO for Cat-M1 FDD UEs274

5.5A.3.1.1Handover delay274

5.5A.3.1.2Interruption time274

5.5A.3.2E-UTRAN FDD – FDD HO for Cat-M1 HD – FDD UEs275

5.5A.3.3E-UTRAN FDD – FDD conditional HO for Cat-M1 FDD UEs275

5.5A.3.3.1Handover delay275

5.5A.3.3.2Measurement time276

5.5A.3.3.3Preparation time277

5.5A.3.3.4Interruption time277

5.5A.3.4E-UTRAN FDD – FDD conditional HO for Cat-M1 HD – FDD UEs278

5.6Void278

5.7E-UTRAN DAPS Handover278

5.7.1Introduction278

5.7.2Requirements279

5.7.2.1E-UTRAN FDD – FDD279

5.7.2.1.1DAPS Handover delay279

5.7.2.1.2Interruption time279

5.7.2.2E-UTRAN FDD – TDD280

5.7.2.3E-UTRAN TDD – FDD280

5.7.2.4E-UTRAN TDD – TDD280

5.8EN-DC Handover with PSCell280

5.8.1Introduction280

5.8.1.1Handover with PSCell Interruption time280

5.8.1.2Handover with PSCell - NR PSCell Change Delay requirements281

5.9EN-DC Handover with PSCell using CCA282

5.9.1Introduction282

5.9.1.1Handover with PSCell – E-UTRA HO Interruption time282

5.9.1.2Handover with PSCell - NR PSCell Change Delay requirements282

6RRC Connection Mobility Control283

6.1RRC Re-establishment283

6.1.1Introduction283

6.1.2Requirements283

6.1.2.1UE Re-establishment delay requirement284

6.2Random Access284

6.2.1Introduction284

6.2.2Requirements284

6.2.2.1Contention based random access284

6.2.2.1.1Correct behaviour when receiving Random Access Response reception284

6.2.2.1.2Correct behaviour when not receiving Random Access Response reception285

6.2.2.1.3Correct behaviour when receiving a NACK on msg3285

6.2.2.1.4Void285

6.2.2.1.5Correct behaviour when receiving a message over Temporary C-RNTI285

6.2.2.1.6Correct behaviour when contention Resolution timer expires285

6.2.2.2Non-Contention based random access285

6.2.2.2.1Correct behaviour when receiving Random Access Response285

6.2.2.2.2Correct behaviour when not receiving Random Access Response285

6.2.3Requirements for Cat-M1 UEs285

6.2.3ARandom Access Requirements for Cat-M1 UEs for Satellite Access286

6.2.4ARandom Access Requirements for Cat-M1 UEs with CB-Msg3 EDT for Satellite Access286

6.2.4A.1Correct behaviour when transmitting CB-Msg3286

6.2.4A.2Correct behaviour when receiving CB-Msg4286

6.2.4A.3Correct behaviour when not receiving CB-Msg4286

6.2.4A.4MSG3-based channel quality report for UE Category NB1 with CB-Msg3-EDT procedure286

6.3RRC Connection Release with Redirection287

6.3.1Introduction287

6.3.2Requirements287

6.3.2.1RRC connection release with redirection to UTRAN FDD287

6.3.2.2RRC connection release with redirection to GERAN288

6.3.2.3RRC connection release with redirection to UTRAN TDD288

6.3.2.4RRC connection release with redirection to NR289

6.3.2.5RRC connection release with redirection to NR carrier subject to CCA289

6.3.2.6RRC connection release with redirection to NR Redcap291

6.4CSG Proximity Indication for E-UTRAN and UTRAN292

6.4.1Introduction292

6.4.2Requirements292

6.5RRC Re-establishment for NB-IoT UEs292

6.5.1Introduction292

6.5.2Requirements292

6.5.2.1UE Re-establishment delay requirement in normal coverage292

6.5.2.2UE Re-establishment delay requirement in enhanced coverage293

6.5ARRC Re-establishment for NB-IoT UEs for Satellite Access293

6.5A.1Introduction293

6.5A.2Requirements294

6.5A.2.1UE Re-establishment delay requirement in normal coverage294

6.5A.2.2UE Re-establishment delay requirement in enhanced coverage294

6.5BRRC Re-establishment for NB-IoT UEs for frame structure type 1 for NTN-TDD295

6.5B.1Introduction295

6.5B.2Requirements295

6.5B.2.1UE Re-establishment delay requirement in normal coverage295

6.6Random Access for UE category NB1296

6.6.1Introduction296

6.6.2Requirements296

6.6.2.1Correct behaviour when receiving Random Access Response reception296

6.6.2.2Correct behaviour when not receiving Random Access Response reception296

6.6.2.3Correct behaviour when receiving a NACK on msg3297

6.6.2.4Correct behaviour when receiving a message over Temporary C-RNTI297

6.6.2.5Correct behaviour when contention Resolution timer expires297

6.6.2.6MSG3-based channel quality report for UE Category NB1297

6.6.3Requirements for NPRACH configuration297

6.6ARandom Access for UE category NB-IoT for Satellite Access298

6.6A.1Introduction298

6.6A.2Requirements298

6.6A.2.1Correct behaviour when receiving Random Access Response reception298

6.6A.2.2Correct behaviour when not receiving Random Access Response reception298

6.6A.2.3Correct behaviour when receiving a NACK on msg3298

6.6A.2.4Correct behaviour when receiving a message over Temporary C-RNTI298

6.6A.2.5Correct behaviour when contention Resolution timer expires299

6.6A.2.6MSG3-based channel quality report for UE Category NB1299

6.6A.3Requirements for NPRACH configuration299

6.6A.4Requirements for CB-Msg3-EDT procedure300

6.6A.4.1 Correct behaviour when transmitting CB-Msg3300

6.6A.4.2Correct behaviour when receiving a CB-Msg4 over CB-RNTI300

6.6A.4.3Correct behaviour when detecting CB-Msg3-EDT failure300

6.6A.4.4MSG3-based channel quality report for UE Category NB1 with CB-Msg3-EDT procedure300

6.6BRandom Access for UE category NB-IoT for frame structure type 1 for NTN-TDD301

6.6B.1Introduction301

6.6B.2Requirements301

6.6B.2.1Correct behaviour when receiving Random Access Response reception301

6.6B.2.2Correct behaviour when not receiving Random Access Response reception301

6.6B.2.3Correct behaviour when receiving a NACK on msg3302

6.6B.2.4Correct behaviour when receiving a message over Temporary C-RNTI302

6.6B.2.5Correct behaviour when contention Resolution timer expires302

6.6B.2.6MSG3-based channel quality report for UE Category NB1302

6.6B.3Requirements for NPRACH configuration302

6.7RRC Re-establishment for Cat-M1 UEs303

6.7.1Introduction303

6.7.2Requirements303

6.7.2.1UE Re-establishment delay requirement for CEModeA303

6.7.2.2UE Re-establishment delay requirement for CEModeB304

6.7ARRC Re-establishment for Cat-M1 UEs for Satellite Access304

6.7A.1Introduction304

6.7A.2Requirements304

6.7A.2.1UE Re-establishment delay requirement for CEModeA305

6.7A.2.2UE Re-establishment delay requirement for CEModeB305

6.8RRC Connection Release with Redirection for Cat-M1 UEs306

6.8.1Introduction306

6.8.2Requirements306

6.8.2.1RRC connection release with redirection to E-UTRAN with CE Mode A306

6.8ARRC Connection Release with Redirection for UE Category M1 for Satellite Access307

6.8A.1Introduction307

6.8A.2Requirements307

6.8A.2.1RRC connection release with redirection to E-UTRAN with CE Mode A307

6.9RRC Connection Redirection to Non-anchor Carrier in NB-IoT308

6.9.1Introduction308

6.9.2Requirements308

6.9ARRC Connection Redirection to Non-anchor Carrier in NB-IoT for Satellite Access308

6.9A.1Introduction308

6.9BRRC Connection Redirection to Non-anchor Carrier in NB-IoT for frame structure type 1 for NTN-TDD309

6.9B.1Introduction309

6.9B.2Requirements310

7Timing and signalling characteristics310

7.1UE transmit timing310

7.1.1Introduction310

7.1.2Requirements311

7.2UE timer accuracy312

7.2.1Introduction312

7.2.2Requirements312

7.3Timing Advance312

7.3.1Introduction312

7.3.2Requirements312

7.3.2.1Timing Advance adjustment delay312

7.3.2.2Timing Advance adjustment accuracy313

7.4Cell phase synchronization accuracy (TDD)313

7.4.1Definition313

7.4.2Minimum requirements313

7.5Synchronization Requirements for E-UTRAN to 1xRTT and HRPD Handovers314

7.5.1Introduction314

7.5.2eNodeB Synchronization Requirements314

7.5.2.1Synchronized E-UTRAN314

7.5.2.2Non-Synchronized E-UTRAN314

7.6Radio Link Monitoring314

7.6.1Introduction314

7.6.2Requirements316

7.6.2.1Minimum requirement when no DRX is used316

7.6.2.2Minimum requirement when DRX is used316

7.6.2.3Minimum requirement at transitions318

7.6.2.4Minimum requirement during SI Acquisition with autonomous gaps318

7.6.2.5Minimum requirement under IDC Interference318

7.7SCell Activation and Deactivation Delay for E-UTRA Carrier Aggregation318

7.7.1Introduction318

7.7.2SCell Activation Delay Requirement for Deactivated SCell319

7.7.3SCell Deactivation Delay Requirement for Activated SCell320

7.7.4SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells321

7.7.5SCell Deactivation Delay Requirement for Activated SCell with Multiple Downlink SCells322

7.7.6SCell Activation Delay Requirement for Deactivated PUCCH SCell323

7.7.7SCell Activation Delay Requirement for Deactivated PUCCH SCell with Multiple SCells324

7.7.8SCell Deactivation Delay Requirement for Activated PUCCH SCell325

7.7.9SCell Deactivation Delay Requirement for Activated PUCCH SCell with Multiple SCells325

7.7.10SCell Activation Delay Requirement for Deactivated SCell under Frame Structure 3325

7.7.11SCell Deactivation Delay Requirement for Activated SCell under Frame Structure 3326

7.7.12SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells under Frame Structure 3327

7.7.13SCell Deactivation Delay Requirement for Activated SCell with Multiple Downlink SCells under Frame Structure 3328

7.7.14SCell Activation Delay Requirement for Dormant SCell328

7.7.15SCell Hibernation Delay Requirement for Activated SCell330

7.7.16SCell Hibernation Delay Requirement for Deactivated SCell330

7.7.17SCell Deactivation Delay Requirement for Dormant SCell332

7.7.18Direct SCell Activation and Hibernation Delay Requirement332

7.7.19Direct SCell Activation and Hibernation Delay Requirement at RRC Reconfiguration during Handover334

7.8Interruptions with Carrier Aggregation336

7.8.1Introduction336

7.8.2Requirements336

7.8.2.1Interruptions at SCell addition/release for intra-band CA336

7.8.2.2Interruptions at SCell addition/release for inter-band CA336

7.8.2.3Interruptions at SCell activation/deactivation for intra-band CA336

7.8.2.4Interruptions at SCell activation/deactivation for inter-band CA337

7.8.2.5Interruptions during measurements on SCC for intra-band CA337

7.8.2.6Interruptions during measurements on SCC for inter-band CA337

7.8.2.7Interruptions at SCell addition/release with multiple downlink SCells337

7.8.2.8Interruptions at SCell activation/deactivation with multiple downlink SCells337

7.8.2.9Interruptions during measurements on SCC with multiple downlink SCells338

7.8.2.10Interruptions at overlapping addition/release/activation/deactivation of SCells339

7.8.2.11Interruptions during RSSI measurements on one SCC under Frame Structure 3339

7.8.2.12Interruptions during RSSI measurements on multiple SCCs under Frame Structure 3339

7.8.2.13Interruptions at SRS carrier based switching340

7.8.2.14Interruptions at SCell activation and deactivation of dormant SCell for intra-band CA341

7.8.2.15Interruptions at SCell activation and deactivation of dormant SCell for inter-band CA341

7.8.2.16Interruptions at SCell activation and deactivation of multiple dormant SCells341

7.8.2.17Interruptions during CQI measurement on dormant SCell341

7.8.2.18Interruptions during RRM measurement on dormant SCell for intra-band CA342

7.8.2.19Interruptions during RRM measurement on dormant SCell for inter-band CA342

7.8.2.20Interruptions at SCell hibernation342

7.8.2.21Interruptions at direct SCell activation and hibernation342

7.8.2.22Interruptions during inter-RAT NR measurements without measurement gap343

7.9Maximum Transmission Timing Difference in Carrier Aggregation344

7.9.1Introduction344

7.9.2Minimum Requirements for Interband Carrier Aggregation344

7.9.3Minimum Requirements for Intraband non-contiguous Carrier Aggregation344

7.9.4Minimum Requirements for Inter-Band Carrier Aggregation under Frame Structure 3344

7.10Interruptions with RSTD Measurements with Carrier Aggregation345

7.10.1Introduction345

7.10.2Requirements345

7.10.2.1Interruptions during RSTD measurements on SCC for intra-band CA with one downlink SCell345

7.10.2.2Interruptions during RSTD measurements on SCC for inter-band CA with one downlink SCell345

7.10.2.3Interruptions during RSTD measurements on SCC with multiple downlink SCells345

7.10.2.4Interruptions at overlapping RSTD and inter-frequency measurements346

7.11Radio Link Monitoring for UE Category 0346

7.11.1Introduction346

7.11.2Requirements for FD-FDD and TDD347

7.11.2.1Minimum requirement when no DRX is used347

7.11.2.2Minimum requirement when DRX is used348

7.11.2.3Minimum requirement at transitions348

7.11.3Requirements for HD-FDD349

7.11.3.1Minimum requirement when no DRX is used349

7.11.3.2Minimum requirement when DRX is used349

7.11.3.3Minimum requirement at transitions350

7.12Interruptions with Dual Connectivity350

7.12.1Introduction350

7.12.2Requirements350

7.12.2.1Interruptions at PSCell addition/release350

7.12.2.2Interruptions at transitions between active and non-active during DRX350

7.12.2.3Interruptions at transitions from non-DRX to DRX351

7.12.2.4Interruptions at SCell addition/release351

7.12.2.5Interruptions at SCell activation/deactivation351

7.12.2.6Interruptions during measurements on SCC352

7.12.2.7Interruptions at SRS carrier based switching352

7.13Cell phase synchronization accuracy (Synchronized mode of dual connectivity)353

7.13.1Definition353

7.13.2Minimum requirements353

7.14PSCell Addition and Release Delay for E-UTRA Dual Connectivity353

7.14.1Introduction353

7.14.2PSCell Addition Delay Requirement353

7.14.3PSCell Release Delay Requirement354

7.15Maximum Receive Timing Difference in Dual Connectivity354

7.15.1Introduction354

7.15.2Minimum Requirements for Inter-band Dual Connectivity354

7.16Proximity-based Services354

7.16.1Introduction354

7.16.2Requirements354

7.16.2.1ProSe UE transmission timing354

7.16.2.1.1Serving cell or PCell as timing reference355

7.16.2.1.2SCell or non-serving cell as timing reference355

7.16.3Interruptions with ProSe355

7.16.3.1Interruptions at ProSe Direct Discovery configuration355

7.16.3.2Interruptions at ProSe Direct Communication configuration356

7.16.3.3Interruptions during ProSe Direct Discovery356

7.16.3.4Interruptions during ProSe Direct Discovery with discovery gaps356

7.16.3.5Interruptions during ProSe Direct Communication357

7.16.4Cell reselection for ProSe Direct Discovery on non-serving frequency357

7.16.4.1Measurement and evaluation of selected cell357

7.16.4.2Measurement of intra-frequency E-UTRAN cells357

7.16.5Selection / Reselection of ProSe relay UE358

7.16.6ProSe operation under deactivated SCell358

7.17Maximum Transmission Timing Difference in Dual Connectivity358

7.17.1Introduction358

7.17.2Minimum Requirements for maximum transmission timing difference Inter-band Dual Connectivity359

7.18.1Introduction359

7.18.2SCell Activation Delay Requirement for Deactivated SCell359

7.18.3SCell Deactivation Delay Requirement for Activated SCell359

7.19Radio Link Monitoring for UE Category M1359

7.19.1Introduction359

7.19.2Requirements for FD-FDD and TDD CE mode A360

7.19.2.1Minimum requirement when no DRX is used361

7.19.2.2Minimum requirement when DRX is used362

7.19.2.3Minimum requirement at transitions363

7.19.3Requirements for HD-FDD with CE mode A363

7.19.3.1Minimum requirement when no DRX is used364

7.19.3.2Minimum requirement when DRX is used364

7.19.3.3Minimum requirement at transitions365

7.19.4Requirements for FD-FDD and TDD with CE mode B365

7.19.4.1Minimum requirement when no DRX is used367

7.19.4.2Minimum requirement when DRX is used368

7.19.4.3Minimum requirement at transitions369

7.19.5Requirements for HD-FDD with CE mode B369

7.19.5.1Minimum requirement when no DRX is used369

7.19.5.2Minimum requirement when DRX is used370

7.19.5.3Minimum requirement at transitions371

7.19ARadio Link Monitoring for UE Category M1 for Satellite Access371

7.19A.1Introduction371

7.19A.2Requirements for FD-FDD and CE mode A371

7.19A.2.1Minimum requirement when no DRX is used373

7.19A.2.2Minimum requirement when DRX is used374

7.19A.2.3Minimum requirement at transitions375

7.19A.3Requirements for HD-FDD with CE mode A375

7.19A.3.1Minimum requirement when no DRX is used375

7.19A.3.2Minimum requirement when DRX is used376

7.19A.3.3Minimum requirement at transitions377

7.19A.4Requirements for HD-FDD with CE mode B377

7.19A.4.1Minimum requirement when no DRX is used377

7.19A.4.2Minimum requirement when DRX is used377

7.19A.4.3Minimum requirement at transitions378

7.20UE transmit timing for NB-IoT379

7.20.1Introduction379

7.20.2Requirements379

7.20AUE transmit timing for NB-IoT for Satellite Access379

7.20A.1Introduction379

7.20A.2Requirements380

7.20BUE transmit timing for NB-IoT for frame structure type 1 for NTN-TDD380

7.20B.1Introduction380

7.20B.2Requirements381

## 7.21 UE timer accuracy for NB-IoT381

7.21.1Introduction381

7.21.2Requirements381

7.21AUE timer accuracy for NB-IoT for Satellite Access382

7.21A.1Introduction382

7.21A.2Requirements382

7.21BUE timer accuracy for NB-IoT for frame structure type 1 for NTN-TDD382

7.21B.1Introduction382

7.21B.2Requirements382

7.22Timing Advance for NB-IoT383

7.22.1Introduction383

7.22.2Requirements383

7.22.2.1Timing Advance adjustment delay383

7.22.2.2Timing Advance adjustment accuracy383

7.22ATiming Advance for NB-IoT for Satellite Access383

7.22A.1Introduction383

7.22A.2Requirements383

7.22A.2.1Timing Advance adjustment delay383

7.22A.2.2Timing Advance adjustment accuracy383

7.22BTiming Advance for NB-IoT for frame structure type 1 for NTN-TDD383

7.22B.1Introduction383

7.22B.2Requirements383

7.22B.2.1Timing Advance adjustment delay383

7.22B.2.2Timing Advance adjustment accuracy384

7.23Radio Link Monitoring for Category NB1 UE384

7.23.1Introduction384

7.23.2Requirements for Category NB1 UE384

7.23.2.1Minimum requirement when no DRX is used384

7.23.2.2Minimum requirement when DRX is used385

7.23.2.3Minimum requirement at transitions385

7.23ARadio Link Monitoring for Category NB-IoT UE for Satellite Access386

7.23A.1Introduction386

7.23A.2Requirements for Category NB1 UE386

7.23A.2.1Minimum requirement when no DRX is used386

7.23A.2.2Minimum requirement when DRX is used387

7.23A.2.3Minimum requirement at transitions387

7.23BRadio Link Monitoring for Category NB-IoT UE for frame structure type 1 for NTN-TDD387

7.23B.1Introduction387

7.23B.2Requirements for Category NB1 UE388

7.23B.2.1Minimum requirement when no DRX is used388

7.23B.2.2Minimum requirement when DRX is used389

7.23B.2.3Minimum requirement at transitions389

7.24UE transmit timing for Category M1389

7.24.1Introduction389

7.24.2Requirements390

7.24AUE transmit timing for Category M1 for Satellite Access390

7.24A.1Introduction390

7.24A.2Requirements391

7.25Cell phase synchronization accuracy for MBMS services (FDD)392

7.25.1Definition392

7.25.2Minimum requirements392

7.26UE transmit timing for Category M2392

7.26.1Introduction392

7.26.2Requirements392

7.27UE timer accuracy for category M1393

7.27.1Introduction393

7.27.2Requirements393

7.27AUE timer accuracy for category M1 for Satellite Access393

7.27A.1Introduction393

7.27A.2Requirements393

7.28Timing Advance for Category M1393

7.28.1Introduction393

7.28.2Requirements393

7.28ATiming Advance for Category M1 for Satellite Access393

7.28A.1Introduction393

7.28A.2Requirements393

7.28A.2.1Timing Advance adjustment delay393

7.28A.2.2Timing Advance adjustment accuracy394

7.29Interruptions requirements with FeMBMS394

7.29.1Introduction394

7.29.2Requirements394

7.30Numerology switching delay requirements with FeMBMS394

7.30.1Introduction394

7.30.2Requirements394

7.31NR PSCell Addition and Release Delay for E-UTRA - NR Dual Connectivity394

7.31.1Introduction394

7.31.2NR PSCell Addition Delay Requirement395

7.31.3NR PSCell Release Delay Requirement395

7.31AAddition and Release Delay of NR PSCell Operating with CCA for E-UTRA - NR Dual Connectivity396

7.31A.1Introduction396

7.31A.2NR PSCell Addition Delay Requirement396

7.31A.3NR PSCell Release Delay Requirement397

7.32Interruptions with EN-DC397

7.32.1Introduction397

7.32.2Requirements398

7.32.2.1Interruptions at PSCell addition/release398

7.32.2.2Interruptions at transitions between active and non-active during DRX398

7.32.2.3Interruptions at transitions from non-DRX to DRX398

7.32.2.4Interruptions at SCell addition/release398

7.32.2.5Interruptions at SCell activation/deactivation398

7.32.2.6Interruptions during measurements on SCC399

7.32.2.6.1Interruptions during measurements on deactivated NR SCC399

7.32.2.6.2Interruptions during measurements on deactivated E-UTRA SCC399

7.32.2.6.3Interruptions during CQI measurements on dormant E-UTRA SCell399

7.32.2.6.4Interruptions during RRM measurements on dormant E-UTRA SCC400

7.32.2.7Interruptions at active BWP switching400

7.32.2.8Interruptions at SCell activation and deactivation of dormant SCell401

7.32.2.9Interruptions at SCell activation and deactivation of multiple dormant SCell401

7.32.2.10Interruptions at SCell hibernation401

7.32.2.11Interruptions at direct SCell activation and hibernation401

7.32.2.12DL Interruptions at UE switching between two uplink carriers401

7.32.2.13Interruptions at NR SRS carrier based switching401

7.32.2.14Interruptions at NR SCell dormancy402

7.32.2.14.1Interruptions due to NR SCell dormancy switch402

7.32.2.14.2Interruptions due to CSI and RRM measurements during SCell dormancy403

7.32.2.15Interruption during NR measurement with autonomous gaps403

7.32.2.16Interruptions at SRS carrier based switching403

7.32.2.17Interruptions at SCG activation/deactivation404

7.32.2.18Interruptions due to NR SRS antenna port switching404

7.32.2.19Interruptions at fast SCell activation/deactivation404

7.32.2.20Interruptions due to RRM measurements on deactivated NR SCG405

7.32.2.21Interruptions during RLM/BFD measurements on deactivated PScell405

7.33Maximum Transmit/Receive Timing Difference in Carrier Aggregation for sTTI and 1ms-TTI with 3 subframe HARQ processing405

7.33.1Introduction405

7.33.2Requirements405

7.34Void406

7.35Interruptions with SFTD measurements406

7.35.1Introduction406

7.35.2Requirements406

7.36Interruptions with NE-DC406

7.36.1Introduction406

7.36.2Requirements407

7.36.2.1Interruptions at transitions between active and non-active during DRX407

7.36.2.2Interruptions at transitions from non-DRX to DRX407

7.36.2.3Interruptions at SCell addition/release407

7.36.2.4Interruptions at SCell activation/deactivation407

7.36.2.5Interruptions during measurements on SCC408

7.36.2.5.1Interruptions during measurements on deactivated NR SCC408

7.36.2.5.2Interruptions during measurements on deactivated E-UTRA SCC408

7.36.2.5.3Interruptions during CQI measurements on dormant E-UTRA SCell408

7.36.2.5.4Interruptions during RRM measurements on dormant E-UTRA SCC408

7.36.2.6Interruptions at active BWP switching408

7.36.2.7Interruptions at SCell activation and deactivation of dormant SCell409

7.36.2.8Interruptions at SCell activation and deactivation of multiple dormant SCell409

7.36.2.9Interruptions at SCell hibernation409

7.36.2.10Interruptions at direct SCell activation and hibernation409

7.36.2.11Interruptions at NR SRS carrier based switching410

7.36.2.12Interruptions at NR SCell dormancy410

7.36.2.12.1Interruptions due to NR SCell dormancy switch410

7.36.2.12.2Interruptions due to CSI and RRM measurements during SCell dormancy411

7.36.2.13Interruption during E-UTRA measurement with autonomous gaps411

7.36.2.14Interruption during NR measurement with autonomous gaps411

7.36.2.15Interruptions at SRS carrier based switching412

7.36.2.16Interruptions due to NR SRS antenna port switching412

7.37Interruptions during NR measurement with autonomous gaps413

7.37.1Introduction413

7.37.2Requirements413

## 7.38 SCG Activation and Deactivation Delay413

7.38.1Introduction413

7.38.2SCG Activation Delay Requirement413

7.38.3SCG Deactivation Delay Requirement414

8UE Measurements Procedures in RRC_CONNECTED State415

8.1General Measurement Requirements415

8.1.1Introduction415

8.1.2Requirements415

8.1.2.1UE measurement capability415

8.1.2.1.1Monitoring of multiple layers using gaps423

8.1.2.1.1aMonitoring of multiple layers using gaps (Increased UE carrier monitoring)424

8.1.2.1.1bMonitoring of multiple layers using gaps (EN-DC)425

8.1.2.1.1cMonitoring of multiple layers using gaps (NE-DC)427

8.1.2.1.1dMonitoring of multiple layers using gaps (RedCap)428

8.1.2.1.2Network controlled small gap428

8.1.2.2E-UTRAN intra frequency measurements430

8.1.2.2.1E-UTRAN FDD intra frequency measurements430

8.1.2.2.2E-UTRAN TDD intra frequency measurements435

8.1.2.2.3E-UTRAN FDD intra frequency measurements with autonomous gaps439

8.1.2.2.4E-UTRAN TDD intra frequency measurements with autonomous gaps440

8.1.2.2.5E-UTRAN FDD intra-frequency measurements on carrier with FeMBMS/Unicast mixed cells441

8.1.2.3E-UTRAN inter frequency measurements441

8.1.2.3.1E-UTRAN FDD – FDD inter frequency measurements442

8.1.2.3.2E-UTRAN TDD – TDD inter frequency measurements447

8.1.2.3.3E-UTRAN TDD – FDD inter frequency measurements454

8.1.2.3.4E-UTRAN FDD – TDD inter frequency measurements454

8.1.2.3.5E-UTRAN FDD-FDD inter frequency measurements with autonomous gaps454

8.1.2.3.6E-UTRAN TDD-FDD inter frequency measurements using autonomous gaps455

8.1.2.3.7E-UTRAN TDD-TDD inter frequency measurements with autonomous gaps457

8.1.2.3.8E-UTRAN FDD-TDD inter frequency measurements using autonomous gaps458

8.1.2.3.9E-UTRAN FDD – FDD inter frequency measurements with FeMBMS/Unicast mixed cells459

8.1.2.3.10E-UTRAN TDD – FDD inter frequency measurements with FeMBMS/Unicast mixed cells466

8.1.2.4Inter RAT measurements466

8.1.2.4.1E-UTRAN FDD – UTRAN FDD measurements466

8.1.2.4.2E-UTRAN TDD – UTRAN FDD measurements471

8.1.2.4.3E-UTRAN TDD – UTRAN TDD measurements471

8.1.2.4.4E-UTRAN FDD – UTRAN TDD measurements475

8.1.2.4.5E-UTRAN FDD – GSM measurements475

8.1.2.4.6E-UTRAN TDD – GSM measurements480

8.1.2.4.7E-UTRAN FDD – UTRAN FDD measurements for SON480

8.1.2.4.8E-UTRAN TDD – UTRAN FDD measurements for SON482

8.1.2.4.9E-UTRAN FDD – cdma2000 1xRTT measurements482

8.1.2.4.9.1AE-UTRAN FDD – cdma2000 1xRTT measurements when no DRX is used482

8.1.2.4.10E-UTRAN TDD – cdma2000 1xRTT measurements483

8.1.2.4.11E-UTRAN FDD – HRPD measurements483

8.1.2.4.12E-UTRAN TDD – HRPD measurements483

8.1.2.4.13E-UTRAN TDD – UTRAN TDD measurements for SON483

8.1.2.4.14E-UTRAN FDD – UTRAN TDD measurements for SON485

8.1.2.4.15E-UTRAN FDD – cdma2000 1xRTT measurements for SON ANR485

8.1.2.4.16E-UTRAN TDD – cdma2000 1xRTT measurements for SON ANR485

8.1.2.4.17E-UTRAN FDD-UTRAN FDD measurements with autonomous gaps485

8.1.2.4.18E-UTRAN TDD-UTRAN FDD measurements with autonomous gaps486

8.1.2.4.19E-UTRAN FDD – WLAN measurements486

8.1.2.4.20E-UTRAN TDD – WLAN measurements488

8.1.2.4.21E-UTRAN FDD – NR measurements488

8.1.2.4.21AE-UTRAN FDD – NR measurements when CCA is used492

8.1.2.4.22E-UTRAN TDD – NR measurements496

8.1.2.4.22AE-UTRAN TDD – NR measurements when CCA is used496

8.1.2.4.23Void496

8.1.2.4.24Void496

8.1.2.4.25E-UTRAN FDD – NR SFTD Measurements496

8.1.2.4.26E-UTRAN TDD – NR SFTD Measurements498

## 8.1.2.4.27 E-UTRA FDD - NR measurements with autonomous gaps498

## 8.1.2.4.28 E-UTRA TDD - NR measurements with autonomous gaps499

8.1.2.4.29E-UTRAN FDD – NR measurements without measurement gap499

8.1.2.4.30E-UTRAN TDD – NR measurements without measurement gap504

8.1.2.5E-UTRAN OTDOA Intra-Frequency RSTD Measurements504

8.1.2.5.1E-UTRAN FDD Intra-Frequency OTDOA Measurements504

8.1.2.5.2E-UTRAN TDD Intra-Frequency OTDOA Measurements506

8.1.2.5.3E-UTRAN FDD Intra-Frequency OTDOA Measurements for UE Category 1bis507

8.1.2.5.4E-UTRAN TDD Intra-Frequency OTDOA Measurements for UE Category 1bis509

8.1.2.6.5Void511

8.1.2.6.6Void511

8.1.2.6.7Void511

8.1.2.6.8Void511

8.1.2.6E-UTRAN Inter-Frequency OTDOA Measurements511

8.1.2.6.1E-UTRAN FDD-FDD Inter-Frequency OTDOA Measurements511

8.1.2.6.2E-UTRAN TDD-FDD Inter-Frequency OTDOA Measurements513

8.1.2.6.3E-UTRAN TDD-TDD Inter-Frequency OTDOA Measurements515

8.1.2.6.4E-UTRAN FDD-TDD Inter-Frequency OTDOA Measurements516

8.1.2.6.5E-UTRAN FDD-FDD Inter-Frequency OTDOA Measurements for UE Category 1bis518

8.1.2.6.6E-UTRAN TDD-FDD Inter-Frequency OTDOA Measurements for UE Category 1bis520

8.1.2.6.7E-UTRAN TDD-TDD Inter-Frequency OTDOA Measurements for UE Category 1bis521

8.1.2.6.8E-UTRAN FDD-TDD Inter-Frequency OTDOA Measurements for UE Category 1bis523

8.1.2.7E-UTRAN E-CID Measurements525

8.1.2.7.1E-UTRAN FDD UE Rx-Tx Time Difference Measurements525

8.1.2.7.2E-UTRAN TDD UE Rx-Tx Time Difference Measurements526

8.1.2.7.3E-UTRAN FDD Intra-frequency E-CID RSRP and RSRQ Measurements528

8.1.2.7.4E-UTRAN TDD Intra-frequency E-CID RSRP and RSRQ Measurements528

8.1.2.8E-UTRAN intra-frequency measurements under time domain measurement resource restriction529

8.1.2.8.1E-UTRAN FDD intra-frequency measurements529

8.1.2.8.2E-UTRAN TDD intra-frequency measurements532

8.1.2.8.3E-UTRAN FDD intra-frequency measurements with CRS assistance information535

8.1.2.8.4E-UTRAN TDD intra-frequency measurements with CRS assistance infromation538

8.1.2.9E-UTRAN E-CID Measurements when Time Domain Measurement Resource Restriction Pattern is Configured542

8.1.2.9.1E-UTRAN FDD UE Rx-Tx Time Difference Measurements542

8.1.2.9.2E-UTRAN TDD UE Rx-Tx Time Difference Measurements542

8.1.2.9.3E-UTRAN FDD UE Rx-Tx Time Difference Measurements with CRS Assistance Information543

8.1.2.9.4E-UTRAN TDD UE Rx-Tx Time Difference Measurements with CRS Assistance Information543

8.1.2.10Void544

8.2Capabilities for Support of Event Triggering and Reporting Criteria544

8.2.1Introduction544

8.2.2Requirements544

8.3Measurements for E-UTRA carrier aggregation548

8.3.1Introduction548

8.3.2Measurements of the primary component carrier548

8.3.3Measurements of a secondary component carrier548

8.3.3.1Measurements of a secondary component carrier with active SCell548

8.3.3.2Measurements of a secondary component carrier with deactivated SCell549

8.3.3.2.1E-UTRAN secondary component carrier measurements when no common DRX is used549

8.3.3.2.2E-UTRAN secondary component carrier measurements when common DRX is used550

8.3.3.3Measurements on a secondary component carrier with FeMBMS/Unicast mixed cells and activated SCell552

8.3.3.4Measurements on a secondary component carrier with FeMBMS/Unicast mixed cells and deactivated SCell552

8.4OTDOA RSTD Measurements for E-UTRAN carrier aggregation552

8.4.1Introduction552

8.4.2Measurements on the primary component carrier553

8.4.3Measurements on a secondary component carrier554

8.4.4Measurements on both primary component carrier and a secondary component carrier554

8.4.5Measurements on different secondary component carriers555

8.5Measurements for UE category 0556

8.5.1Introduction556

## 8.5.2 Requirements557

## 8.5.2.1 E-UTRAN intra frequency measurements557

## 8.5.2.1.1 E-UTRAN FDD intra frequency measurements557

## 8.5.2.1.2 E-UTRAN intra frequency measurements for HD-FDD560

8.5.2.1.3E-UTRAN TDD intra frequency measurements562

8.5.2.1.4E-UTRAN FDD intra frequency measurements with autonomous gaps for UE category 0566

8.5.2.1.5E-UTRAN intra frequency measurements with autonomous gaps for HD-FDD UE category 0566

8.5.2.1.6E-UTRAN TDD intra frequency measurements with autonomous gaps for UE category 0567

8.6Discovery signal measurements568

8.6.1Introduction568

8.6.2Requirements for CRS based discovery signal measurements568

8.6.2.1E-UTRAN intra frequency measurements568

8.6.2.1.1E-UTRAN FDD intra frequency measurements568

8.6.2.1.2E-UTRAN TDD intra frequency measurements571

8.6.2.2E-UTRAN inter frequency measurements573

8.6.2.2.1E-UTRAN FDD – FDD inter-frequency measurements574

8.6.2.2.2E-UTRAN TDD – TDD inter frequency measurements576

8.6.2.2.3E-UTRAN TDD – FDD inter frequency measurements579

8.6.2.2.4E-UTRAN FDD – TDD inter frequency measurements579

8.6.3Requirements for CSI-RS based discovery signal measurements579

8.6.3.1E-UTRAN intra frequency measurements579

8.6.3.1.1E-UTRAN FDD intra frequency measurements580

8.6.3.1.2E-UTRAN TDD intra frequency measurements582

8.6.3.2E-UTRAN inter frequency measurements584

8.6.3.2.1E-UTRAN FDD – FDD inter frequency measurements585

8.6.3.2.2E-UTRAN TDD – TDD inter frequency measurements587

8.6.3.2.3E-UTRAN TDD – FDD inter frequency measurements590

8.6.3.2.4E-UTRAN FDD – TDD inter frequency measurements590

8.7Discovery signal measurements for E-UTRA carrier aggregation590

8.7.1Introduction590

8.7.2Requirements for CRS based discovery signal measurements for E-UTRA carrier aggregation591

8.7.2.1Measurements of the primary component carrier591

8.7.2.2Measurements of a secondary component carrier591

8.7.2.3Measurements of a secondary component carrier with active SCell591

8.7.2.4Measurements of a secondary component carrier with deactivated SCell591

8.7.2.4.1E-UTRAN secondary component carrier measurements when no common DRX is used591

8.7.2.4.2E-UTRAN secondary component carrier measurements when common DRX is used592

8.7.3Requirements for CSI-RS based discovery signal measurements for E-UTRA carrier aggregation594

8.7.3.1Measurements of the primary component carrier594

8.7.3.2Measurements of a secondary component carrier594

8.7.3.3Measurements of a secondary component carrier with active SCell594

8.7.3.4Measurements of a secondary component carrier with deactivated SCell594

8.7.3.4.1E-UTRAN secondary component carrier measurements when no common DRX is used594

8.7.3.4.2E-UTRAN secondary component carrier measurements when common DRX is used596

8.8Measurements for E-UTRA dual connectivity597

8.8.1Introduction597

8.8.2Intra-frequency measurements requirements on PCell597

8.8.3Intra-frequency measurements requirements on PSCell598

8.8.4Inter-frequency and inter-RAT measurement requirements598

8.8.5Intra-frequency measurements with autonomous gaps598

8.8.5.1Identification of a new CGI of E-UTRA cell with autonomous gaps598

8.8.5.2ECGI reporting delay599

8.8.6Inter-frequency measurements with autonomous gaps599

8.8.6.1Identification of a new CGI of E-UTRA cell with autonomous gaps599

8.8.6.2ECGI reporting delay600

8.8.7SSTD Measurements600

8.8.7.1Introduction600

8.8.7.2SSTD Measurement requirements600

8.8.7.3SSTD Measurement Reporting Delay601

8.8.8Intra-frequency measurements requirements on SCell601

8.9MBSFN Measurements601

8.9.1Introduction601

8.9.2MBSFN RSRP Measurements601

8.9.3MBSFN RSRQ Measurements602

8.9.4MCH BLER Measurements602

8.10Proximity-based Services602

8.10.1Introduction602

8.10.2Requirements602

8.10.2.1Initiation/Cease of SLSS transmissions with ProSe Direct Discovery602

8.10.2.2Initiation/Cease of SLSS transmissions with ProSe Direct Communication603

8.11Discovery Signal Measurements under Operation with Frame Structure 3604

8.11.1Introduction604

8.11.2CRS based discovery signal measurements604

8.11.2.1E-UTRAN intra-frequency measurements604

8.11.2.1.1Requirements604

8.11.2.1.1.1Requirements when no DRX is used604

8.11.2.1.1.1.1Measurement Reporting Requirements606

8.11.2.1.1.2Requirements when DRX is used607

8.11.2.1.1.2.1Measurement Reporting Requirements609

8.11.2.2E-UTRAN inter-frequency measurements610

8.11.2.2.1E-UTRAN FDD-FS3 inter-frequency measurements610

8.11.2.2.2E-UTRAN TDD – FS3 inter-frequency measurements614

8.11.3CSI-RS based discovery signal measurements614

8.11.3.1E-UTRAN intra-frequency measurements614

8.11.3.1.1Requirements614

8.11.3.1.1.1Requirements when no DRX is used614

8.11.3.1.1.1.1Measurement Reporting Requirements616

8.11.3.1.1.2Requirements when DRX is used616

8.11.3.1.1.2.1Measurement Reporting Requirements617

8.11.3.2E-UTRAN inter-frequency measurements618

8.11.3.2.1E-UTRAN FDD – FS3 inter-frequency measurements618

8.11.3.2.2E-UTRAN TDD – FS3 inter-frequency measurements622

8.11.4RSSI measurements622

8.11.4.1E-UTRAN intra-frequency measurements622

8.11.4.2E-UTRAN inter-frequency measurements622

8.11.5Channel occupancy measurements623

8.11.5.1E-UTRAN intra-frequency channel occupancy measurements623

8.11.5.2E-UTRAN inter-frequency channel occupancy measurements623

8.12Discovery Signal Measurements for E-UTRA Carrier Aggregation under Operation with Frame Structure 3623

8.12.1Introduction623

8.12.2CRS based discovery signal measurements for E-UTRA carrier aggregation623

8.12.2.1Introduction623

8.12.2.2Measurements of a secondary component carrier623

8.12.2.3Measurements of a secondary component carrier with active SCell623

8.12.2.4Measurements of a secondary component carrier with deactivated SCell624

8.12.2.4.1E-UTRAN secondary component carrier measurements when no common DRX is used624

8.12.2.4.2E-UTRAN secondary component carrier measurements when common DRX is used626

8.12.3Requirements for CSI-RS based discovery signal measurements for E-UTRA carrier aggregation629

8.12.3.1Introduction629

8.12.3.2Measurements of a secondary component carrier629

8.12.3.3Measurements of a secondary component carrier with active SCell629

8.12.3.4Measurements of a secondary component carrier with deactivated SCell629

8.12.3.4.1E-UTRAN secondary component carrier measurements when no common DRX is used629

8.12.3.4.2E-UTRAN secondary component carrier measurements when common DRX is used631

8.13Measurements for UE Category M1633

8.13.1Introduction633

8.13.2Requirements for UE category M1 with CE mode A633

8.13.2.1E-UTRAN intra frequency measurements by UE category M1 with CE mode A634

8.13.2.1.1E-UTRAN FDD intra frequency measurements634

8.13.2.1.2E-UTRAN intra frequency measurements for HD-FDD639

8.13.2.1.3E-UTRAN TDD intra frequency measurements641

8.13.2.2Void645

8.13.2.3E-UTRAN OTDOA Intra-Frequency RSTD Measurements for Cat-M1 UE in CEModeA645

8.13.2.3.1E-UTRAN FDD Intra-Frequency OTDOA Measurements645

8.13.2.3.2E-UTRAN TDD Intra-Frequency OTDOA Measurements648

8.13.2.3.3E-UTRAN HD-FDD Intra-Frequency OTDOA Measurements650

8.13.2.4E-UTRAN OTDOA Inter-Frequency RSTD Measurements for Cat-M1 UE in CEModeA651

8.13.2.4.1E-UTRAN FDD Inter-Frequency OTDOA Measurements651

8.13.2.4.2E-UTRAN TDD Inter-Frequency OTDOA Measurements653

8.13.2.4.3E-UTRAN HD-FDD Inter-Frequency OTDOA Measurements655

8.13.2.5E-UTRAN E-CID Measurements Requirements for UE category M1 with CE mode A656

8.13.2.5.1Intra-frequency FDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeA656

8.13.2.5.2Intra-frequency HD-FDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeA656

8.13.2.5.3Intra-frequency TDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeA657

8.13.2.5.4Inter-frequency FDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeA657

8.13.2.5.5Inter-frequency HD-FDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeA657

8.13.2.5.6Inter-frequency TDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeA658

8.13.2.5.7E-UTRAN FDD UE Rx-Tx Time Difference Measurements for UE category M1 in CEModeA658

8.13.2.5.8E-UTRAN TDD UE Rx-Tx Time Difference Measurements for UE category M1 in CEModeA659

8.13.2.5.9E-UTRAN HD-FDD UE Rx-Tx Time Difference Measurements for UE category M1 in CEModeA660

8.13.2.6E-UTRAN inter frequency measurements by UE category M1 with CE mode A660

8.13.2.6.1E-UTRAN FDD - FDD inter frequency measurements660

8.13.2.6.2E-UTRAN inter-frequency measurements for HD-FDD665

8.13.2.6.3E-UTRAN TDD inter frequency measurements667

8.13.2.7Maximum allowed layers for multiple monitoring for UE category M1 with CE mode A671

8.13.2.8Channel quality report for UE Category M1 in connected mode with CE mode A671

8.13.3Requirements for UE category M1 with CE mode B672

8.13.3.1E-UTRAN intra frequency measurements by UE category M1 with CE mode B672

8.13.3.1.1E-UTRAN FDD intra frequency measurements673

8.13.3.1.2E-UTRAN intra frequency measurements for HD-FDD677

8.13.3.1.3E-UTRAN TDD intra frequency measurements680

8.13.3.1.4E-UTRAN FDD intra frequency measurements with autonomous gaps for UE category M1 with CE mode B685

8.13.3.1.5E-UTRAN intra frequency measurements with autonomous gaps for HD-FDD UE category M1 with CE mode B686

8.13.3.1.6E-UTRAN TDD intra frequency measurements with autonomous gaps for UE category M1 with CE mode B686

8.13.3.2Void687

8.13.3.3E-UTRAN OTDOA Intra-Frequency RSTD Measurements for Cat-M1 UE in CEModeB687

8.13.3.3.1E-UTRAN FDD Intra-Frequency OTDOA Measurements687

8.13.3.3.2E-UTRAN TDD Intra-Frequency OTDOA Measurements690

8.13.3.3.3E-UTRAN HD-FDD Intra-Frequency OTDOA Measurements692

8.13.3.4E-UTRAN E-CID Measurements Requirements for UE category M1 with CE mode B693

8.13.3.4.1Intra-frequency E-CID FDD RSRP and RSRQ Measurements for Cat-M1 UE in CEModeB693

8.13.3.4.2Intra-frequency HD-FDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeB693

8.13.3.4.3Intra-frequency TDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeB693

8.13.3.4.4Inter-frequency E-CID FDD RSRP and RSRQ Measurements for Cat-M1 UE in CEModeB694

8.13.3.4.5Inter-frequency HD-FDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeB694

8.13.3.4.6Inter-frequency TDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeB695

8.13.3.5E-UTRAN inter frequency measurements by UE category M1 with CE Mode B695

8.13.3.5.1E-UTRAN FDD - FDD inter frequency measurements695

## 8.13.3.5.2 E-UTRAN inter-frequency measurements for HD-FDD700

8.13.3.5.3E-UTRAN TDD inter frequency measurements702

8.13.3.6Maximum allowed layers for multiple monitoring for UE category M1 with CE mode B707

8.13.3.7E-UTRAN OTDOA Inter-Frequency RSTD Measurements for Cat-M1 UE in CEModeB707

8.13.3.7.1E-UTRAN FDD Inter-Frequency OTDOA Measurements707

8.13.3.7.2E-UTRAN TDD Inter-Frequency OTDOA Measurements709

8.13.3.7.3E-UTRAN HD-FDD Inter-Frequency OTDOA Measurements712

8.13.3.8Channel quality report for UE Category M1 in connected mode with CE mode B712

8.13AMeasurements for UE Category M1 for Satellite Access713

8.13A.1Introduction713

8.13A.2Requirements for UE category M1 with CE mode A713

8.13A.2.1E-UTRAN intra frequency measurements by UE category M1 with CE mode A714

8.13A.2.1.1E-UTRAN FDD intra frequency measurements714

8.13A.2.1.1.1E-UTRAN intra frequency measurements when no DRX is used714

8.13A.2.1.1.2E-UTRAN intra frequency measurements when DRX is used716

8.13A.2.1.2E-UTRAN intra frequency measurements for HD-FDD718

8.13A.2.1.2.1E-UTRAN intra frequency measurements when no DRX is used718

8.13A.2.1.2.2E-UTRAN intra frequency measurements when DRX is used718

8.13A.2.2E-UTRAN inter frequency measurements by UE category M1 with CE mode A720

8.13A.2.2.1E-UTRAN FDD - FDD inter frequency measurements720

8.13A.2.2.1.1E-UTRAN FDD - FDD inter frequency measurements when no DRX is used720

8.13A.2.2.1.2E-UTRAN inter frequency measurements when DRX is used722

8.13A.2.2.2E-UTRAN inter-frequency measurements for HD-FDD724

8.13A.2.2.2.1E-UTRAN inter-frequency measurements when no DRX is used724

8.13A.2.2.2.2E-UTRAN inter frequency measurements when DRX is used724

8.13A.2.3Maximum allowed layers for multiple monitoring for UE category M1 with CE mode A726

8.13A.2.4Channel quality report for UE Category M1 in connected mode with CE mode A727

8.13A.3Requirements for UE category M1 with CE mode B727

8.13A.3.1E-UTRAN intra frequency measurements by UE category M1 with CE mode B728

8.13A.3.1.1E-UTRAN FDD intra frequency measurements728

8.13A.3.1.1.1E-UTRAN intra frequency measurements when no DRX is used728

8.13A.3.1.1.2E-UTRAN intra frequency measurements when DRX is used730

8.13A.3.1.2E-UTRAN intra frequency measurements for HD-FDD732

8.13A.3.1.2.1E-UTRAN intra frequency measurements when no DRX is used732

8.13A.3.1.2.2E-UTRAN intra frequency measurements when DRX is used733

8.13A.3.2E-UTRAN inter frequency measurements by UE category M1 with CE Mode B735

8.13A.3.2.1E-UTRAN FDD - FDD inter frequency measurements735

8.13A.3.2.1.1E-UTRAN FDD - FDD inter frequency measurements when no DRX is used735

8.13A.3.2.1.2E-UTRAN inter frequency measurements when DRX is used737

8.13A.3.2.2E-UTRAN inter-frequency measurements for HD-FDD739

8.13A.3.2.2.1E-UTRAN inter-frequency measurements when no DRX is used739

8.13A.3.2.2.2E-UTRAN inter frequency measurements when DRX is used739

8.13A.3.3Maximum allowed layers for multiple monitoring for UE category M1 with CE mode B741

8.13A.3.4Channel quality report for UE Category M1 in connected mode with CE mode B742

8.14Measurements for UE category NB1742

8.14.1Introduction742

8.14.2NB-IoT intra frequency measurements under normal coverage742

8.14.2.1NB-IoT intra frequency measurements when no DRX is used742

8.14.2.2NB-IoT intra frequency measurements when DRX is used742

8.14.3NB-IoT intra frequency measurements under enhanced coverage743

8.14.3.1NB-IoT intra frequency measurements when no DRX is used743

8.14.3.2NB-IoT intra frequency measurements when DRX is used743

8.14.4Connected mode channel quality report for UE Category NB1743

8.14.5Connected mode channel quality report for UE Category NB2 supporting 16QAM743

8.14.6NB-IoT neighbour cell measurements744

8.14.6.1Introduction744

8.14.6.2Requirements744

8.14.6.3Intra-frequency neighbour cell measurements744

8.14.6.4Inter-frequency neighbour cell measurements745

## 8.14.6.5 Requirements for monitoring multiple carriers746

8.14AMeasurements for UE category NB-IoT for Satellite Access746

8.14A.1Introduction746

8.14A.2NB-IoT intra frequency measurements under normal coverage747

8.14A.2.1NB-IoT intra frequency measurements when no DRX is used747

8.14A.2.2NB-IoT intra frequency measurements when DRX is used747

8.14A.3NB-IoT intra frequency measurements under enhanced coverage747

8.14A.3.1NB-IoT intra frequency measurements when no DRX is used747

8.14A.3.2NB-IoT intra frequency measurements when DRX is used747

8.14A.4Connected mode channel quality report for UE Category NB1747

8.14A.5Reserved748

8.14A.6NB-IoT neighbour cell measurements748

8.14A.6.1Introduction748

8.14A.6.2Requirements748

8.14BMeasurements for UE category NB-IoT for frame structure type 1 for NTN-TDD750

8.14B.1Introduction750

8.14B.2NB-IoT intra frequency measurements under normal coverage751

8.14B.2.1NB-IoT intra frequency measurements when no DRX is used751

8.14B.2.2NB-IoT intra frequency measurements when DRX is used751

8.14B.4Connected mode channel quality report for UE Category NB1751

8.14B.6NB-IoT neighbour cell measurements752

8.14B.6.1Introduction752

8.14B.6.2Requirements752

8.14B.6.3Intra-frequency neighbour cell measurements752

8.14B.6.4Inter-frequency neighbour cell measurements753

8.14B.6.5Requirements for monitoring multiple carriers754

8.15Void754

8.16Measurements for UE Category M2754

8.16.1Introduction754

8.16.2Requirements for UE category M2 with CE mode A755

8.16.2.1E-UTRAN FDD UE Rx-Tx Time Difference Measurements for UE category M2 in CEModeA755

8.16.2.1.1UE Rx-Tx Measurement Reporting Delay755

8.16.2.2E-UTRAN TDD UE Rx-Tx Time Difference Measurements for UE category M2 in CEModeA756

8.16.2.2.1UE Rx-Tx Measurement Reporting Delay756

8.16.2.2aE-UTRAN HD-FDD UE Rx-Tx Time Difference Measurements for UE category M2 in CEModeA757

8.16.2.2a.1UE Rx-Tx Measurement Reporting Delay757

8.16.2.3E-UTRAN OTDOA Intra-Frequency RSTD Measurements for Cat-M2 UE in CEModeA757

8.16.2.3.1E-UTRAN FDD Intra-Frequency OTDOA Measurements757

8.16.2.3.2E-UTRAN TDD Intra-Frequency OTDOA Measurements760

8.16.2.3.3E-UTRAN HD-FDD Intra-Frequency OTDOA Measurements763

8.16.2.4E-UTRAN OTDOA Inter-Frequency RSTD Measurements for Cat-M2 UE in CEModeA763

8.16.2.4.1E-UTRAN FDD Inter-Frequency OTDOA Measurements763

8.16.2.4.2E-UTRAN TDD Inter-Frequency OTDOA Measurements765

8.16.2.4.3E-UTRAN HD-FDD Inter-Frequency OTDOA Measurements768

8.16.3Requirements for UE category M2 with CE mode B768

8.16.3.1E-UTRAN OTDOA Intra-Frequency RSTD Measurements for Cat-M2 UE in CEModeB768

8.16.3.1.1E-UTRAN FDD Intra-Frequency OTDOA Measurements768

8.16.3.1.2E-UTRAN TDD Intra-Frequency OTDOA Measurements771

8.16.3.1.3E-UTRAN HD-FDD Intra-Frequency OTDOA Measurements774

8.16.3.2E-UTRAN OTDOA Inter-Frequency RSTD Measurements for Cat-M2 UE in CEModeB774

8.16.3.2.1E-UTRAN FDD Inter-Frequency OTDOA Measurements774

8.16.3.2.2E-UTRAN TDD Inter-Frequency OTDOA Measurements776

8.16.3.2.3E-UTRAN HD-FDD Inter-Frequency OTDOA Measurements779

8.17Measurements for E-UTRA – NR Dual Connectivity779

8.17.1Introduction779

8.17.1.1Measurement Gap Sharing779

8.17.1AIntrafrequency Measurements780

8.17.2SFTD Measurements780

8.17.2.1Introduction780

8.17.2.2SFTD Measurement requirements780

8.17.2.2.aSFTD Measurement requirements with CCA on target frequency781

8.17.2.3SFTD Measurement Reporting Delay782

8.17.3E-UTRA Inter-frequency Measurements when Configured with E-UTRA-NR Dual Connectivity Operation782

8.17.3.1Introduction782

8.17.3.2E-UTRAN FDD inter frequency measurements783

8.17.3.2.1E-UTRAN FDD inter frequency measurements when no DRX is used783

8.17.3.2.2E-UTRAN FDD inter frequency measurements when DRX is used784

8.17.3.3E-UTRAN TDD inter frequency measurements786

8.17.3.3.1E-UTRAN TDD inter frequency measurements when no DRX is used786

8.17.3.3.2E-UTRAN TDD inter frequency measurements when DRX is used788

8.17.4E-UTRA Inter-RAT NR Measurements when Configured with E-UTRA-NR Dual Connectivity Operation790

8.17.4.1E-UTRAN FDD – NR measurements when configured with E-UTRA-NR Dual connectivity790

8.17.4.1.1NR Inter-RAT cell identification790

8.17.4.1.2NR Inter-RAT measurement792

8.17.4.1.3NR Inter-RAT measurement reporting792

8.17.4.2E-UTRAN TDD – NR measurements when configured with E-UTRA-NR Dual connectivity793

8.17.4AE-UTRA Inter-RAT NR Measurements when CCA is used when Configured with E-UTRA-NR Dual Connectivity Operation793

8.17.4A.1E-UTRAN FDD – NR measurements when configured with E-UTRA-NR Dual connectivity793

8.17.4A.1.1NR Inter-RAT cell identification794

8.17.4A.1.2NR Inter-RAT measurement795

8.17.4A.1.3NR Inter-RAT measurement reporting796

8.17.4A.1.4NR inter-RAT RSSI measurements797

8.17.4A.1.5NR inter-RAT channel occupancy measurements797

8.17.4A.2E-UTRAN TDD – NR measurements when configured with E-UTRA-NR Dual connectivity798

8.17.5E-UTRAN FDD – UTRAN FDD measurements when Configured with E-UTRA-NR Dual Connectivity798

8.17.5.1Introduction798

8.17.5.2E-UTRAN FDD – UTRAN FDD measurements when no DRX is used798

8.17.5.2.1Identification of a new UTRA FDD cell798

8.17.5.2.2Enhanced UTRA FDD cell identification requirements798

8.17.5.2.3UE UTRA FDD CPICH measurement capability799

8.17.5.2.4Periodic Reporting799

8.17.5.2.5Event Triggered Reporting799

8.17.5.2.6Event-triggered Periodic Reporting800

8.17.5.3E-UTRAN FDD – UTRAN FDD measurements when DRX is used800

8.17.5.3.1Periodic Reporting801

8.17.5.3.2Event Triggered Reporting801

8.17.5.3.3Event-triggered Periodic Reporting802

8.17.6E-UTRAN TDD – UTRAN FDD measurements when Configured with E-UTRA-NR Dual Connectivity802

8.17.7E-UTRAN FDD – UTRAN FDD measurements for SON when Configured with E-UTRA-NR Dual Connectivity802

8.17.7.1Introduction802

8.17.7.2Identification of a new UTRA FDD cell for SON802

8.17.7.2.1Requirements when no DRX is used802

8.17.7.2.2Requirements when DRX is used803

8.17.7.2.3Reporting Delay803

8.17.8E-UTRAN TDD – UTRAN FDD measurements for SON when Configured with E-UTRA-NR Dual Connectivity804

8.17.9E-UTRAN TDD – UTRAN TDD measurements when Configured with E-UTRA-NR Dual Connectivity804

8.17.9.1Introduction804

8.17.9.2E-UTRAN FDD – UTRAN TDD measurements when no DRX is used804

8.17.9.2.1Identification of a new UTRA FDD cell804

8.17.9.2.2Enhanced UTRA TDD cell identification requirements804

8.17.9.2.3UE UTRA TDD P-CCPCH RSCP measurement capability805

8.17.9.2.4Periodic Reporting805

8.17.9.2.5Event Triggered Reporting805

8.17.9.2.6Event-triggered Periodic Reporting806

8.17.9.3E-UTRAN TDD – UTRAN TDD measurements when DRX is used806

8.17.9.3.1Periodic Reporting807

8.17.9.3.2Event Triggered Reporting807

8.17.9.3.3Event-triggered Periodic Reporting807

8.17.10E-UTRAN FDD – UTRAN TDD measurements when Configured with E-UTRA-NR Dual Connectivity808

8.17.11E-UTRAN TDD – UTRAN TDD measurements for SON when Configured with E-UTRA-NR Dual Connectivity808

8.17.11.1Introduction808

8.17.11.2Identification of a new UTRA TDD cell for SON808

8.17.11.2.1Requirements when no DRX is used808

8.17.11.2.2Requirements when DRX is used808

8.17.11.2.3Reporting Delay809

8.17.12E-UTRAN FDD – UTRAN TDD measurements for SON when Configured with E-UTRA-NR Dual Connectivity809

8.17.13E-UTRAN FDD – GSM measurements when Configured with E-UTRA-NR Dual Connectivity810

8.17.13.1Introduction810

8.17.13.2E-UTRAN FDD – GSM measurements when no DRX is used810

8.17.13.2.1GSM carrier RSSI810

8.17.13.2.2BSIC verification810

8.17.13.2.3Enhanced BSIC verification812

8.17.13.2.4Periodic Reporting812

8.17.13.2.5Event Triggered Reporting812

8.17.13.2.6Event-triggered Periodic Reporting813

8.17.13.3E-UTRAN FDD – GSM measurements when DRX is used813

8.17.13.3.1GSM carrier RSSI813

8.17.13.3.2BSIC verification813

8.17.13.3.3Periodic Reporting815

8.17.13.3.4Event Triggered Reporting815

8.17.13.3.5Event-triggered Periodic Reporting815

8.17.14E-UTRAN TDD – GSM measurements when Configured with E-UTRA-NR Dual Connectivity815

8.17.15E-UTRAN Inter-Frequency RSTD measurements when configured with E-UTRA-NR Dual Connectivity815

8.17.15.1E-UTRAN FDD-FDD Inter-Frequency RSTD measurements when configured with E-UTRA-NR Dual Connectivity815

8.17.15.1.1RSTD Measurement Reporting Delay816

8.17.15.2E-UTRAN TDD-FDD Inter-Frequency RSTD measurements when configured with E-UTRA-NR Dual Connectivity816

8.17.15.2.1RSTD Measurement Reporting Delay816

8.17.15.3E-UTRAN TDD-TDD Inter-Frequency RSTD measurements when configured with E-UTRA-NR Dual Connectivity816

8.17.15.3.1RSTD Measurement Reporting Delay817

8.17.15.4E-UTRAN FDD-TDD Inter-Frequency RSTD measurements when configured with E-UTRA-NR Dual Connectivity817

8.17.15.4.1RSTD Measurement Reporting Delay817

8.17.16E-UTRAN intra-frequency measurement with autonomous gaps when configured with E-UTRA-NR Dual Connectivity818

8.17.16.1Introduction818

8.17.16.2E-UTRAN FDD intra frequency measurements with autonomous gaps818

8.17.16.3E-UTRAN TDD intra frequency measurements with autonomous gaps818

8.17.17E-UTRAN inter-frequency measurement with autonomous gaps when configured with E-UTRA-NR Dual Connectivity818

8.17.17.1Introduction818

8.17.17.2E-UTRAN FDD-FDD inter frequency measurements with autonomous gaps818

8.17.17.3E-UTRAN TDD-FDD inter frequency measurements using autonomous gaps818

8.17.17.4E-UTRAN TDD-TDD inter frequency measurements with autonomous gaps818

8.17.17.5E-UTRAN FDD-TDD inter frequency measurements using autonomous gaps818

8.17.18E-UTRA FDD - NR CGI measurements with autonomous gaps818

8.17.19E-UTRA TDD - NR CGI measurements with autonomous gaps818

8.18Measurements for non-BL/CE UE818

8.18.1Introduction818

8.18.2Requirements for non-BL/CE UE with CE Mode B819

8.18.2.1E-UTRAN intra frequency measurements819

8.18.2.1.1E-UTRAN FDD intra frequency measurements with autonomous gaps for non-BL/CE with CE Mode B819

8.18.2.1.2E-UTRAN intra frequency measurements with autonomous gaps for HD-FDD non-BL/CE with CE Mode B819

8.18.2.1.3E-UTRAN TDD intra frequency measurements with autonomous gaps for non-BL/CE with CE Mode B820

8.19Measurements for NR – E-UTRA Dual Connectivity821

8.19.1Introduction821

8.19.2Intra-frequency Measurements821

8.19.3Inter-frequency Measurements821

8.19.4Void821

8.19.5Intra-frequency E-CID Measurements821

8.19.6Intra-frequency measurements with autonomous gaps822

8.19.6.1Introduction822

8.19.6.2E-UTRAN FDD intra frequency measurements with autonomous gaps822

8.19.6.3E-UTRAN TDD intra frequency measurements with autonomous gaps822

8.19.7Inter-frequency measurements with autonomous gaps822

8.19.7.1Introduction822

8.19.7.2E-UTRAN FDD-FDD inter frequency measurements with autonomous gaps822

8.19.7.3E-UTRAN TDD-FDD inter frequency measurements with autonomous gaps822

8.19.7.4E-UTRAN TDD-TDD inter frequency measurements with autonomous gaps822

8.19.7.5E-UTRAN FDD-TDD inter frequency measurements with autonomous gaps822

8.20Inter-RAT NR Measurements for RedCap UE822

8.20.1Introduction822

8.20.2E-UTRAN FDD – NR measurements822

8.20.2.1Identification of a new NR cell822

8.20.2.2Periodic Reporting826

8.20.2.3Event Triggered Reporting826

8.20.2.4Event-triggered Periodic Reporting826

8.20.3E-UTRAN TDD – NR measurements826

9Measurements performance requirements for UE827

9.1E-UTRAN measurements827

9.1.1Introduction827

9.1.2Intra-frequency RSRP Accuracy Requirements827

9.1.2.1Absolute RSRP Accuracy827

9.1.2.2Relative Accuracy of RSRP828

9.1.2.3Absolute RSRP Accuracy under Time Domain Measurement Resource Restriction829

9.1.2.4Relative Accuracy of RSRP under Time Domain Measurement Resource Restriction829

9.1.2.5Absolute RSRP Accuracy under Time Domain Measurement Resource Restriction with CRS assistance information830

9.1.2.6Relative Accuracy of RSRP under Time Domain Measurement Resource Restriction with CRS assistance information831

9.1.2.7Absolute RSRP Accuracy for UE Category 1bis832

9.1.2.8Relative Accuracy of RSRP for UE Category 1bis833

9.1.2AIntra-frequency RSRP Accuracy Requirements in High Doppler Conditions834

9.1.2A.1Absolute RSRP Accuracy in high Doppler conditions834

9.1.2A.2Relative Accuracy of RSRP in high Doppler conditions834

9.1.2BIntra-frequency RSRP Accuracy requirements for CA Idle Mode Measurements835

9.1.2B.1Introduction835

9.1.2B.2Intra-frequency Absolute RSRP Accuracy for CA Idle Mode Measurements835

9.1.3Inter-frequency RSRP Accuracy Requirements836

9.1.3.1Absolute RSRP Accuracy836

9.1.3.2Relative Accuracy of RSRP837

9.1.3.3Absolute RSRP Accuracy for UE Category 1bis838

9.1.3.4Relative Accuracy of RSRP for UE Category 1bis838

9.1.3AInter-frequency RSRP Accuracy Requirements in High Doppler Conditions839

9.1.3A.1Absolute RSRP Accuracy in high Doppler conditions839

9.1.3A.2Relative Accuracy of RSRP in high Doppler conditions840

9.1.3BInter-frequency RSRP Accuracy requirements for CA Idle Mode Measurements841

9.1.3B.1Introduction841

9.1.3B.2Inter-frequency Absolute RSRP Accuracy for Overlapping Carrier841

9.1.3B.3Inter-frequency Absolute RSRP Accuracy for Overlapping and Non-overlapping Carrier841

9.1.4RSRP Measurement Report Mapping842

9.1.5Intra-frequency RSRQ Accuracy Requirements842

9.1.5.1Absolute RSRQ Accuracy842

9.1.5.2Absolute RSRQ Accuracy under Time Domain Measurement Resource Restriction843

9.1.5.3Absolute RSRQ Accuracy under Time Domain Measurement Resource Restriction with CRS assistance information844

9.1.5.4Absolute WB-RSRQ Accuracy845

9.1.5.5Absolute RSRQ Accuracy for UE Category 1bis846

9.1.5AIntra-frequency RSRQ Accuracy Requirements in High Doppler Conditions847

9.1.5A.1Absolute RSRQ Accuracy in high Doppler conditions847

9.1.5BIntra-frequency RSRQ Accuracy requirements for CA Idle Mode Measurements847

9.1.5B.1Introduction847

9.1.5B.2Intra-frequency Absolute RSRQ Accuracy for CA Idle Mode Measurements847

9.1.6Inter-frequency RSRQ Accuracy Requirements848

9.1.6.1Absolute RSRQ Accuracy848

9.1.6.2Relative Accuracy of RSRQ849

9.1.6.3Absolute WB-RSRQ Accuracy850

9.1.6.4Relative WB-RSRQ Accuracy850

9.1.6.5Absolute RSRQ Accuracy for UE Category 1bis851

9.1.6.6Relative Accuracy of RSRQ for UE Category 1bis852

9.1.6AInter-frequency RSRQ Accuracy Requirements in High Doppler Conditions852

9.1.6A.1Absolute RSRQ Accuracy in high Doppler conditions852

9.1.6A.2Relative Accuracy of RSRQ in high Doppler conditions853

9.1.6BInter-frequency absolute RSRQ Accuracy requirements for CA Idle Mode Measurements854

9.1.6B.1Introduction854

9.1.6B.2Inter-frequency Absolute RSRQ Accuracy for Overlapping Carrier854

9.1.6B.3Inter-frequency absolute RSRQ Accuracy for Overlapping and Non-overlapping Carrier854

9.1.7RSRQ Measurement Report Mapping855

9.1.8Power Headroom855

9.1.8.1Period856

9.1.8.2Reporting Delay856

9.1.8.3Void856

9.1.8.4Report Mapping856

9.1.8APower Headroom for UE category M1 for satellite access856

9.1.8A.1Period857

9.1.8A.2Reporting Delay857

9.1.8A.3Void857

9.1.8A.4Report Mapping857

9.1.9UE Rx – Tx time difference857

9.1.9.1Measurement Requirement857

9.1.9.2Measurement Report mapping858

9.1.9.3Measurement Requirement under Time Domain Measurement Resource Restriction859

9.1.9.4Measurement Requirement when Time Domain Measurement Resource Restriction Pattern is Configured with CRS Assistance Information860

9.1.10Reference Signal Time Difference (RSTD)861

9.1.10.1Intra-Frequency Accuracy Requirement861

9.1.10.2Inter-Frequency Accuracy Requirement862

9.1.10.3RSTD Measurement Report Mapping864

9.1.10.4Higher-Resolution RSTD Measurement Report Mapping864

9.1.10.5Intra-Frequency Accuracy Requirement for UE Category 1bis865

9.1.10.6Inter-Frequency Accuracy Requirement for UE Category 1bis866

9.1.11Carrier aggregation measurement accuracy867

9.1.11.1Primary component carrier accuracy requirement868

9.1.11.2Secondary component carrier accuracy requirement868

9.1.11.3Primary and secondary component carrier relative accuracy requirement868

9.1.11.4Secondary component carrier relative accuracy requirement868

9.1.12Reference Signal Time Difference (RSTD) Measurement Accuracy Requirements for Carrier Aggregation868

9.1.13Measurement accuracy for UE category 0869

9.1.13.1Intra-frequency Absolute RSRP Accuracy for UE category 0869

9.1.13.2Intra-frequency Relative Accuracy of RSRP for UE category 0869

9.1.13.3Intra-frequency Absolute RSRQ Accuracy for UE category 0870

9.1.14Accuracy requirements for Discovery Signal Measurements871

9.1.14.1Introduction871

9.1.14.2RSRP measurements in discovery signal occasions871

9.1.14.3CSI-RSRP measurements in discovery signal occasions871

9.1.14.3.1Intra-frequency CSI-RSRP measurements871

9.1.14.3.1.1Absolute CSI-RSRP measurement requirements871

9.1.14.3.1.2Relative CSI-RSRP measurement requirements872

9.1.14.3.2Inter-frequency CSI-RSRP measurements873

9.1.14.3.2.1Absolute CSI-RSRP measurement requirements873

9.1.14.3.2.2Relative CSI-RSRP measurement requirements873

9.1.14.3.3CSI-RSRP measurement report mapping874

9.1.14.4RSRQ measurements in discovery signal occasions874

9.1.15Discovery signal measurements accuracy for E-UTRAN carrier aggregation874

9.1.15.1Requirements for CRS based discovery signal measurements accuracy for E-UTRAN carrier aggregation875

9.1.15.1.1Primary component carrier accuracy requirement875

9.1.15.1.2Secondary component carrier accuracy requirement875

9.1.15.1.3Primary and secondary component carrier relative accuracy requirement875

9.1.15.1.4Secondary component carrier relative accuracy requirement875

9.1.15.2Requirements for CSI-RS based discovery signal measurements accuracy for E-UTRAN carrier aggregation875

9.1.15.2.1Primary component carrier accuracy requirement875

9.1.15.2.2Secondary component carrier accuracy requirement875

9.1.15.2.3Primary and secondary component carrier relative accuracy requirement875

9.1.15.2.4Secondary component carrier relative accuracy requirement875

9.1.16Accuracy requirements for RSRQ measurement on all OFDM symbols876

9.1.17RS-SINR Measurements876

9.1.17.1Measurement Report Mapping876

9.1.17.2Intra-frequency RS-SINR Measurement Accuracy Requirements877

9.1.17.2.1Absolute RS-SINR Measurement Accuracy Requirements877

9.1.17.3Inter-frequency RS-SINR Measurement Accuracy Requirements877

9.1.17.3.1Absolute RS-SINR Measurement Accuracy Requirements877

9.1.17.3.2Relative RS-SINR Measurement Accuracy Requirements878

9.1.18Accuracy Requirements for Measurements under Operation with Frame Structure 3879

9.1.18.1Introduction879

9.1.18.2RSRP measurements879

9.1.18.2.1RSRP measurement report mapping879

9.1.18.2.2Inter-frequency absolute RSRP measurement accuracy requirements879

9.1.18.2.3Inter-frequency relative RSRP measurement accuracy requirements880

9.1.18.2.4Intra-frequency absolute RSRP measurement accuracy requirements880

9.1.18.2.5Intra-frequency relative RSRP measurement accuracy requirements881

9.1.18.3RSRQ measurements881

9.1.18.3.1RSRQ measurement report mapping881

9.1.18.3.2Inter-frequency absolute RSRQ measurement accuracy requirements881

9.1.18.3.3Inter-frequency relative RSRQ measurement accuracy requirements882

9.1.18.3.4Intra-frequency absolute RSRQ measurement accuracy requirements882

9.1.18.4CSI-RSRP measurements883

9.1.18.4.1CSI-RSRP measurement report mapping883

9.1.18.4.2Inter-frequency absolute CSI-RSRP measurement accuracy requirements883

9.1.18.4.3Inter-frequency relative CSI-RSRP measurement accuracy requirements883

9.1.18.4.4Intra-frequency absolute CSI-RSRP measurement accuracy requirements884

9.1.18.4.5Intra-frequency relative CSI-RSRP measurement accuracy requirements884

9.1.18.5RSSI measurements885

9.1.18.5.1RSSI measurement report mapping885

9.1.18.5.2Intra-frequency absolute RSSI measurement accuracy requirements885

9.1.18.5.3Inter-frequency absolute RSSI measurement accuracy requirements886

9.1.18.6Channel occupancy measurements886

9.1.18.6.1Intra-frequency channel occupancy measurement accuracy requirements886

9.1.18.6.2Inter-frequency channel occupancy measurement accuracy requirements886

9.1.19Accuracy Requirements for Carrier Aggregation for Measurements under Operation with Frame Structure 3887

9.1.19.1Introduction887

9.1.19.2Accuracy requirements for measurements on SCC887

9.1.19.3Relative accuracy requirements for measurements on different SCCs887

9.1.19.4Relative accuracy requirements for measurements on SCC and PCC887

9.1.20SFN and Subframe Time Difference (SSTD)888

9.1.20.1SSTD Accuracy Requirement888

9.1.20.2SSTD Measurement Report Mapping888

9.1.21Measurement accuracy for UE category M1889

9.1.21.1Intra-frequency Absolute RSRP Accuracy for UE category M1 with CE mode A889

9.1.21.2Intra-frequency Relative Accuracy of RSRP for UE category M1 with CE mode A891

9.1.21.3Intra-frequency Absolute RSRP Accuracy for UE category M1 with CE mode B892

9.1.21.4Intra-frequency Relative Accuracy of RSRP for UE category M1 with CE mode B894

9.1.21.5RSRP Measurement Report Mapping895

9.1.21.6Intra-frequency Absolute Accuracy of RSRQ for UE category M1 with CE mode A895

9.1.21.7Intra-frequency Absolute Accuracy of RSRQ for UE category M1 with CE mode B896

9.1.21.8RSRQ Measurement Report Mapping897

9.1.21.9Inter-frequency Absolute RSRP Accuracy for UE category M1 with CE mode A897

9.1.21.10Inter-frequency Relative Accuracy of RSRP for UE category M1 with CE mode A898

9.1.21.11Inter-frequency Absolute RSRP Accuracy for UE category M1 with CE mode B899

9.1.21.12Inter-frequency Relative Accuracy of RSRP for UE category M1 with CE mode B900

## 9.1.21.13 Inter-frequency Absolute Accuracy of RSRQ for UE category M1 in CE mode A901

9.1.21.14Inter-frequency Relative Accuracy of RSRQ for UE category M1 in CE mode A902

## 9.1.21.15 Inter-frequency Absolute Accuracy of RSRQ for UE category M1 in CE mode B903

9.1.21.16Inter-frequency Relative Accuracy of RSRQ for UE category M1 in CE mode B904

9.1.21.17Inter-Frequency RSTD Accuracy Requirement for UE catergory M1 in CE mode A905

9.1.21.18Inter-Frequency RSTD Accuracy Requirement for UE catergory M1 in CE mode B906

9.1.21.19UE RX-TX time difference Accuracy Requirement for Cat-M1907

9.1.21.20Intra-Frequency RSTD Accuracy Requirement for UE catergory M1 in CE mode A908

9.1.21.21Intra-Frequency RSTD Accuracy Requirement for UE catergory M1 in CE mode B911

9.1.21.22Downlink Channel Report Mapping for UE Category M1914

9.1.21.23Downlink Channel Quality Measurement Accuracy for UE Category M1 with CE Mode A914

9.1.21.24Downlink Channel Quality Measurement Accuracy for UE Category M1 with CE Mode B917

9.1.21AMeasurement accuracy for UE category M1 for satellite access918

9.1.21A.1Intra-frequency Absolute RSRP Accuracy for UE category M1 with CE mode A919

9.1.21A.2Intra-frequency Relative Accuracy of RSRP for UE category M1 with CE mode A920

9.1.21A.3Intra-frequency Absolute RSRP Accuracy for UE category M1 with CE mode B921

9.1.21A.4Intra-frequency Relative Accuracy of RSRP for UE category M1 with CE mode B923

9.1.21A.5RSRP Measurement Report Mapping924

9.1.21A.6Intra-frequency Absolute Accuracy of RSRQ for UE category M1 with CE mode A924

9.1.21A.7Intra-frequency Absolute Accuracy of RSRQ for UE category M1 with CE mode B925

9.1.21A.8RSRQ Measurement Report Mapping926

9.1.21A.9Inter-frequency Absolute RSRP Accuracy for UE category M1 with CE mode A926

9.1.21A.10Inter-frequency Relative Accuracy of RSRP for UE category M1 with CE mode A927

9.1.21A.11Inter-frequency Absolute RSRP Accuracy for UE category M1 with CE mode B928

9.1.21A.12Inter-frequency Relative Accuracy of RSRP for UE category M1 with CE mode B929

9.1.21A.13Inter-frequency Absolute Accuracy of RSRQ for UE category M1 in CE mode A930

9.1.21A.14Inter-frequency Relative Accuracy of RSRQ for UE category M1 in CE mode A931

9.1.21A.15Inter-frequency Absolute Accuracy of RSRQ for UE category M1 in CE mode B932

9.1.21A.16Inter-frequency Relative Accuracy of RSRQ for UE category M1 in CE mode B933

9.1.21A.17Downlink Channel Report Mapping for UE Category M1934

9.1.21A.18Downlink Channel Quality Measurement Accuracy for UE Category M1 with CE Mode A934

9.1.21A.19Downlink Channel Quality Measurement Accuracy for UE Category M1 with CE Mode B936

9.1.22Measurement accuracy for UE Category NB1937

9.1.22.1Intra-frequency Absolute NRSRP Accuracy for UE Category NB1937

9.1.22.2Void938

9.1.22.3Intra-frequency Absolute NRSRQ Accuracy for UE Category NB1938

9.1.22.4Void939

9.1.22.5Inter-frequency Absolute NRSRP Accuracy for UE Category NB1939

9.1.22.6Void940

9.1.22.7Inter-frequency Absolute NRSRQ Accuracy for UE Category NB1940

9.1.22.8Void941

9.1.22.9NRSRP Measurement Report Mapping941

9.1.22.10Intra-Frequency RSTD Accuracy Requirement for NB1 for normal coverage941

9.1.22.11Inter-Frequency RSTD Accuracy Requirement for NB1 for normal coverage942

9.1.22.12Intra-Frequency RSTD Accuracy Requirement for NB1 for enhanced coverage943

9.1.22.13Inter-Frequency RSTD Accuracy Requirement for NB1 for enhanced coverage944

9.1.22.14NRSRQ Measurement Report Mapping945

9.1.22.15MSG3-based Measurement Report Mapping for UE Category NB1946

9.1.22.16Downlink Channel Quality Measurement Accuracy for UE Category NB1946

9.1.22.17Channel quality reporting for UE Category NB2 with 16-QAM947

9.1.22AMeasurement accuracy for UE Category NB1 for satellite access947

9.1.22A.1Intra-frequency Absolute NRSRP Accuracy for UE Category NB1947

9.1.22A.2Intra-frequency Absolute NRSRQ Accuracy for UE Category NB1948

9.1.22A.3Inter-frequency Absolute NRSRP Accuracy for UE Category NB1950

9.1.22A.4Inter-frequency Absolute NRSRQ Accuracy for UE Category NB1951

9.1.22A.5NRSRP Measurement Report Mapping952

9.1.22A.6NRSRQ Measurement Report Mapping952

9.1.22A.7MSG3-based Measurement Report Mapping for UE Category NB1952

9.1.22A.8Downlink Channel Quality Measurement Accuracy for UE Category NB1952

9.1.23Power Headroom for UE Category NB1953

9.1.23.1Period953

9.1.23.2Reporting Delay953

9.1.23.3Report Mapping for UE Category NB1954

9.1.23.3.1Void955

9.1.23.3.2Void955

9.1.23.4Report Mapping for UE Category NB1 for UE Power Class 6955

9.1.23APower Headroom for UE Category NB1 for Satellite Access956

9.1.23A.1Period956

9.1.23A.2Reporting Delay956

9.1.23A.3Report Mapping for UE Category NB1 for Satellite Access957

9.1.23A.3.1Void957

9.1.23A.3.2Void957

9.1.23A.4Report Mapping for UE Category NB1 for UE Power Class 6 for Satellite Access957

9.1.24Void957

9.1.25Measurement accuracy for UE category M2957

9.1.25.1Inter-Frequency RSTD Accuracy Requirement for UE catergory M2 in CE mode A957

9.1.25.2Inter-Frequency RSTD Accuracy Requirement for UE catergory M2 in CE mode B958

9.1.25.3UE RX-TX time difference Accuracy Requirement for Cat-M2959

9.1.25.4Intra-Frequency RSTD Accuracy Requirement for UE catergory M2 in CE mode A960

9.1.25.5Intra-Frequency RSTD Accuracy Requirement for UE catergory M2 in CE mode B962

9.1.26Measurement Accuracy for non-BL CE UE963

9.1.26.1Intra-frequency Absolute Accuracy of RSRP for non-BL CE UE in CE mode A964

9.1.26.2Intra-frequency Relative Accuracy of RSRP for non-BL CE UE in CE mode A966

9.1.26.3Intra-frequency Absolute Accuracy of RSRP for non-BL CE UE in CE mode B966

9.1.26.4Intra-frequency Relative Accuracy of RSRP for non-BL CE UE in CE mode B968

9.1.26.5RSRP Measurement Report Mapping969

9.1.26.6Intra-frequency Absolute Accuracy of RSRQ for non-BL CE UE in CE mode A969

9.1.26.7Intra-frequency Absolute Accuracy of RSRQ for non-BL CE UE in CE mode B969

9.1.26.8RSRQ Measurement Report Mapping970

9.1.26.9Inter-frequency Absolute Accuracy of RSRP for non-BL CE UE in CE mode A970

9.1.26.10Inter-frequency Relative Accuracy of RSRP for non-BL CE UE in CE mode A971

9.1.26.11Inter-frequency Absolute Accuracy of RSRP for non-BL CE UE in CE mode B972

9.1.26.12Inter-frequency Relative Accuracy of RSRP for non-BL CE UE in CE mode B973

9.1.26.13Inter-frequency Absolute Accuracy of RSRQ for non-BL CE UE in CE mode A974

9.1.26.14Inter-frequency Relative Accuracy of RSRQ for non-BL CE UE in CE mode A974

9.1.26.15Inter-frequency Absolute Accuracy of RSRQ for non-BL CE UE in CE mode B974

9.1.26.16Inter-frequency Relative Accuracy of RSRQ for non-BL CE UE in CE mode B975

9.1.27SFN and frame Timing Difference (SFTD)976

9.1.27.1SFTD Accuracy Requirement976

9.1.28SFN and Frame Timing Difference (SFTD) under CCA978

9.1.28.1SFTD Accuracy Requirement under CCA978

9.2UTRAN FDD Measurements979

9.2.1UTRAN FDD CPICH RSCP979

9.2.2Void980

9.2.3UTRAN FDD CPICH Ec/No980

9.3UTRAN TDD Measurements980

9.3.1UTRAN TDD P-CCPCH RSCP981

9.3.2Void981

9.3.3Void981

9.4GSM Measurements981

9.4.1GSM carrier RSSI981

9.5CDMA2000 1x RTT Measurements981

9.5.1CDMA2000 1x RTT Pilot Strength981

9.6PCMAX,c982

9.6.1Report Mapping982

## 9.6.2 Estimation Period982

9.6.3Reporting Delay982

9.7IEEE802.11 Measurements982

9.7.1WLAN RSSI982

9.7.2WLAN RSSI Measurement Report Mapping982

9.8MBSFN Measurements983

9.8.1Introduction983

9.8.2MBSFN RSRP983

9.8.2.1Absolute MBSFN RSRP measurement accuracy requirements983

9.8.2.2MBSFN RSRP measurement report mapping984

9.8.2.3MBSFN RSRP measurement report mapping for 7.5 kHz subcarrier spacing984

9.8.2.4MBSFN RSRP measurement report mapping for 1.25 kHz subcarrier spacing985

9.8.2.5MBSFN RSRP measurement report mapping for 2.5 kHz subcarrier spacing985

9.8.2.6MBSFN RSRP measurement report mapping for 370.37Hz subcarrier spacing985

9.8.3MBSFN RSRQ986

9.8.3.1Absolute MBSFN RSRQ measurement accuracy requirements986

9.8.3.2MBSFN RSRQ measurement report mapping986

9.8.3.3MBSFN RSRQ measurement report mapping for 7.5 kHz subcarrier spacing987

9.8.3.4MBSFN RSRQ measurement report mapping for 1.25 kHz subcarrier spacing987

9.8.3.5MBSFN RSRQ measurement report mapping for 2.5 kHz subcarrier spacing987

9.8.3.6MBSFN RSRQ measurement report mapping for 370.37 kHz subcarrier spacing988

9.8.4MCH BLER988

9.8.4.1Measurement report mapping for MCH BLER988

9.8.4.2Measurement report mapping for MCH Block Number989

9.9ProSe Measurements990

9.9.1Introduction990

9.9.2Intra-Frequency S-RSRP Measurement Accuracy Requirements990

9.9.2.1Absolute S-RSRP Accuracy990

9.9.2.2Relative Accuracy of S-RSRP991

9.9.3Intra-Frequency SD-RSRP Measurement Accuracy Requirements992

9.9.3.1Absolute SD-RSRP Accuracy992

9.9.3.2Relative Accuracy of SD-RSRP992

9.10V2X Measurements993

9.10.1Introduction993

9.10.2Intra-Frequency S-RSRP Measurement Accuracy Requirements993

9.10.2.1Absolute S-RSRP Accuracy993

9.10.2.2Relative Accuracy of S-RSRP994

9.10.3PSSCH-RSRP Measurement Accuracy Requirements994

9.10.3.1Intra-frequency Absolute PSSCH-RSRP Accuracy994

9.10.4S-RSSI Measurement Accuracy Requirements995

9.10.4.1Intra-frequency absolute S-RSSI measurement accuracy requirements995

## 9.10.4.2 Intra-frequency relative S-RSSI measurement accuracy requirements995

9.11NR Measurements996

9.11.1NR SS-RSRP Measurements996

9.11.1ANR SS-RSRP Measurements for DC Idle Mode Measurements996

9.11.2NR SS-RSRQ Measurements997

9.11.2ANR SS-RSRQ Measurements for DC Idle Mode Measurements997

9.11.3NR SS-SINR Measurements997

9.11.4NR SS-RSRP Measurements under CCA998

9.11.5NR SS-RSRQ Measurements under CCA998

9.11.6NR SS-SINR Measurements under CCA998

9.11.7NR RSSI Measurements under CCA998

9.11.8NR Channel Occupancy Measurements under CCA999

10Measurements Performance Requirements for E-UTRAN999

10.1Received Interference Power999

10.1.1Absolute accuracy requirement999

10.1.2Relative accuracy requirement999

10.1.3Received Interference Power measurement report mapping1000

10.2Angle of Arrival (AOA)1000

10.2.1Range/mapping1000

10.3Timing Advance (TADV)1000

10.3.1Report mapping1000

11ProSe Requirements in Any Cell Selection state1001

11.1Introduction1001

11.2UE Transmit Timing for ProSe in Any Cell Selection State1001

11.2.1Introduction1001

11.2.2ProSe UE transmission timing1001

11.3Initiation/Cease of SLSS Transmissions1002

11.3.1Introduction1002

11.3.2Requirements1002

11.4Measurements for ProSe in Any Cell Selection State1002

11.4.1Introduction1002

11.4.2Requirements1002

11.4.2.1E-UTRA FDD1002

11.4.2.2E-UTRA TDD1003

11.5Selection / Reselection of ProSe Synchronization Reference1003

11.5.1Introduction1003

11.5.2Selection/Reselection to intra-frequency SyncRef UE1003

11.5.2.1Introduction1003

11.5.2.2Requirements1003

11.6Void1004

11.7Selection / Reselection of ProSe relay UE1004

11.7.1Introduction1004

11.7.2Selection / Reselection of intra-frequency ProSe relay UE1004

12V2V Sidelink Communication Requirements for V2V Operation on Dedicated V2V Carrier1004

12.1Introduction1004

12.2Transmit Timing1005

12.2.1GNSS as timing reference1005

12.3Interruption1005

12.4Reliability of GNSS signal1005

13V2X Requirements1005

13.1Introduction1005

13.2UE Transmit Timing1006

13.2.1Introduction1006

13.2.2GNSS as synchronization reference source1006

13.2.3Serving cell/PCell as synchronization reference source1006

13.2.4SyncRef UE as synchronization reference source1006

13.3Initiation/Cease of SLSS Transmissions1006

13.3.1Introduction1006

13.3.1.1Initiation/Cease of SLSS transmissions with Serving cell / PCell as synchronization reference source1006

13.3.1.2Initiation/Cease of SLSS transmissions with GNSS as synchronization reference source1007

13.3.1.3Initiation/Cease of SLSS transmissions with SyncRef UE as synchronization reference source1007

13.4Selection / Reselection of V2X Synchronization Reference Source1008

13.5Autonomous Resource Selection/Reselection measurements1009

13.5.1Introduction1009

13.5.2PSSCH-RSRP measurements1009

13.5.3S-RSSI measurements1009

13.6Congestion Control measurements1009

13.7Interruption1009

13.7.1Interruptions to WAN due to V2X Sidelink Communication1009

13.7.2V2X Sidelink Communication Dropping due to synchronization reference source change1009

13.7.3Interruptions to WAN due to V2X Carrier Aggregation1010

13.7.4Interruptions to WAN due to NR V2X sidelink communication1010

13.8Reliability of GNSS signal1010

13.9Component Carrier Addition and Release Delay for V2X Sidelink Carrier Aggregation1011

13.10Selection / Reselection of V2X Synchronization Reference Source for V2X Carrier Aggregation1011

Annex A (normative):Test Cases1012

A.1Purpose of annex1012

A.2Requirement classification for statistical testing1012

A.2.1Types of requirements in TS 36.1331012

A.2.1.1Time and delay requirements on UE higher layer actions1012

A.2.1.2Measurements of power levels, relative powers and time1012

A.2.1.3Implementation requirements1013

A.2.1.4Physical layer timing requirements1013

A.3RRM test configurations1014

A.3.1Reference Measurement Channels1014

A.3.1.1PDSCH1014

A.3.1.1.1FDD1014

A.3.1.1.2TDD1019

A.3.1.1.3FDD for UE category 01022

A.3.1.1.4HD-FDD for UE category 01023

A.3.1.1.5TDD for UE category 01024

A.3.1.1.6Frame Structure 31025

A.3.1.2PCFICH/PDCCH/PHICH1026

A.3.1.2.1FDD1026

A.3.1.2.2TDD1026

A.3.1.2.3HD-FDD for UE category 01027

A.3.1.2.4FS 31027

A.3.1.3MPDCCH Reference Channels for Cat-M1 UEs1027

A.3.1.3.1FDD in CEModeA1028

A.3.1.3.2HD-FDD in CEModeA1028

A.3.1.3.3TDD in CEModeA1029

A.3.1.3.4FDD in CEModeB1029

A.3.1.3.5HD-FDD in CEModeB1030

A.3.1.3.6TDD in CEModeB1030

A.3.1.4PDSCH Reference Channel for Cat-M1 UEs1031

A.3.1.4.1FDD in CEModeA1031

A.3.1.4.2HD-FDD in CEModeA1032

A.3.1.4.3TDD in CEModeA1033

A.3.1.4.4FDD in CEModeB1034

A.3.1.4.5HD-FDD in CEModeB1035

A.3.1.4.6TDD in CEModeB1035

A.3.1.5NPDSCH Reference Channel for UE category NB11036

A.3.1.5.1HD-FDD in-band operation1036

A.3.1.5.2Void1037

A.3.1.5.3HD-FDD standalone operation1037

A.3.1.5.4Void1038

A.3.1.5.5HD-FDD guard band operation1038

A.3.1.5.6Void1039

A.3.1.5.7TDD in-band operation1039

A.3.1.5.8TDD standalone operation1039

A.3.1.5.9TDD guard band operation1040

A.3.1.5.10NTN-TDD standalone operation1040

A.3.1.6NPDCCH Reference Channel for UE category NB11041

A.3.1.6.1In-band operation1041

A.3.1.6.2Void1042

A.3.1.6.3Standalone operation1042

A.3.1.6.4Void1042

A.3.1.6.5Guard band operation1042

A.3.1.6.6Void1043

A.3.2OFDMA Channel Noise Generator (OCNG)1043

A.3.2.1OCNG Patterns for FDD1043

A.3.2.1.1OCNG FDD pattern 1: outer resource blocks allocation in 10 MHz1043

A.3.2.1.2OCNG FDD pattern 2: full bandwidth allocation in 10 MHz1044

A.3.2.1.3OCNG FDD pattern 3: outer resource blocks allocation in 1.4 MHz1045

A.3.2.1.4OCNG FDD pattern 4: full bandwidth allocation in 1.4 MHz1045

A.3.2.1.5OCNG FDD pattern 5: outer resource blocks allocation in 10 MHz (without MBSFN)1046

A.3.2.1.6OCNG FDD pattern 6: full bandwidth allocation in 10 MHz (without MBSFN)1047

A.3.2.1.7OCNG FDD pattern 7: full bandwidth allocation in 1.4 MHz (without MBSFN)1047

A.3.2.1.8OCNG FDD pattern 8: outer resource blocks allocation in 10 MHz for MBSFN ABS1047

A.3.2.1.9OCNG FDD pattern 9: full bandwidth allocation in 10 MHz for MBSFN ABS1048

A.3.2.1.10OCNG FDD pattern 10: outer resource blocks allocation in 10 MHz with user data in every subframe (without MBSFN)1049

A.3.2.1.11OCNG FDD pattern 11: outer resource blocks allocation in 20 MHz1049

A.3.2.1.12OCNG FDD pattern 12: full bandwidth allocation in 20 MHz1050

A.3.2.1.13OCNG FDD pattern 13: outer resource blocks allocation in 20 MHz (without MBSFN)1050

A.3.2.1.14OCNG FDD pattern 14: full bandwidth allocation in 20 MHz (without MBSFN)1051

A.3.2.1.15OCNG FDD pattern 15: outer resource blocks allocation in 5 MHz1051

A.3.2.1.16OCNG FDD pattern 16: full bandwidth allocation in 5 MHz1052

A.3.2.1.17OCNG FDD pattern 17: outer resource blocks allocation in 20 MHz with user data in every subframe (without MBSFN)1052

A.3.2.1.18OCNG FDD pattern 18: outer resource blocks allocation in 5 MHz (without MBSFN)1053

A.3.2.1.19OCNG FDD pattern 19: full bandwidth allocation in 5 MHz (without MBSFN)1053

A.3.2.1.20OCNG FDD pattern 20: outer resource blocks allocation in 5 MHz with user data in every subframe (without MBSFN)1054

A.3.2.1.21OCNG FDD pattern 21: Generic resource blocks allocation (without MBSFN)1054

A.3.2.1.22OCNG FDD pattern 22: Generic resource blocks allocation in 5MHz (without MBSFN)1055

A.3.2.2OCNG Patterns for TDD1055

A.3.2.2.1OCNG TDD pattern 1: outer resource blocks allocation in 10 MHz1056

A.3.2.2.2OCNG TDD pattern 2: full bandwidth allocation in 10 MHz1056

A.3.2.2.3OCNG TDD pattern 3: outer resource blocks allocation in 1.4 MHz1057

A.3.2.2.4OCNG TDD pattern 4: full bandwidth allocation in 1.4 MHz1057

A.3.2.2.5OCNG TDD pattern 5: outer resource blocks allocation in 10 MHz for MBSFN ABS1058

A.3.2.2.6OCNG TDD pattern 6: full bandwidth allocation in 10 MHz for MBSFN ABS1059

A.3.2.2.7OCNG TDD pattern 7: outer resource blocks allocation in 20 MHz1060

A.3.2.2.8OCNG TDD pattern 8: full bandwidth allocation in 20 MHz1061

A.3.2.2.9OCNG TDD pattern 9: outer resource blocks allocation in 5 MHz1061

A.3.2.2.10OCNG TDD pattern 10: full bandwidth allocation in 5 MHz1062

A.3.2.2.11OCNG TDD pattern 11: Generic resource blocks allocation (without MBSFN)1063

A.3.2.3OCNG Patterns for Narrowband IoT1063

A.3.2.3.1Narrowband IoT OCNG FDD pattern 1: In-band NB-IoT in 10 MHz EUTRAN cell1065

A.3.2.3.2Narrowband IoT OCNG FDD pattern 2: guard band NB-IoT in 10 MHz EUTRAN cell1066

A.3.2.3.3Narrowband IoT OCNG FDD pattern 3: standalone NB-IoT1066

A.3.2.3.4Narrowband IoT OCNG FDD pattern 4: In-band NB-IoT in 5 MHz EUTRAN cell1067

A.3.2.3.5Narrowband IoT OCNG FDD pattern 5: guard band NB-IoT in 5 MHz EUTRAN cell1068

A.3.2.3.6Narrowband IoT OCNG TDD pattern 1: In-band NB-IoT in 10 MHz EUTRAN cell1069

A.3.2.3.7Narrowband IoT OCNG TDD pattern 2: guard band NB-IoT in 10 MHz EUTRAN cell1071

A.3.2.3.8Narrowband IoT OCNG TDD pattern 3: standalone NB-IoT1071

A.3.2.3.9Narrowband IoT OCNG FDD pattern 6: In-band NB-IoT in 5 MHz NTN NR cell1072

A.3.2.3.10Narrowband IoT OCNG NTN TDD pattern 4: standalone NB-IoT1073

A.3.2.4OCNG Patterns for V2X sidelink1074

A.3.2.4.1V2X sidelink OCNG TDD pattern 1: outer resource blocks allocation in 10 MHz1074

A.3.2.4.2V2X sidelink OCNG TDD pattern 2: outer resource blocks allocation in 10 MHz1075

A.3.3Reference DRX Configurations1075

A.3.4ABS Transmission Configurations1076

A.3.4.1Non-MBSFN ABS Transmission Configurations1076

A.3.4.1.1Non-MBSFN ABS Transmission, 1x2 antenna with PBCH1076

A.3.4.1.2Non-MBSFN ABS Transmission, 2x2 antenna without PBCH1076

A.3.4.2MBSFN ABS Transmission Configurations1077

A.3.4.2.1MBSFN ABS Transmission, 1x2 antenna1077

A.3.4.2.2MBSFN ABS Transmission, 2x2 antenna1078

A.3.5Impact of Reference Sensitivity Degradation with Carrier Aggregation on Test Cases1078

A.3.5.1Impact of Reference Sensitivity Degradation due to Insertion Loss1078

A.3.6Carrier Aggregation Test Cases with Different Channel Bandwidth Combinations1079

A.3.6.1Introduction1079

A.3.7Test Cases with Different Channel Bandwidths1079

A.3.7.1Introduction1079

A.3.7.2Principle of testing1079

A.3.8Antenna Configuration1079

A.3.8.1Antenna connection for 4 Rx capable UEs1079

A.3.8.1.1 Introduction1079

A.3.8.1.2 Principle of testing1079

A.3.8.1.2.1 Single carrier tests1079

A.3.8.1.2.2Carrier aggregation and Dual connectivity tests1080

A.3.8.1.2.3Antenna connection for bands where 2RX is supported1081

A.3.8.1.2.4Antenna connection for bands where 4RX is supported1081

A.3.8.2Antenna connection for 8 Rx capable UEs1081

A.3.8.2.1Introduction1081

A.3.8.2.2Principle of testing1081

A.3.8.2.2.1Single carrier tests1081

A.3.8.2.2.2Carrier aggregation and Dual connectivity tests1082

A.3.8.2.2.3Antenna connection for bands where 2RX is supported1082

A.3.8.2.2.4Antenna connection for bands where 4RX is supported1082

A.3.8.2.2.5Antenna connection for bands where 8RX is supported1082

A.3.9Carrier Aggregation Test Cases with Different Duplex Modes1082

A.3.9.1Introduction1082

A.3.9.2Principle of testing1082

A.3.10Carrier Aggregation Test Cases with Different CA Configurations1083

A.3.10.1Introduction1083

A.3.10.2Principle of testing1083

A.3.11Test Cases for Synchronous and Asynchronous Dual Connectivity1083

A.3.11.1Introduction1083

A.3.11.2Principle of Testing1083

A.3.12Proximity-based Services1083

A.3.12.1Introduction1083

A.3.12.2Reference DRX configurations for ProSe tests1083

A.3.12.3Test Cases with Different Channel Bandwidths1084

A.3.12.3.1Introduction1084

A.3.12.3.2Principle of testing1084

A.3.12.4Reference resource pool configurations for ProSe Direct Discovery1084

A.3.12.5Reference resource pool configurations for ProSe Direct Communication1091

A.3.12.6Reference Measurement Channels for ProSe Direct Discovery1094

A.3.12.6.1FDD1094

A.3.12.7Reference measurement channels for ProSe Direct Communication1094

A.3.12.7.1FDD1094

A.3.12.8ProSe Receive Traffic Generator1095

A.3.12.8.1ProSe Direct Communication Receive Traffic Generator for FDD1095

A.3.12.8.2ProSe Direct Discovery Receive Traffic Generator for FDD1095

A.3.13Time Offset between Cells1096

A.3.13.1Introduction1096

A.3.13.2Definition1096

A.3.14Carrier Aggregation under operation with Frame Structure 3 Test Cases with Different Duplex Modes1096

A.3.14.1Introduction1096

A.3.14.2Principle of testing1096

A.3.15Dual connectivity test cases with different combination of duplex mode1096

A.3.15.1Introduction1096

A.3.15.2Principle of testing1096

A.3.16Reference PRACH Configurations1097

A.3.17Listen before talk model1097

A.3.17.1Introduction1097

A.3.17.2Definition1097

A.3.18Reference NPRACH Configurations1098

A.3.19Dual connectivity test cases with different bandwidth combinations1100

A.3.19.1Introduction1100

A.3.19.2Principle of testing1100

A.3.20Category M1 UE Test Cases1101

A.3.20.1Introduction1101

A.3.20.2Principle of Cat-M1 UE Testing1101

A.3.20.3Principle of Cat-M1 UE testing for inter-frequency RSTD measurement period requirements with measurement gaps1102

A.3.21V2V Sidelink Communication on Dedicated V2V Carrier1103

A.3.21.1Introduction1103

A.3.21.2Reference resource pool configurations for V2V Sidelink Communication1103

A.3.21.3Reference measurement channels for V2V Sidelink Communication1104

A.3.22Category 1bis UE Test Cases1105

A.3.22.1Introduction1105

A.3.22.2Principle of Category 1bis UE Testing1105

A.3.23Category NB2 UE Test Cases1109

A.3.23.1Introduction1109

A.3.23.2Principle of Category NB2 UE Testing1109

A.3.24V2X sidelink communication1112

A.3.24.1Introduction1112

A.3.24.2Reference resource pool configurations for V2X Sidelink Communication1113

A.3.24.3Reference measurement channels for V2X Sidelink Communication1117

A.3.25Category M2 UE Test Cases1118

A.3.25.1Introduction1118

A.3.25.2Principle of Cat-M2 UE Testing1118

A.3.25.3Principle of Cat-M2 UE testing for inter-frequency RSTD measurement period requirements with measurement gaps1119

A.3.26sTTI and processing time reduction test cases with different sTTI/processing time reduction scheme1120

A.3.26.1Introduction1120

A.3.26.2Principle of testing1120

A.3.27LTE INACTIVE Cell Re-selection Test Cases1120

A.3.27.1Introduction1120

A.3.27.2Principle of INACTIVE cell re-selection Testing1120

A.3.28Testing related to Satellite access1120

A.3.28.1Introduction1120

A.3.28.2Principle of testing GSO and NGSO scenarios1120

A.3.28.2Principle of testing different RRM requirements1121

A.3.28.3Principle of testing different ephemeris formats1125

A.3.28.4General setup for SIB31/SIB-31-NB1125

A.3.28.5Satellite specific parameters configuration1125

A.3.28.5.1Satellite specific configuration for serving cell1125

A.3.28.5.2Satellite specific configuration for neighbour cell1125

A.4E-UTRAN RRC_IDLE state1126

A.4.2Cell Re-Selection1126

A.4.2.1E-UTRAN FDD – FDD Intra frequency case1126

A.4.2.1.1Test Purpose and Environment1126

A.4.2.1.2Test Requirements1128

A.4.2.2E-UTRAN TDD – TDD Intra frequency case1129

A.4.2.2.1Test Purpose and Environment1129

A.4.2.2.2Test Requirements1130

A.4.2.3E-UTRAN FDD – FDD Inter frequency case1131

A.4.2.3.1Test Purpose and Environment1131

A.4.2.3.2Test Requirements1132

A.4.2.4E-UTRAN FDD – TDD Inter frequency case1133

A.4.2.4.1Test Purpose and Environment1133

A.4.2.4.2Test Requirements1134

A.4.2.5E-UTRAN TDD – FDD Inter frequency case1135

A.4.2.5.1Test Purpose and Environment1135

A.4.2.5.2Test Requirements1136

A.4.2.6E-UTRAN TDD – TDD: Inter frequency case1137

A.4.2.6.1Test Purpose and Environment1137

A.4.2.6.2Test Requirements1138

A.4.2.7E-UTRAN FDD – FDD Inter frequency case in the existence of non-allowed CSG cell1139

A.4.2.7.1Test Purpose and Environment1139

A.4.2.7.2Test Requirements1140

A.4.2.8E-UTRAN TDD – TDD Inter frequency case in the existence of non-allowed CSG cell1141

A.4.2.8.1Test Purpose and Environment1141

A.4.2.8.2Test Requirements1142

A.4.2.9E-UTRAN FDD – FDD Intra frequency case for 5MHz bandwidth1143

A.4.2.9.1Test Purpose and Environment1143

A.4.2.9.2Test Requirements1143

A.4.2.10E-UTRAN FDD – FDD reselection using an increased number of carriers1143

A.4.2.10.1Test Purpose and Environment1143

A.4.2.10.2Test Requirements1147

A.4.2.11E-UTRAN TDD – TDD reselection using an increased number of carriers1147

A.4.2.11.1Test Purpose and Environment1147

A.4.2.11.2Test Requirements1151

A.4.2.12E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage1151

A.4.2.12.1Test Purpose and Environment1151

A.4.2.12.2Test Requirements1153

A.4.2.13E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in normal coverage1154

A.4.2.13.1Test Purpose and Environment1154

A.4.2.13.2Test Requirements1155

A.4.2.14E-UTRAN TDD – TDD Intra frequency case for Cat-M1 UE in normal coverage1156

A.4.2.14.1Test Purpose and Environment1156

A.4.2.14.2Test Requirements1157

A.4.2.15 E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in enhanced coverage1158

A.4.2.15.1Test Purpose and Environment1158

A.4.2.15.2Test Requirements1159

A.4.2.16 E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in enhanced coverage1160

A.4.2.16.1Test Purpose and Environment1160

A.4.2.16.2Test Requirements1161

A.4.2.17 E-UTRAN TDD – TDD Intra frequency case for Cat-M1 UE in enhanced coverage1162

A.4.2.17.1Test Purpose and Environment1162

A.4.2.17.2Test Requirements1163

A.4.2.18 HD – FDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage1164

A.4.2.18.1Test Purpose and Environment1164

A.4.2.18.2Test Requirements1166

A.4.2.19HD – FDD Intra frequency case for UE Category NB1 In-Band mode in enhanced coverage1167

A.4.2.19.1Test Purpose and Environment1167

A.4.2.19.2Test Requirements1169

A.4.2.20E-UTRAN FDD – FDD Intra frequency case for UE Category 1bis1170

A.4.2.20.1Test Purpose and Environment1170

A.4.2.20.2Test Requirements1171

A.4.2.21E-UTRAN TDD – TDD Intra frequency case for UE Category 1bis1172

A.4.2.21.1Test Purpose and Environment1172

A.4.2.21.2Test Requirements1173

A.4.2.22E-UTRAN FDD – FDD Intra frequency case for UE configured with highSpeedEnhancedMeasFlag1174

A.4.2.22.1Test Purpose and Environment1174

A.4.2.22.2Test Requirements1175

A.4.2.23E-UTRAN TDD – TDD Intra frequency case for UE configured with highSpeedEnhancedMeasFlag1176

A.4.2.23.1Test Purpose and Environment1176

A.4.2.23.2Test Requirements1177

A.4.2.24HD – FDD Inter frequency case for UE Category NB1 In-Band mode in enhanced coverage1178

A.4.2.24.1Test Purpose and Environment1178

A.4.2.24.2Test Requirements1181

A.4.2.25E-UTRAN FDD – FDD Inter frequency case for Cat-M1 UE in normal coverage1182

A.4.2.25.1Test Purpose and Environment1182

A.4.2.25.2Test Requirements1183

A.4.2.26E-UTRAN HD – FDD Inter frequency case for Cat-M1 UE in normal coverage1184

A.4.2.26.1Test Purpose and Environment1184

A.4.2.26.2Test Requirements1185

A.4.2.27E-UTRAN TDD – FDD Inter frequency case for Cat-M1 UE in normal coverage1186

A.4.2.27.1Test Purpose and Environment1186

A.4.2.27.2Test Requirements1187

A.4.2.28E-UTRAN FDD – FDD Inter frequency case for Cat-M1 UE in enhanced coverage1188

A.4.2.28.1Test Purpose and Environment1188

A.4.2.28.2Test Requirements1189

A.4.2.29E-UTRAN HD – FDD Inter frequency case for Cat-M1 UE in enhanced coverage1190

A.4.2.29.1Test Purpose and Environment1190

A.4.2.29.2Test Requirements1191

A.4.2.30E-UTRAN TDD Inter frequency case for Cat-M1 UE in enhanced coverage1192

A.4.2.30.1Test Purpose and Environment1192

A.4.2.30.2Test Requirements1193

A.4.2.31E-UTRAN FDD – FDD Inter frequency case for UE Category 1bis1194

A.4.2.31.1Test Purpose and Environment1194

A.4.2.31.2Test Requirements1195

A.4.2.32E-UTRAN FDD – TDD Inter frequency case for UE Category 1bis1196

A.4.2.32.1Test Purpose and Environment1196

A.4.2.32.2Test Requirements1197

A.4.2.33E-UTRAN TDD – FDD Inter frequency case for UE Category 1bis1198

A.4.2.33.1Test Purpose and Environment1198

A.4.2.33.2Test Requirements1199

A.4.2.34E-UTRAN TDD – TDD: Inter frequency case for UE Category 1bis1200

A.4.2.34.1Test Purpose and Environment1200

A.4.2.34.2Test Requirements1201

A.4.2.35E-UTRAN TDD - TDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage1202

A.4.2.35.1Test Purpose and Environment1202

A.4.2.35.2Test Requirements1204

A.4.2.36E-UTRAN TDD – TDD Intra frequency case for UE Category NB1 In-Band mode in enhanced coverage1205

A.4.2.36.1Test Purpose and Environment1205

A.4.2.36.2Test Requirements1207

A.4.2.37E-UTRAN TDD – TDD Inter frequency case for UE Category NB1 In-Band mode in enhanced coverage1208

A.4.2.37.1Test Purpose and Environment1208

A.4.2.37.2Test Requirements1210

A.4.2.38HD – FDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage with serving cell RRM measurement relaxation1211

A.4.2.38.1Test Purpose and Environment1211

A.4.2.38.2Test Requirements1213

A.4.2.39E-UTRAN FDD – FDD Intra frequency case for UE configured with highSpeedEnhMeasFlag2-r161214

A.4.2.39.1Test Purpose and Environment1214

A.4.2.39.2Test Requirements1215

A.4.2.40E-UTRAN TDD – TDD Intra frequency case for UE configured with highSpeedEnhMeasFlag2-r161216

A.4.2.40.1Test Purpose and Environment1216

A.4.2.40.2Test Requirements1217

A.4.2.41 HD – FDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage with UE specific DRX1218

A.4.2.41.1Test Purpose and Environment1218

A.4.2.41.2Test Requirements1221

A.4.2.42HD – FDD Intra frequency case for UE Category NB1 In-Band mode in enhanced coverage with UE specific DRX1222

A.4.2.42.1Test Purpose and Environment1222

A.4.2.42.2Test Requirements1224

A.4.2.43HD – FDD Inter frequency case for UE Category NB1 In-Band mode in enhanced coverage with UE specific DRX1225

A.4.2.43.1Test Purpose and Environment1225

A.4.2.43.2Test Requirements1227

A.4.2.44E-UTRAN TDD - TDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage with UE specific DRX1228

A.4.2.44.1Test Purpose and Environment1228

A.4.2.44.2Test Requirements1230

A.4.2.45E-UTRAN TDD – TDD Intra frequency case for UE Category NB1 In-Band mode in enhanced coverage with UE specific DRX1231

A.4.2.45.1Test Purpose and Environment1231

A.4.2.45.2Test Requirements1233

A.4.2.46E-UTRAN TDD – TDD Inter frequency case for UE Category NB1 In-Band mode in enhanced coverage with UE specific DRX1234

A.4.2.46.1Test Purpose and Environment1234

A.4.2.46.2Test Requirements1236

A.4.2.47HD – FDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage with serving cell RRM measurement relaxation with UE specific DRX1237

A.4.2.47.1Test Purpose and Environment1237

A.4.2.47.2Test Requirements1239

A.4.2.48E-UTRAN FD-FDD RSS based Intra frequency case for Cat-M1 UE in normal coverage1240

A.4.2.48.1Test Purpose and Environment1240

A.4.2.48.2Test Requirements1241

A.4.2.49E-UTRAN HD-FDD RSS based Intra frequency case for Cat-M1 UE in normal coverage1242

A.4.2.49.1Test Purpose and Environment1242

A.4.2.49.2Test Requirements1244

A.4.2.50E-UTRAN TDD RSS based Intra frequency case for Cat-M1 UE in normal coverage1245

A.4.2.50.1Test Purpose and Environment1245

A.4.2.50.2Test Requirements1247

A.4.2.51 E-UTRAN FD-FDD RSS based Intra frequency case for Cat-M1 UE in enhanced coverage1248

A.4.2.51.1Test Purpose and Environment1248

A.4.2.51.2Test Requirements1250

A.4.2.52 E-UTRAN HD-FDD RSS based Intra frequency case for Cat-M1 UE in enhanced coverage1251

A.4.2.52.1Test Purpose and Environment1251

A.4.2.52.2Test Requirements1253

A.4.2.53 E-UTRAN TDD RSS based Intra frequency case for Cat-M1 UE in enhanced coverage1254

A.4.2.53.1Test Purpose and Environment1254

A.4.2.53.2Test Requirements1255

A.4.2.54E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage with serving cell RRM measurement relaxation1256

A.4.2.54.1Test Purpose and Environment1256

A.4.2.54.2Test Requirements1258

A.4.2.55E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in normal coverage with serving cell RRM measurement relaxation1259

A.4.2.55.1Test Purpose and Environment1259

A.4.2.55.2Test Requirements1261

A.4.2.56E-UTRAN TDD – TDD Intra frequency case for Cat-M1 UE in normal coverage1262

A.4.2.56.1Test Purpose and Environment1262

A.4.2.56.2Test Requirements1263

A.4.3E-UTRAN to UTRAN Cell Re-Selection1264

A.4.3.1E-UTRAN FDD – UTRAN FDD:1264

A.4.3.1.1EUTRA FDD-UTRA FDD cell reselection: UTRA FDD is of higher priority1264

A.4.3.1.1.1Test Purpose and Environment1264

A.4.3.1.1.2Test Requirements1266

A.4.3.1.2EUTRA FDD-UTRA FDD cell reselection: UTRA FDD is of lower priority1266

A.4.3.1.2.1Test Purpose and Environment1266

A.4.3.1.2.2Test Requirements1269

A.4.3.1.3EUTRA FDD-UTRA FDD cell reselection in fading propagation conditions: UTRA FDD is of lower priority1269

A.4.3.1.3.1Test Purpose and Environment1269

A.4.3.1.3.2Test Requirements1272

A.4.3.1.4EUTRA FDD-UTRA FDD cell reselection: UTRA FDD is of lower priority for 5MHz bandwidth1272

A.4.3.1.4.1Test Purpose and Environment1272

A.4.3.1.4.2Test Requirements1273

A.4.3.1.5Idle mode FDD to UTRA FDD interRAT reselection1273

A.4.3.1.5.1Test Purpose and Environment1273

A.4.3.1.5.2Test Requirements1276

A.4.3.2E-UTRAN FDD – UTRAN TDD:1277

A.4.3.2.1Test Purpose and Environment1277

A.4.3.2.1.1Void1277

A.4.3.2.1.21.28Mcps TDD option1277

A.4.3.2.1.3Void1279

A.4.3.2.2Test Requirements1279

A.4.3.2.2.11.28Mcps TDD option1279

A.4.3.2AE-UTRA FDD to UTRA TDD cell re-selection for IncMon1279

A.4.3.2A.1Test Purpose and Environment1279

A.4.3.2A.2Test Requirements1283

A.4.3.3E-UTRAN TDD – UTRAN FDD:1283

A.4.3.3.1Test Purpose and Environment1283

A.4.3.3.2Test Requirements1286

A.4.3.3AIdle mode TDD to UTRA FDD interRAT reselection1286

A.4.3.3A.1Test Purpose and Environment1286

A.4.3.3A.2Test Requirements1291

A.4.3.4E-UTRAN TDD – UTRAN TDD:1292

A.4.3.4.1E-UTRA to UTRA TDD cell re-selection: UTRA is of higher priority1292

A.4.3.4.1.1Test Purpose and Environment1292

A.4.3.4.1.2Test Requirements1294

A.4.3.4.2E-UTRA to UTRA TDD cell re-selection: UTRA is of lower priority1294

A.4.3.4.2.1Test Purpose and Environment1294

A.4.3.4.2.2Test Requirements1296

A.4.3.4.3EUTRA TDD-UTRA TDD cell reselection in fading propagation conditions: UTRA TDD is of lower priority1296

A.4.3.4.3.1Test Purpose and Environment1296

A.4.3.4.3.2Test Requirements1299

A.4.3.4.4E-UTRA TDD to UTRA TDD cell re-selection for IncMon1299

A.4.3.4.4.1Test Purpose and Environment1299

A.4.3.4.4.2Test Requirements1303

A.4.4E-UTRAN to GSM Cell Re-Selection1303

A.4.4.1E-UTRAN FDD – GSM:1303

A.4.4.1.1Test Purpose and Environment1303

A.4.4.1.2Test Requirements1305

A.4.4.2E-UTRAN TDD – GSM:1305

A.4.4.2.1Test Purpose and Environment1305

A.4.4.2.2Test Requirements1307

A.4.5E-UTRAN to HRPD Cell Re-Selection1308

A.4.5.1E-UTRAN FDD – HRPD1308

A.4.5.1.1E-UTRAN FDD – HRPD Cell Reselection: HRPD is of Lower Priority1308

A.4.5.1.1.1Test Purpose and Environment1308

A.4.5.1.1.2Test Requirements1310

A.4.5.2E-UTRAN TDD – HRPD1310

A.4.5.2.1E-UTRAN TDD – HRPD Cell Reselection: HRPD is of Lower Priority1310

A.4.5.2.1.1Test Purpose and Environment1310

A.4.5.2.1.2Test Requirements1313

A.4.6E-UTRAN to cdma2000 1X Cell Re-Selection1313

A.4.6.1E-UTRAN FDD – cdma2000 1X1313

A.4.6.1.1E-UTRAN FDD – cdma2000 1X Cell Reselection: cdma2000 1X is of Lower Priority1313

A.4.6.1.1.1Test Purpose and Environment1313

A.4.6.1.1.2Test Requirements1316

A.4.6.2E-UTRAN TDD – cdma2000 1X1316

A.4.6.2.1E-UTRAN TDD –cdma2000 1X Cell Reselection: cdma2000 1X is of Lower Priority1316

A.4.6.2.1.1Test Purpose and Environment1316

A.4.6.2.1.2Test Requirements1319

A.4.7Idle State Positioning Measurement for UE category NB11319

A.4.7.1HD – FDD Intra frequency case for UE Category NB1 standalone mode in enhanced coverage1319

A.4.7.1.1Test Purpose and Environment1319

A.4.7.1.2Test Requirements1324

A.4.7.2HD – FDD Inter frequency case for UE Category NB1 standalone mode in enhanced coverage1325

A.4.7.2.1Test Purpose and Environment1325

A.4.7.4.2Test Requirements1329

A.4.7.3TDD Intra frequency case for UE Category NB1 standalone mode in enhanced coverage1330

A.4.7.3.1Test Purpose and Environment1330

A.4.7.3.2Test Requirements1334

A.4.7.4TDD Inter frequency case for UE Category NB1 standalone mode in enhanced coverage1335

A.4.7.4.1Test Purpose and Environment1335

A.4.7.4.2Test Requirements1339

A.5E-UTRAN RRC CONNECTED Mode Mobility1340

A.5.1E-UTRAN Handover1340

A.5.1.1E-UTRAN FDD - FDD Intra frequency handover1340

A.5.1.1.1Test Purpose and Environment1340

A.5.1.1.2Test Requirements1342

A.5.1.2E-UTRAN TDD - TDD Intra frequency handover1342

A.5.1.2.1Test Purpose and Environment1342

A.5.1.2.2Test Requirements1344

A.5.1.3E-UTRAN FDD – FDD Inter frequency handover1344

A.5.1.3.1Test Purpose and Environment1344

A.5.1.3.2Test Requirements1346

A.5.1.4E-UTRAN TDD – TDD Inter frequency handover1346

A.5.1.4.1Test Purpose and Environment1346

A.5.1.4.2Test Requirements1348

A.5.1.5E-UTRAN FDD – FDD Inter frequency handover: unknown target cell1348

A.5.1.5.1Test Purpose and Environment1348

A.5.1.5.2Test Requirements1350

A.5.1.6 E-UTRAN TDD – TDD Inter frequency handover; unknown Target Cell1350

A.5.1.6.1Test Purpose and Environment1350

A.5.1.6.2Test Requirements1352

A.5.1.7E-UTRAN FDD – TDD Inter frequency handover1352

A.5.1.7.1Test Purpose and Environment1352

A.5.1.7.2Test Requirements1355

A.5.1.8E-UTRAN TDD – FDD Inter frequency handover1355

A.5.1.8.1Test Purpose and Environment1355

A.5.1.8.2Test Requirements1358

A.5.1.9E-UTRAN FDD - FDD Intra frequency handover for 5MHz bandwidth1358

A.5.1.9.1Test Purpose and Environment1358

A.5.1.9.2Test Requirements1359

A.5.1.10E-UTRAN FDD - FDD Intra frequency handover for UE category 01359

A.5.1.10.1Test Purpose and Environment1359

A.5.1.10.2Test Requirements1361

A.5.1.11E-UTRAN HD - FDD Intra frequency handover for UE category 01361

A.5.1.11.1Test Purpose and Environment1361

A.5.1.11.2Test Requirements1363

A.5.1.12E-UTRAN TDD - TDD Intra frequency handover for UE category 01363

A.5.1.12.1Test Purpose and Environment1363

A.5.1.12.2Test Requirements1365

A.5.1.13E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA1365

A.5.1.13.1Test Purpose and Environment1365

A.5.1.13.2Test Requirements1367

A.5.1.14E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA1368

A.5.1.14.1Test Purpose and Environment1368

A.5.1.14.2Test Requirements1369

A.5.1.15E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeA1370

A.5.1.15.1Test Purpose and Environment1370

A.5.1.15.2Test Requirements1371

A.5.1.16E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeB1372

A.5.1.16.1Test Purpose and Environment1372

A.5.1.16.2Test Requirements1373

A.5.1.17E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeB1374

A.5.1.17.1Test Purpose and Environment1374

A.5.1.17.2Test Requirements1375

A.5.1.18E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeB1376

A.5.1.18.1Test Purpose and Environment1376

A.5.1.18.2Test Requirements1377

A.5.1.19E-UTRAN FDD - FDD Intra frequency handover for UE Category 1bis1378

A.5.1.19.1Test Purpose and Environment1378

A.5.1.19.2Test Requirements1379

A.5.1.20E-UTRAN TDD - TDD Intra frequency handover for UE Category 1bis1380

A.5.1.20.1Test Purpose and Environment1380

A.5.1.20.2Test Requirements1381

A.5.1.21E-UTRAN FDD - FDD Intra frequency RACH-less handover1382

A.5.1.21.1Test Purpose and Environment1382

A.5.1.21.2Test Requirements1383

A.5.1.22E-UTRAN TDD - TDD Intra frequency RACH-less handover1383

A.5.1.22.1Test Purpose and Environment1383

A.5.1.22.2Test Requirements1385

A.5.1.23E-UTRAN FDD – FDD Inter frequency RACH-less handover1385

A.5.1.23.1Test Purpose and Environment1385

A.5.1.23.2Test Requirements1387

A.5.1.24E-UTRAN TDD – TDD Inter frequency RACH-less handover1387

A.5.1.24.1Test Purpose and Environment1387

A.5.1.24.2Test Requirements1389

A.5.1.25E-UTRAN FDD - FDD Intra frequency make-before-break handover1389

A.5.1.25.1Test Purpose and Environment1389

A.5.1.25.2Test Requirements1391

A.5.1.26E-UTRAN TDD - TDD Intra frequency make-before-break handover1392

A.5.1.26.1Test Purpose and Environment1392

A.5.1.26.2Test Requirements1393

A.5.1.27E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeA1394

A.5.1.27.1Test Purpose and Environment1394

A.5.1.27.2Test Requirements1395

A.5.1.28E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeA1396

A.5.1.28.1Test Purpose and Environment1396

A.5.1.28.2Test Requirements1397

A.5.1.29E-UTRAN TDD inter frequency handover for Cat-M1 UEs in CEModeA1398

A.5.1.29.1Test Purpose and Environment1398

A.5.1.29.2Test Requirements1399

A.5.1.30E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeB1400

A.5.1.30.1Test Purpose and Environment1400

A.5.1.30.2Test Requirements1401

A.5.1.31E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeB1402

A.5.1.31.1Test Purpose and Environment1402

A.5.1.31.2Test Requirements1403

A.5.1.32E-UTRAN TDD inter frequency handover for Cat-M1 UEs in CEModeB1404

A.5.1.32.1Test Purpose and Environment1404

A.5.1.32.2Test Requirements1405

A.5.1.33E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition1406

A.5.1.33.1Test Purpose and Environment1406

A.5.1.13.2Test Requirements1407

A.5.1.34E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition1408

A.5.1.34.1Test Purpose and Environment1408

A.5.1.34.2Test Requirements1409

A.5.1.35E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition1410

A.5.1.35.1Test Purpose and Environment1410

A.5.1.35.2Test Requirements1411

A.5.1.36E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition1412

A.5.1.36.1Test Purpose and Environment1412

A.5.1.36.2Test Requirements1413

A.5.1.37E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition1414

A.5.1.37.1Test Purpose and Environment1414

A.5.1.37.2Test Requirements1415

A.5.1.38E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition1416

A.5.1.38.1Test Purpose and Environment1416

A.5.1.38.2Test Requirements1417

A.5.1.39E-UTRAN FDD - FDD Intra frequency handover with direct SCell activation1418

A.5.1.39.1Test Purpose and Environment1418

A.5.1.39.2Test Requirements1419

A.5.1.40E-UTRAN TDD - TDD Intra frequency handover with direct SCell activation1420

A.5.1.40.1Test Purpose and Environment1420

A.5.1.40.2Test Requirements1421

A.5.1.41E-UTRAN FDD – FDD Intra-band Inter-frequency sync DAPS handover1422

A.5.1.41.1Test Purpose and Environment1422

A.5.1.41.2Test Requirements1424

A.5.1.42E-UTRAN FDD – FDD Intra-band Inter-frequency async DAPS handover1425

A.5.1.42.1Test Purpose and Environment1425

A.5.1.42.2Test Requirements1426

A.5.1.43E-UTRAN FDD – FDD Inter-band Inter-frequency sync DAPS handover1427

A.5.1.43.1Test Purpose and Environment1427

A.5.1.43.2Test Requirements1428

A.5.1.44E-UTRAN FDD – FDD Inter-band Inter-frequency async DAPS handover1429

A.5.1.44.1Test Purpose and Environment1429

A.5.1.44.2Test Requirements1430

A.5.1.45E-UTRAN FDD - FDD Intra frequency DAPS handover1431

A.5.1.45.1Test Purpose and Environment1431

A.5.1.45.1Test Requirements1432

A.5.1.46E-UTRAN TDD - TDD Intra frequency DAPS handover1433

A.5.1.46.1Test Purpose and Environment1433

A.5.1.46.2Test Requirements1434

A.5.1.47E-UTRAN FDD - FDD Intra frequency conditional handover1435

A.5.1.47.1Test Purpose and Environment1435

A.5.1.47.2Test Requirements1436

A.5.1.48E-UTRAN TDD - TDD Intra frequency conditional handover1437

A.5.1.48.1Test Purpose and Environment1437

A.5.1.48.2Test Requirements1438

A.5.1.49E-UTRAN FDD - FDD Inter frequency conditional handover1439

A.5.1.49.1Test Purpose and Environment1439

A.5.1.49.2Test Requirements1440

A.5.1.50E-UTRAN TDD - TDD Inter frequency conditional handover1441

A.5.1.50.1Test Purpose and Environment1441

A.5.1.50.2Test Requirements1442

A.5.1.51E-UTRAN FDD - TDD Inter frequency conditional handover1443

A.5.1.51.1Test Purpose and Environment1443

A.5.1.51.2Test Requirements1445

A.5.1.52E-UTRAN TDD - FDD Inter frequency conditional handover1445

A.5.152.1Test Purpose and Environment1445

A.5.1.52.2Test Requirements1448

A.5.1.53E-UTRAN TDD – TDD Intra-band Inter-frequency sync DAPS handover1449

A.5.1.53.1Test Purpose and Environment1449

A.5.1.53.2Test Requirements1451

A.5.1.54E-UTRAN TDD – TDD Inter-band Inter-frequency sync DAPS handover1452

A.5.1.54.1Test Purpose and Environment1452

A.5.1.54.2Test Requirements1454

A.5.1.55E-UTRAN FDD - TDD inter-band inter-frequency synchronous DAPS handover1455

A.5.1.55.1Test Purpose and Environment1455

A.5.1.56E-UTRAN TDD - FDD inter-band inter-frequency synchronous DAPS handover1459

A.5.1.56.1Test Purpose and Environment1459

A.5.1.56.2Test Requirements1462

A.5.1.57E-UTRAN FDD – TDD Inter-band Inter-frequency async DAPS handover1463

A.5.1.57.1Test Purpose and Environment1463

A.5.1.57.2Test Requirements1465

A.5.1.58E-UTRAN TDD – FDD Inter-band Inter-frequency async DAPS handover1465

A.5.1.58.1Test Purpose and Environment1465

A.5.1.58.2Test Requirements1468

A.5.2E-UTRAN Handover to other RATs1468

A.5.2.1E-UTRAN FDD – UTRAN FDD Handover1468

A.5.2.1.1Test Purpose and Environment1468

A.5.2.1.2Test Requirements1470

A.5.2.2E-UTRAN TDD - UTRAN FDD Handover1471

A.5.2.2.1Test Purpose and Environment1471

A.5.2.2.2Test Requirements1474

A.5.2.3 E-UTRAN FDD- GSM Handover1474

A.5.2.3.1Test Purpose and Environment1474

A.5.2.3.2Test Requirements1475

A.5.2.4E-UTRAN TDD - UTRAN TDD Handover1476

A.5.2.4.1Test Purpose and Environment1476

A.5.2.4.1.1Void1476

A.5.2.4.1.21.28 Mcps TDD option1476

A.5.2.4.1.3Void1478

A.5.2.4.2Test Requirements1478

A.5.2.4.2.1Void1478

A.5.2.4.2.21.28 Mcps TDD option1478

A.5.2.4.2.3Void1478

A.5.2.5E-UTRAN FDD – UTRAN TDD Handover1478

A.5.2.5.1Test Purpose and Environment1478

A.5.2.5.1.3Void1481

A.5.2.5.2Test Requirements1481

A.5.2.5.2.1Void1481

A.5.2.5.2.21.28 Mcps TDD option1481

A.5.2.5.2.3Void1481

A.5.2.6E-UTRAN TDD - GSM Handover1481

A.5.2.6.1Test Purpose and Environment1481

A.5.2.6.2Test Requirements1483

A.5.2.7E-UTRAN FDD – UTRAN FDD Handover; Unknown Target Cell1484

A.5.2.7.1Test Purpose and Environment1484

A.5.2.7.2Test Requirements1486

A.5.2.8E-UTRAN FDD - GSM Handover; Unknown Target Cell1486

A.5.2.8.1Test Purpose and Environment1486

A.5.2.8.2Test Requirements1487

A.5.2.9E-UTRAN TDD - GSM Handover; Unknown Target Cell1488

A.5.2.9.1Test Purpose and Environment1488

A.5.2.9.2Test Requirements1489

A.5.2.10E-UTRAN TDD to UTRAN TDD handover: unknown target cell1490

A.5.2.10.1Test Purpose and Environment1490

A.5.2.10.2Test Requirements1492

A.5.2.10AE-UTRAN FDD – UTRAN FDD Multicarrier Handover with two target cells1492

A.5.2.10A.1Test Purpose and Environment1492

A.5.2.10A.2Test Requirements1495

A.5.2.10BE-UTRAN TDD – UTRAN FDD Multicarrier Handover with two target cells1495

A.5.2.10B.1Test Purpose and Environment1495

A.5.2.10B.2Test Requirements1498

A.5.2.11E-UTRAN FDD – UTRAN FDD Handover for 5MHz Bandwidth1498

A.5.2.11.1Test Purpose and Environment1498

A.5.2.11.2Test Requirements1498

A.5.3E-UTRAN Handover to Non-3GPP RATs1499

A.5.3.1E-UTRAN FDD – HRPD Handover1499

A.5.3.1.1Test Purpose and Environment1499

A.5.3.1.2Test Requirements1501

A.5.3.2E-UTRAN FDD – cdma2000 1X Handover1501

A.5.3.2.1Test Purpose and Environment1501

A.5.3.2.2Test Requirements1504

A.5.3.3E-UTRAN FDD – HRPD Handover; Unknown Target Cell1504

A.5.3.3.1Test Purpose and Environment1504

A.5.3.3.2Test Requirements1507

A.5.3.4E-UTRAN FDD – cdma2000 1X Handover; Unknown Target cell1507

A.5.3.4.1Test Purpose and Environment1507

A.5.3.4.2Test Requirements1509

A.5.3.5E-UTRAN TDD – HRPD Handover1509

A.5.3.5.1Test Purpose and Environment1509

A.5.3.5.2Test Requirements1512

A.5.3.6E-UTRAN TDD – cdma2000 1X Handover1512

A.5.3.6.1Test Purpose and Environment1512

A.5.3.6.2Test Requirements1515

A.6RRC Connection Control1515

A.6.1RRC Re-establishment1515

A.6.1.1E-UTRAN FDD Intra-frequency RRC Re-establishment1515

A.6.1.1.1Test Purpose and Environment1515

A.6.1.1.2Test Requirements1516

A.6.1.2E-UTRAN FDD Inter-frequency RRC Re-establishment1517

A.6.1.2.1Test Purpose and Environment1517

A.6.1.2.2Test Requirements1518

A.6.1.3E-UTRAN TDD Intra-frequency RRC Re-establishment1519

A.6.1.3.1Test Purpose and Environment1519

A.6.1.3.2Test Requirements1520

A.6.1.4E-UTRAN TDD Inter-frequency RRC Re-establishment1521

A.6.1.4.1Test Purpose and Environment1521

A.6.1.4.2Test Requirements1522

A.6.1.5E-UTRAN FDD Intra-frequency RRC Re-establishment for 5MHz bandwidth1523

A.6.1.5.1Test Purpose and Environment1523

A.6.1.5.2Test Requirements1523

A.6.1.6E-UTRAN FD-FDD Intra-frequency RRC Re-establishment for UE category 01523

A.6.1.6.1Test Purpose and Environment1523

A.6.1.6.2Test Requirements1525

A.6.1.7E-UTRAN HD-FDD Intra-frequency RRC Re-establishment for UE category 01526

A.6.1.7.1Test Purpose and Environment1526

A.6.1.7.2Test Requirements1527

A.6.1.8E-UTRAN TDD Intra-frequency RRC Re-establishment for UE category 01528

A.6.1.8.1Test Purpose and Environment1528

A.6.1.8.2Test Requirements1529

A.6.1.9E-UTRAN FD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA1530

A.6.1.9.1Test Purpose and Environment1530

A.6.1.9.2Test Requirements1531

A.6.1.10E-UTRAN HD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA1532

A.6.1.10.1Test Purpose and Environment1532

A.6.1.10.2Test Requirements1533

A.6.1.11E-UTRAN TDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA1534

A.6.1.11.1Test Purpose and Environment1534

A.6.1.11.2Test Requirements1535

A.6.1.12E-UTRAN FD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeB1536

A.6.1.12.1Test Purpose and Environment1536

A.6.1.12.2Test Requirements1537

A.6.1.13E-UTRAN HD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeB1538

A.6.1.13.1Test Purpose and Environment1538

A.6.1.13.2Test Requirements1539

A.6.1.14E-UTRAN TDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeB1540

A.6.1.14.1Test Purpose and Environment1540

A.6.1.14.2Test Requirements1541

A.6.1.15HD-FDD Intra-frequency RRC Re-establishment for UE category NB1 in In-Band mode under enhanced coverage1542

A.6.1.15.1Test Purpose and Environment1542

A.6.1.15.2Test Requirements1544

A.6.1.16HD-FDD Inter-frequency RRC Re-establishment for UE category NB1 in In-Band mode under normal coverage1545

A.6.1.16.1Test Purpose and Environment1545

A.6.1.16.2Test Requirements1547

A.6.1.17E-UTRAN FD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA1548

A.6.1.17.1Test Purpose and Environment1548

A.6.1.17.2Test Requirements1549

A.6.1.18E-UTRAN HD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA1550

A.6.1.18.1Test Purpose and Environment1550

A.6.1.18.2Test Requirements1551

A.6.1.19E-UTRAN TDD-TDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA1552

A.6.1.19.1Test Purpose and Environment1552

A.6.1.19.2Test Requirements1553

A.6.1.20E-UTRAN FD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeB1554

A.6.1.20.1Test Purpose and Environment1554

A.6.1.20.2Test Requirements1555

A.6.1.21E-UTRAN HD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeB1556

A.6.1.21.1Test Purpose and Environment1556

A.6.1.21.2Test Requirements1557

A.6.1.22E-UTRAN TDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeB1558

A.6.1.22.1Test Purpose and Environment1558

A.6.1.22.2Test Requirements1559

A.6.1.23E-UTRAN TDD Inter-frequency RRC Re-establishment for UE category NB1 in In-Band mode under normal coverage1560

A.6.1.23.1Test Purpose and Environment1560

A.6.1.23.2Test Requirements1562

A.6.1.24E-UTRAN TDD - TDD Intra-frequency RRC Re-establishment for UE category NB1 in In-Band mode under enhanced coverage1563

A.6.1.24.1Test Purpose and Environment1563

A.6.1.24.2Test Requirements1565

A.6.2Random Access1566

A.6.2.1E-UTRAN FDD – Contention Based Random Access Test1566

A.6.2.1.1Test Purpose and Environment1566

A.6.2.1.2Test Requirements1567

A.6.2.1.2.1Random Access Response Reception1567

A.6.2.1.2.2No Random Access Response Reception1567

A.6.2.1.2.3Receiving a NACK on msg31567

A.6.2.1.2.4Reception of an Incorrect Message over Temporary C-RNTI1568

A.6.2.1.2.5Reception of a Correct Message over Temporary C-RNTI1568

A.6.2.1.2.6Contention Resolution Timer expiry1568

A.6.2.2E-UTRAN FDD – Non-Contention Based Random Access Test1568

A.6.2.2.1Test Purpose and Environment1568

A.6.2.2.2Test Requirements1569

A.6.2.2.2.1Random Access Response Reception1570

A.6.2.2.2.2No Random Access Response Reception1570

A.6.2.3E-UTRAN TDD – Contention Based Random Access Test1570

A.6.2.3.1Test Purpose and Environment1570

A.6.2.3.2Test Requirements1572

A.6.2.3.2.1Random Access Response Reception1572

A.6.2.3.2.2No Random Access Response reception1572

A.6.2.3.2.3Receiving a NACK on msg31572

A.6.2.3.2.4Reception of an Incorrect Message over Temporary C-RNTI1573

A.6.2.3.2.5Reception of a Correct Message over Temporary C-RNTI1573

A.6.2.3.2.6Contention Resolution Timer expiry1573

A.6.2.4E-UTRAN TDD – Non-Contention Based Random Access Test1573

A.6.2.4.1Test Purpose and Environment1573

A.6.2.4.2Test Requirements1575

A.6.2.4.2.1Random Access Response Reception1575

A.6.2.4.2.2No Random Access Response Reception1575

A.6.2.5E-UTRAN FDD – Contention Based Random Access Test for 5MHz bandwidth1575

A.6.2.5.1Test Purpose and Environment1575

A.6.2.5.2Test Requirements1576

A.6.2.6E-UTRAN FDD – Non-contention Based Random Access Test for 5MHz bandwidth1576

A.6.2.6.1Test Purpose and Environment1576

A.6.2.6.2Test Requirements1576

A.6.2.7E-UTRAN FDD – Non-Contention Based Random Access Test For SCell1577

A.6.2.7.1Test Purpose and Environment1577

A.6.2.7.2Test Requirements1579

A.6.2.7.2.1Random Access Response Reception1579

A.6.2.7.2.2No Random Access Response Reception1579

A.6.2.7.2.3Stop Preamble transmission if maximum number of preamble transmission counter has been reached1579

A.6.2.8E-UTRAN TDD – Non-Contention Based Random Access Test For SCell1580

A.6.2.8.1Test Purpose and Environment1580

A.6.2.8.2Test Requirements1582

A.6.2.8.2.1Random Access Response Reception1582

A.6.2.8.2.2No Random Access Response Reception1582

A.6.2.8.2.3Stop Preamble transmission if maximum number of preamble transmission counter has been reached1582

A.6.2.93DL/3UL TDD CA Non-Contention Based Random Access Test for 2 SCells1583

A.6.2.9.1Test Purpose and Environment1583

A.6.2.9.2Test Requirements1586

A.6.2.9.2.1Random Access Response Reception1586

A.6.2.9.2.2No Random Access Response Reception1587

A.6.2.9.2.3Stop Preamble transmission if maximum number of preamble transmission counter has been reached1587

A.6.2.10E-UTRAN FDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage1588

A.6.2.10.1Test Purpose and Environment1588

A.6.2.10.2Test Requirements1590

A.6.2.10.2.1Random Access Response Reception1590

A.6.2.10.2.2No Random Access Response Reception1591

A.6.2.10.2.3Receiving a NACK on msg31591

A.6.2.10.2.4Reception of an Incorrect Message over Temporary C-RNTI1591

A.6.2.10.2.5Reception of a Correct Message over Temporary C-RNTI1591

A.6.2.10.2.6Contention Resolution Timer expiry1591

A.6.2.10.2.7PRACH Resource Selection1592

A.6.2.11E-UTRAN HD-FDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage1592

A.6.2.11.1Test Purpose and Environment1592

A.6.2.11.2Test Requirements1594

A.6.2.11.2.1Random Access Response Reception1594

A.6.2.11.2.2No Random Access Response Reception1595

A.6.2.11.2.3Receiving a NACK on msg31595

A.6.2.11.2.4Reception of an Incorrect Message over Temporary C-RNTI1595

A.6.2.11.2.5Reception of a Correct Message over Temporary C-RNTI1595

A.6.2.11.2.6Contention Resolution Timer expiry1595

A.6.2.11.2.7PRACH Resource Selection1596

A.6.2.12E-UTRAN TDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage1596

A.6.2.12.1Test Purpose and Environment1596

A.6.2.12.2Test Requirements1598

A.6.2.12.2.1Random Access Response Reception1598

A.6.2.12.2.2No Random Access Response Reception1599

A.6.2.12.2.3Receiving a NACK on msg31599

A.6.2.12.2.4Reception of an Incorrect Message over Temporary C-RNTI1599

A.6.2.12.2.5Reception of a Correct Message over Temporary C-RNTI1599

A.6.2.12.2.6Contention Resolution Timer expiry1599

A.6.2.12.2.7PRACH Resource Selection1600

A.6.2.13E-UTRAN FDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage1600

A.6.2.13.1Test Purpose and Environment1600

A.6.2.13.2Test Requirements1602

A.6.2.13.2.1Random Access Response Reception1602

A.6.2.13.2.2No Random Access Response Reception1603

A.6.2.13.2.3Receiving a NACK on msg31603

A.6.2.13.2.4Reception of an Incorrect Message over Temporary C-RNTI1603

A.6.2.13.2.5Reception of a Correct Message over Temporary C-RNTI1603

A.6.2.13.2.6Contention Resolution Timer expiry1603

A.6.2.13.2.7PRACH Resource Selection1604

A.6.2.14E-UTRAN HD-FDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage1604

A.6.2.14.1Test Purpose and Environment1604

A.6.2.14.2Test Requirements1606

A.6.2.14.2.1Random Access Response Reception1606

A.6.2.14.2.2No Random Access Response Reception1607

A.6.2.14.2.3Receiving a NACK on msg31607

A.6.2.14.2.4Reception of an Incorrect Message over Temporary C-RNTI1607

A.6.2.14.2.5Reception of a Correct Message over Temporary C-RNTI1607

A.6.2.14.2.6Contention Resolution Timer expiry1607

A.6.2.14.2.7PRACH Resource Selection1608

A.6.2.15E-UTRAN TDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage1608

A.6.2.15.1Test Purpose and Environment1608

A.6.2.15.2Test Requirements1610

A.6.2.15.2.1Random Access Response Reception1610

A.6.2.15.2.2No Random Access Response Reception1611

A.6.2.15.2.3Receiving a NACK on msg31611

A.6.2.15.2.4Reception of an Incorrect Message over Temporary C-RNTI1611

A.6.2.15.2.5Reception of a Correct Message over Temporary C-RNTI1611

A.6.2.15.2.6Contention Resolution Timer expiry1611

A.6.2.15.2.7PRACH Resource Selection1612

A.6.2.16Contention Based Random Access Test for UE category NB1 UEs In-band mode in normal coverage1612

A.6.2.16.1Test Purpose and Environment1612

A.6.2.16.2Test Requirements1615

A.6.2.16.2.1Random Access Response Reception1615

A.6.2.16.2.2No Random Access Response Reception1616

A.6.2.16.2.3Receiving a NACK on msg31616

A.6.2.16.2.4Reception of an Incorrect Message over Temporary C-RNTI1616

A.6.2.16.2.5Reception of a Correct Message over Temporary C-RNTI1616

A.6.2.16.2.6Contention Resolution Timer expiry1616

A.6.2.16.2.7NPRACH Resource Selection1616

A.6.2.17Contention Based Random Access Test for UE category NB1 UEs In-band mode in Enhanced Coverage1617

A.6.2.17.1Test Purpose and Environment1617

A.6.2.17.2Test Requirements1620

A.6.2.17.2.1Random Access Response Reception1620

A.6.2.17.2.2No Random Access Response Reception1621

A.6.2.17.2.3Receiving a NACK on msg31621

A.6.2.17.2.4Reception of an Incorrect Message over Temporary C-RNTI1621

A.6.2.17.2.5Reception of a Correct Message over Temporary C-RNTI1621

A.6.2.17.2.6Contention Resolution Timer expiry1621

A.6.2.17.2.7NPRACH Resource Selection1621

A.6.2.18Contention Based Random Access on Non-anchor Carrier Test for UE category NB1 UEs In-band mode in Enhanced Coverage1622

A.6.2.18.1Test Purpose and Environment1622

A.6.2.18.2Test Requirements1625

A.6.2.18.2.1Random Access Response Reception1625

A.6.2.18.2.2No Random Access Response Reception1626

A.6.2.18.2.3Receiving a NACK on msg31626

A.6.2.18.2.4Reception of an Incorrect Message over Temporary C-RNTI1626

A.6.2.18.2.5Reception of a Correct Message over Temporary C-RNTI1626

A.6.2.18.2.6Contention Resolution Timer expiry1626

A.6.2.18.2.7NPRACH Resource Selection1626

A.6.2.19TDD Contention Based Random Access Test for UE category NB1 UEs In-band mode in normal coverage1627

A.6.2.19.1Test Purpose and Environment1627

A.6.2.19.2Test Requirements1629

A.6.2.19.2.1Random Access Response Reception1629

A.6.2.19.2.2No Random Access Response Reception1630

A.6.2.19.2.3Receiving a NACK on msg31630

A.6.2.19.2.4Reception of an Incorrect Message over Temporary C-RNTI1630

A.6.2.19.2.5Reception of a Correct Message over Temporary C-RNTI1630

A.6.2.19.2.6Contention Resolution Timer expiry1630

A.6.2.19.2.7NPRACH Resource Selection1630

A.6.2.20TDD Contention Based Random Access Test for UE category NB1 UEs In-band mode in enhanced coverage1631

A.6.2.20.1Test Purpose and Environment1631

A.6.2.20.2Test Requirements1633

A.6.2.20.2.1Random Access Response Reception1633

A.6.2.20.2.2No Random Access Response Reception1634

A.6.2.20.2.3Receiving a NACK on msg31634

A.6.2.20.2.4Reception of an Incorrect Message over Temporary C-RNTI1634

A.6.2.20.2.5Reception of a Correct Message over Temporary C-RNTI1634

A.6.2.20.2.6Contention Resolution Timer expiry1634

A.6.2.20.2.7NPRACH Resource Selection1634

A.6.2.21TDD Contention Based Random Access on Non-anchor Carrier Test for UE category NB1 UEs In-band mode in Enhanced Coverage1635

A.6.2.21.1Test Purpose and Environment1635

A.6.2.21.2Test Requirements1637

A.6.2.21.2.1Random Access Response Reception1637

A.6.2.21.2.2No Random Access Response Reception1638

A.6.2.21.2.3Receiving a NACK on msg31638

A.6.2.21.2.4Reception of an Incorrect Message over Temporary C-RNTI1638

A.6.2.21.2.5Reception of a Correct Message over Temporary C-RNTI1638

A.6.2.21.2.6Contention Resolution Timer expiry1638

A.6.2.21.2.7NPRACH Resource Selection1638

A.6.3RRC Connection Release with Redirection1639

A.6.3.1Redirection from E-UTRAN FDD to UTRAN FDD1639

A.6.3.1.1Test Purpose and Environment1639

A.6.3.1.2Test Requirements1641

A.6.3.2Redirection from E-UTRAN TDD to UTRAN FDD1641

A.6.3.2.1Test Purpose and Environment1641

A.6.3.2.2Test Requirements1643

A.6.3.3Redirection from E-UTRAN FDD to GERAN when System Information is provided1643

A.6.3.3.1Test Purpose and Environment1643

A.6.3.3.2Test Requirements1644

A.6.3.4Redirection from E-UTRAN TDD to GERAN when System Information is provided1645

A.6.3.4.1Test Purpose and Environment1645

A.6.3.4.2Test Requirements1646

A.6.3.5E-UTRA TDD RRC connection release redirection to UTRA TDD1647

A.6.3.5.1Test Purpose and Environment1647

A.6.3.5.2Test Requirements1649

A.6.3.6E-UTRA FDD RRC connection release redirection to UTRA TDD1649

A.6.3.6.1Test Purpose and Environment1649

A. 6.3.6.2Test Requirements1652

A.6.3.7E-UTRA TDD RRC connection release redirection to UTRA TDD without SI provided1652

A.6.3.7.1Test Purpose and Environment1652

A.6.3.7.2Test Requirements1655

A.6.3.8E-UTRA FDD RRC connection release redirection to UTRA TDD without SI provided1655

A.6.3.8.1Test Purpose and Environment1655

A.6.3.8.2Test Requirements1658

A.6.3.9Redirection from E-UTRAN FDD to UTRAN FDD without System Information1658

A.6.3.9.1Test Purpose and Environment1658

A.6.3.9.2Test Requirements1660

A.6.3.10Redirection from E-UTRAN FDD to GERAN when System Information is not provided1660

A.6.3.10.1Test Purpose and Environment1660

A.6.3.10.2Test Requirements1662

A.6.3.11Redirection from E-UTRAN TDD to GERAN when System Information is not provided1662

A.6.3.11.1Test Purpose and Environment1662

A.6.3.11.2Test Requirements1664

A.6.3.12E-UTRAN TDD RRC connection release redirection to UTRAN FDD without SI provided1664

A.6.3.12.1Test Purpose and Environment1664

A.6.3.12.2Test Requirements1667

A.6.3.13Redirection from E-UTRA to NR FR1 for redcap UE1667

A.6.3.13.1Test Purpose and Environment1667

A.6.3.13.2Test Parameters1667

A.6.3.13.3Test Requirements1671

A.7Timing and Signalling Characteristics1672

A.7.1UE Transmit Timing1672

A.7.1.1E-UTRAN FDD – UE Transmit Timing Accuracy Tests1672

A.7.1.1.1Test Purpose and Environment1672

A.7.1.1.2Test Requirements1673

A.7.1.2E-UTRAN TDD - UE Transmit Timing Accuracy Tests1674

A.7.1.2.1Test Purpose and Environment1674

A.7.1.2.2Test Requirements1676

A.7.1.3E-UTRAN FDD – UE Transmit Timing Accuracy Tests for SCell1677

A.7.1.3.1Test Purpose and Environment1677

A.7.1.3.2Test Requirements1679

A.7.1.4E-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell1680

A.7.1.4.1Test Purpose and Environment1680

A.7.1.4.2Test Requirements1681

A.7.1.4AE-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell for 20 MHz + 10 MHz1682

A.7.1.4A.1Test Purpose and Environment1682

A.7.1.4A.2Test Requirements1682

A.7.1.5E-UTRAN FDD – UE Transmit Timing Accuracy Tests for 5MHz Bandwidth1682

A.7.1.5.1Test Purpose and Environment1682

A.7.1.5.2Test Requirements1683

A.7.1.6E-UTRAN FDD – UE Transmit Timing Accuracy Tests for SCell in sTAG1683

A.7.1.6.1Test Purpose and Environment1683

A.7.1.6.2Test Requirements1685

A.7.1.7E-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell in sTAG1686

A.7.1.7.1Test Purpose and Environment1686

A.7.1.7.2Test Requirements1687

A.7.1.7AE-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell in sTAG for 20MHz +20MHz1688

A.7.1.7A.1Test Purpose and Environment1688

A.7.1.7A.2Test Requirements1688

A.7.1.7BE-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell in sTAG for 20MHz +10MHz1688

A.7.1.7B.1Test Purpose and Environment1688

A.7.1.7B.2Test Requirements1688

A.7.1.8Void1689

A.7.1.8.1Void1689

A.7.1.8.2Void1689

A.7.1.9Void1689

A.7.1.9.1Void1689

A.7.1.9.2Void1689

A.7.1.10E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA1689

A.7.1.10.1Test Purpose and Environment1689

A.7.1.10.2Test Requirements1691

A.7.1.11E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA1691

A.7.1.11.1Test Purpose and Environment1691

A.7.1.11.2Test Requirements1693

A.7.1.12E-UTRAN TDD - UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA1693

A.7.1.12.1Test Purpose and Environment1693

A.7.1.12.2Test Requirements1695

A.7.1.133DL/3UL TDD CA UE Transmit Timing Accuracy Tests for 2 SCells1695

A.7.1.13.1Test Purpose and Environment1695

A.7.1.13.2Test Requirements1697

A.7.1.14E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB1698

A.7.1.14.1Test Purpose and Environment1698

A.7.1.14.2Test Requirements1699

A.7.1.15E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB1699

A.7.1.15.1Test Purpose and Environment1699

A.7.1.15.2Test Requirements1700

A.7.1.16E-UTRAN TDD - UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB1701

A.7.1.16.1Test Purpose and Environment1701

A.7.1.16.2Test Requirements1702

A.7.1.17E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Category NB1 UE In-Band mode under normal coverage1703

A.7.1.17.1Test Purpose and Environment1703

A.7.1.17.2Test Requirements1705

A.7.1.18E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Category NB1 UE In-band mode under enhanced coverage1706

A.7.1.18.1Test Purpose and Environment1706

A.7.1.18.2Test Requirements1708

A.7.1.19E-UTRAN FDD - UE Transmit Timing Accuracy Test for RACH-less Handover1709

A.7.1.19.1Test Purpose and Environment1709

A.7.1.19.2Test Requirements1710

A.7.1.20E-UTRAN TDD - UE Transmit Timing Accuracy Test for RACH-less Handover1710

A.7.1.20.1Test Purpose and Environment1710

A.7.1.20.2Test Requirements1712

A.7.1.21E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeA1712

A.7.1.21.1Test Purpose and Environment1712

A.7.1.21.2Test Requirements1714

A.7.1.22E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeA1714

A.7.1.22.1Test Purpose and Environment1714

A.7.1.22.2Test Requirements1716

A.7.1.23E-UTRAN TDD - UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeA1716

A.7.1.23.1Test Purpose and Environment1716

A.7.1.23.2Test Requirements1718

A.7.1.24E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeB1718

A.7.1.24.1Test Purpose and Environment1718

A.7.1.24.2Test Requirements1719

A.7.1.25E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeB1720

A.7.1.25.1Test Purpose and Environment1720

A.7.1.25.2Test Requirements1721

A.7.1.26E-UTRAN TDD - UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeB1722

A.7.1.26.1Test Purpose and Environment1722

A.7.1.26.2Test Requirements1723

A.7.1.27E-UTRAN TDD – UE Transmit Timing Accuracy Tests for Category NB1 UE In-Band mode under normal coverage1724

A.7.1.27.1Test Purpose and Environment1724

A.7.1.27.2Test Requirements1726

A.7.1.28E-UTRAN TDD – UE Transmit Timing Accuracy Tests for Category NB1 UE In-band mode under enhanced coverage1726

A.7.1.28.1Test Purpose and Environment1726

A.7.1.28.2Test Requirements1728

A.7.2UE Timing Advance1729

A.7.2.1E-UTRAN FDD – UE Timing Advance Adjustment Accuracy Test1729

A.7.2.1.1Test Purpose and Environment1729

A.7.2.1.2Test Requirements1730

A.7.2.2E-UTRAN TDD – UE Timing Advance Adjustment Accuracy Test1731

A.7.2.2.1Test Purpose and Environment1731

A.7.2.2.2Test Requirements1733

A.7.2.3E-UTRAN FDD – UE Timing Advance Adjustment Accuracy Test for 5MHz1733

A.7.2.3.1Test Purpose and Environment1733

A.7.2.3.2Test Requirements1733

A.7.2.4E-UTRAN FDD – UE Timing Advance Adjustment Accuracy Test for SCell in sTAG1733

A.7.2.4.1Test Purpose and Environment1733

A.7.2.4.2Test Requirements1736

A.7.2.5E-UTRAN TDD – UE Timing Advance Adjustment Accuracy Test for Scell in sTAG1736

A.7.2.5.1Test Purpose and Environment1736

A.7.2.5.2Test Requirements1738

A.7.2.5AE-UTRAN TDD – UE Timing Advance Adjustment Accuracy Test for Scell in sTAG for 20 MHz +20 MHz1738

A.7.2.5A.1Test Purpose and Environment1738

A.7.2.5A.2Test Requirements1739

A.7.2.5BE-UTRAN TDD – UE Timing Advance Adjustment Accuracy Test for Scell in sTAG for 20 MHz +10 MHz1739

A.7.2.5B.1Test Purpose and Environment1739

A.7.2.5B.2Test Requirements1739

A.7.2.6E-UTRAN FDD Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA1739

A.7.2.6.1Test Purpose and Environment1739

A.7.2.6.2Test Requirements1742

A.7.2.7E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA1742

A.7.2.7.1Test Purpose and Environment1742

A.7.2.7.2Test Requirements1744

A.7.2.8E-UTRAN TDD Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA1744

A.7.2.8.1Test Purpose and Environment1744

A.7.2.8.2Test Requirements1746

A.7.2.9.2Test Requirements1747

A.7.2.10E-UTRAN FDD UE Timing Advance Adjustment Accuracy Test in CEModeB1748

A.7.2.10.1Test Purpose and Environment1748

A.7.2.10.2Test Requirements1749

A.7.2.11E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test in CEModeB1749

A.7.2.11.1Test Purpose and Environment1749

A.7.2.11.2Test Requirements1751

A.7.2.12E-UTRAN TDD UE Timing Advance Adjustment Accuracy Test in CEModeB1751

A.7.2.12.1Test Purpose and Environment1751

A.7.2.12.2Test Requirements1753

A.7.2.13E-UTRAN FDD – UE Timing Advance Adjustment delay Test for sTTI and ShortProcessingTime=TRUE1754

A.7.2.13.1Test Purpose and Environment1754

A.7.2.13.2Test Requirements1755

A.7.2.14E-UTRAN TDD – UE Timing Advance Adjustment delay Test for sTTI and ShortProcessingTime=TRUE1756

A.7.2.14.1Test Purpose and Environment1756

A.7.2.14.2Test Requirements1758

A.7.2.15E-UTRAN TDD – TDD UE Timing Advance Adjustment Accuracy Test for UE Category NB1 in Standalone Mode under Enhanced Coverage1758

A.7.2.15.1Test Purpose and Environment1758

A.7.2.15.2Test Requirements1760

A.7.3Radio Link Monitoring1760

A.7.3.1E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync1760

A.7.3.1.1Test Purpose and Environment1760

A.7.3.1.2Test Requirements1764

A.7.3.2E-UTRAN FDD Radio Link Monitoring Test for In-sync1764

A.7.3.2.1Test Purpose and Environment1764

A.7.3.2.2Test Requirements1768

A.7.3.3E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync1768

A.7.3.3.1Test Purpose and Environment1768

A.7.3.3.2Test Requirements1772

A.7.3.4E-UTRAN TDD Radio Link Monitoring Test for In-sync1772

A.7.3.4.1Test Purpose and Environment1772

A.7.3.4.2Test Requirements1776

A.7.3.5E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync in DRX1776

A.7.3.5.1Test Purpose and Environment1776

A.7.3.5.2Test Requirements1779

A.7.3.6E-UTRAN FDD Radio Link Monitoring Test for In-sync in DRX1780

A.7.3.6.1Test Purpose and Environment1780

A.7.3.6.2Test Requirements1783

A.7.3.7E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync in DRX1783

A.7.3.7.1Test Purpose and Environment1783

A.7.3.7.2Test Requirements1786

A.7.3.8E-UTRAN TDD Radio Link Monitoring Test for In-sync in DRX1786

A.7.3.8.1Test Purpose and Environment1786

A.7.3.8.2Test Requirements1789

A.7.3.9 E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction and Non-MBSFN ABS1789

A.7.3.9.2Test Requirements1792

A.7.3.10E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with Non-MBSFN ABS1792

A.7.3.10.1Test Purpose and Environment1792

A.7.3.11E-UTRAN FDD Radio Link Monitoring Test for In-sync for Non-MBSFN ABS1796

A.7.3.11.1Test Purpose and Environment1796

A.7.3.11.2Test Requirements1801

A.7.3.12E-UTRAN TDD Radio Link Monitoring Test for In-sync for Non-MBSFN ABS1801

A.7.3.12.1Test Purpose and Environment1801

A.7.3.12.2Test Requirements1806

A.7.3.13 E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with MBSFN ABS1806

A.7.3.13.1Test Purpose and Environment1806

A.7.3.13.2Test Requirements1809

A.7.3.14 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with MBSFN ABS1809

A.7.3.14.1Test Purpose and Environment1809

A.7.3.14.2Test Requirements1812

A.7.3.15E-UTRAN FDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resource Restriction with MBSFN ABS1812

A.7.3.15.1Test Purpose and Environment1812

A.7.3.15.2Test Requirements1816

A.7.3.16E-UTRAN TDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resource Restriction with MBSFN ABS1816

A.7.3.16.1Test Purpose and Environment1816

A.7.3.16.2Test Requirements1821

A.7.3.17E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS1821

A.7.3.17.1Test Purpose and Environment1821

A.7.3.17.2Test Requirements1825

A.7.3.18E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS1825

A.7.3.18.1Test Purpose and Environment1825

A.7.3.18.2Test Requirements1829

A.7.3.19E-UTRAN FDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resouce Restriction with CRS assistance information and Non-MBSFN ABS1829

A.7.3.19.1Test Purpose and Environment1829

A.7.3.19.2Test Requirements1834

A.7.3.20E-UTRAN TDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resouce Restriction with CRS assistance information and Non-MBSFN ABS1834

A.7.3.20.1Test Purpose and Environment1834

A.7.3.20.2Test Requirements1839

A.7.3.21E-UTRAN FDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resouce Restriction with CRS assistance information and MBSFN ABS1839

A.7.3.21.1Test Purpose and Environment1839

A.7.3.21.2Test Requirements1844

A.7.3.22E-UTRAN TDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resouce Restriction with CRS assistance information and MBSFN ABS1844

A.7.3.22.1Test Purpose and Environment1844

A.7.3.22.2Test Requirements1849

A.7.3.23E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync for 5MHz Bandwidth1849

A.7.3.23.1Test Purpose and Environment1849

A.7.3.23.2Test Requirements1850

A.7.3.24E-UTRAN FDD Radio Link Monitoring Test for In-sync for 5MHz Bandwidth1850

A.7.3.24.1Test Purpose and Environment1850

A.7.3.24.2Test Requirements1851

A.7.3.25E-UTRAN FDD Radio Link Monitoring Test for In-sync in DRX for 5MHz Bandwidth1851

A.7.3.25.1Test Purpose and Environment1851

A.7.3.25.2Test Requirements1852

A.7.3.26E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for UE Category 01852

A.7.3.26.1Test Purpose and Environment1852

A.7.3.26.2Test Requirements1855

A.7.3.27E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync for UE Category 01855

A.7.3.27.1Test Purpose and Environment1855

A.7.3.27.2Test Requirements1858

A.7.3.28E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category 01858

A.7.3.28.1Test Purpose and Environment1858

A.7.3.28.2Test Requirements1861

A.7.3.29E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category 01861

A.7.3.29.1Test Purpose and Environment1861

A.7.3.29.2Test Requirements1864

A.7.3.30E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync for UE Category 01864

A.7.3.30.1Test Purpose and Environment1864

A.7.3.30.2Test Requirements1867

A.7.3.31E-UTRAN HD-FDD Radio Link Monitoring Test for In-sync for UE Category 01867

A.7.3.31.1Test Purpose and Environment1867

A.7.3.31.2Test Requirements1870

A.7.3.32E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category 01870

A.7.3.32.1Test Purpose and Environment1870

A.7.3.32.2Test Requirements1873

A.7.3.33E-UTRAN HD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category 01873

A.7.3.33.1Test Purpose and Environment1873

A.7.3.33.2Test Requirements1876

A.7.3.34E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync for UE Category 01876

A.7.3.34.1Test Purpose and Environment1876

A.7.3.34.2Test Requirements1879

A.7.3.35E-UTRAN TDD Radio Link Monitoring Test for In-sync for UE category 01879

A.7.3.35.1Test Purpose and Environment1879

A.7.3.35.2Test Requirements1882

A.7.3.36E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category 01882

A.7.3.36.1Test Purpose and Environment1882

A.7.3.36.2Test Requirements1885

A.7.3.37E-UTRAN TDD Radio Link Monitoring Test for In-sync in DRX for UE category 01885

A.7.3.37.1Test Purpose and Environment1885

A.7.3.37.2Test Requirements1888

A.7.3.38E-UTRAN FDD-FDD DC Radio Link Monitoring Test for Out-of-sync in DRX in synchronous DC1888

A.7.3.38.1Test Purpose and Environment1888

A.7.3.38.2Test Requirements1891

A.7.3.39E-UTRAN FDD-FDD DC Radio Link Monitoring Test for Out-of-sync in DRX in asynchronous DC1891

A.7.3.39.1Test Purpose and Environment1891

A.7.3.39.2Test Requirements1894

A.7.3.40E-UTRAN TDD-TDD DC Radio Link Monitoring Test for Out-of-sync in DRX in synchronous DC1895

A.7.3.40.1Test Purpose and Environment1895

A.7.3.40.2Test Requirements1897

A.7.3.41E-UTRAN FDD-FDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity1898

A.7.3.41.1Test Purpose and Environment1898

A.7.3.41.2Test Requirements1901

A.7.3.42E-UTRAN FDD-FDD DC Radio Link Monitoring Test for In-sync in DRX in asynchronous DC1901

A.7.3.42.1Test Purpose and Environment1901

A.7.3.42.2Test Requirements1904

A.7.3.43E-UTRAN TDD-TDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity1904

A.7.3.43.1Test Purpose and Environment1904

A.7.3.43.2Test Requirements1907

A.7.3.44E-UTRAN TDD-FDD DC Radio Link Monitoring Test for Out-of-sync in DRX in synchronous DC with PCell in FDD1907

A.7.3.44.1Test Purpose and Environment1907

A.7.3.44.2Test Requirements1910

A.7.3.45E-UTRAN TDD-FDD DC Radio Link Monitoring Test for Out-of-sync in DRX in synchronous DC with PCell in TDD1911

A.7.3.45.1Test Purpose and Environment1911

A.7.3.45.2Test Requirements1913

A.7.3.46E-UTRAN TDD-FDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in FDD1914

A.7.3.46.1Test Purpose and Environment1914

A.7.3.46.2Test Requirements1917

A.7.3.47E-UTRAN TDD-FDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in TDD1917

A.7.3.47.1Test Purpose and Environment1917

A.7.3.47.2Test Requirements1920

A.7.3.48E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A1920

A.7.3.48.1Test Purpose and Environment1920

A.7.3.48.2Test Requirements1923

A.7.3.49E-UTRAN FD-FDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A1923

A.7.3.49.1Test Purpose and Environment1923

A.7.3.49.2Test Requirements1926

A.7.3.50E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A1926

A.7.3.50.1Test Purpose and Environment1926

A.7.3.50.2Test Requirements1929

A.7.3.51E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A1929

A.7.3.51.1Test Purpose and Environment1929

A.7.3.51.2Test Requirements1932

A.7.3.52E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A1932

A.7.3.52.1Test Purpose and Environment1932

A.7.3.52.2Test Requirements1935

A.7.3.53E-UTRAN HD-FDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A1935

A.7.3.53.1Test Purpose and Environment1935

A.7.3.53.2Test Requirements1938

A.7.3.54E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A1938

A.7.3.54.1Test Purpose and Environment1938

A.7.3.54.2Test Requirements1941

A.7.3.55E-UTRAN HD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A1941

A.7.3.55.1Test Purpose and Environment1941

A.7.3.55.2Test Requirements1944

A.7.3.56E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A1944

A.7.3.56.1Test Purpose and Environment1944

A.7.3.56.2Test Requirements1947

A.7.3.57E-UTRAN TDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A1947

A.7.3.57.1Test Purpose and Environment1947

A.7.3.57.2Test Requirements1950

A.7.3.58E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A1950

A.7.3.58.1Test Purpose and Environment1950

A.7.3.58.2Test Requirements1953

A.7.3.59E-UTRAN TDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A1953

A.7.3.59.1Test Purpose and Environment1953

A.7.3.59.2Test Requirements1956

A.7.3.60HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in normal coverage1956

A.7.3.60.1Test Purpose and Environment1956

A.7.3.60.2Test Requirements1960

A.7.3.61HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage1960

A.7.3.61.1Test Purpose and Environment1960

A.7.3.61.2Test Requirements1964

A.7.3.62HD-FDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 In-Band mode in Enhanced Coverage1964

A.7.3.62.1Test Purpose and Environment1964

A.7.3.62.2Test Requirements1968

A.7.3.63HD-FDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 In-Band mode in Normal Coverage1968

A.7.3.63.1Test Purpose and Environment1968

A.7.3.63.2Test Requirements1972

A.7.3.64HD-FDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 In-Band mode in Normal Coverage1972

A.7.3.64.1Test Purpose and Environment1972

A.7.3.64.2Test Requirements1975

A.7.3.65HD-FDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 In-Band mode in Enhanced Coverage1976

A.7.3.65.1Test Purpose and Environment1976

A.7.3.65.2Test Requirements1979

A.7.3.66HD-FDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 Standalone mode in Normal Coverage1980

A.7.3.66.1Test Purpose and Environment1980

A.7.3.66.2Test Requirements1982

A.7.3.67HD-FDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 guard band mode in Enhanced Coverage1983

A.7.3.67.1Test Purpose and Environment1983

A.7.3.67.2Test Requirements1986

A.7.3.68E-UTRAN FD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEMode A1987

A.7.3.68.1Test Purpose and Environment1987

A.7.3.68.2Test Requirements1989

A.7.3.69E-UTRAN HD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEMode A1989

A.7.3.69.1Test Purpose and Environment1989

A.7.3.69.2Test Requirements1991

A.7.3.70E-UTRAN TDD Early Out-of-sync reporting Test for Cat-M1 UE in CEMode A1991

A.7.3.70.1Test Purpose and Environment1991

A.7.3.70.2Test Requirements1993

A.7.3.71E-UTRAN FD-FDD Early In-Sync reporting Test for Cat-M1 UE in CEModeA1993

A.7.3.71.1Test Purpose and Environment1993

A.7.3.71.2Test Requirements1996

A.7.3.72E-UTRAN HD-FDD Early In-Sync reporting Test for Cat-M1 UE in CEModeA1996

A.7.3.72.1Test Purpose and Environment1996

A.7.3.72.2Test Requirements1998

A.7.3.73E-UTRAN TDD Early In-Sync reporting Test for Cat-M1 UE in CEModeA1998

A.7.3.73.1Test Purpose and Environment1998

A.7.3.73.2Test Requirements2000

A.7.3.74E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for non-BL CE UE in CEMode A2000

A.7.3.74.1Test Purpose and Environment2000

A.7.3.74.2Test Requirements2003

A.7.3.75E-UTRAN FD-FDD Radio Link Monitoring Test for In-Sync for non-BL CE UE in CEMode A2003

A.7.3.75.1Test Purpose and Environment2003

A.7.3.75.2Test Requirements2005

A.7.3.76E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for non-BL CE UE configured in CEMode A2006

A.7.3.76.1Test Purpose and Environment2006

A.7.3.76.2Test Requirements2009

A.7.3.77E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync in DRX for non-BL CE UE configured in CEMode A2009

A.7.3.77.1Test Purpose and Environment2009

A.7.3.77.2Test Requirements2012

A.7.3.78E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync for non-BL CE UE in CEMode A2012

A.7.3.78.1Test Purpose and Environment2012

A.7.3.78.2Test Requirements2015

A.7.3.79E-UTRAN TDD Radio Link Monitoring Test for In-Sync for non-BL CE UE in CEMode A2015

A.7.3.79.1Test Purpose and Environment2015

A.7.3.79.2Test Requirements2018

A.7.3.80E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync in DRX for non-BL CE UE configured in CEMode A2018

A.7.3.80.1Test Purpose and Environment2018

A.7.3.80.2Test Requirements2021

A.7.3.81E-UTRAN TDD Radio Link Monitoring Test for In-sync in DRX for non-BL CE UE configured in CEMode A2021

A.7.3.81.1Test Purpose and Environment2021

A.7.3.81.2Test Requirements2024

A.7.3.82E-UTRAN FD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB2024

A.7.3.82.1Test Purpose and Environment2024

A.7.3.82.2Test Requirements2027

A.7.3.83E-UTRAN FD-FDD Early In-Sync reporting Test for Cat-M1 UE in CEModeB2027

A.7.3.83.1Test Purpose and Environment2027

A.7.3.83.2Test Requirements2028

A.7.3.84E-UTRAN HD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB2029

A.7.3.84.1Test Purpose and Environment2029

A.7.3.84.2Test Requirements2031

A.7.3.85E-UTRAN HD-FDD Early In-Sync reporting Test for Cat-M1 UE in CEModeB2031

A.7.3.85.1Test Purpose and Environment2031

A.7.3.85.2Test Requirements2032

A.7.3.86E-UTRAN TDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB2033

A.7.3.86.1Test Purpose and Environment2033

A.7.3.86.2Test Requirements2035

A.7.3.87E-UTRAN TDD Early In-Sync reporting Test for Cat-M1 UE in CEModeB2035

A.7.3.87.1Test Purpose and Environment2035

A.7.3.87.2Test Requirements2037

A.7.3.88TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in normal coverage2038

A.7.3.88.1Test Purpose and Environment2038

A.7.3.88.2Test Requirements2042

A.7.3.89TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage2042

A.7.3.89.1Test Purpose and Environment2042

A.7.3.89.2Test Requirements2046

A.7.3.90TDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 In-Band mode in Normal Coverage2046

A.7.3.90.1Test Purpose and Environment2046

A.7.3.90.2Test Requirements2050

A.7.3.91TDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 In-Band mode in Enhanced Coverage2050

A.7.3.91.1Test Purpose and Environment2050

A.7.3.91.2Test Requirements2054

A.7.3.92TDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 In-Band mode in Normal Coverage2054

A.7.3.92.1Test Purpose and Environment2054

A.7.3.92.2Test Requirements2057

A.7.3.93TDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 In-Band mode in Enhanced Coverage2058

A.7.3.93.1Test Purpose and Environment2058

A.7.3.93.2Test Requirements2061

A.7.3.94TDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 Standalone mode in Normal Coverage2062

A.7.3.94.1Test Purpose and Environment2062

A.7.3.94.2Test Requirements2064

A.7.3.95TDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 guard band mode in Enhanced Coverage2065

A.7.3.95.1Test Purpose and Environment2065

A.7.3.95.2Test Requirements2068

A.7.3.96E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for MPDCCH performance improvement2069

A.7.3.96.1Test Purpose and Environment2069

A.7.3.97E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for MPDCCH performance improvement2070

A.7.3.97.1Test Purpose and Environment2070

A.7.3.97.2Test Requirements2073

A.7.3.98E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for MPDCCH performance improvement2073

A.7.3.98.1Test Purpose and Environment2073

A.7.3.98.2Test Requirements2076

A.7.3.99E-UTRAN FD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB for MPDCCH performance improvement2076

A.7.3.99.1Test Purpose and Environment2076

A.7.3.99.2Test Requirements2079

A.7.3.100E-UTRAN HD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB for MPDCCH performance improvement2079

A.7.3.100.1Test Purpose and Environment2079

A.7.3.100.2Test Requirements2081

A.7.3.101E-UTRAN TDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB for MPDCCH performance improvement2081

A.7.3.101.1Test Purpose and Environment2081

A.7.3.101.2Test Requirements2083

A.7.4Interruption for Dual Connectivity2083

A.7.4.1E-UTRAN FDD-FDD DC interruption at transitions between active and non-active during DRX in synchronous DC2083

A.7.4.1.1Test Purpose and Environment2083

A.7.4.1.2Test Requirements2086

A.7.4.2E-UTRAN TDD-TDD DC interruption at transitions between active and non-active during DRX in synchronous DC2086

A.7.4.2.1Test Purpose and Environment2086

A.7.4.2.2Test Requirements2088

A.7.4.3E-UTRAN FDD-FDD Interruption at transitions between active and non-active during DRX in asynchronous dual connectivity2088

A.7.4.3.1Test Purpose and Environment2088

A.7.4.3.2Test Requirements2090

A.7.4.4E-UTRAN FDD-TDD DC interruption at transitions between active and non-active during DRX in synchronous DC2090

A.7.4.4.1Test Purpose and Environment2090

A.7.4.4.2Test Requirements2093

A.7.4.5E-UTRAN TDD-FDD DC interruption at transitions between active and non-active during DRX in synchronous DC2093

A.7.4.5.1Test Purpose and Environment2093

A.7.4.5.2Test Requirements2095

A.7.4.6E-UTRAN FDD-TDD DC interruption at SRS carrier based switching2095

A.7.4.6.1Test Purpose and Environment2095

A.7.4.6.2Test Requirements2097

A.7.4.7E-UTRAN TDD-TDD DC interruption at SRS carrier based switching2097

A.7.4.7.1Test Purpose and Environment2097

A.7.4.7.2Test Requirements2101

A.7.5Proximity-based Services2101

A.7.5.1E-UTRAN FDD – UE ProSe Direct Discovery Transmission Timing Accuracy Test2101

A.7.5.1.1Test Purpose and Environment2101

A.7.5.1.2Test Requirements2102

A.7.5.2E-UTRAN TDD – UE ProSe Direct Discovery Transmission Timing Accuracy Test2103

A.7.5.2.1Test Purpose and Environment2103

A.7.5.1.2Test Requirements2103

A.7.5.3E-UTRAN FDD - Interruptions due to ProSe Direct Discovery2104

A.7.5.3.1Test Purpose and Environment2104

A.7.5.3.2Test Requirements2105

A.7.5.4E-UTRAN FDD – UE ProSe Direct Communication Transmission Timing Accuracy Test2106

A.7.5.4.1Test Purpose and Environment2106

A.7.5.4.2Test Requirements2107

A.7.5.5E-UTRAN FDD - Interruptions due to ProSe Direct Communication2108

A.7.5.5.1Test Purpose and Environment2108

A.7.5.5.2Test Requirements2110

A.7.5.6E-UTRAN FDD - Interruptions due to ProSe Direct Discovery with discovery period less than 320ms2111

A.7.5.6.1Test Purpose and Environment2111

A.7.5.6.2Test Requirements2112

A.7.5.7E-UTRAN FDD-FDD - Interruptions due to ProSe Direct Discovery2113

A.7.5.7.1Test Purpose and Environment2113

A.7.5.7.2Test Requirements2115

A.7.5.8E-UTRAN FDD-FDD - Cell reselection and timing accuracy for ProSe Direct Discovery transmission on non-serving frequency2115

A.7.5.8.1Test Purpose and Environment2115

A.7.5.8.2Test Requirements2117

A.7.5.9E-UTRAN FDD-FDD - Interruptions due to ProSe Direct Discovery reception on non-serving frequency2118

A.7.5.9.1Test Purpose and Environment2118

A.7.5.9.2Test Requirements2120

A.7.5.10E-UTRAN FDD-FDD - Interruptions due to ProSe Direct Discovery transmission on non-serving frequency2121

A.7.5.10.1Test Purpose and Environment2121

A.7.5.10.2Test Requirements2123

A.7.5.11E-UTRAN FDD-FDD - Interruptions due to ProSe Direct Communication on non-serving frequency2124

A.7.5.11.1Test Purpose and Environment2124

A.7.5.11.2Test Requirements2126

A.7.5.12E-UTRAN FDD - Selection / Reselection of ProSe relay UE2126

A.7.5.12.1Test Purpose and Environment2126

A.7.5.12.2Test Requirements2130

A.7.6Interruption for carrier aggregation2131

A.7.6.1E-UTRAN FDD-TDD CA interruption at SRS carrier based switching2131

A.7.6.1.1Test Purpose and Environment2131

A.7.6.1.2Test Requirements2134

A.7.6.2E-UTRAN TDD-TDD CA interruption at SRS carrier based switching2134

A.7.6.2.1Test Purpose and Environment2134

A.7.6.2.2Test Requirements2137

A.8UE Measurements Procedures2138

A.8.1E-UTRAN FDD Intra-frequency Measurements2138

A.8.1.1E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells2138

A.8.1.1.1Test Purpose and Environment2138

A.8.1.1.2Test Requirements2139

A.8.1.2E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells2140

A.8.1.2.1Test Purpose and Environment2140

A.8.1.2.2Test Requirements2141

A.8.1.3E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells with DRX2142

A.8.1.3.1Test Purpose and Environment2142

A.8.1.3.2Test Requirements2144

A.8.1.4Void2144

A.8.1.5E-UTRAN FDD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps2144

A.8.1.5.1Test Purpose and Environment2144

A.8.1.5.2Test Requirements2146

A.8.1.6E-UTRAN FDD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX2146

A.8.1.6.1Test Purpose and Environment2146

A.8.1.6.2Test Requirements2148

A.8.1.7 E-UTRAN FDD-FDD Intra-Frequency Event-Triggered Reporting under Time Domain Measurement Resource Restriction with Non-MBSFN ABS2148

A.8.1.7.1Test Purpose and Environment2148

A.8.1.7.2Test Requirements2150

A.8.1.8E-UTRAN FDD-FDD Intra-Frequency Event-Triggered Reporting under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS2151

A.8.1.8.1Test Purpose and Environment2151

A.8.1.8.2Test Requirements2153

A.8.1.9E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for 5MHz bandwidth2154

A.8.1.9.1Test Purpose and Environment2154

A.8.1.9.2Test Requirements2154

A.8.1.10E-UTRAN FDD-FDD Intra-Frequency Event Triggered Reporting under Fading Propagation Conditions in Synchronous Cells with DRX for 5 MHz Bandwidth2154

A.8.1.10.1Test Purpose and Environment2154

A.8.1.10.2Test Requirements2155

A.8.1.11E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category 02155

A.8.1.11.1Test Purpose and Environment2155

A.8.1.11.2Test Requirements2157

A.8.1.12E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for UE category 02158

A.8.1.12.1Test Purpose and Environment2158

A.8.1.12.2Test Requirements2159

A.8.1.13E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells with DRX for UE category 02160

A.8.1.13.1Test Purpose and Environment2160

A.8.1.13.2Test Requirements2162

A.8.1.14E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category 02162

A.8.1.14.1Test Purpose and Environment2162

A.8.1.14.2Test Requirements2164

A.8.1.15E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for UE category 02165

A.8.1.15.1Test Purpose and Environment2165

A.8.1.15.2Test Requirements2166

A.8.1.16E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells with DRX for UE category 02167

A.8.1.16.1Test Purpose and Environment2167

A.8.1.16.2Test Requirements2169

A.8.1.17Void2169

A.8.1.18Void2169

A.8.1.19E-UTRAN FDD-FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps for UE category 02169

A.8.1.19.1Test Purpose and Environment2169

A.8.1.19.2Test Requirements2171

A.8.1.20E-UTRAN FDD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX for UE category 02172

A.8.1.20.1Test Purpose and Environment2172

A.8.1.20.2Test Requirements2174

A.8.1.21E-UTRAN HD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps for UE category 02174

A.8.1.21.1Test Purpose and Environment2174

A.8.1.21.2Test Requirements2176

A.8.1.22E-UTRAN HD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX for UE category 02177

A.8.1.22.1Test Purpose and Environment2177

A.8.1.22.2Test Requirements2179

A.8.1.23E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for Cat-M1 UE in CEModeA2179

A.8.1.23.1Test Purpose and Environment2179

A.8.1.23.2Test Requirements2180

A.8.1.24E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeA2181

A.8.1.24.1Test Purpose and Environment2181

A.8.1.24.2Test Requirements2183

A.8.1.25E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeA in DRX2183

A.8.1.25.1Test Purpose and Environment2183

A.8.1.25.2Test Requirements2185

A.8.1.26E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for Cat-M1 UE in CEModeA2185

A.8.1.26.1Test Purpose and Environment2185

A.8.1.27E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeA2188

A.8.1.27.1Test Purpose and Environment2188

A.8.1.27.2Test Requirements2190

A.8.1.28E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeA in DRX2190

A.8.1.28.1Test Purpose and Environment2190

A.8.1.28.2Test Requirements2192

A.8.1.29E-UTRAN TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeA2192

A.8.1.29.1Test Purpose and Environment2192

A.8.1.29.2Test Requirements2194

A.8.1.30E-UTRAN TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeA in DRX2195

A.8.1.30.1Test Purpose and Environment2195

A.8.1.30.2Test Requirements2197

A.8.1.31 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for Cat-M1 UE in CEModeB2197

A.8.1.31.1Test Purpose and Environment2197

A.8.1.31.2Test Requirements2199

A.8.1.32 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeB2200

A.8.1.32.1Test Purpose and Environment2200

A.8.1.32.2Test Requirements2201

A.8.1.33E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for Cat-M1 UE in CEModeB2202

A.8.1.33.1Test Purpose and Environment2202

A.8.1.33.2Test Requirements2203

A.8.1.34E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeB2204

A.8.1.34.1Test Purpose and Environment2204

A.8.1.34.2Test Requirements2205

A.8.1.35E-UTRAN TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeB2206

A.8.1.35.1Test Purpose and Environment2206

A.8.1.35.2Test Requirements2207

A.8.1.36E-UTRAN FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps for Cat-M1 UE in CEModeB2208

A.8.1.36.1Test Purpose and Environment2208

A.8.1.36.2Test Requirements2209

A.8.1.37E-UTRAN FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX for Cat-M1 UE in CEModeB2210

A.8.1.37.1Test Purpose and Environment2210

A.8.1.37.2Test Requirements2212

A.8.1.38E-UTRAN HD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps for Cat-M1 UE in CEModeB2212

A.8.1.38.1Test Purpose and Environment2212

A.8.1.38.2Test Requirements2213

A.8.1.39E-UTRAN HD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX for Cat-M1 UE in CEModeB2214

A.8.1.39.1Test Purpose and Environment2214

A.8.1.39.2Test Requirements2216

A.8.1.40E-UTRAN FDD-FDD intra-frequency event triggered reporting with DRX for UE configured with highSpeedEnhancedMeasFlag2216

A.8.1.40.1Test Purpose and Environment2216

A.8.1.40.2Test Requirements2218

A.8.1.41E-UTRAN FDD intra-frequency event triggered reporting for serving cell under fading propagation conditions for UE category M1 in CEModeA without gap2218

A.8.1.41.1Test Purpose and Environment2218

A.8.1.41.2Test Requirement2220

A.8.1.42E-UTRAN HD-FDD intra-frequency event triggered reporting for serving cell under fading propagation conditions for UE category M1 in CEModeA without gap2220

A.8.1.42.1Test Purpose and Environment2220

A.8.1.42.2Test Requirement2221

A.8.1.43E-UTRAN FDD-FDD intra-frequency event triggered reporting with DRX for UE configured with highSpeedEnhMeasFlag2-r162221

A.8.1.43.1Test Purpose and Environment2221

A.8.1.43.2Test Requirements2224

A.8.1.44HD-FDD Intra-frequency neighbour cell measurement for UE category NB1 in In-Band mode under normal coverage2224

A.8.1.44.1Test Purpose and Environment2224

A.8.1.44.2Test Requirements2227

A.8.1.45HD-FDD Intra-frequency neighbour cell measurement for UE category NB1 in guard-band mode under normal coverage2228

A.8.1.45.1Test Purpose and Environment2228

A.8.1.45.2Test Requirements2230

A.8.1.46HD-FDD Intra-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage2231

A.8.1.46.1Test Purpose and Environment2231

A.8.1.46.2Test Requirements2232

A.8.1.47TDD Intra-frequency neighbour cell measurement for UE category NB1 in In-Band mode under normal coverage2233

A.8.1.47.1Test Purpose and Environment2233

A.8.1.47.2Test Requirements2235

A.8.1.48TDD Intra-frequency neighbour cell measurement for UE category NB1 in guard-band mode under normal coverage2236

A.8.1.48.1Test Purpose and Environment2236

A.8.1.48.2Test Requirements2238

A.8.1.49TDD Intra-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage2239

A.8.1.49.1Test Purpose and Environment2239

A.8.1.49.2Test Requirements2240

A.8.150HD-FDD Inter-frequency neighbour cell measurement for UE category NB1 in In-Band mode under normal coverage2241

A.8.1.50.1Test Purpose and Environment2241

A.8.1.50.2Test Requirements2243

A.8.1.51HD-FDD Inter-frequency neighbour cell measurement for UE category NB1 in guard-band mode under normal coverage2244

A.8.1.51.1Test Purpose and Environment2244

A.8.1.51.2Test Requirements2246

A.8.1.52HD-FDD Inter-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage2247

A.8.1.52.1Test Purpose and Environment2247

A.8.1.52.2Test Requirements2248

A.8.1.53TDD Inter-frequency neighbour cell measurement for UE category NB1 in In-Band mode under normal coverage2249

A.8.1.53.1Test Purpose and Environment2249

A.8.1.53.2Test Requirements2251

A.8.1.54TDD Inter-frequency neighbour cell measurement for UE category NB1 in guard-band mode under normal coverage2252

A.8.1.54.1Test Purpose and Environment2252

A.8.1.54.2Test Requirements2254

A.8.1.55TDD Inter-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage2255

A.8.1.55.1Test Purpose and Environment2255

A.8.1.55.2Test Requirements2256

A.8.2E-UTRAN TDD Intra-frequency Measurements2257

A.8.2.1E-UTRAN TDD-TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells2257

A.8.2.1.1Test Purpose and Environment2257

A.8.2.1.2Test Requirements2258

A.8.2.2E-UTRAN TDD-TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells with DRX2258

A.8.2.2.1Test Purpose and Environment2258

A.8.2.2.2Test Requirements2261

A.8.2.3E-UTRAN TDD - TDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps2261

A.8.2.3.1Test Purpose and Environment2261

A.8.2.3.2Test Requirements2263

A.8.2.4E-UTRAN TDD - TDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX2264

A.8.2.4.1Test Purpose and Environment2264

A.8.2.4.2Test Requirements2266

A.8.2.5E-UTRAN TDD-TDD Intra-Frequency Event-Triggered Reporting under Time Domain Measurement Resource Restriction with Non-MBSFN ABS2266

A.8.2.5.1Test Purpose and Environment2266

A.8.2.5.2Test Requirements2268

A.8.2.6E-UTRAN TDD-TDD Intra-Frequency Event-Triggered Reporting under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS2269

A.8.2.6.1Test Purpose and Environment2269

A.8.2.6.2Test Requirements2272

A.8.2.7E-UTRAN TDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps2273

A.8.2.7.1Test Purpose and Environment2273

A.8.2.7.2Test Requirements2274

A.8.2.8E-UTRAN TDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX2275

A.8.2.8.1Test Purpose and Environment2275

A.8.2.8.2Test Requirements2277

A.8.2.9E-UTRAN TDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps for Cat-M1 UE in CEModeB2277

A.8.2.9.1Test Purpose and Environment2277

A.8.2.9.2Test Requirements2279

A.8.2.10E-UTRAN TDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX for Cat-M1 UE in CEModeB2280

A.8.2.10.1Test Purpose and Environment2280

A.8.2.10.2Test Requirements2282

A.8.2.11E-UTRAN TDD-TDD intra-frequency event triggered reporting with DRX for UE configured with highSpeedEnhancedMeasFlag2282

A.8.2.11.1Test Purpose and Environment2282

A.8.2.11.2Test Requirements2284

A.8.2.12E-UTRAN TDD-TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for UE category 02284

A.8.2.12.1Test Purpose and Environment2284

A.8.2.12.2Test Requirements2286

A.8.2.13E-UTRAN TDD-TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells with DRX for UE category 02287

A.8.2.13.1Test Purpose and Environment2287

A.8.2.13.2Test Requirements2289

A.8.2.14E-UTRAN TDD intra-frequency event triggered reporting for serving cell under fading propagation conditions for UE category M1 in CEModeA without gap2289

A.8.2.14.1Test Purpose and Environment2289

A.8.2.14.2Test Requirement2291

A.8.2.15E-UTRAN TDD-TDD intra-frequency event triggered reporting with DRX for UE configured with highSpeedEnhMeasFlag2-r162291

A.8.2.15.1Test Purpose and Environment2291

A.8.2.15.2Test Requirements2293

A.8.3E-UTRAN FDD - FDD Inter-frequency Measurements2293

A.8.3.1E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells2293

A.8.3.1.1Test Purpose and Environment2293

A.8.3.1.2Test Requirements2295

A.8.3.2E-UTRAN FDD-FDD Inter-frequency event triggered reporting when DRX is used under fading propagation conditions in asynchronous cells2295

A.8.3.2.1Test Purpose and Environment2295

A.8.3.2.2Test Requirements2298

A.8.3.3E-UTRAN FDD-FDD inter-frequency event triggered reporting under AWGN propagation conditions in asynchronous cells with DRX when L3 filtering is used2298

A.8.3.3.1Test Purpose and Environment2298

A.8.3.3.2Test Requirements2301

A.8.3.4E-UTRAN FDD - FDD Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps2301

A.8.3.4.1Test Purpose and Environment2301

A.8.3.4.2Test Requirements2303

A.8.3.5E-UTRAN FDD - FDD Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX2303

A.8.3.5.2Test Requirements2305

A.8.3.6E-UTRAN FDD-FDD Inter-frequency event triggered reporting without measurement gaps under AWGN propagation conditions in asynchronous cells2305

A.8.3.6.1Test Purpose and Environment2305

A.8.3.6.2Test Requirements2307

A.8.3.7E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for Increased Carrier Monitoring without Reduced Performance Group2308

A.8.3.7.1Test Purpose and Environment2308

A.8.3.7.2Test Requirements2310

A.8.3.8FDD-FDD Interfrequency correct reporting of measurement events with reduced performance group configured, non DRX2311

A.8.3.8.1Test Purpose and Environment2311

A.8.3.8.2Test Requirements2314

A.8.3.9FDD-FDD Inter-frequency correct reporting of measurement events with reduced performance group configured, DRX2314

A.8.3.9.1Test Purpose and Environment2314

A.8.3.9.2Test Requirements2318

A.8.3.10E-UTRAN FDD-FDD Inter-frequency event triggered reporting with MGL=3ms under fading propagation conditions in synchronous cells2319

A.8.3.10.1Test Purpose and Environment2319

A.8.3.10.2Test Requirements2320

A.8.3.11E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells with burst gap2320

A.8.3.11.1Test Purpose and Environment2320

A.8.3.11.2Test Requirement2322

A.8.3.12E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeA2323

A.8.3.12.1Test Purpose and Environment2323

A.8.3.12.2Test Requirement2324

A.8.3.13E-UTRAN HD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeA2325

A.8.3.13.1Test Purpose and Environment2325

A.8.3.13.2Test Requirement2326

A.8.3.14E-UTRAN FDD-FDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeB2327

A.8.3.14.1Test Purpose and Environment2327

A.8.3.14.2Test Requirement2328

A.8.3.15E-UTRAN HD-FDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeB2329

A.8.3.15.1Test Purpose and Environment2329

A.8.3.15.2Test Requirement2330

A.8.3.16E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 in CEModeA when DRX is used2331

A.8.3.16.1Test Purpose and Environment2331

A.8.3.16.2Test Requirement2333

A.8.3.17E-UTRAN HD-FDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 in CEModeA in DRX2333

A.8.3.17.1Test Purpose and Environment2333

A.8.3.17.2Test Requirement2336

A.8.3.18E-UTRAN FDD-FDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 in CEModeB in DRX2336

A.8.3.18.1Test Purpose and Environment2336

A.8.3.18.2Test Requirement2339

A.8.3.19E-UTRAN HD-FDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 in CEModeB in DRX2339

A.8.3.19.1Test Purpose and Environment2339

A.8.3.19.2Test Requirement2342

A.8.4E-UTRAN TDD - TDD Inter-frequency Measurements2342

A.8.4.1E-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells2342

A.8.4.1.1Test Purpose and Environment2342

A.8.4.1.2Test Requirements2344

A.8.4.2E-UTRAN TDD-TDD Inter-frequency event triggered reporting when DRX is used under fading propagation conditions in synchronous cells2344

A.8.4.2.1Test Purpose and Environment2344

A.8.4.2.2Test Requirements2347

A.8.4.3E-UTRAN TDD-TDD inter-frequency event triggered reporting under AWGN propagation conditions in synchronous cells with DRX when L3 filtering is used2347

A.8.4.3.1Test Purpose and Environment2347

A.8.4.3.2Test Requirements2349

A.8.4.4E-UTRAN TDD - TDD Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps2350

A.8.4.4.1Test Purpose and Environment2350

A.8.4.4.2Test Requirements2352

A.8.4.5E-UTRAN TDD - TDD Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX2353

A.8.4.5.1Test Purpose and Environment2353

A.8.4.5.2Test Requirements2355

A.8.4.6E-UTRAN TDD-TDD Inter-frequency event triggered reporting for TDD UL/DL configuration 02355

A.8.4.6.1Test Purpose and Environment2355

A.8.4.6.2Test Requirements2356

A.8.4.7E-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells for Increased Carrier Monitoring without Reduced Performance Group2356

A.8.4.7.1Test Purpose and Environment2356

A.8.4.7.2Test Requirements2360

A.8.4.8TDD-TDD Interfrequency correct reporting of measurement events with reduced performance group configured, non DRX2360

A.8.4.8.1Test Purpose and Environment2360

A.8.4.8.2Test Requirements2363

A.8.4.9TDD-TDD Inter-frequency correct reporting of measurement events with reduced performance group configured, DRX2363

A.8.4.9.1Test Purpose and Environment2363

A.8.4.9.2Test Requirements2368

A.8.4.10E-UTRAN TDD-TDD Inter-frequency event triggered reporting with MGL=3ms under fading propagation conditions in synchronous cells2368

A.8.4.10.1Test Purpose and Environment2368

A.8.4.10.2Test Requirements2370

A.8.4.11E-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells with burst gap2370

A.8.4.11.1Test Purpose and Environment2370

A.8.4.11.2Test Requirement2372

A.8.4.12E-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeA2372

A.8.4.12.1Test Purpose and Environment2372

A.8.4.12.2Test Requirement2374

A.8.4.13E-UTRAN TDD-TDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeB2375

A.8.4.13.1Test Purpose and Environment2375

A.8.4.13.2Test Requirement2376

A.8.4.14E-UTRAN TDD-TDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 in CEModeA in DRX2377

A.8.4.14.1Test Purpose and Environment2377

A.8.4.14.2Test Requirement2379

A.8.4.15E-UTRAN TDD-TDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 in CEModeB in DRX2379

A.8.4.15.1Test Purpose and Environment2379

A.8.4.15.2Test Requirement2382

A.8.5E-UTRAN FDD - UTRAN FDD Measurements2382

A.8.5.1E-UTRAN FDD - UTRAN FDD event triggered reporting under fading propagation conditions2382

A.8.5.1.1Test Purpose and Environment2382

A.8.5.1.2Test Requirements2384

A.8.5.2E-UTRAN FDD - UTRAN FDD SON ANR cell search reporting under AWGN propagation conditions2384

A.8.5.2.1Test Purpose and Environment2384

A.8.5.2.2Test Requirements2386

A.8.5.3E-UTRAN FDD-UTRAN FDD event triggered reporting when DRX is used under fading propagation conditions2386

A.8.5.3.1Test Purpose and Environment2386

A.8.5.3.2Test Requirements2389

A.8.5.4E-UTRAN FDD - UTRAN FDD enhanced cell identification under AWGN propagation conditions2389

A.8.5.4.1Test Purpose and Environment2389

A.8.5.4.2Test Requirements2391

A.8.5.5E- UTRAN FDD - UTRAN FDD identification of a new CGI of UTRAN cell using autonomous gaps2391

A.8.5.5.1Test Purpose and Environment2391

A.8.5.5.2Test Requirements2394

A.8.5.6E-UTRAN FDD - UTRAN FDD event triggered reporting without measurement gaps under AWGN propagation conditions2394

A.8.5.6.1Test Purpose and Environment2394

A.8.5.6.2Test Requirements2395

A.8.5.7E-UTRAN FDD - UTRAN FDD Event Triggered Reporting under Fading Propagation Conditions for 5 MHz Bandwidth2396

A.8.5.7.1Test Purpose and Environment2396

A.8.5.7.2Test Requirements2396

A.8.5.8E-UTRA FDD InterRAT UTRA FDD correct reporting of measurement events with reduced performance group configured, non DRX2396

A.8.5.8.1Test Purpose and Environment2396

A.8.5.8.2Test Requirements2399

A.8.6E-UTRAN TDD - UTRAN FDD Measurements2399

A.8.6.1E-UTRAN TDD - UTRAN FDD event triggered reporting under fading propagation conditions2399

A.8.6.1.1Test Purpose and Environment2399

A.8.6.1.2Test Requirements2401

A.8.6.2E- UTRAN TDD - UTRAN FDD identification of a new CGI of UTRAN cell using autonomous gaps2401

A.8.6.2.1Test Purpose and Environment2401

A.8.6.2.2Test Requirements2404

A.8.6.3E-UTRA TDD InterRAT UTRA FDD correct reporting of measurement events with reduced performance group configured, non DRX2404

A.8.6.3.1Test Purpose and Environment2404

A.8.6.3.2Test Requirements2407

A.8.7E-UTRAN TDD – UTRAN TDD Measurements2407

A.8.7.1E-UTRAN TDD to UTRAN TDD cell search under fading propagation conditions2407

A.8.7.1.1Test Purpose and Environment2407

A.8.7.1.1.1Void2407

A.8.7.1.1.21.28 Mcps TDD option2407

A.8.7.1.1.3Void2409

A.8.7.1.2Test Requirements2409

A.8.7.1.2.1Void2409

A.8.7.1.2.21.28 Mcps TDD option2409

A.8.7.1.2.3Void2409

A.8.7.2E-UTRAN TDD-UTRAN TDD cell search when DRX is used under fading propagation conditions2409

A.8.7.2.1Test Purpose and Environment2409

A.8.7.2.2Test Requirements2412

A.8.7.3E-UTRAN TDD - UTRAN TDD SON ANR cell search reporting in AWGN propagation conditions2413

A.8.7.3.1Test Purpose and Environment2413

A.8.7.3.2Test Parameters2413

A.8.7.3.3Test Requirements2414

A.8.7.4E-UTRAN TDD - UTRAN TDD enhanced cell identification under AWGN propagation conditions2415

A.8.7.4.1Test Purpose and Environment2415

A.8.7.4.2Test Requirements2417

A.8.7.5E-UTRA TDD InterRAT UTRA TDD correct reporting of measurement events with reduced performance group configured, non DRX2417

A.8.7.5.1Test Purpose and Environment2417

A.8.7.5.2Test Requirements2419

A.8.7AE-UTRAN FDD – UTRAN TDD Measurements2419

A.8.7A.1E-UTRA FDD InterRAT UTRA TDD correct reporting of measurement events with reduced performance group configured, non DRX2419

A.8.7A.1.1Test Purpose and Environment2419

A.8.7A.1.2Test Requirements2422

A.8.8E-UTRAN FDD – GSM Measurements2422

A.8.8.1E-UTRAN FDD – GSM event triggered reporting in AWGN2422

A.8.8.1.1Test Purpose and Environment2422

A.8.8.1.2Test Requirements2424

A.8.8.2E-UTRAN FDD-GSM event triggered reporting when DRX is used in AWGN2424

A.8.8.2.1Test Purpose and Environment2424

A.8.8.2.2Test Requirements2426

A.8.8.3E-UTRAN FDD – GSM event triggered reporting in AWGN with enhanced BSIC identification2427

A.8.8.3.1Test Purpose and Environment2427

A.8.8.3.2Test Requirements2428

A.8.9E-UTRAN FDD - UTRAN TDD measurements2429

A.8.9.1E-UTRAN FDD - UTRAN TDD event triggered reporting in fading propagation conditions2429

A.8.9.1.1Test Purpose and Environment2429

A.8.9.1.2Test Requirements2430

A.8.9.2E-UTRAN FDD - UTRAN TDD enhanced cell identification under AWGN propagation conditions2431

A.8.9.2.1Test Purpose and Environment2431

A.8.9.2.2Test Requirements2433

A.8.10E-UTRAN TDD – GSM Measurements2433

A.8.10.1E-UTRAN TDD – GSM event triggered reporting in AWGN2433

A.8.10.1.1Test Purpose and Environment2433

A.8.10.1.2Test Requirements2434

A.8.10.2E-UTRAN TDD-GSM event triggered reporting when DRX is used in AWGN2435

A.8.10.2.1Test Purpose and Environment2435

A.8.10.2.2Test Requirements2437

A.8.11Monitoring of Multiple Layers2437

A.8.11.1Multiple E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions2437

A.8.11.1.1Test Purpose and Environment2437

A.8.11.1.2Test Requirements2439

A.8.11.2E-UTRAN TDD – E-UTRAN TDD and E-UTRAN TDD Inter-frequency event triggered reporting under fading propagation conditions2440

A.8.11.2.1Test Purpose and Environment2440

A.8.11.2.2Test Requirements2441

A.8.11.3E-UTRAN FDD-FDD Inter-frequency and UTRAN FDD event triggered reporting under fading propagation conditions2442

A.8.11.3.1Test Purpose and Environment2442

A.8.11.3.2Test Requirements2444

A.8.11.4InterRAT E-UTRA TDD to E-UTRA TDD and UTRA TDD cell search test case2444

A.8.11.4.1Test Purpose and Environment2444

A.8.11.4.2Test Requirements2447

A.8.11.5Combined E-UTRAN FDD – E-UTRA FDD and GSM cell search. E-UTRA cells in fading; GSM cell in static propagation conditions2447

A.8.11.5.1Test Purpose and Environment2447

A.8.11.5.2Test Requirements2449

A.8.11.6Combined E-UTRAN TDD – E-UTRA TDD and GSM cell search. E-UTRA cells in fading; GSM cell in static propagation conditions2450

A.8.11.6.1Test Purpose and Environment2450

A.8.11.6.2Test Requirements2452

A.8.12RSTD Intra-frequency Measurements2453

A.8.12.1E-UTRAN FDD intra-frequency RSTD measurement reporting delay test case2453

A.8.12.1.1Test Purpose and Environment2453

A.8.12.1.2Test Requirements2457

A.8.12.1.2ATest Requirements for UE Category 1bis2457

A.8.12.2E-UTRAN TDD intra-frequency RSTD measurement reporting delay test case2457

A.8.12.2.1Test Purpose and Environment2457

A.8.12.2.2Test Requirements2462

A.8.12.2.2ATest Requirements for UE Category 1bis2462

A.8.12.3E-UTRAN FDD intra-frequency RSTD measurement period test case in CE Mode A2462

A.8.12.3.1Test Purpose and Environment2462

A.8.12.3.2Test Requirements2468

A.8.12.4E-UTRAN HD-FDD intra-frequency RSTD measurement period test case in CE Mode A2468

A.8.12.4.1Test Purpose and Environment2468

A.8.12.4.2Test Requirements2473

A.8.12.5E-UTRAN TDD intra-frequency RSTD measurement period test case in CE Mode A2473

A.8.12.5.1Test Purpose and Environment2473

A.8.12.5.2Test Requirements2478

A.8.12.6E-UTRAN FDD intra-frequency RSTD measurement period test case in CE Mode B2478

A.8.12.6.1Test Purpose and Environment2478

A.8.12.6.2Test Requirements2483

A.8.12.7E-UTRAN HD-FDD intra-frequency RSTD measurement period test case in CE Mode B2483

A.8.12.7.1Test Purpose and Environment2483

A.8.12.7.2Test Requirements2488

A.8.12.8E-UTRAN TDD intra-frequency RSTD measurement period test case in CE Mode B2488

A.8.12.8.1Test Purpose and Environment2488

A.8.12.8.2Test Requirements2493

A.8.12.9E-UTRAN FDD intra-frequency RSTD measurement period test case in CE Mode A with longer PRS occasions2493

A.8.12.9.1Test Purpose and Environment2493

A.8.12.9.2Test Requirements2498

A.8.12.10E-UTRAN HD-FDD intra-frequency RSTD measurement period test case in CE Mode A with longer PRS occasions2498

A.8.12.10.1Test Purpose and Environment2498

A.8.12.10.2Test Requirements2503

A.8.12.11E-UTRAN TDD intra-frequency RSTD measurement period test case in CE Mode A with longer PRS occasions2503

A.8.12.11.1Test Purpose and Environment2503

A.8.12.11.2Test Requirements2508

A.8.12.12E-UTRAN FDD intra-frequency RSTD measurement period test case in CE Mode B with longer PRS occasions2508

A.8.12.12.1Test Purpose and Environment2508

A.8.12.12.2Test Requirements2513

A.8.12.13E-UTRAN HD-FDD intra-frequency RSTD measurement period test case in CE Mode B with longer PRS occasions2513

A.8.12.13.1Test Purpose and Environment2513

A.8.12.13.2Test Requirements2518

A.8.12.14E-UTRAN TDD intra-frequency RSTD measurement period test case in CE Mode B with longer PRS occasions2518

A.8.12.14.1Test Purpose and Environment2518

A.8.12.14.2Test Requirements2523

A.8.13RSTD Inter-frequency Measurements2523

A.8.13.1E-UTRAN FDD-FDD inter-frequency RSTD measurement reporting delay test case with the reference cell on the serving carrier frequency2523

A.8.13.1.1Test Purpose and Environment2523

A.8.13.1.2Test Requirements2528

A.8.13.1.2ATest Requirements for UE Category 1bis2528

A.8.13.2E-UTRAN TDD-TDD inter-frequency RSTD measurement reporting delay test case with the reference cell on the serving carrier frequency2528

A.8.13.2.1Test Purpose and Environment2528

A.8.13.2.2Test Requirements2534

A.8.13.2.2ATest Requirements for UE Category 1bis2534

A.8.13.3E-UTRAN FDD inter-frequency RSTD measurement period test case in CE Mode A2534

A.8.13.3.1Test Purpose and Environment2534

A.8.13.3.2Test Requirements2541

A.8.13.4E-UTRAN HD-FDD inter-frequency RSTD measurement period test case in CE Mode A2541

A.8.13.4.1Test Purpose and Environment2541

A.8.13.4.2Test Requirements2547

A.8.13.5E-UTRAN TDD inter-frequency RSTD measurement period test case in CE Mode A2547

A.8.13.5.1Test Purpose and Environment2547

A.8.13.5.2Test Requirements2553

A.8.13.6E-UTRAN FDD inter-frequency RSTD measurement period test case in CE Mode B2553

A.8.13.6.1Test Purpose and Environment2553

A.8.13.6.2Test Requirements2559

A.8.13.7E-UTRAN HD-FDD inter-frequency RSTD measurement period test case in CE Mode B2559

A.8.13.7.1Test Purpose and Environment2559

A.8.13.7.2Test Requirements2565

A.8.13.8E-UTRAN TDD inter-frequency RSTD measurement period test case in CE Mode B2565

A.8.13.8.1Test Purpose and Environment2565

A.8.13.8.2Test Requirements2571

A.8.13.9E-UTRAN FDD inter-frequency RSTD measurement period test case in CE Mode A with longer PRS occasions2571

A.8.13.9.1Test Purpose and Environment2571

A.8.13.9.2Test Requirements2577

A.8.13.10E-UTRAN HD-FDD inter-frequency RSTD measurement period test case in CE Mode A with longer PRS occasions2577

A.8.13.10.1Test Purpose and Environment2577

A.8.13.10.2Test Requirements2583

A.8.13.11E-UTRAN TDD inter-frequency RSTD measurement period test case in CE Mode A with longer PRS occasions2583

A.8.13.11.1Test Purpose and Environment2583

A.8.13.11.2Test Requirements2589

A.8.13.12E-UTRAN FDD inter-frequency RSTD measurement period test case in CE Mode B with longer PRS occasions2589

A.8.13.12.1Test Purpose and Environment2589

A.8.13.12.2Test Requirements2595

A.8.13.13E-UTRAN HD-FDD inter-frequency RSTD measurement period test case in CE Mode B with longer PRS occasions2595

A.8.13.13.1Test Purpose and Environment2595

A.8.13.13.2Test Requirements2601

A.8.13.14E-UTRAN TDD inter-frequency RSTD measurement period test case in CE Mode B with longer PRS occasions2601

A.8.13.14.1Test Purpose and Environment2601

A.8.13.14.2Test Requirements2607

A.8.14E-UTRAN TDD - FDD Inter-frequency Measurements2607

A.8.14.1E-UTRAN TDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells2607

A.8.14.1.1Test Purpose and Environment2607

A.8.14.1.2Test Requirements2609

A.8.14.2E-UTRAN TDD-FDD Inter-frequency event triggered reporting when DRX is used under fading propagation conditions in asynchronous cells2609

A.8.14.2.1Test Purpose and Environment2609

A.8.14.2.2Test Requirements2612

A.8.14.3E-UTRAN TDD - FDD Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps2612

A.8.14.3.1Test Purpose and Environment2612

A.8.14.3.2Test Requirements2614

A.8.15E-UTRAN FDD - TDD Inter-frequency Measurements2615

A.8.15.1E-UTRAN FDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells2615

A.8.15.1.1Test Purpose and Environment2615

A.8.15.1.2Test Requirements2616

A.8.15.2E-UTRAN FDD-TDD Inter-frequency event triggered reporting when DRX is used under fading propagation conditions in asynchronous cells2616

A.8.15.2.1Test Purpose and Environment2616

A.8.15.2.2Test Requirements2619

A.8.15.3E-UTRAN FDD - TDD Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps2619

A.8.15.3.1Test Purpose and Environment2619

A.8.15.3.2Test Requirements2621

A.8.16E-UTRAN Carrier Aggregation Measurements2622

A.8.16.1E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX2622

A.8.16.1.1Test Purpose and Environment2622

A.8.16.1.2Test Requirements2624

A.8.16.2E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX2624

A.8.16.2.1Test Purpose and Environment2624

A.8.16.2.2Test Requirements2626

A.8.16.3E-UTRAN FDD-FDD Event triggered reporting on deactivated SCell with PCell interruption in non-DRX2626

A.8.16.3.1Test Purpose and Environment2626

A.8.16.3.2Test Requirements2628

A.8.16.3AE-UTRAN FDD-FDD Event triggered reporting on deactivated SCell with network controlled PCell interruption in non-DRX2629

A.8.16.3A.1Test Purpose and Environment2629

A.8.16.3A.2Test Requirements2630

A.8.16.4E-UTRAN TDD-TDD Event triggered reporting on deactivated SCell  with PCell interruption in non-DRX2631

A.8.16.4.1Test Purpose and Environment2631

A.8.16.4.2Test Requirements2632

A.8.16.4AE-UTRAN TDD-TDD Event triggered reporting on deactivated SCell with PCell interruption in non-DRX2633

A.8.16.4A.1Test Purpose and Environment2633

A.8.16.4A.2Test Requirements2635

A.8.16.5E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX for 20 MHz bandwidth2636

A.8.16.5.1Test Purpose and Environment2636

A.8.16.5.2Test Requirements2636

A.8.16.6E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX for 20 MHz bandwidth2636

A.8.16.6.1Test Purpose and Environment2636

A.8.16.6.2Test Requirements2637

A.8.16.7E-UTRA FDD event triggered reporting on deactivated SCell with PCell interruption in non-DRX for 20 MHz bandwidth2637

A.8.16.7.1 Test Purpose and Environment2637

A.8.16.7.2 Test Requirements2638

A.8.16.8E-UTRA TDD event triggered reporting on deactivated SCell with PCell interruption in non-DRX for 20 MHz bandwidth2638

A.8.16.8.1 Test Purpose and Environment2638

A.8.16.8.2 Test Requirements2639

A.8.16.9E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX for 10MHz+5MHz2639

A.8.16.9.1Test Purpose and Environment2639

A.8.16.9.2Test Requirements2640

A.8.16.10E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX for 10MHz+5MHz2640

A.8.16.10.1Test Purpose and Environment2640

A.8.16.10.2Test Requirements2641

A.8.16.11E-UTRAN FDD event triggered reporting on deactivating SCell with PCell interruption in non-DRX for 10MHz+5MHz2641

A.8.16.11.1 Test Purpose and Environment2641

A.8.16.11.2 Test Requirements2642

A.8.16.12E-UTRAN TDD event triggered reporting on deactivating SCell with PCell interruption in non-DRX for 10MHz+5MHz2642

A.8.16.12.1 Test Purpose and Environment2642

A.8.16.12.2 Test Requirements2642

A.8.16.13E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX for 5MHz +5 MHz bandwidth2642

A.8.16.13.1Test Purpose and Environment2642

A.8.16.13.2Test Requirements2643

A.8.16.14E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX for 5 MHz +5 MHz bandwidth2643

A.8.16.14.1Test Purpose and Environment2643

A.8.16.14.2Test Requirements2644

A.8.16.15E-UTRA FDD event triggered reporting on deactivated SCell with PCell interruption in non-DRX for 5 +5 MHz bandwidth2644

A.8.16.15.1 Test Purpose and Environment2644

A.8.16.7.2 Test Requirements2644

A.8.16.16E-UTRA TDD event triggered reporting on deactivated SCell with PCell interruption in non-DRX for 5+5 MHz bandwidth2644

A.8.16.16.1 Test Purpose and Environment2644

A.8.16.16.2 Test Requirements2645

A.8.16.17E-UTRAN FDD activation and deactivation of known SCell in non-DRX2645

A.8.16.17.1Test Purpose and Environment2645

A.8.16.17.2Test Requirements2647

A.8.16.17AE-UTRAN FDD activation and deactivation of known SCell in non-DRX for 20MHz2648

A.8.16.17A.1Test Purpose and Environment2648

A.8.16.17A.2Test Requirements2648

A.8.16.17BE-UTRAN FDD activation and deactivation of known SCell in non-DRX for 10MHz + 5MHz2648

A.8.16.17B.1Test Purpose and Environment2648

A.8.16.17B.2Test Requirements2649

A.8.16.17CE-UTRAN FDD activation and deactivation of known SCell in non-DRX for 5MHz + 5MHz2649

A.8.16.17C.1Test Purpose and Environment2649

A.8.16.17C.2Test Requirements2649

A.8.16.18E-UTRAN TDD activation and deactivation of known SCell in non-DRX2649

A.8.16.18.1Test Purpose and Environment2649

A.8.16.18.2Test Requirements2651

A.8.16.18AE-UTRAN TDD activation and deactivation of known SCell in non-DRX for 20MHz2652

A.8.16.18A.1Test Purpose and Environment2652

A.8.16.18A.2Test Requirements2652

A.8.16.18BE-UTRAN TDD activation and deactivation of known SCell in non-DRX for 10MHz + 5MHz2652

A.8.16.18B.1Test Purpose and Environment2652

A.8.16.18B.2Test Requirements2653

A.8.16.18CE-UTRAN TDD activation and deactivation of known SCell in non-DRX for 5MHz + 5MHz2653

A.8.16.18C.1Test Purpose and Environment2653

A.8.16.18C.2Test Requirements2653

A.8.16.18DE-UTRAN TDD activation and deactivation of known SCell in non-DRX for 20MHz + 10MHz2653

A.8.16.18D.1Test Purpose and Environment2653

A.8.16.18D.2Test Requirements2654

A.8.16.19E-UTRAN FDD activation and deactivation of unknown SCell in non-DRX2654

A.8.16.19.1Test Purpose and Environment2654

A.8.16.19.2Test Requirements2656

A.8.16.19AE-UTRAN FDD activation and deactivation of unknown SCell in non-DRX for 20MHz2656

A.8.16.19A.1Test Purpose and Environment2656

A.8.16.19A.2Test Requirements2657

A.8.16.19B E-UTRAN FDD activation and deactivation of unknown SCell in non-DRX for 10MHz + 5MHz2657

A.8.16.19B.1Test Purpose and Environment2657

A.8.16.19B.2Test Requirements2657

A.8.16.19CE-UTRAN FDD activation and deactivation of unknown SCell in non-DRX for 5MHz + 5MHz2657

A.8.16.19C.1Test Purpose and Environment2657

A.8.16.19C.2Test Requirements2658

A.8.16.20E-UTRAN TDD activation and deactivation of unknown SCell in non-DRX2658

A.8.16.20.1Test Purpose and Environment2658

A.8.16.20.2Test Requirements2660

A.8.16.20AE-UTRAN TDD activation and deactivation of unknown SCell in non-DRX for 20MHz2661

A.8.16.20A.1Test Purpose and Environment2661

A.8.16.20A.2Test Requirements2661

A.8.16.20BE-UTRAN TDD activation and deactivation of unknown SCell in non-DRX for 10MHz + 5MHz2661

A.8.16.20B.1Test Purpose and Environment2661

A.8.16.20B.2Test Requirements2662

A.8.16.20CE-UTRAN TDD activation and deactivation of unknown SCell in non-DRX for 5MHz + 5MHz2662

A.8.16.20C.1Test Purpose and Environment2662

A.8.16.20C.2Test Requirements2662

A.8.16.20DE-UTRAN TDD activation and deactivation of unknown SCell in non-DRX for 20MHz + 10MHz2662

A.8.16.20D.1Test Purpose and Environment2662

A.8.16.20D.2Test Requirements2663

A.8.16.21E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX for 20MHz+10MHz2663

A.8.16.21.1Test Purpose and Environment2663

A.8.16.21.2Test Requirements2665

A.8.16.22E-UTRAN TDD event triggered reporting on deactivating SCell with PCell interruption in non-DRX for 20MHz+10MHz2665

A.8.16.22.1Test Purpose and Environment2665

A.8.16.22.2Test Requirements2667

A.8.16.23E-UTRAN TDD-FDD CA Event Triggered Reporting Under Deactivated SCell in Non-DRX with PCell in FDD2667

A.8.16.23.1Test Purpose and Environment2667

A.8.16.23.2Test Requirements2670

A.8.16.24E-UTRAN TDD-FDD CA Event Triggered Reporting Under Deactivated SCell in Non-DRX with PCell in TDD2670

A.8.16.24.1Test Purpose and Environment2670

A.8.16.24.2Test Requirements2673

A.8.16.25E-UTRAN TDD-FDD CA Event triggered reporting on deactivated SCell with PCell interruption in non-DRX with PCell in FDD2673

A.8.16.25.1Test Purpose and Environment2673

A.8.16.25.2Test Requirements2676

A.8.16.26E-UTRAN TDD-FDD CA Event triggered reporting on deactivated SCell with PCell interruption in non-DRX with PCell in TDD2676

A.8.16.26.1Test Purpose and Environment2676

A.8.16.26.2Test Requirements2679

A.8.16.273 DL PCell in FDD CA Event Triggered Reporting with 2 Deactivated SCells in Non-DRX2679

A.8.16.27.1Test Purpose and Environment2679

A.8.16.27.2Test Requirements2684

A.8.16.283 DL PCell in TDD CA Event Triggered Reporting with 2 Deactivated SCells in Non-DRX2684

A.8.16.28.1Test Purpose and Environment2684

A.8.16.28.2Test Requirements2689

A.8.16.293 DL FDD CA Event Triggered Reporting under Deactivated SCells in Non-DRX2689

A.8.16.29.1Test Purpose and Environment2689

A.8.16.29.2Test Requirements2694

A.8.16.303 DL TDD CA Event Triggered Reporting under Deactivated SCells in Non-DRX2694

A.8.16.30.1Test Purpose and Environment2694

A.8.16.30.2Test Requirements2699

A.8.16.31E-UTRAN TDD-FDD 3 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX and with PCell in FDD2699

A.8.16.31.1Test Purpose and Environment2699

A.8.16.31.2Test Requirements2704

A.8.16.32E-UTRAN TDD-FDD 3 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX and with PCell in TDD2704

A.8.16.32.1Test Purpose and Environment2704

A.8.16.32.2Test Requirements2709

A.8.16.33E-UTRAN FDD 3 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX2709

A.8.16.33.1Test Purpose and Environment2709

A.8.16.33.2Test Requirements2714

A.8.16.34E-UTRAN TDD 3 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX2714

A.8.16.34.1Test Purpose and Environment2714

A.8.16.34.2Test Requirements2719

A.8.16.353 DL PCell in FDD CA Activation and Deactivation of Known SCell in Non-DRX2719

A.8.16.35.1Test Purpose and Environment2719

A.8.16.35.2Test Requirements2721

A.8.16.363 DL PCell in TDD CA Activation and Deactivation of Known SCell in Non-DRX2722

A.8.16.36.1Test Purpose and Environment2722

A.8.16.36.2Test Requirements2724

A.8.16.373 DL FDD CA activation and deactivation of known SCell in non-DRX2725

A.8.16.37.1Test Purpose and Environment2725

A.8.16.37.2Test Requirements2727

A.8.16.383 DL TDD CA activation and deactivation of known SCell in non-DRX2728

A.8.16.38.1Test Purpose and Environment2728

A.8.16.38.2Test Requirements2730

A.8.16.39E-UTRA TDD-FDD 3DL CA Activation and Deactivation of Unknown SCell in Non-DRX with PCell in FDD2731

A.8.16.39.1Test Purpose and Environment2731

A.8.16.39.2Test Requirements2734

A.8.16.40E-UTRA TDD-FDD 3DL CA Activation and Deactivation of Unknown SCell in Non-DRX with PCell in TDD2734

A.8.16.40.1Test Purpose and Environment2734

A.8.16.40.2Test Requirements2737

A.8.16.413 DL FDD CA activation and deactivation of unknown SCell in non-DRX2737

A.8.16.41.1Test Purpose and Environment2737

A.8.16.41.2Test Requirements2739

A.8.16.423 DL TDD CA activation and deactivation of unknown SCell in non-DRX2740

A.8.16.42.1Test Purpose and Environment2740

A.8.16.42.2Test Requirements2742

A.8.16.43E-UTRAN TDD-FDD CA activation and deactivation of known SCell in non-DRX with PCell in FDD2743

A.8.16.43.1Test Purpose and Environment2743

A.8.16.43.2Test Requirements2746

A.8.16.44E-UTRAN TDD-FDD CA activation and deactivation of unknown SCell in non-DRX with PCell in FDD2746

A.8.16.44.1Test Purpose and Environment2746

A.8.16.44.2Test Requirements2749

A.8.16.45E-UTRAN TDD-FDD CA activation and deactivation of known SCell in non-DRX with PCell in TDD2749

A.8.16.45.1Test Purpose and Environment2749

A.8.16.45.2Test Requirements2752

A.8.16.46E-UTRAN TDD-FDD CA activation and deactivation of unknown SCell in non-DRX with PCell in TDD2752

A.8.16.46.1Test Purpose and Environment2752

A.8.16.46.2Test Requirements2754

A.8.16.472DL/2UL FDD CA activation and deactivation of known PUCCH SCell without valid TA in non-DRX2755

A.8.16.47.1Test Purpose and Environment2755

A.8.16.47.2Test Requirements2757

A.8.16.482DL/2UL TDD CA activation and deactivation of known PUCCH SCell without valid TA in non-DRX2758

A.8.16.48.1Test Purpose and Environment2758

A.8.16.48.2Test Requirements2760

A.8.16.492DL/2UL TDD-FDD CA (FDD PCell) activation and deactivation of known PUCCH SCell without valid TA in non-DRX2761

A.8.16.49.1Test Purpose and Environment2761

A.8.16.49.2Test Requirements2764

A.8.16.502DL/2UL TDD-FDD CA (TDD PCell) activation and deactivation of known PUCCH SCell without valid TA in non-DRX2764

A.8.16.50.1Test Purpose and Environment2764

A.8.16.50.2Test Requirements2766

A.8.16.51E-UTRAN 4 DL FDD CA Event Triggered Reporting with 3 deactivated SCells in Non-DRX2767

A.8.16.51.1Test Purpose and Environment2767

A.8.16.51.2Test Requirements2772

A.8.16.52E-UTRAN 4 DL TDD CA Event Triggered Reporting with 3 deactivated SCells in Non-DRX2772

A.8.16.52.1Test Purpose and Environment2772

A.8.16.52.2Test Requirements2777

A.8.16.534 DL PCell in FDD CA Event Triggered Reporting with 3 Deactivated SCells in Non-DRX2777

A.8.16.53.1Test Purpose and Environment2777

A.8.16.53.2Test Requirements2781

A.8.16.544 DL PCell in TDD CA Event Triggered Reporting with 3 Deactivated SCells in Non-DRX2781

A.8.16.54.1Test Purpose and Environment2781

A.8.16.54.2Test Requirements2785

A.8.16.55E-UTRAN FDD 4 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX2785

A.8.16.55.1Test Purpose and Environment2785

A.8.16.55.2Test Requirements2791

A.8.16.56E-UTRAN TDD 4 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX2791

A.8.16.56.1Test Purpose and Environment2791

A.8.16.56.2Test Requirements2797

A.8.16.57E-UTRAN FDD 4DL CA activation and deactivation of know SCell in non-DRX2797

A.8.16.57.1Test Purpose and Environment2797

A.8.16.57.2Test Requirements2799

A.8.16.58E-UTRAN TDD 4DL CA activation and deactivation of know SCell in non-DRX2800

A.8.16.58.1Test Purpose and Environment2800

A.8.16.58.2Test Requirements2802

A.8.16.59E-UTRAN PCell in FDD FDD-TDD 4 DL CA activation and deactivation of known SCell in non-DRX2803

A.8.16.59.1Test Purpose and Environment2803

A.8.16.59.2Test Requirements2807

A.8.16.60E-UTRAN PCell in TDD FDD-TDD 4 DL CA activation and deactivation of known SCell in non-DRX2808

A.8.16.60.1Test Purpose and Environment2808

A.8.16.60.2Test Requirements2811

A.8.16.61E-UTRAN FDD 4DL CA activation and deactivation of unknown SCell in non-DRX2812

A.8.16.61.1Test Purpose and Environment2812

A.8.16.61.2Test Requirements2815

A.8.16.62E-UTRAN TDD 4DL CA activation and deactivation of unknown SCell in non-DRX2815

A.8.16.62.1Test Purpose and Environment2815

A.8.16.62.2Test Requirements2817

A.8.16.63E-UTRAN PCell in FDD FDD-TDD 4 DL CA activation and deactivation of unknown SCell in non-DRX2818

A.8.16.63.1Test Purpose and Environment2818

A.8.16.63.2Test Requirements2821

A.8.16.64E-UTRAN PCell in TDD FDD-TDD 4 DL CA activation and deactivation of unknown SCell in non-DRX2822

A.8.16.64.1Test Purpose and Environment2822

A.8.16.64.2Test Requirements2826

A.8.16.655 DL FDD-TDD with PCell in FDD CA Event Triggered Reporting with 4 Deactivated SCells in Non-DRX2826

A.8.16.65.1Test Purpose and Environment2826

A.8.16.65.2Test Requirements2831

A.8.16.665 DL FDD-TDD with PCell in TDD CA Event Triggered Reporting with 4 Deactivated SCells in Non-DRX2831

A.8.16.66.1Test Purpose and Environment2831

A.8.16.66.2Test Requirements2836

A.8.16.675 DL FDD-TDD with PCell in FDD CA activation and deactivation of Unknown SCell in non-DRX2836

A.8.16.67.1Test Purpose and Environment2836

A.8.16.67.2Test Requirements2841

A.8.16.685 DL FDD-TDD with PCell in TDD CA activation and deactivation of Unknown SCell in non-DRX2841

A.8.16.68.1Test Purpose and Environment2841

A.8.16.68.2Test Requirements2846

A.8.16.695 DL FDD CA activation and deactivation of unknown SCell in non-DRX2846

A.8.16.69.1Test Purpose and Environment2846

A.8.16.69.2Test Requirements2850

A.8.16.705 DL TDD CA activation and deactivation of unknown SCell in non-DRX2850

A.8.16.70.1Test Purpose and Environment2850

A.8.16.70.2Test Requirements2854

A.8.16.715 DL FDD CA Event Triggered Reporting with Deactivated SCells in Non-DRX2854

A.8.16.71.1Test Purpose and Environment2854

A.8.16.71.2Test Requirements2859

A.8.16.725 DL TDD CA Event Triggered Reporting with Deactivated SCells in Non-DRX2859

A.8.16.72.1Test Purpose and Environment2859

A.8.16.72.2Test Requirements2864

A.8.16.735 DL FDD CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX2864

A.8.16.73.1Test Purpose and Environment2864

A.8.16.73.2Test Requirements2871

A.8.16.745 DL TDD CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX2871

A.8.16.74.1Test Purpose and Environment2871

A.8.16.74.2Test Requirements2878

A.8.16.755 DL FDD-TDD with PCell in FDD CA activation and deactivation of known SCell in non-DRX2878

A.8.16.75.1Test Purpose and Environment2878

A.8.16.75.2Test Requirements2884

A.8.16.765 DL FDD-TDD with PCell in TDD CA activation and deactivation of known SCell in non-DRX2884

A.8.16.76.1Test Purpose and Environment2884

A.8.16.76.2Test Requirements2890

A.8.16.775 DL FDD CA activation and deactivation of know SCell in non-DRX2890

A.8.16.77.1Test Purpose and Environment2890

A.8.16.77.2Test Requirements2894

A.8.16.785 DL TDD CA activation and deactivation of know SCell in non-DRX2894

A.8.16.78.1Test Purpose and Environment2894

A.8.16.78.2Test Requirements2896

A.8.16.79E-UTRAN PCell in FDD FDD-TDD 4 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX2897

A.8.16.79.1Test Purpose and Environment2897

A.8.16.79.2Test Requirements2904

A.8.16.80E-UTRAN PCell in TDD TDD-FDD 4 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX2904

A.8.16.80.1Test Purpose and Environment2904

A.8.16.80.2Test Requirements2911

A.8.16.81E-UTRAN PCell in FDD FDD-TDD 5 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX2911

A.8.16.81.1Test Purpose and Environment2911

A.8.16.81.2Test Requirements2917

A.8.16.82E-UTRAN PCell in TDD TDD-FDD 5 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX2917

A.8.16.82.1Test Purpose and Environment2917

A.8.16.82.2Test Requirements2923

A.8.16.833 DL CA Event Triggered Reporting under Deactivated SCells in Non-DRX with generic duplex modes2923

A.8.16.83.1Test Purpose and Environment2923

A.8.16.83.2Test Requirements2928

A.8.16.843 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX with generic duplex modes2928

A.8.16.84.1Test Purpose and Environment2928

A.8.16.84.2Test Requirements2934

A.8.16.853 DL CA Activation and Deactivation of Known SCell in Non-DRX with generic duplex modes2934

A.8.16.85.1Test Purpose and Environment2934

A.8.16.85.2Test Requirements2938

A.8.16.863 DL CA Activation and Deactivation of Unknown SCell in Non-DRX with generic duplex modes2938

A.8.16.86.1Test Purpose and Environment2938

A.8.16.86.2Test Requirements2941

A.8.16.874 DL CA Event Triggered Reporting under Deactivated SCells in Non-DRX with generic duplex modes2941

A.8.16.87.1Test Purpose and Environment2941

A.8.16.87.2Test Requirements2947

A.8.16.884 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX with generic duplex modes2947

A.8.16.88.1Test Purpose and Environment2947

A.8.16.88.2Test Requirements2955

A.8.16.894 DL CA Activation and Deactivation of Known SCell in Non-DRX with generic duplex modes2955

A.8.16.89.1Test Purpose and Environment2955

A.8.16.89.2Test Requirements2962

A.8.16.904 DL CA Activation and Deactivation of Unknown SCell in Non-DRX with generic duplex modes2962

A.8.16.90.1Test Purpose and Environment2962

A.8.16.90.2Test Requirements2969

A.8.16.915 DL CA Event Triggered Reporting under Deactivated SCells in Non-DRX with generic duplex modes2969

A.8.16.91.1Test Purpose and Environment2969

A.8.16.91.2Test Requirements2975

A.8.16.925 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX with generic duplex modes2975

A.8.16.92.1Test Purpose and Environment2975

A.8.16.92.2Test Requirements2983

A.8.16.935 DL CA Activation and Deactivation of Known SCell in Non-DRX with generic duplex modes2983

A.8.16.93.1Test Purpose and Environment2983

A.8.16.93.2Test Requirements2990

A.8.16.945 DL CA Activation and Deactivation of Unknown SCell in Non-DRX with generic duplex modes2990

A.8.16.94.1Test Purpose and Environment2990

A.8.16.94.2Test Requirements2997

A.8.16.956 DL CA Event Triggered Reporting under Deactivated SCells in Non-DRX with generic duplex modes2997

A.8.16.95.1Test Purpose and Environment2997

A.8.16.95.2Test Requirements3005

A.8.16.966 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX with generic duplex modes3005

A.8.16.96.1Test Purpose and Environment3005

A.8.16.96.2Test Requirements3014

A.8.16.976 DL CA Activation and Deactivation of Known SCell in Non-DRX with generic duplex modes3014

A.8.16.97.1Test Purpose and Environment3014

A.8.16.97.2Test Requirements3021

A.8.16.986 DL CA Activation and Deactivation of Unknown SCell in Non-DRX with generic duplex modes3021

A.8.16.98.1Test Purpose and Environment3021

A.8.16.98.2Test Requirements3029

A.8.16.997 DL CA Event Triggered Reporting under Deactivated SCells in Non-DRX with generic duplex modes3029

A.8.16.99.1Test Purpose and Environment3029

A.8.16.99.2Test Requirements3039

A.8.16.1007 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX with generic duplex modes3039

A.8.16.100.1Test Purpose and Environment3039

A.8.16.100.2Test Requirements3049

A.8.16.1017 DL CA Activation and Deactivation of Known SCell in Non-DRX with generic duplex modes3049

A.8.16.101.1Test Purpose and Environment3049

A.8.16.101.2Test Requirements3059

A.8.16.1027 DL CA Activation and Deactivation of Unknown SCell in Non-DRX with generic duplex modes3059

A.8.16.102.1Test Purpose and Environment3059

A.8.16.102.2Test Requirements3070

A.8.16.103Hibernation and Activation of Known SCell in Non-DRX with generic duplex modes3070

A.8.16.103.1Test Purpose and Environment3070

A.8.16.103.2Test Requirements3075

A.8.16.104Hibernation and Activation of Unknown SCell in Non-DRX with generic duplex modes3076

A.8.16.104.1Test Purpose and Environment3076

A.8.16.104.2Test Requirements3080

A.8.16.105Idle Mode measurements of inter-frequency CA candidate cells for early reporting3081

A.8.16.105.1Test Purpose and Environment3081

A.8.16.105.2Test Requirements3085

A.8.16.106Direct Activation of Known SCell in Non-DRX with generic duplex modes3086

A.8.16.106.1Test Purpose and Environment3086

A.8.16.106.2Test Requirements3090

A.8.16.107E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX with highSpeedEnhMeasFlag2-r163090

A.8.16.107.1Test Purpose and Environment3090

A.8.16.107.2Test Requirements3092

A.8.16.108E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX with highSpeedEnhMeasFlag2-r163093

A.8.16.108.1Test Purpose and Environment3093

A.8.16.108.2Test Requirements3095

A.8.17RSTD Measurements for E-UTRAN Carrier Aggregation3096

A.8.17.1E-UTRAN FDD RSTD measurement reporting delay test case3096

A.8.17.1.1Test Purpose and Environment3096

A.8.17.1.2Test Requirements3102

A.8.17.2E-UTRAN TDD RSTD measurement reporting delay test case3102

A.8.17.2.1Test Purpose and Environment3102

A.8.17.2.2Test Requirements3109

A.8.17.3E-UTRAN FDD RSTD Measurement Reporting Test Case for 20 MHz3109

A.8.17.3.1Test Purpose and Environment3109

A.8.17.3.2Test Requirements3110

A.8.17.4E-UTRAN TDD RSTD Measurement Reporting Test Case for 20 MHz3110

A.8.17.4.1Test Purpose and Environment3110

A.8.17.4.2Test Requirements3111

A.8.17.5E-UTRAN FDD RSTD Measurement Reporting Test Case for 10MHz+5MHz3111

A.8.17.5.1Test Purpose and Environment3111

A.8.17.5.2Test Requirements3112

A.8.17.6E-UTRAN TDD RSTD Measurement Reporting Test Case for 10MHz+5MHz3112

A.8.17.6.1Test Purpose and Environment3112

A.8.17.6.2Test Requirements3113

A.8.17.7E-UTRAN FDD RSTD Measurement Reporting Test Case for 5 + 5 MHz Bandwidth3114

A.8.17.7.1Test Purpose and Environment3114

A.8.17.7.2Test Requirements3114

A.8.17.8E-UTRAN TDD RSTD Measurement Reporting Test Case for 5+5 MHz bandwidth3115

A.8.17.8.1Test Purpose and Environment3115

A.8.17.8.2Test Requirements3115

A.8.17.9E-UTRAN TDD RSTD Measurement Reporting Test Case for 20MHz+10MHz3116

A.8.17.9.1Test Purpose and Environment3116

A.8.17.9.2Test Requirements3117

A.8.17.10E-UTRAN 3 DL FDD CA RSTD Measurement Reporting Delay Test Case3117

A.8.17.10.1Test Purpose and Environment3117

A.8.17.10.2Test Requirements3124

A.8.17.11E-UTRAN 3 DL TDD CA RSTD Measurement Reporting Delay Test Case3125

A.8.17.11.1Test Purpose and Environment3125

A.8.17.11.2Test Requirements3131

A.8.18E-UTRAN TDD – HRPD Measurements3132

A.8.18.1E-UTRAN TDD-HRPD event triggered reporting under fading propagation conditions3132

A.8.18.1.1Test Purpose and Environment3132

A.8.18.1.2Test Requirements3134

A.8.19E-UTRAN TDD – CDMA2000 1X Measurements3134

A.8.19.1E-UTRAN TDD – CDMA2000 1X event triggered reporting under fading propagation conditions3134

A.8.19.1.1Test Purpose and Environment3134

A.8.19.1.2Test Requirements3135

A.8.20Inter-frequency/RAT Measurements in CA mode3136

A.8.20.1E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells3136

A.8.20.1.1Test Purpose and Environment3136

A.8.20.1.2Test Requirements3137

A.8.20.2E-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells3137

A.8.20.2.1Test Purpose and Environment3138

A.8.20.2.2Test Requirements3139

A.8.20.2AE-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells for 20 MHz +20 MHz bandwidth.3140

A.8.20.2A.1Test Purpose and Environment3140

A.8.20.2A.2Test Requirements3140

A.8.20.2BE-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells for 20 MHz +10 MHz bandwidth.3140

A.8.20.2B.1Test Purpose and Environment3140

A.8.20.2B.2Test Requirements3143

A.8.20.3E-UTRAN FDD - UTRAN FDD event triggered reporting under fading propagation conditions3143

A.8.20.3.1Test Purpose and Environment3143

A.8.20.3.2Test Requirements3145

A.8.20.4E-UTRAN TDD to UTRAN TDD cell search under fading propagation conditions3145

A.8.20.4.1Test Purpose and Environment3145

A.8.20.4.1.11.28 Mcps TDD option3145

A.8.20.4.2Test Requirements3147

A.8.20.4.2.11.28 Mcps TDD option3147

A.8.20.4AE-UTRAN TDD with 20 MHz +20 MHz bandwidth to UTRAN TDD cell search under fading propagation conditions3147

A.8.20.4A.1Test Purpose and Environment3147

A.8.20.4A.1.11.28 Mcps TDD option3147

A.8.20.4A.2Test Requirements3147

A.8.20.4A.2.11.28 Mcps TDD option3147

A.8.20.4BE-UTRAN TDD with 20 MHz +10 MHz bandwidth to UTRAN TDD cell search under fading propagation conditions3148

A.8.20.4B.1Test Purpose and Environment3148

A.8.20.4B.1.11.28 Mcps TDD option3148

A.8.20.4B.2Test Requirements3150

A.8.20.4B.2.11.28 Mcps TDD option3150

A.8.21CSG Proximity Indication Testing Case for E-UTRAN FDD – FDD Inter frequency3150

A.8.21.1Test Purpose and Environment3150

A.8.21.2 Test Requirements3154

A.8.22E-UTRAN Discovery Signal Measurements3154

A.8.22.1E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells in DRX based on CRS based discovery signal3154

A.8.22.1.1Test Purpose and Environment3154

A.8.22.1.2Test Requirements3157

A.8.22.2E-UTRAN TDD-TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells in DRX based on CRS based discovery signal3157

A.8.22.2.1Test Purpose and Environment3157

A.8.22.2.2Test Requirements3160

A.8.22.3E-UTRAN FDD-FDD inter-frequency event triggered reporting under fading propagation conditions in DRX based on CRS based discovery signal3160

A.8.22.3.1Test Purpose and Environment3160

A.8.22.3.2Test Requirements3163

A.8.22.4E-UTRAN TDD-TDD inter-frequency event triggered reporting under fading propagation conditions in DRX based on CRS based discovery signal3163

A.8.22.4.1Test Purpose and Environment3163

A.8.22.4.2Test Requirements3166

A.8.22.5E-UTRAN FDD-FDD intra-frequency event triggered reporting in DRX based on CSI-RS based discovery signal3166

A.8.22.5.1Test Purpose and Environment3166

A.8.22.5.2Test Requirements3170

A.8.22.6E-UTRAN TDD-TDD intra-frequency event triggered reporting in DRX based on CSI-RS based discovery signal3170

A.8.22.6.1Test Purpose and Environment3170

A.8.22.6.2Test Requirements3174

A.8.22.7E-UTRAN FDD-FDD Inter-frequency event triggered reporting in DRX based on CSI-RS based discovery signal3174

A.8.22.7.1Test Purpose and Environment3174

A.8.22.7.2Test Requirements3178

A.8.22.8E-UTRAN TDD-TDD inter-frequency event triggered reporting under fading propagation condition in DRX based on CSI-RS based discovery signal3178

A.8.22.8.1Test Purpose and Environment3178

A.8.22.8.2Test Requirements3182

A.8.22.9E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX based on CRS based discovery signal3182

A.8.22.9.1Test Purpose and Environment3182

A.8.22.9.2Test Requirements3184

A.8.22.10E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX based on CRS based discovery signal3185

A.8.22.10.1Test Purpose and Environment3185

A.8.22.10.2Test Requirements3187

A.8.22.11E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX based on CSI-RS based discovery signal3188

A.8.22.11.1Test Purpose and Environment3188

A.8.22.11.2Test Requirements3191

A.8.22.12E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX based on CSI-RS based discovery signal3191

A.8.22.12.1Test Purpose and Environment3191

A.8.22.12.2Test Requirements3195

A.8.23E-UTRAN Dual Connectivity Measurements3195

A.8.23.1E-UTRAN FDD-FDD DC intra-frequency event triggered reporting with DRX in synchronous DC3195

A.8.23.1.1Test Purpose and Environment3195

A.8.23.1.2Test Requirements3198

A.8.23.2E-UTRAN FDD-FDD DC intra-frequency event triggered reporting with DRX in asynchronous DC3198

A.8.23.2.1Test Purpose and Environment3198

A.8.23.2.2Test Requirements3201

A.8.23.3E-UTRAN TDD-TDD DC intra-frequency event triggered reporting with DRX in synchronous DC3201

A.8.23.3.1Test Purpose and Environment3201

A.8.23.3.2Test Requirements3204

A.8.23.4E-UTRAN FDD-FDD DC inter-frequency event triggered reporting with DRX in synchronous DC3204

A.8.23.4.1Test Purpose and Environment3204

A.8.23.4.2Test Requirements3207

A.8.23.5E-UTRAN FDD-FDD DC inter-frequency event triggered reporting with DRX in asynchronous DC3207

A.8.23.5.1Test Purpose and Environment3207

A.8.23.5.2Test Requirements3210

A.8.23.6E-UTRAN TDD-TDD DC inter-frequency event triggered reporting with DRX in synchronous DC3210

A.8.23.6.1Test Purpose and Environment3210

A.8.23.6.2Test Requirements3213

A.8.23.7E-UTRAN FDD-FDD Addition and Release Delay of known PSCell in Synchronous DC3213

A.8.23.7.1Test Purpose and Environment3213

A.8.23.7.2Test Requirements3215

A.8.23.8E-UTRAN FDD-FDD Addition and Release Delay of known PSCell in Asynchronous DC3216

A.8.23.8.1Test Purpose and Environment3216

A.8.23.8.2Test Requirements3218

A.8.23.9E-UTRAN TDD Addition and Release Delay of known PSCell in Synchronous DC3219

A.8.23.9.1Test Purpose and Environment3219

A.8.23.9.2Test Requirements3222

A.8.23.10E-UTRAN TDD-FDD DC intra-frequency event triggered reporting with DRX in synchronous DC with PCell in FDD3222

A.8.23.10.1Test Purpose and Environment3222

A.8.23.10.2Test Requirements3225

A.8.23.11E-UTRAN TDD-FDD DC intra-frequency event triggered reporting with DRX in synchronous DC with PCell in TDD3225

A.8.23.11.1Test Purpose and Environment3225

A.8.23.11.2Test Requirements3228

A.8.23.12E-UTRAN TDD-FDD DC inter-frequency event triggered reporting with DRX in synchronous DC with PCell in FDD3228

A.8.23.12.1Test Purpose and Environment3228

A.8.23.12.2Test Requirements3231

A.8.23.13E-UTRAN TDD-FDD DC inter-frequency event triggered reporting with DRX in synchronous DC with PCell in TDD3231

A.8.23.13.1Test Purpose and Environment3231

A.8.23.13.2Test Requirements3234

A.8.23.14E-UTRAN TDD-FDD Addition and Release Delay of known PSCell in Synchronous DC with PCell in FDD3234

A.8.23.14.1Test Purpose and Environment3234

A.8.23.14.2Test Requirements3237

A.8.23.15E-UTRAN TDD-FDD Addition and Release Delay of known PSCell in Synchronous DC with PCell in TDD3237

A.8.23.15.1Test Purpose and Environment3237

A.8.23.15.2Test Requirements3240

A.8.23.16E-UTRAN FDD-FDD DC SSTD measurement reporting delay with no DRX in asynchronous DC3240

A.8.23.16.1Test Purpose and Environment3240

A.8.23.16.2Test Requirements3241

A.8.23.17E-UTRAN FDD-FDD DC SSTD measurement reporting delay with DRX in asynchronous DC3242

A.8.23.17.1Test Purpose and Environment3242

A.8.23.17.2Test Requirements3244

A.8.23.18E-UTRAN FDD - FDD DC Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps in synchronous DC3244

A.8.23.18.1Test Purpose and Environment3244

A.8.23.18.2Test Requirements3245

A.8.23.19E-UTRAN FDD - FDD DC Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps in asynchronous DC3246

A.8.23.19.1Test Purpose and Environment3246

A.8.23.19.2Test Requirements3247

A.8.23.20E-UTRAN TDD - TDD DC Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps in synchronous DC3248

A.8.23.20.1Test Purpose and Environment3248

A.8.23.20.2Test Requirements3249

A.8.23.21E-UTRAN FDD - FDD DC Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps in synchronous DC3250

A.8.23.21.1Test Purpose and Environment3250

A.8.23.21.2Test Requirements3251

A.8.23.22E-UTRAN FDD - FDD DC Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps in asynchronous DC3252

A.8.23.22.1Test Purpose and Environment3252

A.8.23.22.2Test Requirements3253

A.8.23.23E-UTRAN TDD - TDD DC Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps in synchronous DC3254

A.8.23.23.1Test Purpose and Environment3254

A.8.23.23.2Test Requirements3255

A.8.23.24E-UTRAN FDD-FDD DC activation and deactivation of known SCell in Non-DRX in synchronous DC3256

A.8.23.24.1Test Purpose and Environment3256

A.8.23.24.2Test Requirements3258

A.8.23.25E-UTRAN FDD-FDD DC activation and deactivation of known SCell in Non-DRX in asynchronous DC3259

A.8.23.25.1Test Purpose and Environment3259

A.8.23.25.2Test Requirements3261

A.8.23.26E-UTRAN TDD-TDD DC activation and deactivation of known SCell in Non-DRX in synchronous DC3262

A.8.23.26.1Test Purpose and Environment3262

A.8.23.26.2Test Requirements3264

A.8.23.27E-UTRAN FDD-FDD DC event triggered reporting under deactivated SCell with PCell and PSCell interruption in non-DRX in synchronous DC3265

A.8.23.27.1Test Purpose and Environment3265

A.8.23.27.2Test Requirements3268

A.8.23.28E-UTRAN FDD-FDD DC event triggered reporting under deactivated SCell with PCell and PSCell interruption in non-DRX in asynchronous DC3268

A.8.23.28.1Test Purpose and Environment3268

A.8.23.28.2Test Requirements3272

A.8.23.29E-UTRAN TDD-TDD DC event triggered reporting under deactivated SCell with PCell and PSCell interruption in non-DRX in synchronous DC3272

A.8.23.29.1Test Purpose and Environment3272

A.8.23.29.2Test Requirements3276

A.8.24Proximity-based Services3276

A.8.24.1E-UTRAN FDD - Initiation/Cease of SLSS Transmission with ProSe Direct Discovery3276

A.8.24.1.1Test Purpose and Environment3276

A.8.24.1.2Test Requirements3277

A.8.24.2E-UTRAN TDD - Initiation/Cease of SLSS Transmission with ProSe Direct Discovery3278

A.8.24.2.1Test Purpose and Environment3278

A.8.24.2.2Test Requirements3279

A.8.24.3E-UTRAN FDD - Initiation/Cease of SLSS Transmission with ProSe Direct Communication3279

A.8.24.3.1Test Purpose and Environment3280

A.8.24.3.2Test Requirements3281

A.8.25E-UTRAN-WLAN Measurements3282

A.8.25.1E-UTRAN FDD-WLAN Event Triggered Reporting in non-DRX under AWGN3282

A.8.25.1.1Test Purpose and Environment3282

A.8.25.1.2Test Requirements3284

A.8.25.2E-UTRAN TDD-WLAN Event Triggered Reporting in non-DRX under AWGN3284

A.8.25.2.1Test Purpose and Environment3284

A.8.25.2.2Test Requirements3286

A.8.26 Frame Structure 3 (FS3)3286

A.8.26.1E-UTRAN FDD-FS3 Activation and deactivation of known FS3 SCell with FDD PCell in non-DRX3286

A.8.26.1.1Test Purpose and Environment3286

A.8.26.1.2Test Requirements3288

A.8.26.2E-UTRAN TDD-FS3 Activation and deactivation of known FS3 SCell with TDD PCell in non-DRX3289

A.8.26.2.1Test Purpose and Environment3289

A.8.26.2.2Test Requirements3291

A.8.26.3E-UTRAN FDD-FS3 Event triggered reporting on deactivated FS3 SCell and FDD PCell interruption in non-DRX3292

A.8.26.3.1Test Purpose and Environment3292

A.8.26.3.2Test Requirements3295

A.8.26.3AE-UTRAN FDD-TDD 3DL Event triggered reporting on deactivated FS3 SCell and FDD PCell interruption in non-DRX3295

A.8.26.3A.1Test Purpose and Environment3295

A.8.26.3A.2Test Requirements3298

A.8.26.4E-UTRAN TDD-FS3 Event triggered reporting on deactivated FS3 SCell and TDD PCell interruption in non-DRX3298

A.8.26.4.1Test Purpose and Environment3298

A.8.26.4.2Test Requirements3302

A.8.26.4AE-UTRAN TDD-TDD 3DL Event triggered reporting on deactivated FS3 SCell and FDD PCell interruption in non-DRX3302

A.8.26.4A.1Test Purpose and Environment3302

A.8.26.4A.2Test Requirements3306

A.8.26.5E-UTRAN FDD-FS3 Intra-frequency event triggered reporting in non-DRX for CRS based discovery signal3306

A.8.26.5.1Test Purpose and Environment3306

A.8.26.5.2Test Requirements3309

A.8.26.5AE-UTRAN FDD-FS3 Intra-frequency event triggered reporting in non-DRX for CRS based discovery signal with 2 SCells3309

A.8.26.5A.1Test Purpose and Environment3309

A.8.26.5A.2Test Requirements3313

A.8.26.6E-UTRAN TDD-FS3 Intra-frequency event triggered reporting in non-DRX for CRS based discovery signal3313

A.8.26.6.1Test Purpose and Environment3313

A.8.26.6.2Test Requirements3317

A.8.26.6AE-UTRAN TDD-FS3 Intra-frequency event triggered reporting in non-DRX for CRS based discovery signal with 2 SCells3317

A.8.26.6A.1Test Purpose and Environment3317

A.8.26.6A.2Test Requirements3321

A.8.26.7E-UTRAN FDD-FS3 Intra-frequency event triggered reporting in DRX for CRS based discovery signal3321

A.8.26.7.1Test Purpose and Environment3321

A.8.26.7.2Test Requirements3324

A.8.26.8E-UTRAN TDD-FS3 Intra-frequency event triggered reporting in DRX for CRS based discovery signal3324

A.8.26.8.1Test Purpose and Environment3324

A.8.26.8.2Test Requirements3328

A.8.26.9E-UTRAN FDD-FS3 Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells3328

A.8.26.9.1Test Purpose and Environment3328

A.8.26.9.2Test Requirements3331

A.8.26.10E-UTRAN TDD-FS3 inter-frequency event triggered reporting under fading propagation conditions in synchronous cells3331

A.8.26.10.1Test Purpose and Environment3331

A.8.26.10.2Test Requirements3334

A.9Measurement Performance Requirements3334

A.9.1RSRP3334

A.9.1.1FDD Intra frequency case3334

A.9.1.1.1Test Purpose and Environment3334

A.9.1.1.2Test parameters3334

A.9.1.1.3Test Requirements3337

A.9.1.2TDD Intra frequency case3337

A.9.1.2.1Test Purpose and Environment3337

A.9.1.2.2Test parameters3337

A.9.1.2.3Test Requirements3338

A.9.1.3FDD—FDD Inter frequency case3339

A.9.1.3.1Test Purpose and Environment3339

A.9.1.3.2Test parameters3339

A.9.1.3.3Test Requirements3342

A.9.1.4TDD—TDD Inter frequency case3342

A.9.1.4.1Test Purpose and Environment3342

A.9.1.4.2Test parameters3342

A.9.1.4.3Test Requirements3344

A.9.1.5FDD—TDD Inter frequency case3345

A.9.1.5.1Test Purpose and Environment3345

A.9.1.5.2Test parameters3345

A.9.1.5.3Test Requirements3346

A.9.1.6FDD RSRP for E-UTRAN Carrier Aggregation3347

A.9.1.6.1Test Purpose and Environment3347

A.9.1.6.2Test parameters3347

A.9.1.6.3Test Requirements3350

A.9.1.7TDD RSRP for E-UTRAN Carrier Aggregation3350

A.9.1.7.1Test Purpose and Environment3350

A.9.1.7.2Test parameters3350

A.9.1.7.3Test Requirements3353

A.9.1.8FDD RSRP under Time-Domain Measurement Resource Restriction with Non-MBSFN ABS3353

A.9.1.8.1Test Purpose and Environment3353

A.9.1.8.2Test parameters3353

A.9.1.8.3Test Requirements3357

A.9.1.9TDD RSRP under Time-Domain Measurement Resource Restriction with Non-MBSFN ABS3357

A.9.1.9.1Test Purpose and Environment3357

A.9.1.9.2Test parameters3357

A.9.1.9.3Test Requirements3360

A.9.1.10FDD RSRP under Time-Domain Measurement Resource Restriction with MBSFN ABS3360

A.9.1.10.1Test Purpose and Environment3360

A.9.1.10.2Test parameters3360

A.9.1.10.3Test Requirements3363

A.9.1.11TDD RSRP under Time-Domain Measurement Resource Restriction with MBSFN ABS3363

A.9.1.11.1Test Purpose and Environment3363

A.9.1.11.2Test parameters3363

A.9.1.11.3Test Requirements3367

A.9.1.12FDD RSRP for E-UTRAN Carrier Aggregation for 20MHz3367

A.9.1.12.1Test Purpose and Environment3367

A.9.1.12.2Test parameters3367

A.9.1.12.3Test Requirements3368

A.9.1.13TDD RSRP for E-UTRAN Carrier Aggregation for 20MHz3368

A.9.1.13.1Test Purpose and Environment3368

A.9.1.13.2Test parameters3368

A.9.1.13.3Test Requirements3369

A.9.1.14FDD RSRP under Time-Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS3369

A.9.1.14.1Test Purpose and Environment3369

A.9.1.14.2Test parameters3369

A.9.1.14.3Test Requirements3373

A.9.1.15TDD RSRP under Time-Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS3373

A.9.1.15.1Test Purpose and Environment3373

A.9.1.15.2Test parameters3373

A.9.1.15.3Test Requirements3375

A.9.1.16FDD Intra frequency case for 5MHz Bandwidth3376

A.9.1.16.1Test Purpose and Environment3376

A.9.1.16.2Test parameters3376

A.9.1.16.3Test Requirements3377

A.9.1.17FDD—FDD Inter frequency case for 5MHz Bandwidth3377

A.9.1.17.1Test Purpose and Environment3377

A.9.1.17.2Test parameters3378

A.9.1.17.3Test Requirements3379

A.9.1.18FDD RSRP for E-UTRAN Carrier Aggregation for 10MHz + 5MHz3379

A.9.1.18.1Test Purpose and Environment3379

A.9.1.18.2Test parameters3379

A.9.1.18.3Test Requirements3380

A.9.1.19TDD RSRP for E-UTRAN Carrier Aggregation for 10MHz + 5MHz3381

A.9.1.19.1Test Purpose and Environment3381

A.9.1.19.2Test parameters3381

A.9.1.19.3Test Requirements3381

A.9.1.20FDD RSRP for E-UTRAN Carrier Aggregation for 5MHz + 5MHz bandwidth3381

A.9.1.20.1Test Purpose and Environment3381

A.9.1.20.2Test parameters3381

A.9.1.20.3Test Requirements3383

A.9.1.21TDD RSRP for E-UTRAN Carrier Aggregation for 5MHz + 5MHz bandwidth3383

A.9.1.21.1Test Purpose and Environment3383

A.9.1.21.2Test parameters3383

A.9.1.21.3Test Requirements3383

A.9.1.22RSRP for E-UTRAN TDD-FDD Carrier Aggregation with PCell in FDD3383

A.9.1.22.1Test Purpose and Environment3383

A.9.1.22.2Test parameters3384

A.9.1.22.3Test Requirements3388

A.9.1.23 RSRP for E-UTRAN TDD-FDD Carrier Aggregation with PCell in TDD3388

A.9.1.23.1Test Purpose and Environment3388

A.9.1.23.2Test parameters3388

A.9.1.23.3Test Requirements3392

A.9.1.24TDD RSRP for E-UTRAN Carrier Aggregation for 20MHz + 10MHz3392

A.9.1.24.1Test Purpose and Environment3392

A.9.1.24.2Test parameters3392

A.9.1.24.3Test Requirements3393

A.9.1.25FDD intra-frequency absolute and relative RSRP accuracies in CRS based discovery signal3393

A.9.1.25.1Test Purpose and Environment3393

A.9.1.25.2Test parameters3393

A.9.1.25.3Test Requirements3396

A.9.1.26TDD intra-frequency absolute and relative RSRP accuracies in CRS based discovery signal3396

A.9.1.26.1Test Purpose and Environment3396

A.9.1.26.2Test parameters3396

A.9.1.26.3Test Requirements3399

A.9.1.27FDD—FDD inter-frequency absolute and relative RSRP accuracies in CRS based discovery signal3399

A.9.1.27.1Test Purpose and Environment3399

A.9.1.27.2Test parameters3399

A.9.1.27.3Test Requirements3402

A.9.1.28TDD—TDD inter-frequency absolute and relative  RSRP accuracies in CRS based discovery signal3402

A.9.1.28.1Test Purpose and Environment3402

A.9.1.28.2Test parameters3402

A.9.1.28.3Test Requirements3405

A.9.1.29FDD intra frequency absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal3405

A.9.1.29.1Test Purpose and Environment3405

A.9.1.29.2Test parameters3405

A.9.1.29.3Test Requirements3408

A.9.1.30TDD intra frequency absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal3408

A.9.1.30.1Test Purpose and Environment3408

A.9.1.30.2Test parameters3409

A.9.1.30.3Test Requirements3412

A.9.1.31FDD—FDD inter-frequency absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal3412

A.9.1.31.1Test Purpose and Environment3412

A.9.1.31.2Test parameters3412

A.9.1.31.3Test Requirements3415

A.9.1.32TDD—TDD inter-frequency absolute and relative  CSI-RSRP accuracies in CSI-RS based discovery signal3416

A.9.1.32.1Test Purpose and Environment3416

A.9.1.32.2Test parameters3416

A.9.1.32.3Test Requirements3419

A.9.1.33FDD absolute and relative RSRP accuracies for E-UTRAN Carrier Aggregation in CRS based discovery signal3419

A.9.1.33.1Test Purpose and Environment3419

A.9.1.33.2Test parameters3419

A.9.1.33.3Test Requirements3422

A.9.1.34TDD absolute and relative RSRP accuracies for E-UTRAN Carrier Aggregation in CRS based discovery signal3422

A.9.1.34.1Test Purpose and Environment3422

A.9.1.34.2Test parameters3422

A.9.1.34.3Test Requirements3425

A.9.1.35FDD absolute and relative CSI-RSRP accuracies for E-UTRAN Carrier Aggregation in CSI-RS based discovery signal3425

A.9.1.35.1Test Purpose and Environment3425

A.9.1.35.2Test parameters3425

A.9.1.35.3Test Requirements3428

A.9.1.36TDD absolute and relative CSI-RSRP accuracies for E-UTRAN Carrier Aggregation in CSI-RS based discovery signal3429

A.9.1.36.1Test Purpose and Environment3429

A.9.1.36.2Test parameters3429

A.9.1.36.3Test Requirements3432

A.9.1.373 DL PCell in FDD RSRP for E-UTRAN in Carrier Aggregation3432

A.9.1.37.1Test Purpose and Environment3432

A.9.1.37.2Test parameters3432

A.9.1.37.3Test Requirements3435

A.9.1.383 DL PCell in TDD RSRP for E-UTRAN in Carrier Aggregation3436

A.9.1.38.1Test Purpose and Environment3436

A.9.1.38.2Test parameters3436

A.9.1.38.3Test Requirements3439

A.9.1.393 DL FDD RSRP for E-UTRAN in Carrier Aggregation3440

A.9.1.39.1Test Purpose and Environment3440

A.9.1.39.2Test parameters3440

A.9.1.39.3Test Requirements3446

A.9.1.403 DL TDD RSRP for E-UTRAN in Carrier Aggregation3446

A.9.1.40.1Test Purpose and Environment3446

A.9.1.40.2Test parameters3447

A.9.1.40.3Test Requirements3453

A.9.1.41FD-FDD RSRP Intra frequency case for UE category 03453

A.9.1.41.1Test Purpose and Environment3453

A.9.1.41.2Test parameters3453

A.9.1.41.3Test Requirements3456

A.9.1.42HD-FDD RSRP Intra frequency case for UE category 03456

A.9.1.42.1Test Purpose and Environment3456

A.9.1.42.2Test parameters3456

A.9.1.42.3Test Requirements3459

A.9.1.43TDD RSRP Intra frequency case for UE category 03459

A.9.1.43.1Test Purpose and Environment3459

A.9.1.43.2Test parameters3459

A.9.1.43.3Test Requirements3460

A.9.1.444 DL CA PCell in FDD FDD-TDD RSRP for E-UTRAN in Carrier Aggregation3461

A.9.1.44.1Test Purpose and Environment3461

A.9.1.44.2Test parameters3461

A.9.1.44.3Test Requirements3466

A.9.1.454 DL CA PCell in TDD FDD-TDD RSRP for E-UTRAN in Carrier Aggregation3466

A.9.1.45.1Test Purpose and Environment3466

A.9.1.45.2Test parameters3466

A.9.1.45.3Test Requirements3432

A.9.1.464 DL FDD RSRP for E-UTRAN in Carrier Aggregation3432

A.9.1.46.1Test Purpose and Environment3432

A.9.1.46.2Test parameters3432

A.9.1.46.3Test Requirements3441

A.9.1.474 DL TDD RSRP for E-UTRAN in Carrier Aggregation3442

A.9.1.47.1Test Purpose and Environment3442

A.9.1.47.2Test parameters3442

A.9.1.47.3Test Requirements3451

A.9.1.485 DL FDD-TDD with PCell in FDD RSRP for E-UTRAN in Carrier Aggregation3451

A.9.1.48.1Test Purpose and Environment3451

A.9.1.48.2Test parameters3452

A.9.1.48.3Test Requirements3462

A.9.1.495 DL FDD-TDD with PCell in TDD RSRP for E-UTRAN in Carrier Aggregation3463

A.9.1.49.1Test Purpose and Environment3463

A.9.1.49.2Test parameters3463

A.9.1.49.3Test Requirements3473

A.9.1.505 DL FDD RSRP for E-UTRAN in Carrier Aggregation3474

A.9.1.50.1Test Purpose and Environment3474

A.9.1.50.2Test parameters3474

A.9.1.50.3Test Requirements3481

A.9.1.515 DL TDD RSRP for E-UTRAN in Carrier Aggregation3482

A.9.1.51.1Test Purpose and Environment3482

A.9.1.51.2Test parameters3482

A.9.1.51.3Test Requirements3488

A.9.1.52FD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeA3489

A.9.1.52.1Test Purpose and Environment3489

A.9.1.52.2Test parameters3489

A.9.1.52.3Test Requirements3492

A.9.1.52AFD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeA3492

A.9.1.52A.1Test Purpose and Environment3492

A.9.1.52A.2Test parameters3492

A.9.1.52A.3Test Requirements3493

A.9.1.53HD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeA3493

A.9.1.53.1Test Purpose and Environment3493

A.9.1.53.2Test parameters3494

A.9.1.53.3Test Requirements3497

A.9.1.53AHD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeA3497

A.9.1.53A.1Test Purpose and Environment3497

A.9.1.53A.2Test parameters3497

A.9.1.53A.3Test Requirements3498

A.9.1.54TDD RSRP Intra frequency case for Cat-M1 UE in CEModeA3499

A.9.1.54.1Test Purpose and Environment3499

A.9.1.54.2Test parameters3499

A.9.1.54.3Test Requirements3501

A.9.1.55FS3 Intra frequency absolute and relative RSRP accuracies with FDD PCell3501

A.9.1.55.1Test Purpose and Environment3501

A.9.1.55.2Test parameters3501

A.9.1.55.3Test Requirements3505

A.9.1.56FS3 Intra frequency absolute and relative RSRP accuracies with TDD PCell3505

A.9.1.56.1Test Purpose and Environment3505

A.9.1.56.2Test parameters3505

A.9.1.56.3Test Requirements3508

A.9.1.57FD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeB3509

A.9.1.57.1Test Purpose and Environment3509

A.9.1.57.2Test parameters3509

A.9.1.57.3Test Requirements3512

A.9.1.57AFD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeB3512

A.9.1.57A.1Test Purpose and Environment3512

A.9.1.57A.2Test parameters3512

A.9.1.57A.3Test Requirements3513

A.9.1.58HD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeB3513

A.9.1.58.1Test Purpose and Environment3513

A.9.1.58.2Test parameters3514

A.9.1.58.3Test Requirements3517

A.9.1.58AHD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeB3517

A.9.1.58A.1Test Purpose and Environment3517

A.9.1.58A.2Test parameters3517

A.9.1.58A.3Test Requirements3518

A.9.1.59TDD RSRP Intra frequency case for Cat-M1 UE in CEModeB3518

A.9.1.59.1Test Purpose and Environment3518

A.9.1.59.2Test parameters3519

A.9.1.59.3Test Requirements3521

A.9.1.60FS3 Absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal with FDD PCell3521

A.9.1.60.1Test Purpose and Environment3521

A.9.1.60.2Test parameters3521

A.9.1.60.3Test Requirements3524

A.9.1.61FS3 Absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal with TDD PCell3525

A.9.1.61.1Test Purpose and Environment3525

A.9.1.61.2Test parameters3525

A.9.1.61.3Test Requirements3528

A.9.1.62FD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeA3528

A.9.1.62.1Test Purpose and Environment3528

A.9.1.62.2Test parameters3528

A.9.1.62.3Test Requirements3531

A.9.1.63HD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeA3531

A.9.1.53.1Test Purpose and Environment3531

A.9.1.53.2Test parameters3531

A.9.1.63.3Test Requirements3534

A.9.1.64TDD RSRP Inter frequency case for Cat-M1 UE in CEModeA3534

A.9.1.64.1Test Purpose and Environment3534

A.9.1.64.2Test parameters3534

A.9.1.64.3Test Requirements3535

A.9.1.65FD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeB3536

A.9.1.65.1Test Purpose and Environment3536

A.9.1.65.2Test parameters3536

A.9.1.65.3Test Requirements3542

A.9.1.66HD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeB3542

A.9.1.66.1Test Purpose and Environment3542

A.9.1.66.2Test parameters3542

A.9.1.66.3Test Requirements3548

A.9.1.67TDD RSRP Inter frequency case for Cat-M1 UE in CEModeB3548

A.9.1.67.1Test Purpose and Environment3548

A.9.1.67.2Test parameters3548

A.9.1.67.3Test Requirements3549

A.9.1.683 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes3550

A.9.1.68.1Test Purpose and Environment3550

A.9.1.68.2Test parameters3550

A.9.1.68.3Test Requirements3554

A.9.1.694 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes3554

A.9.1.69.1Test Purpose and Environment3554

A.9.1.69.2Test parameters3554

A.9.1.69.3Test Requirements3558

A.9.1.705 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes3559

A.9.1.70.1Test Purpose and Environment3559

A.9.1.70.2Test parameters3559

A.9.1.70.3Test Requirements3571

A.9.1.716 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes3572

A.9.1.71.1Test Purpose and Environment3572

A.9.1.71.2Test parameters3572

A.9.1.71.3Test Requirements3584

A.9.1.727 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes3585

A.9.1.72.1Test Purpose and Environment3585

A.9.1.72.2Test parameters3585

A.9.1.72.3Test Requirements3597

A.9.1.73FDD Intra frequency case for CA Idle Mode Measurements3598

A.9.1.73.1Test Purpose and Environment3598

A.9.1.73.2Test parameters3598

A.9.1.73.3Test Requirements3601

A.9.1.74FDD—FDD Inter frequency case for CA Idle Mode Measurements for overlapping carrier3601

A.9.1.74.1Test Purpose and Environment3601

A.9.1.74.2Test parameters3601

A.9.1.74.3Test Requirements3602

A.9.1.75FDD—FDD Inter frequency case for CA Idle Mode Measurements for non-overlapping carrier3602

A.9.1.75.1Test Purpose and Environment3602

A.9.1.75.2Test parameters3603

A.9.1.75.3Test Requirements3604

A.9.1.76FD-FDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeA3604

A.9.1.76.1Test Purpose and Environment3604

A.9.1.76.2Test parameters3604

A.9.1.76.3Test Requirements3607

A.9.1.77HD-FDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeA3607

A.9.1.77.1Test Purpose and Environment3607

A.9.1.77.2Test parameters3607

A.9.1.77.3Test Requirements3610

A.9.1.78TDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeA3610

A.9.1.78.1Test Purpose and Environment3610

A.9.1.78.2Test parameters3610

A.9.1.78.3Test Requirements3613

A.9.1.79FD-FDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeB3613

A.9.1.79.1Test Purpose and Environment3613

A.9.1.79.2Test parameters3613

A.9.1.79.3Test Requirements3616

A.9.1.80HD-FDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeB3616

A.9.1.80.1Test Purpose and Environment3616

A.9.1.80.2Test parameters3616

A.9.1.80.3Test Requirements3619

A.9.1.81TDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeB3619

A.9.1.81.1Test Purpose and Environment3619

A.9.1.78.2Test parameters3619

A.9.1.81.3Test Requirements3622

A.9.2RSRQ3622

A.9.2.1FDD Intra frequency case3622

A.9.2.1.1Test Purpose and Environment3622

A.9.2.1.2Test parameters3622

A.9.2.1.3Test Requirements3625

A.9.2.2TDD Intra frequency case3625

A.9.2.2.1Test Purpose and Environment3625

A.9.2.2.2Test parameters3625

A.9.2.2.3Test Requirements3627

A.9.2.3FDD—FDD Inter frequency case3627

A.9.2.3.1Test Purpose and Environment3627

A.9.2.3.2Test parameters3627

A.9.2.3.3Test Requirements3630

A.9.2.4TDD—TDD Inter frequency case3630

A.9.2.4.1Test Purpose and Environment3630

A.9.2.4.2Test parameters3630

A.9.2.4.3Test Requirements3632

A.9.2.4AFDD—TDD Inter frequency case3633

A.9.2.4A.1Test Purpose and Environment3633

A.9.2.4A.2Test parameters3633

A.9.2.4A.3Test Requirements3635

A.9.2.5FDD RSRQ for E-UTRA Carrier Aggregation3635

A.9.2.5.1Test Purpose and Environment3635

A.9.2.5.2Test parameters3636

A.9.2.5.3Test Requirements3639

A.9.2.6TDD RSRQ for E-UTRA Carrier Aggregation3639

A.9.2.6.1Test Purpose and Environment3639

A.9.2.6.2Test parameters3639

A.9.2.6.3Test Requirements3642

A.9.2.7FDD RSRQ under Time Domain Measurement Resource Restriction with Non-MBSFN ABS3642

A.9.2.7.1Test Purpose and Environment3642

A.9.2.7.2Test parameters3642

A.9.2.7.3Test Requirements3646

A.9.2.8TDD RSRQ under Time Domain Measurement Resource Restriction with Non-MBSFN ABS3646

A.9.2.8.1Test Purpose and Environment3646

A.9.2.8.2Test parameters3646

A.9.2.8.3Test Requirements3650

A.9.2.9FDD RSRQ under Time Domain Measurement Resource Restriction with MBSFN ABS3650

A.9.2.9.1Test Purpose and Environment3650

A.9.2.9.2Test parameters3650

A.9.2.9.3Test Requirements3654

A.9.2.10TDD Intra frequency case under time domain measurement resource restriction with MBSFN ABS3654

A.9.2.10.1Test Purpose and Environment3654

A.9.2.10.2Test parameters3654

A.9.2.10.3Test Requirements3658

A.9.2.11FDD RSRQ for E-UTRA Carrier Aggregation (20MHz bandwidth)3658

A.9.2.11.1Test Purpose and Environment3658

A.9.2.11.2Test parameters3658

A.9.2.11.3Test Requirements3659

A.9.2.12TDD RSRQ for E-UTRA Carrier Aggregation (20MHz bandwidth)3659

A.9.2.12.1Test Purpose and Environment3659

A.9.2.12.2Test parameters3660

A.9.2.12.3Test Requirements3660

A.9.2.13Void3661

A.9.2.13.1Void3661

A.9.2.13.2Void3661

A.9.2.13.3Void3661

A.9.2.14Void3661

A.9.2.14.1Void3661

A.9.2.14.2Void3661

A.9.2.14.3Void3661

A.9.2.15FDD RSRQ under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS3661

A.9.2.15.1Test Purpose and Environment3661

A.9.2.15.2Test parameters3661

A.9.2.15.3Test Requirements3665

A.9.2.16TDD RSRQ under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS3665

A.9.2.16.1Test Purpose and Environment3665

A.9.2.16.2Test parameters3665

A.9.2.16.3Test Requirements3670

A.9.2.17FDD Intra frequency case for 5 MHz bandwidth3670

A.9.2.17.1Test Purpose and Environment3670

A.9.2.17.2Test parameters3670

A.9.2.17.3Test Requirements3672

A.9.2.18FDD—FDD Inter frequency case for 5MHz bandwidth3672

A.9.2.18.1Test Purpose and Environment3672

A.9.2.18.2Test parameters3672

A.9.2.18.3Test Requirements3675

A.9.2.19FDD-FDD Inter Frequency WB-RSRQ3675

A.9.2.19.1Test Purpose and Environment3675

A.9.2.19.2Test parameters3675

A.9.2.19.3Test Requirements3677

A.9.2.20TDD—TDD Inter Frequency WB-RSRQ3677

A.9.2.20.1Test Purpose and Environment3677

A.9.2.20.2Test parameters3677

A.9.2.20.3Test Requirements3680

A.9.2.21FDD RSRQ for E-UTRAN Carrier Aggregation for 10MHz+5MHz3680

A.9.2.21.1Test Purpose and Environment3680

A.9.2.21.2Test parameters3680

A.9.2.21.3Test Requirements3683

A.9.2.22TDD RSRQ for E-UTRAN Carrier Aggregation for 10MHz+5MHz3683

A.9.2.22.1Test Purpose and Environment3684

A.9.2.22.2Test parameters3684

A.9.2.22.3Test Requirements3684

A.9.2.23FDD RSRQ for E-UTRA Carrier Aggregation (5MHz + 5MHz bandwidth)3684

A.9.2.23.1Test Purpose and Environment3684

A.9.2.23.2Test parameters3684

A.9.2.23.3Test Requirements3687

A.9.2.24TDD RSRQ for E-UTRA Carrier Aggregation (5MHz + 5MHz bandwidth)3687

A.9.2.24.1Test Purpose and Environment3687

A.9.2.24.2Test parameters3687

A.9.2.24.3Test Requirements3688

A.9.2.25RSRQ for E-UTRAN TDD-FDD Carrier Aggregation with PCell in FDD3688

A.9.2.25.1Test Purpose and Environment3688

A.9.2.25.2Test parameters3688

A.9.2.25.3Test Requirements3693

A.9.2.26RSRQ for E-UTRAN TDD-FDD Carrier Aggregation with PCell in TDD3693

A.9.2.26.1Test Purpose and Environment3693

A.9.2.26.2Test parameters3693

A.9.2.26.3Test Requirements3697

A.9.2.27TDD RSRQ for E-UTRAN Carrier Aggregation for 20MHz+10MHz3697

A.9.2.27.1Test Purpose and Environment3697

A.9.2.27.2Test parameters3697

A.9.2.27.3Test Requirements3698

A.9.2.28FDD intra-frequency absolute RSRQ accuracy with CRS based discovery signal3698

A.9.2.28.1Test Purpose and Environment3698

A.9.2.28.2Test parameters3698

A.9.2.28.3Test Requirements3701

A.9.2.29TDD intra-frequency absolute RSRQ accuracy with CRS based discovery signal3701

A.9.2.29.1Test Purpose and Environment3701

A.9.2.29.2Test parameters3701

A.9.2.29.3Test Requirements3704

A.9.2.30FDD-FDD inter-frequency absolute and relative RSRQ accuracies with CRS based discovery signal3704

A.9.2.30.1Test Purpose and Environment3704

A.9.2.30.2Test parameters3704

A.9.2.30.3Test Requirements3707

A.9.2.31TDD-TDD inter-frequency absolute and relative RSRQ accuracies with CRS based discovery signal3707

A.9.2.31.1Test Purpose and Environment3707

A.9.2.31.2Test parameters3707

A.9.2.31.3Test Requirements3710

A.9.2.32FDD absolute and relative RSRQ accuracy for E-UTRAN Carrier Aggregation in CRS based discovery signal3710

A.9.2.32.1Test Purpose and Environment3710

A.9.2.32.2Test parameters3710

A.9.2.32.3Test Requirements3713

A.9.2.33TDD absolute and relative RSRQ accuracy for E-UTRAN Carrier Aggregation in CRS based discovery signal3713

A.9.2.33.1Test Purpose and Environment3713

A.9.2.33.2Test parameters3713

A.9.2.33.3Test Requirements3717

A.9.2.34FDD—FDD Inter frequency new RSRQ3717

A.9.2.34.1Test Purpose and Environment3717

A.9.2.34.2Test parameters3717

A.9.2.34.3Test Requirements3720

A.9.2.35TDD—TDD Inter frequency new RSRQ3720

A.9.2.35.1Test Purpose and Environment3720

A.9.2.35.2Test parameters3720

A.9.2.35.3Test Requirements3723

A.9.2.36FDD—FDD Inter frequency RSRQ measured on all OFDM symbols3723

A.9.2.36.1Test Purpose and Environment3723

A.9.2.36.2Test parameters3723

A.9.2.36.3Test Requirements3724

A.9.2.37TDD—TDD Inter frequency RSRQ measurement on all OFDM symbols3725

A.9.2.37.1Test Purpose and Environment3725

A.9.2.37.2Test parameters3725

A.9.2.37.3Test Requirements3726

A.9.2.383 DL PCell in FDD RSRQ for E-UTRAN in Carrier Aggregation3727

A.9.2.38.1Test Purpose and Environment3727

A.9.2.38.2Test parameters3727

A.9.2.38.3Test Requirements3731

A.9.2.393 DL PCell in TDD RSRQ for E-UTRAN in Carrier Aggregation3731

A.9.2.39.1Test Purpose and Environment3731

A.9.2.39.2Test parameters3731

A.9.2.39.3Test Requirements3735

A.9.2.403 DL FDD RSRQ for E-UTRAN in Carrier Aggregation3735

A.9.2.40.1Test Purpose and Environment3735

A.9.2.40.2Test parameters3735

A.9.2.40.3Test Requirements3738

A.9.2.413 DL TDD RSRQ for E-UTRAN in Carrier Aggregation3739

A.9.2.41.1Test Purpose and Environment3739

A.9.2.41.2Test parameters3739

A.9.2.41.3Test Requirements3742

A.9.2.42FD-FDD RSRQ Intra frequency case for UE category 03742

A.9.2.42.1Test Purpose and Environment3742

A.9.2.42.2Test parameters3742

A.9.2.42.3Test Requirements3745

A.9.2.43HD-FDD RSRQ Intra frequency case for UE category 03745

A.9.2.43.1Test Purpose and Environment3745

A.9.2.43.2Test parameters3745

A.9.2.43.3Test Requirements3748

A.9.2.44TDD RSRQ Intra frequency case for UE category 03748

A.9.2.44.1Test Purpose and Environment3748

A.9.2.44.2Test parameters3748

A.9.2.44.3Test Requirements3750

A.9.2.454 DL CA PCell in FDD FDD-TDD RSRQ for E-UTRAN in Carrier Aggregation3750

A.9.2.45.1Test Purpose and Environment3750

A.9.2.45.2Test parameters3750

A.9.2.45.3Test Requirements3754

A.9.2.464 DL CA PCell in TDD TDD-FDD RSRQ for E-UTRAN in Carrier Aggregation3755

A.9.2.46.1Test Purpose and Environment3755

A.9.2.46.2Test parameters3755

A.9.2.46.3Test Requirements3759

A.9.2.475 DL FDD-TDD with PCell in FDD RSRQ for E-UTRAN in Carrier Aggregation3760

A.9.2.47.1Test Purpose and Environment3760

A.9.2.47.2Test parameters3760

A.9.2.47.3Test Requirements3764

A.9.2.485 DL FDD-TDD with PCell in TDD RSRQ for E-UTRAN in Carrier Aggregation3764

A.9.2.48.1Test Purpose and Environment3764

A.9.2.48.2Test parameters3765

A.9.2.48.3Test Requirements3769

A.9.2.495 DL FDD RSRQ for E-UTRAN in Carrier Aggregation3770

A.9.2.49.1Test Purpose and Environment3770

A.9.2.49.2Test parameters3770

A.9.2.49.3Test Requirements3776

A.9.2.505 DL TDD RSRQ for E-UTRAN in Carrier Aggregation3777

A.9.2.50.1Test Purpose and Environment3777

A.9.2.50.2Test parameters3777

A.9.2.50.3Test Requirements3783

A.9.2.51FS3 Intra frequency absolute and relative RSRQ accuracies with FDD PCell3783

A.9.2.51.1Test Purpose and Environment3783

A.9.2.51.2Test parameters3784

A.9.2.51.3Test Requirements3788

A.9.2.52FS3 Intra frequency absolute and relative RSRQ accuracies with TDD PCell3788

A.9.2.52.1Test Purpose and Environment3788

A.9.2.52.2Test parameters3788

A.9.2.52.3Test Requirements3791

A.9.2.534DL FDD RSRQ for E-UTRAN in Carrier Aggregation3792

A.9.2.53.1Test Purpose and Environment3792

A.9.2.53.2Test parameters3792

A.9.2.53.3Test Requirements3798

A.9.2.544DL TDD RSRQ for E-UTRAN in Carrier Aggregation3799

A.9.2.54.1Test Purpose and Environment3799

A.9.2.54.2Test parameters3799

A.9.2.54.3Test Requirements3805

A.9.2.553 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes3805

A.9.2.55.1Test Purpose and Environment3805

A.9.2.55.2Test parameters3806

A.9.2.55.3Test Requirements3811

A.9.2.564 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes3811

A.9.2.56.1Test Purpose and Environment3811

A.9.2.56.2Test parameters3811

A.9.2.56.3Test Requirements3816

A.9.2.575 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes3816

A.9.2.57.1Test Purpose and Environment3816

A.9.2.57.2Test parameters3817

A.9.2.57.3Test Requirements3821

A.9.2.586 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes3822

A.9.2.58.1Test Purpose and Environment3822

A.9.2.58.2Test parameters3822

A.9.2.58.3Test Requirements3826

A.9.2.597 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes3827

A.9.2.59.1Test Purpose and Environment3827

A.9.2.59.2Test parameters3827

A.9.2.59.3Test Requirements3832

A.9.2.60FDD Intra frequency case for CA Idle Mode Measurements3833

A.9.2.60.1Test Purpose and Environment3833

A.9.2.60.2Test parameters3833

A.9.2.60.3Test Requirements3836

A.9.2.61FDD—FDD Inter frequency case for CA Idle Mode Measurements on overlapping carrier3836

A.9.2.61.1Test Purpose and Environment3836

A.9.2.61.2Test parameters3836

A.9.2.61.3Test Requirements3839

A.9.2.62FDD—FDD Inter frequency case for CA Idle Mode Measurements on non-overlapping carrier3839

A.9.2.62.1Test Purpose and Environment3839

A.9.2.62.2Test parameters3839

A.9.2.62.3Test Requirements3842

A.9.3UTRAN FDD CPICH RSCP3842

A.9.3.1E-UTRAN FDD3842

A.9.3.1.1Test Purpose and Environment3842

A.9.3.1.2Parameters3842

A.9.3.1.3Test Requirements3845

A.9.3.2 E-UTRAN TDD3845

A.9.3.2.1Test Purpose and Environment3845

A.9.3.2.2Parameters3845

A.9.3.2.3Test Requirements3848

A.9.3.3E-UTRAN FDD for 5MHz Bandwidth3848

A.9.3.3.1Test Purpose and Environment3848

A.9.3.3.2Parameters3848

A.9.3.3.3Test Requirements3849

A.9.4UTRAN FDD CPICH Ec/No3850

A.9.4.1E-UTRAN FDD3850

A.9.4.1.1Test Purpose and Environment3850

A.9.4.1.2Parameters3850

A.9.4.1.3Test Requirements3852

A.9.4.2E-UTRAN TDD3853

A.9.4.2.1Test Purpose and Environment3853

A.9.4.2.2Parameters3853

A.9.4.2.3Test Requirements3855

A.9.4.3E-UTRAN FDD for 5MHz Bandwidth3856

A.9.4.3.1Test Purpose and Environment3856

A.9.4.3.2Parameters3856

A.9.4.3.3Test Requirements3857

A.9.5UTRAN TDD measurement3857

A.9.5.1P-CCPCH RSCP absolute accuracy for E-UTRAN FDD3857

A.9.5.1.1Test Purpose and Environment3857

A.9.5.1.2Test parameters3857

A.9.5.1.3Test Requirements3859

A.9.5.2P-CCPCH RSCP absolute accuracy for E-UTRAN TDD3859

A.9.5.2.1Test Purpose and Environment3859

A.9.5.2.2Test parameters3859

A.9.5.2.3Test Requirements3861

A.9.6GSM Carrier RSSI3862

A.9.6.1E-UTRAN FDD3862

A.9.6.1.1Test Purpose and Environment3862

A.9.6.1.2Test Requirements3863

A.9.6.2E-UTRAN TDD3863

A.9.6.2.1Test Purpose and Environment3863

A.9.6.2.2Test Requirements3865

A.9.7UE Rx – Tx Time Difference3866

A.9.7.1E-UTRAN FDD UE Rx – Tx time difference case3866

A.9.7.1.1Test Purpose and Environment3866

A.9.7.1.2Test parameters3866

A.9.7.1.3Test Requirements3867

A.9.7.2E-UTRA TDD UE Rx – Tx time difference case3867

A.9.7.2.1Test Purpose and Environment3867

A.9.7.2.2Test parameters3867

A.9.7.2.3Test Requirements3869

A.9.7.3E-UTRAN FDD UE Rx–Tx Time Difference under Time-Domain Measurement Resource Restriction with Non-MBSFN ABS3869

A.9.7.3.1Test Purpose and Environment3869

A.9.7.3.2Test parameters3869

A.9.7.3.3Test Requirements3872

A.9.7.4E-UTRAN TDD UE Rx-Tx Time Difference under Time-Domain Measurement Resource Restriction with Non-MBSFN ABS3872

A.9.7.4.1Test Purpose and Environment3872

A.9.7.4.2Test Parameters3872

A.9.7.4.3Test Requirements3875

A.9.7.5E-UTRAN FDD UE Rx–Tx time difference under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS3875

A.9.7.5.1Test Purpose and Environment3875

A.9.7.5.2Test parameters3875

A.9.7.5.3Test Requirements3878

A.9.7.6E-UTRAN TDD UE Rx-Tx Time Difference under Time-Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS3878

A.9.7.6.1Test Purpose and Environment3878

A.9.7.6.2Test Parameters3878

A.9.7.6.3Test Requirements3881

A.9.7.7E-UTRAN FDD UE Rx-Tx time difference case for Cat-M1/M2 UE in CEModeA3881

A.9.7.7.1Test Purpose and Environment3881

A.9.7.7.2Test parameters3881

A.9.7.7.3Test Requirements3882

A.9.7.8E-UTRAN HD-FDD UE Rx-Tx time difference case for Cat-M1/M2 UE in CEModeA3883

A.9.7.8.1Test Purpose and Environment3883

A.9.7.8.2Test parameters3883

A.9.7.8.3Test Requirements3884

A.9.7.9E-UTRAN TDD UE Rx-Tx time difference case for Cat-M1/M2 UE in CEModeA3884

A.9.7.9.1Test Purpose and Environment3884

A.9.7.9.2Test parameters3884

A.9.7.9.3Test Requirements3885

A.9.8RSTD3886

A.9.8.1E-UTRAN FDD RSTD intra frequency case3886

A.9.8.1.1Test Purpose and Environment3886

A.9.8.1.2Test Requirements3888

A.9.8.1.2ATest Requirements for UE Category 1bis3888

A.9.8.2E-UTRAN TDD RSTD intra frequency case3889

A.9.8.2.1Test Purpose and Environment3889

A.9.8.2.2Test Requirements3892

A.9.8.2.2ATest Requirements for UE Category 1bis3892

A.9.8.3E-UTRAN FDD-FDD RSTD inter frequency case3893

A.9.8.3.1Test Purpose and Environment3893

A.9.8.3.2Test Requirements3895

A.9.8.3.2ATest Requirements for UE Category 1bis3895

A.9.8.4E-UTRAN TDD-TDD RSTD inter frequency case3896

A.9.8.4.1Test Purpose and Environment3896

A.9.8.4.2Test Requirements3898

A.9.8.4.2ATest Requirements for UE Category 1bis3898

A.9.8.5E-UTRAN FDD RSTD Measurement Accuracy in Carrier Aggregation3899

A.9.8.5.1Test Purpose and Environment3899

A.9.8.5.2Test Requirements3901

A.9.8.6E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation3901

A.9.8.6.1Test Purpose and Environment3901

A.9.8.6.2Test Requirements3904

A.9.8.7E-UTRAN FDD RSTD Measurement Accuracy in Carrier Aggregation for 20MHz bandwidth3904

A.9.8.7.1Test Purpose and Environment3904

A.9.8.7.2Test Requirements3905

A.9.8.8E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation for 20MHz bandwidth3905

A.9.8.8.1Test Purpose and Environment3905

A.9.8.8.2Test Requirements3906

A.9.8.9E-UTRAN FDD RSTD Measurement Accuracy in Carrier Aggregation for 10MHz+5MHz3906

A.9.8.9.1Test Purpose and Environment3906

A.9.8.9.2Test Requirements3907

A.9.8.10E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation for 10MHz+5MHz3907

A.9.8.10.1Test Purpose and Environment3907

A.9.8.10.2Test Requirements3908

A.9.8.11E-UTRAN FDD RSTD Measurement Accuracy in Carrier Aggregation for 5 + 5MHz bandwidth3908

A.9.8.11.1Test Purpose and Environment3908

A.9.8.11.2Test Requirements3909

A.9.8.12E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation for 5+5MHz bandwidth3909

A.9.8.12.1Test Purpose and Environment3909

A.9.8.12.2Test Requirements3910

A.9.8.13E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation for 20MHz+10MHz3910

A.9.8.13.1Test Purpose and Environment3910

A.9.8.13.2Test Requirements3911

A.9.8.14E-UTRAN FDD RSTD Measurement Accuracy in 3DL Carrier Aggregation3911

A.9.8.14.1Test Purpose and Environment3911

A.9.8.14.2Test Requirements3918

A.9.8.15E-UTRAN TDD RSTD Measurement Accuracy in 3DL Carrier Aggregation3918

A.9.8.15.1Test Purpose and Environment3918

A.9.8.15.2Test Requirements3924

A.9.8.16HD – FDD Intra frequency case for UE Category NB1 inband mode in normal coverage3924

A.9.8.16.1Test Purpose and Environment3924

A.9.8.16.2Test Requirements3927

A.9.8.17HD – FDD Inter frequency case for UE Category NB1 inband mode in normal coverage3927

A.9.8.17.1Test Purpose and Environment3927

A.9.8.17.2Test Requirements3930

A.9.8.18HD – FDD Intra frequency case for UE Category NB1 inband mode in enhanced coverage3930

A.9.8.18.1Test Purpose and Environment3930

A.9.8.18.2Test Requirements3933

A.9.8.19HD – FDD Inter frequency case for UE Category NB1 inband mode in enhanced coverage3933

A.9.8.19.1Test Purpose and Environment3933

A.9.8.19.2Test Requirements3936

A.9.8.20E-UTRAN FDD RSTD intra-frequency measurement accuracy in CE Mode A3936

A.9.8.20.1Test Purpose and Environment3936

A.9.8.20.2Test Requirements3939

A.9.8.21E-UTRAN HD-FDD RSTD intra-frequency measurement accuracy in CEModeA3940

A.9.8.21.1Test Purpose and Environment3940

A.9.8.21.2Test Requirements3943

A.9.8.22E-UTRAN TDD RSTD intra-frequency measurement accuracy in CE Mode A3944

A.9.8.22.1Test Purpose and Environment3944

A.9.8.22.2Test Requirements3947

A.9.8.23E-UTRAN FDD RSTD intra-frequency measurement accuracy in CE Mode B3948

A.9.8.23.1Test Purpose and Environment3948

A.9.8.23.2Test Requirements3951

A.9.8.24E-UTRAN HD-FDD RSTD intra-frequency measurement accuracy in CE Mode B3951

A.9.8.24.1Test Purpose and Environment3951

A.9.8.24.2Test Requirements3955

A.9.8.25E-UTRAN TDD RSTD intra-frequency measurement accuracy in CE Mode B3956

A.9.8.25.1Test Purpose and Environment3956

A.9.8.25.2Test Requirements3959

A.9.8.26E-UTRAN FDD-FDD RSTD inter-frequency measurement accuracy in CE Mode A3960

A.9.8.26.1Test Purpose and Environment3960

A.9.8.26.2Test Requirements3962

A.9.8.27E-UTRAN HD-FDD RSTD inter-frequency measurement accuracy in CE Mode A3962

A.9.8.27.1Test Purpose and Environment3962

A.9.8.27.2Test Requirements3965

A.9.8.28E-UTRAN TDD RSTD inter-frequency measurement accuracy in CE Mode A3965

A.9.8.28.1Test Purpose and Environment3965

A.9.8.28.2Test Requirements3968

A.9.8.29E-UTRAN FDD-FDD RSTD inter-frequency measurement accuracy in CE Mode B3968

A.9.8.29.1Test Purpose and Environment3968

A.9.8.29.2Test Requirements3972

A.9.8.30E-UTRAN HD-FDD RSTD inter-frequency measurement accuracy in CE Mode B3973

A.9.8.30.1Test Purpose and Environment3973

A.9.8.30.2Test Requirements3976

A.9.8.31E-UTRAN TDD RSTD inter-frequency measurement accuracy in CE Mode B3977

A.9.8.31.1Test Purpose and Environment3977

A.9.8.31.2Test Requirements3981

A.9.8.32TDD Intra frequency case for UE Category NB1 inband mode in normal coverage3981

A.9.8.32.1Test Purpose and Environment3981

A.9.8.32.2Test Requirements3984

A.9.8.33TDD Inter frequency case for UE Category NB1 inband mode in normal coverage3984

A.9.8.33.1Test Purpose and Environment3984

A.9.8.33.2Test Requirements3987

A.9.8.34TDD Intra frequency case for UE Category NB1 inband mode in enhanced coverage3987

A.9.8.34.1Test Purpose and Environment3987

A.9.8.34.2Test Requirements3990

A.9.8.35TDD Inter frequency case for UE Category NB1 inband mode in enhanced coverage3990

A.9.8.35.1Test Purpose and Environment3990

A.9.8.35.2Test Requirements3993

A.9.9RSRP and RSRQ on the serving cell3993

A.9.9.1FDD Intra frequency serving cell case3993

A.9.9.1.1Test Purpose and Environment3993

A.9.9.1.2Test parameters3993

A.9.9.1.3Test Requirements3996

A.9.9.2TDD Intra frequency serving cell case3996

A.9.9.2.1Test Purpose and Environment3996

A.9.9.2.2Test parameters3996

A.9.9.2.3Test Requirements3998

A.9.10SSTD3998

A.9.10.1EUTRAN FDD-FDD SSTD accuracy in asynchronous DC3998

A.9.10.1.1Test Purpose and Environment3998

A.9.10.1.2Test parameters3998

A.9.10.1.3Test Requirements4000

A.9.10.2Void4000

A.9.10.3Void4000

A.9.10.4Void4000

A.9.11 RSSI4000

A.9.11.1FS3 average RSSI accuracy case (PCell using FDD)4000

A.9.11.1.1Test Purpose and Environment4000

A.9.11.1.2Test parameters4000

A.9.11.1.3Test Requirements4003

A.9.11.2FS3 average RSSI accuracy case (PCell using TDD)4003

A.9.11.2.1Test Purpose and Environment4003

A.9.11.2.2Test parameters4003

A.9.12Channel occupancy4006

A.9.12.1FS3 channel occupancy test (PCell using FDD)4006

A.9.12.1.1Test Purpose and Environment4006

A.9.12.1.2Test parameters4006

A.9.12.1.3Test Requirements4009

A.9.12.2FS3 channel occupancy test (PCell using TDD)4009

A.9.12.2.1Test Purpose and Environment4009

A.9.12.2.2Test parameters4009

A.9.12.2.3Test Requirements4012

A.9.13RS-SINR4012

A.9.13.1FDD Intra-Frequency Case4012

A.9.13.1.1Test Purpose and Environment4012

A.9.13.1.2Test parameters4012

A.9.13.1.3Test Requirements4015

A.9.13.2TDD Intra-Frequency Case4015

A.9.13.2.1Test Purpose and Environment4015

A.9.13.2.2Test parameters4015

A.9.13.2.3Test Requirements4018

A.9.13.3FDD—FDD Inter frequency case4018

A.9.13.3.1Test Purpose and Environment4018

A.9.13.3.2Test parameters4018

A.9.13.3.3Test Requirements4021

A.9.13.4TDD—TDD Inter frequency case4021

A.9.13.4.1Test Purpose and Environment4021

A.9.13.4.2Test parameters4021

A.9.13.4.3Test Requirements4025

A.9.13.5FDD—TDD Inter frequency case4026

A.9.13.5.1Test Purpose and Environment4026

A.9.13.5.2Test parameters4026

A.9.13.5.3Test Requirements4032

A.9.13.6TDD—FDD Inter frequency case4032

A.9.13.6.1Test Purpose and Environment4032

A.9.13.6.2Test parameters4032

A.9.13.6.3Test Requirements4036

A.9.14Channel quality reporting accuracy4036

A.9.14.1E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category NB1 Standalone mode under normal coverage4036

A.9.14.1.1Test Purpose and Environment4036

A.9.14.1.2Test parameters4037

A.9.14.1.3Test Requirements4037

A.9.14.2E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category NB1 Standalone mode under enhanced coverage4038

A.9.14.2.1Test Purpose and Environment4038

A.9.14.2.2Test parameters4038

A.9.14.2.3Test Requirements4039

A.9.14.3E-UTRAN HD-FDD Downlink channel quality reporting accuracy on non-anchor carrier for UE Category NB1 Standalone mode under normal coverage4039

A.9.14.3.1Test Purpose and Environment4039

A.9.14.3.2Test parameters4039

A.9.14.3.3Test Requirements4040

A.9.14.4E-UTRAN HD-FDD Downlink channel quality reporting accuracy on non-anchor carrier for UE Category NB1 Standalone mode under enhanced coverage4040

A.9.14.4.1Test Purpose and Environment4040

A.9.14.4.2Test parameters4040

A.9.14.4.3Test Requirements4041

A.10Proximity-based Services in Any Cell Selection State4064

A.10.1E-UTRAN FDD – UE ProSe Direct Communication Transmission Timing Accuracy Test4064

A.10.1.1Test Purpose and Environment4064

A.10.1.2Test Requirements4065

A.10.2E-UTRAN FDD – Initiation/Cease of SLSS Transmission with ProSe Direct Communication4066

A.10.2.1Test Purpose and Environment4066

A.10.2.2Test Requirements4067

A.10.3E-UTRAN FDD – SyncRef UE Selection / Reselection Test4067

A.10.3.1Test Purpose and Environment4067

A.10.3.2Test Requirements4069

A.10.4E-UTRAN FDD – Cell Identification on downlink frequency associated with ProSe frequency (when UE is transmitting for ProSe)4070

A.10.4.1Test Purpose and Environment4070

A.10.4.2Test Requirements4072

A.11V2V Sidelink Communication for V2V Operation on Dedicated V2V Carrier4072

A.11.1V2V UE Transmission Timing Accuracy Test4072

A.11.1.1Test Purpose and Environment4072

A.11.1.2Test requirements4073

A.11.2Interruptions due to V2V sidelink communication4073

A.11.2.1Test Purpose and Environment4073

A.11.2.2Test Requirements4075

A.124075

A.12.1V2X UE Transmission Timing Accuracy Test4075

A.12.1.1V2X UE Transmission Timing Accuracy Test for eNB as Timing Reference4075

A.12.1.1.1Test Purpose and Environment4075

A.12.1.1.2Test requirements4076

A.12.1.2V2X UE Transmission Timing Accuracy Test for SyncRef UE as Timing Reference4077

A.12.1.2.1Test Purpose and Environment4077

A.12.1.2.2Test Requirements4077

A.12.2Initiation/Cease of SLSS Transmission with V2X Sidelink Communication4078

A.12.2.1Initiation/Cease of SLSS Transmission with V2X Sidelink Communication for eNB as Timing Reference4078

A.12.2.1.1Test Purpose and Environment4078

A.12.2.1.2Test Requirements4079

A.12.2.2Initiation/Cease of SLSS Transmission with V2X Sidelink Communication for SyncRef UE as Timing Reference4080

A.12.2.2.1Test Purpose and Environment4080

A.12.2.2.2Test Requirements4081

A.12.3V2X Synchronization Reference Selection/Reselection Tests4081

A.12.3.1V2X Synchronization Reference Selection/Reselection Tests for GNSS configured as the highest priority4081

A.12.3.1.1Test Purpose and Environment4081

A.12.3.1.2Test Requirements4084

A.12.3.2V2X Synchronization Reference Selection/Reselection Tests for eNB configured as the highest priority4085

A.12.3.2.1Test Purpose and Environment4085

A.12.3.1.2Test Requirements4087

A.12.4Congestion Control Measurement Test for V2X UE4087

A.12.4.1Test Purpose and Environment4087

A.12.4.2Test Requirements4089

A.12.5Interruptions due to V2X Sidelink Communication4089

A.12.5.1Test Purpose and Environment4089

A.12.5.2Test Requirements4091

A.12.6V2X UE Autonomous Resource Selection/Reselection Measurement Test4091

A.12.6.1V2X UE Autonomous Resource Selection/Reselection Tests for PSSCH-RSRP measurements4091

A.12.6.1.1Test Purpose and Environment4091

A.12.6.1.2Test Requirements4093

A.12.6.2V2X UE Autonomous Resource Selection/Reselection Tests for S-RSSI measurements4093

A.12.6.2.1Test Purpose and Environment4093

A.12.6.1.2Test Requirements4095

A.12.7V2X Synchronization Reference Selection/Reselection Tests for V2X Carrier Aggregation4095

A.12.7.1Test Purpose and Environment4095

A.12.7.2Test Requirements4098

A.12.8Interruptions due to V2X Carrier Aggregation4099

A.12.8.1Interruptions on a FDD PCell4099

A.12.8.1.1Test Purpose and Environment4099

A.12.8.1.2Test Requirements4100

A.12.8.2Interruptions on a TDD PCell4100

A.12.8.2.1Test Purpose and Environment4100

A.12.8.2.2Test Requirements4102

A.13E-UTRAN Standalone Tests for UE Category NB for Satellite Access4103

A.13.1RRC_IDLE state for satellite access4103

A.13.1.1Cell re-selection for satellite access4103

A.13.1.1.1HD – FDD and TDD Intra frequency case for UE Category NB1 Standalone mode in normal coverage4103

A.13.1.1.1.1Test Purpose and Environment4103

A.13.1.1.1.2Test Requirements4105

A.13.1.1.2HD – FDD Intra frequency case for UE Category NB1 Standalone mode in normal coverage with serving cell RRM measurement relaxation4106

A.13.1.1.2.1Test Purpose and Environment4106

A.13.1.1.3HD – FDD and TDD Intra frequency case for UE Category NB1 Standalone mode in normal coverage with UE specific DRX4109

A.13.1.1.3.1Test Purpose and Environment4109

A.13.1.1.3.2Test Requirements4111

A.13.1.1.4HD – FDD and TDD Inter frequency case for UE Category NB1 Standalone mode in normal coverage4112

A.13.1.1.4.1Test Purpose and Environment4112

A.13.1.1.4.2Test Requirements4113

A.13.1.1.5HD – FDD Intra frequency case for UE Category NB1 Standalone mode in enhanced coverage, location-based cell reselection for NGSO4114

A.13.1.1.5.1Test Purpose and Environment4114

A.13.1.1.5.2Test Requirements4116

A.13.1.1.6HD – FDD Inter frequency case for UE Category NB1 Standalone mode in enhanced coverage, time-based cell reselection for NGSO4117

A.13.1.1.6.1Test Purpose and Environment4117

A.13.1.1.6.2Test Requirements4118

A.13.1.1.7HD – FDD Intra frequency case for UE Category NB1 in in-band mode in NTN NR in normal coverage4119

A.13.1.1.7.1Test Purpose and Environment4119

A.13.1.1.7.2Test Requirements4121

A.13.1.1.8HD – FDD Inter-frequency case for UE Category NB1 in-band mode in NTN NR in normal coverage4122

A.13.1.1.8.1Test Purpose and Environment4122

A.13.1.1.8.2Test Requirements4124

A.13.2Void4125

A.13.3RRC connection mobility control for satellite access4125

A.13.3.1RRC re-establishment for satellite access4125

A.13.3.1.1HD-FDD and TDD Intra-frequency RRC Re-establishment for UE category NB1 in Standalone mode under normal coverage4125

A.13.3.1.1.1Test Purpose and Environment4125

A.13.3.1.1.2Test Requirements4126

A.13.3.1.2HD-FDD Intra-frequency RRC Re-establishment for UE category NB1 in Standalone mode under enhanced coverage4127

A.13.3.1.2.1Test Purpose and Environment4127

A.13.3.1.2.2Test Requirements4128

A.13.3.1.3HD-FDD Inter-frequency RRC Re-establishment for UE category NB1 in Standalone mode under enhanced coverage4129

A.13.3.1.3.1Test Purpose and Environment4129

A.13.3.1.3.2Test Requirements4130

A.13.3.2Random Access for Satellite Access4130

A.13.3.2.1Contention Based Random Access Test for UE category NB1 UEs in Satellite Access - Standalone mode in normal coverage4131

A.13.3.2.1.1Test Purpose and Environment4131

A.13.3.2.1.2Test Requirements4133

A.13.3.2.2Contention Based Random Access Test for UE category NB1 UEs in Satellite Access - Standalone mode in Enhanced Coverage4135

A.13.3.2.2.1Test Purpose and Environment4135

A.13.3.2.2.2Test Requirements4137

A.13.3.2.3Contention Based Random Access on Non-anchor Carrier Test for UE category NB1 UEs Standalone mode in Enhanced Coverage4139

A.13.3.2.3.1Test Purpose and Environment4139

A.13.3.2.3.2Test Requirements4140

A.13.3.2.4Contention Based Random Access Test for UE category NB1 UEs in Satellite Access - Standalone mode in normal coverage for CB-Msg3-EDT procedure4142

A.13.3.2.4.1Test Purpose and Environment4142

A.13.3.2.4.2Test Requirements4144

A.13.4Timing and signalling characteristics for satellite access4145

A.13.4.1UE transmit timing for satellite access4145

A.13.4.1.1E-UTRAN HD-FDD and TDD – UE Transmit Timing Accuracy Tests for Category NB1 UE Standalone mode under normal coverage for Satellite Access4145

A.13.4.1.1.1Test Purpose and Environment4145

A.13.4.1.1.2Test Requirements4146

A.13.4.1.2E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Category NB1 UE Standalone mode under enhanced coverage for Satellite Access4147

A.13.4.1.2.1Test Purpose and Environment4147

A.13.4.1.2.2Test Requirements4149

A.13.4.1.3E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Category NB1 UE Standalone mode under enhanced coverage with segment transmission in NGSO for Satellite Access4149

A.13.4.1.3.1Test Purpose and Environment4149

A.13.4.1.3.2Test Requirements4151

A.13.4.2UE timing advance for satellite access4151

A.13.4.2.1HD-FDD and TDD UE Timing Advance Adjustment Accuracy Test for UE Category NB1 in Standalone Mode under Normal Coverage for Satellite Access4151

A.13.4.2.1.1Test Purpose and Environment4151

A.13.4.2.1.2Test Requirements4153

A.13.4.2.2HD-FDD UE Timing Advance Adjustment Accuracy Test for UE Category NB1 in Standalone Mode under Enhance Coverage for Satellite Access4153

A.13.4.2.2.1Test Purpose and Environment4153

A.13.4.2.2.2Test Requirements4155

A.13.4.3Radio Link Monitoring for satellite access4155

A.13.4.3.1HD-FDD and TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in normal coverage4155

A.13.4.3.1.1Test Purpose and Environment4155

A.13.4.3.1.2Test Requirements4158

A.13.4.3.2HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in enhanced coverage4158

A.13.4.3.2.1Test Purpose and Environment4158

A.13.4.3.2.2Test Requirements4161

A.13.4.3.3HD-FDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 Standalone mode in Enhanced Coverage4161

A.13.4.3.3.1Test Purpose and Environment4161

A.13.4.3.3.2Test Requirements4164

A.13.4.3.4HD-FDD and TDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 Standalone mode in Normal Coverage4164

A.13.4.3.4.1Test Purpose and Environment4164

A.13.4.3.4.2Test Requirements4167

A.13.4.3.5HD-FDD and TDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 Standalone mode in Normal Coverage4167

A.13.4.3.5.1Test Purpose and Environment4167

A.13.4.3.5.2Test Requirements4170

A.13.4.3.6HD-FDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 Standalone mode in Enhanced Coverage4170

A.13.4.3.6.1Test Purpose and Environment4170

A.13.4.3.6.2Test Requirements4173

A.13.4.3.7HD-FDD and TDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 Standalone mode in Normal Coverage4173

A.13.4.3.7.1Test Purpose and Environment4173

A.13.4.3.7.2Test Requirements4175

A.13.4.3.8HD-FDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 Standalone mode in Enhanced Coverage4176

A.13.4.3.8.1Test Purpose and Environment4176

A.13.4.3.8.2Test Requirements4178

A.13.4.3.9HD-FDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 in-band mode in NTN NR in Enhanced Coverage4179

A.13.4.3.9.1Test Purpose and Environment4179

A.13.4.3.9.2Test Requirements4182

A.13.5UE measurement procedures in RRC_CONNECTED state for UE category NB1 for satellite access4182

A.13.5.1HD-FDD and TDD Intra-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access4182

A.13.5.1.1Test Purpose and Environment4182

A.13.5.2HD-FDD and TDD Inter-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access4185

A.13.5.2.1Test Purpose and Environment4185

A.13.5.3HD-FDD and TDD Intra-frequency location-based neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access4187

A.13.5.3.1Test Purpose and Environment4187

A.13.5.3.2Test Requirements4188

A.13.5.4HD-FDD Intra-frequency neighbour cell measurement for UE category NB1 in in-band mode in NTN NR under normal coverage for Satellite Access4189

A.13.5.4.1Test Purpose and Environment4189

A.13.5.4.2Test Requirements4191

A.13.5.5HD-FDD Inter-frequency neighbour cell measurement for UE category NB1 in in-band mode in NTN NR under normal coverage for Satellite Access4191

A.13.5.5.1Test Purpose and Environment4191

A.13.5.5.2Test Requirements4194

A.13.6Measurement performance requirements for UE for satellite access4195

A.13.6.1Void4195

A.13.6.2Channel quality reporting accuracy for satellite access4195

A.13.6.2.1E-UTRAN HD-FDD and TDD Downlink channel quality reporting accuracy for UE Category NB1 Standalone mode under normal coverage4195

A.13.6.2.1.1Test Purpose and Environment4195

A.13.6.2.1.2Test parameters4195

A.13.6.2.1.3Test Requirements4196

A.13.6.2.2E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category NB1 Standalone mode under enhanced coverage4196

A.13.6.2.2.1Test Purpose and Environment4196

A.13.6.2.2.2Test parameters4196

A.13.6.2.2.3Test Requirements4197

A.13.6.2.3E-UTRAN HD-FDD and TDD Downlink channel quality reporting accuracy on non-anchor carrier for UE Category NB1 Standalone mode under normal coverage4197

A.13.6.2.3.1Test Purpose and Environment4197

A.13.6.2.3.2Test parameters4198

A.13.6.2.3.3Test Requirements4199

A.13.6.2.4E-UTRAN HD-FDD Downlink channel quality reporting accuracy on non-anchor carrier for UE Category NB1 Standalone mode under enhanced coverage4199

A.13.6.2.4.1Test Purpose and Environment4199

A.13.6.2.4.2Test parameters4199

A.13.6.2.4.3Test Requirements4200

A.13.6.2.5E-UTRAN HD-FDD and TDD Downlink channel quality reporting accuracy in RRC_CONNECTED for UE Category NB1 Standalone mode under normal coverage4200

A.13.6.2.5.2Test parameters4200

A.13.6.2.5.3Test Requirements4202

A.13.6.2.6E-UTRAN HD-FDD Downlink channel quality reporting accuracy in RRC_CONNECTED for UE Category NB1 Standalone mode under enhanced coverage4202

A.13.6.2.6.1Test Purpose and Environment4202

A.13.6.2.6.2Test parameters4202

A.13.6.2.6.3Test Requirements4203

A.14E-UTRAN Standalone Tests for UE Category M1 for Satellite Access4203

A.14.1RRC_IDLE state for satellite access4203

A.14.1.1Cell re-selection for satellite access4203

A.14.1.1.1E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage4203

A.14.1.1.1.1Test Purpose and Environment4203

A.14.1.1.1.2Test Requirements4205

A.14.1.1.2E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in normal coverage4206

A.14.1.1.2.1Test Purpose and Environment4206

A.14.1.1.2.2Test Requirements4208

A.14.1.1.3E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage with serving cell RRM measurement relaxation4209

A.14.1.1.3.1Test Purpose and Environment4209

A.14.1.1.3.2Test Requirements4211

A.14.1.1.4E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in normal coverage with serving cell RRM measurement relaxation4212

A.14.1.1.4.1Test Purpose and Environment4212

A.14.1.1.4.2Test Requirements4214

A.14.1.1.5E-UTRAN FDD – FDD Inter frequency case for Cat-M1 UE in normal coverage4215

A.14.1.1.5.1Test Purpose and Environment4215

A.14.1.1.5.2Test Requirements4217

A.14.1.1.6E-UTRAN HD – FDD Inter frequency case for Cat-M1 UE in normal coverage4218

A.14.1.1.6.1Test Purpose and Environment4218

A.14.1.1.6.2Test Requirements4220

A.14.1.1.7E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage, time-based triggering4221

A.14.1.1.7.1Test Purpose and Environment4221

A.14.1.1.7.2Test Requirements4222

A.14.1.1.8 E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in enhanced coverage, time-based triggering4223

A.14.1.1.8.1Test Purpose and Environment4223

A.14.1.1.8.2Test Requirements4224

A.14.1.1.9E-UTRAN FDD – FDD Inter frequency case for Cat-M1 UE in enhanced coverage, location-based triggering4225

A.14.1.1.9.1Test Purpose and Environment4225

A.14.1.1.9.2Test Requirements4226

A.14.1.1.10E-UTRAN HD – FDD Inter frequency case for Cat-M1 UE in normal coverage, location-based triggering4227

A.14.1.1.10.1Test Purpose and Environment4227

A.14.1.1.10.2Test Requirements4228

A.14.2RRC_CONNECTED state mobility for satellite access4229

A.14.2.1E-UTRAN handover for satellite access4229

A.14.2.1.1E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition4229

A.14.2.1.1.1Test Purpose and Environment4229

A.14.2.1.1.2Test Requirements4231

A.14.2.1.2E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition4232

A.14.2.1.2.1Test Purpose and Environment4232

A.14.2.1.2.2Test Requirements4233

A.14.2.1.3E-UTRAN FDD-FDD Intra frequency conditional handover for Cat-M1 UEs in CEModeA4234

A.14.2.1.3.1Test Purpose and Environment4234

A.14.2.1.3.2Test Requirements4235

A.14.2.1.4E-UTRAN HD-FDD Intra frequency conditional handover for Cat-M1 UEs in CEModeA4236

A.14.2.1.4.1Test Purpose and Environment4236

A.14.2.1.4.2Test Requirements4237

A.14.2.1.5E-UTRAN FDD Intra frequency handover for Cat-M1 UEs in CEModeA4238

A.14.2.1.5.1Test Purpose and Environment4238

A.14.2.1.5.2Test Requirements4239

14.2.1.6E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA4240

A.14.2.1.6.1Test Purpose and Environment4240

A.14.2.1.6.2Test Requirements4241

A.14.2.1.7E-UTRAN FD-FDD Inter frequency handover for Cat-M1 UEs in CEModeA4242

A.14.2.1.7.1Test Purpose and Environment4242

A.14.2.1.7.2Test Requirements4243

A.14.2.1.8E-UTRAN HD-FDD Inter frequency handover for Cat-M1 UEs in CEModeA4244

A.14.2.1.8.1Test Purpose and Environment4244

A.14.2.1.8.2Test Requirements4245

A.14.2.1.9E-UTRAN FDD Inter frequency handover for Cat-M1 UEs in CEModeB4246

A.14.2.1.9.1Test Purpose and Environment4246

A.14.2.1.9.2Test Requirements4247

A.14.2.1.10E-UTRAN HD-FDD Inter frequency handover for Cat-M1 UEs in CEModeB4248

A.14.2.1.10.1Test Purpose and Environment4248

A.14.2.1.10.2Test Requirements4249

A.14.2.1.11E-UTRAN FDD-FDD Inter frequency conditional handover for Cat-M1 UEs in CEModeA4250

A.14.2.1.11.1Test Purpose and Environment4250

A.14.2.1.12.2Test Requirements4251

A.14.2.1.12E-UTRAN HD-FDD Inter frequency conditional handover for Cat-M1 UEs in CEModeA4252

A.14.2.1.12.1Test Purpose and Environment4252

A.14.2.1.12.2Test Requirements4253

A.14.2.1.15E-UTRAN FDD-FDD Inter frequency location based conditional handover for Cat-M1 UEs in CEModeA4258

A.14.2.1.15.1Test Purpose and Environment4258

A.14.2.1.16.2Test Requirements4259

A.14.2.1.16E-UTRAN HD-FDD Inter frequency time based conditional handover for Cat-M1 UEs in CEModeA4260

A.14.2.1.16.1Test Purpose and Environment4260

A.14.2.1.16.2Test Requirements4261

A.14.3RRC connection mobility control for satellite access4262

A.14.3.1RRC re-establishment for satellite access4262

A.14.3.1.1E-UTRAN FD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA for Satellite access4262

A.14.3.1.1.1Test Purpose and Environment4262

A.14.3.1.1.2Test Requirements4263

A.14.3.1.2E-UTRAN HD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA4264

A.14.3.1.2.1Test Purpose and Environment4264

A.14.3.1.2.2Test Requirements4266

A.14.3.1.3E-UTRAN FD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA for Satellite access4267

A.14.3.1.3.1Test Purpose and Environment4267

A.14.3.1.3.2Test Requirements4269

A.14.3.1.4E-UTRAN HD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA for Satellite access4270

A.14.3.1.4.1Test Purpose and Environment4270

A.14.3.1.4.2 Test Requirements4272

A.14.3.2Random access for satellite access4273

A.14.3.2.1E-UTRAN FDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage for satellite access4273

A.14.3.2.1.1Test Purpose and Environment4273

A.14.3.2.1.2Test Requirements4275

A.14.3.2.2E-UTRAN HD-FDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage for satellite access4276

A.14.3.2.2.1Test Purpose and Environment4276

A.14.3.2.2.2Test Requirements4278

A.14.3.2.3E-UTRAN FDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage for satellite access4280

A.14.3.2.3.1Test Purpose and Environment4280

A.14.3.2.3.2Test Requirements4282

A.14.3.2.4E-UTRAN HD-FDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage for satellite access4283

A.14.3.2.4.1Test Purpose and Environment4283

A.14.3.2.4.2Test Requirements4285

A.14.4Timing and signalling characteristics for satellite access4287

A.14.4.1UE transmit timing for satellite access4287

A.14.4.1.1E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA4287

A.14.4.1.1.1Test Purpose and Environment4287

A.14.4.1.1.2Test Requirements4289

A.14.4.1.2E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA4290

A.14.4.1.2.1Test Purpose and Environment4290

A.14.4.1.2.2Test Requirements4292

A.14.4.1.3E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB4293

A.14.4.1.3.1Test Purpose and Environment4293

A.14.4.1.3.2Test Requirements4294

A.14.4.1.4E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB4295

A.14.4.1.4.1Test Purpose and Environment4295

A.14.4.1.4.2Test Requirements4296

A.14.4.1.5E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB with segment transmission in NGSO for Satellite Access4297

A.14.4.1.5.1Test Purpose and Environment4297

A.14.4.1.5.2Test Requirements4298

A.14.4.2UE timing advance for satellite access4299

A.14.4.2.1E-UTRAN FDD Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA4299

A.14.4.2.1.1Test Purpose and Environment4299

A.14.4.2.1.2Test Requirements4302

A.14.4.2.2E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA4302

A.14.4.2.2.1Test Purpose and Environment4302

A.14.4.2.2.2Test Requirements4304

A.14.4.2.3E-UTRAN FDD UE Timing Advance Adjustment Accuracy Test in CEModeB4304

A.14.4.2.3.1Test Purpose and Environment4304

A.14.4.2.3.2Test Requirements4306

A.14.4.2.4E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test in CEModeB4306

A.14.4.2.4.1Test Purpose and Environment4306

A.14.4.2.4.2Test Requirements4307

A.14.4.3Radio Link Monitoring for satellite access4308

A.14.4.3.1E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for Satellite access4308

A.14.4.3.1.1Test Purpose and Environment4308

A.14.4.3.1.2Test Requirements4311

A.14.4.3.2E-UTRAN FD-FDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A for Satellite access4311

A.14.4.3.2.1Test Purpose and Environment4311

A.14.4.3.2.2Test Requirements4314

A.14.4.3.3E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for Satellite access4314

A.14.4.3.3.1Test Purpose and Environment4314

A.14.4.3.3.2Test Requirements4317

A.14.4.3.4E-UTRAN HD-FDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A for Satellite access4317

A.14.4.3.4.1Test Purpose and Environment4317

A.14.4.3.4.2Test Requirements4320

A.14.4.3.5E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A4320

A.14.4.3.5.1Test Purpose and Environment4320

A.14.4.3.5.2 Test Requirements4323

A.14.4.3.6E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A4323

A.14.4.3.6.1Test Purpose and Environment4323

A.14.4.3.6.2Test Requirements4326

A.14.4.3.7E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A4326

A.14.4.3.7.1Test Purpose and Environment4326

A.14.4.3.8E-UTRAN HD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A4329

A.14.4.3.8.1 Test Purpose and Environment4329

A.14.4.3.8.2Test Requirements4332

A.14.5UE measurement procedures in RRC_CONNECTED state for satellite access4332

A.14.5.1 Intra-frequency measurements for satellite access4332

A.14.5.1.1E-UTRAN FDD-FDD intra-frequency event triggered reporting under AWGN conditions in asynchronous cells for Cat-M1 UE in CEModeA4332

A.14.5.1.1.1Test Purpose and Environment4332

A.14.5.1.1.2Test Requirements4334

A.14.5.1.2E-UTRAN FDD-FDD intra-frequency event triggered reporting under AWGN conditions in synchronous cells for Cat-M1 UE in CEModeA in DRX4335

A.14.5.1.2.1Test Purpose and Environment4335

A.14.5.1.2.2Test Requirements4337

A.14.5.1.3E-UTRAN HD-FDD intra-frequency event triggered reporting under AWGN conditions in asynchronous cells for Cat-M1 UE in CEModeA4337

A.14.5.1.3.1Test Purpose and Environment4337

A.14.5.1.3.2Test Requirements4339

A.14.5.1.4E-UTRAN HD-FDD intra-frequency event triggered reporting under AWGN conditions in synchronous cells for Cat-M1 UE in CEModeA in DRX4340

A.14.5.1.4.1Test Purpose and Environment4340

A.14.5.1.4.2Test Requirements4342

A.14.5.1.5E-UTRAN FD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA with location-based triggering4342

A.14.5.1.5.1Test Purpose and Environment4342

A.14.5.1.5.2Test Requirements4344

A.14.5.1.6 E-UTRAN HD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA with location-based triggering4345

A.14.5.1.6.1Test Purpose and Environment4345

A.14.5.1.6.2Test Requirements4346

A.14.5.1.7E-UTRAN HD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering4347

A.14.5.1.7.1Test Purpose and Environment4347

A.14.5.1.7.2Test Requirements4348

A.14.5.2 Inter-frequency measurements for satellite access4349

A.14.5.2.1E-UTRAN FD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering4349

A.14.5.2.1.1Test Purpose and Environment4349

A.14.5.2.1.2Test Requirements4350

A.14.5.2.2E-UTRAN HD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering4351

A.14.5.2.2.1Test Purpose and Environment4351

A.14.5.2.2.2Test Requirements4352

A.14.5.2.3E-UTRAN HD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeB when DRX is used with time-based triggering4353

A.14.5.2.3.1Test Purpose and Environment4353

A.14.5.2.3.2Test Requirements4354

A.14.5.2.4E-UTRAN FDD-FDD Inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeA4355

A.14.5.2.4.1Test Purpose and Environment4355

A.14.5.2.4.2Test Requirement4356

A.14.5.2.5E-UTRAN FDD-FDD Inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 in CEModeA when DRX is used4357

A.14.5.2.5.1Test Purpose and Environment4357

A.14.5.2.5.2Test Requirement4359

A.14.5.2.6E-UTRAN HD-FDD Inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeA4359

A.14.5.2.6.1Test Purpose and Environment4359

A.14.5.2.6.2Test Requirement4361

A.14.5.2.7E-UTRAN HD-FDD inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 in CEModeA in DRX4361

A.14.5.2.7.1Test Purpose and Environment4361

A.14.5.2.7.2Test Requirement4363

A.14.5.2.8E-UTRAN FDD-FDD inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeB4363

A.14.5.2.8.1Test Purpose and Environment4363

A.14.5.2.8.2Test Requirement4365

A.14.5.2.9E-UTRAN HD-FDD inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeB4366

A.14.5.2.9.1Test Purpose and Environment4366

A.14.5.2.9.2Test Requirement4367

A.14.6Measurement performance requirements for UE for satellite access4368

A.14.6.1RSRP for satellite access4368

A.14.6.1.1FD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeA4368

A.14.6.1.1.1Test Purpose and Environment4368

A.14.6.1.1.2Test parameters4368

A.14.6.1.1.3Test Requirements4370

A.14.6.1.2HD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeA4370

A.14.6.1.2.1Test Purpose and Environment4370

A.14.6.1.2.2Test parameters4370

A.14.6.1.2.3Test Requirements4372

A.14.6.1.3FD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeA4372

A.14.6.1.3.1Test Purpose and Environment4372

A.14.6.1.3.2Test parameters4372

A.14.6.1.3.3Test Requirements4373

A.14.6.1.4HD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeA4374

A.14.6.1.4.1Test Purpose and Environment4374

A.14.6.1.4.2Test parameters4374

A.14.6.1.4.3Test Requirements4375

A.14.6.1.5FD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeB4375

A.14.6.1.5.1Test Purpose and Environment4375

A.14.6.1.5.2Test parameters4375

A.14.6.1.5.3Test Requirements4376

A.14.6.1.6HD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeB4376

A.14.6.1.6.1Test Purpose and Environment4376

A.14.6.1.6.2Test parameters4377

A.14.6.1.6.3Test Requirements4378

A.14.6.2Channel quality reporting accuracy for satellite access4378

A.14.6.2.1E-UTRAN FD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode A for Satellite access4378

A.14.6.2.1.1Test Purpose and Environment4378

A.14.6.2.1.2Test parameters4378

A.14.6.2.1.3Test Requirements4379

A.14.6.2.2E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode A for Satellite access4380

A.14.6.2.2.1Test Purpose and Environment4380

A.14.6.2.2.2Test parameters4380

A.14.6.2.2.3Test Requirements4381

A.14.6.2.3.2Test parameters4381

A.14.6.2.3.3Test Requirements4382

A.14.6.2.4E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode B for Satellite access4383

A.14.6.2.4.1Test Purpose and Environment4383

A.14.6.2.4.2Test parameters4383

A.14.6.2.4.3Test Requirements4384

Annex B (normative):Conditions for RRM requirements applicability for operating bands4385

B.1Conditions for E-UTRAN RRC_IDLE state mobility4385

B.1.1Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection4385

B.1.2Conditions for measurements of inter-frequency E-UTRAN cells for cell re-selection4385

B.1.3Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection for UE Category M14385

B.1.4Conditions for measurements of intra-frequency NB-IoT cells for cell re-selection for UE Category NB14387

B.1.5Conditions for measurements of inter-frequency NB-IoT cells for cell re-selection for UE Category NB14388

B.1.6Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection for UE Category 1bis4388

B.1.7Conditions for measurements of E-UTRAN cells for cell re-selection for UE Category M24388

B.1.7.1Conditions for measurements of intra-frequence E-UTRAN cells for cell selection4388

B.1.7.2Condition for measurements of inter-frequence E-UTRAN cells for cell selection4390

B.1.8Conditions for measurements of inter-frequency E-UTRAN cells for cell re-selection for UE Category M14391

B.1.9Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection for UE Category M1 for satellite access4391

B.1.10Conditions for measurements of intra-frequency NB-IoT cells for cell re-selection for UE Category NB1 and NB2 for satellite access4392

B.1.11Conditions for measurements of inter-frequency NB-IoT cells for cell re-selection for UE Category NB1 for satellite access4393

B.1.12Conditions for measurements of inter-frequency E-UTRAN cells for cell re-selection for UE Category M1 for satellite access4393

B.2Conditions for UE Measurements Procedures in RRC_CONNECTED State4394

B.2.1Conditions for E-UTRAN intra-frequency measurements4394

B.2.2Conditions for E-UTRAN intra-frequency measurements with autonomous gaps4394

B.2.3Conditions for E-UTRAN inter-frequency measurements4394

B.2.4Conditions for E-UTRAN inter-frequency measurements with autonomous gaps4395

B.2.5Conditions for E-UTRAN OTDOA intra-frequency RSTD Measurements4395

B.2.6Conditions for E-UTRAN OTDOA inter-frequency RSTD Measurements4396

B.2.7Conditions for Measurements of the secondary component carrier with deactivated SCell4396

B.2.8Conditions for E-UTRAN Intra-Frequency Measurements under Time Domain Measurement Resource Restriction4396

B.2.9Conditions for E-UTRAN Intra-Frequency Measurements under Time Domain Measurement Resource Restriction with CRS Assistance Information4397

B.2.10Conditions for E-UTRAN intra-frequency discovery signal measurements4397

B.2.10.1Conditions for E-UTRAN intra-frequency CRS-based measurements4397

B.2.10.2Conditions for E-UTRAN intra-frequency CSI-RS based measurements4398

B.2.11Conditions for E-UTRAN inter-frequency discovery signal measurements4398

B.2.11.1Conditions for E-UTRAN inter-frequency CRS-based measurements4398

B.2.11.2Conditions for E-UTRAN inter-frequency CSI-RS based measurements4399

B.2.12Conditions for E-UTRAN intra-frequency discovery signal measurements under operation with frame structure 34399

B.2.13Conditions for E-UTRAN inter-frequency discovery signal measurements under operation with frame structure 34399

B.2.13.1Conditions for E-UTRAN inter-frequency CRS-based measurements4399

B.2.13.2Conditions for E-UTRAN inter-frequency CSI-RS based measurements4400

B.2.14Conditions for E-UTRAN intra-frequency measurements by UE Category M14400

B.2.15Conditions for NB-IoT intra-frequency measurements by UE Category NB14401

B.2.16Conditions for NB-IoT intra-frequency RSTD measurements by UE Category NB14402

B.2.17Conditions for NB-IoT inter-frequency RSTD measurements by UE Category NB14403

B.2.18Conditions for E-UTRAN inter-frequency measurements by UE Category M14404

B.2.19Conditions for E-UTRAN measurements by UE Category M24405

B.2.19.1Conditions for E-UTRAN intra-frequency measurements4405

B.2.19.2Conditions for E-UTRAN inter-frequency measurements4405

B.2.20Conditions for E-UTRAN inter-frequency RSTD measurements by UE Category M14405

B.2.21Conditions for E-UTRAN inter-frequency RSTD measurements by UE Category M24406

B.2.22Conditions for E-UTRAN intra-frequency RSTD measurements by UE Category M14406

B.2.23Conditions for E-UTRAN intra-frequency RSTD measurements by UE Category M24408

B.2.24Conditions for intra-frequency neighbour cell measurements of NB-IoT cells for UE Category NB14408

B.2.25Conditions for inter-frequency neighbour cell measurements of NB-IoT cells for UE Category NB14408

B.2.26Conditions for E-UTRAN intra-frequency measurements by UE Category M1 for satellite access4408

B.2.27Conditions for NB-IoT intra-frequency measurements by UE Category NB1 and NB2 for satellite access4409

B.2.28Conditions for E-UTRAN inter-frequency measurements by UE Category M1 for satellite access4410

B.2.29Conditions for intra-frequency neighbour cell measurements of NB-IoT cells for UE Category NB1 for satellite access4410

B.2.30Conditions for inter-frequency neighbour cell measurements of NB-IoT cells for UE Category NB1 for satellite access4411

B.3Conditions for measurements performance requirements for UE4411

B.3.1Conditions for intra-frequency RSRP and RSRQ Accuracy Requirements4411

B.3.2Void4411

B.3.3Conditions for inter-frequency RSRP and RSRQ Accuracy Requirements4412

B.3.4Conditions for inter-frequency relative RSRP and RSRQ Accuracy Requirements4412

B.3.5Conditions for UE Rx – Tx time difference4412

B.3.6Conditions for intra-frequency Reference Signal Time Difference (RSTD) measurements4412

B.3.7Conditions for inter-frequency RSTD measurements4412

B.3.8Conditions for Intra-Frequency Relative RSRP Accuracy Requirements4412

B.3.9Conditions for Intra-Frequency Absolute RSRP and RSRQ Accuracy Requirements under Time Domain Measurement Resource Restriction4413

B.3.10Conditions for Intra-Frequency Relative RSRP Accuracy Requirements under Time Domain Measurement Resource Restriction4413

B.3.11Conditions for Intra-Frequency Absolute RSRP and RSRQ Accuracy Requirements under Time Domain Measurement Resource Restriction with CRS Assistance Information4413

B.3.12Conditions for Intra-Frequency Relative RSRP Accuracy Requirements under Time Domain Measurement Resource Restriction with CRS Assistance Information4413

B.3.13Conditions for UE Rx–Tx Time Difference Measurement under Time Domain Measurement Resource Restriction with CRS Assistance Information4413

B.3.14Conditions for Intra-Frequency Absolute Discovery Signal Measurement Accuracy Requirements4413

B.3.14.1Conditions for Intra-frequency CRS-based measurements4413

B.3.14.2Conditions for Intra-frequency CSI-RS-based measurements4414

B.3.15Conditions for Intra-Frequency Relative Discovery Signal Measurement Accuracy Requirements4414

B.3.15.1Conditions for Intra-frequency CRS-based measurements4414

B.3.15.2Conditions for Intra-frequency CSI-RS-based measurements4414

B.3.16Conditions for Inter-Frequency Absolute Discovery Signal Measurement Accuracy Requirements4415

B.3.16.1Conditions for Inter-frequency CRS-based measurements4415

B.3.16.2Conditions for Inter-frequency CSI-RS-based measurements4415

B.3.17Conditions for Inter-Frequency Relative Discovery Signal Measurement Accuracy Requirements4415

B.3.17.1Conditions for Inter-frequency CRS-based measurements4415

B.3.17.2Conditions for Inter-frequency CSI-RS-based measurements4415

B.3.18Conditions for Intra-frequency Absolute RS-SINR Accuracy Requirements4416

B.3.19Conditions for Inter-frequency Absolute RS-SINR Accuracy Requirements4416

B.3.20Conditions for Inter-frequency Relative RS-SINR Accuracy Requirements4416

B.3.21Conditions for Intra-Frequency Absolute Accuracy Requirements for Measurements under Operation with Frame Structure 34416

B.3.21.1Conditions for RSRP measurements4416

B.3.21.2Conditions for RSRQ measurements4416

B.3.21.3Conditions for CSI-RSRP measurements4416

B.3.22Conditions for Intra-Frequency Relative Accuracy Requirements for Measurements under Operation with Frame Structure 34417

B.3.22.1Conditions for RSRP measurements4417

B.3.22.2Void4417

B.3.22.3Conditions for CSI-RSRP measurements4417

B.3.23Conditions for Inter-Frequency Absolute Accuracy Requirements for Measurements under Operation with Frame Structure 34417

B.3.23.1Conditions for RSRP measurements4417

B.3.23.2Conditions for RSRQ measurements4418

B.3.23.3Conditions for CSI-RSRP measurements4418

B.3.24Conditions for Inter-Frequency Relative Accuracy Requirements for Measurements under Operation with Frame Structure 34418

B.3.24.1Conditions for RSRP measurements4418

B.3.24.2Conditions for RSRQ measurements4418

B.3.24.3Conditions for CSI-RSRP measurements4418

B.3.25Conditions for NB-IoT intra-frequency Absolute NRSRP and NRSRQ Accuracy Requirements for UE Category NB14418

B.3.25AConditions for NB-IoT intra-frequency Absolute NRSRP and NRSRQ Accuracy Requirements for UE Category NB1 for satellite access4419

B.3.26Conditions for NB-IoT inter-frequency Absolute NRSRP and NRSRQ Accuracy Requirements for UE Category NB14419

B.3.27Conditions for intra-frequency RSRP and RSRQ Accuracy Requirements for Category 04419

B.3.28Conditions for Intra-Frequency Relative RSRP Accuracy Requirements for Category 04419

B.3.29Conditions for intra-frequency Reference Signal Time Difference (RSTD) measurements for NB14420

B.3.30Conditions for inter-frequency Reference Signal Time Difference (RSTD) measurements for NB14420

B.3.31Conditions for inter-frequency Reference Signal Time Difference (RSTD) measurements for Cat M14420

B.3.32Conditions for inter-frequency Reference Signal Time Difference (RSTD) measurements for Cat M24420

B.3.33Conditions for intra-frequency Reference Signal Time Difference (RSTD) measurements for Cat M14420

B.3.34Conditions for intra-frequency Reference Signal Time Difference (RSTD) measurements for Cat M24420

B.4RRM Requirements Exceptions4421

B.4.1General4421

B.4.2Receiver sensitivity relaxation for UE supporting CA4421

B.4.3Receiver sensitivity relaxation for UE configured with CA4421

B.4.3.1Inter-band carrier aggregation4421

B.4.3.2Intra-band non-contiguous carrier aggregation4421

B.4.3.3Inter-band carrier aggregation with operating bands without uplink band4421

B.5Conditions for Measurement Performance Requirements for ProSe UE4422

B.5.1Conditions for S-RSRP Accuracy Requirements4422

B.5.2Conditions for Relative S-RSRP Accuracy Requirements4422

B.5.3Conditions for Selection/Reselection to Intra-frequency SyncRef UE4422

B.5.4Conditions for SD-RSRP Accuracy Requirements4423

B.5.5Conditions for Relative SD-RSRP Accuracy Requirements4423

B.6Conditions for V2X4424

B.6.1Test parameters for GNSS signals4424

B.6.2Conditions for Absolute S-RSRP Accuracy Requirements4424

B.6.3Conditions for Relative S-RSRP Accuracy Requirements4424

B.6.4Conditions for Selection/Reselection to Intra-frequency SyncRef UE4424

B.6.5Conditions for Absolute PSSCH-RSRP Accuracy Requirements4425

B.7Conditions for sTTI and 1ms-TTI with 3 Subframe HARQ Processing4425

B.7.1Conditions for Maximum Timing Difference Between Uplink and Downlink Carriers in Carrier Aggregation4425

B.8High level test procedure for SAN RRM tests4427

Annex C (informative):Change history:4427
