#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());

        int T = int.Parse(reader.ReadLine());
        
        int FillFace(ref int remain, int cap) {
            // 채울 블록 수
            int used = Math.Min(remain, cap);

            // 한 줄 길이
            int k = (int)Math.Floor(Math.Sqrt(used));
            // 이 줄이 양쪽 면에 노출될 면 수
            int added = k * 2;

            // 남은 블록으로 개별 칸 채우기
            int extra = used - k * k;
            if (extra > 0) {
                added += 1;
                if (extra > k) added += 1;
            }

            remain -= used;
            return added;
        }

        for (int i = 0; i < T; i++)
        {
            int N = int.Parse(reader.ReadLine());
            int c = (int)Math.Floor(Math.Cbrt(N));

            int ans = c * c * 3;
            int remain = N - c * c * c;

            ans += FillFace(ref remain, c * c);  // 첫 번째 면
            ans += FillFace(ref remain, c * c);  // 두 번째 면

            // 두 면 사이 줄 먼저 채우기
            if (remain > 0)
            {
                ans += 1;
                remain = Math.Max(0, remain - c);
            }

            // 상단 면 채우기
            ans += FillFace(ref remain, int.MaxValue);

            writer.WriteLine(ans * 2);
        }

        writer.Flush();
    }
}