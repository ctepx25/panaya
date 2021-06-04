#!/usr/bin/env python3
import mysql.connector

try:
  mydb = mysql.connector.connect(host="mysql", user="nginx", password="nginx", database="panaya")
  mycursor = mydb.cursor()

  mycursor.execute("select A.id as Company_ID,A.name as Company_Name,B.id as Account_ID,B.name as Account_Name,C.id as Project_ID,C.name as Project_Name,CASE C.status WHEN 0 THEN 'Inactive' WHEN 1 THEN 'Active' WHEN 2 THEN 'Frozen' ELSE NULL END as 'Status' from As_company as A join As_account as B on A.id=B.company_id join As_project as C on B.id=C.account_id")

  myresult = mycursor.fetchall()

  with open("/usr/share/nginx/html/index.html", "w") as file1:
      file1.write("<!DOCTYPE html>\n<html>\n<head>\n<style>table, th, td {border: 1px solid black;}\n</style>\n</head>\n<body>\n")
      file1.write("<table>\n<tr>\n<th>Company_ID</th>\n<th>Company_Name</th>\n<th>Account_ID</th>\n<th>Account_Name</th>\n<th>Project_ID</th>\n<th>Project_Name</th>\n<th>Project_Status</th>\n</tr>")
      for x in myresult:
         file1.write("<tr>\n<td> %s </td>\n<td> %s </td>\n<td> %s </td>\n<td> %s </td>\n<td> %s </td>\n<td> %s </td>\n<td> %s </td>\n</tr>\n " % (x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
      file1.write("</table>\n</body>\n</html>")
except:
  print('Something wrong')
