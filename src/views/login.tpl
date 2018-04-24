<!DOCTYPE html>
<html>
<head>
	<link type="text/css" href="/static/css/styles.css" rel="stylesheet">
  	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
	<div class="wrapperLogin">

	<div class="box header">
		<a href="/home"><h1>KSU</h1><h2>socialsuite</h2></a>
	</div>

	<div class="box content">
		<div class="login-page">
		  <div class="form">
		    <form class="login-form" action="/auth" method="POST">
		      	<input type="text" placeholder="email"/ name = "username" id="username" maxlength="100">
		      	<input type="password" placeholder="password"/ name="password" id="password" maxlength="100">
		      	<button type="submit" onclick="confirmationAlert()" name="save">login</button>
		      	<p class="message">Not registered? <a href="/signup">Create an account!</a></p>

		      	%if (status == 'fail'):
				Email or password were incorrect.
				%end
		    </form>
		 </div>
	</div>
		
	</div>
	
	<div class="box footer">
		All your social media, in one place.<br>
		Simple, Easy, Done.<br>
		Kent State University<br>
		CS Capstone Spring 2018<br>

	</div>

</div>
</body>

<script>
$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});
</script>

</html>
