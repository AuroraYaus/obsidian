# Foreword

This Technical Specification has been produced by the 3rd Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

x the first digit:

## 1 presented to TSG for information;

## 2 presented to TSG for approval;

## 3 or greater indicates TSG approved document under change control.

y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.

z the third digit is incremented when editorial only changes have been incorporated in the document.

# 1 Scope

The present document describes the physical channels for evolved UTRA.

# 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or nonspecific.

- For a specific reference, subsequent revisions do not apply.

- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2] TS 36.201: "Evolved Universal Terrestrial Radio Access (E-UTRA); LTE physical layer; General description".

[3] TS36.212: "Evolved Universal Terrestrial Radio Access (E-UTRA); Multiplexing and channel coding".

[4] TS36.213: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer procedures".

[5] TS 36.214: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer; Measurements".

[6] TS36.104: "Evolved Universal Terrestrial Radio Access (E-UTRA); Base Station (BS) radio transmission and reception".

[7] TS36.101: "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) radio transmission and reception".

[8] TS 36.321, "Evolved Universal Terrestrial Radio Access (E-UTRA); Medium Access Control (MAC) protocol specification".

[9] TS 36.331, "Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC) Protocol specification"

[10] TS 36.304, "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) procedures in idle mode"

[11] TS 37.213: "Physical layer procedures for shared spectrum channel access"

[12] TS 36.300: "Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Overall description; Stage 2"

# 3 Symbols and abbreviations

## 3.1 Symbols

For the purposes of the present document, the following symbols apply:

![](media_svg/image1.svg) [公式: (k,l)] Resource element with frequency-domain index ![](media_svg/image2.svg) [公式: k] and time-domain index ![](media_svg/image3.svg) [公式: l]

![](media_svg/image4.svg) [公式≈: _{a}_{k}(_{,}p_{l})] Value of resource element ![](media_svg/image1.svg) [公式: (k,l)] [for antenna port![](media_svg/image5.svg) [公式: p]]

![](media_svg/image6.svg) [公式: D] Matrix for supporting cyclic delay diversity

![](media_svg/image7.svg) [公式≈: ^{D}RA] Density of random access opportunities per radio frame

![](media_svg/image8.svg) [公式≈: ^{f}0] Carrier frequency

![](media_svg/image9.svg) [公式≈: ^{f}RA] PRACH resource frequency index within the considered time-domain location

![](media_svg/image10.svg) [公式≈: ^{f}PRB,^{PRACH}hop] PRACH frequency hopping offset, expressed as a number of resource blocks

![](media_svg/image11.svg) [公式≈: ^{l}NPDCCHStart] Start symbol in slot 0 for NPDCCH

![](media_svg/image12.svg) [公式≈: ^{l}NPDSCHStart] Start symbol in slot 0 for NPDSCH

![](media_svg/image13.svg) [公式≈: _{M}_{sc}PSBCH] Bandwidth for PSBCH transmission, expressed as a number of subcarriers

![](media_svg/image14.svg) [公式≈: _{M}_{RB}PSBCH] Bandwidth for PSBCH transmission, expressed as a number of resource blocks

![](media_svg/image15.svg) [公式≈: _{M}_{sc}PSCCH] Bandwidth for PSCCH transmission, expressed as a number of subcarriers

![](media_svg/image16.svg) [公式≈: _{M}_{RB}PSCCH] Bandwidth for PSCCH transmission, expressed as a number of resource blocks

![](media_svg/image17.svg) [公式≈: _{M}_{sc}PSDCH] Bandwidth for PSDCH transmission, expressed as a number of subcarriers

![](media_svg/image18.svg) [公式≈: _{M}_{RB}PSDCH] Bandwidth for PSDCH transmission, expressed as a number of resource blocks

![](media_svg/image19.svg) [公式≈: _{M}_{sc}PSSCH] Scheduled bandwidth for PSSCH transmission, expressed as a number of subcarriers

![](media_svg/image20.svg) [公式≈: _{M}_{RB}PSSCH] Scheduled bandwidth for PSSCH transmission, expressed as a number of resource blocks

![](media_svg/image21.svg) [公式≈: _{M}_{sc}PUSCH] Scheduled bandwidth for uplink transmission, expressed as a number of subcarriers

![](media_svg/image22.svg) [公式≈: _{M}_{RB}PUSCH] Scheduled bandwidth for uplink transmission, expressed as a number of resource blocks

![](media_svg/image23.svg) [公式≈: _{M}_{rep}NPUSCH] Scheduled number of repetitions of a NPUSCH transmission

![](media_svg/image24.svg) [公式≈: _{M}_{rep}NPDSCH] Scheduled number of repetitions of a NPDSCH transmission

![](media_svg/image25.svg) [公式≈: _{M}_{sc}NPUSCH] Scheduled bandwidth for uplink NPUSCH transmission, expressed as a number of subcarriers

![](media_svg/image26.svg) [公式≈: ^{M}identical^{NPUSCH}] Number of repetitions of identical slots for NPUSCH

![](media_svg/image27.svg) [公式≈: _{M}_{bit}(q)] Number of coded bits to transmit on a physical channel [for codeword ![](media_svg/image28.svg) [公式: q]]

![](media_svg/image29.svg) [公式≈: ^{M}symb^{(q)}] Number of modulation symbols to transmit on a physical channel [for codeword ![](media_svg/image28.svg) [公式: q]]

![](media_svg/image30.svg) [公式≈: _{M}_{symb}layer] Number of modulation symbols to transmit per layer for a physical channel

![](media_svg/image31.svg) [公式≈: ^{M}symb^{ap}] Number of modulation symbols to transmit per antenna port for a physical channel

Number of consecutive subcarriers in an UL resource unit for PUSCH sub-PRB allocation

Number of slots in an UL resource unit for PUSCH sub-PRB allocation

Number of SC-FDMA symbols in an uplink slot for PUSCH sub-PRB allocation

Number of subcarriers in the frequency domain for PUSCH sub-PRB allocation

$ M_{seq}^{RU}$ Number of reference signal sequences available for the UL resource unit size for PUSCH sub-PRB allocation

$ M_{RU}$ Number of scheduled UL resource units for PUSCH sub-PRB allocation

![](media_svg/image35.svg) [公式: N] A constant equal to 2048 for ![](media_svg/image36.svg) [公式: δf=15kHz], 4096 for ![](media_svg/image37.svg) [公式: δf=7.5kHz] and 8192 for ![](media_svg/image38.svg) [公式: δf=3.75kHz]

![](media_svg/image39.svg) [公式≈: ^{N}CP,l] Downlink cyclic prefix length for OFDM symbol ![](media_svg/image3.svg) [公式: l] in a slot

![](media_svg/image40.svg) [公式≈: ^{N}CS] Cyclic shift value used for random access preamble generation

![](media_svg/image41.svg) [公式≈: _{N}_{cs}(1)] Number of cyclic shifts used for PUCCH formats 1/1a/1b in a resource block with a mix of formats 1/1a/1b and 2/2a/2b

![](media_svg/image42.svg) [公式≈: _{N}_{RB}(2)] Bandwidth available for use by PUCCH formats 2/2a/2b, expressed in multiples of ![](media_svg/image43.svg) [公式≈: _{N}_{sc}RB]

![](media_svg/image44.svg) [公式≈: _{N}_{RB}HO] The offset used for PUSCH frequency hopping, expressed in number of resource blocks (set by higher layers)

![](media_svg/image45.svg) [公式≈: _{N}_{ID}cell] Physical layer cell identity

![](media_svg/image46.svg) [公式≈: _{N}_{ID}Ncell] Narrowband physical layer cell identity

![](media_svg/image47.svg) [公式≈: _{N}_{ID}MBSFN] MBSFN area identity

![](media_svg/image48.svg) [公式≈: _{N}_{ID}SL] Physical layer sidelink synchronization identity

![](media_svg/image49.svg) [公式≈: _{N}_{ID}PRS] Positioning reference signal identity

![](media_svg/image50.svg) [公式≈: _{N}_{RB}DL] Downlink bandwidth configuration, expressed in multiples of ![](media_svg/image43.svg) [公式≈: _{N}_{sc}RB]

![](media_svg/image51.svg) [公式≈: _{N}_{RB}min,DL] Smallest downlink bandwidth configuration, expressed in multiples of ![](media_svg/image43.svg) [公式≈: _{N}_{sc}RB]

![](media_svg/image52.svg) [公式≈: _{N}_{RB}max,DL] Largest downlink bandwidth configuration, expressed in multiples of ![](media_svg/image43.svg) [公式≈: _{N}_{sc}RB]

![](media_svg/image53.svg) [公式≈: _{N}_{RB}UL] Uplink bandwidth configuration, expressed in multiples of ![](media_svg/image43.svg) [公式≈: _{N}_{sc}RB]

![](media_svg/image54.svg) [公式≈: _{N}_{RB}min, UL] Smallest uplink bandwidth configuration, expressed in multiples of ![](media_svg/image43.svg) [公式≈: _{N}_{sc}RB]

![](media_svg/image55.svg) [公式≈: _{N}_{RB}max, UL] Largest uplink bandwidth configuration, expressed in multiples of ![](media_svg/image43.svg) [公式≈: _{N}_{sc}RB]

![](media_svg/image56.svg) [公式≈: _{N}_{RB}SL] Sidelink bandwidth configuration, expressed in multiples of ![](media_svg/image43.svg) [公式≈: _{N}_{sc}RB]

$ N_{RSS}$ Duration of RSS measured in subframes

![](media_svg/image57.svg) [公式≈: ^{N}SF] Number of scheduled subframes for NPDSCH transmission

![](media_svg/image58.svg) [公式≈: _{N}_{symb}NPSS] Number of symbols for NPSS in a subframe

![](media_svg/image59.svg) [公式≈: _{N}_{symb}NSSS] Number of symbols for NSSS in a subframe

![](media_svg/image60.svg) [公式≈: _{N}_{sc}RU] Number of consecutive subcarriers in an UL resource unit for NB-IoT

![](media_svg/image61.svg) [公式≈: ^{N}seq^{RU}] Number of reference signal sequences available for the UL resource unit size

![](media_svg/image62.svg) [公式≈: ^{N}RU] Number of scheduled UL resource units for NB-IoT

![](media_svg/image63.svg) [公式≈: _{N}_{NB}UL] Total number of uplink narrowbands

![](media_svg/image64.svg) [公式≈: _{N}_{WB}UL] Total number of uplink widebands

![](media_svg/image65.svg) [公式≈: _{N}_{sc}UL] Number of subcarriers in the frequency domain for NB-IoT

![](media_svg/image66.svg) [公式≈: ^{N}acc] Number of consecutive absolute subframes over which the scrambling sequence stays the same

![](media_svg/image67.svg) [公式≈: _{N}_{abs}PUSCH] Total number of absolute subframes a PUSCH with repetition spans expressed as a number of absolute subframes

![](media_svg/image68.svg) [公式≈: _{N}_{rep}PUSCH] Number of repetitions of a PUSCH transmission

![](media_svg/image69.svg) [公式≈: _{N}_{NB}ch,UL] Number of consecutive absolute subframes over which PUCCH or PUSCH stays at the same narrowband before hopping to another narrowband, expressed as a number of absolute subframes

![](media_svg/image70.svg) [公式≈: ^{f}NB,^{PUSCH}hop] Narrowband offset between one narrowband and the next narrowband a PUSCH hops to, expressed as a number of uplink narrowbands

![](media_svg/image71.svg) [公式≈: _{N}_{abs}PUCCH] Total number of absolute subframes a PUCCH with repetition spans, expressed as a number of absolute subframes

![](media_svg/image72.svg) [公式≈: _{N}_{rep}PUCCH] Number of repetitions of a PUCCH transmission

![](media_svg/image73.svg) [公式≈: _{N}_{rep}PRACH] Number of PRACH repetitions per preamble transmission attempt

![](media_svg/image74.svg) [公式≈: _{N}_{sf}RA] Number of subframes allowed for preamble transmission within a 1024-frame interval

![](media_svg/image75.svg) [公式≈: _{N}_{start}PRACH] PRACH starting subframe periodicity

![](media_svg/image76.svg) [公式≈: _{N}_{rep}NPRACH] Number of NPRACH repetitions per preamble transmission attempt

![](media_svg/image77.svg) [公式≈: _{N}_{period}NPRACH] NPRACH resource periodicity

![](media_svg/image78.svg) [公式≈: ^{N}scoffset^{NPRACH}] Frequency location of the first sub-carrier allocated to NPRACH

![](media_svg/image79.svg) [公式≈: _{N}_{sc}NPRACH] Number of sub-carriers allocated to NPRACH

![](media_svg/image80.svg) [公式≈: ^{N}sc_cont ^{NPRACH}] Number of starting sub-carriers allocated for UE initiated random access

![](media_svg/image81.svg) [公式≈: _{N}_{start}NPRACH] NPRACH starting subframe

![](media_svg/image82.svg) [公式≈: _{N}_{MSG3}NPRACH] Fraction for starting subcarrier index for UE support for multi-tone msg3 transmission

![](media_svg/image83.svg) [公式≈: ^{N}gap,period] Periodicity for NPDSCH/NPDCCH gaps

![](media_svg/image84.svg) [公式≈: ^{N}gap,duration] Duration for NPDSCH/NPDCCH gaps

![](media_svg/image85.svg) [公式≈: ^{N}gap,threshold] Threshold for applying NPDSCH/NPDCCH gaps

![](media_svg/image86.svg) [公式≈: _{N}_{NB}DL] Total number of downlink narrowbands

![](media_svg/image87.svg) [公式≈: _{N}_{WB}DL] Total number of downlink widebands

![](media_svg/image88.svg) [公式≈: _{N}_{abs}PDSCH] Total number of absolute subframes a PDSCH with repetition spans, expressed as a number of absolute subframes

![](media_svg/image89.svg) [公式≈: _{N}_{rep}PDSCH] Number of repetitions of a PDSCH transmission

![](media_svg/image90.svg) [公式≈: _{N}_{NB}ch,DL] Number of consecutive absolute subframes over which MPDCCH or PDSCH stays at the same narrowband before hopping to another narrowband, expressed as a number of absolute subframes

![](media_svg/image91.svg) [公式≈: ^{N}NB,^{ch,}^{DL}hop] Number of narrowbands over which MPDCCH or PDSCH frequency hops

![](media_svg/image92.svg) [公式≈: ^{f}NB,^{DL}hop] Narrowband offset between one narrowband and the next narrowband an MPDCCH or PDSCH hops to, expressed as a number of downlink narrowbands

![](media_svg/image93.svg) [公式≈: _{N}_{PDSCH}SIB1-BR] Number of times a PDSCH carrying SIB1-BR is transmitted over 8 radio frames

![](media_svg/image94.svg) [公式≈: _{N}_{abs}MPDCCH] Total number of absolute subframes a MPDCCH with repetition spans, expressed as a number of absolute subframes

![](media_svg/image95.svg) [公式≈: _{N}_{rep}MPDCCH] Number of repetitions of a MPDCCH transmission

![](media_svg/image96.svg) [公式≈: _{N}_{abs,}MPDCCH_{ss}] Total number of absolute subframes a MPDCCH search space with maximum repetition level spans, expressed as a number of absolute subframes

![](media_svg/image97.svg) [公式≈: _{N}_{rep,}MPDCCH_{ss}] Maximum repetition level of a MPDCCH search space

![](media_svg/image98.svg) [公式≈: _{N}_{ECCE}MPDCCH] Number of ECCEs in a subframe for one MPDCCH

![](media_svg/image99.svg) [公式≈: ^{N}symb^{DL}] Number of OFDM symbols in a downlink slot

![](media_svg/image100.svg) [公式≈: ^{N}symb^{UL}] Number of SC-FDMA symbols in an uplink slot

![](media_svg/image101.svg) [公式≈: _{N}_{symb}retune] Number of symbols in a guard period for narrowband or wideband retuning

![](media_svg/image102.svg) [公式≈: ^{N}slots^{UL}] Number of consecutive slots in an UL resource unit for NB-IoT

![](media_svg/image103.svg) [公式≈: ^{N}symb^{SL}] Number of SC-FDMA symbols in a sidelink slot

![](media_svg/image43.svg) [公式≈: _{N}_{sc}RB] Resource block size in the frequency domain, expressed as a number of subcarriers

![](media_svg/image104.svg) [公式≈: ^{N}sb] Number of sub-bands for PUSCH frequency-hopping with predefined hopping pattern

![](media_svg/image105.svg) [公式≈: _{N}_{RB}sb] Size of each sub-band for PUSCH frequency-hopping with predefined hopping pattern, expressed as a number of resource blocks

![](media_svg/image106.svg) [公式≈: _{N}_{sc}RA] Size of narrow-band random-access resource in number of subcarriers

![](media_svg/image107.svg) [公式≈: ^{N}SP] Number of downlink to uplink switch points within the radio frame

![](media_svg/image108.svg) [公式≈: _{N}_{RS}PUCCH] Number of reference symbols per slot for PUCCH

Number of reference symbols per subslot or per slot for SPUCCH

![](media_svg/image110.svg) [公式≈: ^{N}TA] Timing offset between uplink and downlink radio frames at the UE, expressed in units of ![](media_svg/image111.svg) [公式≈: ^{T}s]

![](media_svg/image112.svg) [公式≈: ^{N}TA offset] Fixed timing advance offset, expressed in units of ![](media_svg/image111.svg) [公式≈: ^{T}s]

![](media_svg/image113.svg) [公式≈: ^{N}TA,SL] Timing offset between sidelink and timing reference frames at the UE, expressed in units of ![](media_svg/image111.svg) [公式≈: ^{T}s]

![](media_svg/image114.svg) [公式≈: _{n}_{PUCCH}(1,^{~}p)] Resource index for PUCCH formats 1/1a/1b

![](media_svg/image115.svg) [公式≈: _{n}_{PUCCH}(2,^{~}p)] Resource index for PUCCH formats 2/2a/2b

![](media_svg/image116.svg) [公式≈: _{n}_{PUCCH}(3,^{~}p)] Resource index for PUCCH format 3

![](media_svg/image117.svg) [公式≈: ^{n}PDCCH] Number of PDCCHs present in a subframe

![](media_svg/image118.svg) [公式≈: ^{n}PRB] Physical resource block number

![](media_svg/image119.svg) [公式≈: ^{n}PRB^{RA}] First physical resource block occupied by PRACH resource considered

![](media_svg/image120.svg) [公式≈: ^{n}PRB^{RA}offset] First physical resource block available for PRACH

$ n_{PRB,RSS}$ Lowest PRB number of RSS

![](media_svg/image121.svg) [公式≈: _{n}_{sc}RA] Subcarrier occupied by NPRACH resource considered

![](media_svg/image122.svg) [公式≈: ^{n}VRB] Virtual resource block number

![](media_svg/image123.svg) [公式≈: ^{n}RNTI] Radio network temporary identifier

![](media_svg/image124.svg) [公式≈: _{n}_{ID}SA] Sidelink group destination identity

![](media_svg/image125.svg) [公式≈: ^{n}f] System frame number

![](media_svg/image126.svg) [公式≈: ^{n}s] Slot number within a radio frame

![](media_svg/image127.svg) [公式≈: _{n}_{sf}abs] Absolute subframe number

![](media_svg/image128.svg) [公式≈: _{n}_{sf}RA] Index for subframes allowed for preamble transmission

$ O_{RSS}$ Starting frame offset of RSS in each RSS period

![](media_svg/image129.svg) [公式: P] Number of antenna ports used for transmission of a channel

![](media_svg/image5.svg) [公式: p] Antenna port number

$ P_{RSS}$ Period of RSS measured in frames

![](media_svg/image28.svg) [公式: q] Codeword number

![](media_svg/image130.svg) [公式≈: ^{r}RA] Index for PRACH versions with same preamble format and PRACH density

Qm Modulation order: 1 for π/2-BPSK, 2 for QPSK, 4 for 16QAM, 6 for 64QAM and 8 for 256QAM transmissions

![](media_svg/image131.svg) [公式≈: s_{l}^{(}^{p}^{)}(t)] Time-continuous baseband signal for antenna port ![](media_svg/image5.svg) [公式: p] and SC-FDMA/OFDM symbol ![](media_svg/image3.svg) [公式: l] in a slot

![](media_svg/image132.svg) [公式≈: _{t}_{RA}(0)] Radio frame indicator index of PRACH opportunity

![](media_svg/image133.svg) [公式≈: _{t}_{RA}(1)] Half frame index of PRACH opportunity within the radio frame

![](media_svg/image134.svg) [公式≈: _{t}_{RA}(2)] Uplink subframe number for start of PRACH opportunity within the half frame

![](media_svg/image135.svg) [公式≈: ^{T}f] Radio frame duration

![](media_svg/image111.svg) [公式≈: ^{T}s] Basic time unit

![](media_svg/image136.svg) [公式≈: ^{T}slot] Slot duration

![](media_svg/image137.svg) [公式: W] Precoding matrix for downlink spatial multiplexing

![](media_svg/image138.svg) [公式≈: ^{Β}PRACH] Amplitude scaling for PRACH

![](media_svg/image139.svg) [公式≈: ^{Β}NPRACH] Amplitude scaling for NPRACH

![](media_svg/image140.svg) [公式≈: ^{Β}PUCCH] Amplitude scaling for PUCCH

![](media_svg/image141.svg) [公式≈: ^{Β}PUSCH] Amplitude scaling for PUSCH

![](media_svg/image142.svg) [公式≈: ^{Β}NPUSCH] Amplitude scaling for NPUSCH

![](media_svg/image143.svg) [公式≈: ^{Β}SPUCCH] Amplitude scaling for SPUCCH

![](media_svg/image144.svg) [公式≈: ^{Β}SRS] Amplitude scaling for sounding reference symbols

![](media_svg/image145.svg) [公式: δf] Subcarrier spacing

![](media_svg/image146.svg) [公式≈: ^{δ}^{f}RA] Subcarrier spacing for the random access preamble

![](media_svg/image147.svg) [公式: Υ] Number of transmission layers

## 3.2 Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. 
An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

CCE Control Channel Element

CDD Cyclic Delay Diversity

CRS Cell-specific Reference Signal

CSI Channel-State Information

DCI Downlink Control Information

DM-RS Demodulation Reference Signal

ECCE Enhanced Control Channel Element

EPDCCH Enhanced Physical Downlink Control CHannel

EREG Enhanced Resource-Element Group

MPDCCH MTC Physical Downlink Control Channel

MWUS MTC Wake-Up Signal

NCCE Narrowband Control Channel Element

NPBCH Narrowband Physical Broadcast CHannel

NPDCCH Narrowband Physical Downlink Control CHannel

NPDSCH Narrowband Physical Downlink Shared CHannel

NPRACH Narrowband Physical Random Access CHannel

NPUSCH Narrowband Physical Uplink Shared CHannel

NPRS Narrowband Positioning Reference Signal

NPSS Narrowband Primary Synchronization Signal

NSSS Narrowband Secondary Synchronization Signal

NRS Narrowband Reference Signal PBCH Physical Broadcast CHannel

NTN Non-Terrestrial Networks

PCFICH Physical Control Format Indicator CHannel

PDCCH Physical Downlink Control CHannel

PDSCH Physical Downlink Shared CHannel

PHICH Physical Hybrid-ARQ Indicator CHannel

PMCH Physical Multicast CHannel

PRACH Physical Random Access CHannel

PRB Physical Resource Block

PRG Precoding Resource Block Group

PRS Positioning Reference Signal

PSBCH Physical Sidelink Broadcast CHannel

PSCCH Physical Sidelink Control CHannel

PSDCH Physical Sidelink Discovery CHannel

PSSCH Physical Sidelink Shared CHannel

PUCCH Physical Uplink Control CHannel

PUSCH Physical Uplink Shared CHannel

REG Resource-Element Group

RSS Resynchronization Signal

SCCE Short Control Channel Element

SCG Secondary Cell Group

SPDCCH Short Physical Downlink Control CHannel

SPUCCH Short Physical Uplink Control CHannel

SREG Short Resource-Element Group

SRS Sounding Reference Signal

VRB Virtual Resource Block

# 4 Frame structure

Throughout this specification, unless otherwise noted, the size of various fields in the time domain is expressed as a number of time units ![](media_svg/image148.svg) [公式: T_{s}=1(15000≠2048)] seconds.

Downlink, uplink and sidelink transmissions are organized into radio frames with ![](media_svg/image149.svg) [公式: T_{f}=307200≠T_{s}=10ms] duration. 
Three radio frame structures are supported:

- Type 1, applicable to FDD and IoT NTN TDD only,

- Type 2, applicable to TDD only,

- Type 3, applicable to LAA secondary cell operation only.

NOTE: LAA secondary cell operation only applies to frame structure type 3.

Transmissions in multiple cells can be aggregated where up to 31 secondary cells can be used in addition to the primary cell. Unless otherwise noted, the description in this specification applies to each of the up to 32 serving cells. In case of multi-cell aggregation, different frame structures can be used in the different serving cells.

## 4.1 Frame structure type 1 for FDD

Frame structure type 1 is applicable to both full duplex and half duplex FDD only. Each radio frame is ![](media_svg/image150.svg) [公式: T_{f}=307200∪T_{s}=10ms] long and consists of 10 subframes of length ![](media_svg/image151.svg) [公式: 30720∪T_{s}=1ms], numbered from 0 to 9. Subframe ![](media_svg/image152.svg) [公式: i] in frame ![](media_svg/image153.svg) [公式≈: ^{n}f] has an absolute subframe number ![](media_svg/image154.svg) [公式: n_{sf}^{abs}=10n_{f}+i] where ![](media_svg/image155.svg) [公式≈: ^{n}f] is the system frame number.

For subframes using $\Delta  f=2.5 kHz $, ![](media_svg/image156.svg) [公式: δf=7.5kHz], or ![](media_svg/image157.svg) [公式: δf=15kHz], subframe ![](media_svg/image152.svg) [公式: i] is defined as two slots, ![](media_svg/image158.svg) [公式: 2i] and ![](media_svg/image159.svg) [公式: 2i+1], of length ![](media_svg/image160.svg) [公式≈: T_{slot}=15360∪T_{s}=0.5ms] each.

For subframes using ![](media_svg/image161.svg) [公式: δf=1.25kHz], subframe ![](media_svg/image152.svg) [公式: i] is defined as one slot, ![](media_svg/image158.svg) [公式: 2i], of length ![](media_svg/image162.svg) [公式≈: T_{slot}=30720∪T_{s}=1ms].

For transmissions using $\Delta  f=\frac {1}{\left ( 82944T_{s}\right ) }\approx  0.37kHz $, a slot has a length of 92160 $ T_{s}=3ms $. There are 13 slots, numbered in increasing order from 0 to 12, in a 40 ms period starting at $ n_{f}mod4=0 $ with slot 0 starting at $ 30720T_{s}$ in the 40 ms period.

For subframes using ![](media_svg/image163.svg) [公式: δf=15kHz], the subframe can further be divided into six subslots according to Table 4.1-1. Downlink subslot pattern 1 is applied if the number of symbols used for PDCCH is equal to 1 or 3 and downlink subslot pattern 2 is applied if the number of symbols used for PDCCH is equal to 2. For system bandwidths , subslot transmission is not supported in case 4 symbols used for PDCCH.

For FDD, 10 subframes, 20 slots, or up to 60 subslots are available for downlink transmission and 10 subframes, 20 slots, or up to 60 subslots are available for uplink transmissions in each 10 ms interval. Uplink and downlink transmissions are separated in the frequency domain. In half-duplex FDD operation, the UE cannot transmit and receive at the same time while there are no such restrictions in full-duplex FDD.

![](media/image165.emf)

Figure 4.1-1: Frame structure type 1 (assuming $\Delta  f\varepsilon  \left \{ 2.5, 7.5, 15\right \} kHz $).

Table 4.1-1: SC-FDMA/OFDM symbols in different subslots of subframe i

| Subslot number | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Slot number | 2i |  |  | 2i+1 |  |  |
| Uplink subslot pattern | 0, 1, 2 | 3, 4 | 5, 6 | 0, 1 | 2, 3 | 4, 5, 6 |
| Downlink subslot pattern 1 | 0, 1, 2 | 3, 4 | 5, 6 | 0, 1 | 2, 3 | 4, 5, 6 |
| Downlink subslot pattern 2 | 0, 1 | 2, 3, 4 | 5, 6 | 0, 1 | 2, 3 | 4, 5, 6 |

## 4.2 Frame structure type 2

Frame structure type 2 is applicable to TDD only. Each radio frame of length ![](media_svg/image150.svg) [公式: T_{f}=307200∪T_{s}=10ms] consists of two half-frames of length ![](media_svg/image166.svg) [公式: 153600∪T_{s}=5ms]each. Each half-frame consists of five subframes of length![](media_svg/image151.svg) [公式: 30720∪T_{s}=1ms]. Each subframe ![](media_svg/image152.svg) [公式: i]is defined as two slots, ![](media_svg/image158.svg) [公式: 2i]and![](media_svg/image159.svg) [公式: 2i+1], of length ![](media_svg/image160.svg) [公式≈: T_{slot}=15360∪T_{s}=0.5ms] each. Subframe ![](media_svg/image152.svg) [公式: i] in frame ![](media_svg/image153.svg) [公式≈: ^{n}f] has an absolute subframe number ![](media_svg/image154.svg) [公式: n_{sf}^{abs}=10n_{f}+i] where ![](media_svg/image155.svg) [公式≈: ^{n}f] is the system frame number.

The uplink-downlink configuration in a cell may vary between frames and controls in which subframes uplink or downlink transmissions may take place in the current frame. The uplink-downlink configuration in the current frame is obtained according to Clause 13 in [4].

The supported uplink-downlink configurations are listed in Table 4.2-2 where, for each subframe in a radio frame, "D" denotes a downlink subframe reserved for downlink transmissions, "U" denotes an uplink subframe reserved for uplink transmissions and "S" denotes a special subframe with the three fields DwPTS, GP and UpPTS. The length of DwPTS and UpPTS is given by Table 4.2-1 subject to the total length of DwPTS, GP and UpPTS being equal to![](media_svg/image151.svg) [公式: 30720∪T_{s}=1ms] where X is the number of additional SC-FDMA symbols in UpPTS provided by the higher layer parameter srs-UpPtsAdd if configured otherwise X is equal to 0. The UE is not expected to be configured with 2 additional UpPTS SC-FDMA symbols for special subframe configurations {3, 4, 7, 8} for normal cyclic prefix in downlink and special subframe configurations {2, 3, 5, 6} for extended cyclic prefix in downlink and 4 additional UpPTS SC-FDMA symbols for special subframe configurations {1, 2, 3, 4, 6, 7, 8} for normal cyclic prefix in downlink and special subframe configurations {1, 2, 3, 5, 6} for extended cyclic prefix in downlink.

Uplink-downlink configurations with both 5 ms and 10 ms downlink-to-uplink switch-point periodicity are supported.

- In case of 5 ms downlink-to-uplink switch-point periodicity, the special subframe exists in both half-frames.

- In case of 10 ms downlink-to-uplink switch-point periodicity, the special subframe exists in the first half-frame only.

Subframes 0 and 5 and DwPTS are always reserved for downlink transmission. For special subframe configurations 1, 2, 3, 4, 6, 7 and 8, DwPTS is split into two parts, of which the first part is a slot and the second part is of X-symbol duration within the second slot. Downlink subframes, downlink slots in the downlink subframe and DwPTS, and the X–symbol duration in the second slot of DwPTS are available for downlink transmission. The X-symbol transmission opportunity is only available for special subframe configuration 3,4 and 8.

UpPTS and the subframe immediately following the special subframe are always reserved for uplink transmission. Uplink subframes, uplink slots and UpPTS with special subframe configuration 10 are available for uplink transmission. Note that UpPTS with special subframe configuration 10 are not available for SPUCCH transmission.

In case multiple cells are aggregated, the UE may assume that the guard period of the special subframe in the cells using frame structure type 2 have an overlap of at least ![](media_svg/image167.svg) [公式: 1456∪T_{s}].

In case multiple cells with different uplink-downlink configurations in the current radio frame are aggregated and the UE is not capable of simultaneous reception and transmission in the aggregated cells, the following constraints apply:

- if the subframe in the primary cell is a downlink subframe, the UE shall not transmit any signal or channel on a secondary cell in the same subframe

- if the subframe in the primary cell is an uplink subframe, the UE is not expected to receive any downlink transmissions on a secondary cell in the same subframe

- if the subframe in the primary cell is a special subframe and the same subframe in a secondary cell is a downlink subframe, the UE is not expected to receive PDSCH/EPDCCH/PMCH/PRS transmissions in the secondary cell in the same subframe, and the UE is not expected to receive any other signals on the secondary cell in OFDM symbols that overlaps with the guard period or UpPTS in the primary cell.

For frame structure type 2, the higher-layer parameters for symbol-level resource reservation for BL/CE UEs (symbolBitmap1 and symbolBitmap2) do not apply to special subframes.

![](media/image168.emf)

Figure 4.2-1: Frame structure type 2 (for 5 ms switch-point periodicity)

Table 4.2-1: Configuration of special subframe (lengths of DwPTS/GP/UpPTS)

| Special subframe configuration | Normal cyclic prefix in downlink |  |  | Extended cyclic prefix in downlink |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | DwPTS | UpPTS |  | DwPTS | UpPTS |  |
|  |  | Normal cyclic prefix  in uplink | Extended cyclic prefix  in uplink |  | Normal cyclic prefix in uplink | Extended cyclic prefix in uplink |
| 0 | ![](media_svg/image169.svg) [公式: 6592∪T_{s}] | ![](media_svg/image170.svg) [公式: (1X2192+∪∪)T_{s}] | ![](media_svg/image171.svg) [公式: (1X2560+∪∪)T_{s}] | ![](media_svg/image172.svg) [公式: 7680∪T_{s}] | ![](media_svg/image173.svg) [公式: (1X2192+∪∪)T_{s}] | ![](media_svg/image174.svg) [公式: (1X2560+∪∪)T_{s}] |
| 1 | ![](media_svg/image175.svg) [公式: 19760∪T_{s}] |  |  | ![](media_svg/image176.svg) [公式: 20480∪T_{s}] |  |  |
| 2 | ![](media_svg/image177.svg) [公式: 21952∪T_{s}] |  |  | ![](media_svg/image178.svg) [公式: 23040∪T_{s}] |  |  |
| 3 | ![](media_svg/image179.svg) [公式: 24144∪T_{s}] |  |  | ![](media_svg/image180.svg) [公式: 25600∪T_{s}] |  |  |
| 4 | ![](media_svg/image181.svg) [公式: 26336∪T_{s}] |  |  | ![](media_svg/image182.svg) [公式: 7680∪T_{s}] | ![](media_svg/image183.svg) [公式: (2X2192+∪∪)T_{s}] | ![](media_svg/image184.svg) [公式: (2X2560+∪∪)T_{s}] |
| 5 | ![](media_svg/image185.svg) [公式: 6592∪T_{s}] | ![](media_svg/image186.svg) [公式: (2X2192+∪∪)T_{s}] | ![](media_svg/image187.svg) [公式: (2X2560+∪∪)T_{s}] | ![](media_svg/image188.svg) [公式: 20480∪T_{s}] |  |  |
| 6 | ![](media_svg/image189.svg) [公式: 19760∪T_{s}] |  |  | ![](media_svg/image178.svg) [公式: 23040∪T_{s}] |  |  |
| 7 | ![](media_svg/image190.svg) [公式: 21952∪T_{s}] |  |  | ![](media_svg/image191.svg) [公式: 12800∪T_{s}] |  |  |
| 8 | ![](media_svg/image179.svg) [公式: 24144∪T_{s}] |  |  | - | - | - |
| 9 | ![](media_svg/image192.svg) [公式: 13168∪T_{s}] |  |  | - | - | - |
| 10 | ![](media_svg/image192.svg) [公式: 13168∪T_{s}] | ![](media_svg/image193.svg) [公式: 13152∪T_{s}] | ![](media_svg/image194.svg) [公式: 12800∪T_{s}] | - | - | - |

Table 4.2-2: Uplink-downlink configurations

| Uplink-downlink configuration | Downlink-to-Uplink Switch-point periodicity | Subframe number |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 0 | 5 ms | D | S | U | U | U | D | S | U | U | U |
| 1 | 5 ms | D | S | U | U | D | D | S | U | U | D |
| 2 | 5 ms | D | S | U | D | D | D | S | U | D | D |
| 3 | 10 ms | D | S | U | U | U | D | D | D | D | D |
| 4 | 10 ms | D | S | U | U | D | D | D | D | D | D |
| 5 | 10 ms | D | S | U | D | D | D | D | D | D | D |
| 6 | 5 ms | D | S | U | U | U | D | S | U | U | D |

## 4.3 Frame structure type 3

Frame structure type 3 is applicable to LAA secondary cell operation with normal cyclic prefix only. Each radio frame is ![](media_svg/image150.svg) [公式: T_{f}=307200∪T_{s}=10ms] long and consists of 20 slots of length![](media_svg/image195.svg) [公式≈: T_{slot}=15360∪T_{s}=0.5ms], numbered from 0 to 19. A subframe is defined as two consecutive slots where subframe ![](media_svg/image152.svg) [公式: i] consists of slots ![](media_svg/image158.svg) [公式: 2i]and![](media_svg/image159.svg) [公式: 2i+1].

The 10 subframes within a radio frame are available for downlink or uplink transmissions. Downlink transmissions occupy one or more consecutive subframes, starting anywhere within a subframe and ending with the last subframe either fully occupied or following one of the DwPTS durations in Table 4.2-1. Uplink transmisisons occupy one or more consecutive subframes.

## 4.4 Frame structure type 1 for IoT NTN TDD

Frame structure type 1 is applicable to IoT NTN TDD in band 249. Each radio frame is $ T_{f}=307200T_{s}=10ms $ long and consists of 10 subframes of length $ 30720T_{s}=1ms $, numbered from 0 to 9. Subframe $ i $ in frame $ n_{f}$ has an absolute subframe number $ n_{sf}^{abs}=10n_{f}+i $ where $ n_{f}$ is the system frame number.

The frame structure for IoT NTN TDD, at the uplink time synchronization reference point defined in clause 16.1.2 of TS 36.213 [4] consists of $ D=8 $ consecutive downlink subframes, followed by 50 consecutive guard period subframes, followed by $ U=8 $ consecutive uplink subframes, followed by 24 consecutive guard period subframes in each 90 ms interval.

- The UE shall not assume any signal or channel being transmitted in subframes other than downlink subframes 3, 4, 5, 6, 7, 8, 9, and 0 across two consecutive radio frames.

- The UE shall not transmit any signal or channel on a subframe other than the 8 consecutive uplink subframes.

# 5 Uplink

## 5.1 Overview

The smallest resource unit for uplink transmissions is denoted a resource element and is defined in clause 5.2.2.

### 5.1.1 Physical channels

An uplink physical channel corresponds to a set of resource elements carrying information originating from higher layers and is the interface defined between TS36.212 [3] and the present document TS36.211. 
The following uplink physical channels are defined:

- Physical Uplink Shared Channel, PUSCH

- Physical Uplink Control Channel, PUCCH

- Short Physical Uplink Control Channel, SPUCCH

- Physical Random Access Channel, PRACH

### 5.1.2 Physical signals

An uplink physical signal is used by the physical layer but does not carry information originating from higher layers. The following uplink physical signals are defined:

- Reference signal

## 5.2 Slot structure and physical resources

### 5.2.1 Resource grid

The transmitted signal in each slot is described by one or several resource grids of ![](media_svg/image196.svg) [公式≈: _{N}_{RB}UL_{N}_{sc}RB] subcarriers and ![](media_svg/image100.svg) [公式≈: ^{N}symb^{UL}] SC-FDMA symbols. The resource grid is illustrated in Figure 5.2.1-1. The quantity ![](media_svg/image53.svg) [公式≈: _{N}_{RB}UL] depends on the uplink transmission bandwidth configured in the cell and shall fulfil

![](media_svg/image197.svg) [公式≈: _{N}_{RB}min,UL_{≥}_{N}_{RB}UL_{≥}_{N}_{RB}max,UL]

where ![](media_svg/image198.svg) [公式≈: _{N}_{RB}min,UL_{=}_{6}] and ![](media_svg/image199.svg) [公式≈: _{N}_{RB}max,UL_{=}_{110}] are the smallest and largest uplink bandwidths, respectively, supported by the current version of this specification. The set of allowed values for ![](media_svg/image53.svg) [公式≈: _{N}_{RB}UL] is given by TS36.101 [7].

The number of SC-FDMA symbols in a slot depends on the cyclic prefix length configured by the higher layer parameter UL-CyclicPrefixLength and is given in Table 5.2.3-1.

An antenna port is defined such that the channel over which a symbol on the antenna port is conveyed can be inferred from the channel over which another symbol on the same antenna port is conveyed. There is one resource grid per antenna port. The antenna ports used for transmission of a physical channel or signal depends on the number of antenna ports configured for the physical channel or signal as shown in Table 5.2.1-1. The index ![](media_svg/image200.svg) [公式≈: ^{~}p] is used throughout clause 5 when a sequential numbering of the antenna ports is necessary.

![](media/image201.emf)

Figure 5.2.1-1: Uplink resource grid

Table 5.2.1-1: Antenna ports used for different physical channels and signals

| Physical channel or signal | Index ![](media_svg/image202.svg) [公式≈: ^{~}p] | Antenna port number ![](media_svg/image203.svg) [公式: p] as a function of the number of antenna ports configured  for the respective physical channel/signal |  |  |
| --- | --- | --- | --- | --- |
|  |  | 1 | 2 | 4 |
| PUSCH | 0 | 10 | 20 | 40 |
|  | 1 | - | 21 | 41 |
|  | 2 | - | - | 42 |
|  | 3 | - | - | 43 |
| SRS | 0 | 10 | 20 | 40 |
|  | 1 | - | 21 | 41 |
|  | 2 | - | - | 42 |
|  | 3 | - | - | 43 |
| PUCCH, SPUCCH | 0 | 100 | 200 | - |
|  | 1 | - | 201 | - |

### 5.2.2 Resource elements

Each element in the resource grid is called a resource element and is uniquely defined by the index pair ![](media_svg/image204.svg) [公式: (k,l)] in a slot where ![](media_svg/image205.svg) [公式≈: k=0,...,N_{RB}^{UL}N_{sc}^{RB}−1] and ![](media_svg/image206.svg) [公式≈: l=0,...,N_{symb}^{UL}−1] are the indices in the frequency and time domains, respectively. Resource element ![](media_svg/image204.svg) [公式: (k,l)] on antenna port ![](media_svg/image5.svg) [公式: p] corresponds to the complex value ![](media_svg/image4.svg) [公式≈: _{a}_{k}(_{,}p_{l})]. 
When there is no risk for confusion, or no particular antenna port is specified, the index ![](media_svg/image5.svg) [公式: p] may be dropped. 
Quantities ![](media_svg/image4.svg) [公式≈: _{a}_{k}(_{,}p_{l})] corresponding to resource elements not used for transmission of a physical channel or a physical signal in a slot shall be set to zero.

### 5.2.3 Resource blocks

A physical resource block is defined as ![](media_svg/image100.svg) [公式≈: ^{N}symb^{UL}]consecutive SC-FDMA symbols in the time domain and ![](media_svg/image207.svg) [公式≈: _{N}_{sc}RB]consecutive subcarriers in the frequency domain, where ![](media_svg/image100.svg) [公式≈: ^{N}symb^{UL}] and ![](media_svg/image207.svg) [公式≈: _{N}_{sc}RB] are given by Table 5.2.3-1. 
A physical resource block in the uplink thus consists of ![](media_svg/image208.svg) [公式≈: ^{N}symb^{UL}^{≠}^{N}sc^{RB}] resource elements, corresponding to one slot in the time domain and 180 kHz in the frequency domain.

Table 5.2.3-1: Resource block parameters

| Configuration | ![](media_svg/image43.svg) [公式≈: _{N}_{sc}RB] | ![](media_svg/image100.svg) [公式≈: ^{N}symb^{UL}] |
| --- | --- | --- |
| Normal cyclic prefix | 12 | 7 |
| Extended cyclic prefix | 12 | 6 |

The relation between the physical resource block number ![](media_svg/image118.svg) [公式≈: ^{n}PRB] in the frequency domain and resource elements ![](media_svg/image1.svg) [公式: (k,l)] in a slot is given by

![](media_svg/image209.svg) [公式≈: ^{n}^{PRB}^{=}^{⋅}^{⋅}⋅√N^{k}sc^{RB}^{∂}^{∂}∂∃]

5.2.3A Resource unit

Resource units are used to describe the mapping of PUSCH using sub-PRB allocations to resource elements for BL/CE UEs. A resource unit is defined as  SC-FDMA symbols in the time domain and consecutive subcarriers in the frequency domain, where  and  are given by Table 5.2.3A-1.

Table 5.2.3A-1: Supported combinations of , , and  for PUSCH using sub-PRB allocations for Frame Structure type 1 and Frame Structure type 2.

| Physical channel |  | Modulation scheme | ![](media_svg/image218.svg) [公式≈: _{M}_{sc}UL] |  |  |  | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PUSCH | 15 kHz | π/2-BPSK | 12 | 3 | 16 | 7 | 2 out of 3 subcarriers used |
|  |  | QPSK |  | 3 | 8 |  |  |
|  |  |  |  | 6 | 4 |  |  |

### 5.2.4 Narrowbands and widebands

A narrowband is defined as six non-overlapping consecutive physical resource blocks in the frequency domain. The total number of uplink narrowbands in the uplink transmission bandwidth configured in the cell is given by

![](media_svg/image219.svg) [公式≈: NNB^{UL}=^{⋅}⋅_{⋅}_{√}^{N}_{6}^{RB}^{UL}^{∂}∂_{∂}_{∃}]

The narrowbands are numbered ![](media_svg/image220.svg) [公式≈: n_{NB}=0,...,N_{NB}^{UL}−1] in order of increasing physical resource-block number where narrowband ![](media_svg/image221.svg) [公式≈: ^{n}NB]is composed of physical resource-block indices

![](media_svg/image222.svg) [公式≈: ^{√}^{⌡}⌠_{⌡}_{∞}^{6}6_{6}^{n}n_{n}^{NB}NB_{NB}^{+}+_{+}^{i}i_{i}^{0}0_{0}^{+}+_{+}^{i}i_{i}_{+}_{1}^{if}if_{if}^{N}N_{N}^{RB}RB_{RB}^{UL}^{UL}_{UL}^{mod}mod_{mod}^{2}2_{2}^{=}=_{=}1_{1}^{0}and_{and}n_{n}NB_{NB}<_{÷}N_{N}NB_{NB}^{UL}_{UL}2_{2}]

where

![](media_svg/image223.svg) [公式≈: _{i}_{0}i=_{=}0_{⋅}_{⋅}_{⋅}_{√},_{N}1,...,_{2}_{RB}_{UL}5_{∂}_{∂}_{∂}_{∃}_{−}_{6}_{N}_{2}_{NB}_{UL}]

If ![](media_svg/image224.svg) [公式: N_{NB}^{UL}÷4], a wideband is defined as four non-overlapping narrowbands in the frequency domain. The total number of uplink widebands in the uplink transmission bandwidth configured in the cell is given by

![](media_svg/image225.svg) [公式≈: NWB^{UL}=^{⋅}⋅_{⋅}_{√}^{N}_{4}^{NB}^{UL}^{∂}∂_{∂}_{∃}]

and the widebands are numbered ![](media_svg/image226.svg) [公式≈: n_{WB}=0,...,N_{WB}^{UL}−1] in order of increasing narrowband number where wideband ![](media_svg/image227.svg) [公式≈: ^{n}WB] is composed of narrowband indices ![](media_svg/image228.svg) [公式: 4n_{WB}+i] where ![](media_svg/image229.svg) [公式: i=0,1,...,3].

If ![](media_svg/image230.svg) [公式: N_{NB}^{UL}<4], then ![](media_svg/image231.svg) [公式: N_{WB}^{UL}=1] and the single wideband is composed of the ![](media_svg/image232.svg) [公式≈: _{N}_{NB}UL] non-overlapping narrowband(s).

### 5.2.5 Guard period for narrowband and wideband retuning

For BL/CE UEs, a guard period of at most ![](media_svg/image233.svg) [公式≈: _{N}_{symb}retune] SC-FDMA symbols is created for Tx-to-Tx frequency retuning between two consecutive subframes.

- If the higher layer parameter ce-RetuningSymbols is set, then ![](media_svg/image234.svg) [公式≈: _{N}_{symb}retune] equals ce-RetuningSymbols, otherwise ![](media_svg/image235.svg) [公式≈: _{N}_{symb}retune_{=}_{2}].

- If the higher layer parameter ce-pusch-maxBandwidth-config is set to 5 MHz, then the rules for guard period creation defined in the remainder of this clause do not apply for retuning between narrowbands but for retuning between widebands and for transmissions involving multiple widebands.

- If a UE is configured with higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocConfig and the allocation resources are not fully within one narrowband, the rules for guard period creation defined in the remainder of this clause apply for retuning between tuning narrowbands, where

- In case of CEModeA, the tuning narrowband is defined as the 6 consecutive PRBs starting from $ RB_{start}$ defined in 8.1.1 of [4] with the center frequency set in the middle.

- In case of CEModeB, the tuning narrowband is defined as the 6 consecutive PRBs with the center frequency set in the middle of allocated two PRBs.

- If the UE retunes from a first narrowband carrying PUSCH to a second narrowband carrying PUSCH, or if the UE retunes from a first narrowband carrying PUCCH to a second narrowband carrying PUCCH,

- if ![](media_svg/image236.svg) [公式≈: _{N}_{symb}retune_{=}_{1}], a guard period is created by the UE not transmitting the last SC-FDMA symbol in the first subframe;

- if ![](media_svg/image237.svg) [公式≈: _{N}_{symb}retune_{=}_{2}], a guard period is created by the UE not transmitting the last SC-FDMA symbol in the first subframe and the first SC-FDMA symbol in the second subframe.

- If the UE retunes from a first narrowband carrying PUCCH to a second narrowband carrying PUSCH,

- if the PUCCH uses a shortened PUCCH format and ![](media_svg/image236.svg) [公式≈: _{N}_{symb}retune_{=}_{1}], a guard period is created by the UE not transmitting the last SC-FDMA symbol in the first subframe;

- if the PUCCH uses a shortened PUCCH format and ![](media_svg/image237.svg) [公式≈: _{N}_{symb}retune_{=}_{2}], a guard period is created by the UE not transmitting the last SC-FDMA symbol in the first subframe and the first SC-FDMA symbol in the second subframe;

- if the PUCCH uses a normal PUCCH format, a guard period is created by the UE not transmitting the first ![](media_svg/image233.svg) [公式≈: _{N}_{symb}retune] SC-FDMA symbols in the second subframe.

- If the UE retunes from a first narrowband carrying PUSCH to a second narrowband carrying PUCCH,

- a guard period is created by the UE not transmitting the last ![](media_svg/image233.svg) [公式≈: _{N}_{symb}retune] SC-FDMA symbols in the first subframe.

- For CEModeA, if the PUSCH is associated with C-RNTI or SPS C-RNTI and the higher layer parameter ce-pusch-maxBandwidth-config is set to 5 MHz,

- If the PUSCH resource allocation is within a 5 MHz wideband, the center frequency of the transmission bandwidth is the center frequency of the wideband;

- If the PUSCH resource allocation spans two 5 MHz widebands, the center frequency of transmission bandwidth is in the center of PUSCH resource allocation.

Furthermore, for BL/CE UEs configured with the higher layer parameter srs-UpPtsAdd, a guard period of at most ![](media_svg/image233.svg) [公式≈: _{N}_{symb}retune] SC-FDMA symbols is created for Tx-to-Tx frequency retuning between a first special subframe and a second uplink subframe for frame structure type 2 according to:

- If the UE retunes from a first narrowband carrying SRS in the last UpPTS symbol to a second narrowband carrying PUSCH,

- a guard period is created by the UE not transmitting the first ![](media_svg/image233.svg) [公式≈: _{N}_{symb}retune] SC-FDMA symbols in the second subframe.

- If the UE retunes from a first narrowband carrying SRS in the last but one UpPTS symbol, but not in the last UpPTS symbol, to a second narrowband carrying PUSCH,

- if ![](media_svg/image238.svg) [公式≈: _{N}_{symb}retune_{=}_{1}], a guard period is created by the UE not transmitting the last UpPTS symbol in the first subframe;

- if ![](media_svg/image239.svg) [公式≈: _{N}_{symb}retune_{=}_{2}], a guard period is created by the UE not transmitting the last UpPTS symbol in the first subframe and the first SC-FDMA symbol in the second subframe.

- If the UE retunes from a first narrowband carrying SRS to a second narrowband carrying PUCCH,

- if ![](media_svg/image240.svg) [公式≈: _{N}_{symb}retune_{=}_{1}], a guard period is created by the UE not transmitting the last UpPTS symbol in the first subframe;

- if ![](media_svg/image235.svg) [公式≈: _{N}_{symb}retune_{=}_{2}], a guard period is created by the UE not transmitting the last UpPTS symbol in the first subframe and the first SC-FDMA symbol in the second subframe.

For ![](media_svg/image241.svg) [公式≈: _{N}_{symb}retune_{>}_{0}], and for SRS transmission in a special subframe, a BL/CE UE is not expected to be configured with a first SRS transmission in symbol l and a second SRS transmission in any of symbols ![](media_svg/image242.svg) [公式≈: {l+1,...,l+N_{symb}^{retune}}]if the first SRS transmission and the second SRS transmission use different narrowbands.

## 5.3 Physical uplink shared channel

The baseband signal representing the physical uplink shared channel is defined in terms of the following steps:

- scrambling

- modulation of scrambled bits to generate complex-valued symbols

- mapping of the complex-valued modulation symbols onto one or several transmission layers

- transform precoding to generate complex-valued symbols

- precoding of the complex-valued symbols

- mapping of precoded complex-valued symbols to resource elements

- generation of complex-valued time-domain SC-FDMA signal for each antenna port

![](media/image243.emf)

Figure 5.3-1: Overview of uplink physical channel processing

### 5.3.1 Scrambling

For each codeword ![](media_svg/image244.svg) [公式: q], the block of bits ![](media_svg/image245.svg) [公式≈: b^{(}^{q}^{)}(0),...,b^{(}^{q}^{)}(M_{bit}^{(}^{q}^{)}−1)], where ![](media_svg/image246.svg) [公式≈: _{M}_{bit}(q)] is the number of bits transmitted in codeword ![](media_svg/image28.svg) [公式: q] on the physical uplink shared channel in subframe(s)/slot/subslot, shall be scrambled with a UE-specific scrambling sequence prior to modulation, resulting in a block of scrambled bits ![](media_svg/image247.svg) [公式≈: b^{~}^{(}^{q}^{)}(0),...,b^{~}^{(}^{q}^{)}(M_{bit}^{(q)}−1)] according to the following pseudo code

Set i = 0

while ![](media_svg/image248.svg) [公式≈: _{i}_{<}_{M}_{bit}(q)]

if ![](media_svg/image249.svg) [公式: b^{(}^{q}^{)}(i)=x] // ACK/NACK or Rank Indication placeholder bits

![](media_svg/image250.svg) [公式≈: b^{~}^{(}^{q}^{)}(i)=1]

else

if ![](media_svg/image251.svg) [公式: b^{(}^{q}^{)}(i)=y] // ACK/NACK or Rank Indication repetition placeholder bits

![](media_svg/image252.svg) [公式≈: b^{~}^{(}^{q}^{)}(i)=b^{~}^{(}^{q}^{)}(i−1)]

else // Data or channel quality coded bits, Rank Indication coded bits or ACK/NACK coded bits

![](media_svg/image253.svg) [公式≈: b^{~}^{(}^{q}^{)}(i)=(b^{(}^{q}^{)}(i)+c^{(}^{q}^{)}(i))mod2]

end if

end if

i = i + 1

end while

where x and y are tags defined in TS36.212 [3] clause 5.2.2.6 and where the scrambling sequence ![](media_svg/image254.svg) [公式: c^{(}^{q}^{)}(i)] is given by clause 7.2. The scrambling sequence generator shall be initialised with ![](media_svg/image255.svg) [公式≈: c_{init}=n_{RNTI}∪2^{14}+q∪2^{13}+_{√}n_{s}2_{∃}∪2^{9}+N_{ID}^{cell}] at the start of each subframe where ![](media_svg/image256.svg) [公式≈: ^{n}RNTI] corresponds to the RNTI associated with the PUSCH transmission as described in clause 8 in TS36.213[4]. For AUL PUSCH, $ n_{RNTI}=0.$

For BL/CE UEs,

- if the PUSCH transmission is using sub-PRB allocations, the scrambling sequence generator shall be initialised with

$$ c_{init}=n_{RNTI}\cdot  2^{14}+q\cdot  2^{13}+\left [ \lfloor  \frac {i}{M_{RU}\cdot  M_{slots}^{UL}/ 2}\rfloor  mod 10\right ] \cdot  2^{9}+N_{ID}^{cell}$$

at the first valid uplink subframe of every $ M_{RU}\cdot  M_{slots}^{UL}/ 2 $ subframes comprising the allocated UL resource unit(s), where $ i=0, 1, \ldots  ,N-1 $, and N is the number of BL/CE UL subframes for the PUSCH transmission as determined in clause 8.0 in [4].

- otherwise, the same scrambling sequence is applied per subframe to PUSCH for a given block of ![](media_svg/image66.svg) [公式≈: ^{N}acc] subframes. The subframe number of the first subframe in each block of ![](media_svg/image257.svg) [公式≈: ^{N}acc] consecutive subframes, denoted as ![](media_svg/image258.svg) [公式≈: ^{n}abs,1], satisfies ![](media_svg/image259.svg) [公式≈: ^{n}abs,1^{mod}^{N}acc^{=}^{0}]. For the ![](media_svg/image260.svg) [公式≈: _{j}th]block of ![](media_svg/image66.svg) [公式≈: ^{N}acc] subframes, the scrambling sequence generator shall be initialised with

![](media_svg/image261.svg) [公式≈: c_{init}=n_{RNTI}∪2^{14}+q∪2^{13}+{(j_{0}+j)N_{acc}mod10}∪2^{9}+N_{ID}^{cell}]

where

![](media_svg/image262.svg) [公式≈: _{j}_{0}j=_{=}0_{√}_{i},_{0}1,...,_{N}_{acc}^{⋅}⋅_{⋅}_{√}^{i}^{0}_{∃}^{+}^{N}_{N}^{abs}^{PUSCH}_{acc}^{−}^{1}^{∂}∂_{∂}_{∃}−j0]

and ![](media_svg/image263.svg) [公式≈: ^{i}0] is the absolute subframe number of the first uplink subframe intended for PUSCH. The PUSCH transmission spans ![](media_svg/image67.svg) [公式≈: _{N}_{abs}PUSCH] consecutive subframes including subframes that are not BL/CE UL subframes where the UE postpones the PUSCH transmission. For a BL/CE UE configured in CEModeA, ![](media_svg/image264.svg) [公式: N_{acc}=1]. For a BL/CE UE configured with CEModeB, ![](media_svg/image265.svg) [公式: N_{acc}=4] for frame structure type 1 and ![](media_svg/image266.svg) [公式: N_{acc}=5] for frame structure type 2.

For PUSCH with a subframe duration, up to two codewords can be transmitted in one subframe, i.e., ![](media_svg/image267.svg) [公式: q⎰{0,1}]. In the case of single-codeword transmission, ![](media_svg/image268.svg) [公式: q=0].

### 5.3.2 Modulation

For each codeword![](media_svg/image28.svg) [公式: q], the block of scrambled bits ![](media_svg/image247.svg) [公式≈: b^{~}^{(}^{q}^{)}(0),...,b^{~}^{(}^{q}^{)}(M_{bit}^{(q)}−1)] shall be modulated as described in clause7.1, resulting in a block of complex-valued symbols ![](media_svg/image269.svg) [公式≈: d^{(}^{q}^{)}(0),...,d^{(}^{q}^{)}(M_{symb}^{(}^{q}^{)}−1)]. Table 5.3.2-1 specifies the modulation mappings applicable for the physical uplink shared channel. For sub-PRB allocations only π/2 BPSK and QPSK are supported.



Table 5.3.2-1: Uplink modulation schemes

| Physical channel | Modulation schemes |
| --- | --- |
| PUSCH | π/2 BPSK, QPSK, 16QAM, 64QAM, 256QAM |

### 5.3.2A Layer mapping

The complex-valued modulation symbols for each of the codewords to be transmitted are mapped onto one or two layers. Complex-valued modulation symbols ![](media_svg/image269.svg) [公式≈: d^{(}^{q}^{)}(0),...,d^{(}^{q}^{)}(M_{symb}^{(}^{q}^{)}−1)] for codeword ![](media_svg/image28.svg) [公式: q] shall be mapped onto the layers ![](media_svg/image270.svg) [公式≈: x(i)={x^{(}^{0}^{)}(i)...x^{(}^{Υ}^{−}^{1}^{)}(i)}^{T}], ![](media_svg/image271.svg) [公式≈: i=0,1,...,M_{symb}^{layer}−1] where ![](media_svg/image272.svg) [公式: Υ] is the number of layers and ![](media_svg/image30.svg) [公式≈: _{M}_{symb}layer] is the number of modulation symbols per layer.

#### 5.3.2A.1 Layer mapping for transmission on a single antenna port

For transmission on a single antenna port, a single layer is used, ![](media_svg/image273.svg) [公式: Υ=1], and the mapping is defined by

![](media_svg/image274.svg) [公式≈: x^{(}^{0}^{)}(i)=d^{(}^{0}^{)}(i)]

with ![](media_svg/image275.svg) [公式≈: _{M}_{symb}layer_{=}_{M}_{symb}(0)].

#### 5.3.2A.2 Layer mapping for spatial multiplexing

For spatial multiplexing, the layer mapping shall be done according to Table 5.3.2A.2-1. The number of layers ![](media_svg/image272.svg) [公式: Υ] is less than or equal to the number of antenna ports ![](media_svg/image129.svg) [公式: P] used for transmission of the physical uplink shared channel. 
The case of a single codeword mapped to multiple layers is only applicable when the number of antenna ports used for PUSCH is four, except for slot-PUSCH and subslot-PUSCH transmission where a single codeword is used irrespective of the number of layers.

Table 5.3.2A.2-1: Codeword-to-layer mapping for spatial multiplexing

| Number of layers | Number of codewords | Codeword-to-layer mapping![](media_svg/image276.svg) [公式≈: i=0,1,...,M_{symb}^{layer}−1] |  |
| --- | --- | --- | --- |
| 1 | 1 | ![](media_svg/image277.svg) [公式≈: x^{(}^{0}^{)}(i)=d^{(}^{0}^{)}(i)] | ![](media_svg/image278.svg) [公式≈: _{M}_{symb}layer_{=}_{M}_{symb}(0)] |
| 2 | 1 | ![](media_svg/image279.svg) [公式≈: ^{x}x^{(}^{(}^{0}^{1}^{)}^{)}^{(}(^{i}i^{)})^{=}=^{d}d^{(}^{(}^{0}^{0}^{)}^{)}^{(}(^{2}2^{i}i^{)}+1)] | ![](media_svg/image280.svg) [公式≈: _{M}_{symb}layer_{=}_{M}_{symb}(0)_{2}] |
| 2 | 2 | ![](media_svg/image281.svg) [公式≈: x^{(}^{0}^{)}(i)=d^{(}^{0}^{)}(i)] | ![](media_svg/image282.svg) [公式≈: ^{M}symb^{layer}^{=}^{M}symb^{(}^{0}^{)}^{=}^{M}symb^{(}^{1}^{)}] |
|  |  | ![](media_svg/image283.svg) [公式≈: x^{(}^{1}^{)}(i)=d^{(}^{1}^{)}(i)] |  |
| 3 | 2 | ![](media_svg/image284.svg) [公式≈: x^{(}^{0}^{)}(i)=d^{(}^{0}^{)}(i)]![](media_svg/image285.svg) [公式≈: x^{x}^{(}^{(}^{2}^{1}^{)}^{)}^{(}(^{i}i^{)})^{=}=^{d}d^{(}^{(}^{1}^{1}^{)}^{)}^{(}(^{2}2^{i}i^{)}+1)] | ![](media_svg/image286.svg) [公式≈: ^{M}symb^{layer}^{=}^{M}symb^{(}^{0}^{)}^{=}^{M}symb^{(}^{1}^{)}^{2}] |
| 4 | 2 | ![](media_svg/image279.svg) [公式≈: ^{x}x^{(}^{(}^{0}^{1}^{)}^{)}^{(}(^{i}i^{)})^{=}=^{d}d^{(}^{(}^{0}^{0}^{)}^{)}^{(}(^{2}2^{i}i^{)}+1)] | ![](media_svg/image287.svg) [公式≈: ^{M}symb^{layer}^{=}^{M}symb^{(}^{0}^{)}^{2}^{=}^{M}symb^{(}^{1}^{)}^{2}] |
|  |  | ![](media_svg/image288.svg) [公式≈: ^{x}x^{(}^{(}^{2}^{3}^{)}^{)}^{(}(^{i}i^{)})^{=}=^{d}d^{(}^{(}^{1}^{1}^{)}^{)}^{(}(^{2}2^{i}i^{)}+1)] |  |
| 41 | 11 | ![](media_svg/image289.svg) [公式≈: ^{x}^{x}x^{x}^{(}^{(}^{(}^{(}^{0}^{2}^{3}^{1}^{)}^{)}^{)}^{)}^{(}^{(}^{(}(^{i}^{i}^{i}i^{)}^{)}^{)})^{=}^{=}^{=}=^{d}^{d}^{d}d^{(}^{(}^{(}^{(}^{0}^{0}^{0}^{0}^{)}^{)}^{)}^{)}^{(}^{(}^{(}(^{4}^{4}^{4}4^{i}^{i}^{i}i^{)}^{+}^{+}+^{1}3^{2}^{)})^{)}] ![](media_svg/image290.svg) [公式≈: _{M}_{symb}layer_{=}_{M}_{symb}(0)_{4}] |  |
| NOTE 1: Only used for slot-PUSCH and subslot-PUSCH |  |  |  |

### 5.3.3 Transform precoding

For each layer ![](media_svg/image291.svg) [公式: Λ=0,1,...,Υ−1] the block of complex-valued symbols ![](media_svg/image292.svg) [公式≈: x^{(}^{Λ}^{)}(0),...,x^{(}^{Λ}^{)}(M_{symb}^{layer}−1)] is divided into ![](media_svg/image293.svg) [公式≈: _{M}_{symb}layer_{M}_{sc}PUSCH] sets, each corresponding to one SC-FDMA symbol. Transform precoding shall be applied according to

![](media_svg/image294.svg) [公式≈: _{y}(Λ)_{(}_{l}_{∪}_{M}_{sc}PUSCH_{+}_{k}_{k}_{)}_{l}_{=}_{=}_{=}_{0}_{0}_{,...,}_{,...,}_{M}_{sc}_{PUSCH}_{M}_{M}1_{sc}_{symb}_{layer}_{PUSCH}^{M}_{M}^{sc}^{PUSCH}_{−}_{⊆}_{i}_{=}_{sc}_{1}_{PUSCH}_{0}^{−}^{1}_{x}(_{−}Λ)_{1}_{(}_{l}_{∪}_{M}_{sc}PUSCH_{+}_{i}_{)}_{e}^{−}^{j}M^{2}scPUSCH^{Π}^{ik}]

resulting in a block of complex-valued symbols ![](media_svg/image295.svg) [公式≈: y^{(}^{Λ}^{)}(0),...,y^{(}^{Λ}^{)}(M_{symb}^{layer}−1)]. The variable![](media_svg/image296.svg) [公式≈: _{M}_{sc}PUSCH_{=}_{M}_{RB}PUSCH_{∪}_{N}_{sc}RB], where ![](media_svg/image22.svg) [公式≈: _{M}_{RB}PUSCH] represents the bandwidth of the PUSCH in terms of resource blocks, and shall fulfil

![](media_svg/image297.svg) [公式≈: _{M}_{RB}PUSCH_{=}_{2}Α2_{∪}_{3}Α3_{∪}_{5}Α5_{≥}_{N}_{RB}UL]

where ![](media_svg/image298.svg) [公式: Α_{2},Α_{3},Α_{5}] is a set of non-negative integers.

In case of PUSCH transmissions using sub-PRB allocations for BL/CE UEs, the variable .

### 5.3.3A Precoding

The precoder takes as input a block of vectors ![](media_svg/image300.svg) [公式≈: {y^{(}^{0}^{)}(i)...y^{(}^{Υ}^{−}^{1}^{)}(i)}^{T}], ![](media_svg/image276.svg) [公式≈: i=0,1,...,M_{symb}^{layer}−1] from the transform precoder and generates a block of vectors ![](media_svg/image301.svg) [公式≈: {z^{(}^{0}^{)}(i)κz^{(}^{P}^{−}^{1}^{)}(i)}^{T}], ![](media_svg/image302.svg) [公式≈: i=0,1,...,M_{symb}^{ap}−1] to be mapped onto resource elements.

#### 5.3.3A.1 Precoding for transmission on a single antenna port

For transmission on a single antenna port, precoding is defined by

![](media_svg/image303.svg) [公式≈: z^{(}^{0}^{)}(i)=y^{(}^{0}^{)}(i)]

where ![](media_svg/image304.svg) [公式≈: i=0,1,...,M_{symb}^{ap}−1], ![](media_svg/image305.svg) [公式≈: ^{M}symb^{ap}^{=}^{M}symb^{layer}].

#### 5.3.3A.2 Precoding for spatial multiplexing

Precoding for spatial multiplexing is only used in combination with layer mapping for spatial multiplexing as described in clause 5.3.2A.2. Spatial multiplexing supports ![](media_svg/image306.svg) [公式: P=2] or ![](media_svg/image307.svg) [公式: P=4] antenna ports where the set of antenna ports used for spatial multiplexing is ![](media_svg/image308.svg) [公式: p⎰{20,21}] and ![](media_svg/image309.svg) [公式: p⎰{40,41,42,43}], respectively.

Precoding for spatial multiplexing is defined by

![](media_svg/image310.svg) [公式≈: ^{⊥}^{⋅}^{⋅}⋅_{√}_{z}^{z}(P^{(}^{0}−^{μ}^{)}1^{(})^{i}_{(}^{)}_{i}_{)}^{∀}^{∂}^{∂}∂_{∃}^{=}^{W}^{⊥}^{⋅}^{⋅}⋅_{√}_{y}^{y}(Υ^{(}^{0}−^{μ}^{)}1)^{(}^{i}_{(}^{)}_{i}_{)}^{∀}^{∂}^{∂}∂_{∃}]

where ![](media_svg/image311.svg) [公式≈: i=0,1,...,M_{symb}^{ap}−1], ![](media_svg/image312.svg) [公式≈: ^{M}symb^{ap}^{=}^{M}symb^{layer}].

The precoding matrix ![](media_svg/image313.svg) [公式: W] of size ![](media_svg/image314.svg) [公式: P≠Υ] is given by one of the entries in Table 5.3.3A.2-1 for ![](media_svg/image315.svg) [公式: P=2] and by Tables 5.3.3A.2-2 through 5.3.3A.2-5 for ![](media_svg/image316.svg) [公式: P=4] where the entries in each row are ordered from left to right in increasing order of codebook indices.

Table 5.3.3A.2-1: Codebook for transmission on antenna ports ![](media_svg/image317.svg) [公式: {20,21}]

| Codebook index | Number of layers |  |
| --- | --- | --- |
|  | ![](media_svg/image318.svg) [公式: Υ=1] | ![](media_svg/image319.svg) [公式: Υ=2] |
| 0 | ![](media_svg/image320.svg) [公式≈: 1_{2}⊥_{⋅}_{√}1_{1}∀_{∂}_{∃}] | ![](media_svg/image321.svg) [公式≈: 1_{2}⊥_{⋅}_{√}1_{0}_{1}0∀_{∂}_{∃}] |
| 1 | ![](media_svg/image322.svg) [公式≈: 1_{2}⊥_{⋅}_{√}_{−}1_{1}∀_{∂}_{∃}] | - |
| 2 | ![](media_svg/image323.svg) [公式≈: 1_{2}⊥_{⋅}_{√}1_{j}∀_{∂}_{∃}] | - |
| 3 | ![](media_svg/image324.svg) [公式≈: 1_{2}⊥_{⋅}_{√}_{−}1_{j}∀_{∂}_{∃}] | - |
| 4 | ![](media_svg/image325.svg) [公式≈: 1_{2}⊥_{⋅}_{√}1_{0}∀_{∂}_{∃}] | - |
| 5 | ![](media_svg/image326.svg) [公式≈: 1_{2}⊥_{⋅}_{√}_{1}0∀_{∂}_{∃}] | - |

Table 5.3.3A.2-2: Codebook for transmission on antenna ports ![](media_svg/image327.svg) [公式: {40,41,42,43}] with ![](media_svg/image328.svg) [公式: Υ=1]

| Codebook index | Number of layers ![](media_svg/image318.svg) [公式: Υ=1] |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 – 7 | ![](media_svg/image329.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}_{−}^{1}^{1}1_{1}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image330.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}^{1}j_{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image331.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}−^{1}^{1}_{1}1^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image332.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}−_{−}^{1}^{1}j_{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image333.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}1^{j}_{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image334.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}_{1}^{j}j^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image335.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}_{−}−^{1}^{j}1_{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image336.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}−_{−}^{1}^{j}_{1}j^{∀}^{∂}^{∂}∂_{∂}_{∃}] |
| 8 – 15 | ![](media_svg/image337.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{−}^{1}1_{1}^{1}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image338.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}_{−}^{−}^{1}j^{1}_{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image339.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{−}−_{−}^{1}^{1}1_{1}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image340.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}−^{−}^{1}_{j}^{1}j^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image341.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{−}_{−}^{1}1^{j}_{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image342.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{−}_{−}^{1}j_{1}^{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image343.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{−}−^{1}_{j}1^{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image344.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{−}−^{1}_{1}^{j}j^{∀}^{∂}^{∂}∂_{∂}_{∃}] |
| 16 – 23 | ![](media_svg/image345.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}1^{0}_{0}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image346.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}−^{1}^{0}_{0}1^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image347.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}^{0}_{0}j^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image348.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}−^{1}^{0}_{0}j^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image349.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}_{1}^{0}0^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image350.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}_{−}^{1}^{0}0_{1}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image351.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}^{0}0_{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image352.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}_{−}^{1}^{0}0_{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] |

Table 5.3.3A.2-3: Codebook for transmission on antenna ports ![](media_svg/image353.svg) [公式: {40,41,42,43}] with ![](media_svg/image354.svg) [公式: Υ=2]

| Codebook index | Number of layers ![](media_svg/image355.svg) [公式: Υ=2] |  |  |  |
| --- | --- | --- | --- | --- |
| 0 – 3 | ![](media_svg/image356.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}^{1}0_{0}_{−}1^{0}^{0}_{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image357.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}^{1}0_{0}1^{0}^{0}_{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image358.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{−}^{1}0_{0}^{j}1_{1}^{0}^{0}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image359.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{−}^{1}0_{0}^{j}_{−}1^{0}^{0}_{1}^{∀}^{∂}^{∂}∂_{∂}_{∃}] |
| 4 – 7 | ![](media_svg/image360.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{−}^{1}0_{0}^{1}_{−}1^{0}^{0}_{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image361.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{−}^{1}0_{0}^{1}1^{0}^{0}_{j}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image362.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}0_{0}^{j}1_{1}^{0}^{0}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image363.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}0_{0}^{j}_{−}1^{0}^{0}_{1}^{∀}^{∂}^{∂}∂_{∂}_{∃}] |
| 8 – 11 | ![](media_svg/image364.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}1^{0}_{0}^{1}_{1}^{0}0^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image365.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}1^{0}_{0}_{−}^{1}^{0}0_{1}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image366.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}−^{1}^{0}_{0}1^{1}_{1}^{0}0^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image367.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}−^{1}^{0}_{0}1_{−}^{1}^{0}0_{1}^{∀}^{∂}^{∂}∂_{∂}_{∃}] |
| 12 – 15 | ![](media_svg/image368.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}_{1}^{0}0^{1}1^{0}_{0}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image369.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}_{1}^{0}0−^{1}^{0}_{0}1^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image370.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}_{−}^{1}^{0}0_{1}^{1}1^{0}_{0}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image371.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}_{−}^{1}^{0}0_{1}−^{1}^{0}_{0}1^{∀}^{∂}^{∂}∂_{∂}_{∃}] |

Table 5.3.3A.2-4: Codebook for transmission on antenna ports ![](media_svg/image353.svg) [公式: {40,41,42,43}] with ![](media_svg/image372.svg) [公式: Υ=3]

| Codebook index | Number of layers ![](media_svg/image373.svg) [公式: Υ=3] |  |  |  |
| --- | --- | --- | --- | --- |
| 0 – 3 | ![](media_svg/image374.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}^{1}0_{0}1^{0}^{0}_{0}_{1}^{0}^{0}0^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image375.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{−}^{1}0_{0}^{1}1^{0}^{0}_{0}_{1}^{0}^{0}0^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image376.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}1^{0}_{0}^{1}^{0}0_{0}_{1}^{0}^{0}0^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image377.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}−^{1}^{0}_{0}1^{1}^{0}0_{0}_{1}^{0}^{0}0^{∀}^{∂}^{∂}∂_{∂}_{∃}] |
| 4 – 7 | ![](media_svg/image378.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}_{1}^{0}0^{1}^{0}0_{0}1^{0}^{0}_{0}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image379.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}_{−}^{1}^{0}0_{1}^{1}^{0}0_{0}1^{0}^{0}_{0}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image380.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}1^{0}_{0}^{1}^{0}0_{0}_{1}^{0}^{0}0^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image381.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}−^{1}^{0}_{0}1^{1}^{0}0_{0}_{1}^{0}^{0}0^{∀}^{∂}^{∂}∂_{∂}_{∃}] |
| 8 – 11 | ![](media_svg/image382.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}_{1}^{0}0^{1}^{0}0_{0}1^{0}^{0}_{0}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image383.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}_{−}^{1}^{0}0_{1}^{1}^{0}0_{0}1^{0}^{0}_{0}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image384.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}1_{1}^{0}^{0}^{1}^{0}0_{0}^{1}^{0}0_{0}^{∀}^{∂}^{∂}∂_{∂}_{∃}] | ![](media_svg/image385.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}_{−}1^{0}^{0}_{1}^{1}^{0}0_{0}^{1}^{0}0_{0}^{∀}^{∂}^{∂}∂_{∂}_{∃}] |

Table 5.3.3A.2-5: Codebook for transmission on antenna ports ![](media_svg/image353.svg) [公式: {40,41,42,43}] with ![](media_svg/image386.svg) [公式: Υ=4]

| Codebook index | Number of layers ![](media_svg/image387.svg) [公式: Υ=4] |
| --- | --- |
| 0 | ![](media_svg/image388.svg) [公式≈: ^{1}2^{⊥}^{⋅}^{⋅}⋅_{⋅}_{√}^{1}^{0}0_{0}^{1}^{0}0_{0}1^{0}^{0}_{0}_{1}^{0}^{0}0^{∀}^{∂}^{∂}∂_{∂}_{∃}] |

### 5.3.4 Mapping to physical resources

For each antenna port ![](media_svg/image389.svg) [公式: p] used for transmission of the PUSCH in a subframe the block of complex-valued symbols ![](media_svg/image390.svg) [公式≈: z^{(}^{~}^{p}^{)}(0),...,z^{(}^{~}^{p}^{)}(M_{symb}^{ap}−1)] shall be multiplied with the amplitude scaling factor ![](media_svg/image391.svg) [公式≈: ^{Β}PUSCH] in order to conform to the transmit power ![](media_svg/image392.svg) [公式≈: ^{P}PUSCH]specified in clause 5.1.1.1 in TS36.213[4], and mapped in sequence starting with ![](media_svg/image393.svg) [公式≈: z^{(}^{~}^{p}^{)}(0)] to physical resource blocks on antenna port ![](media_svg/image394.svg) [公式: p] and assigned for transmission of PUSCH. The relation between the index ![](media_svg/image395.svg) [公式≈: ^{~}p] and the antenna port number ![](media_svg/image394.svg) [公式: p] is given by Table 5.2.1-1. The mapping to resource elements ![](media_svg/image396.svg) [公式: (k,l)] corresponding to the physical resource blocks assigned for transmission shall fulfil the following criteria:

- not used for transmission of reference signals, and

- not part of the last SC-FDMA symbol in a subframe, if the UE transmits SRS in the same subframe in the same serving cell, and

- not part of the last SC-FDMA symbol in a subframe configured with cell-specific SRS for non-BL/CE UEs and BL/CE UEs in CEModeA, if the PUSCH transmission partly or fully overlaps with the cell-specific SRS bandwidth, and

- not part of an SC-FDMA symbol reserved for possible trigger type 1 SRS transmission as specified in [4] in a UE-specific aperiodic SRS subframe in the same serving cell, and

- not part of an SC-FDMA symbol reserved for possible trigger type 0 SRS transmission as specified in [4] in a UE-specific periodic SRS subframe in the same serving cell when the UE is configured with multiple TAGs

- not part of the first SC-FDMA symbol in a subframe if the associated DCI indicates PUSCH starting position '01', '10', or '11' and does not indicate PUSCH mode 2.

- not part of the first SC-FDMA symbol in the second slot in a subframe if the associated DCI indicates PUSCH starting position '01', '10', or '11' and PUSCH mode 2.

- not part of the last SC-FDMA symbol in a subframe if the associated DCI indicates PUSCH ending symbol '1' and does not indicate PUSCH mode 3.

- not part of the second slot in a subframe if the associated DCI indicates PUSCH ending symbol '0' and PUSCH mode 3.

- not part of SC-FDMA symbols 5 to 13 in a subframe if the associated DCI indicates PUSCH ending symbol '1' and PUSCH mode 3.

The mapping to resource elements ![](media_svg/image396.svg) [公式: (k,l)] shall be in increasing order of first the index ![](media_svg/image397.svg) [公式: k], then the index ![](media_svg/image398.svg) [公式: l]. The mapping starts with the first slot in an uplink subframe, except for slot-PUSCH, subslot-PUSCH transmission, or PUSCH mode 2.

In case of PUSCH transmissions using sub-PRB allocations for BL/CE UEs, the mapping starts over in every valid uplink subframe composing an UL resource unit.

In case of slot-PUSCH, the mapping shall start at ![](media_svg/image399.svg) [公式: l=0] in the slot assigned for transmission.

In case of PUSCH mode 2, the mapping shall start at  in the second slot of the subframe assigned for transmission.

In case of subslot-PUSCH, the mapping shall start at symbol ![](media_svg/image400.svg) [公式: l] where the start of the mapping is dependent on the uplink subslot number in the subframe assigned for transmission and the DMRS-pattern field in the related uplink DCI format [3] according to Table 5.3.4-1 where starting symbol index "4" for subslot #5 is applied if the UE has indicated the capability ul-pattern-ddd-r15.

Table 5.3.4-1: Starting symbol index for subslot-PUSCH transmission

| DMRS-pattern field in uplink-related DCI format [3] | Uplink subslot number |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | #0 | #1 | #2 | #3 | #4 | #5 |
| 00 | 1 | 4 | 6 | 1 | 3 | 5 |
| 01 | 0 | 3 | 5 | 0 | 2 | 4 |
| 10 | – | 3 | – | 0 | 2 | – |
| 11 | – | 3 | – | – | 2 | – |

In case of a semi-persistently scheduled subslot-PUSCH, and semi-persistent scheduling (i.e. higher layer parameter sps-ConfigUL-STTI is configured, see TS 36.331 [9]) with a configured periodicity of 1 subslot (i.e. semiPersistSchedIntervalUL-STTI set to sTTI1), the mapping shall start at symbol ![](media_svg/image400.svg) [公式: l] depending on the DMRS-pattern field in the related uplink DCI format [3] according to Table 5.3.4-2.

In case of a semi-persistently scheduled subslot-PUSCH and semi-persistent scheduling (the higher layer parameter sps-ConfigUL-sTTI-r15 is configured, see TS 36.331 [9]) with repetitions enabled (the higher layer parameter totalNumberPUSCH-SPS-STTI-UL-Repetitions is configured), the mapping shall start at symbol ![](media_svg/image400.svg) [公式: l] depending on the DMRS-pattern field in the related uplink DCI format [3] according to Table 5.3.4-2.

Table 5.3.4-2: Starting symbol index for subslot-PUSCH transmission in case of semi-persistent scheduling with a configured periodicity of 1 subslot

| DMRS-pattern field in uplink-related DCI format [3] | Uplink subslot number |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | #0 | #1 | #2 | #3 | #4 | #5 |
| 00 | 1 | 4 | 6 | 1 | 3 | 5 |
| 10 | 1 | 3 | 6 | 0 | 3 | 5 |

In case of subslot-PUSCH and semi-persistent scheduling with a configured periodicity longer than 1 subslot the mapping shall start at symbol ![](media_svg/image400.svg) [公式: l] according to the first row of Table 5.3.4-2 (i.e. equivalent to a signalling of DMRS-pattern field set to '00').

For the UpPTS, the mapping shall start at symbol ![](media_svg/image401.svg) [公式: l=1] and if dmrsLess-UpPts is set to true the mapping shall end at symbol ![](media_svg/image402.svg) [公式: l=symPUSCH_UpPts] in the second slot of a special subframe, otherwise, the mapping shall end at symbol ![](media_svg/image403.svg) [公式: l=symPUSCH_UpPts+1] in the second slot of a special subframe.

For BL/CE UEs, the PUSCH transmission is restricted as follows:

- For CEModeA, if the PUSCH is associated with C-RNTI or SPS C-RNTI and the higher layer parameter ce-pusch-maxBandwidth-config is set to 5 MHz, the maximum number of allocatable PRBs for PUSCH is 24 PRBs. The allocatable PRBs include the PRBs belonging to the narrowbands defined in clause 5.2.4 and the odd PRB at the center of the uplink system bandwidth in case of odd total number of uplink PRBs. If a resource assignment or frequency hopping would result in a PUSCH resource allocation outside the allocatable PRBs then the PUSCH transmission in that subframe is dropped.

- For all other cases, the maximum number of allocatable PRBs for PUSCH is 6 PRBs restricted to one of the narrowbands defined in clause 5.2.4.

For BL/CE UEs in CEModeB, resource elements in the last SC-FDMA symbol in a subframe configured with cell-specific SRS shall be counted in the PUSCH mapping but not used for transmission of the PUSCH.

For BL/CE UEs, if one or more SC-FDMA symbol(s) are left empty due to guard period for narrowband or wideband retuning, the affected SC-FDMA symbol(s) shall be counted in the PUSCH mapping but not used for transmission of the PUSCH.

For a UE configured with SRS carrier switching, if the first symbol in a subframe overlaps with an SRS transmission (including any interruption due to uplink or downlink RF retuning time) in a carrier without PUSCH/PUCCH, the resource elements in the first SC-FDMA symbol shall be counted in the PUSCH mapping but not used for transmission of PUSCH.

For a UE configured with SRS carrier switching, if the last symbol in a subframe is counted in the PUSCH mapping and the last symbol in the subframe overlaps with an SRS transmission (including any interruption due to uplink or downlink RF retuning time) in a carrier without PUSCH/PUCCH, the resource elements in the last SC-FDMA symbol shall be counted in the PUSCH mapping but not used for transmission of PUSCH.

For a UE configured with SRS carrier switching, if the last symbol in a subframe is not counted in the PUSCH mapping and the second-to-last symbol in the subframe overlaps with an SRS transmission (including any interruption due to uplink or downlink RF retuning time) in a carrier without PUSCH/PUCCH, the resource elements in the second-to-last SC-FDMA symbol shall be counted in the PUSCH mapping but not used for transmission of PUSCH.

For a UE configured with PUSCH Mode 1, if DCI indicates PUSCH mode 1 enabled and the corresponding transmission of PUSCH starts in the second slot of a subframe, the resource elements in the first slot of the subframe shall be counted in the PUSCH mapping but not used for transmission of PUSCH.

For a UE configured with autonomous uplink,

- if the UE indicates PUSCH ending symbol '1' in uplink control information, or endingSymbolAUL is set to '12', the resource elements in the last SC-FDMA symbol shall be counted in the PUSCH mapping but not used for transmission of PUSCH;

- if the UE indicates PUSCH starting symbol '1' in uplink control information, the resource elements in the first SC-FDMA symbol shall be counted in the PUSCH mapping but not used for transmission of PUSCH.

If uplink frequency-hopping is disabled or the resource blocks allocated for PUSCH transmission are not contiguous in frequency, the set of physical resource blocks to be used for transmission is given by ![](media_svg/image404.svg) [公式≈: ^{n}PRB^{=}^{n}VRB] where ![](media_svg/image122.svg) [公式≈: ^{n}VRB] is obtained from the uplink scheduling grant as described in clause 8.1 in TS36.213[4].

If uplink frequency-hopping with type 1 PUSCH hopping is enabled, the set of physical resource blocks to be used for transmission is given by clause 8.4.1 in TS36.213[4].

If uplink frequency-hopping with predefined hopping pattern is enabled, the set of physical resource blocks to be used for transmission in slot ![](media_svg/image126.svg) [公式≈: ^{n}s] is given by the scheduling grant together with a predefined pattern according to


![](media_svg/image405.svg) [公式≈: n_{n}^{~}_{PRB}_{PRB}_{n}_{~}(_{(}_{VRB}n_{n}_{s}_{s})_{)}_{i}=_{=}_{=}_{=}(_{√}_{⌠}_{∞}_{√}_{⌡}_{⌠}_{⌡}_{∞}_{√}_{⌡}_{⌠}_{⌡}_{∞}n^{~}_{n}_{n}_{n}_{√}_{~}_{VRB}_{n}_{s}_{PRB}_{VRB}_{s}_{2}_{(}+_{∃}_{−}_{n}_{n}_{n}_{~}_{s}f_{VRB}_{⊥}_{PRB}_{)}_{hop}_{N}_{inter}_{intra}_{+}_{RB}_{HO}_{(}(_{⊥}i_{n}_{N})_{s}∪_{−}_{and}_{RB}_{HO}_{)}_{2}N_{subframe}_{∀}_{RB}^{sb}_{inter}_{2}_{∀}+_{N}_{N}(_{sb}_{sb}(N_{−}_{N}_{N}_{=}_{>}_{subframe}_{RB}^{sb}_{hopping}_{sb}_{sb}_{1}_{1}−_{=}_{>}1_{1}_{1})−2_{hopping}(n^{~}_{VRB}modN_{RB}^{sb}))∪f_{m}(i))mod(N_{RB}^{sb}∪N_{sb})]

where ![](media_svg/image122.svg) [公式≈: ^{n}VRB] is obtained from the scheduling grant as described in clause 8.1 in TS36.213[4]. The parameter pusch-HoppingOffset,![](media_svg/image406.svg) [公式≈: _{N}_{RB}HO], is provided by higher layers. The size ![](media_svg/image407.svg) [公式≈: _{N}_{RB}sb] of each sub-band is given by,

![](media_svg/image408.svg) [公式≈: ^{N}^{RB}^{sb}^{=}^{√}^{⌡}^{⌠}_{⌡}_{∞}_{√}(N_{RB}^{UL}−N_{RB}^{HO}^{N}−^{RB}^{UL}N_{RB}^{HO}mod2)N_{sb}_{∃}^{N}N^{sb}_{sb}^{=}>^{1}1]

where the number of sub-bands ![](media_svg/image409.svg) [公式≈: ^{N}sb] is given by higher layers. The function ![](media_svg/image410.svg) [公式: f_{m}(i)⎰{0,1}] determines whether mirroring is used or not. The parameter Hopping-mode provided by higher layers determines if hopping is "inter-subframe" or "intra and inter-subframe".

The hopping function ![](media_svg/image411.svg) [公式: f_{hop}(i)]and the function![](media_svg/image412.svg) [公式: f_{m}(i)] are given by

![](media_svg/image413.svg) [公式≈: ^{f}^{hop}^{(}^{i}^{)}^{=}^{√}^{⌡}^{⌡}^{⌡}^{⌠}^{⌡}^{⌡}_{⌡}_{∞}^{(}(^{f}f^{hop}_{hop}^{(}(^{i}i^{−}−^{1}1^{)})^{+}+^{⊇}^{⊕}_{⊕}_{⊗}^{k}^{i}^{=}_{k}^{∪}^{⊆}^{10}^{i}^{i}_{=}^{∪}^{∪}_{⊆}^{10}^{10}_{i}^{+}_{∪}_{10}^{9}^{+}^{+}^{c}^{1}^{9}_{+}^{(}c_{1}^{k}(^{0}k^{)}^{≠})≠^{2}2^{k}^{−}^{k}^{(}^{−}^{i}^{∪}^{(}^{10}^{i}^{∪}^{10}^{+}^{1}^{+}^{)}^{1}^{)}^{)}^{mod}^{⇒}^{⇐}_{⇐}_{⇔}mod(^{N}^{sb}N_{sb}−^{N}^{N}1^{sb}^{sb})+^{=}^{=}1^{1}^{2})modN_{sb}N_{sb}>2]

![](media_svg/image414.svg) [公式≈: f_{m}(i)=^{√}^{⌡}_{⌠}_{⌡}_{∞}^{i}CURRENT_TX_{c}^{mod}_{(}_{i}_{∪}_{10}^{2}_{)}_NBmod2^{N}N_{N}^{sb}_{sb}_{sb}^{=}=_{>}^{1}1_{1}^{and}and^{intra}inter−^{and}subframe^{inter}^{−}^{subframe}hopping^{hopping}]

where ![](media_svg/image415.svg) [公式: f_{hop}(−1)=0] and the pseudo-random sequence ![](media_svg/image416.svg) [公式: c(i)] is given by clause 7.2 and CURRENT_TX_NB indicates the transmission number for the transport block transmitted in slot ![](media_svg/image126.svg) [公式≈: ^{n}s]as defined in [8]. The pseudo-random sequence generator shall be initialised with ![](media_svg/image417.svg) [公式≈: ^{c}init^{=}^{N}ID^{cell}] for frame structure type 1 and ![](media_svg/image418.svg) [公式≈: c_{init}=2^{9}∪(n_{f}mod4)+N_{ID}^{cell}] for frame structure type 2 at the start of each frame.

For BL/CE UEs, the PRB resources for PUSCH transmission in the first subframe are obtained from the DCI as described in clauses 5.3.3.1.10 and 5.3.3.1.11 in [3], or from higher layers in PUR-Config when PUSCH is transmitted using preconfigured uplink resources. Each of the $ N_{TB}\geq  1 $ PUSCH codewords is transmitted with ![](media_svg/image419.svg) [公式≈: _{N}_{rep}PUSCH_{÷}_{1}]repetitions, where $ N_{TB}$ is the number of transport blocks defined in clause 8.0 of TS 36.213 [4]. The PUSCH transmission spans $ N_{abs}^{PUSCH}\geq  N_{TB}N_{rep}^{PUSCH}$ consecutive subframes, including subframes that are not BL/CE UL subframes where the UE postpones the PUSCH transmission if ![](media_svg/image420.svg) [公式≈: _{N}_{rep}PUSCH_{>}_{1}].

- If uplink resource reservation is enabled for the UE as specified in [9], and the Resource reservation field in the DCI is set to 1, then in case of PUSCH transmission with ![](media_svg/image420.svg) [公式≈: _{N}_{rep}PUSCH_{>}_{1}] associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PUSCH transmission without a corresponding MPDCCH,

- In a subframe that is fully reserved as defined in clause 8.0 in [4], the PUSCH transmission is postponed until the next BL/CE uplink subframe that is not fully reserved.

- In a subframe that is partially reserved, the reserved SC-FDMA symbols shall be counted in the PUSCH mapping but not used for transmission of the PUSCH.

- In case the UE is a BL/CE UE configured with higher layer parameter ce-PUSCH-SubPRB-Config-r15 or subPRB-Allocation in PUR-PUSCH-Config, the PUSCH transmission spans $ N_{abs}^{PUSCH}\geq  N_{TB}N_{rep}^{PUSCH}M_{RU}M_{slots}^{UL}/2 $ consecutive subframes including subframes that are not BL/CE UL subframes where the UE postpones the PUSCH transmission, where $ N_{TB}$ is the number of scheduled TBs if ce-PUSCH-MultiTB-Config is enabled and multiple TBs are scheduled, otherwise $ N_{TB}=1 $.

- For BL/CE UE in CEModeA,

- If PUSCH is transmitted using preconfigured uplink resources,

- PUSCH frequency hopping is enabled when the higher layer parameter pur-PUSCH-FreqHopping is set, otherwise frequency hopping is disabled.

- Else, if PUSCH scheduled by DCI format 6-0A is associated with PUR-RNTI,

- PUSCH frequency hopping is enabled when the higher layer parameter pur-PUSCH-FreqHopping is set and the frequency hopping flag in DCI format 6-0A indicates frequency hopping, otherwise frequency hopping is disabled.

- Else,

- PUSCH frequency hopping is enabled when the higher-layer parameter pusch-HoppingConfig is set and the frequency hopping flag in DCI format 6-0A indicates frequency hopping, otherwise frequency hopping is disabled.

- For BL/CE UE in CEModeB,

- If PUSCH is transmitted using preconfigured uplink resources,

- PUSCH frequency hopping is enabled when the higher layer parameter pur-PUSCH-FreqHopping is set, otherwise frequency hopping is disabled.

- Else, if PUSCH scheduled by DCI format 6-0B is associated with PUR-RNTI,

- PUSCH frequency hopping is enabled when the higher layer parameter pur-PUSCH-FreqHopping is set, otherwise frequency hopping is disabled.

- Else,

- PUSCH frequency hopping is enabled when the higher-layer parameter pusch-HoppingConfig is set, otherwise frequency hopping is disabled.

- If frequency hopping is not enabled for PUSCH, all PUSCH repetitions are located at the same PRB resources.

- If a BL/CE UE is configured with higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocConfig, the UE is not expected to have the frequency hopping enabled for PUSCH with the resource allocation including the center PRB not belonging to any narrowband.

- If frequency hopping is enabled for PUSCH and the UE is not configured with CEModeA and higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocConfig,

- PUSCH is transmitted in uplink subframe ![](media_svg/image421.svg) [公式: i] within the ![](media_svg/image422.svg) [公式≈: _{N}_{abs}PUSCH] consecutive subframes using the same number of consecutive PRBs as in the previous subframe starting from the PRB resources of the narrowband ![](media_svg/image423.svg) [公式≈: _{n}_{NB}()i] with the same RIV as that of narrowband ![](media_svg/image424.svg) [公式≈: _{n}_{NB}()i_{0}]. The narrowband ![](media_svg/image423.svg) [公式≈: _{n}_{NB}()i] is defined as

![](media_svg/image425.svg) [公式≈: ^{n}^{NB}^{(}^{i}_{j}_{i}^{)}_{0}_{0}_{≥}^{=}_{=}_{i}^{√}^{⌡}^{⌠}⌡∞_{√}_{i}(_{≥}^{n}_{0}n^{NB}^{(}NB_{i}^{i}^{(}^{0}^{i}_{0}_{N}^{0}^{)}^{)}_{+}_{NB}_{ch,}+_{N}_{UL}f_{abs}_{PUSCH}NB,^{PUSCH}_{∃}hop_{−})mod_{1}NNB^{UL}^{if}if^{√}√^{i}i^{N}N^{NB}NB^{ch,}^{ch,}^{UL}^{UL}^{−}−^{j}j^{0}0^{∃}∃^{mod}mod^{2}2^{=}=^{0}1]

where ![](media_svg/image426.svg) [公式≈: ^{i}0] is the absolute subframe number of the first UL subframe intended for carrying the PUSCH and ![](media_svg/image69.svg) [公式≈: _{N}_{NB}ch,UL] and ![](media_svg/image70.svg) [公式≈: ^{f}NB,^{PUSCH}hop] are cell-specific higher-layer parameters. For the ![](media_svg/image427.svg) [公式≈: _{N}_{abs}PUSCH] consecutive subframes, the UE shall not transmit PUSCH in subframe ![](media_svg/image428.svg) [公式: i] if it is not a BL/CE UL subframe.

- If frequency hopping is enabled for PUSCH and the UE is configured with CEModeA and higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocConfig,

- Except when the PUSCH resource allocation includes the center PRB not belonging to any narrowband, PUSCH is transmitted in uplink subframe  within the  consecutive subframes using the same number of consecutive PRBs as in the previous subframe, where $ n_{NB}^{(i_{0})}$ is the narrowband index that starting PRB located in the absolute subframe number of the first UL subframe $ i_{0}$, defined as

- If $ N_{RB}^{UL}mod 2=$ 0 or $ N_{RB}^{UL}mod 2=1 $ with $ RB_{START}<\lfloor  \frac {N_{RB}^{UL}}{2}\rfloor  $,  $ n_{NB}^{(i_{0})}=\lfloor  \frac {RB_{START}-l_{e}}{6}\rfloor  $

- If $ N_{RB}^{UL}mod 2=1 $ with $ RB_{START}>\lfloor  \frac {N_{RB}^{UL}}{2}\rfloor  ,$  $ n_{NB}^{(i_{0})}=\lfloor  \frac {RB_{START}-l_{e}-1}{6}\rfloor  $

where $ l_{e}=\lfloor  \frac {N_{RB}^{UL}}{2}\rfloor  -\frac {6N_{NB}^{UL}}{2}$ is the number of edge PRB(s) not belonging to narrowbands in one side of system bandwidth $ N_{RB}^{UL}$, $ N_{NB}^{UL}$ is the number of narrowbands, the starting PRB index $ RB_{START}$ and the length  $ L_{CRBs}$ of the allocated resources are defined in clause 8.1.1 of [4]. After hopping, the narrowband ![](media_svg/image423.svg) [公式≈: _{n}_{NB}()i] in subframe  is defined as

![](media_svg/image425.svg) [公式≈: ^{n}^{NB}^{(}^{i}_{j}_{i}^{)}_{0}_{0}_{≥}^{=}_{=}_{i}^{√}^{⌡}^{⌠}⌡∞_{√}_{i}(_{≥}^{n}_{0}n^{NB}^{(}NB_{i}^{i}^{(}^{0}^{i}_{0}_{N}^{0}^{)}^{)}_{+}_{NB}_{ch,}+_{N}_{UL}f_{abs}_{PUSCH}NB,^{PUSCH}_{∃}hop_{−})mod_{1}NNB^{UL}^{if}if^{√}√^{i}i^{N}N^{NB}NB^{ch,}^{ch,}^{UL}^{UL}^{−}−^{j}j^{0}0^{∃}∃^{mod}mod^{2}2^{=}=^{0}1]

where ![](media_svg/image69.svg) [公式≈: _{N}_{NB}ch,UL] and ![](media_svg/image70.svg) [公式≈: ^{f}NB,^{PUSCH}hop] are cell-specific higher-layer parameters. For the  ![](media_svg/image427.svg) [公式≈: _{N}_{abs}PUSCH] consecutive subframes, the UE shall not transmit PUSCH in subframe ![](media_svg/image428.svg) [公式: i] if it is not a BL/CE UL subframe. After hopping, the resource blocks have the same relative location of starting PRB in $ n_{NB}^{(i)}$ as in narrowband $ n_{NB}^{(i_{0})}$.

- If frequency hopping is enabled for PUSCH and the UE is configured with higher layer parameter ce-PUSCH-FlexibleStartPRB-AllocConfig,

- If a frequency hopping leads to a split resource allocation, where some PRB(s) is (are) on one edge and some PRB(s) is (are) on the other edge of the system bandwidth, the PUSCH transmission is dropped in that subframe.

- If a frequency hopping leads to a resource allocation, where some PRB(s) is (are) not belonging to any narrowband, the PUSCH transmission is dropped in that subframe.

For BL/CE UEs, for PUSCH transmission corresponding to the random access response grant and its retransmission, frequency hopping of the PUSCH is enabled when higher layer parameter rar-HoppingConfig is set. Further

- if PRACH CE level 0 or 1 is used for the last PRACH attempt, ![](media_svg/image69.svg) [公式≈: _{N}_{NB}ch,UL] is set to the higher layer parameter interval-UlHoppingConfigCommonModeA;

- if PRACH CE level 2 or 3 is used for the last PRACH attempt, ![](media_svg/image69.svg) [公式≈: _{N}_{NB}ch,UL] is set to the higher layer parameter interval-UlHoppingConfigCommonModeB.

For BL/CE UEs in CEModeB, for PUSCH transmission not associated with Temporary C-RNTI, for frame structure type 1, after a transmission duration of ![](media_svg/image431.svg) [公式: 256∪30720T_{s}] time units (which may include subframes that are not BL/CE UL subframes), a gap of ![](media_svg/image432.svg) [公式: 40∪30720T_{s}] time units shall be inserted, according to the UE capability ue-CE-NeedULGaps, as specified in TS 36.331 [9]. BL/CE UL subframes within the gap of ![](media_svg/image432.svg) [公式: 40∪30720T_{s}] time units shall be counted for the PUSCH resource mapping but not used for transmission of the PUSCH.

For BL/CE UEs, for PUSCH transmission associated with Temporary C-RNTI for frame structure type 1, and if PRACH CE level 2 or 3 is used for the last PRACH attempt, after a transmission duration of ![](media_svg/image431.svg) [公式: 256∪30720T_{s}] time units (which may include subframes that are not BL/CE UL subframes), a gap of ![](media_svg/image432.svg) [公式: 40∪30720T_{s}] time units shall be inserted. BL/CE UL subframes within the gap of ![](media_svg/image432.svg) [公式: 40∪30720T_{s}] time units shall be counted for the PUSCH resource mapping but not used for transmission of the PUSCH.

For UEs configured with PUSCH-EnhancementsConfig, the number of PUSCH subframe repetitions ![](media_svg/image433.svg) [公式≈: _{N}_{rep}PUSCH] and the PRB resources for PUSCH transmission in the first subframe are obtained from the DCI as described in clause 5.3.3.1.1C in [3]. The PUSCH transmission spans ![](media_svg/image434.svg) [公式≈: _{N}_{abs}PUSCH_{÷}_{N}_{rep}PUSCH] consecutive subframes, including DL subframes where the UE postpones the PUSCH transmission in the case of frame structure type 2. PUSCH frequency hopping is enabled when the higher-layer parameters pusch-HoppingOffsetPUSCH-Enh and interval-ULHoppingPUSCH-Enh are set and the frequency hopping flag in DCI format 0C indicates frequency hopping, otherwise frequency hopping is disabled. If frequency hopping is not enabled for PUSCH, the PUSCH repetitions are located at the same PRB resources as in the first subframe. If frequency hopping is enabled for PUSCH, PUSCH is transmitted in uplink subframe ![](media_svg/image421.svg) [公式: i] within the ![](media_svg/image435.svg) [公式≈: _{N}_{rep}PUSCH] consecutive subframes using the PRB resources starting at PRB index ![](media_svg/image436.svg) [公式≈: _{n}_{PRB}(i)]

$ n_{PRB}^{\left ( i\right ) }={\begin {matrix}n_{PRB}^{\left ( i_{0}\right ) } & if\lfloor  \frac {i}{N_{PRB,hop}^{PUSCH}}-j_{0}\rfloor  mod 2=0 \\ \left ( n_{PRB}^{\left ( i_{0}\right ) }+f_{PRB,hop}^{PUSCH}\right ) modN_{PRB}^{UL} & if\lfloor  \frac {i}{N_{PRB,hop}^{PUSCH}}-j_{0}\rfloor  mod 2=1\end {matrix}$

$ j_{0}=\lfloor  \frac {i_{0}}{N_{PRB,hop}^{PUSCH}}\rfloor  ,i_{0}\leq  i\leq  i_{0}+N_{abs}^{PUSCH}-1 $

where ![](media_svg/image426.svg) [公式≈: ^{i}0] is the absolute subframe number of the first UL subframe carrying the PUSCH and ![](media_svg/image437.svg) [公式≈: ^{N}PRB,^{PUSCH}hop] is given by the higher-layer parameter interval-ULHoppingPUSCH-Enh and ![](media_svg/image438.svg) [公式≈: ^{f}PRB,^{PUSCH}hop] is given by the higher-layer parameter pusch-HoppingOffsetPUSCH-Enh.

For BL/CE UEs communicating over NTN, for PUSCH transmission, for frame structure type 1, after a transmission duration of $ N_{segment}^{precompensation}$ time units (which may include subframes that are not BL/CE UL subframes), a transmission gap of $ N_{gap}^{precompensation}$ time units shall be counted for the PUSCH resource mapping but not used for transmission of the PUSCH, according to the single UE capability ntn-SegmentedPrecompensationGaps-r17, as specified in 3GPP TS 36.331 [9]. The quantity $ N_{segment}^{precompensation}$ is provided by higher layers, and the quantity $ N_{gap}^{precompensation}$ is configured by higher layers based on the UE capability, if signalled.

## 5.4 Physical uplink control channel

The physical uplink control channel, PUCCH, carries uplink control information. Simultaneous transmission of PUCCH and PUSCH from the same UE is supported if enabled by higher layers. For frame structure type 2, the PUCCH is not transmitted in the UpPTS field.

The physical uplink control channel supports multiple formats as shown in Table 5.4-1 with different number of bits per subframe, where ![](media_svg/image439.svg) [公式≈: _{M}_{RB}PUCCH4] represents the bandwidth of the PUCCH format 4 as defined by clause 5.4.2B, and ![](media_svg/image440.svg) [公式≈: _{N}_{0}PUCCH] and ![](media_svg/image441.svg) [公式≈: _{N}_{1}PUCCH] are defined in Table 5.4.2C-1.

Formats 2a and 2b are supported for normal cyclic prefix only.

Table 5.4-1: Supported PUCCH formats

| PUCCH format | Modulation scheme | Number of bits per subframe, ![](media_svg/image442.svg) [公式≈: ^{M}bit] |
| --- | --- | --- |
| 1 | N/A | N/A |
| 1a | BPSK | 1 |
| 1b | QPSK | 2 |
| 2 | QPSK | 20 |
| 2a | QPSK+BPSK | 21 |
| 2b | QPSK+QPSK | 22 |
| 3 | QPSK | 48 |
| 4 | QPSK | ![](media_svg/image443.svg) [公式≈: _{M}_{RB}PUCCH4_{∪}_{N}_{sc}RB_{∪}_{(}_{N}_{0}PUCCH_{+}_{N}_{1}PUCCH_{)}_{∪}_{2}] |
| 5 | QPSK | ![](media_svg/image444.svg) [公式≈: _{N}_{sc}RB_{∪}_{(}_{N}_{0}PUCCH_{+}_{N}_{1}PUCCH_{)}] |

All PUCCH formats use a cyclic shift, ![](media_svg/image445.svg) [公式≈: n_{cs}^{cell}(n_{s},l)], which varies with the symbol number ![](media_svg/image398.svg) [公式: l] and the slot number ![](media_svg/image126.svg) [公式≈: ^{n}s] according to

![](media_svg/image446.svg) [公式≈: n_{cs}^{cell}(n_{s},l)=_{⊆}_{i}^{7}_{=}_{0}c(8N_{symb}^{UL}∪n_{s}+8l+i)∪2^{i}]

where the pseudo-random sequence ![](media_svg/image447.svg) [公式: c(i)] is defined by clause 7.2. The pseudo-random sequence generator shall be initialized with ![](media_svg/image448.svg) [公式≈: ^{c}init^{=}^{n}ID^{RS}], where ![](media_svg/image449.svg) [公式≈: _{n}_{ID}RS] is given by clause 5.5.1.5 with ![](media_svg/image450.svg) [公式≈: _{N}_{ID}cell] corresponding to the primary cell, at the beginning of each radio frame.

The physical resources used for PUCCH format 1/1a/1b and PUCCH format 2/2a/2b depends on two parameters, ![](media_svg/image42.svg) [公式≈: _{N}_{RB}(2)] and ![](media_svg/image41.svg) [公式≈: _{N}_{cs}(1)], given by higher layers. 
The variable ![](media_svg/image451.svg) [公式: N_{RB}^{(2)}÷0] denotes the bandwidth in terms of resource blocks that are available for use by PUCCH formats 2/2a/2b transmission in each slot. The variable ![](media_svg/image452.svg) [公式≈: _{N}_{cs}(1)] denotes the number of cyclic shift used for PUCCH formats 1/1a/1b in a resource block used for a mix of formats 1/1a/1b and 2/2a/2b. The value of ![](media_svg/image452.svg) [公式≈: _{N}_{cs}(1)] is an integer multiple of ![](media_svg/image453.svg) [公式≈: _{δ}PUCCH_{shift}] within the range of {0, 1, …, 7}, where ![](media_svg/image453.svg) [公式≈: _{δ}PUCCH_{shift}] is provided by higher layers. No mixed resource block is present if ![](media_svg/image454.svg) [公式: N_{cs}^{(1)}=0]. At most one resource block in each slot supports a mix of formats 1/1a/1b and 2/2a/2b. 
Resources used for transmission of PUCCH formats 1/1a/1b, 2/2a/2b, 3, 4, and 5 are represented by the non-negative indices ![](media_svg/image455.svg) [公式≈: _{n}_{PUCCH}(1,^{~}p)], ![](media_svg/image456.svg) [公式≈: nPUCCH^{(2,}^{~}^{p}^{)}<NRB^{(2)}Nsc^{RB}+^{⊥}⋅_{⋅}_{⋅}^{N}_{8}^{cs}^{(1)}^{∀}∂_{∂}_{∂}∪(Nsc^{RB}−Ncs^{(1)}−2)], ![](media_svg/image457.svg) [公式≈: _{n}_{PUCCH}(3,^{~}p)], ![](media_svg/image458.svg) [公式≈: ^{n}PUCCH^{(4)}] and ![](media_svg/image459.svg) [公式≈: ^{n}PUCCH^{(5)}], respectively.

### 5.4.1 PUCCH formats 1, 1a and 1b

For PUCCH format 1, information is carried by the presence/absence of transmission of PUCCH from the UE. 
In the remainder of this clause, ![](media_svg/image460.svg) [公式: d(0)=1] shall be assumed for PUCCH format 1.

For PUCCH formats 1a and 1b, one or two explicit bits are transmitted, respectively. The block of bits ![](media_svg/image461.svg) [公式: b(0),...,b(M_{bit}−1)] shall be modulated as described in Table 5.4.1-1, resulting in a complex-valued symbol![](media_svg/image462.svg) [公式: d(0)]. 
The modulation schemes for the different PUCCH formats are given by Table 5.4-1.

The complex-valued symbol ![](media_svg/image463.svg) [公式: d(0)] shall be multiplied with a cyclically shifted length ![](media_svg/image464.svg) [公式≈: _{N}_{seq}PUCCH_{=}_{12}] sequence ![](media_svg/image465.svg) [公式≈: r_{u}^{(}_{,}^{Α}_{v}^{~}^{p}^{)}(n)] for each of the ![](media_svg/image466.svg) [公式: P] antenna ports used for PUCCH transmission according to

![](media_svg/image467.svg) [公式≈: y^{(}^{~}^{p}^{,}^{Δ}^{)}(n)=^{1}_{P}d(0)∪r_{u}^{(}_{,}^{Α}_{v}^{~}^{p}^{,}^{Δ}^{)}(n),n=0,1,...,N_{seq}^{PUCCH}−1]

where ![](media_svg/image468.svg) [公式≈: _{r}_{u}(_{,}Α_{v}~_{p},Δ)_{(}_{n}_{)}] is defined by clause 5.5.1 with![](media_svg/image469.svg) [公式≈: _{M}_{sc}RS_{=}_{N}_{seq}PUCCH] and ![](media_svg/image470.svg) [公式: Δ=0]. The antenna-port specific cyclic shift ![](media_svg/image471.svg) [公式: Α~_{p}] varies between symbols and slots as defined below.

The block of complex-valued symbols ![](media_svg/image472.svg) [公式≈: y^{(}^{~}^{p}^{)}(0),...,y^{(}^{~}^{p}^{)}(N_{seq}^{PUCCH}−1)] shall be scrambled by ![](media_svg/image473.svg) [公式: S(n_{s})] and block-wise spread with the antenna-port specific orthogonal sequence ![](media_svg/image474.svg) [公式≈: w_{n}_{oc}_{(}^{~}_{p}_{)}(i)] according to

![](media_svg/image475.svg) [公式≈: z^{(}^{~}^{p}^{)}(m&apos;∪NSF^{PUCCH}∪Nseq^{PUCCH}+m∪Nseq^{PUCCH}+n)=S(ns)∪wn_{oc}(~p)(m)∪y^{(}^{~}^{p}^{)}(n)]

where

![](media_svg/image476.svg) [公式≈: ^{m}^{n}m&apos;^{=}^{=}=^{0}^{0}0^{,...,}^{,...,},1^{N}^{N}^{seq}^{PUCCH}^{SF}^{PUCCH}^{−}^{−}^{1}^{1}]

and

![](media_svg/image477.svg) [公式≈: _{S}_{(}_{n}_{s}_{)}_{=}√_{⌠}_{∞}_{e}1_{j}_{Π}_{2}ifn_{otherwise}±~_{p}(n_{s})mod2=0]

with ![](media_svg/image478.svg) [公式≈: _{N}_{SF}PUCCH] for the two slots in a subframe given by Table 5.4.1-1a. The sequence ![](media_svg/image479.svg) [公式≈: w_{n}_{oc}_{(}^{~}_{p}_{)}(i)] is given by Table 5.4.1-2 and Table 5.4.1-3 and ![](media_svg/image480.svg) [公式: n±~_{p}(n_{s})] is defined below.

Resources used for transmission of PUCCH format 1, 1a and 1b are identified by a resource index ![](media_svg/image481.svg) [公式≈: _{n}_{PUCCH}(1,^{~}p)] from which the orthogonal sequence index ![](media_svg/image482.svg) [公式≈: n_{oc}^{(}^{~}^{p}^{)}(n_{s})] and the cyclic shift ![](media_svg/image483.svg) [公式: Α~_{p}(n_{s},l)] are determined according to

![](media_svg/image484.svg) [公式≈: _{n}^{Α}_{cs}_{(}^{n}_{~}_{p}^{~}^{oc}^{p}^{(}_{)}^{~}^{p}^{(}_{(}^{)}^{n}_{n}^{(}^{s}_{s}^{n}^{,}_{,}^{s}^{l}_{l}^{)}^{)}_{)}^{=}^{=}_{=}^{√}^{⌡}^{⌠}^{⌡}^{∞}^{2}^{√}_{⌡}_{⌠}_{⌡}_{∞}^{Π}{_{{}^{2}^{√}n_{n}^{n}^{∪}_{cs}_{cs}^{cell}_{cell}^{∪}^{±}^{~}^{p}^{√}^{n}^{n}^{(}^{cs}^{(}^{n}^{±}^{~}^{p}(_{(}^{~}^{p}n_{n}^{s}^{(}^{)}^{)}_{s}_{s}^{n}^{(}^{∪},_{,}^{n}^{s}l_{l}^{δ}^{)}^{s})_{)}^{PUCCH}^{,}^{∪}^{shift}+_{+}^{l}^{δ}^{)}(_{(}^{PUCCH}^{shift}n_{n}^{N}±_{±}~_{~}_{p}_{p}(_{(}^{sc}^{RB}n_{n}^{N}_{s}_{s})_{)}^{±}^{N}∪_{∪}^{∃}δ_{δ}^{±}^{PUCCH}_{PUCCH}^{∃}_{shift}_{shift}^{for }^{for }+_{+}^{extended}^{normal}(_{n}n_{oc}_{(}_{oc}^{(}_{~}_{p}^{~}^{p}_{)}^{)}_{(}(_{n}n_{s}^{cyclic}_{s}_{)})^{cyclic}mod_{2}_{)}_{mod}^{prefix}δ^{prefix}^{PUCCH}_{shift}_{N}_{±}_{}}_{mod}))mod_{N}_{sc}N_{RB}±}modN_{sc}^{RB}for _{for }_{extended}normalcyclic_{cyclic}prefix_{prefix}]

where

![](media_svg/image485.svg) [公式≈: ^{c}^{N}^{=}^{±}^{=}^{√}^{⌠}_{∞}^{3}2^{√}^{⌡}^{⌠}^{⌡}^{∞}^{N}^{N}^{sc}^{cs}extended^{normal}^{(1)}^{RB}^{if}^{otherwise}^{n}^{cyclic}^{PUCCH}^{(1,}cyclic^{~}^{p}^{)}^{prefix}^{<}prefix^{c}^{∪}^{N}^{cs}^{(1)}^{δ}^{PUCCH}^{shift}]

The resource indices within the two resource blocks in the two slots of a subframe to which the PUCCH is mapped are given by

![](media_svg/image486.svg) [公式≈: n±~p(ns)=^{√}^{⌡}⌠_{⌡}_{∞}_{(}^{n}_{n}^{PUCCH}^{(}_{PUCCH}^{1}(1^{,},^{~}^{p}~p^{)})_{−}_{c}_{∪}_{N}_{cs}(1)_{δ}PUCCH_{shift}_{)}_{mod}_{(}_{c}_{∪}_{N}_{sc}RB_{δ}PUCCH_{shift}_{)}^{if}_{otherwise}^{n}^{PUCCH}^{(}^{1}^{,}^{~}^{p}^{)}^{<}^{c}^{∪}^{N}^{cs}^{(1)}^{δ}^{PUCCH}^{shift}]

for ![](media_svg/image487.svg) [公式: n_{s}mod2=0] and by

![](media_svg/image488.svg) [公式≈: ^{n}^{±}^{~}^{p}^{(}^{n}^{s}^{)}^{=}^{√}^{⌡}^{⌠}⌡_{∞}^{{}√^{c}h^{(}~p^{n}^{±}^{~}/^{p}c^{(}^{n}∃^{s}+^{−}(h^{1}~p^{)}^{+}mod^{1}^{)}^{}}c^{mod})N&apos;/^{(}^{cN}δ^{PUCCH}shift^{sc}^{RB}^{δ}^{PUCCH}^{shift}^{+}^{1}^{)}^{−}^{1}otherwise^{n}^{PUCCH}^{(}^{1}^{,}^{~}^{p}^{)}^{÷}^{c}^{∪}^{N}^{cs}^{(1)}^{δ}^{PUCCH}^{shift}]

for ![](media_svg/image489.svg) [公式: n_{s}mod2=1], where ![](media_svg/image490.svg) [公式≈: h~_{p}=(n±~_{p}(n_{s}−1)+d)mod(cN&apos;δ^{PUCCH}_{shif}_{t})], with ![](media_svg/image491.svg) [公式: d=2]for normal CP and ![](media_svg/image492.svg) [公式: d=0]for extended CP.

The parameter deltaPUCCH-Shift ![](media_svg/image493.svg) [公式≈: _{δ}PUCCH_{shift}] is provided by higher layers.

Table 5.4.1-1: Modulation symbol ![](media_svg/image494.svg) [公式: d(0)] for PUCCH formats 1a and 1b

| PUCCH format | ![](media_svg/image495.svg) [公式: b(0),...,b(M_{bit}−1)] | ![](media_svg/image496.svg) [公式: d(0)] |
| --- | --- | --- |
| 1a | 0 | ![](media_svg/image497.svg) [公式: 1] |
|  | 1 | ![](media_svg/image498.svg) [公式: −1] |
| 1b | 00 | ![](media_svg/image497.svg) [公式: 1] |
|  | 01 | ![](media_svg/image499.svg) [公式: −j] |
|  | 10 | ![](media_svg/image500.svg) [公式: j] |
|  | 11 | ![](media_svg/image498.svg) [公式: −1] |

Table 5.4.1-1a: The quantity ![](media_svg/image501.svg) [公式≈: _{N}_{SF}PUCCH] for PUCCH formats 1a and 1b

| PUCCH format | ![](media_svg/image501.svg) [公式≈: _{N}_{SF}PUCCH] |  |
| --- | --- | --- |
|  | first slot | second slot |
| normal 1/1a/1b | 4 | 4 |
| shortened 1/1a/1b | 4 | 3 |
|  |  |  |
|  |  |  |

Table 5.4.1-2: Orthogonal sequences ![](media_svg/image502.svg) [公式≈: {w(0)λw(N_{SF}^{PUCCH}−1)}] for ![](media_svg/image503.svg) [公式≈: _{N}_{SF}PUCCH_{=}_{4}]

| Sequence index ![](media_svg/image504.svg) [公式≈: n_{oc}^{(}^{~}^{p}^{)}(n_{s})] | Orthogonal sequences ![](media_svg/image502.svg) [公式≈: {w(0)λw(N_{SF}^{PUCCH}−1)}] |
| --- | --- |
| 0 |  |
| 1 |  |
| 2 |  |

Table 5.4.1-3: Orthogonal sequences ![](media_svg/image502.svg) [公式≈: {w(0)λw(N_{SF}^{PUCCH}−1)}] for ![](media_svg/image508.svg) [公式≈: _{N}_{SF}PUCCH_{=}_{3}]

| Sequence index ![](media_svg/image509.svg) [公式≈: n_{oc}^{(}^{~}^{p}^{)}(n_{s})] | Orthogonal sequences ![](media_svg/image502.svg) [公式≈: {w(0)λw(N_{SF}^{PUCCH}−1)}] |
| --- | --- |
| 0 | ![](media_svg/image510.svg) [公式: {111}] |
| 1 | ![](media_svg/image511.svg) [公式≈: _{{}_{1}_{e}j2Π3_{e}j4Π3_{}}] |
| 2 | ![](media_svg/image512.svg) [公式≈: _{{}_{1}_{e}j4Π3_{e}j2Π3_{}}] |

### 5.4.2 PUCCH formats 2, 2a and 2b

The block of bits ![](media_svg/image513.svg) [公式: b(0),...,b(19)] shall be scrambled with a UE-specific scrambling sequence, resulting in a block of scrambled bits ![](media_svg/image514.svg) [公式: b^{~}(0),...,b^{~}(19)] according to

![](media_svg/image515.svg) [公式: b^{~}(i)=(b(i)+c(i))mod2]

where the scrambling sequence ![](media_svg/image447.svg) [公式: c(i)] is given by clause 7.2. The scrambling sequence generator shall be initialised with ![](media_svg/image516.svg) [公式≈: c_{init}=(_{√}n_{s}2_{∃}+1)∪(2N_{ID}^{cell}+1)∪2^{16}+n_{RNTI}] at the start of each subframe where ![](media_svg/image517.svg) [公式≈: ^{n}RNTI] is C-RNTI.

The block of scrambled bits ![](media_svg/image518.svg) [公式: b^{~}(0),...,b^{~}(19)] shall be QPSK modulated as described in clause 7.1, resulting in a block of complex-valued modulation symbols ![](media_svg/image519.svg) [公式: d(0),...,d(9)].

Each complex-valued symbol ![](media_svg/image519.svg) [公式: d(0),...,d(9)] shall be multiplied with a cyclically shifted length ![](media_svg/image464.svg) [公式≈: _{N}_{seq}PUCCH_{=}_{12}] sequence ![](media_svg/image520.svg) [公式≈: _{r}_{u}(_{,}Α_{v}~_{p},Δ)_{(}_{n}_{)}] for each of the ![](media_svg/image521.svg) [公式: P] antenna ports used for PUCCH transmission according to

![](media_svg/image522.svg) [公式≈: z^{(}^{~}^{p}^{)}(N_{seq}^{PUCCH}∪n+i_{n})_{i}=_{=}_{=}_{0}_{0}_{,}_{,}^{1}_{1}_{1}_{P}_{,...,}_{,...,}d_{9}(_{N}n_{sc})_{RB}∪r_{u}_{−}^{(}_{,}^{Α}_{v}_{1}^{~}^{p}^{,}^{Δ}^{)}(i)]

where ![](media_svg/image523.svg) [公式≈: _{r}_{u}(_{,}Α_{v}~_{p},Δ)_{(}_{i}_{)}] is defined by clause 5.5.1 with![](media_svg/image469.svg) [公式≈: _{M}_{sc}RS_{=}_{N}_{seq}PUCCH] and ![](media_svg/image470.svg) [公式: Δ=0].

Resources used for transmission of PUCCH formats 2/2a/2b are identified by a resource index ![](media_svg/image524.svg) [公式≈: _{n}_{PUCCH}(2,^{~}p)] from which the cyclic shift ![](media_svg/image525.svg) [公式: Α~_{p}(n_{s},l)] is determined according to

![](media_svg/image526.svg) [公式≈: Α~_{p}(n_{s},l)=2Π∪n_{cs}^{(}^{~}^{p}^{)}(n_{s},l)N_{sc}^{RB}]

where

![](media_svg/image527.svg) [公式≈: n_{cs}^{(}^{~}^{p}^{)}(n_{s},l)=(n_{cs}^{cell}(n_{s},l)+n±~_{p}(n_{s}))modN_{sc}^{RB}]

and

![](media_svg/image528.svg) [公式≈: ^{n}^{±}^{~}^{p}^{(}^{n}^{s}^{)}^{=}^{√}^{⌡}^{⌠}⌡_{∞}(^{n}n^{PUCCH}^{(2,}_{PUCCH}^{(2,}^{~}^{p}^{~}^{p}^{)}^{)}^{mod}+N_{cs}^{(1)}^{N}^{sc}^{RB}+1)modN_{sc}^{RB}^{if}otherwise^{n}^{PUCCH}^{(}^{2}^{,}^{~}^{p}^{)}^{<}^{N}^{sc}^{RB}^{N}^{RB}^{(2)}]

for ![](media_svg/image487.svg) [公式: n_{s}mod2=0] and by

![](media_svg/image529.svg) [公式≈: _{n}_{±}_{~}_{p}_{(}_{n}_{s}_{)}_{=}√⌡_{⌠}_{⌡}_{∞}{_{(}N_{N}sc_{sc}^{RB}_{RB}(_{−}n±~p_{2}(_{−}ns_{n}−_{PUCCH}_{(}_{2}1_{,}_{~}_{p})_{)}+1_{)})}_{mod}mod_{N}(N_{sc}_{RB}sc^{RB}+1)−1if_{otherwise}nPUCCH^{(}^{2}^{,}^{~}^{p}^{)}<Nsc^{RB}NRB^{(2)}]

for ![](media_svg/image489.svg) [公式: n_{s}mod2=1].

For PUCCH formats 2a and 2b, supported for normal cyclic prefix only, the bit(s) ![](media_svg/image530.svg) [公式: b(20),...,b(M_{bit}−1)] shall be modulated as described in Table 5.4.2-1 resulting in a single modulation symbol ![](media_svg/image531.svg) [公式: d(10)] used in the generation of the reference-signal for PUCCH format 2a and 2b as described in clause 5.5.2.2.1.

Table 5.4.2-1: Modulation symbol ![](media_svg/image531.svg) [公式: d(10)] for PUCCH formats 2a and 2b

| PUCCH format | ![](media_svg/image530.svg) [公式: b(20),...,b(M_{bit}−1)] | ![](media_svg/image531.svg) [公式: d(10)] |
| --- | --- | --- |
| 2a | 0 | ![](media_svg/image497.svg) [公式: 1] |
|  | 1 | ![](media_svg/image498.svg) [公式: −1] |
| 2b | 00 | ![](media_svg/image497.svg) [公式: 1] |
|  | 01 | ![](media_svg/image499.svg) [公式: −j] |
|  | 10 | ![](media_svg/image500.svg) [公式: j] |
|  | 11 | ![](media_svg/image498.svg) [公式: −1] |

### 5.4.2A PUCCH format 3

The block of bits ![](media_svg/image532.svg) [公式: b(0),...,b(M_{bit}−1)] shall be scrambled with a UE-specific scrambling sequence, resulting in a block of scrambled bits ![](media_svg/image533.svg) [公式: b^{~}(0),...,b^{~}(M_{bit}−1)] according to

![](media_svg/image534.svg) [公式: b^{~}(i)=(b(i)+c(i))mod2]

where the scrambling sequence ![](media_svg/image447.svg) [公式: c(i)] is given by clause 7.2. The scrambling sequence generator shall be initialised with ![](media_svg/image535.svg) [公式≈: c_{init}=(_{√}n_{s}2_{∃}+1)∪(2N_{ID}^{cell}+1)∪2^{16}+n_{RNTI}] at the start of each subframe where ![](media_svg/image517.svg) [公式≈: ^{n}RNTI] is the C-RNTI.

The block of scrambled bits ![](media_svg/image536.svg) [公式: b^{~}(0),...,b^{~}(M_{bit}−1)] shall be QPSK modulated as described in Clause 7.1, resulting in a block of complex-valued modulation symbols ![](media_svg/image537.svg) [公式≈: d(0),...,d(M_{symb}−1)] where ![](media_svg/image538.svg) [公式≈: ^{M}symb^{=}^{M}bit^{2}^{=}^{2}^{N}sc^{RB}].

The complex-valued symbols ![](media_svg/image539.svg) [公式≈: d(0),...,d(M_{symb}−1)] shall be block-wise spread with the orthogonal sequences ![](media_svg/image540.svg) [公式≈: w_{n}_{oc}_{(}^{~}_{p}_{,}_{)}_{0}(i)] and ![](media_svg/image541.svg) [公式≈: w_{n}_{oc}_{(}^{~}_{p}_{,}_{)}_{1}(i)] resulting in ![](media_svg/image542.svg) [公式≈: _{N}_{SF,0}PUCCH_{+}_{N}_{SF,1}PUCCH] sets of ![](media_svg/image543.svg) [公式≈: _{N}_{sc}RB] values each according to

![](media_svg/image544.svg) [公式≈: _{y}_{n}(~p)_{(}_{i}_{n}_{n}_{)}_{i}_{=}_{=}_{=}_{=}_{0}_{0}^{√}⌡_{⌠}_{⌡}_{∞}_{n}_{,...,}_{,}w_{w}_{1}_{mod}_{,...,}n_{n}oc_{oc}(_{(}~_{~}p_{p}_{N},_{,})_{)}_{1}0_{N}_{(}_{SF,}_{N}(_{PUCCH}_{n}n_{sc}_{RB}_{SF,}_{PUCCH}_{)}_{0})_{∪}∪_{0}_{e}e_{−}_{j}^{j}_{1}_{Π}^{Π}_{+}_{√}^{√}_{n}^{n}_{N}_{cs}_{cell}^{cs}^{cell}_{SF,}_{PUCCH}_{(}^{(}_{n}^{n}_{1}_{s}^{s}_{,}^{,}_{l}^{l}_{)}^{)}_{64}^{64}_{−}_{∃}^{∃}_{1}_{2}^{2}_{∪}∪_{d}d_{(}(_{N}i)_{sc}_{RB}_{+}_{i}_{)}_{otherwise}n<NSF,^{PUCCH}0]

where ![](media_svg/image545.svg) [公式≈: _{N}_{SF,0}PUCCH_{=}_{N}_{SF,1}PUCCH_{=}_{5}] for both slots in a subframe using normal PUCCH format 3 and ![](media_svg/image546.svg) [公式≈: _{N}_{SF,0}PUCCH_{=}_{5}], ![](media_svg/image547.svg) [公式≈: _{N}_{SF,1}PUCCH_{=}_{4}]holds for the first and second slot, respectively, in a subframe using shortened PUCCH format 3. The orthogonal sequences ![](media_svg/image548.svg) [公式≈: w_{n}_{oc}_{(}^{~}_{p}_{,}_{)}_{0}(i)] and ![](media_svg/image549.svg) [公式≈: w_{n}_{oc}_{(}^{~}_{p}_{,}_{)}_{1}(i)] are given by Table 5.4.2A-1. Resources used for transmission of PUCCH format 3 are identified by a resource index ![](media_svg/image550.svg) [公式≈: _{n}_{PUCCH}(3,^{~}p)] from which the quantities ![](media_svg/image551.svg) [公式≈: ^{n}oc,0^{(}^{~}^{p}^{)}] and ![](media_svg/image552.svg) [公式≈: ^{n}oc,1^{(}^{~}^{p}^{)}] are derived according to

![](media_svg/image553.svg) [公式≈: ^{n}_{n}^{oc}_{oc}^{(}(^{~}~^{p}p^{,}_{,}_{1}^{)})^{0}_{=}^{=}√⌡_{⌠}_{⌡}_{∞}^{n}(_{n}^{PUCCH}^{(}3^{3}_{oc}_{(}n^{,}_{~}_{p}^{~}^{p}_{,}oc^{(}_{)}_{0}^{)}^{~}^{p},_{mod}^{)}0)^{mod}mod_{N}_{SF,1}^{N}_{PUCCH}N^{SF,1}^{PUCCH}SF,1^{PUCCH}if_{otherwise}NSF,1^{PUCCH}=5]

Each set of complex-valued symbols shall be cyclically shifted according to

![](media_svg/image554.svg) [公式≈: ^{~}y_{n}^{(}^{~}^{p}^{)}(i)=y_{n}^{(}^{~}^{p}^{)}((i+n_{cs}^{cell}(n_{s},l))modN_{sc}^{RB})]

where ![](media_svg/image555.svg) [公式≈: n_{cs}^{cell}(n_{s},l)] is given by Clause 5.4, ![](media_svg/image556.svg) [公式≈: ^{n}s] is the slot number within a radio frame and ![](media_svg/image557.svg) [公式: l] is the SC-FDMA symbol number within a slot.

The shifted sets of complex-valued symbols shall be transform precoded according to

![](media_svg/image558.svg) [公式≈: _{z}(~p)_{(}_{n}_{∪}_{N}_{sc}RB_{+}_{k}_{k}_{n}_{)}_{=}_{=}_{=}_{0}_{0}_{,...,}_{,...,}1_{P}_{N}_{N}_{N}_{SF,0}_{sc}_{RB}_{PUCCH}1_{sc}_{RB}_{−}_{1}^{N}_{⊆}_{i}^{sc}_{+}^{RB}_{=}_{0}_{N}^{−}^{1}_{SF,1}_{PUCCH}~_{y}_{n}(~p)_{(}_{i}_{)}_{−}_{e}_{1}^{−}^{j}N^{2}^{Π}scRB^{ik}]

where ![](media_svg/image559.svg) [公式: P] is the number of antenna ports used for PUCCH transmission, resulting in a block of complex-valued symbols ![](media_svg/image560.svg) [公式≈: z^{(}^{~}^{p}^{)}(0),...,z^{(}^{~}^{p}^{)}((N_{SF,0}^{PUCCH}+N_{SF,1}^{PUCCH})N_{sc}^{RB}−1)].

Table 5.4.2A-1: The orthogonal sequence ![](media_svg/image561.svg) [公式: w_{n}_{oc}(i)]

| Sequence index ![](media_svg/image562.svg) [公式≈: ^{n}oc] | Orthogonal sequence ![](media_svg/image563.svg) [公式≈: {w_{n}_{oc}(0)λw_{n}_{oc}(N_{SF}^{PUCCH}−1)}] |  |
| --- | --- | --- |
|  | ![](media_svg/image564.svg) [公式≈: _{N}_{SF}PUCCH_{=}_{5}] | ![](media_svg/image565.svg) [公式≈: _{N}_{SF}PUCCH_{=}_{4}] |
| 0 | ![](media_svg/image566.svg) [公式: {11111}] | ![](media_svg/image567.svg) [公式: {+1+1+1+1}] |
| 1 | ![](media_svg/image568.svg) [公式≈: _{{}_{1}_{e}j2Π5_{e}j4Π5_{e}j6Π5_{e}j8Π5_{}}] | ![](media_svg/image569.svg) [公式: {+1−1+1−1}] |
| 2 | ![](media_svg/image570.svg) [公式≈: _{{}_{1}_{e}j4Π5_{e}j8Π5_{e}j2Π5_{e}j6Π5_{}}] | ![](media_svg/image571.svg) [公式: {+1+1−1−1}] |
| 3 | ![](media_svg/image572.svg) [公式≈: _{{}_{1}_{e}j6Π5_{e}j2Π5_{e}j8Π5_{e}j4Π5_{}}] | ![](media_svg/image573.svg) [公式: {+1−1−1+1}] |
| 4 | ![](media_svg/image574.svg) [公式≈: _{{}_{1}_{e}j8Π5_{e}j6Π5_{e}j4Π5_{e}j2Π5_{}}] | - |

### 5.4.2B PUCCH format 4

The block of bits ![](media_svg/image575.svg) [公式: b(0),...,b(M_{bit}−1)] shall be scrambled with a UE-specific scrambling sequence, resulting in a block of scrambled bits ![](media_svg/image576.svg) [公式: b^{~}(0),...,b^{~}(M_{bit}−1)] according to

![](media_svg/image577.svg) [公式: b^{~}(i)=(b(i)+c(i))mod2]

where the scrambling sequence ![](media_svg/image447.svg) [公式: c(i)] is given by clause 7.2. The scrambling sequence generator shall be initialised with ![](media_svg/image578.svg) [公式≈: c_{init}=(_{√}n_{s}2_{∃}+1)∪(2N_{ID}^{cell}+1)∪2^{16}+n_{RNTI}] at the start of each subframe where ![](media_svg/image517.svg) [公式≈: ^{n}RNTI] is the C-RNTI.

The block of scrambled bits ![](media_svg/image536.svg) [公式: b^{~}(0),...,b^{~}(M_{bit}−1)] shall be QPSK modulated as described in Clause 7.1, resulting in a block of complex-valued modulation symbols ![](media_svg/image537.svg) [公式≈: d(0),...,d(M_{symb}−1)] where ![](media_svg/image579.svg) [公式≈: ^{M}symb^{=}^{M}bit^{2}].

The block of complex-valued symbols ![](media_svg/image580.svg) [公式≈: d(0),...,d(M_{symb}−1)] is divided into ![](media_svg/image581.svg) [公式≈: _{N}_{0}PUCCH_{+}_{N}_{1}PUCCH] sets, each corresponding to one SC-FDMA symbol. Transform precoding shall be applied according to

![](media_svg/image582.svg) [公式≈: _{z}(~p)_{(}_{l}_{∪}_{M}_{sc}PUCCH4_{+}_{k}_{k}_{)}_{l}_{=}_{=}_{=}_{0}_{0}_{,...,}_{,...,}_{M}_{sc}_{PUCCH4}_{M}_{N}1_{0}_{PUCCH}_{sc}_{PUCCH4}^{M}_{+}^{sc}^{PUCCH4}_{−}_{⊆}_{i}_{N}_{=}_{1}_{0}_{1}_{PUCCH}^{−}^{1}_{d}_{(}_{l}_{−}_{∪}_{M}_{1}_{sc}PUCCH4_{+}_{i}_{)}_{e}^{−}^{j}Msc^{2}PUCCH4^{Π}^{ik}]

where ![](media_svg/image583.svg) [公式≈: ^{~}p=0], ![](media_svg/image440.svg) [公式≈: _{N}_{0}PUCCH] and ![](media_svg/image441.svg) [公式≈: _{N}_{1}PUCCH] are given by Table 5.4.2C-1 for normal PUCCH format 4 and shortened PUCCH format 4, resulting in a block of complex-valued symbols ![](media_svg/image584.svg) [公式≈: z^{(}^{~}^{p}^{)}(0),...,z^{(}^{~}^{p}^{)}(M_{symb}−1)]. The variable![](media_svg/image585.svg) [公式≈: _{M}_{sc}PUCCH4_{=}_{M}_{RB}PUCCH4_{∪}_{N}_{sc}RB], where ![](media_svg/image439.svg) [公式≈: _{M}_{RB}PUCCH4] represents the bandwidth of the PUCCH format 4 in terms of resource blocks, shall fulfil

![](media_svg/image586.svg) [公式≈: _{M}_{RB}PUCCH4_{=}_{2}Α2_{∪}_{3}Α3_{∪}_{5}Α5_{≥}_{N}_{RB}UL]

where ![](media_svg/image298.svg) [公式: Α_{2},Α_{3},Α_{5}] is a set of non-negative integers.

### 5.4.2C PUCCH format 5

The block of bits ![](media_svg/image575.svg) [公式: b(0),...,b(M_{bit}−1)] shall be scrambled with a UE-specific scrambling sequence, resulting in a block of scrambled bits ![](media_svg/image576.svg) [公式: b^{~}(0),...,b^{~}(M_{bit}−1)] according to

![](media_svg/image577.svg) [公式: b^{~}(i)=(b(i)+c(i))mod2]

where the scrambling sequence ![](media_svg/image447.svg) [公式: c(i)] is given by clause 7.2. The scrambling sequence generator shall be initialised with ![](media_svg/image578.svg) [公式≈: c_{init}=(_{√}n_{s}2_{∃}+1)∪(2N_{ID}^{cell}+1)∪2^{16}+n_{RNTI}] at the start of each subframe where ![](media_svg/image517.svg) [公式≈: ^{n}RNTI] is the C-RNTI.

The block of scrambled bits ![](media_svg/image536.svg) [公式: b^{~}(0),...,b^{~}(M_{bit}−1)] shall be QPSK modulated as described in Clause 7.1, resulting in a block of complex-valued modulation symbols ![](media_svg/image537.svg) [公式≈: d(0),...,d(M_{symb}−1)] where ![](media_svg/image579.svg) [公式≈: ^{M}symb^{=}^{M}bit^{2}].

The complex-valued symbols ![](media_svg/image587.svg) [公式≈: d(0),...,d(M_{symb}−1)] shall be divided into ![](media_svg/image588.svg) [公式≈: _{N}_{0}PUCCH_{+}_{N}_{1}PUCCH] sets, each corresponding to one SC-FDMA symbol. Block-wise spreading shall be applied according to

![](media_svg/image589.svg) [公式≈: y_{n}(i_{n}_{i})=_{=}_{=}_{0}_{0}w_{,...,}_{,}_{1}_{n}_{oc}_{,...,}(_{N}i)_{N}_{0}∪_{PUCCH}d_{sc}_{RB}(imod_{−}_{1}_{+}_{N}N_{1}_{PUCCH}_{sc}^{RB}N_{SF}^{PUCCH}_{−}_{1}+n∪N_{sc}^{RB}N_{SF}^{PUCCH})]

where ![](media_svg/image590.svg) [公式≈: _{N}_{SF}PUCCH_{=}_{2}], ![](media_svg/image440.svg) [公式≈: _{N}_{0}PUCCH] and ![](media_svg/image441.svg) [公式≈: _{N}_{1}PUCCH] are given by Table 5.4.2C-1 for normal PUCCH format 5 and shortened PUCCH format 5, and ![](media_svg/image591.svg) [公式: w_{n}_{oc}(i)] is given by Table 5.4.2C-2 with ![](media_svg/image592.svg) [公式≈: ^{n}oc] provided by higher layers.

The block-wise spread complex-valued symbols shall be transform precoded according to

![](media_svg/image593.svg) [公式≈: z^{(}^{~}^{p}^{)}(n∪N_{sc}^{RB}+k_{k}_{n})=_{=}_{=}_{0}_{0}_{,...,}_{,...,}_{N}^{1}_{sc}_{RB}_{N}_{N}_{sc}_{0}_{RB}_{PUCCH}^{N}_{⊆}_{i}^{sc}^{RB}_{=}_{−}_{0}^{−}_{1}^{1}y_{+}_{n}_{N}(i_{1})_{PUCCH}e^{−}^{j}^{N}^{2}^{Π}^{sc}^{RB}^{ik}_{−}_{1}]

where ![](media_svg/image583.svg) [公式≈: ^{~}p=0], resulting in a block of complex-valued symbols ![](media_svg/image594.svg) [公式≈: z^{(}^{~}^{p}^{)}(0),...,z^{(}^{~}^{p}^{)}((N_{0}^{PUCCH}+N_{1}^{PUCCH})N_{sc}^{RB}−1)].

Table 5.4.2C-1: The quantities ![](media_svg/image440.svg) [公式≈: _{N}_{0}PUCCH] and ![](media_svg/image441.svg) [公式≈: _{N}_{1}PUCCH]

| PUCCH format type | Normal cyclic prefix |  | Extended cyclic prefix |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Normal PUCCH format | 6 | 6 | 5 | 5 |
| Shortened PUCCH format | 6 | 5 | 5 | 4 |

Table 5.4.2C-2: Orthogonal sequences ![](media_svg/image597.svg) [公式: w_{n}_{oc}(i)]

| ![](media_svg/image592.svg) [公式≈: ^{n}oc] | Orthogonal sequences ![](media_svg/image598.svg) [公式≈: {w_{n}_{CDM}(0)λw_{n}_{CDM}(N_{sc}^{RB}−1)}] |
| --- | --- |
| 0 | ![](media_svg/image599.svg) [公式: {+1+1+1+1+1+1+1+1+1+1+1+1}] |
| 1 | ![](media_svg/image600.svg) [公式: {+1+1+1+1+1+1−1−1−1−1−1−1}] |

### 5.4.3 Mapping to physical resources

The block of complex-valued symbols ![](media_svg/image601.svg) [公式≈: z^{(}^{~}^{p}^{)}(i)] shall be multiplied with the amplitude scaling factor ![](media_svg/image602.svg) [公式≈: ^{Β}PUCCH] in order to conform to the transmit power ![](media_svg/image603.svg) [公式≈: ^{P}PUCCH] specified in Clause 5.1.2.1 in TS36.213[4], and mapped in sequence starting with ![](media_svg/image604.svg) [公式≈: z^{(}^{~}^{p}^{)}(0)] to resource elements. PUCCH uses one or more resource block in each of the two slots in a subframe. Within the physical resource block(s) used for transmission, the mapping of ![](media_svg/image605.svg) [公式≈: z^{(}^{~}^{p}^{)}(i)] to resource elements ![](media_svg/image396.svg) [公式: (k,l)] on antenna port ![](media_svg/image606.svg) [公式: p] and not used for transmission of reference signals shall be in increasing order of first ![](media_svg/image607.svg) [公式: k], then ![](media_svg/image398.svg) [公式: l] and finally the slot number, starting with the first slot in the subframe. The relation between the index ![](media_svg/image395.svg) [公式≈: ^{~}p] and the antenna port number ![](media_svg/image394.svg) [公式: p] is given by Table 5.2.1-1.

For non-BL/CE UEs, except for PUCCH format 4, the physical resource blocks to be used for transmission of PUCCH in slot ![](media_svg/image126.svg) [公式≈: ^{n}s] are given by

![](media_svg/image608.svg) [公式≈: ^{n}^{PRB}^{=}^{√}^{⌡}^{⌡}^{⌠}^{⌡}_{⌡}_{∞}^{⋅}^{⋅}^{√}N^{m}^{2}_{RB}^{UL}^{∂}^{∂}^{∃}−1−^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}^{if}if^{(}(^{m}m^{+}+^{n}n^{s}_{s}^{mod}mod^{2}2^{)})^{mod}mod^{2}2^{=}=1^{0}]

For BL/CE UEs, PUCCH is transmitted with ![](media_svg/image609.svg) [公式≈: _{N}_{rep}PUCCH_{÷}_{1}] repetitions.

- The BL/CE UE is not expected to transmit with $ N_{rep}^{PUCCH}>1 $ when ce-PDSCH-14HARQ-Config is configured.

The PUCCH transmission spans ![](media_svg/image610.svg) [公式≈: _{N}_{abs}PUCCH_{÷}_{N}_{rep}PUCCH] consecutive subframes, including subframes that are not BL/CE UL subframes where the UE postpones the PUCCH transmission if ![](media_svg/image611.svg) [公式≈: _{N}_{rep}PUCCH_{>}_{1}]. If the BL/CE UE is configured with ce-HARQ-AckDelay-r17 indicating Alt-2e, the UE does not postpone the PUCCH transmission.

- The quantity ![](media_svg/image612.svg) [公式≈: _{N}_{rep}PUCCH] is given

- by the higher layer parameter pucch-NumRepetitionCE-Format1 for PUCCH format 1/1a and pucch-NumRepetitionCE-Format2 for PUCCH format 2/2a/2b, if configured. Otherwise

- by the higher-layer parameter pucch-NumRepetitionCE-Msg4-Level0-r13, pucch-NumRepetitionCE-Msg4-Level1-r13, pucch-NumRepetitionCE-Msg4-Level2-r13 or pucch-NumRepetitionCE-Msg4-Level3-r13.

- If uplink resource reservation is enabled for the UE as specified in [9], then in case of PUCCH transmission with ![](media_svg/image611.svg) [公式≈: _{N}_{rep}PUCCH_{>}_{1}] associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PUCCH transmission without a corresponding MPDCCH,

- In a subframe that is fully reserved as defined in clause 8.0 in [4], the PUCCH transmission is postponed until the next BL/CE uplink subframe that is not fully reserved.

- In a subframe that is partially reserved, the reserved SC-FDMA symbols shall be counted in the PUCCH mapping but not used for transmission of the PUCCH.

The physical resource blocks to be used for transmission of PUCCH in subframe ![](media_svg/image613.svg) [公式: i] within the ![](media_svg/image71.svg) [公式≈: _{N}_{abs}PUCCH] consecutive subframes are given by

![](media_svg/image614.svg) [公式≈: _{i}^{n}m_{j}_{0}^{PRB}±_{=}_{≥}(j_{⋅}_{⋅}_{⋅}_{√}_{i})^{(}_{N}_{≥}^{i}=^{)}_{NB}_{ch,}_{i}^{=}^{√}^{⌡}⌠_{⌡}_{∞}_{0}_{i}^{m}m_{m}_{UL}_{+}^{√}^{⌠}^{∞}^{m}^{N}+_{−}_{N}_{∂}_{∂}_{∂}_{∃}^{±}_{1}1^{RB}^{UL}^{(}_{abs}_{PUCCH}^{j}^{)}^{if}if_{if}^{−}^{2}^{1}^{j}j_{j}^{−}^{mod}mod_{mod}_{−}^{√}_{1}^{m}^{±}^{(}^{2}2_{2}^{j}^{)}^{=}=_{=}^{2}1_{1}^{0}^{∃}and_{and}^{if}^{if}m_{m}^{m}^{m}mod_{mod}^{±}^{±}^{(}^{(}^{j}^{j}^{)}^{)}^{mod}^{mod}2_{2}=_{=}_{1}0^{2}^{2}^{=}^{=}^{1}^{0}]

where ![](media_svg/image263.svg) [公式≈: ^{i}0] is the absolute subframe number of the first uplink subframe intended for PUCCH.

The variable ![](media_svg/image615.svg) [公式: m] depends on the PUCCH format.

- Formats 1, 1a and 1b:

![](media_svg/image616.svg) [公式≈: _{c}m_{=}=_{√}_{⌠}_{∞}^{√}^{⌡}⌠_{⌡}_{∞}_{3}_{2}⋅_{⋅}_{⋅}_{√}^{N}n^{RB}^{(2)}PUCCH^{(1,}_{extended}_{normal}^{~}^{p}^{)}_{c}_{∪}_{N}−_{sc}_{cyclic}_{RB}c_{cyclic}∪N_{δ}cs^{(1)}_{PUCCH}_{shift}_{prefix}_{prefix}δ^{PUCCH}shift∂_{∂}_{∂}_{∃}_{+}_{N}_{RB}(2)_{+}⊥_{⋅}_{⋅}_{⋅}N_{8}cs^{(1)}∀_{∂}_{∂}_{∂}^{if}_{otherwise}^{n}^{PUCCH}^{(1,}^{~}^{p}^{)}^{<}^{c}^{∪}^{N}^{cs}^{(1)}^{δ}^{PUCCH}^{shift}]

- Formats 2, 2a and 2b:

![](media_svg/image617.svg) [公式≈: m=√nPUCCH^{(2,}^{~}^{p}^{)}Nsc^{RB}∃]

- Format 3:

![](media_svg/image618.svg) [公式≈: ^{m}^{=}√^{n}PUCCH^{(3,}^{~}^{p}^{)}^{N}SF,0^{PUCCH}∃]

- Format 5 (non-BL/CE UEs only):

![](media_svg/image619.svg) [公式≈: ^{m}^{=}^{n}PUCCH^{(}^{5}^{)}]

For non-BL/CE UEs, for PUCCH format 4, the physical resource blocks to be used for transmission of PUCCH in slot ![](media_svg/image126.svg) [公式≈: ^{n}s] are given by

![](media_svg/image620.svg) [公式≈: ^{n}^{PRB}m^{=}=n^{√}^{⌠}^{∞}_{PUCCH}^{(4)}^{m}^{N}^{RB}^{UL}^{−},n^{1}_{PUCCH}^{(4)}^{−}^{m}+^{if}^{if}1,...,^{n}^{n}^{s}^{s}n^{mod}^{mod}_{PUCCH}^{(4)}^{2}^{2}^{=}^{=}+^{1}^{0}M_{RB}^{PUCCH4}−1]

where ![](media_svg/image439.svg) [公式≈: _{M}_{RB}PUCCH4] is obtained from [4].

Mapping of modulation symbols for the physical uplink control channel for PUCCH formats 1 – 3 is illustrated in Figure 5.4.3-1.

In case of simultaneous transmission of sounding reference signal and PUCCH format 1, 1a, 1b, 3, 4 or 5 when there is one serving cell configured, the shortened PUCCH format shall be used where the last SC-FDMA symbol in the second slot of a subframe shall be left empty.

In case of guard period for narrowband or wideband retuning for BL/CE UEs, if an SC-FDMA symbol is left empty due to guard period, the SC-FDMA symbol shall be counted in the PUCCH mapping but not used for transmission of the PUCCH. The SC-FDMA symbol affected by the guard period can be the first SC-FDMA symbol in the first slot of a subframe and/or the last SC-FDMA symbol in the second slot of a subframe.

For BL/CE UEs communicating over NTN, for PUCCH transmission, for frame structure type 1, after a transmission duration of $ N_{segment}^{precompensation}$ time units (which may include subframes that are not BL/CE UL subframes), a transmission gap of $ N_{gap}^{precompensation}$ time units shall be counted for the PUCCH resource mapping but not used for transmission of the PUCCH, according to the single UE capability ntn-SegmentedPrecompensationGaps-r17, as specified in 3GPP TS 36.331 [9]. The quantity $ N_{segment}^{precompensation}$ is provided by higher layers, and the quantity $ N_{gap}^{precompensation}$ is configured by higher layers based on the UE capability, if signalled.

![](media/image621.emf)

Figure 5.4.3-1: Mapping to physical resource blocks for PUCCH formats 1 – 3 for non-BL/CE UEs.



## 5.4A Short Physical Uplink Control Channel

### 5.4A.1 General

The short physical uplink control channel, SPUCCH, carries uplink control information. Simultaneous transmission of SPUCCH and PUSCH from the same UE where both SPUCCH and PUSCH is using either slot or subslot transmission is supported if enabled by higher layers (see simultaneousPUCCH-PUSCH in TS 36.331 [9]). For frame structure type 2 and in UpPTS, transmission of SPUCCH is not supported.

SPUCCH supports multiple formats as shown in Table 5.4A-1 and Table 5.4A-2 with different number of bits carried by each SPUCCH.

Table 5.4A-1: SPUCCH formats for slot transmission

| SPUCCH format | Modulation scheme | Number of bits per slot, ![](media_svg/image622.svg) [公式≈: ^{M}bit] |
| --- | --- | --- |
| 1 | N/A | N/A |
| 1a | BPSK | 1 |
| 1b | QPSK | 2 |
| 3 | QPSK | 24 |
| 4 | QPSK | ![](media_svg/image623.svg) [公式≈: _{M}_{RB}SPUCCH4_{∪}_{N}_{sc}RB_{∪}_{N}_{slot}SPUCCH_{∪}_{2}] |

Table 5.4A-2: SPUCCH formats for subslot transmission

| SPUCCH format | Modulation scheme | Number of bits per subslot, ![](media_svg/image624.svg) [公式≈: ^{M}bit] |
| --- | --- | --- |
| 1 | N/A | N/A |
| 1a | N/A | 1 |
| 1b | N/A | 2 |
| 4 | QPSK | ![](media_svg/image625.svg) [公式≈: _{M}_{RB}SPUCCH4_{∪}_{N}_{sc}RB_{∪}_{N}_{subslot}SPUCCH_{∪}_{2}] |

The quantity ![](media_svg/image626.svg) [公式≈: _{M}_{RB}SPUCCH4] represents the bandwidth of the SPUCCH format 4 as defined by clause 5.4A.4.1, and ![](media_svg/image627.svg) [公式≈: _{N}_{slot}SPUCCH] and ![](media_svg/image628.svg) [公式≈: ^{N}subslot^{SPUCCH}] are defined in Table 5.4A.4.1-1 and Table 5.4A.4.2-1, respectively.

SPUCCH formats 1/1a/1b use a cyclic shift, ![](media_svg/image629.svg) [公式≈: n_{cs}^{cell}(n_{s},l)], which varies with the symbol number ![](media_svg/image398.svg) [公式: l] and the slot number ![](media_svg/image630.svg) [公式≈: ^{n}s] as described in clause 5.4.

### 5.4A.2 SPUCCH formats 1,1a,1b

#### 5.4A.2.1 Slot-SPUCCH

Slot-SPUCCH format 1, 1a, 1b can be configured by higher layers to either have frequency hopping enabled or disabled (see n1SlotSPUCCH-FH-AN-List and n1SlotSPUCCH-NoFH-AN-List in TS 36.331 [9]).

In case slot-SPUCCH format 1, 1a, 1b and frequency hopping is enabled, the scrambled and block-wise spread complex-valued symbols ![](media_svg/image631.svg) [公式≈: _{z}(^{~}p)] are generated as described in clause 5.4.1 for PUCCH format 1/1a/1b where ![](media_svg/image632.svg) [公式: Sn()1_{s}=], ![](media_svg/image633.svg) [公式: m±=0] and![](media_svg/image634.svg) [公式: w(m)=+1].

In case slot-SPUCCH format 1, 1a, 1b and frequency hopping is disabled, the scrambled and block-wise spread complex-valued symbols ![](media_svg/image631.svg) [公式≈: _{z}(^{~}p)] are generated as described in clause 5.4.1 for PUCCH format 1/1a/1b where ![](media_svg/image633.svg) [公式: m±=0].

Irrespective of frequency hopping being enabled or disabled, ![](media_svg/image635.svg) [公式≈: _{N}_{SF}PUCCH] is applied as described in clause 5.4.1 for the slot in which the slot-SPUCCH is transmitted in, i.e. either in the first or the second slot of the subframe.

Resources used for transmission of slot-SPUCCH format 1, 1a and 1b are identified by a resource index ![](media_svg/image636.svg) [公式≈: ^{n}SPUCCH^{(1,}^{~}^{p}^{)}] from which the cyclic shift ![](media_svg/image483.svg) [公式: Α~_{p}(n_{s},l)] is derived:

![](media_svg/image526.svg) [公式≈: Α~_{p}(n_{s},l)=2Π∪n_{cs}^{(}^{~}^{p}^{)}(n_{s},l)N_{sc}^{RB}],

In case frequency hopping is enabled, the cyclic shift is determined as described in clause 5.4.2, assuming the condition ![](media_svg/image637.svg) [公式≈: _{n}_{PUCCH}(2,^{~}p)_{<}_{N}_{sc}RB_{N}_{RB}(2)] is fulfilled.

In case frequency hopping is disabled, the resource index ![](media_svg/image636.svg) [公式≈: ^{n}SPUCCH^{(1,}^{~}^{p}^{)}] also indicates the orthogonal sequence index ![](media_svg/image482.svg) [公式≈: n_{oc}^{(}^{~}^{p}^{)}(n_{s})]. Both the cyclic shift and the orthogonal sequence index is in this case determined as described in clause 5.4.1.

#### 5.4A.2.2 Subslot-SPUCCH

For subslot-SPUCCH formats 1a and 1b, one or two bits are communicated by SPUCCH resource selection. The resource set available for selection are configured by higher layers (see n1SubslotSPUCCH-AN-List and sr-SubslotSPUCCH-ResourceList in TS 36.331 [9]). For subslot-SPUCCH format 1, information is carried by the presence/absence of transmission of subslot-SPUCCH from the UE.

The sequence ![](media_svg/image638.svg) [公式≈: _{y}(^{~}p,Δ)_{(}_{n}_{)}] is generated as described in clause 5.4.1, assuming ![](media_svg/image460.svg) [公式: d(0)=1].

The block of complex-valued symbols ![](media_svg/image472.svg) [公式≈: y^{(}^{~}^{p}^{)}(0),...,y^{(}^{~}^{p}^{)}(N_{seq}^{PUCCH}−1)] shall be scrambled by ![](media_svg/image639.svg) [公式: Sn()1_{s}=] as described in clause 5.4.1 assuming ![](media_svg/image640.svg) [公式: w_{n}_{oc}(~p)(i)=1], ![](media_svg/image641.svg) [公式: m&apos;=0], and with ![](media_svg/image642.svg) [公式≈: _{N}_{SF}PUCCH]replaced by ![](media_svg/image643.svg) [公式≈: _{N}_{SF}SPUCCH], defined in Table 5.4A.2.2-1.

Table 5.4A.2.2-1: The quantity ![](media_svg/image644.svg) [公式≈: _{N}_{SF}SPUCCH] for subslot-SPUCCH formats 1a and 1b

| SPUCCH format type | Subslot number in subframe | ![](media_svg/image645.svg) [公式≈: _{N}_{SF}SPUCCH] |
| --- | --- | --- |
| Normal SPUCCH format | 1,2,3,4 | 2 |
| Normal SPUCCH format | 0,5 | 3 |
| Shortened SPUCCH format | 5 | 2 |

Resources used for transmission of SPUCCH format 1, 1a and 1b are identified by a resource index ![](media_svg/image646.svg) [公式≈: ^{n}SPUCCH,^{(1,}^{~}^{p}^{)}i] from which the cyclic shift ![](media_svg/image483.svg) [公式: Α~_{p}(n_{s},l)] is determined, as described in clause 5.4.2, assuming the condition ![](media_svg/image647.svg) [公式≈: _{n}_{PUCCH}(2,^{~}p)_{<}_{N}_{sc}RB_{N}_{RB}(2)] is fulfilled.The resource set for subslot-SPUCCH format 1/1a/1b is configured by higher layers (see n1SubslotSPUCCH-AN-List in TS 36.331 [9]):

- subslot-SPUCCH format 1: ![](media_svg/image648.svg) [公式≈: ^{n}SPUCCH,^{(1,}^{~}^{p}^{)}i^{,}^{i}^{⎰}^{{}^{0}^{}}]

- subslot-SPUCCH format 1a: ![](media_svg/image649.svg) [公式≈: n_{SPUCCH,}^{(1,}^{~}^{p}^{)}_{i},i⎰{0,1}]

- subslot-SPUCCH format 1b: ![](media_svg/image650.svg) [公式≈: n_{SPUCCH,}^{(1,}^{~}^{p}^{)}_{i},i⎰{0,1,2,3}]

Each resource indicates (a) bit state(s) as defined by Table 5.4A.2.2-2.

Table 5.4A.2.2-2: Subslot-SPUCCH resource for formats 1a and 1b

| PUCCH format | ![](media_svg/image495.svg) [公式: b(0),...,b(M_{bit}−1)] | ![](media_svg/image651.svg) [公式≈: ^{n}SPUCCH,^{(1,}^{~}^{p}^{)}i] |
| --- | --- | --- |
| 1 | - | ![](media_svg/image652.svg) [公式≈: ^{n}SPUCCH,0^{(1,}^{~}^{p}^{)}] |
| 1a | 0 | ![](media_svg/image653.svg) [公式≈: ^{n}SPUCCH,0^{(1,}^{~}^{p}^{)}] |
|  | 1 | ![](media_svg/image654.svg) [公式≈: ^{n}SPUCCH,1^{(1,}^{~}^{p}^{)}] |
| 1b | 00 | ![](media_svg/image653.svg) [公式≈: ^{n}SPUCCH,0^{(1,}^{~}^{p}^{)}] |
|  | 10 | ![](media_svg/image654.svg) [公式≈: ^{n}SPUCCH,1^{(1,}^{~}^{p}^{)}] |
|  | 01 | ![](media_svg/image655.svg) [公式≈: ^{n}SPUCCH,2^{(1,}^{~}^{p}^{)}] |
|  | 11 | ![](media_svg/image656.svg) [公式≈: ^{n}SPUCCH,3^{(1,}^{~}^{p}^{)}] |

### 5.4A.3 SPUCCH format 3

#### 5.4A.3.1 Slot-SPUCCH

The complex-valued modulation symbols ![](media_svg/image537.svg) [公式≈: d(0),...,d(M_{symb}−1)] shall be generated as described in clause 5.4.2A.

Depending on if the slot-SPUCCH is transmitted in the first or the second slot of the subframe, different block-wise spreading with the orthogonal sequences ![](media_svg/image540.svg) [公式≈: w_{n}_{oc}_{(}^{~}_{p}_{,}_{)}_{0}(i)] or ![](media_svg/image541.svg) [公式≈: w_{n}_{oc}_{(}^{~}_{p}_{,}_{)}_{1}(i)] is applied. Each spreading results in ![](media_svg/image657.svg) [公式≈: _{N}_{SF}SPUCCH] sets of ![](media_svg/image543.svg) [公式≈: _{N}_{sc}RB] values each according to:

![](media_svg/image658.svg) [公式≈: _{y}_{n}(~p)_{(}_{i}_{n}_{)}_{i}_{=}_{=}_{=}_{0}_{0}^{√}⌡_{⌠}_{⌡}_{∞}_{,...,}_{,}w_{w}_{1}_{,...,}n_{n}oc_{oc}(_{(}_{N}~_{~}p_{p},_{,}_{1})_{)}0_{N}_{SF}_{(}_{SPUCCH}(_{n}n_{sc}_{RB}_{)})_{∪}∪_{e}e_{−}_{j}^{j}_{1}_{Π}^{Π}_{−}_{√}^{√}_{n}^{n}_{cs}_{1}_{cell}^{cs}^{cell}_{(}^{(}_{n}^{n}_{s}^{s}_{,}^{,}_{l}^{l}_{)}^{)}_{64}^{64}_{∃}^{∃}_{2}^{2}_{∪}∪_{d}d_{(}(_{i}i_{)})if_{otherwise}nsmod2=0]

where

- ![](media_svg/image659.svg) [公式≈: _{N}_{SF}SPUCCH_{=}_{N}_{SF,0}PUCCH] (see clause 5.4.2A) if transmitted in the first slot, and ![](media_svg/image660.svg) [公式≈: _{N}_{SF}SPUCCH_{=}_{N}_{SF,1}PUCCH](see clause 5.4.2A), if transmitted in the second slot.

- The orthogonal sequences ![](media_svg/image548.svg) [公式≈: w_{n}_{oc}_{(}^{~}_{p}_{,}_{)}_{0}(i)] and ![](media_svg/image549.svg) [公式≈: w_{n}_{oc}_{(}^{~}_{p}_{,}_{)}_{1}(i)] are given by Table 5.4.2A-1

Resources used for transmission of SPUCCH format 3 are identified by a resource index ![](media_svg/image661.svg) [公式≈: ^{n}SPUCCH^{(}^{3}^{,}^{~}^{p}^{)}] from which the quantities ![](media_svg/image551.svg) [公式≈: ^{n}oc,0^{(}^{~}^{p}^{)}] and ![](media_svg/image552.svg) [公式≈: ^{n}oc,1^{(}^{~}^{p}^{)}] are derived according to clause 5.4A.3 by replacing ![](media_svg/image662.svg) [公式≈: _{n}_{PUCCH}(3,^{~}p)] with ![](media_svg/image661.svg) [公式≈: ^{n}SPUCCH^{(}^{3}^{,}^{~}^{p}^{)}].

Each set of complex-valued symbols shall be cyclically shifted and transform precoded according to clause 5.4.2A with ![](media_svg/image663.svg) [公式≈: _{N}_{SF,0}PUCCH_{+}_{N}_{SF,1}PUCCH] replaced by ![](media_svg/image664.svg) [公式≈: _{N}_{SF}SPUCCH] in the transform precoding.

### 5.4A.4 SPUCCH format 4

#### 5.4A.4.1 Slot-SPUCCH

The block of bits ![](media_svg/image665.svg) [公式: b(0),...,b(M_{bit}−1)] shall be scrambled according to clause 5.4.2B.

The block of scrambled bits ![](media_svg/image666.svg) [公式: b^{~}(0),...,b^{~}(M_{bit}−1)] shall be QPSK modulated as described in Clause 7.1, resulting in a block of complex-valued modulation symbols ![](media_svg/image667.svg) [公式≈: d(0),...,d(M_{symb}−1)] where ![](media_svg/image668.svg) [公式≈: ^{M}symb^{=}^{M}bit^{2}].

The block of complex-valued symbols ![](media_svg/image669.svg) [公式≈: d(0),...,d(M_{symb}−1)] is divided into ![](media_svg/image670.svg) [公式≈: _{N}_{slot}SPUCCH] (defined in Table 5.4A.4.1-1) sets, each corresponding to one SC-FDMA symbol. Transform precoding shall be applied according to clause 5.4.2B replacing ![](media_svg/image671.svg) [公式≈: _{M}_{sc}PUCCH4] with ![](media_svg/image672.svg) [公式≈: _{M}_{sc}SPUCCH4] and replacing ![](media_svg/image673.svg) [公式≈: _{N}_{0}PUCCH_{+}_{N}_{1}PUCCH] with ![](media_svg/image674.svg) [公式≈: _{N}_{slot}SPUCCH].

The variable![](media_svg/image675.svg) [公式≈: _{M}_{sc}SPUCCH4_{=}_{M}_{RB}SPUCCH4_{∪}_{N}_{sc}RB], where ![](media_svg/image676.svg) [公式≈: _{M}_{RB}SPUCCH4] represents the bandwidth of the SPUCCH format 4 in terms of resource blocks in the frequency domain, and is determined by higher layer signalling (n4numberOfPRB-r15, see TS 36.213 [4, Table 10.1.1-2] and TS 36.331 [9]), and shall fulfil

![](media_svg/image677.svg) [公式≈: _{M}_{RB}SPUCCH4_{=}_{2}Α2_{∪}_{3}Α3_{∪}_{5}Α5_{≥}_{N}_{RB}UL],

where, ![](media_svg/image298.svg) [公式: Α_{2},Α_{3},Α_{5}] is a set of non-negative integers.

Table 5.4A.4.1-1: The quantity ![](media_svg/image627.svg) [公式≈: _{N}_{slot}SPUCCH] .

| SPUCCH format type | ![](media_svg/image678.svg) [公式≈: _{N}_{slot}SPUCCH] |
| --- | --- |
| Normal SPUCCH format | 5 |
| Shortened SPUCCH format | 4 |

#### 5.4A.4.2 Subslot-SPUCCH

For subslot-SPUCCH the procedure of slot-SPUCCH in clause 5.4A.4.1 is followed except that:

- the block of complex-valued symbols ![](media_svg/image669.svg) [公式≈: d(0),...,d(M_{symb}−1)] is divided into ![](media_svg/image679.svg) [公式≈: ^{N}subslot^{SPUCCH}] (defined in Table 5.4A.4.2-1) sets, instead of ![](media_svg/image680.svg) [公式≈: _{N}_{slot}SPUCCH] sets, and,

- ![](media_svg/image681.svg) [公式≈: _{N}_{slot}SPUCCH] is replaced by ![](media_svg/image682.svg) [公式≈: ^{N}subslot^{SPUCCH}], in the transform precoding.

Table 5.4A.4.2-1: The quantity ![](media_svg/image683.svg) [公式≈: ^{N}subslot^{SPUCCH}] .

| SPUCCH format type | Subslot number in subframe | ![](media_svg/image684.svg) [公式≈: ^{N}subslot^{SPUCCH}] |
| --- | --- | --- |
| Normal SPUCCH format | 1,2,3,4 | 1 |
| Normal SPUCCH format | 0,5 | 2 |
| Shortened SPUCCH format | 5 | 1 |

### 5.4A.5 Mapping to physical resources

The block of complex-valued symbols ![](media_svg/image685.svg) [公式≈: z^{(}^{~}^{p}^{)}(i)] shall be multiplied with the amplitude scaling factor ![](media_svg/image686.svg) [公式≈: ^{Β}SPUCCH] in order to conform to the transmit power ![](media_svg/image687.svg) [公式≈: ^{P}SPUCCH] specified in Clause 5.1.2.1 of TS36.213 [4], and mapped in sequence starting with ![](media_svg/image688.svg) [公式≈: z^{(}^{~}^{p}^{)}(0)] to resource elements.

SPUCCH uses one or more resource block in the frequency domain and is mapped to either a slot or a subslot in the time domain. Within the physical resource block(s) used for transmission, the mapping of ![](media_svg/image605.svg) [公式≈: z^{(}^{~}^{p}^{)}(i)] to resource elements ![](media_svg/image396.svg) [公式: (k,l)] on antenna port ![](media_svg/image606.svg) [公式: p] and not used for transmission of reference signals shall be in increasing order of first ![](media_svg/image607.svg) [公式: k], then ![](media_svg/image398.svg) [公式: l].

The starting symbol ![](media_svg/image689.svg) [公式: l]for each subslot number is provided by Table 5.4A.4.5-1 for subslot-SPUCCH.

For slot-SPUCCH the starting symbol is ![](media_svg/image690.svg) [公式: l=0]for the slot the SPUCCH is transmitted in.

Table 5.4A.5-1: Starting symbol for subslot-SPUCCH mapping

|  | Subslot number |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 |
| Format 1/1a/1b | 0 | 3 | 5 | 0 | 2 | 4 |
| Format 4 | 1 | 4 | 6 | 1 | 3 | 5 |

The relation between the index ![](media_svg/image395.svg) [公式≈: ^{~}p] and the antenna port number ![](media_svg/image394.svg) [公式: p] is given by Table 5.2.1-1.

The physical resource blocks (![](media_svg/image691.svg) [公式≈: ^{n}PRB]) within which the transmission of SPUCCH is carried out in slot ![](media_svg/image126.svg) [公式≈: ^{n}s] depends on the SPUCCH format and whether frequency hopping is enabled or not.

In case of slot-SPUCCH format 1, 1a, 1b and frequency hopping disabled, the PRB used is determined as described in clause 5.4.3 for PUCCH format 1, 1a, 1b.

In case of slot-SPUCCH format 3, the PRB used is given by

For the other SPUCCH formats, it is determined by Table 5.4A.5-2, Table 5.4A.5-3 and Table 5.4A.5-4.

Table 5.4A.5-2: ![](media_svg/image692.svg) [公式≈: ^{n}PRB] for slot-SPUCCH format 1, 1a, 1b with frequency hopping enabled

| Slot number | Slot-SPUCCH format |
| --- | --- |
|  | Format 1/1a/1b with frequency hopping enabled |
| ![](media_svg/image693.svg) [公式: n_{s}mod2=0] | ![](media_svg/image694.svg) [公式≈: N_{RB}^{UL}^{⋅}^{⋅}^{√}−^{m}^{2}1^{∂}^{∂}^{∃}−^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}for^{for}l^{l}=^{=}3^{0},4^{,}^{1},5^{or }or ^{2}6]![](media_svg/image695.svg) [公式: for(m+n_{s}mod2)mod2=0]![](media_svg/image696.svg) [公式≈: N_{RB}^{UL}−_{⋅}_{⋅}_{√}_{m}1_{2}−_{∂}_{∂}_{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}_{for }for _{l}l_{=}=_{3}0_{,}_{4},1_{,}_{5}or _{or }2_{6}]![](media_svg/image697.svg) [公式: for(m+n_{s}mod2)mod2=1] |
| ![](media_svg/image698.svg) [公式: n_{s}mod2=1] | ![](media_svg/image699.svg) [公式≈: N_{RB}^{UL}−^{⋅}^{⋅}^{√}^{m}^{2}1−^{∂}^{∂}^{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}^{for}for^{l}l^{=}=^{0}4^{,}^{1},^{,}5^{2}or ^{or }6^{3}]![](media_svg/image695.svg) [公式: for(m+n_{s}mod2)mod2=0]![](media_svg/image700.svg) [公式≈: N_{RB}^{UL}−_{⋅}_{⋅}_{√}_{m}_{2}1−_{∂}_{∂}_{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}for _{for }l_{l}=_{=}0_{4},1_{,},_{5}2_{or }or _{6}3]![](media_svg/image697.svg) [公式: for(m+n_{s}mod2)mod2=1] |

Table 5.4A.5-3: ![](media_svg/image692.svg) [公式≈: ^{n}PRB] for slot-SPUCCH format 4

| Slot number | Slot-SPUCCH format |
| --- | --- |
|  | Format 4 |
| ![](media_svg/image701.svg) [公式: n_{s}mod2=0] | ![](media_svg/image702.svg) [公式≈: N_{RB}^{UL}^{m}−1−mfor ^{for }l^{l}=^{=}3^{0},^{,}^{1}4,^{or }5or ^{2}6] |
| ![](media_svg/image698.svg) [公式: n_{s}mod2=1] | ![](media_svg/image703.svg) [公式≈: N_{RB}^{UL}^{m}−1−m^{for }for ^{l}l^{=}=^{4}0^{,},1^{5},2^{or }or ^{6}3] |

Table 5.4A.5-4: ![](media_svg/image692.svg) [公式≈: ^{n}PRB] for subslot-SPUCCH format 1, 1a, 1b, 4

| Subslot number | SPUCCH format |  |
| --- | --- | --- |
|  | Format 1/1a/1b | Format 4 |
| 0 | ![](media_svg/image704.svg) [公式≈: N_{RB}^{UL}^{⋅}^{⋅}^{√}−^{m}^{2}1−^{∂}^{∂}^{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}for ^{for }l^{l}=^{=}1^{0},2]![](media_svg/image695.svg) [公式: for(m+n_{s}mod2)mod2=0]![](media_svg/image705.svg) [公式≈: N_{RB}^{UL}_{⋅}_{⋅}_{√}−_{m}_{2}1−_{∂}_{∂}_{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}_{for }for _{l}l_{=}=_{1}0_{,}_{2}]![](media_svg/image697.svg) [公式: for(m+n_{s}mod2)mod2=1] | ![](media_svg/image706.svg) [公式: mfor l=1,2] |
| 1 | ![](media_svg/image707.svg) [公式≈: N_{RB}^{UL}^{⋅}^{⋅}^{√}−^{m}^{2}1−^{∂}^{∂}^{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}^{for }for ^{l}l^{=}=^{4}3]![](media_svg/image708.svg) [公式: for(m+n_{s}mod2)mod2=0]![](media_svg/image709.svg) [公式≈: N_{RB}^{UL}_{⋅}_{⋅}_{√}−_{m}_{2}1−_{∂}_{∂}_{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}for _{for }l_{l}=_{=}4_{3}]![](media_svg/image710.svg) [公式: for(m+n_{s}mod2)mod2=1] | ![](media_svg/image711.svg) [公式: mfor l=4] |
| 2 | ![](media_svg/image712.svg) [公式≈: N_{RB}^{UL}^{⋅}^{⋅}^{√}−^{m}^{2}1−^{∂}^{∂}^{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}for ^{for }l^{l}=^{=}6^{5}]![](media_svg/image708.svg) [公式: for(m+n_{s}mod2)mod2=0]![](media_svg/image713.svg) [公式≈: N_{RB}^{UL}_{⋅}_{⋅}_{√}−_{m}_{2}1−_{∂}_{∂}_{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}_{for }for _{l}l_{=}=_{6}5]![](media_svg/image710.svg) [公式: for(m+n_{s}mod2)mod2=1] | ![](media_svg/image714.svg) [公式: mfor l=6] |
| 3 | ![](media_svg/image715.svg) [公式≈: N_{RB}^{UL}^{⋅}^{⋅}^{√}−^{m}^{2}1−^{∂}^{∂}^{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}^{for }for ^{l}l^{=}=^{1}0]![](media_svg/image708.svg) [公式: for(m+n_{s}mod2)mod2=0]![](media_svg/image716.svg) [公式≈: N_{RB}^{UL}_{⋅}_{⋅}_{√}−_{m}_{2}1−_{∂}_{∂}_{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}for _{for }l_{l}=_{=}1_{0}]![](media_svg/image710.svg) [公式: for(m+n_{s}mod2)mod2=1] | ![](media_svg/image717.svg) [公式: mfor l=1] |
| 4 | ![](media_svg/image718.svg) [公式≈: N_{RB}^{UL}^{⋅}^{⋅}^{√}−^{m}^{2}1−^{∂}^{∂}^{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}^{for }for ^{l}l^{=}=^{2}3]![](media_svg/image708.svg) [公式: for(m+n_{s}mod2)mod2=0]![](media_svg/image719.svg) [公式≈: N_{RB}^{UL}_{⋅}_{⋅}_{√}−_{m}_{2}1−_{∂}_{∂}_{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}for _{for }l_{l}=_{=}2_{3}]![](media_svg/image710.svg) [公式: for(m+n_{s}mod2)mod2=1] | ![](media_svg/image720.svg) [公式: mfor l=3] |
| 5 | ![](media_svg/image721.svg) [公式≈: N_{RB}^{UL}^{⋅}^{⋅}^{√}−^{m}^{2}1−^{∂}^{∂}^{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}^{for }for ^{l}l^{=}=^{5}^{,}4^{6}]![](media_svg/image708.svg) [公式: for(m+n_{s}mod2)mod2=0]![](media_svg/image722.svg) [公式≈: N_{RB}^{UL}_{⋅}_{⋅}_{√}−_{m}_{2}1−_{∂}_{∂}_{∃}^{⋅}_{⋅}_{√}^{m}_{2}^{∂}_{∂}_{∃}for _{for }l_{l}=_{=}5,_{4}6]![](media_svg/image710.svg) [公式: for(m+n_{s}mod2)mod2=1] | ![](media_svg/image723.svg) [公式: mfor l=5,6] |

The variable ![](media_svg/image615.svg) [公式: m] depends on the SPUCCH format as defined in Table 5.4A.5-5.

Table 5.4A.5-5: ![](media_svg/image615.svg) [公式: m] for SPUCCH

| SPUCCH Format |  | ![](media_svg/image615.svg) [公式: m] |
| --- | --- | --- |
| Slot | Format 1, 1a, 1b | Frequency hopping disabled: see derivation of ![](media_svg/image615.svg) [公式: m] for PUCCH format 1, 1a, 1b in clause 5.4.3 replacing ![](media_svg/image724.svg) [公式≈: _{n}_{PUCCH}(1,^{~}p)] with ![](media_svg/image725.svg) [公式≈: ^{n}SPUCCH^{(1,}^{~}^{p}^{)}]Frequency hopping enabled: see derivation of ![](media_svg/image615.svg) [公式: m] for PUCCH format 2, 2a, 2b in clause 5.4.3 replacing ![](media_svg/image726.svg) [公式≈: _{n}_{PUCCH}(2,^{~}p)] with ![](media_svg/image727.svg) [公式≈: ^{n}SPUCCH^{(1,}^{~}^{p}^{)}] |
|  | Format 3 | ![](media_svg/image728.svg) [公式≈: √^{n}SPUCCH^{(3,}^{~}^{p}^{)}^{N}SF,0^{PUCCH}∃] |
|  | Format 4 | ![](media_svg/image729.svg) [公式≈: ^{m}^{=}^{n}SPUCCH^{(4)}^{,}^{n}SPUCCH^{(4)}^{+}^{1}^{,...,}^{n}SPUCCH^{(4)}^{+}^{M}RB^{SPUCCH4}^{−}^{1}] |
| Subslot | Format 1, 1a, 1b | see derivation of ![](media_svg/image615.svg) [公式: m] for PUCCH format 2, 2a, 2b in clause 5.4.3 replacing ![](media_svg/image726.svg) [公式≈: _{n}_{PUCCH}(2,^{~}p)] with ![](media_svg/image730.svg) [公式≈: ^{n}SPUCCH,^{(1,}^{~}^{p}^{)}i] |
|  | Format 4 | ![](media_svg/image731.svg) [公式≈: ^{m}^{=}^{n}SPUCCH^{(4)}^{,}^{n}SPUCCH^{(4)}^{+}^{1}^{,...,}^{n}SPUCCH^{(4)}^{+}^{M}RB^{SPUCCH4}^{−}^{1}] |

In case of subslot-SPUCCH, there is a configuration restriction that each SPUCCH resource in the resource set, of up to four resources, ![](media_svg/image650.svg) [公式≈: n_{SPUCCH,}^{(1,}^{~}^{p}^{)}_{i},i⎰{0,1,2,3}], shall map to the same pair of PRBs (![](media_svg/image692.svg) [公式≈: ^{n}PRB]) This restriction applies separately to each of n1SubslotSPUCCH-AN-List and sr-SubslotSPUCCH-Resource in TS 36.331 [9].

In case of simultaneous transmission of sounding reference signal and SPUCCH when there is one serving cell configured, the shortened SPUCCH format shall be used where the last SC-FDMA symbol in the second slot of a subframe shall be left empty.

## 5.5 Reference signals

Two types of uplink reference signals are supported:

- Demodulation reference signal, associated with transmission of PUSCH or (S)PUCCH

- Sounding reference signal, not associated with transmission of PUSCH or (S)PUCCH

The same set of base sequences is used for demodulation and sounding reference signals.

### 5.5.1 Generation of the reference signal sequence

Reference signal sequence ![](media_svg/image732.svg) [公式≈: _{r}_{u}(_{,}Α_{v},Δ)_{(}_{n}_{)}] is defined by a cyclic shift ![](media_svg/image733.svg) [公式: Α] of a base sequence ![](media_svg/image734.svg) [公式: r_{u}_{,}_{v}(n)] according to

![](media_svg/image735.svg) [公式≈: r_{u}^{(}_{,}^{Α}_{v}^{,}^{Δ}^{)}(n)=e^{j}^{Α}^{⊇}^{⊕}^{⊗}^{n}^{+}^{Δ}^{ς}^{mod}^{2}^{2}^{⇒}^{⇐}^{⇔}r_{u}_{,}_{v}(n),0≥n<M_{sc}^{RS}]

where

- ![](media_svg/image736.svg) [公式≈: _{M}_{sc}RS_{=}_{mN}_{sc}RB_{2}Δ] is the length of the reference signal sequence, ![](media_svg/image737.svg) [公式≈: _{1}_{≥}_{m}_{≥}_{N}_{RB}max,UL], ![](media_svg/image738.svg) [公式: ς] is defined in clause 5.5.2.1.2, and,

- ![](media_svg/image739.svg) [公式: Δ=1] when either

- the higher-layer parameter ul-DMRS-IFDMA is set and the most recent uplink-related DCI contains the Cyclic Shift Field mapping table for DMRS bit field which is set to 1 to indicate the use of Table 5.5.2.1.1-3, or,

- the Cyclic Shift Field mapping table for DMRS bit is set to 1 in the most recent uplink-related DCI format 7 which indicates the use of Table 5.5.2.1.1-4, and

- ![](media_svg/image740.svg) [公式: Δ=0] otherwise.

Multiple reference signal sequences are defined from a single base sequence through different values of ![](media_svg/image733.svg) [公式: Α].

Base sequences ![](media_svg/image734.svg) [公式: r_{u}_{,}_{v}(n)] are divided into groups, where ![](media_svg/image741.svg) [公式: u⎰{0,1,...,29}] is the group number and ![](media_svg/image742.svg) [公式: v] is the base sequence number within the group, such that each group contains one base sequence (![](media_svg/image743.svg) [公式: v=0]) of each length ![](media_svg/image744.svg) [公式≈: _{M}_{sc}RS_{=}_{mN}_{sc}RB], ![](media_svg/image745.svg) [公式: 1≥m≥5] and two base sequences (![](media_svg/image746.svg) [公式: v=0,1]) of each length ![](media_svg/image747.svg) [公式≈: _{M}_{sc}RS_{=}_{mN}_{sc}RB], ![](media_svg/image748.svg) [公式≈: _{6}_{≥}_{m}_{≥}_{N}_{RB}max,UL]. The sequence group number ![](media_svg/image749.svg) [公式: u] and the number ![](media_svg/image742.svg) [公式: v] within the group may vary in time as described in clauses 5.5.1.3 and 5.5.1.4, respectively. The definition of the base sequence ![](media_svg/image750.svg) [公式≈: r_{u}_{,}_{v}(0),...,r_{u}_{,}_{v}(M_{sc}^{RS}−1)] depends on the sequence length![](media_svg/image751.svg) [公式≈: _{M}_{sc}RS].

#### 5.5.1.1 Base sequences of length ![](media_svg/image752.svg) [公式≈: _{3}_{N}_{sc}RB] or larger

For![](media_svg/image753.svg) [公式≈: _{M}_{sc}RS_{÷}_{3}_{N}_{sc}RB], the base sequence ![](media_svg/image750.svg) [公式≈: r_{u}_{,}_{v}(0),...,r_{u}_{,}_{v}(M_{sc}^{RS}−1)] is given by

![](media_svg/image754.svg) [公式≈: r_{u}_{,}_{v}(n)=x_{q}(nmodN_{ZC}^{RS}),0≥n<M_{sc}^{RS}]

where the ![](media_svg/image755.svg) [公式≈: _{q}th] root Zadoff-Chu sequence is defined by

![](media_svg/image756.svg) [公式≈: x_{q}(m)=e^{−}^{j}^{Π}^{qm}^{N}^{(}^{ZC}^{RS}^{m}^{+}^{1}^{)},0≥m≥N_{ZC}^{RS}−1]

with ![](media_svg/image757.svg) [公式: q] given by

![](media_svg/image758.svg) [公式≈: q_{q}=_{=}_{√}_{N}q_{ZC}_{RS}+1_{∪}_{(}2_{u}_{∃}_{+}+_{1}v_{)}∪(_{31}−1)^{√}^{2}^{q}^{∃}]

The length ![](media_svg/image759.svg) [公式≈: _{N}_{ZC}RS] of the Zadoff-Chu sequence is given by the largest prime number such that![](media_svg/image760.svg) [公式≈: _{N}_{ZC}RS_{<}_{M}_{sc}RS].

#### 5.5.1.2 Base sequences of length less than ![](media_svg/image752.svg) [公式≈: _{3}_{N}_{sc}RB]

For ![](media_svg/image761.svg) [公式≈: _{M}_{sc}RS_{=}_{N}_{sc}RB], ![](media_svg/image762.svg) [公式≈: _{M}_{sc}RS_{=}_{2}_{N}_{sc}RB], ![](media_svg/image763.svg) [公式≈: M_{sc}^{RS}=N_{sc}^{RB}2], and ![](media_svg/image764.svg) [公式≈: M_{sc}^{RS}=3N_{sc}^{RB}2], the base sequence is given by

![](media_svg/image765.svg) [公式≈: r_{u}_{,}_{v}(n)=e^{j}^{ϑ}^{(}^{n}^{)}^{Π}^{4},0≥n≥M_{sc}^{RS}−1]

where the value of ![](media_svg/image766.svg) [公式: ϑ(n)] is given by Table 5.5.1.2-1, Table 5.5.1.2-2, Table 5.5.1.2-3, and Table 5.5.1.2-4 for ![](media_svg/image761.svg) [公式≈: _{M}_{sc}RS_{=}_{N}_{sc}RB], ![](media_svg/image762.svg) [公式≈: _{M}_{sc}RS_{=}_{2}_{N}_{sc}RB], ![](media_svg/image763.svg) [公式≈: M_{sc}^{RS}=N_{sc}^{RB}2], and ![](media_svg/image764.svg) [公式≈: M_{sc}^{RS}=3N_{sc}^{RB}2], respectively. For ![](media_svg/image767.svg) [公式≈: M_{sc}^{RS}=5N_{sc}^{RB}2], the base sequence ![](media_svg/image750.svg) [公式≈: r_{u}_{,}_{v}(0),...,r_{u}_{,}_{v}(M_{sc}^{RS}−1)] is given by

![](media_svg/image768.svg) [公式≈: _{r}_{u}_{,}_{v}_{(}_{n}_{)}_{=}_{e}_{−}_{j}Π(u+1)(_{31}n+1)(n+2)_{,}_{0}_{≥}_{n}_{≥}_{M}_{sc}_{RS}_{−}_{1}]

Table 5.5.1.2-1: Definition of ![](media_svg/image766.svg) [公式: ϑ(n)] for ![](media_svg/image761.svg) [公式≈: _{M}_{sc}RS_{=}_{N}_{sc}RB].

| ![](media_svg/image749.svg) [公式: u] | ![](media_svg/image769.svg) [公式: ϑ(0),...,ϑ(11)] |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | -1 | 1 | 3 | -3 | 3 | 3 | 1 | 1 | 3 | 1 | -3 | 3 |
| 1 | 1 | 1 | 3 | 3 | 3 | -1 | 1 | -3 | -3 | 1 | -3 | 3 |
| 2 | 1 | 1 | -3 | -3 | -3 | -1 | -3 | -3 | 1 | -3 | 1 | -1 |
| 3 | -1 | 1 | 1 | 1 | 1 | -1 | -3 | -3 | 1 | -3 | 3 | -1 |
| 4 | -1 | 3 | 1 | -1 | 1 | -1 | -3 | -1 | 1 | -1 | 1 | 3 |
| 5 | 1 | -3 | 3 | -1 | -1 | 1 | 1 | -1 | -1 | 3 | -3 | 1 |
| 6 | -1 | 3 | -3 | -3 | -3 | 3 | 1 | -1 | 3 | 3 | -3 | 1 |
| 7 | -3 | -1 | -1 | -1 | 1 | -3 | 3 | -1 | 1 | -3 | 3 | 1 |
| 8 | 1 | -3 | 3 | 1 | -1 | -1 | -1 | 1 | 1 | 3 | -1 | 1 |
| 9 | 1 | -3 | -1 | 3 | 3 | -1 | -3 | 1 | 1 | 1 | 1 | 1 |
| 10 | -1 | 3 | -1 | 1 | 1 | -3 | -3 | -1 | -3 | -3 | 3 | -1 |
| 11 | 3 | 1 | -1 | -1 | 3 | 3 | -3 | 1 | 3 | 1 | 3 | 3 |
| 12 | 1 | -3 | 1 | 1 | -3 | 1 | 1 | 1 | -3 | -3 | -3 | 1 |
| 13 | 3 | 3 | -3 | 3 | -3 | 1 | 1 | 3 | -1 | -3 | 3 | 3 |
| 14 | -3 | 1 | -1 | -3 | -1 | 3 | 1 | 3 | 3 | 3 | -1 | 1 |
| 15 | 3 | -1 | 1 | -3 | -1 | -1 | 1 | 1 | 3 | 1 | -1 | -3 |
| 16 | 1 | 3 | 1 | -1 | 1 | 3 | 3 | 3 | -1 | -1 | 3 | -1 |
| 17 | -3 | 1 | 1 | 3 | -3 | 3 | -3 | -3 | 3 | 1 | 3 | -1 |
| 18 | -3 | 3 | 1 | 1 | -3 | 1 | -3 | -3 | -1 | -1 | 1 | -3 |
| 19 | -1 | 3 | 1 | 3 | 1 | -1 | -1 | 3 | -3 | -1 | -3 | -1 |
| 20 | -1 | -3 | 1 | 1 | 1 | 1 | 3 | 1 | -1 | 1 | -3 | -1 |
| 21 | -1 | 3 | -1 | 1 | -3 | -3 | -3 | -3 | -3 | 1 | -1 | -3 |
| 22 | 1 | 1 | -3 | -3 | -3 | -3 | -1 | 3 | -3 | 1 | -3 | 3 |
| 23 | 1 | 1 | -1 | -3 | -1 | -3 | 1 | -1 | 1 | 3 | -1 | 1 |
| 24 | 1 | 1 | 3 | 1 | 3 | 3 | -1 | 1 | -1 | -3 | -3 | 1 |
| 25 | 1 | -3 | 3 | 3 | 1 | 3 | 3 | 1 | -3 | -1 | -1 | 3 |
| 26 | 1 | 3 | -3 | -3 | 3 | -3 | 1 | -1 | -1 | 3 | -1 | -3 |
| 27 | -3 | -1 | -3 | -1 | -3 | 3 | 1 | -1 | 1 | 3 | -3 | -3 |
| 28 | -1 | 3 | -3 | 3 | -1 | 3 | 3 | -3 | 3 | 3 | -1 | -1 |
| 29 | 3 | -3 | -3 | -1 | -1 | -3 | -1 | 3 | -3 | 3 | 1 | -1 |

Table 5.5.1.2-2: Definition of ![](media_svg/image766.svg) [公式: ϑ(n)] for ![](media_svg/image762.svg) [公式≈: _{M}_{sc}RS_{=}_{2}_{N}_{sc}RB]

| ![](media_svg/image749.svg) [公式: u] | ![](media_svg/image770.svg) [公式: ϑ(0),...,ϑ(23)] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | -1 | 3 | 1 | -3 | 3 | -1 | 1 | 3 | -3 | 3 | 1 | 3 | -3 | 3 | 1 | 1 | -1 | 1 | 3 | -3 | 3 | -3 | -1 | -3 |
| 1 | -3 | 3 | -3 | -3 | -3 | 1 | -3 | -3 | 3 | -1 | 1 | 1 | 1 | 3 | 1 | -1 | 3 | -3 | -3 | 1 | 3 | 1 | 1 | -3 |
| 2 | 3 | -1 | 3 | 3 | 1 | 1 | -3 | 3 | 3 | 3 | 3 | 1 | -1 | 3 | -1 | 1 | 1 | -1 | -3 | -1 | -1 | 1 | 3 | 3 |
| 3 | -1 | -3 | 1 | 1 | 3 | -3 | 1 | 1 | -3 | -1 | -1 | 1 | 3 | 1 | 3 | 1 | -1 | 3 | 1 | 1 | -3 | -1 | -3 | -1 |
| 4 | -1 | -1 | -1 | -3 | -3 | -1 | 1 | 1 | 3 | 3 | -1 | 3 | -1 | 1 | -1 | -3 | 1 | -1 | -3 | -3 | 1 | -3 | -1 | -1 |
| 5 | -3 | 1 | 1 | 3 | -1 | 1 | 3 | 1 | -3 | 1 | -3 | 1 | 1 | -1 | -1 | 3 | -1 | -3 | 3 | -3 | -3 | -3 | 1 | 1 |
| 6 | 1 | 1 | -1 | -1 | 3 | -3 | -3 | 3 | -3 | 1 | -1 | -1 | 1 | -1 | 1 | 1 | -1 | -3 | -1 | 1 | -1 | 3 | -1 | -3 |
| 7 | -3 | 3 | 3 | -1 | -1 | -3 | -1 | 3 | 1 | 3 | 1 | 3 | 1 | 1 | -1 | 3 | 1 | -1 | 1 | 3 | -3 | -1 | -1 | 1 |
| 8 | -3 | 1 | 3 | -3 | 1 | -1 | -3 | 3 | -3 | 3 | -1 | -1 | -1 | -1 | 1 | -3 | -3 | -3 | 1 | -3 | -3 | -3 | 1 | -3 |
| 9 | 1 | 1 | -3 | 3 | 3 | -1 | -3 | -1 | 3 | -3 | 3 | 3 | 3 | -1 | 1 | 1 | -3 | 1 | -1 | 1 | 1 | -3 | 1 | 1 |
| 10 | -1 | 1 | -3 | -3 | 3 | -1 | 3 | -1 | -1 | -3 | -3 | -3 | -1 | -3 | -3 | 1 | -1 | 1 | 3 | 3 | -1 | 1 | -1 | 3 |
| 11 | 1 | 3 | 3 | -3 | -3 | 1 | 3 | 1 | -1 | -3 | -3 | -3 | 3 | 3 | -3 | 3 | 3 | -1 | -3 | 3 | -1 | 1 | -3 | 1 |
| 12 | 1 | 3 | 3 | 1 | 1 | 1 | -1 | -1 | 1 | -3 | 3 | -1 | 1 | 1 | -3 | 3 | 3 | -1 | -3 | 3 | -3 | -1 | -3 | -1 |
| 13 | 3 | -1 | -1 | -1 | -1 | -3 | -1 | 3 | 3 | 1 | -1 | 1 | 3 | 3 | 3 | -1 | 1 | 1 | -3 | 1 | 3 | -1 | -3 | 3 |
| 14 | -3 | -3 | 3 | 1 | 3 | 1 | -3 | 3 | 1 | 3 | 1 | 1 | 3 | 3 | -1 | -1 | -3 | 1 | -3 | -1 | 3 | 1 | 1 | 3 |
| 15 | -1 | -1 | 1 | -3 | 1 | 3 | -3 | 1 | -1 | -3 | -1 | 3 | 1 | 3 | 1 | -1 | -3 | -3 | -1 | -1 | -3 | -3 | -3 | -1 |
| 16 | -1 | -3 | 3 | -1 | -1 | -1 | -1 | 1 | 1 | -3 | 3 | 1 | 3 | 3 | 1 | -1 | 1 | -3 | 1 | -3 | 1 | 1 | -3 | -1 |
| 17 | 1 | 3 | -1 | 3 | 3 | -1 | -3 | 1 | -1 | -3 | 3 | 3 | 3 | -1 | 1 | 1 | 3 | -1 | -3 | -1 | 3 | -1 | -1 | -1 |
| 18 | 1 | 1 | 1 | 1 | 1 | -1 | 3 | -1 | -3 | 1 | 1 | 3 | -3 | 1 | -3 | -1 | 1 | 1 | -3 | -3 | 3 | 1 | 1 | -3 |
| 19 | 1 | 3 | 3 | 1 | -1 | -3 | 3 | -1 | 3 | 3 | 3 | -3 | 1 | -1 | 1 | -1 | -3 | -1 | 1 | 3 | -1 | 3 | -3 | -3 |
| 20 | -1 | -3 | 3 | -3 | -3 | -3 | -1 | -1 | -3 | -1 | -3 | 3 | 1 | 3 | -3 | -1 | 3 | -1 | 1 | -1 | 3 | -3 | 1 | -1 |
| 21 | -3 | -3 | 1 | 1 | -1 | 1 | -1 | 1 | -1 | 3 | 1 | -3 | -1 | 1 | -1 | 1 | -1 | -1 | 3 | 3 | -3 | -1 | 1 | -3 |
| 22 | -3 | -1 | -3 | 3 | 1 | -1 | -3 | -1 | -3 | -3 | 3 | -3 | 3 | -3 | -1 | 1 | 3 | 1 | -3 | 1 | 3 | 3 | -1 | -3 |
| 23 | -1 | -1 | -1 | -1 | 3 | 3 | 3 | 1 | 3 | 3 | -3 | 1 | 3 | -1 | 3 | -1 | 3 | 3 | -3 | 3 | 1 | -1 | 3 | 3 |
| 24 | 1 | -1 | 3 | 3 | -1 | -3 | 3 | -3 | -1 | -1 | 3 | -1 | 3 | -1 | -1 | 1 | 1 | 1 | 1 | -1 | -1 | -3 | -1 | 3 |
| 25 | 1 | -1 | 1 | -1 | 3 | -1 | 3 | 1 | 1 | -1 | -1 | -3 | 1 | 1 | -3 | 1 | 3 | -3 | 1 | 1 | -3 | -3 | -1 | -1 |
| 26 | -3 | -1 | 1 | 3 | 1 | 1 | -3 | -1 | -1 | -3 | 3 | -3 | 3 | 1 | -3 | 3 | -3 | 1 | -1 | 1 | -3 | 1 | 1 | 1 |
| 27 | -1 | -3 | 3 | 3 | 1 | 1 | 3 | -1 | -3 | -1 | -1 | -1 | 3 | 1 | -3 | -3 | -1 | 3 | -3 | -1 | -3 | -1 | -3 | -1 |
| 28 | -1 | -3 | -1 | -1 | 1 | -3 | -1 | -1 | 1 | -1 | -3 | 1 | 1 | -3 | 1 | -3 | -3 | 3 | 1 | 1 | -1 | 3 | -1 | -1 |
| 29 | 1 | 1 | -1 | -1 | -3 | -1 | 3 | -1 | 3 | -1 | 1 | 3 | 1 | -1 | 3 | 1 | 3 | -3 | -3 | 1 | -1 | -1 | 1 | 3 |

Table 5.5.1.2-3: Definition of ![](media_svg/image766.svg) [公式: ϑ(n)] for ![](media_svg/image771.svg) [公式≈: M_{sc}^{RS}=N_{sc}^{RB}2]

| ![](media_svg/image749.svg) [公式: u] | ![](media_svg/image772.svg) [公式: ϑ(0),...,ϑ(5)] |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | -1 | -3 | 3 | -3 | 3 | -3 |
| 1 | -1 | 3 | -1 | 1 | 1 | 1 |
| 2 | 3 | -1 | -3 | -3 | 1 | 3 |
| 3 | 3 | -1 | -1 | 1 | -1 | -1 |
| 4 | -1 | -1 | -3 | 1 | -3 | -1 |
| 5 | 1 | 3 | -3 | -1 | -3 | 3 |
| 6 | -3 | 3 | -1 | -1 | 1 | -3 |
| 7 | -1 | -3 | -3 | 1 | 3 | 3 |
| 8 | 3 | -1 | -1 | 3 | 1 | 3 |
| 9 | 3 | -3 | 3 | 1 | -1 | 1 |
| 10 | -3 | 1 | -3 | -3 | -3 | -3 |
| 11 | -3 | -3 | -3 | 1 | -3 | -3 |
| 12 | 3 | -3 | 1 | -1 | -3 | -3 |
| 13 | 3 | -3 | 3 | -1 | -1 | -3 |
| 14 | 3 | -1 | 1 | 3 | 3 | 1 |
| 15 | -1 | 1 | -1 | -3 | 1 | 1 |
| 16 | -3 | -1 | -3 | -1 | 3 | 3 |
| 17 | 1 | -1 | 3 | -3 | 3 | 3 |
| 18 | 1 | 3 | 1 | 1 | -3 | 3 |
| 19 | -1 | -3 | -1 | -1 | 3 | -3 |
| 20 | 3 | -1 | -3 | -1 | -1 | -3 |
| 21 | 3 | 1 | 3 | -3 | -3 | 1 |
| 22 | 1 | 3 | -1 | -1 | 1 | -1 |
| 23 | -3 | 1 | -3 | 3 | 3 | 3 |
| 24 | 1 | 3 | -3 | 3 | -3 | 3 |
| 25 | -1 | -1 | 1 | -3 | 1 | -1 |
| 26 | 1 | -3 | -1 | -1 | 3 | 1 |
| 27 | -3 | -1 | -1 | 3 | 1 | 1 |
| 28 | -1 | 3 | -3 | -3 | -3 | 3 |
| 29 | 3 | 1 | -1 | 1 | 3 | 1 |

Table 5.5.1.2-4: Definition of ![](media_svg/image766.svg) [公式: ϑ(n)] for ![](media_svg/image773.svg) [公式≈: M_{sc}^{RS}=3N_{sc}^{RB}2]

| ![](media_svg/image749.svg) [公式: u] | ![](media_svg/image774.svg) [公式: ϑ(0),...,ϑ(17)] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | -3 | -3 | -3 | -3 | -3 | -1 | 1 | -1 | -3 | 3 | -1 | 3 | -1 | 3 | -3 | -1 | -1 | 3 |
| 1 | -3 | -3 | -3 | -3 | -3 | -1 | 1 | -1 | 1 | -3 | -3 | -3 | 1 | -1 | 3 | -3 | -3 | 1 |
| 2 | -3 | -3 | -3 | -3 | -3 | -1 | 1 | 1 | 3 | -3 | 1 | 1 | -3 | 1 | -3 | 3 | 1 | -1 |
| 3 | -3 | -3 | -3 | -3 | -3 | -1 | 1 | 3 | -3 | -1 | 3 | -1 | 3 | 1 | -1 | -3 | 3 | -3 |
| 4 | -3 | -3 | -3 | -3 | -3 | -1 | 3 | -3 | -1 | 1 | -1 | -3 | 3 | 3 | 1 | -3 | 1 | -1 |
| 5 | -3 | -3 | -3 | -3 | -3 | 1 | -3 | -3 | -3 | -3 | 1 | 1 | 1 | -3 | 1 | 1 | -3 | -3 |
| 6 | -3 | -3 | -3 | -3 | -3 | 1 | -3 | -3 | 1 | 1 | -3 | -3 | -3 | 1 | -1 | 3 | -1 | 3 |
| 7 | -3 | -3 | -3 | -3 | -3 | 1 | -3 | -1 | 3 | -1 | 3 | 3 | -1 | -1 | 1 | 3 | 3 | -1 |
| 8 | -3 | -3 | -3 | -3 | -3 | 1 | -1 | -1 | -1 | -3 | 3 | -1 | 3 | -3 | 3 | -1 | 1 | 3 |
| 9 | -3 | -3 | -3 | -3 | -3 | 3 | -3 | 1 | -1 | 3 | -3 | 3 | 3 | -1 | -3 | 1 | 1 | -3 |
| 10 | -3 | -3 | -3 | -3 | -3 | 3 | -1 | -3 | -3 | 1 | 1 | 3 | -3 | -1 | 3 | -1 | 3 | 1 |
| 11 | -3 | -3 | -3 | -3 | -3 | 3 | 3 | -1 | -1 | -1 | 3 | 1 | -3 | 3 | -1 | 1 | -3 | 1 |
| 12 | -3 | -3 | -3 | -3 | -1 | -3 | -3 | -3 | 1 | 3 | 1 | -1 | 3 | -3 | -1 | -3 | 1 | 1 |
| 13 | -3 | -3 | -3 | -3 | -1 | -3 | -3 | 1 | -1 | -1 | 3 | -3 | -3 | 1 | 3 | 1 | -3 | 1 |
| 14 | -3 | -3 | -3 | -3 | -1 | -3 | -3 | 1 | 3 | -3 | -1 | 3 | 1 | 3 | -1 | 3 | -1 | -3 |
| 15 | -3 | -3 | -3 | -3 | -1 | -3 | -1 | 3 | -3 | 1 | -3 | 1 | -1 | -3 | -3 | 1 | 1 | 3 |
| 16 | -3 | -3 | -3 | -3 | -1 | -1 | 3 | -3 | 3 | -1 | -3 | 1 | 1 | -1 | -3 | -1 | 3 | -3 |
| 17 | -3 | -3 | -3 | -3 | -1 | -1 | 3 | -1 | -3 | 1 | 3 | -1 | -3 | -3 | 1 | 3 | -1 | 1 |
| 18 | -3 | -3 | -3 | -3 | -1 | 3 | -1 | -1 | 3 | 3 | -1 | -3 | 1 | 1 | 1 | -1 | -3 | -1 |
| 19 | -3 | -3 | -3 | -3 | -1 | 3 | 1 | -3 | -1 | -3 | 3 | 1 | -1 | 3 | -1 | 1 | 3 | -1 |
| 20 | -3 | -3 | -3 | -3 | 1 | -3 | -3 | 3 | 1 | 1 | -3 | -1 | 1 | 3 | 3 | -1 | 3 | -1 |
| 21 | -3 | -3 | -3 | -3 | 1 | -3 | 1 | 3 | 1 | -1 | -1 | 3 | 3 | -1 | 1 | 1 | -3 | 3 |
| 22 | -3 | -3 | -3 | -3 | 1 | -3 | 3 | -3 | -1 | 3 | 1 | 1 | -1 | -1 | 3 | 3 | -1 | 3 |
| 23 | -3 | -3 | -3 | -3 | 1 | -3 | 3 | -1 | 3 | -3 | -1 | -1 | -1 | 1 | -3 | -3 | 3 | 1 |
| 24 | -3 | -3 | -3 | -3 | 1 | 1 | 3 | 1 | 1 | -1 | 3 | 1 | 1 | 3 | -1 | -3 | 1 | 3 |
| 25 | -3 | -3 | -3 | -3 | 1 | 3 | 3 | 3 | 1 | -3 | 1 | -3 | -3 | 3 | -3 | 1 | -1 | -3 |
| 26 | -3 | -3 | -3 | -3 | 3 | 1 | 3 | 3 | -1 | 3 | -3 | -3 | -1 | 3 | -1 | -1 | -3 | 1 |
| 27 | -3 | -3 | -3 | -1 | -3 | -3 | -1 | -1 | -3 | 3 | 3 | 1 | -3 | -1 | -1 | 3 | 1 | -3 |
| 28 | -3 | -3 | -3 | -1 | -3 | 1 | -1 | 1 | -3 | 3 | 1 | -3 | -1 | 1 | 3 | 1 | -1 | -1 |
| 29 | -3 | -3 | -3 | -1 | -3 | 3 | 1 | 1 | -1 | -1 | 1 | 3 | 1 | -3 | 1 | -3 | -1 | 1 |

#### 5.5.1.3 Group hopping

The sequence-group number ![](media_svg/image749.svg) [公式: u] in slot ![](media_svg/image126.svg) [公式≈: ^{n}s] is defined by a group hopping pattern ![](media_svg/image775.svg) [公式: f_{gh}(n_{s})] and a sequence-shift pattern ![](media_svg/image776.svg) [公式≈: ^{f}ss] according to

![](media_svg/image777.svg) [公式≈: u=(f_{gh}(n_{s})+f_{ss})mod30]

There are 17 different hopping patterns and 30 different sequence-shift patterns. Sequence-group hopping can be enabled or disabled by means of the cell-specific parameter Group-hopping-enabled provided by higher layers. Sequence-group hopping for PUSCH can be disabled for a certain UE through the higher-layer parameter Disable-sequence-group-hopping despite being enabled on a cell basis unless the PUSCH transmission corresponds to a Random Access Response Grant or a retransmission of the same transport block as part of the contention based random access procedure.

The group-hopping pattern ![](media_svg/image775.svg) [公式: f_{gh}(n_{s})] may be different for PUSCH, (S)PUCCH and SRS and is given by

![](media_svg/image778.svg) [公式≈: ^{f}^{gh}^{(}^{n}^{s}^{)}^{=}^{√}^{⌡}^{⌠}_{⌡}_{∞}^{⊇}⊕_{⊗}^{0}⊆_{i}^{7}_{=}_{0}c(8ns+i)∪2^{i}^{⇒}⇐_{⇔}mod30^{if}if^{group}group^{hopping}hopping^{is}is^{disabled}enabled]

where the pseudo-random sequence ![](media_svg/image447.svg) [公式: c(i)] is defined by clause 7.2. The pseudo-random sequence generator shall be initialized with ![](media_svg/image779.svg) [公式≈: ^{c}init^{=}^{⋅}⋅_{⋅}_{√}^{n}_{30}^{ID}^{RS}^{∂}∂_{∂}_{∃}] at the beginning of each radio frame where ![](media_svg/image780.svg) [公式≈: _{n}_{ID}RS] is given by clause 5.5.1.5.

The sequence-shift pattern ![](media_svg/image776.svg) [公式≈: ^{f}ss] definition differs between PUCCH, PUSCH and SRS.

For SPUCCH/PUCCH, the sequence-shift pattern ![](media_svg/image781.svg) [公式≈: _{f}_{ss}PUCCH] is given by ![](media_svg/image782.svg) [公式≈: f_{ss}^{PUCCH}=n_{ID}^{RS}mod30] where ![](media_svg/image780.svg) [公式≈: _{n}_{ID}RS] is given by clause 5.5.1.5.

For PUSCH, the sequence-shift pattern ![](media_svg/image783.svg) [公式≈: _{f}_{ss}PUSCH] is given by ![](media_svg/image784.svg) [公式≈: f_{ss}^{PUSCH}=(N_{ID}^{cell}+δ_{ss})mod30], where ![](media_svg/image785.svg) [公式: δ_{ss}⎰{0,1,...,29}] is configured by higher layers, if no value for ![](media_svg/image786.svg) [公式≈: _{n}_{ID}PUSCH] is provided by higher layers or if the PUSCH transmission corresponds to a Random Access Response Grant or a retransmission of the same transport block as part of the contention based random access procedure, otherwise it is given by ![](media_svg/image787.svg) [公式≈: f_{ss}^{PUSCH}=n_{ID}^{RS}mod30] with ![](media_svg/image780.svg) [公式≈: _{n}_{ID}RS] given by clause 5.5.1.5.

For SRS, the sequence-shift pattern ![](media_svg/image788.svg) [公式≈: _{f}_{ss}SRS] is given by![](media_svg/image789.svg) [公式≈: f_{ss}^{SRS}=n_{ID}^{RS}mod30] where ![](media_svg/image780.svg) [公式≈: _{n}_{ID}RS] is given by clause 5.5.1.5.

#### 5.5.1.4 Sequence hopping

Sequence hopping only applies for reference-signals of length ![](media_svg/image790.svg) [公式≈: _{M}_{sc}RS_{÷}_{6}_{N}_{sc}RB].

For reference-signals of length ![](media_svg/image791.svg) [公式≈: _{M}_{sc}RS_{<}_{6}_{N}_{sc}RB], the base sequence number ![](media_svg/image742.svg) [公式: v] within the base sequence group is given by ![](media_svg/image792.svg) [公式: v=0].

For reference-signals of length ![](media_svg/image790.svg) [公式≈: _{M}_{sc}RS_{÷}_{6}_{N}_{sc}RB], the base sequence number ![](media_svg/image742.svg) [公式: v] within the base sequence group in slot ![](media_svg/image793.svg) [公式≈: ^{n}s] is defined by

![](media_svg/image794.svg) [公式≈: _{v}_{=}√_{⌠}_{∞}c_{0}(n_{s})if_{otherwise}grouphoppingisdisabledandsequencehoppingisenabled]

where the pseudo-random sequence ![](media_svg/image447.svg) [公式: c(i)] is given by clause 7.2. The parameter Sequence-hopping-enabled provided by higher layers determines if sequence hopping is enabled or not. Sequence hopping for PUSCH can be disabled for a certain UE through the higher-layer parameter Disable-sequence-group-hopping despite being enabled on a cell basis unless the PUSCH transmission corresponds to a Random Access Response Grant or a retransmission of the same transport block as part of the contention based random access procedure.

For PUSCH or SPUCCH/PUCCH format 4 transmission with ≥ 6 RBs, the pseudo-random sequence generator shall be initialized with ![](media_svg/image795.svg) [公式≈: cinit=^{⋅}⋅_{⋅}_{√}^{n}_{30}^{ID}^{RS}^{∂}∂_{∂}_{∃}∪2^{5}+fss^{PUSCH}] at the beginning of each radio frame where ![](media_svg/image780.svg) [公式≈: _{n}_{ID}RS] is given by clause 5.5.1.5.

For SRS, the pseudo-random sequence generator shall be initialized with ![](media_svg/image796.svg) [公式≈: cinit=^{⋅}⋅_{⋅}_{√}^{n}_{30}^{ID}^{RS}^{∂}∂_{∂}_{∃}∪2^{5}+(nID^{RS}+δss)mod30] at the beginning of each radio frame where ![](media_svg/image780.svg) [公式≈: _{n}_{ID}RS] is given by clause 5.5.1.5 and ![](media_svg/image797.svg) [公式≈: ^{δ}ss] is given by clause 5.5.1.3.

#### 5.5.1.5 Determining virtual cell identity for sequence generation

The definition of ![](media_svg/image780.svg) [公式≈: _{n}_{ID}RS] depends on the type of transmission.

Transmissions associated with PUSCH:

- ![](media_svg/image798.svg) [公式≈: _{n}_{ID}RS_{=}_{N}_{ID}cell] if no value for ![](media_svg/image799.svg) [公式≈: _{n}_{ID}PUSCH] is configured by higher layers or if the PUSCH transmission corresponds to a Random Access Response Grant or a retransmission of the same transport block as part of the contention based random access procedure,

- ![](media_svg/image800.svg) [公式≈: _{n}_{ID}RS_{=}_{n}_{ID}PUSCH] otherwise.

Transmissions associated with SPUCCH/PUCCH:

- ![](media_svg/image798.svg) [公式≈: _{n}_{ID}RS_{=}_{N}_{ID}cell] if no value for ![](media_svg/image801.svg) [公式≈: _{n}_{ID}PUCCH] is configured by higher layers,

- ![](media_svg/image802.svg) [公式≈: _{n}_{ID}RS_{=}_{n}_{ID}PUCCH] otherwise.

Basic sounding reference signals:

- $ n_{ID}^{RS}=n_{ID}^{SRS}$ if the higher-layer parameter srs-VirtualCellID is configured and srs-VirtualCellID-AllSRS is configured as TRUE, where $ n_{ID}^{SRS}$ equals the higher-layer parameter srs-VirtualCellID

- $ n_{ID}^{RS}=N_{ID}^{cell}$ otherwise.

Additional sounding reference signals:

- $ n_{ID}^{RS}=N_{ID}^{cell}$ if no value for $ n_{ID}^{SRS}$ is configured by the higher-layer parameter srs-VirtualCellID

- $ n_{ID}^{RS}=n_{ID}^{SRS}$ otherwise.

### 5.5.2 Demodulation reference signal

#### 5.5.2.1 Demodulation reference signal for PUSCH

##### 5.5.2.1.1 Reference signal sequence

The PUSCH demodulation reference signal sequence ![](media_svg/image803.svg) [公式≈: ^{r}PUSCH^{(}^{Λ}^{)}^{(}^{∪}^{)}] associated with layer ![](media_svg/image804.svg) [公式: Λ⎰{0,1,...,Υ−1}] is defined by

![](media_svg/image805.svg) [公式≈: r_{PUSCH}^{(}^{Λ}^{)}(m∪M_{sc}^{RS}+n)=w^{(}^{Λ}^{)}(m)r_{u}^{(}_{,}^{Α}_{v}^{Λ}^{,}^{Δ}^{)}(n)]

where

![](media_svg/image806.svg) [公式≈: _{m}_{n}_{=}_{=}_{0}√_{⌠}_{∞}_{,...,}0_{0}_{,}_{1}_{M}for _{otherwise}_{sc}_{RS}_{−}special_{1}subframeand(sub)slot-PUSCH]

and ![](media_svg/image807.svg) [公式≈: _{M}_{sc}RS_{=}_{M}_{sc}PUSCH_{2}] if

- the higher-layer parameter ul-DMRS-IFDMA is set and the most recent uplink-related DCI contains the Cyclic Shift Field mapping table for DMRS bit field which is set to 1 to indicate the use of Table 5.5.2.1.1-3, or,

- the Cyclic Shift Field mapping table for DMRS bit field is set to 1 in the most recent uplink-related DCI format 7 which indicates the use of Table 5.5.2.1.1-4, or,

- subslot-PUSCH/slot-PUSCH for the transport block is semi-persistently scheduled (i.e. higher layer parameter sps-ConfigUL-STTI is configured, see TS 36.331 [9]), and ifdma-Config-SPS is set.

In all other cases, ![](media_svg/image808.svg) [公式≈: _{M}_{sc}RS_{=}_{M}_{sc}PUSCH].

Clause 5.5.1 defines the sequence ![](media_svg/image809.svg) [公式≈: r_{u}^{(}_{,}^{Α}_{v}^{Λ}^{,}^{Δ}^{)}(0),...,r_{u}^{(}_{,}^{Α}_{v}^{Λ}^{,}^{Δ}^{)}(M_{sc}^{RS}−1)] where, for PUSCH demodulation reference signal sequence, ![](media_svg/image739.svg) [公式: Δ=1] when

- the higher-layer parameter ul-DMRS-IFDMA is set and the most recent uplink-related DCI contains the Cyclic Shift Field mapping table for DMRS bit field which is set to 1 to indicate the use of Table 5.5.2.1.1-3, or,

- the Cyclic Shift Field mapping table for DMRS bit field is set to 1 in the most recent uplink-related DCI format 7 which indicates the use of Table 5.5.2.1.1-4, or,

- subslot-PUSCH/slot-PUSCH for the transport block is semi-persistently scheduled (i.e. higher layer parameter sps-ConfigUL-STTI is configured, see TS 36.331 [9]), and ifdma-Config-SPS is set.

In all other cases, ![](media_svg/image740.svg) [公式: Δ=0].

The orthogonal sequence ![](media_svg/image810.svg) [公式: w^{(}^{Λ}^{)}(m)] is given by ![](media_svg/image811.svg) [公式: w^{(}^{Λ}^{)}(m)=1] for subslot-PUSCH/slot-PUSCH. In all other cases, it is given by ![](media_svg/image812.svg) [公式: {w^{Λ}(0)w^{Λ}(1)}={11}] for DCI format 0 if the higher-layer parameter Activate-DMRS-with OCC is not set or if the temporary C-RNTI was used to transmit the most recent uplink-related DCI for the transport block associated with the corresponding PUSCH transmission. Otherwise,

- if higher-layer parameter ul-DMRS-IFDMA is not set, ![](media_svg/image810.svg) [公式: w^{(}^{Λ}^{)}(m)] is given by Table 5.5.2.1.1-1 using the cyclic shift field in the most recent uplink-related DCI [3],

- if higher-layer parameter ul-DMRS-IFDMA is set and the Cyclic Shift Field mapping table for DMRS bit field is not present in the most recent uplink-related DCI, ![](media_svg/image810.svg) [公式: w^{(}^{Λ}^{)}(m)] is given by Table 5.5.2.1.1-1 using the cyclic shift field in the most recent uplink-related DCI,

- if higher-layer parameter ul-DMRS-IFDMA is set and the Cyclic Shift Field mapping table for DMRS bit field is present in the most recent uplink-related DCI, ![](media_svg/image810.svg) [公式: w^{(}^{Λ}^{)}(m)] is given by Table 5.5.2.1.1-1 using the cyclic shift field in the most recent uplink-related DCI when the Cyclic Shift Field mapping table for DMRS bit field is set to 0, and

- if higher-layer parameter ul-DMRS-IFDMA is set and the Cyclic Shift Field mapping table for DMRS bit field is present in the most recent uplink-related DCI, ![](media_svg/image810.svg) [公式: w^{(}^{Λ}^{)}(m)] is given by Table 5.5.2.1.1-3 using the cyclic shift field in the most recent uplink-related DCI when the Cyclic Shift Field mapping table for DMRS bit field is set to 1.

The cyclic shift ![](media_svg/image813.svg) [公式≈: ^{Α}Λ] in a slot ![](media_svg/image126.svg) [公式≈: ^{n}s] is given as ![](media_svg/image814.svg) [公式: Α_{Λ}=0]if the ul-V-SPS-RNTI-r14 was used to transmit the most recent uplink-related DCI for the transport block associated with the corresponding PUSCH transmission. For PUSCH transmissions not using sub-PRB allocations, if pusch-CyclicShift in higher layer parameter PUR-PUSCH-Config is configured, then for PUSCH (re)transmission corresponding to preconfigured uplink resource it provides the value of $ n_{cs,\lambda  }$ and the cyclic shift ![](media_svg/image813.svg) [公式≈: ^{Α}Λ] in a slot ![](media_svg/image126.svg) [公式≈: ^{n}s] is given as ![](media_svg/image815.svg) [公式≈: Α_{Λ}=2Πn_{cs,}_{Λ}12].

Otherwise, the cyclic shift ![](media_svg/image813.svg) [公式≈: ^{Α}Λ] in a slot ![](media_svg/image126.svg) [公式≈: ^{n}s] is given as ![](media_svg/image815.svg) [公式≈: Α_{Λ}=2Πn_{cs,}_{Λ}12] with

![](media_svg/image816.svg) [公式≈: n_{cs,}_{Λ}=(n_{DMRS}^{(}^{1}^{)}+n_{DMRS,}^{(}^{2}^{)}_{Λ}+(1+Δ)n_{PN}(n_{s}))mod12]

where the value of ![](media_svg/image817.svg) [公式≈: ^{n}DMRS^{(1)}] is given by Table 5.5.2.1.1-2 according to the parameter cyclicShift provided by higher layers. For non-BL/CE UEs ![](media_svg/image818.svg) [公式≈: ^{n}DMRS,^{(2)}Λ] is given using the most recent uplink-related DCI TS36.212 [3] for the transport block associated with the corresponding PUSCH transmission, except for subslot-PUSCH/slot-PUSCH, as follows:

- if the higher-layer parameter ul-DMRS-IFDMA is not set, ![](media_svg/image819.svg) [公式≈: ^{n}DMRS,^{(2)}Λ] is given by Table 5.5.2.1.1-1 using the cyclic shift field in the most recent uplink-related DCI,

- if higher-layer parameter ul-DMRS-IFDMA is set and the Cyclic Shift Field mapping table for DMRS bit field is not present in the most recent uplink-related DCI, ![](media_svg/image819.svg) [公式≈: ^{n}DMRS,^{(2)}Λ] is given by Table 5.5.2.1.1-1 using the cyclic shift field in the most recent uplink-related DCI,

- if higher-layer parameter ul-DMRS-IFDMA is set and the Cyclic Shift Field mapping table for DMRS bit field is present in the most recent uplink-related DCI, ![](media_svg/image819.svg) [公式≈: ^{n}DMRS,^{(2)}Λ] is given by Table 5.5.2.1.1-1 using the cyclic shift field in the most recent uplink-related DCI when the Cyclic Shift Field mapping table for DMRS bit field is set to 0, and

- if higher-layer parameter ul-DMRS-IFDMA is set and the Cyclic Shift Field mapping table for DMRS bit field is present in the most recent uplink-related DCI, ![](media_svg/image819.svg) [公式≈: ^{n}DMRS,^{(2)}Λ] is given by Table 5.5.2.1.1-3 using the cyclic shift field in the most recent uplink-related DCI when the Cyclic Shift Field mapping table for DMRS bit field is set to 1.

For subslot-PUSCH/slot-PUSCH for non-BL/CE UEs, ![](media_svg/image818.svg) [公式≈: ^{n}DMRS,^{(2)}Λ]is given by Table 5.5.2.1.1-4, using the cyclic shift field in the most recent uplink-related DCI. If the Cyclic Shift Field mapping table for DMRS bit field is set to 0, ![](media_svg/image820.svg) [公式: ς]in Table 5.5.2.1.1-4 is ignored. If the Cyclic Shift Field mapping table for DMRS bit field is set to 1, both ![](media_svg/image821.svg) [公式≈: ^{n}DMRS,^{(2)}Λ] and ![](media_svg/image820.svg) [公式: ς]are given by Table 5.5.2.1.1-4.

For BL/CE UEs, a cyclic shift field of '000' shall be assumed when determining ![](media_svg/image818.svg) [公式≈: ^{n}DMRS,^{(2)}Λ] from Table 5.5.2.1.1-1.

For subframe-based PUSCH transmission, the first row of Table 5.5.2.1.1-1 shall be used to obtain ![](media_svg/image822.svg) [公式≈: ^{n}DMRS,^{(2)}0] and ![](media_svg/image810.svg) [公式: w^{(}^{Λ}^{)}(m)] if there is no uplink-related DCI for the same transport block associated with the corresponding PUSCH transmission, and

- if the initial PUSCH for the same transport block is semi-persistently scheduled and cyclicShiftSPS is not configured, or

- if the initial PUSCH for the same transport block is scheduled by the random-access response grant.

An exception applies if subframe-based PUSCH for the transport block is semi-persistently scheduled and the higher-layer parameter cyclicShiftSPS is configured. In this case, the value of  is given by Table 5.5.2.1.1-1 according to the higher-layer parameter cyclicShiftSPS.

An exception applies if subslot-PUSCH/slot-PUSCH for the transport block is semi-persistently scheduled (see TS 36.331, sps-ConfigUL-sTTI). In this case:

- ![](media_svg/image823.svg) [公式≈: ^{n}DMRS,^{(2)}0] is given by Table 5.5.2.1.1-1 according to the higher-layer parameter cyclicShiftSPS-STTI if the higher layer parameter ifdma-Config-SPS is not set, and,

- ![](media_svg/image824.svg) [公式≈: ^{n}DMRS,^{(2)}0] and ![](media_svg/image820.svg) [公式: ς]are given by Table 5.5.2.1.1-3 according to the higher-layer parameter cyclicShiftSPS-STTI if the higher layer parameter ifdma-Config-SPS is set.

The quantity ![](media_svg/image825.svg) [公式: n_{PN}(n_{s})] is given by

![](media_svg/image826.svg) [公式≈: n_{PN}(n_{s})=_{⊆}_{i}^{7}_{=}_{0}c(8N_{symb}^{UL}∪n_{s}+i)∪2^{i}]

where the pseudo-random sequence ![](media_svg/image447.svg) [公式: c(i)] is defined by clause 7.2. The application of ![](media_svg/image447.svg) [公式: c(i)] is cell-specific. The pseudo-random sequence generator shall be initialized with ![](media_svg/image827.svg) [公式≈: ^{c}init] at the beginning of each radio frame. The quantity ![](media_svg/image827.svg) [公式≈: ^{c}init] is given by ![](media_svg/image828.svg) [公式≈: cinit=^{⋅}⋅_{⋅}_{√}^{N}_{30}^{ID}^{cell}^{∂}∂_{∂}_{∃}∪2^{5}+((NID^{cell}+δss)mod30)] if no value for ![](media_svg/image829.svg) [公式≈: _{N}_{ID}csh_DMRS] is configured by higher layers for PUSCH/(S)PUCCH format 4/PUCCH format 5 or the PUSCH transmission corresponds to a Random Access Response Grant or a retransmission of the same transport block as part of the contention based random access procedure, otherwise it is given by ![](media_svg/image830.svg) [公式≈: cinit=^{⋅}⋅_{⋅}_{√}^{N}^{ID}^{csh_DMRS}_{30}^{∂}∂_{∂}_{∃}∪2^{5}+(NID^{csh_DMRS}mod30)].

The vector of reference signals shall be precoded according to

![](media_svg/image831.svg) [公式≈: ^{⊥}^{⋅}^{⋅}⋅_{√}^{~}~^{r}_{r}^{PUSCH}_{PUSCH}^{(}(^{0}P^{μ}^{)}−1)^{∀}^{∂}^{∂}∂_{∃}^{=}^{W}^{⊥}^{⋅}^{⋅}⋅_{√}^{r}_{r}^{PUSCH}_{PUSCH}^{(}(Υ^{0}^{)}−^{μ}1)^{∀}^{∂}^{∂}∂_{∃}]

where ![](media_svg/image832.svg) [公式: P] is the number of antenna ports used for PUSCH transmission.

For PUSCH transmission using a single antenna port, ![](media_svg/image833.svg) [公式: P=1], ![](media_svg/image834.svg) [公式: W=1] and ![](media_svg/image835.svg) [公式: Υ=1].

For spatial multiplexing, ![](media_svg/image836.svg) [公式: P=2] or ![](media_svg/image837.svg) [公式: P=4] and the precoding matrix ![](media_svg/image838.svg) [公式: W] shall be identical to the precoding matrix used in clause 5.3.3A.2 for precoding of the PUSCH in the same subframe.

Table 5.5.2.1.1-1: Mapping of Cyclic Shift Field in uplink-related DCI format to ![](media_svg/image839.svg) [公式≈: ^{n}DMRS,^{(2)}Λ] and ![](media_svg/image840.svg) [公式≈: {w^{(}^{Λ}^{)}(0)w^{(}^{Λ}^{)}(1)}]

| Cyclic Shift Field in uplink-related DCI format [3] | ![](media_svg/image821.svg) [公式≈: ^{n}DMRS,^{(2)}Λ] |  |  |  | ![](media_svg/image841.svg) [公式≈: {w^{(}^{Λ}^{)}(0)w^{(}^{Λ}^{)}(1)}] |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | ![](media_svg/image844.svg) [公式: Λ=2] | ![](media_svg/image845.svg) [公式: Λ=3] |  | ![](media_svg/image846.svg) [公式: Λ=1] | ![](media_svg/image847.svg) [公式: Λ=2] | ![](media_svg/image848.svg) [公式: Λ=3] |
| 000 | 0 | 6 | 3 | 9 | ![](media_svg/image849.svg) [公式: {11}] | ![](media_svg/image849.svg) [公式: {11}] | ![](media_svg/image850.svg) [公式: {1−1}] | ![](media_svg/image850.svg) [公式: {1−1}] |
| 001 | 6 | 0 | 9 | 3 | ![](media_svg/image850.svg) [公式: {1−1}] | ![](media_svg/image850.svg) [公式: {1−1}] | ![](media_svg/image849.svg) [公式: {11}] | ![](media_svg/image849.svg) [公式: {11}] |
| 010 | 3 | 9 | 6 | 0 | ![](media_svg/image850.svg) [公式: {1−1}] | ![](media_svg/image850.svg) [公式: {1−1}] | ![](media_svg/image849.svg) [公式: {11}] | ![](media_svg/image849.svg) [公式: {11}] |
| 011 | 4 | 10 | 7 | 1 | ![](media_svg/image849.svg) [公式: {11}] | ![](media_svg/image849.svg) [公式: {11}] | ![](media_svg/image849.svg) [公式: {11}] | ![](media_svg/image849.svg) [公式: {11}] |
| 100 | 2 | 8 | 5 | 11 | ![](media_svg/image849.svg) [公式: {11}] | ![](media_svg/image849.svg) [公式: {11}] | ![](media_svg/image849.svg) [公式: {11}] | ![](media_svg/image849.svg) [公式: {11}] |
| 101 | 8 | 2 | 11 | 5 | ![](media_svg/image850.svg) [公式: {1−1}] | ![](media_svg/image850.svg) [公式: {1−1}] | ![](media_svg/image850.svg) [公式: {1−1}] | ![](media_svg/image850.svg) [公式: {1−1}] |
| 110 | 10 | 4 | 1 | 7 | ![](media_svg/image850.svg) [公式: {1−1}] | ![](media_svg/image850.svg) [公式: {1−1}] | ![](media_svg/image850.svg) [公式: {1−1}] | ![](media_svg/image850.svg) [公式: {1−1}] |
| 111 | 9 | 3 | 0 | 6 | ![](media_svg/image849.svg) [公式: {11}] | ![](media_svg/image849.svg) [公式: {11}] | ![](media_svg/image850.svg) [公式: {1−1}] | ![](media_svg/image850.svg) [公式: {1−1}] |

Table 5.5.2.1.1-2: Mapping of cyclicShift to ![](media_svg/image851.svg) [公式≈: ^{n}DMRS^{(1)}]values

| cyclicShift | ![](media_svg/image851.svg) [公式≈: ^{n}DMRS^{(1)}] |
| --- | --- |
| 0 | 0 |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |
| 4 | 6 |
| 5 | 8 |
| 6 | 9 |
| 7 | 10 |

Table 5.5.2.1.1-3: Mapping of Cyclic Shift Field in uplink-related DCI format to ![](media_svg/image839.svg) [公式≈: ^{n}DMRS,^{(2)}Λ], ![](media_svg/image820.svg) [公式: ς], and ![](media_svg/image840.svg) [公式≈: {w^{(}^{Λ}^{)}(0)w^{(}^{Λ}^{)}(1)}]

| Cyclic Shift Field in uplink-related DCI format [3] | ![](media_svg/image820.svg) [公式: ς] | ![](media_svg/image821.svg) [公式≈: ^{n}DMRS,^{(2)}Λ] |  |  |  | ![](media_svg/image841.svg) [公式≈: {w^{(}^{Λ}^{)}(0)w^{(}^{Λ}^{)}(1)}] |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |
| 000 | 1 | 0 | 6 | 3 | 9 |  |  |  |  |
| 001 | 1 | 6 | 0 | 9 | 3 |  |  |  |  |
| 010 | 1 | 3 | 9 | 6 | 0 |  |  |  |  |
| 011 | 0 | 4 | 10 | 7 | 1 |  |  |  |  |
| 100 | 0 | 2 | 8 | 5 | 11 |  |  |  |  |
| 101 | 0 | 8 | 2 | 11 | 5 |  |  |  |  |
| 110 | 0 | 10 | 4 | 1 | 7 |  |  |  |  |
| 111 | 1 | 9 | 3 | 0 | 6 |  |  |  |  |

Table 5.5.2.1.1-4: ![](media_svg/image839.svg) [公式≈: ^{n}DMRS,^{(2)}Λ] for subslot-PUSCH/slot-PUSCH

| Cyclic Shift Field in uplink-related DCI format [3] | ![](media_svg/image821.svg) [公式≈: ^{n}DMRS,^{(2)}Λ] |  |  |  | ![](media_svg/image820.svg) [公式: ς] |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | ![](media_svg/image844.svg) [公式: Λ=2] | ![](media_svg/image845.svg) [公式: Λ=3] |  |  | ![](media_svg/image844.svg) [公式: Λ=2] | ![](media_svg/image845.svg) [公式: Λ=3] |
| 0 | 0 | 6 | 3 | 9 | 0 | 0 | 1 | 1 |
| 1 | 6 | 0 | 9 | 3 | 1 | 1 | 0 | 0 |

##### 5.5.2.1.2 Mapping to physical resources

For each antenna port used for transmission of the PUSCH, the sequence ![](media_svg/image864.svg) [公式≈: ^{~}^{r}PUSCH^{(}^{~}^{p}^{)}^{(}^{∪}^{)}] shall be multiplied with the amplitude scaling factor ![](media_svg/image865.svg) [公式≈: ^{1}^{+}^{Δ}^{Β}PUSCH] and mapped in sequence starting with ![](media_svg/image866.svg) [公式≈: ^{~}^{r}PUSCH^{(}^{~}^{p}^{)}^{(}^{0}^{)}] to the resource blocks.

- ![](media_svg/image739.svg) [公式: Δ=1] when either

- the higher-layer parameter ul-DMRS-IFDMA is set and the most recent uplink-related DCI contains the Cyclic Shift Field mapping table for DMRS bit field which is set to 1 to indicate the use of Table 5.5.2.1.1-3, or

- the Cyclic Shift Field mapping table for DMRS bit field is set to 1 in the most recent uplink-related DCI format 7 which indicates the use of Table 5.5.2.1.1-4, and

- ![](media_svg/image740.svg) [公式: Δ=0] otherwise.

If higher-layer parameter ul-DMRS-IFDMA is set and the most recent uplink-related DCI contains the Cyclic Shift Field mapping table for DMRS bit field which is set to 1 to indicate the use of Table 5.5.2.1.1-3, the mapping to resource elements ![](media_svg/image867.svg) [公式: (k,l)], with ![](media_svg/image868.svg) [公式: l=3] for normal cyclic prefix and ![](media_svg/image869.svg) [公式: l=2] for extended cyclic prefix, in the subframe shall be in increasing order of first ![](media_svg/image2.svg) [公式: k] for all values of ![](media_svg/image2.svg) [公式: k] satisfying ![](media_svg/image870.svg) [公式: kmod2=ς], then the slot number. The quantity ![](media_svg/image820.svg) [公式: ς] is given by Table 5.5.2.1.1-3 using the cyclic shift field in the most recent uplink-related DCI.

In case of slot-PUSCH, the mapping to resource elements ![](media_svg/image867.svg) [公式: (k,l)], with ![](media_svg/image868.svg) [公式: l=3] for normal cyclic prefix, in the slot of the subframe where slot-PUSCH is transmitted shall be in increasing order of first ![](media_svg/image2.svg) [公式: k] for all values of ![](media_svg/image2.svg) [公式: k], except if the Cyclic Shift Field mapping table for DMRS bit field is set to 1 in the most recent uplink-related DCI format 7, which indicates the use of Table 5.5.2.1.1-4. In this case the mapping to resource element shall be in increasing order of first ![](media_svg/image2.svg) [公式: k] only for values of ![](media_svg/image2.svg) [公式: k] satisfying ![](media_svg/image870.svg) [公式: kmod2=ς].

In case of subslot-PUSCH, the mapping to resource elements ![](media_svg/image867.svg) [公式: (k,l)], in the subframe shall be in increasing order of first ![](media_svg/image2.svg) [公式: k] for all values of ![](media_svg/image2.svg) [公式: k], except if the Cyclic Shift Field mapping table for DMRS bit field is set to 1 in the most recent uplink-related DCI format 7, which indicates the use of Table 5.5.2.1.1-4. In this case the mapping to resource element shall be in increasing order of first ![](media_svg/image2.svg) [公式: k] only for values of ![](media_svg/image2.svg) [公式: k] satisfying ![](media_svg/image870.svg) [公式: kmod2=ς]. The value of ![](media_svg/image871.svg) [公式: l] depends on the uplink subslot number and the DMRS-pattern field in the most recent uplink-related DCI, according to Table 5.5.2.1.2-1, or according to Table 5.5.2.1.2-2 in case of semi-persistent scheduling of subslot-PUSCH (i.e. higher layer patameter sps-ConfigUL-sTTI-r15 is configured, se TS 36.331 [9]) and with a configured periodicity of 1 subslot (i.e. semiPersistSchedIntervalUL-STTI-r15 set to sTTI1). In case of subslot-PUSCH and semi-persistent scheduling with a configured periodicity longer than 1 subslot, the mapping shall start at symbol ![](media_svg/image400.svg) [公式: l] according to the first row of Table 5.5.2.1.2-2 (i.e. equivalent to a signalling of DMRS-pattern field set to '00'). In case no value of ![](media_svg/image871.svg) [公式: l] is defined for the uplink subslot number, and in case no valid starting symbol index (see table 5.3.4-1), no reference signal is transmitted associated with the uplink-related DCI format.

Table 5.5.2.1.2-1: The quantity ![](media_svg/image871.svg) [公式: l] for subslot-PUSCH

| DMRS-pattern field in uplink-related DCI format [3] | Uplink subslot number |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | #0 | #1 | #2 | #3 | #4 | #5 |
| 00 | 0 | 3 | 5 | 0 | 2 | 4 |
| 01 | 2 | 4 | - | 1 | 3 | - |
| 10 | - | - | - | 2 | - | - |
| 11 | - | 5 | - | - | 4 | - |

Table 5.5.2.1.2-2: The quantity ![](media_svg/image871.svg) [公式: l] for subslot-PUSCH for semi-persistent scheduling

| DMRS-pattern field in uplink-related DCI format [3] | Uplink subslot number |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | #0 | #1 | #2 | #3 | #4 | #5 |
| 00 | 0 | 3 | 5 | 0 | 2 | 4 |
| 10 | 0 | 5 | 5 | 2 | 2 | 4 |

For all other cases, the set of physical resource blocks used in the mapping process and the relation between the index ![](media_svg/image872.svg) [公式≈: ^{~}p] and the antenna port number ![](media_svg/image873.svg) [公式: p] shall be identical to the corresponding PUSCH transmission as defined in clause 5.3.4.

The mapping to resource elements ![](media_svg/image1.svg) [公式: (k,l)], with ![](media_svg/image868.svg) [公式: l=3], or with ![](media_svg/image871.svg) [公式: l] according to Table 5.5.2.1.2-1 for subslot-PUSCH, for normal cyclic prefix and ![](media_svg/image874.svg) [公式: l=2] for extended cyclic prefix, in the subframe shall be in increasing order of first![](media_svg/image2.svg) [公式: k], then the slot number, except for slot-PUSCH and subslot-PUSCH where the reference signal is only mapped to the slot where the slot-PUSCH/subslot-PUSCH is transmitted). No DM-RS shall be transmitted in UpPTS if dmrsLess-UpPts is set to true.

For BL/CE UEs, if uplink resource reservation is enabled for the UE as specified in [9], and the Resource reservation field in the DCI is set to 1, then in case of PUSCH transmission with ![](media_svg/image420.svg) [公式≈: _{N}_{rep}PUSCH_{>}_{1}] associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PUSCH transmission without a corresponding MPDCCH,

- In a subframe that is fully reserved as defined in clause 8.0 in [4], the demodulation reference signal transmission is postponed until the next BL/CE uplink subframe that is not fully reserved.

- In a subframe that is partially reserved, the demodulation reference signal transmission in a SC-FDMA symbol that is reserved is dropped.

#### 5.5.2.1A Demodulation reference signal for PUSCH with sub-PRB allocations

##### 5.5.2.1A.1 Reference signal sequence using modulation schemes other than π/2-BPSK

The reference signal sequence  for  is defined by a cyclic shift  of a base sequence according to

,

where  is given by Tables 5.5.2.1A.1-1 and 5.5.2.1A.1-2 for and , respectively. The cyclic shift  is derived from higher layer parameters threeTone-CyclicShift and sixTone-CyclicShift, respectively, as defined in Table 5.5.2.1A.1-3.

If group hopping is enabled, the base sequence index  is given by clause 5.5.2.1A.3.

If group hopping is not enabled, the base sequence index  is given by

-  for

-  for

Table 5.5.2.1A.1-1: Definition of  for

|  | $\emptyset  \left ( 0\right ) , \ldots   ,\emptyset  \left ( 2\right ) $ |  |  |
| --- | --- | --- | --- |
| 0 | 1 | -3 | -3 |
| 1 | 1 | -3 | -1 |
| 2 | 1 | -3 | 3 |
| 3 | 1 | -1 | -1 |
| 4 | 1 | -1 | 1 |
| 5 | 1 | -1 | 3 |
| 6 | 1 | 1 | -3 |
| 7 | 1 | 1 | -1 |
| 8 | 1 | 1 | 3 |
| 9 | 1 | 3 | -1 |
| 10 | 1 | 3 | 1 |
| 11 | 1 | 3 | 3 |

Table 5.5.2.1A.1-2: Definition of  for

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 1 | 1 | 3 | -3 |
| 1 | 1 | 1 | 3 | 1 | -3 | 3 |
| 2 | 1 | -1 | -1 | -1 | 1 | -3 |
| 3 | 1 | -1 | 3 | -3 | -1 | -1 |
| 4 | 1 | 3 | 1 | -1 | -1 | 3 |
| 5 | 1 | -3 | -3 | 1 | 3 | 1 |
| 6 | -1 | -1 | 1 | -3 | -3 | -1 |
| 7 | -1 | -1 | -1 | 3 | -3 | -1 |
| 8 | 3 | -1 | 1 | -3 | -3 | 3 |
| 9 | 3 | -1 | 3 | -3 | -1 | 1 |
| 10 | 3 | -3 | 3 | -1 | 3 | 3 |
| 11 | -3 | 1 | 3 | 1 | -3 | -1 |
| 12 | -3 | 1 | -3 | 3 | -3 | -1 |
| 13 | -3 | 3 | -3 | 1 | 1 | -3 |

Table 5.5.2.1A.1-3: Definition of

|  |  |  |  |
| --- | --- | --- | --- |
| threeTone-CyclicShift |  | sixTone-CyclicShift |  |
| 0 |  | 0 |  |
| 1 |  | 1 |  |
| 2 |  | 2 |  |
| - | - | 3 |  |

##### 5.5.2.1A.2 Reference signal sequence using π/2-BPSK modulation scheme

For  using π/2-BPSK modulation scheme, $ N_{ID}^{cell}mod2 $ is used to determine which 2 of 3 subcarriers will be used:

- 0 indicates that the two subcarriers having the lowest indices among the three allocated are utilized.

- 1 indicates that the two subcarriers having the highest indices among the three allocated are utilized.

The reference signal sequences $\hat {r}_{u1}(n)$ and $\hat {r}_{u2}(n)$ for   using 2 out of 3 subcarriers are defined by

$\hat {r}_{u1}\left ( n\right ) =\frac {1}{\sqrt {2}}\left ( 1+j\right ) \left ( 1-2c\left ( n\right ) \right ) w\left ( nmod16\right ) , 0\leq  n<N_{rep}^{PUSCH}M_{slots}^{UL}M_{RU}$

$\hat {r}_{u2}\left ( n\right ) =(-1)^{n}\left ( \frac {1}{\sqrt {2}}\left ( 1+j\right ) \left ( 1-2c\left ( n\right ) \right ) w\left ( nmod16\right ) \right ) , 0\leq  n<N_{rep}^{PUSCH}M_{slots}^{UL}M_{RU}$

where the binary sequence  is defined by clause 7.2 and shall be initialised with  at the start of the PUSCH transmission using sub-PRB allocations for BL/CE UEs. The quantity  is given by Table 5.5.2.1A.2-1 where $ u=N_{ID}^{cell}mod16 $  if group hopping is not enabled, and by clause 5.5.2.1A.3 if group hopping is enabled for PUSCH using sub-PRB allocations for BL/CE UEs.

Table 5.5.2.1A.2-1: Definition of

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 |
| 2 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 |
| 3 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 |
| 4 | 1 | 1 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 | 1 | 1 | -1 | -1 | -1 | -1 |
| 5 | 1 | -1 | 1 | -1 | -1 | 1 | -1 | 1 | 1 | -1 | 1 | -1 | -1 | 1 | -1 | 1 |
| 6 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 |
| 7 | 1 | -1 | -1 | 1 | -1 | 1 | 1 | -1 | 1 | -1 | -1 | 1 | -1 | 1 | 1 | -1 |
| 8 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |
| 9 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 |
| 10 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 |
| 11 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | -1 |
| 12 | 1 | 1 | 1 | 1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | 1 | 1 | 1 | 1 |
| 13 | 1 | -1 | 1 | -1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | 1 | 1 | -1 | 1 | -1 |
| 14 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | 1 | 1 | -1 | -1 |
| 15 | 1 | -1 | -1 | 1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | 1 | -1 | -1 | 1 |

The reference signal sequences for PUSCH using sub-PRB allocations for BL/CE UEs is given by clause 5.3.3, where ![](media_svg/image900.svg) [公式: rn_{u}_{1}()] and ![](media_svg/image901.svg) [公式: rn_{u}_{2}()] correspond to the complex-valued symbols at the input of the transform precoding. The resulting complex-valued symbols at the output of the transform precoding correspond to the sequence ![](media_svg/image902.svg) [公式: r()∪] which is mapped to physical resources as described in clause 5.5.2.1A.4.

##### 5.5.2.1A.3 Group hopping

For the reference signal for PUSCH transmission using sub-PRB allocations for BL/CE UEs, sequence-group hopping can be enabled where the sequence-group number  in slot  of a radio frame $ n_{f}$ is defined by a group hopping pattern $ f_{gh}\left ( n^{'}\right ) $ and a sequence-shift pattern  according to

$ u=\left ( f_{gh}\left ( n'\right ) +f_{ss}\right ) modM_{seq}^{RU}$

where the number of reference signal sequences available for each resource unit size, $ M_{seq}^{RU}$ is given by Table 5.5.2.1A.3-1.

Table 5.5.2.1A.3-1: Definition of $ M_{seq}^{RU}$

| Modulation Scheme | $ M_{sc}^{RU}$ | $ M_{seq}^{RU}$ |
| --- | --- | --- |
| π/2-BPSK | 3 | 16 |
| QPSK | 3 | 12 |
|  | 6 | 14 |

Sequence-group hopping can be enabled or disabled as described in clause 5.5.1.3.

The group-hopping pattern $ f_{gh}\left ( n^{'}\right ) $ is given by

$ f_{gh}\left ( n'\right ) =\left ( \sum  _{i=0}^{7}c(8n'+i)\cdot  2^{i}\right ) modM_{seq}^{RU}$

where $ n^{'}=n_{s}$ for  using QPSK modulation scheme. When using π/2-BPSK modulation scheme, for frame structure type 1, $ n^{'}$ is the slot number $ n_{s}$ of the first slot of the resource unit, and for frame structure type 2, $ n^{'}$ is the frame number $ n_{f}$ of the first slot of the resource unit. The pseudo-random sequence  is defined by clause 7.2. The pseudo-random sequence generator shall be initialized with $ c_{init}=\lfloor  \frac {N_{ID}^{cell}}{M_{seq}^{RU}}\rfloor  $ at the beginning of the resource unit for using π/2-BPSK modulation scheme and in every even slot for  using QPSK modulation scheme.

The sequence-shift pattern  is given by

$ f_{ss}\left ( n_{s}\right ) =\left ( N_{ID}^{cell}+∆_{ss}\right ) modM_{seq}^{RU}$

where .

##### 5.5.2.1A.4 Mapping to physical resources

The sequence  shall be multiplied with the amplitude scaling factor  and mapped in sequence starting with  to the sub-carriers.

The set of sub-carriers used in the mapping process shall be identical to the corresponding PUSCH transmissions using sub-PRB allocations for BL/CE UEs as defined in clause 5.3.4.

The mapping to resource elements  shall be in increasing order of first, then , and finally the slot number. The value of the symbol index  in a slot is 3.

For BL/CE UEs, if uplink resource reservation is enabled for the UE as specified in [9], and the Resource reservation field in the DCI is set to 1, then in case of PUSCH transmission with ![](media_svg/image420.svg) [公式≈: _{N}_{rep}PUSCH_{>}_{1}] associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PUSCH transmission without a corresponding MPDCCH,

- In a subframe that is fully reserved as defined in clause 8.0 in [4], the demodulation reference signal transmission is postponed until the next BL/CE uplink subframe that is not fully reserved.

- In a subframe that is partially reserved, the demodulation reference signal transmission in a SC-FDMA symbol that is reserved is dropped.

#### 5.5.2.2 Demodulation reference signal for PUCCH

##### 5.5.2.2.1 Reference signal sequence

The PUCCH demodulation reference signal sequence ![](media_svg/image908.svg) [公式≈: ^{r}PUCCH^{(}^{~}^{p}^{)}^{(}^{∪}^{)}] for PUCCH formats 1, 1a, 1b, 2, 2a, 2b, and 3 is defined by

![](media_svg/image909.svg) [公式≈: r_{PUCCH}^{(}^{~}^{p}^{)}(m&apos;N_{RS}^{PUCCH}M_{sc}^{RS}+mM_{sc}^{RS}+n)=^{1}_{P}w^{(}^{~}^{p}^{)}(m)z(m)r_{u}^{(}_{,}^{Α}_{v}^{~}^{p}^{,}^{Δ}^{)}(n)]

where

![](media_svg/image910.svg) [公式≈: ^{m}^{n}m&apos;^{=}^{=}=^{0}^{0}0^{,...,}^{,...,},1^{M}^{N}^{sc}^{RS}^{RS}^{PUCCH}^{−}^{1}^{−}^{1}]

and ![](media_svg/image911.svg) [公式: P] is the number of antenna ports used for PUCCH transmission. For PUCCH formats 2a and 2b, ![](media_svg/image912.svg) [公式: z(m)] equals ![](media_svg/image531.svg) [公式: d(10)] for ![](media_svg/image913.svg) [公式: m=1], where ![](media_svg/image531.svg) [公式: d(10)] is defined in clause 5.4.2. For all other cases, ![](media_svg/image914.svg) [公式: z(m)=1.]

The sequence ![](media_svg/image915.svg) [公式≈: r_{u}^{(}_{,}^{Α}_{v}^{~}^{p}^{)}(n)]is given by clause 5.5.1 with ![](media_svg/image916.svg) [公式: M_{sc}^{RS}=12] and ![](media_svg/image917.svg) [公式: Δ=0] where the expression for the cyclic shift ![](media_svg/image918.svg) [公式: Α~_{p}] is determined by the PUCCH format.

For PUCCH formats 1, 1a and 1b, ![](media_svg/image919.svg) [公式: Α~_{p}(n_{s},l)] is given by

![](media_svg/image920.svg) [公式≈: _{n}^{Α}_{cs}_{(}^{n}_{~}_{p}^{oc}^{~}^{p}^{(}_{)}^{~}^{p}^{(}_{(}^{)}^{n}_{n}^{(}^{s}_{s}^{n}^{,}_{,}^{s}^{l}_{l}^{)}^{)}_{)}^{=}^{=}_{=}^{2}^{√}_{⌡}_{⌠}_{⌡}_{∞}^{√}^{n}^{Π}{_{{}n_{n}^{±}^{~}^{p}_{cs}_{cs}^{cell}_{cell}^{∪}^{(}^{n}^{n}^{cs}^{s}^{(}(_{(}^{~}^{)}^{p}n_{n}^{)}^{∪}_{s}_{s}^{(}^{δ},_{,}^{n}l_{l}^{PUCCH}^{shift}^{s})_{)}^{,}+_{+}^{l}^{)}(_{(}n_{n}^{N}±_{±}~_{~}_{p}_{p}(_{(}^{sc}^{N}^{RB}n_{n}_{s}_{s}^{±}^{∃})_{)}∪_{∪}δ_{δ}^{PUCCH}_{PUCCH}_{shift}_{shift}+_{+}(_{n}n_{oc}_{(}_{oc}^{(}_{~}_{p}^{~}^{p}_{)}^{)}_{(}(_{n}n_{s}_{s}_{)})_{)}mod_{mod}δ_{N}^{PUCCH}_{shift}_{±}_{}}_{mod}))mod_{N}_{sc}_{RB}N±}modN_{sc}^{RB}for _{for }_{extended}normalcyclic_{cyclic}prefix_{prefix}]

where ![](media_svg/image921.svg) [公式: n±~_{p}(n_{s})], ![](media_svg/image922.svg) [公式: N^{±}], ![](media_svg/image923.svg) [公式≈: _{δ}PUCCH_{shift}] and ![](media_svg/image924.svg) [公式≈: n_{cs}^{cell}(n_{s},l)] are defined by clause 5.4.1. The number of reference symbols per slot ![](media_svg/image108.svg) [公式≈: _{N}_{RS}PUCCH] and the sequence ![](media_svg/image925.svg) [公式: w(n)] are given by Table 5.5.2.2.1-1 and 5.5.2.2.1-2, respectively.

For PUCCH formats 2, 2a and 2b, ![](media_svg/image926.svg) [公式: Α~_{p}(n_{s},l)] is defined by clause 5.4.2. The number of reference symbols per slot ![](media_svg/image108.svg) [公式≈: _{N}_{RS}PUCCH] and the sequence ![](media_svg/image927.svg) [公式≈: w^{(}^{~}^{p}^{)}(n)] are given by Table 5.5.2.2.1-1 and 5.5.2.2.1-3, respectively.

For PUCCH format 3, ![](media_svg/image926.svg) [公式: Α~_{p}(n_{s},l)] is given by

![](media_svg/image928.svg) [公式≈: n^{Α}_{cs}^{(}^{~}^{p}^{~}^{p}^{)}^{(}(^{n}n^{s}_{s}^{,},^{l}l^{)})^{=}=(^{2}n^{Π}_{cs}^{cell}^{∪}^{n}(^{cs}^{(}n^{~}^{p}_{s}^{)},^{(}l^{n})^{s}+^{,}^{l}n^{)}±~_{p}(^{N}n^{sc}^{RB}_{s}))modN_{sc}^{RB}]

where ![](media_svg/image929.svg) [公式: n±~_{p}(n_{s})] is given by Table 5.5.2.2.1-4 and ![](media_svg/image930.svg) [公式≈: ^{n}oc,^{(}^{~}^{p}^{)}0] and ![](media_svg/image931.svg) [公式≈: ^{n}oc,^{(}^{~}^{p}1^{)}] for the first and second slot in a subframe, respectively, are obtained from clause 5.4.2A. The number of reference symbols per slot ![](media_svg/image108.svg) [公式≈: _{N}_{RS}PUCCH] and the sequence ![](media_svg/image925.svg) [公式: w(n)] are given by Table 5.5.2.2.1-1 and 5.5.2.2.1-3, respectively.

Table 5.5.2.2.1-1: Number of PUCCH demodulation reference symbols per slot![](media_svg/image108.svg) [公式≈: _{N}_{RS}PUCCH]

| PUCCH format | Normal cyclic prefix | Extended cyclic prefix |
| --- | --- | --- |
| 1, 1a, 1b | 3 | 2 |
| 2, 3 | 2 | 1 |
| 2a, 2b | 2 | N/A |

Table 5.5.2.2.1-2: Orthogonal sequences ![](media_svg/image932.svg) [公式≈: {w^{(}^{~}^{p}^{)}(0)λw^{(}^{~}^{p}^{)}(N_{RS}^{PUCCH}−1)}] for PUCCH formats 1, 1a and 1b

| Sequence index ![](media_svg/image933.svg) [公式≈: n_{oc}^{(}^{~}^{p}^{)}(n_{s})] | Normal cyclic prefix | Extended cyclic prefix |
| --- | --- | --- |
| 0 | ![](media_svg/image510.svg) [公式: {111}] | ![](media_svg/image934.svg) [公式: {11}] |
| 1 | ![](media_svg/image511.svg) [公式≈: _{{}_{1}_{e}j2Π3_{e}j4Π3_{}}] | ![](media_svg/image935.svg) [公式: {1−1}] |
| 2 | ![](media_svg/image512.svg) [公式≈: _{{}_{1}_{e}j4Π3_{e}j2Π3_{}}] | N/A |

Table 5.5.2.2.1-3: Orthogonal sequences ![](media_svg/image936.svg) [公式≈: {w^{(}^{~}^{p}^{)}(0)λw^{(}^{~}^{p}^{)}(N_{RS}^{PUCCH}−1)}] for PUCCH formats 2, 2a, 2b and 3.

| Normal cyclic prefix | Extended cyclic prefix |
| --- | --- |
| ![](media_svg/image937.svg) [公式: {11}] | ![](media_svg/image938.svg) [公式: {1}] |

Table 5.5.2.2.1-4: Relation between ![](media_svg/image939.svg) [公式≈: _{n}_{oc}(^{~}p)] and ![](media_svg/image929.svg) [公式: n±~_{p}(n_{s})] for PUCCH format 3.

| ![](media_svg/image940.svg) [公式≈: _{n}_{oc}(^{~}p)] | ![](media_svg/image929.svg) [公式: n±~_{p}(n_{s})] |  |
| --- | --- | --- |
|  | ![](media_svg/image941.svg) [公式≈: ^{N}SF,1^{=}^{5}] | ![](media_svg/image942.svg) [公式≈: ^{N}SF,1^{=}^{4}] |
| 0 | 0 | 0 |
| 1 | 3 | 3 |
| 2 | 6 | 6 |
| 3 | 8 | 9 |
| 4 | 10 | N/A |

The PUCCH demodulation reference signal sequence ![](media_svg/image908.svg) [公式≈: ^{r}PUCCH^{(}^{~}^{p}^{)}^{(}^{∪}^{)}] for PUCCH formats 4 and 5 is defined by

![](media_svg/image943.svg) [公式≈: r_{PUCCH}^{(}^{~}^{p}^{)}(m∪M_{sc}^{RS}+n)=r_{u}^{(}_{,}^{Α}_{v}^{,}^{Δ}^{)}(n)]

where

![](media_svg/image944.svg) [公式≈: ^{m}n^{~}^{p}=^{=}^{=}0^{0}^{0},...,^{,}^{1}M_{sc}^{RS}−1]

and

![](media_svg/image945.svg) [公式≈: _{M}_{sc}RS_{=}√⌡_{⌠}_{⌡}_{∞}M_{N}_{sc}_{RB}sc^{PUCCH4}for _{for }PUCCH_{PUCCH}format _{format }_{5}4]

Clause 5.5.1 defines the sequence ![](media_svg/image946.svg) [公式≈: r_{u}^{(}_{,}^{Α}_{v}^{Λ}^{,}^{Δ}^{)}(0),...,r_{u}^{(}_{,}^{Α}_{v}^{Λ}^{,}^{Δ}^{)}(M_{sc}^{RS}−1)] where ![](media_svg/image947.svg) [公式: Δ=0].

The cyclic shift ![](media_svg/image813.svg) [公式≈: ^{Α}Λ] in a slot ![](media_svg/image126.svg) [公式≈: ^{n}s] is given as ![](media_svg/image815.svg) [公式≈: Α_{Λ}=2Πn_{cs,}_{Λ}12] with

![](media_svg/image948.svg) [公式≈: n_{cs,}_{Λ}=(n_{DMRS}^{(}^{1}^{)}+n_{DMRS}^{(}^{2}^{)}+n_{PN}(n_{s}))mod12]

where the values of ![](media_svg/image817.svg) [公式≈: ^{n}DMRS^{(1)}]and ![](media_svg/image825.svg) [公式: n_{PN}(n_{s})] are given by Clause 5.5.2.1.1 and

![](media_svg/image949.svg) [公式≈: n_{DMRS}^{(2)}=^{√}^{⌡}_{⌠}_{⌡}_{∞}^{0}0_{6}^{PUCCH}PUCCH_{PUCCH}^{format }format _{format }5_{5}^{4} with _{ with }n_{n}_{oc}_{oc}=_{=}_{1}0]

with ![](media_svg/image592.svg) [公式≈: ^{n}oc] obtained as described in clause 5.4.2C.

##### 5.5.2.2.2 Mapping to physical resources

The sequence ![](media_svg/image950.svg) [公式≈: ^{r}PUCCH^{(}^{~}^{p}^{)}^{(}^{∪}^{)}] shall be multiplied with the amplitude scaling factor ![](media_svg/image951.svg) [公式≈: ^{Β}PUCCH] and mapped in sequence starting with ![](media_svg/image952.svg) [公式≈: ^{r}PUCCH^{(}^{~}^{p}^{)}^{(}^{0}^{)}] to resource elements![](media_svg/image1.svg) [公式: (k,l)] on antenna port ![](media_svg/image953.svg) [公式: p]. The mapping shall be in increasing order of first![](media_svg/image2.svg) [公式: k], then ![](media_svg/image3.svg) [公式: l] and finally the slot number. The set of values for ![](media_svg/image2.svg) [公式: k] and the relation between the index ![](media_svg/image395.svg) [公式≈: ^{~}p] and the antenna port number ![](media_svg/image394.svg) [公式: p] shall be identical to the values used for the corresponding PUCCH transmission. The values of the symbol index ![](media_svg/image3.svg) [公式: l] in a slot are given by Table 5.5.2.2.2-1.

Table 5.5.2.2.2-1: Demodulation reference signal location for different PUCCH formats.

| PUCCH format | Set of values for ![](media_svg/image3.svg) [公式: l] |  |
| --- | --- | --- |
|  | Normal cyclic prefix | Extended cyclic prefix |
| 1, 1a, 1b | 2, 3, 4 | 2, 3 |
| 2, 3 | 1, 5 | 3 |
| 2a, 2b | 1, 5 | N/A |
| 4,5 | 3 | 2 |

For BL/CE UEs, if uplink resource reservation is enabled for the UE as specified in [9], then in case of PUCCH transmission with ![](media_svg/image611.svg) [公式≈: _{N}_{rep}PUCCH_{>}_{1}] associated with C-RNTI or SPS C-RNTI using UE-specific MPDCCH search space including PUCCH transmission without a corresponding MPDCCH,

- In a subframe that is fully reserved as defined in clause 8.0 in [4], the demodulation reference signal transmission is postponed until the next BL/CE uplink subframe that is not fully reserved.

- In a subframe that is partially reserved, the demodulation reference signal transmission in a SC-FDMA symbol that is reserved is dropped.

#### 5.5.2.3 Demodulation reference signal for SPUCCH

##### 5.5.2.3.1 Reference signal sequence

The SPUCCH demodulation reference signal sequence ![](media_svg/image954.svg) [公式≈: ^{r}SPUCCH^{(}^{~}^{p}^{)}^{(}^{∪}^{)}] for subslot-SPUCCH format 4, and, slotSPUCCH formats 1, 1a, 1b, 3 and 4 is as defined for ![](media_svg/image955.svg) [公式≈: ^{r}PUCCH^{(}^{~}^{p}^{)}^{(}^{∪}^{)}] in clause 5.5.2.2.1 for PUCCH format 1, 1a, 1b, 2, 2a, 2b and 3, using the parameter settings in Table 5.5.2.3.1-1, and with the number of reference symbols ![](media_svg/image956.svg) [公式≈: _{N}_{RS}PUCCH] replaced by ![](media_svg/image957.svg) [公式≈: _{N}_{RS}SPUCCH] and given by Table 5.5.2.3.1-2.

NOTE: Subslot-SPUCCH format 1/1a/1b does not employ a reference signal based design.

The sequence ![](media_svg/image915.svg) [公式≈: r_{u}^{(}_{,}^{Α}_{v}^{~}^{p}^{)}(n)]is given by clause 5.5.1 with ![](media_svg/image917.svg) [公式: Δ=0], where the expression for the cyclic shift ![](media_svg/image958.svg) [公式: Α]is determined depending on the SPUCCH format, see table 5.5.2.3.1-3.

Table 5.5.2.3.1-1: Parameters for SPUCCH demodulation reference signal

| SPUCCH format |  | Frequency hopping | ![](media_svg/image959.svg) [公式: m&apos;] | ![](media_svg/image960.svg) [公式≈: _{M}_{sc}RS] | ![](media_svg/image961.svg) [公式≈: w^{(}^{~}^{p}^{)}(m)] | ![](media_svg/image962.svg) [公式: z(m)] |
| --- | --- | --- | --- | --- | --- | --- |
| Slot | 1, 1a, 1b | Disabled | 0 | 12 | See Table 5.5.2.2.1-2 for normal cyclic prefix | 1 |
|  |  | Enabled | 0 | 12 | 1 | 1 |
|  | 3 | Disabled | 0 | 12 | See clause 5.5.2.2.2 | 1 |
|  | 4 | Enabled | 0 | ![](media_svg/image963.svg) [公式≈: _{M}_{sc}SPUCCH4] | 1 | 1 |
| Subslot | 4 | Disabled | 0 | ![](media_svg/image963.svg) [公式≈: _{M}_{sc}SPUCCH4] | 1 | 1 |

Table 5.5.2.3.1-2: Number of SPUCCH demodulation reference symbols ![](media_svg/image109.svg) [公式≈: _{N}_{RS}SPUCCH] per slot or per subslot

| SPUCCH format |  | Frequency hopping | ![](media_svg/image964.svg) [公式≈: _{N}_{RS}SPUCCH] |
| --- | --- | --- | --- |
| Slot | 1, 1a, 1b | Enabled or disabled | 3 |
|  | 3 | Disabled | 2 |
|  | 4 | Enabled | 2 |
| Subslot | 4 | Disabled | 1 |

Table 5.5.2.3.1-3: ![](media_svg/image965.svg) [公式: Α]

| SPUCCH format |  | Frequency hopping | ![](media_svg/image966.svg) [公式: Α] |
| --- | --- | --- | --- |
| Slot | 1, 1a, 1b | Enabled or disabled | see ![](media_svg/image967.svg) [公式: Α~_{p}] in clause 5.4A.2 |
|  | 3 | Disabled | see ![](media_svg/image968.svg) [公式: Α~_{p}] for PUCCH format 3 in clause 5.5.2.2.1 and determining ![](media_svg/image930.svg) [公式≈: ^{n}oc,^{(}^{~}^{p}^{)}0] and ![](media_svg/image931.svg) [公式≈: ^{n}oc,^{(}^{~}^{p}1^{)}] in clause 5.4A.3.1 |
|  | 4 | Enabled | see ![](media_svg/image813.svg) [公式≈: ^{Α}Λ] for PUCCH format 4 in clause 5.5.2.2.1 |
| Subslot | 4 | Disabled | see ![](media_svg/image813.svg) [公式≈: ^{Α}Λ] for PUCCH format 4 in clause 5.5.2.2.1 |

##### 5.5.2.3.2 Mapping to physical resources

The sequence ![](media_svg/image969.svg) [公式≈: ^{r}PSUCCH^{(}^{~}^{p}^{)}^{(}^{∪}^{)}] shall be multiplied with the amplitude scaling factor ![](media_svg/image970.svg) [公式≈: ^{Β}SPUCCH] and mapped in sequence starting with ![](media_svg/image971.svg) [公式≈: ^{r}SPUCCH^{(}^{~}^{p}^{)}^{(}^{0}^{)}] to resource elements ![](media_svg/image972.svg) [公式: (k,l)] on antenna port ![](media_svg/image953.svg) [公式: p]. The mapping shall be in increasing order of first![](media_svg/image973.svg) [公式: k], then ![](media_svg/image3.svg) [公式: l]. The set of values for ![](media_svg/image2.svg) [公式: k] and the relation between the index ![](media_svg/image974.svg) [公式≈: ^{~}p] and the antenna port number ![](media_svg/image394.svg) [公式: p] shall be identical to the values used for the corresponding SPUCCH transmission. The values of the symbol index ![](media_svg/image3.svg) [公式: l] in a slot and a subslot are given by Table 5.5.2.3.2-1 and Table 5.5.2.3.2-2 respectively.

Table 5.5.2.3.2-1: Demodulation reference signal location for different slot-SPUCCH formats

| SPUCCH format | Frequency hopping | Slot | Set of values for ![](media_svg/image3.svg) [公式: l] |
| --- | --- | --- | --- |
| 1, 1a, 1b | Enabled | 1st | 1, 4, 5 |
|  |  | 2nd | 1, 2, 5 |
|  | Disabled | 1st and 2nd | 2, 3, 4 |
| 3 | Disabled | 1st and 2nd | 1, 5 |
| 4 | Enabled | 1st and 2nd | 1, 5 |

Table 5.5.2.3.2-2: Demodulation reference signal location for different subslot-SPUCCH formats

| SPUCCH format | Subslot number in subframe | Slot | ![](media_svg/image3.svg) [公式: l] |
| --- | --- | --- | --- |
| 4 | 0 | 1st | 0 |
|  | 1 | 1st | 3 |
|  | 2 | 1st | 5 |
|  | 3 | 2nd | 0 |
|  | 4 | 2nd | 2 |
|  | 5 | 2nd | 4 |

### 5.5.3 Sounding reference signal

Two types of sounding reference signals can be configured:

- basic sounding reference signal, supporting periodic or aperiodic transmission

- additional sounding reference signal, supporting aperiodic transmission only

Basic SRS corresponds to either SRS trigger type 0 or type 1 in clause 8.2 of [4]. Additional SRS corresponds to SRS trigger type 2 in clause 8.2 of [4].

#### 5.5.3.1 Sequence generation

##### 5.5.3.1.1 Sequence generation for basic SRS

The sounding reference signal sequence ![](media_svg/image975.svg) [公式≈: _{r}_{SRS}(~p)_{(}_{n}_{)}_{=}_{r}_{u}(_{,}Α_{v}~p,Δ)_{(}_{n}_{)}] is defined by clause 5.5.1, where ![](media_svg/image976.svg) [公式: u] is the sequence-group number defined in clause 5.5.1.3, ![](media_svg/image977.svg) [公式: Ν] is the base sequence number defined in clause 5.5.1.4, and ![](media_svg/image947.svg) [公式: Δ=0]. The cyclic shift ![](media_svg/image978.svg) [公式: Α~_{p}] of the sounding reference signal is given as

![](media_svg/image979.svg) [公式≈: ^{n}^{SRS}^{Α}^{cs}^{,}^{~}^{~}^{~}^{p}p^{p}⎰^{=}^{=}{^{⊇}^{⊕}^{⊕}^{⊗}^{2}0^{Π}^{n},1^{SRS}^{cs},...,^{n}^{n}^{SRS}^{cs,}^{SRS}^{cs}^{+}N^{max}^{,}^{~}^{p}^{n}_{ap}^{SRS}^{cs,}^{N}−^{max}^{ap}1}^{~}^{p}^{⇒}^{⇐}^{⇐}^{⇔}^{mod}^{n}^{SRS}^{cs,}^{max}],

where ![](media_svg/image980.svg) [公式≈: n_{SRS}^{cs}={0,1,...,n_{SRS}^{cs,}^{max}−1}] is configured separately for periodic and each configuration of aperiodic sounding by the higher-layer parameters cyclicShift and cyclicShift-ap, respectively, for each UE and ![](media_svg/image981.svg) [公式≈: ^{N}ap] is the number of antenna ports used for sounding reference signal transmission. The parameter ![](media_svg/image982.svg) [公式≈: _{n}_{SRS}cs,max_{=}_{8}] if ![](media_svg/image983.svg) [公式: K_{TC}=2] , otherwise ![](media_svg/image984.svg) [公式≈: _{n}_{SRS}cs,max_{=}_{12}]. The parameter ![](media_svg/image985.svg) [公式≈: ^{K}TC] is given by the higher layer parameter transmissionCombNum if configured, otherwise ![](media_svg/image983.svg) [公式: K_{TC}=2].

##### 5.5.3.1.2 Sequence generation for additional SRS

The sounding reference signal $ r_{SRS}^{(\hat {p})}\left ( n\right ) $ is defined by clause 5.5.3.1.1 with the following exceptions

- $ n_{SRS}^{cs}$ is given by the higher-layer parameter srs-CyclicShiftAdd

- $ N_{ap}$ is given by the higher-layer parameter srs-AntennaPortAdd

- $ K_{TC}$ is given by the higher-layer parameter srs-TransmissionCombNumAdd

- the function $ f_{gh}$ in clause 5.5.1.3 is given by

$$ f_{gh}\left ( n_{s},l\right ) ={\begin {matrix}0 & if group hopping is disabled \\ \left ( \sum  _{i=0}^{7}2^{i}c\left ( 8\left ( n_{s}N_{symb}^{UL}+l\right ) +i\right ) \right ) mod30 & if group hopping is enabled\end {matrix}$$

where $ l $ is the SC-FDMA symbol index within the slot $ n_{s}$ and $ N_{symb}^{UL}$ is the number of SC-FDMA symbols per slot

- the function $ v $ in clause 5.5.1.4 is given by

$$ v={\begin {matrix}c\left ( n_{s}N_{symb}^{UL}+l\right )  & if group hopping is disabled and sequence hopping is enabled \\ 0 & otherwise\end {matrix}$$

#### 5.5.3.2 Mapping to physical resources

##### 5.5.3.2.1 Mapping to physical resources for basic SRS

The sequence shall be multiplied with the amplitude scaling factor ![](media_svg/image986.svg) [公式≈: ^{Β}SRS] in order to conform to the transmit power ![](media_svg/image987.svg) [公式≈: ^{P}SRS] specified in clause 5.1.3.1 in TS36.213 [4], and mapped in sequence starting with ![](media_svg/image988.svg) [公式≈: r_{SRS}^{(}^{~}^{p}^{)}(0)] to resource elements ![](media_svg/image1.svg) [公式: (k,l)] on antenna port ![](media_svg/image989.svg) [公式: p] according to

![](media_svg/image990.svg) [公式≈: _{a}_{K}_{(}_{p}_{TC}_{)}_{k}_{&apos;}_{+}_{k}_{0}_{(}_{p}_{)}_{,}_{l}_{=}^{√}_{⌡}_{⌠}_{⌡}_{∞}_{0}_{N}^{1}_{ap}Β_{SRS}r_{SRS}^{(}^{~}^{p}^{)}(k&apos;)_{otherwise}k&apos;=0,1,κ,M_{sc}^{RS}_{,}_{b}−1]

where ![](media_svg/image981.svg) [公式≈: ^{N}ap] is the number of antenna ports used for sounding reference signal transmission and the relation between the index ![](media_svg/image991.svg) [公式≈: ^{~}p] and the antenna port ![](media_svg/image992.svg) [公式: p] is given by Table 5.2.1-1. The set of antenna ports used for sounding reference signal transmission is configured independently for periodic and each configuration of aperiodic sounding. The quantity ![](media_svg/image993.svg) [公式≈: _{k}_{0}(p)] is the frequency-domain starting position of the sounding reference signal and for ![](media_svg/image994.svg) [公式≈: ^{b}^{=}^{B}SRS] and ![](media_svg/image995.svg) [公式≈: ^{M}sc,^{RS}b] is the length of the sounding reference signal sequence defined as

![](media_svg/image996.svg) [公式≈: ^{M}sc,^{RS}b^{=}^{m}SRS,b^{N}sc^{RB}^{K}TC]

where ![](media_svg/image997.svg) [公式≈: ^{m}SRS,b]is given by Table 5.5.3.2-1 through Table 5.5.3.2-4 for each uplink bandwidth ![](media_svg/image998.svg) [公式≈: _{N}_{RB}UL]. The cell-specific parameter srs-BandwidthConfig, ![](media_svg/image999.svg) [公式: C_{SRS}⎰{0,1,2,3,4,5,6,7}] and the UE-specific parameter srs-Bandwidth, ![](media_svg/image1000.svg) [公式: B_{SRS}⎰{0,1,2,3}]are given by higher layers. For UpPTS, ![](media_svg/image1001.svg) [公式≈: ^{m}SRS,0] shall be reconfigured to ![](media_svg/image1002.svg) [公式≈: ^{m}SRS^{max},0^{=}^{max}c⎰C_{SRS}^{{}^{m}SRS^{c},0^{}}^{≥}^{(}^{N}RB^{UL}^{−}^{6}^{N}RA^{)}] if this reconfiguration is enabled by the cell-specific parameter srsMaxUpPts given by higher layers, otherwise if the reconfiguration is disabled ![](media_svg/image1003.svg) [公式≈: ^{m}SRS,0^{max}^{=}^{m}SRS,0],where ![](media_svg/image1004.svg) [公式: c] is a SRS BW configuration and ![](media_svg/image1005.svg) [公式≈: ^{C}SRS] is the set of SRS BW configurations from the Tables 5.5.3.2-1 to 5.5.3.2-4 for each uplink bandwidth ![](media_svg/image1006.svg) [公式≈: _{N}_{RB}UL], ![](media_svg/image1007.svg) [公式≈: ^{N}RA] is the number of format 4 PRACH in the addressed UpPTS and derived from Table 5.7.1-4.

The frequency-domain starting position ![](media_svg/image1008.svg) [公式≈: _{k}_{0}(p)] is defined by

![](media_svg/image1009.svg) [公式≈: ^{k}0^{(}^{p}^{)}^{=}^{k}0^{(}^{p}^{)}^{+}^{B}⊆_{b}^{SRS}_{=}_{0}^{`}^{K}TC^{M}sc,^{RS}b^{n}b]

where for normal uplink subframes ![](media_svg/image1010.svg) [公式≈: _{k}_{0}(p)] is defined by

![](media_svg/image1011.svg) [公式≈: k0^{(}^{p}^{)}=(√NRB^{UL}/2∃−mSRS,02)NSC^{RB}+kTC^{(}^{p}^{)}]

and for UpPTS by

![](media_svg/image1012.svg) [公式≈: _{k}_{0}(p)_{=}^{√}⌡_{⌠}_{⌡}_{∞}(_{k}N_{TC}_{(}_{p}RB^{UL}_{)}−mSRS,0^{max})Nsc^{RB}+kTC^{(}^{p}^{)}if_{otherwise}((nfmod2)∪(2−NSP)+nhf)mod2=0]

The quantity ![](media_svg/image1013.svg) [公式≈: k_{TC}^{(}^{p}^{)}⎰{0,1,...,K_{TC}−1}] is given by

![](media_svg/image1014.svg) [公式≈: _{k}_{TC}_{(}_{p}_{)}_{=}√_{⌠}_{∞}1_{k}-_{TC}k_{TC}if_{otherwise}n_{SRS}^{cs}⎰{4,5,6,7}and^{~}p⎰{1,3}andN_{ap}=4]

where the relation between the index ![](media_svg/image1015.svg) [公式≈: ^{~}p] and the antenna port ![](media_svg/image1016.svg) [公式: p] is given by Table 5.2.1-1, ![](media_svg/image1017.svg) [公式≈: kK_{TCTC}⎰−{0,1,...,1}] is given by the UE-specific parameter transmissionComb or transmissionComb-ap for periodic and each configuration of aperiodic transmission, respectively, provided by higher layers for the UE, and ![](media_svg/image1018.svg) [公式≈: ^{n}b] is frequency position index. The variable ![](media_svg/image1019.svg) [公式≈: ^{n}hf] is equal to 0 for UpPTS in the first half frame and equal to 1 for UpPTS in the second half frame of a radio frame.

The frequency hopping of the sounding reference signal is configured by the parameter ![](media_svg/image1020.svg) [公式: b_{hop}⎰{0,1,2,3}], provided by higher-layer parameter srs-HoppingBandwidth. Frequency hopping is not supported for aperiodic transmission, except for additional SRS. If frequency hopping of the sounding reference signal is not enabled (i.e., ![](media_svg/image1021.svg) [公式≈: ^{b}hop^{÷}^{B}SRS]), the frequency position index ![](media_svg/image1018.svg) [公式≈: ^{n}b] remains constant (unless re-configured) and is defined by ![](media_svg/image1022.svg) [公式≈: ^{n}b^{=}√^{4}^{n}RRC^{m}SRS,b∃^{mod}^{N}b] where the parameter ![](media_svg/image1023.svg) [公式≈: ^{n}RRC] is given by higher-layer parameters freqDomainPosition and freqDomainPosition-ap for periodic and each configuration of aperiodic transmission, respectively. If frequency hopping of the sounding reference signal is enabled (i.e., ![](media_svg/image1024.svg) [公式≈: ^{b}hop^{<}^{B}SRS]), the frequency position indexes ![](media_svg/image1018.svg) [公式≈: ^{n}b] are defined by

![](media_svg/image1025.svg) [公式≈: _{n}_{b}_{=}√_{⌠}_{∞}_{{}_{F}_{b}_{(}_{n}_{SRS}√4n_{)}RRC_{+}_{√}_{4}_{n}m_{RRC}SRS,b_{m}∃_{SRS,}mod_{b}_{∃}N_{}}_{mod}b_{N}_{b}_{otherwise}b≥bhop]

where ![](media_svg/image1026.svg) [公式≈: ^{N}b] is given by Table 5.5.3.2-1 through Table 5.5.3.2-4 for each uplink bandwidth ![](media_svg/image1027.svg) [公式≈: _{N}_{RB}UL],

![](media_svg/image1028.svg) [公式≈: Fb(nSRS)=^{√}^{⌡}^{⌡}⌠_{⌡}_{⌡}_{∞}^{(}^{N}^{b}^{/}^{2}^{)}^{⋅}^{⋅}⋅_{√}^{n}^{SRS}π^{mod}_{√}^{b}b_{N}&apos;^{−}=^{1}_{b}b^{π}_{hop}_{/}_{2}^{b}^{b}N^{&apos;}_{∃}^{=}^{b}_{√}b_{n}^{hop}&apos;_{SRS}^{N}^{b}_{/}^{&apos;}_{π}^{∂}^{∂}∂_{∃}^{+}_{b}_{b}_{&apos;}_{−}_{=}^{⋅}^{⋅}⋅_{√}_{1}_{b}^{n}_{hop}^{SRS}_{N}2_{b}^{mod}π_{&apos;}_{∃}^{b}b&apos;^{−}=^{1}^{π}b_{hop}^{b}^{b}^{&apos;}^{=}N^{b}^{hop}b&apos;^{N}^{b}^{&apos;}^{∂}^{∂}∂_{∃}^{if}_{if}^{N}_{N}^{b}_{b}^{even }_{odd}]

where ![](media_svg/image1029.svg) [公式: N_{b}_{hop}=1] regardless of the ![](media_svg/image1026.svg) [公式≈: ^{N}b] value on Table .2-1 through Table 5.5.3.2-4, and

![](media_svg/image1030.svg) [公式≈: _{n}_{SRS}_{=}^{√}⌡⌡_{⌠}_{⌡}_{⌡}_{∞}2_{√}_{(}N_{n}_{f}SP_{≠}n_{10}f+_{+}2_{√}(_{n}N_{s}SP_{/}_{2}_{∃}−_{)}1_{/})_{T}^{⋅}⋅_{√}_{SRS}_{10}^{n}^{s}^{∂}∂_{∃}_{∃}_{,}+^{⋅}⋅_{⋅}_{√}_{T}_{offset_max}^{T}^{offset}^{∂}∂_{∂}_{∃},_{otherwise}for 2msSRSperiodicity offramestructure type2]

counts the number of UE-specific SRS transmissions, where ![](media_svg/image1031.svg) [公式≈: ^{T}SRS] is UE-specific periodicity of SRS transmission defined in clause 8.2 of TS36.213[4], ![](media_svg/image1032.svg) [公式≈: ^{T}offset] is SRS subframe offset defined in Table 8.2-2 of TS36.213[4] and ![](media_svg/image1033.svg) [公式≈: ^{T}offset_max] is the maximum value of ![](media_svg/image1032.svg) [公式≈: ^{T}offset] for a certain configuration of SRS subframe offset.

The sounding reference signal shall be transmitted in the last symbol of the uplink subframe.

Table 5.5.3.2-1: ![](media_svg/image1034.svg) [公式≈: ^{m}SRS,b] and ![](media_svg/image1035.svg) [公式≈: ^{N}b], ![](media_svg/image1036.svg) [公式: b=0,1,2,3], values for the uplink bandwidth of ![](media_svg/image1037.svg) [公式: 6≥N_{RB}^{UL}≥40]

| SRS bandwidth configuration![](media_svg/image1038.svg) [公式≈: ^{C}SRS] | SRS-Bandwidth ![](media_svg/image1039.svg) [公式: B_{SRS}=0] |  | SRS-Bandwidth ![](media_svg/image1040.svg) [公式: B_{SRS}=1] |  | SRS-Bandwidth ![](media_svg/image1041.svg) [公式: B_{SRS}=2] |  | SRS-Bandwidth ![](media_svg/image1042.svg) [公式: B_{SRS}=3] |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | ![](media_svg/image1043.svg) [公式≈: ^{m}SRS,0] | ![](media_svg/image1044.svg) [公式≈: ^{N}0] | ![](media_svg/image1045.svg) [公式≈: ^{m}SRS,1] | ![](media_svg/image1046.svg) [公式≈: ^{N}1] | ![](media_svg/image1047.svg) [公式≈: ^{m}SRS,2] | ![](media_svg/image1048.svg) [公式≈: ^{N}2] | ![](media_svg/image1049.svg) [公式≈: ^{m}SRS,3] | ![](media_svg/image1050.svg) [公式≈: ^{N}3] |
| 0 | 36 | 1 | 12 | 3 | 4 | 3 | 4 | 1 |
| 1 | 32 | 1 | 16 | 2 | 8 | 2 | 4 | 2 |
| 2 | 24 | 1 | 4 | 6 | 4 | 1 | 4 | 1 |
| 3 | 20 | 1 | 4 | 5 | 4 | 1 | 4 | 1 |
| 4 | 16 | 1 | 4 | 4 | 4 | 1 | 4 | 1 |
| 5 | 12 | 1 | 4 | 3 | 4 | 1 | 4 | 1 |
| 6 | 8 | 1 | 4 | 2 | 4 | 1 | 4 | 1 |
| 7 | 4 | 1 | 4 | 1 | 4 | 1 | 4 | 1 |

Table 5.5.3.2-2: ![](media_svg/image1051.svg) [公式≈: ^{m}SRS,b] and ![](media_svg/image1052.svg) [公式≈: ^{N}b], ![](media_svg/image1053.svg) [公式: b=0,1,2,3], values for the uplink bandwidth of ![](media_svg/image1054.svg) [公式: 40<N_{RB}^{UL}≥60]

| SRS bandwidth configuration![](media_svg/image1038.svg) [公式≈: ^{C}SRS] | SRS-Bandwidth ![](media_svg/image1055.svg) [公式: B_{SRS}=0] |  | SRS-Bandwidth ![](media_svg/image1056.svg) [公式: B_{SRS}=1] |  | SRS-Bandwidth ![](media_svg/image1057.svg) [公式: B_{SRS}=2] |  | SRS-Bandwidth ![](media_svg/image1058.svg) [公式: B_{SRS}=3] |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | ![](media_svg/image1059.svg) [公式≈: ^{m}SRS,0] | ![](media_svg/image1060.svg) [公式≈: ^{N}0] | ![](media_svg/image1061.svg) [公式≈: ^{m}SRS,1] | ![](media_svg/image1062.svg) [公式≈: ^{N}1] | ![](media_svg/image1063.svg) [公式≈: ^{m}SRS,2] | ![](media_svg/image1064.svg) [公式≈: ^{N}2] | ![](media_svg/image1065.svg) [公式≈: ^{m}SRS,3] | ![](media_svg/image1066.svg) [公式≈: ^{N}3] |
| 0 | 48 | 1 | 24 | 2 | 12 | 2 | 4 | 3 |
| 1 | 48 | 1 | 16 | 3 | 8 | 2 | 4 | 2 |
| 2 | 40 | 1 | 20 | 2 | 4 | 5 | 4 | 1 |
| 3 | 36 | 1 | 12 | 3 | 4 | 3 | 4 | 1 |
| 4 | 32 | 1 | 16 | 2 | 8 | 2 | 4 | 2 |
| 5 | 24 | 1 | 4 | 6 | 4 | 1 | 4 | 1 |
| 6 | 20 | 1 | 4 | 5 | 4 | 1 | 4 | 1 |
| 7 | 16 | 1 | 4 | 4 | 4 | 1 | 4 | 1 |

Table 5.5.3.2-3: ![](media_svg/image1067.svg) [公式≈: ^{m}SRS,b] and ![](media_svg/image1068.svg) [公式≈: ^{N}b], ![](media_svg/image1069.svg) [公式: b=0,1,2,3], values for the uplink bandwidth of ![](media_svg/image1070.svg) [公式: 60<N_{RB}^{UL}≥80]

| SRS bandwidth configuration![](media_svg/image1038.svg) [公式≈: ^{C}SRS] | SRS-Bandwidth ![](media_svg/image1071.svg) [公式: B_{SRS}=0] |  | SRS-Bandwidth ![](media_svg/image1072.svg) [公式: B_{SRS}=1] |  | SRS-Bandwidth ![](media_svg/image1073.svg) [公式: B_{SRS}=2] |  | SRS-Bandwidth ![](media_svg/image1074.svg) [公式: B_{SRS}=3] |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | ![](media_svg/image1075.svg) [公式≈: ^{m}SRS,0] | ![](media_svg/image1076.svg) [公式≈: ^{N}0] | ![](media_svg/image1077.svg) [公式≈: ^{m}SRS,1] | ![](media_svg/image1078.svg) [公式≈: ^{N}1] | ![](media_svg/image1079.svg) [公式≈: ^{m}SRS,2] | ![](media_svg/image1080.svg) [公式≈: ^{N}2] | ![](media_svg/image1081.svg) [公式≈: ^{m}SRS,3] | ![](media_svg/image1082.svg) [公式≈: ^{N}3] |
| 0 | 72 | 1 | 24 | 3 | 12 | 2 | 4 | 3 |
| 1 | 64 | 1 | 32 | 2 | 16 | 2 | 4 | 4 |
| 2 | 60 | 1 | 20 | 3 | 4 | 5 | 4 | 1 |
| 3 | 48 | 1 | 24 | 2 | 12 | 2 | 4 | 3 |
| 4 | 48 | 1 | 16 | 3 | 8 | 2 | 4 | 2 |
| 5 | 40 | 1 | 20 | 2 | 4 | 5 | 4 | 1 |
| 6 | 36 | 1 | 12 | 3 | 4 | 3 | 4 | 1 |
| 7 | 32 | 1 | 16 | 2 | 8 | 2 | 4 | 2 |

Table 5.5.3.2-4: ![](media_svg/image1083.svg) [公式≈: ^{m}SRS,b]and![](media_svg/image1084.svg) [公式≈: ^{N}b], ![](media_svg/image1085.svg) [公式: b=0,1,2,3], values for the uplink bandwidth of ![](media_svg/image1086.svg) [公式: 80<N_{RB}^{UL}≥110]

| SRS bandwidth configuration![](media_svg/image1038.svg) [公式≈: ^{C}SRS] | SRS-Bandwidth ![](media_svg/image1087.svg) [公式: B_{SRS}=0] |  | SRS-Bandwidth ![](media_svg/image1088.svg) [公式: B_{SRS}=1] |  | SRS-Bandwidth ![](media_svg/image1089.svg) [公式: B_{SRS}=2] |  | SRS-Bandwidth ![](media_svg/image1090.svg) [公式: B_{SRS}=3] |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | ![](media_svg/image1091.svg) [公式≈: ^{m}SRS,0] | ![](media_svg/image1092.svg) [公式≈: ^{N}0] | ![](media_svg/image1093.svg) [公式≈: ^{m}SRS,1] | ![](media_svg/image1094.svg) [公式≈: ^{N}1] | ![](media_svg/image1095.svg) [公式≈: ^{m}SRS,2] | ![](media_svg/image1096.svg) [公式≈: ^{N}2] | ![](media_svg/image1097.svg) [公式≈: ^{m}SRS,3] | ![](media_svg/image1098.svg) [公式≈: ^{N}3] |
| 0 | 96 | 1 | 48 | 2 | 24 | 2 | 4 | 6 |
| 1 | 96 | 1 | 32 | 3 | 16 | 2 | 4 | 4 |
| 2 | 80 | 1 | 40 | 2 | 20 | 2 | 4 | 5 |
| 3 | 72 | 1 | 24 | 3 | 12 | 2 | 4 | 3 |
| 4 | 64 | 1 | 32 | 2 | 16 | 2 | 4 | 4 |
| 5 | 60 | 1 | 20 | 3 | 4 | 5 | 4 | 1 |
| 6 | 48 | 1 | 24 | 2 | 12 | 2 | 4 | 3 |
| 7 | 48 | 1 | 16 | 3 | 8 | 2 | 4 | 2 |

##### 5.5.3.2.2 Mapping to physical resources for additional SRS

An additional SRS spans one or more SC-FDMA symbols in the time domain, where

- the starting SC-FDMA symbol $ l_{0}$ within the subframe is given by the higher-layer parameter srs-StartPosAdd;

- the duration $ N $ in number of SC-FDMA symbols, including potential guard symbols, is given by the higher-layer parameter srs-DurationAdd.

Mapping to physical resources shall be done according to clause 5.5.3.2.1 with the following exceptions:

- frequency hopping between SC-FDMA symbols is supported and if a UE is configured by higher layer parameter srs-GuardSymbolFH-Add, a guard symbol is added between every frequency hop;

- antenna switching within a subframe is supported and if a UE is configured by higher layer parameter srs-GuardSymbolAS-Add, a guard symbol is added between every antenna switching;

- $ n_{SRS}=\lfloor  \frac {l'}{R}\rfloor  $ where $ l'$ is the additional SRS transmission number not counting guard symbol(s) within the subframe with $ l^{'}=0 $ corresponding to the starting SC-FDMA symbol $ l_{0}$, and $ R\in  \left \{ 1,2,3,4,6,7,8,9,12,13\right \} $ is the repetition factor given by the higher-layer parameter srs-RepNumAdd;

- $ B_{SRS}$ is given by the higher-layer parameter srs-BandwidthAdd;

- $ b_{hop}$ is given by the higher-layer parameter srs-HoppingBandwidthAdd;

- $ N_{FH}$ is the number of frequency hops with the same antenna/antenna pair for additional SRS, derived from $ N=RN_{FH}+\left ( N_{FH}-1\right ) G_{FH}$ if antenna switching is not configured for additional SRS, and from $ N=RN_{AS}N_{FH}+\left ( N_{AS}-1\right ) G_{AS}+\left ( N_{FH}-1\right ) N_{AS}G_{FH}+\left ( N_{AS}-1\right ) (1-G_{AS})G_{FH}$ if antenna switching is configured for additional SRS, where $ R $ is the repetition factor given by the higher-layer parameter srs-RepNumAdd, $ N_{AS}$ is the number of antenna switches for additional SRS defined in 8.2 of [4], $ G_{AS}\in  \left \{ 0, 1\right \} $ is the guard-symbol configuration for antenna switching given by the higher-layer parameter srs-GuardSymbolAS, $ G_{FH}\in  \left \{ 0, 1\right \} $ is the guard symbol configuration for frequency hopping given by the higher-layer parameter srs-GuardSymbolFH, and $ N $ is given by the higher-layer parameter srs-DurationAdd;

- $ n_{RRC}$ is given by the higher-layer parameter srs-FreqDomainPosAdd;

- $ N_{ap}$ is given by the higher-layer parameter srs-AntennaPortAdd;

- $ n_{SRS}^{cs}$ is given by the higher-layer parameter srs-CyclicShiftAdd;

- $ K_{TC}$ is given by the higher-layer parameter srs-TransmissionCombNumAdd;

- $\hat {k}_{TC}$ is given by the higher-layer parameter srs-TransmissionCombAdd.

#### 5.5.3.3 Sounding reference signal subframe configuration

The cell-specific subframe configuration period ![](media_svg/image1099.svg) [公式≈: ^{T}SFC] and the cell-specific subframe offset ![](media_svg/image1100.svg) [公式≈: ^{δ}SFC] for the transmission of sounding reference signals are listed in Tables 5.5.3.3-1 and 5.5.3.3-2, for frame structures type 1 and 2 respectively, where the parameter srs-SubframeConfig is provided by higher layers. Sounding reference signal subframes are the subframes satisfying![](media_svg/image1101.svg) [公式≈: √^{n}s^{/}^{2}∃^{mod}^{T}SFC^{⎰}^{δ}SFC]. For frame structure type 2, a sounding reference signal is transmitted only in uplink subframes or UpPTS.

Table 5.5.3.3-1: Frame structure type 1 sounding reference signal subframe configuration

| srs-SubframeConfig | Binary | Configuration Period ![](media_svg/image1102.svg) [公式≈: ^{T}SFC] (subframes) | Transmission offset  ![](media_svg/image1103.svg) [公式≈: ^{δ}SFC] (subframes) |
| --- | --- | --- | --- |
| 0 | 0000 | 1 | {0} |
| 1 | 0001 | 2 | {0} |
| 2 | 0010 | 2 | {1} |
| 3 | 0011 | 5 | {0} |
| 4 | 0100 | 5 | {1} |
| 5 | 0101 | 5 | {2} |
| 6 | 0110 | 5 | {3} |
| 7 | 0111 | 5 | {0,1} |
| 8 | 1000 | 5 | {2,3} |
| 9 | 1001 | 10 | {0} |
| 10 | 1010 | 10 | {1} |
| 11 | 1011 | 10 | {2} |
| 12 | 1100 | 10 | {3} |
| 13 | 1101 | 10 | {0,1,2,3,4,6,8} |
| 14 | 1110 | 10 | {0,1,2,3,4,5,6,8} |
| 15 | 1111 | reserved | reserved |

Table 5.5.3.3-2: Frame structure type 2 sounding reference signal subframe configuration

| srs-SubframeConfig | Binary | Configuration Period ![](media_svg/image1102.svg) [公式≈: ^{T}SFC] (subframes) | Transmission offset ![](media_svg/image1104.svg) [公式≈: ^{δ}SFC] (subframes) |
| --- | --- | --- | --- |
| 0 | 0000 | 5 | {1} |
| 1 | 0001 | 5 | {1, 2} |
| 2 | 0010 | 5 | {1, 3} |
| 3 | 0011 | 5 | {1, 4} |
| 4 | 0100 | 5 | {1, 2, 3} |
| 5 | 0101 | 5 | {1, 2, 4} |
| 6 | 0110 | 5 | {1, 3, 4} |
| 7 | 0111 | 5 | {1, 2, 3, 4} |
| 8 | 1000 | 10 | {1, 2, 6} |
| 9 | 1001 | 10 | {1, 3, 6} |
| 10 | 1010 | 10 | {1, 6, 7} |
| 11 | 1011 | 10 | {1, 2, 6, 8} |
| 12 | 1100 | 10 | {1, 3, 6, 9} |
| 13 | 1101 | 10 | {1, 4, 6, 7} |
| 14 | 1110 | reserved | reserved |
| 15 | 1111 | reserved | reserved |

## 5.6 SC-FDMA baseband signal generation

This clause applies to all uplink physical signals and uplink physical channels except the physical random access channel and PUSCH using sub-PRB allocations for BL/CE UEs.

The time-continuous signal ![](media_svg/image1105.svg) [公式≈: s_{l}^{(}^{p}^{)}(t)] for antenna port ![](media_svg/image1106.svg) [公式: p] in SC-FDMA symbol ![](media_svg/image3.svg) [公式: l] in an uplink slot is defined by

![](media_svg/image1107.svg) [公式≈: _{s}_{l}(p)_{(}_{t}_{)}_{=}_{k}^{⊥}^{N}_{=}_{−}^{RB}^{UL}_{√}_{N}^{N}_{⊆}_{RB}_{UL}^{sc}^{RB}_{N}^{/}_{sc}^{2}_{RB}^{∀}_{/}^{−}_{2}^{1}_{∃}_{a}_{k}(_{(}p_{−})_{)}_{,}_{l}_{∪}_{e}j2Π(k+12)δf(t−NCP,lTs)]

for![](media_svg/image1108.svg) [公式≈: 0≥t<(N_{CP}_{,}_{l}+N)≠T_{s}] where ![](media_svg/image1109.svg) [公式≈: k^{(}^{−}^{)}=k+√N^{UL}RBNsc^{RB}2∃], ![](media_svg/image1110.svg) [公式: N=2048], ![](media_svg/image1111.svg) [公式: δf=15kHz] and ![](media_svg/image1112.svg) [公式≈: _{a}_{k}(_{,}p_{l})] is the content of resource element ![](media_svg/image204.svg) [公式: (k,l)] on antenna port ![](media_svg/image1113.svg) [公式: p].

For frame structure type 3, if the associated DCI indicates PUSCH starting position other than '00' or if 'autonomous PUSCH' is configured, ![](media_svg/image1114.svg) [公式≈: s_{l}^{(}^{p}^{)}(t),l=0] is given by

![](media_svg/image1115.svg) [公式≈: ^{s}^{0}^{(}^{p}^{)}^{(}^{t}^{)}^{=}^{√}^{⌡}^{⌠}⌡∞^{0}−s1^{(}^{p}^{)}(t−NCP,0Ts)^{0}N^{≥}start^{FS3}^{t}T^{<}s^{N}≥^{start}^{FS3}t<^{T}(^{s}NCP,0+N)Ts]

where

![](media_svg/image1116.svg) [公式≈: N_{start}^{FS3}=^{√}^{⌡}_{⌠}_{⌡}_{∞}^{768}768_{N}_{CP}_{,}+_{0}_{+}N_{N}_{TA}^{if}if_{if}^{ the} the_{ the}^{associated}associated_{associated}^{DCI}DCI_{DCI}^{indicates}indicates_{indicates}^{PUSCH}PUSCH_{PUSCH}^{starting}starting_{starting}^{position }position _{position }^{&apos;01&apos;}&apos;10&apos;_{&apos;11&apos;}]

and were  is given by TS36.213 [4] if 'autonomous PUSCH' is configured.

The quantity ![](media_svg/image1118.svg) [公式≈: ^{N}TA] is given by clause 8.1. The UE behaviour if ![](media_svg/image1119.svg) [公式≈: ^{N}start^{FS3}^{>}^{N}CP,0^{+}^{N}] is undefined.

The SC-FDMA symbols in a slot shall be transmitted in increasing order of ![](media_svg/image3.svg) [公式: l], starting with ![](media_svg/image1120.svg) [公式: l=0], where SC-FDMA symbol ![](media_svg/image1121.svg) [公式: l>0]starts at time ![](media_svg/image1122.svg) [公式≈: ⊆^{l}_{l}_{±}^{−}_{=}^{1}_{0}^{(}^{N}CP,l±^{+}^{N}^{)}^{T}s] within the slot.

Table 5.6-1 lists the values of ![](media_svg/image39.svg) [公式≈: ^{N}CP,l]that shall be used.

Table 5.6-1: SC-FDMA parameters

| Configuration | Cyclic prefix length ![](media_svg/image39.svg) [公式≈: ^{N}CP,l] |
| --- | --- |
| Normal cyclic prefix | ![](media_svg/image1123.svg) [公式: 160for  l=0]![](media_svg/image1124.svg) [公式: 144for  l=1,2,...,6] |
| Extended cyclic prefix | ![](media_svg/image1125.svg) [公式: 512for  l=0,1,...,5] |

## 5.6A SC-FDMA baseband signal generation for PUSCH using sub-PRB allocations

### 5.6A.1 Modulation schemes other than π/2-BPSK

For , the time-continuous signal  for antenna port  in SC-FDMA symbol  in an uplink slot is defined by clause 5.6 with  replaced by .

### 5.6A.2 Modulation scheme π/2-BPSK

For $ M_{sc}^{RU}=3 $ and π/2-BPSK modulation only 2-of-3 adjacent subcarriers are selected as described in 5.5.2.1A.2. The time-continuous signal  in SC-FDMA symbol  in an uplink slot is defined by

![](media_svg/image1129.svg) [公式≈: _{staee}_{staee}^{ststst}_{sc2}_{sc1}^{kl}^{,sc1sc2}_{kkM}^{()()()}_{()}_{()}_{()UL}_{−}^{=+}_{=}_{=}_{=+}_{kl}_{kl}_{()}_{()}_{−}_{−}_{⋅∂}_{√∃}_{,}_{+}_{1,}jjkftNTΦΠ_{sc}kll_{jjkftNT},CP,s_{ΦΠ}_{kll}_{,CP,s}_{2}2(12)()_{2(32)()}+δ−_{+δ−}]

for  where , ,  is given by Table 5.6-1, and ![](media_svg/image1131.svg) [公式≈: ^{a}_{kl}()−_{,}]$ a_{k,l}$ and ![](media_svg/image1132.svg) [公式≈: ^{a}kl^{()}^{−}+1,] are respectively the modulation value for subcarrier index ![](media_svg/image1133.svg) [公式≈: _{k}()−] and $ k+1 $![](media_svg/image1134.svg) [公式≈: _{k}()−_{+}_{1}] for symbol , and the values of ![](media_svg/image1136.svg) [公式: k] used on ![](media_svg/image1137.svg) [公式: st_{sc1}()] and ![](media_svg/image1138.svg) [公式: st_{sc2}()] are respectively obtained by subtracting ![](media_svg/image1139.svg) [公式: ⋅∂_{√∃}M_{sc}^{UL}2] from the resulting set of allocated subcarriers as described in Table 8.1.6-1 of [4], and ![](media_svg/image1133.svg) [公式≈: _{k}()−] represents the lower subcarrier index among the selected subcarriers and ![](media_svg/image1140.svg) [公式≈: _{k}()−_{+}_{1}] is the subcarrier index adjacent to it. The phase rotation  is given by

$$\varphi  =\frac {\pi  }{2}\left ( \hat {l}mod 2\right ) +\varphi  _{avg_{k}}\left ( \hat {l}\right ) $$

$$\varphi  _{avg_{k}}\left ( \hat {l}\right ) =\varphi  _{avg_{k}}\left ( \hat {l}-1\right ) +2\pi  \Delta  f\left ( k+1\right ) \left ( N+N_{CP,l}\right ) T_{s}when\hat {l}>0 $$

$$\varphi  _{avg_{k}}\left ( 0\right ) =0 $$

$$\hat {l}=0,1,\ldots  ,N_{TB}N_{rep}^{PUSCH}M_{RU}M_{slots}^{UL}M_{symb}^{UL}-1 $$

$$ l=\hat {l}modM_{symb}^{UL}$$

where $ N_{TB}$ is the number of transport blocks defined in clause 8.0 of TS 36.213 [4]. If $ N_{TB}$ >1 and interleaving between codewords is applied according to clause 8.0 of TS 36.213 [4], then the symbol counter ![](media_svg/image1142.svg) [公式≈: ^{~}l] is reset at the start of the first PUSCH codeword transmission and incremented for each symbol during the transmission of the $ N_{TB}$ PUSCH codewords. For other cases, the symbol counter ![](media_svg/image1142.svg) [公式≈: ^{~}l] is reset at the start of each PUSCH codeword transmission and incremented for each symbol during the transmission of the PUSCH codeword.

The SC-FDMA symbols in a slot shall be transmitted in increasing order of , starting with , where SC-FDMA symbol  starts at time  within the slot.

## 5.7 Physical random access channel

### 5.7.1 Time and frequency structure

The physical layer random access preamble, illustrated in Figure 5.7.1-1, consists of a cyclic prefix of length![](media_svg/image1144.svg) [公式≈: ^{T}CP] and a sequence part of length![](media_svg/image1145.svg) [公式≈: ^{T}SEQ]. The parameter values are listed in Table 5.7.1-1 and depend on the frame structure and the random access configuration. Higher layers control the preamble format.

![](media/image1146.emf)

Figure 5.7.1-1: Random access preamble format

Table 5.7.1-1: Random access preamble parameters

| Preamble format | ![](media_svg/image1144.svg) [公式≈: ^{T}CP] | ![](media_svg/image1145.svg) [公式≈: ^{T}SEQ] |
| --- | --- | --- |
| 0 | ![](media_svg/image1147.svg) [公式: 3168∪T_{s}] | ![](media_svg/image1148.svg) [公式: 24576∪T_{s}] |
| 1 | ![](media_svg/image1149.svg) [公式: 21024∪T_{s}] | ![](media_svg/image1150.svg) [公式: 24576∪T_{s}] |
| 2 | ![](media_svg/image1151.svg) [公式: 6240∪T_{s}] | ![](media_svg/image1152.svg) [公式: 2∪24576∪T_{s}] |
| 3 | ![](media_svg/image1153.svg) [公式: 21024∪T_{s}] | ![](media_svg/image1154.svg) [公式: 2∪24576∪T_{s}] |
| 4 (see Note) | ![](media_svg/image1155.svg) [公式: 448∪T_{s}] | ![](media_svg/image1156.svg) [公式: 4096∪T_{s}] |
| NOTE: Frame structure type 2 and special subframe configurations with UpPTS lengths ![](media_svg/image1157.svg) [公式: 4384∪T_{s}]and ![](media_svg/image1158.svg) [公式: 5120∪T_{s}]only assuming that the number of additional SC-FDMA symbols in UpPTS X in Table 4.2-1 is 0. |  |  |

The transmission of a random access preamble, if triggered by the MAC layer, is restricted to certain time and frequency resources. These resources are enumerated in increasing order of the subframe number within the radio frame and the physical resource blocks in the frequency domain such that index 0 correspond to the lowest numbered physical resource block and subframe within the radio frame. PRACH resources within the radio frame are indicated by a PRACH configuration index, where the indexing is in the order of appearance in Table 5.7.1-2 and Table 5.7.1-4.

For non-BL/CE UEs there are up to two PRACH configurations in a cell. The first PRACH configuration is configured by higher layers with a PRACH configuration index (prach-ConfigurationIndex) and a PRACH frequency offset ![](media_svg/image1159.svg) [公式≈: ^{n}PRB^{RA}offset] (prach-FrequencyOffset). The second PRACH configuration (if any) is configured by higher layers with a PRACH configuration index (prach-ConfigurationIndexHighSpeed) and a PRACH frequency offset ![](media_svg/image1159.svg) [公式≈: ^{n}PRB^{RA}offset] (prach-FrequencyOffsetHighSpeed).

For BL/CE UEs, for each PRACH coverage enhancement level, there is a PRACH configuration configured by higher layers with a PRACH configuration index (prach-ConfigurationIndex), a PRACH frequency offset ![](media_svg/image1160.svg) [公式≈: ^{n}PRBoffset^{RA}] (prach-FrequencyOffset), a number of PRACH repetitions per attempt ![](media_svg/image73.svg) [公式≈: _{N}_{rep}PRACH] (numRepetitionPerPreambleAttempt) and optionally a PRACH starting subframe periodicity ![](media_svg/image75.svg) [公式≈: _{N}_{start}PRACH] (prach-StartingSubframe). PRACH of preamble format 0-3 is transmitted ![](media_svg/image1161.svg) [公式≈: _{N}_{rep}PRACH_{÷}_{1}] times, whereas PRACH of preamble format 4 is transmitted one time only.

For BL/CE UEs and for each PRACH coverage enhancement level, if frequency hopping is enabled for a PRACH configuration by the higher-layer parameter prach-HoppingConfig, the value of the parameter ![](media_svg/image1162.svg) [公式≈: ^{n}PRB^{RA}offset] depends on the SFN and the PRACH configuration index and is given by

- In case the PRACH configuration index is such that a PRACH resource occurs in every radio frame when calculated as below from Table 5.7.1-2 or Table 5.7.1-4,

![](media_svg/image1163.svg) [公式≈: ^{n}^{PRB}^{RA}^{offset}^{=}^{√}^{⌡}^{⌠}⌡_{∞}(^{n}n^{PRB}^{RA}PRB^{RA}^{offset}offset+fPRB,^{PRACH}hop)modNRB^{UL}^{if}if^{n}n^{f}f^{mod}mod^{2}2^{=}=1^{0}]

- otherwise

![](media_svg/image1164.svg) [公式≈: ^{n}^{PRB}^{RA}^{offset}^{=}^{√}^{⌡}^{⌡}^{⌠}^{⌡}_{⌡}_{∞}^{(}^{n}^{n}^{PRB}^{RA}PRB^{RA}^{offset}offset^{+}^{f}PRB,^{PRACH}hop^{)}^{mod}^{N}RB^{UL}^{if}^{if}^{⋅}^{⋅}^{√}^{⋅}⋅_{√}^{n}^{n}^{f}^{f}^{mod}^{mod}^{2}_{2}^{4}^{4}^{∂}^{∂}^{∃}^{∂}∂_{∃}^{=}^{=}^{1}^{0}]

where ![](media_svg/image1165.svg) [公式≈: ^{n}f] is the system frame number corresponding to the first subframe for each PRACH repetition, ![](media_svg/image10.svg) [公式≈: ^{f}PRB,^{PRACH}hop] corresponds to a cell-specific higher-layer parameter prach-HoppingOffset. If frequency hopping is not enabled for the PRACH configuration then ![](media_svg/image1166.svg) [公式≈: ^{n}PRB^{RA}offset^{=}^{n}PRB^{RA}offset].

For frame structure type 1 with preamble format 0-3, for each of the PRACH configurations there is at most one random access resource per subframe. 
Table 5.7.1-2 lists the preamble formats according to Table 5.7.1-1 and the subframes in which random access preamble transmission is allowed for a given configuration in frame structure type 1. The start of the random access preamble shall be aligned with the start of the corresponding uplink subframe at the UE assuming ![](media_svg/image1167.svg) [公式: N_{TA}=0], where ![](media_svg/image1168.svg) [公式≈: ^{N}TA] is defined in clause 8.1. For PRACH configurations 0, 1, 2, 15, 16, 17, 18, 31, 32, 33, 34, 47, 48, 49, 50 and 63 the UE may for handover purposes assume an absolute value of the relative time difference between radio frame ![](media_svg/image1169.svg) [公式: i] in the current cell and the target cell of less than ![](media_svg/image1170.svg) [公式: 153600∪T_{s}]. 
The first physical resource block ![](media_svg/image1171.svg) [公式≈: ^{n}PRB^{RA}] allocated to the PRACH opportunity considered for preamble formats 0, 1, 2 and 3 is defined as ![](media_svg/image1172.svg) [公式≈: ^{n}PRB^{RA}^{=}^{n}PRB^{RA}offset].

Table 5.7.1-2: Frame structure type 1 random access configuration for preamble formats 0-3

| PRACH ConfigurationIndex | Preamble Format | System frame number | Subframe number | PRACH ConfigurationIndex | Preamble Format | System frame number | Subframe number |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | Even | 1 | 32 | 2 | Even | 1 |
| 1 | 0 | Even | 4 | 33 | 2 | Even | 4 |
| 2 | 0 | Even | 7 | 34 | 2 | Even | 7 |
| 3 | 0 | Any | 1 | 35 | 2 | Any | 1 |
| 4 | 0 | Any | 4 | 36 | 2 | Any | 4 |
| 5 | 0 | Any | 7 | 37 | 2 | Any | 7 |
| 6 | 0 | Any | 1, 6 | 38 | 2 | Any | 1, 6 |
| 7 | 0 | Any | 2 ,7 | 39 | 2 | Any | 2 ,7 |
| 8 | 0 | Any | 3, 8 | 40 | 2 | Any | 3, 8 |
| 9 | 0 | Any | 1, 4, 7 | 41 | 2 | Any | 1, 4, 7 |
| 10 | 0 | Any | 2, 5, 8 | 42 | 2 | Any | 2, 5, 8 |
| 11 | 0 | Any | 3, 6, 9 | 43 | 2 | Any | 3, 6, 9 |
| 12 | 0 | Any | 0, 2, 4, 6, 8 | 44 | 2 | Any | 0, 2, 4, 6, 8 |
| 13 | 0 | Any | 1, 3, 5, 7, 9 | 45 | 2 | Any | 1, 3, 5, 7, 9 |
| 14 | 0 | Any | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 | 46 | N/A | N/A | N/A |
| 15 | 0 | Even | 9 | 47 | 2 | Even | 9 |
| 16 | 1 | Even | 1 | 48 | 3 | Even | 1 |
| 17 | 1 | Even | 4 | 49 | 3 | Even | 4 |
| 18 | 1 | Even | 7 | 50 | 3 | Even | 7 |
| 19 | 1 | Any | 1 | 51 | 3 | Any | 1 |
| 20 | 1 | Any | 4 | 52 | 3 | Any | 4 |
| 21 | 1 | Any | 7 | 53 | 3 | Any | 7 |
| 22 | 1 | Any | 1, 6 | 54 | 3 | Any | 1, 6 |
| 23 | 1 | Any | 2 ,7 | 55 | 3 | Any | 2 ,7 |
| 24 | 1 | Any | 3, 8 | 56 | 3 | Any | 3, 8 |
| 25 | 1 | Any | 1, 4, 7 | 57 | 3 | Any | 1, 4, 7 |
| 26 | 1 | Any | 2, 5, 8 | 58 | 3 | Any | 2, 5, 8 |
| 27 | 1 | Any | 3, 6, 9 | 59 | 3 | Any | 3, 6, 9 |
| 28 | 1 | Any | 0, 2, 4, 6, 8 | 60 | N/A | N/A | N/A |
| 29 | 1 | Any | 1, 3, 5, 7, 9 | 61 | N/A | N/A | N/A |
| 30 | N/A | N/A | N/A | 62 | N/A | N/A | N/A |
| 31 | 1 | Even | 9 | 63 | 3 | Even | 9 |

For frame structure type 2 with preamble formats 0-4, for each of the PRACH configurations there might be multiple random access resources in an UL subframe (or UpPTS for preamble format 4) depending on the UL/DL configuration [see table 4.2-2]. Table -3 lists PRACH configurations allowed for frame structure type 2 where the configuration index corresponds to a certain combination of preamble format, PRACH density value, ![](media_svg/image1173.svg) [公式≈: ^{D}RA] and version index, ![](media_svg/image1174.svg) [公式≈: ^{r}RA]. 
For frame structure type 2 with PRACH configuration indices 0, 1, 2, 20, 21, 22, 30, 31, 32, 40, 41, 42, 48, 49, 50, or with PRACH configuration indices 51, 53, 54, 55, 56, 57 in UL/DL configuration 3, 4, 5, the UE may for handover purposes assume an absolute value of the relative time difference between radio frame ![](media_svg/image1169.svg) [公式: i]in the current cell and the target cell is less than ![](media_svg/image1170.svg) [公式: 153600∪T_{s}].

Table -3: Frame structure type 2 random access configurations for preamble formats 0-4

| PRACH  configurationIndex | Preamble Format | DensityPer 10 ms![](media_svg/image1175.svg) [公式≈: ^{D}RA] | Version ![](media_svg/image1176.svg) [公式≈: ^{r}RA] | PRACH  configurationIndex | Preamble Format | DensityPer 10 ms![](media_svg/image1175.svg) [公式≈: ^{D}RA] | Version ![](media_svg/image1176.svg) [公式≈: ^{r}RA] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.5 | 0 | 32 | 2 | 0.5 | 2 |
| 1 | 0 | 0.5 | 1 | 33 | 2 | 1 | 0 |
| 2 | 0 | 0.5 | 2 | 34 | 2 | 1 | 1 |
| 3 | 0 | 1 | 0 | 35 | 2 | 2 | 0 |
| 4 | 0 | 1 | 1 | 36 | 2 | 3 | 0 |
| 5 | 0 | 1 | 2 | 37 | 2 | 4 | 0 |
| 6 | 0 | 2 | 0 | 38 | 2 | 5 | 0 |
| 7 | 0 | 2 | 1 | 39 | 2 | 6 | 0 |
| 8 | 0 | 2 | 2 | 40 | 3 | 0.5 | 0 |
| 9 | 0 | 3 | 0 | 41 | 3 | 0.5 | 1 |
| 10 | 0 | 3 | 1 | 42 | 3 | 0.5 | 2 |
| 11 | 0 | 3 | 2 | 43 | 3 | 1 | 0 |
| 12 | 0 | 4 | 0 | 44 | 3 | 1 | 1 |
| 13 | 0 | 4 | 1 | 45 | 3 | 2 | 0 |
| 14 | 0 | 4 | 2 | 46 | 3 | 3 | 0 |
| 15 | 0 | 5 | 0 | 47 | 3 | 4 | 0 |
| 16 | 0 | 5 | 1 | 48 | 4 | 0.5 | 0 |
| 17 | 0 | 5 | 2 | 49 | 4 | 0.5 | 1 |
| 18 | 0 | 6 | 0 | 50 | 4 | 0.5 | 2 |
| 19 | 0 | 6 | 1 | 51 | 4 | 1 | 0 |
| 20 | 1 | 0.5 | 0 | 52 | 4 | 1 | 1 |
| 21 | 1 | 0.5 | 1 | 53 | 4 | 2 | 0 |
| 22 | 1 | 0.5 | 2 | 54 | 4 | 3 | 0 |
| 23 | 1 | 1 | 0 | 55 | 4 | 4 | 0 |
| 24 | 1 | 1 | 1 | 56 | 4 | 5 | 0 |
| 25 | 1 | 2 | 0 | 57 | 4 | 6 | 0 |
| 26 | 1 | 3 | 0 | 58 | N/A | N/A | N/A |
| 27 | 1 | 4 | 0 | 59 | N/A | N/A | N/A |
| 28 | 1 | 5 | 0 | 60 | N/A | N/A | N/A |
| 29 | 1 | 6 | 0 | 61 | N/A | N/A | N/A |
| 30 | 2 | 0.5 | 0 | 62 | N/A | N/A | N/A |
| 31 | 2 | 0.5 | 1 | 63 | N/A | N/A | N/A |

Table 5.7.1-4 lists the mapping to physical resources for the different random access opportunities needed for a certain PRACH density value, ![](media_svg/image1175.svg) [公式≈: ^{D}RA]. Each quadruple of the format ![](media_svg/image1177.svg) [公式≈: (f_{RA},t_{RA}^{(}^{0}^{)},t_{RA}^{(}^{1}^{)},t_{RA}^{(}^{2}^{)})] indicates the location of a specific random access resource, where ![](media_svg/image1178.svg) [公式≈: ^{f}RA] is a frequency resource index within the considered time instance, ![](media_svg/image1179.svg) [公式≈: t_{RA}^{(}^{0}^{)}=0,1,2] indicates whether the resource is reoccurring in all radio frames, in even radio frames, or in odd radio frames, respectively, ![](media_svg/image1180.svg) [公式≈: t_{RA}^{(}^{1}^{)}=0,1] indicates whether the random access resource is located in first half frame or in second half frame, respectively, and where ![](media_svg/image1181.svg) [公式≈: _{t}_{RA}(2)] is the uplink subframe number where the preamble starts, counting from 0 at the first uplink subframe between 2 consecutive downlink-to-uplink switch points, with the exception of preamble format 4 where ![](media_svg/image1182.svg) [公式≈: _{t}_{RA}(2)] is denoted as (*). The start of the random access preamble formats 0-3 shall be aligned with the start of the corresponding uplink subframe at the UE assuming ![](media_svg/image1183.svg) [公式: N_{TA}=0] and the random access preamble format 4 shall start ![](media_svg/image1184.svg) [公式: 4832∪T_{s}] before the end of the UpPTS at the UE, where the UpPTS is referenced to the UE's uplink frame timing assuming![](media_svg/image1183.svg) [公式: N_{TA}=0].

The random access opportunities for each PRACH configuration shall be allocated in time first and then in frequency if and only if time multiplexing is not sufficient to hold all opportunities of a PRACH configuration needed for a certain density value ![](media_svg/image1175.svg) [公式≈: ^{D}RA] without overlap in time. For preamble format 0-3, the frequency multiplexing shall be done according to

![](media_svg/image1185.svg) [公式≈: ^{n}^{PRB}^{RA}^{=}^{√}^{⌡}^{⌡}^{⌠}^{⌡}_{⌡}_{∞}^{n}N^{PRB}^{RA}_{RB}^{UL}^{offset}−6−^{+}n^{6}_{PRB}^{RA}^{⋅}^{⋅}^{√}^{f}^{RA}_{offset}^{2}^{∂}^{∂}^{∃}^{,}−6^{⋅}_{⋅}_{√}^{f}^{RA}_{2}^{∂}_{∂}_{∃},^{if}otherwise^{f}^{RA}^{mod}^{2}^{=}^{0}]

where ![](media_svg/image1186.svg) [公式≈: _{N}_{RB}UL] is the number of uplink resource blocks, ![](media_svg/image1187.svg) [公式≈: ^{n}PRB^{RA}]is the first physical resource block allocated to the PRACH opportunity considered and where ![](media_svg/image1188.svg) [公式≈: ^{n}PRB^{RA}offset] is the first physical resource block available for PRACH.

For preamble format 4, the frequency multiplexing shall be done according to

![](media_svg/image1189.svg) [公式≈: _{n}_{PRB}RA_{=}√⌡_{⌠}_{⌡}_{∞}6_{N}f_{RB}_{UL}RA_{−},_{6}_{(}_{f}_{RA}_{+}_{1}_{),}if_{otherwise}((nfmod2)≠(2−NSP)+tRA^{(}^{1}^{)})mod2=0]

where![](media_svg/image125.svg) [公式≈: ^{n}f]is the system frame number and where![](media_svg/image1190.svg) [公式≈: ^{N}SP]is the number of DL to UL switch points within the radio frame.

For BL/CE UEs, only a subset of the subframes allowed for preamble transmission are allowed as starting subframes for the ![](media_svg/image1191.svg) [公式≈: _{N}_{rep}PRACH] repetitions. The allowed starting subframes for a PRACH configuration are determined as follows:

- Enumerate the subframes that are allowed for preamble transmission for the PRACH configuration as ![](media_svg/image1192.svg) [公式≈: n_{sf}^{RA}=0,...N_{sf}^{RA}−1] where ![](media_svg/image1193.svg) [公式: n_{sf}^{RA}=0] and ![](media_svg/image1194.svg) [公式≈: n_{sf}^{RA}=N_{sf}^{RA}−1] correspond to the two subframes allowed for preamble transmission with the smallest and the largest absolute subframe number ![](media_svg/image127.svg) [公式≈: _{n}_{sf}abs] , respectively.

- If a PRACH starting subframe periodicity ![](media_svg/image1195.svg) [公式≈: _{N}_{start}PRACH] is not provided by higher layers, the periodicity of the allowed starting subframes in terms of subframes allowed for preamble transmission is ![](media_svg/image1196.svg) [公式≈: _{N}_{rep}PRACH]. The allowed starting subframes defined over ![](media_svg/image1192.svg) [公式≈: n_{sf}^{RA}=0,...N_{sf}^{RA}−1] are given by ![](media_svg/image1197.svg) [公式≈: _{jN}_{rep}PRACH] where ![](media_svg/image1198.svg) [公式: j=0,1,2,...]

- If a PRACH starting subframe periodicity ![](media_svg/image1195.svg) [公式≈: _{N}_{start}PRACH] is provided by higher layers, it indicates the periodicity of the allowed starting subframes in terms of subframes allowed for preamble transmission. The allowed starting subframes defined over ![](media_svg/image1192.svg) [公式≈: n_{sf}^{RA}=0,...N_{sf}^{RA}−1] are given by ![](media_svg/image1199.svg) [公式≈: _{jN}_{start}PRACH_{+}_{N}_{rep}PRACH] where ![](media_svg/image1198.svg) [公式: j=0,1,2,...]

- No starting subframe defined over ![](media_svg/image1192.svg) [公式≈: n_{sf}^{RA}=0,...N_{sf}^{RA}−1] such that ![](media_svg/image1200.svg) [公式≈: _{n}_{sf}RA_{>}_{N}_{sf}RA_{−}_{N}_{rep}PRACH] is allowed.

Each random access preamble occupies a bandwidth corresponding to 6 consecutive resource blocks for both frame structures.

Table 5.7.1-4: Frame structure type 2 random access preamble mapping in time and frequency

| PRACH configuration Index(See Table 5.7.1-3) | UL/DL configuration (See Table 4.2-2) |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| 0 | (0,1,0,2) | (0,1,0,1) | (0,1,0,0) | (0,1,0,2) | (0,1,0,1) | (0,1,0,0) | (0,1,0,2) |
| 1 | (0,2,0,2) | (0,2,0,1) | (0,2,0,0) | (0,2,0,2) | (0,2,0,1) | (0,2,0,0) | (0,2,0,2) |
| 2 | (0,1,1,2) | (0,1,1,1) | (0,1,1,0) | (0,1,0,1) | (0,1,0,0) | N/A | (0,1,1,1) |
| 3 | (0,0,0,2) | (0,0,0,1) | (0,0,0,0) | (0,0,0,2) | (0,0,0,1) | (0,0,0,0) | (0,0,0,2) |
| 4 | (0,0,1,2) | (0,0,1,1) | (0,0,1,0) | (0,0,0,1) | (0,0,0,0) | N/A | (0,0,1,1) |
| 5 | (0,0,0,1) | (0,0,0,0) | N/A | (0,0,0,0) | N/A | N/A | (0,0,0,1) |
| 6 | (0,0,0,2)(0,0,1,2) | (0,0,0,1)(0,0,1,1) | (0,0,0,0)(0,0,1,0) | (0,0,0,1)(0,0,0,2) | (0,0,0,0)(0,0,0,1) | (0,0,0,0)(1,0,0,0) | (0,0,0,2)(0,0,1,1) |
| 7 | (0,0,0,1)(0,0,1,1) | (0,0,0,0)(0,0,1,0) | N/A | (0,0,0,0)(0,0,0,2) | N/A | N/A | (0,0,0,1)(0,0,1,0) |
| 8 | (0,0,0,0)(0,0,1,0) | N/A | N/A | (0,0,0,0)(0,0,0,1) | N/A | N/A | (0,0,0,0)(0,0,1,1) |
| 9 | (0,0,0,1)(0,0,0,2)(0,0,1,2) | (0,0,0,0)(0,0,0,1)(0,0,1,1) | (0,0,0,0)(0,0,1,0)(1,0,0,0) | (0,0,0,0)(0,0,0,1)(0,0,0,2) | (0,0,0,0)(0,0,0,1)(1,0,0,1) | (0,0,0,0)(1,0,0,0)(2,0,0,0) | (0,0,0,1)(0,0,0,2)(0,0,1,1) |
| 10 | (0,0,0,0)(0,0,1,0) (0,0,1,1) | (0,0,0,1)(0,0,1,0) (0,0,1,1) | (0,0,0,0)(0,0,1,0) (1,0,1,0) | N/A | (0,0,0,0)(0,0,0,1)(1,0,0,0) | N/A | (0,0,0,0)(0,0,0,2)(0,0,1,0) |
| 11 | N/A | (0,0,0,0) (0,0,0,1)(0,0,1,0) | N/A | N/A | N/A | N/A | (0,0,0,1)(0,0,1,0)(0,0,1,1) |
| 12 | (0,0,0,1)(0,0,0,2)(0,0,1,1)(0,0,1,2) | (0,0,0,0)(0,0,0,1)(0,0,1,0)(0,0,1,1) | (0,0,0,0)(0,0,1,0)(1,0,0,0)(1,0,1,0) | (0,0,0,0)(0,0,0,1)(0,0,0,2)(1,0,0,2) | (0,0,0,0)(0,0,0,1)(1,0,0,0)(1,0,0,1) | (0,0,0,0)(1,0,0,0)(2,0,0,0)(3,0,0,0) | (0,0,0,1)(0,0,0,2)(0,0,1,0)(0,0,1,1) |
| 13 | (0,0,0,0)(0,0,0,2)(0,0,1,0)(0,0,1,2) | N/A | N/A | (0,0,0,0)(0,0,0,1)(0,0,0,2)(1,0,0,1) | N/A | N/A | (0,0,0,0)(0,0,0,1)(0,0,0,2)(0,0,1,1) |
| 14 | (0,0,0,0)(0,0,0,1)(0,0,1,0)(0,0,1,1) | N/A | N/A | (0,0,0,0)(0,0,0,1)(0,0,0,2)(1,0,0,0) | N/A | N/A | (0,0,0,0)(0,0,0,2)(0,0,1,0)(0,0,1,1) |
| 15 | (0,0,0,0)(0,0,0,1)(0,0,0,2)(0,0,1,1)(0,0,1,2) | (0,0,0,0)(0,0,0,1)(0,0,1,0)(0,0,1,1)(1,0,0,1) | (0,0,0,0)(0,0,1,0)(1,0,0,0)(1,0,1,0)(2,0,0,0) | (0,0,0,0)(0,0,0,1)(0,0,0,2)(1,0,0,1)(1,0,0,2) | (0,0,0,0)(0,0,0,1)(1,0,0,0)(1,0,0,1)(2,0,0,1) | (0,0,0,0)(1,0,0,0)(2,0,0,0)(3,0,0,0)(4,0,0,0) | (0,0,0,0)(0,0,0,1)(0,0,0,2)(0,0,1,0)(0,0,1,1) |
| 16 | (0,0,0,1)(0,0,0,2)(0,0,1,0)(0,0,1,1)(0,0,1,2) | (0,0,0,0)(0,0,0,1)(0,0,1,0)(0,0,1,1)(1,0,1,1) | (0,0,0,0)(0,0,1,0)(1,0,0,0)(1,0,1,0)(2,0,1,0) | (0,0,0,0)(0,0,0,1)(0,0,0,2)(1,0,0,0)(1,0,0,2) | (0,0,0,0)(0,0,0,1)(1,0,0,0)(1,0,0,1)(2,0,0,0) | N/A | N/A |
| 17 | (0,0,0,0)(0,0,0,1)(0,0,0,2)(0,0,1,0)(0,0,1,2) | (0,0,0,0)(0,0,0,1)(0,0,1,0)(0,0,1,1)(1,0,0,0) | N/A | (0,0,0,0)(0,0,0,1)(0,0,0,2) (1,0,0,0)(1,0,0,1) | N/A | N/A | N/A |
| 18 | (0,0,0,0)(0,0,0,1)(0,0,0,2)(0,0,1,0)(0,0,1,1)(0,0,1,2) | (0,0,0,0)(0,0,0,1)(0,0,1,0)(0,0,1,1)(1,0,0,1)(1,0,1,1) | (0,0,0,0)(0,0,1,0)(1,0,0,0)(1,0,1,0)(2,0,0,0)(2,0,1,0) | (0,0,0,0)(0,0,0,1)(0,0,0,2)(1,0,0,0)(1,0,0,1)(1,0,0,2) | (0,0,0,0)(0,0,0,1)(1,0,0,0)(1,0,0,1)(2,0,0,0)(2,0,0,1) | (0,0,0,0)(1,0,0,0)(2,0,0,0)(3,0,0,0)(4,0,0,0)(5,0,0,0) | (0,0,0,0)(0,0,0,1)(0,0,0,2)(0,0,1,0)(0,0,1,1)(1,0,0,2) |
| 19 | N/A | (0,0,0,0)(0,0,0,1)(0,0,1,0)(0,0,1,1)(1,0,0,0)(1,0,1,0) | N/A | N/A | N/A | N/A | (0,0,0,0)(0,0,0,1)(0,0,0,2)(0,0,1,0)(0,0,1,1)(1,0,1,1) |
| 20 / 30 | (0,1,0,1) | (0,1,0,0) | N/A | (0,1,0,1) | (0,1,0,0) | N/A | (0,1,0,1) |
| 21 / 31 | (0,2,0,1) | (0,2,0,0) | N/A | (0,2,0,1) | (0,2,0,0) | N/A | (0,2,0,1) |
| 22 / 32 | (0,1,1,1) | (0,1,1,0) | N/A | N/A | N/A | N/A | (0,1,1,0) |
| 23 / 33 | (0,0,0,1) | (0,0,0,0) | N/A | (0,0,0,1) | (0,0,0,0) | N/A | (0,0,0,1) |
| 24 / 34 | (0,0,1,1) | (0,0,1,0) | N/A | N/A | N/A | N/A | (0,0,1,0) |
| 25 / 35 | (0,0,0,1)(0,0,1,1) | (0,0,0,0)(0,0,1,0) | N/A | (0,0,0,1)(1,0,0,1) | (0,0,0,0)(1,0,0,0) | N/A | (0,0,0,1)(0,0,1,0) |
| 26 / 36 | (0,0,0,1)(0,0,1,1)(1,0,0,1) | (0,0,0,0)(0,0,1,0)(1,0,0,0) | N/A | (0,0,0,1)(1,0,0,1)(2,0,0,1) | (0,0,0,0)(1,0,0,0)(2,0,0,0) | N/A | (0,0,0,1)(0,0,1,0)(1,0,0,1) |
| 27 / 37 | (0,0,0,1)(0,0,1,1)(1,0,0,1)(1,0,1,1) | (0,0,0,0)(0,0,1,0)(1,0,0,0)(1,0,1,0) | N/A | (0,0,0,1)(1,0,0,1)(2,0,0,1)(3,0,0,1) | (0,0,0,0)(1,0,0,0)(2,0,0,0)(3,0,0,0) | N/A | (0,0,0,1)(0,0,1,0)(1,0,0,1)(1,0,1,0) |
| 28 / 38 | (0,0,0,1)(0,0,1,1)(1,0,0,1)(1,0,1,1)(2,0,0,1) | (0,0,0,0)(0,0,1,0)(1,0,0,0)(1,0,1,0)(2,0,0,0) | N/A | (0,0,0,1)(1,0,0,1)(2,0,0,1)(3,0,0,1)(4,0,0,1) | (0,0,0,0)(1,0,0,0)(2,0,0,0)(3,0,0,0)(4,0,0,0) | N/A | (0,0,0,1)(0,0,1,0)(1,0,0,1)(1,0,1,0)(2,0,0,1) |
| 29 /39 | (0,0,0,1)(0,0,1,1)(1,0,0,1)(1,0,1,1)(2,0,0,1)(2,0,1,1) | (0,0,0,0)(0,0,1,0)(1,0,0,0)(1,0,1,0)(2,0,0,0)(2,0,1,0) | N/A | (0,0,0,1)(1,0,0,1)(2,0,0,1)(3,0,0,1)(4,0,0,1)(5,0,0,1) | (0,0,0,0)(1,0,0,0)(2,0,0,0)(3,0,0,0)(4,0,0,0)(5,0,0,0) | N/A | (0,0,0,1)(0,0,1,0)(1,0,0,1)(1,0,1,0)(2,0,0,1)(2,0,1,0) |
| 40 | (0,1,0,0) | N/A | N/A | (0,1,0,0) | N/A | N/A | (0,1,0,0) |
| 41 | (0,2,0,0) | N/A | N/A | (0,2,0,0) | N/A | N/A | (0,2,0,0) |
| 42 | (0,1,1,0) | N/A | N/A | N/A | N/A | N/A | N/A |
| 43 | (0,0,0,0) | N/A | N/A | (0,0,0,0) | N/A | N/A | (0,0,0,0) |
| 44 | (0,0,1,0) | N/A | N/A | N/A | N/A | N/A | N/A |
| 45 | (0,0,0,0)(0,0,1,0) | N/A | N/A | (0,0,0,0)(1,0,0,0) | N/A | N/A | (0,0,0,0)(1,0,0,0) |
| 46 | (0,0,0,0)(0,0,1,0)(1,0,0,0) | N/A | N/A | (0,0,0,0)(1,0,0,0)(2,0,0,0) | N/A | N/A | (0,0,0,0)(1,0,0,0)(2,0,0,0) |
| 47 | (0,0,0,0)(0,0,1,0)(1,0,0,0)(1,0,1,0) | N/A | N/A | (0,0,0,0)(1,0,0,0)(2,0,0,0)(3,0,0,0) | N/A | N/A | (0,0,0,0)(1,0,0,0)(2,0,0,0)(3,0,0,0) |
| 48 | (0,1,0,*) | (0,1,0,*) | (0,1,0,*) | (0,1,0,*) | (0,1,0,*) | (0,1,0,*) | (0,1,0,*) |
| 49 | (0,2,0,*) | (0,2,0,*) | (0,2,0,*) | (0,2,0,*) | (0,2,0,*) | (0,2,0,*) | (0,2,0,*) |
| 50 | (0,1,1,*) | (0,1,1,*) | (0,1,1,*) | N/A | N/A | N/A | (0,1,1,*) |
| 51 | (0,0,0,*) | (0,0,0,*) | (0,0,0,*) | (0,0,0,*) | (0,0,0,*) | (0,0,0,*) | (0,0,0,*) |
| 52 | (0,0,1,*) | (0,0,1,*) | (0,0,1,*) | N/A | N/A | N/A | (0,0,1,*) |
| 53 | (0,0,0,*)(0,0,1,*) | (0,0,0,*)(0,0,1,*) | (0,0,0,*)(0,0,1,*) | (0,0,0,*)(1,0,0,*) | (0,0,0,*)(1,0,0,*) | (0,0,0,*)(1,0,0,*) | (0,0,0,*)(0,0,1,*) |
| 54 | (0,0,0,*)(0,0,1,*)(1,0,0,*) | (0,0,0,*)(0,0,1,*)(1,0,0,*) | (0,0,0,*)(0,0,1,*)(1,0,0,*) | (0,0,0,*)(1,0,0,*)(2,0,0,*) | (0,0,0,*)(1,0,0,*)(2,0,0,*) | (0,0,0,*)(1,0,0,*)(2,0,0,*) | (0,0,0,*)(0,0,1,*)(1,0,0,*) |
| 55 | (0,0,0,*)(0,0,1,*)(1,0,0,*)(1,0,1,*) | (0,0,0,*)(0,0,1,*)(1,0,0,*)(1,0,1,*) | (0,0,0,*)(0,0,1,*)(1,0,0,*)(1,0,1,*) | (0,0,0,*)(1,0,0,*)(2,0,0,*)(3,0,0,*) | (0,0,0,*)(1,0,0,*)(2,0,0,*)(3,0,0,*) | (0,0,0,*)(1,0,0,*)(2,0,0,*)(3,0,0,*) | (0,0,0,*)(0,0,1,*)(1,0,0,*)(1,0,1,*) |
| 56 | (0,0,0,*)(0,0,1,*)(1,0,0,*)(1,0,1,*)(2,0,0,*) | (0,0,0,*)(0,0,1,*)(1,0,0,*)(1,0,1,*)(2,0,0,*) | (0,0,0,*)(0,0,1,*)(1,0,0,*)(1,0,1,*)(2,0,0,*) | (0,0,0,*)(1,0,0,*)(2,0,0,*)(3,0,0,*)(4,0,0,*) | (0,0,0,*)(1,0,0,*)(2,0,0,*)(3,0,0,*)(4,0,0,*) | (0,0,0,*)(1,0,0,*)(2,0,0,*)(3,0,0,*)(4,0,0,*) | (0,0,0,*)(0,0,1,*)(1,0,0,*)(1,0,1,*)(2,0,0,*) |
| 57 | (0,0,0,*)(0,0,1,*)(1,0,0,*)(1,0,1,*)(2,0,0,*)(2,0,1,*) | (0,0,0,*)(0,0,1,*)(1,0,0,*)(1,0,1,*)(2,0,0,*)(2,0,1,*) | (0,0,0,*)(0,0,1,*)(1,0,0,*)(1,0,1,*)(2,0,0,*)(2,0,1,*) | (0,0,0,*)(1,0,0,*)(2,0,0,*)(3,0,0,*)(4,0,0,*)(5,0,0,*) | (0,0,0,*)(1,0,0,*)(2,0,0,*)(3,0,0,*)(4,0,0,*)(5,0,0,*) | (0,0,0,*)(1,0,0,*)(2,0,0,*)(3,0,0,*)(4,0,0,*)(5,0,0,*) | (0,0,0,*)(0,0,1,*)(1,0,0,*)(1,0,1,*)(2,0,0,*)(2,0,1,*) |
| 58 | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 59 | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 60 | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 61 | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 62 | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 63 | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| NOTE: * UpPTS |  |  |  |  |  |  |  |

### 5.7.2 Preamble sequence generation

The random access preambles are generated from Zadoff-Chu sequences with zero correlation zone, generated from one or several root Zadoff-Chu sequences. The network configures the set of preamble sequences the UE is allowed to use.

There are up to two sets of 64 preambles available in a cell where Set 1 corresponds to higher layer PRACH configuration using prach-ConfigurationIndex and prach-FrequencyOffset and Set 2, if configured, corresponds to higher layer PRACH configuration using prach-ConfigurationIndexHighSpeed and prach-FrequencyOffsetHighSpeed. The set of 64 preamble sequences in a cell is found by including first, in the order of increasing cyclic shift, all the available cyclic shifts of a root Zadoff-Chu sequence with the logical index rootSequenceIndexHighSpeed (for Set 2, if configured) or with the logical index RACH_ROOT_SEQUENCE (for Set 1), where both rootSequenceIndexHighSpeed (if configured) and RACH_ROOT_SEQUENCE are broadcasted as part of the System Information. Additional preamble sequences, in case 64 preambles cannot be generated from a single root Zadoff-Chu sequence, are obtained from the root sequences with the consecutive logical indexes until all the 64 sequences are found. 
The logical root sequence order is cyclic: the logical index 0 is consecutive to 837. The relation between a logical root sequence index and physical root sequence index ![](media_svg/image749.svg) [公式: u] is given by Tables 5.7.2-4 and 5.7.2-5 for preamble formats 0 – 3 and 4, respectively.

The ![](media_svg/image1201.svg) [公式≈: _{u}th] root Zadoff-Chu sequence is defined by

![](media_svg/image1202.svg) [公式≈: x_{u}(n)=e^{−}^{j}^{Π}^{un}^{N}^{(}^{ZC}^{n}^{+}^{1}^{)},0≥n≥N_{ZC}−1]

where the length ![](media_svg/image1203.svg) [公式≈: ^{N}ZC] of the Zadoff-Chu sequence is given by Table 5.7.2-1. From the ![](media_svg/image1201.svg) [公式≈: _{u}th] root Zadoff-Chu sequence, random access preambles with zero correlation zones of length ![](media_svg/image1204.svg) [公式: N_{CS}−1]are defined by cyclic shifts according to

![](media_svg/image1205.svg) [公式≈: x_{u}_{,}_{v}(n)=x_{u}((n+C_{v})modN_{ZC})]

where the cyclic shift is given by

![](media_svg/image1206.svg) [公式≈: C_{w}v=_{=}^{√}^{⌡}^{⌡}^{⌡}⌠_{⌡}_{⌡}_{⌡}_{∞}_{n}_{shift}^{vN}^{0}d_{d}_{d}_{RA}start_{start}_{start}_{n}^{CS}_{group}_{RA}√_{+}_{+}v_{(}_{(}_{v}n_{v}_{+}shift^{RA}_{−}_{−}_{n}_{w}_{w}_{shift}∃_{RA}_{)}+_{−}_{N}(_{n}_{CS}v_{shift}_{RA}mod_{)}_{N}_{CS}nshift^{RA})NCSv_{v}_{v}^{v}^{N}=_{=}_{=}^{=}^{CS}0_{w}_{w}^{0,1,...,}^{=},1_{,...,}_{+},...,^{0}_{n}_{w}_{shift}_{RA}w^{√}_{+}^{N}_{,...,}−_{n}^{ZC}1_{shift}_{RA}_{w}^{N}_{−}_{+}^{CS}_{1}_{n}_{shift}^{∃}_{RA}^{−}^{1}_{+}^{,}^{N}_{n}_{shift}^{CS}_{RA}^{⎯}_{−}_{1}^{0}^{for }^{for }for _{for }_{for }^{unrestrict}^{unrestrict}restricted_{restricted}_{restricted}^{ed}^{ed}sets_{sets}_{sets}^{sets}^{sets} type_{ type}_{ type}A _{B}_{B}andB]

and ![](media_svg/image40.svg) [公式≈: ^{N}CS] is given by Tables 5.7.2-2 and 5.7.2-3 for preamble formats 0-3 and 4, respectively, where the higher-layer parameters zeroCorrelationZoneConfig and zeroCorrelationZoneConfigHighSpeed shall be used for PRACH preamble Set 1 and Set 2 (if configured), respectively. Restricted set type B shall be used for PRACH preamble Set 2 (if configured), and the parameter High-speed-flag provided by higher layers determines if unrestricted set or restricted set type A shall be used for PRACH preamble Set 1.

The variable ![](media_svg/image1207.svg) [公式≈: ^{d}u] is the cyclic shift corresponding to a Doppler shift of magnitude ![](media_svg/image1208.svg) [公式≈: ^{1}^{T}SEQ] and is given by

![](media_svg/image1209.svg) [公式≈: ^{d}^{u}^{=}^{√}^{⌠}_{∞}N^{p}_{ZC}−p^{0}otherwise^{≥}^{p}^{<}^{N}^{ZC}^{2}]

where ![](media_svg/image1210.svg) [公式: p] is the smallest non-negative integer that fulfils ![](media_svg/image1211.svg) [公式: (pu)modN_{ZC}=1]. The parameters for restricted sets of cyclic shifts depend on ![](media_svg/image1207.svg) [公式≈: ^{d}u].

For restricted set type A and ![](media_svg/image1212.svg) [公式≈: N_{CS}≥d_{u}<N_{ZC}3], the parameters are given by

![](media_svg/image1213.svg) [公式≈: ^{n}^{d}^{n}n^{group}^{RA}^{shift}shift^{start}^{RA}^{RA}^{=}^{=}^{=}=^{2}max^{√}^{√}^{d}^{N}^{d}^{u}^{u}^{ZC}^{+}(^{N}√(^{n}^{d}N^{CS}^{shift}^{RA}^{start}ZC^{∃}^{N}^{∃}−^{CS}2du−ngroup^{RA}dstart)NCS∃,0)]

For restricted set type A and ![](media_svg/image1214.svg) [公式≈: N_{ZC}3≥d_{u}≥(N_{ZC}−N_{CS})2], the parameters are given by

![](media_svg/image1215.svg) [公式≈: ^{n}^{d}^{n}n^{group}^{RA}^{shift}shift^{start}^{RA}^{RA}^{=}^{=}^{=}=min^{√}^{√}^{N}^{(}^{d}^{N}^{ZC}^{u}^{ZC}(max^{d}^{−}^{start}^{−}^{2}^{d}^{2}(^{u}^{∃}√^{d}(^{+}d^{u}^{)}u^{n}−^{shift}^{RA}^{N}n^{CS}group^{RA}^{N}^{∃}^{CS}dstart)NCS∃,0),nshift^{RA})]

For restricted set type B and ![](media_svg/image1216.svg) [公式≈: N_{CS}≥d_{u}<N_{ZC}5], the parameters are given by

![](media_svg/image1217.svg) [公式≈: ^{n}^{d}^{n}n^{group}^{RA}^{shift}shift^{start}^{RA}^{RA}^{=}^{=}^{=}=^{4}max^{√}^{√}^{d}^{N}^{d}^{u}^{u}^{ZC}^{+}(^{N}√(^{n}^{d}N^{CS}^{shift}^{RA}^{start}ZC^{∃}^{N}^{∃}−^{CS}4du−ngroup^{RA}dstart)NCS∃,0)]

For restricted set type B and ![](media_svg/image1218.svg) [公式≈: N_{ZC}5≥d_{u}≥(N_{ZC}−N_{CS})4], the parameters are given by

![](media_svg/image1219.svg) [公式≈: ^{n}^{d}^{n}n^{group}^{RA}^{shift}shift^{start}^{RA}^{RA}^{=}^{=}^{=}=min^{√}^{√}^{N}^{(}^{d}^{N}^{ZC}^{u}^{ZC}(max^{d}^{−}^{start}^{−}^{4}^{d}^{4}(^{u}^{∃}√^{d}(^{u}^{+}d^{)}u^{n}−^{shift}^{N}^{RA}n^{CS}group^{RA}^{N}^{∃}^{CS}dstart)NCS∃,0),nshift^{RA})]

For restricted set type B and ![](media_svg/image1220.svg) [公式≈: (N_{ZC}+N_{CS})4≥d_{u}<2N_{ZC}7], the parameters are given by

![](media_svg/image1221.svg) [公式≈: ^{n}^{d}^{d}^{d}^{n}^{n}^{n}n^{group}^{RA}^{shift}^{shift}^{shift}shift^{start}^{start}^{start}^{RA}^{RA}^{RA}^{RA}^{=}^{=}^{=}^{=}^{=}^{=}^{=}=^{4}^{max}^{√}^{√}^{√}√^{N}^{N}(^{min}^{(}^{d}(^{d}1^{4}^{ZC}^{ZC}^{u}^{u}^{d}−^{−}^{(}^{u}^{(}^{d}min^{−}^{−}^{√}^{d}^{(}^{−}^{start}^{N}^{N}^{u}^{3}^{2}^{d}^{N}^{d}^{ZC}^{ZC}^{−}(1^{u}^{u}^{∃}^{ZC}^{n},^{+}n^{+}^{+}^{−}^{group}^{RA}shift^{)}^{RA}^{n}^{3}^{n}^{n}^{group}^{d}^{shift}^{group}^{RA}^{RA}^{RA}^{N}^{u}^{d})^{CS})(^{start}^{−}d^{N}^{d}^{d}^{∃}u^{n}^{CS}^{start}^{start}^{group}^{,}^{RA}−^{4}^{d}n^{+}^{+}^{u}group^{RA}^{d}^{n}^{−}^{n}^{start}^{shift}^{shift}^{RA}^{RA}^{N}d^{ZC}^{)}start^{N}^{N}^{N}^{CS}^{CS}^{−})^{CS}+^{n}^{shift}min^{∃}^{RA}^{,}^{0}^{)}^{N}(1^{CS},n^{)}shift^{RA}^{N})^{CS}(4d^{∃}u−NZC−nshift^{RA}NCS))NCS∃−nshift^{RA}]

For restricted set type B and ![](media_svg/image1222.svg) [公式≈: 2N_{ZC}7≥d_{u}≥(N_{ZC}−N_{CS})3], the parameters are given by

![](media_svg/image1223.svg) [公式≈: ^{n}^{d}^{d}^{d}^{n}^{n}n_{n}^{group}^{RA}^{shift}^{shift}shift_{shift}^{start}^{start}^{start}^{RA}^{RA}^{RA}_{RA}^{=}^{=}^{=}^{=}^{=}^{=}=_{=}^{0}_{0}^{d}^{max}^{√}^{√}√^{N}min^{(}^{d}^{u}^{N}^{ZC}^{u}^{+}^{ZC}^{(}(^{d}^{n}^{−}^{√}d^{(}^{start}^{group}^{4}^{RA}u^{−}^{3}^{d}^{d}−^{3}^{u}^{u}^{∃}^{d}n^{d}^{−}^{+}^{u}group^{RA}^{start}^{)}^{N}^{n}^{shift}^{RA}^{N}^{ZC}^{+}d^{CS}start^{−}^{n}^{N}^{shift}^{∃}^{RA}^{n}^{CS},^{group}^{RA}N^{N}ZC^{CS}^{d}^{start}−3d^{)}u^{N}−^{CS}nshift^{RA}^{∃}^{,}^{0}^{)}NCS)NCS∃]

For restricted set type B and ![](media_svg/image1224.svg) [公式≈: (N_{ZC}+N_{CS})3≥d_{u}<2N_{ZC}5], the parameters are given by

![](media_svg/image1225.svg) [公式≈: ^{n}^{d}^{d}^{d}^{n}n_{n}_{n}^{group}^{RA}^{shift}shift_{shift}_{shift}^{start}^{start}^{start}^{RA}^{RA}_{RA}_{RA}^{=}^{=}^{=}^{=}^{=}=_{=}_{=}^{3}^{0}^{0}_{0}_{0}max^{√}^{√}^{(}^{d}^{d}^{3}^{u}^{u}^{d}^{−}^{u}(^{d}√(^{−}^{start}^{N}N^{N}^{ZC}ZC^{∃}^{ZC}^{+}−^{)}^{n}2^{shift}^{RA}d^{N}u^{CS}−^{N}^{∃}n^{CS}group^{RA}dstart)NCS∃,0)]

For restricted set type B and ![](media_svg/image1226.svg) [公式≈: 2N_{ZC}5≥d_{u}≥(N_{ZC}−N_{CS})2], the parameters are given by

![](media_svg/image1227.svg) [公式≈: ^{n}^{d}^{d}^{d}^{n}n_{n}_{n}^{group}^{RA}^{shift}shift_{shift}_{shift}^{start}^{start}^{start}^{RA}^{RA}_{RA}_{RA}^{=}^{=}^{=}^{=}^{=}=_{=}_{=}^{0}^{0}_{0}_{0}^{2}max^{√}^{√}^{(}^{(}^{(}^{N}^{N}^{N}^{ZC}^{ZC}^{ZC}(√(3^{−}^{−}^{−}d^{2}^{d}u^{2}^{d}^{u}^{d}−^{)}^{u}^{u}N^{)}^{)}^{d}^{+}ZC^{start}^{N}^{n}^{CS}^{shift}−^{RA}^{∃}^{∃}ngroup^{RA}^{N}^{CS}dstart)NCS∃,0)]

For all other values of ![](media_svg/image1207.svg) [公式≈: ^{d}u], there are no cyclic shifts in the restricted set.

Table 5.7.2-1: Random access preamble sequence length

| Preamble format | ![](media_svg/image1203.svg) [公式≈: ^{N}ZC] |
| --- | --- |
| 0 – 3 | 839 |
| 4 | 139 |

Table 5.7.2-2: ![](media_svg/image40.svg) [公式≈: ^{N}CS] for preamble generation (preamble formats 0-3)

| zeroCorrelationZoneConfig, zeroCorrelationZoneConfigHighSpeed | ![](media_svg/image40.svg) [公式≈: ^{N}CS] value |  |  |
| --- | --- | --- | --- |
|  | Unrestricted set | Restricted set type A | Restricted set type B |
| 0 | 0 | 15 | 15 |
| 1 | 13 | 18 | 18 |
| 2 | 15 | 22 | 22 |
| 3 | 18 | 26 | 26 |
| 4 | 22 | 32 | 32 |
| 5 | 26 | 38 | 38 |
| 6 | 32 | 46 | 46 |
| 7 | 38 | 55 | 55 |
| 8 | 46 | 68 | 68 |
| 9 | 59 | 82 | 82 |
| 10 | 76 | 100 | 100 |
| 11 | 93 | 128 | 118 |
| 12 | 119 | 158 | 137 |
| 13 | 167 | 202 | - |
| 14 | 279 | 237 | - |
| 15 | 419 | - | - |

Table 5.7.2-3: ![](media_svg/image40.svg) [公式≈: ^{N}CS] for preamble generation (preamble format 4)

| zeroCorrelationZoneConfig | ![](media_svg/image40.svg) [公式≈: ^{N}CS] value |
| --- | --- |
| 0 | 2 |
| 1 | 4 |
| 2 | 6 |
| 3 | 8 |
| 4 | 10 |
| 5 | 12 |
| 6 | 15 |
| 7 | N/A |
| 8 | N/A |
| 9 | N/A |
| 10 | N/A |
| 11 | N/A |
| 12 | N/A |
| 13 | N/A |
| 14 | N/A |
| 15 | N/A |

Table 5.7.2-4: Root Zadoff-Chu sequence order for preamble formats 0 – 3

| Logical root sequence number | Physical root sequence number ![](media_svg/image749.svg) [公式: u](in increasing order of the corresponding logical sequence number) |
| --- | --- |
| 0–23 | 129, 710, 140, 699, 120, 719, 210, 629, 168, 671, 84, 755, 105, 734, 93, 746, 70, 769, 60, 7792, 837, 1, 838 |
| 24–29 | 56, 783, 112, 727, 148, 691 |
| 30–35 | 80, 759, 42, 797, 40, 799 |
| 36–41 | 35, 804, 73, 766, 146, 693 |
| 42–51 | 31, 808, 28, 811, 30, 809, 27, 812, 29, 810 |
| 52–63 | 24, 815, 48, 791, 68, 771, 74, 765, 178, 661, 136, 703 |
| 64–75 | 86, 753, 78, 761, 43, 796, 39, 800, 20, 819, 21, 818 |
| 76–89 | 95, 744, 202, 637, 190, 649, 181, 658, 137, 702, 125, 714, 151, 688 |
| 90–115 | 217, 622, 128, 711, 142, 697, 122, 717, 203, 636, 118, 721, 110, 729, 89, 750, 103, 736, 61, 778, 55, 784, 15, 824, 14, 825 |
| 116–135 | 12, 827, 23, 816, 34, 805, 37, 802, 46, 793, 207, 632, 179, 660, 145, 694, 130, 709, 223, 616 |
| 136–167 | 228, 611, 227, 612, 132, 707, 133, 706, 143, 696, 135, 704, 161, 678, 201, 638, 173, 666, 106, 733, 83, 756, 91, 748, 66, 773, 53, 786, 10, 829, 9, 830 |
| 168–203 | 7, 832, 8, 831, 16, 823, 47, 792, 64, 775, 57, 782, 104, 735, 101, 738, 108, 731, 208, 631, 184, 655, 197, 642, 191, 648, 121, 718, 141, 698, 149, 690, 216, 623, 218, 621 |
| 204–263 | 152, 687, 144, 695, 134, 705, 138, 701, 199, 640, 162, 677, 176, 663, 119, 720, 158, 681, 164, 675, 174, 665, 171, 668, 170, 669, 87, 752, 169, 670, 88, 751, 107, 732, 81, 758, 82, 757, 100, 739, 98, 741, 71, 768, 59, 780, 65, 774, 50, 789, 49, 790, 26, 813, 17, 822, 13, 826, 6, 833 |
| 264–327 | 5, 834, 33, 806, 51, 788, 75, 764, 99, 740, 96, 743, 97, 742, 166, 673, 172, 667, 175, 664, 187, 652, 163, 676, 185, 654, 200, 639, 114, 725, 189, 650, 115, 724, 194, 645, 195, 644, 192, 647, 182, 657, 157, 682, 156, 683, 211, 628, 154, 685, 123, 716, 139, 700, 212, 627, 153, 686, 213, 626, 215, 624, 150, 689 |
| 328–383 | 225, 614, 224, 615, 221, 618, 220, 619, 127, 712, 147, 692, 124, 715, 193, 646, 205, 634, 206, 633, 116, 723, 160, 679, 186, 653, 167, 672, 79, 760, 85, 754, 77, 762, 92, 747, 58, 781, 62, 777, 69, 770, 54, 785, 36, 803, 32, 807, 25, 814, 18, 821, 11, 828, 4, 835 |
| 384–455 | 3, 836, 19, 820, 22, 817, 41, 798, 38, 801, 44, 795, 52, 787, 45, 794, 63, 776, 67, 772, 72767, 76, 763, 94, 745, 102, 737, 90, 749, 109, 730, 165, 674, 111, 728, 209, 630, 204, 635, 117, 722, 188, 651, 159, 680, 198, 641, 113, 726, 183, 656, 180, 659, 177, 662, 196, 643, 155, 684, 214, 625, 126, 713, 131, 708, 219, 620, 222, 617, 226, 613 |
| 456–513 | 230, 609, 232, 607, 262, 577, 252, 587, 418, 421, 416, 423, 413, 426, 411, 428, 376, 463, 395, 444, 283, 556, 285, 554, 379, 460, 390, 449, 363, 476, 384, 455, 388, 451, 386, 453, 361, 478, 387, 452, 360, 479, 310, 529, 354, 485, 328, 511, 315, 524, 337, 502, 349, 490, 335, 504, 324, 515 |
| 514–561 | 323, 516, 320, 519, 334, 505, 359, 480, 295, 544, 385, 454, 292, 547, 291, 548, 381, 458, 399, 440, 380, 459, 397, 442, 369, 470, 377, 462, 410, 429, 407, 432, 281, 558, 414, 425, 247, 592, 277, 562, 271, 568, 272, 567, 264, 575, 259, 580 |
| 562–629 | 237, 602, 239, 600, 244, 595, 243, 596, 275, 564, 278, 561, 250, 589, 246, 593, 417, 422, 248, 591, 394, 445, 393, 446, 370, 469, 365, 474, 300, 539, 299, 540, 364, 475, 362, 477, 298, 541, 312, 527, 313, 526, 314, 525, 353, 486, 352, 487, 343, 496, 327, 512, 350, 489, 326, 513, 319, 520, 332, 507, 333, 506, 348, 491, 347, 492, 322, 517 |
| 630–659 | 330, 509, 338, 501, 341, 498, 340, 499, 342, 497, 301, 538, 366, 473, 401, 438, 371, 468, 408, 431, 375, 464, 249, 590, 269, 570, 238, 601, 234, 605 |
| 660–707 | 257, 582, 273, 566, 255, 584, 254, 585, 245, 594, 251, 588, 412, 427, 372, 467, 282, 557, 403, 436, 396, 443, 392, 447, 391, 448, 382, 457, 389, 450, 294, 545, 297, 542, 311, 528, 344, 495, 345, 494, 318, 521, 331, 508, 325, 514, 321, 518 |
| 708–729 | 346, 493, 339, 500, 351, 488, 306, 533, 289, 550, 400, 439, 378, 461, 374, 465, 415, 424, 270, 569, 241, 598 |
| 730–751 | 231, 608, 260, 579, 268, 571, 276, 563, 409, 430, 398, 441, 290, 549, 304, 535, 308, 531, 358, 481, 316, 523 |
| 752–765 | 293, 546, 288, 551, 284, 555, 368, 471, 253, 586, 256, 583, 263, 576 |
| 766–777 | 242, 597, 274, 565, 402, 437, 383, 456, 357, 482, 329, 510 |
| 778–789 | 317, 522, 307, 532, 286, 553, 287, 552, 266, 573, 261, 578 |
| 790–795 | 236, 603, 303, 536, 356, 483 |
| 796–803 | 355, 484, 405, 434, 404, 435, 406, 433 |
| 804–809 | 235, 604, 267, 572, 302, 537 |
| 810–815 | 309, 530, 265, 574, 233, 606 |
| 816–819 | 367, 472, 296, 543 |
| 820–837 | 336, 503, 305, 534, 373, 466, 280, 559, 279, 560, 419, 420, 240, 599, 258, 581, 229, 610 |

Table 5.7.2-5: Root Zadoff-Chu sequence order for preamble format 4

| Logical root sequence number | Physical root sequence number ![](media_svg/image749.svg) [公式: u](in increasing order of the corresponding logical sequence number) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 – 19 | 1 | 138 | 2 | 137 | 3 | 136 | 4 | 135 | 5 | 134 | 6 | 133 | 7 | 132 | 8 | 131 | 9 | 130 | 10 | 129 |
| 20 – 39 | 11 | 128 | 12 | 127 | 13 | 126 | 14 | 125 | 15 | 124 | 16 | 123 | 17 | 122 | 18 | 121 | 19 | 120 | 20 | 119 |
| 40 – 59 | 21 | 118 | 22 | 117 | 23 | 116 | 24 | 115 | 25 | 114 | 26 | 113 | 27 | 112 | 28 | 111 | 29 | 110 | 30 | 109 |
| 60 – 79 | 31 | 108 | 32 | 107 | 33 | 106 | 34 | 105 | 35 | 104 | 36 | 103 | 37 | 102 | 38 | 101 | 39 | 100 | 40 | 99 |
| 80 – 99 | 41 | 98 | 42 | 97 | 43 | 96 | 44 | 95 | 45 | 94 | 46 | 93 | 47 | 92 | 48 | 91 | 49 | 90 | 50 | 89 |
| 100 – 119 | 51 | 88 | 52 | 87 | 53 | 86 | 54 | 85 | 55 | 84 | 56 | 83 | 57 | 82 | 58 | 81 | 59 | 80 | 60 | 79 |
| 120 – 137 | 61 | 78 | 62 | 77 | 63 | 76 | 64 | 75 | 65 | 74 | 66 | 73 | 67 | 72 | 68 | 71 | 69 | 70 | - | - |
| 138 – 837 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### 5.7.3 Baseband signal generation

The time-continuous random access signal ![](media_svg/image1228.svg) [公式: s(t)] is defined by

![](media_svg/image1229.svg) [公式≈: _{s}_{(}_{t}_{)}_{=}_{Β}_{PRACH}^{N}_{⊆}_{k}^{ZC}_{=}_{0}^{−}^{1}^{N}_{⊆}_{n}^{ZC}_{=}_{0}^{−}^{1}_{x}_{u}_{,}_{v}_{(}_{n}_{)}_{∪}_{e}^{−}^{j}^{2}N^{Π}ZC^{nk}_{∪}_{e}j2Π(k+ϑ+K(k0+^{1}2))δfRA(t−TCP)]

where![](media_svg/image1230.svg) [公式≈: 0≥t<T_{SEQ}+T_{CP}], ![](media_svg/image1231.svg) [公式≈: ^{Β}PRACH] is an amplitude scaling factor in order to conform to the transmit power ![](media_svg/image1232.svg) [公式≈: ^{P}PRACH] specified in clause 6.1 in TS36.213 [4], and ![](media_svg/image1233.svg) [公式≈: ^{k}0^{=}^{n}PRB^{RA}^{N}sc^{RB}^{−}^{N}RB^{UL}^{N}sc^{RB}^{2}]. The location in the frequency domain is controlled by the parameter ![](media_svg/image1234.svg) [公式≈: ^{n}PRB^{RA}] is derived from clause 5.7.1. The factor ![](media_svg/image1235.svg) [公式: K=δfδf_{RA}] accounts for the difference in subcarrier spacing between the random access preamble and uplink data transmission. The variable![](media_svg/image1236.svg) [公式≈: ^{δ}^{f}RA], the subcarrier spacing for the random access preamble, and the variable![](media_svg/image1237.svg) [公式: ϑ], a fixed offset determining the frequency-domain location of the random access preamble within the physical resource blocks, are both given by Table 5.7.3-1.

Table 5.7.3-1: Random access baseband parameters

| Preamble format | ![](media_svg/image1236.svg) [公式≈: ^{δ}^{f}RA] | ![](media_svg/image1238.svg) [公式: ϑ] |
| --- | --- | --- |
| 0 – 3 | 1250 Hz | 7 |
| 4 | 7500 Hz | 2 |

## 5.8 Modulation and upconversion

Modulation and upconversion to the carrier frequency of the complex-valued SC-FDMA baseband signal for each antenna port or the complex-valued PRACH baseband signal is shown in Figure 5.8-1. The filtering required prior to transmission is defined by the requirements in TS36.101 [7].

![](media/image1239.emf)

Figure 5.8-1: Uplink modulation
