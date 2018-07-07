'''
The declaration file for any pure C functions or structures defined in
scfbutils_c.c and declared (in C) in scfbutils_c.h.
'''

cdef extern from "scfbutils_c.h":
    ctypedef struct f_node:
        pass

    ctypedef struct f_list:
        pass

    ctypedef struct fs_struct:
        double *freqs
        double *strengths

    double *template_vals_c(double *f_vals, int num_vals, double f0, 
            double sigma, int num_h)

    fs_struct template_adapt_c(f_list **f_estimates, int list_len, 
            double f0, double mu, int num_h, double sigma)

    void init_f_list(f_list *l)

    void free_f_list(f_list *l)

    void fl_push(double freq, f_list *l)

    double fl_pop(f_list *l)

    double fl_by_idx(int idx, f_list *l)
