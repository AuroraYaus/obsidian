| 3GPP TS 36.133 V19.5.0 (2026-06) |  |
| --- | --- |
| Technical Specification\|Report |  |
| 3rd Generation Partnership Project;Technical Specification Group Radio Access Network;Evolved Universal Terrestrial Radio Access (E-UTRA);Requirements for support of radio resource management(Release 19) |  |
|  |  |
| ![](media/image1.emf) |  |
|  |  |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. |  |

|  |
| --- |
| 3GPPPostal address3GPP support office address650 Route des Lucioles - Sophia AntipolisValbonne - FRANCETel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16Internethttp://www.3gpp.org |
| Copyright NotificationNo part may be reproduced except as authorized by written permission. The copyright and the foregoing restriction extend to reproduction in all media.© 2026, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).All rights reserved.UMTS™ is a Trade Mark of ETSI registered for the benefit of its members3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersGSM® and the GSM logo are registered and owned by the GSM Association |

Contents

Foreword 107

1 Scope 109

2 References 109

3 Definitions, symbols and abbreviations 111

3.1 Definitions 111

3.2 Symbols 113

3.3 Abbreviations 114

3.4 Test tolerances 117

3.5 Additional notation 117

3.5.1 Groups of bands 117

3.5.1A Groups of bands for satellite access 120

3.6 General 121

3.6.1 Applicability of requirements in this specification version 121

3.6.1.1 Applicability of requirements for UE capable of network-based CRS interference mitigation 127

3.6.1.2 Applicability of requirements with CRS muting for category M1 UE capable of CRS muting 129

3.6.1.3 Applicability of requirements with CRS muting for category M2 UE capable of CRS muting 130

3.6.2 Applicability of requirements for EN-DC operation 131

3.6.3 Applicability of requirements for NE-DC operation 132

3.6.4 Applicability of requirements for NGEN-DC operation 133

3.6.5 Applicability of 2-step RA and 4-step RA in RRM requirements 133

3.6.6 Applicability of requirements for UE category NB-IoT for frame structure type 1 for NTN-TDD 133

3.6.7 Applicability of NB-IoT inband operation in NTN NR 133

Rel-18 UEs supporting only standalone operation do not need to be tested for in-band operation with NR over NTN. In-band operation with NR NTN is not supported in Rel-17. 133

4 E-UTRAN RRC_IDLE state mobility 133

4.1 Cell Selection 133

4.2 Cell Re-selection 134

4.2.1 Introduction 134

4.2.2 Requirements 134

4.2.2.1 Measurement and evaluation of serving cell 135

4.2.2.2 Void 136

4.2.2.3 Measurements of intra-frequency E-UTRAN cells 136

4.2.2.4 Measurements of inter-frequency E-UTRAN cells 138

4.2.2.5 Measurements of inter-RAT cells 140

4.2.2.5.1 Measurements of UTRAN FDD cells 140

4.2.2.5.2 Measurements of UTRAN TDD cells 142

4.2.2.5.3 Measurements of GSM cells 144

4.2.2.5.4 Measurements of HRPD cells 145

4.2.2.5.5 Measurements of cdma2000 1X 146

4.2.2.5.6 Measurements of NR cells 147

4.2.2.5.7 Measurements of NR cells subject to CCA 150

4.2.2.5.8 Measurements of NR cells for RedCap 152

4.2.2.6 Evaluation of cell re-selection criteria 154

4.2.2.7 Maximum interruption in paging reception 154

4.2.2.8 void 155

4.2.2.9 UE measurement capability 155

4.2.2.9a UE measurement capability (Increased UE carrier monitoring) 156

4.2.2.10 Reselection to CSG cells 156

4.2.2.10.1 Reselection from a non CSG to an inter-frequency CSG cell 156

4.2.2.10.2 Reselection from a non CSG to an inter-RAT UTRAN FDD CSG cell 157

4.2.2.11 Void 158

4.2.2.12 Void 158

4.2.2.13 Void 158

4.2.2.14 UE measurement capability for RedCap 158

4.3 Minimization of Drive Tests (MDT) 159

4.3.1 Introduction 159

4.3.2 Measurements 159

4.3.2.1 Requirements 159

4.3.3 Relative Time Stamp Accuracy 159

4.3.3.1 Requirements 159

4.3.4 Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting 160

4.3.4.1  Requirements 160

4.3.5 Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting 160

4.3.5.1 Requirements for timeSinceFailure 160

4.4 MBSFN Measurements 160

4.4.1 Introduction 160

4.4.2 MBSFN RSRP measurements 160

4.4.3 MBSFN RSRQ measurements 161

4.4.4 MCH BLER measurements 161

4.5 Proximity-based Services 161

4.5.1 Introduction 161

4.5.2 Requirements 161

4.5.2.1 Interruptions with ProSe Direct Discovery 161

4.5.2.2 Interruptions with ProSe Direct Communication 161

4.5.2.3 Initiation/Cease of SLSS transmissions with ProSe Direct Discovery 162

4.5.2.4 Initiation/Cease of SLSS transmissions with ProSe Direct Communication 162

4.6 Cell Selection and Re-selection Requirements for UE category NB1 163

4.6.1 Cell Selection 163

4.6.2 Cell Re-selection 163

4.6.2.1 Measurement and evaluation of serving NB-IoT cell for UE category NB1 in normal coverage 163

4.6.2.1A Measurement and evaluation of serving NB-IoT cell for HD-FDD UE category NB1 in normal coverage when configured with WUS 164

4.6.2.2 Measurements of intra-frequency NB-IoT cells for UE category NB1 in normal coverage 165

4.6.2.3 Measurement and evaluation of serving NB-IoT cell for UE category NB1 in enhanced coverage 166

4.6.2.3A Measurement and evaluation of serving NB-IoT cell for HD-FDD UE category NB1 in enhanced coverage when configured with WUS 168

4.6.2.4 Measurements of intra-frequency NB-IoT cells for UE category NB1 in enhanced coverage 169

4.6.2.5 Measurements of inter-frequency NB cells for UE category NB1 in normal coverage 170

4.6.2.6 Measurements of inter-frequency NB-IoT cells for UE category NB1 in enhanced coverage 171

4.6.2.7 Maximum interruption in paging reception in normal coverage 173

4.6.2.7A Maximum interruption in paging reception in enhanced coverage 173

4.6.2.8 UE measurement capability 173

4.6.2.9 WUS receptions for NB1 173

4.6.3 Requirements for transmission using preconfigured uplink resources for UE category NB1 174

4.6.3.1 Introduction 174

4.6.3.2 Requirements on UE synchronization for transmission using PUR 174

4.6.3.3 Requirements on TA validation for transmission using PUR 174

4.6A Cell Selection and Re-selection Requirements for UE category NB-IoT for Satellite Access 175

4.6A.1 Cell Selection 175

4.6A.2 Cell Re-selection for UE category NB-IoT for Satellite Access 175

4.6A.2.1 Measurement and evaluation of serving NB-IoT cell for UE category NB1 in normal coverage 176

4.6A.2.1A Measurement and evaluation of serving NB-IoT cell for HD-FDD UE category NB1 in normal coverage when configured with WUS 177

4.6A.2.2 Measurements of intra-frequency NB-IoT cells for UE category NB1 in normal coverage 178

4.6A.2.3 Measurement and evaluation of serving NB-IoT cell for UE category NB1 in enhanced coverage 180

4.6A.2.3A Measurement and evaluation of serving NB-IoT cell for HD-FDD UE category NB1 in enhanced coverage when configured with WUS 182

4.6A.2.4 Measurements of intra-frequency NB-IoT cells for UE category NB1 in enhanced coverage 183

4.6A.2.5 Measurements of inter-frequency NB cells for UE category NB1 in normal coverage 185

4.6A.2.6 Measurements of inter-frequency NB-IoT cells for UE category NB1 in enhanced coverage 187

4.6A.2.7 Maximum interruption in paging reception in normal coverage 189

4.6A.2.7A Maximum interruption in paging reception in enhanced coverage 189

4.6A.2.8 UE measurement capability 190

4.6A.2.9 WUS receptions for NB1 190

4.6A.3 Requirements for transmission using preconfigured uplink resources for UE category NB-IoT for Satellite Access 191

4.6A.3.1 Introduction 191

4.6A.3.2 Requirements on UE synchronization for transmission using PUR 191

4.6A.3.3 Requirements on TA validation for transmission using PUR 191

4.6B Cell Selection and Re-selection Requirements for UE category NB-IoT for frame structure type 1 for NTN-TDD 191

4.6B.1 Cell Selection 191

4.6B.2 Cell Re-selection for UE category NB-IoT for Satellite Access 191

4.6B.2.1 Measurement and evaluation of serving NB-IoT cell for UE category NB1 in normal coverage 192

4.6B.2.2 Measurements of intra-frequency NB-IoT cells for UE category NB1 in normal coverage 193

4.6B.2.5 Measurements of inter-frequency NB cells for UE category NB1 in normal coverage 194

4.6B.2.7 Maximum interruption in paging reception in normal coverage 195

4.6B.2.8 UE measurement capability 195

4.7 Cell Selection and Re-selection Requirements for UE category M1 196

4.7.1 Cell Selection 196

4.7.2 Cell Re-selection 196

4.7.2.1 Cell Re-selection requirements for UE category M1 in normal coverage 196

4.7.2.1.1 Measurement and evaluation of serving cell for UE category M1 in normal coverage 196

4.7.2.1.1A Relaxed measurement and evaluation of serving cell for UE category M1 in normal coverage 197

4.7.2.1.2 Measurements of intra-frequency cells for UE category M1 in normal coverage 198

4.7.2.1.3 Measurements of inter-frequency cells for UE category M1 in normal coverage 199

4.7.2.1.4 Maximum allowed layers for multiple monitoring for UE category M1 in normal coverage 201

4.7.2.1.5 Maximum interruption in paging reception for Category M1 UEs in normal coverage 201

4.7.2.2 Cell Re-selection requirements for UE category M1 in enhanced coverage 202

4.7.2.2.1 Measurement and evaluation of serving cell for UE category M1 in enhanced coverage 202

4.7.2.2.1A Relaxed measurement and evaluation of serving cell for UE category M1 in enhaned coverage 203

4.7.2.2.2 Measurements of intra-frequency cells for UE category M1 in enhanced coverage 204

4.7.2.2.3 Measurements of inter-frequency cells for UE category M1 in enhanced coverage 207

4.7.2.2.4 Maximum allowed layers for multiple monitoring for UE category M1 in enhanced coverage 208

4.7.2.2.5 Maximum interruption in paging reception for Category M1 UEs in enhanced coverage 209

4.7.2.3 WUS receptions for UE category M1 209

4.7.3 Channel quality report for UE Category M1 in idle mode 209

4.7.4 Requirements for transmission using preconfigured uplink resources for UE category M1 210

4.7.4.1 Introduction 210

4.7.4.2 Requirements on UE synchronization for transmission using PUR 210

4.7.4.3 Requirements on TA validation for transmission using PUR 210

4.7A Cell Selection and Re-selection Requirements for UE category M1 for Satellite Access 211

4.7A.1 Cell Selection 211

4.7A.2 Cell Re-selection for UE category M1 for Satellite Access 211

4.7A.2.1 Cell Re-selection requirements for UE category M1 in normal coverage 212

4.7A.2.1.1 Measurement and evaluation of serving cell for UE category M1 in normal coverage 212

4.7A.2.1.1A Relaxed measurement and evaluation of serving cell for UE category M1 in normal coverage 214

4.7A.2.1.2 Measurements of intra-frequency cells for UE category M1 in normal coverage 215

4.7A.2.1.3 Measurements of inter-frequency cells for UE category M1 in normal coverage 218

4.7A.2.1.4 Maximum allowed layers for multiple monitoring for UE category M1 in normal coverage 220

4.7A.2.1.5 Maximum interruption in paging reception for Category M1 UEs in normal coverage 220

4.7A.2.2 Cell Re-selection requirements for UE category M1 in enhanced coverage 221

4.7A.2.2.1 Measurement and evaluation of serving cell for UE category M1 in enhanced coverage 221

4.7A.2.2.1A Relaxed measurement and evaluation of serving cell for UE category M1 in enhaned coverage 222

4.7A.2.2.2 Measurements of intra-frequency cells for UE category M1 in enhanced coverage 224

4.7A.2.2.3 Measurements of inter-frequency cells for UE category M1 in enhanced coverage 226

4.7A.2.2.4 Maximum allowed layers for multiple monitoring for UE category M1 in enhanced coverage 229

4.7A.2.2.5 Maximum interruption in paging reception for Category M1 UEs in enhanced coverage 229

4.7A.2.3 WUS receptions for UE category M1 230

4.7A.3 Channel quality report for UE Category M1 in idle mode for Satellite Access 230

4.7A.4 Requirements for transmission using preconfigured uplink resources for UE category M1 for Satellite Access 231

4.7A.4.1 Introduction 231

4.7A.4.2 Requirements on UE synchronization for transmission using PUR 231

4.7A.4.3 Requirements on TA validation for transmission using PUR 231

4.8 Idle State Positioning Measurement Requirements for UE category NB1 231

4.8.1 OTDOA Intra-Frequency RSTD Measurements for UE category NB1 for normal coverage 231

4.8.1.1 RSTD Measurement Reporting Delay 233

4.8.2 OTDOA Intra-Frequency RSTD Measurements for UE category NB1 for enhanced coverage 233

4.8.2.1 RSTD Measurement Reporting Delay 234

4.8.3 OTDOA Inter-Frequency RSTD Measurements for UE category NB1 for normal coverage 235

4.8.3.1 RSTD Measurement Reporting Delay 236

4.8.4 OTDOA Inter-Frequency RSTD Measurements for UE category NB1 for enhanced coverage 237

4.8.4.1 RSTD Measurement Reporting Delay 238

4.8.5 Intra-Frequency E-CID NRSRP and NRSRQ Measurements for UE category NB2 for normal coverage 239

4.8.5.1 Measurement Reporting Delay 240

4.8.6 Intra-Frequency E-CID NRSRP and NRSRQ Measurements for UE category NB2 for enhanced coverage 240

4.8.6.1 Measurement Reporting Delay 241

4.8.7 Inter-Frequency E-CID NRSRP and NRSRQ Measurements for UE category NB2 for normal coverage 242

4.8.7.1 Measurement Reporting Delay 243

4.8.8 Inter-Frequency E-CID NRSRP and NRSRQ Measurements for UE category NB2 for enhanced coverage 243

4.8.8.1 Measurement Reporting Delay 244

4.9 Idle Mode CA Measurement 245

4.9.1 Introduction 245

4.9.2 Requirement 245

4.9.2.1 Detected cell requirement during state transition and Idle mode 245

4.9.2.2 Measurements of inter-frequency CA candidate cells 246

4.9.2.3 Measurements on serving cell 246

4A E-UTRAN RRC_INACTIVE state mobility 247

4A.1 Cell Re-selection 247

4A.1.1 Introduction 248

4A.1.2 Requirements 248

4A.1.2.1 UE measurement capability 248

4A.1.2.2 Measurement and evaluation of serving cell 248

4A.1.2.3 Measurements of intra-frequency E-UTRAN cells 248

4A.1.2.4 Measurements of inter-frequency E-UTRAN cells 248

4A.1.2.5 Evaluation of cell re-selection criteria 248

4A.1.2.6 Maximum interruption in paging reception 248

4A.1.2.7 Measurements of inter-RAT NR cells 248

4A.1.2.8 UE measurement capability for RedCap 248

4A.1.2.9 Measurements of inter-RAT NR cells for RedCap 248

4A.2 Requirements for UE Category M1 249

4A.2.1 Introduction 249

4A.2.2 Cell Selection 249

4A.2.3 Cell Reselection 249

4A.2.3.1 Cell Re-selection requirements for UE category M1 in normal coverage 249

4A.2.3.1.1 Measurement and evaluation of serving cell for UE category M1 in normal coverage 249

4A.2.3.1.2 Measurements of intra-frequency cells for UE category M1 in normal coverage 250

4A.2.3.1.3 Measurements of inter-frequency cells for UE category M1 in normal coverage 250

4A.2.3.1.4 Maximum allowed layers for multiple monitoring for UE category M1 in normal coverage 250

4A.2.3.1.5 Maximum interruption in paging reception for Category M1 UEs in normal coverage 250

4A.2.4 Channel quality report for UE Category M1 in idle mode 252

5 E-UTRAN RRC_CONNECTED state mobility 252

5.1 E-UTRAN Handover 253

5.1.1 Introduction 253

5.1.2 Requirements 253

5.1.2.1 E-UTRAN FDD – FDD 253

5.1.2.1.1 Handover delay 253

5.1.2.1.2 Interruption time 253

5.1.2.2 E-UTRAN FDD – TDD 254

5.1.2.2.1 (Void) 255

5.1.2.2.2 (Void) 255

5.1.2.3 E-UTRAN TDD – FDD 255

5.1.2.3.1 (Void) 255

5.1.2.3.2 (Void) 255

5.1.2.4 E-UTRAN TDD – TDD 255

5.1.2.4.1 Handover delay 255

5.1.2.4.2 Interruption time 255

5.1.2.5 E-UTRAN HD–FDD 257

5.1.2.5.1 Handover delay 257

5.1.2.5.2 Interruption time 257

5.1.2.6 E-UTRAN FDD – FDD conditional handover 258

5.1.2.6.1 Handover delay 258

5.1.2.6.2 Measurement time 259

5.1.2.6.3 Preparation time 259

5.1.2.6.4 Interruption time 259

5.1.2.7 E-UTRAN FDD – TDD conditional handover 259

5.1.2.8 E-UTRAN TDD – FDD conditional handover 260

5.1.2.9 E-UTRAN TDD – TDD conditional handover 260

5.2 Void 260

5.3 Handover to other RATs 260

5.3.1 E-UTRAN - UTRAN FDD Handover 260

5.3.1.1 Introduction 260

5.3.1.1.1 Handover delay 260

5.3.1.1.2 Interruption time 260

5.3.2 E-UTRAN - UTRAN TDD Handover 261

5.3.2.1 Introduction 261

5.3.2.2 Requirements 261

5.3.2.2.1 Handover delay 261

5.3.2.2.2 Interruption time 261

5.3.3 E-UTRAN - GSM Handover 262

5.3.3.1 Introduction 262

5.3.3.2 Requirements 262

5.3.3.2.1 Handover delay 262

5.3.3.2.2 Interruption time 262

5.3.4 E-UTRAN - NR FR1 Handover 262

5.3.4.1 Introduction 262

5.3.4.2 Handover delay 263

5.3.4.3 Interruption time 263

5.3.4A E-UTRAN - NR FR1 Handover to target cell using CCA 263

5.3.4A.1 Introduction 263

5.3.4A.2 Handover delay 264

5.3.4A.3 Interruption time 264

5.3.4B E-UTRAN - NR FR1 Handover for RedCap 265

5.3.4B.1 Introduction 265

5.3.4B.2 Requirements 265

5.3.5 E-UTRAN - NR FR2 Handover 265

5.3.5.1 Introduction 265

5.3.5.2 Handover delay 265

5.3.5.3 Interruption time 265

5.4 Handover to Non-3GPP RATs 266

5.4.1 E-UTRAN – HRPD Handover 266

5.4.1.1 Introduction 266

5.4.1.1.1 Handover delay 266

5.4.1.1.2 Interruption time 266

5.4.2 E-UTRAN – cdma2000 1X Handover 267

5.4.2.1 Introduction 267

5.4.2.1.1 Handover delay 267

5.4.2.1.2 Interruption time 267

5.5 E-UTRAN Handover for Cat-M1 UEs 267

5.5.1 Introduction 267

5.5.2 Requirements in CEModeA 268

5.5.2.1 E-UTRAN FDD – FDD for Cat-M1 FDD UEs 268

5.5.2.1.1 Handover delay 268

5.5.2.1.2 Interruption time 268

5.5.2.2 E-UTRAN FDD – FDD for Cat-M1 HD – FDD UEs 268

5.5.2.3 E-UTRAN TDD – TDD for Cat-M1 TDD UEs 269

5.5.2.3.1 Void 269

5.5.2.3.2 Void 269

5.5.3 Requirements in CEModeB 269

5.5.3.1 E-UTRAN FDD – FDD for Cat-M1 FDD UEs 269

5.5.3.1.1 Handover delay 269

5.5.3.1.2 Interruption time 269

5.5.3.2 E-UTRAN FDD – FDD for Cat-M1 HD – FDD UEs 270

5.5.3.3 E-UTRAN TDD – TDD for Cat-M1 TDD UEs 270

5.5A E-UTRAN Handover for Cat-M1 UEs for Satellite Access 270

5.5A.1 Introduction 270

5.5A.2 Requirements in CEModeA 270

5.5A.2.1 E-UTRAN FDD – FDD HO for Cat-M1 FDD UEs 270

5.5A.2.1.1 Handover delay 270

5.5A.2.1.2 Interruption time 270

5.5A.2.2 E-UTRAN FDD – FDD HO for Cat-M1 HD – FDD UEs 271

5.5A.2.3 E-UTRAN FDD – FDD conditional HO for Cat-M1 FDD UEs 271

5.5A.2.3.1 Handover delay 271

5.5A.2.3.2 Measurement time 272

5.5A.2.3.3 Preparation time 273

5.5A.2.3.4 Interruption time 273

5.5A.2.4 E-UTRAN FDD – FDD conditional HO for Cat-M1 HD – FDD UEs 274

5.5A.3 Requirements in CEModeB 274

5.5A.3.1 E-UTRAN FDD – FDD HO for Cat-M1 FDD UEs 274

5.5A.3.1.1 Handover delay 274

5.5A.3.1.2 Interruption time 274

5.5A.3.2 E-UTRAN FDD – FDD HO for Cat-M1 HD – FDD UEs 275

5.5A.3.3 E-UTRAN FDD – FDD conditional HO for Cat-M1 FDD UEs 275

5.5A.3.3.1 Handover delay 275

5.5A.3.3.2 Measurement time 276

5.5A.3.3.3 Preparation time 277

5.5A.3.3.4 Interruption time 277

5.5A.3.4 E-UTRAN FDD – FDD conditional HO for Cat-M1 HD – FDD UEs 278

5.6 Void 278

5.7 E-UTRAN DAPS Handover 278

5.7.1 Introduction 278

5.7.2 Requirements 279

5.7.2.1 E-UTRAN FDD – FDD 279

5.7.2.1.1 DAPS Handover delay 279

5.7.2.1.2 Interruption time 279

5.7.2.2 E-UTRAN FDD – TDD 280

5.7.2.3 E-UTRAN TDD – FDD 280

5.7.2.4 E-UTRAN TDD – TDD 280

5.8 EN-DC Handover with PSCell 280

5.8.1 Introduction 280

5.8.1.1 Handover with PSCell Interruption time 280

5.8.1.2 Handover with PSCell - NR PSCell Change Delay requirements 281

5.9 EN-DC Handover with PSCell using CCA 282

5.9.1 Introduction 282

5.9.1.1 Handover with PSCell – E-UTRA HO Interruption time 282

5.9.1.2 Handover with PSCell - NR PSCell Change Delay requirements 282

6 RRC Connection Mobility Control 283

6.1 RRC Re-establishment 283

6.1.1 Introduction 283

6.1.2 Requirements 283

6.1.2.1 UE Re-establishment delay requirement 284

6.2 Random Access 284

6.2.1 Introduction 284

6.2.2 Requirements 284

6.2.2.1 Contention based random access 284

6.2.2.1.1 Correct behaviour when receiving Random Access Response reception 284

6.2.2.1.2 Correct behaviour when not receiving Random Access Response reception 285

6.2.2.1.3 Correct behaviour when receiving a NACK on msg3 285

6.2.2.1.4 Void 285

6.2.2.1.5 Correct behaviour when receiving a message over Temporary C-RNTI 285

6.2.2.1.6 Correct behaviour when contention Resolution timer expires 285

6.2.2.2 Non-Contention based random access 285

6.2.2.2.1 Correct behaviour when receiving Random Access Response 285

6.2.2.2.2 Correct behaviour when not receiving Random Access Response 285

6.2.3 Requirements for Cat-M1 UEs 285

6.2.3A Random Access Requirements for Cat-M1 UEs for Satellite Access 286

6.2.4A Random Access Requirements for Cat-M1 UEs with CB-Msg3 EDT for Satellite Access 286

6.2.4A.1 Correct behaviour when transmitting CB-Msg3 286

6.2.4A.2 Correct behaviour when receiving CB-Msg4 286

6.2.4A.3 Correct behaviour when not receiving CB-Msg4 286

6.2.4A.4 MSG3-based channel quality report for UE Category NB1 with CB-Msg3-EDT procedure 286

6.3 RRC Connection Release with Redirection 287

6.3.1 Introduction 287

6.3.2 Requirements 287

6.3.2.1 RRC connection release with redirection to UTRAN FDD 287

6.3.2.2 RRC connection release with redirection to GERAN 288

6.3.2.3 RRC connection release with redirection to UTRAN TDD 288

6.3.2.4 RRC connection release with redirection to NR 289

6.3.2.5 RRC connection release with redirection to NR carrier subject to CCA 289

6.3.2.6 RRC connection release with redirection to NR Redcap 291

6.4 CSG Proximity Indication for E-UTRAN and UTRAN 292

6.4.1 Introduction 292

6.4.2 Requirements 292

6.5 RRC Re-establishment for NB-IoT UEs 292

6.5.1 Introduction 292

6.5.2 Requirements 292

6.5.2.1 UE Re-establishment delay requirement in normal coverage 292

6.5.2.2 UE Re-establishment delay requirement in enhanced coverage 293

6.5A RRC Re-establishment for NB-IoT UEs for Satellite Access 293

6.5A.1 Introduction 293

6.5A.2 Requirements 294

6.5A.2.1 UE Re-establishment delay requirement in normal coverage 294

6.5A.2.2 UE Re-establishment delay requirement in enhanced coverage 294

6.5B RRC Re-establishment for NB-IoT UEs for frame structure type 1 for NTN-TDD 295

6.5B.1 Introduction 295

6.5B.2 Requirements 295

6.5B.2.1 UE Re-establishment delay requirement in normal coverage 295

6.6 Random Access for UE category NB1 296

6.6.1 Introduction 296

6.6.2 Requirements 296

6.6.2.1 Correct behaviour when receiving Random Access Response reception 296

6.6.2.2 Correct behaviour when not receiving Random Access Response reception 296

6.6.2.3 Correct behaviour when receiving a NACK on msg3 297

6.6.2.4 Correct behaviour when receiving a message over Temporary C-RNTI 297

6.6.2.5 Correct behaviour when contention Resolution timer expires 297

6.6.2.6 MSG3-based channel quality report for UE Category NB1 297

6.6.3 Requirements for NPRACH configuration 297

6.6A Random Access for UE category NB-IoT for Satellite Access 298

6.6A.1 Introduction 298

6.6A.2 Requirements 298

6.6A.2.1 Correct behaviour when receiving Random Access Response reception 298

6.6A.2.2 Correct behaviour when not receiving Random Access Response reception 298

6.6A.2.3 Correct behaviour when receiving a NACK on msg3 298

6.6A.2.4 Correct behaviour when receiving a message over Temporary C-RNTI 298

6.6A.2.5 Correct behaviour when contention Resolution timer expires 299

6.6A.2.6 MSG3-based channel quality report for UE Category NB1 299

6.6A.3 Requirements for NPRACH configuration 299

6.6A.4 Requirements for CB-Msg3-EDT procedure 300

6.6A.4.1 Correct behaviour when transmitting CB-Msg3 300

6.6A.4.2 Correct behaviour when receiving a CB-Msg4 over CB-RNTI 300

6.6A.4.3 Correct behaviour when detecting CB-Msg3-EDT failure 300

6.6A.4.4 MSG3-based channel quality report for UE Category NB1 with CB-Msg3-EDT procedure 300

6.6B Random Access for UE category NB-IoT for frame structure type 1 for NTN-TDD 301

6.6B.1 Introduction 301

6.6B.2 Requirements 301

6.6B.2.1 Correct behaviour when receiving Random Access Response reception 301

6.6B.2.2 Correct behaviour when not receiving Random Access Response reception 301

6.6B.2.3 Correct behaviour when receiving a NACK on msg3 302

6.6B.2.4 Correct behaviour when receiving a message over Temporary C-RNTI 302

6.6B.2.5 Correct behaviour when contention Resolution timer expires 302

6.6B.2.6 MSG3-based channel quality report for UE Category NB1 302

6.6B.3 Requirements for NPRACH configuration 302

6.7 RRC Re-establishment for Cat-M1 UEs 303

6.7.1 Introduction 303

6.7.2 Requirements 303

6.7.2.1 UE Re-establishment delay requirement for CEModeA 303

6.7.2.2 UE Re-establishment delay requirement for CEModeB 304

6.7A RRC Re-establishment for Cat-M1 UEs for Satellite Access 304

6.7A.1 Introduction 304

6.7A.2 Requirements 304

6.7A.2.1 UE Re-establishment delay requirement for CEModeA 305

6.7A.2.2 UE Re-establishment delay requirement for CEModeB 305

6.8 RRC Connection Release with Redirection for Cat-M1 UEs 306

6.8.1 Introduction 306

6.8.2 Requirements 306

6.8.2.1 RRC connection release with redirection to E-UTRAN with CE Mode A 306

6.8A RRC Connection Release with Redirection for UE Category M1 for Satellite Access 307

6.8A.1 Introduction 307

6.8A.2 Requirements 307

6.8A.2.1 RRC connection release with redirection to E-UTRAN with CE Mode A 307

6.9 RRC Connection Redirection to Non-anchor Carrier in NB-IoT 308

6.9.1 Introduction 308

6.9.2 Requirements 308

6.9A RRC Connection Redirection to Non-anchor Carrier in NB-IoT for Satellite Access 308

6.9A.1 Introduction 308

6.9B RRC Connection Redirection to Non-anchor Carrier in NB-IoT for frame structure type 1 for NTN-TDD 309

6.9B.1 Introduction 309

6.9B.2 Requirements 310

7 Timing and signalling characteristics 310

7.1 UE transmit timing 310

7.1.1 Introduction 310

7.1.2 Requirements 311

7.2 UE timer accuracy 312

7.2.1 Introduction 312

7.2.2 Requirements 312

7.3 Timing Advance 312

7.3.1 Introduction 312

7.3.2 Requirements 312

7.3.2.1 Timing Advance adjustment delay 312

7.3.2.2 Timing Advance adjustment accuracy 313

7.4 Cell phase synchronization accuracy (TDD) 313

7.4.1 Definition 313

7.4.2 Minimum requirements 313

7.5 Synchronization Requirements for E-UTRAN to 1xRTT and HRPD Handovers 314

7.5.1 Introduction 314

7.5.2 eNodeB Synchronization Requirements 314

7.5.2.1 Synchronized E-UTRAN 314

7.5.2.2 Non-Synchronized E-UTRAN 314

7.6 Radio Link Monitoring 314

7.6.1 Introduction 314

7.6.2 Requirements 316

7.6.2.1 Minimum requirement when no DRX is used 316

7.6.2.2 Minimum requirement when DRX is used 316

7.6.2.3 Minimum requirement at transitions 318

7.6.2.4 Minimum requirement during SI Acquisition with autonomous gaps 318

7.6.2.5 Minimum requirement under IDC Interference 318

7.7 SCell Activation and Deactivation Delay for E-UTRA Carrier Aggregation 318

7.7.1 Introduction 318

7.7.2 SCell Activation Delay Requirement for Deactivated SCell 319

7.7.3 SCell Deactivation Delay Requirement for Activated SCell 320

7.7.4 SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells 321

7.7.5 SCell Deactivation Delay Requirement for Activated SCell with Multiple Downlink SCells 322

7.7.6 SCell Activation Delay Requirement for Deactivated PUCCH SCell 323

7.7.7 SCell Activation Delay Requirement for Deactivated PUCCH SCell with Multiple SCells 324

7.7.8 SCell Deactivation Delay Requirement for Activated PUCCH SCell 325

7.7.9 SCell Deactivation Delay Requirement for Activated PUCCH SCell with Multiple SCells 325

7.7.10 SCell Activation Delay Requirement for Deactivated SCell under Frame Structure 3 325

7.7.11 SCell Deactivation Delay Requirement for Activated SCell under Frame Structure 3 326

7.7.12 SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells under Frame Structure 3 327

7.7.13 SCell Deactivation Delay Requirement for Activated SCell with Multiple Downlink SCells under Frame Structure 3 328

7.7.14 SCell Activation Delay Requirement for Dormant SCell 328

7.7.15 SCell Hibernation Delay Requirement for Activated SCell 330

7.7.16 SCell Hibernation Delay Requirement for Deactivated SCell 330

7.7.17 SCell Deactivation Delay Requirement for Dormant SCell 332

7.7.18 Direct SCell Activation and Hibernation Delay Requirement 332

7.7.19 Direct SCell Activation and Hibernation Delay Requirement at RRC Reconfiguration during Handover 334

7.8 Interruptions with Carrier Aggregation 336

7.8.1 Introduction 336

7.8.2 Requirements 336

7.8.2.1 Interruptions at SCell addition/release for intra-band CA 336

7.8.2.2 Interruptions at SCell addition/release for inter-band CA 336

7.8.2.3 Interruptions at SCell activation/deactivation for intra-band CA 336

7.8.2.4 Interruptions at SCell activation/deactivation for inter-band CA 337

7.8.2.5 Interruptions during measurements on SCC for intra-band CA 337

7.8.2.6 Interruptions during measurements on SCC for inter-band CA 337

7.8.2.7 Interruptions at SCell addition/release with multiple downlink SCells 337

7.8.2.8 Interruptions at SCell activation/deactivation with multiple downlink SCells 337

7.8.2.9 Interruptions during measurements on SCC with multiple downlink SCells 338

7.8.2.10 Interruptions at overlapping addition/release/activation/deactivation of SCells 339

7.8.2.11 Interruptions during RSSI measurements on one SCC under Frame Structure 3 339

7.8.2.12 Interruptions during RSSI measurements on multiple SCCs under Frame Structure 3 339

7.8.2.13 Interruptions at SRS carrier based switching 340

7.8.2.14 Interruptions at SCell activation and deactivation of dormant SCell for intra-band CA 341

7.8.2.15 Interruptions at SCell activation and deactivation of dormant SCell for inter-band CA 341

7.8.2.16 Interruptions at SCell activation and deactivation of multiple dormant SCells 341

7.8.2.17 Interruptions during CQI measurement on dormant SCell 341

7.8.2.18 Interruptions during RRM measurement on dormant SCell for intra-band CA 342

7.8.2.19 Interruptions during RRM measurement on dormant SCell for inter-band CA 342

7.8.2.20 Interruptions at SCell hibernation 342

7.8.2.21 Interruptions at direct SCell activation and hibernation 342

7.8.2.22 Interruptions during inter-RAT NR measurements without measurement gap 343

7.9 Maximum Transmission Timing Difference in Carrier Aggregation 344

7.9.1 Introduction 344

7.9.2 Minimum Requirements for Interband Carrier Aggregation 344

7.9.3 Minimum Requirements for Intraband non-contiguous Carrier Aggregation 344

7.9.4 Minimum Requirements for Inter-Band Carrier Aggregation under Frame Structure 3 344

7.10 Interruptions with RSTD Measurements with Carrier Aggregation 345

7.10.1 Introduction 345

7.10.2 Requirements 345

7.10.2.1 Interruptions during RSTD measurements on SCC for intra-band CA with one downlink SCell 345

7.10.2.2 Interruptions during RSTD measurements on SCC for inter-band CA with one downlink SCell 345

7.10.2.3 Interruptions during RSTD measurements on SCC with multiple downlink SCells 345

7.10.2.4 Interruptions at overlapping RSTD and inter-frequency measurements 346

7.11 Radio Link Monitoring for UE Category 0 346

7.11.1 Introduction 346

7.11.2 Requirements for FD-FDD and TDD 347

7.11.2.1 Minimum requirement when no DRX is used 347

7.11.2.2 Minimum requirement when DRX is used 348

7.11.2.3 Minimum requirement at transitions 348

7.11.3 Requirements for HD-FDD 349

7.11.3.1 Minimum requirement when no DRX is used 349

7.11.3.2 Minimum requirement when DRX is used 349

7.11.3.3 Minimum requirement at transitions 350

7.12 Interruptions with Dual Connectivity 350

7.12.1 Introduction 350

7.12.2 Requirements 350

7.12.2.1 Interruptions at PSCell addition/release 350

7.12.2.2 Interruptions at transitions between active and non-active during DRX 350

7.12.2.3 Interruptions at transitions from non-DRX to DRX 351

7.12.2.4 Interruptions at SCell addition/release 351

7.12.2.5 Interruptions at SCell activation/deactivation 351

7.12.2.6 Interruptions during measurements on SCC 352

7.12.2.7 Interruptions at SRS carrier based switching 352

7.13 Cell phase synchronization accuracy (Synchronized mode of dual connectivity) 353

7.13.1 Definition 353

7.13.2 Minimum requirements 353

7.14 PSCell Addition and Release Delay for E-UTRA Dual Connectivity 353

7.14.1 Introduction 353

7.14.2 PSCell Addition Delay Requirement 353

7.14.3 PSCell Release Delay Requirement 354

7.15 Maximum Receive Timing Difference in Dual Connectivity 354

7.15.1 Introduction 354

7.15.2 Minimum Requirements for Inter-band Dual Connectivity 354

7.16 Proximity-based Services 354

7.16.1 Introduction 354

7.16.2 Requirements 354

7.16.2.1 ProSe UE transmission timing 354

7.16.2.1.1 Serving cell or PCell as timing reference 355

7.16.2.1.2 SCell or non-serving cell as timing reference 355

7.16.3 Interruptions with ProSe 355

7.16.3.1 Interruptions at ProSe Direct Discovery configuration 355

7.16.3.2 Interruptions at ProSe Direct Communication configuration 356

7.16.3.3 Interruptions during ProSe Direct Discovery 356

7.16.3.4 Interruptions during ProSe Direct Discovery with discovery gaps 356

7.16.3.5 Interruptions during ProSe Direct Communication 357

7.16.4 Cell reselection for ProSe Direct Discovery on non-serving frequency 357

7.16.4.1 Measurement and evaluation of selected cell 357

7.16.4.2 Measurement of intra-frequency E-UTRAN cells 357

7.16.5 Selection / Reselection of ProSe relay UE 358

7.16.6 ProSe operation under deactivated SCell 358

7.17 Maximum Transmission Timing Difference in Dual Connectivity 358

7.17.1 Introduction 358

7.17.2 Minimum Requirements for maximum transmission timing difference Inter-band Dual Connectivity 359

7.18.1 Introduction 359

7.18.2 SCell Activation Delay Requirement for Deactivated SCell 359

7.18.3 SCell Deactivation Delay Requirement for Activated SCell 359

7.19 Radio Link Monitoring for UE Category M1 359

7.19.1 Introduction 359

7.19.2 Requirements for FD-FDD and TDD CE mode A 360

7.19.2.1 Minimum requirement when no DRX is used 361

7.19.2.2 Minimum requirement when DRX is used 362

7.19.2.3 Minimum requirement at transitions 363

7.19.3 Requirements for HD-FDD with CE mode A 363

7.19.3.1 Minimum requirement when no DRX is used 364

7.19.3.2 Minimum requirement when DRX is used 364

7.19.3.3 Minimum requirement at transitions 365

7.19.4 Requirements for FD-FDD and TDD with CE mode B 365

7.19.4.1 Minimum requirement when no DRX is used 367

7.19.4.2 Minimum requirement when DRX is used 368

7.19.4.3 Minimum requirement at transitions 369

7.19.5 Requirements for HD-FDD with CE mode B 369

7.19.5.1 Minimum requirement when no DRX is used 369

7.19.5.2 Minimum requirement when DRX is used 370

7.19.5.3 Minimum requirement at transitions 371

7.19A Radio Link Monitoring for UE Category M1 for Satellite Access 371

7.19A.1 Introduction 371

7.19A.2 Requirements for FD-FDD and CE mode A 371

7.19A.2.1 Minimum requirement when no DRX is used 373

7.19A.2.2 Minimum requirement when DRX is used 374

7.19A.2.3 Minimum requirement at transitions 375

7.19A.3 Requirements for HD-FDD with CE mode A 375

7.19A.3.1 Minimum requirement when no DRX is used 375

7.19A.3.2 Minimum requirement when DRX is used 376

7.19A.3.3 Minimum requirement at transitions 377

7.19A.4 Requirements for HD-FDD with CE mode B 377

7.19A.4.1 Minimum requirement when no DRX is used 377

7.19A.4.2 Minimum requirement when DRX is used 377

7.19A.4.3 Minimum requirement at transitions 378

7.20 UE transmit timing for NB-IoT 379

7.20.1 Introduction 379

7.20.2 Requirements 379

7.20A UE transmit timing for NB-IoT for Satellite Access 379

7.20A.1 Introduction 379

7.20A.2 Requirements 380

7.20B UE transmit timing for NB-IoT for frame structure type 1 for NTN-TDD 380

7.20B.1 Introduction 380

7.20B.2 Requirements 381

7.21  UE timer accuracy for NB-IoT 381

7.21.1 Introduction 381

7.21.2 Requirements 381

7.21A UE timer accuracy for NB-IoT for Satellite Access 382

7.21A.1 Introduction 382

7.21A.2 Requirements 382

7.21B UE timer accuracy for NB-IoT for frame structure type 1 for NTN-TDD 382

7.21B.1 Introduction 382

7.21B.2 Requirements 382

7.22 Timing Advance for NB-IoT 383

7.22.1 Introduction 383

7.22.2 Requirements 383

7.22.2.1 Timing Advance adjustment delay 383

7.22.2.2 Timing Advance adjustment accuracy 383

7.22A Timing Advance for NB-IoT for Satellite Access 383

7.22A.1 Introduction 383

7.22A.2 Requirements 383

7.22A.2.1 Timing Advance adjustment delay 383

7.22A.2.2 Timing Advance adjustment accuracy 383

7.22B Timing Advance for NB-IoT for frame structure type 1 for NTN-TDD 383

7.22B.1 Introduction 383

7.22B.2 Requirements 383

7.22B.2.1 Timing Advance adjustment delay 383

7.22B.2.2 Timing Advance adjustment accuracy 384

7.23 Radio Link Monitoring for Category NB1 UE 384

7.23.1 Introduction 384

7.23.2 Requirements for Category NB1 UE 384

7.23.2.1 Minimum requirement when no DRX is used 384

7.23.2.2 Minimum requirement when DRX is used 385

7.23.2.3 Minimum requirement at transitions 385

7.23A Radio Link Monitoring for Category NB-IoT UE for Satellite Access 386

7.23A.1 Introduction 386

7.23A.2 Requirements for Category NB1 UE 386

7.23A.2.1 Minimum requirement when no DRX is used 386

7.23A.2.2 Minimum requirement when DRX is used 387

7.23A.2.3 Minimum requirement at transitions 387

7.23B Radio Link Monitoring for Category NB-IoT UE for frame structure type 1 for NTN-TDD 387

7.23B.1 Introduction 387

7.23B.2 Requirements for Category NB1 UE 388

7.23B.2.1 Minimum requirement when no DRX is used 388

7.23B.2.2 Minimum requirement when DRX is used 389

7.23B.2.3 Minimum requirement at transitions 389

7.24 UE transmit timing for Category M1 389

7.24.1 Introduction 389

7.24.2 Requirements 390

7.24A UE transmit timing for Category M1 for Satellite Access 390

7.24A.1 Introduction 390

7.24A.2 Requirements 391

7.25 Cell phase synchronization accuracy for MBMS services (FDD) 392

7.25.1 Definition 392

7.25.2 Minimum requirements 392

7.26 UE transmit timing for Category M2 392

7.26.1 Introduction 392

7.26.2 Requirements 392

7.27 UE timer accuracy for category M1 393

7.27.1 Introduction 393

7.27.2 Requirements 393

7.27A UE timer accuracy for category M1 for Satellite Access 393

7.27A.1 Introduction 393

7.27A.2 Requirements 393

7.28 Timing Advance for Category M1 393

7.28.1 Introduction 393

7.28.2 Requirements 393

7.28A Timing Advance for Category M1 for Satellite Access 393

7.28A.1 Introduction 393

7.28A.2 Requirements 393

7.28A.2.1 Timing Advance adjustment delay 393

7.28A.2.2 Timing Advance adjustment accuracy 394

7.29 Interruptions requirements with FeMBMS 394

7.29.1 Introduction 394

7.29.2 Requirements 394

7.30 Numerology switching delay requirements with FeMBMS 394

7.30.1 Introduction 394

7.30.2 Requirements 394

7.31 NR PSCell Addition and Release Delay for E-UTRA - NR Dual Connectivity 394

7.31.1 Introduction 394

7.31.2 NR PSCell Addition Delay Requirement 395

7.31.3 NR PSCell Release Delay Requirement 395

7.31A Addition and Release Delay of NR PSCell Operating with CCA for E-UTRA - NR Dual Connectivity 396

7.31A.1 Introduction 396

7.31A.2 NR PSCell Addition Delay Requirement 396

7.31A.3 NR PSCell Release Delay Requirement 397

7.32 Interruptions with EN-DC 397

7.32.1 Introduction 397

7.32.2 Requirements 398

7.32.2.1 Interruptions at PSCell addition/release 398

7.32.2.2 Interruptions at transitions between active and non-active during DRX 398

7.32.2.3 Interruptions at transitions from non-DRX to DRX 398

7.32.2.4 Interruptions at SCell addition/release 398

7.32.2.5 Interruptions at SCell activation/deactivation 398

7.32.2.6 Interruptions during measurements on SCC 399

7.32.2.6.1 Interruptions during measurements on deactivated NR SCC 399

7.32.2.6.2 Interruptions during measurements on deactivated E-UTRA SCC 399

7.32.2.6.3 Interruptions during CQI measurements on dormant E-UTRA SCell 399

7.32.2.6.4 Interruptions during RRM measurements on dormant E-UTRA SCC 400

7.32.2.7 Interruptions at active BWP switching 400

7.32.2.8 Interruptions at SCell activation and deactivation of dormant SCell 401

7.32.2.9 Interruptions at SCell activation and deactivation of multiple dormant SCell 401

7.32.2.10 Interruptions at SCell hibernation 401

7.32.2.11 Interruptions at direct SCell activation and hibernation 401

7.32.2.12 DL Interruptions at UE switching between two uplink carriers 401

7.32.2.13 Interruptions at NR SRS carrier based switching 401

7.32.2.14 Interruptions at NR SCell dormancy 402

7.32.2.14.1 Interruptions due to NR SCell dormancy switch 402

7.32.2.14.2 Interruptions due to CSI and RRM measurements during SCell dormancy 403

7.32.2.15 Interruption during NR measurement with autonomous gaps 403

7.32.2.16 Interruptions at SRS carrier based switching 403

7.32.2.17 Interruptions at SCG activation/deactivation 404

7.32.2.18 Interruptions due to NR SRS antenna port switching 404

7.32.2.19 Interruptions at fast SCell activation/deactivation 404

7.32.2.20 Interruptions due to RRM measurements on deactivated NR SCG 405

7.32.2.21 Interruptions during RLM/BFD measurements on deactivated PScell 405

7.33 Maximum Transmit/Receive Timing Difference in Carrier Aggregation for sTTI and 1ms-TTI with 3 subframe HARQ processing 405

7.33.1 Introduction 405

7.33.2 Requirements 405

7.34 Void 406

7.35 Interruptions with SFTD measurements 406

7.35.1 Introduction 406

7.35.2 Requirements 406

7.36 Interruptions with NE-DC 406

7.36.1 Introduction 406

7.36.2 Requirements 407

7.36.2.1 Interruptions at transitions between active and non-active during DRX 407

7.36.2.2 Interruptions at transitions from non-DRX to DRX 407

7.36.2.3 Interruptions at SCell addition/release 407

7.36.2.4 Interruptions at SCell activation/deactivation 407

7.36.2.5 Interruptions during measurements on SCC 408

7.36.2.5.1 Interruptions during measurements on deactivated NR SCC 408

7.36.2.5.2 Interruptions during measurements on deactivated E-UTRA SCC 408

7.36.2.5.3 Interruptions during CQI measurements on dormant E-UTRA SCell 408

7.36.2.5.4 Interruptions during RRM measurements on dormant E-UTRA SCC 408

7.36.2.6 Interruptions at active BWP switching 408

7.36.2.7 Interruptions at SCell activation and deactivation of dormant SCell 409

7.36.2.8 Interruptions at SCell activation and deactivation of multiple dormant SCell 409

7.36.2.9 Interruptions at SCell hibernation 409

7.36.2.10 Interruptions at direct SCell activation and hibernation 409

7.36.2.11 Interruptions at NR SRS carrier based switching 410

7.36.2.12 Interruptions at NR SCell dormancy 410

7.36.2.12.1 Interruptions due to NR SCell dormancy switch 410

7.36.2.12.2 Interruptions due to CSI and RRM measurements during SCell dormancy 411

7.36.2.13 Interruption during E-UTRA measurement with autonomous gaps 411

7.36.2.14 Interruption during NR measurement with autonomous gaps 411

7.36.2.15 Interruptions at SRS carrier based switching 412

7.36.2.16 Interruptions due to NR SRS antenna port switching 412

7.37 Interruptions during NR measurement with autonomous gaps 413

7.37.1 Introduction 413

7.37.2 Requirements 413

7.38 SCG Activation and Deactivation Delay 413

7.38.1 Introduction 413

7.38.2 SCG Activation Delay Requirement 413

7.38.3 SCG Deactivation Delay Requirement 414

8 UE Measurements Procedures in RRC_CONNECTED State 415

8.1 General Measurement Requirements 415

8.1.1 Introduction 415

8.1.2 Requirements 415

8.1.2.1 UE measurement capability 415

8.1.2.1.1 Monitoring of multiple layers using gaps 423

8.1.2.1.1a Monitoring of multiple layers using gaps (Increased UE carrier monitoring) 424

8.1.2.1.1b Monitoring of multiple layers using gaps (EN-DC) 425

8.1.2.1.1c Monitoring of multiple layers using gaps (NE-DC) 427

8.1.2.1.1d Monitoring of multiple layers using gaps (RedCap) 428

8.1.2.1.2 Network controlled small gap 428

8.1.2.2 E-UTRAN intra frequency measurements 430

8.1.2.2.1 E-UTRAN FDD intra frequency measurements 430

8.1.2.2.2 E-UTRAN TDD intra frequency measurements 435

8.1.2.2.3 E-UTRAN FDD intra frequency measurements with autonomous gaps 439

8.1.2.2.4 E-UTRAN TDD intra frequency measurements with autonomous gaps 440

8.1.2.2.5 E-UTRAN FDD intra-frequency measurements on carrier with FeMBMS/Unicast mixed cells 441

8.1.2.3 E-UTRAN inter frequency measurements 441

8.1.2.3.1 E-UTRAN FDD – FDD inter frequency measurements 442

8.1.2.3.2 E-UTRAN TDD – TDD inter frequency measurements 447

8.1.2.3.3 E-UTRAN TDD – FDD inter frequency measurements 454

8.1.2.3.4 E-UTRAN FDD – TDD inter frequency measurements 454

8.1.2.3.5 E-UTRAN FDD-FDD inter frequency measurements with autonomous gaps 454

8.1.2.3.6 E-UTRAN TDD-FDD inter frequency measurements using autonomous gaps 455

8.1.2.3.7 E-UTRAN TDD-TDD inter frequency measurements with autonomous gaps 457

8.1.2.3.8 E-UTRAN FDD-TDD inter frequency measurements using autonomous gaps 458

8.1.2.3.9 E-UTRAN FDD – FDD inter frequency measurements with FeMBMS/Unicast mixed cells 459

8.1.2.3.10 E-UTRAN TDD – FDD inter frequency measurements with FeMBMS/Unicast mixed cells 466

8.1.2.4 Inter RAT measurements 466

8.1.2.4.1 E-UTRAN FDD – UTRAN FDD measurements 466

8.1.2.4.2 E-UTRAN TDD – UTRAN FDD measurements 471

8.1.2.4.3 E-UTRAN TDD – UTRAN TDD measurements 471

8.1.2.4.4 E-UTRAN FDD – UTRAN TDD measurements 475

8.1.2.4.5 E-UTRAN FDD – GSM measurements 475

8.1.2.4.6 E-UTRAN TDD – GSM measurements 480

8.1.2.4.7 E-UTRAN FDD – UTRAN FDD measurements for SON 480

8.1.2.4.8 E-UTRAN TDD – UTRAN FDD measurements for SON 482

8.1.2.4.9 E-UTRAN FDD – cdma2000 1xRTT measurements 482

8.1.2.4.9.1A E-UTRAN FDD – cdma2000 1xRTT measurements when no DRX is used 482

8.1.2.4.10 E-UTRAN TDD – cdma2000 1xRTT measurements 483

8.1.2.4.11 E-UTRAN FDD – HRPD measurements 483

8.1.2.4.12 E-UTRAN TDD – HRPD measurements 483

8.1.2.4.13 E-UTRAN TDD – UTRAN TDD measurements for SON 483

8.1.2.4.14 E-UTRAN FDD – UTRAN TDD measurements for SON 485

8.1.2.4.15 E-UTRAN FDD – cdma2000 1xRTT measurements for SON ANR 485

8.1.2.4.16 E-UTRAN TDD – cdma2000 1xRTT measurements for SON ANR 485

8.1.2.4.17 E-UTRAN FDD-UTRAN FDD measurements with autonomous gaps 485

8.1.2.4.18 E-UTRAN TDD-UTRAN FDD measurements with autonomous gaps 486

8.1.2.4.19 E-UTRAN FDD – WLAN measurements 486

8.1.2.4.20 E-UTRAN TDD – WLAN measurements 488

8.1.2.4.21 E-UTRAN FDD – NR measurements 488

8.1.2.4.21A E-UTRAN FDD – NR measurements when CCA is used 492

8.1.2.4.22 E-UTRAN TDD – NR measurements 496

8.1.2.4.22A E-UTRAN TDD – NR measurements when CCA is used 496

8.1.2.4.23 Void 496

8.1.2.4.24 Void 496

8.1.2.4.25 E-UTRAN FDD – NR SFTD Measurements 496

8.1.2.4.26 E-UTRAN TDD – NR SFTD Measurements 498

8.1.2.4.27  E-UTRA FDD - NR measurements with autonomous gaps 498

8.1.2.4.28  E-UTRA TDD - NR measurements with autonomous gaps 499

8.1.2.4.29 E-UTRAN FDD – NR measurements without measurement gap 499

8.1.2.4.30 E-UTRAN TDD – NR measurements without measurement gap 504

8.1.2.5 E-UTRAN OTDOA Intra-Frequency RSTD Measurements 504

8.1.2.5.1 E-UTRAN FDD Intra-Frequency OTDOA Measurements 504

8.1.2.5.2 E-UTRAN TDD Intra-Frequency OTDOA Measurements 506

8.1.2.5.3 E-UTRAN FDD Intra-Frequency OTDOA Measurements for UE Category 1bis 507

8.1.2.5.4 E-UTRAN TDD Intra-Frequency OTDOA Measurements for UE Category 1bis 509

8.1.2.6.5 Void 511

8.1.2.6.6 Void 511

8.1.2.6.7 Void 511

8.1.2.6.8 Void 511

8.1.2.6 E-UTRAN Inter-Frequency OTDOA Measurements 511

8.1.2.6.1 E-UTRAN FDD-FDD Inter-Frequency OTDOA Measurements 511

8.1.2.6.2 E-UTRAN TDD-FDD Inter-Frequency OTDOA Measurements 513

8.1.2.6.3 E-UTRAN TDD-TDD Inter-Frequency OTDOA Measurements 515

8.1.2.6.4 E-UTRAN FDD-TDD Inter-Frequency OTDOA Measurements 516

8.1.2.6.5 E-UTRAN FDD-FDD Inter-Frequency OTDOA Measurements for UE Category 1bis 518

8.1.2.6.6 E-UTRAN TDD-FDD Inter-Frequency OTDOA Measurements for UE Category 1bis 520

8.1.2.6.7 E-UTRAN TDD-TDD Inter-Frequency OTDOA Measurements for UE Category 1bis 521

8.1.2.6.8 E-UTRAN FDD-TDD Inter-Frequency OTDOA Measurements for UE Category 1bis 523

8.1.2.7 E-UTRAN E-CID Measurements 525

8.1.2.7.1 E-UTRAN FDD UE Rx-Tx Time Difference Measurements 525

8.1.2.7.2 E-UTRAN TDD UE Rx-Tx Time Difference Measurements 526

8.1.2.7.3 E-UTRAN FDD Intra-frequency E-CID RSRP and RSRQ Measurements 528

8.1.2.7.4 E-UTRAN TDD Intra-frequency E-CID RSRP and RSRQ Measurements 528

8.1.2.8 E-UTRAN intra-frequency measurements under time domain measurement resource restriction 529

8.1.2.8.1 E-UTRAN FDD intra-frequency measurements 529

8.1.2.8.2 E-UTRAN TDD intra-frequency measurements 532

8.1.2.8.3 E-UTRAN FDD intra-frequency measurements with CRS assistance information 535

8.1.2.8.4 E-UTRAN TDD intra-frequency measurements with CRS assistance infromation 538

8.1.2.9 E-UTRAN E-CID Measurements when Time Domain Measurement Resource Restriction Pattern is Configured 542

8.1.2.9.1 E-UTRAN FDD UE Rx-Tx Time Difference Measurements 542

8.1.2.9.2 E-UTRAN TDD UE Rx-Tx Time Difference Measurements 542

8.1.2.9.3 E-UTRAN FDD UE Rx-Tx Time Difference Measurements with CRS Assistance Information 543

8.1.2.9.4 E-UTRAN TDD UE Rx-Tx Time Difference Measurements with CRS Assistance Information 543

8.1.2.10 Void 544

8.2 Capabilities for Support of Event Triggering and Reporting Criteria 544

8.2.1 Introduction 544

8.2.2 Requirements 544

8.3 Measurements for E-UTRA carrier aggregation 548

8.3.1 Introduction 548

8.3.2 Measurements of the primary component carrier 548

8.3.3 Measurements of a secondary component carrier 548

8.3.3.1 Measurements of a secondary component carrier with active SCell 548

8.3.3.2 Measurements of a secondary component carrier with deactivated SCell 549

8.3.3.2.1 E-UTRAN secondary component carrier measurements when no common DRX is used 549

8.3.3.2.2 E-UTRAN secondary component carrier measurements when common DRX is used 550

8.3.3.3 Measurements on a secondary component carrier with FeMBMS/Unicast mixed cells and activated SCell 552

8.3.3.4 Measurements on a secondary component carrier with FeMBMS/Unicast mixed cells and deactivated SCell 552

8.4 OTDOA RSTD Measurements for E-UTRAN carrier aggregation 552

8.4.1 Introduction 552

8.4.2 Measurements on the primary component carrier 553

8.4.3 Measurements on a secondary component carrier 554

8.4.4 Measurements on both primary component carrier and a secondary component carrier 554

8.4.5 Measurements on different secondary component carriers 555

8.5 Measurements for UE category 0 556

8.5.1 Introduction 556

8.5.2  Requirements 557

8.5.2.1  E-UTRAN intra frequency measurements 557

8.5.2.1.1  E-UTRAN FDD intra frequency measurements 557

8.5.2.1.2  E-UTRAN intra frequency measurements for HD-FDD 560

8.5.2.1.3 E-UTRAN TDD intra frequency measurements 562

8.5.2.1.4 E-UTRAN FDD intra frequency measurements with autonomous gaps for UE category 0 566

8.5.2.1.5 E-UTRAN intra frequency measurements with autonomous gaps for HD-FDD UE category 0 566

8.5.2.1.6 E-UTRAN TDD intra frequency measurements with autonomous gaps for UE category 0 567

8.6 Discovery signal measurements 568

8.6.1 Introduction 568

8.6.2 Requirements for CRS based discovery signal measurements 568

8.6.2.1 E-UTRAN intra frequency measurements 568

8.6.2.1.1 E-UTRAN FDD intra frequency measurements 568

8.6.2.1.2 E-UTRAN TDD intra frequency measurements 571

8.6.2.2 E-UTRAN inter frequency measurements 573

8.6.2.2.1 E-UTRAN FDD – FDD inter-frequency measurements 574

8.6.2.2.2 E-UTRAN TDD – TDD inter frequency measurements 576

8.6.2.2.3 E-UTRAN TDD – FDD inter frequency measurements 579

8.6.2.2.4 E-UTRAN FDD – TDD inter frequency measurements 579

8.6.3 Requirements for CSI-RS based discovery signal measurements 579

8.6.3.1 E-UTRAN intra frequency measurements 579

8.6.3.1.1 E-UTRAN FDD intra frequency measurements 580

8.6.3.1.2 E-UTRAN TDD intra frequency measurements 582

8.6.3.2 E-UTRAN inter frequency measurements 584

8.6.3.2.1 E-UTRAN FDD – FDD inter frequency measurements 585

8.6.3.2.2 E-UTRAN TDD – TDD inter frequency measurements 587

8.6.3.2.3 E-UTRAN TDD – FDD inter frequency measurements 590

8.6.3.2.4 E-UTRAN FDD – TDD inter frequency measurements 590

8.7 Discovery signal measurements for E-UTRA carrier aggregation 590

8.7.1 Introduction 590

8.7.2 Requirements for CRS based discovery signal measurements for E-UTRA carrier aggregation 591

8.7.2.1 Measurements of the primary component carrier 591

8.7.2.2 Measurements of a secondary component carrier 591

8.7.2.3 Measurements of a secondary component carrier with active SCell 591

8.7.2.4 Measurements of a secondary component carrier with deactivated SCell 591

8.7.2.4.1 E-UTRAN secondary component carrier measurements when no common DRX is used 591

8.7.2.4.2 E-UTRAN secondary component carrier measurements when common DRX is used 592

8.7.3 Requirements for CSI-RS based discovery signal measurements for E-UTRA carrier aggregation 594

8.7.3.1 Measurements of the primary component carrier 594

8.7.3.2 Measurements of a secondary component carrier 594

8.7.3.3 Measurements of a secondary component carrier with active SCell 594

8.7.3.4 Measurements of a secondary component carrier with deactivated SCell 594

8.7.3.4.1 E-UTRAN secondary component carrier measurements when no common DRX is used 594

8.7.3.4.2 E-UTRAN secondary component carrier measurements when common DRX is used 596

8.8 Measurements for E-UTRA dual connectivity 597

8.8.1 Introduction 597

8.8.2 Intra-frequency measurements requirements on PCell 597

8.8.3 Intra-frequency measurements requirements on PSCell 598

8.8.4 Inter-frequency and inter-RAT measurement requirements 598

8.8.5 Intra-frequency measurements with autonomous gaps 598

8.8.5.1 Identification of a new CGI of E-UTRA cell with autonomous gaps 598

8.8.5.2 ECGI reporting delay 599

8.8.6 Inter-frequency measurements with autonomous gaps 599

8.8.6.1 Identification of a new CGI of E-UTRA cell with autonomous gaps 599

8.8.6.2 ECGI reporting delay 600

8.8.7 SSTD Measurements 600

8.8.7.1 Introduction 600

8.8.7.2 SSTD Measurement requirements 600

8.8.7.3 SSTD Measurement Reporting Delay 601

8.8.8 Intra-frequency measurements requirements on SCell 601

8.9 MBSFN Measurements 601

8.9.1 Introduction 601

8.9.2 MBSFN RSRP Measurements 601

8.9.3 MBSFN RSRQ Measurements 602

8.9.4 MCH BLER Measurements 602

8.10 Proximity-based Services 602

8.10.1 Introduction 602

8.10.2 Requirements 602

8.10.2.1 Initiation/Cease of SLSS transmissions with ProSe Direct Discovery 602

8.10.2.2 Initiation/Cease of SLSS transmissions with ProSe Direct Communication 603

8.11 Discovery Signal Measurements under Operation with Frame Structure 3 604

8.11.1 Introduction 604

8.11.2 CRS based discovery signal measurements 604

8.11.2.1 E-UTRAN intra-frequency measurements 604

8.11.2.1.1 Requirements 604

8.11.2.1.1.1 Requirements when no DRX is used 604

8.11.2.1.1.1.1 Measurement Reporting Requirements 606

8.11.2.1.1.2 Requirements when DRX is used 607

8.11.2.1.1.2.1 Measurement Reporting Requirements 609

8.11.2.2 E-UTRAN inter-frequency measurements 610

8.11.2.2.1 E-UTRAN FDD-FS3 inter-frequency measurements 610

8.11.2.2.2 E-UTRAN TDD – FS3 inter-frequency measurements 614

8.11.3 CSI-RS based discovery signal measurements 614

8.11.3.1 E-UTRAN intra-frequency measurements 614

8.11.3.1.1 Requirements 614

8.11.3.1.1.1 Requirements when no DRX is used 614

8.11.3.1.1.1.1 Measurement Reporting Requirements 616

8.11.3.1.1.2 Requirements when DRX is used 616

8.11.3.1.1.2.1 Measurement Reporting Requirements 617

8.11.3.2 E-UTRAN inter-frequency measurements 618

8.11.3.2.1 E-UTRAN FDD – FS3 inter-frequency measurements 618

8.11.3.2.2 E-UTRAN TDD – FS3 inter-frequency measurements 622

8.11.4 RSSI measurements 622

8.11.4.1 E-UTRAN intra-frequency measurements 622

8.11.4.2 E-UTRAN inter-frequency measurements 622

8.11.5 Channel occupancy measurements 623

8.11.5.1 E-UTRAN intra-frequency channel occupancy measurements 623

8.11.5.2 E-UTRAN inter-frequency channel occupancy measurements 623

8.12 Discovery Signal Measurements for E-UTRA Carrier Aggregation under Operation with Frame Structure 3 623

8.12.1 Introduction 623

8.12.2 CRS based discovery signal measurements for E-UTRA carrier aggregation 623

8.12.2.1 Introduction 623

8.12.2.2 Measurements of a secondary component carrier 623

8.12.2.3 Measurements of a secondary component carrier with active SCell 623

8.12.2.4 Measurements of a secondary component carrier with deactivated SCell 624

8.12.2.4.1 E-UTRAN secondary component carrier measurements when no common DRX is used 624

8.12.2.4.2 E-UTRAN secondary component carrier measurements when common DRX is used 626

8.12.3 Requirements for CSI-RS based discovery signal measurements for E-UTRA carrier aggregation 629

8.12.3.1 Introduction 629

8.12.3.2 Measurements of a secondary component carrier 629

8.12.3.3 Measurements of a secondary component carrier with active SCell 629

8.12.3.4 Measurements of a secondary component carrier with deactivated SCell 629

8.12.3.4.1 E-UTRAN secondary component carrier measurements when no common DRX is used 629

8.12.3.4.2 E-UTRAN secondary component carrier measurements when common DRX is used 631

8.13 Measurements for UE Category M1 633

8.13.1 Introduction 633

8.13.2 Requirements for UE category M1 with CE mode A 633

8.13.2.1 E-UTRAN intra frequency measurements by UE category M1 with CE mode A 634

8.13.2.1.1 E-UTRAN FDD intra frequency measurements 634

8.13.2.1.2 E-UTRAN intra frequency measurements for HD-FDD 639

8.13.2.1.3 E-UTRAN TDD intra frequency measurements 641

8.13.2.2 Void 645

8.13.2.3 E-UTRAN OTDOA Intra-Frequency RSTD Measurements for Cat-M1 UE in CEModeA 645

8.13.2.3.1 E-UTRAN FDD Intra-Frequency OTDOA Measurements 645

8.13.2.3.2 E-UTRAN TDD Intra-Frequency OTDOA Measurements 648

8.13.2.3.3 E-UTRAN HD-FDD Intra-Frequency OTDOA Measurements 650

8.13.2.4 E-UTRAN OTDOA Inter-Frequency RSTD Measurements for Cat-M1 UE in CEModeA 651

8.13.2.4.1 E-UTRAN FDD Inter-Frequency OTDOA Measurements 651

8.13.2.4.2 E-UTRAN TDD Inter-Frequency OTDOA Measurements 653

8.13.2.4.3 E-UTRAN HD-FDD Inter-Frequency OTDOA Measurements 655

8.13.2.5 E-UTRAN E-CID Measurements Requirements for UE category M1 with CE mode A 656

8.13.2.5.1 Intra-frequency FDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeA 656

8.13.2.5.2 Intra-frequency HD-FDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeA 656

8.13.2.5.3 Intra-frequency TDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeA 657

8.13.2.5.4 Inter-frequency FDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeA 657

8.13.2.5.5 Inter-frequency HD-FDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeA 657

8.13.2.5.6 Inter-frequency TDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeA 658

8.13.2.5.7 E-UTRAN FDD UE Rx-Tx Time Difference Measurements for UE category M1 in CEModeA 658

8.13.2.5.8 E-UTRAN TDD UE Rx-Tx Time Difference Measurements for UE category M1 in CEModeA 659

8.13.2.5.9 E-UTRAN HD-FDD UE Rx-Tx Time Difference Measurements for UE category M1 in CEModeA 660

8.13.2.6 E-UTRAN inter frequency measurements by UE category M1 with CE mode A 660

8.13.2.6.1 E-UTRAN FDD - FDD inter frequency measurements 660

8.13.2.6.2 E-UTRAN inter-frequency measurements for HD-FDD 665

8.13.2.6.3 E-UTRAN TDD inter frequency measurements 667

8.13.2.7 Maximum allowed layers for multiple monitoring for UE category M1 with CE mode A 671

8.13.2.8 Channel quality report for UE Category M1 in connected mode with CE mode A 671

8.13.3 Requirements for UE category M1 with CE mode B 672

8.13.3.1 E-UTRAN intra frequency measurements by UE category M1 with CE mode B 672

8.13.3.1.1 E-UTRAN FDD intra frequency measurements 673

8.13.3.1.2 E-UTRAN intra frequency measurements for HD-FDD 677

8.13.3.1.3 E-UTRAN TDD intra frequency measurements 680

8.13.3.1.4 E-UTRAN FDD intra frequency measurements with autonomous gaps for UE category M1 with CE mode B 685

8.13.3.1.5 E-UTRAN intra frequency measurements with autonomous gaps for HD-FDD UE category M1 with CE mode B 686

8.13.3.1.6 E-UTRAN TDD intra frequency measurements with autonomous gaps for UE category M1 with CE mode B 686

8.13.3.2 Void 687

8.13.3.3 E-UTRAN OTDOA Intra-Frequency RSTD Measurements for Cat-M1 UE in CEModeB 687

8.13.3.3.1 E-UTRAN FDD Intra-Frequency OTDOA Measurements 687

8.13.3.3.2 E-UTRAN TDD Intra-Frequency OTDOA Measurements 690

8.13.3.3.3 E-UTRAN HD-FDD Intra-Frequency OTDOA Measurements 692

8.13.3.4 E-UTRAN E-CID Measurements Requirements for UE category M1 with CE mode B 693

8.13.3.4.1 Intra-frequency E-CID FDD RSRP and RSRQ Measurements for Cat-M1 UE in CEModeB 693

8.13.3.4.2 Intra-frequency HD-FDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeB 693

8.13.3.4.3 Intra-frequency TDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeB 693

8.13.3.4.4 Inter-frequency E-CID FDD RSRP and RSRQ Measurements for Cat-M1 UE in CEModeB 694

8.13.3.4.5 Inter-frequency HD-FDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeB 694

8.13.3.4.6 Inter-frequency TDD E-CID RSRP and RSRQ Measurements for Cat-M1 UE in CEModeB 695

8.13.3.5 E-UTRAN inter frequency measurements by UE category M1 with CE Mode B 695

8.13.3.5.1 E-UTRAN FDD - FDD inter frequency measurements 695

8.13.3.5.2  E-UTRAN inter-frequency measurements for HD-FDD 700

8.13.3.5.3 E-UTRAN TDD inter frequency measurements 702

8.13.3.6 Maximum allowed layers for multiple monitoring for UE category M1 with CE mode B 707

8.13.3.7 E-UTRAN OTDOA Inter-Frequency RSTD Measurements for Cat-M1 UE in CEModeB 707

8.13.3.7.1 E-UTRAN FDD Inter-Frequency OTDOA Measurements 707

8.13.3.7.2 E-UTRAN TDD Inter-Frequency OTDOA Measurements 709

8.13.3.7.3 E-UTRAN HD-FDD Inter-Frequency OTDOA Measurements 712

8.13.3.8 Channel quality report for UE Category M1 in connected mode with CE mode B 712

8.13A Measurements for UE Category M1 for Satellite Access 713

8.13A.1 Introduction 713

8.13A.2 Requirements for UE category M1 with CE mode A 713

8.13A.2.1 E-UTRAN intra frequency measurements by UE category M1 with CE mode A 714

8.13A.2.1.1 E-UTRAN FDD intra frequency measurements 714

8.13A.2.1.1.1 E-UTRAN intra frequency measurements when no DRX is used 714

8.13A.2.1.1.2 E-UTRAN intra frequency measurements when DRX is used 716

8.13A.2.1.2 E-UTRAN intra frequency measurements for HD-FDD 718

8.13A.2.1.2.1 E-UTRAN intra frequency measurements when no DRX is used 718

8.13A.2.1.2.2 E-UTRAN intra frequency measurements when DRX is used 718

8.13A.2.2 E-UTRAN inter frequency measurements by UE category M1 with CE mode A 720

8.13A.2.2.1 E-UTRAN FDD - FDD inter frequency measurements 720

8.13A.2.2.1.1 E-UTRAN FDD - FDD inter frequency measurements when no DRX is used 720

8.13A.2.2.1.2 E-UTRAN inter frequency measurements when DRX is used 722

8.13A.2.2.2 E-UTRAN inter-frequency measurements for HD-FDD 724

8.13A.2.2.2.1 E-UTRAN inter-frequency measurements when no DRX is used 724

8.13A.2.2.2.2 E-UTRAN inter frequency measurements when DRX is used 724

8.13A.2.3 Maximum allowed layers for multiple monitoring for UE category M1 with CE mode A 726

8.13A.2.4 Channel quality report for UE Category M1 in connected mode with CE mode A 727

8.13A.3 Requirements for UE category M1 with CE mode B 727

8.13A.3.1 E-UTRAN intra frequency measurements by UE category M1 with CE mode B 728

8.13A.3.1.1 E-UTRAN FDD intra frequency measurements 728

8.13A.3.1.1.1 E-UTRAN intra frequency measurements when no DRX is used 728

8.13A.3.1.1.2 E-UTRAN intra frequency measurements when DRX is used 730

8.13A.3.1.2 E-UTRAN intra frequency measurements for HD-FDD 732

8.13A.3.1.2.1 E-UTRAN intra frequency measurements when no DRX is used 732

8.13A.3.1.2.2 E-UTRAN intra frequency measurements when DRX is used 733

8.13A.3.2 E-UTRAN inter frequency measurements by UE category M1 with CE Mode B 735

8.13A.3.2.1 E-UTRAN FDD - FDD inter frequency measurements 735

8.13A.3.2.1.1 E-UTRAN FDD - FDD inter frequency measurements when no DRX is used 735

8.13A.3.2.1.2 E-UTRAN inter frequency measurements when DRX is used 737

8.13A.3.2.2 E-UTRAN inter-frequency measurements for HD-FDD 739

8.13A.3.2.2.1 E-UTRAN inter-frequency measurements when no DRX is used 739

8.13A.3.2.2.2 E-UTRAN inter frequency measurements when DRX is used 739

8.13A.3.3 Maximum allowed layers for multiple monitoring for UE category M1 with CE mode B 741

8.13A.3.4 Channel quality report for UE Category M1 in connected mode with CE mode B 742

8.14 Measurements for UE category NB1 742

8.14.1 Introduction 742

8.14.2 NB-IoT intra frequency measurements under normal coverage 742

8.14.2.1 NB-IoT intra frequency measurements when no DRX is used 742

8.14.2.2 NB-IoT intra frequency measurements when DRX is used 742

8.14.3 NB-IoT intra frequency measurements under enhanced coverage 743

8.14.3.1 NB-IoT intra frequency measurements when no DRX is used 743

8.14.3.2 NB-IoT intra frequency measurements when DRX is used 743

8.14.4 Connected mode channel quality report for UE Category NB1 743

8.14.5 Connected mode channel quality report for UE Category NB2 supporting 16QAM 743

8.14.6 NB-IoT neighbour cell measurements 744

8.14.6.1 Introduction 744

8.14.6.2 Requirements 744

8.14.6.3 Intra-frequency neighbour cell measurements 744

8.14.6.4 Inter-frequency neighbour cell measurements 745

8.14.6.5  Requirements for monitoring multiple carriers 746

8.14A Measurements for UE category NB-IoT for Satellite Access 746

8.14A.1 Introduction 746

8.14A.2 NB-IoT intra frequency measurements under normal coverage 747

8.14A.2.1 NB-IoT intra frequency measurements when no DRX is used 747

8.14A.2.2 NB-IoT intra frequency measurements when DRX is used 747

8.14A.3 NB-IoT intra frequency measurements under enhanced coverage 747

8.14A.3.1 NB-IoT intra frequency measurements when no DRX is used 747

8.14A.3.2 NB-IoT intra frequency measurements when DRX is used 747

8.14A.4 Connected mode channel quality report for UE Category NB1 747

8.14A.5 Reserved 748

8.14A.6 NB-IoT neighbour cell measurements 748

8.14A.6.1 Introduction 748

8.14A.6.2 Requirements 748

8.14B Measurements for UE category NB-IoT for frame structure type 1 for NTN-TDD 750

8.14B.1 Introduction 750

8.14B.2 NB-IoT intra frequency measurements under normal coverage 751

8.14B.2.1 NB-IoT intra frequency measurements when no DRX is used 751

8.14B.2.2 NB-IoT intra frequency measurements when DRX is used 751

8.14B.4 Connected mode channel quality report for UE Category NB1 751

8.14B.6 NB-IoT neighbour cell measurements 752

8.14B.6.1 Introduction 752

8.14B.6.2 Requirements 752

8.14B.6.3 Intra-frequency neighbour cell measurements 752

8.14B.6.4 Inter-frequency neighbour cell measurements 753

8.14B.6.5 Requirements for monitoring multiple carriers 754

8.15 Void 754

8.16 Measurements for UE Category M2 754

8.16.1 Introduction 754

8.16.2 Requirements for UE category M2 with CE mode A 755

8.16.2.1 E-UTRAN FDD UE Rx-Tx Time Difference Measurements for UE category M2 in CEModeA 755

8.16.2.1.1 UE Rx-Tx Measurement Reporting Delay 755

8.16.2.2 E-UTRAN TDD UE Rx-Tx Time Difference Measurements for UE category M2 in CEModeA 756

8.16.2.2.1 UE Rx-Tx Measurement Reporting Delay 756

8.16.2.2a E-UTRAN HD-FDD UE Rx-Tx Time Difference Measurements for UE category M2 in CEModeA 757

8.16.2.2a.1 UE Rx-Tx Measurement Reporting Delay 757

8.16.2.3 E-UTRAN OTDOA Intra-Frequency RSTD Measurements for Cat-M2 UE in CEModeA 757

8.16.2.3.1 E-UTRAN FDD Intra-Frequency OTDOA Measurements 757

8.16.2.3.2 E-UTRAN TDD Intra-Frequency OTDOA Measurements 760

8.16.2.3.3 E-UTRAN HD-FDD Intra-Frequency OTDOA Measurements 763

8.16.2.4 E-UTRAN OTDOA Inter-Frequency RSTD Measurements for Cat-M2 UE in CEModeA 763

8.16.2.4.1 E-UTRAN FDD Inter-Frequency OTDOA Measurements 763

8.16.2.4.2 E-UTRAN TDD Inter-Frequency OTDOA Measurements 765

8.16.2.4.3 E-UTRAN HD-FDD Inter-Frequency OTDOA Measurements 768

8.16.3 Requirements for UE category M2 with CE mode B 768

8.16.3.1 E-UTRAN OTDOA Intra-Frequency RSTD Measurements for Cat-M2 UE in CEModeB 768

8.16.3.1.1 E-UTRAN FDD Intra-Frequency OTDOA Measurements 768

8.16.3.1.2 E-UTRAN TDD Intra-Frequency OTDOA Measurements 771

8.16.3.1.3 E-UTRAN HD-FDD Intra-Frequency OTDOA Measurements 774

8.16.3.2 E-UTRAN OTDOA Inter-Frequency RSTD Measurements for Cat-M2 UE in CEModeB 774

8.16.3.2.1 E-UTRAN FDD Inter-Frequency OTDOA Measurements 774

8.16.3.2.2 E-UTRAN TDD Inter-Frequency OTDOA Measurements 776

8.16.3.2.3 E-UTRAN HD-FDD Inter-Frequency OTDOA Measurements 779

8.17 Measurements for E-UTRA – NR Dual Connectivity 779

8.17.1 Introduction 779

8.17.1.1 Measurement Gap Sharing 779

8.17.1A Intrafrequency Measurements 780

8.17.2 SFTD Measurements 780

8.17.2.1 Introduction 780

8.17.2.2 SFTD Measurement requirements 780

8.17.2.2.a SFTD Measurement requirements with CCA on target frequency 781

8.17.2.3 SFTD Measurement Reporting Delay 782

8.17.3 E-UTRA Inter-frequency Measurements when Configured with E-UTRA-NR Dual Connectivity Operation 782

8.17.3.1 Introduction 782

8.17.3.2 E-UTRAN FDD inter frequency measurements 783

8.17.3.2.1 E-UTRAN FDD inter frequency measurements when no DRX is used 783

8.17.3.2.2 E-UTRAN FDD inter frequency measurements when DRX is used 784

8.17.3.3 E-UTRAN TDD inter frequency measurements 786

8.17.3.3.1 E-UTRAN TDD inter frequency measurements when no DRX is used 786

8.17.3.3.2 E-UTRAN TDD inter frequency measurements when DRX is used 788

8.17.4 E-UTRA Inter-RAT NR Measurements when Configured with E-UTRA-NR Dual Connectivity Operation 790

8.17.4.1 E-UTRAN FDD – NR measurements when configured with E-UTRA-NR Dual connectivity 790

8.17.4.1.1 NR Inter-RAT cell identification 790

8.17.4.1.2 NR Inter-RAT measurement 792

8.17.4.1.3 NR Inter-RAT measurement reporting 792

8.17.4.2 E-UTRAN TDD – NR measurements when configured with E-UTRA-NR Dual connectivity 793

8.17.4A E-UTRA Inter-RAT NR Measurements when CCA is used when Configured with E-UTRA-NR Dual Connectivity Operation 793

8.17.4A.1 E-UTRAN FDD – NR measurements when configured with E-UTRA-NR Dual connectivity 793

8.17.4A.1.1 NR Inter-RAT cell identification 794

8.17.4A.1.2 NR Inter-RAT measurement 795

8.17.4A.1.3 NR Inter-RAT measurement reporting 796

8.17.4A.1.4 NR inter-RAT RSSI measurements 797

8.17.4A.1.5 NR inter-RAT channel occupancy measurements 797

8.17.4A.2 E-UTRAN TDD – NR measurements when configured with E-UTRA-NR Dual connectivity 798

8.17.5 E-UTRAN FDD – UTRAN FDD measurements when Configured with E-UTRA-NR Dual Connectivity 798

8.17.5.1 Introduction 798

8.17.5.2 E-UTRAN FDD – UTRAN FDD measurements when no DRX is used 798

8.17.5.2.1 Identification of a new UTRA FDD cell 798

8.17.5.2.2 Enhanced UTRA FDD cell identification requirements 798

8.17.5.2.3 UE UTRA FDD CPICH measurement capability 799

8.17.5.2.4 Periodic Reporting 799

8.17.5.2.5 Event Triggered Reporting 799

8.17.5.2.6 Event-triggered Periodic Reporting 800

8.17.5.3 E-UTRAN FDD – UTRAN FDD measurements when DRX is used 800

8.17.5.3.1 Periodic Reporting 801

8.17.5.3.2 Event Triggered Reporting 801

8.17.5.3.3 Event-triggered Periodic Reporting 802

8.17.6 E-UTRAN TDD – UTRAN FDD measurements when Configured with E-UTRA-NR Dual Connectivity 802

8.17.7 E-UTRAN FDD – UTRAN FDD measurements for SON when Configured with E-UTRA-NR Dual Connectivity 802

8.17.7.1 Introduction 802

8.17.7.2 Identification of a new UTRA FDD cell for SON 802

8.17.7.2.1 Requirements when no DRX is used 802

8.17.7.2.2 Requirements when DRX is used 803

8.17.7.2.3 Reporting Delay 803

8.17.8 E-UTRAN TDD – UTRAN FDD measurements for SON when Configured with E-UTRA-NR Dual Connectivity 804

8.17.9 E-UTRAN TDD – UTRAN TDD measurements when Configured with E-UTRA-NR Dual Connectivity 804

8.17.9.1 Introduction 804

8.17.9.2 E-UTRAN FDD – UTRAN TDD measurements when no DRX is used 804

8.17.9.2.1 Identification of a new UTRA FDD cell 804

8.17.9.2.2 Enhanced UTRA TDD cell identification requirements 804

8.17.9.2.3 UE UTRA TDD P-CCPCH RSCP measurement capability 805

8.17.9.2.4 Periodic Reporting 805

8.17.9.2.5 Event Triggered Reporting 805

8.17.9.2.6 Event-triggered Periodic Reporting 806

8.17.9.3 E-UTRAN TDD – UTRAN TDD measurements when DRX is used 806

8.17.9.3.1 Periodic Reporting 807

8.17.9.3.2 Event Triggered Reporting 807

8.17.9.3.3 Event-triggered Periodic Reporting 807

8.17.10 E-UTRAN FDD – UTRAN TDD measurements when Configured with E-UTRA-NR Dual Connectivity 808

8.17.11 E-UTRAN TDD – UTRAN TDD measurements for SON when Configured with E-UTRA-NR Dual Connectivity 808

8.17.11.1 Introduction 808

8.17.11.2 Identification of a new UTRA TDD cell for SON 808

8.17.11.2.1 Requirements when no DRX is used 808

8.17.11.2.2 Requirements when DRX is used 808

8.17.11.2.3 Reporting Delay 809

8.17.12 E-UTRAN FDD – UTRAN TDD measurements for SON when Configured with E-UTRA-NR Dual Connectivity 809

8.17.13 E-UTRAN FDD – GSM measurements when Configured with E-UTRA-NR Dual Connectivity 810

8.17.13.1 Introduction 810

8.17.13.2 E-UTRAN FDD – GSM measurements when no DRX is used 810

8.17.13.2.1 GSM carrier RSSI 810

8.17.13.2.2 BSIC verification 810

8.17.13.2.3 Enhanced BSIC verification 812

8.17.13.2.4 Periodic Reporting 812

8.17.13.2.5 Event Triggered Reporting 812

8.17.13.2.6 Event-triggered Periodic Reporting 813

8.17.13.3 E-UTRAN FDD – GSM measurements when DRX is used 813

8.17.13.3.1 GSM carrier RSSI 813

8.17.13.3.2 BSIC verification 813

8.17.13.3.3 Periodic Reporting 815

8.17.13.3.4 Event Triggered Reporting 815

8.17.13.3.5 Event-triggered Periodic Reporting 815

8.17.14 E-UTRAN TDD – GSM measurements when Configured with E-UTRA-NR Dual Connectivity 815

8.17.15 E-UTRAN Inter-Frequency RSTD measurements when configured with E-UTRA-NR Dual Connectivity 815

8.17.15.1 E-UTRAN FDD-FDD Inter-Frequency RSTD measurements when configured with E-UTRA-NR Dual Connectivity 815

8.17.15.1.1 RSTD Measurement Reporting Delay 816

8.17.15.2 E-UTRAN TDD-FDD Inter-Frequency RSTD measurements when configured with E-UTRA-NR Dual Connectivity 816

8.17.15.2.1 RSTD Measurement Reporting Delay 816

8.17.15.3 E-UTRAN TDD-TDD Inter-Frequency RSTD measurements when configured with E-UTRA-NR Dual Connectivity 816

8.17.15.3.1 RSTD Measurement Reporting Delay 817

8.17.15.4 E-UTRAN FDD-TDD Inter-Frequency RSTD measurements when configured with E-UTRA-NR Dual Connectivity 817

8.17.15.4.1 RSTD Measurement Reporting Delay 817

8.17.16 E-UTRAN intra-frequency measurement with autonomous gaps when configured with E-UTRA-NR Dual Connectivity 818

8.17.16.1 Introduction 818

8.17.16.2 E-UTRAN FDD intra frequency measurements with autonomous gaps 818

8.17.16.3 E-UTRAN TDD intra frequency measurements with autonomous gaps 818

8.17.17 E-UTRAN inter-frequency measurement with autonomous gaps when configured with E-UTRA-NR Dual Connectivity 818

8.17.17.1 Introduction 818

8.17.17.2 E-UTRAN FDD-FDD inter frequency measurements with autonomous gaps 818

8.17.17.3 E-UTRAN TDD-FDD inter frequency measurements using autonomous gaps 818

8.17.17.4 E-UTRAN TDD-TDD inter frequency measurements with autonomous gaps 818

8.17.17.5 E-UTRAN FDD-TDD inter frequency measurements using autonomous gaps 818

8.17.18 E-UTRA FDD - NR CGI measurements with autonomous gaps 818

8.17.19 E-UTRA TDD - NR CGI measurements with autonomous gaps 818

8.18 Measurements for non-BL/CE UE 818

8.18.1 Introduction 818

8.18.2 Requirements for non-BL/CE UE with CE Mode B 819

8.18.2.1 E-UTRAN intra frequency measurements 819

8.18.2.1.1 E-UTRAN FDD intra frequency measurements with autonomous gaps for non-BL/CE with CE Mode B 819

8.18.2.1.2 E-UTRAN intra frequency measurements with autonomous gaps for HD-FDD non-BL/CE with CE Mode B 819

8.18.2.1.3 E-UTRAN TDD intra frequency measurements with autonomous gaps for non-BL/CE with CE Mode B 820

8.19 Measurements for NR – E-UTRA Dual Connectivity 821

8.19.1 Introduction 821

8.19.2 Intra-frequency Measurements 821

8.19.3 Inter-frequency Measurements 821

8.19.4 Void 821

8.19.5 Intra-frequency E-CID Measurements 821

8.19.6 Intra-frequency measurements with autonomous gaps 822

8.19.6.1 Introduction 822

8.19.6.2 E-UTRAN FDD intra frequency measurements with autonomous gaps 822

8.19.6.3 E-UTRAN TDD intra frequency measurements with autonomous gaps 822

8.19.7 Inter-frequency measurements with autonomous gaps 822

8.19.7.1 Introduction 822

8.19.7.2 E-UTRAN FDD-FDD inter frequency measurements with autonomous gaps 822

8.19.7.3 E-UTRAN TDD-FDD inter frequency measurements with autonomous gaps 822

8.19.7.4 E-UTRAN TDD-TDD inter frequency measurements with autonomous gaps 822

8.19.7.5 E-UTRAN FDD-TDD inter frequency measurements with autonomous gaps 822

8.20 Inter-RAT NR Measurements for RedCap UE 822

8.20.1 Introduction 822

8.20.2 E-UTRAN FDD – NR measurements 822

8.20.2.1 Identification of a new NR cell 822

8.20.2.2 Periodic Reporting 826

8.20.2.3 Event Triggered Reporting 826

8.20.2.4 Event-triggered Periodic Reporting 826

8.20.3 E-UTRAN TDD – NR measurements 826

9 Measurements performance requirements for UE 827

9.1 E-UTRAN measurements 827

9.1.1 Introduction 827

9.1.2 Intra-frequency RSRP Accuracy Requirements 827

9.1.2.1 Absolute RSRP Accuracy 827

9.1.2.2 Relative Accuracy of RSRP 828

9.1.2.3 Absolute RSRP Accuracy under Time Domain Measurement Resource Restriction 829

9.1.2.4 Relative Accuracy of RSRP under Time Domain Measurement Resource Restriction 829

9.1.2.5 Absolute RSRP Accuracy under Time Domain Measurement Resource Restriction with CRS assistance information 830

9.1.2.6 Relative Accuracy of RSRP under Time Domain Measurement Resource Restriction with CRS assistance information 831

9.1.2.7 Absolute RSRP Accuracy for UE Category 1bis 832

9.1.2.8 Relative Accuracy of RSRP for UE Category 1bis 833

9.1.2A Intra-frequency RSRP Accuracy Requirements in High Doppler Conditions 834

9.1.2A.1 Absolute RSRP Accuracy in high Doppler conditions 834

9.1.2A.2 Relative Accuracy of RSRP in high Doppler conditions 834

9.1.2B Intra-frequency RSRP Accuracy requirements for CA Idle Mode Measurements 835

9.1.2B.1 Introduction 835

9.1.2B.2 Intra-frequency Absolute RSRP Accuracy for CA Idle Mode Measurements 835

9.1.3 Inter-frequency RSRP Accuracy Requirements 836

9.1.3.1 Absolute RSRP Accuracy 836

9.1.3.2 Relative Accuracy of RSRP 837

9.1.3.3 Absolute RSRP Accuracy for UE Category 1bis 838

9.1.3.4 Relative Accuracy of RSRP for UE Category 1bis 838

9.1.3A Inter-frequency RSRP Accuracy Requirements in High Doppler Conditions 839

9.1.3A.1 Absolute RSRP Accuracy in high Doppler conditions 839

9.1.3A.2 Relative Accuracy of RSRP in high Doppler conditions 840

9.1.3B Inter-frequency RSRP Accuracy requirements for CA Idle Mode Measurements 841

9.1.3B.1 Introduction 841

9.1.3B.2 Inter-frequency Absolute RSRP Accuracy for Overlapping Carrier 841

9.1.3B.3 Inter-frequency Absolute RSRP Accuracy for Overlapping and Non-overlapping Carrier 841

9.1.4 RSRP Measurement Report Mapping 842

9.1.5 Intra-frequency RSRQ Accuracy Requirements 842

9.1.5.1 Absolute RSRQ Accuracy 842

9.1.5.2 Absolute RSRQ Accuracy under Time Domain Measurement Resource Restriction 843

9.1.5.3 Absolute RSRQ Accuracy under Time Domain Measurement Resource Restriction with CRS assistance information 844

9.1.5.4 Absolute WB-RSRQ Accuracy 845

9.1.5.5 Absolute RSRQ Accuracy for UE Category 1bis 846

9.1.5A Intra-frequency RSRQ Accuracy Requirements in High Doppler Conditions 847

9.1.5A.1 Absolute RSRQ Accuracy in high Doppler conditions 847

9.1.5B Intra-frequency RSRQ Accuracy requirements for CA Idle Mode Measurements 847

9.1.5B.1 Introduction 847

9.1.5B.2 Intra-frequency Absolute RSRQ Accuracy for CA Idle Mode Measurements 847

9.1.6 Inter-frequency RSRQ Accuracy Requirements 848

9.1.6.1 Absolute RSRQ Accuracy 848

9.1.6.2 Relative Accuracy of RSRQ 849

9.1.6.3 Absolute WB-RSRQ Accuracy 850

9.1.6.4 Relative WB-RSRQ Accuracy 850

9.1.6.5 Absolute RSRQ Accuracy for UE Category 1bis 851

9.1.6.6 Relative Accuracy of RSRQ for UE Category 1bis 852

9.1.6A Inter-frequency RSRQ Accuracy Requirements in High Doppler Conditions 852

9.1.6A.1 Absolute RSRQ Accuracy in high Doppler conditions 852

9.1.6A.2 Relative Accuracy of RSRQ in high Doppler conditions 853

9.1.6B Inter-frequency absolute RSRQ Accuracy requirements for CA Idle Mode Measurements 854

9.1.6B.1 Introduction 854

9.1.6B.2 Inter-frequency Absolute RSRQ Accuracy for Overlapping Carrier 854

9.1.6B.3 Inter-frequency absolute RSRQ Accuracy for Overlapping and Non-overlapping Carrier 854

9.1.7 RSRQ Measurement Report Mapping 855

9.1.8 Power Headroom 855

9.1.8.1 Period 856

9.1.8.2 Reporting Delay 856

9.1.8.3 Void 856

9.1.8.4 Report Mapping 856

9.1.8A Power Headroom for UE category M1 for satellite access 856

9.1.8A.1 Period 857

9.1.8A.2 Reporting Delay 857

9.1.8A.3 Void 857

9.1.8A.4 Report Mapping 857

9.1.9 UE Rx – Tx time difference 857

9.1.9.1 Measurement Requirement 857

9.1.9.2 Measurement Report mapping 858

9.1.9.3 Measurement Requirement under Time Domain Measurement Resource Restriction 859

9.1.9.4 Measurement Requirement when Time Domain Measurement Resource Restriction Pattern is Configured with CRS Assistance Information 860

9.1.10 Reference Signal Time Difference (RSTD) 861

9.1.10.1 Intra-Frequency Accuracy Requirement 861

9.1.10.2 Inter-Frequency Accuracy Requirement 862

9.1.10.3 RSTD Measurement Report Mapping 864

9.1.10.4 Higher-Resolution RSTD Measurement Report Mapping 864

9.1.10.5 Intra-Frequency Accuracy Requirement for UE Category 1bis 865

9.1.10.6 Inter-Frequency Accuracy Requirement for UE Category 1bis 866

9.1.11 Carrier aggregation measurement accuracy 867

9.1.11.1 Primary component carrier accuracy requirement 868

9.1.11.2 Secondary component carrier accuracy requirement 868

9.1.11.3 Primary and secondary component carrier relative accuracy requirement 868

9.1.11.4 Secondary component carrier relative accuracy requirement 868

9.1.12 Reference Signal Time Difference (RSTD) Measurement Accuracy Requirements for Carrier Aggregation 868

9.1.13 Measurement accuracy for UE category 0 869

9.1.13.1 Intra-frequency Absolute RSRP Accuracy for UE category 0 869

9.1.13.2 Intra-frequency Relative Accuracy of RSRP for UE category 0 869

9.1.13.3 Intra-frequency Absolute RSRQ Accuracy for UE category 0 870

9.1.14 Accuracy requirements for Discovery Signal Measurements 871

9.1.14.1 Introduction 871

9.1.14.2 RSRP measurements in discovery signal occasions 871

9.1.14.3 CSI-RSRP measurements in discovery signal occasions 871

9.1.14.3.1 Intra-frequency CSI-RSRP measurements 871

9.1.14.3.1.1 Absolute CSI-RSRP measurement requirements 871

9.1.14.3.1.2 Relative CSI-RSRP measurement requirements 872

9.1.14.3.2 Inter-frequency CSI-RSRP measurements 873

9.1.14.3.2.1 Absolute CSI-RSRP measurement requirements 873

9.1.14.3.2.2 Relative CSI-RSRP measurement requirements 873

9.1.14.3.3 CSI-RSRP measurement report mapping 874

9.1.14.4 RSRQ measurements in discovery signal occasions 874

9.1.15 Discovery signal measurements accuracy for E-UTRAN carrier aggregation 874

9.1.15.1 Requirements for CRS based discovery signal measurements accuracy for E-UTRAN carrier aggregation 875

9.1.15.1.1 Primary component carrier accuracy requirement 875

9.1.15.1.2 Secondary component carrier accuracy requirement 875

9.1.15.1.3 Primary and secondary component carrier relative accuracy requirement 875

9.1.15.1.4 Secondary component carrier relative accuracy requirement 875

9.1.15.2 Requirements for CSI-RS based discovery signal measurements accuracy for E-UTRAN carrier aggregation 875

9.1.15.2.1 Primary component carrier accuracy requirement 875

9.1.15.2.2 Secondary component carrier accuracy requirement 875

9.1.15.2.3 Primary and secondary component carrier relative accuracy requirement 875

9.1.15.2.4 Secondary component carrier relative accuracy requirement 875

9.1.16 Accuracy requirements for RSRQ measurement on all OFDM symbols 876

9.1.17 RS-SINR Measurements 876

9.1.17.1 Measurement Report Mapping 876

9.1.17.2 Intra-frequency RS-SINR Measurement Accuracy Requirements 877

9.1.17.2.1 Absolute RS-SINR Measurement Accuracy Requirements 877

9.1.17.3 Inter-frequency RS-SINR Measurement Accuracy Requirements 877

9.1.17.3.1 Absolute RS-SINR Measurement Accuracy Requirements 877

9.1.17.3.2 Relative RS-SINR Measurement Accuracy Requirements 878

9.1.18 Accuracy Requirements for Measurements under Operation with Frame Structure 3 879

9.1.18.1 Introduction 879

9.1.18.2 RSRP measurements 879

9.1.18.2.1 RSRP measurement report mapping 879

9.1.18.2.2 Inter-frequency absolute RSRP measurement accuracy requirements 879

9.1.18.2.3 Inter-frequency relative RSRP measurement accuracy requirements 880

9.1.18.2.4 Intra-frequency absolute RSRP measurement accuracy requirements 880

9.1.18.2.5 Intra-frequency relative RSRP measurement accuracy requirements 881

9.1.18.3 RSRQ measurements 881

9.1.18.3.1 RSRQ measurement report mapping 881

9.1.18.3.2 Inter-frequency absolute RSRQ measurement accuracy requirements 881

9.1.18.3.3 Inter-frequency relative RSRQ measurement accuracy requirements 882

9.1.18.3.4 Intra-frequency absolute RSRQ measurement accuracy requirements 882

9.1.18.4 CSI-RSRP measurements 883

9.1.18.4.1 CSI-RSRP measurement report mapping 883

9.1.18.4.2 Inter-frequency absolute CSI-RSRP measurement accuracy requirements 883

9.1.18.4.3 Inter-frequency relative CSI-RSRP measurement accuracy requirements 883

9.1.18.4.4 Intra-frequency absolute CSI-RSRP measurement accuracy requirements 884

9.1.18.4.5 Intra-frequency relative CSI-RSRP measurement accuracy requirements 884

9.1.18.5 RSSI measurements 885

9.1.18.5.1 RSSI measurement report mapping 885

9.1.18.5.2 Intra-frequency absolute RSSI measurement accuracy requirements 885

9.1.18.5.3 Inter-frequency absolute RSSI measurement accuracy requirements 886

9.1.18.6 Channel occupancy measurements 886

9.1.18.6.1 Intra-frequency channel occupancy measurement accuracy requirements 886

9.1.18.6.2 Inter-frequency channel occupancy measurement accuracy requirements 886

9.1.19 Accuracy Requirements for Carrier Aggregation for Measurements under Operation with Frame Structure 3 887

9.1.19.1 Introduction 887

9.1.19.2 Accuracy requirements for measurements on SCC 887

9.1.19.3 Relative accuracy requirements for measurements on different SCCs 887

9.1.19.4 Relative accuracy requirements for measurements on SCC and PCC 887

9.1.20 SFN and Subframe Time Difference (SSTD) 888

9.1.20.1 SSTD Accuracy Requirement 888

9.1.20.2 SSTD Measurement Report Mapping 888

9.1.21 Measurement accuracy for UE category M1 889

9.1.21.1 Intra-frequency Absolute RSRP Accuracy for UE category M1 with CE mode A 889

9.1.21.2 Intra-frequency Relative Accuracy of RSRP for UE category M1 with CE mode A 891

9.1.21.3 Intra-frequency Absolute RSRP Accuracy for UE category M1 with CE mode B 892

9.1.21.4 Intra-frequency Relative Accuracy of RSRP for UE category M1 with CE mode B 894

9.1.21.5 RSRP Measurement Report Mapping 895

9.1.21.6 Intra-frequency Absolute Accuracy of RSRQ for UE category M1 with CE mode A 895

9.1.21.7 Intra-frequency Absolute Accuracy of RSRQ for UE category M1 with CE mode B 896

9.1.21.8 RSRQ Measurement Report Mapping 897

9.1.21.9 Inter-frequency Absolute RSRP Accuracy for UE category M1 with CE mode A 897

9.1.21.10 Inter-frequency Relative Accuracy of RSRP for UE category M1 with CE mode A 898

9.1.21.11 Inter-frequency Absolute RSRP Accuracy for UE category M1 with CE mode B 899

9.1.21.12 Inter-frequency Relative Accuracy of RSRP for UE category M1 with CE mode B 900

9.1.21.13  Inter-frequency Absolute Accuracy of RSRQ for UE category M1 in CE mode A 901

9.1.21.14 Inter-frequency Relative Accuracy of RSRQ for UE category M1 in CE mode A 902

9.1.21.15  Inter-frequency Absolute Accuracy of RSRQ for UE category M1 in CE mode B 903

9.1.21.16 Inter-frequency Relative Accuracy of RSRQ for UE category M1 in CE mode B 904

9.1.21.17 Inter-Frequency RSTD Accuracy Requirement for UE catergory M1 in CE mode A 905

9.1.21.18 Inter-Frequency RSTD Accuracy Requirement for UE catergory M1 in CE mode B 906

9.1.21.19 UE RX-TX time difference Accuracy Requirement for Cat-M1 907

9.1.21.20 Intra-Frequency RSTD Accuracy Requirement for UE catergory M1 in CE mode A 908

9.1.21.21 Intra-Frequency RSTD Accuracy Requirement for UE catergory M1 in CE mode B 911

9.1.21.22 Downlink Channel Report Mapping for UE Category M1 914

9.1.21.23 Downlink Channel Quality Measurement Accuracy for UE Category M1 with CE Mode A 914

9.1.21.24 Downlink Channel Quality Measurement Accuracy for UE Category M1 with CE Mode B 917

9.1.21A Measurement accuracy for UE category M1 for satellite access 918

9.1.21A.1 Intra-frequency Absolute RSRP Accuracy for UE category M1 with CE mode A 919

9.1.21A.2 Intra-frequency Relative Accuracy of RSRP for UE category M1 with CE mode A 920

9.1.21A.3 Intra-frequency Absolute RSRP Accuracy for UE category M1 with CE mode B 921

9.1.21A.4 Intra-frequency Relative Accuracy of RSRP for UE category M1 with CE mode B 923

9.1.21A.5 RSRP Measurement Report Mapping 924

9.1.21A.6 Intra-frequency Absolute Accuracy of RSRQ for UE category M1 with CE mode A 924

9.1.21A.7 Intra-frequency Absolute Accuracy of RSRQ for UE category M1 with CE mode B 925

9.1.21A.8 RSRQ Measurement Report Mapping 926

9.1.21A.9 Inter-frequency Absolute RSRP Accuracy for UE category M1 with CE mode A 926

9.1.21A.10 Inter-frequency Relative Accuracy of RSRP for UE category M1 with CE mode A 927

9.1.21A.11 Inter-frequency Absolute RSRP Accuracy for UE category M1 with CE mode B 928

9.1.21A.12 Inter-frequency Relative Accuracy of RSRP for UE category M1 with CE mode B 929

9.1.21A.13 Inter-frequency Absolute Accuracy of RSRQ for UE category M1 in CE mode A 930

9.1.21A.14 Inter-frequency Relative Accuracy of RSRQ for UE category M1 in CE mode A 931

9.1.21A.15 Inter-frequency Absolute Accuracy of RSRQ for UE category M1 in CE mode B 932

9.1.21A.16 Inter-frequency Relative Accuracy of RSRQ for UE category M1 in CE mode B 933

9.1.21A.17 Downlink Channel Report Mapping for UE Category M1 934

9.1.21A.18 Downlink Channel Quality Measurement Accuracy for UE Category M1 with CE Mode A 934

9.1.21A.19 Downlink Channel Quality Measurement Accuracy for UE Category M1 with CE Mode B 936

9.1.22 Measurement accuracy for UE Category NB1 937

9.1.22.1 Intra-frequency Absolute NRSRP Accuracy for UE Category NB1 937

9.1.22.2 Void 938

9.1.22.3 Intra-frequency Absolute NRSRQ Accuracy for UE Category NB1 938

9.1.22.4 Void 939

9.1.22.5 Inter-frequency Absolute NRSRP Accuracy for UE Category NB1 939

9.1.22.6 Void 940

9.1.22.7 Inter-frequency Absolute NRSRQ Accuracy for UE Category NB1 940

9.1.22.8 Void 941

9.1.22.9 NRSRP Measurement Report Mapping 941

9.1.22.10 Intra-Frequency RSTD Accuracy Requirement for NB1 for normal coverage 941

9.1.22.11 Inter-Frequency RSTD Accuracy Requirement for NB1 for normal coverage 942

9.1.22.12 Intra-Frequency RSTD Accuracy Requirement for NB1 for enhanced coverage 943

9.1.22.13 Inter-Frequency RSTD Accuracy Requirement for NB1 for enhanced coverage 944

9.1.22.14 NRSRQ Measurement Report Mapping 945

9.1.22.15 MSG3-based Measurement Report Mapping for UE Category NB1 946

9.1.22.16 Downlink Channel Quality Measurement Accuracy for UE Category NB1 946

9.1.22.17 Channel quality reporting for UE Category NB2 with 16-QAM 947

9.1.22A Measurement accuracy for UE Category NB1 for satellite access 947

9.1.22A.1 Intra-frequency Absolute NRSRP Accuracy for UE Category NB1 947

9.1.22A.2 Intra-frequency Absolute NRSRQ Accuracy for UE Category NB1 948

9.1.22A.3 Inter-frequency Absolute NRSRP Accuracy for UE Category NB1 950

9.1.22A.4 Inter-frequency Absolute NRSRQ Accuracy for UE Category NB1 951

9.1.22A.5 NRSRP Measurement Report Mapping 952

9.1.22A.6 NRSRQ Measurement Report Mapping 952

9.1.22A.7 MSG3-based Measurement Report Mapping for UE Category NB1 952

9.1.22A.8 Downlink Channel Quality Measurement Accuracy for UE Category NB1 952

9.1.23 Power Headroom for UE Category NB1 953

9.1.23.1 Period 953

9.1.23.2 Reporting Delay 953

9.1.23.3 Report Mapping for UE Category NB1 954

9.1.23.3.1 Void 955

9.1.23.3.2 Void 955

9.1.23.4 Report Mapping for UE Category NB1 for UE Power Class 6 955

9.1.23A Power Headroom for UE Category NB1 for Satellite Access 956

9.1.23A.1 Period 956

9.1.23A.2 Reporting Delay 956

9.1.23A.3 Report Mapping for UE Category NB1 for Satellite Access 957

9.1.23A.3.1 Void 957

9.1.23A.3.2 Void 957

9.1.23A.4 Report Mapping for UE Category NB1 for UE Power Class 6 for Satellite Access 957

9.1.24 Void 957

9.1.25 Measurement accuracy for UE category M2 957

9.1.25.1 Inter-Frequency RSTD Accuracy Requirement for UE catergory M2 in CE mode A 957

9.1.25.2 Inter-Frequency RSTD Accuracy Requirement for UE catergory M2 in CE mode B 958

9.1.25.3 UE RX-TX time difference Accuracy Requirement for Cat-M2 959

9.1.25.4 Intra-Frequency RSTD Accuracy Requirement for UE catergory M2 in CE mode A 960

9.1.25.5 Intra-Frequency RSTD Accuracy Requirement for UE catergory M2 in CE mode B 962

9.1.26 Measurement Accuracy for non-BL CE UE 963

9.1.26.1 Intra-frequency Absolute Accuracy of RSRP for non-BL CE UE in CE mode A 964

9.1.26.2 Intra-frequency Relative Accuracy of RSRP for non-BL CE UE in CE mode A 966

9.1.26.3 Intra-frequency Absolute Accuracy of RSRP for non-BL CE UE in CE mode B 966

9.1.26.4 Intra-frequency Relative Accuracy of RSRP for non-BL CE UE in CE mode B 968

9.1.26.5 RSRP Measurement Report Mapping 969

9.1.26.6 Intra-frequency Absolute Accuracy of RSRQ for non-BL CE UE in CE mode A 969

9.1.26.7 Intra-frequency Absolute Accuracy of RSRQ for non-BL CE UE in CE mode B 969

9.1.26.8 RSRQ Measurement Report Mapping 970

9.1.26.9 Inter-frequency Absolute Accuracy of RSRP for non-BL CE UE in CE mode A 970

9.1.26.10 Inter-frequency Relative Accuracy of RSRP for non-BL CE UE in CE mode A 971

9.1.26.11 Inter-frequency Absolute Accuracy of RSRP for non-BL CE UE in CE mode B 972

9.1.26.12 Inter-frequency Relative Accuracy of RSRP for non-BL CE UE in CE mode B 973

9.1.26.13 Inter-frequency Absolute Accuracy of RSRQ for non-BL CE UE in CE mode A 974

9.1.26.14 Inter-frequency Relative Accuracy of RSRQ for non-BL CE UE in CE mode A 974

9.1.26.15 Inter-frequency Absolute Accuracy of RSRQ for non-BL CE UE in CE mode B 974

9.1.26.16 Inter-frequency Relative Accuracy of RSRQ for non-BL CE UE in CE mode B 975

9.1.27 SFN and frame Timing Difference (SFTD) 976

9.1.27.1 SFTD Accuracy Requirement 976

9.1.28 SFN and Frame Timing Difference (SFTD) under CCA 978

9.1.28.1 SFTD Accuracy Requirement under CCA 978

9.2 UTRAN FDD Measurements 979

9.2.1 UTRAN FDD CPICH RSCP 979

9.2.2 Void 980

9.2.3 UTRAN FDD CPICH Ec/No 980

9.3 UTRAN TDD Measurements 980

9.3.1 UTRAN TDD P-CCPCH RSCP 981

9.3.2 Void 981

9.3.3 Void 981

9.4 GSM Measurements 981

9.4.1 GSM carrier RSSI 981

9.5 CDMA2000 1x RTT Measurements 981

9.5.1 CDMA2000 1x RTT Pilot Strength 981

9.6 PCMAX,c 982

9.6.1 Report Mapping 982

9.6.2  Estimation Period 982

9.6.3 Reporting Delay 982

9.7 IEEE802.11 Measurements 982

9.7.1 WLAN RSSI 982

9.7.2 WLAN RSSI Measurement Report Mapping 982

9.8 MBSFN Measurements 983

9.8.1 Introduction 983

9.8.2 MBSFN RSRP 983

9.8.2.1 Absolute MBSFN RSRP measurement accuracy requirements 983

9.8.2.2 MBSFN RSRP measurement report mapping 984

9.8.2.3 MBSFN RSRP measurement report mapping for 7.5 kHz subcarrier spacing 984

9.8.2.4 MBSFN RSRP measurement report mapping for 1.25 kHz subcarrier spacing 985

9.8.2.5 MBSFN RSRP measurement report mapping for 2.5 kHz subcarrier spacing 985

9.8.2.6 MBSFN RSRP measurement report mapping for 370.37Hz subcarrier spacing 985

9.8.3 MBSFN RSRQ 986

9.8.3.1 Absolute MBSFN RSRQ measurement accuracy requirements 986

9.8.3.2 MBSFN RSRQ measurement report mapping 986

9.8.3.3 MBSFN RSRQ measurement report mapping for 7.5 kHz subcarrier spacing 987

9.8.3.4 MBSFN RSRQ measurement report mapping for 1.25 kHz subcarrier spacing 987

9.8.3.5 MBSFN RSRQ measurement report mapping for 2.5 kHz subcarrier spacing 987

9.8.3.6 MBSFN RSRQ measurement report mapping for 370.37 kHz subcarrier spacing 988

9.8.4 MCH BLER 988

9.8.4.1 Measurement report mapping for MCH BLER 988

9.8.4.2 Measurement report mapping for MCH Block Number 989

9.9 ProSe Measurements 990

9.9.1 Introduction 990

9.9.2 Intra-Frequency S-RSRP Measurement Accuracy Requirements 990

9.9.2.1 Absolute S-RSRP Accuracy 990

9.9.2.2 Relative Accuracy of S-RSRP 991

9.9.3 Intra-Frequency SD-RSRP Measurement Accuracy Requirements 992

9.9.3.1 Absolute SD-RSRP Accuracy 992

9.9.3.2 Relative Accuracy of SD-RSRP 992

9.10 V2X Measurements 993

9.10.1 Introduction 993

9.10.2 Intra-Frequency S-RSRP Measurement Accuracy Requirements 993

9.10.2.1 Absolute S-RSRP Accuracy 993

9.10.2.2 Relative Accuracy of S-RSRP 994

9.10.3 PSSCH-RSRP Measurement Accuracy Requirements 994

9.10.3.1 Intra-frequency Absolute PSSCH-RSRP Accuracy 994

9.10.4 S-RSSI Measurement Accuracy Requirements 995

9.10.4.1 Intra-frequency absolute S-RSSI measurement accuracy requirements 995

9.10.4.2 Intra-frequency relative S-RSSI measurement accuracy requirements 995

9.11 NR Measurements 996

9.11.1 NR SS-RSRP Measurements 996

9.11.1A NR SS-RSRP Measurements for DC Idle Mode Measurements 996

9.11.2 NR SS-RSRQ Measurements 997

9.11.2A NR SS-RSRQ Measurements for DC Idle Mode Measurements 997

9.11.3 NR SS-SINR Measurements 997

9.11.4 NR SS-RSRP Measurements under CCA 998

9.11.5 NR SS-RSRQ Measurements under CCA 998

9.11.6 NR SS-SINR Measurements under CCA 998

9.11.7 NR RSSI Measurements under CCA 998

9.11.8 NR Channel Occupancy Measurements under CCA 999

10 Measurements Performance Requirements for E-UTRAN 999

10.1 Received Interference Power 999

10.1.1 Absolute accuracy requirement 999

10.1.2 Relative accuracy requirement 999

10.1.3 Received Interference Power measurement report mapping 1000

10.2 Angle of Arrival (AOA) 1000

10.2.1 Range/mapping 1000

10.3 Timing Advance (TADV) 1000

10.3.1 Report mapping 1000

11 ProSe Requirements in Any Cell Selection state 1001

11.1 Introduction 1001

11.2 UE Transmit Timing for ProSe in Any Cell Selection State 1001

11.2.1 Introduction 1001

11.2.2 ProSe UE transmission timing 1001

11.3 Initiation/Cease of SLSS Transmissions 1002

11.3.1 Introduction 1002

11.3.2 Requirements 1002

11.4 Measurements for ProSe in Any Cell Selection State 1002

11.4.1 Introduction 1002

11.4.2 Requirements 1002

11.4.2.1 E-UTRA FDD 1002

11.4.2.2 E-UTRA TDD 1003

11.5 Selection / Reselection of ProSe Synchronization Reference 1003

11.5.1 Introduction 1003

11.5.2 Selection/Reselection to intra-frequency SyncRef UE 1003

11.5.2.1 Introduction 1003

11.5.2.2 Requirements 1003

11.6 Void 1004

11.7 Selection / Reselection of ProSe relay UE 1004

11.7.1 Introduction 1004

11.7.2 Selection / Reselection of intra-frequency ProSe relay UE 1004

12 V2V Sidelink Communication Requirements for V2V Operation on Dedicated V2V Carrier 1004

12.1 Introduction 1004

12.2 Transmit Timing 1005

12.2.1 GNSS as timing reference 1005

12.3 Interruption 1005

12.4 Reliability of GNSS signal 1005

13 V2X Requirements 1005

13.1 Introduction 1005

13.2 UE Transmit Timing 1006

13.2.1 Introduction 1006

13.2.2 GNSS as synchronization reference source 1006

13.2.3 Serving cell/PCell as synchronization reference source 1006

13.2.4 SyncRef UE as synchronization reference source 1006

13.3 Initiation/Cease of SLSS Transmissions 1006

13.3.1 Introduction 1006

13.3.1.1 Initiation/Cease of SLSS transmissions with Serving cell / PCell as synchronization reference source 1006

13.3.1.2 Initiation/Cease of SLSS transmissions with GNSS as synchronization reference source 1007

13.3.1.3 Initiation/Cease of SLSS transmissions with SyncRef UE as synchronization reference source 1007

13.4 Selection / Reselection of V2X Synchronization Reference Source 1008

13.5 Autonomous Resource Selection/Reselection measurements 1009

13.5.1 Introduction 1009

13.5.2 PSSCH-RSRP measurements 1009

13.5.3 S-RSSI measurements 1009

13.6 Congestion Control measurements 1009

13.7 Interruption 1009

13.7.1 Interruptions to WAN due to V2X Sidelink Communication 1009

13.7.2 V2X Sidelink Communication Dropping due to synchronization reference source change 1009

13.7.3 Interruptions to WAN due to V2X Carrier Aggregation 1010

13.7.4 Interruptions to WAN due to NR V2X sidelink communication 1010

13.8 Reliability of GNSS signal 1010

13.9 Component Carrier Addition and Release Delay for V2X Sidelink Carrier Aggregation 1011

13.10 Selection / Reselection of V2X Synchronization Reference Source for V2X Carrier Aggregation 1011

Annex A (normative): Test Cases 1012

A.1 Purpose of annex 1012

A.2 Requirement classification for statistical testing 1012

A.2.1 Types of requirements in TS 36.133 1012

A.2.1.1 Time and delay requirements on UE higher layer actions 1012

A.2.1.2 Measurements of power levels, relative powers and time 1012

A.2.1.3 Implementation requirements 1013

A.2.1.4 Physical layer timing requirements 1013

A.3 RRM test configurations 1014

A.3.1 Reference Measurement Channels 1014

A.3.1.1 PDSCH 1014

A.3.1.1.1 FDD 1014

A.3.1.1.2 TDD 1019

A.3.1.1.3 FDD for UE category 0 1022

A.3.1.1.4 HD-FDD for UE category 0 1023

A.3.1.1.5 TDD for UE category 0 1024

A.3.1.1.6 Frame Structure 3 1025

A.3.1.2 PCFICH/PDCCH/PHICH 1026

A.3.1.2.1 FDD 1026

A.3.1.2.2 TDD 1026

A.3.1.2.3 HD-FDD for UE category 0 1027

A.3.1.2.4 FS 3 1027

A.3.1.3 MPDCCH Reference Channels for Cat-M1 UEs 1027

A.3.1.3.1 FDD in CEModeA 1028

A.3.1.3.2 HD-FDD in CEModeA 1028

A.3.1.3.3 TDD in CEModeA 1029

A.3.1.3.4 FDD in CEModeB 1029

A.3.1.3.5 HD-FDD in CEModeB 1030

A.3.1.3.6 TDD in CEModeB 1030

A.3.1.4 PDSCH Reference Channel for Cat-M1 UEs 1031

A.3.1.4.1 FDD in CEModeA 1031

A.3.1.4.2 HD-FDD in CEModeA 1032

A.3.1.4.3 TDD in CEModeA 1033

A.3.1.4.4 FDD in CEModeB 1034

A.3.1.4.5 HD-FDD in CEModeB 1035

A.3.1.4.6 TDD in CEModeB 1035

A.3.1.5 NPDSCH Reference Channel for UE category NB1 1036

A.3.1.5.1 HD-FDD in-band operation 1036

A.3.1.5.2 Void 1037

A.3.1.5.3 HD-FDD standalone operation 1037

A.3.1.5.4 Void 1038

A.3.1.5.5 HD-FDD guard band operation 1038

A.3.1.5.6 Void 1039

A.3.1.5.7 TDD in-band operation 1039

A.3.1.5.8 TDD standalone operation 1039

A.3.1.5.9 TDD guard band operation 1040

A.3.1.5.10 NTN-TDD standalone operation 1040

A.3.1.6 NPDCCH Reference Channel for UE category NB1 1041

A.3.1.6.1 In-band operation 1041

A.3.1.6.2 Void 1042

A.3.1.6.3 Standalone operation 1042

A.3.1.6.4 Void 1042

A.3.1.6.5 Guard band operation 1042

A.3.1.6.6 Void 1043

A.3.2 OFDMA Channel Noise Generator (OCNG) 1043

A.3.2.1 OCNG Patterns for FDD 1043

A.3.2.1.1 OCNG FDD pattern 1: outer resource blocks allocation in 10 MHz 1043

A.3.2.1.2 OCNG FDD pattern 2: full bandwidth allocation in 10 MHz 1044

A.3.2.1.3 OCNG FDD pattern 3: outer resource blocks allocation in 1.4 MHz 1045

A.3.2.1.4 OCNG FDD pattern 4: full bandwidth allocation in 1.4 MHz 1045

A.3.2.1.5 OCNG FDD pattern 5: outer resource blocks allocation in 10 MHz (without MBSFN) 1046

A.3.2.1.6 OCNG FDD pattern 6: full bandwidth allocation in 10 MHz (without MBSFN) 1047

A.3.2.1.7 OCNG FDD pattern 7: full bandwidth allocation in 1.4 MHz (without MBSFN) 1047

A.3.2.1.8 OCNG FDD pattern 8: outer resource blocks allocation in 10 MHz for MBSFN ABS 1047

A.3.2.1.9 OCNG FDD pattern 9: full bandwidth allocation in 10 MHz for MBSFN ABS 1048

A.3.2.1.10 OCNG FDD pattern 10: outer resource blocks allocation in 10 MHz with user data in every subframe (without MBSFN) 1049

A.3.2.1.11 OCNG FDD pattern 11: outer resource blocks allocation in 20 MHz 1049

A.3.2.1.12 OCNG FDD pattern 12: full bandwidth allocation in 20 MHz 1050

A.3.2.1.13 OCNG FDD pattern 13: outer resource blocks allocation in 20 MHz (without MBSFN) 1050

A.3.2.1.14 OCNG FDD pattern 14: full bandwidth allocation in 20 MHz (without MBSFN) 1051

A.3.2.1.15 OCNG FDD pattern 15: outer resource blocks allocation in 5 MHz 1051

A.3.2.1.16 OCNG FDD pattern 16: full bandwidth allocation in 5 MHz 1052

A.3.2.1.17 OCNG FDD pattern 17: outer resource blocks allocation in 20 MHz with user data in every subframe (without MBSFN) 1052

A.3.2.1.18 OCNG FDD pattern 18: outer resource blocks allocation in 5 MHz (without MBSFN) 1053

A.3.2.1.19 OCNG FDD pattern 19: full bandwidth allocation in 5 MHz (without MBSFN) 1053

A.3.2.1.20 OCNG FDD pattern 20: outer resource blocks allocation in 5 MHz with user data in every subframe (without MBSFN) 1054

A.3.2.1.21 OCNG FDD pattern 21: Generic resource blocks allocation (without MBSFN) 1054

A.3.2.1.22 OCNG FDD pattern 22: Generic resource blocks allocation in 5MHz (without MBSFN) 1055

A.3.2.2 OCNG Patterns for TDD 1055

A.3.2.2.1 OCNG TDD pattern 1: outer resource blocks allocation in 10 MHz 1056

A.3.2.2.2 OCNG TDD pattern 2: full bandwidth allocation in 10 MHz 1056

A.3.2.2.3 OCNG TDD pattern 3: outer resource blocks allocation in 1.4 MHz 1057

A.3.2.2.4 OCNG TDD pattern 4: full bandwidth allocation in 1.4 MHz 1057

A.3.2.2.5 OCNG TDD pattern 5: outer resource blocks allocation in 10 MHz for MBSFN ABS 1058

A.3.2.2.6 OCNG TDD pattern 6: full bandwidth allocation in 10 MHz for MBSFN ABS 1059

A.3.2.2.7 OCNG TDD pattern 7: outer resource blocks allocation in 20 MHz 1060

A.3.2.2.8 OCNG TDD pattern 8: full bandwidth allocation in 20 MHz 1061

A.3.2.2.9 OCNG TDD pattern 9: outer resource blocks allocation in 5 MHz 1061

A.3.2.2.10 OCNG TDD pattern 10: full bandwidth allocation in 5 MHz 1062

A.3.2.2.11 OCNG TDD pattern 11: Generic resource blocks allocation (without MBSFN) 1063

A.3.2.3 OCNG Patterns for Narrowband IoT 1063

A.3.2.3.1 Narrowband IoT OCNG FDD pattern 1: In-band NB-IoT in 10 MHz EUTRAN cell 1065

A.3.2.3.2 Narrowband IoT OCNG FDD pattern 2: guard band NB-IoT in 10 MHz EUTRAN cell 1066

A.3.2.3.3 Narrowband IoT OCNG FDD pattern 3: standalone NB-IoT 1066

A.3.2.3.4 Narrowband IoT OCNG FDD pattern 4: In-band NB-IoT in 5 MHz EUTRAN cell 1067

A.3.2.3.5 Narrowband IoT OCNG FDD pattern 5: guard band NB-IoT in 5 MHz EUTRAN cell 1068

A.3.2.3.6 Narrowband IoT OCNG TDD pattern 1: In-band NB-IoT in 10 MHz EUTRAN cell 1069

A.3.2.3.7 Narrowband IoT OCNG TDD pattern 2: guard band NB-IoT in 10 MHz EUTRAN cell 1071

A.3.2.3.8 Narrowband IoT OCNG TDD pattern 3: standalone NB-IoT 1071

A.3.2.3.9 Narrowband IoT OCNG FDD pattern 6: In-band NB-IoT in 5 MHz NTN NR cell 1072

A.3.2.3.10 Narrowband IoT OCNG NTN TDD pattern 4: standalone NB-IoT 1073

A.3.2.4 OCNG Patterns for V2X sidelink 1074

A.3.2.4.1 V2X sidelink OCNG TDD pattern 1: outer resource blocks allocation in 10 MHz 1074

A.3.2.4.2 V2X sidelink OCNG TDD pattern 2: outer resource blocks allocation in 10 MHz 1075

A.3.3 Reference DRX Configurations 1075

A.3.4 ABS Transmission Configurations 1076

A.3.4.1 Non-MBSFN ABS Transmission Configurations 1076

A.3.4.1.1 Non-MBSFN ABS Transmission, 1x2 antenna with PBCH 1076

A.3.4.1.2 Non-MBSFN ABS Transmission, 2x2 antenna without PBCH 1076

A.3.4.2 MBSFN ABS Transmission Configurations 1077

A.3.4.2.1 MBSFN ABS Transmission, 1x2 antenna 1077

A.3.4.2.2 MBSFN ABS Transmission, 2x2 antenna 1078

A.3.5 Impact of Reference Sensitivity Degradation with Carrier Aggregation on Test Cases 1078

A.3.5.1 Impact of Reference Sensitivity Degradation due to Insertion Loss 1078

A.3.6 Carrier Aggregation Test Cases with Different Channel Bandwidth Combinations 1079

A.3.6.1 Introduction 1079

A.3.7 Test Cases with Different Channel Bandwidths 1079

A.3.7.1 Introduction 1079

A.3.7.2 Principle of testing 1079

A.3.8 Antenna Configuration 1079

A.3.8.1 Antenna connection for 4 Rx capable UEs 1079

A.3.8.1.1 Introduction 1079

A.3.8.1.2 Principle of testing 1079

A.3.8.1.2.1 Single carrier tests 1079

A.3.8.1.2.2 Carrier aggregation and Dual connectivity tests 1080

A.3.8.1.2.3 Antenna connection for bands where 2RX is supported 1081

A.3.8.1.2.4 Antenna connection for bands where 4RX is supported 1081

A.3.8.2 Antenna connection for 8 Rx capable UEs 1081

A.3.8.2.1 Introduction 1081

A.3.8.2.2 Principle of testing 1081

A.3.8.2.2.1 Single carrier tests 1081

A.3.8.2.2.2 Carrier aggregation and Dual connectivity tests 1082

A.3.8.2.2.3 Antenna connection for bands where 2RX is supported 1082

A.3.8.2.2.4 Antenna connection for bands where 4RX is supported 1082

A.3.8.2.2.5 Antenna connection for bands where 8RX is supported 1082

A.3.9 Carrier Aggregation Test Cases with Different Duplex Modes 1082

A.3.9.1 Introduction 1082

A.3.9.2 Principle of testing 1082

A.3.10 Carrier Aggregation Test Cases with Different CA Configurations 1083

A.3.10.1 Introduction 1083

A.3.10.2 Principle of testing 1083

A.3.11 Test Cases for Synchronous and Asynchronous Dual Connectivity 1083

A.3.11.1 Introduction 1083

A.3.11.2 Principle of Testing 1083

A.3.12 Proximity-based Services 1083

A.3.12.1 Introduction 1083

A.3.12.2 Reference DRX configurations for ProSe tests 1083

A.3.12.3 Test Cases with Different Channel Bandwidths 1084

A.3.12.3.1 Introduction 1084

A.3.12.3.2 Principle of testing 1084

A.3.12.4 Reference resource pool configurations for ProSe Direct Discovery 1084

A.3.12.5 Reference resource pool configurations for ProSe Direct Communication 1091

A.3.12.6 Reference Measurement Channels for ProSe Direct Discovery 1094

A.3.12.6.1 FDD 1094

A.3.12.7 Reference measurement channels for ProSe Direct Communication 1094

A.3.12.7.1 FDD 1094

A.3.12.8 ProSe Receive Traffic Generator 1095

A.3.12.8.1 ProSe Direct Communication Receive Traffic Generator for FDD 1095

A.3.12.8.2 ProSe Direct Discovery Receive Traffic Generator for FDD 1095

A.3.13 Time Offset between Cells 1096

A.3.13.1 Introduction 1096

A.3.13.2 Definition 1096

A.3.14 Carrier Aggregation under operation with Frame Structure 3 Test Cases with Different Duplex Modes 1096

A.3.14.1 Introduction 1096

A.3.14.2 Principle of testing 1096

A.3.15 Dual connectivity test cases with different combination of duplex mode 1096

A.3.15.1 Introduction 1096

A.3.15.2 Principle of testing 1096

A.3.16 Reference PRACH Configurations 1097

A.3.17 Listen before talk model 1097

A.3.17.1 Introduction 1097

A.3.17.2 Definition 1097

A.3.18 Reference NPRACH Configurations 1098

A.3.19 Dual connectivity test cases with different bandwidth combinations 1100

A.3.19.1 Introduction 1100

A.3.19.2 Principle of testing 1100

A.3.20 Category M1 UE Test Cases 1101

A.3.20.1 Introduction 1101

A.3.20.2 Principle of Cat-M1 UE Testing 1101

A.3.20.3 Principle of Cat-M1 UE testing for inter-frequency RSTD measurement period requirements with measurement gaps 1102

A.3.21 V2V Sidelink Communication on Dedicated V2V Carrier 1103

A.3.21.1 Introduction 1103

A.3.21.2 Reference resource pool configurations for V2V Sidelink Communication 1103

A.3.21.3 Reference measurement channels for V2V Sidelink Communication 1104

A.3.22 Category 1bis UE Test Cases 1105

A.3.22.1 Introduction 1105

A.3.22.2 Principle of Category 1bis UE Testing 1105

A.3.23 Category NB2 UE Test Cases 1109

A.3.23.1 Introduction 1109

A.3.23.2 Principle of Category NB2 UE Testing 1109

A.3.24 V2X sidelink communication 1112

A.3.24.1 Introduction 1112

A.3.24.2 Reference resource pool configurations for V2X Sidelink Communication 1113

A.3.24.3 Reference measurement channels for V2X Sidelink Communication 1117

A.3.25 Category M2 UE Test Cases 1118

A.3.25.1 Introduction 1118

A.3.25.2 Principle of Cat-M2 UE Testing 1118

A.3.25.3 Principle of Cat-M2 UE testing for inter-frequency RSTD measurement period requirements with measurement gaps 1119

A.3.26 sTTI and processing time reduction test cases with different sTTI/processing time reduction scheme 1120

A.3.26.1 Introduction 1120

A.3.26.2 Principle of testing 1120

A.3.27 LTE INACTIVE Cell Re-selection Test Cases 1120

A.3.27.1 Introduction 1120

A.3.27.2 Principle of INACTIVE cell re-selection Testing 1120

A.3.28 Testing related to Satellite access 1120

A.3.28.1 Introduction 1120

A.3.28.2 Principle of testing GSO and NGSO scenarios 1120

A.3.28.2 Principle of testing different RRM requirements 1121

A.3.28.3 Principle of testing different ephemeris formats 1125

A.3.28.4 General setup for SIB31/SIB-31-NB 1125

A.3.28.5 Satellite specific parameters configuration 1125

A.3.28.5.1 Satellite specific configuration for serving cell 1125

A.3.28.5.2 Satellite specific configuration for neighbour cell 1125

A.4 E-UTRAN RRC_IDLE state 1126

A.4.2 Cell Re-Selection 1126

A.4.2.1 E-UTRAN FDD – FDD Intra frequency case 1126

A.4.2.1.1 Test Purpose and Environment 1126

A.4.2.1.2 Test Requirements 1128

A.4.2.2 E-UTRAN TDD – TDD Intra frequency case 1129

A.4.2.2.1 Test Purpose and Environment 1129

A.4.2.2.2 Test Requirements 1130

A.4.2.3 E-UTRAN FDD – FDD Inter frequency case 1131

A.4.2.3.1 Test Purpose and Environment 1131

A.4.2.3.2 Test Requirements 1132

A.4.2.4 E-UTRAN FDD – TDD Inter frequency case 1133

A.4.2.4.1 Test Purpose and Environment 1133

A.4.2.4.2 Test Requirements 1134

A.4.2.5 E-UTRAN TDD – FDD Inter frequency case 1135

A.4.2.5.1 Test Purpose and Environment 1135

A.4.2.5.2 Test Requirements 1136

A.4.2.6 E-UTRAN TDD – TDD: Inter frequency case 1137

A.4.2.6.1 Test Purpose and Environment 1137

A.4.2.6.2 Test Requirements 1138

A.4.2.7 E-UTRAN FDD – FDD Inter frequency case in the existence of non-allowed CSG cell 1139

A.4.2.7.1 Test Purpose and Environment 1139

A.4.2.7.2 Test Requirements 1140

A.4.2.8 E-UTRAN TDD – TDD Inter frequency case in the existence of non-allowed CSG cell 1141

A.4.2.8.1 Test Purpose and Environment 1141

A.4.2.8.2 Test Requirements 1142

A.4.2.9 E-UTRAN FDD – FDD Intra frequency case for 5MHz bandwidth 1143

A.4.2.9.1 Test Purpose and Environment 1143

A.4.2.9.2 Test Requirements 1143

A.4.2.10 E-UTRAN FDD – FDD reselection using an increased number of carriers 1143

A.4.2.10.1 Test Purpose and Environment 1143

A.4.2.10.2 Test Requirements 1147

A.4.2.11 E-UTRAN TDD – TDD reselection using an increased number of carriers 1147

A.4.2.11.1 Test Purpose and Environment 1147

A.4.2.11.2 Test Requirements 1151

A.4.2.12 E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage 1151

A.4.2.12.1 Test Purpose and Environment 1151

A.4.2.12.2 Test Requirements 1153

A.4.2.13 E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in normal coverage 1154

A.4.2.13.1 Test Purpose and Environment 1154

A.4.2.13.2 Test Requirements 1155

A.4.2.14 E-UTRAN TDD – TDD Intra frequency case for Cat-M1 UE in normal coverage 1156

A.4.2.14.1 Test Purpose and Environment 1156

A.4.2.14.2 Test Requirements 1157

A.4.2.15 E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in enhanced coverage 1158

A.4.2.15.1 Test Purpose and Environment 1158

A.4.2.15.2 Test Requirements 1159

A.4.2.16 E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in enhanced coverage 1160

A.4.2.16.1 Test Purpose and Environment 1160

A.4.2.16.2 Test Requirements 1161

A.4.2.17 E-UTRAN TDD – TDD Intra frequency case for Cat-M1 UE in enhanced coverage 1162

A.4.2.17.1 Test Purpose and Environment 1162

A.4.2.17.2 Test Requirements 1163

A.4.2.18 HD – FDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage 1164

A.4.2.18.1 Test Purpose and Environment 1164

A.4.2.18.2 Test Requirements 1166

A.4.2.19 HD – FDD Intra frequency case for UE Category NB1 In-Band mode in enhanced coverage 1167

A.4.2.19.1 Test Purpose and Environment 1167

A.4.2.19.2 Test Requirements 1169

A.4.2.20 E-UTRAN FDD – FDD Intra frequency case for UE Category 1bis 1170

A.4.2.20.1 Test Purpose and Environment 1170

A.4.2.20.2 Test Requirements 1171

A.4.2.21 E-UTRAN TDD – TDD Intra frequency case for UE Category 1bis 1172

A.4.2.21.1 Test Purpose and Environment 1172

A.4.2.21.2 Test Requirements 1173

A.4.2.22 E-UTRAN FDD – FDD Intra frequency case for UE configured with highSpeedEnhancedMeasFlag 1174

A.4.2.22.1 Test Purpose and Environment 1174

A.4.2.22.2 Test Requirements 1175

A.4.2.23 E-UTRAN TDD – TDD Intra frequency case for UE configured with highSpeedEnhancedMeasFlag 1176

A.4.2.23.1 Test Purpose and Environment 1176

A.4.2.23.2 Test Requirements 1177

A.4.2.24 HD – FDD Inter frequency case for UE Category NB1 In-Band mode in enhanced coverage 1178

A.4.2.24.1 Test Purpose and Environment 1178

A.4.2.24.2 Test Requirements 1181

A.4.2.25 E-UTRAN FDD – FDD Inter frequency case for Cat-M1 UE in normal coverage 1182

A.4.2.25.1 Test Purpose and Environment 1182

A.4.2.25.2 Test Requirements 1183

A.4.2.26 E-UTRAN HD – FDD Inter frequency case for Cat-M1 UE in normal coverage 1184

A.4.2.26.1 Test Purpose and Environment 1184

A.4.2.26.2 Test Requirements 1185

A.4.2.27 E-UTRAN TDD – FDD Inter frequency case for Cat-M1 UE in normal coverage 1186

A.4.2.27.1 Test Purpose and Environment 1186

A.4.2.27.2 Test Requirements 1187

A.4.2.28 E-UTRAN FDD – FDD Inter frequency case for Cat-M1 UE in enhanced coverage 1188

A.4.2.28.1 Test Purpose and Environment 1188

A.4.2.28.2 Test Requirements 1189

A.4.2.29 E-UTRAN HD – FDD Inter frequency case for Cat-M1 UE in enhanced coverage 1190

A.4.2.29.1 Test Purpose and Environment 1190

A.4.2.29.2 Test Requirements 1191

A.4.2.30 E-UTRAN TDD Inter frequency case for Cat-M1 UE in enhanced coverage 1192

A.4.2.30.1 Test Purpose and Environment 1192

A.4.2.30.2 Test Requirements 1193

A.4.2.31 E-UTRAN FDD – FDD Inter frequency case for UE Category 1bis 1194

A.4.2.31.1 Test Purpose and Environment 1194

A.4.2.31.2 Test Requirements 1195

A.4.2.32 E-UTRAN FDD – TDD Inter frequency case for UE Category 1bis 1196

A.4.2.32.1 Test Purpose and Environment 1196

A.4.2.32.2 Test Requirements 1197

A.4.2.33 E-UTRAN TDD – FDD Inter frequency case for UE Category 1bis 1198

A.4.2.33.1 Test Purpose and Environment 1198

A.4.2.33.2 Test Requirements 1199

A.4.2.34 E-UTRAN TDD – TDD: Inter frequency case for UE Category 1bis 1200

A.4.2.34.1 Test Purpose and Environment 1200

A.4.2.34.2 Test Requirements 1201

A.4.2.35 E-UTRAN TDD - TDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage 1202

A.4.2.35.1 Test Purpose and Environment 1202

A.4.2.35.2 Test Requirements 1204

A.4.2.36 E-UTRAN TDD – TDD Intra frequency case for UE Category NB1 In-Band mode in enhanced coverage 1205

A.4.2.36.1 Test Purpose and Environment 1205

A.4.2.36.2 Test Requirements 1207

A.4.2.37 E-UTRAN TDD – TDD Inter frequency case for UE Category NB1 In-Band mode in enhanced coverage 1208

A.4.2.37.1 Test Purpose and Environment 1208

A.4.2.37.2 Test Requirements 1210

A.4.2.38 HD – FDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage with serving cell RRM measurement relaxation 1211

A.4.2.38.1 Test Purpose and Environment 1211

A.4.2.38.2 Test Requirements 1213

A.4.2.39 E-UTRAN FDD – FDD Intra frequency case for UE configured with highSpeedEnhMeasFlag2-r16 1214

A.4.2.39.1 Test Purpose and Environment 1214

A.4.2.39.2 Test Requirements 1215

A.4.2.40 E-UTRAN TDD – TDD Intra frequency case for UE configured with highSpeedEnhMeasFlag2-r16 1216

A.4.2.40.1 Test Purpose and Environment 1216

A.4.2.40.2 Test Requirements 1217

A.4.2.41 HD – FDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage with UE specific DRX 1218

A.4.2.41.1 Test Purpose and Environment 1218

A.4.2.41.2 Test Requirements 1221

A.4.2.42 HD – FDD Intra frequency case for UE Category NB1 In-Band mode in enhanced coverage with UE specific DRX 1222

A.4.2.42.1 Test Purpose and Environment 1222

A.4.2.42.2 Test Requirements 1224

A.4.2.43 HD – FDD Inter frequency case for UE Category NB1 In-Band mode in enhanced coverage with UE specific DRX 1225

A.4.2.43.1 Test Purpose and Environment 1225

A.4.2.43.2 Test Requirements 1227

A.4.2.44 E-UTRAN TDD - TDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage with UE specific DRX 1228

A.4.2.44.1 Test Purpose and Environment 1228

A.4.2.44.2 Test Requirements 1230

A.4.2.45 E-UTRAN TDD – TDD Intra frequency case for UE Category NB1 In-Band mode in enhanced coverage with UE specific DRX 1231

A.4.2.45.1 Test Purpose and Environment 1231

A.4.2.45.2 Test Requirements 1233

A.4.2.46 E-UTRAN TDD – TDD Inter frequency case for UE Category NB1 In-Band mode in enhanced coverage with UE specific DRX 1234

A.4.2.46.1 Test Purpose and Environment 1234

A.4.2.46.2 Test Requirements 1236

A.4.2.47 HD – FDD Intra frequency case for UE Category NB1 In-Band mode in normal coverage with serving cell RRM measurement relaxation with UE specific DRX 1237

A.4.2.47.1 Test Purpose and Environment 1237

A.4.2.47.2 Test Requirements 1239

A.4.2.48 E-UTRAN FD-FDD RSS based Intra frequency case for Cat-M1 UE in normal coverage 1240

A.4.2.48.1 Test Purpose and Environment 1240

A.4.2.48.2 Test Requirements 1241

A.4.2.49 E-UTRAN HD-FDD RSS based Intra frequency case for Cat-M1 UE in normal coverage 1242

A.4.2.49.1 Test Purpose and Environment 1242

A.4.2.49.2 Test Requirements 1244

A.4.2.50 E-UTRAN TDD RSS based Intra frequency case for Cat-M1 UE in normal coverage 1245

A.4.2.50.1 Test Purpose and Environment 1245

A.4.2.50.2 Test Requirements 1247

A.4.2.51 E-UTRAN FD-FDD RSS based Intra frequency case for Cat-M1 UE in enhanced coverage 1248

A.4.2.51.1 Test Purpose and Environment 1248

A.4.2.51.2 Test Requirements 1250

A.4.2.52 E-UTRAN HD-FDD RSS based Intra frequency case for Cat-M1 UE in enhanced coverage 1251

A.4.2.52.1 Test Purpose and Environment 1251

A.4.2.52.2 Test Requirements 1253

A.4.2.53 E-UTRAN TDD RSS based Intra frequency case for Cat-M1 UE in enhanced coverage 1254

A.4.2.53.1 Test Purpose and Environment 1254

A.4.2.53.2 Test Requirements 1255

A.4.2.54 E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage with serving cell RRM measurement relaxation 1256

A.4.2.54.1 Test Purpose and Environment 1256

A.4.2.54.2 Test Requirements 1258

A.4.2.55 E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in normal coverage with serving cell RRM measurement relaxation 1259

A.4.2.55.1 Test Purpose and Environment 1259

A.4.2.55.2 Test Requirements 1261

A.4.2.56 E-UTRAN TDD – TDD Intra frequency case for Cat-M1 UE in normal coverage 1262

A.4.2.56.1 Test Purpose and Environment 1262

A.4.2.56.2 Test Requirements 1263

A.4.3 E-UTRAN to UTRAN Cell Re-Selection 1264

A.4.3.1 E-UTRAN FDD – UTRAN FDD: 1264

A.4.3.1.1 EUTRA FDD-UTRA FDD cell reselection: UTRA FDD is of higher priority 1264

A.4.3.1.1.1 Test Purpose and Environment 1264

A.4.3.1.1.2 Test Requirements 1266

A.4.3.1.2 EUTRA FDD-UTRA FDD cell reselection: UTRA FDD is of lower priority 1266

A.4.3.1.2.1 Test Purpose and Environment 1266

A.4.3.1.2.2 Test Requirements 1269

A.4.3.1.3 EUTRA FDD-UTRA FDD cell reselection in fading propagation conditions: UTRA FDD is of lower priority 1269

A.4.3.1.3.1 Test Purpose and Environment 1269

A.4.3.1.3.2 Test Requirements 1272

A.4.3.1.4 EUTRA FDD-UTRA FDD cell reselection: UTRA FDD is of lower priority for 5MHz bandwidth 1272

A.4.3.1.4.1 Test Purpose and Environment 1272

A.4.3.1.4.2 Test Requirements 1273

A.4.3.1.5 Idle mode FDD to UTRA FDD interRAT reselection 1273

A.4.3.1.5.1 Test Purpose and Environment 1273

A.4.3.1.5.2 Test Requirements 1276

A.4.3.2 E-UTRAN FDD – UTRAN TDD: 1277

A.4.3.2.1 Test Purpose and Environment 1277

A.4.3.2.1.1 Void 1277

A.4.3.2.1.2 1.28Mcps TDD option 1277

A.4.3.2.1.3 Void 1279

A.4.3.2.2 Test Requirements 1279

A.4.3.2.2.1 1.28Mcps TDD option 1279

A.4.3.2A E-UTRA FDD to UTRA TDD cell re-selection for IncMon 1279

A.4.3.2A.1 Test Purpose and Environment 1279

A.4.3.2A.2 Test Requirements 1283

A.4.3.3 E-UTRAN TDD – UTRAN FDD: 1283

A.4.3.3.1 Test Purpose and Environment 1283

A.4.3.3.2 Test Requirements 1286

A.4.3.3A Idle mode TDD to UTRA FDD interRAT reselection 1286

A.4.3.3A.1 Test Purpose and Environment 1286

A.4.3.3A.2 Test Requirements 1291

A.4.3.4 E-UTRAN TDD – UTRAN TDD: 1292

A.4.3.4.1 E-UTRA to UTRA TDD cell re-selection: UTRA is of higher priority 1292

A.4.3.4.1.1 Test Purpose and Environment 1292

A.4.3.4.1.2 Test Requirements 1294

A.4.3.4.2 E-UTRA to UTRA TDD cell re-selection: UTRA is of lower priority 1294

A.4.3.4.2.1 Test Purpose and Environment 1294

A.4.3.4.2.2 Test Requirements 1296

A.4.3.4.3 EUTRA TDD-UTRA TDD cell reselection in fading propagation conditions: UTRA TDD is of lower priority 1296

A.4.3.4.3.1 Test Purpose and Environment 1296

A.4.3.4.3.2 Test Requirements 1299

A.4.3.4.4 E-UTRA TDD to UTRA TDD cell re-selection for IncMon 1299

A.4.3.4.4.1 Test Purpose and Environment 1299

A.4.3.4.4.2 Test Requirements 1303

A.4.4 E-UTRAN to GSM Cell Re-Selection 1303

A.4.4.1 E-UTRAN FDD – GSM: 1303

A.4.4.1.1 Test Purpose and Environment 1303

A.4.4.1.2 Test Requirements 1305

A.4.4.2 E-UTRAN TDD – GSM: 1305

A.4.4.2.1 Test Purpose and Environment 1305

A.4.4.2.2 Test Requirements 1307

A.4.5 E-UTRAN to HRPD Cell Re-Selection 1308

A.4.5.1 E-UTRAN FDD – HRPD 1308

A.4.5.1.1 E-UTRAN FDD – HRPD Cell Reselection: HRPD is of Lower Priority 1308

A.4.5.1.1.1 Test Purpose and Environment 1308

A.4.5.1.1.2 Test Requirements 1310

A.4.5.2 E-UTRAN TDD – HRPD 1310

A.4.5.2.1 E-UTRAN TDD – HRPD Cell Reselection: HRPD is of Lower Priority 1310

A.4.5.2.1.1 Test Purpose and Environment 1310

A.4.5.2.1.2 Test Requirements 1313

A.4.6 E-UTRAN to cdma2000 1X Cell Re-Selection 1313

A.4.6.1 E-UTRAN FDD – cdma2000 1X 1313

A.4.6.1.1 E-UTRAN FDD – cdma2000 1X Cell Reselection: cdma2000 1X is of Lower Priority 1313

A.4.6.1.1.1 Test Purpose and Environment 1313

A.4.6.1.1.2 Test Requirements 1316

A.4.6.2 E-UTRAN TDD – cdma2000 1X 1316

A.4.6.2.1 E-UTRAN TDD –cdma2000 1X Cell Reselection: cdma2000 1X is of Lower Priority 1316

A.4.6.2.1.1 Test Purpose and Environment 1316

A.4.6.2.1.2 Test Requirements 1319

A.4.7 Idle State Positioning Measurement for UE category NB1 1319

A.4.7.1 HD – FDD Intra frequency case for UE Category NB1 standalone mode in enhanced coverage 1319

A.4.7.1.1 Test Purpose and Environment 1319

A.4.7.1.2 Test Requirements 1324

A.4.7.2 HD – FDD Inter frequency case for UE Category NB1 standalone mode in enhanced coverage 1325

A.4.7.2.1 Test Purpose and Environment 1325

A.4.7.4.2 Test Requirements 1329

A.4.7.3 TDD Intra frequency case for UE Category NB1 standalone mode in enhanced coverage 1330

A.4.7.3.1 Test Purpose and Environment 1330

A.4.7.3.2 Test Requirements 1334

A.4.7.4 TDD Inter frequency case for UE Category NB1 standalone mode in enhanced coverage 1335

A.4.7.4.1 Test Purpose and Environment 1335

A.4.7.4.2 Test Requirements 1339

A.5 E-UTRAN RRC CONNECTED Mode Mobility 1340

A.5.1 E-UTRAN Handover 1340

A.5.1.1 E-UTRAN FDD - FDD Intra frequency handover 1340

A.5.1.1.1 Test Purpose and Environment 1340

A.5.1.1.2 Test Requirements 1342

A.5.1.2 E-UTRAN TDD - TDD Intra frequency handover 1342

A.5.1.2.1 Test Purpose and Environment 1342

A.5.1.2.2 Test Requirements 1344

A.5.1.3 E-UTRAN FDD – FDD Inter frequency handover 1344

A.5.1.3.1 Test Purpose and Environment 1344

A.5.1.3.2 Test Requirements 1346

A.5.1.4 E-UTRAN TDD – TDD Inter frequency handover 1346

A.5.1.4.1 Test Purpose and Environment 1346

A.5.1.4.2 Test Requirements 1348

A.5.1.5 E-UTRAN FDD – FDD Inter frequency handover: unknown target cell 1348

A.5.1.5.1 Test Purpose and Environment 1348

A.5.1.5.2 Test Requirements 1350

A.5.1.6  E-UTRAN TDD – TDD Inter frequency handover; unknown Target Cell 1350

A.5.1.6.1 Test Purpose and Environment 1350

A.5.1.6.2 Test Requirements 1352

A.5.1.7 E-UTRAN FDD – TDD Inter frequency handover 1352

A.5.1.7.1 Test Purpose and Environment 1352

A.5.1.7.2 Test Requirements 1355

A.5.1.8 E-UTRAN TDD – FDD Inter frequency handover 1355

A.5.1.8.1 Test Purpose and Environment 1355

A.5.1.8.2 Test Requirements 1358

A.5.1.9 E-UTRAN FDD - FDD Intra frequency handover for 5MHz bandwidth 1358

A.5.1.9.1 Test Purpose and Environment 1358

A.5.1.9.2 Test Requirements 1359

A.5.1.10 E-UTRAN FDD - FDD Intra frequency handover for UE category 0 1359

A.5.1.10.1 Test Purpose and Environment 1359

A.5.1.10.2 Test Requirements 1361

A.5.1.11 E-UTRAN HD - FDD Intra frequency handover for UE category 0 1361

A.5.1.11.1 Test Purpose and Environment 1361

A.5.1.11.2 Test Requirements 1363

A.5.1.12 E-UTRAN TDD - TDD Intra frequency handover for UE category 0 1363

A.5.1.12.1 Test Purpose and Environment 1363

A.5.1.12.2 Test Requirements 1365

A.5.1.13 E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA 1365

A.5.1.13.1 Test Purpose and Environment 1365

A.5.1.13.2 Test Requirements 1367

A.5.1.14 E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA 1368

A.5.1.14.1 Test Purpose and Environment 1368

A.5.1.14.2 Test Requirements 1369

A.5.1.15 E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeA 1370

A.5.1.15.1 Test Purpose and Environment 1370

A.5.1.15.2 Test Requirements 1371

A.5.1.16 E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeB 1372

A.5.1.16.1 Test Purpose and Environment 1372

A.5.1.16.2 Test Requirements 1373

A.5.1.17 E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeB 1374

A.5.1.17.1 Test Purpose and Environment 1374

A.5.1.17.2 Test Requirements 1375

A.5.1.18 E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeB 1376

A.5.1.18.1 Test Purpose and Environment 1376

A.5.1.18.2 Test Requirements 1377

A.5.1.19 E-UTRAN FDD - FDD Intra frequency handover for UE Category 1bis 1378

A.5.1.19.1 Test Purpose and Environment 1378

A.5.1.19.2 Test Requirements 1379

A.5.1.20 E-UTRAN TDD - TDD Intra frequency handover for UE Category 1bis 1380

A.5.1.20.1 Test Purpose and Environment 1380

A.5.1.20.2 Test Requirements 1381

A.5.1.21 E-UTRAN FDD - FDD Intra frequency RACH-less handover 1382

A.5.1.21.1 Test Purpose and Environment 1382

A.5.1.21.2 Test Requirements 1383

A.5.1.22 E-UTRAN TDD - TDD Intra frequency RACH-less handover 1383

A.5.1.22.1 Test Purpose and Environment 1383

A.5.1.22.2 Test Requirements 1385

A.5.1.23 E-UTRAN FDD – FDD Inter frequency RACH-less handover 1385

A.5.1.23.1 Test Purpose and Environment 1385

A.5.1.23.2 Test Requirements 1387

A.5.1.24 E-UTRAN TDD – TDD Inter frequency RACH-less handover 1387

A.5.1.24.1 Test Purpose and Environment 1387

A.5.1.24.2 Test Requirements 1389

A.5.1.25 E-UTRAN FDD - FDD Intra frequency make-before-break handover 1389

A.5.1.25.1 Test Purpose and Environment 1389

A.5.1.25.2 Test Requirements 1391

A.5.1.26 E-UTRAN TDD - TDD Intra frequency make-before-break handover 1392

A.5.1.26.1 Test Purpose and Environment 1392

A.5.1.26.2 Test Requirements 1393

A.5.1.27 E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeA 1394

A.5.1.27.1 Test Purpose and Environment 1394

A.5.1.27.2 Test Requirements 1395

A.5.1.28 E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeA 1396

A.5.1.28.1 Test Purpose and Environment 1396

A.5.1.28.2 Test Requirements 1397

A.5.1.29 E-UTRAN TDD inter frequency handover for Cat-M1 UEs in CEModeA 1398

A.5.1.29.1 Test Purpose and Environment 1398

A.5.1.29.2 Test Requirements 1399

A.5.1.30 E-UTRAN FDD inter frequency handover for Cat-M1 UEs in CEModeB 1400

A.5.1.30.1 Test Purpose and Environment 1400

A.5.1.30.2 Test Requirements 1401

A.5.1.31 E-UTRAN HD-FDD inter frequency handover for Cat-M1 UEs in CEModeB 1402

A.5.1.31.1 Test Purpose and Environment 1402

A.5.1.31.2 Test Requirements 1403

A.5.1.32 E-UTRAN TDD inter frequency handover for Cat-M1 UEs in CEModeB 1404

A.5.1.32.1 Test Purpose and Environment 1404

A.5.1.32.2 Test Requirements 1405

A.5.1.33 E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition 1406

A.5.1.33.1 Test Purpose and Environment 1406

A.5.1.13.2 Test Requirements 1407

A.5.1.34 E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition 1408

A.5.1.34.1 Test Purpose and Environment 1408

A.5.1.34.2 Test Requirements 1409

A.5.1.35 E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition 1410

A.5.1.35.1 Test Purpose and Environment 1410

A.5.1.35.2 Test Requirements 1411

A.5.1.36 E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition 1412

A.5.1.36.1 Test Purpose and Environment 1412

A.5.1.36.2 Test Requirements 1413

A.5.1.37 E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition 1414

A.5.1.37.1 Test Purpose and Environment 1414

A.5.1.37.2 Test Requirements 1415

A.5.1.38 E-UTRAN TDD Intra frequency handover for Cat-M1 UEs in CEModeB without SFN acquisition 1416

A.5.1.38.1 Test Purpose and Environment 1416

A.5.1.38.2 Test Requirements 1417

A.5.1.39 E-UTRAN FDD - FDD Intra frequency handover with direct SCell activation 1418

A.5.1.39.1 Test Purpose and Environment 1418

A.5.1.39.2 Test Requirements 1419

A.5.1.40 E-UTRAN TDD - TDD Intra frequency handover with direct SCell activation 1420

A.5.1.40.1 Test Purpose and Environment 1420

A.5.1.40.2 Test Requirements 1421

A.5.1.41 E-UTRAN FDD – FDD Intra-band Inter-frequency sync DAPS handover 1422

A.5.1.41.1 Test Purpose and Environment 1422

A.5.1.41.2 Test Requirements 1424

A.5.1.42 E-UTRAN FDD – FDD Intra-band Inter-frequency async DAPS handover 1425

A.5.1.42.1 Test Purpose and Environment 1425

A.5.1.42.2 Test Requirements 1426

A.5.1.43 E-UTRAN FDD – FDD Inter-band Inter-frequency sync DAPS handover 1427

A.5.1.43.1 Test Purpose and Environment 1427

A.5.1.43.2 Test Requirements 1428

A.5.1.44 E-UTRAN FDD – FDD Inter-band Inter-frequency async DAPS handover 1429

A.5.1.44.1 Test Purpose and Environment 1429

A.5.1.44.2 Test Requirements 1430

A.5.1.45 E-UTRAN FDD - FDD Intra frequency DAPS handover 1431

A.5.1.45.1 Test Purpose and Environment 1431

A.5.1.45.1 Test Requirements 1432

A.5.1.46 E-UTRAN TDD - TDD Intra frequency DAPS handover 1433

A.5.1.46.1 Test Purpose and Environment 1433

A.5.1.46.2 Test Requirements 1434

A.5.1.47 E-UTRAN FDD - FDD Intra frequency conditional handover 1435

A.5.1.47.1 Test Purpose and Environment 1435

A.5.1.47.2 Test Requirements 1436

A.5.1.48 E-UTRAN TDD - TDD Intra frequency conditional handover 1437

A.5.1.48.1 Test Purpose and Environment 1437

A.5.1.48.2 Test Requirements 1438

A.5.1.49 E-UTRAN FDD - FDD Inter frequency conditional handover 1439

A.5.1.49.1 Test Purpose and Environment 1439

A.5.1.49.2 Test Requirements 1440

A.5.1.50 E-UTRAN TDD - TDD Inter frequency conditional handover 1441

A.5.1.50.1 Test Purpose and Environment 1441

A.5.1.50.2 Test Requirements 1442

A.5.1.51 E-UTRAN FDD - TDD Inter frequency conditional handover 1443

A.5.1.51.1 Test Purpose and Environment 1443

A.5.1.51.2 Test Requirements 1445

A.5.1.52 E-UTRAN TDD - FDD Inter frequency conditional handover 1445

A.5.152.1 Test Purpose and Environment 1445

A.5.1.52.2 Test Requirements 1448

A.5.1.53 E-UTRAN TDD – TDD Intra-band Inter-frequency sync DAPS handover 1449

A.5.1.53.1 Test Purpose and Environment 1449

A.5.1.53.2 Test Requirements 1451

A.5.1.54 E-UTRAN TDD – TDD Inter-band Inter-frequency sync DAPS handover 1452

A.5.1.54.1 Test Purpose and Environment 1452

A.5.1.54.2 Test Requirements 1454

A.5.1.55 E-UTRAN FDD - TDD inter-band inter-frequency synchronous DAPS handover 1455

A.5.1.55.1 Test Purpose and Environment 1455

A.5.1.56 E-UTRAN TDD - FDD inter-band inter-frequency synchronous DAPS handover 1459

A.5.1.56.1 Test Purpose and Environment 1459

A.5.1.56.2 Test Requirements 1462

A.5.1.57 E-UTRAN FDD – TDD Inter-band Inter-frequency async DAPS handover 1463

A.5.1.57.1 Test Purpose and Environment 1463

A.5.1.57.2 Test Requirements 1465

A.5.1.58 E-UTRAN TDD – FDD Inter-band Inter-frequency async DAPS handover 1465

A.5.1.58.1 Test Purpose and Environment 1465

A.5.1.58.2 Test Requirements 1468

A.5.2 E-UTRAN Handover to other RATs 1468

A.5.2.1 E-UTRAN FDD – UTRAN FDD Handover 1468

A.5.2.1.1 Test Purpose and Environment 1468

A.5.2.1.2 Test Requirements 1470

A.5.2.2 E-UTRAN TDD - UTRAN FDD Handover 1471

A.5.2.2.1 Test Purpose and Environment 1471

A.5.2.2.2 Test Requirements 1474

A.5.2.3 E-UTRAN FDD- GSM Handover 1474

A.5.2.3.1 Test Purpose and Environment 1474

A.5.2.3.2 Test Requirements 1475

A.5.2.4 E-UTRAN TDD - UTRAN TDD Handover 1476

A.5.2.4.1 Test Purpose and Environment 1476

A.5.2.4.1.1 Void 1476

A.5.2.4.1.2 1.28 Mcps TDD option 1476

A.5.2.4.1.3 Void 1478

A.5.2.4.2 Test Requirements 1478

A.5.2.4.2.1 Void 1478

A.5.2.4.2.2 1.28 Mcps TDD option 1478

A.5.2.4.2.3 Void 1478

A.5.2.5 E-UTRAN FDD – UTRAN TDD Handover 1478

A.5.2.5.1 Test Purpose and Environment 1478

A.5.2.5.1.3 Void 1481

A.5.2.5.2 Test Requirements 1481

A.5.2.5.2.1 Void 1481

A.5.2.5.2.2 1.28 Mcps TDD option 1481

A.5.2.5.2.3 Void 1481

A.5.2.6 E-UTRAN TDD - GSM Handover 1481

A.5.2.6.1 Test Purpose and Environment 1481

A.5.2.6.2 Test Requirements 1483

A.5.2.7 E-UTRAN FDD – UTRAN FDD Handover; Unknown Target Cell 1484

A.5.2.7.1 Test Purpose and Environment 1484

A.5.2.7.2 Test Requirements 1486

A.5.2.8 E-UTRAN FDD - GSM Handover; Unknown Target Cell 1486

A.5.2.8.1 Test Purpose and Environment 1486

A.5.2.8.2 Test Requirements 1487

A.5.2.9 E-UTRAN TDD - GSM Handover; Unknown Target Cell 1488

A.5.2.9.1 Test Purpose and Environment 1488

A.5.2.9.2 Test Requirements 1489

A.5.2.10 E-UTRAN TDD to UTRAN TDD handover: unknown target cell 1490

A.5.2.10.1 Test Purpose and Environment 1490

A.5.2.10.2 Test Requirements 1492

A.5.2.10A E-UTRAN FDD – UTRAN FDD Multicarrier Handover with two target cells 1492

A.5.2.10A.1 Test Purpose and Environment 1492

A.5.2.10A.2 Test Requirements 1495

A.5.2.10B E-UTRAN TDD – UTRAN FDD Multicarrier Handover with two target cells 1495

A.5.2.10B.1 Test Purpose and Environment 1495

A.5.2.10B.2 Test Requirements 1498

A.5.2.11 E-UTRAN FDD – UTRAN FDD Handover for 5MHz Bandwidth 1498

A.5.2.11.1 Test Purpose and Environment 1498

A.5.2.11.2 Test Requirements 1498

A.5.3 E-UTRAN Handover to Non-3GPP RATs 1499

A.5.3.1 E-UTRAN FDD – HRPD Handover 1499

A.5.3.1.1 Test Purpose and Environment 1499

A.5.3.1.2 Test Requirements 1501

A.5.3.2 E-UTRAN FDD – cdma2000 1X Handover 1501

A.5.3.2.1 Test Purpose and Environment 1501

A.5.3.2.2 Test Requirements 1504

A.5.3.3 E-UTRAN FDD – HRPD Handover; Unknown Target Cell 1504

A.5.3.3.1 Test Purpose and Environment 1504

A.5.3.3.2 Test Requirements 1507

A.5.3.4 E-UTRAN FDD – cdma2000 1X Handover; Unknown Target cell 1507

A.5.3.4.1 Test Purpose and Environment 1507

A.5.3.4.2 Test Requirements 1509

A.5.3.5 E-UTRAN TDD – HRPD Handover 1509

A.5.3.5.1 Test Purpose and Environment 1509

A.5.3.5.2 Test Requirements 1512

A.5.3.6 E-UTRAN TDD – cdma2000 1X Handover 1512

A.5.3.6.1 Test Purpose and Environment 1512

A.5.3.6.2 Test Requirements 1515

A.6 RRC Connection Control 1515

A.6.1 RRC Re-establishment 1515

A.6.1.1 E-UTRAN FDD Intra-frequency RRC Re-establishment 1515

A.6.1.1.1 Test Purpose and Environment 1515

A.6.1.1.2 Test Requirements 1516

A.6.1.2 E-UTRAN FDD Inter-frequency RRC Re-establishment 1517

A.6.1.2.1 Test Purpose and Environment 1517

A.6.1.2.2 Test Requirements 1518

A.6.1.3 E-UTRAN TDD Intra-frequency RRC Re-establishment 1519

A.6.1.3.1 Test Purpose and Environment 1519

A.6.1.3.2 Test Requirements 1520

A.6.1.4 E-UTRAN TDD Inter-frequency RRC Re-establishment 1521

A.6.1.4.1 Test Purpose and Environment 1521

A.6.1.4.2 Test Requirements 1522

A.6.1.5 E-UTRAN FDD Intra-frequency RRC Re-establishment for 5MHz bandwidth 1523

A.6.1.5.1 Test Purpose and Environment 1523

A.6.1.5.2 Test Requirements 1523

A.6.1.6 E-UTRAN FD-FDD Intra-frequency RRC Re-establishment for UE category 0 1523

A.6.1.6.1 Test Purpose and Environment 1523

A.6.1.6.2 Test Requirements 1525

A.6.1.7 E-UTRAN HD-FDD Intra-frequency RRC Re-establishment for UE category 0 1526

A.6.1.7.1 Test Purpose and Environment 1526

A.6.1.7.2 Test Requirements 1527

A.6.1.8 E-UTRAN TDD Intra-frequency RRC Re-establishment for UE category 0 1528

A.6.1.8.1 Test Purpose and Environment 1528

A.6.1.8.2 Test Requirements 1529

A.6.1.9 E-UTRAN FD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA 1530

A.6.1.9.1 Test Purpose and Environment 1530

A.6.1.9.2 Test Requirements 1531

A.6.1.10 E-UTRAN HD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA 1532

A.6.1.10.1 Test Purpose and Environment 1532

A.6.1.10.2 Test Requirements 1533

A.6.1.11 E-UTRAN TDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA 1534

A.6.1.11.1 Test Purpose and Environment 1534

A.6.1.11.2 Test Requirements 1535

A.6.1.12 E-UTRAN FD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeB 1536

A.6.1.12.1 Test Purpose and Environment 1536

A.6.1.12.2 Test Requirements 1537

A.6.1.13 E-UTRAN HD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeB 1538

A.6.1.13.1 Test Purpose and Environment 1538

A.6.1.13.2 Test Requirements 1539

A.6.1.14 E-UTRAN TDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeB 1540

A.6.1.14.1 Test Purpose and Environment 1540

A.6.1.14.2 Test Requirements 1541

A.6.1.15 HD-FDD Intra-frequency RRC Re-establishment for UE category NB1 in In-Band mode under enhanced coverage 1542

A.6.1.15.1 Test Purpose and Environment 1542

A.6.1.15.2 Test Requirements 1544

A.6.1.16 HD-FDD Inter-frequency RRC Re-establishment for UE category NB1 in In-Band mode under normal coverage 1545

A.6.1.16.1 Test Purpose and Environment 1545

A.6.1.16.2 Test Requirements 1547

A.6.1.17 E-UTRAN FD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA 1548

A.6.1.17.1 Test Purpose and Environment 1548

A.6.1.17.2 Test Requirements 1549

A.6.1.18 E-UTRAN HD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA 1550

A.6.1.18.1 Test Purpose and Environment 1550

A.6.1.18.2 Test Requirements 1551

A.6.1.19 E-UTRAN TDD-TDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA 1552

A.6.1.19.1 Test Purpose and Environment 1552

A.6.1.19.2 Test Requirements 1553

A.6.1.20 E-UTRAN FD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeB 1554

A.6.1.20.1 Test Purpose and Environment 1554

A.6.1.20.2 Test Requirements 1555

A.6.1.21 E-UTRAN HD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeB 1556

A.6.1.21.1 Test Purpose and Environment 1556

A.6.1.21.2 Test Requirements 1557

A.6.1.22 E-UTRAN TDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeB 1558

A.6.1.22.1 Test Purpose and Environment 1558

A.6.1.22.2 Test Requirements 1559

A.6.1.23 E-UTRAN TDD Inter-frequency RRC Re-establishment for UE category NB1 in In-Band mode under normal coverage 1560

A.6.1.23.1 Test Purpose and Environment 1560

A.6.1.23.2 Test Requirements 1562

A.6.1.24 E-UTRAN TDD - TDD Intra-frequency RRC Re-establishment for UE category NB1 in In-Band mode under enhanced coverage 1563

A.6.1.24.1 Test Purpose and Environment 1563

A.6.1.24.2 Test Requirements 1565

A.6.2 Random Access 1566

A.6.2.1 E-UTRAN FDD – Contention Based Random Access Test 1566

A.6.2.1.1 Test Purpose and Environment 1566

A.6.2.1.2 Test Requirements 1567

A.6.2.1.2.1 Random Access Response Reception 1567

A.6.2.1.2.2 No Random Access Response Reception 1567

A.6.2.1.2.3 Receiving a NACK on msg3 1567

A.6.2.1.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1568

A.6.2.1.2.5 Reception of a Correct Message over Temporary C-RNTI 1568

A.6.2.1.2.6 Contention Resolution Timer expiry 1568

A.6.2.2 E-UTRAN FDD – Non-Contention Based Random Access Test 1568

A.6.2.2.1 Test Purpose and Environment 1568

A.6.2.2.2 Test Requirements 1569

A.6.2.2.2.1 Random Access Response Reception 1570

A.6.2.2.2.2 No Random Access Response Reception 1570

A.6.2.3 E-UTRAN TDD – Contention Based Random Access Test 1570

A.6.2.3.1 Test Purpose and Environment 1570

A.6.2.3.2 Test Requirements 1572

A.6.2.3.2.1 Random Access Response Reception 1572

A.6.2.3.2.2 No Random Access Response reception 1572

A.6.2.3.2.3 Receiving a NACK on msg3 1572

A.6.2.3.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1573

A.6.2.3.2.5 Reception of a Correct Message over Temporary C-RNTI 1573

A.6.2.3.2.6 Contention Resolution Timer expiry 1573

A.6.2.4 E-UTRAN TDD – Non-Contention Based Random Access Test 1573

A.6.2.4.1 Test Purpose and Environment 1573

A.6.2.4.2 Test Requirements 1575

A.6.2.4.2.1 Random Access Response Reception 1575

A.6.2.4.2.2 No Random Access Response Reception 1575

A.6.2.5 E-UTRAN FDD – Contention Based Random Access Test for 5MHz bandwidth 1575

A.6.2.5.1 Test Purpose and Environment 1575

A.6.2.5.2 Test Requirements 1576

A.6.2.6 E-UTRAN FDD – Non-contention Based Random Access Test for 5MHz bandwidth 1576

A.6.2.6.1 Test Purpose and Environment 1576

A.6.2.6.2 Test Requirements 1576

A.6.2.7 E-UTRAN FDD – Non-Contention Based Random Access Test For SCell 1577

A.6.2.7.1 Test Purpose and Environment 1577

A.6.2.7.2 Test Requirements 1579

A.6.2.7.2.1 Random Access Response Reception 1579

A.6.2.7.2.2 No Random Access Response Reception 1579

A.6.2.7.2.3 Stop Preamble transmission if maximum number of preamble transmission counter has been reached 1579

A.6.2.8 E-UTRAN TDD – Non-Contention Based Random Access Test For SCell 1580

A.6.2.8.1 Test Purpose and Environment 1580

A.6.2.8.2 Test Requirements 1582

A.6.2.8.2.1 Random Access Response Reception 1582

A.6.2.8.2.2 No Random Access Response Reception 1582

A.6.2.8.2.3 Stop Preamble transmission if maximum number of preamble transmission counter has been reached 1582

A.6.2.9 3DL/3UL TDD CA Non-Contention Based Random Access Test for 2 SCells 1583

A.6.2.9.1 Test Purpose and Environment 1583

A.6.2.9.2 Test Requirements 1586

A.6.2.9.2.1 Random Access Response Reception 1586

A.6.2.9.2.2 No Random Access Response Reception 1587

A.6.2.9.2.3 Stop Preamble transmission if maximum number of preamble transmission counter has been reached 1587

A.6.2.10 E-UTRAN FDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage 1588

A.6.2.10.1 Test Purpose and Environment 1588

A.6.2.10.2 Test Requirements 1590

A.6.2.10.2.1 Random Access Response Reception 1590

A.6.2.10.2.2 No Random Access Response Reception 1591

A.6.2.10.2.3 Receiving a NACK on msg3 1591

A.6.2.10.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1591

A.6.2.10.2.5 Reception of a Correct Message over Temporary C-RNTI 1591

A.6.2.10.2.6 Contention Resolution Timer expiry 1591

A.6.2.10.2.7 PRACH Resource Selection 1592

A.6.2.11 E-UTRAN HD-FDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage 1592

A.6.2.11.1 Test Purpose and Environment 1592

A.6.2.11.2 Test Requirements 1594

A.6.2.11.2.1 Random Access Response Reception 1594

A.6.2.11.2.2 No Random Access Response Reception 1595

A.6.2.11.2.3 Receiving a NACK on msg3 1595

A.6.2.11.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1595

A.6.2.11.2.5 Reception of a Correct Message over Temporary C-RNTI 1595

A.6.2.11.2.6 Contention Resolution Timer expiry 1595

A.6.2.11.2.7 PRACH Resource Selection 1596

A.6.2.12 E-UTRAN TDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage 1596

A.6.2.12.1 Test Purpose and Environment 1596

A.6.2.12.2 Test Requirements 1598

A.6.2.12.2.1 Random Access Response Reception 1598

A.6.2.12.2.2 No Random Access Response Reception 1599

A.6.2.12.2.3 Receiving a NACK on msg3 1599

A.6.2.12.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1599

A.6.2.12.2.5 Reception of a Correct Message over Temporary C-RNTI 1599

A.6.2.12.2.6 Contention Resolution Timer expiry 1599

A.6.2.12.2.7 PRACH Resource Selection 1600

A.6.2.13 E-UTRAN FDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage 1600

A.6.2.13.1 Test Purpose and Environment 1600

A.6.2.13.2 Test Requirements 1602

A.6.2.13.2.1 Random Access Response Reception 1602

A.6.2.13.2.2 No Random Access Response Reception 1603

A.6.2.13.2.3 Receiving a NACK on msg3 1603

A.6.2.13.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1603

A.6.2.13.2.5 Reception of a Correct Message over Temporary C-RNTI 1603

A.6.2.13.2.6 Contention Resolution Timer expiry 1603

A.6.2.13.2.7 PRACH Resource Selection 1604

A.6.2.14 E-UTRAN HD-FDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage 1604

A.6.2.14.1 Test Purpose and Environment 1604

A.6.2.14.2 Test Requirements 1606

A.6.2.14.2.1 Random Access Response Reception 1606

A.6.2.14.2.2 No Random Access Response Reception 1607

A.6.2.14.2.3 Receiving a NACK on msg3 1607

A.6.2.14.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1607

A.6.2.14.2.5 Reception of a Correct Message over Temporary C-RNTI 1607

A.6.2.14.2.6 Contention Resolution Timer expiry 1607

A.6.2.14.2.7 PRACH Resource Selection 1608

A.6.2.15 E-UTRAN TDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage 1608

A.6.2.15.1 Test Purpose and Environment 1608

A.6.2.15.2 Test Requirements 1610

A.6.2.15.2.1 Random Access Response Reception 1610

A.6.2.15.2.2 No Random Access Response Reception 1611

A.6.2.15.2.3 Receiving a NACK on msg3 1611

A.6.2.15.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1611

A.6.2.15.2.5 Reception of a Correct Message over Temporary C-RNTI 1611

A.6.2.15.2.6 Contention Resolution Timer expiry 1611

A.6.2.15.2.7 PRACH Resource Selection 1612

A.6.2.16 Contention Based Random Access Test for UE category NB1 UEs In-band mode in normal coverage 1612

A.6.2.16.1 Test Purpose and Environment 1612

A.6.2.16.2 Test Requirements 1615

A.6.2.16.2.1 Random Access Response Reception 1615

A.6.2.16.2.2 No Random Access Response Reception 1616

A.6.2.16.2.3 Receiving a NACK on msg3 1616

A.6.2.16.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1616

A.6.2.16.2.5 Reception of a Correct Message over Temporary C-RNTI 1616

A.6.2.16.2.6 Contention Resolution Timer expiry 1616

A.6.2.16.2.7 NPRACH Resource Selection 1616

A.6.2.17 Contention Based Random Access Test for UE category NB1 UEs In-band mode in Enhanced Coverage 1617

A.6.2.17.1 Test Purpose and Environment 1617

A.6.2.17.2 Test Requirements 1620

A.6.2.17.2.1 Random Access Response Reception 1620

A.6.2.17.2.2 No Random Access Response Reception 1621

A.6.2.17.2.3 Receiving a NACK on msg3 1621

A.6.2.17.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1621

A.6.2.17.2.5 Reception of a Correct Message over Temporary C-RNTI 1621

A.6.2.17.2.6 Contention Resolution Timer expiry 1621

A.6.2.17.2.7 NPRACH Resource Selection 1621

A.6.2.18 Contention Based Random Access on Non-anchor Carrier Test for UE category NB1 UEs In-band mode in Enhanced Coverage 1622

A.6.2.18.1 Test Purpose and Environment 1622

A.6.2.18.2 Test Requirements 1625

A.6.2.18.2.1 Random Access Response Reception 1625

A.6.2.18.2.2 No Random Access Response Reception 1626

A.6.2.18.2.3 Receiving a NACK on msg3 1626

A.6.2.18.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1626

A.6.2.18.2.5 Reception of a Correct Message over Temporary C-RNTI 1626

A.6.2.18.2.6 Contention Resolution Timer expiry 1626

A.6.2.18.2.7 NPRACH Resource Selection 1626

A.6.2.19 TDD Contention Based Random Access Test for UE category NB1 UEs In-band mode in normal coverage 1627

A.6.2.19.1 Test Purpose and Environment 1627

A.6.2.19.2 Test Requirements 1629

A.6.2.19.2.1 Random Access Response Reception 1629

A.6.2.19.2.2 No Random Access Response Reception 1630

A.6.2.19.2.3 Receiving a NACK on msg3 1630

A.6.2.19.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1630

A.6.2.19.2.5 Reception of a Correct Message over Temporary C-RNTI 1630

A.6.2.19.2.6 Contention Resolution Timer expiry 1630

A.6.2.19.2.7 NPRACH Resource Selection 1630

A.6.2.20 TDD Contention Based Random Access Test for UE category NB1 UEs In-band mode in enhanced coverage 1631

A.6.2.20.1 Test Purpose and Environment 1631

A.6.2.20.2 Test Requirements 1633

A.6.2.20.2.1 Random Access Response Reception 1633

A.6.2.20.2.2 No Random Access Response Reception 1634

A.6.2.20.2.3 Receiving a NACK on msg3 1634

A.6.2.20.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1634

A.6.2.20.2.5 Reception of a Correct Message over Temporary C-RNTI 1634

A.6.2.20.2.6 Contention Resolution Timer expiry 1634

A.6.2.20.2.7 NPRACH Resource Selection 1634

A.6.2.21 TDD Contention Based Random Access on Non-anchor Carrier Test for UE category NB1 UEs In-band mode in Enhanced Coverage 1635

A.6.2.21.1 Test Purpose and Environment 1635

A.6.2.21.2 Test Requirements 1637

A.6.2.21.2.1 Random Access Response Reception 1637

A.6.2.21.2.2 No Random Access Response Reception 1638

A.6.2.21.2.3 Receiving a NACK on msg3 1638

A.6.2.21.2.4 Reception of an Incorrect Message over Temporary C-RNTI 1638

A.6.2.21.2.5 Reception of a Correct Message over Temporary C-RNTI 1638

A.6.2.21.2.6 Contention Resolution Timer expiry 1638

A.6.2.21.2.7 NPRACH Resource Selection 1638

A.6.3 RRC Connection Release with Redirection 1639

A.6.3.1 Redirection from E-UTRAN FDD to UTRAN FDD 1639

A.6.3.1.1 Test Purpose and Environment 1639

A.6.3.1.2 Test Requirements 1641

A.6.3.2 Redirection from E-UTRAN TDD to UTRAN FDD 1641

A.6.3.2.1 Test Purpose and Environment 1641

A.6.3.2.2 Test Requirements 1643

A.6.3.3 Redirection from E-UTRAN FDD to GERAN when System Information is provided 1643

A.6.3.3.1 Test Purpose and Environment 1643

A.6.3.3.2 Test Requirements 1644

A.6.3.4 Redirection from E-UTRAN TDD to GERAN when System Information is provided 1645

A.6.3.4.1 Test Purpose and Environment 1645

A.6.3.4.2 Test Requirements 1646

A.6.3.5 E-UTRA TDD RRC connection release redirection to UTRA TDD 1647

A.6.3.5.1 Test Purpose and Environment 1647

A.6.3.5.2 Test Requirements 1649

A.6.3.6 E-UTRA FDD RRC connection release redirection to UTRA TDD 1649

A.6.3.6.1 Test Purpose and Environment 1649

A. 6.3.6.2 Test Requirements 1652

A.6.3.7 E-UTRA TDD RRC connection release redirection to UTRA TDD without SI provided 1652

A.6.3.7.1 Test Purpose and Environment 1652

A.6.3.7.2 Test Requirements 1655

A.6.3.8 E-UTRA FDD RRC connection release redirection to UTRA TDD without SI provided 1655

A.6.3.8.1 Test Purpose and Environment 1655

A.6.3.8.2 Test Requirements 1658

A.6.3.9 Redirection from E-UTRAN FDD to UTRAN FDD without System Information 1658

A.6.3.9.1 Test Purpose and Environment 1658

A.6.3.9.2 Test Requirements 1660

A.6.3.10 Redirection from E-UTRAN FDD to GERAN when System Information is not provided 1660

A.6.3.10.1 Test Purpose and Environment 1660

A.6.3.10.2 Test Requirements 1662

A.6.3.11 Redirection from E-UTRAN TDD to GERAN when System Information is not provided 1662

A.6.3.11.1 Test Purpose and Environment 1662

A.6.3.11.2 Test Requirements 1664

A.6.3.12 E-UTRAN TDD RRC connection release redirection to UTRAN FDD without SI provided 1664

A.6.3.12.1 Test Purpose and Environment 1664

A.6.3.12.2 Test Requirements 1667

A.6.3.13 Redirection from E-UTRA to NR FR1 for redcap UE 1667

A.6.3.13.1 Test Purpose and Environment 1667

A.6.3.13.2 Test Parameters 1667

A.6.3.13.3 Test Requirements 1671

A.7 Timing and Signalling Characteristics 1672

A.7.1 UE Transmit Timing 1672

A.7.1.1 E-UTRAN FDD – UE Transmit Timing Accuracy Tests 1672

A.7.1.1.1 Test Purpose and Environment 1672

A.7.1.1.2 Test Requirements 1673

A.7.1.2 E-UTRAN TDD - UE Transmit Timing Accuracy Tests 1674

A.7.1.2.1 Test Purpose and Environment 1674

A.7.1.2.2 Test Requirements 1676

A.7.1.3 E-UTRAN FDD – UE Transmit Timing Accuracy Tests for SCell 1677

A.7.1.3.1 Test Purpose and Environment 1677

A.7.1.3.2 Test Requirements 1679

A.7.1.4 E-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell 1680

A.7.1.4.1 Test Purpose and Environment 1680

A.7.1.4.2 Test Requirements 1681

A.7.1.4A E-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell for 20 MHz + 10 MHz 1682

A.7.1.4A.1 Test Purpose and Environment 1682

A.7.1.4A.2 Test Requirements 1682

A.7.1.5 E-UTRAN FDD – UE Transmit Timing Accuracy Tests for 5MHz Bandwidth 1682

A.7.1.5.1 Test Purpose and Environment 1682

A.7.1.5.2 Test Requirements 1683

A.7.1.6 E-UTRAN FDD – UE Transmit Timing Accuracy Tests for SCell in sTAG 1683

A.7.1.6.1 Test Purpose and Environment 1683

A.7.1.6.2 Test Requirements 1685

A.7.1.7 E-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell in sTAG 1686

A.7.1.7.1 Test Purpose and Environment 1686

A.7.1.7.2 Test Requirements 1687

A.7.1.7A E-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell in sTAG for 20MHz +20MHz 1688

A.7.1.7A.1 Test Purpose and Environment 1688

A.7.1.7A.2 Test Requirements 1688

A.7.1.7B E-UTRAN TDD - UE Transmit Timing Accuracy Tests for SCell in sTAG for 20MHz +10MHz 1688

A.7.1.7B.1 Test Purpose and Environment 1688

A.7.1.7B.2 Test Requirements 1688

A.7.1.8 Void 1689

A.7.1.8.1 Void 1689

A.7.1.8.2 Void 1689

A.7.1.9 Void 1689

A.7.1.9.1 Void 1689

A.7.1.9.2 Void 1689

A.7.1.10 E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA 1689

A.7.1.10.1 Test Purpose and Environment 1689

A.7.1.10.2 Test Requirements 1691

A.7.1.11 E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA 1691

A.7.1.11.1 Test Purpose and Environment 1691

A.7.1.11.2 Test Requirements 1693

A.7.1.12 E-UTRAN TDD - UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA 1693

A.7.1.12.1 Test Purpose and Environment 1693

A.7.1.12.2 Test Requirements 1695

A.7.1.13 3DL/3UL TDD CA UE Transmit Timing Accuracy Tests for 2 SCells 1695

A.7.1.13.1 Test Purpose and Environment 1695

A.7.1.13.2 Test Requirements 1697

A.7.1.14 E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB 1698

A.7.1.14.1 Test Purpose and Environment 1698

A.7.1.14.2 Test Requirements 1699

A.7.1.15 E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB 1699

A.7.1.15.1 Test Purpose and Environment 1699

A.7.1.15.2 Test Requirements 1700

A.7.1.16 E-UTRAN TDD - UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB 1701

A.7.1.16.1 Test Purpose and Environment 1701

A.7.1.16.2 Test Requirements 1702

A.7.1.17 E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Category NB1 UE In-Band mode under normal coverage 1703

A.7.1.17.1 Test Purpose and Environment 1703

A.7.1.17.2 Test Requirements 1705

A.7.1.18 E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Category NB1 UE In-band mode under enhanced coverage 1706

A.7.1.18.1 Test Purpose and Environment 1706

A.7.1.18.2 Test Requirements 1708

A.7.1.19 E-UTRAN FDD - UE Transmit Timing Accuracy Test for RACH-less Handover 1709

A.7.1.19.1 Test Purpose and Environment 1709

A.7.1.19.2 Test Requirements 1710

A.7.1.20 E-UTRAN TDD - UE Transmit Timing Accuracy Test for RACH-less Handover 1710

A.7.1.20.1 Test Purpose and Environment 1710

A.7.1.20.2 Test Requirements 1712

A.7.1.21 E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeA 1712

A.7.1.21.1 Test Purpose and Environment 1712

A.7.1.21.2 Test Requirements 1714

A.7.1.22 E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeA 1714

A.7.1.22.1 Test Purpose and Environment 1714

A.7.1.22.2 Test Requirements 1716

A.7.1.23 E-UTRAN TDD - UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeA 1716

A.7.1.23.1 Test Purpose and Environment 1716

A.7.1.23.2 Test Requirements 1718

A.7.1.24 E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeB 1718

A.7.1.24.1 Test Purpose and Environment 1718

A.7.1.24.2 Test Requirements 1719

A.7.1.25 E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeB 1720

A.7.1.25.1 Test Purpose and Environment 1720

A.7.1.25.2 Test Requirements 1721

A.7.1.26 E-UTRAN TDD - UE Transmit Timing Accuracy Tests for Cat-M2 UE in CEModeB 1722

A.7.1.26.1 Test Purpose and Environment 1722

A.7.1.26.2 Test Requirements 1723

A.7.1.27 E-UTRAN TDD – UE Transmit Timing Accuracy Tests for Category NB1 UE In-Band mode under normal coverage 1724

A.7.1.27.1 Test Purpose and Environment 1724

A.7.1.27.2 Test Requirements 1726

A.7.1.28 E-UTRAN TDD – UE Transmit Timing Accuracy Tests for Category NB1 UE In-band mode under enhanced coverage 1726

A.7.1.28.1 Test Purpose and Environment 1726

A.7.1.28.2 Test Requirements 1728

A.7.2 UE Timing Advance 1729

A.7.2.1 E-UTRAN FDD – UE Timing Advance Adjustment Accuracy Test 1729

A.7.2.1.1 Test Purpose and Environment 1729

A.7.2.1.2 Test Requirements 1730

A.7.2.2 E-UTRAN TDD – UE Timing Advance Adjustment Accuracy Test 1731

A.7.2.2.1 Test Purpose and Environment 1731

A.7.2.2.2 Test Requirements 1733

A.7.2.3 E-UTRAN FDD – UE Timing Advance Adjustment Accuracy Test for 5MHz 1733

A.7.2.3.1 Test Purpose and Environment 1733

A.7.2.3.2 Test Requirements 1733

A.7.2.4 E-UTRAN FDD – UE Timing Advance Adjustment Accuracy Test for SCell in sTAG 1733

A.7.2.4.1 Test Purpose and Environment 1733

A.7.2.4.2 Test Requirements 1736

A.7.2.5 E-UTRAN TDD – UE Timing Advance Adjustment Accuracy Test for Scell in sTAG 1736

A.7.2.5.1 Test Purpose and Environment 1736

A.7.2.5.2 Test Requirements 1738

A.7.2.5A E-UTRAN TDD – UE Timing Advance Adjustment Accuracy Test for Scell in sTAG for 20 MHz +20 MHz 1738

A.7.2.5A.1 Test Purpose and Environment 1738

A.7.2.5A.2 Test Requirements 1739

A.7.2.5B E-UTRAN TDD – UE Timing Advance Adjustment Accuracy Test for Scell in sTAG for 20 MHz +10 MHz 1739

A.7.2.5B.1 Test Purpose and Environment 1739

A.7.2.5B.2 Test Requirements 1739

A.7.2.6 E-UTRAN FDD Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA 1739

A.7.2.6.1 Test Purpose and Environment 1739

A.7.2.6.2 Test Requirements 1742

A.7.2.7 E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA 1742

A.7.2.7.1 Test Purpose and Environment 1742

A.7.2.7.2 Test Requirements 1744

A.7.2.8 E-UTRAN TDD Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA 1744

A.7.2.8.1 Test Purpose and Environment 1744

A.7.2.8.2 Test Requirements 1746

A.7.2.9.2 Test Requirements 1747

A.7.2.10 E-UTRAN FDD UE Timing Advance Adjustment Accuracy Test in CEModeB 1748

A.7.2.10.1 Test Purpose and Environment 1748

A.7.2.10.2 Test Requirements 1749

A.7.2.11 E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test in CEModeB 1749

A.7.2.11.1 Test Purpose and Environment 1749

A.7.2.11.2 Test Requirements 1751

A.7.2.12 E-UTRAN TDD UE Timing Advance Adjustment Accuracy Test in CEModeB 1751

A.7.2.12.1 Test Purpose and Environment 1751

A.7.2.12.2 Test Requirements 1753

A.7.2.13 E-UTRAN FDD – UE Timing Advance Adjustment delay Test for sTTI and ShortProcessingTime=TRUE 1754

A.7.2.13.1 Test Purpose and Environment 1754

A.7.2.13.2 Test Requirements 1755

A.7.2.14 E-UTRAN TDD – UE Timing Advance Adjustment delay Test for sTTI and ShortProcessingTime=TRUE 1756

A.7.2.14.1 Test Purpose and Environment 1756

A.7.2.14.2 Test Requirements 1758

A.7.2.15 E-UTRAN TDD – TDD UE Timing Advance Adjustment Accuracy Test for UE Category NB1 in Standalone Mode under Enhanced Coverage 1758

A.7.2.15.1 Test Purpose and Environment 1758

A.7.2.15.2 Test Requirements 1760

A.7.3 Radio Link Monitoring 1760

A.7.3.1 E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync 1760

A.7.3.1.1 Test Purpose and Environment 1760

A.7.3.1.2 Test Requirements 1764

A.7.3.2 E-UTRAN FDD Radio Link Monitoring Test for In-sync 1764

A.7.3.2.1 Test Purpose and Environment 1764

A.7.3.2.2 Test Requirements 1768

A.7.3.3 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync 1768

A.7.3.3.1 Test Purpose and Environment 1768

A.7.3.3.2 Test Requirements 1772

A.7.3.4 E-UTRAN TDD Radio Link Monitoring Test for In-sync 1772

A.7.3.4.1 Test Purpose and Environment 1772

A.7.3.4.2 Test Requirements 1776

A.7.3.5 E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync in DRX 1776

A.7.3.5.1 Test Purpose and Environment 1776

A.7.3.5.2 Test Requirements 1779

A.7.3.6 E-UTRAN FDD Radio Link Monitoring Test for In-sync in DRX 1780

A.7.3.6.1 Test Purpose and Environment 1780

A.7.3.6.2 Test Requirements 1783

A.7.3.7 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync in DRX 1783

A.7.3.7.1 Test Purpose and Environment 1783

A.7.3.7.2 Test Requirements 1786

A.7.3.8 E-UTRAN TDD Radio Link Monitoring Test for In-sync in DRX 1786

A.7.3.8.1 Test Purpose and Environment 1786

A.7.3.8.2 Test Requirements 1789

A.7.3.9 E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction and Non-MBSFN ABS 1789

A.7.3.9.2 Test Requirements 1792

A.7.3.10 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with Non-MBSFN ABS 1792

A.7.3.10.1 Test Purpose and Environment 1792

A.7.3.11 E-UTRAN FDD Radio Link Monitoring Test for In-sync for Non-MBSFN ABS 1796

A.7.3.11.1 Test Purpose and Environment 1796

A.7.3.11.2 Test Requirements 1801

A.7.3.12 E-UTRAN TDD Radio Link Monitoring Test for In-sync for Non-MBSFN ABS 1801

A.7.3.12.1 Test Purpose and Environment 1801

A.7.3.12.2 Test Requirements 1806

A.7.3.13 E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with MBSFN ABS 1806

A.7.3.13.1 Test Purpose and Environment 1806

A.7.3.13.2 Test Requirements 1809

A.7.3.14 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with MBSFN ABS 1809

A.7.3.14.1 Test Purpose and Environment 1809

A.7.3.14.2 Test Requirements 1812

A.7.3.15 E-UTRAN FDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resource Restriction with MBSFN ABS 1812

A.7.3.15.1 Test Purpose and Environment 1812

A.7.3.15.2 Test Requirements 1816

A.7.3.16 E-UTRAN TDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resource Restriction with MBSFN ABS 1816

A.7.3.16.1 Test Purpose and Environment 1816

A.7.3.16.2 Test Requirements 1821

A.7.3.17 E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS 1821

A.7.3.17.1 Test Purpose and Environment 1821

A.7.3.17.2 Test Requirements 1825

A.7.3.18 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS 1825

A.7.3.18.1 Test Purpose and Environment 1825

A.7.3.18.2 Test Requirements 1829

A.7.3.19 E-UTRAN FDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resouce Restriction with CRS assistance information and Non-MBSFN ABS 1829

A.7.3.19.1 Test Purpose and Environment 1829

A.7.3.19.2 Test Requirements 1834

A.7.3.20 E-UTRAN TDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resouce Restriction with CRS assistance information and Non-MBSFN ABS 1834

A.7.3.20.1 Test Purpose and Environment 1834

A.7.3.20.2 Test Requirements 1839

A.7.3.21 E-UTRAN FDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resouce Restriction with CRS assistance information and MBSFN ABS 1839

A.7.3.21.1 Test Purpose and Environment 1839

A.7.3.21.2 Test Requirements 1844

A.7.3.22 E-UTRAN TDD Radio Link Monitoring Test for In-sync under Time Domain Measurement Resouce Restriction with CRS assistance information and MBSFN ABS 1844

A.7.3.22.1 Test Purpose and Environment 1844

A.7.3.22.2 Test Requirements 1849

A.7.3.23 E-UTRAN FDD Radio Link Monitoring Test for Out-of-sync for 5MHz Bandwidth 1849

A.7.3.23.1 Test Purpose and Environment 1849

A.7.3.23.2 Test Requirements 1850

A.7.3.24 E-UTRAN FDD Radio Link Monitoring Test for In-sync for 5MHz Bandwidth 1850

A.7.3.24.1 Test Purpose and Environment 1850

A.7.3.24.2 Test Requirements 1851

A.7.3.25 E-UTRAN FDD Radio Link Monitoring Test for In-sync in DRX for 5MHz Bandwidth 1851

A.7.3.25.1 Test Purpose and Environment 1851

A.7.3.25.2 Test Requirements 1852

A.7.3.26 E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for UE Category 0 1852

A.7.3.26.1 Test Purpose and Environment 1852

A.7.3.26.2 Test Requirements 1855

A.7.3.27 E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync for UE Category 0 1855

A.7.3.27.1 Test Purpose and Environment 1855

A.7.3.27.2 Test Requirements 1858

A.7.3.28 E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category 0 1858

A.7.3.28.1 Test Purpose and Environment 1858

A.7.3.28.2 Test Requirements 1861

A.7.3.29 E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category 0 1861

A.7.3.29.1 Test Purpose and Environment 1861

A.7.3.29.2 Test Requirements 1864

A.7.3.30 E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync for UE Category 0 1864

A.7.3.30.1 Test Purpose and Environment 1864

A.7.3.30.2 Test Requirements 1867

A.7.3.31 E-UTRAN HD-FDD Radio Link Monitoring Test for In-sync for UE Category 0 1867

A.7.3.31.1 Test Purpose and Environment 1867

A.7.3.31.2 Test Requirements 1870

A.7.3.32 E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category 0 1870

A.7.3.32.1 Test Purpose and Environment 1870

A.7.3.32.2 Test Requirements 1873

A.7.3.33 E-UTRAN HD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category 0 1873

A.7.3.33.1 Test Purpose and Environment 1873

A.7.3.33.2 Test Requirements 1876

A.7.3.34 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync for UE Category 0 1876

A.7.3.34.1 Test Purpose and Environment 1876

A.7.3.34.2 Test Requirements 1879

A.7.3.35 E-UTRAN TDD Radio Link Monitoring Test for In-sync for UE category 0 1879

A.7.3.35.1 Test Purpose and Environment 1879

A.7.3.35.2 Test Requirements 1882

A.7.3.36 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category 0 1882

A.7.3.36.1 Test Purpose and Environment 1882

A.7.3.36.2 Test Requirements 1885

A.7.3.37 E-UTRAN TDD Radio Link Monitoring Test for In-sync in DRX for UE category 0 1885

A.7.3.37.1 Test Purpose and Environment 1885

A.7.3.37.2 Test Requirements 1888

A.7.3.38 E-UTRAN FDD-FDD DC Radio Link Monitoring Test for Out-of-sync in DRX in synchronous DC 1888

A.7.3.38.1 Test Purpose and Environment 1888

A.7.3.38.2 Test Requirements 1891

A.7.3.39 E-UTRAN FDD-FDD DC Radio Link Monitoring Test for Out-of-sync in DRX in asynchronous DC 1891

A.7.3.39.1 Test Purpose and Environment 1891

A.7.3.39.2 Test Requirements 1894

A.7.3.40 E-UTRAN TDD-TDD DC Radio Link Monitoring Test for Out-of-sync in DRX in synchronous DC 1895

A.7.3.40.1 Test Purpose and Environment 1895

A.7.3.40.2 Test Requirements 1897

A.7.3.41 E-UTRAN FDD-FDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity 1898

A.7.3.41.1 Test Purpose and Environment 1898

A.7.3.41.2 Test Requirements 1901

A.7.3.42 E-UTRAN FDD-FDD DC Radio Link Monitoring Test for In-sync in DRX in asynchronous DC 1901

A.7.3.42.1 Test Purpose and Environment 1901

A.7.3.42.2 Test Requirements 1904

A.7.3.43 E-UTRAN TDD-TDD Radio Link Monitoring Test for In-sync in DRX in synchronous dual connectivity 1904

A.7.3.43.1 Test Purpose and Environment 1904

A.7.3.43.2 Test Requirements 1907

A.7.3.44 E-UTRAN TDD-FDD DC Radio Link Monitoring Test for Out-of-sync in DRX in synchronous DC with PCell in FDD 1907

A.7.3.44.1 Test Purpose and Environment 1907

A.7.3.44.2 Test Requirements 1910

A.7.3.45 E-UTRAN TDD-FDD DC Radio Link Monitoring Test for Out-of-sync in DRX in synchronous DC with PCell in TDD 1911

A.7.3.45.1 Test Purpose and Environment 1911

A.7.3.45.2 Test Requirements 1913

A.7.3.46 E-UTRAN TDD-FDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in FDD 1914

A.7.3.46.1 Test Purpose and Environment 1914

A.7.3.46.2 Test Requirements 1917

A.7.3.47 E-UTRAN TDD-FDD Radio Link Monitoring Test for In-sync in DRX for PSCell in synchronous DC with PCell in TDD 1917

A.7.3.47.1 Test Purpose and Environment 1917

A.7.3.47.2 Test Requirements 1920

A.7.3.48 E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A 1920

A.7.3.48.1 Test Purpose and Environment 1920

A.7.3.48.2 Test Requirements 1923

A.7.3.49 E-UTRAN FD-FDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A 1923

A.7.3.49.1 Test Purpose and Environment 1923

A.7.3.49.2 Test Requirements 1926

A.7.3.50 E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A 1926

A.7.3.50.1 Test Purpose and Environment 1926

A.7.3.50.2 Test Requirements 1929

A.7.3.51 E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A 1929

A.7.3.51.1 Test Purpose and Environment 1929

A.7.3.51.2 Test Requirements 1932

A.7.3.52 E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A 1932

A.7.3.52.1 Test Purpose and Environment 1932

A.7.3.52.2 Test Requirements 1935

A.7.3.53 E-UTRAN HD-FDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A 1935

A.7.3.53.1 Test Purpose and Environment 1935

A.7.3.53.2 Test Requirements 1938

A.7.3.54 E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A 1938

A.7.3.54.1 Test Purpose and Environment 1938

A.7.3.54.2 Test Requirements 1941

A.7.3.55 E-UTRAN HD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A 1941

A.7.3.55.1 Test Purpose and Environment 1941

A.7.3.55.2 Test Requirements 1944

A.7.3.56 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A 1944

A.7.3.56.1 Test Purpose and Environment 1944

A.7.3.56.2 Test Requirements 1947

A.7.3.57 E-UTRAN TDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A 1947

A.7.3.57.1 Test Purpose and Environment 1947

A.7.3.57.2 Test Requirements 1950

A.7.3.58 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A 1950

A.7.3.58.1 Test Purpose and Environment 1950

A.7.3.58.2 Test Requirements 1953

A.7.3.59 E-UTRAN TDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A 1953

A.7.3.59.1 Test Purpose and Environment 1953

A.7.3.59.2 Test Requirements 1956

A.7.3.60 HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in normal coverage 1956

A.7.3.60.1 Test Purpose and Environment 1956

A.7.3.60.2 Test Requirements 1960

A.7.3.61 HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage 1960

A.7.3.61.1 Test Purpose and Environment 1960

A.7.3.61.2 Test Requirements 1964

A.7.3.62 HD-FDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 In-Band mode in Enhanced Coverage 1964

A.7.3.62.1 Test Purpose and Environment 1964

A.7.3.62.2 Test Requirements 1968

A.7.3.63 HD-FDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 In-Band mode in Normal Coverage 1968

A.7.3.63.1 Test Purpose and Environment 1968

A.7.3.63.2 Test Requirements 1972

A.7.3.64 HD-FDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 In-Band mode in Normal Coverage 1972

A.7.3.64.1 Test Purpose and Environment 1972

A.7.3.64.2 Test Requirements 1975

A.7.3.65 HD-FDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 In-Band mode in Enhanced Coverage 1976

A.7.3.65.1 Test Purpose and Environment 1976

A.7.3.65.2 Test Requirements 1979

A.7.3.66 HD-FDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 Standalone mode in Normal Coverage 1980

A.7.3.66.1 Test Purpose and Environment 1980

A.7.3.66.2 Test Requirements 1982

A.7.3.67 HD-FDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 guard band mode in Enhanced Coverage 1983

A.7.3.67.1 Test Purpose and Environment 1983

A.7.3.67.2 Test Requirements 1986

A.7.3.68 E-UTRAN FD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEMode A 1987

A.7.3.68.1 Test Purpose and Environment 1987

A.7.3.68.2 Test Requirements 1989

A.7.3.69 E-UTRAN HD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEMode A 1989

A.7.3.69.1 Test Purpose and Environment 1989

A.7.3.69.2 Test Requirements 1991

A.7.3.70 E-UTRAN TDD Early Out-of-sync reporting Test for Cat-M1 UE in CEMode A 1991

A.7.3.70.1 Test Purpose and Environment 1991

A.7.3.70.2 Test Requirements 1993

A.7.3.71 E-UTRAN FD-FDD Early In-Sync reporting Test for Cat-M1 UE in CEModeA 1993

A.7.3.71.1 Test Purpose and Environment 1993

A.7.3.71.2 Test Requirements 1996

A.7.3.72 E-UTRAN HD-FDD Early In-Sync reporting Test for Cat-M1 UE in CEModeA 1996

A.7.3.72.1 Test Purpose and Environment 1996

A.7.3.72.2 Test Requirements 1998

A.7.3.73 E-UTRAN TDD Early In-Sync reporting Test for Cat-M1 UE in CEModeA 1998

A.7.3.73.1 Test Purpose and Environment 1998

A.7.3.73.2 Test Requirements 2000

A.7.3.74 E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for non-BL CE UE in CEMode A 2000

A.7.3.74.1 Test Purpose and Environment 2000

A.7.3.74.2 Test Requirements 2003

A.7.3.75 E-UTRAN FD-FDD Radio Link Monitoring Test for In-Sync for non-BL CE UE in CEMode A 2003

A.7.3.75.1 Test Purpose and Environment 2003

A.7.3.75.2 Test Requirements 2005

A.7.3.76 E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for non-BL CE UE configured in CEMode A 2006

A.7.3.76.1 Test Purpose and Environment 2006

A.7.3.76.2 Test Requirements 2009

A.7.3.77 E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync in DRX for non-BL CE UE configured in CEMode A 2009

A.7.3.77.1 Test Purpose and Environment 2009

A.7.3.77.2 Test Requirements 2012

A.7.3.78 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync for non-BL CE UE in CEMode A 2012

A.7.3.78.1 Test Purpose and Environment 2012

A.7.3.78.2 Test Requirements 2015

A.7.3.79 E-UTRAN TDD Radio Link Monitoring Test for In-Sync for non-BL CE UE in CEMode A 2015

A.7.3.79.1 Test Purpose and Environment 2015

A.7.3.79.2 Test Requirements 2018

A.7.3.80 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync in DRX for non-BL CE UE configured in CEMode A 2018

A.7.3.80.1 Test Purpose and Environment 2018

A.7.3.80.2 Test Requirements 2021

A.7.3.81 E-UTRAN TDD Radio Link Monitoring Test for In-sync in DRX for non-BL CE UE configured in CEMode A 2021

A.7.3.81.1 Test Purpose and Environment 2021

A.7.3.81.2 Test Requirements 2024

A.7.3.82 E-UTRAN FD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB 2024

A.7.3.82.1 Test Purpose and Environment 2024

A.7.3.82.2 Test Requirements 2027

A.7.3.83 E-UTRAN FD-FDD Early In-Sync reporting Test for Cat-M1 UE in CEModeB 2027

A.7.3.83.1 Test Purpose and Environment 2027

A.7.3.83.2 Test Requirements 2028

A.7.3.84 E-UTRAN HD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB 2029

A.7.3.84.1 Test Purpose and Environment 2029

A.7.3.84.2 Test Requirements 2031

A.7.3.85 E-UTRAN HD-FDD Early In-Sync reporting Test for Cat-M1 UE in CEModeB 2031

A.7.3.85.1 Test Purpose and Environment 2031

A.7.3.85.2 Test Requirements 2032

A.7.3.86 E-UTRAN TDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB 2033

A.7.3.86.1 Test Purpose and Environment 2033

A.7.3.86.2 Test Requirements 2035

A.7.3.87 E-UTRAN TDD Early In-Sync reporting Test for Cat-M1 UE in CEModeB 2035

A.7.3.87.1 Test Purpose and Environment 2035

A.7.3.87.2 Test Requirements 2037

A.7.3.88 TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in normal coverage 2038

A.7.3.88.1 Test Purpose and Environment 2038

A.7.3.88.2 Test Requirements 2042

A.7.3.89 TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 In-band mode in enhanced coverage 2042

A.7.3.89.1 Test Purpose and Environment 2042

A.7.3.89.2 Test Requirements 2046

A.7.3.90 TDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 In-Band mode in Normal Coverage 2046

A.7.3.90.1 Test Purpose and Environment 2046

A.7.3.90.2 Test Requirements 2050

A.7.3.91 TDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 In-Band mode in Enhanced Coverage 2050

A.7.3.91.1 Test Purpose and Environment 2050

A.7.3.91.2 Test Requirements 2054

A.7.3.92 TDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 In-Band mode in Normal Coverage 2054

A.7.3.92.1 Test Purpose and Environment 2054

A.7.3.92.2 Test Requirements 2057

A.7.3.93 TDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 In-Band mode in Enhanced Coverage 2058

A.7.3.93.1 Test Purpose and Environment 2058

A.7.3.93.2 Test Requirements 2061

A.7.3.94 TDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 Standalone mode in Normal Coverage 2062

A.7.3.94.1 Test Purpose and Environment 2062

A.7.3.94.2 Test Requirements 2064

A.7.3.95 TDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 guard band mode in Enhanced Coverage 2065

A.7.3.95.1 Test Purpose and Environment 2065

A.7.3.95.2 Test Requirements 2068

A.7.3.96 E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for MPDCCH performance improvement 2069

A.7.3.96.1 Test Purpose and Environment 2069

A.7.3.97 E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for MPDCCH performance improvement 2070

A.7.3.97.1 Test Purpose and Environment 2070

A.7.3.97.2 Test Requirements 2073

A.7.3.98 E-UTRAN TDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for MPDCCH performance improvement 2073

A.7.3.98.1 Test Purpose and Environment 2073

A.7.3.98.2 Test Requirements 2076

A.7.3.99 E-UTRAN FD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB for MPDCCH performance improvement 2076

A.7.3.99.1 Test Purpose and Environment 2076

A.7.3.99.2 Test Requirements 2079

A.7.3.100 E-UTRAN HD-FDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB for MPDCCH performance improvement 2079

A.7.3.100.1 Test Purpose and Environment 2079

A.7.3.100.2 Test Requirements 2081

A.7.3.101 E-UTRAN TDD Early Out-of-sync reporting Test for Cat-M1 UE in CEModeB for MPDCCH performance improvement 2081

A.7.3.101.1 Test Purpose and Environment 2081

A.7.3.101.2 Test Requirements 2083

A.7.4 Interruption for Dual Connectivity 2083

A.7.4.1 E-UTRAN FDD-FDD DC interruption at transitions between active and non-active during DRX in synchronous DC 2083

A.7.4.1.1 Test Purpose and Environment 2083

A.7.4.1.2 Test Requirements 2086

A.7.4.2 E-UTRAN TDD-TDD DC interruption at transitions between active and non-active during DRX in synchronous DC 2086

A.7.4.2.1 Test Purpose and Environment 2086

A.7.4.2.2 Test Requirements 2088

A.7.4.3 E-UTRAN FDD-FDD Interruption at transitions between active and non-active during DRX in asynchronous dual connectivity 2088

A.7.4.3.1 Test Purpose and Environment 2088

A.7.4.3.2 Test Requirements 2090

A.7.4.4 E-UTRAN FDD-TDD DC interruption at transitions between active and non-active during DRX in synchronous DC 2090

A.7.4.4.1 Test Purpose and Environment 2090

A.7.4.4.2 Test Requirements 2093

A.7.4.5 E-UTRAN TDD-FDD DC interruption at transitions between active and non-active during DRX in synchronous DC 2093

A.7.4.5.1 Test Purpose and Environment 2093

A.7.4.5.2 Test Requirements 2095

A.7.4.6 E-UTRAN FDD-TDD DC interruption at SRS carrier based switching 2095

A.7.4.6.1 Test Purpose and Environment 2095

A.7.4.6.2 Test Requirements 2097

A.7.4.7 E-UTRAN TDD-TDD DC interruption at SRS carrier based switching 2097

A.7.4.7.1 Test Purpose and Environment 2097

A.7.4.7.2 Test Requirements 2101

A.7.5 Proximity-based Services 2101

A.7.5.1 E-UTRAN FDD – UE ProSe Direct Discovery Transmission Timing Accuracy Test 2101

A.7.5.1.1 Test Purpose and Environment 2101

A.7.5.1.2 Test Requirements 2102

A.7.5.2 E-UTRAN TDD – UE ProSe Direct Discovery Transmission Timing Accuracy Test 2103

A.7.5.2.1 Test Purpose and Environment 2103

A.7.5.1.2 Test Requirements 2103

A.7.5.3 E-UTRAN FDD - Interruptions due to ProSe Direct Discovery 2104

A.7.5.3.1 Test Purpose and Environment 2104

A.7.5.3.2 Test Requirements 2105

A.7.5.4 E-UTRAN FDD – UE ProSe Direct Communication Transmission Timing Accuracy Test 2106

A.7.5.4.1 Test Purpose and Environment 2106

A.7.5.4.2 Test Requirements 2107

A.7.5.5 E-UTRAN FDD - Interruptions due to ProSe Direct Communication 2108

A.7.5.5.1 Test Purpose and Environment 2108

A.7.5.5.2 Test Requirements 2110

A.7.5.6 E-UTRAN FDD - Interruptions due to ProSe Direct Discovery with discovery period less than 320ms 2111

A.7.5.6.1 Test Purpose and Environment 2111

A.7.5.6.2 Test Requirements 2112

A.7.5.7 E-UTRAN FDD-FDD - Interruptions due to ProSe Direct Discovery 2113

A.7.5.7.1 Test Purpose and Environment 2113

A.7.5.7.2 Test Requirements 2115

A.7.5.8 E-UTRAN FDD-FDD - Cell reselection and timing accuracy for ProSe Direct Discovery transmission on non-serving frequency 2115

A.7.5.8.1 Test Purpose and Environment 2115

A.7.5.8.2 Test Requirements 2117

A.7.5.9 E-UTRAN FDD-FDD - Interruptions due to ProSe Direct Discovery reception on non-serving frequency 2118

A.7.5.9.1 Test Purpose and Environment 2118

A.7.5.9.2 Test Requirements 2120

A.7.5.10 E-UTRAN FDD-FDD - Interruptions due to ProSe Direct Discovery transmission on non-serving frequency 2121

A.7.5.10.1 Test Purpose and Environment 2121

A.7.5.10.2 Test Requirements 2123

A.7.5.11 E-UTRAN FDD-FDD - Interruptions due to ProSe Direct Communication on non-serving frequency 2124

A.7.5.11.1 Test Purpose and Environment 2124

A.7.5.11.2 Test Requirements 2126

A.7.5.12 E-UTRAN FDD - Selection / Reselection of ProSe relay UE 2126

A.7.5.12.1 Test Purpose and Environment 2126

A.7.5.12.2 Test Requirements 2130

A.7.6 Interruption for carrier aggregation 2131

A.7.6.1 E-UTRAN FDD-TDD CA interruption at SRS carrier based switching 2131

A.7.6.1.1 Test Purpose and Environment 2131

A.7.6.1.2 Test Requirements 2134

A.7.6.2 E-UTRAN TDD-TDD CA interruption at SRS carrier based switching 2134

A.7.6.2.1 Test Purpose and Environment 2134

A.7.6.2.2 Test Requirements 2137

A.8 UE Measurements Procedures 2138

A.8.1 E-UTRAN FDD Intra-frequency Measurements 2138

A.8.1.1 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells 2138

A.8.1.1.1 Test Purpose and Environment 2138

A.8.1.1.2 Test Requirements 2139

A.8.1.2 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells 2140

A.8.1.2.1 Test Purpose and Environment 2140

A.8.1.2.2 Test Requirements 2141

A.8.1.3 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells with DRX 2142

A.8.1.3.1 Test Purpose and Environment 2142

A.8.1.3.2 Test Requirements 2144

A.8.1.4 Void 2144

A.8.1.5 E-UTRAN FDD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps 2144

A.8.1.5.1 Test Purpose and Environment 2144

A.8.1.5.2 Test Requirements 2146

A.8.1.6 E-UTRAN FDD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX 2146

A.8.1.6.1 Test Purpose and Environment 2146

A.8.1.6.2 Test Requirements 2148

A.8.1.7  E-UTRAN FDD-FDD Intra-Frequency Event-Triggered Reporting under Time Domain Measurement Resource Restriction with Non-MBSFN ABS 2148

A.8.1.7.1 Test Purpose and Environment 2148

A.8.1.7.2 Test Requirements 2150

A.8.1.8 E-UTRAN FDD-FDD Intra-Frequency Event-Triggered Reporting under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS 2151

A.8.1.8.1 Test Purpose and Environment 2151

A.8.1.8.2 Test Requirements 2153

A.8.1.9 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for 5MHz bandwidth 2154

A.8.1.9.1 Test Purpose and Environment 2154

A.8.1.9.2 Test Requirements 2154

A.8.1.10 E-UTRAN FDD-FDD Intra-Frequency Event Triggered Reporting under Fading Propagation Conditions in Synchronous Cells with DRX for 5 MHz Bandwidth 2154

A.8.1.10.1 Test Purpose and Environment 2154

A.8.1.10.2 Test Requirements 2155

A.8.1.11 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category 0 2155

A.8.1.11.1 Test Purpose and Environment 2155

A.8.1.11.2 Test Requirements 2157

A.8.1.12 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for UE category 0 2158

A.8.1.12.1 Test Purpose and Environment 2158

A.8.1.12.2 Test Requirements 2159

A.8.1.13 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells with DRX for UE category 0 2160

A.8.1.13.1 Test Purpose and Environment 2160

A.8.1.13.2 Test Requirements 2162

A.8.1.14 E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category 0 2162

A.8.1.14.1 Test Purpose and Environment 2162

A.8.1.14.2 Test Requirements 2164

A.8.1.15 E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for UE category 0 2165

A.8.1.15.1 Test Purpose and Environment 2165

A.8.1.15.2 Test Requirements 2166

A.8.1.16 E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells with DRX for UE category 0 2167

A.8.1.16.1 Test Purpose and Environment 2167

A.8.1.16.2 Test Requirements 2169

A.8.1.17 Void 2169

A.8.1.18 Void 2169

A.8.1.19 E-UTRAN FDD-FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps for UE category 0 2169

A.8.1.19.1 Test Purpose and Environment 2169

A.8.1.19.2 Test Requirements 2171

A.8.1.20 E-UTRAN FDD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX for UE category 0 2172

A.8.1.20.1 Test Purpose and Environment 2172

A.8.1.20.2 Test Requirements 2174

A.8.1.21 E-UTRAN HD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps for UE category 0 2174

A.8.1.21.1 Test Purpose and Environment 2174

A.8.1.21.2 Test Requirements 2176

A.8.1.22 E-UTRAN HD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX for UE category 0 2177

A.8.1.22.1 Test Purpose and Environment 2177

A.8.1.22.2 Test Requirements 2179

A.8.1.23 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for Cat-M1 UE in CEModeA 2179

A.8.1.23.1 Test Purpose and Environment 2179

A.8.1.23.2 Test Requirements 2180

A.8.1.24 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeA 2181

A.8.1.24.1 Test Purpose and Environment 2181

A.8.1.24.2 Test Requirements 2183

A.8.1.25 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeA in DRX 2183

A.8.1.25.1 Test Purpose and Environment 2183

A.8.1.25.2 Test Requirements 2185

A.8.1.26 E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for Cat-M1 UE in CEModeA 2185

A.8.1.26.1 Test Purpose and Environment 2185

A.8.1.27 E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeA 2188

A.8.1.27.1 Test Purpose and Environment 2188

A.8.1.27.2 Test Requirements 2190

A.8.1.28 E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeA in DRX 2190

A.8.1.28.1 Test Purpose and Environment 2190

A.8.1.28.2 Test Requirements 2192

A.8.1.29 E-UTRAN TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeA 2192

A.8.1.29.1 Test Purpose and Environment 2192

A.8.1.29.2 Test Requirements 2194

A.8.1.30 E-UTRAN TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeA in DRX 2195

A.8.1.30.1 Test Purpose and Environment 2195

A.8.1.30.2 Test Requirements 2197

A.8.1.31 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for Cat-M1 UE in CEModeB 2197

A.8.1.31.1 Test Purpose and Environment 2197

A.8.1.31.2 Test Requirements 2199

A.8.1.32 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeB 2200

A.8.1.32.1 Test Purpose and Environment 2200

A.8.1.32.2 Test Requirements 2201

A.8.1.33 E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in asynchronous cells for Cat-M1 UE in CEModeB 2202

A.8.1.33.1 Test Purpose and Environment 2202

A.8.1.33.2 Test Requirements 2203

A.8.1.34 E-UTRAN HD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeB 2204

A.8.1.34.1 Test Purpose and Environment 2204

A.8.1.34.2 Test Requirements 2205

A.8.1.35 E-UTRAN TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for Cat-M1 UE in CEModeB 2206

A.8.1.35.1 Test Purpose and Environment 2206

A.8.1.35.2 Test Requirements 2207

A.8.1.36 E-UTRAN FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps for Cat-M1 UE in CEModeB 2208

A.8.1.36.1 Test Purpose and Environment 2208

A.8.1.36.2 Test Requirements 2209

A.8.1.37 E-UTRAN FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX for Cat-M1 UE in CEModeB 2210

A.8.1.37.1 Test Purpose and Environment 2210

A.8.1.37.2 Test Requirements 2212

A.8.1.38 E-UTRAN HD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps for Cat-M1 UE in CEModeB 2212

A.8.1.38.1 Test Purpose and Environment 2212

A.8.1.38.2 Test Requirements 2213

A.8.1.39 E-UTRAN HD - FDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX for Cat-M1 UE in CEModeB 2214

A.8.1.39.1 Test Purpose and Environment 2214

A.8.1.39.2 Test Requirements 2216

A.8.1.40 E-UTRAN FDD-FDD intra-frequency event triggered reporting with DRX for UE configured with highSpeedEnhancedMeasFlag 2216

A.8.1.40.1 Test Purpose and Environment 2216

A.8.1.40.2 Test Requirements 2218

A.8.1.41 E-UTRAN FDD intra-frequency event triggered reporting for serving cell under fading propagation conditions for UE category M1 in CEModeA without gap 2218

A.8.1.41.1 Test Purpose and Environment 2218

A.8.1.41.2 Test Requirement 2220

A.8.1.42 E-UTRAN HD-FDD intra-frequency event triggered reporting for serving cell under fading propagation conditions for UE category M1 in CEModeA without gap 2220

A.8.1.42.1 Test Purpose and Environment 2220

A.8.1.42.2 Test Requirement 2221

A.8.1.43 E-UTRAN FDD-FDD intra-frequency event triggered reporting with DRX for UE configured with highSpeedEnhMeasFlag2-r16 2221

A.8.1.43.1 Test Purpose and Environment 2221

A.8.1.43.2 Test Requirements 2224

A.8.1.44 HD-FDD Intra-frequency neighbour cell measurement for UE category NB1 in In-Band mode under normal coverage 2224

A.8.1.44.1 Test Purpose and Environment 2224

A.8.1.44.2 Test Requirements 2227

A.8.1.45 HD-FDD Intra-frequency neighbour cell measurement for UE category NB1 in guard-band mode under normal coverage 2228

A.8.1.45.1 Test Purpose and Environment 2228

A.8.1.45.2 Test Requirements 2230

A.8.1.46 HD-FDD Intra-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage 2231

A.8.1.46.1 Test Purpose and Environment 2231

A.8.1.46.2 Test Requirements 2232

A.8.1.47 TDD Intra-frequency neighbour cell measurement for UE category NB1 in In-Band mode under normal coverage 2233

A.8.1.47.1 Test Purpose and Environment 2233

A.8.1.47.2 Test Requirements 2235

A.8.1.48 TDD Intra-frequency neighbour cell measurement for UE category NB1 in guard-band mode under normal coverage 2236

A.8.1.48.1 Test Purpose and Environment 2236

A.8.1.48.2 Test Requirements 2238

A.8.1.49 TDD Intra-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage 2239

A.8.1.49.1 Test Purpose and Environment 2239

A.8.1.49.2 Test Requirements 2240

A.8.150 HD-FDD Inter-frequency neighbour cell measurement for UE category NB1 in In-Band mode under normal coverage 2241

A.8.1.50.1 Test Purpose and Environment 2241

A.8.1.50.2 Test Requirements 2243

A.8.1.51 HD-FDD Inter-frequency neighbour cell measurement for UE category NB1 in guard-band mode under normal coverage 2244

A.8.1.51.1 Test Purpose and Environment 2244

A.8.1.51.2 Test Requirements 2246

A.8.1.52 HD-FDD Inter-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage 2247

A.8.1.52.1 Test Purpose and Environment 2247

A.8.1.52.2 Test Requirements 2248

A.8.1.53 TDD Inter-frequency neighbour cell measurement for UE category NB1 in In-Band mode under normal coverage 2249

A.8.1.53.1 Test Purpose and Environment 2249

A.8.1.53.2 Test Requirements 2251

A.8.1.54 TDD Inter-frequency neighbour cell measurement for UE category NB1 in guard-band mode under normal coverage 2252

A.8.1.54.1 Test Purpose and Environment 2252

A.8.1.54.2 Test Requirements 2254

A.8.1.55 TDD Inter-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage 2255

A.8.1.55.1 Test Purpose and Environment 2255

A.8.1.55.2 Test Requirements 2256

A.8.2 E-UTRAN TDD Intra-frequency Measurements 2257

A.8.2.1 E-UTRAN TDD-TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells 2257

A.8.2.1.1 Test Purpose and Environment 2257

A.8.2.1.2 Test Requirements 2258

A.8.2.2 E-UTRAN TDD-TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells with DRX 2258

A.8.2.2.1 Test Purpose and Environment 2258

A.8.2.2.2 Test Requirements 2261

A.8.2.3 E-UTRAN TDD - TDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps 2261

A.8.2.3.1 Test Purpose and Environment 2261

A.8.2.3.2 Test Requirements 2263

A.8.2.4 E-UTRAN TDD - TDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX 2264

A.8.2.4.1 Test Purpose and Environment 2264

A.8.2.4.2 Test Requirements 2266

A.8.2.5 E-UTRAN TDD-TDD Intra-Frequency Event-Triggered Reporting under Time Domain Measurement Resource Restriction with Non-MBSFN ABS 2266

A.8.2.5.1 Test Purpose and Environment 2266

A.8.2.5.2 Test Requirements 2268

A.8.2.6 E-UTRAN TDD-TDD Intra-Frequency Event-Triggered Reporting under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS 2269

A.8.2.6.1 Test Purpose and Environment 2269

A.8.2.6.2 Test Requirements 2272

A.8.2.7 E-UTRAN TDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps 2273

A.8.2.7.1 Test Purpose and Environment 2273

A.8.2.7.2 Test Requirements 2274

A.8.2.8 E-UTRAN TDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX 2275

A.8.2.8.1 Test Purpose and Environment 2275

A.8.2.8.2 Test Requirements 2277

A.8.2.9 E-UTRAN TDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps for Cat-M1 UE in CEModeB 2277

A.8.2.9.1 Test Purpose and Environment 2277

A.8.2.9.2 Test Requirements 2279

A.8.2.10 E-UTRAN TDD Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX for Cat-M1 UE in CEModeB 2280

A.8.2.10.1 Test Purpose and Environment 2280

A.8.2.10.2 Test Requirements 2282

A.8.2.11 E-UTRAN TDD-TDD intra-frequency event triggered reporting with DRX for UE configured with highSpeedEnhancedMeasFlag 2282

A.8.2.11.1 Test Purpose and Environment 2282

A.8.2.11.2 Test Requirements 2284

A.8.2.12 E-UTRAN TDD-TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells for UE category 0 2284

A.8.2.12.1 Test Purpose and Environment 2284

A.8.2.12.2 Test Requirements 2286

A.8.2.13 E-UTRAN TDD-TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells with DRX for UE category 0 2287

A.8.2.13.1 Test Purpose and Environment 2287

A.8.2.13.2 Test Requirements 2289

A.8.2.14 E-UTRAN TDD intra-frequency event triggered reporting for serving cell under fading propagation conditions for UE category M1 in CEModeA without gap 2289

A.8.2.14.1 Test Purpose and Environment 2289

A.8.2.14.2 Test Requirement 2291

A.8.2.15 E-UTRAN TDD-TDD intra-frequency event triggered reporting with DRX for UE configured with highSpeedEnhMeasFlag2-r16 2291

A.8.2.15.1 Test Purpose and Environment 2291

A.8.2.15.2 Test Requirements 2293

A.8.3 E-UTRAN FDD - FDD Inter-frequency Measurements 2293

A.8.3.1 E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells 2293

A.8.3.1.1 Test Purpose and Environment 2293

A.8.3.1.2 Test Requirements 2295

A.8.3.2 E-UTRAN FDD-FDD Inter-frequency event triggered reporting when DRX is used under fading propagation conditions in asynchronous cells 2295

A.8.3.2.1 Test Purpose and Environment 2295

A.8.3.2.2 Test Requirements 2298

A.8.3.3 E-UTRAN FDD-FDD inter-frequency event triggered reporting under AWGN propagation conditions in asynchronous cells with DRX when L3 filtering is used 2298

A.8.3.3.1 Test Purpose and Environment 2298

A.8.3.3.2 Test Requirements 2301

A.8.3.4 E-UTRAN FDD - FDD Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps 2301

A.8.3.4.1 Test Purpose and Environment 2301

A.8.3.4.2 Test Requirements 2303

A.8.3.5 E-UTRAN FDD - FDD Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX 2303

A.8.3.5.2 Test Requirements 2305

A.8.3.6 E-UTRAN FDD-FDD Inter-frequency event triggered reporting without measurement gaps under AWGN propagation conditions in asynchronous cells 2305

A.8.3.6.1 Test Purpose and Environment 2305

A.8.3.6.2 Test Requirements 2307

A.8.3.7 E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for Increased Carrier Monitoring without Reduced Performance Group 2308

A.8.3.7.1 Test Purpose and Environment 2308

A.8.3.7.2 Test Requirements 2310

A.8.3.8 FDD-FDD Interfrequency correct reporting of measurement events with reduced performance group configured, non DRX 2311

A.8.3.8.1 Test Purpose and Environment 2311

A.8.3.8.2 Test Requirements 2314

A.8.3.9 FDD-FDD Inter-frequency correct reporting of measurement events with reduced performance group configured, DRX 2314

A.8.3.9.1 Test Purpose and Environment 2314

A.8.3.9.2 Test Requirements 2318

A.8.3.10 E-UTRAN FDD-FDD Inter-frequency event triggered reporting with MGL=3ms under fading propagation conditions in synchronous cells 2319

A.8.3.10.1 Test Purpose and Environment 2319

A.8.3.10.2 Test Requirements 2320

A.8.3.11 E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells with burst gap 2320

A.8.3.11.1 Test Purpose and Environment 2320

A.8.3.11.2 Test Requirement 2322

A.8.3.12 E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeA 2323

A.8.3.12.1 Test Purpose and Environment 2323

A.8.3.12.2 Test Requirement 2324

A.8.3.13 E-UTRAN HD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeA 2325

A.8.3.13.1 Test Purpose and Environment 2325

A.8.3.13.2 Test Requirement 2326

A.8.3.14 E-UTRAN FDD-FDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeB 2327

A.8.3.14.1 Test Purpose and Environment 2327

A.8.3.14.2 Test Requirement 2328

A.8.3.15 E-UTRAN HD-FDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeB 2329

A.8.3.15.1 Test Purpose and Environment 2329

A.8.3.15.2 Test Requirement 2330

A.8.3.16 E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 in CEModeA when DRX is used 2331

A.8.3.16.1 Test Purpose and Environment 2331

A.8.3.16.2 Test Requirement 2333

A.8.3.17 E-UTRAN HD-FDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 in CEModeA in DRX 2333

A.8.3.17.1 Test Purpose and Environment 2333

A.8.3.17.2 Test Requirement 2336

A.8.3.18 E-UTRAN FDD-FDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 in CEModeB in DRX 2336

A.8.3.18.1 Test Purpose and Environment 2336

A.8.3.18.2 Test Requirement 2339

A.8.3.19 E-UTRAN HD-FDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 in CEModeB in DRX 2339

A.8.3.19.1 Test Purpose and Environment 2339

A.8.3.19.2 Test Requirement 2342

A.8.4 E-UTRAN TDD - TDD Inter-frequency Measurements 2342

A.8.4.1 E-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells 2342

A.8.4.1.1 Test Purpose and Environment 2342

A.8.4.1.2 Test Requirements 2344

A.8.4.2 E-UTRAN TDD-TDD Inter-frequency event triggered reporting when DRX is used under fading propagation conditions in synchronous cells 2344

A.8.4.2.1 Test Purpose and Environment 2344

A.8.4.2.2 Test Requirements 2347

A.8.4.3 E-UTRAN TDD-TDD inter-frequency event triggered reporting under AWGN propagation conditions in synchronous cells with DRX when L3 filtering is used 2347

A.8.4.3.1 Test Purpose and Environment 2347

A.8.4.3.2 Test Requirements 2349

A.8.4.4 E-UTRAN TDD - TDD Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps 2350

A.8.4.4.1 Test Purpose and Environment 2350

A.8.4.4.2 Test Requirements 2352

A.8.4.5 E-UTRAN TDD - TDD Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps with DRX 2353

A.8.4.5.1 Test Purpose and Environment 2353

A.8.4.5.2 Test Requirements 2355

A.8.4.6 E-UTRAN TDD-TDD Inter-frequency event triggered reporting for TDD UL/DL configuration 0 2355

A.8.4.6.1 Test Purpose and Environment 2355

A.8.4.6.2 Test Requirements 2356

A.8.4.7 E-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells for Increased Carrier Monitoring without Reduced Performance Group 2356

A.8.4.7.1 Test Purpose and Environment 2356

A.8.4.7.2 Test Requirements 2360

A.8.4.8 TDD-TDD Interfrequency correct reporting of measurement events with reduced performance group configured, non DRX 2360

A.8.4.8.1 Test Purpose and Environment 2360

A.8.4.8.2 Test Requirements 2363

A.8.4.9 TDD-TDD Inter-frequency correct reporting of measurement events with reduced performance group configured, DRX 2363

A.8.4.9.1 Test Purpose and Environment 2363

A.8.4.9.2 Test Requirements 2368

A.8.4.10 E-UTRAN TDD-TDD Inter-frequency event triggered reporting with MGL=3ms under fading propagation conditions in synchronous cells 2368

A.8.4.10.1 Test Purpose and Environment 2368

A.8.4.10.2 Test Requirements 2370

A.8.4.11 E-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells with burst gap 2370

A.8.4.11.1 Test Purpose and Environment 2370

A.8.4.11.2 Test Requirement 2372

A.8.4.12 E-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeA 2372

A.8.4.12.1 Test Purpose and Environment 2372

A.8.4.12.2 Test Requirement 2374

A.8.4.13 E-UTRAN TDD-TDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeB 2375

A.8.4.13.1 Test Purpose and Environment 2375

A.8.4.13.2 Test Requirement 2376

A.8.4.14 E-UTRAN TDD-TDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 in CEModeA in DRX 2377

A.8.4.14.1 Test Purpose and Environment 2377

A.8.4.14.2 Test Requirement 2379

A.8.4.15 E-UTRAN TDD-TDD inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells for UE category M1 in CEModeB in DRX 2379

A.8.4.15.1 Test Purpose and Environment 2379

A.8.4.15.2 Test Requirement 2382

A.8.5 E-UTRAN FDD - UTRAN FDD Measurements 2382

A.8.5.1 E-UTRAN FDD - UTRAN FDD event triggered reporting under fading propagation conditions 2382

A.8.5.1.1 Test Purpose and Environment 2382

A.8.5.1.2 Test Requirements 2384

A.8.5.2 E-UTRAN FDD - UTRAN FDD SON ANR cell search reporting under AWGN propagation conditions 2384

A.8.5.2.1 Test Purpose and Environment 2384

A.8.5.2.2 Test Requirements 2386

A.8.5.3 E-UTRAN FDD-UTRAN FDD event triggered reporting when DRX is used under fading propagation conditions 2386

A.8.5.3.1 Test Purpose and Environment 2386

A.8.5.3.2 Test Requirements 2389

A.8.5.4 E-UTRAN FDD - UTRAN FDD enhanced cell identification under AWGN propagation conditions 2389

A.8.5.4.1 Test Purpose and Environment 2389

A.8.5.4.2 Test Requirements 2391

A.8.5.5 E- UTRAN FDD - UTRAN FDD identification of a new CGI of UTRAN cell using autonomous gaps 2391

A.8.5.5.1 Test Purpose and Environment 2391

A.8.5.5.2 Test Requirements 2394

A.8.5.6 E-UTRAN FDD - UTRAN FDD event triggered reporting without measurement gaps under AWGN propagation conditions 2394

A.8.5.6.1 Test Purpose and Environment 2394

A.8.5.6.2 Test Requirements 2395

A.8.5.7 E-UTRAN FDD - UTRAN FDD Event Triggered Reporting under Fading Propagation Conditions for 5 MHz Bandwidth 2396

A.8.5.7.1 Test Purpose and Environment 2396

A.8.5.7.2 Test Requirements 2396

A.8.5.8 E-UTRA FDD InterRAT UTRA FDD correct reporting of measurement events with reduced performance group configured, non DRX 2396

A.8.5.8.1 Test Purpose and Environment 2396

A.8.5.8.2 Test Requirements 2399

A.8.6 E-UTRAN TDD - UTRAN FDD Measurements 2399

A.8.6.1 E-UTRAN TDD - UTRAN FDD event triggered reporting under fading propagation conditions 2399

A.8.6.1.1 Test Purpose and Environment 2399

A.8.6.1.2 Test Requirements 2401

A.8.6.2 E- UTRAN TDD - UTRAN FDD identification of a new CGI of UTRAN cell using autonomous gaps 2401

A.8.6.2.1 Test Purpose and Environment 2401

A.8.6.2.2 Test Requirements 2404

A.8.6.3 E-UTRA TDD InterRAT UTRA FDD correct reporting of measurement events with reduced performance group configured, non DRX 2404

A.8.6.3.1 Test Purpose and Environment 2404

A.8.6.3.2 Test Requirements 2407

A.8.7 E-UTRAN TDD – UTRAN TDD Measurements 2407

A.8.7.1 E-UTRAN TDD to UTRAN TDD cell search under fading propagation conditions 2407

A.8.7.1.1 Test Purpose and Environment 2407

A.8.7.1.1.1 Void 2407

A.8.7.1.1.2 1.28 Mcps TDD option 2407

A.8.7.1.1.3 Void 2409

A.8.7.1.2 Test Requirements 2409

A.8.7.1.2.1 Void 2409

A.8.7.1.2.2 1.28 Mcps TDD option 2409

A.8.7.1.2.3 Void 2409

A.8.7.2 E-UTRAN TDD-UTRAN TDD cell search when DRX is used under fading propagation conditions 2409

A.8.7.2.1 Test Purpose and Environment 2409

A.8.7.2.2 Test Requirements 2412

A.8.7.3 E-UTRAN TDD - UTRAN TDD SON ANR cell search reporting in AWGN propagation conditions 2413

A.8.7.3.1 Test Purpose and Environment 2413

A.8.7.3.2 Test Parameters 2413

A.8.7.3.3 Test Requirements 2414

A.8.7.4 E-UTRAN TDD - UTRAN TDD enhanced cell identification under AWGN propagation conditions 2415

A.8.7.4.1 Test Purpose and Environment 2415

A.8.7.4.2 Test Requirements 2417

A.8.7.5 E-UTRA TDD InterRAT UTRA TDD correct reporting of measurement events with reduced performance group configured, non DRX 2417

A.8.7.5.1 Test Purpose and Environment 2417

A.8.7.5.2 Test Requirements 2419

A.8.7A E-UTRAN FDD – UTRAN TDD Measurements 2419

A.8.7A.1 E-UTRA FDD InterRAT UTRA TDD correct reporting of measurement events with reduced performance group configured, non DRX 2419

A.8.7A.1.1 Test Purpose and Environment 2419

A.8.7A.1.2 Test Requirements 2422

A.8.8 E-UTRAN FDD – GSM Measurements 2422

A.8.8.1 E-UTRAN FDD – GSM event triggered reporting in AWGN 2422

A.8.8.1.1 Test Purpose and Environment 2422

A.8.8.1.2 Test Requirements 2424

A.8.8.2 E-UTRAN FDD-GSM event triggered reporting when DRX is used in AWGN 2424

A.8.8.2.1 Test Purpose and Environment 2424

A.8.8.2.2 Test Requirements 2426

A.8.8.3 E-UTRAN FDD – GSM event triggered reporting in AWGN with enhanced BSIC identification 2427

A.8.8.3.1 Test Purpose and Environment 2427

A.8.8.3.2 Test Requirements 2428

A.8.9 E-UTRAN FDD - UTRAN TDD measurements 2429

A.8.9.1 E-UTRAN FDD - UTRAN TDD event triggered reporting in fading propagation conditions 2429

A.8.9.1.1 Test Purpose and Environment 2429

A.8.9.1.2 Test Requirements 2430

A.8.9.2 E-UTRAN FDD - UTRAN TDD enhanced cell identification under AWGN propagation conditions 2431

A.8.9.2.1 Test Purpose and Environment 2431

A.8.9.2.2 Test Requirements 2433

A.8.10 E-UTRAN TDD – GSM Measurements 2433

A.8.10.1 E-UTRAN TDD – GSM event triggered reporting in AWGN 2433

A.8.10.1.1 Test Purpose and Environment 2433

A.8.10.1.2 Test Requirements 2434

A.8.10.2 E-UTRAN TDD-GSM event triggered reporting when DRX is used in AWGN 2435

A.8.10.2.1 Test Purpose and Environment 2435

A.8.10.2.2 Test Requirements 2437

A.8.11 Monitoring of Multiple Layers 2437

A.8.11.1 Multiple E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions 2437

A.8.11.1.1 Test Purpose and Environment 2437

A.8.11.1.2 Test Requirements 2439

A.8.11.2 E-UTRAN TDD – E-UTRAN TDD and E-UTRAN TDD Inter-frequency event triggered reporting under fading propagation conditions 2440

A.8.11.2.1 Test Purpose and Environment 2440

A.8.11.2.2 Test Requirements 2441

A.8.11.3 E-UTRAN FDD-FDD Inter-frequency and UTRAN FDD event triggered reporting under fading propagation conditions 2442

A.8.11.3.1 Test Purpose and Environment 2442

A.8.11.3.2 Test Requirements 2444

A.8.11.4 InterRAT E-UTRA TDD to E-UTRA TDD and UTRA TDD cell search test case 2444

A.8.11.4.1 Test Purpose and Environment 2444

A.8.11.4.2 Test Requirements 2447

A.8.11.5 Combined E-UTRAN FDD – E-UTRA FDD and GSM cell search. E-UTRA cells in fading; GSM cell in static propagation conditions 2447

A.8.11.5.1 Test Purpose and Environment 2447

A.8.11.5.2 Test Requirements 2449

A.8.11.6 Combined E-UTRAN TDD – E-UTRA TDD and GSM cell search. E-UTRA cells in fading; GSM cell in static propagation conditions 2450

A.8.11.6.1 Test Purpose and Environment 2450

A.8.11.6.2 Test Requirements 2452

A.8.12 RSTD Intra-frequency Measurements 2453

A.8.12.1 E-UTRAN FDD intra-frequency RSTD measurement reporting delay test case 2453

A.8.12.1.1 Test Purpose and Environment 2453

A.8.12.1.2 Test Requirements 2457

A.8.12.1.2A Test Requirements for UE Category 1bis 2457

A.8.12.2 E-UTRAN TDD intra-frequency RSTD measurement reporting delay test case 2457

A.8.12.2.1 Test Purpose and Environment 2457

A.8.12.2.2 Test Requirements 2462

A.8.12.2.2A Test Requirements for UE Category 1bis 2462

A.8.12.3 E-UTRAN FDD intra-frequency RSTD measurement period test case in CE Mode A 2462

A.8.12.3.1 Test Purpose and Environment 2462

A.8.12.3.2 Test Requirements 2468

A.8.12.4 E-UTRAN HD-FDD intra-frequency RSTD measurement period test case in CE Mode A 2468

A.8.12.4.1 Test Purpose and Environment 2468

A.8.12.4.2 Test Requirements 2473

A.8.12.5 E-UTRAN TDD intra-frequency RSTD measurement period test case in CE Mode A 2473

A.8.12.5.1 Test Purpose and Environment 2473

A.8.12.5.2 Test Requirements 2478

A.8.12.6 E-UTRAN FDD intra-frequency RSTD measurement period test case in CE Mode B 2478

A.8.12.6.1 Test Purpose and Environment 2478

A.8.12.6.2 Test Requirements 2483

A.8.12.7 E-UTRAN HD-FDD intra-frequency RSTD measurement period test case in CE Mode B 2483

A.8.12.7.1 Test Purpose and Environment 2483

A.8.12.7.2 Test Requirements 2488

A.8.12.8 E-UTRAN TDD intra-frequency RSTD measurement period test case in CE Mode B 2488

A.8.12.8.1 Test Purpose and Environment 2488

A.8.12.8.2 Test Requirements 2493

A.8.12.9 E-UTRAN FDD intra-frequency RSTD measurement period test case in CE Mode A with longer PRS occasions 2493

A.8.12.9.1 Test Purpose and Environment 2493

A.8.12.9.2 Test Requirements 2498

A.8.12.10 E-UTRAN HD-FDD intra-frequency RSTD measurement period test case in CE Mode A with longer PRS occasions 2498

A.8.12.10.1 Test Purpose and Environment 2498

A.8.12.10.2 Test Requirements 2503

A.8.12.11 E-UTRAN TDD intra-frequency RSTD measurement period test case in CE Mode A with longer PRS occasions 2503

A.8.12.11.1 Test Purpose and Environment 2503

A.8.12.11.2 Test Requirements 2508

A.8.12.12 E-UTRAN FDD intra-frequency RSTD measurement period test case in CE Mode B with longer PRS occasions 2508

A.8.12.12.1 Test Purpose and Environment 2508

A.8.12.12.2 Test Requirements 2513

A.8.12.13 E-UTRAN HD-FDD intra-frequency RSTD measurement period test case in CE Mode B with longer PRS occasions 2513

A.8.12.13.1 Test Purpose and Environment 2513

A.8.12.13.2 Test Requirements 2518

A.8.12.14 E-UTRAN TDD intra-frequency RSTD measurement period test case in CE Mode B with longer PRS occasions 2518

A.8.12.14.1 Test Purpose and Environment 2518

A.8.12.14.2 Test Requirements 2523

A.8.13 RSTD Inter-frequency Measurements 2523

A.8.13.1 E-UTRAN FDD-FDD inter-frequency RSTD measurement reporting delay test case with the reference cell on the serving carrier frequency 2523

A.8.13.1.1 Test Purpose and Environment 2523

A.8.13.1.2 Test Requirements 2528

A.8.13.1.2A Test Requirements for UE Category 1bis 2528

A.8.13.2 E-UTRAN TDD-TDD inter-frequency RSTD measurement reporting delay test case with the reference cell on the serving carrier frequency 2528

A.8.13.2.1 Test Purpose and Environment 2528

A.8.13.2.2 Test Requirements 2534

A.8.13.2.2A Test Requirements for UE Category 1bis 2534

A.8.13.3 E-UTRAN FDD inter-frequency RSTD measurement period test case in CE Mode A 2534

A.8.13.3.1 Test Purpose and Environment 2534

A.8.13.3.2 Test Requirements 2541

A.8.13.4 E-UTRAN HD-FDD inter-frequency RSTD measurement period test case in CE Mode A 2541

A.8.13.4.1 Test Purpose and Environment 2541

A.8.13.4.2 Test Requirements 2547

A.8.13.5 E-UTRAN TDD inter-frequency RSTD measurement period test case in CE Mode A 2547

A.8.13.5.1 Test Purpose and Environment 2547

A.8.13.5.2 Test Requirements 2553

A.8.13.6 E-UTRAN FDD inter-frequency RSTD measurement period test case in CE Mode B 2553

A.8.13.6.1 Test Purpose and Environment 2553

A.8.13.6.2 Test Requirements 2559

A.8.13.7 E-UTRAN HD-FDD inter-frequency RSTD measurement period test case in CE Mode B 2559

A.8.13.7.1 Test Purpose and Environment 2559

A.8.13.7.2 Test Requirements 2565

A.8.13.8 E-UTRAN TDD inter-frequency RSTD measurement period test case in CE Mode B 2565

A.8.13.8.1 Test Purpose and Environment 2565

A.8.13.8.2 Test Requirements 2571

A.8.13.9 E-UTRAN FDD inter-frequency RSTD measurement period test case in CE Mode A with longer PRS occasions 2571

A.8.13.9.1 Test Purpose and Environment 2571

A.8.13.9.2 Test Requirements 2577

A.8.13.10 E-UTRAN HD-FDD inter-frequency RSTD measurement period test case in CE Mode A with longer PRS occasions 2577

A.8.13.10.1 Test Purpose and Environment 2577

A.8.13.10.2 Test Requirements 2583

A.8.13.11 E-UTRAN TDD inter-frequency RSTD measurement period test case in CE Mode A with longer PRS occasions 2583

A.8.13.11.1 Test Purpose and Environment 2583

A.8.13.11.2 Test Requirements 2589

A.8.13.12 E-UTRAN FDD inter-frequency RSTD measurement period test case in CE Mode B with longer PRS occasions 2589

A.8.13.12.1 Test Purpose and Environment 2589

A.8.13.12.2 Test Requirements 2595

A.8.13.13 E-UTRAN HD-FDD inter-frequency RSTD measurement period test case in CE Mode B with longer PRS occasions 2595

A.8.13.13.1 Test Purpose and Environment 2595

A.8.13.13.2 Test Requirements 2601

A.8.13.14 E-UTRAN TDD inter-frequency RSTD measurement period test case in CE Mode B with longer PRS occasions 2601

A.8.13.14.1 Test Purpose and Environment 2601

A.8.13.14.2 Test Requirements 2607

A.8.14 E-UTRAN TDD - FDD Inter-frequency Measurements 2607

A.8.14.1 E-UTRAN TDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells 2607

A.8.14.1.1 Test Purpose and Environment 2607

A.8.14.1.2 Test Requirements 2609

A.8.14.2 E-UTRAN TDD-FDD Inter-frequency event triggered reporting when DRX is used under fading propagation conditions in asynchronous cells 2609

A.8.14.2.1 Test Purpose and Environment 2609

A.8.14.2.2 Test Requirements 2612

A.8.14.3 E-UTRAN TDD - FDD Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps 2612

A.8.14.3.1 Test Purpose and Environment 2612

A.8.14.3.2 Test Requirements 2614

A.8.15 E-UTRAN FDD - TDD Inter-frequency Measurements 2615

A.8.15.1 E-UTRAN FDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells 2615

A.8.15.1.1 Test Purpose and Environment 2615

A.8.15.1.2 Test Requirements 2616

A.8.15.2 E-UTRAN FDD-TDD Inter-frequency event triggered reporting when DRX is used under fading propagation conditions in asynchronous cells 2616

A.8.15.2.1 Test Purpose and Environment 2616

A.8.15.2.2 Test Requirements 2619

A.8.15.3 E-UTRAN FDD - TDD Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps 2619

A.8.15.3.1 Test Purpose and Environment 2619

A.8.15.3.2 Test Requirements 2621

A.8.16 E-UTRAN Carrier Aggregation Measurements 2622

A.8.16.1 E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX 2622

A.8.16.1.1 Test Purpose and Environment 2622

A.8.16.1.2 Test Requirements 2624

A.8.16.2 E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX 2624

A.8.16.2.1 Test Purpose and Environment 2624

A.8.16.2.2 Test Requirements 2626

A.8.16.3 E-UTRAN FDD-FDD Event triggered reporting on deactivated SCell with PCell interruption in non-DRX 2626

A.8.16.3.1 Test Purpose and Environment 2626

A.8.16.3.2 Test Requirements 2628

A.8.16.3A E-UTRAN FDD-FDD Event triggered reporting on deactivated SCell with network controlled PCell interruption in non-DRX 2629

A.8.16.3A.1 Test Purpose and Environment 2629

A.8.16.3A.2 Test Requirements 2630

A.8.16.4 E-UTRAN TDD-TDD Event triggered reporting on deactivated SCell  with PCell interruption in non-DRX 2631

A.8.16.4.1 Test Purpose and Environment 2631

A.8.16.4.2 Test Requirements 2632

A.8.16.4A E-UTRAN TDD-TDD Event triggered reporting on deactivated SCell with PCell interruption in non-DRX 2633

A.8.16.4A.1 Test Purpose and Environment 2633

A.8.16.4A.2 Test Requirements 2635

A.8.16.5 E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX for 20 MHz bandwidth 2636

A.8.16.5.1 Test Purpose and Environment 2636

A.8.16.5.2 Test Requirements 2636

A.8.16.6 E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX for 20 MHz bandwidth 2636

A.8.16.6.1 Test Purpose and Environment 2636

A.8.16.6.2 Test Requirements 2637

A.8.16.7 E-UTRA FDD event triggered reporting on deactivated SCell with PCell interruption in non-DRX for 20 MHz bandwidth 2637

A.8.16.7.1  Test Purpose and Environment 2637

A.8.16.7.2  Test Requirements 2638

A.8.16.8 E-UTRA TDD event triggered reporting on deactivated SCell with PCell interruption in non-DRX for 20 MHz bandwidth 2638

A.8.16.8.1  Test Purpose and Environment 2638

A.8.16.8.2  Test Requirements 2639

A.8.16.9 E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX for 10MHz+5MHz 2639

A.8.16.9.1 Test Purpose and Environment 2639

A.8.16.9.2 Test Requirements 2640

A.8.16.10 E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX for 10MHz+5MHz 2640

A.8.16.10.1 Test Purpose and Environment 2640

A.8.16.10.2 Test Requirements 2641

A.8.16.11 E-UTRAN FDD event triggered reporting on deactivating SCell with PCell interruption in non-DRX for 10MHz+5MHz 2641

A.8.16.11.1  Test Purpose and Environment 2641

A.8.16.11.2  Test Requirements 2642

A.8.16.12 E-UTRAN TDD event triggered reporting on deactivating SCell with PCell interruption in non-DRX for 10MHz+5MHz 2642

A.8.16.12.1  Test Purpose and Environment 2642

A.8.16.12.2  Test Requirements 2642

A.8.16.13 E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX for 5MHz +5 MHz bandwidth 2642

A.8.16.13.1 Test Purpose and Environment 2642

A.8.16.13.2 Test Requirements 2643

A.8.16.14 E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX for 5 MHz +5 MHz bandwidth 2643

A.8.16.14.1 Test Purpose and Environment 2643

A.8.16.14.2 Test Requirements 2644

A.8.16.15 E-UTRA FDD event triggered reporting on deactivated SCell with PCell interruption in non-DRX for 5 +5 MHz bandwidth 2644

A.8.16.15.1  Test Purpose and Environment 2644

A.8.16.7.2  Test Requirements 2644

A.8.16.16 E-UTRA TDD event triggered reporting on deactivated SCell with PCell interruption in non-DRX for 5+5 MHz bandwidth 2644

A.8.16.16.1  Test Purpose and Environment 2644

A.8.16.16.2  Test Requirements 2645

A.8.16.17 E-UTRAN FDD activation and deactivation of known SCell in non-DRX 2645

A.8.16.17.1 Test Purpose and Environment 2645

A.8.16.17.2 Test Requirements 2647

A.8.16.17A E-UTRAN FDD activation and deactivation of known SCell in non-DRX for 20MHz 2648

A.8.16.17A.1 Test Purpose and Environment 2648

A.8.16.17A.2 Test Requirements 2648

A.8.16.17B E-UTRAN FDD activation and deactivation of known SCell in non-DRX for 10MHz + 5MHz 2648

A.8.16.17B.1 Test Purpose and Environment 2648

A.8.16.17B.2 Test Requirements 2649

A.8.16.17C E-UTRAN FDD activation and deactivation of known SCell in non-DRX for 5MHz + 5MHz 2649

A.8.16.17C.1 Test Purpose and Environment 2649

A.8.16.17C.2 Test Requirements 2649

A.8.16.18 E-UTRAN TDD activation and deactivation of known SCell in non-DRX 2649

A.8.16.18.1 Test Purpose and Environment 2649

A.8.16.18.2 Test Requirements 2651

A.8.16.18A E-UTRAN TDD activation and deactivation of known SCell in non-DRX for 20MHz 2652

A.8.16.18A.1 Test Purpose and Environment 2652

A.8.16.18A.2 Test Requirements 2652

A.8.16.18B E-UTRAN TDD activation and deactivation of known SCell in non-DRX for 10MHz + 5MHz 2652

A.8.16.18B.1 Test Purpose and Environment 2652

A.8.16.18B.2 Test Requirements 2653

A.8.16.18C E-UTRAN TDD activation and deactivation of known SCell in non-DRX for 5MHz + 5MHz 2653

A.8.16.18C.1 Test Purpose and Environment 2653

A.8.16.18C.2 Test Requirements 2653

A.8.16.18D E-UTRAN TDD activation and deactivation of known SCell in non-DRX for 20MHz + 10MHz 2653

A.8.16.18D.1 Test Purpose and Environment 2653

A.8.16.18D.2 Test Requirements 2654

A.8.16.19 E-UTRAN FDD activation and deactivation of unknown SCell in non-DRX 2654

A.8.16.19.1 Test Purpose and Environment 2654

A.8.16.19.2 Test Requirements 2656

A.8.16.19A E-UTRAN FDD activation and deactivation of unknown SCell in non-DRX for 20MHz 2656

A.8.16.19A.1 Test Purpose and Environment 2656

A.8.16.19A.2 Test Requirements 2657

A.8.16.19B  E-UTRAN FDD activation and deactivation of unknown SCell in non-DRX for 10MHz + 5MHz 2657

A.8.16.19B.1 Test Purpose and Environment 2657

A.8.16.19B.2 Test Requirements 2657

A.8.16.19C E-UTRAN FDD activation and deactivation of unknown SCell in non-DRX for 5MHz + 5MHz 2657

A.8.16.19C.1 Test Purpose and Environment 2657

A.8.16.19C.2 Test Requirements 2658

A.8.16.20 E-UTRAN TDD activation and deactivation of unknown SCell in non-DRX 2658

A.8.16.20.1 Test Purpose and Environment 2658

A.8.16.20.2 Test Requirements 2660

A.8.16.20A E-UTRAN TDD activation and deactivation of unknown SCell in non-DRX for 20MHz 2661

A.8.16.20A.1 Test Purpose and Environment 2661

A.8.16.20A.2 Test Requirements 2661

A.8.16.20B E-UTRAN TDD activation and deactivation of unknown SCell in non-DRX for 10MHz + 5MHz 2661

A.8.16.20B.1 Test Purpose and Environment 2661

A.8.16.20B.2 Test Requirements 2662

A.8.16.20C E-UTRAN TDD activation and deactivation of unknown SCell in non-DRX for 5MHz + 5MHz 2662

A.8.16.20C.1 Test Purpose and Environment 2662

A.8.16.20C.2 Test Requirements 2662

A.8.16.20D E-UTRAN TDD activation and deactivation of unknown SCell in non-DRX for 20MHz + 10MHz 2662

A.8.16.20D.1 Test Purpose and Environment 2662

A.8.16.20D.2 Test Requirements 2663

A.8.16.21 E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX for 20MHz+10MHz 2663

A.8.16.21.1 Test Purpose and Environment 2663

A.8.16.21.2 Test Requirements 2665

A.8.16.22 E-UTRAN TDD event triggered reporting on deactivating SCell with PCell interruption in non-DRX for 20MHz+10MHz 2665

A.8.16.22.1 Test Purpose and Environment 2665

A.8.16.22.2 Test Requirements 2667

A.8.16.23 E-UTRAN TDD-FDD CA Event Triggered Reporting Under Deactivated SCell in Non-DRX with PCell in FDD 2667

A.8.16.23.1 Test Purpose and Environment 2667

A.8.16.23.2 Test Requirements 2670

A.8.16.24 E-UTRAN TDD-FDD CA Event Triggered Reporting Under Deactivated SCell in Non-DRX with PCell in TDD 2670

A.8.16.24.1 Test Purpose and Environment 2670

A.8.16.24.2 Test Requirements 2673

A.8.16.25 E-UTRAN TDD-FDD CA Event triggered reporting on deactivated SCell with PCell interruption in non-DRX with PCell in FDD 2673

A.8.16.25.1 Test Purpose and Environment 2673

A.8.16.25.2 Test Requirements 2676

A.8.16.26 E-UTRAN TDD-FDD CA Event triggered reporting on deactivated SCell with PCell interruption in non-DRX with PCell in TDD 2676

A.8.16.26.1 Test Purpose and Environment 2676

A.8.16.26.2 Test Requirements 2679

A.8.16.27 3 DL PCell in FDD CA Event Triggered Reporting with 2 Deactivated SCells in Non-DRX 2679

A.8.16.27.1 Test Purpose and Environment 2679

A.8.16.27.2 Test Requirements 2684

A.8.16.28 3 DL PCell in TDD CA Event Triggered Reporting with 2 Deactivated SCells in Non-DRX 2684

A.8.16.28.1 Test Purpose and Environment 2684

A.8.16.28.2 Test Requirements 2689

A.8.16.29 3 DL FDD CA Event Triggered Reporting under Deactivated SCells in Non-DRX 2689

A.8.16.29.1 Test Purpose and Environment 2689

A.8.16.29.2 Test Requirements 2694

A.8.16.30 3 DL TDD CA Event Triggered Reporting under Deactivated SCells in Non-DRX 2694

A.8.16.30.1 Test Purpose and Environment 2694

A.8.16.30.2 Test Requirements 2699

A.8.16.31 E-UTRAN TDD-FDD 3 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX and with PCell in FDD 2699

A.8.16.31.1 Test Purpose and Environment 2699

A.8.16.31.2 Test Requirements 2704

A.8.16.32 E-UTRAN TDD-FDD 3 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX and with PCell in TDD 2704

A.8.16.32.1 Test Purpose and Environment 2704

A.8.16.32.2 Test Requirements 2709

A.8.16.33 E-UTRAN FDD 3 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX 2709

A.8.16.33.1 Test Purpose and Environment 2709

A.8.16.33.2 Test Requirements 2714

A.8.16.34 E-UTRAN TDD 3 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX 2714

A.8.16.34.1 Test Purpose and Environment 2714

A.8.16.34.2 Test Requirements 2719

A.8.16.35 3 DL PCell in FDD CA Activation and Deactivation of Known SCell in Non-DRX 2719

A.8.16.35.1 Test Purpose and Environment 2719

A.8.16.35.2 Test Requirements 2721

A.8.16.36 3 DL PCell in TDD CA Activation and Deactivation of Known SCell in Non-DRX 2722

A.8.16.36.1 Test Purpose and Environment 2722

A.8.16.36.2 Test Requirements 2724

A.8.16.37 3 DL FDD CA activation and deactivation of known SCell in non-DRX 2725

A.8.16.37.1 Test Purpose and Environment 2725

A.8.16.37.2 Test Requirements 2727

A.8.16.38 3 DL TDD CA activation and deactivation of known SCell in non-DRX 2728

A.8.16.38.1 Test Purpose and Environment 2728

A.8.16.38.2 Test Requirements 2730

A.8.16.39 E-UTRA TDD-FDD 3DL CA Activation and Deactivation of Unknown SCell in Non-DRX with PCell in FDD 2731

A.8.16.39.1 Test Purpose and Environment 2731

A.8.16.39.2 Test Requirements 2734

A.8.16.40 E-UTRA TDD-FDD 3DL CA Activation and Deactivation of Unknown SCell in Non-DRX with PCell in TDD 2734

A.8.16.40.1 Test Purpose and Environment 2734

A.8.16.40.2 Test Requirements 2737

A.8.16.41 3 DL FDD CA activation and deactivation of unknown SCell in non-DRX 2737

A.8.16.41.1 Test Purpose and Environment 2737

A.8.16.41.2 Test Requirements 2739

A.8.16.42 3 DL TDD CA activation and deactivation of unknown SCell in non-DRX 2740

A.8.16.42.1 Test Purpose and Environment 2740

A.8.16.42.2 Test Requirements 2742

A.8.16.43 E-UTRAN TDD-FDD CA activation and deactivation of known SCell in non-DRX with PCell in FDD 2743

A.8.16.43.1 Test Purpose and Environment 2743

A.8.16.43.2 Test Requirements 2746

A.8.16.44 E-UTRAN TDD-FDD CA activation and deactivation of unknown SCell in non-DRX with PCell in FDD 2746

A.8.16.44.1 Test Purpose and Environment 2746

A.8.16.44.2 Test Requirements 2749

A.8.16.45 E-UTRAN TDD-FDD CA activation and deactivation of known SCell in non-DRX with PCell in TDD 2749

A.8.16.45.1 Test Purpose and Environment 2749

A.8.16.45.2 Test Requirements 2752

A.8.16.46 E-UTRAN TDD-FDD CA activation and deactivation of unknown SCell in non-DRX with PCell in TDD 2752

A.8.16.46.1 Test Purpose and Environment 2752

A.8.16.46.2 Test Requirements 2754

A.8.16.47 2DL/2UL FDD CA activation and deactivation of known PUCCH SCell without valid TA in non-DRX 2755

A.8.16.47.1 Test Purpose and Environment 2755

A.8.16.47.2 Test Requirements 2757

A.8.16.48 2DL/2UL TDD CA activation and deactivation of known PUCCH SCell without valid TA in non-DRX 2758

A.8.16.48.1 Test Purpose and Environment 2758

A.8.16.48.2 Test Requirements 2760

A.8.16.49 2DL/2UL TDD-FDD CA (FDD PCell) activation and deactivation of known PUCCH SCell without valid TA in non-DRX 2761

A.8.16.49.1 Test Purpose and Environment 2761

A.8.16.49.2 Test Requirements 2764

A.8.16.50 2DL/2UL TDD-FDD CA (TDD PCell) activation and deactivation of known PUCCH SCell without valid TA in non-DRX 2764

A.8.16.50.1 Test Purpose and Environment 2764

A.8.16.50.2 Test Requirements 2766

A.8.16.51 E-UTRAN 4 DL FDD CA Event Triggered Reporting with 3 deactivated SCells in Non-DRX 2767

A.8.16.51.1 Test Purpose and Environment 2767

A.8.16.51.2 Test Requirements 2772

A.8.16.52 E-UTRAN 4 DL TDD CA Event Triggered Reporting with 3 deactivated SCells in Non-DRX 2772

A.8.16.52.1 Test Purpose and Environment 2772

A.8.16.52.2 Test Requirements 2777

A.8.16.53 4 DL PCell in FDD CA Event Triggered Reporting with 3 Deactivated SCells in Non-DRX 2777

A.8.16.53.1 Test Purpose and Environment 2777

A.8.16.53.2 Test Requirements 2781

A.8.16.54 4 DL PCell in TDD CA Event Triggered Reporting with 3 Deactivated SCells in Non-DRX 2781

A.8.16.54.1 Test Purpose and Environment 2781

A.8.16.54.2 Test Requirements 2785

A.8.16.55 E-UTRAN FDD 4 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX 2785

A.8.16.55.1 Test Purpose and Environment 2785

A.8.16.55.2 Test Requirements 2791

A.8.16.56 E-UTRAN TDD 4 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX 2791

A.8.16.56.1 Test Purpose and Environment 2791

A.8.16.56.2 Test Requirements 2797

A.8.16.57 E-UTRAN FDD 4DL CA activation and deactivation of know SCell in non-DRX 2797

A.8.16.57.1 Test Purpose and Environment 2797

A.8.16.57.2 Test Requirements 2799

A.8.16.58 E-UTRAN TDD 4DL CA activation and deactivation of know SCell in non-DRX 2800

A.8.16.58.1 Test Purpose and Environment 2800

A.8.16.58.2 Test Requirements 2802

A.8.16.59 E-UTRAN PCell in FDD FDD-TDD 4 DL CA activation and deactivation of known SCell in non-DRX 2803

A.8.16.59.1 Test Purpose and Environment 2803

A.8.16.59.2 Test Requirements 2807

A.8.16.60 E-UTRAN PCell in TDD FDD-TDD 4 DL CA activation and deactivation of known SCell in non-DRX 2808

A.8.16.60.1 Test Purpose and Environment 2808

A.8.16.60.2 Test Requirements 2811

A.8.16.61 E-UTRAN FDD 4DL CA activation and deactivation of unknown SCell in non-DRX 2812

A.8.16.61.1 Test Purpose and Environment 2812

A.8.16.61.2 Test Requirements 2815

A.8.16.62 E-UTRAN TDD 4DL CA activation and deactivation of unknown SCell in non-DRX 2815

A.8.16.62.1 Test Purpose and Environment 2815

A.8.16.62.2 Test Requirements 2817

A.8.16.63 E-UTRAN PCell in FDD FDD-TDD 4 DL CA activation and deactivation of unknown SCell in non-DRX 2818

A.8.16.63.1 Test Purpose and Environment 2818

A.8.16.63.2 Test Requirements 2821

A.8.16.64 E-UTRAN PCell in TDD FDD-TDD 4 DL CA activation and deactivation of unknown SCell in non-DRX 2822

A.8.16.64.1 Test Purpose and Environment 2822

A.8.16.64.2 Test Requirements 2826

A.8.16.65 5 DL FDD-TDD with PCell in FDD CA Event Triggered Reporting with 4 Deactivated SCells in Non-DRX 2826

A.8.16.65.1 Test Purpose and Environment 2826

A.8.16.65.2 Test Requirements 2831

A.8.16.66 5 DL FDD-TDD with PCell in TDD CA Event Triggered Reporting with 4 Deactivated SCells in Non-DRX 2831

A.8.16.66.1 Test Purpose and Environment 2831

A.8.16.66.2 Test Requirements 2836

A.8.16.67 5 DL FDD-TDD with PCell in FDD CA activation and deactivation of Unknown SCell in non-DRX 2836

A.8.16.67.1 Test Purpose and Environment 2836

A.8.16.67.2 Test Requirements 2841

A.8.16.68 5 DL FDD-TDD with PCell in TDD CA activation and deactivation of Unknown SCell in non-DRX 2841

A.8.16.68.1 Test Purpose and Environment 2841

A.8.16.68.2 Test Requirements 2846

A.8.16.69 5 DL FDD CA activation and deactivation of unknown SCell in non-DRX 2846

A.8.16.69.1 Test Purpose and Environment 2846

A.8.16.69.2 Test Requirements 2850

A.8.16.70 5 DL TDD CA activation and deactivation of unknown SCell in non-DRX 2850

A.8.16.70.1 Test Purpose and Environment 2850

A.8.16.70.2 Test Requirements 2854

A.8.16.71 5 DL FDD CA Event Triggered Reporting with Deactivated SCells in Non-DRX 2854

A.8.16.71.1 Test Purpose and Environment 2854

A.8.16.71.2 Test Requirements 2859

A.8.16.72 5 DL TDD CA Event Triggered Reporting with Deactivated SCells in Non-DRX 2859

A.8.16.72.1 Test Purpose and Environment 2859

A.8.16.72.2 Test Requirements 2864

A.8.16.73 5 DL FDD CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX 2864

A.8.16.73.1 Test Purpose and Environment 2864

A.8.16.73.2 Test Requirements 2871

A.8.16.74 5 DL TDD CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX 2871

A.8.16.74.1 Test Purpose and Environment 2871

A.8.16.74.2 Test Requirements 2878

A.8.16.75 5 DL FDD-TDD with PCell in FDD CA activation and deactivation of known SCell in non-DRX 2878

A.8.16.75.1 Test Purpose and Environment 2878

A.8.16.75.2 Test Requirements 2884

A.8.16.76 5 DL FDD-TDD with PCell in TDD CA activation and deactivation of known SCell in non-DRX 2884

A.8.16.76.1 Test Purpose and Environment 2884

A.8.16.76.2 Test Requirements 2890

A.8.16.77 5 DL FDD CA activation and deactivation of know SCell in non-DRX 2890

A.8.16.77.1 Test Purpose and Environment 2890

A.8.16.77.2 Test Requirements 2894

A.8.16.78 5 DL TDD CA activation and deactivation of know SCell in non-DRX 2894

A.8.16.78.1 Test Purpose and Environment 2894

A.8.16.78.2 Test Requirements 2896

A.8.16.79 E-UTRAN PCell in FDD FDD-TDD 4 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX 2897

A.8.16.79.1 Test Purpose and Environment 2897

A.8.16.79.2 Test Requirements 2904

A.8.16.80 E-UTRAN PCell in TDD TDD-FDD 4 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX 2904

A.8.16.80.1 Test Purpose and Environment 2904

A.8.16.80.2 Test Requirements 2911

A.8.16.81 E-UTRAN PCell in FDD FDD-TDD 5 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX 2911

A.8.16.81.1 Test Purpose and Environment 2911

A.8.16.81.2 Test Requirements 2917

A.8.16.82 E-UTRAN PCell in TDD TDD-FDD 5 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX 2917

A.8.16.82.1 Test Purpose and Environment 2917

A.8.16.82.2 Test Requirements 2923

A.8.16.83 3 DL CA Event Triggered Reporting under Deactivated SCells in Non-DRX with generic duplex modes 2923

A.8.16.83.1 Test Purpose and Environment 2923

A.8.16.83.2 Test Requirements 2928

A.8.16.84 3 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX with generic duplex modes 2928

A.8.16.84.1 Test Purpose and Environment 2928

A.8.16.84.2 Test Requirements 2934

A.8.16.85 3 DL CA Activation and Deactivation of Known SCell in Non-DRX with generic duplex modes 2934

A.8.16.85.1 Test Purpose and Environment 2934

A.8.16.85.2 Test Requirements 2938

A.8.16.86 3 DL CA Activation and Deactivation of Unknown SCell in Non-DRX with generic duplex modes 2938

A.8.16.86.1 Test Purpose and Environment 2938

A.8.16.86.2 Test Requirements 2941

A.8.16.87 4 DL CA Event Triggered Reporting under Deactivated SCells in Non-DRX with generic duplex modes 2941

A.8.16.87.1 Test Purpose and Environment 2941

A.8.16.87.2 Test Requirements 2947

A.8.16.88 4 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX with generic duplex modes 2947

A.8.16.88.1 Test Purpose and Environment 2947

A.8.16.88.2 Test Requirements 2955

A.8.16.89 4 DL CA Activation and Deactivation of Known SCell in Non-DRX with generic duplex modes 2955

A.8.16.89.1 Test Purpose and Environment 2955

A.8.16.89.2 Test Requirements 2962

A.8.16.90 4 DL CA Activation and Deactivation of Unknown SCell in Non-DRX with generic duplex modes 2962

A.8.16.90.1 Test Purpose and Environment 2962

A.8.16.90.2 Test Requirements 2969

A.8.16.91 5 DL CA Event Triggered Reporting under Deactivated SCells in Non-DRX with generic duplex modes 2969

A.8.16.91.1 Test Purpose and Environment 2969

A.8.16.91.2 Test Requirements 2975

A.8.16.92 5 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX with generic duplex modes 2975

A.8.16.92.1 Test Purpose and Environment 2975

A.8.16.92.2 Test Requirements 2983

A.8.16.93 5 DL CA Activation and Deactivation of Known SCell in Non-DRX with generic duplex modes 2983

A.8.16.93.1 Test Purpose and Environment 2983

A.8.16.93.2 Test Requirements 2990

A.8.16.94 5 DL CA Activation and Deactivation of Unknown SCell in Non-DRX with generic duplex modes 2990

A.8.16.94.1 Test Purpose and Environment 2990

A.8.16.94.2 Test Requirements 2997

A.8.16.95 6 DL CA Event Triggered Reporting under Deactivated SCells in Non-DRX with generic duplex modes 2997

A.8.16.95.1 Test Purpose and Environment 2997

A.8.16.95.2 Test Requirements 3005

A.8.16.96 6 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX with generic duplex modes 3005

A.8.16.96.1 Test Purpose and Environment 3005

A.8.16.96.2 Test Requirements 3014

A.8.16.97 6 DL CA Activation and Deactivation of Known SCell in Non-DRX with generic duplex modes 3014

A.8.16.97.1 Test Purpose and Environment 3014

A.8.16.97.2 Test Requirements 3021

A.8.16.98 6 DL CA Activation and Deactivation of Unknown SCell in Non-DRX with generic duplex modes 3021

A.8.16.98.1 Test Purpose and Environment 3021

A.8.16.98.2 Test Requirements 3029

A.8.16.99 7 DL CA Event Triggered Reporting under Deactivated SCells in Non-DRX with generic duplex modes 3029

A.8.16.99.1 Test Purpose and Environment 3029

A.8.16.99.2 Test Requirements 3039

A.8.16.100 7 DL CA Event Triggered Reporting on Deactivated SCell with PCell and SCell Interruptions in Non-DRX with generic duplex modes 3039

A.8.16.100.1 Test Purpose and Environment 3039

A.8.16.100.2 Test Requirements 3049

A.8.16.101 7 DL CA Activation and Deactivation of Known SCell in Non-DRX with generic duplex modes 3049

A.8.16.101.1 Test Purpose and Environment 3049

A.8.16.101.2 Test Requirements 3059

A.8.16.102 7 DL CA Activation and Deactivation of Unknown SCell in Non-DRX with generic duplex modes 3059

A.8.16.102.1 Test Purpose and Environment 3059

A.8.16.102.2 Test Requirements 3070

A.8.16.103 Hibernation and Activation of Known SCell in Non-DRX with generic duplex modes 3070

A.8.16.103.1 Test Purpose and Environment 3070

A.8.16.103.2 Test Requirements 3075

A.8.16.104 Hibernation and Activation of Unknown SCell in Non-DRX with generic duplex modes 3076

A.8.16.104.1 Test Purpose and Environment 3076

A.8.16.104.2 Test Requirements 3080

A.8.16.105 Idle Mode measurements of inter-frequency CA candidate cells for early reporting 3081

A.8.16.105.1 Test Purpose and Environment 3081

A.8.16.105.2 Test Requirements 3085

A.8.16.106 Direct Activation of Known SCell in Non-DRX with generic duplex modes 3086

A.8.16.106.1 Test Purpose and Environment 3086

A.8.16.106.2 Test Requirements 3090

A.8.16.107 E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX with highSpeedEnhMeasFlag2-r16 3090

A.8.16.107.1 Test Purpose and Environment 3090

A.8.16.107.2 Test Requirements 3092

A.8.16.108 E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX with highSpeedEnhMeasFlag2-r16 3093

A.8.16.108.1 Test Purpose and Environment 3093

A.8.16.108.2 Test Requirements 3095

A.8.17 RSTD Measurements for E-UTRAN Carrier Aggregation 3096

A.8.17.1 E-UTRAN FDD RSTD measurement reporting delay test case 3096

A.8.17.1.1 Test Purpose and Environment 3096

A.8.17.1.2 Test Requirements 3102

A.8.17.2 E-UTRAN TDD RSTD measurement reporting delay test case 3102

A.8.17.2.1 Test Purpose and Environment 3102

A.8.17.2.2 Test Requirements 3109

A.8.17.3 E-UTRAN FDD RSTD Measurement Reporting Test Case for 20 MHz 3109

A.8.17.3.1 Test Purpose and Environment 3109

A.8.17.3.2 Test Requirements 3110

A.8.17.4 E-UTRAN TDD RSTD Measurement Reporting Test Case for 20 MHz 3110

A.8.17.4.1 Test Purpose and Environment 3110

A.8.17.4.2 Test Requirements 3111

A.8.17.5 E-UTRAN FDD RSTD Measurement Reporting Test Case for 10MHz+5MHz 3111

A.8.17.5.1 Test Purpose and Environment 3111

A.8.17.5.2 Test Requirements 3112

A.8.17.6 E-UTRAN TDD RSTD Measurement Reporting Test Case for 10MHz+5MHz 3112

A.8.17.6.1 Test Purpose and Environment 3112

A.8.17.6.2 Test Requirements 3113

A.8.17.7 E-UTRAN FDD RSTD Measurement Reporting Test Case for 5 + 5 MHz Bandwidth 3114

A.8.17.7.1 Test Purpose and Environment 3114

A.8.17.7.2 Test Requirements 3114

A.8.17.8 E-UTRAN TDD RSTD Measurement Reporting Test Case for 5+5 MHz bandwidth 3115

A.8.17.8.1 Test Purpose and Environment 3115

A.8.17.8.2 Test Requirements 3115

A.8.17.9 E-UTRAN TDD RSTD Measurement Reporting Test Case for 20MHz+10MHz 3116

A.8.17.9.1 Test Purpose and Environment 3116

A.8.17.9.2 Test Requirements 3117

A.8.17.10 E-UTRAN 3 DL FDD CA RSTD Measurement Reporting Delay Test Case 3117

A.8.17.10.1 Test Purpose and Environment 3117

A.8.17.10.2 Test Requirements 3124

A.8.17.11 E-UTRAN 3 DL TDD CA RSTD Measurement Reporting Delay Test Case 3125

A.8.17.11.1 Test Purpose and Environment 3125

A.8.17.11.2 Test Requirements 3131

A.8.18 E-UTRAN TDD – HRPD Measurements 3132

A.8.18.1 E-UTRAN TDD-HRPD event triggered reporting under fading propagation conditions 3132

A.8.18.1.1 Test Purpose and Environment 3132

A.8.18.1.2 Test Requirements 3134

A.8.19 E-UTRAN TDD – CDMA2000 1X Measurements 3134

A.8.19.1 E-UTRAN TDD – CDMA2000 1X event triggered reporting under fading propagation conditions 3134

A.8.19.1.1 Test Purpose and Environment 3134

A.8.19.1.2 Test Requirements 3135

A.8.20 Inter-frequency/RAT Measurements in CA mode 3136

A.8.20.1 E-UTRAN FDD-FDD Inter-frequency event triggered reporting under fading propagation conditions in asynchronous cells 3136

A.8.20.1.1 Test Purpose and Environment 3136

A.8.20.1.2 Test Requirements 3137

A.8.20.2 E-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells 3137

A.8.20.2.1 Test Purpose and Environment 3138

A.8.20.2.2 Test Requirements 3139

A.8.20.2A E-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells for 20 MHz +20 MHz bandwidth. 3140

A.8.20.2A.1 Test Purpose and Environment 3140

A.8.20.2A.2 Test Requirements 3140

A.8.20.2B E-UTRAN TDD-TDD Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells for 20 MHz +10 MHz bandwidth. 3140

A.8.20.2B.1 Test Purpose and Environment 3140

A.8.20.2B.2 Test Requirements 3143

A.8.20.3 E-UTRAN FDD - UTRAN FDD event triggered reporting under fading propagation conditions 3143

A.8.20.3.1 Test Purpose and Environment 3143

A.8.20.3.2 Test Requirements 3145

A.8.20.4 E-UTRAN TDD to UTRAN TDD cell search under fading propagation conditions 3145

A.8.20.4.1 Test Purpose and Environment 3145

A.8.20.4.1.1 1.28 Mcps TDD option 3145

A.8.20.4.2 Test Requirements 3147

A.8.20.4.2.1 1.28 Mcps TDD option 3147

A.8.20.4A E-UTRAN TDD with 20 MHz +20 MHz bandwidth to UTRAN TDD cell search under fading propagation conditions 3147

A.8.20.4A.1 Test Purpose and Environment 3147

A.8.20.4A.1.1 1.28 Mcps TDD option 3147

A.8.20.4A.2 Test Requirements 3147

A.8.20.4A.2.1 1.28 Mcps TDD option 3147

A.8.20.4B E-UTRAN TDD with 20 MHz +10 MHz bandwidth to UTRAN TDD cell search under fading propagation conditions 3148

A.8.20.4B.1 Test Purpose and Environment 3148

A.8.20.4B.1.1 1.28 Mcps TDD option 3148

A.8.20.4B.2 Test Requirements 3150

A.8.20.4B.2.1 1.28 Mcps TDD option 3150

A.8.21 CSG Proximity Indication Testing Case for E-UTRAN FDD – FDD Inter frequency 3150

A.8.21.1 Test Purpose and Environment 3150

A.8.21.2 Test Requirements 3154

A.8.22 E-UTRAN Discovery Signal Measurements 3154

A.8.22.1 E-UTRAN FDD-FDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells in DRX based on CRS based discovery signal 3154

A.8.22.1.1 Test Purpose and Environment 3154

A.8.22.1.2 Test Requirements 3157

A.8.22.2 E-UTRAN TDD-TDD intra-frequency event triggered reporting under fading propagation conditions in synchronous cells in DRX based on CRS based discovery signal 3157

A.8.22.2.1 Test Purpose and Environment 3157

A.8.22.2.2 Test Requirements 3160

A.8.22.3 E-UTRAN FDD-FDD inter-frequency event triggered reporting under fading propagation conditions in DRX based on CRS based discovery signal 3160

A.8.22.3.1 Test Purpose and Environment 3160

A.8.22.3.2 Test Requirements 3163

A.8.22.4 E-UTRAN TDD-TDD inter-frequency event triggered reporting under fading propagation conditions in DRX based on CRS based discovery signal 3163

A.8.22.4.1 Test Purpose and Environment 3163

A.8.22.4.2 Test Requirements 3166

A.8.22.5 E-UTRAN FDD-FDD intra-frequency event triggered reporting in DRX based on CSI-RS based discovery signal 3166

A.8.22.5.1 Test Purpose and Environment 3166

A.8.22.5.2 Test Requirements 3170

A.8.22.6 E-UTRAN TDD-TDD intra-frequency event triggered reporting in DRX based on CSI-RS based discovery signal 3170

A.8.22.6.1 Test Purpose and Environment 3170

A.8.22.6.2 Test Requirements 3174

A.8.22.7 E-UTRAN FDD-FDD Inter-frequency event triggered reporting in DRX based on CSI-RS based discovery signal 3174

A.8.22.7.1 Test Purpose and Environment 3174

A.8.22.7.2 Test Requirements 3178

A.8.22.8 E-UTRAN TDD-TDD inter-frequency event triggered reporting under fading propagation condition in DRX based on CSI-RS based discovery signal 3178

A.8.22.8.1 Test Purpose and Environment 3178

A.8.22.8.2 Test Requirements 3182

A.8.22.9 E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX based on CRS based discovery signal 3182

A.8.22.9.1 Test Purpose and Environment 3182

A.8.22.9.2 Test Requirements 3184

A.8.22.10 E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX based on CRS based discovery signal 3185

A.8.22.10.1 Test Purpose and Environment 3185

A.8.22.10.2 Test Requirements 3187

A.8.22.11 E-UTRAN FDD event triggered reporting under deactivated SCell in non-DRX based on CSI-RS based discovery signal 3188

A.8.22.11.1 Test Purpose and Environment 3188

A.8.22.11.2 Test Requirements 3191

A.8.22.12 E-UTRAN TDD event triggered reporting under deactivated SCell in non-DRX based on CSI-RS based discovery signal 3191

A.8.22.12.1 Test Purpose and Environment 3191

A.8.22.12.2 Test Requirements 3195

A.8.23 E-UTRAN Dual Connectivity Measurements 3195

A.8.23.1 E-UTRAN FDD-FDD DC intra-frequency event triggered reporting with DRX in synchronous DC 3195

A.8.23.1.1 Test Purpose and Environment 3195

A.8.23.1.2 Test Requirements 3198

A.8.23.2 E-UTRAN FDD-FDD DC intra-frequency event triggered reporting with DRX in asynchronous DC 3198

A.8.23.2.1 Test Purpose and Environment 3198

A.8.23.2.2 Test Requirements 3201

A.8.23.3 E-UTRAN TDD-TDD DC intra-frequency event triggered reporting with DRX in synchronous DC 3201

A.8.23.3.1 Test Purpose and Environment 3201

A.8.23.3.2 Test Requirements 3204

A.8.23.4 E-UTRAN FDD-FDD DC inter-frequency event triggered reporting with DRX in synchronous DC 3204

A.8.23.4.1 Test Purpose and Environment 3204

A.8.23.4.2 Test Requirements 3207

A.8.23.5 E-UTRAN FDD-FDD DC inter-frequency event triggered reporting with DRX in asynchronous DC 3207

A.8.23.5.1 Test Purpose and Environment 3207

A.8.23.5.2 Test Requirements 3210

A.8.23.6 E-UTRAN TDD-TDD DC inter-frequency event triggered reporting with DRX in synchronous DC 3210

A.8.23.6.1 Test Purpose and Environment 3210

A.8.23.6.2 Test Requirements 3213

A.8.23.7 E-UTRAN FDD-FDD Addition and Release Delay of known PSCell in Synchronous DC 3213

A.8.23.7.1 Test Purpose and Environment 3213

A.8.23.7.2 Test Requirements 3215

A.8.23.8 E-UTRAN FDD-FDD Addition and Release Delay of known PSCell in Asynchronous DC 3216

A.8.23.8.1 Test Purpose and Environment 3216

A.8.23.8.2 Test Requirements 3218

A.8.23.9 E-UTRAN TDD Addition and Release Delay of known PSCell in Synchronous DC 3219

A.8.23.9.1 Test Purpose and Environment 3219

A.8.23.9.2 Test Requirements 3222

A.8.23.10 E-UTRAN TDD-FDD DC intra-frequency event triggered reporting with DRX in synchronous DC with PCell in FDD 3222

A.8.23.10.1 Test Purpose and Environment 3222

A.8.23.10.2 Test Requirements 3225

A.8.23.11 E-UTRAN TDD-FDD DC intra-frequency event triggered reporting with DRX in synchronous DC with PCell in TDD 3225

A.8.23.11.1 Test Purpose and Environment 3225

A.8.23.11.2 Test Requirements 3228

A.8.23.12 E-UTRAN TDD-FDD DC inter-frequency event triggered reporting with DRX in synchronous DC with PCell in FDD 3228

A.8.23.12.1 Test Purpose and Environment 3228

A.8.23.12.2 Test Requirements 3231

A.8.23.13 E-UTRAN TDD-FDD DC inter-frequency event triggered reporting with DRX in synchronous DC with PCell in TDD 3231

A.8.23.13.1 Test Purpose and Environment 3231

A.8.23.13.2 Test Requirements 3234

A.8.23.14 E-UTRAN TDD-FDD Addition and Release Delay of known PSCell in Synchronous DC with PCell in FDD 3234

A.8.23.14.1 Test Purpose and Environment 3234

A.8.23.14.2 Test Requirements 3237

A.8.23.15 E-UTRAN TDD-FDD Addition and Release Delay of known PSCell in Synchronous DC with PCell in TDD 3237

A.8.23.15.1 Test Purpose and Environment 3237

A.8.23.15.2 Test Requirements 3240

A.8.23.16 E-UTRAN FDD-FDD DC SSTD measurement reporting delay with no DRX in asynchronous DC 3240

A.8.23.16.1 Test Purpose and Environment 3240

A.8.23.16.2 Test Requirements 3241

A.8.23.17 E-UTRAN FDD-FDD DC SSTD measurement reporting delay with DRX in asynchronous DC 3242

A.8.23.17.1 Test Purpose and Environment 3242

A.8.23.17.2 Test Requirements 3244

A.8.23.18 E-UTRAN FDD - FDD DC Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps in synchronous DC 3244

A.8.23.18.1 Test Purpose and Environment 3244

A.8.23.18.2 Test Requirements 3245

A.8.23.19 E-UTRAN FDD - FDD DC Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps in asynchronous DC 3246

A.8.23.19.1 Test Purpose and Environment 3246

A.8.23.19.2 Test Requirements 3247

A.8.23.20 E-UTRAN TDD - TDD DC Intra-frequency identification of a new CGI of E-UTRA cell using autonomous gaps in synchronous DC 3248

A.8.23.20.1 Test Purpose and Environment 3248

A.8.23.20.2 Test Requirements 3249

A.8.23.21 E-UTRAN FDD - FDD DC Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps in synchronous DC 3250

A.8.23.21.1 Test Purpose and Environment 3250

A.8.23.21.2 Test Requirements 3251

A.8.23.22 E-UTRAN FDD - FDD DC Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps in asynchronous DC 3252

A.8.23.22.1 Test Purpose and Environment 3252

A.8.23.22.2 Test Requirements 3253

A.8.23.23 E-UTRAN TDD - TDD DC Inter-frequency identification of a new CGI of E-UTRA cell using autonomous gaps in synchronous DC 3254

A.8.23.23.1 Test Purpose and Environment 3254

A.8.23.23.2 Test Requirements 3255

A.8.23.24 E-UTRAN FDD-FDD DC activation and deactivation of known SCell in Non-DRX in synchronous DC 3256

A.8.23.24.1 Test Purpose and Environment 3256

A.8.23.24.2 Test Requirements 3258

A.8.23.25 E-UTRAN FDD-FDD DC activation and deactivation of known SCell in Non-DRX in asynchronous DC 3259

A.8.23.25.1 Test Purpose and Environment 3259

A.8.23.25.2 Test Requirements 3261

A.8.23.26 E-UTRAN TDD-TDD DC activation and deactivation of known SCell in Non-DRX in synchronous DC 3262

A.8.23.26.1 Test Purpose and Environment 3262

A.8.23.26.2 Test Requirements 3264

A.8.23.27 E-UTRAN FDD-FDD DC event triggered reporting under deactivated SCell with PCell and PSCell interruption in non-DRX in synchronous DC 3265

A.8.23.27.1 Test Purpose and Environment 3265

A.8.23.27.2 Test Requirements 3268

A.8.23.28 E-UTRAN FDD-FDD DC event triggered reporting under deactivated SCell with PCell and PSCell interruption in non-DRX in asynchronous DC 3268

A.8.23.28.1 Test Purpose and Environment 3268

A.8.23.28.2 Test Requirements 3272

A.8.23.29 E-UTRAN TDD-TDD DC event triggered reporting under deactivated SCell with PCell and PSCell interruption in non-DRX in synchronous DC 3272

A.8.23.29.1 Test Purpose and Environment 3272

A.8.23.29.2 Test Requirements 3276

A.8.24 Proximity-based Services 3276

A.8.24.1 E-UTRAN FDD - Initiation/Cease of SLSS Transmission with ProSe Direct Discovery 3276

A.8.24.1.1 Test Purpose and Environment 3276

A.8.24.1.2 Test Requirements 3277

A.8.24.2 E-UTRAN TDD - Initiation/Cease of SLSS Transmission with ProSe Direct Discovery 3278

A.8.24.2.1 Test Purpose and Environment 3278

A.8.24.2.2 Test Requirements 3279

A.8.24.3 E-UTRAN FDD - Initiation/Cease of SLSS Transmission with ProSe Direct Communication 3279

A.8.24.3.1 Test Purpose and Environment 3280

A.8.24.3.2 Test Requirements 3281

A.8.25 E-UTRAN-WLAN Measurements 3282

A.8.25.1 E-UTRAN FDD-WLAN Event Triggered Reporting in non-DRX under AWGN 3282

A.8.25.1.1 Test Purpose and Environment 3282

A.8.25.1.2 Test Requirements 3284

A.8.25.2 E-UTRAN TDD-WLAN Event Triggered Reporting in non-DRX under AWGN 3284

A.8.25.2.1 Test Purpose and Environment 3284

A.8.25.2.2 Test Requirements 3286

A.8.26 Frame Structure 3 (FS3) 3286

A.8.26.1 E-UTRAN FDD-FS3 Activation and deactivation of known FS3 SCell with FDD PCell in non-DRX 3286

A.8.26.1.1 Test Purpose and Environment 3286

A.8.26.1.2 Test Requirements 3288

A.8.26.2 E-UTRAN TDD-FS3 Activation and deactivation of known FS3 SCell with TDD PCell in non-DRX 3289

A.8.26.2.1 Test Purpose and Environment 3289

A.8.26.2.2 Test Requirements 3291

A.8.26.3 E-UTRAN FDD-FS3 Event triggered reporting on deactivated FS3 SCell and FDD PCell interruption in non-DRX 3292

A.8.26.3.1 Test Purpose and Environment 3292

A.8.26.3.2 Test Requirements 3295

A.8.26.3A E-UTRAN FDD-TDD 3DL Event triggered reporting on deactivated FS3 SCell and FDD PCell interruption in non-DRX 3295

A.8.26.3A.1 Test Purpose and Environment 3295

A.8.26.3A.2 Test Requirements 3298

A.8.26.4 E-UTRAN TDD-FS3 Event triggered reporting on deactivated FS3 SCell and TDD PCell interruption in non-DRX 3298

A.8.26.4.1 Test Purpose and Environment 3298

A.8.26.4.2 Test Requirements 3302

A.8.26.4A E-UTRAN TDD-TDD 3DL Event triggered reporting on deactivated FS3 SCell and FDD PCell interruption in non-DRX 3302

A.8.26.4A.1 Test Purpose and Environment 3302

A.8.26.4A.2 Test Requirements 3306

A.8.26.5 E-UTRAN FDD-FS3 Intra-frequency event triggered reporting in non-DRX for CRS based discovery signal 3306

A.8.26.5.1 Test Purpose and Environment 3306

A.8.26.5.2 Test Requirements 3309

A.8.26.5A E-UTRAN FDD-FS3 Intra-frequency event triggered reporting in non-DRX for CRS based discovery signal with 2 SCells 3309

A.8.26.5A.1 Test Purpose and Environment 3309

A.8.26.5A.2 Test Requirements 3313

A.8.26.6 E-UTRAN TDD-FS3 Intra-frequency event triggered reporting in non-DRX for CRS based discovery signal 3313

A.8.26.6.1 Test Purpose and Environment 3313

A.8.26.6.2 Test Requirements 3317

A.8.26.6A E-UTRAN TDD-FS3 Intra-frequency event triggered reporting in non-DRX for CRS based discovery signal with 2 SCells 3317

A.8.26.6A.1 Test Purpose and Environment 3317

A.8.26.6A.2 Test Requirements 3321

A.8.26.7 E-UTRAN FDD-FS3 Intra-frequency event triggered reporting in DRX for CRS based discovery signal 3321

A.8.26.7.1 Test Purpose and Environment 3321

A.8.26.7.2 Test Requirements 3324

A.8.26.8 E-UTRAN TDD-FS3 Intra-frequency event triggered reporting in DRX for CRS based discovery signal 3324

A.8.26.8.1 Test Purpose and Environment 3324

A.8.26.8.2 Test Requirements 3328

A.8.26.9 E-UTRAN FDD-FS3 Inter-frequency event triggered reporting under fading propagation conditions in synchronous cells 3328

A.8.26.9.1 Test Purpose and Environment 3328

A.8.26.9.2 Test Requirements 3331

A.8.26.10 E-UTRAN TDD-FS3 inter-frequency event triggered reporting under fading propagation conditions in synchronous cells 3331

A.8.26.10.1 Test Purpose and Environment 3331

A.8.26.10.2 Test Requirements 3334

A.9 Measurement Performance Requirements 3334

A.9.1 RSRP 3334

A.9.1.1 FDD Intra frequency case 3334

A.9.1.1.1 Test Purpose and Environment 3334

A.9.1.1.2 Test parameters 3334

A.9.1.1.3 Test Requirements 3337

A.9.1.2 TDD Intra frequency case 3337

A.9.1.2.1 Test Purpose and Environment 3337

A.9.1.2.2 Test parameters 3337

A.9.1.2.3 Test Requirements 3338

A.9.1.3 FDD—FDD Inter frequency case 3339

A.9.1.3.1 Test Purpose and Environment 3339

A.9.1.3.2 Test parameters 3339

A.9.1.3.3 Test Requirements 3342

A.9.1.4 TDD—TDD Inter frequency case 3342

A.9.1.4.1 Test Purpose and Environment 3342

A.9.1.4.2 Test parameters 3342

A.9.1.4.3 Test Requirements 3344

A.9.1.5 FDD—TDD Inter frequency case 3345

A.9.1.5.1 Test Purpose and Environment 3345

A.9.1.5.2 Test parameters 3345

A.9.1.5.3 Test Requirements 3346

A.9.1.6 FDD RSRP for E-UTRAN Carrier Aggregation 3347

A.9.1.6.1 Test Purpose and Environment 3347

A.9.1.6.2 Test parameters 3347

A.9.1.6.3 Test Requirements 3350

A.9.1.7 TDD RSRP for E-UTRAN Carrier Aggregation 3350

A.9.1.7.1 Test Purpose and Environment 3350

A.9.1.7.2 Test parameters 3350

A.9.1.7.3 Test Requirements 3353

A.9.1.8 FDD RSRP under Time-Domain Measurement Resource Restriction with Non-MBSFN ABS 3353

A.9.1.8.1 Test Purpose and Environment 3353

A.9.1.8.2 Test parameters 3353

A.9.1.8.3 Test Requirements 3357

A.9.1.9 TDD RSRP under Time-Domain Measurement Resource Restriction with Non-MBSFN ABS 3357

A.9.1.9.1 Test Purpose and Environment 3357

A.9.1.9.2 Test parameters 3357

A.9.1.9.3 Test Requirements 3360

A.9.1.10 FDD RSRP under Time-Domain Measurement Resource Restriction with MBSFN ABS 3360

A.9.1.10.1 Test Purpose and Environment 3360

A.9.1.10.2 Test parameters 3360

A.9.1.10.3 Test Requirements 3363

A.9.1.11 TDD RSRP under Time-Domain Measurement Resource Restriction with MBSFN ABS 3363

A.9.1.11.1 Test Purpose and Environment 3363

A.9.1.11.2 Test parameters 3363

A.9.1.11.3 Test Requirements 3367

A.9.1.12 FDD RSRP for E-UTRAN Carrier Aggregation for 20MHz 3367

A.9.1.12.1 Test Purpose and Environment 3367

A.9.1.12.2 Test parameters 3367

A.9.1.12.3 Test Requirements 3368

A.9.1.13 TDD RSRP for E-UTRAN Carrier Aggregation for 20MHz 3368

A.9.1.13.1 Test Purpose and Environment 3368

A.9.1.13.2 Test parameters 3368

A.9.1.13.3 Test Requirements 3369

A.9.1.14 FDD RSRP under Time-Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS 3369

A.9.1.14.1 Test Purpose and Environment 3369

A.9.1.14.2 Test parameters 3369

A.9.1.14.3 Test Requirements 3373

A.9.1.15 TDD RSRP under Time-Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS 3373

A.9.1.15.1 Test Purpose and Environment 3373

A.9.1.15.2 Test parameters 3373

A.9.1.15.3 Test Requirements 3375

A.9.1.16 FDD Intra frequency case for 5MHz Bandwidth 3376

A.9.1.16.1 Test Purpose and Environment 3376

A.9.1.16.2 Test parameters 3376

A.9.1.16.3 Test Requirements 3377

A.9.1.17 FDD—FDD Inter frequency case for 5MHz Bandwidth 3377

A.9.1.17.1 Test Purpose and Environment 3377

A.9.1.17.2 Test parameters 3378

A.9.1.17.3 Test Requirements 3379

A.9.1.18 FDD RSRP for E-UTRAN Carrier Aggregation for 10MHz + 5MHz 3379

A.9.1.18.1 Test Purpose and Environment 3379

A.9.1.18.2 Test parameters 3379

A.9.1.18.3 Test Requirements 3380

A.9.1.19 TDD RSRP for E-UTRAN Carrier Aggregation for 10MHz + 5MHz 3381

A.9.1.19.1 Test Purpose and Environment 3381

A.9.1.19.2 Test parameters 3381

A.9.1.19.3 Test Requirements 3381

A.9.1.20 FDD RSRP for E-UTRAN Carrier Aggregation for 5MHz + 5MHz bandwidth 3381

A.9.1.20.1 Test Purpose and Environment 3381

A.9.1.20.2 Test parameters 3381

A.9.1.20.3 Test Requirements 3383

A.9.1.21 TDD RSRP for E-UTRAN Carrier Aggregation for 5MHz + 5MHz bandwidth 3383

A.9.1.21.1 Test Purpose and Environment 3383

A.9.1.21.2 Test parameters 3383

A.9.1.21.3 Test Requirements 3383

A.9.1.22 RSRP for E-UTRAN TDD-FDD Carrier Aggregation with PCell in FDD 3383

A.9.1.22.1 Test Purpose and Environment 3383

A.9.1.22.2 Test parameters 3384

A.9.1.22.3 Test Requirements 3388

A.9.1.23 RSRP for E-UTRAN TDD-FDD Carrier Aggregation with PCell in TDD 3388

A.9.1.23.1 Test Purpose and Environment 3388

A.9.1.23.2 Test parameters 3388

A.9.1.23.3 Test Requirements 3392

A.9.1.24 TDD RSRP for E-UTRAN Carrier Aggregation for 20MHz + 10MHz 3392

A.9.1.24.1 Test Purpose and Environment 3392

A.9.1.24.2 Test parameters 3392

A.9.1.24.3 Test Requirements 3393

A.9.1.25 FDD intra-frequency absolute and relative RSRP accuracies in CRS based discovery signal 3393

A.9.1.25.1 Test Purpose and Environment 3393

A.9.1.25.2 Test parameters 3393

A.9.1.25.3 Test Requirements 3396

A.9.1.26 TDD intra-frequency absolute and relative RSRP accuracies in CRS based discovery signal 3396

A.9.1.26.1 Test Purpose and Environment 3396

A.9.1.26.2 Test parameters 3396

A.9.1.26.3 Test Requirements 3399

A.9.1.27 FDD—FDD inter-frequency absolute and relative RSRP accuracies in CRS based discovery signal 3399

A.9.1.27.1 Test Purpose and Environment 3399

A.9.1.27.2 Test parameters 3399

A.9.1.27.3 Test Requirements 3402

A.9.1.28 TDD—TDD inter-frequency absolute and relative  RSRP accuracies in CRS based discovery signal 3402

A.9.1.28.1 Test Purpose and Environment 3402

A.9.1.28.2 Test parameters 3402

A.9.1.28.3 Test Requirements 3405

A.9.1.29 FDD intra frequency absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal 3405

A.9.1.29.1 Test Purpose and Environment 3405

A.9.1.29.2 Test parameters 3405

A.9.1.29.3 Test Requirements 3408

A.9.1.30 TDD intra frequency absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal 3408

A.9.1.30.1 Test Purpose and Environment 3408

A.9.1.30.2 Test parameters 3409

A.9.1.30.3 Test Requirements 3412

A.9.1.31 FDD—FDD inter-frequency absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal 3412

A.9.1.31.1 Test Purpose and Environment 3412

A.9.1.31.2 Test parameters 3412

A.9.1.31.3 Test Requirements 3415

A.9.1.32 TDD—TDD inter-frequency absolute and relative  CSI-RSRP accuracies in CSI-RS based discovery signal 3416

A.9.1.32.1 Test Purpose and Environment 3416

A.9.1.32.2 Test parameters 3416

A.9.1.32.3 Test Requirements 3419

A.9.1.33 FDD absolute and relative RSRP accuracies for E-UTRAN Carrier Aggregation in CRS based discovery signal 3419

A.9.1.33.1 Test Purpose and Environment 3419

A.9.1.33.2 Test parameters 3419

A.9.1.33.3 Test Requirements 3422

A.9.1.34 TDD absolute and relative RSRP accuracies for E-UTRAN Carrier Aggregation in CRS based discovery signal 3422

A.9.1.34.1 Test Purpose and Environment 3422

A.9.1.34.2 Test parameters 3422

A.9.1.34.3 Test Requirements 3425

A.9.1.35 FDD absolute and relative CSI-RSRP accuracies for E-UTRAN Carrier Aggregation in CSI-RS based discovery signal 3425

A.9.1.35.1 Test Purpose and Environment 3425

A.9.1.35.2 Test parameters 3425

A.9.1.35.3 Test Requirements 3428

A.9.1.36 TDD absolute and relative CSI-RSRP accuracies for E-UTRAN Carrier Aggregation in CSI-RS based discovery signal 3429

A.9.1.36.1 Test Purpose and Environment 3429

A.9.1.36.2 Test parameters 3429

A.9.1.36.3 Test Requirements 3432

A.9.1.37 3 DL PCell in FDD RSRP for E-UTRAN in Carrier Aggregation 3432

A.9.1.37.1 Test Purpose and Environment 3432

A.9.1.37.2 Test parameters 3432

A.9.1.37.3 Test Requirements 3435

A.9.1.38 3 DL PCell in TDD RSRP for E-UTRAN in Carrier Aggregation 3436

A.9.1.38.1 Test Purpose and Environment 3436

A.9.1.38.2 Test parameters 3436

A.9.1.38.3 Test Requirements 3439

A.9.1.39 3 DL FDD RSRP for E-UTRAN in Carrier Aggregation 3440

A.9.1.39.1 Test Purpose and Environment 3440

A.9.1.39.2 Test parameters 3440

A.9.1.39.3 Test Requirements 3446

A.9.1.40 3 DL TDD RSRP for E-UTRAN in Carrier Aggregation 3446

A.9.1.40.1 Test Purpose and Environment 3446

A.9.1.40.2 Test parameters 3447

A.9.1.40.3 Test Requirements 3453

A.9.1.41 FD-FDD RSRP Intra frequency case for UE category 0 3453

A.9.1.41.1 Test Purpose and Environment 3453

A.9.1.41.2 Test parameters 3453

A.9.1.41.3 Test Requirements 3456

A.9.1.42 HD-FDD RSRP Intra frequency case for UE category 0 3456

A.9.1.42.1 Test Purpose and Environment 3456

A.9.1.42.2 Test parameters 3456

A.9.1.42.3 Test Requirements 3459

A.9.1.43 TDD RSRP Intra frequency case for UE category 0 3459

A.9.1.43.1 Test Purpose and Environment 3459

A.9.1.43.2 Test parameters 3459

A.9.1.43.3 Test Requirements 3460

A.9.1.44 4 DL CA PCell in FDD FDD-TDD RSRP for E-UTRAN in Carrier Aggregation 3461

A.9.1.44.1 Test Purpose and Environment 3461

A.9.1.44.2 Test parameters 3461

A.9.1.44.3 Test Requirements 3466

A.9.1.45 4 DL CA PCell in TDD FDD-TDD RSRP for E-UTRAN in Carrier Aggregation 3466

A.9.1.45.1 Test Purpose and Environment 3466

A.9.1.45.2 Test parameters 3466

A.9.1.45.3 Test Requirements 3432

A.9.1.46 4 DL FDD RSRP for E-UTRAN in Carrier Aggregation 3432

A.9.1.46.1 Test Purpose and Environment 3432

A.9.1.46.2 Test parameters 3432

A.9.1.46.3 Test Requirements 3441

A.9.1.47 4 DL TDD RSRP for E-UTRAN in Carrier Aggregation 3442

A.9.1.47.1 Test Purpose and Environment 3442

A.9.1.47.2 Test parameters 3442

A.9.1.47.3 Test Requirements 3451

A.9.1.48 5 DL FDD-TDD with PCell in FDD RSRP for E-UTRAN in Carrier Aggregation 3451

A.9.1.48.1 Test Purpose and Environment 3451

A.9.1.48.2 Test parameters 3452

A.9.1.48.3 Test Requirements 3462

A.9.1.49 5 DL FDD-TDD with PCell in TDD RSRP for E-UTRAN in Carrier Aggregation 3463

A.9.1.49.1 Test Purpose and Environment 3463

A.9.1.49.2 Test parameters 3463

A.9.1.49.3 Test Requirements 3473

A.9.1.50 5 DL FDD RSRP for E-UTRAN in Carrier Aggregation 3474

A.9.1.50.1 Test Purpose and Environment 3474

A.9.1.50.2 Test parameters 3474

A.9.1.50.3 Test Requirements 3481

A.9.1.51 5 DL TDD RSRP for E-UTRAN in Carrier Aggregation 3482

A.9.1.51.1 Test Purpose and Environment 3482

A.9.1.51.2 Test parameters 3482

A.9.1.51.3 Test Requirements 3488

A.9.1.52 FD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeA 3489

A.9.1.52.1 Test Purpose and Environment 3489

A.9.1.52.2 Test parameters 3489

A.9.1.52.3 Test Requirements 3492

A.9.1.52A FD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeA 3492

A.9.1.52A.1 Test Purpose and Environment 3492

A.9.1.52A.2 Test parameters 3492

A.9.1.52A.3 Test Requirements 3493

A.9.1.53 HD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeA 3493

A.9.1.53.1 Test Purpose and Environment 3493

A.9.1.53.2 Test parameters 3494

A.9.1.53.3 Test Requirements 3497

A.9.1.53A HD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeA 3497

A.9.1.53A.1 Test Purpose and Environment 3497

A.9.1.53A.2 Test parameters 3497

A.9.1.53A.3 Test Requirements 3498

A.9.1.54 TDD RSRP Intra frequency case for Cat-M1 UE in CEModeA 3499

A.9.1.54.1 Test Purpose and Environment 3499

A.9.1.54.2 Test parameters 3499

A.9.1.54.3 Test Requirements 3501

A.9.1.55 FS3 Intra frequency absolute and relative RSRP accuracies with FDD PCell 3501

A.9.1.55.1 Test Purpose and Environment 3501

A.9.1.55.2 Test parameters 3501

A.9.1.55.3 Test Requirements 3505

A.9.1.56 FS3 Intra frequency absolute and relative RSRP accuracies with TDD PCell 3505

A.9.1.56.1 Test Purpose and Environment 3505

A.9.1.56.2 Test parameters 3505

A.9.1.56.3 Test Requirements 3508

A.9.1.57 FD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeB 3509

A.9.1.57.1 Test Purpose and Environment 3509

A.9.1.57.2 Test parameters 3509

A.9.1.57.3 Test Requirements 3512

A.9.1.57A FD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeB 3512

A.9.1.57A.1 Test Purpose and Environment 3512

A.9.1.57A.2 Test parameters 3512

A.9.1.57A.3 Test Requirements 3513

A.9.1.58 HD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeB 3513

A.9.1.58.1 Test Purpose and Environment 3513

A.9.1.58.2 Test parameters 3514

A.9.1.58.3 Test Requirements 3517

A.9.1.58A HD-FDD RSRP Intra frequency case for Cat-M1 UE for 5MHz Bandwidth in CEModeB 3517

A.9.1.58A.1 Test Purpose and Environment 3517

A.9.1.58A.2 Test parameters 3517

A.9.1.58A.3 Test Requirements 3518

A.9.1.59 TDD RSRP Intra frequency case for Cat-M1 UE in CEModeB 3518

A.9.1.59.1 Test Purpose and Environment 3518

A.9.1.59.2 Test parameters 3519

A.9.1.59.3 Test Requirements 3521

A.9.1.60 FS3 Absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal with FDD PCell 3521

A.9.1.60.1 Test Purpose and Environment 3521

A.9.1.60.2 Test parameters 3521

A.9.1.60.3 Test Requirements 3524

A.9.1.61 FS3 Absolute and relative CSI-RSRP accuracies in CSI-RS based discovery signal with TDD PCell 3525

A.9.1.61.1 Test Purpose and Environment 3525

A.9.1.61.2 Test parameters 3525

A.9.1.61.3 Test Requirements 3528

A.9.1.62 FD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeA 3528

A.9.1.62.1 Test Purpose and Environment 3528

A.9.1.62.2 Test parameters 3528

A.9.1.62.3 Test Requirements 3531

A.9.1.63 HD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeA 3531

A.9.1.53.1 Test Purpose and Environment 3531

A.9.1.53.2 Test parameters 3531

A.9.1.63.3 Test Requirements 3534

A.9.1.64 TDD RSRP Inter frequency case for Cat-M1 UE in CEModeA 3534

A.9.1.64.1 Test Purpose and Environment 3534

A.9.1.64.2 Test parameters 3534

A.9.1.64.3 Test Requirements 3535

A.9.1.65 FD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeB 3536

A.9.1.65.1 Test Purpose and Environment 3536

A.9.1.65.2 Test parameters 3536

A.9.1.65.3 Test Requirements 3542

A.9.1.66 HD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeB 3542

A.9.1.66.1 Test Purpose and Environment 3542

A.9.1.66.2 Test parameters 3542

A.9.1.66.3 Test Requirements 3548

A.9.1.67 TDD RSRP Inter frequency case for Cat-M1 UE in CEModeB 3548

A.9.1.67.1 Test Purpose and Environment 3548

A.9.1.67.2 Test parameters 3548

A.9.1.67.3 Test Requirements 3549

A.9.1.68 3 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes 3550

A.9.1.68.1 Test Purpose and Environment 3550

A.9.1.68.2 Test parameters 3550

A.9.1.68.3 Test Requirements 3554

A.9.1.69 4 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes 3554

A.9.1.69.1 Test Purpose and Environment 3554

A.9.1.69.2 Test parameters 3554

A.9.1.69.3 Test Requirements 3558

A.9.1.70 5 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes 3559

A.9.1.70.1 Test Purpose and Environment 3559

A.9.1.70.2 Test parameters 3559

A.9.1.70.3 Test Requirements 3571

A.9.1.71 6 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes 3572

A.9.1.71.1 Test Purpose and Environment 3572

A.9.1.71.2 Test parameters 3572

A.9.1.71.3 Test Requirements 3584

A.9.1.72 7 DL RSRP for E-UTRAN in Carrier Aggregation with generic duplex modes 3585

A.9.1.72.1 Test Purpose and Environment 3585

A.9.1.72.2 Test parameters 3585

A.9.1.72.3 Test Requirements 3597

A.9.1.73 FDD Intra frequency case for CA Idle Mode Measurements 3598

A.9.1.73.1 Test Purpose and Environment 3598

A.9.1.73.2 Test parameters 3598

A.9.1.73.3 Test Requirements 3601

A.9.1.74 FDD—FDD Inter frequency case for CA Idle Mode Measurements for overlapping carrier 3601

A.9.1.74.1 Test Purpose and Environment 3601

A.9.1.74.2 Test parameters 3601

A.9.1.74.3 Test Requirements 3602

A.9.1.75 FDD—FDD Inter frequency case for CA Idle Mode Measurements for non-overlapping carrier 3602

A.9.1.75.1 Test Purpose and Environment 3602

A.9.1.75.2 Test parameters 3603

A.9.1.75.3 Test Requirements 3604

A.9.1.76 FD-FDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeA 3604

A.9.1.76.1 Test Purpose and Environment 3604

A.9.1.76.2 Test parameters 3604

A.9.1.76.3 Test Requirements 3607

A.9.1.77 HD-FDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeA 3607

A.9.1.77.1 Test Purpose and Environment 3607

A.9.1.77.2 Test parameters 3607

A.9.1.77.3 Test Requirements 3610

A.9.1.78 TDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeA 3610

A.9.1.78.1 Test Purpose and Environment 3610

A.9.1.78.2 Test parameters 3610

A.9.1.78.3 Test Requirements 3613

A.9.1.79 FD-FDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeB 3613

A.9.1.79.1 Test Purpose and Environment 3613

A.9.1.79.2 Test parameters 3613

A.9.1.79.3 Test Requirements 3616

A.9.1.80 HD-FDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeB 3616

A.9.1.80.1 Test Purpose and Environment 3616

A.9.1.80.2 Test parameters 3616

A.9.1.80.3 Test Requirements 3619

A.9.1.81 TDD RSS based RSRP Intra frequency case for Cat-M1 UE in CEModeB 3619

A.9.1.81.1 Test Purpose and Environment 3619

A.9.1.78.2 Test parameters 3619

A.9.1.81.3 Test Requirements 3622

A.9.2 RSRQ 3622

A.9.2.1 FDD Intra frequency case 3622

A.9.2.1.1 Test Purpose and Environment 3622

A.9.2.1.2 Test parameters 3622

A.9.2.1.3 Test Requirements 3625

A.9.2.2 TDD Intra frequency case 3625

A.9.2.2.1 Test Purpose and Environment 3625

A.9.2.2.2 Test parameters 3625

A.9.2.2.3 Test Requirements 3627

A.9.2.3 FDD—FDD Inter frequency case 3627

A.9.2.3.1 Test Purpose and Environment 3627

A.9.2.3.2 Test parameters 3627

A.9.2.3.3 Test Requirements 3630

A.9.2.4 TDD—TDD Inter frequency case 3630

A.9.2.4.1 Test Purpose and Environment 3630

A.9.2.4.2 Test parameters 3630

A.9.2.4.3 Test Requirements 3632

A.9.2.4A FDD—TDD Inter frequency case 3633

A.9.2.4A.1 Test Purpose and Environment 3633

A.9.2.4A.2 Test parameters 3633

A.9.2.4A.3 Test Requirements 3635

A.9.2.5 FDD RSRQ for E-UTRA Carrier Aggregation 3635

A.9.2.5.1 Test Purpose and Environment 3635

A.9.2.5.2 Test parameters 3636

A.9.2.5.3 Test Requirements 3639

A.9.2.6 TDD RSRQ for E-UTRA Carrier Aggregation 3639

A.9.2.6.1 Test Purpose and Environment 3639

A.9.2.6.2 Test parameters 3639

A.9.2.6.3 Test Requirements 3642

A.9.2.7 FDD RSRQ under Time Domain Measurement Resource Restriction with Non-MBSFN ABS 3642

A.9.2.7.1 Test Purpose and Environment 3642

A.9.2.7.2 Test parameters 3642

A.9.2.7.3 Test Requirements 3646

A.9.2.8 TDD RSRQ under Time Domain Measurement Resource Restriction with Non-MBSFN ABS 3646

A.9.2.8.1 Test Purpose and Environment 3646

A.9.2.8.2 Test parameters 3646

A.9.2.8.3 Test Requirements 3650

A.9.2.9 FDD RSRQ under Time Domain Measurement Resource Restriction with MBSFN ABS 3650

A.9.2.9.1 Test Purpose and Environment 3650

A.9.2.9.2 Test parameters 3650

A.9.2.9.3 Test Requirements 3654

A.9.2.10 TDD Intra frequency case under time domain measurement resource restriction with MBSFN ABS 3654

A.9.2.10.1 Test Purpose and Environment 3654

A.9.2.10.2 Test parameters 3654

A.9.2.10.3 Test Requirements 3658

A.9.2.11 FDD RSRQ for E-UTRA Carrier Aggregation (20MHz bandwidth) 3658

A.9.2.11.1 Test Purpose and Environment 3658

A.9.2.11.2 Test parameters 3658

A.9.2.11.3 Test Requirements 3659

A.9.2.12 TDD RSRQ for E-UTRA Carrier Aggregation (20MHz bandwidth) 3659

A.9.2.12.1 Test Purpose and Environment 3659

A.9.2.12.2 Test parameters 3660

A.9.2.12.3 Test Requirements 3660

A.9.2.13 Void 3661

A.9.2.13.1 Void 3661

A.9.2.13.2 Void 3661

A.9.2.13.3 Void 3661

A.9.2.14 Void 3661

A.9.2.14.1 Void 3661

A.9.2.14.2 Void 3661

A.9.2.14.3 Void 3661

A.9.2.15 FDD RSRQ under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS 3661

A.9.2.15.1 Test Purpose and Environment 3661

A.9.2.15.2 Test parameters 3661

A.9.2.15.3 Test Requirements 3665

A.9.2.16 TDD RSRQ under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS 3665

A.9.2.16.1 Test Purpose and Environment 3665

A.9.2.16.2 Test parameters 3665

A.9.2.16.3 Test Requirements 3670

A.9.2.17 FDD Intra frequency case for 5 MHz bandwidth 3670

A.9.2.17.1 Test Purpose and Environment 3670

A.9.2.17.2 Test parameters 3670

A.9.2.17.3 Test Requirements 3672

A.9.2.18 FDD—FDD Inter frequency case for 5MHz bandwidth 3672

A.9.2.18.1 Test Purpose and Environment 3672

A.9.2.18.2 Test parameters 3672

A.9.2.18.3 Test Requirements 3675

A.9.2.19 FDD-FDD Inter Frequency WB-RSRQ 3675

A.9.2.19.1 Test Purpose and Environment 3675

A.9.2.19.2 Test parameters 3675

A.9.2.19.3 Test Requirements 3677

A.9.2.20 TDD—TDD Inter Frequency WB-RSRQ 3677

A.9.2.20.1 Test Purpose and Environment 3677

A.9.2.20.2 Test parameters 3677

A.9.2.20.3 Test Requirements 3680

A.9.2.21 FDD RSRQ for E-UTRAN Carrier Aggregation for 10MHz+5MHz 3680

A.9.2.21.1 Test Purpose and Environment 3680

A.9.2.21.2 Test parameters 3680

A.9.2.21.3 Test Requirements 3683

A.9.2.22 TDD RSRQ for E-UTRAN Carrier Aggregation for 10MHz+5MHz 3683

A.9.2.22.1 Test Purpose and Environment 3684

A.9.2.22.2 Test parameters 3684

A.9.2.22.3 Test Requirements 3684

A.9.2.23 FDD RSRQ for E-UTRA Carrier Aggregation (5MHz + 5MHz bandwidth) 3684

A.9.2.23.1 Test Purpose and Environment 3684

A.9.2.23.2 Test parameters 3684

A.9.2.23.3 Test Requirements 3687

A.9.2.24 TDD RSRQ for E-UTRA Carrier Aggregation (5MHz + 5MHz bandwidth) 3687

A.9.2.24.1 Test Purpose and Environment 3687

A.9.2.24.2 Test parameters 3687

A.9.2.24.3 Test Requirements 3688

A.9.2.25 RSRQ for E-UTRAN TDD-FDD Carrier Aggregation with PCell in FDD 3688

A.9.2.25.1 Test Purpose and Environment 3688

A.9.2.25.2 Test parameters 3688

A.9.2.25.3 Test Requirements 3693

A.9.2.26 RSRQ for E-UTRAN TDD-FDD Carrier Aggregation with PCell in TDD 3693

A.9.2.26.1 Test Purpose and Environment 3693

A.9.2.26.2 Test parameters 3693

A.9.2.26.3 Test Requirements 3697

A.9.2.27 TDD RSRQ for E-UTRAN Carrier Aggregation for 20MHz+10MHz 3697

A.9.2.27.1 Test Purpose and Environment 3697

A.9.2.27.2 Test parameters 3697

A.9.2.27.3 Test Requirements 3698

A.9.2.28 FDD intra-frequency absolute RSRQ accuracy with CRS based discovery signal 3698

A.9.2.28.1 Test Purpose and Environment 3698

A.9.2.28.2 Test parameters 3698

A.9.2.28.3 Test Requirements 3701

A.9.2.29 TDD intra-frequency absolute RSRQ accuracy with CRS based discovery signal 3701

A.9.2.29.1 Test Purpose and Environment 3701

A.9.2.29.2 Test parameters 3701

A.9.2.29.3 Test Requirements 3704

A.9.2.30 FDD-FDD inter-frequency absolute and relative RSRQ accuracies with CRS based discovery signal 3704

A.9.2.30.1 Test Purpose and Environment 3704

A.9.2.30.2 Test parameters 3704

A.9.2.30.3 Test Requirements 3707

A.9.2.31 TDD-TDD inter-frequency absolute and relative RSRQ accuracies with CRS based discovery signal 3707

A.9.2.31.1 Test Purpose and Environment 3707

A.9.2.31.2 Test parameters 3707

A.9.2.31.3 Test Requirements 3710

A.9.2.32 FDD absolute and relative RSRQ accuracy for E-UTRAN Carrier Aggregation in CRS based discovery signal 3710

A.9.2.32.1 Test Purpose and Environment 3710

A.9.2.32.2 Test parameters 3710

A.9.2.32.3 Test Requirements 3713

A.9.2.33 TDD absolute and relative RSRQ accuracy for E-UTRAN Carrier Aggregation in CRS based discovery signal 3713

A.9.2.33.1 Test Purpose and Environment 3713

A.9.2.33.2 Test parameters 3713

A.9.2.33.3 Test Requirements 3717

A.9.2.34 FDD—FDD Inter frequency new RSRQ 3717

A.9.2.34.1 Test Purpose and Environment 3717

A.9.2.34.2 Test parameters 3717

A.9.2.34.3 Test Requirements 3720

A.9.2.35 TDD—TDD Inter frequency new RSRQ 3720

A.9.2.35.1 Test Purpose and Environment 3720

A.9.2.35.2 Test parameters 3720

A.9.2.35.3 Test Requirements 3723

A.9.2.36 FDD—FDD Inter frequency RSRQ measured on all OFDM symbols 3723

A.9.2.36.1 Test Purpose and Environment 3723

A.9.2.36.2 Test parameters 3723

A.9.2.36.3 Test Requirements 3724

A.9.2.37 TDD—TDD Inter frequency RSRQ measurement on all OFDM symbols 3725

A.9.2.37.1 Test Purpose and Environment 3725

A.9.2.37.2 Test parameters 3725

A.9.2.37.3 Test Requirements 3726

A.9.2.38 3 DL PCell in FDD RSRQ for E-UTRAN in Carrier Aggregation 3727

A.9.2.38.1 Test Purpose and Environment 3727

A.9.2.38.2 Test parameters 3727

A.9.2.38.3 Test Requirements 3731

A.9.2.39 3 DL PCell in TDD RSRQ for E-UTRAN in Carrier Aggregation 3731

A.9.2.39.1 Test Purpose and Environment 3731

A.9.2.39.2 Test parameters 3731

A.9.2.39.3 Test Requirements 3735

A.9.2.40 3 DL FDD RSRQ for E-UTRAN in Carrier Aggregation 3735

A.9.2.40.1 Test Purpose and Environment 3735

A.9.2.40.2 Test parameters 3735

A.9.2.40.3 Test Requirements 3738

A.9.2.41 3 DL TDD RSRQ for E-UTRAN in Carrier Aggregation 3739

A.9.2.41.1 Test Purpose and Environment 3739

A.9.2.41.2 Test parameters 3739

A.9.2.41.3 Test Requirements 3742

A.9.2.42 FD-FDD RSRQ Intra frequency case for UE category 0 3742

A.9.2.42.1 Test Purpose and Environment 3742

A.9.2.42.2 Test parameters 3742

A.9.2.42.3 Test Requirements 3745

A.9.2.43 HD-FDD RSRQ Intra frequency case for UE category 0 3745

A.9.2.43.1 Test Purpose and Environment 3745

A.9.2.43.2 Test parameters 3745

A.9.2.43.3 Test Requirements 3748

A.9.2.44 TDD RSRQ Intra frequency case for UE category 0 3748

A.9.2.44.1 Test Purpose and Environment 3748

A.9.2.44.2 Test parameters 3748

A.9.2.44.3 Test Requirements 3750

A.9.2.45 4 DL CA PCell in FDD FDD-TDD RSRQ for E-UTRAN in Carrier Aggregation 3750

A.9.2.45.1 Test Purpose and Environment 3750

A.9.2.45.2 Test parameters 3750

A.9.2.45.3 Test Requirements 3754

A.9.2.46 4 DL CA PCell in TDD TDD-FDD RSRQ for E-UTRAN in Carrier Aggregation 3755

A.9.2.46.1 Test Purpose and Environment 3755

A.9.2.46.2 Test parameters 3755

A.9.2.46.3 Test Requirements 3759

A.9.2.47 5 DL FDD-TDD with PCell in FDD RSRQ for E-UTRAN in Carrier Aggregation 3760

A.9.2.47.1 Test Purpose and Environment 3760

A.9.2.47.2 Test parameters 3760

A.9.2.47.3 Test Requirements 3764

A.9.2.48 5 DL FDD-TDD with PCell in TDD RSRQ for E-UTRAN in Carrier Aggregation 3764

A.9.2.48.1 Test Purpose and Environment 3764

A.9.2.48.2 Test parameters 3765

A.9.2.48.3 Test Requirements 3769

A.9.2.49 5 DL FDD RSRQ for E-UTRAN in Carrier Aggregation 3770

A.9.2.49.1 Test Purpose and Environment 3770

A.9.2.49.2 Test parameters 3770

A.9.2.49.3 Test Requirements 3776

A.9.2.50 5 DL TDD RSRQ for E-UTRAN in Carrier Aggregation 3777

A.9.2.50.1 Test Purpose and Environment 3777

A.9.2.50.2 Test parameters 3777

A.9.2.50.3 Test Requirements 3783

A.9.2.51 FS3 Intra frequency absolute and relative RSRQ accuracies with FDD PCell 3783

A.9.2.51.1 Test Purpose and Environment 3783

A.9.2.51.2 Test parameters 3784

A.9.2.51.3 Test Requirements 3788

A.9.2.52 FS3 Intra frequency absolute and relative RSRQ accuracies with TDD PCell 3788

A.9.2.52.1 Test Purpose and Environment 3788

A.9.2.52.2 Test parameters 3788

A.9.2.52.3 Test Requirements 3791

A.9.2.53 4DL FDD RSRQ for E-UTRAN in Carrier Aggregation 3792

A.9.2.53.1 Test Purpose and Environment 3792

A.9.2.53.2 Test parameters 3792

A.9.2.53.3 Test Requirements 3798

A.9.2.54 4DL TDD RSRQ for E-UTRAN in Carrier Aggregation 3799

A.9.2.54.1 Test Purpose and Environment 3799

A.9.2.54.2 Test parameters 3799

A.9.2.54.3 Test Requirements 3805

A.9.2.55 3 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes 3805

A.9.2.55.1 Test Purpose and Environment 3805

A.9.2.55.2 Test parameters 3806

A.9.2.55.3 Test Requirements 3811

A.9.2.56 4 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes 3811

A.9.2.56.1 Test Purpose and Environment 3811

A.9.2.56.2 Test parameters 3811

A.9.2.56.3 Test Requirements 3816

A.9.2.57 5 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes 3816

A.9.2.57.1 Test Purpose and Environment 3816

A.9.2.57.2 Test parameters 3817

A.9.2.57.3 Test Requirements 3821

A.9.2.58 6 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes 3822

A.9.2.58.1 Test Purpose and Environment 3822

A.9.2.58.2 Test parameters 3822

A.9.2.58.3 Test Requirements 3826

A.9.2.59 7 DL RSRQ for E-UTRAN in Carrier Aggregation with generic duplex modes 3827

A.9.2.59.1 Test Purpose and Environment 3827

A.9.2.59.2 Test parameters 3827

A.9.2.59.3 Test Requirements 3832

A.9.2.60 FDD Intra frequency case for CA Idle Mode Measurements 3833

A.9.2.60.1 Test Purpose and Environment 3833

A.9.2.60.2 Test parameters 3833

A.9.2.60.3 Test Requirements 3836

A.9.2.61 FDD—FDD Inter frequency case for CA Idle Mode Measurements on overlapping carrier 3836

A.9.2.61.1 Test Purpose and Environment 3836

A.9.2.61.2 Test parameters 3836

A.9.2.61.3 Test Requirements 3839

A.9.2.62 FDD—FDD Inter frequency case for CA Idle Mode Measurements on non-overlapping carrier 3839

A.9.2.62.1 Test Purpose and Environment 3839

A.9.2.62.2 Test parameters 3839

A.9.2.62.3 Test Requirements 3842

A.9.3 UTRAN FDD CPICH RSCP 3842

A.9.3.1 E-UTRAN FDD 3842

A.9.3.1.1 Test Purpose and Environment 3842

A.9.3.1.2 Parameters 3842

A.9.3.1.3 Test Requirements 3845

A.9.3.2 E-UTRAN TDD 3845

A.9.3.2.1 Test Purpose and Environment 3845

A.9.3.2.2 Parameters 3845

A.9.3.2.3 Test Requirements 3848

A.9.3.3 E-UTRAN FDD for 5MHz Bandwidth 3848

A.9.3.3.1 Test Purpose and Environment 3848

A.9.3.3.2 Parameters 3848

A.9.3.3.3 Test Requirements 3849

A.9.4 UTRAN FDD CPICH Ec/No 3850

A.9.4.1 E-UTRAN FDD 3850

A.9.4.1.1 Test Purpose and Environment 3850

A.9.4.1.2 Parameters 3850

A.9.4.1.3 Test Requirements 3852

A.9.4.2 E-UTRAN TDD 3853

A.9.4.2.1 Test Purpose and Environment 3853

A.9.4.2.2 Parameters 3853

A.9.4.2.3 Test Requirements 3855

A.9.4.3 E-UTRAN FDD for 5MHz Bandwidth 3856

A.9.4.3.1 Test Purpose and Environment 3856

A.9.4.3.2 Parameters 3856

A.9.4.3.3 Test Requirements 3857

A.9.5 UTRAN TDD measurement 3857

A.9.5.1 P-CCPCH RSCP absolute accuracy for E-UTRAN FDD 3857

A.9.5.1.1 Test Purpose and Environment 3857

A.9.5.1.2 Test parameters 3857

A.9.5.1.3 Test Requirements 3859

A.9.5.2 P-CCPCH RSCP absolute accuracy for E-UTRAN TDD 3859

A.9.5.2.1 Test Purpose and Environment 3859

A.9.5.2.2 Test parameters 3859

A.9.5.2.3 Test Requirements 3861

A.9.6 GSM Carrier RSSI 3862

A.9.6.1 E-UTRAN FDD 3862

A.9.6.1.1 Test Purpose and Environment 3862

A.9.6.1.2 Test Requirements 3863

A.9.6.2 E-UTRAN TDD 3863

A.9.6.2.1 Test Purpose and Environment 3863

A.9.6.2.2 Test Requirements 3865

A.9.7 UE Rx – Tx Time Difference 3866

A.9.7.1 E-UTRAN FDD UE Rx – Tx time difference case 3866

A.9.7.1.1 Test Purpose and Environment 3866

A.9.7.1.2 Test parameters 3866

A.9.7.1.3 Test Requirements 3867

A.9.7.2 E-UTRA TDD UE Rx – Tx time difference case 3867

A.9.7.2.1 Test Purpose and Environment 3867

A.9.7.2.2 Test parameters 3867

A.9.7.2.3 Test Requirements 3869

A.9.7.3 E-UTRAN FDD UE Rx–Tx Time Difference under Time-Domain Measurement Resource Restriction with Non-MBSFN ABS 3869

A.9.7.3.1 Test Purpose and Environment 3869

A.9.7.3.2 Test parameters 3869

A.9.7.3.3 Test Requirements 3872

A.9.7.4 E-UTRAN TDD UE Rx-Tx Time Difference under Time-Domain Measurement Resource Restriction with Non-MBSFN ABS 3872

A.9.7.4.1 Test Purpose and Environment 3872

A.9.7.4.2 Test Parameters 3872

A.9.7.4.3 Test Requirements 3875

A.9.7.5 E-UTRAN FDD UE Rx–Tx time difference under Time Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS 3875

A.9.7.5.1 Test Purpose and Environment 3875

A.9.7.5.2 Test parameters 3875

A.9.7.5.3 Test Requirements 3878

A.9.7.6 E-UTRAN TDD UE Rx-Tx Time Difference under Time-Domain Measurement Resource Restriction with CRS Assistance Information and Non-MBSFN ABS 3878

A.9.7.6.1 Test Purpose and Environment 3878

A.9.7.6.2 Test Parameters 3878

A.9.7.6.3 Test Requirements 3881

A.9.7.7 E-UTRAN FDD UE Rx-Tx time difference case for Cat-M1/M2 UE in CEModeA 3881

A.9.7.7.1 Test Purpose and Environment 3881

A.9.7.7.2 Test parameters 3881

A.9.7.7.3 Test Requirements 3882

A.9.7.8 E-UTRAN HD-FDD UE Rx-Tx time difference case for Cat-M1/M2 UE in CEModeA 3883

A.9.7.8.1 Test Purpose and Environment 3883

A.9.7.8.2 Test parameters 3883

A.9.7.8.3 Test Requirements 3884

A.9.7.9 E-UTRAN TDD UE Rx-Tx time difference case for Cat-M1/M2 UE in CEModeA 3884

A.9.7.9.1 Test Purpose and Environment 3884

A.9.7.9.2 Test parameters 3884

A.9.7.9.3 Test Requirements 3885

A.9.8 RSTD 3886

A.9.8.1 E-UTRAN FDD RSTD intra frequency case 3886

A.9.8.1.1 Test Purpose and Environment 3886

A.9.8.1.2 Test Requirements 3888

A.9.8.1.2A Test Requirements for UE Category 1bis 3888

A.9.8.2 E-UTRAN TDD RSTD intra frequency case 3889

A.9.8.2.1 Test Purpose and Environment 3889

A.9.8.2.2 Test Requirements 3892

A.9.8.2.2A Test Requirements for UE Category 1bis 3892

A.9.8.3 E-UTRAN FDD-FDD RSTD inter frequency case 3893

A.9.8.3.1 Test Purpose and Environment 3893

A.9.8.3.2 Test Requirements 3895

A.9.8.3.2A Test Requirements for UE Category 1bis 3895

A.9.8.4 E-UTRAN TDD-TDD RSTD inter frequency case 3896

A.9.8.4.1 Test Purpose and Environment 3896

A.9.8.4.2 Test Requirements 3898

A.9.8.4.2A Test Requirements for UE Category 1bis 3898

A.9.8.5 E-UTRAN FDD RSTD Measurement Accuracy in Carrier Aggregation 3899

A.9.8.5.1 Test Purpose and Environment 3899

A.9.8.5.2 Test Requirements 3901

A.9.8.6 E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation 3901

A.9.8.6.1 Test Purpose and Environment 3901

A.9.8.6.2 Test Requirements 3904

A.9.8.7 E-UTRAN FDD RSTD Measurement Accuracy in Carrier Aggregation for 20MHz bandwidth 3904

A.9.8.7.1 Test Purpose and Environment 3904

A.9.8.7.2 Test Requirements 3905

A.9.8.8 E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation for 20MHz bandwidth 3905

A.9.8.8.1 Test Purpose and Environment 3905

A.9.8.8.2 Test Requirements 3906

A.9.8.9 E-UTRAN FDD RSTD Measurement Accuracy in Carrier Aggregation for 10MHz+5MHz 3906

A.9.8.9.1 Test Purpose and Environment 3906

A.9.8.9.2 Test Requirements 3907

A.9.8.10 E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation for 10MHz+5MHz 3907

A.9.8.10.1 Test Purpose and Environment 3907

A.9.8.10.2 Test Requirements 3908

A.9.8.11 E-UTRAN FDD RSTD Measurement Accuracy in Carrier Aggregation for 5 + 5MHz bandwidth 3908

A.9.8.11.1 Test Purpose and Environment 3908

A.9.8.11.2 Test Requirements 3909

A.9.8.12 E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation for 5+5MHz bandwidth 3909

A.9.8.12.1 Test Purpose and Environment 3909

A.9.8.12.2 Test Requirements 3910

A.9.8.13 E-UTRAN TDD RSTD Measurement Accuracy in Carrier Aggregation for 20MHz+10MHz 3910

A.9.8.13.1 Test Purpose and Environment 3910

A.9.8.13.2 Test Requirements 3911

A.9.8.14 E-UTRAN FDD RSTD Measurement Accuracy in 3DL Carrier Aggregation 3911

A.9.8.14.1 Test Purpose and Environment 3911

A.9.8.14.2 Test Requirements 3918

A.9.8.15 E-UTRAN TDD RSTD Measurement Accuracy in 3DL Carrier Aggregation 3918

A.9.8.15.1 Test Purpose and Environment 3918

A.9.8.15.2 Test Requirements 3924

A.9.8.16 HD – FDD Intra frequency case for UE Category NB1 inband mode in normal coverage 3924

A.9.8.16.1 Test Purpose and Environment 3924

A.9.8.16.2 Test Requirements 3927

A.9.8.17 HD – FDD Inter frequency case for UE Category NB1 inband mode in normal coverage 3927

A.9.8.17.1 Test Purpose and Environment 3927

A.9.8.17.2 Test Requirements 3930

A.9.8.18 HD – FDD Intra frequency case for UE Category NB1 inband mode in enhanced coverage 3930

A.9.8.18.1 Test Purpose and Environment 3930

A.9.8.18.2 Test Requirements 3933

A.9.8.19 HD – FDD Inter frequency case for UE Category NB1 inband mode in enhanced coverage 3933

A.9.8.19.1 Test Purpose and Environment 3933

A.9.8.19.2 Test Requirements 3936

A.9.8.20 E-UTRAN FDD RSTD intra-frequency measurement accuracy in CE Mode A 3936

A.9.8.20.1 Test Purpose and Environment 3936

A.9.8.20.2 Test Requirements 3939

A.9.8.21 E-UTRAN HD-FDD RSTD intra-frequency measurement accuracy in CEModeA 3940

A.9.8.21.1 Test Purpose and Environment 3940

A.9.8.21.2 Test Requirements 3943

A.9.8.22 E-UTRAN TDD RSTD intra-frequency measurement accuracy in CE Mode A 3944

A.9.8.22.1 Test Purpose and Environment 3944

A.9.8.22.2 Test Requirements 3947

A.9.8.23 E-UTRAN FDD RSTD intra-frequency measurement accuracy in CE Mode B 3948

A.9.8.23.1 Test Purpose and Environment 3948

A.9.8.23.2 Test Requirements 3951

A.9.8.24 E-UTRAN HD-FDD RSTD intra-frequency measurement accuracy in CE Mode B 3951

A.9.8.24.1 Test Purpose and Environment 3951

A.9.8.24.2 Test Requirements 3955

A.9.8.25 E-UTRAN TDD RSTD intra-frequency measurement accuracy in CE Mode B 3956

A.9.8.25.1 Test Purpose and Environment 3956

A.9.8.25.2 Test Requirements 3959

A.9.8.26 E-UTRAN FDD-FDD RSTD inter-frequency measurement accuracy in CE Mode A 3960

A.9.8.26.1 Test Purpose and Environment 3960

A.9.8.26.2 Test Requirements 3962

A.9.8.27 E-UTRAN HD-FDD RSTD inter-frequency measurement accuracy in CE Mode A 3962

A.9.8.27.1 Test Purpose and Environment 3962

A.9.8.27.2 Test Requirements 3965

A.9.8.28 E-UTRAN TDD RSTD inter-frequency measurement accuracy in CE Mode A 3965

A.9.8.28.1 Test Purpose and Environment 3965

A.9.8.28.2 Test Requirements 3968

A.9.8.29 E-UTRAN FDD-FDD RSTD inter-frequency measurement accuracy in CE Mode B 3968

A.9.8.29.1 Test Purpose and Environment 3968

A.9.8.29.2 Test Requirements 3972

A.9.8.30 E-UTRAN HD-FDD RSTD inter-frequency measurement accuracy in CE Mode B 3973

A.9.8.30.1 Test Purpose and Environment 3973

A.9.8.30.2 Test Requirements 3976

A.9.8.31 E-UTRAN TDD RSTD inter-frequency measurement accuracy in CE Mode B 3977

A.9.8.31.1 Test Purpose and Environment 3977

A.9.8.31.2 Test Requirements 3981

A.9.8.32 TDD Intra frequency case for UE Category NB1 inband mode in normal coverage 3981

A.9.8.32.1 Test Purpose and Environment 3981

A.9.8.32.2 Test Requirements 3984

A.9.8.33 TDD Inter frequency case for UE Category NB1 inband mode in normal coverage 3984

A.9.8.33.1 Test Purpose and Environment 3984

A.9.8.33.2 Test Requirements 3987

A.9.8.34 TDD Intra frequency case for UE Category NB1 inband mode in enhanced coverage 3987

A.9.8.34.1 Test Purpose and Environment 3987

A.9.8.34.2 Test Requirements 3990

A.9.8.35 TDD Inter frequency case for UE Category NB1 inband mode in enhanced coverage 3990

A.9.8.35.1 Test Purpose and Environment 3990

A.9.8.35.2 Test Requirements 3993

A.9.9 RSRP and RSRQ on the serving cell 3993

A.9.9.1 FDD Intra frequency serving cell case 3993

A.9.9.1.1 Test Purpose and Environment 3993

A.9.9.1.2 Test parameters 3993

A.9.9.1.3 Test Requirements 3996

A.9.9.2 TDD Intra frequency serving cell case 3996

A.9.9.2.1 Test Purpose and Environment 3996

A.9.9.2.2 Test parameters 3996

A.9.9.2.3 Test Requirements 3998

A.9.10 SSTD 3998

A.9.10.1 EUTRAN FDD-FDD SSTD accuracy in asynchronous DC 3998

A.9.10.1.1 Test Purpose and Environment 3998

A.9.10.1.2 Test parameters 3998

A.9.10.1.3 Test Requirements 4000

A.9.10.2 Void 4000

A.9.10.3 Void 4000

A.9.10.4 Void 4000

A.9.11 RSSI 4000

A.9.11.1 FS3 average RSSI accuracy case (PCell using FDD) 4000

A.9.11.1.1 Test Purpose and Environment 4000

A.9.11.1.2 Test parameters 4000

A.9.11.1.3 Test Requirements 4003

A.9.11.2 FS3 average RSSI accuracy case (PCell using TDD) 4003

A.9.11.2.1 Test Purpose and Environment 4003

A.9.11.2.2 Test parameters 4003

A.9.12 Channel occupancy 4006

A.9.12.1 FS3 channel occupancy test (PCell using FDD) 4006

A.9.12.1.1 Test Purpose and Environment 4006

A.9.12.1.2 Test parameters 4006

A.9.12.1.3 Test Requirements 4009

A.9.12.2 FS3 channel occupancy test (PCell using TDD) 4009

A.9.12.2.1 Test Purpose and Environment 4009

A.9.12.2.2 Test parameters 4009

A.9.12.2.3 Test Requirements 4012

A.9.13 RS-SINR 4012

A.9.13.1 FDD Intra-Frequency Case 4012

A.9.13.1.1 Test Purpose and Environment 4012

A.9.13.1.2 Test parameters 4012

A.9.13.1.3 Test Requirements 4015

A.9.13.2 TDD Intra-Frequency Case 4015

A.9.13.2.1 Test Purpose and Environment 4015

A.9.13.2.2 Test parameters 4015

A.9.13.2.3 Test Requirements 4018

A.9.13.3 FDD—FDD Inter frequency case 4018

A.9.13.3.1 Test Purpose and Environment 4018

A.9.13.3.2 Test parameters 4018

A.9.13.3.3 Test Requirements 4021

A.9.13.4 TDD—TDD Inter frequency case 4021

A.9.13.4.1 Test Purpose and Environment 4021

A.9.13.4.2 Test parameters 4021

A.9.13.4.3 Test Requirements 4025

A.9.13.5 FDD—TDD Inter frequency case 4026

A.9.13.5.1 Test Purpose and Environment 4026

A.9.13.5.2 Test parameters 4026

A.9.13.5.3 Test Requirements 4032

A.9.13.6 TDD—FDD Inter frequency case 4032

A.9.13.6.1 Test Purpose and Environment 4032

A.9.13.6.2 Test parameters 4032

A.9.13.6.3 Test Requirements 4036

A.9.14 Channel quality reporting accuracy 4036

A.9.14.1 E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category NB1 Standalone mode under normal coverage 4036

A.9.14.1.1 Test Purpose and Environment 4036

A.9.14.1.2 Test parameters 4037

A.9.14.1.3 Test Requirements 4037

A.9.14.2 E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category NB1 Standalone mode under enhanced coverage 4038

A.9.14.2.1 Test Purpose and Environment 4038

A.9.14.2.2 Test parameters 4038

A.9.14.2.3 Test Requirements 4039

A.9.14.3 E-UTRAN HD-FDD Downlink channel quality reporting accuracy on non-anchor carrier for UE Category NB1 Standalone mode under normal coverage 4039

A.9.14.3.1 Test Purpose and Environment 4039

A.9.14.3.2 Test parameters 4039

A.9.14.3.3 Test Requirements 4040

A.9.14.4 E-UTRAN HD-FDD Downlink channel quality reporting accuracy on non-anchor carrier for UE Category NB1 Standalone mode under enhanced coverage 4040

A.9.14.4.1 Test Purpose and Environment 4040

A.9.14.4.2 Test parameters 4040

A.9.14.4.3 Test Requirements 4041

A.10 Proximity-based Services in Any Cell Selection State 4064

A.10.1 E-UTRAN FDD – UE ProSe Direct Communication Transmission Timing Accuracy Test 4064

A.10.1.1 Test Purpose and Environment 4064

A.10.1.2 Test Requirements 4065

A.10.2 E-UTRAN FDD – Initiation/Cease of SLSS Transmission with ProSe Direct Communication 4066

A.10.2.1 Test Purpose and Environment 4066

A.10.2.2 Test Requirements 4067

A.10.3 E-UTRAN FDD – SyncRef UE Selection / Reselection Test 4067

A.10.3.1 Test Purpose and Environment 4067

A.10.3.2 Test Requirements 4069

A.10.4 E-UTRAN FDD – Cell Identification on downlink frequency associated with ProSe frequency (when UE is transmitting for ProSe) 4070

A.10.4.1 Test Purpose and Environment 4070

A.10.4.2 Test Requirements 4072

A.11 V2V Sidelink Communication for V2V Operation on Dedicated V2V Carrier 4072

A.11.1 V2V UE Transmission Timing Accuracy Test 4072

A.11.1.1 Test Purpose and Environment 4072

A.11.1.2 Test requirements 4073

A.11.2 Interruptions due to V2V sidelink communication 4073

A.11.2.1 Test Purpose and Environment 4073

A.11.2.2 Test Requirements 4075

A.12 4075

A.12.1 V2X UE Transmission Timing Accuracy Test 4075

A.12.1.1 V2X UE Transmission Timing Accuracy Test for eNB as Timing Reference 4075

A.12.1.1.1 Test Purpose and Environment 4075

A.12.1.1.2 Test requirements 4076

A.12.1.2 V2X UE Transmission Timing Accuracy Test for SyncRef UE as Timing Reference 4077

A.12.1.2.1 Test Purpose and Environment 4077

A.12.1.2.2 Test Requirements 4077

A.12.2 Initiation/Cease of SLSS Transmission with V2X Sidelink Communication 4078

A.12.2.1 Initiation/Cease of SLSS Transmission with V2X Sidelink Communication for eNB as Timing Reference 4078

A.12.2.1.1 Test Purpose and Environment 4078

A.12.2.1.2 Test Requirements 4079

A.12.2.2 Initiation/Cease of SLSS Transmission with V2X Sidelink Communication for SyncRef UE as Timing Reference 4080

A.12.2.2.1 Test Purpose and Environment 4080

A.12.2.2.2 Test Requirements 4081

A.12.3 V2X Synchronization Reference Selection/Reselection Tests 4081

A.12.3.1 V2X Synchronization Reference Selection/Reselection Tests for GNSS configured as the highest priority 4081

A.12.3.1.1 Test Purpose and Environment 4081

A.12.3.1.2 Test Requirements 4084

A.12.3.2 V2X Synchronization Reference Selection/Reselection Tests for eNB configured as the highest priority 4085

A.12.3.2.1 Test Purpose and Environment 4085

A.12.3.1.2 Test Requirements 4087

A.12.4 Congestion Control Measurement Test for V2X UE 4087

A.12.4.1 Test Purpose and Environment 4087

A.12.4.2 Test Requirements 4089

A.12.5 Interruptions due to V2X Sidelink Communication 4089

A.12.5.1 Test Purpose and Environment 4089

A.12.5.2 Test Requirements 4091

A.12.6 V2X UE Autonomous Resource Selection/Reselection Measurement Test 4091

A.12.6.1 V2X UE Autonomous Resource Selection/Reselection Tests for PSSCH-RSRP measurements 4091

A.12.6.1.1 Test Purpose and Environment 4091

A.12.6.1.2 Test Requirements 4093

A.12.6.2 V2X UE Autonomous Resource Selection/Reselection Tests for S-RSSI measurements 4093

A.12.6.2.1 Test Purpose and Environment 4093

A.12.6.1.2 Test Requirements 4095

A.12.7 V2X Synchronization Reference Selection/Reselection Tests for V2X Carrier Aggregation 4095

A.12.7.1 Test Purpose and Environment 4095

A.12.7.2 Test Requirements 4098

A.12.8 Interruptions due to V2X Carrier Aggregation 4099

A.12.8.1 Interruptions on a FDD PCell 4099

A.12.8.1.1 Test Purpose and Environment 4099

A.12.8.1.2 Test Requirements 4100

A.12.8.2 Interruptions on a TDD PCell 4100

A.12.8.2.1 Test Purpose and Environment 4100

A.12.8.2.2 Test Requirements 4102

A.13 E-UTRAN Standalone Tests for UE Category NB for Satellite Access 4103

A.13.1 RRC_IDLE state for satellite access 4103

A.13.1.1 Cell re-selection for satellite access 4103

A.13.1.1.1 HD – FDD and TDD Intra frequency case for UE Category NB1 Standalone mode in normal coverage 4103

A.13.1.1.1.1 Test Purpose and Environment 4103

A.13.1.1.1.2 Test Requirements 4105

A.13.1.1.2 HD – FDD Intra frequency case for UE Category NB1 Standalone mode in normal coverage with serving cell RRM measurement relaxation 4106

A.13.1.1.2.1 Test Purpose and Environment 4106

A.13.1.1.3 HD – FDD and TDD Intra frequency case for UE Category NB1 Standalone mode in normal coverage with UE specific DRX 4109

A.13.1.1.3.1 Test Purpose and Environment 4109

A.13.1.1.3.2 Test Requirements 4111

A.13.1.1.4 HD – FDD and TDD Inter frequency case for UE Category NB1 Standalone mode in normal coverage 4112

A.13.1.1.4.1 Test Purpose and Environment 4112

A.13.1.1.4.2 Test Requirements 4113

A.13.1.1.5 HD – FDD Intra frequency case for UE Category NB1 Standalone mode in enhanced coverage, location-based cell reselection for NGSO 4114

A.13.1.1.5.1 Test Purpose and Environment 4114

A.13.1.1.5.2 Test Requirements 4116

A.13.1.1.6 HD – FDD Inter frequency case for UE Category NB1 Standalone mode in enhanced coverage, time-based cell reselection for NGSO 4117

A.13.1.1.6.1 Test Purpose and Environment 4117

A.13.1.1.6.2 Test Requirements 4118

A.13.1.1.7 HD – FDD Intra frequency case for UE Category NB1 in in-band mode in NTN NR in normal coverage 4119

A.13.1.1.7.1 Test Purpose and Environment 4119

A.13.1.1.7.2 Test Requirements 4121

A.13.1.1.8 HD – FDD Inter-frequency case for UE Category NB1 in-band mode in NTN NR in normal coverage 4122

A.13.1.1.8.1 Test Purpose and Environment 4122

A.13.1.1.8.2 Test Requirements 4124

A.13.2 Void 4125

A.13.3 RRC connection mobility control for satellite access 4125

A.13.3.1 RRC re-establishment for satellite access 4125

A.13.3.1.1 HD-FDD and TDD Intra-frequency RRC Re-establishment for UE category NB1 in Standalone mode under normal coverage 4125

A.13.3.1.1.1 Test Purpose and Environment 4125

A.13.3.1.1.2 Test Requirements 4126

A.13.3.1.2 HD-FDD Intra-frequency RRC Re-establishment for UE category NB1 in Standalone mode under enhanced coverage 4127

A.13.3.1.2.1 Test Purpose and Environment 4127

A.13.3.1.2.2 Test Requirements 4128

A.13.3.1.3 HD-FDD Inter-frequency RRC Re-establishment for UE category NB1 in Standalone mode under enhanced coverage 4129

A.13.3.1.3.1 Test Purpose and Environment 4129

A.13.3.1.3.2 Test Requirements 4130

A.13.3.2 Random Access for Satellite Access 4130

A.13.3.2.1 Contention Based Random Access Test for UE category NB1 UEs in Satellite Access - Standalone mode in normal coverage 4131

A.13.3.2.1.1 Test Purpose and Environment 4131

A.13.3.2.1.2 Test Requirements 4133

A.13.3.2.2 Contention Based Random Access Test for UE category NB1 UEs in Satellite Access - Standalone mode in Enhanced Coverage 4135

A.13.3.2.2.1 Test Purpose and Environment 4135

A.13.3.2.2.2 Test Requirements 4137

A.13.3.2.3 Contention Based Random Access on Non-anchor Carrier Test for UE category NB1 UEs Standalone mode in Enhanced Coverage 4139

A.13.3.2.3.1 Test Purpose and Environment 4139

A.13.3.2.3.2 Test Requirements 4140

A.13.3.2.4 Contention Based Random Access Test for UE category NB1 UEs in Satellite Access - Standalone mode in normal coverage for CB-Msg3-EDT procedure 4142

A.13.3.2.4.1 Test Purpose and Environment 4142

A.13.3.2.4.2 Test Requirements 4144

A.13.4 Timing and signalling characteristics for satellite access 4145

A.13.4.1 UE transmit timing for satellite access 4145

A.13.4.1.1 E-UTRAN HD-FDD and TDD – UE Transmit Timing Accuracy Tests for Category NB1 UE Standalone mode under normal coverage for Satellite Access 4145

A.13.4.1.1.1 Test Purpose and Environment 4145

A.13.4.1.1.2 Test Requirements 4146

A.13.4.1.2 E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Category NB1 UE Standalone mode under enhanced coverage for Satellite Access 4147

A.13.4.1.2.1 Test Purpose and Environment 4147

A.13.4.1.2.2 Test Requirements 4149

A.13.4.1.3 E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Category NB1 UE Standalone mode under enhanced coverage with segment transmission in NGSO for Satellite Access 4149

A.13.4.1.3.1 Test Purpose and Environment 4149

A.13.4.1.3.2 Test Requirements 4151

A.13.4.2 UE timing advance for satellite access 4151

A.13.4.2.1 HD-FDD and TDD UE Timing Advance Adjustment Accuracy Test for UE Category NB1 in Standalone Mode under Normal Coverage for Satellite Access 4151

A.13.4.2.1.1 Test Purpose and Environment 4151

A.13.4.2.1.2 Test Requirements 4153

A.13.4.2.2 HD-FDD UE Timing Advance Adjustment Accuracy Test for UE Category NB1 in Standalone Mode under Enhance Coverage for Satellite Access 4153

A.13.4.2.2.1 Test Purpose and Environment 4153

A.13.4.2.2.2 Test Requirements 4155

A.13.4.3 Radio Link Monitoring for satellite access 4155

A.13.4.3.1 HD-FDD and TDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in normal coverage 4155

A.13.4.3.1.1 Test Purpose and Environment 4155

A.13.4.3.1.2 Test Requirements 4158

A.13.4.3.2 HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category NB1 Standalone mode in enhanced coverage 4158

A.13.4.3.2.1 Test Purpose and Environment 4158

A.13.4.3.2.2 Test Requirements 4161

A.13.4.3.3 HD-FDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 Standalone mode in Enhanced Coverage 4161

A.13.4.3.3.1 Test Purpose and Environment 4161

A.13.4.3.3.2 Test Requirements 4164

A.13.4.3.4 HD-FDD and TDD Radio Link Monitoring Test for In-sync with DRX for UE Category NB1 Standalone mode in Normal Coverage 4164

A.13.4.3.4.1 Test Purpose and Environment 4164

A.13.4.3.4.2 Test Requirements 4167

A.13.4.3.5 HD-FDD and TDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 Standalone mode in Normal Coverage 4167

A.13.4.3.5.1 Test Purpose and Environment 4167

A.13.4.3.5.2 Test Requirements 4170

A.13.4.3.6 HD-FDD Radio Link Monitoring Test for In-sync without DRX for UE Category NB1 Standalone mode in Enhanced Coverage 4170

A.13.4.3.6.1 Test Purpose and Environment 4170

A.13.4.3.6.2 Test Requirements 4173

A.13.4.3.7 HD-FDD and TDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 Standalone mode in Normal Coverage 4173

A.13.4.3.7.1 Test Purpose and Environment 4173

A.13.4.3.7.2 Test Requirements 4175

A.13.4.3.8 HD-FDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 Standalone mode in Enhanced Coverage 4176

A.13.4.3.8.1 Test Purpose and Environment 4176

A.13.4.3.8.2 Test Requirements 4178

A.13.4.3.9 HD-FDD Radio Link Monitoring Test for Out-of-sync without DRX for UE Category NB1 in-band mode in NTN NR in Enhanced Coverage 4179

A.13.4.3.9.1 Test Purpose and Environment 4179

A.13.4.3.9.2 Test Requirements 4182

A.13.5 UE measurement procedures in RRC_CONNECTED state for UE category NB1 for satellite access 4182

A.13.5.1 HD-FDD and TDD Intra-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access 4182

A.13.5.1.1 Test Purpose and Environment 4182

A.13.5.2 HD-FDD and TDD Inter-frequency neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access 4185

A.13.5.2.1 Test Purpose and Environment 4185

A.13.5.3 HD-FDD and TDD Intra-frequency location-based neighbour cell measurement for UE category NB1 in standalone mode under normal coverage for Satellite Access 4187

A.13.5.3.1 Test Purpose and Environment 4187

A.13.5.3.2 Test Requirements 4188

A.13.5.4 HD-FDD Intra-frequency neighbour cell measurement for UE category NB1 in in-band mode in NTN NR under normal coverage for Satellite Access 4189

A.13.5.4.1 Test Purpose and Environment 4189

A.13.5.4.2 Test Requirements 4191

A.13.5.5 HD-FDD Inter-frequency neighbour cell measurement for UE category NB1 in in-band mode in NTN NR under normal coverage for Satellite Access 4191

A.13.5.5.1 Test Purpose and Environment 4191

A.13.5.5.2 Test Requirements 4194

A.13.6 Measurement performance requirements for UE for satellite access 4195

A.13.6.1 Void 4195

A.13.6.2 Channel quality reporting accuracy for satellite access 4195

A.13.6.2.1 E-UTRAN HD-FDD and TDD Downlink channel quality reporting accuracy for UE Category NB1 Standalone mode under normal coverage 4195

A.13.6.2.1.1 Test Purpose and Environment 4195

A.13.6.2.1.2 Test parameters 4195

A.13.6.2.1.3 Test Requirements 4196

A.13.6.2.2 E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category NB1 Standalone mode under enhanced coverage 4196

A.13.6.2.2.1 Test Purpose and Environment 4196

A.13.6.2.2.2 Test parameters 4196

A.13.6.2.2.3 Test Requirements 4197

A.13.6.2.3 E-UTRAN HD-FDD and TDD Downlink channel quality reporting accuracy on non-anchor carrier for UE Category NB1 Standalone mode under normal coverage 4197

A.13.6.2.3.1 Test Purpose and Environment 4197

A.13.6.2.3.2 Test parameters 4198

A.13.6.2.3.3 Test Requirements 4199

A.13.6.2.4 E-UTRAN HD-FDD Downlink channel quality reporting accuracy on non-anchor carrier for UE Category NB1 Standalone mode under enhanced coverage 4199

A.13.6.2.4.1 Test Purpose and Environment 4199

A.13.6.2.4.2 Test parameters 4199

A.13.6.2.4.3 Test Requirements 4200

A.13.6.2.5 E-UTRAN HD-FDD and TDD Downlink channel quality reporting accuracy in RRC_CONNECTED for UE Category NB1 Standalone mode under normal coverage 4200

A.13.6.2.5.2 Test parameters 4200

A.13.6.2.5.3 Test Requirements 4202

A.13.6.2.6 E-UTRAN HD-FDD Downlink channel quality reporting accuracy in RRC_CONNECTED for UE Category NB1 Standalone mode under enhanced coverage 4202

A.13.6.2.6.1 Test Purpose and Environment 4202

A.13.6.2.6.2 Test parameters 4202

A.13.6.2.6.3 Test Requirements 4203

A.14 E-UTRAN Standalone Tests for UE Category M1 for Satellite Access 4203

A.14.1 RRC_IDLE state for satellite access 4203

A.14.1.1 Cell re-selection for satellite access 4203

A.14.1.1.1 E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage 4203

A.14.1.1.1.1 Test Purpose and Environment 4203

A.14.1.1.1.2 Test Requirements 4205

A.14.1.1.2 E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in normal coverage 4206

A.14.1.1.2.1 Test Purpose and Environment 4206

A.14.1.1.2.2 Test Requirements 4208

A.14.1.1.3 E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage with serving cell RRM measurement relaxation 4209

A.14.1.1.3.1 Test Purpose and Environment 4209

A.14.1.1.3.2 Test Requirements 4211

A.14.1.1.4 E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in normal coverage with serving cell RRM measurement relaxation 4212

A.14.1.1.4.1 Test Purpose and Environment 4212

A.14.1.1.4.2 Test Requirements 4214

A.14.1.1.5 E-UTRAN FDD – FDD Inter frequency case for Cat-M1 UE in normal coverage 4215

A.14.1.1.5.1 Test Purpose and Environment 4215

A.14.1.1.5.2 Test Requirements 4217

A.14.1.1.6 E-UTRAN HD – FDD Inter frequency case for Cat-M1 UE in normal coverage 4218

A.14.1.1.6.1 Test Purpose and Environment 4218

A.14.1.1.6.2 Test Requirements 4220

A.14.1.1.7 E-UTRAN FDD – FDD Intra frequency case for Cat-M1 UE in normal coverage, time-based triggering 4221

A.14.1.1.7.1 Test Purpose and Environment 4221

A.14.1.1.7.2 Test Requirements 4222

A.14.1.1.8 E-UTRAN HD – FDD Intra frequency case for Cat-M1 UE in enhanced coverage, time-based triggering 4223

A.14.1.1.8.1 Test Purpose and Environment 4223

A.14.1.1.8.2 Test Requirements 4224

A.14.1.1.9 E-UTRAN FDD – FDD Inter frequency case for Cat-M1 UE in enhanced coverage, location-based triggering 4225

A.14.1.1.9.1 Test Purpose and Environment 4225

A.14.1.1.9.2 Test Requirements 4226

A.14.1.1.10 E-UTRAN HD – FDD Inter frequency case for Cat-M1 UE in normal coverage, location-based triggering 4227

A.14.1.1.10.1 Test Purpose and Environment 4227

A.14.1.1.10.2 Test Requirements 4228

A.14.2 RRC_CONNECTED state mobility for satellite access 4229

A.14.2.1 E-UTRAN handover for satellite access 4229

A.14.2.1.1 E-UTRAN FDD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition 4229

A.14.2.1.1.1 Test Purpose and Environment 4229

A.14.2.1.1.2 Test Requirements 4231

A.14.2.1.2 E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA without SFN acquisition 4232

A.14.2.1.2.1 Test Purpose and Environment 4232

A.14.2.1.2.2 Test Requirements 4233

A.14.2.1.3 E-UTRAN FDD-FDD Intra frequency conditional handover for Cat-M1 UEs in CEModeA 4234

A.14.2.1.3.1 Test Purpose and Environment 4234

A.14.2.1.3.2 Test Requirements 4235

A.14.2.1.4 E-UTRAN HD-FDD Intra frequency conditional handover for Cat-M1 UEs in CEModeA 4236

A.14.2.1.4.1 Test Purpose and Environment 4236

A.14.2.1.4.2 Test Requirements 4237

A.14.2.1.5 E-UTRAN FDD Intra frequency handover for Cat-M1 UEs in CEModeA 4238

A.14.2.1.5.1 Test Purpose and Environment 4238

A.14.2.1.5.2 Test Requirements 4239

14.2.1.6 E-UTRAN HD-FDD Intra frequency handover for Cat-M1 UEs in CEModeA 4240

A.14.2.1.6.1 Test Purpose and Environment 4240

A.14.2.1.6.2 Test Requirements 4241

A.14.2.1.7 E-UTRAN FD-FDD Inter frequency handover for Cat-M1 UEs in CEModeA 4242

A.14.2.1.7.1 Test Purpose and Environment 4242

A.14.2.1.7.2 Test Requirements 4243

A.14.2.1.8 E-UTRAN HD-FDD Inter frequency handover for Cat-M1 UEs in CEModeA 4244

A.14.2.1.8.1 Test Purpose and Environment 4244

A.14.2.1.8.2 Test Requirements 4245

A.14.2.1.9 E-UTRAN FDD Inter frequency handover for Cat-M1 UEs in CEModeB 4246

A.14.2.1.9.1 Test Purpose and Environment 4246

A.14.2.1.9.2 Test Requirements 4247

A.14.2.1.10 E-UTRAN HD-FDD Inter frequency handover for Cat-M1 UEs in CEModeB 4248

A.14.2.1.10.1 Test Purpose and Environment 4248

A.14.2.1.10.2 Test Requirements 4249

A.14.2.1.11 E-UTRAN FDD-FDD Inter frequency conditional handover for Cat-M1 UEs in CEModeA 4250

A.14.2.1.11.1 Test Purpose and Environment 4250

A.14.2.1.12.2 Test Requirements 4251

A.14.2.1.12 E-UTRAN HD-FDD Inter frequency conditional handover for Cat-M1 UEs in CEModeA 4252

A.14.2.1.12.1 Test Purpose and Environment 4252

A.14.2.1.12.2 Test Requirements 4253

A.14.2.1.15 E-UTRAN FDD-FDD Inter frequency location based conditional handover for Cat-M1 UEs in CEModeA 4258

A.14.2.1.15.1 Test Purpose and Environment 4258

A.14.2.1.16.2 Test Requirements 4259

A.14.2.1.16 E-UTRAN HD-FDD Inter frequency time based conditional handover for Cat-M1 UEs in CEModeA 4260

A.14.2.1.16.1 Test Purpose and Environment 4260

A.14.2.1.16.2 Test Requirements 4261

A.14.3 RRC connection mobility control for satellite access 4262

A.14.3.1 RRC re-establishment for satellite access 4262

A.14.3.1.1 E-UTRAN FD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA for Satellite access 4262

A.14.3.1.1.1 Test Purpose and Environment 4262

A.14.3.1.1.2 Test Requirements 4263

A.14.3.1.2 E-UTRAN HD-FDD Intra-frequency RRC Re-establishment for Cat-M1 UE in CEModeA 4264

A.14.3.1.2.1 Test Purpose and Environment 4264

A.14.3.1.2.2 Test Requirements 4266

A.14.3.1.3 E-UTRAN FD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA for Satellite access 4267

A.14.3.1.3.1 Test Purpose and Environment 4267

A.14.3.1.3.2 Test Requirements 4269

A.14.3.1.4 E-UTRAN HD-FDD Inter-frequency RRC Re-establishment for Cat-M1 UE in CEModeA for Satellite access 4270

A.14.3.1.4.1 Test Purpose and Environment 4270

A.14.3.1.4.2  Test Requirements 4272

A.14.3.2 Random access for satellite access 4273

A.14.3.2.1 E-UTRAN FDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage for satellite access 4273

A.14.3.2.1.1 Test Purpose and Environment 4273

A.14.3.2.1.2 Test Requirements 4275

A.14.3.2.2 E-UTRAN HD-FDD Contention Based Random Access Test for Cat-M1 UEs in Normal Coverage for satellite access 4276

A.14.3.2.2.1 Test Purpose and Environment 4276

A.14.3.2.2.2 Test Requirements 4278

A.14.3.2.3 E-UTRAN FDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage for satellite access 4280

A.14.3.2.3.1 Test Purpose and Environment 4280

A.14.3.2.3.2 Test Requirements 4282

A.14.3.2.4 E-UTRAN HD-FDD Contention Based Random Access Test for Cat-M1 UEs in Enhanced Coverage for satellite access 4283

A.14.3.2.4.1 Test Purpose and Environment 4283

A.14.3.2.4.2 Test Requirements 4285

A.14.4 Timing and signalling characteristics for satellite access 4287

A.14.4.1 UE transmit timing for satellite access 4287

A.14.4.1.1 E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA 4287

A.14.4.1.1.1 Test Purpose and Environment 4287

A.14.4.1.1.2 Test Requirements 4289

A.14.4.1.2 E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeA 4290

A.14.4.1.2.1 Test Purpose and Environment 4290

A.14.4.1.2.2 Test Requirements 4292

A.14.4.1.3 E-UTRAN FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB 4293

A.14.4.1.3.1 Test Purpose and Environment 4293

A.14.4.1.3.2 Test Requirements 4294

A.14.4.1.4 E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB 4295

A.14.4.1.4.1 Test Purpose and Environment 4295

A.14.4.1.4.2 Test Requirements 4296

A.14.4.1.5 E-UTRAN HD-FDD – UE Transmit Timing Accuracy Tests for Cat-M1 UE in CEModeB with segment transmission in NGSO for Satellite Access 4297

A.14.4.1.5.1 Test Purpose and Environment 4297

A.14.4.1.5.2 Test Requirements 4298

A.14.4.2 UE timing advance for satellite access 4299

A.14.4.2.1 E-UTRAN FDD Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA 4299

A.14.4.2.1.1 Test Purpose and Environment 4299

A.14.4.2.1.2 Test Requirements 4302

A.14.4.2.2 E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test for Cat-M1 UE in CEModeA 4302

A.14.4.2.2.1 Test Purpose and Environment 4302

A.14.4.2.2.2 Test Requirements 4304

A.14.4.2.3 E-UTRAN FDD UE Timing Advance Adjustment Accuracy Test in CEModeB 4304

A.14.4.2.3.1 Test Purpose and Environment 4304

A.14.4.2.3.2 Test Requirements 4306

A.14.4.2.4 E-UTRAN HD-FDD UE Timing Advance Adjustment Accuracy Test in CEModeB 4306

A.14.4.2.4.1 Test Purpose and Environment 4306

A.14.4.2.4.2 Test Requirements 4307

A.14.4.3 Radio Link Monitoring for satellite access 4308

A.14.4.3.1 E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for Satellite access 4308

A.14.4.3.1.1 Test Purpose and Environment 4308

A.14.4.3.1.2 Test Requirements 4311

A.14.4.3.2 E-UTRAN FD-FDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A for Satellite access 4311

A.14.4.3.2.1 Test Purpose and Environment 4311

A.14.4.3.2.2 Test Requirements 4314

A.14.4.3.3 E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync for Cat-M1 UE in CEMode A for Satellite access 4314

A.14.4.3.3.1 Test Purpose and Environment 4314

A.14.4.3.3.2 Test Requirements 4317

A.14.4.3.4 E-UTRAN HD-FDD Radio Link Monitoring Test for In-Sync for Cat-M1 UE in CEMode A for Satellite access 4317

A.14.4.3.4.1 Test Purpose and Environment 4317

A.14.4.3.4.2 Test Requirements 4320

A.14.4.3.5 E-UTRAN FD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A 4320

A.14.4.3.5.1 Test Purpose and Environment 4320

A.14.4.3.5.2  Test Requirements 4323

A.14.4.3.6 E-UTRAN FD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A 4323

A.14.4.3.6.1 Test Purpose and Environment 4323

A.14.4.3.6.2 Test Requirements 4326

A.14.4.3.7 E-UTRAN HD-FDD Radio Link Monitoring Test for Out-of-sync in DRX for UE category M1 configured in CEMode A 4326

A.14.4.3.7.1 Test Purpose and Environment 4326

A.14.4.3.8 E-UTRAN HD-FDD Radio Link Monitoring Test for In-sync in DRX for UE Category M1 configured in CEMode A 4329

A.14.4.3.8.1  Test Purpose and Environment 4329

A.14.4.3.8.2 Test Requirements 4332

A.14.5 UE measurement procedures in RRC_CONNECTED state for satellite access 4332

A.14.5.1 Intra-frequency measurements for satellite access 4332

A.14.5.1.1 E-UTRAN FDD-FDD intra-frequency event triggered reporting under AWGN conditions in asynchronous cells for Cat-M1 UE in CEModeA 4332

A.14.5.1.1.1 Test Purpose and Environment 4332

A.14.5.1.1.2 Test Requirements 4334

A.14.5.1.2 E-UTRAN FDD-FDD intra-frequency event triggered reporting under AWGN conditions in synchronous cells for Cat-M1 UE in CEModeA in DRX 4335

A.14.5.1.2.1 Test Purpose and Environment 4335

A.14.5.1.2.2 Test Requirements 4337

A.14.5.1.3 E-UTRAN HD-FDD intra-frequency event triggered reporting under AWGN conditions in asynchronous cells for Cat-M1 UE in CEModeA 4337

A.14.5.1.3.1 Test Purpose and Environment 4337

A.14.5.1.3.2 Test Requirements 4339

A.14.5.1.4 E-UTRAN HD-FDD intra-frequency event triggered reporting under AWGN conditions in synchronous cells for Cat-M1 UE in CEModeA in DRX 4340

A.14.5.1.4.1 Test Purpose and Environment 4340

A.14.5.1.4.2 Test Requirements 4342

A.14.5.1.5 E-UTRAN FD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA with location-based triggering 4342

A.14.5.1.5.1 Test Purpose and Environment 4342

A.14.5.1.5.2 Test Requirements 4344

A.14.5.1.6  E-UTRAN HD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA with location-based triggering 4345

A.14.5.1.6.1 Test Purpose and Environment 4345

A.14.5.1.6.2 Test Requirements 4346

A.14.5.1.7 E-UTRAN HD-FDD Intra-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering 4347

A.14.5.1.7.1 Test Purpose and Environment 4347

A.14.5.1.7.2 Test Requirements 4348

A.14.5.2 Inter-frequency measurements for satellite access 4349

A.14.5.2.1 E-UTRAN FD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering 4349

A.14.5.2.1.1 Test Purpose and Environment 4349

A.14.5.2.1.2 Test Requirements 4350

A.14.5.2.2 E-UTRAN HD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeA when DRX is used with time-based triggering 4351

A.14.5.2.2.1 Test Purpose and Environment 4351

A.14.5.2.2.2 Test Requirements 4352

A.14.5.2.3 E-UTRAN HD-FDD Inter-frequency event triggered reporting in asynchronous cells for UE category M1 in CEModeB when DRX is used with time-based triggering 4353

A.14.5.2.3.1 Test Purpose and Environment 4353

A.14.5.2.3.2 Test Requirements 4354

A.14.5.2.4 E-UTRAN FDD-FDD Inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeA 4355

A.14.5.2.4.1 Test Purpose and Environment 4355

A.14.5.2.4.2 Test Requirement 4356

A.14.5.2.5 E-UTRAN FDD-FDD Inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 in CEModeA when DRX is used 4357

A.14.5.2.5.1 Test Purpose and Environment 4357

A.14.5.2.5.2 Test Requirement 4359

A.14.5.2.6 E-UTRAN HD-FDD Inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeA 4359

A.14.5.2.6.1 Test Purpose and Environment 4359

A.14.5.2.6.2 Test Requirement 4361

A.14.5.2.7 E-UTRAN HD-FDD inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 in CEModeA in DRX 4361

A.14.5.2.7.1 Test Purpose and Environment 4361

A.14.5.2.7.2 Test Requirement 4363

A.14.5.2.8 E-UTRAN FDD-FDD inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeB 4363

A.14.5.2.8.1 Test Purpose and Environment 4363

A.14.5.2.8.2 Test Requirement 4365

A.14.5.2.9 E-UTRAN HD-FDD inter-frequency event triggered reporting under AWGN conditions in asynchronous cells for UE category M1 with discontinuous MPDCCH monitoring in CEModeB 4366

A.14.5.2.9.1 Test Purpose and Environment 4366

A.14.5.2.9.2 Test Requirement 4367

A.14.6 Measurement performance requirements for UE for satellite access 4368

A.14.6.1 RSRP for satellite access 4368

A.14.6.1.1 FD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeA 4368

A.14.6.1.1.1 Test Purpose and Environment 4368

A.14.6.1.1.2 Test parameters 4368

A.14.6.1.1.3 Test Requirements 4370

A.14.6.1.2 HD-FDD RSRP Intra frequency case for Cat-M1 UE in CEModeA 4370

A.14.6.1.2.1 Test Purpose and Environment 4370

A.14.6.1.2.2 Test parameters 4370

A.14.6.1.2.3 Test Requirements 4372

A.14.6.1.3 FD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeA 4372

A.14.6.1.3.1 Test Purpose and Environment 4372

A.14.6.1.3.2 Test parameters 4372

A.14.6.1.3.3 Test Requirements 4373

A.14.6.1.4 HD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeA 4374

A.14.6.1.4.1 Test Purpose and Environment 4374

A.14.6.1.4.2 Test parameters 4374

A.14.6.1.4.3 Test Requirements 4375

A.14.6.1.5 FD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeB 4375

A.14.6.1.5.1 Test Purpose and Environment 4375

A.14.6.1.5.2 Test parameters 4375

A.14.6.1.5.3 Test Requirements 4376

A.14.6.1.6 HD-FDD RSRP Inter frequency case for Cat-M1 UE in CEModeB 4376

A.14.6.1.6.1 Test Purpose and Environment 4376

A.14.6.1.6.2 Test parameters 4377

A.14.6.1.6.3 Test Requirements 4378

A.14.6.2 Channel quality reporting accuracy for satellite access 4378

A.14.6.2.1 E-UTRAN FD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode A for Satellite access 4378

A.14.6.2.1.1 Test Purpose and Environment 4378

A.14.6.2.1.2 Test parameters 4378

A.14.6.2.1.3 Test Requirements 4379

A.14.6.2.2 E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode A for Satellite access 4380

A.14.6.2.2.1 Test Purpose and Environment 4380

A.14.6.2.2.2 Test parameters 4380

A.14.6.2.2.3 Test Requirements 4381

A.14.6.2.3.2 Test parameters 4381

A.14.6.2.3.3 Test Requirements 4382

A.14.6.2.4 E-UTRAN HD-FDD Downlink channel quality reporting accuracy for UE Category M1 in CE Mode B for Satellite access 4383

A.14.6.2.4.1 Test Purpose and Environment 4383

A.14.6.2.4.2 Test parameters 4383

A.14.6.2.4.3 Test Requirements 4384

Annex B (normative): Conditions for RRM requirements applicability for operating bands 4385

B.1 Conditions for E-UTRAN RRC_IDLE state mobility 4385

B.1.1 Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection 4385

B.1.2 Conditions for measurements of inter-frequency E-UTRAN cells for cell re-selection 4385

B.1.3 Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection for UE Category M1 4385

B.1.4 Conditions for measurements of intra-frequency NB-IoT cells for cell re-selection for UE Category NB1 4387

B.1.5 Conditions for measurements of inter-frequency NB-IoT cells for cell re-selection for UE Category NB1 4388

B.1.6 Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection for UE Category 1bis 4388

B.1.7 Conditions for measurements of E-UTRAN cells for cell re-selection for UE Category M2 4388

B.1.7.1 Conditions for measurements of intra-frequence E-UTRAN cells for cell selection 4388

B.1.7.2 Condition for measurements of inter-frequence E-UTRAN cells for cell selection 4390

B.1.8 Conditions for measurements of inter-frequency E-UTRAN cells for cell re-selection for UE Category M1 4391

B.1.9 Conditions for measurements of intra-frequency E-UTRAN cells for cell re-selection for UE Category M1 for satellite access 4391

B.1.10 Conditions for measurements of intra-frequency NB-IoT cells for cell re-selection for UE Category NB1 and NB2 for satellite access 4392

B.1.11 Conditions for measurements of inter-frequency NB-IoT cells for cell re-selection for UE Category NB1 for satellite access 4393

B.1.12 Conditions for measurements of inter-frequency E-UTRAN cells for cell re-selection for UE Category M1 for satellite access 4393

B.2 Conditions for UE Measurements Procedures in RRC_CONNECTED State 4394

B.2.1 Conditions for E-UTRAN intra-frequency measurements 4394

B.2.2 Conditions for E-UTRAN intra-frequency measurements with autonomous gaps 4394

B.2.3 Conditions for E-UTRAN inter-frequency measurements 4394

B.2.4 Conditions for E-UTRAN inter-frequency measurements with autonomous gaps 4395

B.2.5 Conditions for E-UTRAN OTDOA intra-frequency RSTD Measurements 4395

B.2.6 Conditions for E-UTRAN OTDOA inter-frequency RSTD Measurements 4396

B.2.7 Conditions for Measurements of the secondary component carrier with deactivated SCell 4396

B.2.8 Conditions for E-UTRAN Intra-Frequency Measurements under Time Domain Measurement Resource Restriction 4396

B.2.9 Conditions for E-UTRAN Intra-Frequency Measurements under Time Domain Measurement Resource Restriction with CRS Assistance Information 4397

B.2.10 Conditions for E-UTRAN intra-frequency discovery signal measurements 4397

B.2.10.1 Conditions for E-UTRAN intra-frequency CRS-based measurements 4397

B.2.10.2 Conditions for E-UTRAN intra-frequency CSI-RS based measurements 4398

B.2.11 Conditions for E-UTRAN inter-frequency discovery signal measurements 4398

B.2.11.1 Conditions for E-UTRAN inter-frequency CRS-based measurements 4398

B.2.11.2 Conditions for E-UTRAN inter-frequency CSI-RS based measurements 4399

B.2.12 Conditions for E-UTRAN intra-frequency discovery signal measurements under operation with frame structure 3 4399

B.2.13 Conditions for E-UTRAN inter-frequency discovery signal measurements under operation with frame structure 3 4399

B.2.13.1 Conditions for E-UTRAN inter-frequency CRS-based measurements 4399

B.2.13.2 Conditions for E-UTRAN inter-frequency CSI-RS based measurements 4400

B.2.14 Conditions for E-UTRAN intra-frequency measurements by UE Category M1 4400

B.2.15 Conditions for NB-IoT intra-frequency measurements by UE Category NB1 4401

B.2.16 Conditions for NB-IoT intra-frequency RSTD measurements by UE Category NB1 4402

B.2.17 Conditions for NB-IoT inter-frequency RSTD measurements by UE Category NB1 4403

B.2.18 Conditions for E-UTRAN inter-frequency measurements by UE Category M1 4404

B.2.19 Conditions for E-UTRAN measurements by UE Category M2 4405

B.2.19.1 Conditions for E-UTRAN intra-frequency measurements 4405

B.2.19.2 Conditions for E-UTRAN inter-frequency measurements 4405

B.2.20 Conditions for E-UTRAN inter-frequency RSTD measurements by UE Category M1 4405

B.2.21 Conditions for E-UTRAN inter-frequency RSTD measurements by UE Category M2 4406

B.2.22 Conditions for E-UTRAN intra-frequency RSTD measurements by UE Category M1 4406

B.2.23 Conditions for E-UTRAN intra-frequency RSTD measurements by UE Category M2 4408

B.2.24 Conditions for intra-frequency neighbour cell measurements of NB-IoT cells for UE Category NB1 4408

B.2.25 Conditions for inter-frequency neighbour cell measurements of NB-IoT cells for UE Category NB1 4408

B.2.26 Conditions for E-UTRAN intra-frequency measurements by UE Category M1 for satellite access 4408

B.2.27 Conditions for NB-IoT intra-frequency measurements by UE Category NB1 and NB2 for satellite access 4409

B.2.28 Conditions for E-UTRAN inter-frequency measurements by UE Category M1 for satellite access 4410

B.2.29 Conditions for intra-frequency neighbour cell measurements of NB-IoT cells for UE Category NB1 for satellite access 4410

B.2.30 Conditions for inter-frequency neighbour cell measurements of NB-IoT cells for UE Category NB1 for satellite access 4411

B.3 Conditions for measurements performance requirements for UE 4411

B.3.1 Conditions for intra-frequency RSRP and RSRQ Accuracy Requirements 4411

B.3.2 Void 4411

B.3.3 Conditions for inter-frequency RSRP and RSRQ Accuracy Requirements 4412

B.3.4 Conditions for inter-frequency relative RSRP and RSRQ Accuracy Requirements 4412

B.3.5 Conditions for UE Rx – Tx time difference 4412

B.3.6 Conditions for intra-frequency Reference Signal Time Difference (RSTD) measurements 4412

B.3.7 Conditions for inter-frequency RSTD measurements 4412

B.3.8 Conditions for Intra-Frequency Relative RSRP Accuracy Requirements 4412

B.3.9 Conditions for Intra-Frequency Absolute RSRP and RSRQ Accuracy Requirements under Time Domain Measurement Resource Restriction 4413

B.3.10 Conditions for Intra-Frequency Relative RSRP Accuracy Requirements under Time Domain Measurement Resource Restriction 4413

B.3.11 Conditions for Intra-Frequency Absolute RSRP and RSRQ Accuracy Requirements under Time Domain Measurement Resource Restriction with CRS Assistance Information 4413

B.3.12 Conditions for Intra-Frequency Relative RSRP Accuracy Requirements under Time Domain Measurement Resource Restriction with CRS Assistance Information 4413

B.3.13 Conditions for UE Rx–Tx Time Difference Measurement under Time Domain Measurement Resource Restriction with CRS Assistance Information 4413

B.3.14 Conditions for Intra-Frequency Absolute Discovery Signal Measurement Accuracy Requirements 4413

B.3.14.1 Conditions for Intra-frequency CRS-based measurements 4413

B.3.14.2 Conditions for Intra-frequency CSI-RS-based measurements 4414

B.3.15 Conditions for Intra-Frequency Relative Discovery Signal Measurement Accuracy Requirements 4414

B.3.15.1 Conditions for Intra-frequency CRS-based measurements 4414

B.3.15.2 Conditions for Intra-frequency CSI-RS-based measurements 4414

B.3.16 Conditions for Inter-Frequency Absolute Discovery Signal Measurement Accuracy Requirements 4415

B.3.16.1 Conditions for Inter-frequency CRS-based measurements 4415

B.3.16.2 Conditions for Inter-frequency CSI-RS-based measurements 4415

B.3.17 Conditions for Inter-Frequency Relative Discovery Signal Measurement Accuracy Requirements 4415

B.3.17.1 Conditions for Inter-frequency CRS-based measurements 4415

B.3.17.2 Conditions for Inter-frequency CSI-RS-based measurements 4415

B.3.18 Conditions for Intra-frequency Absolute RS-SINR Accuracy Requirements 4416

B.3.19 Conditions for Inter-frequency Absolute RS-SINR Accuracy Requirements 4416

B.3.20 Conditions for Inter-frequency Relative RS-SINR Accuracy Requirements 4416

B.3.21 Conditions for Intra-Frequency Absolute Accuracy Requirements for Measurements under Operation with Frame Structure 3 4416

B.3.21.1 Conditions for RSRP measurements 4416

B.3.21.2 Conditions for RSRQ measurements 4416

B.3.21.3 Conditions for CSI-RSRP measurements 4416

B.3.22 Conditions for Intra-Frequency Relative Accuracy Requirements for Measurements under Operation with Frame Structure 3 4417

B.3.22.1 Conditions for RSRP measurements 4417

B.3.22.2 Void 4417

B.3.22.3 Conditions for CSI-RSRP measurements 4417

B.3.23 Conditions for Inter-Frequency Absolute Accuracy Requirements for Measurements under Operation with Frame Structure 3 4417

B.3.23.1 Conditions for RSRP measurements 4417

B.3.23.2 Conditions for RSRQ measurements 4418

B.3.23.3 Conditions for CSI-RSRP measurements 4418

B.3.24 Conditions for Inter-Frequency Relative Accuracy Requirements for Measurements under Operation with Frame Structure 3 4418

B.3.24.1 Conditions for RSRP measurements 4418

B.3.24.2 Conditions for RSRQ measurements 4418

B.3.24.3 Conditions for CSI-RSRP measurements 4418

B.3.25 Conditions for NB-IoT intra-frequency Absolute NRSRP and NRSRQ Accuracy Requirements for UE Category NB1 4418

B.3.25A Conditions for NB-IoT intra-frequency Absolute NRSRP and NRSRQ Accuracy Requirements for UE Category NB1 for satellite access 4419

B.3.26 Conditions for NB-IoT inter-frequency Absolute NRSRP and NRSRQ Accuracy Requirements for UE Category NB1 4419

B.3.27 Conditions for intra-frequency RSRP and RSRQ Accuracy Requirements for Category 0 4419

B.3.28 Conditions for Intra-Frequency Relative RSRP Accuracy Requirements for Category 0 4419

B.3.29 Conditions for intra-frequency Reference Signal Time Difference (RSTD) measurements for NB1 4420

B.3.30 Conditions for inter-frequency Reference Signal Time Difference (RSTD) measurements for NB1 4420

B.3.31 Conditions for inter-frequency Reference Signal Time Difference (RSTD) measurements for Cat M1 4420

B.3.32 Conditions for inter-frequency Reference Signal Time Difference (RSTD) measurements for Cat M2 4420

B.3.33 Conditions for intra-frequency Reference Signal Time Difference (RSTD) measurements for Cat M1 4420

B.3.34 Conditions for intra-frequency Reference Signal Time Difference (RSTD) measurements for Cat M2 4420

B.4 RRM Requirements Exceptions 4421

B.4.1 General 4421

B.4.2 Receiver sensitivity relaxation for UE supporting CA 4421

B.4.3 Receiver sensitivity relaxation for UE configured with CA 4421

B.4.3.1 Inter-band carrier aggregation 4421

B.4.3.2 Intra-band non-contiguous carrier aggregation 4421

B.4.3.3 Inter-band carrier aggregation with operating bands without uplink band 4421

B.5 Conditions for Measurement Performance Requirements for ProSe UE 4422

B.5.1 Conditions for S-RSRP Accuracy Requirements 4422

B.5.2 Conditions for Relative S-RSRP Accuracy Requirements 4422

B.5.3 Conditions for Selection/Reselection to Intra-frequency SyncRef UE 4422

B.5.4 Conditions for SD-RSRP Accuracy Requirements 4423

B.5.5 Conditions for Relative SD-RSRP Accuracy Requirements 4423

B.6 Conditions for V2X 4424

B.6.1 Test parameters for GNSS signals 4424

B.6.2 Conditions for Absolute S-RSRP Accuracy Requirements 4424

B.6.3 Conditions for Relative S-RSRP Accuracy Requirements 4424

B.6.4 Conditions for Selection/Reselection to Intra-frequency SyncRef UE 4424

B.6.5 Conditions for Absolute PSSCH-RSRP Accuracy Requirements 4425

B.7 Conditions for sTTI and 1ms-TTI with 3 Subframe HARQ Processing 4425

B.7.1 Conditions for Maximum Timing Difference Between Uplink and Downlink Carriers in Carrier Aggregation 4425

B.8 High level test procedure for SAN RRM tests 4427

Annex C (informative): Change history: 4427
