using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Vehicle
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 89;
            Console.WriteLine(x);
        }
    }
}

Console.WriteLine("x = {0}; y = {1};", x, y);

string yourName;
yourName = Console.RaedLine();
int age = Convert.ToInt32(Console.RaedLine());
Console.WriteLine("You are {0} years old", age);

n = ConvertToDouble("77");
// Comment single line
/* 
Multiline Comment
*/

var num = 15; // Ak hodnotu dostane na zaciatku pride na to sam akeho je typu
const double PI = 3.14 // Konstanta, hodnota sa neda zmenit neskor

// 16/5 = 3  Delenie dvoch int je cele cislo
x += 1
x++ //  ako x+=1, funguje aj ako prefix a postfix
x -= 1
x *= 1
x /= 1
x %= 5  // Modulus, zvysok po deleni

int x=3;
int y = ++x // y=4 x=4  prefix increment value then expression
int y = x++ // y=3 x=4  expression, than increment value
// -- funguje podobne

// nepouziva & namiesto toho + bez medizer
Console.WriteLine(x+" "+y); // 4 3

// ------------- Conditionals and Loops -----------------------
if(podmienka) // < > >= <= == !=
{
    // ak len 1 riadok, nepotrebuje {}
}

if(podmienka)
{}
else if (podmienka)
{}
else
{}

switch // elegantny if
int age = 88;
switch(age){
    case 16:
        // to do
        break;
    case 42:
        break;
    default:
        break;
}

int num = 1;
while (num++ < 6){
    //stuff, pojde viac krat ako ++num
}

for(init; condition; increment){}

for(int x=10; x<15; x++) {}

for(int x=10; x>0; x-=2) {}

int x=10;
for(; x>0; ) {
    x-=2;
    }

// do-while - ako while ale prebehne aspon raz pretoze najprv vykona a potom testuje podmienku
int a=0;
do{
    a++;
} while (a<5);

break; a continue; ako v pythone

// Logice operatori
&& and
|| or
! not

// ? elegantne if
if(podmienka)
    msg = "A"
else
    msg = "B"

msg = (podmienka) ? "A": "B";

// ------------------ METHODS -------------------------------
int Sqr(int x)
    {
        int result = x*x
        return result;
    }

// ak nevracia nic tak definujeme static void
static void Meno()
{}

Meno();

int Sum (int x, int y=2)
{
    return x+y;
}
//mozme volat aj takto
Sum(y:4, x:3);

// ref tells the compiler that the object is initialized before entering the function, ref is two-ways,  // tipujem, ze ref upravuje global premennu
public void myFunction(ref MyClass someClass)
// out tells the compiler that the object will be initialized inside the function. out is out-only. // a out premenna existuje len pocas behu funkcie
public void myFunction(out MyClass someClass)

// Method Overlad - Ak vytvoris viac method s rovnakym menom, C# ich rozlisuje podla argumentov (int, double, boolean...) C# hlasi chybu ak vytvoris
// metody s rovnakymi premennymi

// Recursion, ked metoda vola samu seba. Napr vypocet Faktorial
static internal Fact(int num){
    if(num==1){
        return 1;
    }
    return num*Fact(num-1);
}

// -----------  Classes & Objects -------------------------------------

//Encapsulation - skryva balance od okolyteho kodu, da sa menit len cez Deposit a Withdraw a citat s GetBalance
class BankAccount{
    private double balance = 0
    public void Deposit(double n){
        balance+=n
    }
    public void Withdraw(double n){
        balance-=n
    }
    public double GetBalance(){
        return balance;
    }
}

BankAccount b = new BankAccount;
b.Deposit(100);
b.Withdraw(40);
Console.WriteLine(b.GetBalance)


// ------------------- Arrays & Strings ----------------------------------
int [] nyArray = new int[5]; // pocet clenov
myArray[0] = 23; // [23, 0, 0, 0, 0]

string [] names = new string[3]{"John", "Paul", "Bob"};
// Loop through Array
for(int k=0; x<10; k++) {
    myArray[k] = 3;
}
foreach(int k in myArray){}

// 2 dim array
type [,] name = new type [size, size]
int[,] name = {{2,3}, {5,6}, {2,7}};

// Jagged Array - Pole poli - Kazde pole moze mat vlastnu dlzku

int[][] jaggedArray = new int[3][]; // 3 podpolia
int[][] jaggedArray = new int[][]{
    new int[]{1, 2, 3, 5, 8},
    new int[]{1, 5, 9, },
    new int[]{1, 22, 3, 51, 8, 13}
};
jaggedArray.Length // pocet clenov
jaggedArray.Rank    // pocet dimenzii
jaggedArray.Max     // max val
jaggedArray.Min     // min val
jaggedArray.Sum     // sucet clenov

// --------------------------------- STRING ------------------------
a = "abc"
a.Length = 3
a.IndexOf("b") // kde sa 'b' vyskytuje
a.Inset(index, "text")
a.Remove(index) // odstrani text za index
a.Replace("a", "b")
a.Substring(x, dlzka) //retazec od miesta x s dlzkou
a.Contains("abc") // true/false

String.Concat(s1, s2);  // Skombinuje stringy
String.Equals(s1, s2);  // ak niesu rovnake, false


// --------------------------- More on Classes -----------------------
//Destructor  - uvolnuje pamat
// Volame ~MenoTriedy(){some code}

