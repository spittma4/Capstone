
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
		<h2>
			What is Kent State Social Suite?
		</h2>
		<p>
		Kent State Social Suite is designed to give individuals and organizations a convenient, easy to use, and powerful way to manage their social media pages.
		</p>
		<p>
		In a world where your online presence is a huge influence about your brand or organization, being able to effectively manage this is very important. The biggest problem with this is that there are a
		number of social media platforms that need attention! Wouldn't it be convenient if you could manage all of them from a single place? Enter Kent State Social Suite, designed to help Kent State students and organizations succeed. 
		</p>
		<p>
		Developed by a team of Kent State students with experience in business and development, we know what is important to manage and having used other platforms, know some things that we want to implement to create a better way to do it.
		</p>
		<h2>
			Our Team:
		</h2>
		
		<p>Jack Dauphers</p>
		<p>Hayden Knapp</p>
		<p>Stu McKaige</p> 
		<p>Jason Penza</p>
		<p>Sam Pittman</p>
		<img src="/static/img/sam-pittman.jpg">

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
