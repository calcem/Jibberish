import random
class Jibberish:

	
	

	def makeJib():
		para =" "
		for i in range(0,100):
			letters = random.randint(1,7)
			for j in range(0,letters):
				let = random.randint(1,26)
				if let == 1:	  
					para +="a"
				elif let ==2:
					para +="b"
				elif let ==3:
					para +="c"
				elif let ==4:
					para +="d"
				elif let ==5:
					para +="e"
				elif let ==6:
					para +="f"
				elif let ==7:
					para +="g"
				elif let ==8:
					para +="h"
				elif let ==9:
					para +="i"
				elif let ==10:
					para +="j"
				elif let ==11:
					para +="k"
				elif let ==12:
					para+="l"
				elif let ==13:
					para +="m"
				elif let ==14:
					para+="n"
				elif let ==15:
					para +="o"
				elif let ==16:
					para +="p"
				elif let ==17:
					para +="q"
				elif let ==18:
					para +="r"
				elif let ==19:
					para +="s"
				elif let ==20:
					para +="t"
				elif let ==21:
					para +="u"
				elif let ==22:
					para +="v"
				elif let ==23:
					para +="w"
				elif let ==24:
					para +="x"
				elif let ==25:
					para +="y"
				elif let ==26:				
					para +="z"
			para +=" "

		return para
					
