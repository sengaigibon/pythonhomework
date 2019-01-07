<?php
/* by default there's no pass-by-reference */
function addNext($lst) {
    $lst[] = $lst[count($lst) - 1] + 1; 
}

$arr = [1,2];

print_r($arr);

addNext($arr);

print_r($arr);