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
function myFunction() {
    document.getElementById("getpin").innerHTML = 'Put pin here:<br><input type="text" name="pin"><input type="submit" value="Add Twitter">';
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

			<button class="dropdown-btn">Admin Settings 
			 	<i class="fa fa-caret-down"></i>
			</button>
			<div class="dropdown-container">
			  	<a href="/settings/users">Users</a>
			</div>

			<button class="dropdown-btn">
				Instagram <img src="/static/img/instagram.png" height=40px align="center"> 
			 	<i class="fa fa-caret-down"></i>
			</button>
			<div class="dropdown-container">
			  	<a href="/instagram">Dashboard</a>
			    <a href="/instagramanalytics">Analytics</a>
			</div>

			<button class="dropdown-btn">
				Reddit <img src="/static/img/reddit.png" height=40px align="center">
				<i class="fa fa-caret-down"></i>	
			</button>
			<div class="dropdown-container">
			  	<a href="/reddit">Dashboard</a>
			    <a href="/redditanalytics">Analytics</a>
			</div>

			<button class="dropdown-btn">
				Twitter <img src="/static/img/twitter.png" height=40px align="center">
				<i class="fa fa-caret-down"></i>
			</button>
			<div class="dropdown-container">
			  	<a href="/twitter">Dashboard</a>
			    <a href="/twitteranalytics">Analytics</a>
			</div>
			<a href="/about">About</a>
			<a href="/contact">Contact</a>
			<a href="/settings">Settings</a>

		</div>
	</div>
	
	<div class="box content">
		% if pendingTwitter:
		<a href="{{twitterlink}}" onclick="myFunction()" target="_blank">Add twitter account.</a>
		<form id="getpin" action="/inserttwitter" method="POST"></form><br><br>
		% end

		% if not pendingTwitter:
		<form action="/tweet" method="POST">
		What's Happening?<br>
		<input class="tweetContent" type="text" name="text"><br>
		<input class="tweetButton" type="submit" value="Tweet">
		</form>

		<br>
		<a 
			class="twitter-timeline" 
			data-width= 40% 
			data-chrome= "nofooter"
			href="https://twitter.com/Sampitdawg?ref_src=twsrc%5Etfw">
			Tweets by @Sampitdawg
		</a> 
		<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

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
    this.classList.toggle("active");=]
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
