import os
import csv
import webbrowser

new_window = 1;
new_tab = 2;


boxURL = "https://province-west.account.box.com/login";
landvisionURL = "https://login.digitalmapcentral.com/MemberPages/Login.aspx?ReturnUrl=%2fmemberpages%2fdefault.aspx%3fma%3dProvinceWest&ma=ProvinceWest";
gblack686 = "https://mail.google.com/mail/u/0/#inbox";
gblack_Province = "https://mail.google.com/mail/u/1/#inbox";
reuters = "http://www.reuters.tv/";
broker_manual = os.path.join("Work_Startup","broker_manual.xlsx");

webbrowser.open(boxURL,new=new_window)
webbrowser.open(landvisionURL,new=new_tab)
webbrowser.open(gblack686,new=new_tab)
webbrowser.open(gblack_Province,new=new_tab)
webbrowser.open(reuters,new=new_tab)

broker_manual = os.path.join("Broker_Manual.xlsx");
os.startfile(broker_manual)