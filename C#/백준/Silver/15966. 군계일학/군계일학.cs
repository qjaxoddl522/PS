#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());

        int N = int.Parse(reader.ReadLine());
        int[] A = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);

        int ans = 0;
        int[] dp = new int[1000001];
        foreach (int a in A)
        {
            dp[a] = Math.Max(dp[a], dp[a - 1] + 1);
            ans = Math.Max(ans, dp[a]);
        }
        writer.WriteLine(ans);

        writer.Flush();
    }
}