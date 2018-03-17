<head>

</head>
<body style="background-color:lightblue;">
<p>Login Information:</p>
<form action="/auth" method="POST">
        Email:<input type="text" size="20" maxlength="100" name = "username" id="username"><br>
        Password:<input type="password" size="20" maxlength="100" name = "password" id="password"><br>

<br><input type="submit" onclick="confirmationAlert()" name="save" value="Login">
</form>

%if (status == 'fail'):
	Email or password were incorrect.
%end
<p>Need an account?<br><a href="/signup">Create one here!</a><p>

</body>

