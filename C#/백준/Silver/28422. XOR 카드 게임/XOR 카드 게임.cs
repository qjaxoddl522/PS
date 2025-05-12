#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());
        
        int N = int.Parse(reader.ReadLine());
        int[] A = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);

        int Count(int a) {
            int cnt = 0;
            while (a != 0)
            {
                a &= a - 1;
                cnt++;
            }
            return cnt;
        }

        int[] dp = new int[N+1];
        if (N >= 2)
            dp[2] = Count(A[0] ^ A[1]);
        if (N >= 3)
        dp[3] = Count(A[0] ^ A[1] ^ A[2]);
        for (int i = 4; i <= N; i++) {
            dp[i] = dp[i-2] + Count(A[i-2] ^ A[i-1]);
            if (i >= 5)
                dp[i] = Math.Max(dp[i], dp[i-3] + Count(A[i-3] ^ A[i-2] ^ A[i-1]));
        }
        writer.WriteLine(dp[N]);

        writer.Flush();
    }
}