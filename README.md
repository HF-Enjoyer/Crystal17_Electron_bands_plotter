# Band structure plot from CRYSTAL17 .BAND file
There exist an online instrument by CRYSTAL17 creators - CRYSPLOT, but images made by CRYSPLOT are not quite suitable for academic works and publications and require additional treatment. Therefore, I made this script. 

## How to work with the code
The script uses two python standard libraries:
- matplotlib
- numpy

All you need is the filename.BAND and labels for special points in the Brillouin zone, which connect the whole BZ path.
First things first, you should pay attention to the part that is restricted by "---" lines. 
Find **labels** lines and put names of special points of BZ in the order of your chosen path. For instance, path:
(0.5, 0, 0.5) -- (0.5, 0.5, 0.5) -- (0, 0, 0) -- (0, 0, 0.5) -- (0.5, 0, 0.5)

It should be labeled like this:
```python
	labels = ['M', 'R', r'$\Gamma$', 'X', 'M']
```
The letter &Gamma; should be typed in LaTeX format: "$\Gamma$".
### Adding Fermi level
To add straight horizontal line right on the Fermi energy, put 1 in the following:
```python
	plot_fermi = 1
```
Below this line you can choose color for the Fermi level

## Saving your bands plot
To save your bands in .png format, put 1 in the following line:
```python
	save_fig = 1
```
Below this line you can choose filename and image dpi.

I added 'Example.BAND' file of KNbO3 cubic modification calculated bands.
"# Crystal17_Electron_bands_plotter" 
