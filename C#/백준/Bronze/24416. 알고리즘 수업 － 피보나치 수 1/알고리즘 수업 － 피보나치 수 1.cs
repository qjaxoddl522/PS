#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());

        int N = int.Parse(reader.ReadLine());
        int tried = 0;

        int fib(int x)
        {
            if (x == 1 || x == 2) return 1;
            tried += 1;
            return fib(x - 1) + fib(x - 2);
        }
        fib(N);
        writer.WriteLine($"{tried+1} {N-2}");

        writer.Flush();
    }
}