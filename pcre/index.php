<?php
        $flag = "Flag{Art_Of_Exploit}";
        $restrictred = array('system','exec','eval','fpassthru','passthru','shell_exec','popen','escapeshellcmd');
?>
<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
        <title>My First Program</title>
</head>
<body>
        <center>
        <img src="https://kprofiles.com/wp-content/uploads/2017/05/Daehyun.jpg" height="240px">
        <form action="" method="post">
                <input type="text" name="search" placeholder="Search For Replace"><br>
                <select name="mod">
                        <option value="i">Caseless</option>
                        <option value="m">Multiline</option>
                        <option value="s">Dot All</option>
                        <option value="x">Extended</option>
                </select><br>
                <input type="text" name="replacement" placeholder="Replace With"><br>
                <input type="text" name="subject" placeholder="Subject"><br>
                <button type="submit" name="submit">replace</button>
        </form>

        <?php
                if(isset($_POST['submit'])) {
                        $replacement = preg_replace("/system|exec|eval|fpassthru|passthru|shell_exec|popen|escapeshellcmd/", "", $_POST['replacement']);
                        $new = preg_replace('/'.$_POST['search'].'/'.$_POST['mod'], $replacement, $_POST['subject']);
                        echo htmlentities($new);
                }
        ?>

        </center>
</body>
</html>