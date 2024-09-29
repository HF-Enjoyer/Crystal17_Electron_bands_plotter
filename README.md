# Band structure plot from CRYSTAL17 .BAND file
There exist an online instrument by CRYSTAL17 creators - CRYSPLOT, but images made by CRYSPLOT are not quite suitable for academic works and publications and require additional treatment. Therefore, I made this script. 

## How to use
The script uses two python standard libraries:
- matplotlib
- numpy

Just cmd in your working directory
```python
	py bands.py <filename>
```
Then follow the instructions.

# Example:

```python
	size of the figure <x y>: 9 10
	Title of the graph, fontsize <title, number>: My bands, 16
	Title of y axis, fontsize e.g. <Energy, ev; 16>: Energy, eV; 16
	add BZ path  e.g. <M, Gamma, X, K, M>: Gamma, X, M, R, Gamma
	fontsize for BZ labels: 14
	plot grid? <y/n>: y
	Plot Fermi level? <y/n>: y
```
You can find .png of your bands in your working directory
