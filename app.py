import pyperclip
#pyperclip.copy('test')
print(pyperclip.paste())
dictKeyboard={'q':'й','w':'ц','e':'у','r':'к','t':'е','y':'н','u':'г','i':'ш','o':'щ','p':'з','[':'х',']':'ъ',
              'Q':'Й','W':'Ц','E':'У','R':'К','T':'Е','Y':'Н','U':'Г','I':'Ш','O':'Щ','P':'З','{':'Х','}':'Ъ',
              'a':'ф','s':'ы','d':'в','f':'а','g':'п','h':'р','j':'о','k':'л','l':'д',';':'ж',"'":'э',
              'A':'Ф','S':'Ы','D':'В','F':'А','G':'П','H':'Р','J':'О','K':'Л','L':'Д',':':'Ж','"':'Э',
              'z':'я','x':'ч','c':'с','v':'м','b':'и','n':'т','m':'ь',',':'б','.':'ю','/':'.',
              'Z':'Я','X':'Ч','C':'С','V':'М','B':'И','N':'Т','M':'Ь','<':'Б','>':'Ю','?':',',
              '@':'"', '#':'№','$':';','^':':','&':'?',' ':' '


}
def changeInvalidText(dictKeyboard):
    result=''
    buf=pyperclip.paste()
    for item in buf:
        result+=dictKeyboard[item]
    pyperclip.copy(result)

changeInvalidText(dictKeyboard)
