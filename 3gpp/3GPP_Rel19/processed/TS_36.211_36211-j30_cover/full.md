3GPP TS 36.211 V19.3.0 (2026-03)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

Evolved Universal Terrestrial Radio Access (E-UTRA);

Physical channels and modulation



(Release 19)

| ![](media/image1.emf) | ![](media/image2.emf) |
| --- | --- |

The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. 
The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. 
This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.
Specifications and reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices.


Keywords

E-UTRA, radio, layer 1

3GPP

Postal address

3GPP support office address

## 650 Route des Lucioles - Sophia Antipolis

Valbonne - FRANCE

Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16

Internet

http://www.3gpp.org

Copyright Notification

No part may be reproduced except as authorized by written permission.
The copyright and the foregoing restriction extend to reproduction in all media.

© 2026, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners
LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association


Contents

Foreword 9

1 Scope 10

2 References 10

3 Symbols and abbreviations 11

3.1 Symbols 11

3.2 Abbreviations 15

4 Frame structure 15

4.1 Frame structure type 1 for FDD 16

4.2 Frame structure type 2 17

4.3 Frame structure type 3 18

4.4 Frame structure type 1 for IoT NTN TDD 19

5 Uplink 20

5.1 Overview 20

5.1.1 Physical channels 20

5.1.2 Physical signals 20

5.2 Slot structure and physical resources 20

5.2.1 Resource grid 20

5.2.2 Resource elements 22

5.2.3 Resource blocks 22

5.2.4 Narrowbands and widebands 22

5.2.5 Guard period for narrowband and wideband retuning 23

5.3 Physical uplink shared channel 26

5.3.1 Scrambling 26

5.3.2 Modulation 27

5.3.2A Layer mapping 28

5.3.2A.1 Layer mapping for transmission on a single antenna port 28

5.3.2A.2 Layer mapping for spatial multiplexing 28

5.3.3 Transform precoding 29

5.3.3A Precoding 29

5.3.3A.1 Precoding for transmission on a single antenna port 29

5.3.3A.2 Precoding for spatial multiplexing 29

5.3.4 Mapping to physical resources 32

5.4 Physical uplink control channel 38

5.4.1 PUCCH formats 1, 1a and 1b 39

5.4.2 PUCCH formats 2, 2a and 2b 42

5.4.2A PUCCH format 3 43

5.4.2B PUCCH format 4 45

5.4.2C PUCCH format 5 45

5.4.3 Mapping to physical resources 46

5.4A Short Physical Uplink Control Channel 49

5.4A.1 General 49

5.4A.2 SPUCCH formats 1,1a,1b 49

5.4A.2.1 Slot-SPUCCH 49

5.4A.2.2 Subslot-SPUCCH 50

5.4A.3 SPUCCH format 3 51

5.4A.3.1 Slot-SPUCCH 51

5.4A.4 SPUCCH format 4 51

5.4A.4.1 Slot-SPUCCH 51

5.4A.4.2 Subslot-SPUCCH 52

5.4A.5 Mapping to physical resources 52

5.5 Reference signals 56

5.5.1 Generation of the reference signal sequence 56

5.5.1.1 Base sequences of length ![](media_svg/image3.svg) [公式≈: _{3}_{N}_{sc}RB] or larger 57

5.5.1.2 Base sequences of length less than ![](media_svg/image3.svg) [公式≈: _{3}_{N}_{sc}RB] 58

5.5.1.3 Group hopping 62

5.5.1.4 Sequence hopping 63

5.5.1.5 Determining virtual cell identity for sequence generation 63

5.5.2 Demodulation reference signal 64

5.5.2.1 Demodulation reference signal for PUSCH 64

5.5.2.1.1 Reference signal sequence 64

5.5.2.1.2 Mapping to physical resources 68

5.5.2.1A Demodulation reference signal for PUSCH with sub-PRB allocations 69

5.5.2.1A.1 Reference signal sequence using modulation schemes other than π/2-BPSK 69

5.5.2.1A.2 Reference signal sequence using π/2-BPSK modulation scheme 70

5.5.2.1A.3 Group hopping 71

5.5.2.1A.4 Mapping to physical resources 72

5.5.2.2 Demodulation reference signal for PUCCH 72

5.5.2.2.1 Reference signal sequence 72

5.5.2.2.2 Mapping to physical resources 74

5.5.2.3 Demodulation reference signal for SPUCCH 75

5.5.2.3.1 Reference signal sequence 75

5.5.2.3.2 Mapping to physical resources 76

