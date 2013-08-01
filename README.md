plivo-mailgun-sms-voice
=======================

Send Auto Response to SMS sender. Get Email on receiving the message. Make caller hear a recording when Plivo Number is called.

<html>
  <head>
		<title>Help</title>
		<link rel="stylesheet" href="/static/bootstrap/css/bootstrap.css">
	</head>

	<body>
		<h2>Help Yourselves</h2>
	</body>

	<div class="span12">
      <div class="alert alert-success">
        <a class="close">&times;</a>
        <h4>Email Controller</h4>
        <ol>
        	<li>For Email Service this app uses <a href="http://www.mailgun.com/">Mailgun</a> <a href="http://documentation.mailgun.com/">API</a></li>
        	<li>Visit <a href="http://www.mailgun.com/">Mailgun</a></li>
        	<li>Create an account there.</li>
        	<li>Pick a <a href="http://www.mailgun.com/pricing">Plan</a></li>
        	<li>Free plan comes with 200 messages per day!</li>
        	<li>Get the API key from <a href="https://mailgun.com/cp">here</a>. Look for "API Key"</li>
        	<li>Keep that in a safe place.</li>
        	<li>On the same page look for "Domain Name" under the section "Email Domains"</li>
        	<li><strong>From Email</strong> is the email from where the email will be sent.</li>
        	<li><strong>Mailgun API Token</strong> is the place where you are going to put in the API Key in received in step 6</li>
        	<li><strong>Email To</strong> is where you want to receive the email.</li>
        	<li><strong>Mail Subject</strong> is the subject of the email which will be sent to the "Email To" address.</li>
        	<li><strong>Mailgun Email Domain</strong> is the domain which you noted in step 8</li>
        	<li>After all these click on "Save Changes"</li>
     	</ol>
     	<h4>SMS Controller</h4>
     	<ol>
     		<li><strong>Input SMS Reply</strong> allows you to set the auto response for the incoming SMS on plivo DID</li>
     		<li>Enter the text</li>
     		<li>Click on "Save Changes"</li>
     	</ol>

     	<h4>Voice Call Controller</h4>
     	<ol>
     		<li>Enter the url of the audio file in the text box</li>
     		<li>Click on "Save Changes"</li>
     	</ol>
     	<br/>
     	<br/>
     	<h4><u>After all these settings you can go ahead and configure your Plivo App attached to the Plivo DID</u></h4>
     	<ol>
     		<li><strong>answer_url</strong> field of the application should be: <strong>http://ryan-sms-voice.herokuapp.com/acceptcalls/</strong> with method as <strong>POST</strong></li>
     		<li><strong>message_url</strong> field of the application should be: <strong>http://ryan-sms-voice.herokuapp.com/acceptsms/</strong> with method as <strong>POST</strong></li>
     		<li>Save the Plivo application and you are all set!</li>
     	</ol>

     	<h4>What should be expected?</h4>
     	<ul>
     		<li>When an incoming SMS is received by Plivo DID Plivo makes an HTTP REQUEST to the message url of the application attached to the DID. That application here is <strong>http://ryan-sms-voice.herokuapp.com/acceptsms/</strong> along with certain paramteres like From To Text Type. This example app replies back to sender an automatic response which was set in the previous SMS Controller step.</li>
     		<li>Also it internally sends an email to the email id configured in the Email Controller step.</li>
     		<li>When an Incoming calls come to the Plivo DID then a recorded media file is played which was configured in Voice Call Controller Step.</li>
     	</ul>

        	<strong>Success</strong> Enjoy!.
      	</ol>
      </div>
    </div>
</html>
