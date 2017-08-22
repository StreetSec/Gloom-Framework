import os
import sys
import time
import random
from termcolor import colored, cprint

def load_banner():
	"""
		This Function allows me to randomly load banners
		for the main program.

	"""

	banner1 = colored(''' 
			
			
	  ________.__                          
	 /  _____/|  |   ____   ____   _____   
	/   \  ___|  |  /  _ \ /  _ \ /     \  
	\    \_\  \  |_(  <_> |  <_> )  Y Y  \ 
 	\______  /____/ \____/ \____/|__|_|  / 
               \/                          \/  
			
				- Security Framework 	
			
		''', 'green')

	banner2 = colored(''' 
			
			
	      >===>     >=>                                           
	    >>    >=>   >=>                                           
	    >=>          >=>    >=>        >=>     >===>>=>>==>        
	    >=>          >=>  >=>  >=>   >=>  >=>   >=>  >>  >=>       
	    >=>   >===>  >=> >=>    >=> >=>    >=>  >=>  >>  >=>       
	     >=>    >>   >=>  >=>  >=>   >=>  >=>   >=>  >>  >=>       
	       >====>    >==>    >=>        >=>     >==>  >>  >=>       
		                                                                  
			
			      :: Framework ::
			
			''', 'yellow')

	banner3 = colored(''' 
			
			
	___________   ________________________
	7     77  7   7     77     77        7
	|   __!|  |   |  7  ||  7  ||  _  _  |
	|  !  7|  !___|  |  ||  |  ||  7  7  |
	|     ||     7|  !  ||  !  ||  |  |  |
	!_____!!_____!!_____!!_____!!__!__!__!
		                                      
			
		''', 'red')


	headers = [banner1, banner2, banner3]
	random_choice = headers[random.randint(0, 2)] 
	print random_choice


