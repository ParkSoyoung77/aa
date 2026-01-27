<?php
	$con=mysqli_connect("localhost", "root", "1111") or die("MariaDB 접속 실패");
	phpinfo();
	mysqli_close($con);
?>