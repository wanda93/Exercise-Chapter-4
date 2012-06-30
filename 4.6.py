
def total (hour,rate):		#bagian dari pendeklerasian fungsi
	jam = float(hour)
	byr = float(rate)


	if jam < 40:		#bagian pengecekan
   	  byarn = jam * byr
          print byarn

	else :
   	  nrmal = 40 * byr
   	  ext = jam - 40
   	  rte = (byr*3/2) * ext
  	  total = nrmal + rte	
  	  print "pay :", float(total)

hours = raw_input ('Enter Hours:')	
rates  = raw_input ('Enter Rate:')

total(hours,rates)		#bagian memanggil fungsi
