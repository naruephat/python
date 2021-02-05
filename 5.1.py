class st :
    def __init__(self,name,sex,year,study):
        self.name = name
        self.sex = sex
        self.year = year
        self.study = study

    def showstudent(self) :
       print("name:sex:year:study:")    
       print("name :",self.name,end=(' '))
       print("sex :",self.sex,end=(' '))
       print("year :",self.year,end=(' '))
       print("study :",self.study)
x = st("นฤพัทธ์ นามมงคุณ","ชาย","1","com education")
x.showstudent()