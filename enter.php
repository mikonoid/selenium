<?php
session_start();

if($_SESSION['admin']){
	header("Location: admin.php");
	exit;
}

$admin = 'admin';
$pass = '48a7d652a8f2de5d31a2fe6433d1e9e0';

if($_POST['submit']){
	if($admin == $_POST['user'] AND $pass == md5($_POST['pass'])){
		$_SESSION['admin'] = $admin;
		header("Location: admin.php");
		exit;
	}else echo '<p>Access Denied!</p>';
}
?>
<p><a href="index.php">Main page</a> | <a href="admin.php">Admin</a></p>
<hr />
Authentication required. Softserve Selenium test.
<br />
<form method="post">
	Username: <input type="text" name="user" /><br />
	Password: <input type="password" name="pass" /><br />
	<input type="submit" name="submit" value="Enter" />
</form>