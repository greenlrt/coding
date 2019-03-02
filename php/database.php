<?php
$host = "localhost";
$db_name = "api_db";
$username = "monitor";
$password = "password";

// Create connection
try {
	$conn = new PDO("mysql:host=$host;dbname=$db_name", $username, $password);
	// set the PDO error mode to expception
	$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	echo "Connected successfully";
} catch (PDOException $exception) {
	echo "Connection failed: " . $exception->getMessage();
}
?>
