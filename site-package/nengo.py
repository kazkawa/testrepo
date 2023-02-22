print('このPythonファイルでは西暦を和暦に自動で変換します。\n')

year = input('調べたい年号を西暦４桁で入力してください：\n')

reiwa = int(year)-2018

if reiwa >= 2:
    print('西暦',year,'年は令和',reiwa,'年です。')
    
if reiwa == 1:
    print('西暦',year,'年は令和元年です。')

if reiwa <= 0:
    print('西暦',year,'年はまだ平成です。')