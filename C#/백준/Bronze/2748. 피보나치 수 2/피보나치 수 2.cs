#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());

        int N = int.Parse(reader.ReadLine());
        long prev = 0; long now = 1;
        for (int i = 1; i < N; i++)
        {
            long temp = now;
            now += prev;
            prev = temp;
        }
        writer.WriteLine(N > 0 ? now : 0);

        writer.Flush();
    }
}