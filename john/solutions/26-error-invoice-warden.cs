using System;

class Program
{
    static void Main()
    {
        string input = Console.ReadLine() ?? string.Empty;

        try
        {
            string[] parts = input.Split('|', 2, StringSplitOptions.TrimEntries);
            string amountPart = parts.Length > 0 ? parts[0] : string.Empty;
            string description = parts.Length > 1 ? parts[1] : "Unknown charge";

            if (!decimal.TryParse(amountPart, out decimal amount))
            {
                throw new InvalidInvoiceException("Amount could not be parsed.");
            }

            Console.WriteLine($"Processed amount {amount:F2} for {description}");
        }
        catch (InvalidInvoiceException ex)
        {
            Console.WriteLine($"Invoice error: {ex.Message}");
        }
        finally
        {
            Console.WriteLine("Ledger updated.");
        }
    }
}

class InvalidInvoiceException : Exception
{
    public InvalidInvoiceException(string message) : base(message)
    {
    }
}
