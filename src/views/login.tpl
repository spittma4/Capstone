<body>
<p>Login Information:</p>
<form action="/auth" method="POST">
        Username:<input type="text" size="50" maxlength="100" name = "username" id="username"><br>
        Password:<input type="password" size="50" maxlength="100" name = "password" id="password"><br>

<br><input type="submit" onclick="confirmationAlert()" name="save" value="save">
</form>

%if (status == 'fail'):
	Incorrect
%end	

</body>

