/*
 * Header file for all functions and structures defined in scfbutils_c.c. Must
 * be available for scfbutils.d.pxd file, where all relevant contents must be
 * redclared in appropriate Cython format
 *
 */


/* 
 * Structure/Type Declarations
 * ---------------------------
 */

typedef struct f_node_s{
	double val;
	struct f_node_s *next;	
} f_node;

typedef struct f_list_s{
	struct f_node_s *head;
	int count;
} f_list;

typedef struct fs_struct_s {
	double *freqs;
	double *strengths;
} fs_struct;



/* 
 * Function Declarations
 * ---------------------
 */

double *template_vals_c(double *f_vals, int num_vals, double f0, double sigma, 
					    int num_h);

fs_struct template_adapt_c(f_list **f_estimates, int list_len, double f0,
						   double mu, int num_h, double sigma);

void fl_push(double freq, f_list *l);

double fl_pop(f_list *l);

void init_f_list(f_list *l);

void free_f_list(f_list *l);

double fl_by_idx(int idx, f_list *l);
