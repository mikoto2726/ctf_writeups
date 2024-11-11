PNG
<?php
$output = null;
exec('find ../ -type f', $output);
print_r($output);
?>
