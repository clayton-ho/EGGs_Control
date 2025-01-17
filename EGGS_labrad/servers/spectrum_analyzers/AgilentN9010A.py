import numpy as np
from labrad.gpib import GPIBDeviceWrapper
from twisted.internet.defer import inlineCallbacks, returnValue


class AgilentN9010AWrapper(GPIBDeviceWrapper):

    # SYSTEM
    @inlineCallbacks
    def reset(self):
        yield self.write('*RST')

    @inlineCallbacks
    def clear_buffers(self):
        yield self.write('*CLS')

    @inlineCallbacks
    def autoset(self):
        yield self.write(':SENS:POW:ATUN')


    # ATTENUATION
    @inlineCallbacks
    def preamplifier(self, status):
        raise NotImplementedError

    @inlineCallbacks
    def attenuation(self, att):
        if att is not None:
            if (att > 0) and (att < 60):
                yield self.write(':POW:ATT {:f}'.format(att))
            else:
                raise Exception('Error: RF attenuation must be in range: [0, 60].')
        resp = yield self.query(':POW:ATT?')
        returnValue(float(resp))


    # FREQUENCY RANGE
    @inlineCallbacks
    def frequencyStart(self, freq):
        if freq is not None:
            if (freq > 0) and (freq < 7.5e9):
                yield self.write(':SENS:FREQ:STAR {:f}'.format(freq))
            else:
                raise Exception('Error: start frequency must be in range: [0, 7.5e9].')
        resp = yield self.query(':SENS:FREQ:STAR?')
        returnValue(float(resp))

    @inlineCallbacks
    def frequencyStop(self, freq):
        if freq is not None:
            if (freq > 0) and (freq < 7.5e9):
                yield self.write(':SENS:FREQ:STOP {:f}'.format(freq))
            else:
                raise Exception('Error: stop frequency must be in range: [0, 7.5e9].')
        resp = yield self.query(':SENS:FREQ:STOP?')
        returnValue(float(resp))

    @inlineCallbacks
    def frequencyCenter(self, freq):
        if freq is not None:
            if (freq > 0) and (freq < 7.5e9):
                yield self.write(':SENS:FREQ:CENT {:f}'.format(freq))
            else:
                raise Exception('Error: center frequency must be in range: [0, 7.5e9].')
        resp = yield self.query(':SENS:FREQ:CENT?')
        returnValue(float(resp))

    @inlineCallbacks
    def frequencySpan(self, span):
        if span is not None:
            if (span > 0) and (span < 7.5e9):
                yield self.write(':SENS:FREQ:SPAN {:f}'.format(span))
            else:
                raise Exception('Error: frequency span must be in range: [0, 7.5e9].')
        resp = yield self.query(':SENS:FREQ:SPAN?')
        returnValue(float(resp))


    # AMPLITUDE
    @inlineCallbacks
    def amplitudeReference(self, ampl):
        if ampl is not None:
            if (ampl > -100) and (ampl < 20):
                yield self.write(':DISP:WIND:TRAC:Y:SCAL:RLEV {:f}'.format(ampl))
            else:
                raise Exception('Error: display reference value must be in range: [-100, 20].')
        resp = yield self.query(':DISP:WIND:TRAC:Y:SCAL:RLEV?')
        returnValue(float(resp))

    @inlineCallbacks
    def amplitudeOffset(self, ampl):
        if ampl is not None:
            if (ampl > -300) and (ampl < 300):
                yield self.write(':DISP:WIND:TRAC:Y:SCAL:RLEV:OFFS {:f}'.format(ampl))
            else:
                raise Exception('Error: display offset must be in range: [-300, 300].')
        resp = yield self.query(':DISP:WIND:TRAC:Y:SCAL:RLEV:OFFS?')
        returnValue(float(resp))

    @inlineCallbacks
    def amplitudeScale(self, factor):
        if factor is not None:
            if (factor > 0.1) and (factor < 20):
                yield self.write(':DISP:WIND:TRAC:Y:SCAL:PDIV {:f}'.format(factor))
            else:
                raise Exception('Error: display scale must be in range: [0.1, 20].')
        resp = yield self.query(':DISP:WIND:TRAC:Y:SCAL:PDIV?')
        returnValue(float(resp))

    # todo: account for OFF in marker mode
    # todo: marker track problem
    # MARKER SETUP
    @inlineCallbacks
    def markerToggle(self, channel, status):
        if status is not None:
            yield self.write(':CALC:MARK{:d}:STAT {:d}'.format(channel, status))
        resp = yield self.query(':CALC:MARK{:d}:STAT?'.format(channel))
        returnValue(bool(int(resp)))

    @inlineCallbacks
    def markerTrace(self, channel, trace):
        if trace is not None:
            yield self.write(':CALC:MARK{:d}:TRAC {:d}'.format(channel, trace))
        resp = yield self.query(':CALC:MARK{:d}:TRAC?'.format(channel))
        returnValue(int(resp))

    @inlineCallbacks
    def markerMode(self, channel, mode):
        modeConvert = {0: 'POS', 1: 'DELT', 2: 'BAND', 3: 'SPAN'}
        modeInvert = {val: key for key, val in modeConvert.items()}
        if mode is not None:
            mode = modeConvert[mode]
            yield self.write(':CALC:MARK{:d}:MODE {:s}'.format(channel, mode))
        resp = yield self.query(':CALC:MARK{:d}:MODE?'.format(channel))
        returnValue(modeInvert[resp])

    @inlineCallbacks
    def markerReadoutMode(self, channel, mode):
        modeConvert = {0: 'FREQ', 1: 'TIME', 2: 'ITIM', 3: 'PER'}
        modeInvert = {val: key for key, val in modeConvert.items()}
        if mode is not None:
            mode = modeConvert[mode]
            yield self.write(':CALC:MARK{:d}:X:READ {:s}'.format(channel, mode))
        resp = yield self.query(':CALC:MARK{:d}:X:READ?'.format(channel))
        returnValue(modeInvert[resp])

    @inlineCallbacks
    def markerTrack(self, channel, status):
        if status is not None:
            yield self.write(':CALC:MARK{:d}:TRCK:STAT {:d}'.format(channel, status))
        resp = yield self.query(':CALC:MARK{:d}:TRCK:STAT?'.format(channel))
        returnValue(bool(int(resp)))


    # MARKER READOUT
    @inlineCallbacks
    def markerAmplitude(self, channel):
        resp = yield self.query(':CALC:MARK{:d}:Y?'.format(channel))
        returnValue(float(resp))

    @inlineCallbacks
    def markerFrequency(self, channel, freq):
        if freq is not None:
            if (freq > 0) and (freq < 1.5e9):
                yield self.write(':CALC:MARK{:d}:X {:f}'.format(channel, freq))
            else:
                raise Exception('Error: marker frequency must be in range: [0, 1.5e9].')
        resp = yield self.query(':CALC:MARK{:d}:X?'.format(channel))
        returnValue(float(resp))


    # MARKER-RELATED PEAK FUNCTIONS
    @inlineCallbacks
    def peakSearch(self, status):
        # todo: fix, current implementation is wrong is wrong
        return NotImplementedError
        # if status is not None:
        #     yield self.write(':CALC:MARK:CPE:STAT {:d}'.format(status))
        # resp = yield self.query(':CALC:MARK:CPE:STAT?')
        # returnValue(bool(int(resp)))

    @inlineCallbacks
    def peakSet(self, channel):
        yield self.write(':CALC:MARK{:d}:MAX'.format(channel))


    @inlineCallbacks
    def peakNext(self, channel):
        yield self.write(':CALC:MARK{:d}:MAX:NEXT'.format(channel))


    # PEAKS ONLY
    @inlineCallbacks
    def peakThreshold(self, threshold):
        if threshold is not None:
            if (threshold > -200) and (threshold < 30):
                yield self.write(':CALC:MARK:PEAK:THR {:f}'.format(threshold))
            else:
                raise Exception('Error: peak threshold must be in range: [-200, 30].')

        resp = yield self.query(':CALC:MARK:PEAK:THR?')
        returnValue(float(resp))

    @inlineCallbacks
    def peakExcursion(self, excursion):
        if excursion is not None:
            if (excursion > 0) and (excursion < 100):
                yield self.write(':CALC:MARK:PEAK:EXC {:f}'.format(excursion))
            else:
                raise Exception('Error: peak excursion must be in range: [0, 100].')

        resp = yield self.query(':CALC:MARK:PEAK:EXC?')
        returnValue(float(resp))

    @inlineCallbacks
    def peakTable(self):
        # todo: fix - need to obligately specify excursion and threshold for this measurement
        # parse response
        resp = yield self.query(':CALC:DATA1:PEAK?')
        resp = [float(val) for val in resp.split(',')]

        # separate amplitude and frequency
        amp_list = resp[1::2]
        freq_list = resp[2::2]

        return list(zip(freq_list, amp_list))


    # BANDWIDTH
    @inlineCallbacks
    def bandwidthSweepTime(self, time):
        if time is not None:
            if (time > 2e-6) and (time < 7500):
                yield self.write(':SENS:SWE:TIME {:f}'.format(time))
            else:
                raise Exception('Error: sweep time must be in range: [2e-6, 7500].')
        resp = yield self.query(':SENS:SWE:TIME?')
        returnValue(float(resp))

    @inlineCallbacks
    def bandwidthResolution(self, bw):
        if bw is not None:
            if (bw > 1) and (bw < 1e7):
                yield self.write(':SENS:BAND:RES {:f}'.format(bw))
            else:
                raise Exception('Error: resolution bandwidth must be in range: [1, 1e7].')
        resp = yield self.query(':SENS:BAND:RES?')
        returnValue(float(resp))

    @inlineCallbacks
    def bandwidthVideo(self, bw):
        if bw is not None:
            if (bw > 1) and (bw < 1e7):
                yield self.write(':SENS:BAND:VID {:f}'.format(bw))
            else:
                raise Exception('Error: video bandwidth must be in range: [1, 1e7].')
        resp = yield self.query(':SENS:BAND:VID?')
        returnValue(float(resp))


    # TRACE
    @inlineCallbacks
    def getTrace(self, channel):
        # set data format
        yield self.write(':FORM:TRAC:DATA ASC')

        # get data
        data = yield self.query(':TRAC:DATA? TRACE{:d}'.format(channel))
        data = self._processData(data)

        # create x-axis
        freq_start = yield self.query(':SENS:FREQ:START?')
        freq_stop = yield self.query(':SENS:FREQ:STOP?')
        xAxis = np.linspace(int(freq_start), int(freq_stop), len(data))

        returnValue((xAxis, data))


    # HELPER
    def _processData(self, data):
        """
        Process data for header and separate data values.
        """
        # header is in #NXXXXXXXXX format
        tmc_N = int(data[1])

        # remove header and split data
        processed_data = np.array(data[2 + tmc_N:].split(', '), dtype=float)
        return processed_data
