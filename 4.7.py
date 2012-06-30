def total (enter,score):	#bagian fungsi
	

  if score >= 1.0:		#bagian pengecekan
        print 'Bad Score'

  elif score >= 0.9:
        print 'A'	

  elif score >= 0.8:
	print 'B'

  elif score >= 0.7:
        print 'C'

  elif score >= 0.6:
        print 'D'

  elif score < 0.6:
	print 'E'

  elif score > 10:
	print 'Error'



enter = raw_input ('Enter Score:')
score = float(enter)


total (enter,score)		#bagian pemanggilan fungsi
