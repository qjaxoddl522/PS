#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());

        while (true)
        {
            string input = reader.ReadLine();
            if (input == null) break;
            int N = int.Parse(input);
            Recursion(N);
            writer.WriteLine();
        }

        void Recursion(int n)
        {
            if (n == 0)
            {
                writer.Write('-');
                return;
            }
            Recursion(n - 1);
            for (int i = 0; i < Math.Pow(3, n-1); i++)
                writer.Write(' ');
            Recursion(n - 1);
        }

        writer.Flush();
    }
}