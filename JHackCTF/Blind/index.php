<?php
$sandbox = dirname(__FILE__) . '/'  .md5($_SERVER['REMOTE_ADDR']);
@mkdir($sandbox);
copy(dirname(__FILE__) . '/' . ".htflag",  $sandbox . "/.htflagsandboxzazsdmno");
@chmod($sandbox);
@chdir($sandbox);
if (isset($_GET['reset'])) die(exec('/bin/rm -rf ' . $sandbox));
$command = substr(urldecode(trim(file_get_contents('php://input'))), 1, 10);
if (strpos($command, '*') !== false) die("* di blacklist om");
@exec($command);
highlight_file(__FILE__);

