import yagmail
import smtplib
import sys
#mail listesi oluşturuldu
while True:
    with open("mailler.txt","r") as file:
        mail_listesi=file.read().split("\n")
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        #sunucuya bağlanıldı.
        yag=yagmail.SMTP("yourmail@adress","yourpassword")
        #mail metni oluşturulldu
        konusu = input("konu yazın")
        metin=input("içerik yazın:")
        #mail gönderme işlemleri yapıldı
    try:
        for mail in mail_listesi:
            yag.send(to=mail,subject=konusu,contents=metin)
            print("{} mail adresine gönderilmiştir.".format(mail))
            yag.close()

    except:
            sys.stderr.write("Başardınız! Mail/mailler gönderildi.\n")
            sys.stderr.flush()