5.5.3 Sounding reference signal 77

5.5.3.1 Sequence generation 77

5.5.3.1.1 Sequence generation for basic SRS 77

5.5.3.1.2 Sequence generation for additional SRS 77

5.5.3.2 Mapping to physical resources 78

5.5.3.2.1 Mapping to physical resources for basic SRS 78

5.5.3.2.2 Mapping to physical resources for additional SRS 80

5.5.3.3 Sounding reference signal subframe configuration 81

5.6 SC-FDMA baseband signal generation 83

5.6A SC-FDMA baseband signal generation for PUSCH using sub-PRB allocations 84

5.6A.1 Modulation schemes other than π/2-BPSK 84

5.6A.2 Modulation scheme π/2-BPSK 84

5.7 Physical random access channel 85

5.7.1 Time and frequency structure 85

5.7.2 Preamble sequence generation 92

5.7.3 Baseband signal generation 97

5.8 Modulation and upconversion 98

6 Downlink 98

6.1 Overview 98

6.1.1 Physical channels 98

6.1.2 Physical signals 98

6.2 Slot structure and physical resource elements 99

6.2.1 Resource grid 99

6.2.2 Resource elements 100

6.2.3 Resource blocks 101

6.2.3.1 Virtual resource blocks of localized type 102

6.2.3.2 Virtual resource blocks of distributed type 102

6.2.4 Resource-element groups (REGs) 103

6.2.4A Enhanced Resource-Element Groups (EREGs) 104

6.2.4B Short Resource-Element Groups (SREGs) 104

6.2.5 Guard period for half-duplex FDD operation 104

6.2.6 Guard Period for TDD Operation 105

6.2.7 Narrowbands and widebands 105

6.2.8 Guard period for narrowband and wideband retuning 106

6.3 General structure for downlink physical channels 106

6.3.1 Scrambling 107

6.3.2 Modulation 108

6.3.3 Layer mapping 108

6.3.3.1 Layer mapping for transmission on a single antenna port 108

6.3.3.2 Layer mapping for spatial multiplexing 109

6.3.3.3 Layer mapping for transmit diversity 110

6.3.4 Precoding 110

6.3.4.1 Precoding for transmission on a single antenna port 110

6.3.4.2 Precoding for spatial multiplexing using antenna ports with cell-specific reference signals 111

6.3.4.2.1 Precoding without CDD 111

6.3.4.2.2 Precoding for large delay CDD 111

6.3.4.2.3 Codebook for precoding and CSI reporting 112

6.3.4.3 Precoding for transmit diversity 113

6.3.4.4 Precoding for spatial multiplexing using antenna ports with UE-specific reference signals 114

6.3.5 Mapping to resource elements 115

6.4 Physical downlink shared channel 116

6.4.1 Physical downlink shared channel for BL/CE UEs 118

6.4.2 Slot/subslot-based physical downlink shared channel 121

6.5 Physical multicast channel 123

6.5.1 Cyclic shift for PMCH 123

6.5.2 Frequency-domain interleaving 124

6.6 Physical broadcast channel 125

6.6.1 Scrambling 125

6.6.2 Modulation 125

6.6.3 Layer mapping and precoding 126

6.6.4 Mapping to resource elements 126

6.6.4.1 PBCH repetition in the cell acquisition subframe 127

6.7 Physical control format indicator channel 128

6.7.1 Scrambling 128

6.7.2 Modulation 128

6.7.3 Layer mapping and precoding 129

6.7.4 Mapping to resource elements 129

6.8 Physical downlink control channel 129

6.8.1 PDCCH formats 129

6.8.2 PDCCH multiplexing and scrambling 130

6.8.3 Modulation 130

6.8.4 Layer mapping and precoding 130

6.8.5 Mapping to resource elements 130

6.8A Enhanced physical downlink control channel 132

6.8A.1 EPDCCH formats 132

6.8A.2 Scrambling 133

6.8A.3 Modulation 133

6.8A.4 Layer mapping and precoding 134

6.8A.5 Mapping to resource elements 134

6.8B MTC physical downlink control channel 135

6.8B.1 MPDCCH formats 135

6.8B.2 Scrambling 136

6.8B.3 Modulation 136

6.8B.4 Layer mapping and precoding 137

6.8B.5 Mapping to resource elements 137

6.8C Short physical downlink control channel (SPDCCH) 140

6.8C.1 SPDCCH formats 141

6.8C.2 Scrambling 142

6.8C.3 Modulation 142

