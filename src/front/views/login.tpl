<body>
<p>Login Information:</p>
<form action="/auth" method="POST">
        Username:<input type="text" size="50" maxlength="100" name = "username" id="usernameID"><br>
        Password:<input type="text" size="50" maxlength="100" name = "password" id="passwordID"><br>

<br><input type="submit" onclick="confirmationAlert()" name="save" value="save">
</form>

%if (status == 'fail'):
	Incorrect
%end	

</body>

