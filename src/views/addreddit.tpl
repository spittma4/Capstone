<!doctype html>
<html>
<head>
<script>
	function stepTwo() {
		redditForm = "<form id='redditForm'>Id:<br><input type='text' name='id'><br>Secret:<br><input type='text' name='secret'></form>"
		document.getElementById("goto").outerHTML = redditForm;
	}
</script>
</head>
<body>
<p id="goto" >Go here: <a onclick="stepTwo()" target='_blank' href="https://www.reddit.com/prefs/apps/">Reddit authentication.</a></p>
</body>
</html>
