# -*- coding: utf-8 -*-
#!/usr/bin/env python
from subprocess import call

def query_DB_full_box(min_FOF_Id, max_FOF_Id, snapnum, file_ID=0,outputpath="./data/", user="anonimo", passwd="secreto"):
    """
    Queries the multidark database to extract all the haloes in the box within a ID range.

    The output is stored as an ascii (CSV) file.
    """
    #define the output file
    outputfile=outputpath+"halos_bolshoi_"+str(file_ID)+".csv"

    #define the range in positions to query
    min_Id = int((snapnum*10)*1E8 + (min_FOF_Id))
    max_Id = int((snapnum*10)*1E8 + (max_FOF_Id))
    
    # Build the SQL query
    id_query = " fofId between "+str(min_Id)+" and " +str(max_Id)
    query   = "select * from Bolshoi..FOF where snapnum="+str(snapnum)
    query  = query + " and "+id_query #+" order by logMvir desc"

    # Build the wget command to query the database
    website = "http://wget.multidark.org/MyDB?action=doQuery&SQL="
    username = user
    password = passwd
    
    wget_options=" --content-disposition --cookies=on --keep-session-cookies --save-cookies=cookie.txt --load-cookies=cookie.txt" 
    wget_options=wget_options+" -O "+outputfile +" "
    wget_command="wget --http-user="+username+" --http-passwd="+password+" "+wget_options    
    command=wget_command + "\""+ website + query+"\""
    print ""
    print query
    print ""
    print command
    print ""
    # execute wget in shell
    retcode = call(command,shell=True)


def query_DB_environment(min_Id, max_Id, snapnum, web_resolution=256, web="TWeb", file_ID=0,outputpath="./data/", user="anonimo", passwd="secreto"):
    """
    Queries the multidark database to extract all the haloes in the box within a ID range.

    The output is stored as an ascii (CSV) file.
    """
    #define the output file
    outputfile=outputpath+web+str(web_resolution)+"_env_bolshoi_"+str(file_ID)+".csv"
    # Build the SQL query
    id_query = " webId between "+str(min_Id)+" and " +str(max_Id)
    query   = "select * from Bolshoi.."+web+str(web_resolution)+" where " + id_query

    # Build the wget command to query the database
    website = "http://wget.multidark.org/MyDB?action=doQuery&SQL="
    username = user
    password = passwd
    
    wget_options=" --content-disposition --cookies=on --keep-session-cookies --save-cookies=cookie.txt --load-cookies=cookie.txt" 
    wget_options=wget_options+" -O "+outputfile +" "
    wget_command="wget --http-user="+username+" --http-passwd="+password+" "+wget_options    
    command=wget_command + "\""+ website + query+"\""
    print ""
    print query
    print ""
    print command
    print ""
    # execute wget in shell
    retcode = call(command,shell=True)



query_DB_full_box(0, 10000, 416, file_ID=0, outputpath="/Users/forero/Dropbox/PaperDM_Signal_MW/data/", user="XXX", passwd="XXX")


query_DB_environment(0, 255, 416, web_resolution=256, web="VWeb", file_ID=0, outputpath="/Users/forero/Dropbox/PaperDM_Signal_MW/data/", user="XXX", passwd="XXX")