// Dalsie staticke metody -----------------
Math.PI
Math.E
Math.Max()  / vacsie z dvoch cisel
Math.Min()
Math.Abs()
Math.Sin()
Math.Cos()
Math.Pow() // x*x*x
Math.Sqrt() // odmocnina
Math.Round()

int[] arr {1, 2, 3};
nyArray.Reverse(arr) // {3, 2, 1}
nyArray.Sort(arr) // {1, 2, 3}

DateTime.Now
DateTime.Today
DateTime.DaysInMonth(2016, 2); // 29

this // podobne ako Me vo VB. Sluzi na rozlisenie "svojich" a "cudzich" premennych
readonly // ako const ale const je napevno navzdy. readonly sa da menit za urcitych okolnosti. Moze menit constructor
const // musi mat hned priradenu hodnotu, nemoze byt vysledkom vypoctu, neda sa menit

// ------------- Operator overloading -----------------
// Mozeme pretazit operator (+ - * / < > =)
public static Box operator + (Box a, Box b){
    int h = a.Height + b.Height;
    int w = a.Width + b.Width;
    Box res = new Box (h, w);
    return res;
}

static void Main (string [] args) {
    Box b1 = new Box (14,3);
    Box b2 = new Box (5,7);
    Box b3 = b1 + b2; // b3.Height=19, b3.Width=10
}

// ---------------- Inheritance and Polymorphism -----------------
class Person{}

class Student: Person{} // Student moze pouzivat metody Person (Inheritance)

Public // moze byt pristupovane zovsadial
Private // Iba z vnutra triedy
Protected // aj z odvodenych tried
Sealed class Animal{}  // Ine triedy ju nemozu inherit a pouzivat jej metody

// Polymorphism - Viac tried pouziva nadtriedu roznmym sposobom 

class Shape{
    public virtual void Draw(){
        Console.Write("Base Draw");
    }
}// Metoda Draw bude prepisana ked budeme pouzivat metody inych tried

class Rectangle:Shape{
    public override void Draw()
    {
        Console.Write("Base Draw");
        //base.Draw(); netusim VS Code to sem hodil
    }
} // Trieda Rectangle metoda Draw prepise metodu triedy Shape. Klucove slova VIRTUAL a OVERRIDE

// Abstract Class
abstract class Shape {
    public abstract void Draw();
} // Abstraktne metody nepotrebuju mat kod. Kod do nej implementuju az triedy ktore ju pouziju cez OVERRIDE

// Interface - kompletne abstraktna trieda
public interface IShape {  // pismeno I na zaciatok, nemusime pisat abstract vsade
    void Draw();
} // Pri implementovani interfacu musime zadefinovat vsetky metody
class Circle: IShape{
    public void Draw(){
        // nemusime pouzit OVERRIDE
    }
} // Class can inherit from just one base class, but can implement multiple interfaces


Namespace Vehicle{  // volame na zaciatku kodu ako python import. using Vehicle; using System; using Sytem.Text;
    class Program{
        static void Main(string[]args){}
    }
}

// ---------------- Structs, Enums, Exceptions, Files ----------------------------
//Struct moze obsahovat metody, properties, indexers...
// constructor thjat can take parameter
Struct Point {
    public int x;
    public int y;
    public Point (int x, int y){
        this.x = x;
    }
}
Point p = new Point(10,15);

// Enums - pouziva sa na mena mesiacov, dni v tyzdni, karty v bal
enum Days{Mon, Tue, Wed, Thu=10, Fri, Sat, Sun};
/*
Mon=0 Wed=2 Thu=10 Fri=11 Sat=12
int x = (int)Days.Tue  // x=1
*/

// --------------- Exceptions ----------------------
try{
    int[] arr = new int[]{4, 5, 8};
    Console.Write(arr[8]); // 2 je max
}
catch(Exception e){
    Console.WriteLine(e.Message); // napise chybovu hlasku ak je chyba
}
// ak je viac chyb, treba umiestnit viac catch(DivideByZeroException e){}  catch kodov/blokov
finally{
    //Tento kod sa spusti bez ohladu na to ci bola chyba alebo nie.
}

// -------------- Files System.IO --------------------
string  str="nejaky text";
File.WiriteAllText("test.txt", str); // napise obsah str do suboru

AppendAllText() // vlaozi teext na koniec suboru
Create() // Vytvori subor
Delete() // Zmaze
Exists() // test ci existuje, True/False
Copy()
Move()
// Vsetky metody po skonceni zavru subor

// ------------------------ Generics ------------------------------
// mozeme navrhnut metodu ktora vymeni 2 premenne
Static void Swap (ref int a, ref int b){} // funguje len s int premennymi
Static void Swap <T>(ref Ta, ref Tb){} // funguje s viac premennymi ale musia byt rovnakeho typu. T sa pouziva pre generic type
Static void Swap <T,U>(Tx, Uy){} // x a y mozu byt rozne typy, napr integer a double

// ------------- Collections ---------------------------
// .NET framework provides number of generic collection classes. Usefull of storing and maniulating data.
// These are contained in:System.Collections.Generic namespace.List

List<string>colors = new List<string>();
colors.Add("Red"); // - prida "Red" do Listu
colors.Clear  // zmaze obsah
colors.Contains // ci list obsahuje hodnotu
colors.Count // pocet clenov
colors.Insert // vlozi element na konkretne miesto
colors.Reverse  // obrati poradie
// List - sa moze zvacsovat/zmansovat dynamicky na rozdiel od pola.



