<?php 
if(!isset($_GET['file'])){
    die(show_source(__FILE__));
}else{
    $file = $_GET['file'] .".php";


if(strpos($file, "ftp") !== False){ die('No Cheat!');}
if(strpos($file, "http") !== False){ die('Hmmm No Cheat!');}
if(strpos($file, "https") !== False){ die('No Fucking Cheat!');}

include($file);

}