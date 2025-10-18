var original = new ChargeRune(10);
var copy = original;
copy.Power = 5;
Console.WriteLine($"Original charge: {original.Power}");
Console.WriteLine($"Copied charge: {copy.Power}");

struct ChargeRune
{
    public ChargeRune(int power)
    {
        Power = power;
    }

    public int Power { get; set; }
}
