<?php

$file = fopen("/var/www/html/input.txt","w+");
$xc = fgets($file);
$yc = fgets($file);
$th = fgets($file);
$tu = fgets($file);
$go = fgets($file);
$tt = fgets($file);
$j1 = fgets($file);
$j2 = fgets($file);
$j3 = fgets($file);
$as = fgets($file);

$xca = $_REQUEST["xc"];
$yca = $_REQUEST["yc"];
$tha = $_REQUEST["th"];
$tua = $_REQUEST["tu"];
$goa = $_REQUEST["go"];
$tta = $_REQUEST["tb"];

$j1a = $_REQUEST["j1"];
$j2a = $_REQUEST["j2"];
$j3a = $_REQUEST["j3"];
$asa = $_REQUEST["as"];

if(is_numeric($xca) == true){   // If the data from the website is numeric, store that in the variable to be sent to control. If the previous data from the file is not numeric and the data from the website is not numeric, then make it the default number (90 or 0)
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
if(is_numeric($tta) == true){
$tt = $tta;
}else if(is_numeric($tt) == false){
$tt = 0;
}
if(is_numeric($j1a) == true){
$j1 = $j1a;
}else if(is_numeric($j1) == false){
$j1 = 0;
}
if(is_numeric($j2a) == true){
$j2 = $j2a;
}else if(is_numeric($j2) == false){
$j2 = 0;
}
if(is_numeric($j3a) == true){
$j3 = $j3a;
}else if(is_numeric($j3) == false){
$j3 = 0;
}
if(is_numeric($asa) == true){
$as = $asa;
}else if(is_numeric($as) == false){
$as = 0;
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
fwrite($file,"\n");
fwrite($file,$tt);
fwrite($file,"\n");
fwrite($file,$j1);
fwrite($file,"\n");
fwrite($file,$j2);
fwrite($file,"\n");
fwrite($file,$j3);
fwrite($file,"\n");
fwrite($file,$as);
fclose($file);


echo $xc;
?>
