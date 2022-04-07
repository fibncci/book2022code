from pythonping import ping
import time

for ip3 in range(28,29):
    for ip4 in range(1,255):
        ip = '192.168.' + str(ip3) +'.' +  str(ip4)
        result = ping(ip)
        if 'Reply' in str(result):
            with open('reachable.txt','a+') as R: # R = file 
                R.write(ip + '\n')
                print(ip + ' is reachable ')
                time.sleep(0.1)
        else: # if 'timed out' in str(result):
            with open('unreached.txt','a+') as R:
                R.write(ip + '\n')
                print(ip + " can't reached")
                time.sleep(0.1)

# for i in range(11,17):
#     ip = '192.168.11.' + str(i)
#     result = ping(ip)
#     if 'Reply' in str(result):
#         print(ip + '可达')
#     else: print(ip + '不可达')