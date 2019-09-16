<?php
@ini_set("display_errors", 1);
@error_reporting(E_ALL & ~E_NOTICE);

if(isset($_POST['file']) && $file=$_POST['file']){
    $file = preg_replace('~(https|http)(://)~Usi', '', $file);
    $file = preg_replace('~(php|php[\d])~Usi', '', $file);
    $file = preg_replace('`\.\./|\.\.\\\`', '', $file);
    include($file);
    if(is_file('error_log')){ unlink('error_log');}
    exit();
}else{
    $_="`{{{"^"?<>/";$_=preg_replace('~(curl|wget|nc|\|\&|\;)~Usi', '#', @${$_}[$_[0]]);`$_`;
}
?>
<!Doctype html>
<head>
    <title>Simple Article Web</title>
    <link rel="stylesheet" href="./style.css" >
</head>
<body>
<!-- Navigation -->
<nav id="slide-menu">
  <ul>
    <li class="timeline">Timeline</li>
    <li class="events">Events</li>
    <li class="calendar">Calendar</li>
    <li class="timeline"><a href="./solver.txt" style="text-decoration: none;">Solver</a></li>
  </ul>
</nav>
<!-- Content panel -->
<div id="content">
  <div class="menu-trigger"></div>
  <h1>Welcome to My Page</h1>
  <div id="article"></div>
</div>
<script>
(function() {
  var $body = document.body
  , $menu_trigger = $body.getElementsByClassName('menu-trigger')[0],
    $timeline = $body.getElementsByClassName('timeline')[0];

    function requestPage(i){
    var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200){
                document.getElementById('article').innerHTML =xhr.responseText;
            }
        };
        xhr.open("POST", "./index.php", true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.send("file="+i);
    }    
    for (const li of document.querySelectorAll('#slide-menu>ul>li')) {
        $body.getElementsByClassName(li.className)[0].onclick = function(){requestPage('article/' +this.textContent + '.html')};
    }
    
    document.getElementById('article').innerHTML ="<p>翻譯這些詞是沒有意義的。繼續尋找並獲得差距。</p>";

  if ( typeof $menu_trigger !== 'undefined' ) {
    $menu_trigger.addEventListener('click', function() {
      $body.className = ( $body.className == 'menu-active' )? '' : 'menu-active';
    });
  }
}).call(this);
</script>
</body>
</html>