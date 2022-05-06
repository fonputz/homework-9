abetka = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
abetka_L = ['А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я']
 



#Функція яке показує номер букви
def ord_ua(a):
  if a.isupper():
    return abetka_L.index(a)
    
  else:
    return abetka.index(a)

#Ф. яка повертає букву за номером
def chr_ua(a):
  return abetka[a]
#Ф. яка повертає ВЕЛИКУ букву за номером
def chr_L_ua(a):
  return abetka_L[a]


#Ф. яка шифрує


def tochp_ua (text, key):
  key_len = len(key)
  key_as_int = [ord_ua(i) for i in key.lower()]
  ciphertext = ''
  j = 0
  for i in text:
  #шифруємо і записуємо результат в список
    if i == ' ':
      ciphertext += ' '
    elif i.isdigit():
      ciphertext += str((int(i)+key_as_int[j%key_len]))%10
    else:
      if i.isupper():  
    #число по абеткі + індекс шифрування "ділим" 26 = нове число за абеткою(зашифрована правильно буква)
        new_index = (ord_ua(i) +key_as_int[j%key_len])%33
    # отримуєм саму букву = нчза+ ord('a')
        ciphertext+= chr_L_ua(new_index)
      elif i.islower():
    #число по абеткі + індекс шифрування "ділим" 26 = нове число за абеткою(зашифрована правильно буква)
        new_index = (ord_ua(i) +key_as_int[j%key_len])%33
    # отримуєм саму букву = нчза+ ord('a')
 
        ciphertext += chr_ua(new_index)
    j+=1
  return ciphertext

#Ф. Розшифровуває
def frchp_ua (text, key):
  key_len = len(key)
  key = key.lower()
  key_as_int = [ord_ua(i) for i in key]
  ciphertext = ''
  j = 0
  for i in text:
  #шифруємо і записуємо результат в список
    if i == ' ':
      ciphertext += ' '
    elif i.isdigit():
      ciphertext += str((int(i)-key_as_int[j%key_len]))%10
    else:
      if i.isupper():  
    #число по абеткі + індекс шифрування "ділим" 26 = нове число за абеткою(зашифрована правильно буква)
        new_index = (ord_ua(i) - key_as_int[j%key_len])%33
    # отримуєм саму букву = нчза+ ord('a')
        ciphertext+= chr_L_ua(new_index)
      elif i.islower():
    #число по абеткі + індекс шифрування "ділим" 26 = нове число за абеткою(зашифрована правильно буква)
        new_index = (ord_ua(i) - key_as_int[j%key_len])%33
    # отримуєм саму букву = нчза+ ord('a')
 
        ciphertext += chr_ua(new_index)
    j+=1
  return ciphertext
        

t = input('Enter Text')
k = input('Enter key')

print(tochp_ua(t,k))
z = tochp_ua(t,k)
print(frchp_ua(z,k))
