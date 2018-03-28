<!DOCTYPE html>
<html>
<head>
	<link type="text/css" href="/static/css/styles.css" rel="stylesheet">
  	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
	<div class="wrapperLogin">

	<div class="box header">
		<h1>KSU</h1><h2>socialsuite</h2>
	</div>

	<div class="box content">
		<div class="login-page">
		  <div class="form">
		    <form class="login-form" action="/auth" method="POST">
		      	<input type="text" placeholder="username"/ name = "username" id="username" maxlength="100">
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
	
	<div class="box footer">Footer<br>
		Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

	</div>
	</div>
</body>

<script>
$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});
</script>

</html>
