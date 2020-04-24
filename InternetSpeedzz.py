import os,time
i=0;A='     '
while True:
 out = os.popen('''ping -c 1 www.google.com''').read()
 out = (out).split()[14].replace('time=','').split('.')
 out2 = eval(out[0])-7
 if i==10:A='    '
 if i==100:A='   '
 if out2<=50:print(f'[{i}]'+A+str(''.join(out[0]))+'  '+(':'*out2))
 i+=1
 if i>=500:
  os.system('clear');i=0;A='     '