6.8C.4 Layer mapping and precoding 142

6.8C.5 Mapping to resource elements 143

6.9 Physical hybrid ARQ indicator channel 144

6.9.1 Modulation 145

6.9.2 Resource group alignment, layer mapping and precoding 146

6.9.3 Mapping to resource elements 147

6.10 Reference signals 149

6.10.1 Cell-specific Reference Signal (CRS) 149

6.10.1.1 Sequence generation 150

6.10.1.2 Mapping to resource elements 150

6.10.2 MBSFN reference signals 152

6.10.2.1 Sequence generation 152

6.10.2.1.1 Sequence generation for 15 kHz and 7.5 kHz subcarrier spacing 152

6.10.2.1.2 Sequence generation for 1.25 kHz subcarrier spacing 153

6.10.2.1.3 Sequence generation for 2.5 kHz subcarrier spacing 153

6.10.2.1.4 Sequence generation for 0.37 kHz subcarrier spacing 153

6.10.2.2 Mapping to resource elements 153

6.10.2.2.1 Mapping to resource elements for 15 kHz and 7.5 kHz subcarrier spacing 153

6.10.2.2.2 Mapping to resource elements for 1.25 kHz 155

6.10.2.2.3 Mapping to resource elements for 2.5 kHz subcarrier spacing 155

6.10.2.2.4 Mapping to resource elements for 0.37 kHz subcarrier spacing 156

6.10.3 UE-specific reference signals associated with PDSCH 156

6.10.3.1 Sequence generation 157

6.10.3.2 Mapping to resource elements 158

6.10.3A Demodulation reference signals associated with EPDCCH, MPDCCH, or SPDCCH 166

6.10.3A.1 Sequence generation 166

6.10.3A.2 Mapping to resource elements 167

6.10.4 Positioning reference signals 169

6.10.4.1 Sequence generation 169

6.10.4.2 Mapping to resource elements 170

6.10.4.3 Positioning reference signal subframe configuration 172

6.10.5 CSI reference signals 172

6.10.5.1 Sequence generation 173

6.10.5.2 Mapping to resource elements 173

6.10.5.3 CSI reference signal subframe configuration 182

6.11 Synchronization signals 182

6.11.1 Primary synchronization signal (PSS) 182

6.11.1.1 Sequence generation 182

6.11.1.2 Mapping to resource elements 183

6.11.2 Secondary synchronization signal (SSS) 183

6.11.2.1 Sequence generation 184

6.11.2.2 Mapping to resource elements 185

6.11.3 Resynchronization signal (RSS) 186

6.11.3.1 Sequence generation 186

6.11.3.2 Mapping to resource elements 186

6.11A Discovery signal 187

6.11B MTC wake-up signal (MWUS) 188

6.11B.1 Sequence generation 188

6.11B.2 Mapping to resource elements 188

6.12 OFDM baseband signal generation 189

6.13 Modulation and upconversion 189

7 Generic functions 191

7.1 Modulation mapper 191

7.1.1 BPSK 191

7.1.2 QPSK 191

7.1.3 16QAM 191

7.1.4 64QAM 192

7.1.5 256QAM 194

7.1.6 1024QAM 195

7.2 Pseudo-random sequence generation 195

8 Timing 195

8.1 Uplink-downlink frame timing 196

9 Sidelink 198

9.1 Overview 198

9.1.1 Physical channels 198

9.1.2 Physical signals 198

9.1.3 Handling of simultaneous sidelink and uplink/downlink transmissions 198

9.2 Slot structure and physical resources 199

9.2.1 Resource grid 199

9.2.2 Resource elements 199

9.2.3 Resource blocks 200

9.2.4 Resource pool 200

9.2.5 Guard period 200

9.3 Physical Sidelink Shared Channel 200

9.3.1 Scrambling 200

9.3.2 Modulation 201

9.3.3 Layer mapping 201

9.3.4 Transform precoding 201

9.3.5 Precoding 201

9.3.6 Mapping to physical resources 201

9.4 Physical Sidelink Control Channel 202

9.4.1 Scrambling 202

9.4.2 Modulation 202

9.4.3 Layer mapping 202

9.4.4 Transform precoding 202

9.4.5 Precoding 202

9.4.6 Mapping to physical resources 202

9.5 Physical Sidelink Discovery Channel 203

9.5.1 Scrambling 203

9.5.2 Modulation 203

9.5.3 Layer mapping 203

9.5.4 Transform precoding 203

9.5.5 Precoding 203

9.5.6 Mapping to physical resources 203

