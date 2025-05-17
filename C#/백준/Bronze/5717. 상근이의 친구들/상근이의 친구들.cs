#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());

        while (true) {
            int[] input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
            if (input[0] == 0 && input[1] == 0) break;
            writer.WriteLine(input[0] + input[1]);
        }

        writer.Flush();
    }
}