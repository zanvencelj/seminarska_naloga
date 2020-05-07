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
        <h1>Login</h1> <br>
        <form action="user.php" method="post">
            <label for="user"><b>Username</b></label> <br>
            <input type="text" placeholder="Enter Username" name="user" required> <br>

            <label for="pass"><b>Password</b></label><br>
            <input type="password" placeholder="Enter Password" name="pass" required> <br>

            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>