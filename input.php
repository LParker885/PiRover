<?php

$filer = fopen("/mnt/ramdisk/input.txt","r");
$values[0] = fgets($filer);
$values[1] = fgets($filer);
$values[2] = fgets($filer);
$values[3] = fgets($filer);
$values[4] = fgets($filer);
$values[5] = fgets($filer);
$values[6] = fgets($filer);
$values[7] = fgets($filer);
$values[8] = fgets($filer);
$values[9] = fgets($filer);
fclose($filer);
$file = fopen("/mnt/ramdisk/input.txt","w+");

$val = $_REQUEST["val"];
$pos = $_REQUEST["pos"];



if(is_numeric($val) == true){
	if(is_numeric($pos) == true){
		$values[$pos] = $val;
	}
}



fwrite($file,intval($values[0]));
fwrite($file,"\n");
fwrite($file,intval($values[1]));
fwrite($file,"\n");
fwrite($file,intval($values[2]));
fwrite($file,"\n");
fwrite($file,intval($values[3]));
fwrite($file,"\n");
fwrite($file,intval($values[4]));
fwrite($file,"\n");
fwrite($file,intval($values[5]));
fwrite($file,"\n");
fwrite($file,intval($values[6]));
fwrite($file,"\n");
fwrite($file,intval($values[7]));
fwrite($file,"\n");
fwrite($file,intval($values[8]));
fwrite($file,"\n");
fwrite($file,intval($values[9]));
fclose($file);


?>
