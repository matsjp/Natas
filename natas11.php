$plaintextarray = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
$plaintextjson = json_encode($plaintextarray);

$base64ciphertext = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";
$ciphertext = base64_decode($base64ciphertext);
for($i=0;$i<strlen($ciphertext);$i++) {
    echo($ciphertext[$i] ^ $plaintextjson[$i]);
}

function xor_encrypt($in) {
    $key = "qw8J";
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$myarray = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
echo base64_encode(xor_encrypt(json_encode($myarray)));
