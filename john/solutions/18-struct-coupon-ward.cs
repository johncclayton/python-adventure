using System;

class Program
{
    static void Main()
    {
        var coupon = new SnackCoupon("CRUNCH-7", 2, 3.50m);
        var after = coupon.Redeem();

        Console.WriteLine($"Before: {coupon.Code} -> Uses {coupon.UsesRemaining}");
        Console.WriteLine($"After: {after.Code} -> Uses {after.UsesRemaining}");
    }
}

public readonly struct SnackCoupon
{
    public SnackCoupon(string code, int usesRemaining, decimal value)
    {
        Code = code;
        UsesRemaining = usesRemaining;
        Value = value;
    }

    public string Code { get; }

    public int UsesRemaining { get; }

    public decimal Value { get; }

    public SnackCoupon Redeem()
    {
        int newUses = UsesRemaining > 0 ? UsesRemaining - 1 : 0;
        return new SnackCoupon(Code, newUses, Value);
    }
}
