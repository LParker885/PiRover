<?php

$filer = fopen("/mnt/ramdisk/input.txt","r");
$valuesa[0] = fgets($filer);
$valuesa[1] = fgets($filer);
$valuesa[2] = fgets($filer);
$valuesa[3] = fgets($filer);
$valuesa[4] = fgets($filer);
$valuesa[5] = fgets($filer);
$valuesa[6] = fgets($filer);
$valuesa[7] = fgets($filer);
$valuesa[8] = fgets($filer);
$valuesa[9] = fgets($filer);
$values = [90,90,0,0,0,0,0,0,0,0];
fclose($filer);


$val = $_REQUEST["val"];
$pos = $_REQUEST["pos"];

if(is_numeric($valuesa[0]) == true && intval($values[0]) <= 180 && intval($values[0]) >= 0){
$values[0] = $valuesa[0];
}
if(is_numeric($valuesa[1]) == true && intval($values[1]) <= 180 && intval($values[1]) >= 0){
$values[1] = $valuesa[1];
}
if(is_numeric($valuesa[2]) == true && intval($values[2]) <= 100 && intval($values[2]) >= 0){
$values[2] = $valuesa[2];
}
if(is_numeric($valuesa[3]) == true&& intval($values[3]) <= 2 && intval($values[3]) >= 0){
$values[3] = $valuesa[3];
}
if(is_numeric($valuesa[4]) == true&& intval($values[4]) <= 2 && intval($values[4]) >= 0){
$values[4] = $valuesa[4];
}
if(is_numeric($valuesa[5]) == true&& intval($values[5]) <= 180 && intval($values[5]) >= 0){
$values[5] = $valuesa[5];
}
if(is_numeric($valuesa[6]) == true&& intval($values[6]) <= 2 && intval($values[6]) >= 0){
$values[6] = $valuesa[6];
}
if(is_numeric($valuesa[7]) == true&& intval($values[7]) <= 2 && intval($values[7]) >= 0){
$values[7] = $valuesa[7];
}
if(is_numeric($valuesa[8]) == true&& intval($values[8]) <= 2 && intval($values[8]) >= 0){
$values[8] = $valuesa[8];
}
if(is_numeric($valuesa[9]) == true&& intval($values[9]) <= 100 && intval($values[9]) >= 0){
$values[9] = $valuesa[9];
}

if(is_numeric($val) == true && is_numeric($pos) == true){
	
		$values[$pos] = $val;
		
}


$file = fopen("/mnt/ramdisk/input.txt","w+");
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
