# qe_plotter
program for plotting gnu files generated from a quantum espresso bands.x or dos.x calculation using python

Command to execute from terminal: python3 qe_plotter.py  (or python qe_plotter.py, depends on the version)

Needs the .gnu file generated from a bands.x calculation using quantum espresso or the .dos file generated from a dos.x calculation using quantum espresso as input file. Optional: use a k points input file where the first column is the k point label (Gamma, M ,...) and the second is the relative x coordinate in which you want to put the label.

The output file is a plot image, all python supported output images can be selected by choosing the relative extension when naming the output file from terminal.

As an example, I have added to the repository a dos.x output file and the relative pdf showing the density of states plot using this program. The quantum sistem is WSe2. 
