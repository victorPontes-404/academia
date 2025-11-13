import os
import time

def limpar():
     """
     limpa o terminal
     """
     _ = os.system("clear")

def delay(tempo):
     """
     tempo de espera
     """
     time.sleep(tempo)