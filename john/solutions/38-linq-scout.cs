var rooms = new[] { "Calm Coral Council", "Noisy Eel Briefing", "Calm Bubble Pod" };
var calmRooms = System.Linq.Enumerable.Where(rooms, room => room.Contains("Calm"));
foreach (var room in calmRooms)
{
    Console.WriteLine(room);
}
