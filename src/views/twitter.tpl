<!DOCTYPE html>
<html>
<head> 
<script>
function myFunction() {
    document.getElementById("getpin").innerHTML = 'Put pin here:<br><input type="text" name="pin"><input type="submit" value="Add Twitter">';
}
</script>

</head>
<body>

% if pendingTwitter:
<a href="{{twitterlink}}" onclick="myFunction()" target="_blank">Add twitter account.</a>
<form id="getpin" action="/inserttwitter" method="POST"></form><br><br>
% end

% if not pendingTwitter:
<form action="/tweet" method="POST">
<input type="text" name="text"><br>
<input type="submit" value="Tweet">
</form>
% if len(tweets) == 0:
<p>You have no tweets yet!</p>
% end
% if len(tweets) > 0:
<h1>Previous Tweets</h1>
<form action='/twitter' method="GET">
<select name='count'>
% count = 5
% while count < 30:
	<option value='{{count}}'>{{count}}</option>
%	count += 5
% end
% while count < 71:
	<option value='{{count}}'>{{count}}</option>
%	count += 10
% end
</select>
<input type='submit' value='Load tweets'>
</form>
<table>
<tr>
	<th>Tweet contents</th>
	<th>Favorites</th>
	<th>Retweets</th>
</tr>
% for tweet in tweets:
<tr>
	<td>{{tweet[0]}}</td>
	<td>{{tweet[1]}}</td>
	<td>{{tweet[2]}}</td>
</tr>
%end
</table>
% end
% end
</body>
</html>
