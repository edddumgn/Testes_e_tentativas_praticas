import time

def cont_reg(time_sec):
	while time_sec:
		mins, secs = divmod(time_sec, 60)
		formato_tempo = f'{mins}:{secs}'
		
		print(formato_tempo, end='\r')
		time.sleep(1)
		time_sec -= 1
		
		print('Stop')
		
num = int(input('Defina o tempo do seu contador: '))

cont_reg(num)
