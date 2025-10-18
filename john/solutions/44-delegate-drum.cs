Chant caster = name => $"Rise, {name}!";
Console.WriteLine($"Chanting: {caster("Debugsworth")}");

delegate string Chant(string name);
