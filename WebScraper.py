import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from bs4 import BeautifulSoup
from datetime import date,datetime

fromad="koulronak@gmail.com"
toad=["ayushkoul33@gmail.com"]
today = date.today()
i=datetime.now()
x=today.strftime("%d")
if(x[0]=='0'):
        d2=today.strftime("%B "+x[1]+", %Y")
else:
        d2 = today.strftime("%B %d, %Y")
file1=open("C://Users/USER/Desktop/"+d2+".txt","a",encoding="utf-8")
print("Today's date:", d2)
file1.write("CURRENT AFFAIRS FOR DATE : " + d2 + "\n\n")
curr_month = str(datetime.now().month)
curr_year = str(datetime.now().year)
url='https://vajiramias.com/current-affairs'
fin_url='/'.join([url, curr_year,curr_month])
#page = requests.get('https://vajiramias.com/current-affairs/2021/4/')
page=requests.get(fin_url)
soup = BeautifulSoup(page.text, 'html.parser')
fi=soup.find_all(class_='box-header')
fi2=soup.find_all(class_='box-body')
title=soup.find_all(class_='feed_item_title')
sub=soup.find_all(class_='feed_item_subtitle')
data=soup.find_all(class_='feed_item_content')
print("\n\n")
i="1"
for (b,c,d,e,g) in zip(fi,title,sub,data,fi2):
    z=b.contents[3].prettify().find(d2)
    if z!=-1:
        print(c.contents[0])
        print(d.contents[0])
        print(e.contents[3].text)
        if g.find(class_="feed_item_important_info_box alert alert-info"):
                print(g.find(class_="feed_item_important_info_box alert alert-info").text)
        print("\n\n")
        file1.write("### "+ i + c.contents[0]+"\n")
        i=str(int(i)+1)
        file1.write(d.contents[0])
        file1.write(e.contents[3].text+"\n")
        if g.find(class_="feed_item_important_info_box alert alert-info"):
                file1.write(g.find(class_="feed_item_important_info_box alert alert-info").text)     
        file1.write("\n\n")
file1.write("Source: VajiRam & Ravi IAS Study Center\nHope you find it useful for most of the Govt Job Exams you are preparing for--\n\t\t\t Ayush Koul-Developer")
file1.close()
#‪C://Users/USER/Desktop/April 14, 2021.docx
msg = MIMEMultipart()
# string to store the body of the mail
body = "Hope you will find it useful.\n All the best\n\n\n From Ayush Koul"
    
# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain')) 

for rec in toad:  
    # storing the senders email address  
    msg['From'] = fromad
    
    # storing the receivers email address 
    msg['To'] = rec
    
    # storing the subject 
    msg['Subject'] = "Current Affairs of "+d2
    
    
    # open the file to be sent 
    filename = d2+".txt"
    attachment = open("C://Users/USER/Desktop/"+d2+".txt", "rb")
    
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    
    # To change the payload into encoded form
    p.set_payload((attachment).read())
    
    # encode into base64
    encoders.encode_base64(p)
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
    
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login(fromad, "@Gmail123")
    
    # Converts the Multipart msg into a string
    text = msg.as_string()
    
    # sending the mail
    s.sendmail(fromad, rec, text)
    
    # terminating the session
    s.quit()
    