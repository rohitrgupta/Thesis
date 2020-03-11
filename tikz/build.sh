for i in *.tex;do pdflatex -synctex=1 -shell-escape -enable-write18 -interaction=nonstopmode "$i";done
rm *.log
rm *.gz
rm *.aux
rm *.gnuplot
rm *.table
