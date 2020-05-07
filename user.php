<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <title>Vencelj &bull; Login</title>
    <link rel="icon" href="slike/icon.png">

    <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Ubuntu&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="./CSS/login.css">
</head>
<body>
    <div class="loginform">
        <?php
            $username = $_POST['user'];
            $password = $_POST['pass'];

            $db = new mysqli('localhost', 'root', '', 'zvweb');

            $rezultat = $db->query("SELECT * FROM uporabniki WHERE upime='$username' AND geslo='$password'");

            if($rezultat->num_rows == 1)
                echo "<h1>Prijava uspešna</h1>";
            else
                echo "<h1>Napačno geslo ali uporabniško ime!</h1>";
        ?>
        <a href="index.html">BACK TO HOME</a>
    </div>
    
</body>
</html>