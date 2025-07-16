#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());

        int N = int.Parse(reader.ReadLine());
        ulong[] A = Array.ConvertAll(reader.ReadLine().Split(), ulong.Parse);

        ulong ans = 0;
        for (int i = 0; i < N - 1; i++)
        {
            ulong[] B = Array.ConvertAll(reader.ReadLine().Split(), ulong.Parse);
            ans += A[0] * B[1] + A[1] * B[0];
            A = new ulong[] { A[0] + B[0], A[1] + B[1] };
        }
        writer.WriteLine(ans);

        writer.Flush();
    }
}