try
{
    ThrowSwampError();
}
catch (InvalidOperationException)
{
    Console.WriteLine("Handled specific swamp hiccup.");
}
catch (Exception)
{
    Console.WriteLine("Handled generic issue.");
}

static void ThrowSwampError()
{
    throw new InvalidOperationException("Mud refused to stay put.");
}
