var vault = new AccessVault("frog-harmony");
Console.WriteLine(vault.Reveal());

class AccessVault
{
    private readonly string _secret;

    public AccessVault(string secret)
    {
        _secret = secret;
    }

    public string Reveal() => $"Vault whispers: {_secret}";
}
