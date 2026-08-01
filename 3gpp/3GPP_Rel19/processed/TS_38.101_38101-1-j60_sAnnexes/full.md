###### Annex A (normative):
Measurement channels

# A.1 General

The throughput values defined in the measurement channels specified in Annex A, are calculated and are valid per datastream (codeword). For multi-stream (more than one codeword) transmissions, the throughput referenced in the minimum requirements is the sum of throughputs of all datastreams (codewords).

The UE category entry in the definition of the reference measurement channel in Annex A is only informative and reveals the UE categories, which can support the corresponding measurement channel. Whether the measurement channel is used for testing a certain UE category or not is specified in the individual minimum requirements.

# A.2 UL reference measurement channels

## A.2.1 General

The measurement channels in the following clauses are defined to derive the requirements in clause 6 (Transmitter Characteristics) and clause 7 (Receiver Characteristics). The measurement channels represent example configurations of physical channels for different data rates.

The measurement channels in the following clauses are applicable to both FDD and TDD.

The active uplink slots for TDD configurations are specified in Table A.2.1-1. TDD slot patterns defined for reference sensitivity tests will be used for TDD UL RMCs, unless otherwise stated. The active uplink slots for additional TDD configuration specified in Table A.2.1-2, with the TDD pattern defined in Table A.2.1-3, is used for the phase continuity tests for DMRS bundling with 15 kHz SCS. The active uplink slots configuration specified in Table A.2.1-4 and the additional TDD pattern in Table A.2.1-5 are used for shorter transient period capability EVM tests at 15 kHz SCS.

Table A.2.1-1: TDD active uplink slots

| SCS | Active Uplink slots |
| --- | --- |
| 15 kHz | 4, 9 |
| 30 kHz | 8, 9, 18, 19 |
| 60 kHz | 16, 17, 18, 19, 36, 37, 38, 39 |

Table A.2.1-2: TDD active uplink slots for additional TDD configuration

| SCS | Active Uplink slots |
| --- | --- |
| 15 kHz | 8, 9 |

Table A.2.1-3: TDD pattern for additional TDD configuration

| Parameter |  | Value |
| --- | --- | --- |
|  |  | SCS 15 kHz (µ0) |
| TDD Slot Configuration pattern (Note 1) |  | 7DS2U |
| Special Slot Configuration (Note 2) |  | 6D+4G+4U |
| referenceSubcarrierSpacing |  | 15 kHz |
| UL-DL configuration | dl-UL-TransmissionPeriodicity | 10 ms |
|  | nrofDownlinkSlots | 7 |
|  | nrofDownlinkSymbols | 6 |
|  | nrofUplinkSlot | 2 |
|  | nrofUplinkSymbols | 4 |
| NOTE 1: D denotes a slot with all DL symbols; S denotes a slot with a mix of DL, UL and guard symbols; U denotes a slot with all UL symbols. The field is for information.NOTE 2: D, G, U denote DL, guard and UL symbols, respectively. The field is for information. |  |  |

Table A.2.1-4: TDD active uplink slots for shorter transient period capability

| SCS | Active Uplink slots |
| --- | --- |
| 15 kHz | 3,4 |

Table A.2.1-5: Additional TDD pattern for shorter transient period capability

| Parameter |  | Value |
| --- | --- | --- |
|  |  | SCS 15 kHz (µ0) |
| TDD Slot Configuration pattern (Note 1) |  | 2DS2U |
| Special Slot Configuration (Note 2) |  | 10D+2G+2U |
| referenceSubcarrierSpacing |  | 15 kHz |
| UL-DL configuration | dl-UL-TransmissionPeriodicity | 5 ms |
|  | nrofDownlinkSlots | 2 |
|  | nrofDownlinkSymbols | 10 |
|  | nrofUplinkSlot | 2 |
|  | nrofUplinkSymbols | 2 |
| NOTE 1: D denotes a slot with all DL symbols; S denotes a slot with a mix of DL, UL and guard symbols; U denotes a slot with all UL symbols. The field is for information.NOTE 2: D, G, U denote DL, guard and UL symbols, respectively. The field is for information. |  |  |

## A.2.2 Reference measurement channels

### A.2.2.1 DFT-s-OFDM Pi/2-BPSK

Table A.2.2.1-1: Reference Channels for DFT-s-OFDM Pi/2-BPSK

| Parameter | Allocated resource blocks (LCRB) | DFT-s-OFDM Symbols per slot (Note 1) | Modulation | MCS Index (Note 2) | Payload size | Transport block CRC | LDPC Base Graph | Number of code blocks per slot (Note 3) | Total number of bits per slot | Total modulated symbols per slot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unit |  |  |  |  | Bits | Bits |  |  | Bits |  |
|  | 1 | 11 | pi/2 BPSK | 0 | 24 | 16 | 2 | 1 | 132 | 132 |
|  | 5 | 11 | pi/2 BPSK | 0 | 160 | 16 | 2 | 1 | 660 | 660 |
|  | 9 | 11 | pi/2 BPSK | 0 | 288 | 16 | 2 | 1 | 1188 | 1188 |
|  | 10 | 11 | pi/2 BPSK | 0 | 320 | 16 | 2 | 1 | 1320 | 1320 |
|  | 12 | 11 | pi/2 BPSK | 0 | 384 | 16 | 2 | 1 | 1584 | 1584 |
|  | 15 | 11 | pi/2 BPSK | 0 | 480 | 16 | 2 | 1 | 1980 | 1980 |
|  | 18 | 11 | pi/2 BPSK | 0 | 576 | 16 | 2 | 1 | 2376 | 2376 |
|  | 24 | 11 | pi/2 BPSK | 0 | 768 | 16 | 2 | 1 | 3168 | 3168 |
|  | 25 | 11 | pi/2 BPSK | 0 | 808 | 16 | 2 | 1 | 3300 | 3300 |
|  | 30 | 11 | pi/2 BPSK | 0 | 984 | 16 | 2 | 1 | 3960 | 3960 |
|  | 32 | 11 | pi/2 BPSK | 0 | 1032 | 16 | 2 | 1 | 4224 | 4224 |
|  | 36 | 11 | pi/2 BPSK | 0 | 1128 | 16 | 2 | 1 | 4752 | 4752 |
|  | 45 | 11 | pi/2 BPSK | 0 | 1416 | 16 | 2 | 1 | 5940 | 5940 |
|  | 50 | 11 | pi/2 BPSK | 0 | 1544 | 16 | 2 | 1 | 6600 | 6600 |
|  | 60 | 11 | pi/2 BPSK | 0 | 1864 | 16 | 2 | 1 | 7920 | 7920 |
|  | 64 | 11 | pi/2 BPSK | 0 | 2024 | 16 | 2 | 1 | 8448 | 8448 |
|  | 75 | 11 | pi/2 BPSK | 0 | 2408 | 16 | 2 | 1 | 9900 | 9900 |
|  | 80 | 11 | pi/2 BPSK | 0 | 2472 | 16 | 2 | 1 | 10560 | 10560 |
|  | 81 | 11 | pi/2 BPSK | 0 | 2536 | 16 | 2 | 1 | 10692 | 10692 |
|  | 90 | 11 | pi/2 BPSK | 0 | 2792 | 16 | 2 | 1 | 11880 | 11880 |
|  | 100 | 11 | pi/2 BPSK | 0 | 3104 | 16 | 2 | 1 | 13200 | 13200 |
|  | 108 | 11 | pi/2 BPSK | 0 | 3368 | 16 | 2 | 1 | 14256 | 14256 |
|  | 120 | 11 | pi/2 BPSK | 0 | 3752 | 16 | 2 | 1 | 15840 | 15840 |
|  | 128 | 11 | pi/2 BPSK | 0 | 3976 | 24 | 2 | 2 | 16896 | 16896 |
|  | 135 | 11 | pi/2 BPSK | 0 | 4104 | 24 | 2 | 2 | 17820 | 17820 |
|  | 160 | 11 | pi/2 BPSK | 0 | 4872 | 24 | 2 | 2 | 21120 | 21120 |
|  | 162 | 11 | pi/2 BPSK | 0 | 5000 | 24 | 2 | 2 | 21384 | 21384 |
|  | 180 | 11 | pi/2 BPSK | 0 | 5512 | 24 | 2 | 2 | 23760 | 23760 |
|  | 216 | 11 | pi/2 BPSK | 0 | 6664 | 24 | 2 | 2 | 28512 | 28512 |
|  | 243 | 11 | pi/2 BPSK | 0 | 7560 | 24 | 2 | 2 | 32076 | 32076 |
|  | 270 | 11 | pi/2 BPSK | 0 | 8448 | 24 | 2 | 3 | 35640 | 35640 |
| NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.NOTE 2: MCS Index is based on MCS Table 6.1.4.1-1 defined in TS 38.214 [10].NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 4: The RMCs apply to all channel bandwidth where LCRB ≤ NRB. |  |  |  |  |  |  |  |  |  |  |

Table A.2.2.1-2: Void

Table A.2.2.1-3: Void

### A.2.2.2 DFT-s-OFDM QPSK

Table A.2.2.2-1: Reference Channels for DFT-s-OFDM QPSK

| Parameter | Allocated resource blocks (LCRB) | DFT-s-OFDM Symbols per slot (Note 1) | Modulation | MCS Index (Note 2) | Payload size | Transport block CRC | LDPC Base Graph | Number of code blocks per slot (Note 3) | Total number of bits per slot | Total modulated symbols per slot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unit |  |  |  |  | Bits | Bits |  |  | Bits |  |
|  | 1 | 11 | QPSK | 2 | 48 | 16 | 2 | 1 | 264 | 132 |
|  | 4 | 11 | QPSK | 2 | 200 | 16 | 2 | 1 | 1056 | 528 |
|  | 5 | 11 | QPSK | 2 | 256 | 16 | 2 | 1 | 1320 | 660 |
|  | 6 | 11 | QPSK | 2 | 304 | 16 | 2 | 1 | 1584 | 792 |
|  | 8 | 11 | QPSK | 2 | 408 | 16 | 2 | 1 | 2112 | 1056 |
|  | 9 | 11 | QPSK | 2 | 456 | 16 | 2 | 1 | 2376 | 1188 |
|  | 10 | 11 | QPSK | 2 | 504 | 16 | 2 | 1 | 2640 | 1320 |
|  | 12 | 11 | QPSK | 2 | 608 | 16 | 2 | 1 | 3168 | 1584 |
|  | 15 | 11 | QPSK | 2 | 768 | 16 | 2 | 1 | 3960 | 1980 |
|  | 16 | 11 | QPSK | 2 | 808 | 16 | 2 | 1 | 4224 | 2112 |
|  | 18 | 11 | QPSK | 2 | 928 | 16 | 2 | 1 | 4752 | 2376 |
|  | 20 | 11 | QPSK | 2 | 1032 | 16 | 2 | 1 | 5280 | 2640 |
|  | 24 | 11 | QPSK | 2 | 1192 | 16 | 2 | 1 | 6336 | 3168 |
|  | 25 | 11 | QPSK | 2 | 1256 | 16 | 2 | 1 | 6600 | 3300 |
|  | 30 | 11 | QPSK | 2 | 1544 | 16 | 2 | 1 | 7920 | 3960 |
|  | 32 | 11 | QPSK | 2 | 1608 | 16 | 2 | 1 | 8448 | 4224 |
|  | 36 | 11 | QPSK | 2 | 1800 | 16 | 2 | 1 | 9504 | 4752 |
|  | 40 | 11 | QPSK | 2 | 2024 | 16 | 2 | 1 | 10560 | 5280 |
|  | 45 | 11 | QPKS | 2 | 2208 | 16 | 2 | 1 | 11880 | 5940 |
|  | 50 | 11 | QPSK | 2 | 2472 | 16 | 2 | 1 | 13200 | 6600 |
|  | 60 | 11 | QPSK | 2 | 3104 | 16 | 2 | 1 | 15840 | 7920 |
|  | 64 | 11 | QPSK | 2 | 3240 | 16 | 2 | 1 | 16896 | 8448 |
|  | 75 | 11 | QPSK | 2 | 3752 | 16 | 2 | 1 | 19800 | 9900 |
|  | 80 | 11 | QPSK | 2 | 3976 | 24 | 2 | 2 | 21120 | 10560 |
|  | 81 | 11 | QPSK | 2 | 4040 | 24 | 2 | 2 | 21384 | 10692 |
|  | 90 | 11 | QPSK | 2 | 4488 | 24 | 2 | 2 | 23760 | 11880 |
|  | 100 | 11 | QPSK | 2 | 5000 | 24 | 2 | 2 | 26400 | 13200 |
|  | 108 | 11 | QPSK | 2 | 5384 | 24 | 2 | 2 | 28512 | 14256 |
|  | 120 | 11 | QPSK | 2 | 5896 | 24 | 2 | 2 | 31680 | 15840 |
|  | 128 | 11 | QPSK | 2 | 6408 | 24 | 2 | 2 | 33792 | 16896 |
|  | 135 | 11 | QPSK | 2 | 6664 | 24 | 2 | 2 | 35640 | 17820 |
|  | 160 | 11 | QPSK | 2 | 7944 | 24 | 2 | 3 | 42240 | 21120 |
|  | 162 | 11 | QPSK | 2 | 8064 | 24 | 2 | 3 | 42768 | 21384 |
|  | 180 | 11 | QPSK | 2 | 8976 | 24 | 2 | 3 | 47520 | 23760 |
|  | 216 | 11 | QPSK | 2 | 10752 | 24 | 2 | 3 | 57024 | 28512 |
|  | 240 | 11 | QPSK | 2 | 11776 | 24 | 2 | 4 | 63360 | 31680 |
|  | 243 | 11 | QPSK | 2 | 12040 | 24 | 2 | 4 | 64152 | 32076 |
|  | 270 | 11 | QPSK | 2 | 13320 | 24 | 2 | 4 | 71280 | 35640 |
| NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.NOTE 2: MCS Index is based on MCS Table 6.1.4.1-1 defined in TS 38.214 [10].NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 4: The RMCs apply to all channel bandwidth where LCRB ≤ NRB. |  |  |  |  |  |  |  |  |  |  |

Table A.2.2.2-2: Void

Table A.2.2.2-3: Void

### A.2.2.3 DFT-s-OFDM 16QAM

Table A.2.2.3-1: Reference Channels for DFT-s-OFDM 16QAM

| Parameter | Allocated resource blocks (LCRB) | DFT-s-OFDM Symbols per slot (Note 1) | Modulation | MCS Index (Note 2) | Payload size | Transport block CRC | LDPC Base Graph | Number of code blocks per slot (Note 3) | Total number of bits per slot | Total modulated symbols per slot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unit |  |  |  |  | Bits | Bits |  |  | Bits |  |
|  | 1 | 11 | 16QAM | 10 | 176 | 16 | 2 | 1 | 528 | 132 |
|  | 5 | 11 | 16QAM | 10 | 888 | 16 | 2 | 1 | 2640 | 660 |
|  | 9 | 11 | 16QAM | 10 | 1608 | 16 | 2 | 1 | 4752 | 1188 |
|  | 10 | 11 | 16QAM | 10 | 1800 | 16 | 2 | 1 | 5280 | 1320 |
|  | 12 | 11 | 16QAM | 10 | 2088 | 16 | 2 | 1 | 6336 | 1584 |
|  | 15 | 11 | 16QAM | 10 | 2664 | 16 | 2 | 1 | 7920 | 1980 |
|  | 18 | 11 | 16QAM | 10 | 3240 | 16 | 2 | 1 | 9504 | 2376 |
|  | 24 | 11 | 16QAM | 10 | 4224 | 24 | 1 | 1 | 12672 | 3168 |
|  | 25 | 11 | 16QAM | 10 | 4352 | 24 | 1 | 1 | 13200 | 3300 |
|  | 30 | 11 | 16QAM | 10 | 5248 | 24 | 1 | 1 | 15840 | 3960 |
|  | 32 | 11 | 16QAM | 10 | 5632 | 24 | 1 | 1 | 16896 | 4224 |
|  | 36 | 11 | 16QAM | 10 | 6272 | 24 | 1 | 1 | 19008 | 4752 |
|  | 45 | 11 | 16QAM | 10 | 7808 | 24 | 1 | 1 | 23760 | 5940 |
|  | 50 | 11 | 16QAM | 10 | 8712 | 24 | 1 | 2 | 26400 | 6600 |
|  | 60 | 11 | 16QAM | 10 | 10504 | 24 | 1 | 2 | 31680 | 7920 |
|  | 64 | 11 | 16QAM | 10 | 11272 | 24 | 1 | 2 | 33792 | 8448 |
|  | 75 | 11 | 16QAM | 10 | 13064 | 24 | 1 | 2 | 39600 | 9900 |
|  | 80 | 11 | 16QAM | 10 | 14088 | 24 | 1 | 2 | 42240 | 10560 |
|  | 81 | 11 | 16QAM | 10 | 14088 | 24 | 1 | 2 | 42768 | 10692 |
|  | 100 | 11 | 16QAM | 10 | 17424 | 24 | 1 | 3 | 52800 | 13200 |
|  | 108 | 11 | 16QAM | 10 | 18960 | 24 | 1 | 3 | 57024 | 14256 |
|  | 120 | 11 | 16QAM | 10 | 21000 | 24 | 1 | 3 | 63360 | 15840 |
|  | 128 | 11 | 16QAM | 10 | 22536 | 24 | 1 | 3 | 67584 | 16896 |
|  | 135 | 11 | 16QAM | 10 | 23568 | 24 | 1 | 3 | 71280 | 17820 |
|  | 160 | 11 | 16QAM | 10 | 28168 | 24 | 1 | 4 | 84480 | 21120 |
|  | 162 | 11 | 16QAM | 10 | 28168 | 24 | 1 | 4 | 85536 | 21384 |
|  | 216 | 11 | 16QAM | 10 | 37896 | 24 | 1 | 5 | 114048 | 28512 |
|  | 243 | 11 | 16QAM | 10 | 43032 | 24 | 1 | 6 | 128304 | 32076 |
|  | 270 | 11 | 16QAM | 10 | 47112 | 24 | 1 | 6 | 142560 | 35640 |
| NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.NOTE 2: MCS Index is based on MCS Table 6.1.4.1-1 defined in TS 38.214 [10].NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 4: The RMCs apply to all channel bandwidth where LCRB ≤ NRB. |  |  |  |  |  |  |  |  |  |  |

Table A.2.2.3-2: Void

Table A.2.2.3-3: Void

### A.2.2.4 DFT-s-OFDM 64QAM

Table A.2.2.4-1: Reference Channels for DFT-s-OFDM 64QAM

| Parameter | Allocated resource blocks (LCRB) | DFT-s-OFDM Symbols per slot (Note 1) | Modulation | MCS Index (Note 2) | Payload size | Transport block CRC | LDPC Base Graph | Number of code blocks per slot (Note 3) | Total number of bits per slot | Total modulated symbols per slot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unit |  |  |  |  | Bits | Bits |  |  | Bits |  |
|  | 1 | 11 | 64QAM | 18 | 408 | 16 | 2 | 1 | 792 | 132 |
|  | 5 | 11 | 64QAM | 18 | 2024 | 16 | 2 | 1 | 3960 | 660 |
|  | 9 | 11 | 64QAM | 18 | 3624 | 16 | 2 | 1 | 7128 | 1188 |
|  | 10 | 11 | 64QAM | 18 | 3968 | 24 | 1 | 1 | 7920 | 1320 |
|  | 12 | 11 | 64QAM | 18 | 4736 | 24 | 1 | 1 | 9504 | 1584 |
|  | 15 | 11 | 64QAM | 18 | 6016 | 24 | 1 | 1 | 11880 | 1980 |
|  | 18 | 11 | 64QAM | 18 | 7168 | 24 | 1 | 1 | 14256 | 2376 |
|  | 24 | 11 | 64QAM | 18 | 9480 | 24 | 1 | 2 | 19008 | 3168 |
|  | 25 | 11 | 64QAM | 18 | 9992 | 24 | 1 | 2 | 19800 | 3300 |
|  | 30 | 11 | 64QAM | 18 | 12040 | 24 | 1 | 2 | 23760 | 3960 |
|  | 32 | 11 | 64QAM | 18 | 12808 | 24 | 1 | 2 | 25344 | 4224 |
|  | 36 | 11 | 64QAM | 18 | 14344 | 24 | 1 | 2 | 28512 | 4752 |
|  | 45 | 11 | 64QAM | 18 | 17928 | 24 | 1 | 3 | 35640 | 5940 |
|  | 50 | 11 | 64QAM | 18 | 19968 | 24 | 1 | 3 | 39600 | 6600 |
|  | 60 | 11 | 64QAM | 18 | 24072 | 24 | 1 | 3 | 47520 | 7920 |
|  | 64 | 11 | 64QAM | 18 | 25608 | 24 | 1 | 4 | 50688 | 8448 |
|  | 75 | 11 | 64QAM | 18 | 30216 | 24 | 1 | 4 | 59400 | 9900 |
|  | 80 | 11 | 64QAM | 18 | 31752 | 24 | 1 | 4 | 63360 | 10560 |
|  | 81 | 11 | 64QAM | 18 | 32264 | 24 | 1 | 4 | 64152 | 10692 |
|  | 90 | 11 | 64QAM | 18 | 35856 | 24 | 1 | 5 | 71280 | 11880 |
|  | 100 | 11 | 64QAM | 18 | 39936 | 24 | 1 | 5 | 79200 | 13200 |
|  | 108 | 11 | 64QAM | 18 | 43032 | 24 | 1 | 6 | 85536 | 14256 |
|  | 120 | 11 | 64QAM | 18 | 48168 | 24 | 1 | 6 | 95040 | 15840 |
|  | 128 | 11 | 64QAM | 18 | 51216 | 24 | 1 | 7 | 101376 | 16896 |
|  | 135 | 11 | 64QAM | 18 | 54296 | 24 | 1 | 7 | 106920 | 17820 |
|  | 160 | 11 | 64QAM | 18 | 63528 | 24 | 1 | 8 | 126720 | 21120 |
|  | 162 | 11 | 64QAM | 18 | 64552 | 24 | 1 | 8 | 128304 | 21384 |
|  | 180 | 11 | 64QAM | 18 | 71688 | 24 | 1 | 9 | 142560 | 23760 |
|  | 216 | 11 | 64QAM | 18 | 86040 | 24 | 1 | 11 | 171072 | 28512 |
|  | 243 | 11 | 64QAM | 18 | 96264 | 24 | 1 | 12 | 192456 | 32076 |
|  | 270 | 11 | 64QAM | 18 | 108552 | 24 | 1 | 13 | 213840 | 35640 |
| NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.NOTE 2: MCS Index is based on MCS Table 6.1.4.1-1 defined in TS 38.214 [10].NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 4: The RMCs apply to all channel bandwidth where LCRB ≤ NRB. |  |  |  |  |  |  |  |  |  |  |

Table A.2.2.4-2: Void

Table A.2.2.4-3: Void

### A.2.2.5 DFT-s-OFDM 256QAM

Table A.2.2.5-1: Reference Channels for DFT-s-OFDM 256QAM

| Parameter | Allocated resource blocks (LCRB) | DFT-s-OFDM Symbols per slot (Note 1) | Modulation | MCS Index (Note 2) | Payload size | Transport block CRC | LDPC Base Graph | Number of code blocks per slot (Note 3) | Total number of bits per slot | Total modulated symbols per slot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unit |  |  |  |  | Bits | Bits |  |  | Bits |  |
|  | 1 | 11 | 256QAM | 20 | 704 | 16 | 2 | 1 | 1056 | 132 |
|  | 5 | 11 | 256QAM | 20 | 3496 | 16 | 2 | 1 | 5280 | 660 |
|  | 9 | 11 | 256QAM | 20 | 6272 | 24 | 1 | 1 | 9504 | 1188 |
|  | 10 | 11 | 256QAM | 20 | 7040 | 24 | 1 | 1 | 10560 | 1320 |
|  | 12 | 11 | 256QAM | 20 | 8456 | 24 | 1 | 2 | 12672 | 1584 |
|  | 15 | 11 | 256QAM | 20 | 10504 | 24 | 1 | 2 | 15840 | 1980 |
|  | 18 | 11 | 256QAM | 20 | 12552 | 24 | 1 | 2 | 19008 | 2376 |
|  | 24 | 11 | 256QAM | 20 | 16896 | 24 | 1 | 3 | 25344 | 3168 |
|  | 25 | 11 | 256QAM | 20 | 17424 | 24 | 1 | 3 | 26400 | 3300 |
|  | 30 | 11 | 256QAM | 20 | 21000 | 24 | 1 | 3 | 31680 | 3960 |
|  | 32 | 11 | 256QAM | 20 | 22536 | 24 | 1 | 3 | 33792 | 4224 |
|  | 36 | 11 | 256QAM | 20 | 25104 | 24 | 1 | 3 | 38016 | 4752 |
|  | 45 | 11 | 256QAM | 20 | 31752 | 24 | 1 | 4 | 47520 | 5940 |
|  | 50 | 11 | 256QAM | 20 | 34816 | 24 | 1 | 5 | 52800 | 6600 |
|  | 60 | 11 | 256QAM | 20 | 42016 | 24 | 1 | 5 | 63360 | 7920 |
|  | 64 | 11 | 256QAM | 20 | 45096 | 24 | 1 | 6 | 67584 | 8448 |
|  | 75 | 11 | 256QAM | 20 | 53288 | 24 | 1 | 7 | 79200 | 9900 |
|  | 80 | 11 | 256QAM | 20 | 56368 | 24 | 1 | 7 | 84480 | 10560 |
|  | 81 | 11 | 256QAM | 20 | 57376 | 24 | 1 | 7 | 85536 | 10692 |
|  | 90 | 11 | 256QAM | 20 | 63528 | 24 | 1 | 8 | 95040 | 11880 |
|  | 100 | 11 | 256QAM | 20 | 69672 | 24 | 1 | 9 | 105600 | 13200 |
|  | 108 | 11 | 256QAM | 20 | 75792 | 24 | 1 | 9 | 114048 | 14256 |
|  | 120 | 11 | 256QAM | 20 | 83976 | 24 | 1 | 10 | 126720 | 15840 |
|  | 128 | 11 | 256QAM | 20 | 90176 | 24 | 1 | 11 | 135168 | 16896 |
|  | 135 | 11 | 256QAM | 20 | 94248 | 24 | 1 | 12 | 142560 | 17820 |
|  | 160 | 11 | 256QAM | 20 | 112648 | 24 | 1 | 14 | 168960 | 21120 |
|  | 162 | 11 | 256QAM | 20 | 114776 | 24 | 1 | 14 | 171072 | 21384 |
|  | 180 | 11 | 256QAM | 20 | 127080 | 24 | 1 | 16 | 190080 | 23760 |
|  | 216 | 11 | 256QAM | 20 | 151608 | 24 | 1 | 18 | 228096 | 28512 |
|  | 243 | 11 | 256QAM | 20 | 172176 | 24 | 1 | 21 | 256608 | 32076 |
|  | 270 | 11 | 256QAM | 20 | 188576 | 24 | 1 | 23 | 285120 | 35640 |
| NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.NOTE 2: MCS Index is based on MCS Table 5.1.3.1-2 defined in TS 38.214 [10].NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 4: The RMCs apply to all channel bandwidth where LCRB ≤ NRB. |  |  |  |  |  |  |  |  |  |  |

Table A.2.2.5-2: Void

Table A.2.2.5-3: Void

### A.2.2.6 CP-OFDM QPSK

Table A.2.2.6-1: Reference Channels for CP-OFDM QPSK

| Parameter | Allocated resource blocks (LCRB) | CP-OFDM Symbols per slot (Note 1) | Modulation | MCS Index (Note 2) | Payload size | Transport block CRC | LDPC Base Graph | Number of code blocks per slot (Note 3) | Total number of bits per slot | Total modulated symbols per slot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unit |  |  |  |  | Bits | Bits |  |  | Bits |  |
|  | 1 | 11 | QPSK | 2 | 48 | 16 | 2 | 1 | 264 | 132 |
|  | 5 | 11 | QPSK | 2 | 256 | 16 | 2 | 1 | 1320 | 660 |
|  | 6 | 11 | QPSK | 2 | 304 | 16 | 2 | 1 | 1584 | 792 |
|  | 9 | 11 | QPSK | 2 | 456 | 16 | 2 | 1 | 2376 | 1188 |
|  | 10 | 11 | QPSK | 2 | 504 | 16 | 2 | 1 | 2640 | 1320 |
|  | 11 | 11 | QPSK | 2 | 552 | 16 | 2 | 1 | 2904 | 1452 |
|  | 12 | 11 | QPSK | 2 | 608 | 16 | 2 | 1 | 3168 | 1584 |
|  | 13 | 11 | QPSK | 2 | 672 | 16 | 2 | 1 | 3432 | 1716 |
|  | 15 | 11 | QPSK | 2 | 768 | 16 | 2 | 1 | 3960 | 1980 |
|  | 16 | 11 | QPSK | 2 | 808 | 16 | 2 | 1 | 4224 | 2112 |
|  | 18 | 11 | QPSK | 2 | 928 | 16 | 2 | 1 | 4752 | 2376 |
|  | 19 | 11 | QPSK | 2 | 984 | 16 | 2 | 1 | 5016 | 2508 |
|  | 24 | 11 | QPSK | 2 | 1192 | 16 | 2 | 1 | 6336 | 3168 |
|  | 25 | 11 | QPSK | 2 | 1256 | 16 | 2 | 1 | 6600 | 3300 |
|  | 26 | 11 | QPSK | 2 | 1288 | 16 | 2 | 1 | 6864 | 3432 |
|  | 31 | 11 | QPSK | 2 | 1544 | 16 | 2 | 1 | 8184 | 4092 |
|  | 33 | 11 | QPSK | 2 | 1672 | 16 | 2 | 1 | 8712 | 4356 |
|  | 35 | 11 | QPSK | 2 | 1736 | 16 | 2 | 1 | 9240 | 4620 |
|  | 38 | 11 | QPSK | 2 | 1928 | 16 | 2 | 1 | 10032 | 5016 |
|  | 39 | 11 | QPSK | 2 | 2024 | 16 | 2 | 1 | 10296 | 5148 |
|  | 40 | 11 | QPSK | 2 | 2024 | 16 | 2 | 1 | 10560 | 5280 |
|  | 47 | 11 | QPSK | 2 | 2408 | 16 | 2 | 1 | 12408 | 6204 |
|  | 51 | 11 | QPSK | 2 | 2536 | 16 | 2 | 1 | 13464 | 6732 |
|  | 52 | 11 | QPSK | 2 | 2600 | 16 | 2 | 1 | 13728 | 6864 |
|  | 53 | 11 | QPSK | 2 | 2664 | 16 | 2 | 1 | 13992 | 6996 |
|  | 54 | 11 | QPSK | 2 | 2664 | 16 | 2 | 1 | 14256 | 7128 |
|  | 61 | 11 | QPSK | 2 | 3104 | 16 | 2 | 1 | 16104 | 8052 |
|  | 65 | 11 | QPSK | 2 | 3240 | 16 | 2 | 1 | 17160 | 8580 |
|  | 67 | 11 | QPSK | 2 | 3368 | 16 | 2 | 1 | 17688 | 8844 |
|  | 68 | 11 | QPSK | 2 | 3368 | 16 | 2 | 1 | 17952 | 8976 |
|  | 78 | 11 | QPSK | 2 | 3848 | 24 | 2 | 2 | 20592 | 10296 |
|  | 79 | 11 | QPSK | 2 | 3912 | 24 | 2 | 2 | 20856 | 10428 |
|  | 80 | 11 | QPSK | 2 | 3976 | 24 | 2 | 2 | 21120 | 10560 |
|  | 81 | 11 | QPSK | 2 | 4040 | 24 | 2 | 2 | 21384 | 10692 |
|  | 93 | 11 | QPSK | 2 | 4616 | 24 | 2 | 2 | 24552 | 12276 |
|  | 95 | 11 | QPSK | 2 | 4744 | 24 | 2 | 2 | 25080 | 12540 |
|  | 106 | 11 | QPSK | 2 | 5256 | 24 | 2 | 2 | 27984 | 13992 |
|  | 107 | 11 | QPSK | 2 | 5256 | 24 | 2 | 2 | 28248 | 14124 |
|  | 108 | 11 | QPSK | 2 | 5384 | 24 | 2 | 2 | 28512 | 14256 |
|  | 109 | 11 | QPSK | 2 | 5384 | 24 | 2 | 2 | 28776 | 14388 |
|  | 121 | 11 | QPSK | 2 | 6024 | 24 | 2 | 2 | 31944 | 15972 |
|  | 123 | 11 | QPSK | 2 | 6152 | 24 | 2 | 2 | 32472 | 16236 |
|  | 133 | 11 | QPSK | 2 | 6664 | 24 | 2 | 2 | 35112 | 17556 |
|  | 135 | 11 | QPSK | 2 | 6664 | 24 | 2 | 2 | 35640 | 17820 |
|  | 137 | 11 | QPSK | 2 | 6792 | 24 | 2 | 2 | 36168 | 18084 |
|  | 160 | 11 | QPSK | 2 | 7944 | 24 | 2 | 3 | 42240 | 21120 |
|  | 162 | 11 | QPSK | 2 | 8064 | 24 | 2 | 3 | 42768 | 21384 |
|  | 189 | 11 | QPSK | 2 | 9480 | 24 | 2 | 3 | 49896 | 24948 |
|  | 216 | 11 | QPSK | 2 | 10752 | 24 | 2 | 3 | 57024 | 28512 |
|  | 217 | 11 | QPSK | 2 | 10752 | 24 | 2 | 3 | 57288 | 28644 |
|  | 245 | 11 | QPSK | 2 | 12296 | 24 | 2 | 4 | 64680 | 32340 |
|  | 270 | 11 | QPSK | 2 | 13320 | 24 | 2 | 4 | 71280 | 35640 |
|  | 273 | 11 | QPSK | 2 | 13576 | 24 | 2 | 4 | 72072 | 36036 |
| NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.NOTE 2: MCS Index is based on MCS Table 5.1.3.1-1 defined in TS 38.214 [10].NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 4: The RMCs apply to all channel bandwidth where LCRB ≤ NRB. |  |  |  |  |  |  |  |  |  |  |

Table A.2.2.6-2: Void

Table A.2.2.6-3: Void

### A.2.2.7 CP-OFDM 16QAM

Table A.2.2.7-1: Reference Channels for CP-OFDM 16QAM

| Parameter | Allocated resource blocks (LCRB) | CP-OFDM Symbols per slot (Note 1) | Modulation | MCS Index (Note 2) | Payload size | Transport block CRC | LDPC Base Graph | Number of code blocks per slot (Note 3) | Total number of bits per slot | Total modulated symbols per slot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unit |  |  |  |  | Bits | Bits |  |  | Bits |  |
|  | 1 | 11 | 16QAM | 10 | 176 | 16 | 2 | 1 | 528 | 132 |
|  | 5 | 11 | 16QAM | 10 | 888 | 16 | 2 | 1 | 2640 | 660 |
|  | 6 | 11 | 16QAM | 10 | 1064 | 16 | 2 | 1 | 3168 | 792 |
|  | 9 | 11 | 16QAM | 10 | 1608 | 16 | 2 | 1 | 4752 | 1188 |
|  | 10 | 11 | 16QAM | 10 | 1800 | 16 | 2 | 1 | 5280 | 1320 |
|  | 11 | 11 | 16QAM | 10 | 1928 | 16 | 2 | 1 | 5808 | 1452 |
|  | 12 | 11 | 16QAM | 10 | 2088 | 16 | 2 | 1 | 6336 | 1584 |
|  | 13 | 11 | 16QAM | 10 | 2280 | 16 | 2 | 1 | 6864 | 1716 |
|  | 15 | 11 | 16QAM | 10 | 2664 | 16 | 2 | 1 | 7920 | 1980 |
|  | 16 | 11 | 16QAM | 10 | 2792 | 16 | 2 | 1 | 8448 | 2112 |
|  | 18 | 11 | 16QAM | 10 | 3240 | 16 | 2 | 1 | 9504 | 2376 |
|  | 19 | 11 | 16QAM | 10 | 3368 | 16 | 2 | 1 | 10032 | 2508 |
|  | 24 | 11 | 16QAM | 10 | 4224 | 24 | 1 | 1 | 12672 | 3168 |
|  | 25 | 11 | 16QAM | 10 | 4352 | 24 | 1 | 1 | 13200 | 3300 |
|  | 26 | 11 | 16QAM | 10 | 4480 | 24 | 1 | 1 | 13728 | 3432 |
|  | 31 | 11 | 16QAM | 10 | 5376 | 24 | 1 | 1 | 16368 | 4092 |
|  | 33 | 11 | 16QAM | 10 | 5760 | 24 | 1 | 1 | 17424 | 4356 |
|  | 35 | 11 | 16QAM | 10 | 6144 | 24 | 1 | 1 | 18480 | 4620 |
|  | 38 | 11 | 16QAM | 10 | 6656 | 24 | 1 | 1 | 20064 | 5016 |
|  | 39 | 11 | 16QAM | 10 | 6784 | 24 | 1 | 1 | 20592 | 5148 |
|  | 40 | 11 | 16QAM | 10 | 7040 | 24 | 1 | 1 | 21120 | 5280 |
|  | 47 | 11 | 16QAM | 10 | 8192 | 24 | 1 | 1 | 24816 | 6204 |
|  | 51 | 11 | 16QAM | 10 | 8968 | 24 | 1 | 2 | 26928 | 6732 |
|  | 52 | 11 | 16QAM | 10 | 9224 | 24 | 1 | 2 | 27456 | 6864 |
|  | 53 | 11 | 16QAM | 10 | 9224 | 24 | 1 | 2 | 27984 | 6996 |
|  | 54 | 11 | 16QAM | 10 | 9480 | 24 | 1 | 2 | 28512 | 7128 |
|  | 61 | 11 | 16QAM | 10 | 10760 | 24 | 1 | 2 | 32208 | 8052 |
|  | 65 | 11 | 16QAM | 10 | 11272 | 24 | 1 | 2 | 34320 | 8580 |
|  | 67 | 11 | 16QAM | 10 | 11784 | 24 | 1 | 2 | 35376 | 8844 |
|  | 68 | 11 | 16QAM | 10 | 11784 | 24 | 1 | 2 | 35904 | 8976 |
|  | 78 | 11 | 16QAM | 10 | 13576 | 24 | 1 | 2 | 41184 | 10296 |
|  | 79 | 11 | 16QAM | 10 | 13832 | 24 | 1 | 2 | 41712 | 10428 |
|  | 80 | 11 | 16QAM | 10 | 14088 | 24 | 1 | 2 | 42240 | 10560 |
|  | 81 | 11 | 16QAM | 10 | 14088 | 24 | 1 | 2 | 42768 | 10692 |
|  | 93 | 11 | 16QAM | 10 | 16392 | 24 | 1 | 2 | 49404 | 12276 |
|  | 95 | 11 | 16QMA | 10 | 16392 | 24 | 1 | 2 | 50160 | 12540 |
|  | 106 | 11 | 16QAM | 10 | 18432 | 24 | 1 | 3 | 55968 | 13992 |
|  | 107 | 11 | 16QAM | 10 | 18960 | 24 | 1 | 3 | 56496 | 14124 |
|  | 108 | 11 | 16QAM | 10 | 18960 | 24 | 1 | 3 | 57024 | 14256 |
|  | 109 | 11 | 16QAM | 10 | 18960 | 24 | 1 | 3 | 57552 | 14388 |
|  | 121 | 11 | 16QAM | 10 | 21000 | 24 | 1 | 3 | 63888 | 15972 |
|  | 123 | 11 | 16QAM | 10 | 21504 | 24 | 1 | 3 | 64944 | 16236 |
|  | 133 | 11 | 16QAM | 10 | 23040 | 24 | 1 | 3 | 70224 | 17556 |
|  | 135 | 11 | 16QAM | 10 | 23568 | 24 | 1 | 3 | 71280 | 17820 |
|  | 137 | 11 | 16QAM | 10 | 24072 | 24 | 1 | 3 | 72336 | 18084 |
|  | 160 | 11 | 16QAM | 10 | 28168 | 24 | 1 | 4 | 84480 | 21120 |
|  | 162 | 11 | 16QAM | 10 | 28168 | 24 | 1 | 4 | 85536 | 21384 |
|  | 189 | 11 | 16QAM | 10 | 32776 | 24 | 1 | 4 | 99792 | 24948 |
|  | 216 | 11 | 16QAM | 10 | 37896 | 24 | 1 | 5 | 114048 | 28512 |
|  | 217 | 11 | 16QAM | 10 | 37896 | 24 | 1 | 5 | 114576 | 28644 |
|  | 245 | 11 | 16QAM | 10 | 43032 | 24 | 1 | 6 | 129360 | 32340 |
|  | 270 | 11 | 16QAM | 10 | 47112 | 24 | 1 | 6 | 142560 | 35640 |
|  | 273 | 11 | 16QAM | 10 | 48168 | 24 | 1 | 6 | 144144 | 36036 |
| NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.NOTE 2: MCS Index is based on MCS Table 5.1.3.1-1 defined in TS 38.214 [10].NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 4: The RMCs apply to all channel bandwidth where LCRB ≤ NRB. |  |  |  |  |  |  |  |  |  |  |

Table A.2.2.7-2: Void

Table A.2.2.7-3: Void

### A.2.2.8 CP-OFDM 64QAM

Table A.2.2.8-1: Reference Channels for CP-OFDM 64QAM

| Parameter | Allocated resource blocks (LCRB) | CP-OFDM Symbols per slot (Note 1) | Modulation | MCS Index (Note 2) | Payload size | Transport block CRC | LDPC Base Graph | Number of code blocks per slot (Note 3) | Total number of bits per slot | Total modulated symbols per slot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unit |  |  |  |  | Bits | Bits |  |  | Bits |  |
|  | 1 | 11 | 64QAM | 19 | 408 | 16 | 2 | 1 | 792 | 132 |
|  | 5 | 11 | 64QAM | 19 | 2024 | 16 | 2 | 1 | 3960 | 660 |
|  | 9 | 11 | 64QAM | 19 | 3624 | 16 | 2 | 1 | 7128 | 1188 |
|  | 10 | 11 | 64QAM | 19 | 3968 | 24 | 1 | 1 | 7920 | 1320 |
|  | 11 | 11 | 64QAM | 19 | 4352 | 24 | 1 | 1 | 8712 | 1452 |
|  | 12 | 11 | 64QAM | 19 | 4736 | 24 | 1 | 1 | 9504 | 1584 |
|  | 13 | 11 | 64QAM | 19 | 5120 | 24 | 1 | 1 | 10296 | 1716 |
|  | 15 | 11 | 64QAM | 19 | 6016 | 24 | 1 | 1 | 11880 | 1980 |
|  | 18 | 11 | 64QAM | 19 | 7168 | 24 | 1 | 1 | 14256 | 2376 |
|  | 19 | 11 | 64QAM | 19 | 7552 | 24 | 1 |  | 15048 | 2508 |
|  | 24 | 11 | 64QAM | 19 | 9480 | 24 | 1 | 2 | 19008 | 3168 |
|  | 25 | 11 | 64QAM | 19 | 9992 | 24 | 1 | 2 | 19800 | 3300 |
|  | 26 | 11 | 64QAM | 19 | 10504 | 24 | 1 | 2 | 20592 | 3432 |
|  | 31 | 11 | 64QAM | 19 | 12296 | 24 | 1 | 2 | 24552 | 4092 |
|  | 33 | 11 | 64QAM | 19 | 13064 | 24 | 1 | 2 | 26136 | 4356 |
|  | 35 | 11 | 64QAM | 19 | 14088 | 24 | 1 | 2 | 27720 | 4620 |
|  | 38 | 11 | 64QAM | 19 | 15112 | 24 | 1 | 2 | 30096 | 5016 |
|  | 39 | 11 | 64QAM | 19 | 15624 | 24 | 1 | 2 | 30888 | 5148 |
|  | 47 | 11 | 64QAM | 19 | 18960 | 24 | 1 | 3 | 37224 | 6204 |
|  | 51 | 11 | 64QAM | 19 | 20496 | 24 | 1 | 3 | 40392 | 6732 |
|  | 52 | 11 | 64QAM | 19 | 21000 | 24 | 1 | 3 | 41184 | 6864 |
|  | 53 | 11 | 64QAM | 19 | 21000 | 24 | 1 | 3 | 41976 | 6996 |
|  | 61 | 11 | 64QAM | 19 | 24567 | 24 | 1 | 3 | 48312 | 8052 |
|  | 65 | 11 | 64QAM | 19 | 26120 | 24 | 1 | 4 | 51480 | 8580 |
|  | 67 | 11 | 64QAM | 19 | 26632 | 24 | 1 | 4 | 53064 | 8844 |
|  | 78 | 11 | 64QAM | 19 | 31240 | 24 | 1 | 4 | 61776 | 10296 |
|  | 79 | 11 | 64QAM | 19 | 31752 | 24 | 1 | 4 | 62568 | 10428 |
|  | 80 | 11 | 64QAM | 19 | 31752 | 24 | 1 | 4 | 63360 | 10560 |
|  | 81 | 11 | 64QAM | 19 | 32264 | 24 | 1 | 4 | 64152 | 10692 |
|  | 93 | 11 | 64QAM | 19 | 36896 | 24 | 1 | 5 | 73656 | 12276 |
|  | 95 | 11 | 64QAM | 19 | 37896 | 24 | 1 | 5 | 75240 | 12540 |
|  | 93 | 11 | 64QAM | 19 | 36896 | 24 | 1 | 5 | 73656 | 12276 |
|  | 106 | 11 | 64QAM | 19 | 42016 | 24 | 1 | 5 | 83952 | 13992 |
|  | 107 | 11 | 64QAM | 19 | 43032 | 24 | 1 | 6 | 84744 | 14124 |
|  | 108 | 11 | 64QAM | 19 | 43032 | 24 | 1 | 6 | 85536 | 14256 |
|  | 109 | 11 | 64QAM | 19 | 44040 | 24 | 1 | 6 | 86328 | 14388 |
|  | 121 | 11 | 64QAM | 19 | 48168 | 24 | 1 | 6 | 95832 | 15972 |
|  | 123 | 11 | 64QAM | 19 | 49176 | 24 | 1 | 6 | 97416 | 16236 |
|  | 133 | 11 | 64QAM | 19 | 53288 | 24 | 1 | 7 | 105336 | 17556 |
|  | 135 | 11 | 64QAM | 19 | 54296 | 24 | 1 | 7 | 106920 | 17820 |
|  | 137 | 11 | 64QAM | 19 | 54296 | 24 | 1 | 7 | 108504 | 18084 |
|  | 160 | 11 | 64QAM | 19 | 63528 | 24 | 1 | 8 | 126720 | 21120 |
|  | 162 | 11 | 64QAM | 19 | 64552 | 24 | 1 | 8 | 128304 | 21384 |
|  | 189 | 11 | 64QAM | 19 | 75792 | 24 | 1 | 9 | 149688 | 24948 |
|  | 216 | 11 | 64QAM | 19 | 86040 | 24 | 1 | 11 | 171072 | 28512 |
|  | 217 | 11 | 64QAM | 19 | 86040 | 24 | 1 | 11 | 171864 | 28644 |
|  | 245 | 11 | 64QAM | 19 | 98376 | 24 | 1 | 12 | 194040 | 32340 |
|  | 270 | 11 | 64QAM | 19 | 108552 | 24 | 1 | 13 | 213840 | 35640 |
|  | 273 | 11 | 64QAM | 19 | 108552 | 24 | 1 | 13 | 216216 | 36036 |
| NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.NOTE 2: MCS Index is based on MCS Table 5.1.3.1-1 defined in TS 38.214 [10].NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 4: The RMCs apply to all channel bandwidth where LCRB ≤ NRB. |  |  |  |  |  |  |  |  |  |  |

Table A.2.2.8-2: Void

Table A.2.2.8-3: Void

### A.2.2.9 CP-OFDM 256QAM

Table A.2.2.9-1: Reference Channels for CP-OFDM 256QAM

| Parameter | Allocated resource blocks (LCRB) | CP-OFDM Symbols per slot (Note 1) | Modulation | MCS Index (Note 2) | Payload size | Transport block CRC | LDPC Base Graph | Number of code blocks per slot (Note 3) | Total number of bits per slot | Total modulated symbols per slot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unit |  |  |  |  | Bits | Bits |  |  | Bits |  |
|  | 1 | 11 | 256QAM | 20 | 704 | 16 | 2 | 1 | 1056 | 132 |
|  | 5 | 11 | 256QAM | 20 | 3496 | 16 | 2 | 1 | 5280 | 660 |
|  | 9 | 11 | 256QAM | 20 | 6272 | 24 | 1 | 1 | 9504 | 1188 |
|  | 10 | 11 | 256QAM | 20 | 7040 | 24 | 1 | 1 | 10560 | 1320 |
|  | 11 | 11 | 256QAM | 20 | 7680 | 24 | 1 | 1 | 11616 | 1452 |
|  | 12 | 11 | 256QAM | 20 | 8456 | 24 | 1 | 2 | 12672 | 1584 |
|  | 13 | 11 | 256QAM | 20 | 9224 | 24 | 1 | 2 | 13728 | 1716 |
|  | 15 | 11 | 256QAM | 20 | 10504 | 24 | 1 | 2 | 15840 | 1980 |
|  | 18 | 11 | 256QAM | 20 | 12552 | 24 | 1 | 2 | 19008 | 2376 |
|  | 19 | 11 | 256QAM | 20 | 13320 | 24 | 1 | 2 | 20064 | 2508 |
|  | 24 | 11 | 256QAM | 20 | 16896 | 24 | 1 | 3 | 25344 | 3168 |
|  | 25 | 11 | 256QAM | 20 | 17424 | 24 | 1 | 3 | 26400 | 3300 |
|  | 26 | 11 | 256QAM | 20 | 18432 | 24 | 1 | 3 | 27456 | 3432 |
|  | 31 | 11 | 256QAM | 20 | 22032 | 24 | 1 | 3 | 32736 | 4092 |
|  | 33 | 11 | 256QAM | 20 | 23040 | 24 | 1 | 3 | 34848 | 4356 |
|  | 35 | 11 | 256QAM | 20 | 24576 | 24 | 1 | 3 | 36960 | 4620 |
|  | 38 | 11 | 256QAM | 20 | 26632 | 24 | 1 | 4 | 40128 | 5016 |
|  | 39 | 11 | 256QAM | 20 | 27656 | 24 | 1 | 4 | 41184 | 5148 |
|  | 47 | 11 | 256QAM | 20 | 32776 | 24 | 1 | 4 | 49632 | 6204 |
|  | 51 | 11 | 256QAM | 20 | 35856 | 24 | 1 | 5 | 53856 | 6732 |
|  | 52 | 11 | 256QAM | 20 | 36896 | 24 | 1 | 5 | 54912 | 6864 |
|  | 53 | 11 | 256QAM | 20 | 36896 | 24 | 1 | 5 | 55968 | 6996 |
|  | 61 | 11 | 256QAM | 20 | 43032 | 24 | 1 | 6 | 64416 | 8052 |
|  | 65 | 11 | 256QAM | 20 | 46104 | 24 | 1 | 6 | 68640 | 8580 |
|  | 67 | 11 | 256QAM | 20 | 47112 | 24 | 1 | 6 | 70752 | 8844 |
|  | 78 | 11 | 256QAM | 20 | 55304 | 24 | 1 | 7 | 82368 | 10296 |
|  | 79 | 11 | 256QAM | 20 | 55304 | 24 | 1 | 7 | 83424 | 10428 |
|  | 80 | 11 | 256QAM | 20 | 56368 | 24 | 1 | 7 | 84480 | 10560 |
|  | 81 | 11 | 256QAM | 20 | 57376 | 24 | 1 | 7 | 85536 | 10692 |
|  | 93 | 11 | 256QAM | 20 | 65576 | 24 | 1 | 8 | 98208 | 12276 |
|  | 95 | 11 | 256QAM | 20 | 67584 | 24 | 1 | 8 | 100320 | 12540 |
|  | 106 | 11 | 256QAM | 20 | 73776 | 24 | 1 | 9 | 111936 | 13992 |
|  | 107 | 11 | 256QAM | 20 | 75792 | 24 | 1 | 9 | 112992 | 14124 |
|  | 108 | 11 | 256QAM | 20 | 75792 | 24 | 1 | 9 | 114048 | 14256 |
|  | 109 | 11 | 256QAM | 20 | 75792 | 24 | 1 | 9 | 115104 | 14388 |
|  | 121 | 11 | 256QAM | 20 | 86040 | 24 | 1 | 11 | 127776 | 15972 |
|  | 123 | 11 | 256QAM | 20 | 86040 | 24 | 1 | 11 | 129888 | 16236 |
|  | 133 | 11 | 256QAM | 20 | 94248 | 24 | 1 | 12 | 140448 | 17556 |
|  | 135 | 11 | 256QAM | 20 | 94248 | 24 | 1 | 12 | 142560 | 17820 |
|  | 137 | 11 | 256QAM | 20 | 96264 | 24 | 1 | 12 | 144672 | 18084 |
|  | 160 | 11 | 256QAM | 20 | 112648 | 24 | 1 | 14 | 168960 | 21120 |
|  | 162 | 11 | 256QAM | 20 | 114776 | 24 | 1 | 14 | 171072 | 21384 |
|  | 189 | 11 | 256QAM | 20 | 131176 | 24 | 1 | 16 | 199584 | 24948 |
|  | 216 | 11 | 256QAM | 20 | 151608 | 24 | 1 | 18 | 228096 | 28512 |
|  | 217 | 11 | 256QAM | 20 | 151608 | 24 | 1 | 18 | 229152 | 28644 |
|  | 245 | 11 | 256QAM | 20 | 172176 | 24 | 1 | 21 | 258720 | 32340 |
|  | 270 | 11 | 256QAM | 20 | 188576 | 24 | 1 | 23 | 285120 | 35640 |
|  | 273 | 11 | 256QAM | 20 | 192624 | 24 | 1 | 23 | 288288 | 36036 |
| NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.NOTE 2: MCS Index is based on MCS Table 5.1.3.1-2 defined in TS 38.214 [10].NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 4: The RMCs apply to all channel bandwidth where LCRB ≤ NRB. |  |  |  |  |  |  |  |  |  |  |

Table A.2.2.9-2: Void

Table A.2.2.9-3: Void

## A.2.3 Reference measurement channels for TDD

The TDD UL RMCs are defined in clause A.2.2 with the active UL slots specified in Table A.2.1-1 and TDD slot patterns as defined for reference sensitivity tests.

The TDD UL RMCs for the phase continuty tests for DMRS bundling are defined in clause A.2.2 with the active UL slots and TDD pattern specified in Tables A.2.1-2 and A.2.1-3.

### A.2.3.1 DFT-s-OFDM Pi/2-BPSK

Table A.2.3.1-1: Void

Table A.2.3.1-2: Void

Table A.2.3.1-3: Void

### A.2.3.2 DFT-s-OFDM QPSK

Table A.2.3.2-1: Void

Table A.2.3.2-2: Void

Table A.2.3.2-3: Void

### A.2.3.3 DFT-s-OFDM 16QAM

Table A.2.3.3-1: Void

Table A.2.3.3-2: Void

Table A.2.3.3-3: Void

### A.2.3.4 DFT-s-OFDM 64QAM

Table A.2.3.4-1: Void

Table A.2.3.4-2: Void

Table A.2.3.4-3: Void

### A.2.3.5 DFT-s-OFDM 256QAM

Table A.2.3.5-1: Void

Table A.2.3.5-2: Void

Table A.2.3.5-3: Void

### A.2.3.6 CP-OFDM QPSK

Table A.2.3.6-1: Void

Table A.2.3.6-2: Void

Table A.2.3.6-3: Void

### A.2.3.7 CP-OFDM 16QAM

Table A.2.3.7-1: Void

Table A.2.3.7-2: Void

Table A.2.3.7-3: Void

### A.2.3.8 CP-OFDM 64QAM

Table A.2.3.8-1: Void

Table A.2.3.8-2: Void

Table A.2.3.8-3: Void

### A.2.3.9 CP-OFDM 256QAM

Table A.2.3.9-1: Void

Table A.2.3.9-2: Void

Table A.2.3.9-3: Void

# A.3 DL reference measurement channels

## A.3.1 General

Unless otherwise stated, Tables A.3.2.2-1, A.3.2.2-2, A.3.2.2-3, A.3.3.2-1, A.3.3.2-2 and A.3.3.2-3 are applicable for measurements of the Receiver Characteristics (clause 7) with the exception of clauses 7.4 (Maximum input level).

Unless otherwise stated, Tables A.3.2.3-1, A.3.2.3-2, A.3.2.3-3, A.3.3.3-1, A.3.3.3-2 and A.3.3.3-3 are applicable for clauses 7.4 (Maximum input level) and for UE not supporting PDSCH 256QAM,

Unless otherwise stated, Tables A.3.2.4-1, A.3.2.4-2, A.3.2.4-3, A.3.3.4-1, A.3.3.4-2 and A.3.3.4-3 are applicable for clauses 7.4 (Maximum input level) and for UE supporting PDSCH 256QAM,

Unless otherwise stated, Tables A.3.2.2-1, A.3.2.2-2, A.3.2.2-3, A.3.3.2-1, A.3.3.2-2 and A.3.3.2-3 also apply for the modulated interferer used in Clauses 7.5, 7.6 and 7.8 with test specific bandwidths.

In case of carrier aggregation scenarios, the k1 values and number of HARQ processes of the Reference Measurement Channels specified in Annex A.3 shall be adapted as specified in Tables A.3.1-2 and A.3.1-3.

Table A.3.1-1. Common reference channel parameters

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
| CORESET frequency domain allocation |  |  | Full BW |
| CORESET time domain allocation |  |  | 2 OFDM symbols at the begin of each slot |
| PDSCH mapping type |  |  | Type A |
| PDSCH start symbol index (S) |  |  | 2 |
| Number of consecutive PDSCH symbols (L) |  |  | 12 |
| PDSCH PRB bundling |  | PRBs | 2 |
| Dynamic PRB bundling |  |  | false |
|  |  |  |  |
| Overhead value for TBS determination |  |  | 0 |
| First DMRS position for Type A PDSCH mapping |  |  | 2 |
| DMRS type |  |  | Type 1 |
| Number of additional DMRS |  |  | 2 |
| FDM between DMRS and PDSCH |  |  | Disable |
| CSIRS for tracking | First subcarrier index in the PRB used for CSI-RS (k0) |  | 0 for CSI-RS resource 1,2,3,4 |
|  | OFDM symbols in the PRB used for CSIRS |  | l0 = 6 for CSI-RS resource 1 and 3l0 = 10 for CSI-RS resource 2 and 4 |
|  | Number of CSI-RS ports |  | 1 for CSI-RS resource 1,2,3,4 |
|  | CDM Type |  | 'No CDM' for CSI-RS resource 1,2,3,4 |
|  | Density (ρ) |  | 3 for CSI-RS resource 1,2,3,4 |
|  | CSIRS periodicity | Slots | 15 kHz SCS: 20 for CSI-RS resource 1,2,3,430 kHz SCS: 40 for CSI-RS resource 1,2,3,460 kHz SCS: 80 for CSI-RS resource 1,2,3,4 |
|  | CSIRS offset | Slots | 15 kHz SCS:0 for CSI-RS resource 1 and 21 for CSI-RS resource 3 and 430 kHz SCS:1 for CSI-RS resource 1 and 22 for CSI-RS resource 3 and 460 kHz SCS:2 for CSI-RS resource 1 and 23 for CSI-RS resource 3 and 4 |
|  | Frequency Occupation |  | Start PRB 0Number of PRB = BWP size |
|  | QCL info |  | TCI state #0 |
| PTRS configuration |  |  | PTRS is not configured |

Table A.3.1-2: Carrier aggregation test parameters for K1 values

| The number of slots between PDSCH and corresponding HARQ-ACK information |  | CCs with the same duplex mode and SCS with PCell | CCs with different duplex mode and/or SCS with PCell |
| --- | --- | --- | --- |
| FDD 15 kHz + | FDD PCell | {2} | N/A |
| FDD 15 kHz CA |  |  |  |
| FDD 15 kHz + | 15kHz PCell | {2} | {3} |
| FDD 30 kHz CA | 30kHz PCell | {2} | {2} |
| FDD 15 kHz + | FDD PCell | {2} | {2} |
| TDD 15 kHz CA | TDD PCell | {4,3,2} | {4,3,2,6,5} |
| FDD 15 kHz + | FDD PCell | {2} | {3} |
| TDD 30 kHz CA | TDD PCell | {8,7,6,5,4,3,2} | {8,6,4,2,10} |
| TDD 15 kHz + | TDD PCell | {4,3,2} | N/A |
| TDD 15 kHz CA |  |  |  |
| TDD 15 kHz + | 15kHz PCell | {4,3,2} | {4,4,3,3,2,7,6} |
| TDD 30 kHz CA | 30kHz PCell | {8,7,6,5,4,3,2} | {7,5,4} |
| FDD 30 kHz + | FDD PCell | {2} | N/A |
| FDD 30 kHz CA |  |  |  |
| FDD 30 kHz + | FDD PCell | {2} | {2} |
| TDD 15 kHz CA | TDD PCell | {4,3,2} | {4,4,3,3,7,7,6,6,5,5} |
| FDD 30 kHz + | FDD PCell | {2} | {2} |
| TDD 30 kHz CA | TDD PCell | {8,7,6,5,4,3,2} | {8,7,6,5,4,3,2,2,10,-}(NOTE 1) |
| TDD 30 kHz + | TDD PCell | {8,7,6,5,4,3,2} | N/A |
| TDD 30 kHz CA |  |  |  |
| NOTE 1: No PDSCH shall be scheduled in slots 9 and 19 to avoid HARQ conflicts and maximize Throughput. Hence no K1 value is applicable for them. |  |  |  |

Table A.3.1-3: Carrier Aggregation test parameters for number of HARQ processes

| HARQ process number |  | CCs with the same duplex mode and SCS with PCell | CCs with different duplex mode and/or SCS with PCell |
| --- | --- | --- | --- |
| FDD 15 kHz + | FDD PCell | 4 | N/A |
| FDD 15 kHz CA |  |  |  |
| FDD 15 kHz + | 15kHz PCell | 8 | 8 |
| FDD 30 kHz CA | 30kHz PCell | 8 | 8 |
| FDD 15 kHz + | FDD PCell | 4 | 8 |
| TDD 15 kHz CA | TDD PCell | 8 | 8 |
| FDD 15 kHz + | FDD PCell | 4 | 8 |
| TDD 30 kHz CA | TDD PCell | 10 | 8 |
| TDD 15 kHz + | TDD PCell | 8 | N/A |
| TDD 15 kHz CA |  |  |  |
| TDD 15 kHz + | 15kHz PCell | 8 | 12 |
| TDD 30 kHz CA | 30kHz PCell | 8 | 8 |
| FDD 30 kHz + | FDD PCell | 8 | N/A |
| FDD 30 kHz CA |  |  |  |
| FDD 30 kHz + | FDD PCell | 8 | 8 |
| TDD 15 kHz CA | TDD PCell | 8 | 16 |
| FDD 30 kHz + | FDD PCell | 8 | 8 |
| TDD 30 kHz CA | TDD PCell | 8 | 16 |
| TDD 30 kHz + | TDD PCell | 8 | N/A |
| TDD 30 kHz CA |  |  |  |

## A.3.2 DL reference measurement channels for FDD

### A.3.2.1 General

Table A.3.2.1-1 Additional reference channels parameters for FDD

| Parameter | Unit | Value |
| --- | --- | --- |
| Number of HARQ Processes |  | 4 |
| K1 value |  | 2 for all slots |

### A.3.2.2 FRC for receiver requirements for QPSK

Table A.3.2.2-1 Fixed reference channel for receiver requirements (SCS 15 kHz, FDD, QPSK 1/3)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 3 | 5, 10, 15, 20 (Note 5) | 7 | 10 | 15 | 20 | 25 | 30 | 40 | 50 |
| Subcarrier spacing | kHz | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Allocated resource blocks |  | 15 | 25 | 35 | 52 | 79 | 106 | 133 | 160 | 216 | 270 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| MCS Index |  | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| MCS Table for TBS determination | 64QAM |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK |
| Target Coding Rate |  | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,3,4,5,6,7,8,9 | Bits | 984 | 1672 | 2280 | 3368 | 5120 | 6912 | 8712 | 10504 | 14088 | 17424 |
| Transport block CRC | Bits | 16 | 16 | 16 | 16 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,3,4,5,6,7,8,9 | CBs | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 3 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,3,4,5,6,7,8,9 | Bits | 3240 | 5400 | 7560 | 11232 | 17064 | 22896 | 28728 | 34560 | 46656 | 58320 |
| Max. Throughput averaged over 1 frame | Mbps | 0.787 | 1.338 | 1.824 | 2.694 | 4.096 | 5.530 | 6.970 | 8.403 | 11.270 | 13.9392 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frameNOTE 5: Channel bandwidths 10, 15, and 20 MHz in this column only apply to UEs supporting IE supportOfERedCap-r18 but not eRedCapNotReducedBB-BW-r18. |  |  |  |  |  |  |  |  |  |  |  |

Table A.3.2.2-2 Fixed reference channel for receiver requirements (SCS 30 kHz, FDD, QPSK 1/3)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 10, 15, 20 (Note 5) | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 80 | 90 | 100 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Allocated resource blocks |  | 24 | 12 | 38 | 51 | 65 | 78 | 106 | 133 | 162 | 217 | 245 | 273 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 |
| MCS Index |  | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| MCS Table for TBS determination |  | 64QAM |  |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK |
| Target Coding Rate |  | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 3,…,19 | Bits | 1608 | 808 | 2472 | 3368 | 4224 | 4992 | 6912 | 8712 | 10504 | 14088 | 15880 | 17928 |
| Transport block CRC | Bits | 16 | 16 | 16 | 16 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 3,…,19 | CBs | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 3 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 3,…,19 | Bits | 5184 | 2592 | 8208 | 11016 | 14040 | 16848 | 22896 | 28728 | 34992 | 46872 | 52920 | 58968 |
| Max. Throughput averaged over 1 frame | Mbps | 2.734 | 1.374 | 4.202 | 5.726 | 7.181 | 8.486 | 11.750 | 14.810 | 17.857 | 23.950 | 26.996 | 30.478 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frameNOTE 5: Channel bandwidths 10, 15, and 20 MHz in this column only apply to UEs supporting IE supportOfERedCap-r18 but not eRedCapNotReducedBB-BW-r18. |  |  |  |  |  |  |  |  |  |  |  |  |  |

Table A.3.2.2-3 Fixed reference channel for receiver requirements (SCS 60 kHz, FDD, QPSK 1/3)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 80 | 90 | 100 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Allocated resource blocks |  | 11 | 18 | 24 | 31 | 38 | 51 | 65 | 79 | 107 | 121 | 135 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 36 | 36 | 36 | 36 | 36 | 36 | 36 | 36 | 36 | 36 | 36 |
| MCS Index |  | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| MCS Table for TBS Determination |  | 64QAM |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK |
| Target Coding Rate |  | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 4,…,39 | Bits | 736 | 1192 | 1608 | 2024 | 2472 | 3368 | 4224 | 5120 | 6912 | 7808 | 8712 |
| Transport block CRC | Bits | 16 | 16 | 16 | 16 | 16 | 16 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slot 0,1,2,3 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 4,…,39 | CBs | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slot 0,1,2,3 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 4,…,39 | Bits | 2376 | 3888 | 5184 | 6696 | 8208 | 11016 | 14040 | 17064 | 23112 | 26136 | 29160 |
| Max. Throughput averaged over 1 frame | Mbps | 2.650 | 4.291 | 5.789 | 7.286 | 8.899 | 12.125 | 15.206 | 18.432 | 24.883 | 28.109 | 31.363 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frame |  |  |  |  |  |  |  |  |  |  |  |  |

### A.3.2.3 FRC for maximum input level for 64QAM

Table A.3.2.3-1 Fixed reference channel for maximum input level receiver requirements (SCS 15 kHz, FDD, 64QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 3 | 5, 10,15, 20 (Note 5) | 5 | 7 | 10 | 15 | 20 | 25 | 30 | 40 | 50 |
| Subcarrier spacing | kHz | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Allocated resource blocks |  | 15 | 20 | 25 | 35 | 52 | 79 | 106 | 133 | 160 | 216 | 270 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| MCS Index |  | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| MCS Table for TBS determination | 64QAM |  |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | 64 QAM | 64 QAM | 64 QAM | 64QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM |
| Target Coding Rate |  | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,3,4,5,6,7,8,9 | Bits | 7296 | 9736 | 12296 | 16896 | 25608 | 38936 | 52224 | 64552 | 77896 | 106576 | 131176 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slot 0,1 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,3,4,5,6,7,8,9 | CBs | 1 | 2 | 2 | 3 | 4 | 5 | 7 | 8 | 10 | 13 | 16 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slot 0,1 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,3,4,5,6,7,8,9 | Bits | 9720 | 12960 | 16200 | 22680 | 33696 | 51192 | 68688 | 86184 | 103680 | 139968 | 174960 |
| Max. Throughput averaged over 1 frame | Mbps | 5.837 | 7.789 | 9.837 | 13.517 | 20.486 | 31.149 | 41.779 | 51.642 | 62.317 | 85.261 | 104.941 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot 0 of each frameNOTE 4: Slot i is slot index per frameNOTE 5: Channel bandwidths in this column only apply to UEs supporting IE supportOfERedCap-r18. |  |  |  |  |  |  |  |  |  |  |  |  |

Table A.3.2.3-2 Fixed reference channel for maximum input level receiver requirements (SCS 30 kHz, FDD, 64QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10, 15, 20 (Note 5) | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 80 | 100 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Allocated resource blocks |  | 10 | 24 | 38 | 51 | 65 | 78 | 106 | 133 | 162 | 217 | 273 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 |
| MCS Index |  | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| MCS Table for TBS determination |  | 64QAM |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM |
| Target Coding Rate |  | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 3,…,19 | Bits | 4864 | 11784 | 18432 | 25104 | 31752 | 37896 | 52224 | 64552 | 79896 | 106576 | 135296 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slot2 0,1,2 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 3,…,19 | CBs | 1 | 2 | 3 | 3 | 4 | 5 | 7 | 8 | 10 | 13 | 17 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 3,…,19 | Bits | 6480 | 15552 | 24624 | 33048 | 42120 | 50544 | 68688 | 86184 | 104976 | 140616 | 176904 |
| Max. Throughput averaged over 1 frame | Mbps | 8.269 | 20.033 | 31.334 | 42.677 | 53.978 | 64.423 | 88.781 | 109.738 | 135.823 | 181.179 | 230.003 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot 0 of each frameNOTE 4: Slot i is slot index per frameNOTE 5:  Channel bandwidths in this column only apply to UEs supporting IE supportOfERedCap-r18. |  |  |  |  |  |  |  |  |  |  |  |  |

Table A.3.2.3-3 Fixed Reference Channel for Maximum input level receiver requirements (SCS 60 kHz, FDD, 64QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 80 | 100 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Allocated resource blocks |  | 11 | 18 | 24 | 31 | 38 | 51 | 65 | 79 | 107 | 135 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 36 | 36 | 36 | 36 | 36 | 36 | 36 | 36 | 36 | 36 |
| MCS Index |  | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| MCS Table for TBS determination |  | 64QAM |  |  |  |  |  |  |  |  |  |
| Modulation |  | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM |
| Target Coding Rate |  | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 4,…,39 | Bits | 5376 | 8712 | 11784 | 15112 | 18432 | 25104 | 31752 | 38936 | 52224 | 65576 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 4,…,39 | CBs | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 5 | 7 | 8 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 4,…,39 | Bits | 7128 | 11664 | 15552 | 20088 | 24624 | 33048 | 42120 | 51192 | 69336 | 87480 |
| Max. Throughput averaged over 1 frame | Mbps | 19.354 | 31.363 | 42.422 | 54.403 | 66.355 | 90.374 | 114.307 | 140.170 | 188.006 | 236.074 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frame |  |  |  |  |  |  |  |  |  |  |  |

### A.3.2.4 FRC for maximum input level for 256 QAM

Table A.3.2.4-1 Fixed reference channel for maximum input level receiver requirements (SCS 15 kHz, FDD, 256QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 3, 5, 10,15, 20 (NOTE 5) | 5 | 7 | 10 | 15 | 20 | 25 | 30 | 40 | 50 |
| Subcarrier spacing | kHz | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Allocated resource blocks |  | 15 | 25 | 35 | 52 | 79 | 106 | 133 | 160 | 216 | 270 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| MCS Index |  | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 |
| MCS Table for TBS determination | 256QAM |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM |
| Target Coding Rate |  | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,3,4,5,6,7,8,9 | Bits | 9992 | 16896 | 23568 | 34816 | 53288 | 71688 | 90176 | 108552 | 143400 | 180376 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slot 0,1 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,3,4,5,6,7,8,9 | CBs | 2 | 3 | 3 | 5 | 7 | 9 | 11 | 13 | 18 | 22 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,3,4,5,6,7,8,9 | Bits | 12960 | 21600 | 30240 | 44928 | 68256 | 91584 | 114912 | 138240 | 186624 | 233280 |
| Max. Throughput averaged over 1 frame | Mbps | 7.994 | 13.517 | 18.854 | 27.853 | 42.630 | 57.350 | 72.141 | 86.842 | 114.720 | 144.301 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot 0 of each frameNOTE 4: Slot i is slot index per frameNOTE 5: Channel bandwidths 5, 10, 15, and 20 MHz in this column only apply to UEs supporting IE supportOfERedCap-r18. |  |  |  |  |  |  |  |  |  |  |  |

Table A.3.2.4-2 Fixed reference channel for maximum input level receiver requirements (SCS 30 kHz, FDD, 256QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10,15, 20 (NOTE 5) | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 80 | 100 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Allocated resource blocks |  | 7 | 24 | 38 | 51 | 65 | 78 | 106 | 133 | 162 | 217 | 273 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 |
| MCS Index |  | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 |
| MCS Table for TBS determination |  | 256QAM |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM |
| Target Coding Rate |  | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 3,…,19 | Bits | 4736 | 16136 | 25608 | 33816 | 44040 | 52224 | 71688 | 90176 | 108552 | 147576 | 184424 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 3,…,19 | CBs | 1 | 2 | 4 | 5 | 6 | 7 | 9 | 11 | 13 | 18 | 22 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 3,…,19 | Bits | 6048 | 20736 | 32832 | 44064 | 56160 | 67392 | 91584 | 114912 | 139968 | 187488 | 235872 |
| Max. Throughput averaged over 1 frame | Mbps | 8.051 | 27.431 | 43.534 | 57.487 | 74.868 | 88.781 | 121.870 | 153.299 | 184.538 | 250.879 | 313.521 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot 0 of each frameNOTE 4: Slot i is slot index per frameNOTE 5: Channel bandwidths in this column only apply to UEs supporting IE supportOfERedCap-r18. |  |  |  |  |  |  |  |  |  |  |  |  |

Table A.3.2.4-3 Fixed reference channel for maximum input level receiver requirements (SCS 60 kHz, FDD, 256QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 80 | 100 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Allocated resource blocks |  | 11 | 18 | 24 | 31 | 38 | 51 | 65 | 79 | 107 | 135 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 36 | 36 | 36 | 36 | 36 | 36 | 36 | 36 | 36 | 36 |
| MCS Index |  | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 |
| MCS Table for TBS determination |  | 256QAM |  |  |  |  |  |  |  |  |  |
| Modulation |  | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM |
| Target Coding Rate |  | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 4,…,39 | Bits | 7424 | 12040 | 16136 | 21000 | 25608 | 33816 | 44040 | 53288 | 71688 | 90176 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 4,…,39 | CBs | 1 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 9 | 11 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slot 0,1,2,3 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 4,…,39 | Bits | 9504 | 15552 | 20736 | 26784 | 32832 | 44064 | 56160 | 68256 | 92448 | 116640 |
| Max. Throughput averaged over 1 frame | Mbps | 26.726 | 43.344 | 58.090 | 75.600 | 92.189 | 121.738 | 158.544 | 191.837 | 258.077 | 324.634 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frame |  |  |  |  |  |  |  |  |  |  |  |

### A.3.2.5 FRC for maximum input level for 1024 QAM

Table A.3.2.5-1 Fixed reference channel for maximum input level receiver requirements (SCS 15 kHz, FDD, 1024QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 3 | 5 | 7 | 10 | 15 | 20 | 25 | 30 | 40 | 50 |
| Subcarrier spacing | kHz | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| Subcarrier spacing configuration $\mu  $ |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Allocated resource blocks |  | 15 | 25 | 35 | 52 | 79 | 106 | 133 | 160 | 216 | 270 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| MCS Index |  | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 |
| MCS Table for TBS determination | 1024QAM |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM |
| Target Coding Rate |  | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,3,4,5,6,7,8,9 | Bits | 12808 | 21000 | 29704 | 44040 | 67584 | 90176 | 112648 | 135296 | 184424 | 229576 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slot 0,1 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,3,4,5,6,7,8,9 | CBs | 2 | 3 | 4 | 6 | 9 | 11 | 14 | 17 | 22 | 28 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,3,4,5,6,7,8,9 | Bits | 16200 | 27000 | 37800 | 56160 | 85320 | 114480 | 143640 | 172800 | 233280 | 291600 |
| Max. Throughput averaged over 1 frame | Mbps | 10.246 | 16.800 | 23.763 | 35.232 | 54.067 | 72.141 | 90.118 | 108.237 | 147.539 | 183.661 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot 0 of each frameNOTE 4: Slot i is slot index per frame |  |  |  |  |  |  |  |  |  |  |  |

Table A.3.2.5-2 Fixed reference channel for maximum input level receiver requirements (SCS 30 kHz, FDD, 1024QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 80 | 100 |
| Subcarrier spacing configuration $\mu  $ |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Allocated resource blocks |  | 24 | 38 | 51 | 65 | 78 | 106 | 133 | 162 | 217 | 273 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 |
| MCS Index |  | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 |
| MCS Table for TBS determination |  | 1024QAM |  |  |  |  |  |  |  |  |  |
| Modulation |  | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM |
| Target Coding Rate |  | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 3,…,19 | Bits | 20496 | 32264 | 43032 | 55304 | 65576 | 90176 | 112648 | 139376 | 184424 | 233608 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 3,…,19 | CBs | 3 | 4 | 6 | 7 | 8 | 11 | 14 | 17 | 22 | 28 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 3,…,19 | Bits | 25920 | 41040 | 55080 | 70200 | 84240 | 114480 | 143640 | 174960 | 234360 | 294840 |
| Max. Throughput averaged over 1 frame | Mbps | 34.843 | 54.849 | 73.154 | 94.017 | 111.479 | 153.299 | 191.502 | 236.939 | 313.521 | 397.134 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot 0 of each frameNOTE 4: Slot i is slot index per frame |  |  |  |  |  |  |  |  |  |  |  |

Table A.3.2.5-3 Fixed reference channel for maximum input level receiver requirements (SCS 60 kHz, FDD, 1024QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 80 | 100 |
| Subcarrier spacing configuration $\mu  $ |  | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Allocated resource blocks |  | 11 | 18 | 24 | 31 | 38 | 51 | 65 | 79 | 107 | 135 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 36 | 36 | 36 | 36 | 36 | 36 | 36 | 36 | 36 | 36 |
| MCS Index |  | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 |
| MCS Table for TBS determination |  | 1024QAM |  |  |  |  |  |  |  |  |  |
| Modulation |  | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM |
| Target Coding Rate |  | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 4,…,39 | Bits | 9224 | 15368 | 20496 | 26120 | 32264 | 43032 | 55304 | 67584 | 90176 | 114776 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 4,…,39 | CBs | 2 | 2 | 3 | 4 | 4 | 6 | 7 | 9 | 11 | 14 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |
| For Slot 0,1,2,3 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 4,…,39 | Bits | 11880 | 19440 | 25920 | 33480 | 41040 | 55080 | 70200 | 85320 | 115560 | 145800 |
| Max. Throughput averaged over 1 frame | Mbps | 33.206 | 55.325 | 73.786 | 94.032 | 116.150 | 154.915 | 199.094 | 243.302 | 324.634 | 413.194 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frame |  |  |  |  |  |  |  |  |  |  |  |

## A.3.3 DL reference measurement channels for TDD

### A.3.3.1 General

Table A.3.3.1-1 Additional reference channels parameters for TDD

| Parameter |  | Value |  |  |
| --- | --- | --- | --- | --- |
|  |  | SCS 15 kHz (µ=0) | SCS 30 kHz (µ=1) | SCS 60 kHz (µ=2) |
| TDD Slot Configuration pattern (Note 1) |  | DDDSU | 7DS2U | 14DS1S24U |
| Special Slot Configuration (Note 2) |  | 10D+2G+2U | 6D+4G+4U | S1=12D+2G, S2=6G+8U |
| referenceSubcarrierSpacing |  | 15 kHz | 30 kHz | 60 kHz |
| UL-DL configuration | dl-UL-TransmissionPeriodicity | 5 ms | 5 ms | 5 ms |
|  | nrofDownlinkSlots | 3 | 7 | 14 |
|  | nrofDownlinkSymbols | 10 | 6 | 12 |
|  | nrofUplinkSlot | 1 | 2 | 4 |
|  | nrofUplinkSymbols | 2 | 4 | 8 |
| Number of HARQ Processes |  | 8 | 8 | 16 |
| The number of slots between PDSCH and corresponding HARQ-ACK information (Note 3) |  | K1 = 4 if mod(i,5) = 0 K1 = 3 if mod(i,5) = 1 K1 = 2 if mod(i,5) = 2 where i is slot index per frame; i = {0,…,9} | K1 = 8 if mod(i,10) = 0 K1 = 7 if mod(i,10) = 1 K1 = 6 if mod(i,10) = 2 K1 = 5 if mod(i,10) = 3 K1 = 4 if mod(i,10) = 4 K1 = 3 if mod(i,10) = 5 K1 = 2 if mod(i,10) = 6 where i is slot index per frame; i = {0,…,19} | K1 = 13 if mod(i,20) = 2K1 = 12 if mod(i,20) = 3K1 = 11 if mod(i,20) = 4K1 = 10 if mod(i,20) = 5K1 = 9 if mod(i,20) = 6K1 = 8 if mod(i,20) = 7K1 = 7 if mod(i,20) = 8K1 = 6 if mod(i,20) = 9 K1 = 6 if mod(i,20) = 10K1 = 6 if mod(i,20) = 11K1 = 6 if mod(i,20) = 12 K1 = 6 if mod(i,20) = 13 where i is slot index per frame; i = {0,…,39} |
| NOTE 1: D denotes a slot with all DL symbols; S denotes a slot with a mix of DL, UL and guard symbols; U denotes a slot with all UL symbols. The field is for information.NOTE 2: D, G, U denote DL, guard and UL symbols, respectively. The field is for information.NOTE 3: i is the slot index per frame.NOTE 4: A -2ms or +3ms time offset to the NR configuration pattern relative to the E-UTRA UL-DL configuration must be apply in the TDD intra-band EN-DC. |  |  |  |  |

### A.3.3.2 FRC for receiver requirements for QPSK

Table A.3.3.2-1 Fixed reference channel for receiver requirements (SCS 15 kHz, TDD, QPSK 1/3)

| Parameter | Unit | Value |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 5, 10, 15, 20 (Note 5) | 10 | 15 | 20 | 25 | 30 | 40 | 50 |
| Subcarrier spacing | kHz | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| Subcarrier spacing configuration |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Allocated resource blocks |  | 25 | 52 | 79 | 106 | 133 | 160 | 216 | 270 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| MCS Index |  | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| MCS Table for TBS determination |  | 64QAM |  |  |  |  |  |  |  |
| Modulation |  | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK |
| Target Coding Rate |  | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,3,4,8,9 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,5,6,7 | Bits | 1672 | 3368 | 5120 | 6912 | 8712 | 10504 | 14088 | 17424 |
| Transport block CRC | Bits | 16 | 16 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,3,4,8,9 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,5,6,7 | CBs | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 3 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,3,4,8,9 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,5,6,7 | Bits | 5400 | 11232 | 17064 | 22896 | 28728 | 34560 | 46656 | 58320 |
| Max. Throughput averaged over 1 frame | Mbps | 0.669 | 1.347 | 2.048 | 2.765 | 3.485 | 4.202 | 5.635 | 6.970 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot 0 of each frameNOTE 4: Slot i is slot index per frameNOTE 5: Channel bandwidths 10, 15, and 20 MHz in this column only apply to UEs supporting IE supportOfERedCap-r18 but not eRedCapNotReducedBB-BW-r18. |  |  |  |  |  |  |  |  |  |

Table A.3.3.2-2 Fixed reference channel for receiver requirements (SCS 30 kHz, TDD, QPSK 1/3)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10, 15, 20 (Note 5) | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 70 | 80 | 100 |
| Subcarrier spacing configuration |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Allocated resource blocks |  | 12 | 24 | 38 | 51 | 65 | 78 | 106 | 133 | 162 | 162 | 217 | 273 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 13 | 11 | 11 |
| MCS Index |  | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| MCS Table for TBS determination |  | 64QAM |  |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK |
| Target Coding Rate |  | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19} | Bits | 808 | 1608 | 2472 | 3368 | 4224 | 4992 | 6912 | 8712 | 10504 | 12296 | 14088 | 17928 |
| Transport block CRC | Bits | 16 | 16 | 16 | 16 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19} | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19} | CBs | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 3 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19} | Bits | 2592 | 5184 | 8208 | 11016 | 14040 | 16848 | 22896 | 28728 | 34992 | 40824 | 46872 | 58968 |
| Max. Throughput averaged over 1 frame | Mbps | 0.889 | 1.7699 | 2.719 | 3.705 | 4.646 | 5.491 | 7.603 | 9.583 | 11.554 | 13.526 | 15.497 | 19.721 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frameNOTE 5: Channel bandwidths in this column only apply to UEs supporting IE supportOfERedCap-r18 but not eRedCapNotReducedBB-BW-r18. |  |  |  |  |  |  |  |  |  |  |  |  |  |

Table A.3.3.2-3 Fixed reference channel for receiver requirements (SCS 60 kHz, TDD, QPSK 1/3)

| Parameter | Unit |  | Value |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 70 | 80 | 100 |
| Subcarrier spacing configuration |  | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Allocated resource blocks |  | 11 | 18 | 24 | 31 | 38 | 51 | 65 | 79 | 93 | 107 | 135 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 26 | 24 | 24 |
| MCS Index |  | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| MCS Table for TBS determination |  | 64QAM |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK | QPSK |
| Target Coding Rate |  | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39} | Bits | 736 | 1192 | 1608 | 2024 | 2472 | 3368 | 4224 | 5120 | 6016 | 6912 | 8712 |
| Transport block CRC | Bits | 16 | 16 | 16 | 16 | 16 | 16 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39} | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39} | CBs | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 20) = {0,…,13} for i from {4,…,39} | Bits | 2376 | 3888 | 5184 | 6696 | 8208 | 11016 | 14040 | 17064 | 20088 | 23112 | 29160 |
| Max. Throughput averaged over 1 frame | Mbps | 1.766 | 2.861 | 3.859 | 4.858 | 5.933 | 8.083 | 10.138 | 12.288 | 14.438 | 16.589 | 20.909 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frame |  |  |  |  |  |  |  |  |  |  |  |  |

### A.3.3.3 FRC for maximum input level for 64QAM

Table A.3.3.3-1 Fixed reference channel for maximum input level receiver requirements (SCS 15 kHz, TDD, 64QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 5, 10, 15, 20 (Note 5) | 5 | 10 | 15 | 20 | 25 | 30 | 40 | 50 |
| Subcarrier spacing | kHz | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Allocated resource blocks |  | 20 | 25 | 52 | 79 | 106 | 133 | 160 | 216 | 270 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| MCS Index |  | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| MCS Table for TBS deermination |  | 64QAM |  |  |  |  |  |  |  |  |
| Modulation |  | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM |
| Target Coding Rate |  | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,3,4,8,9 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,5,6,7 | Bits | 9736 | 12296 | 25608 | 38936 | 52224 | 64552 | 77896 | 106576 | 131176 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,3,4,8,9 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,5,6,7 | CBs | 2 | 2 | 4 | 5 | 7 | 8 | 10 | 13 | 16 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,3,4,8,9 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,5,6,7 | Bits | 12960 | 16200 | 33696 | 51192 | 68688 | 86184 | 103680 | 139968 | 174960 |
| Max. Throughput averaged over 1 frame | Mbps | 3.894 | 4.918 | 10.243 | 15.574 | 20.890 | 20.890 | 31.158 | 42.630 | 52.470 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot 0 of each frameNOTE 4: Slot i is slot index per frameNOTE 5: Channel bandwidths in this column only apply to UEs supporting IE supportOfERedCap-r18. |  |  |  |  |  |  |  |  |  |  |

Table A.3.3.3-2 Fixed reference channel for maximum input level receiver requirements (SCS 30 kHz, TDD, 64QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10, 15, 20 (Note 5) | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 70 | 80 | 100 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Allocated resource blocks |  | 10 | 24 | 38 | 51 | 65 | 78 | 106 | 133 | 162 | 189 | 217 | 273 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 13 | 11 | 11 |
| MCS Index |  | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| MCS Table for TBS determination |  | 64QAM |  |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | 4864 | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM |
| Target Coding Rate |  | 24 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19} | Bits | 1 | 11784 | 18432 | 25104 | 31752 | 37896 | 52224 | 64552 | 79896 | 92200 | 106576 | 135296 |
| Transport block CRC | Bits |  | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | N/A | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  | 6480 |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19} | CBs | 5.350 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19} | CBs | 4864 | 2 | 3 | 3 | 4 | 5 | 7 | 8 | 10 | 11 | 13 | 17 |
| Binary Channel Bits per Slot |  | 24 |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19} | Bits | 1 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19} | Bits |  | 15552 | 24624 | 33048 | 42120 | 50544 | 68688 | 86184 | 104976 | 122472 | 140616 | 176904 |
| Max. Throughput averaged over 1 frame | Mbps | N/A | 12.962 | 20.275 | 27.614 | 34.927 | 41.686 | 57.446 | 71.007 | 87.886 | 101.42 | 117.234 | 148.826 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frameNOTE 5:  Channel bandwidths in this column only apply to UEs supporting IE supportOfERedCap-r18. |  |  |  |  |  |  |  |  |  |  |  |  |  |

Table A.3.3.3-3. Fixed reference channel for maximum input level receiver requirements (SCS 60 kHz, TDD, 64QAM)

| Parameter | Unit |  | Value |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 70 | 80 | 100 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Allocated resource blocks |  | 11 | 18 | 24 | 31 | 38 | 51 | 65 | 79 | 93 | 107 | 135 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 26 | 24 | 24 |
| MCS Index |  | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| MCS Table for TBS determination |  | 64QAM |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM | 64 QAM |
| Target Coding Rate |  | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 | 3/4 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39} | Bits | 5376 | 8712 | 11784 | 15112 | 18432 | 25104 | 31752 | 38936 | 45096 | 52224 | 65576 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39} | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39} | CBs | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 7 | 8 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39} | Bits | 7128 | 11664 | 15552 | 20088 | 24624 | 33048 | 42120 | 51192 | 60264 | 69336 | 87480 |
| Max. Throughput averaged over 1 frame | Mbps | 12.902 | 20.909 | 28.282 | 36.269 | 44.237 | 60.250 | 76.205 | 93.446 | 108.23 | 125.338 | 157.382 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frame |  |  |  |  |  |  |  |  |  |  |  |  |

### A.3.3.4 FRC for maximum input level for 256 QAM

Table A.3.3.4-1 Fixed reference channel for maximum input level receiver requirements (SCS 15 kHz, TDD, 256QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 5, 10, 15, 20 (NOTE 5) | 5 | 10 | 15 | 20 | 25 | 30 | 40 | 50 |
| Subcarrier spacing | kHz | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Allocated resource blocks |  | 15 | 25 | 52 | 79 | 106 | 133 | 160 | 216 | 270 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| MCS Index |  | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 |
| MCS table for TBS determination |  | 256QAM |  |  |  |  |  |  |  |  |
| Modulation |  | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM |
| Target Coding Rate |  | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,3,4,8,9 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,5,6,7 | Bits | 9992 | 16896 | 34816 | 53288 | 71688 | 90176 | 108552 | 143400 | 180376 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,3,4,8,9 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,5,6,7 | CBs | 2 | 3 | 5 | 7 | 9 | 12 | 14 | 18 | 23 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,3,4,8,9 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,5,6,7 | Bits | 12960 | 21600 | 44928 | 68256 | 91584 | 114912 | 138240 | 186624 | 233280 |
| Max. Throughput averaged over 1 frame | Mbps | 3.997 | 6.758 | 13.926 | 21.315 | 28.675 | 36.070 | 43.421 | 57.360 | 72.150 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot 0 of each frameNOTE 4: Slot i is slot index per frameNOTE 5: Channel bandwidths in this column only apply to UEs supporting IE supportOfERedCap-r18. |  |  |  |  |  |  |  |  |  |  |

Table A.3.3.4-2 Fixed Reference channel for maximum input level receiver requirements (SCS 30 kHz, TDD, 256QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10, 15, 20 (NOTE 5) | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 70 | 80 | 100 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Allocated resource blocks |  | 7 | 24 | 38 | 51 | 65 | 78 | 106 | 133 | 162 | 189 | 217 | 273 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 13 | 11 | 11 |
| MCS Index |  | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 |
| MCS Table for TBS determination |  |  | 256QAM |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM |
| Target Coding Rate |  | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19} | Bits | 4736 | 16136 | 25608 | 33816 | 44040 | 52224 | 71688 | 90176 | 108552 | 127080 | 147576 | 184424 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19} | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19} | CBs | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 3 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19} | Bits | 6048 | 20736 | 32832 | 44064 | 56160 | 67392 | 91584 | 114912 | 139968 | 163296 | 187488 | 235872 |
| Max. Throughput averaged over 1 frame | Mbps | 5.210 | 17.750 | 28.169 | 37.198 | 48.444 | 57.446 | 78.857 | 99.194 | 119.407 | 139.788 | 162.334 | 202.866 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frameNOTE 5: Channel bandwidths in this column only apply to UEs supporting IE supportOfERedCap-r18. |  |  |  |  |  |  |  |  |  |  |  |  |  |

Table A.3.3.4-3 Fixed reference channel for maximum input level receiver requirements (SCS 60 kHz, TDD, 256QAM)

| Parameter | Unit |  | Value |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 70 | 80 | 100 |
| Subcarrier spacing configuration ![](media_svg/image1.svg) [公式: Μ] |  | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Allocated resource blocks |  | 11 | 18 | 24 | 31 | 38 | 51 | 65 | 79 | 93 | 107 | 135 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 26 | 24 | 24 |
| MCS Index |  | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 |
| MCS Table for TBS determination |  | 256QAM |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM | 256 QAM |
| Target Coding Rate |  | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39} | Bits | 7424 | 12040 | 16136 | 21000 | 25608 | 33816 | 44040 | 53288 | 62504 | 71688 | 90176 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39} | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39} | CBs | 1 | 2 | 3 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 12 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39} | Bits | 9504 | 15552 | 20736 | 26784 | 32832 | 44064 | 56160 | 68256 | 80352 | 92448 | 116640 |
| Max. Throughput averaged over 1 frame | Mbps | 17.818 | 28.896 | 38.726 | 50.400 | 61.459 | 81.158 | 105.696 | 127.891 | 150.010 | 172.051 | 216.422 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frame |  |  |  |  |  |  |  |  |  |  |  |  |

### A.3.3.5 FRC for maximum input level for 1024 QAM

Table A.3.3.5-1 Fixed reference channel for maximum input level receiver requirements (SCS 15 kHz, TDD, 1024QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 5 | 10 | 15 | 20 | 25 | 30 | 40 | 50 |
| Subcarrier spacing | kHz | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| Subcarrier spacing configuration $\mu  $ |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Allocated resource blocks |  | 25 | 52 | 79 | 106 | 133 | 160 | 216 | 270 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| MCS Index |  | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 |
| MCS table for TBS determination |  | 1024QAM |  |  |  |  |  |  |  |
| Modulation |  | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM |
| Target Coding Rate |  | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,3,4,8,9 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,5,6,7 | Bits | 21000 | 44040 | 67584 | 90176 | 112648 | 135296 | 184424 | 229576 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,3,4,8,9 | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,5,6,7 | CBs | 3 | 6 | 9 | 11 | 14 | 17 | 22 | 28 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,3,4,8,9 | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slots 2,5,6,7 | Bits | 27000 | 56160 | 85320 | 114480 | 143640 | 172800 | 233280 | 291600 |
| Max. Throughput averaged over 1 frame | Mbps | 8.400 | 17.616 | 27.034 | 36.070 | 45.059 | 54.118 | 73.770 | 91.830 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot 0 of each frameNOTE 4: Slot i is slot index per frame |  |  |  |  |  |  |  |  |  |

Table A.3.3.5-2 Fixed Reference channel for maximum input level receiver requirements (SCS 30 kHz, TDD, 1024QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 70 | 80 | 100 |
| Subcarrier spacing configuration $\mu  $ |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Allocated resource blocks |  | 24 | 38 | 51 | 65 | 78 | 106 | 133 | 162 | 189 | 217 | 273 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 13 | 11 | 11 |
| MCS Index |  | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 |
| MCS Table for TBS determination |  | 1024QAM |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM |
| Target Coding Rate |  | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19} | Bits | 20496 | 32264 | 43032 | 55304 | 65576 | 90176 | 112648 | 139376 | 159800 | 184424 | 233608 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19} | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19} | CBs | 3 | 4 | 6 | 7 | 8 | 11 | 14 | 17 | 19 | 22 | 28 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19} | Bits | 25920 | 41040 | 55080 | 70200 | 84240 | 114480 | 143640 | 174960 | 204120 | 234360 | 294840 |
| Max. Throughput averaged over 1 frame | Mbps | 22.546 | 35.490 | 47.335 | 60.834 | 72.134 | 99.194 | 123.913 | 153.314 | 175.868 | 202.866 | 256.969 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frame |  |  |  |  |  |  |  |  |  |  |  |  |

Table A.3.3.5-3 Fixed reference channel for maximum input level receiver requirements (SCS 60 kHz, TDD, 1024QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 70 | 80 | 100 |
| Subcarrier spacing configuration $\mu  $ |  | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Allocated resource blocks |  | 11 | 18 | 24 | 31 | 38 | 51 | 65 | 79 | 93 | 107 | 135 |
| Subcarriers per resource block |  | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Allocated slots per Frame |  | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 26 | 24 | 24 |
| MCS Index |  | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 23 |
| MCS Table for TBS determination |  | 1024QAM |  |  |  |  |  |  |  |  |  |  |
| Modulation |  | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM | 1024 QAM |
| Target Coding Rate |  | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 |
| Maximum number of HARQ transmissions |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Information Bit Payload per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39} | Bits | 9224 | 15368 | 20496 | 26120 | 32264 | 43032 | 55304 | 67584 | 79896 | 90176 | 114776 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39} | CBs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39} | CBs | 2 | 2 | 3 | 4 | 4 | 6 | 7 | 9 | 10 | 11 | 14 |
| Binary Channel Bits per Slot |  |  |  |  |  |  |  |  |  |  |  |  |
| For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39} | Bits | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39} | Bits | 11880 | 19440 | 25920 | 33480 | 41040 | 55080 | 70200 | 85320 | 100440 | 115560 | 145800 |
| Max. Throughput averaged over 1 frame | Mbps | 22.138 | 36.883 | 49.190 | 62.688 | 77.434 | 103.277 | 132.730 | 162.202 | 191.750 | 216.422 | 275.462 |
| NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 3: SS/PBCH block is transmitted in slot #0 of each frameNOTE 4: Slot i is slot index per frame |  |  |  |  |  |  |  |  |  |  |  |  |

# A.3M LP-WUR reference channel

## A.3M.1 General

Unless otherwise stated, Table A.3M.1-1 is applicable for all receiver requirements of LP-WUR when LP-WUS is generated with 15 KHz SCS. Table A.3M.1-2 is applicable for all receiver requirements of LP-WUR when LP-WUS is generated with 30 KHz SCS.

Table A.3M.1-1. Common reference channel parameters for 15 kHz SCS

| Parameter | Unit | Value |
| --- | --- | --- |
| MR Channel bandwidth | MHz | All CBW |
| LP-WUS bandwidth | RB | 11 |
| Subcarrier spacing | kHz | 15 |
| RM coding | Bits | 16 |
| CRC |  | No CRC |
| Chip rate |  | M=4 (4 chips in an OFDM symbol) |
| Overlaid OFDM sequence |  | Length 33: generated by 31-length ZC sequence with extension |
| Number of overlaid OFDM sequence per chip to carry information |  | 4 |
| LP-WUS duration for OOK |  | 8 OFDM symbols |
| LP-WUS duration for OFDM |  | 2 OFDM symbols |
| Manchester coding for OOK |  | ½ |
| Number of information bits | Bits | 5 |

Table A.3M.1-2. Common reference channel parameters for 30 kHz SCS

| Parameter | Unit | Value |
| --- | --- | --- |
| MR Channel bandwidth | MHz | All CBW |
| LP-WUS bandwidth | RB | 11 |
| Subcarrier spacing | kHz | 30 |
| RM coding | Bits | 16 |
| CRC |  | No CRC |
| Chip rate |  | M=4 (4 chips in an OFDM symbol) |
| Overlaid OFDM sequence |  | Length 33: generated by 31-length ZC sequence with extension |
| Number of overlaid OFDM sequence per chip to carry information |  | 4 |
| LP-WUS duration for OOK |  | 8 OFDM symbols |
| LP-WUS duration for OFDM |  | 2 OFDM symbols |
| Manchester coding for OOK |  | ½ |
| Number of information bits | Bits | 5 |

# A.4 CSI reference measurement channels

# A.5 OFDMA Channel Noise Generator (OCNG)

## A.5.1 OCNG Patterns for FDD

### A.5.1.1 OCNG FDD pattern 1: Generic OCNG FDD Pattern for all unused REs

Table A.5.1.1-1: OP.1 FDD: Generic OCNG FDD Pattern for all unused REs

| OCNG ApplianceOCNG Parameters | Control Region  (Core Set) | Data Region |
| --- | --- | --- |
| Resources allocated | All unused REs (Note 1) | All unused REs (Note 2) |
| Structure | PDCCH | PDSCH |
| Content | Uncorrelated pseudo random QPSK modulated data | Uncorrelated pseudo random QPSK modulated data |
| Transmission scheme for multipleantennas ports transmission | Single Tx port transmission | Spatial multiplexing using any precoding matrix with dimensions same as the precoding matrix for PDSCH |
| Subcarrier Spacing | Same as for RMC PDCCH in the active BWP | Same as for RMC PDSCH in the active BWP |
| Power Level | Same as for RMC PDCCH | Same as for RMC PDSCH |
| NOTE 1: All unused REs in the active CORESETS appointed by the search spaces in use.NOTE 2: Unused available REs refer to REs in PRBs not allocated for any physical channels, CORESETs, synchronization signals or reference signals in channel bandwidth. |  |  |

## A.5.2 OCNG Patterns for TDD

### A.5.2.1 OCNG TDD pattern 1: Generic OCNG TDD Pattern for all unused REs

Table A.5.2.1-1: OP.1 TDD: Generic OCNG TDD Pattern for all unused REs

| OCNG ApplianceOCNG Parameters | Control Region  (Core Set) | Data Region |
| --- | --- | --- |
| Resources allocated | All unused REs (Note 1) | All unused REs (Note 2) |
| Structure | PDCCH | PDSCH |
| Content | Uncorrelated pseudo random QPSK modulated data | Uncorrelated pseudo random QPSK modulated data |
| Transmission scheme for multipleantennas ports transmission | Single Tx port transmission | Spatial multiplexing using any precoding matrix with dimensions same as the precoding matrix for PDSCH |
| Subcarrier Spacing | Same as for RMC PDCCH in the active BWP | Same as for RMC PDSCH in the active BWP |
| Power Level | Same as for RMC PDCCH | Same as for RMC PDSCH |
| NOTE 1: All unused REs in the active CORESETS appointed by the search spaces in use.NOTE 2: Unused available REs refer to REs in PRBs not allocated for any physical channels, CORESETs, synchronization signals or reference signals in channel bandwidth. |  |  |

# A.6 Void

# A.7 V2X reference measurement channels

## A.7.1 General

The algorithm for determining the payload size A is as follows; given a desired coding rate R and radio block allocation NRB

1. Calculate the RE number of 2nd stage SCI Q_SCI2^' that can be transmitted in a given sub-frame, where in order to make sure that the code-rate of 2-A is approximate to SCI 1-A, a beta offset is selected based on MCS, and vacant resource elements γ value is determined based on NRB and DMRS frequency density.

2. Transport Block Size is determined according to clause 8.1.3.2 of TS 38.214 [13] based on Table A.7.1-1.

3. Calculate Binary Channel Bits per Slot for PSSCH as below

Binary Channel Bits per Slot  = (NRB* Subcarriers per resource block*CP-OFDM symbols per slot – DMRS resource REs – PSCCH resource Res - Q_SCI2^') * Qm

Where Qm is the modulation order corresponding to MCS.

In Table A.7.1-1 Common reference channel parameters are listed the Sidelink reference measurement channels specified in annexes A.7.2 to A.7.6.

Table A.7.1-1: Common reference channel parameters

| Parameter | Value | remark |
| --- | --- | --- |
| Number of HARQ Processes | 1 |  |
| Channel state | AWGN |  |
| Subcarriers per resource block | 12 |  |
| sl-PSSCH-DMRS-TimePatternList | 2 | symbol4 and symbol 10 in each slotFDMed with PSSCH within DMRS symbolFrequency density is ½ |
| CP-OFDM symbols per slot (Note1) | 12 for all slots | Excluding the first OFDM symbol in one SL slot used for AGC |
| PSCCH resource | 10 PRBs, 3 symbols in time domain |  |
| Slot number in 10ms | $ 10*2^{\mu  }$ | $\mu  =0,1,2 $ for 15kHz, 30kHz, 60kHz |
| PT-RS | disable |  |
| CSI-RS | disable |  |
| x-overhead | 0 |  |
| PSFCH period | 0 |  |
| 2nd stage SCI payload size | 59 | 35bits SCI-2A + 24bits CRC |
| Redundancy Version | RV0 | For channel coding |
| Alpha value for SCI-2 | 1 |  |

## A.7.2 FRC for V2X receiver requirements for QPSK

For V2X transmission over PC5, Table A.7.2-1, Table A.7.2-2 and Table A.7.2-3 are applicable for measurements on the Receiver Characteristics with the exception of Maximum input level.

Table A.7.2-1: Fixed reference channel for V2X receiver requirements (SCS 15 kHz, QPSK)

| Parameter | Unit | Value |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 53 | 10 | 20 | 30 | 40 |
| Subcarrier spacing | kHz | 15 | 15 | 15 | 15 | 15 |
| Subchannel size |  | 12 | 10 | 15 | 10 | 12 |
| Allocated resource blocks |  | 24 | 50 | 105 | 160 | 216 |
| MCS Index |  | 4 | 4 | 4 | 4 | 4 |
| MCS Table for TBS determination | 64QAM |  |  |  |  |  |
| Modulation |  | QPSK | QPSK | QPSK | QPSK | QPSK |
| Transport Block Size |  | 1608 | 3624 | 7936 | 12296 | 16896 |
| Transport block CRC | Bits | 16 | 16 | 24 | 24 | 24 |
| LDPC base graph |  | 2 | 2 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  | 1 | 1 | 1 | 2 | 3 |
| Beta offset for 2nd stage SCI |  | 2.25 | 2.25 | 2.25 | 2.25 | 2.25 |
| $\gamma  $ value when  2nd stage SCI rate match |  | 7 | 1 | 1 | 1 | 1 |
| Binary Channel Bits per Slot |  | 5160 | 12036 | 26556 | 41076 | 55860 |
| Max. Throughput averaged over 100ms | Mbps | 0.1608 | 0.3624 | 0.7936 | 1.2296 | 1.6896 |
| NOTE 1: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 2: $\gamma  $ is the number of vacant resource elements in the resource block to which the last coded symbol of the 2nd-stage SCI belongs.NOTE 3:  The CBW is only applicable for PS UE in n14. |  |  |  |  |  |  |

Table A.7.2-2: Fixed reference channel for V2X receiver requirements (SCS 30 kHz, QPSK)

| Parameter | Unit | Value |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 20 | 30 | 40 | 60 | 80 | 100 |
| Subcarrier spacing | kHz | 30 | 30 | 30 | 30 | [30] | [30] | [30] |
| Subchannel size |  | 12 | 10 | 15 | 15 | [10] | [12] | [15] |
| Allocated resource blocks |  | 24 | 50 | 75 | 105 | [160] | [216] | [270] |
| MCS Index |  | 4 | 4 | 4 | 4 | [4] | [4] | [4] |
| MCS Table for TBS determination | 64QAM |  |  |  |  |  |  |  |
| Modulation |  | QPSK | QPSK | QPSK | QPSK | [QPSK] | [QPSK] | [QPSK] |
| Transport Block Size |  | 1608 | 3624 | 5632 | 7936 | [12296] | [16392] | [21000] |
| Transport block CRC | Bits | 16 | 16 | 24 | 24 | [24] | [24] | [24] |
| LDPC base graph |  | 2 | 2 | 1 | 1 | [1] | [1] | [1] |
| Number of Code Blocks per Slot |  | 1 | 1 | 1 | 1 | [2] | [2] | [3] |
| Beta offset for 2nd stage SCI |  | 2.25 | 2.25 | 2.25 | 2.25 | [2.25] | [2.25] | [2.25] |
| $\gamma  $ value when  2nd stage SCI rate match |  | 7 | 1 | 1 | 1 | [1] | [1] | [1] |
| Binary Channel Bits per Slot |  | 5160 | 12036 | 18636 | 26556 | [41076] | [55860] | [70116] |
| Max. Throughput averaged over 100ms | Mbps | 0.3216 | 0.7248 | 1.1264 | 1.5872 | [2.4592] | [3.2784] | [4.2] |
| NOTE 1: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 2: $\gamma  $ is the number of vacant resource elements in the resource block to which the last coded symbol of the 2nd-stage SCI belongs. |  |  |  |  |  |  |  |  |

Table A.7.2-3: Fixed reference channel for V2X receiver requirements (SCS 60 kHz, QPSK)

| Parameter | Unit | Value |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 20 | 30 | 40 | 60 | 80 | 100 |
| Subcarrier spacing | kHz | 60 | 60 | 60 | 60 | [60] | [60] | [60] |
| Subchannel size |  | 10 | 12 | 12 | 10 | [15] | [15] | [15] |
| Allocated resource blocks |  | 10 | 24 | 36 | 50 | [75] | [105] | [135] |
| MCS Index |  | 4 | 4 | 4 | 4 | [4] | [4] | [4] |
| MCS Table for TBS determination | 64QAM |  |  |  |  |  |  |  |
| Modulation |  | QPSK | QPSK | QPSK | QPSK | [QPSK] | [QPSK] | [QPSK] |
| Transport Block Size |  | 456 | 1608 | 2536 | 3624 | [5504] | [7936] | [10248] |
| Transport block CRC | Bits | 16 | 16 | 16 | 16 | [24] | [24] | [24] |
| LDPC base graph |  | 2 | 2 | 2 | 2 | [1] | [1] | [1] |
| Number of Code Blocks per Slot |  | 1 | 1 | 1 | 1 | [1] | [1] | [2] |
| Beta offset for 2nd stage SCI |  | 2.25 | 2.25 | 2.25 | 2.25 | [2.25] | [2.25] | [2.25] |
| $\gamma  $ value when  2nd stage SCI rate match |  | 7 | 7 | 7 | 1 | [1] | [1] | [1] |
| Binary Channel Bits per Slot |  | 1464 | 5160 | 8328 | 12036 | [18636] | [26556] | [34476] |
| Max. Throughput averaged over 100ms | Mbps | 0.1824 | 0.6432 | 1.0144 | 1.4496 | [2.2016] | [3.1744] | [4.0992] |
| NOTE 1: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 2: $\gamma  $ is the number of vacant resource elements in the resource block to which the last coded symbol of the 2nd-stage SCI belongs. |  |  |  |  |  |  |  |  |

## A.7.3 FRC for maximum input level for 64QAM

For V2X transmission over PC5, Table A.7.3-1, Table A.7.3-2 and TableA.7.3-3 are applicable for Maximum input level when the maximum modulation order is 64QAM.

Table A.7.3-1: Fixed reference channel for V2X receiver requirements (SCS 15 kHz, 64QAM)

| Parameter | Unit | Value |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 53 | 10 | 20 | 30 | 40 |
| Subcarrier spacing | kHz | 15 | 15 | 15 | 15 | 15 |
| Subchannel size |  | 12 | 10 | 15 | 10 | 12 |
| Allocated resource blocks |  | 24 | 50 | 105 | 160 | 216 |
| MCS Index |  | 24 | 24 | 24 | 24 | 24 |
| MCS Table for TBS determination | 64QAM |  |  |  |  |  |
| Modulation |  | 64QAM | 64QAM | 64QAM | 64QAM | 64QAM |
| Transport Block Size |  | 11528 | 27144 | 60456 | 92200 | 127080 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  | 2 | 4 | 8 | 11 | 16 |
| Beta offset for 2nd stage SCI |  | 6.25 | 6.25 | 6.25 | 6.25 | 6.25 |
| $\gamma  $ value when  2nd stage SCI rate match |  | 7 | 1 | 1 | 1 | 1 |
| Binary Channel Bits per Slot |  | 15336 | 35964 | 79524 | 123084 | 167436 |
| Max. Throughput averaged over 100ms | Mbps | 1.1528 | 2.7144 | 6.0456 | 9.22 | 12.708 |
| NOTE 1: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 2: $\gamma  $ is the number of vacant resource elements in the resource block to which the last coded symbol of the 2nd-stage SCI belongs.NOTE 3: The CBW is only applicable for PS UE in n14. |  |  |  |  |  |  |

Table A.7.3-2: Fixed reference channel for V2X receiver requirements (SCS 30 kHz, 64QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 20 | 30 | 40 | 60 | 80 | 100 |
| Subcarrier spacing | kHz | 30 | 30 | 30 | 30 | [30] | [30] | [30] |
| Subchannel size |  | 12 | 10 | 15 | 15 | [10] | [12] | [15] |
| Allocated resource blocks |  | 24 | 50 | 75 | 105 | [160] | [216] | [270] |
| MCS Index |  | 24 | 24 | 24 | 24 | [24] | [24] | [24] |
| MCS Table for TBS determination | 64QAM |  |  |  |  |  |  |  |
| Modulation |  | 64QAM | 64QAM | 64QAM | 64QAM | [64QAM] | [64QAM] | [64QAM] |
| Transport Block Size |  | 11528 | 27144 | 42016 | 60456 | [92200] | [125016] | [155776] |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | [24] | [24] | [24] |
| LDPC base graph |  | 1 | 1 | 1 | 1 | [1] | [1] | [1] |
| Number of Code Blocks per Slot |  | 2 | 4 | 5 | 8 | [11] | [15] | [19] |
| Beta offset for 2nd stage SCI |  | 6.25 | 6.25 | 6.25 | 6.25 | [6.25] | [6.25] | [6.25] |
| $\gamma  $ value when  2nd stage SCI rate match |  | 7 | 1 | 1 | 1 | [1] | [1] | [1] |
| Binary Channel Bits per Slot |  | 15336 | 35964 | 55764 | 79524 | [123084] | [167436] | [210204] |
| Max. Throughput averaged over 100ms | Mbps | 2.3056 | 5.4288 | 8.4032 | 12.091 | [18.44] | [25.0032] | [31.1552] |
| NOTE 1: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 2: $\gamma  $ is the number of vacant resource elements in the resource block to which the last coded symbol of the 2nd-stage SCI belongs. |  |  |  |  |  |  |  |  |

TableA.7.3-3: Fixed reference channel for V2X receiver requirements (SCS 60 kHz, 64QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 20 | 30 | 40 | 60 | 80 | 100 |
| Subcarrier spacing | kHz | 60 | 60 | 60 | 60 | [60] | [60] | [60] |
| Subchannel size |  | 10 | 12 | 12 | 10 | [15] | [15] | [15] |
| Allocated resource blocks |  | 10 | 24 | 36 | 50 | [75] | [105] | [135] |
| MCS Index |  | 24 | 24 | 24 | 24 | [24] | [24] | [24] |
| MCS Table for TBS determination | 64QAM |  |  |  |  |  |  |  |
| Modulation |  | 64QAM | 64QAM | 64QAM | 64QAM | [64QAM] | [64QAM] | [64QAM] |
| Transport Block Size |  | 3240 | 11528 | 18960 | 27144 | [42016] | [59432] | [77896] |
| Transport block CRC | Bits | 16 | 24 | 24 | 24 | [24] | [24] | [24] |
| LDPC base graph |  | 2 | 1 | 1 | 1 | [1] | [1] | [1] |
| Number of Code Blocks per Slot |  | 1 | 2 | 3 | 4 | [5] | [8] | [10] |
| Beta offset for 2nd stage SCI |  | 6.25 | 6.25 | 6.25 | 6.25 | [6.25] | [6.25] | [6.25] |
| $\gamma  $ value when  2nd stage SCI rate match |  | 7 | 7 | 7 | 1 |  |  |  |
| Binary Channel Bits per Slot |  | 4248 | 15336 | 24840 | 35964 | [55764] | [79524] | [103284] |
| Max. Throughput averaged over 100ms | Mbps | 1.296 | 4.6112 | 7.584 | 10.858 | [16.8064] | [23.7728] | [31.1584] |
| NOTE 1: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 2: $\gamma  $ is the number of vacant resource elements in the resource block to which the last coded symbol of the 2nd-stage SCI belongs. |  |  |  |  |  |  |  |  |

## A.7.4 FRC for maximum input level for 256QAM

For V2X transmission over PC5, Table A.7.4-1, Table A.7.4-2 and Table A.7.4-3 are applicable for Maximum input level when the 256QAM is supported.

Table A.7.4-1: Fixed reference channel for V2X receiver requirements (SCS 15 kHz, 256QAM)

| Parameter | Unit | Value |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 53 | 10 | 20 | 30 | 40 |
| Subcarrier spacing | kHz | 15 | 15 | 15 | 15 | 15 |
| Subchannel size |  | 12 | 10 | 15 | 10 | 12 |
| Allocated resource blocks |  | 24 | 50 | 105 | 160 | 216 |
| MCS Index |  | 23 | 23 | 23 | 23 | 23 |
| MCS Table for TBS determination | 256QAM |  |  |  |  |  |
| Modulation |  | 256QAM | 256QAM | 256QAM | 256QAM | 256QAM |
| Transport Block Size |  | 15880 | 36896 | 81976 | 127080 | 172176 |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | 24 |
| LDPC base graph |  | 1 | 1 | 1 | 1 | 1 |
| Number of Code Blocks per Slot |  | 2 | 5 | 10 | 16 | 21 |
| Beta offset for 2nd stage SCI |  | 6.25 | 6.25 | 6.25 | 6.25 | 6.25 |
| $\gamma  $ value when  2nd stage SCI rate match |  | 3 | 3 | 3 | 3 | 3 |
| Binary Channel Bits per Slot |  | 20544 | 48000 | 106080 | 164160 | 223296 |
| Max. Throughput averaged over 100ms | Mbps | 1.588 | 3.6896 | 8.1976 | 12.708 | 17.218 |
| NOTE 1: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 2: $\gamma  $ is the number of vacant resource elements in the resource block to which the last coded symbol of the 2nd-stage SCI belongs.NOTE 3: The CBW is only applicable for PS UE in n14. |  |  |  |  |  |  |

Table A.7.4-2: Fixed reference channel for V2X receiver requirements (SCS 30 kHz, 256QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 20 | 30 | 40 | 60 | 80 | 100 |
| Subcarrier spacing | kHz | 30 | 30 | 30 | 30 | [30] | [30] | [30] |
| Subchannel size |  | 12 | 10 | 15 | 15 | [10] | [12] | [15] |
| Allocated resource blocks |  | 24 | 50 | 75 | 105 | [160] | [216] | [270] |
| MCS Index |  | 23 | 23 | 23 | 23 | [24] | [24] | [24] |
| MCS Table for TBS determination | 256QAM |  |  |  |  |  |  |  |
| Modulation |  | 256QAM | 256QAM | 256QAM | 256QAM | [256QAM] | [256QAM] | [256QAM] |
| Transport Block Size |  | 15880 | 36896 | 58384 | 81976 | [127080] | [172176] | [217128] |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | [24] | [24] | [24] |
| LDPC base graph |  | 1 | 1 | 1 | 1 | [1] | [1] | [1] |
| Number of Code Blocks per Slot |  | 2 | 5 | 7 | 10 | [16] | [21] | [26] |
| Beta offset for 2nd stage SCI |  | 6.25 | 6.25 | 6.25 | 6.25 | [6.25] | [6.25] | [6.25] |
| $\gamma  $ value when  2nd stage SCI rate match |  | 3 | 3 | 3 | 3 | [3] | [3] | [3] |
| Binary Channel Bits per Slot |  | 20544 | 48000 | 74400 | 106080 | [164160] | [223296] | [280320] |
| Max. Throughput averaged over 100ms | Mbps | 3.176 | 7.3792 | 11.677 | 16.395 | [25.416] | [34.4352] | [43.4256] |
| NOTE 1: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 2: $\gamma  $ is the number of vacant resource elements in the resource block to which the last coded symbol of the 2nd-stage SCI belongs. |  |  |  |  |  |  |  |  |

Table A.7.4-3: Fixed reference channel for V2X receiver requirements (SCS 60kHz, 256QAM)

| Parameter | Unit | Value |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth | MHz | 10 | 20 | 30 | 40 | 60 | 80 | 100 |
| Subcarrier spacing | kHz | 60 | 60 | 60 | 60 | [60] | [60] | [60] |
| Subchannel size |  | 10 | 12 | 12 | 10 | [15] | [15] | [15] |
| Allocated resource blocks |  | 10 | 24 | 36 | 50 | [75] | [105] | [135] |
| MCS Index |  | 23 | 23 | 23 | 23 | [23] | [23] | [23] |
| MCS Table for TBS determination | 256QAM |  |  |  |  |  |  |  |
| Modulation |  | 256QAM | 256QAM | 256QAM | 256QAM | [256QAM] | [256QAM] | [256QAM] |
| Transport Block Size |  | 4480 | 15880 | 25608 | 36896 | [57376] | [81976] | [106576] |
| Transport block CRC | Bits | 24 | 24 | 24 | 24 | [24] | [24] | [24] |
| LDPC base graph |  | 1 | 1 | 1 | 1 | [1] | [1] | [1] |
| Number of Code Blocks per Slot |  | 1 | 2 | 4 | 5 | [7] | [10] | [13] |
| Beta offset for 2nd stage SCI |  | 6.25 | 6.25 | 6.25 | 6.25 | [6.25] | [6.25] | [6.25] |
| $\gamma  $ value when  2nd stage SCI rate match |  | 3 | 3 | 3 | 3 | [3] | [3] | [3] |
| Binary Channel Bits per Slot |  | 5760 | 20544 | 33216 | 48000 | [74400] | [106080] | [137760] |
| Max. Throughput averaged over 100ms | Mbps | 1.792 | 6.352 | 10.243 | 14.758 | [22.9504] | [32.7904] | [42.6304] |
| NOTE 1: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).NOTE 2: $\gamma  $ is the number of vacant resource elements in the resource block to which the last coded symbol of the 2nd-stage SCI belongs. |  |  |  |  |  |  |  |  |

# A.8 Reference measurement channels for low NR band carrier aggregation via switching

## A.8.1 DL reference measurement channels for low NR band carrier aggregation via switching

Table A.8.1-1: DL RMC for low NR band carrier aggregation via switching

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
| Switching Pattern for Low-band CA | LowBandCA-Switching-r19 -> switchingPattern-r19 | A bitmap of slots | 00011 00110 01100 11001 11100 11001 10011 00110 |
|  | Period of Switching Pattern | Slots | 40 |
|  | Slots on the PCell |  | A bit value of ‘0’ in LBCA-SwitchingPattern |
|  | Slots on the SCell |  | A bit value of ‘1’ in LBCA-SwitchingPattern |
| Switch-from DL slot on the PCell/SCell | Slot Location |  | Mod(i, 20) = 2, 4, 6, 8, 10, 12, 14, 16, 18 |
|  | The number of Switch-from Slot |  | 18 slots for each period of 40 slots. |
|  | CORESET frequency domain allocation |  | Full BW |
|  | CORESET time domain allocation |  | 2 OFDM symbol at the begin of each slot |
|  | PDSCH mapping type |  | Type A |
|  | PDSCH start symbol index (S) |  | 2 |
|  | Number of consecutive PDSCH symbols (L) |  | 12 - gapDurationPCelltoSCell-r19 for the slot indicated as ‘0’ in the LBCA-SwitchingPatternOr 12 - gapDurationSCelltoPCell-r19 for the slot indicated as ‘1’ in the LBCA-SwitchingPattern |
|  | PDSCH PRB bundling | PRBs | 2 |
|  | Dynamic PRB bundling |  | false |
|  | Overhead value for TBS determination |  | 0 |
|  | First DMRS position for Type A PDSCH mapping |  | 2 |
|  | DMRS type |  | Type 1 |
|  | Number of additional DMRS |  | 2 |
|  | FDM between DMRS and PDSCH |  | Disable |
|  | The number of slots between PDSCH and corresponding HARQ-ACK information (K1 Value) | Slots | 2 |
| Switch-to DL slot on the PCell/SCell | Slot Location |  | Mod(i, 20) = 3, 5, 7, 9, 11, 13, 15, 17, 19 |
|  | The number of Switch-from Slot |  | 18 slots for every period of 40 slots. |
|  | CORESET frequency domain allocation |  | Full BW |
|  | CORESET time domain allocation |  | 2 OFDM symbol at the begin of each slot |
|  | PDSCH mapping type |  | Type A |
|  | PDSCH start symbol index (S) |  | 2 |
|  | Number of consecutive PDSCH symbols (L) |  | 12 |
|  | PDSCH PRB bundling | PRBs | 2 |
|  | Dynamic PRB bundling |  | false |
|  | Overhead value for TBS determination |  | 0 |
|  | First DMRS position for Type A PDSCH mapping |  | 2 |
|  | DMRS type |  | Type 1 |
|  | Number of additional DMRS |  | 2 |
|  | FDM between DMRS and PDSCH |  | Disable |
|  | The number of slots between PDSCH and corresponding HARQ-ACK information (K1 Value) | Slots | 2 |
| HARQ process number |  |  | 4 |
| Subcarrier spacing |  | kHz | 15 |
| Subcarrier spacing configuration µ |  |  | 0 |
| Subcarriers per resource block |  |  | 12 |
| Allocated slots per period of 40 slots on the PCell |  | Slots | 18 |
| Allocated slots per period of 40 slots on the SCell |  | Slots | 18 |
| MCS Index |  |  | 4 |
| MCS Table for TBS determination |  |  | 64QAM / table 5.1.3.1-1: MCS index table 1 for PDSCH in TS 38.214 |
| Modulation |  |  | QPSK |
| Target Coding Rate R x [1024] |  |  | 308 |
| Maximum number of HARQ transmissions |  |  | 1 |
| Channel bandwidth |  |  | These parameters can refer to Table A.8.1-2 for differernt channel bandwidth. As PCell and SCell can be configured with different channel bandwidth, TBS per slot for PCell and SCell could be different. |
| Allocated resource blocks |  |  |  |
| Information Bit Payload (TBS) per Slot |  |  |  |
| Number of Code Blocks per Slot |  |  |  |
| Number of Code Blocks per Slot |  |  |  |
| Max. Throughput averaged over 4 frame |  | Mbps | (18*TBSPCell + 18*TBSSCell) / 0.04 / 10^6 |
| RTDP2S (NOTE2) |  | µs | 0 |
| RTDS2P (NOTE2) |  | µs | 0 |
| $ N_{TA}$ |  | $ T_{c}$ | 0 |
| $ N_{TA,offset}$ |  | $ T_{c}$ | 0 |
| gapDurationPCelltoSCell-r19 |  | Symbol | ‘1’ for 35us of  switchingPeriodForFDD-SDL-r19‘2’ for 70us of  switchingPeriodForFDD-SDL-r19‘3’ for 140us of  switchingPeriodForFDD-SDL-r19 |
| gapDurationSCelltoPCell-r19 |  | Symbol | ‘1’ for 35us of  switchingPeriodForFDD-SDL-r19‘2’ for 70us of  switchingPeriodForFDD-SDL-r19‘3’ for 140us of  switchingPeriodForFDD-SDL-r19 |
| CSIRS for tracking | First subcarrier index in the PRB used for CSI-RS (k0) |  | 0 for CSI-RS resource 1,2,3,4 |
|  | OFDM symbols in the PRB used for CSIRS |  | l0 = 6 for CSI-RS resource 1 and 3l0 = 10 for CSI-RS resource 2 and 4 |
|  | Number of CSI-RS ports |  | 1 for CSI-RS resource 1,2,3,4 |
|  | CDM Type |  | 'No CDM' for CSI-RS resource 1,2,3,4 |
|  | Density (ρ) |  | 3 for CSI-RS resource 1,2,3,4 |
|  | CSIRS periodicity | Slots | 40 for CSI-RS resource 1,2,3,4 |
|  | CSIRS offset | Slots | For PCell FDD band, CSI-RS offset are:0 for CSI-RS resource 1 and 21 for CSI-RS resource 3 and 4For SCell SDL band, CSI-RS offset are:20 for CSI-RS resource 1 and 221 for CSI-RS resource 3 and 4 |
|  | Frequency Occupation |  | Start PRB 0Number of PRB = BWP size |
|  | QCL info |  | TCI state #0 |
| PTRS configuration |  |  | PTRS is not configured |
| NOTE 1: Slot i is slot index per four frames.NOTE 2: The definition is referred to the clause 5.2.2 and 5.2.3 of TR 38.768 |  |  |  |

Table A.8.1-2: DL TBS for different channel bandwidth for low NR band carrier aggregation via switching

| Parameter |  | Unit | Value |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Channel bandwidth |  | MHz | 5 | 10 | 15 | 20 | 25 |
| Allocated resource blocks |  |  | 25 | 52 | 79 | 106 | 133 |
| For Slots i in which PDSCH is not allocated,If Mod(i, 20) = 0 or 1 | Information Bit Payload per Slot | Bits | NA | NA | NA | NA | NA |
|  | Number of Code Blocks per Slot | CBs | NA | NA | NA | NA | NA |
|  | Binary Channel Bits per Slot | Bits | NA | NA | NA | NA | NA |
| For Switch-from Slots i in which PDSCH is allocated,if Mod(i, 20) = 2, 4, 6, 8, 10, 12, 14, 16, 18 and ‘1’ is indicated by gapDurationPCelltoSCell-r19 or gapDurationSCelltoPCell-r19 | Allocated data symbols of PDSCH | Symbols | 8 |  |  |  |  |
|  | Information Bit Payload per Slot | Bits | 1480 | 2976 | 4480 | 6144 | 7680 |
|  | Transport block CRC | Bits | 16 | 16 | 24 | 24 | 24 |
|  | LDPC base graph |  | 2 | 2 | 1 | 1 | 1 |
|  | Number of Code Blocks per Slot / CBs | CBs | 1 | 1 | 1 | 1 | 1 |
|  | Binary Channel Bits per Slot / Bits | Bits | 4800 | 9984 | 15168 | 20352 | 25536 |
| For Switch-from Slots i in which PDSCH is allocated,if Mod(i, 20) = 2, 4, 6, 8, 10, 12, 14, 16, 18 and ‘2’ is indicated by gapDurationPCelltoSCell-r19 or gapDurationSCelltoPCell-r19 | Allocated data symbols of PDSCH | Symbols | 7 |  |  |  |  |
|  | Information Bit Payload per Slot | Bits | 1256 | 2664 | 3968 | 5376 | 6656 |
|  | Transport block CRC | Bits | 16 | 16 | 24 | 24 | 24 |
|  | LDPC base graph |  | 2 | 2 | 1 | 1 | 1 |
|  | Number of Code Blocks per Slot / CBs | CBs | 1 | 1 | 1 | 1 | 1 |
|  | Binary Channel Bits per Slot / Bits | Bits | 4200 | 8736 | 13272 | 17808 | 22344 |
| For Switch-from Slots i in which PDSCH is allocated,if Mod(i, 20) = 2, 4, 6, 8, 10, 12, 14, 16, 18 and ‘3’ is indicated by gapDurationPCelltoSCell-r19 or gapDurationSCelltoPCell-r19 | Allocated data symbols of PDSCH | Symbols | 6 |  |  |  |  |
|  | Information Bit Payload per Slot | Bits | 1128 | 2280 | 3496 | 4608 | 5760 |
|  | Transport block CRC | Bits | 16 | 16 | 16 | 24 | 24 |
|  | LDPC base graph |  | 2 | 2 | 2 | 1 | 1 |
|  | Number of Code Blocks per Slot / CBs | CBs | 1 | 1 | 1 | 1 | 1 |
|  | Binary Channel Bits per Slot / Bits | Bits | 3600 | 7488 | 11376 | 15264 | 19152 |
| For Switch-to Slots i in which PDSCH is allocated,If Mod(i, 20) = 3, 5, 7, 9, 11, 13, 15, 17, 19 | Allocated data symbols of PDSCH | Symbols | 9 |  |  |  |  |
|  | Information Bit Payload per Slot | Bits | 1672 | 3368 | 5120 | 6912 | 8712 |
|  | Transport block CRC | Bits | 16 | 16 | 24 | 24 | 24 |
|  | LDPC base graph |  | 2 | 2 | 1 | 1 | 1 |
|  | Number of Code Blocks per Slot | CBs | 1 | 1 | 1 | 1 | 2 |
|  | Binary Channel Bits per Slot | Bits | 5400 | 11232 | 17064 | 22896 | 28728 |
| NOTE 1: Additional parameters are specified in Table A.8.1-1.NOTE 2: If TB size is larger than 3824, the CRC sequence of L = 24 Bits is attached to each Code Block.NOTE 3: SS/PBCH block is transmitted in slot 0, 1 and 20, 21 of each period of 40 slots.NOTE 4: Slot i is slot index per four frames. |  |  |  |  |  |  |  |

###### Annex B (informative):
Void

###### Annex C (informative):
Downlink physical channels

# C.1 General

The following clauses, describes the downlink Physical Channels that are transmitted during a connection i.e., when measurements are done.

# C.2 Setup

Table C.2-1 describes the downlink Physical Channels that are required for connection set up.

Table C.2-1: Downlink Physical Channels required
for connection set-up

| Physical Channel |
| --- |
| PBCH |
| SSS |
| PSS |
| PDCCH |
| PDSCH |
| PBCH DMRS |
| PDCCH DMRS |
| PDSCH DMRS |
| CSI-RS |

# C.3 Connection

## C.3.1 Measurement of Receiver Characteristics

Unless otherwise stated, Table C.3.1-1 is applicable for measurements on the Receiver Characteristics (clause 7).

Table C.3.1-1: Downlink Physical Channels transmitted during a connection (FDD and TDD)

| Parameter | Unit | Value |
| --- | --- | --- |
| SSS transmit power | W | Test specific |
| EPRE ratio of PSS to SSS | dB | 0 |
| EPRE ratio of PBCH to SSS | dB | 0 |
| EPRE ratio of PBCH to PBCH DMRS | dB | 0 |
| EPRE ratio of PDCCH to SSS | dB | 0 |
| EPRE ratio of PDCCH to PDCCH DMRS | dB | 0 |
| EPRE ratio of PDSCH to SSS | dB | 0 |
| EPRE ratio of PDSCH to PDSCH DMRS (Note 1) | dB | -3 |
| EPRE ratio of CSI-RS to SSS | dB | 0 |
| EPRE ratio of PTRS to PDSCH | dB | Test specific |
| EPRE ratio of OCNG DMRS to SSS | dB | 0 |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) | dB | 0 |
| NOTE 1: No boosting is applied to any of the channels except PDSCH DMRS. For PDSCH DMRS, 3 dB power boosting is applied assuming DMRS Type 1 configuration when DMRS and PDSCH are TDM'ed and only half of the DMRS REs are occupied.NOTE 2: Number of DMRS CDM groups without data for PDSCH DMRS configuration for OCNG is set to 1. |  |  |

###### Annex D (normative):
Characteristics of the interfering signal

# D.1 General

Some RF performance requirements for the NR UE receiver are defined with interfering signals present in addition to the wanted signal.

For NR bands with FDL_high < 2700 MHz and FUL_high < 2700 MHz, a modulated 3 or 5 MHz full bandwidth NR down link signal, and in some cases an additional CW signal, are used as interfering signal for single carrier and inter-band CA cases. For intra-band contiguous CA bandwidth class B and C, a modulated 5 MHz NR downlink signal is used. And for some cases an additional CW signal is used.

For NR bands with FDL_low ≥ 3300 MHz and FUL_low ≥ 3300 MHz, a modulated NR downlink signal which equals to channel bandwidth of the wanted signal for single carrier and inter-band CA cases is used as interfering signal. For intra-band contiguous CA bandwidth Class C, a modulated NR downlink signal which equals to the aggregated channel bandwidth of the wanted signal is used. For intra-band contiguous CA bandwidth class D and E cases, a modulated 50 MHz NR downlink signal is used. And for some cases an additional CW signal is used.

# D.2 Void

###### Annex E (normative): 
Environmental conditions

# E.1 General

This normative annex specifies the environmental requirements of the UE. Within these limits the requirements of the present documents shall be fulfilled.

# E.2 Environmental

The requirements in this clause apply to all types of UE(s).

## E.2.1 Temperature

The UE shall fulfil all the requirements in the full temperature range of:

Table E.2.1-1: Temperature conditions

| +15C to +35C | For normal conditions (with relative humidity up to 75 %) |
| --- | --- |
| -10C to +55C | For extreme conditions (see IEC publications 6821 and 6822) |

Outside this temperature range the UE, if powered on, shall not make ineffective use of the radio frequency spectrum. In no case shall the UE exceed the transmitted levels as defined in clause 6.2 for extreme operation.

## E.2.2 Voltage

The UE shall fulfil all the requirements in the full voltage range, i.e. the voltage range between the extreme voltages.

The manufacturer shall declare the lower and higher extreme voltages and the approximate shutdown voltage. For the equipment that can be operated from one or more of the power sources listed below, the lower extreme voltage shall not be higher, and the higher extreme voltage shall not be lower than that specified below.

Table E.2.2-1: Voltage conditions

| Power source | Lower extremevoltage | Higher extremevoltage | Normal conditionsvoltage |
| --- | --- | --- | --- |
| AC mains | 0,9 * nominal | 1,1 * nominal | nominal |
| Regulated lead acid battery | 0,9 * nominal | 1,3 * nominal | 1,1 * nominal |
| Non regulated batteries:LeclanchéLithiumMercury/nickel & cadmium | 0,85 * nominal0,95 * nominal0,90 * nominal | Nominal1,1 * Nominal | Nominal1,1 * NominalNominal |

Outside this voltage range the UE if powered on, shall not make ineffective use of the radio frequency spectrum. In no case shall the UE exceed the transmitted levels as defined in clause 6.2 for extreme operation. In particular, the UE shall inhibit all RF transmissions when the power supply voltage is below the manufacturer declared shutdown voltage.

## E.2.3 Vibration

The UE shall fulfil all the requirements when vibrated at the following frequency/amplitudes.

Table E.2.3-1: Vibration conditions

| Frequency | ASD (Acceleration Spectral Density) random vibration |
| --- | --- |
| 5 Hz to 20 Hz | 0.96 m2/s3 |
| 20 Hz to 500 Hz | 0.96 m2/s3 at 20 Hz, thereafter –3 dB/Octave |

Outside the specified frequency range the UE, if powered on, shall not make ineffective use of the radio frequency spectrum. In no case shall the UE exceed the transmitted levels as defined in TS 38.101-1 for extreme operation.

###### Annex F (normative): 
Transmit modulation

# F.0 General

While measuring the transmit modulation quality of carriers, an existence of the carrier leakage needs to be taken into account indicated by the parameters in UplinkTxDirectCurrent IE, UplinkTxDirectCurrentTwoCarrierList-r16 or UplinkTxDirectCurrentMoreCarrierList.

# F.1 Measurement Point

Figure F.1-1 shows the measurement point for the unwanted emission falling into non-allocated RB(s) and the EVM for the allocated RB(s).

Figure F.1-1: EVM measurement points

# F.2 Basic Error Vector Magnitude measurement

The EVM is the difference between the ideal waveform and the measured waveform for the allocated RB(s)

![](media_svg/image4.svg) [公式≈: _{EVM}_{=}_{v}_{⊆}_{⎰}_{T}_{m}z_{T}&apos;(_{m}v)_{∪}−_{P}_{0}i(v)^{2}],

where

![](media_svg/image5.svg) [公式≈: ^{T}m] is a set of ![](media_svg/image6.svg) [公式≈: ^{T}m] modulation symbols with the considered modulation scheme being active within the measurement period,

![](media_svg/image7.svg) [公式: z&apos;(v)] are the samples of the signal evaluated for the EVM,

![](media_svg/image8.svg) [公式: i(v)] is the ideal signal reconstructed by the measurement equipment, and

![](media_svg/image9.svg) [公式≈: ^{P}0] is the average power of the ideal signal. For normalized modulation symbols ![](media_svg/image9.svg) [公式≈: ^{P}0] is equal to 1.

The basic EVM measurement interval is defined over one slot in the time domain for PUCCH and PUSCH and over one preamble sequence for the PRACH.

# F.3 Basic in-band emissions measurement

The in-band emissions are a measure of the interference falling into the non-allocated resources blocks. The in-band emission requirement is evaluated for PUCCH and PUSCH transmissions. The in-band emission requirement is not evaluated for PRACH transmissions.

The in-band emissions are measured as follows

![](media_svg/image10.svg) [公式≈: _{Emissions}_{absolute}_{(}_{δ}_{RB}_{)}_{=}^{√}^{⌡}⌡_{⌠}_{⌡}_{⌡}_{∞}_{T}_{1}T_{s}^{1}s_{t}_{⊆}_{⎰}t^{⊆}_{T}⎰_{s}Ts_{min(}max(_{f}_{h}^{f}_{f}_{+}^{l}_{max}^{+}f_{(}_{12}min^{(}^{12}_{,}_{∪}_{f}_{δ},_{⊆}^{∪}_{h}^{δ}f^{⊆}_{RB}_{+}l^{RB}_{12}+_{−}12_{11}^{+}_{∪}_{δ}^{11}∪δ_{)}_{RB}_{*}^{)}RB_{δ}^{*}_{*}^{δ}_{f}_{δ}*^{f}δ_{f}f_{)}^{Y})_{Y}^{(}^{t}_{(}^{,}_{t}_{,}^{f}_{f}^{)}_{)}^{2}_{2}^{,}^{δ}_{,}_{δ}^{RB}_{RB}^{<}_{>}^{0}_{0}],

where

![](media_svg/image11.svg) [公式≈: ^{T}s] is a set of ![](media_svg/image12.svg) [公式≈: ^{T}s]OFDM symbols with the considered modulation scheme being active within the measurement period,

![](media_svg/image13.svg) [公式≈: ^{δ}RB] is the starting frequency offset between the allocated RB and the measured non-allocated RB (e.g. ![](media_svg/image14.svg) [公式: δ_{RB}=1] or ![](media_svg/image15.svg) [公式: δ_{RB}=−1] for the first adjacent RB),

![](media_svg/image16.svg) [公式≈: ^{f}min] (resp. ![](media_svg/image17.svg) [公式≈: ^{f}max]) is the lower (resp. upper) edge of the UL UE channel bandwidth,

![](media_svg/image18.svg) [公式≈: ^{f}l] and ![](media_svg/image19.svg) [公式≈: ^{f}h] are the lower and upper edge of the allocated BW, and

![](media_svg/image20.svg) [公式: Y(t,f)] is the frequency domain signal evaluated for in-band emissions as defined in the clause (ii)

The relative in-band emissions are, given by

![](media_svg/image21.svg) [公式≈: ^{Emissions}relative^{(}^{δ}RB^{)}^{=}_{T}_{s}_{∪}_{1}_{N}^{Emissions}_{RB}_{⊆}_{t}_{⎰}_{T}_{s}f_{l}+(12^{absolute}_{⊆}∪N_{f}_{l}_{RB}−1)^{(}δ^{δ}f_{Y}^{RB}_{(}^{)}_{t}_{,}_{f}_{)}_{2}]

where

![](media_svg/image22.svg) [公式≈: ^{N}RB] is the number of allocated RBs

The basic in-band emissions measurement interval is defined over one slot in the time domain. When the PUSCH or PUCCH transmission slot is shortened due to multiplexing with SRS, the in-band emissions measurement interval is reduced by one OFDM symbol, accordingly.

In the evaluation of in-band emissions, the timing is set according to ![](media_svg/image23.svg) [公式: δ^{~}t=δc^{~}], where sample time offsets ![](media_svg/image24.svg) [公式: δ^{~}t] and ![](media_svg/image25.svg) [公式: δc^{~}] are defined in clause F.4.

# F.4 Modified signal under test

Implicit in the definition of EVM is an assumption that the receiver is able to compensate a number of transmitter impairments.

The DFT-s-OFDM modulated signals or PRACH signal under test is modified and, in the case of DFT-s-OFDM modulated signals, decoded according to:

![](media_svg/image26.svg) [公式≈: Z&apos;(t,f)=IDFT^{√}^{⌡}⌠_{⌡}_{∞}^{FFT}^{{}^{z}^{(}^{v}_{a}_{~}^{−}_{(}_{t}_{,}^{δ}_{f}^{~}^{t}_{)}^{)}_{∪}^{∪}_{e}^{e}_{j}^{−}_{ϑ}~^{j}_{(}^{2}_{t}_{,}^{Π}_{f}^{δ}_{)}^{~}^{f}^{v}^{}}^{.}^{e}^{j}^{2}^{Π}^{f}^{δ}^{~}^{t}^{∅}^{⌡}∇_{⌡}_{∈}]

where

![](media_svg/image27.svg) [公式: z(v)] is the time domain samples of the signal under test.

The CP-OFDM modulated signals or PUSCH demodulation reference signal or PUCCH data signal under test is equalised and, in the case of CP-OFDM modulated signals decoded according to:

![](media_svg/image28.svg) [公式≈: _{Z}_{&apos;}_{(}_{t}_{,}_{f}_{)}_{=}FFT{z(v_{a}_{~}−_{(}_{t}_{,}δ_{f}^{~}t_{)})_{∪}∪_{e}e_{j}^{−}_{ϑ}_{~}^{j}_{(}^{2}_{t}_{,}^{Π}_{f}^{δ}_{)}^{~}^{f}^{v}}.e^{j}^{2}^{Π}^{f}^{δ}^{~}^{t}]

where

![](media_svg/image27.svg) [公式: z(v)] is the time domain samples of the signal under test.

To minimize the error, the signal under test should be modified with respect to a set of parameters following the procedure explained below.

Notation:

![](media_svg/image29.svg) [公式: δ^{~}t] is the sample timing difference between the FFT processing window in relation to nominal timing of the ideal signal.

![](media_svg/image30.svg) [公式: δ^{~}f] is the RF frequency offset.

![](media_svg/image31.svg) [公式: ϑ^{~}(t,f)] is the phase response of the TX chain.

![](media_svg/image32.svg) [公式: a^{~}(t,f)] is the amplitude response of the TX chain.

In the following ![](media_svg/image25.svg) [公式: δc^{~}] represents the middle sample of the EVM window of length ![](media_svg/image33.svg) [公式: W] (defined in the next clauses) or the last sample of the first window half if ![](media_svg/image33.svg) [公式: W]is even.

The EVM analyser shall

- detect the start of each slot and estimate ![](media_svg/image24.svg) [公式: δ^{~}t] and ![](media_svg/image34.svg) [公式: δ^{~}f],

- determine ![](media_svg/image25.svg) [公式: δc^{~}] so that the EVM window of length ![](media_svg/image33.svg) [公式: W] is centred

- on the time interval determined by the measured cyclic prefix minus 16κ samples of the considered OFDM symbol for symbol l for subcarrier spacing configuration µ in a subframe, with l = 0 or l = 7*2^µ for normal CP, i.e. the first 16κ samples of the CP should not be taken into account for this step. In the determination of the number of excluded samples, a sampling rate of 1/Tc is assumed. If a different sampling rate is used, the number of excluded samples is scaled linearly.

- on the measured cyclic prefix of the considered OFDM symbol for all other symbols for normal CP and for symbol 0 to 11 for extended CP.

- on the measured preamble cyclic prefix for the PRACH

To determine the other parameters a sample timing offset equal to ![](media_svg/image25.svg) [公式: δc^{~}] is corrected from the signal under test. The EVM analyser shall then

- correct the RF frequency offset ![](media_svg/image30.svg) [公式: δ^{~}f]for each time slot, and

- apply an FFT of appropriate size. The chosen FFT size shall ensure that in the case of an ideal signal under test, there is no measured inter-subcarrier interference.

The carrier leakage shall be removed from the evaluated signal before calculating the EVM and the in-band emissions; however, the removed relative carrier leakage power also has to satisfy the applicable requirement.

At this stage the allocated RBs shall be separated from the non-allocated RBs. In the case of PUCCH and PUSCH EVM, the signal on the non-allocated RB(s), ![](media_svg/image35.svg) [公式: Y(t,f)], is used to evaluate the in-band emissions.

Moreover, the following procedure applies only to the signal on the allocated RB(s).

- In the case of PUCCH and PUSCH, the UL EVM analyzer shall estimate the TX chain equalizer coefficients ![](media_svg/image32.svg) [公式: a^{~}(t,f)]and ![](media_svg/image31.svg) [公式: ϑ^{~}(t,f)] used by the ZF equalizer for all subcarriers by time averaging at each signal subcarrier of the amplitude and phase of the reference and data symbols. The time-averaging length is 1 slot. This process creates an average amplitude and phase for each signal subcarrier used by the ZF equalizer. The knowledge of data modulation symbols may be required in this step because the determination of symbols by demodulation is not reliable before signal equalization.

- In the case of PRACH, the UL EVM analyzer shall estimate the TX chain coefficients ![](media_svg/image36.svg) [公式: a^{~}(t)]and ![](media_svg/image37.svg) [公式: ϑ^{~}(t)] used for phase and amplitude correction and are selected so as to minimize the resulting EVM. The TX chain coefficients are not dependent on frequency, i.e. ![](media_svg/image38.svg) [公式: a^{~}(t,f)=a^{~}(t)] and ![](media_svg/image39.svg) [公式: ϑ^{~}(t,f)=ϑ^{~}(t)]. The TX chain coefficient are chosen independently for each preamble transmission and for each ![](media_svg/image24.svg) [公式: δ^{~}t].

At this stage estimates of ![](media_svg/image30.svg) [公式: δ^{~}f], ![](media_svg/image32.svg) [公式: a^{~}(t,f)], ![](media_svg/image31.svg) [公式: ϑ^{~}(t,f)] and ![](media_svg/image25.svg) [公式: δc^{~}] are available. ![](media_svg/image24.svg) [公式: δ^{~}t] is one of the extremities of the window ![](media_svg/image33.svg) [公式: W], i.e. ![](media_svg/image24.svg) [公式: δ^{~}t]can be ![](media_svg/image40.svg) [公式≈: δc^{~}+Α−^{⋅}_{⋅}_{√}^{W}_{2}^{∂}_{∂}_{∃}] or ![](media_svg/image41.svg) [公式≈: _{δ}_{c}_{~}_{+}⋅_{⋅}_{√}W_{2}∂_{∂}_{∃}], where ![](media_svg/image42.svg) [公式: Α=0] if ![](media_svg/image43.svg) [公式: W] is odd and ![](media_svg/image44.svg) [公式: Α=1] if ![](media_svg/image45.svg) [公式: W]is even. The EVM analyser shall then

- calculate EVMl with ![](media_svg/image24.svg) [公式: δ^{~}t] set to ![](media_svg/image40.svg) [公式≈: δc^{~}+Α−^{⋅}_{⋅}_{√}^{W}_{2}^{∂}_{∂}_{∃}],

- calculate EVMh with ![](media_svg/image24.svg) [公式: δ^{~}t] set to ![](media_svg/image41.svg) [公式≈: _{δ}_{c}_{~}_{+}⋅_{⋅}_{√}W_{2}∂_{∂}_{∃}].

For the EVM calculation on the symbols with a transient period when the UE signals a transient period capability (tp) of 2, 4 or 7usec, $\Delta  \hat {t}$ is is given below.

- calculate EVMl_tp with $\Delta  \hat {t}$ set to $\lfloor  \frac {tp+tp_{start}}{T_{c}}\rfloor  +1 $, where is 1/Tc the sampling rate

- calculate EVMh_tp with $\Delta  \hat {t}$ set to $\lfloor  \frac {CP+tp_{start}}{T_{c}}\rfloor  -1 $, where 1/Tc is the sampling rate and the CP is the cyclic prefix of the symbol on which EVM is calculated(e.g. long CP for the first symbol of the slot) in seconds

A pictorial representation of the EVM measurement windows is given in Figure F.4-1.

![](media/image46.emf)

Figure F.4-1 EVM measruement window

# F.5 Window length

## F.5.1 Timing offset

As a result of using a cyclic prefix, there is a range of![](media_svg/image47.svg) [公式: δ^{~}t], which, at least in the case of perfect Tx signal quality, would give close to minimum error vector magnitude. As a first order approximation, that range should be equal to the length of the cyclic prefix. Any time domain windowing or FIR pulse shaping applied by the transmitter reduces the ![](media_svg/image48.svg) [公式: δ^{~}t] range within which the error vector is close to its minimum.

## F.5.2 Window length

The window length W affects the measured EVM and is expressed as a function of the configured cyclic prefix length. In the case where equalization is present, as with frequency domain EVM computation, the effect of FIR is reduced. This is because the equalization can correct most of the linear distortion introduced by the FIR. However, the time domain windowing effect can't be removed.

## F.5.3 Window length for normal CP

Tables F.5.3-1, F.5.3-2, and F.5.3-3 below specify the EVM window length (W) for normal CP.

Table F.5.3-1: EVM window length for normal CP for NR, FR1, 15 kHz SCS

| Channel Bandwidth (MHz) | FFT size | Cyclic prefix length for symbols 16 and 8-13 in FFT samples | EVM window length W | Ratio of W to total CP length for symbols 16 and 8-131 (%) |  |
| --- | --- | --- | --- | --- | --- |
| 3 | 256 | 18 | 9 | 50 |  |
| 5 | 512 | 36 | 18 | 50 |  |
| 7 | 512 | 36 | 18 | 50 |  |
| 10 | 1024 | 72 | 36 | 50 |  |
| 15 | 1536 | 108 | 54 | 50 |  |
| 20 | 2048 | 144 | 72 | 50 |  |
| 25 | 2048 | 144 | 72 | 50 |  |
| 30 | 3072 | 216 | 108 | 50 |  |
| 35 | 3072 | 216 | 108 | 50 |  |
| 40 | 4096 | 288 | 144 | 50 |  |
| 45 | 4096 | 288 | 144 | 50 |  |
| 50 | 4096 | 288 | 144 | 50 |  |
| NOTE 1: These percentages are informative and apply to a slot's symbols 1 to 6 and 8 to 13. Symbols 0 and 7 have a longer CP and therefore a lower percentage. |  |  |  |  |  |

Table F.5.3-2: EVM window length for normal CP for NR, FR1, 30 kHz SCS

| Channel Bandwidth (MHz) | FFT size | Cyclic prefix length for symbols 113 in FFT samples | EVM window length W | Ratio of W to total CP length for symbols 1131 (%) |
| --- | --- | --- | --- | --- |
| 5 | 256 | 18 | 9 | 50 |
| 10 | 512 | 36 | 18 | 50 |
| 15 | 768 | 54 | 27 | 50 |
| 20 | 1024 | 72 | 36 | 50 |
| 25 | 1024 | 72 | 36 | 50 |
| 30 | 1536 | 108 | 54 | 50 |
| 35 | 1536 | 108 | 54 | 50 |
| 40 | 2048 | 144 | 72 | 50 |
| 45 | 2048 | 144 | 72 | 50 |
| 50 | 2048 | 144 | 72 | 50 |
| 60 | 3072 | 216 | 108 | 50 |
| 70 | 3072 | 216 | 108 | 50 |
| 80 | 4096 | 288 | 144 | 50 |
| 90 | 4096 | 288 | 144 | 50 |
| 100 | 4096 | 288 | 144 | 50 |
| NOTE 1: These percentages are informative and apply to a slot's symbols 1 through 13. Symbol 0 has a longer CP and therefore a lower percentage. |  |  |  |  |

Table F.5.3-3: EVM window length for normal CP for NR (60 kHz SCS)

| Channel Bandwidth (MHz) | FFT size | Cyclic prefix length for symbols in FFT samples | EVM window length W | Ratio of W to total CP length 1 (%) |
| --- | --- | --- | --- | --- |
| 10 | 256 | 18 | 9 | 50 |
| 15 | 384 | 27 | 14 | 50 |
| 20 | 512 | 36 | 18 | 50 |
| 25 | 512 | 36 | 18 | 50 |
| 30 | 768 | 54 | 27 | 50 |
| 35 | 768 | 54 | 27 | 50 |
| 40 | 1024 | 72 | 36 | 50 |
| 45 | 1024 | 72 | 36 | 50 |
| 50 | 1024 | 72 | 36 | 50 |
| 60 | 1536 | 108 | 54 | 50 |
| 70 | 1536 | 108 | 54 | 50 |
| 80 | 2048 | 144 | 72 | 50 |
| 90 | 2048 | 144 | 72 | 50 |
| 100 | 2048 | 144 | 72 | 50 |
| NOTE 1: These percentages are informative and apply to all OFDM symbols within subframe except for symbol 0 of slot 0 and slot 2. Symbol 0 of slot 0 and slot 2 may have a longer CP and therefore a lower percentage. |  |  |  |  |

## F.5.4 Window length for Extended CP

Table F.5.4-1 below specifies the EVM window length (W) for extended CP. The number of CP samples excluded from the EVM window is the same as for normal CP length.

Table F.5.4-1: EVM window length for extended CP for NR, FR1, 60 kHz SCS

| Channel Bandwidth (MHz) | FFT size | Cyclic prefix length in FFT samples | EVM window length W | Ratio of W to total CP length1 (%) |
| --- | --- | --- | --- | --- |
| 10 | 256 | 64 | 54 | 84.4 |
| 15 | 384 | 96 | 80 | 83.3 |
| 20 | 512 | 128 | 106 | 82.8 |
| 25 | 512 | 128 | 110 | 85.9 |
| 30 | 768 | 192 | 164 | 85.4 |
| 35 | 768 | 192 | 164 | 85.4 |
| 40 | 1024 | 256 | 220 | 85.9 |
| 45 | 1024 | 256 | 220 | 85.9 |
| 50 | 1024 | 256 | 220 | 85.9 |
| 60 | 1536 | 384 | 330 | 85.9 |
| 70 | 1536 | 384 | 330 | 85.9 |
| 80 | 2048 | 512 | 440 | 85.9 |
| 90 | 2048 | 512 | 440 | 85.9 |
| 100 | 2048 | 512 | 440 | 85.9 |
| NOTE 1: These percentages are informative. |  |  |  |  |

## F.5.5 Window length for PRACH

The table below specifies the EVM window length for PRACH preamble formats for LRA= 839 and ![](media_svg/image49.svg) [公式: δf^{RA}⎰{1.25,5}kHz].

Table F.5.5-1 EVM window length for PRACH formats for  LRA= 839

| Preamble format | Cyclic prefix length NCP | Nominal FFT size1 | EVM window length W in FFT samples | Ratio of W to CP2 |
| --- | --- | --- | --- | --- |
| 0 | 3168 | 24576 | 2307 | 72.8% |
| 1 | 21024 | 24576 | 20163 | 95.9% |
| 2 | 4688 | 24576 | 3827 | 81.6% |
| 3 | 3168 | 6144 | 2952 | 93.2% |
| NOTE 1: The use of other FFT sizes is possible as long as appropriate scaling of the window length is appliedNOTE 2: These percentages are informative |  |  |  |  |

The table below specifies the EVM window length for PRACH preamble formats for LRA= 139 and ![](media_svg/image50.svg) [公式: δf^{RA}=15∪2^{Μ}kHz] where![](media_svg/image51.svg) [公式: Μ⎰{0,1,2}].

Table F.5.5-2 EVM window length for PRACH formats for LRA= 139

| Preamble format | Cyclic prefix length  NCP | Nominal FFT size1 | EVM window length W in FFT samples | Ratio of W to CP2 |
| --- | --- | --- | --- | --- |
| A1 | 2882- | 20482- | 1442- | 50.0% |
| A2 | 5762- | 20482- | 4322- | 75.0% |
| A3 | 8642- | 20482- | 7202- | 83.3% |
| B1 | 2162- | 20482- | 722- | 33.3% |
| B2 | 3602- | 20482- | 2162- | 60.0% |
| B3 | 5042- | 20482- | 3602- | 71.4% |
| B4 | 9362- | 20482- | 7922- | 84.6% |
| C0 | 12402- | 20482- | 10962- | 88.4% |
| C2 | 20482- | 20482- | 19042- | 93.0% |
| NOTE 1: The use of other FFT sizes is possible as long as appropriate scaling of the window length is appliedNOTE 2: These percentages are informative |  |  |  |  |

# F.6 Averaged EVM

The general EVM is averaged over basic EVM measurements for n slots in the time domain.

![](media_svg/image52.svg) [公式≈: EVM=^{1}_{n}_{⊆}_{i}_{=}^{n}_{1}EVM_{i}^{2}],

where n is

$$ n={10, for 15 kHz SCS\\20, for 30 kHz SCS\\40, for 60 kHz SCS $$

for PUCCH, PUSCH.

The EVM requirements shall be tested against the maximum of the RMS average at the window W extremities of the EVM measurements:

Thus ![](media_svg/image53.svg) [公式: EVMl] is calculated using ![](media_svg/image54.svg) [公式: δ^{~}t=δ^{~}t_{l}]in the expressions above and ![](media_svg/image55.svg) [公式: EVMh]is calculated using ![](media_svg/image56.svg) [公式: δ^{~}t=δ^{~}t_{h}].

Thus we get:

![](media_svg/image57.svg) [公式: EVM=max(EVMl,EVMh)]

The calculation of the EVM for the demodulation reference signal, ![](media_svg/image58.svg) [公式≈: ^{EVM}DMRS], follows the same procedure as calculating the general EVM, with the exception that the modulation symbol set ![](media_svg/image5.svg) [公式≈: ^{T}m] defined in clause F.2 is restricted to symbols containing uplink demodulation reference signals.

The basic ![](media_svg/image58.svg) [公式≈: ^{EVM}DMRS] measurements are first averaged over n slots in the time domain to obtain an intermediate average ![](media_svg/image59.svg) [公式: EVMDMRS].

$$\overline {EVM}_{DMRS}=\sqrt {\frac {1}{n}\sum  _{i=1}^{n}EVM_{DMRS,i}^{2}}$$

In the determination of each , the timing is set to ![](media_svg/image54.svg) [公式: δ^{~}t=δ^{~}t_{l}] if ![](media_svg/image61.svg) [公式: EVMl>EVMh], and it is set to ![](media_svg/image56.svg) [公式: δ^{~}t=δ^{~}t_{h}] otherwise, where ![](media_svg/image53.svg) [公式: EVMl] and ![](media_svg/image55.svg) [公式: EVMh] are the general average EVM values calculated in the same n slots over which the intermediate average ![](media_svg/image59.svg) [公式: EVMDMRS] is calculated. Note that in some cases, the general average EVM may be calculated only for the purpose of timing selection for the demodulation reference signal EVM.

Then the results are further averaged to get the EVM for the demodulation reference signal, ![](media_svg/image58.svg) [公式≈: ^{EVM}DMRS],

![](media_svg/image62.svg) [公式≈: EVM_{DMRS}=^{1}_{6}_{⊆}_{j}^{6}_{=}_{1}EVM^{2}DMRS,j]

The PRACH EVM, ![](media_svg/image63.svg) [公式≈: ^{EVM}PRACH], is averaged over 2 preamble sequence measurements for long preamble formats as defined in Table 6.3.3.1-1 in [6] and averaged over 10 preamble sequence measurements for short preamble formats as defined in Table 6.3.3.1-2 in [6].

The EVM requirements shall be tested against the maximum of the RMS average at the window W extremities of the EVM measurements:

Thus ![](media_svg/image64.svg) [公式: EVMPRACH,l] is calculated using ![](media_svg/image54.svg) [公式: δ^{~}t=δ^{~}t_{l}] and ![](media_svg/image65.svg) [公式: EVMPRACH,h]is calculated using ![](media_svg/image56.svg) [公式: δ^{~}t=δ^{~}t_{h}].

Thus we get:

![](media_svg/image66.svg) [公式≈: EVM_{PRACH}=max(EVMPRACH,l,EVMPRACH,h)]

# F.7 Spectrum Flatness

The data shall be taken from FFT coded data symbols and the demodulation reference symbols of the allocated resource block.

# F.8 EVM measurement for multiple Tx

For UE with multiple transmission antennas, if UE indicates Tx diversity capability, EVM is measured at each antenna connector to get EVMi, and the total EVM is calculated by values of EVMi with weighting factor of linear power at each antenna connector.

$ EVM=\frac {\sum  _{i=1}^{k}P_{i}*EVM_{i}}{\sum  _{i=1}^{k}P_{i}}$

where k=2, 4, and Pi denotes the linear power measured at each antenna connector respectively.

# F.9 Phase offset measurement for DMRS bundling

## F.9.1 Measurement point

The measurement point for phase offset measurement is defined in Figure F.9.1-1.

![](media/image67.emf)

Figure F.9.1-1: Measurement point for phase offset for DMRS bundling

## F.9.2 Symbols used

Phase offset is determined based on DMRS REs (3 DMRS symbols per slot) with the option to use data symbols.

## F.9.3 Modified test signal

Same as described in Annex F.4.

## F.9.4 Phase offset measurement

The phase offset measurement is based on the phase response of the Tx chain ![](media_svg/image31.svg) [公式: ϑ^{~}(t,f)] as derived based on Annex F.4.

The subcarrier at the carrier leakage frequency of the transmitted signal shall be excluded from the measured subcarriers.

The phase difference $∆\hat {\varphi  }\left ( f\right ) $ for each measured subcarrier between a reference timeslot tref and the measurement timeslot tm is then calculated as defined below.

$∆\hat {\varphi  }\left ( f\right ) =\hat {\varphi  }\left ( t_{m},f\right ) -\hat {\varphi  }(t_{ref},f)$

The phase offset between the reference and measurement timeslots are then calculated as the maximum over the results for all measured subcarriers as shown below:

$ PhaseOffset=\operatorname {max_{f}}\left ((\left | ∆\hat {\varphi  }\left ( f\right ) \right | )\right )$

# F.10 EVM for UL MIMO

## F10.1 General

EVM for UL MIMO is measured per layer. A zero-forcing (ZF) MIMO receiver architecture is used so that dual layer or 4-layer transmissions by the UE can be demodulated by the test equipment receiver.

![](media/X:\PROJECT\CMW\DEVELOP\USER\1CM5\KRAKOWSK\NR\NR_EVM_2L_UL_MIMO.png)

Figure F.10.1-1: EVM calculation block diagram for 2-Layer UL MIMO

![](media/D:\NR_MIMO_EVM_4x4 (1).jpg)

Figure F.10.1-2: EVM calculation block diagram for 4-Layer UL MIMO

The TE receives signals from 2 or 4 different ports which are connected to two or four antenna connectors in the test system.

For UL MIMO measurements a MIMO equalization step as described in section F.10.2 is performed to separate the layers.

Each layer is then processed as described in section F.10.3 to receive the measurement results for each individual layer.

## F10.2 MIMO Equalization

The MIMO equalization is based only on reference signals (DMRS) without using any data symbols. For the equalization process all available DMRS symbols shall be used.

The effective 2x2 or 4x4 channel matrix is estimated using reference signals of different subcarriers, e.g. in case of DMRS antenna ports 0 and 2. In case that same subcarriers are used, e.g. DMRS antenna ports 0 and 1, a channel decomposition is necessary taking advantage of the orthogonal codes wf and wt and assuming identical channel coefficients for adjacent subcarriers of same CDM group.

Effective channel including the precoding matrix P is:

$\hat {H}=HP=\left [ \begin {matrix}\hat {h}_{0,0} & \hat {h}_{0,1} \\ \hat {h}_{1,0} & \hat {h}_{1,1}\end {matrix}\right ] $ for 2-Layer UL MIMO, or  $\hat {H}=HP=\left [ \begin {matrix}\begin {matrix}\hat {h}_{0,0} & \hat {h}_{0,1} \\ \hat {h}_{1,0} & \hat {h}_{1,1}\end {matrix} & \begin {matrix}\hat {h}_{0,2} & \hat {h}_{0,3} \\ \hat {h}_{1,2} & \hat {h}_{1,3}\end {matrix} \\ \begin {matrix}\hat {h}_{2,0} & \hat {h}_{2,1} \\ \hat {h}_{3,0} & \hat {h}_{3,1}\end {matrix} & \begin {matrix}\hat {h}_{2,2} & \hat {h}_{2,3} \\ \hat {h}_{3,2} & \hat {h}_{3,3}\end {matrix}\end {matrix}\right ] $ for 4-Layer UL MIMO,

with

$$\hat {h}_{n,\nu  }=\frac {y_{n}r_{\nu  }^{*}}{|r_{\nu  }|^{2}}$$

where y denotes the received symbol on port index n and r the reference signal for layer index ν.

Since reference signals of a specific layer are transmitted only on subcarriers of one CDM group channel, interpolation is needed in order to obtain channel coefficients for all subcarriers. Channel interpolation is done using the channel coefficients of active CDM group in all other CDM groups.

The channel coefficients used to calculate the equalizer coefficients are obtained after channel smoothing in frequency domain by computing the moving average of interpolated channel coefficients. The moving average window size is 7. For subcarriers at or near the edge of allocation the window size is reduced accordingly.

The ZF equalizer coefficients are calculated as the inverse of the effective channel matrix, in general:

$$ G_{ZF}=\hat {H}^{-1}$$

## F10.3 Layer processing

After performing the MIMO equalization as described in section F.10.2 each layer is processed using the existing procedure as defined in Annex E of TS 38.521-1 [4].

Since the channel estimation is calculated only on the DMRS symbols, an averaging including all 14 symbols of one slot, i.e. data and reference signals, is needed in order to minimize EVM. The averaging is achieved by the least square (LS) equalization method described for single layer in Annex E.3. of TS 38.521-1 [4].

MS(f,t) and NS(f,t) are processed with a LS estimator, to derive one equalizer coefficient per time slot and per allocated subcarrier. EC(f) is defined for each layer as:

$$ EC_{\nu  }(f)=\frac {\sum  _{t=0}^{13}NS_{\nu  }(f,t)^{*}NS_{\nu  }(f,t)}{\sum  _{t=0}^{13}MS_{\nu  }(f,t)^{*}NS_{\nu  }(f,t)}$$

With * denoting complex conjugation. EC(f) are used to equalize layer data symbols.

EVM equalizer spectral flatness is derived from equalizer coefficients for each layer as follows:

$ c_{\nu  }=\left | EC_{\nu  }(f)\right | \sqrt {\left | g_{\nu  ,0}\right | ^{2}+\left | g_{\nu  ,1}\right | ^{2}}$ for 2-Layer UL MIMO, or $ c_{\nu  }=\left | EC_{\nu  }(f)\right | \sqrt {\left | g_{\nu  ,0}\right | ^{2}+\left | g_{\nu  ,1}\right | ^{2}+\left | g_{\nu  ,2}\right | ^{2}+\left | g_{\nu  ,3}\right | ^{2}}$ for 4-Layer UL MIMO,

###### Annex G (normative): 
Difference of relative phase and power errors

# G.0 General

This annex gives further information needed for understanding and implementing 6.4D.4. The following terms should be understood as follows:

Relative phase error: refers to the phase difference between signals at different antenna connectors, which should be ideally 0. It should be understood as for a slot i.e. (slot) relative phase. It is calculated based on DMRS symbols of that slot or on SRS symbols.

Difference of relative phase error: refers to the difference between the relative phase error determined per slot and the relative phase error determined based on the SRS transmitted.

# G.1 Measurement Point

Figure G.1-1 shows the measurement point for the difference of relative phase and power errors.

![](media/image70.emf)

Figure G.1-1 - Measurement point for difference of relative phase/power error for UL coherent MIMO

# G.2 Relative Phase Error Measurement

Here are listed the different aspects that may lead to different interpretations.

## G.2.1 Symbols and subcarriers used

Phase error is determined based on DMRS REs (DMRS mapping type A with 3 DMRS symbols per slot, the REs corresponding to the odd subcarriers and DMRS symbols are non-allocated for data or DMRS.) and SRS REs (with 4 SRS symbols in the SRS slot, same SRS resource mapping is used for non-codebook-based and codebook-based precoding).

For the DMRS and SRS to occupy identical SCs and maximize their frequency density, DMRS configuration type 1 and SRS comb2 configuration are used.

UL RMC described in Annex A.2 is used.

## G.2.2 CFO (carrier frequency offset) correction

The TE performs a CFO correction on a slot-by-slot basis using a common frequency correction at the two uplink antenna connectors.

## G.2.3 Steps of the measurement method

Below are detailed the steps necessary to obtain the maximum difference of relative phase error during the 20ms time window.

## 1 Determination for each subcarrier and at each antenna, the SRS relative phase error based on the last SRS transmitted on Ant1 and Ant2, that relative phase error serves as a reference for the calculation of the difference of relative phase error for each slot inside the 20 ms time window.

The output is the “SRS relative phase error” vector for the last SRS transmitted: $\left [ 1\times  number\_of\_subcarriers\right ] $.

## 2 Calculation for the last SRS transmitted, for each RB of the SRS relative phase errors based on the arithmetic mean of the subcarrier SRS relative phase errors determined in previous step.

The output is the “SRS relative phase error” vector for the last SRS transmitted: $\left [ 1\times  number\_of\_RBs\right ] $.

## 3 CFO correction on slot-by-slot basis using a common frequency correction for both antenna outputs.

## 4 Determination for each subcarrier and at each antenna, the phase over the slot being analyzed. The phase is extracted from the channel estimate derived from the 3 DMRS symbols of the slot using the LSE technique.

The output is one vector of dimension $\left [ 1\times  number\_of\_subcarriers\right ] $ for each antenna.

## 5 Calculation for a slot for each subcarrier of the relative phase error (difference between the vectors determined in the previous step).

The output is subcarrier relative phase errors of a slot: $\left [ 1\times  number\_of\_subcarriers\right ] $.

## 6 Calculation for a slot, for each RB of the relative phase errors based on the arithmetic mean of the subcarrier relative phase errors determined in previous step.

The output is a “slot relative phase error” vector for a slot:$\left [ 1\times  number\_of\_RBs\right ] $.

## 7 Calculation for a slot of the difference of relative phase errors based on the “SRS relative phase error” (reference) determined in step 2 and the “slot relative phase error” determined in previous step.

The output is a “difference of relative phase error” vector for a slot:$\left [ 1\times  number\_of\_RBs\right ] $.

## 8 Calculation for a slot of the arithmetic mean value of the “difference of relative phase error” vector determined in previous step, this value corresponds to an RB.

The output is a “difference of relative phase error” value for a slot: $\left [ 1\times  1\right ] .$

## 9 Perform for each slot of the 20ms time window, steps 3 to 8.

The output is a “difference of relative phase error” vector: $\left [ 1\times  number\_of\_slots\right ] $.

## 10 Calculation of the maximum value of the “difference of relative phase error”.

The output is the “difference of relative phase error” that should be verified as complying with the 40° maximum allowable difference of relative phase error requirement: $\left [ 1\times  1\right ] $.

###### Annex H (informative):
Void

###### Annex I (informative):
Void

###### Annex J (informative):
Void

###### Annex K (informative):
Void

###### Annex L (normative):
ModifiedMPR-Behavior

# L.1 Indication of modified MPR behavior

This annex contains the definitions of the bits in the field modifiedMPR-Behaviour indicated per supported NR band in the IE RF-Parameters [7] by a UE supporting an MPR or A-MPR modified in a given version of this specification. A modified MPR or A-MPR behaviour can apply to a supported NR band in stand-alone operation (including CA and NN-DC operation) or in non-standalone operation with the said NR band as part of an EN-DC or NE-DC band combination.

NOTE 1: In the present release, the modifiedMPR-Behaviour is indicated [7] by an 8-bit bitmap per supported NR band.

Table L.1-1: Definitions of the bits in the field modifiedMPR-Behaviour

| NR Band | Index of field(bit number) | Definition(description of the supported functionality if indicator set to one) | Notes |
| --- | --- | --- | --- |
| n1 | 0 (leftmost bit) | Requirements for network signalling values NS_05 and NS_05U as defined in Clause 6.5.3.3.4 of 38.101-1 v19.3.0 and the A-MPR as defined in clause 6.2.3.4 of 38.101-1 v19.3.0 | - This bit shall be set to 1 by a UE supporting this version of the specification. |
| n5 | 0 (leftmost bit) | Additional requirements for network signalling values NS_14 and NS_15 as defined in the respective Clause 6.5.3.3.19 and Clause 6.5.3.3.20 of 38.101-1 v19.2.0. | This bit shall be set to 1 by a UE supporting Power Class 2 as indicated by ue-PowerClass in BandNR. This bit may be set to 1 by a UE supporting Power Class 3 as indicated by ue-PowerClass in BandNR. |
| n30 | 0 (leftmost bit) | Requirements for network signalling value NS_21 as defined in Clause 6.5.2.3.9 of 38.101-1 v17.6.0 and A-MPR as defined in Clause 6.2.3.14 of 38.101-1 v17.6.0. | This bit shall be set to 1 by a UE supporting this release of the specification. |
| n34 | 0 (leftmost bit) | PC 1.5 MPR as defined in Table 6.2D.2-3 | This bit may be set to 1 by a UE of any release supporting power class 1.5. This bit is intended to be set by larger form factor FWA devices. If the bit is not set for a Rel-17 and later UE, PC 1.5 MPR as defined in Table 6.2D.2-2  applies. If the bit is not set for a Rel-16 and earlier UE, MPR in Table 6.2.2-4 of 38.101-1 v16.5.0 applies. |
| n39 | 0 (leftmost bit) | PC 1.5 MPR as defined in Table 6.2D.2-3 | This bit may be set to 1 by a UE of any release supporting power class 1.5. This bit is intended to be set by larger form factor FWA devices. If the bit is not set for a Rel-17 and later UE, PC 1.5 MPR as defined in Table 6.2D.2-2  applies. If the bit is not set for a Rel-16 and earlier UE, MPR in Table 6.2.2-4 of 38.101-1 v16.5.0 applies. |
| n40 | 0 (leftmost bit) | PC 1.5 MPR as defined in Table 6.2D.2-3 | This bit may be set to 1 by a UE of any release supporting power class 1.5. This bit is intended to be set by larger form factor FWA devices. If the bit is not set for a Rel-17 and later UE, PC 1.5 MPR as defined in Table 6.2D.2-2  applies. If the bit is not set for a Rel-16 and earlier UE, MPR in Table 6.2.2-4 of 38.101-1 v16.5.0 applies. |
| n41 | 0 (leftmost bit) | EN-DC contiguous intraband MPR as defined in clause 6.2B.2.1 of 38.101-3 v15.5.0 | - This bit shall be set to 1 by a UE supporting DC_(n)41AA UE EN-DC |
|  | 1 | EN-DC non-contiguous intraband MPR as defined in clause 6.2B.2.2 of 38.101-3 v15.5.0 | - This bit shall be set to 1 by a UE supporting DC_41A_n41A EN-DC |
|  | 2 | EN-DC contiguous and non-contiguous intraband A-MPR as defined in 38.101-3 v16.4.0. If this bit is not set the UE uses Rel-15 A-MPR for EN-DC contiguous and non-contiguous intraband A-MPR | -This bit may be set to 1 by a UE supporting DC_(n)41AA or DC_41A_n41A EN-DC |
|  | 3 | PC 1.5 MPR as defined in Table 6.2D.2-3 | This bit may be set to 1 by a UE of any release supporting power class 1.5. This bit is intended to be set by larger form factor FWA devices. If the bit is not set for a Rel-17 and later UE, PC 1.5 MPR as defined in Table 6.2D.2-2 applies. If the bit is not set for a Rel-16 and earlier UE, MPR in Table 6.2.2-4 of 38.101-1 v16.5.0 applies. |
| n71 | 0 (leftmost bit) | EN-DC contiguous intraband MPR as defined in clause 6.2B.2.1 of 38.101-3 v15.5.0 | - This bit shall be set to 1 by a UE supporting DC_(n)71AA UE EN-DC |
| n77 | 0 (leftmost bit) | PC 1.5 MPR as defined in Table 6.2D.2-3 | This bit may be set to 1 by a UE of any release supporting power class 1.5. This bit is intended to be set by larger form factor FWA devices. If the bit is not set for a Rel-17 and later UE, PC 1.5 MPR as defined in Table 6.2D.2-2 applies. If the bit is not set for a Rel-16 and earlier UE, MPR in Table 6.2.2-4 of 38.101-1 v16.5.0 applies. |
| n78 | 0 (leftmost bit) | PC 1.5 MPR as defined in Table 6.2D.2-3 | This bit may be set to 1 by a UE of any release supporting power class 1.5. This bit is intended to be set by larger form factor FWA devices. If the bit is not set for a Rel-17 and later UE, PC 1.5 MPR as defined in Table 6.2D.2-2. If the bit is not set for a Rel-16 and earlier UE, MPR in Table 6.2.2-4 of 38.101-1 v16.5.0 applies. |
| n79 | 0 (leftmost bit) | PC 1.5 MPR as defined in Table 6.2D.2-3 | This bit may be set to 1 by a UE of any release supporting power class 1.5. This bit is intended to be set by larger form factor FWA devices. If the bit is not set for a Rel-17 and later UE, PC 1.5 MPR as defined in Table 6.2D.2-2  applies. If the bit is not set for a Rel-16 and earlier UE, MPR in Table 6.2.2-4 of 38.101-1 v16.5.0 applies. |
| n96 | 0 (leftmost bit) | Support of all band n96 network signalling labels as defined in Table 6.2F.3.1-1 of 38.101-1 Rel-17 | This bit may be set to 1 by a Rel-16 UE to indicate support of all network signalling labels for n96 as defined in Table 6.2F.3.1-1 of 38.101-1 Rel-17 |
|  | 1 | Support of all band n96 network signalling labels as defined in Table 6.2F.3.1-1 of 38.101-1 Rel-18 | This bit may be set to 1 by a Rel-16 and Rel-17 UE to indicate support of all network signalling labels for n96 as defined in Table 6.2F.3.1-1 of 38.101-1 Rel-18 |
| n102 | 0 (leftmost bit) | Support of all band n102 network signalling labels as defined in Table 6.2F.3.1-1 of 38.101-1 Rel-17 | This bit may be set to 1 by a Rel-16 UE to indicate support of all network signalling labels for n102 as defined in Table 6.2F.3.1-1 of 38.101-1 Rel-17 |
|  | 1 | Support of all band n102 network signalling labels as defined in Table 6.2F.3.1-1 of 38.101-1 Rel-18 | This bit may be set to 1 by a Rel-16 and Rel-17 UE to indicate support of all network signalling labels for n102 as defined in Table 6.2F.3.1-1 of 38.101-1 Rel-18 |
| n104 | 0 (leftmost bit) | PC 1.5 MPR as defined in Table 6.2D.2-3 | This bit may be set to 1 by a UE of any release supporting power class 1.5. This bit is intended to be set by larger form factor FWA devices. If the bit is not set for a Rel-17 and later UE, PC 1.5 MPR as defined in Table 6.2D.2-2  applies. If the bit is not set for a Rel-16 and earlier UE, MPR in Table 6.2.2-4 of 38.101-1 v16.5.0 applies. |

###### Annex M (normative): 
Declared Supported Post Antenna Gain for UE


# M.1 FRMCS operating bands

Due to large form factor of the FRMCS (Future Railway Mobile Communication System) rooftop mounted cab-radio unit, UE in bands n100 and n101 can have external antenna placed far away from the chipset unit. In this case, the effective antenna gain is a UE specific condition. This effective antenna gain includes the feeding loss of all components after the chipset unit antenna connector and the peak directional gain of the external antenna and hence will be called the post chipset unit antenna connector gain Gn100post connector and Gn101post connector for band n100 and n101, respectively. Note that 3GPP specifications mandate cab-radio UE manufacturer declaration of the post chipset unit antenna connector gains Gn100post connector and Gn101post connector.

If no external antenna is used, the value of 0dBi will be applied. If an external antenna is used, the cab-radio UE PEIRP shall be computed as the summation in dB of the cab-radio UE maximum conducted output power specified in Table 6.2.1-1 and the declared Gn100post connector or Gn101post connector in dB. If the resulting cab-radio UE PEIRP is larger  than 33 dBm, the transmitter conducted requirements shall be scaled by subtracting the difference in dB between the UE PEIRP and 33 dBm from the transmitter conducted requirements. If the resulting cab-radio UE PEIRP is less than or equal to 33 dBm, no additional scaling of conducted requirements is needed.

The applicable regional requirements for bands n100 and n101 in PEIRP shall be converted to conducted requirements by subtracting Gn100post connector or Gn101post connector as:

PConducted = PEIRP - Gn100post connector for band n100, and

PConducted = PEIRP - G101post connector for band n101.

###### Annex N (informative):
Change history


| Change history |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Date | Meeting | TDoc | CR | Rev | Cat | Subject/Comment | New version |  |
| 2017-08 | RAN4#84 | R4-1708909 |  |  |  | Initial Skeleton | 0.0.1 |  |
| 2017-10 | RAN4#84Bis | R4-1709958 |  |  |  | Added approved TPs in RAN4-NR-AH#3R4-1709948, TP for TS 38.101-1: minimum output power, HuaweiR4-1709454, TP for TS 38.101-1:UE Tx spurious emission for range 1, ZTE Corporation | 0.1.0 |  |
| 2017-10 | RAN4#84Bis | R4-1711978 |  |  |  | Embedded approved TPs in RAN4#84BisR4-1711556, "TP to TS 38.101: Draft CR to Transmitter power clause", NokiaR4-1710962, "TP to TS 38.101-1: Draft CR to Output RF spectrum emissions" NokiaR4-1711608, "TP for TS38.101-1 on conducted UE transmitter intermodulation for FR1(section 6.5)" ZTE CorporationNumber of TPs by editors | 0.2.0 |  |
| 2017-12 | RAN4#85 | R4-1713805 |  |  |  | Approved TPs in RAN4#85R4-1713204, TP on general parts for 38.101-1 NR FR1, EricssonR4-1714047, WF on MPR for sub6GHz, NTT DOCOMO, INC.R4-1714052, TP for TS 38.101-1 introduction of band n71 for transmitter characteristics, T-Mobile USA Inc.R4-1714162, TP to 38.101-1: ACS, EricssonR4-1714163, TP to 36.101-1: In-band blocking, EricssonR4-1714446, TP to 36.101-1: Out-of-band blocking and exceptions for spurious response, EricssonR4-1714369, TP for NBB requirement for FR1, Intel CorporationR4-1714529, TP on introducing operating bands for NR-LTE DC including SUL band combinations in 38.101-1, HuaweiR4-1714097, TP for TS 38.101-1: UE RF requirements for standalone SUL, HuaweiR4-1714536, TP for TS 38.101-1: Channel Bandwidth Definition, Qualcomm Incorporated (Note, this TP was further discussed and edited in the reflector)R4-1714114, TP for TS 38.101-1: Channel Arrangement, Qualcomm Incorporated (Note, this TP was further discussed and edited in the reflector)R4-1714029, Sub6 Reference Sensitivity, Qualcomm IncorporatedR4-1714329, TP to TR 38.101-01 v0.2.0: ON/OFF mask design for NR UE transmissions for FR1, EricssonBand list according to R4-1714542, List of bands and band combinations to be introduced into RAN4 NR core requirements by December 2017, RAN4 ChairmenInput from:R4-1714479, TP for TR 38.817-01 NR channel bandwidth, Huawei, HiSilicon | 0.3.0 |  |
| 2017-12 | RAN4#85 | R4-1714569 |  |  |  | Further corrections and alignments with 38.104 after email review | 0.4.0 |  |
| 2017-12 | RAN#78 | RP-172475 |  |  |  | v1.0.0 submitted for plenary approval. Contents same as 0.4.0 | 1.0.0 |  |
| 2017-12 | RAN#78 |  |  |  |  | Approved by plenary – Rel-15 spec under change control | 15.0.0 |  |
| 2018-03 | RAN#79 | RP-180264 | 0003 |  | F | Implementation of endorced CRs to 38.101-1Endorsed draft CRsF: R4-1800400, Editorial corrections for 38.101-1, QualcommB: R4-1801102, Draft CR for 30 MHz CBW support, HuaweiF: R4-1800032, 38.101-1 n71 draft CR for section 6.2.3 - UE A-MPR - NS values, T-Mobile USA Inc.B: R4-1801121, Draft pCR for TS 38.101-1 version 15.0.0: Remaining ON/OFF masks for FR1 NR UE transmissions, EricssonF: R4-1800417, Correction of NR SEM table and additional requirements table, vivoF: R4-1800033, 38.101-1 n71 draft CR for section 6.5.3.2 Spurious emissions for UE co-existence, T-Mobile USA Inc.F: R4-1801114, Proposal on protected band numbering in UE specs, Sprint CorporationF: R4-1800407, Draft CR for TS 38.101-1: Mandatory 4Rx antenna performance for NR UE, Vodafone Group PlcF: R4-1800451 Draft CR for TS 38.101-1: Clarification of 4Rx NR bands, Huawei, HiSiliconF: R4-1801136, Draft CR for TS 38.101-1: REFSENS for NR bands, Huawei, HiSiliconF: R4-1801137, Draft CR: n71 REFSENS, Dish NetworkF: R4-1800395, Draft CR to 38.101-1: corrections to ACS and in-band blocking, EricssonF: R4-1800396, Draft CR to 38.101-1: corrections to out-of-band blocking, EricssonF: R4-1800397, Draft CR to 38.101-1: corrections to spurious response, EricssonF: R4-1800305, Draft CR for NR FR1 wide band intermodulation requirements, MediaTek Inc.F: R4-1800320, Draft CR to 38.101-1: Rx Spurious emission for NR FR1 (section 7.9), ZTE CorporationF: R4-1800473, Draft CR on UE RF requirements for SUL in TS 38.101-1, HuaweiF: R4-1800965, Draft CR to TS 38.101-1: Asymmetric CH BW operation, Dish NetworkF: R4-1800882, Draft CR for correction of UE channel bandwidth for Bands n77 and n78 for TS 38.101-1, Orange UKF: R4-1801012, Draft CR to 38.101-1: Clarifications to UE spectrum utilization section 5.3, EricssonF: R4-1800030, 38.101-1 n71 draft CR for section 5.4.4 - TX–RX frequency separation, T-Mobile USA IncF: R4-1801228, Draft CR to 38.101-1: Channel spacing for CA for NR FR1(section 5.4.1.2), ZTE CorporationF: R4-1801231, Correction CR for channel spacing:38.101-1, SamsungF: R4-1801235, Draft CR to TS 38.101-1: Corrections on channel raster calculation in section 5.4.2, ZTE CorporationF: R4-1801318, Draft CR on synchronization raster, HuaweiRAN4#86:R4-1803053, Draft CR for new spec structure of 38.101-1, EricssonR4-1801479, Draft CR to 38.101-1: Default Tx-RX frequency separation for NR FR1(section 5.4.4), ZTER4-1801581, Draft CR for TS 38.101-1 update of 4Rx bands, Huawei Technologies FranceR4-1802211, draft CR TS 38.101-1 Uplink configuration for FR1 NR REFSENS, Skyworks Solutions Inc.R4-1802342, Draft CR for NR FR1 ACS case 2 transmitter power setting correction (Note 1), MediaTek Inc.R4-1802509, Draft CR on 38.101-1 v15.0.0: Remaining ON/OFF masks for FR1 NR UE transmissions, EricssonR4-1802566, Draft CR to TS 38.101-1: Clarification of mixed numerology guardband size, EricssonR4-1802978, Draft CR to TS 38.101-1: Corrections on channel raster in Section 5.4.2.3, Intel CorporationR4-1803064, Draft CR for 38.101-1: Correction of errors, Sprint CorporationR4-1803065, Draft CR for 38.101-1 Introduction of n41requirements, Sprint CorporationR4-1803242, Draft CR to 38.101-1: Corrections to n66, Dish NetworkR4-1803285, Draft CR to 38.101-1: Correction to CH BWs without symmetric uplink Dish Network, Skyworks Solutions Inc.R4-1803436, Introduction of UL subcarrier alignment for additional bands, AT&TR4-1803456, Draft CR for 38.101-1: Spurious Emissions for UE Coexistence, Sprint CorporationR4-1803461, CR on configured transmitted power for TS 38.101-1, HuaweiR4-1803452, draft CR for introduction of completed band combinations from 37.865-01-01 into 38.101-1, EricssonR4-1803567, Draft CR for TS 38.101-1: Sync raster offset in re-farming bands (5.4.3), EricssonR4-1803365, CR to introduce MPR for PC2 and PC3 and A-MPR for UTRA protection, Nokia | 15.1.0 |  |
| 2018-06 | RAN#80 | RP-181262 | 0011 |  | F | CR to TS 38.101-1: Implementation of endorsed draft CRs from RAN4 #86bis and RAN4 #87R4-1803900, Draft CR into TS 38.101-1 Introduction of band combinations for SUL, HuaweiR4-1804021 CR for clarifications for NR FR1 CA BW Classes Nokia, Nokia Shanghai BellR4-1804140 CR for Narrow Band Blocking requirement for FR1 Intel CorporationR4-1804219 Draft CR for 38.101-1: n41 SEM and additional spurious emissions SPRINT CorporationR4-1804266 Draft CR to 38.101-1 MPR channel bandwidth criteria Skyworks Solutions Inc.R4-1804267 Draft CR to 38.101-1 n3,n5,n8 REFSENS levels Skyworks Solutions Inc.R4-1804268 Draft CR to 38.101-1: Corrrection to n41 uplink configuration for reference sensitivity Skyworks Solutions Inc.R4-1804370 Draft CR to add missing NR inter-band DL CA in FR1 for TS 38.101-1 NTT DOCOMO, INC.R4-1804581 Draft CR to 38.101-1: On EVM Wording Qualcomm, Inc.R4-1804948 Corrections to 5.3.3 in TS 38.101-1 Nokia, Nokia Shanghai BellR4-1804877 draft CR introduction completed band combinations 37.865-01-01 -> 38.101-1 EricssonR4-1805444 Draft CR to TS 38.101-1: Asymmetric CH BW operation Dish NetworkR4-1805447 drfat CR for including SRS antenna switching in configured output power Qualcomm IncorporatedR4-1805462 Editorial corrections to UE RF requirements in 38.101-1 Qualcomm IncorporatedR4-1805659 Draft CR for CBW for n50 for 38.101-1 HuaweiR4-1805664 Draft CR to 38.101-1: Addition of Annex F Rohde & SchwarzR4-1805665 Correction to inner and outer definitions for MPR Qualcomm IncorporatedR4-1805684 Draft CR to TS38.101-1: Channel Raster to Resource Element Mapping (Section 5.4.2.2) and RB alignment with different numerologies (Section 5.3.4) ZTE CorporationR4-1805698 Draft CR for 38.101-1 for Rx(Ch7) of Band n77, n78 and n79 RF requirements CMCCR4-1805699 Draft CR to 38.101-1:introduction of  Tx/Rx requirements for inter-band CA ZTE CorporationR4-1805751 Draft CR on UE-to-UE coexistence requirements to protect band 29 from NR band 71 LG Electronics FranceR4-1805783 Draft CR for 38.101-1 for Tx(Ch6) of Band n77, n78 and n79 RF requirements CMCCR4-1805902 Draft CR into TS 38.101-1 Correction on SUL_n78-n80 Huawei, HiSiliconR4-1805904 Draft CR into TS 38.101-1 Introduction of new band combinations for SUL Huawei, HiSiliconR4-1805921 Draft CR on NR UE REFSENS SNR FRC for FR1 Intel CorporationR4-1805981 Draft CR for  TS38.101-1:Sync raster SamsungR4-1804548 Draft CR for CA BW class for FR1 NTT DOCOMO, INC.R4-1806170     Draft CR on frequency error for TS 38.101-1 ZTE CorporationR4-1806481     Draft CR for Environmental conditions in TS 38.101-1 Annex NTT DOCOMO, INC.R4-1806657     Draft CR to 38.101-1: Measurement BW for min and off power  Skyworks Solutions Inc.R4-1806669     Draft CR to TS38.101-1_introduction of completed band combinations for inter-band 2UL CA  ZTE CorporationR4-1806673     Draft CR to TS38.101-1_Remove brackets from Tx and Rx spurious emission table ZTE CorporationR4-1806677     Draft CR on including CA bandwidth class and band combinations for intra-band CA  LG Electronics FranceR4-1806719      Introduction of 7.5 kHz frequency shift for Band n71 Ericsson, T-MobileR4-1806844      Draft CR for 38.101-1 for Tx(Ch6): missing maximum power requirements for n1 and n8 SoftBank Corp.R4-1806945      Draft CR for TS 38.101-1: Channel raster and NR-ARFCN clarification (5.4.2) EricssonR4-1807039      Intra-band CA terminology for UE  ZTE CorporationR4-1807178      Corrections to n70 TX/RX frequency separation Dish NetworkR4-1807181      Corrections to spurious emissions UE co-existence table Dish NetworkR4-1807234      Draft CR into TS 38.101-1 Some Corrections for SUL  Huawei, HiSiliconR4-1807269      Corrections to Wide band intermodulation table <2700MHz Dish NetworkR4-1807392       to remove the brackets for SU in 38.101-1  Huawei, HiSiliconR4-1807647       Draft CR to TS 38.101-1: Correction to Asymmetric CH BW operation    Dish NetworkR4-1807680       Draft CR on 38.101-1 on channel raster to achieve alignment of data and SSB subcarrier grids    Nokia, Nokia Shanghai Bell, EricssonR4-1807705        CR for TS 38.101-1 A-MPR for n51   Huawei, HisiliconR4-1807814        Draft CR for 38.101-1: SEM correction for n41   Sprint CorporationR4-1807851        Draft CR for 38.101-1: UE spurious emission protection requirements for n5     Sprint CorporationR4-1807920        General requirements for downlink inter-band CA   Qualcomm IncorporatedR4-1807923        Resolution bandwidth for ACLR   Qualcomm IncorporatedR4-1808084          Introduction of n12 into TS 38.101-1      NokiaR4-1808087         Draft CR 38.101-1: Introduction of n2, n25, n66 and n70    Sprint Corporation, DishnetworkR4-1808090         Draft CR to TS 38.101-1: Inclusion of Simultaneous RxTx UE capability for some band combinations   Ericsson, Vodafone, OrangeR4-1808107             Draft CR to TS38.101-1_corrections on UE coexistence   ZTE CorporationR4-1808111         TP to TS38.101-1 - UE ON/OFF masks    EricssonR4-1808116            Draft CR to 38.101-1: introduction of Band n34,n39 and n40 RF requirements     ZTE Corporation,CMCCR4-1808136          Draft CR to 38.101-1: FR1 UE Power Control    Qualcomm IncorporatedR4-1808141          Correction to MPR for PC2 and spectrum emission mask measurement bandwidth      Qualcomm IncorporatedR4-1808142          Draft CR for 38.101-1 n41 A-MPR     Sprint Corporation, Nokia, Nokia Shanghai Bell, EricssonR4-1808143           Draft CR for TS 38.101-1 A-MPR for n20    Huawei, HiSiliconR4-1808155          Draft CR for TS 38.101-1: to correct reqirements for n71    SamsungR4-1808178         Addition parameters about n50 & n51 in TS 38.101-1   Huawei, Hisilicon, Etisalat (editors note: n50 not implemented per chairmans aggreement)R4-1808182         Draft CR for TS 38.101-1 A-MPR for n28    Huawei, HiSiliconR4-1808187         CR for RF requirements for Coherent UL MIMO for FR1          Qualcomm Austria RFFE GmbHR4-1808207         Draft CR to 38.101-1: On EVM Averaging Length, Wording  , QualcommR4-1808209         Draft CR for 38.101-1 for Tx (Ch6) of HPUE       QualcommR4-1808466         Draft CR on UL RMC and OCNG pattern for FDD REFSENS tests    RD sessionR4-1808493           Draft CR for TS 38.101-1: Channel and sync raster corrections (5.4)       EricssonR4-1808507          Draft CR for TS38.101-1 on addition of new 90MHz UE CBW for n41/n78      LG Electronics Inc., LG Uplus, SamsungR4-1808176, Draft CR for 38.101-1 : Introduction of A-MPR for n8, SoftBankR4-1808201, Draft CR for 38.101-1 : Introduction of A-MPR for n1, SoftBankR4-1807101, draft CR introduction completed band combinations 37.865-01-01 -> 38.101-1, Ericsson | 15.2.0 |  |
| 2018-09 | RAN#81 | RP-181896 | 0025 |  | F | Big CR for 38.101-1Endorced draft CRs from RAN4#NR-AH-1807R4-1809335, Draft CR on UL RMC for FR1 RF tests , Qualcomm IncorporatedR4-1809337, Draft CR on NR UE REFSENS SNR FRC for FR1, Intel CorporationR4-1809339, Draft CR on measurement of receiver characteristics for FR1 RF Tests, Qualcomm IncorporatedR4-1809396, Draft CR on NR UE maximum input level FRC for FR1, IntelR4-1809567, Draft CR on OCNG pattern for FR1 REFSENS tests, Qualcomm Incorporated, Rohde & SchwarzEndorced draft CRs from RAN4#88R4-1809714, Draft CR to correct in-band blocking parameters for FR1, Anritsu CorporationR4-1809784, Draft CR to 38.101-1: Corrections on CA bandwidth classes for FR1, ZTE CorporationR4-1809785, Draft CR to TS 38.101-1 for Corrections on UE transmitter power, ZTE CorporationR4-1809793, Draft CR to 38.101-1: Corrections on additional spectrum emission mask, ZTE CorporationR4-1809919, Correction on UE receiver requirement for FR1, CATTR4-1810091, Draft CR TS 38.101-1 - UE ON-OFF mask clean up, EricssonR4-1810210, Draft CR for TS 38.101-1: MPR inner and outer RB allocations formula correction, MediaTek, Inc.R4-1810229, Draft CR for TS 38.101-1: Spurious emission for UE coexistence table corrections, MediaTek, Inc.R4-1810230, Draft CR for TS38.101-1 to correct 90MHz UE CBW, LG Electronics, Inc.R4-1810232, Draft CR for TS 38.101-1: Table 7.3.2-1 n77 reference sensitivity corrections, MediaTek, Inc.R4-1810369, Draft CR to 38.101-1: Corrections on symbols and abbreviations in section 3, ZTE CorporationR4-1810376, Draft CR: General corrections to n71 requirements, Dish NetworkR4-1810428, Draft CR on TS38.101-1 for UE maximum output power for UL MIMO, OPPOR4-1810552, Correction of reference tables, OPPOR4-1810729, Draft CR for introduction of Band n74 for TS 38.101-1, NTT DOCOMO, Inc.R4-1810862, Draft CR to 38.101-1: Updates to Transmit Modulation Annex, Rohde & SchwarzR4-1810892, CR to update Table 6.2D.1-2 for FR1, Qualcomm IncorporatedR4-1810961, CR on ACS minimum requirement, Intel CorporationR4-1810965, CR on Out-of-Band Blocking minimum requirement, Intel CorporationR4-1810967, CR on Rx Intermodulation characteristics for CA, Intel CorporationR4-1810974, Annex lettering change for 38.101-1, Qualcomm IncorporatedR4-1811189, CR to add more details to Coherent UL MIMO spec for FR1, Qualcomm IncorporatedR4-1811280, Corrections of NR receiver characteristics titles, VivoR4-1811455, Draft CR on DL Physical Channel for FR1 RF tests, Qualcomm Europe Inc. (Spain)R4-1811457, NS numbering, Qualcomm IncorporatedR4-1811459, Correction on UE transmitter requirement for FR1, CATTR4-1811463, Draft CR for 38.101-1: Addition of missing NR CA configurations n8-n75 and n28-n75, VodafoneItalia SpAR4-1811472, Addition parameters about n51 in TS 38.101-1, Huawei, Hisilicon, EtisalatR4-1811474, CR CP- OFDM almost contiguous allocation, Nokia, Nokia Shanghai BellR4-1811477, Draft CR to 38.101-1: FR1 Power Control, Qualcomm IncorporatedR4-1811478, A-MPR correction for n20 and n28, Huawei, HiSiliconR4-1811490, Draft CR to 38.101-1: Addition of Carrier Leakage table, Rohde & SchwarzR4-1811491, Draft CR for TS38.101-1 on transmit signal quality, OPPOR4-1811493, CR to TS 38.101-1: pi/2 BPSK with Spectrum Shaping, Indian Institute of Tech (M),Indian Institute of Tech (H), CEWiT,  NokiaR4-1811513, A proposal on 2UL co-ex table modification, SoftBank Corp.R4-1811514, Draft CR to TS 38.101-1: Clarification on OCNG, Keysight Technologies UK LtdR4-1811516, Draft CR on NR DL FRCs for FR1 UE RF requirements, Intel CorporationR4-1811550, Draft CR to TS 38.101-1 on  channel bandwidth and spacing descriptions, EricssonR4-1811553, Draft CR to 38.101-1: Corrections on description of channel raster entries, ZTE CorporationR4-1811783, Measurement period of PRACH time mask, CATTR4-1811792, Draft CR for A-MPR revision for n1, NTT DOCOMO, INC.R4-1811798, Draft CR for Pcmax for FR1, Qualcomm IncorporatedR4-1811799, Pcmax for inter-band NR CA FR1 draft CR, InterDigital, Inc.R4-1811812, Draft CR to 38.101-1: On FR1 AMPR Band n41 NS_04, Qualcomm IncorporatedR4-1811816, CR to update the definition of Long and Short subslot for FR1, QualcommR4-1811894, Addition parameters about n50 in TS 38.101-1, HuaweiR4-1811896, Draft CR for TS 38.101-1: n41 GSCN range modification, MediaTek Inc.R4-1811285, Draft CR TS 38.101-1: NS_04 A-MPR' and spurious emisison corrections, Sprint | 15.3.0 |  |
| 2018-12 | RAN#82 | RP-182836 | 0029 | 1 | F | Endorced draft CRs from RAN4#88Bis:R4-1812050, CR Simplification of NR NS_08, NokiaR4-1812054, Correction for Inter-band CA operating bands table in TS 38.101-1, Nokia.R4-1812079, draft CR to introduce asymmetric UL DL channel BW combinations for n71, T-Mobile USA Inc.R4-1812121, Draft CR on Note1 Corrections in 38.101 RX tests, QualcommR4-1812128, draftCR on 256QAM UL power requirement, Intel CorporationR4-1812200, Draft CR to TS 38.101-1 Add clarification note to PC3 MPR table, Intel CorporationR4-1812217, Draft CR to 38.101-1: Corrections on the descriptions of UE channel bandwidth for CA, ZTE CorporationR4-1812319, Draft CR for TS 38.101-1: REFSENS UL configuration corrections, MediaTek Inc.R4-1812320, Draft CR for TS 38.101-1: Out-of-band blocking exceptions for CA, MediaTek Inc.R4-1812322, Draft CR for TS 38.101-1: Blocking characteristics for SUL, MediaTek Inc.R4-1812397, Clarification for almost contiguous CP-OFDM, Qualcomm IncorporatedR4-1812508, Draft CR to 38.101-1: Corrections on channel raster & SS raster for operating bands, ZTE CorporationR4-1812611, Draft CR to 38.101-1: Some corrections for inter-band CA combinations, ZTE CorporationR4-1813459, Draft CR for TS 38.101-1: Support 4Rx for n38, HuaweiR4-1813469, draftCR on applicability of TDD configuratiin for CA in TS 38.101-1, HuaweiR4-1813521, Addition of ?TC,c for single carrier Pcmax for FR1, vivoR4-1813798, Draft CR to 38.101-1: Corrections on UE additional maximum output power reduction, ZTE CorporationR4-1813811, Draft CR to 38.101-1: Corrrection to n12 reference sensitivity power levels, Skyworks Solutions Inc.R4-1813812, Band n41 spurious emission limits , Qualcomm IncorporatedR4-1813813, Draft CR for TS 38.101-1: P-Max for 5G NR HPUE, CMCCR4-1814158, CR on Spurious emissions for UE co-existence, Intel CorporationR4-1814159, Draft CR for CA ACS/IBB for Bandwidth class C, QualcommR4-1813843, Draft CR to 38.101-1: Update of Annex F, Rohde & SchwarzR4-1813845, Correction for PI/2 PBSK requriements, NokiaEndorsed draft CR's from RAN4#89R4-1815950, dCR on TS38.101-1 merging draft CRs from RAN4#88Bis, Qualcomm IncorporatedR4-1814752, DraftCR to TS 38.101-1 pi/2 BPSK in n41, CMCCR4-1814824, n50 A-MPR, Qualcomm IncorporatedR4-1814959, Changes to Max input power UL and DL configuratgions in FR1, OPPOR4-1814970, NR FR1 relative power tolerance CR, NokiaR4-1814972, A-MPR for NS_03 and NS_03U and re-formulation of NS_100, NokiaR4-1815060, draft CR for adding note about the fallback of NR CA in FR1 for TS 38.101-1, NTT DOCOMO, INC.R4-1815392, Draft CR to 38.101-1: Update to NS_04 requirements, Rohde & SchwarzR4-1815563, Draft CR to 38.101-1 on Clarification on 7.5 KHz raster shift in NR re-farmed bands, EricssonR4-1815863, Draft CR for 38.101-1: Nominal carrier spacing for 30 kHz raster, SPRINT CorporationR4-1815898, draft CR on CA configuration on bandwidth class F, HuaweiR4-1815917, draftCR on DL RMC for TS 38.101-1, HuaweiR4-1816162, Draft CR on introduction of SRS switch IL in FR1, OPPOR4-1816199, Draft CR on FR1-FR2 UE-to-UE coexistence for TS38.101-1, LG Electronics FranceR4-1816200, Draft CR to 38.101-1 on intra-band contiguous CA configurations for FR1, ZTE CorporationR4-1816240, Transient period for SRS Antenna Switching for FR1, QualcommR4-1816243, Draft CR to TS38.101-1_Clarifications on MSD and UL configuration tables for inter-band CA, ZTE CorporationR4-1816466, Draft CR on some changes for SUL band combinations to TS 38.101-1, HuaweiR4-1816468, Support of 7.5 kHz carrier shift for additional operating bands, EricssonR4-1816604, TDD configuration for UE Tx test in FR1, EricssonR4-1816663, Draft CR to 38.101-1 (5.3.4) RB alignment, HuaweiR4-1816755, CR to 38.101-1: ACS and IBB intra-band contiguous CA, Intel CorporationFurther changes in RAN#82- 7.5 kHz frequency shift is specified for all FDD bands in clause 5.4.2.1 | 15.4.0 |  |
| 2018-12 | RAN#82 | RP-182814 | 0030 | 2 | F | Company CR on 2Rx exception for NR vehicular UE at FR1 | 15.4.0 |  |
| 2019-03 | RAN#83 | RP-190403 | 0034 |  | F | CR to TS 38.101-1: Implementation of endorsed draft CRs from RAN4#90Endorced draft CR from Ran4#90R4-1900032, Editorial corrections for 38.101-1, Qualcomm IncorporatedR4-1900031, draftCR on SRS IL for CA, Qualcomm IncorporatedR4-1900161, CR on Relative power tolerance, Intel CorporationR4-1900162, CR on Minimum output power, Intel CorporationR4-1900274, Draft CR to TS 38.101-1 on NR general spectrum emission mask, ZTE CorporationR4-1900275, Draft CR to TS 38.101-1 on spurious emisssion for network signalled value NS_40, NS_41 and NS_42, ZTE CorporationR4-1900424, Correction of table references and other typos, EricssonR4-1900508, Draft CR to TS 38.101-1 on UE transmitter power and some other editorial corrections, ZTE CorporationR4-1900723, Draft CR on editorial error of TS38.101-1, LG Electronics Inc.R4-1900727, Update to PRACH EVM window length for FR1, Rohde & SchwarzR4-1900840, Draft CR for 38.101-1 modification of Transmit intermodulation requirement, HuaweiR4-1900848, [RAN5 LS]Draft CR for 38.101-1: adding note for inter-band CA spurious emissions, HuaweiR4-1901033, Alignment of Foob related description for 38.101-1, vivoR4-1901273, Correction of HARQ-ACK transmission timing for DL RMC for FR1 TDD SCS=60kHz, EricssonR4-1901766, draft_CR TS 38.101-1 Correction to UL configuration for reference sensitivity, Skyworks Solutions Inc.R4-1901823, draft CR on spurious requirment for TS 38.101-1, Huawei, HiSiliconR4-1901835, draftCR on MSD for CA_n41-n78 for TS 38.101-1, HuaweiR4-1901847, Draft CR for 38.101-1: Addition of default power class, Sprint Corporation R4-1901873, Receiver requirement RMC references, Qualcomm IncorporatedR4-1901925, Draft CR to 38.101-1 to update and clarify Rx wide band intermod and spurious requirments for BW class C, D, E, Qualcomm IncorporatedR4-1901992, Draft CR to 38.101-1. Correct  FR1 NS_41 AMPR for n50 , HuaweiR4-1902001, Draft CR to 38.101-1 on n41 – B40 coexistence, Qualcomm IncorporatedR4-1902150, Draft CR to TS38.101-1_Clarifications on MSD and UL configuration tables for inter-band CA, ZTE CorporationR4-1902166, Tx ON/OFF time mask for FR1, Qualcomm IncR4-1902174, Draft CR to 38.101-1: On FR1 A-MPR NS_08 for n8, Qualcomm IncorporatedR4-1902175, Draft CR on AMPR requirements for NS_05U and NS_08U to TS 38.101-1, HuaweiR4-1902194, [41 DL]Draft CR for 38.101-1 adding DL intra-band CA requirements for frequency less than 2700MHz, HuaweiR4-1902196, Draft CR for 7.9A Spurious emissions for CA, CMCCR4-1902223, UE optional bandwidth for FR1, NokiaR4-1902225, CR to 38.101-1 on CA BW Classes fallback groups, Intel CorporationR4-1902233, Draft CR to 38.101-1: SUL clarifications, NokiaR4-1902339, Draft CR to TS 38.101-1 on FR1 extension, EricssonR4-1902455, Completion of the Pcmax specification: additional P-max and P_NR, EricssonR4-1902468, Draft CR: Introduction of Annex on Characteristics of the Interfering Signal, SamsungR4-1902479, Draft CR on some errors to TS 38.101-1, HuaweiR4-1902480, Draft CR for 38.101-1 modification of requirements for network signalled value NS_04, HuaweiR4-1902655, CR to 38.101-1 on NR Uplink RBs location, Intel CorporationR4-1901610, Draft CR for 38.101-1 REFSENS for UL MIMO , HuaweiEditorial changes after RAN#83To align the annex numbering with other specifications (TS 38.101-x series), annexes J and K were added and Change history was numbered as annex L. | 15.5.0 |  |
| 2019-06 | RAN#84 | RP-191240 | 0047 |  | F | CR to TS 38.101-1: Implementation of endorsed draft CRs from RAN4#90bis and RAN4#91Endorced draft CRs from RAN4#90BisR4-1902826, Draft CR for 38.101-1 modification of ACS test parameters case 2 for intra-band contiguous CA , HuaweiR4-1902926, Draft CR to TS 38.101-1 Correction to Pcmax, Intel CorporationR4-1902975, Draft CR on PRACH and PUCCH format description for EVM in FR1, Anritsu corporationR4-1903032, Draft CR on editorial error of TS38.101-1, LG Electronics FranceR4-1903120, Draft CR on DL power allocation for TS 38.101-1, Intel CorporationR4-1903124, Draft CR on b41-n40 coexistence, Intel CorporationR4-1903151, Draft CR to TS38.101-1_removing DC sections, ZTE CorporationR4-1903195, Draft CR for 38.101-1: remove the bracket of UE capability "powerBoosting-pi2BPSK", HuaweiR4-1903392, Draft CR for TS 38.101-1: Corrections to EVM equalizer spectrum flatness requirements, MediaTek Inc.R4-1903473, Draft CR on FREF,Shift, CMCCR4-1903508, Draft CR to TS 38.101-1 on spurious emissions for UE co-existence, ZTE CorporationR4-1904335, DraftCR TS 38.101 Corrections to NS_100 UTRA ACLR frequency band list, Skyworks Solutions Inc.R4-1904460, Draft CR for 38.101-1 CA Pcmax, HuaweiR4-1904537, Draft CR for TR 38.101-1 correction of A-MPR for NS_04, HuaweiR4-1904554, Draft CR to 38.101-1: FR1 power dynamics DTX removal, Qualcomm IncorporatedR4-1904927, Draft CR to clarify frequency of carrier leakage in RBs for FR1, Anritsu corporationR4-1904928, Draft CR to TS 38.101-1 on description of UE additional output power reduction, ZTE CorporationR4-1904929, draft Rel-15 CR for editorial corrections in 38.101-1, EricssonR4-1904941, draft CR to 38.101-1 Correction to Pi/2 BPSK power boosting, Intel CorporationR4-1904957, Draft CR for TR38.101-1 – Update to EVM averaging, Rohde & SchwarzR4-1904958, Draft CR for TR38.101-1 – Update to spectrum flatness, Rohde & SchwarzR4-1904967, Draft CR for 38.101-1 definition of Maximum input level for intra-band contiguous CA, HuaweiR4-1904969, Draft CR for 38.101-1: editoral correction, HuaweiR4-1904987, Draft CR for correction on TS38.101-1, CATTEndorced draft CRs from RAN4#91R4-1905339 removal of A-MPR brackets in FR1 NokiaR4-1905503 Change description 4.2(d) in Applicability of minimum requirements for TS 38.101-1 vivoR4-1905524 [Rx]Draft CR for 38.101-1 Removing the brackets in Rx requirements HuaweiR4-1905526 [Rx]Draft CR for 38.101-1 defining NBB requirements<2.7GHz HuaweiR4-1905772 Draft CR to TS38.101-1 Almost contiguous MPR Intel CorporationR4-1905795 Correction to a description of PRB for in-band emission in FR1 Anritsu CorporationR4-1905797 Correction to power control in FR1 Anritsu CorporationR4-1906140 draft CR for TS 38.101-1 Rx requirement for CA HuaweiR4-1906153 Draft CR for TS 38.101-1: Editorial corrections to intra-band contiguous CA ACS and in-band blocking requirements MediaTek Inc.R4-1906154 Draft CR for TS 38.101-1: Adding symbol definitions for intra-band contiguous CA Rx maximum input level and ACS requirements MediaTek Inc.R4-1906871 Draft CR for TS 38.101-1 UE optional bandwidth for FR1 HuaweiR4-1907131 Draft CR to 38.101-1. Clarification to  FR1 NS_43 AMPR frequency ranges Qualcomm IncorporatedR4-1907135 Draft CR to 38.101-1 rel. 15 to fix missing Exceptions for Out-of-band Blocking AppleR4-1907419 Draft CR for TS 38.101-1: Editorial improvement to EVM equalizer spectrum flatness requirements for Pi/2 BPSK MediaTek Inc.R4-1907429 Draft CR to TS38.101-1 A-MPR for Inter-band CA Intel CorporationR4-1907434 [Rx]Draft CR for 38.101-1 modifying characteristics of the interfering signal in Annex D HuaweiR4-1907435 Draft CR to TS38.101-1_introduction of n41C and corrections on Rx requirements for NR intra-band contiguous CA ZTE CorporationR4-1907439 Draft CR to TS 38.101-1 on CA bandwidth class description ZTE CorporationR4-1907471 Draft CR to 38.101-1. Clarify all RB reference so transmission BW applies for all SCS Qualcomm IncorporatedR4-1907474 Draft CR for TS 38.101-1 Correction of channel bandwidth set for NR CA HuaweiR4-1907477 Draft CR to TS 38.101-1 on maximum aggregated bandwidth for NR CA configurations ZTE CorporationR4-1907481 Correction of RefSens exceptions due to UL harmonic interference for NR CA in 38.101-1 vivoR4-1907687 Correction to CA carrier spacing Ericsson | 15.6.0 |  |
| 2019-06 | RAN#84 | RP-191248 | 0037 | 1 | B | Introduction of n48 in to TS 38.101-1 | 16.0.0 |  |
| 2019-06 | RAN#84 | RP-191241 | 0040 |  | B | CR to REL-16 TS 38.101-1: Implementation of endorsed draft CRs on NR combinations and dual Connectivity combinations | 16.0.0 |  |
| 2019-06 | RAN#84 | RP-191242 | 0041 | 1 | B | CR to TS 38.101-1: Introduction of band n14 – Endorsed R4-1904008 in RAN4#90b | 16.0.0 |  |
| 2019-06 | RAN#84 | RP-191246 | 0042 | 1 | B | CR to TS 38.101-1: Introduction of band n30 + editorial in table 7.6.2-2 | 16.0.0 |  |
| 2019-06 | RAN#84 | RP-191244 | 0043 | 1 | B | CR to introduce n18 to TS 38.101-1 | 16.0.0 |  |
| 2019-06 | RAN#84 | RP-191250 | 0044 | 1 | B | n65 introduction to 38.101-1 | 16.0.0 |  |
| 2019-06 | RAN#84 | RP-191251 | 0045 |  | B | Addition channel bandwidth of 30MHz for n50 in TS 38.101-1 | 16.0.0 |  |
| 2019-06 | RAN#84 | RP-191252 | 0046 | 1 | B | Introduction of a new NR band for LTE/NR spectrum sharing in Band 41/n41 | 16.0.0 |  |
| 2019-06 | RAN#84 | RP-191241 | 0048 |  | B | CR on introducing NR inter-band CA of 3DL Bands and 1UL band | 16.0.0 |  |
| 2019-06 | RAN#84 | RP-191241 | 0049 |  | B | CR to reflect the completed NR inter-band CA/DC combinations into Rel16 TS38.101-1 | 16.0.0 |  |
| 2019-06 | RAN#84 | RP-191241 | 0050 |  | B | CR to reflect the completed NR inter-band CA/DC combinations for 3 bands DL with 2 bands UL into Rel16 TS38.101-1 | 16.0.0 |  |
| 2019-06 | RAN#84 | RP-191241 | 0051 |  | B | CR introduction completed band combinations 38.716-01-01 -> 38.101-1 | 16.0.0 |  |
| 2019-09 | RAN#85 | RP-192038 | 0052 |  | F | Correction to FR1 ASEM NS_27 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192032 | 0053 |  | B | Addition of NS information on 30MHz support for n41 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192031 | 0054 | 1 | B | Addition of new channel bandwidths for n7 into TS 38.101-1 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192027 | 0055 |  | B | CR on introducing NR intra-band CA for 3DL Bands and 1UL band | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192027 | 0057 | 1 | F | Minor corrections of intra-band non-contiguous CA operating bands in TS 38.101-1 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192027 | 0058 | 1 | F | Adding DeltaFHD for CA_n1-n77 refersense requirments | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192032 | 0060 |  | B | CR to introduce 30MHz bandwidth of n41 into TS 38.101-1 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192026 | 0061 | 1 | B | Characteristics of Interfering signal for Contiguous Intra-band CA Class B | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192027 | 0062 | 1 | F | Correction Inter-band CA configurations | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192027 | 0063 | 1 | F | Finalizing Generic Intra-band Contiguous CA Class B requirements | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192034 | 0064 | 1 | B | n29 introduction to 38.101 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192027 | 0065 |  | F | [SUL] CR on SUL band combinations into Rel-16 TS 38.101-1 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192029 | 0066 |  | B | CR on Introduction of SUL band n89 into Rel-16 TS 38.101-1 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192046 | 0068 | 2 | F | Correction to Band n66 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192026 | 0070 | 1 | F | CR to 38.101-1. Revamp CA ACS and IBB tables to differentiate by band numbers and not frequency | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192038 | 0071 |  | F | CR to 38.101-1. Add missing AMPR to NS27 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192026 | 0072 |  | B | CR for 38.101-1 Rx requirement for NR intra-band non-contiguous CA | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192036 | 0073 |  | F | CR for 38.101-1: Correction to the Spurious Emission for UE Coexistence table for n14 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192037 | 0074 |  | F | CR for 38.101-1: Correction to the Spurious Emission for UE Coexistence table for n30 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192027 | 0075 |  | B | CR introduction completed band combinations 38.716-01-01 -> 38.101-1 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192027 | 0076 |  | B | CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into Rel16 TS 38.101-1 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192027 | 0077 |  | B | CR to reflect the completed NR inter band CA DC combinations for 3 bands DL with 2 bands UL into Rel16 TS 38.101-1 | 16.1.0 |  |
| 2019-09 | RAN#85 | RP-192049 | 0079 |  | A | CR to TS 38.101-1: Implementation of endorsed draft CRs from RAN4#92 (Rel-16)- Mirrors changes in R4-1910350 (of RAN4#92)  for Rel-15 TS 38.101-1 | 16.1.0 |  |
| 2019-12 | RAN#86 | RP-193022 | 0097 |  | F | CR to align NS27 AMPR to CA_NS_10 AMPR for 40MHz BW at the center of band 48. | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193028 | 0099 |  | A | CR for 38.101- RX Out-of-Band Blocking for B38 and B41 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193028 | 0103 |  | A | CR for 38.101-1 n39 AMPR | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193013 | 0105 | 1 | B | Introduction of 2010-2025MHz SUL band into Rel-16 TS 38.101-1 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193015 | 0110 |  | B | Addition of 25, 30 and 40 MHz to NR band n25 in TS 38.101-1 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193028 | 0112 |  | A | Sync raster to SSB resource element mapping | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193028 | 0114 |  | A | CR to TS 38.101-1 Almost contiguous A-MPR (R16) | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193028 | 0118 |  | A | CR to 38.101-1 (Rel-16) to clarify measurement interval and observation window on frequency error | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193020 | 0119 |  | D | Format misalignment on NS_47 protection requirement table | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193028 | 0121 |  | A | CR to TS 38.101-1: Replace CBW with symbols defined in the specification | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193012 | 0124 |  | B | CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into Rel16 TS 38.101-1 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193012 | 0125 |  | B | CR to reflect the completed NR inter band CA DC combinations for 3 bands DL with 2 bands UL into Rel16 TS 38.101-1 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193012 | 0126 |  | F | CR to remove square brackets for n90 in TS38.101-1 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193028 | 0128 |  | A | CR for TS38.101-1, Clarification and Editorial corrections | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193012 | 0132 |  | B | Introducing NR inter-band CA for 3DL Bands and 1UL band for 38.101-1 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193029 | 0133 |  | B | Adding band n71 and n28 to 4 Rx antenna ports support in 38.101-1 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193028 | 0137 |  | A | CR for TS 38.101-1: Editorial correction for n2 uplink configuration note index in Table 7.3.2-3 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193028 | 0138 |  | A | CR to TS 38.101-1 on A-MPR table cleanup (Rel-16) | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193029 | 0140 |  | A | CR for TS 38.101-1: Removing CA configurations for CA_n77D/E, CA_n78D/E, and CA_n79D/E | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193029 | 0144 |  | A | CR for TS 38.101-1: Fix out-of-band blocking issue for n50 and n75 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193029 | 0146 |  | A | CR to TS 38.101-1 on corrections to channel raster entries for NR band (Rel-16) | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193029 | 0150 |  | A | CR to transmit modulation quality in FR1 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193012 | 0151 |  | F | Corrections Intra-band CA simultaneous TX/RX requirements | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193029 | 0153 |  | F | Removal of brackets from reciever requirements in 38.101-1 REL-16 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193012 | 0155 |  | B | Extension of CA BW class B | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193029 | 0157 |  | A | CR to 38.101-1: Editorial correction of UL RMCs | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193012 | 0164 |  | B | CR for 38.101-1 introduce SUL band combination CA_n78(2A)_SUL_n78A-n86A | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193010 | 0165 |  | F | CR for 38.101-1: add BCS1 configurations for CA_n78(2A) | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193017 | 0166 |  | B | CR to 38.101-1 - Band n75 - wider CBW | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193018 | 0167 |  | B | CR for TS 38.101: adding wider channel bandwidths | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193016 | 0168 |  | B | CR to 38.101-1: Addition of channel bandwidth for band n38 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193012 | 0169 |  | B | CR introduction completed band combinations 38.716-01-01 -> 38.101-1 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193012 | 0170 |  | B | CR introduction completed band combinations 38.716-04-01 -> 38.101-1 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193021 | 0171 |  | C | CR for 38.101-1: Making 90 MHz channel bandwidth mandatory for n41, n78 and n90 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193020 | 0172 |  | B | CR for 38.101-1: adding 30 MHz CHBW to NS_04 for n41 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193029 | 0174 |  | A | CR to 38.101-1-g10 Corrections to Transient Time Masks | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193010 | 0176 | 1 | F | CR for intra-band DL contiguous CA RF requirements | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193010 | 0179 |  | B | Introduction of almost contiguous MPR for PC2 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193029 | 0180 |  | A | CR for asynchronous operation for NR CA n78-n79 | 16.2.0 |  |
| 2019-12 | RAN#86 | RP-193028 | 0182 |  | A | CR to 38.101-1: DMRS Exceptions | 16.2.0 |  |
| 2020-03 | RAN#87 | RP-200408 | 0191 |  | F | Corrections to n65 | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200377 | 0201 | 1 | F | CR for 38.101-1 to introduce BCS1 for CA_n77C and CA_n78C | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200394 | 0203 |  | A | CR to TS 38.101-1 on corrections to network signalling value (Rel-16) | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200484 | 0208 |  | A | CR for 38.101- n39 NS flag change due to conflict | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200394 | 0210 |  | A | Mirror CR for 38.101-1: n41 and n25 corrections | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200380 | 0211 | 2 | F | CR for 38.101-1: Corrections to intra-band CA tables | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200387 | 0212 |  | F | CR for 38.101-1: Missing 70 MHz for NS_01 | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200381 | 0215 |  | B | CR for 38.101-1: Introduction of n26 | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200380 | 0216 |  | F | CR to TS 38.101-1: Corrections on MSD tables for CA_n20-n78 and CA_n66-n78 | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200394 | 0218 |  | A | CR to TS 38.101-1: corrections on ACS for intra-band contiguous CA | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200380 | 0219 | 1 | F | CR to TS 38.101-1: Improvement on NR 3DL inter-band CA combination | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200394 | 0221 |  | A | CR to TS 38.101-1: Replace CBW with symbols defined in the specification.NOTE: The CR is based on something else than the latest version of the specification and therefore it is not implemented, e.g. Tables 6.2.3.1-1, 7.6.2-2 and Table 7.6.2-4 in CR0221 are different compared to those in 38.101-1 v16.2.0. | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200380 | 0222 |  | B | CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into Rel16 TS 38.101-1 | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200380 | 0223 |  | B | CR to reflect the completed NR inter band CA DC combinations for 3 bands DL with 2 bands UL into Rel16 TS 38.101-1 | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200394 | 0224 | 1 | B | Introduction of n53 into TS 38.101-1 | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200394 | 0229 |  | A | CR for TS38.101-1, Remove notes for UE channel bandwidth | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200394 | 0231 |  | A | CR for TS38.101-1, Correction of IE RF-Parameters name of maxUplinkDutyCycle | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200380 | 0234 | 1 | B | Introducing NR inter-band CA for 3DL Bands and 1UL band for 38.101-1 | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200377 | 0239 | 1 | F | CR for TS 38.101-1: Corrections for n48 receiver requirements | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200386 | 0240 | 1 | B | CR for TS 38.101: adding wider channel bandwidths for n66 | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200392 | 0241 | 1 | F | Maintenance on the UE BW for n92 and n94 | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200392 | 0242 |  | F | Maintenance on the Rx-Tx separation terms | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200394 | 0244 |  | A | CR for 38.101-1: to remove fallback group 1 in table 5.5A.1-1 | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200389 | 0247 |  | F | CR for 38.101-1: to correct CA_n8A-n75A REFSENS | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200384 | 0249 | 1 | B | CR for 38.101-1: to introduce UE RF requirements for adding wider channel bandwidth in band n28 | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200383 | 0250 | 1 | B | CR to 38.101-1 Band n1 - wider CBW - Additional Channel BW | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200385 | 0252 | 1 | B | CR to 38.101-1 Band n38 - wider CBW - Additional Channel BW | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200380 | 0260 | 1 | F | Editorial corrections | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200377 | 0263 |  | F | CR for alomost contiguous allocation applicability | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200394 | 0265 | 1 | A | CR for inter-band CA Tx requirement | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200377 | 0266 | 1 | F | CR for intra-band CA configuration and DL RF requirements | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200391 | 0273 |  | F | CR for 38.101-1: Mandatory support for n41 by UEs that support n90 | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200394 | 0275 |  | A | CR for [agreed] asynchronous operation for NR CA n78-n79NOTE: The CR is based on something else than the latest version of the specification and therefore it is not implemented, e.g. Tables 6.2A.4.2.3-1, Table 7.3A.6-1, 7.3A.6.2 and table notes are different compared to those in 38.101-1 v16.2.0. | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200380 | 0280 |  | F | CR for 38.101-1: delta Tib corrections | 16.3.0 |  |
| 2020-03 | RAN#87 | RP-200394 | 0281 |  | A | Removal of unnecessary definition of offsetmax,IMD3 from Table 6.2.3.2-1 | 16.3.0 |  |
| 2020-06 | RAN#88 | RP-201338 | 0293 | 4 | B | CR to TS 38.101-1: Switching time mask between two uplink carriers in UL CA and SUL | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200959 | 0294 |  | F | Corrections to CA n48 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0300 |  | A | CR to asymmetric CBW operation in FR1 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0302 |  | A | CR on ACLR MBW definition in FR1 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200959 | 0305 |  | B | Introducing NR inter-band CA for 3DL Bands and 1UL band for 38.101-1 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200959 | 0307 |  | F | CR Coexistence cleanup for 38101-1 Rel16 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0310 |  | A | CR to TS 38.101-1 R16: corrections on ACS for intra-band contiguous CA | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200966 | 0311 |  | F | CR for TS 38.101-1: UL harmonic MSD and OOBB exception | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200981 | 0315 |  | F | Update 4Rx Requirement for Band n30 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200958 | 0317 |  | B | CR on NR V2X UE RF requirements for single carrier in TS38.101-1 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0327 |  | A | Maintenance CR to 38101-1 on relative power tolerance R16 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200974 | 0329 |  | F | Endorsed CR on default AMPR signaling for n91 n92 n93 and n94 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0331 |  | A | Update of CSI-RS definition for FR1 DL RMCs | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0335 |  | A | Correction to FR1 QPSK UL RMC | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200966 | 0336 |  | B | CR to TS38.101-1: Introduction of NR DC(Clauses 3 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0338 |  | A | CR to TS 38.101-1: Correction on the CA nominal channel spacing | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0340 |  | A | CR to TS 38.101-1: Replace CBW with symbols defined in the specification. | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200959 | 0341 |  | B | CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into Rel16 TS 38.101-1 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0345 |  | A | 30k SSB SCS for n50 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0347 |  | A | Addition of 30k SSB SCS for Band n38 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0354 |  | A | IBE measurements for Pi/2 BPSK with spectrum shaping | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200959 | 0357 |  | B | CR to reflect the completed NR inter band CA DC combinations for 3 bands DL with 2 bands UL into Rel16 TS 38.101-1 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200959 | 0360 |  | B | CR introduction completed band combinations 38.716-01-01 - | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200959 | 0361 |  | B | CR introduction completed band combinations 38.716-04-01 - | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200959 | 0364 |  | B | CR on Introduction of completed SUL band combinations into TS 38.101-1 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-201045 | 0365 |  | F | CR for 38.101-1 to introduce BCS2 for CA_n78(2A). | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0367 |  | A | CR for 38.101-1 to remove the NR CA configuration for REFSENS exception due to cross band isolation for CA (mirror CR) | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0369 |  | A | CR for 38.101-1 to add the REFSENS exception for inter band CA with SDL (mirror CR) | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200979 | 0373 |  | F | CR on introduce delta-MPR for inter-band CA in band n28 and review value with brackets | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0379 |  | A | IBE requirement for almost contiguous allocations | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0385 |  | A | OOB blocking for n70 adjacent to n25 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0394 |  | F | CR for TS 38.101-1 UE co-existence correction (R16) | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0396 |  | F | CR for 38.101-1 RFC corrections (R16) | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0400 |  | A | TS38.101-1 CR on 30KHz SSB SCS for n40(Rel-16) | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200959 | 0318 | 1 | F | CR to add simultaneous RXTX capability for CA_n41-n79 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0404 |  | A | CR for 38.101-1: to add some missing sub-clause title for NR inter-band CA | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0343 | 1 | A | CR for [agreed] asynchronous operation for NR CA n78-n79 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-201045 | 0387 | 1 | B | CR on FR1 UL contiguous CA requirement | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200974 | 0325 | 1 | F | CR on blocking requirements for n91 n92 n93 and n94 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-201045 | 0380 | 1 | B | Addition of mutual UE coexistence between US bands and NR Band n77 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200977 | 0356 | 1 | B | CR for TS 38.101: adding 50 MHz CBW for n1 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200980 | 0358 | 1 | B | CR to TS 38.101-1 - Add 40 MHz CBW in band n3 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200982 | 0359 | 1 | B | CR to TS 38.101-1 - Add 50 MHz CBW in band n65 | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200985 | 0405 |  | F | Corrections of UE co-ex tables for Japan-related bands (R16) | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-201045 | 0320 | 2 | B | CR to 38.101-1: Introduce an operating band list and NR bands to UL MIMO | 16.4.0 |  |
| 2020-06 | RAN#88 | RP-200966 | 0362 | 1 | B | CR to 38.101-1 for Introduction of requirements for NR-DC | 16.4.0 |  |
| 2020-09 | RAN#89 | RP-201495 | 0407 | 1 | F | Correction to FR1 UL contiguous CA MPR regions | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201506 | 0409 |  | F | CR for n26 AMPR for 256QAM | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201512 | 0411 |  | A | OOB blocking for Inter-band CA | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201512 | 0416 | 1 | F | Correction to ASEM for NS_27 | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201507 | 0419 |  | F | Introduction of UE PC2 for NR band n40 | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201502 | 0422 | 1 | B | Introduction of LTE/NR spectrum sharing in band 48/n48 frequency range | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201507 | 0423 |  | F | Coexistence cleanup for 38101-1 Rel16 | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201506 | 0424 |  | D | CR Editorial cleanup of band combination tables for 38101-1 Rel16 | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201512 | 0426 |  | A | CR to TS 38.101-1: corrections on narrow band blocking for intra-band contiguous CA | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201492 | 0428 | 1 | F | CR for TS 38.101-1: Removal of table 6.5E.3.4.3-1 and table 6.5E.3.4.3-2 | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201503 | 0432 | 1 | B | CR for 38.101-1: Introduction of Power Class 1.5 | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201488 | 0433 | 1 | B | CR to TS38.101-1 on introduction of Uplink Full Power Transmission | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201512 | 0435 |  | A | Corrections of Japan-related CA co-ex tables for REL-15 combo | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201492 | 0437 | 1 | F | Correction on 5G V2X UE RF requirements in rel-16 | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201495 | 0438 | 2 | B | A-MPR definition for CA_n48B, CA_n41B and CA_n41C | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201495 | 0439 |  | F | CR Restoring the clause structure of NR FR1 uplink contiguous intraband CA | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201492 | 0440 | 1 | F | CR on TS38.101-1 for NR V2X | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201512 | 0442 |  | A | 30k SSB SCS for Band n34 and n39 | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201512 | 0444 |  | F | Correction for 5 MHz channel bandwidth for n50 and introduction of Annex H | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201512 | 0458 |  | A | CR for 38.101-1 FRC corrections (R16) | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201506 | 0459 | 1 | F | CR for 38.101-1 to remove PHS system and 860~890 protection for NR CA band combination with band n1 and band n8 | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201506 | 0460 | 1 | F | CR for 38.101-1 to add the missing region for NS_18 and maintenance the ?mprc | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201512 | 0462 |  | A | CR for 38.101-1 to add the missing MSD for CA_n41A-n78A | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201512 | 0465 |  | A | Correction to configured power with allowance for SRS switching | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-202117 | 0466 |  | B | Introduce UE NR-U requirements to 38.101-1 including Band n46 (5 GHz) and Band n96 (6 GHz) | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201495 | 0468 | 1 | F | CR for intra-band UL CA non-contiguous CA requirement | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201495 | 0469 | 1 | F | CR for correction on intra-band UL CA contiguous CA requirement | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201495 | 0470 | 1 | F | CR for intra-band UL contiguous CA DC location | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201495 | 0471 | 1 | B | CR for intra-band UL CA non-contiguous CA requirement | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201507 | 0480 | 1 | F | CR to 38.101-1 - Correction to CA BCS and cross band isolation MSD tables | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201512 | 0483 |  | A | Correction of applicability of 2Rx requirements | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-201488 | 0486 | 2 | B | CR to add PC3 Pi/2 BPSK DMRS for IE powerBoostPi2BPSK = 0 | 16.5.0 |  |
| 2020-09 | RAN#89 | RP-202098 | 0499 | 1 | C | 7.5 kHz UL shift for LTE/NR spectrum sharing in Band 38/n38 | 16.5.0 |  |
| 2020-12 | RAN#90 | RP-202440 | 0492 | 1 | F | CR CatF n7 NS_46 AMPR and coexistence | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202427 | 0498 | 1 | F | Correction on 5G V2X UE RF requirements in TS38.101-1 in rel-16 | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202438 | 0506 |  | F | n53 bracket removal | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202442 | 0507 | 2 | F | A-MPR definition for CA_n7B, CA_n48B, CA_n41B and CA_n41C | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202485 | 0512 |  | A | CR to TS38.101-1 on DC location correction | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202509 | 0518 |  | F | Coexistence cleanup for 38.101-1 Rel16 | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202509 | 0524 | 1 | F | CR to TS 38.101-1 on simplification for inter-band CA configuration | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202427 | 0525 |  | F | CR on TS38.101-1 for NR V2X | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202485 | 0527 |  | A | CR to TS 38.101-1[R16]: Clarification of non-simultaneous Rx/Tx operation for CA_n77-n79 and CA_n78-n79 in TS 38.101-1. | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202442 | 0533 | 1 | F | CR to 38.101-1 Add requirement on the UL CA configurations with no DL interruption | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202509 | 0534 |  | F | Editorial correction on section 5.2C to 38.101-1 R16 | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202427 | 0535 | 1 | F | CR on V2X bands reference table | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202509 | 0536 | 1 | F | CR on sum of power for multiple transmit connectors | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202428 | 0540 |  | F | CR for 38.101-1 to correct the notation of SUL band combinations in order to be aligned with 38.101-3 | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202485 | 0542 |  | A | CR for 38.101-1 to adjust the structure of NR CA REFSENS (Rel-16) | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202509 | 0544 |  | F | Reference measurement channels for 70 MHz CBW | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202428 | 0547 |  | F | Correction to supported channel bandwidths per SUL_n41A-n81A | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202414 | 0550 | 3 | F | Correction to the intra-cell guard band definition for wideband operation | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202414 | 0552 | 1 | F | Correction to receiver requirements for shared spectrum channel access | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202442 | 0556 |  | F | CR Correction to NS_27 and Band 10 protection 38101-1 Rel16 | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202428 | 0557 | 1 | F | CR for editorial corrections 38.101-1 | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202414 | 0558 | 2 | F | Removal of square brackets for 38.101-1 NR-U | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202509 | 0562 |  | F | CR to for 38.101-1: CA uplink power clarification | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202509 | 0563 |  | D | CR for 38.101-1: Editorial corrections | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202427 | 0566 | 1 | F | CR for 38.101-1 NR V2X FRC | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202485 | 0571 |  | A | CR for TS 38.101-1: correction of delta Tib for UE supporting multiple band combinations (R16) | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202442 | 0574 | 1 | B | CR for intra-band UL CA non-contiguous CA requirement | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202485 | 0581 |  | A | CR for 38.101-1 on corrections for AMPR-Rel-16 | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202485 | 0584 |  | A | CR to DMRS position in UL RMC for FR1 | 16.6.0 |  |
| 2020-12 | RAN#90 | RP-202456 | 0408 | 3 | B | LTE/NR spectrum sharing in Band 40/n40 | 17.0.0 |  |
| 2020-12 | RAN#90 | RP-202451 | 0499 |  | B | Introduction of 1880-1920MHz SUL band into Rel-17 TS 38.101-1 | 17.0.0 |  |
| 2020-12 | RAN#90 | RP-202452 | 0500 |  | B | introduction of 2300-2400MHz SUL band into Rel-17 TS 38.101-1 | 17.0.0 |  |
| 2020-12 | RAN#90 | RP-202450 | 0503 | 1 | B | CR for TS 38.101-1, Introduce new band combination of V2X_n39A-n47A and V2X_n40A-n47A | 17.0.0 |  |
| 2020-12 | RAN#90 | RP-202468 | 0504 |  | B | CR on Introducing NR inter-band CA for 3DL Bands and 1UL band for 38.101-1 | 17.0.0 |  |
| 2020-12 | RAN#90 | RP-202471 | 0513 |  | B | CR on introduction of completed NR CA/DC combs with 4DL/2UL within FR1 | 17.0.0 |  |
| 2020-12 | RAN#90 | RP-202472 | 0514 |  | B | CR on Introduction of completed SUL band combinations into TS 38.101-1 | 17.0.0 |  |
| 2020-12 | RAN#90 | RP-202448 | 0543 | 1 | B | CR to TS 38.101-1: introduction of NR band n13 | 17.0.0 |  |
| 2020-12 | RAN#90 | RP-202455 | 0545 |  | B | CR to 38.101-1 Introduce band combination requirements for PC2 CA_n1A-n78A | 17.0.0 |  |
| 2020-12 | RAN#90 | RP-202453 | 0546 | 1 | B | Big CR to 38.101-1 - Additional Channel BW | 17.0.0 |  |
| 2020-12 | RAN#90 | RP-202466 | 0548 |  | B | CR introduction completed band combinations Rel-17 NR Intra-band - | 17.0.0 |  |
| 2020-12 | RAN#90 | RP-202470 | 0549 |  | B | CR introduction completed band combinations NR Inter-band 4 bands CA - | 17.0.0 |  |
| 2020-12 | RAN#90 | RP-202467 | 0585 |  | B | CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into TS 38.101-1 | 17.0.0 |  |
| 2020-12 | RAN#90 | RP-202469 | 0586 |  | B | CR to reflect the completed NR inter band CA DC combinations for 3 bands DL with 2 bands UL into TS 38.101-1 | 17.0.0 |  |
| 2021-03 | RAN#91 | RP-210190 | 0589 |  | A | PC1 and PC3 Updates for Band n14 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210117 | 0594 | 1 | A | 38.101 Void clean up R17 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210097 | 0604 | 2 | B | CR for TS 38.101-1 introduction of NR band n24 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210072 | 0606 |  | A | CR on editorial correction on V2X operation in TS38.101-1 in Rel-17 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210178 | 0607 |  | B | CR on Introduction of completed SUL band combinations into TS 38.101-1 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210096 | 0609 | 2 | B | CR to 38101-1 on introducing new SUL band n99 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210117 | 0612 |  | A | CR for TS38 101-1 Rel-17 Correction for definition of P-MPR | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210117 | 0614 |  | A | CR for TS38 101-1 Rel-17 Correction of condition for MPR and delta MPR | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210094 | 0616 | 1 | B | CR for TS 38.101-1, Introduce new band combination of V2X_n41A-n47A | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210179 | 0617 |  | B | CR on Introducing NR inter-band CA for 3DL Bands and 1UL band for 38.101-1 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210094 | 0625 |  | F | Revision of inter-band V2X con-currency table for V2X_n39A-n47A and V2X_n40A-n47A | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210092 | 0628 | 1 | B | Switching time mask for 2Tx-2Tx switching between two carriers and 1Tx-2Tx/2Tx-2Tx switching between two bands in Rel-17 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210082 | 0630 |  | F | CR for TS 38.101-1: Correction on 1Tx-2Tx switching between two uplink carriers (Rel-17) | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210092 | 0631 |  | B | CR on introducing NR SUL bands n80 to UL-MIMO configuration | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210091 | 0633 |  | A | CR for 38.101-1: Update of missing fallback NR-DC combinations Rel-17 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210184 | 0636 | 1 | B | CR on introduction of completed NR CA/DC combs with 4DL/2UL within FR1 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210091 | 0642 |  | A | CR on introduction of shorter Transient Period Capability | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210100 | 0657 |  | B | CR introduction completed band combinations Rel-17 NR Intra-band - | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210091 | 0660 |  | A | CR for 38.101-1 to add missing spurious emissions for band n38 UE co-existence (Rel-17) | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210084 | 0663 |  | A | CR to TS 38.101-1: system parameters maintenance for NR-U | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210117 | 0665 |  | A | Simplification of n70 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210074 | 0669 |  | A | CR for 38.101-1: Add CA_n25A-n41(2A)-n71A which was missing in the CR implementation | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210189 | 0670 | 1 | F | Big CR to TS 38.101-1 - New CBW Basket WI | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210117 | 0674 |  | A | CR to TS38.101-1: Correction on applicability of minimum requirements | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210117 | 0677 |  | A | CR to TS38.101-1: Correction on the Aggregated Channel Bandwidth | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210117 | 0679 |  | A | CR to TS38.101-1: Correction on configured transmitted power requirement | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210100 | 0680 | 1 | B | Rel-17 CR 38.101-1 for improvements Intra-band tables | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210101 | 0681 |  | F | Rel-17 CR 38.101-1 for corrections NR CA 2, 3 and 4 band configuration tables | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210099 | 0688 |  | B | CR for TS 38.101-1 Introduce NR SUL bands to PC3 UL-MIMO configuration | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210117 | 0690 |  | A | Missing parent clause for NR-DC PCMAX | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210117 | 0692 |  | A | Corrections to PCMAX for UL CA | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210082 | 0695 |  | A | CR CA_n7B REFSENS | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210117 | 0699 |  | A | CR for TS 38.101-1: Correction to FR1 time mask for SRS antenna switching | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210082 | 0701 |  | A | CR for TS 38.101-1: Corrections to intra-band UL NC CA requirements | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210091 | 0703 |  | A | CR for TS 38.101-1: Cleanup for spurious emissions for UE co-existence table | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210091 | 0713 |  | A | CR on TS 38.101-1 NS_49 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210176 | 0715 |  | B | CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into TS 38.101-1 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210181 | 0716 |  | B | CR to reflect the completed NR inter band CA DC combinations for 3 bands DL with 2 bands UL into TS 38.101-1 | 17.1.0 |  |
| 2021-03 | RAN#91 | RP-210101 | 0717 |  | B | Introduction of specific Pcmax requirements for inter-band CA category A-B combos | 17.1.0 |  |
| 2021-06 | RAN#92 | RP-211084 | 0736 |  | A | Update of FR1 UL RMC tables | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211104 | 0738 |  | F | CR Removal of square brackets from n48 NS_27 R17 CAT F | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211114 | 0740 |  | A | CR TDD Intraband CA REFSENS requirement issue R17 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211118 | 0745 | 1 | A | CR on PC1.5 HPUE SAR issue into Rel-17 TS 38.101-1 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211104 | 0750 |  | A | CR on spurious emission between n40 and n41 into Rel-17 TS 38.101-1 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211085 | 0751 |  | F | Simplification of n70 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211117 | 0752 | 1 | F | CR for updates related to n24 in 38.101-1 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211114 | 0755 |  | B | CR on Introducing NR inter-band CA for 3DL Bands and 1UL band for 38.101-1 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211114 | 0757 |  | A | Correction on supported channel bandwidth for CA_n39-n41-n79 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211080 | 0760 | 1 | F | Correction of an improper usage of band edge relaxation for MOP | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211085 | 0765 |  | A | CR to TS38.101-1[R17]: Addition of UE co-existence requirements for n40 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211115 | 0768 |  | B | CR for  Pcmax - NR-DC for DC cat. A-B combinations | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211114 | 0770 |  | B | Add channel bandwidth configuration for CA_n46A-n48A | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211114 | 0773 |  | B | Adding new CA_n46N-n48A configurations | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211077 | 0779 |  | A | Cleanup for UE co-existence 38.101-1 Rel-17 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211102 | 0780 | 1 | F | Correction on DL interruption applicability for inter-band CA | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211079 | 0781 |  | F | CR to TS 38.101-1 on UE channel bandwidth per operating band | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211105 | 0783 |  | A | UL MIMO coherence for Tx switching between two carriers (Rel-17) | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211115 | 0784 |  | B | CR on introduction of completed NR CA/DC combs with 4DL/2UL within FR1 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211077 | 0786 |  | A | CR to 38.101-1 for missing MSD due to receiver harmonic mixing for combos with n46 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211120 | 0787 |  | B | CR on Introduction of completed SUL band combinations into TS 38.101-1 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211115 | 0788 |  | B | CR on Introduction of completed 5 bands inter-band CA into TS 38.101-1 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211078 | 0792 |  | A | CR for updating the note of mandatory simultaneous Rx/Tx capability for FR1 NR-CA combinations | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211078 | 0800 |  | A | Correction to MPR for serving cells of intra-band UL CA | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211095 | 0802 |  | A | Corrections to BCS for n46 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211095 | 0804 |  | A | Applicability of minimum requirements for shared spectrum access | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211120 | 0805 |  | B | CR to 38.101-1 Introduce RF requirements for HPUE CA with 2 bands downlink and x bands uplink (x =1,2) | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211120 | 0806 |  | B | CR to 38.101-1 Introduce DL interruption clarification for CA conduting Tx Switching | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211115 | 0807 |  | B | Big CR to TS 38.101-1: Adding channel BW support in existing NR bands | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211116 | 0808 | 1 | B | CR to TS 38.101-1: Introduction of band n67 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211116 | 0809 | 2 | B | CR to TS 38.101-1: Introduction of band n85 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211095 | 0811 |  | A | CR to 38.101-1 with correction of NR-U 60 MHz and 80 MHz channels | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211086 | 0814 |  | F | CR for Rel-17 38.101-1 to correct some errors in Delta TIB and Delta RIB table | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211086 | 0816 |  | A | CR for 38.101-1 Rel17 corrections on power tolerance for intra-band contiguous CA | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211101 | 0821 |  | A | CR for 38.101-1 to correct AMPR value for NR V2X NS_52(Rel-17) | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211107 | 0823 |  | A | CR to TS38.101-1: Correction on configured transmitted power for NR non-contiguous CA | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211115 | 0825 |  | A | CR to TS38.101-1: Add missing CA_n1A-n3A-n78A | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211115 | 0826 |  | B | CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into TS 38.101-1 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211115 | 0827 |  | B | CR to reflect the completed NR inter band CA DC combinations for 3 bands DL with 2 bands UL into TS 38.101-1 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211095 | 0836 |  | A | Applicability of requirements for intra-band contiguous CA | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211110 | 0838 |  | A | Correction to Band n48 reference sensitivity | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211115 | 0843 |  | B | CR 38.101-1 new combinations Rel-17 NR Intra-band | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211115 | 0844 |  | B | CR 38.101-1 new combinations NR Inter-band 4 bands CA | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211115 | 0845 |  | F | CR 38.101-1 to re-introduce the 3DL/2UL configuration accidently deleted in R4-2102320 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211114 | 0847 | 1 | F | Rel-17 CR 38101-1-h10 corrections 1 band NR and 2 band NR CA | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211114 | 0848 | 1 | F | Rel-17 CR 38101-1-h10 corrections 3 band NR CA | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211115 | 0849 |  | F | CR 38101-1-h10 correction non-contiguous intra-band config table | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211110 | 0864 |  | A | CR for TS 38.101-1 update configured transmitted power for V2X (R17) | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211116 | 0870 |  | A | CR for 38.101-1-h10: Corrections to NS_12, NS_13, NS_14, NS_15 | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211114 | 0871 |  | A | CR for correction of Rel-17 NR inter-band CA DC configuration for 2DL with up to 2 bands UL | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211122 | 0872 |  | B | Big CR for 38.101, Introduce new band combinations for V2X con-current operation | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211114 | 0873 |  | F | Rel-17 CR 38101-1-g70 corrections | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211080 | 0874 |  | F | CR for 38.101-1-h10: Corrections to intra-band non-contiguous CA REFSENS | 17.2.0 |  |
| 2021-06 | RAN#92 | RP-211114 | 0875 |  | F | CR for TS 38.101-1: introduction of MSD test configurations related to IMD for inter-band combinations with intra-band UL CA as UL configuration | 17.2.0 |  |
| 2021-09 | RAN#93 | RP-211915 | 0884 |  | B | CR on Introducing NR inter-band CA for 3DL Bands and 1UL band for 38.101-1 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211909 | 0885 | 2 | B | bigCR to TS 38.101-1 - Introduction of 35MHz and 45MHz channel bandwidth | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211896 | 0888 | 1 | F | CR for updates related to NR Band n24 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211900 | 0889 |  | B | Big CR on introduction of completed NR CA/DC combs with 4DL/2UL within FR1 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211901 | 0890 | 1 | B | CR to 38.101-1 Introduce SAR solution for UE power class 2 NR inter-band CA and SUL configurations | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211901 | 0891 |  | B | CR to 38.101-1 Introduce RF requirements for HPUE CA with 2 bands downlink and x bands uplink (x =1,2) | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211902 | 0893 |  | B | CR on Introduction of completed SUL band combinations into TS 38.101-1 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211900 | 0894 |  | B | CR on Introduction of completed 5 bands inter-band CA into TS 38.101-1 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211901 | 0896 |  | F | CR to TS 38.101-1: Correction on PC2 1UL_2DL table 6.2A.1.3-2 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211900 | 0898 |  | B | Big CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into TS 38.101-1 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211900 | 0899 |  | B | Big CR to reflect the completed NR inter band CA DC combinations for 3 bands DL with 2 bands UL into TS 38.101-1 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211900 | 0903 |  | B | CR 38.101-1 new combinations Rel-17 NR Intra-band | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211900 | 0904 |  | B | CR 38.101-1 new combinations NR Inter-band 4 bands CA | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211907 | 0905 |  | B | Big CR to TS 38.101-1: Adding channel BW support in existing NR bands | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211896 | 0906 |  | B | CR for 38.101-1: Introduction of BCS4 and BCS5 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211900 | 0907 |  | F | CR for TS 38.101-1: Correcting CA frequency setup for 2UL interband reference sensitivity | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211895 | 0908 | 1 | F | CR for TS 38.101-1 Rel-17: Applying n40 and n41 spurious emissions on CA | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211910 | 0911 | 1 | B | Introduction of the UL 7.5kHz shift for NR TDD band n34 and n39 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211895 | 0912 |  | B | CR on contiguous CA with UL MIMO for power class 3 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211895 | 0913 | 1 | B | CR on PC2 intra-band UL contiguous CA RF requirements | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211897 | 0914 |  | B | CR for TS 38.101-1 Tx diversity requirementsNOTE: The CR is partly implemented. .The changes were ignored in CR0914’s regarding PC1.5 in clause 6.2.2 due to conflict with CR0915 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211901 | 0915 |  | B | CR to 38.101-1: Introduction of PC1.5 in Bands n77 and n78 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211901 | 0916 |  | B | CR to 38.101-1: Introduction of PC1.5 in Band n79 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211888 | 0917 |  | F | CR to 38.101-1: PC1.5 MPR for Band n41 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211901 | 0918 |  | B | CR to TS 38.101-1: Addition of PC2 A-MPR for NS_50 | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211921 | 0921 |  | F | Big CR for TS 38.101-1 Maintenance part1 (Rel-17) | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211907 | 0923 |  | A | Big CR for TS 38.101-1 Maintenance part2 (Rel-17) | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211900 | 0924 |  | F | Rel-17 CR 38.101-1, band combination corrections | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-211905 | 0925 |  | B | CR for updating the note of mandatory simultaneous Rx/Tx capability for Rel.17 FR1 NR-CA combinations | 17.3.0 |  |
| 2021-09 | RAN#93 | RP-212600 | 0927 | 2 | A | Introduction of NS value for distinguishing support of extended n77 | 17.3.0 |  |
| 2021-12 | RAN#94 | RP-212837 | 0930 |  | F | Clarification on applicability of RB restriction for n39 and n98 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212837 | 0932 | 1 | B | CR on PC2 UE RF requirements of n34 in Rel-17 TS 38.101-1 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212837 | 0933 |  | B | CR on PC2 UE RF requirements of n39 in Rel-17 TS 38.101-1 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212830 | 0940 |  | B | CR on Introducing NR inter-band CA for 3DL Bands and 1UL band for 38.101-1 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212826 | 0941 |  | F | CR for 38.101-1 to remove UL MIMO restriction for SUL carrier | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212833 | 0942 |  | B | CR on UE maximum output power for n1 and n3 PC2 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212825 | 0944 | 1 | B | CR for TS 38.101-1: 1024QAM | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212831 | 0945 |  | B | Big CR on introduction of completed NR CA/DC combs with 4DL/2UL within FR1 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212836 | 0947 |  | F | CR: Rel-17 38.101-1 Corrections on spurious emission band UE co-existence | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212830 | 0948 | 1 | F | CR for TS 38.101-1: MSD test configurations modification for US inter-band CA combinations with n77 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212835 | 0949 | 1 | F | CR for TS 38.101-1: Remove unsupported channel BWs for n25 and n79 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212835 | 0950 |  | B | Big CR to TS 38.101-1: Adding channel BW support in existing NR bands | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212832 | 0951 | 1 | F | CR to TS38.101-1: Correction on MSD table to apply PC2 NR inter-band CA combination | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212830 | 0952 |  | F | CR to TS38.101-1: Inter-band NR CA Tx requirement including intra-band non-contiguous CA and combinations of intra-band and inter-band CA UL configuration | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212830 | 0953 |  | B | Big CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into TS 38.101-1 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212830 | 0954 |  | B | Big CR to reflect the completed NR inter band CA DC combinations for 3 bands DL with 2 bands UL into TS 38.101-1 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212832 | 0955 |  | B | CR to 38.101-1 Introduce RF requirements for HPUE CA with 2 bands downlink and x bands uplink (x =1,2) | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212834 | 0956 |  | B | CR to 38.101-1 Introduce DL interruption clarification for CA conduting Tx Switching | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212831 | 0957 |  | B | CR on Introduction of completed SUL band combinations into TS 38.101-1 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212831 | 0958 |  | B | CR on Introduction of completed 5 bands inter-band CA into TS 38.101-1 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212830 | 0959 |  | B | CR 38.101-1 new combinations Rel-17 NR Intra-band | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212831 | 0960 |  | B | CR 38.101-1 new combinations NR Inter-band 4 bands CA | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212904 | 0961 |  | B | CR for 38.101-1 to introduce PC2 RF requirements for NR V2X | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212837 | 0973 | 1 | F | Correction to maxUplinkDutyCycle-MPE-FR1 for PC1.5 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212832 | 0974 |  | F | Correction to uplink Tx power for PC2 2UL CA MSD | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212847 | 0977 |  | A | CR to remove LO exceptions | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212832 | 0979 |  | B | CR to 38.101-1 Introduce RF requirements for HPUE CA with x (x>2) bands DL and y (y=1,2) bands UL | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212827 | 0980 |  | B | CR 38.101-1 to improve how to include BCS4 and BCS5 | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-212845 | 0983 |  | F | Big CR for TS 38.101-1 Maintenance (Rel-17) | 17.4.0 |  |
| 2021-12 | RAN#94 | RP-213687 | 0984 | 1 | B | Bandwidth class correction for DC_n46N-n48A DC_n46N-n48B DC_n46N-n48C combos | 17.4.0 |  |
| 2022-03 | RAN#95 | RP-220357 | 0990 | 1 | B | CR for introduction of the lower 6GHz unlicensed band | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220357 | 0991 | 1 | B | CR for introduction of operation in full unlicensed band 5925-7125MHz | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220342 | 0993 |  | F | CR on UL MIMO coherence for Tx switching | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220359 | 0994 |  | B | CR on Introducing NR inter-band CA for 3DL Bands and 1UL band for 38.101-1 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220359 | 0995 |  | B | Big CR to reflect the completed NR inter band CA DC combinations for 3 bands DL with 2 bands UL into TS 38.101-1 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220352 | 0996 |  | B | CR for 4 Rx antenna ports support of band n8 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220343 | 0997 |  | B | Big CR to 38.101-1 Introduce RF requirements for HPUE CA | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220343 | 0998 | 1 | B | CR to TS38101-1 Addition of MSD for FDD PC2 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220343 | 0999 | 1 | B | CR to TS38101-1 Addition of PC2 A-MPR for FDD PC2 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220359 | 1000 | 1 | F | CR to TS38101-1 Addition of DC configurations | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220359 | 1001 | 1 | F | Clarification of A-MPR/NS applicability for inter-band NR-DC | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220365 | 1002 |  | B | Formal big CR to introduce SL enhancements UE RF requirements in Rel-17 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220358 | 1003 |  | B | Big CR for 38.101-1, Introduce new band combination for V2X con-current operation | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220358 | 1004 |  | B | Big CR for 38.101-3, Introduce new band combination for V2X con-current operationNOTE: The CR is allocated to 38.101-1 but was used for 38.101-3. The changes were ignored in CR1004 since it is not the correct spec. CR 1003 is related to 38.101-1.The changes in CR1004 will be implemented in 38.101-3 due to conflict with CR numbering | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220343 | 1005 |  | B | Big CR to 38.101-1 Introduce RF requirements for HPUE CA with 2 bands downlink and x bands uplink (x =1,2) | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220347 | 1007 | 1 | B | Introduction of upper 700MHz A block into TS 38.101 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220359 | 1008 |  | B | Big CR on introduction of completed NR CA/DC combs with 4DL/2UL within FR1 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220359 | 1009 |  | B | Big CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into TS 38.101-1 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220376 | 1011 |  | B | 38.101-1: Introduction of 1900 MHz to 5G NR for RMR | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220343 | 1013 |  | F | CR to TS38.101-1: Corrections on MOP tolerance for PC2 FDD n3 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220358 | 1015 |  | B | Big CR to TS 38.101-1: Adding channel BW support in existing NR bands | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220359 | 1016 | 1 | F | CR for TS 38.101-1 Rel-17: Corrections on UE co-existence | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220359 | 1017 |  | B | CR on Introduction of completed 5 bands inter-band CA into TS 38.101-1 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220371 | 1019 | 2 | B | CR for 38.101-1 to introduce RF requirements for RedCap UE | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220344 | 1020 |  | B | CR for 38.101-1 to correct the REFSENS errors due to the new format(n41 n77 n78) (R17) | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220349 | 1021 |  | B | Big CR for TS 38.101-1 Tx diversity requirements (phase 2) | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220342 | 1022 |  | B | Big CR for TS 38.101-1 introduction of PC2 intra-band non-contiguous UL CA | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220342 | 1023 | 1 | B | Big CR for TS 38.101-1 contiguous CA with UL MIMO for power class 2 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220363 | 1024 | 1 | B | Big CR for TS38.101-1:  introduction of new UL MIMO bands | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220359 | 1025 |  | B | Big CR 38.101-1 new combinations Rel-17 NR Intra-band | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220359 | 1026 |  | B | Big CR 38.101-1 new combinations NR CA Inter-band 4DL/1UL | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220350 | 1027 |  | F | Clarification of modifiedMPR-Behavior for PC1.5 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220344 | 1030 |  | F | CR R17 TS38.101-1 on TDD REFSENS and MSDs | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220334 | 1031 |  | F | CR to R17 TS38.101-1 on MSD for CA_n5-n28 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220353 | 1032 |  | F | Big CRs to TS 38.101-1 for NR_BCS4 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220343 | 1033 |  | B | CR to TS 38.101-1 on PC1 MPR table | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220360 | 1034 |  | B | CR on UE RF requirements for DMRS bundling in TS 38.101-1NOTE: The CR was not implemented. | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220337 | 1037 |  | F | Big CR for TS 38.101-1 Maintenance Part-1 (Rel-17) | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220337 | 1039 |  | F | Big CR for TS 38.101-1 Maintenance Part-2 (Rel-17) | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220360 | 1040 |  | B | CR on measurement for DMRS bundling in TS 38.101-1 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220360 | 1041 |  | B | CR on measurement for DMRS bundling in TS 38.101-1 | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220371 | 1042 |  | B | Big CR on RedCap UE FR1-RX | 17.5.0 |  |
| 2022-03 | RAN#95 | RP-220786 | 1043 |  | C | Mandatory 70 MHz and 90 MHz RF channel bandwidth in TS 38.101-1 | 17.5.0 |  |
| 2022-06 | RAN#96 | RP-221656 | 1048 | 1 | F | V2X intra-band con-current operation | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221677 | 1049 |  | B | CR 38.101-1 DMRS for CA | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221654 | 1050 | 1 | F | CR 38101-1-h50 adding FR1 NR-CA fallbacks | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221661 | 1051 | 1 | F | CR: Update of UE capability and RRC parameter name for Tx switching | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221666 | 1053 |  | A | CR for 38.101-1-h50: Correction for n7 A-MPR (NS_46) | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221668 | 1057 |  | A | CR for 38.101-1 Rel17 Minor AMPR Corrections for n65 to account for SCS | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221671 | 1058 |  | F | CR for 38.101-1 Rel17 Minor Correction for n48 NS_27 30MHz inequality | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221695 | 1063 |  | B | Big CR for TS 38.101-1, Introduce new band combinations of V2X con-current operation | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221686 | 1064 |  | B | CR on Introducing NR inter-band CA for 3DL Bands and 1UL band for 38.101-1 | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221694 | 1065 |  | B | Big CR to 38.101-1 Introduce RF requirements for HPUE CA with 2 bands downlink and x bands uplink (x =1,2) | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221672 | 1067 | 1 | F | CR on NR-U A-MPR for PC5 VLP in South Korea | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221679 | 1070 | 1 | F | CR to TS 38.101-1: Protection for band 103 from newly introduced CA combinations | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221661 | 1071 | 1 | F | CR to TS38.101-1[R17] Some Corrections for Transmitter characteristics | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221683 | 1072 | 1 | F | CR to TS38.101-1: Some corrections for the tables due to introduction of 35MHz_45MHz CBW | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221676 | 1073 | 1 | F | CR to TS38.101-1: Corrections on Redcap requirements | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221687 | 1074 | 1 | F | CR to TS38.101-1: Corrections on MSD for PC2 FDD band | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221686 | 1075 |  | B | Big CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into TS 38.101-1 | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221671 | 1077 |  | F | Correction to additional spurious emission requirements for n48 | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221681 | 1079 | 1 | F | CR to TS38.101-1 for the corrections on Tx Diversity Requirement | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221671 | 1080 |  | B | Big CR to TS 38.101-1: Adding channel BW support in existing NR bands | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221695 | 1081 | 1 | B | Big CR to 38.101-1: update of simultaneous RxTx capability for band combinations | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221675 | 1082 |  | B | CR: Introduction of RMC for 1024QAM maximum input level | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221684 | 1083 |  | B | 38.101-1: Introduction of 900 MHz to 5G NR for RMR | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221677 | 1086 |  | B | CR on UE RF requirements for DMRS bundling in TS 38.101-1 | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221694 | 1087 |  | B | Big CR to 38.101-1 Introduce RF requirements for HPUE CA | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221686 | 1089 |  | B | Big CR on Introduction of completed SUL band combinations into TS 38.101-1 | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221686 | 1090 |  | B | Big CR on Introduction of completed 5 bands inter-band CA into TS 38.101-1 | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221694 | 1092 | 1 | F | CR for TS 38.101-1 Rel-17: Corrections on band combinations for UE co-existence | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221680 | 1098 |  | F | CR for 38.101-1 to introduce the missing requirements for BCS4 | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221677 | 1100 | 1 | F | CR on DMRS bundling phase offset measurement FR1 | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221686 | 1103 |  | B | big CR 38.101-1 new combinations Rel-17 NR Intra-band | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221686 | 1104 |  | B | big CR 38.101-1 new combinations NR CA Inter-band 4DL/1UL | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221686 | 1105 |  | B | Big CR to reflect the completed NR inter band CA DC combinations for 3 bands DL with 2 bands UL into TS 38.101-1 | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221670 | 1107 |  | B | Big CR for TS38.101-1: introduction of new UL MIMO bands | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221677 | 1110 |  | F | CR to TS 38.101-1: update of NR-V2X MPR requirements (R17) | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221694 | 1111 | 1 | B | Big CR for TS 38.101-1: Introduce high power UE for NR TDD intra-band CA in FR1 | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221673 | 1112 | 1 | B | Introduction of NR licensed band 6425 – 7125 MHzNOTE: The CR is covered in CR 1112 revision2 | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221673 | 1112 | 2 | B | Introduction of NR licensed band 6425 – 7125 MHz | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221680 | 1113 | 1 | B | Increasing the maximum power limit for inter-band UL CA | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221661 | 1116 | 1 | A | CR to R17 TS38.101-1 on transient period capability | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221661 | 1117 |  | F | CR for TS 38.101-1: Removing square brackets for Intra-band NC UL CA requirements | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221655 | 1121 |  | F | Big CR for TS 38.101-1 Maintenance Part-1 (Rel-17) | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221676 | 1123 |  | F | CR on RedCap FR1 RF | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221681 | 1124 |  | F | CR on Receiver requirements for TX diversity | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221066 | 1125 |  | F | CR for updating the note of mandatory simultaneous Rx/Tx capability for FR1 NR-CA combinations | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221067 | 1126 |  | F | CR for updating the note of mandatory simultaneous Rx/Tx capability for FR1 NR-CA combinations | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221868 | 1128 | 2 | F | CR to 38.101-1 on corrections of NS_21 requirements | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221748 | 1129 | 1 | B | CR for 38.101-1: Addition PC1.5 single uplink for 3DL combinations [NR_PC1.5_SingleUL_3DLCA] | 17.6.0 |  |
| 2022-06 | RAN#96 | RP-221789 | 1130 | 1 | C | Extension of operation in the n77 frequency range in Canada [n77 Canada] | 17.6.0 |  |
| 2022-09 | RAN#97 | RP-222032 | 1135 | 1 | F | CR: Maintenance of phase continuity requirements for DMRS bundling in FR1 | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222032 | 1136 | 1 | F | V2X corrections | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222050 | 1137 |  | F | CR to R17 38.101-1 to correct NR-U 100MHz UL configuration | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222050 | 1138 |  | D | CR to R17 38.101-1 to correct table number for UL MIMO NR-U section | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222032 | 1139 | 1 | F | CR for TS 38.101-1, Correction of configured transmitted power for V2X | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222032 | 1140 | 1 | F | NR Band n14 PC1 MPR for NR Sidelink Operation | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222028 | 1143 | 1 | F | CR 38.101-1: Rel-17 Adding missing fallback combinations and bug fixes | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222036 | 1145 |  | F | CR for TS 38.101-1 Rel-17: Introducing missing UE coex requirements for CA_n7-n79 | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222034 | 1148 |  | F | CR to 38.101-1: Corrections on Pcmax for TxD | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222036 | 1149 | 1 | F | CR to 38.101-1: Corrections on Pcmax for intra-band contiguous CA with UL MIMO | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222033 | 1150 | 1 | F | CR to 38.101-1 Maintenance for HPUE CA with 2 bands downlink and x bands uplink (x =1,2) | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222036 | 1151 |  | F | Removal of [] for Reference Sensitivity Degradation of PC2 FDD band | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222036 | 1152 |  | F | Corrections on the MSD tables for inter-band NR CA | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222034 | 1155 |  | F | Maintanence of NR TxD Tx requirements | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222036 | 1157 | 1 | F | CR 38.101-1 for editorial corrections to band combination tables | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222032 | 1158 |  | F | CR for 38.101-1 to correct the errors for FR1 RedCap UE | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222050 | 1159 |  | F | CR for 38.101-1 to update the requirements for V2X con-current band combinations | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222036 | 1160 | 1 | F | CR for 38.101-1 to introduce the missing MSD due to cross band isolation | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222036 | 1161 | 1 | F | CR for 38.101-1 to clarify the ambiguity of BCS4 and BCS5 | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222023 | 1162 |  | A | Mirror CR for 38.101-1 to clarify the applicability of requirements for NS_xxU | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222023 | 1164 |  | F | CR to 38.101-1 Corrections to tables with wrong unit declarations | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222036 | 1165 | 1 | F | NOTE: The CR is allocated to 38.101-1 but the title on the coversheet is wrong as it says spec TS 38.101-3. This 38.101-1 CR. can not be implemented. | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222032 | 1167 | 1 | F | CR on RedCap RF to add section 6.1I | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222036 | 1169 | 1 | F | Correction to RF requirements of NR_RF_FR1_enh | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222032 | 1173 | 1 | F | CR TS 38.101-1: Correction on NR V2X requirements in TS 38.101-1 | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222028 | 1174 |  | F | CR for TS 38.101-1 on corrections to MOP band edge relaxation for intra-band contiguous and non-contiguous CA band combinations | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222050 | 1177 |  | F | CR to R17 TS38.101-1 on corrections to NRU 100MHz MPR | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222034 | 1180 | 1 | F | CR for 38.101-1: Corrections for PC2 MPR and PC1.5 fallback to PC2 MPR | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222036 | 1181 | 1 | B | CR for 38.101-1: Missing combinations for NR-CA | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222050 | 1182 | 1 | B | CR for 38.101-1: Addition of 5 MHz channel BW for n41 | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222032 | 1184 | 1 | F | CR 38.101-1 DMRS DL CA | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222028 | 1187 |  | D | Editorial clean-up | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222032 | 1188 |  | F | CR: Correction of DMRS bundling requirements for FR1 CA | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222023 | 1192 |  | F | Big CR for 38.101-1 maintenance part1 (Rel-17) | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222023 | 1194 |  | F | Big CR for 38.101-1 maintenance part2 (Rel-17) | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222686 | 1196 | 1 | A | Extension of operation in the n77 frequency range in US [n77 US] | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222683 | 1197 | 2 | C | Extension of operation in the n77 frequency range in Canada [n77 Canada] | 17.7.0 |  |
| 2022-09 | RAN#97 | RP-222490 | 1198 |  | F | CR to 38.101-1 on new NS for Canadian WCS regulation R17 | 17.7.0 |  |
| 2022-12 | RAN#98-e | RP-223298 | 1199 |  | B | Introduction of intra band NC UL CA in the n77 frequency range in Canada [n77 Canada] | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223307 | 1200 | 1 | F | Corrections on the definition of RedCap UE | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223306 | 1202 | 1 | F | CR on clarification for DMRS bundling RF requirements for SUL in TS 38.101-1 | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223308 | 1205 | 3 | F | CR to clarify UE requirements for DMRS bundling | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223311 | 1206 |  | F | CR for TS 38.101-1, Correction of maximum configured power for PSFCH in Rel-17 sidelink enhancement | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223290 | 1210 |  | A | Addition of FR1 UL MIMO EVM measurement description | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223290 | 1213 |  | A | Addition of FR2 UL MIMO EVM measurement descriptionNote: The CR was not implementable and therefore was not implemented in the specification. | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223309 | 1216 |  | F | CR correction to n100 and n101 UE to UE coexsistence tables and revoval of brackets | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223295 | 1218 | 1 | A | Addition of CA_n77-n78 to CA Band table R17 | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223297 | 1220 |  | A | Correction to n91,n92,n93 and n94 co-ex R17 | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223310 | 1223 |  | F | Definition of Window lengths for 35 and 45 MHz channel bandwidths | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223296 | 1225 |  | A | CR for TS 38.101-1 Rel-17 CAT-A: Correcting critical error with co-existence for band CA_n8-n40 | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223291 | 1226 | 1 | F | CR for TS 38.101-1 Rel-17: Corrections on band combinations for UE co-existence | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223309 | 1230 |  | F | CR on NR-U A-MPR for PC5 VLP | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223290 | 1233 |  | F | Rel17 Cat F CR Correct the DL configuration for harmonic MSD for CA_n12-n66 and CA_n25-n71 | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223481 | 1238 | 4 | A | Clarification of the CA_NS indication the values for n77 in the US [n77 US] | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223308 | 1242 |  | F | CR to R17 TS38.101-1 maintenance for UE co-ex requirements for UL CA | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223309 | 1245 | 2 | F | CR to 38.101-1: 4 Rx support for n104 | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223311 | 1246 |  | F | Correction on the HigherPowerLimitCADC and powerClassPerBand IE | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223298 | 1251 | 1 | F | CR for corrections on Rel-17 band combinations in TS38.101-1 | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223296 | 1253 |  | A | CR to 38.101-1 on removing ambiguity in CA MPR definition | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223308 | 1254 |  | F | CR for 38.101-1: introduce UL MIMO configurations for band n40 | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223309 | 1262 | 1 | F | CR TS38.101-1 R17 Re-construct NR-U clause structure and introduce missing requirements | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223291 | 1263 | 1 | F | CR TS38.101-1 R17 Corrections to Cross-band isolation and Rx harmonic mixing MSD | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223291 | 1267 |  | A | CR on ‘Annex G Difference of relative phase and power errors’ for FR1 UL coherent MIMO | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223291 | 1270 |  | A | CR on TDD RMC for Intra-band EN-DC - TS 38.101-1 | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223308 | 1273 | 1 | F | CR for 38.101-1 DMRS bundling with FR1 uplink CA | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223308 | 1275 |  | F | CR for 38.101-1: Corrections for 5 MHz for n41 and other errors | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223308 | 1276 |  | F | CR for 38.101-1: NR CA table corrections | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223308 | 1278 |  | F | CR for updating the note of mandatory simultaneous Rx/Tx capability for FR1 NR-CA combinations | 17.8.0 |  |
| 2022-12 | RAN#98-e | RP-223308 | 1279 |  | F | CR for 38.101-1 for DC location R17 method | 17.8.0 |  |

| Change history |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Date | Meeting | TDoc | CR | Rev | Cat | Subject/Comment | New version |
| 2022-12 | RAN#98-e | RP-223315 | 1207 | 1 | B | CR related to Introduction of new LTE TDD Band in 1670 – 1675 MHz | 18.0.0 |
| 2022-12 | RAN#98-e | RP-223328 | 1217 |  | B | Big CR for FWA MPR and A-MPR for n71 and n85 | 18.0.0 |
| 2022-12 | RAN#98-e | RP-223331 | 1227 |  | B | Big CR to 38.101-1 Introduce RF requirements for HPUE inter- band CA with y(y=2,3,4) bands downlink and x bands uplink (x =1,2) | 18.0.0 |
| 2022-12 | RAN#98-e | RP-223333 | 1228 |  | B | Big CR for TS 38.101-1, Introduction of new R18 Uu+V2X band combinations | 18.0.0 |
| 2022-12 | RAN#98-e | RP-223332 | 1232 |  | B | BigCR for High power UE for inter-band CA with power class 2 on single carrier uplink on FDD band | 18.0.0 |
| 2022-12 | RAN#98-e | RP-223324 | 1244 |  | B | big CR 38.101-1 new combinations Rel-18 NR Intra-band | 18.0.0 |
| 2022-12 | RAN#98-e | RP-223326 | 1247 |  | B | big CR 38.101-1 new combinations Rel-18 NR Inter-band CA/DC for y bands DL with x bands UL (y=4,5,6, x=1,2) | 18.0.0 |
| 2022-12 | RAN#98-e | RP-223325 | 1248 |  | B | Big CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into TS 38.101-1 | 18.0.0 |
| 2022-12 | RAN#98-e | RP-223329 | 1250 |  | B | Big CR on TS38.101-1 Addition of intra-band CA Combinations with PC2 and PC1.5 | 18.0.0 |
| 2022-12 | RAN#98-e | RP-223318 | 1255 |  | B | Big CR for 38.101-1 introduce UL MIMO configurations for Rel-18 | 18.0.0 |
| 2022-12 | RAN#98-e | RP-223327 | 1256 |  | B | Big CR on Introduction of completed SUL band combinations into TS 38.101-1 | 18.0.0 |
| 2022-12 | RAN#98-e | RP-223325 | 1264 |  | B | Big CR to reflect the completed NR inter-band CA DC combinations for  3 bands DL with x bands UL (x=1,2) into TS 38.101-1 | 18.0.0 |
| 2022-12 | RAN#98-e | RP-223319 | 1280 |  | B | Introduction of APT 600 MHz band | 18.0.0 |
| 2023-03 | RAN#99 | RP-230527 | 1281 |  | F | Updates to spurious emissions UE coexistence table | 18.1.0 |
| 2023-03 | RAN#99 | RP-230535 | 1282 |  | B | CR related to Introduction of NR TDD Band n54 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230519 | 1289 |  | A | CR TS 38.101-1: Correction on NR V2X requirements in Rel-18 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230605 | 1294 | 1 | B | UE RF requirements for supporting intra-band non-collocated CA for 2MIMO layer case | 18.1.0 |
| 2023-03 | RAN#99 | RP-230501 | 1296 |  | A | CR for TS 38.101-1 Rel-18: Adding missing harmonic mixing MSD for CA_n25-n71 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230517 | 1298 |  | A | TS 38.101-1 Rel-18 CAT-A: Correction to co-existence requirements of band n8 and n100 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230504 | 1300 |  | A | CR for TS 38.101-1 Rel-18 CAT-A: Corrections on band combinations for UE co-existence | 18.1.0 |
| 2023-03 | RAN#99 | RP-230507 | 1302 |  | A | CR for TS 38.101-1 Rel-18 CAT-A: Correction to NRU spectrum emission mask | 18.1.0 |
| 2023-03 | RAN#99 | RP-230501 | 1305 |  | A | CR for TS 38.101-1 Rel-18: Correction for wrong reference in NS_50 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230544 | 1309 | 1 | F | CR 38.101-1: Rel-18 Band combinations bug fixing and adding missing fallbacks | 18.1.0 |
| 2023-03 | RAN#99 | RP-230512 | 1313 |  | A | CR to 38.101-1: Correction of PC1 ACLR definition R18 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230544 | 1315 |  | A | NR CA corrections R18 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230513 | 1317 |  | A | CR 38.101-1 correction to A-MPR for NS_24 R18 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230549 | 1318 |  | B | Big CR for High-power UE operation for fixed-wireless/vehicle-mounted use cases in LTE bands and NR bands | 18.1.0 |
| 2023-03 | RAN#99 | RP-230549 | 1320 |  | A | CR to 38.101-1: Corection to PC1 UTRA ACLR for bands n71 and n85. | 18.1.0 |
| 2023-03 | RAN#99 | RP-230502 | 1324 |  | A | Addition of configuration for carrier aggregation RMCs | 18.1.0 |
| 2023-03 | RAN#99 | RP-230516 | 1328 | 1 | A | CR to introduce emissions specifications for certain LTE_V2X band combinations | 18.1.0 |
| 2023-03 | RAN#99 | RP-230509 | 1338 |  | A | Clarification of the CA_NS indication and NS values for n77 in Canada [n77 Canada] | 18.1.0 |
| 2023-03 | RAN#99 | RP-230547 | 1339 |  | B | Big CR for NR CA band combinations with two SUL cells in Rel-18 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230519 | 1341 |  | A | CR for 38.101-1 Corrections to the section 6.2D | 18.1.0 |
| 2023-03 | RAN#99 | RP-230558 | 1342 |  | B | Big CR to 38.101-1 Introduce DL interruption clarification for CA conduting Tx Switching | 18.1.0 |
| 2023-03 | RAN#99 | RP-230519 | 1345 |  | F | CR on NR-U A-MPR for PC5 VLP in NS_61 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230543 | 1346 |  | B | big CR 38.101-1 new combinations Rel-18 NR Intra-band | 18.1.0 |
| 2023-03 | RAN#99 | RP-230519 | 1350 |  | A | Rel18 Cat A CR Introduce the missing Pcmax tolerance requirement for PC2 intra-band NC UL CA | 18.1.0 |
| 2023-03 | RAN#99 | RP-230519 | 1352 |  | A | Rel18 Cat A CR Add verification clarification for OOB emission and SE emission for intra-band NC UL CA | 18.1.0 |
| 2023-03 | RAN#99 | RP-230502 | 1355 |  | A | Rel18 Cat A CR Correct the wrong table and clause that clause 6.2A.3.1.1 refer to | 18.1.0 |
| 2023-03 | RAN#99 | RP-230504 | 1359 | 1 | A | CR to clarify duplex mode of SDL bands | 18.1.0 |
| 2023-03 | RAN#99 | RP-230501 | 1362 |  | A | CR to add band n29 to blocking requirements | 18.1.0 |
| 2023-03 | RAN#99 | RP-230507 | 1373 |  | A | Correct the scaling number for MPR/A-MPR and NS_04 SEM requirement | 18.1.0 |
| 2023-03 | RAN#99 | RP-230519 | 1375 |  | A | Correct the Pcmax for intra-band non-contiguous CA to support HPUE | 18.1.0 |
| 2023-03 | RAN#99 | RP-230544 | 1376 |  | B | Big CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into TS 38.101-1 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230562 | 1377 |  | B | Big CR to reflect the completed 4Rx support for NR FR1 bands (<2.6GHz) into TS 38.101-1 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230519 | 1378 |  | A | CR to 38.101-1 R18 corrections on A-MPR for CA_NC_NS_04 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230502 | 1381 |  | A | CR on Harmonic mixing MSD for CA_n8A-n79A (R18 CAT-A) | 18.1.0 |
| 2023-03 | RAN#99 | RP-230559 | 1384 |  | B | Big CR to TS 38.101-1: Adding channel BW support in existing NR bands | 18.1.0 |
| 2023-03 | RAN#99 | RP-230546 | 1385 |  | B | big CR 38.101-1 NR Inter-band CA/DC for y bands DL (y=4, 5, 6) with x bands UL (x=1, 2) | 18.1.0 |
| 2023-03 | RAN#99 | RP-230514 | 1386 |  | A | Frequency range definition update for TS 38.101-1 (Rel-18) | 18.1.0 |
| 2023-03 | RAN#99 | RP-230519 | 1393 |  | A | Clarification on Time mask for Tx switching for SA (Rel-18) | 18.1.0 |
| 2023-03 | RAN#99 | RP-230503 | 1400 |  | A | CR for Rel-18 38.101-1 to correct the configurations for CA_n46M/N/O | 18.1.0 |
| 2023-03 | RAN#99 | RP-230532 | 1401 |  | B | Big CR for 38.101-1 introduce UL MIMO configurations for Rel-18 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230547 | 1403 |  | B | Big CR on Introduction of completed SUL band combinations into TS 38.101-1 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230549 | 1405 |  | B | Big CR for Rel-18 Simultaneous Rx/Tx inter-band combinations | 18.1.0 |
| 2023-03 | RAN#99 | RP-230513 | 1407 |  | A | CR for TS 38.101-1 to correct the delta MPR (R18) | 18.1.0 |
| 2023-03 | RAN#99 | RP-230503 | 1411 |  | A | CR for TS 38.101-1 to clarify the inner outer condition for almost contiguous RB allocation (R18) | 18.1.0 |
| 2023-03 | RAN#99 | RP-230501 | 1414 |  | A | CR for TS 38.101-1 to clarify band n34 protection for band n1 and n65 (R18) | 18.1.0 |
| 2023-03 | RAN#99 | RP-230501 | 1417 |  | A | CR for TS 38.101-1 to clarify Out-of-band blocking exception for band n20 and n28 (R18) | 18.1.0 |
| 2023-03 | RAN#99 | RP-230552 | 1418 |  | B | Big CR on TS38.101-1 Addition of intra-band CA Combinations with PC2 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230501 | 1427 |  | A | Additional maximum power reduction for NS_21 (Rel-18) | 18.1.0 |
| 2023-03 | RAN#99 | RP-230513 | 1430 |  | A | CR for 38.101-1: Band combination corrections (Rel-18 Cat A) | 18.1.0 |
| 2023-03 | RAN#99 | RP-230519 | 1432 |  | A | CR for 38.101-1: Clarification of PC1.5 requirements (Rel-18 Cat A) | 18.1.0 |
| 2023-03 | RAN#99 | RP-230503 | 1436 |  | A | CR to TS 38.101-1 on humidity condition for normal temperature | 18.1.0 |
| 2023-03 | RAN#99 | RP-230545 | 1439 |  | B | Big CR to reflect the completed NR inter-band CA DC combinations for  3 bands DL with x bands UL (x=1,2) into TS 38.101-1 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230516 | 1441 |  | A | CR for TS 38.101-1 on cleanups for V2X operating bands and channel bandwidth (R18_CAT_A) | 18.1.0 |
| 2023-03 | RAN#99 | RP-230504 | 1459 |  | A | Output power for NS_38, NS_40, and NS_41 | 18.1.0 |
| 2023-03 | RAN#99 | RP-230504 | 1464 | 1 | A | CR to TS 38.101-1 Rel-18 Minimum guardband and missing ULCA power class | 18.1.0 |
| 2023-03 | RAN#99 | RP-230533 | 1467 |  | F | Corection to Band n105 in coexistence table | 18.1.0 |
| 2023-03 | RAN#99 | RP-230519 | 1469 |  | A | CR for TS 38.101-1, Correction of minor errors in suffix E (NR V2X/Sidelink) requirements | 18.1.0 |
| 2023-03 | RAN#99 | RP-230501 | 1471 |  | A | CR to TS 38.101-1 Rel-18 4Rx for SUL | 18.1.0 |
| 2023-03 | RAN#99 | RP-230519 | 1472 |  | A | CR to update NS_50 PC2 A-MPR | 18.1.0 |
| 2023-03 | RAN#99 | RP-230507 | 1475 |  | F | CR to return he Eq1 for intra-band UL CA contiguous | 18.1.0 |
| 2023-03 | RAN#99 | RP-230554 | 1476 |  | B | Big CR for 38.101-1 on High power UE for FR1 NR inter-band CA/DC or SUL band combination with y DL-x UL and PCm (m<3) and high power on TDD | 18.1.0 |
| 2023-06 | RAN#100 | RP-231355 | 1484 |  | F | CR to K1 and PdschNumOfHarqProcess for DL-CA | 18.2.0 |
| 2023-06 | RAN#100 | RP-231356 | 1488 |  | A | FR1 OOB requirements correction | 18.2.0 |
| 2023-06 | RAN#100 | RP-231343 | 1501 |  | A | Update to UL-MIMO requirements  (Rel-18) | 18.2.0 |
| 2023-06 | RAN#100 | RP-231350 | 1504 |  | A | CR to correct the A-MPR table for NS_05/NS_05U | 18.2.0 |
| 2023-06 | RAN#100 | RP-231389 | 1505 | 1 | B | CR for 38.101-1: Time mask for switching across three or four uplink bands | 18.2.0 |
| 2023-06 | RAN#100 | RP-231384 | 1513 |  | B | BigCR for High power UE for inter-band CA with power class 2 on single carrier uplink on FDD band | 18.2.0 |
| 2023-06 | RAN#100 | RP-231377 | 1515 |  | B | Big CR on Introduction of completed SUL band combinations into TS 38.101-1 | 18.2.0 |
| 2023-06 | RAN#100 | RP-231348 | 1517 |  | A | CR for TS 38.101-1 to modify the errors in table 7.6.4-1 due to the introduction of equation-based method (R18) | 18.2.0 |
| 2023-06 | RAN#100 | RP-231343 | 1519 |  | A | CR for TS 38.101-1 to modify the errors for SUL_n78A-n80A configuration (R18) | 18.2.0 |
| 2023-06 | RAN#100 | RP-231367 | 1521 |  | F | On RF requirements for intra-band non-collocated CA | 18.2.0 |
| 2023-06 | RAN#100 | RP-231355 | 1531 |  | A | CR to TS38.101-1 Correction to out-of-band blocking table | 18.2.0 |
| 2023-06 | RAN#100 | RP-231374 | 1534 |  | F | NR interband 2UL CA co-ex simplication R18 | 18.2.0 |
| 2023-06 | RAN#100 | RP-231378 | 1535 | 1 | B | Big CR for FWA HPUE | 18.2.0 |
| 2023-06 | RAN#100 | RP-231383 | 1538 |  | B | Big CR to 38.101-1 new combinations for Rel-18 NR HPUE Inter-band | 18.2.0 |
| 2023-06 | RAN#100 | RP-231375 | 1539 | 1 | B | Big CR to reflect the completed NR inter-band CA DC combinations for  3 bands DL with x bands UL (x=1,2) into TS 38.101-1 | 18.2.0 |
| 2023-06 | RAN#100 | RP-231355 | 1543 |  | A | CR for TS 38.101-1 on corrections to the minimum guardband calculation (R18_CAT_A) | 18.2.0 |
| 2023-06 | RAN#100 | RP-231351 | 1546 |  | A | Rel-18 CR to 38 101-1 for Clarification of UL Tx Switching | 18.2.0 |
| 2023-06 | RAN#100 | RP-231355 | 1549 |  | A | Rel18 Cat A CR for 38.101-1 Correct the MSD test configuration for CA_n18-n41 | 18.2.0 |
| 2023-06 | RAN#100 | RP-231343 | 1554 |  | A | CR to TS38.101-1: Generalize the increase higher power limit requirements for current CA band combinations | 18.2.0 |
| 2023-06 | RAN#100 | RP-231355 | 1557 |  | A | CR to TS38.101-1: Correction on terms for NR DC Pcmax | 18.2.0 |
| 2023-06 | RAN#100 | RP-231374 | 1558 |  | B | CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into TS 38.101-1 | 18.2.0 |
| 2023-06 | RAN#100 | RP-231379 | 1560 |  | B | CR on PC 1.5 for FR1 TDD single bands | 18.2.0 |
| 2023-06 | RAN#100 | RP-231385 | 1565 |  | B | Big CR to TS 38.101-1: Adding channel BW support in existing NR bands | 18.2.0 |
| 2023-06 | RAN#100 | RP-231356 | 1569 |  | A | CR for Rel-18 38.101-1 to correct CA_n46N_BCS0 to  CA_n46N_BCS1 for inter-band CA including CA_n46N | 18.2.0 |
| 2023-06 | RAN#100 | RP-231368 | 1570 |  | B | Big CR for 38.101-1 introduce UL MIMO configurations for Rel-18 | 18.2.0 |
| 2023-06 | RAN#100 | RP-231349 | 1577 |  | F | CR to 38.101-1 add the missing additional spurious emissions for CA_n5B | 18.2.0 |
| 2023-06 | RAN#100 | RP-231350 | 1581 |  | A | CR to TS38.101-1 on corrections for DMRS bundling with Tx Switching (Rel-18) | 18.2.0 |
| 2023-06 | RAN#100 | RP-231388 | 1585 | 1 | F | CR for TS 38.101-1 Rel-18 CAT-F: Corrections on band combinations for UE co-existence | 18.2.0 |
| 2023-06 | RAN#100 | RP-231351 | 1588 |  | A | CR for TS 38.101-1: Adding missing requirements for NR-U Rel-18 CAT-A | 18.2.0 |
| 2023-06 | RAN#100 | RP-231351 | 1590 |  | A | CR for TS 38.101-1: Adding missing requirements for NR-U Rel-18 CAT-A | 18.2.0 |
| 2023-06 | RAN#100 | RP-231343 | 1591 | 2 | B | Introduction of enhancements for unlicensed access to 38.101-1 | 18.2.0 |
| 2023-06 | RAN#100 | RP-231375 | 1592 |  | F | CR for 38.101-1 18.1.0 Bug fixes for CA/DC tables | 18.2.0 |
| 2023-06 | RAN#100 | RP-231377 | 1595 |  | F | CR for 38.101-1: Single SUL CA combination notation modifications | 18.2.0 |
| 2023-06 | RAN#100 | RP-231356 | 1599 |  | A | Update of FR1 UL MIMO EVM measurement description | 18.2.0 |
| 2023-06 | RAN#100 | RP-231356 | 1605 |  | A | CR to 38.101-1 Rel-18 Cat A, FRC correction | 18.2.0 |
| 2023-06 | RAN#100 | RP-231349 | 1610 |  | A | CR to 38.101-1 Rel-18 Cat A,   Missing MSD correction | 18.2.0 |
| 2023-06 | RAN#100 | RP-231343 | 1615 |  | A | CR to clarify DC location wording | 18.2.0 |
| 2023-06 | RAN#100 | RP-231381 | 1616 |  | B | Big CR on TS38.101-1 Addition of intra-band CA Combinations | 18.2.0 |
| 2023-06 | RAN#100 | RP-231338 | 1617 | 1 | F | CR on R18 TS38.101-1 Modification on the PC2 and PC1.5 note on the CA configuration with UL single carrier | 18.2.0 |
| 2023-06 | RAN#100 | RP-231373 | 1618 |  | B | big CR 38.101-1 new combinations Rel-18 NR Intra-band | 18.2.0 |
| 2023-06 | RAN#100 | RP-231383 | 1622 |  | A | CR to TS 38.101-1 (Rel-18): Alignment of PC2 uplink/downlink frequency locations to PC3 in configuration | 18.2.0 |
| 2023-06 | RAN#100 | RP-231383 | 1625 |  | A | CR to TS 38.101-1 (Rel-18): Correction of an invalid channel bandwidth in 3DL/2UL inter-band reference sensitivity testing for both PC3 and PC2 | 18.2.0 |
| 2023-06 | RAN#100 | RP-231376 | 1627 |  | B | big CR 38.101-1 new combinations Rel-18 NR Inter-band CA/DC for y bands DL with x bands UL (y=4,5,6, x=1,2) | 18.2.0 |
| 2023-06 | RAN#100 | RP-231385 | 1630 | 1 | F | CR 38.101-1 for correction of Notes in Table 5.3.5-1 | 18.2.0 |
| 2023-06 | RAN#100 | RP-231356 | 1635 |  | F | CR for 38.101-1: Foob clarification and n5 and n26 protection for B26/n26 | 18.2.0 |
| 2023-06 | RAN#100 | RP-231342 | 1636 |  | A | CR on PC2 for adding note to CA_n77C and CA_n78C | 18.2.0 |
| 2023-06 | RAN#100 | RP-231349 | 1637 |  | A | CR on MSD for shared spectrum band | 18.2.0 |
| 2023-06 | RAN#100 | RP-231389 | 1638 |  | B | CR for 38.101-1 to clarify the time mask for switching with multiple TAGs | 18.2.0 |
| 2023-06 | RAN#100 | RP-231343 | 1639 |  | B | Addition of 30 KHz SCS for Sync Raster for Band n53 | 18.2.0 |
| 2023-06 | RAN#100 | RP-231386 | 1640 |  | B | Big CR for TS 38.101-1 Rel-18 Simultaneous Rx/Tx inter-band combinations | 18.2.0 |
| 2023-09 | RAN#101 | RP-232521 | 1642 |  | B | Big CR to 38.101-1 new combinations for Rel-18 NR HPUE Inter-band | 18.3.0 |
| 2023-09 | RAN#101 | RP-232520 | 1643 |  | B | big CR 38.101-1 new combinations Rel-18 NR Intra-band | 18.3.0 |
| 2023-09 | RAN#101 | RP-232505 | 1644 |  | F | CR to TS 38.101-1 Rel-18 Corrections to UE co-existence requirements | 18.3.0 |
| 2023-09 | RAN#101 | RP-232505 | 1646 | 1 | A | CR to TS 38.101-1 Rel-18 Introduction of TDD uplink RMC for shorter transients | 18.3.0 |
| 2023-09 | RAN#101 | RP-232505 | 1649 | 1 | A | CR to TS 38.101-1 Rel-18 SUL MSD alignment | 18.3.0 |
| 2023-09 | RAN#101 | RP-232505 | 1651 | 1 | F | CR to TS 38.101-1 Rel-18 Corrections to cross-band MSD and CA_n7-n38 fallback | 18.3.0 |
| 2023-09 | RAN#101 | RP-232505 | 1653 |  | F | CR to TS 38.101-1 Rel-18 Removing triple uplink configurations and corrections to 2UL CA exceptions | 18.3.0 |
| 2023-09 | RAN#101 | RP-232520 | 1655 | 1 | F | CR for 38.101-1 18.2.0 Bug fixes for CA/DC tables | 18.3.0 |
| 2023-09 | RAN#101 | RP-232487 | 1659 |  | A | CR for TS 38.101-1 Rel-18 CAT-A: Introducing modification for NS_43 A-MPR region | 18.3.0 |
| 2023-09 | RAN#101 | RP-232499 | 1660 | 1 | F | [NR_unlic_enh-Core] CR for TS 38.101-1 Rel-18: Corrections to NS_53 A-MPR for 100MHz | 18.3.0 |
| 2023-09 | RAN#101 | RP-232490 | 1662 |  | A | CR for TS 38.101-1 Rel-18 CAT-A: Adding missing channel bandwidth for NS_01 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232504 | 1666 |  | A | CR to clarify pi2BPSK note | 18.3.0 |
| 2023-09 | RAN#101 | RP-232489 | 1671 |  | A | [NR_CADC_R16_2BDL_xBUL] Correction of a note number for CA_n77A-n78A (R18) | 18.3.0 |
| 2023-09 | RAN#101 | RP-232525 | 1674 |  | A | [TEI18] CR 38.101-1: Various maintenance issues R18 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232515 | 1677 | 1 | B | CR to 38.101-1 Introduction of dedicated spectrum less than 5MHz for FR1 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232498 | 1680 | 1 | A | [NR_RF_FR1-Core] Correction to EVM measurement point for DFTs-OFDM DM-RS Type 2 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232521 | 1683 |  | B | BigCR for High power UE for FDD single band PC2 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232520 | 1685 |  | A | Correction of band n77 channel bandwidth in configuration 2DL/2UL inter-band harmonic mixing testing for PC3 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232520 | 1687 |  | A | Correction of n48 channel bandwidth in configuration for PC3 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232487 | 1692 |  | A | CR for 38101-1: Almost contiguos NBC change reversal | 18.3.0 |
| 2023-09 | RAN#101 | RP-232498 | 1695 |  | A | CR for 38.101-1: CA_NS_27 and CA_NS_46 fix | 18.3.0 |
| 2023-09 | RAN#101 | RP-232520 | 1696 |  | B | Big CR for NR CA band combinations with two SUL cells in Rel-18 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232525 | 1697 | 1 | B | CR for TS 38.101-1: Adding asymmetric channel bandwidth of UL 15/ DL 35 MHz for n66 [n66_asymBW] | 18.3.0 |
| 2023-09 | RAN#101 | RP-232513 | 1702 | 1 | F | Correction of applicability of time mask for Tx swtiching with dual TAG | 18.3.0 |
| 2023-09 | RAN#101 | RP-232489 | 1704 |  | A | [NR_CADC_R17_2BDL_xBUL-Core]CR for missing MSD due to 4th order harmonic mixing requirements | 18.3.0 |
| 2023-09 | RAN#101 | RP-232505 | 1710 |  | A | CR to TS 38.101-1: correction of Pcmax tolerance for 2Tx (Rel-18) | 18.3.0 |
| 2023-09 | RAN#101 | RP-232489 | 1716 |  | A | [NR_CADC_R17_2BDL_xBUL-Core ] CR on MSD for shared spectrum band | 18.3.0 |
| 2023-09 | RAN#101 | RP-232486 | 1718 |  | A | [NR_6GHz-Core] CR to 38.101-1: applicability note for n104 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232489 | 1720 |  | A | [NR_DL1024QAM_FR1-Core] CR to 38.101-1: correction of FRC reference for maximum input level for 1024 QAM R18 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232520 | 1721 |  | B | Big CR to reflect the completed NR inter band CA DC combinations for 2 bands DL with up to 2 bands UL into TS 38.101-1 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232522 | 1722 |  | B | CR to reflect the completed 4Rx support for NR FR1 bands (<2.6GHz) into TS 38.101-1 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232520 | 1723 |  | B | Big CR to reflect the completed NR inter-band CA DC combinations for  3 bands DL with x bands UL (x=1,2) into TS 38.101-1 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232487 | 1730 |  | A | CR for Rel-18 38.101-1 to correct the superscript and some notes for 2 bands inter-band CA related to simultaneous Rx/Tx. | 18.3.0 |
| 2023-09 | RAN#101 | RP-232502 | 1735 |  | A | [NR_newRAT-Core]Editorial modification CR for TS 38.101-1_V2 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232498 | 1736 |  | A | [NR_RF_FR1_enh-Core] Editorial modification CR for TS 38.101-1 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232498 | 1738 |  | A | [NR_RF_FR1_enh] Supplementation of HPUE SAR schemes for Intra-band UL CA requirements (R18) | 18.3.0 |
| 2023-09 | RAN#101 | RP-232496 | 1739 |  | A | [NR_RF_TxD] Editorial modification CR for TS 38.101-1 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232499 | 1743 |  | A | CR for correcting the SEM for intra-band contiguous CA operation | 18.3.0 |
| 2023-09 | RAN#101 | RP-232503 | 1750 |  | A | [NR_newRAT-Perf] CR: Correction of FRC for maximum input level for 256QAM | 18.3.0 |
| 2023-09 | RAN#101 | RP-232489 | 1753 |  | A | [NR_CADC_R16_2BDL_xBUL-Core] CR to 38.101-1 R18 add the missing Tx requirement for CA_n25-n71 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232501 | 1758 |  | A | [NR_newRAT-Core] CR for TS 38.101-1 to modify MSD due to harmonic mixing interference (R18) | 18.3.0 |
| 2023-09 | RAN#101 | RP-232496 | 1760 |  | A | NR_SAR_PC2_interB_SUL_2BUL]Rel18 Cat A CR for 38.101-1 Correct ?PPowerClass,CA relevant requirement in clause 6.2A.1.3 for inter-band ULCA | 18.3.0 |
| 2023-09 | RAN#101 | RP-232486 | 1763 |  | A | [NR_6GHz_unlic_full] CR 38.101-1 correction to A-MPR requirements_R18 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232503 | 1768 |  | A | [NR_RF_FR1-Core] Editorial correction to 6.2A.4 (Rel-18) | 18.3.0 |
| 2023-09 | RAN#101 | RP-232488 | 1771 |  | A | [NR_cov_enh-Core] Update of FR1 DMRS bundling measurements | 18.3.0 |
| 2023-09 | RAN#101 | RP-232518 | 1772 |  | B | Big CR for 38.101-1 introduce UL MIMO configurations for Rel-18 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232520 | 1773 |  | B | big CR 38.101-1 new combinations Rel-18 NR Inter-band CA/DC for y bands DL with x bands UL (y=4,5,6, x=1,2) | 18.3.0 |
| 2023-09 | RAN#101 | RP-232521 | 1775 |  | B | Big CR on TS38.101-1 Addition of intra-band CA Combinations | 18.3.0 |
| 2023-09 | RAN#101 | RP-232489 | 1777 |  | A | [NR_CADC_R17_2BDL_xBUL-Core] CR on TS38.101-1 Modification on MSD due to UL harmonic interference for CA _n48A-n66A | 18.3.0 |
| 2023-09 | RAN#101 | RP-232522 | 1780 |  | B | Big CR to TS 38.101-1: Adding channel BW support in existing NR bands | 18.3.0 |
| 2023-09 | RAN#101 | RP-232522 | 1785 |  | F | CR to 38.101-1 correction on CA_n34-n41, CA_n40-n41-n79 for simultaneous RxTx | 18.3.0 |
| 2023-09 | RAN#101 | RP-232501 | 1789 |  | A | [NR_newRAT-Core] Correction of intraband contiguous CA ACS requirements | 18.3.0 |
| 2023-09 | RAN#101 | RP-232498 | 1792 |  | A | [NR_RF_FR1] Correction of intraband non-contiguous CA ACS requirements | 18.3.0 |
| 2023-09 | RAN#101 | RP-232518 | 1797 |  | B | CR adding REFSENS for HD-FDD RedCap UE for band n105 | 18.3.0 |
| 2023-09 | RAN#101 | RP-232498 | 1799 |  | A | [NR_RF_FR1-Core] CR for TS38101-1 Clarifying applicable power classes for NR CA | 18.3.0 |
| 2023-12 | RAN#102 | RP-233361 | 1810 |  | B | Introduction of higherPowerLimit-r17 into NR CA of PC3+PC5 including UL Intra band CA | 18.4.0 |
| 2023-12 | RAN#102 | RP-233361 | 1811 |  | B | Introduction of delta PPowerClass report | 18.4.0 |
| 2023-12 | RAN#102 | RP-233331 | 1815 |  | A | Fc terminology update | 18.4.0 |
| 2023-12 | RAN#102 | RP-233340 | 1818 |  | A | CR for Intra-band UL CA MPR clarification | 18.4.0 |
| 2023-12 | RAN#102 | RP-233369 | 1821 |  | B | BigCR for High power UE for FDD single band PC2 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233369 | 1822 | 1 | B | CR to R18 TS38.101-1 to introduce PC2 UTRA ACLR | 18.4.0 |
| 2023-12 | RAN#102 | RP-233348 | 1826 |  | A | CR for TS 38.101 Rel-18 correcting the starting RB location for NS_07 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233368 | 1828 | 1 | B | TS 38.101-1 big CR for NR_700800900_combo_enh | 18.4.0 |
| 2023-12 | RAN#102 | RP-233368 | 1829 |  | F | CR Bug Fixes for Band Combinations in 38101-1-i30_s00-05 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233336 | 1832 |  | A | CR on TS38.101-1 for simplification of NR V2X UE coexistence in Rel-18 (Cat. A) | 18.4.0 |
| 2023-12 | RAN#102 | RP-233351 | 1834 |  | F | [NR_RF_TxD-Core] Correction to 7.3G REFSENS for TxD (Rel-18) | 18.4.0 |
| 2023-12 | RAN#102 | RP-233368 | 1835 |  | F | CR to R18 TS38.101-1 to align frequency range restriction for MSD | 18.4.0 |
| 2023-12 | RAN#102 | RP-233368 | 1842 |  | A | CR for 38.101-1 UE to UE coex  R18 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233366 | 1845 | 1 | B | CR for 38.101-1: Introduction of n106 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233363 | 1850 |  | F | CR to TS 38.101-1 on clarification of applicable SS raster entries for 3 MHz channel bandwidth | 18.4.0 |
| 2023-12 | RAN#102 | RP-233371 | 1851 |  | F | Corrections on requirements for NR-U enhancements | 18.4.0 |
| 2023-12 | RAN#102 | RP-233348 | 1857 |  | A | CR to TS38.101-1 Rel-18 CAT-A: On harmonisation network signalling requirements | 18.4.0 |
| 2023-12 | RAN#102 | RP-233369 | 1860 |  | A | CR to TS 38.101-1 (Rel-18): Correction of an Fc location for a 100MHz channel bandwidth of band n77 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233369 | 1868 |  | B | CR for TS 38.101-1 to introduce indication of modified MPR behaviour for band n34 and n40 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233364 | 1869 | 1 | B | Big CR for TS 38.101-1 for NR ATG | 18.4.0 |
| 2023-12 | RAN#102 | RP-233368 | 1870 | 1 | B | CR for 38.101-1: Add delta RIB requirements for CA_n78C_n84A-n89A | 18.4.0 |
| 2023-12 | RAN#102 | RP-233332 | 1875 |  | A | [NR_newRAT] CR for clarification on applicability of Rx antenna number for Rx requirements for TS 38.101-1 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233361 | 1876 |  | B | CR for 38.101-1: Time mask for switching across three or four uplink bands | 18.4.0 |
| 2023-12 | RAN#102 | RP-233365 | 1877 | 1 | B | Introduction of an enhanced channel raster | 18.4.0 |
| 2023-12 | RAN#102 | RP-233369 | 1880 |  | B | Big CR to 38.101-1 new combinations for Rel-18 NR HPUE Inter-band | 18.4.0 |
| 2023-12 | RAN#102 | RP-233332 | 1883 |  | A | [NR_newRAT-Core] Editorial modification CR for TS 38.101-1 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233364 | 1886 | 3 | B | Rel-18 CR for 38.101-1 New BS signalling implementation for non-collocated scenario | 18.4.0 |
| 2023-12 | RAN#102 | RP-233339 | 1887 |  | A | [NR_n41_BW-Core] Support of PC1.5 for n41 30MHz in Japan (R18) | 18.4.0 |
| 2023-12 | RAN#102 | RP-233361 | 1894 |  | F | [NR_MC_enh-Core]CR for DL interruption note improvement | 18.4.0 |
| 2023-12 | RAN#102 | RP-233339 | 1899 |  | A | [NR_n30-Core] CR to add resolution BW for Additional SEM for NS_21 - TS38.101-1, Rel-18, Cat-A | 18.4.0 |
| 2023-12 | RAN#102 | RP-233332 | 1903 |  | A | [NR_newRAT-Core] CR to remove the word capable in power class 3 capable UE - TS38.101-1, Rel-18, Cat-A | 18.4.0 |
| 2023-12 | RAN#102 | RP-233340 | 1906 |  | A | [NR_RF_FR1-Core] CR concerning the RMS average used in EVM measurement with transient period - TS38.101-1, Rel-18, Cat-A | 18.4.0 |
| 2023-12 | RAN#102 | RP-233370 | 1907 | 2 | B | Big CR to 38.101-1 Simultaneous Rx-Tx basket | 18.4.0 |
| 2023-12 | RAN#102 | RP-233370 | 1908 |  | B | Big CR to TS 38.101-1: Adding channel BW support in existing NR bands | 18.4.0 |
| 2023-12 | RAN#102 | RP-233362 | 1909 | 3 | B | Running CR to TS 38.101-1 - Introduction of Aerial UEs support | 18.4.0 |
| 2023-12 | RAN#102 | RP-233366 | 1910 |  | B | CR to TS 38.101-1 - Introduction of bands n31 and n72 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233339 | 1913 |  | A | [NR_n38_BW2] Clarify A-MPR values for NS_44 - Rel18 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233368 | 1914 | 1 | B | Big CR to reflect the completed NR inter-band CA DC combinations for 3 bands DL with up to 2 bands UL into TS 38.101-1 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233337 | 1917 |  | A | [NR_CADC_R16_2BDL_xBUL] CR for TS 38.101-1 to correct inter-band NR DC configuration table (R18_CAT A) | 18.4.0 |
| 2023-12 | RAN#102 | RP-233368 | 1918 | 1 | B | big CR 38.101-1 new combinations Rel-18 NR Inter-band CA/DC for y bands DL with x bands UL (y=4,5,6, x=1,2) | 18.4.0 |
| 2023-12 | RAN#102 | RP-233368 | 1921 |  | A | Rel18 Cat A CR for 38.101-1 Add missing Uplink configurations for PC3 CA_n46M-n48B-n96A and CA_n46M-n48(4A)-n96D | 18.4.0 |
| 2023-12 | RAN#102 | RP-233368 | 1923 |  | A | Rel18 Cat A CR for 38.101-1 Add missing MSD due to UL harmonic interference for PC3 CA_n71-n78 in clause 7.3A.4 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233368 | 1925 |  | B | Big CR on Introduction of completed SUL band combinations into TS 38.101-1 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233332 | 1929 |  | A | [NR_newRAT-Core] CR for 38.101-1 to clarify the applicable bands for additional UTRA ACLR requirements. (R18) | 18.4.0 |
| 2023-12 | RAN#102 | RP-233345 | 1931 |  | A | [NR_BCS4-Core] CR for 38.101-1 to modify the MSD value for CA_20-n78 harmonic mixing and NOTE2 in harmonic mixing table (R18) | 18.4.0 |
| 2023-12 | RAN#102 | RP-233370 | 1934 | 1 | B | R18 38101-1 CR for 3Tx inter-band CA | 18.4.0 |
| 2023-12 | RAN#102 | RP-233370 | 1935 |  | B | R18 38101-1 CR for low band 4Rx | 18.4.0 |
| 2023-12 | RAN#102 | RP-233361 | 1936 |  | B | Big CR for NR SL evoluation | 18.4.0 |
| 2023-12 | RAN#102 | RP-233361 | 1938 | 1 | B | CR to 38.101 for introduction of MPR reduction | 18.4.0 |
| 2023-12 | RAN#102 | RP-233371 | 1939 | 1 | F | Spectrum emission mask for operation with shared spectrum channel access R18 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233363 | 1940 | 1 | B | TS 38.101-1 big CR for NR_ENDC_RF_FR1_enh2 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233366 | 1941 | 1 | B | TS 38.101-1 big CR for NR_bands_UL_MIMO_R18 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233368 | 1945 | 1 | B | TS 38.101-1 big CR for NR_CADC_R18_2BDL_xBUL | 18.4.0 |
| 2023-12 | RAN#102 | RP-233371 | 1948 | 1 | F | CR for introducing NR-U uplink CA for NS_53 and NS_54 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233371 | 1949 |  | F | CR to TS38.101-1 for NR-U NS table reference | 18.4.0 |
| 2023-12 | RAN#102 | RP-233345 | 1951 | 1 | A | [NR_CADC_R17_3BDL_2BUL-Core] CR for 38.101-1 to add missing IMD5 for CA_n48-n66-n70 with UL CA_n48-n66 (Rel-18, Cat. A) | 18.4.0 |
| 2023-12 | RAN#102 | RP-233368 | 1952 |  | B | big CR for addition of NR CA Intra-band FR1 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233369 | 1953 |  | F | CR for 38.101-1: HPUE Band Combination Corrections | 18.4.0 |
| 2023-12 | RAN#102 | RP-233366 | 1955 | 1 | B | CR to TS38.101-1: Introduction of n109 | 18.4.0 |
| 2023-12 | RAN#102 | RP-233331 | 1959 |  | A | [NR_newRAT] CR to 38.101-1 on FRC correction | 18.4.0 |
| 2023-12 | RAN#102 | RP-233331 | 1963 |  | A | [NR_newRAT] CR to 38.101-1 on FRC deletion for 5MHz 30 KHz | 18.4.0 |
| 2023-12 | RAN#102 | RP-233361 | 1964 | 1 | B | CR to 38.101-1: Introduction of eRedCap | 18.4.0 |
| 2023-12 | RAN#102 | RP-233345 | 1966 |  | A | [NR_CADC_R17_2BDL_xBUL] CR to 38.101-1, n3-n77(2A) test point correction | 18.4.0 |
| 2023-12 | RAN#102 | RP-233340 | 1972 |  | A | Correction of ?T_RxSRS for SRS resource set consisting of two SRS ports | 18.4.0 |
| 2024-03 | RAN#103 | RP-240601 | 1984 |  | F | CR: Correction to remedy 3GU error of CR1907r2 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240613 | 1988 | 1 | F | Adding support for the VLP mode in US | 18.5.0 |
| 2024-03 | RAN#103 | RP-240597 | 1989 |  | F | CR Bug Fixes for Band Combinations in 38101-1-i40_s00-05 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240558 | 1991 |  | A | CR to 38.101-1 on correction of CA_n2A-n78A UL configuration | 18.5.0 |
| 2024-03 | RAN#103 | RP-240612 | 1994 |  | B | CR for 38101-1 to add PC1.5 for band n39 and annex L for band n39 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240607 | 1995 | 2 | F | CR for 38101-1 to update ATG related signaling name | 18.5.0 |
| 2024-03 | RAN#103 | RP-240603 | 1998 |  | F | (NR_cov_enh2-Core) Correction on dpc-Reporting-FR1 related requirements | 18.5.0 |
| 2024-03 | RAN#103 | RP-240606 | 1999 | 2 | F | (NR_ENDC_RF_FR1_enh2-Core) Correction on delta TRxSRS related texts for 8Rx | 18.5.0 |
| 2024-03 | RAN#103 | RP-240600 | 2000 |  | B | BigCR for High power UE for intra-band and inter-band CA with power class 2 on single carrier uplink on FDD band | 18.5.0 |
| 2024-03 | RAN#103 | RP-240599 | 2001 |  | B | BigCR for High power UE for FDD single band PC2 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240562 | 2002 |  | F | CR to TS 38.101-1 Rel-18 Corrections to UL configuration for asymmetric ULDL | 18.5.0 |
| 2024-03 | RAN#103 | RP-240607 | 2008 | 1 | F | Modification on power imbalance requirements | 18.5.0 |
| 2024-03 | RAN#103 | RP-240576 | 2011 |  | A | CR to TS38.101-1 Rel-18 CAT-A: On corrections for NR-U R16 A-MPR requirements | 18.5.0 |
| 2024-03 | RAN#103 | RP-240557 | 2013 |  | A | CR to TS38.101-1 Rel-18 CAT-A: On corrections for NR-U R17 A-MPR requirements | 18.5.0 |
| 2024-03 | RAN#103 | RP-240613 | 2014 |  | F | CR to TS38.101-1 Rel-18 CAT-F: On corrections for NR-U R18 A-MPR requirements | 18.5.0 |
| 2024-03 | RAN#103 | RP-240574 | 2018 |  | A | (NR_RF_FR1) Introduction of missing DMRS configuration restriction for intra-ULCA in FR1 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240599 | 2035 |  | B | FWA Big CR | 18.5.0 |
| 2024-03 | RAN#103 | RP-240614 | 2039 |  | F | (TEI18) CR for 38.101-1 corrections for  UL CA conigurations R18 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240552 | 2043 |  | A | (TEI16) almost contiguous A-MPR for PC2 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240597 | 2045 |  | F | (NR_CADC_R18_2BDL_xBUL-Core) Correction for MSD IMD test points R18 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240574 | 2048 |  | A | CA MPR correction | 18.5.0 |
| 2024-03 | RAN#103 | RP-240606 | 2049 |  | F | (NR_ENDC_RF_FR1_enh2-Core ) 4Tx RF issues | 18.5.0 |
| 2024-03 | RAN#103 | RP-240606 | 2050 | 1 | F | (NR_ENDC_RF_FR1_enh2-Core ) Power class for Lower MSD verification – TS38.101-1 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240587 | 2053 |  | F | (NR_MC_enh-Core) CR for 38.101-1: Correction on time mask for Rel-18 Tx switching | 18.5.0 |
| 2024-03 | RAN#103 | RP-240597 | 2057 |  | A | CR to TS 38.101-1 (Rel-18): CR for removing n48(A-C) intra-band CA configuration | 18.5.0 |
| 2024-03 | RAN#103 | RP-240597 | 2058 |  | B | Big CR to reflect the completed NR inter-band CA DC combinations for 3 bands DL with up to 2 bands UL into TS 38.101-1 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240558 | 2060 |  | A | (NR_CADC_R17_3BDL_2BUL) CR for TS 38.101-1 on inter-band CA for n46-n48-n96 (R18_CAT_A) | 18.5.0 |
| 2024-03 | RAN#103 | RP-240594 | 2065 |  | B | TS 38.101-1 big CR for NR_bands_UL_MIMO_R18 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240607 | 2068 | 3 | F | Rel-18 CR for 38.101-1 NonCol_IntraB_ENDC_NR_CA | 18.5.0 |
| 2024-03 | RAN#103 | RP-240600 | 2069 |  | B | Big CR to 38.101-1 new combinations for Rel-18 NR HPUE Inter-band | 18.5.0 |
| 2024-03 | RAN#103 | RP-240614 | 2076 | 1 | F | CR for Rel-18 38.101-1 to unify the minimum guardband symbol | 18.5.0 |
| 2024-03 | RAN#103 | RP-240603 | 2078 | 1 | F | CR for Rel-18 38.101-1 is to modify the requirements for eRedCap | 18.5.0 |
| 2024-03 | RAN#103 | RP-240597 | 2082 |  | F | (NR_newRAT-Core) Correct the equation in the NOTE for harmonic mixing MSD | 18.5.0 |
| 2024-03 | RAN#103 | RP-240597 | 2089 |  | B | TS 38.101-1 big CR for NR_CADC_R18_2BDL_xBUL | 18.5.0 |
| 2024-03 | RAN#103 | RP-240601 | 2090 |  | B | CR to reflect the completed 4Rx support for NR FR1 bands (<2.6GHz) into TS 38.101-1 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240558 | 2096 |  | A | (NR_CADC_R17_2BDL_xBUL-Core) CR to correct carrier frequencies used in REFSENS exceptions due to IMD for CA_n26-n70 - TS38.101-1, Rel-18, Cat-A | 18.5.0 |
| 2024-03 | RAN#103 | RP-240561 | 2100 |  | F | (NR_n48-Core) CR to correct or add note applicable for specific channel bandwidths for CA including band n48 - TS38.101-1, Rel-18, Cat-F | 18.5.0 |
| 2024-03 | RAN#103 | RP-240613 | 2102 | 1 | F | (NR_RF_FR1_enh-Core, 4Rx_low_NR_band_handheld_3Tx_NR_CA_ENDC-Core) CR to add clarification regarding the configurations of the UL CCs for suffix H - TS38.101-1, Rel-18, Cat-F | 18.5.0 |
| 2024-03 | RAN#103 | RP-240565 | 2106 | 1 | A | (NR_newRAT-Core) CR to correct "Supplement" to "Supplementary" in the definition of the suffix used for SUL - TS38.101-1, Rel-18, Cat-F | 18.5.0 |
| 2024-03 | RAN#103 | RP-240597 | 2108 |  | B | big CR 38.101-1 new combinations Rel-18 NR Intra-band | 18.5.0 |
| 2024-03 | RAN#103 | RP-240601 | 2109 |  | F | CR 38.101-1 for corrections in tables 5.2-1 and 5.3.5-1 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240597 | 2110 |  | F | CR 38.101-1 correcting 2 bands configuration tables | 18.5.0 |
| 2024-03 | RAN#103 | RP-240597 | 2111 |  | F | CR 38.101-1 correcting 3 bands configuration tables | 18.5.0 |
| 2024-03 | RAN#103 | RP-240598 | 2112 |  | F | CR 38.101-1 correcting 4 and 5 bands configuration tables | 18.5.0 |
| 2024-03 | RAN#103 | RP-240598 | 2113 |  | B | Big CR on Introduction of completed SUL band combinations into TS 38.101-1 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240557 | 2115 |  | F | (NR_CA_R17_3BDL_1BUL-Core) CR for TS 38.101-1 to add missing combo CA_n3A-n8A-n79A (R18) | 18.5.0 |
| 2024-03 | RAN#103 | RP-240564 | 2119 |  | A | (NR_newRAT-Core) CR for TS 38.101-1 to correct the Finterferer (offset) for intra-band CA ACS and IBB requirements (R18) | 18.5.0 |
| 2024-03 | RAN#103 | RP-240558 | 2121 |  | A | (NR_CADC_R17_2BDL_xBUL-Core) CR for TS 38.101-1 to clarify the applicable SCS when UE testing (R18) | 18.5.0 |
| 2024-03 | RAN#103 | RP-240601 | 2122 |  | F | Big CR for 3Tx NR inter-band UL CA and EN-DC basket WI (38.101-1) | 18.5.0 |
| 2024-03 | RAN#103 | RP-240613 | 2123 |  | F | Big CR for Low band 4Rx for handheld UE and 3Tx for inter-band UL CA and EN-DC (38.101-1) | 18.5.0 |
| 2024-03 | RAN#103 | RP-240603 | 2124 |  | F | (NR_SL_enh2-Core) BigCR to TS38.101-1 for Sidelink enhancement | 18.5.0 |
| 2024-03 | RAN#103 | RP-240611 | 2137 | 1 | F | CR for TS 38.101-1 to maintain low band combos | 18.5.0 |
| 2024-03 | RAN#103 | RP-240587 | 2138 |  | F | bigCR to 38.101-1 Corrections for aerial NR UEs | 18.5.0 |
| 2024-03 | RAN#103 | RP-240587 | 2139 |  | F | BigCR to 38.101 for Corrections for MPR reduction | 18.5.0 |
| 2024-03 | RAN#103 | RP-240608 | 2140 | 1 | F | CR to TS 38.101-1: correction on enhanced channel raster | 18.5.0 |
| 2024-03 | RAN#103 | RP-240574 | 2143 |  | A | (NR_RF_FR1) CR to TS 38.101-1: Channel raster to resource element mapping | 18.5.0 |
| 2024-03 | RAN#103 | RP-240606 | 2146 |  | F | (NR_ENDC_RF_FR1_enh2-Core) Correction of Lower-MSD requirements for NR CA | 18.5.0 |
| 2024-03 | RAN#103 | RP-240564 | 2150 |  | A | (NR_newRAT-Core) CR to remove the word capable in power class related requirements | 18.5.0 |
| 2024-03 | RAN#103 | RP-240564 | 2154 |  | A | (NR_newRAT-Core) CR to TS38.101-1: Correction of band number in uplink configuration for reference sensitivity table | 18.5.0 |
| 2024-03 | RAN#103 | RP-240599 | 2155 |  | B | Big CR on TS38.101-1 Addition of intra-band CA Combinations | 18.5.0 |
| 2024-03 | RAN#103 | RP-240598 | 2156 |  | B | big CR 38.101-1 new combinations Rel-18 NR Inter-band CA/DC for y bands DL with x bands UL (y=4,5,6, x=1,2) | 18.5.0 |
| 2024-03 | RAN#103 | RP-240606 | 2160 | 1 | F | R18 Cat-F CR 38.101-1 correction CR for 4Tx requirements | 18.5.0 |
| 2024-03 | RAN#103 | RP-240558 | 2167 |  | A | [NR_CADC_R17_2BDL_xBUL] CR for 38.101-1: Correct missing CA_n71-n77 Harmonic | 18.5.0 |
| 2024-03 | RAN#103 | RP-240597 | 2168 |  | F | [NR_CADC_R18_2BDL_xBUL] CR for 38.101-1: Correct n25 instead of n41 for CA_n41(3A)-n85A | 18.5.0 |
| 2024-03 | RAN#103 | RP-240557 | 2170 |  | A | [NR_BCS4-Core] CR for 38.101-1: Maximum Aggregated BW for BCS5 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240576 | 2172 | 1 | A | (NR_unlic-Core) Correction CR for NS_59 in TS38.101-1_V2 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240613 | 2173 | 1 | F | (NR_unlic_enh-Core) Correction CR for NS_63, NS_64 in TS38.101-1 | 18.5.0 |
| 2024-03 | RAN#103 | RP-240606 | 2176 | 2 | F | (NR_FR1_lessthan_5MHz_BW-Core) CR to TS 38.101-1 for sub 5MHz channel bandwidth | 18.5.0 |
| 2024-03 | RAN#103 | RP-240603 | 2178 |  | F | (NR_cov_enh2-Core) CR to TS38.101-1 on higher power limit for inter-band CA with an intra-band component | 18.5.0 |
| 2024-03 | RAN#103 | RP-240597 | 2179 | 1 | F | CR to R18 38101-1 to correct Note on PC2 CA_n71-n77 IMD5 MSD | 18.5.0 |
| 2024-03 | RAN#103 | RP-240597 | 2183 | 1 | F | (NR_CADC_R18_2BDL_xBUL) CR to R18 38101-1 to correct channel bandwidths in MSD test points | 18.5.0 |
| 2024-03 | RAN#103 | RP-240588 | 2184 |  | F | Big CR for 38.101-1 for SRS aggregation for positioning | 18.5.0 |
| 2024-03 | RAN#103 | RP-240606 | 2185 |  | F | Big CR for lower MSD for inter-band CA/EN-DC/DC | 18.5.0 |
| 2024-03 | RAN#103 | RP-240606 | 2186 |  | F | Big CR for 38.101-1 on less than 5MHz | 18.5.0 |
| 2024-03 | RAN#103 | RP-240603 | 2187 |  | F | Big CR for 38.101-1 on MC | 18.5.0 |
| 2024-03 | RAN#103 | RP-240572 | 2189 |  | A | Compensating for post antenna connector gain impact to unwanted emissions for n101 band | 18.5.0 |
| 2024-03 | RAN#103 | RP-240598 | 2190 |  | F | Big CR to 38.101-1 for two SUL cells | 18.5.0 |
| 2024-03 | RAN#103 | RP-240855 | 2191 | 4 | B | CR 38.101-1 addition of 2Rx XR exception for REFSENS [2Rx_XR_Device] | 18.5.0 |
| 2024-06 | RAN#104 | RP-241461 | 2200 |  | B | CR: Simultaneous Rx-Tx to remedy the de-implementation of CR1907r2 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241489 | 2201 |  | F | Clarification for the mandatory support of enhanced channel raster for the TN bands | 18.6.0 |
| 2024-06 | RAN#104 | RP-241382 | 2203 |  | A | CR to fix CBW listing of NS_37 emission requirements | 18.6.0 |
| 2024-06 | RAN#104 | RP-241394 | 2205 |  | A | CR to 38.101-1 on Wgap correction for CA_n2(2A) REFSENS requirement | 18.6.0 |
| 2024-06 | RAN#104 | RP-241491 | 2206 |  | F | CR to 38.101-1 on corrections for n109 UE channel BW table misalignment in Table 5.3.5-1 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241393 | 2214 |  | A | CR to align NR carrier centre frequencies with LTE for NS_24 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241443 | 2215 |  | F | CR Bugfix 38101-1-i50_s0505B-0505C | 18.6.0 |
| 2024-06 | RAN#104 | RP-241443 | 2216 | 1 | F | CR Bug Fixes 38101-1-i50_s0505A03-0505A03 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241483 | 2218 | 2 | F | (NR_ATG-Core) CR for 38101-1 on ATG UE Tx Rfrequirement | 18.6.0 |
| 2024-06 | RAN#104 | RP-241484 | 2220 | 1 | F | (NonCol_intraB_ENDC_NR_CA-Core) On applicability of diversity characteristic | 18.6.0 |
| 2024-06 | RAN#104 | RP-241494 | 2222 |  | F | CR on updating UE capability name for 2Rx XR UEs [2Rx_XR_Device] | 18.6.0 |
| 2024-06 | RAN#104 | RP-241393 | 2226 |  | A | CR for TS 38.101-1 Rel-18 correcting maximum transmission bandwidth for NS_04 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241483 | 2228 | 1 | B | Big CR of TS 38.101-1 for ATG | 18.6.0 |
| 2024-06 | RAN#104 | RP-241395 | 2230 |  | A | (NR_CADC_R17_3BDL_2BUL) CR to 38.101-1: Adding note to CA_n7-n8-n78 for IMD4 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241461 | 2231 |  | B | Big CR to 38.101-1 on simultaneous Rx-Tx basket | 18.6.0 |
| 2024-06 | RAN#104 | RP-241388 | 2234 |  | A | CR 38.101-1 correction CR for Rx requirements with TxD indication | 18.6.0 |
| 2024-06 | RAN#104 | RP-241493 | 2235 |  | F | R18 Cat-F CR 38.101-1 correction CR for 3Tx requirements | 18.6.0 |
| 2024-06 | RAN#104 | RP-241478 | 2236 |  | F | R18 Cat-F CR 38.101-1 correction CR for 4Tx requirements | 18.6.0 |
| 2024-06 | RAN#104 | RP-241460 | 2237 |  | B | BigCR for High power UE for intra-band and inter-band CA with power class 2 on single carrier uplink on FDD band | 18.6.0 |
| 2024-06 | RAN#104 | RP-241456 | 2238 |  | B | BigCR for High power UE for FDD single band PC2 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241465 | 2244 |  | F | Correction of parameter name for dpc-Reporting-FR1 for range 1 SA | 18.6.0 |
| 2024-06 | RAN#104 | RP-241453 | 2245 |  | D | (NR_CADC_R18_yBDL_xBUL) CR for 38.101-1: Table format corrections | 18.6.0 |
| 2024-06 | RAN#104 | RP-241459 | 2246 |  | F | (HPUE_FR1_TDD_NR_CADC_SUL_R18) CR for 38.101-1: Corrections for missing PC2 CA_n41C and MOP Table | 18.6.0 |
| 2024-06 | RAN#104 | RP-241402 | 2259 |  | A | (NR_RF_FR1_enh-Core) CR to 38.101-1 R18 corrections on Pcmax tolerance for intra-band contiguous CA with UL MIMO | 18.6.0 |
| 2024-06 | RAN#104 | RP-241382 | 2261 |  | A | CR for Rel-18 to correct the signalling IE for FR1 Intra-band non-contiguous CA in clause 6.2A.2.2.0. | 18.6.0 |
| 2024-06 | RAN#104 | RP-241478 | 2262 |  | F | CR for TS 38.101-1: some update on EVM requirement for 4Tx UL MIMO | 18.6.0 |
| 2024-06 | RAN#104 | RP-241483 | 2266 |  | F | CR on MOP and configured transmitted power for ATG UE | 18.6.0 |
| 2024-06 | RAN#104 | RP-241391 | 2270 |  | A | (LTE_NR_DC_CA_enh) CR to TS 38.101-1: correction of Pcmax tolerance for NR DC (Rel-18) | 18.6.0 |
| 2024-06 | RAN#104 | RP-241389 | 2273 |  | F | (5G_V2X_NRSL) CR to TS 38.101-1: correction of Pcmax tolerance for sidelink (Rel-18) | 18.6.0 |
| 2024-06 | RAN#104 | RP-241394 | 2281 | 1 | F | (NR_CA_R16_intra-Core, , ) CR to add notes for SCS restrictions on CBWs in CA configurations - TS38.101-1, Rel-18 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241395 | 2283 |  | A | (NR_CADC_R17_3BDL_2BUL) CR to correct n66 transmission bandwidth used in REFSENS exceptions due to IMD5 for CA_n5-n48-n66 - TS38.101-1, Rel-18 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241383 | 2287 |  | A | (NR_newRAT-Core)Correct the Pcmax tolerance for inter-band CA and TxD | 18.6.0 |
| 2024-06 | RAN#104 | RP-241478 | 2288 |  | F | CR for TS 38.101-1: 4Rx/8Rx applicability for Lower-MSD requirements | 18.6.0 |
| 2024-06 | RAN#104 | RP-241451 | 2289 |  | B | TS 38.101-1 big draft CR for NR_CADC_R18_2BDL_xBUL | 18.6.0 |
| 2024-06 | RAN#104 | RP-241492 | 2293 |  | A | Cat A CR to TS 38.101-1 Rel-18 NR-U Nominal channel spacing | 18.6.0 |
| 2024-06 | RAN#104 | RP-241450 | 2297 |  | B | CR 38.101-1 adding intra-band NR CA configurations | 18.6.0 |
| 2024-06 | RAN#104 | RP-241477 | 2302 | 1 | F | Introduce asymmetric UL DL channel BW combinations for n28 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241405 | 2303 | 2 | F | CR to 38.101-1 on Aerial Specific Pmax Values | 18.6.0 |
| 2024-06 | RAN#104 | RP-241478 | 2304 |  | F | CR on 38.101-1: adding missing 8Rx requirements | 18.6.0 |
| 2024-06 | RAN#104 | RP-241477 | 2305 |  | F | NS_17 correction on Band n28 3 MHz operation in Japan | 18.6.0 |
| 2024-06 | RAN#104 | RP-241455 | 2308 | 1 | F | CR to TS 38.101-1: n100-n101 Car radio receiver requirements | 18.6.0 |
| 2024-06 | RAN#104 | RP-241455 | 2309 |  | B | Big CR High-power UE operation for fixed-wireless/vehicle-mounted use cases in LTE bands and NR bands | 18.6.0 |
| 2024-06 | RAN#104 | RP-241443 | 2310 |  | F | CR for 38.101-1 Correction of cell issues | 18.6.0 |
| 2024-06 | RAN#104 | RP-241462 | 2311 |  | F | Big CR for 3Tx NR inter-band basket WI 38.101-1 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241402 | 2313 |  | A | (NR_RF_FR1_enh-Core) CR for TS 38.101-1: Add ACLR requirement for PC2 intra-band non-contiguous UL CA | 18.6.0 |
| 2024-06 | RAN#104 | RP-241402 | 2315 |  | A | (NR_RF_FR1_enh-Core) CR for TS 38.101-1: Corrections on intra-band UL contiguous CA with UL MIMO for PC3 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241477 | 2317 | 1 | F | CR for TS 38.101-1: Define the reserved GSCN / ARFCN-ValueNR and NR operating band | 18.6.0 |
| 2024-06 | RAN#104 | RP-241456 | 2321 | 1 | B | CR to TS 38.101-1: Addition of PC2 for n7 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241467 | 2326 |  | F | CR to TS38.101-1 for Sidelink enhancement  cover RAN4#110bis | 18.6.0 |
| 2024-06 | RAN#104 | RP-241464 | 2331 |  | F | (NR_MC_enh-Core) CR for 38.101-1: Correction on time mask for Rel-18 Tx switching | 18.6.0 |
| 2024-06 | RAN#104 | RP-241454 | 2335 |  | B | Big CR on Introduction of completed SUL band combinations into TS 38.101-1 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241483 | 2336 | 2 | F | (NR_ATG-Core) CR for TS 38.101-1 to modify the note for ACS requirements 4dB below Pcmax | 18.6.0 |
| 2024-06 | RAN#104 | RP-241453 | 2339 |  | B | big CR 38.101-1 new combinations Rel-18 NR Inter-band CA/DC for y bands DL with x bands UL (y=4,5,6, x=1,2) | 18.6.0 |
| 2024-06 | RAN#104 | RP-241457 | 2341 | 1 | B | Big CR on TS38.101-1 Addition of intra-band CA Combinations | 18.6.0 |
| 2024-06 | RAN#104 | RP-241453 | 2343 |  | B | (NR_CADC_R18_yBDL_xBUL)  CR for TS 38101-1 to clarify 1 UL configuration for NR CA | 18.6.0 |
| 2024-06 | RAN#104 | RP-241452 | 2344 |  | B | Big CR to reflect the completed NR inter-band CA DC combinations for 3 bands DL with up to 2 bands UL into TS 38.101-1 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241382 | 2348 |  | A | (NR_newRAT-Core) CR for TS 38.101-1 on UE additional spurious emissions (R18_CAT_A) | 18.6.0 |
| 2024-06 | RAN#104 | RP-241398 | 2351 |  | A | CR to TS 38.101-1: Clarification on band-specific post antenna gain values for the FRMCS operation | 18.6.0 |
| 2024-06 | RAN#104 | RP-241398 | 2353 |  | A | CR to TS 38.104: clarifications on RMR terminology and related operating bands | 18.6.0 |
| 2024-06 | RAN#104 | RP-241478 | 2361 |  | F | (NR_ENDC_RF_FR1_enh2-Core) Correction on lowerMSD verification | 18.6.0 |
| 2024-06 | RAN#104 | RP-241388 | 2367 |  | A | Rel-18 SUL configuration correction for REFSENS for DL in n24 and UL in n99 | 18.6.0 |
| 2024-06 | RAN#104 | RP-241493 | 2369 |  | F | CR for correction of condition for 3Tx SAR solution | 18.6.0 |
| 2024-06 | RAN#104 | RP-241494 | 2370 |  | B | CR to support uplink Tx switching for CA with two contiguous aggregated carriers in each band [2CC-2CC_ULTx_switching] | 18.6.0 |
| 2024-06 | RAN#104 | RP-241459 | 2371 |  | B | Big CR to 38.101-1 new combinations for Rel-18 NR HPUE Inter-band | 18.6.0 |
| 2024-09 | RAN#105 | RP-242156 | 2374 |  | A | CR to R18 38.101-1 to add 25MHz CBW to NS_18 emissions requirement | 18.7.0 |
| 2024-09 | RAN#105 | RP-242188 | 2376 |  | F | CR for 38.101-1: Correction on the SL-U RB set and intra-cell guard band determination | 18.7.0 |
| 2024-09 | RAN#105 | RP-242159 | 2377 | 1 | F | Clarification for the enhanced channel raster and carrier aggregation | 18.7.0 |
| 2024-09 | RAN#105 | RP-242163 | 2380 |  | F | (NR_FDD_ULn28_DLn75_n76) CR to 38.101-1 on Channel raster for Band n109 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242158 | 2387 |  | A | (NR_CADC_R17_2BDL_xBUL) Removal of CA combinations containing n48(A-C) | 18.7.0 |
| 2024-09 | RAN#105 | RP-242173 | 2391 |  | A | CR for TS 38.101-1 Rel-18 correction on the terminology of emission bandwidth for NS_04 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242196 | 2392 | 1 | F | (NR_pos_enh2-Core) CR to 38.101-1 on positioning IE correction | 18.7.0 |
| 2024-09 | RAN#105 | RP-242184 | 2394 |  | A | (NR_redcap-Core) Correction of the channel raster for RedCap UEs by added entries | 18.7.0 |
| 2024-09 | RAN#105 | RP-242155 | 2399 |  | A | (NR_6GHz_unlic_EU-Core) CR for TS 38.101-1 on UE transmitter power for the Pcmax tolerance for NR unlicensed operation (R18_CAT_A) | 18.7.0 |
| 2024-09 | RAN#105 | RP-242158 | 2401 |  | F | (NR_CADC_R18_3BDL_xBUL-Core) CR for TS 38.101-1 on UE configured power relaxation for special component bands (R18) | 18.7.0 |
| 2024-09 | RAN#105 | RP-242163 | 2402 | 1 | F | (NR_FR1_lessthan_5MHz_BW-Core) CR for TS 38.101-1 on narrow band blocking for 3MHz channel bandwidth | 18.7.0 |
| 2024-09 | RAN#105 | RP-242186 | 2404 |  | F | (NR_RF_FR1_enh-Core) CR for TS 38.101-1: Corrections on intra-band UL contiguous CA with UL MIMO for PC3 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242159 | 2405 |  | F | CR on 38.101-1 Update the IE names for coverage enhancement | 18.7.0 |
| 2024-09 | RAN#105 | RP-242157 | 2407 |  | A | Remove the superscript NOTE 1 for intra-band contiguous CA | 18.7.0 |
| 2024-09 | RAN#105 | RP-242174 | 2410 |  | A | (NR_n28_BW-Core) Apply ?MPR to the total MOP reduction | 18.7.0 |
| 2024-09 | RAN#105 | RP-242183 | 2412 | 1 | F | (NR_PC2_CA_R17_2BDL_2BUL) Remove superscript NOTE 6 for PC2 TDD-TDD inter-band CA | 18.7.0 |
| 2024-09 | RAN#105 | RP-242152 | 2413 |  | F | CR 38.101-1 addtion of ETSI TC RT based on ECC Decision(20)02 reference to NB blocking | 18.7.0 |
| 2024-09 | RAN#105 | RP-242155 | 2415 | 1 | F | CR 38.101-1 Clarifications for non-collocated requirements | 18.7.0 |
| 2024-09 | RAN#105 | RP-242190 | 2418 |  | A | CR on typo for A-MPR of NR unlicensed band | 18.7.0 |
| 2024-09 | RAN#105 | RP-242188 | 2419 |  | F | CR on missing NS values for SL-U(R18) | 18.7.0 |
| 2024-09 | RAN#105 | RP-242156 | 2425 |  | F | CR 38.101-1 correcting the table for NR operating bands in FR1 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242158 | 2426 |  | F | CR 38.101-1 correcting 2 bands NR CA configuration tables | 18.7.0 |
| 2024-09 | RAN#105 | RP-242158 | 2427 |  | F | CR 38.101-1 correcting 3 bands NR CA configuration tables | 18.7.0 |
| 2024-09 | RAN#105 | RP-242158 | 2428 |  | F | CR 38.101-1 correcting 4 bands NR CA configuration tables | 18.7.0 |
| 2024-09 | RAN#105 | RP-242158 | 2432 |  | A | CR on MSD value correction for power class 5 cross band isolation | 18.7.0 |
| 2024-09 | RAN#105 | RP-242174 | 2436 |  | A | (NR_newRAT-core) CR for TS 38.101-1 R18 correction on AMPR for NS_10 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242149 | 2442 |  | A | (5G_V2X_NRSL-Core) CR to correct the name of the feature "V2X con-current operation" to "V2X concurrent operation" - TS38.101-1 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242191 | 2447 |  | A | (TEI16) CR to correct (typo) of the definitions of the symbols Nrb_agg - TS38.101-1 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242188 | 2449 | 1 | F | (NR_SL_enh2-Core) CR to add third level clause suffixes for V2X - TS38.101-1 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242186 | 2452 | 1 | A | Correction for value B for non-contiguous uplink carrier aggregation | 18.7.0 |
| 2024-09 | RAN#105 | RP-242158 | 2457 | 2 | F | CR for NR CA Harmonic Mixing clean-up PC3 PC5 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242158 | 2459 | 1 | F | CR Adding missing MSD for CA_n2A-n66A and for CA_n25A-n66A PC3 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242150 | 2460 | 2 | F | CR for NR CA Harmonic Mixing clean-up PC2 PC1.5 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242156 | 2461 | 1 | F | (NR_ATG-Core) CR for TS 38.101-1 to clarify the Tx requirements definition for ATG UE | 18.7.0 |
| 2024-09 | RAN#105 | RP-242189 | 2463 |  | A | (NR_SUL_combos_R17-Core) CR for TS 38.101-1 to clarify the applicability for NUL carriers (R18) | 18.7.0 |
| 2024-09 | RAN#105 | RP-242158 | 2465 | 1 | F | CR to TS 38.101-1 Rel-18 NR CA Uplink Harmonic clean-up PC3 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242150 | 2466 | 1 | F | CR to TS 38.101-1 Rel-18 NR CA Uplink Harmonic clean-up PC2 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242163 | 2470 | 1 | F | Cat F CR to TS 38.101-1 Rel-18 REFSENS Corrections | 18.7.0 |
| 2024-09 | RAN#105 | RP-242158 | 2471 | 1 | F | CR to TS 38.101-1 Rel-18 Intra-band CA REFSENS corrections | 18.7.0 |
| 2024-09 | RAN#105 | RP-242158 | 2472 | 1 | F | CR to TS 38.101-1 Rel-18 Corrections to ACLR for CA_NC_NS_100 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242191 | 2476 |  | A | Cat A CR to TS 38.101-1 Rel-18 Power Class 4 clean-up | 18.7.0 |
| 2024-09 | RAN#105 | RP-242158 | 2477 | 1 | F | CR to TS 38.101-1 Rel-18 Dual-UL IMD corrections | 18.7.0 |
| 2024-09 | RAN#105 | RP-242150 | 2478 |  | F | ( HPUE_FR1_TDD_NR_CADC_SUL_R18 ) CR to TS 38.101-1 for missing HPUE TDD configurations | 18.7.0 |
| 2024-09 | RAN#105 | RP-242171 | 2481 |  | A | (NR_n41_BW-Core) CR to TS 38.101-1: NS_47 correction | 18.7.0 |
| 2024-09 | RAN#105 | RP-242150 | 2484 |  | F | ( HPUE_FR1_FDD_NR_CADC_R18 ) CR to TS 38.101-1 for missing HPUE FDD configurations | 18.7.0 |
| 2024-09 | RAN#105 | RP-242191 | 2489 |  | A | (TEI) On missing BCS set definition for asymmetric TDD | 18.7.0 |
| 2024-09 | RAN#105 | RP-242156 | 2492 |  | F | 3MHz channel bandwidth optional for frequency bands n31 and n72 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242152 | 2493 |  | F | (LTE_NR_HPUE_FWVM_R18-Core) Clarification on FRMCS PC1 applicability for bands n100 and n101 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242171 | 2496 | 1 | F | (NR_n14-Core, TEI16) Correction of notes for UE output power | 18.7.0 |
| 2024-09 | RAN#105 | RP-242150 | 2497 |  | F | (HPUE_FR1_FDD_NR_CADC_R18-Core) CR for 38.101-1: Corrections for CA_n71A-n77A PC2 n71 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242150 | 2498 |  | F | ( HPUE_NR_FR1_FDD) CR for 38.101-1 NS_06 corrections | 18.7.0 |
| 2024-09 | RAN#105 | RP-242158 | 2499 | 1 | F | (CA and HPUE) CR for 38.101-1: Various corrections for CA and HPUE | 18.7.0 |
| 2024-09 | RAN#105 | RP-242173 | 2503 | 1 | A | CR to 38.101-1 Rel-18: Corrections of NR operating bands clause in FR1 | 18.7.0 |
| 2024-09 | RAN#105 | RP-242156 | 2505 | 1 | F | CR to R18 38101-1 to add 35MHz CBW to NS_35 definition | 18.7.0 |
| 2024-12 | RAN#106 | RP-243054 | 2515 | 1 | A | (NR_newRAT-Core) Replacement of dual with 2Tx | 18.8.0 |
| 2024-12 | RAN#106 | RP-243054 | 2516 |  | F | IE and UE capability name corrections (38.101-1) | 18.8.0 |
| 2024-12 | RAN#106 | RP-243048 | 2517 |  | F | Removal of non-existing UE capabilities and associated texts | 18.8.0 |
| 2024-12 | RAN#106 | RP-243042 | 2519 |  | F | CR to TS 38.101-1 on addition of 3 MHz CBW in Annex D | 18.8.0 |
| 2024-12 | RAN#106 | RP-243038 | 2520 | 1 | F | (NR_cov_enh2) Note clarification on applicability conditions of boost in 38.101-1 Rel-18 | 18.8.0 |
| 2024-12 | RAN#106 | RP-243040 | 2523 |  | A | (NR_eMIMO) Clarification of Rel-15 pi2BPSK variant in wording  in 38.101-1 Rel-18 | 18.8.0 |
| 2024-12 | RAN#106 | RP-243023 | 2526 | 1 | A | (5G_V2X_NRSL-Core) CR to 38.101-1 Rel-18 Cat-A for 7.6E.3.1 Out-of-band blocking for V2X non-concurrent operation | 18.8.0 |
| 2024-12 | RAN#106 | RP-243052 | 2528 |  | A | (NR_n30-Core) n30 NS_21 AMPR correction CR to 38.101-1 (cat-A) | 18.8.0 |
| 2024-12 | RAN#106 | RP-243055 | 2532 |  | A | (NR_newRAT-Core) Correction to IBB for intraband contiguous CA | 18.8.0 |
| 2024-12 | RAN#106 | RP-243036 | 2536 |  | F | CR Bugfix 38101-1-i70_s0505A03-0505A03 | 18.8.0 |
| 2024-12 | RAN#106 | RP-243036 | 2537 |  | F | (NR_CADC_R18_2BDL_xBUL) CR for 38.101-1: CA_n77-n85 PC3 IMD MSD correction | 18.8.0 |
| 2024-12 | RAN#106 | RP-243063 | 2539 |  | A | (NR_RF_FR1_enh-Core) CR on typo for carrier leakage of intra-band NC CA (R18) | 18.8.0 |
| 2024-12 | RAN#106 | RP-243025 | 2544 |  | F | (HPUE_FR1_TDD_NR_CADC_SUL_R18) CR for TS 38.101-1 to add the missing combo CA_n3A-n28A-n41A-n77A | 18.8.0 |
| 2024-12 | RAN#106 | RP-243037 | 2549 | 1 | F | (NR_channel_raster_enh) CR for TS 38.101-1: Add bands supporting enhanced channel raster | 18.8.0 |
| 2024-12 | RAN#106 | RP-243023 | 2550 |  | F | (4Rx_low_NR_band_handheld_3Tx_NR_CA_ENDC) CR for TS 38.101-1 to correct the wrong referenced clause number for 3Tx | 18.8.0 |
| 2024-12 | RAN#106 | RP-243025 | 2551 | 1 | F | CR 38.101-1 adding missing PC2 harmonic mixing MSD for CA_n26-n78 | 18.8.0 |
| 2024-12 | RAN#106 | RP-243025 | 2552 | 2 | F | CR 38.101-1 correcting PC2 and PC3 IMD MSDs | 18.8.0 |
| 2024-12 | RAN#106 | RP-243035 | 2554 |  | A | (NR_CADC_R17_2BDL_xBUL-Core) CR on 38.101-1 [R18] Some corrections on the MSD table | 18.8.0 |
| 2024-12 | RAN#106 | RP-243063 | 2556 | 1 | F | (NR_redcap_enh-Core) Add eRedCap in the context of requirements | 18.8.0 |
| 2024-12 | RAN#106 | RP-243063 | 2559 |  | A | (NR_RF_FR1) Update the ACLR description for intra-band NC CA | 18.8.0 |
| 2024-12 | RAN#106 | RP-243054 | 2561 |  | A | (NR_newRAT-Core) CR to TS38.101-1: Correction on applicability of minimum requirements | 18.8.0 |
| 2024-12 | RAN#106 | RP-243036 | 2564 | 1 | F | CR 38.101-1 Some editorials and minor clarifications for NR CA | 18.8.0 |
| 2024-12 | RAN#106 | RP-243036 | 2567 |  | F | (NR_CADC_R18_2BDL_xBUL-Core) CR for TS 38.101-1 to fix the BCS 4 and 5 configurations placement for CA_n1-n40 | 18.8.0 |
| 2024-12 | RAN#106 | RP-243052 | 2570 |  | F | (NR_SUL_combos_R18-Core) CR for TS 38.101-1 to align the MSD table format for SUL combos (R18) | 18.8.0 |
| 2024-12 | RAN#106 | RP-243036 | 2571 | 1 | F | Corrections to Harmonic Mixing UL RB allocations and MSD for NR CA | 18.8.0 |
| 2024-12 | RAN#106 | RP-243052 | 2574 | 1 | A | CR on n28 30MHz channel confinement | 18.8.0 |
| 2024-12 | RAN#106 | RP-243025 | 2575 | 1 | F | Re-adding Cross-band and Harmonic Mixing MSD for TDD PC2 UE's supportingTX Diversity | 18.8.0 |
| 2024-12 | RAN#106 | RP-243054 | 2580 |  | A | (NR_newRAT-Core) CR to modify MBW definition - TS38.101-1 | 18.8.0 |
| 2024-12 | RAN#106 | RP-243067 | 2582 |  | A | (NR_newRAT-Core, TEI17) CR to correct the note 1 indication from NS_05 to NS_05U - TS38.101-1 | 18.8.0 |
| 2024-12 | RAN#106 | RP-243052 | 2585 |  | A | (NR_n53-Core) CR to correct Note 6 of Table 7.6.3-2 regarding band n53 OOB - TS38.101-1 | 18.8.0 |
| 2024-12 | RAN#106 | RP-243029 | 2588 |  | F | (LTE_NR_Simult_RxTx_R18) CR to correct the note index of CA_n3-n40-n41 in Table 6_2A_4_2_4_1 - TS38.101-1 | 18.8.0 |
| 2024-12 | RAN#106 | RP-243064 | 2589 |  | F | (NR_SL_enh2-Core) Removal of note index in a table for A-MPR for NS_65 - TS38.101-1 | 18.8.0 |
| 2024-12 | RAN#106 | RP-243038 | 2591 |  | F | (NR_cov_enh2-Core) CR to 38.101-1 for power boosting feature supporting CA | 18.8.0 |
| 2024-12 | RAN#106 | RP-243036 | 2598 |  | F | Cleanup on 38.101-1 for FR1 inter-band DC configuration grouping | 18.8.0 |
| 2024-12 | RAN#106 | RP-243036 | 2603 | 1 | F | CR for TS 38.101-1-i70 Corrections to UL harmonic MSD | 18.8.0 |
| 2024-12 | RAN#106 | RP-243025 | 2604 | 1 | F | (HPUE_FR1_TDD_NR_CADC_SUL_R18) CR for TS 38.101-1-i70 Correction to valid CA configurations and power class | 18.8.0 |
| 2024-12 | RAN#106 | RP-243036 | 2605 | 1 | F | (NR_CADC_R18_2BDL_xBUL-Core) CR for TS 38.101-1-i70 Introducing missing n85 3MHz RSD | 18.8.0 |
| 2024-12 | RAN#106 | RP-243023 | 2607 |  | A | CR to TS 38.101-1: DL CA HPUE | 18.8.0 |
| 2024-12 | RAN#106 | RP-243024 | 1336 |  | F | CR to 38.101-3 correcting duplicated UL configuration | 18.8.0 |

| Change history |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Date | Meeting | TDoc | CR | Rev | Cat | Subject/Comment | New version |  |
| 2024-12 | RAN#106 | RP-243074 | 2518 |  | B | Big CR to 38.101-1 new combinations for HPUE_NR_CADC_SUL_R19 | 19.0.0 |  |
| 2024-12 | RAN#106 | RP-243072 | 2546 |  | B | big CR 38.101-1 for NR_CADC_SUL_R19 | 19.0.0 |  |
| 2024-12 | RAN#106 | RP-243079 | 2562 | 2 | B | CR on introduction of PC2 and 40MHz for n28 | 19.0.0 |  |
| 2025-03 | RAN#107 | RP-250622 | 2610 | 1 | B | CR to 38.101-1 - Introduction of band n68 | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250608 | 2613 |  | A | (NR_unlic_enh-Core) Corrections to the 6GHz unlicensed band NS flags | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250604 | 2618 | 1 | A | CR 38.101-1 R19 Corection for ACS requirement for 3 MHz carrier | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250584 | 2619 |  | A | CR 38.101-1 Clarifications for non-collocated requirements R19 | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250596 | 2625 |  | A | (NR_RF_TxD-Core) Replacement of dual Tx with 2Tx and single Tx with 1Tx | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250608 | 2628 |  | A | (NR_SL_enh2-Core) CR to 38.101-1 Rel-19 Cat-A for 7.6E.3.1A Out-of-band blocking for Sidelink CA | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250627 | 2629 | 1 | B | CR to 38.101-1 on introduction of Band n110 | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250615 | 2638 |  | B | Big CR to 38.101-1 new combinations for HPUE_NR_CADC_SUL_R19 | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250620 | 2639 |  | B | BigCR to 38.101-1: Simultaneous Rx-Tx | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250616 | 2642 | 1 | B | CR for TS 38.101-1 to introduce PC1.5 n104 | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250617 | 2646 | 1 | F | CR on support of UL MIMO for PC2 n28 | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250603 | 2653 |  | A | (  NR_MC_enh-Core) Correct the capability name for Tx switching | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250630 | 2654 |  | B | TS 38.101-1 big CR for NR_bands_xFeature_R19-Core | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250629 | 2659 |  | B | Big CR to 38.101-1 Introduce no DL interruption clarification for CA at dynamic Tx Switching in uplink | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250595 | 2661 |  | A | (NR_RAIL_EU_900MHz, NR_UAV) CR to TS 38101-1 - Wrong references | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250624 | 2662 | 1 | B | Big CR to TS 38.101-1: Adding channel BW support in existing NR bands | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250602 | 2678 |  | F | Corrections to Harmonic Mixing UL allocations | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250599 | 2683 |  | A | (HPUE_NR_FR1_FDD_R18) CR for TS 38.101-1 to clarify A-MPR for NS_43 | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250598 | 2686 |  | A | (HPUE_FR1_TDD_NR_CADC_SUL_R18-Core) Corrections on single uplink carrier for inter-band CA configurations_R19_CAT_A | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250602 | 2688 |  | A | (NR_CADC_R18_2BDL_xBUL-Core) Corrections on inter-band CA reference sensitivity due to intermodulation interference_R19_CAT_A | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250602 | 2690 |  | F | Corrections to 2 3 and 4 NR CA configuration tabels | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250597 | 2694 |  | A | (NR_SL_enh-Core) CR on A-MPR for NS_33 (R19) | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250581 | 2698 |  | A | (5G_V2X_NRSL-Core) CR on SL MIMO configuration (R19) | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250613 | 2699 |  | B | big CR 38.101-1 for NR_CADC_SUL_R19 | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250613 | 2700 |  | F | CR 38.101-1 correcting band combination configuration tables | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250598 | 2708 |  | A | (HPUE_FR1_TDD_NR_CADC_SUL_R18) Cat A CR for TS 38.101-1-j00 Corrections to PC2 harmonic MSD | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250613 | 2709 | 1 | F | (HPUE_NR_CADC_SUL_R19) Cat F CR for TS 38.101-1-j00 Corrections to intra-band non-contiguous MSD | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250609 | 2717 |  | A | (NR_newRAT-Core) Correction of reference to Suspended version of ITU-R SM.329 Recommendation | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250615 | 2720 | 1 | F | CR for 38.101-1 to correct errors and remove redundant CA with TxD table | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250615 | 2721 |  | F | CR for 38.101-1 to correct FDD HPUE notes | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250626 | 2723 |  | B | Big CR for less than 5MHz UE RF requirements in Rel-19 | 19.1.0 |  |
| 2025-03 | RAN#107 | RP-250519 | 2725 |  | B | CR to TS 38.101-1 on introduction NR bands n87 and n88 | 19.1.0 |  |
| 2025-06 | RAN#108 | RP-250953 | 2727 |  | B | BigCR to 38.101-1: Simultaneous Rx-Tx | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250925 | 2730 |  | A | (NR_CADC_R18_3BDL_xBUL-Core) CR to 38.101-1: Correction on CA_n28-n40-n77 (Rel-19) | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250918 | 2733 |  | A | (NR_CADC_R17_3BDL_2BUL-Core)CR to 38.101-1: Correction on CA_n28-n40-n78 (Rel-18) | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250950 | 2737 |  | B | CR to TS 38.101-1: UL MIMO in bands n100 and n101 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250919 | 2740 |  | A | (NR_RAIL_EU_900MHz-Core, NR_RAIL_EU_1900MHz_TDD-Core) CR to TS 38.101-1: Correction to mapping of network signalling table (Rel-19) | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250958 | 2741 | 1 | B | CR to 38.101-1 on adding new channel bandwidth to band n48 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250952 | 2746 |  | F | CR Bugfixes and missing Fallbacks 38101-1-j10_s0505A03-0505A03 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250935 | 2748 |  | A | (TEI18) CR to TS 38.101-1 correction of 4Tx [RF_FR1_4Tx] | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250925 | 2751 | 1 | F | (NR_CADC_R18_2BDL_xBUL) CR to clarify that sources of IMD coming from two CCs in section 7.3A.5 can be from two bands or just a single band - TS38.101-1 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250955 | 2753 |  | A | (HPUE_NR_CADC_SUL_R19) CR for addition and correction of notes in clause 6.2A.1.3 UE MOP for Inter-band CA - TS38.101-1 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250918 | 2756 |  | A | (NR_CADC_R17_2BDL_xBUL-Core) CR to clarify the applicable SCS when UE testing in clause 7.3A.1 - TS 38.101-1 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250918 | 2759 |  | A | (NR_CADC_R17_2BDL_xBUL-Core) CR to correct Band n40 DL Fc used in the configuration for CA_n40-n77 cross band isolation MSD requirements in clause 7.3A.6 - TS38.101-1 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250935 | 2769 |  | A | (TEI18) CR on 38.101-1 clarifications on special sync rasters for n100[Sync_raster_3MHz_n100] | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250962 | 2771 |  | F | CR to TS 38.101-1 - Correction of A-MPR tables for band n68 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250961 | 2773 |  | F | CR to TS 38.101-1 on sync raster correction for band n110 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250957 | 2788 | 1 | B | Introduction of requirements for PC2 operation in band n5 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250957 | 2789 | 1 | B | Introduction of requirements for PC2 operation in band n26 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250935 | 2791 |  | A | (TEI18) CR to 38.101-1 on  adding asymmetric channel bandwidth for n70 UL15/DL10 [n70_asymBW] | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250922 | 2800 |  | F | (HPUE_FR1_TDD_NR_CADC_SUL_R18) CR for 38.101-1 Correct the NOTE for HPUE harmonic/harmonic mixing MSD | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250950 | 2801 |  | B | TS 38.101-1 big CR for NR_bands_xFeature_R19-Core | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250927 | 2805 |  | A | (NR_MC_enh) R19 correction of switchig time between NUL and SUL carriers | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250956 | 2806 | 1 | B | CR for 38.101-1 to introduce PC2 RedCap | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250960 | 2811 |  | F | CR to TS 38.101-1 on addition of 3 MHz channel bandwidth into Annex D.1 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250922 | 2813 |  | A | (  NonCol_intraB_ENDC_NR_CA) CR for 38.101-1 Correct the NOTE for non-collocated CA | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250946 | 2819 |  | B | Big CR for SL intra-band CA | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250927 | 2821 | 1 | A | CR to 38.101-1 to correct switching period reference for UL Tx Switching | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250925 | 2824 |  | A | (NR_CADC_R18_2BDL_xBUL-Core) Corrections on BCS denotation for two bands CA configurations_R19_CAT_A | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250925 | 2826 |  | A | (NR_CADC_R18_3BDL_xBUL-Core)_Corrections on BCS denotation for three bands CA configurations_R19_CAT_A | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250925 | 2828 |  | A | (NR_CADC_R18_yBDL_xBUL-Core)_Corrections on BCS denotation for four and five bands CA configurations_R19_CAT_A | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250925 | 2830 |  | A | (NR_CADC_R18_2BDL_xBUL-Core) Corrections on two bands CA configurations_R19_CAT_A | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250952 | 2831 |  | B | big CR 38.101-1 for NR_CADC_SUL_R19 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250952 | 2832 |  | F | CR 38.101-1 correcting 3 bands NR CA combinatons | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250922 | 2836 |  | A | [HPUE_NR_FR1_FDD_R18-Core] CR to TS38.101-1-i90: Correction to PC2 intra-band contiguous CA REFSENS - CatA | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250924 | 2842 |  | A | (NR_ATG-Core) Rel-19 Clarifications on some ATG requirements applicability per connector | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250925 | 2850 |  | A | CR to TS 38.101-1:Removal of 3 MHz CBW from CA in Rel-18 | 19.2.0 |  |
| 2025-06 | RAN#108 | RP-250955 | 2859 |  | B | Big CR to 38.101-1 new combinations for HPUE_NR_CADC_SUL_R19 | 19.2.0 |  |
| 2025-09 | RAN#109 | RP-252403 | 2860 |  | B | Big CR to 38.101-1 new combinations for HPUE_NR_CADC_SUL_R19 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252378 | 2865 |  | A | (NR_newRAT-Core, NR_FR1_lessthan_5MHz_BW-Core) CR to TS 38.101-1 on the channel bandwidth list in the normative Annex D | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252388 | 2872 |  | A | CR to TS 38.101-1 - Correction to A-MPR for CA_NS_04 (Rel-19) | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252414 | 2873 |  | F | CR to TS 38.101-1 - Correction of A-MPR NS_36 table for band n68 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252431 | 2875 | 1 | F | CR for TS 38.101-1 to clarify the REFSENS requirements for PC2 TDD HD-FDD RedCap UE | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252427 | 2876 | 2 | F | CR for TS 38.101-1 to modify the delta MPR errors for PC2 n28 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252404 | 2884 |  | F | CR to 38.101-1 on removing wrong REFSENS entry for 30MHz CBW of band n5 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252417 | 2885 |  | F | CR to 38.101-1 Rel-19 Band Combination Bug Fixes | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252381 | 2887 |  | A | CR to 38.101-1 Rel-18 Band Combination Bug Fixes CATA Rel19 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252423 | 2898 | 2 | B | (NR_LBCA_Sw-Core) Introducing low NR band aggregation via switching to TS38.101-1 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252380 | 2902 |  | A | (LTE_NR_DC_CA_enh-Core) CR on typo of inter-band NR DC configuration | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252384 | 2906 |  | A | (NR_RF_FR1-Core) CR on editorial change for CA channel arrangement | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252412 | 2907 |  | B | Big CR on 38.101-1 for Support of intra-band non-collocated EN-DC/NR-CA deployment Phase 2 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252399 | 2910 | 1 | B | CR 38.101-1 on time mask of Tx switching for 3Tx UEs [TxSwitch_R19] | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252384 | 2914 |  | A | (NR_unlic-Core) CR to correct the frequency offset of the interferer used in clause 7.5F.1 - TS38.101-1 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252381 | 2917 |  | A | (NR_CADC_R17_2BDL_xBUL-Core) CR to correct and clarify the applicable RB allocations for 30kHz SCS when UE testing in clause 7.3A.1 - TS 38.101-1 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252381 | 2920 |  | F | (NR_CADC_R17_3BDL_2BUL-Core) CR to correct DL Fc in some REFSENS exceptions not respecting default duplex distance in clause 7.3A.5 - TS 38.101-1 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252378 | 2926 |  | A | (NR_newRAT-Core) CR to add Lcrb in Figure 5.3.1-1 - TS 38.101-1 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252389 | 2928 |  | A | (4Rx_low_NR_band_handheld_3Tx_NR_CA_ENDC-Core) CR to correct the typo Clrb for Lcrb in clause 7.3A.5 – TS 38.101-1 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252419 | 2939 | 1 | B | Big formal CR for TS38.101-1 for HPUE objective | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252391 | 2941 |  | A | (NR_ENDC_RF_FR1_enh2-Core)Correction CR for TS 38.101-1 for 4Tx_Rel-19 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252381 | 2946 |  | A | (NR_CA_R16_intra-Core) CR to TR 38.101-1 on symbols for NR carrier aggregation_R19_CAT_A | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252381 | 2948 |  | A | (NR_CADC_R18_2BDL_xBUL-Core) CR to TR 38.101-1 on corrections to band number for CA_n8A-n77A reference sensitivity_R19_CAT_A | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252413 | 2949 |  | B | Big CR on TS 38.101-1 to introduce R19 ATG UE RF requirements (NR_ATG_enh-Core) | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252424 | 2958 | 1 | B | Big CR for LP-WUS UE RF requirements in Rel-19 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252391 | 2963 |  | A | (NR_channel_raster_enh-Core) Correction to nominal CA spacing to accommodate UE-specific channel bandwidths | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252380 | 2967 |  | A | (  LTE_NR_B41_Bn41_PC29dBm-Core) CR to TS38.101-1 Corrections on configured transmitted power | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252397 | 2974 |  | B | Big CR to 38.101-1 Introduce no DL interruption clarification for CA at dynamic Tx Switching in uplink | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252381 | 2976 |  | F | (NR_CADC_R18_2BDL_xBUL-Core) Correct the harmonic MSD test point for CA_n5-n77 and CA_n77-n85 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252389 | 2978 |  | A | (NR_cov_enh2-Core) CR for 38.101-1 Correct the NOTE for MPR power boosting | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252385 | 2981 |  | F | (NR_PC2_CA_R17_2BDL_2BUL) Remove the footnote for the HPUE band combination | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252415 | 2982 |  | B | TS 38.101-1 big CR for NR_bands_xFeature_R19-Core | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252395 | 2986 | 2 | A | CR to 38.101-1 Rel-19. To add indication of modified MPR behavior [PHS_System_NRonly] | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252419 | 2988 | 1 | B | Big CR for TS 38.101-1: Introduction of MPR reduction | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252378 | 2999 |  | A | CR on clarification of maximum number of RB’s for n50 asymmetric UL/DL BW’s | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252383 | 3002 |  | A | CR on clarification of UL/DL bandwidths on overlapping NR SUL and NR bands | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252417 | 3004 |  | F | CR for 38.101-1 to correct UL configurations for inter-band BCs CA_n2A-n48A and CA_n2A-n48B | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252417 | 3005 |  | B | Big CR 38.101-1 for NR_CADC_SUL_R19 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252380 | 3009 |  | A | (NR_6GHz-Core) CR to 38.101-1 correction on the band definition for n104 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252419 | 3014 |  | B | Big CR to TS38.101-1: Introduction of requirements for 6Rx | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252417 | 3016 |  | F | CR 38.101-1 correcting 4DL configurations | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252383 | 3023 |  | A | (NR_SUL_combos_R16-Core) CR to TS 38.101-1 Rel-19 cat A, SUL and CA requirements | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252388 | 3026 |  | A | (NR_redcap-Core) CR to TS 38.101-1: OOB blocking for RedCap UEs | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252404 | 3028 |  | F | CR to TS 38.101-1: n26 PC2 - adding missing content to A-MPR summary table | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252404 | 3029 | 1 | F | CR to TS 38.101-1: NS_48 and NS_49 A-MPR corrections | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252393 | 3033 |  | A | CR to TS 38.101-1: Correction of the reference to the updated ECC/DEC/(22)07 decision on harmonised technical conditions for the usage of aerial UE | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252399 | 3040 | 2 | F | (TEI19) CR to TS38.101-1 j20: Corrections to n28 and n41 UE coex spurious emissions – CatF [UE_coex_spurs_CA] | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252425 | 3041 | 1 | B | Big CR for TS 38.101-1 to introduce FR1 3Tx RF requirements | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252420 | 3042 |  | B | Big CR on 7 MHz Channel Bandwidth for bands n5 and n26 | 19.3.0 |  |
| 2025-09 | RAN#109 | RP-252399 | 3043 |  | B | CR to 38.101-1 Updated PHS requirement for band n1 [PHS_system_NRonly] | 19.3.0 |  |
| 2025-09 | RAN#109 |  |  |  |  | Editorial correction | 19.3.1 |  |
| 2025-12 | RAN#110 | RP-253666 | 3047 | 1 | F | CR for TS 38.101-1 to introduce DL RMC for LB-LB CA via switching | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253641 | 3048 | 1 | B | CR for TS 38.101-1 to introduce 2U/2D CA_n5-n8 | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253671 | 3052 |  | A | (NR_CADC_R17_2BDL_xBUL-Core) CR for TS 38.101-1 to modify the RB allocations for MSD tests of 30kHz SCS bands. | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253659 | 3054 |  | F | CR to R19 38.101-1 to introduce extended bandwidth capability for PC2 2Tx and exclude 7MHz CBW | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253640 | 3055 | 1 | F | (NR_CADC_SUL_R19-Core) CR to 38.101-1-j31 to change MSD for band n41 10MHz CBW and to remove redundant dual-UL IMD MSD | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253640 | 3056 | 1 | F | (NR_CADC_SUL_R19-Core) CR to 38.101-1-j31 on Band n71 mandatory support of 25MHz CBW | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253640 | 3057 |  | F | (NR_CADC_SUL_R19-Core) CR to TS38.101-1-j31: Correction and missing harmonic mixing MSD - Cat-F | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253640 | 3058 |  | F | (NR_CADC_SUL_R19-Core) CR to 38.101-1-j31 correction to CA_NS_27 | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253643 | 3059 |  | B | (HPUE_NR_CADC_SUL_R19) CR on SUL missing MSD and HPUE MSD requirements simplification | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253644 | 3060 |  | B | CR to TS 38.101-1 on introduction of HPUE CA and DC in bands n100 and n101 for FRMCS | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253659 | 3061 |  | F | (NR_ENDC_RF_Ph4-Core)Correction CR for 38.101-1 for Rel-19 HPUE | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253671 | 3069 |  | A | (NR_CADC_R17_2BDL_xBUL) CR to correct the n70 UL and DL CHBWs used for CA_n48-n70 requirement in clause 7.3A.5 - TS 38.101-1 | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253659 | 3071 |  | F | CR on open issues of MPR enhancement | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253640 | 3072 | 1 | F | CR-Bugfix 38101-1-j31_s0505A03-0505A03 | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253640 | 3073 | 1 | F | CR Missing UL Fallbacks 38101-1-j31_s0505A03-0505A03 | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253659 | 3074 | 1 | F | CR for 38.101-1 on enabling HPUE support for band combinations without HPUE applicability notes in clause 5 | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253675 | 3079 |  | F | (NR_NewRAT-Core, TEI19) CR for 38.101-1: Correction on NR FDD band REFSENS UL configurations R19 Cat F [REFSENS_ULConfig_R19] | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253661 | 3080 |  | F | (NonCol_intraB_ENDC_NR_CA_Ph2) Type 4 UE requirement alignment with RAN2 signalling | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253651 | 3083 |  | F | CR to TS38.101-1 on transmission bandwidth configuration for LP-WUS | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253649 | 3084 |  | F | CR to TS38.101-1 on 3Tx MIMO Rx requirements | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253671 | 3087 |  | A | (NR_CADC_R17_3BDL_2BUL-Core) CR for 38.101-1: Rel-17 Missing MSD for CA_n25A-n41A-n71A | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253667 | 3089 |  | A | (HPUE_FR1_TDD_NR_CADC_SUL_R18-Core) CR for 38.101-1: Rel-18 Missing MSD for CA_n25A-n41A-n71A | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253662 | 3092 |  | F | CR to TS38.101-1: correction on ATG DL CA | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253646 | 3097 |  | F | CR 38.101-1 Maintenance for time mask of Tx switching for 3Tx UEs [TxSwitch_R19] | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253682 | 3101 |  | A | (NR_RF_FR1-Core) Correction to Rel-16 inter-band CA time mask | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253682 | 3105 |  | A | Clarification of the bandwidth of guard bands for intra-band contiguous CA | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253659 | 3106 |  | F | (NR_ENDC_RF_Ph4) CR to TS 38.101-1: Corrections for UE RF enhancements | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253659 | 3112 |  | F | CR for 38.101-1 Clarification on the requirement for CA+TxD | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253659 | 3113 |  | F | CR to TS38.101-1_Remove square bracket for the 3T6R IE | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253638 | 3114 |  | B | TS 38.101-1 big CR for NR_bands_xFeature_R19-Core | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253643 | 3115 |  | B | Big CR to 38.101-1 new combinations for HPUE_NR_CADC_SUL_R19 | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253643 | 3116 | 1 | F | (HPUE_NR_CADC_SUL_R19-Core) CR for correction on missing PC2 NOTE for CA_n1-n78-n79 and CA_n28-n78-n79 | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253643 | 3117 | 1 | B | (HPUE_NR_CADC_SUL_R19-Core) CR for adding PC2 NOTE for BCS4 and BCS5 of CA_n28-n78-n79 | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253682 | 3121 | 1 | A | (NR_RF_FR1) R19 correction on modifiedMPR-Behaviour | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253640 | 3126 |  | B | Big CR 38.101-1 for NR_CADC_SUL_R19 | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253640 | 3130 |  | F | CR 38.101-1 correcting missing return ? for 2DL DC combinations | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253640 | 3131 |  | F | CR 38.101-1 correcting missing return ? for 3DL DC combinations | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253640 | 3132 |  | F | CR 38.101-1 correcting missing return ? for 4DL DC combinations | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253680 | 3135 |  | A | (NR_RAIL_EU_1900MHz_TDD-Core) CR to TS 38.101-1: Annex M corrections for FRMCS operation | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253680 | 3145 |  | A | (NR_RAIL_HPUE_n100_n101-Core) CR to TS 38.101-1: n101 MPR | 19.4.0 |  |
| 2025-12 | RAN#110 | RP-253681 | 3147 | 1 | A | CR to 38.101-1 for eRedCap channel bandwidth | 19.4.0 |  |
| 2026-03 | RAN#111 | RP-260465 | 3155 |  | A | CR for TS 38.101-1 to remove brackets in the Table 6.2D.2-2 for PC1.5 with 2Tx | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260444 | 3156 |  | F | CR for TS 38.101-1 to void the NOTE 6 in table 5.3.5-1 | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260446 | 3158 |  | F | CR to TS 38.101-1 to introduce an enhanced power extended inner allocation region | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260444 | 3160 |  | F | (NR_CADC_SUL_R19-Core) CR for correction of the DL Fc on MSD table for PC1.5 CA_n1-n78 | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260446 | 3161 |  | F | (NR_ENDC_RF_Ph4-Core) CR on MPR for Contiguous RB allocation for Power Class 1.5 with 2Tx | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260452 | 3178 |  | A | (NR_CADC_R18_2BDL_xBUL-Core) CR to TS38.101-1: Remove UL3/DL1 harmonic near-miss MSD cases | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260444 | 3198 |  | F | CR 38.101-1 corrections NR CA configurations | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260444 | 3200 |  | F | CR 38.101-1 correcting PC2 note in CA_n3A-n7A-n20A | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260444 | 3201 |  | F | (NR_CADC_SUL_R19) CR to 38101-1 Corrections to BT band combinations with band n1, n3, n7, n28, n75 and n78 | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260444 | 3204 |  | F | CR to TS38.101-1 for correcting HPUE notes to CA_n3A-n28A-n41A | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260444 | 3207 |  | F | (NR_CADC_SUL_R19-Core, ) CR to correct Fc for some MSDs for CA_n5-n28-n78, CA_n40-n41-n79, CA_n40-n71-n77, CA_n41-n74-n77 in clause 7.3A.5 - Rel-19 TS 38.101-1 | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260446 | 3215 |  | F | (NR_ENDC_RF_Ph4-Core) CR to TS 38.101-1: PC1.5 Inter-band CA correction | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260444 | 3216 |  | F | Corrections for HPUE notes | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260444 | 3217 |  | F | Corrections for HPUE MOP table | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260456 | 3171 | 1 | A | (NR_newRAT-Core)CR to generalize band edge relaxation for UL MIMO_Rel-19 | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260444 | 3151 | 1 | F | CR-Bugfix 38.101-1 | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260446 | 3163 | 1 | F | (NR_ENDC_RF_Ph4-Core) CR on HPUE MSD simplification requirements for TS38.101-1 | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260446 | 3172 | 1 | F | CR to 38101-1-j40 on DeltaMSD correction for UL configurations including intra-band ULCA | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260446 | 3176 | 1 | F | CR for TR38.101-1 Correct the IE name for LBCA switching | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260446 | 3180 | 1 | F | CR for TS38.101-1 Clarification on HD-FDD REFSEN for PC3 Redcap | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260441 | 3159 | 2 | B | (TEI19) CR to enable 4Tx inter-band UL CA [4Tx_UL_CA] | 19.5.0 |  |
| 2026-03 | RAN#111 | RP-260444 | 3211 | 2 | F | CR for TS 38.101-1 Rel-19 to correct an inconsistency issue | 19.5.0 |  |
| 2026-06 | RAN#112 | RP-261410 | 3222 |  | A | (NR_SAR_PC2_interB_SUL_2BUL) CR for correcting power class configuration in triggering default power class behavior | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261410 | 3231 |  | A | CR on correction for n50 NS_42 CBW 30 MHz A-MPR region and adding missing BW in NS_41 and NS_42 emission requirements tables | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261388 | 3233 |  | F | (HPUE_NR_FR1_bands_R19-Core) CR to TS 38.101-1 on correction of HPUE CA and DC in bands n100 and n101 for FRMCS | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261388 | 3234 |  | F | CR on adding missing PC3 MSD for CA_n3B with 1UL CC | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261388 | 3236 | 1 | F | (NR_CADC_SUL_R19) CR for TS38.101-1 Rel-19_Correction on CA_n3A-n77(3A) | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261395 | 3237 |  | F | CR for TS 38.101-1 to modify IE name for R19 Low bands CA via switching | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261408 | 3239 |  | A | CR for TS 38.101-1 to clarify the boundary for EVM equalizer spectrum flatness | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261388 | 3242 |  | F | CR for TS 38.101-1 add CA_n3-n71 and CA_n40-n71 to clause 5 [TEI19 with Cat.F, NR_CADC_SUL_R19-Core] | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261388 | 3243 |  | F | CR for TS 38.101-1 to correct SUL combination notation [TEI19 with Cat.F, NR_CADC_SUL_R19-Core] | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261388 | 3249 | 1 | F | Addition of clause 6 content for already agreed HPUE combinations of n25, n41, n66 and n71 | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261399 | 3257 | 1 | F | (NR_CADC_R17_2BDL_xBUL-Core, ) CR to clarify the applicable RB allocations for 30kHz SCS when UE testing and correct some values in clause 7.3A - TS 38.101-1 | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261399 | 3260 |  | A | (NR_CADC_R17_2BDL_xBUL-Core, ) CR to add missing Lcrb values in Table A2.2.2-1 - TS 38.101-1 | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261411 | 3267 |  | A | (NR_RF_FR1) R19 correction on Tx switching period | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261407 | 3270 |  | A | (NR_6GHz-Core) CR to TS 38.101-1: Correct the Single Carrier Tx requirements for n104 | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261392 | 3271 |  | F | (NR_ENDC_RF_Ph4-Core) CR on signaling for Rel-18 power boosting and Rel-19 MPR reduction feature combiantion | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261400 | 3281 |  | A | (LTE_NR_HPUE_FWVM_R18-Core) CR to TS 38.101-1: n7 NS_46 PC1 A-MPR | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261388 | 3282 |  | F | (HPUE_NR_CADC_SUL_R19-Core) CR to correct the DL Fc for CA_n28-n41-n79 in clause 7.3A.5-2a PC2 - Rel-19 TS 38.101-1 | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261388 | 3287 | 1 | F | (HPUE_NR_CADC_SUL_R19) Inter-band CA HPUE corrections | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261388 | 3289 |  | F | (NR_CADC_SUL_R19-Core) Correction to NS_27. | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261393 | 3290 |  | F | CR on correcting n68 REFSENS UL configuration | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261410 | 3293 |  | A | Correction on configured transmitted power for SUL | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261388 | 3295 |  | F | (HPUE_NR_CADC_SUL_R19) Removal of Note 7 for NS_05 | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261396 | 3296 | 2 | B | CR for TS38.101-1 to add UL25/DL30 and UL25/DL35 asymmetric bandwidth combinations to n71 [n71_asym_BCS3] | 19.6.0 |  |
| 2026-06 | RAN#112 | RP-261388 | 3297 |  | F | CR Modifications to HPUE MSD Look up tables | 19.6.0 |  |
