using System;

class Program
{
    static void Main()
    {
        try
        {
            int potency = int.Parse(Console.ReadLine() ?? "0");

            if (potency > 9)
            {
                throw new InvalidOperationException("Potion imploded");
            }

            if (potency < 0)
            {
                throw new ArgumentOutOfRangeException(nameof(potency), "Potency cannot drop below zero.");
            }

            Console.WriteLine($"Potion stable at intensity {potency}.");
        }
        catch (ArgumentOutOfRangeException)
        {
            Console.WriteLine("Negative potency! The swamp refuses backward bubbles.");
        }
        catch (InvalidOperationException ex)
        {
            Console.WriteLine(ex.Message);
        }
        catch (Exception)
        {
            Console.WriteLine("Mysterious fizz detected. Log a bug with the frogs.");
        }
        finally
        {
            Console.WriteLine("Workbench sanitized.");
        }
    }
}
