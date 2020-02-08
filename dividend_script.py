from bs4 import BeautifulSoup
import csv
from datetime import datetime
def read_data():
        company_list=[]
        for x in range(1,65):
            #print("C:\\Users\\H1rop\\Downloads\\"+str(x)+".html")
            soup = BeautifulSoup(open("C:\\Users\\H1rop\\Downloads\\"+str(x)+".html"), "html.parser")
            rows = soup.find_all('tr', {'class' : 'market-calendar-table__row'})
            symbol=""
            company_name=""
            ex_date=""
            pay_date=""
            div_amount=""
            for row in rows:
                count=1
                company_name=""
                symbol=""
                ex_date=1/1/2020
                pay_date=1/1/2020
                div_amount=0.00
                for cell in row:
                        data=cell.find_all('div',{'class':'market-calendar-table__cell-content'})
                        if(count==1):
                            company_name=data[0].text.replace(',', '')
                        if(count==2):
                            symbol=data[0].text.replace(',', '')
                        if(count==3):
                            ex_date=data[0].text.replace(',', '')
                        if(count==4):
                            pay_date=data[0].text.replace(',', '')
                        if(count==5):
                            pass
                        if(count==6):
                            div_amount=data[0].text.replace(',', '')
                        count+=1

                        #print(company_name+" "+symbol+" "+ex_date+" "+pay_date+" "+div_amount)
                company=[company_name,symbol,ex_date,pay_date,div_amount]
                print(company)
                company_list.append(company)
        sort_listed = sorted(company_list , key=lambda x: datetime.strptime(x[3],"%m/%d/%Y"))

        return(sort_listed)
def write_to_csv(company):
    with open('C:\\Users\\H1rop\\Desktop\\dump.csv', mode='w') as file:
        file_writer = csv.writer(file, delimiter='\n', lineterminator='\n', quoting=csv.QUOTE_NONE,escapechar='\\')
        file_writer.writerow(company)


##def get_key(phone_record):
##  return datetime.strptime(phone_record[1], '%d %B %Y')
 

      
##def convert_date(date):
##    new_date= datetime.strptime(date , '%m/%d/%Y').date()
##    return new_date



##def sort_tuple(unsorted_tuple):
##    return sorted_tuple


write_to_csv(read_data())

