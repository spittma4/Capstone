<body style="background-color:lightblue;">
<p>Signup Information:</p>
<form action="/adduser" method="POST">
	Email:<input type="text" size="20" maxlength="100" name = "username" id="username"><br>
	Fullname <input type="text" size="30" maxlength="100" name = "fullname" id="fullname"><br>
	Password:<input type="password" size="20" maxlength="100" name = "password" id="password"><br>

<br><input type="submit" onclick="confirmationAlert()" name="save" value="Signup">
</form>
% if status != 'new':
{{status}}
% end

</body>

