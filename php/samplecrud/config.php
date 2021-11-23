<?php
	define('DB_SERVER','localhost');
	define('DB_USERNAME','root');
	define('DB_PASSWARD','');
	define('DB_NAME','test');
	$conn=mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWARD,DB_NAME);
	if($conn === false){
		die("ERROR:Could not connect." . mysqli_connect_error());
	}
?>