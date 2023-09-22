<head>
    <link rel="stylesheet" type="text/css" href="style.css">    
</head>
<html>

<title>Not Navy Federal</title>
<?php
// Start a session
session_start();

// Check if John's balance is greater than 2000
if ($_SESSION['users']['Snuffy'] > 2000) {

    echo "<img src='Soldier-Holding-Money.jpg'>";
echo "</br></br>";
    echo "Here is the secret for you cygame{I _ m4k3 _ B4d _ F1n4nc14l _ D3c1510n5}.";
    
} else {
    echo "You are not allowed. Only the members who have balance more than 2000 are allowed to get the secret";
}
?>

