import numpy as np
import pickle
import matplotlib.pyplot as plt
import scfb 
import scfbutils

################################################################################
if __name__=="__main__":
    chunks, sig_len_n = pickle.load(open("chunks.pkl", "rb"))
    freqs = np.logspace(np.log10(50.0), np.log10(4000.0), 100)
    lims = np.sqrt(freqs[0:-1]*freqs[1:])
    lims = np.concatenate([[0], lims, [20000]])
    # limits = []
    # for k in range(len(freqs)):
    #     limits.append((lims[k], lims[k+1]))
    limits = [(lims[k], lims[k+1]) for k in range(len(freqs))]
    # freqs = np.linspace(50.0, 4000.0, 100)
    bump_heights = [(1/k)**0.9 for k in range(1,7)]
    bump_heights = np.array(bump_heights)
    sigma = 0.03 
    mu = 1
    # turn on limits if want to eliminate "butte" behavior
    temp_array = scfb.TemplateArray(chunks, sig_len_n, freqs, sigma,
            bump_heights, mu)#, limits=limits)
    temp_array.adapt(verbose=True)

    pickle.dump((temp_array.templates, freqs), open('template_data.pkl', 'wb'))
