var beats = new[] { 1, 2, 3 };
var chants = System.Linq.Enumerable.Select(beats, beat => $"Beat {beat} ready");
foreach (var chant in chants)
{
    Console.WriteLine(chant);
}
