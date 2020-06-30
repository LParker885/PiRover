<?php

$file = fopen("/var/www/html/input.txt","w+");
$xc = fgets($file);
$yc = fgets($file);
$th = fgets($file);
$tu = fgets($file);
$go = fgets($file);

$xca = $_REQUEST["xc"];

$yca = $_REQUEST["yc"];

$tha = $_REQUEST["th"];

$tua = $_REQUEST["tu"];

$goa = $_REQUEST["go"];



if(is_numeric($xca) == true){
$xc = $xca;
}else if(is_numeric($xc) == false){
$xc = 90;
}
if(is_numeric($yca) == true){
$yc = $yca;
}else if(is_numeric($yc) == false){
$yc = 90;
}
if(is_numeric($tha) == true){
$th = $tha;
}else if(is_numeric($th) == false){
$th = 0;
}
if(is_numeric($tua) == true){
$tu = $tua;
}else if(is_numeric($tu) == false){
$tu = 0;
}
if(is_numeric($goa) == true){
$go = $goa;
}else if(is_numeric($go) == false){
$go = 0;
}











fwrite($file,$xc);
fwrite($file,"\n");
fwrite($file,$yc);
fwrite($file,"\n");
fwrite($file,$th);
fwrite($file,"\n");
fwrite($file,$tu);
fwrite($file,"\n");
fwrite($file,$go);
fclose($file);


echo $xc;
?>