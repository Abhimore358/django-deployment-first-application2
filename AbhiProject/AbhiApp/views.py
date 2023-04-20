from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request):
    #ss----> is html-data/code
    print("welcome/ url is requested & display () is executed");
    ss = '''
            <center>
                <h2 style="color:blue;">
                    Hello User Welcome To Django Abhi-Project Abhi-App
                </h2>
                <hr/>
            </center>
            ''';
    return HttpResponse(ss);       
    
def show(request):
    ss='''
        <!--
	HTML Web Page To Display "Welcome-Message" With Different Headings
	
-->
<html>
		<head>
			<title>***Welcome-Page***</title>
			<style>
				h1	{
						color:blue;
					}
				h2	{
						color:greem;
					}	
				h3	{
						color:red;
					}	
				h4	{
						color:orange;
					}	
				h5	{
						color:pink;
					}	
				h6	{
						color:violet;
					}				
				h1,h3,h5{
							background-color:yellow;
						}
				h2,h4,h6{
							background-color:lightgreen;
						}
			</style>
		</head>
		<body>
			<center>
				<h1>Welcome To DJANGO HTML Webpage</h1>
				<hr color="brown" width="95%"/>
				<h2>Welcome To DJANGO HTML Webpage</h2>
				<hr color="brown" width="85%"/>
				<h3>Welcome To DJANGO HTML Webpage</h3>
				<hr color="brown" width="75%"/>
				<h4>Welcome To DJANGO HTML Webpage</h4>
				<hr color="brown" width="65%"/>
				<h5>Welcome To DJANGO HTML Webpage</h5>
				<hr color="brown" width="55%"/>
				<h6>Welcome To DJANGO HTML Webpage</h6>
				<hr color="brown" width="45%"/>
			</center>
		</body>
</html>
    '''
    return HttpResponse(ss);
    
    
def hello(request):
    print("hello/ url is requested & hello() is executed ")
    
    ss='''
            <html>
                <head>
                    <title>HELLO WEBPAGE</title>
                    <style>
                            h1{
                                color:blue;
                                width:90%;
                              }
                              h2{
                                color:green;
                                width:90%;
                              }
                              h3{
                                color:red;
                                width:90%;
                              }
                              h1,h2,h3{
                                background-color:lightblue;
                                border:2px Solid Brown
                              }
                            
                    </style>
                </head>
                <body>
                    <center>
                            <h1>HELLO USER...!!!</h1>
                            <hr color='brown' width='80%'/>
                            <h2>WELCOME TO D-JANGO APP..!</h2>
                            <hr color='brown' width='60%'/>
                            <h1>HAVE A NICE DAY...</h1>
                            <hr color='brown' width='40%'/>
                    </center>
                </body>
            </html>
    ''';
    return HttpResponse(ss);

import time;
def senddatetime(request):
    print("datetime/ url is rerquested * senddatetime() is executed");
    ct=time.ctime()
    print("client request date & time on server::",ct);
    ss='''
        <html>
            <head>
                <title>DATE TIME WEB-PAGE</title>
                <style>
                    h1{
                        color:blue;
                        width:90%;
                    }
                    h2{
                        color:green;
                        width:80%;
                    }
                    h3{
                        color:red;
                        width:70%;
                    }
                    h1,h2,h3{
                        background-color:lightgreen;
                        border:2px Solid Brown
                    }
                </style>
            </head>
            <body>
                <center>
                    <h1>WELCOME TO D-JANGO USER....!!</h1>
                    <hr color='brown' width='80%'/>
                    <h2>SERVER DATE AND TIME::</h2>
                    <hr color='brown' width='700%'/>
                    <h3>''',ct,'''</h3>
                    <hr color='brown' width='60%'/>
                </center>
            </body>
        </html>
    ''';
    return HttpResponse(ss); 
    
def demo(request):
    print("Multiple-Request-URLs Same Response");
    htmldata = ''' <cnter>
                <h1>WELCOME DEMO USER..!!</h1>
                <hr/>
                <h2>This is Same-Output for Different-Multiple-Request-URLs</h2>
                <hr/>
                <h3>Have a Greate Day..!!</h3>
                <hr/>
                </center>''';
    return HttpResponse(htmldata);
    
def homepage(request):
    htmldata = ''' <center>
                    <h1>WELCOME TO DEFAULT HOME-PAGE...</h1>
                    <hr/>
                    <h2>Your Request Page Not-Found...</h2>
                    <hr/>
                    <h3>plaese Try Other URLs or Links!!!</h3>
                    <hr/>
                   </center>''';
    return HttpResponse(htmldata);               