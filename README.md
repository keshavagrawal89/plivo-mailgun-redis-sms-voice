## This app can be deployed on Heroku with RedisToGo addon


## How, What and Where?


#### What should be expected?

*   When an incoming SMS is received by Plivo DID Plivo makes an HTTP REQUEST to the message url of the application attached to the DIDa long with certain paramteres like From To Text Type. That application here is **http://xyzapp-sms-voice.herokuapp.com/acceptsms/**  This example app replies back to sender an automatic response which can be set in SMS Controller
*   All received messages which are not replied can be seen under: http://xyzapp-sms-voice.herokuapp.com/sms-dashboard/
*   Text box besides each message can be used to type in the reply and hit "Reply"
*   Messages already replied will have staus as "Replied!"
*   Messages awaiting reply will show up as "Waiting Reply!"
*   Messages can be deleted permanently from UI by clicking on "Delete"
*   Columns of the table can be sorted to suit the requirement.
*   Also it internally sends an email to the email id configured in the Email Controller step.
*   When an Incoming calls come to the Plivo DID then a recorded media file is played which can be configured in Voice Call Controller.        

#### Email Controller


![alt tag](https://dl.dropboxusercontent.com/u/54579287/smsvoice/Email%20Controller.png)

1.  For Email Service this app uses [Mailgun](http://www.mailgun.com/) [API](http://documentation.mailgun.com/)
2.  Visit [Mailgun](http://www.mailgun.com/)
3.  Create an account there.
4.  Pick a [Plan](http://www.mailgun.com/pricing)
5.  Free plan comes with 200 messages per day!
6.  Get the API key from [here](https://mailgun.com/cp). Look for "API Key"
7.  Keep that in a safe place.
8.  On the same page look for "Domain Name" under the section "Email Domains"
9.  **From Email** is the email from where the email will be sent.
10.  **Mailgun API Token** is the place where you are going to put in the API Key in received in step 6
11.  **Email To** is where you want to receive the email.
12.  **Mail Subject** is the subject of the email which will be sent to the "Email To" address.
13.  **Mailgun Email Domain** is the domain which you noted in step 8
14.  After all these click on "Save Changes"

#### SMS Controller

![alt tag](https://dl.dropboxusercontent.com/u/54579287/smsvoice/SMSautoresponder.png)

1.  **Input SMS Reply** allows you to set the auto response for the incoming SMS on plivo DID
2.  Enter the text
3.  Click on "Save Changes"

#### Reply directly from browser

![alt tag](https://dl.dropboxusercontent.com/u/54579287/smsvoice/SMSdashboard.png)


#### Voice Call Controller


![alt tag](https://dl.dropboxusercontent.com/u/54579287/smsvoice/Voice%20call%20controller.png)


1.  Enter the url of the audio file in the text box
2.  Click on "Save Changes"

#### After all these settings you can go ahead and configure your Plivo App attached to the Plivo DID

1.  **answer_url** field of the application should be: **http://xyzapp-sms-voice.herokuapp.com/acceptcalls/** with method as **POST**
2.  **message_url** field of the application should be: **http://xyzapp-sms-voice.herokuapp.com/acceptsms/** with method as **POST**
3.  Save the Plivo application and you are all set!

#### Things needs to be changed in handle.py file

1. <auth_id> - Replace with your own plivo auth_id
2. <auth_token> - Replace with your own plivo auth_token


#### Help

![alt tag](https://dl.dropboxusercontent.com/u/54579287/smsvoice/help.png)


**Success** Enjoy!.
