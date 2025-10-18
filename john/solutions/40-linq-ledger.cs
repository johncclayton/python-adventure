var loot = new[] { 5, 1, 3 };
var sorted = System.Linq.Enumerable.OrderBy(loot, value => value).ToArray();
int total = System.Linq.Enumerable.Sum(sorted);
Console.WriteLine($"Sorted loot: {string.Join(", ", sorted)}");
Console.WriteLine($"Total sparkle: {total}");
