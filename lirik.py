import sys
import time

def jalanin_lirik():
    lirik = [
        ("Hold on and hope that we'll find our way back in the end", 0.07),
        ("Do you think I have forgotten ?", 0.1),
        ("Do you think I have forgotten ? ", 0.1),         
        ("Do you think I have forgotten about you ?", 0.1),
        ("Do you think I have forgotten ?", 0.1),
        ("Do you think I have forgotten ? ", 0.1),         
        ("Do you think I have forgotten about you ?", 0.1),
    ]

    delay = [5.3, 2, 2, 6 , 2, 2,2 ]

    print("\nAbout You - The 1975")
    time.sleep(2)

    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
      
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('') 

    print("code by: kolskY")


jalanin_lirik()
