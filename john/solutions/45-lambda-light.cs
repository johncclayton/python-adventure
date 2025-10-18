Action wave = () => Console.WriteLine("Waving to the crowd!");
wave();
Func<int, int> doubleSparkles = amount => amount * 2;
Console.WriteLine($"Doubled sparkles: {doubleSparkles(4)}");