9.6 Physical Sidelink Broadcast Channel 204

9.6.1 Scrambling 204

9.6.2 Modulation 204

9.6.3 Layer mapping 204

9.6.4 Transform precoding 204

9.6.5 Precoding 204

9.6.6 Mapping to physical resources 204

9.7 Sidelink Synchronization Signals 204

9.7.1 Primary sidelink synchronization signal 205

9.7.1.1 Sequence generation 205

9.7.1.2 Mapping to resource elements 205

9.7.2 Secondary sidelink synchronization signal 205

9.7.2.1 Sequence generation 205

9.7.2.2 Mapping to resource elements 205

9.8 Demodulation reference signals 205

9.9 SC-FDMA baseband signal generation 207

9.10 Timing 207

10 Narrowband IoT 208

10.0 General 208

10.0.1 Frame structure 208

10.0.1.1 Frame structure type 1 208

10.0.1.2 Frame structure type 2 208

10.1 Uplink 209

10.1.1 Overview 209

10.1.1.1 Physical channels 209

10.1.1.2 Physical signals 209

10.1.2 Slot structure and physical resources 209

10.1.2.1 Resource grid 209

10.1.2.2 Resource elements 210

10.1.2.3 Resource unit 210

10.1.3 Narrowband physical uplink shared channel 211

10.1.3.1 Scrambling 211

10.1.3.2 Modulation 211

10.1.3.3 Layer mapping 212

10.1.3.4 Transform precoding 212

10.1.3.5 Precoding 212

10.1.3.6 Mapping to physical resources 212

10.1.4 Demodulation reference signal 214

10.1.4.1 Reference signal sequence 214

10.1.4.1.1 Reference signal sequence for ![](media_svg/image4.svg) [公式: N_{sc}^{RU}=1] 214

10.1.4.1.2 Reference signal sequence for ![](media_svg/image5.svg) [公式: N_{sc}^{RU}>1] 216

10.1.4.1.3 Group hopping 217

10.1.4.2 Mapping to physical resources 218

10.1.5 SC-FDMA baseband signal generation 219

10.1.6 Narrowband physical random-access channel 220

10.1.6.1 Time and frequency structure 220

10.1.6.2 Baseband signal generation 223

10.1.7 Modulation and upconversion 224

10.2 Downlink 224

10.2.1 Overview 224

10.2.1.1 Physical channels 224

10.2.1.2 Physical signals 224

10.2.2 Slot structure and physical resource elements 224

10.2.2.1 Resource grid 224

10.2.2.2 Resource elements 225

10.2.2.3 Guard period for half-duplex FDD operation 225

10.2.2.4 Guard period for TDD operation 225

10.2.3 Narrowband physical downlink shared channel 225

10.2.3.1 Scrambling 225

10.2.3.2 Modulation 225

10.2.3.3 Layer mapping and precoding 225

10.2.3.4 Mapping to resource elements 226

10.2.4 Narrowband physical broadcast channel 227

10.2.4.1 Scrambling 227

10.2.4.2 Modulation 228

10.2.4.3 Layer mapping and precoding 228

10.2.4.4 Mapping to resource elements 228

10.2.5 Narrowband physical downlink control channel 228

10.2.5.1 NPDCCH formats 228

10.2.5.2 Scrambling 229

10.2.5.3 Modulation 229

10.2.5.4 Layer mapping and precoding 229

10.2.5.5 Mapping to resource elements 229

10.2.6 Narrowband reference signal (NRS) 230

10.2.6.1 Sequence generation 234

10.2.6.2 Mapping to resource elements 234

10.2.6A Narrowband positioning reference signal (NPRS) 235

10.2.6A.1 Sequence generation 236

10.2.6A.2 Mapping to resource elements 236

10.2.6A.3 NPRS subframe configuration 237

10.2.6B Narrowband wake up signal (NWUS) 238

10.2.6B.1 Sequence generation 238

10.2.6B.2 Mapping to resource elements 238

10.2.7 Synchronization signals 239

10.2.7.1 Narrowband primary synchronization signal (NPSS) 239

10.2.7.1.1 Sequence generation 239

10.2.7.1.2 Mapping to resource elements 239

10.2.7.2 Narrowband secondary synchronization signal (NSSS) 240

10.2.7.2.1 Sequence generation 240

10.2.7.2.2 Mapping to resource elements 241

10.2.8 OFDM baseband signal generation 241

10.2.9 Modulation and upconversion 242

Annex A (informative): Change history 243
