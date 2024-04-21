<?php // zaciatok skriptu
// You should have basic understanding of HTML
// koment
echo "<strong>Bold Text</strong>";

/*
Multiline comment
*/

// end of script ?> 

--------------- Variables -----------------------
$meno = hodnota;
PHP je case sensitive, takze $meno != $meno
int, string, double netreba definovat. PHP pride na spravny typ pri prvom prideleni hodnoty

konstanty definujeme
define(meno, hodnota, case-insensitive default false)

<?php
    define("MSG", "Hello!", true); // konstanta nepotrebuje $ na zaciatku
    echo msg // output "Hello!"
?>

<?php
// Udajove typy
$string = "Hello"  // funguje aj s "" a ''
$string2 = 'Hello'
echo $string.$string2 // pre vypisanie retazcov
$int = -42; // moze byt zaporny
$x=42.13; // float
$y = false  // boolean
// PHP rozozna aj Array, Object, NULL, Resource
// Vacsina udajovych typov, moze byt pouzita spolu
$str = "10";
$int = 20;
$sum= $str + $int;  // $sum = 30
?>

Premenne definovane mimo funkcie su global a vo vnutri su local
<?php
$name='David';
function getName(){
    global $name; // bez toho by zahlasilo chybu pretoze $name je global a funkcia k nej nema pristup
    echo $name;
}
getName();

//Premenna moze byt odkazom na inu premennu
$a='hello';
$hello = 'Hi';
echo $$a  // otput bude: Hi lebo $$a = $hello
?>

<?php // ----------------- OPERATORS -------------------
//aritmeticke operatori  + - * / %
$x++; // post-increment
--$x; // pre-decrement

$a=2; $b=$a++; //$a=3 $b=2
$a=2; $b=++$a; //$a=3 $b=3

x += y;  // x=x+y
x-=y; x*=y; x /= y; x%=y

// Porovnavacie operatori
== equal, true ak $x=$y
=== identical, true ak $x a $y maju rovnaky typ aj hodnotu
!= nerovna sa 
<> nerovna sa
!== nie je identicke
> < >= <=
// Logicke operatori
and, &&
or ||
xor - True ak $x alebo $y su true, ale nie obidve
! not

// ---------------------- ARRAYS ---------------------------
// mozeme definovat
$names = array("David", 'Amy', 'John');
//alebo
$names[0] = 'David';
$names[1] = 'Amy';
// dokonca s roznymi typmi
$names[2] = "<strong>PHP</strong>";
$names[3] = 21;

echo "$names[0] is $names[3] and knows $names[2]"; // David is 21 and knows PHP
// comu nerozumie berie ako text

//Associative Array  //ako dic v pythone
$people = array("David"=>"27", "Amy"=>"21");
// alebo
$poeple['David'] = '27';
echo $poeple['David'];

//Viacrozmerne pole
//2D pole obsahujuce 3 polia
$people array(
    'online' => array("David", 'Amy'),
    'offline' => array("John", 'Paul'),
    'away' => array("Bob", 'Ringo')
);
echo $people['online'][1];  // output: Amy
?>


<?php
// ----------------- Control Structures ------------------------------
if (condition){}else{}elseif(condition){}

while(condition is true){}

do{}while(condition is true) // do-while prebehne aspon raz

for(int, test, increment){}
for($a=0; $a<6; $a++){}  // O.o ??  Parametre oddlene ; normalne su to ,

continue;  // poznas z pythonu

foreach(array as $value){}  // pouziva sa pri poliach
foreach(array as $key=>$value){}
$names = array('John', 'Paul', 'Bob');
foreach($names as $name){
    echo $name.'<br />';
}

Switch($premenna){
    case 1:
        //kod
    break;  // break ukoncuje case, ak ho nedame prebehne vsetky case-y
    case 2:
        //adasdasdas
    break;
    default:
        // ak neodchytil ziaden case
}
?>

// Include % Require
// Subor header.php:
<?php
echo '<h1>Welcome</h1>';
?>

<html>
    <body>
        <?php include 'header.php'; ?>
        <p>Something.</p>
    </body>
</html>
<!-- Include nacita kod z header.php a spusti ho
Require je skoro to iste, ale padne ak nenajde header.php
-->

<?php
// ------------- Functions ------------------
function Meno($prem1, $prem2=10){
    $vysl = $prem1 + $prem2;
    echo $vysl;
    return $vysl;
}
Meno(1, 2);
?>


<?php
// ------------------ Predefined Variables ---------------------
// superglobal je predefinovana premenna pristupna zovsadial
$_SERVER, $GLOBALS, $_REQUEST, $_POST, $_GET, $_FILES, $_ENV, $_COOKIE, $_SESSION

$_SERVER // je array ktory obsahuje info o headers, paths a script locations. Cele je to na webserv
echo $_SERVER['SCRIPT_NAME']; // vrati cestu k sucastnemu scriptu
echo $_SERVER['HTTP_HOST']; // vrati host header z terajsej poziadavky /request

// Tato metoda je vhodna napr. ked mame vela obrazkov na servri a potrebujeme premiestnit stranku na iny host.
// Nmiesto zmeny cesty ku kazdemu obrazku mozeme opravit / vytvorit config.php ktory obsahuje cestu k obrazkom
$host = $_SERVER['HTTP_HOST'];
$image_path = $host.'/images/';

// Pouzit config.php v scriptoch

require 'config.php';
echo '<img_src"'.$image_path.'header.png"/>';
// cesta k obrazkom je teraz dynamicka

//Elementy $_SERVER
$_SERVER['PHP_SELF'] // filename of currently executing script
$_SERVER['SERVER_ADDR'] // IP of Host server
$_SERVER['SERVER_NAME'] // Name of Host server
$_SERVER['HTTP_HOST'] // Host header from current request
$_SERVER['REMOTE_ADDR'] // IP from where user is viewing the current page
$_SERVER['REMOTE_HOST'] // Host name from where user is viewing the current page
$_SERVER['REMOTE_PORT'] // Port used on user's machine to communicate with web_server
$_SERVER['SCRIPT_FILENAME'] // absolute pathname of currently executing script
$_SERVER['SERVER_PORT'] // Port on server machine used by web server for communication
$_SERVER['SCRIPT_NAME'] // casta k scriptu
$_SERVER['SCRIPT_URI'] // URI of current page
?>

<form action="first.php" method="ost">
    <p>Name:<input type="text" name="name"/></p>
    <p>Age:<input type="text" name="age"/></p>
    <p><input type="submit" name="submit" value="submit"/></p>
</form>
<!-- 
    Name: ___________
    Age:  ___________
    |Submit|
-->
Teraz mozeme pristupovat k premennym cez $_POST["name"] a $_POST["age"] . Data su neviditelne pre inych
Teraz mozeme pristupovat k premennym cez $_GET["name"] a $_GET["age"] . Prenasa data cez adresu stranky a vidia to vsetci
GET sa nesmie pouzivat na prenos hesiel a citlivych informacii


--------------- SESSION -------------------
Spusta sa cez session_start() function. Musi to byt prva vec pred HTML tagmy
<?php
session_start();
$SESSION['color']="red";
?>

Premenne ostavaju kym neukonci session alebo odstranim rucne session_unset()
alebo znicime session_destroy()

---------------- COOKIE ---------------------------


