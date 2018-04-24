<!--
	Home Template
	Uses: Bottle Template, CSS Grid, Custom KSUSocialSuite Core Application
-->

<!DOCTYPE html>
<html>
<head>
	<link type="text/css" href="/static/css/styles.css" rel="stylesheet">
  	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<script>
	function stepTwo() {
        redditForm = "<form id='redditForm' action='/redditurl' method='POST'>Id:<br><input type='text' name='id'><br>Secret:<br><input type='text' name='secret'><input type='submit'></form>"
        document.getElementById("goto").outerHTML = redditForm;
    }
</script>

<body>
<div class="wrapper">
	
	<div class="box header">
		<a href="/home"><h1>KSU</h1><h2>socialsuite</h2></a>
	</div>
	
	<div class="login">
			Welcome, {{username}}!<br><br>
			<a href="/signout">Signout</a><br>
	</div>
	
	<div class="box sidebar">
		<div class="sidenav">

			<button class="dropdown-btn">
				Instagram <img src="/static/img/instagram.png" height=40px align="center"> 
			 	<i class="fa fa-caret-down"></i>
			</button>
			<div class="dropdown-container">
			  	<a href="/instagram">Dashboard</a>
			</div>

			<button class="dropdown-btn">
				Reddit <img src="/static/img/reddit.png" height=40px align="center">
				<i class="fa fa-caret-down"></i>	
			</button>
			<div class="dropdown-container">
			  	<a href="/reddit">Dashboard</a>
			</div>

			<button class="dropdown-btn">
				Twitter <img src="/static/img/twitter.png" height=40px align="center">
				<i class="fa fa-caret-down"></i>
			</button>
			<div class="dropdown-container">
			  	<a href="/twitter">Dashboard</a>
			</div>
			<a href="/about">About</a>
			<a href="/contact">Contact</a>
			<a href="/settings">Settings</a>

		</div>
	</div>
	
	<div class="box content">
		
		% if pendingReddit:
		<p id="goto" >Go here: <a onclick="stepTwo()" target='_blank' href="https://www.reddit.com/prefs/apps/">Reddit authentication.</a></p> 
		% end

		% if not pendingReddit:
		<form action="/redditpost" method="POST">
		Subreddit:<br>
		<input class="redditSubreddit" type="text" name="subreddit" id="subreddit"><br>
		Title:<br>
		<input class="redditSubreddit" type="text" name="title" id="title"><br>
		Post Content:<br>
		<textarea class="redditPostContent" name="content" id="content" rows="5"></textarea><br>
		<input class="redditButton" type="submit" value="Post to reddit">
		</form>
		<br>
		<script src="https://www.reddit.com/user/{{redditName}}/submitted.embed?limit=10&sort=new" type="text/javascript"></script>
		<script src="https://www.reddit.com/user/{{redditName}}/comments.embed?limit=10&sort=new" type="text/javascript"></script>

	</div>
	
	<div class="box footer">
		All your social media, in one place.<br>
		Simple, Easy, Done.<br>
		Kent State University<br>
		CS Capstone Spring 2018<br>

	</div>

</div>

<script>
/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}
</script>

</body>
</html>
