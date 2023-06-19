from pyo import *

# class Piano(EventInstrument):
#     def __init__(self, **kwargs):
#         EventInstrument.__init__(self, **kwargs)
#         # تعریف سازنده صدا
#         self.osc = Sine(freq=self.freq, mul=self.vel/127.0)
#         self.envelope = Adsr(attack=.01, decay=.1, sustain=.5, release=.1, dur=self.dur, mul=self.vel/127.0)
#         self.filt = MoogLP(self.osc*self.envelope, freq=self.freq*2, res=0.5)
#         self.out = self.filt.out()

#     def play(self, freq, dur, vel=100):
#         self.freq = midiToHz(freq)
#         self.dur = dur
#         self.vel = vel
#         self.envelope.dur = self.dur
#         self.envelope.mul = self.vel/127.0
#         self.osc.freq = self.freq
#         self.osc.mul = self.vel/127.0

#         self.out.play()

#     def stop(self):
#         self.out.stop()



# from pyo import *

# # ساخت یک شی از کلاس Server
# s = Server().boot()

# # ساخت یک شی از کلاس Sine
# osc = Sine(freq=440, mul=0.2)

# # تعریف ویژگی envelope
# envelope = Adsr(attack=1, decay=2, sustain=0.5, release=1)

# # اتصال ویژگی envelope به ورودی شی osc
# osc_mul = osc * envelope

# # ساخت یک شی از کلاس Thresh
# thresh = Thresh(osc_mul, threshold=0.001)

# # اتصال ورودی شی thresh به خروجی شی s و پخش صدا
# out = thresh.mix(1).out()
# s.start()

# # آغاز کنترل صدا با فعال کردن ویژگی envelope
# envelope.play()

# # منتظر بمانید تا صدا به پایان برسد
# time.sleep(5)

# # متوقف کردن صدا
# envelope.stop()

# # خاموش کردن سرور
# s.stop()



# class Piano(EventInstrument):
#     def __init__(self, **kwargs):
#         EventInstrument.__init__(self, **kwargs)

#         # Define the frequencies of the piano keys
#         key_freqs = [261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30, 440.00, 466.16, 493.88]

#         # Create a list of sine waves with the key frequencies
#         self.sines = [Sine(freq=freq, mul=0.1) for freq in key_freqs]

#         # Create an ADSR envelope
#         self.envelope = Adsr(attack=0.01, decay=0.1, sustain=0.5, release=0.1, dur=1, mul=0.1)

#         # Create a mixer to combine the sine waves
#         self.mixer = Mix(self.sines, mul=self.envelope)

#     def note_on(self, pitch, velocity):
#         # Calculate the index of the sine wave to add to the mixer
#         index = pitch % 12
#         self.mixer.addInput(self.sines[index])

#         # Trigger the envelope
#         self.envelope.play()

#     def note_off(self, pitch):
#         # Calculate the index of the sine wave to remove from the mixer
#         index = pitch % 12
#         self.mixer.delInput(self.sines[index])

#         # Release the envelope
#         self.envelope.release()


# s = Server().boot()

# # Create an instance of the Piano instrument
# piano = Piano()
# envelope = Adsr(attack=1, decay=2, sustain=0.5, release=1)
# # Send the output of the Piano instrument to the server's audio output
# piano.out()

# # Start the server
# s.start()

# # Play a C major chord
# piano.note_on(60, 127)
# piano.note_on(64, 127)
# piano.note_on(67, 127)
# piano.note_off(60)
# piano.note_off(64)
# piano.note_off(67)


# from pyo import *

class Piano(EventInstrument):
    def __init__(self, **kwargs):
        EventInstrument.__init__(self, **kwargs)

        # ایجاد جنراتورهای موج برای تولید صدا
        self.osc1 = Sine(freq=261.63, mul=0.2)
        self.osc2 = Sine(freq=329.63, mul=0.2)

        # ایجاد envelope برای کنترل پویایی صدا
        self.env = Adsr(attack=0.01, decay=0.1, sustain=0.5, release=0.1, dur=self.dur, mul=self.vel)

        # ترکیب و اعمال envelope بر روی جنراتورهای موج
        self.sig = (self.osc1 + self.osc2) * self.env

        # افزودن صدا به لیست صداهای خروجی
        self.add_out(self.sig)


s = Server().boot()

# ایجاد یک اینستنس از کلاس Piano
piano = Piano()

# ارسال یک رویداد MIDI برای پخش صدای پیانو
midi_event = [0, 0, 60, 100]
piano.play_midi_event(midi_event)

s.gui(locals())
