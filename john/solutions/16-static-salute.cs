Console.WriteLine(QuestPlanner.BuildCheer("Labyrinth"));

static class QuestPlanner
{
    public static string BuildCheer(string biome)
    {
        return $"Fanfare for {biome} launched!";
    }
}
