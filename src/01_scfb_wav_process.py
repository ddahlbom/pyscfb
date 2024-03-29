import sys
import pickle
import scfb
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt


# import wav file
if len(sys.argv)==2:
    f_name = str(sys.argv[1])
    f_s, in_sig = scipy.io.wavfile.read(f_name)
    in_sig = np.array(in_sig, dtype=np.float32)
    in_sig = in_sig/(2**15)
    in_sig = in_sig/np.max(in_sig)
# else:     # linear sliding (dynamic pitch shift example)
#     f_s = 44100
#     dur = 0.5
#     t = np.arange(0,f_s*dur)/f_s
#     in_sig = np.zeros_like(t)
#     num_h = 5
#     f0 = 400.0
#     freqs = np.linspace(f0, f0*1.25, len(t))
#     for p in range(1, num_h+1):
#         in_sig += np.cos(2*np.pi*p*freqs*t)
# else:   # first 8 notes of Die Kunst der Fuge
#     def gen_env(a, d, r, sus_val, dur_n, fs):
#         t_a = np.arange(a*fs)/fs
#         t_d = np.arange(d*fs)/fs
#         t_r = np.arange(r*fs)/fs
#         t_s_n = dur_n - len(t_a) - len(t_d) - len(t_r) 
#         assert dur >= 0
#         gamma = np.log(2)/a
#         seg_a = np.exp(gamma * t_a) - 1
#         gamma = -np.log(sus_val)/d
#         seg_d = np.exp(-gamma*t_d)
#         gamma = np.log(sus_val+1)/r
#         seg_r = (sus_val+1) - np.exp(gamma*t_r)
#         seg_s = np.ones(t_s_n)*sus_val
#         return np.concatenate([seg_a, seg_d, seg_s, seg_r])
#     f_s = 44100
#     dt = 1/f_s
#     num_h = 10 
#     d = 293.6648; a = 440.0; f = 349.2282; cs = 277.1826; e = 329.6276;
#     dur = 0.100     # eighth note duration
#     freqs = [d, a, f, d, cs, d, e, f]
#     durs = [4*dur, 4*dur, 4*dur, 4*dur, 4*dur, 2*dur, 2*dur, 5*dur]
#     notes = []
#     for k, freq in enumerate(freqs):
#         num_cycles = int(durs[k]*freq)
#         t = np.arange(0, num_cycles/freq, dt)
#         note = np.zeros_like(t)
#         for n in range(num_h):
#             note += ((1/(n+1))**0.1)*np.cos(2*np.pi*freq*(n+1)*t)
#         note = note * gen_env(0.02, durs[k] - 0.045, 0.02, 0.65, len(note), f_s)
#         notes.append(note)
#     in_sig = np.concatenate(notes)
#     in_sig /= np.max(in_sig)
#     in_sig += np.random.normal(scale=np.sqrt(0.0000000001 * f_s / 2), size=in_sig.shape)
#     scipy.io.wavfile.write("dkdf.wav", f_s, in_sig)
#     in_sig *= 4 
# else:   # first note of Die Kunst der Fuge
#     def gen_env(a, d, r, sus_val, dur_n, fs):
#         t_a = np.arange(a*fs)/fs
#         t_d = np.arange(d*fs)/fs
#         t_r = np.arange(r*fs)/fs
#         t_s_n = dur_n - len(t_a) - len(t_d) - len(t_r) 
#         assert dur >= 0
#         gamma = np.log(2)/a
#         seg_a = np.exp(gamma * t_a) - 1
#         gamma = -np.log(sus_val)/d
#         seg_d = np.exp(-gamma*t_d)
#         gamma = np.log(sus_val+1)/r
#         seg_r = (sus_val+1) - np.exp(gamma*t_r)
#         seg_s = np.ones(t_s_n)*sus_val
#         return np.concatenate([seg_a, seg_d, seg_s, seg_r])
#     f_s = 44100
#     dt = 1/f_s
#     num_h = 10 
#     d = 293.6648; a = 440.0; f = 349.2282; cs = 277.1826; e = 329.6276;
#     dur = 0.100     # eighth note duration
#     freqs = [d]
#     durs = [4*dur]
#     notes = []
#     for k, freq in enumerate(freqs):
#         num_cycles = int(durs[k]*freq)
#         t = np.arange(0, num_cycles/freq, dt)
#         note = np.zeros_like(t)
#         for n in range(num_h):
#             note += ((1/(n+1))**0.1)*np.cos(2*np.pi*freq*(n+1)*t)
#         note = note * gen_env(0.02, durs[k] - 0.045, 0.02, 0.65, len(note), f_s)
#         notes.append(note)
#     in_sig = np.concatenate(notes)
#     in_sig /= np.max(in_sig)
#     in_sig += np.random.normal(scale=np.sqrt(0.0000000001 * f_s / 2), size=in_sig.shape)
#     scipy.io.wavfile.write("dkdf.wav", f_s, in_sig)
#     in_sig *= 4 
# else:
#     f_s = 44100
#     dt = 1/f_s
#     num_h = 10
#     # freqs = [300, 300.*(5/4), 300.*(3/2)]
#     freqs = [300, 300.*(3/2)]
#     dur = 0.2
#     t = np.arange(dur*f_s)/f_s
#     in_sig = np.zeros_like(t)
#     for freq in freqs:
#         for p in range(1, num_h+1):
#             in_sig += ((1/p)**0.0)*np.cos(2*np.pi*freq*p*t +
#                     np.random.random(1)*2*np.pi)
#     in_sig /= np.max(in_sig) 
else:     # two notes with pause
    f_s = 44100
    dt = 1./f_s
    note_dur = 0.200
    pause_dur = 0.020
    freqs = [293.6649, 440.0] # D3, A4
    num_h = 6
    periods = int(note_dur//(1/freqs[0]))
    dur_1 = periods/freqs[0]
    periods = int(note_dur//(1/freqs[1]))
    dur_2 = periods/freqs[1]
    sig1 = np.concatenate([np.sin(2*np.pi*freqs[0]*np.arange(0, dur_1, dt)),
                           np.zeros(int(pause_dur/dt)),
                           np.sin(2*np.pi*freqs[1]*np.arange(0, dur_2, dt))])
    for p in range(2, num_h+1):
        sig1 += np.concatenate([np.sin(2*np.pi*p*freqs[0]*np.arange(0, dur_1, dt)),
                               np.zeros(int(pause_dur/dt)),
                               np.sin(2*np.pi*p*freqs[1]*np.arange(0, dur_2, dt))])
    in_sig = sig1
    print("in_sig shape", type(in_sig), in_sig.dtype)
    in_sig /= np.max(in_sig)
# else:   # single tones for butte diagram
#     f_s = 44100
#     dt = 1/f_s
#     num_h = 1
#     # freqs = [300, 300.*(5/4), 300.*(3/2)]
#     freqs = [300, 500]
#     dur = 0.2
#     t = np.arange(dur*f_s)/f_s
#     in_sig = np.zeros_like(t)
#     for freq in freqs:
#         for p in range(1, num_h+1):
#             in_sig += ((1/p)**0.0)*np.cos(2*np.pi*freq*p*t +
#                     np.random.random(1)*2*np.pi)
#     in_sig /= np.max(in_sig) 
#     print("in_sig shape", in_sig.shape, type(in_sig), in_sig.dtype)
# else:
#     f_s = 44100
#     dt = 1/f_s
#     f0 = 200
#     T = 1/f0
#     num_h = 6
#     dur = 1.5
#     dur = dur - dur%T
#     dur_s = int(dur/dt)
#     t = np.arange(0, dur, dt)
#     t = t[:-2]
#     taper = np.concatenate([np.ones(int((dur/2)//dt)), np.linspace(1, 0, int(dur_s//2))])
#     f_keep = [400., 800., 1200.]
#     f_kill = [600]
#     sig2 = np.zeros_like(t)
#     sig_tail = np.zeros_like(t)
#     for f in f_keep:
#         sig2 += np.sin(2*np.pi*f*t)
#     for f in f_kill:
#         sig2 += np.sin(2*np.pi*f*t)*taper
#     for f in f_keep:
#         sig_tail += np.sin(2*np.pi*f*t)
#     in_sig = np.concatenate([sig2, sig_tail])
#     in_sig /= np.max(in_sig)

# process through SCFB
peri = scfb.SCFB(100., 4000., 100, f_s, filt_type='gammatone', bounding=True)
# peri = scfb.SCFB(250., 350., 10, f_s, filt_type='gammatone')
peri.process_signal(in_sig, verbose=True)
sig_len_n = len(in_sig)

# plot results
fig = plt.figure()
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

ax1.plot(np.arange(len(in_sig))/f_s, in_sig, color='808080', linewidth=0.5)

times = np.arange(len(in_sig))/f_s
for n in range(peri.num_chan):
    ax2.plot(times, peri.filtered_channels[n,:] + n, color='808080',
            linewidth=0.7)
    
idcs = np.arange(0, peri.num_chan, 5)
ax2.set_yticks(idcs)
labels = ["{:.1f}".format(f) for f in peri.f_c[idcs]]
ax2.set_yticklabels(labels)

for fdl in peri.fdl:
    ax3.plot(np.arange(0,len(in_sig))/f_s, fdl.f_record, linewidth=0.7,
            color='808080', linestyle='--')
peri.plot_output(ax3)

# fig2 = plt.figure()
# ax1 = fig2.add_subplot(1,1,1)
# print(len(peri.out_chunks))
# for i in range(len(peri.out_chunks)):
#     ax1.plot(peri.out_chunks[i])

plt.show()
# write ordered data to file (for template processing)
pickle.dump((peri.chunks, sig_len_n), open("chunks.pkl", "wb"))

