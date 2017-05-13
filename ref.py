
# coding:utf-8

fin=open("ref.txt", "r", encoding='UTF-8');
fout=open("refadv.txt", "w", encoding='UTF-8');

while True:
    line = fin.readline();
    if not line:
        break;
    #print(line);
    index="";title="";author="";booktitle="";pages="";year="";page="";year="";volume="";number="";
    while True:
        if(line.find("inproceedings=")!=-1 or line.find("article=")!=-1 ):
            start=line.find("{")+1;
            ending = line.find(",");
            index = "{"+line[start:ending]+"}";
            print("index " + index )
            ##fout.write("\\bibitem" +index+'\n');
        elif(line.find("journal=")!=-1 or line.find("booktitle=")!=-1):
            booktitle = "\\emph{" + line[line.find("{")+1:line.find("}")] + "}";
            print("booktitle: " + booktitle);
            #fout.write(booktitle+', ');  
            print("booktitle: " + booktitle); 
        elif(line.find("title=")!=-1):
            title = "\""+line[line.find("{")+1:line.find(",}")] + "\"";
            print("title: "+title);
            #fout.write(title+' ');
        elif(line.find("author=")!=-1):
            author = "{"+line[line.find("{")+1:line.find("}")]+"}";
            print("author: "+author);
            #fout.write(author+', ');   
        elif(line.find("volume=")!=-1):
            volume = "vol. "+line[line.find("{")+1:line.find("}")];
            print("volume: " + volume);
            #fout.write(volume+', ');    
        elif(line.find("number=")!=-1):
            number = "no. "+line[line.find("{")+1:line.find("}")];
            print("number: " + number); 
            #fout.write(number+', ');                
        elif(line.find("pages=")!=-1):
            page = "pp. "+line[line.find("{")+1:line.find("}")];
            print("page: " + page);
            #fout.write(page+', ');
        elif(line.find("year=")!=-1):
            year = line[line.find("{")+1:line.find("}")];
            print("year: " + year);
            #fout.write(year+'.');
        elif(line.find("}") and len(line)< 2 ):
            res = "\\bibitem" +index+'\n'+author+', '+title+booktitle+', ';
            if(volume):
                res+=volume;
                res+=', ';
            if(number):
                res+=number;
                res+=', ';
            if(page):
                res+=page;
                res+=', '
            res+=year;
            fout.write(res+"\r\n");
            break;
        line = fin.readline();
        
fin.close();
fout.close();
        
