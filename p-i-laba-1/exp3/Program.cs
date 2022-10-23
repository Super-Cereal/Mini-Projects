internal class User
{
    public string name { get; set; }
    public string surname { get; set; }
    public string fathername { get; set; }
    public int age { get; set; }

    public User(string name, string surname, string fathername, int age)
    {
        this.name = name;
        this.surname = surname;
        this.fathername = fathername;
        this.age = age;
    }

    public User()
    {
        this.name = "Иван";
        this.surname = "Данилов";
        this.fathername = "Степанович";
        this.age = 23;
    }

    public string fullName
    {
        get
        {
            return String.Format("{0} {1} {2}", this.surname, this.name, this.fathername);
        }
    }
}

internal class Program
{
    private static void Main()
    {
        var user = new User();
        Console.WriteLine(user.fullName);
    }
}
